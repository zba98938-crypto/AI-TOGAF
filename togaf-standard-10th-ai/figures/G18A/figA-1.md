# G18A/figA-1 · 业务模型画布

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/figA-1.md) · [JSON](../../architecture/diagrams/G18A/figA-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 29 页

![英文原图](../assets/G18A/figA-1-p0029.png)

PDF 坐标：`[48.2, 36.0, 563.8, 350.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
=
—
A
Z
+
ie,
SRA
ik
ME
er}
Key
Key
ae
Partnerships | Activities
Value
Customer
Propositions | Relationships
ustomer
Segments
A
Key
SF
Channels
Resources
hm
Cost Structures
J=}]
Revenue Streams
oe
SF
Ne
```

## 概要（历史解释；局部修正见上）

用一张标准九宫格画布界定业务模型的九个构建块及其位置。

## 目的（历史解释；局部修正见上）

在附录 A 给出业务模型画布的标准结构与九块名称，配合正文逐条定义，作为第 7 章零售案例与全书业务模型表述的参照框架。

## 阅读顺序（历史解释；局部修正见上）

按画布布局读：中列 Value Propositions；向右上 Customer Relationships、右下 Channels、最右 Customer Segments；向左 Key Partnerships，其右上 Key Activities、右下 Key Resources；底部左 Cost Structures、右 Revenue Streams。每块左上角是块名，右侧配一幅线描小图。图中没有条目文字，具体内容需回到正文九条定义。

## 关键含义（历史解释；局部修正见上）

- 九个构建块：Key Partnerships、Key Activities、Value Propositions、Customer Relationships、Customer Segments、Key Resources、Channels、Cost Structures、Revenue Streams。
- 版式是标准画布：上半五列，其中关键合作伙伴、价值主张、客户细分三块通高，关键活动/关键资源与客户关系/渠道分别上下叠放；下半为成本结构与收入来源两段。
- 与图 2-4 的用词不同：此处为 Key Partnerships（复数）、Cost Structures（复数）、Customer Segments；图 2-4 用手绘版 Key Partners、Costs、Customers。
- 每块内只有一幅线描小图（戒指、挖掘机、礼盒、心形、人物、木箱、卡车、票据、收银机），仅作视觉提示，不承载信息。
- 画布内没有任何条目、数字或箭头，只有块名；这是一张结构定义图，不是某个企业的实例。
- 中文稿附录 A 正文按客户细分、价值主张、渠道、客户关系、收入来源、关键资源、关键活动、关键合作伙伴、成本结构的顺序逐条给出定义。

## 层级（历史解释；局部修正见上）

两层：外层画布框下分九个构建块，块内不再分层（只有块名与插画）。九个块并列，其中三块通高、四块两两上下叠放、两块位于底部。

## 线条含义（历史解释；局部修正见上）

图中没有箭头或关系连线，只有分隔九个块用的直线。块的相邻与上下叠放表达画布的标准布局，不表示流程或依赖方向。

## 易误读点（历史解释；局部修正见上）

- 不要把图 A-1 与图 2-4 当成同一张图：图 A-1 是平面九宫格（Key Partnerships / Customer Segments / Cost Structures / Revenue Streams），图 2-4 是手绘透视图（Key Partners / Customers / Costs / Revenue）。
- 不要从块内的线描小图推断该块的具体内容，它们只是装饰性提示。
- 不要把九个块读成流程步骤；画布是同时成立的结构。
- 中文稿第 337 行图 A-1 复用了图 2-4 的 SVG，但两张英文原图并不相同，不能据该 SVG 判断图 A-1 的原貌。

## 元素

```json
[
  {
    "id": "canvas",
    "label_en": null,
    "label_zh": "业务模型画布（无标题外框）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "整张画布"
  },
  {
    "id": "kp",
    "label_en": "Key Partnerships",
    "label_zh": "关键合作伙伴",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 1 列，通高",
    "description_zh": "块内画有一对相扣的圆环。"
  },
  {
    "id": "ka",
    "label_en": "Key Activities",
    "label_zh": "关键活动",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 2 列上半",
    "description_zh": "块内画有一人操作挖掘机。"
  },
  {
    "id": "kr",
    "label_en": "Key Resources",
    "label_zh": "关键资源",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 2 列下半",
    "description_zh": "块内画有一人守着木箱。"
  },
  {
    "id": "vp",
    "label_en": "Value Propositions",
    "label_zh": "价值主张",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 3 列，通高",
    "description_zh": "块内画有一个系缎带的礼盒。"
  },
  {
    "id": "cr",
    "label_en": "Customer Relationships",
    "label_zh": "客户关系",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 4 列上半",
    "description_zh": "块内画有一颗心。"
  },
  {
    "id": "ch",
    "label_en": "Channels",
    "label_zh": "渠道",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 4 列下半",
    "description_zh": "块内画有一辆厢式货车。"
  },
  {
    "id": "cs",
    "label_en": "Customer Segments",
    "label_zh": "客户细分",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 5 列，通高",
    "description_zh": "块内画有一个站立的人。"
  },
  {
    "id": "cost",
    "label_en": "Cost Structures",
    "label_zh": "成本结构",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "底部左段",
    "description_zh": "块内画有一张带线条的票据。"
  },
  {
    "id": "rev",
    "label_en": "Revenue Streams",
    "label_zh": "收入来源",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "底部右段",
    "description_zh": "块内画有一台收银机。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_vp_cs",
    "from": "vp",
    "to": "cs",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "版式隐含：价值主张列紧邻客户细分区，表示价值主张面向客户细分；图中无连线。"
  },
  {
    "id": "r_ch_cs",
    "from": "ch",
    "to": "cs",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "版式隐含：渠道位于客户细分左侧，表示触达客户的途径；图中无连线。"
  },
  {
    "id": "r_kp_ka",
    "from": "kp",
    "to": "ka",
    "type": "dependency",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "版式隐含：关键合作伙伴紧邻关键活动，表示伙伴支撑活动；图中无连线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅灰底 + 细黑分隔线",
    "meaning_zh": "业务模型画布及其九个区块",
    "explicit": false
  },
  {
    "symbol": "块名（蓝色粗体）",
    "meaning_zh": "构建块名称",
    "explicit": false
  },
  {
    "symbol": "块内线描小图",
    "meaning_zh": "该构建块的视觉提示，无编码含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "一个带细黑边框的浅灰画布：上部五列，第 1 列 Key Partnerships 通高，第 2 列上 Key Activities、下 Key Resources，第 3 列 Value Propositions 通高，第 4 列上 Customer Relationships、下 Channels，第 5 列 Customer Segments 通高；底部横条左侧 Cost Structures、右侧 Revenue Streams。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig2-4",
    "relation": "variant_of",
    "note_zh": "同一画布的平面九宫格版（本图）与手绘插画版（图 2-4）；块名用词不同"
  },
  {
    "target": "G18A/fig7-1",
    "relation": "generalizes",
    "note_zh": "图 7-1 是本画布在零售企业现状中的实例"
  },
  {
    "target": "G18A/fig7-2",
    "relation": "generalizes",
    "note_zh": "图 7-2 是本画布在零售企业未来态中的实例"
  },
  {
    "target": "G18A/fig4-1",
    "relation": "related",
    "note_zh": "图 4-1 的业务模型区使用本画布的九个构建块名称，排成 3×3"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "画布本身没有标题，图题仅写在图注中；是否应把“Figure A-1”视为画布标题，图中无法判断。",
    "块内线描小图是否对应特定隐喻（如戒指=伙伴关系、心=关系），原图未注释。",
    "原图使用 Cost Structures 复数形式，中文稿统一译为“成本结构”，不复数化。"
  ],
  "analyzed_from": [
    "英文 PDF 第 29 页原图截图（figA-1_p29_1.png，1240 px 宽，块名可直接辨读）",
    "英文 PDF 第 28–29 页正文",
    "中文稿 G18Ae_业务模型.md 第 315–337 行",
    "figs/g18a_fig2-4.svg 源码与 SVG 文本（中文稿为图 A-1 复用该资产）"
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
