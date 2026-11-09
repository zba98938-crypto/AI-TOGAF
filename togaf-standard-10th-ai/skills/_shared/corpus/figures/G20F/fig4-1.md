# G20F/fig4-1 · 架构全景的分级分类模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig4-1.md) · [JSON](../../architecture/diagrams/G20F/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 20 页

![英文原图](../assets/G20F/fig4-1-p0020.png)

PDF 坐标：`[118.5, 252.7, 493.5, 589.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
‘The Open Group
Breadth
Time
Enterprise Strategic Architecture
Segment
Segment
Architecture
Architecture
```

## 概要（历史解释；局部修正见上）

用三层立体板块加三个方向轴，说明企业战略、分段、能力架构在层级、广度与时间上的关系。

## 目的（历史解释；局部修正见上）

为 4.1 节建立“按详细程度分层”的模型：企业战略架构铺满整个广度与时间，分段架构在其下沿时间并列出现，能力架构再向下细分且以冲刺为节奏。作者同时提醒不要把这个层级划分与业务/数据/应用/技术四个架构域混淆。

## 阅读顺序（历史解释；局部修正见上）

先看三个轴：向左下的 LEVEL 箭头由高到低，斜向上的 BREADTH 箭头由窄到宽，水平向右的 TIME 箭头表示时间推进。再按颜色读三层：最上方一整块黄色是企业战略架构；其下一列绿色块是分段架构，沿时间轴重复出现；最下方一排排紫色小块是能力架构。底部红色大箭头 Sprints 说明能力层按冲刺节奏交付。

## 关键含义（历史解释；局部修正见上）

- 三个层级由高到低：企业战略架构（黄）→ 分段架构（绿）→ 能力架构（紫），对应 LEVEL 轴的向下箭头。
- 黄色的企业战略架构是一整块，横跨全部广度与时间，表示它为企业整体提供语境与约束，本身不再按分段切分。
- 绿色的分段架构在时间轴上重复出现多块，表示分段可以多个并行、逐个交付；正文补充其通常位于组合/项目群/产品层并沿功能自然边界划分。
- 紫色能力架构是最小、数量最多的块，位于最低层，表示对业务能力增量的详细描述，可直接交给开发团队。
- BREADTH 轴表示覆盖广度：越往上覆盖越宽（整个企业），越往下覆盖越窄（单个能力）。
- 底部红色 Sprints 箭头表示冲刺沿时间持续推进；中文稿说明冲刺可发生在任何层级，但最常与能力或能力增量的交付相关，且可并行。
- 正文特别强调：这三个层级不是架构域；业务、数据、应用、技术架构可能存在于所有详细层级，二者是正交的。
- 自下而上，能力增量的实施会反馈并影响更高层级，各层架构因部署经验而演进。

## 层级（历史解释；局部修正见上）

三层视觉层级：企业战略架构（L1，最上层、最宽）包含/约束其下的多个分段架构（L2），分段架构再向下由多个能力架构（L3）支撑。图中的“上下”同时表示详细程度与覆盖广度，而不是组织上的汇报关系。

## 线条含义（历史解释；局部修正见上）

图中没有连接各板块的线；关系由三维位置与颜色表达：黄色块在上且横贯全图，绿色块在其下并沿时间轴排列，紫色小块在最下层成排。三个轴箭头是量纲示意：LEVEL 向下=层级降低，BREADTH 斜向上=覆盖变宽，TIME 向右=时间推进；红色 Sprints 箭头=冲刺随时间的推进方向。

## 易误读点（历史解释；局部修正见上）

- 不要把三层理解为业务架构/数据架构/应用架构/技术架构四个域；正文明确说层级与架构域是两回事，四个域在每个层级都可能存在。
- 不要以为绿色分段架构只有一块：原图中它沿时间轴重复出现（后方还有未标注的块），表示多个分段并行交付。
- 不要以为紫色小块是“应用系统清单”；它们表示能力架构（业务能力的详细描述），中文稿说明其详细程度足以交给开发人员执行。
- 中文稿当前引用的 figs/g20f_fig4-1.svg 已改成三层堆叠方框并丢失三个轴与 Sprints 箭头，不能据它理解“广度/时间/冲刺”这三层含义。

## 元素

