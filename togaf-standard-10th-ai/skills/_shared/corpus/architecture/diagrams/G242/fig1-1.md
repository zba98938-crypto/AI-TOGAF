# G242/fig1-1 · 2010–2025 年全球年度产生的数据量

类型：`analytical-view`。用一条不断加速上升的柱状曲线，让读者直观感受“数据洪流”的规模：2025 年将达到 181 ZB，是 2018 年的 5.5 倍。作者借此说明每个新增字节都要耗能存储、都会带来额外碳排放，从而为“清理存量数据、新增存储只留给最有用的用例”这一主张提供量级依据。

英文 PDF 物理页：[21]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 21 页原图](../../../figures/assets/G242/fig1-1-p0021.png)

[完整 JSON](fig1-1.json) · [可编辑 Mermaid](fig1-1.mmd) · [仅关系图](fig1-1.relations.mmd) · [层级分解图](fig1-1.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Global Data Generated Annually"]
  n1["Data Generated (zettabytes)"]
  n2["Year"]
  n3["0, 50, 100, 150, 200"]
  n4["Global Data Generated Annually"]
```

## 架构分析

从横轴左侧 2010 年向右读至 2025 年，柱高代表该年全球产生的数据量（ZB）；纵轴只标 0、50、100、150、200。2018 年及以后的年份带星号，表示预测值。先看整体形状：2010–2016 年近乎贴地，2019 年后陡然抬升，2025 年达到最高。

- 本图有 5 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 5 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 16根柱、2010–2025年份、2018–2025星号、0/50/100/150/200刻度及轴标题逐项核对。
- 原图柱子没有数值标签；现有表数值属于估读，只有2025的181ZB及相对2018的5.5倍由正文明确给出。
- 图和本页正文均未解释星号，不能把预测含义写成已确认事实；Generated与正文stored不同措辞分别保留。

### 如何用于项目

- 围绕作者目的读取本图实体、分组与连线，并用对应原文限定其含义。
- 把参考模型与项目事实分开，实际范围、约束、值和责任须有项目证据。

### 结构所表达的逻辑

- 横轴连续覆盖2010–2025共16年；纵轴Data Generated (zettabytes)为线性0–200刻度。
- 柱高显示数据量快速上升；正文给出2025年181ZB及比2018年5.5倍两个锚点，其他数值仅为估读。
- 2018–2025标签带星号，原图未说明其含义，不把它们自动定性为已发生统计或预测。
- 图内Generated与正文stored措辞不同；不能将产生量无条件等同存储存量。
- 正文建议清理现有数据，并将新存储能力留给最有用的用例。

## 上下级与包含

无层级。图由标题、纵轴标题、横轴标题、纵轴刻度、16 根年柱与年份标签构成；年份与数值是并列的数据点，不是上下级。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|title|Global Data Generated Annually|note|图内标题；图题另注明 [Exploding Topics] 来源。|—||
|y_axis_label|Data Generated (zettabytes)|note|纵轴标题，单位 ZB。|—||
|x_axis_label|Year|note|横轴标题。|—||
|y_ticks|0, 50, 100, 150, 200|note|线性刻度，单位 ZB。|—||
|data_series|Global Data Generated Annually|metric|2010–2025 年逐年数据量，数值见表 t_data。|—||

## 全部关系

图中没有连线或箭头。唯一编码是柱高（线性映射到 ZB 数值）与年份顺序；柱与柱之间的空白不代表间隔时间。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## 2010–2025 年全球年度数据产生量（按柱高估读，单位 ZB）

```json
{
  "id": "t_data",
  "title_zh": "2010–2025 年全球年度数据产生量（按柱高估读，单位 ZB）",
  "columns": [
    "年份",
    "数据产生量（ZB，≈）",
    "原图标记"
  ],
  "rows": [
    [
      "2010",
      "2",
      ""
    ],
    [
      "2011",
      "5",
      ""
    ],
    [
      "2012",
      "6.5",
      ""
    ],
    [
      "2013",
      "9",
      ""
    ],
    [
      "2014",
      "12",
      ""
    ],
    [
      "2015",
      "15",
      ""
    ],
    [
      "2016",
      "18",
      ""
    ],
    [
      "2017",
      "26",
      ""
    ],
    [
      "2018",
      "33",
      "*（原图未释义）"
    ],
    [
      "2019",
      "41",
      "*（原图未释义）"
    ],
    [
      "2020",
      "64",
      "*（原图未释义）"
    ],
    [
      "2021",
      "79",
      "*（原图未释义）"
    ],
    [
      "2022",
      "97",
      "*（原图未释义）"
    ],
    [
      "2023",
      "120",
      "*（原图未释义）"
    ],
    [
      "2024",
      "147",
      "*（原图未释义）"
    ],
    [
      "2025",
      "181",
      "*（原图未释义）"
    ]
  ],
  "cell_legend": [
    "数值按柱高估读，不是原图打印值；2025=181 ZB由PDF第21页正文明确给出。",
    "2018–2025年份后有星号；源图及本页正文没有解释星号。"
  ],
  "notes_zh": "2025 年 181 ZB 与正文一致；2018 年按“2025 为 2018 的 5.5 倍”反推约 33 ZB，与柱高吻合。"
}
```

## 误读检查

- 表中估读值不能当作精确测量结果或当前年度实际值。
- 源文没有星号图例，预测解释只是猜测。
- 本图不支持按柱高直接计算某企业的排放量。

## 原文证据

### [PDF 第 21 页](../../../documents/G242.md#page-21)

> According to a study led by Exploding Topics [Exploding Topics]: “the volume of stored data will reach 181 ZB (zettabytes) in 2025; i.e. 5.5 times more than that what was stored in 2018”; see Figure 1-1. The Digitization of the World – From Edge to Core [IDC, 2018] is an older reference, providing a similar order of magnitude. As each additional byte requires energy to be stored, this generates additional carbon emissions. Given today’s goal of CO2 emissions reduction, ICT professionals must try to stabilize this trend by cleansing current data stocks and dedicating new storage capabilities to only the most useful data use-cases only.
> Figure 1-1: Global Data Generated Annually 2010-2025 [Exploding Topics]

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

源图记录：[原始解释与转录](../../../figures/G242/fig1-1.json)。

```json
{
  "quality": {
    "graph_integrity": "checked",
    "semantic_analysis": "typed-graph-and-context-analysis",
    "visual_review": "source-content-audited",
    "notice_zh": "所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。"
  },
  "source_uncertainty": {
    "confidence": "high",
    "uncertainties_zh": [
      "除 2025 年 181 ZB 外，原图未标任何数值，逐年数值按柱高估读，误差约 ±1–2 ZB（小数值年份相对误差更大）。",
      "原图未说明年份星号含义，按常见做法解释为预测值。",
      "图题用 Generated、正文用 stored data，两者口径略有差异。"
    ],
    "analyzed_from": [
      "英文 PDF 第 21 页原图截图（1115×847）",
      "英文 PDF 第 21 页正文",
      "中文稿 G242e_环境可持续的信息系统.md 第 162–198 行",
      "figs/zh/g242_fig1-1_zh.svg 源码",
      "figs/g242_fig1-1.svg 源码文本",
      "figs/g242_fig1-1_en.png"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
