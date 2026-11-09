# G21B/fig1-1 · 组织能力的通用描述

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig1-1.md) · [JSON](../../architecture/diagrams/G21B/fig1-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 12 页

![英文原图](../assets/G21B/fig1-1-p0012.png)

PDF 坐标：`[74.0, 143.3, 538.0, 537.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
External Data Provider Capabilities
a) (
External Partner Capabilities
|
y X
Engagement
Prospect & Customer Digital Access
a
Partner Digital Access
Customer Relationship Management
fl
Marketing
Core Business Primary Activities Supporting the Value Chain
Inbound Logistics 4
Operations
fe
Outbound
a
Logistics
Data Management Support
Ee
Business Support
F
Human
Metadata ff
BI & Analytics #f]
Ee
Finance & ff
Communication & cf
Management
Resources
Procurement
Content
Management
Master Data ff
Integration & ff
Security ff
Workplace ff
IT Management ff
Management
Interoperability
Infrastructure
a
Legend
Internal
dH) Capabilities provided by the IT department of the organization considered.
Capability
eB External digital capabilities with which the organization has to interact.
```

## 概要（历史解释；局部修正见上）

把组织的信息系统能力按价值链分为核心业务、互动、数据管理支撑、业务支撑四个内部区域，外加两类外部能力。

## 目的（历史解释；局部修正见上）

为第 1.2 节“数据管理能力”建立全景：先说明企业价值链上的主活动与支撑活动如何被信息系统能力覆盖，再把“数据管理支撑”（元数据、BI 与分析、主数据管理、集成与互操作）定位为跨业务共享的能力底座，从而引出 C-MDM 所属的主数据管理。

## 阅读顺序（历史解释；局部修正见上）

从上到下读：最上方两个灰色框是组织要对接的外部能力；其下是蓝色“互动”区（面向客户/伙伴的数字接触点）；再下是“核心业务主活动”区（价值链主活动，收入在此产生）；最下方并列“数据管理支撑”和“业务支撑”两个内部支撑区。大框内的小框是该能力区包含的具体能力，框的大小和位置不表示优先级。阅读时把“数据管理支撑”当作与业务支撑并列、但横向服务于所有业务线的能力层。

## 关键含义（历史解释；局部修正见上）

- 图把能力分为六类：4 个内部能力区（核心业务主活动、互动、数据管理支撑、业务支撑）+ 2 个外部能力（外部数据提供方、外部伙伴）。
- 核心业务主活动沿价值链展开：入站物流（如接单）—运营（如处理订单）—出站物流（如交付订单），是企业收入产生的地方。
- 互动区承载与客户、业务用户、伙伴的数字交互，包含潜在客户与客户的数字访问、伙伴数字访问、CRM 与营销。
- 数据管理支撑只有四项：元数据管理、BI 与分析、主数据管理、集成与互操作；正文强调它们是各业务共享的常见数据管理能力，是“无边界信息流”的基础。
- 业务支撑包含人力资源、财务与采购、沟通与内容管理、安全、工作场所、IT 管理与基础设施；基础设施横贯业务支撑区底部。
- C-MDM 位于“数据管理支撑”的主数据管理之内，聚焦客户数据；图本身不画 C-MDM，只给出它的能力归属。
- 外部数据提供方与外部伙伴是组织必须交互的外部数字能力，不属于组织内部能力（图例用灰色区分）。

## 层级（历史解释；局部修正见上）

两层：第 1 层是 6 个能力区域（4 个内部 + 2 个外部）；第 2 层是区域内的具体能力（互动 4 项、核心业务 3 项、数据管理支撑 4 项、业务支撑 6 项 + 基础设施）。第 1 层与第 2 层为包含关系，不是上下级汇报关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连接线或箭头。能力之间的从属关系完全由“小框是否位于大框内”表达；外部能力与内部能力只用颜色和图例区分，二者之间没有画交互线。

## 易误读点（历史解释；局部修正见上）

- 不要把“数据管理支撑”理解为与核心业务无关的 IT 后台：正文把它定位为跨业务共享、支撑无边界信息流的能力底座。
- 图中没有“治理”能力区，也没有把“技术支撑”单列；基础设施在“业务支撑”内。
- 六个能力区不是一条流程链，区域之间没有先后顺序；只有核心业务区内部沿价值链有入站—运营—出站的顺序含义。
- 中文稿当前引用的 figs/g21b_fig1-1.svg 是自拟的六框链条图，漏掉外部能力和全部子能力，不能据此理解原图。

## 元素

```json
[
  {
    "id": "ext_data_provider",
    "label_en": "External Data Provider Capabilities",
    "label_zh": "外部数据提供方能力",
    "type": "capability",
    "parent": null,
    "level": 1,
    "position": "顶部一行"
  },
  {
    "id": "ext_partner",
    "label_en": "External Partner Capabilities",
    "label_zh": "外部伙伴能力",
    "type": "capability",
    "parent": null,
    "level": 1,
    "position": "顶部一行"
  },
  {
    "id": "g_engagement",
    "label_en": "Engagement",
    "label_zh": "互动",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "蓝色大框，内含 4 个能力。"
  },
  {
    "id": "eng_prospect_access",
    "label_en": "Prospect & Customer Digital Access",
    "label_zh": "潜在客户与客户数字访问",
    "type": "capability",
    "parent": "g_engagement",
    "level": 2
  },
  {
    "id": "eng_partner_access",
    "label_en": "Partner Digital Access",
    "label_zh": "伙伴数字访问",
    "type": "capability",
    "parent": "g_engagement",
    "level": 2
  },
  {
    "id": "eng_crm",
    "label_en": "Customer Relationship Management",
    "label_zh": "客户关系管理",
    "type": "capability",
    "parent": "g_engagement",
    "level": 2
  },
  {
    "id": "eng_marketing",
    "label_en": "Marketing",
    "label_zh": "营销",
    "type": "capability",
    "parent": "g_engagement",
    "level": 2
  },
  {
    "id": "g_core",
    "label_en": "Core Business Primary Activities Supporting the Value Chain",
    "label_zh": "支撑价值链的核心业务主活动",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "core_inbound",
    "label_en": "Inbound Logistics",
    "label_zh": "入站物流",
    "type": "capability",
    "parent": "g_core",
    "level": 2,
    "order": 1
  },
  {
    "id": "core_operations",
    "label_en": "Operations",
    "label_zh": "运营",
    "type": "capability",
    "parent": "g_core",
    "level": 2,
    "order": 2
  },
  {
    "id": "core_outbound",
    "label_en": "Outbound Logistics",
    "label_zh": "出站物流",
    "type": "capability",
    "parent": "g_core",
    "level": 2,
    "order": 3
  },
  {
    "id": "g_data_support",
    "label_en": "Data Management Support",
    "label_zh": "数据管理支撑",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "dm_metadata",
    "label_en": "Metadata Management",
    "label_zh": "元数据管理",
    "type": "capability",
    "parent": "g_data_support",
    "level": 2
  },
  {
    "id": "dm_bi",
    "label_en": "BI & Analytics",
    "label_zh": "BI 与分析",
    "type": "capability",
    "parent": "g_data_support",
    "level": 2
  },
  {
    "id": "dm_mdm",
    "label_en": "Master Data Management",
    "label_zh": "主数据管理",
    "type": "capability",
    "parent": "g_data_support",
    "level": 2,
    "description_zh": "C-MDM 所属的能力。"
  },
  {
    "id": "dm_integration",
    "label_en": "Integration & Interoperability",
    "label_zh": "集成与互操作",
    "type": "capability",
    "parent": "g_data_support",
    "level": 2
  },
  {
    "id": "g_business_support",
    "label_en": "Business Support",
    "label_zh": "业务支撑",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "bs_hr",
    "label_en": "Human Resources",
    "label_zh": "人力资源",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2
  },
  {
    "id": "bs_finance",
    "label_en": "Finance & Procurement",
    "label_zh": "财务与采购",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2
  },
  {
    "id": "bs_comms",
    "label_en": "Communication & Content Management",
    "label_zh": "沟通与内容管理",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2
  },
  {
    "id": "bs_security",
    "label_en": "Security",
    "label_zh": "安全",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2
  },
  {
    "id": "bs_workplace",
    "label_en": "Workplace",
    "label_zh": "工作场所",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2
  },
  {
    "id": "bs_it",
    "label_en": "IT Management",
    "label_zh": "IT 管理",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2
  },
  {
    "id": "bs_infrastructure",
    "label_en": "Infrastructure",
    "label_zh": "基础设施",
    "type": "capability",
    "parent": "g_business_support",
    "level": 2,
    "description_zh": "横贯业务支撑区底部的宽框。"
  },
  {
    "id": "legend_internal",
    "label_en": "Internal Capability",
    "label_zh": "内部能力（图例）",
    "type": "note",
    "parent": null,
    "position": "左下角图例"
  },
  {
    "id": "legend_external",
    "label_en": "External Capability",
    "label_zh": "外部能力（图例）",
    "type": "note",
    "parent": null,
    "position": "左下角图例"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色大框（图例 Internal Capability）",
    "meaning_zh": "组织内部、由组织 IT 部门提供的能力",
    "explicit": true
  },
  {
    "symbol": "灰色大框（图例 External Capability）",
    "meaning_zh": "组织必须与之交互的外部数字能力",
    "explicit": true
  },
  {
    "symbol": "大框内的小圆角框",
    "meaning_zh": "该能力区域包含的具体能力（无独立图例，由版式推断）",
    "explicit": false
  },
  {
    "symbol": "每个框右上角的小图标（三个叠放方块）",
    "meaning_zh": "ArchiMate 的 Capability（能力）记法图标",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "上下四层：顶部并排两个灰色外部能力框；其下蓝色“互动”大框（内含 2×2 小框）；再下“核心业务主活动”大框（横排 3 个小框）；最下方左右并排“数据管理支撑”（2×2 小框）与“业务支撑”（2 行小框 + 横贯的基础设施）；左下角为图例。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig1-2",
    "relation": "overview_of",
    "note_zh": "图 1-2 把本图“数据管理支撑”区与其 DMBoK/DAMA 轮盘的知识领域逐一对应，是本图该区域的细化。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图没有写出“能力区域/子能力”的层级文字，层级由框的嵌套推断。",
    "图例只说明内部/外部颜色，未说明每个框右上角图标含义；该图标判为 ArchiMate Capability 图标（依据图 2-1，背景知识）。"
  ],
  "analyzed_from": [
    "英文 PDF 第 12 页原图截图（含图例）",
    "英文 PDF 第 12 页正文",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 92–108 行",
    "figs/g21b_fig1-1.svg 源码与渲染图"
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
