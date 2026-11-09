# -*- coding: utf-8 -*-
"""Instantiate the authored fictional ADM case; never invent real approvals.

Raw input is maintained separately. Source-step reasoning below is authored case
analysis, not a claim that arbitrary documents are automatically understood.
"""
from pathlib import Path
import copy,json,hashlib,re,sys
sys.dont_write_bytecode=True
H=Path(__file__).resolve().parent;C=H.parents[2];S=C/'skills/_shared';sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
from adm import initialize,contracts,load,digest,iteration_fingerprint,requirements_fingerprint,requirements_context,CONTRACT_PATH,check_cycle,markdown_report
from validate import validate
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
ANCHORS={'Preliminary':'preliminary',**{p:'phase-'+p.lower() for p in 'ABCDEFGH'},'Requirements':'requirements'}
DECISIONS={
'Preliminary':('如何复用实践并确保职责和治理可用？','复用已有EA实践，为跨订单/库存/物流实验裁剪；专项协调不变成人事汇报。','不重建整个组织；已有设计工时不等于实施和运营容量。'),
'A':('是否启动限定范围的架构设计与实验？','接受设计及隔离实验工作，不接受采购或生产扩店；愿景是受理/确认分离。','减少错误承诺是目标；缺收入和总体成本，不宣称财务收益。'),
'B':('怎样修正业务确认与物流门槛？','待确认和异常作为业务状态保留，中央预占后确认才允许物流。','保持断连受理连续性，同时不提供无依据的全球库存承诺。'),
'C':('数据权威和应用交互如何一致？','中央是承诺权威；order/event/reservation/policy身份贯通；同步A支持给定线上目标。','B满足库存条件但420ms超出300ms；成本及生产规模维度不能定优。'),
'D':('断连时哪些技术约束必须实现？','持久日志、认证恢复、去重/隔离和可观察性支持同一确认规则。','沿用现有中心与门店边界；产品、生产容量、保护措施实测仍待提供。'),
'E':('哪些工作包和可运营过渡覆盖跨域差距？','在线契约/物流门槛与离线持久/恢复工作包组合；先中央契约再恢复联调。','可并行开发日志；部署退出依赖、回退与运营检查仍必须明确。'),
'F':('怎样在本实验内排序与安排资源？','价值4.1/3.6、风险2.8/4.0分别呈现；80/120工时不超过实验可用100/140。','不相减指数，不计算无成本依据的ROI，不把设计容量当实施容量。'),
'G':('给定交付是否符合架构，例外是否受控？','给定160ms、不超量、重复去重、冲突隔离及物流拒绝测试满足实验判据；限期审计豁免后修复关闭。','实验结果不证明生产性能；实际部署和真实批准仍未取得。'),
'H':('观察是否触发架构变更，选择哪种迭代？','118/120是给定离线观察；V2触发接口、风险、运营、过渡及验证重新评审。','范围未扩展而局部迭代；超范围提交新工作请求；不把确认率当收入收益。')}
STEP_REASON={
'Preliminary':[
'限定订单/库存/物流和隔离试点；门店为渠道及运营参与方。',
'复用委员会、业务线管理和项目控制；库存政策及风险接受由业务承担。',
'采用四类架构任务及已给定设计期间容量；实施运维能力另列缺口。',
'中央原子预占后确认，物流只接已确认，来源与版本必须保留。',
'裁剪为并行B/C/D、跨域稳定ID和持续需求；不把模板当强制产物。',
'采用共享JSON与可编辑图派生；存储库区分来源、候选和治理记录；工具不代签。'],
'A':[
'根据情景委托建立设计与实验项目，11-10发起人仅接受该限定工作。',
'识别经营、库存、订单、物流、门店、安全数据及交付责任方和确认/恢复关注点。',
'目标减少错误库存承诺；范围外支付财税和平台重构明确列除。',
'设计任务容量给定，生产实施能力不可由此推断；采用现有跨域能力对象。',
'准备度仅支持隔离实验；采购、生产扩容和实施排班缺依据。',
'范围为在线预占、断连受理恢复和运营异常，覆盖11-09至12-04演练。',
'采用中央确认、已受理非承诺、物流门槛及可审计恢复原则。',
'愿景统一待确认、最终确认及异常；不声称已经上线。',
'实验指标1000请求不超量及线上p95≤300ms；收入增长不在证明范围。',
'风险为容量未知、重复/冲突、过期及人工责任；设计控制并保留生产验证。',
'情景接受设计与实验工作说明，明确真实上线采购需另授权，不生成真实批准。'],
'E':[
'组织可以复用现有EA及控制；重大影响是门店受理和中央承诺责任分离。',
'不断店受理但不能无库存承诺；保留纸面基线及真实负载/设备容量约束。',
'合并语义、持久化和运营三类跨B/C/D差距，不重复计算为三个独立目标。',
'物流只接确认，门店待确认，库存中央承诺；对齐跨业务职能要求。',
'统一order/event/reservation/policy标识、去重和隔离及中央重新检查。',
'WP-OFFLINE恢复联调依赖中央契约；日志开发可并行，不伪造全串行。',
'仅隔离实验就绪；容量未知和人工责任形成上线准入行动而非已消除风险。',
'受控在线试点后断连恢复，失败停止新增并保留存量核对。',
'WP-ONLINE覆盖确认语义和物流门槛；WP-OFFLINE覆盖持久、恢复与运营。',
'TRANS-ONLINE和TRANS-OFFLINE均保留数据、运营、依赖、控制及回退条件。',
'形成候选工作包/过渡/依赖和计划草稿；F才进一步评价资源及投资安排。'],
'F':[
'衔接既有项目控制、预算和治理；本次只接受隔离实验资源计划。',
'按事先准则加权：在线5×.7+2×.3=4.1；离线3×.7+5×.3=3.6。',
'在线80/100小时、离线120/140小时分开估算；非四个架构设计任务工时。',
'风险在线2×.6+4×.4=2.8、离线4；结合依赖优先中央契约；成本未知不算ROI。',
'确认相同工作包及过渡ID，架构定义保留确认、重放、隔离和物流条件。',
'计划包含实验窗口、依赖、运营检查点、退出及回退；情景接受不是真实批准。',
'记录复用和迭代经验，向实施交接治理；后续G/H不由设计周期收尾而省略。'],
'G':[
'交付负责人确认实验部署范围及优先级，拒绝扩大到生产扩店。',
'实施80/120小时与架构设计容量分开，实验团队责任有声明，真实排班未证。',
'按架构契约指导中央确认、持久恢复、幂等、隔离及物流拒绝。',
'用给定1000请求160ms/不超量、冲突隔离及96/100恢复检查符合性。',
'运营交接监控年龄、冲突、积压；阈值触发停止新增受理及人工核对。',
'11-30情景后实施评审关闭实验；DEV-AUDIT期限11-30，11-29修复关闭。'],
'H':[
'定义观察期12-01至12-04及分母120，118确认和2人工异常分别计算。',
'观察待确认年龄、混合政策、过期及人工处理，不从缺测量推断收益。',
'保留混合队列、误隔离和处理遗漏的风险及责任。',
'V2改变1件/8小时边界，对接口、风险、运营、过渡和验证联动。',
'形成版本化V2需求；中央确认原则不变，新增边界需新场景。',
'情景业务负责人提出变更并决定本范围迭代；超范围另请求新工作。',
'重开受影响B/C/D/E/F/G分析，旧决定不覆盖新政策，保留V1历史。'],
'Requirements':[
'从愿景和各域材料识别库存确认、离线受理、物流及恢复需求入规格/库。',
'相关阶段架构师和业务所有者确定优先级；需求过程组织基线并记录同意。',
'持续监控实验基线及V2触发，不把需求库当静态一次性表。',
'H识别限量2改1、24改8小时变化，保留其他原则。',
'记录优先级、冲突及影响评估，并确认情景利益相关者接受处理方式。',
'评价对当前及既往阶段影响，选择本范围迭代并发布n+1影响评估。',
'接收H产生的需求，交由受影响阶段的新迭代处理，不伪造生产实施。',
'更新库、版本及受影响接口/风险/运营/过渡/验证视图，保留历史。',
'在新迭代候选设计执行变更；本教学包未提供V2生产实施证据。',
'补回目标草稿意外漏掉的保留未确认订单/人工核对义务；该项是gap requirement，8小时新增门槛本身不是。']}
DOMAIN_STEPS=[
'选择回应%s确认语义和断连恢复关注点的视点，复用现有模型与来源。',
'基线：%s；保留真实环境与情景声明的区别。',
'目标：%s；只在本实验范围形成候选。',
'从同范围基线到目标分析差距：%s。',
'候选路线图组件追溯在线/离线工作包，评估工作、价值及风险而非只画图。',
'跨域复核中央确认、持久重放、物流门槛及运营职责，不让域设计互相冲突。',
'11-13情景利益相关者评审接受实验设计；保留生产未知与真实批准边界。',
'根据情景评审细化%s定义；未解决输入清楚列出，不虚构正式验收。',
'将同版本的%s基线、目标、差距及关系写入阶段工作记录并关联共享对象。']
def common(domain,baseline,target,gaps):return [s%(domain if i in (0,7,8) else baseline if i==1 else target if i==2 else gaps) if i in (0,1,2,3,7,8) else s for i,s in enumerate(DOMAIN_STEPS)]
STEP_REASON['B']=common('业务','纸面断连受理，物流门槛不一致','待确认/确认/异常与中央承诺','统一语义、持久化及异常责任')
STEP_REASON['C']=common('数据','纸面与中央缺稳定关联','中央权威与order/event/reservation/policy身份','缺关联、去重、隔离和治理')+common('应用','门店人工录入及各自对接物流','门店持久受理/中央预占/恢复及确认物流','接口职责、恢复契约和门槛缺失')
STEP_REASON['D']=common('技术','单中心及门店终端，断连无法访问中央','持久日志、认证恢复、去重/隔离和监控','断连持久、恢复保护和可观察性')

