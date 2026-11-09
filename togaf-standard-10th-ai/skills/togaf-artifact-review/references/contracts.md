# togaf-artifact-review 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 架构成果验收准则

- `id`：`architecture-acceptance-criteria`
- 英文名：Architecture Acceptance Criteria
- 决策问题：怎样判断架构成果足以支持决策？
- 主责技能：`togaf-artifact-review`
- 来源：G188 §3.1–3.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, deliverable, criterion, verification
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：acceptance_criterion
- 关系类型：traces_to
- 关联交付物：`compliance-assessment`

### 分析步骤

1. 从目标与关注点定义准则
2. 指定检验和评审责任
3. 记录证据及未决项
4. 区分移交批准和生成完成

### `acceptance_criterion` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `deliverable` | 架构交付物引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `criterion` | 单项判断准则 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `verification` | 验证方法与验收证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `reviewer` | 评审责任人或角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `status` | 该条记录的工作状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 可持续性架构评审画布

- `id`：`sustainability-review-canvas`
- 英文名：Sustainability Architecture Review Canvas
- 决策问题：方案的环境贡献与措施是否一致？
- 主责技能：`togaf-artifact-review`
- 来源：G242 §3.8–3.9；图3-14
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_contribution, year, scope
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：9；对象类型：sustainability_action
- 关系类型：traces_to
- 关联交付物：`compliance-assessment`

### 分析步骤

1. 说明三类业务环境贡献
2. 分别记录新增退役净值
3. 评价措施与选择理由
4. 核对印刷或计算差异

### `sustainability_action` 必填字段（8）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_contribution` | 业务对环境目标的贡献类型 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `year` | 环境核算年度 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `increase` | 新增环境影响 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `decrease` | 退役或减少的环境影响 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `net` | 同一边界下的净影响 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `selection` | 措施或选项的选择状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rationale` | 分析或选择的理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 视角库

- `id`：`viewpoint-library`
- 英文名：Viewpoint Library
- 决策问题：为完整利益相关者关注点选择哪些可复用构图规范？
- 主责技能：`togaf-artifact-review`
- 来源：G184 §8.2–8.4；G186 §6.3.1、§9.1.3、附录C表C-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围和五维语境, 原始访谈/计划/测量及定位, 授权角色和适用目标版本
- 可选输入：既有模型、视图、参考规范和组织规则
- 缺输入策略：逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。
- 字段总数：10；对象类型：guide:viewpoint
- 关系类型：未声明
- 关联交付物：`tailored-architecture-framework`, `architecture-repository`

### 分析步骤

1. 从业务原话区分关注点、决策与角色
2. 明确每组问题需要哪些信息并查模型缺口
3. 定义构造规则、筛选范围与状态
4. 关联profile_id和多个实际view_id，检查关注点覆盖
5. 缺信息单列，不以已有图名代替分析

### `guide:viewpoint` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `concern` | 标准关注点 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `stakeholders` | 拥有架构决策权的利益相关者 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision` | 待支持的业务决定 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `construction` | 可重复构造视图的方法和筛选规则 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `required_information` | 必需对象、关系、属性、单位等 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `source_models` | 模型/版本引用 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `view_ids` | 实际视图实例ID；视角不是视图 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `gaps` | 缺信息及其影响 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `selection_reason` | 为何覆盖这组关注点 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

### 关系语义

表内ID字段提供显式引用；同名或相邻不代表语义关系。无建模关系时不伪造traces_to。

## 架构治理检查清单

- `id`：`architecture-governance-checklist`
- 英文名：Architecture Governance Checklist
- 决策问题：目标能否批准，实施是否合理遵循目标且如何处理偏差？
- 主责技能：`togaf-artifact-review`
- 来源：G184 §6.2；G186 §15.2.1表15-1、§15.2.2表15-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围和五维语境, 原始访谈/计划/测量及定位, 授权角色和适用目标版本
- 可选输入：既有模型、视图、参考规范和组织规则
- 缺输入策略：逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。
- 字段总数：10；对象类型：guide:governance_check
- 关系类型：未声明
- 关联交付物：`compliance-assessment`, `architecture-contract`, `implementation-governance-model`
- `implementation-governance-model`适用边界：项目路由：F阶段在适用时（if any）准备实施治理模型；G阶段使用其检查点、决策权和升级规则进行实施治理。关联工作产品不自动创建必需交付物、不代替适用性裁剪或真实授权。

