# G234/fig4-7 · 元数据集成：混合式模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-7.md) · [JSON](../../architecture/diagrams/G234/fig4-7.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 27 页

![英文原图](../assets/G234/fig4-7-p0027.png)

PDF 坐标：`[154.3, 464.4, 346.3, 578.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Date
Governance
Dataiglossany.
Reference
(bate Quality
Policies. &
aes
Data
| _Blisinest
| Processes
as,
\|
mad
Privacy
‘Applitaten
a ~-
Repostay,
Technical &
)
Risk
Management
rational
s— \ a
icadsta
ma
‘Security
Management
```

## 概要（历史解释；局部修正见上）

混合式：一部分元数据以中央库为主副本并由库内流程维护，其余元数据仍由现有工具持有主副本并与中央库同步。

## 目的（历史解释；局部修正见上）

表 4-1 的第二种集成模型，说明迁移的中间状态：对选定子集把主副本、流程与校验工作流一起迁入中央库，其余范围保留现有工具并与之同步。

## 阅读顺序（历史解释；局部修正见上）

以中央圆柱 Central Repository 为中心。先看哪些域只有人物图标直连中央库：Data Glossary, Policies, & Data Quality、Business Processes、Reference Data，以及顶部的 Data Governance——这些表示元数据与流程都在库内。再看哪些域是“人物 + 灰色存储库”再连到中央库：Application Repository、Technical & Operational Metadata、Data Privacy、Risk Management、Security Management——这些表示现有工具仍持主副本并向中央库同步。

## 关键含义（历史解释；局部修正见上）

- 主副本分裂：选定子集在中央库中为主副本，现有工具迁移后退役；其余范围仍以现有工具为主副本。
- 对迁入子集，中央库同时承载维护流程与校验工作流；图中以“人物直连、无中间存储库”表示。
- 对其余范围，现有工具与中央库同步；图中以“人物 + 灰色存储库 → 中央库”表示。
- Data Governance 仍以双向箭头直连中央库，跨越两种范围，负责治理监督。
- 直连域（Data Glossary、Business Processes、Reference Data）与中央库是双向箭头；经存储库的域是单向箭头指向中央库（同步）。
- 子集范围由业务架构产出决定：要接入的业务参与者、元数据校验流程、数据治理运营模式。

## 层级（历史解释；局部修正见上）

中央存储库为中心；9 个域/治理主体分两类：库内管理（直连，4 个）与外部主副本（经存储库，5 个）。

## 线条含义（历史解释；局部修正见上）

人物直连 + 双向箭头 = 该域元数据与流程都在中央库内；人物 + 灰色存储库 + 单向箭头 = 该域现有工具持主副本并向中央库同步。箭头方向表示同步写入方向。

## 易误读点（历史解释；局部修正见上）

- 不要以为所有域都迁入了中央库；只有子集迁入，其余仍在现有工具中。
- 人物直连不等于没有流程，恰恰表示流程与校验工作流在库内。
- 不要把灰色存储库都当成来源；在混合式中它们是仍持主副本的现有工具。
- 双向箭头只出现在直连域与 Data Governance 上，不要把它套到经存储库的域。

## 元素

```json
[
  {
    "id": "central_repository",
    "label_en": "Central Repository",
    "label_zh": "中央存储库",
    "type": "artifact",
    "parent": null,
    "level": 0,
    "position": "图中央",
    "description_zh": "对迁入子集持有主副本并承载流程。"
  },
  {
    "id": "data_governance",
    "label_en": "Data Governance",
    "label_zh": "数据治理",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "position": "顶部中央",
    "description_zh": "直连中央库的治理主体。"
  },
  {
    "id": "data_glossary",
    "label_en": "Data Glossary, Policies, & Data Quality",
    "label_zh": "数据术语表、政策与数据质量",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左上",
    "description_zh": "仅人物图标，直连中央库。"
  },
  {
    "id": "business_processes",
    "label_en": "Business Processes",
    "label_zh": "业务流程",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左侧",
    "description_zh": "仅人物图标，直连中央库。"
  },
  {
    "id": "reference_data",
    "label_en": "Reference Data",
    "label_zh": "参考数据",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右上",
    "description_zh": "仅人物图标，直连中央库。"
  },
  {
    "id": "application_repository",
    "label_en": "Application Repository",
    "label_zh": "应用存储库",
    "type": "artifact",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "人物 + 灰色存储库，向中央库同步。"
  },
  {
    "id": "technical_operational",
    "label_en": "Technical & Operational Metadata",
    "label_zh": "技术与运营元数据",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左下偏底",
    "description_zh": "人物 + 灰色存储库，向中央库同步。"
  },
  {
    "id": "data_privacy",
    "label_en": "Data Privacy",
    "label_zh": "数据隐私",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右侧居中",
    "description_zh": "人物 + 灰色存储库，向中央库同步。"
  },
  {
    "id": "risk_management",
    "label_en": "Risk Management",
    "label_zh": "风险管理",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右下",
    "description_zh": "人物 + 灰色存储库，向中央库同步。"
  },
  {
    "id": "security_management",
    "label_en": "Security Management",
    "label_zh": "安全管理",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右下偏底",
    "description_zh": "人物 + 灰色存储库，向中央库同步。"
  }
]
```

## 关系

```json
[
  {
    "from": "data_governance",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both"
  },
  {
    "from": "data_glossary",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both"
  },
  {
    "from": "business_processes",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both"
  },
  {
    "from": "reference_data",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both"
  },
  {
    "from": "application_repository",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "现有工具持主副本，向中央库同步。"
  },
  {
    "from": "technical_operational",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "data_privacy",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "risk_management",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "security_management",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  }
]
```

## 图例

```json
[
  {
    "symbol": "青色圆柱 Central Repository",
    "meaning_zh": "中央元数据存储库（子集的主副本）",
    "explicit": true
  },
  {
    "symbol": "人物图标直连中央库",
    "meaning_zh": "该域元数据与流程都在中央库内",
    "explicit": false
  },
  {
    "symbol": "人物 + 灰色圆柱再连中央库",
    "meaning_zh": "该域现有工具持主副本，向中央库同步",
    "explicit": false
  },
  {
    "symbol": "双向箭头",
    "meaning_zh": "库内域与中央库双向交换",
    "explicit": false
  },
  {
    "symbol": "单向箭头",
    "meaning_zh": "外部主副本向中央库同步",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中央圆柱居中；左上与正左为直连域人物，右上为直连的参考数据；左下、正下、右侧三个经存储库的域；Data Governance 在顶部直连。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-6",
    "relation": "follows",
    "note_zh": "从集中式（只有副本）演进到混合式（部分主副本入库）"
  },
  {
    "target": "G234/fig4-8",
    "relation": "precedes",
    "note_zh": "混合式进一步演进为统一式（全范围主副本与流程入库）"
  },
  {
    "target": "G234/fig4-5",
    "relation": "related",
    "note_zh": "决定哪些资产迁入中央库的依据是图 4-5 的资产清单"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中没有文字说明“直连 = 库内主副本、经存储库 = 外部主副本”，该对应关系由表 4-1 与版式推断。",
    "Data Governance 只有人物、无存储库，按治理主体处理。"
  ],
  "analyzed_from": [
    "英文 PDF 第 27 页原图截图（2x2 放大分块）",
    "英文 PDF 第 27 页表 4-1 文字",
    "中文稿 G234e_信息架构_元数据管理.md 第 353–406 行",
    "figs/g234e_fig4-7_en.png、figs/zh/g234e_fig4-7_zh.png"
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
