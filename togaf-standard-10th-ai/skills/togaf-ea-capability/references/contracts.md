# togaf-ea-capability 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 架构成熟度模型

- `id`：`architecture-maturity-model`
- 英文名：Architecture Maturity Model
- 决策问题：用什么可解释标准评价 EA 能力？
- 主责技能：`togaf-ea-capability`
- 来源：G203 §2.1–2.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, element, level, description
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：criterion, maturity_criterion, maturity_element
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 声明选定模型和适用范围
2. 定义要素与级别特征
3. 规定证据及权重
4. 校准评审者理解

本工作产品未声明 `required_attributes`；其字段约束须由 owner 补齐后才能机器校验。

其余字段（6）：`name`、`element`、`level`、`description`、`evidence_rule`、`weight`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 架构成熟度评分卡

- `id`：`architecture-maturity-scorecard`
- 英文名：Architecture Maturity Scorecard
- 决策问题：当前 EA 实践达到哪些成熟度特征？
- 主责技能：`togaf-ea-capability`
- 来源：G203 §2.2–2.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, element, level, evidence
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：maturity_observation
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 按要素获取证据
2. 逐特征评价达成
3. 记录争议和未知
4. 分别报告加权级别与逐级达成比例

### `maturity_observation` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `element` | 成熟度要素 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `level` | 所用模型下的层级 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `assessment_date` | 评估日期 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `assessor` | 评价人或评价角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `confidence` | 判断可信度及理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `assessment_result` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `subject_ref` | 评估对象的稳定引用 | 评估对象的稳定引用；与范围、方法和期间一起确定结果适用对象；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `method_ref` | 评估结果采用的方法引用 | 评估结果采用的方法引用；与评分口径及版本可定位关联；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `result_value` | 评估结果值及尺度 | 评估结果值及尺度；原始分项与聚合分开，无方法依据不得算总分；类型约束：`{"anyOf":[{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]},{"type":"number"}]}`（来源：`project-operational-convention`） |
| `unit` | 评估结果的单位或量表标识 | 评估结果的单位或量表标识；不可将不同单位结果直接相加；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `period` | 结果或核算记录的时间窗 | 结果或核算记录的时间窗；注明起止、周期口径，不混合不同期间的值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数字技术采用定位

- `id`：`digital-adoption-position`
- 英文名：Digital Adoption Position
- 决策问题：选择怎样的数字技术采用方式？
- 主责技能：`togaf-ea-capability`
- 来源：G212 §5.1；图5-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, ubiquity, velocity, rationale
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：adoption_option
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 明确普及度与采用速度
2. 比较 ABCD 四种方式
3. 阐明选择理由和范围
4. 与就绪度结果结合

### `adoption_option` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `ubiquity` | 数字技术采用的普及广度 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `velocity` | 数字技术采用的速度 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rationale` | 分析或选择的理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `tradeoffs` | 已考虑的权衡 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数字技术就绪度问卷

- `id`：`digital-readiness-questionnaire`
- 英文名：Digital Readiness Questionnaire
- 决策问题：如何取得可比较的就绪度观察？
- 主责技能：`togaf-ea-capability`
- 来源：G212 §5.2、附录A
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, factor, category, statement
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：readiness_question
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 按因素选择问题
2. 声明七级李克特锚点
3. 邀请关键领导者作答并讨论共识
4. 保留原始答复与证据

### `readiness_question` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `factor` | 就绪度因素 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `category` | 所声明分类体系下的分类 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `statement` | 原子陈述或问题 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scale_anchor` | 量表级别的含义 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `respondent` | 问卷回答者或角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 数字技术就绪度评估

- `id`：`digital-readiness-assessment`
- 英文名：Digital Readiness Assessment
- 决策问题：哪些采用因素需要管理关注？
- 主责技能：`togaf-ea-capability`
- 来源：G212 §5.2–5.4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, category, question_ids, rating
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：readiness_factor
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 逐因素汇总有依据的问卷结果
2. 按来源规则识别关注因素
3. 分析其主要后果
4. 形成改进建议

### `readiness_factor` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `category` | 所声明分类体系下的分类 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `question_ids` | 参与评价的问题标识 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rating` | 声明量表下的评价值 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `anchor` | 评价值对应的量表锚点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `attention` | 需要管理关注的原因 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 就绪度因素后果分析

