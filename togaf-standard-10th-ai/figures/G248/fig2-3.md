# G248/fig2-3 · 包含 MVP 与 MMP 概念的 TOGAF 过渡架构 ERD

> 当前图示解析：[Markdown](../../architecture/diagrams/G248/fig2-3.md) · [JSON](../../architecture/diagrams/G248/fig2-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G248e.pdf`；SHA-256：`810df20478f65d8dfd969089f9c682ec268d0e3a9126e062bda5191c9017e19c`。

## 原图 · PDF 第 17 页

![英文原图](../assets/G248/fig2-3-p0017.png)

PDF 坐标：`[48.2, 36.0, 563.8, 351.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
© becomes the next
Lt
addressed by >
Le
Business
Available Capability &
Goal / Objective
€ achieves
Implemented Solution
Lt
1.
impacts
provides
Ls
1.
changed to >
Baseline
Target
Architecture
€ evolved from
Architecture
Lt
‘maps to
Transition
MvP
Architecture
Lt
implements
0.1
hypothesis proved MVP
implemented by 1
MMP
deployed in 7
implements
implemented by
|
Lt
4 implements
implemented by J
1
1
‘maps to
Delivery Sprints
Work Package
Le
© The Open Group
```

## 概要（历史解释；局部修正见上）

在过渡架构 ERD 上加入 MVP、MMP 与交付冲刺，并用 maps to 虚线把它们对齐到过渡架构与工作包。

## 目的（历史解释；局部修正见上）

把敏捷的 MVP/MMP 概念挂到 TOGAF 的过渡架构模型上：MVP 映射到过渡架构，交付冲刺映射到工作包，MMP 由 MVP 验证假设后形成，并由交付冲刺实现，从而说明敏捷增量交付如何与标准中的架构层级对应。

## 阅读顺序（历史解释；局部修正见上）

先按图 2-2 的方式读蓝色部分的架构 ERD（目标—基线—过渡—工作包）。再看左下角的橙色链：MVP → MMP → Delivery Sprints，注意三条纵向关系及其基数。最后看两条斜体“maps to”虚线：MVP 映射到 Transition Architecture，Delivery Sprints 映射到 Work Package；另有一条从 Delivery Sprints 绕左侧上行的“implements”线直接回到 MVP。

## 关键含义（历史解释；局部修正见上）

- 图 2-2 的六个架构实体全部保留，关系与基数不变；新增的是 MVP、MMP、Delivery Sprints 三个橙色敏捷概念。
- MVP 通过虚线“maps to”对应到过渡架构，说明一个 MVP 是某个过渡架构在交付上的映射物；该虚线没有箭头与基数。
- MMP 与 MVP 之间标注“hypothesis proved MVP ↑”，基数 MVP 端 1、MMP 端 0..1：一个 MVP 最多形成一个 MMP，MMP 用来证明 MVP 的假设成立。
- MMP 与 Delivery Sprints 之间是双向 1..*：交付冲刺实现 MMP，MMP 由交付冲刺实现。
- 另有一条从 Delivery Sprints 左侧绕行、直接指向 MVP 的“implements / implemented by”线，MVP 端标 1，表示交付冲刺也可越过 MMP 直接实现 MVP。
- Delivery Sprints 通过虚线“maps to”对应到 Work Package，把敏捷冲刺与架构侧的工作包对齐；该虚线同样没有箭头与基数。
- 蓝色部分仍表达：目标架构提供可用能力、工作包部署于目标架构、目标架构成为下一轮基线。

## 层级（历史解释；局部修正见上）

没有容器或上下级。蓝色架构实体与橙色敏捷概念分列左右两侧，靠实线（实现/验证）与虚线（映射）相连；可读作“架构侧（目标/基线/过渡/工作包）”与“交付侧（MVP/MMP/冲刺）”两栏，但图中没有画分栏边框。

## 线条含义（历史解释；局部修正见上）

细实线表示实体间的实现、验证或变更关系，线旁写主动/被动关系名并用箭头指示方向，两端标基数；斜体“maps to”配细虚线，表示跨模型的概念对应，不带箭头和基数。橙色框与蓝色框只靠颜色区分交付概念和架构概念，没有图例说明。

## 易误读点（历史解释；局部修正见上）

- “maps to”是虚线且无箭头，不能读成实现关系或数据流；它只表示 MVP 与过渡架构、交付冲刺与工作包之间的概念对应。
- “hypothesis proved MVP”的箭头向上，应读作 MMP 证明 MVP 的假设（MMP→MVP），不要反读成 MVP 证明 MMP。
- Delivery Sprints 左侧那条长线不是连接到基线架构，而是绕到 MVP 左缘，表示冲刺直接实现 MVP。
- MMP 端基数是 0..1 而不是 1：一个 MVP 可能尚未形成 MMP。
- 中文稿当前引用的 PNG 删掉了所有箭头，MVP/MMP 主标签缩成几乎不可读的小字，“implemented by”还未翻译，不能据它判断方向或辨认实体。

## 元素

```json
[
  {
    "id": "business_goal",
    "label_en": "Business Goal / Objective",
    "label_zh": "业务目标／目的",
    "type": "goal",
    "parent": null,
    "position": "左上",
    "description_zh": "动机层实体，合并表示业务目标与业务目的。"
  },
  {
    "id": "available_capability",
    "label_en": "Available Capability & Implemented Solution",
    "label_zh": "可用能力与已实现的解决方案",
    "type": "capability",
    "parent": null,
    "position": "右上",
    "description_zh": "已经可获得的能力及其已落地解决方案。"
  },
  {
    "id": "baseline_architecture",
    "label_en": "Baseline Architecture",
    "label_zh": "基线架构",
    "type": "architecture",
    "parent": null,
    "position": "左中",
    "description_zh": "当前状态的架构。"
  },
  {
    "id": "target_architecture",
    "label_en": "Target Architecture",
    "label_zh": "目标架构",
    "type": "architecture",
    "parent": null,
    "position": "右中",
    "description_zh": "期望的最终状态架构。"
  },
  {
    "id": "transition_architecture",
    "label_en": "Transition Architecture",
    "label_zh": "过渡架构",
    "type": "architecture",
    "parent": null,
    "position": "中央偏上",
    "description_zh": "向目标推进的可实施中间状态。"
  },
  {
    "id": "work_package",
    "label_en": "Work Package",
    "label_zh": "工作包",
    "type": "process",
    "parent": null,
    "position": "底部中央",
    "description_zh": "实现过渡架构的一组工作。"
  },
  {
    "id": "mvp",
    "label_en": "MVP",
    "label_zh": "最小可行产品（MVP）",
    "type": "product",
    "parent": null,
    "position": "左侧橙色链最上",
    "description_zh": "Minimum Viable Product，用最小范围验证假设的产品增量。"
  },
  {
    "id": "mmp",
    "label_en": "MMP",
    "label_zh": "最小可市场化产品（MMP）",
    "type": "product",
    "parent": null,
    "position": "左侧橙色链中间",
    "description_zh": "Minimum Marketable Product，经客户期望检验、可被市场接受的产品状态。"
  },
  {
    "id": "delivery_sprints",
    "label_en": "Delivery Sprints",
    "label_zh": "交付冲刺",
    "type": "time",
    "parent": null,
    "position": "左侧橙色链最下",
    "description_zh": "实现 MVP/MMP 的迭代交付冲刺。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_addressed_by",
    "from": "business_goal",
    "to": "available_capability",
    "type": "association",
    "label_en": "addressed by →",
    "label_zh": "由……应对 →",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "业务目标/目的由可用能力与已实现方案来应对；两端 1..*。"
  },
  {
    "id": "r_achieves",
    "from": "available_capability",
    "to": "business_goal",
    "type": "realization",
    "label_en": "← achieves",
    "label_zh": "← 实现",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "与 addressed by 同一条连线：可用能力与已实现方案实现业务目标；两端 1..*。"
  },
  {
    "id": "r_impacts",
    "from": "business_goal",
    "to": "baseline_architecture",
    "type": "influence",
    "label_en": "↓ impacts",
    "label_zh": "↓ 影响",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "业务目标/目的影响基线架构；箭头向下，两端 1..*。"
  },
  {
    "id": "r_changed_to",
    "from": "baseline_architecture",
    "to": "transition_architecture",
    "type": "transitions_to",
    "label_en": "changed to →",
    "label_zh": "变更为 →",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1:1..*",
    "description_zh": "基线架构变更为过渡架构；基线端 1、过渡架构端 1..*。"
  },
  {
    "id": "r_evolved_from",
    "from": "transition_architecture",
    "to": "baseline_architecture",
    "type": "association",
    "label_en": "← evolved from",
    "label_zh": "← 演进自",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1",
    "description_zh": "与 changed to 同一条连线：过渡架构演进自基线；箭头指向基线，基线端 1。"
  },
  {
    "id": "r_provides",
    "from": "target_architecture",
    "to": "available_capability",
    "type": "serving",
    "label_en": "provides ↑",
    "label_zh": "提供 ↑",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "目标架构提供可用能力与已实现方案；箭头向上，两端 1..*。"
  },
  {
    "id": "r_implements",
    "from": "work_package",
    "to": "transition_architecture",
    "type": "realization",
    "label_en": "↑ implements",
    "label_zh": "↑ 实现",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "工作包实现过渡架构；箭头向上，两端 1..*。"
  },
  {
    "id": "r_implemented_by",
    "from": "transition_architecture",
    "to": "work_package",
    "type": "assignment",
    "label_en": "implemented by ↓",
    "label_zh": "由……实现 ↓",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "与 implements 同一条连线：过渡架构由工作包实现；箭头指向工作包，两端 1..*。"
  },
  {
    "id": "r_deployed_in",
    "from": "work_package",
    "to": "target_architecture",
    "type": "dependency",
    "label_en": "deployed in ↑",
    "label_zh": "部署于 ↑",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1",
    "description_zh": "工作包部署于目标架构；目标架构端 1、工作包端 1..*。"
  },
  {
    "id": "r_becomes_next",
    "from": "target_architecture",
    "to": "baseline_architecture",
    "type": "transitions_to",
    "label_en": "← becomes the next",
    "label_zh": "← 成为下一个",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": null,
    "description_zh": "目标架构成为下一轮基线；线沿图框顶部绕行，箭头指向基线，未标基数。"
  },
  {
    "id": "r_maps_mvp_ta",
    "from": "mvp",
    "to": "transition_architecture",
    "type": "maps_to",
    "label_en": "maps to",
    "label_zh": "映射到",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "cardinality": null,
    "description_zh": "MVP 映射到过渡架构；斜体标签，细虚线，无箭头与基数。"
  },
  {
    "id": "r_mmp_proves_mvp",
    "from": "mmp",
    "to": "mvp",
    "type": "association",
    "label_en": "hypothesis proved MVP ↑",
    "label_zh": "假设经 MVP 验证 ↑",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "0..1:1",
    "description_zh": "MMP 证明 MVP 的假设；箭头向上，MVP 端 1、MMP 端 0..1。"
  },
  {
    "id": "r_ds_implements_mmp",
    "from": "delivery_sprints",
    "to": "mmp",
    "type": "realization",
    "label_en": "↑ implements",
    "label_zh": "↑ 实现",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "交付冲刺实现 MMP；箭头向上，两端 1..*。"
  },
  {
    "id": "r_mmp_implemented_by_ds",
    "from": "mmp",
    "to": "delivery_sprints",
    "type": "assignment",
    "label_en": "implemented by ↓",
    "label_zh": "由……实现 ↓",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1..*:1..*",
    "description_zh": "与 implements 同一条连线：MMP 由交付冲刺实现；箭头指向交付冲刺，两端 1..*。"
  },
  {
    "id": "r_ds_implements_mvp",
    "from": "delivery_sprints",
    "to": "mvp",
    "type": "realization",
    "label_en": "↑ implements / implemented by ↓",
    "label_zh": "↑ 实现 / 由……实现 ↓",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "cardinality": "1",
    "description_zh": "交付冲刺也可直接实现 MVP；线从交付冲刺左缘向左、向上再向右接到 MVP 左缘，箭头向上指 MVP，仅在 MVP 端标 1（交付冲刺端未标基数）。"
  },
  {
    "id": "r_maps_ds_wp",
    "from": "delivery_sprints",
    "to": "work_package",
    "type": "maps_to",
    "label_en": "maps to",
    "label_zh": "映射到",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "cardinality": null,
    "description_zh": "交付冲刺映射到工作包；斜体标签，细虚线，无箭头与基数。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_agile_delivery",
    "kind": "sequence",
    "name_zh": "MVP→MMP→交付冲刺",
    "steps": [
      "mvp",
      "mmp",
      "delivery_sprints"
    ],
    "description_zh": "橙色链自上而下的交付演进：先做 MVP，验证假设后形成 MMP，再由交付冲刺实现；图中另有一条冲刺直接实现 MVP 的旁路线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色矩形",
    "meaning_zh": "架构/目标类实体（目标、能力、基线/目标/过渡架构、工作包）",
    "explicit": false
  },
  {
    "symbol": "橙色圆角矩形",
    "meaning_zh": "敏捷交付概念（MVP、MMP、交付冲刺）",
    "explicit": false
  },
  {
    "symbol": "斜体 maps to + 细虚线",
    "meaning_zh": "跨模型的概念映射，无方向与基数",
    "explicit": false
  },
  {
    "symbol": "细实线 + 关系短语 + 箭头",
    "meaning_zh": "实现、验证、变更等关系，箭头指示阅读方向",
    "explicit": false
  },
  {
    "symbol": "线旁 1、0..1、1..*",
    "meaning_zh": "该端基数",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "上半部沿用图 2-2 的环形 ERD（业务目标左上、能力右上、基线左中、目标右中、过渡架构中央、工作包底部）；左下另起一条竖向橙色链 MVP → MMP → Delivery Sprints，两条斜体 maps to 虚线分别从 MVP 指向过渡架构、从 Delivery Sprints 指向工作包，另有一条实现线从 Delivery Sprints 左侧绕回 MVP。"
}
```

## 相关图

```json
[
  {
    "target": "G248/fig2-2",
    "relation": "variant_of",
    "note_zh": "保留图 2-2 的全部架构实体与关系，增加 MVP、MMP、Delivery Sprints 及两条 maps to 虚线。"
  },
  {
    "target": "G248/fig3-1",
    "relation": "instance_of",
    "note_zh": "蓝色部分的实体类型取自企业元模型，本图是其在过渡架构 + 敏捷交付场景中的子集。"
  },
  {
    "target": "G20F/fig4-2",
    "relation": "related",
    "note_zh": "另一份指南中专门讲“过渡架构”的图，主题相同、画法不同。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "Delivery Sprints 直接实现 MVP 的旁路线只在 MVP 端标了 1，交付冲刺端没有基数；已按“1（仅 MVP 端）”记录。",
    "两条 maps to 虚线均未标基数与箭头，只能判为无方向的概念映射。",
    "“hypothesis proved MVP”是不完整英语（应为 hypothesis proved by MVP），按图原样转录，语义按“MMP 证明 MVP 假设”理解。",
    "图右下有“copy”水印，不属于图内容。"
  ],
  "analyzed_from": [
    "英文 PDF 第 17 页图 2-3 截图（220 dpi）与 600 dpi 重渲染分块",
    "英文 PDF 第 16–17 页正文",
    "中文稿 G248e_构建块的选择方法.md 第 132–174 行",
    "figs/zh/g248e_fig2-3_zh.png（中文化 PNG）",
    "figs/g248e_fig2-3_en.png（英文原图 PNG）"
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
