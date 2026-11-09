# C · 信息系统架构（数据＋应用）

本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。

## 输入

- 当前愿景、业务架构要求及信息系统约束
- 现有数据、应用、接口、质量和责任边界

## 工作与治理门

1. 分别选择数据与应用视点，记录先后及并行依据
2. 开发数据和应用目标及可比基线
3. 识别数据质量、生命周期、服务、接口与交互差距
4. 分析应用/数据一致性、迁移和跨域影响
5. 形成候选构建块及架构需求并评审

- data-architecture：数据含义、责任、关系、质量及生命周期的目标/基线/差距明确；无数据变更须有影响判断
- application-architecture：应用职责、接口、交互的目标/基线/差距明确；无应用变更须有影响判断
- data-application-alignment：应用/数据使用与拥有、业务支持和集成约束一致
- work-cross-domain：差距工作、价值、风险、迁移及其他域影响已处理

## 候选交付物与制品

|交付物ID|名称|关系依据|所含制品ID|
|---|---|---|---|
|architecture-building-blocks|架构构建块|phase-contract-output-candidate|requirements-catalog, solution-concept-diagram|
|architecture-definition-document|架构定义文档|phase-contract-output-candidate|business-capability-map, conceptual-data-diagram, application-communication-diagram, platform-decomposition-diagram|
|architecture-requirements-specification|架构需求规格|phase-contract-output-candidate|requirements-catalog, constraints-catalog|

## 完整制品候选路由

