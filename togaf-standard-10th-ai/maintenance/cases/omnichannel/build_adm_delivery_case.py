#!/usr/bin/env python3
"""Assemble 23 case-specific candidate deliverables from one fictional ADM dossier.

Uses the existing ADM model and raw sources, not profile example factories.
The added material is authored scenario input, not inferred historical approval.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import shutil
import sys

H = Path(__file__).resolve().parent
C = H.parents[2]
S = C / 'skills/_shared'
sys.path[:0] = [str(S/'scripts'), str(S/'vendor')]
sys.dont_write_bytecode = True
from adm import check_cycle, iteration_fingerprint, requirements_context, requirements_fingerprint
from deliverable_assembly import assemble, load_rules
from generate import generate
from registry import load as registry
from validate import validate

MATERIALS = H/'adm-delivery-materials.json'

def load(path):
    return json.loads(Path(path).read_text())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def build(material):
    arts, deliveries, profiles, _ = registry()
    rules = load_rules()
    authored = {d['deliverable_id']:d for d in material['deliverables']}
    if set(authored) != set(deliveries) or len(authored) != len(material['deliverables']):
        raise ValueError('material must explicitly cover each current deliverable once')
    model = copy.deepcopy(load(H/'generated-adm/model.json'))
    cycle = copy.deepcopy(load(H/'generated-adm/cycles/cycle.json'))
    model['project']['version'] = '1-delivery-draft'
    model['extensions']['entity_types']['project:section_evidence'] = '针对性章节候选证据，人工推理不冒充计算或官方实体类型'
    model['sources'].append({'id':'ADM-DELIVERY-BRIEF','kind':'example',
        'description':material['notice'], 'locator':'maintenance/cases/omnichannel/adm-delivery-materials.json'})
    model['sources'].append({'id':'ADM-INPUT-Requirements','kind':'example',
        'description':'给定虚构持续需求管理原材料',
        'locator':'maintenance/cases/omnichannel/adm-business-materials.md#requirements'})
    entities = {e['id']:e for e in model['entities']}
    for identity, attrs in material['existing_object_attributes'].items():
        if identity not in entities:
            raise ValueError('unknown existing scenario object '+identity)
        entities[identity]['attributes'].update(copy.deepcopy(attrs))
        entities[identity]['evidence']=list(dict.fromkeys(entities[identity].get('evidence',[])+['ADM-DELIVERY-BRIEF']))
        if identity in {'WP-ONLINE','WP-OFFLINE','TRANS-ONLINE','TRANS-OFFLINE','RISK-STOCK'}:
            entities[identity]['evidence'].append('ADM-INPUT-F')
        if entities[identity]['type']=='application':
            entities[identity].setdefault('concept_id',identity)
            entities[identity].setdefault('evolution','target')
    for obj in material['objects']:
        if obj['id'] in entities:
            raise ValueError('duplicate material object '+obj['id'])
        entity = {k:copy.deepcopy(obj[k]) for k in ('id','type','name','attributes')}
        entity.update(evidence=['ADM-DELIVERY-BRIEF','ADM-INPUT-'+obj['source_phase']],certainty='assumed')
        model['entities'].append(entity)
        entities[entity['id']] = entity
    # Scope-specific policy and observations remain structured inputs in the same model.
    model['extensions']['entity_types']['case:delivery-policy'] = '同一虚构材料的版本化政策和给定观察'
    policy_entity={'id':'ADM-DELIVERY-POLICY','type':'case:delivery-policy','name':'全渠道V1及V2候选边界',
        'attributes':{'policy':copy.deepcopy(material['policy']), 'active_policy':copy.deepcopy(material['policy']['baseline']), 'given_observations':copy.deepcopy(material['given_observations']),
                      'planning':copy.deepcopy(material['planning'])},'evidence':['ADM-DELIVERY-BRIEF'],'certainty':'assumed'}
    model['entities'].append(policy_entity);entities[policy_entity['id']]=policy_entity
    needed={family for rule in rules['deliverables'] for req in rule.get('core_requirements',[]) for family in req.get('artifact_ids',[])}
    # Each core group requires one applicable representation, not every alternative.
    for family in sorted(needed):
        if any(v['artifact_id']==family for v in model['views']):
            continue
        profile=profiles.get('compat-'+family)
        if profile is None:
            continue
        ids=[e['id'] for e in model['entities'] if e['type'] in profile.get('entity_types',[])]
        selection=material.get('view_selections',{}).get(family)
        if selection:
            if not selection.get('rationale') or not set(selection['entity_ids'])<=set(ids):
                raise ValueError('invalid authored view selection '+family)
            ids=selection['entity_ids']
        if not ids:
            continue
        edges=[r['id'] for r in model['relationships'] if r['source'] in ids and r['target'] in ids and r['type'] in profile.get('relationship_types',[])]
        model['views'].append({'id':'adm-delivery-'+family,'artifact_id':family,'profile_id':profile['id'],
            'title':'全渠道情景／'+arts[family]['name_zh'],'context':copy.deepcopy(model['project']['context']),
            'entity_ids':ids,'relationship_ids':edges,
            'analysis':'从同一ADM交付物材料选择本情景对象；未知保护、厂商、真实权限不补造。',
            'legend':'全虚构候选设计；章节与来源支持另列，图表生成不授予业务批准。'})
    model['deliverables']=[]
    stage_map=[]
    for rule in rules['deliverables']:
        did=rule['id'];source=authored[did];contract=deliveries[did]
        if [r['title'] for r in source['sections']] != [r['title'] for r in contract['sections']]:
            raise ValueError('authored chapters differ from current contract: '+did)
        if source['applicability'] != 'applicable-scenario-draft' or not source['scope_rationale']:
            raise ValueError('missing explicit applicability '+did)
        if not source['support_ids'] or any(i not in entities for i in source['support_ids']):
            raise ValueError('missing scenario supports '+did)
        d={'id':'ADM-DLV-'+did,'deliverable_id':did,'title':'全渠道／'+contract['name_zh'],
            'view_ids':[],'entity_ids':[],'sections':{},'approval_status':'candidate','implementation_status':'not-started',
            'assembly':{'mode':'strict','rules_version':rules['rules_version'],'section_bindings':{},'tailoring':[]}}
        core_ids=[]
        for req in rule.get('core_requirements',[]):
            v=next((v for v in model['views'] if v['artifact_id'] in req.get('artifact_ids',[]) or v.get('profile_id') in req.get('profile_ids',[])),None)
            if v is None:
                raise ValueError('no case-specific core support '+did+':'+req['id'])
            core_ids.append(v['id'])
        for ordinal, chapter in enumerate(source['sections'],1):
            if not chapter['conclusion'].strip() or not chapter['source_anchors']:
                raise ValueError('missing chapter reasoning/source '+did+':'+chapter['title'])
            identity='ADM-SECTION-'+did+'-'+str(ordinal)
            phase_ids=['ADM-WORK-'+p for p in chapter['source_anchors'] if p!='Requirements']
            policy_refs=['ADM-DELIVERY-POLICY'] if did in material['policy_sensitive_deliverables'] else []
            refs=list(dict.fromkeys(source['support_ids']+phase_ids+policy_refs))
            record={'id':identity,'type':'project:section_evidence','name':chapter['title']+'／全渠道论证',
                'certainty':'assumed','evidence':['ADM-DELIVERY-BRIEF']+['ADM-INPUT-'+p for p in chapter['source_anchors']],
                'attributes':{'deliverable_id':did,'section_title':chapter['title'],'question':chapter['question'],
                    'conclusion':chapter['conclusion'],'decision':chapter['conclusion'],'scope':source['scope_rationale'],
                    'owner':source['owner'],'acceptance':source['acceptance'],'status':'scenario-proposal',
                    'authority':'scenario-authority','reasoning_kind':'authored-from-fixed-business-materials; not a deterministic calculation',
                    'unknowns':source['unknowns'],'model_refs':refs,'source_material_sha256':digest(chapter),
                    'applicability':source['applicability'],'stage_ids':source['phases']}}
            model['entities'].append(record)
            sr=next(r for r in rule['sections'] if r['title']==chapter['title'])
            vs=[v['id'] for v in model['views'] if (v.get('profile_id') in sr.get('profile_ids',[]) if sr.get('profile_ids') else v['artifact_id'] in sr.get('artifact_ids',[]))]
            binding={'entity_ids':[identity]+refs,'view_ids':vs}
            if sr.get('entity_types'):
                binding['override']={'reason':'本章直接绑定同一材料的治理职责、阶段决定及章节论证；新增文档是候选，不替代真实治理授权。','owner':source['owner'],'evidence':['ADM-DELIVERY-BRIEF']}
            d['assembly']['section_bindings'][chapter['title']]=binding
            d['view_ids'].extend(vs)
            d['sections'][chapter['title']]=chapter['conclusion']
        d['view_ids']=list(dict.fromkeys(core_ids+d['view_ids']))
        model['deliverables'].append(d)
        stage_map.append({'deliverable_id':did,'instance_id':d['id'],'phases':source['phases'],
            'applicability':source['applicability'],'rationale':source['scope_rationale'],'review_status':'candidate-business-review-pending',
            'source_material_sha256':digest(source),'chapter_count':len(source['sections'])})
    # Refresh snapshots after explicit scenario projection changes; personnel
    # observations, ratings, task hours and approval data are not modified.
    data=model['analyses'][0]['inputs']
    data['source_ids']=list(dict.fromkeys(data['source_ids']+['ADM-DELIVERY-BRIEF','ADM-INPUT-F']))
    selected={i for task in data['tasks'] for i in task['model_object_refs']}
    wanted={i for task in data['tasks'] for i in task['artifact_ids']}
    data['model_objects']=copy.deepcopy([e for e in model['entities'] if e['id'] in selected])
    data['model_relationships']=copy.deepcopy([r for r in model['relationships'] if r['source'] in selected and r['target'] in selected])
    data['model_views']=copy.deepcopy([v for v in model['views'] if v['artifact_id'] in wanted])
    entities[data['model_binding']['context_ref']]['attributes']['assessment_inputs']=copy.deepcopy(data)
    for phase in cycle['phases']:
        it=phase['iterations'][-1]
        added=[{'collection':'deliverables','id':row['instance_id']} for row in stage_map if phase['phase'] in row['phases']]
        it['output_refs']=[r for r in it['output_refs'] if r['collection']!='deliverables']+added
        it['decision']['rationale']+=' 新增正式文档是本轮从同一情景材料派生的候选；本记录只追踪原情景决定，不授予新增文档独立业务接受。'
        current=iteration_fingerprint(model,it,cycle['scope'])
        it['model_sha256']=current
        for step in it['source_step_coverage']:
            step['context_sha256']=current
        for review in cycle['requirements']['reviews']:
            if review['iteration_id']==it['id']:
                review['model_sha256']=requirements_fingerprint(model,cycle,phase['phase'])
    for step in cycle['requirements']['source_step_coverage']:
        step['context_sha256']=requirements_context(model,cycle)
    return model,cycle,stage_map

def relocate_evidence(cycle, raw_path):
    # Snapshot the exact original source. Original records stay unchanged on disk.
    def visit(value):
        if isinstance(value,dict):
            if 'path' in value and 'sha256' in value and value['path'].endswith('adm-business-materials.md'):
                value['path']='../materials/adm-business-materials.md'
                value['sha256']=sha(raw_path)
            for v in value.values():visit(v)
        elif isinstance(value,list):
            for v in value:visit(v)
    visit(cycle)


def run(out, material_path=MATERIALS):
    if out.exists():
        raise ValueError('new output directory required; historical evidence is immutable')
    material=load(material_path)
    for relative, expected in material['raw_source_files'].items():
        if sha(H/relative)!=expected:
            raise ValueError('raw scenario source changed; re-author/review dossier: '+relative)
    model,cycle,stage_map=build(material)
    errors=[x for x in validate(model) if x['level']=='error']
    if errors:raise ValueError(json.dumps(errors,ensure_ascii=False))
    out.mkdir(parents=True)
    for name in material['raw_source_files']:
        (out/'materials').mkdir(exist_ok=True);shutil.copyfile(H/name,out/'materials'/name)
    shutil.copyfile(material_path,out/'materials/adm-delivery-materials.json')
    relocate_evidence(cycle,out/'materials/adm-business-materials.md')
    for phase in cycle['phases']:
        phase['iterations'][-1]['decision']['evidence'].append({
            'path':'../materials/adm-delivery-materials.json',
            'sha256':sha(out/'materials/adm-delivery-materials.json'),
            'locator':'本轮新增候选文档材料附件；不表示原情景决定已审阅新增正式文档'})
    save(out/'model.json',model);save(out/'cycles/cycle.json',cycle)
    save(out/'stage-deliverable-map.json',stage_map)
    checks=check_cycle(cycle,model,out/'cycles')
    save(out/'adm-check.json',checks)
    if checks['errors'] or not checks['recorded_cycle_complete'] or not checks['foundation_source_coverage_complete']:
        raise ValueError('ADM decisions/94-step records do not bind current deliverables: '+str(checks))
    _,contracts,_,_=registry()
    assemblies={d['id']:assemble(model,d,contracts[d['deliverable_id']]) for d in model['deliverables']}
    save(out/'assemblies.json',assemblies)
    failed={k:v['gaps'] for k,v in assemblies.items() if v['status']!='assembled-awaiting-review' or v['unbound_section_titles']}
    if failed:raise ValueError('assembly failed: '+str(failed))
    generate(model,out/'generated',all_items=True,strict=True,render=False)
    summary={'schema_version':'omnichannel-adm-delivery/1','phases':9,'source_steps':94,
        'structured_deliverables':len(model['deliverables']),'chapter_count':sum(len(d['sections']) for d in model['deliverables']),
        'strict_assemblies':len(assemblies),'stage_outputs_bound':True,'approval_status':'candidate',
        'independent_business_accepted':False,'real_approval':'not-granted',
        'input_sha256':{str(p.relative_to(C)):sha(p) for p in [material_path,H/'adm-business-materials.md',H/'sufficient-business-materials.md',H/'generated-adm/model.json',H/'generated-adm/cycles/cycle.json',S/'deliverables.json',S/'capability-addenda/deliverable-assembly-rules.json']},
        'limits_zh':['同一扩充虚构材料驱动当前阶段/模型/23份实际组装文档；新增提案明确标记。','90章内容为作者具体推理和模型引用，未用统一计算器冒充专业分析。','程序结构与前向断言不能授予不同评审人的全范围接受；不证明真实组织批准或部署。']}
    save(out/'summary.json',summary)
    print(json.dumps({k:summary[k] for k in ['phases','source_steps','structured_deliverables','chapter_count','strict_assemblies','independent_business_accepted']},ensure_ascii=False))
    return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--materials',type=Path,default=MATERIALS);args=parser.parse_args()
    run(args.out,args.materials)
