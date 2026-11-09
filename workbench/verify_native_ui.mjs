// Reproducible local-controller UI check; no model service or downloaded runtime.
import fs from 'node:fs/promises';
import path from 'node:path';
import net from 'node:net';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {launchBrowser} from '../togaf-standard-10th-ai/skills/_shared/scripts/browser_resolver.mjs';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
function require(value, message) { if (!value) throw Error(message); }
require(args.length === 2 && args[0] === '--out', 'Use --out NEW_DIRECTORY');
const out = path.resolve(args[1]);
const relative = path.relative(path.join(repo, 'output'), out);
require(relative && relative !== '..' && !relative.startsWith('..' + path.sep) && !path.isAbsolute(relative), 'Evidence must be in repository output');
for (let cursor = path.dirname(out); cursor !== path.dirname(repo); cursor = path.dirname(cursor)) {
  require(!(await fs.lstat(cursor)).isSymbolicLink(), 'Symlink evidence paths are forbidden');
  if (cursor === repo) break;
}
await fs.mkdir(out); // Reject previously used evidence directories.
const sha = data => createHash('sha256').update(data).digest('hex');
const xml = '\ufeff' + `<?xml version="1.0" encoding="UTF-8"?>\r\n<!-- <script>window.nativeInjected=true</script> -->\r\n<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:version="2.5.1" xmi:id="M" name="订单模型">\r\n <packagedElement xmi:type="uml:Class" xmi:id="C" name="订单"/>\r\n</uml:Model>`;
const fixture = path.join(out, 'native-input.uml');
await fs.writeFile(fixture, xml, 'utf8');
const bpmnSource = path.join(repo,'togaf-standard-10th-ai/skills/_shared/examples/native-modeling/order-collaboration.bpmn');
const bpmn = await fs.readFile(bpmnSource);
const bpmnFixture = path.join(out,'native-input.bpmn');
await fs.writeFile(bpmnFixture,bpmn);
const noDI = `<?xml version="1.0" encoding="UTF-8"?>\n<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" id="D" targetNamespace="urn:workbench:ui"><process id="P" isExecutable="false"><startEvent id="S" name="开始"/><endEvent id="E" name="完成"/><sequenceFlow id="F" sourceRef="S" targetRef="E"/></process></definitions>`;
const noDIFixture=path.join(out,'native-input-nodi.bpmn');await fs.writeFile(noDIFixture,noDI);
const report = {schema_version:'workbench-native-ui/1',runtime_mode:'local-test-controller',actor_sandbox_used:false,
  source_authority:'native.xml UTF-8 bytes',checks:[],errors:[],blocked_requests:[],passed:false,
  fixture_sha256:sha(Buffer.from(xml)),source_sha256:{}};
