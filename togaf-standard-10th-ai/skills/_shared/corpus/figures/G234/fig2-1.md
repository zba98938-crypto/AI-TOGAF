# G234/fig2-1 · 本文档使用的 ArchiMate 建模元素

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig2-1.md) · [JSON](../../architecture/diagrams/G234/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 12 页

![英文原图](../assets/G234/fig2-1-p0012.png)

PDF 坐标：`[138.5, 207.5, 473.5, 366.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
ht Go Eo
Not in the scope of this document
```

## 概要（历史解释；局部修正见上）

本文档 ArchiMate 元素分层图例：动机层目标/需求、业务层角色/功能/协作、应用层应用功能；技术层不在范围。

## 目的（历史解释；局部修正见上）

第 2.1 节声明全文参考模型采用 ArchiMate 正式记法，并先用一张图例统一元素名称、形状与建模范围；后文图 3-1、图 5-1、图 5-2 的每个框都依赖这套记法来区分“谁负责、做什么、产出什么”。

## 阅读顺序（历史解释；局部修正见上）

先看四个灰色带标题定位层：左上 Business、左下 Application、正下方 Technology、右侧 Motivation。每个带内是该层允许出现的元素示例；Technology 带内只有一句 “Not in the scope of this document”。图里没有任何连线，元素之间也没有上下级，只有“属于哪一层”的归属关系。

## 关键含义（历史解释；局部修正见上）

- 本图只定义记法，不是元数据管理模型；它回答“后文用哪些符号说话”。
- 动机层只有 Goal 与 Requirement，位于右侧独立带，表示建模从“为何要做”开始。
- 业务层列 Business Role、Business Function、Business Collaboration：角色与协作是主动结构（谁来做），业务功能是行为（做什么）。
- 应用层只列 Application Function，说明参考模型不细化应用组件、接口或服务。
- 技术层明确标注不在本文档范围，因此后文不会出现技术节点、设备或平台的技术架构模型。
- 原图靠形状与图标区分元素种类；中文重绘 SVG 抹平了形状差异并删掉技术层，是理解本图时最容易出错的地方。

## 层级（历史解释；局部修正见上）

四个并列层带（Motivation / Business / Application / Technology）；元素隶属所在带。业务层三元素并列，动机层两元素并列，层与层之间没有上下级连线。

## 线条含义（历史解释；局部修正见上）

图中没有连线。层带边界表示 ArchiMate 分层；元素在带内的位置只表示归属，不表示顺序或依赖。

## 易误读点（历史解释；局部修正见上）

- 不要以为原图没有技术层：原图有 Technology 带，只是写明技术层不在本文档范围内。
- 不要把六个元素当成同一层级的清单；它们分属动机、业务、应用三层。
- 不要把中文稿 SVG 底部的“逐层把为何落到如何实现”当成原图结论，原图没有这句话，也没有箭头。

## 元素

```json
[
  {
    "id": "layer_business",
    "label_en": "Business",
    "label_zh": "业务层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左上横带",
    "description_zh": "ArchiMate 业务层，包含三个元素。"
  },
  {
    "id": "layer_application",
    "label_en": "Application",
    "label_zh": "应用层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左中横带",
    "description_zh": "ArchiMate 应用层，只列一个应用功能。"
  },
  {
    "id": "layer_technology",
    "label_en": "Technology",
    "label_zh": "技术层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左下横带",
    "description_zh": "ArchiMate 技术层，带内只有范围说明。"
  },
  {
    "id": "layer_motivation",
    "label_en": "Motivation",
    "label_zh": "动机层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右侧竖带",
    "description_zh": "ArchiMate 动机层，含目标与需求。"
  },
  {
    "id": "business_role",
    "label_en": "Business Role",
    "label_zh": "业务角色",
    "type": "role",
    "parent": "layer_business",
    "level": 2,
    "position": "业务带左",
    "description_zh": "执行特定行为的责任，可分配参与者。"
  },
  {
    "id": "business_function",
    "label_en": "Business Function",
    "label_zh": "业务功能",
    "type": "function",
    "parent": "layer_business",
    "level": 2,
    "position": "业务带中",
    "description_zh": "基于一组标准的业务行为集合。"
  },
  {
    "id": "business_collaboration",
    "label_en": "Business Collaboration",
    "label_zh": "业务协作",
    "type": "organization_unit",
    "parent": "layer_business",
    "level": 2,
    "position": "业务带右",
    "description_zh": "两个或以上业务内部主动结构要素的聚合，共同执行集体行为。"
  },
  {
    "id": "application_function",
    "label_en": "Application Function",
    "label_zh": "应用功能",
    "type": "function",
    "parent": "layer_application",
    "level": 2,
    "position": "应用带左",
    "description_zh": "可由应用组件执行的自动化行为。"
  },
  {
    "id": "goal",
    "label_en": "Goal",
    "label_zh": "目标",
    "type": "goal",
    "parent": "layer_motivation",
    "level": 2,
    "position": "动机带上",
    "description_zh": "对组织及其利益相关者的意图、方向或期望终态的高层陈述。"
  },
  {
    "id": "requirement",
    "label_en": "Requirement",
    "label_zh": "需求",
    "type": "requirement",
    "parent": "layer_motivation",
    "level": 2,
    "position": "动机带下",
    "description_zh": "定义适用于架构所描述特定系统之属性的需求陈述。"
  },
  {
    "id": "tech_scope_note",
    "label_en": "Not in the scope of this document",
    "label_zh": "不在本文档范围内",
    "type": "note",
    "parent": "layer_technology",
    "level": 2,
    "position": "技术带居中",
    "description_zh": "原图技术层唯一的文字，声明技术层不建模。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色带标题 Business / Application / Technology / Motivation",
    "meaning_zh": "ArchiMate 分层：业务层、应用层、技术层、动机层",
    "explicit": true
  },
  {
    "symbol": "黄色框 + 角色/功能图标",
    "meaning_zh": "业务层元素（业务角色、业务功能、业务协作）",
    "explicit": false
  },
  {
    "symbol": "浅蓝框 + 功能图标",
    "meaning_zh": "应用层元素（应用功能）",
    "explicit": false
  },
  {
    "symbol": "淡紫框",
    "meaning_zh": "动机层元素（目标、需求）",
    "explicit": false
  },
  {
    "symbol": "“Not in the scope of this document”",
    "meaning_zh": "技术层不在本文档建模范围",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "左侧上下两条横带（Business 在上、Application 在中、Technology 在最下），右侧一条高竖带 Motivation；各带内元素横向排列。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig3-1",
    "relation": "legend_for",
    "note_zh": "图 3-1 的业务/应用功能框使用本图定义的元素记法"
  },
  {
    "target": "G234/fig5-1",
    "relation": "legend_for",
    "note_zh": "图 5-1 的业务功能层级使用本图定义的元素记法"
  },
  {
    "target": "G234/fig5-2",
    "relation": "legend_for",
    "note_zh": "图 5-2 的应用功能层级使用本图定义的元素记法"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "技术层在原图中只有一句范围说明，没有给出任何技术元素示例，无法判断原设计是否还省略了其他技术层元素。",
    "中文重绘 SVG 与英文原图差异很大，本分析以英文 PDF 第 12 页截图为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 12 页原图截图（2x2 放大分块）",
    "英文 PDF 第 12 页正文",
    "中文稿 G234e_信息架构_元数据管理.md 第 95–113 行",
    "figs/g234_legend.svg 源码"
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
