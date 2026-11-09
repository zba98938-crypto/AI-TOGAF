# G18A/fig2-1 · 业务模型的抽象视图

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/fig2-1.md) · [JSON](../../architecture/diagrams/G18A/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 13 页

![英文原图](../assets/G18A/fig2-1-p0013.png)

PDF 坐标：`[99.8, 207.4, 512.2, 451.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
fe}
Customer
perating Model
Capability D
Experience
Capability C
Targets
Segmentation
Capability B
Experience Mapping
Capability A
=
Unmet Need
Value Proposition
create
O
deliver
C
Z
aN
x)
a
$
$
Financial Model
(Revenue, Pricing, Costs, Capital)
capture
```

## 概要（历史解释；局部修正见上）

以运营模式、客户体验、财务模型三要素及创造/交付/获取三个动作，给出业务模型最抽象的结构。

## 目的（历史解释；局部修正见上）

为第 2 节的业务模型定义提供最简骨架：说明业务模型是「创造价值—交付价值—获取价值」的整体逻辑，而不只是一张收入表；随后图 2-2、2-3、2-4 给出更具体的框架与画布。

## 阅读顺序（历史解释；局部修正见上）

先看外框：它圈定「业务模型」这一整体。左侧 Operating Model 旁标 create，右侧 Customer Experience 旁标 deliver，底部横贯的 Financial Model 下方标 capture；三块之间各有一条粗双向箭头。再看内部：Operating Model 中四张卡片从前到后叠放，最前的 Capability A 内有 People、Process、Technology 三个交叠圆；Customer Experience 的标题栏下纵向列出五个关注点；Financial Model 的标题栏下是四项财务组成。

## 关键含义（历史解释；局部修正见上）

- 三块分别对应价值创造（运营模式）、价值交付（客户体验）、价值获取（财务模型），它们是业务模型的三个侧面，不是三个部门或三个步骤。
- create / deliver / capture 是标注三个区域的动作词，位于外框之外，图中没有箭头把它们串成流程。
- 客户体验被拆成 Targets、Segmentation、Experience Mapping、Unmet Need、Value Proposition 五个关注点，说明交付侧从客户细分与未满足需求出发。
- 财务模型由 Revenue、Pricing、Costs、Capital 四类构成，既含收入与定价，也含成本与资本投入。
- 运营模式用四张叠放卡片表示存在多项能力；最前一张 Capability A 内的 People、Process、Technology 三圆交叠，表示能力由人员、流程、技术共同构成。
- 三块之间全部是粗双向箭头，表示相互制约与反馈：运营模式影响客户体验与财务结果，财务约束又反过来限制前两者。
- 本图刻意不含组织、流程步骤或指标，正文称其为业务模型「最抽象」的表示；更具体的制品才定义结构要素及其关系。

## 层级（历史解释；局部修正见上）

外框（业务模型整体）之下是三个并列的一级要素：Operating Model、Customer Experience、Financial Model。Operating Model 之下是多个 Capability（图中以 D、C、B、A 四张叠放卡示意），Capability A 之下是 People、Process、Technology 三个交叠成分。Customer Experience 与 Financial Model 之下是各自的关注点/组成项。三块之间是相互作用关系，不是上下级。

## 线条含义（历史解释；局部修正见上）

图中只有三条粗双向箭头：Operating Model ↔ Customer Experience、Operating Model ↔ Financial Model、Customer Experience ↔ Financial Model，均表示双向影响，没有起点终点。外框是边界线，不表示关系。四张能力卡之间、三个交叠圆之间没有连线，叠放与交叠本身表达「多个能力」「三者共同构成」。

## 易误读点（历史解释；局部修正见上）

- 不要把 create → deliver → capture 读成先后三步：图中没有任何箭头把它们连起来，三者是同时成立的三项功能。
- 不要把 Capability D/C/B/A 理解为从低到高的四级能力：它们只是四张叠放卡片，A 在最前是为了展示其内部结构。
- 不要以为 Financial Model 画在底部就只是「结果」：它与另外两块是并列要素，箭头是双向的。
- 不要把 People、Process、Technology 三圆交叠当成三个部门的重叠；它表示一项能力的三个构成成分。
- 中文稿第 93 行引用的 figs/g18a_fig2-1.svg 是三圆链示意，与本图不是同一结构，不能据它理解本图。

## 元素

```json
[
  {
    "id": "bm_frame",
    "label_en": null,
    "label_zh": "业务模型整体（无标题外框）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "全图外框",
    "description_zh": "细黑矩形边框，圈定三块要素；图中没有标题。"
  },
  {
    "id": "create",
    "label_en": "create",
    "label_zh": "创造（价值）",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "外框左侧中部，与 Operating Model 齐平",
    "description_zh": "标注运营模式所做的动作，不是流程节点。"
  },
  {
    "id": "deliver",
    "label_en": "deliver",
    "label_zh": "交付（价值）",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "外框右侧中部，与 Customer Experience 齐平",
    "description_zh": "标注客户体验所做的动作。"
  },
  {
    "id": "capture",
    "label_en": "capture",
    "label_zh": "获取（价值）",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "外框下方中部",
    "description_zh": "标注财务模型所做的动作。"
  },
  {
    "id": "op_model",
    "label_en": "Operating Model",
    "label_zh": "运营模式",
    "type": "group",
    "parent": "bm_frame",
    "level": 1,
    "position": "框内左上，最大的面板",
    "description_zh": "标题栏下有横线，内部为叠放的能力卡。"
  },
  {
    "id": "capability_d",
    "label_en": "Capability D",
    "label_zh": "能力 D",
    "type": "capability",
    "parent": "op_model",
    "level": 2,
    "position": "最靠后的一张卡，仅露出顶部",
    "description_zh": "叠放卡片中的一张，原图未说明 D 的含义。"
  },
  {
    "id": "capability_c",
    "label_en": "Capability C",
    "label_zh": "能力 C",
    "type": "capability",
    "parent": "op_model",
    "level": 2,
    "position": "由后向前第三张",
    "description_zh": "叠放卡片中的一张。"
  },
  {
    "id": "capability_b",
    "label_en": "Capability B",
    "label_zh": "能力 B",
    "type": "capability",
    "parent": "op_model",
    "level": 2,
    "position": "由后向前第二张",
    "description_zh": "叠放卡片中的一张。"
  },
  {
    "id": "capability_a",
    "label_en": "Capability A",
    "label_zh": "能力 A",
    "type": "capability",
    "parent": "op_model",
    "level": 2,
    "position": "最前一张卡，遮住其余三张大部",
    "description_zh": "唯一展示内部结构的能力卡。"
  },
  {
    "id": "people",
    "label_en": "People",
    "label_zh": "人员",
    "type": "actor",
    "parent": "capability_a",
    "level": 3,
    "position": "能力 A 内左上方圆",
    "description_zh": "三圆之一，与 Process、Technology 交叠。"
  },
  {
    "id": "process",
    "label_en": "Process",
    "label_zh": "流程",
    "type": "process",
    "parent": "capability_a",
    "level": 3,
    "position": "能力 A 内右上方圆",
    "description_zh": "三圆之一。"
  },
  {
    "id": "technology",
    "label_en": "Technology",
    "label_zh": "技术",
    "type": "technology",
    "parent": "capability_a",
    "level": 3,
    "position": "能力 A 内下方圆",
    "description_zh": "三圆之一。"
  },
  {
    "id": "cx",
    "label_en": "Customer Experience",
    "label_zh": "客户体验",
    "type": "group",
    "parent": "bm_frame",
    "level": 1,
    "position": "框内右上，窄长面板",
    "description_zh": "标题栏下有横线，下面纵向列出五个关注点。"
  },
  {
    "id": "cx_targets",
    "label_en": "Targets",
    "label_zh": "目标客户",
    "type": "concept",
    "parent": "cx",
    "level": 2,
    "order": 1,
    "position": "客户体验列表第 1 行"
  },
  {
    "id": "cx_segmentation",
    "label_en": "Segmentation",
    "label_zh": "客户细分",
    "type": "concept",
    "parent": "cx",
    "level": 2,
    "order": 2,
    "position": "第 2 行"
  },
  {
    "id": "cx_mapping",
    "label_en": "Experience Mapping",
    "label_zh": "体验映射",
    "type": "concept",
    "parent": "cx",
    "level": 2,
    "order": 3,
    "position": "第 3 行"
  },
  {
    "id": "cx_unmet_need",
    "label_en": "Unmet Need",
    "label_zh": "未满足需求",
    "type": "concept",
    "parent": "cx",
    "level": 2,
    "order": 4,
    "position": "第 4 行"
  },
  {
    "id": "cx_value_prop",
    "label_en": "Value Proposition",
    "label_zh": "价值主张",
    "type": "concept",
    "parent": "cx",
    "level": 2,
    "order": 5,
    "position": "第 5 行"
  },
  {
    "id": "fin_model",
    "label_en": "Financial Model",
    "label_zh": "财务模型",
    "type": "group",
    "parent": "bm_frame",
    "level": 1,
    "position": "框内底部横条",
    "description_zh": "标题栏下有横线，其下是四项财务组成。"
  },
  {
    "id": "fin_items",
    "label_en": "(Revenue, Pricing, Costs, Capital)",
    "label_zh": "（收入、定价、成本、资本）",
    "type": "concept",
    "parent": "fin_model",
    "level": 2,
    "position": "财务模型标题栏下方",
    "description_zh": "原图以括号形式并列四项。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_op_cx",
    "from": "op_model",
    "to": "cx",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "粗双向箭头：运营模式与客户体验相互影响（创造什么、如何交付）。"
  },
  {
    "id": "r_op_fin",
    "from": "op_model",
    "to": "fin_model",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "粗双向箭头：运营模式与财务模型相互约束。"
  },
  {
    "id": "r_cx_fin",
    "from": "cx",
    "to": "fin_model",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "粗双向箭头：客户体验与财务模型相互影响（体验设计影响收入与成本）。"
  },
  {
    "id": "r_create_op",
    "from": "create",
    "to": "op_model",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "仅靠位置表达：create 标注运营模式。"
  },
  {
    "id": "r_deliver_cx",
    "from": "deliver",
    "to": "cx",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "仅靠位置表达：deliver 标注客户体验。"
  },
  {
    "id": "r_capture_fin",
    "from": "capture",
    "to": "fin_model",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "仅靠位置表达：capture 标注财务模型。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "细黑外框",
    "meaning_zh": "业务模型的整体边界（图中无标题）",
    "explicit": false
  },
  {
    "symbol": "浅蓝带标题栏的面板",
    "meaning_zh": "业务模型的一个要素（运营模式/客户体验/财务模型）",
    "explicit": false
  },
  {
    "symbol": "四张由后向前叠放的卡片",
    "meaning_zh": "运营模式下的多项业务能力",
    "explicit": false
  },
  {
    "symbol": "三个交叠的圆",
    "meaning_zh": "一项能力由人员、流程、技术共同构成",
    "explicit": false
  },
  {
    "symbol": "粗深灰双向箭头",
    "meaning_zh": "两个要素之间的双向影响/相互作用",
    "explicit": false
  },
  {
    "symbol": "外框外的 create / deliver / capture",
    "meaning_zh": "对三个区域所做动作的标注（创造/交付/获取）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "一个细黑外框内：左上为较大的 Operating Model 面板，右上为较窄的 Customer Experience 面板，底部为横贯两列的 Financial Model 长条；外框左侧、右侧、下方分别写 create、deliver、capture。三个面板之间共三条粗双向箭头（水平一条、竖直两条）。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig2-2",
    "relation": "complements",
    "note_zh": "正文并列介绍：图 2-2 的四框框架是同一业务模型概念的另一著名表示"
  },
  {
    "target": "G18A/fig2-3",
    "relation": "complements",
    "note_zh": "正文并列介绍：图 2-3 的业务模型立方体以多维方式表示同一概念"
  },
  {
    "target": "G18A/fig2-4",
    "relation": "complements",
    "note_zh": "图 2-4 的业务模型画布是本书采用的更具体表示，可视为本抽象框架的落地形式"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "Capability A–D 的排列（由后向前 D→A）是否暗示层级或先后，原图与正文均未说明；解析按「四张并列叠放卡」处理。",
    "People/Process/Technology 三圆交叠是否特指三者交集，图中未标注。",
    "Customer Experience 列表第 5 项 Value Proposition 与 Operating Model 的关系，图中未画线。",
    "Operating Model / Customer Experience / Financial Model 与 create / deliver / capture 的中文译名由解析者拟定，中文稿未给出对照。"
  ],
  "analyzed_from": [
    "英文 PDF 第 13 页原图截图（fig2-1_p13_1.png）及 2×2 放大分块 z11/z12/z22",
    "英文 PDF 第 13 页正文",
    "中文稿 G18Ae_业务模型.md 第 89–93 行",
    "figs/g18a_fig2-1.svg 源码与 SVG 文本"
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
