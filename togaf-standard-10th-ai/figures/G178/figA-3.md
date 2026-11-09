# G178/figA-3 · 精益价值流

> 当前图示解析：[Markdown](../../architecture/diagrams/G178/figA-3.md) · [JSON](../../architecture/diagrams/G178/figA-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G178e.pdf`；SHA-256：`517130a041a8d956b2868dc39d570b84e2d80c64709e4c1368f9747388a3a026`。

## 原图 · PDF 第 27 页

![英文原图](../assets/G178/figA-3-p0027.png)

PDF 坐标：`[48.2, 36.0, 563.8, 268.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
le
Itt
172
Information
Flow
Process 1
Process 2
Process 3
Process 4
Process 5
Pes
Function A
Function B
Function ©
Function D
Fu
ne
Work Flow
1 items
\45 items
10 items
25
ott
o7
o4
LT =05 days |
LT = 5 days
days
[LT = 1 days.
PT = 10 mins,
IPT=5 mins.
[PT = 120 mins.
0 mins.
[PT = 15 mins.
CBA = 50%
CBA = 75%
[CRA = 85%
RCBA = 99%
[RCRA = 95%
Adays
OS days
S days
2days
Adays
[Total LT
5 days:
Timeline
10 mins.
‘Smins,
| 20mins |
30 mins.
l
1S mins.
J
Total PT = 180 mins.
[Activity Ratio = 3.9%
[Rolled %C&A = 30.0%
```

## 概要（历史解释；局部修正见上）

精益价值流图：信息流、工作流、时间线三层，5 个流程标注 LT/PT/%C&A，汇总得总前置时间 9.5 天、活动比 3.9%。

## 目的（历史解释；局部修正见上）

附录 A.3 用它展示精益价值流：用图表示为客户设计、生产、交付产品或服务所需的活动序列，并给每个流程加上绩效指标，以发现减少浪费的机会。作者借此说明它与业务架构价值流同名但目的不同：精益价值流记录、分析、改进信息或物料的流动，不适合分解为为利益相关者逐步创造价值的阶段，也不适合与业务能力交叉映射。

## 阅读顺序（历史解释；局部修正见上）

左侧红色数字和大括号把图分成三层：1 信息流（顶部）、2 工作流（中部）、3 时间线（底部）。先看信息流：顶部锯齿屋顶图标是客户，它的细线箭头指向流程 1；流程 1 把信息送到 IT-1，IT-1 再送到流程 2；流程 3 送到 IT-2，IT-2 送到流程 5；流程 5 的箭头回到客户。再看工作流：流程 1 到 5 由粗点线箭头依次推进，每个流程框上半写流程名，下半写执行它的职能（Function A–E），左下角人员图标旁的数字推断为人数；流程之间的收件盘图标表示排队的工作项。每个流程下方的小表给出 LT、PT 和 %C&A。最后看时间线：阶梯线在每个流程下方下沉，线上写该流程的 LT，线下写 PT；右端汇总框给出总 LT、总 PT、活动比和累积 %C&A。

## 关键含义（历史解释；局部修正见上）

- 三层结构：信息流（客户、IT 系统与流程之间的信息传递）、工作流（5 个流程依次推进及排队）、时间线（逐流程的时间与汇总指标）。
- 总前置时间 9.5 天是各流程 LT 之和（1 + 0.5 + 5 + 2 + 1）；总加工时间 180 分钟是各流程 PT 之和（10 + 5 + 120 + 30 + 15）。
- 活动比 3.9% = 总加工时间 ÷ 总前置时间；按每天 8 小时计，180 ÷（9.5 × 480）≈ 3.9%（解析者验算）。也就是说 96% 以上的时间不在加工，而在等待，这正是精益方法要找的浪费。
- 累积 %C&A 30.0% 是各流程 %C&A 连乘：50% × 75% × 85% × 99% × 95% ≈ 30.0%（解析者验算），即只有约三成工作项能一次走完全程而不需返工；流程 1 的 50% 最低。
- 按图中数字，流程 3 的 LT（5 天）和 PT（120 分钟）都最大，它前面排队的 45 个工作项也最多。
- 流程 4 不与任何 IT 系统相连；流程 1、3 向 IT 系统发出信息，流程 2、5 从 IT 系统接收信息。
- 正文：精益价值流来自精益思想（起源于日本汽车业，丰田称“物料与信息流图”），核心是识别并消除浪费，只保留为最终用户创造或增加价值的活动；给流程加上加工时间、响应时间、完整准确率等指标，就能找到减少浪费的机会。
- 与业务架构价值流的区别：这里的单元是流程（带职能、人员、IT 系统和时间指标），关注信息或物料怎样流动；业务架构价值流的单元是为利益相关者逐步创造价值的阶段，并要交叉映射到业务能力，精益价值流不适合这种用途。

## 层级（历史解释；局部修正见上）

三个横向分层（信息流 / 工作流 / 时间线）是视觉分组。工作流层内 5 个流程同级，每个流程框内含执行它的职能；客户和 IT 系统在信息流层。没有能力或阶段的层级。

## 线条含义（历史解释；局部修正见上）

细实线箭头 = 信息流，共 6 条：客户→流程 1、流程 1→IT-1、IT-1→流程 2、流程 3→IT-2、IT-2→流程 5、流程 5→客户。粗点线箭头 = 工作在流程之间推送，共 4 条（流程 1→2→3→4→5）；在 VSM 中这种箭头通常表示推式生产（背景知识）。排队图标与流程之间没有连线，由位置表示它们在哪两个流程之间。时间线是阶梯折线，不是箭头：下沉段对应一个流程，线上为 LT、线下为 PT。

## 易误读点（历史解释；局部修正见上）

- 这不是业务架构价值流图：方框是具体流程，不是价值流阶段，也没有能力映射。
- 活动比低不表示加工慢，而是等待时间远大于加工时间。
- 人员图标旁的数字（5、11、3、7、4）推断为人数，不是工作项数；“n items”才是排队的工作项。
- 框右上角的小数字 1–6（客户为 1，流程 1–5 为 2–6）推断为图形编号，不表示别的含义。
- 中文稿引用的 SVG 是另一套自拟数字（4 道工序、加工 2′–5′、等待 1′–2′、总周期 20′），没有信息流、IT 系统和指标框，不能据它理解本图。

## 元素

```json
[
  {
    "id": "g_info_flow",
    "label_en": "1 Information Flow",
    "label_zh": "1 信息流",
    "type": "group",
    "parent": null,
    "order": 1,
    "position": "顶部层"
  },
  {
    "id": "g_work_flow",
    "label_en": "2 Work Flow",
    "label_zh": "2 工作流",
    "type": "group",
    "parent": null,
    "order": 2,
    "position": "中部层"
  },
  {
    "id": "g_timeline",
    "label_en": "3 Timeline",
    "label_zh": "3 时间线",
    "type": "group",
    "parent": null,
    "order": 3,
    "position": "底部层"
  },
  {
    "id": "customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "actor",
    "notation_type": "VSM external entity (factory icon)",
    "parent": "g_info_flow",
    "position": "顶部居中",
    "attributes": {
      "box_number": 1
    }
  },
  {
    "id": "it1",
    "label_en": "IT-1",
    "label_zh": "IT 系统 1",
    "type": "application",
    "parent": "g_info_flow",
    "position": "流程 1、2 上方"
  },
  {
    "id": "it2",
    "label_en": "IT-2",
    "label_zh": "IT 系统 2",
    "type": "application",
    "parent": "g_info_flow",
    "position": "流程 3–5 上方"
  },
  {
    "id": "p1",
    "label_en": "Process 1",
    "label_zh": "流程 1",
    "type": "process",
    "parent": "g_work_flow",
    "order": 1,
    "attributes": {
      "function": "Function A",
      "people": 5,
      "LT": "1 days",
      "PT": "10 mins.",
      "pct_CA": "50%",
      "box_number": 2
    }
  },
  {
    "id": "p2",
    "label_en": "Process 2",
    "label_zh": "流程 2",
    "type": "process",
    "parent": "g_work_flow",
    "order": 2,
    "attributes": {
      "function": "Function B",
      "people": 11,
      "LT": "0.5 days",
      "PT": "5 mins.",
      "pct_CA": "75%",
      "box_number": 3
    }
  },
  {
    "id": "p3",
    "label_en": "Process 3",
    "label_zh": "流程 3",
    "type": "process",
    "parent": "g_work_flow",
    "order": 3,
    "attributes": {
      "function": "Function C",
      "people": 3,
      "LT": "5 days",
      "PT": "120 mins.",
      "pct_CA": "85%",
      "box_number": 4
    }
  },
  {
    "id": "p4",
    "label_en": "Process 4",
    "label_zh": "流程 4",
    "type": "process",
    "parent": "g_work_flow",
    "order": 4,
    "attributes": {
      "function": "Function D",
      "people": 7,
      "LT": "2 days",
      "PT": "30 mins.",
      "pct_CA": "99%",
      "box_number": 5
    }
  },
  {
    "id": "p5",
    "label_en": "Process 5",
    "label_zh": "流程 5",
    "type": "process",
    "parent": "g_work_flow",
    "order": 5,
    "attributes": {
      "function": "Function E",
      "people": 4,
      "LT": "1 days",
      "PT": "15 mins.",
      "pct_CA": "95%",
      "box_number": 6
    }
  },
  {
    "id": "fn_a",
    "label_en": "Function A",
    "label_zh": "职能 A",
    "type": "organization_unit",
    "parent": "p1",
    "description_zh": "流程框下半部，执行流程 1 的职能"
  },
  {
    "id": "fn_b",
    "label_en": "Function B",
    "label_zh": "职能 B",
    "type": "organization_unit",
    "parent": "p2"
  },
  {
    "id": "fn_c",
    "label_en": "Function C",
    "label_zh": "职能 C",
    "type": "organization_unit",
    "parent": "p3"
  },
  {
    "id": "fn_d",
    "label_en": "Function D",
    "label_zh": "职能 D",
    "type": "organization_unit",
    "parent": "p4"
  },
  {
    "id": "fn_e",
    "label_en": "Function E",
    "label_zh": "职能 E",
    "type": "organization_unit",
    "parent": "p5"
  },
  {
    "id": "q0",
    "label_en": "1 items",
    "label_zh": "排队 1 项",
    "type": "resource",
    "notation_type": "VSM inventory/queue (in-box icon)",
    "parent": "g_work_flow",
    "position": "流程 1 左侧",
    "description_zh": "进入流程 1 前排队的工作项"
  },
  {
    "id": "q2",
    "label_en": "45 items",
    "label_zh": "排队 45 项",
    "type": "resource",
    "notation_type": "VSM inventory/queue (in-box icon)",
    "parent": "g_work_flow",
    "position": "流程 2 与流程 3 之间"
  },
  {
    "id": "q3",
    "label_en": "10 items",
    "label_zh": "排队 10 项",
    "type": "resource",
    "notation_type": "VSM inventory/queue (in-box icon)",
    "parent": "g_work_flow",
    "position": "流程 3 与流程 4 之间"
  },
  {
    "id": "m_total_lt",
    "label_en": "Total LT = 9.5 days",
    "label_zh": "总前置时间 = 9.5 天",
    "type": "metric",
    "parent": "g_timeline",
    "position": "时间线右端汇总框第 1 行"
  },
  {
    "id": "m_total_pt",
    "label_en": "Total PT = 180 mins.",
    "label_zh": "总加工时间 = 180 分钟",
    "type": "metric",
    "parent": "g_timeline",
    "position": "汇总框第 2 行"
  },
  {
    "id": "m_activity_ratio",
    "label_en": "Activity Ratio = 3.9%",
    "label_zh": "活动比 = 3.9%",
    "type": "metric",
    "parent": "g_timeline",
    "position": "汇总框第 3 行"
  },
  {
    "id": "m_rolled_ca",
    "label_en": "Rolled %C&A = 30.0%",
    "label_zh": "累积完整准确率 = 30.0%",
    "type": "metric",
    "parent": "g_timeline",
    "position": "汇总框第 4 行"
  }
]
```

## 关系

```json
[
  {
    "from": "customer",
    "to": "p1",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "信息流：客户 → 流程 1（折线，先向左再向下）"
  },
  {
    "from": "p1",
    "to": "it1",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "信息流"
  },
  {
    "from": "it1",
    "to": "p2",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "信息流"
  },
  {
    "from": "p3",
    "to": "it2",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "信息流"
  },
  {
    "from": "it2",
    "to": "p5",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "信息流"
  },
  {
    "from": "p5",
    "to": "customer",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "信息流：流程 5 → 客户（折线，先向上再向左）"
  },
  {
    "from": "p1",
    "to": "p2",
    "type": "flow",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "粗点线推送箭头：工作流"
  },
  {
    "from": "p2",
    "to": "p3",
    "type": "flow",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward"
  },
  {
    "from": "p3",
    "to": "p4",
    "type": "flow",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward"
  },
  {
    "from": "p4",
    "to": "p5",
    "type": "flow",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward"
  },
  {
    "from": "q0",
    "to": "p1",
    "type": "flow",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "排队项位于流程 1 之前，等待被流程 1 处理"
  },
  {
    "from": "q2",
    "to": "p3",
    "type": "flow",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "位于流程 2 与 3 之间，等待被流程 3 处理"
  },
  {
    "from": "q3",
    "to": "p4",
    "type": "flow",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "位于流程 3 与 4 之间，等待被流程 4 处理"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_work",
    "kind": "sequence",
    "name_zh": "工作流（推送）",
    "steps": [
      "p1",
      "p2",
      "p3",
      "p4",
      "p5"
    ]
  },
  {
    "id": "f_info_1",
    "kind": "sequence",
    "name_zh": "信息流（前段）",
    "steps": [
      "customer",
      "p1",
      "it1",
      "p2"
    ]
  },
  {
    "id": "f_info_2",
    "kind": "sequence",
    "name_zh": "信息流（后段）",
    "steps": [
      "p3",
      "it2",
      "p5",
      "customer"
    ]
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_process_metrics",
    "title_zh": "逐流程数据（流程框、人员图标、指标框与时间线，按原图转录）",
    "columns": [
      "流程",
      "职能",
      "人数（人员图标）",
      "之前排队",
      "LT 前置时间",
      "PT 加工时间",
      "%C&A",
      "信息流连接"
    ],
    "rows": [
      [
        "Process 1",
        "Function A",
        "5",
        "1 items",
        "1 days",
        "10 mins.",
        "50%",
        "接收客户信息；发往 IT-1"
      ],
      [
        "Process 2",
        "Function B",
        "11",
        "无",
        "0.5 days",
        "5 mins.",
        "75%",
        "接收 IT-1 信息"
      ],
      [
        "Process 3",
        "Function C",
        "3",
        "45 items",
        "5 days",
        "120 mins.",
        "85%",
        "发往 IT-2"
      ],
      [
        "Process 4",
        "Function D",
        "7",
        "10 items",
        "2 days",
        "30 mins.",
        "99%",
        "无"
      ],
      [
        "Process 5",
        "Function E",
        "4",
        "无",
        "1 days",
        "15 mins.",
        "95%",
        "接收 IT-2 信息；发往客户"
      ]
    ],
    "notes_zh": "时间线阶梯在每个流程下方重复了该流程的 LT（线上）和 PT（线下），数值与指标框一致。“之前排队”按收件盘图标所在位置判断。"
  },
  {
    "id": "t_summary",
    "title_zh": "时间线右端汇总框",
    "columns": [
      "指标",
      "数值",
      "验算（解析者）"
    ],
    "rows": [
      [
        "Total LT 总前置时间",
        "9.5 days",
        "1 + 0.5 + 5 + 2 + 1 = 9.5 天"
      ],
      [
        "Total PT 总加工时间",
        "180 mins.",
        "10 + 5 + 120 + 30 + 15 = 180 分钟"
      ],
      [
        "Activity Ratio 活动比",
        "3.9%",
        "180 ÷（9.5 × 480）≈ 3.9%，按每天 8 小时工作时间计"
      ],
      [
        "Rolled %C&A 累积完整准确率",
        "30.0%",
        "0.50 × 0.75 × 0.85 × 0.99 × 0.95 ≈ 0.300"
      ]
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "左侧红色数字 + 大括号",
    "meaning_zh": "三层：1 信息流 / 2 工作流 / 3 时间线",
    "explicit": true
  },
  {
    "symbol": "锯齿屋顶（工厂形）浅蓝图标",
    "meaning_zh": "外部实体，此处为客户（VSM 惯例）",
    "explicit": false
  },
  {
    "symbol": "白色矩形 IT-1、IT-2",
    "meaning_zh": "IT 系统（信息系统）",
    "explicit": false
  },
  {
    "symbol": "细实线箭头",
    "meaning_zh": "信息流",
    "explicit": false
  },
  {
    "symbol": "粗点线箭头（实心三角箭头）",
    "meaning_zh": "工作在流程之间推送（VSM 中通常表示推式）",
    "explicit": false
  },
  {
    "symbol": "上浅蓝下白的流程框",
    "meaning_zh": "流程：上半为流程名，下半为执行它的职能",
    "explicit": false
  },
  {
    "symbol": "人员图标 + 数字",
    "meaning_zh": "该流程的人数（推断）",
    "explicit": false
  },
  {
    "symbol": "收件盘图标 + “n items”",
    "meaning_zh": "两个流程之间排队等待的工作项（在制品）",
    "explicit": false
  },
  {
    "symbol": "LT / PT / %C&A 小表",
    "meaning_zh": "前置时间 / 加工时间 / 完整准确率（Percent Complete & Accurate）",
    "explicit": false
  },
  {
    "symbol": "时间线阶梯（线上数值、线下数值）",
    "meaning_zh": "逐流程的 LT（线上）与 PT（线下）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "三个横向层自上而下：顶部信息流（客户居中，IT-1、IT-2 在其下方左右两侧），中部工作流（5 个流程框从左到右），底部时间线（阶梯折线 + 右端汇总框）；左侧红色数字 1/2/3 与大括号标出三层。"
}
```

## 相关图

```json
[
  {
    "target": "G178/fig1-1",
    "relation": "contrasts_with",
    "note_zh": "附录 A.3 指出精益价值流与业务架构价值流同名不同义：前者改进流程中的信息/物料流动，后者分解为为利益相关者创造价值的阶段并映射能力（如图 1-1）"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "人员图标旁的数字按 VSM 惯例解读为人数，框右上角数字解读为图形编号，图上没有说明。",
    "图中写“LT”，按 VSM 惯例为前置时间（Lead Time）；正文列举的指标是 Processing Time、Response Time、Percent Complete & Accurate，没有直接说明 LT 的含义。中文稿把 %C&A 对应的指标译为“一次合格率”，本解析用“完整准确率”。",
    "活动比 3.9% 只有按每天 8 小时折算才能得出（按 24 小时为 1.3%），这是解析者的验算，图中未说明折算口径。"
  ],
  "analyzed_from": [
    "英文 PDF 第 27 页原图截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 26–27 页正文",
    "中文稿 G178e_价值流.md 第 311–317 行",
    "figs/g178_figA-3.svg 源码"
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
