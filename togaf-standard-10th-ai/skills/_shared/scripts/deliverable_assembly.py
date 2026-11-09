"""Assemble selected model facts into deliverable sections with explicit gaps.

Assembly is opt-in for v2. It never expands a profile selector into every view
in the model; only instance references and explicit section bindings are read.
It returns data and Markdown blocks for the generator, without writing files.
"""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RULES_PATH=ROOT/'capability-addenda/deliverable-assembly-rules.json'

def load_rules(path=None):
    return json.loads(Path(path or RULES_PATH).read_text())

def _unique(values):return list(dict.fromkeys(values))
def _refs(value):return [v for v in value if isinstance(v,str) and v.strip()] if isinstance(value,list) else []
def _json(value):return json.dumps(value,ensure_ascii=False,sort_keys=True)
def _sha(value):return hashlib.sha256(_json(value).encode()).hexdigest()
def _cell(value):
    return (value if isinstance(value,str) else _json(value)).replace('|','\\|').replace('\n','<br>')
def _table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(_cell(v) for v in row)+' |\n' for row in rows)

def dependency_closure(model,deliverable_instance):
    """Exact per-instance view/analysis closure; no registry-wide selection."""
    config=deliverable_instance.get('assembly',{})
    bindings=config.get('section_bindings',{})
    view_ids=_unique(deliverable_instance.get('view_ids',[])+[v for b in bindings.values() for v in b.get('view_ids',[])])
    views={v['id']:v for v in model.get('views',[])}
    analysis_ids=_unique(config.get('analysis_ids',[])+[a for b in bindings.values() for a in b.get('analysis_ids',[])]+
                         [a for vid in view_ids for a in views.get(vid,{}).get('attributes',{}).get('analysis_ids',[])])
    entity_ids=_unique(deliverable_instance.get('entity_ids',[])+[e for b in bindings.values() for e in b.get('entity_ids',[])])
    # Only selected chapter records may introduce semantic supports. Never scan
    # every record in the model or recursively expand arbitrary inventory links.
    entities={e['id']:e for e in model.get('entities',[])}
    records=[entities[eid] for eid in entity_ids if eid in entities and entities[eid].get('type')=='project:section_evidence'
             and entities[eid].get('attributes',{}).get('record_contract')=='scenario-section/2']
    entity_ids=_unique(entity_ids+[ref for e in records for ref in _refs(e['attributes'].get('model_refs'))])
    analysis_ids=_unique(analysis_ids+[ref for e in records for ref in _refs(e['attributes'].get('analysis_refs'))])
    relationship_ids=_unique([ref for e in records for ref in _refs(e['attributes'].get('relationship_refs'))])
    return {'required_view_ids':view_ids,'required_analysis_ids':analysis_ids,'direct_entity_ids':entity_ids,
            'required_relationship_ids':relationship_ids}

