#!/usr/bin/env node
// Network-free rendering after npm ci; font and labels come from the output model.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {launchBrowser} from './browser_resolver.mjs';
import {renderMermaid} from '@mermaid-js/mermaid-cli';
import {Resvg} from '@resvg/resvg-js';
import {rasterPlan,renderTiles} from './raster_tiles.mjs';
const jobFile=process.argv[2];
if(!jobFile)throw new Error('Usage: node render.mjs render-jobs.json');
const spec=JSON.parse(await fs.readFile(jobFile,'utf8'));
const jobRoot=path.dirname(path.resolve(jobFile));
spec.font=path.resolve(jobRoot,spec.font);
for(const job of spec.jobs)for(const key of ['source','svg','png'])job[key]=path.resolve(jobRoot,job[key]);
const fontDir=path.dirname(spec.font);
const css=path.join(fontDir,'font-subset.css');
const fontData=(await fs.readFile(spec.font)).toString('base64');
await fs.writeFile(css,`@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,${fontData})} body,text{font-family:TogafCJK,sans-serif}`);
const browserNeeded=spec.jobs.some(j=>j.kind==='mmd');
let browser;
let browserInfo;
const results=[];
const sha=data=>createHash('sha256').update(data).digest('hex');
// Explicitly match Mermaid's supported limits; never render its fallback error card as a passed diagram.
const MERMAID_LIMITS={maxTextSize:50000,maxEdges:500};
const definitions=new Map();
try {
 for(const job of spec.jobs)if(job.kind==='mmd'){
  const definition=await fs.readFile(job.source,'utf8');
  if(definition.length>MERMAID_LIMITS.maxTextSize)
   throw new Error(`diagram-capacity: ${job.id}: Mermaid source has ${definition.length} characters; supported maxTextSize is ${MERMAID_LIMITS.maxTextSize}; source retained, SVG/PNG untested`);
  definitions.set(job,definition);
 }
 if(browserNeeded){browser=await launchBrowser();browserInfo=browser.togafBrowser;}
 for(const job of spec.jobs){
  if(job.kind==='mmd'){
   const definition=definitions.get(job);
   const result=await renderMermaid(browser,definition,'svg',{
    backgroundColor:'white',fontEmbed:false,viewport:{width:1800,height:1200,deviceScaleFactor:1},
    customFontCSS:[{cssUrl:pathToFileURL(css),allowParentDirectoryLevel:0}],
    mermaidConfig:{...MERMAID_LIMITS,securityLevel:'strict',theme:'base',look:'classic',htmlLabels:false,fontFamily:'TogafCJK',themeVariables:{fontFamily:'TogafCJK',fontSize:'18px',primaryColor:'#e8f1f8',primaryTextColor:'#18334a',lineColor:'#536d83',edgeLabelBackground:'#ffffff',secondaryColor:'#f2f5f8',tertiaryColor:'#ffffff',attributeBackgroundColorOdd:'#f2f5f8',attributeBackgroundColorEven:'#ffffff'},
      flowchart:{htmlLabels:false,curve:'linear',useMaxWidth:false,wrappingWidth:320},sequence:{useMaxWidth:false},er:{useMaxWidth:false,minEntityWidth:440,entityPadding:30}}
   });
   let svg=new TextDecoder().decode(result.data);
   if(/<[^>]+\sclass=["'][^"']*\berror-(?:icon|text)\b[^"']*["'][^>]*>/.test(svg)){
    await fs.writeFile(job.svg,svg);
    throw new Error(`mermaid-render-error: ${job.id}: Mermaid returned an error SVG; diagnostic SVG retained, PNG untested`);
   }
   svg=svg.replace(/(<svg[^>]*>)/,`$1<defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,${fontData})}</style></defs>`);
   svg=svg.replace('</svg>','<style> .row-rect-odd path,.row-rect-odd rect,.row-rect-even path,.row-rect-even rect{fill:#eef3f8 !important} .background{fill:#ffffff !important} .attributeBoxEven{fill:#ffffff !important} .attributeBoxOdd{fill:#eef3f8 !important} .relationshipLabelBox{fill:#ffffff !important} text{fill:#18334a}</style></svg>');
   // Standalone diagrams retain their title, factual status, notation legend.
   const bounds=svg.match(/viewBox="([^"]+)"/);
   if(!bounds)throw new Error(`${job.id}: missing SVG viewBox`);
   const [vx,vy,vw,vh]=bounds[1].split(/[ ,]+/).map(Number);
   const width=Math.max(vw,760), header=84;
   const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
   const wrap=(text,max)=>{let result=[],line='',units=0;for(const c of text){const n=c.codePointAt(0)>255?2:1;if(units+n>max){result.push(line);line='';units=0;}line+=c;units+=n;}if(line)result.push(line);return result;};
   const footer=wrap('图例：'+job.legend,Math.floor((width-40)/9));
   const height=header+vh+45+footer.length*26;
   const root=svg.match(/^<svg[^>]*>/)[0];
   const updated=root.replace(/viewBox="[^"]*"/,`viewBox="0 0 ${width} ${height}"`).replace(/width="[^"]*"/,`width="${width}"`).replace(/height="[^"]*"/,`height="${height}"`).replace(/style="[^"]*"/,'');
   const content=svg.slice(root.length,-6);
   const text=(y,s,size=18)=>`<text x="20" y="${y}" style="font-family:TogafCJK;font-size:${size}px;fill:#18334a">${escape(s)}</text>`;
   svg=updated+`<rect width="${width}" height="${height}" fill="white"/>`+`<g transform="translate(${-vx+(width-vw)/2},${header-vy})">${content}</g>`+text(30,job.title,22)+text(59,job.is_example?'虚构示例 / 候选草案':'项目架构视图 / 状态与证据见模型',15)+footer.map((line,i)=>text(header+vh+30+i*26,line,16)).join('')+'</svg>';
   await fs.writeFile(job.svg,svg);
  }
  const svg=await fs.readFile(job.svg,'utf8');
  const plan=rasterPlan(svg);
  if(plan.mode==='tiles'){
   if(spec.oversized_policy!=='tile')throw new Error('diagram-capacity: oversized SVG requires explicit tile policy; SVG retained');
   const tiled=await renderTiles(svg,job,spec.font,plan);
   const base=path.dirname(job.svg);
   const tileBytes=await fs.readFile(path.join(base,tiled.tile_manifest));
   const tileManifest=JSON.parse(tileBytes);
   tiled.svg_sha256=sha(Buffer.from(svg));
   tiled.tile_manifest_sha256=sha(tileBytes);tiled.png_sha256={};
   for(const tile of tileManifest.tiles)tiled.png_sha256[path.basename(tile.png)]=sha(await fs.readFile(path.join(base,tile.png)));
   results.push(tiled);
   continue;
  }
  const resvg=new Resvg(svg,{font:{fontFiles:[spec.font],loadSystemFonts:false,defaultFontFamily:'TogafCJK'},background:'white'});
  const rendered=resvg.render();
  if(rendered.width<80||rendered.height<40)throw new Error(`${job.id}: empty render`);
  const pngBytes=rendered.asPng();
  await fs.writeFile(job.png,pngBytes);
  results.push({id:job.id,width:rendered.width,height:rendered.height,svg:path.basename(job.svg),png:path.basename(job.png),svg_sha256:sha(Buffer.from(svg)),png_sha256:sha(pngBytes)});
 }
} catch(error) {
 const blocked=String(error).includes('browser-unavailable:')||String(error).includes('diagram-capacity:')||String(error).includes('Edge limit exceeded.');
 await fs.writeFile(path.join(path.dirname(jobFile),'render-report.json'),JSON.stringify({status:blocked?'blocked':'failed',reason:String(error),browser:browserInfo,results},null,2)+'\n');
 console.error(String(error));process.exitCode=blocked?3:1;
} finally {if(browser)await browser.close();}
if(!process.exitCode){
 await fs.writeFile(path.join(path.dirname(jobFile),'render-report.json'),JSON.stringify({status:'passed',renderer:'Mermaid CLI 12 / resvg 2.6.2',font:'bundled Noto Sans SC subset',browser:browserInfo,results},null,2)+'\n');
 console.log(`Rendered ${results.length} SVG/PNG diagrams`);
}
