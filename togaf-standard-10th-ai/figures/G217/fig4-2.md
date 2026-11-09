# G217/fig4-2 · 企业架构服务到 DPBoK 标准涌现模型的映射

> 当前图示解析：[Markdown](../../architecture/diagrams/G217/fig4-2.md) · [JSON](../../architecture/diagrams/G217/fig4-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G217e.pdf`；SHA-256：`ad38b0c9563a3558532e7ffd7f4e84e0ab82d29fc86f53bc08d583b604738488`。

## 原图 · PDF 第 50 页

![英文原图](../assets/G217/fig4-2-p0050.png)

PDF 坐标：`[48.2, 36.0, 563.8, 360.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
g
€
3
3
8g
sg
£
2
=
=
£
2
|Context I: In
jual/Founder
|Context Il: Team
|Context Ill: Team of Teams
|Context I'
: Enduring Enterprise
maRSSEEE SES SEE
```

## 概要（历史解释；局部修正见上）

按四个 DPBoK 语境列出应交付的企业架构服务，形成一张服务清单矩阵。

## 目的（历史解释；局部修正见上）

汇总每个语境中应考虑的企业架构服务，以交付企业架构能力；它是 4.4 节各语境服务说明的总览，也支撑“EA 以服务方式按需交付、并按语境运营节奏及时提供”的论点。

## 阅读顺序（历史解释；局部修正见上）

按行读：Context I 个人/创始人 → II 团队 → III 团队之团队 → IV 持久企业，组织规模递增。按列读：24 列中 6 个加粗竖排标题是服务分类带（本身不带 ×），其右侧的普通列才是具体服务；绿色格中的 × 表示该服务在该语境应被考虑。

## 关键含义（历史解释；局部修正见上）

- 24 列由 6 个加粗分类带（需求获取与理解、架构规划、设计支持、开发支持、企业支持、EA 实践发展支持）和 18 项具体服务组成；分类带列不带 ×。
- 语境 I 只考虑 5 项服务：利益相关者管理、业务价值评估与分析、架构与标准指导、风险管理、可持续性管理支持。
- 语境 II 增加到 6 项，唯一新增的是变更管理。
- 语境 III 跃升到 14 项，新增架构项目规划、架构裁剪、愿景与战略、建模与文档、集成、发布支持、组合管理、企业分析与评估。
- 语境 IV 覆盖全部 18 项，新增架构合规开发、合规评估与分析、能力规划、EA 开发过程改进。
- 每项服务的 × 都是从某一语境起连续到语境 IV，说明服务组合是累积的：一旦引入，后续语境继续保留。
- “EA 实践发展支持服务”分类下的“企业架构开发过程改进服务”只在语境 IV 出现；分类本身没有 ×，不能把分类列当作服务。
- 正文提醒：这些是“应考虑”的服务，提供方需按语境和运营节奏裁剪交付，并不意味着每个语境都要全量服务。

## 层级（历史解释；局部修正见上）

列方向两层：6 个服务分类（加粗带）> 18 项具体服务；行方向一层：4 个 DPBoK 语境。分类带只做视觉分组，不是可映射的服务。

## 线条含义（历史解释；局部修正见上）

图中没有连线。绿色底 + × 是唯一的数据编码；竖线与加粗列边界只是表格网格和分类带分隔，不表示流程或依赖。

## 易误读点（历史解释；局部修正见上）

- 6 个加粗列是分类标题，不是“整个分类都适用”的服务列，分类列内没有 ×。
- × 表示“应考虑/建议使用”，不是强制实施；空白不表示禁止。
- 四个语境不是互斥的组织类型，而是涌现层级；服务在语境间累积，不是在语境间迁移。
- 行序是 I→IV（自上而下变大），与图 4-3 的 IV→I 相反，不能把两张图的行序混用。
- 中文稿引用的 g217e_fig4-2_zh.png 表头被截断、绿色格错位，不能据它读出服务名、分类或映射。

## 元素

```json
[
  {
    "id": "ctx_i",
    "label_en": "Context I: Individual/Founder",
    "label_zh": "语境 I：个人/创始人",
    "type": "phase",
    "parent": null,
    "order": 1,
    "level": 1,
    "position": "第 1 行"
  },
  {
    "id": "ctx_ii",
    "label_en": "Context II: Team",
    "label_zh": "语境 II：团队",
    "type": "phase",
    "parent": null,
    "order": 2,
    "level": 1,
    "position": "第 2 行"
  },
  {
    "id": "ctx_iii",
    "label_en": "Context III: Team of Teams",
    "label_zh": "语境 III：团队之团队",
    "type": "phase",
    "parent": null,
    "order": 3,
    "level": 1,
    "position": "第 3 行"
  },
  {
    "id": "ctx_iv",
    "label_en": "Context IV: Enduring Enterprise",
    "label_zh": "语境 IV：持久企业",
    "type": "phase",
    "parent": null,
    "order": 4,
    "level": 1,
    "position": "第 4 行"
  },
  {
    "id": "cat_req",
    "label_en": "Requirements Elicitation and Understanding Services",
    "label_zh": "需求获取与理解服务",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 1 列（分类带）"
  },
  {
    "id": "svc_stakeholders",
    "label_en": "Stakeholders Management Services",
    "label_zh": "利益相关者管理服务",
    "type": "service",
    "parent": "cat_req",
    "level": 2,
    "position": "第 2 列",
    "description_zh": "四个语境全部适用。"
  },
  {
    "id": "svc_business_value",
    "label_en": "Business Value Assessment and Analysis Service",
    "label_zh": "业务价值评估与分析服务",
    "type": "service",
    "parent": "cat_req",
    "level": 2,
    "position": "第 3 列",
    "description_zh": "四个语境全部适用。"
  },
  {
    "id": "cat_arch_plan",
    "label_en": "Architecture Planning Services",
    "label_zh": "架构规划服务",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 4 列（分类带）"
  },
  {
    "id": "svc_arch_project_planning",
    "label_en": "Architecture Project Planning Services",
    "label_zh": "架构项目规划服务",
    "type": "service",
    "parent": "cat_arch_plan",
    "level": 2,
    "position": "第 5 列"
  },
  {
    "id": "svc_arch_tailoring",
    "label_en": "Architecting Tailoring Services",
    "label_zh": "架构裁剪服务",
    "type": "service",
    "parent": "cat_arch_plan",
    "level": 2,
    "position": "第 6 列"
  },
  {
    "id": "cat_design",
    "label_en": "Design Support Services",
    "label_zh": "设计支持服务",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 7 列（分类带）"
  },
  {
    "id": "svc_vision",
    "label_en": "Architecture Vision and Strategy Definition Services",
    "label_zh": "架构愿景与战略服务",
    "type": "service",
    "parent": "cat_design",
    "level": 2,
    "position": "第 8 列"
  },
  {
    "id": "svc_modeling",
    "label_en": "Architecture Modeling and Documentation Services (MVA)",
    "label_zh": "架构建模与文档服务（MVA）",
    "type": "service",
    "parent": "cat_design",
    "level": 2,
    "position": "第 9 列"
  },
  {
    "id": "svc_integration",
    "label_en": "Architecture Integration Services",
    "label_zh": "架构集成服务",
    "type": "service",
    "parent": "cat_design",
    "level": 2,
    "position": "第 10 列"
  },
  {
    "id": "svc_compliance_dev",
    "label_en": "Architecture Compliance Dev. Services (Bus, Info, Appl, Infra, Systs, ...)",
    "label_zh": "架构合规开发服务（业务、信息、应用、基础设施、系统等）",
    "type": "service",
    "parent": "cat_design",
    "level": 2,
    "position": "第 11 列",
    "description_zh": "只在语境 IV 出现。"
  },
  {
    "id": "cat_dev",
    "label_en": "Development Support Services",
    "label_zh": "开发支持服务",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 12 列（分类带）"
  },
  {
    "id": "svc_standards",
    "label_en": "Architecture and Standards Guidance Service",
    "label_zh": "架构与标准指导服务",
    "type": "service",
    "parent": "cat_dev",
    "level": 2,
    "position": "第 13 列",
    "description_zh": "四个语境全部适用，是语境 I/II 中唯一的开发支持类服务。"
  },
  {
    "id": "svc_compliance_assessment",
    "label_en": "Compliance Assessment and Analysis Service",
    "label_zh": "合规评估与分析服务",
    "type": "service",
    "parent": "cat_dev",
    "level": 2,
    "position": "第 14 列",
    "description_zh": "只在语境 IV 出现。"
  },
  {
    "id": "svc_change",
    "label_en": "Change Management Services",
    "label_zh": "变更管理",
    "type": "service",
    "parent": "cat_dev",
    "level": 2,
    "position": "第 15 列",
    "description_zh": "从语境 II 开始适用。"
  },
  {
    "id": "svc_release",
    "label_en": "Release Support Services",
    "label_zh": "发布支持服务",
    "type": "service",
    "parent": "cat_dev",
    "level": 2,
    "position": "第 16 列"
  },
  {
    "id": "cat_enterprise",
    "label_en": "Enterprise Support Services",
    "label_zh": "企业支持服务",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 17 列（分类带）"
  },
  {
    "id": "svc_portfolio",
    "label_en": "Portfolio Management Support Services (inc. Asset Mgmt, Acquisitions)",
    "label_zh": "组合管理支持服务（含资产管理、收购）",
    "type": "service",
    "parent": "cat_enterprise",
    "level": 2,
    "position": "第 18 列"
  },
  {
    "id": "svc_risk",
    "label_en": "Risk Management Services",
    "label_zh": "风险管理服务",
    "type": "service",
    "parent": "cat_enterprise",
    "level": 2,
    "position": "第 19 列",
    "description_zh": "四个语境全部适用。"
  },
  {
    "id": "svc_sustainability",
    "label_en": "Sustainability Management Support Services",
    "label_zh": "可持续性管理支持服务",
    "type": "service",
    "parent": "cat_enterprise",
    "level": 2,
    "position": "第 20 列",
    "description_zh": "四个语境全部适用。"
  },
  {
    "id": "svc_enterprise_analysis",
    "label_en": "Enterprise Analysis and Assessment Services",
    "label_zh": "企业分析与评估服务",
    "type": "service",
    "parent": "cat_enterprise",
    "level": 2,
    "position": "第 21 列"
  },
  {
    "id": "svc_capability",
    "label_en": "Capability Planning Support Service",
    "label_zh": "能力规划支持服务",
    "type": "service",
    "parent": "cat_enterprise",
    "level": 2,
    "position": "第 22 列",
    "description_zh": "只在语境 IV 出现。"
  },
  {
    "id": "cat_practice",
    "label_en": "Enterprise Architecture Practice Development Support Services",
    "label_zh": "企业架构实践发展支持服务",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "第 23 列（分类带）"
  },
  {
    "id": "svc_process_improvement",
    "label_en": "Enterprise Architecture Development Process Improvement Service",
    "label_zh": "企业架构开发过程改进服务",
    "type": "service",
    "parent": "cat_practice",
    "level": 2,
    "position": "第 24 列",
    "description_zh": "只在语境 IV 出现；其所属分类带本身没有 ×。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_services",
    "title_zh": "企业架构服务 × DPBoK 语境映射（按原图逐列转录）",
    "columns": [
      "服务分类（加粗带）",
      "企业架构服务",
      "Context I: Individual/Founder",
      "Context II: Team",
      "Context III: Team of Teams",
      "Context IV: Enduring Enterprise"
    ],
    "rows": [
      [
        "Requirements Elicitation and Understanding Services",
        "Stakeholders Management Services",
        "×",
        "×",
        "×",
        "×"
      ],
      [
        "Requirements Elicitation and Understanding Services",
        "Business Value Assessment and Analysis Service",
        "×",
        "×",
        "×",
        "×"
      ],
      [
        "Architecture Planning Services",
        "Architecture Project Planning Services",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Architecture Planning Services",
        "Architecting Tailoring Services",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Design Support Services",
        "Architecture Vision and Strategy Definition Services",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Design Support Services",
        "Architecture Modeling and Documentation Services (MVA)",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Design Support Services",
        "Architecture Integration Services",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Design Support Services",
        "Architecture Compliance Dev. Services (Bus, Info, Appl, Infra, Systs, ...)",
        "",
        "",
        "",
        "×"
      ],
      [
        "Development Support Services",
        "Architecture and Standards Guidance Service",
        "×",
        "×",
        "×",
        "×"
      ],
      [
        "Development Support Services",
        "Compliance Assessment and Analysis Service",
        "",
        "",
        "",
        "×"
      ],
      [
        "Development Support Services",
        "Change Management Services",
        "",
        "×",
        "×",
        "×"
      ],
      [
        "Development Support Services",
        "Release Support Services",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Enterprise Support Services",
        "Portfolio Management Support Services (inc. Asset Mgmt, Acquisitions)",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Enterprise Support Services",
        "Risk Management Services",
        "×",
        "×",
        "×",
        "×"
      ],
      [
        "Enterprise Support Services",
        "Sustainability Management Support Services",
        "×",
        "×",
        "×",
        "×"
      ],
      [
        "Enterprise Support Services",
        "Enterprise Analysis and Assessment Services",
        "",
        "",
        "×",
        "×"
      ],
      [
        "Enterprise Support Services",
        "Capability Planning Support Service",
        "",
        "",
        "",
        "×"
      ],
      [
        "Enterprise Architecture Practice Development Support Services",
        "Enterprise Architecture Development Process Improvement Service",
        "",
        "",
        "",
        "×"
      ]
    ],
    "cell_legend": [
      "× = 该服务在该语境中应考虑；空白 = 该语境未列入"
    ],
    "notes_zh": "原图另有 6 个加粗分类列（需求获取、架构规划、设计支持、开发支持、企业支持、EA 实践发展）穿插在服务列之间，本身不带 ×；本表把它们并入“服务分类”列。各语境服务数：I=5、II=6、III=14、IV=18。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色单元格 + ×",
    "meaning_zh": "该企业架构服务在该语境中应被考虑",
    "explicit": false
  },
  {
    "symbol": "空白单元格",
    "meaning_zh": "该语境未列入该服务",
    "explicit": false
  },
  {
    "symbol": "加粗竖排标题列",
    "meaning_zh": "服务分类带（需求获取、架构规划、设计支持、开发支持、企业支持、EA 实践发展），不是具体服务",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "矩阵：左侧 4 行语境标签（粗体、带底纹），右侧 24 个竖排列；第 1、4、7、12、17、23 列为加粗分类带（列宽相同、右侧粗竖线），其余为服务列；表体下方为图题。"
}
```

## 相关图

```json
[
  {
    "target": "G217/fig4-1",
    "relation": "complements",
    "note_zh": "同一组四个 DPBoK 语境：图 4-1 映射 TOGAF 原则，图 4-2 映射企业架构服务。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "× 的含义按正文“should be considered”理解为应考虑/建议使用；原图无图例。",
    "6 个分类带的列宽与数据列相同，容易被误当成服务列；已按加粗与粗竖线区分。",
    "中文稿引用的中文化 PNG 严重损坏，无法用它复核任何映射；本分析完全以英文 PDF 原图为准。",
    "图题中的 “to ... Emergence Model” 表示“映射到涌现模型”，中文图题按此拟译。"
  ],
  "analyzed_from": [
    "英文 PDF 第 50 页 500 dpi 渲染与 figctx 220 dpi 截图",
    "fig4-2_p50_1.png 及放大分块 z11/z12/z21/z22",
    "绿色单元格像素统计（24 列 × 4 行）与列线检测",
    "英文 PDF 第 50 页正文与图题（Figure 4-2）",
    "中文稿 G217e_在数字企业中使用TOGAF标准.md 第 641–679 行",
    "figs/zh/g217e_fig4-2_zh.png、标签对照表"
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
