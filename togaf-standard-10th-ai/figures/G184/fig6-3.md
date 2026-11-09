# G184/fig6-3 · ISO 31000 风险管理标准模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G184/fig6-3.md) · [JSON](../../architecture/diagrams/G184/fig6-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G184e.pdf`；SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

## 原图 · PDF 第 67 页

![英文原图](../assets/G184/fig6-3-p0067.png)

PDF 坐标：`[125.6, 153.2, 486.4, 379.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
© The Open Group
(
,
.
Communication =>)
Establishing the Context
=>)
Tontoring nd)
and
}___|
Review
Consultation
Risk Assessment
(
Risk Identification
—_—_—
Risk Analysis
>)
—_—
Risk Evaluation
—
Risk Treatment
```

## 概要（历史解释；局部修正见上）

ISO 31000 风险管理过程：建立情境 → 风险识别、分析、评价 → 风险应对；沟通与咨询、监督与评审贯穿全程并形成闭环。

## 目的（历史解释；局部修正见上）

第 6.4 节要求 EA 能力与企业风险管理（ERM）紧密集成。第 6.4.2 节把 ISO 31000 作为 ERM 的权威标准介绍，并强调风险管理应深入嵌入所有业务活动，是持续的生命周期而不是孤立活动；本图给出该标准的风险管理过程模型，供领导者理解企业 ERM 的结构，并据此确定 EA 治理如何与之衔接。

## 阅读顺序（历史解释；局部修正见上）

先读中间一列，自上而下：建立情境 → 风险评估（大框内依次为风险识别 → 风险分析 → 风险评价）→ 风险应对。再看底部：风险应对的箭头折向右侧“监督与评审”；顶部：监督与评审的箭头折回“建立情境”，构成循环。左侧“沟通与咨询”和右侧“监督与评审”是通高竖框，用横线连到中间 5 个步骤，表示它们伴随每一步。各框右上角的空心箭头只是过程图标，不表示流向。

## 关键含义（历史解释；局部修正见上）

- 主过程有 5 步：建立情境、风险识别、风险分析、风险评价、风险应对；其中识别、分析、评价三步合称风险评估。
- 沟通与咨询、监督与评审是两项持续活动，与每个步骤都相连，贯穿整个过程，而不是某一步之后才做。
- 风险应对的结果进入监督与评审，监督与评审又反馈到建立情境，形成闭环：正文强调风险管理是持续的生命周期，而不是孤立活动。
- ISO 31000 把风险定义为“不确定性对目标的影响”，即任何偏离预期的结果；有效风险管理的核心是围绕预期目标进行管理，降低不确定性，并在正面与负面结果之间取得平衡。
- EA 能力的核心作用之一是营造一种环境，使运营风险得到优化，以实现最大业务收益和最小业务损失；这需要理解 ERM 的范围与关注点并与之紧密集成。
- 正文要求回答：企业的风险偏好和风险容忍度是什么；谁认可风险评估、谁认可风险应对计划。这些问题分别对应图中的风险评估与风险应对环节。
- （背景知识）图中步骤名称与 ISO 31000:2009 的过程模型一致；2018 版把“建立情境”扩展为“范围、情境与准则”，并增加了“记录与报告”。

## 层级（历史解释；局部修正见上）

两层：风险评估是一个分组框，内含风险识别、风险分析、风险评价三个子过程；其余步骤与两侧持续活动都是同级过程。

## 线条含义（历史解释；局部修正见上）

带实心箭头的线表示先后顺序：建立情境 → 风险识别 → 风险分析 → 风险评价 → 风险应对（第一条和最后一条分别穿过风险评估框的上、下边），以及两条折线回路：风险应对 → 监督与评审、监督与评审 → 建立情境。两侧竖框与每个步骤之间的横线没有箭头，表示该持续活动伴随此步骤，记为 association、无方向。各框右上角的空心箭头是过程图标，不是连线。

## 易误读点（历史解释；局部修正见上）

- 框右上角的空心箭头不表示流向，只是过程图标（背景知识：ArchiMate 风格的业务流程记法）。
- 两侧竖框与步骤之间的横线没有箭头，表示伴随与参与，不是单向的信息流。
- “风险评估”是三个子过程的分组，不是在风险识别之前的独立一步。
- 监督与评审回到建立情境的回路说明过程是循环的，不要读成从上到下只走一遍。
- 本图与 G152 图 3-3 是同一张图；G152 的图题注明 ISO 31000:2009，引用较新的 ISO 31000:2018 时步骤名称有变化（见背景知识）。

## 元素

