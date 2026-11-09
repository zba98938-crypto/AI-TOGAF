# G234/fig4-1 · 元数据来源示意

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-1.md) · [JSON](../../architecture/diagrams/G234/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G234/fig4-1-p0023.png)

PDF 坐标：`[61.1, 36.0, 550.9, 259.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Data Glossary,
Business
Security
Application
Data Privacy
Risk Management
Reference
Processes
Data
Policies, & Quality
Management
Repository
Data
Medeling
Business Processes
[Security Management
‘Application Metadata
Data Privacy
Fisk Management
ReteenceData
Glossary
Toole
Modeling Tools
Repostories
Repositories
Registries
Registries
Repository
|
I
Process
Business|
(
Rule
aa
Aatvity
an
Aepli
(Ceonro)
(waar)
‘anfidantalty
Data Policy
fisinessRue)
Classification
J
(WaaFiow |
(Privacy Gasiteaton
(CPrevess_)
(Coaevave )
Data Documentation and Governance
(BisinessataDomain
Role] (Organization) ata Classification) [Metadata Association ) ( Metadata Activity Logs }
(Database) [DataSet] [Data Field | ( DataFiow | {Technical Data Deletion Rule }( Technical Data Qualiy Rule )
(Data Guay Anomay) (Data Volume | [Data Access Event]
Technical
ee oe
Operational
Metadata
S=
ee ===
Metadata
BIE Analytics
Relational
Analytica
==
Platform
“STRUCTURED DATA
Bre Analyiee
or
Platform
Daa integration
Tools
a, =
rs
oe
a
soon
‘Administration &
(Daas)
Monitering Tools
Management &
‘System Catalog
‘SEMI-STRUCTURED DATA
UNSTRUCTURED DATA
```

## 概要（历史解释；局部修正见上）

把组织内可获取元数据的 7 个域、约 30 类元数据资产，以及技术与运营元数据的数据形态一次铺开。

## 目的（历史解释；局部修正见上）

第 4.2 节开头说明元数据散落在多个来源、多个社区、不同流程与生命周期中，图 4-1 先把“有哪些域、每域能提供什么资产”摆出来，随后正文才建议按业务目标分步建立文档，而不是一次性全量登记。

## 阅读顺序（历史解释；局部修正见上）

先看顶部 7 列：每列标题是一个元数据域，列内标签是该域可提供的元数据资产。再看中部横带 “Data Documentation and Governance”，它是跨域共用的治理标签。最后看底部两框：左侧 Technical Metadata 列数据库/数据集/字段/数据流/删除规则/质量规则，并用图标区分关系型、分析型与结构化/半结构化/非结构化数据；右侧 Operational Metadata 列质量异常、数据量、访问事件和产生它们的工具。全图没有箭头。

## 关键含义（历史解释；局部修正见上）

- 7 个元数据域：数据术语表/政策/质量、业务流程、安全管理、应用存储库、数据隐私、风险管理、参考数据。
- 同一类资产会跨域出现：Control 同时出现在安全管理与风险管理，Process/Activity 同时出现在业务流程与数据隐私，说明“域”是视角而非互斥分区。
- 中部 “Data Documentation and Governance” 不属于任何单一域，它把业务数据域、角色、组织、数据分类、元数据关联、元数据活动日志作为贯穿各域的治理维度。
- 技术元数据框把资产（Database、Data Set、Data Field、Data Flow、Technical Data Deletion Rule、Technical Data Quality Rule）与数据形态（Relational、Analytical；Structured/Semi-structured/Unstructured data）并列，暗示形态决定采集方式。
- 运营元数据框用零散小方块示意事件流，资产是 Data Quality Anomaly、Data Volume、Data Access Event，由 BI & Analytics Platform 与 Administration & Monitoring Tools 产生。
- 图注说明这些元数据域是从用例中提炼后套用到本文语境的，因此清单是基线而非穷举；这与正文“分步推进”的建议一致。

## 层级（历史解释；局部修正见上）

