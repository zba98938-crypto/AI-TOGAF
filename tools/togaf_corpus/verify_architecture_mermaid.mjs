#!/usr/bin/env node
// Parse every emitted diagram and render representative complete graphs locally.
// Uses the repository's existing Mermaid and installed browser, without downloads.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {launchBrowser} from '../../togaf-standard-10th-ai/skills/_shared/scripts/browser_resolver.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const output=path.join(root,'togaf-standard-10th-ai');
const index=JSON.parse(await fs.readFile(path.join(output,'architecture/diagrams/index.json'),'utf8'));
const dest=path.join(output,'architecture/diagrams/verification');
await fs.mkdir(dest,{recursive:true});
const browser=await launchBrowser();
const digest=buffer=>createHash('sha256').update(buffer).digest('hex');
const report={browser:browser.togafBrowser,architecture_index_sha256:digest(await fs.readFile(path.join(output,'architecture/diagrams/index.json'))),
  verifier_sha256:digest(await fs.readFile(fileURLToPath(import.meta.url))),parsed:0,rendered:[],errors:[]};
try {
  const page=await browser.newPage();
  await page.setViewport({width:1600,height:1200,deviceScaleFactor:1});
  await page.setContent('<html><head><meta name="color-scheme" content="light"><style>html,body{background:#fff;color:#172638;color-scheme:light}#container svg{background:#fff}</style></head><body><div id="container"></div></body></html>');
  await page.addScriptTag({path:path.join(root,'togaf-standard-10th-ai/skills/_shared/node_modules/mermaid/dist/mermaid.min.js')});
  await page.evaluate(()=>mermaid.initialize({startOnLoad:false,theme:'default',maxEdges:10000,maxTextSize:2000000,securityLevel:'strict'}));
  for(const entry of index.diagrams){
    for(const suffix of ['.mmd','.relations.mmd','.hierarchy.mmd']){
      const file=entry.mermaid_path.replace(/\.mmd$/,suffix);
      const source=await fs.readFile(path.join(output,file),'utf8');
      try{await page.evaluate(s=>mermaid.parse(s),source);report.parsed++;}
      catch(error){report.errors.push({file,message:String(error)});}
    }
  }
  const matrix=index.diagrams.filter(x=>x.category==='role-skill-matrix').sort((a,b)=>b.statistics.source_relations-a.statistics.source_relations)[0];
  const selected=['G206/fig3-1','G233/fig3-1','G233/fig4-1','G249/fig4-1','G249/fig4-2','G248/fig3-1','G238/fig3-4',matrix?.id].filter(Boolean);
  for(let i=0;i<selected.length;i++){
    const id=selected[i],entry=index.diagrams.find(x=>x.id===id),source=await fs.readFile(path.join(output,entry.mermaid_path),'utf8');
    try{
      const rendered=await page.evaluate(async ({source,i})=>{
        const {svg}=await mermaid.render('diagram'+i,source);document.getElementById('container').innerHTML=svg;
        const el=document.querySelector('#container svg'),box=el.viewBox.baseVal;
        el.style.maxWidth='1500px';el.style.width='1500px';el.style.height='auto';
        el.style.background='#fff';
        return {svg:el.outerHTML,width:box.width,height:box.height,nodes:el.querySelectorAll('.node').length};
      },{source,i});
      const basename=id.replace('/','-');
      await fs.writeFile(path.join(dest,basename+'.svg'),rendered.svg);
      await page.screenshot({path:path.join(dest,basename+'.png'),fullPage:true});
      report.rendered.push({id,svg:'verification/'+basename+'.svg',png:'verification/'+basename+'.png',width:rendered.width,height:rendered.height,nodes:rendered.nodes});
    }catch(error){report.errors.push({id,message:String(error)});}
  }
} finally {await browser.close();}
await fs.writeFile(path.join(dest,'mermaid-validation.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
if(report.errors.length)process.exitCode=1;
