# G20F/fig4-4 · ADM 层级与敏捷交付概念的映射

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig4-4.md) · [JSON](../../architecture/diagrams/G20F/fig4-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G20F/fig4-4-p0028.png)

PDF 坐标：`[48.2, 127.6, 563.8, 417.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
he O
oop
TOGAF ADM - Levels
SAFe/Agile/Scrum Layers
Characteristic Agile Team Iterations
—=
SAFe ~ Strategic Themes —
Strategic
Enterprise Portfolio Delivery
Architecture
Planning
Business Team
Iteration
Direction-
Technical Team
tting at an
Operational Team
(Time-Boxed)
level
is
QS
So
<5)
Segment
Agile/SAF
Product/Portfolio Backlog ~
cece
Architecture
Change Plans - Epics
os
LS)
Organizing for
operational and
solution
3
change at a
Enterprise/Segment Portfolio - Epics
program or
ei
A
portfolio level
Capability
Agile/SAFe — Product/Solution Backlog ~
ull
Solution Team *;
‘Delivery
Delivery Team
Architecture
Capabilities to be Delivered
Iteration
H
Iteration
(Dev Ops)
Agile/SAFe - Produc/Program Backlog ~
Daily Stand-Up |
Daily Stand-Up
framework for
Organizing
Capability Increments (Features)
ar
change activity
Agile/SAF
Program Team Backlog ~
and roadmaps
Deliverable User Stories
i
realizing
ais
i
H
capability
increments
Scrum ~ Sprint Te
Backlog—
Solut
yn Runway,’
Agile Development
Deliverable Us
ries,
Continuous Inte;
ti
Deli
```

## 概要（历史解释；局部修正见上）

把战略、分段、能力三层架构逐行对照到 SAFe/Scrum 的待办层次与各自特征性的迭代方式。

## 目的（历史解释；局部修正见上）

4.5 节要回答“ADM 的层级与阶段如何落到敏捷交付概念上”。这张图把三个架构层（左列）、对应的 SAFe/Agile/Scrum 待办层次（中列）和典型团队迭代形态（右列）排成对照表，说明三层可以各自循环 A–G，但重点、待办粒度与迭代节奏不同。

## 阅读顺序（历史解释；局部修正见上）

横向按列读：左列是 TOGAF ADM 的三个层级及其定位，中列是该层级在 SAFe/敏捷/Scrum 中对应的待办层次，右列是特征性的团队迭代形态。纵向按行读：第一行战略层（与分段层共用同一个大的规划迭代框），第三行能力层拆成 Build Iteration 与 Delivery Iteration 两个并行框。左列的三个轮盘之间还有浅蓝虚线箭头，表示层级自上而下的驱动。

## 关键含义（历史解释；局部修正见上）

- 同一个 ADM 在三个层级重复：左列三个轮盘都含完整 A–H，说明每层都可循环经历全部阶段，只是重点不同。
- 战略层（第一行）重点是方向设定（Direction-setting at an executive level），对应 SAFe 的战略主题与企业组合交付，迭代是时间盒的规划迭代（Planning Iteration）。
- 分段层（第二行）重点是按项目群/组合组织运营与解决方案变更，对应 Product/Portfolio Backlog – Change Plans – Epics；它与战略层共用右上那个大的规划迭代框，说明两层共用企业/分段组合与 Epic 这一层待办。
- 能力层（第三行）重点是变更活动与路线图、实现能力增量，对应四条更细的待办：Product/Solution Backlog（Capabilities to be Delivered）、Product/Program Backlog（Capability Increments / Features）、Program Team Backlog（Deliverable User Stories）、Scrum Sprint Team Backlog（Deliverable User Stories）。
- 能力层内部还有 Build Iteration 与 Delivery Iteration 两条并行迭代线：前者由 Solution Team 做每日站会并维护 Solution Runway，后者由 Delivery Team (Dev Ops) 做每日站会并负责持续集成/交付。
- 团队构成随层级变化：规划迭代由 Business Team、Technical Team、Operational Team 混合组成（人形图标蓝橙相间），能力层则按 Solution Team / Delivery Team 分工。
- 正文补充：三层也可以由一个跨层集成团队在连贯冲刺中推进，具体编排取决于企业复杂度与敏捷实施方式，图只是“典型”形态。

