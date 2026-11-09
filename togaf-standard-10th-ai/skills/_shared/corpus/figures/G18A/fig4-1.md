# G18A/fig4-1 · 战略、业务模型与架构之间的关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G18A/fig4-1.md) · [JSON](../../architecture/diagrams/G18A/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G18Ae.pdf`；SHA-256：`ed764e6eaeaad0cfccc67841223c76429684b31f188e6e90fbaf17cd44bc1fe4`。

## 原图 · PDF 第 18 页

![英文原图](../assets/G18A/fig4-1-p0018.png)

PDF 坐标：`[61.1, 36.0, 550.9, 375.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Bargaining
Bargaining
Po’
of
Pov
of
Buy
Suppl
Three
of
Competiti
Si
ubstitut
Riv
Produ
or
Organization
Value Chain
Process/Value Stream
Agi
ation &
rvic
lodels
lodels
Decomposition
of
s
Balanced
Operational
Dashboards
Models
Scorecard
Strategic
Posi
n
Supply Chain
Capability Map
Business/ Domain
repre:
Models
Mappings
ted by
=== 3 2 —>
articulated by
Value Streams
Information Map
Business Model
Business Architecture Blueprints
```

## 概要（历史解释；局部修正见上）

从波特五力到战略定位，再到业务模型与业务架构蓝图，展示战略如何经业务模型被架构阐明。

## 目的（历史解释；局部修正见上）

说明业务模型在战略与业务架构之间的中介位置：竞争态势驱动战略定位，战略定位由业务模型来表示，业务模型再由一组业务架构蓝图展开；以此支撑第 4 节「业务架构阐明业务模型的不同视角」的论点，并对应 TOGAF 阶段 B 的架构蓝图工作。

## 阅读顺序（历史解释；局部修正见上）

左上读五力：四个蓝框的箭头全部指向中央圆形 Competitive Rivalry，表示竞争强度由四力共同决定。沿向下的粗箭头读“drives”：竞争强度驱动 Strategic Position。再向下读“represented by”：战略定位由业务模型（3×3 灰蓝网格）来表示。最后向右读“articulated by”：业务模型由右侧 11 个业务架构蓝图来阐明。三个斜体短语是判断方向的关键，不要漏读。

## 关键含义（历史解释；局部修正见上）

- 左上四力（Bargaining Power of Buyers、Bargaining Power of Suppliers、Threat of New Entrants、Threat of Substitute Products or Services）分别用箭头指向中央的 Competitive Rivalry，表示它们共同塑造竞争强度。
- Competitive Rivalry 通过标有 drives 的箭头指向 Strategic Position：战略定位是对竞争态势的回应。
- Strategic Position 通过标有 represented by 的箭头指向 Business Model：业务模型是战略定位的表示，而不是战略本身。
- Business Model 区域是 3×3 网格：上排 Key Activities、Value Proposition、Customer Relationships；中排 Key Partners、Customers、Key Resources；下排 Costs、Channels、Revenue。
- Business Model 通过标有 articulated by 的箭头指向右侧 Business Architecture Blueprints：业务架构把模型展开为多个视角的蓝图。
- 蓝图共 11 个，分四行：Organization Models、Value Chain Models、Process/Value Stream Aggregation & Decomposition；Operational Models、Dashboards、Balanced Scorecard；Supply Chain Models、Capability Map、Business/Domain Mappings；Value Streams、Information Map。
- 图注说明左上改编自 Porter 的五力模型、右侧蓝图来自 BIZBOK 6.5，因此本图是引用并组合两套来源的示意图，不是 TOGAF 专用记法。
- 全图只有一条向下的主链，没有反馈箭头；正文虽提到业务架构可把讨论回馈到业务模型，但图中未画这条回路。

## 层级（历史解释；局部修正见上）

