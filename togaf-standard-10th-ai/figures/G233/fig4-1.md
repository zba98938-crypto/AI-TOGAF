# G233/fig4-1 · 零售公司组织架构图

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig4-1.md) · [JSON](../../architecture/diagrams/G233/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G233/fig4-1-p0023.png)

PDF 坐标：`[74.0, 36.0, 538.0, 250.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
fas}
Retail Organization
Finance
@Q
Supply Chain
oa
Sales
oa
Human Resources ©
Management
Accounts Payable cD
Purchasing
@®
Retail Stores =
Talent Management cD
Region A
fa}
Accounts.
oO
Warehouse
Management
Recruiting
fa}
Region B
fae}
Cash
@
Clothing
Management
Warehouses
Region C
fas}
Payroll
fas}
Accounts CD)
Electonics
Region D
fas}
Receivable
Warehouses
‘Accounts CD)
Distribution
Internet Store
```

## 概要（历史解释；局部修正见上）

用嵌套的 ArchiMate 利益相关者框，展示零售组织四个职能领域及其下属部门的汇报层级。

## 目的（历史解释；局部修正见上）

第 4 章“做好功课”的第一个输入是组织结构。作者用它说明组织单元常与业务能力高度对齐（人员执行流程、分配资金/IT/资产），因此组织架构可以启发能力目录；同时用零售示例演示哪些层级能启发目录、哪些不能，以及组织架构比能力更易变、应避免名称一一对应。

## 阅读顺序（历史解释；局部修正见上）

从最外层“Retail Organization”读起，向下是四个并列的职能域（Finance、Supply Chain Management、Sales、Human Resources），再向下是部门与更小单元。框套框＝组织上的隶属/汇报关系，不是流程先后；外层颜色最深、越往里越浅。每个框右上角的小图标表示它是 ArchiMate 利益相关者元素。

## 关键含义（历史解释；局部修正见上）

- 全组织分四个主要职能域：财务、供应链管理、销售、人力资源；每个域下有更小的部门向上级汇报，纵向最多到第四层（组织→职能域→部门→区域/仓库）。
- 财务域顶层有两个直接下属：Accounts Payable 与 Accounts Receivable 部门；Accounts Receivable 部门内又设 Cash Management、Accounts Receivable、Accounts Payable 三个职能。
- 正文明确指出：财务下的现金管理、应收账款、应付账款三项职能，对多数组织而言就是业务能力，因此财务域可以直接启发能力目录。
- 仓库管理按产品划分（服装仓库、电子产品仓库），零售门店按地域划分（Region A–D）；这两种划分反映地理/产品维度，正文说这些领域的组织层级不能为能力目录提供启示。
- 人力资源域下有 Talent Management、Recruiting、Payroll 三个单元，是典型的“部门名≈能力名”情形；正文提醒应尽量避免让业务单元名称与业务能力名称紧密对应。
- 组织架构只用于“指示能力可能存在的位置”，不能替代能力目录；组织结构比业务能力更易变，二者只是有对齐、并不完全对齐。
- 图中每个职能域（包括白色容器）在模型里都是 ArchiMate 利益相关者，隶属关系通过把下级利益相关者嵌套进上级来表达。

## 层级（历史解释；局部修正见上）

四层。L0 Retail Organization；L1 四个职能域 Finance、Supply Chain Management、Sales、Human Resources；L2 部门：Finance 下 Accounts Payable、Accounts Receivable，Supply Chain Management 下 Purchasing、Warehouse Management、Distribution，Sales 下 Retail Stores、Internet Store，Human Resources 下 Talent Management、Recruiting、Payroll；L3：Accounts Receivable 部门下的 Cash Management、Accounts Receivable、Accounts Payable，Warehouse Management 下的 Clothing/Electronics Warehouses，Retail Stores 下的 Region A–D。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线；全部层级由框的嵌套（视觉包含）表达，嵌套方向即“下级隶属于上级”的汇报关系。关系清单把这 23 条隶属关系补记为隐式的 reports_to。

## 易误读点（历史解释；局部修正见上）

- 不要把嵌套读成流程顺序或价值流阶段；它只是组织汇报层级。
- 不要把 Warehouse Management 下的服装/电子产品仓库当成两个业务能力；它们是按产品划分的仓库单元，正文明确说这一层不能启发能力目录。
- 不要把 Retail Stores 下的 Region A–D 当成能力分层；它们是地域单元。
- 不要把两个 Accounts Receivable、两个 Accounts Payable 当成重复绘制错误；原图确实同名嵌套（部门与其职能同名），中文 PNG 也保留了这个重复。
- 四个职能域是白色容器而非紫色框，容易被误认为普通分组；正文说明它们在模型中仍是利益相关者。
- 不要据此认为组织架构可以一一映射为能力目录；正文强调两者只是“有对齐、但不完全对齐”。

