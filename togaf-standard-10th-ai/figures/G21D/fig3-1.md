# G21D/fig3-1 · 拟议的国防与安全部门 L1–L3 要素的结构与内容概览

> 当前图示解析：[Markdown](../../architecture/diagrams/G21D/fig3-1.md) · [JSON](../../architecture/diagrams/G21D/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21De.pdf`；SHA-256：`220ead5fef846c52417b9b7a915ff4a64f327680b384c369840926b85958786a`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G21D/fig3-1-p0028.png)

PDF 坐标：`[74.0, 132.3, 538.0, 353.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
/
/
\
Defense Activi
‘Defense Readiness and
Intelligence and
)
Preparation
International Security
~ Defence Training and —
~ International Security —
Military Operations
Allocation
Assistance
Intelligence and Counter-
Threat Reduction
Defense Application
Intelligence Operations
-
~ Defense Network and —
Counter Terrorism
Special Intelligence
IT Infrastructure
-
-
Population Protection
```

## 概要（历史解释；局部修正见上）

政府参考模型中“国防与安全”部门的 L1–L3 分解：1 个部门、3 个功能、10 项服务。

## 目的（历史解释；局部修正见上）

第 3 章开篇用这张图概览“国防与安全”部门（L1）下的功能（L2）与服务（L3），随后的表 3-1 逐项给出说明。它是图 1-1 三层结构在本部门的具体展开，与其余 10 个部门图采用同一模板，附录 A 第 48 页把它与图 2-1、图 4-1 汇总在同一页。

## 阅读顺序（历史解释；局部修正见上）

最外层浅蓝色大框是 L1 部门，顶部白色粗体字是部门名称。框内三个等宽的白色圆角框是 L2 功能，从左到右依次为国防活动、国防准备与战备、情报与国际安全。每个功能框里自上而下排列的胶囊形小框是 L3 服务。图中没有连线或箭头，上下级关系完全由框的嵌套表达，同一功能内的服务是并列的。

## 关键含义（历史解释；局部修正见上）

- 本部门分为 3 个 L2 功能：国防活动（3 项服务）、国防准备与战备（4 项）、情报与国际安全（3 项），共 10 项 L3 服务。
- 按表 3-1 的功能说明：国防活动是国家防务所利用的项目，包括国防相关活动、威胁削减与反恐；国防准备与战备是部队与基础设施的维护、装备、采购与开发，以及向人员支付的薪酬与福利；情报与国际安全是保护、分析并理解政府与盟友需求与利益的活动。
- 部门定义中的“向人员支付的薪酬与福利”只出现在国防准备与战备的功能说明里，图中没有对应的 L3 服务；薪酬发放作为服务出现在共享服务部门的财务共享中心下（图 11-1）。
- 与网络和信息有关的服务：威胁削减包括数据利用、有效的信息机动与网络安全作战；国防网络与 IT 基础设施满足国防的连接与互操作需求。政府内部的信息安全与数据保护在共享服务部门的转型功能下（图 11-1）。
- 国际维度分在两个部门：情报与国际安全在本部门；外交事务与外交条约在国际事务与贸易部门（图 2-1）。
- 民众保护（确保民众、政府与领导人的安全）属于国防准备与战备；应急规划与消防服务在司法、治安与内政部门（图 7-1）。

## 层级（历史解释；局部修正见上）

三层严格树形：L1 部门“国防与安全”（最外层框）→ 3 个 L2 功能（白色圆角框）→ 10 个 L3 服务（胶囊框）。每项服务只属于一个功能，对应图 1-1 中“部门—功能—服务”的组成关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。服务框位于功能框内，表示该服务属于该功能；功能框位于部门框内，表示该功能属于本部门（图 1-1 用菱形组合线表示同样的组成关系）。元素清单用 parent/level 记录这种嵌套，因此关系清单为空。

## 易误读点（历史解释；局部修正见上）

- 部分服务的名称与表 3-1 的说明并不对应：“Military Operations（军事行动）”的说明是所有杂项国防相关活动（如国家防务之外的采购费用）；“International Security Assistance（国际安全援助）”的说明是利用跨政府 IT 基础设施、网络与信息保护政府利益并应对潜在威胁。判断服务范围时以表 3-1 的说明为准，不要只凭名称。
- 图中拼写不统一：“Defence Training and Allocation”用英式拼写，其余为“Defense”；“Counter Terrorism”在表 3-1 中写作“Counter-Terrorism”。元素按图记录。
- 同一功能内服务的上下次序不表示优先级或流程先后。
- 中文稿引用的中文化 PNG 字号混乱（“国防活动”比另两个功能标题小得多），不能用字号判断层级，应以框的嵌套为准。
- 图框下方的浅灰色线条是 PDF 评估版水印的残影，不属于图的内容。

## 元素

```json
[
  {
    "id": "l1_defense_security",
    "label_en": "Defense and Security",
    "label_zh": "国防与安全",
    "type": "other",
    "notation_type": "GRM L1 部门（Sector）",
    "parent": null,
    "level": 1,
    "position": "最外层浅蓝色框，标题在顶部居中",
    "description_zh": "GRM 第 1 层“部门”，即政府的一个业务领域；词表没有对应类型，故用 other。"
  },
  {
    "id": "l2_defense_activities",
    "label_en": "Defense Activities",
    "label_zh": "国防活动",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_defense_security",
    "level": 2,
    "order": 1,
    "position": "左",
    "description_zh": "国家防务所利用的项目，包括国防相关活动、威胁削减与反恐（表 3-1）。"
  },
  {
    "id": "l2_defense_readiness_preparation",
    "label_en": "Defense Readiness and Preparation",
    "label_zh": "国防准备与战备",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_defense_security",
    "level": 2,
    "order": 2,
    "position": "中",
    "description_zh": "部队与基础设施的维护、装备、采购与开发，以及向人员支付的薪酬与福利（表 3-1）。"
  },
  {
    "id": "l2_intelligence_international_security",
    "label_en": "Intelligence and International Security",
    "label_zh": "情报与国际安全",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_defense_security",
    "level": 2,
    "order": 3,
    "position": "右",
    "description_zh": "保护、分析并理解政府与盟友需求与利益的活动（表 3-1）。"
  },
  {
    "id": "l3_military_operations",
    "label_en": "Military Operations",
    "label_zh": "军事行动",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_activities",
    "level": 3,
    "order": 1,
    "description_zh": "表 3-1 说明为所有杂项国防相关活动（如国家防务之外的采购费用）。"
  },
  {
    "id": "l3_threat_reduction",
    "label_en": "Threat Reduction",
    "label_zh": "威胁削减",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_activities",
    "level": 3,
    "order": 2,
    "description_zh": "减少与防止与威胁相关的货物或机密数据扩散，包括数据利用、信息机动与网络安全作战。"
  },
  {
    "id": "l3_counter_terrorism",
    "label_en": "Counter Terrorism",
    "label_zh": "反恐",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_activities",
    "level": 3,
    "order": 3,
    "description_zh": "消除与威慑恐怖主义行为的国内与国际响应；表 3-1 写作 Counter-Terrorism。",
    "attributes": {
      "table_label_en": "Counter-Terrorism"
    }
  },
  {
    "id": "l3_defence_training_allocation",
    "label_en": "Defence Training and Allocation",
    "label_zh": "国防训练与分配",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_readiness_preparation",
    "level": 3,
    "order": 1,
    "description_zh": "通过真实任务与模拟训练环境提升国防领域个人与集体绩效；图中用英式拼写 Defence，表 3-1 写作 Defense。",
    "attributes": {
      "table_label_en": "Defense Training and Allocation"
    }
  },
  {
    "id": "l3_defense_application",
    "label_en": "Defense Application",
    "label_zh": "国防应用",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_readiness_preparation",
    "level": 3,
    "order": 2,
    "description_zh": "综合运用交战与机动，在所有环境中达成国防目标。"
  },
  {
    "id": "l3_defense_network_it",
    "label_en": "Defense Network and IT Infrastructure",
    "label_zh": "国防网络与 IT 基础设施",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_readiness_preparation",
    "level": 3,
    "order": 3,
    "description_zh": "为满足国防连接性与互操作需求的信息流动。"
  },
  {
    "id": "l3_population_protection",
    "label_en": "Population Protection",
    "label_zh": "民众保护",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_defense_readiness_preparation",
    "level": 3,
    "order": 4,
    "description_zh": "确保民众、政府与领导人安全并受保护。"
  },
  {
    "id": "l3_international_security_assistance",
    "label_en": "International Security Assistance",
    "label_zh": "国际安全援助",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_intelligence_international_security",
    "level": 3,
    "order": 1,
    "description_zh": "表 3-1 说明为利用跨政府 IT 基础设施、网络与信息保护政府利益并应对潜在威胁。"
  },
  {
    "id": "l3_intelligence_counter_intelligence",
    "label_en": "Intelligence and Counter-Intelligence Operations",
    "label_zh": "情报与反情报行动",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_intelligence_international_security",
    "level": 3,
    "order": 2
  },
  {
    "id": "l3_special_intelligence",
    "label_en": "Special Intelligence",
    "label_zh": "特殊情报",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_intelligence_international_security",
    "level": 3,
    "order": 3,
    "description_zh": "为支持国家利益而处理、分析、收集信息的先进服务。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色大圆角框 + 顶部白色粗体标题",
    "meaning_zh": "L1 部门（Sector）",
    "explicit": false
  },
  {
    "symbol": "白色圆角框 + 黑色粗体标题",
    "meaning_zh": "L2 功能（Function），属于所在部门",
    "explicit": false
  },
  {
    "symbol": "白色胶囊形小框（细灰边）",
    "meaning_zh": "L3 服务（Service），属于所在功能",
    "explicit": false
  },
  {
    "symbol": "框的嵌套",
    "meaning_zh": "组成/归属关系，与图 1-1 中菱形组合线表达的“部门—功能—服务”关系相同",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "最外层浅蓝色圆角框（顶部居中为部门标题，右上角为版权署名）内，三个等宽功能框从左到右并排：国防活动（3 项）、国防准备与战备（4 项）、情报与国际安全（3 项）；各框内服务自上而下单列排列。"
}
```

## 相关图

```json
[
  {
    "target": "G21D/fig1-1",
    "relation": "detail_of",
    "note_zh": "图 1-1 的三层结构（L1 部门—L2 功能—L3 服务）在“国防与安全”部门的展开"
  },
  {
    "target": "G21D/fig4-1",
    "relation": "complements",
    "note_zh": "同一模板的相邻部门概览（一般政府与地方服务）"
  },
  {
    "target": "G21D/fig11-1",
    "relation": "related",
    "note_zh": "网络安全作战与国防网络在本图，政府内部的信息安全、数据保护与薪酬发放在图 11-1 的共享服务部门"
  },
  {
    "target": "G21D/appA-p48",
    "relation": "related",
    "note_zh": "附录 A 第 48 页（PDF 第 68 页）原样收录本图，与图 2-1、图 4-1 同页"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 28 页原图截图",
    "英文 PDF 第 28–29 页正文（第 3 章开篇、表 3-1）",
    "英文 PDF 第 68 页附录 A 图示（同内容面板，用于复核标签）",
    "中文稿 G21De_政府参考模型.md 第 280–325 行",
    "figs/zh/g21de_fig3-1_zh.png（逐项对照）"
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