|制品ID|名称|表达|阶段依据|Profiles|
|---|---|---|---|---|
|business-glossary-catalog|业务术语表目录|catalog|project-owner-routing-candidate|compat-business-glossary-catalog|
|application-portfolio-catalog|应用组合目录|catalog|source-artifact-phase-list|compat-application-portfolio-catalog|
|interface-catalog|接口目录|catalog|source-artifact-phase-list|compat-interface-catalog, msa-contract-consumer-evidence|
|data-entity-data-component-catalog|数据实体/数据组件目录|catalog|source-artifact-phase-list|compat-data-entity-data-component-catalog|
|application-function-matrix|应用/功能矩阵|matrix|source-artifact-phase-list|compat-application-function-matrix|
|application-organization-matrix|应用/组织矩阵|matrix|source-artifact-phase-list|compat-application-organization-matrix|
|data-entity-business-function-matrix|数据实体/业务功能矩阵|matrix|source-artifact-phase-list|compat-data-entity-business-function-matrix|
|role-application-matrix|角色/应用矩阵|matrix|source-artifact-phase-list|compat-role-application-matrix|
|application-interaction-matrix|应用交互矩阵|matrix|source-artifact-phase-list|compat-application-interaction-matrix|
|application-data-matrix|应用/数据矩阵|matrix|source-artifact-phase-list|compat-application-data-matrix|
|application-and-user-location-diagram|应用与用户位置图|diagram|source-artifact-phase-list|compat-application-and-user-location-diagram|
|business-service-information-diagram|业务服务/信息图|diagram|project-owner-routing-candidate|compat-business-service-information-diagram|
|conceptual-data-diagram|概念数据图|diagram|source-artifact-phase-list|information-bounded-cardinality, compat-conceptual-data-diagram|
|information-map|信息地图|diagram|project-owner-routing-candidate|information-concept-network, information-capability-use-modify, information-aggregation-generalization, compat-information-map, information-concept-object-meaning|
|process-application-realization-diagram|流程/应用实现图|diagram|source-artifact-phase-list|compat-process-application-realization-diagram|
|application-communication-diagram|应用通信图|diagram|source-artifact-phase-list|compat-application-communication-diagram|
|application-migration-diagram|应用迁移图|diagram|source-artifact-phase-list|application-gap-dependency, compat-application-migration-diagram|
|application-use-case-diagram|应用用例图|diagram|source-artifact-phase-list|compat-application-use-case-diagram|
|processing-diagram|处理图|diagram|project-owner-routing-candidate|compat-processing-diagram|
|software-distribution-diagram|软件分布图|diagram|source-artifact-phase-list|compat-software-distribution-diagram, msa-source-deployment-execution, msa-source-deployment-diagram|
|software-engineering-diagram|软件工程图|diagram|source-artifact-phase-list|compat-software-engineering-diagram|
|data-dissemination-diagram|数据分发图|diagram|source-artifact-phase-list|compat-data-dissemination-diagram, msa-data-distribution-conditions|
|data-lifecycle-diagram|数据生命周期图|diagram|source-artifact-phase-list|compat-data-lifecycle-diagram|
|data-migration-diagram|数据迁移图|diagram|source-artifact-phase-list|compat-data-migration-diagram|
|data-security-diagram|数据安全图|diagram|source-artifact-phase-list|compat-data-security-diagram|
|logical-data-diagram|逻辑数据图|diagram|source-artifact-phase-list|logical-data-identifiers, compat-logical-data-diagram|
|enterprise-manageability-diagram|企业可管理性图|diagram|source-artifact-phase-list|compat-enterprise-manageability-diagram|
|data-quality-assessment|数据质量评估|assessment|project-owner-routing-candidate|data-quality-assessment-default|
|metadata-dictionary|元数据字典|catalog|project-owner-routing-candidate|metadata-dictionary-default|
|data-usage-documentation|数据使用文档|report|project-owner-routing-candidate|data-usage-documentation-default|
|metadata-policy-documentation|元数据规则与政策文档|report|project-owner-routing-candidate|metadata-policy-documentation-default|
|data-issue-register|数据问题文档／登记册|catalog|project-owner-routing-candidate|data-issue-register-default|
|business-technical-asset-mapping|业务与技术资产关联|diagram|project-owner-routing-candidate|business-technical-asset-mapping-default|
|metadata-repository-design|元数据存储库设计|diagram|project-owner-routing-candidate|metadata-repository-design-default, metadata-three-part-solution|
|metadata-model|元数据模型|diagram|project-owner-routing-candidate|metadata-model-default|
|metadata-asset-coverage|元数据资产覆盖矩阵|diagram|project-owner-routing-candidate|metadata-asset-coverage-default, metadata-category-coverage, metadata-application-function-coverage|
|metadata-validation-workflow|元数据校验工作流|diagram|project-owner-routing-candidate|metadata-validation-workflow-default|
|metadata-integration-model|元数据集成模型|diagram|project-owner-routing-candidate|metadata-integration-model-default, metadata-central-hybrid-unified|
|metadata-ingestion-options|元数据采集备选方案|diagram|project-owner-routing-candidate|metadata-ingestion-options-default, metadata-manual-push-pull|
|metadata-inference-design|技术元数据推断方案|diagram|project-owner-routing-candidate|metadata-inference-design-default, metadata-inference-structure|
|customer-mdm-model|客户主数据模型|diagram|project-owner-routing-candidate|customer-mdm-model-default, mdm-operational-ten-questions, mdm-four-plateau-operations, mdm-match-merge-arbitration, mdm-business-function-coverage, mdm-application-function-coverage|
|mdm-integration-style|主数据集成风格|diagram|project-owner-routing-candidate|mdm-integration-style-default, mdm-consolidation-collaboration-central|
|mdm-exchange-pattern|主数据交换模式|diagram|project-owner-routing-candidate|mdm-exchange-pattern-default|
|bi-transition-architecture|BI 与分析演进架构|diagram|project-owner-routing-candidate|bi-transition-architecture-default, bi-baseline-transition-target, bi-stage-operability-and-exit, bi-value-chain-controls, bi-model-operating-monitoring|
|microservice-decomposition-method|微服务应用分解方法|report|project-owner-routing-candidate|microservice-decomposition-method-default|
|microservice-value-catalog|微服务价值与资源目录|catalog|project-owner-routing-candidate|microservice-value-catalog-default, msa-value-resource-evidence|

