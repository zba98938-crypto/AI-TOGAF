# G249/fig4-1 · 架构角色及其关系

> 当前图示解析：[Markdown](../../architecture/diagrams/G249/fig4-1.md) · [JSON](../../architecture/diagrams/G249/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G249e.pdf`；SHA-256：`a21ad2452d4b7f77608254a7b1d0568481c52407277fd742a5430935d08271da`。

## 原图 · PDF 第 16 页

![英文原图](../assets/G249/fig4-1-p0016.png)

PDF 坐标：`[61.1, 444.8, 550.9, 719.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Strategy (goals and objectives) -
Chief Architect
> Executing and evolving +
as
services and systems delivering
operational
ellence and strategic
Provides context, leadership and oversight of the
‘alignment
capabilites and solution components in the architecture landscape
Data, Application,
Business
Enterprise Architect
Domain
Technology Domain
Provides leadership and governance
‘across multiple domains and situations
¥
4
Data, Application,
Business Specialists
———|
Segment Architect
Provides leadership
Provides leadership
Technology Specialists
‘and governance for,
‘and governance for
‘and situations
specific domains
Provides context,
specific domains
‘and situations
leadership,
|
and oversight
|
Receive potential
|
+ Receive requirements|
‘and constraints «
Business Users and
IS/IT Users and
Stakeholders
= Provide
Solution Architect
Stakeholders
Provide specifications
specifications and
govern the delivery of
(of solutions +
‘and govem the delivery|
solutions
a
working systems, sub-systems, and components —+
‘= Deliver actors, working systems, sub-systems, and components
1g solu
```

## 概要（历史解释；局部修正见上）

架构角色从首席架构师经企业、分段到解决方案架构师逐级细化，并与专业领域角色、用户和利益相关者双向交换需求与规格。

## 目的（历史解释；局部修正见上）

第 4 章用本图给出企业架构实践中的示例角色及其关系：首席架构师是企业架构师的特例，负责把架构视图整合进企业战略与运营语境；企业、分段、解决方案架构师逐级增加对架构全景特定要素的理解、领导与治理细节；专业角色与用户在两侧提供细节知识、需求和交付治理。

## 阅读顺序（历史解释；局部修正见上）

先看中央纵向链：Chief Architect → Enterprise Architect → Segment Architect → Solution Architect，箭头旁的紫字说明每一级提供的上下文、领导与治理范围。再看左右两侧：Business Specialists 与 Data, Application, Technology Specialists 位于两个灰色 Domain 框内；Business Users and Stakeholders、IS/IT Users and Stakeholders 在最外侧。纵向双箭头表示用户向专家提供需求、专家向用户提供规格与交付治理；Solution Architect 通过横向双箭头与两侧用户互动，并向下交付解决方案。

## 关键含义（历史解释；局部修正见上）

- 中央四级：首席架构师（企业架构师的特例）→ 企业架构师 → 分段架构师 → 解决方案架构师；向下对架构全景中特定要素的理解、领导与治理细节逐级增加。
- 首席架构师负责把企业架构视图整合进企业更广泛的战略与运营语境，向企业架构师提供架构全景能力与解决方案组件的上下文、领导与监督。
- 企业架构师跨越多个域和情境提供领导与治理；分段架构师对特定业务/技术域和情境提供领导与治理；解决方案架构师对具体解决方案提供上下文、领导与监督。
- Business Specialists 与 Data, Application, Technology Specialists 分别位于 Business Domain 和 Data, Application, Technology Domain 灰色范围内，接受分段架构师的领导。
- 用户/利益相关者与专家之间是双向关系：用户提供需求，专家提供规格并治理解决方案的交付；Solution Architect 同样从两侧接收需求/约束并给出规格与交付治理。
- 底部注记说明最终交付的是 actor(s)、工作系统、子系统与组件，以及可工作的解决方案；这些交付物由解决方案架构师及两侧角色共同产出。

## 层级（历史解释；局部修正见上）

纵向五级角色链：Chief Architect（最上）→ Enterprise Architect → Segment Architect → Solution Architect；两侧的 Business/Data-Application-Technology Specialists 位于 Domain 大框内，Users and Stakeholders 位于最外侧。Domain 大框是范围，不是汇报层级。

## 线条含义（历史解释；局部修正见上）

纵向实线箭头：上级向下级提供上下文、领导与治理/监督。横向与纵向双箭头：两侧角色之间的需求—规格—交付治理互动；标签说明方向（如 Business Users 向专家提供需求，专家向用户提供规格并治理交付）。底部虚线/箭头是交付物注记，不是角色间连线。

## 易误读点（历史解释；局部修正见上）

- Chief Architect 不是与 Enterprise Architect 并列的另一个层级，而是企业架构师的特例，位于最高层。
- Business/Data, Application, Technology Specialists 不是架构师的上级；他们接受 Segment Architect 的领导，补充细节知识与专长。
- Users and Stakeholders 不是被动接收方：他们提供需求，并对解决方案的交付进行治理。
- 灰色 Business Domain / Data, Application, Technology Domain 是范围框，不是组织部门；专家位于其中表示其专业领域。
- 中文稿引用的 figs/g249_fig4-1.svg 只画了四个架构角色和两个泛化框，缺少原图的全部关系与标签，不能据它理解角色互动。

## 元素

```json
[
  {
    "id": "strategy",
    "label_en": "Strategy (goals and objectives)",
    "label_zh": "战略（目标与目的）",
    "type": "note",
    "parent": null,
    "position": "左上"
  },
  {
    "id": "chief_arch",
    "label_en": "Chief Architect",
    "label_zh": "首席架构师",
    "type": "role",
    "parent": null,
    "position": "中央最上"
  },
  {
    "id": "enterprise_arch",
    "label_en": "Enterprise Architect",
    "label_zh": "企业架构师",
    "type": "role",
    "parent": null,
    "position": "中央第二级"
  },
  {
    "id": "segment_arch",
    "label_en": "Segment Architect",
    "label_zh": "分段架构师",
    "type": "role",
    "parent": null,
    "position": "中央第三级"
  },
  {
    "id": "solution_arch",
    "label_en": "Solution Architect",
    "label_zh": "解决方案架构师",
    "type": "role",
    "parent": null,
    "position": "中央第四级"
  },
  {
    "id": "business_domain",
    "label_en": "Business Domain",
    "label_zh": "业务域",
    "type": "group",
    "parent": null,
    "position": "左侧灰色大框"
  },
  {
    "id": "tech_domain",
    "label_en": "Data, Application, Technology Domain",
    "label_zh": "数据、应用、技术域",
    "type": "group",
    "parent": null,
    "position": "右侧灰色大框"
  },
  {
    "id": "business_specialists",
    "label_en": "Business Specialists",
    "label_zh": "业务专家",
    "type": "role",
    "parent": "business_domain",
    "position": "业务域内左侧"
  },
  {
    "id": "tech_specialists",
    "label_en": "Data, Application, Technology Specialists",
    "label_zh": "数据、应用、技术专家",
    "type": "role",
    "parent": "tech_domain",
    "position": "技术域内右侧"
  },
  {
    "id": "business_users",
    "label_en": "Business Users and Stakeholders",
    "label_zh": "业务用户与利益相关者",
    "type": "stakeholder",
    "parent": null,
    "position": "左下"
  },
  {
    "id": "isit_users",
    "label_en": "IS/IT Users and Stakeholders",
    "label_zh": "IS/IT 用户与利益相关者",
    "type": "stakeholder",
    "parent": null,
    "position": "右下"
  },
  {
    "id": "deliverables",
    "label_en": "Deliver working solutions / Deliver actors, working systems, sub-systems, and components",
    "label_zh": "交付物：可工作的解决方案；参与者、工作系统、子系统与组件",
    "type": "note",
    "parent": null,
    "position": "底部注记"
  }
]
```

## 关系

```json
[
  {
    "from": "strategy",
    "to": "chief_arch",
    "type": "influence",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "战略目标与目的构成首席架构师的语境"
  },
  {
    "from": "chief_arch",
    "to": "enterprise_arch",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provides context, leadership, and oversight of the capabilities and solution components in the architecture landscape",
    "label_zh": "提供架构全景能力与解决方案组件的上下文、领导与监督"
  },
  {
    "from": "enterprise_arch",
    "to": "segment_arch",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provides leadership and governance across multiple domains and situations",
    "label_zh": "跨多个域和情境提供领导与治理"
  },
  {
    "from": "segment_arch",
    "to": "business_specialists",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provides leadership and governance for specific domains and situations",
    "label_zh": "为特定域和情境提供领导与治理"
  },
  {
    "from": "segment_arch",
    "to": "tech_specialists",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provides leadership and governance for specific domains and situations",
    "label_zh": "为特定域和情境提供领导与治理"
  },
  {
    "from": "segment_arch",
    "to": "solution_arch",
    "type": "governs",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provides context, leadership, and oversight",
    "label_zh": "提供上下文、领导与监督"
  },
  {
    "from": "business_users",
    "to": "business_specialists",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Receive requirements",
    "label_zh": "接收需求"
  },
  {
    "from": "business_specialists",
    "to": "business_users",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provide specifications and govern the delivery of solutions",
    "label_zh": "提供规格并治理解决方案交付"
  },
  {
    "from": "isit_users",
    "to": "tech_specialists",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Receive requirements",
    "label_zh": "接收需求"
  },
  {
    "from": "tech_specialists",
    "to": "isit_users",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provide specifications and govern the delivery of solutions",
    "label_zh": "提供规格并治理解决方案交付"
  },
  {
    "from": "business_users",
    "to": "solution_arch",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Receive requirements",
    "label_zh": "接收需求"
  },
  {
    "from": "solution_arch",
    "to": "business_users",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provide specifications and govern the delivery of solutions",
    "label_zh": "提供规格并治理解决方案交付"
  },
  {
    "from": "solution_arch",
    "to": "isit_users",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Receive potential solutions and constraints",
    "label_zh": "接收潜在解决方案与约束"
  },
  {
    "from": "isit_users",
    "to": "solution_arch",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Provide specifications and govern the delivery of solutions",
    "label_zh": "提供规格并治理解决方案交付"
  },
  {
    "from": "solution_arch",
    "to": "deliverables",
    "type": "produces",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "向底部交付物注记输出解决方案、工作系统、子系统与组件"
  }
]
```

## 图例

```json
[
  {
    "symbol": "方框",
    "meaning_zh": "架构角色或专业/用户角色",
    "explicit": false
  },
  {
    "symbol": "纵向实线箭头",
    "meaning_zh": "上级向下级提供上下文、领导与治理/监督",
    "explicit": true
  },
  {
    "symbol": "双向箭头",
    "meaning_zh": "需求、规格与交付治理的双向互动",
    "explicit": true
  },
  {
    "symbol": "灰色大框",
    "meaning_zh": "业务域 / 数据、应用、技术域的范围",
    "explicit": false
  },
  {
    "symbol": "Strategy（goals and objectives）",
    "meaning_zh": "企业战略与目标，作为首席架构师的语境",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "中央纵向四级角色链；左右各有一个灰色 Domain 大框（Business Domain 在左，Data, Application, Technology Domain 在右），框内是专家角色；最外侧左右为 Business Users and Stakeholders 与 IS/IT Users and Stakeholders；顶部左侧是 Strategy 注记，底部是交付物注记。"
}
```

## 相关图

```json
[
  {
    "target": "G249/fig4-2",
    "relation": "precedes",
    "note_zh": "本图给出角色层级；图 4-2 用 ERD 说明架构层级中的企业、分段、能力、服务、系统、构建块与域概念"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "双向箭头上的需求/规格标签未逐一标出箭头头部；本解析按文字位置与正文语义分配方向（用户给需求，专家/架构师给规格与治理）。",
    "底部交付物注记是说明文字而非角色框，本解析将其作为 note 元素并记一条 produces 关系。"
  ],
  "analyzed_from": [
    "英文 PDF 第 16 页原图截图（600 dpi）",
    "英文 PDF 第 16 页正文",
    "中文稿 G249e_架构角色与技能.md 第 151–173 行",
    "figs/g249_fig4-1.svg 源码（确认与原图不对应）"
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
