# G152/fig3-2 · SABSA 运营风险模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G152/fig3-2.md) · [JSON](../../architecture/diagrams/G152/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G152e.pdf`；SHA-256：`919c53bfa4259a4b3a9686762f37c0576a1cd2f8e77e74648826d9f9c84ed6e0`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G152/fig3-2-p0023.png)

PDF 坐标：`[61.1, 36.0, 550.9, 366.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Negative
Risk context
Positive
outcomes
<a
—p>
outcomes
Assets
at risk
Likelihood of
Asset
Asset
Likelihood of
threat
value
value
opportunity
materialising
materialising
Likelihood of
Negative
Positive
Lil
ood of
weakness
impact
impact
st
gth
exploited
value
value
exploited
%
2
```

## 概要（历史解释；局部修正见上）

SABSA 运营风险模型：以处于风险中的资产为中心，把威胁导致损失与机会带来收益画成左右对称的两条链。

## 目的（历史解释；局部修正见上）

纠正“风险只等于威胁与损失”的行业惯性：先由 Risk context 给出风险语境，再把处于风险中的资产分别放到负向（威胁/损失）与正向（机会/收益）两条对称链上，用可能性和货币价值两个维度量化，说明风险管理是在正负结果之间取得平衡。

## 阅读顺序（历史解释；局部修正见上）

从顶部中央的 Risk context 读起：红色箭头向左指向 Negative outcomes，绿色箭头向右指向 Positive outcomes；向下则进入 Assets at risk。由 Assets at risk 向下分叉，向左、向右各有一个箭头指向两侧的 Asset value，表示同一组资产在两条链上都被估值。左支红色：Threats 下的“威胁发生可能性/弱点被利用可能性”（%）与“资产价值/负面影响值”（€）共同导致 Loss event；右支绿色：Opportunities 下的“资产价值/正面影响值”（€）与“机会出现可能性/优势被利用可能性”（%）共同导致 Beneficial event。

## 关键含义（历史解释；局部修正见上）

- 风险语境（Risk context）同时产生负向结果与正向结果两种可能，图中用红色左箭头与绿色右箭头并列表示，没有偏向任何一侧。
- 处于风险中的资产（Assets at risk）位于模型中心，并向左右两侧的 Asset value 各发出一条箭头：同一资产既承受威胁，也可能带来机会。
- 左支（红/橙）表示威胁侧：两个可能性框以 % 计量（威胁发生的可能性、弱点被利用的可能性），两个价值框以 € 计量（资产价值、负面影响值），汇总为 Loss event。
- 右支（绿）与左支严格对称：机会侧同样有 % 列（机会出现的可能性、优势被利用的可能性）与 € 列（资产价值、正面影响值），汇总为 Beneficial event。
- 模型把“资产价值”在两侧各画一次，强调风险计算的分母/基准相同，只是影响方向相反：负向为损失，正向为收益。
- 四列底部的 % 与 € 大符号标明了两个量化维度：可能性与货币影响；这也解释了 SABSA 为何要求业务属性可度量。
- 该图是第 3 章“平衡的风险观”的图形依据：运营风险既要控制损失事件，也要使能收益事件。

## 层级（历史解释；局部修正见上）

三层。第 1 层是两个核心概念：Risk context 与 Assets at risk（后者由前者向下引出）；第 2 层是左右两条对称支路及其类别带（Threats / Opportunities）；第 3 层是每条支路内的可能性列与价值列，以及底部的 Loss event / Beneficial event 结果条。左右两支是并列关系，不是先后步骤。

## 线条含义（历史解释；局部修正见上）

深蓝色箭头表示概念间的推导方向：Risk context → 负向/正向结果，Risk context → Assets at risk，Assets at risk → 两侧 Asset value。左侧红色双线箭头与右侧绿色箭头是同一关系的两种结果方向，不是对立箭头。两个“Assets at risk → Asset value”箭头分别指向左右，强调双向估值。底部事件条与上方列之间没有画箭头，风险=可能性×影响值的合成关系由上下叠放隐含。

## 易误读点（历史解释；局部修正见上）

- 不要只读左支：右支 Opportunities → Beneficial event 与左支同等重要，是模型的一半。
- 两侧各有一个 Asset value 框，不是两个不同的资产；指的是同一组处于风险中的资产在正负两条链上的估值。
- Threats 与 Opportunities 是两条并列类别带，不是先后阶段；Loss event 与 Beneficial event 也不是时间上的先后。
- Risk context 左右的两个箭头不是“输入/输出”，而是同一风险语境下的两种结果可能。
- 图中没有画出乘法公式；% 与 € 只是列单位，不能据此推断具体计算公式或权重。

## 元素

