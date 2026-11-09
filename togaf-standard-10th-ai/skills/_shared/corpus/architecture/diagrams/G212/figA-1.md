# G212/figA-1 · 李克特量表

类型：`mapping-or-assessment-matrix`。使问卷回答具有明确行为/组织状态含义：Neutral意味着已定义、已验证和已理解，但没有承诺、传播与演进路径。

英文 PDF 物理页：[49]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 49 页原图](../../../figures/assets/G212/figA-1-p0049.png)

[完整 JSON](figA-1.json) · [可编辑 Mermaid](figA-1.mmd) · [仅关系图](figA-1.relations.mmd) · [层级分解图](figA-1.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
  n0["Strongly Agree"]
  n1["Agree"]
  n2["Somewhat Agree"]
  n3["Neutral"]
  n4["Somewhat Disagree"]
  n5["Disagree"]
  n6["Strongly Disagree"]
  n7["Define"]
  n8["Validate"]
  n9["Understand"]
  n10["Commit"]
  n11["Disseminate"]
  n12["Evolve"]
```

## 架构分析

从左到右读七个回答，再按每列自下而上核对Define、Validate、Understand、Commit、Disseminate、Evolve六条件。颜色表示该回答对应的条件状态；没有数字计分或连接箭头。

- 本图有 13 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 本图没有可直接确认为人员直属汇报的关系；视觉上下位置、能力分解和治理职责分别读取。
- 包含分组后有 13 个连通分量；分离可能源于图例、并列分类或独立示例，未自动补边。
- 逐格核对7级回答×6层共42格，青色已满足状态分别为6、5、4、3、2、1、0层。
- Neutral只定义/验证/理解，不含承诺/传播/演进；完整保留Existent/Fulfilled及Nonexistent/Not Fulfilled图例。
- 本轮再次实际目视PDF49：七个语言回答、六个条件层及全部42格，无1–7数字赋分。
- 历史中文及节点score=7…1是编者附加编码，不能当作官方量表或自动计算总分/平均。当前节点与表格移除此编码。

### 如何用于项目

- 先固定行、列所代表的维度及单元格含义，再登记有证据的映射或评分。
- 空白、无关系、未测量和不适用分别处理；颜色不自动等于优先级。

### 结构所表达的逻辑

- 七个回答依次为Strongly Agree、Agree、Somewhat Agree、Neutral、Somewhat Disagree、Disagree、Strongly Disagree。
- 对应满足条件数为6、5、4、3、2、1、0；该计数仅描述图的填充格，不是官方评分。
- Neutral不是无意见，而是已定义、验证、理解；尚未承诺、传播或演进。
- 非常不同意明确表示六条件均不满足；未填写、缺证据和不适用不是该回答。
- 原图没有1–7数值，未给跨题加权、平均分、总分阈值或通过规则。

## 上下级与包含

七列为同一语言量表的回答档位；六条件按填充图案累积。图没有组织上下级、任务授权或阶段执行顺序。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|
|sa|Strongly Agree|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|a|Agree|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|swa|Somewhat Agree|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|n|Neutral|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|swd|Somewhat Disagree|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|d|Disagree|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|sd|Strongly Disagree|metric|官方语言回答档位；不是数字评分，未填写不等于非常不同意。|—||
|lvl_define|Define|concept|最低层级：特征已被定义。|—||
|lvl_validate|Validate|concept|定义之后被验证。|—||
|lvl_understand|Understand|concept|验证之后被理解。|—||
|lvl_commit|Commit|concept|组织对特征作出承诺。|—||
|lvl_disseminate|Disseminate|concept|承诺之后在组织内传播。|—||
|lvl_evolve|Evolve|concept|最高层级：具备演进路径。|—||

### 非常同意：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Strongly Agree",
  "official_numeric_score": null
}
```

### 同意：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Agree",
  "official_numeric_score": null
}
```

### 比较同意：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Somewhat Agree",
  "official_numeric_score": null
}
```

