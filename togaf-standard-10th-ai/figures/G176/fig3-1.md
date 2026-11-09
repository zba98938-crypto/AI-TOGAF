# G176/fig3-1 · 创建业务场景

> 当前图示解析：[Markdown](../../architecture/diagrams/G176/fig3-1.md) · [JSON](../../architecture/diagrams/G176/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G176e.pdf`；SHA-256：`48c76fbfd164020fcbc0a4f2ec12ee849a2af83424a332883f9a8e0260bf4961`。

## 原图 · PDF 第 18 页

![英文原图](../assets/G176/fig3-1-p0018.png)

PDF 坐标：`[125.6, 321.8, 486.4, 656.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
1-Problem
(pain points, barriers, issues)
2- Environment
(business and technology, value streams,
business capabilities)
3- Outcomes
(SMART - Specific, Measurable, Actionable,
Realistic, and Time-bound)
4— Human Actors
(capabilities, roles, and responsibilities)
S— Computer Actors
(capabilities, roles, and responsibilities)
```

## 概要（历史解释；局部修正见上）

创建业务场景要依次覆盖五个要素：问题、环境、成果（SMART）、人的参与者、计算机参与者。

## 目的（历史解释；局部修正见上）

第 3.1 节“总体过程”用它概括业务场景必须捕获的五个要素；正文列出的六个步骤中，前五步依次对应图中编号 1–5，第 6 步是检验“是否适用”并仅在必要时细化。第 3.2.2 节“收集”步骤又以本图的五个领域作为信息收集的范围。

## 阅读顺序（历史解释；局部修正见上）

从上往下按编号读 5 个色块，阶梯式右移只表示先后，不表示上下级。每块第一行是要素名，括号内是该要素要涵盖的内容。图中没有连线、箭头或图例。

## 关键含义（历史解释；局部修正见上）

- 业务场景由五个要素组成，编号 1–5：问题、环境、成果、人的参与者、计算机参与者；对应第 3.1 节六个步骤的前五步，第 6 步（检验是否适用、仅在必要时细化）不在图中。
- 问题是起点，指痛点、障碍和议题；步骤 1 要识别、记录并排序驱动该场景的问题。
- 环境既包括业务环境也包括技术环境，用价值流和业务能力来建模（步骤 2：记录在包含价值流和业务能力的场景模型中）。
- 成果是成功处理问题后的结果，必须 SMART：具体、可度量、可行动、现实、有时限（步骤 3）。
- 人的参与者和计算机参与者的括注相同，都按能力、角色和职责描述；区别在于前者定位到业务模型，后者（计算元素）定位到技术模型（步骤 4、5）。
- 业务场景方法是迭代的：每轮包括规划、收集、分析、记录和评审，并改进一个或多个要素，直到理解足以决定推进；不审视全部要素会有解决方案不完整的风险，但也不应无谓地反复（第 1 章）。

## 层级（历史解释；局部修正见上）

五个要素同级，是“业务场景”的组成部分（业务场景本身在图中没有单独的框）。括号内的文字是该要素的内容说明，不是下级元素。

## 线条含义（历史解释；局部修正见上）

图中没有连线。编号和阶梯式错位排列表示先后顺序（关系清单中标为推断的 sequence）；颜色从深蓝渐变到绿色，推断只是视觉上的递进，没有额外含义。

## 易误读点（历史解释；局部修正见上）

- 阶梯排列不是层级：问题并不统辖其余四个要素；中文稿引用的 SVG 用树形连线把“问题”画成上级，原图没有这种关系。
- 顺序也不等于一次走完：正文说明业务场景按多轮迭代完善，每轮可改进任一要素。
- 参与者括注中的“capabilities”指参与者具备的能力；第 3.1 节对“能力”和“业务能力”分别下了定义。
- 中文稿把本图放在第 1 章引言（L82），图题写作“业务场景的五个要素”；英文原文中图 3-1 位于第 3.1 节“总体过程”，图题为“Creating a Business Scenario”，中文稿第 3.1 节（L135）引用图 3-1 处没有放图。

## 元素

```json
[
  {
    "id": "business_scenario",
    "label_en": "Business Scenario",
    "label_zh": "业务场景",
    "type": "concept",
    "parent": null,
    "level": 0,
    "description_zh": "图中未单独画出；由图题与正文得知五个要素都属于业务场景。"
  },
  {
    "id": "e_problem",
    "label_en": "1 – Problem (pain points, barriers, issues)",
    "label_zh": "1 – 问题（痛点、障碍、议题）",
    "type": "requirement",
    "parent": "business_scenario",
    "level": 1,
    "order": 1,
    "description_zh": "对应步骤 1：识别、记录并排序驱动场景的问题。"
  },
  {
    "id": "e_environment",
    "label_en": "2 – Environment (business and technology, value streams, business capabilities)",
    "label_zh": "2 – 环境（业务与技术、价值流、业务能力）",
    "type": "concept",
    "parent": "business_scenario",
    "level": 1,
    "order": 2,
    "description_zh": "对应步骤 2：识别业务与技术环境，记录在包含价值流和业务能力的场景模型中。"
  },
  {
    "id": "e_outcomes",
    "label_en": "3 – Outcomes (SMART – Specific, Measurable, Actionable, Realistic, and Time-bound)",
    "label_zh": "3 – 成果（SMART：具体、可度量、可行动、现实、有时限）",
    "type": "goal",
    "parent": "business_scenario",
    "level": 1,
    "order": 3,
    "description_zh": "对应步骤 3：识别并记录期望成果。"
  },
  {
    "id": "e_human_actors",
    "label_en": "4 – Human Actors (capabilities, roles, and responsibilities)",
    "label_zh": "4 – 人的参与者（能力、角色与职责）",
    "type": "actor",
    "parent": "business_scenario",
    "level": 1,
    "order": 4,
    "description_zh": "对应步骤 4：识别人的参与者及其在业务模型中的位置。"
  },
  {
    "id": "e_computer_actors",
    "label_en": "5 – Computer Actors (capabilities, roles, and responsibilities)",
    "label_zh": "5 – 计算机参与者（能力、角色与职责）",
    "type": "application",
    "parent": "business_scenario",
    "level": 1,
    "order": 5,
    "description_zh": "对应步骤 5：识别计算机参与者（计算元素）及其在技术模型中的位置。"
  }
]
```

## 关系

```json
[
  {
    "from": "e_problem",
    "to": "e_environment",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "编号与阶梯排列表示顺序"
  },
  {
    "from": "e_environment",
    "to": "e_outcomes",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "e_outcomes",
    "to": "e_human_actors",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "e_human_actors",
    "to": "e_computer_actors",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_elements",
    "kind": "sequence",
    "name_zh": "业务场景五要素（步骤 1–5）",
    "steps": [
      "e_problem",
      "e_environment",
      "e_outcomes",
      "e_human_actors",
      "e_computer_actors"
    ],
    "description_zh": "第 6 步“检验是否适用、仅在必要时细化”不在图中；整个过程按需多轮迭代。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "带编号的圆角色块",
    "meaning_zh": "业务场景的一个要素；编号表示顺序",
    "explicit": false
  },
  {
    "symbol": "逐级右移的阶梯排列",
    "meaning_zh": "先后顺序，不是层级",
    "explicit": false
  },
  {
    "symbol": "括号内文字",
    "meaning_zh": "该要素涵盖的内容",
    "explicit": false
  },
  {
    "symbol": "深蓝到绿色的渐变",
    "meaning_zh": "视觉递进，无额外含义（推断）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "5 个宽色块自上而下排列，每块比上一块右移一段，形成向右下方的阶梯；颜色从深蓝（1）渐变到绿色（5）。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 18 页原图截图（220 dpi）",
    "英文 PDF 第 13、18、21 页正文",
    "中文稿 G176e_业务场景.md 第 62–92 行、第 131–150 行",
    "figs/g176_fig3-1.svg 源码"
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
