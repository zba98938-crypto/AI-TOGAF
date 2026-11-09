# 战略 MVA 追溯与边界变更：把退款塞进首期开放，代价是什么

虚构图书馆的战略是"读者自助办理预约与取消"。产品负责人把"预约受理"列为首次开放的必须项，"退款登记"暂为应有项。后来业务要求"预约与取消必须在同一开放窗口提供"，退款被提升为必须项并扩入同一 MVA。本案例演练：战略→epic→feature→story 的追溯链如何保证不断裂，以及边界变更时哪些记录必须保留、哪些证据仍然缺失。

所有业务材料、人物、优先级与授权均为虚构教学材料（`BR-1`–`BR-6`）；"战略意图—epic—feature—story"四层是**本项目追溯规则**，不是 TOGAF 默认层次。指南只提供方法依据。

方法：`architecture-backlog-trace-review`。来源方法：G20F §4.5 L304–327；§5.2.3 L529–547；§5.3.2 L601–632。
入口：[architecture-backlog-trace-review](../analysis-methods/architecture-backlog-trace-review.md)。
素材：原料（历史材料已清理）、基线模型（历史材料已清理）。

## 决策与原始业务资料

要回答：**首期开放（MVA）到底该包含哪些故事？扩容之后，原边界历史还在吗？哪些验收证据仍缺？**

| 证据 ID | 原始材料 |
|---|---|
| `BR-1` | 虚构图书馆战略：让读者自助办理预约与取消，减少人工重复录入。**本项目采用战略意图—epic—feature—story 层次**；只是本项目追溯规则。 |
| `BR-2` | 产品负责人把**预约受理**列为首次开放的**必须项**，**退款登记暂为应有项**。首个 MVA **仅覆盖预约受理**，排除退款自动结算与历史借阅迁移；后续功能仍保留在产品待办。 |
| `BR-3` | 预约受理故事要求每位读者每场次最多一项有效预约。退款登记故事要求取消后下一营业日生成退款队列记录；**依赖预约标识**。两故事均由读者服务负责人确认，**尚无运行验收结果**。 |
| `BR-4` | 架构负责人规定**预约幂等 ABB** 与**退款可追溯 ABB**；实施候选分别为**预约 API** 与**退款队列适配器 SBB**。**SBB 到 ABB 是设计实现关系，尚未部署。** |
| `BR-5` | **修改**：预约与取消必须在同一开放窗口提供。产品负责人把退款登记提升为 **must-have**，扩展同一 MVA 范围，仍排除自动结算及历史迁移；**保留原 MVA 范围历史**。 |
| `BR-6` | **修改后的测试记录**：预约幂等契约测试**通过**；退款队列与外部财务接口**尚未演练**。测试通过仅证明预约验收条件，**不证明整套 MVA 可运营**。 |

## 来源规则与项目规则

1. **来源方法（G20F §4.5）**：强调战略到待办的可追溯性；本案以 BR-1 的项目四层规则实现直接父项路径，不把该固定层次归为来源强制要求。
2. **来源方法（§5.2.3）**：MVA 边界是显式声明的**纳入集 + 排除集**；边界变更须留历史。
3. **来源方法（§5.3.2）**：优先级（must-have / should-have）需有证据；`included-in-mva` 是关系，不是隐含排序。
4. **项目规则**：四层层次由 `BR-1` 声明为**本项目**规则，不外推为 TOGAF 规定。
5. **项目规则**：MVA 边界变更必须同时保留 `history` 的旧版本，**不得覆盖**（`BR-5` 明示）。
6. **项目规则**：依赖方向为"退款依赖预约"，**不得反向**（`BR-3` 明示"依赖预约标识"）。
7. **项目规则**：验收状态只有"已观察"与"未观察"，`verified` 必须附证据（`BR-3` 明示尚无运行验收）。

## 转换与推理

1. **先建四层，再验路径**。`G-SELF`（战略意图）→ `E-RESERVE`（epic）→ `F-BOOK`/`F-REFUND`（feature）→ `S-BOOK`/`S-REFUND`（story）。关系 `R-GE`、`R-EFB`、`R-EFR`、`R-FSB`、`R-FSR` 均为 `refines`。**任一条缺失，某条 story 就失去向上追溯**——`R-EFB` 被删除时即产生"broken-strategic-trace"。

2. **ABB/SBB 是约束与实现，不是层次**。`ABB-IDEMPOTENT` 通过 `R-CB`（`constrains-story`）约束 `S-BOOK`；`ABB-REFUND` 通过 `R-CR` 约束 `S-REFUND`。`SBB-API` 通过 `R-IB`（`realizes`）实现 `ABB-IDEMPOTENT`，方向是 **SBB → ABB**。若把方向反过来写成"ABB 实现 SBB"，语义就反了（"reversed-realizes"）。

