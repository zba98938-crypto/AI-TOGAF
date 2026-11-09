# G21B/fig5-3 · C-MDM 详细业务功能参考模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig5-3.md) · [JSON](../../architecture/diagrams/G21B/fig5-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 41 页

![英文原图](../assets/G21B/fig5-3-p0041.png)

PDF 坐标：`[48.2, 62.3, 563.8, 460.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
‘Customer-MDM Team
Business Data Owner
Data Steward
Architect
Data Manager
z
gz
(C-MDM Capabilities Management and Governance
A
Define C-MDM
Define and Onboard
Define and Operate (4)
Coordinate Decision- (9)
Define Team Services. (9)
Objectives and
Data Owners and Data
Data Governance
Making and
and Operate SLAS
Roadmaps
Stewards
Principles
Prioritization
External Data
C-MDM Design
Aa
Data Quality and
‘Acquisition
Busit
sss Value
Design Customer Data Models (2)
Design C-MDM Architecture (3)
Support Customer Data (9)
Measurement
Principles and Ensure
Management
Consistency of Data Solutions
Implementations.
Analyze the Data
Market and Identify
‘Opportunities
Formalize Customer Master Data (9)
Help Businesses to Adapt (A)
Define and Operate Data (9)
Validation Workflos, Quality, and
their Processes to Ensure
‘Access Model
Business Rules
Data Quality
Build & Deliver
Reports on
Define, Maintain, and Share Customer Data Documentations (9)
Define, Follow, and Monitor Data (A)
Customer Data
(Data Dictionaries, Glossaries, Models)
Retention Rules
Set Up a Date
a
Quality and
Partnership
Evolutions.
C-MDM Operation
Aa
Receive and Manage
‘Assess and Manage Master
Correct Data Issues
A
Requests about Customer
Customer Data Quality
Issues
Data (GDPR, etc.)
Report C-MDM
Validate Customer Merges (9)
Business Value
Leverage C-MDM Services in Operational Business Processes
Purchase Extemal (9)
Customer Data
A
Extension of C-MDM Scope and Usages
Aa
‘Support New Integration of
‘Support New External
Support New Integration ()
of a Data Consumer
Data Produce Application
Data Source Integration
Application
Communication
‘Communicate about C-
Communicate the
Communicate about
MOM Value and Curent
Customer Data Team
Customer Data Quality
Usage
Services Catalog
```

## 概要（历史解释；局部修正见上）

把 C-MDM 团队的业务功能分解为 7 组 29 项，并标明 4 类角色。

## 目的（历史解释；局部修正见上）

第 5.2 节给出可复用的详细参考模型：组织可以用它对照自己的 C-MDM 业务功能覆盖度、设计目标组织与职责，或作为供应商/方案评估的清单。图 5-3 是业务侧的全景分解，逐项说明见表 5-3。

## 阅读顺序（历史解释；局部修正见上）

先看顶部：Customer-MDM Team 是一个业务参与者容器，里面并排 4 个角色——数据经理、业务数据所有者、数据管家、架构师，他们共同承担下面的功能。再看 7 个浅黄分组：能力管理与治理（横向横跨顶部）、外部客户数据获取（左列）、C-MDM 设计（中部最大）、C-MDM 运营、范围与用途扩展、数据质量与业务价值度量（右列）、沟通（底部横贯）。每组内的圆角框是具体业务功能，组框只表示归类，不表示流程顺序。

## 关键含义（历史解释；局部修正见上）

