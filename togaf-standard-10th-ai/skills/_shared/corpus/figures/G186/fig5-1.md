# G186/fig5-1 · TOGAF 架构存储库

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig5-1.md) · [JSON](../../architecture/diagrams/G186/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 47 页

![英文原图](../assets/G186/fig5-1-p0047.png)

PDF 坐标：`[61.1, 36.0, 550.9, 428.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Enterprise Repository
Ft
Architecture Metamodel
Architecture Repo:
Artifacts in the
landscape are
Reference
Library
structured according
Best practic
to the framework
creates
Reference
reference
models
Solutions
Architecture
itecture|
Landscape
Landscape
adopted by
External
Organization
the enterpris
Reference
Reference
Strategic
Adopted
Materials
Models
by the
Architectures
enterprise
Solution
Enables the
Building
enterprise
Segment
Standards have
Blocks
Architectures
Standards
reference
are complied
implementations
‘Standards
Capability
Architectures
Library
Standards
adopted by
Business Standards
the enterprise
External
Business.
Best
‘outcomes
practice
Data Standards
Standards
delivered
creates
standards:
Application Standards
Architecture
The landscape
Technology Standards|
ements
Req
is governed
Repository
Compliance is governed
Drivers,
for the
Governance Repository
Strategic
enter
Visibility and
Requirements
esdalation
>
Segment
Architecture
Requirements
Architecture
Board
Board steers
Architecture Capability
and manages
Capability
the capability
Requirements
```

## 概要（历史解释；局部修正见上）

TOGAF 架构存储库的分区构成，以及架构全景、参考库、标准库、治理库与外部材料、架构委员会之间的流向。

## 目的（历史解释；局部修正见上）

作者用这张总览图告诉实践者：架构存储库不是一个文件夹，而是由元模型、架构全景、解决方案全景、参考库、标准库、需求库、治理库和架构能力组成的系统；实践者日常直接打交道的是架构全景、参考库、标准库、需求库以及治理库中的合规评估。

## 阅读顺序（历史解释；局部修正见上）

从左上进入：最外层浅灰是 Enterprise Repository，里面整块灰色是 Architecture Repository。先认颜色分区：绿色=元模型与架构能力，深蓝=架构全景/解决方案全景/参考库/标准库（内容库），品红=需求库与解决方案全景，紫色=治理库，灰色=外部参考模型/外部标准/架构委员会。然后顺着带文字的箭头读：元模型如何约束全景，全景如何产生参考架构与标准，外部材料如何被采纳，治理库如何治理全景与合规，架构委员会如何与治理库互动并管理架构能力。

## 关键含义（历史解释；局部修正见上）

- 架构存储库位于更宽的企业存储库之内；企业存储库还包括外部参考模型、外部标准与架构委员会等外部要素。
- 架构元模型由 Architecture Method（架构方法）与 Enterprise Metamodel（企业元模型）组成，它规定“全景中的制品按框架结构化”。
- 架构全景分三层：战略架构、分段架构、能力架构；它通过“Enables the enterprise”使能解决方案全景及其解决方案构建块。
- 参考库存放组织参考材料，标准库存放业务/数据/应用/技术四类标准；两者都从外部参考模型/外部标准“采纳”材料。
- 全景与内容库之间是双向的：全景中的最佳实践产生参考架构与标准；参考架构与标准又被企业采纳回全景（Adopted by the enterprise / Standards are complied with）。
- 标准库与参考库之间还有一条“Standards have reference implementations”，说明标准需要参考实现来落地。
- 治理存储库（决策日志、合规评估、能力评估、日历、项目组合、绩效度量）治理架构全景；标准库则向下指向治理库，表示合规以标准为依据。
- 架构需求库与治理库之间交换“Drivers for the enterprise”，与解决方案全景之间用虚线双向箭头表示“Business outcomes delivered”。
- 架构委员会在存储库之外，与治理库之间是双向的“Visibility and escalation”，并“steers and manages the capability”指向架构能力。

## 层级（历史解释；局部修正见上）

三层包含：Enterprise Repository ⊃ Architecture Repository ⊃ 七个分区（架构元模型、架构全景、解决方案全景、参考库、标准库、架构需求库、治理存储库）+ 架构能力。每个分区内再列具体内容项（如战略/分段/能力架构，四类标准，六个治理项，三个能力项）。外部参考模型、外部标准、架构委员会不属于架构存储库，画在外侧。

## 线条含义（历史解释；局部修正见上）

共 15 条带文字的箭头：单箭头表示材料/影响的方向（如“Artifacts in the landscape are structured according to the framework”由元模型指向全景，“Enables the enterprise”由全景指向解决方案全景）；双向箭头表示持续交换（决策驱动、业务成果、可见性与上报）；虚线双向箭头只有“Business outcomes delivered”一条。被动语态的标签（The landscape is governed、Standards are complied with、Compliance is governed）要按标签读主语，箭头方向表示“受…作用”的一侧。

## 易误读点（历史解释；局部修正见上）

- 不要把 Architecture Landscape 当成整个存储库；它只是七个分区之一，且只含战略/分段/能力三层架构。
- 不要把 Solutions Landscape 与 Architecture Landscape 混为一谈：前者放解决方案构建块，后者放架构。
- “The landscape is governed”箭头由全景向下指入治理库，不要读成“全景治理治理库”；语义是全景受治理。
- 外部参考模型与外部标准画在架构存储库之外，它们不是存储库的内部库；架构委员会同样在外部。
- 治理库中的 Decision Log 与 Calendar、架构能力中的 Skills Repository 在中文 PNG 中被漏掉，不要据此认为原图没有这些项。
- 中文 PNG 把架构需求库标题误写成“架构存储库”，并把 Architecture Board 译成“架构董事会”；应以英文原图为准。
- 图中没有画 ADM 阶段或流程顺序；箭头表示材料与治理关系，不是时间顺序。

## 元素

```json
[
  {
    "id": "enterprise_repository",
    "label_en": "Enterprise Repository",
    "label_zh": "企业存储库",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "最外层浅灰大框",
    "description_zh": "比架构存储库更大的企业级存储范围。"
  },
  {
    "id": "architecture_repository",
    "label_en": "Architecture Repository",
    "label_zh": "架构存储库",
    "type": "group",
    "parent": "enterprise_repository",
    "level": 1,
    "position": "内部灰色大框",
    "description_zh": "TOGAF 架构存储库本体，包含七个分区与架构能力。"
  },
  {
    "id": "arch_metamodel",
    "label_en": "Architecture Metamodel",
    "label_zh": "架构元模型",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "顶部绿色横条",
    "description_zh": "规定全景中的制品如何按框架结构化。"
  },
  {
    "id": "arch_method",
    "label_en": "Architecture Method",
    "label_zh": "架构方法",
    "type": "artifact",
    "parent": "arch_metamodel",
    "level": 3,
    "position": "元模型左侧白框",
    "description_zh": "架构方法。"
  },
  {
    "id": "enterprise_metamodel",
    "label_en": "Enterprise Metamodel",
    "label_zh": "企业元模型",
    "type": "artifact",
    "parent": "arch_metamodel",
    "level": 3,
    "position": "元模型右侧白框",
    "description_zh": "企业元模型。"
  },
  {
    "id": "architecture_landscape",
    "label_en": "Architecture Landscape",
    "label_zh": "架构全景",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "中部深蓝框",
    "description_zh": "战略、分段、能力三层架构的容器。"
  },
  {
    "id": "strategic_architectures",
    "label_en": "Strategic Architectures",
    "label_zh": "战略架构",
    "type": "architecture",
    "parent": "architecture_landscape",
    "level": 3,
    "position": "架构全景上层",
    "description_zh": "架构全景的第一层。"
  },
  {
    "id": "segment_architectures",
    "label_en": "Segment Architectures",
    "label_zh": "分段架构",
    "type": "architecture",
    "parent": "architecture_landscape",
    "level": 3,
    "position": "架构全景中层",
    "description_zh": "架构全景的第二层。"
  },
  {
    "id": "capability_architectures",
    "label_en": "Capability Architectures",
    "label_zh": "能力架构",
    "type": "architecture",
    "parent": "architecture_landscape",
    "level": 3,
    "position": "架构全景下层",
    "description_zh": "架构全景的第三层。"
  },
  {
    "id": "solutions_landscape",
    "label_en": "Solutions Landscape",
    "label_zh": "解决方案全景",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "左侧品红框（上）",
    "description_zh": "解决方案构建块的容器。"
  },
  {
    "id": "solution_building_blocks",
    "label_en": "Solution Building Blocks",
    "label_zh": "解决方案构建块",
    "type": "building_block",
    "parent": "solutions_landscape",
    "level": 3,
    "position": "解决方案全景内部白框",
    "description_zh": "已实现的解决方案构建块。"
  },
  {
    "id": "reference_library",
    "label_en": "Reference Library",
    "label_zh": "参考库",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "右上深蓝框",
    "description_zh": "参考模型、参考架构、模式等加速器材料。"
  },
  {
    "id": "organization_reference_materials",
    "label_en": "Organization Reference Materials",
    "label_zh": "组织参考材料",
    "type": "artifact",
    "parent": "reference_library",
    "level": 3,
    "position": "参考库内部白框",
    "description_zh": "组织可用的参考材料。"
  },
  {
    "id": "standards_library",
    "label_en": "Standards Library",
    "label_zh": "标准库",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "右侧中部深蓝框",
    "description_zh": "四类标准的容器。"
  },
  {
    "id": "business_standards",
    "label_en": "Business Standards",
    "label_zh": "业务标准",
    "type": "principle",
    "parent": "standards_library",
    "level": 3,
    "order": 1,
    "position": "标准库第一行",
    "description_zh": "业务标准。"
  },
  {
    "id": "data_standards",
    "label_en": "Data Standards",
    "label_zh": "数据标准",
    "type": "principle",
    "parent": "standards_library",
    "level": 3,
    "order": 2,
    "position": "标准库第二行",
    "description_zh": "数据标准。"
  },
  {
    "id": "application_standards",
    "label_en": "Application Standards",
    "label_zh": "应用标准",
    "type": "principle",
    "parent": "standards_library",
    "level": 3,
    "order": 3,
    "position": "标准库第三行",
    "description_zh": "应用标准。"
  },
  {
    "id": "technology_standards",
    "label_en": "Technology Standards",
    "label_zh": "技术标准",
    "type": "principle",
    "parent": "standards_library",
    "level": 3,
    "order": 4,
    "position": "标准库第四行",
    "description_zh": "技术标准。"
  },
  {
    "id": "architecture_requirements_repository",
    "label_en": "Architecture Requirements Repository",
    "label_zh": "架构需求库",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "左下品红框",
    "description_zh": "战略/分段/能力需求的容器。"
  },
  {
    "id": "strategic_requirements",
    "label_en": "Strategic Requirements",
    "label_zh": "战略需求",
    "type": "requirement",
    "parent": "architecture_requirements_repository",
    "level": 3,
    "order": 1,
    "position": "需求库第一行",
    "description_zh": "战略层需求。"
  },
  {
    "id": "segment_requirements",
    "label_en": "Segment Requirements",
    "label_zh": "分段需求",
    "type": "requirement",
    "parent": "architecture_requirements_repository",
    "level": 3,
    "order": 2,
    "position": "需求库第二行",
    "description_zh": "分段层需求。"
  },
  {
    "id": "capability_requirements",
    "label_en": "Capability Requirements",
    "label_zh": "能力需求",
    "type": "requirement",
    "parent": "architecture_requirements_repository",
    "level": 3,
    "order": 3,
    "position": "需求库第三行",
    "description_zh": "能力层需求。"
  },
  {
    "id": "governance_repository",
    "label_en": "Governance Repository",
    "label_zh": "治理存储库",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "中下紫色框",
    "description_zh": "决策、合规、能力、日历、组合与绩效记录的容器。"
  },
  {
    "id": "decision_log",
    "label_en": "Decision Log",
    "label_zh": "决策日志",
    "type": "artifact",
    "parent": "governance_repository",
    "level": 3,
    "order": 1,
    "position": "治理库左上",
    "description_zh": "记录决策。"
  },
  {
    "id": "compliance_assessments",
    "label_en": "Compliance Assessments",
    "label_zh": "合规评估",
    "type": "artifact",
    "parent": "governance_repository",
    "level": 3,
    "order": 2,
    "position": "治理库中上",
    "description_zh": "合规性评估记录。"
  },
  {
    "id": "capability_assessments",
    "label_en": "Capability Assessments",
    "label_zh": "能力评估",
    "type": "artifact",
    "parent": "governance_repository",
    "level": 3,
    "order": 3,
    "position": "治理库右上",
    "description_zh": "能力评估记录。"
  },
  {
    "id": "calendar",
    "label_en": "Calendar",
    "label_zh": "日历",
    "type": "artifact",
    "parent": "governance_repository",
    "level": 3,
    "order": 4,
    "position": "治理库左下",
    "description_zh": "治理日程。"
  },
  {
    "id": "project_portfolio",
    "label_en": "Project Portfolio",
    "label_zh": "项目组合",
    "type": "artifact",
    "parent": "governance_repository",
    "level": 3,
    "order": 5,
    "position": "治理库中下",
    "description_zh": "项目组合记录。"
  },
  {
    "id": "performance_measurement",
    "label_en": "Performance Measurement",
    "label_zh": "绩效度量",
    "type": "metric",
    "parent": "governance_repository",
    "level": 3,
    "order": 6,
    "position": "治理库右下",
    "description_zh": "绩效度量。"
  },
  {
    "id": "architecture_capability",
    "label_en": "Architecture Capability",
    "label_zh": "架构能力",
    "type": "group",
    "parent": "architecture_repository",
    "level": 2,
    "position": "底部绿色横条",
    "description_zh": "支撑架构工作的组织能力。"
  },
  {
    "id": "skills_repository",
    "label_en": "Skills Repository",
    "label_zh": "技能库",
    "type": "artifact",
    "parent": "architecture_capability",
    "level": 3,
    "order": 1,
    "position": "架构能力左格",
    "description_zh": "架构技能目录。"
  },
  {
    "id": "organization_structure",
    "label_en": "Organization Structure",
    "label_zh": "组织架构",
    "type": "organization_unit",
    "parent": "architecture_capability",
    "level": 3,
    "order": 2,
    "position": "架构能力中格",
    "description_zh": "架构团队的组织结构。"
  },
  {
    "id": "architecture_charter",
    "label_en": "Architecture Charter",
    "label_zh": "架构章程",
    "type": "artifact",
    "parent": "architecture_capability",
    "level": 3,
    "order": 3,
    "position": "架构能力右格",
    "description_zh": "架构能力的授权章程。"
  },
  {
    "id": "external_reference_models",
    "label_en": "External Reference Models",
    "label_zh": "外部参考模型",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "存储库外右侧上部",
    "description_zh": "来自企业外部的参考模型。"
  },
  {
    "id": "external_standards",
    "label_en": "External Standards",
    "label_zh": "外部标准",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "存储库外右侧中部",
    "description_zh": "来自企业外部的标准。"
  },
  {
    "id": "architecture_board",
    "label_en": "Architecture Board",
    "label_zh": "架构委员会",
    "type": "organization_unit",
    "parent": null,
    "level": 2,
    "position": "存储库外右侧下部",
    "description_zh": "治理架构工作的委员会，不属于架构存储库。"
  }
]
```

## 关系

```json
[
  {
    "from": "arch_metamodel",
    "to": "architecture_landscape",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Artifacts in the landscape are structured according to the framework",
    "label_zh": "全景中的制品按框架结构化",
    "description_zh": "从架构元模型底部向下的箭头，指入架构全景顶部。"
  },
  {
    "from": "architecture_landscape",
    "to": "reference_library",
    "type": "produces",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Best practice creates reference architecture",
    "label_zh": "最佳实践创建参考架构",
    "description_zh": "由架构全景右侧指向参考库左侧。"
  },
  {
    "from": "reference_library",
    "to": "architecture_landscape",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Adopted by the enterprise",
    "label_zh": "被企业采纳",
    "description_zh": "参考库左侧指向架构全景右侧，与上一条方向相反，形成循环。"
  },
  {
    "from": "architecture_landscape",
    "to": "solutions_landscape",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Enables the enterprise",
    "label_zh": "使能企业",
    "description_zh": "由架构全景左侧指向解决方案全景右侧。"
  },
  {
    "from": "architecture_landscape",
    "to": "standards_library",
    "type": "produces",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Best practice creates standards",
    "label_zh": "最佳实践创建标准",
    "description_zh": "由架构全景右下指向标准库左侧。"
  },
  {
    "from": "standards_library",
    "to": "architecture_landscape",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Standards are complied with",
    "label_zh": "标准得到遵循",
    "description_zh": "由标准库左侧指向架构全景右下。"
  },
  {
    "from": "standards_library",
    "to": "reference_library",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Standards have reference implementations",
    "label_zh": "标准有参考实现",
    "description_zh": "由标准库顶部向上的箭头指入参考库底部。"
  },
  {
    "from": "external_reference_models",
    "to": "reference_library",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Reference models adopted by the enterprise",
    "label_zh": "参考模型被企业采纳",
    "description_zh": "由外部参考模型左侧指向参考库右侧。"
  },
  {
    "from": "external_standards",
    "to": "standards_library",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Standards adopted by the enterprise",
    "label_zh": "标准被企业采纳",
    "description_zh": "由外部标准左侧发出的多条细线，分别指向业务/数据/应用/技术标准四行；主箭头落在标准库右侧。"
  },
  {
    "from": "architecture_landscape",
    "to": "governance_repository",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "The landscape is governed",
    "label_zh": "架构全景受治理",
    "description_zh": "由架构全景底部向下指入治理存储库顶部；被动语态表示全景受治理库治理。"
  },
  {
    "from": "standards_library",
    "to": "governance_repository",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Compliance is governed",
    "label_zh": "合规受治理",
    "description_zh": "由标准库底部向下指入治理存储库的合规评估区域。"
  },
  {
    "from": "governance_repository",
    "to": "architecture_requirements_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "label_en": "Drivers for the enterprise",
    "label_zh": "企业驱动因素",
    "description_zh": "治理存储库与架构需求库之间的水平双向箭头，箭头在需求库右侧与治理库左侧各一个。"
  },
  {
    "from": "solutions_landscape",
    "to": "architecture_requirements_repository",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "both",
    "label_en": "Business outcomes delivered",
    "label_zh": "业务成果交付",
    "description_zh": "解决方案全景底部与需求库顶部之间的竖直虚线双向箭头。"
  },
  {
    "from": "governance_repository",
    "to": "architecture_board",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "label_en": "Visibility and escalation",
    "label_zh": "可见性与上报",
    "description_zh": "治理库右侧（能力评估一行）与架构委员会左侧之间的水平双向箭头。"
  },
  {
    "from": "architecture_board",
    "to": "architecture_capability",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Architecture Board steers and manages the capability",
    "label_zh": "架构委员会引领并管理架构能力",
    "description_zh": "由架构委员会左侧指向架构能力右端（架构章程一行）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色分区",
    "meaning_zh": "元模型（架构方法/企业元模型）与架构能力（技能库/组织架构/架构章程）",
    "explicit": false
  },
  {
    "symbol": "深蓝色分区",
    "meaning_zh": "内容库：架构全景、解决方案全景、参考库、标准库",
    "explicit": false
  },
  {
    "symbol": "品红色分区",
    "meaning_zh": "架构需求库与解决方案全景（原图用同色系）",
    "explicit": false
  },
  {
    "symbol": "紫色分区",
    "meaning_zh": "治理存储库",
    "explicit": false
  },
  {
    "symbol": "灰色外部块",
    "meaning_zh": "不属于架构存储库的外部要素：外部参考模型、外部标准、架构委员会",
    "explicit": false
  },
  {
    "symbol": "带文字的箭头",
    "meaning_zh": "材料流向、采纳、治理或双向交换；文字说明关系性质",
    "explicit": false
  },
  {
    "symbol": "虚线双向箭头",
    "meaning_zh": "业务成果在解决方案全景与需求库之间持续交付",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "大矩形套小矩形：外层浅灰 Enterprise Repository，内层灰色 Architecture Repository。内部左列自上而下为解决方案全景、架构需求库；中列为架构全景（三层堆叠）；右上为参考库、标准库；中下为治理存储库与架构能力；顶部为架构元模型。右侧外挂三个灰色块：外部参考模型、外部标准、架构委员会。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "外部标准到标准库的多条细线在低分辨率下难以逐条确认终点；按“分别指向四类标准”记录为一条关系。",
    "“Compliance is governed”箭头从标准库底部指向治理库顶部，具体落在合规评估一行还是治理库整体，图上无法精确判断。",
    "“The landscape is governed”的箭头由全景向下指入治理库，但标签是被动语态；本分析按“全景受治理”记录为依赖关系。",
    "原图没有图例，颜色分组（绿/蓝/品红/紫/灰）是解析者据色块与文字推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 47 页图 5-1 截图（220 dpi）及 3×3 放大分块、右侧局部 3 倍放大",
    "英文 PDF 第 46–47 页正文",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 479–528 行及标签对照表 L489–L524",
    "figs/g186e_fig5-1_en.png 与 figs/zh/g186e_fig5-1_zh.png"
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
