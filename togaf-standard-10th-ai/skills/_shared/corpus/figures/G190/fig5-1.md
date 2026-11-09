# G190/fig5-1 · 多个业务概念之间的示例关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G190/fig5-1.md) · [JSON](../../architecture/diagrams/G190/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G190e.pdf`；SHA-256：`7d7431f02be8992e49abbee999263a7d0065506dd6f8d94da210b2ae20853d03`。

## 原图 · PDF 第 16 页

![英文原图](../assets/G190/fig5-1-p0016.png)

PDF 坐标：`[86.9, 391.4, 525.1, 576.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Customer
Product
is based on
Customer
Perception
evaluates
impas
‘the
establishes
‘ome of
Sales Force
Customer Mgmt.
has the ability
Sales
Customer
Lead
Analysis
```

## 概要（历史解释；局部修正见上）

用客户认知、产品供给、销售线索、客户分析四个概念，示范信息地图如何表达无法还原为数据字段的业务信息。

## 目的（历史解释；局部修正见上）

第 5 章要说明信息地图不等于数据模型：客户认知是主观判断，不能存成数据字段，但它与产品供给、销售能力、利益相关者之间存在真实关系。本图给出这种“多概念关系”的样例，为图 2-1/4-1 这类可数据化的示例作对照。

## 阅读顺序（历史解释；局部修正见上）

先看右侧图例确认卡片标题颜色的含义（蓝=信息类型、绿=利益相关者、红=业务能力），再按箭头读四个概念：客户认知—产品供给在上方，销售线索在左下，客户分析在右下。箭头旁的动词短语说明主语对宾语做什么；卡片彩色标题是类别，白色部分才是被连线指涉的具体概念。

## 关键含义（历史解释；局部修正见上）

- 四个概念分属三种类型：客户认知与产品供给是信息类型，销售线索是利益相关者，客户分析是业务能力；颜色只标在卡片标题上。
- 客户认知“基于”产品供给：企业需要了解客户对某产品的认知，才能做内部规划（正文语境）。
- 销售线索负责人“评估”客户认知——这是一种依赖经验、无法还原为数据字段的主观判断，正是本图要说明的非数据化信息。
- 销售线索“影响产品供给的结果”，并“具备”客户分析能力：利益相关者通过能力作用于信息，而不是直接读写数据。
- 客户分析（业务能力）“建立”产品供给：能力确立信息概念，与第 4 章“能力使用/修改信息”的论断一致。
- 图中没有任何数据存储、字段或系统，说明信息地图可以描述尚未（甚至无法）数据化的业务信息。

## 层级（历史解释；局部修正见上）

两层卡片结构：每张卡片的彩色标题是类别/主体（Customer、Product、Sales Force、Customer Mgmt.），白色部分是具体概念（Customer Perception、Product Offering、Sales Lead、Customer Analysis），白框在视觉上隶属同一张卡片。概念之间没有上下级，只有箭头关系；右侧图例是独立说明区。

## 线条含义（历史解释；局部修正见上）

5 条黑色实线箭头，均带动词短语：is based on（客户认知→产品供给）、evaluates（销售线索→客户认知）、impacts the outcome of（销售线索→产品供给）、has the ability（销售线索→客户分析）、establishes（客户分析→产品供给）。箭头方向即句子主语→宾语；没有虚线、基数或组合/泛化符号。

## 易误读点（历史解释；局部修正见上）

- 卡片彩色标题不是与白框并列的第二个实体，而是同一张卡片上的类别标题；箭头都落在白色部分的具体概念上。
- “is based on”箭头由客户认知指向产品供给（客户认知基于产品供给），不是产品供给基于客户认知。
- 红色卡片标题“Customer Mgmt.”只是说明这是业务能力类别，不代表客户管理系统或组织单元。
- 中文图的“销售线索”是错译，不要据此把 Sales Lead 理解为营销线索；它是做出产品建议的人（利益相关者）。
- 本图不是数据模型：客户认知被正文明确描述为不可直接读取、不可还原为数据字段的信息。

## 元素

