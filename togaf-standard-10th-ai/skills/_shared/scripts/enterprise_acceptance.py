"""Full two-case design delivery and stage-specific ADM records, never approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from adm import initialize,check_cycle,contracts,digest,load,iteration_fingerprint,requirements_fingerprint,CONTRACT_PATH
from registry import load as registry
from validate import validate
from deliverable_assembly import assemble
from case_simulations import run as simulate

ROOT=Path(__file__).resolve().parents[1]

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

PHASE_KEYS={
'Preliminary':(['organization','role','principle'],['repository','standard']),
'A':(['driver','stakeholder','constraint'],['goal','project']),
'B':(['goal','capability'],['capability','value_stream','value_stage']),
'C':(['req','capability'],['data','interface']),
'D':(['interface','req'],['technology','control']),
'E':(['gap','abb'],['sbb','wp']),
'F':(['wp','migration'],['wp1','wp3','milestone']),
'G':(['contract','req'],['control','decision']),
'H':(['benefit','measure'],['change','req'])}

PHASE_NOTES={
'Preliminary':'明确运营/平台/数据责任，设备控制独立；建立原则、版本库和裁剪方法。',
'A':'用驱动、利益相关者、硬边界确定研究范围及可验证目标；报价和生产能力未知。',
'B':'比较基线人工处理与目标职责分离，分析证据可用性、价值流及人工异常责任。',
'C':'比较版本身份、样本/温控时标、接口回放和数据权威，目标不覆盖原始证据。',
'D':'明确隔离/网关平台、事件留存和恢复控制；生产容量与现场安全测试未知。',
'E':'把跨域差距分配给契约、影子回放及受控推广工作包；保留适配与替换的显式权衡。',
'F':'按工作包依赖安排过渡，人工权威、数据核对、冻结和回退分别规定；真实资源日历未知。',
'G':'将候选合同判据与实际软件模拟回执对照；设备、隔离、真实签署与业务接受不由模拟授予。',
'H':'从行为阈值/撤销要求触发影响分析，明确不受影响边界；决定只在模拟研究范围内有效。'}

def prepare(kind):
    if kind=='lingang':
        from lingang_casework import build_case
        return build_case()
    from qianlin_casework import build_case
    model,raw,inventory=build_case()
    # Preserve historical generic-trace fixture. This delivery gives each relation
    # a semantic predicate while retaining its identity and hand-authored meaning.
    predicates=['motivates','requires','assigned_to','assigns','uses','used_by','exposes','runs_on','exposes_risk','reveals_gap','addressed_by','realized_by','verified_by','requires_gate','enables_value','measured_by','triggers','changes','constrains','mitigates','constrains','binds','contains_stage','enabled_by','depends_on','depends_on','references','samples','owns','publishes','consumes','governs','maintains']
    for r,predicate in zip([r for r in model['relationships'] if r['id'].startswith('QL-TRACE-')],predicates):
        typ='ql:'+predicate
        model['extensions']['relationship_types'][typ]={'source_types':['*'],'target_types':['*'],'meaning':predicate+'；具体语义以关系label和手写章节为准，不表示批准'}
        r['type']=typ
    # Inventory is a scale fixture, not evidence for this enterprise decision.
    # Deliver the authored projection; retain the original inventory on disk.
    model['entities']=[e for e in model['entities'] if 'QL-INVENTORY' not in e.get('evidence',[])]
    kept={e['id'] for e in model['entities']}
    model['relationships']=[r for r in model['relationships'] if {r['source'],r['target']}<=kept]
    for scope in model['scopes']:scope['included_ids']=[i for i in scope.get('included_ids',[]) if i in kept]
    excluded={'balanced-scorecard-default','capability-increment-analysis-default','capability-instance-composition','customer-journey-default','mdm-consolidation-collaboration-central'}
    removed={v['id'] for v in model['views'] if v['profile_id'] in excluded}
    model['views']=[v for v in model['views'] if v['id'] not in removed]
    for d in model['deliverables']:
        d['view_ids']=[v for v in d['view_ids'] if v not in removed]
        for b in d['assembly']['section_bindings'].values():b['view_ids']=[v for v in b.get('view_ids',[]) if v not in removed]
    for e in model['entities']:
        if e['type']=='interface' and 'QL-INVENTORY' not in e['evidence']:
            e['attributes'].update(producer='LIMS检验事件发布方',consumer='MES隔离区消费方')
    inventory['external_evidence']=['真实质量/架构评审与签章','现场隔离、回退和故障注入','岗位容量观察与真实报价']
    bind_relation_types(model)
    return model,inventory

def bind_relation_types(model):
    byid={e['id']:e for e in model['entities']}
    for typ,definition in model.get('extensions',{}).get('relationship_types',{}).items():
        if not typ.startswith(('lg:','ql:')):continue
        uses=[r for r in model['relationships'] if r['type']==typ]
        if uses:
            definition['source_types']=sorted({byid[r['source']]['type'] for r in uses})
            definition['target_types']=sorted({byid[r['target']]['type'] for r in uses})

def phase_records(model,inventory,out):
    cycle=initialize(model,model['project']['id']+'-design-cycle','模拟设计与软件规则验证；不是生产批准')
    versions=inventory['versions'];ids={k:v[-1] for k,v in versions.items()}
    if 'tech' in ids:ids['technology']=ids['tech']
    for phase in cycle['phases']:
        key=phase['phase'];it=phase['iterations'][-1];ins,outs=PHASE_KEYS[key]
        it.update(status='completed',owner='模拟架构角色；scenario-authority',
                  input_refs=[{'collection':'entities','id':ids[k]} for k in ins],
                  output_refs=[{'collection':'entities','id':ids[k]} for k in outs],
                  contract_sha256=digest(load(CONTRACT_PATH)))
        # Stage-specific artifacts and authored arguments are saved as actual bytes.
        documents=[d for d in model['deliverables'] if d['deliverable_id'] in contracts()[key]['deliverables']]
        evidence={'phase':key,'scope':'fictional-design-only','reasoning':PHASE_NOTES[key],
          'inputs':[next(e for e in model['entities'] if e['id']==r['id']) for r in it['input_refs']],
          'outputs':[next(e for e in model['entities'] if e['id']==r['id']) for r in it['output_refs']],
          'chapters':{d['deliverable_id']:d['sections'] for d in documents},
          'simulation':'simulation.json' if key in {'C','D','G','H'} else None,
          'external_evidence':inventory['external_evidence'],
          'business_acceptance':'not-assessed','professional_review':'pending-professional-review'}
        filename='phase-'+key+'.json';save(out/filename,evidence)
        record=[{'path':filename,'sha256':hashlib.sha256((out/filename).read_bytes()).hexdigest(),'locator':'/'+key+'/reasoning+inputs+outputs+chapters'}]
        it['decision']={'status':'accepted','authority':'情景作者（虚构），只接受模拟分析记录','authority_role':'stakeholder',
                        'rationale':PHASE_NOTES[key]+'本决定不批准真实预算、采购、实施或业务运行。','evidence':record}
        for criterion,text in contracts()[key]['criteria'].items():
            it['criteria'][criterion].update(status='satisfied',rationale=text+'；'+PHASE_NOTES[key]+'详见本阶段输入、输出及交付物章节；仅在模拟研究范围记录。',evidence=record)
        it['model_sha256']=iteration_fingerprint(model,it,cycle['scope'])
        cycle['requirements']['owner']='模拟需求责任人'
        cycle['requirements']['reviews'].append({'iteration_id':it['id'],'reviewer':'模拟运营和架构角色','rationale':'对照本阶段实际输入/输出与候选需求，生产证据限制已显式记录。','change_ids':[],
          'model_sha256':requirements_fingerprint(model,cycle,key),'evidence':record})
    return cycle

def acceptance_probes(model,inventory,cycle,out):
    # A new versioned behavior requirement is an accepted change candidate, not an
    # in-place rewrite of the immutable original requirements baseline.
    modified=copy.deepcopy(model);versions=inventory['versions'];req=copy.deepcopy(next(e for e in model['entities'] if e['id']==versions['req'][-1]))
    req['attributes']['supersedes_id']=req['id']
    req['id']+='-CR-next';req['version']=str(int(req.get('version','1'))+1)
    req['attributes']['acceptance']='LG：时差31秒按30秒容差拒绝；QL：撤销后跨日重放必须保持冻结；其余边界不变。'
    modified['entities'].append(req)
    changed=copy.deepcopy(cycle);ev=copy.deepcopy(cycle['phases'][0]['iterations'][-1]['decision']['evidence'])
    changed['requirements']['baseline_ids'].append(req['id'])
    changed['requirements']['changes']=[{'id':'design-CR-02','requirement_ids':[req['id']],'reason':'版本化的行为验收变更；原基线只读',
       'affected_phases':['C','D','G','H'],'affected_refs':[{'collection':'entities','id':req['id']}],
       'decision':{'status':'accepted','authority':'情景作者（虚构）','authority_role':'stakeholder','rationale':'仅授权模拟影响分析，生产决定独立。','evidence':ev}}]
    result=check_cycle(changed,modified,out)
    save(out/'changed-model.json',modified);save(out/'changed-cycle.json',changed);save(out/'changed-check.json',result)
    # Corrupt one copy of a real evidence file; never rewrite the original receipt.
    stale=copy.deepcopy(cycle)
    stale['phases'][1]['iterations'][-1]['decision']['evidence'][0]['sha256']='0'*64
    stale_result=check_cycle(stale,model,out);save(out/'stale-check.json',stale_result)
    states={p['phase']:p['status'] for p in result['phases']}
    from adm import new_iteration
    for phase in changed['phases']:
        if phase['phase'] not in {'C','D','G','H'}:continue
        previous=phase['iterations'][-1];it=new_iteration(phase['phase'],2,'CR-02行为变更后实际重新验证；旧记录只读保留')
        it.update(status='completed',owner=previous['owner'],input_refs=copy.deepcopy(previous['input_refs'])+[{'collection':'entities','id':req['id']}],output_refs=copy.deepcopy(previous['output_refs']),contract_sha256=digest(load(CONTRACT_PATH)))
        filename='phase-'+phase['phase']+'-CR02.json'
        save(out/filename,{'phase':phase['phase'],'requirement':req,'simulation':simulate(),'scope':'software-design-simulation-only','business_acceptance':'not-assessed'})
        evidence=[{'path':filename,'sha256':hashlib.sha256((out/filename).read_bytes()).hexdigest(),'locator':'/requirement+/simulation'}]
        it['decision']=copy.deepcopy(previous['decision']);it['decision']['evidence']=evidence
        for criterion in it['criteria'].values():criterion.update(status='satisfied',rationale='按版本化CR-02实际重放规则与原验收边界；证据保留新输入和模拟回执，现场接受仍独立。',evidence=evidence)
        it['model_sha256']=iteration_fingerprint(modified,it,changed['scope']);phase['iterations'].append(it)
        changed['requirements']['reviews'].append({'iteration_id':it['id'],'reviewer':'模拟运营及架构角色','rationale':'CR-02逐项复核且重放新边界','change_ids':['design-CR-02'],'model_sha256':requirements_fingerprint(modified,changed,phase['phase']),'evidence':evidence})
    revalidated=check_cycle(changed,modified,out);save(out/'revalidated-cycle.json',changed);save(out/'revalidated-check.json',revalidated)

    return {'changed_phases':states,'affected_reopened':all(states.get(k)=='incomplete' for k in ['C','D','G','H']),
            'unaffected_preserved':all(states.get(k)=='recorded-complete' for k in ['Preliminary','A','B','E','F']),
            'revalidated_complete':not revalidated['errors'] and all(p['status']=='recorded-complete' for p in revalidated['phases']),
            'stale_evidence_rejected':next(p for p in stale_result['phases'] if p['phase']=='A')['status']=='incomplete'}

def run_case(kind,out,render=True):
    from generate import generate
    model,inventory=prepare(kind);bind_relation_types(model);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    save(out/'model.json',model);save(out/'inventory.json',inventory);save(out/'simulation.json',simulate()[kind]);save(out/'validation.json',validate(model))
    cycle=phase_records(model,inventory,out);save(out/'adm-cycle.json',cycle)
    result=check_cycle(cycle,model,out);save(out/'adm-check.json',result)
    probes=acceptance_probes(model,inventory,cycle,out);save(out/'change-probes.json',probes)
    arts,dels,profiles,methods=registry();assemblies=[]
    for d in model['deliverables']:
        a=assemble(model,d,dels[d['deliverable_id']]);assemblies.append({'id':d['deliverable_id'],'status':a['status'],'section_coverage':a['section_coverage'],'gaps':a['gaps']})
    save(out/'assemblies.json',assemblies)
    generated=[]
    for layout in ['reference','adaptive']:
        manifest=generate(model,out/layout,all_items=True,render=render,layout=layout)
        generated.append({'layout':layout,'views':len(manifest['artifacts']),'deliverables':len(manifest['deliverables']),'draft_views':[a['view_id'] for a in manifest['artifacts'] if a.get('status')=='draft-with-gaps']})
    summary={'case':kind,'entities':len(model['entities']),'chapters':sum(len(a['section_coverage']) for a in assemblies),
      'unbound_chapters':[c for a in assemblies for c in a['section_coverage'] if c['status']=='unbound'],
      'assembly_gaps':[g for a in assemblies for g in a['gaps']],
      'adm_errors':result['errors'],'phases':{p['phase']:p['status'] for p in result['phases']},'probes':probes,'generated':generated,
      'business_acceptance':'not-assessed','professional_review':'pending-professional-review','external_evidence':inventory['external_evidence']}
    save(out/'summary.json',summary);return summary

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--case',choices=['lingang','qianlin'],required=True);parser.add_argument('--out',type=Path,required=True);parser.add_argument('--no-render',action='store_true');a=parser.parse_args()
    print(json.dumps(run_case(a.case,a.out,not a.no_render),ensure_ascii=False))