```json
[
  {
    "id": "arch_landscape",
    "label_en": null,
    "label_zh": "架构全景（三层立体块整体）",
    "type": "group",
    "parent": null,
    "level": 0,
    "description_zh": "原图没有总标题，此元素代表被三个轴度量的整个板块群。"
  },
  {
    "id": "lvl_enterprise",
    "label_en": "Enterprise Strategic Architecture",
    "label_zh": "企业战略架构",
    "type": "architecture",
    "parent": "arch_landscape",
    "level": 1,
    "order": 1,
    "position": "最上层黄色整块"
  },
  {
    "id": "lvl_segment_1",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "architecture",
    "parent": "arch_landscape",
    "level": 2,
    "order": 1,
    "position": "中层左侧绿色块"
  },
  {
    "id": "lvl_segment_2",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "architecture",
    "parent": "arch_landscape",
    "level": 2,
    "order": 2,
    "position": "中层右侧绿色块",
    "description_zh": "同一层级沿时间轴的第二个分段；其后还有未标注的重复块。"
  },
  {
    "id": "lvl_capability_1",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "parent": "arch_landscape",
    "level": 3,
    "order": 1,
    "position": "底层前排左侧紫色块"
  },
  {
    "id": "lvl_capability_2",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "parent": "arch_landscape",
    "level": 3,
    "order": 2,
    "position": "底层前排中间紫色块"
  },
  {
    "id": "lvl_capability_3",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "parent": "arch_landscape",
    "level": 3,
    "order": 3,
    "position": "底层前排右侧紫色块"
  },
  {
    "id": "axis_level",
    "label_en": "Level",
    "label_zh": "层级（Level）",
    "type": "concept",
    "parent": null,
    "position": "左侧竖线，箭头向下"
  },
  {
    "id": "axis_breadth",
    "label_en": "Breadth",
    "label_zh": "广度（Breadth）",
    "type": "concept",
    "parent": null,
    "position": "左上斜线，箭头向右上"
  },
  {
    "id": "axis_time",
    "label_en": "Time",
    "label_zh": "时间（Time）",
    "type": "concept",
    "parent": null,
    "position": "水平线，箭头向右，穿过板块中部"
  },
  {
    "id": "sprints",
    "label_en": "Sprints",
    "label_zh": "冲刺",
    "type": "time",
    "parent": null,
    "position": "图底部红色大箭头",
    "description_zh": "表示能力架构按冲刺节奏持续交付。"
  }
]
```

## 关系

```json
[
  {
    "from": "axis_level",
    "to": "arch_landscape",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向下箭头：层级由高到低、详细程度增加"
  },
  {
    "from": "axis_breadth",
    "to": "arch_landscape",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "斜向上箭头：覆盖广度由窄到宽"
  },
  {
    "from": "axis_time",
    "to": "arch_landscape",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向右箭头：时间推进方向"
  },
  {
    "from": "sprints",
    "to": "lvl_capability_2",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "红色大箭头横贯能力层下方，表示冲刺沿时间推进、逐块交付能力增量"
  },
  {
    "from": "lvl_enterprise",
    "to": "lvl_segment_1",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "由上下位置与 LEVEL 轴隐含：高层为低层提供语境与约束"
  },
  {
    "from": "lvl_enterprise",
    "to": "lvl_segment_2",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "lvl_segment_1",
    "to": "lvl_capability_1",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "lvl_segment_2",
    "to": "lvl_capability_2",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "lvl_segment_2",
    "to": "lvl_capability_3",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_levels_tb",
    "kind": "sequence",
    "name_zh": "自上而下：语境与约束",
    "steps": [
      "lvl_enterprise",
      "lvl_segment_1",
      "lvl_capability_1"
    ],
    "description_zh": "高层建立语境、低层细化；原图用层叠位置而非箭头表达。"
  },
  {
    "id": "f_levels_bt",
    "kind": "loop",
    "name_zh": "自下而上：反馈与演进",
    "steps": [
      "lvl_capability_3",
      "lvl_segment_2",
      "lvl_enterprise"
    ],
    "loop_type": "reinforcing",
    "description_zh": "能力增量的实施经验反馈到更高层（依据正文，图中无回指箭头）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色立体大板",
    "meaning_zh": "企业战略架构（最高层、覆盖最广）",
    "explicit": false
  },
  {
    "symbol": "绿色立体块",
    "meaning_zh": "分段架构（中层，沿时间重复出现）",
    "explicit": false
  },
  {
    "symbol": "紫色小立体块",
    "meaning_zh": "能力架构（最低层、最细、数量最多）",
    "explicit": false
  },
  {
    "symbol": "深蓝 LEVEL 竖箭头（向下）",
    "meaning_zh": "层级由高到低、详细程度增加",
    "explicit": true
  },
  {
    "symbol": "深蓝 BREADTH 斜箭头（向上）",
    "meaning_zh": "覆盖广度由窄到宽",
    "explicit": true
  },
  {
    "symbol": "深蓝 TIME 横箭头（向右）",
    "meaning_zh": "时间推进方向",
    "explicit": true
  },
  {
    "symbol": "红色 Sprints 大箭头（向右）",
    "meaning_zh": "冲刺节奏沿时间推进",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "等轴测视角：黄色大板在顶部，绿色块在其下方向右后方排列（至少 2 个带标签、后方还有重复块），紫色小块在最下层排成数行；左侧竖直 LEVEL 箭头向下，左上斜向 BREADTH 箭头向上，水平 TIME 箭头向右穿过板块中部，底部一条红色 Sprints 大箭头向右。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig4-5",
    "relation": "complements",
    "note_zh": "图 4-5 用同一套企业/分段/能力三层模型，进一步画出每层的待办、迭代与交付节奏及层间“指导”箭头。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图中绿色与紫色块有明显重复（后方还有未标注的块），具体块数在缩略图中不易精确计数，只标注了带文字的三类块。",
    "三个轴分别度量的是“层级/广度/时间”，但图中未说明轴的取值刻度，只能按方向解读。"
  ],
  "analyzed_from": [
    "英文 PDF 第 20 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 20 页正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 184–206 行",
    "figs/g20f_fig4-1.svg 源码与文本"
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
