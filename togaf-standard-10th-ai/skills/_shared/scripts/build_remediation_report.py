"""Build a linked engineering report; never promotes source or business approval."""
import argparse,html,json,os,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parents[1]
SPECS=[
('G186/fig5-1','architecture-repository-structure','组成边驱动嵌套；外部标准/参考分别采纳。'),
('G186/fig3-2','architecture-landscape-projection','类别坐标交集投影；不声称精确三维尺度。'),
('G152/fig1-1','security-adm-concept-map','核对21概念、P/A共享、E/RM关联、15新增标记。'),
('G234/fig4-10','metadata-inference-structure','三来源、读取、结构上推和两路上行；内容访问限制单列。'),
('G234/fig5-1','metadata-business-function-map','业务功能映射保留概览；完整对象和关系在可导航分组明细中，不把伴随内容声称为主图连线。'),
('G234/fig5-2','metadata-application-function-map','应用功能映射按同ID保留概览和分页明细；实际DOM位置和锚点单独检查。'),
('G217/figC-1','ea-service-adm-reference-matrix','24列=6分类+18服务，10阶段；开发支持分类G格保留语义不确定性。'),
('G21I/fig5-2','msa-federated-governance-diagram','六治理要素与图5-1四层治理分开；项目候选控制复用同ID。'),
('G21I/fig5-3','soa-layered-reference','五层与四横切关注点；参考映射不是企业实际调用图。'),
('G21I/fig9-1','msa-source-deployment-diagram','源码、无业务库、部署、执行；项目实例不复制源图固定数量。'),
('G186/fig5-2','repository-state-view-tree','显式包含的状态/视图树；折叠内容未知。'),
('G186/fig5-3','repository-parallel-candidates','并列候选互相独立，不伪造比较箭头或时间顺序。'),
('G186/fig13-1','repository-target-baseline-comparison','Target→Baseline；状态由源/目标属性及子项数据推导。'),
('G186/fig13-2','repository-baseline-target-comparison','Baseline→Target；源/目标导航到稳定ID明细；不是商业工具界面复刻。'),
('G186/fig8-1','capability-project-continuum','0–10无单位，维持到改进的阅读顺序；不作日期或成熟度。'),
('G186/tabB-1','portfolio-stakeholder-concern-matrix','7×16、52个X；空白=未标注，非RACI。'),
('G186/fig5-5','architecture-project-schedule-default','多层任务、日期轴；旧milestone字符串为说明，显式里程碑才画菱形。')]

def load(path,default=None):return json.loads(path.read_text()) if path.is_file() else default

