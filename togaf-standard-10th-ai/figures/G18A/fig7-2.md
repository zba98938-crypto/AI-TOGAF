# G18A/fig7-2 · 零售商业务模型画布——未来态

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/fig7-2.md) · [JSON](../../architecture/diagrams/G18A/fig7-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 25 页

![英文原图](../assets/G18A/fig7-2-p0025.png)

PDF 坐标：`[48.2, 324.5, 563.8, 653.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Retailer Business Model Diagram — Future State
Key Partners
?
Key Activities
G
Value Propositions
a
=
Customer Relationships @
Customer Segments
2
Product
Customer
Lowest
Automated
Mass
Manufacturers
Analysis
Prices
Al Services
Market
Supplier
Convenience
Web Shopping
Consumer-
Global Suppliers
Management
Anywhere
Self-service
specific
Specialization
Key Resources
Channels
san
ms
Internet and App
Availability for
Providers
Brand
Common and
Limited
Specific Needs
Reputation
Shopfronts
Cloud Hosting &
Web-based
App Support
Shopping Apps
Cost Structure
Revenue Streams
Infrastructure & Transport
Profit on Sales
Employees and Supply
Warranty Service
Scale Across Globe
Manufacture Rebates
```

## 概要（历史解释；局部修正见上）

在同一张业务模型画布上给出零售企业的未来态：客户与价值主张右移数字化，成本与伙伴随之重构。

## 目的（历史解释；局部修正见上）

展示业务模型如何因市场压力、销售下滑或成本上升而改变；通过与图 7-1 逐块对照，说明真正的新业务模型来自客户细分与价值主张的联合转变，并引出价值流与能力差距分析。

## 阅读顺序（历史解释；局部修正见上）

先按与图 7-1 相同的布局定位九块，再逐块对照现状图找差异：右上 Customer Segments 由 Regional Specialization 变为 Consumer-specific Specialization；Value Propositions 由 Low Prices 变为 Lowest Prices 并新增 Convenience Anywhere；Channels 与 Customer Relationships 改为线上/自动化；Key Resources、Key Partners、Cost Structure 随之更换；Key Activities 与 Revenue Streams 不变。同样可按正文建议从右向左读。

## 关键含义（历史解释；局部修正见上）

- 客户细分：Mass Market 保留，Regional Specialization 改为 Consumer-specific Specialization，从区域专业化转向面向特定消费者。
- 价值主张：Low Prices 改为 Lowest Prices，新增 Convenience Anywhere，第三条由 Regional 改为 Specific，整体转向“更低价格 + 随处便利 + 特定需求”。
- 渠道：Retail Shopfronts 改为 Limited Shopfronts，Web-based Inventory Info 改为 Web-based Shopping Apps，从“实体为主 + 线上查信息”转为“有限店面 + 线上购物”。
- 客户关系：Personal Assistance、Warranty Service 改为 Automated AI Services、Web Shopping Self-service，服务方式自动化、自助化。
- 关键资源：保留 Brand Reputation，Real Estate 换成 Cloud Hosting & App Support；成本侧 Facilities and Transport 换成 Infrastructure & Transport，Scale Across Nation 换成 Scale Across Globe。
- 关键合作伙伴：National/Regional Suppliers 换成 Global Suppliers，并新增 Internet and App Providers，供应链全球化且引入数字伙伴。
- Key Activities（Customer Analysis、Supplier Management）与 Revenue Streams（Profit on Sales、Warranty Service、Manufacture Rebates）完全不变，对应正文“部分区域不变”。
- 收入侧（右）与成本侧（左）同时变化，符合正文“真正的新业务模型来自客户细分与价值主张的联合转变”。

## 层级（历史解释；局部修正见上）

两层：画布整体（带标题的矩形框）下分九个构建块，每块下为 2–3 个条目。九个块并列；底部成本结构与收入来源各占一半宽度。

## 线条含义（历史解释；局部修正见上）

图中没有箭头或连线，只有分隔块用的直线。块内条目为并列清单；未来态与现状的差异不靠颜色或标记表示，只能通过与图 7-1 逐条比对得出。

## 易误读点（历史解释；局部修正见上）

- 不要把未来态理解为九块全部重写：关键活动与收入来源与现状完全相同。
- 不要忽略 Mass Market 仍然保留：未来态仍是“大众市场 + 特定消费者”的双重定位。
- 图中没有任何“变化标记”（箭头、颜色、删除线），差异必须对照图 7-1 才能看出。
- 不要以为 Warranty Service 只属于客户关系：它在收入来源中仍保留。
- 中文稿正文第 255 行的块顺序（先客户细分后价值主张）与画布从左到右的布局不同，只是叙述顺序，不影响内容。

## 元素

```json
[
  {
    "id": "canvas",
    "label_en": "Retailer Business Model Diagram – Future State",
    "label_zh": "零售商业务模型图——未来态",
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
    "id": "kp_global",
    "label_en": "Global Suppliers",
    "label_zh": "全球供应商",
    "type": "actor",
    "parent": "kp",
    "level": 2,
    "order": 2,
    "position": "第 1 列第 2 条"
  },
  {
    "id": "kp_internet",
    "label_en": "Internet and App Providers",
    "label_zh": "互联网与应用提供商",
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
    "id": "kr_cloud",
    "label_en": "Cloud Hosting & App Support",
    "label_zh": "云托管与应用支持",
    "type": "resource",
    "parent": "kr",
    "level": 2,
    "order": 2,
    "position": "第 2 列下块第 2 条"
  },
  {
    "id": "vp_lowest",
    "label_en": "Lowest Prices",
    "label_zh": "最低价格",
    "type": "concept",
    "parent": "vp",
    "level": 2,
    "order": 1,
    "position": "第 3 列第 1 条"
  },
  {
    "id": "vp_convenience",
    "label_en": "Convenience Anywhere",
    "label_zh": "随处便利",
    "type": "concept",
    "parent": "vp",
    "level": 2,
    "order": 2,
    "position": "第 3 列第 2 条"
  },
  {
    "id": "vp_availability",
    "label_en": "Availability for Common and Specific Needs",
    "label_zh": "满足通用与特定需求的可获得性",
    "type": "concept",
    "parent": "vp",
    "level": 2,
    "order": 3,
    "position": "第 3 列第 3 条"
  },
  {
    "id": "cr_ai",
    "label_en": "Automated AI Services",
    "label_zh": "自动化 AI 服务",
    "type": "service",
    "parent": "cr",
    "level": 2,
    "order": 1,
    "position": "第 4 列上块第 1 条"
  },
  {
    "id": "cr_selfservice",
    "label_en": "Web Shopping Self-service",
    "label_zh": "网络购物自助服务",
    "type": "service",
    "parent": "cr",
    "level": 2,
    "order": 2,
    "position": "第 4 列上块第 2 条"
  },
  {
    "id": "ch_limited",
    "label_en": "Limited Shopfronts",
    "label_zh": "有限店面",
    "type": "other",
    "parent": "ch",
    "level": 2,
    "order": 1,
    "position": "第 4 列下块第 1 条",
    "description_zh": "缩减后的实体渠道。"
  },
  {
    "id": "ch_apps",
    "label_en": "Web-based Shopping Apps",
    "label_zh": "基于网络的购物应用",
    "type": "other",
    "parent": "ch",
    "level": 2,
    "order": 2,
    "position": "第 4 列下块第 2 条",
    "description_zh": "线上购物渠道。"
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
    "id": "cs_consumer",
    "label_en": "Consumer-specific Specialization",
    "label_zh": "面向特定消费者的专业化",
    "type": "actor",
    "parent": "cs",
    "level": 2,
    "order": 2,
    "position": "第 5 列第 2 条"
  },
  {
    "id": "cost_infra",
    "label_en": "Infrastructure & Transport",
    "label_zh": "基础设施与运输",
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
    "id": "cost_global",
    "label_en": "Scale Across Globe",
    "label_zh": "全球规模扩张",
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
    "position": "底部右段第 2 条"
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
    "id": "t_canvas_future",
    "title_zh": "图 7-2 画布九块逐条转录（未来态）",
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
        "Global Suppliers 全球供应商",
        "Internet and App Providers 互联网与应用提供商"
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
        "Cloud Hosting & App Support 云托管与应用支持",
        "—"
      ],
      [
        "Value Propositions 价值主张",
        "Lowest Prices 最低价格",
        "Convenience Anywhere 随处便利",
        "Availability for Common and Specific Needs 满足通用与特定需求的可获得性"
      ],
      [
        "Customer Relationships 客户关系",
        "Automated AI Services 自动化 AI 服务",
        "Web Shopping Self-service 网络购物自助服务",
        "—"
      ],
      [
        "Channels 渠道",
        "Limited Shopfronts 有限店面",
        "Web-based Shopping Apps 基于网络的购物应用",
        "—"
      ],
      [
        "Customer Segments 客户细分",
        "Mass Market 大众市场",
        "Consumer-specific Specialization 面向特定消费者的专业化",
        "—"
      ],
      [
        "Cost Structure 成本结构",
        "Infrastructure & Transport 基础设施与运输",
        "Employees and Supply 员工与供应",
        "Scale Across Globe 全球规模扩张"
      ],
      [
        "Revenue Streams 收入来源",
        "Profit on Sales 销售利润",
        "Warranty Service 保修服务",
        "Manufacture Rebates 制造商返利"
      ]
    ],
    "notes_zh": "按原图块内自上而下顺序转录；「—」表示该块只有两条条目。"
  },
  {
    "id": "t_current_vs_future",
    "title_zh": "现状（图 7-1）与未来态（图 7-2）逐块差异",
    "columns": [
      "构建块",
      "现状",
      "未来态",
      "变化性质"
    ],
    "rows": [
      [
        "Customer Segments",
        "Mass Market；Regional Specialization",
        "Mass Market；Consumer-specific Specialization",
        "区域专业化 → 面向特定消费者的专业化"
      ],
      [
        "Value Propositions",
        "Low Prices；Personal Touch；Availability for Common and Regional Needs",
        "Lowest Prices；Convenience Anywhere；Availability for Common and Specific Needs",
        "价格更低、新增随处便利、区域→特定"
      ],
      [
        "Channels",
        "Retail Shopfronts；Web-based Inventory Info",
        "Limited Shopfronts；Web-based Shopping Apps",
        "实体收缩、线上从信息转为购物"
      ],
      [
        "Customer Relationships",
        "Personal Assistance；Warranty Service",
        "Automated AI Services；Web Shopping Self-service",
        "人工/保修 → 自动化/自助"
      ],
      [
        "Key Resources",
        "Brand Reputation；Real Estate",
        "Brand Reputation；Cloud Hosting & App Support",
        "地产 → 云与应用支持"
      ],
      [
        "Key Partners",
        "Product Manufacturers；National Suppliers；Regional Suppliers",
        "Product Manufacturers；Global Suppliers；Internet and App Providers",
        "全国/区域 → 全球 + 数字伙伴"
      ],
      [
        "Cost Structure",
        "Facilities and Transport；Employees and Supply；Scale Across Nation",
        "Infrastructure & Transport；Employees and Supply；Scale Across Globe",
        "设施 → 基础设施；全国 → 全球"
      ],
      [
        "Key Activities",
        "Customer Analysis；Supplier Management",
        "Customer Analysis；Supplier Management",
        "不变"
      ],
      [
        "Revenue Streams",
        "Profit on Sales；Warranty Service；Manufacture Rebates",
        "Profit on Sales；Warranty Service；Manufacture Rebates",
        "不变"
      ]
    ],
    "notes_zh": "差异为逐条对照两图得出；原图本身不含差异标记。"
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
    "meaning_zh": "成本/资源侧",
    "explicit": false
  },
  {
    "symbol": "右侧三块 + 底部右段",
    "meaning_zh": "客户/收入侧",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "与图 7-1 完全相同的版式：外框内上部五列（Key Partners｜Key Activities/Key Resources｜Value Propositions｜Customer Relationships/Channels｜Customer Segments），底部 Cost Structure 与 Revenue Streams 左右并列；标题条在外框上方。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig7-1",
    "relation": "follows",
    "note_zh": "图 7-2 是图 7-1 现状基线的未来态版本，逐块对照可见变化与不变项"
  },
  {
    "target": "G18A/figA-1",
    "relation": "instance_of",
    "note_zh": "未来态仍是附录 A 所定义九块画布的一个实例"
  },
  {
    "target": "G18A/fig2-4",
    "relation": "instance_of",
    "note_zh": "使用图 2-4 所示的业务模型画布形式"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "块内条目自上而下的顺序是否表示优先级，原图未说明。",
    "“Consumer-specific Specialization”与现状的“Regional Specialization”是否为同一维度的替换，图中只能从事务所对照推断。",
    "原图没有标注哪些块是新增、删除或修改，差异表为解析者逐条比对的结果。"
  ],
  "analyzed_from": [
    "英文 PDF 第 25 页原图截图（fig7-2_p25_1.png）及 3×3 放大分块",
    "英文 PDF 第 25 页正文",
    "中文稿 G18Ae_业务模型.md 第 251–296 行（含图内标签对照表）",
    "figs/g18ae_fig7-2_en.png 与 figs/zh/g18ae_fig7-2_zh.png"
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