```json
[
  {
    "id": "risk_context",
    "label_en": "Risk context",
    "label_zh": "风险语境",
    "type": "concept",
    "parent": null,
    "position": "顶部中央深蓝框"
  },
  {
    "id": "negative_outcomes",
    "label_en": "Negative outcomes",
    "label_zh": "负向结果",
    "type": "concept",
    "parent": null,
    "position": "左上红色文字"
  },
  {
    "id": "positive_outcomes",
    "label_en": "Positive outcomes",
    "label_zh": "正向结果",
    "type": "concept",
    "parent": null,
    "position": "右上绿色文字"
  },
  {
    "id": "assets_at_risk",
    "label_en": "Assets at risk",
    "label_zh": "处于风险中的资产",
    "type": "concept",
    "parent": null,
    "position": "Risk context 正下方深蓝框"
  },
  {
    "id": "threats",
    "label_en": "Threats",
    "label_zh": "威胁",
    "type": "risk",
    "parent": null,
    "position": "左支红色标题带",
    "description_zh": "横跨左支两个列。"
  },
  {
    "id": "opportunities",
    "label_en": "Opportunities",
    "label_zh": "机会",
    "type": "goal",
    "parent": null,
    "position": "右支绿色标题带",
    "description_zh": "横跨右支两个列。"
  },
  {
    "id": "likelihood_threat",
    "label_en": "Likelihood of threat materialising",
    "label_zh": "威胁发生的可能性",
    "type": "metric",
    "parent": "threats",
    "position": "左支左列上格"
  },
  {
    "id": "likelihood_weakness",
    "label_en": "Likelihood of weakness exploited",
    "label_zh": "弱点被利用的可能性",
    "type": "metric",
    "parent": "threats",
    "position": "左支左列下格"
  },
  {
    "id": "pct_threat",
    "label_en": "%",
    "label_zh": "百分比（%）",
    "type": "metric",
    "parent": "threats",
    "position": "左支左列底部",
    "description_zh": "该列的单位标记。"
  },
  {
    "id": "asset_value_threat",
    "label_en": "Asset value",
    "label_zh": "资产价值（威胁侧）",
    "type": "metric",
    "parent": "threats",
    "position": "左支右列上格"
  },
  {
    "id": "negative_impact",
    "label_en": "Negative impact value",
    "label_zh": "负面影响值",
    "type": "metric",
    "parent": "threats",
    "position": "左支右列下格"
  },
  {
    "id": "eur_threat",
    "label_en": "€",
    "label_zh": "欧元（€）",
    "type": "metric",
    "parent": "threats",
    "position": "左支右列底部",
    "description_zh": "该列的单位标记。"
  },
  {
    "id": "loss_event",
    "label_en": "Loss event",
    "label_zh": "损失事件",
    "type": "event",
    "parent": null,
    "position": "左支底部红色横条"
  },
  {
    "id": "asset_value_opp",
    "label_en": "Asset value",
    "label_zh": "资产价值（机会侧）",
    "type": "metric",
    "parent": "opportunities",
    "position": "右支左列上格"
  },
  {
    "id": "positive_impact",
    "label_en": "Positive impact value",
    "label_zh": "正面影响值",
    "type": "metric",
    "parent": "opportunities",
    "position": "右支左列下格"
  },
  {
    "id": "eur_opp",
    "label_en": "€",
    "label_zh": "欧元（€）",
    "type": "metric",
    "parent": "opportunities",
    "position": "右支左列底部",
    "description_zh": "该列的单位标记。"
  },
  {
    "id": "likelihood_opportunity",
    "label_en": "Likelihood of opportunity materialising",
    "label_zh": "机会出现的可能性",
    "type": "metric",
    "parent": "opportunities",
    "position": "右支右列上格"
  },
  {
    "id": "likelihood_strength",
    "label_en": "Likelihood of strength exploited",
    "label_zh": "优势被利用的可能性",
    "type": "metric",
    "parent": "opportunities",
    "position": "右支右列下格"
  },
  {
    "id": "pct_opp",
    "label_en": "%",
    "label_zh": "百分比（%）",
    "type": "metric",
    "parent": "opportunities",
    "position": "右支右列底部",
    "description_zh": "该列的单位标记。"
  },
  {
    "id": "beneficial_event",
    "label_en": "Beneficial event",
    "label_zh": "收益事件",
    "type": "event",
    "parent": null,
    "position": "右支底部绿色横条"
  }
]
```

## 关系

