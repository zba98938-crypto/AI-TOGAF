"""Build an explicit reviewed package; never mutate the central registries."""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from evidence_analysis import scenario_transformation_evidence
def read(path): return json.loads(path.read_text())
def write(path, obj): path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
CAP = read(ROOT/'capabilities.json')
KEYS = {'business-attribute-profile':'togaf-addenda:g152-bap', 'scenario-traceability-matrix':'togaf-addenda:g176-scenario', 'environment-lifecycle-accounting':'togaf-addenda:g242-accounting'}
CALCS = {'business-attribute-profile':'business-attribute-evaluation', 'scenario-traceability-matrix':'scenario-traceability-review', 'environment-lifecycle-accounting':'environmental-annual-accounting'}
ARTS = {'business-attribute-profile':'business-attribute-profile', 'scenario-traceability-matrix':'scenario-traceability-matrix', 'environment-lifecycle-accounting':'environmental-is-assessment'}
package = {'package_id':'evidence-work-products','version':'1.0','work_products':[], 'profiles':[], 'analysis_methods':[], 'default_profiles':{},'candidate_resolutions':[]}

def supplemental(ident, name, data, refs):
    return {'id':ident,'type':'repository_asset','name':name,'attributes':data,'evidence':refs,'certainty':'assumed'}

def view(model, ident, artifact, profile, title, es, rs, analysis_id):
    return {'id':ident,'artifact_id':artifact,'profile_id':profile,'title':title,'entity_ids':es,'relationship_ids':rs,
            'analysis':'原始陈述、分析规则和修改记录均保留稳定引用；计算只采用显式项目规则。',
            'legend':'虚构图书馆案例。空白矩阵格为未确认；相邻/包含不代表额外关系；规则和数值不是TOGAF默认值。',
            'context':copy.deepcopy(model['project']['context']),'attributes':{'analysis_ids':[analysis_id]}}

