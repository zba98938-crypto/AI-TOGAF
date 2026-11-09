# G21I/fig5-2 · MSA 治理参考模型

> 当前图示解析：[Markdown](../../architecture/diagrams/G21I/fig5-2.md) · [JSON](../../architecture/diagrams/G21I/fig5-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Ie.pdf`；SHA-256：`279f6c06124f49a147a168591965805115b2fc976eea2664e41e491ac5d163bf`。

## 原图 · PDF 第 26 页

![英文原图](../assets/G21I/fig5-2-p0026.png)

PDF 坐标：`[177.1, 323.1, 434.9, 598.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
\|
\\
\\
a
\\
(\
\)
\\
\\
\
a
iding
Technol
9Y\|\ p
ng
iples
(Gan
\
UY]
|v
ray
\ \\
ws
\
Ay
‘ loles\
\\
Governing
nsibiliti
Processes
\\ \\
\\ \
\\
Le
\\
\\\
\ \\
\|
\|
Governed
Vs
Artifacts
MSA
Processes
Vy)
©The Open Group
```

## 概要（历史解释；局部修正见上）

MSA 治理参考模型由 6 个部分组成，外圈顺时针箭头表示它们构成持续改进的循环。

## 目的（历史解释；局部修正见上）

第 5.3 节用本图给出 MSA 治理参考模型：它与 SOA 治理参考模型大体相同，只是范围限于 MSA 流程。外圈箭头强调治理是过程而不是项目，各阶段构成持续改进循环：度量进展，需要时纠偏并更新流程。

## 阅读顺序（历史解释；局部修正见上）

从右上方的“指导原则”扇区开始，沿外圈箭头顺时针读：指导原则 → 治理流程 → 受治理的 MSA 流程 → 制品 → 角色与职责 → 技术，再回到指导原则。外圈上的 6 个箭头头部都位于扇区分界处，方向一致为顺时针。

## 关键含义（历史解释；局部修正见上）

- 模型有 6 个组成部分：指导原则、治理流程、受治理的 MSA 流程、制品、角色与职责、技术。
- 原文说明 MSA 治理参考模型与 SOA 治理参考模型大体相同，区别只在于它限于 MSA 流程；图中“受治理的 MSA 流程”一格体现了这一点。
- “治理流程”与“受治理的 MSA 流程”是两回事：前者是实施治理的流程，后者是被治理的对象（MSA 的流程），二者在环上相邻。
- 外圈顺时针箭头把 6 个部分连成闭环：治理模型应被视为过程而不是项目，各阶段循环进行，度量进展并在需要时纠偏和更新流程。
- 原文没有逐一解释 6 个部分的含义，也没有给出相邻部分之间具体的输入/输出。

## 层级（历史解释；局部修正见上）

一层：MSA 治理参考模型（图中没有单独的框，由整个圆表示）包含 6 个并列的组成部分，扇区等大，彼此没有上下级。

## 线条含义（历史解释；局部修正见上）

外圈粗灰线带 6 个箭头头部，均为顺时针，各位于一条分隔线与外圈的交点，表示循环方向；关系清单把每段外圈记为相邻扇区之间的先后关系。三条细灰直径只用于分隔扇区，不表示对角扇区之间有关系。

## 易误读点（历史解释；局部修正见上）

- 直径不是连线：被同一条直径穿过的对角扇区之间没有关系。
- 6 个部分在环上首尾相接，没有起点和终点；从“指导原则”读起只是阅读习惯，不表示它最重要。
- 原图中空心大字“Evaluation Copy”是英文 PDF 的水印，不是图的内容。
- 中文稿引用的中文化 PNG 中“角色与职责”字号特别大并遮住一段外圈，“受治理的微服务架构流程”字号极小，容易让人以为各部分权重不同；原图 6 个标签字号一致。

## 元素

```json
[
  {
    "id": "gov_model",
    "label_en": "MSA Governance Reference Model",
    "label_zh": "MSA 治理参考模型",
    "type": "framework",
    "parent": null,
    "level": 0,
    "description_zh": "图中没有单独的框，由整个圆表示；名称来自图题。"
  },
  {
    "id": "s_principles",
    "label_en": "Guiding Principles",
    "label_zh": "指导原则",
    "type": "principle",
    "parent": "gov_model",
    "level": 1,
    "order": 1,
    "position": "右上扇区"
  },
  {
    "id": "s_governing",
    "label_en": "Governing Processes",
    "label_zh": "治理流程",
    "type": "process",
    "parent": "gov_model",
    "level": 1,
    "order": 2,
    "position": "右中扇区"
  },
  {
    "id": "s_governed",
    "label_en": "Governed MSA Processes",
    "label_zh": "受治理的微服务架构流程",
    "type": "process",
    "parent": "gov_model",
    "level": 1,
    "order": 3,
    "position": "右下扇区",
    "description_zh": "被治理的对象，即 MSA 的流程；SOA 治理参考模型中对应的是受治理的 SOA 流程（背景知识）。"
  },
  {
    "id": "s_artifacts",
    "label_en": "Artifacts",
    "label_zh": "制品",
    "type": "artifact",
    "parent": "gov_model",
    "level": 1,
    "order": 4,
    "position": "左下扇区"
  },
  {
    "id": "s_roles",
    "label_en": "Roles and Responsibilities",
    "label_zh": "角色与职责",
    "type": "role",
    "parent": "gov_model",
    "level": 1,
    "order": 5,
    "position": "左中扇区"
  },
  {
    "id": "s_technology",
    "label_en": "Technology",
    "label_zh": "技术",
    "type": "technology",
    "parent": "gov_model",
    "level": 1,
    "order": 6,
    "position": "左上扇区"
  }
]
```

## 关系

```json
[
  {
    "from": "s_principles",
    "to": "s_governing",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "外圈顺时针箭头（右上分界处）"
  },
  {
    "from": "s_governing",
    "to": "s_governed",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "外圈顺时针箭头（右下分界处）"
  },
  {
    "from": "s_governed",
    "to": "s_artifacts",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "外圈顺时针箭头（底部分界处）"
  },
  {
    "from": "s_artifacts",
    "to": "s_roles",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "外圈顺时针箭头（左下分界处）"
  },
  {
    "from": "s_roles",
    "to": "s_technology",
    "type": "sequence",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "外圈顺时针箭头（左上分界处）"
  },
  {
    "from": "s_technology",
    "to": "s_principles",
    "type": "iteration",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "外圈顺时针箭头（顶部分界处），闭合循环"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_gov_loop",
    "kind": "cycle",
    "name_zh": "MSA 治理持续改进循环",
    "steps": [
      "s_principles",
      "s_governing",
      "s_governed",
      "s_artifacts",
      "s_roles",
      "s_technology"
    ],
    "description_zh": "外圈顺时针；原文称各阶段构成持续改进循环，度量进展并在需要时纠偏、更新流程。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "扇区 + 蓝色粗体标签",
    "meaning_zh": "治理参考模型的一个组成部分",
    "explicit": false
  },
  {
    "symbol": "外圈粗灰线上的箭头（顺时针）",
    "meaning_zh": "持续改进循环的方向",
    "explicit": false
  },
  {
    "symbol": "细灰直径",
    "meaning_zh": "扇区分隔线，无关系含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "一个圆被三条直径（一条竖直、两条斜向）分成 6 个等大扇区；标签按顺时针排列：右上指导原则、右中治理流程、右下受治理的 MSA 流程、左下制品、左中角色与职责、左上技术。外圈箭头头部分别位于顶部、右上、右下、底部、左下、左上。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原文没有解释 6 个组成部分各自的含义，也没有说明相邻部分之间传递什么；关系清单只按外圈箭头记录先后。"
  ],
  "analyzed_from": [
    "英文 PDF 第 26 页原图截图（220 dpi）",
    "英文 PDF 第 25–26 页正文",
    "中文稿 G21Ie_微服务架构.md 第 306–323 行（含图内标签对照表 L312–L321）",
    "figs/zh/g21ie_fig5-2_zh.png",
    "figs/g21ie_fig5-2_en.png（自动相似度 0.954）"
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
