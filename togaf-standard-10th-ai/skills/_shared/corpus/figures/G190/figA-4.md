# G190/figA-4 · 信息类型之间的关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/figA-4.md) · [JSON](../../architecture/diagrams/G190/figA-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 25 页

![英文原图](../assets/G190/figA-4-p0025.png)

PDF 坐标：`[86.9, 36.0, 525.1, 271.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
1..2
41%
Customer
Account
First Name: text
Balance owing: currency
Last Name: text
Age: numeric
Address: text
```

## 概要（历史解释；局部修正见上）

用客户与账户两个类及两端基数 1..2 / 1..*，示范 UML 多重度如何约束信息类型之间的关联数量。

## 目的（历史解释；局部修正见上）

附录 A.2 在讲完类与属性后，用本图补上 UML 的另一项能力：基数可以约束“一个类的对象能与另一类的多少个对象关联”。正文正是借这张图解释 1..* 与 1..2 的含义。

## 阅读顺序（历史解释；局部修正见上）

先读两个圆：左边 Customer、右边 Account，属性写在各自圆的下方并带类型。再看中间那条水平关联线：靠近某一端的数字描述“该端类相对另一端一个对象可以有多少个实例”。因此账户端的 1..* 表示一个客户至少有 1 个账户、数量无上限；客户端的 1..2 表示一个账户至少关联 1 个、最多 2 个客户。

## 关键含义（历史解释；局部修正见上）

- 两个信息类型：Customer 有 4 个带类型的属性（First Name/Last Name/Age/Address），Account 只有 1 个（Balance owing: currency）。
- 属性带类型（text、numeric、currency），比图 A-3 只给属性名更接近逻辑层设计。
- 账户端基数 1..*：一个客户必须至少拥有一个账户，账户数量没有上限。
- 客户端基数 1..2：一个账户必须关联至少一个、最多两个客户。
- 基数标在它所描述的那一端：读某个数字时要看它靠近哪个类，再反推另一端的对象。
- 图中没有箭头、没有关联名、没有角色名，关联是未指定导航性的双向关联。

## 层级（历史解释；局部修正见上）

没有层级：两个类平级，只有一条关联。属性以文字清单挂在各自圆的下方，属于类的组成部分，不是独立元素。

## 线条含义（历史解释；局部修正见上）

一条水平实线 = UML 无向关联；两端分别标多重度 1..2（客户端）与 1..*（账户端）；无箭头、无关联名、无角色名。圆形与圆内横线只是类符号的画法，不表示包含关系。

## 易误读点（历史解释；局部修正见上）

- 不要把 1..2 读成“一个客户最多两个账户”：它标在客户一端，描述的是每个账户对应的客户数。
- 1..* 标在账户一端，描述的是每个客户对应的账户数（至少 1、无上限），不是“账户有很多客户”。
- 圆形不是 ER 图的实体椭圆，也不是维恩图；属性写在圆外下方。
- 中文重绘 SVG 把两个基数对调了（客户 1..*、账户 1..2），与正文解释相反，不能据它理解本图。
- 图里没有方法、没有主键标记，不能当作完整的类设计或数据库模式。

## 元素

```json
[
  {
    "id": "cls_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "data",
    "notation_type": "UML Class（圆形符号）",
    "level": 1,
    "position": "左侧圆",
    "attributes": {
      "attributes": [
        "First Name: text",
        "Last Name: text",
        "Age: numeric",
        "Address: text"
      ]
    }
  },
  {
    "id": "cls_account",
    "label_en": "Account",
    "label_zh": "账户",
    "type": "data",
    "notation_type": "UML Class（圆形符号）",
    "level": 1,
    "position": "右侧圆",
    "attributes": {
      "attributes": [
        "Balance owing: currency"
      ]
    }
  }
]
```

## 关系

```json
[
  {
    "from": "cls_customer",
    "to": "cls_account",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "cardinality": "客户端 1..2；账户端 1..*",
    "description_zh": "水平无向关联；靠近 Account 写 1..*（每个客户 1 个以上账户），靠近 Customer 写 1..2（每个账户 1–2 个客户）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "圆形（内含一条横线）",
    "meaning_zh": "类/信息类型的简化符号",
    "explicit": false
  },
  {
    "symbol": "圆下方的缩进文字",
    "meaning_zh": "该类实例的属性及其类型",
    "explicit": false
  },
  {
    "symbol": "无箭头实线 + 两端数字",
    "meaning_zh": "UML 关联及两端多重度",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "左右并置两个大圆（Customer 左、Account 右），圆下方各有缩进排列的属性清单；两圆之间一条水平关联线，线上方靠近两端分别写 1..2 与 1..*。"
}
```

## 相关图

```json
[
  {
    "target": "G190/figA-3",
    "relation": "detail_of",
    "note_zh": "本图是图 A-3 中 Customer—Account 关联的局部放大，补上属性类型与两端多重度"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "圆形类符号不是当前 UML 规范的标准类框（标准为矩形三栏），此处按原图记法描述为“简化的类符号”，不主张其符合 UML 图形规范。",
    "1..2 的业务合理性（一个账户最多两个客户）由原图与正文共同给出，未见进一步解释。"
  ],
  "analyzed_from": [
    "英文 PDF 第 25 页图 A-4 原图截图",
    "英文 PDF 第 24 页基数说明段落与第 25 页属性段落",
    "中文稿 G190e_信息映射.md 第 259–263 行",
    "figs/g190_figA-4.svg 源码"
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
