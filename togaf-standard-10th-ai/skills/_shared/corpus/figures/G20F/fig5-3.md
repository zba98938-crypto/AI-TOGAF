# G20F/fig5-3 · 商业模式画布（BMC）模板

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig5-3.md) · [JSON](../../architecture/diagrams/G20F/fig5-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 38 页

![英文原图](../assets/G20F/fig5-3-p0038.png)

PDF 坐标：`[84.2, 352.3, 563.8, 622.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Customer
Customer
Key Partners Key Activities | Value Proposition
Relationships | Segments
Key
Channels
Resources
Cost Structure
Revenue Streams
```

## 概要（历史解释；局部修正见上）

一张空白的商业模式画布模板，用九个区块规定描述商业模式时要填什么。

## 目的（历史解释；局部修正见上）

在 5.2.1“定义问题”阶段，把商业模式画布列为刻画问题的敏捷工具之一：先用九个区块把业务的基本特征摊开，再据此定义要处理的需求。图中只给模板，不含任何示例内容，细节指向《TOGAF 系列指南：业务模型》[G18A]。

## 阅读顺序（历史解释；局部修正见上）

这是一张空白模板，没有箭头也没有数据。按“价值创造—价值交付—价值获取”的顺序读：左列 Key Partners 提供 Key Activities，Key Activities 消耗 Key Resources，三者共同支撑中间最大的 Value Proposition；价值主张通过 Customer Relationships 与 Channels 触达右侧的 Customer Segments。底部一行是结果面：左边 Cost Structure 记录成本，右边 Revenue Streams 记录收入。

## 关键含义（历史解释；局部修正见上）

- 画布分为九个区块：Key Partners、Key Activities、Key Resources、Value Proposition、Customer Relationships、Channels、Customer Segments、Cost Structure、Revenue Streams。
- Layout 体现商业逻辑：左侧是供给与成本侧（伙伴、活动、资源），中间是价值主张，右侧是需求与收入侧（关系、渠道、客户），底部是财务结果（成本/收入）。
- Value Proposition 占中部整列、Customer Segments 占右端整列，说明二者是画布的两个核心锚点。
- 图中没有任何填写内容，它是模板而非案例；正文用它来说明“用什么框架刻画问题”，具体填写方法见 G18A。
- 在本文语境中，画布属于“定义问题”可用的敏捷工具之一，与业务需求、客户旅程、设计思维、Epic 并列。

## 层级（历史解释；局部修正见上）

没有上下级，只有版式分区：画布是一个大框，内部被切成 5 列 + 2 个底部横格；Key Activities 与 Key Resources 上下叠在同一列，Customer Relationships 与 Channels 上下叠在同一列。

## 线条含义（历史解释；局部修正见上）

图中只有分隔区块的直线，没有箭头或连线；任何“伙伴→活动→价值主张→客户”的流向都由区块位置隐含，属阅读惯例而非图中绘制的关系。

## 易误读点（历史解释；局部修正见上）

- 不要以为图中有任何案例数据：九个区块全是空的，它只是模板。
- 不要把相邻区块的边界线读成流程箭头；画布没有表达顺序或因果。
- 不要把 Key Activities 与 Key Resources 读成两个独立列：它们同属第二列，上下分割。
- 中文稿引用的 figs/zh/g20fe_fig5-3_zh.svg 是可用的重绘版；同目录下的 g20fe_fig5-3_zh.png 文字层错位严重（多处中英重叠、标签跑出框外），不要使用。

## 元素

```json
[
  {
    "id": "canvas",
    "label_en": null,
    "label_zh": "商业模式画布（整体）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "整张画布"
  },
  {
    "id": "key_partners",
    "label_en": "Key Partners",
    "label_zh": "关键合作伙伴",
    "type": "group",
    "parent": "canvas",
    "position": "第 1 列，通高"
  },
  {
    "id": "key_activities",
    "label_en": "Key Activities",
    "label_zh": "关键活动",
    "type": "group",
    "parent": "canvas",
    "position": "第 2 列上半"
  },
  {
    "id": "key_resources",
    "label_en": "Key Resources",
    "label_zh": "关键资源",
    "type": "group",
    "parent": "canvas",
    "position": "第 2 列下半"
  },
  {
    "id": "value_proposition",
    "label_en": "Value Proposition",
    "label_zh": "价值主张",
    "type": "group",
    "parent": "canvas",
    "position": "第 3 列，通高"
  },
  {
    "id": "customer_relationships",
    "label_en": "Customer Relationships",
    "label_zh": "客户关系",
    "type": "group",
    "parent": "canvas",
    "position": "第 4 列上半"
  },
  {
    "id": "channels",
    "label_en": "Channels",
    "label_zh": "渠道",
    "type": "group",
    "parent": "canvas",
    "position": "第 4 列下半"
  },
  {
    "id": "customer_segments",
    "label_en": "Customer Segments",
    "label_zh": "客户细分",
    "type": "group",
    "parent": "canvas",
    "position": "第 5 列，通高"
  },
  {
    "id": "cost_structure",
    "label_en": "Cost Structure",
    "label_zh": "成本结构",
    "type": "group",
    "parent": "canvas",
    "position": "底部左格"
  },
  {
    "id": "revenue_streams",
    "label_en": "Revenue Streams",
    "label_zh": "收入来源",
    "type": "group",
    "parent": "canvas",
    "position": "底部右格"
  }
]
```

## 图例

```json
[
  {
    "symbol": "细线分隔的矩形区块",
    "meaning_zh": "画布的一个构建块（待填写）",
    "explicit": false
  },
  {
    "symbol": "中部整列大区块",
    "meaning_zh": "价值主张（画布核心）",
    "explicit": false
  },
  {
    "symbol": "底部两个横格",
    "meaning_zh": "财务结果：成本结构与收入来源",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "5 列 × 2 行（第二行只在第 2、4 列各分上下两格）再加底部整行两格：左起第 1 列 Key Partners 通高，第 2 列上 Key Activities / 下 Key Resources，第 3 列 Value Proposition 通高，第 4 列上 Customer Relationships / 下 Channels，第 5 列 Customer Segments 通高；底部左 Cost Structure、右 Revenue Streams。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig2-4",
    "relation": "related",
    "note_zh": "同一商业模式画布（G18A 图 A-1 与其为同一张图），本文正文把细节指向《业务模型》指南。"
  },
  {
    "target": "G20F/fig5-4",
    "relation": "related",
    "note_zh": "同属第 5 章：画布用于定义问题，图 5-4 说明架构如何支撑后续待办定义。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图内没有标题，中文图题“商业模式画布（BMC）模板”取自中文稿图注。",
    "画布本身无内容，各区块应填什么只能引用 Osterwalder 画布的通行定义，图中未作说明。"
  ],
  "analyzed_from": [
    "英文 PDF 第 38 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 38 页正文（5.2.1 工具清单）",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 476–489 行",
    "figs/g20fe_fig5-3_en.png、figs/zh/g20fe_fig5-3_zh.png 与 figs/zh/g20fe_fig5-3_zh.svg"
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
