# D · 技术架构

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 业务、数据、应用的能力和质量需求
- 平台、网络、环境、标准、安全及运营基线

## 工作与治理门

1. 选择平台、部署、通信与运营视点
2. 开发技术目标与可比基线
3. 识别质量、容量、韧性、技术标准及运营差距
4. 分析技术构建块、成本、风险与依赖
5. 协调跨域影响并评审

- baseline-target-gaps：技术目标、基线与差距可比较且有范围
- quality-operations：质量、安全、韧性及运营要求有对应设计与验证办法
- standards-blocks：技术标准和构建块约束可追溯
- work-cross-domain：实现工作、价值、风险、成本及跨域影响已处理

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-building-blocks|架构构建块|phase-contract-output-candidate|requirements-catalog, solution-concept-diagram|
|architecture-definition-document|架构定义文档|phase-contract-output-candidate|business-capability-map, conceptual-data-diagram, application-communication-diagram, platform-decomposition-diagram|
|architecture-requirements-specification|架构需求规格|phase-contract-output-candidate|requirements-catalog, constraints-catalog|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|location-catalog|位置目录|catalog|project-owner-routing-candidate|compat-location-catalog|
|technology-portfolio-catalog|技术组合目录|catalog|source-artifact-phase-list|compat-technology-portfolio-catalog|
|technology-standards-catalog|技术标准目录|catalog|source-artifact-phase-list|compat-technology-standards-catalog|
|application-technology-matrix|应用/技术矩阵|matrix|source-artifact-phase-list|compat-application-technology-matrix|
|environments-and-locations-diagram|环境与位置图|diagram|source-artifact-phase-list|compat-environments-and-locations-diagram|
|processing-diagram|处理图|diagram|source-artifact-phase-list|compat-processing-diagram|
|data-security-diagram|数据安全图|diagram|project-owner-routing-candidate|compat-data-security-diagram|
|enterprise-manageability-diagram|企业可管理性图|diagram|project-owner-routing-candidate|compat-enterprise-manageability-diagram|
|network-and-communications-diagram|网络与通信图|diagram|source-artifact-phase-list|compat-network-and-communications-diagram|
|networked-computing-hardware-diagram|联网计算/硬件图|diagram|source-artifact-phase-list|compat-networked-computing-hardware-diagram|
|platform-decomposition-diagram|平台分解图|diagram|source-artifact-phase-list|compat-platform-decomposition-diagram|
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
|security-training-plan|安全培训与意识计划|report|project-owner-routing-candidate|security-training-plan-default|
|microservice-technical-guidance|微服务技术指南|report|project-owner-routing-candidate|microservice-technical-guidance-default, msa-readiness-evidence, msa-federated-governance-process, msa-federated-governance-diagram|
|interoperability-assessment|互操作性评估|assessment|project-owner-routing-candidate|interoperability-assessment-default|
|soa-layered-reference|SOA 分层参考|diagram|project-owner-routing-candidate|soa-layered-reference|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_08_03_01|8.3.1. Select Reference Models, Viewpoints, and Tools|本阶段|技术原则、参考、视点和工具根据业务驱动及相关方关切选择。|
|C220-web-2025:02-architecture-development-method#tag_08_03_02|8.3.2. Develop Baseline Technology Architecture Description|本阶段|技术基线将已有环境转译为组织技术服务/组件分类。|
|C220-web-2025:02-architecture-development-method#tag_08_03_03|8.3.3. Develop Target Technology Architecture Description|本阶段|目标技术支撑愿景、业务和信息系统架构；ABBs描述功能及可能实现。|
|C220-web-2025:02-architecture-development-method#tag_08_03_04|8.3.4. Perform Gap Analysis|本阶段|技术差距分析必须先核对内部一致性和准确性。|
|C220-web-2025:02-architecture-development-method#tag_08_03_05|8.3.5. Define Candidate Roadmap Components|本阶段|初始技术路线图基于基线目标差距并为后续活动排序。|
|C220-web-2025:02-architecture-development-method#tag_08_03_06|8.3.6. Resolve Impacts Across the Architecture Landscape|本阶段|技术架构需识别景观范围的双向影响与复用。|
|C220-web-2025:02-architecture-development-method#tag_08_03_07|8.3.7. Conduct Formal Stakeholder Review|本阶段|技术正式复核以原动机和说明书检验适合后续域工作。|
|C220-web-2025:02-architecture-development-method#tag_08_03_08|8.3.8. Finalize the Technology Architecture|本阶段|完成技术块标准、完整描述、最终追溯和库映射。|
|C220-web-2025:02-architecture-development-method#tag_08_03_09|8.3.9. Create/Update the Architecture Definition Document|本阶段|技术定义需无歧义地表达功能属性、安全和可管理性。|

来源摘要：G186 §§5.2.2, 6.3, 15.2.1；C220 ADM 8

具体原文节与定位保留在mapping.json及adm-phases.json。
