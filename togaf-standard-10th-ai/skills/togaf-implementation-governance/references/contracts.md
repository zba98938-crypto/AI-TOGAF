# togaf-implementation-governance 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 安全审计记录

- `id`：`security-audit-record`
- 英文名：Security Audit Record
- 决策问题：实现是否遵循安全政策与要求？
- 主责技能：`togaf-implementation-governance`
- 来源：G152 §5.8
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, criterion, implementation, evidence
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：audit_finding
- 关系类型：traces_to
- 关联交付物：`compliance-assessment`

### 分析步骤

1. 确定评审对象与判据
2. 获取设计配置代码和测试证据
3. 区分符合偏离证据不足
4. 追踪纠正措施

### `audit_finding` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `criterion` | 单项判断准则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `implementation` | 实现对象或实施证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `result` | 评估结果及不确定性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `deviation` | 偏离要求的内容与处置 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 环境决策日志

- `id`：`environmental-decision-log`
- 英文名：Environmental Decision Log
- 决策问题：环境标准怎样进入架构决策？
- 主责技能：`togaf-implementation-governance`
- 来源：G242 §3.8–4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, options, environmental_criteria, evidence
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：environmental_decision
- 关系类型：traces_to
- 关联交付物：`compliance-assessment`, `business-principles`

### 分析步骤

1. 明确备选与评价边界
2. 比较环境及其他质量属性
3. 记录权衡和决策依据
4. 追溯执行与复评

### `environmental_decision` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `options` | 被比较的备选方案 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `environmental_criteria` | 环境评价准则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `tradeoff` | 环境与其他质量的权衡 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `decision` | 决策结果、理由和状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 变革画像治理检查清单

- `id`：`change-profile-governance-checklist`
- 英文名：change-profile-governance-checklist
- 决策问题：按Rapid/Functional/Robust及具体过渡，哪些规格、实施和价值条件已有证据，哪些需要返工或裁剪？
- 主责技能：`togaf-implementation-governance`
- 来源：G248 §3、§9表9-1、§11表11-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：原始业务材料和来源, 范围、状态和决策问题, source_check_id, step, adm_phase, change_profile, applicability, response, evidence_locator, owner, action, transition_id
- 可选输入：既有模型及历史结论
- 缺输入策略：缺少来源、责任、结果或决定时列缺口，不默认通过；未核实资料不能支撑批准。
- 字段总数：11；对象类型：guide:governance-check
- 关系类型：未声明
- 关联交付物：`compliance-assessment`, `architecture-contract`, `implementation-migration-plan`

### 分析步骤

1. 识别变革范围、画像及具体过渡；保留选择理由
2. 载入完整源表并记录项目纳入/排除决定
3. 逐项核对证据，区分规格可实现性与实际实施效果
4. 记录未决、负责人、措施及治理决定，变更后重审受影响项

### `guide:governance-check` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `source_check_id` | source_check_id | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `step` | step | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `adm_phase` | adm_phase | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `change_profile` | change_profile | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `applicability` | applicability | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `response` | response | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `evidence_locator` | evidence_locator | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `owner` | owner | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `action` | action | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |
| `transition_id` | transition_id | 从来源或明确的项目约定记录，保留未知和不适用理由（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

## 决策授权与可逆性登记

- `id`：`decision-delegation-register`
- 英文名：Decision Delegation and Reversibility Register
- 决策问题：某类决策由谁、在何种边界内决定，何时需扩大参与或重新评审？
- 主责技能：`togaf-implementation-governance`
- 来源：G210 §5.4（转引Management 3.0及Bezos）
- 定义状态：`guide-body-located-with-explicit-project-operational-contract`
- 必需输入：决策范围和影响对象, 参与人、权限与企业护栏, 可逆性证据和回滚条件, 组织采用的授权规则及批准状态
- 可选输入：已有模型/待办/历史决策, 组织特定规则及证据
- 缺输入策略：缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。
- 字段总数：14；对象类型：guide:delegation_decision
- 关系类型：未声明
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `compliance-assessment`, `implementation-governance-model`
- `implementation-governance-model`适用边界：项目路由：F阶段在适用时（if any）准备实施治理模型；G阶段使用其检查点、决策权和升级规则进行实施治理。关联工作产品不自动创建必需交付物、不代替适用性裁剪或真实授权。

### 分析步骤

1. 为具体决策划清范围、受影响方及护栏。
2. 记录reversible/irreversible/unknown及依据；未知不能默认为可逆。
3. 可选引用七授权名称tell/sell/consult/agree/advise/inquire/delegate，逐条用项目语言明确定谁决定、谁参与。
4. 不可逆或可逆性不明时明确更广群体及需补证据；不从数值等级自动推导批准。
5. 记录提案、批准证据与复评触发，授权状态与架构实现状态独立。

