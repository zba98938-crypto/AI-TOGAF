# G206/fig3-2 · 通用组织地图

> 当前图示解析：[Markdown](../../architecture/diagrams/G206/fig3-2.md) · [JSON](../../architecture/diagrams/G206/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G206e.pdf`；SHA-256：`5de1a634ef389e88b16b11454fdf96350ab33664468a0df2a6aed513e2270c35`。

## 原图 · PDF 第 15 页

![英文原图](../assets/G206/fig3-2-p0015.png)

PDF 坐标：`[48.2, 36.0, 563.8, 324.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
The Oy
Temp
Staffing
Network
Provider
Board of
Directors
Human
Facilities
Resources
Key
Engi
ing
Employe
Final
Union
&
min
Finance
Quality
Assurance
ABC
Corporation
Department
supply
ain
Ad
ertising
Marketing
Product
Agencies
Design Board
Collaborative
Team
Public
Product
Relations
Suppliers
Agen
Warehouse
```

## 概要（历史解释；局部修正见上）

以企业为中心，用五色椭圆和箭头把业务单元、部门、外部伙伴与协作团队连成一张工作关系网。

## 目的（历史解释；局部修正见上）

给出组织地图的“通用模板”：在同一张图里同时容纳企业内部单元、外部伙伴和跨单元协作团队，并用颜色区分组织单元类型，从而直观说明组织地图比组织架构图画得更宽、更深。

## 阅读顺序（历史解释；局部修正见上）

从中央蓝色椭圆 ABC Corporation 读起，它表示地图范围；向外先看绿色业务单元（财务与行政、工程、供应链、市场），再沿箭头看紫色部门、橙色外部伙伴和灰色协作团队。先按颜色判断类型，再按箭头判断工作关系。

## 关键含义（历史解释；局部修正见上）

- 全图 18 个组织单元、5 种类型：1 个企业、4 个业务单元、4 个部门、6 个外部伙伴、3 个协作团队。
- 中央企业椭圆表示地图所要覆盖的整体范围，不只是法律实体名称。
- 4 个业务单元实为职能领域（财务与行政、工程、供应链、市场），说明此处的 business unit 指企业之下的下一层级。
- 部门（紫色）围绕所属业务单元：HR、设施、财务属财务与行政，仓库属供应链；工程与市场没有紫色部门。
- 外部伙伴（橙色）贴近对应业务单元：临时用工与工会连 HR，网络供应商连工程，产品供应商连供应链，广告代理商与公共关系机构连市场。
- 协作团队（灰色）跨单元：董事会连企业，质量保证同时接工程与供应链，产品设计委员会接企业与产品供应商。
- 箭头是工作关系而非汇报线，方向表示“谁向谁发起/提供”，例如人力资源与设施都指向临时用工。

## 层级（历史解释；局部修正见上）

按表 2-1 的类型层级：企业为 L0；业务单元为 L1；部门与外部伙伴同为 L2；协作团队为 L3。图中没有包含框，层级不由嵌套而由颜色和围绕关系表达。

## 线条含义（历史解释；局部修正见上）

深青色曲线箭头，无文字标签，表示组织单元之间的工作关系/互动；箭头指出关系的主动方或提供方。箭头不表示汇报，也不表示数据流或价值流。

## 易误读点（历史解释；局部修正见上）

- 不要把绿色业务单元当作紫色部门的汇报上级；图只画工作关系，未画汇报线。
- 橙色是外部伙伴，不是部门；工会、临时用工、广告代理商都在企业法定边界之外。
- 灰色不是“其他/未分类”，而是跨单元的协作团队。
- 中央椭圆不是总部，而是整张地图的范围。
- 中文重绘 SVG 的连线与方向有多处错误（财务部→广告代理商、产品设计委员会→仓库、产品设计委员会→产品供应商等），不能据它读关系。

## 元素

```json
[
  {
    "id": "abc_corporation",
    "label_en": "ABC Corporation",
    "label_zh": "ABC 公司",
    "type": "organization_unit",
    "parent": null,
    "level": 0,
    "position": "中央",
    "attributes": {
      "org_type": "Enterprise"
    }
  },
  {
    "id": "finance_admin",
    "label_en": "Finance & Admin",
    "label_zh": "财务与行政",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "中左偏上",
    "attributes": {
      "org_type": "Business Unit"
    }
  },
  {
    "id": "engineering",
    "label_en": "Engineering",
    "label_zh": "工程",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "右上",
    "attributes": {
      "org_type": "Business Unit"
    }
  },
  {
    "id": "supply_chain",
    "label_en": "Supply Chain",
    "label_zh": "供应链",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "右中",
    "attributes": {
      "org_type": "Business Unit"
    }
  },
  {
    "id": "marketing",
    "label_en": "Marketing",
    "label_zh": "市场",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "左下",
    "attributes": {
      "org_type": "Business Unit"
    }
  },
  {
    "id": "human_resources",
    "label_en": "Human Resources",
    "label_zh": "人力资源",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "左上",
    "attributes": {
      "org_type": "Department"
    }
  },
  {
    "id": "facilities",
    "label_en": "Facilities",
    "label_zh": "设施",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "上中偏右",
    "attributes": {
      "org_type": "Department"
    }
  },
  {
    "id": "finance",
    "label_en": "Finance",
    "label_zh": "财务",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "左中",
    "attributes": {
      "org_type": "Department"
    }
  },
  {
    "id": "warehouse",
    "label_en": "Warehouse",
    "label_zh": "仓库",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "右下",
    "attributes": {
      "org_type": "Department"
    }
  },
  {
    "id": "temp_staffing",
    "label_en": "Temp Staffing",
    "label_zh": "临时用工",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "左上角",
    "attributes": {
      "org_type": "External Partner"
    }
  },
  {
    "id": "employee_union",
    "label_en": "Employee Union",
    "label_zh": "工会",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "最左",
    "attributes": {
      "org_type": "External Partner"
    }
  },
  {
    "id": "network_provider",
    "label_en": "Network Provider",
    "label_zh": "网络供应商",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "右上角",
    "attributes": {
      "org_type": "External Partner"
    }
  },
  {
    "id": "product_suppliers",
    "label_en": "Product Suppliers",
    "label_zh": "产品供应商",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "中下偏右",
    "attributes": {
      "org_type": "External Partner"
    }
  },
  {
    "id": "advertising_agencies",
    "label_en": "Advertising Agencies",
    "label_zh": "广告代理商",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "左下偏左",
    "attributes": {
      "org_type": "External Partner"
    }
  },
  {
    "id": "public_relations_agency",
    "label_en": "Public Relations Agency",
    "label_zh": "公共关系机构",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "左下角",
    "attributes": {
      "org_type": "External Partner"
    }
  },
  {
    "id": "board_of_directors",
    "label_en": "Board of Directors",
    "label_zh": "董事会",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "position": "上中",
    "attributes": {
      "org_type": "Collaborative Team"
    }
  },
  {
    "id": "quality_assurance",
    "label_en": "Quality Assurance",
    "label_zh": "质量保证",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "position": "右中偏上",
    "attributes": {
      "org_type": "Collaborative Team"
    }
  },
  {
    "id": "product_design_board",
    "label_en": "Product Design Board",
    "label_zh": "产品设计委员会",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "position": "中下",
    "attributes": {
      "org_type": "Collaborative Team"
    }
  }
]
```

## 关系

```json
[
  {
    "from": "abc_corporation",
    "to": "finance_admin",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "企业指向业务单元的工作关系"
  },
  {
    "from": "abc_corporation",
    "to": "engineering",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "abc_corporation",
    "to": "supply_chain",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "abc_corporation",
    "to": "marketing",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "abc_corporation",
    "to": "board_of_directors",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "abc_corporation",
    "to": "product_design_board",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "finance_admin",
    "to": "human_resources",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "finance_admin",
    "to": "facilities",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "finance_admin",
    "to": "finance",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "human_resources",
    "to": "temp_staffing",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "human_resources",
    "to": "employee_union",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "facilities",
    "to": "temp_staffing",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "engineering",
    "to": "network_provider",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "engineering",
    "to": "quality_assurance",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "supply_chain",
    "to": "quality_assurance",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "supply_chain",
    "to": "warehouse",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "product_suppliers",
    "to": "product_design_board",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "product_suppliers",
    "to": "supply_chain",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "marketing",
    "to": "advertising_agencies",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "marketing",
    "to": "public_relations_agency",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色椭圆 Enterprise",
    "meaning_zh": "企业（地图范围）",
    "explicit": true
  },
  {
    "symbol": "绿色椭圆 Business Unit",
    "meaning_zh": "业务单元",
    "explicit": true
  },
  {
    "symbol": "紫色椭圆 Department",
    "meaning_zh": "部门",
    "explicit": true
  },
  {
    "symbol": "橙色椭圆 External Partner",
    "meaning_zh": "外部合作伙伴",
    "explicit": true
  },
  {
    "symbol": "灰蓝色椭圆 Collaborative Team",
    "meaning_zh": "协作团队",
    "explicit": true
  },
  {
    "symbol": "深青色曲线箭头",
    "meaning_zh": "组织单元之间的工作关系，箭头指方向",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中央蓝色企业椭圆；左侧与下方为四个绿色业务单元及其紫色部门、橙色伙伴；上方与右侧为工程/供应链及其伙伴、协作团队；右侧独立一列 Key。"
}
```

## 相关图

```json
[
  {
    "target": "G206/fig7-1",
    "relation": "generalizes",
    "note_zh": "图 3-2 给出与行业无关的通用组织地图模板，图 7-1 用同一套五色记法把它落成全球零售企业实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "所有箭头都没有文字标签，具体语义（工作关系/提供/影响）由图形推断，统一记为 association",
    "“产品设计委员会”与“质量保证”画成灰色协作团队，但英文正文未逐一解释其成员构成",
    "英文页脚与图内左上有“© The Open Group”水印"
  ],
  "analyzed_from": [
    "英文 PDF 第 15 页原图（600 dpi 裁切）及 figctx 2x2 放大分块",
    "英文 PDF 第 14–15 页正文",
    "中文稿 G206e_组织映射.md 第 152–186 行",
    "figs/g206_fig3-2.svg 源码（节点与连线坐标）"
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
