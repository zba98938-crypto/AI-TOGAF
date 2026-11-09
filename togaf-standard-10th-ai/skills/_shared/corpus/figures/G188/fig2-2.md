# G188/fig2-2 · 架构项目生命周期（从 TOGAF ADM 视角）

> 当前图示解析：[Markdown](../../architecture/diagrams/G188/fig2-2.md) · [JSON](../../architecture/diagrams/G188/fig2-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G188e.pdf`；SHA-256：`6e654af12a0bc034c7548d425a01123331ac9129c478a0bb957db89dd353dd29`。

## 原图 · PDF 第 24 页

![英文原图](../assets/G188/fig2-2-p0024.png)

PDF 坐标：`[99.8, 36.0, 512.2, 345.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Capabil
Architecture
ce, Monitor, and Contry
\
ctwcare
lopment
Architecture
eration
al
{-
‘\
a
Transition
NS
Se.
68S eenvon puesowvon Fo
```

## 概要（历史解释；局部修正见上）

把架构项目生命周期叠在 ADM 圆盘上：每个 ADM 阶段边界做阶段收尾与下一阶段规划，外环持续执行监控，并有四类迭代回路。

## 目的（历史解释；局部修正见上）

说明“架构项目生命周期”不是一条直线，而是与 ADM 阶段叠合、可迭代的循环：项目启动对应预备到 A 之间，项目收尾对应 F 之后，阶段规划/执行监控/阶段收尾在每个 ADM 阶段边界重复，并用四个回路指出能力、开发、过渡规划与治理各自的迭代范围。

## 阅读顺序（历史解释；局部修正见上）

从顶部 Preliminary 开始，顺时针读 A→B→C→D→E→F→G→H。每个阶段圆之间的青绿色双带是阶段边界：左边一条“Ending a Stage”，右边一条“Planning a Stage”。最外圈黄色环是项目层活动：H 与 A 之间是 Architecture Project Starting，F 与 G 之间是 Architecture Project Closing，其余四段反复写 Execute, Monitor, and Control a Stage。再看深灰色闭合箭头：它们标出四个迭代回路，箭头方向表示回路回到起点。

## 关键含义（历史解释；局部修正见上）

- 架构项目阶段与 ADM 阶段不是一一对应：图中为简化才让每个项目阶段对应一个 ADM 阶段；正文明确多数情况下不应如此，一个阶段可覆盖多个 ADM 阶段并重复执行。
- 阶段边界是双向活动：结束当前阶段（Ending a Stage）之后紧接规划下一阶段（Planning a Stage），因此每个边界画成两条并排的青绿色带。
- 外环的 Execute, Monitor, and Control a Stage 沿圆周重复出现，表示执行监控不是某个阶段的专属步骤，而是贯穿整个项目阶段环。
- 项目启动发生在进入阶段 A 之前（H 与 A 之间的黄色扇区），项目收尾发生在阶段 F 之后（F 与 G 之间的黄色扇区）；G、H 仍画在圆盘上，但属于项目实施/运营侧。
- 四个迭代回路各有范围：能力迭代在预备与 A 之间，开发迭代覆盖 B–F，过渡规划迭代在 E–F，治理迭代在 G/H 与需求管理一侧；说明不同管理问题在不同粒度上循环。
- 需求管理位于圆心并与各阶段相连，是贯穿所有阶段与所有迭代的公共活动。

## 层级（历史解释；局部修正见上）

三层同心结构：最内是中心需求管理；中间是八个 ADM 阶段圆（外加顶部的预备阶段）；最外是黄色项目阶段环与青绿色阶段边界带。项目启动/收尾是外环上的两个扇区，不是独立阶段圆。四个迭代回路是叠加在圆盘上的标注，不构成层级。

## 线条含义（历史解释；局部修正见上）

阶段圆之间的细灰线表示 ADM 相邻阶段关系；中心到各阶段的放射线表示需求管理贯穿；青绿色径向双带表示阶段边界（Ending/Planning）；黄色外环的弧段表示项目层活动；深灰色带箭头的闭合曲线表示迭代回路，箭头指向回路的下一个位置。所有阶段连接线本身无箭头，循环方向由顺时针阅读给出。

## 易误读点（历史解释；局部修正见上）

- 不要把青色“Ending a Stage / Planning a Stage”带理解为 ADM 阶段之间的额外阶段；它是每个阶段边界处要做的两项管理活动。
- 不要以为项目阶段一定等于 ADM 阶段；原图注明这是简化假设。
- 不要把 G、H 排除在圆盘之外：它们仍属于 ADM 循环，只是在架构项目范围之外（见图 1-1）。
- 中文稿引用的 figs/g188_fig2-2.svg 是线性六步图，没有圆盘、阶段边界带和四个迭代回路，不能据它理解本图。

## 元素

```json
[
  {
    "id": "preliminary",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": null,
    "level": 1,
    "position": "顶部"
  },
  {
    "id": "phase_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 1
  },
  {
    "id": "phase_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 2
  },
  {
    "id": "phase_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 3
  },
  {
    "id": "phase_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 4
  },
  {
    "id": "phase_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 5
  },
  {
    "id": "phase_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 6
  },
  {
    "id": "phase_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 7
  },
  {
    "id": "phase_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 8
  },
  {
    "id": "requirements_management",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "position": "圆心"
  },
  {
    "id": "project_starting",
    "label_en": "Architecture Project Starting",
    "label_zh": "架构项目启动",
    "type": "phase",
    "parent": null,
    "level": 0,
    "position": "外环左上方扇区（H 与 A 之间）",
    "description_zh": "项目层活动，位于进入阶段 A 之前。"
  },
  {
    "id": "project_closing",
    "label_en": "Architecture Project Closing",
    "label_zh": "架构项目收尾",
    "type": "phase",
    "parent": null,
    "level": 0,
    "position": "外环左下方扇区（F 与 G 之间）"
  },
  {
    "id": "execute_monitor_control",
    "label_en": "Execute, Monitor, and Control a Stage",
    "label_zh": "执行、监控与控制阶段",
    "type": "phase",
    "parent": null,
    "level": 0,
    "position": "外环上重复四次（上、右、下、左下）",
    "description_zh": "项目层活动，沿外环重复出现，表示贯穿各阶段。"
  },
  {
    "id": "stage_boundary",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段",
    "type": "note",
    "parent": null,
    "position": "每个阶段圆之间的青绿色径向双带",
    "description_zh": "同一组标签在 Preliminary–A、A–B、B–C、C–D、D–E、E–F 之间重复；F–G 之间只见 Ending a Stage。"
  },
  {
    "id": "architecture_capability_iteration",
    "label_en": "Architecture Capability Iteration",
    "label_zh": "架构能力迭代",
    "type": "note",
    "parent": null,
    "position": "左上方，Preliminary 与 A 之间",
    "description_zh": "回路标注，对应深灰闭合箭头。"
  },
  {
    "id": "architecture_development_iteration",
    "label_en": "Architecture Development Iteration",
    "label_zh": "架构开发迭代",
    "type": "note",
    "parent": null,
    "position": "右上方，B–F 外侧",
    "description_zh": "大回路覆盖 B–F。"
  },
  {
    "id": "transition_planning_iteration",
    "label_en": "Transition Planning Iteration",
    "label_zh": "过渡规划迭代",
    "type": "note",
    "parent": null,
    "position": "左下方，E–F 外侧"
  },
  {
    "id": "architecture_governance_iteration",
    "label_en": "Architecture Governance Iteration",
    "label_zh": "架构治理迭代",
    "type": "note",
    "parent": null,
    "position": "左侧，H/G 与需求管理之间"
  }
]
```

## 关系

```json
[
  {
    "from": "preliminary",
    "to": "phase_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段",
    "description_zh": "两圆之间的青绿色双带"
  },
  {
    "from": "phase_a",
    "to": "phase_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段"
  },
  {
    "from": "phase_b",
    "to": "phase_c",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段"
  },
  {
    "from": "phase_c",
    "to": "phase_d",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段"
  },
  {
    "from": "phase_d",
    "to": "phase_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段"
  },
  {
    "from": "phase_e",
    "to": "phase_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage / Planning a Stage",
    "label_zh": "阶段收尾 / 规划阶段"
  },
  {
    "from": "phase_f",
    "to": "phase_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_en": "Ending a Stage",
    "label_zh": "阶段收尾",
    "description_zh": "该边界只有一条收尾带，随后进入项目收尾扇区"
  },
  {
    "from": "phase_g",
    "to": "phase_h",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_h",
    "to": "phase_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "闭合 ADM 圆环；外侧为项目启动扇区"
  },
  {
    "from": "phase_a",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_b",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_c",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_d",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_e",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_f",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_g",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_h",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "project_starting",
    "to": "phase_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "外环扇区由 H→A 方向延伸至阶段 A，表示项目在 A 前启动"
  },
  {
    "from": "phase_f",
    "to": "project_closing",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "项目收尾扇区位于 F 之后"
  },
  {
    "from": "project_starting",
    "to": "phase_a",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Architecture Capability Iteration",
    "label_zh": "架构能力迭代",
    "description_zh": "左上闭合回路，从预备阶段绕到 A 再返回"
  },
  {
    "from": "phase_b",
    "to": "phase_f",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Architecture Development Iteration",
    "label_zh": "架构开发迭代",
    "description_zh": "大回路沿 B–F 绕行后回到 B"
  },
  {
    "from": "phase_e",
    "to": "phase_f",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Transition Planning Iteration",
    "label_zh": "过渡规划迭代"
  },
  {
    "from": "phase_h",
    "to": "phase_g",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Architecture Governance Iteration",
    "label_zh": "架构治理迭代",
    "description_zh": "左侧闭合回路，围绕 G/H 与需求管理一侧"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_adm",
    "kind": "cycle",
    "name_zh": "ADM 循环",
    "steps": [
      "preliminary",
      "phase_a",
      "phase_b",
      "phase_c",
      "phase_d",
      "phase_e",
      "phase_f",
      "phase_g",
      "phase_h",
      "phase_a"
    ]
  },
  {
    "id": "f_capability_iter",
    "kind": "loop",
    "name_zh": "架构能力迭代",
    "steps": [
      "preliminary",
      "phase_a",
      "preliminary"
    ]
  },
  {
    "id": "f_development_iter",
    "kind": "loop",
    "name_zh": "架构开发迭代（B–F）",
    "steps": [
      "phase_b",
      "phase_c",
      "phase_d",
      "phase_e",
      "phase_f",
      "phase_b"
    ]
  },
  {
    "id": "f_transition_iter",
    "kind": "loop",
    "name_zh": "过渡规划迭代",
    "steps": [
      "phase_e",
      "phase_f",
      "phase_e"
    ]
  },
  {
    "id": "f_governance_iter",
    "kind": "loop",
    "name_zh": "架构治理迭代",
    "steps": [
      "phase_h",
      "phase_g",
      "phase_h"
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色阶段圆",
    "meaning_zh": "ADM 阶段（Preliminary、A–H）",
    "explicit": false
  },
  {
    "symbol": "深琥珀色中心圆",
    "meaning_zh": "贯穿各阶段的需求管理",
    "explicit": false
  },
  {
    "symbol": "灰色圆盘底面",
    "meaning_zh": "ADM 与项目阶段共同覆盖的范围",
    "explicit": false
  },
  {
    "symbol": "青绿色径向双带（Ending a Stage / Planning a Stage）",
    "meaning_zh": "阶段边界：收尾当前阶段并规划下一阶段",
    "explicit": true
  },
  {
    "symbol": "黄色外环弧段 + 文字",
    "meaning_zh": "项目层活动：项目启动、执行监控、项目收尾",
    "explicit": true
  },
  {
    "symbol": "深灰色闭合箭头",
    "meaning_zh": "迭代回路（能力/开发/过渡规划/治理）",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "ADM 圆盘：Preliminary 在顶部，A 在其下，B–H 顺时针环绕，Requirements Management 居中。圆盘外是黄色圆环，被青绿色径向分界带切成扇段；H→A 方向的外环段写 Architecture Project Starting，F→G 方向写 Architecture Project Closing，其余外环反复写 Execute, Monitor, and Control a Stage。四个深灰闭合箭头分布在左上、右上、左下、左中。"
}
```

## 相关图

```json
[
  {
    "target": "G188/fig1-1",
    "relation": "detail_of",
    "note_zh": "图 1-1 只标架构项目在 ADM 中的阶段范围；本图在同一圆盘上展开项目阶段、阶段边界与迭代回路"
  },
  {
    "target": "G188/fig3-1",
    "relation": "complements",
    "note_zh": "图 3-1 用线性方框重述本图的六个生命周期活动"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "外环“Execute, Monitor, and Control a Stage”在圆周上重复四次，具体起止角度因文字沿弧线排布难以精确判断，本文按四个弧段记录。",
    "F–G 边界处只看到一条“Ending a Stage”带，另一条“Planning a Stage”被项目收尾扇区取代；原图较小，无法完全排除还有被遮挡的带。",
    "四个迭代回路的具体起止节点按箭头与位置判断，回路在圆盘上互相交叠，起止点可能有半个节点的误差。"
  ],
  "analyzed_from": [
    "英文 PDF 第 24 页原图截图（含 2x2 与 3x3 放大分块）",
    "英文 PDF 第 23–24 页正文",
    "中文稿 G188e_架构项目管理.md 第 197–228 行",
    "figs/g188_fig2-2.svg 文本内容"
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
