# G233/fig3-1 · ArchiMate 业务能力元素与关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig3-1.md) · [JSON](../../architecture/diagrams/G233/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 19 页

![英文原图](../assets/G233/fig3-1-p0019.png)

PDF 坐标：`[99.8, 36.0, 512.2, 434.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
n—-
er Se
—_ oe ie
--
a ae
```

## 概要（历史解释；局部修正见上）

用 ArchiMate 元素与关系，说明业务能力如何使能价值流阶段、被实例化，并由角色、应用、数据、流程与资源支撑。

## 目的（历史解释；局部修正见上）

为整本指南规定最小的 ArchiMate 元素集与合法关系集。作者在第 3 章开头指出：业务能力规划只需要 ArchiMate 的一个子集，先用这张图把“战略—价值流—能力—能力实例—落地要素”的语义固定下来，后续能力目录、价值流映射与实例模型都复用它；表 3-1 再逐元素解释这些元素在能力规划中的用法。

## 阅读顺序（历史解释；局部修正见上）

从上往下、从中间向两侧读。上方：Stakeholder 接收 Value、受益于 Value Stream；Value Stream 提出 Value、达成 Goal，Value 由 Outcome 度量。中轴：Business Event 触发 Value Stream，Value Stream 包含 Value Stream Stage，Business Capability 以带箭头的 Enables 支撑阶段。右侧目标链：Goal 导致 Outcome，Capability 交付 Outcome。下方落地链：Business Capability Instance 以空心三角“实例化”Business Capability，并被 Business Process 使能、由 Resource 服务、与 Application Process 对齐。左下：Business Object 对齐能力，并由应用组件内的 Data Object 表示；业务角色使用应用组件、在业务流程中活动。无箭头连线按标签的语法主语→宾语理解。

## 关键含义（历史解释；局部修正见上）

- 全图用四种底色区分 ArchiMate 层：紫=动机（Stakeholder、Value、Goal、Outcome），黄=业务（Event、Object、Role、Process），沙=战略（Value Stream、Stage、Capability、Capability Instance、Resource），青=应用（Application Component、Data Object、Application Process）。
- Business Capability 是枢纽：向上用 Enables 支撑 Value Stream Stage（全图唯一带普通箭头的线），向下用 Instantiates 由 Business Capability Instance 实现（空心三角，方向为实例→能力）。
- “实例化”是能力从“做什么”变成“怎么做”的关键：能力实例再挂上 Business Role、Application Component、Business Object/Data Object、Business Process 与 Resource，这些要素才使能力可交付成果。
- 价值流是分层的：Value Stream Contains Value Stream Stage；阶段是“Is value item for”Value 的增量单位；价值最终由 Outcome 度量，而不是由活动量度量。
- 目标与成果是两种元素：Goal 是意图，Outcome 是结果；Value Stream Achieves Goal、Goal Results in Outcome、Value Measured by Outcome，Capability Delivers Outcome。
- Business Event 触发 Value Stream；表 3-1 补充说明业务事件至少触发价值流，也可触发单个价值流阶段，本图只画了触发整条价值流。
- Business Object 与 Data Object 不是一回事：前者是业务域概念对象（黄），后者是应用组件内为自动化处理而结构化的数据（青），两者以 Represented by 相连。
- 全图只有两处箭头，其余关系靠标签措辞定向；图中没有时间轴，Value Stream 与 Stage 是包含关系而非先后步骤。

## 层级（历史解释；局部修正见上）

三条层级链。价值流链：Value Stream → Value Stream Stage（由 Contains 表达，视觉上并未嵌套）。能力链：Business Capability → Business Capability Instance（实例是能力的特化/实例，箭头由实例指向能力）。应用链：Application Component 视觉上包含 Data Object 与 Application Process。业务能力与价值流阶段之间是“使能”关系，不是上下级；Stakeholder、Goal、Outcome 等是同一层的关联元素。

## 线条含义（历史解释；局部修正见上）

实线无箭头＝ArchiMate 关联，方向按标签读：Receives、Benefits from、Proposes、Achieves、Contains、Is value item for、Triggers、Aligned to、Represented by、Delivers、Served by、Enabled by、Activities in、Used by、Results in、Measured by。唯一带普通实心箭头的是 Business Capability → Value Stream Stage 的 Enables；唯一带空心三角的是 Business Capability Instance → Business Capability 的 Instantiates（画法类似 UML 泛化，语义是实例化）。

