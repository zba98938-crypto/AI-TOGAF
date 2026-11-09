# G211/fig5-3 · 能力/价值流映射示例

> 当前图示解析：[Markdown](../../architecture/diagrams/G211/fig5-3.md) · [JSON](../../architecture/diagrams/G211/fig5-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G211e.pdf`；SHA-256：`93fa7ac115956d34c0ad2161c46a5fd01cbc972d5f85a0f19f2f5b9d8c0a2b34`。

## 原图 · PDF 第 26 页

![英文原图](../assets/G211/fig5-3-p0026.png)

PDF 坐标：`[48.2, 36.0, 563.8, 361.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Define
Communicate
Assess
Interview
Onboard
Position
Position
Responses
Candidates
Employee
Program Mgmt.
HR Mgmt.
HR Mgmt.
HR Mgmt.
HR Mgmt.
Program/Human
Employee Supply
Employee Supply
Benefits Mgmt.
Onboard Tracking
Resource
land
and Demand Mgmt.
Matching
Demand Mgmt.
Terms Mgmt.
Skills Assessment
Asset Mgmt.
Position
‘Compensation
HR Mgmt.
‘Advertising
Asset Allocation
Mgmt.
‘Competency
Mgmt.
Finance Mgmt.
Facilities Mgmt.
Agreement Mgmt.
Labor Funding
Space Allocatiom
[Agreement
Structuring
Security Mgmt.
Employee
Background and ID
Information Mgmt.
Employee
Information Mgmt.
```

## 概要（历史解释；局部修正见上）

把“招聘员工”价值流的 5 个阶段逐一对应到使能该阶段的一级/二级业务能力，形成价值流—能力交叉映射。

## 目的（历史解释；局部修正见上）

示范第 5.2.2 节的做法：识别完整实现价值流所需的能力后，按阶段走查并把能力映射到各阶段，从而看出哪些能力对价值交付更关键、哪些能力被多个阶段或多个价值流复用，为投资排序与举措规划提供依据。正文说明每项能力使能一个或多个价值阶段，并指出该示例是“招聘员工”价值流。

## 阅读顺序（历史解释；局部修正见上）

从左到右读顶部 5 个 V 形箭头，这是价值流阶段的先后顺序。每个箭头正下方那一列灰框，是使能该阶段的能力：框左上角较大字号的字是一级能力，框内深灰色条是该一级能力下被选中的二级能力。同一列内的多个框是并列关系，上下次序没有含义。图中没有连线，能力与阶段的对应完全由“在哪一列”表达。

## 关键含义（历史解释；局部修正见上）

- 价值流由 5 个有序阶段构成：定义岗位 → 发布职位 → 评估应聘 → 面试候选人 → 入职；这张图只画阶段，不画阶段的进入/退出标准。
- 人力资源管理是贯穿型一级能力，5 个阶段都出现，但每个阶段调用的二级能力不同：胜任力管理（定义）、员工供需管理与职位广告（发布）、员工供需管理与技能评估（评估）、福利/条款/薪酬管理（面试）、入职跟踪（入职）。
- 同一个二级能力可以支撑多个阶段：员工供需管理同时出现在“发布职位”和“评估应聘”下，说明能力与阶段是多对多映射。
- “入职”阶段涉及的一级能力最多（人力资源、资产、设施、安全、信息管理 5 项），是跨职能协作最重的阶段。
- 图中只列出与阶段直接相关的二级能力（如“入职”只列入职跟踪），没有把每个一级能力下的全部子能力都展开；未列出的子能力不表示不存在。
- 本图只表达“能力使能阶段”，不表达能力成熟度、绩效或差距；把能力映射到多个价值流的复用分析也只用文字说明，图上没有画。
- 交叉映射的比较价值在正文中明确指出：同一能力被多个价值流使用时，对运营与业务成功更重要；本图只画一个价值流，因此这一层复用分析要靠组织定义完整价值流集合后另行完成。

## 层级（历史解释；局部修正见上）

共三层。第 1 层是“招聘员工”价值流（图中未单独画框，由 5 个阶段整体表示）；第 2 层是 5 个价值流阶段；第 3 层是业务能力，其中一级能力为灰框、二级能力为框内深灰条并嵌套在所属一级能力内。能力与阶段之间是映射（使能）关系，不是上下级关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连接线。V 形箭头首尾相接表示阶段的先后顺序（关系清单中记为显式 sequence）；能力与阶段的使能关系由“灰框位于该阶段箭头正下方”隐含表达（explicit=false, line=implicit）；二级能力与一级能力的上下级由框内嵌套表达。这种“能力位于阶段下方”的画法对应价值流建模中的“能力使能价值阶段”关系（背景知识）。

## 易误读点（历史解释；局部修正见上）

- 不要把同一列中灰框的上下顺序理解为优先级或时间先后，它们是并列的。
- 多次出现的“HR Mgmt.”是同一个一级能力在不同阶段被引用，不是 5 个不同的能力。
- 本图不是热力图，没有红/黄/绿差距含义；差距着色在图 4-4（G178）中才引入。
- 中文稿第 335 行引用的 figs/g211_fig5-3.svg 是自拟的 5×5 矩阵，漏掉全部二级能力和 4 个一级能力，还混入了“政策发布”，不能据它理解本图。

## 元素

```json
[
  {
    "id": "vs_recruit",
    "label_en": "Recruit Employee (value stream)",
    "label_zh": "招聘员工（价值流）",
    "type": "value_stream",
    "parent": null,
    "level": 0,
    "description_zh": "图中未单独画出，由 5 个阶段整体表示；名称来自正文 p25 与图 4-2。"
  },
  {
    "id": "st_define",
    "label_en": "Define Position",
    "label_zh": "定义岗位",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 1,
    "position": "第 1 列"
  },
  {
    "id": "st_communicate",
    "label_en": "Communicate Position",
    "label_zh": "发布职位",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 2,
    "position": "第 2 列"
  },
  {
    "id": "st_assess",
    "label_en": "Assess Responses",
    "label_zh": "评估应聘",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 3,
    "position": "第 3 列"
  },
  {
    "id": "st_interview",
    "label_en": "Interview Candidates",
    "label_zh": "面试候选人",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 4,
    "position": "第 4 列"
  },
  {
    "id": "st_onboard",
    "label_en": "Onboard Employee",
    "label_zh": "入职",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 5,
    "position": "第 5 列"
  },
  {
    "id": "c_program",
    "label_en": "Program Mgmt.",
    "label_zh": "项目群管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_hr",
    "label_en": "HR Mgmt.",
    "label_zh": "人力资源管理",
    "type": "capability",
    "parent": null,
    "level": 1,
    "description_zh": "5 个阶段下都出现，但每个阶段调用的二级能力不同。"
  },
  {
    "id": "c_finance",
    "label_en": "Finance Mgmt.",
    "label_zh": "财务管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_agreement",
    "label_en": "Agreement Mgmt.",
    "label_zh": "协议管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_asset",
    "label_en": "Asset Mgmt.",
    "label_zh": "资产管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_facilities",
    "label_en": "Facilities Mgmt.",
    "label_zh": "设施管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_security",
    "label_en": "Security Mgmt.",
    "label_zh": "安全管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_information",
    "label_en": "Information Mgmt.",
    "label_zh": "信息管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_prog_hr_match",
    "label_en": "Program/Human Resource Matching",
    "label_zh": "项目群/人力资源匹配",
    "type": "capability",
    "parent": "c_program",
    "level": 2
  },
  {
    "id": "c_competency",
    "label_en": "Competency Mgmt.",
    "label_zh": "胜任力管理",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_supply_demand",
    "label_en": "Employee Supply and Demand Mgmt.",
    "label_zh": "员工供需管理",
    "type": "capability",
    "parent": "c_hr",
    "level": 2,
    "description_zh": "同时支撑“发布职位”和“评估应聘”。"
  },
  {
    "id": "c_position_ad",
    "label_en": "Position Advertising",
    "label_zh": "职位广告",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_skills_assess",
    "label_en": "Skills Assessment",
    "label_zh": "技能评估",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_benefits",
    "label_en": "Benefits Mgmt.",
    "label_zh": "福利管理",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_terms",
    "label_en": "Terms Mgmt.",
    "label_zh": "雇佣条款管理",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_compensation",
    "label_en": "Compensation Mgmt.",
    "label_zh": "薪酬管理",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_onboard_track",
    "label_en": "Onboard Tracking",
    "label_zh": "入职跟踪",
    "type": "capability",
    "parent": "c_hr",
    "level": 2
  },
  {
    "id": "c_labor_funding",
    "label_en": "Labor Funding",
    "label_zh": "人工经费",
    "type": "capability",
    "parent": "c_finance",
    "level": 2
  },
  {
    "id": "c_agreement_struct",
    "label_en": "Agreement Structuring",
    "label_zh": "协议架构设计",
    "type": "capability",
    "parent": "c_agreement",
    "level": 2
  },
  {
    "id": "c_asset_alloc",
    "label_en": "Asset Allocation",
    "label_zh": "资产分配",
    "type": "capability",
    "parent": "c_asset",
    "level": 2
  },
  {
    "id": "c_space_alloc",
    "label_en": "Space Allocation",
    "label_zh": "空间分配",
    "type": "capability",
    "parent": "c_facilities",
    "level": 2
  },
  {
    "id": "c_background_id",
    "label_en": "Employee Background and ID",
    "label_zh": "员工背景调查与身份",
    "type": "capability",
    "parent": "c_security",
    "level": 2
  },
  {
    "id": "c_employee_info",
    "label_en": "Employee Information Mgmt.",
    "label_zh": "员工信息管理",
    "type": "capability",
    "parent": "c_information",
    "level": 2
  }
]
```

## 关系

```json
[
  {
    "from": "st_define",
    "to": "st_communicate",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "V 形箭头首尾相接"
  },
  {
    "from": "st_communicate",
    "to": "st_assess",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "st_assess",
    "to": "st_interview",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "st_interview",
    "to": "st_onboard",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "c_prog_hr_match",
    "to": "st_define",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "位于“定义岗位”列下方"
  },
  {
    "from": "c_competency",
    "to": "st_define",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_supply_demand",
    "to": "st_communicate",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_position_ad",
    "to": "st_communicate",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_labor_funding",
    "to": "st_communicate",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_supply_demand",
    "to": "st_assess",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_skills_assess",
    "to": "st_assess",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_benefits",
    "to": "st_interview",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_terms",
    "to": "st_interview",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_compensation",
    "to": "st_interview",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_agreement_struct",
    "to": "st_interview",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_onboard_track",
    "to": "st_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_asset_alloc",
    "to": "st_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_space_alloc",
    "to": "st_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_background_id",
    "to": "st_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "c_employee_info",
    "to": "st_onboard",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_recruit",
    "kind": "sequence",
    "name_zh": "招聘员工价值流",
    "steps": [
      "st_define",
      "st_communicate",
      "st_assess",
      "st_interview",
      "st_onboard"
    ]
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_crossmap",
    "title_zh": "阶段 × 能力交叉映射（按原图逐列转录，列内自上而下）",
    "columns": [
      "价值流阶段",
      "一级能力",
      "二级能力"
    ],
    "rows": [
      [
        "定义岗位 Define Position",
        "项目群管理 Program Mgmt.",
        "项目群/人力资源匹配 Program/Human Resource Matching"
      ],
      [
        "定义岗位 Define Position",
        "人力资源管理 HR Mgmt.",
        "胜任力管理 Competency Mgmt."
      ],
      [
        "发布职位 Communicate Position",
        "人力资源管理 HR Mgmt.",
        "员工供需管理 Employee Supply and Demand Mgmt.；职位广告 Position Advertising"
      ],
      [
        "发布职位 Communicate Position",
        "财务管理 Finance Mgmt.",
        "人工经费 Labor Funding"
      ],
      [
        "评估应聘 Assess Responses",
        "人力资源管理 HR Mgmt.",
        "员工供需管理 Employee Supply and Demand Mgmt.；技能评估 Skills Assessment"
      ],
      [
        "面试候选人 Interview Candidates",
        "人力资源管理 HR Mgmt.",
        "福利管理 Benefits Mgmt.；雇佣条款管理 Terms Mgmt.；薪酬管理 Compensation Mgmt."
      ],
      [
        "面试候选人 Interview Candidates",
        "协议管理 Agreement Mgmt.",
        "协议架构设计 Agreement Structuring"
      ],
      [
        "入职 Onboard Employee",
        "人力资源管理 HR Mgmt.",
        "入职跟踪 Onboard Tracking"
      ],
      [
        "入职 Onboard Employee",
        "资产管理 Asset Mgmt.",
        "资产分配 Asset Allocation"
      ],
      [
        "入职 Onboard Employee",
        "设施管理 Facilities Mgmt.",
        "空间分配 Space Allocation"
      ],
      [
        "入职 Onboard Employee",
        "安全管理 Security Mgmt.",
        "员工背景调查与身份 Employee Background and ID"
      ],
      [
        "入职 Onboard Employee",
        "信息管理 Information Mgmt.",
        "员工信息管理 Employee Information Mgmt."
      ]
    ],
    "notes_zh": "每行对应原图中的一个灰色一级能力框；同一阶段多行即该列从上到下的多个框。英文按图原样记录。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "V 形灰色箭头（chevron）",
    "meaning_zh": "价值流阶段，左到右为先后顺序",
    "explicit": false
  },
  {
    "symbol": "浅灰带黑框的框 + 左上角较大字号标题",
    "meaning_zh": "一级业务能力",
    "explicit": false
  },
  {
    "symbol": "框内深灰色条",
    "meaning_zh": "该一级能力下被选中的二级业务能力",
    "explicit": false
  },
  {
    "symbol": "灰框位于某阶段箭头的正下方",
    "meaning_zh": "该能力使能（支撑）这个阶段",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "顶部一行 5 个 V 形箭头，从左到右首尾相接；每个箭头下方是一列纵向堆叠的灰色能力框，每列 1–5 个，列内框的上下次序无含义。"
}
```

## 相关图

```json
[
  {
    "target": "G178/fig4-3",
    "relation": "same_as",
    "note_zh": "同一张“招聘员工”能力/价值流映射示例，在《价值流》指南中编号为图 4-3"
  },
  {
    "target": "G178/fig4-4",
    "relation": "related",
    "note_zh": "在本图基础上加入差距着色（热力图）并新增“政策发布”能力"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "二级能力的中文译名（如“项目群/人力资源匹配”“协议架构设计”“人工经费”“雇佣条款管理”）为解析者拟定，中文稿只给出 5 个阶段名和 5 个一级能力名。",
    "“Recruit Employee”价值流名未印在图内，取自英文正文 p25 与图 4-2。",
    "V 形箭头之间是否有独立箭头符号：原图为相邻 chevron 首尾相接，未画箭杆，顺序由形状表达。"
  ],
  "analyzed_from": [
    "英文 PDF 第 26 页原图截图（2×2 放大分块）",
    "英文 PDF 第 25–26 页正文",
    "中文稿 G211e_业务能力.md 第 328–339 行",
    "figs/g211_fig5-3.svg 源码与文字"
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
