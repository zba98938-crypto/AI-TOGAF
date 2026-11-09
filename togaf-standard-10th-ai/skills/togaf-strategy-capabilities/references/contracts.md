# togaf-strategy-capabilities 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 能力实例组成模型

- `id`：`capability-instance-model`
- 英文名：Capability Instance Model
- 决策问题：某阶段由什么具体组成实现能力？
- 主责技能：`togaf-strategy-capabilities`
- 来源：G233 §6.4；图6-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, capability_type, stage, role
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：9；对象类型：application, capability, capability_instance, information, process, role, value_stage
- 关系类型：instance_comprises, instance_of, precedes, stage_uses_instance, traces_to
- 关联交付物：`capability-assessment`, `architecture-roadmaps`

### 分析步骤

1. 从价值阶段识别能力使用语境
2. 引用能力类型
3. 描述实例的人员流程应用和对象
4. 校核跨实例信息流

### `capability` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `capability_instance` 必填字段（2）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `stage_id` | 在本工作产品范围中明确定义的 stage_id 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（7）：`name`、`capability_type`、`stage`、`role`、`process`、`application`、`information`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 平衡计分卡目标与成果

- `id`：`balanced-scorecard`
- 英文名：Balanced Scorecard Goals and Outcomes
- 决策问题：从四个视角识别可追溯目标与可度量成果以驱动能力改进
- 主责技能：`togaf-strategy-capabilities`
- 来源：G233/fig4-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, perspective, definition, metric
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：8；对象类型：goal, outcome
- 关系类型：realizes, traces_to
- 关联交付物：`capability-assessment`, `architecture-roadmaps`, `business-goals-objectives`

### 分析步骤

1. 分别提出客户学习成长内部流程财务目标
2. 定义成果度量基线目标单位与期间
3. 用成果实现目标关系连接
4. 继续追溯能力实例
5. 检验指标可验证性

### `goal` 必填字段（2）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `perspective` | 在本工作产品范围中明确定义的 perspective 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `outcome` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `perspective` | 在本工作产品范围中明确定义的 perspective 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `metric` | 度量方法和计算定义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `unit` | 度量单位 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `baseline` | 比较基线及状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `target` | 期望结果或目标值 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `period` | 分析期间 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## SMART目的评估

- `id`：`smart-objective-assessment`
- 英文名：SMART Objective Assessment
- 决策问题：每个目的是否具体、可度量、可行动、现实、有时限，并追溯到已分类的目标？
- 主责技能：`togaf-strategy-capabilities`
- 来源：G176 §9.1–9.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "statement", "meaning": "陈述", "origin": "source-purpose-plus-project-contract"}, {"id": "category", "meaning": "G176 §9.3目标类别ID", "origin": "source-purpose-plus-project-contract"}, {"id": "business_goal_ref", "meaning": "对应的组织业务目标", "origin": "source-purpose-plus-project-contract"}, {"id": "goal_id", "meaning": "所属目标ID", "origin": "source-purpose-plus-project-contract"}, {"id": "scope", "meaning": "该对象负责或适用的范围", "origin": "source-purpose-plus-project-contract"}, {"id": "measure", "meaning": "度量", "origin": "source-purpose-plus-project-contract"}, {"id": "unit", "meaning": "单位", "origin": "source-purpose-plus-project-contract"}, {"id": "target", "meaning": "目标值", "origin": "source-purpose-plus-project-contract"}, {"id": "organization_category", "meaning": "组织自定类别", "origin": "source-purpose-plus-project-contract"}, {"id": "baseline", "meaning": "基线值", "origin": "source-purpose-plus-project-contract"}, {"id": "owner", "meaning": "负责人", "origin": "source-purpose-plus-project-contract"}, {"id": "action", "meaning": "实现行动", "origin": "source-purpose-plus-project-contract"}, {"id": "realism_rationale", "meaning": "现实性理由", "origin": "source-purpose-plus-project-contract"}, {"id": "realism_evidence", "meaning": "支持现实性的证据ID", "origin": "source-purpose-plus-project-contract"}, {"id": "due", "meaning": "截止日期（ISO）", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：16；对象类型：guide:goal, guide:smart-objective
- 关系类型：未声明
- 关联交付物：`business-goals-objectives`

### 分析步骤

1. 把目标归入G176 §9.3的13类之一或组织自定类别
2. 把每个目的追溯到目标
3. 逐项核对具体、可度量、可行动、现实、有时限
4. 可度量项记录基线、目标与单位
5. 现实性给出理由与证据
6. 缺项列为待补，不由模板补数值

### `guide:goal` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `statement` | 陈述 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `category` | G176 §9.3目标类别ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `business_goal_ref` | 对应的组织业务目标 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

### `guide:smart-objective` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `goal_id` | 所属目标ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `statement` | 陈述 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `scope` | 该对象负责或适用的范围 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `measure` | 度量 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `unit` | 单位 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `target` | 目标值 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（8）：`name`、`organization_category`、`baseline`、`owner`、`action`、`realism_rationale`、`realism_evidence`、`due`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 3 个工作产品，33 个字段。
