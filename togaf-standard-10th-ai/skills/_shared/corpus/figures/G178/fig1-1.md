# G178/fig1-1 · 价值流示例

> 当前图示解析：[Markdown](../../architecture/diagrams/G178/fig1-1.md) · [JSON](../../architecture/diagrams/G178/fig1-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G178e.pdf`；SHA-256：`517130a041a8d956b2868dc39d570b84e2d80c64709e4c1368f9747388a3a026`。

## 原图 · PDF 第 12 页

![英文原图](../assets/G178/fig1-1-p0012.png)

PDF 坐标：`[48.2, 190.7, 563.8, 273.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
7
Acquire Retail Product
Advertise
Display
Enable
Process
Deliver
Channels
Merchandise
Selection
Payment
Merchandise
D
y
D
y,
y,
```

## 概要（历史解释；局部修正见上）

“获取零售产品”价值流由 5 个依次相接的阶段组成：广告渠道→展示商品→启用选择→处理付款→交付商品。

## 目的（历史解释；局部修正见上）

第 1.3 节用它给出价值流最简单的样子：价值流是为客户、利益相关者或最终用户创造整体结果的一组端到端增值活动，建模时表示为一串价值流阶段，每个阶段在前一阶段的基础上增加利益相关者价值。正文还用它作为“外部触发”价值流的例子（零售客户购买商品）。同一张图在第 4.1 节作为图 4-1 再次出现，作为基线示例，配合表 4-1（价值流定义）和表 4-2（各阶段要素）。

## 阅读顺序（历史解释；局部修正见上）

先读外框左上角的价值流名称“Acquire Retail Product（获取零售产品）”，再从左到右读框内 5 个 V 形箭头，每个箭头是一个价值流阶段。第一个箭头左端是缺口，最后一个箭头右端是尖头，其余箭头的尖端嵌进下一个箭头的缺口，表示紧接的先后顺序。图里没有单独的连线，也没有利益相关者、能力或流程等其他元素。

## 关键含义（历史解释；局部修正见上）

- 价值流用“动词—名词”命名，从触发方利益相关者（这里是零售顾客）的视角表述；“获取零售产品”是本指南贯穿使用的两个价值流示例之一（另一个是“招聘员工”，见图 4-2）。
- 价值流的 5 个阶段按顺序排列：广告渠道 → 展示商品 → 启用选择 → 处理付款 → 交付商品；阶段名用两三个词说明该阶段达成什么（第 2.2 节规则）。
- 每个阶段逐步累加利益相关者价值；表 4-2 给出各阶段的价值项，依次为：客户可获得零售渠道、客户获得产品选项、定位到所需产品、交付承诺、客户占有产品。
- 前一阶段的退出标准就是后一阶段的进入标准（第 2.2 节），表 4-2 中依次衔接：客户选择渠道 → 客户查看产品 → 客户选定产品 → 款项已支付 → 产品已交付。
- 这是外部触发的价值流（零售客户购买商品）；正文用“经理招聘新员工”作为内部触发价值流的对照，后者就是第 4.2 节的“招聘员工”价值流。
- 首尾相接的箭头不代表一旦开始就必须走完：正文指出每个阶段之后都可以停止，例如顾客看到价格后决定不买了。
- 图中只画阶段，不画执行阶段所需的流程、角色、信息或技术，也还没有映射业务能力；能力映射在第 2.3 节和第 4.2 节（图 4-3）才做。

## 层级（历史解释；局部修正见上）

两层。第 0 层是外框代表的“获取零售产品”价值流；第 1 层是框内的 5 个价值流阶段，通过视觉包含表达“价值流由价值阶段组成”。阶段之间是同级的先后关系，没有更深的分解。

## 线条含义（历史解释；局部修正见上）

图中没有独立的连线。V 形箭头本身就是阶段，箭头尖端嵌进下一阶段的缺口，表示先后顺序（关系清单中记为 sequence）；外框只表示这些阶段属于同一条价值流（用 parent 表示）。

## 易误读点（历史解释；局部修正见上）

- V 形箭头是阶段本身，不是阶段之间的流转线，也不表示物流或数据流。
- 阶段首尾相接不表示必须连续走完，每个阶段之后都可能停止。
- 价值流阶段不是业务流程：一个阶段可以映射到一个或多个业务流程，流程的粒度更细（第 1.4 节）。
- “广告渠道（Advertise Channels）”指“让客户知道有哪些零售渠道可用”的行为（价值项是“客户可获得零售渠道”），不是指投放广告的媒体渠道；“启用选择（Enable Selection）”指帮助客户筛选和评估产品。
- 中文稿引用的 SVG 底部写着“外箭头表示端到端流向”，原图和 SVG 中都没有外箭头；原图用灰色外框表示价值流整体。

## 元素

```json
[
  {
    "id": "vs_acquire_retail",
    "label_en": "Acquire Retail Product",
    "label_zh": "获取零售产品（价值流）",
    "type": "value_stream",
    "parent": null,
    "level": 0,
    "position": "外框左上角",
    "description_zh": "触发方利益相关者：希望购买产品的零售顾客；价值：客户能找到所需产品并及时获得（表 4-1）。"
  },
  {
    "id": "st_advertise",
    "label_en": "Advertise Channels",
    "label_zh": "广告渠道",
    "type": "value_stream_stage",
    "parent": "vs_acquire_retail",
    "level": 1,
    "order": 1,
    "description_zh": "让客户知道公司产品的行为；进入标准：客户搜索产品；退出标准：客户选择渠道；价值项：客户可获得零售渠道（表 4-2）。"
  },
  {
    "id": "st_display",
    "label_en": "Display Merchandise",
    "label_zh": "展示商品",
    "type": "value_stream_stage",
    "parent": "vs_acquire_retail",
    "level": 1,
    "order": 2,
    "description_zh": "以实体或可搜索的数字形式呈现产品；进入：客户选择渠道；退出：客户查看产品；价值项：客户获得产品选项。"
  },
  {
    "id": "st_enable_selection",
    "label_en": "Enable Selection",
    "label_zh": "启用选择",
    "type": "value_stream_stage",
    "parent": "vs_acquire_retail",
    "level": 1,
    "order": 3,
    "description_zh": "帮助客户筛选和评估最符合需求的产品；进入：客户查看产品；退出：客户选定产品；价值项：定位到所需产品。"
  },
  {
    "id": "st_process_payment",
    "label_en": "Process Payment",
    "label_zh": "处理付款",
    "type": "value_stream_stage",
    "parent": "vs_acquire_retail",
    "level": 1,
    "order": 4,
    "description_zh": "收取并处理客户付款；进入：客户选定产品；退出：款项已支付；价值项：交付承诺。"
  },
  {
    "id": "st_deliver",
    "label_en": "Deliver Merchandise",
    "label_zh": "交付商品",
    "type": "value_stream_stage",
    "parent": "vs_acquire_retail",
    "level": 1,
    "order": 5,
    "description_zh": "把产品交到客户手中；进入：款项已支付；退出：产品已交付；价值项：客户占有产品。"
  }
]
```

## 关系

```json
[
  {
    "from": "st_advertise",
    "to": "st_display",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "V 形箭头首尾相接"
  },
  {
    "from": "st_display",
    "to": "st_enable_selection",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "st_enable_selection",
    "to": "st_process_payment",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "st_process_payment",
    "to": "st_deliver",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_acquire_retail",
    "kind": "sequence",
    "name_zh": "获取零售产品价值流",
    "steps": [
      "st_advertise",
      "st_display",
      "st_enable_selection",
      "st_process_payment",
      "st_deliver"
    ],
    "description_zh": "每个阶段之后都可能停止（第 2.2 节）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深灰色外框 + 左上角粗体名称",
    "meaning_zh": "一条价值流（整体）",
    "explicit": false
  },
  {
    "symbol": "浅灰 V 形箭头（chevron）",
    "meaning_zh": "价值流阶段",
    "explicit": false
  },
  {
    "symbol": "箭头首尾相接、从左到右",
    "meaning_zh": "阶段的先后顺序；前一阶段的退出标准是后一阶段的进入标准",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "一个横向的深灰色长框，左上角是价值流名称，框内一行 5 个首尾相接的浅灰 V 形箭头，从左到右；右上角有很小的“© The Open Group”。"
}
```

## 相关图

```json
[
  {
    "target": "G178/fig4-1",
    "relation": "same_as",
    "note_zh": "第 4.1 节把本图作为图 4-1 再次使用，内容完全相同"
  },
  {
    "target": "G178/fig1-2",
    "relation": "instance_of",
    "note_zh": "图 1-2 中“价值流由价值阶段组成”的具体例子"
  },
  {
    "target": "G178/fig4-2",
    "relation": "complements",
    "note_zh": "正文以本图为外部触发价值流的例子、以“招聘员工”（图 4-2）为内部触发价值流的例子，两者是本指南贯穿使用的两个价值流"
  },
  {
    "target": "G233/fig6-3",
    "relation": "related",
    "note_zh": "G233 图 6-3 是同名价值流的在线零售版本，阶段不同（浏览在线商店、选择产品、审核购物篮、购买产品、交付产品），并用 ArchiMate 展开了能力与应用；不是同一张图"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 12 页原图截图（220 dpi）",
    "英文 PDF 第 12、15、16、18、19 页正文（含表 4-1、表 4-2）",
    "中文稿 G178e_价值流.md 第 97–104 行、第 197–222 行",
    "figs/g178_fig1-1.svg 源码",
    "G233/fig6-3 原图截图（仅用于核对图间关系）"
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
