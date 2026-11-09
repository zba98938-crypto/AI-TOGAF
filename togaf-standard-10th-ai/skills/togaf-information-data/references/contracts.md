# togaf-information-data 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 数据质量评估

- `id`：`data-quality-assessment`
- 英文名：Data Quality Assessment
- 决策问题：数据质量能否支持业务与风险目标？
- 主责技能：`togaf-information-data`
- 来源：G152 §5.4；G234 §4.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, dataset, dimension, metric
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：8；对象类型：data_quality_measure
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 确定数据集与质量责任
2. 选定相关维度和可计算定义
3. 使用日志或样本评估
4. 关联业务影响和改进措施

### `data_quality_measure` 必填字段（7）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dataset` | 被评价或使用的数据集 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `dimension` | 评价维度 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `metric` | 度量方法和计算定义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `unit` | 度量单位 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `threshold` | 判定边界及依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence_period` | 证据采集期间 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `data_quality_rule` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dimension` | 评价维度 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rule_expression` | 可执行或可复核的数据质量规则表达式 | 可执行或可复核的数据质量规则表达式；注明字段、判定条件及未知值处理；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `threshold` | 判定边界及依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `measure_period` | 数据质量测量时间窗 | 数据质量测量时间窗；明确起止与时区或采样周期，不能混合不同窗口结果；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
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

## 元数据字典

- `id`：`metadata-dictionary`
- 英文名：Metadata Dictionary
- 决策问题：元数据资产究竟表示什么？
- 主责技能：`togaf-information-data`
- 来源：G234 §3、§5.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, metadata_category, definition, domain
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：metadata_asset
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 界定业务技术运营范围
2. 定义条目和域
3. 指定所有权
4. 关联业务需求与技术资产

### `metadata_asset` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `metadata_category` | 业务、技术或运营元数据类别 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `domain` | 属性允许的值域或业务域 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `source` | 该条内容的输入来源 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `quality` | 所需或观察到的数据质量 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数据使用文档

- `id`：`data-usage-documentation`
- 英文名：Data Usage Documentation
- 决策问题：谁为何在什么条件下使用数据？
- 主责技能：`togaf-information-data`
- 来源：G234 §3、§5.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, dataset, user_role, purpose
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：data_usage
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从用例识别使用者和目的
2. 记录访问与生命周期条件
3. 关联政策和业务流程
4. 检查用途冲突

### `data_usage` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dataset` | 被评价或使用的数据集 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `user_role` | 使用数据的角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `purpose` | 数据使用目的 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `access_condition` | 访问允许条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `retention` | 数据保留规则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `lawful_basis` | 数据使用的法规或政策依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 元数据规则与政策文档

- `id`：`metadata-policy-documentation`
- 英文名：Metadata Rule and Policy Documentation
- 决策问题：怎样保证元数据被一致维护？
- 主责技能：`togaf-information-data`
- 来源：G234 §3、§5.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, scope, rule, authority
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：metadata_policy
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 收集监管和业务规则
2. 形式化验证条件
3. 明确维护责任和例外流程
4. 与质量需求对齐

### `metadata_policy` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rule` | 可验证规则陈述 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `validation` | 校验条件与方法 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `exception` | 例外及其治理方式 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `version` | 来源或规范版本 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数据问题文档／登记册

- `id`：`data-issue-register`
- 英文名：Data Issue Register
- 决策问题：哪些数据问题应优先解决？
- 主责技能：`togaf-information-data`
- 来源：G234 §3、§4.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, dataset, symptom, business_impact
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：data_issue
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 记录可观察症状与证据
2. 关联受影响数据和用例
3. 分析候选根因
4. 追踪处置和效果

### `data_issue` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dataset` | 被评价或使用的数据集 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `symptom` | 可观察的数据问题症状 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `business_impact` | 对业务的影响 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `root_cause` | 已验证根因或明确标记的候选根因 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `status` | 该条记录的工作状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
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

## 业务与技术资产关联

