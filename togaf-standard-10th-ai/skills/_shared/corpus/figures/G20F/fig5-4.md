# G20F/fig5-4 · 架构支撑产品与冲刺待办列表定义

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig5-4.md) · [JSON](../../architecture/diagrams/G20F/fig5-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 44 页

![英文原图](../assets/G20F/fig5-4-p0044.png)

PDF 坐标：`[48.2, 138.9, 563.8, 423.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Architecture Supports Product and Sprint Backlog Definition
A Sprint — Architecture Iteration
High Priority Items
Should Deliver:
Envision — Strategic Planning
Features
Roadmap — Intentional Architecture
Requirements
Enhancements
Daily
Bugs Correction (Technical
Debt)
Initial Strategic
Scrum
Planning
Product/Solution Knowledge
Architecture Vision
Interdependencies
Two
Input to Conform the
Initial Modeling
Requirements
Weeks
Acc,
Product Backlog
Definition
Support for the User Stories
Definition (Sprint Backlog)
Potentially
Product
Sprint
Shippable
Backlog
Backlog
Sprint
Product
Delivery
——,
High Business Value
Release 1
Key Features
i
Further Priorities-
Release 2
Based Product
Operation
Roadmap
Maintenance
Release n
—~ 4
Less Important
Management
an
Features — Additional,
4
Optional
```

## 概要（历史解释；局部修正见上）

架构在冲刺中交付什么、如何把产品待办切成冲刺待办，以及交付后新需求如何回流。

## 目的（历史解释；局部修正见上）

说明架构工作在敏捷交付中的位置：架构迭代（冲刺）本身要交付特性、需求、增强、技术债修复等；架构规格为产品待办与冲刺待办提供输入与约束（有意架构），并接受运营反馈与新需求，形成持续治理闭环。

## 阅读顺序（历史解释；局部修正见上）

从左上青色框读“一个冲刺（架构迭代）应交付什么”，共 8 项。再到中部：上方是 High Priority Items 与 Envision/Roadmap 两句，左侧“Initial Strategic Planning / Architecture Vision / Initial Modeling / Requirements Definition”是架构侧输入；中间两条条纹柱分别是 Product Backlog 与 Sprint Backlog，一个深色弯箭头把产品待办顶部（高优先级）拉进冲刺待办。右侧是冲刺循环（Two Weeks，附 Daily Scrum），粗箭头 Sprint → Potentially Shippable Product → Delivery → Operation Maintenance Management。底部左是发布堆叠（Release 1/2/n 与三段价值说明），底部中是“New Requirements Change Management Continuous Governance”，一条长曲线从右侧运营区向左回流，并向上弯入 Sprint Backlog。右上橙框是总原则：有意架构与涌现架构相协调。

## 关键含义（历史解释；局部修正见上）

- 架构迭代（冲刺）不只是写文档：应交付特性、需求、增强、缺陷修复（技术债）、产品/解决方案知识、相互依赖、对产品待办的输入、对用户故事定义（冲刺待办）的支持。
- 架构通过“对产品待办的输入”和“对冲刺待办的支持”两种方式进入敏捷交付，而不是另起一套流程。
- 产品待办是分层的：顶部为高优先级条目（深色），一个弯箭头只把顶部若干条拉入冲刺待办；冲刺待办里同样用深色块表示本轮选中的条目。
- 右上“Intentional Architecture Reconciled with Emergent Architecture”是全图的原则：有意的、事先规划的架构必须与团队在实践中涌现的架构相协调。
- 交付节奏：两周一个冲刺、每日 Scrum；冲刺产出潜在可交付产品，经 Delivery 进入 Operation Maintenance Management。
- 发布按价值分层：高业务价值的关键特性在 Release 1，其次进入“进一步基于优先级的产品路线图”，最不重要的附加/可选特性排在 Release 2…n。
- 闭环：运营与维护产生的新需求经“变革管理/持续治理”回流，一部分进入冲刺待办、一部分回到发布路线图，因此架构与待办会持续演进。

## 层级（历史解释；局部修正见上）

版式分四大块：左上“冲刺交付清单”框（8 项并列）、中部待办与迭代（Product Backlog → Sprint Backlog → 冲刺循环）、右侧交付与运维链、底部发布路线图与回流。元素之间没有嵌套层级，只有流程先后与反馈。

## 线条含义（历史解释；局部修正见上）

深色细弯箭头：从产品待办顶部指向冲刺待办，表示按优先级抽取本轮条目。蓝色环形箭头 + “Two Weeks”：冲刺的时间盒循环；小环“Daily Scrum”：每日站会。蓝色粗长箭头（标 Sprint）：冲刺推进方向，末端指向 Potentially Shippable Product。向下细箭头：交付后进入运营/维护/管理。青色长曲线（向左，末端分叉）：新需求回流，一支向上进冲刺待办、一支向左回到路线图。左侧四条短箭头：把 Release 1/2/n 标签指向发布堆叠的对应层。花括号：把堆叠层分组成高价值/其次/可选三段。

## 易误读点（历史解释；局部修正见上）

- 不要以为架构只产出文档：左上清单明确把“对产品待办的输入”“对冲刺待办的支持”列为架构迭代的交付物。
- 不要把产品待办整列都当成下一冲刺的内容：弯箭头只从顶部取高优先级条目。
- 不要漏掉右上橙框：它是本图的原则句（有意架构与涌现架构相协调），不是装饰。
- 不要把回流曲线读成单向：它同时回到冲刺待办与发布路线图，说明变更管理贯穿两者。
- 中文稿引用的 figs/zh/g20fe_fig5-4_zh.svg 基本可用但少画了回流到冲刺待办的支线；同目录下的 g20fe_fig5-4_zh.png 文字严重重叠，不可使用。

## 元素

```json
[
  {
    "id": "fig_title",
    "label_en": "Architecture Supports Product and Sprint Backlog Definition",
    "label_zh": "架构支撑产品与冲刺待办列表定义",
    "type": "note",
    "parent": null,
    "position": "图顶部标题"
  },
  {
    "id": "box_sprint_deliver",
    "label_en": "A Sprint – Architecture Iteration Should Deliver:",
    "label_zh": "一个冲刺——架构迭代应交付：",
    "type": "group",
    "parent": null,
    "position": "左上青色大框"
  },
  {
    "id": "d_features",
    "label_en": "Features",
    "label_zh": "特性",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 1
  },
  {
    "id": "d_requirements",
    "label_en": "Requirements",
    "label_zh": "需求",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 2
  },
  {
    "id": "d_enhancements",
    "label_en": "Enhancements",
    "label_zh": "增强",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 3
  },
  {
    "id": "d_bugs",
    "label_en": "Bugs Correction (Technical Debt)",
    "label_zh": "缺陷修复（技术债务）",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 4
  },
  {
    "id": "d_knowledge",
    "label_en": "Product/Solution Knowledge",
    "label_zh": "产品/解决方案知识",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 5
  },
  {
    "id": "d_interdependencies",
    "label_en": "Interdependencies",
    "label_zh": "相互依赖",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 6
  },
  {
    "id": "d_input_backlog",
    "label_en": "Input to Conform the Product Backlog",
    "label_zh": "对产品待办列表的输入",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 7
  },
  {
    "id": "d_user_stories",
    "label_en": "Support for the User Stories Definition (Sprint Backlog)",
    "label_zh": "对用户故事定义（冲刺待办列表）的支持",
    "type": "artifact",
    "parent": "box_sprint_deliver",
    "order": 8
  },
  {
    "id": "high_priority",
    "label_en": "High Priority Items",
    "label_zh": "高优先级事项",
    "type": "note",
    "parent": null,
    "position": "中部上方"
  },
  {
    "id": "envision",
    "label_en": "Envision – Strategic Planning",
    "label_zh": "构想——战略规划",
    "type": "note",
    "parent": null,
    "position": "高优先级事项下方第一行"
  },
  {
    "id": "roadmap_intent",
    "label_en": "Roadmap – Intentional Architecture",
    "label_zh": "路线图——有意架构",
    "type": "note",
    "parent": null,
    "position": "高优先级事项下方第二行"
  },
  {
    "id": "initial_planning",
    "label_en": "Initial Strategic Planning",
    "label_zh": "初始战略规划",
    "type": "process",
    "parent": null,
    "position": "待办柱左侧文字（第 1 行）"
  },
  {
    "id": "arch_vision",
    "label_en": "Architecture Vision",
    "label_zh": "架构愿景",
    "type": "artifact",
    "parent": null,
    "position": "待办柱左侧文字（第 2 行）"
  },
  {
    "id": "initial_modeling",
    "label_en": "Initial Modeling",
    "label_zh": "初始建模",
    "type": "process",
    "parent": null,
    "position": "待办柱左侧文字（第 3 行）"
  },
  {
    "id": "requirements_def",
    "label_en": "Requirements Definition",
    "label_zh": "需求定义",
    "type": "process",
    "parent": null,
    "position": "待办柱左侧文字（第 4 行）"
  },
  {
    "id": "product_backlog",
    "label_en": "Product Backlog",
    "label_zh": "产品待办列表",
    "type": "artifact",
    "parent": null,
    "position": "中部左侧条纹柱（9 段，顶部一段深色）"
  },
  {
    "id": "sprint_backlog",
    "label_en": "Sprint Backlog",
    "label_zh": "冲刺待办列表",
    "type": "artifact",
    "parent": null,
    "position": "中部右侧条纹柱（4 段，全为深色）"
  },
  {
    "id": "intentional_box",
    "label_en": "Intentional Architecture Reconciled with Emergent Architecture",
    "label_zh": "有意架构与涌现架构相协调",
    "type": "note",
    "parent": null,
    "position": "右上橙色框"
  },
  {
    "id": "sprint_loop",
    "label_en": "Two Weeks",
    "label_zh": "两周",
    "type": "time",
    "parent": null,
    "position": "右侧大环形箭头中心"
  },
  {
    "id": "daily_scrum",
    "label_en": "Daily Scrum",
    "label_zh": "每日 Scrum",
    "type": "event",
    "parent": null,
    "position": "大环右上方小环形箭头"
  },
  {
    "id": "sprint_arrow",
    "label_en": "Sprint",
    "label_zh": "冲刺",
    "type": "process",
    "parent": null,
    "position": "右侧粗长水平箭头"
  },
  {
    "id": "delivery",
    "label_en": "Delivery",
    "label_zh": "交付",
    "type": "note",
    "parent": null,
    "position": "冲刺箭头下方"
  },
  {
    "id": "psp",
    "label_en": "Potentially Shippable Product",
    "label_zh": "潜在可交付产品",
    "type": "product",
    "parent": null,
    "position": "右侧，配轮船图标"
  },
  {
    "id": "operation",
    "label_en": "Operation Maintenance Management",
    "label_zh": "运营/维护/管理",
    "type": "process",
    "parent": null,
    "position": "右下"
  },
  {
    "id": "new_req",
    "label_en": "New Requirements Change Management Continuous Governance",
    "label_zh": "新需求 / 变革管理 / 持续治理",
    "type": "process",
    "parent": null,
    "position": "底部中央橙色框"
  },
  {
    "id": "release_stack",
    "label_en": null,
    "label_zh": "发布堆叠（立体层）",
    "type": "group",
    "parent": null,
    "position": "左下"
  },
  {
    "id": "layer_1",
    "label_en": null,
    "label_zh": "第一层（橙色，最高价值）",
    "type": "artifact",
    "parent": "release_stack",
    "order": 1
  },
  {
    "id": "layer_2",
    "label_en": null,
    "label_zh": "第二层（蓝色）",
    "type": "artifact",
    "parent": "release_stack",
    "order": 2
  },
  {
    "id": "layer_3",
    "label_en": null,
    "label_zh": "第三层（深灰）",
    "type": "artifact",
    "parent": "release_stack",
    "order": 3
  },
  {
    "id": "layer_4",
    "label_en": null,
    "label_zh": "第四层（浅色淡出）",
    "type": "artifact",
    "parent": "release_stack",
    "order": 4
  },
  {
    "id": "release_1",
    "label_en": "Release 1",
    "label_zh": "发布 1",
    "type": "artifact",
    "parent": null,
    "position": "堆叠左侧标注 1"
  },
  {
    "id": "release_2",
    "label_en": "Release 2",
    "label_zh": "发布 2",
    "type": "artifact",
    "parent": null,
    "position": "堆叠左侧标注 2"
  },
  {
    "id": "release_n",
    "label_en": "Release n",
    "label_zh": "发布 n",
    "type": "artifact",
    "parent": null,
    "position": "堆叠左侧标注 3"
  },
  {
    "id": "arrow_unlabeled",
    "label_en": null,
    "label_zh": "无标签箭头（指向第一层）",
    "type": "other",
    "parent": null,
    "position": "堆叠最左侧最上方箭头"
  },
  {
    "id": "brace_high",
    "label_en": "High Business Value Key Features",
    "label_zh": "高业务价值关键特性",
    "type": "note",
    "parent": null,
    "position": "花括号第 1 段"
  },
  {
    "id": "brace_roadmap",
    "label_en": "Further Priorities-Based Product Roadmap",
    "label_zh": "进一步基于优先级的产品路线图",
    "type": "note",
    "parent": null,
    "position": "花括号第 2 段"
  },
  {
    "id": "brace_optional",
    "label_en": "Less Important Features – Additional, Optional",
    "label_zh": "次要特性——附加、可选",
    "type": "note",
    "parent": null,
    "position": "花括号第 3 段"
  }
]
```

## 关系

```json
[
  {
    "from": "product_backlog",
    "to": "sprint_backlog",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "深色弯箭头：把产品待办顶部的高优先级条目拉入冲刺待办"
  },
  {
    "from": "high_priority",
    "to": "product_backlog",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "文字位于待办柱正上方，指示待办顶部的深色段为高优先级"
  },
  {
    "from": "sprint_arrow",
    "to": "psp",
    "type": "flow",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "蓝色粗长箭头，冲刺指向潜在可交付产品"
  },
  {
    "from": "psp",
    "to": "operation",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向下细箭头：交付后进入运营/维护/管理"
  },
  {
    "from": "sprint_loop",
    "to": "sprint_arrow",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "环形箭头绕“两周”一圈，表示冲刺的时间盒循环"
  },
  {
    "from": "daily_scrum",
    "to": "sprint_loop",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "小环形箭头，表示冲刺内每日站会的循环"
  },
  {
    "from": "operation",
    "to": "new_req",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "青色长曲线自运营/维护一侧向左引出，经过新需求/变革管理框"
  },
  {
    "from": "new_req",
    "to": "sprint_backlog",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "曲线的一支向上弯入冲刺待办列表底部"
  },
  {
    "from": "new_req",
    "to": "brace_roadmap",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "曲线的另一支以左向箭头结束，回到发布路线图一侧（端点未接触具体元素）"
  },
  {
    "from": "release_1",
    "to": "layer_2",
    "type": "assignment",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "短箭头指向堆叠第二层（标签位于箭头上方，层与标签的对应按行高判断）"
  },
  {
    "from": "release_2",
    "to": "layer_3",
    "type": "assignment",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "release_n",
    "to": "layer_4",
    "type": "assignment",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "arrow_unlabeled",
    "to": "layer_1",
    "type": "assignment",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "最上方箭头无文字，指向橙色顶层"
  },
  {
    "from": "brace_high",
    "to": "layer_1",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "花括号第 1 段括住顶层"
  },
  {
    "from": "brace_roadmap",
    "to": "layer_2",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "brace_optional",
    "to": "layer_3",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "花括号第 3 段覆盖下方两层（附加、可选）"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_sprint",
    "kind": "sequence",
    "name_zh": "产品待办→冲刺待办→冲刺→可交付产品→运营",
    "steps": [
      "product_backlog",
      "sprint_backlog",
      "sprint_arrow",
      "psp",
      "operation"
    ]
  },
  {
    "id": "f_feedback",
    "kind": "loop",
    "name_zh": "新需求回流",
    "steps": [
      "operation",
      "new_req",
      "sprint_backlog",
      "sprint_arrow",
      "psp",
      "operation"
    ],
    "loop_type": "reinforcing",
    "description_zh": "运营中发现的新需求经变革管理回到待办，形成持续演进闭环。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "青色圆角大框",
    "meaning_zh": "一个冲刺（架构迭代）应交付的内容清单",
    "explicit": false
  },
  {
    "symbol": "条纹横线柱",
    "meaning_zh": "待办列表（Product Backlog / Sprint Backlog）",
    "explicit": false
  },
  {
    "symbol": "深色填充条目",
    "meaning_zh": "高优先级、已选入下一层的条目",
    "explicit": false
  },
  {
    "symbol": "蓝色环形箭头",
    "meaning_zh": "冲刺时间盒循环（Two Weeks）/ 每日站会（Daily Scrum）",
    "explicit": false
  },
  {
    "symbol": "青色长曲线箭头",
    "meaning_zh": "新需求回流（进冲刺待办 / 回发布路线图）",
    "explicit": false
  },
  {
    "symbol": "立体堆叠层 + 花括号",
    "meaning_zh": "按价值与优先级分层的发布内容（Release 1/2/n）",
    "explicit": false
  },
  {
    "symbol": "橙色矩形框",
    "meaning_zh": "原则/说明框（有意架构与涌现架构相协调；新需求变革管理持续治理）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "左上大青色圆角框（清单）；中部两列条纹待办柱与文字说明；右上橙色原则框；右侧冲刺循环与交付链；底部左侧立体发布堆叠与花括号说明，底部中间橙色“新需求/变革管理/持续治理”框，一条长曲线把这些底部元素与中部的待办连起来。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig5-2",
    "relation": "related",
    "note_zh": "图 5-2 说明五类架构活动并行推进；本图具体展示“部署目标”阶段之后待办与冲刺如何运转。"
  },
  {
    "target": "G20F/fig4-4",
    "relation": "complements",
    "note_zh": "图 4-4 从层级角度给出三层待办，本图从单条产品/冲刺待办的角度展示架构输入与回流。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四层发布堆叠与 Release 1/2/n 三个标签的对应关系存在歧义：标签位于箭头上方，按行高判断为“无标签箭头→橙色顶层，Release 1→蓝层，Release 2→深灰层，Release n→浅色层”，但也可读成标签标注其上方箭头。",
    "回流曲线在图中穿过“新需求/变革管理/持续治理”框附近，未与框线相接；把它归因于该框是依据位置与正文的判断。",
    "产品待办为 9 段、冲刺待办为 4 段，按条纹计数，仅示意优先级切分。"
  ],
  "analyzed_from": [
    "英文 PDF 第 44 页原图截图（figctx GT crop + 400dpi 与 600dpi 局部）",
    "英文 PDF 第 43–44 页 5.3.1–5.3.3 正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 600–631 行",
    "figs/g20fe_fig5-4_en.png、figs/zh/g20fe_fig5-4_zh.png 与 figs/zh/g20fe_fig5-4_zh.svg"
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
