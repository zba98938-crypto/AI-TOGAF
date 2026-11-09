"""Evidence-bounded calculators for G152, G176 and G242 work products.

These contracts are explicit project operation rules, not TOGAF default scores.
All quantities are checked before arithmetic; missing values are never zero.
"""
from decimal import Decimal, InvalidOperation
import operator

class RuleError(ValueError):
    def __init__(self, code, object_id, message):
        self.code, self.object_id = code, object_id
        super().__init__(f'{code} [{object_id}]: {message}')

def require(condition, code, ident, message):
    if not condition: raise RuleError(code, ident, message)

def number(value, code, ident, minimum=None, maximum=None):
    require(not isinstance(value, bool) and isinstance(value, (int,float,Decimal)), code, ident, 'A finite numeric value is required')
    try: result=Decimal(str(value))
    except (InvalidOperation,ValueError): raise RuleError(code, ident, 'Invalid numeric value')
    require(result.is_finite(), code, ident, 'NaN and infinity are not observations')
    require(minimum is None or result>=minimum, code, ident, 'Value below declared minimum')
    require(maximum is None or result<=maximum, code, ident, 'Value above declared maximum')
    return result

def unique(records, code, ident):
    require(isinstance(records,list) and all(isinstance(r,dict) for r in records),code,ident,'Records must be a list of objects')
    ids=[r.get('id') for r in records]
    require(all(isinstance(i,str) and i.strip() for i in ids) and len(set(ids))==len(ids),code,ident,'Missing or duplicate stable ID')
    return {r['id']:r for r in records}

def evidence(refs, known, code, ident):
    require(isinstance(refs,list) and bool(refs) and all(isinstance(r,str) for r in refs) and set(refs)<=known,code,ident,'Missing or unknown evidence IDs')

def sources(data,code,ident):
    require(isinstance(data,dict),code,ident,'Analysis inputs must be an object')
    raw=data.get('source_ids')
    require(isinstance(raw,list) and raw and all(isinstance(x,str) for x in raw) and len(set(raw))==len(raw),code,ident,'Explicit source ID inventory required')
    return set(raw)

COMPARE={'>':operator.gt,'>=':operator.ge,'<':operator.lt,'<=':operator.le,'==':operator.eq,'!=':operator.ne}