- `id`：`readiness-consequence-analysis`
- 英文名：Readiness Consequence Analysis
- 决策问题：缺失因素会如何影响采用结果？
- 主责技能：`togaf-ea-capability`
- 来源：G212 §5.3；图5-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, factor, primary_consequence, business_effect
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：consequence, readiness_consequence, readiness_factor
- 关系类型：has_consequence, traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 识别不足因素
2. 对照其主要后果
3. 分析多个后果相互作用
4. 指定管理行动及责任

本工作产品未声明 `required_attributes`；其字段约束须由 owner 补齐后才能机器校验。

其余字段（6）：`name`、`factor`、`primary_consequence`、`business_effect`、`owner`、`action`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 采用因素递进路线

- `id`：`adoption-factor-progression`
- 英文名：Adoption Factor Progression
- 决策问题：怎样逐步补齐采用短板？
- 主责技能：`togaf-ea-capability`
- 来源：G212 §5.4；图5-4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, factor_category, prerequisite, action
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：6；对象类型：readiness_factor, assessment_result
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 依据问卷及特征证据识别基础、影响、持续因素短板
2. 保留三层前置语义及类型1/2/3的定性定义
3. 将项目分类与原始证据绑定；证据不足保留待评估
4. 将补齐短板的具体行动追溯至因素；日期与依赖另建工作包路线图

### `readiness_factor` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `factor_category` | 基础、影响或持续因素分类 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `prerequisite` | 可执行该项的前置条件 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `action` | 拟采取的具体行动 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `readiness_evidence` | 就绪条件的证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `assessment_result` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `organization_type` | 采用就绪类型1/2/3；解释性类别，表示满足列明因素层，不是实施步骤或已批准企业评定 | 整数1、2或3；类型1仅基础层，类型2基础与影响，类型3三层均满足。不得把类型当成项目阶段。；类型约束：`{"type":"integer","enum":[1,2,3]}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `fulfilled_layers` | 该评估情形已声明满足的因素层 | 数组，元素仅限 foundational/impact/sustaining；须与 organization_type 的层定义一致，不能由射线长度推断。；类型约束：`{"type":"array","minItems":1,"items":{"type":"string","enum":["foundational","impact","sustaining"]}}`（来源：`project-operational-convention-guided-by-cited-source`） |
| `interpretation` | 评估结果的业务解释与排除边界 | 非空文字，须说明不是项目步骤、分数或已批准评定。；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（2）：`name`、`state_id`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 企业架构服务目录

- `id`：`ea-service-catalog`
- 英文名：Enterprise Architecture Service Catalog
- 决策问题：EA 团队应提供哪些决策支持服务？
- 主责技能：`togaf-ea-capability`
- 来源：G217 附录B–C；G217 §4.4.1–4.4.5，图4-3；G217 附录C.1–C.7、附录D
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, consumer, decision, output
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：19；对象类型：ea_service, guide:ea_service_context, guide:ea_adm_mapping
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 选择候选服务
2. 明确消费者决策和成果
3. 映射 ADM 与能力
4. 核对团队容量与服务约定
5. 按服务梳理首次出现与后续范围
6. N只用于首次引入，P表示沿用，D要求明确新增深度
7. 记录项目证据与原图证据两个状态，不混称相同
8. 先明确服务输出与消费者决策
9. 由项目活动确定使用阶段
10. 分别登记来源映射和项目映射
11. 未知原图格不推断不适用或唯一阶段

