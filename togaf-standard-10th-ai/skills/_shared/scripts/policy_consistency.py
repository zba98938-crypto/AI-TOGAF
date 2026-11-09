# -*- coding: utf-8 -*-
"""Compare explicit shared-object policy projections; never invent business policy."""
import argparse,json
from pathlib import Path

def value_at(obj,path):
 for key in path:
  if not isinstance(obj,dict) or key not in obj:return False,None
  obj=obj[key]
 return True,obj

def check(model,contract):
 problems=[];es={e['id']:e for e in model.get('entities',[])};sources={s['id'] for s in model.get('sources',[])}
 def issue(code,identity,message):problems.append({'level':'error','code':code,'id':identity,'message':message})
 if contract.get('schema_version')!='shared-policy-projection/1':return [{'level':'error','code':'policy-contract-version','id':'contract','message':'Unsupported contract version'}]
 if not contract.get('source_ids') or not set(contract['source_ids'])<=sources:issue('policy-source','contract','Policy needs explicit business-material sources')
 root=es.get(contract.get('policy_object_ref'))
 if not root:return [{'level':'error','code':'policy-object','id':'contract','message':'Shared policy object absent'}]
 present,policy=value_at(root,contract.get('policy_path',[]))
 if not present or not isinstance(policy,dict):return [{'level':'error','code':'policy-missing','id':root['id'],'message':'Shared policy remains unresolved'}]
 for projection in contract.get('projections',[]):
  target=es.get(projection['entity_ref']);ok,actual=value_at(target,projection['path'])
  if not ok:issue('policy-projection-missing',projection['entity_ref'],'Projection path absent');continue
  for field in projection.get('policy_fields',[]):
   if field not in policy or not isinstance(actual,dict) or actual.get(field)!=policy[field]:issue('policy-projection-stale',projection['entity_ref'],field+' differs from explicit shared policy')
 return problems

def classify_change(before,after,object_id,contract):
 old=next((e for e in before.get('entities',[]) if e['id']==object_id),None);new=next((e for e in after.get('entities',[]) if e['id']==object_id),None)
 if old is None or new is None:raise ValueError('Both models must retain the stable object ID')
 a=value_at(old,contract['policy_path']);b=value_at(new,contract['policy_path']);semantic=a!=b
 return {'object_id':object_id,'change_type':'business-policy-change' if semantic else 'editorial-only' if old!=new else 'unchanged','required_review_object_ids':[r['entity_ref'] for r in contract['projections']] if semantic else [],'projection_issues':check(after,contract),'approval':'not-inferred'}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('model');p.add_argument('--contract',required=True);p.add_argument('--before');p.add_argument('--out',required=True);a=p.parse_args();m=json.loads(Path(a.model).read_text());c=json.loads(Path(a.contract).read_text());r={'issues':check(m,c),'notice_zh':'仅验证明确声明的政策字段一致；不从名称或自然语言推断业务已接受。'}
 if a.before:r['change']=classify_change(json.loads(Path(a.before).read_text()),m,c['policy_object_ref'],c)
 r['passed']=not r['issues'];Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'passed':r['passed'],'issues':len(r['issues'])}));return int(not r['passed'])
if __name__=='__main__':raise SystemExit(main())
