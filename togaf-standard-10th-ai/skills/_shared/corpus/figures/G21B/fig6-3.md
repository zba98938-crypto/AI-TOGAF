# G21B/fig6-3 · 整合式风格模式

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig6-3.md) · [JSON](../../architecture/diagrams/G21B/fig6-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 51 页

![英文原图](../assets/G21B/fig6-3-p0051.png)

PDF 坐标：`[61.1, 36.0, 550.9, 313.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
irect Point of Truth
Point of Truth Service
HH
Pe
of Truth
H
Batch Acquisition
Acqui
n Ul
HH
(no local storage,
Ht
Ht
‘Synchronization Service
(local storage, batch)
HH
near-real time)
(local storage,
se
iH
HH
Ht
H
near-real time)
HH
HH
Ht
HH
Point of
HH
H
Pointor @
Pointor @
HH
Acquisition App
HH
iH
cquisition App
|
[Acquisition App
is
iH
HH
iH
iH
iH
iH
Consolidation
C-MDM System
(Point of Tru
7
Hf
ut
Be
if
Hy
Hf
HH
Point of
HH
Point of
Point of
HH
HH
Hy
Hi
HH
HH
Consumption App
Consumption App
Consumption App
Bo
HH
Point of Truth “On
BB
:
:
iH
HH
Point of Truth “Search
H
O8
HH
Ht
Update Event”
| Direct Point of Truth |!
and Read” Service
H
H
Consumption
Access UI
iH
iH
(no local storage,
Hh
(local storage,
Batch Consumption
(search and read)
near-real time)
H
H
near-real time)
(local storage, batch)
Legend
@ sere On eaves \  customerdatasorage
Qeustomer pata pistroutes ep customer Data Flow
```

## 概要（历史解释；局部修正见上）

用红框标出整合式（Consolidation）只使用批量获取与批量消费两种模式。

## 目的（历史解释；局部修正见上）

把“整合式”这一集成风格落到具体交换模式：它只用批量获取（Batch Acquisition）与批量消费（Batch Consumption），因此能支持分析型客户数据整合，但不能支持与客户的运营交互。左侧小图同时提醒整合式的数据方向是“多源→MDM”。

## 阅读顺序（历史解释；局部修正见上）

先看左侧小图 Consolidation：三个源系统都指向 MDM，表示数据单向汇聚。再看右侧矩阵：红框只围住第 4 列，上格是 Batch Acquisition（采集端批量），下格是 Batch Consumption（分发端批量）；其余 6 种模式不在红框内，表示整合式不用它们。

## 关键含义（历史解释；局部修正见上）

- 整合式使用 Batch Acquisition + Batch Consumption 两种模式，均为“本地存储、批处理”。
- 批量模式适合分析型用例（细分、市场份额、C360 等），不适合与客户的实时/运营交互。
- 左侧小图显示整合式有 3 个源系统向 MDM 汇聚，MDM 不反向写回源系统。
- 红框是“本风格选用的模式”标注，不是警告或错误标记。
- 与图 6-2 相比，本图只增加了红框与左侧风格小图，矩阵内容完全相同。

## 层级（历史解释；局部修正见上）

两层：上方矩阵的采集/分发两大类与 8 个模式；左侧小图是风格级示意（3 源系统 + MDM），不参与矩阵层级。

## 线条含义（历史解释；局部修正见上）

矩阵内箭头仍表示数据流（采集向上、分发向下）；红框表示“选用”，没有方向含义；左侧小图的箭头全部由源系统指向 MDM，表示单向汇聚。

## 易误读点（历史解释；局部修正见上）

- 红框不是“高风险”或“不推荐”，只是标出整合式选用的两种模式。
- 整合式并非“没有分发”：它用批量消费把整合结果发给分析用户，只是不写回运营系统。
- 不要因为红框只在第 4 列就认为其他模式不存在；它们仍可选，只是不属于整合式。
- 左侧小图与图 6-1 的整合式相同，但本图多了交换模式矩阵，二者应结合看。

## 元素

```json
[
  {
    "id": "style_mini",
    "label_en": "Consolidation",
    "label_zh": "整合式小图",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左侧"
  },
  {
    "id": "mini_src_purple",
    "label_en": null,
    "label_zh": "源系统（紫色圆柱）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "mini_src_orange",
    "label_en": null,
    "label_zh": "源系统（橙色圆柱）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
  },
  {
    "id": "mini_src_grey",
    "label_en": null,
    "label_zh": "源系统（灰色圆柱）",
    "type": "application",
    "parent": "style_mini",
    "level": 2
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
    "id": "g_acq_patterns",
    "label_en": "Customer Data Acquisition Patterns",
    "label_zh": "客户数据采集模式",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "矩阵上半"
  },
  {
    "id": "g_dist_patterns",
    "label_en": "Customer Data Distribution Patterns",
    "label_zh": "客户数据分发模式",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "矩阵下半"
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
    "order": 1
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
    "order": 3
  },
  {
    "id": "a4",
    "label_en": "Batch Acquisition (local storage, batch)",
    "label_zh": "批量获取（本地存储，批处理）",
    "type": "service",
    "parent": "g_acq_patterns",
    "level": 2,
    "order": 4,
    "description_zh": "本图被红框圈住。"
  },
  {
    "id": "d1",
    "label_en": "Direct Point of Truth Access UI (search and read)",
    "label_zh": "直接真相点访问界面（搜索与读取）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 1
  },
  {
    "id": "d2",
    "label_en": "Point of Truth \"Search and Read\" Service (no local storage, near-real time)",
    "label_zh": "真相点“搜索与读取”服务（无本地存储，近实时）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 2
  },
  {
    "id": "d3",
    "label_en": "Point of Truth \"On Update Event\" Consumption (local storage, near-real time)",
    "label_zh": "真相点“更新事件”消费（本地存储，近实时）",
    "type": "service",
    "parent": "g_dist_patterns",
    "level": 2,
    "order": 3
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
    "from": "mini_src_purple",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：源系统→MDM。"
  },
  {
    "id": "mini2",
    "from": "mini_src_orange",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：源系统→MDM。"
  },
  {
    "id": "mini3",
    "from": "mini_src_grey",
    "to": "mini_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "左侧小图：源系统→MDM。"
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
    "description_zh": "采集第 3 列（Synchronization Service）。"
  },
  {
    "id": "r3",
    "from": "poa_app",
    "to": "c_mdm",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "采集第 4 列（Batch Acquisition），位于红框内。"
  },
  {
    "id": "r4",
    "from": "c_mdm",
    "to": "poc_app",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分发第 2 列（Search and Read Service）。"
  },
  {
    "id": "r5",
    "from": "c_mdm",
    "to": "poc_app",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分发第 3 列（On Update Event Consumption）。"
  },
  {
    "id": "r6",
    "from": "c_mdm",
    "to": "poc_app",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "分发第 4 列（Batch Consumption），位于红框内。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_selected_patterns",
    "title_zh": "整合式选用的模式（红框范围）",
    "columns": [
      "方向",
      "模式",
      "本地存储",
      "实时性"
    ],
    "rows": [
      [
        "采集 Acquisition",
        "Batch Acquisition (local storage, batch)",
        "本地存储",
        "批量"
      ],
      [
        "分发 Distribution",
        "Batch Consumption (local storage, batch)",
        "本地存储",
        "批量"
      ]
    ],
    "cell_legend": [
      "红框=本风格选用"
    ],
    "notes_zh": "红框在像素上覆盖第 4 列的上下两格（x 1197–1507，y 15–731）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "红色粗框",
    "meaning_zh": "该集成风格选用的交换模式（本图为第 4 列批量获取 + 批量消费）",
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
  "description_zh": "左侧一个小的整合式示意图（3 源系统→MDM）；右侧为与图 6-2 相同的 4×2 矩阵，第 4 列被红色粗框圈住；中央为 C-MDM 带；底部为图例。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig6-2",
    "relation": "variant_of",
    "note_zh": "与图 6-2 使用同一 4×2 模式矩阵，只增加红色选用框与左侧整合式小图。"
  },
  {
    "target": "G21B/fig6-1",
    "relation": "instance_of",
    "note_zh": "本图是图 6-1 中 Consolidation 集成风格在交换模式层面的具体化。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "左侧小图的源系统圆柱无标签，颜色仅作区分。",
    "第 1 列 Direct UI 仍无箭头，与图 6-2 一致。"
  ],
  "analyzed_from": [
    "英文 PDF 第 51 页原图截图",
    "英文 PDF 第 50–51 页正文",
    "中文稿第 775 行（整合式说明）；图 6-3 本身未被中文稿引用"
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
