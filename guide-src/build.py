# -*- coding: utf-8 -*-
import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from css import CSS

SITE = "odyssey-jotun.github.io/understanding-bpd"

ABOUT_T = """
<div class="about">
  <div class="about-inner">
    <div class="about-photo">
      <img src="img/marley.jpg" alt="Marley Spraggins, standing outdoors at golden hour, smiling">
    </div>
    <div class="about-body">
      %(kicker)s
      <h2>Meet Marley</h2>
      <div class="rule"></div>
      <p class="name-line">This project started with one family trying to make sense of a
      diagnosis.</p>
      <p>Marley grew up inside a family where emotions ran high and nobody had a word for
      why. That question led her to spend a summer buried in clinical research on borderline
      personality disorder, and to build this series of guides for other families doing the
      same thing hers did.</p>
      <p>Each guide is written from the peer-reviewed literature rather than from anecdote,
      and every claim is traceable to the sources listed at the back. They are free, and they
      are meant to be shared with the people who need them.</p>
      <div class="about-quote">
        <p>&ldquo;Nobody in my family had the language for what was happening. These guides
        are the thing I wish someone had handed us.&rdquo;</p>
      </div>
    </div>
  </div>
  <div class="about-foot">
    <span class="mark">Understanding <em>BPD</em></span>
    <span>%(foot)s %(site)s</span>
  </div>
</div>
"""

def about(kicker='<p class="kicker">About the guide</p>', foot="All three guides are free at",
          body=None):
    html = ABOUT_T % {"kicker": kicker, "foot": foot, "site": SITE}
    if body:
        # Swap the third-person bio for one the author wrote in her own voice.
        start = html.index('<h2>Meet Marley</h2>')
        end = html.index('</div>\n  </div>\n  <div class="about-foot">')
        html = html[:start] + body.strip() + "\n    " + html[end:]
    return html

ABOUT = about()

def cover(kicker, title, sub, img):
    return """
<div class="cover">
  <div class="cover-top">
    <p class="wordmark">Understanding <em>BPD</em></p>
    %s
    <h1>%s</h1>
    <p class="sub">%s</p>
  </div>
  <div class="cover-img"><img src="img/%s" alt=""></div>
  <div class="cover-foot">
    <span class="by">Marley Spraggins</span>
    <span class="site">%s</span>
  </div>
</div>""" % (('<p class="kicker">%s</p>' % kicker) if kicker else '', title, sub, img, SITE)

def refs(items, note, kicker="Sources", cls=""):
    lis = "\n".join("    <li>%s</li>" % i for i in items)
    return """
<section class="refs%s">
  %s
  <h2>Works cited</h2>
  <div class="rule"></div>
  <ol>
%s
  </ol>
  <p class="note">%s</p>
</section>""" % ((" " + cls) if cls else "", ('<p class="kicker">%s</p>' % kicker) if kicker else '', lis, note)

def page(title, body):
    return """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Karla:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>%s</style></head><body>
%s
</body></html>""" % (title, CSS, body)
