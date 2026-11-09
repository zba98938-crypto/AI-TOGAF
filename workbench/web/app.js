const $ = selector => document.querySelector(selector);
const $$ = selector => [...document.querySelectorAll(selector)];
const esc = value => String(value ?? '').replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;');
const clone = value => structuredClone(value);
const short = value => String(value || '').slice(0, 9);
const date = value => value ? new Date(value).toLocaleString('zh-CN', {hour12: false}) : '—';
const pretty = value => JSON.stringify(value, null, 2);
const STATES = {draft:'草稿',in_review:'评审中',accepted:'本地评审接受',changes_requested:'请求修改',submit:'提交评审',comment:'评审意见',request_changes:'请求修改',accept:'本地接受',queued:'排队中',running:'生成中',succeeded:'已生成',failed:'失败',blocked:'预览待补充'};
const S = {projects:[],project:null,model:null,layout:{},base:null,view:null,selected:null,dirty:false,
  tab:'canvas',query:'',type:'',undo:[],redo:[],jobs:[],catalog:[],busy:false,modelGroup:'entities',
  native:null,nativeDiagnostics:null,nativeAutoLayout:false,
  transform:{x:60,y:80,k:1},positions:new Map(),pendingFit:false,jobTimers:new Map()};

async function api(path, {method='GET',body}={}) {
  const response = await fetch('/api' + path, {method,headers:body === undefined ? {} : {'Content-Type':'application/json'},body:body === undefined ? undefined : JSON.stringify(body)});
  let data;
  try { data = await response.json(); } catch { throw new Error('服务返回了非 JSON 响应，请检查本地后端。'); }
  if (!response.ok) { const error = new Error(data.message || data.error || '请求失败'); Object.assign(error, {issues:data.issues,status:response.status}); throw error; }
  return data;
}
function toast(message, error=false) {
  const item=document.createElement('div');item.className='toast'+(error?' error':'');item.textContent=message;
  $('#toasts').append(item);setTimeout(()=>item.remove(),6500);
}
function report(error) { toast(error.message || String(error),true); if(error.issues){if(S.native&&error.issues.some(i=>i.category)){const data={valid:false,conformance_complete:false,validation_errors:[],missing_material:[],capability_uncovered:[]};for(const row of error.issues)(data[row.category] || data.validation_errors).push(row);S.nativeDiagnostics=data;setTab('native');}else showIssues(error.issues);} }
function guarded(fn) {return (...args)=>Promise.resolve().then(()=>fn(...args)).catch(report);}
function act(selector,fn) {$(selector).addEventListener('click',guarded(fn));}
function view() {return S.model?.views.find(row=>row.id===S.view);}
function reviewState(version=S.base) {return S.project?.review_states?.[version] || S.project?.versions?.find(v=>v.id===version)?.review_state || 'draft';}
function versions() {return [...(S.project?.versions || [])].sort((a,b)=>String(b.created_at).localeCompare(String(a.created_at)));}
function selection() {return S.selected ? S.model?.[S.selected.group]?.find(e=>e.id===S.selected.id) : null;}
function snapshot() {return {model:clone(S.model),layout:clone(S.layout),native:clone(S.native)};}
function remember() {S.undo.push(snapshot());if(S.undo.length>40)S.undo.shift();S.redo=[];}
function modified() {S.dirty=true;$('#validation-status').textContent='更改后待校验';updateHeader();}
function updateHeader() {
  const loaded=!!S.model;
  $('#project-name').textContent=S.project?.name || '架构项目';
  $('#view-title').textContent=view()?.title || S.project?.name || '让架构从静态走向协作';
  $('#example-label').hidden=!loaded;$('#example-label').textContent=S.model?.project.is_example?'虚构示例':'项目模型';
  $('#version-label').textContent=loaded?'版本 '+short(S.base):'尚未载入';
  $('#version-label').title=S.base || '';
  $('#dirty-label').textContent=S.dirty?'有未保存的更改':'所有更改已保存';$('#dirty-label').classList.toggle('unsaved',S.dirty);
  $('#review-label').textContent=STATES[reviewState()] || '草稿';
  for(const id of ['validate','save','generate','export','add-entity','add-relation'])$('#'+id).disabled=!loaded || S.busy;
  $('#save').disabled=!loaded || !S.dirty || S.busy;
  $('#job-count').textContent=S.jobs.length;
}
function setTab(tab) {
  S.tab=tab;$$('.tab').forEach(item=>{item.classList.toggle('active',item.dataset.tab===tab);item.setAttribute('aria-selected',item.dataset.tab===tab);});
  $$('.workspace-panel').forEach(panel=>{panel.hidden=panel.id!=='panel-'+tab;panel.classList.toggle('active',!panel.hidden);});
  if(tab==='model')renderModel();if(tab==='native')renderNative();if(tab==='versions')renderVersions();if(tab==='reviews')renderReviews();if(tab==='jobs')renderJobs();
  if(tab==='canvas')requestAnimationFrame(()=>{drawGraph();if(S.pendingFit){fit();S.pendingFit=false;}});
}
function modal(title,html,onSubmit) {
  $('#modal-title').textContent=title;$('#modal-content').innerHTML=html;$('#modal').showModal();
  const form=$('#modal-content form');
  if(form)form.addEventListener('submit',async event=>{
    event.preventDefault();const button=form.querySelector('[type=submit]');button.disabled=true;
    try {await onSubmit(new FormData(form),form);$('#modal').close();}
    catch(error){const target=form.querySelector('.form-error');if(target)target.textContent=error.message;report(error);}
    finally {button.disabled=false;}
  });
  requestAnimationFrame(()=>$('#modal-content input, #modal-content textarea, #modal-content select')?.focus());
}
function actions(label='确认') {return `<p class="form-error" role="alert"></p><div class="dialog-actions"><button type="button" class="button" data-dismiss>取消</button><button type="submit" class="button primary">${label}</button></div>`;}
$('#modal').addEventListener('click',e=>{if(e.target.closest('[data-dismiss]'))$('#modal').close();});
act('#modal-close',()=>$('#modal').close());
function canLeave() {return !S.dirty || confirm('存在未保存的更改。离开后这些更改将丢失，是否继续？');}

async function refreshProjects() {const data=await api('/projects');S.projects=data.projects;renderProjects();}
function renderProjects() {
  $('#projects').innerHTML=S.projects.length?S.projects.map(p=>`<button class="project-item ${p.id===S.project?.id?'active':''}" data-project="${esc(p.id)}"><span class="project-symbol">▱</span><span class="item-text">${esc(p.name)}</span></button>`).join(''):'<p class="hint" style="padding:0 12px;color:#90aaab">尚无项目，点击 ＋ 创建</p>';
}
async function openProject(id) {
  if(!canLeave())return;
  const data=await api('/projects/'+encodeURIComponent(id));
  S.project=data;S.model=clone(data.model);S.layout=clone(data.layout || {});S.base=data.head_version;
  S.native=clone(data.native || null);S.nativeDiagnostics=data.validation?.native || null;S.nativeAutoLayout=false;
  S.view=S.model.views[0]?.id;S.selected=null;S.dirty=false;S.undo=[];S.redo=[];S.query='';S.type='';S.pendingFit=true;
  S.jobs=data.jobs || [];$('#search').value='';$('#issues-panel').hidden=true;
  $('#validation-status').textContent=data.validation?.valid?'已保存版本规则校验通过':data.validation?.native&&!data.validation.native.valid?'已保存原生草稿有错误':'等待校验';
  localStorage.setItem('atlas-project',id);
  renderAll();for(const job of S.jobs)if(['queued','running'].includes(job.status))trackJob(job.id);
}
function renderViews() {
  const views=S.model?.views || [];$('#view-count').textContent=views.length;
  $('#views').innerHTML=views.map(v=>`<button class="view-item ${S.view===v.id?'active':''}" data-view="${esc(v.id)}"><span>◈</span><span>${esc(v.title)}</span></button>`).join('');
  const types=[...new Set((S.model?.entities || []).map(e=>e.type))].sort();
  $('#type-filter').innerHTML='<option value="">全部类型</option>'+types.map(t=>`<option ${t===S.type?'selected':''} value="${esc(t)}">${esc(t)}</option>`).join('');
}
function renderAll() {renderProjects();renderViews();updateHeader();renderInspector();setTab(S.tab);}

