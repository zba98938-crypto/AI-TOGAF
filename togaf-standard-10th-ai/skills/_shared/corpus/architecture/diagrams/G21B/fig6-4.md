# G21B/fig6-4 · 协作式风格模式

类型：`mapping-or-assessment-matrix`。把“协作式”落到交换模式：正文说协作式使用主源与副本源之间的数据同步管理，运营系统与 C-MDM 真相保持对齐但可能有延迟；左侧小图用双向箭头强调“系统保留自己的数据、同时与 MDM 同步”。

英文 PDF 物理页：[51]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 51 页原图](../../../figures/assets/G21B/fig6-4-p0051.png)

[完整 JSON](fig6-4.json) · [可编辑 Mermaid](fig6-4.mmd) · [仅关系图](fig6-4.relations.mmd) · [层级分解图](fig6-4.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Cooperation"]
  n1["MDM"]
  n2["业务系统（紫色圆柱，左上）"]
  n3["业务系统（灰色圆柱，右上）"]
  n4["业务系统（橙色圆柱，左下）"]
  n5["业务系统（绿色圆柱，右下）"]
  n6["Customer Data Acquisition Patterns"]
  n7["Customer Data Distribution Patterns"]
  n8["C-MDM System (Point of Truth)"]
  n9["Direct Point of Truth Acquisition UI"]
  n10["Point of Truth Service (no local storage, near-real time)"]
  n11["Point of Truth Synchronization Service (local storage, near-real time)"]
  n12["Batch Acquisition (local storage, batch)"]
  n13["Direct Point of Truth Access UI (search and read)"]
  n14["Point of Truth &quot;Search and Read&quot; Service (no local storage, near-real time)"]
  n15["Point of Truth &quot;On Update Event&quot; Consumption (local storage, near-real time)"]
  n16["Batch Consumption (local storage, batch)"]
  n17["Point of Acquisition App"]
  n18["Point of Consumption App"]
  n19["Point of Acquisition App"]
  n20["Point of Acquisition App"]
  n21["本地客户数据存储图标"]
  n22["Point of Acquisition App"]
  n23["本地客户数据存储图标"]
  n24["Point of Consumption App"]
  n25["Point of Consumption App"]
  n26["本地客户数据存储图标"]
  n27["Point of Consumption App"]
  n28["本地客户数据存储图标"]
  n29["客户数据已采集标记"]
  n30["客户数据已采集标记"]
  n31["客户数据已采集标记"]
  n32["客户数据已采集标记"]
  n33["客户数据已分发标记"]
  n34["客户数据已分发标记"]
  n35["客户数据已分发标记"]
  n36["客户数据已分发标记"]
  n2 <-->|"流动"| n1
  n3 <-->|"流动"| n1
  n4 <-->|"流动"| n1
  n5 <-->|"流动"| n1
  n19 -->|"流动"| n8
  n20 <-->|"流动"| n8
  n22 -->|"流动"| n8
  n8 -->|"流动"| n24
  n8 -->|"流动"| n25
  n8 -->|"流动"| n27
  n0 -.->|"分组"| n1
  n0 -.->|"分组"| n2
  n0 -.->|"分组"| n3
  n0 -.->|"分组"| n4
  n0 -.->|"分组"| n5
  n6 -.->|"分组"| n9
  n6 -.->|"分组"| n10
  n6 -.->|"分组"| n11
  n6 -.->|"分组"| n12
  n7 -.->|"分组"| n13
  n7 -.->|"分组"| n14
  n7 -.->|"分组"| n15
  n7 -.->|"分组"| n16
  n10 -.->|"visual_containment_only"| n19
  n11 -.->|"visual_containment_only"| n20
  n20 -.->|"application_encapsulation"| n21
  n12 -.->|"visual_containment_only"| n22
  n22 -.->|"application_encapsulation"| n23
  n14 -.->|"visual_containment_only"| n24
  n15 -.->|"visual_containment_only"| n25
  n25 -.->|"application_encapsulation"| n26
  n16 -.->|"visual_containment_only"| n27
  n27 -.->|"application_encapsulation"| n28
  n8 -.->|"application_encapsulation"| n29
  n19 -.->|"application_encapsulation"| n30
  n20 -.->|"application_encapsulation"| n31
  n22 -.->|"application_encapsulation"| n32
  n8 -.->|"application_encapsulation"| n33
  n24 -.->|"application_encapsulation"| n34
  n25 -.->|"application_encapsulation"| n35
  n27 -.->|"application_encapsulation"| n36
```

## 架构分析

先看左侧Cooperation示意：MDM与四个系统均双向连接。右侧八模式矩阵按原图红框读取：采集a1/a3/a4，分发d1/d2/d4。正文强调主源与副本源同步及可能存在的延迟；正文未逐一列举某模式，并不构成图文矛盾。

- 本图有 37 个具名或隐含元素、10 条关系和 31 条包含/分组记录。
- 包含/分组树最大深度为 3；根节点为 协作式小图、客户数据采集模式、客户数据分发模式、C-MDM 系统（真相点）、采集点应用、消费点应用。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 4 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 逐一核对左侧风格图、八种模式全部文字、六个独立应用、四个存储圆柱、八个数据标记、全部连线及红框范围。
- 将按列重复的同名应用拆为独立实例；修正同步服务的双向箭头。
- 选用模式与完整背景矩阵分开记录；相邻正文的未提及不解释为源图错误。

### 如何用于项目

- 先固定行、列所代表的维度及单元格含义，再登记有证据的映射或评分。
- 空白、无关系、未测量和不适用分别处理；颜色不自动等于优先级。

### 结构所表达的逻辑

- 左侧四条双向线表达协作式的数据交换。
- 图中红框选择a1、a3、a4、d1、d2、d4；d3虽绘于完整矩阵，但未被红框选择。
- 采集a3同步服务的连线双向，其他五条有应用的矩阵连线单向。
- 正文强调主源与副本源的数据同步，允许交换频率或架构导致延迟；未提及某个红框模式不能据此宣布原图错误。

## 上下级与包含

两层：矩阵的采集/分发两大类 + 8 个模式；左侧小图是风格级示意，不参与矩阵层级。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|协作式小图|MDM|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|协作式小图|业务系统（紫色圆柱，左上）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|协作式小图|业务系统（灰色圆柱，右上）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|协作式小图|业务系统（橙色圆柱，左下）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|协作式小图|业务系统（绿色圆柱，右下）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据采集模式|直接真相点采集界面|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据采集模式|真相点服务（无本地存储，近实时）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据采集模式|真相点同步服务（本地存储，近实时）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据采集模式|批量获取（本地存储，批处理）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据分发模式|直接真相点访问界面（搜索与读取）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据分发模式|真相点“搜索与读取”服务（无本地存储，近实时）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据分发模式|真相点“更新事件”消费（本地存储，近实时）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|客户数据分发模式|批量消费（本地存储，批处理）|visual_grouping|框、泳道、域或分类组的成员归属；没有额外证据不提升为业务组合或管理关系。|
|真相点服务（无本地存储，近实时）|采集点应用|visual_containment_only|保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。|
|真相点同步服务（本地存储，近实时）|采集点应用|visual_containment_only|保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。|
|采集点应用|本地客户数据存储图标|application_encapsulation|应用组件包含其数据、行为或子组件。|
|批量获取（本地存储，批处理）|采集点应用|visual_containment_only|保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。|
|采集点应用|本地客户数据存储图标|application_encapsulation|应用组件包含其数据、行为或子组件。|
|真相点“搜索与读取”服务（无本地存储，近实时）|消费点应用|visual_containment_only|保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。|
|真相点“更新事件”消费（本地存储，近实时）|消费点应用|visual_containment_only|保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。|
|消费点应用|本地客户数据存储图标|application_encapsulation|应用组件包含其数据、行为或子组件。|
|批量消费（本地存储，批处理）|消费点应用|visual_containment_only|保存原图解释中的包含；业务关系类型需要图例或正文进一步限定。|
|消费点应用|本地客户数据存储图标|application_encapsulation|应用组件包含其数据、行为或子组件。|
|C-MDM 系统（真相点）|客户数据已采集标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|采集点应用|客户数据已采集标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|采集点应用|客户数据已采集标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|采集点应用|客户数据已采集标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|C-MDM 系统（真相点）|客户数据已分发标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|消费点应用|客户数据已分发标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|消费点应用|客户数据已分发标记|application_encapsulation|应用组件包含其数据、行为或子组件。|
|消费点应用|客户数据已分发标记|application_encapsulation|应用组件包含其数据、行为或子组件。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|style_mini|Cooperation|group|分组：协作式小图|—||
|mini_mdm|MDM|application|应用：MDM|协作式小图|1|
|mini_sys_purple|业务系统（紫色圆柱，左上）|application|应用：业务系统（紫色圆柱，左上）|协作式小图|1|
|mini_sys_grey|业务系统（灰色圆柱，右上）|application|应用：业务系统（灰色圆柱，右上）|协作式小图|1|
|mini_sys_orange|业务系统（橙色圆柱，左下）|application|应用：业务系统（橙色圆柱，左下）|协作式小图|1|
|mini_sys_green|业务系统（绿色圆柱，右下）|application|应用：业务系统（绿色圆柱，右下）|协作式小图|1|
|g_acq_patterns|Customer Data Acquisition Patterns|group|分组：客户数据采集模式|—||
|g_dist_patterns|Customer Data Distribution Patterns|group|分组：客户数据分发模式|—||
|c_mdm|C-MDM System (Point of Truth)|application|应用：C-MDM 系统（真相点）|—||
|a1|Direct Point of Truth Acquisition UI|service|本图被红框圈住。|客户数据采集模式|1|
|a2|Point of Truth Service (no local storage, near-real time)|service|服务：真相点服务（无本地存储，近实时）|客户数据采集模式|1|
|a3|Point of Truth Synchronization Service (local storage, near-real time)|service|本图被红框圈住；正文指定协作式使用的核心模式。|客户数据采集模式|1|
|a4|Batch Acquisition (local storage, batch)|service|本图第 4 列整列被红框圈住（与正文不一致）。|客户数据采集模式|1|
|d1|Direct Point of Truth Access UI (search and read)|service|本图与 d2 一起被红框圈住。|客户数据分发模式|1|
|d2|Point of Truth "Search and Read" Service (no local storage, near-real time)|service|本图被红框圈住。|客户数据分发模式|1|
|d3|Point of Truth "On Update Event" Consumption (local storage, near-real time)|service|正文所述协作式的分发核心模式，但本图未被红框圈住。|客户数据分发模式|1|
|d4|Batch Consumption (local storage, batch)|service|本图第 4 列整列被红框圈住。|客户数据分发模式|1|
|poa_app|Point of Acquisition App|concept|采集应用图形类别，具体实例分别见a2_app/a3_app/a4_app。|—||
|poc_app|Point of Consumption App|concept|消费应用图形类别，具体实例分别见d2_app/d3_app/d4_app。|—||
|a2_app|Point of Acquisition App|application|该交换模式中的独立应用图形；不能与其他模式的同名应用合并。|真相点服务（无本地存储，近实时）|2|
|a3_app|Point of Acquisition App|application|该交换模式中的独立应用图形；不能与其他模式的同名应用合并。|真相点同步服务（本地存储，近实时）|2|
|a3_local_storage|本地客户数据存储图标|data|本模式应用内部蓝色圆柱；图例定义Customer Data Storage，不代表独立命名数据库。|采集点应用|3|
|a4_app|Point of Acquisition App|application|该交换模式中的独立应用图形；不能与其他模式的同名应用合并。|批量获取（本地存储，批处理）|2|
|a4_local_storage|本地客户数据存储图标|data|本模式应用内部蓝色圆柱；图例定义Customer Data Storage，不代表独立命名数据库。|采集点应用|3|
|d2_app|Point of Consumption App|application|该交换模式中的独立应用图形；不能与其他模式的同名应用合并。|真相点“搜索与读取”服务（无本地存储，近实时）|2|
|d3_app|Point of Consumption App|application|该交换模式中的独立应用图形；不能与其他模式的同名应用合并。|真相点“更新事件”消费（本地存储，近实时）|2|
|d3_local_storage|本地客户数据存储图标|data|本模式应用内部蓝色圆柱；图例定义Customer Data Storage，不代表独立命名数据库。|消费点应用|3|
|d4_app|Point of Consumption App|application|该交换模式中的独立应用图形；不能与其他模式的同名应用合并。|批量消费（本地存储，批处理）|2|
|d4_local_storage|本地客户数据存储图标|data|本模式应用内部蓝色圆柱；图例定义Customer Data Storage，不代表独立命名数据库。|消费点应用|3|
|a1_data_marker|客户数据已采集标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|C-MDM 系统（真相点）|1|
|a2_data_marker|客户数据已采集标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|采集点应用|3|
|a3_data_marker|客户数据已采集标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|采集点应用|3|
|a4_data_marker|客户数据已采集标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|采集点应用|3|
|d1_data_marker|客户数据已分发标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|C-MDM 系统（真相点）|1|
|d2_data_marker|客户数据已分发标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|消费点应用|3|
|d3_data_marker|客户数据已分发标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|消费点应用|3|
|d4_data_marker|客户数据已分发标记|data|源图图例Customer Data Acquired/Distributed的实例；不是独立命名业务实体。|消费点应用|3|

## 全部关系

矩阵采集第2、4列为应用→C-MDM，第3列同步服务为应用↔C-MDM；分发第2–4列为C-MDM→应用；Direct UI列没有单独应用或连线。红框仅表示选中的模式，虚线格界和图标不表示流向。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|
|业务系统（紫色圆柱，左上）|流动|MDM|显式连线||左侧小图：双向同步。|
|业务系统（灰色圆柱，右上）|流动|MDM|显式连线||左侧小图：双向同步。|
|业务系统（橙色圆柱，左下）|流动|MDM|显式连线||左侧小图：双向同步。|
|业务系统（绿色圆柱，右下）|流动|MDM|显式连线||左侧小图：双向同步。|
|采集点应用|流动|C-MDM 系统（真相点）|显式连线||按模式列分开三个同名应用实例，保留实际连线端点。|
|采集点应用|流动|C-MDM 系统（真相点）|显式连线||按模式列分开三个同名应用实例，保留实际连线端点。 Synchronization Service连线双端有箭头。|
|采集点应用|流动|C-MDM 系统（真相点）|显式连线||按模式列分开三个同名应用实例，保留实际连线端点。|
|C-MDM 系统（真相点）|流动|消费点应用|显式连线||按模式列分开三个同名应用实例，保留实际连线端点。|
|C-MDM 系统（真相点）|流动|消费点应用|显式连线||按模式列分开三个同名应用实例，保留实际连线端点。|
|C-MDM 系统（真相点）|流动|消费点应用|显式连线||按模式列分开三个同名应用实例，保留实际连线端点。|

## 本图红框的实际覆盖范围（按像素坐标转录）

```json
{
  "id": "t_red_frames",
  "title_zh": "本图红框的实际覆盖范围（按像素坐标转录）",
  "columns": [
    "红框",
    "覆盖列",
    "覆盖的模式",
    "正文说明与观察边界"
  ],
  "rows": [
    [
      "上排红框 1",
      "第 1 列",
      "Direct Point of Truth Acquisition UI",
      "红框范围直接可见；正文强调同步，没有逐项排除其他模式。"
    ],
    [
      "上排红框 2",
      "第 3 列",
      "Point of Truth Synchronization Service",
      "红框范围直接可见；正文强调同步，没有逐项排除其他模式。"
    ],
    [
      "整列红框",
      "第 4 列（上下两格）",
      "Batch Acquisition + Batch Consumption",
      "红框范围直接可见；正文强调同步，没有逐项排除其他模式。"
    ],
    [
      "下排红框",
      "第 1–2 列",
      "Direct Point of Truth Access UI + Point of Truth “Search and Read” Service",
      "红框范围直接可见；正文强调同步，没有逐项排除其他模式。"
    ]
  ],
  "cell_legend": [
    "红框为原图像素级标注，非本分析推断"
  ],
  "notes_zh": "红框坐标：上排第 1 列 x371–632/y15–329；第 3 列 x912–1200/y15–329；第 4 列 x1197–1507/y15–731；下排第 1–2 列 x371–911/y404–731。"
}
```

## 本轮语义修正

- 按模式列分开三个同名应用实例，保留实际连线端点。
- 按模式列分开三个同名应用实例，保留实际连线端点。 Synchronization Service连线双端有箭头。
- 按模式列分开三个同名应用实例，保留实际连线端点。
- 按模式列分开三个同名应用实例，保留实际连线端点。
- 按模式列分开三个同名应用实例，保留实际连线端点。
- 按模式列分开三个同名应用实例，保留实际连线端点。

## 误读检查

- 完整矩阵包含的模式不等于此图红框选用的模式。
- 不可把正文着重描述同步，推断为批量列红框错误。
- 双向数据流不保证两方向完全实时；正文允许延迟。
- 红框表示选用范围，不表示风险或流向。

## 原文证据

### [PDF 第 51 页](../../../documents/G21B.md#page-51)

> Patterns to use for the cooperation style are data “synchronization” management between primary source and replica sources (see Figure 6-4). The operational system should be aligned to the C-MDM truth, but potentially with some latency regarding exchange frequencies/architecture.
### [PDF 第 52 页](../../../documents/G21B.md#page-52)

> • All updates and creation initiated through the C-MDM point of truth system and services
> • The same functional coverage as the cooperation style, but less complex and more efficient from the architecture and information system operations point of view

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

源图记录：[原始解释与转录](../../../figures/G21B/fig6-4.json)。

```json
{
  "quality": {
    "graph_integrity": "checked",
    "semantic_analysis": "typed-graph-and-context-analysis",
    "visual_review": "source-content-audited",
    "notice_zh": "所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。"
  },
  "source_uncertainty": {
    "confidence": "medium",
    "uncertainties_zh": [
      "红框覆盖范围与正文“协作式使用同步管理”不一致（还框住了批量列与搜索读取列，且未框住 On Update Event Consumption），疑为原图标注偏移或错误；本分析按像素如实记录并在表中标出。",
      "左侧小图的系统圆柱无标签；双向箭头是否代表“同步”依据正文与图 6-1。"
    ],
    "analyzed_from": [
      "英文 PDF 第 51 页原图截图及 2×2 放大分块",
      "英文 PDF 第 51 页正文",
      "中文稿第 755、776 行（协作式说明）；图 6-4 本身未被中文稿引用",
      "红框像素检测（PIL）结果"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
