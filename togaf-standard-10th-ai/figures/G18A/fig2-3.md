# G18A/fig2-3 · 业务模型立方体

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/fig2-3.md) · [JSON](../../architecture/diagrams/G18A/fig2-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 14 页

![英文原图](../assets/G18A/fig2-3-p0014.png)

PDF 坐标：`[99.8, 36.0, 512.2, 380.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Customers
Relations Relati
Relations Relati
Relations Relati
Relations
Relati
Value Formulas
Relations Relati
Relations R
elati
Relations Relat
Relations Relat
|
R
lations
```

## 概要（历史解释；局部修正见上）

用六块面板围合一个写满 Relations 的立方体，表示业务模型由价值主张、客户、能力等多维要素及其关系构成。

## 目的（历史解释；局部修正见上）

介绍 Lindgren 与 Rasmussen 的业务模型立方体，说明业务模型除了清单式框架外，还可以用多维、可组合、可拆看某一面的立体结构来表示，强调「关系」而非单块内容。

## 阅读顺序（历史解释；局部修正见上）

先看中央蓝色立方体：它表面密密麻麻重复印着 Relations，是全图的核心。再看向外拉开的六块面板：顶部品红为 Value Propositions，底部暗红为 Competences，左侧蓝紫为 Activities，左后方橙色为 Customers，右后方绿色为 Network Partners，右侧橙色为 Value Formulas。面板之间没有连线，靠「围绕中心立方体」表达维度与整体的关系。

## 关键含义（历史解释；局部修正见上）

- 六个维度分别是 Value Propositions、Customers、Network Partners、Activities、Competences、Value Formulas。
- 中央立方体表面重复写满 Relations，强调六维之间的相互关系才是业务模型的核心，六块面板只是维度本身。
- 面板被画成「拉开的外壳」，表示可以单独审视某一维度；合拢起来才构成完整立方体。
- 顶面（价值主张）与底面（能力）相对，左右与后方是活动、客户、网络伙伴、价值公式，位置本身没有严格的层级或顺序。
- 图中没有任何箭头或流程，也没有客户细分、渠道、成本结构等画布块，不能当作业务模型画布使用。
- 六种颜色只用于区分面板，图中没有颜色含义说明。

## 层级（历史解释；局部修正见上）

两层：中央 Relations 立方体代表「关系」这一核心；六块外围面板代表六个维度，彼此并列，均从属于整个立方体。图中没有上级框，也没有把六维再分解。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头。六块面板与中央立方体之间只靠空间围绕关系表达「维度围绕关系」；面板之间的相对位置也不表示连线。

## 易误读点（历史解释；局部修正见上）

- 不要把中央的 Relations 当成第七个维度：它是模型的核心对象（关系），不是一块面板。
- 不要把六块面板读成六个步骤或先后顺序，它们同时存在、可任意组合。
- 不要把面板的上下左右位置当成层级（例如以为 Value Propositions 高于 Competences）。
- 中文稿第 99 行引用的 SVG 只画了三面，并自拟了“客户/渠道”“资源/伙伴”“成本/收入”，与原图六维名称不符，不能据它理解本图。

## 元素

```json
[
  {
    "id": "relations_cube",
    "label_en": "Relations",
    "label_zh": "关系（立方体）",
    "type": "concept",
    "parent": null,
    "level": 0,
    "position": "画面中央，被六块面板围绕",
    "description_zh": "蓝色立方体，三个可见面均重复印有 Relations 字样；原图以此表示六维之间的关系。"
  },
  {
    "id": "value_propositions",
    "label_en": "Value Propositions",
    "label_zh": "价值主张",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "顶部品红色平板（立方体顶面）"
  },
  {
    "id": "customers",
    "label_en": "Customers",
    "label_zh": "客户",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "左后方橙色竖板（立方体后面）"
  },
  {
    "id": "network_partners",
    "label_en": "Network Partners",
    "label_zh": "网络伙伴",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "右后方绿色竖板（立方体后面）"
  },
  {
    "id": "activities",
    "label_en": "Activities",
    "label_zh": "活动",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "左侧蓝紫色竖板（立方体左面）"
  },
  {
    "id": "value_formulas",
    "label_en": "Value Formulas",
    "label_zh": "价值公式",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "右侧橙色竖板（立方体右面）"
  },
  {
    "id": "competences",
    "label_en": "Competences",
    "label_zh": "能力",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "底部暗红色平板（立方体底面）"
  }
]
```

## 关系

```json
[
  {
    "id": "r_vp_cube",
    "from": "value_propositions",
    "to": "relations_cube",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "空间围绕：价值主张面板是立方体顶面，图中没有画线。"
  },
  {
    "id": "r_customers_cube",
    "from": "customers",
    "to": "relations_cube",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "空间围绕：客户面板位于立方体后方，图中没有画线。"
  },
  {
    "id": "r_partners_cube",
    "from": "network_partners",
    "to": "relations_cube",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "空间围绕：网络伙伴面板位于立方体后方，图中没有画线。"
  },
  {
    "id": "r_activities_cube",
    "from": "activities",
    "to": "relations_cube",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "空间围绕：活动面板位于立方体左面，图中没有画线。"
  },
  {
    "id": "r_formulas_cube",
    "from": "value_formulas",
    "to": "relations_cube",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "空间围绕：价值公式面板位于立方体右面，图中没有画线。"
  },
  {
    "id": "r_competences_cube",
    "from": "competences",
    "to": "relations_cube",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "空间围绕：能力面板是立方体底面，图中没有画线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色立方体 + 重复的 Relations 字样",
    "meaning_zh": "业务模型的核心是各维度之间的关系",
    "explicit": false
  },
  {
    "symbol": "品红顶板",
    "meaning_zh": "Value Propositions 维度",
    "explicit": false
  },
  {
    "symbol": "暗红底板",
    "meaning_zh": "Competences 维度",
    "explicit": false
  },
  {
    "symbol": "蓝紫左侧板",
    "meaning_zh": "Activities 维度",
    "explicit": false
  },
  {
    "symbol": "橙色左后板",
    "meaning_zh": "Customers 维度",
    "explicit": false
  },
  {
    "symbol": "绿色右后板",
    "meaning_zh": "Network Partners 维度",
    "explicit": false
  },
  {
    "symbol": "橙色右侧板",
    "meaning_zh": "Value Formulas 维度",
    "explicit": false
  },
  {
    "symbol": "不同颜色",
    "meaning_zh": "仅区分六块面板，无额外编码含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中央为蓝色立方体；六块彩色面板分布在它的上、下、左、右前、右后、左后方，像被拉开的外壳。没有连线，靠包围式构图表达整体。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig2-1",
    "relation": "complements",
    "note_zh": "第 2 节并列介绍的另一种业务模型表示"
  },
  {
    "target": "G18A/fig2-2",
    "relation": "complements",
    "note_zh": "四框框架与本立方体同为第 2 节列举的框架示例"
  },
  {
    "target": "G18A/fig2-4",
    "relation": "complements",
    "note_zh": "立方体与业务模型画布是同一主题的不同表示方式"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "中央立方体纹理中的文字放大后辨认为重复的 Relations，原书可能用 Relationships，无法从图中确认。",
    "六个面板与立方体六个面的严格对应关系（哪块面板是哪个面）在透视中被拉开，只能按大致方位判断。",
    "图中未说明六个维度之间是否存在优先顺序。",
    "Network Partners、Activities、Value Formulas、Competences 的中文译名由解析者拟定，中文稿未给出对照。"
  ],
  "analyzed_from": [
    "英文 PDF 第 14 页原图截图（fig2-3_p14_1.png）及 3×3 放大分块（重点 z22 中央立方体）",
    "英文 PDF 第 14 页正文",
    "中文稿 G18Ae_业务模型.md 第 95–99 行",
    "figs/g18a_fig2-3.svg 源码与 SVG 文本"
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
