# G21B/fig1-2 · 数据管理支撑能力与 DMBoK DAMA 轮盘的对应关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig1-2.md) · [JSON](../../architecture/diagrams/G21B/fig1-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 14 页

![英文原图](../assets/G21B/fig1-2-p0014.png)

PDF 坐标：`[61.1, 36.0, 550.9, 302.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Metadata & data quality
management
Metadata
Bl&Analytics
Data integration &
‘Data Warehousing
& Business
Data Integration &,
capability
~—— interoperability
Inteligence
capability
Reference
‘& Master
& Content
Management,
Focus of this Guide
Copyright® 2017 DAMA International
```

## 概要（历史解释；局部修正见上）

把图 1-1 的“数据管理支撑”四项能力对应到 DMBoK 第 2 版 DAMA 轮盘的 10 个知识领域。

## 目的（历史解释；局部修正见上）

说明本指南所说的“数据管理支撑”只覆盖 DAMA 轮盘的部分知识领域：元数据与数据质量、BI 与分析、数据集成与互操作、参考数据与主数据（本指南关注点）；其余领域（数据安全、文档与内容管理、数据存储与运营、数据建模与设计）在本指南的能力模型中归入业务支撑或基础设施。

## 阅读顺序（历史解释；局部修正见上）

先看中心“Data Governance（数据治理）”，它是轮盘的核心；再顺时针看 10 个扇区，它们地位相同、没有先后顺序。然后看左右两侧的 4 条引线：每条引线从能力名称指向被高亮的扇区——淡黄色块表示由其他 Open Group 指南覆盖的能力，淡紫色块（Reference & Master Data）才是本指南的聚焦范围。图下方版权行说明轮盘取自 DAMA International。

## 关键含义（历史解释；局部修正见上）

- 轮盘有 10 个知识领域：数据架构、数据建模与设计、数据存储与运营、数据安全、数据集成与互操作、文档与内容管理、参考数据与主数据、数据仓库与商业智能、元数据、数据质量；中心是数据治理。
- “元数据与数据质量管理”用一条引线指向 Metadata 与 Data Quality 两个相邻扇区共同的淡黄高亮区，代表这两项由元数据管理能力覆盖。
- “BI 与分析能力”对应 Data Warehousing & Business Intelligence 扇区；“数据集成与互操作能力”对应 Data Integration & Interoperability 扇区。
- “本指南关注点”对应 Reference & Master Data 扇区，用淡紫色（不同于其他三处淡黄）标出，C-MDM 就落在这一领域。
- 正文明确其余领域如何被覆盖：数据安全属于业务支撑中的“安全”；文档与内容管理属于“工作场所”；数据存储与运营属于“基础设施”（技术横向能力）；数据建模与设计是“IT 管理”的子集。
- 因此“数据管理支撑”的四项能力不是 DAMA 轮盘的全部，而是经过剪裁、与本指南范围对齐的子集。

## 层级（历史解释；局部修正见上）

轮盘为单层结构：中心的数据治理 + 周围 10 个并列知识领域；10 个领域之间没有上下级。4 个能力标注是轮盘外的注释标签，不属于层级中的节点。

## 线条含义（历史解释；局部修正见上）

4 条细实线是无箭头的引线，只表示“该能力名称指的就是这个扇区”，不表示流向或依赖；扇区之间的黑色轮辐线只起分隔作用，不表示关系。中心圆与扇区相接表示数据治理是轮盘的核心主题（背景知识）。

## 易误读点（历史解释；局部修正见上）

- 不要把 10 个扇区读成流程步骤或成熟度等级，它们只是并列的知识领域。
- 淡黄色与淡紫色高亮含义不同：淡黄是“由其他指南/能力覆盖”，淡紫是“本指南关注点”，不能都当作重点。
- “元数据与数据质量管理”不是两个独立能力标注，而是一个能力名同时覆盖 Metadata 与 Data Quality 两个扇区。
- 中文稿的本地化图把“参考数据与主数据”标签缩得很小、轮辐线有断裂，不要据此认为该领域不重要。

## 元素

