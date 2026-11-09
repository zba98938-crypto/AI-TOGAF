# G21B/fig6-5 · 集中式风格模式

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig6-5.md) · [JSON](../../architecture/diagrams/G21B/fig6-5.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 52 页

![英文原图](../assets/G21B/fig6-5-p0052.png)

PDF 坐标：`[61.1, 160.7, 550.9, 437.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
irect Point of Truth
Point of Truth Service
Point of Truth
:
:
Batch Acquisition
Acquisition UL
(ro local storage,
‘Synchronization Service
(local storage, batch)
near-real time)
(local storage,
near-real time)
Point of
Pointor @
Pointof §@
Acquisition App
\equisition App
[Acquisition App
Centralized
e_
C-MDM System (Point of Truth)
S Ss
Point of
Point of
Point of
‘Consumption App
Consumption App
Consumption App
Point of Truth “On
3B
Point of Truth “Search
Update Event”
| Direct Point of Truth
and Read” Service
‘Consumption
:
Access UI
(no local storage,
(localstorage,
Batch Consumption
:
(search and read)
near-real time)
near-real time)
(local storage, batch)
Legend
@evsererona reer — cusomerdstasorage
@evsiomeroaiaoisrbxted mp Customer DataFow
```

## 概要（历史解释；局部修正见上）

集中式只通过 C-MDM 的界面或真相点服务创建/更新数据，分发则可用全部四种模式。

## 目的（历史解释；局部修正见上）

把“集中式”落到交换模式：所有更新与创建都经 C-MDM 的真相点系统与服务发起（采集只保留直接 UI 与 Point of Truth Service），分发覆盖全部四种模式（直接访问、搜索读取、更新事件消费、批量消费）；左侧小图用 MDM 向外的单向箭头强调“唯一主数据存储”。

## 阅读顺序（历史解释；局部修正见上）

先看左侧小图 Centralized：MDM 居中，4 个系统各有一条从 MDM 指向系统的箭头。再看右侧矩阵：上排红框覆盖第 1、2 列（Direct UI + PoT Service），下排红框横跨全部 4 列。含义是：写入口收窄到 C-MDM 服务，读取口保持全部模式。

## 关键含义（历史解释；局部修正见上）

- 集中式的采集只用两种：Direct Point of Truth Acquisition UI（直接在 C-MDM 界面操作）与 Point of Truth Service（通过服务写入）；同步服务与批量获取不再作为写入路径。
- 分发不限制：直接访问、搜索读取、更新事件消费、批量消费四种都可用（下排整行红框）。
- 左侧小图的所有箭头都由 MDM 指向系统，表示系统只从 MDM 取数，不再拥有主数据。
- 正文说明集中式与协作式功能覆盖相同，但从架构与信息系统运营角度更简单、更高效。
- 新应用必须从一开始就依赖 C-MDM；对未按此原则设计的应用改变主数据主控权，代价很高甚至不可行。

## 层级（历史解释；局部修正见上）

两层：矩阵的采集/分发两大类 + 8 个模式；左侧小图是风格级示意，不参与矩阵层级。

## 线条含义（历史解释；局部修正见上）

矩阵内箭头表示数据流（采集向上、分发向下）；红框表示“本风格选用”；左侧小图箭头由 MDM 指向各系统，表示单向分发/只读消费。

## 易误读点（历史解释；局部修正见上）

- 下排整行红框不表示“所有模式都必须用”，而是“都可以用”，按消费场景选择。
- 集中式并非没有采集：创建/更新仍通过 C-MDM 的直接 UI 或服务进行，只是不再由运营系统批量推送。
- 左侧小图的单向箭头不表示系统完全不能写：写入必须经 C-MDM 的服务/界面，而不是系统之间直连。
- 红框是“选用”标注，不是警告。

## 元素

```json
[
  {
    "id": "style_mini",
    "label_en": "Centralized",
    "label_zh": "集中式小图",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左侧"
  },
  {
    "id": "mini_mdm",
    "label_en": "MDM",
    "label_zh": "MDM",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "mini_sys_purple",
    "label_en": null,
    "label_zh": "业务系统（紫色圆柱，左上）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "mini_sys_grey",
    "label_en": null,
    "label_zh": "业务系统（灰色圆柱，右上）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "mini_sys_orange",
    "label_en": null,
    "label_zh": "业务系统（橙色圆柱，左下）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "mini_sys_green",
    "label_en": null,
    "label_zh": "业务系统（绿色圆柱，右下）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "g_acq_patterns",
    "label_en": "Customer Data Acquisition Patterns",
    "label_zh": "客户数据采集模式",
    "type": "group",
    "parent": null,
    "level": 1
  },
  {
    "id": "g_dist_patterns",
    "label_en": "Customer Data Distribution Patterns",
    "label_zh": "客户数据分发模式",
    "type": "group",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_mdm",
    "label_en": "C-MDM System (Point of Truth)",
    "label_zh": "C-MDM 系统（真相点）",
    "type": "application",
    "parent": null,
    "level": 1,
    "position": "中央横带"
  },
  {
    "id": "a1",
    "label_en": "Direct Point of Truth Acquisition UI",
    "label_zh": "直接真相点采集界面",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 1,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "a2",
    "label_en": "Point of Truth Service (no local storage, near-real time)",
    "label_zh": "真相点服务（无本地存储，近实时）",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 2,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "a3",
    "label_en": "Point of Truth Synchronization Service (local storage, near-real time)",
    "label_zh": "真相点同步服务（本地存储，近实时）",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 3,
    "description_zh": "本图未被红框圈住。"
  },
  {
    "id": "a4",
    "label_en": "Batch Acquisition (local storage, batch)",
    "label_zh": "批量获取（本地存储，批处理）",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 4,
    "description_zh": "本图未被红框圈住。"
  },
  {
    "id": "d1",
    "label_en": "Direct Point of Truth Access UI (search and read)",
    "label_zh": "直接真相点访问界面（搜索与读取）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 1,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "d2",
    "label_en": "Point of Truth \"Search and Read\" Service (no local storage, near-real time)",
    "label_zh": "真相点“搜索与读取”服务（无本地存储，近实时）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 2,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "d3",
    "label_en": "Point of Truth \"On Update Event\" Consumption (local storage, near-real time)",
    "label_zh": "真相点“更新事件”消费（本地存储，近实时）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 3,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "d4",
    "label_en": "Batch Consumption (local storage, batch)",
    "label_zh": "批量消费（本地存储，批处理）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 4,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "poa_app",
    "label_en": "Point of Acquisition App",
    "label_zh": "采集点应用",
    "type": "application",
    "parent": null,
    "position": "采集第 2–4 列"
  },
  {
    "id": "poc_app",
    "label_en": "Point of Consumption App",
    "label_zh": "消费点应用",
    "type": "application",
    "parent": null,
    "position": "分发第 2–4 列"
  }
]
```

## 关系

```json
[
  {
    "id": "mini1",
    "from": "mini_mdm",
    "to": "mini_sys_purple",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：MDM→系统单向分发。"
  },
  {
    "id": "mini2",
    "from": "mini_mdm",
    "to": "mini_sys_grey",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：MDM→系统单向分发。"
  },
  {
    "id": "mini3",
    "from": "mini_mdm",
    "to": "mini_sys_orange",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：MDM→系统单向分发。"
  },
  {
    "id": "mini4",
    "from": "mini_mdm",
    "to": "mini_sys_green",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：MDM→系统单向分发。"
  },
  {
    "id": "r1",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 2 列（Point of Truth Service），红框内。"
  },
  {
    "id": "r2",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 3 列（Synchronization Service），红框外。"
  },
  {
    "id": "r3",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 4 列（Batch Acquisition），红框外。"
  },
  {
    "id": "r4",
    "from": "c_mdm",
    "to": "poc_app",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分发第 2 列（Search and Read Service），红框内。"
  },
  {
    "id": "r5",
    "from": "c_mdm",
    "to": "poc_app",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分发第 3 列（On Update Event Consumption），红框内。"
  },
  {
    "id": "r6",
    "from": "c_mdm",
    "to": "poc_app",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分发第 4 列（Batch Consumption），红框内。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_selected_patterns",
    "title_zh": "集中式选用的模式（红框范围）",
    "columns": [
      "方向",
      "红框覆盖的列",
      "模式"
    ],
    "rows": [
      [
        "采集 Acquisition",
        "第 1–2 列",
        "Direct Point of Truth Acquisition UI；Point of Truth Service"
      ],
      [
        "分发 Distribution",
        "第 1–4 列（整行）",
        "Direct Point of Truth Access UI；Point of Truth “Search and Read” Service；Point of Truth “On Update Event” Consumption；Batch Consumption"
      ]
    ],
    "cell_legend": [
      "红框=本风格选用"
    ],
    "notes_zh": "红框坐标：上排 x371–915/y15–329；下排 x371–1507/y404–731。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "红色粗框",
    "meaning_zh": "该风格选用的交换模式（上排第 1–2 列 + 下排全部 4 列）",
    "explicit": false
  },
  {
    "symbol": "左侧小图的单向箭头",
    "meaning_zh": "MDM 向系统单向分发（系统只读消费）",
    "explicit": false
  },
  {
    "symbol": "青色球 / 橙色球 / 圆柱 / 箭头",
    "meaning_zh": "已采集数据 / 已分发数据 / 客户数据存储 / 客户数据流（同图 6-2 图例）",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "左侧集中式小图（MDM 居中、4 系统环绕、箭头由 MDM 向外）；右侧 4×2 矩阵，上排第 1–2 列被红框圈住，下排整行 4 列被红框圈住；中央为 C-MDM 带；底部图例。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig6-2",
    "relation": "variant_of",
    "note_zh": "与图 6-2 使用同一 4×2 模式矩阵，只增加红色选用框与左侧集中式小图。"
  },
  {
    "target": "G21B/fig6-1",
    "relation": "instance_of",
    "note_zh": "本图是图 6-1 中 Centralized 集成风格在交换模式层面的具体化。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "左侧小图的系统圆柱无标签，颜色仅作区分。",
    "第 1 列 Direct UI 仍无箭头（与图 6-2 一致），只能通过 C-MDM 带内的数据球识别其存在。"
  ],
  "analyzed_from": [
    "英文 PDF 第 52 页原图截图及 2×2 放大分块",
    "英文 PDF 第 51–52 页正文",
    "中文稿第 777 行（集中式说明）；图 6-5 本身未被中文稿引用",
    "红框像素检测（PIL）结果"
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
