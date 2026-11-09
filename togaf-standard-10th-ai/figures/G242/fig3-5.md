# G242/fig3-5 · 结合自上而下与自下而上的方法以捕获数字可持续性需求

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-5.md) · [JSON](../../architecture/diagrams/G242/fig3-5.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 48 页

![英文原图](../assets/G242/fig3-5-p0048.png)

PDF 坐标：`[61.1, 449.8, 550.9, 711.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
>
Top-Down
Bottom-Up
Business Uses-Based
Infrastructure-Based Approach
Approach
Adapting Business Architecture
.
Identifying equipment that
Starting work with
has the biggest
businesses to understand
environmental impact
real business uses of the
Identifying equipment that
system
could be removed or
Identifying the business
Adapting Application
improved from
uses for which digital is
Architecture : Software
environmental impact point
vital
Choices, Development, Data
of view
Identifying patterns in the
Management
Identifying patterns in the
use-cases where digital
equipment where digital
renouncement is possible
renouncement or
and stating them as
optimization is possible
standards or principles in
Adapting Technology
and stating them as
the Architecture Repository
Architecture : Servers,
standard or principles in
the Architecture Repository
Terminals, Network Devices
Identifying Patterns for Digital Renouncement or Optimization
```

## 概要（历史解释；局部修正见上）

自上而下从业务用途、自下而上从基础设施，两条路径在业务/应用/技术架构汇合，产出数字放弃或优化模式。

## 目的（历史解释；局部修正见上）

说明捕获数字可持续性需求不能只靠单一视角：自上而下贴近业务运营者，识别哪些用途真正需要数字技术；自下而上贴近基础设施，识别环境影响最大的设备。两条路径最终都落到同一组业务/应用/技术架构调整，并沉淀为可复用的“数字放弃或优化”模式。

## 阅读顺序（历史解释；局部修正见上）

先读左侧绿色框：Top-Down Business Uses-Based Approach，三条要点说明从业务真实用途出发、识别关键用途、把可放弃的模式写入架构存储库。再看中间纵列三个架构框：业务架构 → 应用架构 → 技术架构。右侧紫色框是 Bottom-Up Infrastructure-Based Approach，三条要点从设备环境影响出发。绿色粗箭头向下、紫色粗箭头向上，表示两条路径方向相反；底部横条是两条路径的共同产出。

## 关键含义（历史解释；局部修正见上）

- 自上而下路径的起点是业务：先与业务方一起理解系统真实的业务用途，再识别哪些用途对数字技术至关重要。
- 自下而上路径的起点是设备：先找出环境影响最大的设备，再识别可移除或可改进的设备。
- 两条路径都把识别出的模式写成标准或原则，放入架构存储库（Architecture Repository）。
- 中间三层是两条路径共同的落点：业务架构、应用架构（软件选择、开发、数据管理）、技术架构（服务器、终端、网络设备）。
- 绿色向下箭头表示自上而下逐层下探，紫色向上箭头表示自下而上逐层上升；两条路径不是二选一，而是同时实施。
- 底部“Identifying Patterns for Digital Renouncement or Optimization”是共同产出：可复用的数字放弃/优化模式。
- 正文强调两者唯一变化的参数是切入点：优化业务用途要“向下”走到技术系统，优化技术系统要“向上”走到业务用途并取得业务方接受。

## 层级（历史解释；局部修正见上）

三栏并列：左方法框、中架构列、右方法框。中间三个架构框自上而下排列（业务→应用→技术），但彼此没有画线，顺序由上下位置与两条方向箭头表达；左右方法框各含三条平级要点；底部汇合条横贯全宽，是共同产出。

## 线条含义（历史解释；局部修正见上）

两条粗箭头是方向指示而非框间连接：绿色箭头在架构列左侧、由上向下，表示自上而下的下探路径；紫色箭头在架构列右侧、由下向上，表示自下而上的上升路径。中间三个架构框之间没有箭头；底部汇合条与上方没有连线，汇合关系由版式隐含。

## 易误读点（历史解释；局部修正见上）

- 不要把自上而下与自下而上理解为先后两步；正文要求同时实施（combining simultaneously）。
- 绿色/紫色箭头不是数据流，也不是架构层之间的接口，只表示两条路径的行进方向。
- 中间三个架构框不是三个项目阶段，而是同一系统的三个架构层。
- 底部“数字放弃（digital renouncement）”不是简单删除功能，而是经业务确认后放弃不必要的数字用途或设备。
- 中文稿当前引用的 figs/zh/g242_fig3-5_zh.svg 结构忠实；但仓库中的 figs/zh/g242_fig3-5_zh.png 只译了标题，要点仍是英文，若误用该 PNG 会以为中文版缺内容。

## 元素

```json
[
  {
    "id": "top_down",
    "label_en": "Top-Down Business Uses-Based Approach",
    "label_zh": "自上而下、基于业务用途的方法",
    "type": "concept",
    "parent": null,
    "position": "左栏绿色虚线框",
    "description_zh": "以业务用途为切入点的需求识别方法。"
  },
  {
    "id": "td_b1",
    "label_en": "Starting work with businesses to understand real business uses of the system",
    "label_zh": "与业务方一起工作，理解系统真实的业务用途",
    "type": "note",
    "parent": "top_down",
    "position": "左栏第 1 条要点"
  },
  {
    "id": "td_b2",
    "label_en": "Identifying the business uses for which digital is vital",
    "label_zh": "识别哪些业务用途对数字技术至关重要",
    "type": "note",
    "parent": "top_down",
    "position": "左栏第 2 条要点"
  },
  {
    "id": "td_b3",
    "label_en": "Identifying patterns in the use-cases where digital renouncement is possible and stating them as standards or principles in the Architecture Repository",
    "label_zh": "识别可“数字放弃”的用例模式，并将其写入架构存储库作为标准或原则",
    "type": "note",
    "parent": "top_down",
    "position": "左栏第 3 条要点"
  },
  {
    "id": "business_arch",
    "label_en": "Adapting Business Architecture",
    "label_zh": "调整业务架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 1,
    "position": "中栏最上框"
  },
  {
    "id": "application_arch",
    "label_en": "Adapting Application Architecture : Software Choices, Development, Data Management",
    "label_zh": "调整应用架构：软件选择、开发、数据管理",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 2,
    "position": "中栏中间框"
  },
  {
    "id": "technology_arch",
    "label_en": "Adapting Technology Architecture : Servers, Terminals, Network Devices",
    "label_zh": "调整技术架构：服务器、终端、网络设备",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 3,
    "position": "中栏最下框"
  },
  {
    "id": "bottom_up",
    "label_en": "Bottom-Up Infrastructure-Based Approach",
    "label_zh": "自下而上、基于基础设施的方法",
    "type": "concept",
    "parent": null,
    "position": "右栏紫色虚线框",
    "description_zh": "以基础设施/设备为切入点的需求识别方法。"
  },
  {
    "id": "bu_b1",
    "label_en": "Identifying equipment that has the biggest environmental impact",
    "label_zh": "识别环境影响最大的设备",
    "type": "note",
    "parent": "bottom_up",
    "position": "右栏第 1 条要点"
  },
  {
    "id": "bu_b2",
    "label_en": "Identifying equipment that could be removed or improved from environmental impact point of view",
    "label_zh": "从环境影响角度识别可移除或可改进的设备",
    "type": "note",
    "parent": "bottom_up",
    "position": "右栏第 2 条要点"
  },
  {
    "id": "bu_b3",
    "label_en": "Identifying patterns in the equipment where digital renouncement or optimization is possible and stating them as standard or principles in the Architecture Repository",
    "label_zh": "识别设备层面可“数字放弃”或优化的模式，并写入架构存储库作为标准或原则",
    "type": "note",
    "parent": "bottom_up",
    "position": "右栏第 3 条要点"
  },
  {
    "id": "outcome",
    "label_en": "Identifying Patterns for Digital Renouncement or Optimization",
    "label_zh": "识别数字放弃或优化的模式",
    "type": "artifact",
    "parent": null,
    "position": "底部横条",
    "description_zh": "两条路径的共同产出。"
  }
]
```

## 关系

```json
[
  {
    "from": "top_down",
    "to": "business_arch",
    "type": "flow",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Top-Down",
    "label_zh": "自上而下",
    "description_zh": "绿色粗箭头向下，沿中间架构列左侧贯穿；表示从业务用途逐层下探。"
  },
  {
    "from": "bottom_up",
    "to": "technology_arch",
    "type": "flow",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Bottom-Up",
    "label_zh": "自下而上",
    "description_zh": "紫色粗箭头向上，沿中间架构列右侧贯穿；表示从设备/基础设施逐层上升。"
  },
  {
    "from": "business_arch",
    "to": "application_arch",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "中栏自上而下的相邻关系，对应自上而下路径的顺序。"
  },
  {
    "from": "application_arch",
    "to": "technology_arch",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上。"
  },
  {
    "from": "top_down",
    "to": "outcome",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "方法产出底部汇合条中的模式。"
  },
  {
    "from": "bottom_up",
    "to": "outcome",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_topdown",
    "kind": "sequence",
    "name_zh": "自上而下路径",
    "steps": [
      "top_down",
      "business_arch",
      "application_arch",
      "technology_arch",
      "outcome"
    ],
    "description_zh": "从业务用途出发，逐层下探到技术层，最终沉淀模式。"
  },
  {
    "id": "f_bottomup",
    "kind": "sequence",
    "name_zh": "自下而上路径",
    "steps": [
      "bottom_up",
      "technology_arch",
      "application_arch",
      "business_arch",
      "outcome"
    ],
    "description_zh": "从设备/基础设施出发，逐层上升到业务用途，最终沉淀模式。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色虚线圆角框 + 绿色文字",
    "meaning_zh": "自上而下、基于业务用途的方法",
    "explicit": false
  },
  {
    "symbol": "紫色虚线圆角框 + 紫色文字",
    "meaning_zh": "自下而上、基于基础设施的方法",
    "explicit": false
  },
  {
    "symbol": "绿色粗箭头（向下）",
    "meaning_zh": "自上而下的下探方向",
    "explicit": false
  },
  {
    "symbol": "紫色粗箭头（向上）",
    "meaning_zh": "自下而上的上升方向",
    "explicit": false
  },
  {
    "symbol": "底部横向浅灰条",
    "meaning_zh": "两条路径的共同产出：数字放弃/优化模式",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "左、中、右三栏：左栏绿色虚线框（方法 + 3 条要点），中栏三个上下排列的实线架构框，右栏紫色虚线框（方法 + 3 条要点）；中栏左右各一条粗方向箭头（左绿向下、右紫向上），底部一条横贯全宽的浅灰汇合条。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-4",
    "relation": "follows",
    "note_zh": "图 3-4 先给出业务流程/应用与数据/技术基础设施的对象分层，本图在此分层上给出两种切入点"
  },
  {
    "target": "G242/fig3-7",
    "relation": "precedes",
    "note_zh": "识别出的放弃/优化模式进一步落实为图 3-7 的四类约束"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "两条粗箭头未与具体框端点相接，起止点按其在架构列两侧的上下方向与语义判定。",
    "底部汇合条与上方两方法之间没有画线，产出关系按版式推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 48 页原图截图（1519×787）",
    "英文 PDF 第 48–49 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 730–767 行",
    "figs/zh/g242_fig3-5_zh.svg 源码",
    "figs/zh/g242_fig3-5_zh.png"
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