### 分析步骤

1. 区分目标开发与实施变更两类治理对象
2. 锁定对象版本、上层约束、原价值口径和角色权利
3. 按来源顺序执行检查并引用证据
4. 目标任一否/未知先补足；实施Q1为是时接受合理解释
5. 不合规转影响评估和处置，批准不能由生成器或审计员代行

### `guide:governance_check` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `subject` | 受评对象及精确版本 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `sequence` | 来源规定的检查顺序 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `question` | 检查问题 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `answer` | yes/no/unknown/not-reached；后两者是项目缺口约定 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 对应原料和模型/视图证据 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `accountable_role` | 责任角色及决策权 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `next_action` | 按本问题分支采取的动作 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `result` | 本案例整体结论；不代表真实批准 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `source_variant` | 使用的指南和差异说明 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

### 关系语义

表内ID字段提供显式引用；同名或相邻不代表语义关系。无建模关系时不伪造traces_to。

## 不合规影响与处置登记

- `id`：`non-compliance-disposition`
- 英文名：Non Compliance Disposition
- 决策问题：对已证实偏差应强制执行、临时豁免还是重审目标？
- 主责技能：`togaf-artifact-review`
- 来源：G186 §15.2.2表15-2；G184 §6.2、§6.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围和五维语境, 原始访谈/计划/测量及定位, 授权角色和适用目标版本
- 可选输入：既有模型、视图、参考规范和组织规则
- 缺输入策略：逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。
- 字段总数：14；对象类型：guide:noncompliance_disposition
- 关系类型：未声明
- 关联交付物：`compliance-assessment`, `change-request`, `architecture-contract`

### 分析步骤

1. 核对目标约束是否确被违反而非实现偏好不同
2. 按开发目标时同一价值/风险口径分析影响
3. 请SME核实事实、列出三种处置及取舍
4. 向授权利益相关者提交建议，记录其决定
5. 临时豁免设置期限、复评责任与日期；执行需纠偏证据；改目标重走目标批准

### `guide:noncompliance_disposition` 必填字段（13）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `subject` | 实施对象与目标版本 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `violated_spec` | 违反的规格ID | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `original_value_basis` | 与批准目标一致的范围/期间/量测方法 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 偏差证据 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `impact` | 价值、风险和置信度影响 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `options` | 执行、临时豁免、变更目标三个选项及影响 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `recommendation` | 架构师候选建议 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision_owner` | 授权利益相关者 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision` | 已决定或待决定；与建议分开 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `expiry` | 临时豁免有效期 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `review_date` | 复评日 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `review_owner` | 复评责任人 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `follow_up` | 纠偏/复评/目标重批及其证据 | 值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

### 关系语义

表内ID字段提供显式引用；同名或相邻不代表语义关系。无建模关系时不伪造traces_to。

## 架构描述充分性与正式度评审

- `id`：`architecture-description-formality-review`
- 英文名：Architecture Description Sufficiency and Formality Review
- 决策问题：当前描述是否足以支持指定决策，表达与治理控制是否适合当前目的？
- 主责技能：`togaf-artifact-review`
- 来源：G217 §2.4（图2-1为方法示意）
- 定义状态：`guide-body-located-with-explicit-project-operational-contract`
- 必需输入：被评描述及版本, 具体决策、利益相关者和关注点, 现有内容与证据, 项目所需正式控制及裁剪理由
- 可选输入：已有模型/待办/历史决策, 组织特定规则及证据
- 缺输入策略：缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。
- 字段总数：16；对象类型：guide:description_review
- 关系类型：未声明
- 关联交付物：`architecture-definition-document`, `compliance-assessment`, `tailored-architecture-framework`

### 分析步骤

1. 定义该描述要支持的决策与范围，不能泛称“架构是否完整”。
2. 逐关注点核对内容及证据，判断sufficient-for-stated-decision/insufficient/unknown。
3. 独立列当前与所需正式控制（如术语、记法、版本、审阅证据），判断适合、缺少或过度并给理由。
4. 识别复杂系统缺文档或未验证概念就强制全面建模的极端，按当前目的提出最小补充。
5. 演进状态、审批状态另列；不把approved/target当作正式度。