report.bpmn_fixture={source:path.relative(repo,bpmnSource),sha256:sha(bpmn)};
for (const name of ['server.py','native.py','web/app.js','web/index.html','web/styles.css','verify_native_ui.mjs']) {
  report.source_sha256['workbench/' + name] = sha(await fs.readFile(path.join(repo, 'workbench', name)));
}
let browser, server, browserProcess, profile, page, serverLog = '';
const exists = pid => { try { process.kill(pid, 0); return true; } catch (error) { if (error.code === 'ESRCH') return false; throw error; } };
const until = async (fn, milliseconds=15000) => {
  const deadline=Date.now()+milliseconds;
  while (Date.now()<deadline) { if(await fn())return; await new Promise(resolve=>setTimeout(resolve,100)); }
  throw Error('Local operation did not finish within ' + milliseconds + 'ms');
};
try {
  const reservation = net.createServer();
  reservation.listen(0, '127.0.0.1');
  await once(reservation, 'listening');
  const port = reservation.address().port;
  await new Promise(resolve=>reservation.close(resolve));
  const env = {PATH:process.env.PATH,PYTHONDONTWRITEBYTECODE:'1',PYTHONIOENCODING:'utf-8',LANG:'en_US.UTF-8',
    ...(process.env.TOGAF_BROWSER_PATH?{TOGAF_BROWSER_PATH:process.env.TOGAF_BROWSER_PATH}:{})};
  server = spawn('python3', ['-B', path.join(repo, 'workbench/server.py'), '--port', String(port), '--data-dir', path.join(out, 'data')],
    {cwd:repo,env,stdio:['ignore','pipe','pipe']});
  server.stdout.on('data',chunk=>serverLog+=chunk);server.stderr.on('data',chunk=>serverLog+=chunk);
  server.on('error',error=>report.errors.push(String(error)));
  const origin='http://127.0.0.1:'+port;
  await until(async()=>{try{return(await fetch(origin+'/api/health')).ok;}catch{return false;}});
  profile = path.join(out,'browser-profile');
  browser = await launchBrowser({userDataDir:profile,timeout:30000,env:{...env,TMPDIR:out,TMP:out,TEMP:out},
    args:['--disable-background-networking','--disable-component-update','--no-first-run']});
  browserProcess = browser.process();
  report.browser={...browser.togafBrowser,owned_pid:browserProcess?.pid};report.server={origin,owned_pid:server.pid};
  page=await browser.newPage();page.setDefaultTimeout(15000);
  page.on('pageerror',error=>report.errors.push(String(error)));
  page.on('console',message=>{if(message.type()==='error')report.errors.push(message.text());});
  await page.setRequestInterception(true);
  page.on('request',resource=>{
    let allowed=false;
    try{const url=new URL(resource.url());allowed=url.origin===origin || resource.url()==='about:blank'
      || (url.protocol==='data:'&&['image','font'].includes(resource.resourceType()));}catch{}
    if(!allowed)report.blocked_requests.push(resource.url());
    (allowed?resource.continue():resource.abort('blockedbyclient')).catch(()=>{});
  });
  await page.setViewport({width:1440,height:1080,deviceScaleFactor:1});
  await page.goto(origin,{waitUntil:'networkidle0'});
  await page.waitForFunction(()=>document.querySelector('#connection').textContent.includes('已连接'));
  await (await page.$('#native-import-file')).uploadFile(fixture);
  await page.waitForSelector('#modal[open]');
  await page.click('#modal-content button[type="submit"]');
  await page.waitForSelector('#native-source');
  await page.waitForFunction(()=>!document.querySelector('#modal').open);
  const projectId=await page.$eval('.project-item.active',node=>node.dataset.project);
  const detail=()=>page.evaluate(async id=>(await fetch('/api/projects/'+id)).json(),projectId);
  const initial=await detail();
  require(initial.native.xml===xml && initial.native.source_sha256===report.fixture_sha256,'Import normalized authoritative BOM/CRLF source');
  require(!await page.evaluate(()=>Boolean(window.nativeInjected)),'Native XML was executed in the page');
  report.checks.push({id:'native-import-exact-bytes',passed:true,version:initial.head_version,source_sha256:initial.native.source_sha256});
  report.checks.push({id:'native-source-dom-escaping',passed:true});
  await page.click('#native-diagnose');
  await page.waitForFunction(()=>document.querySelector('#native-diagnostics').textContent.includes('未完成'));
  require(await page.$$eval('.native-diagnostic-group',nodes=>nodes.length)===3,'Diagnostics do not show three separate categories');
  report.checks.push({id:'native-three-diagnostic-categories',passed:true});
  const edited=xml.replace('name="订单"','name="订单修订"').replace(/\r\n/g,'\n');
  const modifier=process.platform==='darwin'?'Meta':'Control';
  await page.focus('#native-source');
  await page.$eval('#native-source',node=>node.select());
  require(await page.$eval('#native-source',node=>node.selectionEnd-node.selectionStart===node.value.length),'Source editor selection failed');
  await page.keyboard.type(edited);
  require(await page.$eval('#native-preview',node=>node.disabled),'Unsaved native draft preview is enabled');
  await page.keyboard.down(modifier);await page.keyboard.press('KeyS');await page.keyboard.up(modifier);
  await page.waitForSelector('#modal[open]');
  await page.type('#modal-content input[name="message"]','原生 UI 键盘修改');
  await page.click('#modal-content button[type="submit"]');
  await page.waitForFunction(previous=>document.querySelector('#version-label').title!==previous,{},initial.head_version);
  await page.waitForFunction(()=>!document.querySelector('#modal').open&&!document.querySelector('#native-preview').disabled);
  const saved=await detail();
  require(saved.native.xml===edited && saved.head_version!==initial.head_version,'Native editor save did not create exact new source version');
  report.checks.push({id:'native-keyboard-edit-save-version',passed:true,version:saved.head_version,source_sha256:saved.native.source_sha256});
  await page.click('#native-auto-layout');
  require(await page.$eval('#native-auto-layout',node=>node.checked),'Explicit automatic layout checkbox did not toggle');
  await page.click('#native-preview');
  await page.waitForFunction(()=>{const img=document.querySelector('.native-preview-image');return img?.complete&&img.naturalWidth>0;},{timeout:45000});
  const completed=await detail();const job=completed.jobs.find(row=>row.kind==='native'&&row.version===saved.head_version);
  require(job?.status==='succeeded' && job.native_preview.derived_layout && !job.full_language_acceptance,'Preview status or complete-language status differs');
  report.checks.push({id:'native-version-bound-uml-preview',passed:true,job:job.id,version:job.version,source_sha256:job.native_source_sha256});
  await page.screenshot({path:path.join(out,'native-desktop.png'),fullPage:true});
  await page.focus('[data-tab="versions"]');await page.keyboard.press('Enter');
  await page.waitForSelector('#panel-versions:not([hidden])');
  await page.click('#compare-versions');
  await page.waitForFunction(()=>document.querySelector('#diff-results').textContent.includes('native'));
  report.checks.push({id:'native-keyboard-tab-and-version-diff',passed:true});
  await page.focus('[data-tab="native"]');await page.keyboard.press('Enter');
  await page.reload({waitUntil:'networkidle0'});
  await page.click('[data-tab="native"]');await page.waitForSelector('#native-source');
  require((await detail()).native.xml===edited,'Reload lost native source');
  await page.waitForFunction(()=>{const img=document.querySelector('.native-preview-image');return img?.complete&&img.naturalWidth>0;});
  report.checks.push({id:'native-reload-persistence',passed:true});
  await page.setViewport({width:390,height:844,deviceScaleFactor:1});
  const geometry=await page.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth,
    editor_width:document.querySelector('#native-source').getBoundingClientRect().width}));
  require(geometry.width<=geometry.viewport+1,'Native mobile page overflows: '+JSON.stringify(geometry));
  report.checks.push({id:'native-mobile-layout',passed:true,...geometry});
  await page.screenshot({path:path.join(out,'native-mobile.png'),fullPage:true});
  await page.setViewport({width:1440,height:1080,deviceScaleFactor:1});
  await (await page.$('#native-import-file')).uploadFile(bpmnFixture);
  await page.waitForFunction(()=>!document.querySelector('#save').disabled);
  await page.click('#save');await page.waitForSelector('#modal[open]');
  await page.type('#modal-content input[name="message"]','显式 BPMNDI 原文版本');
  await page.click('#modal-content button[type="submit"]');
  await page.waitForFunction(previous=>document.querySelector('#version-label').title!==previous,{},saved.head_version);
  await page.waitForFunction(()=>!document.querySelector('#modal').open&&!document.querySelector('#native-preview').disabled);
  const bpmnVersion=await detail();
  require(bpmnVersion.native.language==='bpmn'&&bpmnVersion.native.xml===bpmn.toString('utf8'),'BPMN import changed source or language');
  require(!await page.$eval('#native-auto-layout',node=>node.checked),'BPMN auto-layout enabled implicitly');
  await page.focus('#native-preview');await page.keyboard.press('Enter');
  let bpmnJob;
  await until(async()=>{const current=await detail();bpmnJob=current.jobs.find(row=>row.kind==='native'&&row.version===bpmnVersion.head_version);
    return bpmnJob&&['succeeded','blocked','failed'].includes(bpmnJob.status);},45000);
  require(bpmnJob.status==='succeeded'&&!bpmnJob.native_preview.derived_layout&&!bpmnJob.full_language_acceptance,
    'Explicit DI BPMN preview failed: '+JSON.stringify(bpmnJob));
  await page.waitForFunction(()=>{const img=document.querySelector('.native-preview-image');return img?.complete&&img.naturalWidth>0;});
  report.checks.push({id:'native-bpmn-import-and-explicit-di-preview',passed:true,job:bpmnJob.id,version:bpmnJob.version,
    source_sha256:bpmnJob.native_source_sha256,derived_layout:false});
  await page.screenshot({path:path.join(out,'native-bpmn-desktop.png'),fullPage:true});
  await page.setViewport({width:390,height:844,deviceScaleFactor:1});
  const bpmnGeometry=await page.evaluate(()=>({viewport:innerWidth,width:document.documentElement.scrollWidth}));
  require(bpmnGeometry.width<=bpmnGeometry.viewport+1,'BPMN mobile page overflows');
  report.checks.push({id:'native-bpmn-mobile-layout',passed:true,...bpmnGeometry});
  await page.screenshot({path:path.join(out,'native-bpmn-mobile.png'),fullPage:true});
  await page.setViewport({width:1440,height:1080,deviceScaleFactor:1});
  await (await page.$('#native-import-file')).uploadFile(noDIFixture);
  await page.waitForFunction(()=>!document.querySelector('#save').disabled);
  await page.click('#save');await page.waitForSelector('#modal[open]');
  await page.type('#modal-content input[name="message"]','无坐标 BPMN 权威原文');
  await page.click('#modal-content button[type="submit"]');
  await page.waitForFunction(previous=>document.querySelector('#version-label').title!==previous,{},bpmnVersion.head_version);
  await page.waitForFunction(()=>!document.querySelector('#modal').open&&!document.querySelector('#native-preview').disabled);
  const noDIVersion=await detail();
  require(noDIVersion.native.xml===noDI&&!await page.$eval('#native-auto-layout',node=>node.checked),'No-DI import changed source or enabled layout');
  await page.focus('#native-preview');await page.keyboard.press('Enter');
  let noDIJob;
  await until(async()=>{const current=await detail();noDIJob=current.jobs.filter(row=>row.kind==='native'&&row.version===noDIVersion.head_version).at(-1);
    return noDIJob&&['succeeded','blocked','failed'].includes(noDIJob.status);},45000);
  require(noDIJob.status==='blocked'&&noDIJob.native_preview.category==='missing_material','No-DI preview generated implicit layout');
  report.checks.push({id:'native-bpmn-no-di-default-blocked',passed:true,job:noDIJob.id,version:noDIJob.version});
  await page.focus('#native-auto-layout');await page.keyboard.press('Space');
  await page.focus('#native-preview');await page.keyboard.press('Enter');
  let layoutJob;
  await until(async()=>{const current=await detail();layoutJob=current.jobs.filter(row=>row.kind==='native'&&row.version===noDIVersion.head_version).at(-1);
    return layoutJob&&layoutJob.id!==noDIJob.id&&['succeeded','blocked','failed'].includes(layoutJob.status);},45000);
  require(layoutJob.status==='succeeded'&&layoutJob.native_preview.derived_layout&&!layoutJob.full_language_acceptance,
    'Explicit BPMN auto-layout failed: '+JSON.stringify(layoutJob));
  require(layoutJob.outputs.some(row=>row.name==='native-preview.layout.bpmn'),'Derived BPMN layout was not exported separately');
  require((await detail()).native.xml===noDI,'Automatic layout rewrote authoritative source');
  await page.waitForFunction(()=>{const img=document.querySelector('.native-preview-image');return img?.complete&&img.naturalWidth>0;});
  report.checks.push({id:'native-bpmn-explicit-derived-layout-preserves-source',passed:true,job:layoutJob.id,version:layoutJob.version,
    source_sha256:layoutJob.native_source_sha256,derived_layout:true});
  await page.screenshot({path:path.join(out,'native-bpmn-autolayout-desktop.png'),fullPage:true});
  require(report.errors.length===0 && report.blocked_requests.length===0,'UI errors or external requests occurred');
  report.passed=true;
} catch(error) {
  report.errors.push(String(error));process.exitCode=1;
  if(page)try{await page.screenshot({path:path.join(out,'failure.png'),fullPage:true});
    report.failure_state=await page.evaluate(()=>({modal:document.querySelector('#modal').open,toasts:document.querySelector('#toasts').textContent,
      preview_disabled:document.querySelector('#native-preview')?.disabled,auto_layout:document.querySelector('#native-auto-layout')?.checked,
      preview:document.querySelector('#native-preview-result')?.textContent}));}catch{}
}
finally {
  if(browser)try{await browser.close();}catch(error){report.errors.push(String(error));}
  if(server && server.exitCode===null){server.kill('SIGTERM');await Promise.race([once(server,'exit'),new Promise(resolve=>setTimeout(resolve,5000))]);
    if(server.exitCode===null && server.signalCode===null){server.kill('SIGKILL');await once(server,'exit');}}
  report.cleanup={browser_alive:browserProcess?.pid?exists(browserProcess.pid):false,server_alive:server?.pid?exists(server.pid):false};
  if(profile)await fs.rm(profile,{recursive:true,force:true});
  report.cleanup.profile_removed=profile ? await fs.access(profile).then(()=>false,()=>true) : true;
  report.passed=report.passed && report.errors.length===0 && !report.cleanup.browser_alive && !report.cleanup.server_alive && report.cleanup.profile_removed;
  if(!report.passed)process.exitCode=1;
  await fs.writeFile(path.join(out,'server.log'),serverLog);
  for(const name of ['native-input.uml','native-input.bpmn','native-input-nodi.bpmn','server.log','native-desktop.png','native-mobile.png','native-bpmn-desktop.png','native-bpmn-mobile.png','native-bpmn-autolayout-desktop.png'])
    try{(report.output_sha256??={})[name]=sha(await fs.readFile(path.join(out,name)));}catch{}
  report.source_changed_during_run=[];
  for(const [filename,expected] of Object.entries(report.source_sha256))
    if(sha(await fs.readFile(path.join(repo,filename)))!==expected)report.source_changed_during_run.push(filename);
  if(report.source_changed_during_run.length){report.passed=false;process.exitCode=1;}
  await fs.writeFile(path.join(out,'report.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report));
}
