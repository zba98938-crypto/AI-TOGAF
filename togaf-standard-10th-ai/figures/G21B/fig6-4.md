# G21B/fig6-4 · 协作式风格模式

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig6-4.md) · [JSON](../../architecture/diagrams/G21B/fig6-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 51 页

![英文原图](../assets/G21B/fig6-4-p0051.png)

PDF 坐标：`[61.1, 403.8, 550.9, 681.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
irect Point of Truth
Point of Truth Service
Point of Truth
Batch Acquisition
:
ition UI
:
Acq
(re local storage,
‘Synchronization Service
(local storage, batch)
£5
near-real time)
(local storage,
ce
near-real time)
Bie
Point of
Pointor @
Pointof §@
S=
ES
Acquisition App
\equisition App
‘Acquisition App
ao
33
og
Cooperation
Ss.
C-MDM System (Point of Truth)
Ss “se
£5
ae
of
Point of
Point of
Pointof
‘Consumption App
Consumption App
Consumption App
ES
et
Point of Truth “On
OB
Point of Truth “Search
og
Update Event”
Direct Point of Truth
and Read” Service
Consumption
Access UI
(no local storage,
(local storage,
Batch Consumption
(search and read)
near-real time)
near-real time)
(local storage, batch)
:
:
Legend
@evsereronsreruies GB cusomerdstaserage
@cusiomeroataDisebsted =p Customer Daa Flow
```

## 概要（历史解释；局部修正见上）

用红框标出协作式相关的交换模式：直接采集 UI、真相点同步服务、直接访问 UI、搜索读取服务，以及批量列。

## 目的（历史解释；局部修正见上）

把“协作式”落到交换模式：正文说协作式使用主源与副本源之间的数据同步管理，运营系统与 C-MDM 真相保持对齐但可能有延迟；左侧小图用双向箭头强调“系统保留自己的数据、同时与 MDM 同步”。

## 阅读顺序（历史解释；局部修正见上）

先看左侧小图 Cooperation：MDM 居中，4 个系统与它两两双向箭头。再看右侧矩阵的红框：上排第 1 列、第 3 列、第 4 列被框住；下排第 1–2 列被框住，第 4 列整列也被框住。阅读时应以正文“协作式=同步模式”为准，并注意红框的实际覆盖范围与原图文字并不完全一致（见 misreadings）。

## 关键含义（历史解释；局部修正见上）

- 协作式的核心是同步：Point of Truth Synchronization Service（采集）与 Point of Truth “On Update Event” Consumption（分发）成对使用，运营系统与 C-MDM 保持近实时对齐。
- 左侧小图画出 MDM 与 4 个系统全部双向连接，表示系统既向 MDM 推送更新，也接收 MDM 的真相版本。
- 直接采集 UI 与直接访问 UI 仍可用：用户可以直接在 C-MDM 界面录入或查询。
- 正文强调协作式比整合式复杂，但能在孤岛式信息系统中对客户数据质量与治理实现高水平控制；需要事务型应用支持 UI、工作流与合并/删除。
- 红框的实际覆盖范围（含批量列与搜索读取列）与正文“协作式使用同步”不完全一致，疑为原图标注偏差；判断某模式是否属于协作式应以正文为准。

## 层级（历史解释；局部修正见上）

两层：矩阵的采集/分发两大类 + 8 个模式；左侧小图是风格级示意，不参与矩阵层级。

## 线条含义（历史解释；局部修正见上）

矩阵内箭头表示数据流（采集向上、分发向下）；红框表示“本风格相关/选用”，无方向含义；左侧小图的双向箭头表示系统与 MDM 双向同步。

## 易误读点（历史解释；局部修正见上）

- 不要严格按红框理解协作式：红框还框住了 Batch Acquisition/Batch Consumption 与 Search and Read，而正文只说协作式使用同步管理；这更可能是原图标注偏移。
- 协作式的“系统保留自己的数据”不等于“双主库”：真相版本仍由 C-MDM 定义并同步回系统。
- 双向箭头不是“两个方向都实时”：正文允许交换频率/架构上存在一定时延。
- 红框不是风险标记。

## 元素

```json
[
  {
    "id": "style_mini",
    "label_en": "Cooperation",
    "label_zh": "协作式小图",
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
    "order": 2
  },
  {
    "id": "a3",
    "label_en": "Point of Truth Synchronization Service (local storage, near-real time)",
    "label_zh": "真相点同步服务（本地存储，近实时）",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 3,
    "description_zh": "本图被红框圈住；正文指定协作式使用的核心模式。"
  },
  {
    "id": "a4",
    "label_en": "Batch Acquisition (local storage, batch)",
    "label_zh": "批量获取（本地存储，批处理）",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 4,
    "description_zh": "本图第 4 列整列被红框圈住（与正文不一致）。"
  },
  {
    "id": "d1",
    "label_en": "Direct Point of Truth Access UI (search and read)",
    "label_zh": "直接真相点访问界面（搜索与读取）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 1,
    "description_zh": "本图与 d2 一起被红框圈住。"
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
    "description_zh": "正文所述协作式的分发核心模式，但本图未被红框圈住。"
  },
  {
    "id": "d4",
    "label_en": "Batch Consumption (local storage, batch)",
    "label_zh": "批量消费（本地存储，批处理）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 4,
    "description_zh": "本图第 4 列整列被红框圈住。"
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
    "from": "mini_sys_purple",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "左侧小图：双向同步。"
  },
  {
    "id": "mini2",
    "from": "mini_sys_grey",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "左侧小图：双向同步。"
  },
  {
    "id": "mini3",
    "from": "mini_sys_orange",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "左侧小图：双向同步。"
  },
  {
    "id": "mini4",
    "from": "mini_sys_green",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "左侧小图：双向同步。"
  },
  {
    "id": "r1",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 2 列（Point of Truth Service）。"
  },
  {
    "id": "r2",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 3 列（Synchronization Service），红框内。"
  },
  {
    "id": "r3",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 4 列（Batch Acquisition），红框内。"
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
    "description_zh": "分发第 3 列（On Update Event Consumption），红框外。"
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
    "id": "t_red_frames",
    "title_zh": "本图红框的实际覆盖范围（按像素坐标转录）",
    "columns": [
      "红框",
      "覆盖列",
      "覆盖的模式",
      "与正文的一致性"
    ],
    "rows": [
      [
        "上排红框 1",
        "第 1 列",
        "Direct Point of Truth Acquisition UI",
        "一致（可直接在 C-MDM 界面录入）"
      ],
      [
        "上排红框 2",
        "第 3 列",
        "Point of Truth Synchronization Service",
        "一致（协作式的核心同步模式）"
      ],
      [
        "整列红框",
        "第 4 列（上下两格）",
        "Batch Acquisition + Batch Consumption",
        "不一致：正文未说协作式使用批量模式"
      ],
      [
        "下排红框",
        "第 1–2 列",
        "Direct Point of Truth Access UI + Point of Truth “Search and Read” Service",
        "部分一致：直接访问与搜索读取可用于协作式，但正文强调的是“同步”"
      ]
    ],
    "cell_legend": [
      "红框为原图像素级标注，非本分析推断"
    ],
    "notes_zh": "红框坐标：上排第 1 列 x371–632/y15–329；第 3 列 x912–1200/y15–329；第 4 列 x1197–1507/y15–731；下排第 1–2 列 x371–911/y404–731。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "红色粗框",
    "meaning_zh": "该风格相关/选用的交换模式（本图红框覆盖上排第 1、3、4 列，下排第 1–2 列与第 4 列）",
    "explicit": false
  },
  {
    "symbol": "左侧小图的双向箭头",
    "meaning_zh": "系统与 MDM 双向同步",
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
  "description_zh": "左侧协作式小图（MDM 居中、4 系统环绕、双向箭头）；右侧 4×2 矩阵，红框分别位于上排第 1 列、第 3 列、第 4 列，以及下排第 1–2 列与第 4 列；中央为 C-MDM 带；底部图例。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig6-2",
    "relation": "variant_of",
    "note_zh": "与图 6-2 使用同一 4×2 模式矩阵，只增加红色选用框与左侧协作式小图。"
  },
  {
    "target": "G21B/fig6-1",
    "relation": "instance_of",
    "note_zh": "本图是图 6-1 中 Cooperation 集成风格在交换模式层面的具体化。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "红框覆盖范围与正文“协作式使用同步管理”不一致（还框住了批量列与搜索读取列，且未框住 On Update Event Consumption），疑为原图标注偏移或错误；本分析按像素如实记录并在表中标出。",
    "左侧小图的系统圆柱无标签；双向箭头是否代表“同步”依据正文与图 6-1。"
  ],
  "analyzed_from": [
    "英文 PDF 第 51 页原图截图及 2×2 放大分块",
    "英文 PDF 第 51 页正文",
    "中文稿第 755、776 行（协作式说明）；图 6-4 本身未被中文稿引用",
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
