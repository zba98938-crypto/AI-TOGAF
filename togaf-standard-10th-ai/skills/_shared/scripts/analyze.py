#!/usr/bin/env python3
"""Evidence-bounded change impact traversal and evolution comparison."""
import argparse
import json
from pathlib import Path
from collections import deque
from validate import validate
from numeric_contracts import finite_number, require_finite, stable_id, unique_records
from strict_json import load as load_json, dumps as strict_dumps

def impact(model,ids,max_depth=3):
    entities={e['id']:e for e in model['entities']};known=set(entities)
    if set(ids)-known:raise ValueError('未知对象：'+','.join(set(ids)-known))
    # Undirected traversal intentionally proposes candidates; it is not a claim of actual impact.
    visited={i:0 for i in ids};q=deque(ids);paths={i:[] for i in ids}
    while q:
        current=q.popleft()
        if visited[current]>=max_depth:continue
        for r in model['relationships']:
            if current not in [r['source'],r['target']]:continue
            target=r['target'] if r['source']==current else r['source']
            if target not in visited:
                visited[target]=visited[current]+1;paths[target]=paths[current]+[r['id']];q.append(target)
    return {'notice':'候选排查范围；图可达不自动等于实际业务影响。','candidates':[{'id':i,'name':entities[i]['name'],'depth':depth,'relationship_path':paths[i],'confirmation':'待逐项确认'} for i,depth in visited.items() if i not in ids]}

def compare(model,baseline_state=None,target_state=None,scope_id=None):
    from architecture_comparison import compare_architectures
    return compare_architectures(model,baseline_state,target_state,scope_id)

def decision_matrix(inputs):
    if not inputs.get('rule_evidence'):raise ValueError('决策计算须提供规则来源 rule_evidence')
    criteria=unique_records(inputs['criteria'],'criteria',nonempty=True)
    options=unique_records(inputs['options'],'options',nonempty=True)
    for c in criteria:
        finite_number(c['weight'],c['id']+'.weight',minimum=0)
        finite_number(c['min'],c['id']+'.min');finite_number(c['max'],c['id']+'.max')
        if c['direction'] not in ['maximize','minimize'] or c['max']<=c['min']:raise ValueError('判据须给出优化方向、有效区间和非负权重')
        finite_number(c['max']-c['min'],c['id']+'.range')
    weight=finite_number(sum(c['weight'] for c in criteria),'total-weight')
    if weight<=0:raise ValueError('权重和必须大于零')
    results=[]
    for option in options:
        if option.get('eligible') is False:
            if not option.get('reason'):raise ValueError('淘汰方案须有硬约束理由')
            results.append({'id':option['id'],'eligible':False,'reason':option['reason']});continue
        parts=[]
        for c in criteria:
            value=option['scores'].get(c['id'])
            if value is None:raise ValueError(option['id']+' 缺少判据 '+c['id']+'；不自动填零')
            finite_number(value,option['id']+'.'+c['id'])
            if not c['min']<=value<=c['max']:raise ValueError('评分超出声明区间')
            n=(value-c['min'])/(c['max']-c['min'])
            if c['direction']=='minimize':n=1-n
            parts.append({'criterion_id':c['id'],'raw':value,'normalized':n,'contribution':finite_number(n*c['weight']/weight,option['id']+'.'+c['id']+'.contribution')})
        results.append({'id':option['id'],'eligible':True,'score':sum(p['contribution'] for p in parts),'components':parts})
    ranking=sorted([r for r in results if r['eligible']],key=lambda x:(-x['score'],x['id']))
    return {'method':'weighted-normalized-decision','results':results,'ranking':[r['id'] for r in ranking],'rule_evidence':inputs['rule_evidence'],'notice':'分数仅依据所声明的尺度、方向和权重；不自动批准方案。并列分数不表示优劣。'}

