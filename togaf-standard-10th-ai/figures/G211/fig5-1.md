# G211/fig5-1 · ABC 公司业务能力热力图

> 当前图示解析：[Markdown](../../architecture/diagrams/G211/fig5-1.md) · [JSON](../../architecture/diagrams/G211/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G211e.pdf`；SHA-256：`93fa7ac115956d34c0ad2161c46a5fd01cbc972d5f85a0f19f2f5b9d8c0a2b34`。

## 原图 · PDF 第 24 页

![英文原图](../assets/G211/fig5-1-p0024.png)

PDF 坐标：`[48.2, 36.0, 563.8, 258.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Strategic
Core
Supporting
```

## 概要（历史解释；局部修正见上）

按成熟度给 ABC 公司一级能力地图着色：3 红、3 黄、1 紫，其余 11 项为绿。

## 目的（历史解释；局部修正见上）

示范第 5.1 节的热力映射：用颜色突出能力差距，让业务领导据此排定投资和项目优先级，把紫、红、黄的能力提升到期望成熟度。正文还指出同一能力地图可按其他视角（战略贡献、绩效、收入/成本贡献、覆盖度、关键性）生成不同热力图。

## 阅读顺序（历史解释；局部修正见上）

版式与图 3-2 相同：左列三层（Strategic、Core、Supporting），每层右侧 2 × 3 格。先看颜色：绿 = 已达到期望成熟度；黄 = 差一级；红 = 差两级及以上；紫 = 今天不存在、未来需要。图上没有图例，颜色含义来自第 5.1 节正文。

## 关键含义（历史解释；局部修正见上）

- 红色（需立即关注）：市场规划、政府关系管理（均在战略层）、人力资源管理（支撑层）。
- 黄色（有问题但优先级较低）：合作伙伴管理（战略层）、客户管理（核心层）、培训管理（支撑层）。
- 紫色：代理商管理（核心层），是企业希望发展的新能力；正文说明能力缺失意味着重大差距。
- 其余 11 项为绿色，已达到期望成熟度。需要改进的能力分布在三层，没有集中在某一层。
- 本图与图 3-2 版式相同，但有 3 格名称不同：本图写政府关系管理、采购管理、IT 管理，图 3-2 同位置为监管合规管理、资产管理、信息管理（第 3.1.1 节修正后的名称）；正文解读本图时也沿用“政府关系管理”。
- 颜色只表达“成熟度”这一个视角；正文列出的战略贡献、绩效/有效性、收入贡献、成本贡献、覆盖度、关键性等视角可在同一能力地图上生成其他热力图。
- 热力图的结论用于投资决策：业务领导据此确保投资和项目举措按适当水平排序并获得资金。

## 层级（历史解释；局部修正见上）

与图 3-2 相同：层（战略、核心、支撑）→ 一级能力，每层 6 项。颜色是每格的属性，不表示层级。

## 线条含义（历史解释；局部修正见上）

图中没有连线。能力属于哪一层由所在行带表达；成熟度状态由单元格底色表达（见元素 attributes.heat 和表格的 cell_legend）。

## 易误读点（历史解释；局部修正见上）

- 颜色表示与期望成熟度的差距，不表示能力的重要性或成本；红色是差距最大的，不是最重要的。
- 紫色表示今天不存在但未来需要，不是“比红色更差”的成熟度等级。
- 政府关系管理、采购管理、IT 管理与图 3-2 同位置的监管合规管理、资产管理、信息管理名称不同，原文没有解释；更像是沿用了修正前的名称，而不是新增或删除了能力（解析者推断）。
- 中文稿当前引用的 figs/g211_fig5-1.svg 按颜色重排了格子、去掉了分层，并混入了图 3-2 的能力名，不能据它对照各能力在地图上的位置。

## 元素

```json
[
  {
    "id": "tier_strategic",
    "label_en": "Strategic",
    "label_zh": "战略层",
    "type": "group",
    "parent": null,
    "order": 1
  },
  {
    "id": "tier_core",
    "label_en": "Core",
    "label_zh": "核心层",
    "type": "group",
    "parent": null,
    "order": 2
  },
  {
    "id": "tier_supporting",
    "label_en": "Supporting",
    "label_zh": "支撑层",
    "type": "group",
    "parent": null,
    "order": 3
  },
  {
    "id": "c_business_planning",
    "label_en": "Business Planning",
    "label_zh": "业务规划",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 1 行第 1 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_market_planning",
    "label_en": "Market Planning",
    "label_zh": "市场规划",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 1 行第 2 列",
    "attributes": {
      "heat": "red"
    },
    "description_zh": "需立即关注。"
  },
  {
    "id": "c_partner_mgmt",
    "label_en": "Partner Management",
    "label_zh": "合作伙伴管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 1 行第 3 列",
    "attributes": {
      "heat": "yellow"
    },
    "description_zh": "有问题，优先级较低。"
  },
  {
    "id": "c_capital_mgmt",
    "label_en": "Capital Management",
    "label_zh": "资本管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 2 行第 1 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_policy_mgmt",
    "label_en": "Policy Management",
    "label_zh": "政策管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 2 行第 2 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_gov_relations_mgmt",
    "label_en": "Government Relations Management",
    "label_zh": "政府关系管理",
    "type": "capability",
    "parent": "tier_strategic",
    "level": 1,
    "position": "第 2 行第 3 列",
    "attributes": {
      "heat": "red"
    },
    "description_zh": "需立即关注。图 3-2 同位置为“监管合规管理”。"
  },
  {
    "id": "c_account_mgmt",
    "label_en": "Account Management",
    "label_zh": "账户管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 3 行第 1 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_product_mgmt",
    "label_en": "Product Management",
    "label_zh": "产品管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 3 行第 2 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_distribution_mgmt",
    "label_en": "Distribution Management",
    "label_zh": "分销管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 3 行第 3 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_customer_mgmt",
    "label_en": "Customer Management",
    "label_zh": "客户管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 4 行第 1 列",
    "attributes": {
      "heat": "yellow"
    },
    "description_zh": "有问题，优先级较低。"
  },
  {
    "id": "c_channel_mgmt",
    "label_en": "Channel Management",
    "label_zh": "渠道管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 4 行第 2 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_agent_mgmt",
    "label_en": "Agent Management",
    "label_zh": "代理商管理",
    "type": "capability",
    "parent": "tier_core",
    "level": 1,
    "position": "第 4 行第 3 列",
    "attributes": {
      "heat": "purple"
    },
    "description_zh": "企业希望发展的新能力（今天不存在）。"
  },
  {
    "id": "c_financial_mgmt",
    "label_en": "Financial Management",
    "label_zh": "财务管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 5 行第 1 列",
    "attributes": {
      "heat": "green"
    }
  },
  {
    "id": "c_hr_mgmt",
    "label_en": "HR Management",
    "label_zh": "人力资源管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 5 行第 2 列",
    "attributes": {
      "heat": "red"
    },
    "description_zh": "需立即关注。"
  },
  {
    "id": "c_procurement_mgmt",
    "label_en": "Procurement Management",
    "label_zh": "采购管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 5 行第 3 列",
    "attributes": {
      "heat": "green"
    },
    "description_zh": "图 3-2 同位置为“资产管理”。"
  },
  {
    "id": "c_it_mgmt",
    "label_en": "IT Management",
    "label_zh": "IT 管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 6 行第 1 列",
    "attributes": {
      "heat": "green"
    },
    "description_zh": "图 3-2 同位置为“信息管理”。"
  },
  {
    "id": "c_training_mgmt",
    "label_en": "Training Management",
    "label_zh": "培训管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 6 行第 2 列",
    "attributes": {
      "heat": "yellow"
    },
    "description_zh": "有问题，优先级较低。"
  },
  {
    "id": "c_operations_mgmt",
    "label_en": "Operations Management",
    "label_zh": "运营管理",
    "type": "capability",
    "parent": "tier_supporting",
    "level": 1,
    "position": "第 6 行第 3 列",
    "attributes": {
      "heat": "green"
    }
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_heatmap",
    "title_zh": "能力成熟度热力图（按原图逐行转录，括号内为单元格颜色）",
    "columns": [
      "层",
      "第 1 列",
      "第 2 列",
      "第 3 列"
    ],
    "rows": [
      [
        "战略 Strategic",
        "业务规划 Business Planning（绿）",
        "市场规划 Market Planning（红）",
        "合作伙伴管理 Partner Management（黄）"
      ],
      [
        "战略 Strategic",
        "资本管理 Capital Management（绿）",
        "政策管理 Policy Management（绿）",
        "政府关系管理 Government Relations Management（红）"
      ],
      [
        "核心 Core",
        "账户管理 Account Management（绿）",
        "产品管理 Product Management（绿）",
        "分销管理 Distribution Management（绿）"
      ],
      [
        "核心 Core",
        "客户管理 Customer Management（黄）",
        "渠道管理 Channel Management（绿）",
        "代理商管理 Agent Management（紫）"
      ],
      [
        "支撑 Supporting",
        "财务管理 Financial Management（绿）",
        "人力资源管理 HR Management（红）",
        "采购管理 Procurement Management（绿）"
      ],
      [
        "支撑 Supporting",
        "IT 管理 IT Management（绿）",
        "培训管理 Training Management（黄）",
        "运营管理 Operations Management（绿）"
      ]
    ],
    "cell_legend": [
      "绿 = 已达到期望成熟度",
      "黄 = 差一级",
      "红 = 差两级及以上",
      "紫 = 今天不存在、未来需要",
      "（原图无图例，含义取自第 5.1 节正文）"
    ],
    "notes_zh": "格子位置与图 3-2 一一对应；第 2 行第 3 列、第 5 行第 3 列、第 6 行第 1 列的名称与图 3-2 不同。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深绿色填充",
    "meaning_zh": "已达到期望成熟度",
    "explicit": false
  },
  {
    "symbol": "黄色填充",
    "meaning_zh": "距期望成熟度差一级",
    "explicit": false
  },
  {
    "symbol": "红色填充",
    "meaning_zh": "距期望成熟度差两级及以上",
    "explicit": false
  },
  {
    "symbol": "紫色填充",
    "meaning_zh": "今天不存在、未来需要的能力",
    "explicit": false
  },
  {
    "symbol": "左列白底单元格",
    "meaning_zh": "能力分层（Strategic/Core/Supporting）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "与图 3-2 相同：左列三层名，右侧 6 行 × 3 列能力格，每格整格填色。"
}
```

## 相关图

```json
[
  {
    "target": "G211/fig3-2",
    "relation": "based_on",
    "note_zh": "同一张分层一级能力地图按成熟度着色；18 格中 15 格名称相同，另 3 格沿用修正前的名称（政府关系管理、采购管理、IT 管理）"
  },
  {
    "target": "G178/fig4-4",
    "relation": "related",
    "note_zh": "同为业务能力热力图；G178 图 4-4 着色的是招聘员工价值流各阶段所映射的能力"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图没有图例，颜色含义按第 5.1 节对成熟度热力图的说明解释。",
    "3 格名称与图 3-2 不同的原因原文没有说明。"
  ],
  "analyzed_from": [
    "英文 PDF 第 24 页原图截图（220 dpi）",
    "英文 PDF 第 23–24 页正文",
    "中文稿 G211e_业务能力.md 第 296–311、353 行",
    "figs/g211_fig5-1.svg 源码（格子与颜色）"
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
