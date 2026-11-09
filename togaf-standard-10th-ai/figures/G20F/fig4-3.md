# G20F/fig4-3 · ADM 过程层级示例

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig4-3.md) · [JSON](../../architecture/diagrams/G20F/fig4-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G20F/fig4-3-p0023.png)

PDF 坐标：`[118.5, 36.0, 493.5, 577.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
‘Segment Architecture
we
i
|
\
ili
ve
N
a
S
Or
ul
ae
A
```

## 概要（历史解释；局部修正见上）

同一套 ADM 在三层重复执行：战略架构轮驱动多个分段架构轮，再驱动多个能力架构轮。

## 目的（历史解释；局部修正见上）

回答 4.3 节的问题：多层级架构方法在实践中怎么落地。答案是“ADM 循环的层级”——每一层都完整跑一遍 A–H，上层轮盘的产出成为下层轮盘的输入，从而既能并行又能保持对齐。

## 阅读顺序（历史解释；局部修正见上）

先看三个面板的标题定位层级：右上是 Strategic Architecture，左侧是 Segment Architecture，右下是 Capability Architecture。每个面板内是一个与图 3-1 相同的小 ADM 轮盘，从 Preliminary 进入 A，顺时针到 H。然后顺着长曲线箭头读层级关系：战略轮下方引出的箭头指向分段面板（其中一条直接指入分段的 A），分段轮下方引出的箭头再指向能力面板。

## 关键含义（历史解释；局部修正见上）

- 三个层级各自跑一个完整 ADM：图中三份轮盘都含 Preliminary、A–H 与中心的 Requirements Management。
- 战略架构轮圆盘最大、在最外层，分段与能力轮盘依次缩小并向内/向下排布，表示详细程度递增、覆盖范围递减。
- 一个战略架构可以驱动多个分段架构：分段面板带层叠阴影，且正文说不同分段与能力的工作可并行推进。
- 能力架构同样可有多份并行（面板带层叠阴影），对应正文“多个能力架构可并行开发”。
- 箭头都指向阶段 A：每个下层 ADM 循环从架构愿景开始，而不是从中间阶段接续。
- 正文强调阶段不必按序推进：分段架构活动一旦在战略架构中识别出相关领域即可开始，能力架构也不必等所有分段架构完成。
- 反向的经验反馈在图中没有画成箭头，只在正文说明：能力架构的经验应影响分段架构，分段架构的经验应影响战略架构。

## 层级（历史解释；局部修正见上）

三层：Strategic Architecture（最高、最概括）→ Segment Architecture（中层，可多份并行）→ Capability Architecture（最低、最细，可多份并行）。每层内部是一个 ADM 环：Preliminary 在环外顶部，A–H 在圆周上，Requirements Management 在中心并连到 A–H。

## 线条含义（历史解释；局部修正见上）

每个轮盘内部的实线表示阶段相邻与需求管理的辐射关系（无箭头，与图 3-1 相同）。轮盘之间的长曲线箭头表示上层驱动下层：从战略轮下方引出的两条箭头落在分段面板边框上，第三条指入分段轮的 A；分段轮到能力轮同理。箭头方向一律由外层指向内层，没有画反向反馈线。

## 易误读点（历史解释；局部修正见上）

- 不要以为三个轮盘是“三个不同的方法”；它们是同一 ADM 在不同架构层级上的重复实例。
- 不要把面板的层叠阴影当作装饰：它表示同一层级可以有多份架构（多个分段、多个能力）并行。
- 不要以为层间只有单向驱动：正文明确说下层经验应反馈影响上层，只是图中没画反馈箭头。
- 中文稿引用的 figs/g20f_fig4-3.svg 已换成卡片式示意，看不到三个 ADM 轮盘，也读不出“每层都跑完整 ADM”。

## 元素

