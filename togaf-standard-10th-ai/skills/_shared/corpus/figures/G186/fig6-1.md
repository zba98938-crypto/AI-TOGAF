# G186/fig6-1 · 以 ADM 支持四种目的的“走查”重点

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/fig6-1.md) · [JSON](../../architecture/diagrams/G186/fig6-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`editorial-added`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 概要（历史解释；局部修正见上）

用四栏卡片对照四种架构目的在 ADM 走查中各自要重点检查的事项。

## 目的（历史解释；局部修正见上）

第 6.4 节 ADM 结论的收束图：四种目的都走同一条 ADM，但走查的重点不同。作者用并排四栏提醒实践者按目的选择任务，并强调这些任务是强制性的，跳过就要承担风险。

## 阅读顺序（历史解释；局部修正见上）

从左到右读四栏：支持战略、支持组合、支持项目、支持解决方案交付。每栏标题下七条要点自上而下按该章小节顺序排列。栏与栏之间没有连线；横向位置表示从战略到解决方案交付、范围逐步收窄、交付越来越具体，而不是时间顺序。

## 关键含义（历史解释；局部修正见上）

- 四栏分别对应四种架构目的：支持战略、支持组合、支持项目、支持解决方案交付。
- 支持战略栏：理解语境 → 评估企业 → 确定目标态方法 → 确认变革属性 → 价值主张 → 识别并排序工作包 → 完成愿景与目标架构。
- 支持组合栏：按主题分组工作包 → 平衡机会与可行性 → 进入预算 → 内部参与 → 目标是否达成 → 建立交付信心 → 处理“野生”请求。
- 支持项目栏：确定依赖 → 干系人与关键角色 → 视角与需求 → 与“邻居”沟通 → 交付与验收能力评估 → 平衡选项与供应商 → 确定范围与预算。
- 支持解决方案交付栏：界定范围 → 功能纯度与创新 → 移交与收尾 → 对齐实施者 → 指导交付 → 实现解决方案 → 治理与合规。
- 四栏共用同一条 ADM，不是四套方法；差别在走查的侧重点、详细程度和交付物。
- 图中每栏只列七条，属于重点摘录而非完整任务清单（例如项目栏未列 9.4 准备解决方案交付治理）。

## 层级（历史解释；局部修正见上）

两层：第一层是四个并列的架构目的栏；第二层是每栏下的七个并列要点。没有跨栏的上下级或连线。

## 线条含义（历史解释；局部修正见上）

全图没有连线或箭头。同一栏用同一底色和标题表示同一目的；横向排列表示四种目的的次序（战略→组合→项目→解决方案交付），不表示流程依赖。

## 易误读点（历史解释；局部修正见上）

- 不要把四栏理解为四个 ADM 阶段或四条独立流程；它们是对同一 ADM 的四种配置。
- 不要把每栏七条当作该目的的全部任务；原书章节还有更多小节与活动。
- 横向不是时间轴：四种目的可以并行、迭代，先后取决于业务周期而非图中位置。
- “干系人”应读作中文稿统一术语“利益相关者”。
- “治理与合规”是编者归纳，不是第 10 章的原始小节名。

## 元素

```json
[
  {
    "id": "diagram_title",
    "label_en": null,
    "label_zh": "以 ADM 支持四种目的的“走查”重点",
    "type": "note",
    "parent": null,
    "level": 0,
    "position": "图顶标题"
  },
  {
    "id": "col_strategy",
    "label_en": null,
    "label_zh": "支持战略",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "第 1 栏",
    "description_zh": "浅黄色卡片，含七条要点。"
  },
  {
    "id": "s_understand",
    "label_en": null,
    "label_zh": "理解语境",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 1
  },
  {
    "id": "s_assess",
    "label_en": null,
    "label_zh": "评估企业",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 2
  },
  {
    "id": "s_approach",
    "label_en": null,
    "label_zh": "确定目标态方法",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 3
  },
  {
    "id": "s_change_nature",
    "label_en": null,
    "label_zh": "确认变革属性",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 4
  },
  {
    "id": "s_value_prop",
    "label_en": null,
    "label_zh": "价值主张",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 5
  },
  {
    "id": "s_work_packages",
    "label_en": null,
    "label_zh": "识别并排序工作包",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 6
  },
  {
    "id": "s_vision",
    "label_en": null,
    "label_zh": "完成愿景与目标架构",
    "type": "process",
    "parent": "col_strategy",
    "level": 2,
    "order": 7
  },
  {
    "id": "col_portfolio",
    "label_en": null,
    "label_zh": "支持组合",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 2,
    "position": "第 2 栏",
    "description_zh": "浅蓝色卡片，含七条要点。"
  },
  {
    "id": "p_themes",
    "label_en": null,
    "label_zh": "按主题分组工作包",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 1
  },
  {
    "id": "p_viability",
    "label_en": null,
    "label_zh": "平衡机会与可行性",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 2
  },
  {
    "id": "p_budget",
    "label_en": null,
    "label_zh": "进入预算",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 3
  },
  {
    "id": "p_engagement",
    "label_en": null,
    "label_zh": "内部参与",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 4
  },
  {
    "id": "p_goals_met",
    "label_en": null,
    "label_zh": "目标是否达成",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 5
  },
  {
    "id": "p_confidence",
    "label_en": null,
    "label_zh": "建立交付信心",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 6
  },
  {
    "id": "p_wild_requests",
    "label_en": null,
    "label_zh": "处理“野生”请求",
    "type": "process",
    "parent": "col_portfolio",
    "level": 2,
    "order": 7
  },
  {
    "id": "col_project",
    "label_en": null,
    "label_zh": "支持项目",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 3,
    "position": "第 3 栏",
    "description_zh": "浅绿色卡片，含七条要点。"
  },
  {
    "id": "j_dependencies",
    "label_en": null,
    "label_zh": "确定依赖",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 1
  },
  {
    "id": "j_stakeholders",
    "label_en": null,
    "label_zh": "干系人与关键角色",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 2
  },
  {
    "id": "j_views",
    "label_en": null,
    "label_zh": "视角与需求",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 3
  },
  {
    "id": "j_neighbors",
    "label_en": null,
    "label_zh": "与“邻居”沟通",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 4
  },
  {
    "id": "j_capability_assessment",
    "label_en": null,
    "label_zh": "交付与验收能力评估",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 5
  },
  {
    "id": "j_options",
    "label_en": null,
    "label_zh": "平衡选项与供应商",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 6
  },
  {
    "id": "j_scope_budget",
    "label_en": null,
    "label_zh": "确定范围与预算",
    "type": "process",
    "parent": "col_project",
    "level": 2,
    "order": 7
  },
  {
    "id": "col_solution",
    "label_en": null,
    "label_zh": "支持解决方案交付",
    "type": "group",
    "parent": null,
    "level": 1,
    "order": 4,
    "position": "第 4 栏",
    "description_zh": "浅棕色卡片，含七条要点。"
  },
  {
    "id": "d_scope",
    "label_en": null,
    "label_zh": "界定范围",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 1
  },
  {
    "id": "d_purity",
    "label_en": null,
    "label_zh": "功能纯度与创新",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 2
  },
  {
    "id": "d_handover",
    "label_en": null,
    "label_zh": "移交与收尾",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 3
  },
  {
    "id": "d_align",
    "label_en": null,
    "label_zh": "对齐实施者",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 4
  },
  {
    "id": "d_guide",
    "label_en": null,
    "label_zh": "指导交付",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 5
  },
  {
    "id": "d_realize",
    "label_en": null,
    "label_zh": "实现解决方案",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 6
  },
  {
    "id": "d_governance",
    "label_en": null,
    "label_zh": "治理与合规",
    "type": "process",
    "parent": "col_solution",
    "level": 2,
    "order": 7
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_four_columns",
    "title_zh": "四栏要点逐行对照",
    "columns": [
      "序号",
      "支持战略",
      "支持组合",
      "支持项目",
      "支持解决方案交付"
    ],
    "rows": [
      [
        "1",
        "理解语境",
        "按主题分组工作包",
        "确定依赖",
        "界定范围"
      ],
      [
        "2",
        "评估企业",
        "平衡机会与可行性",
        "干系人与关键角色",
        "功能纯度与创新"
      ],
      [
        "3",
        "确定目标态方法",
        "进入预算",
        "视角与需求",
        "移交与收尾"
      ],
      [
        "4",
        "确认变革属性",
        "内部参与",
        "与“邻居”沟通",
        "对齐实施者"
      ],
      [
        "5",
        "价值主张",
        "目标是否达成",
        "交付与验收能力评估",
        "指导交付"
      ],
      [
        "6",
        "识别并排序工作包",
        "建立交付信心",
        "平衡选项与供应商",
        "实现解决方案"
      ],
      [
        "7",
        "完成愿景与目标架构",
        "处理“野生”请求",
        "确定范围与预算",
        "治理与合规"
      ]
    ],
    "notes_zh": "按每栏自上而下的顺序横向对齐；四栏之间没有对应关系，同一行只是序号相同。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅黄卡片",
    "meaning_zh": "支持战略的架构",
    "explicit": false
  },
  {
    "symbol": "浅蓝卡片",
    "meaning_zh": "支持组合的架构",
    "explicit": false
  },
  {
    "symbol": "浅绿卡片",
    "meaning_zh": "支持项目的架构",
    "explicit": false
  },
  {
    "symbol": "浅棕卡片",
    "meaning_zh": "支持解决方案交付的架构",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "四张等宽圆角卡片从左到右并排，颜色依次为浅黄、浅蓝、浅绿、浅棕；每张卡片顶部一个加粗标题，下面七行居中文字。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig3-3",
    "relation": "related",
    "note_zh": "图 3-3 给出四种企业架构目的；本图进一步给出四种目的各自的走查重点。"
  },
  {
    "target": "G186/fig5-7",
    "relation": "related",
    "note_zh": "图 5-7 是“支持战略”目的的 ADM 项目计划实例，本图第 1 栏概括同一目的的走查重点。"
  },
  {
    "target": "G186/fig5-8",
    "relation": "related",
    "note_zh": "图 5-8 是“支持组合”目的的 ADM 项目计划实例，对应本图第 2 栏。"
  },
  {
    "target": "G186/fig5-9",
    "relation": "related",
    "note_zh": "图 5-9 是“支持项目”目的的 ADM 项目计划实例，对应本图第 3 栏。"
  },
  {
    "target": "G186/fig5-10",
    "relation": "related",
    "note_zh": "图 5-10 是“支持解决方案交付”目的的 ADM 项目计划实例，对应本图第 4 栏。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "英文原书第 6.4 节没有对应插图，本图为中文稿自绘；无法核对它是否逐条对应原书章节。",
    "每栏只列七条，取舍标准未说明；“治理与合规”等条目的来源需要结合第 10 章与第 15 章理解。"
  ],
  "analyzed_from": [
    "figs/g186_fig6-1.svg 源码与渲染后的四栏卡片",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 1128–1132 行及第 7–10 章小节标题",
    "英文 PDF 第 6 章（无对应图，仅核对章节结构）"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": false,
  "caption_page_match": null,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
