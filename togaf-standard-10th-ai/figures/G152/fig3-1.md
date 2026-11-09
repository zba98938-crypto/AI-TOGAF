# G152/fig3-1 · 业务风险领域与网络风险领域（业务栈）

> 当前图示解析：[Markdown](../../architecture/diagrams/G152/fig3-1.md) · [JSON](../../architecture/diagrams/G152/fig3-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G152e.pdf`；SHA-256：`919c53bfa4259a4b3a9686762f37c0576a1cd2f8e77e74648826d9f9c84ed6e0`。

## 原图 · PDF 第 22 页

![英文原图](../assets/G152/fig3-1-p0022.png)

PDF 坐标：`[48.2, 36.0, 563.8, 345.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business Stack
{ Business Value Chains
{ Business Capabilities
Business Risk
Business Processes
Business Services
(Logical information Services)
ICT Infrastructure
Cyber Risk
(Physical Networks/Platforms)
aa
```

## 概要（历史解释；局部修正见上）

把企业业务栈分为 7 层，并用“业务风险管理/网络风险管理”两条大括号划出各自覆盖的层次。

## 目的（历史解释；局部修正见上）

为 ERM 讨论提供“风险可出现在业务栈任何层级”的底图：先让读者看清从业务价值链到技术组件的 7 层结构，再指出业务风险主要在上 4 层管理、网络风险主要在下 3 层管理，而服务管理、人员与支持服务/流程三条竖带横跨两者。

## 阅读顺序（历史解释；局部修正见上）

自上而下读中央的 7 个浅蓝层：Business Value Chains → Business Capabilities → Business Processes → Business Services → Applications → ICT Infrastructure → Technical Components；层间紫色箭头向下，表示上层由下层支撑/逐层落地。然后看右侧两个大括号：上括号覆盖前 4 层，标 Business Risk Management；下括号覆盖后 3 层，标 Cyber Risk Management。最后看左侧三条竖带，它们从顶部贯穿到底部，不属于任何单一层。

## 关键含义（历史解释；局部修正见上）

- 业务栈共 7 层：业务价值链、业务能力、业务流程、业务服务、应用（逻辑信息服务）、ICT 基础设施（物理网络/平台）、技术组件（标准、产品与工具）。
- 右侧两个大括号把栈切成两段风险管理范围：上 4 层为业务风险管理，下 3 层为网络风险管理。
- 切分点落在 Business Services 与 Applications 之间，但两者之间仍有一个向下箭头，说明栈本身是连续的，分段只是管理视角，不是断开的两个栈。
- 左侧三条竖带（Service Management、People: Roles/Responsibilities/Knowledge/Skills/Competencies、Support Services & Processes）横跨业务与网络两段，是贯穿全栈的支撑性关注点。
- 所有层间箭头都向下，表达自上而下的分解与依赖：业务价值链条依赖业务能力，能力通过流程与服务落地，再依赖应用、ICT 与技术组件实现。
- 正文据此指出风险可在业务栈任何层级出现，但风险管理始终由业务价值评估自上而下驱动；因此业务风险与网络风险的划分是“风险在何处被评估”，而不是两套互不相干的风险。

## 层级（历史解释；局部修正见上）

三层。第 1 层是整体 Business Stack（图内左上角标题，未画成框）；第 2 层是两个风险管理范围（Business Risk Management、Cyber Risk Management）；第 3 层是 7 个栈层。左侧 Service Management 是独立的纵向容器，内含 People 带与 Support Services & Processes 带，二者与 7 个栈层是交叉关系而非上下级。

## 线条含义（历史解释；局部修正见上）

紫色细箭头自上而下连接相邻层，表示逐层支撑/分解，箭头指向下层。右侧大括号无箭头，是范围标注，不表示流向。左侧三条竖带没有任何连线，靠“贯穿两组”的位置表达横切关系。Business Services → Applications 的箭头跨过大括号分界线，是唯一跨越业务/网络分段的箭头。

## 易误读点（历史解释；局部修正见上）

- 不要把两个大圆角框读成两个独立的栈：它们是同一业务栈上的两个风险管理范围，中间仍有箭头相连。
- 不要把左侧三条竖带当成第 8–10 层或流程步骤：它们横跨全部 7 层，是横向的支撑性关注点。
- “业务风险”不等于只发生在业务架构，“网络风险”也不等于只发生在技术层；图中只是用括号划分主要管理范围。
- 层间箭头不是数据流，而是上层依赖下层的分解/支撑方向。
- Service Management 是包含 People 与 Support Services & Processes 的外层带，不要把三者读成并列的三条独立带。

## 元素

```json
[
  {
    "id": "business_stack",
    "label_en": "Business Stack",
    "label_zh": "业务栈",
    "type": "note",
    "parent": null,
    "position": "图左上角大号灰字",
    "description_zh": "图内标题，不是框；图题另见 Figure 3-1。"
  },
  {
    "id": "br_group",
    "label_en": "Business Risk Management",
    "label_zh": "业务风险管理",
    "type": "group",
    "parent": null,
    "position": "上半部大圆角框",
    "description_zh": "右侧大括号覆盖 Business Value Chains 至 Business Services 四层。"
  },
  {
    "id": "cr_group",
    "label_en": "Cyber Risk Management",
    "label_zh": "网络风险管理",
    "type": "group",
    "parent": null,
    "position": "下半部大圆角框",
    "description_zh": "右侧大括号覆盖 Applications 至 Technical Components 三层。"
  },
  {
    "id": "service_management",
    "label_en": "Service Management",
    "label_zh": "服务管理",
    "type": "group",
    "parent": null,
    "position": "左侧纵向带，贯穿两组",
    "description_zh": "浅蓝外层竖带，内含人员带与支持服务/流程带。"
  },
  {
    "id": "people",
    "label_en": "People: Roles, Responsibilities, Knowledge, Skills, Competencies",
    "label_zh": "人员：角色、职责、知识、技能、胜任力",
    "type": "capability",
    "parent": "service_management",
    "position": "服务管理带内左侧"
  },
  {
    "id": "support_services",
    "label_en": "Support Services & Processes",
    "label_zh": "支持服务与流程",
    "type": "capability",
    "parent": "service_management",
    "position": "服务管理带内右侧"
  },
  {
    "id": "value_chains",
    "label_en": "Business Value Chains",
    "label_zh": "业务价值链",
    "type": "value_stream",
    "parent": "br_group",
    "level": 1,
    "order": 1
  },
  {
    "id": "capabilities",
    "label_en": "Business Capabilities",
    "label_zh": "业务能力",
    "type": "capability",
    "parent": "br_group",
    "level": 2,
    "order": 2
  },
  {
    "id": "processes",
    "label_en": "Business Processes",
    "label_zh": "业务流程",
    "type": "process",
    "parent": "br_group",
    "level": 3,
    "order": 3
  },
  {
    "id": "business_services",
    "label_en": "Business Services",
    "label_zh": "业务服务",
    "type": "service",
    "parent": "br_group",
    "level": 4,
    "order": 4
  },
  {
    "id": "applications",
    "label_en": "Applications (Logical Information Services)",
    "label_zh": "应用（逻辑信息服务）",
    "type": "application",
    "parent": "cr_group",
    "level": 5,
    "order": 5
  },
  {
    "id": "ict_infrastructure",
    "label_en": "ICT Infrastructure (Physical Networks/Platforms)",
    "label_zh": "ICT 基础设施（物理网络/平台）",
    "type": "technology",
    "parent": "cr_group",
    "level": 6,
    "order": 6
  },
  {
    "id": "technical_components",
    "label_en": "Technical Components (Standards, Products & Tools)",
    "label_zh": "技术组件（标准、产品与工具）",
    "type": "technology",
    "parent": "cr_group",
    "level": 7,
    "order": 7
  }
]
```

## 关系

```json
[
  {
    "id": "r1",
    "from": "value_chains",
    "to": "capabilities",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "紫色向下箭头，上层价值链依赖业务能力。"
  },
  {
    "id": "r2",
    "from": "capabilities",
    "to": "processes",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r3",
    "from": "processes",
    "to": "business_services",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r4",
    "from": "business_services",
    "to": "applications",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "跨过业务/网络风险管理分界线的唯一直连箭头。"
  },
  {
    "id": "r5",
    "from": "applications",
    "to": "ict_infrastructure",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r6",
    "from": "ict_infrastructure",
    "to": "technical_components",
    "type": "dependency",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r7",
    "from": "service_management",
    "to": "br_group",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "左侧竖带贯穿业务风险管理段，未画连线，由位置表达横切关系。"
  },
  {
    "id": "r8",
    "from": "service_management",
    "to": "cr_group",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同一竖带继续贯穿网络风险管理段。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_stack",
    "kind": "sequence",
    "name_zh": "业务栈自上而下的支撑链",
    "steps": [
      "value_chains",
      "capabilities",
      "processes",
      "business_services",
      "applications",
      "ict_infrastructure",
      "technical_components"
    ],
    "description_zh": "沿 6 个向下箭头读取，表示从业务价值到技术组件的逐层落地。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色圆角长条",
    "meaning_zh": "业务栈的一个层次",
    "explicit": false
  },
  {
    "symbol": "紫色向下细箭头",
    "meaning_zh": "相邻层之间的逐层支撑/分解方向（上层依赖下层）",
    "explicit": false
  },
  {
    "symbol": "右侧大括号 + 文字",
    "meaning_zh": "风险管理范围：上括号=Business Risk Management（4 层），下括号=Cyber Risk Management（3 层）",
    "explicit": false
  },
  {
    "symbol": "左侧竖向浅蓝带",
    "meaning_zh": "横跨业务与网络两段的支撑性关注点（服务管理、人员、支持服务与流程）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "中央一列 7 个横向长条框自上而下堆叠；右侧两个大括号加文字标签；左侧三条竖排带从顶部贯穿到底部；整体被两个上下相邻的大圆角框包住。"
}
```

## 相关图

```json
[
  {
    "target": "G152/fig3-2",
    "relation": "precedes",
    "note_zh": "本图给出风险所在的业务栈层次，图 3-2 随即展开 SABSA 运营风险模型（威胁/机会与资产）。"
  },
  {
    "target": "G152/fig1-1",
    "relation": "related",
    "note_zh": "图 1-1 中央列的 Key Risk Areas / Business Impact、Business Risk Model 等概念与本图的业务/网络风险分层相呼应。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图内除图题外没有图例；“层间箭头表示逐层支撑”由箭头方向与 SABSA 业务栈的通常含义推断。",
    "“Service Management”外层带是否把 People 与 Support Services & Processes 二者都包含在内，按边框包含关系判读；原图无说明文字。"
  ],
  "analyzed_from": [
    "英文 PDF 第 22 页原图截图（220 dpi）及 2x2 放大分块",
    "英文 PDF 第 22 页左下与左侧竖带局部放大",
    "英文 PDF 第 21–22 页正文",
    "中文稿 G152e_将风险与安全融入TOGAF企业架构.md 第 188、192 行"
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
