# togaf-change-value 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 信息系统年度环境评估

- `id`：`environmental-is-assessment`
- 英文名：Annual IS Environmental Assessment
- 决策问题：信息系统的环境影响从何而来？
- 主责技能：`togaf-change-value`
- 来源：G242 §3.6, §3.6.1–3.6.3; Figure3-10；G242 Chapter6; English PDF98–99
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "accounting_boundary", "origin": "source-plus-project-contract", "meaning": "组织、服务、地理、期间、生命周期和功能单位"}, {"id": "asset_service_inventory", "origin": "source", "meaning": "自营、云、分包、网络、员工设备、客户终端及归属"}, {"id": "activity_data", "origin": "source", "meaning": "用电、设备与服务使用，含单位时间来源"}, {"id": "factor_catalog", "origin": "source", "meaning": "制造、运行和能源结构原始单位数据及来源"}, {"id": "allocation_rule", "origin": "source-plus-project-contract", "meaning": "供应商或共用资产分配及防重依据"}, {"id": "cloud_service_records", "origin": "source", "meaning": "第6章19字段最小共享记录（适用时）"}, {"id": "offsets", "origin": "source", "meaning": "与毛排放分开记录"}, {"id": "comparison_contract", "origin": "project-operational", "meaning": "历年同范围、同口径及变化说明"}
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：未知量不作零。可用有明确来源的数量级估计，但须列出精度和边界限制；缺关键数据可输出已知小计，禁止称完整总量。
- 字段总数：12；对象类型：environment_measure, repository_asset
- 关系类型：causal_influence, traces_to
- 关联交付物：`change-request`, `capability-assessment`

### 分析步骤

1. 锁定测量范围与功能单位并检查清单覆盖
2. 取原始用量、制造因子和云报告
3. 检查期间、单位、生命周期、报告口径与组织归属
4. 选择并声明Scope2口径和分配规则
5. 逐记录计算并检测重复/子集
6. 按相同边界互斥分类汇总毛排放，抵消另列
7. 对齐年度并解释差额、未知量和规则变化
8. 传达业务职能影响及可验证减排杠杆

### `environment_measure` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `year` | 环境核算年度 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `scope` | 适用组织、业务及架构边界 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `object` | 核算或分析对象 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `lifecycle_stage` | 资产生命周期阶段 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `unit` | 度量单位 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `value` | 度量值或业务价值陈述，依语境声明 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `allocation` | 资源分配 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `overlap_group` | 环境措施潜在重叠效益分组 | 环境措施潜在重叠效益分组；同组措施汇总前须消除双计，不等同自动互斥；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `boundary_id` | 环境核算边界标识 | 环境核算边界标识；同一比较或汇总须引用同一边界定义；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `period_kind` | 环境核算期间类型 | 环境核算期间类型；区分瞬时、期间与累计口径，不跨口径直接相加；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `value_basis` | 环境量值口径 | 环境量值口径；实测、估算或假设明确区分，估算须方法与来源，不当作实测；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |

### `phosphogypsum_record` 必填字段（5）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `generated_tonnage` | 核算期内磷石膏产生量 | 核算期内磷石膏产生量；单位吨、非负，期初堆存不得计为当期产生；类型约束：`{"type":"number","minimum":0}`（来源：`project-operational-convention`） |
| `utilised_tonnage` | 核算期内磷石膏利用量 | 核算期内磷石膏利用量；单位吨、非负，历史堆存利用须标明口径避免误算当期率；类型约束：`{"type":"number","minimum":0}`（来源：`project-operational-convention`） |
| `stockpiled_tonnage` | 核算期末磷石膏堆存量 | 核算期末磷石膏堆存量；单位吨、非负，库存不是当期新增量；类型约束：`{"type":"number","minimum":0}`（来源：`project-operational-convention`） |
| `utilisation_rate` | 磷石膏当期综合利用率 | 磷石膏当期综合利用率；采用utilised/generated的0至1比例，分母为零不计算；类型约束：`{"type":"number","minimum":0,"maximum":1}`（来源：`project-operational-convention`） |
| `period` | 结果或核算记录的时间窗 | 结果或核算记录的时间窗；注明起止、周期口径，不混合不同期间的值；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 环境债务日志

