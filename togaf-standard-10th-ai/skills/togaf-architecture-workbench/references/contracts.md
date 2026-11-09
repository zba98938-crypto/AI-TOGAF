# togaf-architecture-workbench 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 架构项目工作分解

- `id`：`architecture-project-wbs`
- 英文名：Architecture Project WBS
- 决策问题：怎样把架构成果分解为可管理工作？
- 主责技能：`togaf-architecture-workbench`
- 来源：G188 §3.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, deliverable, work_package, owner
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：architecture_task
- 关系类型：project:wbs_decomposes
- 关联交付物：`statement-of-work`

### 分析步骤

1. 明确范围与排除项
2. 按成果分解工作
3. 核对遗漏和重复
4. 指定责任估算与验收

### `architecture_task` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `deliverable` | 架构交付物引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `work_package` | 工作包引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `effort` | 投入估算及单位 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `dependency` | 依赖对象及方向 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `acceptance` | 验收准则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 架构项目资源与进度

- `id`：`architecture-project-schedule`
- 英文名：Architecture Project Resource and Schedule
- 决策问题：架构工作在资源约束下怎样安排？
- 主责技能：`togaf-architecture-workbench`
- 来源：G188 §3.2.6–3.2.7；G210 §3.3–3.3.8
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, duration, resource, predecessor
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：architecture_activity, guide:agile_sprint, guide:agile_activity, guide:dorp_gate, guide:agile_context
- 关系类型：traces_to, guide:agile_handoff, guide:agile_continues, guide:agile_collaborates, guide:agile_finalizes
- 关联交付物：`statement-of-work`

### 分析步骤

1. 确定活动依赖与估算依据
2. 比较资源可用量
3. 形成里程碑和滚动计划
4. 分析关键路径与缓冲

### `architecture_activity` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `duration` | 活动持续时间及单位 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `resource` | 所需资源 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `predecessor` | 前置活动 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `start` | 计划或实际开始时间 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `end` | 计划或实际结束时间 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `milestone` | 里程碑定义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `milestone` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `due_date` | 里程碑计划到期日 | 里程碑计划到期日；使用ISO 8601日历日期，变更须保持依赖与退出条件一致；类型约束：`{"type":"string","minLength":1,"pattern":"\\S","format":"date"}`（来源：`project-operational-convention`） |
| `exit_criteria` | 里程碑退出条件 | 里程碑退出条件；列可核实结果、验收责任与证据，日期到达不等于满足；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `owner` | 本记录、行动或计划的责任方 | 本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `dependency` | 里程碑前置依赖ID | 里程碑前置依赖ID；列清外部依赖与未满足条件，不能把时间相邻当依赖；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 架构项目管理策略

