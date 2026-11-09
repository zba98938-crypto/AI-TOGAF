"""Bind calculator snapshots to current model identities and source inventory."""

def _specialized_issues(model,analysis):
    findings=[];aid=analysis['id'];data=analysis.get('inputs',{})
    def issue(code,identity,message):findings.append({'level':'error','code':code,'id':aid+':'+str(identity),'message':message})
    if analysis.get('method_id')=='change-profile-checklist':
        from governance_check_binding import binding_issues as governance_binding_issues
        findings.extend(governance_binding_issues(model,analysis))
    if analysis.get('method_id')=='metadata-application-coverage-review':
        from metadata_coverage_binding import binding_issues as metadata_binding_issues
        findings.extend(metadata_binding_issues(model,analysis))
    if analysis.get('method_id')=='architecture-role-skill-assessment':
        from g249_binding import binding_issues as g249_binding_issues
        findings.extend(g249_binding_issues(model, analysis))
    if analysis.get('method_id')=='architecture-role-catalog-review':
        from g249_binding import role_binding_issues
        findings.extend(role_binding_issues(model, analysis))
    from migration_analysis import METHOD_IDS, binding_issues as migration_binding_issues
    if analysis.get('method_id') in METHOD_IDS:
        findings.extend(migration_binding_issues(model, analysis))
    if analysis.get('method_id')!='architecture-backlog-trace-review':return findings
    entities={e['id']:e for e in model.get('entities',[])};relations={r['id']:r for r in model.get('relationships',[])}
    kinds={'strategic_intent':'goal','epic':'requirement','feature':'requirement','story':'requirement','abb':'abb','sbb':'sbb','mva':'guide:mva_scope'}
    nodes=data.get('nodes',[]);edges=data.get('relationships',[])
    if not nodes:issue('analysis-binding-required','nodes','追溯分析需要非空对象快照。')
    from analysis_projection_binding import MISSING, _equal
    fields={'id','name','kind','owner','evidence'}
    for n in nodes:
        i=n.get('id');e=entities.get(i)
        if not e:issue('analysis-model-entity',i,'分析对象在主模型中不存在。');continue
        expected_type=kinds.get(n.get('kind'))
        if e['type']!=expected_type:issue('analysis-model-type',i,'分析语义种类与主模型类型不一致。')
        consumed=set(fields)
        if n.get('kind') in {'strategic_intent','epic','feature','story'}:consumed.update({'landscape','evolution'})
        if n.get('kind')=='story':consumed.update({'priority','priority_evidence','acceptance_criteria','acceptance'})
        if n.get('kind')=='mva':consumed.update({'candidate_story_ids','boundary','exclusions','decision_owner','decision_evidence'})
        for key in set(n)|consumed:
            value=n.get(key,MISSING)
            actual=(e.get(key,MISSING) if key in ['id','name','evidence'] else e.get('context',model['project']['context']).get(key,MISSING) if key in ['landscape','evolution'] else e.get('attributes',{}).get(key,MISSING))
            if not _equal(actual,value):issue('analysis-model-field-mismatch',str(i)+'.'+key,'分析输入快照与当前主模型字段不一致；重新审查并同步分析，禁止展示旧结论。')
    for r in edges:
        i=r.get('id');actual=relations.get(i)
        if not actual:issue('analysis-model-relationship',i,'分析关系在主模型中不存在。');continue
        for key in set(r)|{'id','type','source','target','evidence'}:
            if not _equal(actual.get(key,MISSING),r.get(key,MISSING)):issue('analysis-model-field-mismatch',str(i)+'.'+key,'分析关系与当前主模型不一致。')
        if actual.get('attributes',{})!=r.get('attributes',{}):issue('analysis-model-field-mismatch',str(i)+'.attributes','分析遗漏或过期的关系属性。')
    for view in model.get('views',[]):
        if aid not in view.get('attributes',{}).get('analysis_ids',[]):continue
        if set(view.get('entity_ids',[]))!={n.get('id') for n in nodes}:issue('analysis-view-entity-selection',view['id'],'该完整追溯视图的对象集合与分析快照不一致。')
        if set(view.get('relationship_ids',[]))!={r.get('id') for r in edges}:issue('analysis-view-relationship-selection',view['id'],'该完整追溯视图的关系集合与分析快照不一致。')
    return findings

def binding_issues(model, analysis):
    """Validate sources first, then the method's registered snapshot projection."""
    from analysis_evidence import evidence_issues
    from analysis_projection_binding import binding_issues as projection_issues
    findings = evidence_issues(analysis, model)
    if findings:
        return findings
    findings.extend(projection_issues(model, analysis))
    try:
        findings.extend(_specialized_issues(model, analysis))
    except (KeyError, TypeError, AttributeError, IndexError) as exc:
        findings.append({'level': 'error', 'code': 'analysis-binding-shape',
                         'id': str(analysis.get('id', 'analysis')) + ':inputs',
                         'path': 'inputs', 'message': 'Malformed binding input: ' + str(exc)})
    return findings


def require_binding(model,analysis):
    issues=binding_issues(model,analysis)
    if issues:
        import json
        raise ValueError(json.dumps(issues,ensure_ascii=False))
