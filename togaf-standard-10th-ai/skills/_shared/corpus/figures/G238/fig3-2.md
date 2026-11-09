# G238/fig3-2 · 步骤 2——引入新一代平台

> 当前图示解析：[Markdown](../../architecture/diagrams/G238/fig3-2.md) · [JSON](../../architecture/diagrams/G238/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G238e.pdf`；SHA-256：`87e00e009377a887627417ceffc28b1f480bfaf57c9c84ee6f8757cc5c1c9444`。

## 原图 · PDF 第 20 页

![英文原图](../assets/G238/fig3-2-p0020.png)

PDF 坐标：`[48.2, 90.1, 563.8, 448.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
on
Business Intelligence & Analytics Data Platforms
—
Data Mart #1
Enterprise
Data Mart #2
Data
Warehouse
Transactional
Application
Application #4
Including
Embedded
BI & Analytic
Capabilities
Data Mart #3 | Rosms
Connected
Devices, Open
New Generation
Application #2, RDBMS
Data, Log,
BI & Analytics
Data Platforms
—>
Inbound Flow
Application #3, Rosms
Outbound Flow
or NoSQL.
As-Is Architecture
To-Be Architecture
```

## 概要（历史解释；局部修正见上）

过渡步骤 2：保留数仓，新增新一代平台承接新数据源，并向新集市/应用供数。

## 目的（历史解释；局部修正见上）

展示从现状走向目标的第一步：在不拆除企业数据仓库的前提下引入新一代平台，用它处理数仓无法覆盖的新数据源（日志、联网设备等），同时让部分新集市/应用先跑起来，暴露“历史数据双份存储、新平台不存原始数据、血缘困难”等过渡期缺口（表 3-3）。

## 阅读顺序（历史解释；局部修正见上）

先看左右两侧的状态：左侧三个事务型应用与中央企业数据仓库仍是蓝框（现状），下方新增的 New Generation BI & Analytics Data Platforms 是橙框（目标）。灰色虚线箭头从三个事务型应用进入数仓；橙色实线箭头从数仓向下进入新平台（清洗数据），再从新平台指向右侧 Data Mart #3、Application #2、Application #3。左下的 Connected Devices, Open Data, Log 通过橙色虚线入站流进入新平台。注意 Data Mart #3 同时收到来自数仓和新平台的两条橙色实线箭头。

## 关键含义（历史解释；局部修正见上）

- 企业数据仓库仍是现状核心（蓝框），新一代平台是新增目标元素（橙框）；两者并存，尚未替换。
- 数仓→新平台是一条橙色实线出站流，表示数仓把清洗后的数据提供给新平台——这是新平台原本拿不到的数据（正文 p20）。
- 新平台通过橙色虚线入站流接收 Connected Devices、Open Data、Log 等新数据源，并接收 Application #3 回写的入站流（应用产生的新数据经摄取进入平台以保留历史）。
- Data Mart #3 是双供数的典型：同时收到数仓（上）与新平台（下）两条橙色实线箭头，对应正文“部分需快速交付的集市同时由数仓与新平台供数”。
- Data Mart #1、Data Mart #2、Application #1 仍只由数仓供数（灰色实线），尚未切换。
- 新平台向 Data Mart #3、Application #2、Application #3 供数；后两者的存储标为 RDBMS 或 NoSQL，说明新用例不一定落在关系型库。
- 过渡期代价写在表 3-3：历史数据双份存储、新平台不保存来自数仓的原始数据、原始数据缺失导致数据血缘困难。

## 层级（历史解释；局部修正见上）

两层：平台范围容器（大虚线框）包含企业数据仓库、新一代平台、Data Mart #1/#2/#3、Application #1/#2/#3；三个事务型应用与 Connected Devices 在容器之外。每个应用/集市旁的圆柱是其本地存储，不是独立层级。两个平台（数仓与新平台）是并列关系，不是上下级。

## 线条含义（历史解释；局部修正见上）

灰色虚线箭头=现状入站流；橙色虚线箭头=目标入站流（新数据源、应用回写）；灰色实线箭头=现状出站流；橙色实线箭头=目标出站流（数仓→新平台、新平台→新集市/应用、数仓→新集市）。箭头指向数据接收方。图例只说明实线/虚线与蓝/橙框架，箭头颜色随所连接元素的现状/目标状态而变化，未单独列图例。

## 易误读点（历史解释；局部修正见上）

- 不要把 Data Mart #3 的两条入站箭头读成重复或错误：它刻意表示同时由企业数仓与新平台供数。
- 不要把 Application #3 → 新平台的虚线箭头读成“平台依赖应用”；它是入站流，表示应用产生的新数据被摄取回平台保留历史。
- 不要因为新平台出现就认为数仓已被替换：本步骤中数仓仍是蓝框现状元素，且继续向 DM#1/#2/App#1 供数。
- 不要把橙色理解为“可选/未来才用”：橙色是目标架构元素，在本过渡步骤中已经存在并承担新数据源用例。
- 不要忽视 Application #2/#3 的存储标注“RDBMS or NoSQL”：它们与原 RDBMS 集市不是同一种存储形态。
- 中文稿引用的中文化 PNG 把第三个事务型应用框画坏、把“应用 #2”文字变成白色，容易让人误判元素缺失。

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
    "description_zh": "蓝框=现状；自带 RDBMS。"
  },
  {
    "id": "txn_app_2",
    "label_en": "Transactional Application #2",
    "label_zh": "事务型应用 #2",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左中",
    "description_zh": "蓝框=现状；自带 RDBMS。"
  },
  {
    "id": "txn_app_bi",
    "label_en": "Transactional Application Including Embedded BI & Analytic Capabilities",
    "label_zh": "含内嵌 BI 与分析能力的事务型应用",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "蓝框=现状；RDBMS+Other 两个存储。"
  },
  {
    "id": "connected_devices",
    "label_en": "Connected Devices, Open Data, Log, ...",
    "label_zh": "互联设备、开放数据、日志等",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左下，Connected 区",
    "description_zh": "橙框=目标；新数据源，原图中没有对应实体框。"
  },
  {
    "id": "edw",
    "label_en": "Enterprise Data Warehouse",
    "label_zh": "企业数据仓库",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "中央上",
    "description_zh": "蓝框灰底；现状唯一的历史数据仓库。"
  },
  {
    "id": "ng_platform",
    "label_en": "New Generation BI & Analytics Data Platforms",
    "label_zh": "新一代 BI 与分析数据平台",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "中央下",
    "description_zh": "橙框灰底；目标平台，处理新数据源与新用例。"
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
    "description_zh": "蓝框；仍只由数仓供数。"
  },
  {
    "id": "data_mart_3",
    "label_en": "Data Mart #3",
    "label_zh": "数据集市 #3",
    "type": "data",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下上",
    "description_zh": "橙框；同时由数仓与新平台供数。"
  },
  {
    "id": "app_2",
    "label_en": "Application #2",
    "label_zh": "应用 #2",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下中",
    "description_zh": "橙框；由新平台供数，存储为 RDBMS。"
  },
  {
    "id": "app_3",
    "label_en": "Application #3",
    "label_zh": "应用 #3",
    "type": "application",
    "parent": "platform_scope",
    "level": 1,
    "position": "右下",
    "description_zh": "橙框；由新平台供数，并把新产生的数据回写给新平台。"
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
    "label_en": "RDBMS",
    "label_zh": "关系型数据库（RDBMS）",
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
    "to": "edw",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "灰色虚线。"
  },
  {
    "from": "txn_app_2",
    "to": "edw",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "灰色虚线。"
  },
  {
    "from": "txn_app_bi",
    "to": "edw",
    "type": "flow",
    "label_en": "Inbound Flow",
    "label_zh": "入站流",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "灰色虚线。"
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
    "description_zh": "橙色虚线；新数据源进入新平台。"
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
    "description_zh": "灰色实线。"
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
    "description_zh": "橙色实线，垂直向下；数仓向新平台提供清洗数据。"
  },
  {
    "from": "edw",
    "to": "data_mart_3",
    "type": "flow",
    "label_en": "Outbound Flow",
    "label_zh": "出站流",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "橙色实线，从数仓右下方进入 Data Mart #3 的上方箭头。"
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
    "description_zh": "橙色实线；Data Mart #3 因此双供数。"
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
    "description_zh": "橙色虚线，箭头指向新平台；应用产生的新数据经摄取回写平台。"
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
    "meaning_zh": "RDBMS（或 RDBMS/NoSQL）数据存储，紧贴宿主",
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
  "description_zh": "左侧自上而下：三个事务型应用（蓝，各带 RDBMS，第三个另带 Other）、Connected Devices/Open Data/Log（橙框）。中央：上方企业数据仓库（蓝框灰底）、下方新一代平台（橙框灰底），两者以橙色实线箭头相连。右侧自上而下：Data Mart #1、Data Mart #2、Application #1（蓝框），Data Mart #3、Application #2、Application #3（橙框），各带圆柱。大虚线框包住数仓、新平台与右侧六个消费方。"
}
```

## 相关图

```json
[
  {
    "target": "G238/fig3-3",
    "relation": "precedes",
    "note_zh": "步骤 3 让新平台成长、取代暂存区/ODS，并有更多集市/应用切换供数。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "箭头颜色（灰/橙）在原图图例中没有单独说明，本分析按“现状流/目标流”解释；图例只规定实线=出站、虚线=入站。",
    "Connected Devices 框内的“...”在原图是省略号，未列出全部数据源类型。",
    "中文稿中文化 PNG 的第三个事务型应用框绘制损坏，本分析以英文原图为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 20 页图 3-2 截图与 3×3 放大分块",
    "英文 PDF 第 20–21 页步骤 2 正文与表 3-3",
    "中文稿 G238e_信息架构_商业智能与分析.md 第 240–280 行",
    "figs/zh/g238e_fig3-2_zh.png、figs/g238e_fig3-2_en.png（相似度 0.986）"
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
