// Native data DI renderer. Reads only controller-created fixed local resources.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {Resvg} from '@resvg/resvg-js';
import {launchBrowser} from './browser_resolver.mjs';
import {rasterPlan} from './raster_tiles.mjs';
import {renderDataScene} from './bpmn_data_scene.mjs';
const [specFile]=process.argv.slice(2),spec=JSON.parse(await fs.readFile(specFile,'utf8'));
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const sha=data=>createHash('sha256').update(data).digest('hex');let browser;
try{
  const xml=await fs.readFile(spec.input),font=await fs.readFile(spec.font);
  if(sha(xml)!==spec.source_sha256)throw new Error('Data DI source fingerprint differs from plan');
  const fontCSS=`@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,${font.toString('base64')})}`;
  browser=await launchBrowser();const page=await browser.newPage(),rejected=[];
  await page.setRequestInterception(true);
  page.on('request',req=>{if(req.url()==='about:blank'||req.url().startsWith('data:'))req.continue();else{rejected.push(req.url());req.abort();}});
  await page.setContent('<!doctype html><meta charset="utf-8"><div id="canvas"></div><div id="scene"></div>');
  await page.addStyleTag({content:fontCSS+'text{font-family:TogafCJK,sans-serif}'});
  await page.addScriptTag({path:path.join(root,'node_modules/bpmn-js/dist/bpmn-viewer.production.min.js')});
  await page.evaluate(()=>document.fonts.load('14px TogafCJK'));
  const rendered=await page.evaluate(renderDataScene,{spec,fontCSS});
  if(rejected.length)throw new Error('Data DI attempted external resource loading; refused');
  rendered.svg=rendered.svg.replace(/url\((?:&quot;|['"])#([^'"\)&]+)(?:&quot;|['"])\)/g,'url(#$1)');
  if(rasterPlan(rendered.svg).mode!=='single')throw new Error('diagram-capacity: Data DI monolithic raster limit exceeded');
  const raster=new Resvg(rendered.svg,{font:{fontFiles:[spec.font],loadSystemFonts:false,defaultFontFamily:'TogafCJK'},background:'white'}).render();
  if(raster.width<40||raster.height<30)throw new Error('Empty Data DI raster');const png=raster.asPng();
  const report={status:'passed',notation_status:'rendered-explicit-bpmndi',renderer:'AI-TOGAF data DI scene / bpmn-js 18.31.1 symbols / resvg 2.6.2',
    browser:browser.togafBrowser,network:'disabled',warnings:[],diagram_id:spec.diagram_id,
    shape_ids:spec.shape_ids,edge_ids:spec.edge_ids,shape_graphic_ids:spec.shape_graphic_ids,edge_graphic_ids:spec.edge_graphic_ids,
    svg_graphic_ids:rendered.graphicIds,source_geometry:rendered.geometry,geometry_origin:spec.geometry_origin,auto_layout:false,
    common_symbol_evidence:rendered.commonSymbols,label_layouts:rendered.labelLayouts,hidden_native_elements:spec.hidden_native_elements,
    data_depiction_inventory:spec.data_depiction_inventory,diagram_scope:spec.diagram_scope,source_plane_order_preserved:true,
    width:raster.width,height:raster.height,svg_sha256:sha(rendered.svg),png_sha256:sha(png),font_sha256:sha(font),
    notation_adaptations:spec.notation_adaptations,notation_projection_sha256:sha(spec.notation_xml),native_source_unchanged:true,
    limits:['Explicit partial process/collaboration DI view; unpictured data is not a validation failure.','Full applicable BPMN design-time obligations remain incomplete.','SequenceFlow data shorthand and choreography data views need separate verification.','No professional visual acceptance or organization approval is implied.']};
  await fs.writeFile(spec.svg,rendered.svg);await fs.writeFile(spec.png,png);await fs.writeFile(spec.report,JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({status:'passed',graphics:spec.graphics.length}));
}catch(error){const reason=String(error);console.error(reason);process.exitCode=reason.includes('browser-unavailable:')||reason.includes('diagram-capacity:')?3:1;}
finally{if(browser)await browser.close();}
