# G233/fig6-1 · 业务能力目录模型（示例）

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig6-1.md) · [JSON](../../architecture/diagrams/G233/fig6-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 35 页

![英文原图](../assets/G233/fig6-1-p0035.png)

PDF 坐标：`[48.2, 36.0, 563.8, 216.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Retail Storefront
Strategic
Operations (Core)
Basket Management cil
Business Planning i
Risk Management af
Human Resource i
Finance Management <i
Management
Iaentity
c
Payroll Management if
Management
HR Position
ce}
Catalog Products il
Market Research ff
Management
Payment Processing ff
Contract
Es)
Management
Job Posting
ci}
Incentive
a
Product Development
Management
Business Planning <i
Delivery Management i
Skis Assessment ef]
‘Store Layout
Program Management fi
Management
Inventory Management if
Schedule
ei)
Bonofits
ce}
Management
Management
Customer
Relationship
Management
```

## 概要（历史解释；局部修正见上）

把示例业务能力按零售前台、战略、运营（核心）三类编成目录，并用嵌套标出一级能力下的二级能力。

## 目的（历史解释；局部修正见上）

第 6.2.1 节给出能力目录的可视化样例：目录应覆盖组织运作所需的全部能力，并按类别/视角逻辑分组以便导航；同时用嵌套展示“一级能力—二级能力”的分解，示范目录要大到足够包容、小到可被有效导航。

## 阅读顺序（历史解释；局部修正见上）

从左到右读三个灰色分类带：Retail Storefront（门店前台）、Strategic（战略）、Operations (Core)（运营核心）。每个沙色框是一个一级业务能力；框内白色小框是其下的二级能力（如 Program Management 下的 Schedule Management）。分类带只表示目录分组，不表示流程或组织层级；全图没有箭头。

## 关键含义（历史解释；局部修正见上）

- 目录分三类：Retail Storefront 5 个一级能力（无二级）；Strategic 7 个一级能力（含重复的 Business Planning）＋2 个二级能力；Operations (Core) 4 个一级能力＋6 个二级能力。
- Retail Storefront 的五项是 Basket Management、Catalog Products、Incentive Management、Store Layout Management、Customer Relationship Management，都直接面向线上/门店购物体验。
- Strategic 含 Business Planning、Market Research、Product Development、Program Management（下含 Schedule Management）、Risk Management（下含 Identity Management）、Contract Management，以及第二个同名的 Business Planning 框。
- Operations (Core) 含 Human Resource Management（下含 HR Position Management、Job Posting、Skills Assessment、Benefits Management）、Finance Management（下含 Payroll Management、Payment Processing）、Delivery Management、Inventory Management。
- “Business Planning”在原图中出现两次（Strategic 左上与右中），两个框同名同级；更像原图的重复放置，而不是两个不同的能力，读图时不应据此推断存在两个业务规划能力。
- Identity Management 被嵌套在 Risk Management 之下，而不是单列；这是示例作者的归类选择，不应理解为“身份管理必然属于风险管理”。
- 二级能力只在需要说明分解时出现：Program Management、Risk Management、Human Resource Management、Finance Management 有下级；其余一级能力不再下钻。
- 目录是说明性示例，不是完整清单；正文提醒目录超过 100 项时，很可能把能力实例、实例组件或价值流阶段误当成能力。

## 层级（历史解释；局部修正见上）

三层：3 个目录分类（灰色带）→ 16 个一级能力框（Business Planning 重复一次，按 15 个唯一名称计）→ 8 个二级能力（白色小框）。分类是导航分组，不是能力上下级；能力上下级只由框套框表达。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线；分类归属由“位于灰色带内”表达，一级/二级关系由“白色小框嵌在沙色框内”表达。关系清单把 8 条二级→一级的分解补记为隐式 composition。

## 易误读点（历史解释；局部修正见上）

- 中文稿第 6.2.1 节引用的 PNG 与其标签表其实是图 6-2 的价值流—能力映射，不是本图；不能据中文稿理解能力目录，必须以英文 PDF 第 35 页上图为准。
- 不要把两个同名的 Business Planning 当成两个能力；原图重复，按一个能力理解、按两个框记录。
- 不要把 Identity Management 理解为风险管理的必然子能力；这是示例的归类选择。
- 不要把灰色分类带当成组织部门或价值流阶段；它们只是目录的导航分类。
- 不要把“能力目录”与“能力地图/热力图”混为一谈：本图只列能力及层级，不含成熟度、差距或价值流映射。

## 元素

```json
[
  {
    "id": "cat_storefront",
    "label_en": "Retail Storefront",
    "label_zh": "零售前台",
    "type": "group",
    "parent": null,
    "order": 1,
    "position": "左侧灰色分类带"
  },
  {
    "id": "cat_strategic",
    "label_en": "Strategic",
    "label_zh": "战略",
    "type": "group",
    "parent": null,
    "order": 2,
    "position": "中间灰色分类带"
  },
  {
    "id": "cat_operations",
    "label_en": "Operations (Core)",
    "label_zh": "运营（核心）",
    "type": "group",
    "parent": null,
    "order": 3,
    "position": "右侧灰色分类带"
  },
  {
    "id": "cap_basket",
    "label_en": "Basket Management",
    "label_zh": "购物篮管理",
    "type": "capability",
    "parent": "cat_storefront",
    "level": 1,
    "order": 1
  },
  {
    "id": "cap_catalog_products",
    "label_en": "Catalog Products",
    "label_zh": "产品编目",
    "type": "capability",
    "parent": "cat_storefront",
    "level": 1,
    "order": 2
  },
  {
    "id": "cap_incentive",
    "label_en": "Incentive Management",
    "label_zh": "激励管理",
    "type": "capability",
    "parent": "cat_storefront",
    "level": 1,
    "order": 3
  },
  {
    "id": "cap_store_layout",
    "label_en": "Store Layout Management",
    "label_zh": "门店布局管理",
    "type": "capability",
    "parent": "cat_storefront",
    "level": 1,
    "order": 4
  },
  {
    "id": "cap_crm",
    "label_en": "Customer Relationship Management",
    "label_zh": "客户关系管理",
    "type": "capability",
    "parent": "cat_storefront",
    "level": 1,
    "order": 5
  },
  {
    "id": "cap_business_planning_1",
    "label_en": "Business Planning",
    "label_zh": "业务规划",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 1,
    "description_zh": "Strategic 左上；与原图右中的同名框重复。"
  },
  {
    "id": "cap_market_research",
    "label_en": "Market Research",
    "label_zh": "市场研究",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 2
  },
  {
    "id": "cap_product_dev",
    "label_en": "Product Development",
    "label_zh": "产品开发",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 3
  },
  {
    "id": "cap_program",
    "label_en": "Program Management",
    "label_zh": "项目群管理",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 4
  },
  {
    "id": "cap_schedule",
    "label_en": "Schedule Management",
    "label_zh": "进度管理",
    "type": "capability",
    "parent": "cap_program",
    "level": 2
  },
  {
    "id": "cap_risk",
    "label_en": "Risk Management",
    "label_zh": "风险管理",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 5
  },
  {
    "id": "cap_identity",
    "label_en": "Identity Management",
    "label_zh": "身份管理",
    "type": "capability",
    "parent": "cap_risk",
    "level": 2,
    "description_zh": "原图把它嵌在 Risk Management 内，属于示例的归类选择。"
  },
  {
    "id": "cap_contract",
    "label_en": "Contract Management",
    "label_zh": "合同管理",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 6
  },
  {
    "id": "cap_business_planning_2",
    "label_en": "Business Planning",
    "label_zh": "业务规划",
    "type": "capability",
    "parent": "cat_strategic",
    "level": 1,
    "order": 7,
    "description_zh": "Strategic 右中；与原图左上同名框重复。"
  },
  {
    "id": "cap_hr",
    "label_en": "Human Resource Management",
    "label_zh": "人力资源管理",
    "type": "capability",
    "parent": "cat_operations",
    "level": 1,
    "order": 1
  },
  {
    "id": "cap_hr_position",
    "label_en": "HR Position Management",
    "label_zh": "人力资源岗位管理",
    "type": "capability",
    "parent": "cap_hr",
    "level": 2,
    "order": 1
  },
  {
    "id": "cap_job_posting",
    "label_en": "Job Posting",
    "label_zh": "职位发布",
    "type": "capability",
    "parent": "cap_hr",
    "level": 2,
    "order": 2
  },
  {
    "id": "cap_skills",
    "label_en": "Skills Assessment",
    "label_zh": "技能评估",
    "type": "capability",
    "parent": "cap_hr",
    "level": 2,
    "order": 3
  },
  {
    "id": "cap_benefits",
    "label_en": "Benefits Management",
    "label_zh": "福利管理",
    "type": "capability",
    "parent": "cap_hr",
    "level": 2,
    "order": 4
  },
  {
    "id": "cap_finance",
    "label_en": "Finance Management",
    "label_zh": "财务管理",
    "type": "capability",
    "parent": "cat_operations",
    "level": 1,
    "order": 2
  },
  {
    "id": "cap_payroll",
    "label_en": "Payroll Management",
    "label_zh": "薪资管理",
    "type": "capability",
    "parent": "cap_finance",
    "level": 2,
    "order": 1
  },
  {
    "id": "cap_payment_processing",
    "label_en": "Payment Processing",
    "label_zh": "支付处理",
    "type": "capability",
    "parent": "cap_finance",
    "level": 2,
    "order": 2
  },
  {
    "id": "cap_delivery",
    "label_en": "Delivery Management",
    "label_zh": "交付管理",
    "type": "capability",
    "parent": "cat_operations",
    "level": 1,
    "order": 3
  },
  {
    "id": "cap_inventory",
    "label_en": "Inventory Management",
    "label_zh": "库存管理",
    "type": "capability",
    "parent": "cat_operations",
    "level": 1,
    "order": 4
  }
]
```

## 关系

```json
[
  {
    "from": "cap_schedule",
    "to": "cap_program",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "二级能力嵌在一级能力框内，表示分解/组成。"
  },
  {
    "from": "cap_identity",
    "to": "cap_risk",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "cap_hr_position",
    "to": "cap_hr",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "cap_job_posting",
    "to": "cap_hr",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "cap_skills",
    "to": "cap_hr",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "cap_benefits",
    "to": "cap_hr",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "cap_payroll",
    "to": "cap_finance",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "cap_payment_processing",
    "to": "cap_finance",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_catalog",
    "title_zh": "能力目录逐项转录（按分类带、自上而下）",
    "columns": [
      "分类",
      "一级能力（L1）",
      "二级能力（L2）"
    ],
    "rows": [
      [
        "Retail Storefront 零售前台",
        "Basket Management 购物篮管理",
        "—"
      ],
      [
        "Retail Storefront 零售前台",
        "Catalog Products 产品编目",
        "—"
      ],
      [
        "Retail Storefront 零售前台",
        "Incentive Management 激励管理",
        "—"
      ],
      [
        "Retail Storefront 零售前台",
        "Store Layout Management 门店布局管理",
        "—"
      ],
      [
        "Retail Storefront 零售前台",
        "Customer Relationship Management 客户关系管理",
        "—"
      ],
      [
        "Strategic 战略",
        "Business Planning 业务规划（左上）",
        "—"
      ],
      [
        "Strategic 战略",
        "Market Research 市场研究",
        "—"
      ],
      [
        "Strategic 战略",
        "Product Development 产品开发",
        "—"
      ],
      [
        "Strategic 战略",
        "Program Management 项目群管理",
        "Schedule Management 进度管理"
      ],
      [
        "Strategic 战略",
        "Risk Management 风险管理",
        "Identity Management 身份管理"
      ],
      [
        "Strategic 战略",
        "Contract Management 合同管理",
        "—"
      ],
      [
        "Strategic 战略",
        "Business Planning 业务规划（右中，重复框）",
        "—"
      ],
      [
        "Operations (Core) 运营（核心）",
        "Human Resource Management 人力资源管理",
        "HR Position Management 人力资源岗位管理；Job Posting 职位发布；Skills Assessment 技能评估；Benefits Management 福利管理"
      ],
      [
        "Operations (Core) 运营（核心）",
        "Finance Management 财务管理",
        "Payroll Management 薪资管理；Payment Processing 支付处理"
      ],
      [
        "Operations (Core) 运营（核心）",
        "Delivery Management 交付管理",
        "—"
      ],
      [
        "Operations (Core) 运营（核心）",
        "Inventory Management 库存管理",
        "—"
      ]
    ],
    "notes_zh": "原图中 Business Planning 出现两次，均记录；两个白框二级能力分别挂在 Program Management 与 Risk Management 下，HR 与 Finance 的二级能力各有多项。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色标签式横带",
    "meaning_zh": "能力目录的分类/视角（Retail Storefront、Strategic、Operations (Core)）",
    "explicit": false
  },
  {
    "symbol": "沙色圆角框 + 能力网格图标",
    "meaning_zh": "一级业务能力",
    "explicit": false
  },
  {
    "symbol": "白色小框（嵌在沙色框内）",
    "meaning_zh": "该一级能力下的二级能力",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "横向三个灰色分类带：左带窄（Retail Storefront，5 框纵排）；中带最宽（Strategic，左列 4 框、右列 3 框）；右带宽（Operations (Core)，左列 1 个大框含 4 个二级、右列 1 个大框含 2 个二级＋2 个独立一级能力）。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig6-2",
    "relation": "precedes",
    "note_zh": "图 6-2 从本目录中挑选能力，交叉映射到 Acquire Retail Product Online 价值流的五个阶段"
  },
  {
    "target": "G233/fig4-1",
    "relation": "related",
    "note_zh": "组织架构图提供了“能力可能存在的位置”；本图把 Finance、HR 等职能重新分组为跨组织的能力目录"
  },
  {
    "target": "G233/fig6-3",
    "relation": "basis_for",
    "note_zh": "图 6-3 为图 6-2 选中的能力建立实例，能力名全部来自本目录"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "原图 Business Planning 重复出现两次，无法判断是刻意表示两个不同能力还是排版重复；本文按两个框记录、按一个能力解读，并在表格中标注。",
    "Identity Management 被嵌在 Risk Management 内，无法从图上判断是刻意的归类还是排版错位；按画面记录为二级能力。",
    "英文与中文的 fig6-1 PNG 均实际截取了图 6-2，标签表也对应图 6-2；本分析完全依据英文 PDF 第 35 页上图的能力目录。",
    "原图部分能力框字号偏大、贴近边框（如 Customer Relationship Management、Inventory Management），但文字完整可辨。"
  ],
  "analyzed_from": [
    "英文 PDF 第 35 页图 6-1 截图（figctx 裁剪）与 2×2 放大分块",
    "英文 PDF 第 34–35 页正文",
    "英文 PDF 第 35 页上图 6-1 与下图 6-2 两个裁剪（确认二者同页上下排列）",
    "中文稿 G233e_业务能力规划.md 第 501–530 行（含标签对照表）",
    "figs/g233e_fig6-1_en.png、figs/zh/g233e_fig6-1_zh.png（均确认为图 6-2 内容）"
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
