"""Build the two G20F operational extensions; no invented style scoring."""
import copy,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/'examples/addenda/delivery';CASE.mkdir(parents=True,exist_ok=True)
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
source=ROOT.parents[1]/'togaf-standard-10th-zh/G20Fe_赋能企业敏捷性.md'
lines=source.read_text().splitlines();features=[]
for number,line in enumerate(lines,1):
 if 368<=number<=391:
  cells=[s.strip() for s in line.strip('|').split('|')]
  if len(cells)==4:features.append({'id':f'F{len(features)+1:02}','feature':cells[0],'guidance':dict(zip(['rapid','agile','robust'],cells[1:])),'source':f'G20F 表4-1 L{number}'})
assert len(features)==24
save(ROOT/'references/source-tables/delivery-styles.json',{'source':'G20F §4.7.1 表4-1','rule':'一般画像而非刚性判定；混合/嵌套风格按范围记录，不计算匹配总分','features':features})
observations=['通知组件只影响预约回执','总计划涉及47个服务点和中央档案','回执复用既有短信接口','跨点身份与历史档案同步复杂','数据库与消息队列已稳定运行','团队拟采用未在本馆使用的事件流技术','法定保存与复核流程保持稳定','线上预约和退款流程正在重新定义','Java维护技能已有排班记录','事件流设计和恢复演练需要培训','线上预约为新业务能力','短信回执属于现有服务扩展','复用既有身份与检索构建块','将集成现有短信及支付服务','节庆通知组件目标两周交付','全馆迁移预计跨一个年度','节庆通知上线窗口两周不可延','档案迁移必须跨年度保存窗口','志愿者和IT预算限制同时存在','馆藏与收费记录不得丢失且需审计','预约退款功能仍在用户试验','跨馆身份与事件契约需要统一','只读短信模板修改影响有限','个人数据和收费迁移失败后果高']
raw={'notice':'虚构市民图书馆案例；原料、判断和规则均为演练，不代表真实授权','style_materials':[{'id':f'RAW-{i+1:02}','text':v} for i,v in enumerate(observations)],'option_materials':[{'id':'LAB-1','text':'通知子系统可保留集中队列A或事件流B；目录子系统可用已测API C或夜间文件D。A/C首轮可实现分钟级回执；D无法满足实时查验。B的恢复能力尚待实验。'},{'id':'LAB-2','text':'第二轮A端到端压测95分位延迟180毫秒，C契约兼容；项目约定预算与恢复窗口均满足。B恢复演练暂未满足项目要求，保留原始失败日志。'},{'id':'LAB-3','text':'变更实验扩大到47馆并发，A延迟800毫秒超出项目500毫秒要求；B的新恢复方案通过演练且与C的新接口契约兼容。规则和实验值均属项目。'}]}
sources=[{'id':x['id'],'kind':'example','description':x['text']} for x in raw['style_materials']+raw['option_materials']]
style={'features':[{'feature_id':f['id'],'applies':'yes','observation':v,'evidence_refs':[f'RAW-{i+1:02}']} for i,(f,v) in enumerate(zip(features,observations))],
'decisions':[{'scope_id':'archive-program','styles':['robust','agile'],'owner':'馆藏与技术负责人','rationale':'全馆数据迁移保留审慎架构控制；有界预约功能按试验迭代','evidence_refs':['RAW-02','RAW-04','RAW-16','RAW-24'],'conflicting_features':['F01','F02','F23','F24'],'tailoring':'全馆迁移robust；预约功能子项目agile；按过渡出口复核运行和恢复条件'},
{'scope_id':'sms-component','styles':['rapid'],'owner':'通知服务负责人','rationale':'仅复用现有只读模板；两周窗口且影响低','evidence_refs':['RAW-01','RAW-03','RAW-15','RAW-23'],'conflicting_features':['F02','F24'],'tailoring':'rapid只适用于只读通知组件，不继承到收费或数据迁移'}]}
modified_style=copy.deepcopy(style);modified_style['features'][22].update(applies='no',observation='通知增加个人收费数据，影响范围扩大，原低风险判断不成立',evidence_refs=['LAB-3']);modified_style['decisions'][1].update(styles=['agile','robust'],rationale='新增个人收费信息使原快速交付假设失效',tailoring='功能迭代采用agile；跨馆敏感数据契约与恢复门禁采用robust',evidence_refs=['LAB-3'])
def row(option,subsystem,iteration,status,assessment,evidence,reason='',new=None):return {'option_id':option,'subsystem':subsystem,'goal':'可追溯的分钟级预约回执','iteration':iteration,'hypothesis':'明确契约和恢复策略可满足本项目回执要求','assessment':assessment,'evidence_refs':evidence,'decision_owner':'架构与运营评审组','status':status,'decision_reason':reason or assessment,'new_evidence_refs':new or []}
options={'iterations':[row('A','通知',1,'retain','集中队列可复用，待扩大负载验证',['LAB-1']),row('B','通知',1,'retain','事件流需恢复实验',['LAB-1']),row('C','目录',1,'retain','已测API契约可兼容',['LAB-1']),row('D','目录',1,'eliminate','夜间文件不满足分钟级目标',['LAB-1'],'响应窗口不符',['LAB-1']),row('A','通知',2,'selected','180毫秒，满足项目条件',['LAB-2']),row('B','通知',2,'eliminate','恢复实验未满足项目要求',['LAB-2'],'恢复窗口超限',['LAB-2']),row('C','目录',2,'selected','A/C接口兼容',['LAB-2'])],
'constraints':[{'id':'CON-AC','source_option_id':'A','target_option_id':'C','rule':'事件键、事务重试和恢复窗口一致','status':'satisfied','evidence_refs':['LAB-2']},{'id':'CON-BC','source_option_id':'B','target_option_id':'C','rule':'事件契约及恢复窗口一致','status':'unknown','evidence_refs':['LAB-1']}],
'constraint_review':{'scope':'通知/目录两子系统','evidence_refs':['LAB-1','LAB-2'],'unmodeled_coupling':'支付系统接口另列缺口，不声明全企业兼容'}}
modified_options=copy.deepcopy(options);modified_options['iterations']+=[row('A','通知',3,'eliminate','扩大负载后800毫秒超出项目500毫秒限制',['LAB-3'],'新增47馆负载证据推翻旧评估',['LAB-3']),row('B','通知',3,'reopen','新恢复方案和接口演练通过，重开曾淘汰项',['LAB-3'],'新证据改变恢复判断',['LAB-3']),row('B','通知',4,'selected','新条件下满足恢复与契约',['LAB-3']),row('C','目录',4,'selected','与B的新接口契约经验证',['LAB-3'])];modified_options['constraints'][1].update(status='satisfied',evidence_refs=['LAB-3'])
FIELDS={'guide:delivery_feature_review':['feature_id','source_guidance','applies','observation','evidence_refs'],'guide:delivery_style_decision':['scope_id','styles','owner','rationale','evidence_refs','conflicting_features','tailoring'],'guide:sbce_iteration':['option_id','subsystem','goal','iteration','hypothesis','assessment','evidence_refs','decision_owner','status','decision_reason','new_evidence_refs'],'guide:sbce_constraint':['source_option_id','target_option_id','rule','status','evidence_refs']}
def entity(typ,id,name,a):return {'id':id,'type':typ,'name':name,'attributes':a,'evidence':a['evidence_refs'],'certainty':'assumed'}
def example(pid,data):
 if pid=='delivery-style-assessment':
  es=[entity('guide:delivery_feature_review',f['id'],f['feature'],dict(r,source_guidance=f['guidance'])) for f,r in zip(features,data['features'])]+[entity('guide:delivery_style_decision','decision-'+d['scope_id'],d['scope_id'],d) for d in data['decisions']]
  text='跨范围特征同时出现；全馆迁移采用稳健控制，预约按敏捷迭代，初始只读短信可快速。按范围说明理由，没有加权或多数票。'
 else:
  es=[entity('guide:sbce_iteration',f"{r['option_id']}-I{r['iteration']}",f"{r['subsystem']} / {r['option_id']} / 轮次{r['iteration']}",r) for r in data['iterations']]+[entity('guide:sbce_constraint',c['id'],c['rule'],{k:v for k,v in c.items() if k!='id'}) for c in data['constraints']]
  text='子系统分别并行探索备选；保留每轮淘汰和细化依据，再审跨子系统契约。选定后仍需验证未建模的支付接口；分析选择不等于正式批准。'
 return {'sources':sources,'entities':es,'relationships':[],'view':{'id':'v-'+pid,'artifact_id':'options-decision-matrix','profile_id':pid,'title':pid,'entity_ids':[e['id'] for e in es],'relationship_ids':[],'analysis':text,'legend':'项目判断；空白不代表不适用。来源画像、项目观察、淘汰/重开、分析选择和批准分开。'}}
