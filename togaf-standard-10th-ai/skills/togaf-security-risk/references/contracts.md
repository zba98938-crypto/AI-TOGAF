# togaf-security-risk 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 风险偏好

- `id`：`risk-appetite`
- 英文名：Risk Appetite
- 决策问题：承担多大风险才能实现业务结果？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.1.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, scope, impact_scale, likelihood_scale
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：risk_appetite
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 界定风险范围和风险所有者
2. 记录影响与可能性尺度
3. 定义可接受边界及超限处置
4. 用真实业务场景检验边界

### `risk_appetite` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `impact_scale` | 影响评价尺度及锚点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `likelihood_scale` | 可能性评价尺度及锚点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `acceptance_boundary` | 风险可接受范围及超限判据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `approval_authority` | 拥有批准权限的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 业务影响分析

- `id`：`business-impact-analysis`
- 英文名：Business Impact Analysis
- 决策问题：安全不足会使哪些业务结果受损？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.1.4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_process, loss_type, impact
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：impact_scenario
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从关键业务结果识别中断或损失场景
2. 记录影响类型与时间范围
3. 确认关键风险领域
4. 把结果交给风险评估

### `impact_scenario` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_process` | 受影响的业务流程引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `loss_type` | 业务损失或收益的类型 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `impact` | 业务影响及其依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `criticality` | 相对业务关键性及判据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `time_horizon` | 分析覆盖的时间窗口 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `risk_asset` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `asset_id` | 风险资产稳定标识 | 风险资产稳定标识；同一范围唯一，重命名不改变身份；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `criticality` | 相对业务关键性及判据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 本记录、行动或计划的责任方 | 本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `confidentiality_need` | 资产保密需求 | 资产保密需求；说明受限信息、可访问角色及泄露影响的分类依据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `integrity_need` | 资产完整性需求 | 资产完整性需求；列容许误差、修改权限和损坏影响的判断依据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `availability_need` | 资产可用性需求 | 资产可用性需求；列服务时段、允许中断与恢复依据，不预设统一等级；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全资源计划

- `id`：`security-resource-plan`
- 英文名：Security Resource Plan
- 决策问题：架构工作需要哪些安全与风险人员？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.1.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, role, authority, capacity
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：security_resource
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从范围和高风险关注点识别能力需求
2. 比较现有安全支持与专职投入
3. 明确角色授权
4. 安排参与与能力缺口措施

### `security_resource` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `role` | 承担职责的角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `capacity` | 可投入的资源容量 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `availability` | 指定期间可用资源 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `engagement` | 参与方式与节奏 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全蓝图

- `id`：`security-blueprint`
- 英文名：Security Blueprint
- 决策问题：愿景如何使利益相关者确信风险可接受？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, concern, principle, risk
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：application, security_component
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 收集安全关注点
2. 建立业务风险和原则语境
3. 选择高层安全服务与边界
4. 追溯到后续阶段细化要求

### `security_component` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `concern` | 利益相关者的具体关注点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `principle` | 适用原则引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `risk` | 风险对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `service` | 服务对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 业务属性画像

- `id`：`business-attribute-profile`
- 英文名：Business Attribute Profile
- 决策问题：安全架构以什么业务价值衡量？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.10.1; English PDF40–41
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "business_case_ref", "origin": "source", "meaning": "当前业务论证及业务驱动"}, {"id": "attribute_definition", "origin": "source", "meaning": "按业务语境定义的属性，含边界"}, {"id": "measurement_approach", "origin": "source", "meaning": "获取和解释指标的方法"}, {"id": "metrics", "origin": "source-plus-project-contract", "meaning": "带单位、尺度、时期、样本、证据及计算依据的指标"}, {"id": "target", "origin": "source", "meaning": "与业务论证关联的绩效目标"}, {"id": "tolerable_deviation", "origin": "source", "meaning": "管理层在介入前允许的最大结果偏差"}, {"id": "frequency_or_cost_threshold", "origin": "source-conditional", "meaning": "业务采用时记录事件频率/成本阈值；不适用须说明，非强制统一指标"}, {"id": "corrective_action_trigger", "origin": "source", "meaning": "超过业务容忍范围时的显式管理动作"}
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：缺业务论证、量表、目标或容差时生成带ID草稿和阻断项；可以给出观测值，不能判定达标或违规。未知值不填零。
- 字段总数：12；对象类型：business_attribute, control_objective, goal, requirement
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 锁定原始材料及出处
2. 提炼业务关注，按业务语境重定义属性
3. 明确测量样本、分子分母和口径
4. 引用项目已声明目标及容差，不自行补值
5. 从原始数据计算观测并解释目标差值与纠偏触发
6. 建立业务论证—属性—要求—控制目标追溯
7. 提交缺口和纠偏建议供实际责任人评审

