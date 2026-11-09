# G178/fig1-2 · 价值流建模关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G178/fig1-2.md) · [JSON](../../architecture/diagrams/G178/fig1-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G178e.pdf`；SHA-256：`517130a041a8d956b2868dc39d570b84e2d80c64709e4c1368f9747388a3a026`。

## 原图 · PDF 第 13 页

![英文原图](../assets/G178/fig1-2-p0013.png)

PDF 坐标：`[61.1, 36.0, 550.9, 387.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
operationalizes >
© The Open Group
Process
Capability
WV enables
operationalizes W
participates in >
Value Stage
consists of &
triggers >
Stakeholder
Value Stream
creates W
receives >
Value
```

## 概要（历史解释；局部修正见上）

价值流建模的核心元模型：利益相关者触发价值流、参与价值阶段并接收价值；价值流由价值阶段组成并创造价值；能力使能阶段，流程落实阶段与能力。

## 目的（历史解释；局部修正见上）

说明价值流与其他基础业务架构概念（利益相关者、价值、能力、流程）之间的关系，为后文把价值流阶段映射到业务能力（如图 4-3）和业务流程提供概念依据。

## 阅读顺序（历史解释；局部修正见上）

每条连线都按“主语—动词—宾语”读：标签旁的实心三角指向宾语。例如“consists of ▲”位于价值阶段与价值流之间、三角朝上，读作“价值流由价值阶段组成”。线条本身没有箭头。图左侧的利益相关者通过三条线分别连到价值阶段、价值流和价值；右上方的流程与能力通过顶部的横线相连。

## 关键含义（历史解释；局部修正见上）

- 利益相关者在价值流中有三个角色：触发价值流（triggers）、参与其中的价值阶段（participates in）、接收最终价值（receives）。
- 价值流由一个或多个价值阶段组成（consists of），整体创造价值（creates）；正文说明价值流的价值是各阶段所交付增量价值项的汇总。
- 能力使能价值阶段（enables）：能力回答“做什么”，价值流回答“价值如何实现”，二者分离但通过“使能”关系联系起来。图 4-3 就是这条关系的实例。
- 流程有两条“落实（operationalizes）”关系：流程落实价值阶段，也落实能力。正文指出阶段到流程不是一对一，一个阶段可映射到一个或多个业务流程。
- 价值流采取由外而内（客户/最终用户）视角，流程更偏内部运营视角且粒度更细（中文稿 L116）。

## 层级（历史解释；局部修正见上）

本图没有容器嵌套。唯一的“整体—部分”关系是价值流由价值阶段组成；其他都是同级概念之间的关联。纵向上，流程与能力位于最上层（实现与使能层），价值阶段、价值流、价值依次在下。

## 线条含义（历史解释；局部修正见上）

全部为细实线，没有箭头。方向只由标签旁的实心三角（▶▼▲）表示，三角指向关系的宾语（正文明确说明）。关系清单中的 from→to 即按该方向记录的主语→宾语。

## 易误读点（历史解释；局部修正见上）

- 不要把标签旁的三角当作连线的箭头或数据流方向，它只表示读法。
- “consists of ▲”的主语是下方的价值流，不是上方的价值阶段。
- 原图写的是“Value Stage（价值阶段）”，即价值流阶段；图中没有组织单元或业务模型（中文稿引用的重绘 SVG 加入了这两个节点）。

## 元素

```json
[
  {
    "id": "stakeholder",
    "label_en": "Stakeholder",
    "label_zh": "利益相关者",
    "type": "stakeholder",
    "position": "左侧中部"
  },
  {
    "id": "value",
    "label_en": "Value",
    "label_zh": "价值",
    "type": "goal",
    "position": "右列底部"
  },
  {
    "id": "value_stream",
    "label_en": "Value Stream",
    "label_zh": "价值流",
    "type": "value_stream",
    "position": "右列中部"
  },
  {
    "id": "value_stage",
    "label_en": "Value Stage",
    "label_zh": "价值阶段（价值流阶段）",
    "type": "value_stream_stage",
    "position": "右列上部"
  },
  {
    "id": "process",
    "label_en": "Process",
    "label_zh": "流程",
    "type": "process",
    "position": "顶部左"
  },
  {
    "id": "capability",
    "label_en": "Capability",
    "label_zh": "能力",
    "type": "capability",
    "position": "顶部右"
  }
]
```

## 关系

```json
[
  {
    "from": "stakeholder",
    "to": "value_stage",
    "type": "assignment",
    "label_en": "participates in",
    "label_zh": "参与",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "stakeholder",
    "to": "value_stream",
    "type": "triggering",
    "label_en": "triggers",
    "label_zh": "触发",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "stakeholder",
    "to": "value",
    "type": "association",
    "label_en": "receives",
    "label_zh": "接收",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "value_stream",
    "to": "value_stage",
    "type": "composition",
    "label_en": "consists of",
    "label_zh": "由……组成",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "三角朝上指向价值阶段"
  },
  {
    "from": "value_stream",
    "to": "value",
    "type": "produces",
    "label_en": "creates",
    "label_zh": "创造",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "capability",
    "to": "value_stage",
    "type": "serving",
    "label_en": "enables",
    "label_zh": "使能",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "process",
    "to": "value_stage",
    "type": "realization",
    "label_en": "operationalizes",
    "label_zh": "落实",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "process",
    "to": "capability",
    "type": "realization",
    "label_en": "operationalizes",
    "label_zh": "落实",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "顶部横线，三角朝右指向能力"
  }
]
```

## 图例

```json
[
  {
    "symbol": "矩形",
    "meaning_zh": "业务架构概念",
    "explicit": false
  },
  {
    "symbol": "细实线 + 标签",
    "meaning_zh": "两个概念之间的关系（标签即关系动词）",
    "explicit": false
  },
  {
    "symbol": "标签旁的实心三角 ▶▼▲",
    "meaning_zh": "阅读方向：三角指向关系的宾语",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "BT",
  "description_zh": "右列自下而上：价值 → 价值流 → 价值阶段 → 上方并列的流程与能力；左侧的利益相关者用三条横线连到右列三个框。"
}
```

## 相关图

```json
[
  {
    "target": "G178/fig4-2",
    "relation": "generalizes",
    "note_zh": "图 4-2 的招聘员工价值流是“价值流由价值阶段组成”的实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 13 页原图截图（220 dpi）",
    "英文 PDF 第 12 页正文",
    "中文稿 G178e_价值流.md 第 108–116 行",
    "figs/g178_fig1-2.svg 源码"
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
