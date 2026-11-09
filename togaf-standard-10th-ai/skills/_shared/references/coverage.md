# 覆盖与调用索引

本页保留 G248 附录清单的兼容入口。全量指南新增的工作产品、专门视图和分析方法见 [能力注册](../capabilities.json)，操作方式见 [全量能力工作流](workflow-v2.md)。本页数量不代表整个资料库的能力上限。

75种基础登记制品（21目录、16矩阵、37图／地图、1评估）和23项交付物。名称别名、项目拆分及支持概念分别标记；候选清单不是每个项目的强制输出。

当前扩展登记为122工作产品、298规范条目／298独立ID、72方法；基础加扩展共196族，重叠ID只计一次。名称/用途的C220绑定见[基础执行映射](foundation-execution-bindings.json)，94项ADM来源步骤见[阶段契约](adm-phases.json)。

## 制品

### 新补齐的基础规划制品

- [实施因素目录](artifacts/implementation-factor-catalog.md) (`implementation-factor-catalog`)
- [合并差距、方案和依赖矩阵](artifacts/consolidated-gaps-solutions-dependencies-matrix.md) (`consolidated-gaps-solutions-dependencies-matrix`)
- [架构定义增量表](artifacts/architecture-definition-increments-table.md) (`architecture-definition-increments-table`)
- [过渡架构状态演进表](artifacts/transition-architecture-state-evolution-table.md) (`transition-architecture-state-evolution-table`)
- [业务价值与风险矩阵](artifacts/business-value-risk-matrix.md) (`business-value-risk-matrix`)

实施治理模型见[定义](deliverables/implementation-governance-model.md)，F阶段输出保留if any条件。

