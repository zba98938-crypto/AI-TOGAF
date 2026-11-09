import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {launchBrowser} from '../../../skills/_shared/scripts/browser_resolver.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const base=path.join(root,'togaf-standard-10th-ai/fundamental/web-2025');
const work=path.join(root,'togaf-standard-10th-ai/maintenance/work/browser/fundamental');
await fs.mkdir(work,{recursive:true});
const bytes=await fs.readFile(path.join(base,'manifest.json'));
const manifest=JSON.parse(bytes);
const browser=await launchBrowser({userDataDir:path.join(work,'profile'),env:{...process.env,TMPDIR:work,TMP:work,TEMP:work},args:['--disable-background-networking','--disable-component-update','--no-first-run']});
const report={schema_version:'fundamental-offline-browser-validation/1',manifest_sha256:createHash('sha256').update(bytes).digest('hex'),checks:[],errors:[],scope:'Offline resource loading and heading/text rendering only; not semantic source review.'};
try{
 const page=await browser.newPage();await page.setOfflineMode(true);await page.setViewport({width:1440,height:1000,deviceScaleFactor:1});
 for(const doc of manifest.documents){
  await page.goto(pathToFileURL(path.join(base,doc.offline_html)).href,{waitUntil:'load'});
  const state=await page.evaluate(()=>({title:document.title,chapterHeadings:[...document.querySelectorAll('#content h2')].map(x=>x.textContent),images:[...document.images].map(x=>({src:x.getAttribute('src'),loaded:x.complete&&x.naturalWidth>0})),textLength:document.querySelector('#content').innerText.length,remoteResources:performance.getEntriesByType('resource').map(x=>x.name).filter(x=>/^https?:/.test(x))}));
  if(state.images.some(x=>!x.loaded)||state.remoteResources.length||state.textLength<10000)throw Error(JSON.stringify({doc:doc.id,...state}));
  if(doc.id.includes('01-'))await page.screenshot({path:path.join(base,'offline-introduction-preview.png')});
  if(doc.id.includes('05-')){await page.$eval('#content .imageblock',el=>el.scrollIntoView());await page.screenshot({path:path.join(base,'offline-architecture-content-preview.png')});}
  report.checks.push({document_id:doc.id,title:state.title,images_loaded:state.images.length,content_text_characters:state.textLength,remote_requests:state.remoteResources.length});
 }
}catch(e){report.errors.push(String(e));}finally{await browser.close();}
report.passed=!report.errors.length;
await fs.writeFile(path.join(base,'offline-browser-validation.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));if(!report.passed)process.exitCode=1;
