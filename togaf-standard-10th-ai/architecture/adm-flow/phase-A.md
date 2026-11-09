# A · 架构愿景

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 架构工作请求及可复用的上层架构
- 业务驱动、目标、利益相关者、能力与约束

## 工作与治理门

1. 界定架构项目问题、广度、规划期和使用目的
2. 识别利益相关者、关注点与上层约束
3. 评估团队能力、业务风险和可行性
4. 探索各域候选目标的概要价值与工作量
5. 形成工作说明与沟通安排并取得继续推进的决定

- scope-purpose：问题、范围、规划期与业务周期位置清楚
- stakeholders-constraints：利益相关者、关注点及上层架构约束已确认
- value-effort-risk：目标摘要、价值、工作量、风险及置信度限制可供利益相关者判断
- work-capability：工作说明、资源与团队能力足以开展本次架构工作

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-requirements-specification|架构需求规格|registry-phase-context|requirements-catalog, constraints-catalog|
|architecture-vision|架构愿景|phase-contract-output-candidate|stakeholder-catalog, project-context-diagram, solution-concept-diagram, benefits-diagram|
|business-goals-objectives|业务目标与目的|registry-phase-context|driver-goal-objective-catalog, goal-objective-service-diagram|
|business-principles|业务原则|registry-phase-context|principles-catalog|
|business-drivers|业务驱动因素|registry-phase-context|driver-goal-objective-catalog|
|capability-assessment|能力评估|phase-contract-output-candidate|business-capability-map, capability-organization-matrix|
|communications-plan|沟通计划|phase-contract-output-candidate|stakeholder-catalog|
|request-for-architecture-work|架构工作请求|phase-contract-output-candidate|project-context-diagram, driver-goal-objective-catalog|
|statement-of-work|架构工作说明书|phase-contract-output-candidate|project-context-diagram, stakeholder-catalog|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|stakeholder-catalog|利益相关者目录|catalog|source-artifact-phase-list|compat-stakeholder-catalog|
|business-capability-map|业务能力地图|diagram|source-artifact-phase-list|capability-classification, capability-decomposition, capability-gap-heatmap, compat-business-capability-map|
|business-model-diagram|业务模式图|diagram|source-artifact-phase-list|business-model-canvas, business-model-baseline-target, compat-business-model-diagram|
|project-context-diagram|项目语境图|diagram|project-owner-routing-candidate|compat-project-context-diagram|
|value-chain-diagram|价值链图|diagram|source-artifact-phase-list|porter-value-chain, compat-value-chain-diagram|
|value-stream-map|价值流地图|diagram|source-artifact-phase-list|value-stream-definition, value-stream-enabling-capabilities, value-stream-capability-heatmap, compat-value-stream-map|
|solution-concept-diagram|解决方案概念图|diagram|source-artifact-phase-list|compat-solution-concept-diagram|
|business-scenario-document|业务场景文档|report|project-owner-routing-candidate|business-scenario-document-default|
|scenario-traceability-matrix|业务场景关联矩阵|matrix|project-owner-routing-candidate|scenario-traceability-matrix-default, scenario-painpoint-outcome-matrix, scenario-transformation-audit|
|architecture-project-wbs|架构项目工作分解|diagram|project-owner-routing-candidate|architecture-project-wbs-default|
|architecture-project-schedule|架构项目资源与进度|diagram|project-owner-routing-candidate|architecture-project-schedule-default, agile-ea-development, agile-solution-collaboration, agile-cross-development, agile-cross-functional|
|stakeholder-influence-matrix|利益相关者影响力与影响程度矩阵|diagram|project-owner-routing-candidate|stakeholder-influence-matrix-default|
|project-management-strategy|架构项目管理策略|catalog|project-owner-routing-candidate|project-management-strategy-default|
|project-status-highlight-report|架构项目状态要点报告|catalog|project-owner-routing-candidate|project-status-highlight-report-default|
|domain-architecture-alignment|领域架构融入整体EA核对|catalog|project-owner-routing-candidate|domain-architecture-alignment-default|
|business-scenario-checklist-record|业务场景步骤清单与角色记录|catalog|project-owner-routing-candidate|business-scenario-checklist-record-default|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_03_03_01|3.3.1. Establish the Architecture Project|本阶段|架构循环通常按企业项目管理处理，可独立或嵌入较大项目。|
|C220-web-2025:02-architecture-development-method#tag_03_03_02|3.3.2. Identify Stakeholders, Concerns, and Business Requirements|本阶段|相关方识别同时产生候选愿景要求、候选范围和沟通表达因素。|
|C220-web-2025:02-architecture-development-method#tag_03_03_03|3.3.3. Confirm and Elaborate Business Goals, Business Drivers, and Constraints|本阶段|业务目标驱动和企业/项目约束须当前且清楚。|
|C220-web-2025:02-architecture-development-method#tag_03_03_04|3.3.4. Evaluate Capabilities|本阶段|能力评估区分开发/消费架构的EA能力与企业基线/目标业务能力。|
|C220-web-2025:02-architecture-development-method#tag_03_03_05|3.3.5. Assess Readiness for Business Transformation|本阶段|变更就绪评估按因素分析/评级，可定量组织变更准备程度。|
|C220-web-2025:02-architecture-development-method#tag_03_03_06|3.3.6. Define Scope|本阶段|范围区分基线与目标内外，二者细节不必相同。|
|C220-web-2025:02-architecture-development-method#tag_03_03_07|3.3.7. Confirm and Elaborate Architecture Principles, including Business Principles|本阶段|A重新确认架构及业务原则的时效和含义。|
|C220-web-2025:02-architecture-development-method#tag_03_03_08|3.3.8. Develop Architecture Vision|本阶段|愿景先决定整体域交付物如何组合，再以相关方关切形成高层基线/目标。|
|C220-web-2025:02-architecture-development-method#tag_03_03_09|3.3.9. Define the Target Architecture Value Propositions and KPIs|本阶段|价值主张应逐相关方组形成，并纳入工作说明书跟踪。|
|C220-web-2025:02-architecture-development-method#tag_03_03_10|3.3.10. Identify the Business Transformation Risks and Mitigation Activities|本阶段|风险区分缓解前初始等级与实施缓解后的剩余等级。|
|C220-web-2025:02-architecture-development-method#tag_03_03_11|3.3.11. Develop Statement of Architecture Work; Secure Approval|本阶段|工作说明书将工作产品、性能、变更影响、资源依赖、时间与沟通连接到授权。|

来源摘要：G186 §§5.2.1–5.2.2, 6.1, 15.2.1；C220 ADM 3

具体原文节与定位保留在mapping.json及adm-phases.json。
