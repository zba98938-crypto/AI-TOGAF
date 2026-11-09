# B · 业务架构

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 当前架构愿景、业务需求与约束
- 可复用业务基线、参考模型及其他域的影响

## 工作与治理门

1. 选择回应关注点的业务视点
2. 形成同口径的目标与最低必要基线
3. 识别能力、价值流、组织、服务及流程差距
4. 分析差距所需工作、价值、成本和风险
5. 解决跨域影响并提交目标评审

- viewpoints：视图回应已识别业务关注点
- baseline-target-gaps：业务基线与目标可比较，保留、改变、移除和未知明确
- work-value：差距、所需工作、价值、成本及风险可追溯
- cross-domain：其他域、过渡状态及在建项目影响已处理

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-building-blocks|架构构建块|phase-contract-output-candidate|requirements-catalog, solution-concept-diagram|
|architecture-definition-document|架构定义文档|phase-contract-output-candidate|business-capability-map, conceptual-data-diagram, application-communication-diagram, platform-decomposition-diagram|
|architecture-requirements-specification|架构需求规格|phase-contract-output-candidate|requirements-catalog, constraints-catalog|
|business-goals-objectives|业务目标与目的|registry-phase-context|driver-goal-objective-catalog, goal-objective-service-diagram|
|capability-assessment|能力评估|registry-phase-context|business-capability-map, capability-organization-matrix|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|location-catalog|位置目录|catalog|source-artifact-phase-list|compat-location-catalog|
|business-capabilities-catalog|业务能力目录|catalog|source-artifact-phase-list|compat-business-capabilities-catalog|
|business-glossary-catalog|业务术语表目录|catalog|source-artifact-phase-list|compat-business-glossary-catalog|
|business-service-function-catalog|业务服务/功能目录|catalog|source-artifact-phase-list|compat-business-service-function-catalog|
|contract-measure-catalog|合同/度量目录|catalog|source-artifact-phase-list|compat-contract-measure-catalog|
|driver-goal-objective-catalog|驱动因素/目标/目的目录|catalog|source-artifact-phase-list|compat-driver-goal-objective-catalog|
|organization-actor-catalog|组织/参与者目录|catalog|source-artifact-phase-list|compat-organization-actor-catalog|
|process-event-control-product-catalog|流程/事件/控制/产品目录|catalog|source-artifact-phase-list|compat-process-event-control-product-catalog|
|role-catalog|角色目录|catalog|source-artifact-phase-list|compat-role-catalog|
|value-stream-catalog|价值流目录|catalog|source-artifact-phase-list|compat-value-stream-catalog|
|value-stream-stages-catalog|价值流阶段目录|catalog|source-artifact-phase-list|compat-value-stream-stages-catalog|
|actor-role-matrix|参与者/角色矩阵|matrix|source-artifact-phase-list|compat-actor-role-matrix|
|business-interaction-matrix|业务交互矩阵|matrix|source-artifact-phase-list|compat-business-interaction-matrix|
|capability-organization-matrix|能力/组织矩阵|matrix|source-artifact-phase-list|compat-capability-organization-matrix|
|strategy-capability-matrix|战略/能力矩阵|matrix|source-artifact-phase-list|compat-strategy-capability-matrix|
|value-stream-capability-matrix|价值流/能力矩阵|matrix|source-artifact-phase-list|compat-value-stream-capability-matrix|
|benefits-diagram|收益图|diagram|project-owner-routing-candidate|compat-benefits-diagram|
|business-capability-map|业务能力地图|diagram|source-artifact-phase-list|capability-classification, capability-decomposition, capability-gap-heatmap, compat-business-capability-map|
|business-event-diagram|业务事件图|diagram|source-artifact-phase-list|compat-business-event-diagram|
|business-footprint-diagram|业务足迹图|diagram|source-artifact-phase-list|capability-strategy-overlay, compat-business-footprint-diagram|
|business-model-diagram|业务模式图|diagram|project-owner-routing-candidate|business-model-canvas, business-model-baseline-target, compat-business-model-diagram|
|business-service-information-diagram|业务服务/信息图|diagram|source-artifact-phase-list|compat-business-service-information-diagram|
|business-use-case-diagram|业务用例图|diagram|source-artifact-phase-list|compat-business-use-case-diagram|
|functional-decomposition-diagram|功能分解图|diagram|source-artifact-phase-list|metadata-business-function-map, compat-functional-decomposition-diagram, metadata-application-function-map|
|goal-objective-service-diagram|目标/目的/服务图|diagram|source-artifact-phase-list|compat-goal-objective-service-diagram|
|information-map|信息地图|diagram|source-artifact-phase-list|information-concept-network, information-capability-use-modify, information-aggregation-generalization, compat-information-map, information-concept-object-meaning|
|organization-decomposition-diagram|组织分解图|diagram|source-artifact-phase-list|compat-organization-decomposition-diagram|
|organization-map|组织地图|diagram|source-artifact-phase-list|organization-work-network, organization-capability-overlay, compat-organization-map|
|process-flow-diagram|流程图|diagram|source-artifact-phase-list|compat-process-flow-diagram|
|product-lifecycle-diagram|产品生命周期图|diagram|source-artifact-phase-list|compat-product-lifecycle-diagram|
|value-chain-diagram|价值链图|diagram|project-owner-routing-candidate|porter-value-chain, compat-value-chain-diagram|
|value-stream-map|价值流地图|diagram|source-artifact-phase-list|value-stream-definition, value-stream-enabling-capabilities, value-stream-capability-heatmap, compat-value-stream-map|
|capability-instance-model|能力实例组成模型|diagram|project-owner-routing-candidate|capability-instance-model-default, capability-instance-composition|
|customer-journey|客户旅程|diagram|project-owner-routing-candidate|customer-journey-default|
|customer-persona|客户画像|report|project-owner-routing-candidate|customer-persona-default|
|architecture-skill-matrix|架构技能／角色矩阵|diagram|project-owner-routing-candidate|architecture-skill-matrix-default, ea-skill-role-proficiency|
|architecture-development-plan|架构人员发展计划|report|project-owner-routing-candidate|architecture-development-plan-default|
|government-reference-tailoring|政府参考模型裁剪|report|project-owner-routing-candidate|government-reference-tailoring-default, government-reference-catalog-overlay|
|digital-business-reference-tailoring|数字业务参考模型裁剪|report|project-owner-routing-candidate|digital-business-reference-tailoring-default, dbrm-element-applicability, dbrm-digital-perspective-map, dbrm-adm-content-map, dbrm-content-domain-map, dbrm-landscape-map, digital-enablement-competency-overlay|
|value-network|价值网络|diagram|project-owner-routing-candidate|value-network-default|
|lean-value-stream|精益价值流|diagram|project-owner-routing-candidate|lean-value-stream-default|
|four-box-business-model|四框业务模型|diagram|project-owner-routing-candidate|four-box-business-model-default|
|business-model-cube|业务模型立方体|diagram|project-owner-routing-candidate|business-model-cube-default|
|operating-model|运营模式|diagram|project-owner-routing-candidate|operating-model-default, operating-model-four-submodels|
|balanced-scorecard|平衡计分卡目标与成果|diagram|project-owner-routing-candidate|balanced-scorecard-default|
|sustainability-education-plan|数字可持续教育与技能计划|catalog|project-owner-routing-candidate|sustainability-education-plan-default|
|architecture-role-catalog|架构角色定义目录|catalog|project-owner-routing-candidate|architecture-role-catalog-default, architecture-role-collaboration, architecture-work-assignment-review, architecture-work-assignment-map|
|smart-objective-assessment|SMART目的评估|catalog|project-owner-routing-candidate|smart-objective-assessment-default|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_04_03_01|4.3.1. Select Reference Models, Viewpoints, and Tools|本阶段|按业务驱动和相关方关切选业务参考、视点和工具。|
|C220-web-2025:02-architecture-development-method#tag_04_03_02|4.3.2. Develop Baseline Business Architecture Description|本阶段|业务基线只深入到支持目标所需程度。|
|C220-web-2025:02-architecture-development-method#tag_04_03_03|4.3.3. Develop Target Business Architecture Description|本阶段|目标业务描述细节以支持愿景为准。|
|C220-web-2025:02-architecture-development-method#tag_04_03_04|4.3.4. Perform Gap Analysis|本阶段|业务差距分析先核查模型一致性准确性与需求完整。|
|C220-web-2025:02-architecture-development-method#tag_04_03_05|4.3.5. Define Candidate Roadmap Components|本阶段|初始业务路线图为后续活动排序并支撑E的跨域整合。|
|C220-web-2025:02-architecture-development-method#tag_04_03_06|4.3.6. Resolve Impacts Across the Architecture Landscape|本阶段|业务架构需检查整个景观的双向影响及复用机会。|
|C220-web-2025:02-architecture-development-method#tag_04_03_07|4.3.7. Conduct Formal Stakeholder Review|本阶段|正式相关方复核以原动机和工作说明书检验业务方案用途。|
|C220-web-2025:02-architecture-development-method#tag_04_03_08|4.3.8. Finalize the Business Architecture|本阶段|Finalize完成每个业务块标准描述、决策理由与最终追溯及工作产品。|
|C220-web-2025:02-architecture-development-method#tag_04_03_09|4.3.9. Create/Update the Architecture Definition Document|本阶段|定义文档的业务部分按预定范围用途正式化。|

来源摘要：G186 §§5.2.2, 6.3, 15.2.1；C220 ADM 4

具体原文节与定位保留在mapping.json及adm-phases.json。
