# G238/fig3-3 · 步骤 3——新一代平台成长

> 当前图示解析：[Markdown](../../architecture/diagrams/G238/fig3-3.md) · [JSON](../../architecture/diagrams/G238/fig3-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G238e.pdf`；SHA-256：`87e00e009377a887627417ceffc28b1f480bfaf57c9c84ee6f8757cc5c1c9444`。

## 原图 · PDF 第 22 页

![英文原图](../assets/G238/fig3-3-p0022.png)

PDF 坐标：`[48.2, 105.8, 563.8, 472.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business Intelligence & Analytics Data Platforms
—;,
:
Data Mart #1
Transactional
Enterprise
jon #2
Ap
Data
Warehouse
Transactional
Data Mart #2
Application
Including
Embedded
Application #1 Rosms
BI & Analytic
Capabilities
Data Mart #3 | RDBMS
New
Generation
Connected
BI & Analytics
Application #2, RoBms
Devices, Open
Data Platforms
or NoSQL
Data, Log,
—>
Inbound Flow
Outbound Flow
Application #3) Rosms
or NoSQL
As-Is Architecture
To-Be Architecture
```

## 概要（历史解释；局部修正见上）

过渡步骤 3：新平台成长为原始数据主库，更多集市与应用切换到新平台。

## 目的（历史解释；局部修正见上）

展示新平台成熟后的过渡状态：它开始保存原始/集成/加工数据并与数仓双向交换，逐步替代暂存区或 ODS，数据集市与应用按机会分步从数仓切走；同时说明“双份历史存储、双摄取流”的过渡代价（表 3-4）。

## 阅读顺序（历史解释；局部修正见上）

先看中央：上方是蓝框的企业数据仓库，下方是橙框的新一代平台，两者之间有两条方向相反的橙色实线箭头，表示双向交换。左侧事务型应用 #2 与内嵌 BI 应用同时有灰色箭头（指向数仓）和橙色虚线（指向新平台）；事务型应用 #1 只有橙色虚线。右侧 Application #1 收到来自数仓和新平台的两条橙色实线；Data Mart #1/#2 仍只收数仓的灰色实线；Data Mart #3 只收新平台；Application #2/#3 既有来自新平台的橙色实线，也有指回新平台的橙色虚线。

## 关键含义（历史解释；局部修正见上）

- 数仓与新平台之间出现一对方向相反的橙色实线箭头：数仓→新平台与新平台→数仓，表示两者双向交换数据（正文：新平台向数仓提供新数据并覆盖原始数据全貌）。
- 事务型应用 #1 只保留指向新平台的橙色虚线入站流，不再有指向数仓的灰色箭头；事务型应用 #2 与内嵌 BI 应用仍同时向数仓（灰色实线）和新平台（橙色虚线）供数。
- 应用 #1 已改为双供数：同时收到来自数仓和来自新平台的橙色实线箭头；Data Mart #3 只由新平台供数。
- Data Mart #1、Data Mart #2 仍只由数仓供数（灰色实线），尚未迁移。
- 应用 #2、应用 #3 与新平台之间是双向流：新平台向它们供数，它们又以橙色虚线把新产生的数据回写给新平台。
- 平台范围容器内已包含数仓、新平台与全部集市/应用；事务型应用与 Connected Devices 仍在范围外。
- 表 3-4 的缺失能力仍是历史数据双份存储、没有单一事实来源、需维护双摄取流、成本翻倍。

## 层级（历史解释；局部修正见上）

两层：平台范围容器包含企业数据仓库、新一代平台、Data Mart #1/#2/#3 与 Application #1/#2/#3；三个事务型应用与 Connected Devices 在容器外。每个应用/集市的圆柱是其本地存储。数仓与新平台是并列的两个历史数据存储，本步骤尚未合并。

## 线条含义（历史解释；局部修正见上）

橙色虚线箭头=入站流（事务型应用/联网设备进入新平台）；灰色实线箭头=现状出站流（数仓→DM#1/#2）；橙色实线箭头=目标出站流（数仓→App#1、数仓↔新平台、新平台→App#1/DM#3/App#2/App#3）；橙色虚线从 App#2/#3 指回新平台=应用回写的入站流。箭头指向接收方。

## 易误读点（历史解释；局部修正见上）

- 数仓与新平台之间的两条垂直箭头不是重复：一条向下（数仓→新平台），一条向上（新平台→数仓），表示双向交换。
- 不要把 App#2/App#3 指向新平台的橙色虚线读成平台向应用供数；箭头指向新平台，是应用回写的入站流。
- 事务型应用 #1 没有指向数仓的箭头，不应假定是漏画；图中它只向新平台供数，但正文没有解释这一变化的业务原因。
- 英文原文 p22 举例“Transaction Application #1”被两者同时供数，与图 3-3 不符：图中双供数的是右侧 Application #1，左侧 Transactional Application #1 只连新平台。以图为准。
- 不要把 Data Mart #1/#2 的灰色箭头当成已迁移：它们仍只由数仓供数，迁移是分步的。
- 中文稿引用的中文化 PNG 把第三个事务型应用框画成两条竖线，容易让人以为该元素被删除。

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
    "description_zh": "蓝框；只向新平台供数（无至数仓的箭头）。"
  },
  {
    "id": "txn_app_2",
    "label_en": "Transactional Application #2",
    "label_zh": "事务型应用 #2",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左中",
    "description_zh": "蓝框；同时向数仓与新平台供数。"
  },
  {
    "id": "txn_app_bi",
    "label_en": "Transactional Application Including Embedded BI & Analytic Capabilities",
    "label_zh": "含内嵌 BI 与分析能力的事务型应用",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "蓝框；同时向数仓与新平台供数。"
  },
  {
    "id": "connected_devices",
    "label_en": "Connected Devices, Open Data, Log, ...",
    "label_zh": "互联设备、开放数据、日志等",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "橙框=目标；新数据源。"
  },
  {
    "id": "edw",
    "label_en": "Enterprise Data Warehouse",
    "label_zh": "企业数据仓库",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "中央上",
    "description_zh": "蓝框灰底；仍保留的历史数据仓库。"
  },
  {
    "id": "ng_platform",
    "label_en": "New Generation BI & Analytics Data Platforms",
    "label_zh": "新一代 BI 与分析数据平台",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "中央下",
    "description_zh": "橙框灰底；已存储原始/集成/加工数据。"
  },
  {
    "id": "data_mart_1",
    "label_en": "Data Mart #1",
    "label_zh": "数据集市 #1",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右上",
    "description_zh": "蓝框；仍只由数仓供数。"
  },
  {
    "id": "data_mart_2",
    "label_en": "Data Mart #2",
    "label_zh": "数据集市 #2",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右中上",
    "description_zh": "蓝框；仍只由数仓供数。"
  },
  {
    "id": "app_1",
    "label_en": "Application #1",
    "label_zh": "应用 #1",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右中",
    "description_zh": "橙框；同时由数仓与新平台供数。"
  },
  {
    "id": "data_mart_3",
    "label_en": "Data Mart #3",
    "label_zh": "数据集市 #3",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下上",
    "description_zh": "橙框；只由新平台供数。"
  },
  {
    "id": "app_2",
    "label_en": "Application #2",
    "label_zh": "应用 #2",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下中",
    "description_zh": "橙框；与新平台双向交换。"
  },
  {
    "id": "app_3",
    "label_en": "Application #3",
    "label_zh": "应用 #3",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下",
    "description_zh": "橙框；与新平台双向交换。"
  },
  {
    "id": "db_txn_1",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "事务型应用 #1 左侧"
  },
  {
    "id": "db_txn_2",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "事务型应用 #2 左侧"
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
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
    "type": "data",
    "parent": null,
    "level": 2,
    "position": "Application #1 右侧"
  },
  {
    "id": "db_dm_3",
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
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
    "description_zh": "橙色虚线；图 3-3 中事务型应用 #1 不再连数仓。"
  },
  {
    "from": "txn_app_2",
    "to": "edw",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "灰色实线，箭头指向数仓；图例把实线定义为出站流，但此处方向是入站，原图未在线旁标注，线型与图 3-1/3-2 的虚线不一致。"
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
    "to": "edw",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "灰色实线，箭头指向数仓；线型与图例的入站流（虚线）不一致，原图未标注。"
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
    "from": "edw",
    "to": "ng_platform",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线，向下。"
  },
  {
    "from": "ng_platform",
    "to": "edw",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线，向上；新平台向数仓提供新数据。"
  },
  {
    "from": "edw",
    "to": "data_mart_1",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "灰色实线。"
  },
  {
    "from": "edw",
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
    "from": "edw",
    "to": "app_1",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线，从数仓右下方进入应用 #1。"
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
    "description_zh": "橙色实线；应用 #1 因此双供数。"
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
    "symbol": "灰色/橙色虚线 + 箭头",
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
    "meaning_zh": "RDBMS 或 RDBMS/NoSQL 数据存储，紧贴宿主",
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
  "description_zh": "左侧自上而下：三个事务型应用（蓝）、Connected Devices/Open Data/Log（橙）。中央：上为企业数据仓库（蓝），下为新一代平台（橙），两者以一对上下相反的橙色实线箭头相连。右侧自上而下：Data Mart #1、Data Mart #2（蓝）、Application #1（橙）、Data Mart #3（橙）、Application #2（橙）、Application #3（橙），各带圆柱。大虚线框包住数仓、新平台与右侧六个消费方。"
}
```

## 相关图

```json
[
  {
    "target": "G238/fig3-4",
    "relation": "precedes",
    "note_zh": "步骤 4 把新平台变成唯一历史数据存储，数仓被并入新平台内部。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "事务型应用 #2 与内嵌 BI 应用指向数仓的箭头是灰色实线，而图 3-1/3-2 中同样的入站流是虚线；图例把实线定义为出站流，二者矛盾。本分析按箭头指向记录为“流向数仓”，未强行改型。",
    "图 3-3 中事务型应用 #1 不再连数仓，原图与正文均未解释原因；不能确定是刻意表示已切换还是绘制省略。",
    "英文 p22 的“Transaction Application #1 双供数”与图中 Application #1 双供数不一致，本分析以图为准并记为原文笔误。",
    "箭头颜色（灰/橙）在图例中没有单独说明，按现状/目标流解释。"
  ],
  "analyzed_from": [
    "英文 PDF 第 22 页图 3-3 截图与 3×3 放大分块",
    "英文 PDF 第 22–24 页步骤 3 正文与表 3-4",
    "中文稿 G238e_信息架构_商业智能与分析.md 第 284–325 行",
    "figs/zh/g238e_fig3-3_zh.png、figs/g238e_fig3-3_en.png（相似度 0.988）"
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