def business_attribute(data):
    require(isinstance(data,dict),'BAP-001','business-attribute','Analysis inputs must be an object')
    ident=data.get('attribute_id','business-attribute')
    known=sources(data,'BAP-001',ident)
    for field in ['business_case_ref','definition','measurement_approach','metric','target','tolerable_deviation','corrective_action_trigger','frequency_or_cost_threshold','owner']:
        require(field in data and bool(data[field]),'BAP-002',ident,'Missing field '+field)
    require(data['business_case_ref'] in known,'BAP-002',ident,'Unknown business case')
    metric,target,tolerance,trigger=(data[k] for k in ['metric','target','tolerable_deviation','corrective_action_trigger'])
    require(all(isinstance(r,dict) for r in [metric,target,tolerance,trigger,data['measurement_approach'],data['frequency_or_cost_threshold']]),'BAP-002',ident,'Structured metric, target, tolerance, trigger and measurement records required')
    unit=metric.get('unit')
    require(unit and target.get('unit')==trigger.get('unit')==unit,'BAP-001',ident,'Metric/target/trigger units differ')
    require(metric.get('scale') in ['ratio','interval'] and metric.get('period') and metric.get('formula'),'BAP-001',ident,'Explicit numeric scale, period and calculation required')
    for record in [metric,target,tolerance,trigger]:evidence(record.get('evidence'),known,'BAP-001',ident)
    evidence(data['measurement_approach'].get('source_refs'),known,'BAP-001',ident)
    evidence(data.get('source_refs'),known,'BAP-001',ident)
    require(metric.get('rule_origin'),'BAP-001',ident,'Calculation origin required')
    formula=metric['formula']
    if formula in ['100 * numerator / denominator','numerator / denominator']:
        require((formula.startswith('100') and unit=='percent') or (formula=='numerator / denominator' and unit in ['ratio','fraction']),'BAP-001',ident,'Ratio formula and unit differ')
        den=number(metric.get('denominator'),'BAP-001',ident,Decimal(0));num=number(metric.get('numerator'),'BAP-001',ident,Decimal(0))
        require(den>0 and num<=den,'BAP-001',ident,'Empty or invalid sample')
        actual=num/den*(100 if unit=='percent' else 1)
    elif formula=='observed-value': actual=number(metric.get('value'),'BAP-001',ident)
    else: raise RuleError('BAP-001',ident,'Unsupported calculation; do not execute arbitrary formula strings')
    target_value=number(target.get('value'),'BAP-002',ident)
    deviation=number(tolerance.get('value'),'BAP-003',ident,Decimal(0))
    require(tolerance.get('unit')==('percentage-point' if unit=='percent' else unit),'BAP-003',ident,'Tolerance must use absolute metric units, or percentage points for percent')
    direction=tolerance.get('direction')
    require(direction in ['below-target','above-target'],'BAP-005',ident,'Explicit tolerance direction required')
    threshold=target_value+(-deviation if direction=='below-target' else deviation)
    require(number(trigger.get('threshold'),'BAP-005',ident)==threshold,'BAP-005',ident,'Trigger disagrees with target and tolerance')
    require(target.get('operator') in COMPARE and trigger.get('operator') in COMPARE,'BAP-005',ident,'Unknown comparison operator')
    require(trigger['operator'] in (['<','<='] if direction=='below-target' else ['>','>=']),'BAP-005',ident,'Trigger direction conflicts with tolerance')
    require(target['operator'] in (['>','>='] if direction=='below-target' else ['<','<=']),'BAP-005',ident,'Target direction conflicts with tolerance')
    require(trigger.get('action'),'BAP-005',ident,'Correction action is missing')
    extra=data['frequency_or_cost_threshold'];evidence(extra.get('evidence'),known,'BAP-004',ident)
    require((extra.get('status')=='not-applicable' and extra.get('reason')) or (extra.get('status')=='applicable' and extra.get('rules')),'BAP-004',ident,'Conditional threshold needs rules or an explicit non-applicability reason')
    meets=COMPARE[target['operator']](actual,target_value);breach=COMPARE[trigger['operator']](actual,threshold)
    require(not (meets and breach),'BAP-005',ident,'Target and correction rules overlap for this observation')
    return {'attribute_id':ident,'observed':float(actual),'target_gap':float(actual-target_value),'status':'corrective-action-required' if breach else 'meets-target' if meets else 'within-tolerance',
            'corrective_action':breach,'trigger_threshold':float(threshold),'unit':unit,'tolerance_unit':tolerance['unit'],'period':metric['period'],
            'rule_evidence':sorted(set(target['evidence']+tolerance['evidence']+trigger['evidence'])),'notice':'Only the declared project rule was evaluated; no TOGAF default threshold or approval is implied.'}

def scenario_transformation_evidence(data):
    """Resolve declared raw/normalized inputs; never invent transformation evidence."""
    known=sources(data,'SCN-001','scenario')
    raw=data.get('raw_record_ids',[])
    require(isinstance(raw,list) and set(raw)<=known and len(raw)==len(set(raw)),'SCN-001','raw','Raw IDs missing or duplicated')
    norm=unique(data.get('normalized_records',[]),'SCN-001','normalized')
    logs=unique(data.get('transformation_log',[]),'SCN-001','transformation')
    for row in norm.values():
        require(row.get('from') in raw,'SCN-001',row['id'],'Normalized record has no declared raw source')
    result={}
    for log in logs.values():
        inputs=log.get('input')
        require(isinstance(inputs,list) and inputs and set(inputs)<=set(raw)|set(norm),'SCN-001',log['id'],'Transformation input is not a raw/normalized record')
        result[log['id']]=sorted({item if item in raw else norm[item]['from'] for item in inputs})
    return result

