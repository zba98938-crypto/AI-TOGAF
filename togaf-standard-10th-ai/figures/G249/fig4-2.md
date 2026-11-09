# G249/fig4-2 · 架构层级概念的实体关系图

> 当前图示解析：[Markdown](../../architecture/diagrams/G249/fig4-2.md) · [JSON](../../architecture/diagrams/G249/fig4-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G249e.pdf`；SHA-256：`a21ad2452d4b7f77608254a7b1d0568481c52407277fd742a5430935d08271da`。

## 原图 · PDF 第 21 页

![英文原图](../assets/G249/fig4-2-p0021.png)

PDF 坐标：`[61.1, 363.7, 550.9, 617.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Enterprise Architects evolve and
‘Segment Architects evolve and
Capability (specialist) designers and
Solution Architects organize capabilities
govern aspects across and
‘govern capabilities within
build
‘feate and change capability
into new or changed solutions delivering
between segments to achieve
‘segments to achieve goals and
in building blocks to satisfy
services to meet requirements.
goals and objectives.
objectives,
requirements.
Level
1
has >
te
q
offs >
1
enables >
Service
Enterprise
Segment
Capability
Strategic
< enables
<tganized by
< utiizes
1
Le
Performed by v
1
‘System
te
a
[
Other
Biisiness,
hh
‘tlizes capabilies trom >
oe
Ist
implemented by >
1
Building Block
Domains
Domain
Domain
< implements
+
< provides, capabilities to
fo rs |
ata
Application
Technology
‘The TOGAF Standard identifies one overall business
‘The TOGAF Standard identifies three starting
domain that may be broken down further e.g. business
information system domains which may be broken down
function/process portfolios depending on what a
furthe
g.. (Technology) into Software, Servers, User
business does, e.g., Finance, Manufacturing, Legal, HR,
Devices, Execution Environments, Networks, Buildings,
Customer Management, Service, and Support.
and Mechanical Devices.
```

## 概要（历史解释；局部修正见上）

架构层级概念的 ERD：企业战略拥有分段，分段提供能力，能力使能服务；服务由系统执行，能力由构建块实现；业务域使用 IS/IT 域的能力，IS/IT 域细分为数据、应用、技术域。

## 目的（历史解释；局部修正见上）

第 4.3 节用本图说明分段架构师工作的概念结构：分段是为管理与控制而对能力做的连贯分组；域是能力的另一种有用分组。图把企业战略、分段、能力、服务、系统、构建块与业务/IS/IT 域放在同一 ERD 中，说明它们之间的组成、使能、实现与使用关系。

## 阅读顺序（历史解释；局部修正见上）

先看 Level 框内的横向链：Enterprise Strategic —has→ Segment —offers→ Capability —enables→ Service；反向读作 enables、organized by、utilizes。再看下方：Service —performed by→ System，System 内含 Building Block，Capability —implemented by→ Building Block。左侧 Business Domain 通过 utilizes capabilities from 使用 IS/IT Domain 的能力；Business Domain 下含若干 XX 子域，IS/IT Domain 下含 Data、Application、Technology 三个域。顶部四段文字分别说明企业架构师、分段架构师、能力设计/构建者、解决方案架构师的职责。

## 关键含义（历史解释；局部修正见上）

- 层级链：Enterprise Strategic 1..* has Segment 1..*；Segment 1..* offers Capability 1..*；Capability 1..* enables Service 1..*。反向标签分别为 enables、organized by、utilizes。
- Service 1..* is performed by System 1..*；System 1..* contains Building Block 1..*。
- Capability 1..* is implemented by Building Block 1..*；反向为 implements。
- Business Domain 1..* utilizes capabilities from IS/IT Domain 0..*；反向为 IS/IT Domain provides capabilities to Business Domain。
- Business Domain 下可继续分解为若干业务子域（图中用 XX、XX、.. 表示）；IS/IT Domain 下含 Data、Application、Technology 三个起始域，技术域还可继续分解为 Software、Servers、User Devices、Execution Environments、Networks、Buildings、Mechanical Devices 等。
- 顶部四段说明：企业架构师跨分段演进/治理；分段架构师在分段内演进/治理能力；能力设计/构建者创建/变更构建块中的能力；解决方案架构师把能力组织成新的/变更的解决方案以交付服务。
- 图中把 System 画成一个包含 Building Block 的大框，表示系统由构建块组成；服务由系统执行，能力由构建块实现。

## 层级（历史解释；局部修正见上）

Level 框包含 Enterprise Strategic、Segment、Capability、Service 四个层级实体；System 框包含 Building Block；Business Domain 包含 XX 子域；IS/IT Domain 包含 Data、Application、Technology。这是实体包含/分类，不是组织汇报。

## 线条含义（历史解释；局部修正见上）

连线为 ERD 关系，标签说明主语→宾语，两端数字为基数：has/enables（企业战略↔分段）、offers/organized by（分段↔能力）、enables/utilizes（能力↔服务）、performed by（服务→系统）、implemented by/implements（能力↔构建块）、utilizes capabilities from/provides capabilities to（业务域↔IS/IT 域）。System 到 Building Block 的连线表示组成；Business Domain 到 XX、IS/IT Domain 到 Data/Application/Technology 的连线表示细分。

## 易误读点（历史解释；局部修正见上）

- Level 框不是组织层级，而是架构层级概念的集合；Enterprise Strategic、Segment、Capability、Service 是概念类型，不是四个部门。
- Business Domain 与 IS/IT Domain 是并列的域，不是上下级；Business Domain 使用 IS/IT Domain 提供的能力。
- System 与 Building Block 是包含关系，不是同一个概念；服务由系统执行，能力由构建块实现。
- 顶部四段文字是角色职责说明，不是 ERD 实体或关系。
- 中文稿引用的 figs/g249_fig4-2.svg 是简单的架构层级框，没有基数与关系标签，不能据它理解 ERD。

## 元素

```json
[
  {
    "id": "level",
    "label_en": "Level",
    "label_zh": "层级",
    "type": "group",
    "parent": null,
    "position": "顶部大框"
  },
  {
    "id": "enterprise_strategic",
    "label_en": "Enterprise Strategic",
    "label_zh": "企业战略层",
    "type": "architecture",
    "parent": "level",
    "order": 1
  },
  {
    "id": "segment",
    "label_en": "Segment",
    "label_zh": "分段",
    "type": "architecture",
    "parent": "level",
    "order": 2
  },
  {
    "id": "capability",
    "label_en": "Capability",
    "label_zh": "能力",
    "type": "capability",
    "parent": "level",
    "order": 3
  },
  {
    "id": "service",
    "label_en": "Service",
    "label_zh": "服务",
    "type": "service",
    "parent": "level",
    "order": 4
  },
  {
    "id": "system",
    "label_en": "System",
    "label_zh": "系统",
    "type": "application",
    "parent": null,
    "position": "右上大框"
  },
  {
    "id": "building_block",
    "label_en": "Building Block",
    "label_zh": "构建块",
    "type": "building_block",
    "parent": "system",
    "position": "System 框内"
  },
  {
    "id": "other_domains",
    "label_en": "Other Domains",
    "label_zh": "其他域",
    "type": "group",
    "parent": null,
    "position": "左下"
  },
  {
    "id": "business_domain",
    "label_en": "Business Domain",
    "label_zh": "业务域",
    "type": "group",
    "parent": null,
    "position": "左下中"
  },
  {
    "id": "business_subdomains",
    "label_en": "XX, XX, ..",
    "label_zh": "业务子域",
    "type": "group",
    "parent": "business_domain",
    "position": "业务域下方"
  },
  {
    "id": "isit_domain",
    "label_en": "IS/IT Domain",
    "label_zh": "IS/IT 域",
    "type": "group",
    "parent": null,
    "position": "中下"
  },
  {
    "id": "data_domain",
    "label_en": "Data",
    "label_zh": "数据域",
    "type": "architecture",
    "parent": "isit_domain",
    "order": 1
  },
  {
    "id": "application_domain",
    "label_en": "Application",
    "label_zh": "应用域",
    "type": "architecture",
    "parent": "isit_domain",
    "order": 2
  },
  {
    "id": "technology_domain",
    "label_en": "Technology",
    "label_zh": "技术域",
    "type": "architecture",
    "parent": "isit_domain",
    "order": 3
  },
  {
    "id": "note_ea",
    "label_en": "Enterprise Architects evolve and govern aspects across and between segments to achieve goals and objectives.",
    "label_zh": "企业架构师跨分段演进与治理，以达成目标与目的。",
    "type": "note",
    "parent": null,
    "position": "顶部左一"
  },
  {
    "id": "note_segment",
    "label_en": "Segment Architects evolve and govern capabilities within segments to achieve goals and objectives.",
    "label_zh": "分段架构师在分段内演进与治理能力，以达成目标与目的。",
    "type": "note",
    "parent": null,
    "position": "顶部左二"
  },
  {
    "id": "note_capability",
    "label_en": "Capability (specialist) designers and builders create and change capability in building blocks to satisfy requirements.",
    "label_zh": "能力（专家）设计与构建者创建并变更构建块中的能力，以满足需求。",
    "type": "note",
    "parent": null,
    "position": "顶部右二"
  },
  {
    "id": "note_solution",
    "label_en": "Solution Architects organize capabilities into new or changed solutions delivering services to meet requirements.",
    "label_zh": "解决方案架构师把能力组织成新的/变更的解决方案，交付服务以满足需求。",
    "type": "note",
    "parent": null,
    "position": "顶部右一"
  }
]
```

## 关系

```json
[
  {
    "from": "enterprise_strategic",
    "to": "segment",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "has >",
    "label_zh": "拥有",
    "cardinality": "1..* → 1..*",
    "description_zh": "反向读作 < enables"
  },
  {
    "from": "segment",
    "to": "capability",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "offers >",
    "label_zh": "提供",
    "cardinality": "1..* → 1..*",
    "description_zh": "反向读作 < organized by"
  },
  {
    "from": "capability",
    "to": "service",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "enables >",
    "label_zh": "使能",
    "cardinality": "1..* → 1..*",
    "description_zh": "反向读作 < utilizes"
  },
  {
    "from": "service",
    "to": "system",
    "type": "realization",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "performed by v",
    "label_zh": "由……执行",
    "cardinality": "1..* → 1..*"
  },
  {
    "from": "system",
    "to": "building_block",
    "type": "composition",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "label_zh": "包含",
    "cardinality": "1..* → 1..*",
    "description_zh": "System 框内包含 Building Block；连线两端标 v/^ 与 1..*"
  },
  {
    "from": "capability",
    "to": "building_block",
    "type": "realization",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "implemented by >",
    "label_zh": "由……实现",
    "cardinality": "1..* → 1..*",
    "description_zh": "反向读作 < implements"
  },
  {
    "from": "business_domain",
    "to": "isit_domain",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "utilizes capabilities from >",
    "label_zh": "使用……的能力",
    "cardinality": "1..* → 0..*",
    "description_zh": "反向读作 < provides capabilities to"
  },
  {
    "from": "business_domain",
    "to": "business_subdomains",
    "type": "composition",
    "explicit": false,
    "line": "solid",
    "arrow": "forward",
    "label_zh": "细分为",
    "description_zh": "业务域下方画出 XX、XX、.. 子域；原图未标关系文字"
  },
  {
    "from": "isit_domain",
    "to": "data_domain",
    "type": "composition",
    "explicit": false,
    "line": "solid",
    "arrow": "forward",
    "label_zh": "细分为",
    "description_zh": "IS/IT 域下方画出 Data、Application、Technology；原图未标关系文字"
  },
  {
    "from": "isit_domain",
    "to": "application_domain",
    "type": "composition",
    "explicit": false,
    "line": "solid",
    "arrow": "forward",
    "label_zh": "细分为"
  },
  {
    "from": "isit_domain",
    "to": "technology_domain",
    "type": "composition",
    "explicit": false,
    "line": "solid",
    "arrow": "forward",
    "label_zh": "细分为"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_relations",
    "title_zh": "ERD 关系与基数（按原图转录）",
    "columns": [
      "主语",
      "关系",
      "宾语",
      "基数"
    ],
    "rows": [
      [
        "Enterprise Strategic",
        "has（反向 enables）",
        "Segment",
        "1..* → 1..*"
      ],
      [
        "Segment",
        "offers（反向 organized by）",
        "Capability",
        "1..* → 1..*"
      ],
      [
        "Capability",
        "enables（反向 utilizes）",
        "Service",
        "1..* → 1..*"
      ],
      [
        "Service",
        "performed by",
        "System",
        "1..* → 1..*"
      ],
      [
        "System",
        "contains",
        "Building Block",
        "1..* → 1..*"
      ],
      [
        "Capability",
        "implemented by（反向 implements）",
        "Building Block",
        "1..* → 1..*"
      ],
      [
        "Business Domain",
        "utilizes capabilities from（反向 provides capabilities to）",
        "IS/IT Domain",
        "1..* → 0..*"
      ]
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "矩形实体",
    "meaning_zh": "架构层级概念/域/系统/构建块",
    "explicit": false
  },
  {
    "symbol": "连线 + 1..* / 0..*",
    "meaning_zh": "实体关系及基数",
    "explicit": true
  },
  {
    "symbol": "Level 大框",
    "meaning_zh": "企业战略、分段、能力、服务四个层级概念的集合",
    "explicit": true
  },
  {
    "symbol": "顶部四段文字",
    "meaning_zh": "企业/分段/能力/解决方案架构师的职责说明",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "顶部一个 Level 大框，横向排列 Enterprise Strategic、Segment、Capability、Service；右上为 System 大框内含 Building Block；左下为 Other Domains、Business Domain（内含 XX/XX/..），中下为 IS/IT Domain（内含 Data/Application/Technology）；顶部有四个角色说明注记。"
}
```

## 相关图

```json
[
  {
    "target": "G249/fig4-1",
    "relation": "follows",
    "note_zh": "图 4-1 给出架构角色层级；本图用 ERD 说明架构层级概念与域的关系，正文随后定义分段架构师"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "Business Domain 与 Segment 之间、Other Domains 与 Business Domain 之间的连线在原图中没有清晰的关系标签；本解析未把它们列为关系，只保留有标签的关系。",
    "System–Building Block 的连线两端有 1..* 与 v/^ 记号，本解析按“系统包含构建块”记录；原图没有文字标签。",
    "顶部四段角色说明是注记，不是实体关系；本解析将其作为 note 元素并在语义中说明。",
    "中文稿引用的 SVG 与本图无关，已判 not_equivalent。"
  ],
  "analyzed_from": [
    "英文 PDF 第 21 页原图截图（600 dpi）",
    "英文 PDF 第 21 页正文",
    "中文稿 G249e_架构角色与技能.md 第 235–247 行",
    "figs/g249_fig4-2.svg 源码（确认与原图不对应）"
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
