# G21B/tab4-6 · 表 4-6：C-MDM 路线图步骤（plateau）

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/tab4-6.md) · [JSON](../../architecture/diagrams/G21B/tab4-6.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 34 页

![英文原图](../assets/G21B/tab4-6-p0034.png)

PDF 坐标：`[51.2, 130.7, 199.9, 399.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Engagement
ore Bu:
Operational
Operational
Data
Data
No
Kemel
os
Customer
{
Data
= Analytics
Customer
```

## 原图 · PDF 第 35 页

![英文原图](../assets/G21B/tab4-6-p0035.png)

PDF 坐标：`[51.2, 111.7, 199.9, 360.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
-
@
\gagement
ore Business
Operational
Operational
Data
Data
Se
+ -
et -
‘Customer
Analytics
Data
```

## 原图 · PDF 第 36 页

![英文原图](../assets/G21B/tab4-6-p0036-r03.png)

PDF 坐标：`[51.2, 98.2, 199.9, 349.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
proweoneoensce=
¥
v
agement |
‘ore Business
‘Operational
'
‘Operational
Data
'®
Data
conte
Analytics
Customer
```

## 原图 · PDF 第 36 页

![英文原图](../assets/G21B/tab4-6-p0036-r04.png)

PDF 坐标：`[51.2, 449.7, 199.9, 700.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
gagement
f
‘ore Business
Operational
Data
'
$ bas
Data
s-
$ Sas
Customer
Data
```

## 概要（历史解释；局部修正见上）

逐行说明四个 C-MDM plateau 的总述、用例、数据质量与触发条件，并在左侧嵌入对应数据流小图。

## 目的（历史解释；局部修正见上）

把图 4-2 的四个路线图步骤展开成可执行的规划说明：每一步做到什么、支持哪些用例、数据质量达到什么水平、以及什么条件触发进入下一步；嵌入的小图让人不必回看图 4-2 就能看出该步骤的数据流与绿色变化。

## 阅读顺序（历史解释；局部修正见上）

逐行从上到下读四个 plateau。左列是步骤名 + 小图（图内绿色=本步骤变化）；右列先读第一段总述（该步骤的定位与关键做法），再读 Use cases（能用它做什么）、Data quality（质量达到什么程度）、Trigger for next step（为什么进入下一步）。四行构成一条演进链，最后一行 C-MDM Target 没有触发条件，因为它是目标态。

## 关键含义（历史解释；局部修正见上）

- Step 1 是“整合客户数据库”：集中存储但没有真正黄金记录，去重效果差、质量差；小图里内核为绿色、两个运营库向内汇聚。
- Step 2 是“非侵入式真相点”：分析型 C-MDM，为每个唯一个人给出黄金记录并分配稳定客户 ID；内核可 CRUD，黄金记录可传播但不同步；中央团队开始承担数据管家职责。
- Step 3 是“主数据真相点”：运营型 C-MDM，内核在 C-MDM 中更新，自动化流程传播变更；运营库 CRUD 全部变绿，库↔内核双向同步。
- C-MDM Target 是“全范围主数据真相点”：治理与数据管家制度化，覆盖全部业务线客户群体，C-MDM 成为信息系统核心；小图中两个运营库出现绿色顶环（只读副本）。
- 每一步的 Trigger 都是下一步的动因：质量与客户面流程（1→2）、并发更新与业务赞助（2→3）、持续沟通与系统逐个集成（3→目标）。
- 四个用例范围逐级扩大：从可容忍匹配误差的分析型用例（细分、市场份额、C360、部分活动管理），到互动告警与坐席视图，再到跨渠道一致体验与高级客户服务。
- 表格原文对 Step 2 的“中央 C-MDM 团队负责数据管家”一条重复了两次（PDF 排版重复），不是两个不同要点。
- 表下的注说明“黄金记录”的定义：组织认定为真相的客户数据值，即使其他系统中存在其他版本。

## 层级（历史解释；局部修正见上）

四行是四个时间上相继的 plateau（Step 1→2→3→C-MDM Target），不是包含关系。每行内部：左列步骤名 + 小图；右列描述分为总述/用例/数据质量/触发条件四个层级。小图内部是“运营团队—两个运营库—内核（含 Customer ID）—分析库—中央团队”的同一套元素。

## 线条含义（历史解释；局部修正见上）

小图沿用图 4-2 的记法：实线箭头=自动化数据流，虚线箭头=人工交互，双向箭头=同步事务；绿色=该步骤的变化；C/R/U/D 徽标=存储支持的创建/读取/更新/删除操作。表格本身没有连线，行与行之间靠上下顺序表达演进。

## 易误读点（历史解释；局部修正见上）

- 不要把四行读成四种可选的架构风格：它们是同一条迁移路线的四个阶段。
- Step 1 的“整合”不等于主数据管理：它只是把数据集中起来做分析，运营系统仍是数据主人。
- C-MDM Target 行没有 Trigger，不代表它不重要，而是路线图的终点（目标态）。
- 小图是图 4-2 对应面板的裁剪版，绿色含义相同；不要把小图中的绿色顶环理解为“数据库被替换”。

## 元素

```json
[
  {
    "id": "row_step1",
    "label_en": "Step 1: Consolidated Customer Database",
    "label_zh": "步骤 1：整合客户数据库",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 1
  },
  {
    "id": "row_step2",
    "label_en": "Step 2: Non-intrusive Customer Data Point of Truth",
    "label_zh": "步骤 2：非侵入式客户数据真相点",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 2
  },
  {
    "id": "row_step3",
    "label_en": "Step 3: Master Point of Truth",
    "label_zh": "步骤 3：主数据真相点",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 3
  },
  {
    "id": "row_target",
    "label_en": "C-MDM Target",
    "label_zh": "C-MDM 目标",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 4
  },
  {
    "id": "d1",
    "label_en": null,
    "label_zh": "步骤 1 内嵌小图",
    "type": "group",
    "parent": "row_step1",
    "level": 2
  },
  {
    "id": "d2",
    "label_en": null,
    "label_zh": "步骤 2 内嵌小图",
    "type": "group",
    "parent": "row_step2",
    "level": 2
  },
  {
    "id": "d3",
    "label_en": null,
    "label_zh": "步骤 3 内嵌小图",
    "type": "group",
    "parent": "row_step3",
    "level": 2
  },
  {
    "id": "d4",
    "label_en": null,
    "label_zh": "C-MDM 目标内嵌小图",
    "type": "group",
    "parent": "row_target",
    "level": 2
  },
  {
    "id": "m_ops_team",
    "label_en": "Operational teams",
    "label_zh": "运营团队",
    "type": "actor",
    "parent": null,
    "position": "每张小图的顶部与底部",
    "description_zh": "标签来自图 4-2 图例。"
  },
  {
    "id": "m_central_team",
    "label_en": "C-MDM central team",
    "label_zh": "C-MDM 中央团队",
    "type": "organization_unit",
    "parent": null,
    "position": "每张小图右侧"
  },
  {
    "id": "m_eng_data",
    "label_en": "Engagement Operational Data",
    "label_zh": "互动运营数据",
    "type": "data",
    "parent": null,
    "position": "每张小图左上"
  },
  {
    "id": "m_core_data",
    "label_en": "Core Business Operational Data",
    "label_zh": "核心业务运营数据",
    "type": "data",
    "parent": null,
    "position": "每张小图右上"
  },
  {
    "id": "m_kernel",
    "label_en": "Kernel Customer Data",
    "label_zh": "内核客户数据",
    "type": "data",
    "parent": null,
    "position": "每张小图中部"
  },
  {
    "id": "m_customer_id",
    "label_en": "Customer ID",
    "label_zh": "客户 ID",
    "type": "data",
    "parent": "m_kernel",
    "level": 2,
    "position": "步骤 2–4 小图内核内的绿色/蓝色横条"
  },
  {
    "id": "m_analytics",
    "label_en": "Analytics Customer Data",
    "label_zh": "分析客户数据",
    "type": "data",
    "parent": null,
    "position": "每张小图下方"
  }
]
```

## 关系

```json
[
  {
    "id": "d1_1",
    "from": "m_ops_team",
    "to": "m_eng_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，人工交互（灰）。"
  },
  {
    "id": "d1_2",
    "from": "m_ops_team",
    "to": "m_core_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，人工交互（灰）。"
  },
  {
    "id": "d1_3",
    "from": "m_eng_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，绿色自动化流。"
  },
  {
    "id": "d1_4",
    "from": "m_core_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，绿色自动化流。"
  },
  {
    "id": "d1_5",
    "from": "m_kernel",
    "to": "m_analytics",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，绿色自动化流。"
  },
  {
    "id": "d1_6",
    "from": "m_kernel",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，绿色自动化流。"
  },
  {
    "id": "d1_7",
    "from": "m_analytics",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，绿色虚线人工交互。"
  },
  {
    "id": "d1_8",
    "from": "m_analytics",
    "to": "m_ops_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 1 小图，向下指向底部运营团队。"
  },
  {
    "id": "d2_1",
    "from": "m_ops_team",
    "to": "m_eng_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色人工交互。"
  },
  {
    "id": "d2_2",
    "from": "m_ops_team",
    "to": "m_core_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色人工交互。"
  },
  {
    "id": "d2_3",
    "from": "m_eng_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色自动化流。"
  },
  {
    "id": "d2_4",
    "from": "m_core_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色自动化流。"
  },
  {
    "id": "d2_5",
    "from": "m_kernel",
    "to": "m_eng_data",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，绿色反向传播（不同步）。"
  },
  {
    "id": "d2_6",
    "from": "m_kernel",
    "to": "m_core_data",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，绿色反向传播（不同步）。"
  },
  {
    "id": "d2_7",
    "from": "m_central_team",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，绿色虚线回写。"
  },
  {
    "id": "d2_8",
    "from": "m_central_team",
    "to": "m_ops_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，绿色虚线绕顶部指向运营团队。"
  },
  {
    "id": "d2_9",
    "from": "m_kernel",
    "to": "m_analytics",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色。"
  },
  {
    "id": "d2_10",
    "from": "m_analytics",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色虚线。"
  },
  {
    "id": "d2_11",
    "from": "m_analytics",
    "to": "m_ops_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 2 小图，灰色虚线。"
  },
  {
    "id": "d3_1",
    "from": "m_ops_team",
    "to": "m_eng_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色人工交互。"
  },
  {
    "id": "d3_2",
    "from": "m_ops_team",
    "to": "m_core_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色人工交互。"
  },
  {
    "id": "d3_3",
    "from": "m_eng_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "步骤 3 小图，绿色双向同步。"
  },
  {
    "id": "d3_4",
    "from": "m_core_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "步骤 3 小图，绿色双向同步。"
  },
  {
    "id": "d3_5",
    "from": "m_ops_team",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，绿色虚线直接录入内核。"
  },
  {
    "id": "d3_6",
    "from": "m_kernel",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色虚线。"
  },
  {
    "id": "d3_7",
    "from": "m_central_team",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色虚线。"
  },
  {
    "id": "d3_8",
    "from": "m_kernel",
    "to": "m_analytics",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色。"
  },
  {
    "id": "d3_9",
    "from": "m_analytics",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色虚线。"
  },
  {
    "id": "d3_10",
    "from": "m_analytics",
    "to": "m_ops_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "步骤 3 小图，灰色虚线。"
  },
  {
    "id": "d4_1",
    "from": "m_ops_team",
    "to": "m_eng_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色人工交互。"
  },
  {
    "id": "d4_2",
    "from": "m_ops_team",
    "to": "m_core_data",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色人工交互。"
  },
  {
    "id": "d4_3",
    "from": "m_ops_team",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色虚线直接录入。"
  },
  {
    "id": "d4_4",
    "from": "m_eng_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色（只读副本回传）。"
  },
  {
    "id": "d4_5",
    "from": "m_core_data",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色。"
  },
  {
    "id": "d4_6",
    "from": "m_kernel",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色虚线。"
  },
  {
    "id": "d4_7",
    "from": "m_central_team",
    "to": "m_kernel",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色虚线。"
  },
  {
    "id": "d4_8",
    "from": "m_kernel",
    "to": "m_analytics",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色。"
  },
  {
    "id": "d4_9",
    "from": "m_analytics",
    "to": "m_central_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色虚线。"
  },
  {
    "id": "d4_10",
    "from": "m_analytics",
    "to": "m_ops_team",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "C-MDM 目标小图，灰色虚线。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "roadmap_rows",
    "kind": "sequence",
    "name_zh": "表 4-6 的四个 plateau",
    "steps": [
      "row_step1",
      "row_step2",
      "row_step3",
      "row_target"
    ],
    "description_zh": "四行按时间顺序演进，每行的 Trigger 指明进入下一行的条件。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_roadmap",
    "title_zh": "表 4-6 C-MDM 路线图步骤（逐行转录，Description 单元格按原文分段）",
    "columns": [
      "步骤（plateau）",
      "总述",
      "用例 Use cases",
      "数据质量 Data quality",
      "进入下一步的触发条件 Trigger for next step"
    ],
    "rows": [
      [
        "Step 1: Consolidated Customer Database（步骤 1：整合客户数据库）",
        "Central customer data store, but without true golden record (no effective de-duplication, poor data quality)。• Kernel customer data is updated in different operational systems。• This kernel data is consolidated in an initial version of C-MDM as a first version of customer golden records。",
        "• This first version enables use cases such as segmentation, market share analysis, C360 view, some campaign management use cases; these use cases can tolerate errors on the matching process (100% accuracy of the de-duplication is not mandatory)。",
        "• Matching algorithms are executed to evaluate customer duplicate rates。• Customers data quality dashboards are built to share insights on customer data quality: completeness, uniqueness, consistency, etc.。",
        "• Need to improve data quality and support customer-facing business processes。（表下注：客户的“黄金记录”是组织认定为真相的客户数据值，即使其他系统中可能存在其他版本。）"
      ],
      [
        "Step 2: Non-intrusive Customer Data Point of Truth（步骤 2：非侵入式客户数据真相点）",
        "Analytical C-MDM focused on golden record, de-duplication, and data quality improvement。• Kernel data is still updated in different operational systems。• C-MDM provides a golden record for each identified unique person and attributes a stable organization customer ID; this golden record can be propagated in operational systems but is not synchronized。• A dedicated central C-MDM team is responsible for data stewardship including confirming de-duplication, analyzing data quality issues, data correction, and completion（原文该条重复出现两次，为排版重复）。",
        "• Address engagement use cases: send automatic alerts to the CRM system on new address or bad address detection, display golden record to agents。",
        "• Some data quality issues are tackled at root cause in the operational source system thanks to manual feedback loops of the central C-MDM team。• Data quality increases。",
        "• Concurrent updates generate workload that creates an appetite for more integration; the value of shared customer data is obvious for lines of business and allows sponsorship for higher impact on the information system。"
      ],
      [
        "Step 3: Master Point of Truth（步骤 3：主数据真相点）",
        "Operational C-MDM progressively extending its mastership scope on the information system。• Kernel customer data is updated in C-MDM (through different integration patterns: services, real-time synchronization, user interfaces, etc.)。• Automated processes/workflows propagate data changes。",
        "• Indicators are accurate, such as number of customers。• The operational business processes and applications in the core business or engagement are reviewed to leverage the customer golden record; this allows consistent customer experience across channels。• Customer data quality becomes a competitive advantage in business partnerships and allows advanced customer services。",
        "• Data quality is reaching expected target level – high integration comes with high data quality requirements: a wrong merge can lead to a crisis。",
        "• Continuous communication on C-MDM value is done to secure sponsorship over several years – operational systems are integrated one by one, increasing the scope of customer data。"
      ],
      [
        "C-MDM Target（C-MDM 目标）",
        "Operational C-MDM across the entire information system。• Governance and stewardship on customer data are institutionalized。• C-MDM covers the full scope of line of business customer populations: individuals, commercials, etc.。• C-MDM is a central piece of the information system; its value is proven。",
        "—（目标态，无单独用例段）",
        "—（目标态，无单独数据质量段）",
        "—（路线图终点，无触发条件）"
      ]
    ],
    "cell_legend": [
      "• 表示原文的项目符号",
      "— 表示原文该单元格无此段"
    ],
    "notes_zh": "原表为两列（Step / Description）；Description 单元格内以段落 + 项目符号分为总述、Use cases、Data quality、Trigger for next step，本表拆成五列以完整保留结构。中文稿表 4-6（L416–L419）已给出对应译文。"
  },
  {
    "id": "t_embedded_diagrams",
    "title_zh": "四行内嵌小图的差异（同一套元素，绿色=该步骤变化）",
    "columns": [
      "步骤",
      "内核 CRUD",
      "互动/核心运营库 CRUD",
      "分析库 CRUD",
      "与上一行相比的绿色变化"
    ],
    "rows": [
      [
        "Step 1",
        "R",
        "C R U D / C R U D",
        "R",
        "内核整体绿色；两个运营库→内核、内核→分析、内核→中央团队、分析→中央团队为绿色"
      ],
      [
        "Step 2",
        "C R U D（C/U/D 绿）",
        "C R U D / C R U D",
        "R",
        "Customer ID 横条绿色；内核→两个运营库的反向传播、中央团队→内核、中央团队→运营团队的虚线为绿色"
      ],
      [
        "Step 3",
        "C R U D",
        "C R U D（全绿）/ C R U D（全绿）",
        "R",
        "两个运营库 CRUD 全绿；库↔内核双向同步、运营团队→内核直接录入为绿色"
      ],
      [
        "C-MDM Target",
        "C R U D",
        "C R U D / C R U D",
        "R",
        "两个运营库顶部绿色圆环（只读副本）；其余全部灰色"
      ]
    ],
    "cell_legend": [
      "CRUD = Create/Read/Update/Delete",
      "绿=该步骤变化"
    ],
    "notes_zh": "四张小图是图 4-2 对应面板去掉顶部 plateau 块后的裁剪版；元素与连线含义同图 4-2 图例。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色填充/线条",
    "meaning_zh": "该步骤相比上一步新增或变化的部分（小图内）",
    "explicit": true
  },
  {
    "symbol": "C / R / U / D",
    "meaning_zh": "Create / Read / Update / Delete，存储支持的基本操作（同图 4-2 图例）",
    "explicit": false
  },
  {
    "symbol": "人群图标",
    "meaning_zh": "运营团队 / C-MDM 中央团队（同图 4-2 图例）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "单列四行的两列表格：左列窄（步骤名 + 内嵌竖长小图），右列宽（说明文字）；四行自上而下对应 Step 1、Step 2、Step 3、C-MDM Target。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig4-2",
    "relation": "detail_of",
    "note_zh": "本表逐行说明图 4-2 的四个 plateau，并嵌入同样的步骤小图。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "表 4-6 的“C-MDM Target”行在原图中没有编号，本分析按第四行处理。",
    "Step 2 的描述在 PDF 中重复了一条项目符号，无法判断是原文错误还是抽取重复；本分析保留一次并注明。",
    "内嵌小图的 CRUD 徽标很小，个别字母（如步骤 1 内核的 R）依据放大截图判读。"
  ],
  "analyzed_from": [
    "英文 PDF 第 34、35、36 页表格截图（含四张内嵌小图）",
    "英文 PDF 第 34–36 页正文",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 412–419 行（表 4-6 译文）"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": null,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
