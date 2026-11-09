# 预备阶段 · 架构能力

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 企业语境、架构能力目的与期望
- 现有治理、组织职责、架构资产与其他管理框架

## 工作与治理门

1. 定义受影响企业及架构能力范围
2. 确定赞助、治理、角色及能力缺口
3. 裁剪方法、元模型、原则与工具
4. 建立资产存储、维护与度量机制

- capability-scope：EA 服务目的、范围、角色和资源已明确
- governance：决策权、治理接口、原则及升级路径已明确
- method-repository：裁剪方法、内容元模型、工具与存储库可供架构项目使用

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-principles|架构原则|phase-contract-output-candidate|principles-catalog|
|architecture-repository|架构存储库|phase-contract-output-candidate|principles-catalog, technology-standards-catalog, requirements-catalog|
|business-principles|业务原则|registry-phase-context|principles-catalog|
|organization-model|企业架构组织模型|phase-contract-output-candidate|organization-map, role-catalog, actor-role-matrix|
|request-for-architecture-work|架构工作请求|registry-phase-context|project-context-diagram, driver-goal-objective-catalog|
|tailored-architecture-framework|裁剪后的架构框架|phase-contract-output-candidate|principles-catalog, requirements-catalog|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|principles-catalog|原则目录|catalog|source-artifact-phase-list|compat-principles-catalog|
|architecture-maturity-model|架构成熟度模型|assessment|project-owner-routing-candidate|architecture-maturity-model-default, acmm-elements-levels|
|architecture-maturity-scorecard|架构成熟度评分卡|assessment|project-owner-routing-candidate|architecture-maturity-scorecard-default, acmm-scorecard|
|digital-adoption-position|数字技术采用定位|diagram|project-owner-routing-candidate|digital-adoption-position-default, dtra-adoption-quadrant|
|digital-readiness-questionnaire|数字技术就绪度问卷|assessment|project-owner-routing-candidate|digital-readiness-questionnaire-default|
|digital-readiness-assessment|数字技术就绪度评估|assessment|project-owner-routing-candidate|digital-readiness-assessment-default|
|readiness-consequence-analysis|就绪度因素后果分析|diagram|project-owner-routing-candidate|readiness-consequence-analysis-default, dtra-factor-consequence|
|adoption-factor-progression|采用因素递进路线|diagram|project-owner-routing-candidate|adoption-factor-progression-default, dtra-factor-progression|
|ea-service-catalog|企业架构服务目录|catalog|project-owner-routing-candidate|ea-service-catalog-default, ea-service-emergence-npd, ea-service-adm-evidence-map, ea-service-adm-matrix, ea-service-adm-reference-matrix, ea-service-adm-reference-table|
|ea-value-map|EA 与企业价值地图|diagram|project-owner-routing-candidate|ea-value-map-default|
|ea-team-capacity-plan|EA 团队容量计划|report|project-owner-routing-candidate|ea-team-capacity-plan-default|
|enterprise-framework-alignment-catalog|企业框架接触与承诺目录|catalog|project-owner-routing-candidate|enterprise-framework-alignment-catalog-default|
|business-cycle-product-alignment|业务周期与工作产品时点|catalog|project-owner-routing-candidate|business-cycle-product-alignment-default|
|value-realization-assessment|价值实现评估|catalog|project-owner-routing-candidate|value-realization-assessment-default|
|project-learning-record|项目经验记录与教训报告|catalog|project-owner-routing-candidate|project-learning-record-log, project-learning-record-report|
|sustainability-capability-assessment|数字可持续性能力评估|catalog|project-owner-routing-candidate|sustainability-capability-assessment-default|
|ea-point-of-view-register|EA观点文件与影响经营登记|catalog|project-owner-routing-candidate|ea-point-of-view-register-default|
|architecture-repository-structure|架构存储库结构|diagram|project-owner-routing-candidate|architecture-repository-structure|
|architecture-landscape-projection|架构全景投影|diagram|project-owner-routing-candidate|architecture-landscape-projection|
|repository-state-view-tree|存储库状态与视图树|diagram|project-owner-routing-candidate|repository-state-view-tree|
|repository-parallel-candidates|存储库并行候选容器|diagram|project-owner-routing-candidate|repository-parallel-candidates|
|capability-project-continuum|能力与项目连续谱|diagram|project-owner-routing-candidate|capability-project-continuum|
|portfolio-stakeholder-concern-matrix|组合利益相关者×关注点矩阵|diagram|project-owner-routing-candidate|portfolio-stakeholder-concern-matrix|
|repository-target-baseline-comparison|存储库版本比较 Target → Baseline|diagram|project-owner-routing-candidate|repository-target-baseline-comparison, repository-baseline-target-comparison|
|dtra-adm-phase-alignment|DTRA因素与ADM阶段对齐|catalog|project-owner-routing-candidate|dtra-adm-phase-alignment-default|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_02_03_01|2.3.1. Scope the Enterprise Organizations Impacted|本阶段|受影响组织分核心、软、扩展企业、社区与相关治理范围。|
|C220-web-2025:02-architecture-development-method#tag_02_03_02|2.3.2. Confirm Governance and Support Frameworks|本阶段|架构框架决定集中/联邦、轻/重等治理形式及库要求。|
|C220-web-2025:02-architecture-development-method#tag_02_03_03|2.3.3. Define and Establish Enterprise Architecture Team and Organization|本阶段|EA团队建立要连接现有能力、工作差距、职责、预算与其他工作计划。|
|C220-web-2025:02-architecture-development-method#tag_02_03_04|2.3.4. Identify and Establish Architecture Principles|本阶段|架构原则依据业务原则并奠定架构治理基础。|
|C220-web-2025:02-architecture-development-method#tag_02_03_05|2.3.5. Tailor the TOGAF Framework and, if any, Other Selected Architecture Framework(s)|本阶段|框架裁剪有术语、流程和内容三条线。|
|C220-web-2025:02-architecture-development-method#tag_02_03_06|2.3.6. Develop a Strategy and Implementation Plan for Tools and Techniques|本阶段|工具策略涵盖管理、决策、工作坊、模型、办公产品、语言和库，不限于建模软件。|

来源摘要：G184 §§4–12；C220 ADM 2

具体原文节与定位保留在mapping.json及adm-phases.json。
