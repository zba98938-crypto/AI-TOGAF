// Actual local UI import/edit/save/export-resource checks; no model requests.
import fs from 'node:fs/promises';
import path from 'node:path';
import net from 'node:net';
import {spawn,execFile} from 'node:child_process';
import {promisify} from 'node:util';
import {once} from 'node:events';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {launchBrowser} from '../togaf-standard-10th-ai/skills/_shared/scripts/browser_resolver.mjs';
const repo=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const args=process.argv.slice(2);
const require=(value,message)=>{if(!value)throw Error(message);};
require(args.length===2&&args[0]==='--out','Use --out NEW_DIRECTORY');
const out=path.resolve(args[1]);
const relative=path.relative(path.join(repo,'output'),out);
require(relative&&!relative.startsWith('..')&&!path.isAbsolute(relative),'Evidence must use repository output');
await fs.mkdir(out);
const sha=data=>createHash('sha256').update(data).digest('hex');
const resourceEqual=(a,b)=>JSON.stringify(a.map(r=>[r.path,r.payload_encoding,r.content,r.sha256]))===JSON.stringify(b.map(r=>[r.path,r.payload_encoding,r.content,r.sha256]));
const ns='http://www.omg.org/spec/BPMN/20100524/MODEL';
const xml='\ufeff<?xml version="1.0" encoding="UTF-8"?>\r\n<definitions xmlns="'+ns+'" xmlns:r="urn:shared" targetNamespace="urn:main">\r\n<import namespace="urn:shared" location="../shared/model.bpmn" importType="'+ns+'"/>\r\n<collaboration id="C"><participant id="A" processRef="r:P"/></collaboration>\r\n</definitions>\r\n';
const child=Buffer.from('\ufeff<definitions xmlns="'+ns+'" targetNamespace="urn:shared">\r\n<process id="P" name="订单资源"/>\r\n</definitions>\r\n');
const resource={path:'shared/model.bpmn',payload_encoding:'base64',content:child.toString('base64'),sha256:sha(child)};
const fixture=path.join(out,'input-package.json');
const fixtureRoot=path.join(out,'fixture-source');await fs.mkdir(path.join(fixtureRoot,'nested'),{recursive:true});await fs.mkdir(path.join(fixtureRoot,'shared'),{recursive:true});
await fs.writeFile(path.join(fixtureRoot,'nested/main.bpmn'),xml);await fs.writeFile(path.join(fixtureRoot,'shared/model.bpmn'),child);
const imported=await promisify(execFile)('python3',['-B',path.join(repo,'togaf-standard-10th-ai/skills/_shared/scripts/standards.py'),'import','--language','bpmn','--version','2.0.2','--input',path.join(fixtureRoot,'nested/main.bpmn'),'--package-root',fixtureRoot,'--out',fixture],{cwd:repo,env:{PATH:process.env.PATH,PYTHONDONTWRITEBYTECODE:'1'},timeout:30000,maxBuffer:2*1024*1024});
await fs.writeFile(path.join(out,'fixture-import.json'),imported.stdout);
const report={schema_version:'bpmn-resource-ui/1',runtime_mode:'local-test-controller',model_requests:0,passed:false,checks:[],errors:[],blocked_requests:[],source_sha256:{},source_authority:'immutable native.xml and native.resources bytes'};
for(const name of ['workbench/native.py','workbench/server.py','workbench/web/app.js','workbench/web/index.html','workbench/web/styles.css','workbench/verify_bpmn_resources_ui.mjs','togaf-standard-10th-ai/skills/_shared/scripts/standards.py','togaf-standard-10th-ai/skills/_shared/scripts/bpmn_imports.py'])report.source_sha256[name]=sha(await fs.readFile(path.join(repo,name)));
let browser,server,page,profile,ownedBrowser,serverLog='';
const exists=pid=>{try{process.kill(pid,0);return true;}catch(error){if(error.code==='ESRCH')return false;throw error;}};
const until=async(fn,timeout=15000)=>{const end=Date.now()+timeout;while(Date.now()<end){if(await fn())return;await new Promise(resolve=>setTimeout(resolve,100));}throw Error('Local UI timeout');};
try{
  const reservation=net.createServer();reservation.listen(0,'127.0.0.1');await once(reservation,'listening');const port=reservation.address().port;await new Promise(resolve=>reservation.close(resolve));
  const origin='http://127.0.0.1:'+port;
  const env={PATH:process.env.PATH,PYTHONDONTWRITEBYTECODE:'1',PYTHONIOENCODING:'utf-8',LANG:'en_US.UTF-8',...(process.env.TOGAF_BROWSER_PATH?{TOGAF_BROWSER_PATH:process.env.TOGAF_BROWSER_PATH}:{})};
  server=spawn('python3',['-B',path.join(repo,'workbench/server.py'),'--port',String(port),'--data-dir',path.join(out,'data')],{cwd:repo,env,stdio:['ignore','pipe','pipe']});
  server.stdout.on('data',chunk=>serverLog+=chunk);server.stderr.on('data',chunk=>serverLog+=chunk);
  await until(async()=>{try{return(await fetch(origin+'/api/health')).ok;}catch{return false;}});
  profile=path.join(out,'browser-profile');
  browser=await launchBrowser({userDataDir:profile,timeout:30000,env:{...env,TMPDIR:out,TMP:out,TEMP:out},args:['--disable-background-networking','--disable-component-update','--no-first-run']});
  ownedBrowser=browser.process();report.browser={...browser.togafBrowser,owned_pid:ownedBrowser?.pid};
  page=await browser.newPage();page.setDefaultTimeout(15000);
  page.on('pageerror',error=>report.errors.push(String(error)));
  await page.setRequestInterception(true);page.on('request',request=>{let allowed=false;try{const url=new URL(request.url());allowed=url.origin===origin||['data:','blob:','about:'].includes(url.protocol);}catch{}if(!allowed)report.blocked_requests.push(request.url());(allowed?request.continue():request.abort('blockedbyclient')).catch(()=>{});});
  await page.setViewport({width:1440,height:1080,deviceScaleFactor:1});await page.goto(origin,{waitUntil:'networkidle0'});
  await page.waitForFunction(()=>document.querySelector('#connection').textContent.includes('已连接'));
  await(await page.$('#native-import-file')).uploadFile(fixture);await page.waitForSelector('#modal[open]');await page.click('#modal-content button[type="submit"]');await page.waitForSelector('#native-source');await page.waitForFunction(()=>!document.querySelector('#modal').open);
  const projectId=await page.$eval('.project-item.active',node=>node.dataset.project);
  const detail=()=>page.evaluate(async id=>(await fetch('/api/projects/'+id)).json(),projectId);
  const initial=await detail();
  require(initial.native.xml===xml,'Root BOM/CRLF bytes changed on import');
  require(resourceEqual(initial.native.resources,[resource]),'Resource bytes changed on import');
  require(initial.native.document_path==='nested/main.bpmn','Document base was lost');
  require(await page.$eval('#native-language',node=>node.disabled),'Resource package can be relabeled as another language');
  require((await page.$eval('#native-resource-summary',node=>node.textContent)).includes('导入资源：1'),'Resource package is hidden from user');
  report.checks.push({id:'package-import-root-resource-path-authority',passed:true,version:initial.head_version});
  const edited=xml.replace('id="A"','id="A" name="编辑主文档"');
  await page.$eval('#native-source',(node,value)=>{node.value=value;node.dispatchEvent(new Event('input',{bubbles:true}));},edited);
  await page.click('#save');await page.waitForSelector('#modal[open]');await page.type('#modal-content input[name="message"]','主文档修订，保留导入资源');await page.click('#modal-content button[type="submit"]');await page.waitForFunction(previous=>document.querySelector('#version-label').title!==previous,{},initial.head_version);await page.waitForFunction(()=>!document.querySelector('#modal').open&&!document.querySelector('#native-preview').disabled);
  const saved=await detail();
  // Textarea editing uses the browser's documented LF normalization.
  require(saved.native.xml===edited.replace(/\r\n/g,'\n'),'Edited root source differs from textarea input');
  require(resourceEqual(saved.native.resources,initial.native.resources),'Root edit removed or changed imported resource');
  report.checks.push({id:'root-edit-save-resource-preservation',passed:true,version:saved.head_version,root_sha256:saved.native.source_sha256,resource_sha256:resource.sha256});
  let exported;
  await page.evaluate(()=>{window.nativeBlob=null;const original=URL.createObjectURL;URL.createObjectURL=blob=>{window.nativeBlob=blob;return original(blob);};});
  await page.click('#native-export');exported=await page.evaluate(async()=>JSON.parse(await window.nativeBlob.text()));
  require(exported.xml===saved.native.xml&&resourceEqual(exported.resources,saved.native.resources)&&exported.document_path===saved.native.document_path,'Native export lost authoritative package content');
  await fs.writeFile(path.join(out,'exported-native.json'),JSON.stringify(exported,null,2));report.checks.push({id:'native-json-export-retains-resource-bytes',passed:true});
  await page.click('#native-auto-layout');await page.click('#native-preview');let job;
  await until(async()=>{job=(await detail()).jobs.find(row=>row.kind==='native'&&row.version===saved.head_version);return job&&['succeeded','blocked','failed'].includes(job.status);},45000);
  require(job.status==='blocked'&&job.native_preview.category==='capability_uncovered','Cross-document rendering was not blocked before renderer');
  require(!job.outputs.some(row=>/\.svg$|\.png$/.test(row.name)),'Unsupported cross-document render produced images');
  await page.waitForFunction(()=>document.querySelector('#native-preview-result').textContent.includes('Cross-document BPMN semantics/DI/rendering'));
  report.checks.push({id:'cross-document-preview-prelaunch-refusal',passed:true,job:job.id});
  await page.screenshot({path:path.join(out,'desktop.png'),fullPage:true});
  await page.reload({waitUntil:'networkidle0'});await page.click('[data-tab="native"]');await page.waitForSelector('#native-source');require(resourceEqual((await detail()).native.resources,saved.native.resources),'Resources lost after reload');
  report.checks.push({id:'resource-persistence-after-reload',passed:true});
  await page.setViewport({width:390,height:844,deviceScaleFactor:1});const geometry=await page.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth}));require(geometry.width<=geometry.viewport+1,'Mobile page overflow');report.mobile_geometry=geometry;await page.screenshot({path:path.join(out,'mobile.png'),fullPage:true});
  report.checks.push({id:'mobile-resource-source-layout',passed:true});report.passed=true;
}catch(error){report.errors.push(String(error));if(page)try{await page.screenshot({path:path.join(out,'failure.png'),fullPage:true});}catch{}process.exitCode=1;}
finally{
  if(browser)try{await browser.close();}catch(error){report.errors.push(String(error));}
  if(server&&server.exitCode===null&&server.signalCode===null){server.kill('SIGTERM');await Promise.race([once(server,'exit'),new Promise(resolve=>setTimeout(resolve,5000))]);if(server.exitCode===null&&server.signalCode===null){server.kill('SIGKILL');await once(server,'exit');}}
  if(profile)await fs.rm(profile,{recursive:true,force:true});
  report.cleanup={browser_alive:ownedBrowser?.pid?exists(ownedBrowser.pid):false,server_alive:server?.pid?exists(server.pid):false,profile_removed:profile?await fs.access(profile).then(()=>false,()=>true):true};
  await fs.writeFile(path.join(out,'server.log'),serverLog);
  report.source_changed_during_run=[];for(const[name,expected]of Object.entries(report.source_sha256))if(sha(await fs.readFile(path.join(repo,name)))!==expected)report.source_changed_during_run.push(name);
  report.passed=report.passed&&!report.errors.length&&!report.blocked_requests.length&&!report.cleanup.browser_alive&&!report.cleanup.server_alive&&report.cleanup.profile_removed&&!report.source_changed_during_run.length;
  if(!report.passed)process.exitCode=1;
  report.output_sha256={};for(const name of ['input-package.json','exported-native.json','desktop.png','mobile.png','failure.png','server.log'])try{report.output_sha256[name]=sha(await fs.readFile(path.join(out,name)));}catch{}
  await fs.writeFile(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}
