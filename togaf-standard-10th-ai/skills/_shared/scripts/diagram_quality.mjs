#!/usr/bin/env node
// Geometry flags are review evidence, never professional approval.
import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {launchBrowser} from './browser_resolver.mjs';

export async function inspect(page,expected) {
 return page.evaluate(({entity_ids,relationships})=>{
  const root=document.querySelector('svg');if(!root)throw Error('missing SVG root');
  const findings=[],nodes=new Map(),visible=el=>{
   if(el.closest('defs,metadata,style,title,desc'))return false;
   for(let p=el;p&&p!==root.parentElement;p=p.parentElement){const s=getComputedStyle(p);if(s.display==='none'||s.visibility==='hidden'||Number(s.opacity)===0)return false;}
   const r=el.getBoundingClientRect();
   return (r.width>0&&r.height>0)||(el.matches('path,line,polyline')&&(r.width>0||r.height>0)&&getComputedStyle(el).stroke!=='none'&&typeof el.getTotalLength==='function'&&el.getTotalLength()>0);
  };
  const rect=el=>{const r=el.getBoundingClientRect();return{x:r.x,y:r.y,w:r.width,h:r.height};};
  for(const el of root.querySelectorAll('[data-entity-id]'))if(visible(el))nodes.set(el.dataset.entityId,rect(el.querySelector('rect,ellipse,circle,polygon')||el));
  for(const id of entity_ids)if(!nodes.has(id))findings.push({code:'entity-no-visible-geometry',id});
  const relationGroups=new Map();
  for(const el of root.querySelectorAll('[data-relationship-id]')){
   const id=el.dataset.relationshipId;(relationGroups.get(id)||relationGroups.set(id,[]).get(id)).push(el);
  }
  const grid=new Map(),cell=256;
  for(const[id,r]of nodes)for(let x=Math.floor(r.x/cell);x<=Math.floor((r.x+r.w)/cell);x++)for(let y=Math.floor(r.y/cell);y<=Math.floor((r.y+r.h)/cell);y++){
   const key=x+','+y;(grid.get(key)||grid.set(key,[]).get(key)).push([id,r]);
  }
  const distance=(p,r)=>Math.hypot(Math.max(r.x-p.x,0,p.x-r.x-r.w),Math.max(r.y-p.y,0,p.y-r.y-r.h));
  const frame=rect(root),texts=[...root.querySelectorAll('text')].filter(visible).map(el=>({...rect(el),text:el.textContent}));
  for(const t of texts)if(t.x<frame.x-2||t.y<frame.y-2||t.x+t.w>frame.x+frame.w+2||t.y+t.h>frame.y+frame.h+2)findings.push({code:'text-clipped',text:t.text});
  const observed=[];
  for(const relation of relationships){
   const groups=relationGroups.get(relation.id)||[];
   const paths=[...new Set(groups.flatMap(el=>[...(el.matches('path,line,polyline')?[el]:[]),...el.querySelectorAll('path,line,polyline')]))].filter(el=>visible(el)&&typeof el.getTotalLength==='function'&&el.getTotalLength()>1);
   if(!paths.length){findings.push({code:'relationship-no-visible-connector',id:relation.id});continue;}
   const edge=paths.reduce((a,b)=>a.getTotalLength()>b.getTotalLength()?a:b),length=edge.getTotalLength(),matrix=edge.getScreenCTM();
   const point=n=>{const p=edge.getPointAtLength(n);return new DOMPoint(p.x,p.y).matrixTransform(matrix);};
   const first=point(0),last=point(length),source=nodes.get(relation.source),target=nodes.get(relation.target);
   if(!source||!target)findings.push({code:'connector-endpoint-not-visible',id:relation.id});
   else if(distance(first,source)>24||distance(last,target)>24)findings.push({code:'connector-endpoint-or-direction',id:relation.id,start_distance:distance(first,source),end_distance:distance(last,target)});
   const marker=getComputedStyle(edge).markerEnd;
   if(!marker||marker==='none')findings.push({code:'directed-connector-no-arrow',id:relation.id});
   const hits=new Set(),samples=Math.min(4000,Math.max(2,Math.ceil(length/5)));
   for(let n=1;n<samples;n++){
    const p=point(length*n/samples),candidates=grid.get(Math.floor(p.x/cell)+','+Math.floor(p.y/cell))||[];
    for(const[id,r]of candidates)if(id!==relation.source&&id!==relation.target&&p.x>r.x+3&&p.x<r.x+r.w-3&&p.y>r.y+3&&p.y<r.y+r.h-3)hits.add(id);
   }
   if(hits.size)findings.push({code:'connector-crosses-unrelated-node',id:relation.id,node_ids:[...hits]});
   const label=[...new Set(groups.flatMap(el=>[...(el.matches('text')?[el]:[]),...el.querySelectorAll('text')]))].filter(visible).map(el=>el.textContent).join(' ').replace(/\s+/g,' ');
   if(relation.label&&!label.replace(/\s+/g,'').includes(relation.label.replace(/\s+/g,'')))findings.push({code:'connector-label-unconfirmed',id:relation.id,expected:relation.label});
   const guard=relation.attributes?.guard,guardText=typeof guard==='object'?JSON.stringify(guard):String(guard);
   if(guard&&!label.replace(/\s+/g,'').includes(guardText.replace(/\s+/g,'')))findings.push({code:'connector-guard-unconfirmed',id:relation.id,expected:guard});
   observed.push({id:relation.id,has_arrow:marker&&marker!=='none',label,guard:relation.attributes?.guard||null});
  }
  return{findings,observed,visible_entities:nodes.size,text_count:texts.length,status:findings.length?'needs_review':'engineering-pass',visual_acceptance:'pending',limit:'Sampled connector geometry; flags need adjudication. Text occlusion, source notation and business meaning require independent visual review.'};
 },expected);
}

