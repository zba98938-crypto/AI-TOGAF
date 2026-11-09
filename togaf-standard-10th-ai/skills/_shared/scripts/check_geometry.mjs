// Bounding-box heuristics; observable flags require visual review, not approval.
import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {launchBrowser} from './browser_resolver.mjs';
const [input,...args]=process.argv.slice(2);
if(!input)throw new Error('usage: node check_geometry.mjs export-directory-or-manifest.json [--out report.json]');
const inputPath=path.resolve(input),manifestPath=inputPath.endsWith('.json')?inputPath:path.join(inputPath,'manifest.json');
const root=path.dirname(manifestPath),reportPath=args[0]==='--out'?path.resolve(args[1]):path.join(root,'geometry-check.json');
let browser;
let browserInfo;
const results=[];
let status='passed',reason;
try {
  const manifest=JSON.parse(await fs.readFile(manifestPath,'utf8'));
  const artifacts=manifest.artifacts.filter(a=>a.svg);
  if(!artifacts.length)throw new Error('no-svg-artifacts');
  browser=await launchBrowser();
  browserInfo=browser.togafBrowser;
  const page=await browser.newPage();
  await page.setViewport({width:2200,height:1800});
  for(const artifact of artifacts) {
    const svgPath=path.resolve(root,artifact.svg);
    try {
      await page.goto(pathToFileURL(svgPath).href,{waitUntil:'load'});
      await page.evaluate(()=>document.fonts.ready);
      const geometry=await page.evaluate(()=>{
        const root=document.querySelector('svg');
        if(!root)throw new Error('missing-svg-root');
        const frame=root.getBoundingClientRect();
        const texts=[...root.querySelectorAll('text')].map((el,i)=>{
          const b=el.getBoundingClientRect(),s=getComputedStyle(el);
          return {i,text:el.textContent.slice(0,180),x:b.x-frame.x,y:b.y-frame.y,w:b.width,h:b.height,
            visible:s.display!=='none'&&s.visibility!=='hidden'&&s.opacity!=='0'};
        }).filter(x=>x.visible&&x.w>.1&&x.h>.1);
        const clipped=texts.filter(t=>t.x< -2||t.y< -2||t.x+t.w>frame.width+2||t.y+t.h>frame.height+2);
        const overlaps=[];
        for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){
          const a=texts[i],b=texts[j],dx=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x),dy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
          if(dx>5&&dy>5&&dx*dy>Math.min(a.w*a.h,b.w*b.h)*.2)overlaps.push({a:a.text,b:b.text,dx,dy});
        }
        return {width:frame.width,height:frame.height,texts:texts.length,clipped,overlap_count:overlaps.length,overlaps:overlaps.slice(0,12)};
      });
      results.push({view_id:artifact.view_id,file:svgPath,status:'checked',...geometry});
    }catch(error){results.push({view_id:artifact.view_id,file:svgPath,status:'failed',reason:String(error)});status='failed';}
  }
} catch(error){status='blocked';reason=String(error);}
finally{if(browser)await browser.close();}
const summary={schema_version:'geometry-check/2',status,reason,checked:results.filter(r=>r.status==='checked').length,
  browser:browserInfo,
  flagged:results.filter(r=>r.clipped?.length||r.overlap_count).length,
  clipped_files:results.filter(r=>r.clipped?.length).length,overlap_flagged_files:results.filter(r=>r.overlap_count).length,
  limit:'SVG text clipping and text-box overlap heuristics only; flags require visual review. Edge collisions, source equivalence and semantics are not assessed.',results};
if(summary.status==='passed'&&summary.flagged>0)summary.status='review-required';
status=summary.status;
await fs.mkdir(path.dirname(reportPath),{recursive:true});
await fs.writeFile(reportPath,JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({status,checked:summary.checked,flagged:summary.flagged,report:reportPath,reason}));
process.exitCode=status==='passed'?0:status==='blocked'?3:1;
