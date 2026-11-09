# G186/fig5-3 · 多个候选架构

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig5-3.md) · [JSON](../../architecture/diagrams/G186/fig5-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 52 页

![英文原图](../assets/G186/fig5-3-p0052.png)

PDF 坐标：`[112.7, 111.1, 499.3, 302.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
—
“J Austin Workshop Candidate
ee
)~<J Connections
{4 Catalogues
{x} Matrices
#-{S]) Diagrams
Ls
Bh
+ 3D Views
fj Charts
“J Austin Portfolio Candidate
“J Austin Workshop Project Controls Candidate (Project)
- “J Austin Workshop Field Data Capture Candidate (Solution Delivery)
```

## 概要（历史解释；局部修正见上）

同一存储库中并列的四个候选架构容器，其中一个展开显示七类视角，另三个分别对应组合、项目与解决方案交付。

## 目的（历史解释；局部修正见上）

承接图 5-2，作者用第二张截图说明“多个架构项目可以各有独立的候选容器”：四个候选并列存在，互不覆盖；括号里的 Portfolio / Project / Solution Delivery 把容器与第 3 章的四种架构目的对应起来。

## 阅读顺序（历史解释；局部修正见上）

第一行是根“Austin Workshop Candidate”，带“−”表示已展开，下面列出七类视角文件夹（组件、连接、目录、矩阵、图、三维视图、图表）。七类视角之后，回到与根相同的缩进层级，依次是三个独立的候选容器：Austin Portfolio Candidate、Austin Workshop Project Controls Candidate (Project)、Austin Workshop Field Data Capture Candidate (Solution Delivery)。后三者都带“+”，表示折叠；它们不是第一个候选的子项。

## 关键含义（历史解释；局部修正见上）

- 图中一共有四个候选架构容器：工作坊候选、组合候选、项目控制候选、现场数据采集候选。
- 只有第一个“奥斯汀工作坊候选”展开，展示七类视角；其余三个折叠，内容不可见。
- 三个额外候选的括号标注了它们的架构目的：Portfolio、Project、Solution Delivery，与图 3-3 的四种目的中的后三种对应。
- 四个候选在树中并列，说明它们是各自独立的容器，而不是同一候选的四个版本或四个阶段。
- 正文强调这种独立容器让架构师可以自由探索潜在未来，而不影响其他架构师的工作。
- 七类视角在每个容器内重复出现，说明“状态/项目容器 × 视角类型”是存储库的固定组织方式。
- 图中没有目标/现状状态，也没有过渡；这一页只讲并行候选。

## 层级（历史解释；局部修正见上）

两层：顶层是四个并列的候选容器；第一个容器（Austin Workshop Candidate）下挂七个视角文件夹。其余三个容器折叠，子项未显示。

## 线条含义（历史解释；局部修正见上）

灰色点线只表示父子包含；“+/−”表示折叠/展开。图中没有语义箭头，也没有表示候选之间比较或竞争的连线；四个候选的并列关系由同一缩进层级表达。

## 易误读点（历史解释；局部修正见上）

- 不要把后三个候选读成第一个候选的子项；它们与第一个候选同级，只是缩进在中文 PNG 中被破坏。
- 不要把四个候选理解为同一架构的四个版本；它们是不同架构项目/不同目的的候选容器。
- 括号中的 Portfolio、Project、Solution Delivery 是目的标签，不是 ADM 阶段。
- 折叠的候选不代表为空；截图只是没有展开它们。
- 中文 PNG 的层级错位会让人误以为“奥斯汀组合候选”是根的子项，应以英文原图为准。

## 元素

```json
[
  {
    "id": "c_workshop",
    "label_en": "Austin Workshop Candidate",
    "label_zh": "奥斯汀工作坊候选",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "order": 1,
    "position": "第一行（已展开）",
    "description_zh": "工作坊架构的候选容器。"
  },
  {
    "id": "c_workshop_components",
    "label_en": "Components",
    "label_zh": "组件",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 1,
    "position": "候选下第 1 行",
    "description_zh": "组件视图文件夹。"
  },
  {
    "id": "c_workshop_connections",
    "label_en": "Connections",
    "label_zh": "连接",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 2,
    "position": "候选下第 2 行",
    "description_zh": "连接视图文件夹。"
  },
  {
    "id": "c_workshop_catalogues",
    "label_en": "Catalogues",
    "label_zh": "目录",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 3,
    "position": "候选下第 3 行",
    "description_zh": "目录视图文件夹。"
  },
  {
    "id": "c_workshop_matrices",
    "label_en": "Matrices",
    "label_zh": "矩阵",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 4,
    "position": "候选下第 4 行",
    "description_zh": "矩阵视图文件夹。"
  },
  {
    "id": "c_workshop_diagrams",
    "label_en": "Diagrams",
    "label_zh": "图",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 5,
    "position": "候选下第 5 行",
    "description_zh": "图视图文件夹。"
  },
  {
    "id": "c_workshop_3d_views",
    "label_en": "3D Views",
    "label_zh": "三维视图",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 6,
    "position": "候选下第 6 行",
    "description_zh": "三维视图文件夹。"
  },
  {
    "id": "c_workshop_charts",
    "label_en": "Charts",
    "label_zh": "图表",
    "type": "group",
    "parent": "c_workshop",
    "level": 1,
    "order": 7,
    "position": "候选下第 7 行",
    "description_zh": "图表文件夹。"
  },
  {
    "id": "c_portfolio",
    "label_en": "Austin Portfolio Candidate",
    "label_zh": "奥斯汀组合候选",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "order": 2,
    "position": "第 9 行（折叠，顶层）",
    "description_zh": "组合目的的候选架构容器。"
  },
  {
    "id": "c_project_controls",
    "label_en": "Austin Workshop Project Controls Candidate (Project)",
    "label_zh": "奥斯汀工作坊项目控制候选（项目）",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "order": 3,
    "position": "第 10 行（折叠，顶层）",
    "description_zh": "项目目的的候选架构容器。"
  },
  {
    "id": "c_field_data",
    "label_en": "Austin Workshop Field Data Capture Candidate (Solution Delivery)",
    "label_zh": "奥斯汀工作坊现场数据采集候选（解决方案交付）",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "order": 4,
    "position": "第 11 行（折叠，顶层）",
    "description_zh": "解决方案交付目的的候选架构容器。"
  }
]
```

## 关系

```json
[
  {
    "from": "c_workshop",
    "to": "c_workshop_components",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "c_workshop",
    "to": "c_workshop_connections",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "c_workshop",
    "to": "c_workshop_catalogues",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "c_workshop",
    "to": "c_workshop_matrices",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "c_workshop",
    "to": "c_workshop_diagrams",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "c_workshop",
    "to": "c_workshop_3d_views",
    "type": "composition",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "树状包含线。"
  },
  {
    "from": "c_workshop",
    "to": "c_workshop_charts",
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
    "meaning_zh": "架构/候选容器",
    "explicit": false
  },
  {
    "symbol": "红色三点、紫色三角、表格、交叉、图形、彩色柱等图标",
    "meaning_zh": "七类视角文件夹（组件/连接/目录/矩阵/图/三维视图/图表）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "竖直树：第一行是展开的候选根，下面缩进七行视角文件夹；随后在同一顶层缩进位置依次列出三个折叠的候选容器；画面无标题、无图例。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig5-2",
    "relation": "related",
    "note_zh": "同一工具的前一张截图，展示一个架构的候选/目标/现状/过渡容器；本图展示多个并列的候选容器。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四个候选容器之上是否还有一个未显示的共同父节点，无法从截图中确认；按顶层并列处理。",
    "三个额外候选的展开状态均为折叠（+），无法看到它们内部的视角结构。",
    "“Project Controls”与“Field Data Capture”是示例项目名，正文未解释其具体内容。"
  ],
  "analyzed_from": [
    "英文 PDF 第 52 页图 5-3 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 52 页正文",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 592–614 行及标签对照表 L598–L613",
    "figs/g186e_fig5-3_en.png 与 figs/zh/g186e_fig5-3_zh.png"
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
