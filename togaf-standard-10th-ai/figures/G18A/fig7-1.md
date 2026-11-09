# G18A/fig7-1 · 零售商业务模型画布——现状

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/fig7-1.md) · [JSON](../../architecture/diagrams/G18A/fig7-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 24 页

![英文原图](../assets/G18A/fig7-1-p0024.png)

PDF 坐标：`[48.2, 349.5, 563.8, 681.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Retailer Business Model Diagram — Current State
Key Partners
Key Activities
Value Propositions
aa
Customer Segments
?
iv}
=
Customer Relationships @
a2
Product
Customer
Low
Personal
Mass
Manufacturers
Analysis.
Prices
Assistance
Market
National
Supplier
Personal Touch
Warranty
Regional
Suppliers
Management
Service
Specialization
Key Resources
saul
Channels
ms
Regional
Availability for
Suppliers
Brand
Common and
Retail
Reputation
Regional Needs
Shopfronts
Real
Web-based
Estate
Inventory Info
Cost Structure
Revenue Streams
Facilities and Transport
Profit on Sales
Employees and Supply
Warranty Service
Scale Across Nation
Manufacture Rebates
```

## 概要（历史解释；局部修正见上）

用业务模型画布逐块列出某零售企业现状的九个构建块内容。

## 目的（历史解释；局部修正见上）

以零售企业为例演示如何用业务模型画布描述现状业务模型；它既是第 7 章现状基线的完整示例，也是随后与未来态（图 7-2）对照、进而引出价值流与能力差距分析的起点。

## 阅读顺序（历史解释；局部修正见上）

按标准画布布局读：中列 Value Propositions；向右上 Customer Relationships、右下 Channels、最右 Customer Segments；向左 Key Partners 以及上 Key Activities、下 Key Resources；底部左 Cost Structure、右 Revenue Streams。正文建议从客户视角从右向左读：先看客户细分，再看价值主张与渠道/关系，最后看左侧资源、活动、伙伴与成本。块内条目自上而下排列，没有箭头。

## 关键含义（历史解释；局部修正见上）

- 客户细分只有 Mass Market 与 Regional Specialization，说明企业采取“大众市场 + 区域专业化”的双重定位。
- 价值主张三条：Low Prices、Personal Touch、Availability for Common and Regional Needs，集中在价格、服务与可获得性。
- 渠道两条：Retail Shopfronts（实体店面）与 Web-based Inventory Info（线上查库存），是“线下为主、线上仅提供信息”的组合。
- 客户关系两条：Personal Assistance 与 Warranty Service；其中 Warranty Service 同时出现在收入来源块，说明保修既是关系手段也是收入来源。
- 关键资源只有 Brand Reputation 与 Real Estate；关键活动为 Customer Analysis 与 Supplier Management，与正文“强大客户分析、维护品牌与地产”一致。
- 关键合作伙伴三类：Product Manufacturers、National Suppliers、Regional Suppliers，呈“制造 + 全国 + 区域”的供应结构。
- 成本三项：Facilities and Transport、Employees and Supply、Scale Across Nation，与实体店面、房地产、全国扩张相呼应。
- 画布内没有箭头，九个块的关系由版式表达；块内条目自上而下不代表优先级。

## 层级（历史解释；局部修正见上）

两层：画布整体（带标题的矩形框）下分九个构建块，每块下为 2–3 个条目。九个块并列；Cost Structure 与 Revenue Streams 横跨底部两段，各占一半宽度。

## 线条含义（历史解释；局部修正见上）

图中没有箭头或连线，只有分隔块用的直线（竖线与横线）。块内黄色条目框是并列清单，不含顺序或依赖。价值侧与成本侧的区分由左右位置表达。

## 易误读点（历史解释；局部修正见上）

- 不要把块内条目自上而下的次序当成优先级或时间顺序。
- Warranty Service 在客户关系与收入来源两块各出现一次，是两个不同视角，不是重复错误。
- 不要忽略最右侧 Customer Segments 块：画布右侧是客户侧，正文建议从这里开始读。
- 不要把图顶标题中的 Diagram 误认为与 Canvas 不同的方法；正文明确这是 Business Model Canvas 的实例。
- 中文稿正文第 208 行把英文 “sustained services” 译为“保修服务”、把 “facilities” 译为“房地产”，是意译；图内对应 Warranty Service 与 Real Estate。

## 元素

```json
[
  {
    "id": "canvas",
    "label_en": "Retailer Business Model Diagram – Current State",
    "label_zh": "零售商业务模型图——现状",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "整张画布，标题条在框外上方居中"
  },
  {
    "id": "kp",
    "label_en": "Key Partners",
    "label_zh": "关键合作伙伴",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 1 列，通高",
    "order": 1
  },
  {
    "id": "ka",
    "label_en": "Key Activities",
    "label_zh": "关键活动",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 2 列上半",
    "order": 2
  },
  {
    "id": "kr",
    "label_en": "Key Resources",
    "label_zh": "关键资源",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 2 列下半",
    "order": 3
  },
  {
    "id": "vp",
    "label_en": "Value Propositions",
    "label_zh": "价值主张",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 3 列，通高",
    "order": 4
  },
  {
    "id": "cr",
    "label_en": "Customer Relationships",
    "label_zh": "客户关系",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 4 列上半",
    "order": 5
  },
  {
    "id": "ch",
    "label_en": "Channels",
    "label_zh": "渠道",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 4 列下半",
    "order": 6
  },
  {
    "id": "cs",
    "label_en": "Customer Segments",
    "label_zh": "客户细分",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "第 5 列，通高",
    "order": 7
  },
  {
    "id": "cost",
    "label_en": "Cost Structure",
    "label_zh": "成本结构",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "底部横条左半",
    "order": 8
  },
  {
    "id": "rev",
    "label_en": "Revenue Streams",
    "label_zh": "收入来源",
    "type": "group",
    "parent": "canvas",
    "level": 1,
    "position": "底部横条右半",
    "order": 9
  },
  {
    "id": "kp_manufacturers",
    "label_en": "Product Manufacturers",
    "label_zh": "产品制造商",
    "type": "actor",
    "parent": "kp",
    "level": 2,
    "order": 1,
    "position": "第 1 列第 1 条"
  },
  {
    "id": "kp_national",
    "label_en": "National Suppliers",
    "label_zh": "全国供应商",
    "type": "actor",
    "parent": "kp",
    "level": 2,
    "order": 2,
    "position": "第 1 列第 2 条"
  },
  {
    "id": "kp_regional",
    "label_en": "Regional Suppliers",
    "label_zh": "区域供应商",
    "type": "actor",
    "parent": "kp",
    "level": 2,
    "order": 3,
    "position": "第 1 列第 3 条"
  },
  {
    "id": "ka_analysis",
    "label_en": "Customer Analysis",
    "label_zh": "客户分析",
    "type": "process",
    "parent": "ka",
    "level": 2,
    "order": 1,
    "position": "第 2 列上块第 1 条"
  },
  {
    "id": "ka_supplier",
    "label_en": "Supplier Management",
    "label_zh": "供应商管理",
    "type": "process",
    "parent": "ka",
    "level": 2,
    "order": 2,
    "position": "第 2 列上块第 2 条"
  },
  {
    "id": "kr_brand",
    "label_en": "Brand Reputation",
    "label_zh": "品牌声誉",
    "type": "resource",
    "parent": "kr",
    "level": 2,
    "order": 1,
    "position": "第 2 列下块第 1 条"
  },
  {
    "id": "kr_realestate",
    "label_en": "Real Estate",
    "label_zh": "房地产",
    "type": "resource",
    "parent": "kr",
    "level": 2,
    "order": 2,
    "position": "第 2 列下块第 2 条"
  },
  {
    "id": "vp_low",
    "label_en": "Low Prices",
    "label_zh": "低价",
    "type": "concept",
    "parent": "vp",
    "level": 2,
    "order": 1,
    "position": "第 3 列第 1 条"
  },
  {
    "id": "vp_personal",
    "label_en": "Personal Touch",
    "label_zh": "个性化接触",
    "type": "concept",
    "parent": "vp",
    "level": 2,
    "order": 2,
    "position": "第 3 列第 2 条"
  },
  {
    "id": "vp_availability",
    "label_en": "Availability for Common and Regional Needs",
    "label_zh": "满足通用与区域需求的可获得性",
    "type": "concept",
    "parent": "vp",
    "level": 2,
    "order": 3,
    "position": "第 3 列第 3 条"
  },
  {
    "id": "cr_personal",
    "label_en": "Personal Assistance",
    "label_zh": "人工协助",
    "type": "service",
    "parent": "cr",
    "level": 2,
    "order": 1,
    "position": "第 4 列上块第 1 条"
  },
  {
    "id": "cr_warranty",
    "label_en": "Warranty Service",
    "label_zh": "保修服务",
    "type": "service",
    "parent": "cr",
    "level": 2,
    "order": 2,
    "position": "第 4 列上块第 2 条",
    "description_zh": "同一标签在收入来源块再次出现。"
  },
  {
    "id": "ch_shopfronts",
    "label_en": "Retail Shopfronts",
    "label_zh": "零售店面",
    "type": "other",
    "parent": "ch",
    "level": 2,
    "order": 1,
    "position": "第 4 列下块第 1 条",
    "description_zh": "实体渠道触点。"
  },
  {
    "id": "ch_web",
    "label_en": "Web-based Inventory Info",
    "label_zh": "基于网络的库存信息",
    "type": "other",
    "parent": "ch",
    "level": 2,
    "order": 2,
    "position": "第 4 列下块第 2 条",
    "description_zh": "线上信息渠道（只提供库存信息，不是在线交易）。"
  },
  {
    "id": "cs_mass",
    "label_en": "Mass Market",
    "label_zh": "大众市场",
    "type": "actor",
    "parent": "cs",
    "level": 2,
    "order": 1,
    "position": "第 5 列第 1 条"
  },
  {
    "id": "cs_regional",
    "label_en": "Regional Specialization",
    "label_zh": "区域专业化",
    "type": "actor",
    "parent": "cs",
    "level": 2,
    "order": 2,
    "position": "第 5 列第 2 条"
  },
  {
    "id": "cost_facilities",
    "label_en": "Facilities and Transport",
    "label_zh": "设施与运输",
    "type": "resource",
    "parent": "cost",
    "level": 2,
    "order": 1,
    "position": "底部左段第 1 条"
  },
  {
    "id": "cost_employees",
    "label_en": "Employees and Supply",
    "label_zh": "员工与供应",
    "type": "resource",
    "parent": "cost",
    "level": 2,
    "order": 2,
    "position": "底部左段第 2 条"
  },
  {
    "id": "cost_scale",
    "label_en": "Scale Across Nation",
    "label_zh": "全国规模扩张",
    "type": "resource",
    "parent": "cost",
    "level": 2,
    "order": 3,
    "position": "底部左段第 3 条"
  },
  {
    "id": "rev_profit",
    "label_en": "Profit on Sales",
    "label_zh": "销售利润",
    "type": "concept",
    "parent": "rev",
    "level": 2,
    "order": 1,
    "position": "底部右段第 1 条"
  },
  {
    "id": "rev_warranty",
    "label_en": "Warranty Service",
    "label_zh": "保修服务",
    "type": "concept",
    "parent": "rev",
    "level": 2,
    "order": 2,
    "position": "底部右段第 2 条",
    "description_zh": "与客户关系块的同名标签不同实例。"
  },
  {
    "id": "rev_rebates",
    "label_en": "Manufacture Rebates",
    "label_zh": "制造商返利",
    "type": "concept",
    "parent": "rev",
    "level": 2,
    "order": 3,
    "position": "底部右段第 3 条"
  }
]
```

## 关系

```json
[
  {
    "id": "r_vp_cs",
    "from": "vp",
    "to": "cs",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "版式隐含：价值主张列紧邻客户细分区，表示价值主张面向客户细分；图中无连线。"
  },
  {
    "id": "r_ch_cs",
    "from": "ch",
    "to": "cs",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "版式隐含：渠道位于客户细分左侧，表示触达客户的途径；图中无连线。"
  },
  {
    "id": "r_kp_ka",
    "from": "kp",
    "to": "ka",
    "type": "dependency",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "版式隐含：关键合作伙伴紧邻关键活动，表示伙伴支撑活动；图中无连线。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_canvas_current",
    "title_zh": "图 7-1 画布九块逐条转录（现状）",
    "columns": [
      "构建块",
      "条目 1",
      "条目 2",
      "条目 3"
    ],
    "rows": [
      [
        "Key Partners 关键合作伙伴",
        "Product Manufacturers 产品制造商",
        "National Suppliers 全国供应商",
        "Regional Suppliers 区域供应商"
      ],
      [
        "Key Activities 关键活动",
        "Customer Analysis 客户分析",
        "Supplier Management 供应商管理",
        "—"
      ],
      [
        "Key Resources 关键资源",
        "Brand Reputation 品牌声誉",
        "Real Estate 房地产",
        "—"
      ],
      [
        "Value Propositions 价值主张",
        "Low Prices 低价",
        "Personal Touch 个性化接触",
        "Availability for Common and Regional Needs 满足通用与区域需求的可获得性"
      ],
      [
        "Customer Relationships 客户关系",
        "Personal Assistance 人工协助",
        "Warranty Service 保修服务",
        "—"
      ],
      [
        "Channels 渠道",
        "Retail Shopfronts 零售店面",
        "Web-based Inventory Info 基于网络的库存信息",
        "—"
      ],
      [
        "Customer Segments 客户细分",
        "Mass Market 大众市场",
        "Regional Specialization 区域专业化",
        "—"
      ],
      [
        "Cost Structure 成本结构",
        "Facilities and Transport 设施与运输",
        "Employees and Supply 员工与供应",
        "Scale Across Nation 全国规模扩张"
      ],
      [
        "Revenue Streams 收入来源",
        "Profit on Sales 销售利润",
        "Warranty Service 保修服务",
        "Manufacture Rebates 制造商返利"
      ]
    ],
    "notes_zh": "按原图块内自上而下顺序转录；「—」表示该块只有两条条目。Warranty Service 在两个块中各出现一次。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "块名 + 小图标（链环、勾、礼盒、心、人、工厂、卡车、价签、钱袋）",
    "meaning_zh": "九个构建块的名称与视觉标识",
    "explicit": false
  },
  {
    "symbol": "黄色圆角条目框",
    "meaning_zh": "该构建块下的具体条目",
    "explicit": false
  },
  {
    "symbol": "左侧三块 + 底部左段",
    "meaning_zh": "成本/资源侧（伙伴、活动、资源、成本）",
    "explicit": false
  },
  {
    "symbol": "右侧三块 + 底部右段",
    "meaning_zh": "客户/收入侧（关系、渠道、客户、收入）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "外框内上部五列：第 1 列 Key Partners；第 2 列上 Key Activities、下 Key Resources；第 3 列 Value Propositions（通高）；第 4 列上 Customer Relationships、下 Channels；第 5 列 Customer Segments（通高）。底部横条分左右：Cost Structure 与 Revenue Streams。标题条位于外框上方居中。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig7-2",
    "relation": "precedes",
    "note_zh": "图 7-1 是现状基线，图 7-2 是在同一画布上改动后的未来态，两者逐块对照"
  },
  {
    "target": "G18A/figA-1",
    "relation": "instance_of",
    "note_zh": "图 7-1 是附录 A 所定义九块画布在零售企业中的实例"
  },
  {
    "target": "G18A/fig2-4",
    "relation": "instance_of",
    "note_zh": "图 7-1 使用图 2-4 所示的业务模型画布形式"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "块内条目自上而下的顺序是否表示优先级，原图未说明。",
    "“Regional Specialization”作为客户细分条目的确切含义（区域专营客户还是区域化需求）图中未解释。",
    "“Warranty Service”在客户关系与收入来源两块均出现，是否为同一业务的不同侧面，图中未标注。"
  ],
  "analyzed_from": [
    "英文 PDF 第 24 页原图截图（fig7-1_p24_1.png）及 3×3 放大分块",
    "英文 PDF 第 24 页正文",
    "中文稿 G18Ae_业务模型.md 第 206–250 行（含图内标签对照表）",
    "figs/g18ae_fig7-1_en.png 与 figs/zh/g18ae_fig7-1_zh.png"
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
