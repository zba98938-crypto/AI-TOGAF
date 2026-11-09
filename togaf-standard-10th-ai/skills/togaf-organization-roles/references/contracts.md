# togaf-organization-roles 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 架构技能／角色矩阵

- `id`：`architecture-skill-matrix`
- 英文名：Architecture Skill Role Matrix
- 决策问题：每种架构角色需要什么熟练度？
- 主责技能：`togaf-organization-roles`
- 来源：G249 §5 Tables 5-1 and 5-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, category, subskill, role
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：skill, architecture_role, guide:architecture-role
- 关系类型：supports_role
- 关联交付物：`organization-model`

### 分析步骤

1. 识别相关技能分类
2. 按角色确定目标等级
3. 评价人员证据
4. 形成培训与配置建议

### `skill` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `skill_id` | 带版本与类别的技能稳定ID；同名跨类别条目不得合并 | 带版本与类别的技能稳定ID；同名跨类别条目不得合并；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `category` | 所声明分类体系下的分类 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `subskill` | 具体技能子项 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `architecture_role` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 参考节点的完整业务定义；保留排除边界，不由标签扩展原文含义 | 参考节点的完整业务定义；保留排除边界，不由标签扩展原文含义；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:architecture-role` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `tier` | 在本工作产品范围中明确定义的 tier 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `primary_responsibility` | 在本工作产品范围中明确定义的 primary_responsibility 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 架构人员发展计划

- `id`：`architecture-development-plan`
- 英文名：Architecture Development Plan
- 决策问题：怎样弥补人员技能缺口？
- 主责技能：`togaf-organization-roles`
- 来源：G249 §5–6（发展计划字段与判据为项目约定）
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, person, role, current_proficiency
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：14；对象类型：skill_development
- 关系类型：traces_to
- 关联交付物：`organization-model`

### 分析步骤

1. 对齐目标角色与当前技能
2. 区分背景认知通晓专家
3. 选择实践培训或辅导
4. 安排效果验证

### `skill_development` 必填字段（14）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `person` | 人员或匿名人员标识 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `role` | 承担职责的角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `skill_id` | 带版本与类别的技能稳定ID；同名跨类别条目不得合并 | 带版本与类别的技能稳定ID；同名跨类别条目不得合并；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `scale_id` | 熟练度量表ID；G249-table5-1或显式项目量表，不与G198或Open CA认证直接换算 | 熟练度量表ID；G249-table5-1或显式项目量表，不与G198或Open CA认证直接换算；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `task_refs` | 本技能评价或发展行动对应的任务ID；角色名称不能替代任务范围 | 本技能评价或发展行动对应的任务ID；角色名称不能替代任务范围；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `requirement_refs` | 本次发展行动回应的角色任务要求ID；目标不得由当前人员表现倒推 | 本次发展行动回应的角色任务要求ID；目标不得由当前人员表现倒推；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `current_proficiency` | 当前熟练度及证据 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `target_proficiency` | 目标熟练度 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `behavioral_gap` | 尚未证明的具体行为及业务影响；不能只写目标减现状的数字 | 尚未证明的具体行为及业务影响；不能只写目标减现状的数字；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `action` | 补证或改进行动；记录责任方、触发或期限及未关闭事项 | 补证或改进行动；记录责任方、触发或期限及未关闭事项；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `success_criteria` | 学习或实践完成的可观察判据；培训出席不等于技能提升 | 学习或实践完成的可观察判据；培训出席不等于技能提升；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `reassessment` | 复评责任人、期限、行为判据与状态；完成须引用人员实测评价 | 复评责任人、期限、行为判据与状态；完成须引用人员实测评价；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `history` | 保留历史评级、时点与证据；新评价不能无痕覆盖旧事实或角色目标；首次评价可显式空数组 | 保留历史评级、时点与证据；新评价不能无痕覆盖旧事实或角色目标；首次评价可显式空数组；类型约束：`{"type":"array","items":{"type":"object","minProperties":1}}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 威胁事件支持证据的来源引用；不能以风险评估结论循环证明事件事实 | 威胁事件支持证据的来源引用；不能以风险评估结论循环证明事件事实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention-guided-by-cited-source`） |

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数字可持续教育与技能计划

