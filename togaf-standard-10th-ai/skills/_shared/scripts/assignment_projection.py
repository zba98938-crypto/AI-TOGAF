# -*- coding: utf-8 -*-
"""Explicit task/assignment/evidence projections from bound G249 model inputs."""
from pathlib import Path
import argparse,copy,json,html,hashlib
PROFILE='architecture-work-assignment-map'
KINDS={'guide:architecture-task':'架构工作任务；职责与人员分配分别建模','guide:person-assignment':'有任务、期间、容量和证据的候选人员配置','guide:competence-evidence':'人员行为观察及其评价状态'}
def seed_subjects(model,data):
 """Create editable subjects before strict analysis binding; no competence inference."""
 es={e['id']:e for e in model['entities']};ids=[];edges=[]
 def add(row,kind,name):
  i=row['id']
  if i in es:raise ValueError('Seed projection collides with existing object: '+i)
  e={'id':i,'type':kind,'name':name,'attributes':copy.deepcopy(row),'evidence':copy.deepcopy(row.get('evidence',[])),'certainty':'assumed'};model['entities'].append(e);es[i]=e;ids.append(i)
 def link(a,b,label):
  i='work-projection.'+hashlib.sha256(json.dumps([a,b]).encode()).hexdigest()[:20]
  model['relationships'].append({'id':i,'type':'traces_to','source':a,'target':b,'label':label,'attributes':{'origin':'project-task-evidence-projection'},'evidence':copy.deepcopy(data['source_ids'][:1]),'certainty':'assumed'});edges.append(i)
 for t in data.get('tasks',[]):
  add(t,'guide:architecture-task',t.get('scope',t['id']))
  for role in t.get('role_refs',[]):link(role,t['id'],'本次任务职责；不是人事汇报')
 obs={}
 for o in data.get('assessments',[]):
  i=o['id']+'.evidence';obs[o['id']]=i;add({**o,'id':i,'observation_ref':o['id'],'current_proficiency':o.get('proficiency')},'guide:competence-evidence',o['person_ref']+'：'+o['id'])
 for a in data.get('assignments',[]):
  add(a,'guide:person-assignment',a['person_ref']+'候选配置')
  for t in a.get('task_refs',[]):link(a['id'],t,'候选承担；未批准')
  for o in a.get('assessment_refs',[])+a.get('support',{}).get('assessment_refs',[]):link(a['id'],obs[o],'配置依赖的人员/支持证据')
 model.setdefault('extensions',{}).setdefault('entity_types',{}).update(KINDS)
 return ids,edges

