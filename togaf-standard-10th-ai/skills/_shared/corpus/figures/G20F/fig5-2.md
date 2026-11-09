# G20F/fig5-2 · 敏捷环境中的企业架构阶段

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig5-2.md) · [JSON](../../architecture/diagrams/G20F/fig5-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 36 页

![英文原图](../assets/G20F/fig5-2-p0036.png)

PDF 坐标：`[48.2, 389.3, 563.8, 679.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Define Problem
Define Baseline
eo co cs
Define Target
Deploy Target
Govern and Manage Change
aoc &
```

## 概要（历史解释；局部修正见上）

同样的五个架构阶段，在敏捷环境中改为持续管理、并行推进，而不是逐段完成。

## 目的（历史解释；局部修正见上）

紧接图 5-1，用完全相同的五阶段布局说明：阶段划分没有变，变的是它们之间的关系——不再串行，而是持续管理、并行推进；同时给出“足够即可”的问题定义原则和阶段间的真实依赖。

## 阅读顺序（历史解释；局部修正见上）

先把它与图 5-1 对照：五条箭头的名称、颜色、子项排布完全一样，唯一变化是整张图不再暗示“做完一条再做下一条”。读的时候把五条箭头视为同时进行的活动带，每条带内的 A/B/C 子项各自推进；问题定义只需“足够”就可以让其他活动开始，但部署仍受基线/目标定义程度的约束。

## 关键含义（历史解释；局部修正见上）

- 五个阶段名称与图 5-1 完全相同（Define Problem / Define Baseline / Define Target / Deploy Target / Govern and Manage Change），说明敏捷没有取消阶段划分。
- 变化在关系：正文说这些活动在敏捷环境中是“持续管理的过程”，并行推进，而不是一条条顺序完成。
- 问题定义不必一次做完：定义到足以给其他活动提供语境即可，其他活动启动后再回来细化和扩展问题定义。
- 依赖仍然存在：在描述目标某部分的基线与目标被充分定义之前，无法部署该目标的任何部分——这是图中唯一被正文强调的硬约束。
- 每条箭头内的 A/B/C 与省略号表示每个阶段内部仍然分区、可枚举，可分批推进。

## 层级（历史解释；局部修正见上）

两层：五条阶段箭头为第一层（自上而下并列）；每条箭头内的三个子项（Sub-Problem/Baseline/Target/Change A/B/C）为第二层，彼此并列。与图 5-1 的唯一结构差别是“并列”取代了“先后”。

## 线条含义（历史解释；局部修正见上）

图中没有任何连接线或箭头。V 形条本身的形状只表示阶段内部推进方向；五条之间的并行关系靠“与图 5-1 相同的布局 + 正文说明”表达，不能从线条读出。

## 易误读点（历史解释；局部修正见上）

- 不要因为五条仍然自上而下排列就认为它们必须依次完成：本图正是要说明它们可以并行、持续进行。
- 不要把 A/B/C 子项当作先后步骤，它们是同一阶段内的并列事项。
- 不要以为“并行”等于没有依赖：正文明确说在基线与目标充分定义前无法部署目标。
- 中文稿引用的 figs/g20f_fig5-2.svg 被改写成“传统 vs 敏捷”两行对照，看不到五条阶段箭头与子项，不能据它理解本图。

## 元素

```json
[
  {
    "id": "st_problem",
    "label_en": "Define Problem",
    "label_zh": "定义问题",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "第一行，紫色"
  },
  {
    "id": "sp_a",
    "label_en": "Sub-Problem A",
    "label_zh": "子问题 A",
    "type": "requirement",
    "parent": "st_problem",
    "level": 2,
    "order": 1
  },
  {
    "id": "sp_b",
    "label_en": "Sub-Problem B",
    "label_zh": "子问题 B",
    "type": "requirement",
    "parent": "st_problem",
    "level": 2,
    "order": 2
  },
  {
    "id": "sp_c",
    "label_en": "Sub-Problem C",
    "label_zh": "子问题 C",
    "type": "requirement",
    "parent": "st_problem",
    "level": 2,
    "order": 3
  },
  {
    "id": "sp_etc",
    "label_en": "…",
    "label_zh": "……（后续子问题省略）",
    "type": "note",
    "parent": "st_problem",
    "position": "第一行右端"
  },
  {
    "id": "st_baseline",
    "label_en": "Define Baseline",
    "label_zh": "定义基线",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "第二行，蓝灰"
  },
  {
    "id": "bl_a",
    "label_en": "Baseline A",
    "label_zh": "基线 A",
    "type": "artifact",
    "parent": "st_baseline",
    "level": 2,
    "order": 1
  },
  {
    "id": "bl_b",
    "label_en": "Baseline B",
    "label_zh": "基线 B",
    "type": "artifact",
    "parent": "st_baseline",
    "level": 2,
    "order": 2
  },
  {
    "id": "bl_c",
    "label_en": "Baseline C",
    "label_zh": "基线 C",
    "type": "artifact",
    "parent": "st_baseline",
    "level": 2,
    "order": 3
  },
  {
    "id": "bl_etc",
    "label_en": "…",
    "label_zh": "……（后续基线省略）",
    "type": "note",
    "parent": "st_baseline",
    "position": "第二行右端"
  },
  {
    "id": "st_target",
    "label_en": "Define Target",
    "label_zh": "定义目标",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "第三行，橙色"
  },
  {
    "id": "tg_a",
    "label_en": "Target A",
    "label_zh": "目标 A",
    "type": "artifact",
    "parent": "st_target",
    "level": 2,
    "order": 1
  },
  {
    "id": "tg_b",
    "label_en": "Target B",
    "label_zh": "目标 B",
    "type": "artifact",
    "parent": "st_target",
    "level": 2,
    "order": 2
  },
  {
    "id": "tg_c",
    "label_en": "Target C",
    "label_zh": "目标 C",
    "type": "artifact",
    "parent": "st_target",
    "level": 2,
    "order": 3
  },
  {
    "id": "tg_etc",
    "label_en": "…",
    "label_zh": "……（后续目标省略）",
    "type": "note",
    "parent": "st_target",
    "position": "第三行右端"
  },
  {
    "id": "st_deploy",
    "label_en": "Deploy Target",
    "label_zh": "部署目标",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "第四行，蓝色"
  },
  {
    "id": "dp_a",
    "label_en": "Target A",
    "label_zh": "目标 A（部署）",
    "type": "artifact",
    "parent": "st_deploy",
    "level": 2,
    "order": 1,
    "description_zh": "原图该行三个子框同样标为 Target A/B/C。"
  },
  {
    "id": "dp_b",
    "label_en": "Target B",
    "label_zh": "目标 B（部署）",
    "type": "artifact",
    "parent": "st_deploy",
    "level": 2,
    "order": 2
  },
  {
    "id": "dp_c",
    "label_en": "Target C",
    "label_zh": "目标 C（部署）",
    "type": "artifact",
    "parent": "st_deploy",
    "level": 2,
    "order": 3
  },
  {
    "id": "dp_etc",
    "label_en": "…",
    "label_zh": "……（后续部署项省略）",
    "type": "note",
    "parent": "st_deploy",
    "position": "第四行右端"
  },
  {
    "id": "st_govern",
    "label_en": "Govern and Manage Change",
    "label_zh": "治理与管理变更",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 5,
    "position": "第五行，绿色"
  },
  {
    "id": "ch_a",
    "label_en": "Change A",
    "label_zh": "变革 A",
    "type": "requirement",
    "parent": "st_govern",
    "level": 2,
    "order": 1
  },
  {
    "id": "ch_b",
    "label_en": "Change B",
    "label_zh": "变革 B",
    "type": "requirement",
    "parent": "st_govern",
    "level": 2,
    "order": 2
  },
  {
    "id": "ch_c",
    "label_en": "Change C",
    "label_zh": "变革 C",
    "type": "requirement",
    "parent": "st_govern",
    "level": 2,
    "order": 3
  },
  {
    "id": "ch_etc",
    "label_en": "…",
    "label_zh": "……（后续变更省略）",
    "type": "note",
    "parent": "st_govern",
    "position": "第五行右端"
  }
]
```

## 关系

```json
[
  {
    "from": "st_problem",
    "to": "st_baseline",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "保留传统排列顺序，但在敏捷环境中两者并行推进；图中无连线"
  },
  {
    "from": "st_baseline",
    "to": "st_target",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "st_target",
    "to": "st_deploy",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "存在硬依赖：相关基线/目标定义充分前不能部署"
  },
  {
    "from": "st_deploy",
    "to": "st_govern",
    "type": "association",
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
    "id": "f_parallel",
    "kind": "parallel",
    "name_zh": "敏捷环境中并行推进的五类活动",
    "steps": [
      "st_problem",
      "st_baseline",
      "st_target",
      "st_deploy",
      "st_govern"
    ],
    "description_zh": "五类活动持续管理、并行推进；问题定义只需“足够”即可启动其他活动，但部署受基线/目标定义程度约束。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "紫色 V 形条",
    "meaning_zh": "Define Problem（定义问题）",
    "explicit": false
  },
  {
    "symbol": "蓝灰 V 形条",
    "meaning_zh": "Define Baseline（定义基线）",
    "explicit": false
  },
  {
    "symbol": "橙色 V 形条",
    "meaning_zh": "Define Target（定义目标）",
    "explicit": false
  },
  {
    "symbol": "蓝色 V 形条",
    "meaning_zh": "Deploy Target（部署目标）",
    "explicit": false
  },
  {
    "symbol": "绿色 V 形条",
    "meaning_zh": "Govern and Manage Change（治理与管理变更）",
    "explicit": false
  },
  {
    "symbol": "白色圆角子框",
    "meaning_zh": "阶段内并列事项（A/B/C…）",
    "explicit": false
  },
  {
    "symbol": "“…”",
    "meaning_zh": "同类事项可继续增加",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "五条等宽 V 形横条自上而下等距排列（与图 5-1 完全同构），每条内嵌三个白色圆角子框与一个“…”；无连接线。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig5-1",
    "relation": "follows",
    "note_zh": "图 5-1 是同一五阶段的传统（串行）版本，本图是其在敏捷环境中的版本。"
  },
  {
    "target": "G20F/fig5-4",
    "relation": "related",
    "note_zh": "图 5-4 细化了本图“部署目标”之后产品待办与冲刺待办如何形成。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图与图 5-1 在视觉上几乎相同（仅标题不同），五条箭头之间没有任何连线；并行关系完全依赖正文，图中未用图形表示。",
    "“Deploy Target”行子框仍标 Target A/B/C，照原样转录。"
  ],
  "analyzed_from": [
    "英文 PDF 第 36 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 36 页正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 454–460 行",
    "figs/g20f_fig5-2.svg 源码与文本"
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