## 完整来源步骤与责任

|步骤ID|原名|责任|来源绑定中文解释|
|---|---|---|---|
|C220-web-2025:02-architecture-development-method#tag_06_03_01|6.3.1. Select Reference Models, Viewpoints, and Tools|本阶段|数据原则应复核验证，必要时生成，并选择参考/视点/捕获建模工具。|
|C220-web-2025:02-architecture-development-method#tag_06_03_02|6.3.2. Develop Baseline Data Architecture Description|本阶段|数据基线细节以支持目标及保留数据元素为准。|
|C220-web-2025:02-architecture-development-method#tag_06_03_03|6.3.3. Develop Target Data Architecture Description|本阶段|目标数据描述支撑愿景及目标业务架构。|
|C220-web-2025:02-architecture-development-method#tag_06_03_04|6.3.4. Perform Gap Analysis|本阶段|数据差距分析必须先核对内部一致性和准确性。|
|C220-web-2025:02-architecture-development-method#tag_06_03_05|6.3.5. Define Candidate Roadmap Components|本阶段|初始数据路线图基于基线目标差距并为后续活动排序。|
|C220-web-2025:02-architecture-development-method#tag_06_03_06|6.3.6. Resolve Impacts Across the Architecture Landscape|本阶段|数据架构需识别景观范围的双向影响与复用。|
|C220-web-2025:02-architecture-development-method#tag_06_03_07|6.3.7. Conduct Formal Stakeholder Review|本阶段|正式数据复核检查动机和说明书，同时评估对业务/应用影响与技术约束。|
|C220-web-2025:02-architecture-development-method#tag_06_03_08|6.3.8. Finalize the Data Architecture|本阶段|完成数据块标准、完整描述、最终追溯和库映射。|
|C220-web-2025:02-architecture-development-method#tag_06_03_09|6.3.9. Create/Update the Architecture Definition Document|本阶段|定义文档数据部分记录块决策理由并可含业务/逻辑数据和管理过程模型。|
|C220-web-2025:02-architecture-development-method#tag_07_03_01|7.3.1. Select Reference Models, Viewpoints, and Tools|本阶段|应用原则需验证或必要时生成，并选择应用参考、用户视点与工具。|
|C220-web-2025:02-architecture-development-method#tag_07_03_02|7.3.2. Develop Baseline Application Architecture Description|本阶段|应用基线深度依保留应用和已有描述决定。|
|C220-web-2025:02-architecture-development-method#tag_07_03_03|7.3.3. Develop Target Application Architecture Description|本阶段|目标应用支撑愿景、目标业务及目标数据。|
|C220-web-2025:02-architecture-development-method#tag_07_03_04|7.3.4. Perform Gap Analysis|本阶段|应用差距分析必须先核对内部一致性和准确性。|
|C220-web-2025:02-architecture-development-method#tag_07_03_05|7.3.5. Define Candidate Roadmap Components|本阶段|初始应用路线图基于基线目标差距并为后续活动排序。|
|C220-web-2025:02-architecture-development-method#tag_07_03_06|7.3.6. Resolve Impacts Across the Architecture Landscape|本阶段|应用架构需识别景观范围的双向影响与复用。|
|C220-web-2025:02-architecture-development-method#tag_07_03_07|7.3.7. Conduct Formal Stakeholder Review|本阶段|应用正式复核检验动机说明书并识别业务/数据改动和技术基础设施约束。|
|C220-web-2025:02-architecture-development-method#tag_07_03_08|7.3.8. Finalize the Application Architecture|本阶段|完成应用块标准、完整描述、最终追溯和库映射。|
|C220-web-2025:02-architecture-development-method#tag_07_03_09|7.3.9. Create/Update the Architecture Definition Document|本阶段|定义文档应用部分应记录块决定理由和关键视图。|

来源摘要：G186 §§5.2.2, 6.3, 15.2.1；C220 ADM 5,6,7

具体原文节与定位保留在mapping.json及adm-phases.json。