3. **基线 MVA 边界：纳入 1 条、候选 2 条、排除 3 项**。`boundary="预约受理及幂等护栏"`；`exclusions=["退款自动结算","历史借阅迁移","本期退款队列登记"]`；`candidate_story_ids=["S-BOOK","S-REFUND"]` 但实际纳入仅 `S-BOOK`（`R-MB`）。**候选集不等于纳入集**——`S-REFUND` 是候选但被 `exclusions` 排除，这个差异必须由 `history.v1.selected_story_ids=["S-BOOK"]` 显式记录。

4. **优先级需证据**。`S-BOOK.priority=must-have`，`priority_evidence=["BR-2"]`；`S-REFUND.priority=should-have`，同样指向 `BR-2`。`BR-2` 一句话同时支撑两个不同优先级，因为原文明确区分了"必须项"与"应有项"。**若清空 `priority_evidence`，优先级就变成主观断言**。

5. **修改：边界扩容，历史保留**。`BR-5` 使 `MVA-OPEN` 变为：`boundary="预约受理、取消退款登记及其幂等/追溯护栏"`；`exclusions` 减为两项（移除"本期退款队列登记"）；`history` 追加 `v2`，含 `selected_story_ids=["S-BOOK","S-REFUND"]` 与证据 `BR-5`。**`v1` 原样保留**——这是"保留原 MVA 范围历史"的直接落地。

6. **同步调整优先级与关系**。`S-REFUND.priority` 从 `should-have` 改为 `must-have`，`priority_evidence` 从 `["BR-2"]` 改为 `["BR-5"]`（依据变了）。新增 `R-MR`（`included-in-mva`：`S-REFUND → MVA-OPEN`）。依赖 `R-DEP`（`S-REFUND --story-depends-on--> S-BOOK`）**保持原方向**。

7. **验收状态是最容易被夸大的一项**。修改后 `S-BOOK.acceptance.status` 可因 `BR-6` 的"契约测试通过"而更新（但仍需判断测试是否等同验收条件）；`S-REFUND.acceptance.status` **仍为 `not-observed`**，因为"退款队列与外部财务接口尚未演练"。因此 MVA 整体 `readiness="pending-evidence"`，缺口为 `[{story_id: "S-REFUND", code: "acceptance-not-verified"}]`。

8. **`BR-6` 的限定必须照抄**："测试通过仅证明预约验收条件，不证明整套 MVA 可运营"。这句话阻止了"一项测试通过 ⇒ MVA 可上线"的跳跃。

## 输出与追溯

| 结果 ID | 结论 | 追溯 | 状态 |
|---|---|---|---|
| `MVA-1` | 四层追溯路径完整：G-SELF → E-RESERVE → F → S，五条 `refines` 齐备 | `BR-1`,`BR-3` | 已核对 |
| `MVA-2` | ABB 约束 story、SBB 实现 ABB，方向为 `realizes`（SBB → ABB） | `BR-4` | 已核对 |
| `MVA-3` | 基线 MVA 纳入 `S-BOOK` 一项，排除三项，候选集与纳入集差异显式 | `BR-2` | 已判定 |
| `MVA-4` | 修改后纳入 `S-BOOK` + `S-REFUND`，`history` v1/v2 并存 | `BR-5` | 已判定 |
| `MVA-5` | `S-REFUND` 优先级 should→must，依据由 `BR-2` 换为 `BR-5` | `BR-5` | 已判定 |
| `MVA-6` | 依赖方向 `S-REFUND → S-BOOK` 未反转 | `BR-3` | 已核对 |
| `MVA-7` | MVA `readiness=pending-evidence`，缺口为 `S-REFUND` 验收未验证 | `BR-6` | 已判定 |
| `MVA-GAP-1` | `S-REFUND` 验收条件尚无运行证据 | `BR-6` | 未决 |
| `MVA-GAP-2` | 退款队列与外部财务接口未演练 | `BR-6` | 未决 |

本方法采用定性判断与追溯演练，没有适用的统一计算器。追溯链的**连通性可机械检查**（每条 story 是否可达战略意图），但"是否该纳入 MVA""优先级是否合理"属于业务判断，不由计算得出。

## 方法步骤对照

下表把注册表声明的分析步骤逐条对到本案例的执行位置，用以核对"按步骤走"而非"凭印象写"。

| # | 注册表步骤 | 本案执行位置 | 判定 |
| --- | --- | --- | --- |
| 1 | 逐句提取战略意图、业务分段、故事和原始来源；项目声明epic/feature/story层次，不能假称标准要求 | 「转换与推理」 | 已执行 |
| 2 | 依据产品负责人排序形成MVA必须项边界；保留未纳入项及排除理由 | 「转换与推理」 | 已执行 |
| 3 | 把ABB护栏及计划SBB实现显式关联到故事；核对实现方向和前置依赖 | 「转换与推理」 | 已执行 |
| 4 | 修改战略或边界时保留ID与历史，重算纳入集合与依赖；分别检查验收证据和可运营条件 | 「转换与推理」 | 已执行 |

