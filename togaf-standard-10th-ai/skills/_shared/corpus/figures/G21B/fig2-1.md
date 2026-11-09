# G21B/fig2-1 · 本文档使用的 ArchiMate 建模记法元素

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig2-1.md) · [JSON](../../architecture/diagrams/G21B/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 18 页

![英文原图](../assets/G21B/fig2-1-p0018.png)

PDF 坐标：`[61.1, 223.3, 550.9, 542.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
pesivsin |
Principle
a)
Stakeholder CO
hot Cb
ie Ea
[Reet]
Application ~Q
Application
Function
Component
[oy
Not in the scope of this document
[Implementation and Migration |
=
Sj
Plateau
=
```

## 概要（历史解释；局部修正见上）

列出本文档使用的 ArchiMate 元素子集：5 个层/方面的 10 个元素符号，其中技术层明确不在范围内。

## 目的（历史解释；局部修正见上）

在第 2.1 节交代 C-MDM 参考模型所用的建模语言：本文档不覆盖全部 ArchiMate，只选取描述 C-MDM 所需的元素（能力、业务/应用功能与组件、业务对象、干系人、原则、plateau 等），为第 3、5 章的模型图提供统一记法。

## 阅读顺序（历史解释；局部修正见上）

从上到下按层读：Strategy（战略层）只有 Capability；Business（业务层）有 Business Actor、Business Function、Business Object、Business Collaboration；Application（应用层）有 Application Function、Application Component；Technology（技术层）只写“不在本文档范围内”；Implementation and Migration（实施与迁移层）只有 Plateau。右侧竖栏是 Motivation（动机）方面，含 Principle 与 Stakeholder，贯穿所有层。每个元素框右上角的小图标就是该元素在后续图中的记号。

## 关键含义（历史解释；局部修正见上）

- 本文档只用 ArchiMate 的一个子集；图 2-1 是该子集的完整清单，后文图（如图 3-1、图 5-3、图 5-4）中的图标都能在这里找到对应。
- 战略层只用了 Capability：表示组织、人或系统拥有的能力，通常由组织、人员、流程、信息与技术组合实现。
- 业务层有 4 个元素：Business Actor（执行行为的主体）、Business Function（一组业务行为）、Business Object（业务领域中的概念，对应 TOGAF 的“业务信息”）、Business Collaboration（两个及以上业务主体为完成集体行为而组成的集合）。
- 应用层有 2 个元素：Application Function（由应用组件执行的自动化行为）与 Application Component（可模块化替换的应用功能封装）。
- 技术层明确“Not in the scope of this document”，即本文档不建技术架构模型。
- 实施与迁移层只用了 Plateau，表示架构在有限时间内相对稳定的状态，对应第 4 章的路线图阶段（如图 4-2 与表 4-6 的 plateau）。
- 动机方面只用了 Principle（原则）与 Stakeholder（利益相关者），分别对应 4.3 节的架构原则与图 4-1 的干系人。
- 正文另说明：本文档用“嵌套”（nesting）这一视觉手法表示层级或组成关系，例如一个业务对象可包含一个或多个从属业务对象。

## 层级（历史解释；局部修正见上）

两层：第 1 层是 6 个分区（5 个 ArchiMate 层 + Motivation 方面）；第 2 层是各分区内的元素符号（Strategy 1 个、Business 4 个、Application 2 个、Technology 0 个、Implementation and Migration 1 个、Motivation 2 个）。分区是并列的层，不是上下级；Motivation 竖栏在右侧，跨全部层。

## 线条含义（历史解释；局部修正见上）

图中没有任何连接线或箭头，只有分区边框。分区之间的上下排列表示 ArchiMate 的层叠关系（战略在上、实施与迁移在下），右侧动机栏表示它可作用于各层；这些都不构成元素之间的连线关系。

## 易误读点（历史解释；局部修正见上）

- 不要把“Technology: Not in the scope of this document”理解为技术层没有元素，它表示本文档不写技术层模型，所以图中不列技术元素。
- 图中没有画 ArchiMate 关系（serving、realization 等）的记法，只列元素；关系要靠后文模型图中的连线表达。
- Plateau 不是 ADM 阶段，而是路线图上的一个稳定状态（阶段/平台期），对应表 4-6 的 Step 1–4。
- Business Object 是业务概念（对应 TOGAF 业务信息），不是数据库表或应用数据结构。

## 元素

```json
[
  {
    "id": "g_strategy",
    "label_en": "Strategy",
    "label_zh": "战略层",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 1
  },
  {
    "id": "capability",
    "label_en": "Capability",
    "label_zh": "能力",
    "type": "capability",
    "parent": "g_strategy",
    "level": 2
  },
  {
    "id": "g_business",
    "label_en": "Business",
    "label_zh": "业务层",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 2
  },
  {
    "id": "business_actor",
    "label_en": "Business Actor",
    "label_zh": "业务参与者",
    "type": "actor",
    "parent": "g_business",
    "level": 2
  },
  {
    "id": "business_function",
    "label_en": "Business Function",
    "label_zh": "业务功能",
    "type": "function",
    "parent": "g_business",
    "level": 2
  },
  {
    "id": "business_object",
    "label_en": "Business Object",
    "label_zh": "业务对象",
    "type": "data",
    "parent": "g_business",
    "level": 2
  },
  {
    "id": "business_collaboration",
    "label_en": "Business Collaboration",
    "label_zh": "业务协作",
    "type": "actor",
    "parent": "g_business",
    "level": 2,
    "description_zh": "两个及以上业务主体为完成集体行为而组成的（可能临时的）集合。"
  },
  {
    "id": "g_application",
    "label_en": "Application",
    "label_zh": "应用层",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 3
  },
  {
    "id": "application_function",
    "label_en": "Application Function",
    "label_zh": "应用功能",
    "type": "function",
    "parent": "g_application",
    "level": 2
  },
  {
    "id": "application_component",
    "label_en": "Application Component",
    "label_zh": "应用组件",
    "type": "application",
    "parent": "g_application",
    "level": 2
  },
  {
    "id": "g_technology",
    "label_en": "Technology",
    "label_zh": "技术层",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 4
  },
  {
    "id": "tech_out_of_scope",
    "label_en": "Not in the scope of this document",
    "label_zh": "不在本文档范围内",
    "type": "note",
    "parent": "g_technology",
    "level": 2
  },
  {
    "id": "g_impl",
    "label_en": "Implementation and Migration",
    "label_zh": "实施与迁移层",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 5
  },
  {
    "id": "plateau",
    "label_en": "Plateau",
    "label_zh": "平台期（plateau）",
    "type": "architecture",
    "parent": "g_impl",
    "level": 2,
    "description_zh": "架构在有限时间内相对稳定的状态，不是 ADM 阶段。"
  },
  {
    "id": "g_motivation",
    "label_en": "Motivation",
    "label_zh": "动机方面",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右侧竖栏"
  },
  {
    "id": "principle",
    "label_en": "Principle",
    "label_zh": "原则",
    "type": "principle",
    "parent": "g_motivation",
    "level": 2
  },
  {
    "id": "stakeholder",
    "label_en": "Stakeholder",
    "label_zh": "利益相关者",
    "type": "stakeholder",
    "parent": "g_motivation",
    "level": 2
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色横带 + 左上角层名（Strategy/Business/Application/Technology/Implementation and Migration）",
    "meaning_zh": "ArchiMate 的层分区",
    "explicit": true
  },
  {
    "symbol": "元素框右上角的小图标",
    "meaning_zh": "该 ArchiMate 元素的记法符号（如小人=Actor、折角箭头=Function、方框套方框=Application Component、堆叠方块=Capability）",
    "explicit": false
  },
  {
    "symbol": "右侧竖栏 Motivation",
    "meaning_zh": "动机方面，独立于 5 个层、可作用于各层",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "左侧为主区，自上而下 5 条灰色层带：Strategy、Business、Application、Technology、Implementation and Migration；每条带左上角有层名标签，带内横排元素框。右侧为贯穿全高的 Motivation 竖栏，内含 Principle 与 Stakeholder 两个框。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig3-1",
    "relation": "legend_for",
    "note_zh": "图 3-1 使用本图列出的 Capability、Business Actor、Business Function、Application Component、Application Function 记法。"
  },
  {
    "target": "G21B/fig5-3",
    "relation": "legend_for",
    "note_zh": "图 5-3 的业务功能框与业务参与者框使用本图的 Business Function / Business Actor 记法。"
  },
  {
    "target": "G21B/fig5-4",
    "relation": "legend_for",
    "note_zh": "图 5-4 的应用功能框使用本图的 Application Function 记法。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图只给出元素符号与名称，没有给出关系记法；本分析不推断未画出的关系。",
    "Motivation 竖栏是否覆盖全部层仅由版式（贯穿全高）推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 18 页原图截图（含层带与元素框）",
    "英文 PDF 第 18–20 页正文中的 ArchiMate 定义",
    "中文稿无此图引用"
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