## 易误读点（历史解释；局部修正见上）

- 不要把它当流程顺序图：Value Stream 与 Stage 是包含关系，图中没有时间轴，也没有阶段顺序。
- 不要把 Business Capability Instance 当成“二级能力/子能力”；它是同一能力的一次具体实现，元素类型仍是能力。
- 不要因为 Instantiates 用空心三角就理解成“继承/特化”；标签写明是实例化，方向是实例→能力。
- 不要把所有无箭头连线都当成双向关联：多数标签有明确的主谓方向（如 Event Triggers Value Stream），应按标签读。
- 中文稿第 3.1 节引用的 figs/g233_fig3-1.svg 只是 12 个名词框加装饰线，既缺元素也缺全部关系，不能据它理解本图；必须以英文原图为准。

## 元素

```json
[
  {
    "id": "stakeholder",
    "label_en": "Stakeholder",
    "label_zh": "利益相关者",
    "type": "stakeholder",
    "parent": null,
    "position": "顶部中央偏左（紫）",
    "notation_type": "ArchiMate Stakeholder"
  },
  {
    "id": "value",
    "label_en": "Value",
    "label_zh": "价值",
    "type": "goal",
    "parent": null,
    "position": "右上（紫椭圆）",
    "notation_type": "ArchiMate Value",
    "description_zh": "价值流提出、由成果度量的相对价值/效用。"
  },
  {
    "id": "goal",
    "label_en": "Goal",
    "label_zh": "目标",
    "type": "goal",
    "parent": null,
    "position": "右中上（紫八边形）",
    "notation_type": "ArchiMate Goal"
  },
  {
    "id": "outcome",
    "label_en": "Outcome",
    "label_zh": "成果",
    "type": "goal",
    "parent": null,
    "position": "右下（紫八边形）",
    "notation_type": "ArchiMate Outcome"
  },
  {
    "id": "value_stream",
    "label_en": "Value Stream",
    "label_zh": "价值流",
    "type": "value_stream",
    "parent": null,
    "position": "中上（沙色）",
    "notation_type": "ArchiMate Value Stream"
  },
  {
    "id": "value_stream_stage",
    "label_en": "Value Stream Stage",
    "label_zh": "价值流阶段",
    "type": "value_stream_stage",
    "parent": null,
    "position": "中部（沙色）",
    "notation_type": "ArchiMate Value Stream Stage",
    "description_zh": "由 Contains 连线表示它是价值流的组成部分，视觉上未被价值流框包裹。"
  },
  {
    "id": "business_capability",
    "label_en": "Business Capability",
    "label_zh": "业务能力",
    "type": "capability",
    "parent": null,
    "position": "中央（沙色）",
    "level": 1,
    "notation_type": "ArchiMate Business Capability"
  },
  {
    "id": "business_capability_instance",
    "label_en": "Business Capability Instance",
    "label_zh": "业务能力实例",
    "type": "capability",
    "parent": null,
    "position": "下方中部（沙色）",
    "notation_type": "ArchiMate Business Capability",
    "description_zh": "同一业务能力的一次具体实现，不是子能力。"
  },
  {
    "id": "business_event",
    "label_en": "Business Event",
    "label_zh": "业务事件",
    "type": "event",
    "parent": null,
    "position": "左上（黄）",
    "notation_type": "ArchiMate Business Event"
  },
  {
    "id": "business_object",
    "label_en": "Business Object",
    "label_zh": "业务对象",
    "type": "data",
    "parent": null,
    "position": "左中（黄）",
    "notation_type": "ArchiMate Business Object"
  },
  {
    "id": "application_component",
    "label_en": "Application Component",
    "label_zh": "应用组件",
    "type": "application",
    "parent": null,
    "position": "左下（青色大框）",
    "notation_type": "ArchiMate Application Component"
  },
  {
    "id": "data_object",
    "label_en": "Data Object",
    "label_zh": "数据对象",
    "type": "data",
    "parent": "application_component",
    "position": "应用组件内上方（白框）",
    "notation_type": "ArchiMate Data Object"
  },
  {
    "id": "application_process",
    "label_en": "Application Process",
    "label_zh": "应用过程",
    "type": "process",
    "parent": "application_component",
    "position": "应用组件内下方（青框）",
    "notation_type": "ArchiMate Application Process"
  },
  {
    "id": "resource",
    "label_en": "Resource",
    "label_zh": "资源",
    "type": "resource",
    "parent": null,
    "position": "右下（沙色）",
    "notation_type": "ArchiMate Resource"
  },
  {
    "id": "business_process",
    "label_en": "Business Process",
    "label_zh": "业务流程",
    "type": "process",
    "parent": null,
    "position": "底部中央（黄）",
    "notation_type": "ArchiMate Business Process"
  },
  {
    "id": "business_role",
    "label_en": "Business Role",
    "label_zh": "业务角色",
    "type": "role",
    "parent": null,
    "position": "左下底部（黄）",
    "notation_type": "ArchiMate Business Role"
  }
]
```