### `ea_service` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `consumer` | 数据或消息消费方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `decision` | 决策结果、理由和状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `output` | 活动输出 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `adm_phase` | 适用 ADM 阶段 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `service_level` | 服务水准与度量 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `guide:ea_service_context` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `service` | 同一稳定服务名/ID | EA服务目录稳定ID或完整名称；跨语境同服务保持身份，不由名称推定资源已就绪；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `context` | 四DPBoK语境，不是成熟度评分 | 服务的DPBoK组织语境；独立于成熟度、审批状态和TOGAF架构域；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `emergence` | N/P/D或本地明确未引入 | EA服务在语境中的出现或加深；N首次/P此前/D加深，未引入另明确记录；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `meaning` | N首次/P此前/D加深 | EA服务N/P/D符号的解释；N首次/P此前/D加深，不解释为成熟度分数；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `local_depth` | D必须说明增加何种活动/范围 | EA服务在D语境增加的活动或范围；不能仅重复“加深”而无本地说明；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 项目服务演进证据 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `mapping_origin` | 项目裁剪或来源逐格转录必须区分 | 映射来源身份；区分project-observation/project-proposal/source-verified，后者须独立原文核实；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `source_cell_status` | 原图对应格核实状态 | 原图对应单元格核实状态；本地服务演进观察不能让来源格自动变成已核实；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `resources` | 交付服务所需责任/容量及缺口 | 交付EA服务所需责任、技能、容量和未满足资源；目录存在不等于可交付；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `guide:ea_adm_mapping` 必填字段（8）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `service` | 服务目录项 | EA服务目录稳定ID或完整名称；跨语境同服务保持身份，不由名称推定资源已就绪；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `ADM_phase` | 项目使用阶段，可多记录而非唯一归属 | ADM阶段标识；同一服务可跨阶段，项目支持活动不宣称原图唯一归属；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |
| `project_activity` | 服务在该阶段支持的活动 | EA服务在指定ADM阶段支持的本地活动；项目观察不能冒充来源图唯一映射；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `output` | 活动输出 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `mapping_origin` | project-observation/project-proposal/source-verified区分 | 映射来源身份；区分project-observation/project-proposal/source-verified，后者须独立原文核实；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 项目或来源定位 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `source_mapping` | 原图映射核实结果；未知不填不适用 | 来源参考态或原图映射与本地裁剪的对应；未知不标成不适用或原文已核实；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## EA 与企业价值地图

- `id`：`ea-value-map`
- 英文名：EA Value Map
- 决策问题：EA 服务如何为企业创造价值？
- 主责技能：`togaf-ea-capability`
- 来源：G184 §13
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, service, consumer, business_outcome
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：ea_value, goal
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 明确 EA 服务和业务受益者
2. 建立贡献假设
3. 选择度量与反馈
4. 检查业务周期对齐

### `ea_value` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `service` | 服务对象引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `consumer` | 数据或消息消费方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `business_outcome` | 企业业务成果 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `measure` | 衡量贡献的指标 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `contribution` | 贡献解释或假设 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## EA 团队容量计划

- `id`：`ea-team-capacity-plan`
- 英文名：EA Team Capacity Plan
- 决策问题：团队容量能否支撑所选架构服务？
- 主责技能：`togaf-ea-capability`
- 来源：G184 §13
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, role, skill, demand
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：ea_capacity
- 关系类型：traces_to
- 关联交付物：`organization-model`, `tailored-architecture-framework`, `capability-assessment`

### 分析步骤

1. 估计服务需求与参与节奏
2. 盘点角色技能和可用量
3. 比较供需
4. 安排招聘发展或裁剪

### `ea_capacity` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `role` | 承担职责的角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `skill` | 技能项或类别 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `demand` | 指定期间的资源需求 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `availability` | 指定期间可用资源 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `allocation` | 资源分配 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
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

## 企业框架接触与承诺目录

- `id`：`enterprise-framework-alignment-catalog`
- 英文名：Enterprise Framework Alignment Catalog
- 决策问题：EA应融入哪些已在使用的框架，在哪些接触点补位？
- 主责技能：`togaf-ea-capability`
- 来源：G184 §7.1–7.2、§10.1、§13.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围和五维语境, 原始访谈/计划/测量及定位, 授权角色和适用目标版本
- 可选输入：既有模型、视图、参考规范和组织规则
- 缺输入策略：逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。
- 字段总数：11；对象类型：guide:framework_touchpoint
- 关系类型：未声明
- 关联交付物：`tailored-architecture-framework`, `organization-model`

### 分析步骤

1. 识别企业实际规划/执行/治理方法、版本与负责人
2. 查批准、资源和连续使用记录区分口头承诺
3. 按成果与信息交接映射接触点
4. 识别已有成果复用、重叠和缺口
5. 协商责任/时点/格式并更新EA路线

