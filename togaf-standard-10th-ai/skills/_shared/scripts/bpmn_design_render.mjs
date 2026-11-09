// Native DI scene: Conversation/Choreography primitives plus installed bpmn-js
// ordinary symbols. No source rewriting, network, or implicit node/edge layout.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {Resvg} from '@resvg/resvg-js';
import {launchBrowser} from './browser_resolver.mjs';
import {rasterPlan} from './raster_tiles.mjs';
import {renderDesignScene} from './bpmn_design_scene.mjs';
const [specFile] = process.argv.slice(2);
const spec = JSON.parse(await fs.readFile(specFile, 'utf8'));
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const sha = data => createHash('sha256').update(data).digest('hex');
let browser;
try {
  const xml = await fs.readFile(spec.input, 'utf8'), font = await fs.readFile(spec.font);
  if (sha(xml) !== spec.source_sha256) throw new Error('Native source fingerprint differs from planned DI');
  const fontCSS = `@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,${font.toString('base64')})}`;
  browser = await launchBrowser();
  const page = await browser.newPage();
  const rejectedRequests = [];
  await page.setRequestInterception(true);
  page.on('request', req => {
    if (req.url() === 'about:blank' || req.url().startsWith('data:')) req.continue();
    else { rejectedRequests.push(req.url()); req.abort(); }
  });
  await page.setContent('<!doctype html><meta charset="utf-8"><div id="canvas" style="width:1800px;height:1400px"></div><div id="scene"></div>');
  await page.addStyleTag({content:fontCSS+'text{font-family:TogafCJK,sans-serif}'});
  await page.addScriptTag({path:path.join(root,'node_modules/bpmn-js/dist/bpmn-viewer.production.min.js')});
  await page.evaluate(() => document.fonts.load('14px TogafCJK'));
  const rendered = await page.evaluate(renderDesignScene,{xml,spec,fontCSS});
  if (rejectedRequests.length) throw new Error('Native BPMN attempted external requests; refused');
  rendered.svg=rendered.svg.replace(/url\((?:&quot;|['"])#([^'"\)&]+)(?:&quot;|['"])\)/g,'url(#$1)');
  const plan=rasterPlan(rendered.svg);
  if (plan.mode!=='single') throw new Error('diagram-capacity: native BPMN monolithic raster limit exceeded');
  const raster=new Resvg(rendered.svg,{font:{fontFiles:[spec.font],loadSystemFonts:false,defaultFontFamily:'TogafCJK'},background:'white'}).render();
  const png=raster.asPng();
  if (raster.width<40||raster.height<30) throw new Error('Empty native BPMN raster');
  const report={status:'passed',notation_status:'rendered-explicit-bpmndi',renderer:'AI-TOGAF native DI scene / bpmn-js 18.31.1 symbols / resvg 2.6.2',
    browser:browser.togafBrowser,network:'disabled',warnings:[],diagram_id:spec.diagram_id,
    shape_ids:spec.shape_ids,edge_ids:spec.edge_ids,shape_graphic_ids:spec.shape_graphic_ids,edge_graphic_ids:spec.edge_graphic_ids,
    svg_graphic_ids:rendered.graphicIds,source_geometry:rendered.geometry,source_coordinate_geometry:rendered.sourceCoordinateGeometry,source_plane_order_preserved:true,data_depiction_inventory:spec.data_depiction_inventory,included_choreography_ids:spec.included_choreography_ids,geometry_origin:spec.geometry_origin,auto_layout:false,
    common_symbol_evidence:rendered.commonSymbols,label_layouts:rendered.labelLayouts,hidden_native_elements:spec.hidden_native_elements,
    width:raster.width,height:raster.height,svg_sha256:sha(rendered.svg),png_sha256:sha(png),font_sha256:sha(font),
    supported_scope:'Explicit Conversation/Choreography view, task/sub/call notation, repeated Participant Bands, optional envelopes and loop/multiplicity markers; installed bpmn-js ordinary process symbols.',
    notation_adaptations:spec.notation_adaptations,notation_projection_sha256:sha(spec.notation_xml),native_source_unchanged:true,
    serialization_adjustments:['Local SVG marker URL quotes normalized for resvg; marker geometry and native DI unchanged'],
    limits:['Full applicable normative obligation coverage remains incomplete.','Missing authoritative DI is blocked. Recursive expanded call graphs require a finite explicit view.','No professional visual acceptance or organization approval is implied.']};
  await fs.writeFile(spec.svg,rendered.svg);await fs.writeFile(spec.png,png);await fs.writeFile(spec.report,JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({status:'passed',graphics:spec.graphics.length}));
} catch(error) {
  const reason=String(error);console.error(reason);
  process.exitCode=reason.includes('browser-unavailable:')||reason.includes('diagram-capacity:')?3:1;
} finally {if(browser)await browser.close();}
