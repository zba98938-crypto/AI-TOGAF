# G234/fig4-8 · 元数据集成：统一式模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-8.md) · [JSON](../../architecture/diagrams/G234/fig4-8.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G234/fig4-8-p0028.png)

PDF 坐标：`[154.3, 72.1, 346.3, 206.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Data
Governance
Data Glossary.
Reference
Policies, &
4
4
Data Quality
pepe
Business,
>
Processes
&..*
=
=
Central
“”
Repository
Technical &
. Privacy
Operational
=
Metadata
Ma
Risk
“8
‘
Management
Application
Repository
Security
Management
```

## 概要（历史解释；局部修正见上）

统一式：全范围元数据及维护流程、校验工作流都统一到中央库，各社区大多直接读写。

## 目的（历史解释；局部修正见上）

表 4-1 的第三种集成模型，说明治理成熟后的目标形态：既统一元数据，也统一维护元数据的流程与校验工作流，从而消除多库同步与孤岛问题。

## 阅读顺序（历史解释；局部修正见上）

看中央圆柱 Central Repository，九个域社区（Data Governance、Data Glossary, Policies, & Data Quality、Business Processes、Technical & Operational Metadata、Application Repository、Security Management、Risk Management、Data Privacy、Reference Data）以人物图标直接环绕。除 Security Management 只有一条箭头指向中央库外，其余八个域都用双向箭头与中央库相连。图中没有灰色存储库图标，表示不存在外部主副本。

## 关键含义（历史解释；局部修正见上）

- 全范围统一：既统一元数据，也统一维护元数据的流程与校验工作流。
- 九个域社区全部直接连接中央库，没有中间存储库，表示所有主副本都在库内。
- 除 Security Management 外，所有域社区与中央库都是双向箭头；Security Management 只有一条单向箭头指向中央库。
- 正文补充：可进一步为不同用户社区提供专属用户体验，可能涉及专属用户界面。
- 该模型要求所有社区都改用中央库，是三种模型中最彻底的一种，代价是迁移与治理投入最大。
- 与图 4-6（只有副本）、图 4-7（部分主副本入库）构成治理深度递增的三种选择。

## 层级（历史解释；局部修正见上）

中央统一存储库为中心；外围 9 个域社区平级环绕，无中间层、无存储库子节点。

## 线条含义（历史解释；局部修正见上）

双向箭头表示社区与中央库之间的读写；Security Management 的箭头为单向，只向中央库供数。图中没有灰色圆柱，说明没有外部主副本。

## 易误读点（历史解释；局部修正见上）

- 人物图标不代表个人，而是该元数据域的社区/角色。
- 不要以为所有箭头都是双向：Security Management 是单向供数，其余八个域为双向读写。
- 图中没有存储库图标，不等于没有存储；中央圆柱就是唯一存储库。
- 中文稿在图 4-8 后附的标签表其实是图 4-9 的，不能据它把本图读成三种集成模式。

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
    "description_zh": "统一式下唯一的元数据存储库。"
  },
  {
    "id": "data_governance",
    "label_en": "Data Governance",
    "label_zh": "数据治理",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "position": "顶部中央"
  },
  {
    "id": "data_glossary",
    "label_en": "Data Glossary, Policies, & Data Quality",
    "label_zh": "数据术语表、政策与数据质量",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左上"
  },
  {
    "id": "business_processes",
    "label_en": "Business Processes",
    "label_zh": "业务流程",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左侧"
  },
  {
    "id": "technical_operational",
    "label_en": "Technical & Operational Metadata",
    "label_zh": "技术与运营元数据",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左下"
  },
  {
    "id": "application_repository",
    "label_en": "Application Repository",
    "label_zh": "应用存储库",
    "type": "artifact",
    "parent": null,
    "level": 1,
    "position": "左下偏外"
  },
  {
    "id": "security_management",
    "label_en": "Security Management",
    "label_zh": "安全管理",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "正下方"
  },
  {
    "id": "risk_management",
    "label_en": "Risk Management",
    "label_zh": "风险管理",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右下"
  },
  {
    "id": "data_privacy",
    "label_en": "Data Privacy",
    "label_zh": "数据隐私",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右侧"
  },
  {
    "id": "reference_data",
    "label_en": "Reference Data",
    "label_zh": "参考数据",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右上"
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
    "from": "technical_operational",
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
    "arrow": "both"
  },
  {
    "from": "security_management",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "单向箭头：安全管理只向中央库供数，不读取。"
  },
  {
    "from": "risk_management",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both"
  },
  {
    "from": "data_privacy",
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
  }
]
```

## 图例

```json
[
  {
    "symbol": "青色圆柱 Central Repository",
    "meaning_zh": "唯一的统一元数据存储库",
    "explicit": true
  },
  {
    "symbol": "人物图标（多种颜色）",
    "meaning_zh": "该元数据域的社区/角色",
    "explicit": false
  },
  {
    "symbol": "双向箭头",
    "meaning_zh": "社区与中央库之间的读写交换",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中央圆柱居中，九个域社区人物图标均匀环绕：上方数据治理、左上数据术语表、左中业务流程、左下技术与运营元数据、左下偏外应用存储库、正下安全管理、右下风险管理、右中数据隐私、右上参考数据。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-7",
    "relation": "follows",
    "note_zh": "从混合式（部分主副本入库）进一步统一到全范围"
  },
  {
    "target": "G234/fig4-6",
    "relation": "related",
    "note_zh": "集中式是本模型治理深度的另一端"
  },
  {
    "target": "G234/fig4-9",
    "relation": "related",
    "note_zh": "统一后仍需与外部来源交换元数据，交换方式见图 4-9"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中没有文字说明九个域是否都等同对待；按全部直连、全部双向箭头理解为全范围统一。",
    "中文稿图 4-8 后附的标签表属于图 4-9，已在 asset_checks 中标注。"
  ],
  "analyzed_from": [
    "英文 PDF 第 28 页原图截图",
    "英文 PDF 第 28 页表 4-1 文字",
    "中文稿 G234e_信息架构_元数据管理.md 第 383–424 行",
    "figs/g234e_fig4-8_en.png、figs/zh/g234e_fig4-8_zh.png"
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
