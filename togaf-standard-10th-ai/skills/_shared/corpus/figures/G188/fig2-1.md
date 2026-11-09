# G188/fig2-1 · 企业架构的层级（TOGAF 架构全景摘要分类模型）

> 当前图示解析：[Markdown](../../architecture/diagrams/G188/fig2-1.md) · [JSON](../../architecture/diagrams/G188/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G188e.pdf`；SHA-256：`6e654af12a0bc034c7548d425a01123331ac9129c478a0bb957db89dd353dd29`。

## 原图 · PDF 第 20 页

![英文原图](../assets/G188/fig2-1-p0020.png)

PDF 坐标：`[99.8, 79.6, 512.2, 446.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
The Open Group
Breadth
Time
Enterprise Strategic Architecture
Segment
Segment
Architecture
Architecture
```

## 概要（历史解释；局部修正见上）

用广度、时间、层级三个维度说明企业架构全景分为战略、分段、能力三层，越往下越具体。

## 目的（历史解释；局部修正见上）

把 TOGAF 的架构全景分类模型压缩成一张透视图，让读者在讨论架构项目范围时能说清“项目覆盖哪一层、多宽、看多长时间”，并支撑下文的结论：一个架构项目通常只覆盖其中一个层级。

## 阅读顺序（历史解释；局部修正见上）

先看三条轴：向右的 Time（时间）、向右上方的 Breadth（广度）、向下的 Level（层级）。再沿 Level 轴自上而下读三层：最上层是一整块黄色 Enterprise Strategic Architecture；中间绿色层由多个并排的 Segment Architecture 方块组成，并沿时间轴向后重复；最下紫色层是数量更多、体量更小的 Capability Architecture 方块。透视方向表示同一层在时间上可有多代、在广度上可有多块。

## 关键含义（历史解释；局部修正见上）

- 企业架构全景有三个分类维度：层级（Level）、广度（Breadth）、时间（Time）；三者共同界定一个架构的范围。
- 层级自上而下为：企业战略架构（覆盖整个企业）→ 分段架构（覆盖企业的一个业务分段）→ 能力架构（覆盖单个业务能力，最详细）。
- 越往下层，架构数量越多、单块范围越小：图中战略层只有一块，分段层有多块，能力层方块最多、最小。
- 同一层沿时间轴向后重复排列，表示架构会随时间演进，存在多个时间切片（基线、过渡、目标等）。
- 正文据此指出：一个架构项目通常恰好覆盖三个层级中的一个；战略层项目的架构通常是分段层项目的输入，分段层又为能力层提供输入。
- 颜色只区分层级（黄/绿/紫），图中没有图例；不应把颜色理解为成熟度或优先级。

## 层级（历史解释；局部修正见上）

三层自上而下：企业战略架构（L1）→ 分段架构（L2）→ 能力架构（L3）。这是架构覆盖范围的层级包含关系（战略层最广、能力层最细），不是组织汇报关系。每条轴是独立的分类维度，不构成层级。

## 线条含义（历史解释；局部修正见上）

三条深蓝色箭头是坐标轴，不是要素之间的流程：Level 向下表示层级由粗到细，Breadth 向右上表示覆盖范围由窄到宽，Time 向右表示时间推进。方块之间没有连线；层与层的上下叠放、同层方块的前后错落表达包含与时间切片。

## 易误读点（历史解释；局部修正见上）

- 不要把三个轴当成三个步骤或三个阶段；它们是同时界定的三个范围维度。
- 不要把绿色分段架构的两块理解为只有两个分段；原图用少量方块加透视重复表示“多个”，未给出确切数量。
- 不要以为能力架构位于分段架构“之后”才出现；它只是范围更小、更详细，三层可并存。
- 中文稿引用的中文化 PNG 中有一个方块残留英文 Architecture，不影响结构判断，但不能据此认为原图混排中英文。

## 元素

```json
[
  {
    "id": "level_axis",
    "label_en": "Level",
    "label_zh": "层级",
    "type": "concept",
    "parent": null,
    "position": "左侧竖直向下箭头",
    "notation_type": "axis",
    "description_zh": "分类维度：架构覆盖的层级，向下由战略到能力。"
  },
  {
    "id": "breadth_axis",
    "label_en": "Breadth",
    "label_zh": "广度",
    "type": "concept",
    "parent": null,
    "position": "左上，指向右上方的斜箭头",
    "notation_type": "axis",
    "description_zh": "分类维度：架构覆盖的广度。"
  },
  {
    "id": "time_axis",
    "label_en": "Time",
    "label_zh": "时间",
    "type": "concept",
    "parent": null,
    "position": "水平向右箭头",
    "notation_type": "axis",
    "description_zh": "分类维度：架构覆盖的时间跨度/时间切片。"
  },
  {
    "id": "enterprise_strategic_architecture",
    "label_en": "Enterprise Strategic Architecture",
    "label_zh": "企业战略架构",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "position": "最上层黄色大板",
    "description_zh": "覆盖整个企业的高层架构。"
  },
  {
    "id": "segment_architecture",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "position": "中间绿色层",
    "attributes": {
      "visible_blocks": 2
    },
    "description_zh": "覆盖企业某一业务分段的架构；原图可见两块带标签方块，右侧另有未加标签的同类方块表示多个分段。"
  },
  {
    "id": "capability_architecture",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "parent": null,
    "level": 3,
    "position": "最下层紫色小方块",
    "attributes": {
      "visible_blocks": 3
    },
    "description_zh": "覆盖单个业务能力的架构，最详细；原图可见三块带标签方块，后方还有多排小块。"
  }
]
```

## 关系

```json
[
  {
    "from": "level_axis",
    "to": "enterprise_strategic_architecture",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Level",
    "label_zh": "层级",
    "description_zh": "层级轴指向战略层，表示其位于最高层"
  },
  {
    "from": "breadth_axis",
    "to": "enterprise_strategic_architecture",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Breadth",
    "label_zh": "广度",
    "description_zh": "广度轴沿战略层板的对角方向，表示覆盖广度"
  },
  {
    "from": "time_axis",
    "to": "segment_architecture",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Time",
    "label_zh": "时间",
    "description_zh": "时间轴横贯各层方块，表示同一架构在时间上的多个切片"
  },
  {
    "from": "enterprise_strategic_architecture",
    "to": "segment_architecture",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "上下叠放表示战略层范围包含若干分段，分段是其更详细的分解"
  },
  {
    "from": "segment_architecture",
    "to": "capability_architecture",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "上下叠放表示分段层范围包含若干能力，能力是其更详细的分解"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色大板",
    "meaning_zh": "企业战略架构（覆盖整个企业）",
    "explicit": false
  },
  {
    "symbol": "绿色方块",
    "meaning_zh": "分段架构（覆盖一个业务分段）",
    "explicit": false
  },
  {
    "symbol": "紫色小方块",
    "meaning_zh": "能力架构（覆盖单个业务能力）",
    "explicit": false
  },
  {
    "symbol": "同层方块沿右后方重复排列",
    "meaning_zh": "同一层级存在多个实例/多个时间切片",
    "explicit": false
  },
  {
    "symbol": "三条深蓝箭头",
    "meaning_zh": "Level / Breadth / Time 三个分类维度",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "透视堆叠：顶部一块大的黄色战略层板；其下绿色分段层由两块并排的大方块加右侧多块渐远的方块组成；底部紫色能力层由一排小块加右侧多排更小块组成。左上为竖直向下的 Level 轴，顶部为指向右上的 Breadth 轴，水平为指向右的 Time 轴；三轴交于左上角。"
}
```

## 相关图

```json
[
  {
    "target": "G188/fig1-1",
    "relation": "complements",
    "note_zh": "图 1-1 界定架构项目在 ADM 中的阶段范围，本图界定其在架构全景中的层级/广度/时间范围"
  },
  {
    "target": "G188/fig2-2",
    "relation": "complements",
    "note_zh": "本图给出架构项目的静态范围维度，图 2-2 给出其生命周期"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图分段层、能力层后方未加标签的方块数量无法精确计数，本分析只记录可见的带标签方块数并以“多个”描述其余。",
    "三个轴在原图中从左上角同一点引出，Level 与 Breadth 箭头的具体交点被战略层板遮挡，按视觉判断记录。"
  ],
  "analyzed_from": [
    "英文 PDF 第 20 页原图截图（含 2x2 放大分块）",
    "英文 PDF 第 19–21 页正文",
    "中文稿 G188e_架构项目管理.md 第 147–182 行及图内标签对照表 L154–L164",
    "figs/zh/g188e_fig2-1_zh.png 与 figs/g188e_fig2-1_en.png"
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