async function createProject(imported) {
  await ready;
  if(!imported&&!S.catalog.length){const data=await api('/catalog');S.catalog=data.templates || [];}
  if(!canLeave())return;
  const options=S.catalog.map(t=>`<option value="${esc(t.id)}" ${t.id==='trust-framework-default'?'selected':''}>${esc(t.name || t.id)}</option>`).join('');
  modal(imported?'导入模型为新项目':'创建架构项目',`<form><p class="hint">${imported?'保留原始模型字段、来源和确定性；由后端校验后建立首个版本。':'从现有视点示例开始。示例明确标记为虚构，不会被转换成真实企业事实。'}</p><label class="field"><span>项目名称</span><input name="name" required maxlength="120" placeholder="例如：订单履约架构" value="${esc(imported?.project?.name || '')}"></label>${imported?'':`<label class="field"><span>初始视点模板</span><select name="template">${options}</select></label>`}${actions(imported?'校验并导入':'创建项目')}</form>`,async data=>{
    const result=await api('/projects',{method:'POST',body:{name:data.get('name'),...(imported?{model:imported}:{template:data.get('template')})}});
    S.dirty=false;await refreshProjects();await openProject(result.id);toast('项目已创建，原始模型已建立版本');
  });
}
$('#projects').addEventListener('click',guarded(e=>{const button=e.target.closest('[data-project]');if(button)return openProject(button.dataset.project);}));
$('#views').addEventListener('click',e=>{const button=e.target.closest('[data-view]');if(!button)return;chooseView(button.dataset.view);});
function chooseView(id) {S.view=id;S.selected=null;S.type='';S.query='';$('#search').value='';S.pendingFit=true;renderAll();}
act('#new-project',()=>createProject());act('#new-project-top',()=>createProject());act('#empty-create',()=>createProject());
act('#import',()=>$('#import-file').click());
$('#import-file').addEventListener('change',guarded(async e=>{
  const file=e.target.files[0];if(!file)return;
  try {if(file.size>8*1024*1024)throw new Error('导入文件超过 8 MB 限制');await createProject(JSON.parse(await file.text()));}
  finally {e.target.value='';}
}));
act('#export',()=>{
  const blob=new Blob([pretty(S.model)+'\n'],{type:'application/json'});const url=URL.createObjectURL(blob);
  const a=document.createElement('a');a.href=url;a.download=(S.model.project.id || 'architecture')+'.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  toast('已导出当前模型；画布布局随平台版本保存，不写入业务模型');
});

act('#native-import',()=>$('#native-import-file').click());
$('#native-import-file').addEventListener('change',guarded(async event=>{
  const file=event.target.files[0];if(!file)return;
  try {
    const isPackage=/\.json$/i.test(file.name);
    if(file.size>(isPackage?8:7)*1024*1024)throw new Error(isPackage?'原生资源包超过 8 MiB 编辑请求容量；请使用本地命令行，文件不会截断':'原生源码超过 7 MiB 编辑限制');
    const text=new TextDecoder('utf-8',{fatal:true,ignoreBOM:true}).decode(await file.arrayBuffer());
    let native;
    if(isPackage){
      const value=JSON.parse(text);
      if(value.format==='ai-togaf-native-language-package'){
        native=(await api('/native/unpack',{method:'POST',body:{package:value}})).native;
      }else native=value;
      await api('/native/validate',{method:'POST',body:{native}});
    }else{
      const language=/\.bpmn$/i.test(file.name)||text.includes('http://www.omg.org/spec/BPMN/20100524/MODEL')?'bpmn':'uml';
      native={language,version:language==='bpmn'?'2.0.2':'2.5.1',xml:text};
    }
    if(S.model){remember();S.native=native;S.nativeDiagnostics=null;modified();setTab('native');toast('原生源码已载入草稿；保存将建立新版本');}
    else modal('建立原生模型项目',`<form><p class="hint">原生 XML 原文作为权威数据保存。无效源码可以保存为带诊断的草稿，生成必须先通过已实现规则。</p><label class="field"><span>项目名称</span><input name="name" required maxlength="120" value="${esc(file.name.replace(/\.[^.]+$/,''))}"></label>${actions('保存首个原生版本')}</form>`,async data=>{
      const project=await api('/projects',{method:'POST',body:{name:data.get('name'),native}});
      await refreshProjects();await openProject(project.id);setTab('native');toast('原生模型与诊断已建立首个版本');
    });
  } finally {event.target.value='';}
}));

