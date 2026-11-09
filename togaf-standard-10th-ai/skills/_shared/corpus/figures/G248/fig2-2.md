# G248/fig2-2 · TOGAF 过渡架构的实体关系图（ERD）

> 当前图示解析：[Markdown](../../architecture/diagrams/G248/fig2-2.md) · [JSON](../../architecture/diagrams/G248/fig2-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G248e.pdf`；SHA-256：`810df20478f65d8dfd969089f9c682ec268d0e3a9126e062bda5191c9017e19c`。

## 原图 · PDF 第 16 页

![英文原图](../assets/G248/fig2-2-p0016.png)

PDF 坐标：`[48.2, 36.0, 563.8, 394.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
‘€ becomes the next
1?
addressed by >
1
Business
Available Capability &
Implemented Solution
Goal / Objective
€ achieves
Ls
1
wv impacts
provides
Le
Le
changed to >
Baseline
Target
Architecture
€ evolved from
Architecture
1
Transition
Architecture
1
4 implements
implemented
1.
Work
Package
Ls
© The Open Group
```

## 概要（历史解释；局部修正见上）

用 ERD 表达业务目标、能力与解决方案、基线/目标/过渡架构及工作包之间的六组关系。

## 目的（历史解释；局部修正见上）

为 2.1 节定义过渡架构在架构全景中的位置：基线架构经变更产生一个或多个过渡架构，过渡架构由工作包实现；目标架构提供可用能力与已实现方案，并在实现后成为下一轮基线。它把正文中“基线—目标—过渡”三个概念及其实现关系一次说清。

## 阅读顺序（历史解释；局部修正见上）

从左上“Business Goal / Objective”读起：向右看它与“Available Capability & Implemented Solution”的双向关系，向下看它对基线架构的影响。再沿左侧“Baseline Architecture → Transition Architecture → Work Package”读实现链，注意每条线两端的 1 或 1..*。最后沿右侧“Target Architecture → Available Capability”以及“Target → Work Package”读目标架构的提供与部署关系，并顺着图框顶部绕行的“becomes the next”回到基线。

## 关键含义（历史解释；局部修正见上）

- 图中共六个实体：业务目标/目的、可用能力与已实现的解决方案、基线架构、目标架构、过渡架构、工作包；没有属性栏，只表达实体与关系。
- 业务目标与可用能力/已实现方案之间是双向的：目标“由……应对”（addressed by），能力/方案“实现”（achieves）目标，两端基数均为 1..*。
- 基线架构与过渡架构是一对多：1 个基线可“变更为”1..* 个过渡架构，反过来过渡架构“演进自”基线。
- 工作包实现过渡架构（implements / implemented by，两端 1..*），并“部署于”目标架构（目标端 1、工作包端 1..*）。
- 目标架构“提供”可用能力与已实现的解决方案（provides，两端 1..*），体现目标态才交付最终能力。
- 顶部绕行的“becomes the next”从目标架构回到基线架构，表示本轮目标实现后成为下一轮的基线；该线未标基数。
- 业务目标/目的“影响”基线架构（impacts，向下箭头，两端 1..*），说明动机层对现状架构的约束。

## 层级（历史解释；局部修正见上）

没有容器或上下级：六个实体平铺，由连线组织。若按语义分层，可读作“动机层（业务目标/目的）—能力层（可用能力与已实现方案）—架构层（基线/目标/过渡）—实施层（工作包）”，但图中没有画出这种分层边界。

## 线条含义（历史解释；局部修正见上）

细实线连接两个实体；同一条线常写两个互为反向的关系名（如 addressed by / achieves、changed to / evolved from、implements / implemented by），箭头指出该关系名的阅读方向；线两端的 1、1..* 是基数。顶部“becomes the next”沿图框外缘绕行，是一条从目标架构回到基线架构的长折线。全图没有图例，记法靠线旁文字自解释。

## 易误读点（历史解释；局部修正见上）

- “becomes the next”不是目标架构→过渡架构，而是目标架构→基线架构：本轮目标成为下一轮基线。
- “impacts”的箭头向下，应读作业务目标/目的影响基线架构；不要反读成基线架构影响目标。
- “provides”的箭头向上，应读作目标架构提供可用能力与已实现方案，不要读成能力提供目标架构。
- “deployed in”是工作包→目标架构（工作包部署于目标架构），且目标端基数为 1、工作包端为 1..*，不要读成目标架构部署于工作包。
- 图中没有主键、属性或表结构，它不是数据库物理模型，只是概念层 ERD。
- 中文稿当前引用的 PNG 删掉了所有关系箭头，“implemented by”还只剩“in”，不能据它判断方向；应以英文原图为准。

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
    "description_zh": "动机层的实体，合并表示业务目标与业务目的。"
  },
  {
    "id": "available_capability",
    "label_en": "Available Capability & Implemented Solution",
    "label_zh": "可用能力与已实现的解决方案",
    "type": "capability",
    "parent": null,
    "position": "右上",
    "description_zh": "已经可获得的能力及其已落地的解决方案。"
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
    "position": "中央偏下",
    "description_zh": "向目标推进的可实施中间状态，可有多个。"
  },
  {
    "id": "work_package",
    "label_en": "Work Package",
    "label_zh": "工作包",
    "type": "process",
    "parent": null,
    "position": "底部中央",
    "description_zh": "实现过渡架构的一组工作，可部署到目标架构。"
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
    "description_zh": "业务目标/目的由可用能力与已实现方案来应对；目标端与能力端均标 1..*。"
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
    "description_zh": "与 addressed by 同一条连线：可用能力与已实现方案实现业务目标；箭头指向业务目标，两端 1..*。"
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
    "description_zh": "基线架构变更为过渡架构；基线端 1，过渡架构端 1..*。"
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
    "description_zh": "与 changed to 同一条连线：过渡架构演进自基线；箭头指向基线，基线端标 1。"
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
    "description_zh": "目标架构提供可用能力与已实现的解决方案；箭头向上，两端 1..*。"
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
    "description_zh": "工作包部署于目标架构；箭头向上，目标架构端 1、工作包端 1..*。"
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
    "description_zh": "目标架构成为下一轮的基线架构；线从目标架构右缘向上、沿顶部向左、再下折到基线架构左缘，箭头指向基线，未标基数。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色矩形",
    "meaning_zh": "一个元模型实体（业务目标、架构、工作包等）",
    "explicit": false
  },
  {
    "symbol": "细实线 + 线旁两侧的关系短语",
    "meaning_zh": "两个实体之间的关系；同一连线上的主动/被动短语互为反向读法",
    "explicit": false
  },
  {
    "symbol": "线旁的 1、1..*",
    "meaning_zh": "该端的基数（1 个或 1 个以上）",
    "explicit": false
  },
  {
    "symbol": "关系短语旁的 →、←、↑、↓",
    "meaning_zh": "该关系短语的阅读方向（主语→宾语）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "六实体呈环形分布：业务目标在左上、可用能力/已实现方案在右上、基线架构在左中、目标架构在右中、过渡架构居中偏下、工作包在底部中央。目标架构→基线架构的“becomes the next”沿图框顶部与左右外缘绕成一个大回路，其余关系为直线或单折线。"
}
```

## 相关图

```json
[
  {
    "target": "G248/fig2-3",
    "relation": "basis_for",
    "note_zh": "图 2-3 在同一 ERD 上增加 MVP、MMP、交付冲刺及两条 maps to 虚线。"
  },
  {
    "target": "G248/fig3-1",
    "relation": "instance_of",
    "note_zh": "本图的基线/目标/过渡架构、业务目标、能力、工作包等实体类型来自图 3-1 的企业元模型，是其在过渡架构场景中的子集。"
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
    "“becomes the next”沿线没有基数标注，只能记录为无基数。",
    "“deployed in”与“implemented by”两条线在工作包附近相邻，基数 1（目标架构端）与 1..*（工作包端）按线的走向归属，判读无误但需注意不要互换。",
    "图右下角有巨大的“copy”水印，是 PDF 防伪标记，不属于图内容。"
  ],
  "analyzed_from": [
    "英文 PDF 第 16 页图 2-2 截图（220 dpi）与 600 dpi 重渲染分块",
    "英文 PDF 第 16 页正文",
    "中文稿 G248e_构建块的选择方法.md 第 104–130 行",
    "figs/zh/g248e_fig2-2_zh.png（中文化 PNG）",
    "figs/g248e_fig2-2_en.png（英文原图 PNG）"
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
