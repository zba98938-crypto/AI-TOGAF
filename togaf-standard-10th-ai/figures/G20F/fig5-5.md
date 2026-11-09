# G20F/fig5-5 · 产品与项目

> 当前图示解析：[Markdown](../../architecture/diagrams/G20F/fig5-5.md) · [JSON](../../architecture/diagrams/G20F/fig5-5.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G20Fe.pdf`；SHA-256：`a8fe6569c7d6045ce4ac8d5320c09a3abdc556a0fc1cbcd584bd76a75f3f84be`。

## 原图 · PDF 第 45 页

![英文原图](../assets/G20F/fig5-5-p0045.png)

PDF 坐标：`[118.5, 36.0, 493.5, 174.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Products
Projects
Deliverables
> Outcomes
Activities
Resources
```

## 概要（历史解释；局部修正见上）

产品是比项目更大的容器：项目在产品内运行，消耗活动与资源，产出交付物并导向成果。

## 目的（历史解释；局部修正见上）

说明产品与项目的关系：产品管理比项目管理更宽，覆盖发现、开发、交付、长期支持维护与处置的完整生命周期；在这个生命周期内会启动多个项目与过程，项目是产品内的一个执行单元。

## 阅读顺序（历史解释；局部修正见上）

由外向内读：最大的框是 Products，里面的框是 Projects，Projects 里两个与下边缘交叠的小框是 Activities 与 Resources（交叠表示它们既属于项目，也超出单个项目的边界、在产品层面持续存在）。同一层产品框内还有 Deliverables，箭头从 Deliverables 指向框外的 Outcomes，表示交付物带来成果。

## 关键含义（历史解释；局部修正见上）

- 产品（Products）在外层，项目（Projects）在其内部：一个产品在其生命周期内可以包含多个项目。
- 项目框内是活动（Activities）与资源（Resources），二者的小框压过项目框的下边缘——表示活动与资源并不被单个项目完全占有，而是在产品层面延续。
- 交付物（Deliverables）位于产品框内、项目框外，说明交付物属于产品而不只属于某个项目。
- 箭头从交付物指向成果（Outcomes），位于产品框之外，说明成果是产品对外的结果，而非项目内部的产物。
- 正文补充：产品管理覆盖发现、开发、交付、长期支持与维护、处置；处置对数字产品往往相对简单。
- 正文举例：每个主要产品交付物可能对应一个项目，另有处理用户支持请求的过程——即产品生命周期内会调用多个项目与过程。

## 层级（历史解释；局部修正见上）

三层视觉包含：Products（最外）⊃ Projects（内层）⊃ Activities / Resources（最内，且越过项目边界）；Deliverables 与 Projects 同级、都在 Products 内；Outcomes 在产品之外，与 Products 平级。

## 线条含义（历史解释；局部修正见上）

只有一条线：从 Deliverables 指向 Outcomes 的空心右向箭头，表示交付物产生成果。其余关系全部由框的嵌套与交叠表达（包含/归属），没有连线；Activities、Resources 与 Projects 框线的交叠是刻意的，表示跨项目边界。

## 易误读点（历史解释；局部修正见上）

- 不要把 Activities 与 Resources 读成项目的子步骤：它们的小框刻意压过项目框边线，表示在产品层面跨项目存在。
- 不要把 Outcomes 读成产品内部产物：它画在产品框之外，是交付物带来的外部结果。
- 不要以为一个产品只有一个项目：外层 Products 框明显大于 Projects 框，正文也说明生命周期内会启动多个项目。
- 中文稿把该图标注为“英文原图”，实际引用的是中文化 PNG；内容本身忠实，不影响理解。

## 元素

```json
[
  {
    "id": "products",
    "label_en": "Products",
    "label_zh": "产品",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "最外层大框"
  },
  {
    "id": "projects",
    "label_en": "Projects",
    "label_zh": "项目",
    "type": "group",
    "parent": "products",
    "level": 2,
    "position": "产品框内左侧"
  },
  {
    "id": "activities",
    "label_en": "Activities",
    "label_zh": "活动",
    "type": "process",
    "parent": "projects",
    "level": 3,
    "position": "项目框内左下，下边缘越出项目框"
  },
  {
    "id": "resources",
    "label_en": "Resources",
    "label_zh": "资源",
    "type": "resource",
    "parent": "projects",
    "level": 3,
    "position": "项目框内中下，下边缘越出项目框"
  },
  {
    "id": "deliverables",
    "label_en": "Deliverables",
    "label_zh": "交付物",
    "type": "artifact",
    "parent": "products",
    "level": 2,
    "position": "产品框内中部、项目框之外"
  },
  {
    "id": "outcomes",
    "label_en": "Outcomes",
    "label_zh": "成果",
    "type": "goal",
    "parent": null,
    "level": 1,
    "position": "产品框之外右侧"
  }
]
```

## 关系

```json
[
  {
    "from": "deliverables",
    "to": "outcomes",
    "type": "produces",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "空心右向箭头：交付物带来成果"
  },
  {
    "from": "activities",
    "to": "deliverables",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "活动与交付物同在产品框内、由位置隐含（图中未画线）"
  },
  {
    "from": "resources",
    "to": "projects",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "资源框与项目框交叠，隐含资源支撑项目实施"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_value",
    "kind": "sequence",
    "name_zh": "从项目执行到成果",
    "steps": [
      "activities",
      "deliverables",
      "outcomes"
    ],
    "description_zh": "活动产出交付物，交付物带来成果；除最后一段外均为位置隐含。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "外层大矩形",
    "meaning_zh": "产品（Products）",
    "explicit": true
  },
  {
    "symbol": "内层矩形",
    "meaning_zh": "项目（Projects）",
    "explicit": true
  },
  {
    "symbol": "与项目框下边缘交叠的小矩形",
    "meaning_zh": "活动与资源（跨项目边界存在）",
    "explicit": false
  },
  {
    "symbol": "空心右向箭头",
    "meaning_zh": "交付物产生成果",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "单层嵌套结构：大框 Products 内左侧是 Projects 框（框内两个小框 Activities、Resources 下边缘越出 Projects 框），中部是 Deliverables 框；Products 框右侧一个空心箭头指向独立的 Outcomes 框。"
}
```

## 相关图

```json
[
  {
    "target": "G20F/fig5-4",
    "relation": "related",
    "note_zh": "同属 5.3 节：图 5-4 展示产品/冲刺待办的运转，本图界定产品与项目的包含关系。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中没有文字说明“交叠”的含义，Activities/Resources 压过项目边线表示跨项目边界属版式推断。",
    "原图内无标题，中文图题“产品与项目”按英文标题直译；英文标题另注明基于 DPBoK 标准 Figure 43。"
  ],
  "analyzed_from": [
    "英文 PDF 第 45 页原图截图（figctx GT crop + 2x2 放大块）",
    "英文 PDF 第 44–45 页正文与图题",
    "中文稿 G20Fe_赋能企业敏捷性.md 第 635–641 行",
    "figs/g20fe_fig5-5_en.png 与 figs/zh/g20fe_fig5-5_zh.png"
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