### `guide:description_review` 必填字段（15）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `description_ref` | 被评架构描述及其版本的稳定引用 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `decision` | 该描述将支持的具体决策；充分性仅对该决策有效 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `stakeholders` | 使用该描述做决策或受到其影响的利益相关者 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `concerns` | 本次评审必须回应的具体关注点 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `sufficiency` | 对明确决策的sufficient-for-stated-decision/insufficient/unknown文字判断 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `sufficiency_evidence` | 逐关注点支持或阻断决策的内容及证据 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `current_formality` | 当前采用的术语/记法/版本/审阅等正式控制集合 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `needed_formality` | 针对用途所需正式控制集合，必须给裁剪依据 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `formality_fit` | 当前控制是否合适、缺少或过度的文字判断；不是批准状态 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `rationale` | 将内容/控制与决策联系起来的评审推理 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `actions` | 最小必要补充、削减或下一轮验证行动 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `evolution_state` | 被评描述所表达的架构演进状态，不当作正式程度 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `approval_state` | 描述的批准状态，独立于充分性与正式控制 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `review_rule` | 本项目使用的判断约定与出处；不称TOGAF量表 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `source_refs` | 支持本条业务内容的来源ID列表，区别指南定义来源 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |

其余字段（1）：`name`

### 输出

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

## 阶段边界与项目收尾记录

- `id`：`project-stage-closure-record`
- 英文名：Project Stage Closure Record
- 决策问题：是否继续、修改或终止阶段/项目，责任与成果是否可交接？
- 主责技能：`togaf-artifact-review`
- 来源：G188 §3.5.1–3.6.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：12；对象类型：guide:closure_record
- 关系类型：未声明
- 关联交付物：`statement-of-work`, `compliance-assessment`

### 分析步骤

1. 区分阶段边界、成功完成和提前终止
2. 核对所有产品状态及验收/撤销/移交去向
3. 比较计划/实际并保留容差未知
4. 提交剩余风险、项目影响与下一阶段或关闭建议
5. 监督机构决定并记录正式接受，之后才能释放/重新授权资源

### `guide:closure_record` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `closure_kind` | stage-boundary或project-closure | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `closure_reason` | 完成或提前终止及依据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `products` | 产品验收状态与未完成处置 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `performance` | 计划/实际时间成本质量范围风险收益；不合并成单分 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `risks_issues` | 风险问题剩余责任和处置 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `handover` | 接收方与足以开展后续工作的条件 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `next_stage` | 下一阶段计划或不适用 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `authority` | 决定继续/变更/终止的监督机构 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision` | 建议与批准分开 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `follow_up` | 所需补证、变更或资源释放条件 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

## 交付物章程与验收流程

- `id`：`project-deliverable-charter`
- 英文名：Project Deliverable Charter
- 决策问题：交付物要交什么、如何核验、由谁接受？
- 主责技能：`togaf-artifact-review`
- 来源：G188 §3.1.8示例3-14、§3.2.2–3.2.3、§3.5.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围、五维语境、所用目标与交付物版本, 原始计划/访谈/验收/估算及来源ID, 组织授权和容差规则；缺失时不代推
- 可选输入：历史项目及组织模板
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：12；对象类型：guide:deliverable_charter
- 关系类型：未声明
- 关联交付物：`statement-of-work`, `compliance-assessment`

### 分析步骤

1. 从决策和利益相关者定义产品范围与排除
2. 确认输入与版本并找缺口
3. 写可观察验收准则，引用已有architecture-acceptance-criteria记录
4. 规定评审与修订流程及有权接受者
5. 逐条实际评审，保留拒绝/重作路径；接受后再进入阶段/项目关闭

### `guide:deliverable_charter` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `deliverable_id` | 交付物稳定ID与版本 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `scope` | 内容与范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `exclusions` | 明确排除 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `required_inputs` | 输入及其版本/就绪情况 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `acceptance_criteria` | 可检验条件与既有单项验收准则ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `acceptance_process` | 按组织规则的移交/评审/修订/终审流程 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `decision_roles` | 评审/修订/最终接受角色分开 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `review_observations` | 实际评审发现与证据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `status` | 候选/评审/接受/拒绝；生成不等于接受 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `evidence_refs` | 材料ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `next_action` | 补缺或下一验收动作 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

跨记录ID明确表达前置、分组或引用；PM工作任务与TOGAF变革工作包保持不同身份。表格相邻不代表依赖。

---

合计 8 个工作产品，90 个字段。
