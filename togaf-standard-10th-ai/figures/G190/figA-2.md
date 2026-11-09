# G190/figA-2 · 使用 ArchiMate 语言的“信息—业务能力”交叉映射

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/figA-2.md) · [JSON](../../architecture/diagrams/G190/figA-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G190/figA-2-p0023.png)

PDF 坐标：`[86.9, 229.8, 525.1, 548.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business capabilities
E)
Information
Investment il
Payment
Investment
Financial
management
|
Management
‘
instrument
)
Uses
él
Payment
Financial
Financial
Financial
transaction
instrument
transaction
management
)
|
management
|
Investment
Modifies
Biises
Investment
management
Financial instrument
Uses
a
Uses
Financial transaction
```

## 概要（历史解释；局部修正见上）

用 ArchiMate 分组表达信息与业务能力两类元素的整体“使用/修改”关系，并把投资管理一项放大成局部详图。

## 目的（历史解释；局部修正见上）

附录 A.1 在讲完业务对象之间的结构关系后，用本图说明 ArchiMate 还能表达信息概念与业务能力等其他业务架构概念之间的关系。上方分组图给出总体关系，下方详图证明这些关系可以落到底层业务对象上。

## 阅读顺序（历史解释；局部修正见上）

先读上方两个分组框：Information 组左侧引出的虚线箭头（Uses）指向 Business capabilities 组，表示信息被能力使用；反向的实线（Modifies）连接两组，表示能力修改信息。再读下方面板：这是投资管理一行的放大，实线 Modifies 从投资管理连到 Investment，三条虚线 Uses 分别从 Investment、Financial instrument、Financial transaction 指回投资管理。

## 关键含义（历史解释；局部修正见上）

- 上图把两类元素各装进一个 ArchiMate 分组（Business capabilities / Information），关系只画在分组边界上，是高度概括的视图。
- Uses 用虚线、Modifies 用实线，线型本身编码关系种类；Uses 的箭头指向能力（信息被能力使用），Modifies 没有箭头但按标签读作能力→信息。
- 下方面板把投资管理展开：它修改 Investment，同时使用 Investment、Financial instrument、Financial transaction 三个业务对象。
- 同一个业务对象可以既被修改又被使用：Investment 在详图中同时出现在 Modifies 与 Uses 两端。
- 投资管理是唯一被展开的能力，说明这一面板是示例性的下钻，而不是完整映射。
- 分组框、能力框、业务对象框都带 ArchiMate 图标，表明这是 ArchiMate 视图而非普通框图。

## 层级（历史解释；局部修正见上）

两层容器关系：Business capabilities 分组包含 4 项能力，Information 分组包含 4 个业务对象；能力与业务对象之间是使用/修改的交叉关系，不构成层级。下方面板是同一模型的一个局部视图，不是新的层级。

## 线条含义（历史解释；局部修正见上）

虚线 + 箭头 = Uses（信息概念→业务能力）；实线、无箭头 = Modifies（业务能力→信息概念）。上方两条线连接分组边界；下方四条线连接具体元素，其中 Modifies 用折线从投资管理顶部绕到 Investment，三条 Uses 用虚线折线指回投资管理的右上、右侧与底部。

## 易误读点（历史解释；局部修正见上）

- 上方的分组级连线只是概括：不能据此认为 Information 组内每个业务对象都参与 Use，具体参与情况要看下方面板。
- Uses 是虚线箭头且指向能力；Modifies 是实线且没有箭头，不能凭“有没有箭头”判断谁是主语。
- 下方面板不是第二套模型，而是投资管理一行的放大；两处出现同名元素是重复展示，不是重复定义。
- 分组框（Business capabilities / Information）是 ArchiMate 的容器，不是能力或信息概念本身。
- 中文重绘 SVG 只有 2×2 个元素、没有分组和虚线，不能据它理解本图的两层结构。

## 元素

