# TOGAF 系列指南中文导读

内容角色：`derived-reading-guide`。这是基于各指南指定页的中文辅助解读，不是标准原文或完整译文。PDF页码为从1开始的物理页。适用场景、误读提示和阅读关联为项目使用建议；推荐关联不构成标准强制前置关系。

按问题选择入口：建立 EA 能力读 G184；开展架构工作读 G186；业务架构基础结合 G18A、G211、G178、G206、G190；数字与敏捷主题结合 G217、G20F、G210；数据治理按 G21B、G234、G238 定位。

## G152 · 将风险与安全融入TOGAF企业架构

把安全与风险融入企业架构和 ADM。

适用场景：规划安全治理及四个架构域的安全要求。

核心概念：Security Architecture、ISM、ERM、Cross-Cutting Concern。

- 安全架构利用企业架构信息，也向企业架构提供信息，应共同设计。（[PDF 第 13 页](documents/G152.md#page-13)）
- 安全贯穿业务、数据、应用、技术四域；它包含相关视图、视角和制品，并依托安全及风险管理过程。（[PDF 第 28 页](documents/G152.md#page-28)）
- 在 ADM 各阶段定位安全风险概念，预备阶段先建立安全上下文。（[PDF 第 29 页](documents/G152.md#page-29)）

误读提示：不要把安全作为与其他架构域隔离的附加工作。

推荐关联：[G186](documents/G186.md)、[G184](documents/G184.md)。

## G176 · 业务场景

用业务场景澄清问题、环境、结果和参与者，导出架构需求。

适用场景：启动架构工作或业务需求尚不清晰时。

核心概念：Business Scenario、SMART、Actor、Business Requirement。

- 通过多轮规划、收集、分析、记录和评审逐步改善需求理解，达到适用程度即可。（[PDF 第 13 页](documents/G176.md#page-13)）
- 六步覆盖问题、环境、期望结果、人类参与者、计算参与者及适用性检查。（[PDF 第 18 页](documents/G176.md#page-18)）
- 业务场景服务于架构及后续开发，应聚焦高价值问题，控制范围蔓延。（[PDF 第 52 页](documents/G176.md#page-52)）

误读提示：不要把场景文档数量和持续细化本身当成目标。

推荐关联：[G211](documents/G211.md)、[G178](documents/G178.md)、[G186](documents/G186.md)。

## G178 · 价值流

从利益相关者视角描述价值交付阶段并映射支撑能力。

适用场景：分析端到端价值交付及阶段能力缺口时。

核心概念：Value Stream、Value Stream Stage、Stakeholder、Business Capability。

- 业务架构的价值流关注利益相关者价值，其用途区别于价值链、价值网络和精益价值流。（[PDF 第 11 页](documents/G178.md#page-11)）
- 价值流以名称、描述、触发利益相关者和预期价值四项描述。（[PDF 第 15 页](documents/G178.md#page-15)）
- 能力关注业务做什么；价值流关注怎样组合能力交付价值。（[PDF 第 24 页](documents/G178.md#page-24)）

误读提示：不要把价值仅等同金额，也不要直接以详细流程替代业务架构价值流。

推荐关联：[G211](documents/G211.md)、[G233](documents/G233.md)、[G18A](documents/G18A.md)。

## G184 · 领导者指南_建立并演进EA能力

建立、运营并演进适配企业上下文的 EA 能力。

适用场景：建立架构团队、治理机制或能力改进计划时。

核心概念：EA Capability、Enterprise Context、Governance、Capability Roadmap。

- 指南面向负责建立或演进 EA 能力的领导者，要求适配组织特定期望。（[PDF 第 17 页](documents/G184.md#page-17)）
- 企业使命、环境、战略和架构上下文是裁剪、排序和建设能力的基础。（[PDF 第 31 页](documents/G184.md#page-31)）
- 能力路线图表达当前到目标的候选路径和取舍，并服务沟通、资源与业务节奏。（[PDF 第 107 页](documents/G184.md#page-107)）

误读提示：不要直接套用其他企业的团队结构或把 EA 能力简化为工具采购。

推荐关联：[G186](documents/G186.md)、[G203](documents/G203.md)、[G249](documents/G249.md)。

## G186 · 实践者方法_按TOGAF_ADM开发企业架构

把 TOGAF 概念应用于架构开发、维护、使用和有效变革。

适用场景：明确架构目的、选择 ADM 路径并贯通战略到交付时。

核心概念：Architecture Purpose、ADM Iteration、Stakeholder、Governance。

- 通用概念可以保持一致，具体技术、模板和过程实现需要适配。（[PDF 第 17 页](documents/G186.md#page-17)）
- 企业架构用于引导有效变革，并支持利益相关者指导和控制变革。（[PDF 第 25 页](documents/G186.md#page-25)）
- 不同目的的 ADM 路径不简单也不线性，详细程度需适配目的。（[PDF 第 77 页](documents/G186.md#page-77)）

误读提示：不要把 ADM 当成每次必须完整顺序执行的固定瀑布。

推荐关联：[G184](documents/G184.md)、[G176](documents/G176.md)、[G248](documents/G248.md)。

## G188 · 架构项目管理

用项目管理方法组织架构定义项目的计划、控制及交接。

适用场景：管理架构项目阶段、交付和成果移交时。

核心概念：Architecture Project、PRINCE2、PMBOK、ADM A–F。

- 指南把 ADM 与 PRINCE2/PMBOK 方法结合，但不是完整项目管理教材。（[PDF 第 15 页](documents/G188.md#page-15)）
- 本指南定义的架构项目涵盖 A–F 和需求管理，到架构定义、路线图及实施计划移交结束。（[PDF 第 19 页](documents/G188.md#page-19)）
- 项目工作覆盖启动、计划、阶段执行监控、阶段结束和关闭。（[PDF 第 31 页](documents/G188.md#page-31)）

误读提示：不要把预备阶段、实施治理 G 和持续变更管理 H 混入本指南的架构项目定义。

推荐关联：[G186](documents/G186.md)、[G184](documents/G184.md)。

## G18A · 业务模型

把业务模型的价值创造逻辑展开为可实施的业务架构。

适用场景：明确业务创新、战略方向及架构影响时。

核心概念：Business Model、Value Creation、Business Architecture、Canvas。

- 业务模型描述组织如何创造、交付和获取价值，支持战略与执行对齐。（[PDF 第 11 页](documents/G18A.md#page-11)）
- 业务架构展开能力、价值流、组织和信息对象，并反馈业务模型假设的缺口。（[PDF 第 17 页](documents/G18A.md#page-17)）
- 业务模型自身粒度不足以形成详细实施计划，需要业务架构继续展开。（[PDF 第 27 页](documents/G18A.md#page-27)）

误读提示：不要把业务模型画布当作完整实施蓝图或风险分析。

推荐关联：[G178](documents/G178.md)、[G211](documents/G211.md)、[G206](documents/G206.md)、[G190](documents/G190.md)。

## G190 · 信息映射

建立业务信息概念和关系的共同语言，连接后续数据架构。

适用场景：统一业务信息含义并关联能力和价值流时。

核心概念：Information Map、Information Concept、Business Vocabulary、Data Model。

- 信息地图收集业务关心的概念及关系，先采用业务词汇表达。（[PDF 第 12 页](documents/G190.md#page-12)）
- 业务信息不局限于可存储字段；信息地图与数据模型不相同。（[PDF 第 16 页](documents/G190.md#page-16)）
- 信息地图结合能力、价值流及组织地图，为后续架构提供业务依据。（[PDF 第 21 页](documents/G190.md#page-21)）

误读提示：不要提前将所有信息概念压缩为数据库字段，遗漏主观及非结构化信息。

推荐关联：[G211](documents/G211.md)、[G178](documents/G178.md)、[G206](documents/G206.md)、[G234](documents/G234.md)。

## G198 · 架构技能框架

用角色、技能和知识深度识别架构人员匹配与缺口。

适用场景：架构团队招聘、培训和人员能力盘点。

核心概念：Role、Skill、Competency Level、Skills Gap。

- 技能框架描述角色、技能及知识深度，帮助快速识别匹配与缺口。（[PDF 第 9 页](documents/G198.md#page-9)）
- 架构工作需要业务与 IT 专业人员共同参与，框架服务人员发展和工作分配。（[PDF 第 13 页](documents/G198.md#page-13)）
- 框架希望降低培训、招聘和管理架构人员的时间、成本与风险。（[PDF 第 26 页](documents/G198.md#page-26)）

误读提示：技能等级用于表达要求；不要累加为未定义的总分或排名。

推荐关联：[G249](documents/G249.md)、[G184](documents/G184.md)。

## G203 · 架构成熟度模型

通过成熟度模型诊断架构实践并组织渐进改进。

适用场景：识别 EA 薄弱环节、制定改进优先级。

核心概念：CMM、ACMM、Maturity Assessment、Improvement Path。

- 公开框架是组织建立自身成熟度模型的示例，评估可用于周期性改进。（[PDF 第 11 页](documents/G203.md#page-11)）
- 美国商务部 ACMM 示例包括六个成熟度级别和九个架构要素。（[PDF 第 13 页](documents/G203.md#page-13)）

误读提示：不要把美国商务部示例当作所有组织必须采用的唯一评分体系。

推荐关联：[G184](documents/G184.md)、[G249](documents/G249.md)。

## G206 · 组织映射

表达企业生态中组织单元及其实际工作关系。

适用场景：跨部门协作、伙伴关系和能力归属分析。

核心概念：Organization Map、Organization Unit、Ecosystem、Working Relationship。

- 组织地图包括单元、伙伴、利益相关者及正式和非正式关系，可跨法人边界。（[PDF 第 12 页](documents/G206.md#page-12)）
- 组织地图补充汇报图未充分表达的水平、多对多及外部协作。（[PDF 第 14 页](documents/G206.md#page-14)）
- 组织、能力、价值流与信息概念相互映射，帮助确定整体架构范围。（[PDF 第 24 页](documents/G206.md#page-24)）

误读提示：不要把组织地图简化为姓名职位的汇报树或自动限定一个法人。

推荐关联：[G211](documents/G211.md)、[G178](documents/G178.md)、[G190](documents/G190.md)。

## G20F · 赋能企业敏捷性

使架构开发和产品管理方式支持企业敏捷。

适用场景：按价值增量推进架构并改善产品团队协作。

核心概念：Enterprise Agility、Architecture Partitioning、Product-Centric、Iteration。

- 战略、分段、能力是详细程度层级，四个架构域均可存在于各层级。（[PDF 第 20 页](documents/G20F.md#page-20)）
- 敏捷架构需要迭代增量、配套技能与治理，并更加关注产品和结果。（[PDF 第 35 页](documents/G20F.md#page-35)）

误读提示：不要混淆详细程度与架构域，也不要把敏捷等同取消治理。

推荐关联：[G210](documents/G210.md)、[G217](documents/G217.md)、[G186](documents/G186.md)。

## G210 · 以敏捷冲刺应用TOGAF_ADM

用冲刺和协作模式把企业架构接入敏捷交付。

适用场景：短周期架构增量及多个敏捷团队协同。

核心概念：Sprint、MVA、Collaboration Pattern、Partition。

- 四种协作模式包括架构开发敏捷、解决方案、跨开发和跨职能协作，需按组织调整。（[PDF 第 13 页](documents/G210.md#page-13)）
- 短周期工作帮助应对不确定性和迟到信息，强调及早试验概念。（[PDF 第 17 页](documents/G210.md#page-17)）
- 一个 MVA 可涉及部分或全部 ADM 阶段，B–E 可以跨阶段迭代。（[PDF 第 30 页](documents/G210.md#page-30)）

误读提示：不要把一个冲刺机械对应一个 ADM 阶段。

推荐关联：[G20F](documents/G20F.md)、[G186](documents/G186.md)、[G217](documents/G217.md)。

## G211 · 业务能力

定义业务能力、建立能力地图并支持分析与投资。

适用场景：能力地图、能力缺口和组织系统投资分析。

核心概念：Business Capability、Capability Map、Heat Map、Cross-Mapping。

- 能力首先说明业务能做什么，与怎样做、谁来做等问题分开。（[PDF 第 12 页](documents/G211.md#page-12)）
- 能力地图相对独立于组织结构、流程和 IT 系统，再通过交叉映射深化分析。（[PDF 第 15 页](documents/G211.md#page-15)）
- 热力图可表达成熟度、绩效、价值或成本等不同属性，颜色要有具体定义。（[PDF 第 23 页](documents/G211.md#page-23)）

误读提示：不要把能力名称等同系统或部门，也不要对所有热力图赋予同一颜色含义。

推荐关联：[G178](documents/G178.md)、[G233](documents/G233.md)、[G206](documents/G206.md)。

## G212 · 数字技术采用就绪度评估

评估数字技术采用的准备度，并制定有依据的采用路线。

适用场景：转型前识别人员、流程、技术及领导力缺口。

核心概念：DTRA、Readiness Factors、Adoption Approach、ABCD。

- 用数字资源替代物理资源本身不等于数字化转型。（[PDF 第 20 页](documents/G212.md#page-20)）
- 采用方式根据普及广度和采用速度选择，需解释选择理由。（[PDF 第 39 页](documents/G212.md#page-39)）
- 准备度覆盖人员、流程、生态、技术和系统；缺口可纳入实施前或实施中的补救。（[PDF 第 48 页](documents/G212.md#page-48)）

误读提示：不要把四种采用方式当作优劣排名或把采购清单当作准备度。

推荐关联：[G217](documents/G217.md)、[G21H](documents/G21H.md)、[G184](documents/G184.md)。

## G217 · 在数字企业中使用TOGAF标准

按数字企业成长上下文裁剪 TOGAF 能力与服务。

适用场景：企业从创业者发展到多团队和持续运营阶段时。

核心概念：DPBoK、Emergence Model、EA Services、Digital Enterprise。

- 四种上下文为个人/创始人、团队、团队之团队、持久企业，实施要适配规模文化和运营。（[PDF 第 17 页](documents/G217.md#page-17)）
- 企业架构帮助数字产品敏捷交付，并连贯地管理技术债务。（[PDF 第 22 页](documents/G217.md#page-22)）
- 架构服务组合为各上下文提供决策、风险认识及下一阶段准备。（[PDF 第 31 页](documents/G217.md#page-31)）

误读提示：不要为不同成长阶段复制同样重量的流程和文档。

推荐关联：[G20F](documents/G20F.md)、[G210](documents/G210.md)、[G21H](documents/G21H.md)。

## G21B · 信息架构_客户主数据管理

把跨组织共享的核心客户信息作为资产管理。

适用场景：客户信息分散、重复与质量治理问题。

核心概念：C-MDM、Kernel Customer Data、Data Quality、Integration Style。

- 客户主数据能力涵盖人员、流程、组织和系统，以提高共享信息价值。（[PDF 第 11 页](documents/G21B.md#page-11)）
- 共享核心客户数据需要兼顾价值、质量、安全和可用性，自动化与人工处理需平衡。（[PDF 第 21 页](documents/G21B.md#page-21)）
- 整合、协作和集中集成方式可以组合，影响运营流程和质量治理。（[PDF 第 48 页](documents/G21B.md#page-48)）

误读提示：不要把 C-MDM 简化为数据库采购，也不要把三种集成方式当成互斥选项。

推荐关联：[G190](documents/G190.md)、[G234](documents/G234.md)、[G238](documents/G238.md)。

## G21D · 政府参考模型

用可裁剪政府参考模型支持公共部门变革。

适用场景：公共部门分类、变革影响与跨部门依赖分析。

核心概念：GRM、Sector、Business Function、Government Service。

- GRM 提供公共部门共同视角和参考模板，可扩展或按机构裁剪。（[PDF 第 21 页](documents/G21D.md#page-21)）
- 十一类领域用于分段部门、识别变革影响和依赖，驱动因素帮助表达结果。（[PDF 第 67 页](documents/G21D.md#page-67)）

误读提示：不要把参考分类直接当成本地政府实际编制或已验证服务清单。

推荐关联：[G206](documents/G206.md)、[G211](documents/G211.md)、[G186](documents/G186.md)。

## G21H · TOGAF数字业务参考模型

用数字业务参考模型理解企业核心构成和变革影响。

适用场景：建立数字业务全景、定位战略和运营模型变化。

核心概念：DBRM、Digital Enablement、Operating Model、Ecosystem。

- 数字化转型需要组织范围变化，并对齐上下文、环境和战略。（[PDF 第 15 页](documents/G21H.md#page-15)）
- 十个核心要素归入数字、战略、结构、运营四域，高层图并不规定详细关系。（[PDF 第 24 页](documents/G21H.md#page-24)）
- 可配置的模块化构建块支持架构随环境演进和适当层级决策。（[PDF 第 39 页](documents/G21H.md#page-39)）

误读提示：不要从高层图布局自动推导详细依赖方向或业务流程。

推荐关联：[G217](documents/G217.md)、[G18A](documents/G18A.md)、[G211](documents/G211.md)。

## G21I · 微服务架构

在企业架构上下文中判断、设计和治理微服务。

适用场景：微服务采用、拆分、独立部署及组织治理。

核心概念：MSA、Atomic Business Function、Service Independence、Federated Governance。

- 微服务是架构风格，不是产品或平台；服务独立、自包含并承担原子业务功能。（[PDF 第 16 页](documents/G21I.md#page-16)）
- 指南通过 ADM 帮助决定在哪里及如何使用微服务，重点涉及数据应用和技术设计。（[PDF 第 20 页](documents/G21I.md#page-20)）
- MSA 是企业架构的一部分而非完整 EA，预备阶段需要处理组织准备和分布式治理。（[PDF 第 51 页](documents/G21I.md#page-51)）

误读提示：不要只按代码体量划分微服务或把微服务方案等同完整企业架构。

推荐关联：[G186](documents/G186.md)、[G152](documents/G152.md)、[G210](documents/G210.md)。

## G233 · 业务能力规划

连接能力实例与价值流，支持投资、改进和退役决策。

适用场景：评估投资、减少重复并规划能力优化。

核心概念：Business Capability Instance、Value Stream、Capability Planning、Maturity。

- 先理解使命愿景价值观、组织、财务与业务计划，并整理逻辑 IT 目录。（[PDF 第 15 页](documents/G233.md#page-15)）
- 通用能力说明做什么；在具体价值流中实例化后才能评估实际绩效。（[PDF 第 32 页](documents/G233.md#page-32)）
- 可复用既有能力实例形成新价值流，或根据条件变化改进与退役。（[PDF 第 40 页](documents/G233.md#page-40)）

误读提示：不要将抽象能力目录与不同场景的能力实例混为一谈。

推荐关联：[G211](documents/G211.md)、[G178](documents/G178.md)、[G206](documents/G206.md)、[G18A](documents/G18A.md)。

## G234 · 信息架构_元数据管理

建立元数据能力，使数据含义、质量和责任可理解。

适用场景：数据目录、术语表、血缘和元数据治理。

核心概念：Metadata、Metadata Repository、Data Documentation、Validation Workflow。

- 指南提供共同语言，强调数据文档化价值及元数据能力所需投入。（[PDF 第 11 页](documents/G234.md#page-11)）
- 元数据管理包含规划、实施和控制活动，以支持高质量集成元数据。（[PDF 第 14 页](documents/G234.md#page-14)）
- IT 解决方案由技术功能、数据模型、更新与验证流程共同组成。（[PDF 第 25 页](documents/G234.md#page-25)）

误读提示：不要把元数据能力等同一次扫描或一个目录工具。

推荐关联：[G190](documents/G190.md)、[G21B](documents/G21B.md)、[G238](documents/G238.md)。

## G238 · 信息架构_商业智能与分析

用参考模型及 ADM 设计面向决策的 BI 与分析能力。

适用场景：报表分析能力规划、缺口评估和业务目标对齐。

核心概念：BI & Analytics、Decision-Making Data、Business Function、Application Function。

- 提供 BI 能力参考模型及 ADM 适配方法，形成共同语言并加快架构工作。（[PDF 第 11 页](documents/G238.md#page-11)）
- 能力组合人员、流程、组织及系统，将决策相关数据转为增值信息。（[PDF 第 13 页](documents/G238.md#page-13)）
- 参考模型将目标、说明和 KPI 联系起来，例如隐私合规和数据泄露指标。（[PDF 第 28 页](documents/G238.md#page-28)）

误读提示：不要把 BI 简化为报表工具选型，也不要把示例 KPI 直接当作项目目标。

推荐关联：[G234](documents/G234.md)、[G190](documents/G190.md)、[G21B](documents/G21B.md)。

## G242 · 环境可持续的信息系统

把数字可持续性作为组织能力并纳入架构转型和治理。

适用场景：评估系统环境影响、制定可持续政策和路线图。

核心概念：Digital Sustainability、Lifecycle Impact、Transition Architecture、Environmental Governance。

- 环境影响不能只看使用阶段能耗，还需考虑制造 ICT 资产的足迹。（[PDF 第 29 页](documents/G242.md#page-29)）
- 通过 ADM 从基线到目标、借助过渡架构增量建立可持续能力。（[PDF 第 85 页](documents/G242.md#page-85)）
- 该主题适配不是独立的 ADM 完整说明，需要与 TOGAF 标准一起阅读。（[PDF 第 85 页](documents/G242.md#page-85)）

误读提示：不要将运行节能直接等同生命周期减排，也不要将示例数据当作项目测量。

推荐关联：[G186](documents/G186.md)、[G184](documents/G184.md)、[G238](documents/G238.md)。

## G248 · 构建块的选择方法

按变革类型选择适用的构建块、视图和交付物。

适用场景：控制架构工作范围并选择必要模型。

核心概念：Change Profile、ABB、SBB、Fitness for Purpose。

- 根据三种变革画像选择构建块，并借助检查表判断交付物适用性。（[PDF 第 13 页](documents/G248.md#page-13)）
- ABB、SBB、视角、视图和交付物容器需分别识别，以服务具体问题。（[PDF 第 19 页](documents/G248.md#page-19)）
- 本书是可采用方法示例而非唯一必选流程，考虑上下文、概念、逻辑和物理层。（[PDF 第 25 页](documents/G248.md#page-25)）

误读提示：不要将全部制品及构建块目录当成每个项目的强制产出。

推荐关联：[G186](documents/G186.md)、[G184](documents/G184.md)。

## G249 · 架构角色与技能

明确架构角色、任务和技能要求，支持实践团队建设。

适用场景：岗位职责、人员分工和技能发展计划。

核心概念：Job、Role、Assignment、Proficiency Level。

- 框架帮助识别角色技能与知识深度，并发现匹配和缺口。（[PDF 第 11 页](documents/G249.md#page-11)）
- 岗位、角色和任务不同；一人可以承担多角色，多人也可共同承担一个角色。（[PDF 第 16 页](documents/G249.md#page-16)）
- 技能覆盖应用、架构、业务、变更、数据、通用、法律和技术类别。（[PDF 第 26 页](documents/G249.md#page-26)）

误读提示：不要把角色一对一固定为职位或照搬示例组织结构。

推荐关联：[G184](documents/G184.md)、[G198](documents/G198.md)、[G203](documents/G203.md)。
