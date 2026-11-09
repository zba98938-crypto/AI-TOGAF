# G176/fig6-1 · 需求在整个 TOGAF ADM 中的相关性

> 当前图示解析：[Markdown](../../architecture/diagrams/G176/fig6-1.md) · [JSON](../../architecture/diagrams/G176/fig6-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G176e.pdf`；SHA-256：`48c76fbfd164020fcbc0a4f2ec12ee849a2af83424a332883f9a8e0260bf4961`。

## 原图 · PDF 第 30 页

![英文原图](../assets/G176/fig6-1-p0030.png)

PDF 坐标：`[125.6, 191.7, 486.4, 438.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
“Business Scenarios are an appropriate
and useful technique to discover and
oo
document business requirements, and to
articulate an Architecture Vision that
responds to those requirements.”
~ Phase A: Architecture Vision
“Business Scenarios are a useful
technique to discover and document
business requirements, and may be used
iteratively, at different levels of detail in
the hierarchical decomposition of the
Business Architecture
f
~ Phase B: Business Architecture
“Identify/document requirements — use
Business Scenarios, or an analogous
technique.”
= Requirements Management
on
```

## 概要（历史解释；局部修正见上）

ADM 轮：需求管理居中连到 A–H 各阶段；三段引文指出业务场景在阶段 A、阶段 B 和需求管理中的用法。

## 目的（历史解释；局部修正见上）

第 6 章说明业务场景与 TOGAF ADM 的关系：业务场景在阶段 A（架构愿景）最为突出，用来定义相关业务需求并与业务管理层和其他利益相关者达成共识；也用于业务架构阶段，从业务的高层需求直接推导架构特征。正文说业务需求在 ADM 生命周期的所有阶段都会被引用，并以本图为证：需求管理位于 ADM 轮中心、与每个阶段相连，右侧三段引文标出业务场景被明确推荐的三个位置。

## 阅读顺序（历史解释；局部修正见上）

左侧是 TOGAF ADM 轮：顶部单独的“Preliminary（预备阶段）”用一条竖线连到阶段 A；阶段 A–H 八个黄色圆排成一圈，相邻阶段由弧线相连；中心的橙色大圆是“Requirements Management（需求管理）”，用 8 条辐条连到每个阶段。这些线都没有箭头，ADM 按 A→B→…→H 顺时针推进是 TOGAF 标准的约定（背景知识）。右侧三段带引号的文字各有一个绿色箭头，分别指向阶段 A、阶段 B 和需求管理，引文末尾的斜体字标明它对应的阶段。

## 关键含义（历史解释；局部修正见上）

- 需求管理位于 ADM 轮中心，并与 A–H 每个阶段相连，表达图题的意思：业务需求在 ADM 生命周期的所有阶段都会被引用。
- 阶段 A（架构愿景）的引文：业务场景是发现并记录业务需求、并阐明响应这些需求的架构愿景的合适且有用的技术。正文称业务场景在阶段 A 最为突出，用于定义业务需求并与业务管理层和其他利益相关者达成共识。
- 阶段 B（业务架构）的引文：业务场景可用于发现并记录业务需求，并可在业务架构分层分解的不同详细程度上迭代使用。正文称它用于从业务的高层需求直接推导架构特征。
- 需求管理的引文：识别和记录需求时，使用业务场景或类似技术。
- 业务场景不限于这三处：正文说任何 ADM 阶段需要推导需求时都可以使用，例如在预备阶段定义建立企业架构能力所需的需求（图中预备阶段没有引文）。
- 正文结论：由于业务需求在 ADM 各阶段都重要，业务场景技术通过确保业务需求本身完整、正确，在 ADM 中发挥重要作用。

## 层级（历史解释；局部修正见上）

没有容器嵌套。预备阶段位于循环之外的上方；阶段 A–H 构成循环；需求管理在中心，与各阶段是居中支撑关系，不是上下级。三段引文是附加注释。

## 线条含义（历史解释；局部修正见上）

灰色细线全部没有箭头：预备阶段与阶段 A 之间一条竖线；环上 8 段弧线连接相邻阶段（A–B、B–C……H–A），表示 ADM 阶段次序，方向按 TOGAF 标准为 A→B→…→H→A（背景知识，关系清单按此方向记录）；中心 8 条辐条连接需求管理与每个阶段，表示需求管理服务于所有阶段。绿色箭头是注释箭头，从引文指向它所说的阶段。

## 易误读点（历史解释；局部修正见上）

- 绿色箭头只表示引文说的是哪个阶段，不是流程或数据流。
- 图中线条没有箭头，ADM 的顺时针次序来自 TOGAF 标准，不是本图画出的。
- 只有三处有引文，不表示业务场景只能用在这三处；正文说任何需要推导需求的阶段都可以用。
- 中文稿第 6 章（L363–L369）没有放这张图，也删去了英文“see Figure 6-1”的引用，读中文稿无从得知需求管理居中和三段引文的内容。

## 元素

```json
[
  {
    "id": "preliminary",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": null,
    "position": "最上方，循环之外"
  },
  {
    "id": "ph_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": null,
    "order": 1,
    "position": "环的正上方"
  },
  {
    "id": "ph_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": null,
    "order": 2,
    "position": "右上"
  },
  {
    "id": "ph_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": null,
    "order": 3,
    "position": "右"
  },
  {
    "id": "ph_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": null,
    "order": 4,
    "position": "右下"
  },
  {
    "id": "ph_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": null,
    "order": 5,
    "position": "正下"
  },
  {
    "id": "ph_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": null,
    "order": 6,
    "position": "左下"
  },
  {
    "id": "ph_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "parent": null,
    "order": 7,
    "position": "左"
  },
  {
    "id": "ph_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": null,
    "order": 8,
    "position": "左上"
  },
  {
    "id": "req_mgmt",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "phase",
    "parent": null,
    "position": "中心，较大的橙色圆"
  },
  {
    "id": "note_a",
    "label_en": "“Business Scenarios are an appropriate and useful technique to discover and document business requirements, and to articulate an Architecture Vision that responds to those requirements.” – Phase A: Architecture Vision",
    "label_zh": "“业务场景是发现并记录业务需求、并阐明响应这些需求的架构愿景的合适且有用的技术。”——阶段 A：架构愿景",
    "type": "note",
    "parent": null,
    "position": "右侧第 1 段"
  },
  {
    "id": "note_b",
    "label_en": "“Business Scenarios are a useful technique to discover and document business requirements, and may be used iteratively, at different levels of detail in the hierarchical decomposition of the Business Architecture.” – Phase B: Business Architecture",
    "label_zh": "“业务场景是发现并记录业务需求的有用技术，可在业务架构分层分解的不同详细程度上迭代使用。”——阶段 B：业务架构",
    "type": "note",
    "parent": null,
    "position": "右侧第 2 段"
  },
  {
    "id": "note_rm",
    "label_en": "“Identify/document requirements – use Business Scenarios, or an analogous technique.” – Requirements Management",
    "label_zh": "“识别/记录需求——使用业务场景或类似技术。”——需求管理",
    "type": "note",
    "parent": null,
    "position": "右侧第 3 段"
  }
]
```

## 关系

```json
[
  {
    "from": "preliminary",
    "to": "ph_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "竖线，无箭头；预备阶段在循环之前（背景知识）"
  },
  {
    "from": "ph_a",
    "to": "ph_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "环上弧线，无箭头；方向按 ADM 约定"
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
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_a",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "中心辐条，无箭头"
  },
  {
    "from": "req_mgmt",
    "to": "ph_b",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_c",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_d",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_e",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_f",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_g",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "req_mgmt",
    "to": "ph_h",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "note_a",
    "to": "ph_a",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "绿色注释箭头"
  },
  {
    "from": "note_b",
    "to": "ph_b",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "绿色注释箭头"
  },
  {
    "from": "note_rm",
    "to": "req_mgmt",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "绿色注释箭头"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_entry",
    "kind": "sequence",
    "name_zh": "进入 ADM 循环",
    "steps": [
      "preliminary",
      "ph_a"
    ]
  },
  {
    "id": "f_adm",
    "kind": "cycle",
    "name_zh": "ADM 循环",
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
    "description_zh": "图中弧线无箭头，次序按 TOGAF 标准；需求管理居中贯穿所有阶段。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色圆",
    "meaning_zh": "ADM 阶段（预备阶段、A–H）",
    "explicit": false
  },
  {
    "symbol": "中心橙色大圆",
    "meaning_zh": "需求管理",
    "explicit": false
  },
  {
    "symbol": "环上灰色弧线（无箭头）",
    "meaning_zh": "相邻 ADM 阶段的次序",
    "explicit": false
  },
  {
    "symbol": "中心灰色辐条（无箭头）",
    "meaning_zh": "需求管理与每个阶段相连",
    "explicit": false
  },
  {
    "symbol": "绿色箭头 + 引文",
    "meaning_zh": "引文所说的阶段；引文末尾斜体为阶段名",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "左侧是 ADM 轮：预备阶段在最上方，下面 8 个阶段圆围成一圈（A 正上、B 右上、C 右、D 右下、E 正下、F 左下、G 左、H 左上），中心是较大的橙色需求管理圆；右侧三段带圆点的引文，各有绿色箭头指向左侧；“© The Open Group”在轮的右下方。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "三段引文与各阶段名的中文由解析者翻译；中文稿没有本图，无对照。"
  ],
  "analyzed_from": [
    "英文 PDF 第 30 页原图截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 13、30 页正文",
    "中文稿 G176e_业务场景.md 第 361–369 行（无本图）"
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
