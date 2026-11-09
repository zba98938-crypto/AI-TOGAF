# G21D/fig4-1 · 拟议的一般政府与地方服务部门 L1–L3 要素的结构与内容概览

> 当前图示解析：[Markdown](../../architecture/diagrams/G21D/fig4-1.md) · [JSON](../../architecture/diagrams/G21D/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21De.pdf`；SHA-256：`220ead5fef846c52417b9b7a915ff4a64f327680b384c369840926b85958786a`。

## 原图 · PDF 第 32 页

![英文原图](../assets/G21D/fig4-1-p0032.png)

PDF 坐标：`[74.0, 132.3, 538.0, 359.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
™
The Open Group
Customer Services
Customer Operations
Local Service
Cashiers
Social Security, Benefits,
and Pensions
Social Security
Superintendent Registrar )
‘Community Planning
Tax Forms
)
Business Licenses
Benefits
and Consultation
(
Front Desk
Student Finance
Pensions.
Customer Forums
)
.
(
(imports Administrations
License Applications
Income Support
Community Grants
-
\
Y
(
Planning Applications
(
People Hub
(
Benefits Fraud
Neighbourhood
.
Engagement and
(
Housing Gateway
Workforce Planning
Customer Complaints
Development
Y
Registration Cards
(
Back to Work
Local Law
y
.
```

## 概要（历史解释；局部修正见上）

政府参考模型中“一般政府与地方服务”部门的 L1–L3 分解：1 个部门、3 个功能、26 项服务。

## 目的（历史解释；局部修正见上）

第 4 章开篇用这张图概览“一般政府与地方服务”部门（L1）下的功能（L2）与服务（L3），让读者先看到整个部门的分类结构；随后的表 4-1 逐项给出每个功能与服务的说明。它是图 1-1 三层结构在本部门的具体展开，与其余 10 个部门图采用同一模板，附录 A 第 48 页把它与图 2-1、图 3-1 汇总在同一页。

## 阅读顺序（历史解释；局部修正见上）

最外层浅蓝色大框是 L1 部门，顶部白色粗体字是部门名称。框内三个白色圆角框是 L2 功能，从左到右依次为客户服务、客户运营、地方服务，框顶黑色粗体字是功能名称。每个功能框里的胶囊形小框是 L3 服务。客户服务的服务较多，排成左右两列（左列 7 项、右列 6 项），按表 4-1 的顺序先读左列再读右列，两列地位相同。图中没有连线或箭头，上下级关系完全由框的嵌套表达，同一功能内的服务是并列的。

## 关键含义（历史解释；局部修正见上）

- 本部门分为 3 个 L2 功能：客户服务（13 项服务）、客户运营（7 项）、地方服务（6 项），共 26 项 L3 服务。
- 表 1-1 把本部门写作“一般政府（客户服务、客户运营）与地方服务”：部门名称中的“一般政府”对应左侧两个功能，“地方服务”对应右侧的地方服务功能。
- 按表 4-1 的功能说明：客户服务向服务使用者提供协助与建议，客户运营是直接与公众接触的职能，地方服务是在特定地点或社区内提供的服务。
- 客户服务把多种事务的受理窗口放在一起：出纳、税务表单、前台、进口单证、规划许可、可负担住房购买计划（住房门户）、庇护申请人的登记文书（登记卡）、营业执照、学生贷款与助学金（学生资助）、从事受监管职业所需的许可，以及为这些岗位招聘和培训人员的人员中心与劳动力规划。
- 社会保障、福利、养老金在两个功能里都出现，但分工不同：客户服务下的“社会保障、福利与养老金”处理查询以及申请社会保障号码、福利与养老金计划所需的文书；客户运营下的“社会保障”“福利”“养老金”负责号码分配、资格判定与发放等实际管理。
- 地方服务面向本地社区：登记主管负责本地出生、婚姻、死亡登记，其余服务涉及社区规划与咨询、在线客户论坛、社区补助、邻里参与与发展，以及城镇与区域层面的地方法规。
- 原文称 GRM 穷尽且互斥；图中“Social Security”这一名称在财政部门（图 8-1）的收入功能下再次出现，那里的说明是通过援助措施促进人口福利，与本图的号码分配和保险计划管理不同，阅读时应按所在部门和功能区分同名服务。另外，学生贷款与助学金归在本部门的客户服务下，而不在青少年与教育部门（图 5-1）。

## 层级（历史解释；局部修正见上）

三层严格树形：L1 部门“一般政府与地方服务”（最外层框）→ 3 个 L2 功能（白色圆角框）→ 26 个 L3 服务（胶囊框）。每项服务只属于一个功能，每个功能只属于本部门，对应图 1-1 中“部门—功能—服务”的组成关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。服务框位于功能框内，表示该服务属于该功能；功能框位于部门框内，表示该功能属于本部门（图 1-1 用菱形组合线表示同样的组成关系）。元素清单用 parent/level 记录这种嵌套，因此关系清单为空。

## 易误读点（历史解释；局部修正见上）

- 客户服务框内的左右两列只是排版，不是两个子功能；13 项服务都直接属于客户服务。
- 同一功能内服务的上下次序不表示优先级或流程先后。
- 客户服务下的“社会保障、福利与养老金”与客户运营下的“社会保障”“福利”“养老金”不是重复项：前者是受理与文书，后者是实际管理与发放。
- 图中写“Social Security”，英文原文表 4-1 与中文稿表 4-1 写作“Social Security Administration（社会保障管理）”；图中拼作英式“Neighbourhood”，表中为“Neighborhood”。两处都是原文自身的不一致，元素按图记录。
- 中文稿引用的中文化 PNG 字号混乱（部分服务标签比功能标题还大），不能用字号判断层级，应以框的嵌套为准；该 PNG 还把“邻里参与与发展”写成了“社区参与与发展”。
- 图框下方的浅灰色弧线是 PDF 评估版水印的残影，不属于图的内容。

## 元素

```json
[
  {
    "id": "l1_general_gov_local_services",
    "label_en": "General Government and Local Services",
    "label_zh": "一般政府与地方服务",
    "type": "other",
    "notation_type": "GRM L1 部门（Sector）",
    "parent": null,
    "level": 1,
    "position": "最外层浅蓝色框，标题在顶部居中",
    "description_zh": "GRM 第 1 层“部门”，即政府的一个业务领域；词表没有对应类型，故用 other。表 1-1 写作“一般政府（客户服务、客户运营）与地方服务”。"
  },
  {
    "id": "l2_customer_services",
    "label_en": "Customer Services",
    "label_zh": "客户服务",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_general_gov_local_services",
    "level": 2,
    "order": 1,
    "position": "左（最宽，服务分两列）",
    "description_zh": "向服务使用者提供协助与建议（表 4-1）。"
  },
  {
    "id": "l2_customer_operations",
    "label_en": "Customer Operations",
    "label_zh": "客户运营",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_general_gov_local_services",
    "level": 2,
    "order": 2,
    "position": "中",
    "description_zh": "直接与公众接触的职能（表 4-1）。"
  },
  {
    "id": "l2_local_service",
    "label_en": "Local Service",
    "label_zh": "地方服务",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_general_gov_local_services",
    "level": 2,
    "order": 3,
    "position": "右",
    "description_zh": "在特定地点或社区内提供服务（表 4-1）。"
  },
  {
    "id": "l3_cashiers",
    "label_en": "Cashiers",
    "label_zh": "出纳柜台",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 1,
    "position": "左列第 1 项",
    "description_zh": "负责处理来访咨询和一般文书事务的人员。"
  },
  {
    "id": "l3_tax_forms",
    "label_en": "Tax Forms",
    "label_zh": "税务表单",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 2,
    "position": "左列第 2 项",
    "description_zh": "向纳税人和免税组织提供申报财务信息的表单。"
  },
  {
    "id": "l3_front_desk",
    "label_en": "Front Desk",
    "label_zh": "前台",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 3,
    "position": "左列第 3 项"
  },
  {
    "id": "l3_imports_admin",
    "label_en": "Imports Administrations",
    "label_zh": "进口管理",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 4,
    "position": "左列第 4 项",
    "description_zh": "海外货物入境所需进口单证的收集、准备与咨询。"
  },
  {
    "id": "l3_planning_applications",
    "label_en": "Planning Applications",
    "label_zh": "规划申请",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 5,
    "position": "左列第 5 项",
    "description_zh": "在土地上建造或改变土地用途所需规划许可的管理与文书。"
  },
  {
    "id": "l3_housing_gateway",
    "label_en": "Housing Gateway",
    "label_zh": "住房门户",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 6,
    "position": "左列第 6 项",
    "description_zh": "可负担住房购买计划的运营、资格判定与申请评估。"
  },
  {
    "id": "l3_registration_cards",
    "label_en": "Registration Cards",
    "label_zh": "登记卡",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 7,
    "position": "左列第 7 项",
    "description_zh": "庇护申请人的整体管理与文书工作（表 4-1）。"
  },
  {
    "id": "l3_ss_benefits_pensions",
    "label_en": "Social Security, Benefits, and Pensions",
    "label_zh": "社会保障、福利与养老金",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 8,
    "position": "右列第 1 项",
    "description_zh": "处理相关查询以及申请社会保障号码、福利与养老金计划所需的文书；实际管理在客户运营下。"
  },
  {
    "id": "l3_business_licenses",
    "label_en": "Business Licenses",
    "label_zh": "营业执照",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 9,
    "position": "右列第 2 项",
    "description_zh": "办理创办企业申请的流程。"
  },
  {
    "id": "l3_student_finance",
    "label_en": "Student Finance",
    "label_zh": "学生资助",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 10,
    "position": "右列第 3 项",
    "description_zh": "学生贷款与助学金的提供与管理。"
  },
  {
    "id": "l3_license_applications",
    "label_en": "License Applications",
    "label_zh": "许可申请",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 11,
    "position": "右列第 4 项",
    "description_zh": "从事受监管角色所需书面授权的管理与文书。"
  },
  {
    "id": "l3_people_hub",
    "label_en": "People Hub",
    "label_zh": "人员中心",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 12,
    "position": "右列第 5 项",
    "description_zh": "客户服务与运营岗位人员的招聘、行政与培训。"
  },
  {
    "id": "l3_workforce_planning",
    "label_en": "Workforce Planning",
    "label_zh": "劳动力规划",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_services",
    "level": 3,
    "order": 13,
    "position": "右列第 6 项"
  },
  {
    "id": "l3_social_security",
    "label_en": "Social Security",
    "label_zh": "社会保障",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 1,
    "description_zh": "分配社会保障号码，管理退休、遗属与伤残保险计划。表 4-1 中此项写作 Social Security Administration（社会保障管理）。",
    "attributes": {
      "table_label_en": "Social Security Administration"
    }
  },
  {
    "id": "l3_benefits",
    "label_en": "Benefits",
    "label_zh": "福利",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 2,
    "description_zh": "各类福利的提供与资格判定。"
  },
  {
    "id": "l3_pensions",
    "label_en": "Pensions",
    "label_zh": "养老金",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 3,
    "description_zh": "定期发放固定款项，支持公民退休生活。"
  },
  {
    "id": "l3_income_support",
    "label_en": "Income Support",
    "label_zh": "收入补助",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 4
  },
  {
    "id": "l3_benefits_fraud",
    "label_en": "Benefits Fraud",
    "label_zh": "福利欺诈",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 5,
    "description_zh": "调查与处理冒领福利。"
  },
  {
    "id": "l3_customer_complaints",
    "label_en": "Customer Complaints",
    "label_zh": "客户投诉",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 6
  },
  {
    "id": "l3_back_to_work",
    "label_en": "Back to Work",
    "label_zh": "重返工作岗位",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_customer_operations",
    "level": 3,
    "order": 7,
    "description_zh": "为职业中断后希望重返工作的人提供指导与支持。"
  },
  {
    "id": "l3_superintendent_registrar",
    "label_en": "Superintendent Registrar",
    "label_zh": "登记主管",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_local_service",
    "level": 3,
    "order": 1,
    "description_zh": "监督本地出生、婚姻与死亡登记。"
  },
  {
    "id": "l3_community_planning_consultation",
    "label_en": "Community Planning and Consultation",
    "label_zh": "社区规划与咨询",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_local_service",
    "level": 3,
    "order": 2
  },
  {
    "id": "l3_customer_forums",
    "label_en": "Customer Forums",
    "label_zh": "客户论坛",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_local_service",
    "level": 3,
    "order": 3,
    "description_zh": "用于整合社区、分享反馈的在线渠道。"
  },
  {
    "id": "l3_community_grants",
    "label_en": "Community Grants",
    "label_zh": "社区补助",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_local_service",
    "level": 3,
    "order": 4
  },
  {
    "id": "l3_neighbourhood_engagement",
    "label_en": "Neighbourhood Engagement and Development",
    "label_zh": "邻里参与与发展",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_local_service",
    "level": 3,
    "order": 5,
    "description_zh": "表 4-1 拼作 Neighborhood；中文化 PNG 误作“社区参与与发展”。",
    "attributes": {
      "table_label_en": "Neighborhood Engagement and Development"
    }
  },
  {
    "id": "l3_local_law",
    "label_en": "Local Law",
    "label_zh": "地方法规",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_local_service",
    "level": 3,
    "order": 6,
    "description_zh": "在城镇与区域层面提供法律建议并执行法律程序。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色大圆角框 + 顶部白色粗体标题",
    "meaning_zh": "L1 部门（Sector）",
    "explicit": false
  },
  {
    "symbol": "白色圆角框 + 黑色粗体标题",
    "meaning_zh": "L2 功能（Function），属于所在部门",
    "explicit": false
  },
  {
    "symbol": "白色胶囊形小框（细灰边）",
    "meaning_zh": "L3 服务（Service），属于所在功能",
    "explicit": false
  },
  {
    "symbol": "框的嵌套",
    "meaning_zh": "组成/归属关系，与图 1-1 中菱形组合线表达的“部门—功能—服务”关系相同",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "最外层浅蓝色圆角框（顶部居中为部门标题，右上角为版权署名）内，三个功能框从左到右并排：客户服务（最宽，服务分左右两列，左列 7 项、右列 6 项）、客户运营（7 项）、地方服务（6 项）；各功能框内服务自上而下排列。"
}
```

## 相关图

```json
[
  {
    "target": "G21D/fig1-1",
    "relation": "detail_of",
    "note_zh": "图 1-1 的三层结构（L1 部门—L2 功能—L3 服务）在“一般政府与地方服务”部门的展开"
  },
  {
    "target": "G21D/fig5-1",
    "relation": "complements",
    "note_zh": "同一模板的相邻部门概览（青少年与教育）；学生贷款与助学金归在本图的客户服务下，而不在图 5-1"
  },
  {
    "target": "G21D/fig8-1",
    "relation": "related",
    "note_zh": "“Social Security”同时出现在本图客户运营和图 8-1 收入功能下；本图的养老金发放、进口单证受理与图 8-1 的养老基金管理、进口关税分属不同部门"
  },
  {
    "target": "G21D/appA-p48",
    "relation": "related",
    "note_zh": "附录 A 第 48 页（PDF 第 68 页）原样收录本图，与图 2-1、图 3-1 同页"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "L3 的 order 按表 4-1 的顺序给出（客户服务框先左列后右列），原图本身没有编号。"
  ],
  "analyzed_from": [
    "英文 PDF 第 32 页原图截图及 3×3 放大分块（核对 Neighbourhood 拼写）",
    "英文 PDF 第 21–24 页（1.3–1.4 节）与第 32–34 页（第 4 章开篇、表 4-1）正文",
    "英文 PDF 第 68 页附录 A 图示（同内容面板）",
    "中文稿 G21De_政府参考模型.md 第 150–205 行、第 355–432 行",
    "figs/zh/g21de_fig4-1_zh.png（逐项对照）"
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
