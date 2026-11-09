"""Curated project routing of all 71 G249 Table 5-2 human competencies.

The source names/levels remain official transcriptions. These task examples,
existing-method routes and observable outputs are project inferences, not claims
that generating an artifact demonstrates a person's competence.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# source identity suffix | task | existing methods | existing artifacts | observable work evidence
ROWS = '''
application:artificial-intelligence-ai-and-expert-systems|为预测或规则推理应用定义目标、失效条件与人工处置|bi-model-operating-monitoring-method,bi-requirement-origin-boundary-method|bi-requirements-profile,options-decision-matrix|带适用数据、错误成本、监控和人工退出条件的方案评审
application:application-development|把业务需求分解为可验收应用变更并评审实现约束|microservice-boundary-method,solution-delivery-notebook-review|software-engineering-diagram,solution-delivery-notebook|需求到接口规格及验收测试的追溯和独立代码/设计评审
application:application-modeling|表达应用边界、职责和交互以支持方案决定|microservice-boundary-method,msa-contract-consumer-evidence-method|application-communication-diagram,application-function-matrix|模型对象与实际应用接口逐项核对的评审记录
application:application-security|识别应用信任边界、威胁及控制要求|business-risk-assessment,solution-delivery-notebook-review|security-blueprint,security-impact-analysis|威胁到控制及验证结果的追溯，注明残余风险责任方
application:integration-and-interoperability|判断应用接口协议、语义及异常交互是否兼容|msa-contract-consumer-evidence-method,metadata-integration-tradeoff|interface-catalog,interoperability-assessment|消费者契约、失败重试和兼容性验证证据
application:optimistic-pessimistic-patterns|先澄清来源技能名在本项目中的专业含义，再定义适用任务|option-weighted-decision|options-decision-matrix|专业定义来源与采用记录；未经定义不得给出技能评级
application:programming|审查代码原型能否满足架构约束和接口行为|solution-delivery-notebook-review,product-constraint-conformance-review|software-engineering-diagram,solution-delivery-notebook|有版本的代码、运行测试和专业评审；架构图不能替代编程实绩
application:micro-macro-service-oriented-architecture-soa|选择服务边界、契约和生命周期治理安排|microservice-boundary-method,msa-federated-governance-process-method|microservice-decomposition-method,soa-layered-reference|服务拆分依据、消费者证据和治理例外评审
business:budget-management|为架构工作分配预算并解释估算和变更偏差|architecture-project-scheduling,project-highlight-review|architecture-project-schedule,project-status-highlight-report|预算基线、估算假设及实际偏差的核对记录
business:business-capability-modeling|按业务成果定义稳定能力及分解边界|capability-decomposition-method,capability-instance-gap-method|business-capability-map,capability-increment-analysis|能力定义与重复/遗漏边界的业务评审
business:business-case|比较架构选择的价值、成本、风险及不行动后果|option-weighted-decision,benefit-realization-trigger|options-decision-matrix,ea-value-map|带假设、收益责任人和敏感性解释的商业论证
business:business-culture|识别行为习惯对变革采纳和协作的限制|dtra-readiness-method,scenario-elicitation|digital-readiness-assessment,business-scenario-document|访谈证据、相反观察与采纳障碍解释
business:business-information-management|识别业务信息责任、用途和共享规则|metadata-requirement-method,mdm-identity-analysis|information-map,metadata-policy-documentation|信息定义、使用场景及责任人确认
business:business-metrics|将业务目的转为有口径和观测来源的度量|business-attribute-evaluation,smart-objective-review|business-attribute-profile,balanced-scorecard|度量口径、基线、目标来源与采样核对
business:business-process-design|设计角色、事件、活动和控制组成的目标流程|scenario-elicitation,value-stream-definition-method|process-flow-diagram,process-event-control-product-catalog|场景走查、异常分支和控制有效性评审
business:business-process-management|建立流程运行监测、责任和改进闭环|business-attribute-evaluation,benefit-realization-trigger|process-flow-diagram,business-attribute-profile|运行指标、异常处置及改进前后可比证据
business:business-scenario|从原始叙述识别问题、参与者和可验证结果|scenario-elicitation,scenario-traceability-review|business-scenario-document,scenario-traceability-matrix|原料到问题和需求的可追溯转换及反例
business:business-service-development|定义服务受益人、价值、契约和支撑能力|value-stream-definition-method,ea-service-emergence-npd-method|business-service-function-catalog,contract-measure-catalog|服务边界、质量承诺与消费者验收
business:integration-and-sharing|确定跨业务单元共享能力和协作边界|operating-model-submodel-analysis-method,domain-architecture-alignment-review|business-interaction-matrix,operating-model|共享与本地差异的业务决策依据及交接责任
business:legacy-management|比较保留、替换和演进既有资产的后果|option-weighted-decision,technical-debt-register-method|application-portfolio-catalog,technical-debt-register|遗留依赖、迁移约束和延迟处置成本的证据
business:organization-design|对齐组织职责、协作和能力归属|operating-model-submodel-analysis-method,architecture-role-catalog-review|organization-map,capability-organization-matrix|组织边界、能力责任和冲突处置的确认记录
business:role-design|从任务需求设计可裁剪角色和责任交接|architecture-role-catalog-review,architecture-role-skill-assessment|architecture-role-catalog,actor-role-matrix|岗位/角色/任务区别及权限、协作、技能要求追溯
business:security-and-asset-management|确定业务资产的价值、保护责任和控制需求|business-risk-assessment,domain-architecture-alignment-review|security-classification-scheme,security-domain-model|资产分类、责任方和控制适用性评审
business:strategic-planning|将战略选择转换为能力与变革优先项|architecture-backlog-trace-review,work-package-prioritization|strategy-capability-matrix,architecture-backlog|战略到能力和工作包的因果假设及取舍记录
business:visioning|建立利益相关者可共同评审的目标愿景|scenario-elicitation,ea-point-of-view-review|solution-concept-diagram,ea-point-of-view-register|愿景边界、相反意见及共识/未决项记录
change:managing-change|识别变革影响、采纳障碍与沟通支持需求|dtra-readiness-method,project-management-strategy-review|readiness-consequence-analysis,project-management-strategy|影响群体、就绪证据与分阶段应对记录
change:value-management|追踪变革收益目标、责任与实现条件|benefit-realization-trigger,business-attribute-evaluation|value-realization-assessment,benefits-diagram|收益基线、观测及复评触发，区分相关和归因
change:work-package-management|分解架构工作并协调依赖、资源和验收|architecture-project-scheduling,dependency-topological-order|architecture-project-wbs,architecture-project-schedule|依赖、资源期间、工作量和验收责任核对
change:governance-of-change|确定变更决策权、合规检查与例外处置|change-profile-governance-review,product-constraint-conformance-review|architecture-governance-checklist,non-compliance-disposition|有权限来源的决定、例外期限及跟进证据
data:analytical-data|定义分析数据语义、质量和用途边界|bi-requirement-origin-boundary-method,bi-value-chain-controls-method|bi-requirements-profile,metadata-dictionary|指标到原始数据与质量控制的追溯
data:big-data|根据规模、时效和资源条件评审数据处理架构|bi-transition-method,metadata-integration-tradeoff|processing-diagram,bi-transition-architecture|真实容量/延迟测量、分布方案取舍及运行边界
data:data-governance|建立数据责任、质量规则和决策机制|metadata-requirement-method,metadata-application-coverage-review|metadata-policy-documentation,data-quality-assessment|规则到责任与观测的对应及违规处置记录
data:data-integration|对齐数据源、身份、转换和交换语义|metadata-integration-tradeoff,mdm-identity-analysis|metadata-integration-model,mdm-exchange-pattern|字段映射、冲突样例和接口验证结果
data:data-migration|设计数据切换、核对、退出及回退条件|transition-operability-check,bi-stage-operability-and-exit-method|data-migration-diagram,rollback-plan|迁移前后数量/语义核对和回退演练结果
data:data-modeling|建立实体、关系和约束以回答业务问题|metadata-requirement-method,mdm-identity-analysis|conceptual-data-diagram,logical-data-diagram|模型业务定义、边界反例及独立评审
data:data-security|确定数据分类、访问、保护及生命周期控制|business-risk-assessment,metadata-requirement-method|data-security-diagram,security-classification-scheme|敏感数据流、访问规则和控制测试证据
data:master-data-management|设计主数据身份、主记录及冲突仲裁|mdm-identity-analysis,mdm-match-merge-arbitration-method|customer-mdm-model,mdm-integration-style|匹配误差、来源优先级与可取消合并的评审
data:operational-data|明确业务运行数据的一致性、时效和责任|msa-data-distribution-conditions-method,metadata-requirement-method|data-lifecycle-diagram,data-usage-documentation|更新来源、失效窗口和异常恢复验证
architecture:broad-and-focused-perspective|选择整体与局部架构视角并解释决策边界|domain-architecture-alignment-review,architecture-description-formality-review-method|architecture-landscape-projection,project-context-diagram|跨域影响与局部细节取舍的审查记录
architecture:broad-generic-modeling|选用适合关注点的抽象、对象和关系|reference-model-tailoring,architecture-description-formality-review-method|building-block-description,viewpoint-library|模型语义、关注点覆盖和抽象遗漏的验证
architecture:decision-making|基于约束、备选与证据形成可复议决定|option-weighted-decision,decision-delegation-register-method|options-decision-matrix,decision-delegation-register|被淘汰选项、证据冲突、权限与复议条件
architecture:generic-integration-and-interoperability|检查业务、数据、应用和技术的跨域一致性|domain-architecture-alignment-review,metadata-integration-tradeoff|interoperability-assessment,domain-architecture-alignment|跨域接口、语义和治理依赖的联合评审
architecture:generic-standards-and-regulations|判断标准与法规在本范围的适用性和冲突|product-constraint-conformance-review,reference-model-tailoring|technology-standards-catalog,applicable-legislation-register|版本、司法/组织范围与适用性专业确认
architecture:principle-definition|为架构选择定义有理由和后果的原则|ea-point-of-view-review,product-constraint-conformance-review|principles-catalog,product-constraint-register|原则理由、影响及冲突例外决策证据
architecture:road-mapping|组织目标、过渡、依赖和可运营退出条件|dependency-topological-order,transition-operability-check|transition-architecture-model,architecture-project-schedule|依赖与过渡验收/回退条件的核对
architecture:strategy-into-architecture|把战略意图落实到能力、需求与构建块|architecture-backlog-trace-review,capability-instance-gap-method|strategy-capability-matrix,building-block-description|战略到能力增量和工作包的稳定ID追溯
architecture:viewpoints-and-views|从受众关注点制定视点并验证视图充分性|architecture-description-formality-review-method,reference-model-tailoring|viewpoint-library,architecture-description-formality-review|受众、关注点、构造规则与评审结论
generic:influencing|使架构建议在决策者语境中得到理解和处置|ea-point-of-view-review|ea-point-of-view-register,stakeholder-influence-matrix|沟通后的异议、采纳决定和实际影响记录
generic:inter-personal|处理架构协作中的分歧与信任问题|scenario-elicitation,agile-collaboration-selection-switch|stakeholder-catalog,organization-map|真实协作观察、分歧处理及对方反馈
generic:leadership|组织共同方向、责任与复杂事项升级|architecture-role-catalog-review,project-management-strategy-review|architecture-role-catalog,project-management-strategy|目标澄清、授权边界及团队结果的行为证据
generic:logical-analysis|检查假设、推理与结论之间的有效联系|scenario-traceability-review,option-weighted-decision|scenario-traceability-matrix,options-decision-matrix|可复算/可复核推理和反例处置
generic:oral-communication|向指定受众解释架构取舍并回应问题|ea-point-of-view-review,scenario-elicitation|ea-point-of-view-register,business-scenario-document|现场讲解、问答、受众理解反馈；演示文件本身不够
generic:risk-management|识别架构风险、应对及剩余风险接受条件|business-risk-assessment,incident-architecture-adjustment-review|business-risk-register,risk-mitigation-plan|风险依据、控制效果、残余风险与责任方记录
generic:stakeholder-management|识别关注点、影响与参与决策方式|scenario-elicitation,ea-point-of-view-review|stakeholder-catalog,stakeholder-influence-matrix|参与记录、关注点变化与未决冲突跟踪
generic:teamwork|协调跨角色共同产出和交接责任|agile-collaboration-selection-switch,architecture-role-catalog-review|organization-map,actor-role-matrix|共同任务、交接验收、同事反馈与异常协作记录
generic:training|设计能力学习活动并验证实际应用|architecture-role-skill-assessment|architecture-development-plan|可观察学习目标、实践产出和独立复评；出席不等于能力
generic:written-communication|写出受众可采取行动且可追溯的架构说明|ea-point-of-view-review,project-highlight-review|ea-point-of-view-register,project-status-highlight-report|真实文稿、读者反馈和误解修订记录
technology:data-center|评审计算设施的容量、可用性和演进条件|transition-operability-check,sustainability-option-review|environments-and-locations-diagram,technology-portfolio-catalog|容量与故障演练测量、设施边界和运维确认
technology:device|评审终端设备的接入、生命周期与兼容需求|product-constraint-conformance-review,reference-model-tailoring|technology-portfolio-catalog,networked-computing-hardware-diagram|真实设备约束、兼容测试及维护责任
technology:integration-and-interoperability|检查技术协议和平台之间的连接与兼容性|product-constraint-conformance-review,reference-model-tailoring|network-and-communications-diagram,interoperability-assessment|协议/版本兼容和故障模式验证
technology:location-security-and-directory-services|评审位置服务、身份目录和访问控制边界|business-risk-assessment,product-constraint-conformance-review|data-security-diagram,security-services-catalog|目录职责、授权规则、服务依赖和控制测试
technology:network-topology|设计满足业务流量与故障隔离需求的拓扑|reference-model-tailoring,transition-operability-check|network-and-communications-diagram,networked-computing-hardware-diagram|拓扑选择依据、流量和故障域验证
technology:networks|评审网络容量、协议、延迟和运营条件|transition-operability-check,product-constraint-conformance-review|network-and-communications-diagram,technology-standards-catalog|网络测量、协议约束和运维故障处理记录
technology:operating-systems-and-services|确定操作系统及平台服务的支持与兼容边界|product-constraint-conformance-review,transition-operability-check|platform-decomposition-diagram,technology-portfolio-catalog|版本支持、补丁约束、恢复和兼容性验证
technology:physical-security|判断场地和设施实体防护是否满足风险需求|business-risk-assessment|environments-and-locations-diagram,security-blueprint|现场控制、访问流程与专业检查记录
legal:contracts|识别架构相关合同义务、责任和约束|product-constraint-conformance-review,solution-delivery-notebook-review|contract-measure-catalog,applicable-legislation-register|具体合同条款、适用主体及法务确认；不能自动出具法律意见
legal:data-protection|识别数据处理目的、地域和保护义务|business-risk-assessment,metadata-requirement-method|applicable-legislation-register,data-security-diagram|实际数据处理活动、适用法规版本与法务确认
legal:fraud-and-fair-dealing|识别欺诈和公平交易风险及控制责任|business-risk-assessment,scenario-traceability-review|business-risk-register,applicable-control-framework-register|具体交易场景、风险证据和专业合规复核
legal:procurement|将采购规则与供应商/产品选择约束对应|option-weighted-decision,product-constraint-conformance-review|applicable-legislation-register,product-constraint-register|适用采购程序、利益冲突、选择理由和授权记录
legal:risk|评审架构决定造成的法律责任与处置选择|business-risk-assessment,incident-architecture-adjustment-review|business-risk-register,security-impact-analysis|责任范围、风险后果及法务意见，不以通用风险分代替
legal:rules-and-regulations|确认架构范围内规则法规的适用与持续更新|product-constraint-conformance-review,domain-architecture-alignment-review|applicable-legislation-register,applicable-control-framework-register|有版本和适用地区的条款、控制映射及变更复核
'''


def build():
    source = json.loads((ROOT / 'corpus/architecture/roles/skills.json').read_text())['G249']
    declared = {}
    for line in ROWS.strip().splitlines():
        key, task, methods, artifacts, behavior = line.split('|')
        identity = 'G249:skill:' + key
        if identity in declared:
            raise ValueError('Duplicate routing identity: ' + identity)
        declared[identity] = dict(task_example_zh=task, method_ids=methods.split(','), artifact_ids=artifacts.split(','), observable_evidence_zh=behavior)
    official = {s['id']: s for s in source['skills']}
    if set(declared) != set(official) or len(official) != 71:
        raise ValueError('Routing must match all 71 official source identities exactly')
    registry = json.loads((ROOT / 'capabilities.json').read_text())
    methods = {r['id'] for r in registry['analysis_methods']}
    artifacts = {r['id'] for r in registry['work_products']} | {r['id'] for r in json.loads((ROOT / 'artifacts.json').read_text())['artifacts']}
    rows = []
    for sid, src in official.items():
        inferred = declared[sid]
        if set(inferred['method_ids']) - methods or set(inferred['artifact_ids']) - artifacts:
            raise ValueError('Unregistered route for ' + sid)
        unresolved = src['label_en'] == 'Optimistic/ Pessimistic Patterns'
        conditional = []
        if sid.endswith(':generic:training'):
            conditional.append({'artifact_id': 'security-training-plan', 'when_zh': '仅当本次学习任务涉及安全教育，且已声明安全目标与受众时选择'})
        if sid.endswith(':technology:physical-security'):
            conditional.append({'method_id': 'sustainability-option-review', 'when_zh': '仅在实体防护选项另需比较环境影响，且具备相应环境数据时作为辅助方法；不用于判定门禁或实体安全有效性'})
        rows.append({'skill_id': sid, 'source_name_en': src['label_en'], 'category_en': src['category_en'],
                     'official': {'origin': 'source-transcription', 'evidence': src['evidence'],
                                  'reference_proficiencies': dict(zip((r['id'] for r in source['role_columns']), src['values'])),
                                  'scale_id': 'G249-table5-1'},
                     'mapping_origin': 'project-derived-task-routing-not-official-prescription',
                     'conditional_routes': conditional,
                     'definition_status': 'source-name-unresolved' if unresolved else 'source-name-with-project-task-example',
                     'sources_needed': ['专业词义来源及组织采用记录；G249未定义此术语，不自行展开为并发控制模式'] if unresolved else
                                       ['本项目实际工作产出、独立观察/评审及适用专业方法；G249矩阵不提供这些证据'],
                     'boundary_zh': '生成制品只支持架构任务；不能证明人员熟练度、赋予组织权限或替代专业实现/法律判断。',
                     **inferred})
    return {'schema_version': 'g249-skill-task-routing/1', 'source': 'G249 Table 5-2; §§2–6', 'skill_count': 71,
            'notice_zh': '71项人的能力映射到现有方法与制品，不建立71个AI技能；任务路由、行为证据建议均为项目推导。', 'skills': rows}


def markdown(data):
    lines = ['# G249 全部 71 项技能的任务与制品映射', '', data['notice_zh'], '',
             '官方技能名、角色参考等级和页码/原表格坐标保存在 [JSON](skill-task-map.json)。下表中的任务、路由和行为证据是项目推导；不会由生成制品自动认定人员能力。具体执行与缺口规则见 [运行契约](runtime-contract.md)。', '',
             '| 官方技能（类别） | 项目任务示例 | 复用方法 | 复用制品 | 所需可观察证据 |', '|---|---|---|---|---|']
    for row in data['skills']:
        name = row['source_name_en'] + '（' + row['category_en'] + '）'
        if row['definition_status'] == 'source-name-unresolved':
            name += ' **词义待专业来源确认**'
        methods = '<br>'.join('`' + identity + '`' for identity in row['method_ids'])
        artifacts = '<br>'.join('`' + identity + '`' for identity in row['artifact_ids'])
        lines.append('| ' + ' | '.join([name, row['task_example_zh'], methods, artifacts, row['observable_evidence_zh']]) + ' |')
        for conditional in row.get('conditional_routes', []):
            lines.append('| 条件辅助路由 | ' + conditional['when_zh'] + ' | ' + conditional.get('method_id','—') + ' | ' + conditional.get('artifact_id','—') + ' | 不作为默认选项 |')
    lines += ['', '每项还需本项目真实工作产出、独立观察或专业评审；适用法律、技术实现、人员认可和组织授权不由本表替代。源文仅列出 Optimistic/ Pessimistic Patterns，未定义其含义，必须保留原名与待补来源。', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    path = ROOT / 'references/g249/skill-task-map.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    path.with_suffix('.md').write_text(markdown(data))
    print(path)
