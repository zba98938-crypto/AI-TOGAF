# togaf-requirements 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## BI 与分析需求规格

- `id`：`bi-requirements-profile`
- 英文名：BI and Analytics Requirements Profile
- 决策问题：分析平台需要满足什么可验证业务要求？
- 主责技能：`togaf-requirements`
- 来源：G238 §4；G238 §4.4（特别是本地补写示例说明）；G238 §3.1阶段B、表4-1、表4-2；G238 §2.2、表4-2；G238 §2.3、表4-3、§4.4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_function, statement, verification
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：41；对象类型：analytics_requirement, guide:bi_requirement_provenance, ops:bi_usage, ops:functional_coverage
- 关系类型：traces_to
- 关联交付物：`architecture-requirements-specification`

### 分析步骤

1. 从业务功能识别需求
2. 拆成原子独立陈述
3. 定义验证方式
4. 分离产品约束与业务要求
5. 记录来源身份再提炼需求
6. 按功能解释系统，检查原子/唯一/可验证
7. 区分项目需求和本地示例与官方配套记录
8. 未找到电子表格时只交付局部候选与缺口
9. 从用户痛点提炼决策及业务对象
10. 连接参考目标，但另设有来源的项目度量
11. 让赞助人提供价值/复杂性排序规则并保留理由
12. 定义从设计到持续维护的责任
13. 检查测量结果和目标/方向不同
14. 加载随技能携带的完整源表，保留参考分组/ID/出处
15. 限定项目范围和时点，逐项寻找组织活动或实际应用功能证据
16. 区分已见、计划、未知和有理由不适用
17. 不得以宏观组或产品名称推断子项覆盖
18. 对缺口形成具体补证/实现/复评行动，不合成成熟度分数

### `analytics_requirement` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_function` | 业务功能引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `statement` | 原子陈述或问题 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `verification` | 验证方法与验收证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `priority` | 优先级及排序依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `source` | 该条内容的输入来源 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `constraint` | 适用约束 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:bi_requirement_provenance` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `statement` | 原子陈述或问题 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `function` | “系统”指的功能子系统 | BI需求涉及的功能子系统；不是泛指整套技术系统，必须明确功能边界；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `requirement_origin` | project-user-input/local-translation-added-example/verified-companion区别 | BI需求来源分类；项目输入、本地译注补例、经核实配套源明确分开；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `origin_locator` | 具体出处 | BI需求具体来源定位；项目访谈、本地补例和配套源分别可回查；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `official_requirement_id` | 未取得配套源则unknown | 经核实配套资料的官方需求ID；未取得该资料时只写unknown，不自造官方编号；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `verification` | 验证方法与验收证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `completeness_claim` | 项目局部/示例/全集的严格边界 | 需求集合覆盖边界；区分项目局部、示例与经核实配套全集；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `validation_criteria` | 清晰原子唯一可验证，不混成测试细节 | BI需求验收标准；清晰、原子、唯一且可验证，与测试步骤和设计细节区分；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `companion_sheet` | 配套电子表格是否实际找到并读完 | 配套BI需求表的取得和阅读状态；未取得不能声明已覆盖官方全集；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `ops:bi_usage` 必填字段（13）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `user` | 现实业务用户/角色 | BI实际业务用户或角色；不能只写技术系统，不把候选用户当已采用人数；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `pain` | 业务痛点 | BI用户的业务痛点；应来自业务材料，不用技术平台不足替代实际决策问题；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `decision` | 要改善的决策 | 待作或已作的业务决定；写问题、选项与结果边界，建议不自动成为批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `business_objects` | 先业务对象再技术数据 | 支撑BI用途的业务对象；先写业务身份与粒度，不直接替换为技术表名；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `sponsor` | 业务/IT赞助 | 项目或BI用途的业务/IT赞助责任方；尚未接受职责须明确候选而非默认授权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `goal_reference` | 带ID/源行的参考目标，参考身份不可删 | BI用途关联的参考目标ID与源行；参考目标不证明本地目标已实现；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `metric` | 单位/时间/基线/目标/观测/规则/依据 | 业务用途度量；列定义、单位、周期、基线、目标和实际观测，未知不作为零值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `priority_rationale` | 价值和复杂性或数据可得性的明确理由 | BI用途优先级理由；说明价值、复杂性或数据可得性及证据，未知不计零；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `priority_rule` | 项目排序规则，不借TOGAF名义自定权重 | 项目明确的BI排序规则及出处；未给权重不计算加权分，不冒称TOGAF默认算法；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `lifecycle` | 从设计到维护的组织 | 用途或模型从设计到维护的生命周期；列业务和技术责任，发布计划不能当实际运行；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `data_access` | 访问/隐私限制 | BI用途数据的访问与隐私约束；注明角色、使用目的及限制，不能默认公开；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 项目访谈证据 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `gap` | 缺口与未验证结论 | 未覆盖或未验证事项；记录影响与后续补证，不把未知写成已通过；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `ops:functional_coverage` 必填字段（15）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `reference_id` | 稳定参考行ID | 可携带来源行稳定ID；不能改写成本地实现ID或按名称去重；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_kind` | 业务/应用参考功能 | 参考节点种类；按来源业务/应用功能或sector/function/service分层，不跨体系混用；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_name` | 源行功能名 | 来源参考行原始名称；同名异义必须保留完整ID与路径；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_definition` | 源行完整含义 | 来源参考行完整业务含义；不以简写标签替代定义和排除边界；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_group` | 源参考分组，不是部署边界 | 来源参考分组；仅用于来源组织，不当作强制部署边界；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_level` | 宏观/独立高层/组内子功能，保留源表粒度 | 参考节点原始粒度；保留宏观、高层、组内子功能或目录层次，不自行压平；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_scope` | 源表分组适用范围，不从标签隐含推断 | 来源参考分组适用边界；未说明处保留未知，不由名称暗推范围；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `source_locator` | 源表行 | 来源章节、表和具体行定位；不以笼统指南名称代替可回查出处；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_identity` | reference-only，不能当实现对象 | 参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `project_scope` | 评估范围与时间 | 功能覆盖评估的项目范围与时点；范围外须明确理由，不能默认为未覆盖；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `coverage_status` | evidenced-in-example/planned/unknown/out-of-scope-with-reason | 参考功能覆盖结论；区别证据覆盖、计划、未知和附理由的不适用；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `implementation_ref` | 真实/计划项目实现或unknown | 参考功能对应的本地实现或计划引用；unknown不是已实现证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 范围内观察，不由名称推断 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `gap_action` | 不足/不适用理由及下一步 | 参考功能覆盖不足或不适用的处置；保留原因、责任方及下一步；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `source_uncertainty` | 本地翻译/缺失来源边界 | 来源缺失、译注或解释的不确定性；不把本地补充写成原文核实结论；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 架构业务变革与冲刺待办