```json
[
  {
    "id": "cust_type",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "data",
    "level": 1,
    "position": "左上卡片标题（蓝色）",
    "attributes": {
      "card_color": "blue"
    }
  },
  {
    "id": "customer_perception",
    "label_en": "Customer Perception",
    "label_zh": "客户认知",
    "type": "data",
    "parent": "cust_type",
    "level": 2,
    "position": "左上卡片正文"
  },
  {
    "id": "product_type",
    "label_en": "Product",
    "label_zh": "产品",
    "type": "data",
    "level": 1,
    "position": "右上卡片标题（蓝色）",
    "attributes": {
      "card_color": "blue"
    }
  },
  {
    "id": "product_offering",
    "label_en": "Product Offering",
    "label_zh": "产品供给",
    "type": "data",
    "parent": "product_type",
    "level": 2,
    "position": "右上卡片正文"
  },
  {
    "id": "sales_force",
    "label_en": "Sales Force",
    "label_zh": "销售队伍",
    "type": "organization_unit",
    "level": 1,
    "position": "左下卡片标题（绿色）",
    "attributes": {
      "card_color": "green"
    }
  },
  {
    "id": "sales_lead",
    "label_en": "Sales Lead",
    "label_zh": "销售线索负责人",
    "type": "stakeholder",
    "parent": "sales_force",
    "level": 2,
    "position": "左下卡片正文"
  },
  {
    "id": "customer_mgmt",
    "label_en": "Customer Mgmt.",
    "label_zh": "客户管理",
    "type": "capability",
    "level": 1,
    "position": "右下卡片标题（红色）",
    "attributes": {
      "card_color": "red"
    }
  },
  {
    "id": "customer_analysis",
    "label_en": "Customer Analysis",
    "label_zh": "客户分析",
    "type": "capability",
    "parent": "customer_mgmt",
    "level": 2,
    "position": "右下卡片正文"
  }
]
```

## 关系

```json
[
  {
    "from": "customer_perception",
    "to": "product_offering",
    "type": "association",
    "label_en": "is based on",
    "label_zh": "基于",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "上方水平箭头，客户认知基于产品供给。"
  },
  {
    "from": "sales_lead",
    "to": "customer_perception",
    "type": "association",
    "label_en": "evaluates",
    "label_zh": "评估",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧竖直箭头向上，销售线索负责人评估客户认知。"
  },
  {
    "from": "sales_lead",
    "to": "product_offering",
    "type": "influence",
    "label_en": "impacts the outcome of",
    "label_zh": "影响……的结果",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "中部斜线，销售线索负责人影响产品供给的结果。"
  },
  {
    "from": "sales_lead",
    "to": "customer_analysis",
    "type": "assignment",
    "label_en": "has the ability",
    "label_zh": "具备……能力",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "下方水平箭头，销售线索负责人具备客户分析能力。"
  },
  {
    "from": "customer_analysis",
    "to": "product_offering",
    "type": "produces",
    "label_en": "establishes",
    "label_zh": "建立",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "右侧竖直箭头向上，客户分析能力建立产品供给信息。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色标题条 Information Type",
    "meaning_zh": "信息类型（Information Type）",
    "explicit": true
  },
  {
    "symbol": "绿色标题条 Stakeholder",
    "meaning_zh": "利益相关者（Stakeholder）",
    "explicit": true
  },
  {
    "symbol": "红色标题条 Business Capability",
    "meaning_zh": "业务能力（Business Capability）",
    "explicit": true
  },
  {
    "symbol": "彩色标题 + 白色正文的两段式卡片",
    "meaning_zh": "标题是类别/主体，白色部分是具体概念",
    "explicit": false
  },
  {
    "symbol": "黑色实线箭头 + 动词短语",
    "meaning_zh": "概念间的有向关系",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "四张两段式卡片呈 2×2 分布（客户认知左上、产品供给右上、销售线索左下、客户分析右下），右侧竖排三色图例；箭头在上方横向、左侧纵向与中部斜向连接。"
}
```

## 相关图

```json
[
  {
    "target": "G190/fig2-1",
    "relation": "complements",
    "note_zh": "图 2-1 的概念都可以落到数据模式；本图专门给出无法数据化的客户认知，用来说明信息地图与数据模型的区别"
  },
  {
    "target": "G190/fig4-1",
    "relation": "related",
    "note_zh": "两图都涉及“业务能力—信息概念”的关系，本图把能力与利益相关者、主观判断放在一起"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "卡片彩色标题与白色正文究竟是“类别+具体概念”还是“同一概念的两行名称”，原图未明说；此处按前者记录并作为父子关系。",
    "“impacts the outcome of”从销售线索卡片的右上角（Sales Force 标题处）引出而非白框正文，但语义指向 Sales Lead；元素归属按正文判断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 16 页图 5-1 原图截图",
    "英文 PDF 第 16 页正文",
    "中文稿 G190e_信息映射.md 第 153、157 行及第 161–181 行标签对照表",
    "figs/g190e_fig5-1_en.png 与 figs/zh/g190e_fig5-1_zh.png"
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