- `id`：`business-technical-asset-mapping`
- 英文名：Business-Technical Asset Mapping
- 决策问题：业务概念落在哪些技术资产上？
- 主责技能：`togaf-information-data`
- 来源：G234 §3、§4.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, metadata_category, business_meaning, technical_locator
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：goal, metadata_asset
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 识别业务与技术资产身份
2. 定义关联类型与粒度
3. 记录源头和转换
4. 验证覆盖与多义映射

### `metadata_asset` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `metadata_category` | 业务、技术或运营元数据类别 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `business_meaning` | 业务概念的含义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `technical_locator` | 技术资产定位符 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `source` | 该条内容的输入来源 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 元数据存储库设计

- `id`：`metadata-repository-design`
- 英文名：Metadata Repository Design
- 决策问题：元数据如何存储治理和供不同社区使用？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.1、§4.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, scope, community, authority
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：application, metadata_repository
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 确定用户与元数据范围
2. 比较集中专用与集成存储
3. 设计概念逻辑模型
4. 定义变更校验与交换契约

### `metadata_repository` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `community` | 元数据贡献或使用社区 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `model` | 所采用数据模型 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `integration` | 与其他系统的集成约定 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `governance` | 治理责任及变更规则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 元数据模型

- `id`：`metadata-model`
- 英文名：Metadata Model
- 决策问题：哪些元数据对象和关系足以支撑需求？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.3；图4-5、4-6
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, metadata_category, definition, attributes
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：metadata_asset
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 从业务需求识别关键资产
2. 建立业务技术运营分类
3. 细化属性域和标识
4. 核查资产关联与生命周期

### `metadata_asset` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `metadata_category` | 业务、技术或运营元数据类别 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `definition` | 业务含义和排除边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `identifier` | 对象标识与唯一性规则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `domain` | 属性允许的值域或业务域 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（2）：`name`、`attributes`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 元数据资产覆盖矩阵

- `id`：`metadata-asset-coverage`
- 英文名：Metadata Asset Coverage Matrix
- 决策问题：所需元数据范围是否覆盖管理关注点？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.3；图4-5；G234 §5.2 图5-2、表5-2 L641–664；G234 §4.3 图4-5（现有工作产品扩展关系）
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, metadata_category, management_dimension, definition
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则, 按需使用 metadata-application-function-coverage，输入功能/工具/资产覆盖证据；不改变原默认分类矩阵
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：criterion, metadata_asset
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 确定三类元数据和四个管理维度
2. 归置资产
3. 检查业务需求所需但缺失的条目
4. 记录裁剪

本工作产品未声明 `required_attributes`；其字段约束须由 owner 补齐后才能机器校验。

其余字段（6）：`name`、`metadata_category`、`management_dimension`、`definition`、`owner`、`coverage`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 元数据校验工作流

- `id`：`metadata-validation-workflow`
- 英文名：Metadata Validation Workflow
- 决策问题：谁在何时保证元数据质量？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.2.2、§4.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, actor, action, input
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：metadata_activity
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 比较规范式与协作式质量方法
2. 明确创建校验发布变更角色
3. 规定异常和回路
4. 对应质量目标

### `metadata_activity` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `actor` | 执行活动的主体 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `action` | 拟采取的具体行动 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `input` | 活动必需输入 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `validation` | 校验条件与方法 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `output` | 活动输出 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `order` | 明确次序号 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 元数据集成模型

- `id`：`metadata-integration-model`
- 英文名：Metadata Integration Model
- 决策问题：多个元数据源如何协作并避免孤岛？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.3；图4-7、4-8
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, integration_style, authority, scope
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：metadata_repository
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 比较集中混合统一模型
2. 明确各库主次权威
3. 定义交换契约
4. 检查一致性和社区协作

### `metadata_repository` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `integration_style` | 集中、混合或统一等组织方式 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `contract` | 数据或元数据交换契约 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `synchronization` | 同步方向、时效和一致性条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
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

## 元数据采集备选方案

- `id`：`metadata-ingestion-options`
- 英文名：Metadata Ingestion Options
- 决策问题：选择手工、推送还是拉取元数据？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.3；图4-9
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, mechanism, responsibility, frequency
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：metadata_component, metadata_repository, metadata_source
- 关系类型：pulls_metadata, pushes_metadata, traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 识别源系统与采集责任
2. 区分控制命令和回传信息
3. 比较人工API代理机制
4. 权衡时效负担安全

