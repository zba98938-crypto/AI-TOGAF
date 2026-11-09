# G190/fig2-1 · 金融机构的简单信息地图

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/fig2-1.md) · [JSON](../../architecture/diagrams/G190/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 12 页

![英文原图](../assets/G190/fig2-1-p0012.png)

PDF 坐标：`[86.9, 314.1, 525.1, 463.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
is made
requests or
against
receives
Payment
Loan
Customer
holds
provides
supports
Account
manages
Branch
Employee
works for
```

## 概要（历史解释；局部修正见上）

用付款、贷款、客户、账户、分支机构、员工 6 个信息概念及其 7 条带动词的关系，示范金融机构的高层信息地图。

## 目的（历史解释；局部修正见上）

第 2 章把信息地图定义为“信息概念及其相互关系的集合”，本图给出一个最小可读的样例：先用“名词质疑”从业务语言中挑出关键名词，再把它们按业务说法连起来。正文同时声明这只是简单高层示例，更细致的建模见附录 A。

## 阅读顺序（历史解释；局部修正见上）

没有固定起点，可从任一概念出发沿箭头读：箭头尾部是句子的主语，箭头指向宾语，线上方/旁的动词短语是关系名。例如 Employee → Branch 旁的 works for 读作“员工为分支机构工作”。先读概念框（蓝色），再读箭头标签，不要给框补充属性和基数。

## 关键含义（历史解释；局部修正见上）

- 全图只有 6 个概念、7 条关系，全部是业务名词和业务动词，没有属性、主键、基数——这正是信息地图区别于数据模型的地方。
- 关系用业务语言表达（is made against、requests or receives、holds、provides、manages、supports、works for），没有采用 UML 的关联/组合/泛化等建模记法。
- 客户是关系的汇聚点：客户“申请或接收”贷款、“持有”账户；贷款与账户又分别被付款、分支机构连接。
- 付款只连到贷款（is made against），说明付款是针对某笔贷款发生的，而不是直接挂在客户或账户上。
- 分支机构同时“提供”贷款、“管理”账户；员工“支持”客户、“为”分支机构“工作”，把组织侧的概念也纳入同一张图。
- 图中有意省略了产品、渠道等概念，属于“简单、高层”示例；正文明确更详细的示例与技术放在附录 A。
- 方向不可反读：holds 是客户→账户（客户持有账户），works for 是员工→分支机构，反过来会改变业务含义。

## 层级（历史解释；局部修正见上）

没有上下级。6 个信息概念平级，图中没有分类、分解或包含关系；层级只体现在概念图整体属于“信息地图”这一制品。

## 线条含义（历史解释；局部修正见上）

7 条黑色实线箭头都带动词标签，方向表示业务语句的主语→宾语；没有虚线、没有菱形（组合/聚合）、没有空心三角（泛化）、也没有基数标注。关系是业务词汇层面的关联，不承诺任何实现或数据结构。

## 易误读点（历史解释；局部修正见上）

- 不要当成 ER 图或类图：图里没有属性、主键、外键和基数，付款与贷款之间不是数据库的“一对多”。
- “持有”是客户→账户，不是账户→客户；中文重绘 SVG 把这条线画成从贷款出发且不接触账户，不能据它理解。
- 6 个概念之间没有分类层级，贷款不是付款的一种，账户也不是客户的子类。
- 图中没有出现“产品”，不能据此认为该金融机构没有产品概念——正文说明这是刻意简化的示例。

## 元素

```json
[
  {
    "id": "ic_payment",
    "label_en": "Payment",
    "label_zh": "付款",
    "type": "data",
    "level": 1,
    "position": "左上",
    "description_zh": "信息概念；只与 Loan 相连。"
  },
  {
    "id": "ic_loan",
    "label_en": "Loan",
    "label_zh": "贷款",
    "type": "data",
    "level": 1,
    "position": "上中",
    "description_zh": "信息概念；连接付款、客户、分支机构。"
  },
  {
    "id": "ic_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "data",
    "level": 1,
    "position": "右上",
    "description_zh": "信息概念；连接贷款、账户、员工。"
  },
  {
    "id": "ic_account",
    "label_en": "Account",
    "label_zh": "账户",
    "type": "data",
    "level": 1,
    "position": "中部偏右",
    "description_zh": "信息概念；连接客户与分支机构。"
  },
  {
    "id": "ic_branch",
    "label_en": "Branch",
    "label_zh": "分支机构",
    "type": "data",
    "level": 1,
    "position": "左下",
    "description_zh": "信息概念；连接贷款、账户、员工。"
  },
  {
    "id": "ic_employee",
    "label_en": "Employee",
    "label_zh": "员工",
    "type": "data",
    "level": 1,
    "position": "右下",
    "description_zh": "信息概念；连接客户与分支机构。"
  }
]
```

## 关系

```json
[
  {
    "from": "ic_payment",
    "to": "ic_loan",
    "type": "association",
    "label_en": "is made against",
    "label_zh": "针对……付款",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "付款针对某笔贷款发生（水平箭头向右）。"
  },
  {
    "from": "ic_loan",
    "to": "ic_customer",
    "type": "association",
    "label_en": "requests or receives",
    "label_zh": "申请或接收",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "客户申请或接收贷款（水平箭头向右）。"
  },
  {
    "from": "ic_customer",
    "to": "ic_account",
    "type": "association",
    "label_en": "holds",
    "label_zh": "持有",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "客户持有账户；斜线由右上指向账户。"
  },
  {
    "from": "ic_branch",
    "to": "ic_loan",
    "type": "association",
    "label_en": "provides",
    "label_zh": "提供",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分支机构提供贷款；斜线由左下指向贷款。"
  },
  {
    "from": "ic_branch",
    "to": "ic_account",
    "type": "association",
    "label_en": "manages",
    "label_zh": "管理",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分支机构管理账户；斜线由左下指向账户。"
  },
  {
    "from": "ic_employee",
    "to": "ic_customer",
    "type": "association",
    "label_en": "supports",
    "label_zh": "支持",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "员工支持客户；竖线由员工向上指向客户。"
  },
  {
    "from": "ic_employee",
    "to": "ic_branch",
    "type": "association",
    "label_en": "works for",
    "label_zh": "为……工作",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "员工为分支机构工作；长横线由右向左指向分支机构。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色矩形",
    "meaning_zh": "一个信息概念（业务名词）",
    "explicit": false
  },
  {
    "symbol": "黑色实线箭头 + 动词短语",
    "meaning_zh": "两个概念之间的有向业务关系，箭头指向关系宾语",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "6 个蓝色矩形分两行错落排布：上行为付款（左）、贷款（中）、客户（右），中间偏右为账户，下行为分支机构（左）与员工（右）；7 条带标签的箭头在框间穿插，贷款、账户、客户构成交叉的视觉中心。"
}
```

## 相关图

```json
[
  {
    "target": "G190/fig4-1",
    "relation": "complements",
    "note_zh": "同为信息地图示例：图 2-1 只画概念与关系，图 4-1 进一步把信息概念挂到业务能力上"
  },
  {
    "target": "G190/figA-3",
    "relation": "related",
    "note_zh": "同样的 6 个概念与 7 组关系，在附录 A 中改用 UML 类图并补充属性"
  },
  {
    "target": "G190/figA-5",
    "relation": "related",
    "note_zh": "同样的 6 个概念与 7 组关系，在附录 A 中改用带鸦爪基数的 ERD"
  },
  {
    "target": "G190/fig5-1",
    "relation": "contrasts_with",
    "note_zh": "图 5-1 说明信息地图还可以包含无法还原为数据字段的概念（客户认知），与本图“可数据化”的示例形成对照"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图未说明 7 条关系是否有意省略其他概念间关系，本分析只按画出的线记录。",
    "“is made against”的中文译法不唯一（针对贷款付款／以贷款为付款对象），此处取“针对……付款”。"
  ],
  "analyzed_from": [
    "英文 PDF 第 12 页图 2-1 原图截图（含 2x2 放大分块）",
    "英文 PDF 第 12 页正文与第 16 页相关段落",
    "中文稿 G190e_信息映射.md 第 94、98 行",
    "figs/g190_fig2-1.svg 源码及其渲染图对比"
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