## 关系

```json
[
  {
    "from": "stakeholder",
    "to": "value_stream",
    "type": "association",
    "label_en": "Benefits from",
    "label_zh": "受益于",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "利益相关者从价值流获得收益；无箭头，方向按标签。"
  },
  {
    "from": "stakeholder",
    "to": "value",
    "type": "association",
    "label_en": "Receives",
    "label_zh": "接收",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "利益相关者接收价值；无箭头。"
  },
  {
    "from": "value_stream",
    "to": "value",
    "type": "association",
    "label_en": "Proposes",
    "label_zh": "提出",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "价值流提出/交付价值；标签靠近价值流一侧，无箭头。"
  },
  {
    "from": "value_stream",
    "to": "goal",
    "type": "association",
    "label_en": "Achieves",
    "label_zh": "达成",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "价值流达成目标；无箭头。"
  },
  {
    "from": "value_stream",
    "to": "value_stream_stage",
    "type": "composition",
    "label_en": "Contains",
    "label_zh": "包含",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "价值流由阶段组成；竖向无箭头连线。"
  },
  {
    "from": "value_stream_stage",
    "to": "value",
    "type": "association",
    "label_en": "Is value item for",
    "label_zh": "是……的价值项",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "斜线从价值流阶段穿过 Goal 框画到 Value 椭圆，端点不是 Goal；按画面记为阶段→价值。"
  },
  {
    "from": "business_event",
    "to": "value_stream",
    "type": "triggering",
    "label_en": "Triggers",
    "label_zh": "触发",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "业务事件触发价值流；无箭头。"
  },
  {
    "from": "business_capability",
    "to": "value_stream_stage",
    "type": "serving",
    "label_en": "Enables",
    "label_zh": "使能",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "全图唯一带普通箭头的连线，箭头由业务能力指向价值流阶段。"
  },
  {
    "from": "business_capability_instance",
    "to": "business_capability",
    "type": "specialization",
    "label_en": "Instantiates",
    "label_zh": "实例化",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "空心三角指向业务能力，语义是能力实例实现/实例化该能力，不是继承子类。"
  },
  {
    "from": "business_capability",
    "to": "outcome",
    "type": "produces",
    "label_en": "Delivers",
    "label_zh": "交付",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "业务能力交付成果；无箭头。"
  },
  {
    "from": "business_object",
    "to": "business_capability",
    "type": "maps_to",
    "label_en": "Aligned to",
    "label_zh": "对齐于",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "业务对象对齐（可分配给）一个或多个业务能力；无箭头。"
  },
  {
    "from": "business_object",
    "to": "data_object",
    "type": "maps_to",
    "label_en": "Represented by",
    "label_zh": "表示为",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "业务对象在应用组件中表示为数据对象；无箭头。"
  },
  {
    "from": "application_process",
    "to": "business_capability_instance",
    "type": "maps_to",
    "label_en": "Aligned to",
    "label_zh": "对齐于",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "应用过程与能力实例对齐；无箭头。"
  },
  {
    "from": "resource",
    "to": "business_capability_instance",
    "type": "serving",
    "label_en": "Served by",
    "label_zh": "由……服务",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "资源为能力实例提供支撑；图上用被动语态 Served by，无箭头。"
  },
  {
    "from": "business_capability_instance",
    "to": "business_process",
    "type": "serving",
    "label_en": "Enabled by",
    "label_zh": "由……使能",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "业务流程在能力实例语境中实现结果，能力实例使能流程；无箭头。"
  },
  {
    "from": "business_role",
    "to": "business_process",
    "type": "assignment",
    "label_en": "Activities in",
    "label_zh": "在……中活动",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "业务角色在业务流程中执行行为；无箭头。"
  },
  {
    "from": "business_role",
    "to": "application_component",
    "type": "access",
    "label_en": "Used by",
    "label_zh": "被……使用",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "应用组件被业务角色使用；图上为被动语态，无箭头。"
  },
  {
    "from": "goal",
    "to": "outcome",
    "type": "produces",
    "label_en": "Results in",
    "label_zh": "导致",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "目标导致成果；无箭头。"
  },
  {
    "from": "value",
    "to": "outcome",
    "type": "association",
    "label_en": "Measured by",
    "label_zh": "由……度量",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "价值由成果度量；无箭头。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "紫色框/八边形/椭圆",
    "meaning_zh": "动机层元素：Stakeholder、Value、Goal、Outcome",
    "explicit": false
  },
  {
    "symbol": "黄色框",
    "meaning_zh": "业务层元素：Business Event、Business Object、Business Role、Business Process",
    "explicit": false
  },
  {
    "symbol": "沙色框",
    "meaning_zh": "能力与价值流元素：Value Stream、Value Stream Stage、Business Capability、Business Capability Instance、Resource",
    "explicit": false
  },
  {
    "symbol": "青色框",
    "meaning_zh": "应用层元素：Application Component 及其内部的 Data Object、Application Process",
    "explicit": false
  },
  {
    "symbol": "框右上角小图标",
    "meaning_zh": "ArchiMate 元素类型图标（能力网格、价值流 V 形、目标靶心、成果靶心带箭头、利益相关者双人等）",
    "explicit": false
  },
  {
    "symbol": "空心三角箭头",
    "meaning_zh": "实例化（Instantiates）：Business Capability Instance → Business Capability",
    "explicit": false
  },
  {
    "symbol": "普通实心箭头",
    "meaning_zh": "使能（Enables）：Business Capability → Value Stream Stage",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "网络式布局：顶部横排 Stakeholder、Value；右上 Goal、右下 Outcome；中轴自上而下为 Value Stream → Value Stream Stage → Business Capability → Business Capability Instance → Business Process，Business Event 在左、Business Object/Application Component/Business Role 在左下，Resource 在右下。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig6-2",
    "relation": "basis_for",
    "note_zh": "图 6-2 只用到本图的 Value Stream、Value Stream Stage、Business Capability 三个元素及其 Enables 关系，是同一记法的具体映射"
  },
  {
    "target": "G233/fig6-3",
    "relation": "basis_for",
    "note_zh": "图 6-3 的能力实例模型按本图定义的元素集与关系集展开：实例内嵌角色、应用组件、业务对象/数据对象与流程"
  },
  {
    "target": "G233/figC-1",
    "relation": "basis_for",
    "note_zh": "附录 C 的招聘价值流模型复用本图的 Stakeholder、Value Stream、Stage、Capability Instance、Business Object 等元素"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "16 个元素与 19 条关系均清晰可辨；但除 Enables、Instantiates 外都没有箭头，关系方向按标签语法推定。",
    "“Proposes”的主语存在歧义（价值流提出价值，还是价值向价值流提出主张），本文按“价值流提出价值”记录。",
    "“Is value item for”斜线穿过 Goal 框并终止于 Value 椭圆；若按正文语境理解“阶段的价值项服务于目标”，语义对象应为 Goal，但按画面端点记为 Value。"
  ],
  "analyzed_from": [
    "英文 PDF 第 19 页图 3-1 截图（figctx 裁剪）及 2×2、3×3 放大分块",
    "英文 PDF 第 18–19 页正文与表 3-1",
    "中文稿 G233e_业务能力规划.md 第 136–169 行（含表 3-1）",
    "figs/g233_fig3-1.svg 源码（12 个文本框与 12 条无标签连线）"
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