def evidence_failures(summary,stages,routes,portable):
 """Exit codes alone do not prove that persisted evidence met its contract."""
 failures=[]
 def require(ok,code):
  if not ok:failures.append(code)
 execution=summary['execution'];require(execution.get('all_commands_succeeded') is True,'command-failure-or-missing')
 require(execution.get('runtime_stable') is True,'runtime-changed-or-missing')
 if 'source_snapshot_current' in execution:require(execution['source_snapshot_current'] is True,'acceptance-source-snapshot-stale')
 if 'source_snapshot_stable' in execution:require(execution['source_snapshot_stable'] is True,'acceptance-source-snapshot-changed')
 if 'tests' in stages:
  s=summary['tests'];require(s.get('suite_count',0)>0 and s.get('suite_failures')==0,'unit-suite-failure-or-missing')
 if 'profiles' in stages:
  p=summary['profiles'];require(p.get('independent_profiles_checked',0)>0 and p.get('failed_profiles')==0 and not p.get('unselected_artifact_families'),'profile-failure-or-missing')
 if 'full' in stages:
  for layout,f in summary['full'].items():
   require(f['views']>0 and f['deliverables']==22 and not f['draft_views'] and not f['unbound_chapters'],'full-output-incomplete:'+layout)
 if 'cases' in stages:
  for kind,c in summary['cases'].items():
   require(c.get('chapters')==86 and not c.get('unbound_chapters') and not c.get('adm_errors'),'case-chapters-or-adm:'+kind)
   require(set(c.get('phases',{}))==set(['Preliminary']+list('ABCDEFGH')) and all(v=='recorded-complete' for v in c.get('phases',{}).values()),'case-phases:'+kind)
   require(all(c.get('probes',{}).get(k) is True for k in ['affected_reopened','unaffected_preserved','revalidated_complete','stale_evidence_rejected']),'case-change-probes:'+kind)
   require({g['layout'] for g in c.get('generated',[])}=={'reference','adaptive'} and all(g.get('deliverables')==22 and not g.get('draft_views') for g in c.get('generated',[])),'case-deliverables:'+kind)
   require(all(g.get('code')=='assembly-section-evidence-gap' and g.get('message') and g.get('needed_input') for g in c.get('assembly_gaps',[])),'internal-or-unexplained-case-evidence-gap:'+kind)
 if 'language' in stages:
  lang=summary['natural_language'];tasks=lang.get('tasks',[])
  require(lang.get('passed') is True and len({t['owner'] for t in tasks})==17 and all(t.get('missing_required_input_rejected') is True and not t.get('failures') for t in tasks),'natural-language-failure-or-missing')
 if 'sources' in stages:
  s=summary.get('source_integrity') or {};require(s.get('guides')==26 and s.get('guide_hash_matches')==26 and s.get('figure_records')==243 and s.get('figure_hash_matches')==243 and s.get('portable_projection_matches')==243 and s.get('figures_with_unresolved_routes')==0,'source-integrity-or-routes')
  require(routes.get('entry_count')==243 and len({r['id'] for r in routes.get('entries',[])})==243 and all(not r['unresolved'] for r in routes.get('entries',[])),'source-entry-routes')
 if 'portable' in stages:require(portable.get('passed') is True,'portable-failure-or-missing')
 if summary.get('focused_schedule') is not None:require(summary['focused_schedule'].get('passed') is True,'focused-schedule-failure')
 if summary.get('scale') is not None:require(summary['scale'].get('checks_passed') is True,'scale-regression')
 if summary.get('supplemental_validation') is not None:require(summary['supplemental_validation'].get('passed') is True,'supplemental-validation-failure')
 if execution.get('rendered'):
  expected=(1 if 'profiles' in stages else 0)+(2 if 'full' in stages else 0)+(4 if 'cases' in stages else 0)+(2 if summary.get('focused_schedule') is not None else 0)
  require(len(summary['geometry'])>=expected,'geometry-results-missing')
  for path,g in summary['geometry'].items():require(g.get('checked',0)>0 and g.get('flagged')==0 and g['text_overlaps']==0 and g['edges_through_nodes']==0,'geometry-failure:'+path)
 return failures