四段递进：① 四力 → Competitive Rivalry；② Competitive Rivalry → Strategic Position；③ Strategic Position → Business Model（其内 9 个画布块并列）；④ Business Model → Business Architecture Blueprints（其内 11 个蓝图并列，按 3+3+3+2 排布）。各段内部并列，段与段之间是单向推导，不是组织上下级。

## 线条含义（历史解释；局部修正见上）

共 7 条箭头：4 条从四力框指向 Competitive Rivalry（无文字）；1 条向下标 drives；1 条向下标 represented by；1 条向右标 articulated by。全部为浅蓝色粗箭头、单向；斜体动词说明关系性质，箭头方向即阅读方向。

## 易误读点（历史解释；局部修正见上）

- 不要把左上五力框当成业务模型的组成部分：它们属于战略分析区，只通过 Competitive Rivalry 与主链相连。
- 不要漏看 drives / represented by / articulated by 三个动词：它们决定整条链的方向，只看框会误以为四者并列。
- 不要把 11 个业务架构蓝图当成 11 个流程步骤，它们是同一阶段可选的架构视角/蓝图。
- 不要把 Business Model 的 3×3 网格与图 2-4 的手绘画布混为一谈：本图把九块排成 3×3，且用的是 Customers 而非 Customer Segments。
- 中文稿第 140 行引用的 SVG 把本图简化为“战略→业务模型→业务架构→执行”四框，丢失五力、战略定位与全部蓝图，不能据它理解本图。

## 元素

```json
[
  {
    "id": "f_buyers",
    "label_en": "Bargaining Power of Buyers",
    "label_zh": "买方议价能力",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "五力区上排左"
  },
  {
    "id": "f_suppliers",
    "label_en": "Bargaining Power of Suppliers",
    "label_zh": "供方议价能力",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "五力区上排右"
  },
  {
    "id": "f_entrants",
    "label_en": "Threat of New Entrants",
    "label_zh": "新进入者威胁",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "五力区左侧"
  },
  {
    "id": "f_substitutes",
    "label_en": "Threat of Substitute Products or Services",
    "label_zh": "替代产品或服务威胁",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "五力区右侧"
  },
  {
    "id": "f_rivalry",
    "label_en": "Competitive Rivalry",
    "label_zh": "竞争强度",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "五力区中央圆"
  },
  {
    "id": "strategic_position",
    "label_en": "Strategic Position",
    "label_zh": "战略定位",
    "type": "concept",
    "parent": null,
    "level": 1,
    "position": "中列上方，深青色框"
  },
  {
    "id": "business_model",
    "label_en": "Business Model",
    "label_zh": "业务模型",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "中列下方，3×3 网格及其下方标题",
    "description_zh": "标题 Business Model 位于网格正下方；网格本身没有外框。"
  },
  {
    "id": "bm_activities",
    "label_en": "Key Activities",
    "label_zh": "关键活动",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 1 行第 1 列"
  },
  {
    "id": "bm_value_prop",
    "label_en": "Value Proposition",
    "label_zh": "价值主张",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 1 行第 2 列"
  },
  {
    "id": "bm_cust_rel",
    "label_en": "Customer Relationships",
    "label_zh": "客户关系",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 1 行第 3 列"
  },
  {
    "id": "bm_partners",
    "label_en": "Key Partners",
    "label_zh": "关键合作伙伴",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 2 行第 1 列"
  },
  {
    "id": "bm_customers",
    "label_en": "Customers",
    "label_zh": "客户",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 2 行第 2 列"
  },
  {
    "id": "bm_resources",
    "label_en": "Key Resources",
    "label_zh": "关键资源",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 2 行第 3 列"
  },
  {
    "id": "bm_costs",
    "label_en": "Costs",
    "label_zh": "成本",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 3 行第 1 列"
  },
  {
    "id": "bm_channels",
    "label_en": "Channels",
    "label_zh": "渠道",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 3 行第 2 列"
  },
  {
    "id": "bm_revenue",
    "label_en": "Revenue",
    "label_zh": "收入",
    "type": "concept",
    "parent": "business_model",
    "level": 2,
    "position": "网格第 3 行第 3 列"
  },
  {
    "id": "ba_blueprints",
    "label_en": "Business Architecture Blueprints",
    "label_zh": "业务架构蓝图",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右侧大区，标题在区下方",
    "description_zh": "包含 11 个橙色卡片，按 3+3+3+2 排列。"
  },
  {
    "id": "ba_org",
    "label_en": "Organization Models",
    "label_zh": "组织模型",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 1 行第 1 列"
  },
  {
    "id": "ba_value_chain",
    "label_en": "Value Chain Models",
    "label_zh": "价值链模型",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 1 行第 2 列"
  },
  {
    "id": "ba_process",
    "label_en": "Process/Value Stream Aggregation & Decomposition",
    "label_zh": "流程/价值流聚合与分解",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 1 行第 3 列"
  },
  {
    "id": "ba_operational",
    "label_en": "Operational Models",
    "label_zh": "运营模型",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 2 行第 1 列"
  },
  {
    "id": "ba_dashboards",
    "label_en": "Dashboards",
    "label_zh": "仪表盘",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 2 行第 2 列"
  },
  {
    "id": "ba_scorecard",
    "label_en": "Balanced Scorecard",
    "label_zh": "平衡计分卡",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 2 行第 3 列"
  },
  {
    "id": "ba_supply_chain",
    "label_en": "Supply Chain Models",
    "label_zh": "供应链模型",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 3 行第 1 列"
  },
  {
    "id": "ba_capability_map",
    "label_en": "Capability Map",
    "label_zh": "能力地图",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 3 行第 2 列"
  },
  {
    "id": "ba_domain_map",
    "label_en": "Business/ Domain Mappings",
    "label_zh": "业务/域映射",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 3 行第 3 列"
  },
  {
    "id": "ba_value_streams",
    "label_en": "Value Streams",
    "label_zh": "价值流",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 4 行第 1 列"
  },
  {
    "id": "ba_info_map",
    "label_en": "Information Map",
    "label_zh": "信息地图",
    "type": "artifact",
    "parent": "ba_blueprints",
    "level": 2,
    "position": "第 4 行第 2 列"
  }
]
```

