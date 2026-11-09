# G21H/fig5-1 · O-AA 构建块

> 当前图示解析：[Markdown](../../architecture/diagrams/G21H/fig5-1.md) · [JSON](../../architecture/diagrams/G21H/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21He.pdf`；SHA-256：`40881f73b66ae8cfabc279aba8fe3767182ac3e865823054d0aca58f6292a470`。

## 原图 · PDF 第 39 页

![英文原图](../assets/G21H/fig5-1-p0039.png)

PDF 坐标：`[61.1, 384.4, 550.9, 651.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Architecture Development
Strategy
What the Enterprise
What the Enterprise
“Does”
“Ig”
Experience
Experience
Product
Architecture
Perspective
Design
Value
Journey Maps
Operations
Work System
Value Streams
Architecture
Perspective
Data /
Information
Technical
System
GF oman Jl
Perspective
```

## 概要（历史解释；局部修正见上）

O-AA 构建块按“企业做什么/是什么”两半与体验、工作系统、技术系统三个视角排布，右侧列出三条 O-AA 品质。

## 目的（历史解释；局部修正见上）

第 5.2 节用这张图给出 O-AA 构建块的全景：哪些构建块属于“企业做什么”（面向体验与运营的实践），哪些属于“企业是什么”（产品、运营、组织、治理等结构），它们分别落在体验、工作系统、技术系统三个视角的哪一层，以及 O-AA 强调的三条品质（有意与涌现、并行淘汰弱者、持续可演进可重构）。目的是让数字架构开发者在选配构建块时有共同的地图，而不是给出流程步骤。

## 阅读顺序（历史解释；局部修正见上）

先读顶部标题“Architecture Development”，确认这是架构开发的总图。再看中间的大圆：左半蓝色是 What the Enterprise “Does”，右半绿色是 What the Enterprise “Is”；三条横向虚线自上而下切出 Experience、Work System、Technical System 三个视角，虚线左端有视角名称。圆心偏上是深青色 Value 圆，圆心下方是灰色竖带 Data / Information & AI，底部灰色横条是 Software and Hardware Architecture。最后看右侧三个橙色面板，它们不是构建块，而是 O-AA 的品质说明。

## 关键含义（历史解释；局部修正见上）

- 构建块按两半分工：蓝色“做什么”一侧是 Experience Design、Corporate Brand Identity、Corporate Culture、Journey Maps Value Streams、Event Storming；绿色“是什么”一侧是 Product Architecture、Operations Architecture、Organization、Governance、Domain-Driven Design。
- 三个视角（体验、工作系统、技术系统）横切两半：Experience Design 与 Product Architecture 在体验视角；Journey Maps/Value Streams、Operations Architecture、Corporate Brand Identity、Corporate Culture、Organization、Governance 主要在工作系统视角；Event Storming 与 Domain-Driven Design 在技术系统视角。
- Corporate Brand Identity 与 Corporate Culture 是竖框，跨在工作系统与技术系统两条视角带之间；Organization 与 Governance 也是竖框，同样跨带，说明这些构建块不只属于单一视角。
- Strategy 是顶部中央唯一的灰色框，横跨蓝绿两半；Value 是深青色圆，位于蓝绿分界与体验/工作系统分界的交点，表示价值是两半与多视角的共同焦点。
- Data / Information & AI 是灰色竖带，纵跨工作系统与技术系统，向下与灰色横条 Software and Hardware Architecture 相接；后者位于技术系统带底部，Event Storming 与 Domain-Driven Design 压在它上面，表示软件与硬件架构是技术侧的基底。
- 右侧三个橙色面板是 O-AA 的品质/原则：Intentional & Emergent（两条弧线构成往复）、Concurrent 与 Eliminate the weak（多行平行箭头链，短链提前终止）、Continuous / Evolvable / Refactored（椭圆回路）。它们不是与圆内方块同级的构建块。
- 圆内构建块之间没有任何连线，关系完全由“在左半还是右半、在哪个视角带、在中心还是边缘”表达；这是一张分类地图，不是流程图。
- 正文强调这些构建块之间存在相互依赖，应以敏捷方式管理，以支持数字能力的增量交付和可持续的数字旅程（p39）。

## 层级（历史解释；局部修正见上）

三层。第 1 层是外层“Architecture Development”面板；第 2 层是大圆内的两个半边（What the Enterprise “Does” / “Is”）与三个横向视角带（体验/工作系统/技术系统），二者是交叉分区而非父子；第 3 层是十个构建块方块。Strategy、Value、Data/Information & AI、Software and Hardware Architecture 是跨半边的中心/基底元素，不隶属于某一半边。右侧三个橙色面板与圆内构建块并列，属于品质说明层。

## 线条含义（历史解释；局部修正见上）

圆内没有任何连接线或箭头；三条水平虚线是视角分界线，不是流程线，也没有方向。唯一的箭头在右侧三个橙色面板内：Intentional & Emergent 的两条弧线（左弧向上指向 Intentional，右弧向下指向 Emergent）、Concurrent 面板的 8 行蓝色平行箭头链（每行 1–3 段，长度不一，短链提前终止）、Continuous/Evolvable/Refactored 的椭圆回路（上弧向右、下弧向左）。这些是品质的图标化表达，不是构建块之间的关系。中央灰色 Value—Data/Information & AI—Software and Hardware Architecture 形状相连，但无箭头，本分析按“自下而上支撑”记为隐含关系。

## 易误读点（历史解释；局部修正见上）

- 不要把左蓝右绿读成两个阶段或先后顺序；它是“企业做什么/是什么”的并列二分，两边同时存在。
- 三条水平虚线不是流程线，而是三个视角的分界；同一个构建块可以跨线（企业品牌标识、企业文化、组织、治理都是竖框跨带），不要强行把它归入单一视角。
- 圆心“Value”不是“价值流”（value stream）；它是 O-AA 关注的价值，位置在蓝绿分界与体验/工作系统分界的交点，不要与 Journey Maps Value Streams 中的 value streams 混为一谈。
- 右侧三个橙色面板不是构建块清单，而是 O-AA 的品质/原则；不要把它们当作与 Experience Design、Product Architecture 同级的要素，也不要把面板内的箭头读成构建块之间的依赖。
- “Concurrent / Eliminate the weak”面板的箭头链长度不一是示意“并行推进中弱者被淘汰”，不是精确的进度或数量数据。
- 中文稿的中文化 PNG 把“企业品牌标识/企业文化”缩得几乎不可读，且“消除薄弱环节”“有意图的/涌现的”等译法与标签表不一致；理解本图应以英文原图为准。

## 元素

```json
[
  {
    "id": "arch_dev",
    "label_en": "Architecture Development",
    "label_zh": "架构开发",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "外层浅黄面板的顶部标题",
    "description_zh": "整张图的外框与标题，表示这些构建块用于架构开发。"
  },
  {
    "id": "does_side",
    "label_en": "What the Enterprise “Does”",
    "label_zh": "企业“做什么”",
    "type": "group",
    "parent": "arch_dev",
    "level": 1,
    "position": "大圆左半（蓝色）",
    "description_zh": "原图用弯引号；与右半“是什么”并列。"
  },
  {
    "id": "is_side",
    "label_en": "What the Enterprise “Is”",
    "label_zh": "企业“是什么”",
    "type": "group",
    "parent": "arch_dev",
    "level": 1,
    "position": "大圆右半（绿色）"
  },
  {
    "id": "exp_persp",
    "label_en": "Experience Perspective",
    "label_zh": "体验视角",
    "type": "note",
    "parent": "arch_dev",
    "level": 1,
    "position": "图左外侧，第一条与第二条虚线之间"
  },
  {
    "id": "work_persp",
    "label_en": "Work System Perspective",
    "label_zh": "工作系统视角",
    "type": "note",
    "parent": "arch_dev",
    "level": 1,
    "position": "图左外侧，第二条与第三条虚线之间"
  },
  {
    "id": "tech_persp",
    "label_en": "Technical System Perspective",
    "label_zh": "技术系统视角",
    "type": "note",
    "parent": "arch_dev",
    "level": 1,
    "position": "图左外侧，第三条与第四条虚线之间"
  },
  {
    "id": "strategy",
    "label_en": "Strategy",
    "label_zh": "战略",
    "type": "concept",
    "parent": "arch_dev",
    "level": 1,
    "position": "大圆顶部中央，蓝色与绿色分界线上"
  },
  {
    "id": "value",
    "label_en": "Value",
    "label_zh": "价值",
    "type": "goal",
    "parent": "arch_dev",
    "level": 1,
    "position": "大圆圆心偏上，蓝绿分界与体验/工作系统分界的交点"
  },
  {
    "id": "data_ai",
    "label_en": "Data / Information & AI",
    "label_zh": "数据／信息与 AI",
    "type": "data",
    "parent": "arch_dev",
    "level": 1,
    "position": "圆心下方的灰色竖带，跨工作系统与技术系统两层"
  },
  {
    "id": "sw_hw",
    "label_en": "Software and Hardware Architecture",
    "label_zh": "软件与硬件架构",
    "type": "architecture",
    "parent": "arch_dev",
    "level": 1,
    "position": "技术系统带底部的灰色横条，压在 Event Storming 与 Domain-Driven Design 后面"
  },
  {
    "id": "experience_design",
    "label_en": "Experience Design",
    "label_zh": "体验设计",
    "type": "building_block",
    "parent": "does_side",
    "level": 2,
    "position": "左半体验视角带，靠右"
  },
  {
    "id": "brand_identity",
    "label_en": "Corporate Brand Identity",
    "label_zh": "企业品牌标识",
    "type": "building_block",
    "parent": "does_side",
    "level": 2,
    "position": "左半工作系统带左侧竖框，向下跨到技术系统带上缘"
  },
  {
    "id": "corporate_culture",
    "label_en": "Corporate Culture",
    "label_zh": "企业文化",
    "type": "building_block",
    "parent": "does_side",
    "level": 2,
    "position": "左半工作系统带左侧竖框，紧邻企业品牌标识"
  },
  {
    "id": "journey_maps",
    "label_en": "Journey Maps Value Streams",
    "label_zh": "旅程地图／价值流",
    "type": "building_block",
    "parent": "does_side",
    "level": 2,
    "position": "左半工作系统带中部",
    "description_zh": "原图两行文字，中间没有斜杠；中文稿/标签表写作 Journey Maps / Value Streams。"
  },
  {
    "id": "event_storming",
    "label_en": "Event Storming",
    "label_zh": "事件风暴",
    "type": "building_block",
    "parent": "does_side",
    "level": 2,
    "position": "左半技术系统带，压在灰色 Software and Hardware Architecture 条上"
  },
  {
    "id": "product_arch",
    "label_en": "Product Architecture",
    "label_zh": "产品架构",
    "type": "building_block",
    "parent": "is_side",
    "level": 2,
    "position": "右半体验视角带"
  },
  {
    "id": "operations_arch",
    "label_en": "Operations Architecture",
    "label_zh": "运营架构",
    "type": "building_block",
    "parent": "is_side",
    "level": 2,
    "position": "右半工作系统带"
  },
  {
    "id": "organization",
    "label_en": "Organization",
    "label_zh": "组织",
    "type": "building_block",
    "parent": "is_side",
    "level": 2,
    "position": "右半工作系统带右侧竖框，向下跨到技术系统带上缘"
  },
  {
    "id": "governance",
    "label_en": "Governance",
    "label_zh": "治理",
    "type": "building_block",
    "parent": "is_side",
    "level": 2,
    "position": "右半工作系统带最右侧竖框，紧邻组织"
  },
  {
    "id": "ddd",
    "label_en": "Domain-Driven Design",
    "label_zh": "领域驱动设计",
    "type": "building_block",
    "parent": "is_side",
    "level": 2,
    "position": "右半技术系统带，压在灰色 Software and Hardware Architecture 条上"
  },
  {
    "id": "intentional",
    "label_en": "Intentional",
    "label_zh": "有意的",
    "type": "principle",
    "parent": "arch_dev",
    "level": 1,
    "position": "右侧第一个橙色面板上方"
  },
  {
    "id": "emergent",
    "label_en": "Emergent",
    "label_zh": "涌现的",
    "type": "principle",
    "parent": "arch_dev",
    "level": 1,
    "position": "右侧第一个橙色面板下方"
  },
  {
    "id": "concurrent",
    "label_en": "Concurrent",
    "label_zh": "并行的",
    "type": "principle",
    "parent": "arch_dev",
    "level": 1,
    "position": "右侧第二个橙色面板标题",
    "description_zh": "面板内有 8 行蓝色平行箭头链，每行 1–3 段，长短不一；短链提前终止，表示并行推进中被淘汰的弱者。"
  },
  {
    "id": "eliminate_weak",
    "label_en": "Eliminate the weak",
    "label_zh": "淘汰弱者",
    "type": "note",
    "parent": "arch_dev",
    "level": 2,
    "position": "Concurrent 面板底部说明",
    "description_zh": "中文图写作“消除/薄弱环节”。"
  },
  {
    "id": "continuous_evol_refactor",
    "label_en": "Continuous / Evolvable / Refactored",
    "label_zh": "持续／可演进／可重构",
    "type": "principle",
    "parent": "arch_dev",
    "level": 1,
    "position": "右侧第三个橙色面板，三词自上而下排列",
    "description_zh": "面板内有一个椭圆回路（上弧箭头向右、下弧箭头向左），把 Evolvable 围在中间；中文图写作“持续/可演进/重构”。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_emergent_intentional",
    "from": "emergent",
    "to": "intentional",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "Intentional & Emergent 面板左侧的弧线，箭头向上指向 Intentional。"
  },
  {
    "id": "r_intentional_emergent",
    "from": "intentional",
    "to": "emergent",
    "type": "iteration",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同一面板右侧的弧线，箭头向下指向 Emergent；两条弧线构成往复。"
  },
  {
    "id": "r_concurrent_eliminate",
    "from": "concurrent",
    "to": "eliminate_weak",
    "type": "other",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_zh": "淘汰弱者",
    "description_zh": "面板内 8 行平行箭头链表示并行推进的多条举措，短链提前终止；下方的 Eliminate the weak 是对这一图标的说明，不是独立的构建块。箭头链本身没有指向具体要素，故只记面板到说明文字的关系。"
  },
  {
    "id": "r_sw_data",
    "from": "sw_hw",
    "to": "data_ai",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "灰色横条与灰色竖带在底部相接、无箭头；按支撑关系推断为软件与硬件架构支撑数据/信息与 AI。"
  },
  {
    "id": "r_data_value",
    "from": "data_ai",
    "to": "value",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "灰色竖带上端与 Value 圆相接、无箭头；按支撑关系推断为数据/信息与 AI 支撑价值。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "左半蓝色区域",
    "meaning_zh": "What the Enterprise “Does”（企业做什么）的构建块",
    "explicit": true
  },
  {
    "symbol": "右半绿色区域",
    "meaning_zh": "What the Enterprise “Is”（企业是什么）的构建块",
    "explicit": true
  },
  {
    "symbol": "三条水平虚线 + 左侧斜体标签",
    "meaning_zh": "Experience / Work System / Technical System 三个视角的分界",
    "explicit": true
  },
  {
    "symbol": "灰色 Strategy 框",
    "meaning_zh": "横跨两半的战略构建块",
    "explicit": false
  },
  {
    "symbol": "深青色 Value 圆",
    "meaning_zh": "O-AA 关注的价值，位于两半与视角分界的交点",
    "explicit": false
  },
  {
    "symbol": "灰色竖带 Data / Information & AI",
    "meaning_zh": "跨工作系统与技术系统视角的横切数据/信息与 AI 能力",
    "explicit": false
  },
  {
    "symbol": "灰色横条 Software and Hardware Architecture",
    "meaning_zh": "技术系统带底部的软件与硬件架构基底",
    "explicit": false
  },
  {
    "symbol": "橙色面板 + 弧形/直线箭头图标",
    "meaning_zh": "O-AA 品质/原则的图标化说明，不是构建块之间的关系",
    "explicit": true
  },
  {
    "symbol": "蓝色水平箭头链（8 行，长短不一）",
    "meaning_zh": "并行推进的多条举措；短链提前终止表示弱者被淘汰（Eliminate the weak）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "左侧约八成宽度是一个大圆：蓝左半、绿右半，三条水平虚线切成三个视角带；圆顶中央压着灰色 Strategy 框，圆心是深青色 Value 圆，圆下方是灰色竖带 Data / Information & AI，圆底是灰色横条 Software and Hardware Architecture；十个彩色方块分布在两半与各视角带。右侧一列三个橙色面板自上而下为 Intentional & Emergent、Concurrent/Eliminate the weak、Continuous/Evolvable/Refactored。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "右侧三个橙色面板内的箭头是 O-AA 品质的图标化表达；Intentional/Emergent 的往复可拆成两条箭头，Concurrent 的 8 行箭头链没有具体端点，Continuous/Evolvable/Refactored 的椭圆回路也没有拆成三节点循环，均按图标语义记录而非强行造要素间连线。",
    "Value、Data/Information & AI、Software and Hardware Architecture 三者之间的灰色形状相连但无箭头；本分析按自下而上的支撑关系记为隐含关系，方向为推断。",
    "Corporate Brand Identity/Culture 与 Organization/Governance 的竖框跨越视角分界，具体归属哪个视角带存在歧义；本分析只按左/右半归属，视角位置写入 position。",
    "三个橙色面板的字号、斜体与箭头细节在原图中较小，个别箭头端点（尤其 Intentional 面板上方）不易辨认。"
  ],
  "analyzed_from": [
    "英文 PDF 第 39 页 figure 截图（220 dpi）与 600 dpi 局部放大（三个橙色面板）",
    "英文 PDF 第 39 页正文",
    "中文稿 G21He_TOGAF数字业务参考模型.md 第 541–578 行（含图内标签对照表）",
    "figs/g21he_fig5-1_en.png 与 figs/zh/g21he_fig5-1_zh.png 目视比较"
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