- `id`：`environmental-debt-register`
- 英文名：Environmental Debt Register
- 决策问题：哪些环境代价被推迟处理？
- 主责技能：`togaf-change-value`
- 来源：G242 §3.9.5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, decision, impact, reason
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：environmental_debt
- 关系类型：traces_to
- 关联交付物：`change-request`, `capability-assessment`

### 分析步骤

1. 识别设计运营中的环境债务
2. 记录接受理由与影响
3. 安排消除措施
4. 按证据复评

### `environmental_debt` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `decision` | 决策结果、理由和状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `impact` | 业务影响及其依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `reason` | 接受或处置的理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `remediation` | 消除债务的措施 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `review_date` | 计划复评日期 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 冲刺DORP记录

- `id`：`dorp-record`
- 英文名：Sprint DORP Record
- 决策问题：本冲刺是否达成目标、学到什么、哪些工作需要回流或进入下一次规划？
- 主责技能：`togaf-change-value`
- 来源：G210 §3.3.2、§5.5
- 定义状态：`guide-body-located-with-explicit-project-operational-contract`
- 必需输入：明确冲刺目标与所选待办, 演示观察及成果证据, 未完成项/新需求, 回顾及下一步行动责任
- 可选输入：已有模型/待办/历史决策, 组织特定规则及证据
- 缺输入策略：缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。
- 字段总数：11；对象类型：guide:dorp_record
- 关系类型：未声明
- 关联交付物：`change-request`, `compliance-assessment`, `implementation-migration-plan`

### 分析步骤

1. 先固定本次冲刺目标和评审时点，不因结果不好而改写目标。
2. 按Demo记录实际展示和未展示内容；按Outcome核对目标与成果。
3. 按Retrospective解释偏差与可改进做法，不将推测当根因事实。
4. 按Planning形成有责任人与依据的下一步建议；未完成项回到业务待办。
5. 新需求先登记澄清，不自动承诺下一冲刺；保留历史与后续补充。

### `guide:dorp_record` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `sprint_ref` | DORP所审阅冲刺稳定ID；在独立调用时作为明确外部引用 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `goal` | 整个冲刺的可验证目标；不能由选中事项标题自动代替 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `demo` | 逐项实际展示内容、证据和未展示/失败观察，不是完成自报 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `outcomes` | 相对于原目标的结论、完成/未完成集合及理由 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `retrospective` | 对做法及结果的回顾，区分观察与推测根因 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `next_plan` | 下一步建议的ID、行动、责任、时间和状态，不能冒充已批准承诺 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `returned_to_business_backlog` | 未完成项回流业务待办的原始ID列表 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `new_backlog_requests` | 新提出但可能尚未澄清/估算的需求，不默认承诺 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `review_at` | DORP的评审时点，用于保留历史目标判断 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `history` | 按观察时间保留状态/结论与证据的历史，不由后续结果覆盖 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |

其余字段（1）：`name`

### 输出

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

## 技术与架构债登记

- `id`：`technical-debt-register`
- 英文名：Technical and Architecture Debt Register
- 决策问题：哪些债务应由本产品或EA协调处理，如何追溯偿还并验证关闭？
- 主责技能：`togaf-change-value`
- 来源：G217 §2.2–2.3、附录D.4
- 定义状态：`guide-body-located-with-explicit-project-operational-contract`
- 必需输入：运营/架构问题与证据, 受影响产品和跨产品关系, 原因及业务后果, 偿还选项、负责人、待办与关闭规则
- 可选输入：已有模型/待办/历史决策, 组织特定规则及证据
- 缺输入策略：缺失关键输入标记draft和带ID缺口，停止对应通过判断；可以生成明确草稿，不能编造分数、批准、实现或事实。
- 字段总数：17；对象类型：guide:technical_debt
- 关系类型：未声明
- 关联交付物：`change-request`, `architecture-repository`, `implementation-migration-plan`

### 分析步骤

1. 从问题记录识别债务及来源，区分技术局部问题与架构跨产品问题。
2. 描述影响、原因及不确定性，不凭债务比喻生成利率/金额。
3. 判断是否需EA协调；仅局部债可交产品团队，说明理由。
4. 比较偿还候选与资源/依赖，关联待办、标准、复用或变更记录。
5. 按声明的项目关闭规则收集修复、验证和复核证据，不能凭排期关闭。