function nativeDiagnosticMarkup(data) {
  if(!data)return '<p class="hint">源码更改后请重新诊断。完整标准能力的状态与输入错误分开记录。</p>';
  const groups={validation_errors:'校验错误',missing_material:'材料缺失',capability_uncovered:'能力未覆盖'};
  return `<p class="hint">已实现规则：${data.valid?'未发现输入错误':'存在输入错误'} · 完整标准能力：${data.conformance_complete?'已验证':'未完成'}</p>`+Object.entries(groups).map(([key,label])=>`<section class="native-diagnostic-group"><h3>${label} · ${(data[key] || []).length}</h3>${(data[key] || []).length?(data[key] || []).map(row=>`<div class="issue ${esc(row.level)}"><span class="issue-code">${esc(row.code)}</span><div>${esc(row.message)}</div></div>`).join(''):'<p class="hint">本次未记录此类问题。</p>'}</section>`).join('');
}
function renderNative() {
  const panel=$('#panel-native');
  if(!S.model){panel.innerHTML='<div class="empty-state"><h3>导入原生 UML 或 BPMN</h3><p>选择 UTF-8 的 .uml、.xmi、.bpmn 或 .xml 文件，保存原文、诊断和不可变版本。</p><button id="native-empty-import" class="button primary">选择原生文件</button></div>';$('#native-empty-import').addEventListener('click',()=>$('#native-import-file').click());return;}
  if(!S.native){panel.innerHTML='<div class="panel-heading"><div><h2>原生模型源码</h2><p>本项目尚无原生 XML。可将 UML 或 BPMN 原文加入当前草稿。</p></div><button id="native-add-source" class="button primary">导入原生源码</button></div>';$('#native-add-source').addEventListener('click',()=>$('#native-import-file').click());return;}
  panel.innerHTML=`<div class="panel-heading"><div><h2>原文驱动模型与预览</h2><p>UTF-8 XML 原文是权威数据；诊断、交换包和布局预览由已保存版本派生。</p></div><div class="row-actions"><button id="native-remove" class="button">移除草稿中的原生模型</button><button id="native-export" class="button">导出原文 ↗</button></div></div><div class="native-editor-grid"><div class="panel-card"><div class="native-editor-toolbar"><label class="field"><span>标准与版本</span><select id="native-language"><option value="bpmn" ${S.native.language==='bpmn'?'selected':''}>BPMN 2.0.2</option><option value="uml" ${S.native.language==='uml'?'selected':''}>UML 2.5.1</option></select></label><button id="native-diagnose" class="button">诊断源码</button></div><label class="field"><span>原生 XML 源码</span><textarea id="native-source" class="editor-large native-source" spellcheck="false" aria-label="原生XML源码">${esc(S.native.xml)}</textarea></label><p class="hint">保存包含无效源码的草稿会保留错误诊断；这些版本不能生成。原有 DI 坐标保持原文，自动布局必须显式选择。</p></div><div class="panel-card"><h3>诊断与能力状态</h3><div id="native-diagnostics">${nativeDiagnosticMarkup(S.nativeDiagnostics)}</div></div></div><div class="panel-card"><div class="native-preview-toolbar"><label><input id="native-auto-layout" type="checkbox" ${S.nativeAutoLayout?'checked':''}> 显式生成派生自动布局（已有 DI 保持）</label><button id="native-preview" class="button primary" ${S.dirty?'disabled':''}>预览已保存版本</button></div><p class="hint">预览复用生成任务及版本评审。材料缺失或图形能力未覆盖会保留明确状态；原文导出不受派生布局影响。</p><div id="native-preview-result"></div></div>`;
  let remembered=false;
  if(S.native.resources || S.native.document_path){
    $('#native-language').disabled=true;
    const summary=document.createElement('p');summary.className='hint';summary.id='native-resource-summary';
    summary.textContent=`主文档：${S.native.document_path || 'main.bpmn'} · 导入资源：${(S.native.resources || []).length} 个。主文档编辑会保留资源原字节；跨文件语义与图形能力未覆盖。`;
    $('#native-source').parentElement.after(summary);
    $('#native-export').textContent='导出原生源码包 ↗';
  }
  $('#native-source').addEventListener('input',event=>{if(!remembered){remember();remembered=true;}S.native.xml=event.target.value;delete S.native.source_sha256;S.nativeDiagnostics=null;modified();$('#native-preview').disabled=true;$('#native-diagnostics').innerHTML=nativeDiagnosticMarkup(null);});
  $('#native-language').addEventListener('change',event=>{remember();S.native.language=event.target.value;S.native.version=event.target.value==='bpmn'?'2.0.2':'2.5.1';S.nativeDiagnostics=null;modified();$('#native-preview').disabled=true;$('#native-diagnostics').innerHTML=nativeDiagnosticMarkup(null);});
  $('#native-auto-layout').addEventListener('change',event=>{S.nativeAutoLayout=event.target.checked;});
  $('#native-diagnose').addEventListener('click',guarded(async()=>{const result=await api('/native/validate',{method:'POST',body:{native:S.native}});S.nativeDiagnostics=result;$('#native-diagnostics').innerHTML=nativeDiagnosticMarkup(result);$('#validation-status').textContent=result.valid?'原生规则诊断完成':'原生源码有错误';}));
  $('#native-export').addEventListener('click',()=>{const bundled=Boolean(S.native.resources || S.native.document_path);const url=URL.createObjectURL(new Blob([bundled?pretty(S.native)+'\n':S.native.xml],{type:bundled?'application/json':'application/xml;charset=utf-8'}));const link=document.createElement('a');link.href=url;link.download=(S.model.project.id || 'native')+(bundled?'.native.json':S.native.language==='bpmn'?'.bpmn':'.uml');link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
  $('#native-remove').addEventListener('click',()=>{remember();S.native=null;S.nativeDiagnostics=null;modified();renderNative();toast('原生模型已从草稿移除；历史版本保持，可撤销');});
  $('#native-preview').addEventListener('click',guarded(async()=>{if(S.dirty)throw new Error('先保存原生草稿，再生成版本预览');const job=await api(`/projects/${S.project.id}/generate`,{method:'POST',body:{version:S.base,kind:'native',render:true,auto_layout:S.nativeAutoLayout}});S.jobs.unshift(job);updateHeader();trackJob(job.id);renderNativePreview();toast('原生预览任务已排队');}));
  renderNativePreview();
}
function renderNativePreview() {
  const target=$('#native-preview-result');if(!target)return;
  const job=S.jobs.find(row=>row.kind==='native'&&row.version===S.base);
  if(!job){target.innerHTML='<p class="hint">尚无此版本的原生预览任务。</p>';return;}
  const picture=(job.outputs || []).find(row=>row.name==='native-preview.png');
  target.innerHTML=`<p class="hint">任务 ${esc(short(job.id))} · ${esc(STATES[job.status] || job.status)} · 版本 ${esc(short(job.version))}</p>${job.native_preview?.issues?nativeDiagnosticMarkup({valid:true,conformance_complete:false,[job.native_preview.category]:job.native_preview.issues}):''}${job.error?`<pre>${esc(job.error)}</pre>`:''}${picture?`<img class="native-preview-image" src="${esc(picture.url)}" alt="已保存原生模型版本的图形预览">`:''}<div class="output-links">${(job.outputs || []).map(row=>`<a class="button small" href="${esc(row.url)}" target="_blank" rel="noopener">${esc(row.name)} ↗</a>`).join('')}</div>`;
}

// Canvas state is separate from semantic model data. The graph is explicitly a
// relationship projection, not a replacement for each profile's notation.
const NODE_W=238,NODE_H=110;
function members() {
  const v=view();const byid=new Map((S.model?.entities || []).map(e=>[e.id,e]));
  const ids=new Set(v?.entity_ids || []);const entities=[...ids].map(id=>byid.get(id)).filter(Boolean);
  const relationships=(S.model?.relationships || []).filter(r=>(v?.relationship_ids || []).includes(r.id));
  const external=new Set();for(const r of relationships)for(const id of [r.source,r.target])if(!ids.has(id)&&byid.has(id)){entities.push(byid.get(id));ids.add(id);external.add(id);}
  return {entities,relationships,external};
}
function currentPositions() {return S.layout.views?.[S.view]?.positions || {};}
function savePosition(id,x,y) {
  S.layout.views ||= {};S.layout.views[S.view] ||= {};S.layout.views[S.view].positions ||= {};
  S.layout.views[S.view].positions[id]={x:Math.round(x),y:Math.round(y)};
}
function drawGraph() {
  $('#empty-canvas').hidden=!!S.model;
  if(!S.model){$('#nodes').replaceChildren();$('#edges').replaceChildren();return;}
  const {entities,relationships,external}=members();const q=S.query.trim().toLowerCase();
  const related=new Set(relationships.filter(r=>q&&[r.id,r.label,r.type].some(v=>String(v).toLowerCase().includes(q))).flatMap(r=>[r.source,r.target]));
  const matched=entities.filter(e=>(!S.type||e.type===S.type)&&(!q||JSON.stringify(e).toLowerCase().includes(q)||related.has(e.id)));
  const visible=matched.slice(0,600);const visibleIds=new Set(visible.map(e=>e.id));
  const rels=relationships.filter(r=>visibleIds.has(r.source)&&visibleIds.has(r.target));
  const pos=currentPositions();const columns=Math.max(2,Math.min(6,Math.ceil(Math.sqrt(entities.length))));
  S.positions.clear();entities.forEach((e,i)=>{const p=pos[e.id];S.positions.set(e.id,p&&Number.isFinite(p.x)&&Number.isFinite(p.y)?{x:p.x,y:p.y}:{x:(i%columns)*(NODE_W+110),y:Math.floor(i/columns)*(NODE_H+115)});});
  const selected=selection();const neighbors=new Set();
  if(S.selected?.group==='entities'){neighbors.add(selected?.id);for(const r of relationships)if(r.source===selected?.id||r.target===selected?.id){neighbors.add(r.source);neighbors.add(r.target);}}
  const nodes=visible.map(e=>{
    const p=S.positions.get(e.id),isSelected=S.selected?.group==='entities'&&S.selected.id===e.id;
    const dimmed=neighbors.size&&!neighbors.has(e.id);
    const excerpt=(text,n)=>String(text).length>n?String(text).slice(0,n-1)+'…':String(text);
    return `<g class="node ${isSelected?'selected':''} ${dimmed?'dimmed':''}" data-node="${esc(e.id)}" transform="translate(${p.x},${p.y})" role="button" tabindex="0" aria-label="实体 ${esc(e.name)}"><title>${esc(e.name)}\n${esc(e.id)}\n${esc(e.type)}</title><rect class="node-card" width="${NODE_W}" height="${NODE_H}" rx="8"/><path class="node-header" d="M8 0H230Q238 0 238 8V31H0V8Q0 0 8 0"/><text x="14" y="20" class="node-kind">${esc(excerpt(e.type.toUpperCase(),28))}</text><text x="14" y="57" class="node-name">${esc(excerpt(e.name,16))}</text><text x="14" y="75" class="node-id">${esc(excerpt(e.id,34))}</text><circle cx="17" cy="94" r="3" fill="${e.certainty==='confirmed'?'#529b83':'#c3a46d'}"/><text x="26" y="98" class="node-meta">${external.has(e.id)?'视图外端点 · ':''}${esc(e.certainty || 'unknown')} · ${(e.evidence || []).length} 个来源</text></g>`;
  }).join('');
  $('#nodes').innerHTML=nodes;
  $('#edges').innerHTML=rels.map((r,i)=>{
    const a=S.positions.get(r.source),b=S.positions.get(r.target);const ax=a.x+NODE_W/2,ay=a.y+NODE_H/2,bx=b.x+NODE_W/2,by=b.y+NODE_H/2;
    let d,mx,my;
    if(r.source===r.target){d=`M${a.x+NODE_W-10} ${ay} C${a.x+NODE_W+100} ${ay-110},${a.x+NODE_W+100} ${ay+110},${a.x+NODE_W-10} ${ay+12}`;mx=a.x+NODE_W+50;my=ay;}
    else {const dx=bx-ax,dy=by-ay;const offset=((i%3)-1)*20;
      const distance=Math.hypot(dx,dy)||1,ux=dx/distance,uy=dy/distance;
      const border=Math.min(Math.abs(dx)>0?NODE_W/2/Math.abs(ux):Infinity,Math.abs(dy)>0?NODE_H/2/Math.abs(uy):Infinity);
      const sx=ax+ux*(border+4),sy=ay+uy*(border+4),tx=bx-ux*(border+8),ty=by-uy*(border+8);
      d=`M${sx} ${sy} C${sx+(tx-sx)*.45} ${sy+(ty-sy)*.1+offset},${tx-(tx-sx)*.45} ${ty-(ty-sy)*.1+offset},${tx} ${ty}`;mx=(ax+bx)/2;my=(ay+by)/2+offset*.75;}
    const highlighted=S.selected?.group==='relationships'&&S.selected.id===r.id;const dimmed=neighbors.size&&r.source!==selected?.id&&r.target!==selected?.id;
    const available=Math.max(60,Math.min(210,Math.hypot(bx-ax,by-ay)-NODE_W-24));
    const length=Math.max(5,Math.floor(available/10));
    const label=r.label.length>length?r.label.slice(0,length-1)+'…':r.label;const w=Math.min(220,Math.max(60,label.length*10));
    return `<g class="edge ${highlighted?'selected':''} ${dimmed?'dimmed':''}" data-edge="${esc(r.id)}" role="button" tabindex="0" aria-label="关系 ${esc(r.label)}"><title>${esc(r.label)} · ${esc(r.type)}\n${esc(r.source)} → ${esc(r.target)}</title><path d="${d}" marker-end="url(#edge-arrow)"/><path class="edge-hit" d="${d}"/><rect class="edge-label-bg" x="${mx-w/2}" y="${my-11}" width="${w}" height="20" rx="4"/><text x="${mx}" y="${my+3}" text-anchor="middle">${esc(label)}</text></g>`;
  }).join('');
  $('#graph-counts').textContent=`${visible.length}/${entities.length} 个实体 · ${rels.length}/${relationships.length} 条关系`;
  $('.graph-limit')?.remove();
  if(matched.length>600){const tip=document.createElement('div');tip.className='graph-limit';tip.textContent=`匹配 ${matched.length} 个实体，当前绘制前 600 个。请按类型或搜索收窄范围；完整模型未删减。`;$('#canvas').append(tip);}
  if(!entities.length){$('#empty-canvas').hidden=false;$('#empty-canvas').innerHTML='<div class="empty-symbol">◈</div><h2>当前视图没有实体</h2><p>通过“＋ 实体”添加对象，或在模型 JSON 中配置视图成员。</p>';}
  applyTransform();
}
function applyTransform() {const {x,y,k}=S.transform;$('#viewport').setAttribute('transform',`translate(${x},${y}) scale(${k})`);$('#zoom-label').textContent=Math.round(k*100)+'%';}
function zoom(factor,cx,cy) {const rect=$('#canvas').getBoundingClientRect();cx??=rect.width/2;cy??=rect.height/2;const old=S.transform.k,k=Math.max(.08,Math.min(2.5,old*factor));S.transform={x:cx-(cx-S.transform.x)*k/old,y:cy-(cy-S.transform.y)*k/old,k};applyTransform();}
function fit() {
  const nodes=$$('[data-node]');if(!nodes.length)return;
  const ps=nodes.map(n=>S.positions.get(n.dataset.node));const minx=Math.min(...ps.map(p=>p.x)),miny=Math.min(...ps.map(p=>p.y)),maxx=Math.max(...ps.map(p=>p.x))+NODE_W,maxy=Math.max(...ps.map(p=>p.y))+NODE_H;
  const r=$('#canvas').getBoundingClientRect();const k=Math.min(1.15,(r.width-100)/(maxx-minx),(r.height-120)/(maxy-miny));
  if(k>0)S.transform={x:(r.width-(maxx-minx)*k)/2-minx*k,y:(r.height-(maxy-miny)*k)/2-miny*k,k};applyTransform();
}
let drag=null;
$('#graph').addEventListener('pointerdown',e=>{
  if(e.button!==0||!S.model)return;
  const node=e.target.closest('[data-node]');const edge=e.target.closest('[data-edge]');if(edge)return;
  const p=node?S.positions.get(node.dataset.node):null;
  drag={id:node?.dataset.node,x:e.clientX,y:e.clientY,origin:p?{...p}:{...S.transform},moved:false};
  $('#graph').setPointerCapture(e.pointerId);e.preventDefault();
});
$('#graph').addEventListener('pointermove',e=>{
  if(!drag)return;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;
  if(!drag.moved&&Math.abs(dx)+Math.abs(dy)<4)return;
  if(!drag.moved&&drag.id)remember();drag.moved=true;
  if(drag.id){savePosition(drag.id,drag.origin.x+dx/S.transform.k,drag.origin.y+dy/S.transform.k);modified();drawGraph();}
  else {S.transform.x=drag.origin.x+dx;S.transform.y=drag.origin.y+dy;applyTransform();}
});
$('#graph').addEventListener('pointerup',e=>{if(!drag)return;const d=drag;drag=null;if(!d.moved&&d.id)select('entities',d.id);else if(!d.moved&&!e.target.closest('[data-edge]')){S.selected=null;drawGraph();renderInspector();}});
$('#graph').addEventListener('pointercancel',()=>{drag=null;});
$('#graph').addEventListener('click',e=>{const edge=e.target.closest('[data-edge]');if(edge)select('relationships',edge.dataset.edge);});
$('#graph').addEventListener('keydown',e=>{if(e.key!=='Enter'&&e.key!==' ')return;const node=e.target.closest('[data-node]'),edge=e.target.closest('[data-edge]');if(node||edge){e.preventDefault();select(node?'entities':'relationships',node?.dataset.node||edge.dataset.edge);}});
$('#canvas').addEventListener('wheel',e=>{if(!S.model)return;e.preventDefault();const r=$('#canvas').getBoundingClientRect();zoom(Math.exp(-e.deltaY*.0015),e.clientX-r.left,e.clientY-r.top);},{passive:false});
act('#zoom-in',()=>zoom(1.2));act('#zoom-out',()=>zoom(1/1.2));act('#fit',fit);
act('#reset-layout',()=>{if(!S.model)return;remember();if(S.layout.views)delete S.layout.views[S.view];modified();drawGraph();fit();});
$('#search').addEventListener('input',e=>{S.query=e.target.value;drawGraph();});
$('#type-filter').addEventListener('change',e=>{S.type=e.target.value;drawGraph();fit();});

function select(group,id) {S.selected={group,id};if(S.tab!=='canvas')setTab('canvas');drawGraph();renderInspector();}
function renderInspector() {
  const box=$('#inspector'),item=selection();
  if(!S.model){box.innerHTML='<div class="eyebrow">INSPECTOR</div><h2>模型的每一处，皆可追溯</h2><p class="hint">选中实体或连线，查看并编辑属性、证据和确定性。更改将保存为新版本。</p><div class="warning-note">先创建项目或导入现有模型。平台不会自动构造企业事实。</div>';return;}
  if(!item){
    const m=members();box.innerHTML=`<div class="eyebrow">VIEW OVERVIEW</div><h2>${esc(view()?.title || '项目总览')}</h2><p class="identity">${esc(S.view || '未选择视图')}</p><label class="field"><span>切换视图</span><select id="inspector-view">${S.model.views.map(v=>`<option value="${esc(v.id)}" ${v.id===S.view?'selected':''}>${esc(v.title)}</option>`).join('')}</select></label><div class="stat-grid"><div><strong>${m.entities.length}</strong><span>模型实体</span></div><div><strong>${m.relationships.length}</strong><span>显式关系</span></div></div><h3>视图分析</h3><p class="hint">${esc(view()?.analysis || '没有分析记录')}</p><h3>图例与边界</h3><p class="hint">${esc(view()?.legend || '未提供图例')}</p><div class="warning-note">画布是用于交互编辑的关系投影。画面上的位置不代表业务次序、信任边界或专业符号认证。</div><button id="edit-view" class="button small">编辑视图 JSON</button><hr><p class="hint">滚轮缩放 · 背景拖动平移<br>节点拖动调整布局 · 点击连线编辑<br>Ctrl / ⌘ + S 保存版本</p>`;
    $('#inspector-view').addEventListener('change',e=>chooseView(e.target.value));$('#edit-view').addEventListener('click',()=>editJSON('views',S.view));return;
  }
  const isEntity=S.selected.group==='entities';const evidence=(item.evidence || []).map(id=>{const s=S.model.sources.find(s=>s.id===id);return `<div class="hint"><strong>${esc(id)}</strong><br>${esc(s?.description || '引用不存在，需校验')}</div>`;}).join('');
  box.innerHTML=`<div class="eyebrow">${isEntity?'ENTITY DETAILS':'RELATIONSHIP DETAILS'}</div><h2>${esc(isEntity?item.name:item.label)}</h2><p class="identity">${esc(item.id)}</p><form id="inspector-form"><label class="field"><span>${isEntity?'实体名称':'关系说明'}</span><input name="name" required value="${esc(isEntity?item.name:item.label)}"></label><label class="field"><span>类型</span><input name="type" required value="${esc(item.type)}"></label>${isEntity?'':`<label class="field"><span>起点</span><select name="source">${S.model.entities.map(e=>`<option value="${esc(e.id)}" ${item.source===e.id?'selected':''}>${esc(e.name)}</option>`).join('')}</select></label><label class="field"><span>终点</span><select name="target">${S.model.entities.map(e=>`<option value="${esc(e.id)}" ${item.target===e.id?'selected':''}>${esc(e.name)}</option>`).join('')}</select></label>`}<label class="field"><span>确定性</span><select name="certainty">${['confirmed','assumed','unknown'].map(c=>`<option ${c===item.certainty?'selected':''}>${c}</option>`).join('')}</select></label><label class="field"><span>属性（JSON 对象）</span><textarea name="attributes" class="code" spellcheck="false">${esc(pretty(item.attributes || {}))}</textarea></label><label class="field"><span>证据 ID（每行一个）</span><textarea name="evidence" style="min-height:58px">${esc((item.evidence || []).join('\n'))}</textarea></label><button type="submit" class="button primary" style="width:100%">应用到当前草稿</button></form><div class="row-actions" style="margin-top:10px"><button id="full-json" class="button small">完整字段</button><button id="delete-item" class="button small danger">删除${isEntity?'实体':'关系'}</button></div><hr><h3>来源证据</h3>${evidence || '<p class="hint">尚未绑定来源</p>'}`;
  $('#inspector-form').addEventListener('submit',guarded(async e=>{
    e.preventDefault();const data=new FormData(e.target);const attributes=JSON.parse(data.get('attributes'));
    if(!attributes||typeof attributes!=='object'||Array.isArray(attributes))throw new Error('属性必须是 JSON 对象');
    remember();item[isEntity?'name':'label']=data.get('name');item.type=data.get('type');item.certainty=data.get('certainty');
    item.attributes=attributes;item.evidence=[...new Set(data.get('evidence').split('\n').map(v=>v.trim()).filter(Boolean))];
    if(!isEntity){item.source=data.get('source');item.target=data.get('target');}
    modified();renderViews();drawGraph();renderInspector();toast('已应用到草稿，请校验并保存新版本');
  }));
  $('#full-json').addEventListener('click',()=>editJSON(S.selected.group,item.id));
  $('#delete-item').addEventListener('click',()=>deleteItem(S.selected.group,item.id));
  if(isEntity){const rels=S.model.relationships.filter(r=>r.source===item.id||r.target===item.id);box.insertAdjacentHTML('beforeend',`<hr><h3>关联关系 · ${rels.length}</h3>`+rels.slice(0,40).map(r=>`<button class="relation-row" data-select-relation="${esc(r.id)}">${esc(r.label)}<span>${esc(r.type)} · ${esc(r.source===item.id?'向外 →':'← 向内')}</span></button>`).join(''));}
}
$('#inspector').addEventListener('click',e=>{const b=e.target.closest('[data-select-relation]');if(b)select('relationships',b.dataset.selectRelation);});
function editJSON(group,id) {
  const item=group==='model'?S.model:S.model[group].find(r=>r.id===id);
  modal(group==='model'?'编辑完整模型':'编辑完整字段',`<form><p class="hint">保留稳定 ID 和来源；不认识的字段或无效引用会在校验时明确报错。应用草稿不会自动保存。</p><textarea name="json" class="editor-large" spellcheck="false" aria-label="完整 JSON 编辑器">${esc(pretty(item))}</textarea>${actions('应用草稿')}</form>`,data=>{
    const value=JSON.parse(data.get('json'));if(!value||typeof value!=='object'||Array.isArray(value))throw new Error('必须提供 JSON 对象');
    if(group!=='model'&&value.id!==id)throw new Error('稳定 ID 不能在字段编辑中修改；请显式更新完整模型和引用');
    if(group==='model'&&(!value.project||!['entities','relationships','views','sources','gaps','deliverables'].every(key=>Array.isArray(value[key]))))throw new Error('缺少 project/entities/relationships/views/sources/gaps/deliverables 必要结构');
    remember();if(group==='model')S.model=value;else S.model[group][S.model[group].findIndex(r=>r.id===id)]=value;
    if(!S.model.views.some(v=>v.id===S.view))S.view=S.model.views[0]?.id;
    modified();renderAll();toast('草稿已更新，保存前将进行完整校验');
  });
}
function deleteItem(group,id) {
  modal('删除草稿记录',`<form><p>确认删除 <code>${esc(id)}</code>？</p><p class="warning-note">将移除相关视图成员和关联关系；其他业务引用不会被静默修复，须通过校验处理。当前操作可撤销，保存后建立新版本。</p>${actions('确认删除')}</form>`,()=>{
    remember();const removed=new Set([id]);
    if(group==='entities'){for(const r of S.model.relationships)if(r.source===id||r.target===id)removed.add(r.id);S.model.relationships=S.model.relationships.filter(r=>!removed.has(r.id));}
    S.model[group]=S.model[group].filter(r=>r.id!==id);
    for(const v of S.model.views){v.entity_ids=v.entity_ids.filter(id=>!removed.has(id));v.relationship_ids=v.relationship_ids.filter(id=>!removed.has(id));}
    S.selected=null;modified();renderAll();toast('已从草稿删除；保存将检查剩余引用');
  });
}
function addItem(group) {
  if(!S.model)return;const entity=group==='entities';const v=view();
  modal(entity?'添加模型实体':'建立显式关系',`<form><label class="field"><span>稳定 ID（字母、数字、连字符）</span><input name="id" required pattern="[a-zA-Z0-9][a-zA-Z0-9_.-]*" value="${entity?'entity':'relation'}-${Date.now().toString(36)}"></label><label class="field"><span>${entity?'实体名称':'关系说明'}</span><input name="name" required></label><label class="field"><span>类型（必须符合模型词汇）</span><input name="type" required value="${esc(entity?(S.model.entities[0]?.type || 'application'):'traces_to')}"></label>${entity?'':`<label class="field"><span>起点</span><select name="source" required>${S.model.entities.map(e=>`<option value="${esc(e.id)}">${esc(e.name)}</option>`).join('')}</select></label><label class="field"><span>终点</span><select name="target" required>${S.model.entities.map((e,i)=>`<option value="${esc(e.id)}" ${i===1?'selected':''}>${esc(e.name)}</option>`).join('')}</select></label>`}<label class="field"><span>属性 JSON（必要字段请按视点填写）</span><textarea name="attributes" class="code" spellcheck="false">{}</textarea></label><p class="hint">初始确定性为 assumed、证据为空。请补充真实来源，不会自动伪造证据。</p>${actions(entity?'添加实体':'建立关系')}</form>`,data=>{
    const id=data.get('id');if(Object.values(S.model).some(g=>Array.isArray(g)&&g.some(r=>r?.id===id)))throw new Error('ID 已存在');
    const attributes=JSON.parse(data.get('attributes'));if(!attributes||Array.isArray(attributes)||typeof attributes!=='object')throw new Error('属性必须是 JSON 对象');
    const item={id,type:data.get('type'),attributes,evidence:[],certainty:'assumed'};
    if(entity)item.name=data.get('name');else Object.assign(item,{label:data.get('name'),source:data.get('source'),target:data.get('target')});
    remember();S.model[group].push(item);if(v)v[entity?'entity_ids':'relationship_ids'].push(id);modified();renderViews();select(group,id);toast('已添加到草稿，请补充来源并校验');
  });
}
act('#add-entity',()=>addItem('entities'));act('#add-relation',()=>addItem('relationships'));

function showIssues(issues) {
  $('#issues-panel').hidden=false;const errors=issues.filter(i=>i.level==='error').length;
  $('#issues-title').textContent=`模型校验 · ${errors} 个错误 / ${issues.length-errors} 个提示`;
  $('#validation-status').textContent=errors?`${errors} 个校验错误`:'工程校验通过';
  $('#issues-list').innerHTML=issues.length?issues.map(i=>`<div class="issue ${esc(i.level)}"><span class="issue-code">${esc(i.code || i.level)}</span><div><strong>${esc(i.id)}</strong> ${esc(i.message)}</div></div>`).join(''):'<p class="hint">未发现已编码规则错误。结构校验通过不代表专业结论或业务批准。</p>';
  if(S.tab!=='canvas')setTab('canvas');
}
act('#close-issues',()=>{$('#issues-panel').hidden=true;});
act('#validate',async()=>{S.busy=true;updateHeader();try{const data=await api('/validate',{method:'POST',body:{model:S.model}});if(S.native){S.nativeDiagnostics=await api('/native/validate',{method:'POST',body:{native:S.native}});setTab('native');$('#validation-status').textContent=S.nativeDiagnostics.valid?'已实现原生规则诊断完成':'原生源码有校验错误';toast(S.nativeDiagnostics.valid?'原生规则诊断完成；完整能力状态见面板':'原生草稿有错误，可保存诊断版本',!S.nativeDiagnostics.valid);}else{showIssues(data.issues);toast(data.valid?'已编码规则校验通过':'发现模型问题，请在校验面板处理',!data.valid);}}finally{S.busy=false;updateHeader();}});
act('#save',()=>{
  modal('保存不可变模型版本',`<form><p class="hint">保存模型、原生 XML 原文和独立画布布局。当前基线：<code>${esc(short(S.base))}</code>。原生错误诊断随草稿保存，含错误版本不能生成；并发修改被拒绝，历史版本保持。</p><label class="field"><span>变更说明</span><input name="message" required maxlength="500" placeholder="例如：明确承运商数据范围与责任"></label>${actions('保存新版本')}</form>`,async data=>{
    const result=await api(`/projects/${S.project.id}/versions`,{method:'POST',body:{base_version:S.base,model:S.model,layout:S.layout,native:S.native,message:data.get('message')}});
    const id=S.project.id;S.dirty=false;await refreshProjects();await openProject(id);toast('新版本已保存：'+short(result.head_version || S.base));
  });
});

function panelEmpty(id,text) {$('#panel-'+id).innerHTML=`<div class="empty-state"><h3>尚未载入项目</h3><p>${text}</p></div>`;}
function renderModel() {
  if(!S.model)return panelEmpty('model','创建项目或导入模型后，在此管理完整记录。');
  const groups={entities:'实体',relationships:'关系',views:'视图',sources:'来源',gaps:'缺口',deliverables:'交付物'};
  const group=S.modelGroup;const rows=S.model[group] || [];
  $('#panel-model').innerHTML=`<div class="panel-heading"><div><h2>模型数据</h2><p>同一个模型驱动画布、校验和生成；不维护第二份业务数据。</p></div><button class="button" id="edit-model-json">编辑完整 JSON</button></div><div class="model-tabs">${Object.entries(groups).map(([g,label])=>`<button class="button small ${g===group?'active':''}" data-model-group="${g}">${label} ${(S.model[g] || []).length}</button>`).join('')}</div><label class="search-field" style="max-width:400px;margin-bottom:18px"><input id="model-search" type="search" aria-label="搜索模型记录" placeholder="按任意字段搜索完整记录…"></label><div class="panel-card table-wrap"><table><thead><tr><th>稳定 ID</th><th>名称 / 说明</th><th>类型 / 状态</th><th>操作</th></tr></thead><tbody id="model-rows"></tbody></table><p id="model-count" class="hint"></p></div>`;
  const draw=()=>{const q=$('#model-search').value.toLowerCase();const filtered=rows.filter(r=>JSON.stringify(r).toLowerCase().includes(q));$('#model-rows').innerHTML=filtered.slice(0,150).map(r=>`<tr><td><code>${esc(r.id)}</code></td><td>${esc(r.name || r.title || r.label || r.description || r.id)}</td><td><span class="pill">${esc(r.type || r.certainty || r.kind || r.profile_id || '记录')}</span></td><td><button class="table-row-button" data-edit-record="${esc(r.id)}">编辑 ↗</button></td></tr>`).join('');$('#model-count').textContent=`匹配 ${filtered.length} 条，展示前 ${Math.min(150,filtered.length)} 条；全部记录保留于模型。`;};draw();
  $('#model-search').addEventListener('input',draw);$('#edit-model-json').addEventListener('click',()=>editJSON('model'));
}
$('#panel-model').addEventListener('click',e=>{const g=e.target.closest('[data-model-group]'),r=e.target.closest('[data-edit-record]');if(g){S.modelGroup=g.dataset.modelGroup;renderModel();}if(r)editJSON(S.modelGroup,r.dataset.editRecord);});

function versionOptions(selected) {return versions().map(v=>`<option value="${esc(v.id)}" ${v.id===selected?'selected':''}>${esc(short(v.id))} · ${esc(v.message || '初始版本')} · ${esc(date(v.created_at))}</option>`).join('');}
function renderVersions() {
  if(!S.model)return panelEmpty('versions','版本记录与差异将在保存模型后出现。');
  const vs=versions();
  $('#panel-versions').innerHTML=`<div class="panel-heading"><div><h2>每次修改，都有来处</h2><p>比较已保存快照中的实体、关系、来源、原生 XML 及布局。未保存草稿不在版本差异中。</p></div><span class="pill">${vs.length} 个不可变版本</span></div><div class="panel-card"><div class="diff-controls"><label class="field"><span>基线版本</span><select id="diff-from">${versionOptions(vs.length>1?vs[1].id:vs[0]?.id)}</select></label><span>→</span><label class="field"><span>目标版本</span><select id="diff-to">${versionOptions(S.base)}</select></label><button id="compare-versions" class="button primary">比较版本</button><button id="checkout-version" class="button">载入为草稿</button></div><div id="diff-results" class="hint">选择两个版本查看字段级差异。</div></div><div class="panel-card"><h3>版本历史</h3><div class="table-wrap"><table><thead><tr><th>快照</th><th>变更说明</th><th>时间</th><th>评审状态</th></tr></thead><tbody>${vs.map(v=>`<tr><td title="${esc(v.id)}"><code>${esc(short(v.id))}</code>${v.id===S.project.head_version?' <span class="pill">HEAD</span>':''}</td><td>${esc(v.message)}</td><td>${esc(date(v.created_at))}</td><td>${esc(STATES[reviewState(v.id)] || reviewState(v.id))}</td></tr>`).join('')}</tbody></table></div></div>`;
  $('#compare-versions').addEventListener('click',guarded(async()=>{
    const from=$('#diff-from').value,to=$('#diff-to').value;
    const data=await api(`/projects/${S.project.id}/diff?from=${encodeURIComponent(from)}&to=${encodeURIComponent(to)}`);
    $('#diff-results').innerHTML=data.changes.length?`<p class="hint">${data.changes.length} 处记录变更 · <span class="diff-kind">added 新增</span><span class="diff-kind removed">removed 删除</span><span class="diff-kind modified">modified 修改</span></p>`+data.changes.map(c=>`<details class="diff-group"><summary><span class="diff-kind ${esc(c.kind)}">${esc(c.kind)}</span>${esc(c.group)} / ${esc(c.id || '字段')}</summary><div class="diff-content"><div><p class="hint" style="padding:0 16px">变更前</p><pre>${esc(pretty(c.before ?? null))}</pre></div><div><p class="hint" style="padding:0 16px">变更后</p><pre>${esc(pretty(c.after ?? null))}</pre></div></div></details>`).join(''):'<div class="empty-state">两个版本的模型与布局没有差异。</div>';
  }));
  $('#checkout-version').addEventListener('click',guarded(async()=>{
    if(!canLeave())return;const id=$('#diff-to').value;const version=await api(`/projects/${S.project.id}/versions/${encodeURIComponent(id)}`);
    remember();S.model=clone(version.model);S.layout=clone(version.layout || {});S.native=clone(version.native || null);S.nativeDiagnostics=version.validation?.native || null;S.view=S.model.views[0]?.id;S.selected=null;
    // Always save the restored snapshot against current HEAD; never rewrite history.
    S.base=S.project.head_version;modified();setTab('canvas');S.pendingFit=true;renderAll();toast('历史快照已载入为草稿；保存会建立新版本，不覆盖历史');
  }));
}

function renderReviews() {
  if(!S.model)return panelEmpty('reviews','评审必须绑定到不可变版本。');
  const current=reviewState();const events=S.project.reviews || [];
  $('#panel-reviews').innerHTML=`<div class="panel-heading"><div><h2>把判断留在版本上</h2><p>评审绑定保存后的模型快照。修改模型不会自动继承旧版本的接受结论。</p></div><span class="pill">${esc(STATES[current] || current)}</span></div><div class="warning-note">这里记录本地声明身份与评审意见，不提供身份认证，也不自动更改模型的 approval_status，更不等于业务签批。</div><div class="panel-card"><form id="review-form" class="review-form"><label class="field"><span>评审版本</span><select name="version">${versionOptions(S.base)}</select></label><label class="field"><span>记录人（本地声明身份）</span><input name="author" required maxlength="100" placeholder="填写姓名或角色"></label><label class="field"><span>评审动作</span><select name="action"><option value="submit">提交评审</option><option value="comment">添加意见</option><option value="request_changes">请求修改</option><option value="accept">记录本地接受</option></select></label><div class="field"><span>流程规则</span><p class="hint">先提交评审，才可接受或请求修改。已接受的版本不可继续变更评审结论；需要新版本。</p></div><label class="field wide"><span>意见与依据</span><textarea name="comment" required maxlength="10000" placeholder="说明判断、依据和待确认的问题"></textarea></label><div class="wide"><button type="submit" class="button primary">写入版本评审记录</button></div></form></div><div class="panel-card"><h3>评审时间线 · ${events.length} 条</h3><div class="timeline">${events.length?events.map(r=>`<article class="timeline-item"><strong>${esc(r.author)} · ${esc(STATES[r.action] || r.action)}</strong><p>${esc(r.comment)}</p><small>${esc(date(r.created_at))} · 版本 ${esc(short(r.version))} · 声明身份，未经认证</small></article>`).join(''):'<p class="hint">还没有评审记录。提交评审，开始形成有版本依据的反馈。</p>'}</div></div>`;
  $('#review-form').addEventListener('submit',guarded(async e=>{
    e.preventDefault();const form=e.target;const button=form.querySelector('[type=submit]');button.disabled=true;
    try{await api(`/projects/${S.project.id}/reviews`,{method:'POST',body:Object.fromEntries(new FormData(form))});
      const data=await api('/projects/'+S.project.id);S.project=data;updateHeader();renderReviews();toast('评审事件已绑定至指定版本');
    }finally{button.disabled=false;}
  }));
}

act('#generate',()=>{
  if(S.dirty){toast('请先保存当前草稿；生成任务只使用不可变的已保存版本',true);return;}
  modal('生成可追溯架构制品',`<form><p class="hint">输入绑定版本 <code>${esc(short(S.base))}</code>，成果保存到新的任务目录。</p><label class="field"><span>生成内容</span><select name="kind"><option value="project">项目 JSON 制品与交付物</option>${S.native?`<option value="native" ${!S.model.views.length?'selected':''}>原生 ${S.native.language.toUpperCase()} 原文与交换包</option>`:''}</select></label><label class="field"><span>预览方式</span><select name="render"><option value="false">保存可编辑源码与交换成果</option><option value="true">额外生成 SVG / PNG 预览</option></select></label>${S.native?'<label class="field"><span><input name="auto_layout" value="true" type="checkbox"> 显式为无坐标原生模型生成派生自动布局</span></label>':''}<p class="hint">原生图形能力不足或材料缺失时单独记录预览阻断；原文和已有 DI 保持。完整能力状态随诊断保存。</p>${actions('启动生成任务')}</form>`,async data=>{
    const job=await api(`/projects/${S.project.id}/generate`,{method:'POST',body:{version:S.base,kind:data.get('kind'),render:data.get('render')==='true',auto_layout:data.get('auto_layout')==='true'}});
    S.jobs.unshift(job);updateHeader();setTab('jobs');trackJob(job.id);toast('生成任务已排队');
  });
});
function renderJobs() {
  const panel=$('#panel-jobs');panel.innerHTML=`<div class="panel-heading"><div><h2>每个成果，绑定一个输入版本</h2><p>任务在后台执行；输出受空间限额和保留策略管理，重新打开项目后仍可查看任务记录。</p></div><span class="pill">${S.jobs.length} 个任务</span></div>`+(S.jobs.length?S.jobs.map(job=>`<article class="panel-card"><div class="job-header"><div><strong>${job.kind==='native'?'原生模型':'生成'}任务 ${esc(short(job.id))}</strong><p class="hint">版本 ${esc(short(job.version))} · ${esc(date(job.created_at))}</p></div><span class="job-status ${esc(job.status)}">${esc(STATES[job.status] || job.status)}</span></div>${job.outputs_pruned?'<p class="hint">此任务的输出附件已按保留策略清理；任务记录仍在。</p>':''}${job.native_preview?.issues?job.native_preview.issues.map(row=>`<p class="hint">${esc(row.category)} · ${esc(row.message)}</p>`).join(''):''}${job.error?`<pre>${esc(typeof job.error==='string'?job.error:pretty(job.error))}</pre>`:''}<div class="output-links">${(job.outputs || []).map(output=>`<a class="button small" href="${esc(output.url)}" target="_blank" rel="noopener">${esc(output.name)} ↗</a>`).join('')}</div></article>`).join(''):'<div class="panel-card empty-state"><h3>还没有生成任务</h3><p>保存模型后，点击顶部“生成制品”启动真实后端任务。</p></div>');
}
function trackJob(id) {
  if(S.jobTimers.has(id))return;
  const tick=async()=>{
    try {
      const data=await api('/jobs/'+id),index=S.jobs.findIndex(job=>job.id===id);
      if(index<0){S.jobTimers.delete(id);return;}S.jobs[index]=data;if(S.tab==='jobs')renderJobs();if(S.tab==='native')renderNativePreview();
      if(['queued','running'].includes(data.status))S.jobTimers.set(id,setTimeout(tick,1500));
      else {S.jobTimers.delete(id);toast(data.status==='succeeded'?'制品生成完成':data.status==='blocked'?'原文交换完成，预览材料或能力待补':'制品生成失败，请查看任务诊断',data.status!=='succeeded');}
    } catch(error){S.jobTimers.delete(id);report(error);}
  };
  S.jobTimers.set(id,setTimeout(tick,300));
}

$$('.tab').forEach(button=>button.addEventListener('click',()=>setTab(button.dataset.tab)));
act('#help',()=>modal('交互工作台 · 操作与边界',`<p>本工作台将现有共享模型、校验器和生成器连接起来，不再只是打开静态图。</p><ol class="hint"><li>创建项目或导入现有模型 JSON。</li><li>选择视图，搜索实体、筛选类型；拖动节点只改变布局。</li><li>选择实体或关系，在右侧修改属性、证据和确定性。</li><li>校验模型，处理结构与引用问题，再保存不可变版本。</li><li>比较版本，提交/反馈本地评审，按保存版本生成制品。</li></ol><div class="warning-note">仅本机单用户运行。不提供远程部署安全、真实身份认证或专业批准。交互画布是关系投影，不声明 TOGAF 或建模语言完整认证。表格和大模型提供明确的展示上限；原模型不删减。</div><p class="hint">Ctrl/⌘ + S 保存 · Ctrl/⌘ + Z 撤销草稿 · Ctrl/⌘ + Shift + Z 重做 · / 搜索 · Esc 清除选择</p>`));
act('#theme',()=>{const theme=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=theme;localStorage.setItem('atlas-theme',theme);});
document.documentElement.dataset.theme=localStorage.getItem('atlas-theme') || (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
window.addEventListener('beforeunload',e=>{if(S.dirty){e.preventDefault();e.returnValue='';}});
document.addEventListener('keydown',e=>{
  const typing=['INPUT','TEXTAREA','SELECT'].includes(e.target.tagName);
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='s'){e.preventDefault();if(!$('#save').disabled)$('#save').click();return;}
  if(!typing&&!$('#modal').open&&(e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='z'){
    e.preventDefault();const from=e.shiftKey?S.redo:S.undo,to=e.shiftKey?S.undo:S.redo;
    if(from.length){to.push(snapshot());const state=from.pop();S.model=state.model;S.layout=state.layout;S.native=state.native || null;S.nativeDiagnostics=null;S.selected=null;modified();renderAll();}return;
  }
  if(!typing&&!$('#modal').open&&e.key==='/'){e.preventDefault();setTab('canvas');$('#search').focus();}
  if(!typing&&e.key==='Escape'&&!$('#modal').open){S.selected=null;drawGraph();renderInspector();}
});
window.addEventListener('resize',()=>applyTransform());

async function init() {
  try {
    await api('/health');$('#connection').textContent='本地服务已连接';
    const catalog=await api('/catalog');S.catalog=catalog.templates || [];await refreshProjects();
    const previous=localStorage.getItem('atlas-project');const project=S.projects.find(p=>p.id===previous)||S.projects[0];
    if(project)await openProject(project.id);else renderAll();
  } catch(error){$('#connection').textContent='连接失败';renderAll();report(error);}
}
const ready=init();
