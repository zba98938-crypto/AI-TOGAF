# G238/fig3-4 · 步骤 4——目标架构

> 当前图示解析：[Markdown](../../architecture/diagrams/G238/fig3-4.md) · [JSON](../../architecture/diagrams/G238/fig3-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G238e.pdf`；SHA-256：`87e00e009377a887627417ceffc28b1f480bfaf57c9c84ee6f8757cc5c1c9444`。

## 原图 · PDF 第 25 页

![英文原图](../assets/G238/fig3-4-p0025.png)

PDF 坐标：`[48.2, 105.8, 563.8, 482.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business Intelligence & Analytics Data Platforms
=a
Enterprise
Data
Warehouse
seenen
New
Transactional
Generation
Application
BI & Analytics
eanee
Including
wane
Data Platforms
Embedded
BI & Analytic
Capabi
‘ies
sanee
Connected
pesecanecee
Devices, Open
Data, Log.
=>
Inbound Flow
—>
Outbound Flow
O
As-Is Architecture
(i)
To-Be Architecture
```

## 概要（历史解释；局部修正见上）

目标架构：新一代平台吸收数仓，成为唯一历史数据源，并向全部集市/应用供数。

## 目的（历史解释；局部修正见上）

给出路线图的终点：说明为什么最终不应保留数仓与新平台两个历史库，以及目标状态下新平台如何覆盖数仓的全部范围（含统一企业数据模型）、向所有数据集市与既有应用供数，并成为历史数据的单一事实来源。

## 阅读顺序（历史解释；局部修正见上）

先看中央的大橙框：它就是 New Generation BI & Analytics Data Platforms，企业数据仓库被画在它内部，表示数仓的范围已被新平台覆盖，二者不再并列。左侧三个事务型应用与 Connected Devices 全部通过橙色虚线进入新平台，没有一条箭头指向旧数仓。右侧六个消费方分两类：Data Mart #1、#2 与 Application #1 是蓝框、琥珀色填充的既有资产，只收灰色实线；Data Mart #3、Application #2、Application #3 是橙框新资产，既有来自新平台的橙色实线，也有指回新平台的橙色虚线（回写）。

## 关键含义（历史解释；局部修正见上）

- 企业数据仓库不再是独立元素：它被画在新平台内部（橙框灰底），对应正文“新平台将覆盖数仓的完整范围，包括为分析需求构建的统一企业数据模型”。
- 所有数据源都直接进入新平台：三个事务型应用与 Connected Devices/Open Data/Log 均为橙色虚线入站流；图中没有任何事务型应用再直接向数仓供数。
- 新平台向 Data Mart #1/#2 和 Application #1 供数（灰色实线），这三个是保留下来的既有资产（蓝边框、琥珀色填充），正文称“现有数据集市接入新平台”。
- Data Mart #3、Application #2、Application #3 是目标状态的新消费方（橙框），既接收新平台数据，又通过橙色虚线把新产生的数据回写新平台。
- 目标是单一事实来源：新平台同时存储原始、集成与加工数据，覆盖历史数据；正文明确“同时保留数仓与新平台两个历史库不是可靠的目标愿景”。
- 平台范围大虚线框包含新平台、被吸收的数仓与全部集市/应用；数据源在框外。

## 层级（历史解释；局部修正见上）

三层：L1 平台范围容器；L2 新一代平台（含其内部的 L3 企业数据仓库）与 Data Mart #1/#2/#3、Application #1/#2/#3 并列；数据源（三个事务型应用、Connected Devices）在容器外。每个应用/集市的圆柱是其本地存储。EDW 的嵌套表示范围被覆盖，不是“EDW 是平台的子应用”。

## 线条含义（历史解释；局部修正见上）

橙色虚线箭头=入站流（所有数据源进入新平台）；灰色实线箭头=保留下来的既有出站流（新平台→Data Mart #1/#2、Application #1）；橙色实线箭头=目标出站流（新平台→Data Mart #3、Application #2/#3）；从 DM#3/App#2/App#3 指回新平台的橙色虚线=应用回写的入站流。图例只解释线型与蓝/橙框，未解释灰色与橙色箭头的区别。

## 易误读点（历史解释；局部修正见上）

- 不要把 EDW 画在新平台内部读成“EDW 是新平台的一个子应用”；它表示数仓的范围与职责被目标平台覆盖。
- 不要因为 DM#1/#2、App#1 是蓝框就认为它们仍是“现状未迁移”：它们是被保留并改由新平台供数的既有资产；琥珀色填充在图例中没有定义。
- 不要把灰色实线当成已废弃的旧流：它表示保留下来的既有供数关系，箭头仍指向现有集市/应用。
- 不要把 DM#3/App#2/App#3 的回写虚线读成查询请求或双向同步；它是应用产生的新数据经摄取进入平台以保留历史。
- 目标图中没有任何数据源再直接连数仓，若把 EDW 当作仍在独立接收数据就会误读目标状态。
- 中文稿引用的中文化 PNG 把第三个事务型应用框画成两条竖线、丢失出站流图例箭头，容易造成元素缺失的错觉。

## 元素

```json
[
  {
    "id": "platform_scope",
    "label_en": "Business Intelligence & Analytics Data Platforms",
    "label_zh": "商业智能与分析数据平台",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "大虚线框",
    "description_zh": "平台范围边界。"
  },
  {
    "id": "txn_app_1",
    "label_en": "Transactional Application #1",
    "label_zh": "事务型应用 #1",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左上",
    "description_zh": "蓝框；直接向新平台供数。"
  },
  {
    "id": "txn_app_2",
    "label_en": "Transactional Application #2",
    "label_zh": "事务型应用 #2",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左中",
    "description_zh": "蓝框；直接向新平台供数。"
  },
  {
    "id": "txn_app_bi",
    "label_en": "Transactional Application Including Embedded BI & Analytic Capabilities",
    "label_zh": "含内嵌 BI 与分析能力的事务型应用",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "蓝框；直接向新平台供数。"
  },
  {
    "id": "connected_devices",
    "label_en": "Connected Devices, Open Data, Log, ...",
    "label_zh": "互联设备、开放数据、日志等",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "橙框=目标数据源。"
  },
  {
    "id": "ng_platform",
    "label_en": "New Generation BI & Analytics Data Platforms",
    "label_zh": "新一代 BI 与分析数据平台",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "中央大橙框",
    "description_zh": "目标平台，吸收数仓并成为单一事实来源。"
  },
  {
    "id": "edw",
    "label_en": "Enterprise Data Warehouse",
    "label_zh": "企业数据仓库",
    "type": "data",
    "parent": "ng_platform",
    "level": 2,
    "position": "新平台内部上方",
    "description_zh": "橙框灰底；表示数仓范围被新平台覆盖，不再独立接收数据。"
  },
  {
    "id": "data_mart_1",
    "label_en": "Data Mart #1",
    "label_zh": "数据集市 #1",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右上",
    "description_zh": "蓝框、琥珀色填充；保留的既有集市，由新平台供数。"
  },
  {
    "id": "data_mart_2",
    "label_en": "Data Mart #2",
    "label_zh": "数据集市 #2",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右中上",
    "description_zh": "蓝框、琥珀色填充；保留的既有集市。"
  },
  {
    "id": "app_1",
    "label_en": "Application #1",
    "label_zh": "应用 #1",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右中",
    "description_zh": "蓝框、琥珀色填充；保留的既有应用，由新平台供数。"
  },
  {
    "id": "data_mart_3",
    "label_en": "Data Mart #3",
    "label_zh": "数据集市 #3",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下上",
    "description_zh": "橙框新集市；与新平台双向交换。"
  },
  {
    "id": "app_2",
    "label_en": "Application #2",
    "label_zh": "应用 #2",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下中",
    "description_zh": "橙框新应用；与新平台双向交换。"
  },
  {
    "id": "app_3",
    "label_en": "Application #3",
    "label_zh": "应用 #3",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下",
    "description_zh": "橙框新应用；与新平台双向交换。"
  },
  {
    "id": "db_txn_1",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "事务型应用 #1 右侧"
  },
  {
    "id": "db_txn_2",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "事务型应用 #2 右侧"
  },
  {
    "id": "db_txn_bi",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "内嵌 BI 应用左侧上"
  },
  {
    "id": "db_other_bi",
    "label_en": "Other",
    "label_zh": "其他",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "内嵌 BI 应用左侧下"
  },
  {
    "id": "db_dm_1",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Data Mart #1 右侧"
  },
  {
    "id": "db_dm_2",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Data Mart #2 右侧"
  },
  {
    "id": "db_app_1",
    "label_en": "Other",
    "label_zh": "其他",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Application #1 右侧",
    "description_zh": "圆柱标注 Other，而非 RDBMS。"
  },
  {
    "id": "db_dm_3",
    "label_en": "RDBMS or NoSQL",
    "label_zh": "关系型数据库或 NoSQL",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Data Mart #3 右侧",
    "description_zh": "橙框圆柱=目标。"
  },
  {
    "id": "db_app_2",
    "label_en": "RDBMS or NoSQL",
    "label_zh": "关系型数据库或 NoSQL",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Application #2 右侧",
    "description_zh": "橙框圆柱=目标。"
  },
  {
    "id": "db_app_3",
    "label_en": "RDBMS or NoSQL",
    "label_zh": "关系型数据库或 NoSQL",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Application #3 右侧",
    "description_zh": "橙框圆柱=目标。"
  }
]
```

## 关系

```json
[
  {
    "from": "txn_app_1",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线。"
  },
  {
    "from": "txn_app_2",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线。"
  },
  {
    "from": "txn_app_bi",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线。"
  },
  {
    "from": "connected_devices",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线。"
  },
  {
    "from": "ng_platform",
    "to": "data_mart_1",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "灰色实线；保留的既有供数关系。"
  },
  {
    "from": "ng_platform",
    "to": "data_mart_2",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "灰色实线。"
  },
  {
    "from": "ng_platform",
    "to": "app_1",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "灰色实线。"
  },
  {
    "from": "ng_platform",
    "to": "data_mart_3",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线。"
  },
  {
    "from": "data_mart_3",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线，箭头指向新平台。"
  },
  {
    "from": "ng_platform",
    "to": "app_2",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线。"
  },
  {
    "from": "app_2",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线，箭头指向新平台。"
  },
  {
    "from": "ng_platform",
    "to": "app_3",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线。"
  },
  {
    "from": "app_3",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "橙色虚线，箭头指向新平台。"
  },
  {
    "from": "txn_app_1",
    "to": "db_txn_1",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "圆柱紧贴宿主，原图未画线。"
  },
  {
    "from": "txn_app_2",
    "to": "db_txn_2",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "txn_app_bi",
    "to": "db_txn_bi",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "txn_app_bi",
    "to": "db_other_bi",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "data_mart_1",
    "to": "db_dm_1",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "data_mart_2",
    "to": "db_dm_2",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "app_1",
    "to": "db_app_1",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "data_mart_3",
    "to": "db_dm_3",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "app_2",
    "to": "db_app_2",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "app_3",
    "to": "db_app_3",
    "type": "access",
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
    "symbol": "橙色虚线 + 箭头",
    "meaning_zh": "入站流 Inbound Flow",
    "explicit": true
  },
  {
    "symbol": "灰色/橙色实线 + 箭头",
    "meaning_zh": "出站流 Outbound Flow",
    "explicit": true
  },
  {
    "symbol": "蓝色边框方框",
    "meaning_zh": "现状架构 As-Is Architecture",
    "explicit": true
  },
  {
    "symbol": "橙色边框方框",
    "meaning_zh": "目标架构 To-Be Architecture",
    "explicit": true
  },
  {
    "symbol": "圆柱",
    "meaning_zh": "RDBMS、RDBMS/NoSQL 或 Other 数据存储，紧贴宿主",
    "explicit": false
  },
  {
    "symbol": "琥珀色填充 + 蓝边框（Data Mart #1/#2、Application #1）",
    "meaning_zh": "既有、被保留下来的集市/应用（图例未解释填充色，按正文推断）",
    "explicit": false
  },
  {
    "symbol": "深蓝点线大框",
    "meaning_zh": "BI & Analytics 数据平台范围",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "左侧自上而下：三个事务型应用（蓝，各带 RDBMS/Other）与 Connected Devices/Open Data/Log（橙）。中央一个大的橙色圆角容器“New Generation BI & Analytics Data Platforms”，其内部上方嵌着一个橙色边框的企业数据仓库框。右侧自上而下：Data Mart #1、Data Mart #2、Application #1（蓝框、琥珀色填充），Data Mart #3、Application #2、Application #3（橙框、灰底），各带圆柱。大虚线框包住中央平台与右侧六个消费方。"
}
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "琥珀色填充只出现在 Data Mart #1/#2 与 Application #1，图例未解释；本分析按正文“现有数据集市接入新平台/保留既有投资”推断为“保留下来的既有资产”，不能确定作者是否另有编码。",
    "箭头灰/橙的区分没有图例说明；按“灰色=既有关系、橙色=新增/目标关系”解释。",
    "EDW 嵌套在新平台内的确切含义（范围覆盖 vs. 逻辑包含）正文支持“覆盖数仓完整范围”，但图形本身没有文字说明。",
    "Application #1 的存储圆柱标注为 Other，与步骤 1–3 中同一应用的 RDBMS 不同，原图未说明原因。"
  ],
  "analyzed_from": [
    "英文 PDF 第 25 页图 3-4 截图与 3×3 放大分块",
    "英文 PDF 第 24–25 页步骤 4 正文与表 3-5",
    "中文稿 G238e_信息架构_商业智能与分析.md 第 332–368 行",
    "figs/zh/g238e_fig3-4_zh.png、figs/g238e_fig3-4_en.png（相似度 0.988）"
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
