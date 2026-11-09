# G186/fig4-1 · 业务周期与四种架构目的的对应

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig4-1.md) · [JSON](../../architecture/diagrams/G186/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 41 页

![英文原图](../assets/G186/fig4-1-p0041.png)

PDF 坐标：`[48.2, 370.7, 563.8, 606.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Architecture to
Architecture to
Architecture to
Architecture to
Support
Support
Support
Support
Strategy
Portfolio
Project
Solution
Delivery
L
I
|
!
Budget Planning
Budget Preparation Budget Allocation
Budget Control
```

## 概要（历史解释；局部修正见上）

把四种架构目的分别对齐到预算规划、编制、分配、控制四个阶段，并强调架构在决策里程碑之前交付。

## 目的（历史解释；局部修正见上）

作者用一条简化的预算周期时间线说明 EA 必须与组织既有的预算节奏对齐：支持战略、组合、项目的架构要在对应的预算决策之前完成，支持解决方案交付的架构则围绕预算控制持续运作；核心结论是“架构先于决策”。

## 阅读顺序（历史解释；局部修正见上）

先看贯穿全图的橙色粗箭头，它表示时间从左向右流动。上方四个彩色方框是四种架构目的；下方四个文字标签是预算周期的四个阶段。每个阶段在时间轴上有一个紫色圆点（决策里程碑），标签用向上的短箭头指向自己的圆点。每个目的方框用一条向下的长箭头落到时间轴上，注意落点在对应圆点的左侧——表示架构工作要在该决策点之前交付。

## 关键含义（历史解释；局部修正见上）

- 预算周期四阶段：Budget Planning（识别需要什么、将启动哪些新举措）→ Budget Preparation（自上而下与自下而上编制支出申请）→ Budget Allocation（释放资金）→ Budget Control（持续的财务与收益实现）。
- 四种架构目的与四个预算阶段一一对齐：战略对规划、组合对编制、项目对分配、解决方案交付对控制。
- 每个目的框的下箭头落点都在对应紫色里程碑圆点的左侧，这是“架构先于决策”的图形表达；正文明确说战略/组合/项目架构要在预算决策的关键里程碑之前完成。
- 支持解决方案交付的架构不是一次性交付，而是围绕预算控制持续运作；它在图中的方框也略高，暗示持续期更长。
- 整条时间轴只有一个方向（向右），没有回路；预算周期逐年重复，但图中只画了一个周期。
- 正文强调这是简化模型：用单向流程说明关键决策里程碑之间的相互作用，真实预算过程会更反复。

## 层级（历史解释；局部修正见上）

两层：上层是四个并列的架构目的（Architecture to Support …），下层是四个并列的预算阶段标签；两层通过垂直箭头一一对应。橙色时间轴是承载所有阶段的基线，不是上下级。

## 线条含义（历史解释；局部修正见上）

橙色粗箭头 = 时间方向（左→右）。四条从目的框向下的实线箭头 = 该目的的架构交付时点，落点在时间轴上。四条从预算阶段标签向上的短箭头 = 指向该阶段的决策里程碑圆点。目的框箭头落点与圆点之间的水平间距表示“提前量”。图中没有表示阶段之间因果或依赖的连线。

## 易误读点（历史解释；局部修正见上）

- 不要把紫色圆点读成阶段起点；它是该预算阶段的决策里程碑，阶段标签从下方指向它。
- 不要把目的框的下箭头读成“架构由预算阶段产生”；方向是架构交付到时间轴上，语义是架构先于该决策完成。
- 不要把四个阶段理解为必须严格串行、不可回退；正文说这是简化模型，只用于说明结构。
- 不要把“支持解决方案交付”放在最后理解为它只在预算控制阶段才启动；正文说它是围绕预算控制的持续运作。
- 英文 PDF 第 41 页把本图图题印成 “Figure 4-1: Characteristics of the EA Landscape”（与图 3-1 同名），这是原文的图题复制错误；第 136 页的图 14-1 是同一张图，图题正确为 Business Cycle and Architecture by Purpose。
- 中文稿当前引用的 figs/g186_fig4-1.svg 已改成四张串联卡片，看不到“落点在圆点左侧”的关键信息，不能据它理解本图。

## 元素

```json
[
  {
    "id": "budget_timeline",
    "label_en": null,
    "label_zh": "预算周期时间轴（橙色箭头）",
    "type": "time",
    "parent": null,
    "level": 0,
    "position": "横贯画面中部",
    "description_zh": "无文字的橙色粗箭头，表示时间从左向右推进。"
  },
  {
    "id": "ph_planning",
    "label_en": "Budget Planning",
    "label_zh": "预算规划",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "时间轴下方最左",
    "description_zh": "识别需要什么、将启动哪些新举措。"
  },
  {
    "id": "ph_preparation",
    "label_en": "Budget Preparation",
    "label_zh": "预算编制",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "时间轴下方左二",
    "description_zh": "自上而下与自下而上结合，形成各部门支出申请。"
  },
  {
    "id": "ph_allocation",
    "label_en": "Budget Allocation",
    "label_zh": "预算分配",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "时间轴下方右二",
    "description_zh": "把资金释放给实施项目。"
  },
  {
    "id": "ph_control",
    "label_en": "Budget Control",
    "label_zh": "预算控制",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "时间轴下方最右",
    "description_zh": "实施项目持续的财务控制与收益实现。"
  },
  {
    "id": "m_planning",
    "label_en": null,
    "label_zh": "预算规划决策里程碑（紫色圆点）",
    "type": "event",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "Budget Planning 上方",
    "description_zh": "无文字；由阶段标签的向上箭头指示。"
  },
  {
    "id": "m_preparation",
    "label_en": null,
    "label_zh": "预算编制决策里程碑（紫色圆点）",
    "type": "event",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "Budget Preparation 上方",
    "description_zh": "无文字。"
  },
  {
    "id": "m_allocation",
    "label_en": null,
    "label_zh": "预算分配决策里程碑（紫色圆点）",
    "type": "event",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "Budget Allocation 上方",
    "description_zh": "无文字。"
  },
  {
    "id": "m_control",
    "label_en": null,
    "label_zh": "预算控制决策里程碑（紫色圆点）",
    "type": "event",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "Budget Control 上方",
    "description_zh": "无文字。"
  },
  {
    "id": "a_strategy",
    "label_en": "Architecture to Support Strategy",
    "label_zh": "支持战略的架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 1,
    "position": "左上，黄色框",
    "description_zh": "与预算规划对齐；应在预算规划决策前完成。"
  },
  {
    "id": "a_portfolio",
    "label_en": "Architecture to Support Portfolio",
    "label_zh": "支持组合的架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 2,
    "position": "上排左二，绿色框",
    "description_zh": "与预算编制对齐。"
  },
  {
    "id": "a_project",
    "label_en": "Architecture to Support Project",
    "label_zh": "支持项目的架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 3,
    "position": "上排右二，浅棕框",
    "description_zh": "与预算分配对齐。"
  },
  {
    "id": "a_solution",
    "label_en": "Architecture to Support Solution Delivery",
    "label_zh": "支持解决方案交付的架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 4,
    "position": "右上，品红框（略高）",
    "description_zh": "与预算控制对齐，是围绕预算控制的持续运作。"
  }
]
```

## 关系

```json
[
  {
    "from": "a_strategy",
    "to": "m_planning",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从支持战略的方框向下的实线箭头，落在时间轴上 Budget Planning 圆点的左侧，表示该架构须在预算规划决策之前交付。"
  },
  {
    "from": "a_portfolio",
    "to": "m_preparation",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向下的实线箭头落在 Budget Preparation 圆点左侧。"
  },
  {
    "from": "a_project",
    "to": "m_allocation",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向下的实线箭头落在 Budget Allocation 圆点左侧。"
  },
  {
    "from": "a_solution",
    "to": "m_control",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向下的实线箭头落在 Budget Control 圆点左侧；该目的的架构在预算控制期间持续运作。"
  },
  {
    "from": "ph_planning",
    "to": "m_planning",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "预算阶段标签向上的短箭头，指向它在时间轴上的圆点。"
  },
  {
    "from": "ph_preparation",
    "to": "m_preparation",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同上。"
  },
  {
    "from": "ph_allocation",
    "to": "m_allocation",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同上。"
  },
  {
    "from": "ph_control",
    "to": "m_control",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同上。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_budget_cycle",
    "kind": "sequence",
    "name_zh": "预算周期四阶段（沿时间轴）",
    "steps": [
      "ph_planning",
      "ph_preparation",
      "ph_allocation",
      "ph_control"
    ],
    "description_zh": "橙色箭头给出时间方向，四个阶段标签依次贴在其下方；图中只画一个周期。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "橙色粗箭头",
    "meaning_zh": "时间轴，方向从左到右",
    "explicit": false
  },
  {
    "symbol": "紫色圆点",
    "meaning_zh": "预算阶段的决策里程碑",
    "explicit": false
  },
  {
    "symbol": "目的框下方的长箭头",
    "meaning_zh": "该目的的架构交付时点（落在里程碑左侧，表示提前）",
    "explicit": false
  },
  {
    "symbol": "预算阶段标签上方的短箭头",
    "meaning_zh": "把阶段名指向它在时间轴上的圆点",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "横向构图：上层从左到右四个彩色矩形（黄、绿、浅棕、品红），每个下方引出一条向下的黑箭头；中层是一条贯穿左右的橙色粗箭头（时间轴），轴上有四个紫色圆点；下层四个预算阶段文字，各自用短箭头向上指向对应圆点。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig14-1",
    "relation": "same_as",
    "note_zh": "第 136 页图 14-1 与本图逐像素同构（四个目的框、橙色时间轴、四个紫点、四个预算阶段），且图题正确为 Business Cycle and Architecture by Purpose；本图第 41 页的图题误印为 Characteristics of the EA Landscape。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "英文 PDF 第 41 页的图题 “Characteristics of the EA Landscape” 与图内容不符，应为 Business Cycle and Architecture by Purpose（与图 14-1 相同）；本分析按图内容解析。",
    "紫色圆点没有文字标签，只能由下方阶段标签的向上箭头判断它代表该阶段的决策里程碑。",
    "目的框下箭头落点与圆点之间的水平距离没有标尺，无法量化“提前多少”。",
    "四个方框的高度略有差异（解决方案交付更高），是否刻意表达持续时间无法确认。"
  ],
  "analyzed_from": [
    "英文 PDF 第 41 页图 4-1 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 41 页正文",
    "英文 PDF 第 136 页图 14-1 截图（用于确认同图与正确图题）",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 396–410 行",
    "figs/g186_fig4-1.svg 的文本与结构"
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