def maturity_assessment(inputs):
    if not inputs.get('rule_evidence'):raise ValueError('成熟度汇总须提供采用模型和规则的证据')
    factors=unique_records(inputs['factors'],'factors',nonempty=True)
    lo=finite_number(inputs['scale']['min'],'scale.min');hi=finite_number(inputs['scale']['max'],'scale.max')
    if hi<=lo or not factors:raise ValueError('量表或因素为空')
    for f in factors:
        finite_number(f['value'],f['id']+'.value',minimum=lo,maximum=hi)
        finite_number(f['weight'],f['id']+'.weight',minimum=0)
        if not f.get('evidence'):raise ValueError('因素须有量表内评分、非负权重和证据')
    total=finite_number(sum(f['weight'] for f in factors),'total-weight')
    if total<=0:raise ValueError('权重和必须大于零')
    weighted=finite_number(sum(f['value']*f['weight'] for f in factors),'weighted-total')
    result={'weighted_level':weighted/total,'factor_results':factors,'rule_evidence':inputs['rule_evidence'],'notice':'采用模型下的加权结果；不自创合格线。逐级达成率只由明确的达成证据计算。'}
    if 'levels' in inputs:
        levels=inputs['levels']
        if not isinstance(levels,list):raise ValueError('levels 必须为量表内等级列表')
        for level in levels:finite_number(level,'levels',minimum=lo,maximum=hi)
        if len(set(levels))!=len(levels):raise ValueError('levels 等级重复')
        if any('achieved_levels' not in f for f in factors):raise ValueError('逐级达成率须提供每因素的 achieved_levels；不从等级分数猜测')
        for f in factors:
            if not isinstance(f['achieved_levels'],list):raise ValueError('achieved_levels 必须为等级列表')
            for level in f['achieved_levels']:finite_number(level,f['id']+'.achieved_levels',minimum=lo,maximum=hi)
        result['level_attainment_percent']={str(level):100*sum(level in f['achieved_levels'] for f in factors)/len(factors) for level in inputs['levels']}
    return result

def preference_decision(inputs):
    """G176 §12.8-style anchored preference scores; monetary cost is not a score."""
    if not inputs.get('rule_evidence'):raise ValueError('偏好评分须给出评分锚点和规则证据')
    criteria=unique_records(inputs['criteria'],'criteria',nonempty=True)
    options=unique_records(inputs['options'],'options',nonempty=True)
    total=finite_number(sum(finite_number(c.get('weight',1),c['id']+'.weight',minimum=0) for c in criteria),'total-weight')
    if total<=0:raise ValueError('权重须非负且和大于零')
    results=[]
    for o in options:
        parts=[]
        for c in criteria:
            value=o.get('scores',{}).get(c['id'])
            finite_number(value,o['id']+'.'+c['id'],minimum=1,maximum=5)
            parts.append({'criterion_id':c['id'],'preference_score':value,'weight':c.get('weight',1),
                          'contribution':finite_number(value*c.get('weight',1),o['id']+'.'+c['id']+'.contribution')})
        weighted=finite_number(sum(p['contribution'] for p in parts),o['id']+'.weighted-sum')
        results.append({'id':o['id'],'weighted_sum':weighted,
                        'weighted_mean':weighted/total,'components':parts})
    return {'method':'preference-weighted-decision','results':results,
            'ranking':[r['id'] for r in sorted(results,key=lambda r:(-r['weighted_sum'],r['id']))],
            'rule_evidence':inputs['rule_evidence'],
            'notice':'G176式1至5偏好评分；成本和资源列已是偏好值，5最佳，不再反向。权重为项目选择；并列不表示优劣。'}

