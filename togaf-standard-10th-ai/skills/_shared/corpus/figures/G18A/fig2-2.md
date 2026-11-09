# G18A/fig2-2 · 四框框架

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/fig2-2.md) · [JSON](../../architecture/diagrams/G18A/fig2-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 13 页

![英文原图](../assets/G18A/fig2-2-p0013.png)

PDF 坐标：`[151.3, 540.8, 460.7, 681.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Customer Value
Proposition
Resources Processes
\—
Formula
```

## 概要（历史解释；局部修正见上）

用客户价值主张、利润公式、关键资源、关键流程四个相互作用的框，刻画业务模型的四要素框架。

## 目的（历史解释；局部修正见上）

作为图 2-1 之外的另一种著名表示，说明业务模型可以用四个必须彼此自洽的要素来描述：为谁创造什么价值、如何赚钱、靠什么资源与流程实现。

## 阅读顺序（历史解释；局部修正见上）

从顶部中央的 Customer Value Proposition 开始，沿两条斜向粗双向箭头分别看向左下（Key Resources + Key Processes 虚线组）与右下（Profit Formula）；再注意虚线组与 Profit Formula 之间的水平双向箭头，以及组内两框之间的小双向箭头。全图没有起点和终点，四框构成一个相互约束的整体。

## 关键含义（历史解释；局部修正见上）

- 四个框分别是 Customer Value Proposition（顶部中央）、Profit Formula（右下）、Key Resources 与 Key Processes（左下，被虚线框圈在一起）。
- 所有连线都是粗双向箭头，说明四要素两两互动：改动任一框都会牵动其他框，框架用来检验一致性而不是描述流程。
- 关键资源与关键流程同处一个虚线分组，代表业务模型的「运营侧」作为一个整体与价值主张、利润公式互动。
- 价值主张与利润公式直接双向相连：客户价值与盈利方式必须同时成立，不能只优化一边。
- 关键资源与关键流程之间还有一条短双向箭头，表示资源支撑流程、流程又积累/消耗资源。
- 原图只有框名，没有任何解释文字；四要素的具体含义依赖正文与原书，不能从图中推断细节。
- 图中没有客户、渠道、竞争等要素，不能当作业务模型画布使用。

## 层级（历史解释；局部修正见上）

没有上下级。四个框并列；Key Resources 与 Key Processes 被虚线框圈为一个视觉分组（组内两框仍并列），该组与 Customer Value Proposition、Profit Formula 构成三角。

## 线条含义（历史解释；局部修正见上）

四条粗灰双向箭头表示双向依赖/相互影响，没有起点终点；虚线圆角框是分组边界，不是关系线。箭头是粗灰色实心三角头，两端都有。

## 易误读点（历史解释；局部修正见上）

- 不要按箭头读成先后顺序：全部是双向箭头，表示同时成立、互相制约。
- 不要把虚线框当成第五个要素：它只是把关键资源与关键流程圈成运营侧一组。
- 不要把 Profit Formula 只理解为财务部门的事：它与价值主张直接双向相连，是业务模型的一极。
- 中文稿第 97 行引用的 SVG 是 2×2 网格且没有箭头，还把四框内容改写为自拟解释，不能据它理解四框之间的互动。

## 元素

```json
[
  {
    "id": "cvp",
    "label_en": "Customer Value Proposition",
    "label_zh": "客户价值主张",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "顶部中央",
    "description_zh": "四框之一，位于三角顶点。"
  },
  {
    "id": "profit_formula",
    "label_en": "Profit Formula",
    "label_zh": "利润公式",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "右下",
    "description_zh": "四框之一。"
  },
  {
    "id": "ops_group",
    "label_en": null,
    "label_zh": "运营侧分组（虚线框，无标题）",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "虚线圆角框，仅圈住关键资源与关键流程两个框。"
  },
  {
    "id": "key_resources",
    "label_en": "Key Resources",
    "label_zh": "关键资源",
    "type": "resource",
    "parent": "ops_group",
    "level": 2,
    "position": "虚线框内左侧"
  },
  {
    "id": "key_processes",
    "label_en": "Key Processes",
    "label_zh": "关键流程",
    "type": "process",
    "parent": "ops_group",
    "level": 2,
    "position": "虚线框内右侧"
  }
]
```

## 关系

```json
[
  {
    "id": "r_cvp_ops",
    "from": "cvp",
    "to": "ops_group",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "斜向粗双向箭头：价值主张与资源/流程组相互制约。"
  },
  {
    "id": "r_cvp_profit",
    "from": "cvp",
    "to": "profit_formula",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "斜向粗双向箭头：价值主张与利润公式相互制约。"
  },
  {
    "id": "r_ops_profit",
    "from": "ops_group",
    "to": "profit_formula",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "水平粗双向箭头：运营侧与利润公式相互制约。"
  },
  {
    "id": "r_res_proc",
    "from": "key_resources",
    "to": "key_processes",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "组内短粗双向箭头：关键资源与关键流程互相依赖。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅灰蓝圆角矩形",
    "meaning_zh": "业务模型的一个要素（四框之一）",
    "explicit": false
  },
  {
    "symbol": "虚线圆角外框",
    "meaning_zh": "把关键资源与关键流程圈为一个分组（运营侧）",
    "explicit": false
  },
  {
    "symbol": "粗灰双向箭头",
    "meaning_zh": "两要素之间的双向影响/依赖",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "三角布局：Customer Value Proposition 位于顶部居中；左下为虚线圆角框，内含并排的 Key Resources 与 Key Processes；右下为 Profit Formula。四条粗双向箭头把三组连成闭环。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig2-1",
    "relation": "complements",
    "note_zh": "两者都是第 2 节介绍的业务模型框架：图 2-1 为三要素抽象视图，本图为四框框架"
  },
  {
    "target": "G18A/fig2-3",
    "relation": "complements",
    "note_zh": "正文并列介绍的另一种业务模型表示"
  },
  {
    "target": "G18A/fig2-4",
    "relation": "complements",
    "note_zh": "四框框架与业务模型画布是同一主题的不同框架"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四条双箭头的具体语义（影响、依赖还是信息流）图中没有文字说明，解析统一按「双向影响/依赖」处理。",
    "虚线分组没有标题，称其为「运营侧」是依据框内两框（资源、流程）的通用含义所作的概括。"
  ],
  "analyzed_from": [
    "英文 PDF 第 13 页原图截图（fig2-2_p13_1.png）及 2×2 放大分块 z11",
    "英文 PDF 第 13 页正文",
    "中文稿 G18Ae_业务模型.md 第 95–97 行",
    "figs/g18a_fig2-2.svg 源码与 SVG 文本"
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
