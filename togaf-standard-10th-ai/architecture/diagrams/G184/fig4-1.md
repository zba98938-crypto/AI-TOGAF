# G184/fig4-1 · 运营模式

类型：`analytical-view`。第 4.2.1 节要求在理解企业语境时识别业务模型与运营模式。作者选用行业中立的 CISR 模型（改编自 Ross 等《Enterprise Architecture as Strategy》）作为记录运营模式的模板之一，帮助领导者判断企业以哪种模式处理业务流程，从而理解企业如何为增长与可持续性组织运营。

英文 PDF 物理页：[35]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 35 页原图](../../../figures/assets/G184/fig4-1-p0035.png)

[完整 JSON](fig4-1.json) · [可编辑 Mermaid](fig4-1.mmd) · [仅关系图](fig4-1.relations.mmd) · [层级分解图](fig4-1.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Business Process Integration"]
  n1["Business Process Standardization"]
  n2["Coordination"]
  n3["Unification"]
  n4["Diversification"]
  n5["Replication"]
```

## 架构分析

先看两个轴：纵轴“业务流程集成”下低上高，横轴“业务流程标准化”左低右高。四个象限由两轴高低组合定位：左上协调（高集成、低标准化）、右上统一（高集成、高标准化）、左下多元化（低集成、低标准化）、右下复制（低集成、高标准化）。每个方块先给模式名称，再给一句定义和一个示例。图中没有连线。

- 本图有 6 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 6 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 两轴、Low/High标度、四象限名称和全部说明段落逐句核对；表格中的英文定义与例子完整。
- 上为高集成、右为高标准化；协调=高/低，统一=高/高，多元化=低/低，复制=低/高。
- 正文允许同企业不同部分采用不同模式；不从象限位置构造成熟度高低或优劣排序。

### 如何用于项目

- 围绕作者目的读取本图实体、分组与连线，并用对应原文限定其含义。
- 把参考模型与项目事实分开，实际范围、约束、值和责任须有项目证据。

### 结构所表达的逻辑

- 两个维度：业务流程集成（按象限说明归纳，指各业务单元需要了解彼此交易、共享数据的程度）与业务流程标准化（各单元以同一方式执行流程的程度）；两两组合得到四种运营模式。
- 协调（高集成、低标准化）：各具特色的业务单元需要了解彼此的交易，典型是向同一批客户提供不同产品，如信用卡与住房/汽车贷款，或寿险、财产险与车险。
- 统一（高集成、高标准化）：单一业务，采用全球统一的流程标准和数据访问，如在全球范围、跨客户管理活动或外包服务。
- 多元化（低集成、低标准化）：业务单元相互独立，客户与专业能力不同，如陆上住宿与邮轮住宿几乎没有共同客户和专业知识，但各单元之间仍可互相借鉴以保持效率。
- 复制（低集成、高标准化）：业务单元相互独立但做法相似，如分布在各地的工厂以同样方式运作，保证质量与产地无关。
- 同一家企业可以同时具有多种运营模式。正文举例：在美国、巴西、德国经营的全球银行保险公司，各国单元按复制模式独立经营，全球控股公司则承担协调职能，以向投资者保证业务模型可行。
- 正文区分运营模式与业务模型：运营模式描述企业如何执行其主要职能以实现目的，业务模型是这样做的理由，核心是现金流与盈利能力；运营模式把详细的组织设计与企业的战略、价值观、目的连接起来。
- 正文建议通过利益相关者分析来捕获和验证运营模式，并同时记录产品/服务价值、目标市场、价值链、收入模式、战略优势以及业务的核心性质（制造、营销、销售与分销、专业服务等）。

## 上下级与包含

没有上下级。四个象限是同级的运营模式类型，位置由两个轴的高低组合决定。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|axis_integration|Business Process Integration|metric|度量：业务流程集成|—||
|axis_standardization|Business Process Standardization|metric|度量：业务流程标准化|—||
|q_coordination|Coordination|concept|各具特色的业务单元需要了解彼此的交易；例：向同一批客户提供信用卡与住房/汽车贷款，或寿险、财产险与车险。|—||
|q_unification|Unification|concept|单一业务，全球统一的流程标准与数据访问；例：在全球、跨客户管理活动或外包服务。|—||
|q_diversification|Diversification|concept|相互独立的业务单元，客户与专业能力不同；例：陆上住宿与邮轮住宿共同点很少，但可互相借鉴以保持效率。|—||
|q_replication|Replication|concept|相互独立但相似的业务单元；例：各地工厂以同样方式运作，保证质量与产地无关。|—||

### 业务流程集成：属性

```json
{
  "scale": [
    "Low",
    "High"
  ],
  "direction": "自下而上"
}
```

### 业务流程标准化：属性

```json
{
  "scale": [
    "Low",
    "High"
  ],
  "direction": "自左向右"
}
```

### 协调：属性

```json
{
  "integration": "High",
  "standardization": "Low"
}
```

### 统一：属性

```json
{
  "integration": "High",
  "standardization": "High"
}
```

### 多元化：属性

```json
{
  "integration": "Low",
  "standardization": "Low"
}
```

### 复制：属性

```json
{
  "integration": "Low",
  "standardization": "High"
}
```

## 全部关系

图中没有连线或箭头。两个轴只给出 Low/High 两档，象限的位置就是模式的定义。关系清单为空；每个象限对应的两轴取值写在元素属性和表格中。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## 四个象限（按原图逐块转录）

```json
{
  "id": "t_quadrants",
  "title_zh": "四个象限（按原图逐块转录）",
  "columns": [
    "象限（运营模式）",
    "业务流程集成",
    "业务流程标准化",
    "原图说明（英文原文）",
    "说明（中文转述）"
  ],
  "rows": [
    [
      "协调 Coordination",
      "高 High",
      "低 Low",
      "Unique business units have a need to know each other’s transactions. For example, different products are provided to the same customers like credit cards and home/auto loans or life, home, and automobile insurance.",
      "各具特色的业务单元需要了解彼此的交易。例如向同一批客户提供不同产品：信用卡与住房/汽车贷款，或寿险、财产险与车险。"
    ],
    [
      "统一 Unification",
      "高 High",
      "高 High",
      "Single business with global process standards and data access. For example, managing events or outsourced services globally and across clients.",
      "单一业务，采用全球统一的流程标准和数据访问。例如在全球范围、跨客户管理活动或外包服务。"
    ],
    [
      "多元化 Diversification",
      "低 Low",
      "低 Low",
      "Independent business units with different customers and expertise. For example, lodging services provided on land and cruises have very little commonality in customer base and internal employee subject matter expertise, but lessons can be learned to stay efficient across all business units.",
      "相互独立的业务单元，客户与专业能力各不相同。例如陆上住宿与邮轮住宿在客户群和员工专业知识上几乎没有共同点，但各业务单元之间仍可互相借鉴以保持效率。"
    ],
    [
      "复制 Replication",
      "低 Low",
      "高 High",
      "Independent but similar business units. For example, geographically distributed set of factories operate the same way to assure quality to customers, irrespective of where the product was made.",
      "相互独立但彼此相似的业务单元。例如分布在各地的工厂以同样方式运作，无论产品在哪里生产，都向客户保证同样的质量。"
    ]
  ],
  "notes_zh": "原图每个象限是一个蓝色方块：粗体模式名称 + 一句定义 + 一个示例。"
}
```

## 误读检查

- 两个轴衡量的是业务流程的集成程度和标准化程度，不是 IT 系统集成或技术标准化程度。
- 轴只分高、低两档，四个象限是类型划分；图中没有从一种模式演进到另一种模式的路径，也没有说哪种模式更好。
- 运营模式不等于业务模型：正文把业务模型定义为企业如此运作的理由（现金流与盈利），运营模式只描述如何运作。
- 一家企业不必只落在一个象限：正文的银行保险例子同时出现复制与协调。
- 中文稿第 4.2.1 节（L223–225）把英文本节压缩成一段概述，没有收录本图，也没有提到 CISR 模型和四种运营模式。

## 原文证据

### [PDF 第 34 页](../../../documents/G184.md#page-34)

> There are several templates and references available for documenting the operating model – differentiated by industry or geography or by public, private, or social incorporation. It should be noted that some of the industry verticals (e.g., retail, wholesale, online, digital) have their own versions of operating model classification. The Center for Information Systems Research (CISR) model shown in Figure 4-1 is industry-neutral and focuses on patterns for how business processes are handled by the enterprise for growth and sustainability.
### [PDF 第 35 页](../../../documents/G184.md#page-35)

> and financial structuring of these three units may replicate best practices of one another across each unit. The global holding company may be performing a coordination function to assure viability of the organization’s business model to its investors.
> While capturing the operating model, it is essential to explore and document the value of products or services or both delivered by the enterprise, its target market, value chain, revenue generation model, and the strategic advantage of the enterprise. Another dimension to consider while creating the operating model is the core nature of the business such as a manufacturing, marketing, sales and distribution services, professional services, community business, or public utility core nature. Value chain and revenue generation models will be covered in detail later in this document.
### [PDF 第 45 页](../../../documents/G184.md#page-45)

> • Enable decision-making – it is important to set precedence during trade-off discussions and authority of tie-breaking if it must occur
> • Align the enterprise – principles take subjectivity and bias out of the equation and drive critical conversations that are objective and aligned to the enterprise’s values

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

源图记录：[原始解释与转录](../../../figures/G184/fig4-1.json)。

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
      "四种运营模式的中文译名（协调、统一、多元化、复制）由解析者拟定；中文稿未收录本图，没有对照译名。",
      "原图没有定义两个轴的含义；key_points 中对“集成”“标准化”的解释依据四个象限的说明归纳。"
    ],
    "analyzed_from": [
      "英文 PDF 第 35 页原图截图（220 dpi）与整页预览",
      "英文 PDF 第 33–35 页正文（第 4.2.1 节）、第 45 页第 4 章尾注 [1]、第 92 页",
      "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 221–225、1026 行（本图未被中文稿引用）"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