```json
[
  {
    "id": "strategic_arch",
    "label_en": "Strategic Architecture",
    "label_zh": "战略架构",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右上",
    "description_zh": "单张面板（无层叠阴影），代表企业级的一次 ADM 迭代。 面板内是一个完整的 ADM 轮盘。"
  },
  {
    "id": "strategic_prelim",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 0,
    "position": "顶部"
  },
  {
    "id": "strategic_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 1,
    "position": "正上方"
  },
  {
    "id": "strategic_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 2,
    "position": "右上"
  },
  {
    "id": "strategic_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 3,
    "position": "右侧"
  },
  {
    "id": "strategic_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 4,
    "position": "右下"
  },
  {
    "id": "strategic_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 5,
    "position": "正下方"
  },
  {
    "id": "strategic_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 6,
    "position": "左下"
  },
  {
    "id": "strategic_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 7,
    "position": "左侧"
  },
  {
    "id": "strategic_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": "strategic_arch",
    "level": 2,
    "order": 8,
    "position": "左上"
  },
  {
    "id": "strategic_rm",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "process",
    "parent": "strategic_arch",
    "level": 2,
    "position": "轮心",
    "description_zh": "橙色大圆，辐射线连到本轮的 A–H。"
  },
  {
    "id": "segment_arch",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "左侧",
    "description_zh": "面板右下带两层灰色阴影，表示可有多份分段架构并行。 面板内是一个完整的 ADM 轮盘。"
  },
  {
    "id": "segment_prelim",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 0,
    "position": "顶部"
  },
  {
    "id": "segment_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 1,
    "position": "正上方"
  },
  {
    "id": "segment_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 2,
    "position": "右上"
  },
  {
    "id": "segment_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 3,
    "position": "右侧"
  },
  {
    "id": "segment_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 4,
    "position": "右下"
  },
  {
    "id": "segment_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 5,
    "position": "正下方"
  },
  {
    "id": "segment_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 6,
    "position": "左下"
  },
  {
    "id": "segment_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 7,
    "position": "左侧"
  },
  {
    "id": "segment_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": "segment_arch",
    "level": 2,
    "order": 8,
    "position": "左上"
  },
  {
    "id": "segment_rm",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "process",
    "parent": "segment_arch",
    "level": 2,
    "position": "轮心",
    "description_zh": "橙色大圆，辐射线连到本轮的 A–H。"
  },
  {
    "id": "capability_arch",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "group",
    "parent": null,
    "level": 3,
    "position": "右下",
    "description_zh": "面板右下带两层灰色阴影，表示可有多份能力架构并行。 面板内是一个完整的 ADM 轮盘。"
  },
  {
    "id": "capability_prelim",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 0,
    "position": "顶部"
  },
  {
    "id": "capability_a",
    "label_en": "A. Architecture Vision",
    "label_zh": "阶段 A：架构愿景",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 1,
    "position": "正上方"
  },
  {
    "id": "capability_b",
    "label_en": "B. Business Architecture",
    "label_zh": "阶段 B：业务架构",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 2,
    "position": "右上"
  },
  {
    "id": "capability_c",
    "label_en": "C. Information Systems Architectures",
    "label_zh": "阶段 C：信息系统架构",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 3,
    "position": "右侧"
  },
  {
    "id": "capability_d",
    "label_en": "D. Technology Architecture",
    "label_zh": "阶段 D：技术架构",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 4,
    "position": "右下"
  },
  {
    "id": "capability_e",
    "label_en": "E. Opportunities and Solutions",
    "label_zh": "阶段 E：机会与解决方案",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 5,
    "position": "正下方"
  },
  {
    "id": "capability_f",
    "label_en": "F. Migration Planning",
    "label_zh": "阶段 F：迁移规划",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 6,
    "position": "左下"
  },
  {
    "id": "capability_g",
    "label_en": "G. Implementation Governance",
    "label_zh": "阶段 G：实施治理",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 7,
    "position": "左侧"
  },
  {
    "id": "capability_h",
    "label_en": "H. Architecture Change Management",
    "label_zh": "阶段 H：架构变更管理",
    "type": "phase",
    "parent": "capability_arch",
    "level": 2,
    "order": 8,
    "position": "左上"
  },
  {
    "id": "capability_rm",
    "label_en": "Requirements Management",
    "label_zh": "需求管理",
    "type": "process",
    "parent": "capability_arch",
    "level": 2,
    "position": "轮心",
    "description_zh": "橙色大圆，辐射线连到本轮的 A–H。"
  }
]
```

## 关系

