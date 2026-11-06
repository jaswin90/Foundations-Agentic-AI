// Playwright check for changed pages. Usage (from repo root, with `python3 -m http.server 8000 -d docs` running):
//   node tools/check_pages.js chapters/ch01.html index.html ...   [SHOTS=/path/to/dir]
const { chromium } = require('playwright');
(async () => {
  const pages = process.argv.slice(2); const base = 'http://localhost:8000/';
  const browser = await chromium.launch(); let bad = 0;
  for (const p of pages) {
    for (const width of [390, 1280]) {
      const ctx = await browser.newContext({ viewport: { width, height: 900 } });
      const pg = await ctx.newPage(); const errs = [];
      pg.on('pageerror', e => errs.push(e.message));
      pg.on('console', m => { if (m.type() === 'error' && !/firestore|firebase|googleapis|gstatic|fonts|Failed to load resource/i.test(m.text())) errs.push('console: ' + m.text()); });
      await pg.goto(base + p, { waitUntil: 'networkidle' }); await pg.waitForTimeout(800);
      const r = await pg.evaluate(() => ({
        katexErr: document.querySelectorAll('.katex-error').length,
        overflow: document.documentElement.scrollWidth - window.innerWidth,
        charts: document.querySelectorAll('figure.chart').length,
        chartsDrawn: document.querySelectorAll('figure.chart svg').length,
        svgs: document.querySelectorAll('svg.dg').length,
        figOutside: Array.from(document.querySelectorAll('figure')).filter(f => !f.closest('article')).length,
        mcq: document.querySelectorAll('.mcq').length, qa: document.querySelectorAll('details.qa').length,
        drills: document.querySelectorAll('details.drill').length, examples: document.querySelectorAll('.box.example').length,
        words: (document.querySelector('article') || document.body).innerText.split(/\s+/).length,
        dupIds: (() => { const s = new Set(), d = []; document.querySelectorAll('[id]').forEach(e => { if (s.has(e.id)) d.push(e.id); s.add(e.id); }); return d; })(),
        brokenRefs: Array.from(document.querySelectorAll('a[href^="#"]')).map(a => a.getAttribute('href').slice(1)).filter(id => id && !document.getElementById(id))
      }));
      const ok = !errs.length && !r.katexErr && r.overflow <= 0 && r.charts === r.chartsDrawn && !r.figOutside && !r.dupIds.length && !r.brokenRefs.length;
      if (!ok) bad++;
      console.log((ok ? 'OK  ' : 'FAIL') + ' ' + p + ' @' + width, JSON.stringify(r), errs.slice(0, 5).join(' | '));
      if (process.env.SHOTS && width === 1280) await pg.screenshot({ path: process.env.SHOTS + '/' + p.replace(/\W+/g, '_') + '.png', fullPage: true });
      await ctx.close();
    }
  }
  await browser.close(); process.exit(bad ? 1 : 0);
})();