- `id`：`project-management-strategy`
- 英文名：Architecture Project Management Strategy
- 决策问题：架构项目如何管理风险、质量、沟通、配置与控制，谁确认方法和授权边界？
- 主责技能：`togaf-architecture-workbench`
- 来源：G188 §3.1.8 L541–631；G188 §4.2.1 L1524–1531
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "project_scope", "meaning": "作为项目管理的工作范围与排除项", "origin": "source-purpose-plus-project-contract"}, {"id": "selected_method", "meaning": "组织采用的项目管理方法", "origin": "source-purpose-plus-project-contract"}, {"id": "method_tailoring", "meaning": "阶段和方法裁剪理由", "origin": "source-purpose-plus-project-contract"}, {"id": "project_governance", "meaning": "时间预算质量监督职能与责任方", "origin": "source-purpose-plus-project-contract"}, {"id": "architecture_governance", "meaning": "架构一致性治理职能与责任方", "origin": "source-purpose-plus-project-contract"}, {"id": "confirmation_state", "meaning": "管理方法确认状态及所缺依据", "origin": "source-purpose-plus-project-contract"}, {"id": "topics", "meaning": "风险、质量、利益相关者沟通、控制、配置五主题的实际操作规范和责任", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：不足时保留带ID草案与needs-input；未知容差不设默认值，缺实际阅读/验收证据不声称已阅读/完成。冲突、重复ID和未经批准覆盖基线属于错误。
- 字段总数：10；对象类型：guide:project-management-strategy
- 关系类型：未声明
- 关联交付物：`statement-of-work`, `tailored-architecture-framework`

### 分析步骤

1. 识别项目范围和组织既有项目管理框架
2. 分开项目治理与架构治理角色，即使由同一机构承担也分别说明
3. 提炼风险、质量、沟通和控制方法并链接对应登记册
4. 按组织方法明确配置基线与批准后变更规则
5. 记录有来源的频率、容差、上报和授权监控，不套用示例数值
6. 交治理责任方确认，变更后复核受影响控制

### `guide:project-management-strategy` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `project_scope` | 作为项目管理的工作范围与排除项 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `selected_method` | 组织采用的项目管理方法 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `method_tailoring` | 阶段和方法裁剪理由 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `project_governance` | 时间预算质量监督职能与责任方 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `architecture_governance` | 架构一致性治理职能与责任方 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `confirmation_state` | 管理方法确认状态及所缺依据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `topics` | 风险、质量、利益相关者沟通、控制、配置五主题的实际操作规范和责任 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `analysis_result` | 确定性审查结果与带ID缺口 | 确定性审查结果与带ID缺口；由本方法明确输入重算，输出存在不等于治理批准；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention`） |
| `raw_material_refs` | 完整原始业务材料ID列表 | 完整原始业务材料ID列表；须能检索随包原料，不以分析结果循环充当业务事实；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

## 架构项目状态要点报告

- `id`：`project-status-highlight-report`
- 英文名：Architecture Project Highlight Report
- 决策问题：本报告期实际完成了什么、下期做什么、余项如何预测，哪些事项需要决策或上报？
- 主责技能：`togaf-architecture-workbench`
- 来源：G188 §3.4.2–3.4.8 L1112–1205
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "period", "meaning": "本报告期起止日期", "origin": "source-purpose-plus-project-contract"}, {"id": "next_period", "meaning": "下一报告期起止日期", "origin": "source-purpose-plus-project-contract"}, {"id": "audience", "meaning": "受众与所需细节", "origin": "source-purpose-plus-project-contract"}, {"id": "communication_plan_ref", "meaning": "沟通计划引用", "origin": "source-purpose-plus-project-contract"}, {"id": "approved_plan_ref", "meaning": "批准范围/进度基线引用", "origin": "source-purpose-plus-project-contract"}, {"id": "previous_planned_task_ids", "meaning": "上期计划的稳定任务ID", "origin": "source-purpose-plus-project-contract"}, {"id": "tasks", "meaning": "任务的实际/预测、责任、计划日期和验收证据", "origin": "source-purpose-plus-project-contract"}, {"id": "next_period_activities", "meaning": "下一期关键活动与责任", "origin": "source-purpose-plus-project-contract"}, {"id": "risks_issues", "meaning": "关键风险/问题及需关注/上报事项", "origin": "source-purpose-plus-project-contract"}, {"id": "corrective_actions", "meaning": "纠正措施与责任、期限", "origin": "source-purpose-plus-project-contract"}, {"id": "remaining_stage_forecast", "meaning": "阶段剩余部分预测与不确定性", "origin": "source-purpose-plus-project-contract"}, {"id": "remaining_project_forecast", "meaning": "项目剩余部分预测与不确定性", "origin": "source-purpose-plus-project-contract"}, {"id": "decisions_required", "meaning": "需利益相关者作出的决策及权限", "origin": "source-purpose-plus-project-contract"}, {"id": "changes", "meaning": "批准、未批准与拒绝变更状态及基线处理", "origin": "source-purpose-plus-project-contract"}, {"id": "schedule_tolerance", "meaning": "具有单位、比较符、依据与授权者的项目规则", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：不足时保留带ID草案与needs-input；未知容差不设默认值，缺实际阅读/验收证据不声称已阅读/完成。冲突、重复ID和未经批准覆盖基线属于错误。
- 字段总数：18；对象类型：guide:project-highlight-report
- 关系类型：未声明
- 关联交付物：`statement-of-work`, `communications-plan`

### 分析步骤

1. 锁定报告期、受众、沟通计划及批准基线版本
2. 读取检查点、当前阶段计划、质量/风险/问题日志和收益评审计划
3. 沿用上期计划任务的同一ID核对实际、未完、取消和验收证据
4. 列下一期关键活动、风险问题、纠正措施和阶段/项目余项预测
5. 分别登记已批准和未批准变更，保持批准基线不被草案覆盖
6. 仅按显式委托容差识别例外，形成需决策/上报事项供治理审查

### `guide:project-highlight-report` 必填字段（17）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `period` | 本报告期起止日期 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `next_period` | 下一报告期起止日期 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `audience` | 受众与所需细节 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `communication_plan_ref` | 沟通计划引用 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `approved_plan_ref` | 批准范围/进度基线引用 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `previous_planned_task_ids` | 上期计划的稳定任务ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `tasks` | 任务的实际/预测、责任、计划日期和验收证据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `next_period_activities` | 下一期关键活动与责任 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `risks_issues` | 关键风险/问题及需关注/上报事项 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `corrective_actions` | 纠正措施与责任、期限 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `remaining_stage_forecast` | 阶段剩余部分预测与不确定性 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `remaining_project_forecast` | 项目剩余部分预测与不确定性 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `decisions_required` | 需利益相关者作出的决策及权限 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `changes` | 批准、未批准与拒绝变更状态及基线处理 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `schedule_tolerance` | 具有单位、比较符、依据与授权者的项目规则 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `analysis_result` | 确定性审查结果与带ID缺口 | 确定性审查结果与带ID缺口；由本方法明确输入重算，输出存在不等于治理批准；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention`） |
| `raw_material_refs` | 完整原始业务材料ID列表 | 完整原始业务材料ID列表；须能检索随包原料，不以分析结果循环充当业务事实；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

## 领域架构融入整体EA核对

- `id`：`domain-architecture-alignment`
- 英文名：Domain Architecture Alignment Check
- 决策问题：各领域架构是否服务同一EA项目与目标、引用共享模型，安全是否作为关注点贯穿其他域？
- 主责技能：`togaf-architecture-workbench`
- 来源：G186 §12.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "kind", "meaning": "领域类别", "origin": "source-purpose-plus-project-contract"}, {"id": "project_id", "meaning": "所属EA项目ID", "origin": "source-purpose-plus-project-contract"}, {"id": "objective_ids", "meaning": "服务的EA项目目标ID", "origin": "source-purpose-plus-project-contract"}, {"id": "model_id", "meaning": "共享架构模型ID", "origin": "source-purpose-plus-project-contract"}, {"id": "shared_entity_ids", "meaning": "引用的共享模型对象ID", "origin": "source-purpose-plus-project-contract"}, {"id": "treated_as", "meaning": "安全的处理方式：concern或其他", "origin": "source-purpose-plus-project-contract"}, {"id": "referenced_domain_ids", "meaning": "安全关注点所引用的其他领域ID", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：8；对象类型：guide:domain-architecture, guide:ea-project-scope
- 关系类型：未声明
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 登记EA项目及其目标与共享模型
2. 登记每个领域架构所属项目、服务目标及共享对象
3. 标出按另一个项目工作或目的不在EA目标内的领域
4. 把安全作为关注点并引用其所涉其他领域
5. 修正后再进入跨域评审

### `guide:domain-architecture` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `kind` | 领域类别 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `project_id` | 所属EA项目ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `objective_ids` | 服务的EA项目目标ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

### `guide:ea-project-scope` 必填字段（2）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `objective_ids` | 服务的EA项目目标ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `model_id` | 共享架构模型ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（4）：`name`、`shared_entity_ids`、`treated_as`、`referenced_domain_ids`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 5 个工作产品，50 个字段。
