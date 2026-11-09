# G190/fig4-1 · 业务能力与信息概念

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/fig4-1.md) · [JSON](../../architecture/diagrams/G190/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 14 页

![英文原图](../assets/G190/fig4-1-p0014.png)

PDF 坐标：`[86.9, 435.0, 525.1, 720.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Capabilities
Information Concepts
C>),
Modifies
(a >
Investment
Uses
Investment
Management
Uses
ey,
Financial
—
Uses
Financial
Instrument
Modifies
Instrument
Management
we
(nn )
Payment
Uses
Modifies
Payment
Management
we
yse®
_
Financial
Use:
Financial
Transaction
Modifies
+|
Transaction
Management
Source: Business Architecture Guild® 2019
```

## 概要（历史解释；局部修正见上）

把 4 项投资类业务能力与 4 个信息概念交叉连线，用红/蓝箭头区分“能力修改信息”与“能力使用信息”。

## 目的（历史解释；局部修正见上）

第 4 章说明信息地图与业务能力地图联系最紧密：设计未来态架构时能力使用信息概念，能力也确立（修改）信息概念。本图用“投资”场景给出能力—信息交叉映射的一个子集，示范如何在不假定数据存储或系统的前提下描述业务制品。

## 阅读顺序（历史解释；局部修正见上）

先读左右两列标题（Capabilities / Information Concepts），再按行看红色水平箭头：每项能力修改与它同名的信息概念。然后看蓝色斜线：从右列信息概念出发、箭头落在左列能力上的，表示该能力使用这个信息概念。蓝色线会交叉，读线时以箭头落点（能力端）为准，不要按起点所在行猜。

## 关键含义（历史解释；局部修正见上）

- 4 项能力各自“修改”一个同名信息概念（红箭头水平向右），这是能力的产出/维护责任。
- 除同名概念外，能力还“使用”其他信息概念：投资管理使用投资、金融工具、金融交易三项，是使用最多的能力。
- 信息概念也被多项能力共享：投资信息被投资管理、支付管理、金融交易管理三项能力使用；付款信息被支付管理（同名）和金融交易管理使用。
- 金融工具管理只使用金融工具（加同名水平线），映射最单纯；金融交易管理使用金融交易、投资、付款三项。
- 红蓝两种箭头表达两种不同责任：修改=写/维护，使用=读/引用；同一对能力—概念可以只有其中一种。
- 图中刻意不出现数据仓储、业务系统等实现元素，说明这是业务架构层面的信息概念映射，不是数据模型。
- 正文指出这只是构建“投资”概念的映射子集，完整映射还应包含协议、合作伙伴等能力与信息概念。

## 层级（历史解释；局部修正见上）

两列平级：左列 4 项业务能力、右列 4 个信息概念，各自没有上下级。两列标题只是列头（Capabilities / Information Concepts），不是父节点。能力与概念之间是交叉映射，不是分类层级。

## 线条含义（历史解释；局部修正见上）

红色实线箭头（4 条）= 能力修改信息，方向由能力指向信息概念；蓝色实线箭头（9 条）= 能力使用信息，方向由信息概念指向能力。两者都是直线、无虚线、无基数、无组合/泛化符号；蓝线在中间交叉但交叉点不表示任何关系。

## 易误读点（历史解释；局部修正见上）

- 蓝线箭头指向能力，不能按“能力→信息”读成能力向信息提供数据；语义是“信息被能力使用”。
- 红线与蓝线不是“强/弱”或“正/负”的极性，而是两种不同关系（修改 vs 使用）。
- 同名能力与概念之间的水平线不是“等同”，而是“该能力修改该信息概念”。
- 蓝线交叉处没有节点，交叉不代表两条关系相交或互相影响。
- 中文重绘 SVG 无箭头、且把多条线接到错误的概念上（如投资管理—付款），不能据它推断能力—信息对应关系。

## 元素

```json
[
  {
    "id": "grp_capabilities",
    "label_en": "Capabilities",
    "label_zh": "业务能力",
    "type": "group",
    "level": 1,
    "position": "左上列标题"
  },
  {
    "id": "grp_information",
    "label_en": "Information Concepts",
    "label_zh": "信息概念",
    "type": "group",
    "level": 1,
    "position": "右列标题"
  },
  {
    "id": "cap_investment",
    "label_en": "Investment Management",
    "label_zh": "投资管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 1
  },
  {
    "id": "cap_financial_instrument",
    "label_en": "Financial Instrument Management",
    "label_zh": "金融工具管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 2
  },
  {
    "id": "cap_payment",
    "label_en": "Payment Management",
    "label_zh": "支付管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 3
  },
  {
    "id": "cap_financial_transaction",
    "label_en": "Financial Transaction Management",
    "label_zh": "金融交易管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 4
  },
  {
    "id": "info_investment",
    "label_en": "Investment",
    "label_zh": "投资",
    "type": "data",
    "parent": "grp_information",
    "level": 2,
    "order": 1
  },
  {
    "id": "info_financial_instrument",
    "label_en": "Financial Instrument",
    "label_zh": "金融工具",
    "type": "data",
    "parent": "grp_information",
    "level": 2,
    "order": 2
  },
  {
    "id": "info_payment",
    "label_en": "Payment",
    "label_zh": "付款",
    "type": "data",
    "parent": "grp_information",
    "level": 2,
    "order": 3
  },
  {
    "id": "info_financial_transaction",
    "label_en": "Financial Transaction",
    "label_zh": "金融交易",
    "type": "data",
    "parent": "grp_information",
    "level": 2,
    "order": 4
  }
]
```

## 关系

```json
[
  {
    "from": "cap_investment",
    "to": "info_investment",
    "type": "access",
    "label_en": "Modifies",
    "label_zh": "修改",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "红色水平箭头，能力修改同名信息概念。"
  },
  {
    "from": "cap_financial_instrument",
    "to": "info_financial_instrument",
    "type": "access",
    "label_en": "Modifies",
    "label_zh": "修改",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "cap_payment",
    "to": "info_payment",
    "type": "access",
    "label_en": "Modifies",
    "label_zh": "修改",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "cap_financial_transaction",
    "to": "info_financial_transaction",
    "type": "access",
    "label_en": "Modifies",
    "label_zh": "修改",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "info_investment",
    "to": "cap_investment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "水平蓝线，信息被同名能力使用。"
  },
  {
    "from": "info_financial_instrument",
    "to": "cap_financial_instrument",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "info_payment",
    "to": "cap_payment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "info_financial_transaction",
    "to": "cap_financial_transaction",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "info_financial_instrument",
    "to": "cap_investment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "斜线：投资管理使用金融工具信息。"
  },
  {
    "from": "info_investment",
    "to": "cap_payment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "斜线：支付管理使用投资信息。"
  },
  {
    "from": "info_investment",
    "to": "cap_financial_transaction",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "斜线：金融交易管理使用投资信息。"
  },
  {
    "from": "info_payment",
    "to": "cap_financial_transaction",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "斜线：金融交易管理使用付款信息。"
  },
  {
    "from": "info_financial_transaction",
    "to": "cap_investment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "斜线：投资管理使用金融交易信息。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_crossmap",
    "title_zh": "能力 × 信息概念交叉映射（按原图逐条线转录）",
    "columns": [
      "能力",
      "信息概念",
      "关系",
      "线型"
    ],
    "rows": [
      [
        "投资管理 Investment Management",
        "投资 Investment",
        "修改 Modifies",
        "红色实线箭头，能力→概念"
      ],
      [
        "金融工具管理 Financial Instrument Management",
        "金融工具 Financial Instrument",
        "修改 Modifies",
        "红色实线箭头，能力→概念"
      ],
      [
        "支付管理 Payment Management",
        "付款 Payment",
        "修改 Modifies",
        "红色实线箭头，能力→概念"
      ],
      [
        "金融交易管理 Financial Transaction Management",
        "金融交易 Financial Transaction",
        "修改 Modifies",
        "红色实线箭头，能力→概念"
      ],
      [
        "投资管理 Investment Management",
        "投资 Investment",
        "使用 Uses",
        "蓝色实线箭头，概念→能力"
      ],
      [
        "金融工具管理 Financial Instrument Management",
        "金融工具 Financial Instrument",
        "使用 Uses",
        "蓝色实线箭头，概念→能力"
      ],
      [
        "支付管理 Payment Management",
        "付款 Payment",
        "使用 Uses",
        "蓝色实线箭头，概念→能力"
      ],
      [
        "金融交易管理 Financial Transaction Management",
        "金融交易 Financial Transaction",
        "使用 Uses",
        "蓝色实线箭头，概念→能力"
      ],
      [
        "投资管理 Investment Management",
        "金融工具 Financial Instrument",
        "使用 Uses",
        "蓝色斜线"
      ],
      [
        "支付管理 Payment Management",
        "投资 Investment",
        "使用 Uses",
        "蓝色斜线"
      ],
      [
        "金融交易管理 Financial Transaction Management",
        "投资 Investment",
        "使用 Uses",
        "蓝色斜线"
      ],
      [
        "金融交易管理 Financial Transaction Management",
        "付款 Payment",
        "使用 Uses",
        "蓝色斜线"
      ],
      [
        "投资管理 Investment Management",
        "金融交易 Financial Transaction",
        "使用 Uses",
        "蓝色斜线"
      ]
    ],
    "notes_zh": "每行对应原图中一条画出的线；蓝线共 9 条（4 条水平、5 条斜线），红线 4 条。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色实线箭头 + Uses",
    "meaning_zh": "信息概念被业务能力使用（箭头指向能力）",
    "explicit": true
  },
  {
    "symbol": "红色实线箭头 + Modifies",
    "meaning_zh": "业务能力修改信息概念（箭头指向信息概念）",
    "explicit": true
  },
  {
    "symbol": "左列圆角框",
    "meaning_zh": "业务能力",
    "explicit": false
  },
  {
    "symbol": "右列圆角框",
    "meaning_zh": "信息概念",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "左右两列：左列自上而下为投资管理、金融工具管理、支付管理、金融交易管理；右列对应为投资、金融工具、付款、金融交易。4 条红色水平箭头逐行连接同名项，9 条蓝色斜线在中间交叉形成网状。"
}
```

## 相关图

```json
[
  {
    "target": "G190/fig2-1",
    "relation": "complements",
    "note_zh": "同为信息地图示例；图 2-1 只画概念间关系，本图把概念挂到业务能力上"
  },
  {
    "target": "G190/figA-2",
    "relation": "basis_for",
    "note_zh": "图 A-2 用 ArchiMate 记法重画同一组“投资类能力—信息概念”的 Uses/Modifies 映射"
  },
  {
    "target": "G190/fig5-1",
    "relation": "related",
    "note_zh": "第 5 章以本图为例说明信息地图不等于数据模型"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "蓝线共 9 条（按能力端和概念端的箭头/出线计数），但原图只有 8 个可见的 Uses 文字标签，靠近投资管理右上角的两条线似乎共用标签，无法确定哪一条没有独立标签。",
    "斜线在中间大量交叉，个别线（如投资→支付管理与金融工具→投资管理）的标签归属靠端点与斜率推断，未见文字重复标注。"
  ],
  "analyzed_from": [
    "英文 PDF 第 14 页图 4-1 原图截图及 2x2 放大分块",
    "对原图蓝色/红色像素按列扫描并做 Hough 直线拟合，确认 9 条蓝线与 4 条红线的端点",
    "英文 PDF 第 14、15 页正文",
    "中文稿 G190e_信息映射.md 第 131–139 行",
    "figs/g190_fig4-1.svg 源码"
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
