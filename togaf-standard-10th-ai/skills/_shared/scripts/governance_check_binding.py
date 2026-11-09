"""Optional project binding for G248 checklist snapshots, not official schema.

Legacy direct inputs remain usable without model_binding. Opted-in model analyses
must resolve sources, named transition, source-row identities and exact view union.
A matching snapshot is not a verified business fact or authorization decision.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def binding_issues(model,analysis):
    data=analysis.get('inputs',{});binding=data.get('model_binding')
    if binding is None:return []
    findings=[]
    def issue(code,identity,message):findings.append({'level':'error','code':code,'id':analysis['id']+':'+str(identity),'message':message})
    def known_ids(values,label,known):
        if not isinstance(values,list) or not values or any(not isinstance(v,str) or not v.strip() for v in values):
            issue('governance-source-shape',label,'选入绑定时来源必须为非空ID数组。');return
        for value in values:
            if value not in known:issue('governance-source-reference',label+':'+value,'来源ID不在主模型sources中。')
    if not isinstance(binding,dict) or binding.get('version')!='governance-checks/1':
        issue('governance-binding-shape','model_binding','需要明确governance-checks/1版本的绑定对象。');return findings
    if set(binding)-{'version','view_ids','check_entity_ids'}:
        issue('governance-binding-shape','model_binding','绑定含未支持字段。')
    selected={}
    for key in ['view_ids','check_entity_ids']:
        values=binding.get(key)
        if not isinstance(values,list) or not values or any(not isinstance(v,str) or not v.strip() for v in values) or len(set(values))!=len(values):
            issue('governance-binding-shape',key,'需要非空、唯一字符串ID数组。');return findings
        selected[key]=set(values)
    sources={s['id'] for s in model.get('sources',[])}
    known_ids(data.get('rule_evidence'),'rule_evidence',sources)
    states={s['id']:s for s in model.get('states',[])};transition=data.get('transition_id')
    if not isinstance(transition,str) or transition not in states or states[transition].get('evolution')!='transition':
        issue('governance-transition-reference',transition,'需要主模型states中明确的命名transition状态。')
    stage=data.get('stage','all');profile=data.get('change_profile')
    if stage not in ['all','planning','implementation'] or profile not in ['rapid','functional','robust']:
        issue('governance-selection','stage/profile','未知阶段或画像。');return findings
    rows=json.loads((ROOT/'references/source-tables/change-profile-checks.json').read_text())['rows']
    rows={r['id']:r for r in rows if stage=='all' or r['id'].startswith(stage)}
    responses=data.get('responses',{});tailoring=data.get('tailoring',{})
    if not isinstance(responses,dict) or not isinstance(tailoring,dict):
        issue('governance-input-shape','responses/tailoring','需要对象映射。');return findings
    if (set(responses)|set(tailoring))-rows.keys():issue('governance-source-row','responses/tailoring','含不属于本阶段的来源检查ID。')
    for cid,response in responses.items():
        if not isinstance(response,dict):issue('governance-input-shape',cid,'逐项response需要对象。');continue
        if response.get('status')=='pass':known_ids(response.get('evidence'),cid+':response',sources)
        elif response.get('evidence') is not None:known_ids(response['evidence'],cid+':response',sources)
    for cid,rule in tailoring.items():
        if not isinstance(rule,dict):issue('governance-input-shape',cid,'逐项tailoring需要对象。');continue
        known_ids(rule.get('evidence'),cid+':tailoring',sources)
    entities={e['id']:e for e in model.get('entities',[])};seen={}
    for eid in selected['check_entity_ids']:
        entity=entities.get(eid)
        if not entity:issue('governance-entity-reference',eid,'选中检查实体不存在。');continue
        attrs=entity.get('attributes',{});cid=attrs.get('source_check_id')
        if entity.get('type')!='guide:governance-check' or not isinstance(cid,str) or cid not in rows:
            issue('governance-entity-type',eid,'需要本阶段有来源行的guide:governance-check。');continue
        if cid in seen:issue('governance-duplicate-check',cid,'同一来源检查被多个选中实体冒充。')
        seen[cid]=eid;row=rows[cid];rule=tailoring.get(cid,{})
        if entity.get('name')!=row['question']:issue('governance-question-mismatch',eid,'实体名称必须保留该来源检查问句，不得用已批准结论替换。')
        if attrs.get('tailoring')!=tailoring.get(cid):issue('governance-tailoring-mismatch',eid,'主模型tailoring必须与分析的include/reason/evidence完整一致；无裁剪时省略或null。')
        if not isinstance(rule,dict):rule={}
        expected={'source_check_id':cid,'step':row['step'],'adm_phase':row['phase'],
          'change_profile':profile,'transition_id':transition,
          'applicability':rule.get('include',profile in row['profiles']),
          'response':responses.get(cid,{'status':'unreviewed'})}
        for key,value in expected.items():
            if attrs.get(key)!=value or (key in ['step','applicability'] and type(attrs.get(key)) is not type(value)):
                issue('governance-model-field-mismatch',eid+'.'+key,'检查快照与当前主模型/来源行不一致；不能继续展示旧结论。')
        response=expected['response']
        if isinstance(response,dict):
            for key in ['owner','action']:
                if key in response and attrs.get(key)!=response[key]:issue('governance-model-field-mismatch',eid+'.'+key,'主模型责任/行动与response不一致。')
        if attrs.get('evidence_locator')!=row['source']:issue('governance-source-locator',eid,'来源行定位与所选source_check_id不符。')
        known_ids(entity.get('evidence'),eid+':entity',sources)
    if set(seen)!=set(rows):issue('governance-check-coverage','check_entity_ids','选中实体须完整覆盖所选阶段所有源行（含未建议纳入项），不把源表空白当不适用。')
    views={v['id']:v for v in model.get('views',[])};union=set()
    profiles={'change-profile-planning-checklist':'planning','change-profile-implementation-checklist':'implementation'}
    for vid in selected['view_ids']:
        view=views.get(vid)
        if not view:issue('governance-view-reference',vid,'绑定视图不存在。');continue
        expected_stage=profiles.get(view.get('profile_id'))
        if view.get('artifact_id')!='change-profile-governance-checklist' or expected_stage is None:
            issue('governance-view-profile',vid,'需要对应工作产品的planning/implementation专用profile。')
        ids=view.get('entity_ids',[]);union.update(ids)
        if analysis['id'] not in view.get('attributes',{}).get('analysis_ids',[]):issue('governance-view-analysis',vid,'视图未显式引用本分析。')
        for eid in ids:
            cid=entities.get(eid,{}).get('attributes',{}).get('source_check_id','')
            if not isinstance(cid,str) or expected_stage is None or not cid.startswith(expected_stage+'-'):
                issue('governance-view-stage',vid+':'+eid,'所选profile与检查阶段不符。')
    if union!=selected['check_entity_ids']:issue('governance-view-closure','view_ids','视图实体并集必须精确等于分析所选检查集合。')
    return findings