```json
[
  {
    "id": "r1",
    "from": "risk_context",
    "to": "negative_outcomes",
    "type": "influence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "红色粗双线箭头向左；from 取箭尾的 Risk context，to 取箭头所指的 Negative outcomes。"
  },
  {
    "id": "r2",
    "from": "risk_context",
    "to": "positive_outcomes",
    "type": "influence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "绿色粗箭头向右。"
  },
  {
    "id": "r3",
    "from": "risk_context",
    "to": "assets_at_risk",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "深蓝色向下箭头。"
  },
  {
    "id": "r4",
    "from": "assets_at_risk",
    "to": "asset_value_threat",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Assets at risk 底部向下再向左折，箭头指向左侧 Asset value。"
  },
  {
    "id": "r5",
    "from": "assets_at_risk",
    "to": "asset_value_opp",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同一分叉向右，箭头指向右侧 Asset value。"
  },
  {
    "id": "r6",
    "from": "threats",
    "to": "likelihood_threat",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "红色标题带横跨左支两个列，由位置表示归属。"
  },
  {
    "id": "r7",
    "from": "threats",
    "to": "asset_value_threat",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r8",
    "from": "opportunities",
    "to": "asset_value_opp",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r9",
    "from": "opportunities",
    "to": "likelihood_opportunity",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r10",
    "from": "likelihood_weakness",
    "to": "pct_threat",
    "type": "aggregation",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同列底部 % 表示该列以百分比计量。"
  },
  {
    "id": "r11",
    "from": "negative_impact",
    "to": "eur_threat",
    "type": "aggregation",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同列底部 € 表示该列以货币计量。"
  },
  {
    "id": "r12",
    "from": "positive_impact",
    "to": "eur_opp",
    "type": "aggregation",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r13",
    "from": "likelihood_strength",
    "to": "pct_opp",
    "type": "aggregation",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r14",
    "from": "likelihood_weakness",
    "to": "loss_event",
    "type": "causal",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "可能性 × 影响值合成损失事件；原图仅以上下叠放表示，未画箭头。"
  },
  {
    "id": "r15",
    "from": "negative_impact",
    "to": "loss_event",
    "type": "causal",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "polarity": "+"
  },
  {
    "id": "r16",
    "from": "likelihood_strength",
    "to": "beneficial_event",
    "type": "causal",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "机会侧同理合成收益事件，未画箭头。"
  },
  {
    "id": "r17",
    "from": "positive_impact",
    "to": "beneficial_event",
    "type": "causal",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "polarity": "+"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_negative",
    "kind": "sequence",
    "name_zh": "负向风险链",
    "steps": [
      "risk_context",
      "assets_at_risk",
      "negative_impact",
      "loss_event"
    ],
    "description_zh": "风险语境 → 处于风险中的资产 → 负面影响值 → 损失事件（合成关系为隐含）。"
  },
  {
    "id": "f_positive",
    "kind": "sequence",
    "name_zh": "正向机会链",
    "steps": [
      "risk_context",
      "assets_at_risk",
      "positive_impact",
      "beneficial_event"
    ],
    "description_zh": "风险语境 → 处于风险中的资产 → 正面影响值 → 收益事件。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "红色左向双线箭头 + 红色类别带",
    "meaning_zh": "负向结果链：威胁、损失事件",
    "explicit": false
  },
  {
    "symbol": "绿色右向箭头 + 绿色类别带",
    "meaning_zh": "正向结果链：机会、收益事件",
    "explicit": false
  },
  {
    "symbol": "橙色列",
    "meaning_zh": "威胁侧的两个量化列：可能性（%）与影响值（€）",
    "explicit": false
  },
  {
    "symbol": "浅绿色列",
    "meaning_zh": "机会侧的量化列：影响值（€）与可能性（%）",
    "explicit": false
  },
  {
    "symbol": "深蓝色框",
    "meaning_zh": "模型的两个核心概念：Risk context、Assets at risk",
    "explicit": false
  },
  {
    "symbol": "% 与 € 大符号",
    "meaning_zh": "该列使用的度量单位：百分比（可能性）与货币（价值）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "顶部中央 Risk context；其下为 Assets at risk；左右对称展开两条支路，左红右绿；每条支路内为“可能性列（%）+ 价值列（€）”；底部各有一条结果条（Loss event / Beneficial event）。"
}
```

## 相关图

```json
[
  {
    "target": "G152/fig3-1",
    "relation": "follows",
    "note_zh": "图 3-1 说明风险出现在业务栈的哪些层次，本图随后给出 SABSA 的运营风险正负对称模型。"
  },
  {
    "target": "G152/fig3-3",
    "relation": "complements",
    "note_zh": "两者都是风险模型：本图为 SABSA 的正负结果平衡观，图 3-3 为 ISO 31000 的过程观，正文并列引用。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "Assets at risk 到左右两个 Asset value 的连线在原图中是一条向下分叉、两端各带箭头的折线；本分析拆成两条关系记录。",
    "底部事件条与上方列之间没有画箭头，本分析把“可能性×影响值→事件”记为隐含因果（polarity +），属于对模型含义的解读。",
    "图中 % 与 € 的确切含义（可能性百分比、货币价值）由图题与 SABSA 背景推断，图内无文字说明。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页原图截图（220 dpi）及 2x2 放大分块",
    "英文 PDF 第 22–23 页正文",
    "中文稿 G152e_将风险与安全融入TOGAF企业架构.md 第 192、194 行"
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
