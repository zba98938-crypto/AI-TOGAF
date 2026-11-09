# 架构分析证据索引

以下短引已独立匹配原始PDF的实体页，并核对SHA-256；中文释义为人工编写分析。完整证据及上下文见 [JSON](evidence.json)。

| 发现 | 中文释义 | 原文证据 |
|---|---|---|
| [G152:A01](guides/G152.md#a01) | 安全架构由组织、概念、逻辑和物理构件协同形成，用于维持受管理的风险状态。 | [G152 PDF 20](../documents/G152.md#page-20) · organizational, conceptual, logical, and physical components |
| [G152:A02](guides/G152.md#a02) | 风险是目标受到不确定性影响；结果偏差可以正向或负向。 | [G152 PDF 21](../documents/G152.md#page-21) · effect of uncertainty on objectives |
| [G152:A03](guides/G152.md#a03) | 安全架构与业务、数据、应用、技术四域交互，不能作为隔离的第五个实现烟囱。 | [G152 PDF 28](../documents/G152.md#page-28) · Business, Data, Application, and Technology |
| [G152:A04](guides/G152.md#a04) | 安全域把处于同一安全政策管辖的资产分组，并明确政策责任与外部责任交换。 | [G152 PDF 33](../documents/G152.md#page-33) · one security policy |
| [G152:A05](guides/G152.md#a05) | 信任关系有单向、双向和不存在三种可能，必须记录其成立依据。 | [G152 PDF 33](../documents/G152.md#page-33) · unidirectional, bidirectional, or non-existent |
| [G152:A06](guides/G152.md#a06) | 业务属性画像把业务目标与驱动转为风险导向要求，并追溯到测量目标。 | [G152 PDF 40](../documents/G152.md#page-40) · Traceability mapping between business drivers and requirements |
| [G152:A07](guides/G152.md#a07) | 控制目标是安全管理要实现的期望状态，与安全需求有区别，并与业务属性关联。 | [G152 PDF 41](../documents/G152.md#page-41) · It differs from a security requirement |
| [G176:A01](guides/G176.md#a01) | 六步涵盖问题、环境、预期结果、人类参与者、计算参与者及适用性核对。 | [G176 PDF 18](../documents/G176.md#page-18) · six steps |
| [G176:A02](guides/G176.md#a02) | 场景需要捕捉关键步骤与参与者交互，并说明责任、前置条件和技术质量要求。 | [G176 PDF 27](../documents/G176.md#page-27) · critical steps and interactions between actors |
| [G176:A03](guides/G176.md#a03) | 业务场景突出用于愿景及业务架构，也可在任何需要导出需求的ADM阶段使用。 | [G176 PDF 30](../documents/G176.md#page-30) · any ADM phase |
| [G176:A04](guides/G176.md#a04) | 目标需以SMART方式表达，使场景需求有可检验成功条件。 | [G176 PDF 36](../documents/G176.md#page-36) · specific, measurable |
| [G176:A05](guides/G176.md#a05) | 多个角色可由同一人承担；人员与角色配置应在规划时决定。 | [G176 PDF 42](../documents/G176.md#page-42) · roles that can be filled by the same person |
| [G176:A06](guides/G176.md#a06) | 替代方案决策应说明评价因子及权重，不能只凭图中位置推断优先级。 | [G176 PDF 51](../documents/G176.md#page-51) · Add weight if necessary |
| [G178:A01](guides/G178.md#a01) | 一个价值流阶段可以映射一个或多个业务过程，映射不是固定一对一。 | [G178 PDF 13](../documents/G178.md#page-13) · one or more business processes |
| [G178:A02](guides/G178.md#a02) | 价值流从受益者外向内观察价值；业务过程通常聚焦内部操作实现。 | [G178 PDF 13](../documents/G178.md#page-13) · outside-in perspective |
| [G178:A03](guides/G178.md#a03) | 价值流由名称、描述、触发利益相关者及预期价值定义。 | [G178 PDF 15](../documents/G178.md#page-15) · four standard elements |
| [G178:A04](guides/G178.md#a04) | 价值流按顺序或并行动作分为阶段，阶段累积创造利益相关者价值。 | [G178 PDF 16](../documents/G178.md#page-16) · sequential and/or parallel actions |
| [G178:A05](guides/G178.md#a05) | 阶段需名称、描述、参与利益相关者、进入条件、退出条件和价值项。 | [G178 PDF 16](../documents/G178.md#page-16) · Entrance Criteria |
| [G178:A06](guides/G178.md#a06) | 能力与阶段通过使能映射关联。 | [G178 PDF 16](../documents/G178.md#page-16) · required to enable each value stream stage |
| [G178:A07](guides/G178.md#a07) | 价值流及其阶段既不是能力，也不是能力的组成部分。 | [G178 PDF 17](../documents/G178.md#page-17) · not capabilities, nor components of capabilities |
| [G184:A01](guides/G184.md#a01) | 企业范围可跨法人或功能边界，必须按架构工作的范围界定。 | [G184 PDF 20](../documents/G184.md#page-20) · not associated with an organization’s legal or functional boundaries |
| [G184:A02](guides/G184.md#a02) | EA能力包括开发、维护、演进架构以及用架构治理变更的能力。 | [G184 PDF 20](../documents/G184.md#page-20) · ability to use the architecture to govern change activity |
| [G184:A03](guides/G184.md#a03) | 指南处理的是EA能力，不能用组织部门名称代替能力模型。 | [G184 PDF 23](../documents/G184.md#page-23) · explicitly does not discuss an EA department |
| [G184:A04](guides/G184.md#a04) | 架构治理委员会负责过程及完整性、可信度建议；目标架构、豁免和强制遵守目标（enforcement）的决策权属于利益相关者。 | [G184 PDF 61](../documents/G184.md#page-61) · An EA governance board owns process |
| [G184:A05](guides/G184.md#a05) | 批准架构及路线图与批准能力治理政策是不同决策。 | [G184 PDF 68](../documents/G184.md#page-68) · Only the set of stakeholders can approve an architecture and roadmap |
| [G184:A06](guides/G184.md#a06) | 从稳定利益相关者关注点形成视点库，视点所需信息驱动内容元模型和存储库设计。 | [G184 PDF 73](../documents/G184.md#page-73) · viewpoint library |
| [G184:A07](guides/G184.md#a07) | 能力路线图用于组织从当前到期望能力的候选演进与取舍。 | [G184 PDF 107](../documents/G184.md#page-107) · Roadmap |
| [G186:A01](guides/G186.md#a01) | EA可分别支持战略、组合、项目和方案交付，各自规划期、范围与详细程度不同。 | [G186 PDF 30](../documents/G186.md#page-30) · four broad purposes |
| [G186:A02](guides/G186.md#a02) | 视图是面向利益相关者关注点的架构全景表示，不是任意无目的图形。 | [G186 PDF 35](../documents/G186.md#page-35) · a representation of the EA Landscape that addresses |
| [G186:A03](guides/G186.md#a03) | 实施者需要显式上下文、差距、规范和控制，仅交付图纸不足以明确实施责任。 | [G186 PDF 37](../documents/G186.md#page-37) · context, gap, architecture specification, and control |
| [G186:A04](guides/G186.md#a04) | 规范应关联其所服务的要求，便于以要求/规范对评估实现。 | [G186 PDF 37](../documents/G186.md#page-37) · always to link a specification to a requirement |
| [G186:A05](guides/G186.md#a05) | ADM把关键活动与信息流组织成逻辑方法；不能由环图推断唯一固定执行顺序。 | [G186 PDF 72](../documents/G186.md#page-72) · not an activity diagram |
| [G186:A06](guides/G186.md#a06) | 上位架构是在覆盖范围上交叠、详细程度更低的已批准目标，用来引导和约束详细架构。 | [G186 PDF 72](../documents/G186.md#page-72) · less detailed approved target that overlaps in terms of breadth |
| [G186:A07](guides/G186.md#a07) | ABB描述整体架构模型的一部分，其具体内容取决于架构问题及上下文。 | [G186 PDF 73](../documents/G186.md#page-73) · a constituent of the architecture model |
| [G186:A08](guides/G186.md#a08) | 目标架构、豁免及强制遵守目标（enforcement）的决策权属于架构利益相关者；该权力不等同变更执行权（execution rights）。 | [G186 PDF 139](../documents/G186.md#page-139) · Decision rights about the Target Architecture |
| [G186:A09](guides/G186.md#a09) | 正式定义把利益相关者定义为对系统有利益的个人、团队、组织或其类别；本实践指南为治理便利进一步聚焦有批准权的参与者，二者不能无条件替换。 | [G186 PDF 34](../documents/G186.md#page-34) · an individual, team, organization, or classes thereof, having an interest in a system |
| [G188:A01](guides/G188.md#a01) | 架构项目定义包括A–F及需求管理，是形成待实施架构的工作。 | [G188 PDF 19](../documents/G188.md#page-19) · Phases A to F and Requirements Management |
| [G188:A02](guides/G188.md#a02) | 预备阶段建立架构能力，G/H涉及治理和持续变更，均不在本指南架构项目定义内。 | [G188 PDF 19](../documents/G188.md#page-19) · does not include the Preliminary Phase, Phase G, or Phase H |
| [G188:A03](guides/G188.md#a03) | 最终产物需提前定义验收条件，并让项目利益相关者参与以避免期望失配。 | [G188 PDF 51](../documents/G188.md#page-51) · acceptance criteria are a set of conditions |
| [G188:A04](guides/G188.md#a04) | 工作分解之前应确定需开发哪些架构域、详细程度及视图。 | [G188 PDF 54](../documents/G188.md#page-54) · prior to creating the Work Breakdown Structure |
| [G188:A05](guides/G188.md#a05) | 项目经理把计划并入架构工作说明书，并取得赞助人批准。 | [G188 PDF 60](../documents/G188.md#page-60) · sponsor’s approval |
| [G188:A06](guides/G188.md#a06) | 项目关闭要将架构定义、路线图和实施迁移计划等交给实施责任方。 | [G188 PDF 72](../documents/G188.md#page-72) · body responsible for implementation |
| [G18A:A01](guides/G18A.md#a01) | 业务模型说明组织如何创造、交付和获取价值。 | [G18A PDF 11](../documents/G18A.md#page-11) · creates, delivers, and captures value |
| [G18A:A02](guides/G18A.md#a02) | 摘要业务模型通常不足以直接完成风险评估或执行计划。 | [G18A PDF 17](../documents/G18A.md#page-17) · does not normally contain sufficient information |
| [G18A:A03](guides/G18A.md#a03) | 业务架构把业务模型展开为能力、价值流、组织与信息对象等核心要素。 | [G18A PDF 17](../documents/G18A.md#page-17) · business capabilities, value streams, organizational structure and information objects |
| [G18A:A04](guides/G18A.md#a04) | 业务架构发现的缺口和假设冲突应反馈修改业务模型。 | [G18A PDF 17](../documents/G18A.md#page-17) · loop the discussion back |
| [G18A:A05](guides/G18A.md#a05) | 业务模型通常关联愿景阶段，并作为业务架构阶段的重要输入。 | [G18A PDF 19](../documents/G18A.md#page-19) · key input into Phase B |
| [G18A:A06](guides/G18A.md#a06) | 通过能力与价值流映射识别目标模型所需新增或增强的能力及价值交付缺口。 | [G18A PDF 19](../documents/G18A.md#page-19) · identify new capabilities |
| [G190:A01](guides/G190.md#a01) | 信息地图由业务信息概念及其相互关系构成。 | [G190 PDF 12](../documents/G190.md#page-12) · collection of information concepts and their relationships |
| [G190:A02](guides/G190.md#a02) | 信息概念使用业务词汇，先问业务是否需要知道、存储或操作该信息。 | [G190 PDF 12](../documents/G190.md#page-12) · business’ vocabulary |
| [G190:A03](guides/G190.md#a03) | 信息地图是数据架构的来源，但两者不等同；业务信息可能包括主观信息。 | [G190 PDF 16](../documents/G190.md#page-16) · not the same |
| [G190:A04](guides/G190.md#a04) | 如客户感知等经验判断不能自动压缩为单个数据字段。 | [G190 PDF 16](../documents/G190.md#page-16) · not in a form reducible to a data field |
| [G190:A05](guides/G190.md#a05) | A阶段查找既有地图，B阶段扩展业务概念与映射，C/D在可能时转为数据模型，E可反馈更新。 | [G190 PDF 17](../documents/G190.md#page-17) · Phases C and D translate information |
| [G190:A06](guides/G190.md#a06) | 信息视角与能力、价值流及组织地图一起支撑业务价值分析及后续架构阶段。 | [G190 PDF 21](../documents/G190.md#page-21) · joined with business capabilities, value streams, and organization maps |
| [G198:A01](guides/G198.md#a01) | 框架同时描述角色、技能及成功履行角色所需知识深度。 | [G198 PDF 13](../documents/G198.md#page-13) · depth of knowledge required |
| [G198:A02](guides/G198.md#a02) | G198采用四个知识/熟练等级，按每项技能分别表达要求。 | [G198 PDF 15](../documents/G198.md#page-15) · four levels of knowledge or proficiency |
| [G198:A03](guides/G198.md#a03) | 架构师对架构适用性和完整性负责，即充分回应相关利益相关者关注点。 | [G198 PDF 20](../documents/G198.md#page-20) · completeness (fitness-for-purpose) |
| [G198:A04](guides/G198.md#a04) | 架构完整性还包括视图相互联结、调和冲突关注点并呈现取舍。 | [G198 PDF 20](../documents/G198.md#page-20) · connecting all the various views |
| [G198:A05](guides/G198.md#a05) | 关键要求包括复杂系统设计经验、广泛技术经验及一到少数领域的深度。 | [G198 PDF 24](../documents/G198.md#page-24) · Technical Breadth |
| [G198:A06](guides/G198.md#a06) | 全项目范围经验涵盖设计、开发、测试、实施和生产，并支持更实际的设计取舍。 | [G198 PDF 25](../documents/G198.md#page-25) · from design through development, testing, implementation, and production |
| [G203:A01](guides/G203.md#a01) | 指南提供成熟度模型示例，组织可据此建立本地模型。 | [G203 PDF 11](../documents/G203.md#page-11) · organization-specific maturity model |
| [G203:A02](guides/G203.md#a02) | 成熟度评估用于周期性衡量实践改进，而非一次性的证书计数。 | [G203 PDF 11](../documents/G203.md#page-11) · periodically measure improvement |
| [G203:A03](guides/G203.md#a03) | DoC ACMM示例由六个成熟度等级和九个架构要素组成。 | [G203 PDF 13](../documents/G203.md#page-13) · six maturity levels and nine architecture elements |
| [G203:A04](guides/G203.md#a04) | 一种评价方法计算加权平均成熟度，另一种表达九要素在各等级达成的百分比。 | [G203 PDF 14](../documents/G203.md#page-14) · weighted mean |
| [G203:A05](guides/G203.md#a05) | 等级0表示没有企业架构实践，必须与证据不足或未评估区分。 | [G203 PDF 14](../documents/G203.md#page-14) · Level 0: None |
| [G203:A06](guides/G203.md#a06) | CMMI介绍强调能力改进与业务目标对齐，不能仅为分数而改进。 | [G203 PDF 18](../documents/G203.md#page-18) · align operations to business goals |
| [G206:A01](guides/G206.md#a01) | 组织地图涵盖内部单元、伙伴和利益相关者群体间正式或非正式工作关系。 | [G206 PDF 12](../documents/G206.md#page-12) · informal as well as formal |
| [G206:A02](guides/G206.md#a02) | 组织生态可超越法律边界，不应由法人范围自动裁切。 | [G206 PDF 12](../documents/G206.md#page-12) · beyond the legal boundaries |
| [G206:A03](guides/G206.md#a03) | 实际协作包含横向、同级及多对多关系，正式汇报树无法完整表达。 | [G206 PDF 14](../documents/G206.md#page-14) · horizontal, peer-to-peer, or many-to-many relationships |
| [G206:A04](guides/G206.md#a04) | 组织地图中心的企业框代表绘图范围，不能直接当作法人层级。 | [G206 PDF 14](../documents/G206.md#page-14) · total scope to be represented in the map |
| [G206:A05](guides/G206.md#a05) | 组织单元与能力之间明确存在多对多映射。 | [G206 PDF 19](../documents/G206.md#page-19) · with a many-to-many mapping |
| [G206:A06](guides/G206.md#a06) | 组织单元间可以标出有形/无形价值及具体信息类型的流动。 | [G206 PDF 19](../documents/G206.md#page-19) · information types can be shown flowing |
| [G20F:A01](guides/G20F.md#a01) | 架构可按战略、分段和能力三个详细程度层级组织。 | [G20F PDF 20](../documents/G20F.md#page-20) · three levels of detail |
| [G20F:A02](guides/G20F.md#a02) | 业务、数据、应用、技术架构可以存在于每个详细程度层级。 | [G20F PDF 20](../documents/G20F.md#page-20) · may exist at all levels of detail |
| [G20F:A03](guides/G20F.md#a03) | 过渡架构表达架构上有意义的时间状态，通常包含多个能力增量。 | [G20F PDF 22](../documents/G20F.md#page-22) · architecturally significant point in time |
| [G20F:A04](guides/G20F.md#a04) | 过渡架构与向利益相关者释放业务价值关联，也帮助管理增量交付风险。 | [G20F PDF 22](../documents/G20F.md#page-22) · releases of business value |
| [G20F:A05](guides/G20F.md#a05) | 分段架构只需覆盖保证结果所需的阶段与步骤，不必机械完成每一步。 | [G20F PDF 25](../documents/G20F.md#page-25) · only the minimum needed to ensure outcomes are met |
| [G20F:A06](guides/G20F.md#a06) | 敏捷架构趋向产品和结果，并加强业务、数据、应用、技术跨域协作。 | [G20F PDF 35](../documents/G20F.md#page-35) · product-centric |
| [G210:A01](guides/G210.md#a01) | 所给协作模式是可裁剪样例，不是唯一强制流程。 | [G210 PDF 13](../documents/G210.md#page-13) · not the only possible patterns |
| [G210:A02](guides/G210.md#a02) | 架构冲刺应交付最小可行架构，并用演示与回顾改进结果和过程。 | [G210 PDF 23](../documents/G210.md#page-23) · Each sprint will deliver an MVA |
| [G210:A03](guides/G210.md#a03) | 跨开发协作图的虚线表示协作、敏捷治理与支持。 | [G210 PDF 27](../documents/G210.md#page-27) · dashed lines indicate collaboration |
| [G210:A04](guides/G210.md#a04) | 每个MVA可包含部分或全部ADM阶段。 | [G210 PDF 30](../documents/G210.md#page-30) · some or all TOGAF ADM phases |
| [G210:A05](guides/G210.md#a05) | 可以跨B–E形成架构切片，联结业务架构、ABB及方案实现。 | [G210 PDF 30](../documents/G210.md#page-30) · slices (partitions) across Phases B to E |
| [G210:A06](guides/G210.md#a06) | 跨多冲刺工作也需切成适合冲刺且能提供价值的成果，而非只累计文档。 | [G210 PDF 37](../documents/G210.md#page-37) · something valuable for the stakeholders |
| [G211:A01](guides/G211.md#a01) | 业务能力表达业务做什么，不直接说明怎样、为何或由谁实现。 | [G211 PDF 12](../documents/G211.md#page-12) · what a business does |
| [G211:A02](guides/G211.md#a02) | 角色、过程、信息和工具共同使能能力实现。 | [G211 PDF 13](../documents/G211.md#page-13) · roles, processes, information, and tools |
| [G211:A03](guides/G211.md#a03) | 能力地图应相对独立于当前组织、流程、系统和产品结构。 | [G211 PDF 15](../documents/G211.md#page-15) · independent of the current organizational structure |
| [G211:A04](guides/G211.md#a04) | 一个能力可由多个业务单元共同创造或交付，因此不能简单复制组织树。 | [G211 PDF 16](../documents/G211.md#page-16) · multiple business units |
| [G211:A05](guides/G211.md#a05) | 能力分层分类将能力归入类别、层或组，以帮助不同利益相关者理解。 | [G211 PDF 20](../documents/G211.md#page-20) · classifying, grouping, and aligning |
| [G211:A06](guides/G211.md#a06) | 逐级分解将一级能力拆到更细能力；层数以沟通和决策需要为限。 | [G211 PDF 21](../documents/G211.md#page-21) · decomposing each top-level |
| [G211:A07](guides/G211.md#a07) | 热力图颜色取决于所选择的评价属性；成熟度、绩效、价值和成本不可混为一谈。 | [G211 PDF 23](../documents/G211.md#page-23) · Different attributes determine the colors |
| [G212:A01](guides/G212.md#a01) | 基础因素提供数字技术采用的最低可接受准备度。 | [G212 PDF 26](../documents/G212.md#page-26) · minimum acceptable readiness |
| [G212:A02](guides/G212.md#a02) | 因素依赖图只表达强和主导关联，不能当作穷尽因果网络。 | [G212 PDF 26](../documents/G212.md#page-26) · strong and dominant relationships |
| [G212:A03](guides/G212.md#a03) | ABCD横轴为采用广度，纵轴为预期速度，需说明选择理由。 | [G212 PDF 39](../documents/G212.md#page-39) · breadth/extensiveness |
| [G212:A04](guides/G212.md#a04) | 四象限是类型分类，不表示优劣排序。 | [G212 PDF 40](../documents/G212.md#page-40) · do not depict any type of ranking |
| [G212:A05](guides/G212.md#a05) | 采用方式和因素渐进不是互斥路径，可结合企业上下文使用。 | [G212 PDF 44](../documents/G212.md#page-44) · not mutually-exclusive |
| [G212:A06](guides/G212.md#a06) | 愿景阶段识别利益相关者、驱动和关注点并开展就绪评估，结果影响架构推进路径。 | [G212 PDF 46](../documents/G212.md#page-46) · identification of stakeholders |
| [G217:A01](guides/G217.md#a01) | TOGAF应用需要适配组织规模、文化和运营方式。 | [G217 PDF 17](../documents/G217.md#page-17) · scale, culture, and operation |
| [G217:A02](guides/G217.md#a02) | 快速产品交付仍需考虑整体架构，否则可能形成集成、安全和隐私方面技术债务。 | [G217 PDF 20](../documents/G217.md#page-20) · tomorrow’s technical debt |
| [G217:A03](guides/G217.md#a03) | 数字企业上下文包括个人/创始人、团队、团队之团队和持久企业。 | [G217 PDF 31](../documents/G217.md#page-31) · Individual/Founder |
| [G217:A04](guides/G217.md#a04) | 按上下文组合最小EA服务集，为当前决策及下一阶段准备提供支持。 | [G217 PDF 31](../documents/G217.md#page-31) · minimal set of Enterprise Architecture services |
| [G217:A05](guides/G217.md#a05) | EA服务是交付EA能力的机制；能力描述特定条件下可做什么。 | [G217 PDF 49](../documents/G217.md#page-49) · delivery mechanism |
| [G217:A06](guides/G217.md#a06) | 服务涌现模型以矩阵关联服务与成长上下文，表示适用关联而不是人员层级。 | [G217 PDF 59](../documents/G217.md#page-59) · services per context |
| [G21B:A01](guides/G21B.md#a01) | C-MDM是人员、过程、组织和系统组合，用来把核心客户数据当作资产管理。 | [G21B PDF 21](../documents/G21B.md#page-21) · people, processes, organizations, and systems |
| [G21B:A02](guides/G21B.md#a02) | 核心客户数据是跨部门共享的信息，包含标识、联系、偏好同意和关系等。 | [G21B PDF 21](../documents/G21B.md#page-21) · shared across the organization’s departments |
| [G21B:A03](guides/G21B.md#a03) | 自动化质量及去重算法不能解决所有不确定性，需要人工流程配合。 | [G21B PDF 21](../documents/G21B.md#page-21) · algorithms do not produce certainty |
| [G21B:A04](guides/G21B.md#a04) | 集成优先级可考虑业务价值、客户量、当前质量和复杂度，并结合相邻项目依赖。 | [G21B PDF 28](../documents/G21B.md#page-28) · business value, customers volume and current quality, complexity |
| [G21B:A05](guides/G21B.md#a05) | 核心客户数据字段清单是比较基线或检查表，不是无条件强制范围。 | [G21B PDF 37](../documents/G21B.md#page-37) · not be used as a mandatory guideline |
| [G21B:A06](guides/G21B.md#a06) | 整合、协作及集中三种集成风格可以组合；需要明确主数据权威及传播机制。 | [G21B PDF 48](../documents/G21B.md#page-48) · not mutually-exclusive |
| [G21D:A01](guides/G21D.md#a01) | GRM为公共部门提供共同视角以规划和执行转型。 | [G21D PDF 21](../documents/G21D.md#page-21) · common way to view themselves |
| [G21D:A02](guides/G21D.md#a02) | 模型是可用于描述不同公共部门业务的参考模板。 | [G21D PDF 21](../documents/G21D.md#page-21) · reference model template |
| [G21D:A03](guides/G21D.md#a03) | 分类分段帮助识别变化影响及架构层之间的依赖。 | [G21D PDF 21](../documents/G21D.md#page-21) · map dependencies between the architecture layers |
| [G21D:A04](guides/G21D.md#a04) | GRM定位于ADM业务架构阶段，为公共部门业务建模提供参考。 | [G21D PDF 24](../documents/G21D.md#page-24) · Phase B: Business Architecture |
| [G21D:A05](guides/G21D.md#a05) | 领域分类表区分功能、服务及描述，形成参考分类而非现成人员汇报关系。 | [G21D PDF 26](../documents/G21D.md#page-26) · Function |
| [G21D:A06](guides/G21D.md#a06) | 十一领域构成政府部门分段视角，变化驱动用于说明结果与影响。 | [G21D PDF 67](../documents/G21D.md#page-67) · 11 sectors |
| [G21H:A01](guides/G21H.md#a01) | 业务架构整合能力、端到端价值、信息和组织等多维业务视图及相互关系。 | [G21H PDF 18](../documents/G21H.md#page-18) · holistic, multi-dimensional business views |
| [G21H:A02](guides/G21H.md#a02) | 业务系统包括硬软资源、政策、过程、标准和人员，共同实现业务能力。 | [G21H PDF 19](../documents/G21H.md#page-19) · together implement a business capability |
| [G21H:A03](guides/G21H.md#a03) | DBRM以十个核心要素覆盖数字、战略、结构和运营四域。 | [G21H PDF 24](../documents/G21H.md#page-24) · ten (10) core elements |
| [G21H:A04](guides/G21H.md#a04) | 高层图仅说明实体存在，不能据其布局推断详细关系。 | [G21H PDF 24](../documents/G21H.md#page-24) · says nothing about the detailed relationships |
| [G21H:A05](guides/G21H.md#a05) | 运营模型把业务模型转成关联的业务能力、过程和运行环境，并按战略分配资源。 | [G21H PDF 34](../documents/G21H.md#page-34) · translates the business model |
| [G21H:A06](guides/G21H.md#a06) | 数字架构使用可配置可组合的模块化构建块来支持共同演进和敏捷。 | [G21H PDF 39](../documents/G21H.md#page-39) · configured and assembled |
| [G21H:A07](guides/G21H.md#a07) | TOGAF业务、数据、应用和技术域具有不同对象与责任，可与DBRM要素建立映射。 | [G21H PDF 46](../documents/G21H.md#page-46) · Business Architecture defines |
| [G21I:A01](guides/G21I.md#a01) | MSA是架构风格，构建独立、自包含的服务；不是产品、框架或平台。 | [G21I PDF 16](../documents/G21I.md#page-16) · not a product, framework, or platform |
| [G21I:A02](guides/G21I.md#a02) | 微服务实现原子业务功能，并以独立、单一责任、自包含为关键特征。 | [G21I PDF 16](../documents/G21I.md#page-16) · implements an Atomic Business Function |
| [G21I:A03](guides/G21I.md#a03) | ABF是企业内交付价值的最小业务功能单位，通常提供支撑一个企业能力的服务。 | [G21I PDF 35](../documents/G21I.md#page-35) · smallest unit of business function |
| [G21I:A04](guides/G21I.md#a04) | 业务功能价值流必须处于企业上下文并与整体目标架构一致。 | [G21I PDF 36](../documents/G21I.md#page-36) · align with the overall Target Architecture |
| [G21I:A05](guides/G21I.md#a05) | MSA数据架构由所服务业务功能管理的数据及必要外部数据源约束。 | [G21I PDF 38](../documents/G21I.md#page-38) · data managed by the business function |
| [G21I:A06](guides/G21I.md#a06) | 每个微服务有服务契约和接口/API，可供其他架构构件使用的微服务登记在目录中。 | [G21I PDF 41](../documents/G21I.md#page-41) · defined service contract |
| [G21I:A07](guides/G21I.md#a07) | 迁移需要明确工作包和过渡架构的业务价值、成本及企业组合协调。 | [G21I PDF 46](../documents/G21I.md#page-46) · business value and cost of work packages |
| [G21I:A08](guides/G21I.md#a08) | 实施治理验证项目符合目标架构，并处理实现驱动的变更请求。 | [G21I PDF 48](../documents/G21I.md#page-48) · conformance with the Target Architecture |
| [G233:A01](guides/G233.md#a01) | 示例模型常用嵌套表达关系，关系仍存在，工具应保留其含义而非仅视觉框。 | [G233 PDF 21](../documents/G233.md#page-21) · implied by having elements nested |
| [G233:A02](guides/G233.md#a02) | 能力类型不说明怎样使用；映射并实例化到价值流后才能评价其实际绩效。 | [G233 PDF 32](../documents/G233.md#page-32) · business capability instance |
| [G233:A03](guides/G233.md#a03) | 能力与阶段通过使能关系映射，识别交付利益相关者价值所必需的能力。 | [G233 PDF 35](../documents/G233.md#page-35) · required to enable each value stream stage |
| [G233:A04](guides/G233.md#a04) | 能力实例用于表达同一能力在组织不同位置的使用，避免在能力目录中冲突或重复。 | [G233 PDF 36](../documents/G233.md#page-36) · otherwise conflict or create duplicates |
| [G233:A05](guides/G233.md#a05) | 实例分析连接参与者、利益相关者、资源、应用和过程的差距与投资计划。 | [G233 PDF 36](../documents/G233.md#page-36) · actors, stakeholders, resources, applications, or processes |
| [G233:A06](guides/G233.md#a06) | 可复用既有实例支撑新价值流，也可建立或改进实例以适应新要求。 | [G233 PDF 40](../documents/G233.md#page-40) · new or improved business capability instances |
| [G233:A07](guides/G233.md#a07) | 能力增量按依赖顺序组合成台阶，每个台阶应维持价值流可运行。 | [G233 PDF 43](../documents/G233.md#page-43) · preserve a functional value stream |
| [G234:A01](guides/G234.md#a01) | 元数据管理包括规划、实施和控制活动，用于获得高质量、集成的元数据。 | [G234 PDF 14](../documents/G234.md#page-14) · planning, implementation, and control activity |
| [G234:A02](guides/G234.md#a02) | 需求既可由法规/业务用例自上而下，也可由数据问题和数据集自下而上识别。 | [G234 PDF 23](../documents/G234.md#page-23) · top-down approach |
| [G234:A03](guides/G234.md#a03) | 元数据质量由过程和验证工作流保障；规范式和协作式方式服务不同上下文。 | [G234 PDF 24](../documents/G234.md#page-24) · processes and validation workflows |
| [G234:A04](guides/G234.md#a04) | 元数据IT方案由技术功能、数据模型和更新/验证流程共同构成。 | [G234 PDF 25](../documents/G234.md#page-25) · combination of technologies |
| [G234:A05](guides/G234.md#a05) | 元数据分为业务、技术、运营三类，其来源和维护方式不同。 | [G234 PDF 26](../documents/G234.md#page-26) · Business metadata |
| [G234:A06](guides/G234.md#a06) | 交换可选择手工导入、来源推送或存储库代理拉取，需定义范围和协作契约。 | [G234 PDF 28](../documents/G234.md#page-28) · Manual ingestion |
| [G234:A07](guides/G234.md#a07) | 拉取代理可能访问多个系统甚至实际数据，需要安全审计并评估侵入性。 | [G234 PDF 29](../documents/G234.md#page-29) · Security audit is required |
| [G238:A01](guides/G238.md#a01) | BI能力组合人员、过程、组织和系统，将决策相关数据转成增值信息。 | [G238 PDF 13](../documents/G238.md#page-13) · create value-added information |
| [G238:A02](guides/G238.md#a02) | 质量与元数据血缘需覆盖运营数据源到数据消费的完整价值链。 | [G238 PDF 14](../documents/G238.md#page-14) · from operational data sources to data consumption |
| [G238:A03](guides/G238.md#a03) | 共享数据及控制技术多样性用于评价重复平台、数据复制和维护复杂度。 | [G238 PDF 17](../documents/G238.md#page-17) · Control Technical Diversity |
| [G238:A04](guides/G238.md#a04) | 参考过渡步骤2由数据仓库向新平台提供清洗数据，同时引入新的数据源和用途。 | [G238 PDF 20](../documents/G238.md#page-20) · data warehouse feeds |
| [G238:A05](guides/G238.md#a05) | 后续步骤允许消费方逐步迁移，并显式呈现新平台与仓库并存时的数据流。 | [G238 PDF 22](../documents/G238.md#page-22) · step-by-step approach |
| [G238:A06](guides/G238.md#a06) | 本指南参考目标让新平台覆盖历史数据仓库范围并成为历史数据权威。 | [G238 PDF 25](../documents/G238.md#page-25) · single point of truth for historical data storage |
| [G238:A07](guides/G238.md#a07) | 业务使用监测可包括数据科学模型漂移，不能仅监测基础设施。 | [G238 PDF 39](../documents/G238.md#page-39) · model drifting |
| [G238:A08](guides/G238.md#a08) | 完整示例需求清单在配套电子表格中，PDF正文不等于该外部清单的全部内容。 | [G238 PDF 39](../documents/G238.md#page-39) · spreadsheet file |
| [G242:A01](guides/G242.md#a01) | 能效分析不能忽略制造ICT资产的环境足迹。 | [G242 PDF 29](../documents/G242.md#page-29) · environmental footprint required to build |
| [G242:A02](guides/G242.md#a02) | 架构政策需反映业务可持续政策，并由适当治理保障应用。 | [G242 PDF 30](../documents/G242.md#page-30) · Business Policies for Sustainability |
| [G242:A03](guides/G242.md#a03) | 信息系统改造应以年度环境评估为起点，涵盖运行、制造、云、网络和终端等来源。 | [G242 PDF 61](../documents/G242.md#page-61) · yearly environmental assessment |
| [G242:A04](guides/G242.md#a04) | 环境决策要考虑整个业务生态及整体关系，避免只优化局部指标。 | [G242 PDF 75](../documents/G242.md#page-75) · entire business ecosystem |
| [G242:A05](guides/G242.md#a05) | 需要明确哪些环境影响决策提交何种治理机构，阈值必须按组织设定。 | [G242 PDF 78](../documents/G242.md#page-78) · criteria determining whether a decision |
| [G242:A06](guides/G242.md#a06) | ADM用于从基线到目标的增量可持续能力建设，过渡架构承担中间状态。 | [G242 PDF 85](../documents/G242.md#page-85) · incremental approach supported by Transition Architecture |
| [G242:A07](guides/G242.md#a07) | 指南提出服务提供者环境数据的最小模型；该页说明当时缺乏统一交换标准。 | [G242 PDF 98](../documents/G242.md#page-98) · A data standard for that purpose is proposed |
| [G248:A01](guides/G248.md#a01) | 变更画像区分快速、功能和稳健三类，用来调整变更方法和关注点。 | [G248 PDF 14](../documents/G248.md#page-14) · three broad change profiles |
| [G248:A02](guides/G248.md#a02) | ABB描述逻辑模型中的架构构件，相关SBB表达物理/运营实现。 | [G248 PDF 19](../documents/G248.md#page-19) · physical/operational implementations |
| [G248:A03](guides/G248.md#a03) | 架构师依据选定视点形成包含相关实体、构建块及关系的视图。 | [G248 PDF 19](../documents/G248.md#page-19) · selected viewpoints |
| [G248:A04](guides/G248.md#a04) | 实体与构建块由制品描述，并组织进特定交付物以沟通和推进变更。 | [G248 PDF 24](../documents/G248.md#page-24) · documented by various artifacts and organized into specific deliverables |
| [G248:A05](guides/G248.md#a05) | 上下文解释为何、概念解释什么、逻辑解释如何、物理解释用什么实现。 | [G248 PDF 25](../documents/G248.md#page-25) · four levels of abstraction |
| [G248:A06](guides/G248.md#a06) | 上下文识别的上位架构为后续概念与变更提供约束。 | [G248 PDF 30](../documents/G248.md#page-30) · superior architecture |
| [G248:A07](guides/G248.md#a07) | 价值实现阶段需检查契约承诺、服务性能、KPI和利益相关者预期价值。 | [G248 PDF 38](../documents/G248.md#page-38) · satisfaction of the KPIs |
| [G249:A01](guides/G249.md#a01) | 岗位是通常具有雇佣契约的正式位置；角色是活动及技能组合；任务是分配的具体工作。 | [G249 PDF 16](../documents/G249.md#page-16) · Job means |
| [G249:A02](guides/G249.md#a02) | 一人可能承担多个角色，也可能多人分别只承担一个角色；人员与角色不能默认一对一配置。 | [G249 PDF 16](../documents/G249.md#page-16) · multiple roles |
| [G249:A03](guides/G249.md#a03) | 首席架构师是企业架构师的特例，重点把架构融入战略和运营上下文。 | [G249 PDF 17](../documents/G249.md#page-17) · special case of an Enterprise Architect |
| [G249:A04](guides/G249.md#a04) | 解决方案工作受企业和分段上位架构指引；该关系本身不证明人事汇报。 | [G249 PDF 17](../documents/G249.md#page-17) · superior architectures |
| [G249:A05](guides/G249.md#a05) | 分段是为管理和控制而组合的一组连贯能力，通常按能力组合或变更计划管理。 | [G249 PDF 21](../documents/G249.md#page-21) · coherent grouping of capabilities |
| [G249:A06](guides/G249.md#a06) | 角色技能要求涵盖应用、架构、业务、变更、数据、通用、法律和技术类别。 | [G249 PDF 26](../documents/G249.md#page-26) · categories of skills |
| [G249:A07](guides/G249.md#a07) | 本指南提供描述性、可裁剪的实践起点；组织可直接采用或显著调整，不能把示例角色、层级或数值自动认定为企业强制规则。 | [G249 PDF 14](../documents/G249.md#page-14) · The TOGAF Standard is descriptive, not prescriptive |
| [G249:A08](guides/G249.md#a08) | 有效架构实践首先需要适当利益相关者的明确mandate；仅有角色名和技能清单不足以证明实践有何任务、范围与授权。 | [G249 PDF 14](../documents/G249.md#page-14) · Have a clear mandate from the appropriate relevant stakeholders |
| [G249:A09](guides/G249.md#a09) | 先识别企业需要完成的架构任务，再使人员角色、技能和经验与任务对齐；范围包括内部人员和外部顾问。 | [G249 PDF 14](../documents/G249.md#page-14) · aligning necessary staff roles, skills, and experience with the architecture tasks the enterprise needs to be performed |
| [G249:A10](guides/G249.md#a10) | 正式认可架构师的技能和能力是建立与维持专业架构组织的一项工作；角色任命、技能证据和认可结论应分别理解。 | [G249 PDF 14](../documents/G249.md#page-14) · Formally recognize the skills and capabilities of architects |
| [G249:A11](guides/G249.md#a11) | 架构实践需要能力发展路径，建立最低胜任要求，并对架构活动达到可接受水平形成信心；发展不止是罗列课程。 | [G249 PDF 14](../documents/G249.md#page-14) · Provide a competency development path for architects to ensure minimal competency levels |
| [G249:A12](guides/G249.md#a12) | 员工可按所需技能自评并制定培训和职业计划，必要时由导师支持；自评是一类输入，不自动等于独立确认的能力或认证。 | [G249 PDF 15](../documents/G249.md#page-15) · Enable employees to self-assess against a set of required skills |
| [G249:A13](guides/G249.md#a13) | Chief Architect的关键工作是沟通并取得重大业务/技术变革的承诺，将架构需求与企业高层的战略和运营目标相连接；其输出价值不只是一张架构图。 | [G249 PDF 17](../documents/G249.md#page-17) · responsible for communicating and gaining commitment |
| [G249:A14](guides/G249.md#a14) | Chief Architect把业务/技术战略、目标与目的转化为运营模型变化，领导总体架构全景、重大约束和高风险变革，并支持架构团队发展。 | [G249 PDF 18](../documents/G249.md#page-18) · Translating business and technology strategies, goals, and objectives into related changes in the operating model |
| [G249:A15](guides/G249.md#a15) | Enterprise Architect的范围跨多个分段，不局限于单一方案、产品、技术或生命周期环节；通过跨分段路线图、原则和政策塑造架构全景。 | [G249 PDF 19](../documents/G249.md#page-19) · They create roadmaps for change across multiple segments |
| [G249:A16](guides/G249.md#a16) | Enterprise Architect的首要责任是建立并演进解决方案构件的集成、互操作与治理条件；因此必须处理跨分段的依赖、约束和协同。 | [G249 PDF 19](../documents/G249.md#page-19) · conditions for the integration, interoperability, and governance of solution components |
| [G249:A17](guides/G249.md#a17) | Segment Architect围绕分段内系统、子系统与构件的创建、集成、互操作和演进工作，使专家和Solution Architect清楚分工并实现端到端业务服务水平。 | [G249 PDF 22](../documents/G249.md#page-22) · creation, integration, interoperability, and evolution of the systems, sub-systems, and components within a segment(s) |
| [G249:A18](guides/G249.md#a18) | Solution Architect将为明确需求选择的系统、子系统、构件及互操作安排纳入统一变更路线图，通过可实施的过渡架构分步交付价值。 | [G249 PDF 23](../documents/G249.md#page-23) · a series of implementable Transition Architectures |
| [G249:A19](guides/G249.md#a19) | 解决方案职责包括服务、流程、组织、运营模型和技术变化，还包括生产环境中的运营、维护和演进安排；不能仅按应用部署理解解决方案架构。 | [G249 PDF 24](../documents/G249.md#page-24) · including the planned operation, maintenance, and evolution of the solution within a production environment |
| [G249:A20](guides/G249.md#a20) | 安全、隐私和测试要求是Solution Architect必须充分考虑的内容；制品完整不等于这些要求已经得到满足。 | [G249 PDF 24](../documents/G249.md#page-24) · Taking full account of the requirements for security, privacy, and testing of solutions |
| [G249:A21](guides/G249.md#a21) | Solution Architect需要明确不同解决方案拓扑及系统/构件选项的收益与问题，包含本地与非本地方案；选项权衡应有具体需求与约束依据。 | [G249 PDF 24](../documents/G249.md#page-24) · benefits and issues associated with different solution topologies |
| [G249:A22](guides/G249.md#a22) | 解决方案实施采用基于风险的治理，并管理变更请求和必要的规格偏离；规则符合性、例外请求与真实批准不能混为一个状态。 | [G249 PDF 24](../documents/G249.md#page-24) · including managing requests for changes and any necessary deviations from specifications |
| [G249:A23](guides/G249.md#a23) | 潜在KPI包括利益相关者满意、服务水平和约定交付边界；时间、资源与成本边界须反映具体变革的可能波动，不能直接把示例3/5或占位四分位当作企业统一门槛。 | [G249 PDF 25](../documents/G249.md#page-25) · boundaries must be properly set to reflect the potential variation relevant to a specific change |
| [G249:A24](guides/G249.md#a24) | Background（1）：有一定理解，但依赖专家。它描述实践能力和支持条件，不是零能力，也不是缺失证据的默认值。 | [G249 PDF 27](../documents/G249.md#page-27) · Some understanding but reliant on specialists. |
| [G249:A25](guides/G249.md#a25) | Aware（2）：理解问题，并可在专家支持下处理问题。需要把专家支持作为任务执行条件，不能将数值2等同独立胜任。 | [G249 PDF 27](../documents/G249.md#page-27) · Understands and can address issues with the support of specialists. |
| [G249:A26](guides/G249.md#a26) | Knowledgeable（3）：有足够细节知识支持有效决策，困难情境仍需专家输入。因此熟练度必须结合任务复杂性、独立性和支持安排解释。 | [G249 PDF 27](../documents/G249.md#page-27) · Good detail enabling effective decision-making, requiring specialist input in difficult situations. |
| [G249:A27](guides/G249.md#a27) | Expert（4）：具有丰富经验以及实践和应用知识。该等级不是仅凭知识问答、自报分数或课程完成即可证明的能力。 | [G249 PDF 27](../documents/G249.md#page-27) · Extensive experience, practical, and applied knowledge. |
| [G249:A28](guides/G249.md#a28) | 表5-2的列覆盖观察：Enterprise、Business Domain、Data Domain、Application Domain、Technology Domain、Solution共六个角色列；Chief和Segment没有独立数值列。不能把Enterprise列自动复制为Chief要求，也不能把四个domain列无规则地合并成Segment要求。 | [G249 PDF 27](../documents/G249.md#page-27) · Solution Architect |
| [G249:A29](guides/G249.md#a29) | 附录A的Open CA是依据经验评估专业架构师所需技能与经验的认证体系；它与某一项目的角色任命和单项技能熟练度是不同记录。 | [G249 PDF 31](../documents/G249.md#page-31) · experience-based certification assessing the required skills and experience |
| [G249:A30](guides/G249.md#a30) | Open CA提供Certified、Master Certified、Distinguished三个认证层次，分别关联受协助/监督的贡献、独立领导并负责交付、以及领导力和影响广度深度。不能把这些认证层次换算为表5-1的四级技能值。 | [G249 PDF 31](../documents/G249.md#page-31) · Three levels of certification are available |
| [G249:A31](guides/G249.md#a31) | 角色、技能和熟练度模型是企业定制实践的建议起点，需要围绕具体需求持续调整，以形成有效的实践与发展机制。 | [G249 PDF 30](../documents/G249.md#page-30) · shape and customize it to your specific needs |