def main():
 raw=H/'adm-business-materials.md';text=raw.read_text();out=H/'generated-adm';out.mkdir(exist_ok=True)
 m=copy.deepcopy(load(H/'generated/sufficient/model.json'));m['project']['id']='omnichannel-adm-fictional';m['project']['name']='虚构全渠道履约ADM全周期';m['project']['version']='1'
 m['extensions']['entity_types']['case:adm-work-evidence']='有原始材料依据的虚构ADM分析记录，不代表实际组织批准'
 evidence_file='../../adm-business-materials.md'
 cycle=initialize(m,'ADM-FICTIONAL-1','限定设计与隔离情景实验；真实生产/采购/组织批准未授予')
 defs=contracts();phase_results=[]
 for phase,definition in defs.items():
  anchor=ANCHORS[phase];section=text.split('<a id="'+anchor+'"></a>',1)[1].split('<a id="',1)[0].strip()
  source='ADM-INPUT-'+phase;m['sources'].append({'id':source,'kind':'example','description':'独立维护的全虚构ADM原始材料','locator':'maintenance/cases/omnichannel/adm-business-materials.md#'+anchor})
  question,conclusion,tradeoff=DECISIONS[phase];identity='ADM-WORK-'+phase
  dossier={'id':identity,'type':'case:adm-work-evidence','name':'虚构 '+phase+' 架构工作记录','attributes':{'phase':phase,'question':question,'conclusion':conclusion,'tradeoffs':[tradeoff],'raw_material':section,'actual_business_approval':'not-granted','scope':'设计与隔离实验','unresolved_real_conditions':['生产负载/保护实测','真实成本与收益','实际治理授权及签署'],'source_steps':[]},'evidence':[source],'certainty':'assumed'}
  steps=definition['source_step_records'];ensure(len(steps)==len(STEP_REASON[phase]),phase+' step count')
  for step,reason in zip(steps,STEP_REASON[phase]):dossier['attributes']['source_steps'].append({'source_step_id':step['id'],'name_en':step['name_en'],'case_analysis_zh':reason,'evidence_source_id':source,'origin':'authored-fictional-case-analysis'})
  m['entities'].append(dossier);phase_results.append(dossier)
 # Bind actual objects; B/C/D depend on A, not on one another by numbering.
 refs={'Preliminary':['ROLE-CHIEF','ROLE-EA','ROLE-SEG','ROLE-SOL'],'A':['CAP-FULFIL','REQ-CONSISTENCY','REQ-OFFLINE'],'B':['CAP-ORDER','CAP-RESERVE','CAP-LOGISTICS','ORDER-PENDING','ORDER-CONFIRMED'],'C':['APP-ORDER','APP-STOCK','APP-STORE','IF-RESERVE','IF-RECOVERY'],'D':['LOCAL-ORDER-RECORD','CENTRAL-ORDER-RECORD'],'E':['WP-ONLINE','WP-OFFLINE','TRANS-ONLINE','TRANS-OFFLINE'],'F':['WP-ONLINE','WP-OFFLINE','TRANS-ONLINE','TRANS-OFFLINE'],'G':['ORDER-CONFIRMED','ORDER-FULFIL','IF-RECOVERY'],'H':['CAP-RESERVE','RISK-STOCK']}
 dependencies={'Preliminary':[],'A':['Preliminary-1'],'B':['A-1'],'C':['A-1'],'D':['A-1'],'E':['B-1','C-1','D-1'],'F':['E-1'],'G':['F-1'],'H':['G-1']}
 ev=lambda anchor:[{'path':evidence_file,'sha256':sha(raw),'locator':anchor}]
 for p in cycle['phases']:
  phase=p['phase'];it=p['iterations'][-1];it.update(owner='虚构 '+phase+' 责任人',status='completed',input_refs=[{'collection':'entities','id':i} for i in refs[phase]],output_refs=[{'collection':'entities','id':'ADM-WORK-'+phase}],depends_on=dependencies[phase])
  record=next(x for x in phase_results if x['attributes']['phase']==phase);a=record['attributes']
  for key in it['criteria']:it['criteria'][key]={'status':'satisfied','rationale':'情景记录针对“'+defs[phase]['criteria'][key]+'”：'+a['conclusion']+'；'+a['tradeoffs'][0],'evidence':ev(ANCHORS[phase])}
  it['decision']={'status':'accepted','authority':'全虚构情景责任人；无真实签署','authority_role':'stakeholder','rationale':a['conclusion']+'。仅为已给定情景接受，不授予真实批准。','evidence':ev(ANCHORS[phase])}
 cycle['requirements']['owner']='虚构需求协调人；实际优先级由相关阶段决定'
 # Every source step has specific authored reasoning; version checks still do not certify it.
 for p in cycle['phases']:
  phase=p['phase'];it=p['iterations'][-1]
  for step,reason in zip(it['source_step_coverage'],STEP_REASON[phase]):step.update(disposition='reuse' if phase=='Preliminary' else 'execute',rationale=reason+'（仅给定虚构情景）',evidence=ev(ANCHORS[phase]),context_sha256=iteration_fingerprint(m,it,cycle['scope']))
  it.update(model_sha256=iteration_fingerprint(m,it,cycle['scope']),contract_sha256=digest(load(CONTRACT_PATH)))
  cycle['requirements']['reviews'].append({'reviewer':'全虚构情景需求评审人','rationale':'依据需求基线及本阶段原始材料核对当前版本；不代表真实批准。','iteration_id':it['id'],'change_ids':[],'model_sha256':requirements_fingerprint(m,cycle,phase),'evidence':ev('requirements')})
 for step,reason in zip(cycle['requirements']['source_step_coverage'],STEP_REASON['Requirements']):step.update(disposition='execute',rationale=reason+'（情景设计及记录；不证明生产执行）',evidence=ev('requirements'),context_sha256=requirements_context(m,cycle))
 issues=validate(m);ensure(not [i for i in issues if i['level']=='error'],str(issues))
 dump(out/'model.json',m)
 # Evidence paths in nested output remain relative and portable.
 dump(out/'cycles/cycle.json',cycle);report=check_cycle(cycle,m,out/'cycles');ensure(not report['errors'],str(report['errors']));ensure(report['recorded_cycle_complete'] and report['foundation_source_coverage_complete'],'case not closed mechanically')
 dump(out/'adm-check.json',report);(out/'adm-check.md').write_text(markdown_report(report))
 # A new policy must invalidate the old affected phase decisions, even though
 # the diagrams still render. Preserve the old cycle as immutable history.
 changed=copy.deepcopy(m);v2=load(H/'generated/sufficient-policy-change/model.json')
 replacements={e['id']:e for e in v2['entities']}
 changed['entities']=[copy.deepcopy(replacements.get(e['id'],e)) for e in changed['entities']]
 changed['relationships']=copy.deepcopy(v2['relationships']);changed['project']['version']='2-candidate'
 changed['analyses']=copy.deepcopy(v2['analyses'])
 revised=copy.deepcopy(cycle)
 revised['requirements']['changes'].append({'id':'POLICY-V2','requirement_ids':['REQ-OFFLINE'],'reason':'限量2改1，保留24改8小时；需要新迭代，不沿用V1批准。','affected_phases':list('BCDEFGH'),'affected_refs':[{'collection':'entities','id':i} for i in ['CAP-RESERVE','IF-RECOVERY','RISK-STOCK','TRANS-OFFLINE','DELIVERY-NOTE']],'decision':{'status':'accepted','authority':'虚构业务所有者；仅情景变更请求','authority_role':'stakeholder','rationale':'接受在本范围开展局部迭代，不表示生产实施。','evidence':ev('phase-h')}})
 revised_report=check_cycle(revised,changed,out/'cycles')
 ensure(not any(e['code']=='model-invalid' for e in revised_report['errors']),str(revised_report['errors']))
 ensure(not revised_report['recorded_cycle_complete'] and not revised_report['foundation_source_coverage_complete'],'policy change retained stale completion')
 dump(out/'model-policy-v2.json',changed);dump(out/'cycles/cycle-policy-v2-needs-review.json',revised);dump(out/'adm-policy-v2-needs-review.json',revised_report)
 for record in phase_results:
  a=record['attributes'];lines=['# '+record['name'],'','全虚构，来源情景接受不代表真实批准。','',a['question'],'',a['conclusion'],'','权衡：'+a['tradeoffs'][0],'','## 原始材料','',a['raw_material'],'','## 按来源步骤的实际分析','']
  for st in a['source_steps']:lines+=['### '+st['name_en'],'',st['case_analysis_zh'],'','来源ID：'+st['source_step_id'],'']
  (out/(a['phase']+'.md')).write_text('\n'.join(lines))
 summary={'schema_version':'omnichannel-adm-case/1','is_example':True,'phases':9,'source_steps':94,'project_recorded_complete':True,'source_step_record_coverage':True,'actual_business_approval':'not-granted','independent_semantic_acceptance':'pending','source_raw_path':raw.relative_to(C).as_posix(),'source_sha256':sha(raw),'generated_model_sha256':sha(out/'model.json'),'phase_records':[{'id':x['id'],'phase':x['attributes']['phase'],'markdown':x['attributes']['phase']+'.md','source_step_count':len(x['attributes']['source_steps'])} for x in phase_results],'limits_zh':['本案例是源材料给定的完整虚构演练，非实际部署或任意文本自动理解证明。','94项记录须由不同评审人核实分析充分性；程序只检查引用、证据及版本。','与已有5版制品及图像共享稳定对象；本补充生成文字/JSON工作记录，不把它们冒充正式交付物组装。']}
 dump(out/'summary.json',summary);print({'phases':9,'steps':94,'recorded_complete':report['recorded_cycle_complete'],'source_coverage':report['foundation_source_coverage_complete']})
def ensure(v,m):
 if not v:raise AssertionError(m)
if __name__=='__main__':main()
