import fs from 'node:fs';
import path from 'node:path';
import { Resvg } from '@resvg/resvg-js';
import { launchBrowser } from './browser_resolver.mjs';
const out=path.resolve(process.argv[2]);
const report={notation:'project-reading-projection',svg:[],html:[],pdf:'not-requested',human_visual_review:'pending'};
const browser=await launchBrowser({args:['--no-sandbox']});
try {
  const page=await browser.newPage();await page.setViewport({width:1920,height:1080});
  for (const name of ['overview','states','rollback']) {
    const source=fs.readFileSync(path.join(out,name+'.svg'));
    fs.writeFileSync(path.join(out,name+'.png'),new Resvg(source,{font:{loadSystemFonts:true}}).render().asPng());
    await page.goto('file://'+path.join(out,name+'.svg'));
    const geometry=await page.evaluate(()=>Array.from(document.querySelectorAll('text')).map(t=>{const r=t.getBBox();return {text:t.textContent,x:r.x,y:r.y,width:r.width,height:r.height,font:parseFloat(getComputedStyle(t).fontSize)}}));
    const clipped=geometry.filter(t=>t.x<0||t.y<0||t.x+t.width>1920||t.y+t.height>1080);
    const undersize=geometry.filter(t=>t.font<18);
    report.svg.push({file:name+'.svg',text_count:geometry.length,clipped,undersize,status:clipped.length||undersize.length?'fail':'pass'});
  }
  await page.goto('file://'+path.join(out,'reader.html'));await page.evaluate(()=>document.fonts.ready);
  report.html=await page.evaluate(()=>({sections:document.querySelectorAll('section').length,horizontal_overflow:document.documentElement.scrollWidth>1920,failed_images:Array.from(document.images).filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src)}));
  if (process.argv.includes('--pdf')) {
    await page.pdf({path:path.join(out,'architecture-reader.pdf'),printBackground:true,preferCSSPageSize:true});report.pdf='created, pending raster review';
  }
  report.browser=browser.togafBrowser;
} finally {await browser.close();}
fs.writeFileSync(path.join(out,'visual-qa.json'),JSON.stringify(report,null,2));
console.log(JSON.stringify(report));
if(report.svg.some(r=>r.status!=='pass')||report.html.horizontal_overflow||report.html.failed_images.length)process.exitCode=1;