def dtra_review(inputs):
    """Review project-coded ordinal ratings without inventing a TOGAF threshold."""
    if not inputs.get('rule_evidence') or not inputs.get('factor_rating_rule'):
        raise ValueError('须提供因素评分形成规则及证据；不从问卷项擅自平均')
    required={
        'foundational':{'vision','sponsorship-direction','it-capability','culture','scope-scale','business-rationale','implementation-approach'},
        'impact':{'business-model-adaptability','skills-competence','technology-maturity','ecosystem','governance-compliance'},
        'sustaining':{'value-realization','policy-regulations','funding-resources'}}
    threshold=inputs.get('attention_min_rating')
    threshold_evidence=inputs.get('attention_threshold_evidence')
    if threshold is not None and (isinstance(threshold,bool) or not isinstance(threshold,int)
                                  or not 1<=threshold<=7 or not threshold_evidence):
        raise ValueError('管理关注等级阈值须为1至7且有明确项目规则证据')
    byid={};attention=[]
    for f in unique_records(inputs['factors'],'factors'):
        if f['id'] in byid:raise ValueError('因素ID重复')
        if f['category'] not in required or f['id'] not in required[f['category']]:raise ValueError('未知DTRA因素或类别；附加因素需单独报告')
        value=f.get('rating')
        if isinstance(value,bool) or not isinstance(value,int) or not 1<=value<=7 or not f.get('evidence'):
            raise ValueError('因素须有1至7等级和评价证据')
        byid[f['id']]=f
        if threshold is not None and value<threshold:
            attention.append({'id':f['id'],'rating':value,'action':'复核并评估缺失因素后果，不自动推定发生概率'})
    missing=sorted(set.union(*required.values())-byid.keys())
    complete={group:ids<=byid.keys() for group,ids in required.items()}
    satisfied={group:complete[group] and all(byid[i]['rating']>=threshold for i in ids)
               if threshold is not None else None for group,ids in required.items()}
    typ=None
    if threshold is not None and not missing and satisfied['foundational']:
        typ=3 if satisfied['impact'] and satisfied['sustaining'] else 2 if satisfied['impact'] else 1
    return {'method':'dtra-factor-review','attention_factors':attention,'missing_factor_ids':missing,
            'category_complete':complete,'category_satisfied':satisfied,'readiness_type':typ,
            'attention_min_rating':threshold,'attention_threshold_evidence':threshold_evidence,
            'blockers':['project-attention-threshold-missing'] if threshold is None else [],
            'factor_rating_rule':inputs['factor_rating_rule'],'rule_evidence':inputs['rule_evidence'],
            'notice':'数值编码与管理关注阈值须由项目显式声明，非G212原图规则；类型须完整覆盖15因素并满足递进条件。阈值、基础因素或数据缺失时不赋类型；ABCD是独立采用方法，不是排名。'}

def risk_assessment(inputs):
    if inputs.get('formula')!='likelihood-times-impact' or not inputs.get('rule_evidence'):raise ValueError('风险乘法须明确采用公式和规则来源；TOGAF不规定统一乘法公式')
    values={}
    for key in ['likelihood','impact']:
        measure=inputs[key]
        if not measure.get('scale') or not measure.get('evidence'):raise ValueError('概率/影响须有非负评价、量表和证据')
        values[key]=finite_number(measure['value'],key+'.value',minimum=0)
    return {'inherent_risk':finite_number(values['likelihood']*values['impact'],'inherent-risk'),'formula':inputs['formula'],'rule_evidence':inputs['rule_evidence'],'notice':'这是显式采用的项目计算规则；控制存在不自动证明剩余风险降低。'}

def environmental_delta(inputs):
    if not inputs.get('boundary') or not inputs.get('method_evidence'):raise ValueError('环境度量须有核算边界和方法证据')
    results=[]
    if any('id' in row for row in inputs['rows']):unique_records(inputs['rows'],'rows')
    for row in inputs['rows']:
        if not row.get('unit') or not row.get('scope') or not row.get('period') or not row.get('evidence'):raise ValueError('每项环境度量须有单位、Scope、期间和证据')
        added=finite_number(row['added'],'row.added');retired=finite_number(row['retired'],'row.retired')
        if 'reported_net' in row:finite_number(row['reported_net'],'row.reported_net')
        delta=finite_number(added-retired,'row.calculated_net');r={**row,'calculated_net':delta}
        if 'reported_net' in row and row['reported_net']!=delta:r['source_difference']={'reported':row['reported_net'],'calculated':delta,'resolution':'保留印刷值和计算值，核查舍入及边界，不自动改正'}
        results.append(r)
    return {'rows':results,'boundary':inputs['boundary'],'method_evidence':inputs['method_evidence'],'notice':'逐行比较；不跨不同Scope、单位或生命周期范围求和，抵消另行记录。'}