### `guide:delegation_decision` 必填字段（13）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `decision_scope` | 授权适用的具体决定、对象和影响边界 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `delegation_level` | G210引用的Management3.0名称之一；只作词汇，具体权责另列 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `framework_origin` | 外部方法归属与项目操作化说明，防止冒充TOGAF独创 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `authority` | 谁在听取谁意见后做何种决定的项目明文约定 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `participants` | 需要参与当前决策的团队或角色，不仅列被通知人 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `reversibility` | reversible/irreversible/unknown；对整个决定结果而非单一技术动作判断 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `reversibility_evidence` | 支持可逆性判断的业务与技术证据或明确缺口 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `rollback_plan` | 回滚方式、条件与未覆盖部分；不可回滚明确not-available | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `guardrails` | 授权不能突破的企业/项目约束及范围 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `authorization_status` | 授权安排本身的proposed/approved等状态；批准需要真实证据 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `review_trigger` | 哪些范围、消费者、规则或恢复条件变化要求复评 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `decision_result` | 当前决定或建议及未决条件，不由授权级别自动推导 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `source_refs` | 支持本条业务内容的来源ID列表，区别指南定义来源 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |

### `decision_record` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `question` | 待回答的完整业务问题 | 待回答的完整业务问题；保留原问题上下文，不以结论或简称替代；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `options_considered` | 决策审议过的选项集合 | 决策审议过的选项集合；至少保留候选与被拒原因，不事后只记选中项；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `decision` | 待作或已作的业务决定 | 待作或已作的业务决定；写问题、选项与结果边界，建议不自动成为批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `authority` | 谁在听取谁意见后做何种决定的项目明文约定 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `rationale` | 本次选择的理由与依据 | 本次选择的理由与依据；解释与备选的区别，不循环引用选择结果作证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `date` | 决策记录日期 | 决策记录日期；使用ISO 8601日历日期，不能以计划日期冒充已决定日期；类型约束：`{"type":"string","minLength":1,"pattern":"\\S","format":"date"}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

## 可持续ICT采购战略

- `id`：`sustainable-procurement-strategy`
- 英文名：Sustainable Procurement Strategy
- 决策问题：如何在服务范围、地点、合同和全生命周期中形成可证实采购选择？
- 主责技能：`togaf-implementation-governance`
- 来源：G242 §3.7.1–3.7.3、§4.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：组织、服务、业务用途及所评估期间/生命周期边界, 原始访谈、使用数据、供应商记录及稳定证据ID, 适用目标、职责和组织自定决策规则；未知项显式登记
- 可选输入：历史评估、环境数据目录、采购契约及角色技能资料
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：14；对象类型：guide:sustainable_procurement
- 关系类型：未声明
- 关联交付物：`implementation-migration-plan`, `architecture-contract`

### 分析步骤

1. 明确业务用途寿命及采购/外包/所在地方案
2. 要求端到端数据、抵消与可再生采购分别公开
3. 与法务将手段义务和结果义务分别写成可验证条款
4. 比较全生命周期成本、修理能力、退出及供应链访问
5. 按有来源的组织准则权衡；缺资料时给补证/不选择结论

### `guide:sustainable_procurement` 必填字段（13）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `option` | 候选方案/范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `sourcing` | 内包/外包/采购/服务获取 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `location` | 在岸/近岸/离岸及实际地区证据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `lifecycle_evidence` | 端到端足迹、可再生采购和抵消分列 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `whole_life_tco` | 购置、运行、维护、退出等范围和缺项 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `means_obligations` | 证明培训/方法/度量等手段 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `result_obligations` | 可验证成果承诺 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `end_of_use` | 翻新/回收/拆解去向与证据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `supply_chain_access` | 中间环节/供应链访问和演进参与 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `gaps` | 影响比较和选择的数据缺口 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision_rule` | 组织自定准则，不默认权重 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `recommendation` | 候选处理，不自动选商 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `authority` | 发起人决定、法务审查等 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

用途—应用/数据—基础设施用稳定ID追踪；评估维度与功能多对多关联；总额与子集、两种Scope2基础、抵消和复制存储分别表达。表格相邻不代表因果或可相加。

## 云与外包环境数据共享契约

- `id`：`cloud-environmental-data-contract`
- 英文名：Cloud Environmental Data Contract
- 决策问题：服务提供方应以哪些边界和口径交付可审查环境数据？
- 主责技能：`togaf-implementation-governance`
- 来源：G242 §6表6-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：组织、服务、业务用途及所评估期间/生命周期边界, 原始访谈、使用数据、供应商记录及稳定证据ID, 适用目标、职责和组织自定决策规则；未知项显式登记
- 可选输入：历史评估、环境数据目录、采购契约及角色技能资料
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：10；对象类型：guide:cloud_environmental_field
- 关系类型：未声明
- 关联交付物：`architecture-contract`, `architecture-repository`

### 分析步骤

1. 确认提供方、服务、使用实体、期间与服务分配依据
2. 按拟议19字段逐项收集原始值和单位、测量期间
3. 同时保留市场/地点Scope2，设备Scope3包含关系及抵消独列
4. 检查年度/月度、制造/运行水、复制存储与进出流量口径
5. 给缺口/冲突清单后交给独立核算方法；不在数据契约中自动合计排放