def scenario_traceability(data):
    known=sources(data,'SCN-001','scenario')
    raw=data.get('raw_record_ids',[]);require(set(raw)<=known and len(raw)==len(set(raw)),'SCN-001','raw','Raw IDs missing or duplicated')
    cats=data.get('categories',{});expected={'stakeholder','human_actor','computer_actor','problem','objective'}
    require(isinstance(cats,dict),'SCN-004','categories','Categories must be an object')
    require(set(cats)==expected and all(isinstance(v,list) for v in cats.values()),'SCN-004','categories','Five declared scenario categories required; empty categories need explicit per-process gaps')
    all_targets=[v for values in cats.values() for v in values]
    require(len(all_targets)==len(set(all_targets)),'SCN-004','categories','An ID cannot silently change semantic category')
    processes=data.get('processes',[])
    require(processes and len(set(processes))==len(processes) and not set(processes)&set(all_targets),'SCN-004','processes','Invalid process identity')
    norm=unique(data.get('normalized_records',[]),'SCN-001','normalized');logs=unique(data.get('transformation_log',[]),'SCN-001','transformation')
    produced=set()
    for log in logs.values():
        require(log.get('input') and set(log['input'])<=set(raw)|set(norm),'SCN-001',log['id'],'Transformation input is not a raw/normalized record')
        require(log.get('output') and set(log['output'])<=set(norm)|set(data.get('work_product_ids',[])) and log.get('operation') and log.get('reason'),'SCN-001',log['id'],'Transformation output/reason missing')
        produced.update(log['output'])
    for row in norm.values():
        require(row.get('from') in raw and row['id'] in produced and row.get('text') and row.get('entity_id'),'SCN-001',row['id'],'Lost raw source, normalized meaning or transformation')
    transformation_evidence=scenario_transformation_evidence(data)
    active=set(processes+all_targets)
    require(active<={r['entity_id'] for r in norm.values()},'SCN-001','normalized','Active entity lacks normalization evidence')
    links=unique(data.get('associations',[]),'SCN-004','associations');matrix=[];seen=set();by_process={p:set() for p in processes}
    for link in links.values():
        ident=link['id'];kind=link.get('kind')
        require(kind in cats and link.get('process') in processes and link.get('target') in cats[kind],'SCN-004',ident,'Association endpoint/category mismatch')
        evidence(link.get('evidence'),set(raw),'SCN-001',ident)
        require(not link.get('codes'),'SCN-004',ident,'This scenario-association contract does not authorize CRUD/control-flow codes')
        key=(link['process'],link['target']);require(key not in seen,'SCN-004',ident,'Duplicate matrix cell');seen.add(key);by_process[link['process']].add(kind)
        matrix.append({'row':key[0],'column':key[1],'category':kind,'relation_id':ident,'meaning':'scenario-association','evidence':link['evidence']})
    declared_gaps={(g.get('process'),g.get('category')) for g in data.get('category_gaps',[]) if g.get('reason')}
    for process,kinds in by_process.items():
        for kind in expected-kinds:require((process,kind) in declared_gaps,'SCN-002',process,'Unreviewed category gap: '+kind)
    outcomes=unique(data.get('painpoint_outcomes',[]),'SCN-003','outcomes');linked=set();pairs=set()
    for link in outcomes.values():
        require(link.get('problem') in cats['problem'] and link.get('outcome') in cats['objective'],'SCN-003',link['id'],'Unknown problem/outcome')
        evidence(link.get('evidence'),set(raw),'SCN-001',link['id']);pair=(link['problem'],link['outcome'])
        require(pair not in pairs,'SCN-003',link['id'],'Duplicate problem/outcome pair');pairs.add(pair);linked.add(link['problem'])
    require(set(cats['problem'])<=linked,'SCN-003','outcomes','Every painpoint needs an expected outcome')
    for req in unique(data.get('derived_requirements',[]),'SCN-001','requirements').values():
        evidence(req.get('evidence'),set(raw),'SCN-001',req['id'])
        require(req.get('from_goal') in cats['objective'] and req.get('statement'),'SCN-001',req['id'],'Requirement source outcome/statement missing')
        if req.get('kind')=='technical-candidate':require(req.get('status')=='assumption-requires-owner-review','SCN-005',req['id'],'Technical proposal cannot become an approved fact')
    return {'process_rows':len(processes),'column_categories':len(cats),'associations':len(matrix),'painpoint_outcome_links':len(outcomes),'shared_human_actor_count':len(cats['human_actor']),
            'matrix_cells':matrix,'transformation_evidence':transformation_evidence,'unspecified_cell_meaning':'unknown-not-proven-absent','painpoint_outcomes':list(outcomes.values()),'declared_category_gaps':data.get('category_gaps',[]),'notice':'Association is neither CRUD nor sequence. Historical normalized records retain their original IDs.'}

