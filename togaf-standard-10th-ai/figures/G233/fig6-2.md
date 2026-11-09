# G233/fig6-2 · 把业务能力映射到价值流阶段

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig6-2.md) · [JSON](../../architecture/diagrams/G233/fig6-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 35 页

![英文原图](../assets/G233/fig6-2-p0035.png)

PDF 坐标：`[61.1, 418.8, 550.9, 716.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Acquire Retail Product Online Value Stream
Gutoneranverstsore 5) Cusmer cB)
Browse Online =>
Select
>
Review Basket
Purchase
Deliver
p>)
Store
Product(s)
Products
Products
Store Layout ff]
Basket i]
Basket ff
Delivery af]
Management
Management
Management
Management
Il
il
Warehouse S=
‘Value Stream
Fulfilment
Products
Catalog
Products
Catalog
Management
Identity
Processing
Payment f]
ot |
il
Identity]
Inventory
Basket
Delivery
Management
Management
Management
Management
yy
Identity
Inventory
Management
Management
==
```

## 概要（历史解释；局部修正见上）

把在线获取零售产品价值流的五个阶段逐列对应到使能它们的能力，形成“阶段×能力”的交叉映射底图。

## 目的（历史解释；局部修正见上）

第 6.3 节的核心活动：查阅能力目录，把相关能力链接（交叉映射）到每个价值流阶段，从而识别哪些能力对交付利益相关者价值最关键、因而必须被实例化到足够质量。这张图就是该活动的示例结果，也是图 6-3 能力实例模型的直接输入。

## 阅读顺序（历史解释；局部修正见上）

先读顶部沙色容器标题（Acquire Retail Product Online Value Stream），再看左上触发事件与客户；中间五列从左到右是阶段顺序：Browse Online Store → Select Product(s) → Review Basket → Purchase Products → Deliver Products。每列下方的沙色框就是使能该阶段的能力；同一能力出现在多列表示它被多个阶段复用。Deliver Products 列里的灰蓝色框不是能力，而是被调用的子价值流。

## 关键含义（历史解释；局部修正见上）

- 五个阶段及使能能力：Browse Online Store（Store Layout Management、Catalog Products、Identity Management）；Select Product(s)（Basket Management、Catalog Products、Inventory Management）；Review Basket（Basket Management、Identity Management）；Purchase Products（Delivery Management、Payment Processing、Basket Management、Identity Management）；Deliver Products（Warehouse Order Fulfillment Value Stream、Delivery Management、Inventory Management）。
- 能力复用很明显：Basket Management 出现在 3 个阶段，Identity Management 出现在 3 个阶段，Catalog Products、Delivery Management、Inventory Management 各出现 2 次；说明一个能力可以跨阶段使能多个价值流环节。
- Deliver Products 列的第一项不是能力而是子价值流“Warehouse Order Fulfillment Value Stream”，表示该阶段通过另一条价值流来完成；这是“价值流调用价值流”的建模手法（该子价值流的阶段见图 5-1）。
- 映射只表达“哪些能力使能哪个阶段”，不表达能力成熟度、差距或优劣；这些要到图 7-1/7-2 才引入。
- Purchase Products 列挂的能力最多（4 个），是跨能力协作最密集的阶段；这与正文对该阶段需处理配送方式、支付、身份与购物篮的描述一致。
- 按正文，映射的目的是挑出“关键能力”，而不是把所有能力都列上；因此图中列出的能力应理解为对该阶段至关重要的子集。
- 图 6-3 在本图基础上为每个能力框补上角色、应用组件、数据对象与流程，把“能力”变成“能力实例”。

## 层级（历史解释；局部修正见上）

三层：价值流（容器）→ 5 个阶段（列）→ 阶段下的能力框（可多个，纵向并列）。能力框之间无上下级；同一能力在不同列是同一目录能力的多次引用，不是多个子能力。子价值流嵌在 Deliver Products 列内，属于该阶段的使能要素。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线（原图确实无连线）。阶段顺序由列从左到右表达；“能力使能该阶段”由能力框位于该阶段列下方隐含表达（关系清单标为推断）。中文 SVG 自加的竖线/斜线不是原图内容。

## 易误读点（历史解释；局部修正见上）

- 不要把同一能力在多个列中出现理解为多个不同能力实例；在图 6-2 层面它们是同一目录能力被多个阶段复用，实例化是图 6-3 的事。
- 不要把 Deliver Products 列的“Warehouse Order Fulfillment Value Stream”当成一个能力；它是子价值流。
- 不要从本图读出能力差距或优先级；图中没有颜色、评分或排序。
- 中文稿引用的 figs/g233_fig6-2.svg 是占位符示意图（阶段 1–4、能力 A–D），既无真实名称也无原图版式，不能作为理解依据。
- 不要把列内能力框的上下顺序读成优先级或时间顺序；它们是并列的。

## 元素

```json
[
  {
    "id": "vs_acquire",
    "label_en": "Acquire Retail Product Online Value Stream",
    "label_zh": "在线获取零售产品价值流",
    "type": "value_stream",
    "parent": null,
    "position": "沙色大容器"
  },
  {
    "id": "ev_arrives",
    "label_en": "Customer arrives at store",
    "label_zh": "客户到店",
    "type": "event",
    "parent": "vs_acquire",
    "position": "容器内左上（黄）"
  },
  {
    "id": "st_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "stakeholder",
    "parent": "vs_acquire",
    "position": "容器内上排（紫）"
  },
  {
    "id": "stg_browse",
    "label_en": "Browse Online Store",
    "label_zh": "浏览在线商店",
    "type": "value_stream_stage",
    "parent": "vs_acquire",
    "order": 1,
    "position": "第一列"
  },
  {
    "id": "stg_select",
    "label_en": "Select Product(s)",
    "label_zh": "选择产品",
    "type": "value_stream_stage",
    "parent": "vs_acquire",
    "order": 2,
    "position": "第二列"
  },
  {
    "id": "stg_review",
    "label_en": "Review Basket",
    "label_zh": "查看购物篮",
    "type": "value_stream_stage",
    "parent": "vs_acquire",
    "order": 3,
    "position": "第三列"
  },
  {
    "id": "stg_purchase",
    "label_en": "Purchase Products",
    "label_zh": "购买产品",
    "type": "value_stream_stage",
    "parent": "vs_acquire",
    "order": 4,
    "position": "第四列"
  },
  {
    "id": "stg_deliver",
    "label_en": "Deliver Products",
    "label_zh": "交付产品",
    "type": "value_stream_stage",
    "parent": "vs_acquire",
    "order": 5,
    "position": "第五列"
  },
  {
    "id": "cap_store_layout",
    "label_en": "Store Layout Management",
    "label_zh": "门店布局管理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "仅出现在 Browse Online Store 下。"
  },
  {
    "id": "cap_catalog",
    "label_en": "Catalog Products",
    "label_zh": "产品编目",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "同时出现在 Browse 与 Select 两列。"
  },
  {
    "id": "cap_identity",
    "label_en": "Identity Management",
    "label_zh": "身份管理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "出现在 Browse、Review、Purchase 三列。"
  },
  {
    "id": "cap_basket",
    "label_en": "Basket Management",
    "label_zh": "购物篮管理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "出现在 Select、Review、Purchase 三列。"
  },
  {
    "id": "cap_inventory",
    "label_en": "Inventory Management",
    "label_zh": "库存管理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "出现在 Select 与 Deliver 两列。"
  },
  {
    "id": "cap_delivery",
    "label_en": "Delivery Management",
    "label_zh": "交付管理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "出现在 Purchase 与 Deliver 两列。"
  },
  {
    "id": "cap_payment",
    "label_en": "Payment Processing",
    "label_zh": "支付处理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "仅出现在 Purchase Products 下。"
  },
  {
    "id": "vs_warehouse",
    "label_en": "Warehouse Order Fulfillment Value Stream",
    "label_zh": "仓库订单履约价值流",
    "type": "value_stream",
    "parent": null,
    "description_zh": "作为 Deliver Products 阶段的使能要素嵌入，不是业务能力。"
  },
  {
    "id": "out_acquired",
    "label_en": "Customer successfully acquires retail product",
    "label_zh": "客户成功获得零售产品",
    "type": "goal",
    "parent": "vs_acquire",
    "position": "右下紫色椭圆"
  }
]
```

## 关系

```json
[
  {
    "from": "ev_arrives",
    "to": "vs_acquire",
    "type": "triggering",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "触发事件位于价值流容器左上。"
  },
  {
    "from": "vs_acquire",
    "to": "stg_browse",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_acquire",
    "to": "stg_select",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_acquire",
    "to": "stg_review",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_acquire",
    "to": "stg_purchase",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_acquire",
    "to": "stg_deliver",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "st_customer",
    "to": "vs_acquire",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "客户是接收价值的利益相关者。"
  },
  {
    "from": "cap_store_layout",
    "to": "stg_browse",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "位于该阶段列下方，表示使能。"
  },
  {
    "from": "cap_catalog",
    "to": "stg_browse",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_identity",
    "to": "stg_browse",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_basket",
    "to": "stg_select",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_catalog",
    "to": "stg_select",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_inventory",
    "to": "stg_select",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_basket",
    "to": "stg_review",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_identity",
    "to": "stg_review",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_delivery",
    "to": "stg_purchase",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_payment",
    "to": "stg_purchase",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_basket",
    "to": "stg_purchase",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_identity",
    "to": "stg_purchase",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "vs_warehouse",
    "to": "stg_deliver",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "子价值流使能该阶段（此处是价值流而非能力）。"
  },
  {
    "from": "cap_delivery",
    "to": "stg_deliver",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "cap_inventory",
    "to": "stg_deliver",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "vs_acquire",
    "to": "out_acquired",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "价值流成功结束时交付该成果。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_acquire",
    "kind": "sequence",
    "name_zh": "在线获取零售产品阶段序列",
    "steps": [
      "stg_browse",
      "stg_select",
      "stg_review",
      "stg_purchase",
      "stg_deliver"
    ],
    "description_zh": "五个阶段从左到右；正文说明可回退或跳过（如不查看购物篮直接结账）。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_mapping",
    "title_zh": "阶段×能力交叉映射（按列逐项转录，列内自上而下）",
    "columns": [
      "价值流阶段",
      "使能能力/子价值流"
    ],
    "rows": [
      [
        "Browse Online Store 浏览在线商店",
        "Store Layout Management 门店布局管理；Catalog Products 产品编目；Identity Management 身份管理"
      ],
      [
        "Select Product(s) 选择产品",
        "Basket Management 购物篮管理；Catalog Products 产品编目；Inventory Management 库存管理"
      ],
      [
        "Review Basket 查看购物篮",
        "Basket Management 购物篮管理；Identity Management 身份管理"
      ],
      [
        "Purchase Products 购买产品",
        "Delivery Management 交付管理；Payment Processing 支付处理；Basket Management 购物篮管理；Identity Management 身份管理"
      ],
      [
        "Deliver Products 交付产品",
        "Warehouse Order Fulfillment Value Stream 仓库订单履约价值流（子价值流）；Delivery Management 交付管理；Inventory Management 库存管理"
      ]
    ],
    "notes_zh": "同一能力在多列重复出现即多次使能；表中保留每次出现，便于核对原图。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "沙色大框 + V 形图标",
    "meaning_zh": "价值流",
    "explicit": false
  },
  {
    "symbol": "黄色框 + 事件图标",
    "meaning_zh": "触发事件",
    "explicit": false
  },
  {
    "symbol": "紫色六边形 + 双环图标",
    "meaning_zh": "利益相关者",
    "explicit": false
  },
  {
    "symbol": "白色列卡 + V 形图标",
    "meaning_zh": "价值流阶段",
    "explicit": false
  },
  {
    "symbol": "沙色框 + 能力图标",
    "meaning_zh": "使能该阶段的业务能力",
    "explicit": false
  },
  {
    "symbol": "灰蓝色框 + 蓝色价值流图标",
    "meaning_zh": "被调用的子价值流（非能力）",
    "explicit": false
  },
  {
    "symbol": "紫色椭圆（无图标）",
    "meaning_zh": "价值流最终成果/价值项",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "沙色价值流容器横跨全图：顶部标题，左上触发事件与客户；下方五列白色阶段卡，每列内纵向堆叠 2–4 个能力框；Deliver Products 列首项为灰蓝色子价值流；右下角为最终成果椭圆。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig6-1",
    "relation": "follows",
    "note_zh": "本图的能力全部取自图 6-1 的能力目录（Basket、Catalog、Identity、Inventory、Delivery、Payment 等）"
  },
  {
    "target": "G233/fig6-3",
    "relation": "precedes",
    "note_zh": "图 6-3 在本映射基础上为每个能力补上角色、应用、数据对象与流程，形成能力实例模型"
  },
  {
    "target": "G233/fig5-1",
    "relation": "related",
    "note_zh": "本图 Deliver Products 列引用的 Warehouse Order Fulfillment Value Stream 就是图 5-1 示例的那条价值流"
  },
  {
    "target": "G178/fig4-3",
    "relation": "related",
    "note_zh": "G178 图 4-3 是同一手法在招聘价值流上的交叉映射，可对照能力复用与二级能力下钻的做法"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图没有连线，能力是否真的“使能”阶段只能由列位置推断；本文按推断关系记录。",
    "同一能力在多列重复时，原图没有编号区分，无法判断作者是否把它们视为同一能力的不同实例；按图 6-2 的定位，本文记为同一能力的多次映射。"
  ],
  "analyzed_from": [
    "英文 PDF 第 35 页图 6-2 截图（450 dpi）",
    "英文 PDF 第 35 页正文、图题与整页版式",
    "中文稿 G233e_业务能力规划.md 第 533–537 行",
    "figs/g233_fig6-2.svg 的文本与源码"
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
