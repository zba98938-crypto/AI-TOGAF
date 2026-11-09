"""Keep every actual view identity when aggregating profile coverage.

A profile may occur in multiple scopes/states. Presence of one output does not
satisfy all selected views, and a draft coverage record is not a clean result.
"""
from collections import Counter
from pathlib import Path
import json


def generation_evidence(profile_ids, manifests, stale, model, root):
    root=Path(root);profile_ids=set(profile_ids)
    expected_views={v['id']:v for v in model.get('views',[]) if v.get('profile_id') in profile_ids}
    expected={vid:v['profile_id'] for vid,v in expected_views.items()}
    records=[];gaps=[]
    for layout,manifest in manifests.items():
        entries=[e for e in manifest.get('artifacts',[]) if e.get('profile_id') in profile_ids]
        counts=Counter(e.get('view_id') for e in entries)
        actual={e.get('view_id'):e.get('profile_id') for e in entries}
        for vid in sorted(expected):
            if actual.get(vid)!=expected[vid]:gaps.append({'layout':layout,'view_id':vid,'code':'expected-view-missing-or-wrong-profile'})
        for vid in sorted(set(actual)-set(expected)):
            gaps.append({'layout':layout,'view_id':vid,'code':'view-not-in-selected-model'})
        for vid,count in counts.items():
            if count>1:gaps.append({'layout':layout,'view_id':vid,'code':'duplicate-actual-view-id'})
        for entry in entries:
            output=root/'examples/full-capability'/layout
            missing=[]
            required=['path','json','coverage']+(['svg','png'] if entry.get('output_kind','diagram')!='table' else [])
            for field in required:
                path=entry.get(field)
                if not path or not (output/path).is_file():missing.append(field)
            coverage={}
            if entry.get('coverage') and (output/entry['coverage']).is_file():
                try:coverage=json.loads((output/entry['coverage']).read_text())
                except (ValueError,OSError):missing.append('readable-coverage')
            if not isinstance(coverage,dict):coverage={};missing.append('coverage-object-required')
            vid=entry.get('view_id');selected=expected_views.get(vid,{})
            required_coverage=['view_id','profile_id','artifact_id','errors','represented_entity_ids','represented_relationship_ids']
            if any(k not in coverage for k in required_coverage):missing.append('coverage-identity-and-representation-fields')
            if any(coverage.get(k)!=entry.get(k) for k in ['view_id','profile_id']) or coverage.get('artifact_id')!=entry.get('id'):
                missing.append('coverage-identity-matches-manifest')
            for group in ['entity','relationship']:
                actual_ids=coverage.get('represented_'+group+'_ids',[])
                if not isinstance(actual_ids,list) or not all(isinstance(x,str) for x in actual_ids):
                    actual_ids=[];missing.append('represented-'+group+'-ids-array-required')
                if set(actual_ids)!=set(selected.get(group+'_ids',[])):missing.append('represented-'+group+'-selection-matches-model')
            if entry.get('json') and (output/entry['json']).is_file():
                try:
                    payload=json.loads((output/entry['json']).read_text());payload_view=payload.get('view',{})
                    if payload_view.get('id')!=vid or payload_view.get('profile_id')!=entry.get('profile_id'):missing.append('payload-view-identity')
                    for group in ['entity','relationship']:
                        ids=payload_view.get(group+'_ids',[])
                        if not isinstance(ids,list) or not all(isinstance(x,str) for x in ids):
                            ids=[];missing.append('payload-'+group+'-ids-array-required')
                        if set(ids)!=set(selected.get(group+'_ids',[])):missing.append('payload-'+group+'-selection-matches-model')
                except (ValueError,OSError,AttributeError):missing.append('readable-view-payload')
            issues=coverage.get('errors',[])
            if not isinstance(issues,list):issues=[];missing.append('coverage-errors-array-required')
            omitted=[]
            for key in ['unrepresented_entity_ids','unrepresented_relationship_ids']:
                ids=coverage.get(key,[])
                if not isinstance(ids,list) or not all(isinstance(x,str) for x in ids):missing.append(key+'-array-required')
                else:omitted+=ids
            if missing or issues or omitted or entry.get('status')!='generated-awaiting-review':
                gaps.append({'layout':layout,'view_id':entry.get('view_id'),'code':'output-missing-or-draft',
                  'missing_outputs':missing,'expression_errors':issues,'omitted_ids':omitted,'status':entry.get('status')})
            records.append({'layout':layout,'profile_id':entry.get('profile_id'),'view_id':entry.get('view_id'),
              'evidence':'examples/full-capability/'+layout+'/'+entry.get('json','missing-json'),
              'stale_inputs':stale.get(layout,[]),'generation_status':entry.get('status')})
    if records and any(r['stale_inputs'] for r in records):status='stale-output-requires-regeneration'
    elif expected and profile_ids.issubset(set(expected.values())) and records and not gaps and set(manifests)=={'reference','adaptive'}:status='both-layouts-generated-current'
    else:status='pending-or-partial'
    return {'status':status,'evidence':records,'expected_view_ids':sorted(expected),'gaps':gaps,
      'limit':'逐实际view_id核对，不将同规范多个范围/状态压缩为一项；当前输出不代表视觉或业务通过。'}


