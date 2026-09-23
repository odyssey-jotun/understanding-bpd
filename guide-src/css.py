CSS = r"""
@page { size: letter; margin: 0.85in 0.8in 0.75in 0.8in; }
@page fullbleed { margin: 0; }
:root{
  --bg:#F7F4EF; --bg-alt:#EBE6DC; --card:#FFFFFF;
  --ink:#1F2233; --ink-soft:#4A4F66;
  --primary:#2A3352; --primary-dk:#161B2E;
  --accent:#A8432A; --on-dark:#F2EFE9; --on-dark-soft:#C9CBD8;
  --accent-dark-bg:#E9A18A; --line:rgba(31,34,51,0.16);
}
*{ box-sizing:border-box; }
/* Body pages print on white. Chromium never paints the @page margin box,
   so a tinted body would show as a colour block floating on white paper.
   The brand carries on these pages through type, rules and callouts; the
   full-bleed cover and About page supply the colour. */
html{ background:#FFFFFF; }
html,body{ margin:0; padding:0; }
body{
  font-family:'Karla',system-ui,sans-serif;
  color:var(--ink); background:#FFFFFF;
  font-size:10.6pt; line-height:1.62;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}
h1,h2,h3,.display{ font-family:'Fraunces',Georgia,serif; font-weight:600; color:var(--primary); }
p{ margin:0 0 9pt; }
strong{ font-weight:700; color:var(--ink); }

/* ---------- full-bleed cover ---------- */
.cover{ page:fullbleed; break-after:page; width:8.5in; height:11in;
  background:var(--primary-dk); color:var(--on-dark);
  display:flex; flex-direction:column; overflow:hidden; }
.cover-top{ padding:0.78in 0.8in 0.34in; }
.cover .wordmark{ font-family:'Fraunces',serif; font-size:13pt; font-weight:600;
  color:var(--on-dark); letter-spacing:.01em; margin:0 0 0.42in; }
.cover .wordmark em{ font-style:normal; color:var(--accent-dark-bg); }
.cover .kicker{ font-family:'Karla',sans-serif; font-size:8.6pt; font-weight:700;
  letter-spacing:.17em; text-transform:uppercase; color:var(--accent-dark-bg); margin:0 0 11pt; }
.cover h1{ color:var(--on-dark); font-size:33pt; line-height:1.1; margin:0 0 12pt; letter-spacing:-0.01em; }
.cover .sub{ color:var(--on-dark-soft); font-size:11.6pt; line-height:1.5; margin:0; max-width:5.5in; }
.cover-img{ flex:1; position:relative; overflow:hidden; }
.cover-img img{ width:100%; height:100%; object-fit:cover; display:block; }
.cover-foot{ padding:0.24in 0.8in 0.5in; display:flex; justify-content:space-between;
  align-items:baseline; border-top:1px solid rgba(242,239,233,0.16); }
.cover-foot .by{ font-size:10pt; color:var(--on-dark); font-weight:600; }
.cover-foot .site{ font-size:8.6pt; color:var(--on-dark-soft); letter-spacing:.05em; }

/* ---------- body ---------- */
.kicker{ font-family:'Karla',sans-serif; font-size:8.2pt; font-weight:700;
  letter-spacing:.16em; text-transform:uppercase; color:var(--accent); margin:0 0 5pt;
  break-after:avoid-page; }
h2{ font-size:16.5pt; line-height:1.2; margin:0 0 7pt; break-after:avoid-page; }
h3{ font-size:11.4pt; line-height:1.3; margin:13pt 0 4pt; color:var(--primary); break-after:avoid-page; }
section.block{ margin-bottom:17pt; break-inside:avoid-page; }
section.block.loose{ break-inside:auto; }
.rule{ height:2.5pt; width:42pt; background:var(--accent); border-radius:2pt; margin:0 0 10pt;
  break-after:avoid-page; }

ul,ol{ margin:0 0 9pt; padding-left:15pt; }
li{ margin-bottom:5pt; }
li::marker{ color:var(--accent); }
ol.crit{ padding-left:0; list-style:none; counter-reset:c; }
ol.crit li{ counter-increment:c; position:relative; padding-left:24pt; margin-bottom:6pt; }
ol.crit li::before{ content:counter(c); position:absolute; left:0; top:0.5pt;
  width:16pt; height:16pt; border-radius:50%; background:var(--primary); color:var(--on-dark);
  font-family:'Fraunces',serif; font-size:8.4pt; font-weight:600;
  display:flex; align-items:center; justify-content:center; }

.callout{ background:var(--bg-alt); border-left:3pt solid var(--accent);
  padding:11pt 14pt; border-radius:0 8pt 8pt 0; margin:0 0 12pt; break-inside:avoid-page; }
.callout p:last-child{ margin-bottom:0; }
.callout .lead{ font-family:'Fraunces',serif; font-size:11.4pt; color:var(--primary); font-weight:600; margin-bottom:5pt; }

.crisis{ background:var(--primary-dk); color:var(--on-dark); border-radius:10pt;
  padding:14pt 16pt; margin:2pt 0 12pt; break-inside:avoid-page; }
.crisis h3{ color:var(--on-dark); margin:0 0 7pt; font-size:12pt; }
.crisis p, .crisis li{ color:var(--on-dark-soft); }
.crisis ul{ margin:0; padding-left:13pt; }
.crisis li::marker{ color:var(--accent-dark-bg); }
.crisis strong{ color:var(--on-dark); }

figure{ margin:12pt 0; break-inside:avoid-page; }
figure img{ width:100%; display:block; border-radius:10pt; object-fit:cover; }
figure.wide img{ height:1.85in; }
figure.tall{ width:3.4in; margin-left:auto; margin-right:auto; }
figure.tall img{ height:3.4in; }
figure.tall figcaption{ text-align:center; }
figcaption{ font-size:8.4pt; color:var(--ink-soft); margin-top:5pt; font-style:italic; }

/* ---------- about page ---------- */
.about{ page:fullbleed; break-before:page; break-after:page;
  width:8.5in; height:11in; background:var(--bg-alt); overflow:hidden;
  display:flex; flex-direction:column; }
.about-inner{ flex:1; padding:0.9in 0.8in 0.4in; display:flex; flex-direction:column; }
.about-head{ margin-bottom:0.34in; }
.about-head h2{ font-size:27pt; margin:0; }
.about-grid{ display:flex; gap:0.42in; align-items:flex-start; }
.about-photo{ width:2.5in; flex:none; border-radius:12pt; overflow:hidden;
  box-shadow:0 14pt 30pt -14pt rgba(31,34,51,0.5); }
.about-photo img{ width:100%; height:3.75in; object-fit:cover; display:block; }
.about-body{ flex:1; }
.about-body .name-line{ font-family:'Fraunces',serif; font-size:13pt; line-height:1.36;
  color:var(--primary); font-weight:600; margin-bottom:9pt; }
.about-body p{ font-size:10.6pt; }
.about-quote{ margin-top:0.34in; padding-top:0.26in; border-top:1px solid var(--line); }
.about-quote p{ font-family:'Fraunces',serif; font-size:12.4pt; line-height:1.48;
  color:var(--primary); margin:0; }
.about-foot{ background:var(--primary-dk); color:var(--on-dark-soft);
  padding:0.28in 0.8in; font-size:9pt; display:flex; justify-content:space-between; align-items:baseline; }
.about-foot .mark{ font-family:'Fraunces',serif; color:var(--on-dark); font-size:11pt; font-weight:600; }
.about-foot .mark em{ font-style:normal; color:var(--accent-dark-bg); }

/* ---------- works cited ---------- */
.refs{ break-before:page; }
.refs h2{ font-size:15pt; }
.refs ol{ padding-left:14pt; }
.refs li{ font-size:8.9pt; line-height:1.5; color:var(--ink-soft); margin-bottom:6pt; }
.refs li::marker{ color:var(--accent); font-weight:700; }
.refs a{ color:var(--ink-soft); word-break:break-all; text-decoration:none; }
.note{ font-size:8.6pt; color:var(--ink-soft); font-style:italic; margin-top:12pt;
  padding-top:8pt; border-top:1px solid var(--line); }
"""
