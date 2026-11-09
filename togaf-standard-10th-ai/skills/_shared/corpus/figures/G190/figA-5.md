# G190/figA-5 · 实体关系图中的信息地图

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/figA-5.md) · [JSON](../../architecture/diagrams/G190/figA-5.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 26 页

![英文原图](../assets/G190/figA-5-p0026.png)

PDF 坐标：`[86.9, 36.0, 525.1, 303.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
aa
+
Amount
Payment_Number
+
Customer_ID
+
+
Payment_Date
Loan_Number
Customer_Name
+
Payment_Amount
Customer_Street
Customer_City
V
+
Branch_Name
PO
+
Account_ID
+
Branch_Code
+
Balance
+
Branch_City
Employee_ID
Employee_Name
Depedendent_Name
Start_Date
Telephone_Numer
```

## 概要（历史解释；局部修正见上）

把与图 A-3 相同的 6 个实体和 7 条关联画成鸦爪 ERD，用符号标出各端基数。

## 目的（历史解释；局部修正见上）

附录 A.3 说明 ERD 在信息系统设计中的三个层次，并强调业务架构最常用概念层（有时逻辑层）。本图是概念层 ERD 的样例：实体仍是业务实体，但改用数据库设计者熟悉的鸦爪基数符号，为后续逻辑/物理设计留出接口。

## 阅读顺序（历史解释；局部修正见上）

逐个实体读属性，再沿关系线看两端的符号：圈 = 可选（0..1），竖杠 = 恰好一个，鸦爪 = 多个，圈+鸦爪 = 0..多，杠+鸦爪 = 1..多。符号画在哪一端，就描述哪一端相对另一端一个实例的基数。图中没有关系名，只能按符号读基数。

## 关键含义（历史解释；局部修正见上）

- 6 个实体与图 A-3 的 6 个类一一对应，属性清单基本相同，说明这是同一业务模型的 ERD 表达。
- 关系仍是 7 条，拓扑与图 A-3 完全一致：付款—贷款—客户、贷款—分支机构—账户、分支机构—员工—客户。
- 基数用鸦爪符号而非数字：图中出现圈（可选）、竖杠（一个）、圈+鸦爪（0..多）、杠+鸦爪（1..多）四种组合。
- 多数关系是一端为竖杠、另一端为圈，按标准 IE 读法是“一端恰好一个、另一端 0 或 1”；只有分支机构—账户是 0..多，员工—客户两端都是 1..多。
- Employee 的最后一个属性拼写为 Telephone_Numer（少一个 b），与图 A-3 的 Telephone_Number 不一致，属原图笔误。
- 实体框的青色标题条与图 A-3 的黄色标题条不同，是 ERD 工具的样式；属性前缀 + 仍表示 public。

## 层级（历史解释；局部修正见上）

没有层级：6 个实体平级，关系线只表示关联；属性列在实体框内，是实体的组成部分而非独立元素。

## 线条含义（历史解释；局部修正见上）

7 条无箭头的实线关系，两端用鸦爪记法标基数；没有关系名、没有角色名、没有方向箭头。线条走向（水平、折线、绕行）只为避让实体框，不表达额外语义。

## 易误读点（历史解释；局部修正见上）

- 鸦爪符号贴在实体边上时，读的是该实体的基数；不要按“靠近谁就属于谁”理解。
- 图中没有关系名，不能凭线的形状猜“持有/包含/订购”等业务动词——这些是中文重绘 SVG 自拟的。
- 本图是概念层 ERD，不是物理数据库模式：属性没有主外键标记，实体也未必已实现。
- 客户端的圈不是“零个客户”，而是“0 或 1 个”的可选基数；与图 A-4 的 1..2 不是同一套写法。
- Employee 的 Telephone_Numer 是原图拼写错误，不是另一个字段。

## 元素

```json
[
  {
    "id": "ent_payment",
    "label_en": "Payment",
    "label_zh": "付款",
    "type": "data",
    "notation_type": "ER Entity",
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
    "id": "ent_loan",
    "label_en": "Loan",
    "label_zh": "贷款",
    "type": "data",
    "notation_type": "ER Entity",
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
    "id": "ent_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "data",
    "notation_type": "ER Entity",
    "level": 1,
    "position": "右上",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Customer_ID",
        "Customer_Name",
        "Customer_Street",
        "Customer_City"
      ]
    }
  },
  {
    "id": "ent_branch",
    "label_en": "Branch",
    "label_zh": "分支机构",
    "type": "data",
    "notation_type": "ER Entity",
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
    "id": "ent_account",
    "label_en": "Account",
    "label_zh": "账户",
    "type": "data",
    "notation_type": "ER Entity",
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
    "id": "ent_employee",
    "label_en": "Employee",
    "label_zh": "员工",
    "type": "data",
    "notation_type": "ER Entity",
    "level": 1,
    "position": "下中",
    "attributes": {
      "visibility": "+",
      "attributes": [
        "Employee_ID",
        "Employee_Name",
        "Dependent_Name",
        "Start_Date",
        "Telephone_Numer"
      ]
    }
  }
]
```

## 关系

```json
[
  {
    "from": "ent_payment",
    "to": "ent_loan",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Payment 端 ○（0..1）；Loan 端 |（1）",
    "description_zh": "上排水平线；按标准 IE 读法为一笔贷款对应 0 或 1 笔付款、一笔付款对应恰好一笔贷款。"
  },
  {
    "from": "ent_loan",
    "to": "ent_customer",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Loan 端 |（1）；Customer 端 ○（0..1）",
    "description_zh": "上排水平线；符号表示 Loan 端恰好一个、Customer 端 0 或 1 个。"
  },
  {
    "from": "ent_loan",
    "to": "ent_branch",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Loan 端 ○（0..1）；Branch 端 |（1）",
    "description_zh": "从 Loan 左边缘折向左下接到 Branch 的折线。"
  },
  {
    "from": "ent_branch",
    "to": "ent_account",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Branch 端 ○<（0..*）；Account 端 |（1）",
    "description_zh": "中部水平线；唯一使用“零个或多个”鸦爪的一条。"
  },
  {
    "from": "ent_account",
    "to": "ent_customer",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Account 端 |（1）；Customer 端 ○（0..1）",
    "description_zh": "从 Account 右边缘向右再向上接到 Customer 底边的折线。"
  },
  {
    "from": "ent_branch",
    "to": "ent_employee",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Branch 端 |（1）；Employee 端 ○（0..1）",
    "description_zh": "从 Branch 底边向下再向右接到 Employee 左边的折线。"
  },
  {
    "from": "ent_employee",
    "to": "ent_customer",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "Employee 端 |<（1..*）；Customer 端 |<（1..*）",
    "description_zh": "右下方的长折线，两端均为“一个或多个”鸦爪。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "青色标题条 + 属性清单",
    "meaning_zh": "ERD 实体及其属性",
    "explicit": false
  },
  {
    "symbol": "圈 ○",
    "meaning_zh": "可选（0 或 1）",
    "explicit": false
  },
  {
    "symbol": "竖杠 |",
    "meaning_zh": "恰好一个",
    "explicit": false
  },
  {
    "symbol": "圈 + 鸦爪 ○<",
    "meaning_zh": "零个或多个",
    "explicit": false
  },
  {
    "symbol": "竖杠 + 鸦爪 |<",
    "meaning_zh": "一个或多个",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "6 个实体框分三行：Payment（左上）、Loan（上中）、Customer（右上）；Branch（中左）、Account（中中）；Employee（下中）。关系线用水平线与折线绕行，Customer 与 Employee 通过右下方的长折线相连。"
}
```

## 相关图

```json
[
  {
    "target": "G190/figA-3",
    "relation": "variant_of",
    "note_zh": "同一组 6 个实体与 7 组关联，图 A-3 是 UML 类图版本，本图是带鸦爪基数的 ERD 版本"
  },
  {
    "target": "G190/fig2-1",
    "relation": "related",
    "note_zh": "同样使用付款、贷款、客户、账户、分支机构、员工 6 个概念，但本图补上属性与基数"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "基数按标准 IE/鸦爪读法逐端记录（圈=0..1、杠=1、圈+鸦爪=0..*、杠+鸦爪=1..*），但其中 4 条关系按此读法得到的业务含义不自然（如“一个客户恰好一笔贷款”“一个分支机构恰好一个账户”），作者原意可能是把圈当作“多”来用；原图没有基数文字，无法确证。",
    "Employee 的 Telephone_Numer 确认是原图拼写（少一个 b），不是转录错误。",
    "各实体框的青色标题条是样式，不代表主键或分区。"
  ],
  "analyzed_from": [
    "英文 PDF 第 26 页图 A-5 原图截图及 3x 局部放大（逐个关系端点核对鸦爪/圈/杠符号）",
    "英文 PDF 第 25–26 页正文",
    "中文稿 G190e_信息映射.md 第 267–275 行",
    "figs/g190_figA-5.svg 源码"
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