### `guide:cloud_environmental_field` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `sequence` | G242拟议19字段顺序 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `field_key` | 稳定字段key | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `value` | 供应方原始值，未知显式保存 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `unit` | 原始单位 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `period` | 该值测量期间 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `service_boundary` | 服务/组织实体/生命周期/分配边界 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `semantics` | 互斥、包含、抵消、复制等含义 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 供应方报告/方法证据ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `quality` | 完整/未知及口径待确认 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

用途—应用/数据—基础设施用稳定ID追踪；评估维度与功能多对多关联；总额与子集、两种Scope2基础、抵消和复制存储分别表达。表格相邻不代表因果或可相加。

## 解决方案交付笔记本

- `id`：`solution-delivery-notebook`
- 英文名：Solution Delivery Notebook (Architecture Contract Template)
- 决策问题：交付团队据以设计和测试的需求/规格、风险/控制配对、差距范围与目标架构摘要是什么？
- 主责技能：`togaf-implementation-governance`
- 来源：G186 附录D 表D-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "work_package_id", "meaning": "笔记本所对应的工作包", "origin": "source-purpose-plus-project-contract"}, {"id": "solution_concept_ref", "meaning": "解决方案概念图视图ID", "origin": "source-purpose-plus-project-contract"}, {"id": "implementation_strategy", "meaning": "处理差距或工作包的首选方法", "origin": "source-purpose-plus-project-contract"}, {"id": "stakeholders", "meaning": "利益相关者及其需求ID", "origin": "source-purpose-plus-project-contract"}, {"id": "requirements", "meaning": "入向需求及利益相关者ID", "origin": "source-purpose-plus-project-contract"}, {"id": "specifications", "meaning": "架构规格；每条追溯到一项需求", "origin": "source-purpose-plus-project-contract"}, {"id": "risks", "meaning": "适用风险；无控制时记录有证据的处理决定", "origin": "source-purpose-plus-project-contract"}, {"id": "controls", "meaning": "控制；每条追溯到一项风险", "origin": "source-purpose-plus-project-contract"}, {"id": "gaps", "meaning": "差距及in_scope真假", "origin": "source-purpose-plus-project-contract"}, {"id": "architecture_summary", "meaning": "各域目标架构视图引用或不适用理由（仅供参考）", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：11；对象类型：guide:solution-delivery-notebook
- 关系类型：未声明
- 关联交付物：`architecture-contract`, `compliance-assessment`

### 分析步骤

1. 写解决方案摘要：概念图、利益相关者目录、风险目录、差距目录
2. 写规格摘要：实施策略、架构规格、控制
3. 每条规格追溯到需求，每个控制追溯到风险
4. 标出本工作包处理与不处理的差距
5. 用视图引用概述各域目标架构（仅供参考）
6. 用需求/规格与风险/控制两类配对作为合规评估依据

### `guide:solution-delivery-notebook` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `work_package_id` | 笔记本所对应的工作包 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `solution_concept_ref` | 解决方案概念图视图ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `implementation_strategy` | 处理差距或工作包的首选方法 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `stakeholders` | 利益相关者及其需求ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `requirements` | 入向需求及利益相关者ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `specifications` | 架构规格；每条追溯到一项需求 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `risks` | 适用风险；无控制时记录有证据的处理决定 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `controls` | 控制；每条追溯到一项风险 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `gaps` | 差距及in_scope真假 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `architecture_summary` | 各域目标架构视图引用或不适用理由（仅供参考） | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（1）：`name`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

## 产品边界与企业约束登记

- `id`：`product-constraint-register`
- 英文名：Product Boundary and Enterprise Constraint Register
- 决策问题：架构定义了哪些产品、边界与产品负责人约束，哪些待办项与约束冲突，是否有阶段G豁免？
- 主责技能：`togaf-implementation-governance`
- 来源：G186 §12.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "products", "meaning": "产品、边界、产品负责人及架构依据", "origin": "source-purpose-plus-project-contract"}, {"id": "constraints", "meaning": "对产品的企业约束及架构依据", "origin": "source-purpose-plus-project-contract"}, {"id": "backlog_items", "meaning": "产品待办项及冲突约束", "origin": "source-purpose-plus-project-contract"}, {"id": "dispensations", "meaning": "阶段G豁免：约束、权限、理由、到期日与证据", "origin": "source-purpose-plus-project-contract"}, {"id": "purpose", "meaning": "本登记的用途与范围说明", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：6；对象类型：guide:product-constraint-register
- 关系类型：未声明
- 关联交付物：`architecture-contract`, `compliance-assessment`

### 分析步骤

1. 从组合或项目架构列出产品、边界与产品负责人
2. 登记对产品的企业约束及架构依据
3. 标记与约束冲突的待办项
4. 冲突项只有在阶段G有证据豁免时放行，否则阻止
5. 豁免到期前复核

### `guide:product-constraint-register` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `products` | 产品、边界、产品负责人及架构依据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `constraints` | 对产品的企业约束及架构依据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `backlog_items` | 产品待办项及冲突约束 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `dispensations` | 阶段G豁免：约束、权限、理由、到期日与证据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（2）：`name`、`purpose`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 8 个工作产品，80 个字段。