**说明**：步骤顺序来自 `capabilities.json` 的 `architecture-backlog-trace-review` 条目；本案的执行结果见「输出与追溯」，缺口见「反例与输入不足」。

## 修改演练

改动一处输入：`BR-1` 的四层规则改为三层（去掉 feature 层，story 直接挂在 epic 下）。

- `hierarchy_policy.levels`：`["strategic_intent","epic","feature","story"]` → `["strategic_intent","epic","story"]`。
- `F-BOOK`、`F-REFUND` 失去层次位置，其 `refines` 关系必须重接到 `E-RESERVE → S-*`。
- **影响范围**：`R-EFB`、`R-EFR`、`R-FSB`、`R-FSR` 四条关系被替换；追溯路径节点数从 4 层降为 3 层。
- **不能做的事**：直接删除 `F-BOOK`/`F-REFUND` 节点而无替代路径，会导致 `S-BOOK`、`S-REFUND` 追溯断裂。
- 由于 `BR-1` 明确该层次是**本项目规则**，改层次属于**项目规则变更**，需记录变更理由与决策人，不能由分析者单方调整。

反向演练（更常见）：若 `BR-5` 只说"退款提升为 must-have"而未说"扩入同一 MVA"，则 `MVA-OPEN` 的 `boundary` 与 `history` **不应变化**，只有 `S-REFUND.priority` 变化。此时若加入 `R-MR`，就是**把优先级提升误当边界扩容**——两者是不同的决策。

## 四层追溯与 MVA 边界

- 战略意图 → epic → feature → story，每层可向上追溯
- ABB 约束 story，SBB 实现 ABB，方向为 SBB → ABB
- MVA 边界 = 纳入集 + 排除集，候选集不等于纳入集
- 边界变更保留 history 旧版本，不覆盖
- 依赖方向为退款依赖预约，不得反转

## 反例与输入不足

- **错误做法**：两个节点使用同一个 ID（复制粘贴未改）。预期 `duplicate-id`。
- **错误做法**：删除 `R-EFB`，`S-BOOK` 失去向上追溯路径。预期 `broken-strategic-trace`。
- **错误做法**：把 `R-IB` 的方向改成 `ABB-IDEMPOTENT → SBB-API`。实现关系方向是 SBB → ABB。预期 `reversed-realizes`。
- **错误做法**：`BR-5` 已明确退款扩入同一 MVA，但缺少 `R-MR`。已决定的纳入关系遗漏；仅升优先级而未扩边界时不应报此错。预期 `must-have-omitted-from-mva`。
- **错误做法**：`S-BOOK.priority_evidence=[]`，只写 `priority=must-have`。优先级无依据。预期 `priority-without-evidence`。
- **错误做法**：新增 `S-BOOK --story-depends-on--> S-REFUND`，与原 `R-DEP` 形成环。预期 `dependency-cycle`。
- **错误做法**：`landscape` 字段填 `target`（把演化态当景观）。预期 `landscape-evolution-confusion`。
- **错误做法**：`acceptance={status: "verified", evidence: []}`。已验收必须附证据。预期 `false-verified-acceptance`。
- **错误做法**：`BR-5` 扩容后把 `history` v1 删除，只留 v2。历史被覆盖。预期 `missing-evidence`。
- **错误做法**：`BR-6` 的预约契约测试通过后，把整个 MVA 标为验收通过。预期 `approval-without-evidence`。

**输入不足**：`BR-3` 只说两故事"尚无运行验收结果"，未给验收的执行方式与判定人，因此 `acceptance.status` 只能停在 `not-observed`，不能写"待验收"以外的中间态。`BR-6` 未给退款队列演练的计划日期，`MVA-GAP-2` 不能填日期。

## 评审记录

- 核对四层追溯路径逐条可达战略意图，无孤立 story。
- 核对 `refines` 与 `realizes` 方向语义正确，SBB 在源端。
- 核对基线 MVA 的候选集与纳入集差异显式记录，未混为一谈。
- 核对修改后 `history` v1 保留、v2 追加，未覆盖旧版本。
- 核对 `S-REFUND` 优先级变更同步更新了 `priority_evidence`。
- 核对依赖方向未反转且无环。
- 核对 MVA 就绪状态为 `pending-evidence`，缺口指向具体 story。
- 核对 `BR-6` 的"不证明整套 MVA 可运营"限定被写入输出。
- 本案例输出为表格型字段展开，未做图形化渲染，不声明源图视觉复现通过。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
