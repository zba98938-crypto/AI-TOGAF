# G186/fig3-1 · EA 全景的特征

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig3-1.md) · [JSON](../../architecture/diagrams/G186/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G186/fig3-1-p0028.png)

PDF 坐标：`[164.2, 36.0, 447.8, 272.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
ee? och)
Oo
Qannpling
Cn
EA Landscape
```

## 概要（历史解释；局部修正见上）

用三维立方体把 EA 全景画成一个体积，三条箭头轴分别表示广度、时间与详细程度。

## 目的（历史解释；局部修正见上）

作者用一张极简的立体图把“EA 全景”从抽象名词变成可想象的空间：全景不是一个架构，而是由广度、时间、详细程度三个方向张开的全部潜在架构内容；先建立这个体积概念，图 3-2 才能在其中切出一个架构项目。

## 阅读顺序（历史解释；局部修正见上）

先看立方体正面标注的 EA Landscape，它指的是整个立方体而非某一个面；再看三条从立方体左上角伸出的粗箭头，箭头指向维度增大的方向：Breadth (Subject) 沿上边缘向右上，Time (Planning Horizon) 斜穿顶面指向右前，Detail 沿左前竖边向下。图中没有第四条轴，也没有刻度；正文另外讨论的第四个特征“时效性（Recency）”只以文字出现。

## 关键含义（历史解释；局部修正见上）

- 立方体整体就是 EA 全景（EA Landscape），表示企业全部潜在的架构内容，而不是某一个架构或某一个存储库分区。
- 广度（Breadth，主题）是最重要的范围维度之一：可按领域、组织或举措来界定，正文说它最容易混淆。
- 时间（Time，规划期）是从现在到期望达到目标架构的时间点；正文指出规划期越长，架构通常越不详细，但这不是普遍规律。
- 详细程度（Detail）表示架构展开到多细；正文强调做到“回答当前问题所需”即可，越细交付周期（TTM）越长。
- 三个箭头都伸出立方体之外，说明这些维度是连续、开放的量，立方体只是示意，没有边界数值。
- 正文把第四个特征“时效性（Recency）”讲在同一节，但本图没有画对应的轴或标签，读图时不能从图上找到它。
- 正文特意提醒这是简化：真实的架构项目不像这样整齐的立方体，而更像“海胆”——有一个整合的中心，尖刺伸向四面八方。

## 层级（历史解释；局部修正见上）

只有一层：一个 EA 全景立方体 + 三个维度属性。三条轴不是立方体的组成部分，而是描述立方体三个方向的坐标轴；图中没有上级/下级框。

## 线条含义（历史解释；局部修正见上）

图中没有连接两个元素的语义连线，只有三条粗黑箭头作为坐标轴：箭头表示该维度增大的方向，轴线贴着立方体的三条棱。立方体右侧的灰色投影只起立体感作用，没有标注，也不表示任何数据。

## 易误读点（历史解释；局部修正见上）

- 不要把立方体读成“一个架构”或“架构存储库”：它是 EA 全景的总体积。
- 不要以为图上只有三个特征就否定第四个特征；Recency 在正文中明确列为第四个特征，只是没有被画成轴。
- 不要把三条箭头理解成流程或先后顺序；它们是三个正交的范围维度。
- 立方体没有刻度，不能从体积大小推断任何数量、成熟度或时间长度。
- 中文稿当前引用的 figs/g186_fig3-1.svg 是四张文字卡片，不是原图的立方体；它把图 3-2 的项目切片内容和正文别的段落混进来，不能据它理解本图。

## 元素

```json
[
  {
    "id": "ea_landscape",
    "label_en": "EA Landscape",
    "label_zh": "EA 全景",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "position": "立方体正面左侧",
    "description_zh": "整个立方体代表 EA 全景，即企业全部潜在的架构内容；不是某一个架构。"
  },
  {
    "id": "dim_breadth",
    "label_en": "Breadth (Subject)",
    "label_zh": "广度（主题）",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "position": "立方体上边缘，箭头向右上",
    "description_zh": "架构项目覆盖的主题范围，可按领域、组织或举措界定。"
  },
  {
    "id": "dim_time",
    "label_en": "Time (Planning Horizon)",
    "label_zh": "时间（规划期）",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "position": "立方体顶面，箭头斜向右前",
    "description_zh": "从当前到期望达到目标架构的时间点。"
  },
  {
    "id": "dim_detail",
    "label_en": "Detail",
    "label_zh": "详细程度",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "position": "立方体左前竖边，箭头向下",
    "description_zh": "架构展开的细致程度；做到回答当前问题所需即可。"
  }
]
```

## 关系

```json
[
  {
    "from": "ea_landscape",
    "to": "dim_breadth",
    "type": "other",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Breadth (Subject)",
    "label_zh": "广度（主题）",
    "description_zh": "从立方体左上角沿上边缘向右上画出的轴箭头，表示广度增大的方向；轴线本身不属于两个元素的连接。"
  },
  {
    "from": "ea_landscape",
    "to": "dim_time",
    "type": "other",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Time (Planning Horizon)",
    "label_zh": "时间（规划期）",
    "description_zh": "从同一角点斜穿顶面指向右前的轴箭头，表示规划期延伸的方向。"
  },
  {
    "from": "ea_landscape",
    "to": "dim_detail",
    "type": "other",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Detail",
    "label_zh": "详细程度",
    "description_zh": "沿左前竖边向下的轴箭头，表示详细程度增大的方向。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色三维立方体",
    "meaning_zh": "EA 全景（全部潜在架构内容）的体积",
    "explicit": false
  },
  {
    "symbol": "粗黑箭头",
    "meaning_zh": "维度坐标轴，箭头指向该维度增大的方向",
    "explicit": false
  },
  {
    "symbol": "立方体右侧的灰色投影",
    "meaning_zh": "仅用于表现立体感，无标注、无数据含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "单个立方体居中偏左，正面朝向左下；三条粗箭头分别从上边缘、顶面和左前竖边伸出；右侧有一片灰色投影；画面无标题、图例或边框。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig3-2",
    "relation": "variant_of",
    "note_zh": "同一立方体，图 3-2 在体积内切出一个红色半透明的架构项目切片，并保留 Breadth/Time/Detail 三条轴。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "原图只画了三条轴，正文却列出四个特征；Recency 没有对应的轴或标签，只能据正文判断。",
    "立方体右侧的灰色投影没有图例或文字，无法确定它是否在暗示“时效/老化”或只是立体渲染。",
    "三条轴没有刻度，全部为定性示意；无法判断立方体描绘的是“全部潜在内容”还是某一时点的切片。",
    "“EA Landscape”文字位于正面，是否也统摄整个立方体需结合图题与正文判断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 28 页图 3-1 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 28 页正文（Time、Recency 两段）",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 186–195 行",
    "figs/g186_fig3-1.svg 的文本与结构"
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