### `business_attribute` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_case_ref` | 本业务属性对应的业务论证引用 | 本业务属性对应的业务论证引用；应可定位价值、风险或成本依据；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `measurement_approach` | 业务属性度量方法 | 业务属性度量方法；定义样本、算法、单位、周期与观察来源，不任意加权；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `metric` | 度量方法和计算定义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `target` | 期望结果或目标值 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `tolerable_deviation` | 业务属性可容忍偏差 | 业务属性可容忍偏差；列单位、上下界和业务依据，不能无来源假设统一百分比；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `corrective_action_trigger` | 业务属性纠正触发条件 | 业务属性纠正触发条件；以偏差、发生频率或成本阈值关联明确处置；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `frequency_or_cost_threshold` | 偏差频率或处置成本阈值 | 偏差频率或处置成本阈值；数值须周期、币种或单位及项目批准口径；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `source_refs` | 业务属性定义和观察的来源ID或定位集合 | 业务属性定义和观察的来源ID或定位集合；至少一项，不伪造原文强制字段；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `unit` | 度量单位 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `observation` | 范围内实际观察或明确未取得材料 | 范围内实际观察或明确未取得材料；事实、推论和行动不得混写；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全策略架构

- `id`：`security-policy-architecture`
- 英文名：Security Policy Architecture
- 决策问题：安全政策如何分层及分配责任？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.3.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, scope, authority, accountability
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：security_policy
- 关系类型：project:policy_specializes
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`, `architecture-principles`

### 分析步骤

1. 识别业务安全政策
2. 区分治理层级和领域
3. 明确政策权威与问责
4. 检查政策冲突和连续性联系

### `security_policy` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `accountability` | 最终问责关系 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `policy_level` | 政策在治理结构中的层级 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `review_cycle` | 复核周期 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全域模型

- `id`：`security-domain-model`
- 英文名：Security Domain Model
- 决策问题：哪些资产受同一安全策略管辖？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.3.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, policy_authority, classification, assets
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：application, security_domain
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 按相同安全属性与政策分组资产
2. 界定域内政策权威
3. 识别外部责任交换
4. 评估联邦合同与共同对象

### `security_domain` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `policy_authority` | 安全域内的政策制定与执行权威 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `classification` | 安全分类标签 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `assets` | 受该政策或域管辖的资产引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `boundary` | 内外边界的含义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `federation` | 跨组织联邦范围和协议 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 信任框架

- `id`：`trust-framework`
- 英文名：Trust Framework
- 决策问题：谁基于什么条件信任谁？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.3.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_basis, legal_basis, direction
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：goal, trust_party
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 识别业务关系各方
2. 记录业务法律与政策依据
3. 声明单向双向或不存在的信任
4. 限定条件与责任

### `trust_party` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_basis` | 信任所依据的业务关系 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `legal_basis` | 信任所依据的法律协议 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `direction` | 有向或双向关系的明确读法 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `conditions` | 关系或规则成立的条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 业务风险模型／风险登记册

- `id`：`business-risk-register`
- 英文名：Business Risk Register
- 决策问题：哪些风险需要处置并由谁负责？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.3.4–5.3.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, asset, threat, vulnerability
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：9；对象类型：application, control, control_objective, loss_event, risk, risk_asset, security_requirement, threat_event, vulnerability
- 关系类型：causes_loss, derived_from, exploits, impacts_asset, implements_control, requires_control, risk_has_control, traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 识别资产与失败场景
2. 关联威胁脆弱性和损失
3. 按声明方法评估
4. 比较风险偏好
5. 记录处置和剩余风险

### `risk` 必填字段（8）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `asset` | 风险资产引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `threat` | 威胁主体或事件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `vulnerability` | 可被利用的脆弱性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `likelihood` | 已声明尺度下的事件可能性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `impact` | 业务影响及其依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `treatment` | 选定风险处置及理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `residual_risk` | 处置后的剩余风险及评价依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `threat_event` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `threat_actor_ref` | 威胁主体的引用 | 威胁主体的引用；未知主体明确unknown，不凭事件后果臆造攻击者；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `event_time` | 威胁事件发生时点或窗口 | 威胁事件发生时点或窗口；区分已观察、推测和未知时间，不伪造事件记录；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `likelihood_scale` | 威胁事件可能性量表与锚点 | 威胁事件可能性量表与锚点；没有数据不填概率，业务影响不能替代发生可能性；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence` | 威胁事件支持证据的来源引用 | 威胁事件支持证据的来源引用；不能以风险评估结论循环证明事件事实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 适用法律法规登记册

- `id`：`applicable-legislation-register`
- 英文名：Applicable Legislation Register
- 决策问题：哪些法规适用于本次架构范围？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.3.6
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, jurisdiction, version, applicability
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：legal_obligation
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 识别功能数据和司法辖区
2. 记录适用条款与版本
3. 关联架构要求和责任
4. 安排法规变化复核

