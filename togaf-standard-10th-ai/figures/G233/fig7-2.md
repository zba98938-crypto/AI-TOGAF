# G233/fig7-2 · 新增激励管理应用

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig7-2.md) · [JSON](../../architecture/diagrams/G233/fig7-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 44 页

![英文原图](../assets/G233/fig7-2-p0044.png)

PDF 坐标：`[74.0, 160.7, 538.0, 455.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Incentive Management
Legacy Warehouse
Delivery Management uf]
Management
CRM Application
Application
fac}
Store Promotion
Retire Application J)
Delivery Driver
Confirm Package Delivery >
Modern Warehouse
Management
I
Application
New API Call
Shipping Company Tracking
‘Application
‘Add Legacy
Ss
Warehouse
Onli
Store
Application
Notify customer of
Inventory
shipping progress
Store Promotion
a
i
'
1
‘Signature Pad
Online Store
Ss
Incentive
Signature Pad &
Management
application
Integration with
enhancement
CRM
```

## 概要（历史解释；局部修正见上）

把优化、整合、新建、退役四种能力增量落到模型上：新增激励实例、整合仓库应用、退役遗留应用、用签名板改进交付。

## 目的（历史解释；局部修正见上）

第 7.2 节要说明“能力增量如何被规划”：差距用 ArchiMate gap 元素表示，同一差距分配给多个能力表示可分组；平台期（plateau）是一组能保持价值流功能完整的增强。图 7-2 把 7.1 节的四种情景具体化为可执行的差距与依赖，是第 7 章从分析走向实施的落点。

## 阅读顺序（历史解释；局部修正见上）

从左到右三组：左边 Incentive Management 能力实例（CRM Application 与 Online Store 各有一个 Store Promotion 数据对象，中间一条“New API Call”箭头）；中间是 Legacy 与 Modern 两个仓库管理应用，分别挂着“Retire Application”事件与“Add Legacy Warehouse Application Inventory”差距；右边 Delivery Management 能力实例（客户、配送司机、确认送达、运输公司跟踪应用），下方一个绿色“Signature Pad”交付物（内含应用增强差距），用虚线箭头指向运输应用。绿色波浪底框是差距，绿色胶囊＋底座是交付物。

## 关键含义（历史解释；局部修正见上）

- 新建（Create）：Incentive Management 新增一个实例，通过“New API Call”让 Online Store 的 Store Promotion 数据与 CRM Application 的 Store Promotion 同步，从而向网站访客展示通用/个性化激励。
- 整合（Consolidate）：Modern Warehouse Management Application 内有一个差距“Add Legacy Warehouse Application Inventory”，即把电子产品仓库库存并入现代仓库应用；完成后 Legacy 实例即可退役。
- 退役（Retire）：Legacy Warehouse Management Application 内放的是粉色业务事件“Retire Application”，而不是差距——正文说明该应用不存在真正的差距，用事件标记退役。
- 优化（Optimize）：Delivery Management 实例下的“Signature Pad”交付物内含“Signature Pad application enhancement”差距，并用虚线箭头指向 Shipping Company Tracking Application，表示签名数据回传运输应用。
- 差距（gap）用绿色波浪底文档形＋Gap 图标表示；正文说同一 gap 分配给多个能力表示这些能力可能属于同一分组、可一起处理（同一平台期）。
- Delivery Management 实例包含 Customer、Delivery Driver（角色）、Confirm Package Delivery（流程）与运输公司跟踪应用，说明“优化”不是换应用，而是给现有实例加一个资源/应用增强。
- 图中没有画出平台期（plateau）边界；平台期是正文概念，指为解决一组差距而共同实施、能保持价值流功能完整的增强集合。
- 本例的差距彼此独立，唯一例外是退役：Legacy 应用被多个价值流使用，退役前必须确认这些价值流不受影响。

## 层级（历史解释；局部修正见上）

三组并列：Incentive Management、仓库应用组（Legacy/Modern）、Delivery Management。能力框内嵌应用组件；应用组件内嵌数据对象、事件或差距；Signature Pad 交付物内嵌一个应用增强差距（交付物→差距两层）。

## 线条含义（历史解释；局部修正见上）

实线开口箭头“New API Call”：由 Online Store 指向上方 CRM Application，表示新增的接口调用。虚线实心箭头（无标签）：由 Signature Pad 交付物指向 Shipping Company Tracking Application，表示签名回传。除此之外没有连线，归属由嵌套表达。

## 易误读点（历史解释；局部修正见上）

- 不要把粉色“Retire Application”当成差距；它是业务事件，表示退役这一状态变化。
- 不要把两个“Store Promotion”当成同一个数据对象；一个在 CRM 应用内，一个在 Online Store 内，靠新增 API 同步。
- 不要把绿色波浪底框当成文档/交付物；它们是 ArchiMate gap 元素，表示需要弥合的差距。
- 不要把“Signature Pad”外层当成 gap：外层是带底座的交付物/资源容器，没有 Gap 图标；内层“Signature Pad application enhancement”才是应用增强差距。
- 不要以为 Legacy/Modern 仓库应用属于某个能力框；它们直接画在价值流层面，是跨能力使用的应用组件。
- 中文稿 PNG 下方中央有巨大的“客户关系管理应用”白块（左右另有白块）覆盖模型文字，不能据其判断元素归属；必须看英文原图。

## 元素

```json
[
  {
    "id": "cap_incentive",
    "label_en": "Incentive Management",
    "label_zh": "激励管理",
    "type": "capability",
    "parent": null,
    "position": "左列（沙色能力框）"
  },
  {
    "id": "app_crm",
    "label_en": "CRM Application",
    "label_zh": "客户关系管理应用",
    "type": "application",
    "parent": "cap_incentive",
    "order": 1
  },
  {
    "id": "obj_promo_crm",
    "label_en": "Store Promotion",
    "label_zh": "门店促销",
    "type": "data",
    "parent": "app_crm",
    "description_zh": "CRM 数据对象"
  },
  {
    "id": "app_online_store",
    "label_en": "Online Store",
    "label_zh": "在线商店",
    "type": "application",
    "parent": "cap_incentive",
    "order": 2
  },
  {
    "id": "obj_promo_os",
    "label_en": "Store Promotion",
    "label_zh": "门店促销",
    "type": "data",
    "parent": "app_online_store",
    "description_zh": "在线商店数据对象"
  },
  {
    "id": "gap_integration",
    "label_en": "Online Store Incentive Management Integration with CRM",
    "label_zh": "在线商店激励管理与 CRM 集成",
    "type": "requirement",
    "parent": "cap_incentive",
    "position": "左列底部（绿色差距框）",
    "description_zh": "ArchiMate gap 元素，波浪底文档形。"
  },
  {
    "id": "app_legacy",
    "label_en": "Legacy Warehouse Management Application",
    "label_zh": "遗留仓库管理应用",
    "type": "application",
    "parent": null,
    "position": "中列上方"
  },
  {
    "id": "event_retire",
    "label_en": "Retire Application",
    "label_zh": "退役应用",
    "type": "event",
    "parent": "app_legacy",
    "position": "遗留应用框内（粉色）"
  },
  {
    "id": "app_modern",
    "label_en": "Modern Warehouse Management Application",
    "label_zh": "现代仓库管理应用",
    "type": "application",
    "parent": null,
    "position": "中列下方"
  },
  {
    "id": "gap_add_inventory",
    "label_en": "Add Legacy Warehouse Application Inventory",
    "label_zh": "增加遗留仓库应用库存",
    "type": "requirement",
    "parent": "app_modern",
    "position": "现代应用框内（绿色差距框）"
  },
  {
    "id": "cap_delivery",
    "label_en": "Delivery Management",
    "label_zh": "交付管理",
    "type": "capability",
    "parent": null,
    "position": "右列（沙色能力框）"
  },
  {
    "id": "st_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "stakeholder",
    "parent": "cap_delivery",
    "order": 1
  },
  {
    "id": "role_delivery_driver",
    "label_en": "Delivery Driver",
    "label_zh": "配送司机",
    "type": "role",
    "parent": "cap_delivery",
    "order": 2
  },
  {
    "id": "proc_confirm_package",
    "label_en": "Confirm Package Delivery",
    "label_zh": "确认包裹送达",
    "type": "process",
    "parent": "cap_delivery",
    "order": 3
  },
  {
    "id": "app_shipping",
    "label_en": "Shipping Company Tracking Application",
    "label_zh": "运输公司跟踪应用",
    "type": "application",
    "parent": "cap_delivery",
    "order": 4
  },
  {
    "id": "ap_notify_progress",
    "label_en": "Notify customer of shipping progress",
    "label_zh": "通知客户运输进度",
    "type": "process",
    "parent": "app_shipping"
  },
  {
    "id": "art_signature_pad",
    "label_en": "Signature Pad",
    "label_zh": "签名板",
    "type": "artifact",
    "parent": "cap_delivery",
    "position": "右列底部（绿色交付物框，带底座）",
    "description_zh": "绿色胶囊＋底座的交付物/资源容器（与图 C-1 的 Building Pass Card 同形，无 Gap 图标），内嵌应用增强差距；确切 ArchiMate 类型不确定"
  },
  {
    "id": "gap_signature_enh",
    "label_en": "Signature Pad application enhancement",
    "label_zh": "签名板应用增强",
    "type": "requirement",
    "parent": "art_signature_pad",
    "position": "Signature Pad 交付物内"
  }
]
```

## 关系

```json
[
  {
    "from": "app_online_store",
    "to": "app_crm",
    "type": "flow",
    "label_en": "New API Call",
    "label_zh": "新增 API 调用",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "实线开口箭头由 Online Store 指向 CRM Application。"
  },
  {
    "from": "art_signature_pad",
    "to": "app_shipping",
    "type": "flow",
    "label_en": null,
    "label_zh": null,
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "虚线实心箭头由 Signature Pad 指向上方运输公司跟踪应用，表示签名回传。"
  },
  {
    "from": "gap_integration",
    "to": "app_online_store",
    "type": "dependency",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "集成差距位于该能力实例内，依赖在线商店侧的接口改造。"
  },
  {
    "from": "gap_add_inventory",
    "to": "app_modern",
    "type": "dependency",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "库存整合差距需在现代仓库应用中实现。"
  },
  {
    "from": "gap_signature_enh",
    "to": "app_shipping",
    "type": "dependency",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "应用增强差距使签名能够回传运输应用。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_signature",
    "kind": "sequence",
    "name_zh": "签名回传序列",
    "steps": [
      "art_signature_pad",
      "app_shipping"
    ],
    "description_zh": "配送司机在签名板签字后，签名回传运输公司跟踪应用。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "沙色大框 + 能力图标",
    "meaning_zh": "业务能力实例",
    "explicit": false
  },
  {
    "symbol": "青色框 + 左侧双页签",
    "meaning_zh": "应用组件",
    "explicit": false
  },
  {
    "symbol": "黄色矩形（应用内）",
    "meaning_zh": "数据对象（Store Promotion）",
    "explicit": false
  },
  {
    "symbol": "粉色圆角框 + 事件图标",
    "meaning_zh": "业务事件（Retire Application）",
    "explicit": false
  },
  {
    "symbol": "绿色波浪底框 + Gap 图标",
    "meaning_zh": "差距（ArchiMate gap）",
    "explicit": false
  },
  {
    "symbol": "绿色胶囊 + 底座（Signature Pad）",
    "meaning_zh": "交付物/资源容器（内嵌差距；无 Gap 图标）",
    "explicit": false
  },
  {
    "symbol": "紫色六边形（Customer）/黄色矩形（Delivery Driver）",
    "meaning_zh": "利益相关者 / 业务角色",
    "explicit": false
  },
  {
    "symbol": "实线开口箭头",
    "meaning_zh": "新增 API 调用",
    "explicit": true
  },
  {
    "symbol": "虚线实心箭头",
    "meaning_zh": "签名数据回传运输应用",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "三列：左列 Incentive Management（CRM 在上、Online Store 在下，二者之间一条向上箭头）；中列上下两个独立应用框（Legacy、Modern）；右列 Delivery Management（客户、司机、流程、运输应用，底部为 Signature Pad 交付物，内嵌应用增强差距）。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig7-1",
    "relation": "follows",
    "note_zh": "图 7-1 用 New/Retired/Improved 标出三处变化；本图把它们落成具体的差距、事件与接口"
  },
  {
    "target": "G233/fig6-3",
    "relation": "detail_of",
    "note_zh": "本图的 Incentive Management、Delivery Management、Legacy/Modern 仓库应用都来自图 6-3 的能力实例，只增加了差距与变更"
  },
  {
    "target": "G233/fig6-1",
    "relation": "related",
    "note_zh": "Incentive Management、Delivery Management、Inventory Management 均为图 6-1 目录中的能力，本图展示它们的新增/整合/退役实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "“Signature Pad”外层为绿色胶囊＋底座、无 Gap 图标，与图 C-1 的 Building Pass Card 同形，本文按交付物/资源容器（artifact）记录；内层“Signature Pad application enhancement”才是 gap。确切 ArchiMate 类型无法仅凭图形确认。",
    "“New API Call”箭头只有开口箭头、无标签框，方向由箭头指向 CRM 判断。",
    "图中未标出 plateau 边界，平台期只能依据正文概念理解。"
  ],
  "analyzed_from": [
    "英文 PDF 第 44 页图 7-2 截图（500 dpi）与 700 dpi 左右分栏",
    "英文 PDF 第 43–44 页正文",
    "中文稿 G233e_业务能力规划.md 第 737–779 行（含标签对照表）",
    "figs/zh/g233e_fig7-2_zh.png"
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
