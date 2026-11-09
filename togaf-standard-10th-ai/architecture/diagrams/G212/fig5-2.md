# G212/fig5-2 · ABCD 数字技术采用框架

类型：`analytical-view`。第 5.1 节要求组织先选采用方法；作者用 ABCD 框架把“多广（普及度）× 多快（速度）”做成四象限，声称可适配各类组织，并强调选择必须有清晰论证——说明为什么选这种而非其他。

英文 PDF 物理页：[40]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 40 页原图](../../../figures/assets/G212/fig5-2-p0040.png)

[完整 JSON](fig5-2.json) · [可编辑 Mermaid](fig5-2.mmd) · [仅关系图](fig5-2.relations.mmd) · [层级分解图](fig5-2.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Ubiquity (How Extensive is the Adoption)"]
  n1["Velocity (How Rapid is the Adoption)"]
  n2["Avant-Garde"]
  n3["Big-Bang"]
  n4["Cohesive"]
  n5["Discreet"]
  n6["四象限交界的四向箭头"]
```

## 架构分析

先看两根橙色轴：横轴向右表示普及度越来越高（数字实施越广），纵轴向上表示采用速度越来越快（时间是速度的函数）。四个象限按“低/高普及 × 高/低速度”定位：左上 Avant-Garde、右上 Big-Bang、左下 Discreet、右下 Cohesive。每个象限内先读方法名，再读下方说明；说明描述的是选择该方法的企业特征，不是步骤。

- 本图有 7 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 7 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 核对两坐标轴、四象限标题和四段完整说明，分类速度/广度表准确。
- 中心四向小箭头位于四象限交界，坐标原点实际在左下；四种方法不是优劣排名。

### 如何用于项目

- 围绕作者目的读取本图实体、分组与连线，并用对应原文限定其含义。
- 把参考模型与项目事实分开，实际范围、约束、值和责任须有项目证据。

### 结构所表达的逻辑

- 横轴是普及度（ubiquity），指数字实施的广度/广泛性；纵轴是采用速度（velocity），是时间的函数（正文 p39）。
- Avant-Garde（低普及、高速度）：允许部分业务线、职能或地域先采用，再把经验传递给其他部分。
- Big-Bang（高普及、高速度）：有意愿且有能力在全企业一次性铺开，偏好“一次到位”并兼顾速度。
- Cohesive（高普及、低速度）：通过共识与整合让每个部分作为共同使命参与，即使拖慢采用速度。
- Discreet（低普及、低速度）：谨慎起步、稳扎稳打，逐步积累能力与经验。
- 四个象限只是四种方法类型，不代表排名或评价：B 不比 A 好，C 也不比 B 好（原文注）。
- 方法选择需要论证“为什么”；图中不提供打分、门槛或选择算法。

## 上下级与包含

只有一层：四个并列的方法类别，由两根坐标轴切成四个象限；象限之间没有上下级或包含关系，也不构成从 A 到 D 的演进。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|axis_ubiquity|Ubiquity (How Extensive is the Adoption)|other|数字技术采用的广度/广泛性；向右递增。|—||
|axis_velocity|Velocity (How Rapid is the Adoption)|other|预期的采用速度，是时间的函数；向上递增。|—||
|q_avant|Avant-Garde|group|允许部分业务线、职能或地域先采用并快速推进，从实践中学习，随后把经验传递给其他部分。|—||
|q_bigbang|Big-Bang|group|有意愿且有能力在全企业一次性铺开数字技术，偏好全面且快速的采用方式。|—||
|q_cohesive|Cohesive|group|通过共识与整合让组织的每个部分作为共同使命参与，即使影响采用速度。|—||
|q_discreet|Discreet|group|谨慎推进数字技术采用，起步缓慢而稳健，逐步积累能力与经验。|—||
|cross|四象限交界的四向箭头|other|四向视觉标记；不位于橙色坐标轴原点，也不指定象限间迁移顺序。|—||

## 全部关系

外侧横向和纵向橙色箭头标示普及度与速度；四向小箭头位于四象限中心而非坐标轴原点。各方法之间没有连接线。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## ABCD 四象限（按原图位置与文字逐项转录）

```json
{
  "id": "t_quadrants",
  "title_zh": "ABCD 四象限（按原图位置与文字逐项转录）",
  "columns": [
    "象限位置",
    "方法",
    "速度",
    "普及度",
    "图内说明（英文原样）"
  ],
  "rows": [
    [
      "左上",
      "Avant-Garde 先锋式",
      "高",
      "低",
      "Enterprises that allow/enable some parts (like an LOB, function, or geography) to adopt first and fast, learning from and passing on this experience to others subsequently"
    ],
    [
      "右上",
      "Big-Bang 大爆炸式",
      "高",
      "高",
      "Enterprises that have the willingness and ability to roll-out enterprise-wide adoption of digital technology, favoring a comprehensive approach coupled with speed"
    ],
    [
      "右下",
      "Cohesive 凝聚式",
      "低",
      "高",
      "Enterprises that take along every part and everyone through a process of consensus and integration as a common mission, despite its impact on the speed of adoption"
    ],
    [
      "左下",
      "Discreet 谨慎式",
      "低",
      "低",
      "Enterprises that take a cautious approach towards the adoption of digital technology by starting slow and steady, gradually building competence and gaining experience"
    ]
  ],
  "notes_zh": "按象限位置（左上、右上、右下、左下）排列；速度与普及度两列据坐标轴判定。中文名取自中文稿 5.1 节；坐标轴原文：Ubiquity (How Extensive is the Adoption)、Velocity (How Rapid is the Adoption)。"
}
```

## 误读检查

- A/B/C/D 不是等级：原文明确四个象限只是方法类型，B 不比 A 好、C 不比 B 好；字母顺序也不是成熟度顺序。
- 不要把四个象限读成“先 A 再 B 再 C 再 D”的路线；它们是根据两个维度区分的四种情形。
- “高速度”在上方、“高普及”在右方，是由轴箭头决定的；不要因为 Cohesive 在右下就误以为它速度高。
- 四向小箭头位于四象限交界中心，既不是外侧两坐标轴的原点，也不代表四种方法互相影响。
- 中文稿引用的 figs/g212_fig5-2.svg 把 Cohesive 与 Discreet 的左右位置对调，并换成粉彩配色；不能据它判断任一方法的坐标位置。

## 原文证据

### [PDF 第 39 页](../../../documents/G212.md#page-39)

> This chapter gives an overview of the four steps that need to be followed for a comprehensive approach to digital technology adoption. The four steps are highlighted in Figure 5-1 and then explained in more detail in the text that follows.
> The organization must select the adoption approach for the digital technology it desires to adopt. The “ABCD” framework comprises the fitment of all types of organization with respect to their digital technology adoption strategy.
### [PDF 第 40 页](../../../documents/G212.md#page-40)

> Based on the ABCD framework, the four quadrants represent the following adoption approach:
> • Avant-Garde (low ubiquity, high velocity): enterprises that allow or enable some parts (like a Line of Business (LOB), function, geography, department) to adopt first and pass on this experience to others

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

源图记录：[原始解释与转录](../../../figures/G212/fig5-2.json)。

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
      "四个象限的填充色原图没有图例说明；本分析只按位置与色块区分，不推断颜色代表优劣（原文明确无排名）。",
      "中文稿 SVG 与英文原图的象限位置不一致，本分析以英文 PDF 第 40 页为准。"
    ],
    "analyzed_from": [
      "英文 PDF 第 40 页原图截图（2×2 放大分块）",
      "英文 PDF 第 39–40 页正文",
      "中文稿 G212e_数字技术采用就绪度评估.md 第 503–519 行",
      "figs/g212_fig5-2.svg 源码与文字"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": [
    {
      "id": "source-g212-fig5-2",
      "figure_id": "G212/fig5-2",
      "status": "observed-conflict",
      "description": "正文§5.1定义C为高普及低变化、D为低普及低变化；本地中文重绘将底部C/D左右位置互换。",
      "evidence": [
        "G212 §5.1",
        "figs/g212_fig5-2.svg",
        "figs/ai/G212/fig5-2.json"
      ],
      "resolution": "采用正文定义：A左上、B右上、C右下、D左下；保留重绘冲突，不将图中位置误植为架构规则。"
    }
  ]
}
```
