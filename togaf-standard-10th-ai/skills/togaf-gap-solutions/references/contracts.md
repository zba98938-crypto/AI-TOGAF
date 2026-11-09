# togaf-gap-solutions 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 备选方案决策矩阵

- `id`：`options-decision-matrix`
- 英文名：Options Decision Matrix
- 决策问题：哪项候选方案更适合业务问题？
- 主责技能：`togaf-gap-solutions`
- 来源：G176 §12.8；G20F §4.6；G20F §4.7.1 表4-1；G210 §3.3–3.3.8
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, option, criterion, score
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：criterion, option, option_score, guide:delivery_feature_review, guide:delivery_style_decision, guide:sbce_iteration, guide:sbce_constraint, guide:agile_pattern_choice
- 关系类型：evaluated_by, traces_to
- 关联交付物：`architecture-roadmaps`, `solution-building-blocks`

### 分析步骤

1. 归一化候选方案
2. 比较成本资源贡献和可行性
3. 声明一至五分的优劣方向
4. 必要时加权并检查敏感性

### `guide:delivery_feature_review` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `feature_id` | 来源交付特征的稳定ID | 来源交付特征的稳定ID；逐原表特征评估，不按名称匹配新增评分项；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `source_guidance` | 交付特征的原指南提示与定位 | 交付特征的原指南提示与定位；一般画像不当作项目强制选择或评分阈值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `applies` | 交付特征的适用判断 | 交付特征的适用判断；仅yes/no/unknown，观察不充分选unknown；类型约束：`{"type":"string","enum":["yes","no","unknown"]}`（来源：`project-operational-convention`） |
| `observation` | 范围内实际观察或明确未取得材料 | 范围内实际观察或明确未取得材料；事实、推论和行动不得混写；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_refs` | 本项判断使用的来源ID集合 | 本项判断使用的来源ID集合；至少一项，引用存在性不证明内容正确；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |

### `guide:delivery_style_decision` 必填字段（7）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `scope_id` | 交付风格决策范围稳定ID | 交付风格决策范围稳定ID；不同范围可选不同或嵌套风格，不能一次定全企业；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `styles` | 交付风格集合 | 交付风格集合；仅rapid/agile/robust，可按范围嵌套，不以匹配项最多自动选择；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"enum":["rapid","agile","robust"]}}`（来源：`project-operational-convention`） |
| `owner` | 本记录、行动或计划的责任方 | 本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `rationale` | 本次选择的理由与依据 | 本次选择的理由与依据；解释与备选的区别，不循环引用选择结果作证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_refs` | 本项判断使用的来源ID集合 | 本项判断使用的来源ID集合；至少一项，引用存在性不证明内容正确；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `conflicting_features` | 冲突交付特征的来源ID集合 | 冲突交付特征的来源ID集合；只能引用已评估特征，不能按多数票消除冲突；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `tailoring` | 冲突交付特征的项目裁剪说明 | 冲突交付特征的项目裁剪说明；说明范围与取舍，不把风格画像当强制阈值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:sbce_iteration` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `option_id` | 候选方案稳定ID | 候选方案稳定ID；跨轮次保持身份，同ID不允许更换子系统；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `subsystem` | SBCE方案所属子系统稳定名称或ID | SBCE方案所属子系统稳定名称或ID；同option_id跨轮次保持相同子系统；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `goal` | 本轮SBCE共同业务目标 | 本轮SBCE共同业务目标；方案比较必须使用同一目标和约束范围；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `iteration` | SBCE评审轮次 | SBCE评审轮次；正整数，同一option_id每轮唯一，按轮次保留历史；类型约束：`{"type":"integer","minimum":1}`（来源：`project-operational-convention`） |
| `hypothesis` | 本轮候选方案的可检验假设 | 本轮候选方案的可检验假设；说明期待结果和检验边界，不以结论替代假设；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `assessment` | 本轮方案假设的检验结果 | 本轮方案假设的检验结果；区分观察、推论和未验证内容；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_refs` | 本项判断使用的来源ID集合 | 本项判断使用的来源ID集合；至少一项，引用存在性不证明内容正确；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `decision_owner` | 本轮SBCE保留、淘汰或重开决定的责任人 | 本轮SBCE保留、淘汰或重开决定的责任人；不推定拥有正式批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `status` | 本轮方案处置 | 本轮方案处置；retain/eliminate/selected/reopen，淘汰和重开须原因及新增证据，selected不是正式批准；类型约束：`{"enum":["retain","eliminate","selected","reopen"]}`（来源：`project-operational-convention`） |
| `decision_reason` | 淘汰或重开的明确原因 | 淘汰或重开的明确原因；须关联本轮新增证据，不允许无理由恢复被淘汰方案；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `new_evidence_refs` | 本轮淘汰或重开使用的新增证据ID | 本轮淘汰或重开使用的新增证据ID；不能只重用旧结论而无新证据；类型约束：`{"type":"array","minItems":0,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |

### `guide:sbce_constraint` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `source_option_id` | SBCE兼容约束源方案ID | SBCE兼容约束源方案ID；必须是迭代历史中的方案，不由图表顺序推断；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `target_option_id` | SBCE兼容约束目标方案ID | SBCE兼容约束目标方案ID；必须存在于迭代历史，源/目标用于明确耦合而非时间顺序；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `rule` | 两方案间显式兼容约束 | 两方案间显式兼容约束；写清耦合、方向和判定条件，非优先级或加权分，不得忽略未验证耦合；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `status` | 跨子系统方案兼容验证 | 跨子系统方案兼容验证；satisfied/violated/unknown，所选集合存在violated或unknown不能称兼容；类型约束：`{"enum":["satisfied","violated","unknown"]}`（来源：`project-operational-convention`） |
| `evidence_refs` | 本项判断使用的来源ID集合 | 本项判断使用的来源ID集合；至少一项，引用存在性不证明内容正确；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |

### `option` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `option_id` | 候选方案稳定ID | 候选方案稳定ID；跨轮次保持身份，同ID不允许更换子系统；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `criteria_scores` | 选项逐准则评分 | 选项逐准则评分；每项须量表与依据，不适用于SBCE或交付风格定性判断；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention`） |
| `rationale` | 本次选择的理由与依据 | 本次选择的理由与依据；解释与备选的区别，不循环引用选择结果作证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `tradeoff` | 候选方案的取舍 | 候选方案的取舍；逐项列牺牲、收益及受影响方，不把最高分当自动批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（7）：`name`、`option`、`criterion`、`score`、`weight`、`evidence`、`feasibility`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 能力增量分析

- `id`：`capability-increment-analysis`
- 英文名：Capability Increment Analysis
- 决策问题：能力实例需要优化整合新建还是退役？
- 主责技能：`togaf-gap-solutions`
- 来源：G233 §7.1–7.2；图7-1、7-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, instance, change_kind, baseline
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：9；对象类型：application, capability, capability_change, capability_instance, information, process, role, value_stage
- 关系类型：instance_comprises, instance_of, precedes, stage_uses_instance, traces_to
- 关联交付物：`architecture-roadmaps`, `solution-building-blocks`

### 分析步骤

1. 对齐实例基线目标
2. 分类具体变化及理由
3. 聚合应用和业务差距
4. 形成可交付增量

### `capability` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `capability_instance` 必填字段（2）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `stage_id` | 在本工作产品范围中明确定义的 stage_id 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（7）：`name`、`instance`、`change_kind`、`baseline`、`target`、`rationale`、`gap`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 构建块描述

- `id`：`building-block-description`
- 英文名：Building Block Description
- 决策问题：构建块定义和选择怎样追溯到需求与实现？
- 主责技能：`togaf-gap-solutions`
- 来源：G248 §2–3；G21H §2产品架构定义、§5.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, definition, abstraction, service
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：20；对象类型：abb, goal, guide:product_function, guide:product_component, guide:product_interface, sbb, requirement
- 关系类型：traces_to, guide:allocates_function, guide:interface_sender, guide:interface_receiver, realizes
- 关联交付物：`architecture-roadmaps`, `solution-building-blocks`, `architecture-building-blocks`

### 分析步骤

1. 描述所需架构服务与边界
2. 区分ABB和SBB
3. 比较候选实现
4. 记录要求、接口与选择依据

### `abb` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `abstraction` | 语境、概念、逻辑或物理层次 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `service` | 服务对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `requirements` | 架构要求引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `realization` | 构建块的实现关系与候选 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:product_function` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `product` | 产品稳定ID | 产品稳定标识；功能、组件和接口均按同一产品身份追溯，不用版本号代替身份；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `requirement` | 功能需求及结果 | 产品功能需求与期待结果；保持可验证边界，不能混同已实现功能；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `operating_capability` | 产品对运营能力的要求 | 产品对运营能力的要求；说明功能如何支持结果，不能直接推定组织能力已具备；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `version` | 独立版本，非批准 | 产品功能、组件或接口独立版本；版本更新不自动授予批准或部署状态；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 原业务材料 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:product_component` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `product` | 产品稳定ID | 产品稳定标识；功能、组件和接口均按同一产品身份追溯，不用版本号代替身份；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `component_role` | 组件职责 | 组件在产品结构中的职责；不把部署位置或组织职责当作组件身份；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `technical_component` | 技术组件/环境与未知边界 | 产品技术组件或运行环境；版本与未知边界须保留，不把候选技术当已部署事实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `version` | 独立版本，非批准 | 产品功能、组件或接口独立版本；版本更新不自动授予批准或部署状态；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 原业务材料 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:product_interface` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `product` | 产品稳定ID | 产品稳定标识；功能、组件和接口均按同一产品身份追溯，不用版本号代替身份；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `sender_ref` | 发送组件ID | 接口发送组件稳定ID；与receiver_ref共同定义请求方向，响应不改变请求方身份；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `receiver_ref` | 接收组件ID | 接口接收组件稳定ID；与sender_ref共同定义请求方向，不由图形位置推出；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `operation` | 接口操作 | 接口操作的业务含义；说明调用方向、前置条件与结果，不能仅写传输协议；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `request` | 请求数据语义 | 接口请求数据与业务语义；列必要字段、约束和失败前置条件，不以报文名代替契约；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `response` | 结果与异常语义 | 接口返回结果与异常语义；区分成功、失败和补偿，不默认所有调用成功；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `security` | 授权安全约束 | 产品接口认证、授权与安全约束；列调用方权限及拒绝处理，不以采用微服务等同安全；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `version` | 独立版本，非批准 | 产品功能、组件或接口独立版本；版本更新不自动授予批准或部署状态；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 原业务材料 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 过渡架构模型

- `id`：`transition-architecture-model`
- 英文名：Transition Architecture Model
- 决策问题：变革中间状态是否可运营且衔接目标？
- 主责技能：`togaf-gap-solutions`
- 来源：G248 §2；图2-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, state_id, operating_conditions, work_packages
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：8；对象类型：transition, transition_architecture, work_package
- 关系类型：implements_transition, traces_to, depends_on
- 关联交付物：`architecture-roadmaps`, `solution-building-blocks`

### 分析步骤

1. 命名基线过渡目标
2. 描述每个状态的运营条件
3. 关联工作包及实现
4. 检查依赖控制数据一致性和回退

### `transition` 必填字段（2）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `operating_conditions` | 可运营状态的明确条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（6）：`name`、`state_id`、`work_packages`、`dependencies`、`controls`、`rollback`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

---

合计 4 个工作产品，44 个字段。
