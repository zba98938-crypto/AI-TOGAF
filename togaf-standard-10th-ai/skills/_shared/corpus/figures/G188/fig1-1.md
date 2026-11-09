# G188/fig1-1 · 架构项目与 TOGAF ADM 的关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G188/fig1-1.md) · [JSON](../../architecture/diagrams/G188/fig1-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G188e.pdf`；SHA-256：`6e654af12a0bc034c7548d425a01123331ac9129c478a0bb957db89dd353dd29`。

## 原图 · PDF 第 16 页

![英文原图](../assets/G188/fig1-1-p0016.png)

PDF 坐标：`[125.6, 36.0, 486.4, 306.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Architecture Project
omc coe
```

## 概要（历史解释；局部修正见上）

用 ADM 圆盘标出架构项目的范围：阶段 A–F 加需求管理在项目内，预备阶段、G、H 在项目外。

## 目的（历史解释；局部修正见上）

为“架构项目”下操作性定义：作者不按 TOGAF 术语而按项目边界来界定，用一张 ADM 图直观说明哪些 ADM 活动属于架构项目、哪些不属于，从而为后文按项目管理方法管理 A–F 奠定范围基础。

## 阅读顺序（历史解释；局部修正见上）

先看中心：需求管理是贯穿各阶段的中心活动。再沿圆周按 A→B→C→D→E→F→G→H→A 的顺序读八个阶段（图中只有连线、没有箭头，循环方向来自 ADM 常识）。最后看浅蓝色不规则的“Architecture Project”轮廓：它把 A–F 与中心需求管理包在一起，预备阶段、G、H 落在轮廓之外。

## 关键含义（历史解释；局部修正见上）

- 架构项目 = ADM 阶段 A 至 F + 需求管理；这是本文档对“架构项目”的工作定义，而非 TOGAF 标准术语。
- 预备阶段在项目之外：它建立企业的架构能力，其输出（尤其是架构工作请求）作为架构项目的输入。
- 阶段 G（实施治理）在项目之外：它治理架构的实施，通常作为另一个项目或项目群运行。
- 阶段 H（架构变更管理）在项目之外：它维护已实施的架构，属于运营业务/流程而非项目管理。
- 需求管理位于圆心，用放射线与八个阶段相连，表示它贯穿整个 ADM 周期，而不是一个前后相继的阶段。
- 阶段 A–F 首尾相接成环，说明架构项目虽然在 F 结束，但 ADM 本身是循环的；架构项目只是其中的一段。

## 层级（历史解释；局部修正见上）

两层视觉结构：外层是 ADM 的九个圆（预备 + A–H）加中心的需求管理；内层是浅蓝色“Architecture Project”范围轮廓，包住 A–F 与需求管理。图中没有组织上下级，只有范围包含（轮廓）与连接（圆之间细线）。

## 线条含义（历史解释；局部修正见上）

细灰线连接相邻阶段（A–B、B–C……H–A）以及预备阶段–A，表示 ADM 的阶段顺序；中心需求管理向八个阶段各发一条放射线，表示需求管理贯穿每个阶段。所有线都没有箭头，方向由 ADM 的循环阅读习惯给出。浅蓝轮廓是范围边界，不是连线。

## 易误读点（历史解释；局部修正见上）

- 不要把浅蓝色轮廓理解为“架构项目包含 G/H”：G、H 画在轮廓外，颜色也更亮（表示范围外）。
- 不要以为需求管理是第九个阶段；它在圆心，与所有阶段相连，是贯穿性活动。
- 图中没有箭头，不能据此判断阶段之间的严格先后或迭代次数；ADM 实际是迭代执行的。
- 中文稿当前引用的 figs/g188_fig1-1.svg 用虚线圆表示范围，但圆没有包住 A 和 H，且只留字母，不能据它判断项目边界。

## 元素

