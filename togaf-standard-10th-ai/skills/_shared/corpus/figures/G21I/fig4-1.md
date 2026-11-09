# G21I/fig4-1 · TOGAF 架构开发方法（ADM）

> 当前图示解析：[Markdown](../../architecture/diagrams/G21I/fig4-1.md) · [JSON](../../architecture/diagrams/G21I/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Ie.pdf`；SHA-256：`279f6c06124f49a147a168591965805115b2fc976eea2664e41e491ac5d163bf`。

## 原图 · PDF 第 21 页

![英文原图](../assets/G21I/fig4-1-p0021.png)

PDF 坐标：`[151.3, 36.0, 460.7, 447.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Preliminary
A.
Architecture
Vision
H.
Architecture
B.
Business
Change
Architecture
Management
G.
Cc.
Requirements
Information
Implementation
Management
Systems
Governance
Architectures
F.
D.
Migration
Technology
Planning
Architecture
=
Opportunities
and
Solutions
The Open Group
```

## 概要（历史解释；局部修正见上）

标准 TOGAF ADM 图：预备阶段接入 A–H 循环，需求管理居中并连到每个阶段。

## 目的（历史解释；局部修正见上）

本指南按 ADM 阶段组织：第 5–13 章依次对应预备阶段到阶段 H，说明采用 MSA 时架构师在各阶段要考虑什么、对阶段输出有何影响。本图让读者先认出熟悉的 ADM 结构，再进入逐阶段的 MSA 说明。

## 阅读顺序（历史解释；局部修正见上）

从顶部的预备阶段开始，它只连到下方的阶段 A。A–H 八个阶段围成一圈，按 TOGAF 惯例从 A 起顺时针读到 H，再回到 A。中心的需求管理用 8 条辐条与 A–H 相连。所有连线都没有箭头。

## 关键含义（历史解释；局部修正见上）

- 预备阶段在循环之外，只接入阶段 A：它为企业做好开展架构工作的准备，A–H 才是可重复的开发循环。
- A–H 首尾相连成环：H（架构变更管理）之后回到 A，开始新一轮架构开发。
- 需求管理位于中心并连到每个阶段；原文把它列为“面向 MSA 的持续过程”，不是排在某个阶段之后的一步。
- 阶段 C 是“信息系统架构”，原文注明包括数据与应用两部分；本指南第 8 章分 8.1 数据架构、8.2 应用架构展开。
- 本指南第 5–13 章与图中的预备阶段、A–H 一一对应；原文说明它只讲与 MSA 相关的内容（聚焦架构中的微服务层），假定读者已了解 TOGAF 标准。

## 层级（历史解释；局部修正见上）

没有嵌套。预备阶段、A–H 与需求管理都是 ADM 的阶段；需求管理用更大的橙色圆放在中心，表示它与所有阶段相关。

## 线条含义（历史解释；局部修正见上）

全部为无箭头的细实线：8 段弧线把相邻阶段连成环（A–B–C–D–E–F–G–H–A，方向按 TOGAF 惯例读出），8 条辐条把需求管理连到 A–H，1 条竖线把预备阶段连到 A。

## 易误读点（历史解释；局部修正见上）

- 环上没有箭头，但 ADM 的阶段有约定次序（A 到 H 顺时针）；背景知识：TOGAF 标准也允许在阶段之间迭代，图中没有画出迭代。
- 需求管理不是 H 之后的第 10 步，而是贯穿全部阶段的持续过程。
- 预备阶段不在 A–H 循环之内。
- 原图右下角的空心大字是英文 PDF 的“Evaluation Copy”水印，不是图的内容。

## 元素

```json
[
  {
    "id": "ph_prelim",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "order": 0,
    "position": "顶部"
  },
  {
    "id": "ph_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "order": 1,
    "position": "环顶"
  },
  {
    "id": "ph_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "order": 2,
    "position": "右上"
  },
  {
    "id": "ph_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "order": 3,
    "position": "右"
  },
  {
    "id": "ph_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "order": 4,
    "position": "右下"
  },
  {
    "id": "ph_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "order": 5,
    "position": "环底"
  },
  {
    "id": "ph_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "order": 6,
    "position": "左下"
  },
  {
    "id": "ph_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "order": 7,
    "position": "左"
  },
  {
    "id": "ph_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "order": 8,
    "position": "左上"
  },
  {
    "id": "ph_rm",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "phase",
    "position": "圆心",
    "description_zh": "原文称其为面向 MSA 的持续过程。"
  }
]
```

## 关系

```json
[
  {
    "from": "ph_prelim",
    "to": "ph_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "竖线；预备阶段在环外，接入 A"
  },
  {
    "from": "ph_a",
    "to": "ph_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "环上弧线；无箭头，按 ADM 惯例顺时针读"
  },
  {
    "from": "ph_b",
    "to": "ph_c",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_c",
    "to": "ph_d",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_d",
    "to": "ph_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_e",
    "to": "ph_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_f",
    "to": "ph_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_g",
    "to": "ph_h",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_h",
    "to": "ph_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "闭合成环"
  },
  {
    "from": "ph_rm",
    "to": "ph_a",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "辐条；需求管理贯穿所有阶段"
  },
  {
    "from": "ph_rm",
    "to": "ph_b",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_rm",
    "to": "ph_c",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_rm",
    "to": "ph_d",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_rm",
    "to": "ph_e",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_rm",
    "to": "ph_f",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_rm",
    "to": "ph_g",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "ph_rm",
    "to": "ph_h",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_adm_cycle",
    "kind": "cycle",
    "name_zh": "ADM 周期",
    "steps": [
      "ph_a",
      "ph_b",
      "ph_c",
      "ph_d",
      "ph_e",
      "ph_f",
      "ph_g",
      "ph_h"
    ],
    "description_zh": "环上无箭头，按 TOGAF ADM 惯例从 A 顺时针到 H 再回到 A；预备阶段在环外接入 A，需求管理在中心连到各阶段。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_chapters",
    "title_zh": "ADM 阶段与本指南章节的对应（据中文稿目录与英文正文）",
    "columns": [
      "ADM 阶段",
      "本指南章节"
    ],
    "rows": [
      [
        "预备阶段 Preliminary",
        "第 5 章（含 5.3 治理与支持策略、5.4 初始架构存储库与 MSA 参考架构）"
      ],
      [
        "阶段 A：架构愿景",
        "第 6 章"
      ],
      [
        "阶段 B：业务架构",
        "第 7 章"
      ],
      [
        "阶段 C：信息系统架构（数据与应用）",
        "第 8 章"
      ],
      [
        "阶段 D：技术架构",
        "第 9 章"
      ],
      [
        "阶段 E：机会与解决方案",
        "第 10 章"
      ],
      [
        "阶段 F：迁移规划",
        "第 11 章"
      ],
      [
        "阶段 G：实施治理",
        "第 12 章"
      ],
      [
        "阶段 H：架构变更管理",
        "第 13 章"
      ],
      [
        "需求管理 Requirements Management",
        "无单独章节（原文列为面向 MSA 的持续过程）"
      ]
    ],
    "notes_zh": "图本身不含章节信息；本表帮助把图中的阶段与后文对上。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色圆",
    "meaning_zh": "ADM 阶段",
    "explicit": false
  },
  {
    "symbol": "中心较大的橙色圆",
    "meaning_zh": "需求管理（贯穿各阶段）",
    "explicit": false
  },
  {
    "symbol": "无箭头的细实线",
    "meaning_zh": "环上为相邻阶段的连接；辐条为需求管理与各阶段的连接",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "预备阶段在最上方，竖线向下接到阶段 A；A–H 八个圆以 A 为顶点顺时针排成一圈；需求管理在圆心，比其他圆大。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 21 页原图截图（220 dpi）",
    "英文 PDF 第 20–21 页正文",
    "中文稿 G21Ie_微服务架构.md 第 173–215 行（含图内标签对照表 L196–L209）及全文章节标题",
    "figs/zh/g21ie_fig4-1_zh.png",
    "figs/g21ie_fig4-1_en.png（自动相似度 0.993）"
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
