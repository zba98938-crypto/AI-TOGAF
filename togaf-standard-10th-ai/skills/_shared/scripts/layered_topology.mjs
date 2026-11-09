#!/usr/bin/env node
// Bounded, actual directed topology pages. Original records and cross-page IDs remain inspectable.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {Graph} from 'dagre-d3-es/src/graphlib/index.js';
import {layout} from 'dagre-d3-es/src/dagre/index.js';
import {Resvg} from '@resvg/resvg-js';
const argv=process.argv.slice(2),option=name=>argv[argv.indexOf(name)+1];
const out=option('--out');
if(!argv.includes('--out')||(!argv.includes('--model')&&!argv.includes('--mermaid')))throw Error('usage: layered_topology.mjs --model model.json --view id | --mermaid chain.mmd --out NEW [--render]');
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const edgeLabel=edge=>[edge.label||edge.type||edge.id,edge.attributes?.guard?'['+(typeof edge.attributes.guard==='object'?JSON.stringify(edge.attributes.guard):edge.attributes.guard)+']':''].filter(Boolean).join(' ');
let entities,relationships,source,notation='project-labelled-directed-topology';
if(argv.includes('--model')) {
 source=await fs.readFile(option('--model'));
 const model=JSON.parse(source),view=model.views.filter(v=>v.id===option('--view'));
 if(view.length!==1)throw Error('exactly one selected view required');
 const es=new Map(model.entities.map(e=>[e.id,e])),rs=new Map(model.relationships.map(r=>[r.id,r]));
 if(es.size!==model.entities.length||rs.size!==model.relationships.length)throw Error('duplicate model ID');
 entities=view[0].entity_ids.map(id=>es.get(id));relationships=view[0].relationship_ids.map(id=>rs.get(id));
 if(entities.some(e=>!e)||relationships.some(r=>!r))throw Error('unresolved selected record');
 // Off-view endpoints are explicit boundary nodes, never silently omitted.
 const selected=new Set(entities.map(e=>e.id));
 for(const r of relationships)for(const id of [r.source,r.target])if(!selected.has(id)){
  if(!es.has(id))throw Error('unresolved relationship endpoint');entities.push({...es.get(id),boundary_node:true});selected.add(id);
 }
} else {
 source=await fs.readFile(option('--mermaid'));notation='supported-mermaid-flowchart-projection';
 const es=new Map(),rs=[];
 const atom='([A-Za-z_][\\w-]*)(?:\\[(?:"([^"\\n]*)"|([^\\]\\n]*))\\])?';
 const edge=new RegExp('^\\s*'+atom+'\\s*-->(?:\\|(?:"([^"\\n]*)"|([^|\\n]*))\\|)?\\s*'+atom+'\\s*;?\\s*$');
 const node=new RegExp('^\\s*'+atom+'\\s*;?\\s*$');
 const lines=source.toString('utf8').split(/\r?\n/);let header=false;
 const put=(id,label)=>{if(label!==undefined){if(es.has(id)&&es.get(id).explicit&&es.get(id).name!==label)throw Error('conflicting Mermaid node label');es.set(id,{id,name:label,explicit:true});}else if(!es.has(id))es.set(id,{id,name:id});};
 for(const line of lines){
  if(!line.trim()||/^\s*%%/.test(line))continue;
  if(!header){if(!/^\s*(?:flowchart|graph)\s+(?:LR|RL|TD|TB|BT)\s*;?\s*$/.test(line))throw Error('blocked: Mermaid partitioner supports explicit flowcharts only');header=true;continue;}
  const match=line.match(edge);
  if(match){put(match[1],match[2]??match[3]);put(match[6],match[7]??match[8]);rs.push({id:'mermaid-edge-'+(rs.length+1),source:match[1],target:match[6],label:match[4]??match[5]??'',type:'directed-flow'});continue;}
  const single=line.match(node);if(single){put(single[1],single[2]??single[3]);continue;}
  throw Error('blocked: unsupported Mermaid syntax retained without transformation: '+line.slice(0,80));
 }
 entities=[...es.values()];relationships=rs;
}
if(!entities.length||entities.length>100000||relationships.length>100000)throw Error('blocked: input capacity outside bounded topology limits');
if(new Set(entities.map(e=>e.id)).size!==entities.length||new Set(relationships.map(r=>r.id)).size!==relationships.length)throw Error('duplicate selected record ID');
const byId=new Map(entities.map(e=>[e.id,e])),pages=[];let current={ids:new Set(),edges:[]};
const flush=()=>{if(current.ids.size){pages.push(current);current={ids:new Set(),edges:[]};}};
for(const edge of relationships){
 const next=new Set([...current.ids,edge.source,edge.target]);
 if(next.size>12||current.edges.length>=18)flush();
 current.ids.add(edge.source);current.ids.add(edge.target);current.edges.push(edge);
}
flush();const represented=new Set(pages.flatMap(p=>[...p.ids]));
for(const entity of entities)if(!represented.has(entity.id)){if(current.ids.size>=12)flush();current.ids.add(entity.id);}
flush();
// Dense bipartite views route many sources through one another in a generic
// DAG layout. Preserve the same records in source-centred detail pages.
for(let i=0;i<pages.length;i++){
 const page=pages[i];
 if(page.edges.length>page.ids.size){
  const stars=new Map();
  for(const edge of page.edges){const star=stars.get(edge.source)||{ids:new Set(),edges:[]};star.ids.add(edge.source);star.ids.add(edge.target);star.edges.push(edge);stars.set(edge.source,star);}
  if(stars.size>1){pages.splice(i,1,...stars.values());i+=stars.size-1;}
 }
}
await fs.mkdir(out,{recursive:false});
await fs.writeFile(path.join(out,'original-input'),source);
await fs.writeFile(path.join(out,'records.json'),JSON.stringify({entities,relationships},null,2)+'\n');
const shared=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const font=argv.includes('--font')?path.resolve(option('--font')):path.join(shared,'assets/fonts/NotoSansSC.ttf');
await fs.copyFile(font,path.join(out,'font.ttf'));
const wrap=(text,limit=26)=>{const lines=[];let line='',size=0;for(const ch of String(text)){const width=ch.codePointAt(0)>255?2:1;if(size+width>limit){lines.push(line);line='';size=0;}line+=ch;size+=width;}if(line)lines.push(line);return lines;};
const membership={},rows=[];let outputBytes=source.length+(await fs.stat(path.join(out,'records.json'))).size+(await fs.stat(font)).size;
for(let i=0;i<pages.length;i++){
 const page=pages[i],graph=new Graph({multigraph:true}).setGraph({rankdir:'LR',nodesep:70,ranksep:160,marginx:50,marginy:120}).setDefaultEdgeLabel(()=>({}));
 const excerpts=[];
 for(const id of page.ids){const entity=byId.get(id);if(!entity)throw Error('unresolved endpoint');const full=wrap(entity.name);const lines=full.length>6?[...full.slice(0,4),'长名称：见完整记录']:full;if(full.length>6)excerpts.push(id);graph.setNode(id,{width:360,height:Math.max(100,45+lines.length*27),lines});(membership[id]??=[]).push(i+1);}
 for(const edge of page.edges){const lines=wrap(edgeLabel(edge),28);graph.setEdge(edge.source,edge.target,{width:230,height:Math.max(30,lines.length*24),lines},edge.id);}
 layout(graph);const width=Math.max(1200,Math.ceil(graph.graph().width+100)),height=Math.ceil(graph.graph().height+100);
 const svg=['<svg xmlns="http://www.w3.org/2000/svg" width="'+width+'" height="'+height+'" viewBox="0 0 '+width+' '+height+'"><defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8Z" fill="#46647e"/></marker></defs><rect width="100%" height="100%" fill="white"/><g font-family="Noto Sans SC, sans-serif" fill="#18334a"><text x="30" y="35" font-size="24">分层拓扑 '+(i+1)+' / '+pages.length+'</text><text x="30" y="68" font-size="18">有向关系按原记录；节点可跨页重复，完整字段和跨页索引见阅读入口。项目表达，非严格建模语言认证。</text>'];
 for(const edge of page.edges){const route=graph.edge(edge.source,edge.target,edge.id);const points=route.points.map(p=>p.x+','+p.y).join(' ');svg.push('<g data-relationship-id="'+esc(edge.id)+'"><polyline points="'+points+'" fill="none" stroke="#46647e" stroke-width="2" marker-end="url(#arrow)"/>');route.lines.forEach((s,n)=>svg.push('<text x="'+(route.x-110)+'" y="'+(route.y+n*24)+'" font-size="18">'+esc(s)+'</text>'));svg.push('</g>');}
 for(const id of page.ids){const node=graph.node(id);svg.push('<g data-entity-id="'+esc(id)+'"><rect x="'+(node.x-node.width/2)+'" y="'+(node.y-node.height/2)+'" width="'+node.width+'" height="'+node.height+'" rx="8" fill="#e8f1f8" stroke="#46647e"/>');node.lines.forEach((s,n)=>svg.push('<text x="'+(node.x-node.width/2+15)+'" y="'+(node.y-node.height/2+29+n*27)+'" font-size="21">'+esc(s)+'</text>'));svg.push('<text x="'+(node.x-node.width/2+15)+'" y="'+(node.y+node.height/2-10)+'" font-size="16">'+esc(id)+'</text></g>');}
 svg.push('</g></svg>');const bytes=Buffer.from(svg.join(''));const name='topology-'+String(i+1).padStart(4,'0');await fs.writeFile(path.join(out,name+'.svg'),bytes);outputBytes+=bytes.length;
 const row={number:i+1,svg:name+'.svg',entity_ids:[...page.ids],relationship_ids:page.edges.map(e=>e.id),svg_sha256:digest(bytes),width,height,excerpts};
 const aliases=new Map([...page.ids].map((id,n)=>[id,'n'+n]));
 const mermaid=['flowchart LR'];
 for(const id of page.ids)mermaid.push('%% entity-id: '+id+'\n'+aliases.get(id)+'["'+esc(byId.get(id).name)+'"]');
 for(const edge of page.edges)mermaid.push('%% relationship-id: '+edge.id+'\n'+aliases.get(edge.source)+' -->|"'+esc(edgeLabel(edge))+'"| '+aliases.get(edge.target));
 const definition=mermaid.join('\n')+'\n';
 row.mermaid_source=name+'.mmd';row.mermaid_characters=definition.length;row.mermaid_edges=page.edges.length;
 row.mermaid_capacity=definition.length<=50000&&page.edges.length<=500?'within-input-limits-unrendered':'blocked';
 await fs.writeFile(path.join(out,name+'.mmd'),definition);
 outputBytes+=Buffer.byteLength(definition);
 if(argv.includes('--render')){
  if(width*height>16000000||Math.max(width,height)>16384){row.raster_status='blocked';row.raster_reason='bounded page still exceeds unchanged raster safety ceiling';}
  else {const png=new Resvg(bytes,{font:{fontFiles:[font],loadSystemFonts:false},background:'white'}).render().asPng();await fs.writeFile(path.join(out,name+'.png'),png);row.png=name+'.png';row.png_sha256=digest(png);row.raster_status='complete';outputBytes+=png.length;}
 }
 rows.push(row);
 if(outputBytes>1024*1024*1024)throw Error('blocked: topology package exceeds 1GiB output guard');
}
const report={schema_version:'layered-topology/1',notation,source_sha256:digest(source),font_sha256:digest(await fs.readFile(font)),entity_count:entities.length,relationship_count:relationships.length,pages:rows,membership,
 partition_strategy:'bounded directed pages; dense bipartite pages split by source',all_records_preserved:true,monolithic_capacity_claimed:false,strict_language_conformance:false,visual_acceptance:'pending',business_acceptance:'pending',mermaid_partition_limits:{maxTextSize:50000,maxEdges:500},output_bytes:outputBytes};