## 关系

```json
[
  {
    "id": "r_buyers_rivalry",
    "from": "f_buyers",
    "to": "f_rivalry",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "买方议价能力作用于竞争强度。"
  },
  {
    "id": "r_suppliers_rivalry",
    "from": "f_suppliers",
    "to": "f_rivalry",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "供方议价能力作用于竞争强度。"
  },
  {
    "id": "r_entrants_rivalry",
    "from": "f_entrants",
    "to": "f_rivalry",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "新进入者威胁作用于竞争强度。"
  },
  {
    "id": "r_substitutes_rivalry",
    "from": "f_substitutes",
    "to": "f_rivalry",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "替代品威胁作用于竞争强度。"
  },
  {
    "id": "r_rivalry_position",
    "from": "f_rivalry",
    "to": "strategic_position",
    "type": "causal",
    "label_en": "drives",
    "label_zh": "驱动",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "竞争强度驱动战略定位；动词以斜体写在箭头旁。"
  },
  {
    "id": "r_position_model",
    "from": "strategic_position",
    "to": "business_model",
    "type": "other",
    "label_en": "represented by",
    "label_zh": "由……表示",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "战略定位由业务模型来表示：业务模型是战略定位的具象表达。"
  },
  {
    "id": "r_model_blueprints",
    "from": "business_model",
    "to": "ba_blueprints",
    "type": "other",
    "label_en": "articulated by",
    "label_zh": "由……阐明",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "业务模型由业务架构蓝图来阐明/展开：蓝图给出模型的多视角细节。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_strategy_chain",
    "kind": "sequence",
    "name_zh": "竞争态势到业务架构蓝图的推导链",
    "steps": [
      "f_rivalry",
      "strategic_position",
      "business_model",
      "ba_blueprints"
    ],
    "description_zh": "四力汇入竞争强度后，沿 drives → represented by → articulated by 单向推进。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_blueprints",
    "title_zh": "业务架构蓝图区的排列（按原图逐行）",
    "columns": [
      "行",
      "第 1 列",
      "第 2 列",
      "第 3 列"
    ],
    "rows": [
      [
        "1",
        "Organization Models",
        "Value Chain Models",
        "Process/Value Stream Aggregation & Decomposition"
      ],
      [
        "2",
        "Operational Models",
        "Dashboards",
        "Balanced Scorecard"
      ],
      [
        "3",
        "Supply Chain Models",
        "Capability Map",
        "Business/ Domain Mappings"
      ],
      [
        "4",
        "Value Streams",
        "Information Map",
        "—"
      ]
    ],
    "notes_zh": "共 11 个蓝图卡片；第 4 行只有 2 个。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "亮蓝色圆角框",
    "meaning_zh": "波特五力的四个作用力",
    "explicit": false
  },
  {
    "symbol": "亮蓝色圆形",
    "meaning_zh": "Competitive Rivalry（竞争强度）",
    "explicit": false
  },
  {
    "symbol": "深青色圆角框",
    "meaning_zh": "Strategic Position（战略定位）",
    "explicit": false
  },
  {
    "symbol": "灰蓝色标签形小框（3×3）",
    "meaning_zh": "业务模型的九个画布构建块",
    "explicit": false
  },
  {
    "symbol": "橙色圆角框",
    "meaning_zh": "业务架构蓝图（11 个视角）",
    "explicit": false
  },
  {
    "symbol": "浅蓝粗箭头",
    "meaning_zh": "有方向的推导/表示/阐明关系",
    "explicit": false
  },
  {
    "symbol": "斜体动词（drives / represented by / articulated by）",
    "meaning_zh": "关系的性质说明",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "左上为五力区（上排两个框、左右各一个框、中央圆形 Competitive Rivalry）；其下为中列（Strategic Position 框 → 3×3 业务模型网格）；最右为业务架构蓝图区（3 行×3 加 1 行×2 的圆角卡片）。主链自上而下，最后一段水平向右。"
}
```