```json
[
  {
    "id": "grp_capabilities",
    "label_en": "Business capabilities",
    "label_zh": "业务能力",
    "type": "group",
    "level": 1,
    "position": "上方面板左侧"
  },
  {
    "id": "grp_information",
    "label_en": "Information",
    "label_zh": "信息",
    "type": "group",
    "level": 1,
    "position": "上方面板右侧"
  },
  {
    "id": "cap_investment",
    "label_en": "Investment management",
    "label_zh": "投资管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 1,
    "position": "上组左上；下方面板左侧重复出现"
  },
  {
    "id": "cap_payment",
    "label_en": "Payment Management",
    "label_zh": "支付管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 2,
    "position": "上组右上"
  },
  {
    "id": "cap_financial_instrument",
    "label_en": "Financial instrument management",
    "label_zh": "金融工具管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 3,
    "position": "上组左下"
  },
  {
    "id": "cap_financial_transaction",
    "label_en": "Financial transaction management",
    "label_zh": "金融交易管理",
    "type": "capability",
    "parent": "grp_capabilities",
    "level": 2,
    "order": 4,
    "position": "上组右下"
  },
  {
    "id": "info_investment",
    "label_en": "Investment",
    "label_zh": "投资",
    "type": "data",
    "notation_type": "ArchiMate Business Object",
    "parent": "grp_information",
    "level": 2,
    "order": 1,
    "position": "上组左上；下方详图右上"
  },
  {
    "id": "info_financial_instrument",
    "label_en": "Financial instrument",
    "label_zh": "金融工具",
    "type": "data",
    "notation_type": "ArchiMate Business Object",
    "parent": "grp_information",
    "level": 2,
    "order": 2,
    "position": "上组右上；下方详图右中"
  },
  {
    "id": "info_payment",
    "label_en": "Payment",
    "label_zh": "付款",
    "type": "data",
    "notation_type": "ArchiMate Business Object",
    "parent": "grp_information",
    "level": 2,
    "order": 3,
    "position": "上组左下"
  },
  {
    "id": "info_financial_transaction",
    "label_en": "Financial transaction",
    "label_zh": "金融交易",
    "type": "data",
    "notation_type": "ArchiMate Business Object",
    "parent": "grp_information",
    "level": 2,
    "order": 4,
    "position": "上组右下；下方详图右下"
  }
]
```

## 关系

```json
[
  {
    "from": "grp_information",
    "to": "grp_capabilities",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "上方面板：从 Information 分组左边缘引出的虚线箭头指向 Business capabilities 分组右边缘。"
  },
  {
    "from": "grp_capabilities",
    "to": "grp_information",
    "type": "access",
    "label_en": "Modifies",
    "label_zh": "修改",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "上方面板：两分组之间的实线，无箭头。"
  },
  {
    "from": "cap_investment",
    "to": "info_investment",
    "type": "access",
    "label_en": "Modifies",
    "label_zh": "修改",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "下方面板：从投资管理顶部折向上、再向右接到 Investment 左边缘的实线。"
  },
  {
    "from": "info_investment",
    "to": "cap_investment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "下方面板：从 Investment 左边缘折向左下、箭头落在投资管理右上角。"
  },
  {
    "from": "info_financial_instrument",
    "to": "cap_investment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "下方面板：从 Financial instrument 左边缘水平向左，箭头落在投资管理右侧。"
  },
  {
    "from": "info_financial_transaction",
    "to": "cap_investment",
    "type": "serving",
    "label_en": "Uses",
    "label_zh": "使用",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "下方面板：从 Financial transaction 左边缘折向左上，箭头落在投资管理底边。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "虚线 + 箭头 + Uses",
    "meaning_zh": "信息概念被业务能力使用（箭头指向能力）",
    "explicit": true
  },
  {
    "symbol": "实线 + Modifies",
    "meaning_zh": "业务能力修改信息概念（无箭头，按标签读作能力→信息）",
    "explicit": true
  },
  {
    "symbol": "浅棕色分组框（右上角小图标）",
    "meaning_zh": "ArchiMate 分组（group）",
    "explicit": false
  },
  {
    "symbol": "浅棕色圆角框（右上角小图标）",
    "meaning_zh": "ArchiMate 业务能力（capability）",
    "explicit": false
  },
  {
    "symbol": "黄色矩形（顶部标签带）",
    "meaning_zh": "ArchiMate 业务对象（business object）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "上下两个面板：上方横向并置“Business capabilities”分组（2×2 能力框）与“Information”分组（2×2 业务对象框），两分组之间画 Uses 虚线与 Modifies 实线；下方为带细边框的局部详图，投资管理在左，Investment/Financial instrument/Financial transaction 在右。"
}
```

## 相关图

```json
[
  {
    "target": "G190/fig4-1",
    "relation": "based_on",
    "note_zh": "同一组“投资类能力—信息概念”的 Uses/Modifies 映射，本图改用 ArchiMate 分组与业务对象记法，并增加投资管理的局部详图"
  },
  {
    "target": "G190/figA-1",
    "relation": "complements",
    "note_zh": "同一节的两个 ArchiMate 示例：图 A-1 展示业务对象间结构关系，本图展示信息概念与业务能力的关系"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "下方面板左侧、投资管理框后面还有一段被裁切的白色矩形与顶部细线残片（可能是原幻灯片的分组边框或标题），标签不可见，无法判定其身份，未列入 elements。",
    "分组级的两条线是原图的高度概括画法，ArchiMate 规范中并不存在“组到组”的 Uses/Modifies 关系类型；此处按图面文字记录为 serving/access，不主张其符合严格语义。",
    "原图能力框/业务对象框右上角的小图标分辨率有限，按位置判断为 ArchiMate 的能力与业务对象标记。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页图 A-2 原图截图（含上方面板与下方面板）",
    "英文 PDF 第 23 页整页与正文",
    "中文稿 G190e_信息映射.md 第 249–251 行",
    "figs/g190_figA-2.svg 源码"
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
