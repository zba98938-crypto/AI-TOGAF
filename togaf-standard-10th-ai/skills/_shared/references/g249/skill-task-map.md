# G249 全部 71 项技能的任务与制品映射

71项人的能力映射到现有方法与制品，不建立71个AI技能；任务路由、行为证据建议均为项目推导。

官方技能名、角色参考等级和页码/原表格坐标保存在 [JSON](skill-task-map.json)。下表中的任务、路由和行为证据是项目推导；不会由生成制品自动认定人员能力。具体执行与缺口规则见 [运行契约](runtime-contract.md)。

| 官方技能（类别） | 项目任务示例 | 复用方法 | 复用制品 | 所需可观察证据 |
|---|---|---|---|---|
| Artificial Intelligence (AI) and Expert Systems（Application） | 为预测或规则推理应用定义目标、失效条件与人工处置 | `bi-model-operating-monitoring-method`<br>`bi-requirement-origin-boundary-method` | `bi-requirements-profile`<br>`options-decision-matrix` | 带适用数据、错误成本、监控和人工退出条件的方案评审 |
| Application Development（Application） | 把业务需求分解为可验收应用变更并评审实现约束 | `microservice-boundary-method`<br>`solution-delivery-notebook-review` | `software-engineering-diagram`<br>`solution-delivery-notebook` | 需求到接口规格及验收测试的追溯和独立代码/设计评审 |
| Application Modeling（Application） | 表达应用边界、职责和交互以支持方案决定 | `microservice-boundary-method`<br>`msa-contract-consumer-evidence-method` | `application-communication-diagram`<br>`application-function-matrix` | 模型对象与实际应用接口逐项核对的评审记录 |
| Application Security（Application） | 识别应用信任边界、威胁及控制要求 | `business-risk-assessment`<br>`solution-delivery-notebook-review` | `security-blueprint`<br>`security-impact-analysis` | 威胁到控制及验证结果的追溯，注明残余风险责任方 |
| Integration and Interoperability（Application） | 判断应用接口协议、语义及异常交互是否兼容 | `msa-contract-consumer-evidence-method`<br>`metadata-integration-tradeoff` | `interface-catalog`<br>`interoperability-assessment` | 消费者契约、失败重试和兼容性验证证据 |
| Optimistic/ Pessimistic Patterns（Application） **词义待专业来源确认** | 先澄清来源技能名在本项目中的专业含义，再定义适用任务 | `option-weighted-decision` | `options-decision-matrix` | 专业定义来源与采用记录；未经定义不得给出技能评级 |
| Programming（Application） | 审查代码原型能否满足架构约束和接口行为 | `solution-delivery-notebook-review`<br>`product-constraint-conformance-review` | `software-engineering-diagram`<br>`solution-delivery-notebook` | 有版本的代码、运行测试和专业评审；架构图不能替代编程实绩 |
| (Micro/Macro) Service- Oriented Architecture (SOA)（Application） | 选择服务边界、契约和生命周期治理安排 | `microservice-boundary-method`<br>`msa-federated-governance-process-method` | `microservice-decomposition-method`<br>`soa-layered-reference` | 服务拆分依据、消费者证据和治理例外评审 |
| Budget Management（Business） | 为架构工作分配预算并解释估算和变更偏差 | `architecture-project-scheduling`<br>`project-highlight-review` | `architecture-project-schedule`<br>`project-status-highlight-report` | 预算基线、估算假设及实际偏差的核对记录 |
| Business Capability Modeling（Business） | 按业务成果定义稳定能力及分解边界 | `capability-decomposition-method`<br>`capability-instance-gap-method` | `business-capability-map`<br>`capability-increment-analysis` | 能力定义与重复/遗漏边界的业务评审 |
| Business Case（Business） | 比较架构选择的价值、成本、风险及不行动后果 | `option-weighted-decision`<br>`benefit-realization-trigger` | `options-decision-matrix`<br>`ea-value-map` | 带假设、收益责任人和敏感性解释的商业论证 |
| Business Culture（Business） | 识别行为习惯对变革采纳和协作的限制 | `dtra-readiness-method`<br>`scenario-elicitation` | `digital-readiness-assessment`<br>`business-scenario-document` | 访谈证据、相反观察与采纳障碍解释 |
| Business Information Management（Business） | 识别业务信息责任、用途和共享规则 | `metadata-requirement-method`<br>`mdm-identity-analysis` | `information-map`<br>`metadata-policy-documentation` | 信息定义、使用场景及责任人确认 |
| Business Metrics（Business） | 将业务目的转为有口径和观测来源的度量 | `business-attribute-evaluation`<br>`smart-objective-review` | `business-attribute-profile`<br>`balanced-scorecard` | 度量口径、基线、目标来源与采样核对 |
| Business Process Design（Business） | 设计角色、事件、活动和控制组成的目标流程 | `scenario-elicitation`<br>`value-stream-definition-method` | `process-flow-diagram`<br>`process-event-control-product-catalog` | 场景走查、异常分支和控制有效性评审 |
| Business Process Management（Business） | 建立流程运行监测、责任和改进闭环 | `business-attribute-evaluation`<br>`benefit-realization-trigger` | `process-flow-diagram`<br>`business-attribute-profile` | 运行指标、异常处置及改进前后可比证据 |
| Business Scenario（Business） | 从原始叙述识别问题、参与者和可验证结果 | `scenario-elicitation`<br>`scenario-traceability-review` | `business-scenario-document`<br>`scenario-traceability-matrix` | 原料到问题和需求的可追溯转换及反例 |
| Business Service Development（Business） | 定义服务受益人、价值、契约和支撑能力 | `value-stream-definition-method`<br>`ea-service-emergence-npd-method` | `business-service-function-catalog`<br>`contract-measure-catalog` | 服务边界、质量承诺与消费者验收 |
| Integration and Sharing（Business） | 确定跨业务单元共享能力和协作边界 | `operating-model-submodel-analysis-method`<br>`domain-architecture-alignment-review` | `business-interaction-matrix`<br>`operating-model` | 共享与本地差异的业务决策依据及交接责任 |
| Legacy Management（Business） | 比较保留、替换和演进既有资产的后果 | `option-weighted-decision`<br>`technical-debt-register-method` | `application-portfolio-catalog`<br>`technical-debt-register` | 遗留依赖、迁移约束和延迟处置成本的证据 |
| Organization Design（Business） | 对齐组织职责、协作和能力归属 | `operating-model-submodel-analysis-method`<br>`architecture-role-catalog-review` | `organization-map`<br>`capability-organization-matrix` | 组织边界、能力责任和冲突处置的确认记录 |
| Role Design（Business） | 从任务需求设计可裁剪角色和责任交接 | `architecture-role-catalog-review`<br>`architecture-role-skill-assessment` | `architecture-role-catalog`<br>`actor-role-matrix` | 岗位/角色/任务区别及权限、协作、技能要求追溯 |
| Security and Asset Management（Business） | 确定业务资产的价值、保护责任和控制需求 | `business-risk-assessment`<br>`domain-architecture-alignment-review` | `security-classification-scheme`<br>`security-domain-model` | 资产分类、责任方和控制适用性评审 |
| Strategic Planning（Business） | 将战略选择转换为能力与变革优先项 | `architecture-backlog-trace-review`<br>`work-package-prioritization` | `strategy-capability-matrix`<br>`architecture-backlog` | 战略到能力和工作包的因果假设及取舍记录 |
| Visioning（Business） | 建立利益相关者可共同评审的目标愿景 | `scenario-elicitation`<br>`ea-point-of-view-review` | `solution-concept-diagram`<br>`ea-point-of-view-register` | 愿景边界、相反意见及共识/未决项记录 |
| Managing Change（Change） | 识别变革影响、采纳障碍与沟通支持需求 | `dtra-readiness-method`<br>`project-management-strategy-review` | `readiness-consequence-analysis`<br>`project-management-strategy` | 影响群体、就绪证据与分阶段应对记录 |
| Value Management（Change） | 追踪变革收益目标、责任与实现条件 | `benefit-realization-trigger`<br>`business-attribute-evaluation` | `value-realization-assessment`<br>`benefits-diagram` | 收益基线、观测及复评触发，区分相关和归因 |
| Work Package Management（Change） | 分解架构工作并协调依赖、资源和验收 | `architecture-project-scheduling`<br>`dependency-topological-order` | `architecture-project-wbs`<br>`architecture-project-schedule` | 依赖、资源期间、工作量和验收责任核对 |
| Governance of Change（Change） | 确定变更决策权、合规检查与例外处置 | `change-profile-governance-review`<br>`product-constraint-conformance-review` | `architecture-governance-checklist`<br>`non-compliance-disposition` | 有权限来源的决定、例外期限及跟进证据 |
| Analytical Data（Data） | 定义分析数据语义、质量和用途边界 | `bi-requirement-origin-boundary-method`<br>`bi-value-chain-controls-method` | `bi-requirements-profile`<br>`metadata-dictionary` | 指标到原始数据与质量控制的追溯 |
| Big Data（Data） | 根据规模、时效和资源条件评审数据处理架构 | `bi-transition-method`<br>`metadata-integration-tradeoff` | `processing-diagram`<br>`bi-transition-architecture` | 真实容量/延迟测量、分布方案取舍及运行边界 |
| Data Governance（Data） | 建立数据责任、质量规则和决策机制 | `metadata-requirement-method`<br>`metadata-application-coverage-review` | `metadata-policy-documentation`<br>`data-quality-assessment` | 规则到责任与观测的对应及违规处置记录 |
| Data Integration（Data） | 对齐数据源、身份、转换和交换语义 | `metadata-integration-tradeoff`<br>`mdm-identity-analysis` | `metadata-integration-model`<br>`mdm-exchange-pattern` | 字段映射、冲突样例和接口验证结果 |
| Data Migration（Data） | 设计数据切换、核对、退出及回退条件 | `transition-operability-check`<br>`bi-stage-operability-and-exit-method` | `data-migration-diagram`<br>`rollback-plan` | 迁移前后数量/语义核对和回退演练结果 |
| Data Modeling（Data） | 建立实体、关系和约束以回答业务问题 | `metadata-requirement-method`<br>`mdm-identity-analysis` | `conceptual-data-diagram`<br>`logical-data-diagram` | 模型业务定义、边界反例及独立评审 |
| Data Security（Data） | 确定数据分类、访问、保护及生命周期控制 | `business-risk-assessment`<br>`metadata-requirement-method` | `data-security-diagram`<br>`security-classification-scheme` | 敏感数据流、访问规则和控制测试证据 |
| Master Data Management（Data） | 设计主数据身份、主记录及冲突仲裁 | `mdm-identity-analysis`<br>`mdm-match-merge-arbitration-method` | `customer-mdm-model`<br>`mdm-integration-style` | 匹配误差、来源优先级与可取消合并的评审 |
| Operational Data（Data） | 明确业务运行数据的一致性、时效和责任 | `msa-data-distribution-conditions-method`<br>`metadata-requirement-method` | `data-lifecycle-diagram`<br>`data-usage-documentation` | 更新来源、失效窗口和异常恢复验证 |
| Broad and Focused Perspective（Architecture） | 选择整体与局部架构视角并解释决策边界 | `domain-architecture-alignment-review`<br>`architecture-description-formality-review-method` | `architecture-landscape-projection`<br>`project-context-diagram` | 跨域影响与局部细节取舍的审查记录 |
| Broad Generic Modeling（Architecture） | 选用适合关注点的抽象、对象和关系 | `reference-model-tailoring`<br>`architecture-description-formality-review-method` | `building-block-description`<br>`viewpoint-library` | 模型语义、关注点覆盖和抽象遗漏的验证 |
| Decision Making（Architecture） | 基于约束、备选与证据形成可复议决定 | `option-weighted-decision`<br>`decision-delegation-register-method` | `options-decision-matrix`<br>`decision-delegation-register` | 被淘汰选项、证据冲突、权限与复议条件 |
| Generic Integration and Interoperability（Architecture） | 检查业务、数据、应用和技术的跨域一致性 | `domain-architecture-alignment-review`<br>`metadata-integration-tradeoff` | `interoperability-assessment`<br>`domain-architecture-alignment` | 跨域接口、语义和治理依赖的联合评审 |
| Generic Standards and Regulations（Architecture） | 判断标准与法规在本范围的适用性和冲突 | `product-constraint-conformance-review`<br>`reference-model-tailoring` | `technology-standards-catalog`<br>`applicable-legislation-register` | 版本、司法/组织范围与适用性专业确认 |
| Principle Definition（Architecture） | 为架构选择定义有理由和后果的原则 | `ea-point-of-view-review`<br>`product-constraint-conformance-review` | `principles-catalog`<br>`product-constraint-register` | 原则理由、影响及冲突例外决策证据 |
| Road Mapping（Architecture） | 组织目标、过渡、依赖和可运营退出条件 | `dependency-topological-order`<br>`transition-operability-check` | `transition-architecture-model`<br>`architecture-project-schedule` | 依赖与过渡验收/回退条件的核对 |
| Strategy Into Architecture（Architecture） | 把战略意图落实到能力、需求与构建块 | `architecture-backlog-trace-review`<br>`capability-instance-gap-method` | `strategy-capability-matrix`<br>`building-block-description` | 战略到能力增量和工作包的稳定ID追溯 |
| Viewpoints and Views（Architecture） | 从受众关注点制定视点并验证视图充分性 | `architecture-description-formality-review-method`<br>`reference-model-tailoring` | `viewpoint-library`<br>`architecture-description-formality-review` | 受众、关注点、构造规则与评审结论 |
| Influencing（Generic） | 使架构建议在决策者语境中得到理解和处置 | `ea-point-of-view-review` | `ea-point-of-view-register`<br>`stakeholder-influence-matrix` | 沟通后的异议、采纳决定和实际影响记录 |
| Inter-Personal（Generic） | 处理架构协作中的分歧与信任问题 | `scenario-elicitation`<br>`agile-collaboration-selection-switch` | `stakeholder-catalog`<br>`organization-map` | 真实协作观察、分歧处理及对方反馈 |
| Leadership（Generic） | 组织共同方向、责任与复杂事项升级 | `architecture-role-catalog-review`<br>`project-management-strategy-review` | `architecture-role-catalog`<br>`project-management-strategy` | 目标澄清、授权边界及团队结果的行为证据 |
| Logical Analysis（Generic） | 检查假设、推理与结论之间的有效联系 | `scenario-traceability-review`<br>`option-weighted-decision` | `scenario-traceability-matrix`<br>`options-decision-matrix` | 可复算/可复核推理和反例处置 |
| Oral Communication（Generic） | 向指定受众解释架构取舍并回应问题 | `ea-point-of-view-review`<br>`scenario-elicitation` | `ea-point-of-view-register`<br>`business-scenario-document` | 现场讲解、问答、受众理解反馈；演示文件本身不够 |
| Risk Management（Generic） | 识别架构风险、应对及剩余风险接受条件 | `business-risk-assessment`<br>`incident-architecture-adjustment-review` | `business-risk-register`<br>`risk-mitigation-plan` | 风险依据、控制效果、残余风险与责任方记录 |
| Stakeholder Management（Generic） | 识别关注点、影响与参与决策方式 | `scenario-elicitation`<br>`ea-point-of-view-review` | `stakeholder-catalog`<br>`stakeholder-influence-matrix` | 参与记录、关注点变化与未决冲突跟踪 |
| Teamwork（Generic） | 协调跨角色共同产出和交接责任 | `agile-collaboration-selection-switch`<br>`architecture-role-catalog-review` | `organization-map`<br>`actor-role-matrix` | 共同任务、交接验收、同事反馈与异常协作记录 |
| Training（Generic） | 设计能力学习活动并验证实际应用 | `architecture-role-skill-assessment` | `architecture-development-plan` | 可观察学习目标、实践产出和独立复评；出席不等于能力 |
| 条件辅助路由 | 仅当本次学习任务涉及安全教育，且已声明安全目标与受众时选择 | — | security-training-plan | 不作为默认选项 |
| Written Communication（Generic） | 写出受众可采取行动且可追溯的架构说明 | `ea-point-of-view-review`<br>`project-highlight-review` | `ea-point-of-view-register`<br>`project-status-highlight-report` | 真实文稿、读者反馈和误解修订记录 |
| Data Center（Technology） | 评审计算设施的容量、可用性和演进条件 | `transition-operability-check`<br>`sustainability-option-review` | `environments-and-locations-diagram`<br>`technology-portfolio-catalog` | 容量与故障演练测量、设施边界和运维确认 |
| Device（Technology） | 评审终端设备的接入、生命周期与兼容需求 | `product-constraint-conformance-review`<br>`reference-model-tailoring` | `technology-portfolio-catalog`<br>`networked-computing-hardware-diagram` | 真实设备约束、兼容测试及维护责任 |
| Integration and Interoperability（Technology） | 检查技术协议和平台之间的连接与兼容性 | `product-constraint-conformance-review`<br>`reference-model-tailoring` | `network-and-communications-diagram`<br>`interoperability-assessment` | 协议/版本兼容和故障模式验证 |
| Location, Security, and Directory Services（Technology） | 评审位置服务、身份目录和访问控制边界 | `business-risk-assessment`<br>`product-constraint-conformance-review` | `data-security-diagram`<br>`security-services-catalog` | 目录职责、授权规则、服务依赖和控制测试 |
| Network Topology（Technology） | 设计满足业务流量与故障隔离需求的拓扑 | `reference-model-tailoring`<br>`transition-operability-check` | `network-and-communications-diagram`<br>`networked-computing-hardware-diagram` | 拓扑选择依据、流量和故障域验证 |
| Networks（Technology） | 评审网络容量、协议、延迟和运营条件 | `transition-operability-check`<br>`product-constraint-conformance-review` | `network-and-communications-diagram`<br>`technology-standards-catalog` | 网络测量、协议约束和运维故障处理记录 |
| Operating Systems and Services（Technology） | 确定操作系统及平台服务的支持与兼容边界 | `product-constraint-conformance-review`<br>`transition-operability-check` | `platform-decomposition-diagram`<br>`technology-portfolio-catalog` | 版本支持、补丁约束、恢复和兼容性验证 |
| Physical Security（Technology） | 判断场地和设施实体防护是否满足风险需求 | `business-risk-assessment` | `environments-and-locations-diagram`<br>`security-blueprint` | 现场控制、访问流程与专业检查记录 |
| 条件辅助路由 | 仅在实体防护选项另需比较环境影响，且具备相应环境数据时作为辅助方法；不用于判定门禁或实体安全有效性 | sustainability-option-review | — | 不作为默认选项 |
| Contracts（Legal） | 识别架构相关合同义务、责任和约束 | `product-constraint-conformance-review`<br>`solution-delivery-notebook-review` | `contract-measure-catalog`<br>`applicable-legislation-register` | 具体合同条款、适用主体及法务确认；不能自动出具法律意见 |
| Data Protection（Legal） | 识别数据处理目的、地域和保护义务 | `business-risk-assessment`<br>`metadata-requirement-method` | `applicable-legislation-register`<br>`data-security-diagram` | 实际数据处理活动、适用法规版本与法务确认 |
| Fraud and Fair Dealing（Legal） | 识别欺诈和公平交易风险及控制责任 | `business-risk-assessment`<br>`scenario-traceability-review` | `business-risk-register`<br>`applicable-control-framework-register` | 具体交易场景、风险证据和专业合规复核 |
| Procurement（Legal） | 将采购规则与供应商/产品选择约束对应 | `option-weighted-decision`<br>`product-constraint-conformance-review` | `applicable-legislation-register`<br>`product-constraint-register` | 适用采购程序、利益冲突、选择理由和授权记录 |
| Risk（Legal） | 评审架构决定造成的法律责任与处置选择 | `business-risk-assessment`<br>`incident-architecture-adjustment-review` | `business-risk-register`<br>`security-impact-analysis` | 责任范围、风险后果及法务意见，不以通用风险分代替 |
| Rules and Regulations（Legal） | 确认架构范围内规则法规的适用与持续更新 | `product-constraint-conformance-review`<br>`domain-architecture-alignment-review` | `applicable-legislation-register`<br>`applicable-control-framework-register` | 有版本和适用地区的条款、控制映射及变更复核 |

每项还需本项目真实工作产出、独立观察或专业评审；适用法律、技术实现、人员认可和组织授权不由本表替代。源文仅列出 Optimistic/ Pessimistic Patterns，未定义其含义，必须保留原名与待补来源。
