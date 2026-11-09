# G242/fig3-4 · 架构层与碳排放

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-4.md) · [JSON](../../architecture/diagrams/G242/fig3-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 47 页

![英文原图](../assets/G242/fig3-4-p0047.png)

PDF 坐标：`[99.8, 123.1, 512.2, 431.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
wb ot
Business
Applications and Data
Technical Infrastructures
Processes
ICT System
```

## 概要（历史解释；局部修正见上）

ICT 系统由业务流程、应用与数据、技术基础设施三层构成，碳排放随技术基础设施穿出系统边界。

## 目的（历史解释；局部修正见上）

用一张极简的系统边界图说明：企业 ICT 系统的碳足迹来自技术基础设施（设备、服务器、存储、网络、终端及其建造、运行与报废），而技术基础设施只是为业务流程存储/传输/处理数据、运行应用而存在。它把“架构层”与“碳排放来源”绑定，为随后“在多个层面调整设计”的架构杠杆讨论建立对象模型。

## 阅读顺序（历史解释；局部修正见上）

先看最外框“ICT System”，它划定核算边界。框内从左到右三个竖框：带人物插画的 Business Processes、Applications and Data、Technical Infrastructures；相邻框之间是粗双向箭头，表示相互调用/支撑。最右侧技术基础设施上方冲出边界的粗黑箭头标着 CO2，表示排放从这一层产生并离开系统。三个圆形编号 1/2/3 与正文三条编号说明一一对应。

## 关键含义（历史解释；局部修正见上）

- ICT 系统的边界内包含业务流程、应用与数据、技术基础设施三部分，三者不是并列的“架构域”，而是同一系统的三个层面。
- 碳排放箭头只从技术基础设施发出并穿出 ICT System 边界：按正文，碳足迹由设备组件、服务器、存储、网络控制器、屏幕、固定/移动设备及运行它们的技术软件构成。
- 双向粗箭头表示业务流程与应用/数据、应用/数据与技术基础设施之间相互依赖：流程产生信息需求，应用自动化流程；应用调用技术资源。
- 编号 1 对应技术基础设施的碳足迹（含建造、安装、维护、报废，含境外制造排放，含云与分包商），编号 2 说明基础设施只为存储/传输/处理数据或运行应用而存在，编号 3 说明业务流程受控地使用口头/书面/数字信息。
- 图中没有画出“业务流程直接排放”，但正文的核算范围仍以技术基础设施的碳足迹为对象；这提示减排杠杆最终要落到技术层，但调整的起点可以是业务流程与用途。
- 图形是理解后文“自上而下（用途）与自下而上（基础设施）”双视角的共同底图：左端是用途，右端是基础设施。

## 层级（历史解释；局部修正见上）

两层：最外层“ICT System”是系统边界容器；其内三个竖框（Business Processes、Applications and Data、Technical Infrastructures）为并列的组成层，从左到右排列，彼此无父子关系。编号圆点附在对应框上，CO2 箭头附在技术基础设施上并穿出外框。

## 线条含义（历史解释；局部修正见上）

两条粗双向箭头（业务流程↔应用与数据、应用与数据↔技术基础设施）表示相邻层之间的相互依赖与调用，不是单向数据流；向上粗箭头表示 CO2 排放离开系统边界，方向由技术基础设施指向外部。外框实线只表示系统边界，不表示连接。

## 易误读点（历史解释；局部修正见上）

- 不要把三个竖框读成先后阶段或三个独立系统；它们是同一 ICT 系统的三个层面。
- 双向箭头不是“数据双向流动”的技术细节，而是层间相互依赖的抽象表示。
- CO2 箭头画在技术基础设施上方，不等于只有运行用电产生排放；正文明确还包括建造、安装、维护、报废以及境外制造。
- 编号 1/2/3 不是阅读顺序，而是与正文三条解释对应的编号；1 在最右、3 在最左。
- 中文稿当前引用的 figs/g242_fig3-4.svg 是自拟的四层“架构杠杆”清单，增加了原图没有的数据架构层，并丢失 CO2 箭头与系统边界，不能据它理解本图。

## 元素

```json
[
  {
    "id": "ict_system",
    "label_en": "ICT System",
    "label_zh": "ICT 系统",
    "type": "group",
    "parent": null,
    "position": "最外层大矩形",
    "description_zh": "系统边界容器。"
  },
  {
    "id": "business_processes",
    "label_en": "Business Processes",
    "label_zh": "业务流程",
    "type": "process",
    "parent": "ict_system",
    "level": 2,
    "position": "左侧竖框",
    "description_zh": "带人物在工位前的剪影插画。"
  },
  {
    "id": "applications_data",
    "label_en": "Applications and Data",
    "label_zh": "应用与数据",
    "type": "application",
    "parent": "ict_system",
    "level": 2,
    "position": "中间竖框",
    "description_zh": "原图把应用与数据合为一个框。"
  },
  {
    "id": "technical_infrastructures",
    "label_en": "Technical Infrastructures",
    "label_zh": "技术基础设施",
    "type": "technology",
    "parent": "ict_system",
    "level": 2,
    "position": "右侧竖框",
    "description_zh": "设备、服务器、存储、网络、终端及技术软件。"
  },
  {
    "id": "badge_3",
    "label_en": "3",
    "label_zh": "3",
    "type": "note",
    "parent": "business_processes",
    "position": "业务流程框内中部",
    "description_zh": "对应正文第 3 条说明。"
  },
  {
    "id": "badge_2",
    "label_en": "2",
    "label_zh": "2",
    "type": "note",
    "parent": "applications_data",
    "position": "应用与数据框内中部",
    "description_zh": "对应正文第 2 条说明。"
  },
  {
    "id": "badge_1",
    "label_en": "1",
    "label_zh": "1",
    "type": "note",
    "parent": "technical_infrastructures",
    "position": "技术基础设施框内中部",
    "description_zh": "对应正文第 1 条说明。"
  },
  {
    "id": "co2_arrow",
    "label_en": "CO2",
    "label_zh": "CO2（二氧化碳）",
    "type": "other",
    "parent": "technical_infrastructures",
    "position": "技术基础设施上方，穿出 ICT System 边界",
    "description_zh": "粗黑向上箭头，表示碳排放离开系统边界。"
  }
]
```

## 关系

```json
[
  {
    "from": "business_processes",
    "to": "applications_data",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "粗双向箭头，表示业务流程与应用/数据相互依赖。"
  },
  {
    "from": "applications_data",
    "to": "technical_infrastructures",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "粗双向箭头，表示应用/数据与技术基础设施相互依赖。"
  },
  {
    "from": "technical_infrastructures",
    "to": "co2_arrow",
    "type": "produces",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "CO2",
    "label_zh": "CO2（二氧化碳）",
    "description_zh": "向上粗箭头，表示排放由技术基础设施产生并离开系统。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "外层实线矩形 + “ICT System”",
    "meaning_zh": "企业 ICT 系统的核算边界",
    "explicit": false
  },
  {
    "symbol": "粗双向箭头",
    "meaning_zh": "相邻层之间的相互依赖/调用",
    "explicit": false
  },
  {
    "symbol": "粗黑向上箭头 + CO2",
    "meaning_zh": "从技术基础设施产生并离开系统边界的碳排放",
    "explicit": false
  },
  {
    "symbol": "圆形编号 1/2/3",
    "meaning_zh": "与正文三条编号解释对应的注释标记",
    "explicit": false
  },
  {
    "symbol": "人物与工位剪影",
    "meaning_zh": "业务流程由人在工位上执行",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "横向三层：左侧人物在工位前（业务流程），中间空白竖框（应用与数据），右侧空白竖框（技术基础设施）；三者由两条粗双向箭头串联，全部包在“ICT System”外框内；技术基础设施上方有粗黑向上箭头标 CO2 穿出外框；圆形编号 3/2/1 分别在三个框内。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-1",
    "relation": "detail_of",
    "note_zh": "本图展开图 3-1 中“架构并构建可持续信息系统”功能的对象层与排放来源"
  },
  {
    "target": "G242/fig3-5",
    "relation": "precedes",
    "note_zh": "在分清业务用途层与技术基础设施层之后，图 3-5 才给出自上而下/自下而上两种切入点"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "三个竖框内除标题外没有其他文字，编号与正文条目的对应关系按数字顺序确认。",
    "两条粗箭头是否严格表示双向依赖，还是表示“之间的接口”，图中无图例；按双向箭头直观含义记录。"
  ],
  "analyzed_from": [
    "英文 PDF 第 47 页原图截图（1265×956）",
    "英文 PDF 第 47 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 712–724 行",
    "figs/g242_fig3-4.svg 源码"
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