- `id`：`architecture-backlog`
- 英文名：Architecture Business Change and Sprint Backlog
- 决策问题：先处理哪些业务变革，当前团队冲刺承诺哪些架构结果？
- 主责技能：`togaf-requirements`
- 来源：G210 §2、§3.3.2–3.3.4；G20F §4.5、§5.2.3、§5.3.2；G20F §4.5 L304–327；G20F §5.2.3 L529–547；G20F §5.3.2 L601–632
- 定义状态：`guide-body-located-with-explicit-project-operational-contract`
- 必需输入：原始目标/需求/变更及来源, 业务优先级及理由, 依赖与验收条件, 团队时间盒、目标、可用容量及估算依据
- 可选输入：已有模型/待办/历史决策, 组织特定规则及证据
- 缺输入策略：缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。
- 字段总数：21；对象类型：guide:backlog_item, guide:sprint, goal, requirement, abb, sbb, guide:mva_scope
- 关系类型：guide:backlog_depends_on, guide:scheduled_in, g20f:refines, g20f:constrains-story, g20f:allocated-to-sbb, g20f:included-in-mva, g20f:story-depends-on, realizes
- 关联交付物：`architecture-requirements-specification`, `implementation-migration-plan`, `architecture-definition-document`

### 分析步骤

1. 将每项业务需求归一为稳定ID，保留来源、价值、责任人与验收条件；未知不填零。
2. 依据利益相关者给定排序及依赖确定候选顺序；没有权重时不计算分数。
3. 区分业务变革范围与团队冲刺范围；以相同ID选择近期工作，记录目标与容量。
4. 核对前置工作及所选估算是否在声明容量内；未知估算不能给出容量通过。
5. 以演示证据更新状态；未完成项回流业务待办，保存历史且不自动承诺下一冲刺。

### `guide:backlog_item` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `backlog_scope` | 需求所属的业务变革待办范围；冲刺选择以关系和sprint_id表达 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `business_value` | 需求对相关利益人的预期增量价值，允许定性且需来源 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `priority` | 利益相关者明确给定的相对顺序；不是量化价值评分 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `priority_basis` | 排序依据及提出该判断的来源，不由行号推断 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `owner` | 负责澄清、交付或处理该项的角色；不是隐含审批人 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `status` | 该工作产品自身的业务流程状态，独立于模型批准/实现状态 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `acceptance_criteria` | 判断待办成果达成的可检查条件，须符合原始目标 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `estimate` | 带数值或null、单位、依据与estimated/unknown状态的项目估算 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `sprint_id` | 所选冲刺稳定ID，未分配为unassigned；多次选择保留history | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `dependencies` | 前置待办ID，与guide:backlog_depends_on关系逐项一致 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `source_refs` | 支持本条业务内容的来源ID列表，区别指南定义来源 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `history` | 按观察时间保留状态/结论与证据的历史，不由后续结果覆盖 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |

### `guide:sprint` 必填字段（8）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `goal` | 整个冲刺的可验证目标；不能由选中事项标题自动代替 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `timebox` | 项目声明的开始、结束日期及来源；不是TOGAF固定周期 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `team` | 本冲刺共同负责交付的团队范围 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `capacity` | 含value、unit、basis的可用投入；未知不能按零处理 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `selected_item_ids` | 冲刺选择的待办稳定ID；与选择关系一致 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `planning_status` | 该时间点的冲刺规划状态，不代替结果 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `outcome` | 冲刺规划时点是否已有成果观察；未观察需明示 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `snapshot_at` | 当前规划记录所对应的观察时点 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |

其余字段（1）：`name`

### 输出

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

---

合计 2 个工作产品，62 个字段。
