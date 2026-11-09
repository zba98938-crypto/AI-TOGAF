# G248/fig2-1 · 企业变革画像

> 当前图示解析：[Markdown](../../architecture/diagrams/G248/fig2-1.md) · [JSON](../../architecture/diagrams/G248/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G248e.pdf`；SHA-256：`810df20478f65d8dfd969089f9c682ec268d0e3a9126e062bda5191c9017e19c`。

## 原图 · PDF 第 14 页

![英文原图](../assets/G248/fig2-1-p0014.png)

PDF 坐标：`[48.2, 270.6, 563.8, 638.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
The Open Group
True Enterprise Flexibility & Responsiveness
Utilizes the Optimum Set of Change Profiles based on
the Goals, Objectives, Requirements of each specific change and its possible solution options
(Not a one-size-fits-all approach).
Robust Change
Functional Change
Rapid Change
For example, Nuclear Power
For example; Sales\Campaigns,
For example, Two
Weeks Left Before Market
Stations, Aircraft Control
Async Messaging Systems,
Systems,
Information and Document Sharing
Window Closes
Core Banking Systems
Higher
Lower
Arbitrary
Integrity
Integrity
Integrity
Higher Risk
Lower
.
Arbitrary Risk
Risk
i
```

## 概要（历史解释；局部修正见上）

用三列与钟形曲线说明稳健、功能、快速三类变革画像沿同一连续谱分布、风险与完整性要求递变。

## 目的（历史解释；局部修正见上）

作者用一张图交代全篇的分类框架：企业中的变革不是只有一种做法，而是按目标、目的与需求落在稳健、功能、快速三类画像构成的连续谱上；后文第 3 章的实体分组与构建块选择都按这三类画像展开。

## 阅读顺序（历史解释；局部修正见上）

先读顶部灰框的总标题，它说明要按每次变革的目标、目的、需求选择最优画像组合（不是一刀切）。再从左到右读三列：Robust Change → Functional Change → Rapid Change。每列上半部是典型例子，下半部是对完整性（Integrity）与风险（Risk）的判断。蓝色钟形曲线横跨三列、峰值落在功能画像；最底部的灰色箭头两端都有箭头，是一条没有刻度和标签的连续轴。

## 关键含义（历史解释；局部修正见上）

- 三类画像是一条连续谱上的位置，不是互斥的标签；左端稳健、右端快速。
- 完整性要求与风险沿谱变化：稳健为 Higher Integrity / Higher Risk，功能为 Lower Integrity / Lower Risk，快速为 Arbitrary Integrity / Arbitrary Risk。
- 蓝色钟形曲线覆盖三列且峰值在 Functional Change 一列，暗示多数变革落在功能画像，稳健与快速是两端的少数情形；曲线没有纵轴或刻度，属于示意而非统计数据。
- 每列给出典型场景：核电站/飞控/核心银行系统（稳健）；销售活动/异步消息/信息与文档共享（功能）；市场窗口关闭前两周（快速）。
- 顶部标题强调“真正的企业灵活性与响应力”来自按每次变革的目标、目的、需求选择最优画像组合，而不是对所有变革采用同一套方法。
- 底部灰色双向箭头把三列串成一条轴，但两端都没有箭头文字、刻度和单位，不能据此读出定量区间。

## 层级（历史解释；局部修正见上）

共两层：顶部的总标题框统摄全图；其下是三列并列的画像（每列含画像名、示例、完整性/风险三块文字）。三列之间没有上下级，只有横向的连续谱关系。

## 线条含义（历史解释；局部修正见上）

图内唯一的画线是底部贯穿全宽的灰色粗箭头，两端都有箭头，表示三种画像位于同一连续轴上；它不与任何框相连，也没有标签。蓝色钟形曲线是覆盖在列上的面积图形，不是连接线，不表示实体关系。三列之间的竖线只是分栏线。

## 易误读点（历史解释；局部修正见上）

- 不要把钟形曲线当成有数据支撑的概率分布：它没有纵轴、刻度或样本，只是示意“中间多、两端少”。
- 不要把“Arbitrary Integrity / Arbitrary Risk”理解为没有风险，它指快速画像对完整性与风险的取舍是随情境而定的。
- 不要把三类画像读成成熟度阶梯：快速不等于不成熟，稳健也不等于更高级，选择取决于变革性质。
- 底部双向箭头的两端没有标签，不能判断轴的方向（是从稳健到快速还是相反）；左右顺序只由三列的排列给出。
- 中文稿当前引用的 figs/g248_fig2-1.svg 是三张要点卡片，不是本图；不能据它理解曲线与连续谱。

## 元素

```json
[
  {
    "id": "header",
    "label_en": "True Enterprise Flexibility & Responsiveness",
    "label_zh": "真正的企业灵活性与响应力",
    "type": "note",
    "parent": null,
    "position": "顶部浅灰标题框",
    "description_zh": "整张图的总论点，位于带粗黑边框的浅灰横条中。"
  },
  {
    "id": "header_detail",
    "label_en": "Utilizes the Optimum Set of Change Profiles based on the Goals, Objectives, Requirements of each specific change and its possible solution options (Not a one-size-fits-all approach).",
    "label_zh": "根据每次具体变革及其可能解决方案选项的目标、目的与需求，采用最优的变革画像组合（并非一刀切的做法）。",
    "type": "note",
    "parent": "header",
    "position": "标题下方三行小字",
    "description_zh": "解释为什么需要三类画像而不是单一方法。"
  },
  {
    "id": "copyright",
    "label_en": "© The Open Group",
    "label_zh": "© The Open Group",
    "type": "note",
    "parent": "header",
    "position": "标题框右上角",
    "description_zh": "版权标记。"
  },
  {
    "id": "robust_profile",
    "label_en": "Robust Change",
    "label_zh": "稳健变革（Robust）",
    "type": "concept",
    "parent": null,
    "position": "左列标题",
    "description_zh": "风险与架构驱动的长周期变革画像。"
  },
  {
    "id": "robust_example",
    "label_en": "For example, Nuclear Power Stations, Aircraft Control Systems, Core Banking Systems",
    "label_zh": "例如：核电站、飞机控制系统、核心银行系统",
    "type": "note",
    "parent": "robust_profile",
    "position": "左列上部",
    "description_zh": "稳健画像的典型场景。"
  },
  {
    "id": "robust_integrity",
    "label_en": "Higher Integrity Higher Risk",
    "label_zh": "更高完整性、更高风险",
    "type": "note",
    "parent": "robust_profile",
    "position": "左列下部",
    "description_zh": "稳健画像对完整性与风险的判断。"
  },
  {
    "id": "functional_profile",
    "label_en": "Functional Change",
    "label_zh": "功能变革（Functional）",
    "type": "concept",
    "parent": null,
    "position": "中列标题",
    "description_zh": "可实现能力驱动的迭代式变革画像，钟形曲线峰值所在列。"
  },
  {
    "id": "functional_example",
    "label_en": "For example, Sales Campaigns, Async Messaging Systems, Information and Document Sharing",
    "label_zh": "例如：销售活动、异步消息系统、信息与文档共享",
    "type": "note",
    "parent": "functional_profile",
    "position": "中列上部",
    "description_zh": "功能画像的典型场景。"
  },
  {
    "id": "functional_integrity",
    "label_en": "Lower Integrity Lower Risk",
    "label_zh": "较低完整性、较低风险",
    "type": "note",
    "parent": "functional_profile",
    "position": "中列下部",
    "description_zh": "功能画像对完整性与风险的判断。"
  },
  {
    "id": "rapid_profile",
    "label_en": "Rapid Change",
    "label_zh": "快速变革（Rapid）",
    "type": "concept",
    "parent": null,
    "position": "右列标题",
    "description_zh": "短时间交付驱动的变革画像。"
  },
  {
    "id": "rapid_example",
    "label_en": "For example, Two Weeks Left Before Market Window Closes",
    "label_zh": "例如：距离市场窗口关闭只剩两周",
    "type": "note",
    "parent": "rapid_profile",
    "position": "右列上部",
    "description_zh": "快速画像的典型场景。"
  },
  {
    "id": "rapid_integrity",
    "label_en": "Arbitrary Integrity Arbitrary Risk",
    "label_zh": "完整性视情境而定、风险视情境而定",
    "type": "note",
    "parent": "rapid_profile",
    "position": "右列下部",
    "description_zh": "快速画像对完整性与风险的判断。"
  }
]
```

## 关系

```json
[
  {
    "id": "r_axis",
    "from": "robust_profile",
    "to": "rapid_profile",
    "type": "other",
    "label_en": "（无标签的双向轴）",
    "label_zh": "（无标签的双向轴）",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "底部灰色粗箭头横贯三列，两端都有箭头；没有刻度、单位或轴名，只表示三类画像位于同一连续谱上。"
  },
  {
    "id": "r_order_rf",
    "from": "robust_profile",
    "to": "functional_profile",
    "type": "sequence",
    "label_en": null,
    "label_zh": null,
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "按三列从左到右的排列隐含的顺序：稳健—功能。无画线。"
  },
  {
    "id": "r_order_fr",
    "from": "functional_profile",
    "to": "rapid_profile",
    "type": "sequence",
    "label_en": null,
    "label_zh": null,
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "按三列从左到右的排列隐含的顺序：功能—快速。无画线。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "三列并列（Robust Change / Functional Change / Rapid Change）",
    "meaning_zh": "三类变革画像沿横向连续谱排列，左稳健、右快速",
    "explicit": false
  },
  {
    "symbol": "蓝色钟形曲线",
    "meaning_zh": "示意多数变革落在功能画像、向两端递减；无纵轴与刻度",
    "explicit": false
  },
  {
    "symbol": "底部灰色双向粗箭头",
    "meaning_zh": "贯穿三列的连续轴，两端均有箭头且无标签",
    "explicit": false
  },
  {
    "symbol": "每列 For example… 文字",
    "meaning_zh": "该画像的典型变革场景示例",
    "explicit": false
  },
  {
    "symbol": "Higher/Lower/Arbitrary Integrity、Risk",
    "meaning_zh": "该画像对完整性与风险的相对要求",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "顶部一个横跨全宽的浅灰标题框；下方三列等宽并排（Robust 在左、Functional 居中、Rapid 在右），每列自上而下为画像名、For example 示例、完整性/风险判断；一条蓝色钟形曲线压在三列下半部，峰值在中间列；最底部一条灰色粗双向箭头横贯全宽。"
}
```

## 相关图

```json
[
  {
    "target": "G248/fig2-2",
    "relation": "complements",
    "note_zh": "图 2-1 给出三类变革画像的总框架，2.1 节的图 2-2 转入其中过渡架构与工作包的 ERD。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "底部双向轴的箭头两端都没有文字，无法确定作者意图的轴向（文中按三列排列读作“稳健→快速”）。",
    "钟形曲线没有纵轴与刻度，只能作定性理解，不能量化。",
    "原图截图中带蓝色细边框与灰色外框，是 PDF 截取边框，不是图的内容。"
  ],
  "analyzed_from": [
    "英文 PDF 第 14 页图 2-1 截图（220 dpi）及 2×2 放大分块",
    "英文 PDF 第 14 页正文",
    "中文稿 G248e_构建块的选择方法.md 第 86–101 行",
    "figs/g248_fig2-1.svg 源码"
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
