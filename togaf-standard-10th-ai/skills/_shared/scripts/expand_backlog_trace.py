# -*- coding: utf-8 -*-
"""Prepare a source-bounded G20F extension with a complete changed-scope case."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CASE=ROOT/'examples/addenda/backlog-trace'
PID='architecture-strategic-mva-trace';MID='architecture-backlog-trace-review'
REFS=['G20F §4.5 L304–327','G20F §5.2.3 L529–547','G20F §5.3.2 L601–632']
def save(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
raw=[('BR-1','虚构图书馆战略：让读者自助办理预约与取消，减少人工重复录入。本项目采用战略意图—epic—feature—story层次；只是本项目追溯规则。'),
('BR-2','产品负责人把预约受理列为首次开放的必须项，退款登记暂为应有项。首个MVA仅覆盖预约受理，排除退款自动结算和历史借阅迁移；后续功能仍保留在产品待办。'),
('BR-3','预约受理故事要求每位读者每场次最多一项有效预约。退款登记故事要求取消后下一营业日生成退款队列记录；依赖预约标识。两故事均由读者服务负责人确认，尚无运行验收结果。'),
('BR-4','架构负责人规定预约幂等ABB及退款可追溯ABB；实施候选分别为预约API与退款队列适配器SBB。SBB到ABB是设计实现关系，尚未部署。'),
('BR-5','修改：预约与取消必须在同一开放窗口提供。产品负责人把退款登记提升为must-have，扩展同一MVA范围，仍排除自动结算及历史迁移；保留原MVA范围历史。'),
('BR-6','修改后的测试记录：预约幂等契约测试通过；退款队列与外部财务接口尚未演练。测试通过仅证明预约验收条件，不证明整套MVA可运营。')]
sources=[{'id':i,'kind':'example','description':t} for i,t in raw]
def node(i,kind,name,refs,**attrs):
 return dict(id=i,kind=kind,name=name,owner='读者服务负责人' if kind in ['strategic_intent','epic','feature','story','mva'] else '架构负责人',evidence=refs,**attrs)
def edge(i,typ,s,t,refs):return {'id':i,'type':typ,'source':s,'target':t,'evidence':refs}
base={'source_ids':[s['id'] for s in sources],'hierarchy_policy':{'levels':['strategic_intent','epic','feature','story'],'evidence':['BR-1']},'nodes':[
 node('G-SELF','strategic_intent','读者自助服务',['BR-1'],landscape='strategic',evolution='target',statement='让读者自助办理预约与取消，减少人工重复录入'),
 node('E-RESERVE','epic','自助预约与取消产品',['BR-1'],landscape='segment',evolution='target',statement='读者可自助完成预约及取消申请'),
 node('F-BOOK','feature','预约受理功能',['BR-3'],landscape='segment',evolution='target',statement='受理并核验预约唯一性'),
 node('F-REFUND','feature','取消退款登记功能',['BR-3'],landscape='segment',evolution='target',statement='保留取消依据并登记退款队列'),
 node('S-BOOK','story','预约唯一性故事',['BR-2','BR-3'],landscape='capability',evolution='target',statement='作为读者，我希望不会因重复提交产生重复预约',priority='must-have',priority_evidence=['BR-2'],acceptance_criteria='每位读者每场次最多一项有效预约',acceptance={'status':'not-observed','evidence':[]}),
 node('S-REFUND','story','取消后退款登记故事',['BR-2','BR-3'],landscape='capability',evolution='target',statement='作为读者，我希望取消后可查询退款登记',priority='should-have',priority_evidence=['BR-2'],acceptance_criteria='取消后下一营业日生成带预约标识的退款队列记录',acceptance={'status':'not-observed','evidence':[]}),
 node('ABB-IDEMPOTENT','abb','预约幂等规定',['BR-4'],responsibility='保证预约标识与幂等处理',interface='提交/查询预约',quality='并发重复提交不重复受理'),
 node('ABB-REFUND','abb','退款可追溯规定',['BR-4'],responsibility='关联取消、退款登记及原预约',interface='登记/查询退款',quality='取消记录可追溯'),
 node('SBB-API','sbb','预约API候选实现',['BR-4'],responsibility='实现预约幂等契约',product='项目自研预约API',version='candidate-v1'),
 node('SBB-QUEUE','sbb','退款队列适配器候选实现',['BR-4'],responsibility='实现取消后队列登记',product='项目队列适配器',version='candidate-v1'),
 node('MVA-OPEN','mva','首次开放MVA',['BR-2'],boundary='预约受理及幂等护栏',exclusions=['退款自动结算','历史借阅迁移','本期退款队列登记'],candidate_story_ids=['S-BOOK','S-REFUND'],decision_owner='产品负责人',decision_evidence=['BR-2'],history=[{'version':'v1','boundary':'仅预约受理','selected_story_ids':['S-BOOK'],'evidence':['BR-2']}])],
 'relationships':[
 edge('R-GE','g20f:refines','G-SELF','E-RESERVE',['BR-1']),edge('R-EFB','g20f:refines','E-RESERVE','F-BOOK',['BR-1','BR-3']),edge('R-EFR','g20f:refines','E-RESERVE','F-REFUND',['BR-1','BR-3']),
 edge('R-FSB','g20f:refines','F-BOOK','S-BOOK',['BR-3']),edge('R-FSR','g20f:refines','F-REFUND','S-REFUND',['BR-3']),
 edge('R-CB','g20f:constrains-story','ABB-IDEMPOTENT','S-BOOK',['BR-4']),edge('R-CR','g20f:constrains-story','ABB-REFUND','S-REFUND',['BR-4']),
 edge('R-AB','g20f:allocated-to-sbb','S-BOOK','SBB-API',['BR-4']),edge('R-AR','g20f:allocated-to-sbb','S-REFUND','SBB-QUEUE',['BR-4']),
 edge('R-IB','realizes','SBB-API','ABB-IDEMPOTENT',['BR-4']),edge('R-IR','realizes','SBB-QUEUE','ABB-REFUND',['BR-4']),
 edge('R-MB','g20f:included-in-mva','S-BOOK','MVA-OPEN',['BR-2']),edge('R-DEP','g20f:story-depends-on','S-REFUND','S-BOOK',['BR-3'])]}
modified=copy.deepcopy(base);byid={n['id']:n for n in modified['nodes']}
byid['S-REFUND'].update(priority='must-have',priority_evidence=['BR-5'],evidence=['BR-3','BR-5'])
byid['S-BOOK']['acceptance']={'status':'verified','evidence':['BR-6']}
byid['MVA-OPEN'].update(boundary='预约受理、取消退款登记及其幂等/追溯护栏',exclusions=['退款自动结算','历史借阅迁移'],decision_evidence=['BR-5'],evidence=['BR-2','BR-5'])
byid['MVA-OPEN']['history'].append({'version':'v2','boundary':'预约与退款登记同期开放','selected_story_ids':['S-BOOK','S-REFUND'],'evidence':['BR-5']})
modified['relationships'].append(edge('R-MR','g20f:included-in-mva','S-REFUND','MVA-OPEN',['BR-5']))
DEFINITIONS={
 'g20f:refines':{'source_types':['goal','requirement'],'target_types':['requirement'],'meaning':'本项目声明的战略意图到epic/feature/story逐层细化，不是流程先后'},
 'g20f:constrains-story':{'source_types':['abb'],'target_types':['requirement'],'meaning':'ABB对故事给出功能/非功能护栏'},
 'g20f:allocated-to-sbb':{'source_types':['requirement'],'target_types':['sbb'],'meaning':'故事分配到候选SBB实现，不表示已实现'},
 'g20f:included-in-mva':{'source_types':['requirement'],'target_types':['guide:mva_scope'],'meaning':'显式必须项纳入命名MVA边界，非已验收或完整MVP'},
 'g20f:story-depends-on':{'source_types':['requirement'],'target_types':['requirement'],'meaning':'依赖方故事指向前置故事，非优先级或完成顺序断言'}}
NAMES={'g20f:refines':'细化','g20f:constrains-story':'护栏约束','g20f:allocated-to-sbb':'计划分配','g20f:included-in-mva':'纳入MVA','g20f:story-depends-on':'依赖前置','realizes':'候选设计实现'}
TYPES={'strategic_intent':'goal','epic':'requirement','feature':'requirement','story':'requirement','abb':'abb','sbb':'sbb','mva':'guide:mva_scope'}
CTX={'domains':['business','application'],'landscape':'capability','purpose':'project','abstraction':'logical','evolution':'target'}
def example(data):
 entities=[]
 for n in data['nodes']:
  a={k:copy.deepcopy(v) for k,v in n.items() if k not in ['id','name','evidence','landscape','evolution']}
  e={'id':n['id'],'type':TYPES[n['kind']],'name':n['name'],'attributes':a,'evidence':n['evidence'],'certainty':'assumed','approval_status':'candidate','implementation_status':'not-started',
     'context':dict(CTX,landscape=n.get('landscape','capability'),abstraction='physical' if n['kind']=='sbb' else 'conceptual' if n['kind']=='strategic_intent' else 'logical')}
  entities.append(e)
 relations=[dict(r,label=NAMES[r['type']],certainty='assumed') for r in data['relationships']]
 return {'sources':sources,'entities':entities,'relationships':relations,'extensions':{'relationship_types':DEFINITIONS},'analyses':[{'id':'A-TRACE','method_id':MID,'inputs':data,'evidence':data['source_ids']}],
 'view':{'id':'v-'+PID,'artifact_id':'architecture-backlog','profile_id':PID,'title':'战略意图—MVA—产品待办—ABB/SBB追溯','context':CTX,'entity_ids':[e['id'] for e in entities],'relationship_ids':[r['id'] for r in relations],
 'analysis':'从原始材料逐层形成稳定对象、MVA范围和设计实现链接。优先级来自产品负责人；候选SBB关系不证明已部署。','legend':'战略/分段/能力是全景层级，全部目标状态另记；关系方向和项目层次显式定义；入选不等于验收。','attributes':{'analysis_ids':['A-TRACE']}}}
def model(data,label):
 ex=example(data)
 return dict(schema_version='2.0',project={'id':'library-backlog','name':'虚构图书馆MVA范围变更','version':label,'is_example':True,'approval_status':'candidate','implementation_status':'not-started','context':CTX},deliverables=[],gaps=[],**{k:v for k,v in ex.items() if k!='view'},views=[ex['view']])
fields={'goal':['kind','owner','statement'],'requirement':['kind','owner','statement'],'abb':['kind','owner','responsibility','interface','quality'],'sbb':['kind','owner','responsibility','product','version'],'guide:mva_scope':['kind','owner','boundary','exclusions','candidate_story_ids','decision_owner','decision_evidence','history']}
steps=['逐句提取战略意图、业务分段、故事和原始来源；项目声明epic/feature/story层次，不能假称标准要求','依据产品负责人排序形成MVA必须项边界；保留未纳入项及排除理由','把ABB护栏及计划SBB实现显式关联到故事；核对实现方向和前置依赖','修改战略或边界时保留ID与历史，重算纳入集合与依赖；分别检查验收证据和可运营条件']
profile={'id':PID,'artifact_id':'architecture-backlog','name':'战略—MVA—产品待办追溯','owner':'togaf-requirements','renderer':'catalog','output_kind':'table','version':'2.2','source_refs':REFS,'entity_types':list(fields),'relationship_types':list(DEFINITIONS)+['realizes'],'required_attributes':fields,'checks':['每个故事追溯到战略意图','MVA选择与明确的must-have一致','SBB到ABB方向和故事分配一致','未验收和未验证的范围外依赖必须显式报告'],'template':{'id':PID,'version':'2.2','source_verified':False,'layout_notes':'正文方法的关系表；不声称复刻G20F图4-4或5-4'},'table_orientation':'records','example':example(base),'method_reference':'references/capability-addenda/'+PID+'.md'}
method={'id':MID,'name':'战略MVA追溯与边界变更评审','owner':'togaf-requirements','source_refs':REFS,'required_inputs':['原始战略与业务需求','产品负责人明确排序及范围','ABB护栏和SBB候选','依赖及验收证据'],'missing_input_policy':'缺关键关系/来源拒绝完成判断；未观察验收返回pending-evidence而非伪造通过','analysis_steps':steps,'output_work_products':['architecture-backlog'],'calculator_id':MID,'example_model':'examples/addenda/backlog-trace/baseline-model.json','method_reference':profile['method_reference']}
package={'package_id':'strategic-backlog-trace','version':'1.0','profiles':[profile],'analysis_methods':[method],'relationship_definitions':DEFINITIONS,'entity_definitions':{'guide:mva_scope':'有名称、范围和选择依据的最小可行架构边界；不是MVP或部署状态'},
 'patches':[{'target_kind':'work_products','target_id':'architecture-backlog','add':{'entity_types':list(fields),'relationship_types':list(DEFINITIONS)+['realizes'],'source_refs':REFS}}],
 'candidate_resolutions':{'architecture-backlog-trace':{'status':'implemented-engineering-cases; independent-business-review-pending','work_product_ids':['architecture-backlog'],'profile_ids':['architecture-business-backlog','architecture-sprint-backlog',PID],'method_ids':['architecture-backlog-method',MID],'evidence_paths':['examples/addenda/backlog-trace/execution-audit.json'],'remaining_scope':['公开官方正文定义独立核实','新的原始业务材料独立验收']}}}
save(ROOT/'capability-addenda/strategic-backlog-trace.json',package)
save(CASE/'raw-business-materials.json',{'notice':'虚构案例，项目规则不是TOGAF默认规则','records':[{'id':i,'text':t} for i,t in raw]})
for label,data in [('baseline',base),('modified',modified)]:save(CASE/f'{label}-inputs.json',data);save(CASE/f'{label}-model.json',model(data,label))
doc='# 战略—MVA—产品待办追溯\n\n主责 `togaf-requirements`；制品族 `architecture-backlog`，视图规范 `'+PID+'`，分析方法 `'+MID+'`。本实现扩展既有族，不把同一故事在不同待办中的出现计为新制品。\n\n## 决策与输入\n\n产品负责人、架构负责人和开发团队判断：本次MVA为何纳入这些故事、有哪些护栏及依赖、证据是否足以交付。必要输入为原始战略/需求、负责人明确排序、项目层次规则、MVA边界、ABB/SBB设计和验收证据。缺来源/断链拒绝通过；缺运行观察保持pending-evidence。\n\n## 方法\n\n'+'\n'.join(f'{i+1}. {s}' for i,s in enumerate(steps))+'\n\n## 语义与输出\n\n五维语境分别保留；本例全为target状态，同时包含strategic/segment/capability全景层级以及conceptual/logical/physical抽象。批准candidate和实现not-started单独记录。core ABB/SBB与realizes不被扩展覆盖。项目采用的epic/feature/story细化不是所有TOGAF项目的强制结构。MVA不是MVP。\n\n|关系|方向及含义|\n|---|---|\n'+'\n'.join(f"|`{k}`|{v['meaning']}|" for k,v in DEFINITIONS.items())+'\n|`realizes`|SBB → ABB；本例为候选设计，不能视为已部署|\n\n每个对象和关系都有稳定ID、属性及证据；两种布局均输出逐记录表和关系表。表示只依据已审查模型，不从行序推断依赖。分析结果输出战略路径、ABB/SBB关联、传递前置和MVA缺口；保存在JSON的事实同时可见于Markdown表。\n\n## 完整案例与修改\n\n[原料](../../examples/addenda/backlog-trace/raw-business-materials.json)按BR-1至BR-4提取初始范围；[初始模型](../../examples/addenda/backlog-trace/baseline-model.json)只纳入S-BOOK；BR-5把退款登记改为必须项并扩大同一MVA，保留历史。[修改模型](../../examples/addenda/backlog-trace/modified-model.json)纳入S-REFUND，BR-6仅使预约验收证据齐备，退款仍待验证，不应得出整体可运营。\n\n[执行及反例](../../examples/addenda/backlog-trace/execution-audit.json)检查改动、重复ID、断链、反向实现、MVA漏项、缺证据和依赖环。评审按每个story稳定ID追溯原料、护栏、实现、排序和验收；仅请求本制品时不用生成整个成果包。\n\n## 调用与来源\n\n`generate.py model.json --profile '+PID+' --layout reference|adaptive --out output`；`analyze.py model.json --evaluate A-TRACE`。模型内analysis使用来源ID，不能给不存在的来源。\n\n来源：'+'；'.join(REFS)+'。方法摘要与虚构原料随技能相对路径携带；原文用于审计，生成不依赖原工作区。该表是正文的项目操作化，未声称对应图的结构复刻；也未规定默认权重、合格线或MVA必定可运营。\n'
(ROOT/'references/capability-addenda'/f'{PID}.md').write_text(doc)
print(json.dumps({'profiles':1,'methods':1,'nodes':len(base['nodes']),'relationships':len(base['relationships'])}))
