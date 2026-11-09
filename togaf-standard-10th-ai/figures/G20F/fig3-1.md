# G20F/fig3-1 · TOGAF ADM

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig3-1.md) · [JSON](../../architecture/diagrams/G20F/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 18 页

![英文原图](../assets/G20F/fig3-1-p0018.png)

PDF 坐标：`[156.0, 158.5, 456.0, 557.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
A.
Architecture
Vision
H.
Architecture
B.
Business
Change
Architecture
Management
Cc.
G
Information
Implementation
Requirements
Governance
Management
Systems
Architectures
F.
D.
Migration
Technology
Architecture
Planning
[=
Opportunities
and
Solutions
The Open Group
```

## 概要（历史解释；局部修正见上）

TOGAF ADM 的经典轮盘：预备阶段加 A–H 八个阶段围绕中心的需求管理循环展开。

## 目的（历史解释；局部修正见上）

第 3 章开篇用来引出 ADM。作者先承认这张“标志性图形”会让人以为企业架构是漫长的瀑布过程，随即用三条“ADM 并不……”否定这种误读，为全书“按敏捷需要裁剪 ADM”的主张建立前提。

## 阅读顺序（历史解释；局部修正见上）

从顶部的 Preliminary 圆点出发，沿竖线向下进入 A；然后顺时针沿圆周经过 B、C、D、E、F、G、H，再回到 A 开始新一轮。中心较大的 Requirements Management 用辐射线连到每个阶段，表示它贯穿整个循环而不是一个独立阶段。

## 关键含义（历史解释；局部修正见上）

- 圆周上只有阶段名称与连接线：没有任何箭头、时间刻度、工期或“完成才能进入下一阶段”的闸门，所以图本身并不表达瀑布过程。
- Preliminary 画在圆周之外、位于顶端，用一条线接入 A，表示预备阶段为后续所有架构工作建立能力与语境。
- 中心的 Requirements Management 连到全部 8 个阶段，表示需求在每一阶段都被持续管理。
- 圆周闭合表示 ADM 是迭代循环：H（架构变更管理）之后回到 A 开始新一轮架构开发。
- 图中阶段 A–H 的顺序只是编号与相邻关系，正文明确说明不强制按图示顺序执行、不强制瀑布、不规定任何阶段的时长。
- 正文建议按企业需要裁剪 ADM，敏捷性就是其中一种需要；中文稿进一步把该图定位为“参考模型”而非过程模型。

## 层级（历史解释；局部修正见上）

两层：外层是 Preliminary 与 A–H 共 9 个阶段，构成一个闭合环；内层中心是 Requirements Management，与 8 个阶段平级相连（不是上级）。阶段之间没有上下级，只有环形相邻关系。

## 线条含义（历史解释；局部修正见上）

无箭头。圆周上的实线表示阶段相邻（阅读方向顺时针），Preliminary 到 A 的竖线表示预备阶段之后进入架构愿景；中心到 8 个阶段的 8 条辐射线表示需求管理服务于每个阶段。线的粗细与颜色一致，没有强弱或优先级含义。

## 易误读点（历史解释；局部修正见上）

- 不要把圆周读成“必须按 A→H 顺序、逐个阶段完成”的瀑布流程——正文用三条“TOGAF ADM does not…”明确否定这一点。
- 不要以为图中有工期或迭代节奏信息；图中没有任何时间刻度，阶段时长未被规定。
- 不要以为 Requirements Management 是第 9 个阶段或独立于 A–H 的流程；它在中心，作用于所有阶段。
- Preliminary 不在圆周上，这表示它不属于 A–H 的循环本身，而是循环开始前的准备。

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
    "order": 0,
    "position": "顶部中央，圆周之外"
  },
  {
    "id": "phase_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "圆周顶部，Preliminary 正下方"
  },
  {
    "id": "phase_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "圆周右上"
  },
  {
    "id": "phase_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "圆周右侧中部"
  },
  {
    "id": "phase_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "圆周右下"
  },
  {
    "id": "phase_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 5,
    "position": "圆周底部"
  },
  {
    "id": "phase_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 6,
    "position": "圆周左下"
  },
  {
    "id": "phase_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 7,
    "position": "圆周左侧中部"
  },
  {
    "id": "phase_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "order": 8,
    "position": "圆周左上"
  },
  {
    "id": "requirements_management",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "process",
    "parent": null,
    "level": 1,
    "position": "环心，橙色大圆",
    "description_zh": "贯穿 A–H 的持续活动，不是独立阶段。"
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
    "description_zh": "预备阶段之后进入架构愿景"
  },
  {
    "from": "phase_a",
    "to": "phase_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "圆周相邻，顺时针"
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
    "description_zh": "闭合圆周：H 之后回到 A 开始新一轮"
  },
  {
    "from": "requirements_management",
    "to": "phase_a",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "中心辐射线，需求管理服务于该阶段"
  },
  {
    "from": "requirements_management",
    "to": "phase_b",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "requirements_management",
    "to": "phase_c",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "requirements_management",
    "to": "phase_d",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "requirements_management",
    "to": "phase_e",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "requirements_management",
    "to": "phase_f",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "requirements_management",
    "to": "phase_g",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "requirements_management",
    "to": "phase_h",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_adm_cycle",
    "kind": "cycle",
    "name_zh": "TOGAF ADM 循环",
    "steps": [
      "preliminary",
      "phase_a",
      "phase_b",
      "phase_c",
      "phase_d",
      "phase_e",
      "phase_f",
      "phase_g",
      "phase_h"
    ],
    "description_zh": "预备阶段准备之后，A→H 循环推进并回到 A；正文强调这只是参考顺序，可裁剪、可并行。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色圆形节点",
    "meaning_zh": "ADM 的一个阶段（Preliminary 或 A–H）",
    "explicit": false
  },
  {
    "symbol": "橙色较大圆形节点",
    "meaning_zh": "中心的需求管理，作用于所有阶段",
    "explicit": false
  },
  {
    "symbol": "圆周实线",
    "meaning_zh": "相邻阶段的连接，顺时针为阅读方向",
    "explicit": false
  },
  {
    "symbol": "由中心向外的实线",
    "meaning_zh": "需求管理贯穿并服务于该阶段",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "Preliminary 在最上方，A 在其正下方；B–H 沿一个椭圆环顺时针分布（B 右上、C 右、D 右下、E 下、F 左下、G 左、H 左上）；Requirements Management 位于环心，圆比其余 8 个更大且为橙色。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig4-3",
    "relation": "basis_for",
    "note_zh": "图 4-3 把同一个 ADM 轮盘复制三份（战略/分段/能力），用箭头表示层级间的驱动关系。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "中文稿没有引用图 3-1，也没有给出中文图题，标题按英文 Figure 3-1 直译。",
    "中心辐射线是否表示“服务”而非单纯的关联，属于依据 TOGAF 惯例的解读（图中无文字说明）。"
  ],
  "analyzed_from": [
    "英文 PDF 第 18 页原图截图（figctx GT crop，含 2x2 放大块）",
    "英文 PDF 第 18 页正文",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 152–179 行"
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