### `metadata_component` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `mechanism` | 手工、推送或拉取等机制 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `responsibility` | 各方责任及边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `frequency` | 执行或交换频率 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `protocol` | 交互协议 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `security` | 安全要求与处理 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `cost` | 成本及估算边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 技术元数据推断方案

- `id`：`metadata-inference-design`
- 英文名：Technical Metadata Inference Design
- 决策问题：抽取技术元数据需要访问什么？
- 主责技能：`togaf-information-data`
- 来源：G234 §4.3；图4-10
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, data_structure, schema_access, content_access
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：inference_source
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 区分结构化半结构化非结构化
2. 确定可用模式与稳定性
3. 判断是否必须扫描内容
4. 评估成本隐私和风险

### `inference_source` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `data_structure` | 结构化、半结构化或非结构化类别 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `schema_access` | 所需数据模式访问 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `content_access` | 是否及如何访问实际内容 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `cost` | 成本及估算边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `risk` | 风险对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
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

## 客户主数据模型

- `id`：`customer-mdm-model`
- 英文名：Customer Master Data Model
- 决策问题：怎样形成可复用的客户主数据？
- 主责技能：`togaf-information-data`
- 来源：G21B §4–5；G21B 附录A.1–A.2；G21B §4.4、§6.1.1–6.1.2；G21B §3、§5.2.2；G21B §5.2.1表5-3；G21B §5.2.2表5-4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_identity, identifier, source
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：51；对象类型：master_data, guide:mdm_diagnostic_answer, guide:mdm_plateau, guide:mdm_match_case, ops:functional_coverage
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 确定客户内核与业务语境
2. 分析源记录身份匹配
3. 定义质量和责任
4. 建立模型与分发关系
5. 保持十问题ID与原问题含义
6. 逐项取证，区分否定、未知、部分和不适用
7. 将缺口映射行动、责任、影响；不得按yes比例冒充成熟度
8. 识别当前主控和可用业务能力
9. 分开分析黄金记录与运营主控
10. 逐状态验证用例/质量/授权/恢复/支持条件
11. 选择演进触发，不强制固定四期
12. 区分业务键、技术键与姓名属性
13. 按给定规则提出候选，不直接自动合并
14. 人工判定并保留来源/版本/证据
15. 执行前验证可取消合并与历史语义
16. 加载随技能携带的完整源表，保留参考分组/ID/出处
17. 限定项目范围和时点，逐项寻找组织活动或实际应用功能证据
18. 区分已见、计划、未知和有理由不适用
19. 不得以宏观组或产品名称推断子项覆盖
20. 对缺口形成具体补证/实现/复评行动，不合成成熟度分数

### `master_data` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_identity` | 业务身份定义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `identifier` | 对象标识与唯一性规则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `source` | 该条内容的输入来源 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `matching` | 匹配与合并规则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `ownership` | 数据所有权及责任 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `quality` | 所需或观察到的数据质量 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:mdm_diagnostic_answer` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `question_number` | 附录A.2原始问题编号1–10，不能跳过 | MDM来源附录A.2问题编号；1至10逐项保留，不跳题合并；类型约束：`{"type":"integer","minimum":1,"maximum":10}`（来源：`project-operational-convention`） |
| `question` | 原问题的完整业务含义 | 待回答的完整业务问题；保留原问题上下文，不以结论或简称替代；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `answer` | yes/no/partial/unknown/not-applicable-with-reason项目文字判断 | 逐题文字回答；未知和不适用须有理由，不转换为默认零分；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 实际观察或明确未取得证据 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `consequence` | 对C-MDM运营与决策的影响 | 诊断回答对C-MDM运营和决策的影响；与改进行动分列；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `action` | 补证据/改进/复评行动 | 补证或改进行动；记录责任方、触发或期限及未关闭事项；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `owner` | 行动负责人 | 本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `scope` | 诊断范围与时点 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `scoring` | 明确none；无来源不得合成总分 | 明确评分模型与依据或none/null；没有来源和项目授权不合成成熟度总分；类型约束：`{"anyOf":[{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]},{"type":"null"}]}`（来源：`project-operational-convention`） |

