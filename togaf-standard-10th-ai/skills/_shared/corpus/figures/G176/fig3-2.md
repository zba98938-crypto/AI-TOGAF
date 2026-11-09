# G176/fig3-2 · 开发业务场景的阶段与步骤

> 当前图示解析：[Markdown](../../architecture/diagrams/G176/fig3-2.md) · [JSON](../../architecture/diagrams/G176/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G176e.pdf`；SHA-256：`48c76fbfd164020fcbc0a4f2ec12ee849a2af83424a332883f9a8e0260bf4961`。

## 原图 · PDF 第 20 页

![英文原图](../assets/G176/fig3-2-p0020.png)

PDF 坐标：`[74.0, 36.0, 538.0, 178.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Premise Formulation Phase
Initial Verification Phase
Refinement Phase
Steps
Steps
Steps
Plan
.
Plan
.
Plan
.
.
Gather Information
Gather Information
Gather Information
Analyze/Process
.
Analyze/Process
.
Analyze/Process
Document
.
Document
.
Document
Review
.
Review
.
Review
4—Human Acte
Ss
```

## 概要（历史解释；局部修正见上）

业务场景分三个阶段开发（前提形成、初步验证、细化），每个阶段都执行同样 5 个步骤，并逐一改进五个要素。

## 目的（历史解释；局部修正见上）

第 3.1 节用它说明业务场景是怎样开发出来的：经过若干阶段来形成、验证和细化驱动工作的业务需求前提；每个阶段都由规划、收集信息、分析、记录、评审这些步骤组成，并在每个阶段中依次改进业务场景的五个要素（图 3-1）。第 3.2 节先统一描述这些步骤，第 3.3 节再分别描述三个阶段。

## 阅读顺序（历史解释；局部修正见上）

从左到右读 3 个面板，面板标题是阶段名，左右顺序就是阶段的先后。每个面板左侧“Steps:”下的 5 个圆点是该阶段要执行的步骤，自上而下为执行顺序；右侧 5 个编号色块是本阶段要处理的五个要素，配色与图 3-1 相同。三个面板内容完全一样，表示步骤和要素在每个阶段都重复一遍，区别只在阶段的目标和产出（见第 3.3 节）。图中没有箭头或连线。

## 关键含义（历史解释；局部修正见上）

- 三个阶段依次为：前提形成 → 初步验证 → 细化。正文说明这些阶段从提出前提一直走到业务场景获业务领导者批准。
- 每个阶段都重复同样 5 个步骤：规划 → 收集信息 → 分析/处理 → 记录 → 评审；第 3.2 节说明因为步骤在各阶段重复，所以先统一描述步骤。
- 每个阶段都覆盖全部五个要素（问题、环境、成果、人的参与者、计算机参与者），逐阶段改进；这些要素就是图 3-1 的五个要素。
- 前提形成阶段：记录工作背后的主张（前提，如“上 ERP 就能解决系统不互通”）和它隐含的未明说问题，并找出能帮助验证和细化前提的目标利益相关者。
- 初步验证阶段：与利益相关者面对面考察真实业务问题，产出一份草稿性、尚不完整的业务场景和下一步建议。
- 细化阶段：迭代细化直到就推进方式达成一致，产出发布的业务场景文档；正文说明此时要判断业务场景是否已足以把需求传给下游架构过程，决定进入 ADM 下一阶段还是继续细化。
- 获批的业务场景文档放入需求存储库，作为驱动下游架构工作的高层需求陈述，并用来验证架构质量（第 3.3 节）。

## 层级（历史解释；局部修正见上）

三层视觉包含：外框（业务场景开发过程）→ 3 个阶段面板 → 每个面板内的步骤列表与五要素色块。步骤和要素在三个面板中原样重复，表示它们属于每一个阶段。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头。阶段顺序由面板从左到右的位置表示；步骤顺序由列表自上而下表示；“阶段执行步骤、处理要素”由面板包含关系表示。关系清单中这些都标为推断。

## 易误读点（历史解释；局部修正见上）

- 三个面板内容相同不是重复排版，而是表示每个阶段都要执行全部步骤、处理全部要素。
- 面板之间没有箭头，阶段顺序来自左右位置和正文；细化阶段结束时可能继续细化，并非一次走完。
- 五要素色块的上下顺序与图 3-1 的编号一致，不是步骤；步骤是左侧的圆点列表。
- 中文稿引用的 SVG 去掉了五要素色块，只剩阶段和步骤，容易让人以为各阶段不涉及五要素。

## 元素

```json
[
  {
    "id": "ph_premise",
    "label_en": "Premise Formulation Phase",
    "label_zh": "前提形成阶段",
    "type": "phase",
    "parent": null,
    "order": 1,
    "position": "左面板"
  },
  {
    "id": "ph_verification",
    "label_en": "Initial Verification Phase",
    "label_zh": "初步验证阶段",
    "type": "phase",
    "parent": null,
    "order": 2,
    "position": "中面板"
  },
  {
    "id": "ph_refinement",
    "label_en": "Refinement Phase",
    "label_zh": "细化阶段",
    "type": "phase",
    "parent": null,
    "order": 3,
    "position": "右面板"
  },
  {
    "id": "g_steps",
    "label_en": "Steps:",
    "label_zh": "步骤",
    "type": "group",
    "parent": null,
    "description_zh": "在 3 个面板中各出现一次，内容相同；这里只记录一次。"
  },
  {
    "id": "s_plan",
    "label_en": "Plan",
    "label_zh": "规划",
    "type": "process",
    "parent": "g_steps",
    "order": 1
  },
  {
    "id": "s_gather",
    "label_en": "Gather Information",
    "label_zh": "收集信息",
    "type": "process",
    "parent": "g_steps",
    "order": 2
  },
  {
    "id": "s_analyze",
    "label_en": "Analyze/Process",
    "label_zh": "分析/处理",
    "type": "process",
    "parent": "g_steps",
    "order": 3
  },
  {
    "id": "s_document",
    "label_en": "Document",
    "label_zh": "记录（文档化）",
    "type": "process",
    "parent": "g_steps",
    "order": 4
  },
  {
    "id": "s_review",
    "label_en": "Review",
    "label_zh": "评审",
    "type": "process",
    "parent": "g_steps",
    "order": 5
  },
  {
    "id": "g_elements",
    "label_en": "Business Scenario elements (color blocks 1–5)",
    "label_zh": "业务场景五要素（色块 1–5）",
    "type": "group",
    "parent": null,
    "description_zh": "图中无此标签；在 3 个面板中各出现一次，内容相同。"
  },
  {
    "id": "e_problem",
    "label_en": "1 - Problem",
    "label_zh": "1 – 问题",
    "type": "requirement",
    "parent": "g_elements",
    "order": 1
  },
  {
    "id": "e_environment",
    "label_en": "2 - Environment",
    "label_zh": "2 – 环境",
    "type": "concept",
    "parent": "g_elements",
    "order": 2
  },
  {
    "id": "e_outcomes",
    "label_en": "3 - Outcomes",
    "label_zh": "3 – 成果",
    "type": "goal",
    "parent": "g_elements",
    "order": 3
  },
  {
    "id": "e_human_actors",
    "label_en": "4 – Human Actors",
    "label_zh": "4 – 人的参与者",
    "type": "actor",
    "parent": "g_elements",
    "order": 4
  },
  {
    "id": "e_computer_actors",
    "label_en": "5 – Computer Actors",
    "label_zh": "5 – 计算机参与者",
    "type": "application",
    "parent": "g_elements",
    "order": 5
  }
]
```

## 关系

```json
[
  {
    "from": "ph_premise",
    "to": "ph_verification",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "面板左右顺序"
  },
  {
    "from": "ph_verification",
    "to": "ph_refinement",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "s_plan",
    "to": "s_gather",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "列表自上而下"
  },
  {
    "from": "s_gather",
    "to": "s_analyze",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "s_analyze",
    "to": "s_document",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "s_document",
    "to": "s_review",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "ph_premise",
    "to": "g_steps",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "面板内包含全部步骤"
  },
  {
    "from": "ph_verification",
    "to": "g_steps",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "ph_refinement",
    "to": "g_steps",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "ph_premise",
    "to": "g_elements",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "该阶段处理并改进全部五要素"
  },
  {
    "from": "ph_verification",
    "to": "g_elements",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "ph_refinement",
    "to": "g_elements",
    "type": "access",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_phases",
    "kind": "sequence",
    "name_zh": "开发阶段",
    "steps": [
      "ph_premise",
      "ph_verification",
      "ph_refinement"
    ],
    "description_zh": "细化阶段结束时判断是否足以交给下游，否则继续细化。"
  },
  {
    "id": "f_steps",
    "kind": "sequence",
    "name_zh": "每个阶段内的步骤",
    "steps": [
      "s_plan",
      "s_gather",
      "s_analyze",
      "s_document",
      "s_review"
    ],
    "description_zh": "在每个阶段中重复执行。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_panels",
    "title_zh": "三个面板逐项转录",
    "columns": [
      "阶段（面板）",
      "步骤（左侧列表）",
      "要素（右侧色块）"
    ],
    "rows": [
      [
        "Premise Formulation Phase 前提形成阶段",
        "Plan；Gather Information；Analyze/Process；Document；Review",
        "1 - Problem；2 - Environment；3 - Outcomes；4 – Human Actors；5 – Computer Actors"
      ],
      [
        "Initial Verification Phase 初步验证阶段",
        "Plan；Gather Information；Analyze/Process；Document；Review",
        "1 - Problem；2 - Environment；3 - Outcomes；4 – Human Actors；5 – Computer Actors"
      ],
      [
        "Refinement Phase 细化阶段",
        "Plan；Gather Information；Analyze/Process；Document；Review",
        "1 - Problem；2 - Environment；3 - Outcomes；4 – Human Actors；5 – Computer Actors"
      ]
    ],
    "notes_zh": "三个面板内容完全相同，只有阶段名不同。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "面板（竖线分隔）",
    "meaning_zh": "一个开发阶段，左到右为先后",
    "explicit": false
  },
  {
    "symbol": "“Steps:” 圆点列表",
    "meaning_zh": "该阶段内执行的步骤，自上而下",
    "explicit": false
  },
  {
    "symbol": "编号色块 1–5（深蓝到绿色）",
    "meaning_zh": "业务场景的五个要素，与图 3-1 相同",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "一个绿色细边框，内部用竖线分成 3 个等宽面板；每个面板顶部是阶段名，左侧是“Steps:”和 5 个圆点步骤，右侧是 5 个自上而下的编号色块（深蓝到绿色）。"
}
```

## 相关图

```json
[
  {
    "target": "G176/fig3-1",
    "relation": "based_on",
    "note_zh": "每个阶段面板右侧重复了图 3-1 的五要素（编号、名称和配色都相同）"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 20 页原图截图（220 dpi）",
    "英文 PDF 第 19、20、24–26 页正文",
    "中文稿 G176e_业务场景.md 第 152–160 行、第 268–297 行",
    "figs/g176_fig3-2.svg 源码"
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
