# G20F/fig5-1 · 企业架构的传统阶段

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig5-1.md) · [JSON](../../architecture/diagrams/G20F/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 36 页

![英文原图](../assets/G20F/fig5-1-p0036.png)

PDF 坐标：`[48.2, 36.0, 563.8, 90.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Govern and
Define
Define
Manage
Problem
Baseline
Change
```

## 概要（历史解释；局部修正见上）

把企业架构的传统做法概括为五条依次推进的阶段箭头：定义问题、定义基线、定义目标、部署目标、治理与管理变更。

## 目的（历史解释；局部修正见上）

作为 5.2 节的出发点：先用一张“传统、概括性”的图说明企业架构通常被理解为五个前后相继的阶段，再用图 5-2 说明敏捷环境中这些阶段如何并行与持续。

## 阅读顺序（历史解释；局部修正见上）

自上而下读五条箭头，每条箭头左端是尖角、右端是箭头，表示该阶段内部从左向右推进。箭头内并列的子框表示该阶段要处理的若干事项（A、B、C…后面省略）。先读阶段名，再看它对应的 ADM 阶段：A=定义问题；B/C/D=定义基线与目标；E/F/G=部署目标；H=治理与管理变更。

## 关键含义（历史解释；局部修正见上）

- 五个阶段依次是：Define Problem（紫）→ Define Baseline（蓝灰）→ Define Target（橙）→ Deploy Target（蓝）→ Govern and Manage Change（绿）。
- 每个阶段内部并列若干子项（子问题/基线/目标/变更各 A、B、C…），省略号表示可以更多，说明同一阶段内的工作是分区、可枚举的。
- 正文把五个阶段对应到 ADM：阶段 A 定义问题；B、C、D 定义基线与目标；E、F、G 部署目标；H 管理变更。
- 图中阶段是一条条分开的横条、自上而下排列，隐含“依次完成”的传统瀑布式读法——这正是后一张图要打破的印象。

## 层级（历史解释；局部修正见上）

两层：五个阶段为第一层（自上而下排列，无嵌套）；每个阶段包含若干并列子项（Sub-Problem A/B/C、Baseline A/B/C 等）为第二层，子项之间没有上下级。

## 线条含义（历史解释；局部修正见上）

图中没有任何连接线。V 形箭头的形状本身表示方向（从左向右推进），箭头右端的缺口/尖角是 chevron 造型。阶段之间的先后完全由自上而下的堆叠顺序隐含，没有箭头或连线把它们串起来。

## 易误读点（历史解释；局部修正见上）

- 不要以为五个阶段之间画了箭头：图中没有任何阶段间连线，顺序仅由上下位置表达。
- 不要把同一阶段内的 A/B/C 当作阶段步骤，它们是并列的子项（例如三个子问题）。
- 不要把这张图当作 TOGAF 推荐的流程：正文称它是“传统的、概括性的”视图，紧接着用图 5-2 说明敏捷环境下应并行推进。
- 中文稿引用的 figs/zh/g20fe_fig5-1_zh.png 在“部署目标”行的第一个子框排版损坏（“目标 A”溢出），看图时不要误以为那是标题。

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
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "无连线，先后由上下位置隐含"
  },
  {
    "from": "st_baseline",
    "to": "st_target",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "st_target",
    "to": "st_deploy",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "st_deploy",
    "to": "st_govern",
    "type": "sequence",
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
    "id": "f_traditional",
    "kind": "sequence",
    "name_zh": "传统企业架构五阶段",
    "steps": [
      "st_problem",
      "st_baseline",
      "st_target",
      "st_deploy",
      "st_govern"
    ],
    "description_zh": "自上而下依次推进；正文明确说这是传统视图，敏捷环境下应改为并行。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "紫色 V 形条",
    "meaning_zh": "Define Problem（定义问题）阶段",
    "explicit": false
  },
  {
    "symbol": "蓝灰 V 形条",
    "meaning_zh": "Define Baseline（定义基线）阶段",
    "explicit": false
  },
  {
    "symbol": "橙色 V 形条",
    "meaning_zh": "Define Target（定义目标）阶段",
    "explicit": false
  },
  {
    "symbol": "蓝色 V 形条",
    "meaning_zh": "Deploy Target（部署目标）阶段",
    "explicit": false
  },
  {
    "symbol": "绿色 V 形条",
    "meaning_zh": "Govern and Manage Change（治理与管理变更）阶段",
    "explicit": false
  },
  {
    "symbol": "白色圆角子框",
    "meaning_zh": "该阶段内的并列事项（A/B/C…）",
    "explicit": false
  },
  {
    "symbol": "“…”",
    "meaning_zh": "同类事项可以继续增加",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "五条等宽 V 形横条自上而下等距排列，每条横条内左侧并排三个白色圆角子框，右侧一个“…”。整图无连线。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig5-2",
    "relation": "precedes",
    "note_zh": "图 5-2 是同一五阶段在敏捷环境中的版本（活动并行、持续管理），正文用“as shown in Figure 5-2”直接承接。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "子项 A/B/C 的语义（三个并列的子问题/基线/目标/变更）依图与正文推断，原文未逐项解释。",
    "“Deploy Target”行内部仍标 Target A/B/C，是否应与上一行区分（例如 Deployment A）原图未作区分，照原样转录。"
  ],
  "analyzed_from": [
    "英文 PDF 第 36 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 35–36 页正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 441–452 行",
    "figs/g20fe_fig5-1_en.png 与 figs/zh/g20fe_fig5-1_zh.png"
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