- 7 个功能组：C-MDM 能力管理与治理（5 项）、外部客户数据获取（3 项）、C-MDM 设计（8 项）、C-MDM 运营（5 项）、C-MDM 范围与用途扩展（3 项）、数据质量与业务价值度量（2 项）、沟通（3 项），合计 29 项。
- 能力管理与治理组负责定目标与路线图、吸纳数据所有者/数据管家、定义并运行数据治理原则、协调决策与优先级、定义团队服务并运营 SLA——是唯一直接面向治理与赞助的组。
- C-MDM 设计组最大（8 项），覆盖数据模型、架构原则与数据方案一致性、实施支持、校验工作流/质量/业务规则、帮助业务调整流程、数据访问模型、文档（数据字典/术语表/模型）与数据保留规则。
- C-MDM 运营组负责接收并管理客户数据请求（GDPR 等）、评估与处理质量问题、纠正数据、校验合并，并在运营业务流程中利用 C-MDM 服务。
- 外部客户数据获取组是独立的左列，说明“买数据/建伙伴关系/分析数据市场”被当作 C-MDM 团队的常设业务功能，而不是一次性项目。
- 范围与用途扩展组只处理“新集成”：数据生产方应用、数据消费方应用、外部数据源；与运营组的“日常服务”区分开。
- 数据质量与业务价值度量组只有两项：构建并交付客户数据质量/演进报告、报告 C-MDM 业务价值；与沟通组（3 项）一起构成“向组织证明价值”的功能。
- 4 个角色不是按功能组一对一分配的：同一角色会参与多个组（如数据管家参与治理、设计、运营），图中不做角色—功能映射。

## 层级（历史解释；局部修正见上）

三层：第 1 层 Customer-MDM Team（业务参与者容器）；第 2 层 7 个业务功能分组 + 4 个角色；第 3 层各组内的具体业务功能（29 项）。角色与功能组并列位于第 2 层，图中不表示谁负责哪项功能。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。分组关系由浅黄大框的包含表达；角色与功能的归属由“同处 Customer-MDM Team 容器内”表达；功能组之间的上下左右位置不表示流程顺序或依赖。

## 易误读点（历史解释；局部修正见上）

- 不要把 7 个功能组读成流程的 7 个步骤：它们是功能分类，可以并行存在。
- “外部客户数据获取”在左列独立成组，不代表它在时间上先于设计或运营。
- “C-MDM 设计”组里的“支持客户数据管理实施”“帮助业务调整其流程”仍是业务功能，不是项目管理或变革管理的完整方法。
- 角色（数据经理、业务数据所有者、数据管家、架构师）不是功能组的下级；他们与功能组并列，具体分工需结合表 5-3 与组织设计。
- 中文稿引用的中文化 PNG 有多个标签被缩小并加了灰底，不要据此判断这些功能次要；原图所有功能同级同字号。

## 元素

