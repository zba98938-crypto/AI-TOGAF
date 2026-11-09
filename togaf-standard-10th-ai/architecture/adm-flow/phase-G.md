# G · 实施治理

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 已接受目标、架构需求、实施计划和合同
- 实际设计/实施证据、偏离及变更请求

## 工作与治理门

1. 明确合同责任、架构要求与合规判据
2. 核对实施范围与预期差距及工作包
3. 逐项检查设计和实施对架构要求的符合性
4. 评估偏离影响，提交强制执行/临时豁免/变更架构选项
5. 跟踪纠偏、限时豁免及业务运营交接

- contract-controls：要求、合同、责任与验证判据明确
- scope-compliance：实施范围实际覆盖预期差距及工作包
- implementation-evidence：符合性判断依据实际设计/实施证据，计划不冒充结果
- deviation-disposition：偏离有影响评估、实际决定及纠偏/限时豁免复核
- operational-handoff：运营交接、残余风险及后续价值监测责任明确

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-contract|架构合同|phase-contract-output-candidate|contract-measure-catalog, requirements-catalog|
|change-request|变更请求|phase-contract-output-candidate|requirements-impact-assessment|
|communications-plan|沟通计划|registry-phase-context|stakeholder-catalog|
|compliance-assessment|合规评估|phase-contract-output-candidate|requirements-catalog, data-security-diagram|
|solution-building-blocks|解决方案构建块|registry-phase-context|application-portfolio-catalog, technology-portfolio-catalog|
|implementation-governance-model|实施治理模型|registry-phase-context|role-catalog, actor-role-matrix|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|contract-measure-catalog|合同/度量目录|catalog|project-owner-routing-candidate|compat-contract-measure-catalog|
|data-security-diagram|数据安全图|diagram|project-owner-routing-candidate|compat-data-security-diagram|
|risk-appetite|风险偏好|assessment|project-owner-routing-candidate|risk-appetite-default|
|business-impact-analysis|业务影响分析|assessment|project-owner-routing-candidate|business-impact-analysis-default|
|security-resource-plan|安全资源计划|report|project-owner-routing-candidate|security-resource-plan-default|
|security-blueprint|安全蓝图|diagram|project-owner-routing-candidate|security-blueprint-default, security-cross-domain, security-adm-concept-map|
|business-attribute-profile|业务属性画像|catalog|project-owner-routing-candidate|business-attribute-profile-default, business-attribute-profile-trace|
|security-policy-architecture|安全策略架构|diagram|project-owner-routing-candidate|security-policy-architecture-default|
|security-domain-model|安全域模型|diagram|project-owner-routing-candidate|security-domain-model-default|
|trust-framework|信任框架|diagram|project-owner-routing-candidate|trust-framework-default|
|business-risk-register|业务风险模型／风险登记册|catalog|project-owner-routing-candidate|business-risk-register-default, risk-security-traceability|
|applicable-legislation-register|适用法律法规登记册|catalog|project-owner-routing-candidate|applicable-legislation-register-default|
|applicable-control-framework-register|适用控制框架登记册|catalog|project-owner-routing-candidate|applicable-control-framework-register-default|
|security-services-catalog|安全服务目录|catalog|project-owner-routing-candidate|security-services-catalog-default|
|security-classification-scheme|安全分类方案|catalog|project-owner-routing-candidate|security-classification-scheme-default|
|risk-mitigation-plan|风险缓解计划|report|project-owner-routing-candidate|risk-mitigation-plan-default|
|transition-risk-assessment|过渡范围风险评估|assessment|project-owner-routing-candidate|transition-risk-assessment-default|
|security-impact-analysis|安全影响分析|assessment|project-owner-routing-candidate|security-impact-analysis-default|
|security-audit-record|安全审计记录|report|project-owner-routing-candidate|security-audit-record-default|
|security-training-plan|安全培训与意识计划|report|project-owner-routing-candidate|security-training-plan-default|
|environmental-decision-log|环境决策日志|catalog|project-owner-routing-candidate|environmental-decision-log-default, sustainability-culture-quadrant|
|change-profile-governance-checklist|变革画像治理检查清单|catalog|project-owner-routing-candidate|change-profile-planning-checklist, change-profile-implementation-checklist|
|decision-delegation-register|决策授权与可逆性登记|catalog|project-owner-routing-candidate|decision-delegation-register-default|
|sustainable-procurement-strategy|可持续ICT采购战略|catalog|project-owner-routing-candidate|sustainable-procurement-strategy-default|
|cloud-environmental-data-contract|云与外包环境数据共享契约|catalog|project-owner-routing-candidate|cloud-environmental-data-contract-default|
|solution-delivery-notebook|解决方案交付笔记本|catalog|project-owner-routing-candidate|solution-delivery-notebook-default|
|product-constraint-register|产品边界与企业约束登记|catalog|project-owner-routing-candidate|product-constraint-register-default|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_11_03_01|11.3.1. Confirm Scope and Priorities for Deployment with Development Management|本阶段|与开发管理确认部署范围优先、问题与块替换更新。|
|C220-web-2025:02-architecture-development-method#tag_11_03_02|11.3.2. Identify Deployment Resources and Skills|本阶段|部署资源需理解总体EA结果及项目期望，方法应支持架构与设计互操作反馈。|
|C220-web-2025:02-architecture-development-method#tag_11_03_03|11.3.3. Guide Development of Solutions Deployment|本阶段|每实施部署项目需影响分析、符合性规则、路线图时限和已签架构合同。|
|C220-web-2025:02-architecture-development-method#tag_11_03_04|11.3.4. Perform Enterprise Architecture Compliance Reviews|本阶段|按每个构建块审查持续实施治理与符合性。|
|C220-web-2025:02-architecture-development-method#tag_11_03_05|11.3.5. Implement Business and IT Operations|本阶段|运营实施含IT/业务服务、技能培训和沟通文档发布。|
|C220-web-2025:02-architecture-development-method#tag_11_03_06|11.3.6. Perform Post-Implementation Review and Close the Implementation|本阶段|实施后复核需发布并关闭项目，G在解法完整部署一次后关闭。|

来源摘要：G186 §§5.1.5, 5.2.2, 15.2.2；C220 ADM 11

具体原文节与定位保留在mapping.json及adm-phases.json。
