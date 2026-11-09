# togaf-migration-roadmap 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 回退计划

- `id`：`rollback-plan`
- 英文名：Rollback Plan
- 决策问题：迁移失败时如何恢复可运营状态？
- 主责技能：`togaf-migration-roadmap`
- 来源：G152 §5.7
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, trigger, decision_owner, prerequisite
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：rollback_step
- 关系类型：traces_to
- 关联交付物：`implementation-migration-plan`

### 分析步骤

1. 确定回退触发与授权
2. 分析可逆点和数据一致性
3. 排列步骤与依赖
4. 定义恢复验证和演练证据

### `rollback_step` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `trigger` | 触发事件或判据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `decision_owner` | 有权作出该决策的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `prerequisite` | 可执行该项的前置条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `data_recovery` | 数据恢复与一致性规则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `sequence` | 执行次序及其依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `verification` | 验证方法与验收证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 实施因素目录

- `id`：`implementation-factor-catalog`
- 英文名：Implementation Factor Catalog
- 决策问题：哪些组织文化、转型能力和技能因素改变变革实施安排？
- 主责技能：`togaf-migration-roadmap`
- 来源：G186 §7.4.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：11；对象类型：guide:implementation_factor
- 关系类型：未声明
- 关联交付物：`implementation-migration-plan`, `capability-assessment`

### 分析步骤

1. 按业务单元与企业层收集转型属性
2. 区分观察事实、解释和未知
3. 将每个因素连接到具体实施工作或选择影响
4. 记录处理动作、责任、窗口与决策理由
5. 资源/文化变化后重新审视路线与风险

### `guide:implementation_factor` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `unit` | 业务单元/企业范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `change_attribute` | 文化、转型能力或技能等具体因素 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `observation` | 原始观察与当前情况 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `effect` | 对方案/工作包/时点的实际影响 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `required_action` | 补强动作及其进入条件 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `owner` | 动作责任 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `timing` | 可用窗口与业务约束 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `confidence` | 依据局限，不使用无依据分数 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision_record` | 为何采纳此处理及谁仍需确认 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

## 组合主题工作包分组

- `id`：`portfolio-theme-work-package-register`
- 英文名：Portfolio Theme Work Package Register
- 决策问题：如何把工作包按主题排序并识别依赖、投资和资源？
- 主责技能：`togaf-migration-roadmap`
- 来源：G186 §8.2表8-2、§8.3–8.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：12；对象类型：guide:portfolio_assignment
- 关系类型：未声明
- 关联交付物：`architecture-roadmaps`, `implementation-migration-plan`

### 分析步骤

1. 从战略目标、当前路线和在建项目建立主题
2. 按稳定工作包ID区分新/续作与保持/改进分类
3. 记录战略重要性和前置依赖
4. 收集同口径工作量/投资/影响时点并标未齐字段
5. 检查循环、跨主题复用和资源争用后形成候选顺序

### `guide:portfolio_assignment` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `theme` | 组合主题及目标来源 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `work_package_id` | TOGAF变革工作包稳定ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `change_kind` | 保持/改进/新差异化/新市场的项目分类 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `continuation` | 新工作或本财年续作 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `required_work_packages` | 前置工作包ID，方向本项依赖所列项 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `importance` | 继承战略重要性及依据，不发明权重 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `impact_start` | 影响预计开始时间而非全部任务完成期 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `effort` | 工作量/单位/估算依据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `investment` | 金额/币种/估算范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `allocation_note` | 多主题复用不重复计资，分组理由 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

## 组合估算充分性检查

- `id`：`portfolio-estimate-sufficiency-check`
- 英文名：Portfolio Estimate Sufficiency Check
- 决策问题：继续细化是否仍有足够收益，预算决策是否已有充分依据？
- 主责技能：`togaf-migration-roadmap`
- 来源：G186 §8.4.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：9；对象类型：guide:estimate_check
- 关系类型：未声明
- 关联交付物：`implementation-migration-plan`

### 分析步骤

1. 逐项回答来源十问，保留第6问负向语义和第10问数量
2. 比较各轮同范围估算与覆盖计数
3. 只在项目明示公式/应急参数时计算第8/9信号
4. 指出风险、时效和关键未知对建议的影响
5. 给停止/继续调查的有据建议，不自动批准预算

### `guide:estimate_check` 必填字段（8）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `sequence` | 来源十问顺序 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `question` | 检查问题 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `finding` | 事实/回答而非统一分数 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `rule` | 源指南建议或项目规则的归属 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `calculation` | 如适用显示数据和计算过程 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `limitation` | 缺口/时效/不可比限制 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `next_action` | 继续调查或提交决策者的建议 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

## 项目工作包授权记录

- `id`：`project-work-package-authorization`
- 英文名：Project Work Package Authorization
- 决策问题：项目WBS工作能否开始，产品、前提和授权是否齐备？
- 主责技能：`togaf-migration-roadmap`
- 来源：G188 §2.3、§3.4.1–3.4.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：13；对象类型：guide:project_authorization
- 关系类型：未声明
- 关联交付物：`statement-of-work`, `implementation-migration-plan`

### 分析步骤

1. 识别PM项目工作包及其WBS/产品范围
2. 核实前置产品验收及所有进入条件
3. 确认成本/工期/容差、质量配置及报告要求
4. 取得权限范围内PM明确授权并留记录
5. 完成并接受产品后才允许后续工作包重新走授权

### `guide:project_authorization` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `project_task_id` | 项目任务稳定ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `wbs_parent` | WBS父项 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `work_package_kind` | 必须明确project-wbs-leaf，非TOGAF变革包 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `deliverable` | 应交付产品及范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `preconditions` | 前置产品验收与其他进入条件 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `cost_time_tolerance` | 成本/工期/容差及项目规则出处 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `quality_configuration` | 质量准则、版本/配置要求 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `reporting` | 检查点频率和信息分发 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `authority` | 谁有权授权以及授权范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `authorization` | 未授权/授权证据，不能从空闲推断 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `next_action` | 允许开始或缺口处理 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

### `project` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `scope` | 本记录的组织、业务或技术边界和时点 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `sponsor` | 项目或BI用途的业务/IT赞助责任方 | 项目或BI用途的业务/IT赞助责任方；尚未接受职责须明确候选而非默认授权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `start` | 项目计划开始日期 | 项目计划开始日期；使用ISO 8601日历日期，计划存在不代表已获开工授权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S","format":"date"}`（来源：`project-operational-convention`） |
| `end` | 项目计划结束日期 | 项目计划结束日期；使用ISO 8601日历日期，与start的顺序须人工复核；类型约束：`{"type":"string","minLength":1,"pattern":"\\S","format":"date"}`（来源：`project-operational-convention`） |
| `budget` | 经费额度或未知状态 | 经费额度或未知状态；已知金额须币种、周期和批准依据，不以缺失当零；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `status` | 本类型的业务处置状态 | 本类型的业务处置状态；方案保留/淘汰与约束满足/违背分别使用专属枚举；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

---

合计 5 个工作产品，52 个字段。
