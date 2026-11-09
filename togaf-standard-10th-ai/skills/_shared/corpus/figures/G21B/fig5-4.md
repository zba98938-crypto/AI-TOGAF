# G21B/fig5-4 · C-MDM 详细应用功能参考模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig5-4.md) · [JSON](../../architecture/diagrams/G21B/fig5-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 45 页

![英文原图](../assets/G21B/fig5-4-p0045.png)

PDF 坐标：`[48.2, 62.3, 563.8, 550.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
C-MDM System Functions
A
Reference Data
Acquisition — User Interface or Services
A
Dashboards & (|
Management
Create
Update
Reports
Master
Master
Manage Links Between Master Entities and Other (~)
Business Objects
Data
Data
Manage
A
Manage Groups (~)
Relationships.
& Hierarchies
‘Audit Data
Generate ())
Evolution
Input Attributes
Transcodification
A
Import Data Set, Mass Acquisition
A
Reports
Enhance Data with Technical and Business Metadata
A
Manage
Reference List
A
Quality Management
Manage Business Validation & Workflows
A
‘Manage & Apply Attribute Value Quality Rules
A
Manage Syntax,
Manage Consistency and (~)
Manage Accuracy
A
Generate (9)
Format, Normalization
Business Rules
(Accuracy Score, External
Data Quality
Manage
A
Rules
Data)
Dashboards
Customer Key
Mapping
‘Manage Uniqueness Rules
Recommend
Manual
De-duplicate
with
De-duplicate
with
Unmerge ()
Determinist
‘babi
UStatist
‘Merges to
Arbitrate
Merge
Atbitrage
Process
Process
Output Attributes
Transcodification
A
Generate Unique Master Technical Key
Data Privacy Management
Generate)
Us
Ss
Manual Deletion
Dashboard
A
‘Automated Deletion with)
Masking
Rules
Distribution — User Interface or Service
Search
Push Events: Cre
A
Read Data (4)
Extract Data ()
A
Update, Delete, Merge
Contextualize Data Visibility & Provided Values Depending on Human or System Consumer Role
A
Administration
Design Master (>)
Manage Data Historization and (9)
Full Database (~)
Manage (4)
Manage Access (4)
Manage
Data Model
Versioning Rules
Versioning
Roles
Rights
Logging
```

## 概要（历史解释；局部修正见上）

把 C-MDM 系统的应用功能分解为 7 组 40 项，覆盖参考数据、采集、质量、隐私、分发、报表与管理。

## 目的（历史解释；局部修正见上）

第 5.2.2 节给出应用侧的详细参考模型：用稳定的通用语言描述 C-MDM 平台应覆盖的功能，可用于比较供应商功能覆盖、评估组织基线/目标应用架构、设计过渡架构或评估能力成熟度。图 5-4 是这 40 项功能的分类全景，逐项说明见表 5-4。

## 阅读顺序（历史解释；局部修正见上）

先看外层 C-MDM System Functions，说明这些功能都属于同一个系统边界。再按组读：左列 Reference Data Management 单独一列（4 项）；中部自上而下是采集、质量管理、数据隐私管理、分发四个主流程组；右列是 Dashboards & Reports；底部横贯 Administration。组内框是应用功能；带嵌套的框（如 Manage Links、Manage & Apply Attribute Value Quality Rules、Manage Uniqueness Rules）先读父功能，再读其中的子功能。

## 关键含义（历史解释；局部修正见上）

- 7 个功能组与 40 项功能：参考数据管理 4、采集 7、质量管理 12、数据隐私管理 3、分发 5、仪表盘与报表 3、管理 6。
- 采集组以 Create/Update Master Data 为入口，Manage Links Between Master Entities and Other Business Objects 下再分 Manage Relationships 与 Manage Groups & Hierarchies；Import Data Set, Mass Acquisition 与 Enhance Data with Technical and Business Metadata 是两条横贯的批量/元数据能力。
- 质量管理是最大的一组：先 Manage Business Validation & Workflows，再在 Manage & Apply Attribute Value Quality Rules 下分语法/格式/规范化、一致性/业务规则、准确性（准确性评分、外部数据），最后在 Manage Uniqueness Rules 下分确定性去重、概率/统计去重、推荐合并、人工合并仲裁、取消合并，并以 Generate Unique Master Technical Key 收口。
- 数据隐私管理只有三项：人工删除、按规则自动删除、掩码；对应保留/删除/脱敏三类隐私约束。
- 分发组包含 Search、Read Data、Extract Data、Push Events（创建/更新/删除/合并）四项取数方式，外加一条按人类或系统消费者角色呈现可见性与取值的横贯能力。
- 仪表盘与报表组三项：审计数据演进报表、数据质量仪表盘、用途（usage）仪表盘；与图 5-3 的“报告 C-MDM 业务价值”业务功能对应。
- 管理组六项：设计主数据模型、数据历史化与版本规则、全数据库版本管理、角色、访问权限、日志；这些是支撑上述所有功能的管理面。
- 原图的“De-duplicate with Probabilist/Statist Process”标签首字母 P 被左侧框线裁掉，显示为“obabilist/Statist”；中文重绘图已补全为“概率/统计流程去重”。

