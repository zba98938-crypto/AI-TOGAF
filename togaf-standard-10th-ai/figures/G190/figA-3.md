# G190/figA-3 · UML 中的信息地图

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/figA-3.md) · [JSON](../../architecture/diagrams/G190/figA-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 24 页

![英文原图](../assets/G190/figA-3-p0024.png)

PDF 坐标：`[86.9, 143.3, 525.1, 397.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
+ CD Payment_Number
+ Customer_ID
+ CD Payment_Date
+ CD Customer_Name
+ CD Payment_Amount
+ CD Customer_city
+ CD Customer_Street
+ CD Branch_Name
+ CD Branch_Code
+ CD Branch_City
+ CD Employee_ID
+ CD Employee_Name
+ CD Dependent_Name
+ CD Telephone_Number
+ CD Start_Date
```

## 概要（历史解释；局部修正见上）

用 6 个 UML 类及其属性清单表达信息地图，示范比 ArchiMate 更细一层的业务信息结构。

## 目的（历史解释；局部修正见上）

附录 A.2 要说明 UML 类图特别适合信息映射：它比 ArchiMate 多出属性（以及后文的基数），可以把每个业务实体所承载的逻辑信息单元列清楚。本图先给类与属性的全貌，基数留给图 A-4 单独示范。

## 阅读顺序（历史解释；局部修正见上）

逐个类读：黄色标题条是类名，下面每行是一个属性，前缀 + 表示 public。类之间的实线只表示“业务上相关”，没有箭头、没有基数、没有关联名。先读类名确认有哪些信息类型，再按线看它们如何相连（付款—贷款—客户、贷款—分支机构—账户、分支机构—员工—客户）。

## 关键含义（历史解释；局部修正见上）

- 6 个类与图 2-1 的 6 个信息概念一一对应（付款、贷款、客户、分支机构、账户、员工），但这里补上了属性，信息量更大。
- 属性列在类框内，全部为 public（+），且只给名称不给类型；正文说属性是与各业务实体相关的逻辑信息单元，必须在某处完整定义。
- 7 条关联线没有任何标签、箭头或基数，只表达“这两个信息类型相关”；多重度要到图 A-4 才出现。
- 关联的拓扑与图 2-1 相同：付款—贷款—客户、贷款—分支机构—账户、分支机构—员工—客户，形成一个闭合的关系网。
- 类框画成右侧/底部带阴影的“堆叠纸张”样式，是原图的制图风格，不代表多个类或多重实例。
- 正文指出 UML 比 ArchiMate 更详细（有属性、基数和可选的关联名），但本图仍属于概念层，不含方法或数据库实现。

## 层级（历史解释；局部修正见上）

没有层级：6 个类平级，关联线只表示相关，不是分类或包含。属性在类框内形成“类—属性”的两级文字结构，但属性不是独立元素。

## 线条含义（历史解释；局部修正见上）

7 条黑色实线均为无向关联（UML association），没有箭头（不表示导航性）、没有关联名、没有多重度；线只是把两个类连起来，方向不可读。

## 易误读点（历史解释；局部修正见上）

- 关联线没有箭头，不能读成“付款产生贷款”之类的流向；UML 关联默认是双向/未指定的。
- 图中没有多重度，不要因为付款只连贷款就推断“一对一”。
- 属性前的 + 是 UML 可见性 public，不是“新增”或“主键”。
- 黄色标题条是类名，不是包或分组；类框的阴影只是画法。
- 中文重绘 SVG 是客户/账户/交易三个类的另一种模型，且自加了基数与关系名，不能代替本图。

## 元素

```json
[
  {
    "id": "cls_payment",
    "label_en": "Payment",
    "label_zh": "付款",
    "type": "data",
    "notation_type": "UML Class",
    "level": 1,
    "position": "左上",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Payment_Number",
        "Payment_Date",
        "Payment_Amount"
      ]
    }
  },
  {
    "id": "cls_loan",
    "label_en": "Loan",
    "label_zh": "贷款",
    "type": "data",
    "notation_type": "UML Class",
    "level": 1,
    "position": "上中",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Amount",
        "Loan_Number"
      ]
    }
  },
  {
    "id": "cls_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "data",
    "notation_type": "UML Class",
    "level": 1,
    "position": "右上",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Customer_ID",
        "Customer_Name",
        "Customer_City",
        "Customer_Street"
      ]
    }
  },
  {
    "id": "cls_branch",
    "label_en": "Branch",
    "label_zh": "分支机构",
    "type": "data",
    "notation_type": "UML Class",
    "level": 1,
    "position": "中左",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Branch_Name",
        "Branch_Code",
        "Branch_City"
      ]
    }
  },
  {
    "id": "cls_account",
    "label_en": "Account",
    "label_zh": "账户",
    "type": "data",
    "notation_type": "UML Class",
    "level": 1,
    "position": "中中",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Account_ID",
        "Balance"
      ]
    }
  },
  {
    "id": "cls_employee",
    "label_en": "Employee",
    "label_zh": "员工",
    "type": "data",
    "notation_type": "UML Class",
    "level": 1,
    "position": "下中偏右",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Employee_ID",
        "Employee_Name",
        "Dependent_Name",
        "Telephone_Number",
        "Start_Date"
      ]
    }
  }
]
```

## 关系

```json
[
  {
    "from": "cls_payment",
    "to": "cls_loan",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "上排水平实线，无标签。"
  },
  {
    "from": "cls_loan",
    "to": "cls_customer",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "上排水平实线，无标签。"
  },
  {
    "from": "cls_loan",
    "to": "cls_branch",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "从 Loan 左边缘折向左下，再接到 Branch 右上角。"
  },
  {
    "from": "cls_branch",
    "to": "cls_account",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "中部水平实线，无标签。"
  },
  {
    "from": "cls_account",
    "to": "cls_customer",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "从 Account 右边缘向右再向上，接到 Customer 底边。"
  },
  {
    "from": "cls_branch",
    "to": "cls_employee",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "从 Branch 底边向下再向右，接到 Employee 左边缘。"
  },
  {
    "from": "cls_employee",
    "to": "cls_customer",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "从 Employee 右边缘向右再向上，接到 Customer 底边右侧。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色标题条 + 白色属性区",
    "meaning_zh": "UML 类（类名 + 属性清单）",
    "explicit": false
  },
  {
    "symbol": "属性前的 +",
    "meaning_zh": "public 可见性",
    "explicit": false
  },
  {
    "symbol": "无箭头实线",
    "meaning_zh": "UML 关联（未标基数、未标导航性）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "6 个类框分三行错落：Payment（左上）、Loan（上中）、Customer（右上）；Branch（中左）、Account（中中）；Employee（下中偏右）。7 条折线在框间连接，Customer 与 Employee 分别有两条折线绕到右下方。"
}
```

## 相关图

```json
[
  {
    "target": "G190/figA-5",
    "relation": "variant_of",
    "note_zh": "同样的 6 个实体与 7 组关联，图 A-5 改用带鸦爪基数的 ERD 表达"
  },
  {
    "target": "G190/fig2-1",
    "relation": "related",
    "note_zh": "同一组 6 个概念与 7 组关系；本图是补上属性的 UML 版本"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "属性名前的浅蓝色小图标在原图中过小，无法确认是建模工具的“public 属性”图标还是“数据类型”图标；属性本身没有给类型，故只记录名称。",
    "7 条关联线均无标签、无基数、无导航箭头，关联的语义只能按“业务相关”理解，无法确定两端角色名。"
  ],
  "analyzed_from": [
    "英文 PDF 第 24 页图 A-3 原图截图及 2x 放大分块（逐类转录属性）",
    "英文 PDF 第 24 页整页与正文",
    "英文 PDF 第 25 页属性段落",
    "中文稿 G190e_信息映射.md 第 255–263 行",
    "figs/g190_figA-3.svg 源码"
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
