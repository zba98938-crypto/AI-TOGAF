# G186/fig3-3 · 企业架构的目的

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig3-3.md) · [JSON](../../architecture/diagrams/G186/fig3-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 30 页

![英文原图](../assets/G186/fig3-3-p0030.png)

PDF 坐标：`[48.2, 153.2, 563.8, 216.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Architecture to Support
Architecture to Support
Architecture to Support
Strategy
Portfolio
Project
“ei
```

## 概要（历史解释；局部修正见上）

把 EA 能力的四种目的并排成四个彩色方块：战略、组合、项目、解决方案交付。

## 目的（历史解释；局部修正见上）

作者用一条横幅给出“基于目的的 EA 能力模型”的四个类别，作为 3.2.2 节和表 3-1 的分类骨架：先让读者接受目的只有这四类，再用正文逐一说明每类的时间跨度、范围与用途。

## 阅读顺序（历史解释；局部修正见上）

从左到右读四个方框，颜色只是区分，不是编码：黄=支持战略，绿=支持组合，棕=支持项目，品红=支持解决方案交付。四个框大小相同、地位并列；从左到右大致对应规划期由长到短、覆盖范围由宽到窄，但图上没有箭头，顺序本身不表示流程。

## 关键含义（历史解释；局部修正见上）

- 四种目的并列：Architecture to Support Strategy / Portfolio / Project / Solution Delivery；它们不是层级，也不是成熟度阶段。
- 支持战略的架构交付端到端目标架构与 3–10 年变革路线图，通常跨多个变革项目群或组合。
- 支持组合的架构支持跨职能、多阶段、多项目的变革举措，通常跨单个组合。
- 支持项目的架构支持企业的项目交付方法，通常跨单个项目。
- 支持解决方案交付的架构支持解决方案部署，通常是单个项目或项目的重要部分。
- 四种目的会决定架构项目的规划期、深度与广度，以及 EA 存储库的内容；这是后文表 3-1 与图 4-1 的分类依据。
- 方框等大并不表示工作量相同；原图没有给出规模、时间或成熟度信息。

## 层级（历史解释；局部修正见上）

扁平结构：一个浅蓝色横幅容器内并排四个同级方框，没有上下级、没有子项。四个目的共同构成“基于目的的 EA 能力模型”。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。唯一的视觉关系是“并排/相邻”，阅读顺序为从左到右；浅蓝色横幅把它们框为同一组。颜色没有图例，不能据此推断优先级。

## 易误读点（历史解释；局部修正见上）

- 不要把四个方框读成 ADM 阶段或先后步骤；它们是四种并列的架构目的。
- 不要把从左到右理解为必须按顺序经历；一个组织可以同时有多个目的，一个项目也可能横跨多个目的。
- 不要把“支持项目”和“支持解决方案交付”当成互斥：正文说后者通常是单个项目或项目的重要部分，两者范围有重叠。
- 颜色没有含义，不能把黄/绿/棕/品红当作成熟度或优先级。
- 中文图第二个、第三个方框的双重边框是本地化瑕疵，不代表原图有两个框。

## 元素

```json
[
  {
    "id": "purposes_band",
    "label_en": null,
    "label_zh": "四种目的的并排横幅（浅蓝底）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "整幅图",
    "description_zh": "原图没有标题的浅蓝色容器，把四个目的框在一起。"
  },
  {
    "id": "p_strategy",
    "label_en": "Architecture to Support Strategy",
    "label_zh": "支持战略的架构",
    "type": "architecture",
    "parent": "purposes_band",
    "level": 1,
    "order": 1,
    "position": "最左，黄色框",
    "description_zh": "端到端目标架构 + 3–10 年变革路线图，跨多个项目群或组合。"
  },
  {
    "id": "p_portfolio",
    "label_en": "Architecture to Support Portfolio",
    "label_zh": "支持组合的架构",
    "type": "architecture",
    "parent": "purposes_band",
    "level": 1,
    "order": 2,
    "position": "左二，绿色框",
    "description_zh": "支持跨职能、多阶段、多项目变革，通常跨单个组合。"
  },
  {
    "id": "p_project",
    "label_en": "Architecture to Support Project",
    "label_zh": "支持项目的架构",
    "type": "architecture",
    "parent": "purposes_band",
    "level": 1,
    "order": 3,
    "position": "右二，棕色框",
    "description_zh": "支持企业项目交付方法，通常跨单个项目。"
  },
  {
    "id": "p_solution",
    "label_en": "Architecture to Support Solution Delivery",
    "label_zh": "支持解决方案交付的架构",
    "type": "architecture",
    "parent": "purposes_band",
    "level": 1,
    "order": 4,
    "position": "最右，品红框",
    "description_zh": "支持解决方案部署，通常是单个项目或项目的重要部分。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色横条",
    "meaning_zh": "四种目的同属一个“基于目的的 EA 能力模型”",
    "explicit": false
  },
  {
    "symbol": "黄/绿/棕/品红方框",
    "meaning_zh": "四种架构目的的视觉区分，颜色本身无编码含义",
    "explicit": false
  },
  {
    "symbol": "从左到右的排列",
    "meaning_zh": "由企业级战略到单个解决方案交付的范围收窄（推断，不是画出的箭头）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "一条横向浅蓝色横幅，内部从左到右等距排列四个等宽矩形：黄、绿、棕、品红；无标题、无图例、无箭头。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig4-1",
    "relation": "basis_for",
    "note_zh": "图 4-1 把本图的四种目的分别对齐到预算规划、编制、分配、控制四个阶段。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图没有标题、图例或说明文字，四色是否另有含义无法从图上确认；按无编码处理。",
    "四个框等大，无法判断作者是否想表达范围或工作量差异；正文只说范围不同，未给比例。"
  ],
  "analyzed_from": [
    "英文 PDF 第 30 页图 3-3 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 30 页正文（四种目的的段落）",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 211–233 行及标签对照表 L215–L223",
    "figs/g186e_fig3-3_en.png 与 figs/zh/g186e_fig3-3_zh.png"
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
