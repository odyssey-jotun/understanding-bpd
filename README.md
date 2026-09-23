# Understanding BPD

Landing site for Marley Spraggins' passion project: three free, research-informed guides to borderline personality disorder for individuals, families, and loved ones.

## Live site

**https://odyssey-jotun.github.io/understanding-bpd/**

Live. The repository is public and GitHub Pages serves `main` at root, the same
setup used by `kindled-movement` and `woven`. Pushing to `main` redeploys.

The page is still `noindex,nofollow` on purpose. Being reachable is not the same as
being findable: the three guide PDFs are missing, so search traffic would land on
download buttons that 404. Flip the robots meta in `index.html` once the PDFs are in.

`index.html` is the single source of truth. There is no hosted copy of the page
anywhere else, so there is nothing that can drift out of sync with it.

## The guides

All three are in `downloads/` and live on the site. Direct links:

| Guide | File | Live link |
| --- | --- | --- |
| 1. Overview, Characteristics, and Causes | `downloads/BPD_Overview.pdf` | https://odyssey-jotun.github.io/understanding-bpd/downloads/BPD_Overview.pdf |
| 2. So You (Think) You Have BPD? | `downloads/bpd_patient_guide_v6.pdf` | https://odyssey-jotun.github.io/understanding-bpd/downloads/bpd_patient_guide_v6.pdf |
| 3. So Someone You Love (Might Have) BPD? | `downloads/bpd_loved_ones_guide_v2.pdf` | https://odyssey-jotun.github.io/understanding-bpd/downloads/bpd_loved_ones_guide_v2.pdf |

Guide three is now fifteen pages (expanded 2026-09-23). Guides one and two are six and
seven pages and have not been expanded yet. US Letter, 650KB to 1MB.

Guide three carries the components the other two do not have yet: `.ladder` (the six
levels of validation), `.script` (instead-of/try dialogue cards), `.flow` (the ordered
decision steps), `.check` (the caregiver self-check), `.twocol` panels and `figure.diagram`
(inline SVG). They all live in `guide-src/css.py` and are ready to reuse.

The three drawn diagrams in guide three are hand-written inline SVG, not images, so
they stay sharp at any zoom and cost nothing in file size. The indigo ramp on the
validation staircase is an ordinal ramp: one hue, light to dark, checked for monotone
lightness, step separation and contrast against white paper before use. The distress
curve is labelled as a schematic on its face because it carries no measured data.

### How they are built

The PDFs are generated, not hand-made. Source is in `guide-src/`, with its own README:
one shared stylesheet, one content file per guide, and a Playwright script that prints
each to PDF. Each guide runs cover, body, **Meet Marley**, works cited. The About page is
identical in all three and mirrors the `#about` section of `index.html`, so edit both
together. Do not hand-edit the PDFs; change the source and rebuild.

They use the site's palette and both site typefaces. Body pages print on white on
purpose: Chromium never paints the `@page` margin box, so a tinted body renders as a
colour block floating on a white sheet. The colour is carried by the full-bleed cover
and About page instead.

Still worth doing before these are promoted anywhere:

- **Rename guides two and three.** `v6` and `v2` are draft version numbers and they are
  now permanent public URLs.
- **Entries 9 and 10 in guide one** are listed by title because the source carried no
  named author. Confirm them with Marley.

## Status

The site is live and the download buttons work. Two things are still open.

### 1. The page is still `noindex,nofollow`

Deliberate. The Arkansas citations below are not settled, and the page leads with those
figures. Flip the robots meta in `index.html` once they are.

### 2. Two Arkansas sources need full citations

The page carries a numbered Works Cited section. Five of the seven entries are complete.
Two are titles only, taken from Marley's research notes, and need her to supply publisher
and date:

- **[5]** Time Wellness Arkansas, *Arkansas mental health statistics*
- **[6]** *Nearly one in three Arkansans report symptoms of depression*

One claim is cited but still unverified against the source: **[7]** Guillen et al. (2024)
on Family Connections reducing caregiver burden.