```json
[
  {
    "id": "dama_wheel",
    "label_en": null,
    "label_zh": "DAMA 轮盘",
    "type": "group",
    "parent": null,
    "position": "画面中央"
  },
  {
    "id": "dama_center",
    "label_en": "Data Governance",
    "label_zh": "数据治理",
    "type": "concept",
    "parent": "dama_wheel",
    "level": 1,
    "position": "轮盘中心圆"
  },
  {
    "id": "da",
    "label_en": "Data Architecture",
    "label_zh": "数据架构",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "顶部偏左扇区"
  },
  {
    "id": "dmd",
    "label_en": "Data Modeling & Design",
    "label_zh": "数据建模与设计",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "顶部偏右扇区"
  },
  {
    "id": "dso",
    "label_en": "Data Storage & Operations",
    "label_zh": "数据存储与运营",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "右上扇区"
  },
  {
    "id": "dsec",
    "label_en": "Data Security",
    "label_zh": "数据安全",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "右侧扇区"
  },
  {
    "id": "dii",
    "label_en": "Data Integration & Interoperability",
    "label_zh": "数据集成与互操作",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "右下扇区",
    "description_zh": "扇区外叠淡黄高亮。"
  },
  {
    "id": "dcm",
    "label_en": "Document & Content Management",
    "label_zh": "文档与内容管理",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "底部偏右扇区"
  },
  {
    "id": "rmd",
    "label_en": "Reference & Master Data",
    "label_zh": "参考数据与主数据",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "底部偏左扇区",
    "description_zh": "扇区外叠淡紫色高亮，为本指南关注点。"
  },
  {
    "id": "dwbi",
    "label_en": "Data Warehousing & Business Intelligence",
    "label_zh": "数据仓库与商业智能",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "左下扇区"
  },
  {
    "id": "meta",
    "label_en": "Metadata",
    "label_zh": "元数据",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "左侧扇区"
  },
  {
    "id": "dq",
    "label_en": "Data Quality",
    "label_zh": "数据质量",
    "type": "data",
    "parent": "dama_wheel",
    "level": 2,
    "position": "左上扇区"
  },
  {
    "id": "cl_meta",
    "label_en": "Metadata & data quality management",
    "label_zh": "元数据与数据质量管理",
    "type": "note",
    "parent": null,
    "position": "左侧上部"
  },
  {
    "id": "cl_bi",
    "label_en": "BI&Analytics capability",
    "label_zh": "BI 与分析能力",
    "type": "note",
    "parent": null,
    "position": "左侧中部"
  },
  {
    "id": "cl_dii",
    "label_en": "Data integration & interoperability capability",
    "label_zh": "数据集成与互操作性能力",
    "type": "note",
    "parent": null,
    "position": "右侧中部"
  },
  {
    "id": "cl_focus",
    "label_en": "Focus of this Guide",
    "label_zh": "本指南关注点",
    "type": "note",
    "parent": null,
    "position": "左下"
  },
  {
    "id": "copyright",
    "label_en": "Copyright® 2017 DAMA International",
    "label_zh": "版权：DAMA International 2017",
    "type": "note",
    "parent": null,
    "position": "轮盘下方"
  }
]
```

## 关系

```json
[
  {
    "from": "cl_meta",
    "to": "meta",
    "type": "maps_to",
    "label_en": "Metadata & data quality management",
    "label_zh": "元数据与数据质量管理",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "引线指向 Metadata 与 Data Quality 两个扇区共同的淡黄高亮区。"
  },
  {
    "from": "cl_meta",
    "to": "dq",
    "type": "maps_to",
    "label_en": "Metadata & data quality management",
    "label_zh": "元数据与数据质量管理",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "同一条引线覆盖相邻的 Data Quality 扇区。"
  },
  {
    "from": "cl_bi",
    "to": "dwbi",
    "type": "maps_to",
    "label_en": "BI&Analytics capability",
    "label_zh": "BI 与分析能力",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "cl_dii",
    "to": "dii",
    "type": "maps_to",
    "label_en": "Data integration & interoperability capability",
    "label_zh": "数据集成与互操作性能力",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "cl_focus",
    "to": "rmd",
    "type": "maps_to",
    "label_en": "Focus of this Guide",
    "label_zh": "本指南关注点",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "引线指向淡紫色高亮的 Reference & Master Data 扇区。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "轮盘 10 个扇区",
    "meaning_zh": "DMBoK 第 2 版的 10 个数据管理知识领域",
    "explicit": false
  },
  {
    "symbol": "中心圆 Data Governance",
    "meaning_zh": "数据治理是轮盘的核心主题",
    "explicit": false
  },
  {
    "symbol": "淡黄色高亮块",
    "meaning_zh": "由本图 4 个能力标注覆盖的知识领域（元数据与数据质量、数据仓库与 BI、数据集成与互操作）",
    "explicit": false
  },
  {
    "symbol": "淡紫色高亮块",
    "meaning_zh": "本指南（C-MDM）关注点：参考数据与主数据",
    "explicit": false
  },
  {
    "symbol": "无箭头细引线",
    "meaning_zh": "把轮盘外的能力名称指向对应扇区，仅表示对应关系",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中央为圆形轮盘：内圆 Data Governance，外环 10 个等分扇区；左侧两条引线（元数据与数据质量管理、BI 与分析能力），右侧两条引线（数据集成与互操作能力、本指南关注点）；底部版权行。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig1-1",
    "relation": "detail_of",
    "note_zh": "本图是图 1-1“数据管理支撑”能力区与其在 DMBoK 中对应知识领域的细化。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "轮盘外的高亮块是用矩形叠色而非精确扇区着色，Metadata 与 Data Quality 共用一块淡黄区域；无法从像素判断是否刻意将两者合并为一个能力。",
    "轮盘中心 Data Governance 与 10 个扇区的关系（治理覆盖全部领域）依据 DAMA 框架常识推断，图中只有几何相邻，没有文字说明。"
  ],
  "analyzed_from": [
    "英文 PDF 第 14 页原图截图（1522×841）",
    "英文 PDF 第 14 页正文、第 13 页相关段落",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 110、112、136–141 行",
    "figs/zh/g21be_fig1-2_zh.png 中文化图"
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
