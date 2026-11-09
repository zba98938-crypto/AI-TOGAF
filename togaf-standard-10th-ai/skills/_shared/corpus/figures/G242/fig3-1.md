# G242/fig3-1 · 数字可持续性参考模型（高层版）——信息系统“健身计划”

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-1.md) · [JSON](../../architecture/diagrams/G242/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 31 页

![英文原图](../assets/G242/fig3-1-p0031.png)

PDF 坐标：`[74.0, 186.2, 538.0, 378.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Deploying a Sustainable Information System Policy
Developing and Rolling Out a Sustainable Information System Strategy
:
3° The Motivation
Engaging with Customers
Architecting and Building a Sustainable information System
Measuring tho
Providers, Partners,
Environmental Impact of
and Authorities Towards
The Sport Room
the Information System
Sustainable Solutions and
rom Cradle to Grave
Services
‘Operating a Sustainable Information System
eas
Developing a Sustainable Digital Culture
ey)
The Good
The Weighing
Relationships
jaa The State of Being
Governing the Transition Towards a Sustainable Digital Culture
fiz =) The Coach
```

## 概要（历史解释；局部修正见上）

用“健身计划”比喻，给出部署可持续信息系统政策所需的七个高层业务功能。

## 目的（历史解释；局部修正见上）

为“如何部署可持续信息系统政策”提供一张高层参考模型：把散落的可持续 ICT 活动归并为七个业务功能，并用健身房比喻降低理解门槛。它既是分类框架（可用来盘点已开展活动、评估成熟度与改进点），也是后文 3.3–3.9 各节的目录。

## 阅读顺序（历史解释；局部修正见上）

先看最外层的米色容器标题“Deploying a Sustainable Information System Policy”，它框定整个计划。容器内自上而下分三层：顶部横带是战略，中部左/中/右三栏分别是互动、建设运营与文化、度量，底部横带是治理。每个黄色块右上角的小折角图标表示它是 ArchiMate 业务功能；灰色斜体字（The Motivation 等）是健身比喻，不是功能名。图中没有箭头，位置只表达分组，不表达先后。

## 关键含义（历史解释；局部修正见上）

- 七个功能是：制定并推展可持续信息系统战略、与客户/供应商/伙伴/主管部门互动、架构并构建、运营、发展可持续数字文化、从摇篮到坟墓度量影响、治理转型。
- 战略位于顶部并横贯全宽，治理位于底部并横贯全宽，二者夹住中间的五个执行性功能，暗示战略统领、治理兜底。
- 中间一栏把“架构并构建”“运营”“发展文化”上下叠放；文化与建设运营同属日常能力，而不是一次性项目。
- 左侧是对外互动（客户、供应商、伙伴、主管部门），右侧是度量（从摇篮到坟墓的环境影响），形成“向外协作 + 向内量化”的两翼。
- 健身比喻逐块对应：战略=动机（The Motivation）、互动=良好关系、架构=健身房（The Sport Room）、文化=存在状态、度量=称重（The Weighing）、治理=教练（The Coach）。
- 正文强调七项活动对所有组织通用，可降低 ICT 环境足迹并影响 IT 市场走向可持续；该模型应适配各组织语境，并可用于成熟度与横向对标。
- 文化被正文明确为其他活动成功的前提：高管与员工先有认知与承诺，计划才可能被执行。

## 层级（历史解释；局部修正见上）

三层视觉层级：最外层是“Deploying a Sustainable Information System Policy”容器；其内是七个业务功能块；每个功能块内再嵌一个比喻标签与图标（如战略块内的 The Motivation）。七个功能彼此平级，没有上下级；中央一栏的三个块只是纵向排列，不构成父子关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。功能块之间的从属只由外层容器表达；战略/治理横贯全宽、其余分栏，属于版式暗示的“统领/兜底”关系，不是画出的流程。右上角的折角小图标是 ArchiMate 业务功能记法，不是导航箭头。

## 易误读点（历史解释；局部修正见上）

- 这不是流程图：七个功能没有先后顺序，不能按从上到下当作实施步骤。
- 灰色斜体 The Motivation、The Sport Room 等是健身比喻，不是第七个功能或子功能。
- “治理转型”不是最后一步，而是贯穿全过程的兜底功能；它在底部横贯全宽正是这个意思。
- 中文稿当前引用的 figs/g242_fig3-1.svg 是自拟的 7 框清单，丢了外层容器、空间结构与全部比喻，还把治理降为普通第 7 项；不能据它理解原图。
- 七个功能不是 TOGAF ADM 阶段，而是可持续 ICT 政策的业务能力清单。

## 元素

```json
[
  {
    "id": "policy_program",
    "label_en": "Deploying a Sustainable Information System Policy",
    "label_zh": "部署可持续信息系统政策",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "最外层米色容器",
    "description_zh": "七个业务功能的总容器；右上角另有一个小的 ArchiMate 分组图标。"
  },
  {
    "id": "fn_strategy",
    "label_en": "Developing and Rolling Out a Sustainable Information System Strategy",
    "label_zh": "制定并推展可持续信息系统战略",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 1,
    "position": "容器顶部，横贯全宽",
    "description_zh": "对应正文 3.4 节。"
  },
  {
    "id": "an_motivation",
    "label_en": "The Motivation",
    "label_zh": "动机",
    "type": "note",
    "parent": "fn_strategy",
    "level": 3,
    "position": "战略块右下",
    "description_zh": "健身比喻；配一只手托举齿轮/火花的图标。"
  },
  {
    "id": "fn_engage",
    "label_en": "Engaging with Customers Providers, Partners, and Authorities Towards Sustainable Solutions and Services",
    "label_zh": "与客户、供应商、伙伴及主管部门互动，共同走向可持续的解决方案与服务",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 2,
    "position": "中部左栏",
    "description_zh": "对外互动功能。"
  },
  {
    "id": "an_relationships",
    "label_en": "The Good Relationships",
    "label_zh": "良好关系",
    "type": "note",
    "parent": "fn_engage",
    "level": 3,
    "position": "互动块下部",
    "description_zh": "健身比喻；配三个人物图标。"
  },
  {
    "id": "fn_architect",
    "label_en": "Architecting and Building a Sustainable Information System",
    "label_zh": "架构并构建可持续信息系统",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 3,
    "position": "中部中栏最上",
    "description_zh": "对应正文 3.5 节。"
  },
  {
    "id": "an_sport_room",
    "label_en": "The Sport Room",
    "label_zh": "健身房",
    "type": "note",
    "parent": "fn_architect",
    "level": 3,
    "position": "架构块中部",
    "description_zh": "健身比喻；配哑铃图标。"
  },
  {
    "id": "fn_operate",
    "label_en": "Operating a Sustainable Information System",
    "label_zh": "运营可持续信息系统",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 4,
    "position": "中部中栏中间",
    "description_zh": "系统运行阶段的可持续功能。"
  },
  {
    "id": "fn_culture",
    "label_en": "Developing a Sustainable Digital Culture",
    "label_zh": "发展可持续数字文化",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 5,
    "position": "中部中栏最下",
    "description_zh": "对应正文 3.3 节；正文称其为其他活动的前提。"
  },
  {
    "id": "an_state_of_being",
    "label_en": "The State of Being",
    "label_zh": "存在状态",
    "type": "note",
    "parent": "fn_culture",
    "level": 3,
    "position": "文化块中部",
    "description_zh": "健身比喻；配日出下张开双臂的人像照片。"
  },
  {
    "id": "fn_measure",
    "label_en": "Measuring the Environmental Impact of the Information System from Cradle to Grave",
    "label_zh": "从摇篮到坟墓度量信息系统的环境影响",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 6,
    "position": "中部右栏",
    "description_zh": "对应正文 3.6 节。"
  },
  {
    "id": "an_weighing",
    "label_en": "The Weighing",
    "label_zh": "称重",
    "type": "note",
    "parent": "fn_measure",
    "level": 3,
    "position": "度量块下部",
    "description_zh": "健身比喻；配苹果与体重计图标。"
  },
  {
    "id": "fn_govern",
    "label_en": "Governing the Transition Towards a Sustainable Digital Culture",
    "label_zh": "治理向可持续数字文化的转型",
    "type": "function",
    "parent": "policy_program",
    "level": 2,
    "order": 7,
    "position": "容器底部，横贯全宽",
    "description_zh": "横贯全宽的治理功能；不是最后一步。"
  },
  {
    "id": "an_coach",
    "label_en": "The Coach",
    "label_zh": "教练",
    "type": "note",
    "parent": "fn_govern",
    "level": 3,
    "position": "治理块右侧",
    "description_zh": "健身比喻；配教练指导躺卧者的图标。"
  },
  {
    "id": "copyright",
    "label_en": "© The Open Group",
    "label_zh": "© The Open Group",
    "type": "note",
    "parent": "policy_program",
    "level": 3,
    "position": "容器左下角",
    "description_zh": "版权标注。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "米色外层容器",
    "meaning_zh": "部署可持续信息系统政策的整体计划（七个功能的总容器）",
    "explicit": false
  },
  {
    "symbol": "黄色圆角块 + 右上角折角图标",
    "meaning_zh": "一个 ArchiMate 业务功能（business function）",
    "explicit": false
  },
  {
    "symbol": "灰色斜体短语（The Motivation 等）",
    "meaning_zh": "健身比喻，帮助记忆该功能的作用",
    "explicit": false
  },
  {
    "symbol": "块内图标（手、人物、哑铃、日出、苹果、教练）",
    "meaning_zh": "与比喻配套的装饰性图标，不编码流程或强弱",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "外层米色圆角容器；顶部一条全宽战略带；中部三栏（左：互动；中：架构/运营/文化三块纵排；右：度量）；底部一条全宽治理带。七个黄色功能块右上角均有 ArchiMate 功能图标；每块内配一个灰色斜体比喻与图标。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-2",
    "relation": "overview_of",
    "note_zh": "图 3-2 展开本图“发展可持续数字文化”功能下的四个文化轴"
  },
  {
    "target": "G242/fig3-4",
    "relation": "related",
    "note_zh": "本图的“架构并构建”“运营”功能在图 3-4 中展开为架构层与碳排放关系"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "左侧功能名在图中因换行写作“Engaging with Customers Providers, Partners, and Authorities…”，Customers 后是否漏逗号无法从图判断；按可见文字照录。",
    "原图右上角的小 ArchiMate 分组图标与七个功能块的图标细节较模糊，仅能确认类型，未逐笔核对。"
  ],
  "analyzed_from": [
    "英文 PDF 第 31 页原图截图（1460×655）",
    "英文 PDF 第 31 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 390–399 行",
    "figs/g242_fig3-1.svg 源码"
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
