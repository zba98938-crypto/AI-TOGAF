# -*- coding: utf-8 -*-
"""Observable semantic checks, not an automatic maturity or business analyst.

CLI: python methods.py model.json --profile PROFILE
"""
import argparse,json
from cases import CASES,load
CONFIG={c['id']:c for c in CASES}
TABLES={'bi-business-function-coverage':'bi-business-functions','bi-application-function-coverage':'bi-application-functions','mdm-business-function-coverage':'mdm-business-functions','mdm-application-function-coverage':'mdm-application-functions'}
def issues(profile,model):
 c=CONFIG[profile];errors=[];selected=next(v for v in model['views']if v['profile_id']==profile);entities=[e for e in model['entities']if e['id']in selected['entity_ids']]
 def fail(code,id,message):errors.append({'code':code,'object_id':id,'message':message})
 for e in entities:
  a=e.get('attributes',{});id=e['id']
  for f in c['fields']:
   if f not in a:fail('missing-required-attribute',id+':'+f,'必需字段缺失')
  if profile=='msa-readiness-evidence':
   if a.get('scoring',{}).get('scheme')!='none'or a.get('scoring',{}).get('score')is not None:fail('unsourced-maturity-score',id,'本例没有OSIMM规则；不得合成分数')
   if not a.get('action')or not a.get('owner'):fail('unowned-readiness-gap',id,'就绪判断需有责任和行动')
  elif profile=='msa-federated-governance-process':
   waiver=a.get('waiver',{})
   if waiver.get('status')=='approved'and(waiver.get('approver')!='架构评审委员会'or waiver.get('decision_evidence')in ['',None,'unknown','none']):fail('unauthorized-waiver',id,'豁免批准须委员会和实际决定证据')
   if not a.get('feedback'):fail('governance-process-missing',id,'治理不能只有静态要求，需反馈过程')
  elif profile=='msa-value-resource-evidence':
   for category in ['development_resources','operations_resources']:
    resource=a.get(category,{})
    for status in ['allocated','planned']:
     cell=resource.get(status,{})
     if not {'value','unit','period'}<=set(cell):fail('resource-dimensions-missing',id+':'+category+':'+status,'资源需值/单位/期间，未知值可null')
     elif cell['unit']not in ['person-day','person-hour']or not cell['period']:fail('resource-unit-or-period',id,'本例仅明确人日/人时；其他单位须补项目定义')
   cr=a.get('cost_and_return',{})
   if cr.get('ROI')!='not-calculated；无项目财务规则':fail('unsourced-ROI',id,'本例无财务规则不得计算ROI')
   if '='in cr.get('cost',''):fail('incompatible-resource-total',id,'不得无换算规则合并异单位/期间/状态资源')
  elif profile=='bi-usage-goal-measures':
   metric=a.get('metric',{})
   if not all(metric.get(k) for k in ['unit','period','rule','basis']):fail('metric-definition-incomplete',id,'指标需单位/时段/规则/依据')
   if 'TOGAF规定'in metric.get('basis','')or'参考方向就是'in metric.get('rule',''):fail('reference-direction-as-target',id,'来源表只给方向，项目目标需项目依据')
   if a.get('goal_reference',{}).get('id')not in {x['id']for x in load('bi-goals')['rows']}:fail('unknown-goal-reference',id,'目标必须指明实际参考条目')
  elif profile in TABLES:
   status=a.get('coverage_status')
   if status not in ['evidenced-in-example','planned','unknown','out-of-scope-with-reason']:fail('invalid-coverage-status',id,'状态必须区分未知/计划/有证据/范围外')
   if status=='evidenced-in-example'and(a.get('implementation_ref')in [None,'','unknown','none']or not a.get('evidence_detail')):fail('false-function-coverage',id,'参考名称不是实际覆盖证据')
   if status=='out-of-scope-with-reason'and not a.get('gap_action'):fail('unjustified-scope-exclusion',id,'范围外需具体理由及复评条件')
   if not a.get('reference_identity','').startswith('reference-only'):fail('reference-as-deployment',id,'参考模型身份不得替换为实际部署')
  elif profile=='bi-value-chain-controls':
   if a.get('layer_kind')=='raw'and'不更改源内容'not in a.get('transformation_rule',''):fail('raw-source-overwritten',id,'本例原始空间必须保留源内容')
   if not a.get('metadata_lineage')or not a.get('quality_controls')or not a.get('protection_controls'):fail('chain-controls-missing',id,'价值链各层需血缘、质量与保护')
  elif profile=='bi-model-operating-monitoring':
   measure=a.get('measure',{})
   if 'TOGAF'in measure.get('basis','')or('通过'in a.get('claim','')and'无通过'not in a['claim']and'无实际'not in a['claim']):fail('unsourced-model-pass',id,'无来源不得规定准确率/阈值/通过结论')
   if not all(measure.get(k)for k in ['unit','window','definition','basis']):fail('monitor-definition-incomplete',id,'观测需要单位/时间窗口/定义/依据')
   if not a.get('response',{}).get('fallback'):fail('model-fallback-missing',id,'运营模型需失败处置和回退')
 if profile in TABLES:
  reference=load(TABLES[profile])['rows'];ids=[e['attributes'].get('reference_id')for e in entities]
  if len(ids)!=len(set(ids))or set(ids)!={r['id']for r in reference}:fail('reference-row-coverage',profile,'源表行缺失/重复/额外条目；不能声称完整参考覆盖')
  byid={r['id']:r for r in reference}
  for e in entities:
   a=e['attributes'];r=byid.get(a.get('reference_id'))
   if r and(a.get('reference_name')!=r['name']or a.get('reference_definition')!=r['definition']or a.get('reference_group')!=r['group']or a.get('reference_level')!=r.get('level','child-in-source-group')or a.get('reference_scope')!=r.get('group_scope','源表分组；无额外应用范围规则')):fail('reference-semantics-overwritten',e['id'],'参考名/定义/分组/粒度/范围不能按实现修改；修改项目覆盖字段')
 if profile=='bi-value-chain-controls':
  es={e['id']:e for e in entities}
  for r in model['relationships']:
   if r['id']in selected['relationship_ids']and r['source']not in es[r['target']]['attributes']['input_refs']:fail('lineage-direction-conflict',r['id'],'源向目标与目标input_refs不一致')
 if profile=='msa-federated-governance-process':
  types={r['type']for r in model['relationships']if r['id']in selected['relationship_ids']}
  if types!={'ops:governance_'+x for x in ['supports','aligns','extends','constrains']}:fail('governance-relations-conflated',profile,'本例四种治理关系需分别保留')
 return errors
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('model');p.add_argument('--profile',required=True);a=p.parse_args();result=issues(a.profile,json.load(open(a.model)));print(json.dumps({'errors':result},ensure_ascii=False,indent=2));raise SystemExit(bool(result))