### `guide:framework_touchpoint` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `framework` | 框架/企业既有方法及版本 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `focus` | 规划、执行、治理等关注领域 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `commitment_evidence` | 实际使用记录而非口头声明 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `actual_commitment` | 证据支持的采用情况，不使用无依据分数 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `owner` | 流程负责人 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `touchpoint` | 双向接触事件及时点 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `ea_input` | EA消费的信息 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `ea_output` | EA交付的信息 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `gap` | 重叠/缺口 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `action` | 融入或补位动作 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

### 关系语义

表内ID字段提供显式引用；同名或相邻不代表语义关系。无建模关系时不伪造traces_to。

## 业务周期与工作产品时点

- `id`：`business-cycle-product-alignment`
- 英文名：Business Cycle Product Alignment
- 决策问题：架构工作产品何时必须可用以影响业务决定？
- 主责技能：`togaf-ea-capability`
- 来源：G184 §4.3.2、§10.3、§11.4；G186 §4、§8.1、§11.2、§14
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围和五维语境, 原始访谈/计划/测量及定位, 授权角色和适用目标版本
- 可选输入：既有模型、视图、参考规范和组织规则
- 缺输入策略：逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。
- 字段总数：12；对象类型：guide:cycle_product
- 关系类型：未声明
- 关联交付物：`statement-of-work`, `implementation-migration-plan`

### 分析步骤

1. 访谈消费方确认业务事件、决定和最迟输入日期
2. 将目的与所需工作产品/实际视图绑定
3. 以输入依赖倒排完成与评审
4. 比较计划/实际和消费期限，指出错过决策的后果
5. 重排范围资源或显式告知未满足条件，不改原业务事实

### `guide:cycle_product` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_event` | 业务/预算/发布/运营事件 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision` | 该事件需要作出的决定 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `consumer` | 消费架构成果的责任人 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `required_by` | 消费方需要日期 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `planned` | 计划提供日期 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `actual` | 实际交付日期或未知 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `product_view_refs` | 具体工作产品及view_id | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `dependency` | 前置输入/工作 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `status` | 准时/迟到/未知 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `recovery_action` | 晚交付时如何修正或披露决策缺口 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `rule_source` | 项目日历与日期依据 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

### 关系语义

表内ID字段提供显式引用；同名或相邻不代表语义关系。无建模关系时不伪造traces_to。

## 价值实现评估

- `id`：`value-realization-assessment`
- 英文名：Value Realization Assessment
- 决策问题：目标价值是否实际实现，差距是否需要H阶段发起新工作？
- 主责技能：`togaf-ea-capability`
- 来源：G184 §10.1.7、§10.1.9、§11.4；G186 §8.7、§10.4、§14、§15.2.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围和五维语境, 原始访谈/计划/测量及定位, 授权角色和适用目标版本
- 可选输入：既有模型、视图、参考规范和组织规则
- 缺输入策略：逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。
- 字段总数：17；对象类型：guide:value_observation
- 关系类型：未声明
- 关联交付物：`compliance-assessment`, `change-request`, `implementation-migration-plan`

### 分析步骤

1. 明确价值主张、接收方、责任人与观察期间
2. 锁定同范围同单位的基线/目标和计算依据
3. 收集运营实际及证据，识别同时发生变化
4. 逐指标比较目标差距并解释不确定性与归因限制
5. 由组合/运营持续复评，必要时创建H变更/新工作请求

### `guide:value_observation` 必填字段（16）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `target_ref` | 目标/价值主张及版本 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `beneficiary` | 价值接收方 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `baseline` | 基线值 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `expected` | 目标值及期望改善 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `observed` | 实际值及证据 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `unit` | 带方向的单位/量表 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `periods` | 基线与实际期间 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `scope` | 比较范围及业务量 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `method` | 同口径测量方法 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `calculation_basis` | 明确声明的比较规则及计算 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `finding` | 已达/未达/待测；不得把合规当收益 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `confounders` | 同时变化的非架构因素 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `attribution` | 归因是否证实 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `owner` | 组合/运营价值责任人 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `next_review` | 下次价值复评 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `compliance_link` | G实施合规引用与其证明边界 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

### 关系语义

表内ID字段提供显式引用；同名或相邻不代表语义关系。无建模关系时不伪造traces_to。

## 项目经验记录与教训报告

