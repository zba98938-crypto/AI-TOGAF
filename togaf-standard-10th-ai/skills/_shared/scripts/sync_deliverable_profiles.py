"""Refresh registry facts and explicit section bindings; never change selection scope."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    cap=json.loads((ROOT/'capabilities.json').read_text());path=ROOT/'capability-addenda/deliverable-assembly-rules.json';rules=json.loads(path.read_text())
    profiles={p['id']:p for p in cap['profiles']};deliverables={d['id']:d for d in rules['deliverables']}
    rules['default_profiles']=cap['default_profiles'].copy()
    for pid,p in profiles.items():
        prior=rules['profile_metadata'].get(pid,{})
        rules['profile_metadata'][pid]={**prior,'version':p.get('version','2.0'),'template_id':p.get('template',{}).get('id',pid),
          'template_version':p.get('template',{}).get('version',p.get('version','2.0')),'required_attributes':p.get('required_attributes',{}),
          'relationship_requirements':p.get('required_relationship_attributes',prior.get('relationship_requirements',{})),
          'required_identity_fields':p.get('required_identity_fields',prior.get('required_identity_fields',{})),'source_refs':p.get('source_refs',[])}
    count=0
    for spec in sorted((ROOT/'capability-addenda').glob('deliverable-bindings-*.json')):
        for pid,entries in json.loads(spec.read_text())['mappings'].items():
            if pid not in profiles:raise ValueError('未登记profile：'+pid)
            for did,title,focus in entries:
                d=deliverables[did];section=next(s for s in d['sections'] if s['title']==title)
                group_id='optional-'+did+'-'+pid
                group=next((g for g in d['conditional_groups'] if g['id']==group_id),None)
                if group is None:
                    group={'id':group_id,'profile_ids':[pid],'artifact_ids':[],'section_titles':[],'content_focus':[],
                     'applicability':'仅项目显式选择该视图或声明该条件组时适用','activation':'selected-explicit-profile-or-assembly.active_groups'}
                    d['conditional_groups'].append(group)
                for key,value in [('section_titles',title),('content_focus',focus)]:
                    if value not in group[key]:group[key].append(value)
                count+=1
    path.write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'profile_metadata':len(profiles),'explicit_section_bindings':count,'deliverables':len(deliverables)}))
if __name__=='__main__':main()
