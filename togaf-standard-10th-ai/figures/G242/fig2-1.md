# G242/fig2-1 · 本文档使用的 ArchiMate 建模记法元素

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig2-1.md) · [JSON](../../architecture/diagrams/G242/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 26 页

![英文原图](../assets/G242/fig2-1-p0026.png)

PDF 坐标：`[125.6, 223.3, 486.4, 345.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business
Function
```

## 概要（历史解释；局部修正见上）

以战略层和业务层两行示例，给出本文档所用的 Capability 与 Business Function 记法。

## 目的（历史解释；局部修正见上）

在进入具体架构内容前，先固定本文档使用的 ArchiMate 元素子集及其画法：哪个层、用什么形状、右上角用什么图标。读者据此能认出后文各图中黄色圆角矩形分别代表能力还是业务功能。

## 阅读顺序（历史解释；局部修正见上）

自上而下读两行：灰色带标题是架构层（Strategy、Business），带内的黄色圆角矩形是该层的元素样例，右上角小图标是 ArchiMate 的元素类型符号。每一行只给一个元素，不是完整元素清单。

## 关键含义（历史解释；局部修正见上）

- 战略层的示例元素是 Capability（能力），记法为黄色圆角矩形 + 右上角能力图标。
- 业务层的示例元素是 Business Function（业务功能），记法为黄色圆角矩形 + 右上角功能图标。
- 两张黄色框外形相同，靠右上角图标区分元素类型；阅读后文时必须看图标，不能只看框形。
- 原图在页面上被裁切，只显示 Strategy 与 Business 两行，正文随后用文字补充这两个概念的定义。
- 图题声称给出“本文档使用的 ArchiMate 元素”，但可见内容仅是子集的开头两行，不能把它当作完整记法清单。

## 层级（历史解释；局部修正见上）

两层：灰色层带（Strategy、Business）为容器，黄色元素框（Capability、Business Function）分别位于对应层带之内；层带之间上下排列，无连线。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。层与元素的从属关系完全由“元素框位于层带内”表达；元素类型由右上角图标编码。

## 易误读点（历史解释；局部修正见上）

- 这不是完整的 ArchiMate 元模型，只是两个元素的样例；不能据此认为本文档只用 Capability 和 Business Function。
- 不要把灰色层带当成元素；它只是分层背景。
- 不要忽略右上角小图标：两个黄框形状相同，图标才是类型标记。
- 原图底部被裁切，不能把“只有两行”理解为作者只定义了这两层。

## 元素

```json
[
  {
    "id": "strategy_layer",
    "label_en": "Strategy",
    "label_zh": "战略层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "上方的灰色层带",
    "description_zh": "ArchiMate 战略层，作为 Capability 的容器。"
  },
  {
    "id": "capability",
    "label_en": "Capability",
    "label_zh": "能力",
    "type": "capability",
    "parent": "strategy_layer",
    "level": 2,
    "position": "战略层带内左侧",
    "description_zh": "黄色圆角矩形，右上角为能力图标。"
  },
  {
    "id": "capability_icon",
    "label_en": null,
    "label_zh": "能力记法图标",
    "type": "note",
    "parent": "capability",
    "position": "能力框右上角",
    "description_zh": "由三个小方块叠成的 ArchiMate 能力图标。"
  },
  {
    "id": "business_layer",
    "label_en": "Business",
    "label_zh": "业务层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "下方的灰色层带",
    "description_zh": "ArchiMate 业务层，作为 Business Function 的容器。"
  },
  {
    "id": "business_function",
    "label_en": "Business Function",
    "label_zh": "业务功能",
    "type": "function",
    "parent": "business_layer",
    "level": 2,
    "position": "业务层带内左侧",
    "description_zh": "黄色圆角矩形，右上角为功能图标。"
  },
  {
    "id": "function_icon",
    "label_en": null,
    "label_zh": "业务功能记法图标",
    "type": "note",
    "parent": "business_function",
    "position": "业务功能框右上角",
    "description_zh": "折角/屋脊形的 ArchiMate 功能图标。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色横带（Strategy / Business）",
    "meaning_zh": "ArchiMate 架构层（战略层、业务层）",
    "explicit": false
  },
  {
    "symbol": "黄色圆角矩形",
    "meaning_zh": "该层的一个 ArchiMate 元素",
    "explicit": false
  },
  {
    "symbol": "元素框右上角的小图标",
    "meaning_zh": "ArchiMate 元素类型符号（能力图标 / 功能图标）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "上下两行：每行左侧是灰色层带标题，右侧延伸为浅灰底带；带内左侧放一个黄色圆角元素框，框右上角为 ArchiMate 图标。整体在页面中部，底部被页面边界裁断。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-1",
    "relation": "related",
    "note_zh": "图 3-1 的七个高层业务功能块均使用本图定义的 ArchiMate 功能记法与图标"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图在 PDF 页面底部被裁切，只显示两行；被裁掉部分（若有）无法核对。",
    "右上角图标的具体图形细节在原图分辨率下只能辨认为 ArchiMate 能力/功能符号，未逐笔核对。"
  ],
  "analyzed_from": [
    "英文 PDF 第 26 页原图截图与整页截图",
    "英文 PDF 第 26 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 279–308 行",
    "figs/zh/g242_fig2-1_zh.png",
    "figs/g242_fig2-1_en.png"
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
