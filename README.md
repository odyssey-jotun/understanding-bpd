# Understanding BPD

Landing site for Marley Spraggins' passion project: three free, research-informed guides to borderline personality disorder for individuals, families, and loved ones.

## Live site

**https://odyssey-jotun.github.io/understanding-bpd/**

Not serving yet. This repository is currently **private**, and GitHub Pages on a
private repository requires a paid plan. The URL above is the address Pages will
use the moment the repository is made public and Pages is enabled on `main` at
root, which is the same setup used by `kindled-movement` and `woven`.

### Preview link (working now)

**https://claude.ai/artifact/Kg4od2bxK4ipvxBLv9nmw9**

A hosted copy of the page so it can be reviewed before launch. Private by default;
shareable from the page's share menu. The three PDF buttons 404 there too, for the
same reason they do here.

Note that the preview is generated from `index.html` with the outer
`<!doctype>/<html>/<head>/<body>` wrapper stripped, because that host supplies its
own. It is a copy, not a source file, so it does not update when `index.html`
changes. `index.html` remains the single source of truth.

## Status

Deployed and viewable, but not finished. Two things are still outstanding.

### 1. The three PDF guides are missing

`thanks.html` links to three files that do not exist in this repo yet:

| Expected path | Guide |
| --- | --- |
| `downloads/BPD_Overview.pdf` | Overview, Characteristics, and Causes |
| `downloads/bpd_patient_guide_v6.pdf` | So You (Think You) Have BPD? |
| `downloads/bpd_loved_ones_guide_v2.pdf` | So Someone You Love (Might Have) BPD? |

Drop the files in at exactly those names and the buttons work with no code change. A review notice is currently shown on `thanks.html`; remove that block once the files land.

Consider renaming `bpd_patient_guide_v6.pdf` and `bpd_loved_ones_guide_v2.pdf` before launch. Draft version numbers become permanent public URLs.

### 2. Two Arkansas sources need full citations

The page now carries a numbered Works Cited section. Five of the seven entries are
complete. Two are titles only, taken from Marley's research notes, and need her to
supply publisher and date before launch:

- **[5]** Time Wellness Arkansas, *Arkansas mental health statistics*
- **[6]** *Nearly one in three Arkansans report symptoms of depression*

One claim is cited but still unverified against the source: **[7]** Guillen et al.
(2024) on Family Connections reducing caregiver burden.

Every other figure on the page is confirmed verbatim against Marley's own research
notes: the 5-of-9 criteria, the 5.9% vs 1.4% suicide rate, the 1980 DSM-III date,
the 46th state ranking, the 1-in-4 and 1-in-3 Arkansas figures, and the ~125,000.

The site is set to `noindex,nofollow` until the PDFs land. Flip the robots meta in
`index.html` before launch.

## Photography

| File | Use | Source |
| --- | --- | --- |
| `images/marley.webp` | About section only | Marley's own portrait |
| `images/hero-meadow.webp` | Hero background | Unsplash |
| `images/home-window.webp` | "What it looks like at home" | Unsplash |
| `images/mist-clearing.webp` | "What can actually change" | Unsplash |

Unsplash photos are free for commercial use with no attribution required. All are
converted to WebP and committed to the repo rather than hotlinked, so the page has
no external image dependencies.

Deliberately no stock photos of distressed-looking people. Marley's own StoryBrand
failure marker was the perpetuation of stigma, and that genre of image is the most
common way mental health sites do exactly that.

## Structure

```
index.html      Landing page
thanks.html     Guide download page
images/         marley.webp (hero and About portrait)
downloads/      The three PDFs go here
```

Plain static HTML with inline CSS. No build step, no dependencies.

## Deployment

GitHub Pages, from `main` at root. Pushing to `main` redeploys.

Because Pages serves this from a subpath, all internal links are relative. Do not change them to root-absolute paths (`/thanks.html`) or they will break.

## A note on the email capture

The original draft used Netlify form attributes with a POST to `/thanks.html`. GitHub Pages cannot process form submissions, so that would have failed silently on every visitor. The email fields are replaced with direct links to the guides page.

This matches the call to action defined in the Aug 26 StoryBrand session, which was to direct visitors to download the resources rather than to build a list. If Marley does want email capture, it needs a form backend such as Formspree, or a move to Netlify.
