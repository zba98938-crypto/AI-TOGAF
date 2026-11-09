# G238/fig4-1 · 利益相关者借助 BI 与分析能力追求的目标

> 当前图示解析：[Markdown](../../architecture/diagrams/G238/fig4-1.md) · [JSON](../../architecture/diagrams/G238/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G238e.pdf`；SHA-256：`87e00e009377a887627417ceffc28b1f480bfaf57c9c84ee6f8757cc5c1c9444`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G238/fig4-1-p0028.png)

PDF 坐标：`[48.2, 110.0, 563.8, 476.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
CEO
@
cio
@
cDOo
Improve Customeror ©
Store Data as an Asset ©
Generate Business Value
Partner Satisfaction
including Metadata
Leveraging New Data
Capabilities (e.g., Data
Science)
Improve Operational
©
Reduce Use-Case Time-to-
Efficiency
Market
Data Quality is Under ©
Control
Comply with Regulations
Reduce Total Cost of
(Privacy, Solvency Il, etc.)
Ownership
Democratize Use of Data ©
Leverage Innovation
Comply with Security ©
Opportunities
Guarantee Quality of ©
Service
Support Digital and Data ©
Innovation
Provide Interoperability ©
between Systems
> The Open Group
```

## 概要（历史解释；局部修正见上）

CEO、CIO、CDO 三类利益相关者各自追求的一组 BI 与分析目标，按列分组展示。

## 目的（历史解释；局部修正见上）

把表 4-1 的目标按“谁追求”重新组织：让读者一眼看出 CEO 关注业务结果、CIO 关注平台与运营、CDO 关注数据价值与治理，作为定义 BI 与分析能力目标与 KPI 的起点。

## 阅读顺序（历史解释；局部修正见上）

从左到右三列，列顶的 CEO / CIO / CDO 是被拉长的 Stakeholder 框（右上角双圆图标），列内每个淡紫色切角框是一个 Goal（右上角靶心图标）。目标归属完全由它落在哪一列决定；列内自上而下没有先后或优先级含义。图中没有箭头，因此目标之间的关系（如“合规”与“安全”的包含关系）不在图上表达。

## 关键含义（历史解释；局部修正见上）

- CEO 有 4 项目标：提升客户或伙伴满意度、提升运营效率、遵守法规、利用创新机会——偏业务结果与合规。
- CIO 有 7 项目标：数据作为资产（含元数据）、缩短用例上市时间、降低总拥有成本、遵守安全、保证服务质量、支撑数字与数据创新、提供系统间互操作性——偏平台、运营与安全。
- CDO 有 3 项目标：借助新数据能力创造业务价值、数据质量受控、数据民主化使用——聚焦数据价值、质量与共享。
- 图中共 14 个 Goal；表 4-1 有 17 项，因为表中把“Comply with Security”拆成数据分级与加密、数据泄露、身份与访问管理、基础设施基线 4 项（编号 2–5）。
- 目标与 KPI 的对应关系不在图内，只在表 4-1 中给出（如满意度→NPS、TCO→每用户成本、互操作→API 数量）。
- 同一目标可能被多个利益相关者追求，但图中每个目标只出现一次，表示作者给出的示例性归属，不是排他归属。

## 层级（历史解释；局部修正见上）

两层：L1 是三个 Stakeholder（CEO、CIO、CDO）；L2 是其下的 Goal。Goal 被画在 Stakeholder 框内，表示“该利益相关者追求这些目标”（包含/归属，不是分类学上的子类型）。目标之间没有上下级。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。Stakeholder 与 Goal 的关系由“目标位于该列之内”隐含表达（ArchiMate 中通常是关联或组成）；不能把列的左右顺序读成汇报关系或权限大小。

## 易误读点（历史解释；局部修正见上）

- 不要把图数成 17 个目标：原图只有 14 个，17 项是表 4-1 的编号体系（安全被拆为 4 项）。
- 不要以为 CDO 只负责 3 项、CIO 负责 7 项就是完整的职责边界；图只列与 BI & Analytics 能力相关的目标。
- 不要按列内从上到下理解优先级或时间顺序。
- 不要把 CEO/CIO/CDO 三列读成组织汇报链（CEO→CIO→CDO）；三列是并列的利益相关者类别。
- 中文稿当前引用的 figs/g238_fig4-1.svg 把图改成 17 项无归属清单并混入表 4-1 的内容，不能据此判断目标归属。

## 元素

```json
[
  {
    "id": "st_ceo",
    "label_en": "CEO",
    "label_zh": "首席执行官（CEO）",
    "type": "stakeholder",
    "parent": null,
    "level": 1,
    "position": "左列",
    "description_zh": "追求 4 项业务结果类目标。"
  },
  {
    "id": "st_cio",
    "label_en": "CIO",
    "label_zh": "首席信息官（CIO）",
    "type": "stakeholder",
    "parent": null,
    "level": 1,
    "position": "中列",
    "description_zh": "追求 7 项平台、运营与安全类目标。"
  },
  {
    "id": "st_cdo",
    "label_en": "CDO",
    "label_zh": "首席数据官（CDO）",
    "type": "stakeholder",
    "parent": null,
    "level": 1,
    "position": "右列",
    "description_zh": "追求 3 项数据价值、质量与民主化目标。"
  },
  {
    "id": "g_customer_satisfaction",
    "label_en": "Improve Customer or Partner Satisfaction",
    "label_zh": "提升客户或伙伴满意度",
    "type": "goal",
    "parent": "st_ceo",
    "level": 2,
    "order": 1,
    "description_zh": "表 4-1 编号 9；KPI 为 NPS。"
  },
  {
    "id": "g_operational_efficiency",
    "label_en": "Improve Operational Efficiency",
    "label_zh": "提升运营效率",
    "type": "goal",
    "parent": "st_ceo",
    "level": 2,
    "order": 2,
    "description_zh": "表 4-1 编号 10；KPI 为自动化功能数量。"
  },
  {
    "id": "g_regulations",
    "label_en": "Comply with Regulations (Privacy, Solvency II, etc.)",
    "label_zh": "遵守法规（隐私、偿付能力 II 等）",
    "type": "goal",
    "parent": "st_ceo",
    "level": 2,
    "order": 3,
    "description_zh": "表 4-1 编号 1；涉及 GDPR、Solvency II。"
  },
  {
    "id": "g_innovation",
    "label_en": "Leverage Innovation Opportunities",
    "label_zh": "利用创新机会",
    "type": "goal",
    "parent": "st_ceo",
    "level": 2,
    "order": 4,
    "description_zh": "表 4-1 编号 11；KPI 为创新功能。"
  },
  {
    "id": "g_data_asset",
    "label_en": "Store Data as an Asset including Metadata",
    "label_zh": "将数据作为资产存储（含元数据）",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 1,
    "description_zh": "表 4-1 编号 14。"
  },
  {
    "id": "g_time_to_market",
    "label_en": "Reduce Use-Case Time-to-Market",
    "label_zh": "缩短用例上市时间",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 2,
    "description_zh": "表 4-1 编号 13。"
  },
  {
    "id": "g_tco",
    "label_en": "Reduce Total Cost of Ownership",
    "label_zh": "降低总拥有成本",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 3,
    "description_zh": "表 4-1 编号 12。"
  },
  {
    "id": "g_security",
    "label_en": "Comply with Security",
    "label_zh": "遵守安全",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 4,
    "description_zh": "表 4-1 把它拆为编号 2–5：数据分级与加密、数据泄露、身份与访问管理、基础设施基线。"
  },
  {
    "id": "g_qos",
    "label_en": "Guarantee Quality of Service",
    "label_zh": "保证服务质量",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 5,
    "description_zh": "表 4-1 编号 8。"
  },
  {
    "id": "g_digital_innovation",
    "label_en": "Support Digital and Data Innovation",
    "label_zh": "支撑数字与数据创新",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 6,
    "description_zh": "表 4-1 编号 17。"
  },
  {
    "id": "g_interoperability",
    "label_en": "Provide Interoperability between Systems",
    "label_zh": "提供系统间互操作性",
    "type": "goal",
    "parent": "st_cio",
    "level": 2,
    "order": 7,
    "description_zh": "表 4-1 编号 16。"
  },
  {
    "id": "g_new_data_value",
    "label_en": "Generate Business Value Leveraging New Data Capabilities (e.g., Data Science)",
    "label_zh": "借助新数据能力（如数据科学）创造业务价值",
    "type": "goal",
    "parent": "st_cdo",
    "level": 2,
    "order": 1,
    "description_zh": "表 4-1 编号 15。"
  },
  {
    "id": "g_data_quality",
    "label_en": "Data Quality is Under Control",
    "label_zh": "数据质量受控",
    "type": "goal",
    "parent": "st_cdo",
    "level": 2,
    "order": 2,
    "description_zh": "表 4-1 编号 6。"
  },
  {
    "id": "g_democratize",
    "label_en": "Democratize Use of Data",
    "label_zh": "数据民主化使用",
    "type": "goal",
    "parent": "st_cdo",
    "level": 2,
    "order": 3,
    "description_zh": "表 4-1 编号 7。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "纵长矩形 + 列顶名称 + 右上角双圆图标",
    "meaning_zh": "利益相关者（CEO / CIO / CDO）",
    "explicit": false
  },
  {
    "symbol": "淡紫色切角八角形 + 右上角同心圆靶心图标",
    "meaning_zh": "目标 Goal",
    "explicit": false
  },
  {
    "symbol": "目标位于某列内",
    "meaning_zh": "该目标由这一列的利益相关者追求",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "三列并排：左列 CEO（4 个目标）、中列 CIO（7 个目标）、右列 CDO（3 个目标）。每列是一个纵长的 Stakeholder 框，目标自上而下堆叠并留白；列高不齐，CIO 列最高。"
}
```

## 相关图

```json
[
  {
    "target": "G238/fig2-1",
    "relation": "related",
    "note_zh": "目标说明 BI 与分析能力要达成的结果，图 2-1 给出实现这些目标的业务/应用功能，二者共同构成 4.1–4.3 的参考模型。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "原图只有 14 个目标框，表 4-1 有 17 项；本分析按原图 14 个元素转录，并在描述中标注表 4-1 编号，未把安全 4 个子目标拆成图中元素。",
    "Stakeholder 框与 Goal 框之间未画连线，按 ArchiMate 语义应为关联/组成；这里用 parent 表示列包含。",
    "CDO 一列下方留有大片空白，原图未说明是留给未来目标还是纯版式。"
  ],
  "analyzed_from": [
    "英文 PDF 第 28 页图 4-1 截图与 3×3 放大分块",
    "英文 PDF 第 28–30 页表 4-1（目标、说明、KPI）",
    "中文稿 G238e_信息架构_商业智能与分析.md 第 390–414 行",
    "figs/g238_fig4-1.svg 源码"
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
