# G18A/fig2-4 · 业务模型画布

类型：`business-model-canvas`。引出本书采用的业务模型表示——Osterwalder 与 Pigneur 的业务模型画布，说明它用一页纸覆盖价值创造、交付与获取的全部关键要素，为第 4 章战略对齐、第 7 章零售案例和附录 A 的逐块定义奠定基础。

英文 PDF 物理页：[15]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 15 页原图](../../../figures/assets/G18A/fig2-4-p0015.png)

[完整 JSON](fig2-4.json) · [可编辑 Mermaid](fig2-4.mmd) · [仅关系图](fig2-4.relations.mmd) · [层级分解图](fig2-4.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Key Partners"]
  n1["Key Activities"]
  n2["Value Proposition"]
  n3["Customer Relationships"]
  n4["Customers"]
  n5["Key Resources"]
  n6["Channels"]
  n7["Costs"]
  n8["Revenue"]
  n9["drawings by JAM"]
  n2 -.->|"支撑/服务"| n4
  n6 -.->|"支撑/服务"| n4
```

## 架构分析

这是一张 3D 俯视插画，没有箭头。先按标签定位九个区域：左上 Key Partners，顶部 Key Activities，中央 Value Proposition，其下 Channels，右上 Customer Relationships，最右 Customers，左下 Key Resources，底部左 Costs、右 Revenue。每个粗体标签都用一条细引线指向区域。可按第 7 章建议从右侧 Customers 向左读（先看客户与价值，再看成本侧），也可从中央价值主张向外读。

- 本图有 10 个具名或隐含元素、2 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 8 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 9个业务模型构成块及drawings by JAM署名逐项核对；图形、爱心和环形线是说明性绘画。
- 细灰引线连接标题与插图，不是架构依赖。原图没有组件间有向关系；两条概念服务关系单独标为正文支持。

### 如何用于项目

- 先明确受益方和价值主张，再把各画布要素关联到能力、价值流及所需资源。
- 画布用于假设和共同理解；不能替代细化的实现架构或已验证经营数据。

### 结构所表达的逻辑

- 九个构建块：Key Partners、Key Activities、Key Resources、Value Proposition、Customer Relationships、Channels、Customers、Costs、Revenue。
- 版式左半偏成本/资源与伙伴，右半偏客户与关系，中央是价值主张；底部左 Costs、右 Revenue 作为财务结果横贯。
- 原图用 Customers 而非 Customer Segments，用 Revenue、Costs 而非 Revenue Streams、Cost Structure——名称比通行画布更简短。
- 每个区域配一幅线描小图（如礼盒=价值主张、心形=客户关系、卡车=渠道、收银机=收入），仅作视觉提示，不构成额外信息。
- 右下角 drawings by JAM 是插画作者署名，不是模型要素。
- 图形是插画而非标准九宫格：区域边界不规则，不能按矩形框去寻找模块边界。

## 上下级与包含

只有一层：整张画布被隔断为九个并列区域，没有嵌套、没有编号、没有上下级。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|key_partners|Key Partners|group|区域内画有一对相扣的圆环。|—||
|key_activities|Key Activities|group|区域内画有一人操作挖掘机。|—||
|value_proposition|Value Proposition|group|区域内画有一个系缎带的礼盒。|—||
|customer_relationships|Customer Relationships|group|区域内画有一颗心。|—||
|customers|Customers|group|区域内画有一个站立的人。|—||
|key_resources|Key Resources|group|区域内画有一人守着木箱。|—||
|channels|Channels|group|区域内画有一辆厢式货车。|—||
|costs|Costs|group|区域内画有一张带线条的票据。|—||
|revenue|Revenue|group|区域内画有一台收银机。|—||
|credit_jam|drawings by JAM|note|插画作者署名，不属于画布构建块。|—||

## 全部关系

图中没有表示关系的连线，只有九条从标签指向区域的细引线（标注线，无箭头）。区域之间的相邻关系由隔断位置表达，不表示流程或依赖方向。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|
|价值主张|支撑/服务|客户|implicit||Appendix A原文定义价值主张面向客户、渠道用于触达客户；这是正文支持的概念关系，图上没有连接箭头。|
|渠道|支撑/服务|客户|implicit||Appendix A原文定义价值主张面向客户、渠道用于触达客户；这是正文支持的概念关系，图上没有连接箭头。|

## 本轮否定的历史关系

以下旧解释保留用于追溯，不进入当前关系图、层级或知识图谱的有效边。

|旧记录|主体|旧关系|客体|否定依据|
|---|---|---|---|---|
|2|关键合作伙伴|dependency|关键活动|九宫格的邻接排列不能证明特定Key Partners→Key Activities依赖。正文只称伙伴使商业模式运作，未给这两个块之间的定向依赖。|

## 本轮语义修正

- Appendix A原文定义价值主张面向客户、渠道用于触达客户；这是正文支持的概念关系，图上没有连接箭头。
- Appendix A原文定义价值主张面向客户、渠道用于触达客户；这是正文支持的概念关系，图上没有连接箭头。
- 九宫格的邻接排列不能证明特定Key Partners→Key Activities依赖。正文只称伙伴使商业模式运作，未给这两个块之间的定向依赖。

## 误读检查

- 不要把标签引线当成关系箭头：它们只说明“这个名字指这块区域”。
- 不要把 drawings by JAM 当成第十个构建块或方法名，它只是插画署名。
- 不要以为原图就是标准九宫格：它是手绘透视图，区域形状不规则。
- 不要把图 2-4 与图 A-1 当成同一张图：图 A-1 是平面九宫格，标签为 Key Partnerships、Customer Segments、Cost Structures、Revenue Streams；本图标签为 Key Partners、Customers、Costs、Revenue。
- 中文稿第 103 行引用的 SVG 是平面九宫格并带自拟解释，不能据它判断原图版式。

## 原文证据

### [PDF 第 14 页](../../../documents/G18A.md#page-14)

> The theoretical arguments supporting different representations of business models have been in play for many years, yet it was Alexander Osterwalder and Yves Pigneur’s simple-to-use methods and tools described in their book Business Model Generation that popularized the Business Model Canvas (Figure 2-4) and established it as the baseline for business model innovation. We use this form to show business model alignment between strategy and Business Architecture, followed by a deeper look in Appendix A. Note this type of business model has been introduced in earlier work of The Open Group
### [PDF 第 15 页](../../../documents/G18A.md#page-15)

> Figure 2-4: The Business Model Canvas (Source: Business Model Generation, Alexander Osterwalder, Yves
### [PDF 第 28 页](../../../documents/G18A.md#page-28)

> The framers of the Business Model Canvas purposefully created it to be an elegant, one-page representation of a business model that:
> • Provides a shared perspective and understanding of an organization’s business model(s)
### [PDF 第 29 页](../../../documents/G18A.md#page-29)

> The Business Model Canvas is a particularly useful tool for understanding how a business handles its key determinants of revenue and cost, the value proposition it uses to go to market, the customers it serves, and the resources it needs to execute. These elements play a crucial step in laying the framework for:
> • The remaining work to address the specific application, information, and technology solutions

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

源图记录：[原始解释与转录](../../../figures/G18A/fig2-4.json)。

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
      "手绘区域边界不规则，个别区域（如 Channels 与 Customer Relationships）的归属按标签引线落点判定。",
      "原图用 Customers；它是否等同于标准画布的 Customer Segments，图中未说明。",
      "插画细节（如钥匙、礼盒、收银机）是否为特定隐喻，原图未加注释。"
    ],
    "analyzed_from": [
      "英文 PDF 第 15 页原图截图（fig2-4_p15_1.png）及 2×2 放大分块 z11/z22",
      "英文 PDF 第 14–15 页正文",
      "中文稿 G18Ae_业务模型.md 第 101–103 行",
      "figs/g18a_fig2-4.svg 源码与 SVG 文本"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
