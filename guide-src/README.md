# Guide PDF source

The three PDFs in `../downloads/` are generated from these files. Edit here, rebuild,
and commit the PDFs. Do not hand-edit the PDFs.

## Rebuild

```
python3 make.py          # writes the three .html files next to this README
node render.mjs          # prints them into ../downloads/
```

`render.mjs` needs Playwright. There is no copy in this repo, so run it from a
directory that has one, or `npm i playwright` here first.

## Files

| File | What it is |
| --- | --- |
| `css.py` | The whole stylesheet. Palette and typefaces match `../index.html`. |
| `build.py` | Page scaffolding: the cover, the shared **Meet Marley** page, works cited. |
| `g1.py` `g2.py` `g3.py` | One per guide: body copy, references, cover title and image. |
| `make.py` | Assembles each guide into a single HTML file. |
| `render.mjs` | Prints the HTML to PDF. |
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

## The About page

`ABOUT` in `build.py` is the same on all three guides and mirrors the `#about` section of
`../index.html`. If Marley's bio changes on the site, change it here too and rebuild.
