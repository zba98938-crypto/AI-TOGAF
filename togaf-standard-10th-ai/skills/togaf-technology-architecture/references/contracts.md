# togaf-technology-architecture 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 微服务技术指南

- `id`：`microservice-technical-guidance`
- 英文名：Microservice Technical Guidance
- 决策问题：哪些技术约束保障微服务实现？
- 主责技能：`togaf-technology-architecture`
- 来源：G21I §6–7；G21I §5.2、§5.5、表5-1；G21I §5.3、表5-1、§12.2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, concern, standard, rationale
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：23；对象类型：microservice_guideline, ops:msa_readiness, ops:msa_governance
- 关系类型：traces_to, ops:governance_supports, ops:governance_aligns, ops:governance_extends, ops:governance_constrains
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 从目标质量选择指南
2. 定义接口运行与治理约束
3. 说明适用与例外
4. 关联合规验证
5. 按单服务全过程检查归属、技能、自治、DevOps与试点学习
6. 分别记录已知、部分和未知，不按条数计成熟度
7. 将每个不足转为责任、行动和进入试点条件
8. OSIMM按独立来源调用，不用ACMM或项目表替代
9. 界定企业护栏和MSA专属决定两条轨道
10. 区分五类角色职责与请求/决定权限
11. 核对每次发布控制和持续反馈
12. 偏离需显式申请并以委员会决定为准
13. 支持/对齐/扩展/约束分别记录方向

### `microservice_guideline` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `concern` | 利益相关者的具体关注点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `standard` | 适用标准和版本 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `rationale` | 分析或选择的理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `applicability` | 适用性判据与判断理由 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `verification` | 验证方法与验收证据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `exception` | 例外及其治理方式 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `ops:msa_readiness` 必填字段（9）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `concern` | 利益相关者的具体关注点 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `observation` | 实际观察/未取得材料 | 范围内实际观察或明确未取得材料；事实、推论和行动不得混写；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `judgment` | 文字判断，不是成熟度分数 | 微服务准备度定性判断；记录理由和未知，不自动映射成熟度分数；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `owner` | 行动责任 | 本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `action` | 补证据和能力行动 | 补证或改进行动；记录责任方、触发或期限及未关闭事项；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `scope` | 组织/服务/时点 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `decision_consequence` | 对试点/采用的限制 | 微服务准备度判断对采用或试点的限制；补证前不得把候选判断当就绪；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `scoring` | scheme/score/basis，未提供模型时none/null | 明确评分模型与依据或none/null；没有来源和项目授权不合成成熟度总分；类型约束：`{"anyOf":[{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]},{"type":"null"}]}`（来源：`project-operational-convention`） |
| `evidence_detail` | 访谈或试验定位 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

### `ops:msa_governance` 必填字段（10）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `authority` | 对该层决策负责的主体 | 有权作出本项决定的责任主体；列授权范围，不能把执行者当批准方；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `roles` | 五类角色职责摘要，源表5-1 | 微服务治理五类角色的职责与授权边界；不能把角色列举当作各方已接受任命；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `decision` | 治理实际决策/请求 | 待作或已作的业务决定；写问题、选项与结果边界，建议不自动成为批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `decision_status` | 计划/待决等业务状态 | 决定的业务状态；candidate/planned/pending/approved/rejected/unknown，approved另需授权证据；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `waiver` | 请求/状态/决定证据/批准方 | 微服务控制豁免的请求、状态和决定；批准时须scope/expiry/authority/evidence_refs，申请不视为批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `controls` | 可执行控制活动 | 微服务治理可执行控制；逐项列控制活动、责任和验证证据，政策声明不能代替执行；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `feedback` | 持续监督/纠偏 | 治理持续监督与纠偏；注明观察信号、反馈对象、责任及后续行动；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `scope` | 应用范围及时间 | 本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `mapping_origin` | 项目映射与来源图分离 | 映射来源身份；区分project-observation/project-proposal/source-verified，后者须独立原文核实；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 决策证据或缺口 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 互操作性评估

- `id`：`interoperability-assessment`
- 英文名：Interoperability Assessment
- 决策问题：跨系统和组织交换能否满足业务要求？
- 主责技能：`togaf-technology-architecture`
- 来源：G217 §4.4.4、附录C.4表C-5
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, parties, interaction, information
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：interoperability_issue
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 界定交互各方及业务目的
2. 检查信息含义接口协议
3. 分析组织与技术约束
4. 提出证据支持的改进

### `interoperability_issue` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `parties` | 交互各方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `interaction` | 跨方交互及其目的 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `information` | 被使用或修改的信息引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `protocol` | 交互协议 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `constraint` | 适用约束 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `evidence` | 本条观察的证据描述或引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `equipment` 必填字段（4）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `equipment_class` | 设备业务或技术分类 | 设备业务或技术分类；引用分类规则，不以设备名称自行推断分类；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `work_center_ref` | 设备归属工作中心的稳定引用 | 设备归属工作中心的稳定引用；位置相近不自动表示归属或产线依赖；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `criticality` | 对象对业务连续性的关键程度 | 对象对业务连续性的关键程度；声明量表和损失依据，不无来源赋高低分；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `maintenance_plan_ref` | 设备维护计划引用 | 设备维护计划引用；关联版本与有效期，未执行计划不当作设备可用证据；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"array","minItems":1,"uniqueItems":true,"items":{"type":"string","minLength":1,"pattern":"\\S"}}]}`（来源：`project-operational-convention`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## SOA 分层参考

- `id`：`soa-layered-reference`
- 英文名：SOA 分层参考
- 决策问题：依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。
- 主责技能：`togaf-technology-architecture`
- 来源：G21I/fig5-3
- 定义状态：`source-derived-view-with-project-construction-rules`
- 必需输入：视点问题与范围, 带来源的对象、关系及定义
- 可选输入：企业裁剪及例外说明
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。
- 字段总数：4；对象类型：soa_concern, soa_layer
- 关系类型：project:cross_cuts_soa, project:maps_to
- 关联交付物：`architecture-definition-document`, `architecture-building-blocks`

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

---

合计 3 个工作产品，34 个字段。
