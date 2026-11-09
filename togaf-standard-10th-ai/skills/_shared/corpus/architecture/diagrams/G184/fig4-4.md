# G184/fig4-4 · Everett Rogers 创新采用模型（又称技术扩散模型）

类型：`analytical-view`。第 4.2.7 节要求领导者识别企业采用的风险管理模型和风险偏好。当架构路线图包含采用新技术或启动转型时，作者用这条钟形曲线提问：企业落在曲线的哪个位置？企业的不同部分可能落在不同位置，需要识别并编目。

英文 PDF 物理页：[42]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 42 页原图](../../../figures/assets/G184/fig4-4-p0042.png)

[完整 JSON](fig4-4.json) · [可编辑 Mermaid](fig4-4.mmd) · [仅关系图](fig4-4.relations.mmd) · [层级分解图](fig4-4.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Innovators"]
  n1["Early Adopters"]
  n2["Early Majority"]
  n3["Late Majority"]
  n4["Laggards"]
  n5["钟形分布曲线"]
  n6["类别边界1"]
  n7["类别边界2"]
  n8["类别边界3"]
  n9["类别边界4"]
```

## 架构分析

从左到右读：横轴下方依次是五个采用者类别，竖直虚线是类别分界，每段上方的百分比是该类别占全部采用者的比例。中间那条虚线位于曲线峰值，把“大众”分成早期和晚期两半。越靠左，采用新事物越早。

- 本图有 10 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 10 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 5类名称及百分比2.5%、13.5%、34%、34%、16%逐项核对，总和100%；4条竖虚线为类别边界。
- 钟形曲线没有坐标轴名称、数值刻度或标准差符号；表格的σ范围属于背景知识，不能标成原图数据。
- 不是该企业的测量分布，正文要求判断企业及不同部门位于哪类。

### 如何用于项目

- 围绕作者目的读取本图实体、分组与连线，并用对应原文限定其含义。
- 把参考模型与项目事实分开，实际范围、约束、值和责任须有项目证据。

### 结构所表达的逻辑

- 五个采用者类别及占比：创新者 2.5%、早期采用者 13.5%、早期大众 34%、晚期大众 34%、落后者 16%，合计 100%。
- （背景知识）横轴表示采用时间，四条虚线分别位于平均采用时间之前 2 个和 1 个标准差、平均值、之后 1 个标准差，所以各段比例来自正态分布；落后者 16% 是 +1 个标准差以外的全部尾部。
- 本文档把这条曲线放在风险偏好问题中：采用新技术或启动转型时，要判断企业在曲线上的位置；企业不同部分的位置可能不同，需要识别并编目。
- 同组的其他风险偏好问题：可接受的成本偏差是多少（例如首年 10%，第二、三年 25%）；哪些类型和规模的项目要经过额外治理；若做了 SWOT 分析，威胁缓解策略是什么、如何量化；是否接受供应商锁定、利率波动等单点失败；多久复核一次风险与缓解效果，在企业何处处理。
- 正文举例：汽车保险商面对车企推出的防盗技术，可能因盗窃减少而降低理赔成本，也可能技术无效、风险敞口不变；它可以自己做防盗研究，或与执法机构和竞争对手交换数据来验证并缓解未知影响。领导者要找出企业惯用的应对模式。
- 若企业的 ERM 方法不清楚，应发起定义工作；正文推荐以 ISO 31000 风险管理标准和 The Open Group《将风险与安全融入 TOGAF 企业架构》指南（G152）为起点。

## 上下级与包含

没有上下级。五个采用者类别是同级的分段，按采用先后从左到右排列，合起来覆盖全部采用者。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|innovators|Innovators|concept|概念：创新者|—||
|early_adopters|Early Adopters|concept|概念：早期采用者|—||
|early_majority|Early Majority|concept|概念：早期大众|—||
|late_majority|Late Majority|concept|概念：晚期大众|—||
|laggards|Laggards|concept|概念：落后者|—||
|distribution_curve|钟形分布曲线|notation|概念性采用分布，没有测量样本或坐标轴单位。|—||
|boundary_1|类别边界1|notation|类别区分线；原图不标σ值。|—||
|boundary_2|类别边界2|notation|类别区分线；原图不标σ值。|—||
|boundary_3|类别边界3|notation|类别区分线；原图不标σ值。|—||
|boundary_4|类别边界4|notation|类别区分线；原图不标σ值。|—||

### 创新者：属性

```json
{
  "share": "2.5%"
}
```

### 早期采用者：属性

```json
{
  "share": "13.5%"
}
```

### 早期大众：属性

```json
{
  "share": "34%"
}
```

### 晚期大众：属性

```json
{
  "share": "34%"
}
```

### 落后者：属性

```json
{
  "share": "16%"
}
```

## 全部关系

实线是采用者分布的钟形曲线；四条竖直虚线是类别分界，不是流程箭头。类别之间的先后只由横向位置表示，记在 flows 中。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## 采用者类别与占比（按原图转录）

```json
{
  "id": "t_categories",
  "title_zh": "采用者类别与占比（按原图转录）",
  "columns": [
    "采用者类别",
    "图中占比",
    "自左向右位置",
    "分界（背景知识）"
  ],
  "rows": [
    [
      "创新者 Innovators",
      "2.5%",
      "1",
      "平均采用时间 −2σ 之前"
    ],
    [
      "早期采用者 Early Adopters",
      "13.5%",
      "2",
      "−2σ 至 −1σ"
    ],
    [
      "早期大众 Early Majority",
      "34%",
      "3",
      "−1σ 至平均值"
    ],
    [
      "晚期大众 Late Majority",
      "34%",
      "4",
      "平均值至 +1σ"
    ],
    [
      "落后者 Laggards",
      "16%",
      "5",
      "+1σ 之后"
    ]
  ],
  "notes_zh": "前三列照录原图；第四列的标准差分界是 Rogers 模型的通常说明，原图没有写。"
}
```

## 误读检查

- 纵轴没有标注，曲线高度表示各时段采用者的相对数量（背景知识），不是采用率；不要把它与累计采用的 S 形曲线混淆。
- 百分比是 Rogers 模型的理想化分布，不是某个企业或某项技术的实测数据。
- 图本身不评价哪一类更好；正文只用它判断企业对新技术的风险偏好。
- 图题中的“Everett Roger’s”是原文拼写，人名应为 Everett Rogers。
- 中文稿第 4.2.7 节（L247–249）把英文本节压缩为一段，没有收录本图，也没有收录这组风险偏好问题。

## 原文证据

### [PDF 第 41 页](../../../documents/G184.md#page-41)

> • Using the Innovation Adoption Model shown in Figure 4-4, where does the enterprise fall in the bell curve?
### [PDF 第 42 页](../../../documents/G184.md#page-42)

> Figure 4-4: Everett Roger’s Innovation Adoption Model (aka Technology Diffusion Model)
### [PDF 第 45 页](../../../documents/G184.md#page-45)

> • Enable decision-making – it is important to set precedence during trade-off discussions and authority of tie-breaking if it must occur
> • Align the enterprise – principles take subjectivity and bias out of the equation and drive critical conversations that are objective and aligned to the enterprise’s values

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

源图记录：[原始解释与转录](../../../figures/G184/fig4-4.json)。

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
      "采用者类别的中文译名（创新者、早期采用者、早期大众、晚期大众、落后者）按常见译法拟定；中文稿未收录本图。"
    ],
    "analyzed_from": [
      "英文 PDF 第 42 页原图截图（220 dpi）",
      "英文 PDF 第 41–42 页正文（第 4.2.7 节）、第 45 页第 4 章尾注 [3]",
      "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 247–249 行（本图未被中文稿引用）"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