### `guide:mdm_plateau` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `state_ref` | 命名状态ID，连接v2 states | 命名架构状态的稳定引用；baseline/transition/target另填，状态不授予批准；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evolution_kind` | baseline/transition/target，不是审批状态 | 架构演进种类；仅baseline/transition/target，与审批和实施状态独立；类型约束：`{"type":"string","enum":["baseline","transition","target"]}`（来源：`project-operational-convention`） |
| `mastership` | 按属性/范围声明主控 | 按对象、属性与业务范围声明主控系统；跨源冲突须记录权威及例外；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `golden_record` | 是否可信及分析/运营用途 | 黄金记录的可信范围与用途；分析可用不等于运营写回已授权；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `CRUD_ownership` | 谁可创建读取更新删除 | 按主数据对象或属性列C/R/U/D操作责任；冲突权威须保留待裁决；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `propagation` | 方向、同步或异步、版本/重试语义 | 主数据传播方向与机制；记录同步或异步、版本、重试与冲突策略；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `use_cases` | 该态可实际运行的用例 | 主数据当前态可实际运行的业务用例；计划用例与已验证运营能力分开；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `operating_gate` | 投入该态需验证条件 | 主数据本态投入运营的验证条件；包括责任、可运行用例和恢复限制，未满足不称就绪；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `next_trigger` | 演进触发，非凭日期 | 主数据下一演进态的触发条件；不是凭时间到期自动迁移；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `rollback` | 可操作恢复与未决限制 | 主数据演进的可操作恢复办法；说明恢复ID、原值、版本和消费者关联及未决限制；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `scope` | 内核边界与排除 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `source_mapping` | 参考态与本地裁剪关系 | 来源参考态或原图映射与本地裁剪的对应；未知不标成不适用或原文已核实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:mdm_match_case` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `rule` | 项目明确匹配规则及来源，不假冒TOGAF阈值 | 本地明确规则及来源；匹配规则与跨方案兼容约束按实体类型分别解释，不默认加权评分；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `record_refs` | 各源记录稳定ID | 待匹配的各源主数据记录ID集合；保留来源身份，不提前当作同一黄金记录；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `key_comparison` | 标识与属性比较，保留未知和冲突 | 候选主数据记录的键和属性比较；未知与冲突保留，禁止仅凭相似名称合并；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `proposal` | do-not-merge/manual-review/merge-candidate等候选判断 | 主数据匹配建议；do-not-merge/manual-review/merge-candidate，候选不直接执行合并；类型约束：`{"type":"string","enum":["do-not-merge","manual-review","merge-candidate"]}`（来源：`project-operational-convention`） |
| `matching_basis` | 推理证据 | 主数据匹配推理依据；引用比较结果及规则，评分值本身不是匹配真值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `manual_arbitration` | 谁核对什么再如何处理 | 匹配冲突的人工裁决办法；谁核对哪些证据并如何作决定须明确；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `decision_status` | 候选/已决定等业务状态，非真实批准 | 决定的业务状态；candidate/planned/pending/approved/rejected/unknown，approved另需授权证据；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `merge_lineage` | 源记录/黄金记录/版本及实际或候选操作 | 主数据合并血缘；保留源ID、黄金记录ID、版本和实际或候选操作，必须可追溯回原值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `unmerge_plan` | 恢复ID/原值/版本及消费者关联的方法 | 主数据撤销合并方案；恢复ID、原值、版本及消费者关联，不能只说可回滚；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `historical_policy` | 历史用途与当前真值分离规则 | 历史主数据的保留与解释规则；历史用途和当前真值分离，不能无痕改写；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

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

## 主数据集成风格

- `id`：`mdm-integration-style`
- 英文名：MDM Integration Style
- 决策问题：整合、协作还是集中管理主数据？
- 主责技能：`togaf-information-data`
- 来源：G21B §6.1.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, style, authority, collaboration
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：master_repository
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 比较权威与协作需要
2. 选择整合协作集中风格
3. 明确读写和同步责任
4. 评估演进与迁移

### `master_repository` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `style` | 选定集成风格 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `collaboration` | 协同维护机制 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `consumers` | 服务消费者 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `synchronization` | 同步方向、时效和一致性条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 主数据交换模式

- `id`：`mdm-exchange-pattern`
- 英文名：MDM Exchange Pattern
- 决策问题：主数据交换由哪些应用与责任控制？
- 主责技能：`togaf-information-data`
- 来源：G21B §6.1.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, pattern, authority, producer
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：master_exchange
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 声明 PoA 与 PoC 等来源术语
2. 识别权威提供方与消费方
3. 建模请求更新和通知
4. 核对一致性边界

### `master_exchange` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `pattern` | 交换模式及来源定义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `authority` | 决策或数据权威及授权范围 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `producer` | 数据或消息提供方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `consumer` | 数据或消息消费方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `consistency` | 一致性与时效要求 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `trigger` | 触发事件或判据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## BI 与分析演进架构

- `id`：`bi-transition-architecture`
- 英文名：BI and Analytics Transition Architecture
- 决策问题：如何从现有数仓演进到目标分析平台？
- 主责技能：`togaf-information-data`
- 来源：G238 §3；图3-1–3-4；G238 §3.2.1–3.2.4；G238 表4-2价值链设计、表4-3存储/处理/监控；G238 表4-2高级分析模型工业化、运营平台；表4-3分析模型管理与监控
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, state_id, role, inbound
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：39；对象类型：analytics_component, guide:bi_operating_state, ops:bi_value_chain, ops:bi_model_operations
- 关系类型：traces_to, ops:data_derivation
- 关联交付物：`architecture-definition-document`, `architecture-requirements-specification`

### 分析步骤

1. 描述基线和目标
2. 设计多个可运营过渡
3. 区分入站出站和回写
4. 安排数据及应用迁移依赖
5. 识别旧系统已满足需求与新价值
6. 按可选过渡定义流向/数据语义和消费者
7. 记录每态收益、缺口和可运营条件
8. 退出前逐项验证旧需求与恢复、治理、元数据
9. 从业务决策反推数据和语义
10. 逐层区分原始、技术准备和业务信息转换
11. 记录输入输出及有向派生关系
12. 检查质量、安全、元数据和运营责任贯穿全链
13. 不因价值链存在就认定数据正确/及时
14. 由业务用途明确错误后果和运营责任
15. 选有项目依据的准确性/数据/技术/安全/使用观测
16. 给每指标单位、窗口、证据与阈值来源，未知保持未知
17. 按触发设计停止、人工回退、评审和新版本测试
18. 形成运行监控记录后再评审实际表现

### `analytics_component` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `role` | 承担职责的角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `inbound` | 入站信息流 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `outbound` | 出站信息流 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `storage` | 数据存储责任与位置 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `coexistence` | 新旧状态共存条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:bi_operating_state` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `state_ref` | v2命名状态 | 命名架构状态的稳定引用；baseline/transition/target另填，状态不授予批准；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evolution_kind` | 基线/多个过渡/目标区分 | 架构演进种类；仅baseline/transition/target，与审批和实施状态独立；类型约束：`{"type":"string","enum":["baseline","transition","target"]}`（来源：`project-operational-convention`） |
| `data_flows` | 源→目标及清洗/原始区别 | 各BI态源到目标的数据流；标清清洗后、原始流和元数据，方向不能由排版推出；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `raw_and_metadata` | 原始数据和元数据覆盖 | BI当前态的原始数据和元数据覆盖；区分完整、局部、缺失及来源，不推定已打通；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `consumers` | 逐消费者切换和双供数 | 逐消费者的供数与切换安排；保留旧供数、双供数和验证状态，不以平台已建代替切换；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `incremental_benefit` | 该态的新增业务价值 | BI当前阶段相对前态新增的业务收益；候选价值与已观测收益分开；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `known_gap` | 仍未解决的能力与运营代价 | BI阶段尚存能力或运营缺口；双系统代价与不可运营条件须显式保留；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `operating_exit_gate` | 可运营条件与退出验证 | BI态可运营和旧平台退出条件；授权退役时须结构化accepted、authority、evidence_refs，不以目标态代替验收；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `legacy_requirement_coverage` | 旧需求逐项映射/验证状态 | 逐旧需求ID登记覆盖验证状态；verified才表示已核实，计划、保留旧服务、未知均不支持退役；类型约束：`{"type":"object","minProperties":1,"additionalProperties":{"enum":["verified","verified-in-example","legacy-service-retained","planned","unknown","not-covered","out-of-scope-with-reason"]}}`（来源：`project-operational-convention`） |
| `retirement_authorized` | 是否获得退出依据；与架构状态不同 | 旧BI平台退役授权标志；只能布尔，true还须全部旧用途验证与退出验收，目标态不是授权；类型约束：`{"type":"boolean"}`（来源：`project-operational-convention`） |
| `cost_basis` | 成本的已知/未知依据 | BI阶段成本的项目依据；双份存储不推出总成本翻倍，未计费用须列缺口；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `schedule_basis` | 本地时间依据；指南参考非硬期限 | BI阶段时间安排的项目依据；无工期数据不套用指南中的参考年限；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `ops:bi_value_chain` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `layer_kind` | source/raw/prepared/information/business-view语义 | BI价值链语义层；source/raw/prepared/information/business-view，不是强制物理部署；类型约束：`{"type":"string","enum":["source","raw","prepared","information","business-view"]}`（来源：`project-operational-convention`） |
| `input_refs` | 输入ID/明确外部来源 | 本数据价值链层的输入ID；外部输入注明出处，不能凭连线猜数据来源；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |
| `transformation_rule` | 技术/业务/语义规则及版本 | 价值链层的技术、业务或语义转换规则及版本；保持输入输出粒度和失败处理；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `business_purpose` | 该层服务用途 | 本数据价值链层服务的业务用途；不能仅写存储产品或技术动作；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `owner` | 业务或技术责任 | 本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `quality_controls` | 质量和失败处理 | BI层质量校验与失败处理；说明规则、阈值来源和不合格流向；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `protection_controls` | 访问、隐私与保留规则 | BI层访问、隐私和保留控制；写明责任与用途限制，不默认公开或无限保留；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `metadata_lineage` | 数据/规则/作业/用途血缘 | 数据、规则、作业与业务用途的元数据血缘；保留方向和版本，不当作系统部署链；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `scope` | 数据和时点范围 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `reference_identity` | 项目裁剪，非强制部署模式 | 参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 访谈/规则/试验定位 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `ops:bi_model_operations` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `model_ref` | 模型与版本 | 分析模型与版本引用；同名不同版本分开，模型存在不等于已发布运行；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `business_use` | 用途及人工/自动决策边界 | 分析模型服务的业务决策与消费者；注明人工建议或自动执行边界；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `lifecycle` | 生命周期、技术/业务责任和发布证据 | 用途或模型从设计到维护的生命周期；列业务和技术责任，发布计划不能当实际运行；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `measure` | 单位/时间/定义/依据/阈值/观测值 | 模型运营度量定义；列单位、时间窗、阈值来源、观测与缺测，未给阈值不授予通过；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `data_quality` | 样本与生产数据语义/质量 | 模型训练与生产数据的质量及语义；样本、时间窗和缺测分开记录；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `monitoring` | 准确性/漂移/技术/安全/使用多个关注点 | 分析模型监控安排；覆盖准确性、漂移、技术、安全与使用信号，并注明缺口；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `response` | 触发/负责人/回退/再训练控制 | 接口返回结果与异常语义；区分成功、失败和补偿，不默认所有调用成功；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `lineage` | 数据特征模型消费与观测追溯 | 数据、特征、模型、消费者和观测的血缘；区分版本，不能仅用名称串联；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 项目监控约定与试验证据 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `claim` | 已测结果与候选方案分开 | 分析模型结果主张；已测、计划和假设分开，示例试验不冒充生产价值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（2）：`name`、`state_id`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

---

合计 17 个工作产品，193 个字段。
