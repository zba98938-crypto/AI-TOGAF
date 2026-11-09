"""Observable source-view invariants, separate from generic model validity.

Missing content is a draft gap. These rules do not establish business truth or
replace the source-specific human review questions in a profile.
"""
from evaluation_semantics import parse_evaluation, stage_capability_errors

def check_view(model,view,profile):
    byid={e["id"]:e for e in model["entities"]}
    es=[byid[i] for i in view["entity_ids"] if i in byid]
    rs=[r for r in model["relationships"] if r["id"] in view["relationship_ids"]]
    types={e["type"] for e in es};relations={r["type"] for r in rs};pid=profile["id"]
    errors=[]
    def need(condition,code,message):
        if not condition:errors.append({"id":view["id"],"code":code,"message":message})
    missing=set(view['entity_ids'])-set(byid)
    need(not missing,'view-entity-missing','视图引用的对象不存在：'+','.join(sorted(missing)))
    if pid=="capability-decomposition":
        decomposition=[r for r in rs if r['type']=='decomposes' and byid.get(r['source'],{}).get('type')=='capability' and byid.get(r['target'],{}).get('type')=='capability']
        need(bool(decomposition),"missing-semantic-decomposition","能力分解规范需要实际的能力分解关系；视觉包含或实例组成不构成能力分解。")
    if pid in ["capability-instance-composition","capability-instance-model-default"]:
        need("capability_instance" in types and "capability" in types,"missing-instance-type","能力实例视图需要实例及其能力类型。")
        need("instance_of" in relations or "has_instance" in relations,"missing-instance-reference","每个实例应明确回链能力类型。")
        need("instance_comprises" in relations,"missing-instance-composition","实例组成必须具有人员、流程、应用或信息等显式组成。")
        need("stage_uses_instance" in relations,"missing-stage-instance","应明确实例在价值流阶段中的使用语境。")
        for instance in [e for e in es if e['type']=='capability_instance']:
            identity=instance['id']
            targets={r['target'] for r in rs if r['type']=='instance_of' and r['source']==identity}
            targets.update(r['source'] for r in rs if r['type']=='has_instance' and r['target']==identity)
            need(len(targets)==1,'instance-view-type-gap',identity+' 必须在该视图中回链唯一能力类型。')
            need(any(r['type']=='instance_comprises' and r['source']==identity for r in rs),'instance-view-composition-gap',identity+' 在该视图中缺少实例组成。')
            need(any(r['type']=='stage_uses_instance' and r['target']==identity for r in rs),'instance-view-stage-gap',identity+' 在该视图中缺少价值流阶段语境。')
    if pid=="information-capability-use-modify":
        need(bool(types & {"information","business_object"}) and "capability" in types,"missing-information-capability","信息映射需要能力和信息概念。")
        need(bool(relations & {"uses_information","modifies_information"}),"missing-information-operation","使用或修改信息必须有显式类型关系和图例。")
    if pid in ["value-stream-definition","value-stream-enabling-capabilities","value-stream-capability-heatmap"]:
        stages=[e for e in es if e["type"] in ["value_stage","value_stream_stage","stage","customer_journey_stage"]]
        need(bool(stages),"missing-value-stages","价值流视图需要阶段对象。")
        if "capabilit" in pid:need("enabled_by" in relations or "stage_uses_instance" in relations,"missing-stage-enablement","阶段与能力使能关系必须明确。")
    if "heatmap" in pid or profile.get('renderer')=='heatmap':
        if pid=='value-stream-capability-heatmap' or profile.get('template',{}).get('heatmap_axes')=='stage-capability':
            errors.extend(stage_capability_errors(es,rs))
        scales={s['id']:s for s in model.get('scales',[])}
        observations=[parse_evaluation(e,profile.get('template',{}),scales) for e in es+rs]
        need(any(p['observed'] for p in observations),"missing-heatmap-observations","热力图需要实际评价、显式未知或明确未来不存在状态。")
        for parsed in observations:
            for error in parsed['errors']:errors.append({**error,'view_id':view['id']})
    if pid in ["business-model-canvas","business-model-baseline-target"]:
        need(len({e.get("attributes",{}).get("block") for e in es})>=9,"incomplete-canvas-blocks","完整九块画布示例应覆盖九类区块；缺失区块需在裁剪说明中解释。")
    if pid=='business-model-baseline-target':
        states={e.get('state_id') for e in es}
        need(None not in states and len(states)>=2,'missing-canvas-comparison-states','比较画布需要至少两个明确状态，不能用一张画布冒充比较。')
        for state in states:
            need(len({e.get('attributes',{}).get('block') for e in es if e.get('state_id')==state})>=9,'incomplete-state-canvas','每个比较状态分别需要九类区块：'+str(state))
    if pid=="information-bounded-cardinality":
        need(any(any(isinstance(v,dict) and v.get("max") is not None and v.get("min")!=v.get("max") for v in r.get("cardinality",{}).values()) for r in rs),"missing-bounded-example","该有界基数示例应实际包含有限上下界。")
    # Profiles can declare additional portable structural constraints without code edits.
    constraints=profile.get("structural_requirements",{})
    for typ,count in constraints.get("minimum_entity_types",{}).items():
        need(sum(e["type"]==typ for e in es)>=count,"profile-entity-minimum","缺少规定数量的对象类型："+typ)
    for typ in constraints.get("relationship_types",[]):need(typ in relations,"profile-relationship-required","缺少规定关系："+typ)
    from source_shape_semantics import check_source_shape
    errors.extend(check_source_shape(es, rs, profile))
    from source_topology_semantics import check_source_topology
    errors.extend(check_source_topology(es, rs, profile, view))
    if profile.get('renderer')=='roadmap':
        from schedule_semantics import check_schedule
        errors.extend(check_schedule(es))
    if view.get("tailoring"):
        for error in errors:error["tailoring_note"]=view["tailoring"]
    return errors
