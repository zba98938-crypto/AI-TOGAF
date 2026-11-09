# G21D/fig1-1 · 政府参考模型的结构

> 当前图示解析：[Markdown](../../architecture/diagrams/G21D/fig1-1.md) · [JSON](../../architecture/diagrams/G21D/fig1-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21De.pdf`；SHA-256：`220ead5fef846c52417b9b7a915ff4a64f327680b384c369840926b85958786a`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G21D/fig1-1-p0023.png)

PDF 坐标：`[215.8, 384.5, 396.2, 566.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
© The Open Group
```

## 概要（历史解释；局部修正见上）

GRM 的三层结构：L1 部门由 L2 功能组成，L2 功能由 L3 服务组成。

## 目的（历史解释；局部修正见上）

第 1.3 节用这张图给出 GRM 各要素的结构视图，说明后续章节逐一展开的三个层级及其组成关系；第 2–12 章的部门图（图 2-1 至图 12-1）和附录 A 都是这一结构在 11 个部门上的实例。

## 阅读顺序（历史解释；局部修正见上）

自上而下读三个灰色框：L1 部门、L2 功能、L3 服务。相邻两框之间的竖线表示组合关系，实心菱形紧贴上方的框，表示上方是整体、下方是部分，即“部门由功能组成”“功能由服务组成”。线上没有箭头，也没有标注数量（多重性）。图中不列出具体的部门、功能或服务名称。

## 关键含义（历史解释；局部修正见上）

- GRM 只有三个层级：部门（Sectors，政府的业务领域）、功能（Functions，在聚合层面界定政府做什么）、服务（Services，在组件层面进一步界定政府做什么）；定义见图下方的关键术语说明。
- 两条组合关系构成严格的树：每项服务只属于一个功能，每个功能只属于一个部门。在各部门图中，这种关系改用框的嵌套表示。
- 按 11 张部门图统计（本图未标出）：共 11 个部门、36 个功能、194 项服务；每个部门 2–5 个功能，每个功能 2–13 项服务（见派生表 t_sector_counts）。
- 关键术语中的“变革驱动因素（Drivers for Change）”没有画在图中：它不是第 4 层，而是各章“变革的关键驱动因素”一节按部门讨论的元因素（如人口变化、技术创新）。
- 原文说明，三个层级的推荐命名与说明用于进一步给出公共部门组织中可能存在的组织单元的细节与语境；GRM 意在用于 TOGAF ADM 的阶段 B（业务架构）。

## 层级（历史解释；局部修正见上）

三个层级类型自上而下：L1 部门 → L2 功能 → L3 服务，每一层由下一层组成。这是类型之间的组成关系，不是具体实例；具体实例见图 2-1 至图 12-1。

## 线条含义（历史解释；局部修正见上）

两条竖向细实线，上端各有一个实心菱形，贴着上方的框。按 UML 记法（背景知识），实心菱形表示组合关系，菱形所在一端是整体；关系清单中 from 为整体（上层）、to 为部分（下层），arrow 记为 forward 只表示这一读向，线上并没有箭头。图中没有多重性或文字标签。

## 易误读点（历史解释；局部修正见上）

- 菱形不是箭头，不表示数据流、指挥关系或时间顺序，只标出组合关系的整体一端。
- 三个框是层级类型，不是三个具体的部门、功能或服务。
- 图中没有“变革驱动因素”，也没有“说明”层；分类表中的“说明”列只是对每个功能与服务的文字解释。
- 中文稿引用的 figs/g21d_fig1-1.svg 画的是 11 个部门的名称网格，不是本图；其底部所说的“功能—服务—说明三层”也与本图的“部门—功能—服务”三层不一致。

## 元素

```json
[
  {
    "id": "l1_sector",
    "label_en": "L1 – Sector",
    "label_zh": "第 1 层：部门",
    "type": "concept",
    "notation_type": "GRM 层级（元素类型）",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "上",
    "description_zh": "政府的业务领域；共 11 个（表 1-1、第 2–12 章）。"
  },
  {
    "id": "l2_function",
    "label_en": "L2 – Function",
    "label_zh": "第 2 层：功能",
    "type": "concept",
    "notation_type": "GRM 层级（元素类型）",
    "parent": null,
    "level": 2,
    "order": 2,
    "position": "中",
    "description_zh": "在聚合层面界定政府做什么；11 个部门图共 36 个功能。"
  },
  {
    "id": "l3_service",
    "label_en": "L3 – Service",
    "label_zh": "第 3 层：服务",
    "type": "concept",
    "notation_type": "GRM 层级（元素类型）",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "下",
    "description_zh": "在组件层面进一步界定政府做什么；11 个部门图共 194 项服务（表 8-1 另列 2 项）。"
  }
]
```

## 关系

```json
[
  {
    "from": "l1_sector",
    "to": "l2_function",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "竖线上端的实心菱形贴着 L1 框：部门由功能组成；线上无箭头，未标多重性"
  },
  {
    "from": "l2_function",
    "to": "l3_service",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "竖线上端的实心菱形贴着 L2 框：功能由服务组成；线上无箭头，未标多重性"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_sector_counts",
    "title_zh": "11 个部门的 L2/L3 数量（派生：据图 2-1 至图 12-1 统计，不在本图中）",
    "columns": [
      "L1 部门",
      "部门图",
      "L2 功能数",
      "L3 服务数"
    ],
    "rows": [
      [
        "国际事务与贸易 International Affairs and Trade",
        "图 2-1",
        "3",
        "7"
      ],
      [
        "国防与安全 Defense and Security",
        "图 3-1",
        "3",
        "10"
      ],
      [
        "一般政府与地方服务 General Government and Local Services",
        "图 4-1",
        "3",
        "26"
      ],
      [
        "青少年与教育 Young People and Education",
        "图 5-1",
        "3",
        "14"
      ],
      [
        "健康与社区福祉 Health and Community Wellbeing",
        "图 6-1",
        "3",
        "22"
      ],
      [
        "司法、治安与内政 Judiciary, Justice, and Home Affairs",
        "图 7-1",
        "2",
        "13"
      ],
      [
        "财政 Financial",
        "图 8-1",
        "5",
        "17（表 8-1 为 19）"
      ],
      [
        "增长、住房与环境 Growth, Housing, and Environment",
        "图 9-1",
        "4",
        "27"
      ],
      [
        "政策、绩效、人口与创新 Policy, Performance, Population, and Innovation",
        "图 10-1",
        "3",
        "15"
      ],
      [
        "共享服务 Shared Services",
        "图 11-1",
        "5",
        "33"
      ],
      [
        "交通与运营 Transport and Operations",
        "图 12-1",
        "2",
        "10"
      ],
      [
        "合计",
        "—",
        "36",
        "194"
      ]
    ],
    "notes_zh": "本表不是对图 1-1 的转录：图 1-1 只画三个层级，不列部门。数字按各部门图中的框数统计，用于把三层结构与 11 个部门对应起来；部门清单与定义见表 1-1。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色矩形",
    "meaning_zh": "GRM 的一个层级（元素类型）",
    "explicit": false
  },
  {
    "symbol": "竖线 + 上端实心菱形",
    "meaning_zh": "组合关系（UML 记法，背景知识）：菱形一端（上方）是整体，另一端（下方）是部分",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "三个等宽灰色矩形自上而下排列（L1 – Sector、L2 – Function、L3 – Service），相邻两框之间一条竖线，竖线上端带实心菱形；版权署名在右下角。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "实心菱形按 UML 组合关系解读属于背景知识，原文没有解释这一记法。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页原图截图",
    "英文 PDF 第 21–24 页正文（1.2–1.4 节、表 1-1）",
    "中文稿 G21De_政府参考模型.md 第 142–205 行",
    "figs/g21d_fig1-1.svg 源码",
    "图 2-1 至图 12-1 的分析结果（用于统计数量）"
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
