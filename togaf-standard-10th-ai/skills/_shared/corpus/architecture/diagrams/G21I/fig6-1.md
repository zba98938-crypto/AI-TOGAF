# G21I/fig6-1 · 界定企业架构的范围

类型：`decomposition-or-organization-model`。第 6 章（阶段 A：架构愿景）用本图说明 MSA 在企业架构中的位置：企业架构团队通常已有战略架构，可能指出哪些分段应采用微服务/云原生方法；架构师再开发分段架构；分段架构之下是各个能力架构，MSA 层就在这里。由此界定 MSA 架构工作的范围。

英文 PDF 物理页：[32]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 32 页原图](../../../figures/assets/G21I/fig6-1-p0032.png)

[完整 JSON](fig6-1.json) · [可编辑 Mermaid](fig6-1.mmd) · [仅关系图](fig6-1.relations.mmd) · [层级分解图](fig6-1.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Breadth"]
  n1["Time"]
  n2["Level"]
  n3["Enterprise Strategic Architecture"]
  n4["Segment Architecture"]
  n5["Segment Architecture"]
  n6["Capability Architecture"]
  n7["Capability Architecture"]
  n8["Capability Architecture"]
  n9["后方无标签分段架构重复块"]
  n10["后方无标签能力架构重复块"]
```

## 架构分析

看左侧的三条坐标轴：“层级”向下表示越来越具体，“时间”向右，“广度”斜向纵深。再自上而下看三层块：顶部一整块黄色板是企业战略架构，横跨全部广度和时间；中间是多个绿色分段架构块；底部是更多、更小的紫色能力架构块。越往下，块越多、越小，每块覆盖的广度和时间越窄。

- 本图有 11 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 11 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 核对三坐标轴与六个有名架构块；补记后方无标签绿色/紫色重复块。
- 原图架构块间没有连接线。拒绝根据垂直位置推定特定分段治理特定能力块的五条旧边；正文只支持层级粒度与企业约束的总体关系。
- MSA所在能力架构层及企业约束保留在正文支持的说明表中；不虚构一一映射。

### 如何用于项目

- 按父项展开所有直接子项，检查同层粒度、重叠和缺项。
- 保留组成、分类、能力分解与组织汇报的区别；将示例名称替换为已确认的项目对象。

### 结构所表达的逻辑

- 企业战略架构只有一块，覆盖企业的全部广度和整个时间跨度；原文称它是企业的概要性正式描述，为运营与变更活动提供组织框架，给出高管层的长期方向。
- 战略架构可能指出哪些分段应采用微服务/云原生方法、要求分段之间使用交互标准，但基本不会规定具体的微服务，也不会规定支撑它们的详细基础设施。
- 分段架构在战略架构之下，数量更多，各自详细、正式地描述企业内的某个领域，在项目群或组合层面用来组织和协调变更活动。
- 能力架构在分段架构之下，数量最多、块最小；原文指出 MSA 层预期位于能力架构中。
- 原文强调 MSA 只涉及整体系统或企业架构中的一层，企业架构通常处在比 MSA 高得多的层级；各职能/项目架构必须与总体企业架构保持一致，并继承其治理与变更管理。
- 块向“时间”方向重复排列，表示不同时期各有一组分段架构和能力架构；越低层的块在时间方向上越短。

## 上下级与包含

三个架构粒度层从上至下为企业战略、分段、能力。前排分别有1/2/3个有名示意块，后方还有无名重复块。垂直排列不确定任一具体下层块隶属于哪个上层块，不建立实例治理边。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|axis_breadth|Breadth|concept|概念：广度|—||
|axis_time|Time|time|时间：时间|—||
|axis_level|Level|concept|概念：层级|—||
|esa|Enterprise Strategic Architecture|architecture|架构：企业战略架构|—||
|seg_1|Segment Architecture|architecture|其后还有未标名称的绿色块向时间、广度方向延伸，同为分段架构。|—||
|seg_2|Segment Architecture|architecture|架构：分段架构|—||
|cap_1|Capability Architecture|architecture|其后还有成排未标名称的紫色块，同为能力架构；MSA 层位于这一层。|—||
|cap_2|Capability Architecture|architecture|架构：能力架构|—||
|cap_3|Capability Architecture|architecture|架构：能力架构|—||
|unlabelled_segment_repetitions|后方无标签分段架构重复块|group|绿色块向后延伸，部分被上层遮挡；不推定未见数量或名称。|—||
|unlabelled_capability_repetitions|后方无标签能力架构重复块|group|紫色块有多排重复；三个前排标签之外没有逐块文字，不以几何对齐声明治理关系。|—||

## 全部关系

只有Breadth、Time、Level三坐标轴有箭头；架构块之间没有线。上下位置表示粒度层次，不确定某个分段块治理哪些具体能力块。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## 本轮否定的历史关系

以下旧解释保留用于追溯，不进入当前关系图、层级或知识图谱的有效边。

|旧记录|主体|旧关系|客体|否定依据|
|---|---|---|---|---|
||企业战略架构|governs|分段架构|原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。|
|1|企业战略架构|governs|分段架构|原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。|
|2|分段架构|governs|能力架构|原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。|
|3|分段架构|governs|能力架构|原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。|
|4|分段架构|governs|能力架构|原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。|

## 三个架构层级（据原图与第 6 章正文）

```json
{
  "id": "t_levels",
  "title_zh": "三个架构层级（据原图与第 6 章正文）",
  "columns": [
    "层级",
    "图中表示",
    "覆盖范围",
    "原文要点（转述）"
  ],
  "rows": [
    [
      "企业战略架构 Enterprise Strategic Architecture",
      "顶部一整块黄色板",
      "企业全部广度、整个时间跨度",
      "企业的概要性正式描述，组织框架，高管层长期方向；可指定哪些分段用微服务/云原生方法，但不规定具体微服务"
    ],
    [
      "分段架构 Segment Architecture",
      "中层多个绿色立方块",
      "企业内某一领域，时间跨度较短",
      "某一领域的详细正式描述，在项目群/组合层面组织和协调变更"
    ],
    [
      "能力架构 Capability Architecture",
      "底层更多更小的紫色立方块",
      "更窄的范围与更短的时间跨度",
      "位于分段架构之下，MSA 层预期位于其中；须与总体企业架构一致，可能受遗留接口/应用约束"
    ]
  ]
}
```

## 本轮语义修正

- 原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。
- 原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。
- 原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。
- 原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。
- 原图无此连线；正文未指定该示例块到该示例块的治理映射，不能仅凭上下摆放建立governs边。

## 误读检查

- “层级”轴向下表示更具体、范围更窄，不表示更不重要。
- 本图不是甘特图；“时间”轴表示各层架构覆盖的时间跨度，块不对应具体日期。
- MSA 不在战略层或分段层，而是在能力架构层；企业架构通常不会规定单个微服务。
- 后排未标名称的绿色、紫色块与前排同类，分别是更多的分段架构和能力架构，不是别的东西。

## 原文证据

### [PDF 第 31 页](../../../documents/G21I.md#page-31)

> At the enterprise level, we would expect that the Enterprise Architecture team would have developed a Strategic Architecture that gives a summary formal description of the enterprise, providing an organizing framework for operational and change activity, and an executive-level, long-term view for direction-setting. This might, for example, identify particular segments where microservices/cloud- native approaches should be used, and call for use of standards for interaction between segments, but it is highly unlikely to specify particular microservices or groups of microservices, or to prescribe a detailed infrastructure to support those microservices. The architect could then develop Segment Architectures, each of which gives a detailed, formal description of areas within an enterprise, used at the program or portfolio level to organize and align change activity. Below these Segment Architectures are the individual Capability Architectures, where the MSA layers would be expected to reside. This concept is depicted in Figure 6-1.
### [PDF 第 32 页](../../../documents/G21I.md#page-32)

> The scope of the MSA development depends on the size and structure of the project. The first key decision is to determine the focus of the architecture effort, by determining which business functions are to be implemented by the project.
> The TOGAF Standard does not attempt to provide a definition of “project” as it does with “enterprise”. However, it does note the increasing tendency for large-scale architectural developments to take the form of federated architectures, which are “independently developed, maintained, and managed architectures that are subsequently integrated within a meta-architectural framework”. It is almost certainly true that it is impossible to have a single enterprise-level architecture that applies to every business function within the enterprise, unless that architecture itself is a federated one. The important implication is that each of those functional or project architectures must be consistent with the overall Enterprise Architecture, with overall governance and change management as discussed later in Chapter 12 and Chapter 13, respectively.

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`279f6c06124f49a147a168591965805115b2fc976eea2664e41e491ac5d163bf`。

源图记录：[原始解释与转录](../../../figures/G21I/fig6-1.json)。

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
      "后排未标名称的分段块和能力块数量较多且相互遮挡，未逐个列为元素，只在描述中说明。",
      "能力块与分段块的对应（cap_1、cap_2 在 seg_1 下，cap_3 在 seg_2 下）按前排块的水平位置推断。"
    ],
    "analyzed_from": [
      "英文 PDF 第 32 页原图截图（220 dpi）",
      "英文 PDF 第 31–32 页正文",
      "中文稿 G21Ie_微服务架构.md 第 405–438 行（含图内标签对照表 L419–L428）",
      "figs/zh/g21ie_fig6-1_zh.png",
      "figs/g21ie_fig6-1_en.png（自动相似度 0.987）"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
