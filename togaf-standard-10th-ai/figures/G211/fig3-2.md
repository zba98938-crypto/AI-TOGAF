# G211/fig3-2 · ABC 公司一级业务能力地图

> 当前图示解析：[Markdown](../../architecture/diagrams/G211/fig3-2.md) · [JSON](../../architecture/diagrams/G211/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G211e.pdf`；SHA-256：`93fa7ac115956d34c0ad2161c46a5fd01cbc972d5f85a0f19f2f5b9d8c0a2b34`。

## 原图 · PDF 第 20 页

![英文原图](../assets/G211/fig3-2-p0020.png)

PDF 坐标：`[48.2, 399.8, 563.8, 621.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business Planning
Market Planning
Partner Management
Strategic
Capital Management
Policy Management
Regulatory Compliance Management
Account Management
Product Management
Distribution Management
Core
Customer Management
Channel Management
Agent Management
Financial Management
HR Management
Asset Management
Supporting
Information Management
Training Management
Operations Management
```

## 概要（历史解释；局部修正见上）

ABC 公司 18 项一级业务能力按战略、核心、支撑三层排列的能力地图。

## 目的（历史解释；局部修正见上）

示范第 3.2.1 节的“分层”：把 20–30 项能力分类到不同层，让不同利益相关者聚焦各自关注的部分。本图综合了第 3.1 节的各项输入（组织结构、业务模式、战略/财务计划），也是第 5.1 节热力图（图 5-1）的底图。

## 阅读顺序（历史解释；局部修正见上）

左列自上而下是三层：Strategic（战略）、Core（核心）、Supporting（支撑）。每层右侧占两行，每行三格，共 6 项一级能力；某项能力属于哪一层，看它所在行对应的左列层名。同层内格子的行列位置没有含义。

## 关键含义（历史解释；局部修正见上）

- 战略层（顶层，面向高管的战略与方向设定）：业务规划、市场规划、合作伙伴管理、资本管理、政策管理、监管合规管理。
- 核心层（中层，面向客户的核心业务）：账户管理、产品管理、分销管理、客户管理、渠道管理、代理商管理。
- 支撑层（底层，企业运转必需但在幕后支撑）：财务管理、人力资源管理、资产管理、信息管理、培训管理、运营管理。
- 分层与组织单元无关：初始清单中同属销售的能力分布在战略层（市场规划、合作伙伴管理）和核心层（账户、客户、渠道、代理商管理）；同属运营的能力分布在三层。这正是第 3.1.1 节“不要把组织架构图套到能力地图上”的体现。
- 18 项能力基本对应正文修正后的一级能力候选清单，但原图仍保留了正文建议改作价值流阶段处理的“分销管理”；原图写 Financial Management，正文清单写 Finance Management。
- 本图只回答“有哪些一级能力、各属哪一层”，不表达成熟度、重要性或归属单元；在同一版式上按成熟度着色就是图 5-1 的热力图。
- 每格都是一级（L1）能力；图 3-3 以其中的“人力资源管理”为例，向下分解出二级、三级能力。

## 层级（历史解释；局部修正见上）

两级：层（战略、核心、支撑）→ 一级业务能力，每层 6 项，排成 2 × 3。本图没有二级能力。

## 线条含义（历史解释；局部修正见上）

图中没有连线，表格边框只用来分隔单元格。能力属于哪一层由它所在的行带隐含表达，元素清单中用 parent 记录。

## 易误读点（历史解释；局部修正见上）

- 同层内行列位置只是排版，不表示分组、优先级或先后。
- 层不是组织单元，也不说明由哪个部门执行（能力与组织的对应见图 5-2 的做法）。
- 本图没有着色；成熟度差距着色在图 5-1 中才出现。
- 中文稿当前引用的 figs/g211_fig3-2.svg 只有 15 项能力（缺分销管理、培训管理、运营管理），且把市场规划、合作伙伴管理、资本管理、政策管理、监管合规管理、产品管理放到了与原图不同的层，不能据它判断分层。

## 元素

```json
[
  {
    "id": "tier_strategic",
    "label_en": "Strategic",
    "label_zh": "战略层",
    "type": "group",
    "parent": null,
    "order": 1,
    "position": "左列上"
  },
  {
    "id": "tier_core",
    "label_en": "Core",
    "label_zh": "核心层",
    "type": "group",
    "parent": null,
    "order": 2,
    "position": "左列中"
  },
  {
    "id": "tier_supporting",
    "label_en": "Supporting",
    "label_zh": "支撑层",
    "type": "group",
    "parent": null,
    "order": 3,
    "position": "左列下"
  },
  {
    "id": "c_business_planning",
    "label_en": "Business Planning",
    "label_zh": "业务规划",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 1 行第 1 列"
  },
  {
    "id": "c_market_planning",
    "label_en": "Market Planning",
    "label_zh": "市场规划",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 1 行第 2 列"
  },
  {
    "id": "c_partner_mgmt",
    "label_en": "Partner Management",
    "label_zh": "合作伙伴管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 1 行第 3 列"
  },
  {
    "id": "c_capital_mgmt",
    "label_en": "Capital Management",
    "label_zh": "资本管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 2 行第 1 列"
  },
  {
    "id": "c_policy_mgmt",
    "label_en": "Policy Management",
    "label_zh": "政策管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 2 行第 2 列"
  },
  {
    "id": "c_reg_compliance_mgmt",
    "label_en": "Regulatory Compliance Management",
    "label_zh": "监管合规管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 2 行第 3 列"
  },
  {
    "id": "c_account_mgmt",
    "label_en": "Account Management",
    "label_zh": "账户管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 3 行第 1 列"
  },
  {
    "id": "c_product_mgmt",
    "label_en": "Product Management",
    "label_zh": "产品管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 3 行第 2 列"
  },
  {
    "id": "c_distribution_mgmt",
    "label_en": "Distribution Management",
    "label_zh": "分销管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 3 行第 3 列"
  },
  {
    "id": "c_customer_mgmt",
    "label_en": "Customer Management",
    "label_zh": "客户管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 4 行第 1 列"
  },
  {
    "id": "c_channel_mgmt",
    "label_en": "Channel Management",
    "label_zh": "渠道管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 4 行第 2 列"
  },
  {
    "id": "c_agent_mgmt",
    "label_en": "Agent Management",
    "label_zh": "代理商管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 4 行第 3 列"
  },
  {
    "id": "c_financial_mgmt",
    "label_en": "Financial Management",
    "label_zh": "财务管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 5 行第 1 列"
  },
  {
    "id": "c_hr_mgmt",
    "label_en": "HR Management",
    "label_zh": "人力资源管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 5 行第 2 列",
    "description_zh": "图 3-3 对它做了分解。"
  },
  {
    "id": "c_asset_mgmt",
    "label_en": "Asset Management",
    "label_zh": "资产管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 5 行第 3 列"
  },
  {
    "id": "c_information_mgmt",
    "label_en": "Information Management",
    "label_zh": "信息管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 6 行第 1 列"
  },
  {
    "id": "c_training_mgmt",
    "label_en": "Training Management",
    "label_zh": "培训管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 6 行第 2 列"
  },
  {
    "id": "c_operations_mgmt",
    "label_en": "Operations Management",
    "label_zh": "运营管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 6 行第 3 列"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_l1_map",
    "title_zh": "一级能力地图（按原图逐行转录）",
    "columns": [
      "层",
      "第 1 列",
      "第 2 列",
      "第 3 列"
    ],
    "rows": [
      [
        "战略 Strategic",
        "业务规划 Business Planning",
        "市场规划 Market Planning",
        "合作伙伴管理 Partner Management"
      ],
      [
        "战略 Strategic",
        "资本管理 Capital Management",
        "政策管理 Policy Management",
        "监管合规管理 Regulatory Compliance Management"
      ],
      [
        "核心 Core",
        "账户管理 Account Management",
        "产品管理 Product Management",
        "分销管理 Distribution Management"
      ],
      [
        "核心 Core",
        "客户管理 Customer Management",
        "渠道管理 Channel Management",
        "代理商管理 Agent Management"
      ],
      [
        "支撑 Supporting",
        "财务管理 Financial Management",
        "人力资源管理 HR Management",
        "资产管理 Asset Management"
      ],
      [
        "支撑 Supporting",
        "信息管理 Information Management",
        "培训管理 Training Management",
        "运营管理 Operations Management"
      ]
    ],
    "notes_zh": "原图每层两行，层名写在左列的合并单元格中；这里每行重复写出层名。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "左列单元格（层名）",
    "meaning_zh": "能力分层：Strategic 战略 / Core 核心 / Supporting 支撑",
    "explicit": false
  },
  {
    "symbol": "右侧单元格",
    "meaning_zh": "一项一级业务能力，归属所在行带的层",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "左列三个合并单元格写层名；右侧 6 行 × 3 列能力格，每层占两行。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "层名 Strategic/Core/Supporting 的中文“战略层/核心层/支撑层”由解析者拟定；中文稿正文用“顶层/中层/底层”描述。"
  ],
  "analyzed_from": [
    "英文 PDF 第 20 页原图截图（220 dpi）",
    "英文 PDF 第 17–20 页正文",
    "中文稿 G211e_业务能力.md 第 211–243 行",
    "figs/g211_fig3-2.svg 源码"
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