## 层级（历史解释；局部修正见上）

两级结构：外层是三行（战略→分段→能力，自上而下详细程度递增）；每行内部是三列（ADM 层级 / 敏捷层 / 团队迭代）。左列三个 ADM 轮盘之间用虚线箭头自上而下连接，表示上层驱动下层。能力层内部再分为 Build 与 Delivery 两个并列迭代框。

## 线条含义（历史解释；局部修正见上）

浅蓝虚线箭头：从战略轮盘下方指向分段轮盘的 A、从分段轮盘指向能力轮盘的 A，表示层级间的向下驱动。蓝色/紫色/青色环形箭头：迭代循环（绕 ADM 轮盘一圈），表示该层在自己的待办上反复迭代。粗平箭头：把迭代产出向右推给团队/下一环节。橙色与紫色/青色虚线圆角框：把一组活动框成一个迭代单元（Planning / Build / Delivery）。蓝色大括号：把一行三列括在一起，强调“同一层级”。

## 易误读点（历史解释；局部修正见上）

- 不要把三行读成“先后三个阶段”：它们是三个并行存在的架构层级，可以同时进行。
- 不要以为战略层的规划迭代框只属于第一行：橙色虚线框横跨战略与分段两行，右下的“Enterprise/Segment Portfolio – Epics”同时服务这两层。
- 不要把 Build 与 Delivery 当作严格先后：图中两者并列，正文说它们由不同团队（Solution Team / Delivery Team）分别推进。
- 不要把人形图标当作精确人数统计，它只是表示跨职能混合团队。
- 中文稿引用的 figs/g20f_fig4-4.svg 只剩三张概括卡片，看不到三列对照、三层轮盘、两个能力层迭代框，不能据它理解本图。

## 元素

