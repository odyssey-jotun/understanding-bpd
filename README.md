# Understanding BPD

Landing site for Marley Spraggins' passion project: three free, research-informed guides to borderline personality disorder for individuals, families, and loved ones.

## Live site

**https://odyssey-jotun.github.io/understanding-bpd/**

Not serving yet. This repository is currently **private**, and GitHub Pages on a
private repository requires a paid plan. The URL above is the address Pages will
use the moment the repository is made public and Pages is enabled on `main` at
root, which is the same setup used by `kindled-movement` and `woven`.

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

### 2. Citations need finishing

The page makes eight cited claims. Four are confirmed verbatim against Marley's own research notes:

- **[1]** DSM-5-TR diagnostic criteria, five of nine
- **[2]** Leichsenring et al. 2024, suicide rate 5.9% vs 1.4%
- **[4]** Fonagy et al. 2017, mentalizing and resilience
- **[5]** Bozzatello et al. 2021, trauma and early onset

Four have not yet been checked against a source:

- **[3]** Schaich et al. 2021, the 92% / 63% / 74% distress-tolerance figures
- **[6]** May et al. 2016, DBT skill areas
- **[7]** Zhang et al. 2025, brief DBT review of 22 studies
- **[8]** Guillén et al. 2024, Family Connections trial of 121 relatives

Separately, the 92 / 63 / 74 figures come from a qualitative study of 24 participants. Presenting them as a headline statistic overstates what that design supports even if the numbers are accurate.

The site is set to `noindex,nofollow` until these are resolved. Flip the robots meta in `index.html` before launch.

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
