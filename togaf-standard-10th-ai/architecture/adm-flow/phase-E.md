# E · 机会与解决方案

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 跨域目标、差距、架构需求与依赖
- 约束、候选实现、组织就绪度及价值预期

## 工作与治理门

1. 整合跨域差距及解决方案选择
2. 将差距分配到可解释的工作包
3. 评估复用、购买、开发等方案的约束与权衡
4. 定义可运营的过渡架构及依赖
5. 形成架构路线图与迁移策略

- gap-work-package：工作包覆盖所选择差距并追溯价值与约束
- options：候选方案的可行性与取舍有证据
- transitions-dependencies：过渡状态具有运营、数据、控制、依赖及回退条件
- roadmap：路线图说明各工作包的价值、工作量、风险和相互依赖

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-building-blocks|架构构建块|registry-phase-context|requirements-catalog, solution-concept-diagram|
|architecture-definition-document|架构定义文档|phase-contract-output-candidate|business-capability-map, conceptual-data-diagram, application-communication-diagram, platform-decomposition-diagram|
|architecture-roadmaps|架构路线图|phase-contract-output-candidate|application-migration-diagram, data-migration-diagram, benefits-diagram|
|capability-assessment|能力评估|registry-phase-context|business-capability-map, capability-organization-matrix|
|solution-building-blocks|解决方案构建块|phase-contract-output-candidate|application-portfolio-catalog, technology-portfolio-catalog|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|benefits-diagram|收益图|diagram|source-artifact-phase-list|compat-benefits-diagram|
|project-context-diagram|项目语境图|diagram|source-artifact-phase-list|compat-project-context-diagram|
|implementation-factor-catalog|实施因素目录|catalog|source-artifact-phase-list|implementation-factor-catalog-default, c220-implementation-factor-catalog|
|consolidated-gaps-solutions-dependencies-matrix|合并差距、方案和依赖矩阵|matrix|source-artifact-phase-list|c220-consolidated-gaps-solutions-dependencies-matrix|
|architecture-definition-increments-table|架构定义增量表|matrix|source-artifact-phase-list|c220-architecture-definition-increments-table|
|options-decision-matrix|备选方案决策矩阵|assessment|project-owner-routing-candidate|options-decision-matrix-default, delivery-style-assessment, set-based-options-iteration, agile-pattern-selection|
|capability-increment-analysis|能力增量分析|assessment|project-owner-routing-candidate|capability-increment-analysis-default, capability-change-overlay|
|building-block-description|构建块描述|report|project-owner-routing-candidate|building-block-description-default, building-block-content-model, product-function-component-interface|
|transition-architecture-model|过渡架构模型|diagram|project-owner-routing-candidate|transition-architecture-model-default, transition-building-block-trace|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_09_03_01|9.3.1. Determine/Confirm Key Corporate Change Attributes|本阶段|企业文化和单位/企业转型能力形成实施因素。|
|C220-web-2025:02-architecture-development-method#tag_09_03_02|9.3.2. Determine Business Constraints for Implementation|本阶段|业务驱动可约束实施顺序。|
|C220-web-2025:02-architecture-development-method#tag_09_03_03|9.3.3. Review and Consolidate Gap Analysis Results from Phases B to D|本阶段|综合差距、方案与依赖矩阵连接四域差距、候选SBBs和相关ABBs。|
|C220-web-2025:02-architecture-development-method#tag_09_03_04|9.3.4. Review Consolidated Requirements Across Related Business Functions|本阶段|跨业务功能要求整合寻找更有效的最小要求集及共享解法。|
|C220-web-2025:02-architecture-development-method#tag_09_03_05|9.3.5. Consolidate and Reconcile Interoperability Requirements|本阶段|互操作冲突应跨业务数据应用技术四域解决。|
|C220-web-2025:02-architecture-development-method#tag_09_03_06|9.3.6. Refine and Validate Dependencies|本阶段|依赖支撑实施排序、协调、项目分组和增量时间。|
|C220-web-2025:02-architecture-development-method#tag_09_03_07|9.3.7. Confirm Readiness and Risk for Business Transformation|本阶段|E复核A就绪评估对路线图与策略的影响。|
|C220-web-2025:02-architecture-development-method#tag_09_03_08|9.3.8. Formulate Implementation and Migration Strategy|本阶段|实施迁移策略可全新、革命切换或演化收敛。|
|C220-web-2025:02-architecture-development-method#tag_09_03_09|9.3.9. Identify and Group Major Work Packages|本阶段|主要工作包按综合差距因素逻辑分组，再分增量/项目组合。|
|C220-web-2025:02-architecture-development-method#tag_09_03_10|9.3.10. Identify Transition Architectures|本阶段|过渡架构是增量路径的明确目标并须具可测业务价值。|
|C220-web-2025:02-architecture-development-method#tag_09_03_11|9.3.11. Create the Architecture Roadmap & Implementation and Migration Plan|本阶段|E草稿路线图展示基线到目标工作包/过渡时序，迁移计划展示实现所需活动。|

来源摘要：G186 §§5.2.2, 6.3.3–6.3.4；G248 §§3–6；C220 ADM 9

具体原文节与定位保留在mapping.json及adm-phases.json。
