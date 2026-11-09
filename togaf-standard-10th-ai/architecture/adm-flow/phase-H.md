# H · 架构变更管理

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 已实施架构、预期价值和度量口径
- 运营测量、业务/技术变化、风险与反馈

## 工作与治理门

1. 比较实际价值与利益相关者偏好及预期
2. 识别变化触发、架构缺口及风险
3. 评估维护变更、局部迭代或新周期的影响
4. 取得继续、修改或启动新架构工作的决定
5. 更新存储库、需求基线及监测安排

- value-monitoring：实际价值测量与预期、口径及置信度限制可比较
- change-impact：变更触发与对架构/需求/项目的影响有证据
- cycle-disposition：维护、局部迭代或新 ADM 周期的选择有理由及决策权
- repository-feedback：资产、需求、版本和下次监测/评审已衔接

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-repository|架构存储库|phase-contract-output-candidate|principles-catalog, technology-standards-catalog, requirements-catalog|
|architecture-roadmaps|架构路线图|phase-contract-output-candidate|application-migration-diagram, data-migration-diagram, benefits-diagram|
|change-request|变更请求|phase-contract-output-candidate|requirements-impact-assessment|
|communications-plan|沟通计划|registry-phase-context|stakeholder-catalog|
|request-for-architecture-work|架构工作请求|phase-contract-output-candidate|project-context-diagram, driver-goal-objective-catalog|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|environmental-is-assessment|信息系统年度环境评估|catalog|project-owner-routing-candidate|environmental-is-assessment-default, annual-environmental-accounting, sustainability-causal-loop, environmental-accounting-basis|
|environmental-debt-register|环境债务日志|catalog|project-owner-routing-candidate|environmental-debt-register-default|
|dorp-record|冲刺DORP记录|catalog|project-owner-routing-candidate|dorp-record-default|
|technical-debt-register|技术与架构债登记|catalog|project-owner-routing-candidate|technical-debt-register-default|
|sustainability-dual-entry-analysis|用途与基础设施双入口分析|catalog|project-owner-routing-candidate|sustainability-dual-entry-analysis-default|
|shared-carbon-factor-catalog|共享碳单位数据与因子目录|catalog|project-owner-routing-candidate|shared-carbon-factor-catalog-default|
|incident-architecture-adjustment|事件后的架构调整记录|catalog|project-owner-routing-candidate|incident-architecture-adjustment-default|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_12_03_01|12.3.1. Establish Value Realization Process|本阶段|价值实现过程影响业务项目利用EA达成结果。|
|C220-web-2025:02-architecture-development-method#tag_12_03_02|12.3.2. Deploy Monitoring Tools|本阶段|监测覆盖业务技术变化、价值、EA成熟度、资产、QoS使用与连续性。|
|C220-web-2025:02-architecture-development-method#tag_12_03_03|12.3.3. Manage Risks|本阶段|H管理EA风险并提供IT策略建议。|
|C220-web-2025:02-architecture-development-method#tag_12_03_04|12.3.4. Provide Analysis for Architecture Change Management|本阶段|变更分析结合性能、服务管理复核、价值与客户SLA。|
|C220-web-2025:02-architecture-development-method#tag_12_03_05|12.3.5. Develop Change Requirements to Meet Performance Targets|本阶段|H针对性能目标提出变更要求并准备行动。|
|C220-web-2025:02-architecture-development-method#tag_12_03_06|12.3.6. Manage Governance Process|本阶段|架构委员会或治理理事会决定技术、业务与豁免变更处理。|
|C220-web-2025:02-architecture-development-method#tag_12_03_07|12.3.7. Activate the Process to Implement Change|本阶段|激活变更需新的架构工作请求及投资请求，实施变化应入库。|

来源摘要：G186 §§5.1.5, 5.2.2, 15.2.3；C220 ADM 12

具体原文节与定位保留在mapping.json及adm-phases.json。
