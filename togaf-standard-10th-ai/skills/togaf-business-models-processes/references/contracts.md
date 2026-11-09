# togaf-business-models-processes 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 客户旅程

- `id`：`customer-journey`
- 英文名：Customer Journey
- 决策问题：客户如何经历服务并取得价值？
- 主责技能：`togaf-business-models-processes`
- 来源：G20F §5.2.1、§5.3.1、§5.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, actor, goal, touchpoint
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：8；对象类型：customer_journey_stage, journey_stage, value_stream
- 关系类型：has_journey_stage, precedes, traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 确定客户语境与目标
2. 识别触点和体验阶段
3. 记录证据痛点与期望
4. 连接业务运营和改进

### `customer_journey_stage` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `order` | 明确次序号 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `actor` | 执行活动的主体 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `touchpoint` | 客户与服务交互触点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `experience` | 观察或期望体验 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `pain_point` | 有证据的体验痛点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `outcome` | 业务或客户成果 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（2）：`name`、`goal`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 客户画像

- `id`：`customer-persona`
- 英文名：Customer Persona
- 决策问题：为谁设计业务和产品体验？
- 主责技能：`togaf-business-models-processes`
- 来源：G20F §5.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, segment, goals, behaviors
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：persona
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 从研究划分相关群体
2. 归纳目标行为需求
3. 区分观察和假设
4. 检验代表性并链接旅程

### `persona` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `segment` | 客户或业务分群 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `goals` | 用户群体或业务目标 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `behaviors` | 观察到的行为 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `needs` | 用户需求 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `assumptions` | 待验证假设 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 政府参考模型裁剪

- `id`：`government-reference-tailoring`
- 英文名：Government Reference Model Tailoring
- 决策问题：怎样把政府参考分类映射到实际职责？
- 主责技能：`togaf-business-models-processes`
- 来源：G21D §1–12；G21D §1.3、§2.1–12.1、§8.1、§11.1；G21D §1.3、§8.1、§11.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, sector, function, service
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：22；对象类型：government_service, guide:government_overlay, guide:government_reference_node
- 关系类型：traces_to, guide:reference_classifies
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 区分部门功能服务
2. 选择适用范围并映射本地服务
3. 识别跨部门共享
4. 记录偏差与理由

### `government_service` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `sector` | 参考政府部门分类 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `function` | 参考功能或实际功能映射 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `service` | 服务对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `local_owner` | 本地责任部门或角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:government_overlay` 必填字段（13）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `reference_id` | 可携带参考目录稳定ID | 可携带来源行稳定ID；不能改写成本地实现ID或按名称去重；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_kind` | sector/function/service分类层级 | 参考节点种类；按来源业务/应用功能或sector/function/service分层，不跨体系混用；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_path` | 完整路径，同名不能丢上级 | 来源参考节点完整上级路径；同名节点不得丢父级而合并；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `reference_description` | 原目录含义，保持参考身份 | 政府参考目录节点含义；参考分类不等于本地组织职责；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_version` | 本地正文sha256，不冒称官方版本审定 | 本地参考正文版本或sha256；文件摘要不表示官方版本已审定；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `local_object_ids` | 本地职责稳定ID，可多对多复用 | 本地对象稳定ID集合；允许多对多，不能由参考分类自动创造本地对象；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `mapping_type` | 项目覆盖/排除/未知，不把分类当本地组织 | 政府参考裁剪映射类型；覆盖、排除与未知分开，排除须写理由；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `reason` | 裁剪或映射依据 | 参考裁剪或映射的具体依据；写明适用性与排除边界，不因名称相似自动匹配；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `dependencies` | 项目依赖及待确认语义，非参考树 | 本地职责映射的项目依赖；参考目录父子层级不自动形成执行依赖；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `impact_scope` | 变更影响的本地范围 | 参考裁剪或映射变更影响的本地范围；跨组织影响不得隐去；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `source_locator` | 章节和源行 | 来源章节、表和具体行定位；不以笼统指南名称代替可回查出处；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `review_action` | 核查/补证行动 | 来源或本地映射的后续核查行动；记录待确认点与责任，不把待核实写成通过；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:government_reference_node` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `reference_level` | sector/function/service | 参考节点原始粒度；保留宏观、高层、组内子功能或目录层次，不自行压平；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_path` | 来源完整路径 | 来源参考节点完整上级路径；同名节点不得丢父级而合并；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `definition` | 参考定义 | 参考节点的完整业务定义；保留排除边界，不由标签扩展原文含义；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `local_mapping` | 本地候选职责映射 | 参考节点到本地职责的候选映射；未评审保持候选，不当作组织事实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数字业务参考模型裁剪

