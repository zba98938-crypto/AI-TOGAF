# G206/fig3-1 · 标准组织架构图

> 当前图示解析：[Markdown](../../architecture/diagrams/G206/fig3-1.md) · [JSON](../../architecture/diagrams/G206/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G206e.pdf`；SHA-256：`5de1a634ef389e88b16b11454fdf96350ab33664468a0df2a6aed513e2270c35`。

## 原图 · PDF 第 14 页

![英文原图](../assets/G206/fig3-1-p0014.png)

PDF 坐标：`[48.2, 265.2, 563.8, 523.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
CEO
Head,
Head,
Head,
Head,
Finance &Admin
|
Engineering
) |
Supply Chain
|
Marketing
|
Category
Management
H
| User Experience 4 |
K Digital Marketing H Human Resource |
Finance
| Business Logic 4 | Procurement -
H Brand Marketing H
|
Admin
(servers, networks)
H | Shipping & Logistics ~
| Affiliate Marketing a Facilities |
```

## 概要（历史解释；局部修正见上）

用三层方框和折线把 CEO、四位职能负责人与 13 个部门连成自上而下的汇报树。

## 目的（历史解释；局部修正见上）

作为第 3 章的对照物，先给出读者熟悉的传统组织架构图，再说明组织地图的不同：这张图只画正式汇报线，以职位和部门为单位，无法表达横向、同级、多对多以及对外关系。

## 阅读顺序（历史解释；局部修正见上）

从最上方的 CEO 开始沿折线向下：第二层是工程、供应链、市场、财务与行政四位负责人，第三层是各自管辖的部门。同一水平线上的框之间没有任何连线，说明图不表达它们之间的关系。

## 关键含义（历史解释；局部修正见上）

- 共 18 个框、3 个层级：CEO → 4 位职能负责人 → 13 个部门。
- 只有垂直的汇报折线，没有横向、跨部门或对外的连线；这正是正文所说“无法描绘同级、多对多关系”的直观例子。
- 负责人框写作“Head, Engineering”等职位名，体现组织架构图以具名个人和头衔为中心。
- 四条职能线的部门数分别为 3、4、3、3；供应链线最多，含品类管理、采购、运输与物流、仓库。
- 部门名多为职能（财务、人力资源、采购、市场），没有外部伙伴、协作团队或企业边界标识。
- 图中没有图例；方框加折线的记法本身即为读者熟知的组织架构图惯例。

## 层级（历史解释；局部修正见上）

三层。L1 为 CEO；L2 为工程、供应链、市场、财务与行政四位负责人；L3 为各部门（工程线 3 个、供应链线 4 个、市场线 3 个、财务与行政线 3 个）。每个 L3 部门只有一个上级，L2 也只向 CEO 汇报。

## 线条含义（历史解释；局部修正见上）

深色折线从上级框底边中点引出，经一条水平总线分配到各下级框顶边；没有箭头，方向由上下位置隐含（上→下即“管辖/汇报”）。折线不表示流程、数据流或影响。

## 易误读点（历史解释；局部修正见上）

- 折线只表示正式汇报关系，不是流程、数据流或协作关系。
- 同一层的框之间没有连线，不能据此推断它们之间没有协作；只是这种图不表达横向关系。
- CEO 与“Head, …”是职位/角色，不是组织单元本身的名称。
- 本图是被对比的传统做法，不代表本指南推荐的组织地图画法。
- 中文重绘 PNG 中“Head, Finance & Admin”未译，不能据此认为原图本身中英混排。

## 元素

```json
[
  {
    "id": "ceo",
    "label_en": "CEO",
    "label_zh": "首席执行官（CEO）",
    "type": "role",
    "parent": null,
    "level": 1,
    "position": "顶部居中"
  },
  {
    "id": "head_engineering",
    "label_en": "Head, Engineering",
    "label_zh": "工程负责人",
    "type": "role",
    "parent": null,
    "level": 2,
    "order": 1,
    "position": "第二层最左"
  },
  {
    "id": "head_supply_chain",
    "label_en": "Head, Supply Chain",
    "label_zh": "供应链负责人",
    "type": "role",
    "parent": null,
    "level": 2,
    "order": 2,
    "position": "第二层左二"
  },
  {
    "id": "head_marketing",
    "label_en": "Head, Marketing",
    "label_zh": "市场负责人",
    "type": "role",
    "parent": null,
    "level": 2,
    "order": 3,
    "position": "第二层右二"
  },
  {
    "id": "head_finance_admin",
    "label_en": "Head, Finance & Admin",
    "label_zh": "财务与行政负责人",
    "type": "role",
    "parent": null,
    "level": 2,
    "order": 4,
    "position": "第二层最右"
  },
  {
    "id": "user_experience",
    "label_en": "User Experience",
    "label_zh": "用户体验",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 1,
    "position": "工程线第 1 个"
  },
  {
    "id": "business_logic",
    "label_en": "Business Logic",
    "label_zh": "业务逻辑",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 2,
    "position": "工程线第 2 个"
  },
  {
    "id": "admin_servers_networks",
    "label_en": "Admin (servers, networks)",
    "label_zh": "行政（服务器、网络）",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "工程线第 3 个"
  },
  {
    "id": "category_management",
    "label_en": "Category Management",
    "label_zh": "品类管理",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 1,
    "position": "供应链线第 1 个"
  },
  {
    "id": "procurement",
    "label_en": "Procurement",
    "label_zh": "采购",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 2,
    "position": "供应链线第 2 个"
  },
  {
    "id": "shipping_logistics",
    "label_en": "Shipping & Logistics",
    "label_zh": "运输与物流",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "供应链线第 3 个"
  },
  {
    "id": "warehouse",
    "label_en": "Warehouse",
    "label_zh": "仓库",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 4,
    "position": "供应链线第 4 个"
  },
  {
    "id": "digital_marketing",
    "label_en": "Digital Marketing",
    "label_zh": "数字营销",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 1,
    "position": "市场线第 1 个"
  },
  {
    "id": "brand_marketing",
    "label_en": "Brand Marketing",
    "label_zh": "品牌营销",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 2,
    "position": "市场线第 2 个"
  },
  {
    "id": "affiliate_marketing",
    "label_en": "Affiliate Marketing",
    "label_zh": "联盟营销",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "市场线第 3 个"
  },
  {
    "id": "human_resource",
    "label_en": "Human Resource",
    "label_zh": "人力资源",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 1,
    "position": "财务与行政线第 1 个"
  },
  {
    "id": "finance",
    "label_en": "Finance",
    "label_zh": "财务",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 2,
    "position": "财务与行政线第 2 个"
  },
  {
    "id": "facilities",
    "label_en": "Facilities",
    "label_zh": "设施",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "财务与行政线第 3 个"
  }
]
```

## 关系

```json
[
  {
    "from": "head_engineering",
    "to": "ceo",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "负责人向 CEO 汇报"
  },
  {
    "from": "head_supply_chain",
    "to": "ceo",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "head_marketing",
    "to": "ceo",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "head_finance_admin",
    "to": "ceo",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "user_experience",
    "to": "head_engineering",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "business_logic",
    "to": "head_engineering",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "admin_servers_networks",
    "to": "head_engineering",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "category_management",
    "to": "head_supply_chain",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "procurement",
    "to": "head_supply_chain",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "shipping_logistics",
    "to": "head_supply_chain",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "warehouse",
    "to": "head_supply_chain",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "digital_marketing",
    "to": "head_marketing",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "brand_marketing",
    "to": "head_marketing",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "affiliate_marketing",
    "to": "head_marketing",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "human_resource",
    "to": "head_finance_admin",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "finance",
    "to": "head_finance_admin",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "facilities",
    "to": "head_finance_admin",
    "type": "reports_to",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝灰圆角矩形",
    "meaning_zh": "组织单元/职位（CEO、职能负责人、部门）",
    "explicit": false
  },
  {
    "symbol": "深色折线（无箭头）",
    "meaning_zh": "正式汇报关系，方向由上下位置决定",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "自上而下的三层树：CEO 居中置顶，四个负责人框等距横排，每个负责人下方一条垂直总线，左侧挂 3–4 个部门框。"
}
```

## 相关图

```json
[
  {
    "target": "G206/fig3-2",
    "relation": "contrasts_with",
    "note_zh": "图 3-1 是只画正式汇报线、以职位为中心的传统组织架构图；图 3-2 是同时画内部/外部工作关系的组织地图，二者构成第 3 章的核心对比"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "骨架把 figs/zh/g206e_fig3-1_zh.png 标为“被中文稿引用”，实际 L147 引用的是 figs/zh/g206e_fig3-1_zh.svg；两个资产都已核对",
    "英文原图底部有淡色“© The Open Group”水印，不影响标签识读"
  ],
  "analyzed_from": [
    "英文 PDF 第 14 页原图（600 dpi 裁切）及 figctx 2x2 放大分块",
    "英文 PDF 第 14 页正文",
    "中文稿 G206e_组织映射.md 第 142–172 行",
    "figs/zh/g206e_fig3-1_zh.png 与 figs/zh/g206e_fig3-1_zh.svg 的文本/画面",
    "figs/g206e_fig3-1_en.png（自动相似度 0.987）"
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