def deliverable_evidence(identity, manifests, stale, model, root):
    expected={d['id'] for d in model.get('deliverables',[]) if d['deliverable_id']==identity}
    records=[];gaps=[];unbound=[]
    for layout,manifest in manifests.items():
        entries=[d for d in manifest.get('deliverables',[]) if d.get('id')==identity]
        counts=Counter(e.get('instance_id') for e in entries)
        if set(counts)!=expected:gaps.append({'layout':layout,'code':'deliverable-instance-set-mismatch','expected':sorted(expected),'actual':sorted(counts)})
        if any(c>1 for c in counts.values()):gaps.append({'layout':layout,'code':'duplicate-deliverable-instance'})
        for entry in entries:
            folder=Path(root)/'examples/full-capability'/layout
            if not all(entry.get(k) and (folder/entry[k]).is_file() for k in ['path','json']):
                gaps.append({'layout':layout,'code':'deliverable-file-missing','instance_id':entry.get('instance_id')});continue
            try:
                payload=json.loads((folder/entry['json']).read_text());assembly=payload.get('assembly') or {}
                if not isinstance(assembly,dict):raise ValueError('assembly-must-be-object')
            except (ValueError,OSError,AttributeError):
                gaps.append({'layout':layout,'code':'deliverable-payload-unreadable','instance_id':entry.get('instance_id')});continue
            saved_deliverable=payload.get('deliverable')
            if not isinstance(saved_deliverable,dict):saved_deliverable={}
            if saved_deliverable.get('id')!=entry.get('instance_id') or payload.get('contract_id')!=identity:
                gaps.append({'layout':layout,'code':'deliverable-payload-identity-mismatch','instance_id':entry.get('instance_id')})
            if assembly.get('status')!='assembled-awaiting-review' or assembly.get('gaps'):
                gaps.append({'layout':layout,'code':'deliverable-assembly-not-clean','instance_id':entry.get('instance_id')})
            content=assembly.get('content_status');titles=assembly.get('unbound_section_titles',[])
            if content!='all-sections-bound-business-review-pending':
                unbound.append({'layout':layout,'instance_id':entry.get('instance_id'),'titles':titles,'content_status':content})
            records.append({'layout':layout,'instance_id':entry.get('instance_id'),
               'evidence':'examples/full-capability/'+layout+'/'+entry['json'],'content_status':content,'unbound_section_titles':titles})
    if records and any(stale.values()):status='stale-output-requires-regeneration'
    elif expected and not gaps and set(manifests)=={'reference','adaptive'}:
        status='assembled-with-unbound-sections-current' if unbound else 'assembled-current-business-review-pending'
    else:status='pending-or-partial'
    return {'status':status,'evidence':records,'gaps':gaps,'unbound_sections':unbound,
      'limit':'组装当前性、章节证据绑定及业务完整性分别处理；同类多个交付实例不互相覆盖。'}