if(process.argv[1]&&pathToFileURL(path.resolve(process.argv[1])).href===import.meta.url){
 const directory=path.resolve(process.argv[2]||'.'),out=process.argv[3];
 if(!out)throw Error('usage: diagram_quality.mjs delivery-directory NEW-report.json');
 const manifest=JSON.parse(await fs.readFile(path.join(directory,'manifest.json'),'utf8'));
 let jobs;
 if(manifest.pages){
  const records=JSON.parse(await fs.readFile(path.join(directory,'records.json'),'utf8')),index=new Map(records.relationships.map(r=>[r.id,r]));
  jobs=manifest.pages.map(p=>({svg:p.svg,expected:{entity_ids:p.entity_ids,relationships:p.relationship_ids.map(id=>index.get(id))}}));
 }else{
  const model=JSON.parse(await fs.readFile(path.join(directory,'model.json'),'utf8')),relations=new Map(model.relationships.map(r=>[r.id,r]));
  jobs=manifest.artifacts.filter(a=>a.svg).map(a=>{const v=model.views.find(v=>v.id===a.view_id);return{svg:a.svg,expected:{entity_ids:v.entity_ids,relationships:v.relationship_ids.map(id=>relations.get(id))}};});
 }
 let browser;const rows=[];let result;
 try{
  browser=await launchBrowser();const page=await browser.newPage();await page.setViewport({width:1920,height:1080});
  for(const job of jobs){const file=path.resolve(directory,job.svg);if(!file.startsWith(directory+path.sep))throw Error('unsafe SVG path');await page.goto(pathToFileURL(file).href);await page.evaluate(()=>document.fonts.ready);rows.push({file:job.svg,...await inspect(page,job.expected)});}
  result={status:rows.some(r=>r.findings.length)?'needs_review':'engineering-pass',checked:rows.length,rows,visual_acceptance:'pending'};
 }catch(error){result={status:'blocked',reason:String(error),rows};}finally{if(browser)await browser.close();}
 await fs.writeFile(out,JSON.stringify(result,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({status:result.status,checked:result.checked,report:out}));process.exitCode=result.status==='engineering-pass'?0:result.status==='blocked'?3:1;
}
