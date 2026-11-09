# G152/fig5-2 · 使用 ArchiMate 语言对风险与安全建模

> 当前图示解析：[Markdown](../../architecture/diagrams/G152/fig5-2.md) · [JSON](../../architecture/diagrams/G152/fig5-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G152e.pdf`；SHA-256：`919c53bfa4259a4b3a9686762f37c0576a1cd2f8e77e74648826d9f9c84ed6e0`。

## 原图 · PDF 第 43 页

![英文原图](../assets/G152/fig5-2-p0043.png)

PDF 坐标：`[61.1, 36.0, 550.9, 346.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Re
_
—_
ey
en a
—_
—_
y
—
```

## 概要（历史解释；局部修正见上）

用 ArchiMate 元素与关系画出威胁主体、威胁事件、损失事件到风险，再到控制目标、安全需求与控制措施的链条。

## 目的（历史解释；局部修正见上）

证明 ArchiMate 语言足以表达 ISM 与 ERM：把抽象的威胁、脆弱性、风险、控制目标、安全需求、控制措施与安全原则落成有类型、有关系、可被工具解析的模型，并用两个 grouping 说明资产与控制措施的实现都由多层元素构成。

## 阅读顺序（历史解释；局部修正见上）

先读左上方的威胁链：Threat agent → Threat event → Loss event → Risk。再看 Vulnerability：它与 Threat event、Loss event 相连，并向下连到 Asset at risk。右侧是动机与控制层：Risk / security driver 位于 Risk 与 Security control objective 之上；Risk 向下连 Risk control objective；Security control objective 特化 Risk control objective；Security requirement 与 Security principle 通过空心三角实现 Security control objective；Control measure 实现 Security requirement，并被 Security principle 约束。底部两个灰色 grouping 分别是 Asset at risk 与 Implementation of control measure，Control measure 向下由实现组实现；两组之间还有一条虚线箭头由右向左指回资产组。

## 关键含义（历史解释；局部修正见上）

- 威胁链是单向的：Threat agent（威胁主体）关联 Threat event（威胁事件），威胁事件触发 Loss event（损失事件），损失事件再触发 Risk（风险）。
- Vulnerability（脆弱性）位于威胁链与资产之间：它关联 Threat event、Loss event，并向下连到 Asset at risk，表示被利用的弱点使威胁作用于资产。
- Risk / security driver 是风险与安全控制目标的动因，位于二者之上；图中它与 Risk、Security control objective 都是无箭头的关联线。
- Security control objective 用空心三角指向 Risk control objective，表示前者是后者的一种特化（安全控制目标是风险控制目标的专门化）。
- 控制侧形成一条实现链：Implementation of control measure → Control measure → Security requirement → Security control objective，三段都是点线加空心三角（realization）；Security principle 也以实现关系连到 Security control objective。
- Control measure 与 Security principle 之间是实线空心三角（图中唯一的特化式箭头），可读作控制措施落实安全原则；该线型与 ArchiMate 标准 realization 用点线的习惯不同，需按原图判读。
- Asset at risk 与 Implementation of control measure 都是 grouping，内部由黄/青/绿多层元素和“…”组成，表示资产与控制措施实现是跨业务、应用、技术层的集合，而不是单一元素。
- Risk / security domain 是覆盖中部与底部的 grouping，通过多条连线把风险、控制目标、安全需求、资产与实现组收进同一风险/安全域语境；两底部 grouping 之间的虚线箭头由 Implementation of control measure 指向 Asset at risk，表示控制措施的实现作用于处于风险中的资产。

## 层级（历史解释；局部修正见上）

四层。上层是风险与动机：Threat agent、Threat event、Loss event、Risk、Risk/security driver、Vulnerability；中层是控制：Risk control objective、Security control objective、Security requirement、Control measure、Security principle；下层是两个 grouping：Asset at risk、Implementation of control measure（各含未命名的多层实例与“…”）；Risk / security domain 作为横跨中下层的 grouping。分组内的堆叠元素没有名称，只是实例示意。

## 线条含义（历史解释；局部修正见上）

实线无箭头＝关联；实线实心箭头＝触发（Threat event→Loss event、Loss event→Risk）；点线＋空心三角＝实现（realization），方向由下向上（实现组→控制措施→安全需求→安全控制目标，安全原则→安全控制目标）；实线＋空心三角＝特化（Security control objective→Risk control objective；Control measure→Security principle 也是这种画法）；虚线＋小空心箭头＝底部两组之间由实现组指向资产组。带箭头的线方向都以箭头为准，不能按上下位置猜。

## 易误读点（历史解释；局部修正见上）

- 空心三角不是数据流或“继承箭头”的泛称：在 ArchiMate 中它表示实现（点线）或特化（实线），方向是从具体/实现者指向被实现/被特化者。
- 不要把 Security control objective → Risk control objective 读反：是安全控制目标特化风险控制目标，不是风险目标派生安全目标。
- 底部的 Asset at risk 与 Implementation of control measure 是 grouping，不是两个普通元素；框内未命名的黄/青/绿堆叠图形是实例示意，不要当成新的命名概念。
- Risk / security domain 也是 grouping（灰色双框），不是参与者或系统。
- 两组之间的虚线箭头指向左侧的资产组，即“控制措施的实现 → 资产”，不是资产流向实现。
- “威胁主体 → 威胁事件”没有箭头，只是关联；不要把它读成触发。
- 中文图把“威胁事件 → 损失事件”的箭头擦坏了，若只看中文图会误以为两者没有因果关系。

## 元素

```json
[
  {
    "id": "threat_agent",
    "label_en": "Threat agent",
    "label_zh": "威胁主体",
    "type": "actor",
    "parent": null,
    "position": "左上",
    "notation_type": "Business Actor",
    "description_zh": "黄色矩形，右上角人物图标。"
  },
  {
    "id": "threat_event",
    "label_en": "Threat event",
    "label_zh": "威胁事件",
    "type": "event",
    "parent": null,
    "position": "顶左二",
    "notation_type": "Business Event",
    "description_zh": "黄色事件形（左侧凹口）。"
  },
  {
    "id": "loss_event",
    "label_en": "Loss event",
    "label_zh": "损失事件",
    "type": "event",
    "parent": null,
    "position": "顶中",
    "notation_type": "Business Event"
  },
  {
    "id": "vulnerability",
    "label_en": "Vulnerability",
    "label_zh": "脆弱性",
    "type": "risk",
    "parent": null,
    "position": "左上中",
    "notation_type": "Assessment",
    "description_zh": "粉色框，右上角放大镜图标。"
  },
  {
    "id": "risk",
    "label_en": "Risk",
    "label_zh": "风险",
    "type": "risk",
    "parent": null,
    "position": "右上",
    "notation_type": "Risk",
    "description_zh": "粉色框，右上角风险图标。"
  },
  {
    "id": "risk_security_driver",
    "label_en": "Risk / security driver",
    "label_zh": "风险/安全驱动因素",
    "type": "goal",
    "parent": null,
    "position": "最右上",
    "notation_type": "Driver",
    "description_zh": "粉色框，右上角驱动因素图标。"
  },
  {
    "id": "risk_control_objective",
    "label_en": "Risk control objective",
    "label_zh": "风险控制目标",
    "type": "goal",
    "parent": null,
    "position": "右中",
    "notation_type": "Goal",
    "description_zh": "紫色框，右上角目标图标。"
  },
  {
    "id": "security_control_objective",
    "label_en": "Security control objective",
    "label_zh": "安全控制目标",
    "type": "goal",
    "parent": null,
    "position": "右中偏右",
    "notation_type": "Goal"
  },
  {
    "id": "security_requirement",
    "label_en": "Security requirement",
    "label_zh": "安全需求",
    "type": "requirement",
    "parent": null,
    "position": "中右",
    "notation_type": "Requirement",
    "description_zh": "紫色框，右上角文档图标。"
  },
  {
    "id": "control_measure",
    "label_en": "Control measure",
    "label_zh": "控制措施",
    "type": "risk",
    "parent": null,
    "position": "中右偏下",
    "notation_type": "Requirement",
    "description_zh": "紫色框，右上角文档图标；在模型中承担控制措施角色。"
  },
  {
    "id": "security_principle",
    "label_en": "Security principle",
    "label_zh": "安全原则",
    "type": "principle",
    "parent": null,
    "position": "右下",
    "notation_type": "Principle",
    "description_zh": "紫色框，右上角感叹号方框图标。"
  },
  {
    "id": "risk_security_domain",
    "label_en": "Risk / security domain",
    "label_zh": "风险/安全域",
    "type": "group",
    "parent": null,
    "position": "中央",
    "notation_type": "Grouping",
    "description_zh": "灰色双矩形（带标题条），figures 中作为语境容器。"
  },
  {
    "id": "asset_at_risk",
    "label_en": "Asset at risk",
    "label_zh": "处于风险中的资产",
    "type": "group",
    "parent": null,
    "position": "左下",
    "notation_type": "Grouping",
    "description_zh": "灰色虚线 grouping，内含黄色业务元素、青色应用元素与白色虚线“…”文件夹。"
  },
  {
    "id": "implementation_of_control_measure",
    "label_en": "Implementation of control measure",
    "label_zh": "控制措施的实施",
    "type": "group",
    "parent": null,
    "position": "右下",
    "notation_type": "Grouping",
    "description_zh": "灰色虚线 grouping，内含黄/青/绿三层元素与“…”文件夹。"
  },
  {
    "id": "ellipsis_asset",
    "label_en": "...",
    "label_zh": "省略的其他资产元素",
    "type": "note",
    "parent": "asset_at_risk",
    "position": "资产组底部",
    "description_zh": "白色虚线文件夹内的省略号。"
  },
  {
    "id": "ellipsis_impl",
    "label_en": "...",
    "label_zh": "省略的其他实现元素",
    "type": "note",
    "parent": "implementation_of_control_measure",
    "position": "实现组底部",
    "description_zh": "白色虚线文件夹内的省略号。"
  }
]
```

## 关系

```json
[
  {
    "id": "r1",
    "from": "threat_agent",
    "to": "threat_event",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "威胁主体与威胁事件之间的水平实线，无箭头。"
  },
  {
    "id": "r2",
    "from": "threat_event",
    "to": "loss_event",
    "type": "triggering",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "实心箭头。"
  },
  {
    "id": "r3",
    "from": "threat_event",
    "to": "vulnerability",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "垂直实线。"
  },
  {
    "id": "r4",
    "from": "vulnerability",
    "to": "loss_event",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "斜线，原图未画箭头。"
  },
  {
    "id": "r5",
    "from": "vulnerability",
    "to": "asset_at_risk",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "垂直实线穿过画面下部，进入资产组。"
  },
  {
    "id": "r6",
    "from": "loss_event",
    "to": "risk",
    "type": "triggering",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "水平实心箭头。"
  },
  {
    "id": "r7",
    "from": "loss_event",
    "to": "risk_security_domain",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "损失事件向下连到风险/安全域。"
  },
  {
    "id": "r8",
    "from": "loss_event",
    "to": "asset_at_risk",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "长垂直线，从损失事件向下进入资产组。"
  },
  {
    "id": "r9",
    "from": "risk",
    "to": "risk_control_objective",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "垂直实线。"
  },
  {
    "id": "r10",
    "from": "risk_security_driver",
    "to": "risk",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "水平实线，无箭头。"
  },
  {
    "id": "r11",
    "from": "risk_security_driver",
    "to": "security_control_objective",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "垂直实线。"
  },
  {
    "id": "r12",
    "from": "security_control_objective",
    "to": "risk_control_objective",
    "type": "specialization",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "空心三角箭头指向风险控制目标。"
  },
  {
    "id": "r13",
    "from": "security_requirement",
    "to": "security_control_objective",
    "type": "realization",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "点线折向安全控制目标底部，空心三角。"
  },
  {
    "id": "r14",
    "from": "security_principle",
    "to": "security_control_objective",
    "type": "realization",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "从安全原则顶部垂直向上的点线，空心三角。"
  },
  {
    "id": "r15",
    "from": "control_measure",
    "to": "security_requirement",
    "type": "realization",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "垂直点线，空心三角指向安全需求底部。"
  },
  {
    "id": "r16",
    "from": "control_measure",
    "to": "security_principle",
    "type": "realization",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "实线空心三角指向安全原则（线型与 realization 的点线习惯不同，按原图记录）。"
  },
  {
    "id": "r17",
    "from": "implementation_of_control_measure",
    "to": "control_measure",
    "type": "realization",
    "explicit": true,
    "line": "dotted",
    "arrow": "forward",
    "description_zh": "从实现组向上到控制措施底部的点线，空心三角。"
  },
  {
    "id": "r18",
    "from": "risk_security_domain",
    "to": "vulnerability",
    "type": "association",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "点线折线，从脆弱性右侧连到域。"
  },
  {
    "id": "r19",
    "from": "risk_security_domain",
    "to": "risk",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "斜线。"
  },
  {
    "id": "r20",
    "from": "risk_security_domain",
    "to": "risk_control_objective",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "斜线。"
  },
  {
    "id": "r21",
    "from": "risk_security_domain",
    "to": "security_requirement",
    "type": "association",
    "explicit": true,
    "line": "dotted",
    "arrow": "none",
    "description_zh": "点线折线。"
  },
  {
    "id": "r22",
    "from": "risk_security_domain",
    "to": "asset_at_risk",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "斜线进入资产组。"
  },
  {
    "id": "r23",
    "from": "risk_security_domain",
    "to": "implementation_of_control_measure",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "none",
    "description_zh": "斜线进入实现组。"
  },
  {
    "id": "r24",
    "from": "implementation_of_control_measure",
    "to": "asset_at_risk",
    "type": "association",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "两组之间的水平虚线，小空心箭头指向左侧资产组。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_threat",
    "kind": "sequence",
    "name_zh": "威胁链",
    "steps": [
      "threat_agent",
      "threat_event",
      "loss_event",
      "risk"
    ],
    "description_zh": "威胁主体 → 威胁事件 → 损失事件 → 风险。"
  },
  {
    "id": "f_control",
    "kind": "sequence",
    "name_zh": "控制实现链",
    "steps": [
      "implementation_of_control_measure",
      "control_measure",
      "security_requirement",
      "security_control_objective"
    ],
    "description_zh": "Implementation of control measure → Control measure → Security requirement → Security control objective，均为实现关系。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色圆角框/事件形",
    "meaning_zh": "业务层元素：threat agent（actor）、threat event / loss event（event）",
    "explicit": false
  },
  {
    "symbol": "粉色框",
    "meaning_zh": "动机层元素：Risk（风险）、Risk/security driver（驱动因素）、Vulnerability（评估/脆弱性）",
    "explicit": false
  },
  {
    "symbol": "紫色框",
    "meaning_zh": "控制/需求层元素：控制目标、安全需求、控制措施、安全原则",
    "explicit": false
  },
  {
    "symbol": "灰色虚线框 grouping",
    "meaning_zh": "分组容器：Asset at risk、Implementation of control measure、Risk / security domain",
    "explicit": false
  },
  {
    "symbol": "实心箭头",
    "meaning_zh": "触发（triggering）",
    "explicit": false
  },
  {
    "symbol": "空心三角 + 点线",
    "meaning_zh": "实现（realization）",
    "explicit": false
  },
  {
    "symbol": "空心三角 + 实线",
    "meaning_zh": "特化（specialization）",
    "explicit": false
  },
  {
    "symbol": "右上角小图标（人物/靶心/文档/感叹号等）",
    "meaning_zh": "ArchiMate 元素类型图标",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "左上为威胁链（横向），右上为 Risk 与 Risk/security driver，右中为控制目标与安全需求/原则，中央为 Risk/security domain，左下与右下为两个 grouping，控制措施位于中右并向下连到实现组。"
}
```

## 相关图

```json
[
  {
    "target": "G152/fig1-1",
    "relation": "related",
    "note_zh": "图 1-1 中央列的 Risk、Vulnerability、Control Objectives 等概念在本图中被具体建模为 ArchiMate 元素。"
  },
  {
    "target": "G152/fig3-2",
    "relation": "related",
    "note_zh": "两图都在讲风险的正负结果与资产；图 3-2 是 SABSA 概念模型，本图是 ArchiMate 形式化模型。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "Control measure → Security principle 的连线是实线空心三角；按 ArchiMate 标准这更像 specialization，但语义上应为 realization（控制措施落实安全原则），本分析按 realization 记录并在描述中说明线型差异。",
    "Threat agent → Threat event、Vulnerability → Loss event、Risk/security driver → Risk 等线在原图中看不到箭头；本分析按无箭头关联记录，不排除箭头被形状边框遮挡。",
    "Risk / security domain 画成两个重叠的灰色矩形（带标题条），本分析按一个 grouping 记录。",
    "底部两个 grouping 内未命名的黄/青/绿堆叠图形只能判读为业务/应用/技术层实例示意，具体类型无法确认。",
    "“Implementation of control measure → Asset at risk” 的虚线小箭头方向按箭头尖端判读为向左。"
  ],
  "analyzed_from": [
    "英文 PDF 第 43 页原图截图（220 dpi）及 2x2、3x3 放大分块",
    "figs/g152e_fig5-2_en.png（1394×896，与 PDF 截图逐项比对）",
    "figs/zh/g152e_fig5-2_zh.png（逐项与英文原图比较）",
    "英文 PDF 第 42–43 页正文",
    "中文稿 G152e_将风险与安全融入TOGAF企业架构.md 第 429–456 行（含图内标签对照表）"
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