def promote(ident, state):
    base=ROOT/'examples/addenda'/ident
    model=read(base/(state+'-model.json'))
    data=copy.deepcopy(model['extension_data'][KEYS[ident]])
    case=read(base/'case.json')
    aid=ARTS[ident];analysis_id='analysis-'+ident
    # The exact source inventory is part of the calculator input, not an implicit global.
    data['source_ids']=[s['id'] for s in model['sources']]
    if ident=='business-attribute-profile':
        entity=model['entities'][0]
        entity['attributes']=copy.deepcopy({k:v for k,v in data.items() if k not in ['attribute_id','source_ids']})
        entity['attributes']['unit']=data['metric']['unit']
        entity['attributes']['observation']={'numerator':data['metric']['numerator'],'denominator':data['metric']['denominator'],'period':data['metric']['period']}
        model['views']=[view(model,'library-bap',aid,'business-attribute-profile-default','业务属性画像：定义、规则与观测',[entity['id']],[],analysis_id),
                        view(model,'library-bap-trace',aid,'business-attribute-profile-trace','业务属性—业务目标—要求—控制追溯',[e['id'] for e in model['entities']],[r['id'] for r in model['relationships']],analysis_id)]
    elif ident=='scenario-traceability-matrix':
        data['work_product_ids']=['scenario-baseline']
        order=['process','stakeholder','actor','application','problem','goal']
        for entity in model['entities']:
            if entity['id']=='app-payment':entity['name']='统一支付台';entity['attributes']['definition']='仅替换取消退款流程的计算机参与者；受理预约保持原系统'
        es=[e['id'] for typ in order for e in model['entities'] if e['type']==typ];main=[r['id'] for r in data['associations']];outcome=[r['id'] for r in data['painpoint_outcomes']]
        audit=[]
        for record in case['raw_records']:
            audit.append(supplemental('raw-'+record['id'],'原始陈述 '+record['id'],{'record_kind':'raw','raw_id':record['id'],'text':record['text'],'preservation':'immutable'},[record['id']]))
        for record in data['normalized_records']:
            audit.append(supplemental(record['id'],'规范条目 '+record['id'],{'record_kind':'normalized',**record},[record['from']]))
        provenance=scenario_transformation_evidence(data)
        for record in data['transformation_log']:
            audit.append(supplemental(record['id'],'转换步骤 '+record['id'],{'record_kind':'transformation',**record},provenance[record['id']]))
        for record in data['derived_requirements']:
            audit.append(supplemental(record['id'],'派生要求 '+record['id'],{'record_kind':'derived-requirement',**record},record['evidence']))
        model['entities'].extend(audit)
        model['views']=[view(model,'library-scenario',aid,'scenario-traceability-matrix-default','流程与五类场景要素关联',es,main,analysis_id),
                        view(model,'library-scenario-outcomes',aid,'scenario-painpoint-outcome-matrix','问题与预期结果关联',data['categories']['problem']+data['categories']['objective'],outcome,analysis_id),
                        view(model,'library-scenario-audit',aid,'scenario-transformation-audit','原始材料、规范化、转换与派生要求',[e['id'] for e in audit],[],analysis_id)]
    else:
        data['cloud_record']['scope1']={'status':'zero-with-evidence','evidence':['E-R4']}
        data['prior_year'].update(period_kind='year',value_basis='full-year',lifecycle_rule=data['boundary']['lifecycle_rule'])
        for entity,row in zip(model['entities'],data['rows']):
            entity['attributes']=copy.deepcopy(row)
            entity['attributes'].update(year=int(data['boundary']['period']),scope=row['organization_scope'],period_kind=data['boundary']['period_kind'],value_basis=data['boundary']['value_basis'],boundary_id=data['boundary']['id'])
        extra=[]
        for key in ['boundary','factor','cloud_record','prior_year','offsets','rules']:
            record=copy.deepcopy(data[key]); refs=record.get('evidence',record.get('source_refs',data['rules']['source_refs']))
            extra.append(supplemental('accounting-'+key,key,{'record_kind':key,**record},refs))
        rowids=[e['id'] for e in model['entities']];model['entities'].extend(extra)
        model['views']=[view(model,'library-environment',aid,'annual-environmental-accounting','年度环境核算：生命周期与组织Scope',rowids,[],analysis_id),
                        view(model,'library-environment-basis',aid,'environmental-accounting-basis','核算边界、因子、云报告、对比与抵消',[e['id'] for e in extra],[],analysis_id)]
    model['analyses']=[{'id':analysis_id,'method_id':CALCS[ident],'inputs':data,'evidence':data['source_ids']}]
    model['extension_data']['togaf-addenda:case']['render_acceptance']='production-input-awaiting-execution'
    write(base/('production-'+state+'-model.json'),model)
    return model

def example(model,v):
    es=set(v['entity_ids']);rs=set(v['relationship_ids'])
    return {'notice':'虚构图书馆完整案例；数据与阈值不是TOGAF规定。','sources':model['sources'],
            'entities':[e for e in model['entities'] if e['id'] in es], 'relationships':[r for r in model['relationships'] if r['id'] in rs],
            'analyses':model['analyses'],'view':v}

