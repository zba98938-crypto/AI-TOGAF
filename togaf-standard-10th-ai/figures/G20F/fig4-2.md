# G20F/fig4-2 · 过渡架构

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig4-2.md) · [JSON](../../architecture/diagrams/G20F/fig4-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 22 页

![英文原图](../assets/G20F/fig4-2-p0022.png)

PDF 坐标：`[48.2, 68.2, 563.8, 171.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Transition 2
Alternative A.
Transition 1 =|
=)
Nictecitd
(© The Open Group
```

## 概要（历史解释；局部修正见上）

从基线架构经若干（可含备选的）过渡架构逐段演进到目标架构的路线。

## 目的（历史解释；局部修正见上）

为 4.2 节定义过渡架构：架构在“架构上有意义的时点”的一个正式状态，通常包含若干能力增量；图中用一条带分支的链说明路线可以有多个备选过渡状态，且每段实施后系统整体保持稳定。

## 阅读顺序（历史解释；局部修正见上）

从左到右读：Baseline（基线）→ Transition 1 → 黑点处分为上下两条备选（Transition 2 Alternative A / B）→ 黑点汇合 → Transition 3 → Target。每个框右上角的小图标表示“这是一份架构描述”。黑点不是架构状态，只是路线的分叉与汇合。

## 关键含义（历史解释；局部修正见上）

- 过渡架构是介于基线与目标之间的“架构上有意义的时点”状态，不是项目里程碑或发布本身。
- 路线允许存在备选：第 2 个过渡架构给出 Alternative A 与 Alternative B 两条并行选项，说明过渡状态可以被选择而非唯一确定。
- 分支在汇合点重新收拢，之后还有 Transition 3，说明过渡架构可以有多个、逐步逼近目标。
- 正文指出每个过渡架构通常包含若干能力增量；在敏捷中这些增量通常通过冲刺实现，过渡架构因此与向利益相关者释放业务价值相对应。
- 过渡架构也是风险管理手段：把交付拆成可理解的增量状态，逐段确认系统整体仍然稳定。

## 层级（历史解释；局部修正见上）

平级序列，没有上下级：Baseline、Transition 1、Alternative A/B、Transition 3、Target 都是同一抽象层级的架构状态；分支与汇合用两个不带文字的黑色圆点表示。

## 线条含义（历史解释；局部修正见上）

黑色实线箭头表示演进方向（从左到右）；分叉点把一个箭头分成两条，汇合点把两条并回一条，因此“箭头”表达的是时间上的先后而非因果。框右侧的小图标（三条横线加斜线）表示该框承载架构描述/交付物，不是连接线。

## 易误读点（历史解释；局部修正见上）

- 不要把 Alternative A/B 理解为“两个阶段”；它们是同一时点的两个可选过渡状态，最终只走其中一条。
- 不要把过渡架构等同于发布或冲刺：正文说能力增量通常用冲刺实现，过渡架构对应的是向利益相关者释放业务价值的时点。
- 中文稿引用的 figs/g20f_fig4-2.svg 把图压成了无分支的直线且只有 2 个过渡架构，据此会误以为路线唯一且只有两段。

## 元素

```json
[
  {
    "id": "baseline",
    "label_en": "Baseline",
    "label_zh": "基线架构",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "最左"
  },
  {
    "id": "transition_1",
    "label_en": "Transition 1",
    "label_zh": "过渡架构 1",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "左二"
  },
  {
    "id": "split_node",
    "label_en": null,
    "label_zh": "分叉节点",
    "type": "other",
    "parent": null,
    "position": "Transition 1 与两个备选之间的黑点",
    "description_zh": "无文字的连接节点，仅表示路线在此分为两条。"
  },
  {
    "id": "transition_2_alt_a",
    "label_en": "Transition 2 Alternative A",
    "label_zh": "过渡架构 2 备选 A",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "中部上排"
  },
  {
    "id": "transition_2_alt_b",
    "label_en": "Transition 2 Alternative B",
    "label_zh": "过渡架构 2 备选 B",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "中部下排"
  },
  {
    "id": "merge_node",
    "label_en": null,
    "label_zh": "汇合节点",
    "type": "other",
    "parent": null,
    "position": "两个备选与 Transition 3 之间的黑点",
    "description_zh": "无文字的连接节点，表示两条路线在此并为一条。"
  },
  {
    "id": "transition_3",
    "label_en": "Transition 3",
    "label_zh": "过渡架构 3",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "右二"
  },
  {
    "id": "target",
    "label_en": "Target",
    "label_zh": "目标架构",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 5,
    "position": "最右"
  }
]
```

## 关系

```json
[
  {
    "from": "baseline",
    "to": "transition_1",
    "type": "transitions_to",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "transition_1",
    "to": "split_node",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "split_node",
    "to": "transition_2_alt_a",
    "type": "transitions_to",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分叉出的上支（备选 A）"
  },
  {
    "from": "split_node",
    "to": "transition_2_alt_b",
    "type": "transitions_to",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分叉出的下支（备选 B）"
  },
  {
    "from": "transition_2_alt_a",
    "to": "merge_node",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "transition_2_alt_b",
    "to": "merge_node",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "merge_node",
    "to": "transition_3",
    "type": "transitions_to",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "transition_3",
    "to": "target",
    "type": "transitions_to",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_route_a",
    "kind": "sequence",
    "name_zh": "经备选 A 的过渡路线",
    "steps": [
      "baseline",
      "transition_1",
      "transition_2_alt_a",
      "transition_3",
      "target"
    ]
  },
  {
    "id": "f_route_b",
    "kind": "sequence",
    "name_zh": "经备选 B 的过渡路线",
    "steps": [
      "baseline",
      "transition_1",
      "transition_2_alt_b",
      "transition_3",
      "target"
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "等轴测立体浅绿框",
    "meaning_zh": "一个架构状态（基线/过渡/目标）",
    "explicit": false
  },
  {
    "symbol": "框右上角“堆叠文档”小图标",
    "meaning_zh": "该状态以架构描述/交付物形式存在",
    "explicit": false
  },
  {
    "symbol": "黑色实线箭头",
    "meaning_zh": "演进方向（时间先后）",
    "explicit": true
  },
  {
    "symbol": "黑色实心小圆点",
    "meaning_zh": "路线的分叉点/汇合点，本身不是架构状态",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "单行从左到右：Baseline、Transition 1 两个框；随后分叉成上下两行的 Transition 2 Alternative A（上）与 Alternative B（下）；汇合后是 Transition 3 与 Target。所有框为等轴测立体框，尺寸相近。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig4-3",
    "relation": "related",
    "note_zh": "同属 4.2–4.3 节：过渡架构给出时点状态，图 4-3 给出产生这些状态的多级 ADM 循环结构。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "两个黑色圆点在原图中没有文字，标注为“分叉/汇合节点”属版式推断。",
    "框内右上角小图标的含义（架构描述/交付物）由形状推断，原文未在图注中说明。"
  ],
  "analyzed_from": [
    "英文 PDF 第 22 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 22 页正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 219–221 行",
    "figs/g20f_fig4-2.svg 源码与文本"
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