| ID | 制品 | 类型 | 原域 | 主责技能 |
| --- | --- | --- | --- | --- |
| `constraints-catalog` | [约束目录](artifacts/constraints-catalog.md) | catalog | 通用 | [togaf-requirements](../../togaf-requirements/SKILL.md) |
| `location-catalog` | [位置目录](artifacts/location-catalog.md) | catalog | 通用 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `principles-catalog` | [原则目录](artifacts/principles-catalog.md) | catalog | 通用 | [togaf-ea-capability](../../togaf-ea-capability/SKILL.md) |
| `requirements-catalog` | [需求目录](artifacts/requirements-catalog.md) | catalog | 通用 | [togaf-requirements](../../togaf-requirements/SKILL.md) |
| `business-capabilities-catalog` | [业务能力目录](artifacts/business-capabilities-catalog.md) | catalog | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `business-glossary-catalog` | [业务术语表目录](artifacts/business-glossary-catalog.md) | catalog | 业务 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `business-service-function-catalog` | [业务服务/功能目录](artifacts/business-service-function-catalog.md) | catalog | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `contract-measure-catalog` | [合同/度量目录](artifacts/contract-measure-catalog.md) | catalog | 业务 | [togaf-implementation-governance](../../togaf-implementation-governance/SKILL.md) |
| `driver-goal-objective-catalog` | [驱动因素/目标/目的目录](artifacts/driver-goal-objective-catalog.md) | catalog | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `organization-actor-catalog` | [组织/参与者目录](artifacts/organization-actor-catalog.md) | catalog | 业务 | [togaf-organization-roles](../../togaf-organization-roles/SKILL.md) |
| `process-event-control-product-catalog` | [流程/事件/控制/产品目录](artifacts/process-event-control-product-catalog.md) | catalog | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `role-catalog` | [角色目录](artifacts/role-catalog.md) | catalog | 业务 | [togaf-organization-roles](../../togaf-organization-roles/SKILL.md) |
| `stakeholder-catalog` | [利益相关者目录](artifacts/stakeholder-catalog.md) | catalog | 业务 | [togaf-vision-scenarios](../../togaf-vision-scenarios/SKILL.md) |
| `value-stream-catalog` | [价值流目录](artifacts/value-stream-catalog.md) | catalog | 业务 | [togaf-value-streams](../../togaf-value-streams/SKILL.md) |
| `value-stream-stages-catalog` | [价值流阶段目录](artifacts/value-stream-stages-catalog.md) | catalog | 业务 | [togaf-value-streams](../../togaf-value-streams/SKILL.md) |
| `application-portfolio-catalog` | [应用组合目录](artifacts/application-portfolio-catalog.md) | catalog | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `interface-catalog` | [接口目录](artifacts/interface-catalog.md) | catalog | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `data-entity-data-component-catalog` | [数据实体/数据组件目录](artifacts/data-entity-data-component-catalog.md) | catalog | 数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `technology-portfolio-catalog` | [技术组合目录](artifacts/technology-portfolio-catalog.md) | catalog | 技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `technology-standards-catalog` | [技术标准目录](artifacts/technology-standards-catalog.md) | catalog | 技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `actor-role-matrix` | [参与者/角色矩阵](artifacts/actor-role-matrix.md) | matrix | 业务 | [togaf-organization-roles](../../togaf-organization-roles/SKILL.md) |
| `application-function-matrix` | [应用/功能矩阵](artifacts/application-function-matrix.md) | matrix | 业务、应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `application-organization-matrix` | [应用/组织矩阵](artifacts/application-organization-matrix.md) | matrix | 业务、应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `business-interaction-matrix` | [业务交互矩阵](artifacts/business-interaction-matrix.md) | matrix | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `capability-organization-matrix` | [能力/组织矩阵](artifacts/capability-organization-matrix.md) | matrix | 业务 | [togaf-organization-roles](../../togaf-organization-roles/SKILL.md) |
| `data-entity-business-function-matrix` | [数据实体/业务功能矩阵](artifacts/data-entity-business-function-matrix.md) | matrix | 业务、数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `role-application-matrix` | [角色/应用矩阵](artifacts/role-application-matrix.md) | matrix | 业务、应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `strategy-capability-matrix` | [战略/能力矩阵](artifacts/strategy-capability-matrix.md) | matrix | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `value-stream-capability-matrix` | [价值流/能力矩阵](artifacts/value-stream-capability-matrix.md) | matrix | 业务 | [togaf-value-streams](../../togaf-value-streams/SKILL.md) |
| `application-interaction-matrix` | [应用交互矩阵](artifacts/application-interaction-matrix.md) | matrix | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `application-data-matrix` | [应用/数据矩阵](artifacts/application-data-matrix.md) | matrix | 应用、数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `application-technology-matrix` | [应用/技术矩阵](artifacts/application-technology-matrix.md) | matrix | 应用、技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `environments-and-locations-diagram` | [环境与位置图](artifacts/environments-and-locations-diagram.md) | diagram | 通用、业务、技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `application-and-user-location-diagram` | [应用与用户位置图](artifacts/application-and-user-location-diagram.md) | diagram | 业务、应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `benefits-diagram` | [收益图](artifacts/benefits-diagram.md) | diagram | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `business-capability-map` | [业务能力地图](artifacts/business-capability-map.md) | diagram | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `business-event-diagram` | [业务事件图](artifacts/business-event-diagram.md) | diagram | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `business-footprint-diagram` | [业务足迹图](artifacts/business-footprint-diagram.md) | diagram | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `business-model-diagram` | [业务模式图](artifacts/business-model-diagram.md) | diagram | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `business-service-information-diagram` | [业务服务/信息图](artifacts/business-service-information-diagram.md) | diagram | 业务 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `business-use-case-diagram` | [业务用例图](artifacts/business-use-case-diagram.md) | diagram | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `conceptual-data-diagram` | [概念数据图](artifacts/conceptual-data-diagram.md) | diagram | 业务、数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `functional-decomposition-diagram` | [功能分解图](artifacts/functional-decomposition-diagram.md) | diagram | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `goal-objective-service-diagram` | [目标/目的/服务图](artifacts/goal-objective-service-diagram.md) | diagram | 业务 | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `information-map` | [信息地图](artifacts/information-map.md) | diagram | 业务 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `organization-decomposition-diagram` | [组织分解图](artifacts/organization-decomposition-diagram.md) | diagram | 业务 | [togaf-organization-roles](../../togaf-organization-roles/SKILL.md) |
| `organization-map` | [组织地图](artifacts/organization-map.md) | diagram | 业务 | [togaf-organization-roles](../../togaf-organization-roles/SKILL.md) |
| `process-flow-diagram` | [流程图](artifacts/process-flow-diagram.md) | diagram | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `process-application-realization-diagram` | [流程/应用实现图](artifacts/process-application-realization-diagram.md) | diagram | 业务、应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `product-lifecycle-diagram` | [产品生命周期图](artifacts/product-lifecycle-diagram.md) | diagram | 业务 | [togaf-business-models-processes](../../togaf-business-models-processes/SKILL.md) |
| `project-context-diagram` | [项目语境图](artifacts/project-context-diagram.md) | diagram | 业务 | [togaf-vision-scenarios](../../togaf-vision-scenarios/SKILL.md) |
| `value-chain-diagram` | [价值链图](artifacts/value-chain-diagram.md) | diagram | 业务 | [togaf-value-streams](../../togaf-value-streams/SKILL.md) |
| `value-stream-map` | [价值流地图](artifacts/value-stream-map.md) | diagram | 业务 | [togaf-value-streams](../../togaf-value-streams/SKILL.md) |
| `application-communication-diagram` | [应用通信图](artifacts/application-communication-diagram.md) | diagram | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `application-migration-diagram` | [应用迁移图](artifacts/application-migration-diagram.md) | diagram | 应用 | [togaf-migration-roadmap](../../togaf-migration-roadmap/SKILL.md) |
| `application-use-case-diagram` | [应用用例图](artifacts/application-use-case-diagram.md) | diagram | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `processing-diagram` | [处理图](artifacts/processing-diagram.md) | diagram | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `software-distribution-diagram` | [软件分布图](artifacts/software-distribution-diagram.md) | diagram | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `software-engineering-diagram` | [软件工程图](artifacts/software-engineering-diagram.md) | diagram | 应用 | [togaf-application-architecture](../../togaf-application-architecture/SKILL.md) |
| `solution-concept-diagram` | [解决方案概念图](artifacts/solution-concept-diagram.md) | diagram | 应用 | [togaf-vision-scenarios](../../togaf-vision-scenarios/SKILL.md) |
| `data-dissemination-diagram` | [数据分发图](artifacts/data-dissemination-diagram.md) | diagram | 数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `data-lifecycle-diagram` | [数据生命周期图](artifacts/data-lifecycle-diagram.md) | diagram | 数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `data-migration-diagram` | [数据迁移图](artifacts/data-migration-diagram.md) | diagram | 数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `data-security-diagram` | [数据安全图](artifacts/data-security-diagram.md) | diagram | 数据 | [togaf-security-risk](../../togaf-security-risk/SKILL.md) |
| `logical-data-diagram` | [逻辑数据图](artifacts/logical-data-diagram.md) | diagram | 数据 | [togaf-information-data](../../togaf-information-data/SKILL.md) |
| `enterprise-manageability-diagram` | [企业可管理性图](artifacts/enterprise-manageability-diagram.md) | diagram | 技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `network-and-communications-diagram` | [网络与通信图](artifacts/network-and-communications-diagram.md) | diagram | 技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `networked-computing-hardware-diagram` | [联网计算/硬件图](artifacts/networked-computing-hardware-diagram.md) | diagram | 技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `platform-decomposition-diagram` | [平台分解图](artifacts/platform-decomposition-diagram.md) | diagram | 技术 | [togaf-technology-architecture](../../togaf-technology-architecture/SKILL.md) |
| `requirements-impact-assessment` | [需求影响评估](artifacts/requirements-impact-assessment.md) | assessment | 通用 | [togaf-requirements](../../togaf-requirements/SKILL.md) |

