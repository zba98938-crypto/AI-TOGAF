// Trusted worker: all paths/flags are controller-owned; no executable task data.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {Resvg} from '@resvg/resvg-js';
import {launchBrowser} from './browser_resolver.mjs';
import {rasterPlan} from './raster_tiles.mjs';
import {renderDesignScene} from './bpmn_design_scene.mjs';
import {renderDataScene} from './bpmn_data_scene.mjs';
const file = path.resolve(process.argv[2]);
const taskRoot = path.dirname(file);
const shared = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const spec = JSON.parse(await fs.readFile(file, 'utf8'));
const input = await fs.readFile(path.join(taskRoot, 'input'), 'utf8');
const font = await fs.readFile(path.join(taskRoot, 'font.ttf'));
const fontCSS = `@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,${font.toString('base64')})} text{font-family:TogafCJK,sans-serif!important}`;
let browser;
const external = [];
try {
  browser = await launchBrowser({pipe:true, userDataDir:path.join(taskRoot,'.profile'), timeout:30000,
    args:['--disable-background-networking','--disable-component-update','--disable-sync','--no-first-run','--host-resolver-rules=MAP * ~NOTFOUND']});
  const page = await browser.newPage();
  await page.setRequestInterception(true);
  page.on('request', request => {
    if (request.url()==='about:blank' || request.url().startsWith('data:')) request.continue();
    else {external.push(request.url());request.abort();}
  });
  await page.setContent('<!doctype html><meta charset="utf-8"><style>body{margin:0}</style><div id="canvas"></div><div id="scene"></div>');
  await page.addStyleTag({content:fontCSS});
  await page.evaluate(() => document.fonts.load('18px TogafCJK'));
  let svg = input, nativeRegistry, nativeGeometry, notationAdapters, dataSceneEvidence;
  if (spec.kind==='mmd') {
    await page.addScriptTag({path:path.join(shared,'node_modules/mermaid/dist/mermaid.min.js')});
    svg = await page.evaluate(async input => {
      mermaid.initialize({startOnLoad:false,securityLevel:'strict',maxTextSize:50000,maxEdges:500,
        htmlLabels:false,fontFamily:'TogafCJK',flowchart:{htmlLabels:false,useMaxWidth:false},
        sequence:{useMaxWidth:false},theme:'base',themeVariables:{fontFamily:'TogafCJK'}});
      await mermaid.parse(input);
      const result = await mermaid.render('graphic',input);
      return result.svg;
    },input);
  } else if (spec.kind==='bpmn') {
    await page.addScriptTag({path:path.join(shared,'node_modules/bpmn-js/dist/bpmn-viewer.production.min.js')});
    if(spec.bpmn_plan.backend==='native-design-di') {
      const result=await page.evaluate(renderDesignScene,{xml:input,spec:spec.bpmn_plan,fontCSS});
      svg=result.svg;
      nativeRegistry=result.graphicIds;
      nativeGeometry=result.geometry;
      notationAdapters=spec.bpmn_plan.notation_adaptations;
    } else if(spec.bpmn_plan.backend==='native-data-di') {
      if(createHash('sha256').update(input).digest('hex')!==spec.bpmn_plan.source_sha256)
        throw Error('Data DI source fingerprint differs from controller plan');
      const result=await page.evaluate(renderDataScene,{spec:spec.bpmn_plan,fontCSS});
      svg=result.svg;nativeRegistry=result.graphicIds;nativeGeometry=result.geometry;
      notationAdapters=spec.bpmn_plan.notation_adaptations;
      dataSceneEvidence={backend:'native-data-di',source_sha256:spec.bpmn_plan.source_sha256,
        common_symbol_evidence:result.commonSymbols,label_layouts:result.labelLayouts,
        data_depiction_inventory:spec.bpmn_plan.data_depiction_inventory,
        hidden_native_elements:spec.bpmn_plan.hidden_native_elements,
        geometry_origin:spec.bpmn_plan.geometry_origin,diagram_scope:spec.bpmn_plan.diagram_scope,
        source_plane_order_preserved:true,auto_layout:false};
    } else {
      const result = await page.evaluate(async ({input,plan}) => {
      const viewer=new BpmnJS({container:'#canvas',textRenderer:{defaultStyle:{fontFamily:'TogafCJK'}}});
      const {warnings}=await viewer.importXML(input);
      if(warnings.length)throw Error('BPMNDI warnings: '+warnings.map(w=>w.message).join('; '));
      const registry=viewer.get('elementRegistry').getAll().filter(e=>!e.labelTarget).map(e=>e.id).sort();
      const expected=[plan.root_id,...plan.shape_ids,...plan.edge_ids].sort();
      if(JSON.stringify(registry)!==JSON.stringify(expected))throw Error('BPMNDI registry differs from declared view');
      const {svg}=await viewer.saveSVG();return {svg,registry};
    },{input,plan:spec.bpmn_plan});
      svg=result.svg;
      nativeRegistry=result.registry;
    }
    svg=svg.replace(/<!DOCTYPE[^>]*>/g,'').replace(/url\((?:&quot;|['"])#([^'"&]+)(?:&quot;|['"])\)/g,'url(#$1)');
  }
  if (external.length) throw Error('external resources refused');
  if (/<[^>]+\sclass=["'][^"']*\berror-(?:icon|text)\b[^"']*["'][^>]*>/.test(svg)) throw Error('renderer returned error SVG');
  if(!/viewBox=/.test(svg)) {
    const dimensions = await page.evaluate(svg => {
      const doc=new DOMParser().parseFromString(svg,'image/svg+xml');
      const root=doc.documentElement;return {width:Number(root.getAttribute('width')),height:Number(root.getAttribute('height'))};
    },svg);
    if(!Number.isFinite(dimensions.width)||!Number.isFinite(dimensions.height)||dimensions.width<=0||dimensions.height<=0)
      throw Error('SVG requires explicit dimensions or viewBox');
    svg=svg.replace(/(<svg\b)/,`$1 viewBox="0 0 ${dimensions.width} ${dimensions.height}"`);
  }
  svg=svg.replace(/(<svg\b[^>]*>)/,'$1<defs><style>'+fontCSS+'</style></defs>');
  const plan=rasterPlan(svg);
  if(plan.mode!=='single')throw Error('diagram-capacity: raster exceeds fixed worker limit');
  await page.setViewport({width:plan.width,height:plan.height,deviceScaleFactor:1});
  await page.setContent(`<meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src 'none';script-src 'none';style-src 'unsafe-inline';font-src data:;img-src data:;connect-src 'none'"><style>body{margin:0}</style>`+svg);
  await page.evaluate(() => document.fonts.ready);
  const geometry=await page.evaluate(() => {
    const root=document.querySelector('svg'), view=root.viewBox.baseVal;
    const bounds=view.width?{x:view.x,y:view.y,width:view.width,height:view.height}:root.getBBox();
    const labels=[...root.querySelectorAll('text')].filter(e=>e.textContent.trim()).map(e=>{
      const b=e.getBBox(),m=root.getCTM().inverse().multiply(e.getCTM());
      const corners=[new DOMPoint(b.x,b.y),new DOMPoint(b.x+b.width,b.y),new DOMPoint(b.x,b.y+b.height),new DOMPoint(b.x+b.width,b.y+b.height)].map(p=>p.matrixTransform(m));
      const x=Math.min(...corners.map(p=>p.x)),y=Math.min(...corners.map(p=>p.y));
      return {text:e.textContent,x,y,width:Math.max(...corners.map(p=>p.x))-x,height:Math.max(...corners.map(p=>p.y))-y};});
    const outside=labels.filter(b=>b.x<bounds.x-2||b.y<bounds.y-2||b.x+b.width>bounds.x+bounds.width+2||b.y+b.height>bounds.y+bounds.height+2);
    return {label_count:labels.length,outside:outside.map(b=>b.text),font_loaded:document.fonts.check('18px TogafCJK'),bounds};
  });
  if(geometry.outside.length)throw Error('text outside SVG bounds: '+geometry.outside.join(', '));
  if(!geometry.font_loaded)throw Error('bundled Chinese font did not load');
  await page.screenshot({path:path.join(taskRoot,'browser-screenshot.png')});
  const raster=new Resvg(svg,{font:{fontFiles:[path.join(taskRoot,'font.ttf')],loadSystemFonts:false,defaultFontFamily:'TogafCJK'},background:'white'}).render();
  if(raster.width<20||raster.height<20)throw Error('empty raster');
  await fs.writeFile(path.join(taskRoot,'diagram.svg'),svg);
  await fs.writeFile(path.join(taskRoot,'diagram.png'),raster.asPng());
  await fs.writeFile(path.join(taskRoot,'diagram.json'),JSON.stringify({status:'pass',mode:'controlled-local-process',
    kind:spec.kind,browser:browser.togafBrowser,external_requests:external,text_geometry:geometry,
    width:raster.width,height:raster.height,native_registry:nativeRegistry,native_geometry:nativeGeometry,
    notation_adapters:notationAdapters,
    bpmn_data_di:dataSceneEvidence,
    source_authoritative:true,derived_layout:spec.kind==='mmd'||spec.kind==='uml-class-layout',
    native_uml_source_sha256:spec.uml_source_sha256,uml_layout:spec.uml_layout,
    uml_profile_applications:spec.uml_profile_applications,
    layout_choice:spec.kind==='uml-class-layout'?'explicit task kind selected derived class layout':undefined,
    full_standard_acceptance:false},null,2));
} catch(error) {console.error(String(error));process.exitCode=1;}
finally {if(browser)await browser.close();}