def prepare(model,analysis_id=None,view_id=None):
 from analyze import evaluate
 from validate import validate
 m=copy.deepcopy(model);candidates=[a for a in m.get('analyses',[]) if a.get('method')=='architecture-role-skill-assessment' or a.get('method_id')=='architecture-role-skill-assessment']
 if analysis_id:candidates=[a for a in candidates if a['id']==analysis_id]
 if len(candidates)!=1:raise ValueError('Choose exactly one architecture-role-skill-assessment using --analysis')
 a=candidates[0];data=a['inputs'];initial=evaluate(a,m);result=initial['result'];reviews={x['id']:x for x in result['assignment_reviews']}
 entities={e['id']:e for e in m['entities']};edges={r['id']:r for r in m['relationships']};ids=[];rids=[]
 def add(identity,kind,name,attrs,evidence):
  if identity in entities:
   existing=entities[identity]
   if existing['type'] not in [kind,'case:architecture-task','case:person-assignment','case:competence-evidence']:raise ValueError('Projection ID collides with unrelated model object: '+identity)
   existing['attributes'].update(copy.deepcopy(attrs))
  else:
   entities[identity]={'id':identity,'type':kind,'name':name,'attributes':copy.deepcopy(attrs),'evidence':copy.deepcopy(evidence),'certainty':'assumed'};m['entities'].append(entities[identity])
  ids.append(identity)
 def relate(source,target,meaning):
  if source not in entities or target not in entities:raise ValueError('Projection relationship endpoint absent')
  candidates=[r for r in edges.values() if r['source']==source and r['target']==target and r['type']=='traces_to']
  if len(candidates)>1:raise ValueError('Ambiguous existing projection edges: '+source+' / '+target)
  identity=candidates[0]['id'] if candidates else 'work-projection.'+hashlib.sha256(json.dumps([source,target]).encode()).hexdigest()[:20]
  if identity in edges and (edges[identity]['source']!=source or edges[identity]['target']!=target):raise ValueError('Projection relationship collision')
  if identity not in edges:
   r={'id':identity,'type':'traces_to','source':source,'target':target,'label':meaning,'attributes':{'origin':'project-task-evidence-projection'},'evidence':copy.deepcopy(data['source_ids'][:1]),'certainty':'assumed'};m['relationships'].append(r);edges[identity]=r
  rids.append(identity)
 for role in data.get('roles',[]):
  if role['id'] not in entities:raise ValueError('Role must be an explicit model object: '+role['id'])
  ids.append(role['id'])
 for task in data.get('tasks',[]):
  req=[r['id'] for r in data.get('requirements',[]) if r.get('task_ref')==task['id']]
  add(task['id'],'guide:architecture-task',task.get('scope',task['id']),{**task,'requirement_refs':req},task.get('evidence',[]))
  for rid in task.get('role_refs',[]):relate(rid,task['id'],'本次任务职责；不是人事汇报')
 observation_ids={}
 for obs in data.get('assessments',[]):
  existing=[e['id'] for e in entities.values() if e['type'] in {'guide:competence-evidence','case:competence-evidence'} and e['attributes'].get('observation_ref',e['attributes'].get('id'))==obs['id']]
  if len(existing)>1:raise ValueError('Ambiguous observation projection: '+obs['id'])
  identity=existing[0] if existing else obs['id']+'.evidence';observation_ids[obs['id']]=identity
  add(identity,'guide:competence-evidence',obs['person_ref']+'：'+obs['id'],{**obs,'current_proficiency':obs.get('proficiency')},obs.get('evidence',[]))
 for assignment in data.get('assignments',[]):
  review=reviews[assignment['id']]
  add(assignment['id'],'guide:person-assignment',assignment['person_ref']+'候选配置', {**assignment,'review_state':review['state'],'capacity_state':review['capacity_state'],'period_state':review['period_state'],'approval':'not-granted'},assignment.get('evidence',[]))
  for tid in assignment.get('task_refs',[]):relate(assignment['id'],tid,'候选承担；需责任方确认')
  obsrefs=assignment.get('assessment_refs',[])+assignment.get('support',{}).get('assessment_refs',[])
  for oid in obsrefs:
   if oid in observation_ids:relate(assignment['id'],observation_ids[oid],'配置依赖的人员/支持证据')
 m.setdefault('extensions',{}).setdefault('entity_types',{}).update(KINDS)
 view_id=view_id or a['id']+'.configuration';v={'id':view_id,'artifact_id':'architecture-role-catalog','profile_id':PROFILE,'title':'任务、角色、配置及能力证据','context':copy.deepcopy(m['project']['context']),'entity_ids':list(dict.fromkeys(ids)),'relationship_ids':list(dict.fromkeys(rids)),'analysis':'由当前绑定的任务和观察显式投影；角色、容量、期间和能力分别审查。','legend':'箭头为职责、配置或证据追溯；不表示人事汇报、熟练度达标或业务批准。','attributes':{'projection_analysis_id':a['id']}}
 old=next((i for i,x in enumerate(m['views']) if x['id']==view_id),None)
 if old is None:m['views'].append(v)
 else:m['views'][old]=v
 # Preserve strict binding after adding explicit projection objects and views.
 selected={i for t in data.get('tasks',[]) for i in t.get('model_object_refs',[])}
 data['model_objects']=[copy.deepcopy(e) for e in m['entities'] if e['id'] in selected]
 data['model_relationships']=[copy.deepcopy(r) for r in m['relationships'] if r['source'] in selected and r['target'] in selected]
 intended={i for t in data.get('tasks',[]) for i in t.get('artifact_ids',[])}
 if 'model_views' in data:data['model_views']=[copy.deepcopy(x) for x in m['views'] if x['artifact_id'] in intended]
 entities[data['model_binding']['context_ref']]['attributes']['assessment_inputs']=copy.deepcopy(data)
 errors=[x for x in validate(m) if x['level']=='error']
 if errors:raise ValueError(json.dumps(errors,ensure_ascii=False))
 return m