```json
[
  {
    "id": "hdr_adm",
    "label_en": "TOGAF ADM – Levels",
    "label_zh": "TOGAF ADM——层级",
    "type": "note",
    "parent": null,
    "position": "第一列表头"
  },
  {
    "id": "hdr_agile",
    "label_en": "SAFe/Agile/Scrum Layers",
    "label_zh": "SAFe/敏捷/Scrum 层",
    "type": "note",
    "parent": null,
    "position": "第二列表头"
  },
  {
    "id": "hdr_iter",
    "label_en": "Characteristic Agile Team Iterations",
    "label_zh": "特征性的敏捷团队迭代",
    "type": "note",
    "parent": null,
    "position": "第三列表头（右上角有 © The Open Group）"
  },
  {
    "id": "row_strategic",
    "label_en": null,
    "label_zh": "战略层（第一行）",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第一行"
  },
  {
    "id": "r1_level",
    "label_en": "Strategic Architecture",
    "label_zh": "战略架构",
    "type": "architecture",
    "parent": "row_strategic",
    "level": 1,
    "position": "第一行左列标题"
  },
  {
    "id": "r1_desc",
    "label_en": "Direction-setting at an executive level",
    "label_zh": "高管层级的定方向",
    "type": "note",
    "parent": "row_strategic",
    "position": "第一行左列第二段"
  },
  {
    "id": "r1_wheel",
    "label_en": null,
    "label_zh": "ADM 轮盘缩略图",
    "type": "architecture",
    "parent": "row_strategic",
    "position": "第一行左列",
    "description_zh": "与图 3-1 相同的 ADM 轮盘微缩图（Preliminary、A–H、Requirements Management）。"
  },
  {
    "id": "r1_safe",
    "label_en": "SAFe – Strategic Themes – Enterprise Portfolio Delivery",
    "label_zh": "SAFe——战略主题——企业组合交付",
    "type": "note",
    "parent": "row_strategic",
    "position": "第一行中列"
  },
  {
    "id": "frame_planning",
    "label_en": null,
    "label_zh": "规划迭代框（橙色虚线，横跨第一、二行）",
    "type": "group",
    "parent": null,
    "position": "第三列第一、二行"
  },
  {
    "id": "r1_iterbox",
    "label_en": "Planning Iteration (Time-Boxed)",
    "label_zh": "规划迭代（时间盒）",
    "type": "phase",
    "parent": "frame_planning",
    "position": "规划迭代框左上，青色字"
  },
  {
    "id": "r1_loop",
    "label_en": null,
    "label_zh": "蓝色环形迭代箭头",
    "type": "other",
    "parent": "frame_planning",
    "position": "规划迭代框中部",
    "description_zh": "绕 ADM 轮盘一圈的粗蓝箭头，表示迭代循环。"
  },
  {
    "id": "r1_wheel_loop",
    "label_en": null,
    "label_zh": "ADM 轮盘（环内）",
    "type": "architecture",
    "parent": "frame_planning",
    "position": "环形箭头中心",
    "description_zh": "缩略的 A–H 轮盘。"
  },
  {
    "id": "r1_push",
    "label_en": null,
    "label_zh": "粗平箭头（右推）",
    "type": "other",
    "parent": "frame_planning",
    "position": "环形箭头下方",
    "description_zh": "把迭代结果推向右侧团队方向的粗箭头。"
  },
  {
    "id": "r1_portfolio",
    "label_en": "Enterprise/Segment Portfolio – Epics",
    "label_zh": "企业/分段组合——史诗（Epics）",
    "type": "artifact",
    "parent": "frame_planning",
    "position": "规划迭代框下部"
  },
  {
    "id": "r1_team_business",
    "label_en": "Business Team",
    "label_zh": "业务团队",
    "type": "organization_unit",
    "parent": "frame_planning",
    "position": "规划迭代框右上（青色）"
  },
  {
    "id": "r1_team_technical",
    "label_en": "Technical Team",
    "label_zh": "技术团队",
    "type": "organization_unit",
    "parent": "frame_planning",
    "position": "规划迭代框右侧（橙色）"
  },
  {
    "id": "r1_team_operational",
    "label_en": "Operational Team",
    "label_zh": "运营团队",
    "type": "organization_unit",
    "parent": "frame_planning",
    "position": "规划迭代框右侧（橙色）"
  },
  {
    "id": "r1_people",
    "label_en": null,
    "label_zh": "团队人形图标",
    "type": "organization_unit",
    "parent": "frame_planning",
    "position": "规划迭代框右下",
    "description_zh": "两排共 10 个人形图标，蓝橙相间，表示跨职能混合团队。"
  },
  {
    "id": "row_segment",
    "label_en": null,
    "label_zh": "分段层（第二行）",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "第二行"
  },
  {
    "id": "r2_level",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "architecture",
    "parent": "row_segment",
    "level": 2,
    "position": "第二行左列标题"
  },
  {
    "id": "r2_desc",
    "label_en": "Organizing for operational and solution change at a program or portfolio level",
    "label_zh": "在项目群或组合层级组织运营与解决方案变更",
    "type": "note",
    "parent": "row_segment",
    "position": "第二行左列第二段"
  },
  {
    "id": "r2_wheel",
    "label_en": null,
    "label_zh": "ADM 轮盘缩略图",
    "type": "architecture",
    "parent": "row_segment",
    "position": "第二行左列"
  },
  {
    "id": "r2_safe",
    "label_en": "Agile/SAFe – Product/Portfolio Backlog – Change Plans – Epics",
    "label_zh": "敏捷/SAFe——产品/组合待办——变更计划——史诗",
    "type": "note",
    "parent": "row_segment",
    "position": "第二行中列"
  },
  {
    "id": "row_capability",
    "label_en": null,
    "label_zh": "能力层（第三行）",
    "type": "group",
    "parent": null,
    "level": 3,
    "position": "第三行"
  },
  {
    "id": "r3_level",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "parent": "row_capability",
    "level": 3,
    "position": "第三行左列标题"
  },
  {
    "id": "r3_desc",
    "label_en": "Organizing framework for change activity and roadmaps realizing capability increments",
    "label_zh": "组织变更活动与路线图、实现能力增量的框架",
    "type": "note",
    "parent": "row_capability",
    "position": "第三行左列第二段"
  },
  {
    "id": "r3_wheel",
    "label_en": null,
    "label_zh": "ADM 轮盘缩略图",
    "type": "architecture",
    "parent": "row_capability",
    "position": "第三行左列"
  },
  {
    "id": "r3_backlog_1",
    "label_en": "Agile/SAFe – Product/Solution Backlog – Capabilities to be Delivered",
    "label_zh": "敏捷/SAFe——产品/解决方案待办——待交付的能力",
    "type": "artifact",
    "parent": "row_capability",
    "position": "第三行中列第 1 条"
  },
  {
    "id": "r3_backlog_2",
    "label_en": "Agile/SAFe – Product/Program Backlog – Capability Increments (Features)",
    "label_zh": "敏捷/SAFe——产品/项目群待办——能力增量（特性）",
    "type": "artifact",
    "parent": "row_capability",
    "position": "第三行中列第 2 条"
  },
  {
    "id": "r3_backlog_3",
    "label_en": "Agile/SAFe – Program Team Backlog – Deliverable User Stories",
    "label_zh": "敏捷/SAFe——项目群团队待办——可交付的用户故事",
    "type": "artifact",
    "parent": "row_capability",
    "position": "第三行中列第 3 条"
  },
  {
    "id": "r3_backlog_4",
    "label_en": "Scrum – Sprint Team Backlog – Deliverable User Stories",
    "label_zh": "Scrum——冲刺团队待办——可交付的用户故事",
    "type": "artifact",
    "parent": "row_capability",
    "position": "第三行中列第 4 条"
  },
  {
    "id": "frame_build",
    "label_en": null,
    "label_zh": "Build Iteration 框（紫色虚线）",
    "type": "group",
    "parent": "row_capability",
    "position": "第三行右列左侧"
  },
  {
    "id": "r3_build",
    "label_en": "Build Iteration",
    "label_zh": "构建迭代",
    "type": "phase",
    "parent": "frame_build",
    "position": "紫框左上（紫色字）"
  },
  {
    "id": "r3_solution_team",
    "label_en": "Solution Team",
    "label_zh": "解决方案团队",
    "type": "organization_unit",
    "parent": "frame_build",
    "position": "紫框右上"
  },
  {
    "id": "r3_standup_1",
    "label_en": "Daily Stand-Up",
    "label_zh": "每日站会",
    "type": "process",
    "parent": "frame_build",
    "position": "紫框右中"
  },
  {
    "id": "r3_build_loop",
    "label_en": null,
    "label_zh": "紫色环形迭代箭头",
    "type": "other",
    "parent": "frame_build",
    "position": "紫框左侧"
  },
  {
    "id": "r3_build_wheel",
    "label_en": null,
    "label_zh": "ADM 轮盘（紫环内）",
    "type": "architecture",
    "parent": "frame_build",
    "position": "紫环中心"
  },
  {
    "id": "r3_build_push",
    "label_en": null,
    "label_zh": "紫色粗箭头（右推）",
    "type": "other",
    "parent": "frame_build",
    "position": "紫框下部"
  },
  {
    "id": "r3_build_people",
    "label_en": null,
    "label_zh": "解决方案团队人形图标",
    "type": "organization_unit",
    "parent": "frame_build",
    "position": "紫框中右（5 个紫色图标）"
  },
  {
    "id": "r3_runway",
    "label_en": "Solution Runway",
    "label_zh": "解决方案跑道",
    "type": "artifact",
    "parent": "frame_build",
    "position": "紫框右下"
  },
  {
    "id": "frame_delivery",
    "label_en": null,
    "label_zh": "Delivery Iteration 框（青色虚线）",
    "type": "group",
    "parent": "row_capability",
    "position": "第三行右列右侧"
  },
  {
    "id": "r3_delivery",
    "label_en": "Delivery Iteration",
    "label_zh": "交付迭代",
    "type": "phase",
    "parent": "frame_delivery",
    "position": "青框左上（青色字）"
  },
  {
    "id": "r3_delivery_team",
    "label_en": "Delivery Team (Dev Ops)",
    "label_zh": "交付团队（DevOps）",
    "type": "organization_unit",
    "parent": "frame_delivery",
    "position": "青框右上"
  },
  {
    "id": "r3_standup_2",
    "label_en": "Daily Stand-Up",
    "label_zh": "每日站会",
    "type": "process",
    "parent": "frame_delivery",
    "position": "青框右中"
  },
  {
    "id": "r3_deliv_loop",
    "label_en": null,
    "label_zh": "青色环形迭代箭头",
    "type": "other",
    "parent": "frame_delivery",
    "position": "青框左侧"
  },
  {
    "id": "r3_deliv_wheel",
    "label_en": null,
    "label_zh": "ADM 轮盘（青环内）",
    "type": "architecture",
    "parent": "frame_delivery",
    "position": "青环中心"
  },
  {
    "id": "r3_deliv_push",
    "label_en": null,
    "label_zh": "青色粗箭头（右推）",
    "type": "other",
    "parent": "frame_delivery",
    "position": "青框下部"
  },
  {
    "id": "r3_deliv_people",
    "label_en": null,
    "label_zh": "交付团队人形图标",
    "type": "organization_unit",
    "parent": "frame_delivery",
    "position": "青框中右（5 个深青图标）"
  },
  {
    "id": "r3_cicd",
    "label_en": "Agile Development Continuous Integration/Delivery",
    "label_zh": "敏捷开发持续集成/交付",
    "type": "capability",
    "parent": "frame_delivery",
    "position": "青框右下"
  }
]
```

