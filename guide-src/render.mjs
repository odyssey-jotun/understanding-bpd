// Renders each guide HTML to PDF, vertically justified.
//
// Vertical justification pass.
//
// Chromium pools a page's leftover vertical space at the foot. This shares that
// slack out between the blocks on the page instead, so the last block lands near
// the bottom margin rather than leaving a hole.
//
// It works off the real printed output, not a layout approximation: render a probe
// PDF, then let justify_measure.py say which blocks sit on which page (matching the
// page's opening words) and how much slack each page really has (lowest ink in the
// rendered bitmap, which catches photographs and filled panels that text extraction
// misses). Then apply the margins and render for real.
//
// A heading, its eyebrow and its rule are one cluster and never get pushed apart.
// Where a block is simply too big to fit the space left, the leftover hole is a
// content problem, not a spacing one; the report says so rather than stretching
// gaps to absurd sizes.
import { chromium } from 'playwright';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'child_process';
import { readFileSync, writeFileSync, mkdtempSync } from 'fs';
import { tmpdir } from 'os';

const D = dirname(fileURLToPath(import.meta.url));
const OUT = join(D, '..', 'downloads');
const GUIDES = ['BPD_Overview', 'bpd_patient_guide_v6', 'bpd_loved_ones_guide_v2'];
const work = mkdtempSync(join(tmpdir(), 'justify-'));

const browser = await chromium.launch();

for (const name of GUIDES) {
  const page = await browser.newPage({ viewport: { width: 1200, height: 1000 } });
  await page.goto(`file://${join(D, name)}.html`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);

  const blocks = await page.evaluate(() => {
    const SEL = 'section.block > *, section.refs > *, body > figure';
    const flow = [...document.querySelectorAll(SEL)]
      .filter(el => !el.closest('.cover') && !el.closest('.about'));
    const HEAD = el => el.matches('.kicker, h2, h3, .rule');
    // The last page of a run, just before a forced break such as the About page,
    // is allowed to finish short. That is normal typography, not a defect.
    const breaks = [...document.querySelectorAll('.about, section.refs')];
    const runEnd = new Set();
    for (const br of breaks) {
      const before = flow.filter(el =>
        el.compareDocumentPosition(br) & Node.DOCUMENT_POSITION_FOLLOWING);
      if (before.length) runEnd.add(before[before.length - 1]);
    }
    if (flow.length) runEnd.add(flow[flow.length - 1]);
    return flow.map((el, i) => {
      el.setAttribute('data-j', i);
      const prev = el.previousElementSibling;
      return {
        j: i,
        text: (el.textContent || '').slice(0, 400),
        eligible: !HEAD(el) && !(prev && HEAD(prev)),
        runEnd: runEnd.has(el),
      };
    });
  });

  const probe = join(work, `${name}.probe.pdf`);
  const bjson = join(work, `${name}.blocks.json`);
  const gjson = join(work, `${name}.gaps.json`);
  const pdfOpts = { format: 'Letter', printBackground: true, preferCSSPageSize: true };

  await page.pdf({ path: probe, ...pdfOpts });
  writeFileSync(bjson, JSON.stringify(blocks));

  console.log(`${name}:`);
  const log = execFileSync('python3', [join(D, 'justify_measure.py'), probe, bjson, gjson],
                           { encoding: 'utf8' });
  process.stdout.write(log);

  const { plan } = JSON.parse(readFileSync(gjson, 'utf8'));
  const css = Object.entries(plan)
    .map(([j, px]) => `[data-j="${j}"]{margin-top:${px}px !important}`).join('\n');
  if (css) { await page.addStyleTag({ content: css }); await page.waitForTimeout(250); }

  await page.pdf({ path: join(OUT, `${name}.pdf`), ...pdfOpts });
  await page.close();
}
await browser.close();
