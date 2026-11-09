# F · 迁移规划

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 架构路线图、工作包与过渡架构
- 资源、预算、业务周期及实施项目约束

## 工作与治理门

1. 与组合和项目管理协调实施优先级
2. 评估收益、资源、成本、风险与依赖
3. 确定项目、负责人、日期和验收条件
4. 完善迁移计划与治理交接
5. 取得适当的资源与实施计划决定

- priorities-resources：优先级、预算和资源有来源；不足之处已处理
- dependencies-schedule：项目顺序、依赖、起止日期和负责人一致
- migration-continuity：切换、共存、数据核对、回退及过渡退出条件明确
- governance-handoff：实施责任、架构约束与验收/治理交接明确

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-roadmaps|架构路线图|phase-contract-output-candidate|application-migration-diagram, data-migration-diagram, benefits-diagram|
|implementation-migration-plan|实施与迁移计划|phase-contract-output-candidate|application-migration-diagram, data-migration-diagram|
|implementation-governance-model|实施治理模型（if any）|phase-contract-output-candidate|role-catalog, actor-role-matrix|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|application-migration-diagram|应用迁移图|diagram|project-owner-routing-candidate|application-gap-dependency, compat-application-migration-diagram|
|implementation-factor-catalog|实施因素目录|catalog|project-owner-routing-candidate|implementation-factor-catalog-default, c220-implementation-factor-catalog|
|consolidated-gaps-solutions-dependencies-matrix|合并差距、方案和依赖矩阵|matrix|project-owner-routing-candidate|c220-consolidated-gaps-solutions-dependencies-matrix|
|architecture-definition-increments-table|架构定义增量表|matrix|project-owner-routing-candidate|c220-architecture-definition-increments-table|
|transition-architecture-state-evolution-table|过渡架构状态演进表|matrix|source-artifact-phase-list|c220-transition-architecture-state-evolution-table|
|business-value-risk-matrix|业务价值与风险矩阵|matrix|source-artifact-phase-list|c220-business-value-risk-matrix|
|rollback-plan|回退计划|report|project-owner-routing-candidate|rollback-plan-default|
|portfolio-theme-work-package-register|组合主题工作包分组|catalog|project-owner-routing-candidate|portfolio-theme-work-package-register-default|
|portfolio-estimate-sufficiency-check|组合估算充分性检查|catalog|project-owner-routing-candidate|portfolio-estimate-sufficiency-check-default|
|project-work-package-authorization|项目工作包授权记录|catalog|project-owner-routing-candidate|project-work-package-authorization-default|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_10_03_01|10.3.1. Confirm Management Framework Interactions for the Implementation and Migration Plan|本阶段|迁移计划需在业务规划、EA、项目组合、运营管理四框架的计划中反映。|
|C220-web-2025:02-architecture-development-method#tag_10_03_02|10.3.2. Assign a Business Value to Each Work Package|本阶段|工作包价值必须先定义组织价值及测量方法，再应用到项目增量。|
|C220-web-2025:02-architecture-development-method#tag_10_03_03|10.3.3. Estimate Resource Requirements, Project Timings, and Availability/Delivery Vehicle|本阶段|资源时间与成本按项目及增量估计，资本投入和运营维护须分开。|
|C220-web-2025:02-architecture-development-method#tag_10_03_04|10.3.4. Prioritize the Migration Projects by Conducting a Cost/Benefit Assessment and Risk Assessment|本阶段|迁移排序比较全部SBB净收益、交付成本和已计入风险并取得相关方共识。|
|C220-web-2025:02-architecture-development-method#tag_10_03_05|10.3.5. Confirm Architecture Roadmap and Update Architecture Definition Document|本阶段|F更新路线图/过渡间隔并按项目整合能力增量交付物。|
|C220-web-2025:02-architecture-development-method#tag_10_03_06|10.3.6. Complete the Implementation and Migration Plan|本阶段|完整迁移计划整合项目活动、依赖和变更影响，过渡架构作组合里程碑。|
|C220-web-2025:02-architecture-development-method#tag_10_03_07|10.3.7. Complete the Architecture Development Cycle and Document Lessons Learned|本阶段|F结束架构开发并将治理移交架构实现。|

来源摘要：G186 §§4.1.2–4.1.3, 5.2.2；C220 ADM 10

具体原文节与定位保留在mapping.json及adm-phases.json。