### `legal_obligation` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `jurisdiction` | 适用司法辖区 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `version` | 来源或规范版本 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `business_function` | 业务功能引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `data_scope` | 受条款影响的数据范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
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

## 适用控制框架登记册

- `id`：`applicable-control-framework-register`
- 英文名：Applicable Control Framework Register
- 决策问题：采用哪些控制框架来应对风险？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.3.7
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, version, selection_reason, scope
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：control_framework
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从监管认证和风险要求形成候选
2. 比较框架覆盖
3. 界定必须与建议控制
4. 记录选择依据和版本

### `control_framework` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `version` | 来源或规范版本 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `selection_reason` | 选择该方案或框架的理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `mandatory_controls` | 必须满足的控制要求 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `certification` | 所需认证及适用范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全服务目录

- `id`：`security-services-catalog`
- 英文名：Security Services Catalog
- 决策问题：哪些安全服务实现安全目标？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, definition, objective, owner
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：security_service
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从控制目标定义安全服务
2. 标识可复用构建块
3. 记录使用与运营信息
4. 连接需求控制和实施

### `security_service` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `objective` | 服务或控制所实现的目的 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `operations` | 运行与维护要求 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `consumers` | 服务消费者 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `implementation` | 实现对象或实施证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `control_objective` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `objective_statement` | 控制目标要实现的安全结果 | 控制目标要实现的安全结果；不是产品清单或已执行控制声明；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `control_ref` | 实现控制目标的控制记录引用 | 实现控制目标的控制记录引用；控制目标不等同控制已执行；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `evidence_ref` | 控制测试证据的稳定引用 | 控制测试证据的稳定引用；须可定位记录，测试计划不能代替执行结果；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `test_result` | 控制目标测试的实际结果 | 控制目标测试的实际结果；区分通过、失败、未执行，须关联方法、时间与证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全分类方案

- `id`：`security-classification-scheme`
- 英文名：Security Classification Scheme
- 决策问题：资产分类将触发哪些安全要求？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, classification_scheme, criteria, requirements
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：security_classification
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 声明分类方案
2. 按资产特征分类
3. 映射访问保密和可用性要求
4. 核查资产所有者责任

### `security_classification` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `classification_scheme` | 分类规则与版本 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `criteria` | 评价准则及尺度 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `requirements` | 架构要求引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 风险缓解计划

- `id`：`risk-mitigation-plan`
- 英文名：Risk Mitigation Plan
- 决策问题：如何把风险降至可接受水平？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.6
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, risk, action, owner
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：risk_treatment
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 比较提高控制转移规避延迟补偿等选项
2. 评价新架构带来的风险
3. 安排责任与验证
4. 复评剩余风险

### `risk_treatment` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `risk` | 风险对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `action` | 拟采取的具体行动 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `due_date` | 行动计划完成日期 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `control` | 控制措施引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `expected_residual` | 预期剩余风险及假设 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 过渡范围风险评估

- `id`：`transition-risk-assessment`
- 英文名：Transition Risk Assessment
- 决策问题：迁移过程本身会带来什么风险？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.7
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, state_id, migration_activity, impact
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：transition_risk
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 界定过渡状态和迁移活动
2. 分析生产环境风险
3. 关联缓解与回退
4. 检查可运营性和控制连续性

### `transition_risk` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `migration_activity` | 迁移活动引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `impact` | 业务影响及其依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `likelihood` | 已声明尺度下的事件可能性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `mitigation` | 降低风险的措施 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（2）：`name`、`state_id`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全影响分析

- `id`：`security-impact-analysis`
- 英文名：Security Impact Analysis
- 决策问题：架构变更怎样改变安全与风险？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.7、5.9
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, change, affected_asset, requirement
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：security_impact
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`, `requirements-impact-assessment`

### 分析步骤

1. 定位变化对象
2. 沿已知关系查找安全需求控制和风险
3. 区分候选与确认影响
4. 提出复评或新 ADM 迭代建议

### `security_impact` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `change` | 待评估变更引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `affected_asset` | 经分析受影响的资产 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `requirement` | 需求对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `control` | 控制措施引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `risk` | 风险对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `decision` | 决策结果、理由和状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 安全培训与意识计划

- `id`：`security-training-plan`
- 英文名：Security Training and Awareness Plan
- 决策问题：哪些人员需要掌握控制的正确使用？
- 主责技能：`togaf-security-risk`
- 来源：G152 §5.8
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, audience, control, competency
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：training_need
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从控制部署配置运营识别技能需要
2. 区分用户与特权人员
3. 安排培训和验证
4. 保存实际记录

### `training_need` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `audience` | 培训受众与角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `control` | 控制措施引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `competency` | 所需知识技能和行为 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `activity` | 实施或学习活动 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `review` | 复核方法及责任 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

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

合计 17 个工作产品，117 个字段。