await fs.writeFile(path.join(out,'manifest.json'),JSON.stringify(report,null,2)+'\n');
await fs.writeFile(path.join(out,'render-jobs.json'),JSON.stringify({font:'font.ttf',jobs:rows.filter(r=>r.mermaid_capacity!=='blocked').map(r=>({id:'mermaid-'+r.number,kind:'mmd',source:r.mermaid_source,svg:r.svg.replace('.svg','.mermaid.svg'),png:r.svg.replace('.svg','.mermaid.png'),title:'分层关系 '+r.number,legend:'项目有向关系投影；完整ID和记录见manifest；不代表原单图容量通过',is_example:true}))},null,2)+'\n');
const links=rows.map(p=>'<li><a href="'+p.svg+'">拓扑 '+p.number+'</a> · '+p.entity_ids.length+' 节点 / '+p.relationship_ids.length+' 关系'+(p.png?' · <a href="'+p.png+'">PNG</a>':'')+'</li>').join('');
await fs.writeFile(path.join(out,'index.html'),'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>分层拓扑阅读入口</title><h1>总览与分层拓扑</h1><p>完整模型 '+entities.length+' 个对象、'+relationships.length+' 个有向关系；单页最多12个对象、18条关系。正式视觉评审待完成。</p><ul>'+links+'</ul><h2>跨页对象索引</h2><pre>'+esc(JSON.stringify(membership,null,2))+'</pre><h2>完整对象与关系记录</h2><pre>'+esc(JSON.stringify({entities,relationships},null,2))+'</pre></html>');
console.log(JSON.stringify({pages:pages.length,entities:entities.length,relationships:relationships.length,rendered:rows.filter(p=>p.png).length,visual_acceptance:'pending',out}));
