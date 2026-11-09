# G234/fig4-6 · 元数据集成：集中式模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-6.md) · [JSON](../../architecture/diagrams/G234/fig4-6.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 27 页

![英文原图](../assets/G234/fig4-6-p0027.png)

PDF 坐标：`[154.3, 312.6, 346.3, 418.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Data
Governance
Data Glossary,
or)
m4
A
Processes
Business
=~
Data
‘Applicaton
Pevaty
Repostory
J -
Tectneate. (2
|} Management
Risk
Spentne O
| ma:
Metadata
ak
‘security
Management
```

## 概要（历史解释；局部修正见上）

集中式：各来源只把业务元数据副本汇入中央存储库，创建与维护流程仍留在源系统。

## 目的（历史解释；局部修正见上）

表 4-1 用本图说明第一种集成模型：中央库只提供统一访问点，保存业务元数据的副本，而创建与维护这些元数据的流程仍在存储库之外。

## 阅读顺序（历史解释；局部修正见上）

以中央青色圆柱 Central Repository 为中心。四周的灰色圆柱是各域现有存储库，旁边的人物图标代表该域社区；箭头方向表示元数据流向。左侧、下方与右侧的 Data Privacy、Risk Management、Security Management、Reference Data 都向中央库供数；顶部的 Data Governance 没有存储库，直接与中央库双向相连，表示治理监督。

## 关键含义（历史解释；局部修正见上）

- 中央库只保存业务元数据的副本，不是主副本；主副本仍在各来源系统。
- 创建与维护元数据的流程位于存储库之外，中央库不承载校验工作流。
- Data Glossary, Policies, & Quality、Business Processes、Application Repository、Technical & Operational Metadata 以单向箭头向中央库供数。
- Data Privacy、Risk Management、Security Management、Reference Data 也以单向箭头向中央库供数：它们同样只是来源，不反向读取中央库。
- Data Governance 是唯一双向连接：它没有存储库，代表治理监督关系而非元数据存储。
- 与图 4-7、图 4-8 相比，本模型不把流程迁入中央库，只解决“统一访问”而不改变元数据生产方式。

## 层级（历史解释；局部修正见上）

中央存储库为中心节点；外围 8 个元数据域社区 + 1 个治理主体（Data Governance）。各域是否画出自己的存储库图标表示它是否有独立存储库；本图中除 Data Governance 外都有。

## 线条含义（历史解释；局部修正见上）

单向青色箭头 = 该域向中央库提供元数据；双向青色箭头 = 该域与中央库互相交换（供数并读取）；人物图标 = 该域的负责社区，不是独立系统。

## 易误读点（历史解释；局部修正见上）

- 不要把中央库当成主数据源；它只有业务元数据的副本。
- 不要以为右侧域有双向箭头：除 Data Governance 外，所有域都是单向供数。
- 图中没有出现“消费者”角色；消费通过各域社区体现。
- 右上角紫色人物在原图中缺少可见标签，不要因此认为没有 Reference Data 域；表 4-1 与中文对照表都列出该域。

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
    "description_zh": "集中式模型的核心，只保存业务元数据副本。"
  },
  {
    "id": "data_governance",
    "label_en": "Data Governance",
    "label_zh": "数据治理",
    "type": "organization_unit",
    "parent": null,
    "level": 1,
    "position": "顶部中央",
    "description_zh": "治理主体，直接与中央库双向连接，无独立存储库。"
  },
  {
    "id": "data_glossary",
    "label_en": "Data Glossary, Policies, & Data Quality",
    "label_zh": "数据术语表、政策与数据质量",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左上",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "business_processes",
    "label_en": "Business Processes",
    "label_zh": "业务流程",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "左中",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "application_repository",
    "label_en": "Application Repository",
    "label_zh": "应用存储库",
    "type": "artifact",
    "parent": null,
    "level": 1,
    "position": "左下",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "technical_operational",
    "label_en": "Technical & Operational Metadata",
    "label_zh": "技术与运营元数据",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "底部偏左",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "data_privacy",
    "label_en": "Data Privacy",
    "label_zh": "数据隐私",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右侧居中",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "risk_management",
    "label_en": "Risk Management",
    "label_zh": "风险管理",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右下",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "security_management",
    "label_en": "Security Management",
    "label_zh": "安全管理",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右下偏底",
    "description_zh": "以人物 + 灰色存储库图标表示。"
  },
  {
    "id": "reference_data",
    "label_en": "Reference Data",
    "label_zh": "参考数据",
    "type": "data",
    "parent": null,
    "level": 1,
    "position": "右上",
    "description_zh": "原图截图右缘裁切，仅见紫色人物与灰色存储库，标签由表 4-1 与中文对照表确认。"
  }
]
```

## 关系

```json
[
  {
    "from": "data_glossary",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "数据术语表域向中央库供数。"
  },
  {
    "from": "business_processes",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "application_repository",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
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
    "arrow": "forward",
    "description_zh": "该域向中央库提供元数据（单向箭头）。"
  },
  {
    "from": "risk_management",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "该域向中央库提供元数据（单向箭头）。"
  },
  {
    "from": "security_management",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "该域向中央库提供元数据（单向箭头）。"
  },
  {
    "from": "reference_data",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "该域向中央库提供元数据（单向箭头）。"
  },
  {
    "from": "data_governance",
    "to": "central_repository",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "治理主体与中央库双向交换，无存储库。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "青色圆柱 Central Repository",
    "meaning_zh": "中央元数据存储库（副本）",
    "explicit": true
  },
  {
    "symbol": "灰色圆柱",
    "meaning_zh": "各元数据域现有的存储库",
    "explicit": false
  },
  {
    "symbol": "人物图标（多种颜色）",
    "meaning_zh": "该元数据域的负责社区/角色",
    "explicit": false
  },
  {
    "symbol": "单向箭头",
    "meaning_zh": "该域向中央库提供元数据",
    "explicit": false
  },
  {
    "symbol": "双向箭头",
    "meaning_zh": "该域与中央库双向交换元数据",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "中央圆柱居中；左上、左中、左下三个来源存储库与底部技术/运营元数据库从左侧和下方指向中心；右上、右中、右下三个域存储库与顶部 Data Governance 在右侧和上方与中心交换。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-7",
    "relation": "precedes",
    "note_zh": "三种集成模型按集中式 → 混合式 → 统一式递进"
  },
  {
    "target": "G234/fig4-5",
    "relation": "related",
    "note_zh": "集中式中央库保存的业务元数据副本即图 4-5 中的业务类资产"
  },
  {
    "target": "G234/fig4-8",
    "relation": "related",
    "note_zh": "统一式是本模型在治理范围上的另一端"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "右上角 Reference Data 标签被截图右缘裁切，只能依据表 4-1 与中文标签表补全。",
    "各域的灰色圆柱未单独标注名称，按“该域自有存储库”理解。",
    "Data Privacy、Risk Management、Security Management、Reference Data 的双向箭头在 2x 截图中两端箭头可见，但线条很短。"
  ],
  "analyzed_from": [
    "英文 PDF 第 27 页原图截图（2x2 放大分块）",
    "英文 PDF 第 27 页表 4-1 文字",
    "中文稿 G234e_信息架构_元数据管理.md 第 353–387 行",
    "figs/g234e_fig4-6_en.png、figs/zh/g234e_fig4-6_zh.png"
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
