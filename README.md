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
| `images/hero-reading.webp` | Hero | Unsplash |
| `images/home-family.webp` | "What it looks like at home" | Unsplash |
| `images/change-friends.webp` | "What can actually change" | Unsplash |

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
