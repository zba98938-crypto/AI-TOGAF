# G242/fig3-7 · 为实现可持续而应施加的四类约束

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-7.md) · [JSON](../../architecture/diagrams/G242/fig3-7.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 51 页

![英文原图](../assets/G242/fig3-7-p0051.png)

PDF 坐标：`[61.1, 36.0, 550.9, 326.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Constraints on Uses
Limit access with quota or dedicated group of
users to high-consuming functions like, for
example, streaming, mobile network, high
volume storage, etc.
|
$
Constraints on Applications &
Developments
Constraints on Data
Optimize energy consumption,
ee
Quota on data volumes at
rely on open library to limit
different level enterprise, business
software obsolescence, restrain
line, application, users, etc.
the use of library/framework with
high impact, choose low energy
library/framework.
( eg
t
Iteration 3
t
Iteration 2
t
Iteration 1
Constraints on Infrastructure
Take into account environmental criteria
on type of equipment purchased,
restrain number of servers, number of
virtual machine volume.
```

## 概要（历史解释；局部修正见上）

对用途、应用与开发、数据、基础设施四类对象逐步施加约束，分三轮迭代收紧，迫使 ICT 系统走向可持续。

## 目的（历史解释；局部修正见上）

把“设置约束”落到可执行的四种对象上，并用三层迭代框强调约束是逐步加严而非一次到位。它告诉架构师：可持续性约束不是抽象口号，可以具体到配额、库/框架选择、数据量上限、设备采购标准与服务器/虚拟机数量。

## 阅读顺序（历史解释；局部修正见上）

先看中心：云、网络球、数据库、显示器、网络设备组成的 ICT 系统插画。四周是四类约束：上方“对用途的约束”、左侧“对应用与开发的约束”、右侧“对数据的约束”、下方“对基础设施/设备的约束”，每类都配数支小箭头指向中心。外围三层虚线框由内到外是 Iteration 1、2、3，右下三条细引线分别指向三层框，表示每轮迭代增加一层约束。

## 关键含义（历史解释；局部修正见上）

- 四类约束分别作用于用途、应用与开发、数据、基础设施/设备，覆盖从需求到硬件的完整链条。
- 用途约束用配额或专属用户组限制高消耗功能，例如流媒体、移动网络、大容量存储。
- 应用与开发约束包括优化能耗、借助开源库避免软件过时、限制高影响库/框架、优先低能耗库/框架。
- 数据约束是在企业、业务线、应用、用户等不同层级设置数据量配额。
- 基础设施约束是在采购时纳入环境标准，并限制服务器数量与虚拟机数量。
- 三层迭代框表示约束逐步加严：Iteration 1 最内、Iteration 3 最外，每轮新增一层限制。
- 四类约束不是四选一，而是同时施加；箭头都指向中心，表示约束作用于同一 ICT 系统。

## 层级（历史解释；局部修正见上）

三层同心：Iteration 3 虚线框最外，包住 Iteration 2，再包住 Iteration 1，Iteration 1 内是 ICT 设备插画。四类约束位于同心框之外的上/左/右/下四个方位，彼此平级，不属于任何一层迭代框。

## 线条含义（历史解释；局部修正见上）

四个方向的短箭头都指向中心，表示约束施加于系统；每侧由多支叠放小箭头组成，暗示约束逐轮加码（重绘 SVG 简化为单支）。右下三条细引线不带箭头，只把 Iteration 标签连到对应虚线框，表示层级归属。

## 易误读点（历史解释；局部修正见上）

- 三层虚线框不是成熟度等级或架构层，而是约束逐步加严的三轮迭代；Iteration 1 在最内层。
- 四类约束没有先后顺序，不能按上→左→右→下当作实施步骤。
- 箭头指向中心表示“约束作用于系统”，不是数据或能量流。
- 图中的“quota（配额）”是管理上限，不是已用量或技术容量。
- 中文稿当前引用的 figs/zh/g242_fig3-7_zh.svg 每侧只画一支箭头，容易让人忽略“逐步加严”；仓库中的 zh PNG 更是把左侧蓝色箭头几乎擦掉。

## 元素

```json
[
  {
    "id": "central_system",
    "label_en": null,
    "label_zh": "中心 ICT 设备插画（云、网络球、数据库、显示器、网络设备）",
    "type": "technology",
    "parent": "iter_1",
    "position": "图形中心",
    "description_zh": "被约束的 ICT 系统示意，无文字标签。"
  },
  {
    "id": "iter_1",
    "label_en": "Iteration 1",
    "label_zh": "迭代 1",
    "type": "group",
    "parent": "iter_2",
    "level": 3,
    "position": "最内层虚线框",
    "description_zh": "第一轮约束边界。"
  },
  {
    "id": "iter_2",
    "label_en": "Iteration 2",
    "label_zh": "迭代 2",
    "type": "group",
    "parent": "iter_3",
    "level": 2,
    "position": "中间层虚线框",
    "description_zh": "第二轮约束边界。"
  },
  {
    "id": "iter_3",
    "label_en": "Iteration 3",
    "label_zh": "迭代 3",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "最外层虚线框",
    "description_zh": "第三轮约束边界。"
  },
  {
    "id": "iter_label_1",
    "label_en": "Iteration 1",
    "label_zh": "迭代 1",
    "type": "note",
    "parent": null,
    "position": "右下第三行，引线指向最内层框",
    "description_zh": "层级标注文字。"
  },
  {
    "id": "iter_label_2",
    "label_en": "Iteration 2",
    "label_zh": "迭代 2",
    "type": "note",
    "parent": null,
    "position": "右下第二行，引线指向中间层框",
    "description_zh": "层级标注文字。"
  },
  {
    "id": "iter_label_3",
    "label_en": "Iteration 3",
    "label_zh": "迭代 3",
    "type": "note",
    "parent": null,
    "position": "右下第一行，引线指向最外层框",
    "description_zh": "层级标注文字。"
  },
  {
    "id": "uses",
    "label_en": "Constraints on Uses",
    "label_zh": "对用途的约束",
    "type": "principle",
    "parent": null,
    "position": "上方",
    "description_zh": "四类约束之一。"
  },
  {
    "id": "uses_desc",
    "label_en": "Limit access with quota or dedicated group of users to high-consuming functions like, for example, streaming, mobile network, high volume storage, etc.",
    "label_zh": "以配额或专属用户组限制高消耗功能，例如流媒体、移动网络、大容量存储等",
    "type": "note",
    "parent": "uses",
    "position": "上方标题下"
  },
  {
    "id": "apps",
    "label_en": "Constraints on Applications & Developments",
    "label_zh": "对应用与开发的约束",
    "type": "principle",
    "parent": null,
    "position": "左侧",
    "description_zh": "四类约束之一。"
  },
  {
    "id": "apps_desc",
    "label_en": "Optimize energy consumption, rely on open library to limit software obsolescence, restrain the use of library/framework with high impact, choose low energy library/framework.",
    "label_zh": "优化能耗；借助开源库限制软件过时；限制高影响库/框架的使用；优先选择低能耗库/框架",
    "type": "note",
    "parent": "apps",
    "position": "左侧标题下"
  },
  {
    "id": "data",
    "label_en": "Constraints on Data",
    "label_zh": "对数据的约束",
    "type": "principle",
    "parent": null,
    "position": "右侧",
    "description_zh": "四类约束之一。"
  },
  {
    "id": "data_desc",
    "label_en": "Quota on data volumes at different level enterprise, business line, application, users, etc.",
    "label_zh": "在企业、业务线、应用、用户等不同层级设置数据量配额",
    "type": "note",
    "parent": "data",
    "position": "右侧标题下"
  },
  {
    "id": "infra",
    "label_en": "Constraints on Infrastructure",
    "label_zh": "对基础设施/设备的约束",
    "type": "principle",
    "parent": null,
    "position": "下方",
    "description_zh": "四类约束之一。"
  },
  {
    "id": "infra_desc",
    "label_en": "Take into account environmental criteria on type of equipment purchased, restrain number of servers, number of virtual machine volume.",
    "label_zh": "采购设备时纳入环境标准；限制服务器数量与虚拟机数量",
    "type": "note",
    "parent": "infra",
    "position": "下方标题下"
  }
]
```

## 关系

```json
[
  {
    "from": "uses",
    "to": "central_system",
    "type": "governs",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Constraints on Uses",
    "label_zh": "对用途的约束",
    "description_zh": "顶部三支绿色小箭头向下指向中心。"
  },
  {
    "from": "apps",
    "to": "central_system",
    "type": "governs",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Constraints on Applications & Developments",
    "label_zh": "对应用与开发的约束",
    "description_zh": "左侧三支蓝色小箭头向右指向中心。"
  },
  {
    "from": "data",
    "to": "central_system",
    "type": "governs",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Constraints on Data",
    "label_zh": "对数据的约束",
    "description_zh": "右侧三支灰色小箭头向左指向中心。"
  },
  {
    "from": "infra",
    "to": "central_system",
    "type": "governs",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Constraints on Infrastructure",
    "label_zh": "对基础设施/设备的约束",
    "description_zh": "底部三支橙色小箭头向上指向中心。"
  },
  {
    "from": "iter_label_1",
    "to": "iter_1",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "细引线，表示标签归属最内层框。"
  },
  {
    "from": "iter_label_2",
    "to": "iter_2",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "细引线，表示标签归属中间层框。"
  },
  {
    "from": "iter_label_3",
    "to": "iter_3",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "细引线，表示标签归属最外层框。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_iterations",
    "kind": "sequence",
    "name_zh": "约束逐步加严的三轮迭代",
    "steps": [
      "iter_1",
      "iter_2",
      "iter_3"
    ],
    "description_zh": "由内到外，每轮在既有约束上再加一层。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_constraints",
    "title_zh": "四类约束及示例（按原图转录）",
    "columns": [
      "约束类型",
      "作用对象",
      "示例"
    ],
    "rows": [
      [
        "Constraints on Uses（对用途的约束）",
        "业务用途/功能",
        "以配额或专属用户组限制高消耗功能：流媒体、移动网络、大容量存储等"
      ],
      [
        "Constraints on Applications & Developments（对应用与开发的约束）",
        "应用与开发",
        "优化能耗；借助开源库限制软件过时；限制高影响库/框架；优先低能耗库/框架"
      ],
      [
        "Constraints on Data（对数据的约束）",
        "数据量",
        "在企业、业务线、应用、用户等层级设置数据量配额"
      ],
      [
        "Constraints on Infrastructure（对基础设施/设备的约束）",
        "设备与基础设施",
        "采购纳入环境标准；限制服务器数量与虚拟机数量"
      ]
    ],
    "notes_zh": "原图四段说明为连续英文句，表中按语义拆分为示例列。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "三层同心虚线框",
    "meaning_zh": "约束逐轮加严的三次迭代（内→外为 Iteration 1→3）",
    "explicit": false
  },
  {
    "symbol": "指向中心的短箭头（绿/蓝/灰/橙）",
    "meaning_zh": "该方向的约束施加于中心 ICT 系统",
    "explicit": false
  },
  {
    "symbol": "多支叠放箭头",
    "meaning_zh": "约束逐轮叠加、逐步收紧",
    "explicit": false
  },
  {
    "symbol": "无箭头细引线",
    "meaning_zh": "Iteration 标签与对应虚线框的归属连线",
    "explicit": false
  },
  {
    "symbol": "设备周围的 + 号",
    "meaning_zh": "装饰性标记，未编码额外含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中心为 ICT 设备插画，外围三层同心虚线圆角框；上方、左侧、右侧、下方各一组约束标题 + 说明 + 指向中心的短箭头；右下角三行 Iteration 3/2/1 以细引线连到三层框。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-6",
    "relation": "follows",
    "note_zh": "图 3-6 给出非功能需求的变化方向，本图给出落实这些变化的四类约束"
  },
  {
    "target": "G242/fig3-5",
    "relation": "follows",
    "note_zh": "图 3-5 识别数字放弃/优化模式，本图把这些模式制度化为约束"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "每侧小箭头的数量（3 支）在 PDF 分辨率下可辨，但重绘 SVG/PNG 只保留 1 支；以英文原因为准。",
    "Iteration 三层框与四类约束的对应关系（是否每轮新增一类约束）图中未明说，只表达“逐步加严”。",
    "中心设备周围的 + 号含义不明，按装饰处理。"
  ],
  "analyzed_from": [
    "英文 PDF 第 51 页原图截图（1518×806）",
    "英文 PDF 第 51 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 815–839 行",
    "figs/zh/g242_fig3-7_zh.svg 源码",
    "figs/zh/g242_fig3-7_zh.png"
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
