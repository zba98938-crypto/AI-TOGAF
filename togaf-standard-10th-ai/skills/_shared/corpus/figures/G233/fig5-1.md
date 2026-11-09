# G233/fig5-1 · 价值流阶段示例（仓库订单履约价值流）

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig5-1.md) · [JSON](../../architecture/diagrams/G233/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 31 页

![英文原图](../assets/G233/fig5-1-p0031.png)

PDF 坐标：`[74.0, 239.6, 538.0, 329.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Warehouse Order Fulfillment Value Stream
D|
Customer Order Placed
DC ame
Customer Order
Processing
>}
Pick Ondered Products >>)
Pack Ordered Products, >)
Ship Ordered Products, =>)
‘Order shipped within one business day
C
```

## 概要（历史解释；局部修正见上）

一个完整价值流的示例：客户下单触发，经订单处理、拣货、包装、发运四个阶段，交付“一个工作日内发运”的成果。

## 目的（历史解释；局部修正见上）

第 5.1.2 节用具体例子说明“价值流阶段”是什么：利益相关者价值很少由单一步骤产生，而是由一串顺序/并行的阶段逐步累加。作者把触发、利益相关者、阶段序列与最终成果放在同一个价值流框内，给读者一个可套用的模板。

## 阅读顺序（历史解释；局部修正见上）

先看沙色大框的标题“Warehouse Order Fulfillment Value Stream”，它界定范围；左上黄框是触发事件（客户下单），其右紫框是接收价值的利益相关者（客户）；中间一排白色 V 形框从左到右是四个阶段；右下紫八边形是价值流成功结束时交付的成果/价值项。全图没有连线，顺序由左右位置表达。

## 关键含义（历史解释；局部修正见上）

- 价值流由四个阶段组成，顺序为：Customer Order Processing（客户订单处理）→ Pick Ordered Products（拣选所订产品）→ Pack Ordered Products（包装所订产品）→ Ship Ordered Products（发运所订产品）。
- 触发是一个业务事件“Customer Order Placed（客户下单）”，不是客户本身；Customer（客户）是接收价值的利益相关者，两者在图中分开画。
- 成果写成可判定的终态“Order shipped within one business day（订单在一个工作日内发运）”，既是价值项也可直接作为最后阶段的退出标准。
- 价值流是一个整体容器：触发事件、利益相关者、四个阶段与成果都在同一个沙色框内，表示它们属于同一条价值流。
- 图中只画了阶段名称，没有画每个阶段的描述、进入标准、退出标准；正文说明这些字段在模型中另行记录，图只是结构示意。
- 图题虽为“Example Value Stream Stage”，实际画的是“一条价值流及其阶段序列”，用于说明单个阶段所处的上下文，而不是某个阶段的字段明细。
- 阶段框与价值流容器右上角用 V 形（chevron）图标，成果用靶心带箭头图标；这与图 3-1 的 Value Stream/Stage 与 Outcome 记法一致。
- 正文提醒价值流不一定连续流动，可在任一阶段因未产生所需价值而停止；本图没有画停止/分支路径，只给顺序主线。

## 层级（历史解释；局部修正见上）

三层：价值流（沙色容器）→ 4 个价值流阶段（白框，同级并列）；触发事件与利益相关者是价值流的输入/参与要素，成果是价值流的输出，二者都不是阶段的子级。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线。阶段先后由从左到右的排列表达；阶段属于该价值流由“位于沙色框内”表达；事件位于起点表示触发整条价值流；成果位于最后阶段下方表示由该价值流产出。这些关系在清单中标为 implicit。

## 易误读点（历史解释；局部修正见上）

- 不要把四个阶段读成四个部门或四个应用系统；它们是价值流阶段（增值活动序列）。
- 不要因为“Customer Order Placed”在 Customer Order Processing 上方，就以为它只触发第一个阶段；正文说业务事件至少触发价值流，也可触发阶段，本图表达的是触发整条价值流。
- 不要把“Customer”当成执行者；它是接收价值的利益相关者，执行者在该价值流中并未画出。
- 不要把右下紫色八边形当成第五个阶段；它是成果/价值项（Order shipped within one business day）。
- 不要把本图当作单个阶段的完整规格；它没有描述、进入/退出标准等字段，只是阶段上下文示意。
- 中文 PNG 的标题字号比原图小，但阶段名与成果文字完整，不能据此认为标题缺失。

## 元素

```json
[
  {
    "id": "vs_warehouse",
    "label_en": "Warehouse Order Fulfillment Value Stream",
    "label_zh": "仓库订单履约价值流",
    "type": "value_stream",
    "parent": null,
    "position": "沙色大容器",
    "notation_type": "ArchiMate Value Stream"
  },
  {
    "id": "ev_order_placed",
    "label_en": "Customer Order Placed",
    "label_zh": "客户下单",
    "type": "event",
    "parent": "vs_warehouse",
    "position": "容器内左上（黄）",
    "notation_type": "ArchiMate Business Event",
    "description_zh": "触发整条价值流的业务事件。"
  },
  {
    "id": "st_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "stakeholder",
    "parent": "vs_warehouse",
    "position": "容器内上排中（紫）",
    "notation_type": "ArchiMate Stakeholder",
    "description_zh": "接收价值流所交付价值的利益相关者，不是执行者。"
  },
  {
    "id": "stg_order_processing",
    "label_en": "Customer Order Processing",
    "label_zh": "客户订单处理",
    "type": "value_stream_stage",
    "parent": "vs_warehouse",
    "order": 1,
    "position": "下排左一",
    "notation_type": "ArchiMate Value Stream Stage"
  },
  {
    "id": "stg_pick",
    "label_en": "Pick Ordered Products",
    "label_zh": "拣选所订产品",
    "type": "value_stream_stage",
    "parent": "vs_warehouse",
    "order": 2,
    "position": "下排左二",
    "notation_type": "ArchiMate Value Stream Stage"
  },
  {
    "id": "stg_pack",
    "label_en": "Pack Ordered Products",
    "label_zh": "包装所订产品",
    "type": "value_stream_stage",
    "parent": "vs_warehouse",
    "order": 3,
    "position": "下排左三",
    "notation_type": "ArchiMate Value Stream Stage"
  },
  {
    "id": "stg_ship",
    "label_en": "Ship Ordered Products",
    "label_zh": "发运所订产品",
    "type": "value_stream_stage",
    "parent": "vs_warehouse",
    "order": 4,
    "position": "下排右一",
    "notation_type": "ArchiMate Value Stream Stage"
  },
  {
    "id": "out_shipped",
    "label_en": "Order shipped within one business day",
    "label_zh": "订单在一个工作日内发运",
    "type": "goal",
    "parent": "vs_warehouse",
    "position": "右下紫色八边形",
    "notation_type": "ArchiMate Outcome",
    "description_zh": "价值项/成果，同时充当退出标准。"
  }
]
```

## 关系

```json
[
  {
    "from": "ev_order_placed",
    "to": "vs_warehouse",
    "type": "triggering",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "触发事件画在价值流起点，按位置推断触发整条价值流。"
  },
  {
    "from": "st_customer",
    "to": "vs_warehouse",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "客户是接收价值流的利益相关者。"
  },
  {
    "from": "vs_warehouse",
    "to": "stg_order_processing",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "阶段画在价值流容器内，表示被该价值流包含。"
  },
  {
    "from": "vs_warehouse",
    "to": "stg_pick",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_warehouse",
    "to": "stg_pack",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_warehouse",
    "to": "stg_ship",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "from": "vs_warehouse",
    "to": "out_shipped",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "价值流成功结束时交付该成果；成果框位于最后阶段下方。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_warehouse",
    "kind": "sequence",
    "name_zh": "仓库订单履约阶段序列",
    "steps": [
      "stg_order_processing",
      "stg_pick",
      "stg_pack",
      "stg_ship"
    ],
    "description_zh": "从左到右四个阶段；正文说明阶段也可能并行或提前停止，本图给出的是顺序主线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "沙色大框 + 右上角 V 形图标",
    "meaning_zh": "价值流（整体范围）",
    "explicit": false
  },
  {
    "symbol": "黄色圆角框 + 事件图标",
    "meaning_zh": "触发价值流的业务事件",
    "explicit": false
  },
  {
    "symbol": "紫色八边形 + 双人图标",
    "meaning_zh": "利益相关者（接收价值者）",
    "explicit": false
  },
  {
    "symbol": "白色圆角框 + V 形图标",
    "meaning_zh": "价值流阶段",
    "explicit": false
  },
  {
    "symbol": "紫色八边形 + 靶心带箭头图标",
    "meaning_zh": "成果/价值项（同时充当退出标准）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "沙色价值流容器内：上排左侧为触发事件（黄）与客户（紫），下排四个白色阶段框从左到右排列，右下为紫色成果八边形（位于最后阶段下方）。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig6-3",
    "relation": "related",
    "note_zh": "图 6-3 的 Deliver Products 阶段内嵌引用“Warehouse Order Fulfilment Value Stream”，即本条价值流；说明价值流可被其他价值流阶段调用"
  },
  {
    "target": "G233/figC-1",
    "relation": "complements",
    "note_zh": "图 C-1 用同样的“价值流容器＋阶段列”画法展示招聘员工价值流，可对照阶段组织方式"
  },
  {
    "target": "G233/fig3-1",
    "relation": "instance_of",
    "note_zh": "本图是图 3-1 中 Value Stream Contains Value Stream Stage、Business Event Triggers Value Stream 等关系的具体实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中未画阶段间连线，是否存在并行/循环无法从图上判断；按从左到右记录为顺序。",
    "成果八边形带 Outcome（靶心带箭头）图标，按其作为退出标准/价值项的角色记为 goal 类型，而非独立的价值元素。",
    "中文 PNG 的容器标题字号/字重较原图弱，属于本地化排版差异，不影响结构判断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 31 页图 5-1 截图（figctx 裁剪）与 2×2 放大分块",
    "英文 PDF 第 30–31 页正文",
    "中文稿 G233e_业务能力规划.md 第 425–445 行（含 8 条图内标签对照）",
    "figs/g233e_fig5-1_en.png 与 figs/zh/g233e_fig5-1_zh.png"
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
