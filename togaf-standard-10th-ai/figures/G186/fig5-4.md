# G186/fig5-4 · 建模与分析工具中的参考材料

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig5-4.md) · [JSON](../../architecture/diagrams/G186/fig5-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 53 页

![英文原图](../assets/G186/fig5-4-p0053.png)

PDF 坐标：`[138.5, 142.7, 473.5, 398.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
GY Reference Architecture
~-*2 Components
J Connections
#-{]) Catalogues
{J Matrices
8-{33]) Diagrams
‘4 3D Views
(8-y{J Charts
(SY IT4IT Reference Atlas
(“Ff APQC Cross-Industry Reference Atlas
(®~“F APQC Downstream Reference Atlas
(~“F Navigate: Information Reference Atlas
“J BPMN Training Atlas
```

## 概要（历史解释；局部修正见上）

参考库示例：一个 Reference Architecture 容器下含七类视角文件夹和八个参考架构/图谱条目。

## 目的（历史解释；局部修正见上）

作者用这张截图说明参考库应把参考材料作为“离散架构”保存，而不是散落文档：每个参考架构/图谱都有自己的容器，架构师可以把“候选或目标中如何使用参考架构”与基础参考材料逐项比较。

## 阅读顺序（历史解释；局部修正见上）

第一行是根“Reference Architecture”（已展开，带“−”），下面缩进七行视角文件夹：组件、连接、目录、矩阵、图、三维视图、图表。七行之后回到与根相同的层级，依次列出八个参考材料容器：IT4IT Reference Atlas、APQC Cross-Industry Reference Atlas、APQC Upstream Reference Atlas、APQC Downstream Reference Atlas、Navigate: Information, Application & APQC Reference Atlas、Navigate Logical Application Reference Atlas、Navigate: Information Reference Atlas、BPMN Training Atlas。八个条目都带“+”，表示折叠。

## 关键含义（历史解释；局部修正见上）

- 参考库中的参考材料被组织成离散的架构容器，而不是普通文件；根容器名为 Reference Architecture。
- 每个容器同样带七类视角：组件、连接、目录、矩阵、图、三维视图、图表。
- 八个参考条目覆盖三类来源：IT4IT（一个）、APQC（跨行业/上游/下游三个）、Navigate（三个）、BPMN（一个培训图谱）。
- 正文说把参考架构作为离散架构维护，才能把“参考架构在当前候选或目标中的使用方式”与基础参考材料比较。
- 存续较久的存储库常出现多个相互重叠的参考架构：例如 APQC 流程分类框架、ERP 厂商的流程分类、系统集成商的流程分类、后来引入的 IT4IT。
- 参考材料是加速器：提供经过验证的起点，减少重新发明流程，并统一实践者的术语。
- 八个条目均折叠，截图没有展示任何参考架构的内部内容。

## 层级（历史解释；局部修正见上）

两层：根（Reference Architecture）→ 七个视角文件夹 + 八个参考架构/图谱容器。八个容器与视角文件夹同级，均挂在根下；它们之间没有层级关系。

## 线条含义（历史解释；局部修正见上）

灰色点线只表示父子包含；“+/−”表示折叠/展开。图中没有语义箭头，八个参考条目之间的“重叠/引用”关系没有被画出，只能从正文得知。

## 易误读点（历史解释；局部修正见上）

- 不要把八个 Atlas 当成七类视角的子项；它们与视角文件夹同级，都挂在 Reference Architecture 根下。
- 不要把 APQC 的三个图谱理解为版本递进；它们是跨行业、上游、下游三个不同范围的参考图谱。
- 不要把“Reference Architecture”根节点当成某一个参考架构；它是一个存放多个参考架构的容器。
- 图中看不到参考架构之间的重叠关系；正文才说明 APQC、ERP 厂商、系统集成商、IT4IT 可能同时存在。
- 中文 PNG 的缩进错位与译名不统一会造成层级与名称误读；应以英文原图或标签表为准。

## 元素

```json
[
  {
    "id": "ref_arch_root",
    "label_en": "Reference Architecture",
    "label_zh": "参考架构",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "第一行（已展开）",
    "description_zh": "存放多个参考架构/图谱的根容器。"
  },
  {
    "id": "ra_components",
    "label_en": "Components",
    "label_zh": "组件",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 1,
    "position": "根下第 1 行",
    "description_zh": "组件视图文件夹。"
  },
  {
    "id": "ra_connections",
    "label_en": "Connections",
    "label_zh": "连接",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 2,
    "position": "根下第 2 行",
    "description_zh": "连接视图文件夹。"
  },
  {
    "id": "ra_catalogues",
    "label_en": "Catalogues",
    "label_zh": "目录",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 3,
    "position": "根下第 3 行",
    "description_zh": "目录视图文件夹。"
  },
  {
    "id": "ra_matrices",
    "label_en": "Matrices",
    "label_zh": "矩阵",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 4,
    "position": "根下第 4 行",
    "description_zh": "矩阵视图文件夹。"
  },
  {
    "id": "ra_diagrams",
    "label_en": "Diagrams",
    "label_zh": "图",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 5,
    "position": "根下第 5 行",
    "description_zh": "图视图文件夹。"
  },
  {
    "id": "ra_3d_views",
    "label_en": "3D Views",
    "label_zh": "三维视图",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 6,
    "position": "根下第 6 行",
    "description_zh": "三维视图文件夹。"
  },
  {
    "id": "ra_charts",
    "label_en": "Charts",
    "label_zh": "图表",
    "type": "group",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 7,
    "position": "根下第 7 行",
    "description_zh": "图表文件夹。"
  },
  {
    "id": "ref_it4it",
    "label_en": "IT4IT Reference Atlas",
    "label_zh": "IT4IT 参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 8,
    "position": "第 9 行（折叠）",
    "description_zh": "IT4IT 参考架构。"
  },
  {
    "id": "ref_apqc_cross",
    "label_en": "APQC Cross-Industry Reference Atlas",
    "label_zh": "APQC 跨行业参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 9,
    "position": "第 10 行（折叠）",
    "description_zh": "APQC 跨行业流程分类参考。"
  },
  {
    "id": "ref_apqc_up",
    "label_en": "APQC Upstream Reference Atlas",
    "label_zh": "APQC 上游参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 10,
    "position": "第 11 行（折叠）",
    "description_zh": "APQC 上游参考图谱。"
  },
  {
    "id": "ref_apqc_down",
    "label_en": "APQC Downstream Reference Atlas",
    "label_zh": "APQC 下游参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 11,
    "position": "第 12 行（折叠）",
    "description_zh": "APQC 下游参考图谱。"
  },
  {
    "id": "ref_nav_ia",
    "label_en": "Navigate: Information, Application & APQC Reference Atlas",
    "label_zh": "Navigate：信息、应用与 APQC 参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 12,
    "position": "第 13 行（折叠）",
    "description_zh": "Navigate 的信息/应用/APQC 综合参考图谱。"
  },
  {
    "id": "ref_nav_logical",
    "label_en": "Navigate Logical Application Reference Atlas",
    "label_zh": "Navigate 逻辑应用参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 13,
    "position": "第 14 行（折叠）",
    "description_zh": "Navigate 逻辑应用参考图谱。"
  },
  {
    "id": "ref_nav_info",
    "label_en": "Navigate: Information Reference Atlas",
    "label_zh": "Navigate：信息参考图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 14,
    "position": "第 15 行（折叠）",
    "description_zh": "Navigate 信息参考图谱。"
  },
  {
    "id": "ref_bpmn",
    "label_en": "BPMN Training Atlas",
    "label_zh": "BPMN 培训图谱",
    "type": "artifact",
    "parent": "ref_arch_root",
    "level": 1,
    "order": 15,
    "position": "第 16 行（折叠）",
    "description_zh": "BPMN 培训参考材料。"
  }
]
```

## 关系

```json
[
  {
    "from": "ref_arch_root",
    "to": "ra_components",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ra_connections",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ra_catalogues",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ra_matrices",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ra_diagrams",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ra_3d_views",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ra_charts",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_it4it",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_apqc_cross",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_apqc_up",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_apqc_down",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_nav_ia",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_nav_logical",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_nav_info",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "ref_arch_root",
    "to": "ref_bpmn",
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
    "meaning_zh": "已展开",
    "explicit": false
  },
  {
    "symbol": "“+”方框",
    "meaning_zh": "已折叠",
    "explicit": false
  },
  {
    "symbol": "灰色网络图标",
    "meaning_zh": "参考架构/图谱容器",
    "explicit": false
  },
  {
    "symbol": "彩色小图标",
    "meaning_zh": "七类视角文件夹（组件/连接/目录/矩阵/图/三维视图/图表）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "竖直树：根“Reference Architecture”在第一行，下面缩进七行视角文件夹，再回到顶层依次列出八个参考图谱；左侧为点线、展开符与图标，画面无标题、无图例。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig5-1",
    "relation": "instance_of",
    "note_zh": "图 5-1 把 Reference Library 列为架构存储库的一个分区；本图是该参考库在建模工具中的实例截图。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "八个参考图谱之间的重叠/引用关系在图中没有画出，只能据正文理解。",
    "“Reference Architecture”根节点与八个条目的父子关系由缩进判断；工具截图中层级线较淡。",
    "APQC 上游/下游图谱的具体范围图内没有说明，仅从名称推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 53 页图 5-4 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 52–53 页正文",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 620–655 行及标签对照表 L630–L650",
    "figs/g186e_fig5-4_en.png 与 figs/zh/g186e_fig5-4_zh.png"
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