def lean_flow_metrics(inputs):
    """Serial-flow arithmetic with explicit time basis and conditional yields."""
    if not inputs.get('boundary') or not inputs.get('rule_evidence'):
        raise ValueError('精益度量须声明串行流范围和规则证据')
    if inputs.get('aggregation_rule')!='serial-conditional-first-pass':
        raise ValueError('须明确采用串行流与条件首次完整准确率；并行/返工网络需另建分析')
    steps=unique_records(inputs.get('steps',[]),'steps',nonempty=True)
    def minutes(measure):
        value=finite_number(measure['value'],'time.value',minimum=0);unit=measure.get('unit')
        if unit=='minute':return value
        if unit=='hour':return finite_number(value*60,'time.minutes')
        if unit=='working-day':
            hours=finite_number(inputs.get('working_hours_per_day'),'working_hours_per_day',minimum=0,maximum=24)
            if hours<=0:
                raise ValueError('工作日换算必须显式给出每日工作小时')
            return finite_number(value*hours*60,'time.minutes')
        raise ValueError('时间单位仅支持minute/hour/working-day；日历日不能默认为工作日')
    lead=process=0;quality=1
    for step in steps:
        if not step.get('evidence'):raise ValueError('每个流程度量须有证据')
        lt=minutes(step['lead_time']);pt=minutes(step['process_time'])
        if pt>lt:raise ValueError('同一范围中加工时间不能大于前置时间，需核对单位与边界')
        q=finite_number(step['complete_accurate_percent'],step['id']+'.complete_accurate_percent',minimum=0,maximum=100)
        lead=finite_number(lead+lt,'total-lead-time');process=finite_number(process+pt,'total-process-time');quality*=q/100
    if lead<=0:raise ValueError('总前置时间须大于0')
    return {'total_lead_time_minutes':lead,'total_process_time_minutes':process,
            'activity_ratio_percent':finite_number(100*process/lead,'activity-ratio-percent'),'non_processing_time_minutes':lead-process,
            'cumulative_complete_accurate_percent':quality*100,'boundary':inputs['boundary'],
            'notice':'串行流程与显式换算下的算术结果；不把未加工时间全部解释为可消除浪费，不推导产能或业务架构价值流能力。'}

def change_profile_checklist(inputs):
    """Apply G248 source inclusion flags, then review explicit project responses.

    This is checklist accounting, not a score or an authorization decision.
    """
    template=json.loads((Path(__file__).resolve().parents[1]/'references/source-tables/change-profile-checks.json').read_text())
    profile=inputs.get('change_profile');transition=inputs.get('transition_id')
    if profile not in {'rapid','functional','robust'} or not transition or not inputs.get('rule_evidence'):
        raise ValueError('须给出rapid/functional/robust画像、具体过渡ID及采用来源证据')
    stable_id(transition,'transition_id')
    stage=inputs.get('stage','all')
    if stage not in {'all','planning','implementation'}:raise ValueError('未知检查阶段')
    rows=[r for r in template['rows'] if stage=='all' or r['id'].startswith(stage)]
    known={r['id'] for r in rows};responses=inputs.get('responses',{});tailoring=inputs.get('tailoring',{})
    if (set(responses)|set(tailoring))-known:raise ValueError('存在不属于所选范围的检查ID')
    out=[]
    for row in rows:
        included=profile in row['profiles'];reason='源指南建议纳入' if included else '源指南未标Y；不等于不适用'
        if row['id'] in tailoring:
            rule=tailoring[row['id']]
            if not isinstance(rule.get('include'),bool) or not rule.get('reason') or not rule.get('evidence'):
                raise ValueError('每项裁剪须明确include、理由与证据')
            included=rule['include'];reason=rule['reason']
        response=responses.get(row['id'],{'status':'unreviewed'})
        if response['status'] not in {'unreviewed','pass','fail','deferred'}:raise ValueError('未知检查结果')
        if response['status']=='pass' and not response.get('evidence'):raise ValueError(row['id']+'通过但无证据')
        if response['status'] in {'fail','deferred'} and (not response.get('owner') or not response.get('action')):
            raise ValueError(row['id']+'未通过或延后须有负责人和行动')
        out.append({**row,'included':included,'inclusion_reason':reason,'response':response,'transition_id':transition})
    pending=[r['id'] for r in out if r['included'] and r['response']['status']!='pass']
    return {'rows':out,'pending_included_checks':pending,'included_count':sum(r['included'] for r in out),
            'rule_evidence':inputs['rule_evidence'],'notice':'逐项检查记录，不计算合格率、不自动批准；通过仅表示所提供证据声明满足项目检查，仍需治理责任方评审。'}