## 关系

```json
[
  {
    "from": "r1_wheel",
    "to": "r2_wheel",
    "type": "sequence",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "浅蓝虚线箭头自上而下，指入分段轮盘的 A"
  },
  {
    "from": "r2_wheel",
    "to": "r3_wheel",
    "type": "sequence",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "浅蓝虚线箭头指入能力轮盘的 A"
  },
  {
    "from": "r1_loop",
    "to": "r1_wheel_loop",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "环形箭头绕轮盘一周，表示规划迭代循环"
  },
  {
    "from": "r1_push",
    "to": "r1_people",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "粗箭头把迭代结果推向团队一侧"
  },
  {
    "from": "r1_iterbox",
    "to": "r1_portfolio",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "规划迭代的产出是企业/分段组合与 Epic"
  },
  {
    "from": "r3_build_loop",
    "to": "r3_build_wheel",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "r3_build_push",
    "to": "r3_runway",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "r3_deliv_loop",
    "to": "r3_deliv_wheel",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "r3_deliv_push",
    "to": "r3_cicd",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "r3_backlog_4",
    "to": "r3_build",
    "type": "consumes",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "能力层冲刺团队待办是 Build/Delivery 迭代的输入（依位置与正文）"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_planning_iteration",
    "kind": "cycle",
    "name_zh": "规划迭代循环",
    "steps": [
      "r1_iterbox",
      "r1_portfolio"
    ],
    "description_zh": "时间盒的规划迭代反复产出企业/分段组合与 Epic。"
  },
  {
    "id": "f_build_delivery",
    "kind": "parallel",
    "name_zh": "能力层的构建与交付并行",
    "steps": [
      "r3_build",
      "r3_delivery"
    ],
    "description_zh": "Solution Team 与 Delivery Team 各自迭代，并分别产出 Solution Runway 与持续集成/交付。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_levels",
    "title_zh": "三层 × 三列对照（按原图逐格转录）",
    "columns": [
      "TOGAF ADM – Levels",
      "SAFe/Agile/Scrum Layers",
      "Characteristic Agile Team Iterations"
    ],
    "rows": [
      [
        "Strategic Architecture；Direction-setting at an executive level（附 ADM 轮盘缩略图）",
        "SAFe – Strategic Themes – Enterprise Portfolio Delivery",
        "Planning Iteration (Time-Boxed)；环形迭代箭头 + ADM 轮盘；Enterprise/Segment Portfolio – Epics；Business Team / Technical Team / Operational Team；团队人形图标（10 个）"
      ],
      [
        "Segment Architecture；Organizing for operational and solution change at a program or portfolio level（附 ADM 轮盘缩略图）",
        "Agile/SAFe – Product/Portfolio Backlog – Change Plans – Epics",
        "（与战略层共用同一个橙色虚线规划迭代框，本行右列无独立内容）"
      ],
      [
        "Capability Architecture；Organizing framework for change activity and roadmaps realizing capability increments（附 ADM 轮盘缩略图）",
        "Agile/SAFe – Product/Solution Backlog – Capabilities to be Delivered；Agile/SAFe – Product/Program Backlog – Capability Increments (Features)；Agile/SAFe – Program Team Backlog – Deliverable User Stories；Scrum – Sprint Team Backlog – Deliverable User Stories",
        "Build Iteration：Solution Team / Daily Stand-Up / 紫色环形箭头 + ADM 轮盘 / 5 个人形图标 / Solution Runway；Delivery Iteration：Delivery Team (Dev Ops) / Daily Stand-Up / 青色环形箭头 + ADM 轮盘 / 5 个人形图标 / Agile Development Continuous Integration/Delivery"
      ]
    ],
    "notes_zh": "列标题取自原图三列表头；单元格内多行文字按原图自上而下顺序合并。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝虚线箭头",
    "meaning_zh": "层级间自上而下的驱动（战略→分段→能力）",
    "explicit": true
  },
  {
    "symbol": "环形箭头（蓝/紫/青）",
    "meaning_zh": "一轮迭代循环，中心嵌 ADM 轮盘",
    "explicit": false
  },
  {
    "symbol": "粗平箭头",
    "meaning_zh": "迭代产出流向团队或下一环节",
    "explicit": false
  },
  {
    "symbol": "橙色虚线圆角框",
    "meaning_zh": "规划迭代单元（横跨战略与分段两层）",
    "explicit": false
  },
  {
    "symbol": "紫色/青色虚线圆角框",
    "meaning_zh": "能力层的 Build Iteration 与 Delivery Iteration 两个并行迭代单元",
    "explicit": false
  },
  {
    "symbol": "蓝色大括号",
    "meaning_zh": "把同一层级的三列括为一组",
    "explicit": false
  },
  {
    "symbol": "人形图标",
    "meaning_zh": "团队规模示意（蓝/橙或紫/青表示不同团队混合）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "3 列 × 3 行的对照画布。左列每行一个 ADM 轮盘缩略图配两段文字；中列是待办层次文字（能力层有四段）；右列第一、二行共用一个橙色虚线大框（含规划迭代环形箭头与团队），第三行是两个并列的紫色/青色虚线框。行与行之间用细蓝线与大括号分隔。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig3-1",
    "relation": "uses_legend",
    "note_zh": "左列三个层级都用同一张 TOGAF ADM 轮盘缩略图（与图 3-1 相同）。"
  },
  {
    "target": "G20F/fig5-4",
    "relation": "complements",
    "note_zh": "图 5-4 进一步展示架构如何支撑产品待办与冲刺待办的定义。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "人形图标数量按像素计为 10 个（两排各 5 个）与 5 个（能力层两个框各 5 个），仅作团队规模示意。",
    "橙色虚线规划迭代框横跨第一、二行的判断依据框线走向，原文未明说。",
    "左列轮盘内的 A–H 缩略标签极小，按与图 3-1 一致的轮盘结构识别，未逐字转录。"
  ],
  "analyzed_from": [
    "英文 PDF 第 28 页原图截图（figctx GT crop + 2x2 放大块 + 400dpi 局部）",
    "英文 PDF 第 28 页与第 29 页正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 306–320 行",
    "figs/g20f_fig4-4.svg 源码与文本"
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