## 层级（历史解释；局部修正见上）

三层（局部四层）：第 1 层 C-MDM System Functions；第 2 层 7 个功能组；第 3 层 40 项应用功能；Manage Links、Manage & Apply Attribute Value Quality Rules、Manage Uniqueness Rules 三项下还有第 4 层子功能。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。分组由灰色大框包含表达；父子功能由框内嵌套表达（与第 2.1 节说明的 nesting 手法一致）；组与组之间的上下左右位置不表示调用顺序或数据流。

## 易误读点（历史解释；局部修正见上）

- 不要把 7 个功能组当成一条流水线：采集→质量→隐私→分发只是版式上的自上而下，功能之间没有画出的先后关系。
- 参考数据管理单独一列不代表它只在采集时使用；它同时是质量规则与界面控件的使能因素。
- 嵌套子功能不是可选的“高级功能”：如 Manage Uniqueness Rules 下的去重/合并子项共同构成唯一性管理。
- “Manage Links Between Master Entities and Other Business Objects”是父功能，Manage Relationships 与 Manage Groups & Hierarchies 是它的子项，不要读成三个并列功能。
- 中文稿的标签对照表缺了约 18 项，不能当作完整清单使用；完整清单以图或英文表 5-4 为准。

## 元素

```json
[
  {
    "id": "system_functions",
    "label_en": "C-MDM System Functions",
    "label_zh": "C-MDM 系统功能",
    "type": "application",
    "parent": null,
    "level": 1
  },
  {
    "id": "g_ref",
    "label_en": "Reference Data Management",
    "label_zh": "参考数据管理",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "g_acq",
    "label_en": "Acquisition – User Interface or Services",
    "label_zh": "采集——用户界面或服务",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "g_quality",
    "label_en": "Quality Management",
    "label_zh": "质量管理",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "g_privacy",
    "label_en": "Data Privacy Management",
    "label_zh": "数据隐私管理",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "g_dist",
    "label_en": "Distribution – User Interface or Service",
    "label_zh": "分发——用户界面或服务",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "g_dash",
    "label_en": "Dashboards & Reports",
    "label_zh": "仪表盘与报表",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "g_admin",
    "label_en": "Administration",
    "label_zh": "管理",
    "type": "group",
    "parent": "system_functions",
    "level": 2
  },
  {
    "id": "f_input_transcode",
    "label_en": "Input Attributes Transcodification",
    "label_zh": "输入属性转码",
    "type": "function",
    "parent": "g_ref",
    "level": 3
  },
  {
    "id": "f_ref_list",
    "label_en": "Manage Reference List",
    "label_zh": "管理参考列表",
    "type": "function",
    "parent": "g_ref",
    "level": 3
  },
  {
    "id": "f_key_mapping",
    "label_en": "Manage Customer Key Mapping",
    "label_zh": "管理客户键映射",
    "type": "function",
    "parent": "g_ref",
    "level": 3
  },
  {
    "id": "f_output_transcode",
    "label_en": "Output Attributes Transcodification",
    "label_zh": "输出属性转码",
    "type": "function",
    "parent": "g_ref",
    "level": 3
  },
  {
    "id": "f_create",
    "label_en": "Create Master Data",
    "label_zh": "创建主数据",
    "type": "function",
    "parent": "g_acq",
    "level": 3
  },
  {
    "id": "f_update",
    "label_en": "Update Master Data",
    "label_zh": "更新主数据",
    "type": "function",
    "parent": "g_acq",
    "level": 3
  },
  {
    "id": "f_links",
    "label_en": "Manage Links Between Master Entities and Other Business Objects",
    "label_zh": "管理主实体与其他业务对象之间的链接",
    "type": "function",
    "parent": "g_acq",
    "level": 3
  },
  {
    "id": "f_relationships",
    "label_en": "Manage Relationships",
    "label_zh": "管理关系",
    "type": "function",
    "parent": "f_links",
    "level": 4
  },
  {
    "id": "f_groups",
    "label_en": "Manage Groups & Hierarchies",
    "label_zh": "管理群组与层级",
    "type": "function",
    "parent": "f_links",
    "level": 4
  },
  {
    "id": "f_import",
    "label_en": "Import Data Set, Mass Acquisition",
    "label_zh": "导入数据集/批量采集",
    "type": "function",
    "parent": "g_acq",
    "level": 3
  },
  {
    "id": "f_metadata",
    "label_en": "Enhance Data with Technical and Business Metadata",
    "label_zh": "以技术与业务元数据增强数据",
    "type": "function",
    "parent": "g_acq",
    "level": 3
  },
  {
    "id": "f_validation_flow",
    "label_en": "Manage Business Validation & Workflows",
    "label_zh": "管理业务校验与工作流",
    "type": "function",
    "parent": "g_quality",
    "level": 3
  },
  {
    "id": "f_attr_rules",
    "label_en": "Manage & Apply Attribute Value Quality Rules",
    "label_zh": "管理与应用属性值质量规则",
    "type": "function",
    "parent": "g_quality",
    "level": 3
  },
  {
    "id": "f_syntax",
    "label_en": "Manage Syntax, Format, Normalization Rules",
    "label_zh": "管理语法、格式与规范化规则",
    "type": "function",
    "parent": "f_attr_rules",
    "level": 4
  },
  {
    "id": "f_consistency",
    "label_en": "Manage Consistency and Business Rules",
    "label_zh": "管理一致性与业务规则",
    "type": "function",
    "parent": "f_attr_rules",
    "level": 4
  },
  {
    "id": "f_accuracy",
    "label_en": "Manage Accuracy (Accuracy Score, External Data)",
    "label_zh": "管理准确性（准确性评分、外部数据）",
    "type": "function",
    "parent": "f_attr_rules",
    "level": 4
  },
  {
    "id": "f_uniqueness",
    "label_en": "Manage Uniqueness Rules",
    "label_zh": "管理唯一性规则",
    "type": "function",
    "parent": "g_quality",
    "level": 3
  },
  {
    "id": "f_dedup_det",
    "label_en": "De-duplicate with Determinist Process",
    "label_zh": "确定性流程去重",
    "type": "function",
    "parent": "f_uniqueness",
    "level": 4
  },
  {
    "id": "f_dedup_prob",
    "label_en": "De-duplicate with 'obabilist/Statist Process",
    "label_zh": "概率/统计流程去重",
    "type": "function",
    "parent": "f_uniqueness",
    "level": 4,
    "description_zh": "原图首字母 P 被框线裁掉，完整应为 Probabilist/Statist Process。"
  },
  {
    "id": "f_recommend_merge",
    "label_en": "Recommend Merges to Arbitrate",
    "label_zh": "推荐合并以供仲裁",
    "type": "function",
    "parent": "f_uniqueness",
    "level": 4
  },
  {
    "id": "f_manual_merge",
    "label_en": "Manual Merge Arbitrage",
    "label_zh": "人工合并仲裁",
    "type": "function",
    "parent": "f_uniqueness",
    "level": 4
  },
  {
    "id": "f_unmerge",
    "label_en": "Unmerge",
    "label_zh": "取消合并",
    "type": "function",
    "parent": "f_uniqueness",
    "level": 4
  },
  {
    "id": "f_unique_key",
    "label_en": "Generate Unique Master Technical Key",
    "label_zh": "生成唯一主数据技术键",
    "type": "function",
    "parent": "g_quality",
    "level": 3
  },
  {
    "id": "f_manual_delete",
    "label_en": "Manual Deletion",
    "label_zh": "人工删除",
    "type": "function",
    "parent": "g_privacy",
    "level": 3
  },
  {
    "id": "f_auto_delete",
    "label_en": "Automated Deletion with Rules",
    "label_zh": "按规则自动删除",
    "type": "function",
    "parent": "g_privacy",
    "level": 3
  },
  {
    "id": "f_masking",
    "label_en": "Masking",
    "label_zh": "掩码",
    "type": "function",
    "parent": "g_privacy",
    "level": 3
  },
  {
    "id": "f_search",
    "label_en": "Search",
    "label_zh": "搜索",
    "type": "function",
    "parent": "g_dist",
    "level": 3
  },
  {
    "id": "f_read",
    "label_en": "Read Data",
    "label_zh": "读取数据",
    "type": "function",
    "parent": "g_dist",
    "level": 3
  },
  {
    "id": "f_extract",
    "label_en": "Extract Data",
    "label_zh": "抽取数据",
    "type": "function",
    "parent": "g_dist",
    "level": 3
  },
  {
    "id": "f_push",
    "label_en": "Push Events: Create, Update, Delete, Merge",
    "label_zh": "推送事件：创建、更新、删除、合并",
    "type": "function",
    "parent": "g_dist",
    "level": 3
  },
  {
    "id": "f_context",
    "label_en": "Contextualize Data Visibility & Provided Values Depending on Human or System Consumer Role",
    "label_zh": "按人类或系统消费者角色呈现数据可见性与取值",
    "type": "function",
    "parent": "g_dist",
    "level": 3
  },
  {
    "id": "f_audit_reports",
    "label_en": "Generate Audit Data Evolution Reports",
    "label_zh": "生成审计数据演进报表",
    "type": "function",
    "parent": "g_dash",
    "level": 3
  },
  {
    "id": "f_dq_dashboard",
    "label_en": "Generate Data Quality Dashboards",
    "label_zh": "生成数据质量仪表盘",
    "type": "function",
    "parent": "g_dash",
    "level": 3
  },
  {
    "id": "f_usage_dashboard",
    "label_en": "Generate Usages Dashboard",
    "label_zh": "生成用途仪表盘",
    "type": "function",
    "parent": "g_dash",
    "level": 3
  },
  {
    "id": "f_design_model",
    "label_en": "Design Master Data Model",
    "label_zh": "设计主数据模型",
    "type": "function",
    "parent": "g_admin",
    "level": 3
  },
  {
    "id": "f_historization",
    "label_en": "Manage Data Historization and Versioning Rules",
    "label_zh": "管理数据历史化与版本规则",
    "type": "function",
    "parent": "g_admin",
    "level": 3
  },
  {
    "id": "f_db_versioning",
    "label_en": "Full Database Versioning",
    "label_zh": "全数据库版本管理",
    "type": "function",
    "parent": "g_admin",
    "level": 3
  },
  {
    "id": "f_roles",
    "label_en": "Manage Roles",
    "label_zh": "管理角色",
    "type": "function",
    "parent": "g_admin",
    "level": 3
  },
  {
    "id": "f_access_rights",
    "label_en": "Manage Access Rights",
    "label_zh": "管理访问权限",
    "type": "function",
    "parent": "g_admin",
    "level": 3
  },
  {
    "id": "f_logging",
    "label_en": "Manage Logging",
    "label_zh": "管理日志",
    "type": "function",
    "parent": "g_admin",
    "level": 3
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色圆角框 + 右上角折角箭头图标",
    "meaning_zh": "应用功能（ArchiMate Application Function）",
    "explicit": false
  },
  {
    "symbol": "灰色大框",
    "meaning_zh": "应用功能分组",
    "explicit": false
  },
  {
    "symbol": "框内嵌套小框",
    "meaning_zh": "父功能下的子功能（nesting）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "外层大框内：左列参考数据管理（4 项竖排）；中部自上而下采集、质量管理、数据隐私管理、分发四组；右列仪表盘与报表（3 项竖排）；底部横贯管理组（6 项）。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig5-3",
    "relation": "complements",
    "note_zh": "图 5-4 的应用功能（采集、质量、隐私、分发、报表、管理）支撑图 5-3 的业务功能（治理、设计、运营、扩展、度量、沟通）。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图“De-duplicate with 'obabilist/Statist Process”首字母被裁切，本分析按上下文补为 Probabilist/Statist 并在 label_en 保留可见文本。",
    "中文稿标签对照表漏列约 18 项，解读应以原图或英文表 5-4 为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 45 页原图截图",
    "英文 PDF 第 45 页正文与表 5-4 开头",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 632–673 行",
    "figs/zh/g21be_fig5-4_zh.svg 源码与渲染图"
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