- `id`：`digital-business-reference-tailoring`
- 英文名：Digital Business Reference Model Tailoring
- 决策问题：哪些数字业务功能适用于目标企业？
- 主责技能：`togaf-business-models-processes`
- 来源：G21H §2–6；G21H §1.2、§1.4、§3；G21H 表5-1；G21H 表6-1；G21H 表6-2；G21H 表6-3；G21H §4.2.2、§4.5.2–4.5.3 表4-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, reference_domain, function, local_mapping
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：34；对象类型：dbrm_domain, dbrm_element, digital_business_function, guide:dbrm_applicability, guide:dbrm_mapping_row, guide:competency_overlay
- 关系类型：contains, traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 明确企业目的与参考域
2. 映射现有目标能力
3. 记录缺口与不适用
4. 连接战略分段能力全景

### `dbrm_domain` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `dbrm_element` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `local_mapping` | 参考概念与本地概念的映射 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:dbrm_applicability` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dbrm_domain_id` | DBRM参考域ID | DBRM参考域稳定ID；同名域仍按来源ID区分；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `dbrm_domain` | 数字/战略/结构/运营，与TOGAF四域独立 | DBRM域名称；数字、战略、结构、运营独立于TOGAF四架构域；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `element_id` | 参考要素ID | DBRM参考要素稳定ID；与域ID一起定位，不能按名称合并异义要素；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `element` | 原要素名称 | DBRM原要素名称；保留参考身份，不直接当本地已部署组件；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `reference_identity` | 参考身份 | 参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `local_mapping` | 参考概念与本地概念的映射 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `local_evidence` | 原料观察ID | 本地业务材料或观察的稳定引用；参考表行不能证明本地实施存在；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `gap` | 基线目标之间的差距引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `tailoring_reason` | 裁剪理由 | 本地参考裁剪选择理由；结合实际材料说明保留或排除，不抹去参考身份；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `relationship_boundary` | 不可从图线猜关系 | DBRM关系使用边界；不能从图线、相邻或颜色推断未核实关系；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:dbrm_mapping_row` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `source_table` | 来源表ID，各轴独立 | 来源表ID；不同表轴各自独立，不因同名标签合并表结构；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `source_row_id` | 源表稳定行ID，项目补充行单列 | 来源表稳定行ID；项目补充行必须另标身份，不能套用官方行号；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `raw_cells` | 源空格/破折号原样保留 | 来源表原始单元格；空白和破折号按原样保留，解释填入resolved_cells；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention`） |
| `resolved_cells` | 组内延续解释；不能变造源标签 | 来源表延续单元格解释；保留原始单元格并注明继承依据，不变造源标签；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention`） |
| `source_mapping_status` | local-body-mapping/not-specified/project-only | 来源表映射核实状态；local-body-mapping/not-specified/project-only，与本地映射结论独立；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `local_object_ids` | 本地资料稳定ID | 本地对象稳定ID集合；允许多对多，不能由参考分类自动创造本地对象；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `local_mapping_status` | 项目候选映射/未评估，不是源结论 | 本地映射状态；候选、未评估、已核实须区分，与源表转录核实独立；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `local_evidence` | 本地观察依据或unknown | 本地业务材料或观察的稳定引用；参考表行不能证明本地实施存在；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `tailoring_reason` | 本地选择理由 | 本地参考裁剪选择理由；结合实际材料说明保留或排除，不抹去参考身份；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `review_action` | 下一步核实 | 来源或本地映射的后续核查行动；记录待确认点与责任，不把待核实写成通过；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `reference_identity` | 参考/项目身份边界 | 参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:competency_overlay` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `source_row_id` | 完整12源行引用 | 来源表稳定行ID；项目补充行必须另标身份，不能套用官方行号；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `pillar` | 数字使能五支柱 | 数字使能五支柱之一的来源标签；保留源表归属，不按名称推断本地职责；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `competency` | 源胜任力名称，运营/运营管理变体单列来源 | 来源胜任力名称；运营与运营管理变体保留原行来源，不擅自合并；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `dpbok_context` | I–IV组织规模语境 | DPBoK I–IV语境标识；不是成熟度分数，不以规模断言能力已具备；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `context_kind` | 不是成熟度/得分 | 胜任力语境的分类依据；说明为组织规模语境而不是评分或成熟度级别；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `local_roles` | 多责任角色稳定ID | 胜任力对应的本地责任角色ID集合；来源胜任力不是岗位已配齐证据；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `current_evidence` | 已具备能力的观察依据 | 现有胜任力的实际观察；培训计划不能当已具备能力的证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `needed_competency` | 项目需要的工作能力 | 本地工作需要的胜任力；与已有证据区分，避免把培训需求写成能力事实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `gap` | 基线目标之间的差距引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `action` | 改进行动与责任 | 补证或改进行动；记录责任方、触发或期限及未关闭事项；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `next_review` | 复评触发或时间 | 胜任力复评日期或触发事件；未安排须标缺口，不默认持续有效；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `reference_identity` | 参考表身份 | 参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（5）：`name`、`reference_domain`、`function`、`scope`、`decision`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 四框业务模型

