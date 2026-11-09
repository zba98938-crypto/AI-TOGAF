// Native-resolution crops of the SAME SVG, not a record-directory substitute.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {launchBrowser} from './browser_resolver.mjs';

const MAX_PIXELS=16_000_000, MAX_SIDE=16_384, TILE_SIDE=2048;
const MAX_TOTAL_PIXELS=512_000_000, MAX_TILES=512;
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
const capacity=reason=>{throw new Error('diagram-capacity: '+reason);};

export function rasterPlan(svg) {
 const root=svg.match(/<svg\b[^>]*>/)?.[0];
 if(!root)capacity('missing SVG root');
 const attr=name=>root.match(new RegExp('\\b'+name+'=["\x27]([^"\x27]+)["\x27]'))?.[1];
 const vb=(attr('viewBox')||'').trim().split(/[ ,]+/).map(Number);
 if(vb.length!==4||!vb.every(Number.isFinite)||vb[2]<=0||vb[3]<=0)capacity('invalid SVG viewBox');
 const dimension=(name,fallback)=>{
  const raw=attr(name);
  if(raw===undefined)return fallback;
  if(!/^(?:\d+(?:\.\d*)?|\.\d+)(?:px)?$/.test(raw))capacity('unsupported SVG '+name+' unit');
  const value=Number(raw.replace(/px$/,''));
  if(!Number.isFinite(value)||value<=0)capacity('invalid SVG '+name);
  return value;
 };
 const width=Math.ceil(dimension('width',vb[2])),height=Math.ceil(dimension('height',vb[3]));
 if(width*height<=MAX_PIXELS&&Math.max(width,height)<=MAX_SIDE)return {mode:'single',width,height,scale:1};
 // Allocation guards apply before any bitmap is created. No implicit downscale.
 const count=Math.ceil(width/TILE_SIDE)*Math.ceil(height/TILE_SIDE);
 if(width*height>MAX_TOTAL_PIXELS||count>MAX_TILES)capacity(`tiled output ${width}x${height} exceeds ${MAX_TOTAL_PIXELS} total pixels or ${MAX_TILES} tiles; SVG retained`);
 // Cropping in viewBox coordinates is exact only when pixels map uniformly.
 // A nonuniform viewport/aspect ratio needs explicit SVG alignment handling.
 if(Math.abs(width/vb[2]-height/vb[3])>0.01)capacity('nonuniform SVG viewport cannot be tiled without changing alignment');
 const tiles=[];
 for(let y=0;y<height;y+=TILE_SIDE)for(let x=0;x<width;x+=TILE_SIDE){
  const w=Math.min(TILE_SIDE,width-x),h=Math.min(TILE_SIDE,height-y);
  tiles.push({x,y,width:w,height:h,viewBox:[vb[0]+x*vb[2]/width,vb[1]+y*vb[3]/height,w*vb[2]/width,h*vb[3]/height]});
 }
 return {mode:'tiles',width,height,scale:1,tiles};
}

export async function renderTiles(svg,job,font,plan=rasterPlan(svg)) {
 if(plan.mode!=='tiles')throw new Error('tiles requested for single raster');
 const parsed=path.parse(job.png),dir=path.join(parsed.dir,parsed.name+'.tiles');
 await fs.mkdir(dir,{recursive:true});
 const tiles=[];
 // resvg 2.6.2 can abort (not throw) for off-viewport paths when an SVG
 // viewBox is cropped. Chromium clips the original SVG display list without
 // allocating the entire diagram bitmap and retains filters/markers/text.
 const browser=await launchBrowser();
 try {
 const page=await browser.newPage();
 const fontData=(await fs.readFile(font)).toString('base64');
 await page.setViewport({width:TILE_SIDE,height:TILE_SIDE,deviceScaleFactor:1});
 await page.setRequestInterception(true);
 page.on('request',request=>request.url().startsWith('data:')||request.url()==='about:blank'?request.continue():request.abort());
 await page.setContent('<!doctype html><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; font-src data:; img-src data:"><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+fontData+')}html,body{margin:0;background:white;overflow:hidden}svg{position:absolute;max-width:none}text{font-family:TogafCJK,sans-serif}</style>'+svg);
 await page.evaluate(()=>document.fonts.ready);
 for(let i=0;i<plan.tiles.length;i++){
  const tile=plan.tiles[i];
  await page.setViewport({width:tile.width,height:tile.height,deviceScaleFactor:1});
  await page.evaluate(({x,y})=>{const root=document.querySelector('svg');root.style.left=-x+'px';root.style.top=-y+'px';},tile);
  const bytes=await page.screenshot({type:'png'}),filename=String(i+1).padStart(4,'0')+'.png';
  await fs.writeFile(path.join(dir,filename),bytes);
  tiles.push({...tile,png:parsed.name+'.tiles/'+filename,sha256:digest(bytes)});
 }
 } finally {await browser.close();}
 const report={schema_version:'svg-raster-tiles/1',mode:'tiles',width:plan.width,height:plan.height,
  scale:1,source_sha256:digest(svg),monolithic_capacity_claimed:false,
  renderer:'Chromium native-resolution viewport crops',visual_semantics:'needs-review',tiles};
 const reportPath=path.join(parsed.dir,parsed.name+'.tiles.json');
 await fs.writeFile(reportPath,JSON.stringify(report,null,2)+'\n');
 const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
 const html='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>原尺寸分块视图</title>'+
  '<p>原尺寸分块：完整拓扑来自同一 SVG；可滚动查看，不代表单张 PNG 容量或业务验收通过。<a href="'+escape(path.basename(job.svg))+'">原始 SVG</a></p>'+
  '<div style="position:relative;width:'+plan.width+'px;height:'+plan.height+'px">'+
  tiles.map(t=>'<img alt="分块 '+t.x+','+t.y+'" src="'+escape(t.png)+'" width="'+t.width+'" height="'+t.height+'" style="position:absolute;left:'+t.x+'px;top:'+t.y+'px">').join('')+'</div></html>';
 const htmlPath=path.join(parsed.dir,parsed.name+'.tiles.html');
 await fs.writeFile(htmlPath,html);
 return {id:job.id,mode:'tiles',width:plan.width,height:plan.height,svg:path.basename(job.svg),
  tile_manifest:path.basename(reportPath),tile_viewer:path.basename(htmlPath),tile_count:tiles.length,
  monolithic_capacity_claimed:false};
}
