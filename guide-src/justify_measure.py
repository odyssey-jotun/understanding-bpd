"""Works out how much slack each printed page has, and which blocks sit on it.

Ground truth comes from the rendered PDF, not from a layout approximation:
  * pdftotext -bbox says which words land on which page, so matching the first
    words of each page against the block text tells us where each page starts.
  * pdftoppm renders each page so we can find the lowest ink on it. Text
    extraction alone would miss photographs and filled panels.

Usage: justify_measure.py probe.pdf blocks.json gaps.json
"""
import json, re, subprocess, sys, tempfile, os, glob
from xml.etree import ElementTree
from PIL import Image

PT_PER_IN = 72.0
BOTTOM_MARGIN_IN = 0.75
DPI = 50
MAX_GAP = 96.0          # px at 96dpi, ceiling for any single gap
MIN_SLACK = 24.0

norm = lambda s: re.sub(r'[^a-z0-9 ]', ' ', s.lower())
squash = lambda s: re.sub(r'\s+', ' ', s).strip()

def page_words(pdf):
    xml = subprocess.run(['pdftotext', '-bbox', pdf, '-'],
                         capture_output=True, text=True).stdout
    xml = re.sub(r'\sxmlns="[^"]+"', '', xml, count=1)
    root = ElementTree.fromstring(xml)
    out = []
    for pg in root.iter('page'):
        words = [(w.text or '', float(w.get('yMax'))) for w in pg.iter('word')]
        out.append({'height': float(pg.get('height')), 'words': words})
    return out

def last_ink(pdf):
    """Lowest non-paper pixel per page, in points."""
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', str(DPI), '-png', pdf, os.path.join(tmp, 'p')],
                   check=True, capture_output=True)
    rows = []
    for f in sorted(glob.glob(os.path.join(tmp, 'p-*.png')),
                    key=lambda f: int(re.search(r'p-(\d+)', f).group(1))):
        im = Image.open(f).convert('L'); w, h = im.size; px = im.load()
        y = 0
        for yy in range(h - 1, -1, -1):
            if min(px[x, yy] for x in range(0, w, 3)) < 235:
                y = yy; break
        rows.append(y / DPI * PT_PER_IN)          # px -> points
    return rows

def main(pdf, blocks_path, out_path):
    blocks = json.load(open(blocks_path))
    for b in blocks:
        b['n'] = squash(norm(b['text']))
    pages = page_words(pdf)
    inks = last_ink(pdf)

    # Find the first flow block on each page by matching its opening words.
    starts, cursor = {}, 0
    for pi, pg in enumerate(pages):
        words = [squash(norm(w)) for w, _ in pg['words'][:8] if squash(norm(w))]
        if not words:
            continue
        for take in (6, 5, 4, 3):
            needle = ' '.join(words[:take])
            if len(needle) < 8:
                continue
            hit = next((i for i in range(cursor, len(blocks))
                        if needle in blocks[i]['n']), None)
            if hit is not None:
                starts[pi] = hit; cursor = hit; break

    # Turn page starts into page -> block ranges.
    ordered = sorted(starts.items())
    plan, report = {}, []
    for k, (pi, first) in enumerate(ordered):
        last = ordered[k + 1][1] - 1 if k + 1 < len(ordered) else len(blocks) - 1
        if last < first:
            continue
        page_h = pages[pi]['height']
        content_bottom = page_h - BOTTOM_MARGIN_IN * PT_PER_IN
        slack_pt = content_bottom - inks[pi]
        slack_px = slack_pt / PT_PER_IN * 96.0
        on_page = [b for b in blocks[first:last + 1]]
        if any(b.get('runEnd') for b in on_page):
            report.append({'page': pi + 1, 'slack': round(slack_px), 'gaps': 0,
                           'each': 0, 'run_end': True})
            continue
        openable = [b for b in on_page[1:] if b['eligible']]
        if slack_px < MIN_SLACK or not openable:
            report.append({'page': pi + 1, 'slack': round(slack_px), 'gaps': 0, 'each': 0})
            continue
        share = min(slack_px / len(openable), MAX_GAP)
        for b in openable:
            plan[str(b['j'])] = round(share, 2)
        report.append({'page': pi + 1, 'slack': round(slack_px), 'gaps': len(openable),
                       'each': round(share), 'left': round(slack_px - share * len(openable))})

    json.dump({'plan': plan, 'report': report}, open(out_path, 'w'), indent=1)
    for r in report:
        if r['gaps']:
            note = f"  ({r['left']}px left over)" if r.get('left', 0) > 50 else ''
            print(f"   page {r['page']:>2}: {r['slack']:>4}px slack -> {r['gaps']} gaps x {r['each']}px{note}")
        elif r.get('run_end'):
            print(f"   page {r['page']:>2}: {r['slack']:>4}px slack, end of a run, left alone")
        elif r['slack'] > 80:
            print(f"   page {r['page']:>2}: {r['slack']:>4}px slack, no eligible gap")

if __name__ == '__main__':
    main(*sys.argv[1:4])
