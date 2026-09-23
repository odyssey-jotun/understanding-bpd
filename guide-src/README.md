# Guide PDF source

The three PDFs in `../downloads/` are generated from these files. Edit here, rebuild,
and commit the PDFs. Do not hand-edit the PDFs.

## Rebuild

```
python3 make.py          # writes the three .html files next to this README
node render.mjs          # prints them into ../downloads/, vertically justified
```

`render.mjs` needs Playwright and calls `justify_measure.py`, which needs
`pdftotext` and `pdftoppm` (poppler) and Pillow. There is no Playwright copy in
this repo, so run it from a directory that has one, or `npm i playwright` here.

## Files

| File | What it is |
| --- | --- |
| `css.py` | The whole stylesheet. Palette and typefaces match `../index.html`. |
| `build.py` | Page scaffolding: the cover, the shared **Meet Marley** page, works cited. |
| `g1.py` `g2.py` `g3.py` | One per guide: body copy, references, cover title and image. |
| `make.py` | Assembles each guide into a single HTML file. |
| `render.mjs` | Prints the HTML to PDF and evens out the page spacing. |
| `justify_measure.py` | Works out each page's slack from the real printed output. |
| `img/` | Photography, JPEG, capped at 1100px. |

## Two things that will trip you up

**Body pages print on white on purpose.** Chromium never paints the `@page` margin box,
so a tinted `body` renders as a colour block floating on a white sheet, with white
gutters down the edges. The brand colour is carried by the full-bleed cover and About
page, which set `page: fullbleed` and their own background. Do not "fix" this by
tinting the body.

**Images are JPEG, not PNG.** The originals from Marley are ~700KB PNGs each. Embedded
losslessly they pushed each PDF over 4MB. At JPEG quality 82 and 1100px they are 40-100KB
and the PDFs land around 650KB.

## Why the render has two passes

Chromium dumps a page's leftover vertical space in one lump at the foot, so pages
finish early and look unfinished. `render.mjs` prints a probe PDF first, measures
it, then prints the real one with the slack shared out between the blocks on each
page.

The measurement is taken from the printed output rather than from the DOM, because
layout in the browser is not the layout on the page. `justify_measure.py` matches
the opening words of each PDF page against the block text to learn which blocks
landed where, and finds the lowest ink in a bitmap of each page to learn how much
room is left. Text extraction alone would miss photographs and filled panels.

Three rules keep it honest:

- **A heading, its eyebrow and its rule are one cluster** and never get pushed
  apart. Air inside a heading cluster reads as a broken layout.
- **The last page of a run is left alone.** A section finishing halfway down the
  page before the About page is ordinary typography, not a fault.
- **One pass only.** Adding space can push a block onto the next page, opening a
  bigger hole that attracts more space. Iterating was tried and diverges.

Where a page still finishes short, the run log says so. That means a block is too
big to fit the space left, which is a content problem: move it, shrink it, or let
it break. No amount of spacing fixes it.

## The About page

`ABOUT` in `build.py` is the same on all three guides and mirrors the `#about` section of
`../index.html`. If Marley's bio changes on the site, change it here too and rebuild.
