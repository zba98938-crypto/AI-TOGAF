# G188/fig3-2 · 基于 PRINCE2 方法的项目管理团队简化图

> 当前图示解析：[Markdown](../../architecture/diagrams/G188/fig3-2.md) · [JSON](../../architecture/diagrams/G188/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G188e.pdf`；SHA-256：`6e654af12a0bc034c7548d425a01123331ac9129c478a0bb957db89dd353dd29`。

## 原图 · PDF 第 40 页

![英文原图](../assets/G188/fig3-2-p0040.png)

PDF 坐标：`[48.2, 292.4, 563.8, 538.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
weeeensecces:
a
woveweoes
weceeeey
Project Management Team
Covered in “Governance
Governance
in Architecture Projects:
Covered in “Project
Project Support
Manager's Support in
Covered in “Project
Team-evel
Architecture Projects”
Manager's Support in
»
Management
Architecture Projects”
a
a
a
ee
Covered in “Delivery Team
Delivery
in Architecture Projects:
```

## 概要（历史解释；局部修正见上）

PRINCE2 的项目管理团队由治理、项目管理、团队级管理和项目支持四部分组成，交付团队在其外。

## 目的（历史解释；局部修正见上）

用一张简化结构图说明项目经理并非独自工作：PRINCE2 的项目管理团队包含治理机构、项目管理、团队级管理与项目支持；并标出本文档哪几节分别覆盖这些部分，帮助架构师把团队角色对应到本指南章节。

## 阅读顺序（历史解释；局部修正见上）

先看虚线大框“Project Management Team”：框内左上为 Governance，左中为 Project Management，左下为 Team-level Management，右侧大块为 Project Support。再看框外下方的 Delivery，它不属于项目管理团队。最后读三组带箭头的说明文字：左上箭头指向 Governance，左下箭头指向 Team-level Management，右侧箭头指向 Project Support，分别说明这些部分在本指南哪一节讲述。

## 关键含义（历史解释；局部修正见上）

- PRINCE2 的“项目管理团队”是完整的项目管理结构，包含负责治理、管理与支持的机构，不等同于“项目团队”。
- Governance（治理）位于团队结构顶端，对应本指南“架构项目中的治理”一节；在 PRINCE2 中由指导委员会/执行发起人领导，在 TOGAF 中对应架构委员会。
- Project Management（项目管理）是项目经理直接负责的管理活动层，位于治理之下、团队级管理之上。
- Team-level Management（团队级管理）由团队经理承担，负责按项目工作包交付产品；对应本指南“项目经理的支持”一节。
- Project Support（项目支持）通常由项目管理办公室（PMO）承担，提供行政与运营支持及工具技术指导，也归入“项目经理的支持”一节。
- Delivery（交付）在虚线框之外，是实际执行架构工作的人员，对应本指南“架构项目中的交付团队”一节。
- 与 PMBOK 相比，PRINCE2 的项目管理团队明确包含治理机构；PMBOK 的项目管理团队只限管理与领导活动，治理由发起人/指导委员会在团队之外提供。

## 层级（历史解释；局部修正见上）

三层：最外是项目治理（Governance）；中间是项目管理（Project Management）；其下是团队级管理（Team-level Management）与项目支持（Project Support），二者并列。交付（Delivery）不属于项目管理团队，位于虚线框外下方，是被管理/被支持的对象。视觉上 Governance 在最上、Project Management 居中、Team-level Management 在下，Project Support 占右侧整列。

## 线条含义（历史解释；局部修正见上）

虚线大框表示“项目管理团队”的成员范围（包含关系），框内四个色块是组成部分，色块之间没有连线，上下位置只表示治理—管理—团队管理的层次。框外三条实心箭头是注释引线，不是流程：左侧两条分别指向 Governance 与 Team-level Management，右侧一条指向 Project Support，箭头表示“这一部分在本指南某节讲述”。Delivery 与虚线框之间没有连线，表示它不在团队内。

## 易误读点（历史解释；局部修正见上）

- 不要把 Delivery 算进项目管理团队：它画在虚线框外，是交付团队。
- 不要以为 Project Support 与 Team-level Management 有上下级关系：二者在图中并列，分别面向支持与团队管理。
- 不要把 Governance 理解为项目经理之上的另一个项目经理；它是治理机构（指导委员会/执行发起人，TOGAF 中为架构委员会）。
- 图中的色块大小不代表人数或工作量，只用于容纳标签。

## 元素

```json
[
  {
    "id": "pm_team",
    "label_en": "Project Management Team",
    "label_zh": "项目管理团队",
    "type": "organization_unit",
    "parent": null,
    "level": 0,
    "position": "中央虚线大框",
    "description_zh": "PRINCE2 的完整项目管理结构范围。"
  },
  {
    "id": "governance",
    "label_en": "Governance",
    "label_zh": "治理",
    "type": "organization_unit",
    "parent": "pm_team",
    "level": 1,
    "position": "虚线框内左上"
  },
  {
    "id": "project_management",
    "label_en": "Project Management",
    "label_zh": "项目管理",
    "type": "organization_unit",
    "parent": "pm_team",
    "level": 1,
    "position": "虚线框内左中"
  },
  {
    "id": "team_level_management",
    "label_en": "Team-level Management",
    "label_zh": "团队级管理",
    "type": "organization_unit",
    "parent": "pm_team",
    "level": 1,
    "position": "虚线框内左下"
  },
  {
    "id": "project_support",
    "label_en": "Project Support",
    "label_zh": "项目支持",
    "type": "organization_unit",
    "parent": "pm_team",
    "level": 1,
    "position": "虚线框内右侧大块"
  },
  {
    "id": "delivery",
    "label_en": "Delivery",
    "label_zh": "交付",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "position": "虚线框外正下方",
    "description_zh": "交付团队，不属于项目管理团队。"
  },
  {
    "id": "note_governance",
    "label_en": "Covered in \"Governance in Architecture Projects\"",
    "label_zh": "见“架构项目中的治理”一节",
    "type": "note",
    "parent": null,
    "position": "左侧上部"
  },
  {
    "id": "note_pm_support_left",
    "label_en": "Covered in \"Project Manager's Support in Architecture Projects\"",
    "label_zh": "见“架构项目中项目经理的支持”一节",
    "type": "note",
    "parent": null,
    "position": "左侧下部"
  },
  {
    "id": "note_pm_support_right",
    "label_en": "Covered in \"Project Manager's Support in Architecture Projects\"",
    "label_zh": "见“架构项目中项目经理的支持”一节",
    "type": "note",
    "parent": null,
    "position": "右侧中部"
  },
  {
    "id": "note_delivery",
    "label_en": "Covered in \"Delivery Team in Architecture Projects\"",
    "label_zh": "见“架构项目中的交付团队”一节",
    "type": "note",
    "parent": null,
    "position": "左下"
  }
]
```

## 关系

```json
[
  {
    "from": "pm_team",
    "to": "governance",
    "type": "composition",
    "explicit": true,
    "line": "dashed",
    "arrow": "none",
    "description_zh": "虚线框包含 Governance 色块"
  },
  {
    "from": "pm_team",
    "to": "project_management",
    "type": "composition",
    "explicit": true,
    "line": "dashed",
    "arrow": "none"
  },
  {
    "from": "pm_team",
    "to": "team_level_management",
    "type": "composition",
    "explicit": true,
    "line": "dashed",
    "arrow": "none"
  },
  {
    "from": "pm_team",
    "to": "project_support",
    "type": "composition",
    "explicit": true,
    "line": "dashed",
    "arrow": "none"
  },
  {
    "from": "note_governance",
    "to": "governance",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "说明文字用箭头指向 Governance"
  },
  {
    "from": "note_pm_support_left",
    "to": "team_level_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "note_pm_support_right",
    "to": "project_support",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "backward",
    "description_zh": "右侧说明文字在右、箭头向左指向 Project Support"
  },
  {
    "from": "note_delivery",
    "to": "delivery",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "project_management",
    "to": "governance",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "上下叠放表示项目经理接受治理机构的监督与支持"
  },
  {
    "from": "team_level_management",
    "to": "project_management",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "团队经理由项目经理指派并对其负责"
  }
]
```

## 图例

```json
[
  {
    "symbol": "虚线大框",
    "meaning_zh": "项目管理团队的范围",
    "explicit": true
  },
  {
    "symbol": "深蓝色块",
    "meaning_zh": "项目管理团队的组成部分（Governance、Team-level Management、Project Support、Delivery）",
    "explicit": false
  },
  {
    "symbol": "浅灰蓝色块",
    "meaning_zh": "Project Management（项目经理的管理活动层）",
    "explicit": false
  },
  {
    "symbol": "框外色块",
    "meaning_zh": "不属于项目管理团队（Delivery）",
    "explicit": false
  },
  {
    "symbol": "实心箭头引线",
    "meaning_zh": "把说明文字指向被说明的部分",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "画面中央是一个虚线大矩形，标题 Project Management Team 在框顶。框内左列自上而下为 Governance、Project Management、Team-level Management 三个色块；右列是一个更高的 Project Support 色块。框外正下方是 Delivery 色块。左侧两段说明文字分别用右向箭头指向 Governance 与 Team-level Management；右侧一段说明文字用左向箭头指向 Project Support。"
}
```

## 相关图

```json
[
  {
    "target": "G188/fig4-1",
    "relation": "complements",
    "note_zh": "图 4-1 说明 PRINCE2 流程如何映射到 ADM，本图说明执行这些流程的项目管理团队由哪些部分组成"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图为纯色块，Project Management 与其余三块颜色略有差异（浅灰蓝 vs 深蓝），图中无图例，此处按色差推断项目管理层为独立一层，未赋予额外含义。",
    "左侧下方箭头在视觉上落在 Project Management 与 Team-level Management 之间，本文按文字“Project Manager's Support”判为指向 Team-level Management；Project Support 也由同一节覆盖。"
  ],
  "analyzed_from": [
    "英文 PDF 第 40 页原图截图（含 3x3 放大分块）",
    "英文 PDF 第 40 页正文",
    "中文稿 G188e_架构项目管理.md 第 454–517 行",
    "figs/g188e_fig3-2_en.png"
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
