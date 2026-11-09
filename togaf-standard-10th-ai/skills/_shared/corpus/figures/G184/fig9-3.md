# G184/fig9-3 · 执行 EA 能力的团队

> 当前图示解析：[Markdown](../../architecture/diagrams/G184/fig9-3.md) · [JSON](../../architecture/diagrams/G184/fig9-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G184e.pdf`；SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

## 原图 · PDF 第 84 页

![英文原图](../assets/G184/fig9-3-p0084.png)

PDF 坐标：`[125.6, 36.0, 486.4, 399.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
EA Governance
Extended
EA Team
Core
EA Team
© The Open Group
```

## 概要（历史解释；局部修正见上）

执行 EA 能力的三个团队层次：EA 治理、扩展 EA 团队、核心 EA 团队，由外向内嵌套。

## 目的（历史解释；局部修正见上）

说明“谁在执行 EA 能力”：最外层是治理机构（正文称架构委员会或治理委员会），中间是包含各域专家与跨学科人员的扩展 EA 团队，内层是聚焦战略、流程与建议的核心团队。作者用同心圆强调三者是范围与职责的包含关系，而不是三个互不相干的部门。

## 阅读顺序（历史解释；局部修正见上）

从外向内读三个同心圆：最外圈深青色是 EA Governance（EA 治理），中间蓝色是 Extended EA Team（扩展 EA 团队），最内圈浅蓝色是 Core EA Team（核心 EA 团队）。没有箭头；圆的大小与嵌套关系表示范围由大到小、内层被外层包含。

## 关键含义（历史解释；局部修正见上）

- 三层同心嵌套：EA 治理包住扩展 EA 团队，扩展 EA 团队包住核心 EA 团队。
- EA 治理对应正文的架构委员会/治理委员会，相当于 EA 能力这个“企业中的企业”的董事会，设定并管理企业的总体方向。
- 扩展 EA 团队包含业务、信息、应用、技术与安全等主要域的专家，也可包含战略规划者、财务与市场分析师、业务线领导、主题专家及服务/支持人员。
- 核心团队聚焦战略、流程与建议，是日常架构工作的最小核心。
- 正文强调职责分离：构建块构成、目录服务或装配线布局等具体架构决策，更适合在扩展 EA 团队层面决定，不应把这类决策权嵌入治理机构。
- 图中只表达范围嵌套，不表达汇报线、人数、全职/兼职或资金关系；同心圆的面积也没有数量含义。
- 正文补充：多个 EA 团队时仍只有一个 EA 能力、一个领导者；各团队的汇报与资金体系可以不同，但都要在该领导者指导下协作（背景知识，见 9.2 节）。

## 层级（历史解释；局部修正见上）

三层嵌套：EA 治理（L1）⊃ 扩展 EA 团队（L2）⊃ 核心 EA 团队（L3）。语义上是范围/职责的包含，不是组织汇报层级；图中没有画出任何汇报线。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头。三个同心圆的包含关系完全由“圆套圆”的几何位置表达；外层圆环本身代表治理层，不是背景。

## 易误读点（历史解释；局部修正见上）

- 不要把三层读成三个汇报层级或三个独立部门；图中没有汇报线，正文也没有说核心团队向扩展团队汇报。
- 不要因为核心团队画得最小就认为它最不重要；它是日常架构工作的核心，外两层提供治理与专家支持。
- 不要以为治理层包办所有架构决策；正文明确具体构建块与权衡决策应在扩展 EA 团队层面做。
- 不要把圆环面积当作人数或预算比例；图中没有量化编码。
- 中文资产把最内圈“Core EA Team”保留英文，不要误以为内圈没有中文名或另有含义。

## 元素

```json
[
  {
    "id": "ea_governance",
    "label_en": "EA Governance",
    "label_zh": "EA 治理",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "最外层深青色圆环",
    "description_zh": "EA 能力的治理层；正文对应架构委员会/治理委员会，设定并管理总体方向，不嵌入具体架构决策权。"
  },
  {
    "id": "extended_ea_team",
    "label_en": "Extended EA Team",
    "label_zh": "扩展 EA 团队",
    "type": "organization_unit",
    "parent": "ea_governance",
    "level": 2,
    "order": 2,
    "position": "中层蓝色圆环",
    "description_zh": "包含业务、信息、应用、技术与安全等域专家，以及战略规划、财务/市场分析、业务线领导、主题专家等跨学科人员。"
  },
  {
    "id": "core_ea_team",
    "label_en": "Core EA Team",
    "label_zh": "核心 EA 团队",
    "type": "organization_unit",
    "parent": "extended_ea_team",
    "level": 3,
    "order": 3,
    "position": "内层浅蓝色圆",
    "description_zh": "聚焦战略、流程与建议的最小核心团队。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "同心圆 / 色环",
    "meaning_zh": "一个团队范围层次；由外向内范围缩小",
    "explicit": false
  },
  {
    "symbol": "深青外环",
    "meaning_zh": "EA 治理层（架构委员会/治理委员会）",
    "explicit": false
  },
  {
    "symbol": "蓝色中环",
    "meaning_zh": "扩展 EA 团队（含各域专家与跨学科人员）",
    "explicit": false
  },
  {
    "symbol": "浅蓝内圆",
    "meaning_zh": "核心 EA 团队（聚焦战略、流程与建议）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "三个同心圆居中：外层深青色大圆（EA 治理），中层蓝色圆（扩展 EA 团队），内层浅蓝色小圆（核心 EA 团队）；各层名称写在其圆环的上部/中央。"
}
```

## 相关图

```json
[
  {
    "target": "G184/fig9-2",
    "relation": "complements",
    "note_zh": "同属 9.3 节：图 9-2 分解 EA 能力/活动，本图给出执行这些能力的团队范围层次。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中没有箭头；“三层是范围包含而非汇报层级”的判断依据同心圆版式与正文的职责分离表述，未在图中明示。",
    "EA 治理是否等同于正文的架构委员会/治理委员会，正文只作类比（“相当于董事会”），图中未写全称。",
    "扩展 EA 团队与核心团队的具体人员构成来自正文，图中只有层次名称。"
  ],
  "analyzed_from": [
    "英文 PDF 第 84 页图 9-3 截图与 2x2 放大分块",
    "英文 PDF 第 83、84 页正文",
    "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 859-884 行",
    "figs/zh/g184e_fig9-3_zh.png"
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