- `id`：`project-learning-record`
- 英文名：Project Learning Record
- 决策问题：哪些观察应成为后续项目和EA能力改进的输入？
- 主责技能：`togaf-ea-capability`
- 来源：G188 §3.1.3、§3.6.3示例3-37及注释2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：13；对象类型：guide:project_learning
- 关系类型：未声明
- 关联交付物：`change-request`, `architecture-repository`

### 分析步骤

1. 持续日志从以往经验和本项目观察开始
2. AAR分别记录预期/实际/原因/改进
3. 区别证据支持原因与待验证假设
4. 收尾筛选关键教训并指定改进责任与验证
5. 将可执行能力改进形成H变更请求并向后续项目传递

### `guide:project_learning` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `record_kind` | ongoing-log或final-lessons-report | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `expected` | 当初计划或假设 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `actual` | 实际观察 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `difference` | 具体差异，不把因果当事实 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `cause_hypothesis` | 已证实原因或待验证假设 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID/访谈/记录 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `impact` | 对项目的实际影响 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `recommendation` | 下一项目可执行改进 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `owner` | 负责采取改进的人 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `verification` | 如何验证建议有效 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `status` | 观察/原因待证/建议待试点等 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `follow_up_reference` | 能力变更请求或后续项目引用 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

## 数字可持续性能力评估

- `id`：`sustainability-capability-assessment`
- 英文名：Sustainability Capability Assessment
- 决策问题：企业可持续ICT能力有哪些具体强项、缺口和改进？
- 主责技能：`togaf-ea-capability`
- 来源：G242 §3.2、§5.2表5-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：组织、服务、业务用途及所评估期间/生命周期边界, 原始访谈、使用数据、供应商记录及稳定证据ID, 适用目标、职责和组织自定决策规则；未知项显式登记
- 可选输入：历史评估、环境数据目录、采购契约及角色技能资料
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：11；对象类型：guide:sustainability_capability
- 关系类型：未声明
- 关联交付物：`capability-assessment`, `tailored-architecture-framework`

### 分析步骤

1. 按六维访谈并核查已开展活动
2. 以七高层功能/35详细功能作非穷尽检查参照，按范围裁剪
3. 区分缺证、未开展和有效执行
4. 只有项目选择成熟度模型后才评分，公开规则来源
5. 把缺口转为有责任和验收依据的改进

### `guide:sustainability_capability` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `dimension` | G242六维之一 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `reference_functions` | 关联的七功能组/详细功能；多对多 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `current_evidence` | 已做/未证/部分开展的事实 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `target_need` | 组织实际需要 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `gap` | 当前与需要之间的具体缺口 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `action` | 改进动作 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `owner` | 责任人 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `assessment_rule` | 定性或已选成熟度规则及出处 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `rating` | 未选规则时not-scored | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 原始材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

用途—应用/数据—基础设施用稳定ID追踪；评估维度与功能多对多关联；总额与子集、两种Scope2基础、抵消和复制存储分别表达。表格相邻不代表因果或可相加。

## EA观点文件与影响经营登记