### 中立：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Neutral",
  "official_numeric_score": null
}
```

### 比较不同意：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Somewhat Disagree",
  "official_numeric_score": null
}
```

### 不同意：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Disagree",
  "official_numeric_score": null
}
```

### 非常不同意：属性

```json
{
  "scale_id": "G212-figA-1-language-response",
  "response_label_en": "Strongly Disagree",
  "official_numeric_score": null
}
```

## 全部关系

无连线、箭头或基数。列定位回答，行定位条件，深青填充=Existent/Fulfilled，白色=Nonexistent/Not Fulfilled；不用视觉相邻推导过程依赖。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## 七级李克特量表 × 六个累积层级（逐格转录）

```json
{
  "id": "t_likert",
  "title_zh": "七级李克特量表 × 六个累积层级（逐格转录）",
  "columns": [
    "层级（图内自上而下）",
    "Strongly Agree 非常同意",
    "Agree 同意",
    "Somewhat Agree 比较同意",
    "Neutral 中立",
    "Somewhat Disagree 比较不同意",
    "Disagree 不同意",
    "Strongly Disagree 非常不同意"
  ],
  "rows": [
    [
      "Evolve 演进",
      "已存在/已满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足"
    ],
    [
      "Disseminate 传播",
      "已存在/已满足",
      "已存在/已满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足"
    ],
    [
      "Commit 承诺",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足"
    ],
    [
      "Understand 理解",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "不存在/未满足",
      "不存在/未满足",
      "不存在/未满足"
    ],
    [
      "Validate 验证",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "不存在/未满足",
      "不存在/未满足"
    ],
    [
      "Define 定义",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "已存在/已满足",
      "不存在/未满足"
    ]
  ],
  "cell_legend": [
    "已存在/已满足 = 深青色实心格（Existent/Fulfilled）",
    "不存在/未满足 = 白色格（Nonexistent/Not Fulfilled）"
  ],
  "notes_zh": "本轮逐格核对原图，六行七列共42格。深青色为已存在/已满足、白色为不存在/未满足。官方未赋1–7数字，也未规定跨题总分/平均分或合格阈值；未知回答保持未评价。"
}
```

## 误读检查

- 不能将历史score=7…1附加编码当成官方值。
- 不能把已满足条件数当等距分值，进而自动平均或声称通过。
- 不能把无证据默认评为最差档或Neutral。
- 不能把G212组织就绪回答映射成G249个人熟练度、Open CA认证或AI执行权限。

## 原文证据

### [PDF 第 49 页](../../../documents/G212.md#page-49)

> The questionnaire is to be answered using the Likert scale provided in Figure A-1, where each term of the Likert scale has a distinct meaning which is explained through the illustration. For instance, the readiness of an enterprise would be marked “neutral” if the characteristic corresponding to a question is defined, validated, and understood without any commitment, dissemination, and evolution path.

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

源图记录：[原始解释与转录](../../../figures/G212/figA-1.json)。

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
      "原图未说明六个层级各自的操作性定义；本分析只按层级名与累积填充关系描述，不扩展定义。",
      "“Very Strongly Agree”之类中间档不存在：原图只有 7 档，且“Somewhat Agree/Disagree”位于 Neutral 两侧。",
      "中文稿中文化图在“同意”列的“传播”格有半格填充异常，按英文原图与表 A-1 应为整格已满足。"
    ],
    "analyzed_from": [
      "英文 PDF 第 49 页原图截图（2×2 放大分块，逐列核对填充格）",
      "英文 PDF 第 49 页正文（A.1 量表说明）",
      "中文稿 G212e_数字技术采用就绪度评估.md 第 699–745 行（含图内标签对照表与表 A-1）",
      "figs/zh/g212e_figA-1_zh.png",
      "figs/g212e_figA-1_en.png（自动相似度 0.973）"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": [
    {
      "description_zh": "旧中文和历史节点增加1–7数字编码，官方图与邻近正文无此定义；当前解释拒绝该官方归属。",
      "resolution": "preserve-historical-record-exclude-from-current-scale"
    }
  ]
}
```