```json
[
  {
    "id": "arch_project",
    "label_en": "Architecture Project",
    "label_zh": "架构项目",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "浅蓝色不规则轮廓，覆盖中右部",
    "description_zh": "范围边界，不是一个阶段；轮廓内为 A–F 与需求管理。"
  },
  {
    "id": "preliminary",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": null,
    "level": 1,
    "position": "顶部，A 正上方",
    "description_zh": "在架构项目范围之外。"
  },
  {
    "id": "phase_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": "arch_project",
    "level": 1,
    "order": 1
  },
  {
    "id": "phase_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": "arch_project",
    "level": 1,
    "order": 2
  },
  {
    "id": "phase_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": "arch_project",
    "level": 1,
    "order": 3
  },
  {
    "id": "phase_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": "arch_project",
    "level": 1,
    "order": 4
  },
  {
    "id": "phase_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": "arch_project",
    "level": 1,
    "order": 5
  },
  {
    "id": "phase_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": "arch_project",
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
    "order": 7,
    "description_zh": "在架构项目范围之外。"
  },
  {
    "id": "phase_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 8,
    "description_zh": "在架构项目范围之外。"
  },
  {
    "id": "requirements_management",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "phase",
    "parent": "arch_project",
    "level": 1,
    "position": "圆心",
    "description_zh": "贯穿性活动，与八个阶段都有连接。"
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
    "description_zh": "预备阶段位于 A 上方并以细线相连，表示 ADM 从预备进入 A"
  },
  {
    "from": "phase_a",
    "to": "phase_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_b",
    "to": "phase_c",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_c",
    "to": "phase_d",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_d",
    "to": "phase_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_e",
    "to": "phase_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "phase_f",
    "to": "phase_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
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
    "description_zh": "闭合 ADM 圆环的连线"
  },
  {
    "from": "phase_a",
    "to": "requirements_management",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "需求管理放射线之一，表示需求贯穿阶段 A"
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
    "from": "arch_project",
    "to": "phase_a",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "浅蓝轮廓包住该阶段，表示其在架构项目范围内"
  },
  {
    "from": "arch_project",
    "to": "phase_b",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "浅蓝轮廓包住该阶段，表示其在架构项目范围内"
  },
  {
    "from": "arch_project",
    "to": "phase_c",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "浅蓝轮廓包住该阶段，表示其在架构项目范围内"
  },
  {
    "from": "arch_project",
    "to": "phase_d",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "浅蓝轮廓包住该阶段，表示其在架构项目范围内"
  },
  {
    "from": "arch_project",
    "to": "phase_e",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "浅蓝轮廓包住该阶段，表示其在架构项目范围内"
  },
  {
    "from": "arch_project",
    "to": "phase_f",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "浅蓝轮廓包住该阶段，表示其在架构项目范围内"
  },
  {
    "from": "arch_project",
    "to": "phase_g",
    "type": "contrast",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "G 与 H 位于轮廓之外，表示不在项目范围内"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_adm",
    "kind": "cycle",
    "name_zh": "ADM 循环（图中只画到 H，再回到 A）",
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
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色不规则轮廓 + 青色文字 Architecture Project",
    "meaning_zh": "架构项目的范围边界（包住 A–F 与需求管理）",
    "explicit": true
  },
  {
    "symbol": "亮黄色圆（Preliminary、G、H）",
    "meaning_zh": "不在架构项目范围内的 ADM 阶段",
    "explicit": false
  },
  {
    "symbol": "浅黄色圆（A–F）",
    "meaning_zh": "在架构项目范围内的 ADM 阶段",
    "explicit": false
  },
  {
    "symbol": "深琥珀色大圆（Requirements Management）",
    "meaning_zh": "贯穿所有阶段的需求管理",
    "explicit": false
  },
  {
    "symbol": "细灰线",
    "meaning_zh": "阶段相邻关系/需求管理与各阶段的连接，无箭头",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "以需求管理为圆心，八个 ADM 阶段按 A（上）→B（右上）→C（右）→D（右下）→E（下）→F（左下）→G（左）→H（左上）排成圆环；预备阶段位于 A 正上方、圆环之外。浅蓝色不规则轮廓从 A 外缘起，绕过 B–F，把中心与 A–F 围住，G、H 留在轮廓左侧之外。"
}
```

## 相关图

```json
[
  {
    "target": "G188/fig2-2",
    "relation": "overview_of",
    "note_zh": "图 2-2 在同一 ADM 圆盘上展开项目阶段与迭代回路，本图只给项目范围"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图圆环上 H 与 A 之间的连线被浅蓝轮廓遮挡，是否表示从 H 返回 A 只能按 ADM 常识判断；本分析记为闭环连线。",
    "中文稿所附 SVG 的虚线圆半径与节点位置不一致，本文按英文原图判断范围，未采用 SVG 的边界。"
  ],
  "analyzed_from": [
    "英文 PDF 第 16 页原图截图（含 2x2 放大分块）",
    "英文 PDF 第 16 页正文",
    "中文稿 G188e_架构项目管理.md 第 89–100 行",
    "figs/g188_fig1-1.svg 源码"
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