```json
[
  {
    "id": "team",
    "label_en": "Customer-MDM Team",
    "label_zh": "客户主数据管理团队",
    "type": "organization_unit",
    "parent": null,
    "level": 1
  },
  {
    "id": "role_data_manager",
    "label_en": "Data Manager",
    "label_zh": "数据经理",
    "type": "role",
    "parent": "team",
    "level": 2
  },
  {
    "id": "role_data_owner",
    "label_en": "Business Data Owner",
    "label_zh": "业务数据所有者",
    "type": "role",
    "parent": "team",
    "level": 2
  },
  {
    "id": "role_steward",
    "label_en": "Data Steward",
    "label_zh": "数据管家",
    "type": "role",
    "parent": "team",
    "level": 2
  },
  {
    "id": "role_architect",
    "label_en": "Architect",
    "label_zh": "架构师",
    "type": "role",
    "parent": "team",
    "level": 2
  },
  {
    "id": "g_gov",
    "label_en": "C-MDM Capabilities Management and Governance",
    "label_zh": "C-MDM 能力管理与治理",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "g_ext",
    "label_en": "External Data Acquisition",
    "label_zh": "外部客户数据获取",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "g_design",
    "label_en": "C-MDM Design",
    "label_zh": "C-MDM 设计",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "g_operation",
    "label_en": "C-MDM Operation",
    "label_zh": "C-MDM 运营",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "g_extension",
    "label_en": "Extension of C-MDM Scope and Usages",
    "label_zh": "C-MDM 范围与用途扩展",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "g_dq",
    "label_en": "Data Quality and Business Value Measurement",
    "label_zh": "数据质量与业务价值度量",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "g_comm",
    "label_en": "Communication",
    "label_zh": "沟通",
    "type": "group",
    "parent": null,
    "level": 2
  },
  {
    "id": "f_objectives",
    "label_en": "Define C-MDM Objectives and Roadmaps",
    "label_zh": "定义 C-MDM 目标与路线图",
    "type": "function",
    "parent": "g_gov",
    "level": 3
  },
  {
    "id": "f_onboard_owners",
    "label_en": "Define and Onboard Data Owners and Data Stewards",
    "label_zh": "定义并吸纳数据所有者与数据管家",
    "type": "function",
    "parent": "g_gov",
    "level": 3
  },
  {
    "id": "f_governance_principles",
    "label_en": "Define and Operate Data Governance Principles",
    "label_zh": "定义并运行数据治理原则",
    "type": "function",
    "parent": "g_gov",
    "level": 3
  },
  {
    "id": "f_decisions",
    "label_en": "Coordinate Decision-Making and Prioritization",
    "label_zh": "协调决策与优先级",
    "type": "function",
    "parent": "g_gov",
    "level": 3
  },
  {
    "id": "f_team_services",
    "label_en": "Define Team Services and Operate SLAs",
    "label_zh": "定义团队服务并运营 SLA",
    "type": "function",
    "parent": "g_gov",
    "level": 3
  },
  {
    "id": "f_market",
    "label_en": "Analyze the Data Market and Identify Opportunities",
    "label_zh": "分析数据市场并识别机会",
    "type": "function",
    "parent": "g_ext",
    "level": 3
  },
  {
    "id": "f_partnership",
    "label_en": "Set Up a Date Partnership",
    "label_zh": "建立数据伙伴关系",
    "type": "function",
    "parent": "g_ext",
    "level": 3,
    "description_zh": "英文原图写作 Date（应为 Data），中文稿标签表沿用原拼写。"
  },
  {
    "id": "f_purchase",
    "label_en": "Purchase External Customer Data",
    "label_zh": "采购外部客户数据",
    "type": "function",
    "parent": "g_ext",
    "level": 3
  },
  {
    "id": "f_data_models",
    "label_en": "Design Customer Data Models",
    "label_zh": "设计客户数据模型",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_arch_principles",
    "label_en": "Design C-MDM Architecture Principles and Ensure Consistency of Data Solutions",
    "label_zh": "设计 C-MDM 架构原则并确保数据方案一致性",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_support_impl",
    "label_en": "Support Customer Data Management Implementations",
    "label_zh": "支持客户数据管理实施",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_validation",
    "label_en": "Formalize Customer Master Data Validation Workflows, Quality, and Business Rules",
    "label_zh": "形式化客户主数据校验工作流、质量与业务规则",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_adapt_processes",
    "label_en": "Help Businesses to Adapt their Processes to Ensure Data Quality",
    "label_zh": "帮助业务调整其流程以确保数据质量",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_access_model",
    "label_en": "Define and Operate Data Access Model",
    "label_zh": "定义并运行数据访问模型",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_documentation",
    "label_en": "Define, Maintain, and Share Customer Data Documentations (Data Dictionaries, Glossaries, Models)",
    "label_zh": "定义、维护并共享客户数据文档（数据字典、术语表、模型）",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_retention",
    "label_en": "Define, Follow, and Monitor Data Retention Rules",
    "label_zh": "定义、遵循并监控数据保留规则",
    "type": "function",
    "parent": "g_design",
    "level": 3
  },
  {
    "id": "f_requests",
    "label_en": "Receive and Manage Requests about Customer Data (GDPR, etc.)",
    "label_zh": "接收并管理客户数据相关请求（GDPR 等）",
    "type": "function",
    "parent": "g_operation",
    "level": 3
  },
  {
    "id": "f_quality_issues",
    "label_en": "Assess and Manage Master Customer Data Quality Issues",
    "label_zh": "评估并管理客户主数据质量问题",
    "type": "function",
    "parent": "g_operation",
    "level": 3
  },
  {
    "id": "f_correct",
    "label_en": "Correct Data Issues",
    "label_zh": "纠正数据问题",
    "type": "function",
    "parent": "g_operation",
    "level": 3
  },
  {
    "id": "f_merges",
    "label_en": "Validate Customer Merges",
    "label_zh": "校验客户合并",
    "type": "function",
    "parent": "g_operation",
    "level": 3
  },
  {
    "id": "f_leverage",
    "label_en": "Leverage C-MDM Services in Operational Business Processes",
    "label_zh": "运营流程中利用 C-MDM 服务",
    "type": "function",
    "parent": "g_operation",
    "level": 3
  },
  {
    "id": "f_new_producer",
    "label_en": "Support New Integration of Data Produce Application",
    "label_zh": "支持新集成：数据生产方应用",
    "type": "function",
    "parent": "g_extension",
    "level": 3,
    "description_zh": "原文 Produce 为 Producer 的笔误。"
  },
  {
    "id": "f_new_consumer",
    "label_en": "Support New Integration of a Data Consumer Application",
    "label_zh": "支持新集成：数据消费方应用",
    "type": "function",
    "parent": "g_extension",
    "level": 3
  },
  {
    "id": "f_new_external",
    "label_en": "Support New External Data Source Integration",
    "label_zh": "支持新的外部数据源集成",
    "type": "function",
    "parent": "g_extension",
    "level": 3
  },
  {
    "id": "f_reports",
    "label_en": "Build & Deliver Reports on Customer Data Quality and Evolutions",
    "label_zh": "构建并交付报告：客户数据质量与演进",
    "type": "function",
    "parent": "g_dq",
    "level": 3
  },
  {
    "id": "f_value",
    "label_en": "Report C-MDM Business Value",
    "label_zh": "报告 C-MDM 业务价值",
    "type": "function",
    "parent": "g_dq",
    "level": 3
  },
  {
    "id": "f_comm_value",
    "label_en": "Communicate about C-MDM Value and Current Usage",
    "label_zh": "沟通 C-MDM 价值与当前用途",
    "type": "function",
    "parent": "g_comm",
    "level": 3
  },
  {
    "id": "f_comm_catalog",
    "label_en": "Communicate the Customer Data Team Services Catalog",
    "label_zh": "沟通客户数据团队服务目录",
    "type": "function",
    "parent": "g_comm",
    "level": 3
  },
  {
    "id": "f_comm_quality",
    "label_en": "Communicate about Customer Data Quality",
    "label_zh": "沟通客户数据质量",
    "type": "function",
    "parent": "g_comm",
    "level": 3
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅黄大框",
    "meaning_zh": "业务功能分组",
    "explicit": false
  },
  {
    "symbol": "圆角框 + 右上角折角箭头图标",
    "meaning_zh": "业务功能（ArchiMate Business Function）",
    "explicit": false
  },
  {
    "symbol": "圆角框 + 小人图标",
    "meaning_zh": "业务参与者/角色（ArchiMate Business Actor）",
    "explicit": false
  },
  {
    "symbol": "右上角小图标（重叠圆圈）",
    "meaning_zh": "ArchiMate 分组/集合记号（原图装饰性图标，无文字说明）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "顶部横贯 Customer-MDM Team 容器（4 个角色并排）；其下依次为：能力管理与治理（横贯）、左列外部客户数据获取、中部 C-MDM 设计、其下 C-MDM 运营与范围/用途扩展、右列数据质量与业务价值度量、底部横贯沟通。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig5-4",
    "relation": "complements",
    "note_zh": "图 5-3 是业务功能侧参考模型，图 5-4 是与之配套的应用功能侧参考模型；两者共同构成第 5.2 节的详细功能参考模型。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图英文标签“Set Up a Date Partnership”“Data Produce Application”存在拼写错误，本分析按原样记录并在 label_zh 中给出合理译名。",
    "角色与功能组之间没有画责任分配线，无法从图判断每项功能由哪个角色负责。",
    "中文稿标签对照表漏列 11 个功能，解读时应以图或英文表 5-3 为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 41 页原图截图及 3×3 放大分块",
    "英文 PDF 第 41 页表 5-3 开头",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 525–566 行",
    "figs/zh/g21be_fig5-3_zh.png 中文化图"
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