def assemble(model,deliverable_instance,contract,rules=None):
    """Return section_blocks, dependency IDs, gaps and assembly status.

    strict returns ``blocked`` when inputs are missing; draft preserves the same
    gaps and returns ``draft-with-gaps``. Neither status denotes business review,
    approval or implementation. Callers must not publish a blocked assembly.
    """
    d=deliverable_instance;config=d.get('assembly');closure=dependency_closure(model,d)
    result={**closure,'section_blocks':[],'gaps':[],'status':'legacy-unassembled','analysis_results':[]}
    if not config:return result
    rules=rules or load_rules();mode=config.get('mode','strict');gaps=result['gaps']
    def gap(code,identity,message,needed=None):
        item={'id':d['id']+':'+code+':'+str(identity),'code':code,'object_id':identity,'deliverable_id':d['id'],
              'severity':'blocking','message':message,'needed_input':needed or message}
        if item not in gaps:gaps.append(item)
    if model.get('schema_version')!='2.0':gap('assembly-version',d['id'],'结构化组装仅用于v2；v1保持兼容路径。')
    if config.get('rules_version')!=rules.get('rules_version'):gap('assembly-rules-version',d['id'],'声明的规则版本与可用规则不匹配。')
    if mode not in ['strict','draft']:gap('assembly-mode',d['id'],'mode必须是strict或draft。')
    rule=next((x for x in rules.get('deliverables',[]) if x['id']==contract['id']),None)
    if not rule:
        gap('assembly-contract',contract['id'],'交付物没有组装规则。');result['status']='blocked' if mode=='strict' else 'draft-with-gaps';return result
    views={v['id']:v for v in model.get('views',[])};entities={e['id']:e for e in model.get('entities',[])}
    relations={r['id']:r for r in model.get('relationships',[])};analyses={a['id']:a for a in model.get('analyses',[])}
    sources={s['id']:s for s in model.get('sources',[])}
    semantic_delivery=any(entities.get(eid,{}).get('attributes',{}).get('record_contract')=='scenario-section/2'
                          for eid in closure['direct_entity_ids'])
    scales={s['id']:s for s in model.get('scales',[])}
    known_scopes={s['id'] for s in model.get('scopes',[])};known_states={s['id'] for s in model.get('states',[])}
    checked_measurements=set();measurement_findings=[]
    def measurement_sources(entity):
        used=[]
        for measurement in entity.get('measurements',[]):
            used+=measurement.get('evidence',[])+measurement.get('method_evidence',[])
            scale=scales.get(measurement.get('scale_id'))
            if scale:used+=scale.get('evidence',[])
        return used
    def check_measurements(entity):
        if entity['id'] in checked_measurements:return
        checked_measurements.add(entity['id'])
        for ordinal,m in enumerate(entity.get('measurements',[])):
            identity=entity['id']+'.measurements['+str(ordinal)+']'
            observed=m.get('value') is not None
            measurement_findings.append({'object_id':identity,'dimension':m.get('dimension'),
              'status':'declared-value-awaiting-business-review' if observed else 'unknown-value-not-observed',
              'value':m.get('value'),'unit':m.get('unit'),'scale_id':m.get('scale_id')})
            if observed:
                if not m.get('evidence'):gap('assembly-measurement-evidence',identity,'已声明度量值缺少观察/输入来源；仅实体来源不能代替度量依据。')
                if not isinstance(m.get('period'),str) or not m['period'].strip():gap('assembly-measurement-period',identity,'已声明度量值须有观察时间或统计期间。')
                if not any(isinstance(m.get(k),str) and m[k].strip() for k in ['method','calculation_basis']):gap('assembly-measurement-basis',identity,'已声明度量值须有测量方法或计算依据；不自动推断公式。')
            for field in ['evidence','method_evidence']:
                for sid in m.get(field,[]):
                    if sid not in sources:gap('assembly-measurement-source',identity+'.'+field+'.'+sid,'度量/规则依据ID不存在：'+sid)
            if m.get('scale_id'):
                scale=scales.get(m['scale_id'])
                if not scale:gap('assembly-measurement-scale',identity,'度量引用的量表不存在：'+m['scale_id'])
                else:
                    if not scale.get('evidence'):gap('assembly-measurement-scale-evidence',identity,'所选量表缺少来源依据。')
                    for sid in scale.get('evidence',[]):
                        if sid not in sources:gap('assembly-measurement-scale-source',identity+'.'+sid,'量表依据ID不存在：'+sid)
                    if scale.get('unit') and m.get('unit')!=scale['unit']:gap('assembly-measurement-scale-unit',identity,'度量单位与所选量表不一致。')
                    if observed and (type(m['value']) is bool or not any(type(a['value']) is not bool and m['value']==a['value'] for a in scale.get('anchors',[]))):
                        gap('assembly-measurement-scale-value',identity,'度量值不属于所选量表的显式锚点，不自动换算。')
    if config.get('scope_id') and config['scope_id'] not in known_scopes:gap('assembly-scope-missing',config['scope_id'],'交付物声明的范围ID不存在。')
    for sid in config.get('state_ids',[]):
        if sid not in known_states:gap('assembly-state-missing',sid,'交付物声明的命名状态ID不存在。')
    def profile(v):return v.get('profile_id') or rules.get('default_profiles',{}).get(v['artifact_id'],'compat-'+v['artifact_id'])
    def matches(v,selector,family_alternatives=False):
        # Once a section names profiles, a different view of the same family
        # must not satisfy it (e.g. target review versus implementation review).
        if selector.get('profile_ids') and not family_alternatives:return profile(v) in selector['profile_ids']
        return v.get('artifact_id') in selector.get('artifact_ids',[]) or profile(v) in selector.get('profile_ids',[])
    selected=[]
    for vid in closure['required_view_ids']:
        if vid not in views:gap('assembly-view-missing',vid,'所选视图ID不存在。');continue
        v=views[vid];selected.append(v)
        if not v.get('entity_ids') and not v.get('relationship_ids'):gap('assembly-empty-view',vid,'空视图不能证明必要内容已提供。')
        if config.get('scope_id') and v.get('scope_id')!=config['scope_id']:gap('assembly-scope',vid,'所选视图未声明或不属于交付物指定范围。')
        if config.get('state_ids'):
            state_ids=set(v.get('state_ids',[]))|({v['state_id']} if v.get('state_id') else set())
            if not state_ids or not state_ids<=set(config['state_ids']):gap('assembly-state',vid,'所选视图未声明或超出交付物命名状态。')
        for eid in v.get('entity_ids',[]):
            if eid not in entities:gap('assembly-entity-missing',eid,'视图引用了不存在的对象。')
            else:
                entity=entities[eid];check_measurements(entity);metadata=rules.get('profile_metadata',{}).get(profile(v),{})
                if not entity.get('evidence'):gap('assembly-entity-evidence',eid,'所选对象没有依据；不能据此完成严格交付组装。')
                required=metadata.get('required_attributes',{})
                required=required.get(entity['type'],[])+required.get('*',[]) if isinstance(required,dict) else required
                for field in required:
                    value=entity.get('name') if field=='name' else entity.get('attributes',{}).get(field)
                    if value is None or value=='':gap('assembly-required-attribute',eid+'.'+field,'所选规范必要属性缺失：'+profile(v))
                for field in metadata.get('required_identity_fields',{}).get(entity['type'],[]):
                    if not entity.get(field):gap('assembly-required-identity',eid+'.'+field,'所选规范必要身份字段缺失：'+profile(v))
                if config.get('scope_id') and entity.get('scope_id') and entity['scope_id']!=config['scope_id']:gap('assembly-entity-scope',eid,'视图内对象属于另一个范围。')
                if config.get('state_ids') and entity.get('state_id') and entity['state_id'] not in config['state_ids']:gap('assembly-entity-state',eid,'视图内对象属于所选范围之外的命名状态。')
        for rid in v.get('relationship_ids',[]):
            if rid not in relations:gap('assembly-relationship-missing',rid,'视图引用了不存在的关系。')
            else:
                relation=relations[rid];metadata=rules.get('profile_metadata',{}).get(profile(v),{})
                for endpoint in ['source','target']:
                    target=relation.get(endpoint)
                    if target not in entities:gap('assembly-relationship-endpoint-missing',rid+'.'+endpoint,'所选关系端点对象不存在：'+str(target))
                    elif target not in v.get('entity_ids',[]):gap('assembly-relationship-endpoint-unselected',rid+'.'+endpoint,'所选关系端点未列入同一具体视图；不隐式扩大实体依赖闭包：'+str(target))
                if not relation.get('evidence'):gap('assembly-relationship-evidence',rid,'所选关系没有依据。')
                for field in metadata.get('relationship_requirements',{}).get(relation['type'],[]):
                    if relation.get('attributes',{}).get(field) in [None,'']:gap('assembly-required-relation-attribute',rid+'.'+field,'所选规范必要关系属性缺失：'+profile(v))
                if config.get('scope_id') and relation.get('scope_id') and relation['scope_id']!=config['scope_id']:gap('assembly-relationship-scope',rid,'所选关系属于另一个范围。')
                if config.get('state_ids') and relation.get('state_id') and relation['state_id'] not in config['state_ids']:gap('assembly-relationship-state',rid,'所选关系属于范围外命名状态。')
    for eid in closure['direct_entity_ids']:
        if eid not in entities:gap('assembly-entity-missing',eid,'交付物直接引用对象不存在。')
        elif not any(eid in v.get('entity_ids',[]) for v in selected):
            entity=entities[eid];check_measurements(entity)
            if not entity.get('evidence'):gap('assembly-entity-evidence',eid,'直接引用对象没有依据。')
            if config.get('scope_id') and entity.get('scope_id')!=config['scope_id']:gap('assembly-direct-entity-scope',eid,'直接对象没有范围匹配的视图或对象范围声明。')
            if config.get('state_ids') and entity.get('state_id') not in config['state_ids']:gap('assembly-direct-entity-state',eid,'直接对象没有状态匹配的视图或对象状态声明。')
    tailoring={t['requirement_id']:t for t in config.get('tailoring',[]) if t.get('requirement_id')}
    if len(tailoring)!=len(config.get('tailoring',[])):gap('assembly-tailoring-duplicate',d['id'],'裁剪条目重复或缺少requirement_id，不允许静默覆盖。')
    requirement_ids={r['id'] for r in rule.get('core_requirements',[])}
    for tid,t in tailoring.items():
        if tid not in requirement_ids:gap('assembly-tailoring-unknown',tid,'裁剪项不属于本交付物核心要求。')
        if not t.get('reason') or not t.get('evidence') or not t.get('owner'):gap('assembly-tailoring-evidence',tid,'裁剪必须有理由、责任人和依据ID。')
        for sid in t.get('evidence',[]):
            if sid not in sources:gap('assembly-tailoring-source',sid,'裁剪依据不存在。')
    for req in rule.get('core_requirements',[]):
        if not any(matches(v,req,family_alternatives=True) for v in selected) and req['id'] not in tailoring:
            gap('assembly-required-view',req['id'],'缺少核心支撑：'+req.get('description',req['id']),
                {'artifact_ids':req.get('artifact_ids',[]),'profile_ids':req.get('profile_ids',[]),'action':'绑定实际view_id，或登记有依据的明确裁剪。'})
    groups={g['id']:g for g in rule.get('conditional_groups',[])}
    for gid in config.get('active_groups',[]):
        if gid not in groups:gap('assembly-group-unknown',gid,'未登记的适用组。')
        elif not any(matches(v,groups[gid]) for v in selected):gap('assembly-required-group',gid,'已声明适用组缺少明确选中的视图。',groups[gid])
    computed={}
    for aid in closure['required_analysis_ids']:
        if aid not in analyses:gap('assembly-analysis-missing',aid,'显式引用的分析ID不存在。');continue
        a=analyses[aid]
        if not a.get('evidence'):gap('assembly-analysis-evidence',aid,'分析缺少来源依据。')
        for sid in a.get('evidence',[]):
            if sid not in sources:gap('assembly-analysis-source',aid,'分析依据不存在：'+sid)
        try:
            from analyze import evaluate
            computed[aid]=evaluate(a,model)
            computed[aid]['input_sha256']=_sha(a);computed[aid]['evidence']=a.get('evidence',[])
        except (ValueError,KeyError,TypeError,ZeroDivisionError) as error:
            gap('assembly-analysis-unavailable',aid,'所选分析未形成可执行结果：'+str(error))
    result['analysis_results']=[computed[a] for a in closure['required_analysis_ids'] if a in computed]
    section_rules={s['title']:s for s in rule.get('sections',[])}
    titles=[s['title'] for s in contract['sections']];bindings=config.get('section_bindings',{})
    for title in bindings:
        if title not in titles:gap('assembly-section-unknown',title,'显式绑定的章节不属于本交付物。')
    assigned_views=set();assigned_analyses=set();assigned_entities=set()
    blocks=[]
    for section in contract['sections']:
        title=section['title'];sr=section_rules.get(title,{})
        selected_ids=[v['id'] for v in selected if matches(v,sr)]
        for g in groups.values():
            if title in g.get('section_titles',[]):selected_ids.extend(v['id'] for v in selected if matches(v,g))
        b=bindings.get(title,{})
        # Explicit view IDs are scoped selections, not permission to bypass a
        # section's project selector without a recorded tailoring decision.
        has_selector=bool(sr.get('profile_ids') or sr.get('artifact_ids'))
        mismatched=[vid for vid in b.get('view_ids',[]) if vid in views and has_selector and vid not in selected_ids]
        entity_mismatches=[eid for eid in b.get('entity_ids',[]) if eid in entities and sr.get('entity_types') and entities[eid]['type'] not in sr['entity_types']]
        if mismatched or entity_mismatches or 'override' in b:
            override=b.get('override',{})
            if not all(isinstance(override.get(k),str) and override[k].strip() for k in ['reason','owner']) or not override.get('evidence'):
                gap('assembly-section-selector',title,'显式绑定不匹配章节项目选择器或override记录不完整，须提供理由、责任人及有效来源依据。',{'view_ids':mismatched,'entity_ids':entity_mismatches})
            for sid in override.get('evidence',[]):
                if sid not in sources:gap('assembly-section-override-source',sid,'章节override依据不存在。')
        selected_ids=_unique(selected_ids+b.get('view_ids',[]))
        vids=[vid for vid in selected_ids if vid in views and vid in closure['required_view_ids']]
        aids=_unique(b.get('analysis_ids',[])+[a for vid in vids for a in views[vid].get('attributes',{}).get('analysis_ids',[])])
        # Only instance-wide entity_ids may apply across sections. References
        # from another chapter's binding remain scoped to that chapter.
        direct=_unique(b.get('entity_ids',[])+[eid for eid in d.get('entity_ids',[]) if eid in entities and entities[eid]['type'] in sr.get('entity_types',[])])
        records=[entities[eid] for eid in direct if eid in entities and entities[eid].get('type')=='project:section_evidence'
                 and entities[eid].get('attributes',{}).get('record_contract')=='scenario-section/2']
        direct=_unique(direct+[ref for e in records for ref in _refs(e['attributes'].get('model_refs'))])
        aids=_unique(aids+[ref for e in records for ref in _refs(e['attributes'].get('analysis_refs'))])
        from section_evidence import check_section_record, PLACEHOLDER
        context=d.get('sections',{}).get(title,'')
        if isinstance(context,str) and PLACEHOLDER.search(context):
            gap('assembly-section-placeholder',title,'占位正文不能作为章节叙述或证据；须补充针对性问题与论证。')
        for eid in direct:
            if eid in entities:
                for issue in check_section_record(entities[eid],d,title,sources,model=model):gap(issue['code'],issue['object_id'],issue['message'])
        block={'title':title,'context':d.get('sections',{}).get(title,''),'view_ids':vids,'analysis_ids':aids,'direct_entity_ids':direct,'content_focus':sr.get('content_focus',[])}
        project_records=[entities[eid] for eid in direct if eid in entities and entities[eid]['type']=='project:section_evidence']
        if semantic_delivery and not any(e.get('attributes',{}).get('record_contract')=='scenario-section/2' for e in project_records):
            gap('assembly-section-record-missing',title,'本情景交付章节缺少针对性证据记录；其他章节或通用视图不代替本章推理。')
        if project_records:
            block['project_record_findings']=[{'id':e['id'],'unknowns':e['attributes'].get('unknowns',[]),
              'content_status':'unresolved-inputs-business-review-pending' if e['attributes'].get('unknowns') else 'declared-no-unknowns-business-review-pending'} for e in project_records]
        if b.get('override'):block['binding_override']=b['override']
        blocks.append(block);assigned_views.update(vids);assigned_analyses.update(aids);assigned_entities.update(direct)
    # Preserve explicitly selected facts even where no special section selector
    # exists. They are named supplemental evidence, never silently discarded.
    if blocks:
        blocks[-1]['supplemental_view_ids']=[v['id'] for v in selected if v['id'] not in assigned_views]
        blocks[-1]['supplemental_analysis_ids']=[a for a in closure['required_analysis_ids'] if a not in assigned_analyses]
        blocks[-1]['supplemental_entity_ids']=[e for e in closure['direct_entity_ids'] if e not in assigned_entities]
    selected_entity_ids=set(closure['direct_entity_ids'])|{eid for v in selected for eid in v.get('entity_ids',[])}
    selected_relationship_ids={rid for v in selected for rid in v.get('relationship_ids',[])}|set(closure['required_relationship_ids'])
    for rid in closure['required_relationship_ids']:
        r=relations.get(rid)
        if not r:gap('assembly-relationship-missing',rid,'章节显式引用关系不存在。');continue
        if not {r.get('source'),r.get('target')}<=selected_entity_ids:
            gap('assembly-relationship-endpoint-unselected',rid,'章节关系端点必须在单项选择闭包内，不自动扩大选择。')
        if not r.get('evidence'):gap('assembly-relationship-evidence',rid,'章节显式关系没有依据。')
    selected_source_ids=set()
    selected_scale_ids=set()
    for eid in selected_entity_ids:
        entity=entities.get(eid,{})
        selected_source_ids.update(entity.get('evidence',[]));selected_source_ids.update(measurement_sources(entity))
        selected_scale_ids.update(m['scale_id'] for m in entity.get('measurements',[]) if m.get('scale_id'))
    for rid in selected_relationship_ids:selected_source_ids.update(relations.get(rid,{}).get('evidence',[]))
    for aid in closure['required_analysis_ids']:selected_source_ids.update(analyses.get(aid,{}).get('evidence',[]))
    for item in list(tailoring.values())+[binding.get('override',{}) for binding in bindings.values()]:selected_source_ids.update(item.get('evidence',[]))
    # Global validation also rejects duplicates. Keep standalone assembly honest
    # for its exact dependency scope, without pulling unrelated objects into it.
    from collections import Counter
    selected_by_collection={'views':set(closure['required_view_ids']),'entities':selected_entity_ids,
      'relationships':selected_relationship_ids,'analyses':set(closure['required_analysis_ids']),
      'sources':selected_source_ids,'scales':selected_scale_ids}
    for collection,identities in selected_by_collection.items():
        counts=Counter(obj['id'] for obj in model.get(collection,[]))
        for identity in sorted(identities):
            if counts[identity]>1:gap('assembly-duplicate-selected-id',collection+'.'+identity,'所选依赖身份重复，不能以字典覆盖决定采用哪个对象。')
    for item in model.get('gaps',[]):
        if set(item.get('object_ids',[]))&selected_entity_ids or (item.get('severity')=='blocking' and not item.get('object_ids')):
            gap('assembly-model-gap',item['id'],item['description'],item['needed_input'])
    def entity_table(ids):
        rows=[]
        for eid in _unique(ids):
            if eid not in entities:continue
            e=entities[eid]
            rows.append([eid,e.get('type'),e.get('name'),e.get('attributes',{}),e.get('measurements',[]),
                         {k:e[k] for k in ['concept_id','version','scope_id','state_id','context','approval_status','implementation_status'] if k in e},e.get('evidence',[]),e.get('certainty','unknown')])
        return _table(['对象ID','类型','名称','模型属性','度量（值／单位／期间／依据）','身份／状态','依据','确定性'],rows) if rows else ''
    for block in blocks:
        text='';used_sources=list(block.get('binding_override',{}).get('evidence',[]));used_entities=[];used_relations=[]
        if block['context']:text+='人工背景（独立叙述，未自动验证为模型结论）：\n\n'+block['context']+'\n\n'
        allvids=_unique(block['view_ids']+block.get('supplemental_view_ids',[]))
        for vid in allvids:
            v=views[vid];pid=profile(v);meta=rules.get('profile_metadata',{}).get(pid,{})
            text+='### 模型依据：'+v['title']+'\n\n'
            text+='[视图 `'+vid+'`](../artifacts/'+vid+'.md) · 制品 `'+v['artifact_id']+'` · 规范 `'+pid+'`\n\n'
            text+='版本与语境：`'+_json({'model_version':model['project']['version'],'profile':meta,'context':v.get('context'),
                                      'scope_id':v.get('scope_id'),'state_id':v.get('state_id'),'state_ids':v.get('state_ids',[])})+'`\n\n'
            if v.get('analysis'):text+='视图解释（仍需业务复核）：'+v['analysis']+'\n\n'
            text+=entity_table(v.get('entity_ids',[]))+'\n'
            used_entities+=v.get('entity_ids',[]);rr=[]
            for rid in v.get('relationship_ids',[]):
                if rid not in relations:continue
                r=relations[rid];used_relations.append(rid)
                rr.append([rid,r['source'],r['type'],r['target'],r.get('label',''),r.get('cardinality',{}),r.get('attributes',{}),r.get('evidence',[]),r.get('certainty','unknown')]);used_sources+=r.get('evidence',[])
            if rr:text+=_table(['关系ID','起点','语义','终点','说明','每端基数','属性','依据','确定性'],rr)+'\n'
        direct=_unique(block['direct_entity_ids']+block.get('supplemental_entity_ids',[]))
        chapter_relationships=[]
        for eid in direct:
            e=entities.get(eid,{})
            a=e.get('attributes',{})
            if e.get('type')=='project:section_evidence' and a.get('record_contract')=='scenario-section/2':
                text+='### 章节问题与推理（全虚构；scenario-authority，不是实际批准）\n\n'
                for label,field in [('问题','question'),('结论','conclusion'),('候选决策','decision'),('范围','scope'),('责任','owner'),('验收方法（未执行）','acceptance')]:
                    text+='**'+label+'**：'+str(a.get(field,''))+'\n\n'
                text+='**权衡**：'+'；'.join(_refs(a.get('tradeoffs')))+'\n\n'
                text+='**未知/待核验**：'+'；'.join(_refs(a.get('unknowns')))+'\n\n'
                text+='**必要证据缺口**：'+('；'.join(_refs(a.get('evidence_gaps'))) or '情景输入已提供；不表示真实业务已验收')+'\n\n'
                chapter_relationships+=_refs(a.get('relationship_refs'))
        rows=[]
        for rid in _unique(chapter_relationships):
            if rid not in relations:continue
            r=relations[rid];used_relations.append(rid);used_sources+=r.get('evidence',[])
            rows.append([rid,r['source'],r['type'],r['target'],r.get('label',''),r.get('evidence',[])])
        if rows:text+='### 显式跨域论证链（情景依赖，非实际因果或批准）\n\n'+_table(['关系ID','起点','语义','终点','论证','来源'],rows)+'\n'
        if direct:text+='### 直接引用的模型记录\n\n'+entity_table(direct)+'\n';used_entities+=direct
        allaids=_unique(block['analysis_ids']+block.get('supplemental_analysis_ids',[]))
        for aid in allaids:
            if aid not in computed:continue
            text+='### 分析结果 `'+aid+'`\n\n```json\n'+json.dumps(computed[aid],ensure_ascii=False,indent=2)+'\n```\n\n'
            used_sources+=analyses[aid].get('evidence',[])
        for eid in used_entities:
            if eid in entities:used_sources+=entities[eid].get('evidence',[])+measurement_sources(entities[eid])
        source_rows=[]
        for sid in _unique(used_sources):
            if sid not in sources:gap('assembly-source-missing',sid,'所选对象/关系引用的来源不存在。');continue
            s=sources[sid];source_rows.append([sid,s.get('kind'),s.get('description',''),s.get('locator','未提供定位')])
        scale_ids=_unique([m['scale_id'] for eid in used_entities if eid in entities for m in entities[eid].get('measurements',[]) if m.get('scale_id') in scales])
        if scale_ids:text+='### 所选度量量表（项目声明，未独立验收）\n\n'+_table(['量表ID','名称','单位','锚点','来源'],[[sid,scales[sid].get('name'),scales[sid].get('unit'),scales[sid].get('anchors',[]),scales[sid].get('evidence',[])] for sid in scale_ids])+'\n'
        if source_rows:text+='### 来源定位\n\n'+_table(['来源ID','种类','说明','定位'],source_rows)+'\n'
        if not allvids and not direct and not allaids:
            text+='本节尚未绑定模型记录；人工背景不计作结构化证据。\n\n'
        block.update(markdown=text,entity_ids=_unique(used_entities),relationship_ids=_unique(used_relations),source_ids=_unique(used_sources))
    # Repository metadata uses the actual selected scope/version, never an old
    # narrative literal; renderer fingerprints are added by the main manifest.
    if contract['id']=='architecture-repository' and blocks:
        rows=[[v['id'],v['artifact_id'],profile(v),model['project']['version'],rules.get('profile_metadata',{}).get(profile(v),{}),v.get('state_id',v.get('state_ids',[])),v.get('scope_id','unspecified')] for v in selected]
        blocks[0]['markdown']+='### 本次实际资产索引\n\n'+_table(['view_id','artifact_id','profile_id','模型版本','规范／模板版本','演进状态','范围'],rows)+'\n'
    result['section_coverage']=[]
    for block in blocks:
        # Supplemental evidence is retained, but cannot silently satisfy an
        # unrelated section merely because it was appended at the end.
        bound=bool(block['view_ids'] or block['analysis_ids'] or block['direct_entity_ids'])
        coverage={'title':block['title'],'status':'bound-not-business-accepted' if bound else 'narrative-only-unverified' if block['context'] else 'unbound',
          'view_ids':block['view_ids'],'analysis_ids':block['analysis_ids'],'direct_entity_ids':block['direct_entity_ids'],
          'has_narrative':bool(block['context']),'supplemental_evidence_is_not_section_acceptance':True}
        if block.get('project_record_findings'):
            coverage['project_record_findings']=block['project_record_findings']
            block['markdown']='项目章节事实的内容状态（未知不计已完成）：\n\n'+_table(['记录ID','内容状态','尚未解决输入'],
                [[r['id'],r['content_status'],r['unknowns']] for r in block['project_record_findings']])+'\n'+block['markdown']
        result['section_coverage'].append(coverage)
        if not bound:
            gap('assembly-section-unbound',block['title'],'必需章节未绑定实际模型记录；人工叙述或其他章节的补充记录不替代本章证据。')
        block['coverage_status']=coverage['status']
        block['markdown']='章节证据状态：'+coverage['status']+'（仅绑定/叙述状态，不代表内容完整或业务通过）。\n\n'+block['markdown']
        if block.get('binding_override'):
            block['markdown']='章节选择器项目override（不推断批准）：`'+_json(block['binding_override'])+'`\n\n'+block['markdown']
    result['unresolved_project_record_ids']=[r['id'] for b in blocks for r in b.get('project_record_findings',[]) if r['unknowns']]
    result['unbound_section_titles']=[c['title'] for c in result['section_coverage'] if c['status']!='bound-not-business-accepted']
    result['content_status']='sections-unbound-review-required' if result['unbound_section_titles'] else 'all-sections-bound-business-review-pending'
    result['section_blocks']=blocks
    result['applied_tailoring']=list(tailoring.values())
    if tailoring and blocks:
        blocks[-1]['markdown']+='### 明确裁剪记录（不推断批准）\n\n'+_table(['要求ID','理由','责任人','依据'],
            [[t.get('requirement_id'),t.get('reason'),t.get('owner'),t.get('evidence',[])] for t in tailoring.values()])+'\n'
    result['measurement_findings']=measurement_findings
    for block in blocks:
        findings=[finding for finding in measurement_findings if finding['object_id'].split('.measurements[')[0] in block['entity_ids']]
        if findings:block['markdown']+='### 度量声明状态（未知值不算已观察）\n\n'+_table(['记录','维度','状态','值','单位'],[[f['object_id'],f['dimension'],f['status'],f['value'],f['unit']] for f in findings])+'\n'
    result['status']=('blocked' if mode=='strict' else 'draft-with-gaps') if gaps else 'assembled-awaiting-review'
    result['assembly_provenance']={'rules_version':rules.get('rules_version'),'rules_sha256':_sha(rules),'model_sha256':_sha(model),
                                   'model_version':model['project']['version'],'mode':mode,'notice':'结构化组装与显式计算，不推断审批、签署、实现或独立业务验收。'}
    if gaps and blocks:
        blocks[-1]['markdown']+='### 组装缺口（'+result['status']+'）\n\n'+_table(['缺口ID','对象ID','说明','需要'],[[g['id'],g['object_id'],g['message'],g['needed_input']] for g in gaps])+'\n'
    return result
