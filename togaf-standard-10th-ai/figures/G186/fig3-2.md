# G186/fig3-2 · 带一个架构项目的 EA 全景

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig3-2.md) · [JSON](../../architecture/diagrams/G186/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 29 页

![英文原图](../assets/G186/fig3-2-p0029.png)

PDF 坐标：`[151.3, 36.0, 460.7, 271.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
0"
oe
oO
```

## 概要（历史解释；局部修正见上）

在 EA 全景立方体内部，用一块红色半透明小立方体标出单个架构项目覆盖的范围。

## 目的（历史解释；局部修正见上）

把图 3-1 的抽象体积落到一个具体架构项目上：项目不是整个全景，而是在广度、规划期、详细程度三个方向上各取一段的一个子体积；作者用这张图说明“架构工作请求”为何必须界定范围，以及项目产出只是填充/刷新全景的一部分。

## 阅读顺序（历史解释；局部修正见上）

先把它看成图 3-1 的同一个立方体：外框是 EA 全景，三条粗箭头仍是 Breadth (Subject)、Time、Detail。再看悬浮在内部的红色半透明小块，它就是这一个架构项目的切片。比较切片与外框在三条轴上的位置：切片在每条轴上都只占中间一段，四周都留有未覆盖的空间。图中没有文字标注这个红块，它的含义来自图题和正文。

## 关键含义（历史解释；局部修正见上）

- 红色切片只覆盖 EA 全景的一部分：不是全部主题、不是全部时期、也不是最粗或最细的所有层级。
- 切片在三条轴上都“内缩”，不贴外框边界；正文明确说示例不覆盖最粗或最细的层，也不覆盖所有时期或主题。
- 架构项目的产出是填充、替换或重申 EA 全景中这一块的内容，而不是重画整个全景。
- 切片内的所有工作都受更高层架构约束；更高层架构可能是未实现的目标、未实现的过渡，或已实现的现状。
- 若更高层架构没有显式变更，现状通常仍然有效；项目不能自行假定上层已变。
- 范围之外的工作可能有趣、未来也可能需要，但不属于本次架构举措；TTM 取决于是否守住广度、时间、详细程度三条边界。
- 立方体与切片都是示意：正文说真实情形更像海胆，尖刺伸向四面八方，而不是整齐的方块。

## 层级（历史解释；局部修正见上）

视觉上是“外立方体 ⊃ 内部红色切片”的包含关系：外层是 EA 全景（全部潜在架构），内层是一个架构项目的覆盖范围。三条轴是外层立方体的维度，不是切片的子元素；图中没有画出更高层架构或产出的独立框。

## 线条含义（历史解释；局部修正见上）

图中只有三条粗箭头轴（与图 3-1 相同），没有连接两个框的语义线。项目与全景的关系完全由“小块位于大块内部”这一空间包含表达；切片与外框之间的空白表示未覆盖的范围。

## 易误读点（历史解释；局部修正见上）

- 不要把红色小块读成“解决方案”“现状”或“目标状态”；它只表示一个架构项目的覆盖范围，颜色没有状态含义。
- 不要以为切片贴着外框：它在三条轴上都留有未覆盖的层与时段，这正是本图要强调的。
- 不要从红块的大小推算项目工作量或预算；图没有刻度。
- 原图没有任何文字说明红块，必须结合图题与正文，否则容易把内部小块误认成“目标架构”。
- 中文稿当前引用的 figs/g186_fig3-2.svg 已把立方体换成流程框，不能据它理解“切片在体积中的位置”。

## 元素

```json
[
  {
    "id": "ea_landscape_volume",
    "label_en": null,
    "label_zh": "EA 全景（外层立方体）",
    "type": "architecture",
    "parent": null,
    "level": 0,
    "position": "外层大立方体",
    "description_zh": "原图未标注；由与图 3-1 相同的立方体和图题可知其为 EA 全景。"
  },
  {
    "id": "project_slice",
    "label_en": null,
    "label_zh": "架构项目切片（红色小块）",
    "type": "architecture",
    "parent": "ea_landscape_volume",
    "level": 1,
    "position": "大立方体内部中央偏左",
    "description_zh": "一个架构项目覆盖的子体积，在三条轴上各占一段；原图无文字标签。"
  },
  {
    "id": "dim_breadth",
    "label_en": "Breadth (Subject)",
    "label_zh": "广度（主题）",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "position": "上边缘，箭头向右上",
    "description_zh": "主题范围维度。"
  },
  {
    "id": "dim_time",
    "label_en": "Time",
    "label_zh": "时间",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "position": "顶面，箭头斜向右前",
    "description_zh": "规划期维度；本图只写 Time，未加 Planning Horizon。"
  },
  {
    "id": "dim_detail",
    "label_en": "Detail",
    "label_zh": "详细程度",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "position": "左前竖边，箭头向下",
    "description_zh": "详细程度维度。"
  }
]
```

## 关系

```json
[
  {
    "from": "ea_landscape_volume",
    "to": "project_slice",
    "type": "composition",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "切片位于立方体内部，表示项目只覆盖全景的一个子体积；原图没有画连线。"
  },
  {
    "from": "ea_landscape_volume",
    "to": "dim_breadth",
    "type": "other",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Breadth (Subject)",
    "label_zh": "广度（主题）",
    "description_zh": "沿上边缘向右上的轴箭头。"
  },
  {
    "from": "ea_landscape_volume",
    "to": "dim_time",
    "type": "other",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Time",
    "label_zh": "时间",
    "description_zh": "斜穿顶面的轴箭头，箭头末端落在红色切片附近。"
  },
  {
    "from": "ea_landscape_volume",
    "to": "dim_detail",
    "type": "other",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "label_en": "Detail",
    "label_zh": "详细程度",
    "description_zh": "沿左前竖边向下的轴箭头。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "大型半透明立方体（浅灰）",
    "meaning_zh": "EA 全景（全部潜在架构）",
    "explicit": false
  },
  {
    "symbol": "红色半透明小立方体",
    "meaning_zh": "一个架构项目覆盖的切片（广度 × 规划期 × 详细程度的子范围）",
    "explicit": false
  },
  {
    "symbol": "粗黑箭头",
    "meaning_zh": "三个维度的坐标轴，箭头指向维度增大的方向",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "与图 3-1 相同的立方体与三条粗箭头；立方体内部中央偏左悬浮一个红色半透明小立方体（切片），四周留白；无标题、无标签、无图例。"
}
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "红色切片内部可见两条水平接缝，可能是 3D 渲染的分层，也可能是表示多个详细层级；原图无标签，无法确定。",
    "切片在三条轴上的精确起止位置无法量化；只能判断它内缩、未触及外框边界。",
    "原图没有标出更高层架构或“产出”，这两层含义只能从正文补足。",
    "Time 轴箭头穿入红色切片，是透视遮挡还是刻意表达“项目处于该时段”无法区分。"
  ],
  "analyzed_from": [
    "英文 PDF 第 29 页图 3-2 截图（220 dpi）及 2×2 放大分块、切片局部 3 倍放大",
    "英文 PDF 第 29 页正文",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 197–205 行",
    "figs/g186_fig3-2.svg 的文本与结构"
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