- `id`：`ea-point-of-view-register`
- 英文名：EA Point-of-View Document and Influence Register
- 决策问题：外部生态变化要求什么转型，EA建议如何被阅读、讨论并关联到后续变更？
- 主责技能：`togaf-ea-capability`
- 来源：G184 §12.2–12.4；本地L1351–1373
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "charter_alignment", "meaning": "EA章程目的与本主张的关联", "origin": "source-purpose-plus-project-contract"}, {"id": "ecosystem_change", "meaning": "外部生态信号及来源", "origin": "source-purpose-plus-project-contract"}, {"id": "decision_question", "meaning": "决策者要回答的问题", "origin": "source-purpose-plus-project-contract"}, {"id": "position", "meaning": "有理由的主张，不是建模视角规范", "origin": "source-purpose-plus-project-contract"}, {"id": "rationale", "meaning": "回应未来需求、文化与权衡的论据", "origin": "source-purpose-plus-project-contract"}, {"id": "alternatives", "meaning": "候选方案及各自影响和取舍", "origin": "source-purpose-plus-project-contract"}, {"id": "recommendation", "meaning": "待决策的转型建议", "origin": "source-purpose-plus-project-contract"}, {"id": "adoption_timing", "meaning": "从热潮到需要的时间判断及证据", "origin": "source-purpose-plus-project-contract"}, {"id": "cost_risk_tradeoff", "meaning": "采用成本与失败风险的条件性比较", "origin": "source-purpose-plus-project-contract"}, {"id": "audience_ids", "meaning": "目标利益相关者稳定标识", "origin": "source-purpose-plus-project-contract"}, {"id": "document_version", "meaning": "被阅读或修订的观点版本", "origin": "source-purpose-plus-project-contract"}, {"id": "reading_events", "meaning": "有时间、版本、读者和来源的实际阅读观察", "origin": "source-purpose-plus-project-contract"}, {"id": "initiated_changes", "meaning": "后续变更、发起人、证据及关联，不推断因果", "origin": "source-purpose-plus-project-contract"}, {"id": "follow_up", "meaning": "负责人、复评期限与下一步", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：不足时保留带ID草案与needs-input；未知容差不设默认值，缺实际阅读/验收证据不声称已阅读/完成。冲突、重复ID和未经批准覆盖基线属于错误。
- 字段总数：17；对象类型：guide:ea-point-of-view
- 关系类型：未声明
- 关联交付物：`organization-model`, `architecture-vision`

### 分析步骤

1. 从章程与外部生态原料提炼决策问题和时间窗口
2. 提出有理由的主张、备选方案及影响和成本/失败风险权衡
3. 形成面向明确受众的观点文件与建议清单
4. 分别登记分发、实际阅读及文档版本
5. 跟踪阅读者发起的变更并核实归属，保留因果限制
6. 修订观点后分别报告旧版阅读与新版反馈缺口

### `guide:ea-point-of-view` 必填字段（16）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `charter_alignment` | EA章程目的与本主张的关联 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `ecosystem_change` | 外部生态信号及来源 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `decision_question` | 决策者要回答的问题 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `position` | 有理由的主张，不是建模视角规范 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `rationale` | 回应未来需求、文化与权衡的论据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `alternatives` | 候选方案及各自影响和取舍 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `recommendation` | 待决策的转型建议 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `adoption_timing` | 从热潮到需要的时间判断及证据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `cost_risk_tradeoff` | 采用成本与失败风险的条件性比较 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `audience_ids` | 目标利益相关者稳定标识 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `document_version` | 被阅读或修订的观点版本 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `reading_events` | 有时间、版本、读者和来源的实际阅读观察 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `initiated_changes` | 后续变更、发起人、证据及关联，不推断因果 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `follow_up` | 负责人、复评期限与下一步 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-purpose-plus-explicit-project-operational-field`） |
| `analysis_result` | 确定性审查结果与带ID缺口 | 确定性审查结果与带ID缺口；由本方法明确输入重算，输出存在不等于治理批准；类型约束：`{"type":"object","minProperties":1}`（来源：`project-operational-convention`） |
| `raw_material_refs` | 完整原始业务材料ID列表 | 完整原始业务材料ID列表；须能检索随包原料，不以分析结果循环充当业务事实；类型约束：`{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

## 架构存储库结构

- `id`：`architecture-repository-structure`
- 英文名：架构存储库结构
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/fig5-1
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：repository_asset, repository_container, repository_external, repository_partition
- 关系类型：project:adopts, project:contains, project:delivers_outcomes, project:enables, project:governs, project:steers, project:structured_by, project:visibility_escalation
- 关联交付物：`architecture-repository`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## 架构全景投影

- `id`：`architecture-landscape-projection`
- 英文名：架构全景投影
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/fig3-1；G186/fig3-2
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：capability, landscape_dimension, landscape_projection, landscape_slice
- 关系类型：project:contains, project:projects_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## 存储库状态与视图树

- `id`：`repository-state-view-tree`
- 英文名：存储库状态与视图树
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/fig5-2
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：g186:repository_node
- 关系类型：g186:contains
- 关联交付物：`architecture-repository`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## 存储库并行候选容器

- `id`：`repository-parallel-candidates`
- 英文名：存储库并行候选容器
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/fig5-3
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：g186:repository_node
- 关系类型：g186:contains
- 关联交付物：`architecture-repository`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## 能力与项目连续谱

- `id`：`capability-project-continuum`
- 英文名：能力与项目连续谱
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/fig8-1
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：g186:continuum, g186:continuum_label
- 关系类型：未声明
- 关联交付物：`architecture-vision`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## 组合利益相关者×关注点矩阵

- `id`：`portfolio-stakeholder-concern-matrix`
- 英文名：组合利益相关者×关注点矩阵
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/tabB-1
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：g186:concern, g186:stakeholder
- 关系类型：g186:responsibility
- 关联交付物：`communications-plan`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## 存储库版本比较 Target → Baseline

- `id`：`repository-target-baseline-comparison`
- 英文名：存储库版本比较 Target → Baseline
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-ea-capability`
- 来源：G186/fig13-1
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：g186:comparison_item, g186:repository_snapshot
- 关系类型：g186:compares_from, g186:compares_to
- 关联交付物：`requirements-impact-assessment`, `architecture-repository`

### 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

### `*` 必填字段（1）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `definition` | 对象在本视点中的可检查定义 | 使用可追溯描述；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`evidence`、`certainty`

### 输出

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

## DTRA因素与ADM阶段对齐

- `id`：`dtra-adm-phase-alignment`
- 英文名：DTRA Factor to ADM Phase Alignment
- 决策问题：DTRA结果在每个ADM阶段意味着什么，各阶段考虑了哪些因素，低分因素如何处理？
- 主责技能：`togaf-ea-capability`
- 来源：G212 §6、表6-1、图6-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "assessment_ref", "meaning": "DTRA评估引用", "origin": "source-purpose-plus-project-contract"}, {"id": "initiated_in_phase", "meaning": "DTRA启动阶段", "origin": "source-purpose-plus-project-contract"}, {"id": "factor_ratings", "meaning": "15因素1-7评分（G212 表A-1）", "origin": "source-purpose-plus-project-contract"}, {"id": "reassessment", "meaning": "复评时点：end-of-cycle或next-vision", "origin": "source-purpose-plus-project-contract"}, {"id": "phase", "meaning": "ADM阶段", "origin": "source-purpose-plus-project-contract"}, {"id": "implication", "meaning": "该阶段对数字采用的含义（表6-1）", "origin": "source-purpose-plus-project-contract"}, {"id": "actions", "meaning": "行动及其针对的因素ID", "origin": "source-purpose-plus-project-contract"}, {"id": "progression_note", "meaning": "基础因素未满足时的递进安排", "origin": "source-purpose-plus-project-contract"}, {"id": "deferred_factors", "meaning": "有理由延后处理的因素", "origin": "source-purpose-plus-project-contract"}, {"id": "considered_factor_ids", "meaning": "本阶段考虑的DTRA因素", "origin": "source-purpose-plus-project-contract"}, {"id": "tailored_out", "meaning": "被裁剪的区域因素及理由", "origin": "source-purpose-plus-project-contract"}, {"id": "governance_distinction", "meaning": "阶段G治理与“治理与合规”因素的区别说明", "origin": "source-purpose-plus-project-contract"}, {"id": "requirement_changes", "meaning": "由偏好变化引起的需求变更及影响评估引用", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：14；对象类型：guide:dtra-alignment-summary, guide:dtra-phase-record
- 关系类型：未声明
- 关联交付物：`capability-assessment`, `architecture-vision`

### 分析步骤

1. 在阶段A启动DTRA并引用评估结果
2. 按表6-1记录各阶段含义与行动
3. 对照图6-1区域考虑各阶段因素，或记录裁剪
4. 评分低于“同意”的因素安排行动或有理由延后
5. 基础因素未满足时说明递进安排
6. 需求变更经影响评估在下一周期实施
7. 在周期结束或下一周期愿景阶段复评

### `guide:dtra-alignment-summary` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `assessment_ref` | DTRA评估引用 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `initiated_in_phase` | DTRA启动阶段 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `factor_ratings` | 15因素1-7评分（G212 表A-1） | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `reassessment` | 复评时点：end-of-cycle或next-vision | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

### `guide:dtra-phase-record` 必填字段（3）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `phase` | ADM阶段 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `implication` | 该阶段对数字采用的含义（表6-1） | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `actions` | 行动及其针对的因素ID | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（7）：`name`、`progression_note`、`deferred_factors`、`considered_factor_ids`、`tailored_out`、`governance_distinction`、`requirement_changes`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 24 个工作产品，201 个字段。