def projection_issues(model,view):
 if view.get('profile_id')!=PROFILE:return []
 aid=view.get('attributes',{}).get('projection_analysis_id');analyses=[a for a in model.get('analyses',[]) if a['id']==aid]
 def problem(message):return [{'level':'error','code':'assignment-projection-selection','id':view['id'],'message':message}]
 if len(analyses)!=1:return problem('Projection requires exactly one current source analysis')
 data=analyses[0]['inputs'];es={e['id']:e for e in model['entities']};expected={x['id'] for k in ['roles','tasks','assignments'] for x in data.get(k,[])};pairs=set();observations={}
 for obs in data.get('assessments',[]):
  matches=[e['id'] for e in es.values() if e['type'] in {'guide:competence-evidence','case:competence-evidence'} and e['attributes'].get('observation_ref',e['attributes'].get('id'))==obs['id']]
  if len(matches)!=1:return problem('Observation must have one explicit evidence subject: '+obs['id'])
  observations[obs['id']]=matches[0];expected.add(matches[0])
 for task in data.get('tasks',[]):pairs.update((r,task['id']) for r in task.get('role_refs',[]))
 for a in data.get('assignments',[]):
  pairs.update((a['id'],t) for t in a.get('task_refs',[]))
  for obs in a.get('assessment_refs',[])+a.get('support',{}).get('assessment_refs',[]):
   if obs in observations:pairs.add((a['id'],observations[obs]))
 if set(view['entity_ids'])!=expected:return problem('Main view must exactly cover the roles/tasks/assignments/evidence of its bound analysis')
 selected=[r for r in model['relationships'] if r['id'] in view['relationship_ids']]
 actual={(r['source'],r['target']) for r in selected if r['type']=='traces_to'}
 if actual!=pairs or len(selected)!=len(pairs):return problem('Main view must include each actual role-task and assignment-task/evidence relation exactly once')
 return []

def render_assignment(model,view,profile,layout):
 issues=projection_issues(model,view)
 if issues:raise ValueError(json.dumps(issues,ensure_ascii=False))
 from profile_render import Drawing
 es={e['id']:e for e in model['entities'] if e['id'] in view['entity_ids']};rs=[r for r in model['relationships'] if r['id'] in view['relationship_ids']]
 p=copy.deepcopy(profile);p['template']={'separate_detail_ledger':True};d=Drawing(view,p,layout);d.width=2220
 groups=[['guide:architecture-role'],['guide:architecture-task','case:architecture-task'],['guide:person-assignment','case:person-assignment'],['guide:competence-evidence','case:competence-evidence']]
 fields=[['scope','primary_responsibility'],['decision','outcome','required_skill_ids','workload_hours','work_period'],['person_ref','valid_from','valid_until','available_hours','review_state','capacity_state','period_state','approval'],['person_ref','assessment_state','current_proficiency','note']]
 for col,(kinds,attrs) in enumerate(zip(groups,fields)):
  x=30+col*555;y=215;d.text(x,158,['角色责任','任务与成果','人员配置','行为证据'][col],20)
  for e in es.values():
   if e['type'] in kinds:y+=d.card(e,x,y,470,fields=[f for f in attrs if f in e['attributes']])+65
 for r in rs:d.edge(r,es)
 d.edge_register=rs
 svg,report=d.finish(list(es.values()),rs);report.update(projection_contract='generic-assignment-projection/1',business_approval='not-granted');return svg,report

def markdown(model,view):
 es={e['id']:e for e in model['entities']};rs={r['id']:r for r in model['relationships']}
 lines=['# '+view['title'],'','当前模型中的任务、角色、配置及能力证据。配置为候选；未知不默认转换为最低等级。','',view['analysis'],'','|ID|名称|完整属性|','|---|---|---|']
 for identity in view['entity_ids']:
  e=es[identity];attrs=json.dumps(e['attributes'],ensure_ascii=False).replace('|','\\|');lines+=['|'+identity+'|'+e['name']+'|'+attrs+'|']
 lines+=['','|关系ID|起点|含义|终点|','|---|---|---|---|']
 for identity in view['relationship_ids']:
  r=rs[identity];lines+=['|'+identity+'|'+r['source']+'|'+r['label']+'|'+r['target']+'|']
 lines+=['','!['+view['title']+']('+view['id']+'.svg)','','独立图片：['+view['id']+'.png]('+view['id']+'.png)。可编辑源：[SVG]('+view['id']+'.svg) · [Mermaid]('+view['id']+'.mmd)','','图例：'+view['legend'],'']
 return '\n'.join(lines)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('model');p.add_argument('--out',required=True);p.add_argument('--analysis');p.add_argument('--view');a=p.parse_args();m=prepare(json.loads(Path(a.model).read_text()),a.analysis,a.view);out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'out':str(out),'projection_views':[v['id'] for v in m['views'] if v.get('profile_id')==PROFILE]},ensure_ascii=False))
if __name__=='__main__':main()
