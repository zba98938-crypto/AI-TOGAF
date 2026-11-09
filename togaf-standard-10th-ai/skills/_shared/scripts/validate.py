#!/usr/bin/env python3
"""Validate structural and observable semantic invariants; never asserts business approval."""
import argparse
import json
from pathlib import Path
import re
import sys
from numeric_contracts import require_finite
from strict_json import load as load_json
try:
    import jsonschema
except ImportError:
    sys.exit('缺少 jsonschema；请按 skills/README.md 安装本地依赖。')
ROOT=Path(__file__).resolve().parents[1]
def load(path): return load_json(path)
ARTS={a['id']:a for a in load(ROOT/'artifacts.json')['artifacts']}
DELS={d['id']:d for d in load(ROOT/'deliverables.json')['deliverables']}
REG=load(ROOT/'relationships.json')['relationships']
NAMESPACE=re.compile(r'^[A-Za-z][A-Za-z0-9_.-]*:[A-Za-z0-9][A-Za-z0-9_.:-]*$')

def validate(model):
    issues=[]
    def issue(level,code,obj,message): issues.append({'level':level,'code':code,'id':obj,'message':message})
    try:require_finite(model,'model')
    except ValueError as exc:
        issue('error','non-finite-number','model',str(exc));return issues
    if not isinstance(model,dict):
        issue('error','schema','model','Model must be an object');return issues
    v2=model.get('schema_version')=='2.0'
    schema=ROOT/('schemas/model.schema.json' if v2 else 'schemas/model-v1.schema.json')
    for err in jsonschema.Draft202012Validator(load(schema)).iter_errors(model):
        issue('error','schema','/'.join(map(str,err.absolute_path)),err.message)
    if issues:return issues
    indexes={}
    globalids={}
    for group in ['sources','entities','relationships','views','deliverables','gaps','comparisons']+(['states','scopes','scales','analyses'] if v2 else []):
        indexes[group]={}
        for item in model.get(group,[]):
            if item['id'] in globalids:issue('error','duplicate-id',item['id'],f'标识重复，首次出现于 {globalids[item["id"]]}')
            globalids[item['id']]=group;indexes[group][item['id']]=item
    ent=indexes['entities']; rel=indexes['relationships']; sources=indexes['sources']; views=indexes['views']
    from registry import load as load_registry
    allarts,_,profiles,methods=load_registry() if v2 else (ARTS,DELS,{},[])
    meta=load(ROOT/'metamodel.json') if v2 else {}
    types=set(t for a in allarts.values() for t in a.get('entity_types',[]))|set(t for d in DELS.values() for t in d['entity_types'])|{'activity','decision','outcome','benefit','measure','gap','evidence','repository_asset','viewpoint','transition','milestone'}|set(meta.get('entity_types',{}))
    for name in model.get('extensions',{}).get('entity_types',{}):
        if name in types:issue('error','core-vocabulary-override',name,'扩展不能重定义已有核心对象类型。')
        elif v2 and not NAMESPACE.fullmatch(name):issue('error','extension-namespace',name,'新增对象类型须使用 namespace:name；v1 应通过显式迁移转换并保留名称映射。')
    types.update(model.get('extensions',{}).get('entity_types',{}))
    core={**REG,**meta.get('relationships',{})}
    ext=model.get('extensions',{}).get('relationship_types',{})
    for name in ext:
        if name in core:issue('error','core-vocabulary-override',name,'扩展不能覆盖核心关系语义。')
        elif v2 and not NAMESPACE.fullmatch(name):issue('error','extension-namespace',name,'新增关系类型须使用 namespace:name；v1 应通过显式迁移转换并保留名称映射。')
    registry={**ext,**core}
    def evolution(e):
        state=indexes.get('states',{}).get(e.get('state_id'),{})
        return state.get('evolution',e.get('evolution',e.get('context',{}).get('evolution',model['project']['context']['evolution'])))
    def refs(ids,idx,obj,kind):
        for id in ids:
            if id not in idx:issue('error','dangling-reference',obj,f'{kind} 引用不存在：{id}')
    if v2:
        for name,rule in ext.items():
            refs([t for t in rule['source_types']+rule['target_types'] if t!='*'],types,name,'扩展关系端点类型')
        for obj in [model]+list(ent.values())+list(rel.values()):
            for namespace in obj.get('extension_data',{}):
                # Arbitrary nested payloads are opaque; only extension container
                # keys are vocabulary, and the first v2 archive key is reserved.
                if namespace!='legacy_unrecognized_fields' and not NAMESPACE.fullmatch(namespace):
                    issue('error','extension-namespace',obj.get('id','model')+':'+namespace,'扩展数据使用命名空间，不能与核心语义字段混写。')
        for name in model.get('extensions',{}).get('data',{}):
            if not NAMESPACE.fullmatch(name):issue('error','extension-namespace',name,'extensions.data 的键须使用命名空间。')
    def provenance(obj):
        refs(obj.get('evidence',[]),sources,obj['id'],'来源')
        evidence=[sources[i] for i in obj.get('evidence',[]) if i in sources]
        if 'certainty' in obj and not evidence:issue('warning','missing-evidence',obj['id'],'没有来源，不能当成事实。')
        if obj.get('certainty')=='confirmed' and evidence and all(s['kind'] in ['assumption','example','figure-interpretation'] for s in evidence):
            issue('error','unsupported-confirmation',obj['id'],'只有假设、示例或图表解释，不能标为 confirmed。')
        if obj.get('decision_status') in ['approved','realized']:
            refs(obj.get('approval_evidence',[]),sources,obj['id'],'批准证据')
            approval=[sources[i] for i in obj.get('approval_evidence',[]) if i in sources]
            if not approval or all(s['kind'] in ['example','assumption','figure-interpretation'] for s in approval):
                issue('error','approval-without-evidence',obj['id'],'批准或实现状态需要实际证据来源。')
        if v2:
            refs(obj.get('approval_evidence',[]),sources,obj['id'],'批准证据')
            refs(obj.get('implementation_evidence',[]),sources,obj['id'],'实现证据')
            for field,evidence_field,states,code in [
                ('approval_status','approval_evidence',{'approved'},'approval-without-evidence'),
                ('implementation_status','implementation_evidence',{'realized','retired'},'implementation-without-evidence')]:
                if obj.get(field) in states:
                    evidence=[sources[i] for i in obj.get(evidence_field,[]) if i in sources]
                    if not evidence or all(s['kind'] in ['example','assumption','figure-interpretation'] for s in evidence):
                        issue('error',code,obj['id'],field+' 需要独立的实际证据；另一状态不构成证明。')
            if obj.get('decision_status')=='approved' and obj.get('approval_status') in ['candidate','in-review','rejected','withdrawn']:
                issue('error','legacy-status-conflict',obj['id'],'旧 approved 与独立批准状态冲突；保留历史值时应迁入带来源的扩展数据。')
            if obj.get('decision_status')=='realized' and obj.get('implementation_status') in ['not-started','in-progress']:
                issue('error','legacy-status-conflict',obj['id'],'旧 realized 与独立实现状态冲突。')
    provenance(model['project'])
    for e in ent.values():
        provenance(e)
        if e['type'] not in types:issue('error','undefined-entity-type',e['id'],e['type'])
        if e['type']=='work_package' and e['attributes'].get('duration_days',0)<0:issue('error','negative-duration',e['id'],'工期不能为负数。')
        if e.get('concept_id') and not e.get('evolution') and not e.get('context') and not e.get('state_id'):issue('warning','version-state-missing',e['id'],'有 concept_id 但未明确该版本的演进状态。')
        if v2:
            if e.get('state_id'):refs([e['state_id']],indexes['states'],e['id'],'架构状态')
            if e.get('scope_id'):refs([e['scope_id']],indexes['scopes'],e['id'],'范围')
            if e.get('state_id') in indexes['states'] and e.get('evolution') and e['evolution']!=evolution(e):issue('error','state-evolution-conflict',e['id'],'对象演进分类与命名状态不一致。')
            if e.get('context') and e['context']['evolution']!=evolution(e):issue('error','state-evolution-conflict',e['id'],'对象 context 中演进状态与对象版本或命名状态不一致。')
            named_state=indexes['states'].get(e.get('state_id'),{})
            if named_state.get('scope_id') and e.get('scope_id') and named_state['scope_id']!=e['scope_id']:issue('error','state-scope-conflict',e['id'],'对象范围与命名架构状态的范围不一致。')
            for value in e.get('measurements',[]):
                refs(value['evidence'],sources,e['id'],'度量证据')
                refs(value.get('method_evidence',[]),sources,e['id'],'计算规则证据')
                if not value['evidence']:issue('warning','measurement-evidence-gap',e['id'],'度量 '+value['dimension']+' 缺少来源证据。')
                if not value.get('period'):issue('warning','measurement-period-gap',e['id'],'度量 '+value['dimension']+' 缺少观察时间或统计期间。')
                if not value.get('method') and not value.get('calculation_basis'):issue('warning','measurement-basis-gap',e['id'],'度量 '+value['dimension']+' 缺少测量方法或计算依据；不得默认公式。')
                if value.get('scale_id'):refs([value['scale_id']],indexes['scales'],e['id'],'量表')
                scale=indexes['scales'].get(value.get('scale_id'))
                if scale and value['value'] is not None and value['value'] not in [a['value'] for a in scale['anchors']]:issue('error','scale-value',e['id'],'评价值不属于已声明的离散量表锚点。')
                if scale and scale.get('unit') and value['unit']!=scale['unit']:issue('error','scale-unit',e['id'],'度量单位与引用量表单位不一致。')
    names={}
    for e in ent.values():
        attrs=e.get('attributes') or {}
        isolation=attrs.get('integration_style') or attrs.get('comparison_alternative') or attrs.get('stage') or (attrs.get('parent_id') if e['type']=='g186:repository_node' else None)
        key=(e['type'],e['name'],e.get('state_id',evolution(e)),e.get('scope_id'),isolation)
        if key in names:issue('warning','duplicate-name',e['id'],f'与 {names[key]} 同类型同名同状态；核实边界或复用 ID。')
        names[key]=e['id']
    seen_edges=set()
    for edge in rel.values():
        provenance(edge);refs([edge['source'],edge['target']],ent,edge['id'],'端点')
        if v2:
            if edge.get('state_id'):refs([edge['state_id']],indexes['states'],edge['id'],'架构状态')
            if edge.get('scope_id'):refs([edge['scope_id']],indexes['scopes'],edge['id'],'范围')
            for endpoint in [ent.get(edge['source'],{}),ent.get(edge['target'],{})]:
                if edge.get('state_id') and endpoint.get('state_id') and edge['state_id']!=endpoint['state_id'] and edge['type']!='transitions_to':
                    issue('error','relationship-state-conflict',edge['id'],'关系与端点 '+endpoint['id']+' 属于不同命名状态。')
        rule=registry.get(edge['type'])
        if not rule:issue('error','undefined-relation',edge['id'],edge['type']);continue
        if edge['source'] not in ent or edge['target'] not in ent:continue
        for end,allowed in [('source',rule['source_types']),('target',rule['target_types'])]:
            if '*' not in allowed and ent[edge[end]]['type'] not in allowed:issue('error','relation-endpoint-type',edge['id'],f'{end} 类型 {ent[edge[end]]["type"]} 不适用于 {edge["type"]}')
        if edge['type'] in ['decomposes','transitions_to'] and ent[edge['source']]['type']!=ent[edge['target']]['type']:
            issue('error','mixed-hierarchy',edge['id'],'分解或状态转换的端点类型不一致。')
        edge_iso=(edge.get('attributes') or {}).get('integration_style') or (edge.get('attributes') or {}).get('comparison_alternative')
        key=(edge['source'],edge['target'],edge['type'],tuple(sorted(edge.get('codes',[]))),edge.get('attributes',{}).get('order'),edge.get('state_id'),edge.get('scope_id'),edge_iso)
        if edge['type']=='supports_role':
            a=edge.get('attributes',{})
            key+=(json.dumps({field:a.get(field) for field in ('assessment_kind','person_ref','observed_on','task_refs')},sort_keys=True),)
        if edge['type']=='guide:metamodel_relation':
            # Same endpoints can carry distinct source predicates (e.g. serves /
            # implemented on). Preserve both IDs; actual duplicate predicates still warn.
            a=edge.get('attributes',{})
            key+= (a.get('forward_label'),a.get('inverse_label'))
        if key in seen_edges:issue('warning','duplicate-edge',edge['id'],'关系重复，核实是否需要复用。')
        seen_edges.add(key)
        if edge['type'] in ['data_association','logical_association'] and ('cardinality' not in edge or 'unknown' in edge.get('cardinality',{}).values()):
            issue('warning','unknown-cardinality',edge['id'],'数量关系未确认；使用标注未知的关系图，不绘制确定 ER 基数。')
        if v2:
            for end,card in edge.get('cardinality',{}).items():
                if card.get('unknown'):issue('warning','unknown-cardinality',edge['id'],end+' 基数未知，不能当作无界。')
                elif card.get('max') is not None and card['max']<card['min']:issue('error','invalid-cardinality',edge['id'],end+' 最大基数小于最小基数。')
            if edge['type']=='instance_of' and edge['source']==edge['target']:issue('error','self-instance',edge['id'],'实例不能是自身的能力类型。')
            if edge['type']=='causal_influence' and edge.get('attributes',{}).get('polarity') not in ['+','-','unknown']:issue('error','causal-polarity',edge['id'],'因果关系须声明 polarity 为 +、- 或 unknown。')
    # Cycle detection applies only to actual hierarchical/dependency relations.
    for typ in ['decomposes','reports_to','precedes','depends_on']+(['composition','generalization','visually_contains'] if v2 else []):
        graph={}
        for edge in rel.values():
            if edge['type']==typ:graph.setdefault(edge['source'],[]).append(edge['target'])
        active=set();done=set()
        def visit(node):
            if node in active:return True
            if node in done:return False
            active.add(node)
            if any(visit(n) for n in graph.get(node,[])):return True
            active.remove(node);done.add(node);return False
        if any(visit(n) for n in list(graph)):issue('error','cycle',typ,'层级、阶段顺序或前置依赖存在循环。')
    for v in views.values():
        if v2:provenance(v)
        refs(v['entity_ids'],ent,v['id'],'实体');refs(v['relationship_ids'],rel,v['id'],'关系')
        a=allarts.get(v['artifact_id'])
        if not a:issue('error','unknown-artifact',v['id'],v['artifact_id']);continue
        profile=profiles.get(v.get('profile_id'))
        if v.get('profile_id') and not profile:issue('error','unknown-profile',v['id'],v['profile_id'])
        if profile and profile['artifact_id']!=v['artifact_id']:issue('error','profile-artifact-mismatch',v['id'],'视图规范属于不同制品族。')
        if v2 and v.get('state_id'):refs([v['state_id']],indexes['states'],v['id'],'架构状态')
        if v2 and v.get('state_ids'):
            refs(v['state_ids'],indexes['states'],v['id'],'视图比较状态')
            for eid in v['entity_ids']:
                entity=ent.get(eid,{})
                if entity.get('state_id') and entity['state_id'] not in v['state_ids']:
                    issue('error','view-state-selection',v['id'],eid+' 不在视图声明的状态选择内。')
        if v2 and v.get('scope_id'):refs([v['scope_id']],indexes['scopes'],v['id'],'范围')
        if v2 and v.get('state_id') in indexes['states'] and indexes['states'][v['state_id']]['evolution']!=v['context']['evolution']:issue('error','state-evolution-conflict',v['id'],'视图命名状态与五维演进状态不一致。')
        if v2 and v.get('state_id') in indexes['states']:
            state_scope=indexes['states'][v['state_id']].get('scope_id')
            if state_scope and v.get('scope_id') and state_scope!=v['scope_id']:issue('error','state-scope-conflict',v['id'],'视图与命名状态的范围不一致。')
        if not v['entity_ids']:issue('warning','empty-view',v['id'],'视图没有对象；仅能作为明确的待补草稿。')
        for rid in v['relationship_ids']:
            edge=rel.get(rid)
            if edge and not {edge['source'],edge['target']}<=set(v['entity_ids']):issue('error','view-edge-outside',v['id'],f'{rid} 的端点未全部加入视图。')
        for eid in v['entity_ids']:
            e=ent.get(eid)
            if not e:continue
            state=evolution(e)
            if state!=v['context']['evolution'] and not v.get('allow_mixed_evolution'):issue('error','mixed-evolution',v['id'],f'{eid} 是 {state}，与视图状态不符；比较视图需显式允许混合。')
            if v2 and v.get('state_id') and e.get('state_id') and v['state_id']!=e['state_id'] and not v.get('allow_mixed_evolution'):
                issue('error','mixed-named-state',v['id'],f'{eid} 属于命名状态 {e["state_id"]}，不是 {v["state_id"]}；比较视图需显式允许混合。')
            # A named v2 profile narrows the family contract. Classification is not
            # a heatmap, and a typed decomposition edge need not duplicate a parent
            # attribute. Reapplying the broad v1 family fields would solicit facts
            # unrelated to the chosen decision. Profiles declare their own fields.
            if not profile and e['type'] in a['entity_types']:
                for f in a.get('required_attributes',{}).get(e['type'],[]):
                    from proficiency_semantics import is_explicit_unknown_current
                    if f!='name' and not is_explicit_unknown_current(e,f) and (f not in e['attributes'] or e['attributes'][f] in [None,'']):issue('warning','missing-attribute',eid,f'{a["id"]} 缺少项目约定字段 {f}；应填写或在 gaps 说明。')
            if profile:
                required=profile.get('required_attributes',{})
                required=required.get(e['type'],[])+required.get('*',[]) if isinstance(required,dict) else required
                for f in required:
                     from evaluation_semantics import is_evaluation_field_satisfied
                     alternative = (profile.get('renderer') == 'heatmap' and is_evaluation_field_satisfied(
                         e, f, profile.get('template', {}), indexes.get('scales', {})))
                     from proficiency_semantics import is_explicit_unknown_current
                     alternative = alternative or is_explicit_unknown_current(e,f)
                     if f!='name' and not alternative and (f not in e['attributes'] or e['attributes'][f] in [None,'']):issue('warning','profile-attribute-gap',eid,'视图规范缺少必要字段：'+str(f))
        for rid in v['relationship_ids']:
            edge=rel.get(rid)
            if not edge:continue
            if v2 and v.get('state_id') and edge.get('state_id') and v['state_id']!=edge['state_id'] and not v.get('allow_mixed_evolution'):
                issue('error','mixed-named-state',v['id'],f'{rid} 的关系状态与视图命名状态不同。')
            allowed_relationships=set(a['relationship_types']) | set((profile or {}).get('relationship_types',[]))
            if edge['type'] not in allowed_relationships:
                issue('warning','view-relation-outside-contract',v['id'],f'{rid} 不在本制品定义的关系集合；确认表示法或扩展约定。')
            required_relation_fields=set(a.get('relationship_requirements',{}).get(edge['type'],[])) | set((profile or {}).get('relationship_requirements',{}).get(edge['type'],[]))
            for attr in required_relation_fields:
                if attr not in edge.get('attributes',{}):issue('error','missing-relation-attribute',rid,f'关系缺少 {attr}')
        for eid in v['entity_ids']:
            e=ent.get(eid)
            if e:
                for f in a.get('required_identity_fields',{}).get(e['type'],[]):
                    if f not in e:issue('error','missing-identity-field',eid,f'状态比较要求 {f}')
        if a['kind']=='matrix' and a.get('matrix'):
            m=a['matrix']; row=[ent[i] for i in v['entity_ids'] if i in ent and ent[i]['type'] in m['row_types']];col=[ent[i] for i in v['entity_ids'] if i in ent and ent[i]['type'] in m['column_types']]
            if not row or not col:issue('warning','empty-axis',v['id'],'矩阵行或列为空。')
            for rid in v['relationship_ids']:
                edge=rel.get(rid)
                if not edge:continue
                if edge['type']!=m['relationship']:issue('error','matrix-relation',rid,'矩阵引用了不同语义的关系。')
                codes=edge.get('codes',[])
                if m['codes'] and (not codes or set(codes)-set(m['codes'])):issue('error','matrix-code',rid,f'允许的单元代码：{m["codes"]}')
                if edge['source'] in ent and edge['target'] in ent and (ent[edge['source']]['type'] not in m['row_types'] or ent[edge['target']]['type'] not in m['column_types']):issue('error','matrix-direction',rid,'端点必须从声明的行类型指向列类型。')
    for d in indexes['deliverables'].values():
        provenance(d);refs(d['view_ids'],views,d['id'],'视图');refs(d['entity_ids'],ent,d['id'],'实体')
        contract=DELS[d['deliverable_id']]
        if v2 and d.get('assembly'):
            from deliverable_assembly import assemble
            result=assemble(model,d,contract)
            for gap in result['gaps']:
                issue('error' if d['assembly']['mode']=='strict' else 'warning',gap['code'],gap['id'],gap['message'])
        else:
            for section in contract['sections']:
                if not d['sections'].get(section['title'],'').strip():issue('error','missing-section',d['id'],section['title'])
            available={views[i]['artifact_id'] for i in d['view_ids'] if i in views}
            for aid in contract['artifact_ids']:
                if aid not in available:issue('warning','deliverable-artifact-gap',d['id'],f'推荐支撑制品 {aid} 未引用；裁剪时需说明。')
    for c in model.get('comparisons',[]):
        refs(c['baseline_ids']+c['target_ids']+c['gap_ids'],ent,c['id'],'比较实体')
        if v2:
            refs(c.get('state_ids',[]),indexes['states'],c['id'],'比较状态')
            if c.get('scope_id'):refs([c['scope_id']],indexes['scopes'],c['id'],'比较范围')
            refs([c[key] for key in ['baseline_state_id','target_state_id'] if c.get(key)],indexes['states'],c['id'],'比较端状态')
            if c.get('baseline_state_id') and c['baseline_state_id']==c.get('target_state_id'):issue('error','comparison-same-state',c['id'],'比较两端不能选择同一个命名状态。')
            for key in ['baseline_state_id','target_state_id']:
                if c.get(key) and c.get('state_ids') and c[key] not in c['state_ids']:issue('error','comparison-state-scope',c['id'],key+' 未包含在声明的比较状态集合。')
            for eid in c['baseline_ids']+c['target_ids']:
                e=ent.get(eid)
                if not e:continue
                if c.get('scope_id') and e.get('scope_id') and c['scope_id']!=e['scope_id']:issue('error','comparison-scope',c['id'],eid+' 不属于声明的比较范围。')
                if c.get('state_ids') and e.get('state_id') and e['state_id'] not in c['state_ids']:issue('error','comparison-state-scope',c['id'],eid+' 的命名状态不属于声明的比较状态集合。')
            for eid in c['gap_ids']:
                if eid in ent and ent[eid]['type']!='gap':issue('error','comparison-gap-type',c['id'],eid+' 不是差距对象。')
        for key,wanted in [('baseline_ids','baseline'),('target_ids','target')]:
            for eid in c[key]:
                e=ent.get(eid)
                selected=c.get(wanted+'_state_id') if v2 else None
                if e and selected and e.get('state_id')!=selected:issue('error','comparison-state',c['id'],f'{eid} 不是所选命名状态 {selected}')
                elif e and not selected and evolution(e)!=wanted:issue('error','comparison-state',c['id'],f'{eid} 不是 {wanted}')
    if v2:
        for e in ent.values():
            if e['type']=='capability_instance':
                targets={r['target'] for r in rel.values() if r['type']=='instance_of' and r['source']==e['id']}
                targets.update(r['source'] for r in rel.values() if r['type']=='has_instance' and r['target']==e['id'])
                if len(targets)!=1:issue('error','instance-type-cardinality',e['id'],'每个能力实例必须显式归属一个能力类型；不是能力分解。')
        for state in indexes['states'].values():
            provenance(state)
            if state.get('scope_id'):refs([state['scope_id']],indexes['scopes'],state['id'],'范围')
            if state['evolution']=='transition':
                required={'operations','data_consistency','dependencies','controls','rollback'}
                missing=[key for key in required if not state.get('operating_conditions',{}).get(key,'').strip()]
                if missing:issue('warning','transition-operability-gap',state['id'],'过渡可运营条件待补：'+','.join(sorted(missing)))
        for scale in indexes['scales'].values():
            refs(scale['evidence'],sources,scale['id'],'量表证据')
            anchors=[a['value'] for a in scale['anchors']]
            if len(set(anchors))!=len(anchors):issue('error','duplicate-scale-anchor',scale['id'],'量表锚点值重复，含义不唯一。')
        for scope in indexes['scopes'].values():
            refs(scope.get('included_ids',[])+scope.get('excluded_ids',[]),ent,scope['id'],'范围对象')
            if set(scope.get('included_ids',[]))&set(scope.get('excluded_ids',[])):issue('error','scope-conflict',scope['id'],'同一个对象同时列为纳入与排除。')
        for analysis in indexes['analyses'].values():
            refs(analysis.get('evidence',[]),sources,analysis['id'],'分析证据')
            from analysis_binding import binding_issues
            issues.extend(binding_issues(model,analysis))
    if v2:
        from organization_derivation import validate_organization_derivations
        issues.extend(validate_organization_derivations(model))
        from contract_semantics import semantic_issues
        issues.extend(semantic_issues(model, ent, rel))
    from assignment_projection import projection_issues
    for view in model.get('views', []):
        issues.extend(projection_issues(model, view))
    from closure_semantics import check as check_closure
    issues.extend(check_closure(model))
    from proficiency_semantics import check as check_proficiency
    issues.extend(check_proficiency(model))
    from foundation_planning import check as check_foundation_planning
    issues.extend(check_foundation_planning(model))
    return issues

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('model');p.add_argument('--report');p.add_argument('--strict',action='store_true',help='警告也导致非零退出；草稿通常不需要。');p.add_argument('--business-rules',help='可选的项目业务规则契约 JSON；与结构结果分开报告。');a=p.parse_args()
    try: issues=validate(load(a.model))
    except (OSError,ValueError) as e:sys.exit(str(e))
    structural_errors=sum(i['level']=='error' for i in issues)
    business_issues=[]
    if a.business_rules:
        from business_policy import load_and_check
        try: business_issues=load_and_check(load(a.model),a.business_rules)
        except (OSError,ValueError) as e:sys.exit(str(e))
    report={'schema_version':'2.0','errors':structural_errors+len(business_issues),
            'structural_errors':structural_errors,'business_errors':len(business_issues),
            'warnings':sum(i['level']=='warning' for i in issues),
            'issues':issues+business_issues,
            'limit':'结构校验与可选项目业务规则检查分别报告；不证明真实合规或正式批准。'}
    if a.report:Path(a.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2));return int(report['errors']>0 or (a.strict and report['warnings']>0))
if __name__=='__main__':sys.exit(main())
