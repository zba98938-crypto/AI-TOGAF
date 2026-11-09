# G234/fig4-2 · 元数据需求收集示意

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-2.md) · [JSON](../../architecture/diagrams/G234/fig4-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 24 页

![英文原图](../assets/G234/fig4-2-p0024.png)

PDF 坐标：`[61.1, 36.0, 550.9, 296.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Top down
‘Supportfegulatory
gs
Improve operational
Reduce environmental
Improve accessibility
compliance and meet
footprints
efficiency of business
to datato increase
internalcontrol
functionsand increase
businessvalue
requirements
confidencein data
Business Use-Cases
Compliance
Define
Define
metadata req
NN
metadata req
orana
use-cases
Define
metadata req
Define metadata
Support
to generate
ipply metadata
req. for impact
businessdata
business value
ee.
69.
on dataset
analysis
WN
issue resolution
Data Set
Business Data Issue
Documentexisting data sets to democratize
Use a business data issue as an opportunity
accessto the data and generate more value
to define metadata requirements to support
forthe business
the issue resolution
Bottom up
```

## 概要（历史解释；局部修正见上）

自上而下（合规/业务用例）与自下而上（数据集/业务数据问题）两条路径，最终都汇入同一组元数据需求。

## 目的（历史解释；局部修正见上）

展示收集元数据需求的四个起点与两条总体方向，并强调每种起点都不是单向索取：需求要被定义出来，也要被应用回数据集、业务用例或数据问题，才能产生价值。

## 阅读顺序（历史解释；局部修正见上）

左半读自上而下：Compliance 与 Business Use-Cases 在上，各自上方有两张驱动/收益卡；右半读自下而上：Data Set 与 Business Data Issue 在下，各带一张米色做法说明。中央 Metadata Requirements 是汇聚点。每条箭头旁的文字说明动作方向，箭头指向即动作的宾语。

## 关键含义（历史解释；局部修正见上）

- 四类起点：合规要求、业务用例（自上而下）；数据集、业务数据问题（自下而上）。
- 合规由两类驱动支撑：支持监管合规与内控、减少环境足迹；业务用例由两类收益支撑：提升业务功能运营效率与数据信心、提升数据可访问性以增加业务价值。
- Compliance → Metadata Requirements 是单向箭头（Define metadata req.）：合规要求直接推导元数据需求，不再回写。
- Business Use-Cases、Data Set、Business Data Issue 与中央节点之间都是双向箭头：既定义需求，也把需求应用回起点（Link data to use-cases、Apply metadata req. on data set、Support business data issue resolution）。
- 左右两条长箭头 Top down（向下）与 Bottom up（向上）方向相反，但终点都是同一组元数据需求，说明两条路径可并存。
- 底部两张米色卡给出自下而上的具体做法：为现有数据集建档以民主化访问并产生业务价值；把业务数据问题当作定义需求、支持问题解决的机会。

## 层级（历史解释；局部修正见上）

两条方法路径（Top down / Bottom up）各自包含两个起点；中央 Metadata Requirements 不隶属于任何一条路径，而是四个起点的共同汇聚点。驱动卡属于合规，收益卡属于业务用例。

## 线条含义（历史解释；局部修正见上）

实线箭头 + 文字标签表示动作方向：箭头指向中央表示“定义/推导需求”，箭头指回起点表示“把需求应用/链接/支撑到该场景”。两条长箭头只表示方法走向，不是数据流。

## 易误读点（历史解释；局部修正见上）

- 不要把四条连线都读成单向；只有 Compliance 是单向，其余三条是双向。
- 不要把 Top down / Bottom up 两条长箭头当成数据流或流程步骤，它们是方法方向的标识。
- 不要把业务用例上方的两张卡当成两个额外的起点，它们是业务用例的收益说明。
- 中文稿 SVG 只是两段要点清单，没有中央节点和箭头，不能据它理解各起点的指向。

## 元素

```json
[
  {
    "id": "metadata_requirements",
    "label_en": "Metadata Requirements",
    "label_zh": "元数据需求",
    "type": "requirement",
    "parent": null,
    "level": 1,
    "position": "图中央",
    "description_zh": "四个起点共同指向的需求集合。"
  },
  {
    "id": "compliance",
    "label_en": "Compliance",
    "label_zh": "合规",
    "type": "goal",
    "parent": null,
    "level": 1,
    "position": "左上"
  },
  {
    "id": "card_regulatory",
    "label_en": "Support regulatory compliance and meet internal control requirements",
    "label_zh": "支持监管合规并满足内控要求",
    "type": "goal",
    "parent": null,
    "level": 2,
    "position": "Compliance 上方左卡"
  },
  {
    "id": "card_footprint",
    "label_en": "Reduce environmental footprints",
    "label_zh": "减少环境足迹",
    "type": "goal",
    "parent": null,
    "level": 2,
    "position": "Compliance 上方右卡"
  },
  {
    "id": "business_use_cases",
    "label_en": "Business Use-Cases",
    "label_zh": "业务用例",
    "type": "capability",
    "parent": null,
    "level": 1,
    "position": "右上"
  },
  {
    "id": "card_efficiency",
    "label_en": "Improve operational efficiency of business functions and increase confidence in data",
    "label_zh": "提升业务功能运营效率并增强对数据的信心",
    "type": "goal",
    "parent": null,
    "level": 2,
    "position": "Business Use-Cases 上方左卡"
  },
  {
    "id": "card_accessibility",
    "label_en": "Improve accessibility to data to increase business value",
    "label_zh": "提升数据可访问性以增加业务价值",
    "type": "goal",
    "parent": null,
    "level": 2,
    "position": "Business Use-Cases 上方右卡"
  },
  {
    "id": "data_set",
    "label_en": "Data Set",
    "label_zh": "数据集",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左下"
  },
  {
    "id": "note_data_set",
    "label_en": "Document existing data sets to democratize access to the data and generate more value for the business",
    "label_zh": "为现有数据集建档，以民主化数据访问并为业务创造更多价值",
    "type": "note",
    "parent": null,
    "level": 2,
    "position": "Data Set 下方米色卡"
  },
  {
    "id": "business_data_issue",
    "label_en": "Business Data Issue",
    "label_zh": "业务数据问题",
    "type": "risk",
    "parent": null,
    "level": 1,
    "position": "右下"
  },
  {
    "id": "note_issue",
    "label_en": "Use a business data issue as an opportunity to define metadata requirements to support the issue resolution",
    "label_zh": "把业务数据问题作为定义元数据需求、支持问题解决的机会",
    "type": "note",
    "parent": null,
    "level": 2,
    "position": "Business Data Issue 下方米色卡"
  },
  {
    "id": "ind_top_down",
    "label_en": "Top down",
    "label_zh": "自上而下",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "最左侧竖直长箭头旁"
  },
  {
    "id": "ind_bottom_up",
    "label_en": "Bottom up",
    "label_zh": "自下而上",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "最右侧竖直长箭头旁"
  }
]
```

## 关系

```json
[
  {
    "from": "compliance",
    "to": "metadata_requirements",
    "type": "produces",
    "label_en": "Define metadata req.",
    "label_zh": "定义元数据需求",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "business_use_cases",
    "to": "metadata_requirements",
    "type": "produces",
    "label_en": "Define metadata req.",
    "label_zh": "定义元数据需求",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "metadata_requirements",
    "to": "business_use_cases",
    "type": "maps_to",
    "label_en": "Link data to use-cases",
    "label_zh": "把数据关联到用例",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "data_set",
    "to": "metadata_requirements",
    "type": "produces",
    "label_en": "Define metadata req. to generate business value",
    "label_zh": "定义元数据需求以产生业务价值",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "metadata_requirements",
    "to": "data_set",
    "type": "governs",
    "label_en": "Apply metadata req. on data set",
    "label_zh": "在数据集上应用元数据需求",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "business_data_issue",
    "to": "metadata_requirements",
    "type": "produces",
    "label_en": "Define metadata req. for impact analysis",
    "label_zh": "为影响分析定义元数据需求",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "metadata_requirements",
    "to": "business_data_issue",
    "type": "serving",
    "label_en": "Support business data issue resolution",
    "label_zh": "支持业务数据问题解决",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "ind_top_down",
    "to": "data_set",
    "type": "other",
    "label_en": "Top down",
    "label_zh": "自上而下",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "最左侧长箭头从顶部贯穿到底部、箭头朝下，仅表示自上而下的方法方向，不是实体间依赖。"
  },
  {
    "from": "ind_bottom_up",
    "to": "business_use_cases",
    "type": "other",
    "label_en": "Bottom up",
    "label_zh": "自下而上",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "最右侧长箭头从底部向上、箭头朝上，仅表示自下而上的方法方向。"
  },
  {
    "from": "card_regulatory",
    "to": "compliance",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "驱动卡位于 Compliance 正上方，无连线。"
  },
  {
    "from": "card_footprint",
    "to": "compliance",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "驱动卡位于 Compliance 正上方，无连线。"
  },
  {
    "from": "card_efficiency",
    "to": "business_use_cases",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "收益卡位于 Business Use-Cases 正上方，无连线。"
  },
  {
    "from": "card_accessibility",
    "to": "business_use_cases",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "收益卡位于 Business Use-Cases 正上方，无连线。"
  },
  {
    "from": "note_data_set",
    "to": "data_set",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "说明卡位于 Data Set 正下方，无连线。"
  },
  {
    "from": "note_issue",
    "to": "business_data_issue",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "说明卡位于 Business Data Issue 正下方，无连线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "青绿色实线箭头 + 文字",
    "meaning_zh": "元数据需求的定义或应用动作，箭头指向动作用语的对象",
    "explicit": false
  },
  {
    "symbol": "左侧向下长箭头 Top down",
    "meaning_zh": "自上而下的需求收集路径",
    "explicit": true
  },
  {
    "symbol": "右侧向上长箭头 Bottom up",
    "meaning_zh": "自下而上的需求收集路径",
    "explicit": true
  },
  {
    "symbol": "米色说明卡",
    "meaning_zh": "该起点的具体做法说明",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "左右两组：左上 Compliance 与右上 Business Use-Cases（各带两张上方卡片），中央 Metadata Requirements 横贯中线，左下 Data Set 与右下 Business Data Issue（各带一张下方说明卡）；最左一条向下长箭头，最右一条向上长箭头。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-1",
    "relation": "follows",
    "note_zh": "图 4-1 先列元数据来源与域，图 4-2 再从这些来源中收集需求"
  },
  {
    "target": "G234/fig4-3",
    "relation": "precedes",
    "note_zh": "需求收集完成后，图 4-3 定义保障元数据质量的两种流程模式"
  },
  {
    "target": "G234/fig4-5",
    "relation": "related",
    "note_zh": "需求最终落实为图 4-5 的关键元数据资产清单"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "Business Use-Cases 与 Metadata Requirements 之间的两条箭头几乎平行，2x 截图可辨认箭头指向，但两条线的起止点略有交叠。",
    "四张驱动/收益卡与下方方框之间没有画线，只能按版式判断归属。"
  ],
  "analyzed_from": [
    "英文 PDF 第 24 页原图截图（2x2 放大分块）",
    "英文 PDF 第 23–24 页正文",
    "中文稿 G234e_信息架构_元数据管理.md 第 234–251 行",
    "figs/g234_fig4-2.svg 源码"
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