profiles=[];methods=[]
for pid,name,data,mid,refs,steps in [('delivery-style-assessment','交付风格逐范围比较',style,'delivery-style-review',['G20F §4.7.1 表4-1'],['按24个特征提取分范围业务事实，未知保留unknown','对照三种风格的一般画像，解释冲突而非投票','按宏观/微观范围选择单一或混合风格，记录裁剪与负责人','改变风险或范围时重评，不把原选择自动传播给新范围']),('set-based-options-iteration','集合式并行方案逐轮评估',options,'set-based-options-review',['G20F §4.6'],['分子系统识别目标与多个备选，并行做足够架构分析','逐轮用可追溯证据保留/淘汰/细化备选','检查剩余组合的跨子系统约束；证据变化时保留重开历史','选定后继续细化并交授权方；记录未验证耦合'])]:
 ex=example(pid,data);types=list(dict.fromkeys(e['type'] for e in ex['entities']));checks=['没有来源或显式项目依据不增加评分/权重/合格线','每行事实与结论可追溯，未知不能写零','按实例范围和轮次保持稳定ID，改变材料重新生成','分析选择不授予正式批准']
 profiles.append({'id':pid,'artifact_id':'options-decision-matrix','name':name,'owner':'togaf-gap-solutions','renderer':'catalog','output_kind':'table','version':'2.2','source_refs':refs,'entity_types':types,'relationship_types':[],'required_attributes':{t:FIELDS[t] for t in types},'checks':checks,'template':{'id':pid,'version':'2.2','source_verified':False,'layout_notes':'正文方法的操作化表；不是原图复刻。'},'example':ex})
 methods.append({'id':mid,'name':name+'方法','owner':'togaf-gap-solutions','source_refs':refs,'input_fields':FIELDS,'steps':steps,'output_work_products':['options-decision-matrix'],'calculator':mid,'calculation_policy':'非评分，检查项目判断证据与时序约束；规则不代替分析','reference_document':'references/capability-addenda/'+pid+'.md'})
 doc='# '+name+'\n\n来源：'+'；'.join(refs)+'。此规范扩展既有 `options-decision-matrix`，不新增制品族。\n\n## 输入与缺口\n\n[原始材料](../../examples/addenda/delivery/raw-business-materials.json)来自虚构图书馆。需范围、目标、观察、实验、规则来源及有权决策角色。缺证据保留未知，不补默认风格或最优方案。\n\n## 方法\n\n'+'\n'.join(str(i+1)+'. '+s for i,s in enumerate(steps))+'\n\n## 元素与表示\n\n逐字段表保留稳定行ID；风格按范围，备选按option_id与iteration定位。表格相邻不代表依赖；依赖由约束表源/目标显式表示。\n\n```json\n'+json.dumps({t:FIELDS[t] for t in types},ensure_ascii=False,indent=2)+'\n```\n\n## 完整案例、修改和评审\n\n[初始输入](../../examples/addenda/delivery/baseline-inputs.json)、[修改输入](../../examples/addenda/delivery/modified-inputs.json)、[实际执行结果与反例](../../examples/addenda/delivery/execution-audit.json)。修改加入收费敏感数据使短信从rapid转混合控制；新并发实验推翻A方案并带证据重开B。评审先核对证据是否改变，再核对选择；不接受直接重写“最佳”结论。\n\n## 调用\n\n`generate.py model.json --profile '+pid+' --layout reference|adaptive --out output`。分析使用 `analyze.py` 的 `'+mid+'` 方法输入；每次只处理所请求范围。\n'
 (ROOT/'references/capability-addenda'/f'{pid}.md').write_text(doc)
