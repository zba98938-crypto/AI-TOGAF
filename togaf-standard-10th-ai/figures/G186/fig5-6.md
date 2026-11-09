# G186/fig5-6 · 问题解决方法（源自 Conklin 的棘手问题）

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig5-6.md) · [JSON](../../architecture/diagrams/G186/fig5-6.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 63 页

![英文原图](../assets/G186/fig5-6-p0063.png)

PDF 坐标：`[125.6, 496.4, 486.4, 701.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
— ear method
————== Desig! ject process
he
ai
ih
ime —>
y |
```

## 概要（历史解释；局部修正见上）

用红色阶梯线与绿色往复线对比“线性解题”和“设计者实际解题过程”。

## 目的（历史解释；局部修正见上）

作者要破除“问题解决是带关卡的四步直线”这一直觉：常规模型（红）从收集数据一路降到实施，而真实的专业解题（绿）在问题与解决方案之间反复跳跃。图为 5.2.3 节“迭代”提供认知依据——所以 ADM 也要反复重访阶段，而不是一次通过。

## 阅读顺序（历史解释；局部修正见上）

先看两条轴：纵向从上方 Problem 到下方 Solution 表示讨论/工作重心在问题侧还是方案侧；横向 Time 箭头指向右。红色粗线是 Linear method：四个水平台阶（收集数据→分析数据→形成解决方案→实施解决方案），每段都比前一段更低，段与段之间垂直下落。绿色细线是 Designer/subject process：在问题与方案之间快速上下往复，没有稳定的平台。右上角图例明确给出这两条线的名称。

## 关键含义（历史解释；局部修正见上）

- 线性方法（红）被画成四级台阶：Gather data → Analyze data → Formulate solution → Implement solution，每级只下降一次，不回退。
- 设计者/主体过程（绿）在 Problem 与 Solution 两个水平之间反复穿越，整个时间轴上都在摆动。
- 两条线的起点都在 Problem 侧、终点都在 Solution 侧，差别不在终点，而在过程是否往复。
- 图的含义是：线性模型适合解释流程与阶段关卡，但不代表人们实际解题的方式；真实解题需要不断在问题理解与方案尝试之间互相检验。
- 正文据此主张交互式地测试概念与潜在实现，反复考虑高层方向在执行上是否合理、执行在高层方向上是否合理。
- 浅蓝色 L 形框只是坐标轴边框，没有刻度；纵轴不是百分比或进度，只表示“更偏问题/更偏方案”。
- 图例是原图显式给出的，红/绿两色的含义不需要猜测。

## 层级（历史解释；局部修正见上）

无包含层级：两条折线是并列的两种过程模型，四个步骤是红线上的四个阶段（不是四个独立框）。纵轴两端 Problem/Solution 是水平参照，不是上下级。

## 线条含义（历史解释；局部修正见上）

红色粗折线 = Linear method，水平段表示停留在某个步骤、垂直下落表示进入下一步；绿色细折线 = Designer/subject process，斜线在 Problem 与 Solution 之间往返。横向 Time 箭头表示时间方向；浅蓝色 L 形边框是坐标轴。图中没有表示因果或包含的箭头。

## 易误读点（历史解释；局部修正见上）

- 不要把绿色往复线读成“混乱/错误过程”；它代表设计者实际的解题过程，是作者肯定的对象。
- 不要把红色阶梯线读成推荐流程；它代表常规的线性模型，作者指出它不能反映真实解题。
- 纵向位置不是完成百分比或成熟度，只表示当前更关注问题还是更关注方案。
- 四个步骤名是红色水平段的标签，不是四个并列的阶段框；红线在它们之间是连续下降的。
- 中文 PNG 只译了一个步骤名，且把“实施解决方案”写成“实施方案”；不要据其中英混排判断原图用词。

## 元素

```json
[
  {
    "id": "problem_level",
    "label_en": "Problem",
    "label_zh": "问题",
    "type": "concept",
    "notation_type": "axis_level",
    "parent": null,
    "level": 0,
    "position": "纵轴上方",
    "description_zh": "表示工作重心在问题侧。"
  },
  {
    "id": "solution_level",
    "label_en": "Solution",
    "label_zh": "解决方案",
    "type": "concept",
    "notation_type": "axis_level",
    "parent": null,
    "level": 0,
    "position": "纵轴下方",
    "description_zh": "表示工作重心在解决方案侧。"
  },
  {
    "id": "time_axis",
    "label_en": "Time",
    "label_zh": "时间",
    "type": "concept",
    "notation_type": "axis",
    "parent": null,
    "level": 0,
    "position": "横轴底部",
    "description_zh": "时间从左向右。"
  },
  {
    "id": "linear_method",
    "label_en": "Linear method",
    "label_zh": "线性方法",
    "type": "concept",
    "parent": null,
    "level": 0,
    "position": "红色粗阶梯线",
    "description_zh": "常规的带步骤关卡的问题解决模型。"
  },
  {
    "id": "gather_data",
    "label_en": "Gather data",
    "label_zh": "收集数据",
    "type": "process",
    "parent": "linear_method",
    "level": 1,
    "order": 1,
    "position": "红线第一段（最高）",
    "description_zh": "线性方法第一步。"
  },
  {
    "id": "analyze_data",
    "label_en": "Analyze data",
    "label_zh": "分析数据",
    "type": "process",
    "parent": "linear_method",
    "level": 1,
    "order": 2,
    "position": "红线第二段",
    "description_zh": "线性方法第二步。"
  },
  {
    "id": "formulate_solution",
    "label_en": "Formulate solution",
    "label_zh": "形成解决方案",
    "type": "process",
    "parent": "linear_method",
    "level": 1,
    "order": 3,
    "position": "红线第三段",
    "description_zh": "线性方法第三步。"
  },
  {
    "id": "implement_solution",
    "label_en": "Implement solution",
    "label_zh": "实施解决方案",
    "type": "process",
    "parent": "linear_method",
    "level": 1,
    "order": 4,
    "position": "红线第四段（最低）",
    "description_zh": "线性方法第四步。"
  },
  {
    "id": "designer_process",
    "label_en": "Designer/subject process",
    "label_zh": "设计者/主体过程",
    "type": "process",
    "parent": null,
    "level": 0,
    "position": "绿色往复折线",
    "description_zh": "专业人员在问题与方案之间反复检验的实际过程。"
  }
]
```

## 关系

```json
[
  {
    "from": "gather_data",
    "to": "analyze_data",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "none",
    "description_zh": "红色水平段之后垂直下落进入下一段；原图无箭头，方向由时间轴给出。"
  },
  {
    "from": "analyze_data",
    "to": "formulate_solution",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "none",
    "description_zh": "红线垂直下落进入第三段。"
  },
  {
    "from": "formulate_solution",
    "to": "implement_solution",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "none",
    "description_zh": "红线垂直下落进入第四段。"
  },
  {
    "from": "designer_process",
    "to": "problem_level",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "none",
    "description_zh": "绿色折线多次到达“问题”水平；无法逐段枚举，按整条折线与上界的往复记录。"
  },
  {
    "from": "designer_process",
    "to": "solution_level",
    "type": "association",
    "explicit": true,
    "line": "thick",
    "arrow": "none",
    "description_zh": "绿色折线多次到达“解决方案”水平。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_linear",
    "kind": "sequence",
    "name_zh": "线性方法四步",
    "steps": [
      "gather_data",
      "analyze_data",
      "formulate_solution",
      "implement_solution"
    ],
    "description_zh": "红线从问题侧逐级下降到方案侧，不回头。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "红色粗线",
    "meaning_zh": "Linear method（线性方法）",
    "explicit": true
  },
  {
    "symbol": "绿色细线",
    "meaning_zh": "Designer/subject process（设计者/主体过程）",
    "explicit": true
  },
  {
    "symbol": "浅蓝色 L 形边框",
    "meaning_zh": "坐标轴：纵轴 Problem→Solution，横轴 Time",
    "explicit": false
  },
  {
    "symbol": "横向箭头",
    "meaning_zh": "时间方向（向右）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "浅蓝色 L 形坐标框：纵轴上方标 Problem、下方标 Solution，横轴标 Time 并有向右箭头；红色粗阶梯线自左上降到右下，绿色细折线在上下之间反复摆动；右上角有一个带黑框的图例。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig5-5",
    "relation": "complements",
    "note_zh": "同属 5.2.3 节“迭代”：图 5-5 用两轮甘特计划表达阶段重访，图 5-6 用解题过程模型解释为何要重访。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "绿色折线的往复次数与拐点无法逐一对应到语义（原图没有标注每一次跳动的原因）。",
    "纵轴没有刻度，Problem 与 Solution 只是两个水平参照，无法量化“偏向”程度。",
    "红线四段的水平长度不等，但原图未说明各步骤的相对时长是否有意为之。"
  ],
  "analyzed_from": [
    "英文 PDF 第 63 页图 5-6 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 63 页正文",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 818–837 行及标签对照表 L824–L837",
    "figs/g186e_fig5-6_en.png 与 figs/zh/g186e_fig5-6_zh.png"
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
