# G184/fig7-1 · 框架族之间的关系（TOGAF 标准——ADM 技术图 3-1 [C220] 的抽象视图）

> 当前图示解析：[Markdown](../../architecture/diagrams/G184/fig7-1.md) · [JSON](../../architecture/diagrams/G184/fig7-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G184e.pdf`；SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

## 原图 · PDF 第 70 页

![英文原图](../assets/G184/fig7-1-p0070.png)

PDF 坐标：`[125.6, 36.0, 486.4, 301.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Public / Private / Social
The O
Strategy Models
Enterprise
Architecture
Execution
Management
Frameworks
Frameworks
Project
Quality /
Management
People / Financial
```

## 概要（历史解释；局部修正见上）

三类框架族（战略模型、执行框架、管理框架）相互交叠，企业架构位于三者共同交集。

## 目的（历史解释；局部修正见上）

说明框架族之间的关系：企业按经济、问责与执行模型把框架分组后，会得到类似本图的重叠视图；EA 能力不是第四类独立框架，而是位于战略、执行、管理三族框架的交集，需要同时吸收三者的成果，并在缺口处补位。图题说明它是 TOGAF 标准——ADM 技术图 3-1 [C220] 的抽象视图。

## 阅读顺序（历史解释；局部修正见上）

先看三个大圆：上方浅蓝圆是 Strategy Models（战略模型），左下浅绿圆是 Execution Frameworks（执行框架），右下浅粉圆是 Management Frameworks（管理框架）；三圆两两重叠。中央深色小圆落在三圆共同交叠处，右侧“Enterprise Architecture”用引线箭头指向它，表示 EA 位于三族交集。圆外的三段文字各自贴近一个圆，示意该族框架的典型语境或示例。图中没有其他连线。

## 关键含义（历史解释；局部修正见上）

- 三个框架族分别是战略模型、执行框架、管理框架；它们相互交叠而不是互斥分类。
- Enterprise Architecture 画在三圆共同交集处，说明 EA 同时涉及战略、执行与管理三类框架，不是与它们并列的第四类框架。
- 圆外注记与三个圆一一对应：Public / Private / Social 贴近战略模型，Project Management 贴近执行框架，Quality / People / Financial 贴近管理框架；它们说明各族的典型适用范围或示例，没有引线连接。
- 图题明确本图是 TOGAF 标准——ADM 技术图 3-1 [C220] 的抽象视图，不是完整的框架映射表。
- 正文用“重叠视图”描述按经济、问责与执行模型（如风险、会计、规划）对框架分组的结果，并强调要厘清从每个框架、方法或技术中究竟需要什么。
- 7.2 节据此提出“融入/补位”策略：其他框架已提供规划、变更治理与收益实现的成果时，EA 能力融入；出现缺口时，EA 能力补位并调整路线图。
- 圆的大小与交叠面积没有量化含义，图中也没有图例；不要据此判断框架数量、成熟度或重要性。

## 层级（历史解释；局部修正见上）

没有上下级。三个大圆是并列的框架族，中央小圆是三者交集而非某个大圆的下级；圆外三段文字是旁注，不是层级节点。图中唯一的方向符号是“Enterprise Architecture”到中央小圆的标签引线。

## 线条含义（历史解释；局部修正见上）

只有一个画出的箭头：从右侧“Enterprise Architecture”文字指向中央深色小圆，属于标签引线，不表示流程方向。三个大圆之间的关系完全由圆的重叠表达，没有连线；圆外注记与圆之间也没有连线，对应关系由位置推断。

## 易误读点（历史解释；局部修正见上）

- 不要把 Enterprise Architecture 读成第四个圆或第四类框架；它是三个框架族的交集。
- 不要把圆的大小或交叠面积当作框架数量、成熟度、重要性或覆盖比例；图中没有任何量化编码。
- 不要把圆外注记（Public/Private/Social、Project Management、Quality/People/Financial）当作三个独立框架节点；它们是各族的语境/示例说明，且没有引线。
- 不要把“Enterprise Architecture”的引线箭头理解为 EA 指向战略模型或从战略模型获取输入；它只是把标签指向中央小圆。
- 不要把本图当作 TOGAF ADM 技术图 3-1 的完整复制；图题说明它只是抽象视图，细节需回到 [C220]。
- 中文资产把“Enterprise Architecture”排成两行，箭头仍指向中央圆，不要误读为指向右侧某个圆。

## 元素

```json
[
  {
    "id": "fw_strategy",
    "label_en": "Strategy Models",
    "label_zh": "战略模型",
    "type": "group",
    "parent": null,
    "position": "上方大圆（浅蓝）",
    "description_zh": "三类框架族之一：战略模型；圆外上方注记为 Public / Private / Social。"
  },
  {
    "id": "fw_execution",
    "label_en": "Execution Frameworks",
    "label_zh": "执行框架",
    "type": "group",
    "parent": null,
    "position": "左下大圆（浅绿）",
    "description_zh": "三类框架族之一：执行框架；圆外左下方注记为 Project Management。"
  },
  {
    "id": "fw_management",
    "label_en": "Management Frameworks",
    "label_zh": "管理框架",
    "type": "group",
    "parent": null,
    "position": "右下大圆（浅粉）",
    "description_zh": "三类框架族之一：管理框架；圆外右下方注记为 Quality / People / Financial。"
  },
  {
    "id": "ea_overlap",
    "label_en": null,
    "label_zh": "三族框架的交叠区（企业架构所在）",
    "type": "concept",
    "parent": null,
    "position": "中央深色小圆",
    "description_zh": "位于三个大圆的共同交集，表示 Enterprise Architecture；圆本身不带文字，由右侧引线标签命名。"
  },
  {
    "id": "ea_label",
    "label_en": "Enterprise Architecture",
    "label_zh": "企业架构",
    "type": "note",
    "parent": null,
    "position": "右侧，两行文字",
    "description_zh": "图内唯一的文字标签加引线箭头；箭头指向中央深色小圆。"
  },
  {
    "id": "ctx_sector",
    "label_en": "Public / Private / Social",
    "label_zh": "公共/私营/社会",
    "type": "note",
    "parent": null,
    "position": "图顶、战略模型圆外",
    "description_zh": "贴近战略模型圆的无引线注记，示意该族框架跨越公共、私营与社会部门语境（含义据位置推断）。"
  },
  {
    "id": "ctx_project",
    "label_en": "Project Management",
    "label_zh": "项目管理",
    "type": "note",
    "parent": null,
    "position": "左下、执行框架圆外",
    "description_zh": "贴近执行框架圆的无引线注记，项目管理是其典型示例（含义据位置推断）。"
  },
  {
    "id": "ctx_quality",
    "label_en": "Quality / People / Financial",
    "label_zh": "质量/人员/财务",
    "type": "note",
    "parent": null,
    "position": "右下、管理框架圆外",
    "description_zh": "贴近管理框架圆的无引线注记，示意该族覆盖质量、人员与财务等管理领域（含义据位置推断）。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_label_ea",
    "from": "ea_label",
    "to": "ea_overlap",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "标签引线：右侧“Enterprise Architecture”文字指向中央深色小圆，不是流程箭头。"
  },
  {
    "id": "r_ea_strategy",
    "from": "ea_overlap",
    "to": "fw_strategy",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "中央小圆位于三圆共同交叠处，表示 EA 属于战略模型族的交集（由位置推断）。"
  },
  {
    "id": "r_ea_execution",
    "from": "ea_overlap",
    "to": "fw_execution",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上，EA 与执行框架族相交。"
  },
  {
    "id": "r_ea_management",
    "from": "ea_overlap",
    "to": "fw_management",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上，EA 与管理框架族相交。"
  },
  {
    "id": "r_sector_strategy",
    "from": "ctx_sector",
    "to": "fw_strategy",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "圆外注记位于战略模型圆上方，示意该族适用于公共/私营/社会语境（推断）。"
  },
  {
    "id": "r_project_execution",
    "from": "ctx_project",
    "to": "fw_execution",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "圆外注记位于执行框架圆左下方，项目管理为其示例（推断）。"
  },
  {
    "id": "r_quality_management",
    "from": "ctx_quality",
    "to": "fw_management",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "圆外注记位于管理框架圆右下方，质量/人员/财务为其覆盖领域（推断）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "半透明大圆",
    "meaning_zh": "一个框架族（战略模型 / 执行框架 / 管理框架）",
    "explicit": false
  },
  {
    "symbol": "圆的重叠区域",
    "meaning_zh": "两个或三个框架族共同关注的领域",
    "explicit": false
  },
  {
    "symbol": "中央深色小圆",
    "meaning_zh": "企业架构：三个框架族的共同交集",
    "explicit": false
  },
  {
    "symbol": "实线引线箭头",
    "meaning_zh": "把“Enterprise Architecture”标签指向中央小圆",
    "explicit": false
  },
  {
    "symbol": "圆外无引线文字",
    "meaning_zh": "该族框架的典型语境或示例（Public/Private/Social、Project Management、Quality/People/Financial）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "三个等大的半透明圆呈品字形交叠：战略模型在上、执行框架在左下、管理框架在右下；中央深色小圆位于三圆共同交集。三段圆外注记分别位于上方、左下、右下，企业架构标签在右侧并以引线箭头指向中央小圆。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "圆外三段注记（Public/Private/Social、Project Management、Quality/People/Financial）没有引线或图例，其确切作用（适用范围、示例框架族、还是输入来源）只能按位置推断，标为 implicit。",
    "骨架的 title_en 在“TOGAF Standard”处被截断；完整图题见英文 PDF 第 70 页图注，本分析未改写 title_en。",
    "图题引用的 TOGAF Standard – ADM Techniques Figure 3-1 [C220] 不在当前图表库中，无法建立跨文档 related_figures 链接。",
    "中央深色小圆没有自己的文字，其含义由右侧“Enterprise Architecture”引线确定；该箭头按标签引线处理。",
    "三圆交叠面积与圆的大小是否编码任何比例，图中无说明，未作推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 70 页图 7-1 截图与 2x2 放大分块",
    "英文 PDF 第 69、70 页正文",
    "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 610-621 行",
    "figs/zh/g184e_fig7-1_zh.png"
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
