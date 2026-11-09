# G234/fig5-1 · 元数据管理详细业务功能

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig5-1.md) · [JSON](../../architecture/diagrams/G234/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 31 页

![英文原图](../assets/G234/fig5-1-p0031.png)

PDF 坐标：`[86.9, 175.0, 525.1, 471.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
‘Metadata Management Team
,
.
Data Owner
Data Steward
DataProtection
Officer
J
Data custodian |
L
‘Metadata Management Business Functions
‘Strategy & Roadmaps Definition
Define Business
Drivers &
Define Roles &
‘dentiy & Develop |
Define KPIs,
Responsibilities
Bulld the Roadmap
‘Sponsorship
Requirements,
Governance & Measurement
Define Business
(Onboard & Appoint Data Steward,
A
Measure Metadata Documentation
Data Domain
Business Data Owner, Data Privat
‘Quality & Usage
Officer Per Data Domain
7
Business Glossary Documentation
Data Dictionary Documentation
a
Data Usage Documentation
A
Document Application
Document Data Processing Activity
Document Business Concepts
Classify Data Objects & Data
a
Document Database
6
Document Data Transfer
A
Elements (privacy, business criticality)
J
DocumentData Set Data Feld)
Document DPIA Results
\
a
a
Rule & Policy Documentation
¢
Datalssve Documentation
Document Business Rules]
Document Data Policies
A
Document Business Data Issues’
Document Data Quality issues”
Business Assets & Technical Assets Association
Metadata Repository Design
Document the link between
~
the business glossary concepts
Document the link between
Design Metadata Access)
the data usage and the systems
[ Pesunmetacat Repotary
‘Mode!
|
‘and their implementation in the
‘that enable this usage
information systems
a
Design Workflow
Linkbusiness rules to data
Link business rules to
processing activity
business data elements,
‘Communications & Training
y
‘Communicate about the metadata ||
‘Train End Users
Communicate about the usage of the ~ |
|
currently available inthe repository
‘metadata available
```

## 本次原图核对

英文 PDF 第 31 页五类文档化分组为 2+3+3+2+2=12 项，修正历史摘要中的 13。10 个一级分组共有 30 个二级功能。

## 概要（历史解释；局部修正见上）

把 10 项高层业务功能展开为 30 项二级业务功能，并标出承担治理职责的四类角色。

## 目的（历史解释；局部修正见上）

第 5.1 节的详细业务参考模型，供 ADM 阶段 B 做基线—目标差距分析，也供阶段 E 用来挑战解决方案供应商：每一项二级功能都可以对应到具体的组织职责或交付物。

## 阅读顺序（历史解释；局部修正见上）

先看顶部灰色带 Metadata Management Team，里面是四类治理角色。再看下方黄色大组 Metadata Management Business Functions：它按 10 个功能组纵向排列，每个组框的标题是一级功能，组内小框是该功能的二级分解。全图没有连线，框的嵌套表示“属于”，组框的上下次序只是排版。

## 关键含义（历史解释；局部修正见上）

- 治理角色四类：Data Owner、Data Steward、Data Custodian、Data Protection Officer，全部隶属同一个 Metadata Management Team，说明治理职责由团队分担而非单一岗位。
- 战略与路线图定义下 5 项：定义业务驱动因素与需求、定义角色与职责、构建路线图、识别并培养赞助支持、定义 KPI。
- 治理与度量下 3 项构成闭环：定义业务数据域 → 按域任命数据管家/业务数据所有者/数据隐私官 → 度量元数据文档质量与使用。
- 五类文档化功能共 12 项二级功能：业务术语表 2 项、数据字典 3 项、数据使用 3 项、规则与政策 2 项、数据问题 2 项；数据字典细化到应用、数据库、数据集与字段。
- 业务资产与技术资产关联下 4 项，核心是把业务术语映射到系统实现、把数据使用映射到使能系统，并把业务规则链接到处理活动与数据元素。
- 元数据存储库设计下 3 项：存储库模型、访问模型、工作流；沟通与培训下 3 项：培训最终用户、沟通库内现有元数据、沟通元数据使用情况。
- 图 3-1 的一级功能在本图中同时充当分组容器（如 Strategy & Roadmaps Definition），因此组框标题不是纯标题，而是一项功能。

## 层级（历史解释；局部修正见上）

三条线：① 团队带 → 4 个角色（两层）；② 业务功能大组 → 10 个一级功能组 → 30 个二级功能（三层）。两条线并列，团队不是业务功能的父节点。

## 线条含义（历史解释；局部修正见上）

全图无连线。嵌套关系表示“二级功能属于该一级功能”，大组框表示“这些功能都属于元数据管理业务功能”；组框上下位置不表示流程先后。

## 易误读点（历史解释；局部修正见上）

- 不要把顶部四个角色当成四个部门或四个系统；它们是同一团队内的治理职责。
- 不要把组框标题只当标题：Strategy & Roadmaps Definition 等同时是一级业务功能，图 3-1 已把它们列为一级功能。
- 不要以为每个一级功能下的二级功能数量相同；从 2 项到 5 项不等。
- 中文 PNG 中大量二级功能字号极小，不能因为看不清就认为原图没有这些功能。

## 元素

```json
[
  {
    "id": "team",
    "label_en": "Metadata Management Team",
    "label_zh": "元数据管理团队",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "顶部灰色带"
  },
  {
    "id": "role_owner",
    "label_en": "Data Owner",
    "label_zh": "数据所有者",
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
    "id": "role_custodian",
    "label_en": "Data Custodian",
    "label_zh": "数据保管人",
    "type": "role",
    "parent": "team",
    "level": 2
  },
  {
    "id": "role_dpo",
    "label_en": "Data Protection Officer",
    "label_zh": "数据保护官",
    "type": "role",
    "parent": "team",
    "level": 2
  },
  {
    "id": "bf_root",
    "label_en": "Metadata Management Business Functions",
    "label_zh": "元数据管理业务功能",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "黄色大组"
  },
  {
    "id": "g_strategy",
    "label_en": "Strategy & Roadmaps Definition",
    "label_zh": "战略与路线图定义",
    "type": "function",
    "parent": "bf_root",
    "level": 2,
    "position": "功能组 1"
  },
  {
    "id": "f_drivers",
    "label_en": "Define Business Drivers & Requirements",
    "label_zh": "定义业务驱动因素与需求",
    "type": "function",
    "parent": "g_strategy",
    "level": 3
  },
  {
    "id": "f_roles",
    "label_en": "Define Roles & Responsibilities",
    "label_zh": "定义角色与职责",
    "type": "function",
    "parent": "g_strategy",
    "level": 3
  },
  {
    "id": "f_roadmap",
    "label_en": "Build the Roadmap",
    "label_zh": "构建路线图",
    "type": "function",
    "parent": "g_strategy",
    "level": 3
  },
  {
    "id": "f_sponsorship",
    "label_en": "Identify & Develop Sponsorship",
    "label_zh": "识别并培养赞助支持",
    "type": "function",
    "parent": "g_strategy",
    "level": 3
  },
  {
    "id": "f_kpis",
    "label_en": "Define KPIs",
    "label_zh": "定义 KPI",
    "type": "function",
    "parent": "g_strategy",
    "level": 3
  },
  {
    "id": "g_governance",
    "label_en": "Governance & Measurement",
    "label_zh": "治理与度量",
    "type": "function",
    "parent": "bf_root",
    "level": 2,
    "position": "功能组 2"
  },
  {
    "id": "f_domain",
    "label_en": "Define Business Data Domain",
    "label_zh": "定义业务数据域",
    "type": "function",
    "parent": "g_governance",
    "level": 3
  },
  {
    "id": "f_appoint",
    "label_en": "Onboard & Appoint Data Steward, Business Data Owner, Data Privacy Officer Per Data Domain",
    "label_zh": "按数据域吸纳并任命数据管家、业务数据所有者、数据隐私官",
    "type": "function",
    "parent": "g_governance",
    "level": 3
  },
  {
    "id": "f_measure",
    "label_en": "Measure Metadata Documentation Quality & Usage",
    "label_zh": "度量元数据文档质量与使用",
    "type": "function",
    "parent": "g_governance",
    "level": 3
  },
  {
    "id": "g_glossary",
    "label_en": "Business Glossary Documentation",
    "label_zh": "业务术语表文档",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_concepts",
    "label_en": "Document Business Concepts",
    "label_zh": "记录业务概念",
    "type": "function",
    "parent": "g_glossary",
    "level": 3
  },
  {
    "id": "f_classify",
    "label_en": "Classify Data Objects & Data Elements (privacy, business criticality)",
    "label_zh": "对数据对象与数据元素分类（隐私、业务关键性）",
    "type": "function",
    "parent": "g_glossary",
    "level": 3
  },
  {
    "id": "g_dictionary",
    "label_en": "Data Dictionary Documentation",
    "label_zh": "数据字典文档",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_app",
    "label_en": "Document Application",
    "label_zh": "记录应用",
    "type": "function",
    "parent": "g_dictionary",
    "level": 3
  },
  {
    "id": "f_db",
    "label_en": "Document Database",
    "label_zh": "记录数据库",
    "type": "function",
    "parent": "g_dictionary",
    "level": 3
  },
  {
    "id": "f_dataset",
    "label_en": "Document Data Set & Data Field",
    "label_zh": "记录数据集与数据字段",
    "type": "function",
    "parent": "g_dictionary",
    "level": 3
  },
  {
    "id": "g_usage",
    "label_en": "Data Usage Documentation",
    "label_zh": "数据使用文档",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_processing",
    "label_en": "Document Data Processing Activity",
    "label_zh": "记录数据处理活动",
    "type": "function",
    "parent": "g_usage",
    "level": 3
  },
  {
    "id": "f_transfer",
    "label_en": "Document Data Transfer",
    "label_zh": "记录数据传输",
    "type": "function",
    "parent": "g_usage",
    "level": 3
  },
  {
    "id": "f_dpia",
    "label_en": "Document DPIA Results",
    "label_zh": "记录 DPIA 结果",
    "type": "function",
    "parent": "g_usage",
    "level": 3
  },
  {
    "id": "g_rules",
    "label_en": "Rule & Policy Documentation",
    "label_zh": "规则与政策文档",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_business_rules",
    "label_en": "Document Business Rules",
    "label_zh": "记录业务规则",
    "type": "function",
    "parent": "g_rules",
    "level": 3
  },
  {
    "id": "f_policies",
    "label_en": "Document Data Policies",
    "label_zh": "记录数据政策",
    "type": "function",
    "parent": "g_rules",
    "level": 3
  },
  {
    "id": "g_issues",
    "label_en": "Data Issue Documentation",
    "label_zh": "数据问题文档",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_business_issues",
    "label_en": "Document Business Data Issues",
    "label_zh": "记录业务数据问题",
    "type": "function",
    "parent": "g_issues",
    "level": 3
  },
  {
    "id": "f_quality_issues",
    "label_en": "Document Data Quality Issues",
    "label_zh": "记录数据质量问题",
    "type": "function",
    "parent": "g_issues",
    "level": 3
  },
  {
    "id": "g_assets",
    "label_en": "Business Assets & Technical Assets Association",
    "label_zh": "业务资产与技术资产关联",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_link_glossary",
    "label_en": "Document the link between the business glossary concepts and their implementation in the information systems",
    "label_zh": "记录业务术语表概念与其在信息系统中实现之间的链接",
    "type": "function",
    "parent": "g_assets",
    "level": 3
  },
  {
    "id": "f_link_usage",
    "label_en": "Document the link between the data usage and the systems that enable this usage",
    "label_zh": "记录数据使用与使能该使用的系统之间的链接",
    "type": "function",
    "parent": "g_assets",
    "level": 3
  },
  {
    "id": "f_rule_activity",
    "label_en": "Link business rules to data processing activity",
    "label_zh": "将业务规则链接到数据处理活动",
    "type": "function",
    "parent": "g_assets",
    "level": 3
  },
  {
    "id": "f_rule_element",
    "label_en": "Link business rules to business data elements",
    "label_zh": "将业务规则链接到业务数据元素",
    "type": "function",
    "parent": "g_assets",
    "level": 3
  },
  {
    "id": "g_repo_design",
    "label_en": "Metadata Repository Design",
    "label_zh": "元数据存储库设计",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_repo_model",
    "label_en": "Design Metadata Repository Model",
    "label_zh": "设计元数据存储库模型",
    "type": "function",
    "parent": "g_repo_design",
    "level": 3
  },
  {
    "id": "f_access_model",
    "label_en": "Design Metadata Access Model",
    "label_zh": "设计元数据访问模型",
    "type": "function",
    "parent": "g_repo_design",
    "level": 3
  },
  {
    "id": "f_workflow",
    "label_en": "Design Workflow",
    "label_zh": "设计工作流",
    "type": "function",
    "parent": "g_repo_design",
    "level": 3
  },
  {
    "id": "g_comms",
    "label_en": "Communications & Training",
    "label_zh": "沟通与培训",
    "type": "function",
    "parent": "bf_root",
    "level": 2
  },
  {
    "id": "f_train",
    "label_en": "Train End Users",
    "label_zh": "培训最终用户",
    "type": "function",
    "parent": "g_comms",
    "level": 3
  },
  {
    "id": "f_comm_available",
    "label_en": "Communicate about the metadata currently available in the repository",
    "label_zh": "沟通存储库中当前可用的元数据",
    "type": "function",
    "parent": "g_comms",
    "level": 3
  },
  {
    "id": "f_comm_usage",
    "label_en": "Communicate about the usage of the metadata available",
    "label_zh": "沟通可用元数据的使用情况",
    "type": "function",
    "parent": "g_comms",
    "level": 3
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色带 Metadata Management Team",
    "meaning_zh": "元数据管理团队（治理角色）",
    "explicit": true
  },
  {
    "symbol": "黄色大组 Metadata Management Business Functions",
    "meaning_zh": "业务功能总容器",
    "explicit": true
  },
  {
    "symbol": "内层圆角组框标题",
    "meaning_zh": "一级业务功能/功能组",
    "explicit": false
  },
  {
    "symbol": "组内小框 + 右上折角箭头",
    "meaning_zh": "二级业务功能（ArchiMate 功能记号）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "顶部灰色团队横带（4 个角色框横排）；下方黄色大组内按 10 行排列功能组，组内二级功能横排或两列排布。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig3-1",
    "relation": "detail_of",
    "note_zh": "本图把图 3-1 的 10 项高层业务功能逐项展开为二级功能"
  },
  {
    "target": "G234/fig5-2",
    "relation": "complements",
    "note_zh": "本图是业务侧细化，图 5-2 是应用侧细化"
  },
  {
    "target": "G234/fig2-1",
    "relation": "uses_legend",
    "note_zh": "本图使用图 2-1 定义的 ArchiMate 业务功能记法"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中组框标题既是一级功能又是容器，原图没有额外说明；本分析按“功能 + 分组”双重角色处理。",
    "四个角色框之间没有连线，团队与角色、团队与业务功能之间的关系由版式表达。",
    "中文 PNG 多处文字过小，个别二级功能译名（如“识别并培养赞助支持”）以中文稿对照表为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 31 页原图截图",
    "英文 PDF 第 31–34 页表 5-1 文字",
    "中文稿 G234e_信息架构_元数据管理.md 第 509–553 行（图内标签对照）",
    "figs/g234e_fig5-1_en.png、figs/zh/g234e_fig5-1_zh.png"
  ],
  "date": "2026-10-31"
}
```

## 既有来源冲突

```json
[
  {
    "id": "source-g234-fig5-1",
    "figure_id": "G234/fig5-1",
    "status": "observed-conflict",
    "description": "JSON摘要五类文档化功能共13项的分项相加为12；一级10组二级30项需按图逐组核对。",
    "evidence": [
      "G234 §5.1",
      "figs/g234e_fig5-1_en.png",
      "figs/ai/G234/fig5-1.json"
    ],
    "resolution": "使用实际分组与元素清单，不把错误摘要数量转为约束。"
  }
]
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "specific-findings-only",
  "all_source_pages_valid": true
}
```
