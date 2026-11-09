# G238/fig4-2 · BI 与分析详细业务功能

> 当前图示解析：[Markdown](../../architecture/diagrams/G238/fig4-2.md) · [JSON](../../architecture/diagrams/G238/fig4-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G238e.pdf`；SHA-256：`87e00e009377a887627417ceffc28b1f480bfaf57c9c84ee6f8757cc5c1c9444`。

## 原图 · PDF 第 31 页

![英文原图](../assets/G238/fig4-2-p0031.png)

PDF 坐标：`[48.2, 117.4, 563.8, 655.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
BI & Analytics Business Functions
A
© The Open Group
Define the Strategy & Roadmaps
A
Build the BI &
Maintain BI & (Q)
Identity &
Ensure Consistency with (-)
Analytics
Build the Roadmap
Analytics Usages
Define KPIs
Develop
Related Strategies (Security,
Strategy
Backlog
‘Sponsorship
Sustainability, etc.)
Provide Necessary,
Design & Develop BI & Analytics Value Chain
A) Govern & Measure ()
Data Sources for
BI & Analytics
Define BI & Analytics Architecture Principles and Ensure Consistency of Solutions
a
Purposes
Define Governance
Design Infrastructure & Adapted Storage Spaces
a
Organization & RACI
Identity
Relevant Data
Model & Build Data Structuration Depending on Related Uses (Raw, Warehouse, Business (A)
‘Sources
Views)
Define & Enforce A
Identity &
Define & Implement
a
Define & Implement
a
Define & Implement
Process to Onboard
Manage Data
Business Rules
Technical Rules
‘Specific Data Protection
New Source Data
Providers
Rules
Design & Develop Data Pipelines
Design & Build ()
A
Necessary
Interfaces
A
Define & Enforce Cost
Design Semantic Layer
Data Wrangling
Design & Buta A
Optimization Principles
Analytical Models
Design & Build (~)
Design & Build ())
Industrialize & Deploy Advanced = ())
Industrialized
‘Ad Hoc Reports
Analytical Models
Stable Reports
Define & Enforce A
‘Compliance
Protect Data & Ensure Compliance
Requirements
Aa
Define
‘Support for
a
Define & Manage Data Audit Platform Secur Anonymization
Detect & Notify a Dal Handling Data
Breach
& Compliance
Requirements &
Portability
A
Processes
Requests
Measure Data Volumes
Define & Apply a Data Quality Framework (Measures, Quality Management, etc.)
Aa
Leverage Metadata Management for BI & Analytics
a
Aa
Measure Data Use
Operate Platforms.
A
Frequencies
Detect &
Monitor &
Detect&
Control Costs
Monitor &
Control Data
Manage
Manage Data
Incidents
Issues
Quality
Follow Up ROI of
Monitor & (9)
‘Schedule Data (-)
Control Model
Integration &
Grant Access
Usages
‘Accuracy
Pipeline
‘Communicate & Train
Aa
Train End Users in 81 & A
Animate BI & Analytics (-)
Communicate Strategy, (~)
Leverage Technical Al
Users & Expert
Business, & Technical
Analytics & Tools
Evangelism
‘Communities
Roadmaps
```

## 概要（历史解释；局部修正见上）

把 BI 与分析业务功能分解为 9 个高层功能组和 45 项子功能，用嵌套框表达组成关系。

## 目的（历史解释；局部修正见上）

给出业务侧参考模型的详细层级：把图 2-1 的 9 项高层业务功能逐项展开，供组织评估现状、设计目标 BI & Analytics 能力时逐项核对；它也是表 4-2 的图形版，用嵌套位置说明“宏观功能—子功能”的归属。

## 阅读顺序（历史解释；局部修正见上）

从外到内读：最外层大框是全部 BI & Analytics 业务功能；内部 9 个带标题的功能框是宏观功能（与图 2-1 左栏一一对应）；宏观功能框内的小圆角框是子功能。所有框右上角的旗帜图标表示 ArchiMate 功能元素。图中没有箭头，框的包含关系就是组成关系；版式上 Define the Strategy & Roadmaps 横贯顶部，Provide Necessary Data Sources 在左列，Design & Develop Value Chain 是中央最大块，Govern & Measure 在右列纵贯，Protect/Quality/Metadata/Operate/Communicate 依次向下横贯。

## 关键含义（历史解释；局部修正见上）

- 9 个高层业务功能与图 2-1 左栏完全对应：定义战略与路线图、提供必要数据源、设计与开发价值链条、治理与度量、保护数据与确保合规、定义并应用数据质量框架、利用元数据管理、运营平台、沟通与培训。
- 子功能数量：定义战略 6、提供数据源 3、设计与开发价值链条 13（最大）、治理与度量 7、保护数据与合规 5、运营平台 7、沟通与培训 4；数据质量框架与元数据管理没有子功能，是叶子功能。
- 设计与开发价值链条的 13 项覆盖从架构原则、基础设施与存储空间、数据结构化，到业务/技术/数据保护规则、数据管道、语义层、数据整理、高级分析模型、工业化/即席报表与模型部署的完整链条。
- 治理与度量 7 项关注组织与 RACI、新数据源接入、成本优化、合规要求、数据量、使用频率与 ROI，是横跨其他功能的治理面。
- 运营平台 7 项关注事件、数据问题、成本、数据质量、模型准确性、调度与授权，是平台运行面。
- 图只给功能名称，不给定义；每个子功能的说明见表 4-2（粗体行是宏观功能，其余是子功能）。
- 嵌套与字号只表示层级和分组，不表示成熟度、优先级或执行顺序；图中没有流程箭头。

## 层级（历史解释；局部修正见上）

三层：L0 是“BI & Analytics Business Functions”总容器；L1 是 9 个宏观业务功能；L2 是 45 个子功能。数据质量框架与元数据管理两个 L1 功能没有 L2 子项。所有层级都是 ArchiMate 功能，父框在视觉上包住子框表示组成。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。父子关系完全由“框内嵌框”表达（ArchiMate 组合）；同层框并排只表示同属一个宏观功能，不表示顺序或依赖。value chain 组的子功能虽然按“原则→基础设施→规则→管道→语义/模型→报表”自上而下排布，但没有箭头，不能当作正式流程。

## 易误读点（历史解释；局部修正见上）

- 不要把设计与开发价值链条的子功能按从上到下读成有先后时序的流水线；图中没有箭头，位置只是版式。
- 不要把“定义并应用数据质量框架”“利用元数据管理”当成次要功能：它们与其余 7 项同为宏观功能，只是没有画出子功能。
- 不要把嵌套关系读成组织汇报或系统部署关系；它只表示功能组成。
- 不要把 9 个高层功能当成 9 个流程阶段或 ADM 阶段。
- 中文稿中文化 PNG 有几个子功能标签被缩得很小并带底色块，容易让人误以为它们属于另一个层级或不是正式功能；应以英文原图为准。

## 元素

```json
[
  {
    "id": "bf_root",
    "label_en": "BI & Analytics Business Functions",
    "label_zh": "BI 与分析业务功能",
    "type": "function",
    "parent": null,
    "level": 0,
    "position": "最外层大框",
    "description_zh": "整个业务功能参考模型的容器。"
  },
  {
    "id": "bf_strategy",
    "label_en": "Define the Strategy & Roadmaps",
    "label_zh": "定义战略与路线图",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 1,
    "position": "顶部横贯整宽"
  },
  {
    "id": "bf_build_strategy",
    "label_en": "Build the BI & Analytics Strategy",
    "label_zh": "构建 BI 与分析战略",
    "type": "function",
    "parent": "bf_strategy",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_build_roadmap",
    "label_en": "Build the Roadmap",
    "label_zh": "构建路线图",
    "type": "function",
    "parent": "bf_strategy",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_maintain_backlog",
    "label_en": "Maintain BI & Analytics Usages Backlog",
    "label_zh": "维护 BI 与分析用途待办列表",
    "type": "function",
    "parent": "bf_strategy",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_define_kpis",
    "label_en": "Define KPIs",
    "label_zh": "定义 KPI",
    "type": "function",
    "parent": "bf_strategy",
    "level": 2,
    "order": 4
  },
  {
    "id": "bf_sponsorship",
    "label_en": "Identify & Develop Sponsorship",
    "label_zh": "识别并发展赞助",
    "type": "function",
    "parent": "bf_strategy",
    "level": 2,
    "order": 5
  },
  {
    "id": "bf_consistency",
    "label_en": "Ensure Consistency with Related Strategies (Security, Sustainability, etc.)",
    "label_zh": "确保与相关战略一致（安全、可持续性等）",
    "type": "function",
    "parent": "bf_strategy",
    "level": 2,
    "order": 6
  },
  {
    "id": "bf_sources",
    "label_en": "Provide Necessary Data Sources for BI & Analytics Purposes",
    "label_zh": "为 BI 与分析提供必要数据源",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 2,
    "position": "左列"
  },
  {
    "id": "bf_identify_sources",
    "label_en": "Identify Relevant Data Sources",
    "label_zh": "识别相关数据源",
    "type": "function",
    "parent": "bf_sources",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_manage_providers",
    "label_en": "Identify & Manage Data Providers",
    "label_zh": "识别并管理数据提供方",
    "type": "function",
    "parent": "bf_sources",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_build_interfaces",
    "label_en": "Design & Build Necessary Interfaces",
    "label_zh": "设计并构建必要数据接口",
    "type": "function",
    "parent": "bf_sources",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_value_chain",
    "label_en": "Design & Develop BI & Analytics Value Chain",
    "label_zh": "设计与开发 BI 与分析价值链条",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 3,
    "position": "中央最大块"
  },
  {
    "id": "bf_arch_principles",
    "label_en": "Define BI & Analytics Architecture Principles and Ensure Consistency of Solutions",
    "label_zh": "定义 BI 与分析架构原则并确保方案一致性",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_storage_spaces",
    "label_en": "Design Infrastructure & Adapted Storage Spaces",
    "label_zh": "设计基础设施与适配的存储空间",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_structuration",
    "label_en": "Model & Build Data Structuration Depending on Related Uses (Raw, Warehouse, Business Views)",
    "label_zh": "依据用途建模并构建数据结构化（原始、仓库、业务视图）",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_business_rules",
    "label_en": "Define & Implement Business Rules",
    "label_zh": "定义并实施业务规则",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 4
  },
  {
    "id": "bf_technical_rules",
    "label_en": "Define & Implement Technical Rules",
    "label_zh": "定义并实施技术规则",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 5
  },
  {
    "id": "bf_protection_rules",
    "label_en": "Define & Implement Specific Data Protection Rules",
    "label_zh": "定义并实施特定数据保护规则",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 6
  },
  {
    "id": "bf_pipelines",
    "label_en": "Design & Develop Data Pipelines",
    "label_zh": "设计与开发数据管道",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 7
  },
  {
    "id": "bf_semantic_layer",
    "label_en": "Design Semantic Layer",
    "label_zh": "设计语义层",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 8
  },
  {
    "id": "bf_data_wrangling",
    "label_en": "Data Wrangling",
    "label_zh": "数据整理（Data Wrangling）",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 9
  },
  {
    "id": "bf_advanced_models",
    "label_en": "Design & Build Advanced Analytical Models",
    "label_zh": "设计与构建高级分析模型",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 10
  },
  {
    "id": "bf_industrial_reports",
    "label_en": "Design & Build Industrialized Stable Reports",
    "label_zh": "设计与构建工业化稳定报表",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 11
  },
  {
    "id": "bf_adhoc_reports",
    "label_en": "Design & Build Ad Hoc Reports",
    "label_zh": "设计与构建即席报表",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 12
  },
  {
    "id": "bf_industrial_models",
    "label_en": "Industrialize & Deploy Advanced Analytical Models",
    "label_zh": "工业化并部署高级分析模型",
    "type": "function",
    "parent": "bf_value_chain",
    "level": 2,
    "order": 13
  },
  {
    "id": "bf_govern",
    "label_en": "Govern & Measure",
    "label_zh": "治理与度量",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 4,
    "position": "右列纵贯"
  },
  {
    "id": "bf_governance_org",
    "label_en": "Define Governance Organization & RACI",
    "label_zh": "定义治理组织与 RACI",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_onboard_source",
    "label_en": "Define & Enforce Process to Onboard New Source Data",
    "label_zh": "定义并执行新数据源接入流程",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_cost_principles",
    "label_en": "Define & Enforce Cost Optimization Principles",
    "label_zh": "定义并执行成本优化原则",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_compliance_req",
    "label_en": "Define & Enforce Compliance Requirements",
    "label_zh": "定义并执行合规要求",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 4
  },
  {
    "id": "bf_measure_volumes",
    "label_en": "Measure Data Volumes",
    "label_zh": "度量数据量",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 5
  },
  {
    "id": "bf_measure_frequencies",
    "label_en": "Measure Data Use Frequencies",
    "label_zh": "度量数据使用频率",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 6
  },
  {
    "id": "bf_roi",
    "label_en": "Follow Up ROI of Usages",
    "label_zh": "跟踪用途 ROI",
    "type": "function",
    "parent": "bf_govern",
    "level": 2,
    "order": 7
  },
  {
    "id": "bf_protect",
    "label_en": "Protect Data & Ensure Compliance",
    "label_zh": "保护数据并确保合规",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 5,
    "position": "中下部横贯整宽"
  },
  {
    "id": "bf_data_access",
    "label_en": "Define & Manage Data Access",
    "label_zh": "定义并管理数据访问",
    "type": "function",
    "parent": "bf_protect",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_audit",
    "label_en": "Audit Platform Security & Compliance",
    "label_zh": "审计平台安全与合规",
    "type": "function",
    "parent": "bf_protect",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_anonymization",
    "label_en": "Define Anonymization Requirements & Processes",
    "label_zh": "定义匿名化需求与流程",
    "type": "function",
    "parent": "bf_protect",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_breach",
    "label_en": "Detect & Notify a Data Breach",
    "label_zh": "检测并通知数据泄露",
    "type": "function",
    "parent": "bf_protect",
    "level": 2,
    "order": 4
  },
  {
    "id": "bf_portability",
    "label_en": "Support for Handling Data Portability Requests",
    "label_zh": "支持处理数据可携带请求",
    "type": "function",
    "parent": "bf_protect",
    "level": 2,
    "order": 5
  },
  {
    "id": "bf_quality",
    "label_en": "Define & Apply a Data Quality Framework (Measures, Quality Management, etc.)",
    "label_zh": "定义并应用数据质量框架（度量、质量管理等）",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 6,
    "position": "中部单条横贯",
    "description_zh": "没有子功能的叶子宏观功能。"
  },
  {
    "id": "bf_metadata",
    "label_en": "Leverage Metadata Management for BI & Analytics",
    "label_zh": "为 BI 与分析利用元数据管理",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 7,
    "position": "中部单条横贯",
    "description_zh": "没有子功能的叶子宏观功能。"
  },
  {
    "id": "bf_operate",
    "label_en": "Operate Platforms",
    "label_zh": "运营平台",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 8,
    "position": "中下部横贯整宽"
  },
  {
    "id": "bf_incidents",
    "label_en": "Detect & Manage Incidents",
    "label_zh": "检测并管理事件",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_data_issues",
    "label_en": "Detect & Manage Data Issues",
    "label_zh": "检测并管理数据问题",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_costs",
    "label_en": "Monitor & Control Costs",
    "label_zh": "监控与控制成本",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_data_quality_monitor",
    "label_en": "Monitor & Control Data Quality",
    "label_zh": "监控与控制数据质量",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 4
  },
  {
    "id": "bf_model_accuracy",
    "label_en": "Monitor & Control Model Accuracy",
    "label_zh": "监控与控制模型准确性",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 5
  },
  {
    "id": "bf_schedule",
    "label_en": "Schedule Data Integration & Pipeline",
    "label_zh": "调度数据集成与管道",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 6
  },
  {
    "id": "bf_grant_access",
    "label_en": "Grant Access",
    "label_zh": "授予访问",
    "type": "function",
    "parent": "bf_operate",
    "level": 2,
    "order": 7
  },
  {
    "id": "bf_communicate",
    "label_en": "Communicate & Train",
    "label_zh": "沟通与培训",
    "type": "function",
    "parent": "bf_root",
    "level": 1,
    "order": 9,
    "position": "底部横贯整宽"
  },
  {
    "id": "bf_train_users",
    "label_en": "Train End Users in BI & Analytics & Tools",
    "label_zh": "培训最终用户使用 BI 与分析工具",
    "type": "function",
    "parent": "bf_communicate",
    "level": 2,
    "order": 1
  },
  {
    "id": "bf_evangelism",
    "label_en": "Leverage Technical Evangelism",
    "label_zh": "利用技术布道",
    "type": "function",
    "parent": "bf_communicate",
    "level": 2,
    "order": 2
  },
  {
    "id": "bf_communities",
    "label_en": "Animate BI & Analytics Users & Expert Communities",
    "label_zh": "活跃 BI 与分析用户与专家社区",
    "type": "function",
    "parent": "bf_communicate",
    "level": 2,
    "order": 3
  },
  {
    "id": "bf_roadmap_comms",
    "label_en": "Communicate Strategy, Business, & Technical Roadmaps",
    "label_zh": "就战略、业务与技术路线图开展沟通",
    "type": "function",
    "parent": "bf_communicate",
    "level": 2,
    "order": 4
  }
]
```

## 图例

```json
[
  {
    "symbol": "外层大框",
    "meaning_zh": "BI & Analytics 业务功能总体（L0）",
    "explicit": false
  },
  {
    "symbol": "带标题的功能框",
    "meaning_zh": "宏观业务功能（L1，与图 2-1 左栏一致）",
    "explicit": false
  },
  {
    "symbol": "宏观功能框内的小圆角框",
    "meaning_zh": "子功能（L2）",
    "explicit": false
  },
  {
    "symbol": "右上角旗帜图标",
    "meaning_zh": "ArchiMate 功能元素（function）",
    "explicit": false
  },
  {
    "symbol": "黄色/米色填充",
    "meaning_zh": "业务层配色（与图 1-1 的业务功能一致）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "外层大框自上而下分为多层：顶部“定义战略与路线图”横贯整宽（内含 6 个一行排列的子功能）；其下为三列——左列“提供必要数据源”（3 个子功能纵排）、中央大块“设计与开发价值链条”（13 个子功能分 8 行）、右列“治理与度量”（7 个子功能纵排）；再往下依次是“保护数据并确保合规”（5 项一行）、“定义并应用数据质量框架”（单条）、“利用元数据管理”（单条）、“运营平台”（7 项两行）、“沟通与培训”（4 项一行）。"
}
```

## 相关图

```json
[
  {
    "target": "G238/fig2-1",
    "relation": "detail_of",
    "note_zh": "本图是图 2-1 左栏 9 项高层业务功能的细化，新增 45 项子功能。"
  },
  {
    "target": "G238/fig4-3",
    "relation": "complements",
    "note_zh": "本图给出业务功能侧，图 4-3 给出应用功能侧，共同构成 BI & Analytics 参考模型。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "“Identify & Develop Sponsorship”的中文沿用表 4-2 的“识别并发展赞助”，含义应是识别并发展赞助人/发起关系，译法偏直译。",
    "外层大框右上角的图标是一个网格（table/grid）而非其余框的旗帜图标，原图未解释；本分析仍将其作为功能容器。",
    "设计与开发价值链条的子功能在版式上呈自上而下排列，但图中无箭头，不能确定作者是否想暗示价值链顺序。"
  ],
  "analyzed_from": [
    "英文 PDF 第 31 页图 4-2 截图与 3×3 放大分块（逐块转录）",
    "英文 PDF 第 32 页起表 4-2 的宏观/子功能结构",
    "中文稿 G238e_信息架构_商业智能与分析.md 第 418–516 行",
    "figs/zh/g238e_fig4-2_zh.png、figs/g238e_fig4-2_en.png（相似度 0.99）"
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
