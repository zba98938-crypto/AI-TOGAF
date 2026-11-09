# G233/figB-1 · 迈克尔·波特的价值链（来源：《竞争优势》）

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/figB-1.md) · [JSON](../../architecture/diagrams/G233/figB-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 52 页

![英文原图](../assets/G233/figB-1-p0052.png)

PDF 坐标：`[74.0, 155.3, 538.0, 419.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Firm Infrastructure
Human Resource Management
Support
Activities
&;
Technology Development
Procurement
Inbound
Outbound
Service
Operations
Marketing
©
Logistics
Logistics
And Sales
£
Y~
Primary Activities
```

## 概要（历史解释；局部修正见上）

波特的价值链：四项支持活动横贯上方，五项主要活动横向排列，右侧灰色箭头表示扣除全部活动成本后剩下的利润（Margin）。

## 目的（历史解释；局部修正见上）

附录 B.5 用价值链说明另一种价值视角：价值链把企业拆成战略相关活动，以理解成本行为与差异化来源；它提供“企业如何生产经济价值（金钱）”的宏观视图，可作为决定“需要建模哪些价值流来保证价值链运转”的依据。作者把它与价值流对照，说明两者目的相近但切分方式不同。

## 阅读顺序（历史解释；局部修正见上）

先看两条花括号：左侧“Support Activities”覆盖上方四行，底部“Primary Activities”覆盖下方五列。主要活动从左到右读：Inbound Logistics → Operations → Outbound Logistics → Marketing And Sales → Service。支持活动自上而下读：Firm Infrastructure、Human Resource Management、Technology Development、Procurement，它们横贯并支撑所有主要活动。最右侧灰色大箭头“Margin”从顶到底包住整条链，表示总价值减去总成本后的剩余。

## 关键含义（历史解释；局部修正见上）

- 五项主要活动：入站物流、运营、出站物流、市场营销与销售、服务；它们直接创造并交付产品/服务。
- 四项支持活动：企业基础设施、人力资源管理、技术开发、采购；它们不直接面向客户，但为所有主要活动提供支撑。
- Margin（利润）不是一项活动，而是整条链的剩余价值：总收入减去全部主要活动与支持活动的成本。图中用一条从顶贯到底的灰色箭头表示它包住整条链。
- 支持活动画成横贯四行，表示它们服务于所有主要活动，而不是只在某一列发生。
- 价值链以成本与利润为中心，给出经济价值的宏观视图；价值流以利益相关者价值为中心，给出端到端活动序列。两者粒度与目的不同。
- 正文建议：价值链可作为决定“需要建模哪些价值流”的依据——先看价值链哪些环节重要，再为这些环节建价值流模型。
- 价值链通常对整个组织或业务单元建模，与商业模式画布的粒度相近。
- 本图与 G178《价值流》附录 A 的图 A-1 是同一张图（同一来源、同一版式）。

## 层级（历史解释；局部修正见上）

两层：两类活动（支持活动、主要活动）→ 各自包含的活动项。支持活动与主要活动是并列的两组，不是上下级；Margin 是覆盖全图的结果，不属于任何一组。

## 线条含义（历史解释；局部修正见上）

图中没有连线。分组由花括号表达；Margin 的涵盖范围由灰色箭头的跨度表达（从支持活动顶端到主要活动底端）；主要活动的先后由从左到右的排列暗示，但价值链本身不强调时间顺序。

## 易误读点（历史解释；局部修正见上）

- 不要把 Margin 当成第六项主要活动；它是剩余价值，不是活动。
- 不要把四项支持活动理解为按时间先后发生；它们是横贯的支撑职能。
- 不要把主要活动的左右排列当成严格流程；波特价值链是活动分类，不是价值流阶段。
- 不要把本图与价值流图混用：价值链回答“钱如何被创造”，价值流回答“利益相关者价值如何被交付”。
- 中文稿 PNG 的“利润”方块过大并遮住右上角，且下方旋转的 Margin 未译；不要据其判断 Margin 的图形范围。

## 元素

```json
[
  {
    "id": "grp_support",
    "label_en": "Support Activities",
    "label_zh": "支持活动",
    "type": "group",
    "parent": null,
    "position": "左侧花括号"
  },
  {
    "id": "grp_primary",
    "label_en": "Primary Activities",
    "label_zh": "主要活动",
    "type": "group",
    "parent": null,
    "position": "底部花括号"
  },
  {
    "id": "sup_infrastructure",
    "label_en": "Firm Infrastructure",
    "label_zh": "企业基础设施",
    "type": "function",
    "parent": "grp_support",
    "order": 1
  },
  {
    "id": "sup_hr",
    "label_en": "Human Resource Management",
    "label_zh": "人力资源管理",
    "type": "function",
    "parent": "grp_support",
    "order": 2
  },
  {
    "id": "sup_technology",
    "label_en": "Technology Development",
    "label_zh": "技术开发",
    "type": "function",
    "parent": "grp_support",
    "order": 3
  },
  {
    "id": "sup_procurement",
    "label_en": "Procurement",
    "label_zh": "采购",
    "type": "function",
    "parent": "grp_support",
    "order": 4
  },
  {
    "id": "pri_inbound",
    "label_en": "Inbound Logistics",
    "label_zh": "入站物流",
    "type": "function",
    "parent": "grp_primary",
    "order": 1
  },
  {
    "id": "pri_operations",
    "label_en": "Operations",
    "label_zh": "运营",
    "type": "function",
    "parent": "grp_primary",
    "order": 2
  },
  {
    "id": "pri_outbound",
    "label_en": "Outbound Logistics",
    "label_zh": "出站物流",
    "type": "function",
    "parent": "grp_primary",
    "order": 3
  },
  {
    "id": "pri_marketing",
    "label_en": "Marketing And Sales",
    "label_zh": "市场营销与销售",
    "type": "function",
    "parent": "grp_primary",
    "order": 4
  },
  {
    "id": "pri_service",
    "label_en": "Service",
    "label_zh": "服务",
    "type": "function",
    "parent": "grp_primary",
    "order": 5
  },
  {
    "id": "margin",
    "label_en": "Margin",
    "label_zh": "利润",
    "type": "goal",
    "parent": null,
    "position": "右侧灰色大箭头（上下各标一次 Margin）"
  }
]
```

## 关系

```json
[
  {
    "from": "grp_support",
    "to": "grp_primary",
    "type": "serving",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "支持活动横贯并支撑所有主要活动。"
  },
  {
    "from": "grp_primary",
    "to": "margin",
    "type": "produces",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "主要活动直接创造价值、支持活动提供支撑，二者成本扣除后形成 Margin；边际由箭头跨度表达而非连线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色横条",
    "meaning_zh": "支持活动（Firm Infrastructure、HRM、Technology Development、Procurement）",
    "explicit": false
  },
  {
    "symbol": "彩色竖条（粉/蓝/橙/橄榄/紫）",
    "meaning_zh": "五项主要活动，颜色仅作区分",
    "explicit": false
  },
  {
    "symbol": "灰色大箭头",
    "meaning_zh": "Margin（利润）：整条链的剩余价值",
    "explicit": false
  },
  {
    "symbol": "花括号 + 文字",
    "meaning_zh": "活动分组标签（Support Activities / Primary Activities）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "矩形价值链：上方四行绿色横条（支持活动）叠放，下方五列彩色竖条（主要活动）并排；左侧与下方两条花括号分别标注支持活动与主要活动；右侧一条灰色大箭头从顶到底，内写 Margin。"
}
```

## 相关图

```json
[
  {
    "target": "G178/figA-1",
    "relation": "same_as",
    "note_zh": "G178《价值流》附录 A 的图 A-1 与本图同源同版式（波特价值链，Source: Competitive Advantage），两处使用同一张图"
  },
  {
    "target": "G233/fig5-1",
    "relation": "contrasts_with",
    "note_zh": "价值链按职能活动分解、关注成本与利润；价值流按端到端阶段分解、关注利益相关者价值，附录 B.5 正是讨论两者关系"
  },
  {
    "target": "G233/fig6-3",
    "relation": "contrasts_with",
    "note_zh": "图 6-3 的价值流模型可与价值链对照：前者回答价值如何交付，后者回答经济价值如何产生"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "本图是经典波特价值链的通用画法，原图未标注版本年份；引用信息取自图题“Source: Competitive Advantage”。",
    "Margin 箭头跨越支持活动与主要活动两部分，图中未用文字说明其计算口径，本文按波特原义（总收入减总成本）解释。"
  ],
  "analyzed_from": [
    "英文 PDF 第 52 页图 B-1 截图（450 dpi）",
    "英文 PDF 第 52 页 B.5 正文",
    "中文稿 G233e_业务能力规划.md 第 887–915 行（含标签对照表）",
    "figs/zh/g233e_figB-1_zh.png"
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
