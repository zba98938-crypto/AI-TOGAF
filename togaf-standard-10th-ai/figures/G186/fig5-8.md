# G186/fig5-8 · 开发支持组合的架构的示例项目计划

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig5-8.md) · [JSON](../../architecture/diagrams/G186/fig5-8.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 67 页

![英文原图](../assets/G186/fig5-8-p0067.png)

PDF 坐标：`[76.3, 36.0, 535.7, 724.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
eo
1 Start Architecture Project
2 Group Work Packages to Themes
Partial Strategic Level Phase H
09.05
‘Start Partial Strategic Level Phase H
In-fight projects and gaps
Current fiscal year roadmap
Context specific for the EA Capability:
Goals
Request for Architecture Work
10
‘Complete Partial Strategic Level Phase H
un
Partial Strategic Level Phase A
to
12
Start Partial Strategic Level Phase A
13
New Strategic Architecture
14
Request for Architecture Work
15
Work package and themes
16
‘Stakeholder priority trade-off
17
Updated architecture specifications
18
‘Traceabilty matrix for value proposition
10:28
19
Complete Partial Strategic Level Phase A
20
Partial Strategic Level Phaso G
2a
‘Start Partial Strategic Level Phase G
10:28
22
Perform architecture compliance reviews
23
Risk assessment
24
Complete Partial Strategic Level Phase G
1
25
_—————
Balance Opportunity and Viability
26
Partial Capability Level Phases B, C, and D for each Enterprise Capability
—
27
Partial Capability Phase B
—
28
Start Partial Capabilty Phase B
1141
29
Elaborate specifications to estimate effort size
30
Identfy reference architectures and market benchmarks
31
Identfy candidate Architecture Bulding Blocks
32
Identfy Solution Building Blocks (optional)
33
Partial Capability Phase C
34
‘Start Partial Capabilty Phase C
11.16
35
Elaborate specifications to estimate effort size
36
Identfy reference architectures and market benchmarks
37
Identfy candidate Architecture Building Blocks
vm
38
Identfy Solution Building Blocks (optional)
39
Partial Capability Phase D
40
‘Start Partial Capabilty Phase D
a
Elaborate specifications to estimate effort size
42
Identfy reference architectures and market benchmarks
43
Identfy candidate Architecture Building Blocks
44
Identfy Solution Building Blocks (optional)
45
Complete Partial Capabiity Phases B, C, and D
2-08
46
Partial Portfolio Level Phase E
a7
‘Start Partial Portfolio Level Phase E
Pere
48
Consolidate Gaps
49
Define Work Packages
50
Draft Architecture Roadmap
51
‘Complete Partial Portfolio Level Phase E
12.09
52
Partial Capability Phaso F
53
Start Partial Capabilty Phase F
12.09
54
Iniia/draft Implementation and Migration Plan
55
Draft governance plan
56
‘Complete Partial Capabilty Phase F
12.23
57
Partial Project Level Phaso A (for each Project in Portfolio)
58
Start Partial Project Level Phase A (for each Project in Portfolio)
12-23
59
Candidate proof-of-concept work packages (as needed)
60
Draft success measures
61
‘Complete Partial Project Level Phase A (for each Project in Portfolio)
01-06
62
Run Up to Budget
63
—
Partial Capability Level Phase A (for each Capability)
4
64
‘Start Capabilty Phase A
01.06
65
Update roadmap
66
Update risk matrix
67
Update work package and architecture specification
68
Complete Capabiity Phase A
6
Partial Capability Level Phase F (for each Project in Portfolio)
70
‘Start Partial Capabilty Level Phase F (for each Project in Portfobo)
ive
n
Populate governance and approval plan
2
‘Complete Partial Capabity Level Phase F (for each Project in Portfoto)
02-03
73
Partial Capability Level Phase G (for each Prohect in Portfolio)
7
Start Partial Capabilty Level Phase G (for each Prohect in Portfolio)
02-03
75
Finalize governance model and plan
76
‘Complete Partial Capabilty Level Phase G (for each Prohect in Portfolio)
7
Drive Confidence of Delivery
02.17
78
a
Partial Enterprise Level Phase F
q
73
Start Partial Enterprise Level Phase F
0217
80
Enterprise conte:
a1
Initiate completion of architecture work
82
Define target transition architectures
83
Finalze effort and resource estimates
8a
Define variance measures in project-specific governance model
85
Update risk matrix
=
86
EA Capability Context
87
Revise EA governance
88
Revise EA engagement model
89
Revise EA organization mode!
90
‘Complete Partial Enterprise Level Phase F
—
```

## 概要（历史解释；局部修正见上）

支持组合的架构项目计划：90 行任务把工作包分组、机会/可行性平衡、预算申报与交付信心四段串起来。

## 目的（历史解释；局部修正见上）

示范第 5.2.5 节：组合架构的路径是分组工作包到主题→平衡机会与可行性→进入预算→建立交付信心；本图给出任务级样板，说明组合工作要按能力/项目重复推进，而不是一次走完 ADM。

## 阅读顺序（历史解释；局部修正见上）

左侧自上而下读任务，粗体行是四条主线与阶段分组，缩进行是任务。右侧条形自左向右表示时间：深色粗线为阶段汇总条，蓝色条为任务条，细黑箭头为依赖。先读四条主线：Group Work Packages to Themes → Balance Opportunity and Viability → Run Up to Budget → Drive Confidence of Delivery；再读每条主线内的阶段顺序（H→A→G；B/C/D→E→F→A；A→F→G；企业层 F）。

## 关键含义（历史解释；局部修正见上）

- 计划共 90 行任务，四条主线是：把工作包分组到主题、平衡机会与可行性、进入预算、建立交付信心。
- 第一条主线先走阶段 H（在途项目与差距、本财年路线图、EA 能力的目标与架构工作请求），再走阶段 A（新战略架构、工作包与主题、利益相关者优先级权衡、价值主张追溯矩阵），最后阶段 G（架构合规审查、风险评估）。
- 第二条主线对每个企业能力执行 B/C/D：细化规格以估算工作量、识别参考架构与市场基准、识别候选 ABB、可选 SBB；随后组合层阶段 E 汇总差距、定义工作包、起草路线图。
- 第二条主线继续：能力层阶段 F 形成实施/迁移计划与治理计划草案，项目层阶段 A 为组合中的每个项目准备概念验证工作包与成功度量。
- 第三条主线“进入预算”按能力层阶段 A（更新路线图、风险矩阵、工作包与架构规格）、阶段 F（治理与审批计划）、阶段 G（定稿治理模型与计划）重复。
- 第四条主线回到企业层阶段 F，分企业语境与 EA 能力语境：完成架构工作、定义目标过渡架构、资源估算、偏差度量、风险矩阵，以及修订 EA 治理/参与/组织模型。
- 大量标签带“for each Capability / for each Project in Portfolio”限定，说明同一组阶段要在每个能力/项目上重复执行，计划是模板化的多实例推进。

## 层级（历史解释；局部修正见上）

三层：四条主线（G1）→ 阶段分组（G2，如部分战略层阶段 H/A/G、能力层 B/C/D、组合层 E、能力层 F、项目层 A）→ 子分组（G3，如 EA 能力专属语境、Phase B/C/D、企业语境、EA 能力语境）→ 任务。

## 线条含义（历史解释；局部修正见上）

深色粗横线是主线/阶段汇总条；蓝色条是任务条；细黑线加箭头是完成—开始依赖；竖向括号标出共同起止；左缘彩色窄带按主线/阶段分组着色。无图例。本分析只把主线/阶段之间的依赖记入 relationships；同一阶段内任务之间的细箭头未逐条枚举。

## 易误读点（历史解释；局部修正见上）

- 不要把 90 行读成一次线性 ADM；B/C/D、E、F、A 会按每个能力/项目重复。
- 带“for each Project in Portfolio”的行不是一次性任务，而是对组合内每个项目都要执行。
- 不要根据条形长度推算实际工期；原图只有 MM-DD 标记，没有年份或完整日历轴。
- 中文 SVG 只是 16 行摘要，不是原图的完整转录，不能据它核对任务级依赖。
- 中文 PNG 的大量空白/发白行不是“无任务”，而是本地化失败。

## 元素

```json
[
  {
    "id": "prj_start",
    "label_en": "Start Architecture Project",
    "label_zh": "启动架构项目",
    "type": "event",
    "parent": null,
    "level": 0,
    "order": 1
  },
  {
    "id": "group_themes",
    "label_en": "Group Work Packages to Themes",
    "label_zh": "把工作包分组到主题",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 2
  },
  {
    "id": "phase_h",
    "label_en": "Partial Strategic Level Phase H",
    "label_zh": "部分战略层阶段 H",
    "type": "phase",
    "parent": "group_themes",
    "level": 2,
    "order": 3
  },
  {
    "id": "ea_context_h",
    "label_en": "Context specific for the EA Capability:",
    "label_zh": "EA 能力专属语境",
    "type": "group",
    "parent": "phase_h",
    "level": 3,
    "order": 7
  },
  {
    "id": "phase_a",
    "label_en": "Partial Strategic Level Phase A",
    "label_zh": "部分战略层阶段 A",
    "type": "phase",
    "parent": "group_themes",
    "level": 2,
    "order": 11
  },
  {
    "id": "phase_g",
    "label_en": "Partial Strategic Level Phase G",
    "label_zh": "部分战略层阶段 G",
    "type": "phase",
    "parent": "group_themes",
    "level": 2,
    "order": 20
  },
  {
    "id": "balance_opportunity",
    "label_en": "Balance Opportunity and Viability",
    "label_zh": "平衡机会与可行性",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 25
  },
  {
    "id": "capability_bcd",
    "label_en": "Partial Capability Level Phases B, C, and D for each Enterprise Capability",
    "label_zh": "每个企业能力的部分能力层阶段 B、C、D",
    "type": "phase",
    "parent": "balance_opportunity",
    "level": 2,
    "order": 26,
    "description_zh": "原图该行行末被右侧条形区截断，完整标签据图中可见部分与表 8-1 补全。"
  },
  {
    "id": "capability_b",
    "label_en": "Partial Capability Phase B",
    "label_zh": "部分能力阶段 B",
    "type": "group",
    "parent": "capability_bcd",
    "level": 3,
    "order": 27
  },
  {
    "id": "capability_c",
    "label_en": "Partial Capability Phase C",
    "label_zh": "部分能力阶段 C",
    "type": "group",
    "parent": "capability_bcd",
    "level": 3,
    "order": 33
  },
  {
    "id": "capability_d",
    "label_en": "Partial Capability Phase D",
    "label_zh": "部分能力阶段 D",
    "type": "group",
    "parent": "capability_bcd",
    "level": 3,
    "order": 39
  },
  {
    "id": "portfolio_phase_e",
    "label_en": "Partial Portfolio Level Phase E",
    "label_zh": "部分组合层阶段 E",
    "type": "phase",
    "parent": "balance_opportunity",
    "level": 2,
    "order": 46
  },
  {
    "id": "capability_phase_f",
    "label_en": "Partial Capability Phase F",
    "label_zh": "部分能力阶段 F",
    "type": "phase",
    "parent": "balance_opportunity",
    "level": 2,
    "order": 52
  },
  {
    "id": "project_phase_a",
    "label_en": "Partial Project Level Phase A (for each Project in Portfolio)",
    "label_zh": "部分项目层阶段 A（组合中的每个项目）",
    "type": "phase",
    "parent": "balance_opportunity",
    "level": 2,
    "order": 57
  },
  {
    "id": "run_budget",
    "label_en": "Run Up to Budget",
    "label_zh": "进入预算",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 62
  },
  {
    "id": "capability_phase_a",
    "label_en": "Partial Capability Level Phase A (for each Capability)",
    "label_zh": "部分能力层阶段 A（每个能力）",
    "type": "phase",
    "parent": "run_budget",
    "level": 2,
    "order": 63
  },
  {
    "id": "capability_phase_f_2",
    "label_en": "Partial Capability Level Phase F (for each Project in Portfolio)",
    "label_zh": "部分能力层阶段 F（组合中的每个项目）",
    "type": "phase",
    "parent": "run_budget",
    "level": 2,
    "order": 69
  },
  {
    "id": "capability_phase_g",
    "label_en": "Partial Capability Level Phase G (for each Project in Portfolio)",
    "label_zh": "部分能力层阶段 G（组合中的每个项目）",
    "type": "phase",
    "parent": "run_budget",
    "level": 2,
    "order": 73
  },
  {
    "id": "drive_confidence",
    "label_en": "Drive Confidence of Delivery",
    "label_zh": "建立交付信心",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 77
  },
  {
    "id": "enterprise_phase_f",
    "label_en": "Partial Enterprise Level Phase F",
    "label_zh": "部分企业层阶段 F",
    "type": "phase",
    "parent": "drive_confidence",
    "level": 2,
    "order": 78
  },
  {
    "id": "enterprise_context",
    "label_en": "Enterprise context:",
    "label_zh": "企业语境",
    "type": "group",
    "parent": "enterprise_phase_f",
    "level": 3,
    "order": 80
  },
  {
    "id": "ea_capability_context",
    "label_en": "EA Capability Context",
    "label_zh": "EA 能力语境",
    "type": "group",
    "parent": "enterprise_phase_f",
    "level": 3,
    "order": 86
  }
]
```

## 关系

```json
[
  {
    "from": "prj_start",
    "to": "group_themes",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "项目启动后进入“把工作包分组到主题”。"
  },
  {
    "from": "group_themes",
    "to": "balance_opportunity",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "主题分组后平衡机会与可行性。"
  },
  {
    "from": "balance_opportunity",
    "to": "run_budget",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "完成机会/可行性权衡后进入预算。"
  },
  {
    "from": "run_budget",
    "to": "drive_confidence",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "预算申报后建立交付信心。"
  },
  {
    "from": "phase_h",
    "to": "phase_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "阶段 H 完成后进入阶段 A。"
  },
  {
    "from": "phase_a",
    "to": "phase_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "阶段 A 后做阶段 G 的合规审查与风险评估。"
  },
  {
    "from": "capability_bcd",
    "to": "portfolio_phase_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "能力层 B/C/D 后进入组合层阶段 E。"
  },
  {
    "from": "portfolio_phase_e",
    "to": "capability_phase_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "阶段 E 后形成能力层实施/迁移计划。"
  },
  {
    "from": "capability_phase_f",
    "to": "project_phase_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "能力层 F 后为组合内每个项目启动阶段 A。"
  },
  {
    "from": "capability_phase_a",
    "to": "capability_phase_f_2",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "能力层 A 后准备治理与审批计划。"
  },
  {
    "from": "capability_phase_f_2",
    "to": "capability_phase_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "阶段 F 后定稿治理模型与计划。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_main",
    "kind": "sequence",
    "name_zh": "四条计划主线",
    "steps": [
      "prj_start",
      "group_themes",
      "balance_opportunity",
      "run_budget",
      "drive_confidence"
    ]
  },
  {
    "id": "f_phases",
    "kind": "sequence",
    "name_zh": "阶段顺序",
    "steps": [
      "phase_h",
      "phase_a",
      "phase_g",
      "capability_bcd",
      "portfolio_phase_e",
      "capability_phase_f",
      "project_phase_a",
      "capability_phase_a",
      "capability_phase_f_2",
      "capability_phase_g",
      "enterprise_phase_f"
    ]
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_tasks",
    "title_zh": "图 5-8 全部 90 行任务逐行转录",
    "columns": [
      "#",
      "Task (English, as printed)",
      "Row type / 行类型",
      "Parent group (English)",
      "Note / 备注"
    ],
    "rows": [
      [
        "1",
        "Start Architecture Project",
        "项目里程碑",
        "",
        ""
      ],
      [
        "2",
        "Group Work Packages to Themes",
        "主线分组",
        "",
        ""
      ],
      [
        "3",
        "Partial Strategic Level Phase H",
        "阶段分组",
        "Group Work Packages to Themes",
        ""
      ],
      [
        "4",
        "Start Partial Strategic Level Phase H",
        "任务",
        "Partial Strategic Level Phase H",
        ""
      ],
      [
        "5",
        "In-flight projects and gaps",
        "任务",
        "Partial Strategic Level Phase H",
        ""
      ],
      [
        "6",
        "Current fiscal year roadmap",
        "任务",
        "Partial Strategic Level Phase H",
        ""
      ],
      [
        "7",
        "Context specific for the EA Capability:",
        "子分组",
        "Partial Strategic Level Phase H",
        ""
      ],
      [
        "8",
        "Goals",
        "任务",
        "Context specific for the EA Capability:",
        ""
      ],
      [
        "9",
        "Request for Architecture Work",
        "任务",
        "Context specific for the EA Capability:",
        ""
      ],
      [
        "10",
        "Complete Partial Strategic Level Phase H",
        "任务",
        "Context specific for the EA Capability:",
        ""
      ],
      [
        "11",
        "Partial Strategic Level Phase A",
        "阶段分组",
        "Group Work Packages to Themes",
        ""
      ],
      [
        "12",
        "Start Partial Strategic Level Phase A",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "13",
        "New Strategic Architecture",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "14",
        "Request for Architecture Work",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "15",
        "Work package and themes",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "16",
        "Stakeholder priority trade-off",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "17",
        "Updated architecture specifications",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "18",
        "Traceability matrix for value proposition",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "19",
        "Complete Partial Strategic Level Phase A",
        "任务",
        "Partial Strategic Level Phase A",
        ""
      ],
      [
        "20",
        "Partial Strategic Level Phase G",
        "阶段分组",
        "Group Work Packages to Themes",
        ""
      ],
      [
        "21",
        "Start Partial Strategic Level Phase G",
        "任务",
        "Partial Strategic Level Phase G",
        ""
      ],
      [
        "22",
        "Perform architecture compliance reviews",
        "任务",
        "Partial Strategic Level Phase G",
        ""
      ],
      [
        "23",
        "Risk assessment",
        "任务",
        "Partial Strategic Level Phase G",
        ""
      ],
      [
        "24",
        "Complete Partial Strategic Level Phase G",
        "任务",
        "Partial Strategic Level Phase G",
        ""
      ],
      [
        "25",
        "Balance Opportunity and Viability",
        "主线分组",
        "",
        ""
      ],
      [
        "26",
        "Partial Capability Level Phases B, C, and D for each Enterprise Capability",
        "阶段分组",
        "Balance Opportunity and Viability",
        "原图该行右侧被条形区截断，末尾只能看到“…Capabilit”；按表 8-1 补全为 for each Enterprise Capability。"
      ],
      [
        "27",
        "Partial Capability Phase B",
        "子分组",
        "Partial Capability Level Phases B, C, and D for each Enterprise Capability",
        ""
      ],
      [
        "28",
        "Start Partial Capability Phase B",
        "任务",
        "Partial Capability Phase B",
        ""
      ],
      [
        "29",
        "Elaborate specifications to estimate effort size",
        "任务",
        "Partial Capability Phase B",
        ""
      ],
      [
        "30",
        "Identify reference architectures and market benchmarks",
        "任务",
        "Partial Capability Phase B",
        ""
      ],
      [
        "31",
        "Identify candidate Architecture Building Blocks",
        "任务",
        "Partial Capability Phase B",
        ""
      ],
      [
        "32",
        "Identify Solution Building Blocks (optional)",
        "任务",
        "Partial Capability Phase B",
        ""
      ],
      [
        "33",
        "Partial Capability Phase C",
        "子分组",
        "Partial Capability Level Phases B, C, and D for each Enterprise Capability",
        ""
      ],
      [
        "34",
        "Start Partial Capability Phase C",
        "任务",
        "Partial Capability Phase C",
        ""
      ],
      [
        "35",
        "Elaborate specifications to estimate effort size",
        "任务",
        "Partial Capability Phase C",
        ""
      ],
      [
        "36",
        "Identify reference architectures and market benchmarks",
        "任务",
        "Partial Capability Phase C",
        ""
      ],
      [
        "37",
        "Identify candidate Architecture Building Blocks",
        "任务",
        "Partial Capability Phase C",
        ""
      ],
      [
        "38",
        "Identify Solution Building Blocks (optional)",
        "任务",
        "Partial Capability Phase C",
        ""
      ],
      [
        "39",
        "Partial Capability Phase D",
        "子分组",
        "Partial Capability Level Phases B, C, and D for each Enterprise Capability",
        ""
      ],
      [
        "40",
        "Start Partial Capability Phase D",
        "任务",
        "Partial Capability Phase D",
        ""
      ],
      [
        "41",
        "Elaborate specifications to estimate effort size",
        "任务",
        "Partial Capability Phase D",
        ""
      ],
      [
        "42",
        "Identify reference architectures and market benchmarks",
        "任务",
        "Partial Capability Phase D",
        ""
      ],
      [
        "43",
        "Identify candidate Architecture Building Blocks",
        "任务",
        "Partial Capability Phase D",
        ""
      ],
      [
        "44",
        "Identify Solution Building Blocks (optional)",
        "任务",
        "Partial Capability Phase D",
        ""
      ],
      [
        "45",
        "Complete Partial Capability Phases B, C, and D",
        "任务",
        "Partial Capability Level Phases B, C, and D for each Enterprise Capability",
        ""
      ],
      [
        "46",
        "Partial Portfolio Level Phase E",
        "阶段分组",
        "Balance Opportunity and Viability",
        ""
      ],
      [
        "47",
        "Start Partial Portfolio Level Phase E",
        "任务",
        "Partial Portfolio Level Phase E",
        ""
      ],
      [
        "48",
        "Consolidate Gaps",
        "任务",
        "Partial Portfolio Level Phase E",
        ""
      ],
      [
        "49",
        "Define Work Packages",
        "任务",
        "Partial Portfolio Level Phase E",
        ""
      ],
      [
        "50",
        "Draft Architecture Roadmap",
        "任务",
        "Partial Portfolio Level Phase E",
        ""
      ],
      [
        "51",
        "Complete Partial Portfolio Level Phase E",
        "任务",
        "Partial Portfolio Level Phase E",
        ""
      ],
      [
        "52",
        "Partial Capability Phase F",
        "阶段分组",
        "Balance Opportunity and Viability",
        ""
      ],
      [
        "53",
        "Start Partial Capability Phase F",
        "任务",
        "Partial Capability Phase F",
        ""
      ],
      [
        "54",
        "Initial/draft Implementation and Migration Plan",
        "任务",
        "Partial Capability Phase F",
        ""
      ],
      [
        "55",
        "Draft governance plan",
        "任务",
        "Partial Capability Phase F",
        ""
      ],
      [
        "56",
        "Complete Partial Capability Phase F",
        "任务",
        "Partial Capability Phase F",
        ""
      ],
      [
        "57",
        "Partial Project Level Phase A (for each Project in Portfolio)",
        "阶段分组",
        "Balance Opportunity and Viability",
        ""
      ],
      [
        "58",
        "Start Partial Project Level Phase A (for each Project in Portfolio)",
        "任务",
        "Partial Project Level Phase A (for each Project in Portfolio)",
        ""
      ],
      [
        "59",
        "Candidate proof-of-concept work packages (as needed)",
        "任务",
        "Partial Project Level Phase A (for each Project in Portfolio)",
        ""
      ],
      [
        "60",
        "Draft success measures",
        "任务",
        "Partial Project Level Phase A (for each Project in Portfolio)",
        ""
      ],
      [
        "61",
        "Complete Partial Project Level Phase A (for each Project in Portfolio)",
        "任务",
        "Partial Project Level Phase A (for each Project in Portfolio)",
        ""
      ],
      [
        "62",
        "Run Up to Budget",
        "主线分组",
        "",
        ""
      ],
      [
        "63",
        "Partial Capability Level Phase A (for each Capability)",
        "阶段分组",
        "Run Up to Budget",
        ""
      ],
      [
        "64",
        "Start Capability Phase A",
        "任务",
        "Partial Capability Level Phase A (for each Capability)",
        ""
      ],
      [
        "65",
        "Update roadmap",
        "任务",
        "Partial Capability Level Phase A (for each Capability)",
        ""
      ],
      [
        "66",
        "Update risk matrix",
        "任务",
        "Partial Capability Level Phase A (for each Capability)",
        ""
      ],
      [
        "67",
        "Update work package and architecture specification",
        "任务",
        "Partial Capability Level Phase A (for each Capability)",
        ""
      ],
      [
        "68",
        "Complete Capability Phase A",
        "任务",
        "Partial Capability Level Phase A (for each Capability)",
        ""
      ],
      [
        "69",
        "Partial Capability Level Phase F (for each Project in Portfolio)",
        "阶段分组",
        "Run Up to Budget",
        ""
      ],
      [
        "70",
        "Start Partial Capability Level Phase F (for each Project in Portfolio)",
        "任务",
        "Partial Capability Level Phase F (for each Project in Portfolio)",
        ""
      ],
      [
        "71",
        "Populate governance and approval plan",
        "任务",
        "Partial Capability Level Phase F (for each Project in Portfolio)",
        ""
      ],
      [
        "72",
        "Complete Partial Capability Level Phase F (for each Project in Portfolio)",
        "任务",
        "Partial Capability Level Phase F (for each Project in Portfolio)",
        ""
      ],
      [
        "73",
        "Partial Capability Level Phase G (for each Project in Portfolio)",
        "阶段分组",
        "Run Up to Budget",
        ""
      ],
      [
        "74",
        "Start Partial Capability Level Phase G (for each Project in Portfolio)",
        "任务",
        "Partial Capability Level Phase G (for each Project in Portfolio)",
        ""
      ],
      [
        "75",
        "Finalize governance model and plan",
        "任务",
        "Partial Capability Level Phase G (for each Project in Portfolio)",
        ""
      ],
      [
        "76",
        "Complete Partial Capability Level Phase G (for each Project in Portfolio)",
        "任务",
        "Partial Capability Level Phase G (for each Project in Portfolio)",
        ""
      ],
      [
        "77",
        "Drive Confidence of Delivery",
        "主线分组",
        "",
        ""
      ],
      [
        "78",
        "Partial Enterprise Level Phase F",
        "阶段分组",
        "Drive Confidence of Delivery",
        ""
      ],
      [
        "79",
        "Start Partial Enterprise Level Phase F",
        "任务",
        "Partial Enterprise Level Phase F",
        "原图此行以下进入 Enterprise context / EA Capability Context 两个子分组。"
      ],
      [
        "80",
        "Enterprise context:",
        "子分组",
        "Partial Enterprise Level Phase F",
        ""
      ],
      [
        "81",
        "Initiate completion of architecture work",
        "任务",
        "Enterprise context:",
        ""
      ],
      [
        "82",
        "Define target transition architectures",
        "任务",
        "Enterprise context:",
        ""
      ],
      [
        "83",
        "Finalize effort and resource estimates",
        "任务",
        "Enterprise context:",
        ""
      ],
      [
        "84",
        "Define variance measures in project-specific governance model",
        "任务",
        "Enterprise context:",
        ""
      ],
      [
        "85",
        "Update risk matrix",
        "任务",
        "Enterprise context:",
        ""
      ],
      [
        "86",
        "EA Capability Context",
        "子分组",
        "Partial Enterprise Level Phase F",
        ""
      ],
      [
        "87",
        "Revise EA governance",
        "任务",
        "EA Capability Context",
        ""
      ],
      [
        "88",
        "Revise EA engagement model",
        "任务",
        "EA Capability Context",
        ""
      ],
      [
        "89",
        "Revise EA organization model",
        "任务",
        "EA Capability Context",
        ""
      ],
      [
        "90",
        "Complete Partial Enterprise Level Phase F",
        "任务",
        "Partial Enterprise Level Phase F",
        ""
      ]
    ],
    "notes_zh": "任务名保留英文原样；中文阶段名见 elements 的 label_zh。行类型由粗体/缩进判断。原图条形为相对周尺度，日期标记为 MM-DD，无年份，未逐条转录。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深色粗横线（两端短竖线）",
    "meaning_zh": "主线/阶段汇总条",
    "explicit": false
  },
  {
    "symbol": "浅蓝色矩形条",
    "meaning_zh": "单个任务的工期条",
    "explicit": false
  },
  {
    "symbol": "细黑线 + 箭头",
    "meaning_zh": "任务之间的完成—开始依赖",
    "explicit": false
  },
  {
    "symbol": "竖向括号（两端箭头）",
    "meaning_zh": "一组任务或一个阶段的共同时间跨度",
    "explicit": false
  },
  {
    "symbol": "左侧彩色窄带",
    "meaning_zh": "按主线/阶段分组着色",
    "explicit": false
  },
  {
    "symbol": "粗体行 + 缩进",
    "meaning_zh": "粗体为阶段/分组，缩进为任务",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "左侧约三分之一为编号+缩进任务清单，右侧约三分之二为按周排列的条形区；任务自上而下按计划顺序排列，条形自左向右延伸。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig5-5",
    "relation": "instance_of",
    "note_zh": "图 5-5 是程式化的架构开发甘特图；本图把同一模式套用到“支持组合”目的，展开为 90 行任务。"
  },
  {
    "target": "G186/fig5-7",
    "relation": "related",
    "note_zh": "图 5-7 是同一甘特模式在“支持战略”目的下的实例。"
  },
  {
    "target": "G186/fig5-9",
    "relation": "related",
    "note_zh": "图 5-9 是同一甘特模式在“支持项目”目的下的实例。"
  },
  {
    "target": "G186/fig8-1",
    "relation": "related",
    "note_zh": "图 8-1 的能力与项目连续谱说明组合为何要在 Sustain/Improve 之间持续迭代；本图给出对应的项目计划。"
  },
  {
    "target": "G186/fig6-1",
    "relation": "related",
    "note_zh": "图 6-1 第 2 栏概括支持组合目的的走查重点，与本图四条主线对应。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "原图第 26 行行末被条形区截断，完整标签按表 8-1 补全为 for each Enterprise Capability。",
    "原图条形为相对周尺度，日期标记只有 MM-DD，没有年份；无法逐条还原起止日期。",
    "任务级依赖箭头很多，本分析只记录主线/阶段级依赖，未逐条枚举。",
    "中文 SVG 是 16 行摘要，不能用于核对 90 行任务的完整性；中文 PNG 大量文字不可读。"
  ],
  "analyzed_from": [
    "英文 PDF 第 67 页图 5-8 截图（整图与 2x2 放大块）",
    "英文 PDF 第 66 页 5.2.5 节正文、第 67 页图题",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 882–917 行",
    "figs/zh/g186e_fig5-8_zh.svg 与 figs/zh/g186e_fig5-8_zh.png"
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