## 交付物

| ID | 交付物 | 常用 ADM | 主责技能 |
| --- | --- | --- | --- |
| `architecture-building-blocks` | [架构构建块](deliverables/architecture-building-blocks.md) | B C D E | [togaf-gap-solutions](../../togaf-gap-solutions/SKILL.md) |
| `architecture-contract` | [架构合同](deliverables/architecture-contract.md) | G | [togaf-implementation-governance](../../togaf-implementation-governance/SKILL.md) |
| `architecture-definition-document` | [架构定义文档](deliverables/architecture-definition-document.md) | B C D E | [togaf-architecture-workbench](../../togaf-architecture-workbench/SKILL.md) |
| `architecture-requirements-specification` | [架构需求规格](deliverables/architecture-requirements-specification.md) | A B C D | [togaf-requirements](../../togaf-requirements/SKILL.md) |
| `architecture-principles` | [架构原则](deliverables/architecture-principles.md) | Preliminary | [togaf-ea-capability](../../togaf-ea-capability/SKILL.md) |
| `architecture-repository` | [架构存储库](deliverables/architecture-repository.md) | Preliminary H | [togaf-ea-capability](../../togaf-ea-capability/SKILL.md) |
| `architecture-roadmaps` | [架构路线图](deliverables/architecture-roadmaps.md) | E F H | [togaf-migration-roadmap](../../togaf-migration-roadmap/SKILL.md) |
| `architecture-vision` | [架构愿景](deliverables/architecture-vision.md) | A | [togaf-vision-scenarios](../../togaf-vision-scenarios/SKILL.md) |
| `business-goals-objectives` | [业务目标与目的](deliverables/business-goals-objectives.md) | A B | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `business-principles` | [业务原则](deliverables/business-principles.md) | Preliminary A | [togaf-ea-capability](../../togaf-ea-capability/SKILL.md) |
| `business-drivers` | [业务驱动因素](deliverables/business-drivers.md) | A | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `capability-assessment` | [能力评估](deliverables/capability-assessment.md) | A B E | [togaf-strategy-capabilities](../../togaf-strategy-capabilities/SKILL.md) |
| `change-request` | [变更请求](deliverables/change-request.md) | G H | [togaf-change-value](../../togaf-change-value/SKILL.md) |
| `communications-plan` | [沟通计划](deliverables/communications-plan.md) | A G H | [togaf-vision-scenarios](../../togaf-vision-scenarios/SKILL.md) |
| `compliance-assessment` | [合规评估](deliverables/compliance-assessment.md) | G | [togaf-implementation-governance](../../togaf-implementation-governance/SKILL.md) |
| `implementation-migration-plan` | [实施与迁移计划](deliverables/implementation-migration-plan.md) | F | [togaf-migration-roadmap](../../togaf-migration-roadmap/SKILL.md) |
| `organization-model` | [企业架构组织模型](deliverables/organization-model.md) | Preliminary | [togaf-ea-capability](../../togaf-ea-capability/SKILL.md) |
| `request-for-architecture-work` | [架构工作请求](deliverables/request-for-architecture-work.md) | Preliminary H A | [togaf-change-value](../../togaf-change-value/SKILL.md) |
| `requirements-impact-assessment` | [需求影响评估](deliverables/requirements-impact-assessment.md) | Requirements | [togaf-requirements](../../togaf-requirements/SKILL.md) |
| `solution-building-blocks` | [解决方案构建块](deliverables/solution-building-blocks.md) | E G | [togaf-gap-solutions](../../togaf-gap-solutions/SKILL.md) |
| `statement-of-work` | [架构工作说明书](deliverables/statement-of-work.md) | A | [togaf-vision-scenarios](../../togaf-vision-scenarios/SKILL.md) |
| `tailored-architecture-framework` | [裁剪后的架构框架](deliverables/tailored-architecture-framework.md) | Preliminary | [togaf-ea-capability](../../togaf-ea-capability/SKILL.md) |
