# G234/fig3-1 · 元数据管理能力——高层功能

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig3-1.md) · [JSON](../../architecture/diagrams/G234/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 17 页

![英文原图](../assets/G234/fig3-1-p0017.png)

PDF 坐标：`[61.1, 68.2, 550.9, 268.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Metadata Management Business Functions
Metadata Management Application Functions
A
Strategy & Roadmaps Definition
A
A
Acquisition
Governance & Measurement
A
A
Metadata
Business Glossary
Data Dictionary !
Data Usage
Governance
Reporting
Documentation
Documentation
Documentation
Integration
tule & Policy Documentation
Data Issue Documentation
Reference Data Management
Business Assets and
Technical Assets Association
Metadata Repository Design -
Administration
Communication & Training
```

## 概要（历史解释；局部修正见上）

把元数据管理能力拆成 10 项高层业务功能与 6 项高层应用功能，左右并列给出能力全景。

## 目的（历史解释；局部修正见上）

第 3.1 节的高层参考模型，为 3.2 节业务功能表、3.3 节应用功能表和第 5 章的详细参考模型提供顶层索引：先看能力由哪两块组成，再逐项下钻。

## 阅读顺序（历史解释；局部修正见上）

左黄组读业务功能：自上而下依次是战略与路线图定义、治理与度量、五个文档化功能、资产关联与存储库设计、沟通与培训。右蓝组读应用功能：采集在最上，其下并排治理与报表，再下是参考数据管理，右侧单列元数据集成，最下是管理。图中没有连线，包含关系由大组框表达，组内各项并列。

## 关键含义（历史解释；局部修正见上）

- 业务侧 10 项：战略与路线图定义、治理与度量、业务术语表文档、数据字典文档、数据使用文档、规则与政策文档、数据问题文档、业务资产与技术资产关联、元数据存储库设计、沟通与培训。
- 应用侧 6 项：采集、治理、报表、参考数据管理、元数据集成、管理。
- 两组回答不同问题：业务功能说明要产出哪些文档与治理动作，应用功能说明用哪些自动化能力支撑；两组并非一一对应。
- 业务组的纵向次序暗示推进逻辑：先定战略与治理，再做五类文档，随后做资产关联与存储库设计，最后沟通培训；但图中没有箭头，不能当成严格流程。
- 应用组把“元数据集成”单列在右侧通栏，表示它是与其他应用功能并列的一类能力，而不是跨组的连接线。
- 本图只到一级功能；每项功能的二级细化见图 5-1（业务）和图 5-2（应用），定义见表 3-1、表 3-2。

## 层级（历史解释；局部修正见上）

顶层是“元数据管理能力”（图中未单独画框）→ 两个并列组（业务功能、应用功能）→ 组内一级功能项。业务组 10 项并列，应用组 6 项并列，组内没有子功能。

## 线条含义（历史解释；局部修正见上）

全图无连线。大组框表示归属（这些功能属于业务侧或应用侧），组内位置只表示并列与阅读次序，不表示调用或依赖。

## 易误读点（历史解释；局部修正见上）

- 不要以为右侧应用功能是左侧业务功能的子集或实现；它们是两个不同层面的能力清单。
- 不要把“元数据集成”理解为连接左右两组的桥梁；它在原图中只是应用功能组里的一个独立框。
- 中文稿 SVG 只有业务功能，没有应用功能，不能据它判断本图范围；SVG 的五种颜色也没有任何图例依据。

## 元素

```json
[
  {
    "id": "grp_business_functions",
    "label_en": "Metadata Management Business Functions",
    "label_zh": "元数据管理业务功能",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左侧黄色大组",
    "description_zh": "容纳 10 个高层业务功能。"
  },
  {
    "id": "grp_application_functions",
    "label_en": "Metadata Management Application Functions",
    "label_zh": "元数据管理应用功能",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右侧蓝色大组",
    "description_zh": "容纳 6 个高层应用功能。"
  },
  {
    "id": "bf_strategy",
    "label_en": "Strategy & Roadmaps Definition",
    "label_zh": "战略与路线图定义",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 1 行通栏"
  },
  {
    "id": "bf_governance",
    "label_en": "Governance & Measurement",
    "label_zh": "治理与度量",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 2 行通栏"
  },
  {
    "id": "bf_glossary",
    "label_en": "Business Glossary Documentation",
    "label_zh": "业务术语表文档",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 3 行左"
  },
  {
    "id": "bf_dictionary",
    "label_en": "Data Dictionary Documentation",
    "label_zh": "数据字典文档",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 3 行中"
  },
  {
    "id": "bf_usage",
    "label_en": "Data Usage Documentation",
    "label_zh": "数据使用文档",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 3 行右"
  },
  {
    "id": "bf_rules",
    "label_en": "Rule & Policy Documentation",
    "label_zh": "规则与政策文档",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 4 行左"
  },
  {
    "id": "bf_issues",
    "label_en": "Data Issue Documentation",
    "label_zh": "数据问题文档",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 4 行右"
  },
  {
    "id": "bf_assets",
    "label_en": "Business Assets and Technical Assets Association",
    "label_zh": "业务资产与技术资产关联",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 5 行左"
  },
  {
    "id": "bf_repository",
    "label_en": "Metadata Repository Design",
    "label_zh": "元数据存储库设计",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 5 行右"
  },
  {
    "id": "bf_training",
    "label_en": "Communication & Training",
    "label_zh": "沟通与培训",
    "type": "function",
    "parent": "grp_business_functions",
    "level": 2,
    "position": "业务组第 6 行通栏"
  },
  {
    "id": "af_acquisition",
    "label_en": "Acquisition",
    "label_zh": "采集",
    "type": "function",
    "parent": "grp_application_functions",
    "level": 2,
    "position": "应用组顶部通栏"
  },
  {
    "id": "af_governance",
    "label_en": "Governance",
    "label_zh": "治理",
    "type": "function",
    "parent": "grp_application_functions",
    "level": 2,
    "position": "应用组左中"
  },
  {
    "id": "af_reporting",
    "label_en": "Reporting",
    "label_zh": "报表",
    "type": "function",
    "parent": "grp_application_functions",
    "level": 2,
    "position": "应用组中中"
  },
  {
    "id": "af_reference_data",
    "label_en": "Reference Data Management",
    "label_zh": "参考数据管理",
    "type": "function",
    "parent": "grp_application_functions",
    "level": 2,
    "position": "应用组中下通栏"
  },
  {
    "id": "af_integration",
    "label_en": "Metadata Integration",
    "label_zh": "元数据集成",
    "type": "function",
    "parent": "grp_application_functions",
    "level": 2,
    "position": "应用组右侧竖跨"
  },
  {
    "id": "af_administration",
    "label_en": "Administration",
    "label_zh": "管理",
    "type": "function",
    "parent": "grp_application_functions",
    "level": 2,
    "position": "应用组底部通栏"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色大组框",
    "meaning_zh": "Metadata Management Business Functions（业务功能组）",
    "explicit": true
  },
  {
    "symbol": "蓝色大组框",
    "meaning_zh": "Metadata Management Application Functions（应用功能组）",
    "explicit": true
  },
  {
    "symbol": "框右上角折角箭头",
    "meaning_zh": "ArchiMate 功能元素记号（业务功能/应用功能）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "左右两栏：左侧黄色业务功能组（10 个框，按 1-1-3-2-2-1 行排布），右侧蓝色应用功能组（采集通栏、治理与报表并排、参考数据管理通栏、元数据集成右侧竖跨、管理通栏）。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig2-1",
    "relation": "uses_legend",
    "note_zh": "本图的功能框使用图 2-1 定义的 ArchiMate 业务功能/应用功能记法"
  },
  {
    "target": "G234/fig5-1",
    "relation": "overview_of",
    "note_zh": "图 5-1 把本图 10 项业务功能展开为二级功能与角色"
  },
  {
    "target": "G234/fig5-2",
    "relation": "overview_of",
    "note_zh": "图 5-2 把本图 6 项应用功能展开为二级应用功能"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图把业务功能排成 1-1-3-2-2-1 行，但没有说明这种排版是否隐含流程顺序；本分析只按视觉分组解读，不把位置当成严格流程。",
    "框右上角的折角箭头在原图中很小，按 ArchiMate 功能元素记号理解；无法从截图辨认更细的构造型文字。"
  ],
  "analyzed_from": [
    "英文 PDF 第 17 页原图截图（2x2 放大分块）",
    "英文 PDF 第 17 页正文（表 3-1 前五项）",
    "中文稿 G234e_信息架构_元数据管理.md 第 173–204 行（表 3-1、表 3-2）",
    "figs/g234_fig3-1.svg 源码"
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
