import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {launchBrowser} from './browser_resolver.mjs';

const [htmlPath, pdfPath] = process.argv.slice(2);
if (!htmlPath || !pdfPath) throw new Error('usage: node print_deliverable_pdf.mjs input.html output.pdf');
let browser;
try {
  browser = await launchBrowser();
  const page = await browser.newPage();
  await page.goto(pathToFileURL(path.resolve(htmlPath)).href, {waitUntil: 'load'});
  await page.evaluate(() => document.fonts.ready);
  // Wide model tables contain full JSON fields. Convert each row to a labeled
  // record for print so names and source IDs remain legible on an A4 page.
  await page.evaluate(() => {
    for (const table of document.querySelectorAll('table')) {
      const headers = [...table.querySelectorAll('thead th')].map(x => x.textContent.trim());
      if (headers.length <= 5) continue;
      const cards = document.createElement('section');
      cards.className = 'wide-records';
      for (const tr of table.querySelectorAll('tbody tr')) {
        const cells = [...tr.children];
        const card = document.createElement('section');
        card.className = 'wide-record';
        for (let i = 0; i < cells.length; i++) {
          const row = document.createElement('div');
          const label = document.createElement('strong');
          label.textContent = (headers[i] || `字段 ${i + 1}`) + '：';
          row.append(label);
          const value = document.createElement('span');
          value.innerHTML = cells[i].innerHTML;
          row.append(value);
          card.append(row);
        }
        cards.append(card);
      }
      table.replaceWith(cards);
    }
  });
  await page.pdf({path: pdfPath, format: 'A4', printBackground: true,
    margin: {top: '16mm', right: '14mm', bottom: '17mm', left: '14mm'},
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;color:#687584;width:100%;text-align:center"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'});
  await fs.writeFile(pdfPath+'.render.json',JSON.stringify({status:'passed',browser:browser.togafBrowser},null,2)+'\n');
} catch(error) {
  const blocked=String(error).includes('browser-unavailable:');
  await fs.writeFile(pdfPath+'.render.json',JSON.stringify({status:blocked?'blocked':'failed',reason:String(error)},null,2)+'\n');
  console.error(String(error));process.exitCode=blocked?3:1;
} finally {if(browser)await browser.close();}