## 元素

```json
[
  {
    "id": "org_retail",
    "label_en": "Retail Organization",
    "label_zh": "零售组织",
    "type": "organization_unit",
    "parent": null,
    "level": 0,
    "position": "最外层深紫大框",
    "notation_type": "ArchiMate Stakeholder（容器）"
  },
  {
    "id": "fin",
    "label_en": "Finance",
    "label_zh": "财务",
    "type": "organization_unit",
    "parent": "org_retail",
    "level": 1,
    "order": 1,
    "position": "第一列（白容器）",
    "notation_type": "ArchiMate Stakeholder（容器）"
  },
  {
    "id": "fin_ap",
    "label_en": "Accounts Payable",
    "label_zh": "应付账款",
    "type": "organization_unit",
    "parent": "fin",
    "level": 2,
    "order": 1,
    "position": "财务列顶部"
  },
  {
    "id": "fin_ar_dept",
    "label_en": "Accounts Receivable",
    "label_zh": "应收账款",
    "type": "organization_unit",
    "parent": "fin",
    "level": 2,
    "order": 2,
    "position": "财务列中部（紫色大框）",
    "description_zh": "作为部门容器，框内又含一个同名“Accounts Receivable”职能；原图如此。"
  },
  {
    "id": "fin_cash",
    "label_en": "Cash Management",
    "label_zh": "现金管理",
    "type": "organization_unit",
    "parent": "fin_ar_dept",
    "level": 3,
    "order": 1
  },
  {
    "id": "fin_ar_func",
    "label_en": "Accounts Receivable",
    "label_zh": "应收账款",
    "type": "organization_unit",
    "parent": "fin_ar_dept",
    "level": 3,
    "order": 2
  },
  {
    "id": "fin_ap_func",
    "label_en": "Accounts Payable",
    "label_zh": "应付账款",
    "type": "organization_unit",
    "parent": "fin_ar_dept",
    "level": 3,
    "order": 3,
    "description_zh": "与财务列顶部的 Accounts Payable 同名，但属于应收账款部门内的职能单元。"
  },
  {
    "id": "scm",
    "label_en": "Supply Chain Management",
    "label_zh": "供应链管理",
    "type": "organization_unit",
    "parent": "org_retail",
    "level": 1,
    "order": 2,
    "position": "第二列（白容器）",
    "notation_type": "ArchiMate Stakeholder（容器）"
  },
  {
    "id": "scm_purchasing",
    "label_en": "Purchasing",
    "label_zh": "采购",
    "type": "organization_unit",
    "parent": "scm",
    "level": 2,
    "order": 1
  },
  {
    "id": "scm_warehouse",
    "label_en": "Warehouse Management",
    "label_zh": "仓库管理",
    "type": "organization_unit",
    "parent": "scm",
    "level": 2,
    "order": 2
  },
  {
    "id": "scm_wh_clothing",
    "label_en": "Clothing Warehouses",
    "label_zh": "服装仓库",
    "type": "organization_unit",
    "parent": "scm_warehouse",
    "level": 3,
    "order": 1
  },
  {
    "id": "scm_wh_electronics",
    "label_en": "Electronics Warehouses",
    "label_zh": "电子产品仓库",
    "type": "organization_unit",
    "parent": "scm_warehouse",
    "level": 3,
    "order": 2
  },
  {
    "id": "scm_distribution",
    "label_en": "Distribution",
    "label_zh": "分销",
    "type": "organization_unit",
    "parent": "scm",
    "level": 2,
    "order": 3
  },
  {
    "id": "sales",
    "label_en": "Sales",
    "label_zh": "销售",
    "type": "organization_unit",
    "parent": "org_retail",
    "level": 1,
    "order": 3,
    "position": "第三列（白容器）",
    "notation_type": "ArchiMate Stakeholder（容器）"
  },
  {
    "id": "sales_stores",
    "label_en": "Retail Stores",
    "label_zh": "零售门店",
    "type": "organization_unit",
    "parent": "sales",
    "level": 2,
    "order": 1
  },
  {
    "id": "region_a",
    "label_en": "Region A",
    "label_zh": "区域 A",
    "type": "organization_unit",
    "parent": "sales_stores",
    "level": 3,
    "order": 1
  },
  {
    "id": "region_b",
    "label_en": "Region B",
    "label_zh": "区域 B",
    "type": "organization_unit",
    "parent": "sales_stores",
    "level": 3,
    "order": 2
  },
  {
    "id": "region_c",
    "label_en": "Region C",
    "label_zh": "区域 C",
    "type": "organization_unit",
    "parent": "sales_stores",
    "level": 3,
    "order": 3
  },
  {
    "id": "region_d",
    "label_en": "Region D",
    "label_zh": "区域 D",
    "type": "organization_unit",
    "parent": "sales_stores",
    "level": 3,
    "order": 4
  },
  {
    "id": "sales_internet",
    "label_en": "Internet Store",
    "label_zh": "网上商店",
    "type": "organization_unit",
    "parent": "sales",
    "level": 2,
    "order": 2
  },
  {
    "id": "hr",
    "label_en": "Human Resources",
    "label_zh": "人力资源",
    "type": "organization_unit",
    "parent": "org_retail",
    "level": 1,
    "order": 4,
    "position": "第四列（白容器）",
    "notation_type": "ArchiMate Stakeholder（容器）"
  },
  {
    "id": "hr_talent",
    "label_en": "Talent Management",
    "label_zh": "人才管理",
    "type": "organization_unit",
    "parent": "hr",
    "level": 2,
    "order": 1
  },
  {
    "id": "hr_recruiting",
    "label_en": "Recruiting",
    "label_zh": "招聘",
    "type": "organization_unit",
    "parent": "hr",
    "level": 2,
    "order": 2
  },
  {
    "id": "hr_payroll",
    "label_en": "Payroll",
    "label_zh": "薪资",
    "type": "organization_unit",
    "parent": "hr",
    "level": 2,
    "order": 3
  }
]
```