def build(out,tests=None):
 out=Path(out).resolve();tests=Path(tests).resolve() if tests else out
 rel=lambda p:os.path.relpath(p,out)
 suites=load(tests/'unittest-results.json',{});execution=load(out/'execution-summary.json',{})
 snapshot=load(out/'acceptance-inputs-after.json')
 if snapshot is not None:
  from run_remediation_acceptance import acceptance_fingerprints
  execution['source_snapshot_current']=snapshot==acceptance_fingerprints()
 verification=load(out/'profiles/verification.json',{});source=load(out/'source-integrity.json',{});language=load(out/'natural-language-summary.json',{})
 cases={k:load(out/'cases'/k/'summary.json',{}) for k in ['lingang','qianlin']}
 geometry={str(p.relative_to(out)):load(p,{}) for p in out.glob('**/geometry-check.json') if 'portable' not in p.parts}
 geometry_summary={k:{'checked':v.get('checked'),'flagged':v.get('flagged'),'text_overlaps':sum(len(r.get('text_overlaps',[])) for r in v.get('results',[])),'edges_through_nodes':sum(len(r.get('edges_through_nodes',[])) for r in v.get('results',[]))} for k,v in geometry.items()}
 full={layout:load(out/'full-output'/layout/'manifest.json',{}) for layout in ['reference','adaptive']}
 summary={'tests':suites,'execution':execution,'profiles':verification.get('summary',verification),'cases':cases,'geometry':geometry_summary,'source_integrity':source.get('summary'), 'natural_language':language,'full':{k:{'views':len(v.get('artifacts',[])),'deliverables':len(v.get('deliverables',[])),'draft_views':[a['view_id'] for a in v.get('artifacts',[]) if a.get('status')=='draft-with-gaps'],'unbound_chapters':[s for d in v.get('deliverables',[]) for s in d.get('unbound_section_titles',[])]} for k,v in full.items()},'professional_review':'pending-professional-review','business_acceptance':'not-assessed','C220':'full-body-unavailable'}
 summary['focused_schedule']=load(out/'focused-schedule/summary.json')
 summary['scale']=load(out/'scale/report.json')
 summary['supplemental_validation']=load(out/'supplemental-validation.json')
 stages=set(load(out/'baseline.json',{}).get('stages',[]))
 if suites:stages.add('tests')
 summary['engineering_failures']=evidence_failures(summary,stages,load(out/'source-routes.json',{}),load(out/'portable/portability-report.json',{}))
 summary['engineering_passed']=not summary['engineering_failures']
 summary['validated_stages']=sorted(stages)
 (out/'repair-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 gallery=out/'gallery';gallery.mkdir(exist_ok=True);crops=ROOT/'reviews/source-package-2026-11-02-v2/original-crops';sections=[];records=[]
 for fid,pid,assessment in SPECS:
  originals=list(crops.glob(fid.replace('/','-')+'-*'));original=originals[0] if originals else None
  if original:shutil.copyfile(original,gallery/original.name)
  new=out/'profiles'/(pid+'-reference.png');adapt=out/'profiles'/(pid+'-adaptive.png');old=REPO/'output/togaf-skills-recheck-20261104-215807/full-output/reference/artifacts'/('profile-'+pid+'.png')
  tiles=[]
  for title,p in [('英文原图',gallery/original.name if original else None),('修复前',old),('修复后 reference',new),('修复后 adaptive',adapt)]:
   if p and p.is_file():tiles.append('<figure><figcaption>'+title+'</figcaption><a href="'+os.path.relpath(p,gallery)+'"><img loading="lazy" src="'+os.path.relpath(p,gallery)+'"/></a></figure>')
  links=[]
  for suffix,label in [('.svg','SVG'),('.coverage.json','覆盖位置'),('.details.html','分组明细')]:
   path=out/'profiles'/(pid+'-reference'+suffix)
   if path.is_file():links.append('<a href="'+os.path.relpath(path,gallery)+'">'+label+'</a>')
  if pid=='architecture-project-schedule-default' and (out/'focused-schedule/summary.json').is_file():
   links.append('<a href="../focused-schedule/reference/artifacts/three-level-schedule.png">三层排期与同日里程碑复验</a>')
  sections.append('<section id="'+fid.replace('/','-')+'"><h2>'+fid+' / '+pid+'</h2><p>'+html.escape(assessment)+'</p><div class="images">'+''.join(tiles)+'</div><p>'+' · '.join(links)+'</p></section>')
  records.append({'figure_id':fid,'profile_id':pid,'original_locator':str(original.relative_to(REPO)) if original else '未定位裁图','assessment':assessment,'source_verification':'assistant-scoped-comparison; not independent professional acceptance','uncertainty':'布局为可读重排；企业实例不等同参考示例；具体原图限制见portable structure JSON'})
 (gallery/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>TOGAF参考图对照画廊</title><style>body{font:16px sans-serif;margin:30px;line-height:1.6}.images{display:flex;gap:14px;align-items:flex-start}figure{margin:0;flex:1;min-width:0}img{width:100%;max-height:1100px;object-fit:contain;object-position:top}section{border-top:1px solid #aaa;padding:20px 0}a{overflow-wrap:anywhere}</style><h1>参考原图与修复输出</h1><p>来源核对、工程验证、专业评审与业务批准分别记录。点击图片查看原尺寸；本页没有授予source_verified或业务批准。</p>'+''.join(sections)+'</html>')
 (out/'source-comparisons.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
 old=load(REPO/'output/togaf-skills-recheck-20261104-215807/finding-status-diff.json',[])
 descriptions=[
 '修正来源路由并补齐6个G186入口；所有243入口可达性另列。',
 '存储库实际包含/采纳关系与全景坐标交集驱动输出；独立删边反例拒绝。',
 '21概念分组、P/A共享、E/RM关联及15新增标记；企业裁剪保留理由。',
 '读取、剖析、结构上推、元数据上行的连接/方向/端点均检查；逐边删除拒绝。',
 '递归三层排期、日期一致性、孤儿/循环/越界；字符串说明兼容；严格拒绝/草稿披露。',
 '既有ABB/SBB、采用因素及反向realizes契约保留回归保护。',
 'path和g包裹path均扫描；DORP合法门禁交叉专项区分。',
 '主全量样例17个原缺口已绑定；两案各22份86章均绑定；千林9项现场/签章证据缺口保留解释。',
 '两案有四域四态、不同阶段输入/输出、实际分析、完整追溯；版本化CR重开、无关阶段保留和旧证据拒绝。',
 'EA×ADM来源/企业矩阵、MSA六要素及四层治理、源码部署执行入口；SOA五层四关注点保护。',
 '自适应卡片/区域布局、长元数据概览与分页明细、实际DOM位置与稳定锚点；几何复验见单独结果。',
 '注册基线防删除、唯一性完整性检查、类型定义、真实谓词重复检测、指南方法/定义/依赖与技能入口同步。']
 evidence=['source-routes.json','profiles/architecture-repository-structure-reference.coverage.json','profiles/security-adm-concept-map-reference.coverage.json','profiles/metadata-inference-structure-reference.coverage.json',rel(tests/'logs/test_remediation_invariants.log'),rel(tests/'logs/test_building_block_contract.log'),rel(tests/'logs/test_geometry_path_selection.log'),'cases/lingang/assemblies.json','cases/qianlin/change-probes.json','gallery/index.html','repair-summary.json',rel(tests/'unittest-results.json')]
 findings=[]
 for i,desc in enumerate(descriptions):
  previous=next((f for f in old if f['id']=='F%02d'%(i+1)),{})
  findings.append({'id':'F%02d'%(i+1),'title':previous.get('title'),'previous':previous.get('status'),'implementation':desc,'status':'工程复验待核' if not summary['engineering_passed'] or stages!=set(['tests','profiles','full','cases','language','sources','portable']) else '工程修复已复验；专业与业务批准独立','evidence':evidence[i]})
 (out/'F01-F12-closure.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n')
 lines=['# TOGAF Skills 修复与双案例验收报告','',f"全量测试：{suites.get('suite_count','未运行')} 模块，{suites.get('tests_executed','未记录')} 项，失败模块 {suites.get('suite_failures','未记录')}。",'', '工程证据门禁：'+('通过' if summary['engineering_passed'] else '未通过：'+', '.join(summary['engineering_failures']))+'。已验证阶段：'+', '.join(sorted(stages))+'。','', '[参考图对照画廊](gallery/index.html) · [F01–F12台账](F01-F12-closure.json) · [完整指标和几何结果](repair-summary.json) · [243条来源入口](source-routes.json) · [来源文件完整性](source-integrity.json)','', '## 双案例','', '| 模拟案例 | 交付物 | 章节 | 未绑定章 | ADM记录 | 业务批准 |','| --- | --- | --- | --- | --- | --- |']
 for kind,c in cases.items():
  lines.append('| ['+kind+'](cases/'+kind+'/index.md) | 22 | '+str(c.get('chapters','未生成'))+' | '+str(len(c.get('unbound_chapters',[])))+' | '+str(len(c.get('phases',{})))+'阶段 | not-assessed |')
  folder=out/'cases'/kind;folder.mkdir(parents=True,exist_ok=True)
  case_lines=['# '+kind+' 模拟设计交付包','','专业评审待进行；业务批准未评估。软件模拟不证明现场系统性能或真实接受。','', '[模型](model.json) · [阶段记录](adm-cycle.json) · [阶段检查](adm-check.json) · [变更与过期证据反例](change-probes.json) · [软件模拟](simulation.json) · [章节组装和缺口](assemblies.json)','','## 22份交付物','']
  mf=load(folder/'reference/manifest.json',{})
  for d in mf.get('deliverables',[]):case_lines.append('- ['+d['id']+'](reference/'+d['path']+')')
  case_lines+=['','## 外部证据限制','']+['- '+s for s in c.get('external_evidence',[])]+['','具体缺口及其章节、模型ID见assemblies.json；未删除真实缺口来取得绿色状态。']
  (folder/'index.md').write_text('\n'.join(case_lines)+'\n')
 lines+=['','## 工程结果','',f"制品规范 {verification.get('independent_profiles_checked','未生成')} 个，覆盖 {verification.get('artifact_families_checked','未生成')} 个注册制品族；失败规范 {verification.get('failed_profiles','未生成')}。原始与字段修改输入均执行双布局检查。",'',f"几何检查共 {sum(g.get('checked',0) for g in geometry_summary.values())} 张图，标记缺陷 {sum(g.get('flagged',0) for g in geometry_summary.values())}；DORP合法门禁交叉保留在各geometry-check.json中。",'', '[三层排期、持续任务与里程碑](focused-schedule/reference/artifacts/three-level-schedule.png) · [五项独立严格拒绝与草稿披露](focused-schedule/summary.json) · [规模回归与新类型合成补充](scale/report.json) · [17项自然语言任务执行](natural-language-summary.json) · [离线独立目录运行](portable/portability-report.json)','', '[最终定向复验与执行来源](supplemental-validation.json)记录正文状态绑定和报告门禁变更后的实际执行；此前失败输出保留供复查。[目视观察范围与图片哈希](visual-observations.json)单独列明，不与几何测量或专业来源认可合并。','','## F01–F12','','| 缺陷 | 修复和复验范围 | 证据 |','| --- | --- | --- |']
 for f in findings:lines.append('| '+f['id']+' '+str(f['title'])+' | '+f['implementation']+' | [记录]('+f['evidence']+') |')
 lines+=['','## 验收边界','','来源范围是项目现有26份指南；C220全文未取得。243入口的文件/路由复核不等于243幅原图逐项专业认可。详细图形对照限定在画廊列明的图及原图位置，没有批量设置source_verified。','', '千林保留9项涉及真实演练、质量接受及签章的证据缺口；临港保留仪表校准、现场时钟/网络恢复、排班报价及角色批准等外部输入。两案均为模拟设计，软件规则重放不能替代这些现场事实。','', '自然语言验收覆盖17技能各一项实际任务，保存选择依据、输入、输出、字段修改与缺输入反例；由本轮助手选择方法，不宣称盲测或另一模型独立验收。','', '工程结果、来源核对、专业评审及业务批准分开记录。未满足后两类条件时不声称官方TOGAF等价、生产可用或业务批准。','','## 重复运行','','```sh','skills/_shared/.venv/bin/python skills/_shared/scripts/run_remediation_acceptance.py --out output/togaf-remediation-new','```','']
 (out/'repair-report.md').write_text('\n'.join(lines));return summary

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--tests');a=p.parse_args();build(a.out,a.tests)