```json
[
  {
    "from": "strategic_prelim",
    "to": "strategic_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "预备阶段接入阶段 A"
  },
  {
    "from": "strategic_a",
    "to": "strategic_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_b",
    "to": "strategic_c",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_c",
    "to": "strategic_d",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_d",
    "to": "strategic_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_e",
    "to": "strategic_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_f",
    "to": "strategic_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_g",
    "to": "strategic_h",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_h",
    "to": "strategic_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_a",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_b",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_c",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_d",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_e",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_f",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_g",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_rm",
    "to": "strategic_h",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_prelim",
    "to": "segment_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "预备阶段接入阶段 A"
  },
  {
    "from": "segment_a",
    "to": "segment_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_b",
    "to": "segment_c",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_c",
    "to": "segment_d",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_d",
    "to": "segment_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_e",
    "to": "segment_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_f",
    "to": "segment_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_g",
    "to": "segment_h",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_h",
    "to": "segment_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "segment_rm",
    "to": "segment_a",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_b",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_c",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_d",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_e",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_f",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_g",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "segment_rm",
    "to": "segment_h",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_prelim",
    "to": "capability_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "预备阶段接入阶段 A"
  },
  {
    "from": "capability_a",
    "to": "capability_b",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_b",
    "to": "capability_c",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_c",
    "to": "capability_d",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_d",
    "to": "capability_e",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_e",
    "to": "capability_f",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_f",
    "to": "capability_g",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_g",
    "to": "capability_h",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_h",
    "to": "capability_a",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "none"
  },
  {
    "from": "capability_rm",
    "to": "capability_a",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_b",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_c",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_d",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_e",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_f",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_g",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "capability_rm",
    "to": "capability_h",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "轮心辐射线：需求管理贯穿该阶段"
  },
  {
    "from": "strategic_arch",
    "to": "segment_arch",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "两条长曲线箭头从战略轮下方引出，到达分段架构面板右侧边缘（面板本身仍是空白边框，箭头落在框上）。"
  },
  {
    "from": "strategic_arch",
    "to": "segment_a",
    "type": "triggering",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "第三条曲线箭头指入分段轮盘的 A（架构愿景），表示每个分段 ADM 从阶段 A 进入。"
  },
  {
    "from": "segment_arch",
    "to": "capability_arch",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "两条曲线从分段轮下方引出，到达能力架构面板左侧边缘。"
  },
  {
    "from": "segment_arch",
    "to": "capability_a",
    "type": "triggering",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "另一条曲线箭头指入能力轮盘的 A。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_strategic_adm",
    "kind": "cycle",
    "name_zh": "战略架构的 ADM 循环",
    "steps": [
      "strategic_prelim",
      "strategic_a",
      "strategic_b",
      "strategic_c",
      "strategic_d",
      "strategic_e",
      "strategic_f",
      "strategic_g",
      "strategic_h"
    ]
  },
  {
    "id": "f_segment_adm",
    "kind": "cycle",
    "name_zh": "分段架构的 ADM 循环",
    "steps": [
      "segment_prelim",
      "segment_a",
      "segment_b",
      "segment_c",
      "segment_d",
      "segment_e",
      "segment_f",
      "segment_g",
      "segment_h"
    ]
  },
  {
    "id": "f_capability_adm",
    "kind": "cycle",
    "name_zh": "能力架构的 ADM 循环",
    "steps": [
      "capability_prelim",
      "capability_a",
      "capability_b",
      "capability_c",
      "capability_d",
      "capability_e",
      "capability_f",
      "capability_g",
      "capability_h"
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "带标题的方框面板",
    "meaning_zh": "一个架构层级（战略/分段/能力）",
    "explicit": false
  },
  {
    "symbol": "面板内的黄色圆轮",
    "meaning_zh": "一次完整的 ADM 循环",
    "explicit": false
  },
  {
    "symbol": "面板右下角灰色层叠边",
    "meaning_zh": "同一层级可以有多份并行（如多个分段）",
    "explicit": false
  },
  {
    "symbol": "长曲线箭头",
    "meaning_zh": "上层架构驱动/触发下层 ADM 循环",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "三个面板呈三角排布：Strategic Architecture 在右上（最大），Segment Architecture 在左侧（中等），Capability Architecture 在右下（最小）。长曲线箭头从右上向左下、再向右下流动，形成“外层→内层”的走向。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig3-1",
    "relation": "based_on",
    "note_zh": "三个面板内的轮盘与图 3-1 的 TOGAF ADM 图形相同（含 Preliminary、A–H、Requirements Management）。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "三条曲线每层的确切条数（1 条指向 A + 2 条指向面板边缘）在缩略图分辨率下按像素判断，若原文实际为 2 条也不影响语义。",
    "战略轮是否也只表示一份架构（无层叠阴影）依画面判断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 23 页正文与第 22 页 4.3 节引言",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 225–231 行",
    "figs/g20f_fig4-3.svg 源码与文本"
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