## 关系

```json
[
  {
    "from": "fin",
    "to": "org_retail",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "财务嵌套在零售组织内，向上汇报。"
  },
  {
    "from": "scm",
    "to": "org_retail",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "sales",
    "to": "org_retail",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "hr",
    "to": "org_retail",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "fin_ap",
    "to": "fin",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "fin_ar_dept",
    "to": "fin",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "fin_cash",
    "to": "fin_ar_dept",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "fin_ar_func",
    "to": "fin_ar_dept",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "fin_ap_func",
    "to": "fin_ar_dept",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "scm_purchasing",
    "to": "scm",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "scm_warehouse",
    "to": "scm",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "scm_distribution",
    "to": "scm",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "scm_wh_clothing",
    "to": "scm_warehouse",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "scm_wh_electronics",
    "to": "scm_warehouse",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "sales_stores",
    "to": "sales",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "sales_internet",
    "to": "sales",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "region_a",
    "to": "sales_stores",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "region_b",
    "to": "sales_stores",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "region_c",
    "to": "sales_stores",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "region_d",
    "to": "sales_stores",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "hr_talent",
    "to": "hr",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "hr_recruiting",
    "to": "hr",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "hr_payroll",
    "to": "hr",
    "type": "reports_to",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深紫大框 + 双人图标",
    "meaning_zh": "最高层组织（Retail Organization）",
    "explicit": false
  },
  {
    "symbol": "白色容器框 + 双人图标",
    "meaning_zh": "职能域（ArchiMate 利益相关者，浅色表示层级较高）",
    "explicit": false
  },
  {
    "symbol": "紫色八边形/圆角框 + 双人图标",
    "meaning_zh": "部门或下属组织单元（越深层的紫色越浅）",
    "explicit": false
  },
  {
    "symbol": "框套框",
    "meaning_zh": "组织隶属/汇报关系（下级嵌套在上级内）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "最外层是 Retail Organization 大框；内部横向并排四个职能域容器（白底、紫色利益相关者图标）；每个容器内自上而下排列部门框，部门框内再纵向排列更小单元；财务列最高（4 层），人力资源列只有 2 层。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig6-1",
    "relation": "related",
    "note_zh": "图 6-1 的能力目录把财务、人力资源、库存等职能重新分组为 Retail Storefront / Strategic / Operations (Core)，与本图的组织视角互补而非一一对应"
  },
  {
    "target": "G233/fig6-3",
    "relation": "related",
    "note_zh": "图 6-3 的能力实例由组织中的角色实际执行（如财务分析师、招聘经理），组织结构是能力实例的资源来源"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "财务域中“Accounts Receivable”部门框与其内同名单元、以及两处“Accounts Payable”在原图重复出现，无法仅凭图判断是刻意表示“部门与职能同名”还是建模疏忽；本分析按嵌套层级照录。",
    "四个职能域使用白色容器而非紫色框，是否属于 ArchiMate 的 Group 元素无法仅凭图确认；正文明确称每个职能域表示为利益相关者，故按组织单元/利益相关者记录。",
    "Accounts Receivable 部门下同时出现 Cash Management、Accounts Receivable、Accounts Payable 三个职能（应付账款挂在应收账款部门下），业务上略反常；原图如此，本分析按画面照录。",
    "图中没有连线，23 条汇报关系全部由嵌套推断（explicit:false）。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页图 4-1 截图（figctx 裁剪）与 2×2 放大分块",
    "英文 PDF 第 22–23 页正文",
    "中文稿 G233e_业务能力规划.md 第 186–226 行（含 22 条图内标签对照）",
    "figs/g233e_fig4-1_en.png 与 figs/zh/g233e_fig4-1_zh.png"
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