```json
[
  {
    "id": "comm_consult",
    "label_en": "Communication and Consultation",
    "label_zh": "沟通与咨询",
    "type": "process",
    "parent": null,
    "position": "左侧通高竖框"
  },
  {
    "id": "monitor_review",
    "label_en": "Monitoring and Review",
    "label_zh": "监督与评审",
    "type": "process",
    "parent": null,
    "position": "右侧通高竖框"
  },
  {
    "id": "context",
    "label_en": "Establishing the Context",
    "label_zh": "建立情境",
    "type": "process",
    "parent": null,
    "order": 1,
    "position": "中间列顶部"
  },
  {
    "id": "risk_assessment",
    "label_en": "Risk Assessment",
    "label_zh": "风险评估",
    "type": "process",
    "parent": null,
    "position": "中间列中部的大圆角框",
    "description_zh": "分组框，内含识别、分析、评价三个子过程。"
  },
  {
    "id": "identification",
    "label_en": "Risk Identification",
    "label_zh": "风险识别",
    "type": "process",
    "parent": "risk_assessment",
    "order": 2
  },
  {
    "id": "analysis",
    "label_en": "Risk Analysis",
    "label_zh": "风险分析",
    "type": "process",
    "parent": "risk_assessment",
    "order": 3
  },
  {
    "id": "evaluation",
    "label_en": "Risk Evaluation",
    "label_zh": "风险评价",
    "type": "process",
    "parent": "risk_assessment",
    "order": 4
  },
  {
    "id": "treatment",
    "label_en": "Risk Treatment",
    "label_zh": "风险应对",
    "type": "process",
    "parent": null,
    "order": 5,
    "position": "中间列底部"
  }
]
```

## 关系

```json
[
  {
    "from": "context",
    "to": "identification",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "穿过风险评估框上边"
  },
  {
    "from": "identification",
    "to": "analysis",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "analysis",
    "to": "evaluation",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "evaluation",
    "to": "treatment",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "穿过风险评估框下边"
  },
  {
    "from": "treatment",
    "to": "monitor_review",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "底部折线：风险应对的结果进入监督与评审"
  },
  {
    "from": "monitor_review",
    "to": "context",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "顶部折线：监督与评审反馈到建立情境，构成循环"
  },
  {
    "from": "comm_consult",
    "to": "context",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "comm_consult",
    "to": "identification",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "comm_consult",
    "to": "analysis",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "comm_consult",
    "to": "evaluation",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "comm_consult",
    "to": "treatment",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "monitor_review",
    "to": "context",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "monitor_review",
    "to": "identification",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "monitor_review",
    "to": "analysis",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "monitor_review",
    "to": "evaluation",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "monitor_review",
    "to": "treatment",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_risk_cycle",
    "kind": "cycle",
    "name_zh": "风险管理过程循环",
    "steps": [
      "context",
      "identification",
      "analysis",
      "evaluation",
      "treatment",
      "monitor_review"
    ],
    "description_zh": "监督与评审之后回到建立情境。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "圆角矩形 + 右上角空心箭头",
    "meaning_zh": "一个过程/活动（空心箭头为过程图标）",
    "explicit": false
  },
  {
    "symbol": "包住三个框的大圆角框 Risk Assessment",
    "meaning_zh": "风险评估，由风险识别、分析、评价组成",
    "explicit": false
  },
  {
    "symbol": "实线 + 实心箭头",
    "meaning_zh": "过程的先后顺序与回路",
    "explicit": false
  },
  {
    "symbol": "左右两个通高竖框 + 无箭头横线",
    "meaning_zh": "贯穿全过程、伴随每一步的持续活动",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "三列：左侧通高竖框“沟通与咨询”，右侧通高竖框“监督与评审”，中间一列自上而下为建立情境、风险评估分组框（内含三个步骤）、风险应对；顶部和底部各有一条折线回路连接中间列与右侧竖框。"
}
```

## 相关图

```json
[
  {
    "target": "G152/fig3-3",
    "relation": "same_as",
    "note_zh": "同一张 ISO 31000 风险管理过程图：步骤、分组、两侧持续活动、横线与两条回路完全一致。G152 版本图题注明 ISO 31000:2009，图左上角有 © The Open Group，分辨率更高；本文档的截图较模糊，图题为 The ISO 31000 Standard Model for Risk Management。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "框右上角空心箭头按 ArchiMate 风格的过程图标解释（背景知识），原图没有图例。",
    "本文档图题没有写 ISO 31000 的版本，“2009 版”依据 G152 中同一张图的图题。"
  ],
  "analyzed_from": [
    "英文 PDF 第 67 页原图截图（220 dpi）",
    "G152 英文 PDF 第 24 页图 3-3 原图截图及中部放大（对照）",
    "英文 PDF 第 66–67 页正文（第 6.4、6.4.1、6.4.2 节）、第 68 页第 6 章尾注 [2]",
    "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 543–577 行",
    "figs/zh/g184e_fig6-3_zh.png（逐项比较）、figs/zh/g184e_fig6-3_zh.svg 源码"
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
