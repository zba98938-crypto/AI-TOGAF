# G212/fig4-1 · 数字技术采用的影响因素

> 当前图示解析：[Markdown](../../architecture/diagrams/G212/fig4-1.md) · [JSON](../../architecture/diagrams/G212/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G212e.pdf`；SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

## 原图 · PDF 第 27 页

![英文原图](../assets/G212/fig4-1-p0027.png)

PDF 坐标：`[74.0, 36.0, 538.0, 311.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Legend
Vision
Triggers
—T—
Assists
{Funding and Resources
+} Sponsorship and Direction
Defines
Stimulates
‘Scope and Scale
ee
Business Rationale
Leads to
Catalyzes
Organization's
Empowers
Culture
Digital
Technology
Readiness
Drives
‘Governance and
Enhances
Sowers +) Implementation Approach jest
IT Capability
Compliance
¥
‘Quantities
Complements
Conduces
Results in
Skills and
Value Realization
Ecosystem
‘Competence
Technotony Maturity fA
‘Augments,
Policy and Regulations
fhe Open Group
```

## 概要（历史解释；局部修正见上）

用 17 条带标签的箭头画出 15 个数字技术采用因素之间的强依赖，汇聚到“组织数字技术就绪度”。

## 目的（历史解释；局部修正见上）

表 4-1 只把 15 个因素分成基础/影响/持续三类，作者再用这张依赖图说明它们并非并列清单：愿景、赞助、范围、实施方法等相互牵动，最终共同决定组织就绪度。正文明确说图中只画“最强、最主要”的关系，避免把所有弱关系都堆上去。

## 阅读顺序（历史解释；局部修正见上）

先看图例认三种形状，再找中心的菱形“Organization's Digital Technology Readiness”，这是全图汇聚点。然后从左上“Vision”读起：箭头旁的深青色斜体动词说明源因素如何影响目标因素（Aspires、Triggers、Defines 等）。箭头是“影响/促成”，不是流程步骤；同一因素可以有多条进出箭头。

## 关键含义（历史解释；局部修正见上）

- 15 个因素分三类：基础 7 个（愿景、赞助与方向、IT 能力、文化、范围与规模、业务理由、实施方法）、影响 5 个（治理与合规、技能与胜任力、业务模式适应性、技术成熟度、生态系统）、持续 3 个（价值实现、政策与法规、资金与资源）。
- 愿景位于最上方，同时“期望”赞助与方向、“触发”范围与规模；正文解释清晰的愿景有助于找到赞助者、设定方向并界定范围。
- 范围与规模是上游汇聚点：赞助与方向“定义”它、业务理由“刺激”它、资金与资源“协助”赞助、业务模式适应性“催化”业务理由；范围再“导致”组织就绪度。
- 实施方法是操作层面的枢纽：治理与合规“治理”它、价值实现“量化”它、IT 能力“增强”它、技术成熟度“传导”它，它再“驱动”组织就绪度。
- 技术成熟度受政策与法规“扩充”、并被生态系统“导致”；生态系统同时“补充”IT 能力，技能与胜任力“提升”IT 能力。
- 文化直接“赋能”组织就绪度，是唯一不经实施方法/范围而直达中心的因素，说明组织文化被视为横贯性的使能条件。
- 图中只画强而主导的关系，不能当作因果全集；缺失的弱关系不代表不存在。

## 层级（历史解释；局部修正见上）

没有上下级包含关系，是一张以“组织数字技术就绪度”为中心的依赖网络。三类因素用形状区分（矩形/平行四边形/圆角矩形），但图上没有用分区或泳道把它们摆成三层；类别只由形状和图例表达。

## 线条含义（历史解释；局部修正见上）

全部为黑色实线箭头，箭头指向被影响的因素；箭头旁的深青色斜体词是关系标签（Aspires/Triggers/Assists/Defines/Stimulates/Catalyzes/Leads to/Empowers/Governs/Quantifies/Drives/Strengthens/Complements/Results in/Conducts/Augments/Enhances）。折线只用于避让，转角不代表中间节点。所有关系均为正向促进（polarity=+），图中没有负向或反馈箭头。

## 易误读点（历史解释；局部修正见上）

- 箭头不是流程步骤：例如“Leads to”“Results in”只表示因素间的影响，不表示时间先后或阶段转换。
- 形状编码的是因素类别而不是重要性：治理与合规画成平行四边形（影响因素），尽管“治理”听起来像基础因素；业务理由画成矩形（基础因素），尽管它靠近右侧的影响因素。
- 中心菱形不是第 16 个因素，表 4-1 只有 15 个；它是被评估的整体状态。
- 图中关系不完整：正文明确只画最强、最主要的关系，不能据图推断两个未连线因素之间没有影响。
- 中文稿引用的 figs/g212_fig4-1.svg 是三列清单，17 条关系全部丢失，还在类别之间自拟了递进箭头；不能据它理解本图。
- 中文稿的 figs/zh/g212e_fig4-1_zh.png 平行四边形和中心菱形边框破损，形状编码不完整，应以英文原图核对类别。

## 元素

```json
[
  {
    "id": "vision",
    "label_en": "Vision",
    "label_zh": "愿景",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "顶部中央",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "sponsorship",
    "label_en": "Sponsorship and Direction",
    "label_zh": "赞助与方向",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "Vision 下方",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "scope",
    "label_en": "Scope and Scale",
    "label_zh": "范围与规模",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "中部偏右",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "business_rationale",
    "label_en": "Business Rationale",
    "label_zh": "业务理由",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "右上方",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "funding",
    "label_en": "Funding and Resources",
    "label_zh": "资金与资源",
    "type": "concept",
    "notation_type": "圆角矩形（持续因素）",
    "parent": null,
    "position": "左上",
    "attributes": {
      "factor_class": "sustaining"
    }
  },
  {
    "id": "culture",
    "label_en": "Culture",
    "label_zh": "文化",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "左中",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "readiness",
    "label_en": "Organization's Digital Technology Readiness",
    "label_zh": "组织数字技术就绪度",
    "type": "metric",
    "notation_type": "菱形（中心）",
    "parent": null,
    "position": "页面中部偏左",
    "description_zh": "全图汇聚点，评估的整体状态；不是表 4-1 中的第 16 个因素。"
  },
  {
    "id": "governance",
    "label_en": "Governance and Compliance",
    "label_zh": "治理与合规",
    "type": "concept",
    "notation_type": "平行四边形（影响因素）",
    "parent": null,
    "position": "左下",
    "attributes": {
      "factor_class": "impact"
    }
  },
  {
    "id": "implementation",
    "label_en": "Implementation Approach",
    "label_zh": "实施方法",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "下中",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "it_capability",
    "label_en": "IT Capability",
    "label_zh": "IT 能力",
    "type": "concept",
    "notation_type": "矩形（基础因素）",
    "parent": null,
    "position": "右下中",
    "attributes": {
      "factor_class": "foundational"
    }
  },
  {
    "id": "value_realization",
    "label_en": "Value Realization",
    "label_zh": "价值实现",
    "type": "concept",
    "notation_type": "圆角矩形（持续因素）",
    "parent": null,
    "position": "左下角",
    "attributes": {
      "factor_class": "sustaining"
    }
  },
  {
    "id": "technology_maturity",
    "label_en": "Technology Maturity",
    "label_zh": "技术成熟度",
    "type": "concept",
    "notation_type": "平行四边形（影响因素）",
    "parent": null,
    "position": "底部中左",
    "attributes": {
      "factor_class": "impact"
    }
  },
  {
    "id": "ecosystem",
    "label_en": "Ecosystem",
    "label_zh": "生态系统",
    "type": "concept",
    "notation_type": "平行四边形（影响因素）",
    "parent": null,
    "position": "底部中右",
    "attributes": {
      "factor_class": "impact"
    }
  },
  {
    "id": "skills",
    "label_en": "Skills and Competence",
    "label_zh": "技能与胜任力",
    "type": "concept",
    "notation_type": "平行四边形（影响因素）",
    "parent": null,
    "position": "右下角",
    "attributes": {
      "factor_class": "impact"
    }
  },
  {
    "id": "policy",
    "label_en": "Policy and Regulations",
    "label_zh": "政策与法规",
    "type": "concept",
    "notation_type": "圆角矩形（持续因素）",
    "parent": null,
    "position": "最底部",
    "attributes": {
      "factor_class": "sustaining"
    }
  },
  {
    "id": "business_model",
    "label_en": "Business Model Adaptability",
    "label_zh": "业务模式适应性",
    "type": "concept",
    "notation_type": "平行四边形（影响因素）",
    "parent": null,
    "position": "右侧中部",
    "attributes": {
      "factor_class": "impact"
    }
  }
]
```

## 关系

```json
[
  {
    "from": "vision",
    "to": "sponsorship",
    "type": "influence",
    "label_en": "Aspires",
    "label_zh": "期望",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "箭头向下"
  },
  {
    "from": "vision",
    "to": "scope",
    "type": "influence",
    "label_en": "Triggers",
    "label_zh": "触发",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "自 Vision 右侧折向下进入 Scope and Scale 顶部"
  },
  {
    "from": "funding",
    "to": "sponsorship",
    "type": "influence",
    "label_en": "Assists",
    "label_zh": "协助",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "sponsorship",
    "to": "scope",
    "type": "influence",
    "label_en": "Defines",
    "label_zh": "定义",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "business_rationale",
    "to": "scope",
    "type": "influence",
    "label_en": "Stimulates",
    "label_zh": "刺激",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "箭头向左"
  },
  {
    "from": "business_model",
    "to": "business_rationale",
    "type": "influence",
    "label_en": "Catalyzes",
    "label_zh": "催化",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "scope",
    "to": "readiness",
    "type": "influence",
    "label_en": "Leads to",
    "label_zh": "导致",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "自 Scope 底部折向左下，进入菱形顶部"
  },
  {
    "from": "culture",
    "to": "readiness",
    "type": "influence",
    "label_en": "Empowers",
    "label_zh": "赋能",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "governance",
    "to": "implementation",
    "type": "influence",
    "label_en": "Governs",
    "label_zh": "治理",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "value_realization",
    "to": "implementation",
    "type": "influence",
    "label_en": "Quantifies",
    "label_zh": "量化",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "折线先向上再向右"
  },
  {
    "from": "implementation",
    "to": "readiness",
    "type": "influence",
    "label_en": "Drives",
    "label_zh": "驱动",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "it_capability",
    "to": "implementation",
    "type": "influence",
    "label_en": "Strengthens",
    "label_zh": "增强",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "箭头向左"
  },
  {
    "from": "skills",
    "to": "it_capability",
    "type": "influence",
    "label_en": "Enhances",
    "label_zh": "提升",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "折线先向上再向左"
  },
  {
    "from": "ecosystem",
    "to": "it_capability",
    "type": "influence",
    "label_en": "Complements",
    "label_zh": "补充",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "ecosystem",
    "to": "technology_maturity",
    "type": "influence",
    "label_en": "Results in",
    "label_zh": "导致",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "箭头向左"
  },
  {
    "from": "technology_maturity",
    "to": "implementation",
    "type": "influence",
    "label_en": "Conducts",
    "label_zh": "传导",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "from": "policy",
    "to": "technology_maturity",
    "type": "influence",
    "label_en": "Augments",
    "label_zh": "扩充",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+"
  }
]
```

## 图例

```json
[
  {
    "symbol": "矩形（直角框）",
    "meaning_zh": "基础因素 Foundational Factor",
    "explicit": true
  },
  {
    "symbol": "平行四边形（左右斜边）",
    "meaning_zh": "影响因素 Impact Factor",
    "explicit": true
  },
  {
    "symbol": "圆角矩形",
    "meaning_zh": "持续因素 Sustaining Factor",
    "explicit": true
  },
  {
    "symbol": "菱形",
    "meaning_zh": "组织数字技术就绪度（全图汇聚点，非因素类别）",
    "explicit": false
  },
  {
    "symbol": "深青色斜体词 + 黑色实线箭头",
    "meaning_zh": "源因素对目标因素的影响方式；箭头指向被影响者",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "自由布局：Vision 在顶部中央偏左，中心菱形在页面中部偏左；上方为由愿景、赞助、范围、业务理由、业务模式适应性构成的横向链；左中为资金与文化；下方为治理、价值实现、实施方法、技术成熟度、政策、生态系统、IT 能力、技能；图例在右上角。"
}
```

## 相关图

```json
[
  {
    "target": "G212/fig5-3",
    "relation": "complements",
    "note_zh": "图 5-3 的缺失因素后果沿用同一套 15 个因素，正文并提示后果会相互强化、参见本图"
  },
  {
    "target": "G212/fig5-4",
    "relation": "related",
    "note_zh": "图 5-4 按基础/影响/持续三层把因素递进简化为三类企业，本图给出层内因素之间的依赖"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "17 条箭头的文字均为图内斜体小字，已按 2×2 放大块逐条核对；其中“Conducts”在中文稿对照表中缺失，译名“传导”为解析者拟定。",
    "“Aspires”的主语可理解为组织对愿景的期望，图中只给出 Vision → Sponsorship and Direction 的方向；本分析按箭头方向记录，不扩展语义。",
    "所有关系按正向影响处理（polarity=+），图中没有负号或减弱标记。"
  ],
  "analyzed_from": [
    "英文 PDF 第 27 页原图截图（2×2 放大分块）",
    "英文 PDF 第 26–27 页正文（含表 4-1 与 Vision 段落）",
    "中文稿 G212e_数字技术采用就绪度评估.md 第 250–295 行（含图内标签对照表 L272–L295）",
    "figs/zh/g212e_fig4-1_zh.png",
    "figs/g212_fig4-1.svg 源码",
    "figs/g212e_fig4-1_en.png（自动相似度 0.994）"
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
