# G184/fig3-1 · 商业企业的语境

> 当前图示解析：[Markdown](../../architecture/diagrams/G184/fig3-1.md) · [JSON](../../architecture/diagrams/G184/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G184e.pdf`；SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

## 原图 · PDF 第 23 页

![英文原图](../assets/G184/fig3-1-p0023.png)

PDF 坐标：`[112.7, 36.0, 499.3, 270.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Economic Growth, Laws,
Regulations, Taxes, and Incentives
Economy
Demand, Competition,
and Revenues
Market
Trade, Jobs, and
Tax Revenues
Work, Assignments,
and Resources
Enterprise
Supply of Products,
and Services, Earnings
Intraprise
Work Products
and Costs
```

## 概要（历史解释；局部修正见上）

商业企业的四层语境：经济、市场、企业、企业内部，相邻层级之间双向交换资源与约束。

## 目的（历史解释；局部修正见上）

说明商业企业所处的语境：企业活动于市场之中，市场又嵌在更大的经济体中；企业内部单元再从企业接受工作与资源，并回交工作产品与成本。作者用这张图界定 EA 与 EA 能力必须理解的外部与内部交互，并紧接着指出公共、政府、国防企业的语境与此不同。

## 阅读顺序（历史解释；局部修正见上）

从左上角的 Economy 读起，沿对角线向右下走到 Intraprise，这是由外到内的四个语境层级。每一对相邻框之间有两条方向相反的箭头：靠右/靠下的标签描述去程交换，靠左/靠上的标签描述回程交换。例如 Economy 右下方的箭头带“Economic Growth, Laws, Regulations, Taxes, and Incentives”，Market 左上方那条箭头带“Trade, Jobs, and Tax Revenues”。图中没有总框，也没有跨层箭头。

## 关键含义（历史解释；局部修正见上）

- 四个语境层级是 Economy（经济）→ Market（市场）→ Enterprise（企业）→ Intraprise（企业内部），沿对角线自上而下、自左而右排列，表示由外到内的观察范围。
- 相邻层级两两双向交换：经济向市场提供经济增长、法律、法规、税收与激励，市场向经济回交贸易、就业与税收。
- 市场向企业提供需求、竞争与收入，企业向市场回交产品与服务供给、收益。
- 企业向企业内部单元下达工作、任务与资源，企业内部单元向企业回交工作产品与成本。
- 图中只有相邻层对的往返箭头，没有跨层连线，也没有形成闭合回路；它表达的是交换关系，不是价值流或流程顺序。
- 图题把语境限定为“商业企业”（Commercial Enterprise）；正文说明公共、政府、国防企业的语境不同，本文档整体按营利、上市、公共国防或社会部门企业假设。
- Intraprise 按尾注 [2] 定义为“企业内部按地理或逻辑划分、职能不一定延伸到企业边界之外的自治职能组合”，多个 intraprise 构成一个 enterprise。
- 图内的 © The Open Group 与尾注 [1] 表明该图源自 Rouse 2012 年的企业转型演讲，不是 TOGAF 自创的参考模型。

## 层级（历史解释；局部修正见上）

视觉上是四个并列的语境层级，不是嵌套包含：Economy 和 Market 属于企业外部语境，Enterprise 和 Intraprise 属于组织范围。Intraprise 与 Enterprise 分开画、地位并列，但语义上多个 intraprise 构成一个 enterprise（尾注 [2]），所以不能把它读成企业之外的一个独立组织。

## 线条含义（历史解释；局部修正见上）

共六条黑色实线箭头，全部是相邻层级之间的单向交换，两两成对、方向相反：Economy→Market（向下）、Market→Economy（向上）、Market→Enterprise（向下）、Enterprise→Market（向上）、Enterprise→Intraprise（向下）、Intraprise→Enterprise（向上）。箭头旁的文字就是该方向传递的内容；箭头没有线型或颜色区分。

## 易误读点（历史解释；局部修正见上）

- 不要把四个框读成包含关系（例如以为 Intraprise 画在 Enterprise 里面）；它们是阶梯排列的并列范围，包含只体现在语义上（多个 intraprise 构成 enterprise）。
- 不要把四个框读成流程阶段或价值链环节；箭头是双向交换，不是一条从左到右的流程。
- 不要把“需求、竞争与收入”与“产品与服务供给、收益”看成同一方向；它们是一对相反箭头，前者由市场流向企业，后者由企业流向市场。
- 不要把 Intraprise 当作企业内的一个部门框；它是与 Enterprise 并列画出的范围层级，尾注给出了专门定义。
- 中文稿 L623 把本图插在 7.1 节“创建框架目录”中，是错位引用；本图实际属于 3.2 节“什么是企业？”，正文语境在中文稿 L153。
- 中文资产把顶部标签压缩成“法规税收与激励”并留下重叠小字，还断开了一处折线，不能据它理解完整的交换内容。

## 元素

```json
[
  {
    "id": "economy",
    "label_en": "Economy",
    "label_zh": "经济",
    "type": "actor",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "左上角",
    "description_zh": "最外层的经济语境；向市场提供经济增长、法律、法规、税收与激励，并从市场获得贸易、就业与税收。"
  },
  {
    "id": "market",
    "label_en": "Market",
    "label_zh": "市场",
    "type": "actor",
    "parent": null,
    "level": 2,
    "order": 2,
    "position": "中上偏右",
    "description_zh": "企业所处的市场；承接经济条件并向经济回交贸易、就业与税收，向企业提出需求、竞争与收入，并从企业获得产品、服务与收益。"
  },
  {
    "id": "enterprise",
    "label_en": "Enterprise",
    "label_zh": "企业",
    "type": "organization_unit",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "中下偏左",
    "description_zh": "本文档定义的 enterprise（组织的最高描述层级，不等同法律或职能边界）；向企业内部单元分配工作、任务与资源。"
  },
  {
    "id": "intraprise",
    "label_en": "Intraprise",
    "label_zh": "企业内部",
    "type": "organization_unit",
    "parent": null,
    "level": 4,
    "order": 4,
    "position": "右下角",
    "description_zh": "企业内按地理或逻辑划分的自治职能组合（尾注 [2]）；多个 intraprise 构成一个 enterprise，向企业回交工作产品与成本。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_econ_market",
    "from": "economy",
    "to": "market",
    "type": "flow",
    "label_en": "Economic Growth, Laws, Regulations, Taxes, and Incentives",
    "label_zh": "经济增长、法律、法规、税收与激励",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Economy 右侧出线、向下折入 Market 顶部。"
  },
  {
    "id": "r_market_econ",
    "from": "market",
    "to": "economy",
    "type": "flow",
    "label_en": "Trade, Jobs, and Tax Revenues",
    "label_zh": "贸易、就业与税收",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Market 左侧出线、向上折入 Economy 底部。"
  },
  {
    "id": "r_market_ent",
    "from": "market",
    "to": "enterprise",
    "type": "flow",
    "label_en": "Demand, Competition, and Revenues",
    "label_zh": "需求、竞争与收入",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Market 右侧出线、向下折入 Enterprise 顶部。"
  },
  {
    "id": "r_ent_market",
    "from": "enterprise",
    "to": "market",
    "type": "flow",
    "label_en": "Supply of Products, and Services, Earnings",
    "label_zh": "产品与服务供给、收益",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Enterprise 左侧出线、向上折入 Market 底部。"
  },
  {
    "id": "r_ent_intra",
    "from": "enterprise",
    "to": "intraprise",
    "type": "flow",
    "label_en": "Work, Assignments, and Resources",
    "label_zh": "工作、任务与资源",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Enterprise 右侧出线、向下折入 Intraprise 顶部。"
  },
  {
    "id": "r_intra_ent",
    "from": "intraprise",
    "to": "enterprise",
    "type": "flow",
    "label_en": "Work Products and Costs",
    "label_zh": "工作产品与成本",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从 Intraprise 左侧出线、向上折入 Enterprise 底部。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "蓝色实心矩形",
    "meaning_zh": "一个语境层级/参与者（经济、市场、企业、企业内部）",
    "explicit": false
  },
  {
    "symbol": "黑色细实线箭头",
    "meaning_zh": "相邻层级之间传递内容的方向",
    "explicit": false
  },
  {
    "symbol": "箭头旁的两行文字",
    "meaning_zh": "该方向所交换的内容（资源、约束、收入、工作等）",
    "explicit": false
  },
  {
    "symbol": "对角阶梯排列",
    "meaning_zh": "由外（经济）到内（企业内部）的语境层级，不是包含框",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "四个等大的蓝色矩形沿对角线阶梯排列：Economy 左上、Market 中上、Enterprise 中下、Intraprise 右下。每对相邻框之间用“横向出线 + 竖向转折”的折线箭头连接，去程与回程各一条，标签放在折线拐角外侧。"
}
```

## 相关图

```json
[
  {
    "target": "G184/fig4-2",
    "relation": "complements",
    "note_zh": "图 4-2 从组织范围角度给出扩展企业视图（环境⊃扩展企业⊃企业⊃内部单元），与本图的四层经济语境互补；两图共用 Enterprise 与 Intraprise 概念。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "“Intraprise”的中文译名采用中文资产中的“企业内部”；尾注定义为“企业内部按地理或逻辑划分的自治职能组合”，该译名只表达了位置、未表达自治组合的含义。",
    "骨架把本图归到 7.1 节（中文稿 L623 的重复占位图），但图与 3.2 节正文对应；section_en 已按实际章节填写，section_zh/md_lines 仍沿用骨架位置，未能改写。",
    "图中四个框是并列范围而非嵌套；Intraprise 与 Enterprise 的语义包含只来自尾注，图中没有画出包含线。",
    "顶部“Economic Growth...”标签字号较小且换行多，已用 2x2 放大块逐字核对，未发现缺词。"
  ],
  "analyzed_from": [
    "英文 PDF 第 23 页图 3-1 截图与 2x2 放大分块",
    "英文 PDF 第 22、23、28 页正文与尾注",
    "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 140-175 行、第 610-625 行",
    "figs/zh/g184e_fig3-1_zh.png 逐块放大对照"
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