### `guide:technical_debt` 必填字段（16）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `kind` | 债务的技术/数据/接口/架构性质，允许项目分类 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `affected_products` | 受影响产品或服务范围，为EA介入判断提供依据 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `cause` | 已知原因或明确假说，必须区别根因证实程度 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `consequence` | 对业务、运营、变更或集成的影响，不默认货币化 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `evidence_summary` | 债务观察来源、可信度与缺失数值的说明 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `ea_involvement` | 由本产品处理或需要EA跨产品协调的路由判断 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `ea_rationale` | 该路由判断的范围和后果依据，不是所有债一律EA负责 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `repayment_option` | 偿还候选行为及预期解决的问题，不等于已选定执行 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `backlog_refs` | 偿还关联的待办ID；空列表表示尚未形成条目 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `owner` | 负责澄清、交付或处理该项的角色；不是隐含审批人 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `review_date` | 下一复核时点，由项目安排；不代表完成承诺 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `status` | 该工作产品自身的业务流程状态，独立于模型批准/实现状态 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `closure_criteria` | 项目声明的关闭依据要求，来源和变更必须记录 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `verification_evidence` | 修复结果的验证引用，选入计划不能当验证 | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `closure_decision` | 责任人基于关闭依据的复核结论或not-closed | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |
| `cost_or_interest` | 仅记录有出处的成本/金额/假设；未知明示，不自造利率或ROI | 必填有来源的具体值或显式unknown/待确认，并在缺口中登记；空值不能伪装完成。（来源：`project-operational-contract-guided-by-cited-body`） |

其余字段（1）：`name`

### 输出

- 范围、决策与原料出处
- 对象属性表及关系表
- 逐条分析结论和理由
- 待确认输入/例外/修改影响
- 指定视图与交付物引用

## 用途与基础设施双入口分析

- `id`：`sustainability-dual-entry-analysis`
- 英文名：Sustainability Dual Entry Analysis
- 决策问题：从哪里识别可放弃/优化用途与设备，如何形成可接受约束？
- 主责技能：`togaf-change-value`
- 来源：G242 §3.5.2–3.5.3、表3-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：组织、服务、业务用途及所评估期间/生命周期边界, 原始访谈、使用数据、供应商记录及稳定证据ID, 适用目标、职责和组织自定决策规则；未知项显式登记
- 可选输入：历史评估、环境数据目录、采购契约及角色技能资料
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：13；对象类型：guide:dual_entry_opportunity
- 关系类型：未声明
- 关联交付物：`implementation-migration-plan`, `architecture-requirements-specification`

### 分析步骤

1. 取得与业务/技术协作的管理授权
2. 从业务用途和高影响基础设施分别建立候选清单
3. 沿应用/数据/设备向下或业务向上追溯共享影响
4. 核实业务接受性并修订非功能要求
5. 明确四类约束理由/检查/复评，并转入方案评审和治理

### `guide:dual_entry_opportunity` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `entry_point` | use或infrastructure，两入口分别输出 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `use_id` | 业务用途稳定ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `application_data_path` | 应用/数据映射路径 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `infrastructure_id` | 设备/系统稳定ID | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `baseline_evidence` | 初始使用/资源/环境依据及缺口 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `action` | 优化或放弃候选 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `business_acceptance` | 业务可接受性及授权 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `nonfunctional_change` | 修订的非功能要求 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `constraints` | 用途/数据/应用开发/基础设施四类约束 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `priority_basis` | 排序规则与依据，不能无依据打分 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `dependencies` | 共享依赖/退出影响 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `status` | 待验证/候选，不能凭分析认定减排 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

用途—应用/数据—基础设施用稳定ID追踪；评估维度与功能多对多关联；总额与子集、两种Scope2基础、抵消和复制存储分别表达。表格相邻不代表因果或可相加。

## 共享碳单位数据与因子目录

- `id`：`shared-carbon-factor-catalog`
- 英文名：Shared Carbon Factor Catalog
- 决策问题：哪些单位数据可在什么边界、版本和单位下复用于环境评估？
- 主责技能：`togaf-change-value`
- 来源：G242 §3.6.3表3-4
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：组织、服务、业务用途及所评估期间/生命周期边界, 原始访谈、使用数据、供应商记录及稳定证据ID, 适用目标、职责和组织自定决策规则；未知项显式登记
- 可选输入：历史评估、环境数据目录、采购契约及角色技能资料
- 缺输入策略：关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。
- 字段总数：13；对象类型：guide:carbon_reference_data
- 关系类型：未声明
- 关联交付物：`architecture-repository`, `architecture-definition-document`