def evaluate(analysis,model=None):
    require_finite(analysis,'analysis')
    if not isinstance(analysis,dict):raise ValueError('invalid-analysis: expected an object')
    stable_id(analysis.get('id'),'analysis.id')
    stable_id(analysis.get('method_id'),'analysis.method_id')
    from analysis_evidence import require_evidence
    require_evidence(analysis,model)
    if model is not None:
        from analysis_binding import require_binding
        require_binding(model,analysis)
    from backlog_analysis import review_backlog_trace
    from evidence_analysis import business_attribute, scenario_traceability, environmental_annual
    from delivery_analysis import review_styles, review_options
    from collaboration_management_analysis import point_of_view_review, management_strategy_review, highlight_report_review
    from metadata_coverage_analysis import review_metadata_coverage
    from migration_analysis import dependency_order, transition_check, prioritize, benefit_trigger
    from g249_reasoning import review_role_skills
    methods={'weighted-normalized-decision':decision_matrix,'preference-weighted-decision':preference_decision,
             'maturity-weighted':maturity_assessment,'dtra-factor-review':dtra_review,
             'risk-explicit-rule':risk_assessment,'environmental-delta':environmental_delta,
             'lean-serial-flow':lean_flow_metrics,'change-profile-checklist':change_profile_checklist,
             'business-attribute-evaluation':business_attribute,'scenario-traceability-review':scenario_traceability,
             'environmental-annual-accounting':environmental_annual,
             'delivery-style-review':review_styles,'set-based-options-review':review_options,
             'ea-point-of-view-review':point_of_view_review,'project-management-strategy-review':management_strategy_review,
             'project-highlight-review':highlight_report_review}
    methods['architecture-backlog-trace-review']=review_backlog_trace
    methods['metadata-application-coverage-review']=review_metadata_coverage
    methods['architecture-role-skill-assessment']=review_role_skills
    methods.update({'dependency-topological-order': dependency_order,
                    'transition-operability-check': transition_check,
                    'work-package-prioritization': prioritize,
                    'benefit-realization-trigger': benefit_trigger})
    from gap_closure_analysis import (architecture_role_catalog_review, solution_delivery_notebook_review,
                                      product_constraint_conformance_review, domain_architecture_alignment_review,
                                      incident_architecture_adjustment_review)
    from scenario_readiness_analysis import (dtra_adm_phase_alignment_review, business_scenario_checklist_review,
                                             smart_objective_review)
    methods.update({'architecture-role-catalog-review': architecture_role_catalog_review,
                    'solution-delivery-notebook-review': solution_delivery_notebook_review,
                    'product-constraint-conformance-review': product_constraint_conformance_review,
                    'domain-architecture-alignment-review': domain_architecture_alignment_review,
                    'incident-architecture-adjustment-review': incident_architecture_adjustment_review,
                    'dtra-adm-phase-alignment-review': dtra_adm_phase_alignment_review,
                    'business-scenario-checklist-review': business_scenario_checklist_review,
                    'smart-objective-review': smart_objective_review})
    if analysis['method_id'] not in methods:raise ValueError('没有该方法的确定性计算器；按对应技能方法分析：'+analysis['method_id'])
    try:
        result=methods[analysis['method_id']](analysis['inputs'])
        require_finite(result,'analysis.result')
    except ArithmeticError as exc:
        raise ValueError('invalid-calculation:'+analysis['method_id']+': '+str(exc)) from exc
    except (KeyError,TypeError,AttributeError) as exc:
        raise ValueError('invalid-input:'+analysis['method_id']+': '+str(exc)) from exc
    return {'id':analysis['id'],'method_id':analysis['method_id'],'result':result}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('model');p.add_argument('--impact',nargs='+');p.add_argument('--depth',type=int,default=3);p.add_argument('--compare',action='store_true');p.add_argument('--baseline-state');p.add_argument('--target-state');p.add_argument('--scope');p.add_argument('--evaluate',action='append',help='执行指定 analyses ID 的显式规则计算');a=p.parse_args()
    try:
        m=load_json(a.model);errors=[i for i in validate(m) if i['level']=='error']
    except (OSError,ValueError,TypeError) as exc:p.error(str(exc))
    if errors:p.error(json.dumps(errors,ensure_ascii=False))
    if a.depth<0:p.error('depth 必须非负')
    if not a.impact and not a.compare and not a.evaluate:p.error('请选择 --impact、--compare 或 --evaluate')
    result={}
    try:
        if a.impact:result['impact']=impact(m,a.impact,a.depth)
        if a.compare:result['comparison']=compare(m,a.baseline_state,a.target_state,a.scope)
    except ValueError as exc:p.error(str(exc))
    if a.evaluate:
        analyses={x['id']:x for x in m.get('analyses',[])}
        if set(a.evaluate)-analyses.keys():p.error('分析 ID 不存在')
        try:result['analyses']=[evaluate(analyses[i],m) for i in a.evaluate]
        except (ValueError,KeyError,TypeError) as exc:p.error(str(exc))
    print(strict_dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
