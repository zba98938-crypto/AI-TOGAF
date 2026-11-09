# G21B/fig3-1 · C-MDM 能力的功能构成

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig3-1.md) · [JSON](../../architecture/diagrams/G21B/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 22 页

![英文原图](../assets/G21B/fig3-1-p0022.png)

PDF 坐标：`[61.1, 36.0, 550.9, 314.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
zg
Engagement Teams
Engagement Systems
Ea]
@]
Business
Business
Partners
Partner
@)
Core Operations %
Core Operations
Systems
Teams
Systems
C-MDM Team
C-MDM System
~—___
‘C-MDM Capabilities
Data Acquisition
Management and Governance
@
wa
a
wn
Business
C-MDM Design
Data Qu
ity
Quality &
Reference
Management
Technical
H Intelligence
External
Data
Dashboard,
&
Data Quality
Management
Repor
Customer
C-MDM Operation
and Business
Data Privacy
and Au
Analytics
g
Data
Value
Management
Platforms
Data
Acquisition
Measure
> Extension of
Providers
C-MDM Scope and
Data Access
Usages
@]
4
Data
‘Communication
Customer Master Data Administration
Provider
Systems
C-MDM Capability
```

## 概要（历史解释；局部修正见上）

C-MDM 能力 = 团队（7 项业务功能）+ 系统（7 项应用功能），并连接 9 个外部参与者/系统。

## 目的（历史解释；局部修正见上）

第 3 章开头用一张 ArchiMate 图界定 C-MDM 能力的边界：左边是负责客户数据的组织（C-MDM Team，业务架构），右边是支撑它的信息系统（C-MDM System，信息系统架构），四周是必须交互的业务伙伴、数据提供方、互动/核心运营团队及其系统、BI 平台等，说明 C-MDM 不是单个应用而是“人员 + 流程 + 系统”的组合能力。

## 阅读顺序（历史解释；局部修正见上）

先看外圈：左上是业务伙伴，左下是数据提供方，上方是互动团队/核心运营团队及其系统，右侧是伙伴系统、BI 与分析平台、数据提供方系统——它们都在 C-MDM Capability 之外。再看中间的大框：左半黄色 C-MDM Team 是业务侧，7 个浅黄小框是它承担的业务功能；右半蓝色 C-MDM System 是系统侧，7 个蓝色小框是应用功能，其中 Reference Data Management、Quality & Technical Dashboard 与 Customer Master Data Administration 是跨功能的支撑块。最后顺着橙色线（业务层）与青色线（应用层）看外部元素如何接入团队或系统。

## 关键含义（历史解释；局部修正见上）

- C-MDM 能力 = C-MDM Team（人/组织）+ C-MDM System（系统），外层再用一个 Capability 框把它们包住，表示能力是二者组合的结果。
- C-MDM Team 的 7 项业务功能：能力管理与治理、设计、运营、范围与用途扩展、外部客户数据获取、数据质量与业务价值度量、沟通。
- C-MDM System 的 7 项应用功能：参考数据管理、数据采集、数据质量管理、数据隐私管理、数据访问、质量与技术仪表盘/报表/审计、客户主数据管理。
- Reference Data Management、Quality & Technical Dashboard, Reports, and Audit 与 Customer Master Data Administration 在版式上纵贯或横贯其他功能块，表示它们是支撑其他功能的基础能力。
- 外部有 4 类业务参与者（业务伙伴、数据提供方、互动团队、核心运营团队）和 5 类系统（互动系统、核心运营系统、业务伙伴系统、BI 与分析平台、数据提供方系统）。
- 业务伙伴同时接入互动团队、核心运营团队与 C-MDM Team；数据提供方接入 C-MDM Team；互动团队以虚线接入 C-MDM Team，核心运营团队以实线接入。
- 应用侧：互动系统、核心运营系统、业务伙伴系统、BI 平台、数据提供方系统都接入 C-MDM System；互动系统用虚线，其余用实线。
- 该图只表达“谁与谁相连”，不表达数据流向；数据流/交换模式在第 6 章（图 6-1 至 6-5）才展开。

## 层级（历史解释；局部修正见上）

三层：第 1 层 C-MDM Capability（最外层大框）；第 2 层 C-MDM Team 与 C-MDM System（能力的两大组成部分）；第 3 层各自内部的功能（Team 7 项业务功能、System 7 项应用功能）。外部 9 个参与者/系统不属于该能力，画在框外。

## 线条含义（历史解释；局部修正见上）

橙色线表示业务层连接，青色线表示应用层连接；实线表示直接相连，虚线（Engagement Teams→C-MDM Team、Engagement Systems→C-MDM System）表示较间接/非直接的交互。所有线都没有箭头，因此图只表达关联，不表达方向或数据流。外部业务伙伴同时连到两个内部团队，说明它是共同的交互对象。

## 易误读点（历史解释；局部修正见上）

- 不要把 C-MDM Team 与 C-MDM System 读成上下级：二者是同一能力的业务侧与系统侧，并列组成能力。
- C-MDM System 内的 Reference Data Management 等不是“子流程”，而是与其他应用功能并列、但被画成跨块以表示其支撑范围较广的功能。
- 图没有箭头，不能据此判断数据从外部系统流向 C-MDM；数据流向与同步/异步方式见图 4-2 与图 6-2 至 6-5。
- 中文稿引用的 figs/g21b_fig3-1.svg 是自拟的功能树，功能名与外部元素都与原图不符，不能作为理解本图的依据。

## 元素

```json
[
  {
    "id": "c_mdm_capability",
    "label_en": "C-MDM Capability",
    "label_zh": "C-MDM 能力",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "最外层大框，包含团队与系统两部分。"
  },
  {
    "id": "c_mdm_team",
    "label_en": "C-MDM Team",
    "label_zh": "C-MDM 团队",
    "type": "organization_unit",
    "parent": "c_mdm_capability",
    "level": 2
  },
  {
    "id": "c_mdm_system",
    "label_en": "C-MDM System",
    "label_zh": "C-MDM 系统",
    "type": "application",
    "parent": "c_mdm_capability",
    "level": 2
  },
  {
    "id": "bf_governance",
    "label_en": "C-MDM Capabilities Management and Governance",
    "label_zh": "C-MDM 能力管理与治理",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "bf_design",
    "label_en": "C-MDM Design",
    "label_zh": "C-MDM 设计",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "bf_operation",
    "label_en": "C-MDM Operation",
    "label_zh": "C-MDM 运营",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "bf_extension",
    "label_en": "Extension of C-MDM Scope and Usages",
    "label_zh": "C-MDM 范围与用途扩展",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "bf_external_acq",
    "label_en": "External Customer Data Acquisition",
    "label_zh": "外部客户数据获取",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "bf_dq_value",
    "label_en": "Data Quality and Business Value Measure",
    "label_zh": "数据质量与业务价值度量",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "bf_communication",
    "label_en": "Communication",
    "label_zh": "沟通",
    "type": "function",
    "parent": "c_mdm_team",
    "level": 3
  },
  {
    "id": "af_reference_data",
    "label_en": "Reference Data Management",
    "label_zh": "参考数据管理",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "af_acquisition",
    "label_en": "Data Acquisition",
    "label_zh": "数据采集",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "af_dq",
    "label_en": "Data Quality Management",
    "label_zh": "数据质量管理",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "af_privacy",
    "label_en": "Data Privacy Management",
    "label_zh": "数据隐私管理",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "af_access",
    "label_en": "Data Access",
    "label_zh": "数据访问",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "af_dashboard",
    "label_en": "Quality & Technical Dashboard, Reports, and Audit",
    "label_zh": "质量与技术仪表盘、报表与审计",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "af_admin",
    "label_en": "Customer Master Data Administration",
    "label_zh": "客户主数据管理（系统管理功能）",
    "type": "function",
    "parent": "c_mdm_system",
    "level": 3
  },
  {
    "id": "x_business_partners",
    "label_en": "Business Partners",
    "label_zh": "业务伙伴",
    "type": "actor",
    "parent": null,
    "position": "左上"
  },
  {
    "id": "x_data_providers",
    "label_en": "Data Providers",
    "label_zh": "数据提供方",
    "type": "actor",
    "parent": null,
    "position": "左下"
  },
  {
    "id": "x_engagement_teams",
    "label_en": "Engagement Teams",
    "label_zh": "互动团队",
    "type": "actor",
    "parent": null,
    "position": "上排左"
  },
  {
    "id": "x_core_ops_teams",
    "label_en": "Core Operations Teams",
    "label_zh": "核心业务运营团队",
    "type": "actor",
    "parent": null,
    "position": "上排中"
  },
  {
    "id": "x_engagement_systems",
    "label_en": "Engagement Systems",
    "label_zh": "互动系统",
    "type": "application",
    "parent": null,
    "position": "上排右"
  },
  {
    "id": "x_core_ops_systems",
    "label_en": "Core Operations Systems",
    "label_zh": "核心业务运营系统",
    "type": "application",
    "parent": null,
    "position": "上排右中"
  },
  {
    "id": "x_bp_systems",
    "label_en": "Business Partner Systems",
    "label_zh": "业务伙伴系统",
    "type": "application",
    "parent": null,
    "position": "右上"
  },
  {
    "id": "x_bi_platforms",
    "label_en": "Business Intelligence & Analytics Platforms",
    "label_zh": "商业智能与分析平台",
    "type": "application",
    "parent": null,
    "position": "右中"
  },
  {
    "id": "x_dp_systems",
    "label_en": "Data Provider Systems",
    "label_zh": "数据提供方系统",
    "type": "application",
    "parent": null,
    "position": "右下"
  }
]
```

## 关系

```json
[
  {
    "id": "r1",
    "from": "x_business_partners",
    "to": "x_engagement_teams",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "橙色业务层连线，横向。"
  },
  {
    "id": "r2",
    "from": "x_business_partners",
    "to": "x_core_ops_teams",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "橙色业务层连线。"
  },
  {
    "id": "r3",
    "from": "x_business_partners",
    "to": "c_mdm_team",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "橙色线从 Business Partners 右缘下行接入 C-MDM Team 左缘中部。"
  },
  {
    "id": "r4",
    "from": "x_data_providers",
    "to": "c_mdm_team",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "橙色线从 Data Providers 右缘接入 C-MDM Team 左下角。"
  },
  {
    "id": "r5",
    "from": "x_engagement_teams",
    "to": "c_mdm_team",
    "type": "association",
    "explicit": true,
    "line": "dashed",
    "arrow": "none",
    "description_zh": "橙色虚线，从 Engagement Teams 下缘垂直接入 C-MDM Team 上缘。"
  },
  {
    "id": "r6",
    "from": "x_core_ops_teams",
    "to": "c_mdm_team",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "橙色实线短连接，从 Core Operations Teams 下缘接入 C-MDM Team 上缘。"
  },
  {
    "id": "r7",
    "from": "x_engagement_systems",
    "to": "x_bp_systems",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "青色应用层连线，Engagement Systems 右缘 → Business Partner Systems 左缘。"
  },
  {
    "id": "r8",
    "from": "x_core_ops_systems",
    "to": "x_bp_systems",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "青色应用层连线，Core Operations Systems 右缘 → Business Partner Systems 左缘。"
  },
  {
    "id": "r9",
    "from": "x_bp_systems",
    "to": "c_mdm_system",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "青色连线接入 C-MDM System 右缘上部。"
  },
  {
    "id": "r10",
    "from": "x_bi_platforms",
    "to": "c_mdm_system",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "青色连线接入 C-MDM System 右缘中部。"
  },
  {
    "id": "r11",
    "from": "x_dp_systems",
    "to": "c_mdm_system",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "青色连线接入 C-MDM System 右缘下部（Customer Master Data Administration 一侧）。"
  },
  {
    "id": "r12",
    "from": "x_engagement_systems",
    "to": "c_mdm_system",
    "type": "association",
    "explicit": true,
    "line": "dashed",
    "arrow": "none",
    "description_zh": "青色虚线，从 Engagement Systems 下缘垂直接入 C-MDM System 上缘。"
  },
  {
    "id": "r13",
    "from": "x_core_ops_systems",
    "to": "c_mdm_system",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "青色实线短连接，从 Core Operations Systems 下缘接入 C-MDM System 上缘。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "橙色边框（业务层）",
    "meaning_zh": "业务参与者及其之间的连接",
    "explicit": false
  },
  {
    "symbol": "青色边框（应用层）",
    "meaning_zh": "应用组件/系统及其之间的连接",
    "explicit": false
  },
  {
    "symbol": "黄色框（小人图标）",
    "meaning_zh": "业务参与者；黄色大框为 C-MDM Team",
    "explicit": false
  },
  {
    "symbol": "蓝色框（应用组件图标）",
    "meaning_zh": "应用组件；蓝色大框为 C-MDM System",
    "explicit": false
  },
  {
    "symbol": "浅黄小框（折角箭头图标）",
    "meaning_zh": "业务功能（ArchiMate Business Function）",
    "explicit": false
  },
  {
    "symbol": "蓝色小框（折角箭头图标）",
    "meaning_zh": "应用功能（ArchiMate Application Function）",
    "explicit": false
  },
  {
    "symbol": "实线 / 虚线",
    "meaning_zh": "实线=直接交互；虚线=较间接的交互（依据线条样式推断，原图无图例）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "外部元素分列四周：左侧上下为 Business Partners、Data Providers；上方为 Engagement Teams / Core Operations Teams 与 Engagement Systems / Core Operations Systems；右侧自上而下为 Business Partner Systems、Business Intelligence & Analytics Platforms、Data Provider Systems。中央大框内左黄右蓝：C-MDM Team 与 C-MDM System。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig5-3",
    "relation": "overview_of",
    "note_zh": "本图给出 C-MDM Team 的 7 项高层业务功能；图 5-3 把它们细化为 29 项详细业务功能并补充角色。"
  },
  {
    "target": "G21B/fig5-4",
    "relation": "overview_of",
    "note_zh": "本图给出 C-MDM System 的 7 项高层应用功能；图 5-4 把它们细化为详细应用功能参考模型。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图无图例，虚线（Engagement Teams/Systems 到 C-MDM）的确切语义未说明，本分析只按“较间接交互”描述。",
    "C-MDM System 内三个跨块功能（Reference Data Management、Quality & Technical Dashboard、Customer Master Data Administration）的边界在纵向上覆盖多个功能，无法确定它们是否是其他功能的父级；本分析按并列处理。"
  ],
  "analyzed_from": [
    "英文 PDF 第 22 页原图截图及 2×2 放大分块",
    "英文 PDF 第 21–23 页正文与表 3-1",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 242–258、266–272 行",
    "figs/g21b_fig3-1.svg 源码"
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