两层：元数据域（L1，7 个并列列）→ 域内元数据资产（L2）。底部 Technical Metadata 与 Operational Metadata 是两个并列大类（L1），其下资产与数据形态为 L2。中部治理横带独立于所有域。

## 线条含义（历史解释；局部修正见上）

全图没有任何连线或箭头。归属由“标签在哪个域列/哪个大框内”表达；中部横带的位置表示它跨域适用；底部数据形态图标只是示意，不表示数据流。

## 易误读点（历史解释；局部修正见上）

- 不要把 7 列读成流程步骤或成熟度阶段，它们是并列的元数据域。
- 不要因为某资产在一个域出现就认为它只属于该域；Control、Process、Activity 都跨域重复。
- 不要把底部的数据库/文件图标当成数据流或系统接口，它们只是数据形态示意，没有箭头。
- 不要把中部横带当成第三个大类；它是一条治理标签带，横跨上方 7 个域。
- 中文稿 SVG 画的是“5 个来源系统 → 元数据存储库”，与本图的域/资产清单完全不同，不能据它理解本图。

## 元素

```json
[
  {
    "id": "d_glossary",
    "label_en": "Data Glossary, Policies, & Quality",
    "label_zh": "数据术语表、政策与质量",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 1 列",
    "description_zh": "该域提供术语、对象、元素、质量规则与政策类资产。"
  },
  {
    "id": "d_business_processes",
    "label_en": "Business Processes",
    "label_zh": "业务流程",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 2 列"
  },
  {
    "id": "d_security",
    "label_en": "Security Management",
    "label_zh": "安全管理",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 3 列"
  },
  {
    "id": "d_application_repo",
    "label_en": "Application Repository",
    "label_zh": "应用存储库",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 4 列"
  },
  {
    "id": "d_data_privacy",
    "label_en": "Data Privacy",
    "label_zh": "数据隐私",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 5 列"
  },
  {
    "id": "d_risk",
    "label_en": "Risk Management",
    "label_zh": "风险管理",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 6 列"
  },
  {
    "id": "d_reference_data",
    "label_en": "Reference Data",
    "label_zh": "参考数据",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 7 列"
  },
  {
    "id": "a_data_glossary",
    "label_en": "Data Glossary",
    "label_zh": "数据术语表",
    "type": "artifact",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_modeling_tools",
    "label_en": "Modeling Tools",
    "label_zh": "建模工具",
    "type": "application",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_business_term",
    "label_en": "Business Term",
    "label_zh": "业务术语",
    "type": "data",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_business_data_object",
    "label_en": "Business Data Object",
    "label_zh": "业务数据对象",
    "type": "data",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_business_data_element",
    "label_en": "Business Data Element",
    "label_zh": "业务数据元素",
    "type": "data",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_business_dq_rule",
    "label_en": "Business Data Quality Rule",
    "label_zh": "业务数据质量规则",
    "type": "principle",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_data_policy",
    "label_en": "Data Policy",
    "label_zh": "数据政策",
    "type": "principle",
    "parent": "d_glossary",
    "level": 2
  },
  {
    "id": "a_bp_modeling_tools",
    "label_en": "Business Processes Modeling Tools",
    "label_zh": "业务流程建模工具",
    "type": "application",
    "parent": "d_business_processes",
    "level": 2
  },
  {
    "id": "a_business_rule",
    "label_en": "Business Rule",
    "label_zh": "业务规则",
    "type": "principle",
    "parent": "d_business_processes",
    "level": 2
  },
  {
    "id": "a_process",
    "label_en": "Process",
    "label_zh": "流程",
    "type": "process",
    "parent": "d_business_processes",
    "level": 2
  },
  {
    "id": "a_activity",
    "label_en": "Activity",
    "label_zh": "活动",
    "type": "process",
    "parent": "d_business_processes",
    "level": 2
  },
  {
    "id": "a_security_repo",
    "label_en": "Security Management Repositories",
    "label_zh": "安全管理存储库",
    "type": "artifact",
    "parent": "d_security",
    "level": 2
  },
  {
    "id": "a_security_control",
    "label_en": "Control",
    "label_zh": "控制",
    "type": "risk",
    "parent": "d_security",
    "level": 2
  },
  {
    "id": "a_confidentiality",
    "label_en": "Confidentiality Classification",
    "label_zh": "保密性分级",
    "type": "data",
    "parent": "d_security",
    "level": 2
  },
  {
    "id": "a_app_repo",
    "label_en": "Application Metadata Repositories",
    "label_zh": "应用元数据存储库",
    "type": "artifact",
    "parent": "d_application_repo",
    "level": 2
  },
  {
    "id": "a_application",
    "label_en": "Application",
    "label_zh": "应用",
    "type": "application",
    "parent": "d_application_repo",
    "level": 2
  },
  {
    "id": "a_app_data_flow",
    "label_en": "Data Flow",
    "label_zh": "数据流",
    "type": "data",
    "parent": "d_application_repo",
    "level": 2
  },
  {
    "id": "a_privacy_registries",
    "label_en": "Data Privacy Registries",
    "label_zh": "数据隐私登记册",
    "type": "artifact",
    "parent": "d_data_privacy",
    "level": 2
  },
  {
    "id": "a_processing_activity",
    "label_en": "Data Processing Activity",
    "label_zh": "数据处理活动",
    "type": "process",
    "parent": "d_data_privacy",
    "level": 2
  },
  {
    "id": "a_privacy_assessment",
    "label_en": "Data Privacy Assessment",
    "label_zh": "数据隐私评估",
    "type": "artifact",
    "parent": "d_data_privacy",
    "level": 2
  },
  {
    "id": "a_business_deletion_rule",
    "label_en": "Business Data Deletion Rule",
    "label_zh": "业务数据删除规则",
    "type": "principle",
    "parent": "d_data_privacy",
    "level": 2
  },
  {
    "id": "a_privacy_classification",
    "label_en": "Privacy Classification",
    "label_zh": "隐私分级",
    "type": "data",
    "parent": "d_data_privacy",
    "level": 2
  },
  {
    "id": "a_risk_registries",
    "label_en": "Risk Management Registries",
    "label_zh": "风险管理登记册",
    "type": "artifact",
    "parent": "d_risk",
    "level": 2
  },
  {
    "id": "a_risk_committee",
    "label_en": "Committee",
    "label_zh": "委员会",
    "type": "organization_unit",
    "parent": "d_risk",
    "level": 2
  },
  {
    "id": "a_risk_control",
    "label_en": "Control",
    "label_zh": "控制",
    "type": "risk",
    "parent": "d_risk",
    "level": 2
  },
  {
    "id": "a_risk_process",
    "label_en": "Process",
    "label_zh": "流程",
    "type": "process",
    "parent": "d_risk",
    "level": 2
  },
  {
    "id": "a_reference_repo",
    "label_en": "Reference Data Repository",
    "label_zh": "参考数据存储库",
    "type": "artifact",
    "parent": "d_reference_data",
    "level": 2
  },
  {
    "id": "a_code_set",
    "label_en": "Code Set",
    "label_zh": "代码集",
    "type": "data",
    "parent": "d_reference_data",
    "level": 2
  },
  {
    "id": "a_code_value",
    "label_en": "Code Value",
    "label_zh": "代码值",
    "type": "data",
    "parent": "d_reference_data",
    "level": 2
  },
  {
    "id": "grp_governance_band",
    "label_en": "Data Documentation and Governance",
    "label_zh": "数据文档化与治理",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "中部通栏横带",
    "description_zh": "跨域的治理标签带。"
  },
  {
    "id": "g_business_domain",
    "label_en": "Business Data Domain",
    "label_zh": "业务数据域",
    "type": "data",
    "parent": "grp_governance_band",
    "level": 2
  },
  {
    "id": "g_role",
    "label_en": "Role",
    "label_zh": "角色",
    "type": "role",
    "parent": "grp_governance_band",
    "level": 2
  },
  {
    "id": "g_organization",
    "label_en": "Organization",
    "label_zh": "组织",
    "type": "organization_unit",
    "parent": "grp_governance_band",
    "level": 2
  },
  {
    "id": "g_data_classification",
    "label_en": "Data Classification",
    "label_zh": "数据分类",
    "type": "data",
    "parent": "grp_governance_band",
    "level": 2
  },
  {
    "id": "g_metadata_association",
    "label_en": "Metadata Association",
    "label_zh": "元数据关联",
    "type": "artifact",
    "parent": "grp_governance_band",
    "level": 2
  },
  {
    "id": "g_activity_logs",
    "label_en": "Metadata Activity Logs",
    "label_zh": "元数据活动日志",
    "type": "data",
    "parent": "grp_governance_band",
    "level": 2
  },
  {
    "id": "grp_technical",
    "label_en": "Technical Metadata",
    "label_zh": "技术元数据",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左下大框"
  },
  {
    "id": "t_database",
    "label_en": "Database",
    "label_zh": "数据库",
    "type": "data",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_data_set",
    "label_en": "Data Set",
    "label_zh": "数据集",
    "type": "data",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_data_field",
    "label_en": "Data Field",
    "label_zh": "数据字段",
    "type": "data",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_data_flow",
    "label_en": "Data Flow",
    "label_zh": "数据流",
    "type": "data",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_deletion_rule",
    "label_en": "Technical Data Deletion Rule",
    "label_zh": "技术数据删除规则",
    "type": "principle",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_dq_rule",
    "label_en": "Technical Data Quality Rule",
    "label_zh": "技术数据质量规则",
    "type": "principle",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_bi_platform",
    "label_en": "BI & Analytics Platform",
    "label_zh": "BI 与分析平台",
    "type": "application",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_integration_tools",
    "label_en": "Data Integration Tools",
    "label_zh": "数据集成工具",
    "type": "application",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_db_tools",
    "label_en": "Database Management & System Catalog",
    "label_zh": "数据库管理与系统目录",
    "type": "application",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_relational",
    "label_en": "Relational",
    "label_zh": "关系型",
    "type": "data",
    "parent": "grp_technical",
    "level": 2,
    "position": "结构化数据图标下"
  },
  {
    "id": "t_analytical",
    "label_en": "Analytical",
    "label_zh": "分析型",
    "type": "data",
    "parent": "grp_technical",
    "level": 2,
    "position": "结构化数据图标下"
  },
  {
    "id": "t_structured",
    "label_en": "STRUCTURED DATA",
    "label_zh": "结构化数据",
    "type": "note",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_semi_structured",
    "label_en": "SEMI-STRUCTURED DATA",
    "label_zh": "半结构化数据",
    "type": "note",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "t_unstructured",
    "label_en": "UNSTRUCTURED DATA",
    "label_zh": "非结构化数据",
    "type": "note",
    "parent": "grp_technical",
    "level": 2
  },
  {
    "id": "grp_operational",
    "label_en": "Operational Metadata",
    "label_zh": "运营元数据",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右下大框"
  },
  {
    "id": "o_dq_anomaly",
    "label_en": "Data Quality Anomaly",
    "label_zh": "数据质量异常",
    "type": "data",
    "parent": "grp_operational",
    "level": 2
  },
  {
    "id": "o_data_volume",
    "label_en": "Data Volume",
    "label_zh": "数据量",
    "type": "metric",
    "parent": "grp_operational",
    "level": 2
  },
  {
    "id": "o_access_event",
    "label_en": "Data Access Event",
    "label_zh": "数据访问事件",
    "type": "event",
    "parent": "grp_operational",
    "level": 2
  },
  {
    "id": "o_bi_platform",
    "label_en": "BI & Analytics Platform",
    "label_zh": "BI 与分析平台",
    "type": "application",
    "parent": "grp_operational",
    "level": 2
  },
  {
    "id": "o_admin_tools",
    "label_en": "Administration & Monitoring Tools",
    "label_zh": "管理与监控工具",
    "type": "application",
    "parent": "grp_operational",
    "level": 2
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_domains",
    "title_zh": "元数据域 × 域内元数据资产（按原图逐列转录）",
    "columns": [
      "元数据域",
      "域内元数据资产"
    ],
    "rows": [
      [
        "Data Glossary, Policies, & Quality 数据术语表、政策与质量",
        "Data Glossary；Modeling Tools；Business Term；Business Data Object；Business Data Element；Business Data Quality Rule；Data Policy"
      ],
      [
        "Business Processes 业务流程",
        "Business Processes Modeling Tools；Business Rule；Process；Activity"
      ],
      [
        "Security Management 安全管理",
        "Security Management Repositories；Control；Confidentiality Classification"
      ],
      [
        "Application Repository 应用存储库",
        "Application Metadata Repositories；Application；Data Flow"
      ],
      [
        "Data Privacy 数据隐私",
        "Data Privacy Registries；Data Processing Activity；Data Privacy Assessment；Business Data Deletion Rule；Privacy Classification"
      ],
      [
        "Risk Management 风险管理",
        "Risk Management Registries；Committee；Control；Process"
      ],
      [
        "Reference Data 参考数据",
        "Reference Data Repository；Code Set；Code Value"
      ]
    ],
    "notes_zh": "行序即原图从左到右的列序；同一资产名可出现在多个域。"
  },
  {
    "id": "t_bottom_groups",
    "title_zh": "底部两大元数据类别及其资产",
    "columns": [
      "类别",
      "资产与形态"
    ],
    "rows": [
      [
        "Technical Metadata 技术元数据",
        "Database；Data Set；Data Field；Data Flow；Technical Data Deletion Rule；Technical Data Quality Rule；BI & Analytics Platform；Data Integration Tools；Database Management & System Catalog；数据形态：Relational、Analytical（STRUCTURED DATA）、SEMI-STRUCTURED DATA、UNSTRUCTURED DATA"
      ],
      [
        "Operational Metadata 运营元数据",
        "Data Quality Anomaly；Data Volume；Data Access Event；BI & Analytics Platform；Administration & Monitoring Tools"
      ]
    ],
    "notes_zh": "Technical Metadata 框内的数据形态由数据库/文件图标示意，不是可点击资产标签。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "列标题 + 列内灰底标签",
    "meaning_zh": "一个元数据域及其可提供的元数据资产",
    "explicit": false
  },
  {
    "symbol": "青绿色横带",
    "meaning_zh": "Data Documentation and Governance：跨域治理标签",
    "explicit": true
  },
  {
    "symbol": "数据库圆柱图标",
    "meaning_zh": "关系型数据库/分析型数据存储",
    "explicit": false
  },
  {
    "symbol": "散落小方块",
    "meaning_zh": "运营事件或非结构化数据对象示意",
    "explicit": false
  },
  {
    "symbol": "大框标题 Technical Metadata / Operational Metadata",
    "meaning_zh": "元数据的两大类别",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "上部 7 列等宽域面板横向排列；中部一条通栏治理横带；下部左右两个大框（左 Technical Metadata、右 Operational Metadata），左框内再按上中下排三类数据形态。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-2",
    "relation": "precedes",
    "note_zh": "图 4-1 列出元数据域与资产，图 4-2 接着说明如何从这些来源收集需求"
  },
  {
    "target": "G234/fig4-5",
    "relation": "complements",
    "note_zh": "图 4-5 用矩阵重新组织关键元数据资产，可作为本图资产清单的类型化视图"
  },
  {
    "target": "G234/fig4-10",
    "relation": "related",
    "note_zh": "本图底部技术元数据的数据形态（结构化/半结构化/非结构化）在图 4-10 展开为采集与推断方式"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图资产标签的字距很小，个别空格在 PDF 中缺失（如 BusinessTerm），本分析按正常英文词距记录。",
    "“Data Documentation and Governance” 横带属于图内元素还是图题的一部分，版式上无边框区分；按图内横带处理。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页原图截图（2x2 与 3x3 放大分块）",
    "英文 PDF 第 22–23 页正文",
    "中文稿 G234e_信息架构_元数据管理.md 第 226–231 行",
    "figs/g234_fig4-1.svg 源码"
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
