// Native BPMNDI viewer: no invented layout, no network, no warning-tolerant success.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {Resvg} from '@resvg/resvg-js';
import {launchBrowser} from './browser_resolver.mjs';
import {rasterPlan} from './raster_tiles.mjs';
const [specFile] = process.argv.slice(2);
const spec = JSON.parse(await fs.readFile(specFile, 'utf8'));
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const sha = data => createHash('sha256').update(data).digest('hex');
let browser;
try {
  const xml = await fs.readFile(spec.input, 'utf8');
  const font = await fs.readFile(spec.font);
  const fontCSS = `@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,${font.toString('base64')})}`;
  browser = await launchBrowser();
  const page = await browser.newPage();
  await page.setRequestInterception(true);
  const rejectedRequests = [];
  page.on('request', req => {
    if (req.url() === 'about:blank' || req.url().startsWith('data:')) req.continue();
    else { rejectedRequests.push(req.url()); req.abort(); }
  });
  await page.setContent('<!doctype html><meta charset="utf-8"><div id="canvas" style="width:1800px;height:1400px"></div>');
  await page.addStyleTag({content: fontCSS + 'text{font-family:TogafCJK,sans-serif} .djs-outline,.djs-hit{display:none}'});
  await page.addScriptTag({path:path.join(root, 'node_modules/bpmn-js/dist/bpmn-viewer.production.min.js')});
  await page.evaluate(() => document.fonts.load('14px TogafCJK'));
  const imported = await page.evaluate(async ({xml, spec}) => {
    const viewer = new window.BpmnJS({container:'#canvas', textRenderer:{defaultStyle:{fontFamily:'TogafCJK',fontSize:14},externalStyle:{fontFamily:'TogafCJK',fontSize:13}}});
    const {warnings} = await viewer.importXML(xml);
    if (warnings.length) throw new Error('BPMNDI import warnings: '+warnings.map(w=>w.message).join('; '));
    const registry = viewer.get('elementRegistry').getAll().filter(e => !e.labelTarget);
    const actual = registry.map(e=>e.id).sort();
    const expected = [spec.root_id, ...spec.shape_ids, ...spec.edge_ids].sort();
    if (JSON.stringify(actual) !== JSON.stringify(expected)) throw new Error('Rendered registry differs from BPMNDI: '+JSON.stringify({actual,expected}));
    const {svg} = await viewer.saveSVG();
    const doc = new DOMParser().parseFromString(svg, 'image/svg+xml');
    const renderedIds = [...doc.querySelectorAll('[data-element-id]')].map(e=>e.getAttribute('data-element-id'));
    for (const id of [...spec.shape_ids,...spec.edge_ids]) {
      if (!renderedIds.includes(id)) throw new Error('SVG omitted native element '+id);
    }
    const text = doc.documentElement.textContent;
    for (const [id,name] of Object.entries(spec.visible_names)) {
      if (!text.replace(/\s+/g,'').includes(name.replace(/\s+/g,''))) throw new Error('SVG lost visible name '+id);
    }
    return {svg, registry:registry.map(e=>({id:e.id,type:e.businessObject.$type,kind:e.waypoints?'edge':'shape'})), warnings:[],renderedIds};
  }, {xml, spec});
  if (rejectedRequests.length) throw new Error('BPMN attempted external requests; render refused');
  // bpmn-js emits an SVG DTD declaration; remove it so standalone output has no external DTD.
  let svg = imported.svg.replace(/<!DOCTYPE[^>]*>/g, '');
  // resvg 2.6.2 does not resolve quoted CSS paint-server fragments from bpmn-js.
  // Keep the same marker IDs/geometry and serialize their local URLs canonically.
  svg = svg.replace(/url\(['"]#([^'"]+)['"]\)/g, 'url(#$1)');
  svg = svg.replace(/(<svg\b[^>]*>)/, '$1<defs><style>'+fontCSS+'.djs-outline,.djs-hit{display:none}</style></defs>');
  const plan = rasterPlan(svg);
  if (plan.mode !== 'single') throw new Error('diagram-capacity: BPMN monolithic raster limit exceeded; no implicit downscale');
  const resvg = new Resvg(svg, {font:{fontFiles:[spec.font],loadSystemFonts:false,defaultFontFamily:'TogafCJK'},background:'white'});
  const rendered = resvg.render(), png = rendered.asPng();
  if (rendered.width < 80 || rendered.height < 40) throw new Error('Empty BPMN raster');
  const report = {status:'passed', notation_status:'rendered-explicit-bpmndi', renderer:'bpmn-js 18.31.1 Viewer / resvg 2.6.2',
    browser:browser.togafBrowser, network:'disabled', warnings:[], diagram_id:spec.diagram_id,
    shape_ids:spec.shape_ids, edge_ids:spec.edge_ids, registry:imported.registry,
    hidden_native_elements:spec.hidden_native_elements,
    svg_element_ids:imported.renderedIds, width:rendered.width,height:rendered.height,
    svg_sha256:sha(svg),png_sha256:sha(png),font_sha256:sha(font),
    serialization_adjustments:['SVG DTD removed','Local marker URL quotes normalized for resvg; IDs and geometry unchanged'],
    supported_scope:'One explicit process/collaboration BPMNDI view; common activities, event/gateway symbols, sequence/message flows, pools, lanes, collapsed/expanded subprocesses and declared data/annotation graphics.',
    limits:['Full normative BPMN semantics and all 442 constructs remain incomplete.','Choreography, vendor extensions, multiple diagrams, missing DI, hidden/extra graphics and any import warning are refused.','This operation does not grant professional visual or business acceptance.']};
  await fs.writeFile(spec.svg,svg); await fs.writeFile(spec.png,png);
  await fs.writeFile(spec.report,JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({status:'passed',shapes:spec.shape_ids.length,edges:spec.edge_ids.length}));
} catch(error) {
  const reason = String(error);
  console.error(reason);
  process.exitCode = reason.includes('browser-unavailable:') || reason.includes('diagram-capacity:') ? 3 : 1;
} finally { if (browser) await browser.close(); }
