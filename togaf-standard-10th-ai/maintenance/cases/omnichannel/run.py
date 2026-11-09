# -*- coding: utf-8 -*-
"""Local corpus-only execution of a fictional cross-guide case; never business approval."""
from pathlib import Path
import sys,os,json,copy,hashlib
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;C=HERE.parents[2];ROOT=C.parent
sys.path.insert(0,str(C/'maintenance'))
from publish import guard
sys.addaudithook(guard)
sys.path.insert(0,str(HERE));import base_build as base
import assignment_expression
# Rendering uses the directory-local general assignment profile.
TMP=HERE/'tmp';TMP.mkdir(exist_ok=True)
for k in ['TMPDIR','TMP','TEMP']:os.environ[k]=str(TMP)
def dump(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def canonical(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def build(changed=False,rename=False):
 m=base.domain_model(changed)
 note=next(e for e in m['entities'] if e['id']=='DELIVERY-NOTE')['attributes']
 m['relationships'].append(base.edge('WP-ONLINE-CAP','traces_to','WP-ONLINE','CAP-RESERVE','工作包拟改变库存预占实例；承诺规则未决'))
 if changed:
  note['controls']=[{'id':'CTRL-LOCAL-DURABILITY','risk_id':'RISK-STOCK','statement':'候选：门店记录持久成功后答复受理；故障丢失窗口、保留与加密政策待验证','applies_to':'APP-STORE / LOCAL-ORDER-RECORD','owner_status':'门店数据与运营责任待确认','status':'candidate'}, {'id':'CTRL-CENTRAL-REPLAY','risk_id':'RISK-STOCK','statement':'候选：中央按事件标识去重并逐笔对账，保留冲突和恢复检查点；接收不等于库存承诺','applies_to':'APP-STOCK / IF-RECOVERY / CENTRAL-ORDER-RECORD','owner_status':'库存、订单与恢复对账责任待确认','status':'candidate'}]
  m['gaps'].append({'id':'GAP-ASSIGNMENT-PERIOD','description':'ASSIGN-A只覆盖至2026-11-30，离线工作包候选结束2026-12-04；后半段配置未确定','impact':'不能认定完整交付期有人员覆盖；工时与专家支持也未证明充分','needed_input':'续任/替代人员、可用容量和工作量'} )
  m['relationships'] += [base.edge('WP-OFFLINE-CAP','traces_to','WP-OFFLINE','CAP-RESERVE','断连约束要求复核库存能力实现'),base.edge('CHANGE-DECISIONS','traces_to','REQ-OFFLINE','DELIVERY-NOTE','新增约束触发决策议程与运营条件复核'),base.edge('CHANGE-ROLE','traces_to','REQ-OFFLINE','ROLE-SOL','新增恢复设计改变解决方案任务要求'),base.edge('CHANGE-DEVELOPMENT','traces_to','REQ-OFFLINE','DEV-A','新增行为要求触发发展计划及复评标准复核，不自动提高评价')]
 m['gaps'].append({'id':'GAP-EXPERT-LEVEL','description':'原教学输入称专家4级但现有行为证据不足，当前等级保持未评价','impact':'不能仅凭专家头衔确认支持能力','needed_input':'任务相关的广泛经验、实际应用与评审证据'} )
 if rename:
  obj=next(e for e in m['entities'] if e['id']=='CAP-RESERVE');obj['name']='库存预占（共享对象变更验证）';obj['attributes']['definition']='变更验证：按已确认业务政策协调可售库存；政策本身仍待业务确认'
 from assignment_projection import prepare
 return prepare(base.attach_role_assessment(m),view_id='role-assignment')
def projections(m):
 es={e['id']:e for e in m['entities']};rs=m['relationships'];caps=[e for e in es.values() if e['type']=='capability'];entries=[]
 for cap in caps:
  interfaces=[r['target'] for r in rs if r['source']==cap['id'] and es[r['target']]['type']=='interface']
  applications=sorted({r['source'] for r in rs if r['type']=='exposes' and r['target'] in interfaces})
  work=[r['source'] for r in rs if r['target']==cap['id'] and es[r['source']]['type']=='work_package']
  entries.append({'capability_id':cap['id'],'name':cap['name'],'definition':cap['attributes']['definition'],'interface_refs':interfaces,'application_refs':applications,'work_package_refs':work,**({'policy':copy.deepcopy(cap['attributes']['policy'])} if 'policy' in cap['attributes'] else {})})
 return {'content_role':'project-derived-shared-model-projections','status':'candidate-not-approved','model_sha256':canonical(m),'catalog':entries,'capability_application_matrix':[{'capability_id':e['capability_id'],'name':e['name'],'definition':e['definition'],'application_ids':e['application_refs'],'basis':'CAP-IF then exposes; only explicit modeled edges',**({'policy':e['policy']} if 'policy' in e else {})} for e in entries], 'roadmap':[{'capability_id':e['capability_id'],'name':e['name'],'definition':e['definition'],'work_package_id':w,'period':{k:es[w]['attributes'].get(k) for k in ['start','end']},'acceptance':'候选日期；实际运行、回退及生产容量仍须验证',**({'policy':e['policy']} if 'policy' in e else {})} for e in entries for w in e['work_package_refs']]}
def write_projections(dest,m):
 p=projections(m);dump(dest/'shared-object-projections.json',p)
 text=['# 共享对象目录、矩阵与路线图','', '虚构案例；以下均从同一model.json的稳定ID读取，候选日期与映射不表示已实现或已批准。','', '|能力ID|名称与定义|应用矩阵映射|关联工作包|','|---|---|---|---|']
 for e in p['catalog']:text.append('|'+ '|'.join([e['capability_id'],e['name']+'：'+e['definition'],', '.join(e['application_refs']) or '未建立映射',', '.join(e['work_package_refs']) or '未建立映射'])+'|')
 text+=['','|工作包|能力ID/名称|候选期间|条件|','|---|---|---|---|']
 for e in p['roadmap']:text.append('|'+ '|'.join([e['work_package_id'],e['capability_id']+' / '+e['name'],e['period']['start']+' — '+e['period']['end'],e['acceptance']])+'|')
 (dest/'shared-object-projections.md').write_text('\n'.join(text)+'\n')
def main():
 result={};models={}
 for name,changed,rename in [('baseline',False,False),('offline-change',True,False),('shared-object-change',True,True)]:
  m=build(changed,rename);models[name]=m;dest=HERE/'generated'/name
  issues=base.validate(m);assert not [i for i in issues if i['level']=='error'],issues
  manifest=base.generate(m,dest,all_items=True,render=True,strict=True)
  assessment=base.evaluate(m['analyses'][0],m);dump(dest/'role-assessment.json',assessment);write_projections(dest,m)
  result[name]={'model_sha256':canonical(m),'views':len(m['views']),'entities':len(m['entities']),'relationships':len(m['relationships']),'validation_findings':issues,'rendered':True,'business_approval':'not-granted','assessment_gap_count':len(assessment['result']['gaps'])}
 dump(HERE/'generated/change-impact.json',base.impact(models['offline-change'],['REQ-OFFLINE'],max_depth=len(models['offline-change']['entities'])))
 dump(HERE/'generated/summary.json',result)
 dump(HERE/'generated/execution-provenance.json',{'runner_sha256':sha(Path(__file__)),'local_builder_sha256':sha(HERE/'base_build.py'),'local_assignment_expression_sha256':sha(HERE/'assignment_expression.py'),'raw_business_materials_sha256':sha(HERE/'raw-business-materials.md'),'local_inputs_sha256':sha(HERE/'role-skill-inputs.json'),'write_boundary':str(C),'network':'not-used','limits':['候选方案与判断为明确编写的教学分析，不是从任意文本自动规划的证明。','真实业务与人员专业批准均未授予；渲染与完整性通过不改变这一状态。']})
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