## 相关图

```json
[
  {
    "target": "G18A/fig2-4",
    "relation": "related",
    "note_zh": "图中的 Business Model 九块沿用业务模型画布的构建块名称，但排成 3×3 且用 Customers/Costs/Revenue 的简写"
  },
  {
    "target": "G18A/figA-1",
    "relation": "related",
    "note_zh": "九块名称与画布构建块对应，可对照附录 A 的定义阅读"
  },
  {
    "target": "G18A/fig7-1",
    "relation": "related",
    "note_zh": "第 7 章用同一画布九块描述零售现状，可作为业务模型一侧的实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四力指向 Competitive Rivalry 的四条箭头没有文字，解析按波特五力的标准含义处理。",
    "represented by 与 articulated by 的语义较抽象，按“战略定位由业务模型表示、业务模型由蓝图阐明”直译。",
    "Business Model 网格中 Customers 与图 2-4 的 Customers 是否同一概念，图中未说明。",
    "五力名称、Strategic Position 与 11 个蓝图的中文译名由解析者拟定，中文稿仅给出“业务架构蓝图”一词。"
  ],
  "analyzed_from": [
    "英文 PDF 第 18 页原图截图（fig4-1_p18_1.png）及 2×2 放大分块 z11/z21/z22",
    "英文 PDF 第 17–18 页正文与图注",
    "中文稿 G18Ae_业务模型.md 第 136–142 行",
    "figs/g18a_fig4-1.svg 源码与 SVG 文本"
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
