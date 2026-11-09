"""Aggregate actual evidence by source and capability, with conservative status gates."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REV=ROOT/'reviews';WORK=ROOT.parents[1]
def read(p,default=None):return json.loads(p.read_text()) if p.exists() else default
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def relative(p):return str(p.relative_to(ROOT))
def canonical_sha(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def current_manifest(manifest):
    from runtime_provenance import fingerprints
    expected={'capabilities_sha256':ROOT/'capabilities.json','renderer_sha256':ROOT/'scripts/profile_render.py',
      'generator_sha256':ROOT/'scripts/generate.py','table_renderer_sha256':ROOT/'scripts/table_expression.py','metamodel_sha256':ROOT/'metamodel.json',
      'artifacts_sha256':ROOT/'artifacts.json','deliverables_sha256':ROOT/'deliverables.json',
      'assembly_renderer_sha256':ROOT/'scripts/deliverable_assembly.py','assembly_rules_sha256':ROOT/'capability-addenda/deliverable-assembly-rules.json'}
    stale=[key for key,path in expected.items() if manifest.get(key)!=sha(path)]
    if manifest.get('implementation_dependencies_sha256')!=fingerprints(ROOT):stale.append('implementation_dependencies_sha256')
    if manifest.get('model_sha256')!=canonical_sha(read(ROOT/'tests/full-example.json')):stale.append('model_sha256')
    return stale

def method_case_status(index, identity, root=ROOT):
    """Route located cases without turning paths or old run labels into passes."""
    from evidence_integrity import verify_reference
    item=next((m for m in index.get('methods',[]) if m.get('method_id')==identity),None)
    if not item:return None
    roles=item.get('evidence',{});stale=[];integrity=[];current_roles={}
    for records in roles.values():
        for record in records:
            errors=verify_reference(record,root,{'method_id':identity})
            if errors:
                stale.append(record.get('path','invalid-reference'))
                integrity.extend(errors)
    for role,records in roles.items():
        current_roles[role]=bool(records) and all(
            not verify_reference(record,root,{'method_id':identity}) for record in records)
    registry=root/'capabilities.json'
    if not registry.is_file() or index.get('registry_sha256')!=sha(registry):stale.append('capabilities.json')
    required=['raw','steps','result','modification','counterexample']
    complete=all(roles.get(role) for role in required)
    return {'status':'case-index-stale-recheck-required' if stale else 'worked-case-linked; content-and-domain-acceptance-separate' if complete else 'partial-case-links',
      'evidence':['reviews/method-case-index.json#'+identity],
      'roles':roles,'stale_evidence_paths':sorted(set(stale)),
      'integrity_errors':sorted(set(integrity)),'current_roles':current_roles,
      'bounded_cross_review_status':'linked-review-scope-only' if roles.get('cross_review') and not stale else 'not-currently-linked-or-stale',
      'saved_execution_status':'located-not-currently-reverified' if roles.get('execution') else 'written-exercise-no-separate-run-record-located',
      'limit':'可达案例和历史运行记录不是当前执行、业务评审或定义核实通过。'}

def main():
    evidence=read(ROOT/'evidence-registry.json');cap=read(ROOT/'capabilities.json');arts=read(ROOT/'artifacts.json')['artifacts'];ds=read(ROOT/'deliverables.json')['deliverables']
    known={x['id'] for x in arts+ds+cap['work_products']+cap['profiles']+cap['analysis_methods']}
    resolutions={r.get('candidate_id',r.get('id')):r for r in cap.get('candidate_resolutions',[])}
    resolutions.update(read(REV/'candidate-resolutions.json',{}))
    def destinations_for(ids):
        resolved=[];unknown=[]
        for identity in ids:
            if identity in known:resolved.append(identity);continue
            canonical=identity.removeprefix('new:')
            if canonical in known:resolved.append(canonical);continue
            r=resolutions.get(identity,{})
            mapped=r.get('work_product_ids',[])+r.get('profile_ids',[])+r.get('method_ids',[])
            if mapped and all(x in known for x in mapped):resolved.extend(mapped)
            else:unknown.append(identity)
        return list(dict.fromkeys(resolved)),unknown
    guides=[];source_records=[];all_candidates=[]
    for guide in evidence['guides']:
        gid=guide.get('id',guide.get('guide')) or guide['path'][:4];path=next((WORK/'togaf-standard-10th-zh').glob(gid+'*.md'));total=len(path.read_text().splitlines())
        notes=[];covered=set();sections={};tables={};issues=[];refs=[]
        for p in sorted((REV/'full-text-reading'/gid).glob('part-*.json')):
            d=read(p);span=d.get('zh_lines_read',[])
            if len(span)==2 and all(isinstance(x,int) for x in span):covered.update(range(span[0],span[1]+1))
            refs.append(relative(p));notes.append((p,d))
        p=REV/'full-text-reading-v3'/(gid+'.json')
        if p.exists():
            d=read(p)
            if d.get('source_sha256')!=sha(path):issues.append({'type':'source-hash-changed','evidence':relative(p)})
            else:
                for a,b in d.get('read_ranges',[]):covered.update(range(a,b+1))
            refs.append(relative(p));notes.append((p,d))
        for p,d in notes:
            for s in d.get('sections',[]):
                identity=s.get('id',str(s.get('lines')));sections[identity]={**s,'reading_evidence':relative(p)}
            for t in d.get('tables',[]):
                identity=t.get('id',str(t.get('lines')));tables[identity]={**t,'reading_evidence':relative(p)}
            issues.extend(d.get('issues',[]))
            for c in d.get('new_capability_candidates',d.get('new_candidates',[])):
                item={'candidate_id':c} if isinstance(c,str) else dict(c)
                item['source_review']=relative(p);item['guide']=gid;all_candidates.append(item)
        covered=covered&set(range(1,total+1));missing=sorted(set(range(1,total+1))-covered)
        unresolved=[]
        for record_type,entries in [('section',sections),('table',tables)]:
            for s in entries.values():
                destinations=s.get('capability_refs',[])
                resolved,unknown=destinations_for(destinations)
                if unknown:unresolved.append({'source_id':s.get('id'),'record_type':record_type,'refs':unknown})
                source_records.append({'guide':gid,'source_id':s.get('id'),'record_type':record_type,'disposition':s.get('disposition'),
                  'capability_refs':destinations,'resolved_capability_refs':resolved,'candidate_or_unresolved_refs':unknown,'summary':s.get('summary_zh'),
                  'lines':s.get('lines'),'rows':s.get('rows'),'content_sha256':s.get('content_sha256'),
                  'bilingual_check':s.get('bilingual_check'),'evidence':s['reading_evidence'],'status':'read-disposition-recorded; operational-acceptance-separate'})
        guides.append({'guide':gid,'source_sha256':sha(path),'total_lines':total,'read_lines':len(covered),'missing_line_count':len(missing),
          'status':'full-local-text-reading-recorded' if not missing else 'partial-local-text-reading',
          'evidence':refs,'sections':len(sections),'tables':len(tables),'unresolved_destinations':unresolved,'issues':issues,
          'limit':'逐行阅读记录、章节/表处理不证明英文逐字段定义、原图忠实或能力验收；历史记录与本轮记录按来源分别保留。'})
    for p in [REV/'full-text-reading-v3/capability-candidates.json',REV/'full-text-reading-v3/additional-capability-candidates.json']:
        for c in read(p,{}).get('candidates',[]):all_candidates.append({**c,'source_review':relative(p)})
    merged={}
    for c in all_candidates:
        identity=c.get('candidate_id',c.get('id',c.get('name')))
        if not identity:identity='unnamed-'+str(len(merged))
        merged.setdefault(identity,{'id':identity,'observations':[]})['observations'].append(c)
    for c in merged.values():
        c['registered_identity_match']=c['id'] in known
        c['resolution']=resolutions.get(c['id'])
        c['status']=c['resolution'].get('status','explicit-resolution-recorded') if c['resolution'] else 'registered-related; acceptance-pending' if c['id'] in known else 'explicit-capability-gap-or-extension-review'
    for f in evidence['figures']:
        source_records.append({'source_id':f['id'],'record_type':'figure-json-and-assets','disposition':f.get('disposition'),
          'reason':f.get('disposition_reason'),'profile_ids':f.get('profile_ids',[]),'evidence':'evidence-registry.json#'+f['id'],
          'semantic_status':f.get('current_semantic_review'),'source_conflicts':[c for c in evidence.get('source_conflicts',[]) if c.get('figure_id')==f['id']]})
    source_status=read(REV/'source-audit-status.json',{})
    counts={'guides':len(guides),'fully_read_local_guides':sum(g['missing_line_count']==0 for g in guides),
      'figure_json_records':len(evidence['figures']),'source_image_assets':len(evidence.get('image_assets',[])),
      'assets_with_visual_record':source_status.get('counts',{}).get('local_assets_with_some_actual_visual_record'),
      'unrenderable_assets':source_status.get('counts',{}).get('local_assets_without_visual_record'),
      'source_section_records':sum(g['sections'] for g in guides),'source_table_records':sum(g['tables'] for g in guides),
      'candidate_ids':len(merged)}
    save(REV/'source-coverage-unified.json',{'date':'2026-11-01','counts':counts,'guides':guides,'source_entries':source_records,'candidates':list(merged.values()),
      'notice':'source-coverage-unified合并full-text-reading与full-text-reading-v3。旧source-audit-status的7/2/17仅针对前一个目录，不能读为最终全量状态。'})
    manifests={layout:read(ROOT/'examples/full-capability'/layout/'manifest.json',{}) for layout in ['reference','adaptive']}
    stale={layout:current_manifest(manifest) for layout,manifest in manifests.items()}
    from coverage_evidence import generation_evidence,deliverable_evidence
    from acceptance_gate import evaluate_acceptance
    from runtime_provenance import fingerprints
    model_data=read(ROOT/'tests/full-example.json')
    current_fingerprints={**fingerprints(ROOT),**{name:sha(ROOT/name) for name in ['capabilities.json','artifacts.json','deliverables.json','metamodel.json']}}
    valid=read(ROOT/'tests/full-example-validation.json',{});valid_ok=not any(i.get('level')=='error' for i in valid.get('issues',[])) and bool(valid.get('examples')) and valid.get('capabilities_sha256')==sha(ROOT/'capabilities.json') and valid.get('model_sha256')==canonical_sha(read(ROOT/'tests/full-example.json'))
    profiles={p['id']:p for p in cap['profiles']};visual=read(REV/'output-visual-v4.json',{});visual_byid={x['profile_id']:x for x in visual.get('profiles',[])}
    cases={}
    for audit in sorted((ROOT/'examples/addenda').glob('**/execution-audit.json')):
        for case in read(audit,{}).get('cases',[]):
            pid=case.get('profile_id',case.get('id'))
            if pid in profiles:cases.setdefault(pid,[]).append({'evidence':relative(audit),'case_id':pid,'status':case.get('status'),
                'baseline': 'baseline' in case,'modified':'modified' in case,'counterexample':case.get('counterexample')})
    acceptance=read(REV/'capability-acceptance.json',{}).get('capabilities',[])
    accepted_byid={(a['category'],a['id']):a for a in acceptance}
    status=[]
    method_index=read(REV/'method-case-index.json',{})
    replay_index=read(REV/'method-current-replay-index.json',{})
    from method_replay_evidence import replay_status
    section_index=read(REV/'section-case-index.json',{})
    section_stale=[r['path'] for r in section_index.get('evidence',[]) if not (ROOT/r['path']).is_file() or sha(ROOT/r['path'])!=r.get('sha256')]
    if section_index and section_index.get('registry_sha256')!=sha(ROOT/'capabilities.json'):section_stale.append('capabilities.json')
    if section_index and section_index.get('runtime_fingerprints')!=fingerprints(ROOT):section_stale.append('runtime-fingerprints')
    for kind,items in [('artifact-family',arts+cap['work_products']),('guide-work-product',cap['work_products']),('view-template',[p for p in cap['profiles'] if not p.get('alias_of')]),('analysis-method',cap['analysis_methods']),('deliverable',ds)]:
        for item in items:
            identity=item['id'];pids=[identity] if kind=='view-template' else [p['id'] for p in cap['profiles'] if p['artifact_id']==identity]
            generation=generation_evidence(pids,manifests,stale,model_data,ROOT)
            source_refs=item.get('source_refs',item.get('sources',[]))
            definition={'status':'source-located-official-definition-verification-incomplete','evidence':source_refs}
            model={'status':'example-validated' if valid_ok and pids else 'not-applicable-or-pending','evidence':['tests/full-example-validation.json'] if valid_ok and pids else []}
            analysis={'status':'method-specified','evidence':['references/'+('analysis-methods' if kind=='analysis-method' else 'capabilities' if identity in {w['id'] for w in cap['work_products']} else 'profiles' if kind=='view-template' else 'deliverables' if kind=='deliverable' else 'artifacts')+'/'+identity+'.md']}
            case=ROOT/'examples/method-cases'/(identity+'.md')
            if case.exists():analysis={'status':'worked-case-recorded','evidence':[relative(case)]}
            if kind=='analysis-method':
                analysis=method_case_status(method_index,identity) or analysis
                analysis['current_execution_replay']=replay_status(replay_index,identity,ROOT,fingerprints(ROOT))
            if kind=='deliverable':
                generation=deliverable_evidence(identity,manifests,stale,model_data,ROOT)
            if kind=='analysis-method':generation={'status':'see-worked-method-result','evidence':analysis['evidence']}
            vis={'status':'not-applicable-table' if pids and all(profiles[pid].get('output_kind')=='table' for pid in pids) else 'pending-profile-field-review','evidence':[]}
            if identity in visual_byid:vis={'status':visual_byid[identity]['status'],'evidence':['reviews/output-visual-v4.json#'+identity]}
            actual_cases=[c for pid in pids for c in cases.get(pid,[])]
            modification={'status':'executed-baseline-modification-counterexample' if actual_cases and all(c['baseline'] and c['modified'] and (c.get('counterexample') or {}).get('rejected') for c in actual_cases) else 'general-engineering-cases-exist; per-capability-review-pending','evidence':actual_cases}
            review={'status':'independent-business-and-source-review-incomplete','evidence':[]}
            if kind=='analysis-method':
                indexed=next((m for m in method_index.get('methods',[]) if m['method_id']==identity),{})
                routes=indexed.get('qualitative_execution_routes',[])
                stale_case=bool(analysis.get('stale_evidence_paths'))
                if routes:
                    model={'status':'qualitative-case-models-linked; validation-records-separate' if not stale_case else 'case-evidence-stale',
                      'evidence':[r[k] for r in routes for k in ['baseline_model','modified_model']]}
                    modification={'status':'qualitative-modification-and-counterexample-recorded' if not stale_case else 'case-evidence-stale',
                      'evidence':analysis.get('roles',{}).get('modification',[])+analysis.get('roles',{}).get('counterexample',[])}
                cross=analysis.get('roles',{}).get('cross_review',[])
                if cross:review={'status':'bounded-cross-agent-semantic-review-linked; official-and-business-approval-separate' if not stale_case else 'case-evidence-stale',
                  'evidence':cross}
            entry={'category':kind,'id':identity,'name':item.get('name_zh',item.get('name',identity)),'owner':item.get('owner'),
              'definition':definition,'model':model,'analysis':analysis,'generation':generation,
              'modification':modification,
              'review':review,'visual':vis,'accepted':False,
               'visual_applicable':True if kind=='deliverable' else False if kind=='analysis-method' else not (pids and all(profiles[pid].get('output_kind')=='table' for pid in pids)),
              'visual_review_kind':'document-layout' if kind=='deliverable' else 'source-structure-equivalence',
              'limit':'登记及工程执行可使用，但所有必要维度通过之前不计逐项完整验收通过。'}
            if kind=='analysis-method' and identity=='change-profile-governance-review':
                bound=read(REV/'change-profile-bound-author.json',{})
                bound_stale=[name for name,digest in bound.get('hashes',{}).items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
                if bound:
                    entry['supplemental_bound_case']={'status':'case-evidence-stale' if bound_stale else 'bounded-model-snapshot-check-recorded-with-operability-gaps',
                      'stale_paths':bound_stale,'evidence':['reviews/change-profile-bound-author.json','reviews/change-profile-bound-independent.json'],
                      'scope':'Two 59-row candidate snapshots and exact selected view union; optional project binding, not standard-mandated schema.',
                      'limits':['57 unreviewed, 1 limited fictional pass, 1 deferred per version','2 transition-operability-gap warnings retained','Original direct-only and old execution indexes are not rewritten','No business approval, complete official definition or visual acceptance'],
                      'accepted':False}
            if kind=='analysis-method' and identity=='mdm-match-merge-arbitration-method':
                semantic=read(REV/'mdm-arbitration-execution.json',{})
                if semantic:
                    evidence_hashes={**semantic.get('inputs_sha256',{}),**semantic.get('assets_sha256',{})}
                    semantic_stale=[name for name,digest in evidence_hashes.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
                    if not semantic.get('inputs_sha256'):semantic_stale.append('missing-input-fingerprints')
                    if not semantic.get('assets_sha256'):semantic_stale.append('missing-output-fingerprints')
                    if semantic.get('runtime_fingerprints')!=fingerprints(ROOT):semantic_stale.append('runtime-fingerprints')
                    if semantic.get('registry_sha256')!=sha(ROOT/'capabilities.json'):semantic_stale.append('capabilities.json')
                    entry['supplemental_qualitative_case']={'status':'case-evidence-stale' if semantic_stale else 'authored-qualitative-candidate-case-with-scoped-execution',
                      'stale_paths':semantic_stale,'accepted':False,
                      'evidence':['reviews/mdm-arbitration-execution.json','reviews/mdm-arbitration-independent.json'],
                      'scope':'New fictional conflict records and two-stage authored judgments; structural provenance and per-object saved-field checks only.',
                      'limits':['Natural-language wrong claims require manual review, not CLI rejection','No actual merge/unmerge, address oracle or consumer recovery','Source interpretation and project rules stay distinct','Historical indexes and seven-dimensional gates remain unchanged']}
            if kind=='analysis-method' and identity in {'bi-usage-goal-measures-method','bi-model-operating-monitoring-method'}:
                bi=read(REV/'bi-measurement-execution.json',{})
                if bi:
                    hashes={**bi.get('inputs_sha256',{}),**bi.get('assets_sha256',{})}
                    bi_stale=[name for name,digest in hashes.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
                    if not bi.get('inputs_sha256') or not bi.get('assets_sha256'):bi_stale.append('missing-fingerprint-inventory')
                    if bi.get('runtime_fingerprints')!=fingerprints(ROOT):bi_stale.append('runtime-fingerprints')
                    if bi.get('registry_sha256')!=sha(ROOT/'capabilities.json'):bi_stale.append('capabilities.json')
                    entry['supplemental_bi_measurement_case']={'status':'case-evidence-stale' if bi_stale else 'authored-candidate-and-project-shadow-arithmetic-recorded',
                      'stale_paths':bi_stale,'accepted':False,'evidence':['reviews/bi-measurement-execution.json','reviews/bi-measurement-independent.json'],
                      'scope':'Two fictional BI uses, two versions; project sample arithmetic and exact saved-field expression.',
                      'limits':['Paired sample medians are not accuracy percentages or causal improvement','Unreviewed production adoption stays unknown, not zero','Technical restart is not business resolution or deployment approval','Manual claim review is separate from numeric/structural tests','Historical evidence and seven-dimensional gates are not upgraded']}
            if kind=='view-template' and identity=='capability-decomposition':
                hierarchy_case=read(REV/'capability-source-structure-execution.json',{})
                if hierarchy_case:
                    hashes=hierarchy_case.get('input_and_output_sha256',{})
                    stale_structure=[name for name,digest in hashes.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
                    if not hashes:stale_structure.append('missing-fingerprint-inventory')
                    if hierarchy_case.get('runtime_fingerprints')!=fingerprints(ROOT):stale_structure.append('runtime-fingerprints')
                    entry['supplemental_source_structure_case']={'status':'case-evidence-stale' if stale_structure else 'reference-interpretation-geometry-recorded-source-conflict-open',
                      'stale_paths':stale_structure,'accepted':False,'visual_review_performed':False,
                      'evidence':['reviews/capability-source-structure-execution.json','reviews/capability-diagram-source-audit.json','reviews/capability-diagram-render-audit.json'],
                      'scope':'G211/fig3-3 portable interpretation: 12 capabilities and 11 inferred parent edges, two layouts.',
                      'limits':['Chinese redraw SVG and portable interpretation conflict remains','Inferred decomposition is not a source physical arrow or enterprise fact','Geometry/XML checks are not visual or official-definition acceptance']}
            if kind=='deliverable':
                supplementary=[r for r in section_index.get('sections',[]) if r['deliverable_id']==identity]
                if supplementary:entry['supplemental_chapter_cases']={'status':'case-evidence-stale' if section_stale else 'bounded-project-partial-demonstration-recorded',
                  'sections':supplementary,'stale_paths':section_stale,'evidence':'reviews/section-case-index.json',
                  'limit':'仅独立项目章节附录；不满足本全量示例、其他项目或完整交付物的内容缺口。'}
            # Integrity/scope checks validate attestations, not reviewer truthfulness.
            gate=accepted_byid.get((kind,identity),{})
            entry['acceptance_gates']=gate.get('dimensions',{})
            entry['acceptance_evaluation']=evaluate_acceptance(entry,gate,ROOT,current_fingerprints)
            entry['accepted']=entry['acceptance_evaluation']['accepted'] and not any(stale.values())
            status.append(entry)
    registered={'artifact_families':len(arts)+len(cap['work_products']),'legacy_artifact_ids':len(arts),'guide_work_products':len(cap['work_products']),
      'view_templates':sum(not p.get('alias_of') for p in cap['profiles']),'registered_profile_entries':len(cap['profiles']),'compatibility_aliases':sum(bool(p.get('alias_of')) for p in cap['profiles']),'guide_profiles':sum(p.get('registration_class')!='legacy-default' and not p.get('alias_of') for p in cap['profiles']),
      'legacy_default_profiles':sum(p.get('registration_class')=='legacy-default' for p in cap['profiles']),
      'graphical_profiles':sum(p.get('output_kind','diagram')!='table' and not p.get('alias_of') for p in cap['profiles']),
      'table_profiles':sum(p.get('output_kind')=='table' and not p.get('alias_of') for p in cap['profiles']),'analysis_methods':len(cap['analysis_methods']),'deliverables':len(ds)}
    from audit_source_integrity import audit as audit_source_integrity
    source_ledger=audit_source_integrity(ROOT)
    save(REV/'source-integrity-ledger.json',source_ledger)
    source_integrity={'status':'mechanical-inventory-only','summary':source_ledger['summary'],
      'evidence':'reviews/source-integrity-ledger.json','accepted':False,
      'limit':'Source byte/projection equality and route resolution are not official/semantic/visual acceptance; originals may be unavailable in a portable copy.'}
    categories={'artifact_families':'artifact-family','guide_work_products':'guide-work-product','view_templates':'view-template','analysis_methods':'analysis-method','deliverables':'deliverable'}
    from datetime import datetime
    from zoneinfo import ZoneInfo
    dimensions=('definition','model','analysis','generation','modification','review','visual')
    dimension_pass_counts={key:{dimension:sum(x['category']==category and x['acceptance_evaluation']['dimensions'][dimension]['status']=='passed' for x in status)
        for dimension in dimensions} for key,category in categories.items()}
    priority=read(REV/'source-priority-recheck-followup-2026-11-03.json',{})
    routes=read(REV/'figure-route-dispositions-followup-2026-11-03.json',{})
    page_audit=read(REV/'deliverable-page-review/page-audit.json',{})
    chapter_audit=read(ROOT/'examples/xinghe-synthetic/deliverable-case-audit.json',{})
    method_assessment=read(REV/'method-acceptance-assessment-2026-11-03.json',{})
    save(REV/'capability-status.json',{'date':datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat(),'registered_counts':registered,'fully_accepted_counts':{k:sum(x['accepted'] and x['category']==v for x in status) for k,v in categories.items()},'dimension_pass_counts':dimension_pass_counts,'stale_generation_inputs':stale,
      'scoped_execution_evidence':{
        'source_priority_recheck':{'evidence':'reviews/source-priority-recheck-followup-2026-11-03.json','counts':priority.get('counts',{}),'accepted':False},
        'figure_route_dispositions':{'evidence':'reviews/figure-route-dispositions-followup-2026-11-03.json','counts':routes.get('counts',{}),'accepted':False},
        'method_assessment':{'evidence':'reviews/method-acceptance-assessment-2026-11-03.json','summary':method_assessment.get('summary',{}),'accepted':False},
        'xinghe_chapter_binding':{'evidence':'examples/xinghe-synthetic/deliverable-case-audit.json','acceptance':chapter_audit.get('acceptance',{}),'business_review_status':'pending'},
        'document_page_audit':{'evidence':'reviews/deliverable-page-review/page-audit.json','documents':page_audit.get('documents'),'pages':page_audit.get('pages'),'machine_problem_documents':page_audit.get('problem_documents'),'actual_all_page_visual_review':False}},
      'counting_rule':'五种登记量分别列示；工作产品作为可生成制品族也计入family总量，不能将五列相加。legacy-default只是旧入口规范化，不是新增指南定义。',
      'source_integrity':source_integrity,'capabilities':status,'notice':'保守逐项状态：工程样例通过不自动变成定义、分析、修改、评审或视觉的业务验收。'} )
    print(json.dumps({'sources':counts,'registered':registered},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
