# G186/fig5-2 · EA 存储库示例

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig5-2.md) · [JSON](../../architecture/diagrams/G186/fig5-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 51 页

![英文原图](../assets/G186/fig5-2-p0051.png)

PDF 坐标：`[151.3, 174.2, 460.7, 499.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
“Ff Austin Workshop Architecture
ee
J Connections
{5} Catalogues
x} Matrices
3D Views
gj Chars
“J Austin Workshop Candidate
©-“¥ Austin Workshop Target
~-°2 Components
J Connections
(4)-{3] Catalogues
x} Matrices
7 3D Views
8-9 Charts
“J Austin Workshop Annual Transition (Current Year)
“Y Austin Workshop Annual Transition (Next Year)
Austin Workshop Transition
€? Austin Workshop Current
```

## 概要（历史解释；局部修正见上）

EA 存储库中的一个示例树：一个架构的七类视角，以及候选、目标（含三个过渡）与现状四种状态。

## 目的（历史解释；局部修正见上）

作者用真实的工具截图说明“一个架构项目在存储库里如何组织”：同一架构按状态分容器，每个容器下再按七类视角分文件夹；候选、目标、现状并列，目标下再挂多个过渡，从而支持“互不干扰地探索候选未来”。

## 阅读顺序（历史解释；局部修正见上）

从最上面的根节点“Austin Workshop Architecture”往下读。带“−”的节点是已展开，带“+”的是折叠。根下先列七类视角文件夹（组件、连接、目录、矩阵、图、三维视图、图表），然后是三个状态容器：候选（折叠）、目标（已展开）、现状（折叠，位于最底部）。目标容器里重复同样的七类视角，并多出三个过渡：本年度过渡、下一年度过渡、过渡。

## 关键含义（历史解释；局部修正见上）

- 同一个架构在存储库中按状态分成多个容器：候选、目标、现状，三者并列在根节点下；目标还包含三个过渡。
- 每个状态容器内部都重复同一套七类视角：Components、Connections、Catalogues、Matrices、Diagrams、3D Views、Charts。
- 只有“目标”是展开的，因此截图展示了目标状态的内部结构；候选与现状折叠，内容不可见。
- 三个过渡分别是年度过渡（本年度）、年度过渡（下一年度）和一个未标年度的“过渡”，说明过渡状态可以有多个版本。
- 正文说公用的现状会被定期更新并作为所有差距分析的基线；目标（合并目标）也用于差距分析。
- 正文要求为每个架构项目建独立容器，使候选探索不影响其他实践者；这张树就是这种容器的实例。
- 树中没有任何语义箭头；“+/-”与缩进只表示展开状态与包含关系。

## 层级（历史解释；局部修正见上）

三层：根（Austin Workshop Architecture）→ 七个视角文件夹 + 三个状态容器（Candidate、Target、Current）；Target → 七个视角文件夹 + 三个过渡（Annual Transition Current Year、Annual Transition Next Year、Transition）。

## 线条含义（历史解释；局部修正见上）

灰色点线是工具绘制的树状连接线，只表示父子包含；左侧“+/−”表示折叠/展开，不是流程或依赖。图中没有带箭头的语义连线。

## 易误读点（历史解释；局部修正见上）

- 不要把七类视角（组件/连接/目录/矩阵/图/三维视图/图表）当成 ADM 阶段或架构分层；它们是同一架构的不同视图类型。
- 不要把三个过渡理解为严格按“本年度→下一年度→过渡”排序；其中一个只叫“Transition”，没有年份。
- 不要把根节点当成整个存储库；它只是“奥斯汀工作坊”这一个架构示例。
- 候选与现状是折叠的，不能因为看不到内容就认为它们为空。
- 中文 PNG 中“Austin Workshop Transition”仍未翻译，且若干展开符丢失；中文 SVG 又额外加了原图没有的说明栏，两者都不能完全替代英文截图。

## 元素

```json
[
  {
    "id": "aw_architecture",
    "label_en": "Austin Workshop Architecture",
    "label_zh": "奥斯汀工作坊架构",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "position": "树根（第一行，已展开）",
    "description_zh": "示例架构的根容器。"
  },
  {
    "id": "aw_components",
    "label_en": "Components",
    "label_zh": "组件",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 1,
    "position": "根下第 1 行",
    "description_zh": "组件视图文件夹。"
  },
  {
    "id": "aw_connections",
    "label_en": "Connections",
    "label_zh": "连接",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 2,
    "position": "根下第 2 行",
    "description_zh": "连接视图文件夹。"
  },
  {
    "id": "aw_catalogues",
    "label_en": "Catalogues",
    "label_zh": "目录",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 3,
    "position": "根下第 3 行",
    "description_zh": "目录视图文件夹。"
  },
  {
    "id": "aw_matrices",
    "label_en": "Matrices",
    "label_zh": "矩阵",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 4,
    "position": "根下第 4 行",
    "description_zh": "矩阵视图文件夹。"
  },
  {
    "id": "aw_diagrams",
    "label_en": "Diagrams",
    "label_zh": "图",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 5,
    "position": "根下第 5 行",
    "description_zh": "图视图文件夹。"
  },
  {
    "id": "aw_3d_views",
    "label_en": "3D Views",
    "label_zh": "三维视图",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 6,
    "position": "根下第 6 行",
    "description_zh": "三维视图文件夹。"
  },
  {
    "id": "aw_charts",
    "label_en": "Charts",
    "label_zh": "图表",
    "type": "group",
    "parent": "aw_architecture",
    "level": 1,
    "order": 7,
    "position": "根下第 7 行",
    "description_zh": "图表文件夹。"
  },
  {
    "id": "aw_candidate",
    "label_en": "Austin Workshop Candidate",
    "label_zh": "奥斯汀工作坊候选",
    "type": "architecture",
    "parent": "aw_architecture",
    "level": 1,
    "position": "根下第 8 行（折叠）",
    "description_zh": "候选状态容器，未展开。"
  },
  {
    "id": "aw_target",
    "label_en": "Austin Workshop Target",
    "label_zh": "奥斯汀工作坊目标",
    "type": "architecture",
    "parent": "aw_architecture",
    "level": 1,
    "position": "根下第 9 行（已展开）",
    "description_zh": "目标状态容器。"
  },
  {
    "id": "aw_current",
    "label_en": "Austin Workshop Current",
    "label_zh": "奥斯汀工作坊现状",
    "type": "architecture",
    "parent": "aw_architecture",
    "level": 1,
    "position": "最底部（折叠，行被画面裁切）",
    "description_zh": "现状状态容器，未展开。"
  },
  {
    "id": "awt_components",
    "label_en": "Components",
    "label_zh": "组件",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 1,
    "position": "目标下第 1 行",
    "description_zh": "目标状态的组件视图。"
  },
  {
    "id": "awt_connections",
    "label_en": "Connections",
    "label_zh": "连接",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 2,
    "position": "目标下第 2 行",
    "description_zh": "目标状态的连接视图。"
  },
  {
    "id": "awt_catalogues",
    "label_en": "Catalogues",
    "label_zh": "目录",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 3,
    "position": "目标下第 3 行",
    "description_zh": "目标状态的目录视图。"
  },
  {
    "id": "awt_matrices",
    "label_en": "Matrices",
    "label_zh": "矩阵",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 4,
    "position": "目标下第 4 行",
    "description_zh": "目标状态的矩阵视图。"
  },
  {
    "id": "awt_diagrams",
    "label_en": "Diagrams",
    "label_zh": "图",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 5,
    "position": "目标下第 5 行",
    "description_zh": "目标状态的图视图。"
  },
  {
    "id": "awt_3d_views",
    "label_en": "3D Views",
    "label_zh": "三维视图",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 6,
    "position": "目标下第 6 行",
    "description_zh": "目标状态的三维视图。"
  },
  {
    "id": "awt_charts",
    "label_en": "Charts",
    "label_zh": "图表",
    "type": "group",
    "parent": "aw_target",
    "level": 2,
    "order": 7,
    "position": "目标下第 7 行",
    "description_zh": "目标状态的图表。"
  },
  {
    "id": "awt_annual_current",
    "label_en": "Austin Workshop Annual Transition (Current Year)",
    "label_zh": "奥斯汀工作坊年度过渡（本年度）",
    "type": "architecture",
    "parent": "aw_target",
    "level": 2,
    "position": "目标下第 8 行（折叠）",
    "description_zh": "本年度过渡状态。"
  },
  {
    "id": "awt_annual_next",
    "label_en": "Austin Workshop Annual Transition (Next Year)",
    "label_zh": "奥斯汀工作坊年度过渡（下一年度）",
    "type": "architecture",
    "parent": "aw_target",
    "level": 2,
    "position": "目标下第 9 行（折叠）",
    "description_zh": "下一年度过渡状态。"
  },
  {
    "id": "awt_transition",
    "label_en": "Austin Workshop Transition",
    "label_zh": "奥斯汀工作坊过渡",
    "type": "architecture",
    "parent": "aw_target",
    "level": 2,
    "position": "目标下第 10 行（折叠）",
    "description_zh": "未标注年度的过渡状态。"
  }
]
```

## 关系

```json
[
  {
    "from": "aw_architecture",
    "to": "aw_components",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_connections",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_catalogues",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_matrices",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_diagrams",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_3d_views",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_charts",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_candidate",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_target",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_architecture",
    "to": "aw_current",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_components",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_connections",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_catalogues",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_matrices",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_diagrams",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_3d_views",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_charts",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_annual_current",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_annual_next",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "aw_target",
    "to": "awt_transition",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "“−”方框",
    "meaning_zh": "该节点已展开",
    "explicit": false
  },
  {
    "symbol": "“+”方框",
    "meaning_zh": "该节点已折叠，内容未显示",
    "explicit": false
  },
  {
    "symbol": "灰色网络图标",
    "meaning_zh": "架构/状态容器",
    "explicit": false
  },
  {
    "symbol": "红色三点图标",
    "meaning_zh": "Components 视图文件夹",
    "explicit": false
  },
  {
    "symbol": "紫色三角/表格/交叉/图形图标",
    "meaning_zh": "Connections / Catalogues / Matrices / Diagrams 等视图类型",
    "explicit": false
  },
  {
    "symbol": "灰色点线",
    "meaning_zh": "树状包含关系",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "竖直树状列表：根节点在顶部，其下依次缩进排列七个视角文件夹、候选、目标（展开，内含七个视角与三个过渡）、现状；左侧为虚线连接线与展开符，每行前有类型图标。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig5-1",
    "relation": "instance_of",
    "note_zh": "图 5-1 给出架构存储库的通用分区，本图是其中 Architecture Landscape 部分在建模工具中的实例截图。"
  },
  {
    "target": "G186/fig5-3",
    "relation": "related",
    "note_zh": "同一工具中的下一张截图，展示多个并行的候选架构容器。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "最底部的“Austin Workshop Current”一行被画面下缘裁切，只能看到图标与文字上半部分；其展开状态应为折叠（+）。",
    "原图为工具截图，无法确认每个状态容器是否还有截图外的其他子项。",
    "“Austin Workshop Transition”与两个年度过渡的区别只能从名称推断，图内没有说明。"
  ],
  "analyzed_from": [
    "英文 PDF 第 51 页图 5-2 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 51–52 页正文",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 567–592 行及标签对照表 L571–L589",
    "figs/g186e_fig5-2_en.png、figs/zh/g186e_fig5-2_zh.png 与 figs/zh/g186e_fig5-2_zh.svg"
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
