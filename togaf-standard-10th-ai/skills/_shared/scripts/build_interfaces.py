"""Maintainer utility: derive the shared schema/registry from reviewed artifact contracts."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def write(name,data): (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    current=ROOT/"schemas/model.schema.json"
    if current.exists() and json.loads(current.read_text()).get("properties",{}).get("schema_version",{}).get("const")=="2.0":
        raise SystemExit("此脚本是 v1 接口生成器，禁止覆盖 v2。维护 v2 Schema、metamodel 和 capabilities 注册后运行验证与迁移测试。")
    arts=json.loads((ROOT/'artifacts.json').read_text())['artifacts']
    # Directed endpoint contracts; inverse verbal readings do not create additional edges.
    definitions={
    'constrains':('constraint','*','约束限制对象'), 'located_at':('environment application technology hardware actor','location','对象位于地点'),
    'connects_to':('environment location technology','environment location technology','基础连接'),
    'governs':('principle standard','*','原则或标准治理对象'),
    'specifies':('requirement','*','需求规定架构对象'), 'traces_to':('*','*','显式追溯，具体理由记录在 label'),
    'decomposes':('capability function','capability function','整体分解为同类型部分'),
    'defines':('term','information data_entity','术语定义业务概念'), 'synonym_of':('term','term','同义词'),
    'realizes':('function technology sbb','business_service technology_service abb','实现规定的服务或构建块'),
    'measured_by':('*','measure','对象由指标衡量'), 'commits_to':('contract','business_service requirement','合同承诺服务或要求'),
    'motivates':('driver','goal','驱动促成目标'), 'refines':('goal','objective','目标细化为目的'),
    'member_of':('actor','organization','参与者属于组织'), 'triggers':('event','process activity business_service','事件触发行为'),
    'produces':('process activity','event product','行为产出事件或产品'), 'controls':('control','process activity','控制约束行为'),
    'assigned_to':('role','actor activity','职责分配；端点须按 label 明确'), 'concerned_with':('stakeholder','*','利益相关者关注对象'),
    'has_stage':('value_stream','value_stage','价值流具有阶段'), 'precedes':('value_stage','value_stage','价值阶段先后'),
    'supports_function':('application','function','应用支撑功能'), 'exposes':('application','interface','应用提供接口'),
    'consumes':('application','interface','应用消费接口'), 'stored_in':('data_entity','data_component','数据由组件存储'),
    'implements_standard':('technology','standard','技术遵循标准'), 'plays':('actor','role','参与者承担角色'),
    'used_by':('application','organization','组织使用、拥有或运营应用，code 区分'),
    'business_interaction':('organization','organization','提供方向接收方交换服务或产品'),
    'owned_by':('capability','organization','能力责任或贡献，code 区分'),
    'used_in_function':('data_entity','function','功能对数据操作，code 为列功能执行的 CRUD'),
    'uses_application':('actor role','application','主体使用应用，不等于授权'),
    'requires_capability':('goal objective','capability','目标需要能力'),
    'enabled_by':('value_stream value_stage','capability','价值流或阶段由能力使能'),
    'communicates_with':('application','application','应用向另一应用发起通信'),
    'accesses':('application process','data_entity','应用或处理访问数据'),
    'runs_on':('application','technology','应用部署于或依赖技术，code 区分'),
    'delivers':('work_package','outcome','工作包交付成果'), 'enables_benefit':('outcome','benefit','成果使能收益；因果为待验证假设'),
    'contributes_to':('benefit','objective','收益贡献目的'), 'supports_capability':('function application','capability','实现要素支撑能力'),
    'business_dependency':('business_model_element','business_model_element','业务模式要素之间的依赖'),
    'produces_information':('business_service','information','业务服务提供信息'),
    'consumes_information':('business_service','information','业务服务消费信息'),
    'participates':('actor','business_use_case application_use_case','参与者参与用例'),
    'data_association':('data_entity','data_entity','概念数据实体业务关联'),
    'served_by':('objective','business_service','目的由业务服务支撑'),
    'information_association':('information','information','信息概念关系'),
    'reports_to':('organization','organization','下级向上级汇报'),
    'collaborates_with':('organization','organization','组织协作，记录方向或双方语义'),
    'flows_to':('activity process','activity process decision','控制流'),
    'branches':('decision','activity process','有条件分支'),
    'has_activity':('process','activity','流程包含活动'),
    'automated_by':('process activity','application','应用自动或辅助实现行为'),
    'transitions_to':('product_state data_state','product_state data_state','状态转换，label 写触发或条件'),
    'in_scope':('project','actor application organization','项目范围内对象'),
    'external_dependency':('project','actor application organization','项目外部依赖'),
    'supports_activity':('value_chain_activity','value_chain_activity','支持价值链活动'),
    'replaced_by':('application','application','现有应用被另一应用替换'),
    'migrated_by':('application','work_package','应用由工作包迁移'),
    'provided_by':('application_use_case','application','用例由应用提供'),
    'processing_step':('application','application','场景中有序处理消息'),
    'deployed_on':('software_module','technology','软件部署于节点'),
    'depends_on':('software_module work_package','software_module work_package','对象依赖目标作为前置'),
    'implements_interface':('software_module','interface','模块实现接口'),
    'replicated_to':('data_component','data_component','数据组件间复制'),
    'migration_flow':('data_component migration_step','data_component migration_step','迁移流或转换步骤'),
    'protected_by':('data_entity data_component','control','数据由控制保护'),
    'authorized_for':('actor','data_entity','经证据支持的访问授权'),
    'crosses_boundary':('data_component','trust_zone','数据处理跨信任边界'),
    'logical_association':('logical_entity','logical_entity','逻辑实体关联'),
    'managed_by':('technology','management_service','技术组件受管理服务管理'),
    'network_connects':('technology network_zone','technology network_zone','有向网络通信'),
    'member_of_zone':('technology hardware','network_zone','节点属于网络区'),
    'hardware_connects':('hardware','hardware','硬件连接'),
    'contains':('platform','technology','平台组成'),
    'changes':('change_request','requirement','变更修改需求'),
    'affects':('requirement change_request','*','有证据或待验证的影响'),
    'mitigates':('control','risk','控制降低风险'),
    'satisfies':('abb sbb application technology work_package','requirement','实现或工作成果满足需求'),
    'addresses_gap':('work_package','gap','工作包处理差距')}
    missing=set(r for a in arts for r in a['relationship_types'])-definitions.keys();assert not missing,missing
    write('relationships.json',{'schema_version':'1.0','notice':'项目有向关系词汇；不是官方完整元模型。','relationships':{k:{'source_types':s.split(),'target_types':t.split(),'meaning':m} for k,(s,t,m) in definitions.items()}})
    ctx={'type':'object','additionalProperties':False,'required':['domains','landscape','purpose','abstraction','evolution'],'properties':{
        'domains':{'type':'array','minItems':1,'uniqueItems':True,'items':{'enum':['business','data','application','technology']}},
        'landscape':{'enum':['strategic','segment','capability']},'purpose':{'enum':['strategy','portfolio','project','solution-delivery']},
        'abstraction':{'enum':['context','conceptual','logical','physical']},'evolution':{'enum':['baseline','transition','target']}}}
    refarray={'type':'array','uniqueItems':True,'items':{'type':'string','minLength':1}}
    identity={'id':{'type':'string','pattern':'^[a-zA-Z0-9][a-zA-Z0-9_.-]*$'},'name':{'type':'string','minLength':1},'type':{'type':'string','minLength':1}}
    provenance={'evidence':refarray,'certainty':{'enum':['confirmed','assumed','uncertain']}}
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:togaf-skills:model:1.0','title':'TOGAF skill collection project model','type':'object','additionalProperties':False,
    'required':['schema_version','project','sources','entities','relationships','views','deliverables','gaps'],
    'properties':{
      'schema_version':{'const':'1.0'},'project':{'type':'object','additionalProperties':False,'required':['id','name','version','context','is_example','decision_status'],'properties':{**identity,'version':{'type':'string','minLength':1},'context':ctx,'is_example':{'type':'boolean'},'decision_status':{'enum':['candidate','approved','realized']},'approval_evidence':refarray}},
      'sources':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','kind','description'],'properties':{'id':identity['id'],'kind':{'enum':['user','official','local-translation','figure-interpretation','assumption','example']},'description':{'type':'string','minLength':1},'locator':{'type':'string'}}}},
      'entities':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','name','type','attributes','evidence','certainty'],'properties':{**identity,**provenance,'concept_id':{'type':'string'},'context':ctx,'attributes':{'type':'object'},'evolution':{'enum':['baseline','transition','target']},'decision_status':{'enum':['candidate','approved','realized']},'approval_evidence':refarray}}},
      'relationships':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','type','source','target','label','evidence','certainty'],'properties':{'id':identity['id'],'type':identity['type'],'source':{'type':'string'},'target':{'type':'string'},'label':{'type':'string','minLength':1},**provenance,'codes':refarray,'attributes':{'type':'object'},'cardinality':{'type':'object','required':['source','target'],'additionalProperties':False,'properties':{'source':{'enum':['one','zero-or-one','many','one-or-more','unknown']},'target':{'enum':['one','zero-or-one','many','one-or-more','unknown']}}}}}},
      'views':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','artifact_id','title','context','entity_ids','relationship_ids','analysis','legend'],'properties':{'id':identity['id'],'artifact_id':{'enum':[a['id'] for a in arts]},'title':{'type':'string','minLength':1},'context':ctx,'entity_ids':refarray,'relationship_ids':refarray,'analysis':{'type':'string','minLength':1},'legend':{'type':'string','minLength':1},'allow_mixed_evolution':{'type':'boolean'}}}},
      'deliverables':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','deliverable_id','title','view_ids','entity_ids','sections','decision_status'],'properties':{'id':identity['id'],'deliverable_id':{'enum':[d['id'] for d in json.loads((ROOT/'deliverables.json').read_text())['deliverables']]},'title':{'type':'string','minLength':1},'view_ids':refarray,'entity_ids':refarray,'sections':{'type':'object','additionalProperties':{'type':'string','minLength':1}},'decision_status':{'enum':['candidate','approved','realized']},'approval_evidence':refarray}}},
      'gaps':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','description','impact','needed_input'],'properties':{'id':identity['id'],'description':{'type':'string','minLength':1},'impact':{'type':'string','minLength':1},'needed_input':{'type':'string','minLength':1},'owner':{'type':'string'}}}},
      'extensions':{'type':'object','additionalProperties':False,'properties':{'entity_types':{'type':'object','additionalProperties':{'type':'string','minLength':1}},'relationship_types':{'type':'object','additionalProperties':{'type':'object','required':['source_types','target_types','meaning'],'properties':{'source_types':refarray,'target_types':refarray,'meaning':{'type':'string','minLength':1}},'additionalProperties':False}}}},
      'comparisons':{'type':'array','items':{'type':'object','additionalProperties':False,'required':['id','baseline_ids','target_ids','basis','gap_ids','transition_checks'],'properties':{'id':identity['id'],'baseline_ids':refarray,'target_ids':refarray,'basis':{'type':'string','minLength':1},'gap_ids':refarray,'transition_checks':{'type':'object','required':['operations','data_consistency','dependencies','controls','rollback'],'additionalProperties':{'type':'string','minLength':1}}}}}
    }}
    write('schemas/model.schema.json',schema)
if __name__=='__main__':main()