Note that the guide PDFs cite a completely separate body of literature and contain none of
the Arkansas figures, so they do not resolve this.

Every other figure on the page is confirmed verbatim against Marley's own research notes:
the 5-of-9 criteria, the 5.9% vs 1.4% suicide rate, the 1980 DSM-III date, the 46th state
ranking, the 1-in-4 and 1-in-3 Arkansas figures, and the ~125,000.

## Photography

| File | Use | Source |
| --- | --- | --- |
| `images/marley.webp` | About section only | Marley's own portrait |
| `images/hero-reading.webp` | Hero | Unsplash |
| `images/home-family.webp` | "What it looks like at home" | Unsplash |
| `images/therapy-session.webp` | "What can actually change" | Marley, via Canva |
| `images/family-hands.webp` | "Three free guides" band | Marley, via Canva |
| `guide-src/img/p-raising.jpg` | Guide 3, raising the subject | Unsplash `DVoh8VY4NTQ` |
| `guide-src/img/p-listening.jpg` | Guide 3, validation | Unsplash `photo-1654608958160` |
| `guide-src/img/p-calling.jpg` | Guide 3, crisis section | Unsplash `v8UNH7LCDko` |
| `guide-src/img/p-stepping.jpg` | Guide 3, boundaries | Unsplash `tvbjFMHQ2AE` |

Unsplash photos are free for commercial use with no attribution required. All are
converted to WebP and committed rather than hotlinked, so the page has no external
image dependencies.

People, not landscapes, and none of them distressed. Marley's own StoryBrand failure
marker was the perpetuation of stigma, and photographs of visibly miserable people
are the most common way mental health sites do exactly that.

## Accessibility

Palette is warm bone, deep indigo, and terracotta. Every text/background pair is
verified against WCAG 2.1 AA (4.5:1 minimum). Measured ratios:

| Pair | Ratio | AA |
| --- | --- | --- |
| Body text on page background | 14.34 | pass |
| Body text on alt band | 12.65 | pass |
| Secondary text on page background | 7.36 | pass |
| Secondary text on alt band | 6.49 | pass |
| Labels and links on page background | 11.30 | pass |
| Button label on primary | 12.40 | pass |
| Accent text on page background | 5.47 | pass |
| Accent text on alt band | 4.82 | pass |
| Dark band body text | 14.87 | pass |
| Dark band secondary text | 10.58 | pass |
| Dark band accent line | 8.07 | pass |

Also implemented, covering the WCAG criteria most often cited in ADA web
accessibility complaints:

- Single `h1`, no skipped heading levels, verified by script
- Descriptive `alt` text on every image
- Skip-to-content link, `main` landmark, labelled `nav`
- Three "Download PDF" buttons carry screen-reader-only text naming which guide,
  so link purpose is clear out of context (WCAG 2.4.4)
- Visible 3px focus ring on every interactive element
- Interactive targets at least 44px tall
- No meaning conveyed by color alone
- Page zoom not disabled
- `prefers-reduced-motion` respected
- The emphasis line is sentence case rather than literal capitals, which some
  screen readers spell out letter by letter

Re-run the checks with the scripts noted in the commit history if the palette or
markup changes.

## Structure

```
index.html      Landing page
thanks.html     Guide download page
images/         Site photography, WebP
downloads/      The three guide PDFs
guide-src/      Source the PDFs are built from
```

Plain static HTML with inline CSS. No build step, no dependencies.

## Deployment

GitHub Pages, from `main` at root. Pushing to `main` redeploys.

Because Pages serves this from a subpath, all internal links are relative. Do not change them to root-absolute paths (`/thanks.html`) or they will break.

## A note on the email capture

The original draft used Netlify form attributes with a POST to `/thanks.html`. GitHub Pages cannot process form submissions, so that would have failed silently on every visitor. The email fields are replaced with direct links to the guides page.

This matches the call to action defined in the Aug 26 StoryBrand session, which was to direct visitors to download the resources rather than to build a list. If Marley does want email capture, it needs a form backend such as Formspree, or a move to Netlify.