for ident,key in KEYS.items():
    spec=read(ROOT/'capability-addenda'/(ident+'.json'))
    models={state:promote(ident,state) for state in ['baseline','modified']};model=models['baseline'];aid=ARTS[ident]
    old=copy.deepcopy(next(x for x in CAP['work_products'] if x['id']==aid))
    refs={'business-attribute-profile':['G152 §5.10.1; English PDF40–41'], 'scenario-traceability-matrix':['G176 §3.2.3; English PDF22–23','G176 §11.4; English PDF45–46'], 'environment-lifecycle-accounting':['G242 §3.6, §3.6.1–3.6.3; Figure3-10','G242 Chapter6; English PDF98–99']}[ident]
    old.update(source_refs=refs,kind='catalog' if ident!='scenario-traceability-matrix' else 'matrix',
               entity_types=sorted({e['type'] for e in model['entities']}),
               required_inputs=spec['required_inputs'],missing_input_policy=spec['missing_input_policy'],
               analysis_steps=spec['analysis_steps'],misreadings=spec['misreadings'],
               example=example(model,model['views'][0]),
               method_reference='references/capability-addenda/'+ident+'.md',
               operational_contract='capability-addenda/'+ident+'.json',
               implementation_status={'definition':'source-checked-with-recorded-translation-limitations','model':'production-contract','analysis':'calculator-pending-tests','generation':'pending','modification':'pending','review':'pending','visual':'pending'})
    old['semantic_checks']=list(dict.fromkeys(old['semantic_checks']+[x['rule'] if isinstance(x,dict) else x for x in spec['quality_checks']]))
    if ident=='business-attribute-profile':
        fields=list(model['entities'][0]['attributes']);old.update(fields=fields,required_attributes={'business_attribute':fields})
    if ident=='environment-lifecycle-accounting':
        fields=['year','scope','object','lifecycle_stage','unit','value','allocation','evidence','overlap_group','boundary_id','period_kind','value_basis'];old.update(fields=fields,required_attributes={'environment_measure':fields})
    package['work_products'].append(old)
    for v in model['views']:
        matrix=v['id'] in ['library-scenario','library-scenario-outcomes']
        if v['id']=='library-scenario':types=['process','stakeholder','actor','application','problem','goal'];template={'row_types':['process'],'column_types':['stakeholder','actor','application','problem','goal']}
        elif matrix:types=['problem','goal'];template={'row_types':['problem'],'column_types':['goal']}
        else:types=sorted({e['type'] for e in model['entities'] if e['id'] in v['entity_ids']});template={}
        template.update(source_verified=False,layout_notes='依据正文语义的项目操作表单；没有对应原图，不标记为原图复刻。' if ident!='environment-lifecycle-accounting' else '年度核算表采用图3-10的对象与生命周期维度，精确图形等价仍未验收。',review_status='source-semantics-reviewed-project-form')
        required={t:old['required_attributes'][t] for t in types if t in old['required_attributes']}
        profile={'id':v['profile_id'],'artifact_id':aid,'name':v['title'],'name_zh':v['title'],'owner':spec['owner'],
                 'renderer':'matrix' if matrix else 'catalog','output_kind':'diagram' if matrix else 'table','version':'2.1',
                 'source_refs':refs,'source_structure_refs':[],'entity_types':types,'relationship_types':['traces_to'] if v['relationship_ids'] else [],
                 'required_attributes':required,'checks':[x['rule'] if isinstance(x,dict) else x for x in spec['quality_checks']],
                 'definition_status':'source-semantics-with-project-operational-form','template':template,
                 'example':example(model,v),'method_reference':old['method_reference']}
        package['profiles'].append(profile)
    # Keep the established default environment profile reachable and semantically equal.
    if ident=='environment-lifecycle-accounting':
        default=copy.deepcopy(next(p for p in package['profiles'] if p['id']=='annual-environmental-accounting'))
        default['id']='environmental-is-assessment-default';default['alias_of']='annual-environmental-accounting';default['counting_role']='compatibility-alias';default['example']['view']['profile_id']=default['id'];default['example']['view']['id']='environment-default-example';package['profiles'].append(default)
    package['default_profiles'][aid]=model['views'][0]['profile_id']
    method={'id':ident if ident=='environment-lifecycle-accounting' else CALCS[ident], 'name':old['name'],'owner':spec['owner'],'source_refs':refs,
            'required_inputs':spec['required_inputs'],'missing_input_policy':spec['missing_input_policy'],'analysis_steps':spec['analysis_steps'],
            'output_work_products':[aid],'calculator_id':CALCS[ident],'checks':[x['rule'] if isinstance(x,dict) else x for x in spec['quality_checks']],
            'definition_status':'source-method-with-explicit-project-rule-contract','implementation_status':'production-calculator-pending-tests',
            'example_model':'examples/addenda/'+ident+'/production-baseline-model.json','method_reference':old['method_reference']}
    package['analysis_methods'].append(method)

write(ROOT/'capability-addenda/evidence-work-products.json',package)
print('Prepared package:',len(package['work_products']),'work products,',len(package['profiles']),'profiles,',len(package['analysis_methods']),'methods')
