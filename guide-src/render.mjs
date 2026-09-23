// Prints each guide HTML to PDF. Run from a directory that has playwright installed:
//   node render.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const D = dirname(fileURLToPath(import.meta.url));
const GUIDES = ['BPD_Overview', 'bpd_patient_guide_v6', 'bpd_loved_ones_guide_v2'];

const browser = await chromium.launch();
for (const name of GUIDES) {
  const page = await browser.newPage();
  await page.goto(`file://${join(D, name)}.html`, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(700);          // let Fraunces and Karla settle
  await page.pdf({
    path: join(D, '..', 'downloads', `${name}.pdf`),
    format: 'Letter',
    printBackground: true,
    preferCSSPageSize: true,
  });
  await page.close();
  console.log('wrote', name + '.pdf');
}
await browser.close();