MASS={'kgCO2e':Decimal(1),'tCO2e':Decimal(1000),'gCO2e':Decimal('0.001')}
def mass(value,unit,ident):
    require(unit in MASS,'ENV-001',ident,'Unsupported or absent emissions unit')
    return number(value,'ENV-008',ident,Decimal(0))*MASS[unit]

def environmental_annual(data):
    known=sources(data,'ENV-001','accounting');boundary=data.get('boundary',{})
    require(isinstance(boundary,dict) and isinstance(data.get('rules'),dict),'ENV-005','boundary','Boundary and rules must be structured records')
    for key in ['id','organization','geography','service','period','functional_unit','lifecycle_rule','coverage_status']:
        require(boundary.get(key),'ENV-005','boundary','Missing boundary field '+key)
    require(boundary.get('period_kind')=='year' and boundary.get('value_basis')=='full-year','ENV-006',boundary['id'],'Annual calculator requires a full-year reporting period')
    require(boundary.get('scope_perspective')=='organization','ENV-005',boundary['id'],'This contract uses the customer organization perspective')
    basis=boundary.get('scope2_basis');require(basis in ['location-based','market-based'],'ENV-002',boundary['id'],'Select exactly one Scope2 basis')
    require(boundary.get('cadence')=='annual','ENV-006',boundary['id'],'Yearly accounting is required; 2–3 years is comparison horizon, not sampling cadence')
    if 'comparison_horizon_years' in boundary:
        number(boundary['comparison_horizon_years'],'ENV-006',boundary['id']+'.comparison_horizon_years')
    evidence(data.get('rules',{}).get('source_refs'),known,'ENV-001','rules')
    require(data['rules'].get('aggregation') and (not data.get('prior_year') or data['rules'].get('percentage_change')),'ENV-001','rules','Aggregation and comparison rules must be declared')
    factors=unique(data.get('factors',[data['factor']] if data.get('factor') else []),'ENV-001','factors')
    clouds=unique(data.get('cloud_records',[data['cloud_record']] if data.get('cloud_record') else []),'ENV-001','cloud-records')
    cloud_values={}
    for ident,cloud in clouds.items():
        require(cloud.get('period_kind')=='year' and cloud.get('value_basis')=='full-year' and cloud.get('period')==boundary['period'],'ENV-006',ident,'Provider period and value basis differ')
        require(cloud.get('emissions_basis')=='gross','ENV-004',ident,'Gross provider emissions required')
        evidence(cloud.get('evidence'),known,'ENV-001',ident)
        # Require the supplier's disclosed direct-emission boundary explicitly.
        direct=cloud.get('scope1',{})
        require(direct.get('status')=='zero-with-evidence','ENV-005',ident,'Provider Scope1 must be explicitly zero with evidence; otherwise extend the declared method before using this calculator')
        evidence(direct.get('evidence'),known,'ENV-005',ident)
        for key in ['electricity_consumption_kwh','renewable_electricity_purchased_kwh','scope2_market_based_kgco2e','scope2_location_based_kgco2e','total_scope3_kgco2e','digital_equipment_scope3_kgco2e','carbon_credits_offsets_kgco2e','digital_waste_kg','recycled_digital_waste_kg','stored_data_gb_including_replication','network_traffic_gb']:
            number(cloud.get(key),'ENV-008',ident+'.'+key,Decimal(0))
        number(cloud.get('pue'),'ENV-001',ident+'.pue',Decimal(1))
        require(cloud['digital_equipment_scope3_kgco2e']<=cloud['total_scope3_kgco2e'],'ENV-003',ident,'Equipment subset exceeds total Scope3')
        require(cloud['recycled_digital_waste_kg']<=cloud['digital_waste_kg'],'ENV-001',ident,'Recycled subset exceeds the same reported waste total')
        water=cloud.get('water_consumption',{});require(water.get('unit') in ['L','m3'],'ENV-001',ident,'Water quantity needs a supported unit');number(water.get('value'),'ENV-008',ident,Decimal(0))
        selected=number(cloud['scope2_'+basis.replace('-','_')+'_kgco2e'],'ENV-002',ident)
        cloud_values[ident]=selected+number(cloud['total_scope3_kgco2e'],'ENV-003',ident)
    rows=unique(data.get('rows',[]),'ENV-005','rows');require(bool(rows),'ENV-008','rows','No emissions records')
    groups=set();scopes={};calculated=[];used_clouds=set();allocated_cloud_total=Decimal(0)
    for ident,row in rows.items():
        evidence(row.get('evidence'),known,'ENV-001',ident)
        require(row.get('object') and row.get('lifecycle_stage') and row.get('overlap_group'),'ENV-005',ident,'Object/lifecycle/overlap boundary missing')
        require(row['overlap_group'] not in groups,'ENV-005',ident,'Overlapping emissions group');groups.add(row['overlap_group'])
        require(row.get('period',boundary['period'])==boundary['period'] and row.get('boundary_id',boundary['id'])==boundary['id'],'ENV-006',ident,'Row boundary/period differs')
        scope=row.get('organization_scope');require(scope in ['Scope 1','Scope 2','Scope 3'],'ENV-005',ident,'Invalid organization Scope')
        allocation=number(row.get('allocation'),'ENV-001',ident,Decimal(0),Decimal(1));value=mass(row.get('value'),row.get('unit'),ident)
        if row.get('cloud_ref'):
            ref=row['cloud_ref'];require(ref in clouds and ref not in used_clouds,'ENV-005',ident,'Unknown or duplicate provider report');used_clouds.add(ref)
            cloud=clouds[ref];expected=cloud_values[ref]*allocation
            equipment=number(cloud['digital_equipment_scope3_kgco2e'],'ENV-003',ident)*allocation
            other='market-based' if basis=='location-based' else 'location-based';alternative=number(cloud['scope2_'+other.replace('-','_')+'_kgco2e'],'ENV-002',ident)*allocation
            if equipment and value==expected+equipment:raise RuleError('ENV-003',ident,'Equipment subset counted twice')
            if alternative and value==expected+alternative:raise RuleError('ENV-002',ident,'Both Scope2 alternatives added')
            require(value==expected,'ENV-001',ident,'Cloud amount disagrees with declared basis and allocation')
            require(scope=='Scope 3','ENV-005',ident,'Purchased service belongs to customer organization Scope3 in this contract')
            require(data['rules'].get('cloud'),'ENV-001','rules','Cloud allocation rule must be declared')
            allocated_cloud_total+=value
        elif 'activity' in row:
            require(row.get('factor_ref') in factors,'ENV-001',ident,'Unknown factor ID');factor=factors[row['factor_ref']]
            evidence(factor.get('evidence'),known,'ENV-001',factor['id']);require(factor.get('origin'),'ENV-001',factor['id'],'Factor origin missing')
            require(row.get('activity_unit')==factor.get('denominator_unit'),'ENV-001',ident,'Activity and factor units differ')
            applies=factor.get('applicability',{})
            same=factor.get('period')==boundary['period'] and factor.get('geography')==boundary['geography']
            if not same:
                require(boundary['period'] in applies.get('periods',[]) and boundary['geography'] in applies.get('geographies',[]),'ENV-006',factor['id'],'Factor time/geography is not applicable')
                evidence(applies.get('evidence'),known,'ENV-006',factor['id'])
            expected=number(row['activity'],'ENV-008',ident,Decimal(0))*mass(factor.get('value'),factor.get('numerator_unit'),factor['id'])*allocation
            require(value==expected,'ENV-001',ident,'Activity × factor × allocation differs from supplied amount')
        scopes[scope]=scopes.get(scope,Decimal(0))+value
        calculated.append({'id':ident,'value':float(value),'unit':'kgCO2e','scope':scope,'lifecycle_stage':row['lifecycle_stage'],'evidence':row['evidence']})
    if 'Scope 1' not in scopes:
        require(boundary.get('scope1_status')=='zero-with-evidence','ENV-008',boundary['id'],'Missing Scope1 is not automatically zero')
        evidence(boundary.get('scope1_evidence'),known,'ENV-008',boundary['id'])
    gross=sum(scopes.values(),Decimal(0));offsets=data.get('offsets',{})
    require(offsets.get('treatment')=='separate-no-deduction','ENV-004','offsets','Offsets must remain separate')
    organization=offsets.get('organization',{});evidence(organization.get('evidence'),known,'ENV-004','offsets')
    org_offset=mass(organization.get('value'),organization.get('unit'),'offsets')
    # A separately supplied provider disclosure is not deducted from gross
    # emissions; nevertheless its quantity must satisfy the same numeric contract.
    if 'provider' in offsets:
        provider=offsets['provider']
        require(isinstance(provider,dict),'ENV-004','offsets.provider','Provider offsets must be a structured quantity')
        mass(provider.get('value'),provider.get('unit'),'offsets.provider')
    if 'reported_gross' in data:require(mass(data['reported_gross'],data.get('reported_gross_unit','kgCO2e'),'reported-gross')==gross,'ENV-004','reported-gross','Gross cannot deduct offsets')
    result={'gross_kgco2e':float(gross),'scope2_kgco2e':float(scopes.get('Scope 2',0)),'scope3_kgco2e':float(scopes.get('Scope 3',0)),'scope1_kgco2e':float(scopes.get('Scope 1',0)),
            'offsets_separate_kgco2e':float(org_offset),'provider_offsets_separate_kgco2e':float(sum((Decimal(str(clouds[i]['carbon_credits_offsets_kgco2e'])) for i in used_clouds),Decimal(0))),
            'cloud_kgco2e':float(allocated_cloud_total),'rows':calculated,'scope2_basis':basis,'coverage':boundary['coverage_status'],
            'notice':'Sum of declared mutually exclusive rows, not independent proof of inventory completeness. Factors and allocation are project evidence, not TOGAF defaults.'}
    prior=data.get('prior_year')
    if prior:
        evidence(prior.get('evidence'),known,'ENV-005','comparison')
        require(prior.get('boundary_id')==boundary['id'] and prior.get('scope2_basis')==basis and prior.get('functional_unit')==boundary['functional_unit'] and prior.get('lifecycle_rule')==boundary['lifecycle_rule'],'ENV-005','comparison','Comparison boundaries, basis or lifecycle rules differ')
        require(prior.get('period')!=boundary['period'] and prior.get('period_kind')=='year' and prior.get('value_basis')=='full-year','ENV-006','comparison','Comparable distinct full-year period required')
        ids=prior.get('row_ids',[]);values=prior.get('rows',[])
        require(len(ids)==len(values)==len(set(ids)) and set(ids)==set(rows),'ENV-005','comparison','Comparison row identities differ')
        old=sum((mass(v,prior.get('unit'),'comparison') for v in values),Decimal(0))
        result.update(prior_gross_kgco2e=float(old),change_kgco2e=float(gross-old),change_percent=float((gross-old)/old*100) if old else None,
                      percentage_status='defined' if old else 'undefined-zero-baseline')
    return result