- `id`：`sustainability-education-plan`
- 英文名：Sustainability Education Plan
- 决策问题：所有员工和关键专业角色怎样形成可应用的可持续ICT技能？
- 主责技能：`togaf-organization-roles`
- 来源：G242 §3.3.2、§4.3、§5.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：组织、服务、业务用途及所评估期间/生命周期边界, 原始访谈、使用数据、供应商记录及稳定证据ID, 适用目标、职责和组织自定决策规则；未知项显式登记
- 可选输入：历史评估、环境数据目录、采购契约及角色技能资料
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：12；对象类型：guide:sustainability_learning
- 关系类型：未声明
- 关联交付物：`organization-model`, `capability-assessment`

### 分析步骤

1. 列全员与重叠专业角色，查当前证据
2. 将普遍意识与角色技能分开
3. 为采购、核算、架构等设计实操任务
4. 安排资源、责任、时间与HR职位/招聘变更
5. 验证理解/实践效果；参加课程不自动提熟练度

### `guide:sustainability_learning` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `audience` | 全员或具体角色 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `population` | 覆盖人数及范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `current_evidence` | 现有知识/培训/实操证据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `skill_need` | 需补知识与技能 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `learning_activity` | 可执行活动 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `resources` | 已选资源及可用性 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `application_check` | 实际应用能力的验证方式 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `hr_change` | 职位/招聘要求变更 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `owner` | 责任人 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `status` | 覆盖与验证状态 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 原料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

用途—应用/数据—基础设施用稳定ID追踪；评估维度与功能多对多关联；总额与子集、两种Scope2基础、抵消和复制存储分别表达。表格相邻不代表因果或可相加。

## 架构角色定义目录

- `id`：`architecture-role-catalog`
- 英文名：Architecture Role Definition Catalog
- 决策问题：架构实践需要哪些职责，各角色如何提供上下文、治理、协作和交接，任务由谁在什么范围内承担？
- 主责技能：`togaf-organization-roles`
- 来源：G249 §4、§4.1–4.4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "tier", "meaning": "角色类别：chief/enterprise/segment/solution/specialist；不是通用人事职级总序", "origin": "source-purpose-plus-project-contract"}, {"id": "scope", "meaning": "该对象负责或适用的范围", "origin": "source-purpose-plus-project-contract"}, {"id": "primary_responsibility", "meaning": "首要职责", "origin": "source-purpose-plus-project-contract"}, {"id": "segment_scope", "meaning": "分段或域范围；企业级角色写不适用及原因", "origin": "source-purpose-plus-project-contract"}, {"id": "activities", "meaning": "主要活动清单", "origin": "source-purpose-plus-project-contract"}, {"id": "key_stakeholders", "meaning": "关键利益相关者类别", "origin": "source-purpose-plus-project-contract"}, {"id": "kpis", "meaning": "KPI记录：度量、目标、目标来源（project-adopted/source-illustrative）及证据", "origin": "source-purpose-plus-project-contract"}, {"id": "leads", "meaning": "旧版未分类领导关系；需补类型、范围和证据，保留为草稿缺口", "origin": "source-purpose-plus-project-contract"}, {"id": "relationships", "meaning": "有类型关系：architecture_guidance/architecture_constraint/specialization/collaborates_with/reports_to/handoff，含target、scope和evidence", "origin": "source-purpose-plus-project-contract"}, {"id": "assignments", "meaning": "人员、岗位、角色任务分配：person_ref、job_ref、task_refs、authority、valid_from、valid_until和evidence", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：11；对象类型：guide:architecture-role
- 关系类型：未声明
- 关联交付物：`organization-model`

### 分析步骤

1. 按G249 §4区分首席、企业、分段、解决方案架构师及专家
2. 为每个角色记录范围、首要职责、活动和关键利益相关者
3. 分别记录专业指导、架构约束、特化、协作、汇报与交接；旧leads产生待分类缺口
4. 记录KPI口径、期间、来源和责任，区分企业采用目标与来源示例
5. 按第3、6章记录角色裁剪；只有显式采用的项目策略才施加严格层级规则
6. 记录有权限和有效期的人员任务分配，再用architecture-role-skill-assessment连接任务、技能证据及发展

### `guide:architecture-role` 必填字段（7）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `tier` | 角色类别：chief/enterprise/segment/solution/specialist；不是通用人事职级总序 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `scope` | 该对象负责或适用的范围 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `primary_responsibility` | 首要职责 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `segment_scope` | 分段或域范围；企业级角色写不适用及原因 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `activities` | 主要活动清单 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `key_stakeholders` | 关键利益相关者类别 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `kpis` | KPI记录：度量、目标、目标来源（project-adopted/source-illustrative）及证据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（4）：`name`、`leads`、`relationships`、`assignments`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 4 个工作产品，44 个字段。
