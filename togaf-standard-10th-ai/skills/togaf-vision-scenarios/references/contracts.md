# togaf-vision-scenarios 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 业务场景文档

- `id`：`business-scenario-document`
- 英文名：Business Scenario Document
- 决策问题：架构究竟为谁解决什么业务问题？
- 主责技能：`togaf-vision-scenarios`
- 来源：G176 §3–4；G176 §7–§11
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, problem, environment, objectives
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：scenario
- 关系类型：traces_to
- 关联交付物：`architecture-vision`, `statement-of-work`, `business-drivers`, `request-for-architecture-work`

### 分析步骤

1. 形成并验证前提
2. 采集归一化问题目标参与者环境
3. 建立业务与技术模型
4. 反复评审并记录需求
5. 用business-scenario-checklist-record跟踪各步骤清单与角色
6. 用smart-objective-assessment把目的做成SMART

### `scenario` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `problem` | 待解决问题及其业务证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `environment` | 业务与技术环境 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `objectives` | 期望业务结果及可衡量目的 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `human_actors` | 人的参与者与角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `computer_actors` | 计算机参与者与责任 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `requirements` | 架构要求引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 业务场景关联矩阵

- `id`：`scenario-traceability-matrix`
- 英文名：Business Scenario Traceability Matrix
- 决策问题：流程与各关键场景要素是否一致？
- 主责技能：`togaf-vision-scenarios`
- 来源：G176 §3.2.3; English PDF22–23；G176 §11.4; English PDF45–46
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "raw_records", "origin": "source", "meaning": "只读原始业务材料与定位"}, {"id": "normalized_records", "origin": "source", "meaning": "拆分复合陈述、统一术语和分类后的原子记录"}, {"id": "transformation_log", "origin": "source", "meaning": "每一步输入、输出、操作、理由、证据"}, {"id": "processes", "origin": "source", "meaning": "作为关联焦点的流程"}, {"id": "constituencies", "origin": "source", "meaning": "受影响利益相关方群体"}, {"id": "human_actors", "origin": "source", "meaning": "人的参与者"}, {"id": "computer_actors", "origin": "source", "meaning": "计算机参与者"}, {"id": "problems", "origin": "source", "meaning": "待改善问题/痛点"}, {"id": "objectives", "origin": "source", "meaning": "期望达成的结果"}
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：未知关系用缺口ID，不把空格当确定无关联。缺任一类别可生成范围受限草稿；未关联结果的痛点必须列为阻断检查项。
- 字段总数：7；对象类型：actor, application, goal, problem, process, repository_asset, stakeholder
- 关系类型：traces_to
- 关联交付物：`architecture-vision`, `statement-of-work`

### 分析步骤

1. 锁定原始资料
2. 按单点拆分复合陈述
3. 统一术语并分类，记录每次转换
4. 以流程链接五类要素，逐个关联给证据
5. 验证每个痛点至少有一个成果
6. 从已支持关系形成业务/技术需求
7. 评审是否回应原始问题，批准后才进入需求存储库

本工作产品未声明 `required_attributes`；其字段约束须由 owner 补齐后才能机器校验。

其余字段（7）：`name`、`process`、`stakeholder`、`human_actor`、`computer_actor`、`problem`、`goal`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 利益相关者影响力与影响程度矩阵

- `id`：`stakeholder-influence-matrix`
- 英文名：Stakeholder Influence-Impact Matrix
- 决策问题：依据影响力与所受影响程度选择介入策略
- 主责技能：`togaf-vision-scenarios`
- 来源：G184/fig4-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, influence, impact, engagement
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：stakeholder
- 关系类型：traces_to
- 关联交付物：`architecture-vision`, `statement-of-work`

### 分析步骤

1. 明确决策和关注点
2. 分别取得Influence与Impact证据
3. 按高低定位
4. 选择重点管理令其满意随时告知或监督
5. 核实问责与沟通边界

### `stakeholder` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `influence` | 在本工作产品范围中明确定义的 influence 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `impact` | 业务影响及其依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `engagement` | 参与方式与节奏 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `concern` | 利益相关者的具体关注点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `quadrant` | 在本工作产品范围中明确定义的 quadrant 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 业务场景步骤清单与角色记录

- `id`：`business-scenario-checklist-record`
- 英文名：Business Scenario Checklists and Roles Record
- 决策问题：业务场景每个步骤的清单完成到哪里，缺什么证据，G176的角色是否在规划步骤指定？
- 主责技能：`togaf-vision-scenarios`
- 来源：G176 §10、§11.1–11.6
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "stage", "meaning": "G176 §11清单阶段", "origin": "source-purpose-plus-project-contract"}, {"id": "responses", "meaning": "清单项结果：done需证据，not-applicable需理由，open需负责人和行动", "origin": "source-purpose-plus-project-contract"}, {"id": "uses_workshop", "meaning": "是否采用工作坊（决定工作坊条件项是否适用）", "origin": "source-purpose-plus-project-contract"}, {"id": "role_assignments", "meaning": "G176 §10角色分配：人员、指定阶段与证据", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：5；对象类型：guide:scenario-checklist-stage
- 关系类型：未声明
- 关联交付物：`architecture-vision`, `statement-of-work`

### 分析步骤

1. 选择本次涉及的清单阶段
2. 逐项记录done/not-applicable/open及证据、理由或负责人
3. 仅在采用工作坊时纳入工作坊条件项
4. 分组项按任一或全部子项规则核对
5. 在规划步骤指定项目经理、顾问、作者与编辑等角色
6. 报告未完成项，不计算完成率

### `guide:scenario-checklist-stage` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `stage` | G176 §11清单阶段 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `responses` | 清单项结果：done需证据，not-applicable需理由，open需负责人和行动 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `uses_workshop` | 是否采用工作坊（决定工作坊条件项是否适用） | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（2）：`name`、`role_assignments`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 4 个工作产品，25 个字段。