### 分析步骤

1. 收集原始单位数据和来源，不把计算结果当原始因子
2. 声明机型/服务/地区/期间与生命周期边界
3. 核实单位分母、分配与PUE包含情况
4. 登记版本、质量和适用限制
5. 更新时保留旧版及引用该版的评估，禁止静默替换历史计算

### `guide:carbon_reference_data` 必填字段（12）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `data_kind` | 活动强度、设备足迹或电力因子等，不全部称排放因子 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `value` | 原始值；不静默插值 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `unit` | 原始单位与分母 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `period` | 适用/观察期间 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `geography` | 地区/设施/能源结构 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `lifecycle_boundary` | 制造、运行或组合边界 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `applicability` | 机型/服务/分配范围 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `allocation_basis` | 是否含PUE及服务分配依据 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `source_version` | 来源版本和更新日期 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `source_locator` | 原料/供应商/计算记录定位 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `quality` | 测量/估算/未知及不确定性 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |
| `reuse_limits` | 不可跨何种范围/单位/期间复用 | 原料ID与数据版本明确；组织规则显式注明；未知保留缺口。（来源：`guide-derived-project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

### 关系语义

用途—应用/数据—基础设施用稳定ID追踪；评估维度与功能多对多关联；总额与子集、两种Scope2基础、抵消和复制存储分别表达。表格相邻不代表因果或可相加。

## 事件后的架构调整记录

- `id`：`incident-architecture-adjustment`
- 英文名：Architecture Adjustment after an Incident
- 决策问题：事件如何改变了利益相关者的风险偏好与需求，有哪些目标变更、取消目标或取消变更的选项？
- 主责技能：`togaf-change-value`
- 来源：G186 §12.3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：{"id": "incident", "meaning": "事件事实、日期与证据", "origin": "source-purpose-plus-project-contract"}, {"id": "objectives", "meaning": "受影响目标", "origin": "source-purpose-plus-project-contract"}, {"id": "risk_appetite_before", "meaning": "事件前风险偏好及权限方", "origin": "source-purpose-plus-project-contract"}, {"id": "risk_appetite_after", "meaning": "事件后风险偏好及权限方", "origin": "source-purpose-plus-project-contract"}, {"id": "risk_tolerance", "meaning": "风险容忍度及权限方", "origin": "source-purpose-plus-project-contract"}, {"id": "requirement_changes", "meaning": "由偏好变化引起的需求变更及影响评估引用", "origin": "source-purpose-plus-project-contract"}, {"id": "options", "meaning": "变更目标/取消目标/取消变更三类选项及其成本、确定性与后果", "origin": "source-purpose-plus-project-contract"}, {"id": "decision", "meaning": "利益相关者决定状态、所选选项、权限与证据", "origin": "source-purpose-plus-project-contract"}, {"id": "summary", "meaning": "调整事项摘要", "origin": "source-purpose-plus-project-contract"}
- 可选输入：既有模型及历史结论
- 缺输入策略：关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。
- 字段总数：10；对象类型：guide:incident-adjustment
- 关系类型：未声明
- 关联交付物：`change-request`, `requirements-impact-assessment`

### 分析步骤

1. 记录事件事实与证据
2. 记录事件前后的风险偏好与风险容忍度及权限方
3. 把偏好变化登记为需求变更并做影响评估
4. 提出目标与工作变更方案，说明成本、确定性与残余风险
5. 同时评估取消目标与取消变更的后果
6. 由利益相关者决定并留存证据

### `guide:incident-adjustment` 必填字段（8）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `incident` | 事件事实、日期与证据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `objectives` | 受影响目标 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `risk_appetite_before` | 事件前风险偏好及权限方 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `risk_appetite_after` | 事件后风险偏好及权限方 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `risk_tolerance` | 风险容忍度及权限方 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `requirement_changes` | 由偏好变化引起的需求变更及影响评估引用 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `options` | 变更目标/取消目标/取消变更三类选项及其成本、确定性与后果 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |
| `decision` | 利益相关者决定状态、所选选项、权限与证据 | 来源事实、项目规则、参考内容与未知分别记录；不填造数据（来源：`guide-statement-plus-explicit-project-operational-field`） |

其余字段（2）：`name`、`summary`

### 输出

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

---

合计 7 个工作产品，83 个字段。
