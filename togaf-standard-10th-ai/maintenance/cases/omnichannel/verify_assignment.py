# -*- coding: utf-8 -*-
"""Verify generic assignment views in the three original case variants."""
from pathlib import Path
import copy,json,sys,hashlib
sys.dont_write_bytecode=True
H=Path(__file__).resolve().parent;C=H.parents[2];S=C/'skills/_shared';sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
from assignment_projection import projection_issues
from validate import validate
from analyze import evaluate
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 rows=[]
 for name in ['baseline','offline-change','shared-object-change']:
  folder=H/'generated'/name;m=read(folder/'model.json');v=next(v for v in m['views'] if v['id']=='role-assignment');coverage=read(folder/'artifacts/role-assignment.coverage.json');svg=(folder/'artifacts/role-assignment.svg').read_text()
  assert v['profile_id']=='architecture-work-assignment-map';assert not projection_issues(m,v);assert not [x for x in validate(m) if x['level']=='error'];assert len(v['entity_ids'])==11 and len(v['relationship_ids'])==7
  for rid in v['relationship_ids']:assert any(loc['kind']=='main' for loc in coverage['expression_locations']['relationships'][rid]),rid
  for eid in v['entity_ids']:assert 'data-entity-id="'+eid+'"' in svg,eid
  result=evaluate(m['analyses'][0],m)['result'];assignment=result['assignment_reviews'][0];assert assignment['capacity_state']=='unresolved' and assignment['approval']=='not-granted';assert assignment['period_state']==('covered-for-declared-task-periods' if name=='baseline' else 'not-covered');assert all(e['attributes']['current_proficiency'] is None for e in m['entities'] if e['type']=='case:competence-evidence')
  for field in ['entity_ids','relationship_ids']:
   bad=copy.deepcopy(m);next(v for v in bad['views'] if v['id']=='role-assignment')[field].pop();assert any(x['code']=='assignment-projection-selection' for x in validate(bad))
  rows.append({'variant':name,'entities':11,'main_relationships':7,'period_state':assignment['period_state'],'capacity_state':'unresolved','approval':'not-granted','semantic_gaps':len(result['gaps'])})
 report={'schema_version':'assignment-verification/2','passed':True,'rows':rows,'negative_tests':['missing-main-entity','missing-main-relationship'],'input_sha256':{('maintenance/cases/omnichannel/generated/'+x['variant']+'/model.json'):sha(H/'generated'/x['variant']/'model.json') for x in rows},'limits_zh':['校验当前通用执行契约；不替代真实人员评价或组织批准。']};(H/'generated/assignment-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print({'passed':True,'variants':len(rows),'main_relationships_each':7})
if __name__=='__main__':main()
