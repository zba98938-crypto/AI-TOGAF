# G21B/fig4-1 · 架构愿景的利益相关者

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig4-1.md) · [JSON](../../architecture/diagrams/G21B/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 30 页

![英文原图](../assets/G21B/fig4-1-p0030.png)

PDF 坐标：`[48.2, 36.0, 563.8, 284.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
ween ----------------------------------------------.
a 2---------------.
a2------------.
eanenn---------------
External
External Data
Business
Provider
Partners
Customer Regulator
) |
een nee eee
ee
ween een eee
Distributors / Agent
C-MDM Operational Team
(Customer-Facing Employees Capturing
(including IT, Architects,
Operational
Customer Data / Requests)
Data and Business Actors)
Management
and Team
Customer Data Owner
C-MDM Product Owner
wenn
High-Level
Human
Management
Chief Data
Chief Technology
Business
and
Resources/
Process Owners
Officer (CDO)
|
Officer (CTO)
|
Change Leader
Sponsorship
Chief Executive Officer (CEO)
--
```

## 概要（历史解释；局部修正见上）

把 C-MDM 架构愿景的利益相关者按“外部—运营—高层”三层列出，共 13 个角色/群体。

## 目的（历史解释；局部修正见上）

支撑第 4.2 节 ADM 阶段 A（架构愿景）：C-MDM 项目影响整个组织、参与者众多，必须先建立愿景并在高层达成共识；本图给出必须纳入愿景沟通与认可的干系人清单，并暗示越往下越贴近日常运营、越往上越承担赞助与决策。

## 阅读顺序（历史解释；局部修正见上）

从上到下读三条带：最上方“External”是组织外部、只能影响不能指挥的干系人；中间“Operational Management and Team”是日常操作客户数据的人与团队；最下方“High-Level Management and Sponsorship”是提供赞助与跨部门决策的高层。每带左侧的三角形指向右侧，表示该层干系人位于组织边界之内/之外的位置。带内方框并列，从左到右没有顺序或优先级。

## 关键含义（历史解释；局部修正见上）

- 外部干系人 4 个：客户、监管机构、外部数据提供方、业务伙伴；他们决定 C-MDM 必须满足的体验、合规与数据来源约束。
- 运营层 4 个：分销商/代理（面向客户、采集客户数据/请求的员工）、C-MDM 运营团队（含 IT、架构师、数据与业务参与者）、客户数据所有者、C-MDM 产品负责人。
- 高层 5 个：CDO、CTO、人力资源/变革负责人、业务流程所有者，以及横跨整行的 CEO。
- CEO 单独占一整行，位于最底部，呼应正文“最佳执行发起人是能打破组织/业务线孤岛的 CEO”。
- 客户数据所有者与 C-MDM 产品负责人在运营层并列，说明数据问责（owner）与产品交付（product owner）是两条不同的职责线。
- CDO 与 CTO 在高层并列：C-MDM 同时是数据治理议题与技术架构议题；HR/变革负责人负责组织变革与采纳。
- 图只给干系人分层，不画影响力方向或沟通关系；具体愿景维度（FROM/TO/关键举措）见表 4-2。

## 层级（历史解释；局部修正见上）

三层：外部（组织外）→ 运营管理与团队（执行层）→ 高层管理与赞助（决策/赞助层）。每层内的方框并列，无上下级；CEO 虽在最底层带内，但横贯整行，视觉上表示其对全部利益相关者的最终发起作用。

## 线条含义（历史解释；局部修正见上）

图中没有连接线。三条水平虚线只分隔层级；左侧的向右三角形是层级标记（不是箭头关系），不表示数据或影响力流向。干系人之间的关系完全由“在哪一带”表达（关系清单中标为隐含）。

## 易误读点（历史解释；局部修正见上）

- 不要把三条带读成汇报层级：外部干系人不在组织内，运营层与高层也不是严格的上下级，只是按“离日常运营的远近”分组。
- CEO 画在最底部不代表其层级最低；它横跨整行，表示对全部干系人的最终赞助与破孤岛作用。
- 图中没有画出干系人之间的沟通线，不能据此判断谁向谁汇报。
- 中文稿本地化图有两个运营框边框断裂、一个标签字号过小，容易让人以为该框不属于本层；原图中它们都是完整框。

## 元素

```json
[
  {
    "id": "band_external",
    "label_en": "External",
    "label_zh": "外部",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 1
  },
  {
    "id": "st_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "stakeholder",
    "parent": "band_external",
    "level": 2
  },
  {
    "id": "st_regulator",
    "label_en": "Regulator",
    "label_zh": "监管机构",
    "type": "stakeholder",
    "parent": "band_external",
    "level": 2
  },
  {
    "id": "st_ext_data_provider",
    "label_en": "External Data Provider",
    "label_zh": "外部数据提供方",
    "type": "stakeholder",
    "parent": "band_external",
    "level": 2
  },
  {
    "id": "st_business_partners",
    "label_en": "Business Partners",
    "label_zh": "业务伙伴",
    "type": "stakeholder",
    "parent": "band_external",
    "level": 2
  },
  {
    "id": "band_operational",
    "label_en": "Operational Management and Team",
    "label_zh": "运营管理与团队",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 2
  },
  {
    "id": "st_distributors",
    "label_en": "Distributors / Agent\n(Customer-Facing Employees Capturing Customer Data / Requests)",
    "label_zh": "分销商/代理（面向客户、负责采集客户数据/请求的员工）",
    "type": "role",
    "parent": "band_operational",
    "level": 2
  },
  {
    "id": "st_cmdm_ops_team",
    "label_en": "C-MDM Operational Team\n(including IT, Architects, Data and Business Actors)",
    "label_zh": "C-MDM 运营团队（含 IT、架构师、数据与业务参与者）",
    "type": "organization_unit",
    "parent": "band_operational",
    "level": 2
  },
  {
    "id": "st_data_owner",
    "label_en": "Customer Data Owner",
    "label_zh": "客户数据所有者",
    "type": "role",
    "parent": "band_operational",
    "level": 2
  },
  {
    "id": "st_product_owner",
    "label_en": "C-MDM Product Owner",
    "label_zh": "C-MDM 产品负责人",
    "type": "role",
    "parent": "band_operational",
    "level": 2
  },
  {
    "id": "band_high_level",
    "label_en": "High-Level Management and Sponsorship",
    "label_zh": "高层管理与赞助",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 3
  },
  {
    "id": "st_cdo",
    "label_en": "Chief Data Officer (CDO)",
    "label_zh": "首席数据官（CDO）",
    "type": "role",
    "parent": "band_high_level",
    "level": 2
  },
  {
    "id": "st_cto",
    "label_en": "Chief Technology Officer (CTO)",
    "label_zh": "首席技术官（CTO）",
    "type": "role",
    "parent": "band_high_level",
    "level": 2
  },
  {
    "id": "st_hr_change",
    "label_en": "Human Resources/Change Leader",
    "label_zh": "人力资源/变革负责人",
    "type": "role",
    "parent": "band_high_level",
    "level": 2
  },
  {
    "id": "st_process_owners",
    "label_en": "Business Process Owners",
    "label_zh": "业务流程所有者",
    "type": "role",
    "parent": "band_high_level",
    "level": 2
  },
  {
    "id": "st_ceo",
    "label_en": "Chief Executive Officer (CEO)",
    "label_zh": "首席执行官（CEO）",
    "type": "role",
    "parent": "band_high_level",
    "level": 2,
    "position": "底部横贯整行"
  }
]
```

## 图例

```json
[
  {
    "symbol": "三条水平虚线",
    "meaning_zh": "分隔外部 / 运营 / 高层三个干系人层级",
    "explicit": false
  },
  {
    "symbol": "每带左侧的右向三角形",
    "meaning_zh": "层级/位置标记，指示该带干系人相对组织边界的位置",
    "explicit": false
  },
  {
    "symbol": "圆角矩形框",
    "meaning_zh": "一个干系人角色或群体",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "三条水平带自上而下：External（4 框）、Operational Management and Team（上排 2 个细框、下排 2 个框）、High-Level Management and Sponsorship（上排 4 框、下排 CEO 横贯整行）；每带左侧为带名 + 右向三角形，带间以虚线分隔。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig3-1",
    "relation": "related",
    "note_zh": "本图的 C-MDM 运营团队（含 IT、架构师、数据与业务参与者）与客户数据所有者，对应图 3-1 中 C-MDM Team 的参与者群体。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "左侧三角形标记的确切含义原图未说明，本分析按“层级/位置标记”理解。",
    "外部干系人（客户、监管机构）与组织的关系未画线，具体互动方式需结合正文与图 3-1。"
  ],
  "analyzed_from": [
    "英文 PDF 第 30 页原图截图",
    "英文 PDF 第 29–30 页正文",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 317、328、334–353 行",
    "figs/zh/g21be_fig4-1_zh.png 中文化图"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