- `id`：`four-box-business-model`
- 英文名：Four-Box Business Model
- 决策问题：评价客户价值主张能否由利润公式、资源和流程支持
- 主责技能：`togaf-business-models-processes`
- 来源：G18A/fig2-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, component, detail, assumptions
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：4；对象类型：business_model_component
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 明确客户任务与价值主张
2. 定义收入成本利润的候选公式
3. 识别关键资源与流程
4. 检验四框的一致性与约束
5. 记录方案假设和验证方法

### `business_model_component` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `component` | 在本工作产品范围中明确定义的 component 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `detail` | 在本工作产品范围中明确定义的 detail 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `assumptions` | 待验证假设 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 业务模型立方体

- `id`：`business-model-cube`
- 英文名：Business Model Cube
- 决策问题：检查价值主张、客户、伙伴、活动、胜任力和价值公式及其关系是否一致
- 主责技能：`togaf-business-models-processes`
- 来源：G18A/fig2-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, dimension, detail, local_mapping
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：4；对象类型：business_model_dimension
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 分别界定六个并列维度
2. 采集本地内容并注明来源
3. 只声明有依据的维度间关系
4. 分析价值创造与获取约束
5. 标记关系缺口

### `business_model_dimension` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dimension` | 评价维度 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `detail` | 在本工作产品范围中明确定义的 detail 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `local_mapping` | 参考概念与本地概念的映射 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 运营模式

- `id`：`operating-model`
- 英文名：Operating Model
- 决策问题：决定业务流程跨单元集成与标准化的合理程度
- 主责技能：`togaf-business-models-processes`
- 来源：G184/fig4-1；G21H §4.4.2、§5.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, integration, standardization, scope
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：16；对象类型：operating_model, guide:operating_submodel
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 界定业务单元和流程范围
2. 分别评估业务流程集成和标准化
3. 按高低组合定位
4. 检验数据共享和治理要求
5. 允许企业内不同范围并存不同模式

### `operating_model` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `integration` | 与其他系统的集成约定 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `standardization` | 在本工作产品范围中明确定义的 standardization 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rationale` | 分析或选择的理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `quadrant` | 在本工作产品范围中明确定义的 quadrant 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:operating_submodel` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `submodel` | posture/service/organization/resource四类 | 运营子模型类型；posture/service/organization/resource四类之一，不是组织上下级；类型约束：`{"type":"string","enum":["posture","service","organization","resource"]}`（来源：`project-operational-convention`） |
| `customer_segment` | 目标客户细分 | 子运营模型服务的客户细分；给出业务身份与排除边界；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `decision` | 本子模型业务选择 | 待作或已作的业务决定；写问题、选项与结果边界，建议不自动成为批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `implication` | 对相关模型的影响 | 本子运营模型选择对关联模型的影响；逐依赖说明，不能按表邻接推断；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `linked_submodels` | 显式互相约束的子模型ID，不表示层级 | 显式相互约束的运营子模型ID集合；不代表组织层级或自动生成关系；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `measures` | 成本/前置时间/质量/灵活性/敏捷性独立证据 | 运营子模型成本、前置时间、质量、灵活性、敏捷性度量；各有独立依据，不合成无来源总分；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `capacity` | 带单位/时间/依据的本地资源计算 | 范围内资源容量；数值须单位、时段、需求口径及来源，不推算未给资源；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `action` | 缺口行动 | 补证或改进行动；记录责任方、触发或期限及未关闭事项；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 原料引用 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `reference_identity` | 四子模型参考身份 | 参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

---

合计 7 个工作产品，95 个字段。
