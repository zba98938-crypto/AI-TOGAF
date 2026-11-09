# G234/fig4-4 · 元数据管理 IT 方案

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-4.md) · [JSON](../../architecture/diagrams/G234/fig4-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 25 页

![英文原图](../assets/G234/fig4-4-p0025.png)

PDF 坐标：`[61.1, 457.2, 550.9, 651.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Quality
Business Requirements
Finance
HR
Marketing
Documentation
nce)
BBs
Ba
Security,
iy
aA
Privacy,
Compliance
|
Governance
Metadata Management IT Solution
Metadata Management
Metadata Management
Management
1. Technology
Data Model
3. Processes (Workflows)
—
-=-
=
——
```

## 本次原图核对

本次直接从英文 PDF 第 25 页提取的图显示 Technology、Data Model、Processes (Workflows) 三部分；消除了旧英文 PNG 错配问题。历史资产仍保留原有冲突。

## 概要（历史解释；局部修正见上）

元数据管理 IT 方案由技术、数据模型、流程三部分相加组成，向上支撑市场、财务、人力等业务需求。

## 目的（历史解释；局部修正见上）

第 4.3 节开篇把“元数据管理 IT 方案”定义为技术（功能集）、数据模型与流程（更新与校验工作流）的组合，并用图说明它不是单一工具，而是三块能力相加后共同支撑业务需求。

## 阅读顺序（历史解释；局部修正见上）

先看上方米色 3D 箱 Business Requirements：内部按部门分组（Marketing、Finance、HR、…），每个部门用多个人物图标表示不同关注点。再看下方蓝色 3D 箱 Metadata Management IT Solution：三个青色面板从左到右是 1. Technology、2. Data Model、3. Processes (Workflows)，面板之间用 “+” 连接。中间一条向上箭头表示方案支撑业务需求。右侧图例解释人物颜色。

## 关键含义（历史解释；局部修正见上）

- 方案 = 技术（功能集）+ 数据模型 + 流程（元数据更新与校验工作流），三者是相加关系，不是先后步骤。
- 1. Technology 面板是一张元数据管理工具界面截图，代表工具能力，不展开具体技术组件。
- 2. Data Model 面板是一张实体关系图截图，对应正文“澄清要记录的元数据资产及其关系”。
- 3. Processes (Workflows) 面板是一张工作流截图，对应元数据校验与更新流程。
- 业务需求侧以部门（Marketing、Finance、HR、…）和四类角色（Quality、Documentation、Security/Privacy/Compliance、Governance）表示，说明同一方案要同时满足多部门、多关注点。
- 全图只有一条箭头，方向是方案 → 业务需求，表示“支撑”，而不是需求 → 方案。

## 层级（历史解释；局部修正见上）

两层：Business Requirements（业务侧）在上，Metadata Management IT Solution（方案侧）在下；方案内三个面板并列，面板本身不细分组件。

## 线条含义（历史解释；局部修正见上）

中间向上箭头表示方案支撑业务需求；“+” 号表示三个面板组合成方案，不是数据流，也不是流程顺序。

## 易误读点（历史解释；局部修正见上）

- 不要把三个面板读成实施步骤 1→2→3；“+” 表示同时具备。
- 不要以为箭头表示业务需求输入方案；箭头由方案指向业务需求。
- 不要把人物图标当成具体人员编制，它们是关注点/角色类别，颜色由图例定义。
- 中文稿引用的 g234e_fig4-4_zh.png 实际是图 4-3，不能据它理解本图；本图应以英文原图为准。

## 元素

```json
[
  {
    "id": "business_requirements",
    "label_en": "Business Requirements",
    "label_zh": "业务需求",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "上方米色 3D 箱"
  },
  {
    "id": "dept_marketing",
    "label_en": "Marketing",
    "label_zh": "市场",
    "type": "organization_unit",
    "parent": "business_requirements",
    "level": 2,
    "position": "业务需求箱左一"
  },
  {
    "id": "dept_finance",
    "label_en": "Finance",
    "label_zh": "财务",
    "type": "organization_unit",
    "parent": "business_requirements",
    "level": 2,
    "position": "业务需求箱左二"
  },
  {
    "id": "dept_hr",
    "label_en": "HR",
    "label_zh": "人力资源",
    "type": "organization_unit",
    "parent": "business_requirements",
    "level": 2,
    "position": "业务需求箱左三"
  },
  {
    "id": "dept_other",
    "label_en": "…",
    "label_zh": "其他部门（省略号）",
    "type": "organization_unit",
    "parent": "business_requirements",
    "level": 2,
    "position": "业务需求箱最右",
    "description_zh": "原图仅以省略号表示还有其他部门。"
  },
  {
    "id": "it_solution",
    "label_en": "Metadata Management IT Solution",
    "label_zh": "元数据管理 IT 方案",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "下方蓝色 3D 箱"
  },
  {
    "id": "panel_technology",
    "label_en": "Metadata Management 1. Technology",
    "label_zh": "元数据管理 1. 技术",
    "type": "application",
    "parent": "it_solution",
    "level": 2,
    "position": "方案箱左面板",
    "description_zh": "面板内容为一张元数据工具界面截图。"
  },
  {
    "id": "panel_data_model",
    "label_en": "Metadata Management 2. Data Model",
    "label_zh": "元数据管理 2. 数据模型",
    "type": "artifact",
    "parent": "it_solution",
    "level": 2,
    "position": "方案箱中面板",
    "description_zh": "面板内容为一张实体关系图截图。"
  },
  {
    "id": "panel_processes",
    "label_en": "Metadata Management 3. Processes (Workflows)",
    "label_zh": "元数据管理 3. 流程（工作流）",
    "type": "process",
    "parent": "it_solution",
    "level": 2,
    "position": "方案箱右面板",
    "description_zh": "面板内容为一张工作流截图。"
  },
  {
    "id": "leg_quality",
    "label_en": "Quality",
    "label_zh": "质量",
    "type": "role",
    "parent": null,
    "level": 2,
    "position": "右侧图例第一行"
  },
  {
    "id": "leg_documentation",
    "label_en": "Documentation",
    "label_zh": "文档化",
    "type": "role",
    "parent": null,
    "level": 2,
    "position": "右侧图例第二行"
  },
  {
    "id": "leg_security_privacy_compliance",
    "label_en": "Security, Privacy, Compliance",
    "label_zh": "安全、隐私、合规",
    "type": "role",
    "parent": null,
    "level": 2,
    "position": "右侧图例第三行"
  },
  {
    "id": "leg_governance",
    "label_en": "Governance",
    "label_zh": "治理",
    "type": "role",
    "parent": null,
    "level": 2,
    "position": "右侧图例第四行"
  }
]
```

## 关系

```json
[
  {
    "from": "it_solution",
    "to": "business_requirements",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "方案箱上方的单箭头指向业务需求，表示 IT 方案支撑业务需求。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色人物图标 Quality",
    "meaning_zh": "质量关注点",
    "explicit": true
  },
  {
    "symbol": "米色人物图标 Documentation",
    "meaning_zh": "文档化关注点",
    "explicit": true
  },
  {
    "symbol": "粉色人物图标 Security, Privacy, Compliance",
    "meaning_zh": "安全、隐私、合规关注点",
    "explicit": true
  },
  {
    "symbol": "蓝色人物图标 Governance",
    "meaning_zh": "治理关注点",
    "explicit": true
  },
  {
    "symbol": "面板之间的 “+”",
    "meaning_zh": "三部分组合成方案",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "BT",
  "description_zh": "上下两个 3D 箱：上方 Business Requirements 横跨全宽，下方 Metadata Management IT Solution 横跨全宽；方案箱内三个面板横向并列，右侧图例竖排四行。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-3",
    "relation": "follows",
    "note_zh": "图 4-3 的两种质量流程模式是本图 Processes (Workflows) 面板的上文"
  },
  {
    "target": "G234/fig4-5",
    "relation": "complements",
    "note_zh": "图 4-5 给出数据模型面板应包含的关键元数据资产"
  },
  {
    "target": "G234/fig3-1",
    "relation": "related",
    "note_zh": "图 3-1 的应用功能清单说明本图 IT 方案应具备的能力范围"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "三个面板内的截图文字太小，无法转录工具界面、实体关系图与工作流的具体标签；本分析只记录面板标题与截图类型。",
    "右侧图例只解释人物颜色，图中并未画出颜色与部门的一一对应表；无法确定每个部门内各色人物的具体数量与含义。"
  ],
  "analyzed_from": [
    "英文 PDF 第 25 页原图截图（2x2 放大分块）",
    "英文 PDF 第 25 页正文",
    "中文稿 G234e_信息架构_元数据管理.md 第 259–291 行",
    "figs/g234e_fig4-4_en.png、figs/zh/g234e_fig4-4_zh.png"
  ],
  "date": "2026-10-31"
}
```

## 既有来源冲突

```json
[
  {
    "id": "source-g234-fig4-4",
    "figure_id": "G234/fig4-4",
    "status": "observed-conflict",
    "description": "实际英文 PNG 显示规范式／众包式两栏（图4-3内容），正文与JSON语义为技术、数据模型、流程三要素（图4-4）。已有faithful标签不能采信为本轮核验。",
    "evidence": [
      "G234 §4.2.2–4.3",
      "figs/g234e_fig4-4_en.png",
      "figs/ai/G234/fig4-4.json"
    ],
    "resolution": "保留正文可证实三要素与冲突，来源结构模板待取得可信图4-4；不修改原资料。"
  }
]
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "specific-findings-only",
  "all_source_pages_valid": true
}
```