package={'profiles':profiles,'analysis_methods':methods,'entity_definitions':{k:'G20F方法的项目操作记录；字段按视图规范解释，非新增官方元模型类型' for k in FIELDS},'patches':[{'target_kind':'work_products','target_id':'options-decision-matrix','add':{'entity_types':list(FIELDS),'source_refs':['G20F §4.6','G20F §4.7.1 表4-1'],'required_attributes':FIELDS,'checks':['G20F交付风格与SBCE子规范不使用一次性加权评分，按其独立方法执行。']}}],
'candidate_resolutions':{p['id']:{'status':'implemented-engineering-cases; independent-business-review-pending','work_product_ids':['options-decision-matrix'],'profile_ids':[p['id']],'method_ids':[m['id']],'case_evidence':'examples/addenda/delivery/execution-audit.json'} for p,m in zip(profiles,methods)}}
save(ROOT/'capability-addenda/delivery-work-products.json',package);save(CASE/'raw-business-materials.json',raw)
save(CASE/'baseline-inputs.json',{'styles':style,'options':options});save(CASE/'modified-inputs.json',{'styles':modified_style,'options':modified_options})
for label,values in [('baseline',[style,options]),('modified',[modified_style,modified_options])]:
 model={'schema_version':'2.0','project':{'id':'library-delivery','name':'虚构图书馆交付选择','version':label,'is_example':True,'approval_status':'candidate','implementation_status':'not-started','context':{'domains':['business','application'],'landscape':'segment','purpose':'project','abstraction':'logical','evolution':'target'}},'sources':sources,'entities':[],'relationships':[],'views':[],'deliverables':[],'gaps':[]}
 for p,data in zip(profiles,values):
  ex=example(p['id'],data);model['entities']+=ex['entities'];ex['view']['context']=model['project']['context'];model['views'].append(ex['view'])
 save(CASE/f'{label}-model.json',model)
print(json.dumps({'profiles':len(profiles),'methods':len(methods),'source_features':len(features)}))
