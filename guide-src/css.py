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

/* ---------- expansion components ---------- */
.lede{ font-family:'Fraunces',Georgia,serif; font-size:12.6pt; line-height:1.5;
  color:var(--primary); margin:0 0 12pt; }

.twocol{ display:flex; gap:16pt; margin:0 0 12pt; break-inside:avoid-page; }
.twocol > div{ flex:1; }
.panel{ background:var(--bg-alt); border-radius:9pt; padding:11pt 13pt; }
.panel h4{ font-family:'Fraunces',serif; font-size:10.6pt; color:var(--primary);
  margin:0 0 5pt; font-weight:600; }
.panel ul{ margin:0; padding-left:12pt; }
.panel li{ font-size:9.8pt; margin-bottom:3.5pt; }

/* instead-of / try script cards */
.script{ border:1px solid var(--line); border-radius:9pt; padding:11pt 13pt;
  margin:0 0 10pt; break-inside:avoid-page; }
.script .sit{ font-family:'Fraunces',serif; font-size:10.8pt; font-weight:600;
  color:var(--primary); margin:0 0 7pt; }
.script .line{ padding-left:11pt; margin:0 0 6pt; border-left:2.5pt solid var(--line); }
.script .line:last-child{ margin-bottom:0; }
.script .no{ border-left-color:var(--accent); }
.script .yes{ border-left-color:var(--primary); }
.script .tag{ font-family:'Karla',sans-serif; font-size:7.6pt; font-weight:700;
  letter-spacing:.14em; text-transform:uppercase; display:block; margin-bottom:2pt; }
.script .no .tag{ color:var(--accent); }
.script .yes .tag{ color:var(--primary); }
.script .say{ font-size:10pt; line-height:1.5; margin:0; }
.script .yes .say{ font-weight:500; }
.script .why{ font-size:8.8pt; color:var(--ink-soft); font-style:italic; margin:5pt 0 0; }

/* numbered ladder */
.ladder{ counter-reset:rung; margin:0 0 12pt; }
.rung{ counter-increment:rung; position:relative; padding-left:30pt;
  padding-bottom:11pt; break-inside:avoid-page; }
.rung::before{ content:counter(rung); position:absolute; left:0; top:0;
  width:19pt; height:19pt; border-radius:50%; background:var(--primary);
  color:var(--on-dark); font-family:'Fraunces',serif; font-size:9.4pt; font-weight:600;
  display:flex; align-items:center; justify-content:center; }
.rung::after{ content:''; position:absolute; left:9pt; top:19pt; bottom:0;
  width:1px; background:var(--line); }
.rung:last-child{ padding-bottom:0; }
.rung:last-child::after{ display:none; }
.rung h4{ font-family:'Fraunces',serif; font-size:10.8pt; color:var(--primary);
  margin:1pt 0 3pt; font-weight:600; }
.rung p{ font-size:9.9pt; margin:0 0 3pt; }
.rung .say{ font-size:9.9pt; color:var(--primary); font-style:italic;
  background:var(--bg-alt); padding:5pt 9pt; border-radius:6pt; margin:4pt 0 0; }

/* decision flow */
.flow{ margin:0 0 12pt; }
.pair{ break-inside:avoid-page; margin-bottom:5pt; }
.pair .step{ margin-bottom:5pt; }
.step{ border-radius:9pt; padding:9pt 12pt; margin:0 0 5pt; break-inside:avoid-page; }
.step.q{ background:var(--primary); color:var(--on-dark); }
.step.q p{ color:var(--on-dark); margin:0; font-weight:600; font-size:10.2pt; }
.step.a{ background:var(--bg-alt); margin-left:22pt; }
.step.a p{ margin:0; font-size:9.9pt; }
.step.a .label{ font-family:'Karla',sans-serif; font-size:7.6pt; font-weight:700;
  letter-spacing:.14em; text-transform:uppercase; color:var(--accent); display:block;
  margin-bottom:2pt; }
.step.stop{ background:var(--accent); color:#FFF; margin-left:22pt; }
.step.stop p, .step.stop .label{ color:#FFF; }

/* self-check list */
.check{ margin:0 0 10pt; padding:0; list-style:none; }
.check li{ position:relative; padding-left:20pt; margin-bottom:6pt; font-size:10pt;
  break-inside:avoid-page; }
.check li::before{ content:''; position:absolute; left:0; top:1.5pt;
  width:11pt; height:11pt; border:1.4pt solid var(--primary); border-radius:2.5pt; }


/* ---------- drawn diagrams ---------- */
figure.diagram{ margin:14pt 0 14pt; break-inside:avoid-page; }
figure.diagram svg{ width:100%; height:auto; display:block; }
figure.diagram figcaption{ font-size:8.4pt; color:var(--ink-soft); font-style:italic;
  margin-top:6pt; text-align:left; }
.dg-title{ font-family:'Karla',sans-serif; font-size:8pt; font-weight:700;
  letter-spacing:.14em; text-transform:uppercase; fill:var(--accent); }
.dg-lab{ font-family:'Karla',sans-serif; font-size:11px; fill:#4A4F66; }
.dg-lab-b{ font-family:'Karla',sans-serif; font-size:11.5px; font-weight:700; fill:#2A3352; }
.dg-lab-w{ font-family:'Karla',sans-serif; font-size:11.5px; font-weight:700; fill:#F2EFE9; }
.dg-num{ font-family:'Fraunces',serif; font-size:13px; font-weight:600; fill:#F2EFE9; }
.dg-axis{ stroke:#1F2233; stroke-opacity:.30; stroke-width:1; }
.dg-muted{ font-family:'Karla',sans-serif; font-size:10px; fill:#4A4F66; fill-opacity:.85; }

"""
