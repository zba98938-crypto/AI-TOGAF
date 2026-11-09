# G212/fig5-4 · 因素递进

> 当前图示解析：[Markdown](../../architecture/diagrams/G212/fig5-4.md) · [JSON](../../architecture/diagrams/G212/fig5-4.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G212e.pdf`；SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

## 原图 · PDF 第 43 页

![英文原图](../assets/G212/fig5-4-p0043.png)

PDF 坐标：`[99.8, 307.4, 512.2, 606.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
es
S
we
```

## 概要（历史解释；局部修正见上）

按满足 DTRA 因素的层级（基础→影响→持续）把企业分为类型 1–3，越往外层，越有利于启动数字技术采用。

## 目的（历史解释；局部修正见上）

配合第 5.4 节“步骤 4：解决短板并启动数字技术采用”，说明评估后企业所处的三种类型，并强调因素必须由内向外逐层满足：基础因素不满足时评估外层因素是徒劳的，所以应采取渐进（分步）且敏捷的方式补齐短板，即“因素递进”。

## 阅读顺序（历史解释；局部修正见上）

从左下角原点读起。纵轴“DTRA 因素层级”自下而上分为基础、影响、持续三段，分别对应由内到外的绿色、蓝色、橙色同心色带（纵轴左侧的分段箭头标出每段范围）。从原点射出的 3 条黑色细箭头代表三类企业，箭头止于哪一层色带，就表示该类企业的就绪度达到哪一层（并包含其内侧各层）。斜向的灰色虚线箭头指向就绪度对数字技术采用越来越有利的方向。横轴为“普及度与采用速度”。

## 关键含义（历史解释；局部修正见上）

- 三类企业：类型 1 只满足基础因素（箭头止于绿色层）；类型 2 满足基础与影响因素（止于蓝色层）；类型 3 满足基础、影响与持续因素（止于橙色层）。
- 色带同心嵌套：外层以内层为前提。原文指出，组织未满足基础因素时，评估影响因素和持续因素是徒劳的。
- 类型 3 在三层因素上都具备足够就绪度，比类型 2、类型 1 更有利于启动数字技术采用；虚线箭头沿“由内向外”的方向表达这种递增。
- “因素递进”指建议的渐进且敏捷的路径：先基础因素、再影响因素、最后持续因素。原文也允许出于实际原因采用混合方式，此时可借助图 5-3（缺失因素的后果）做有依据的决策。
- 因素递进可与步骤 1 选定的采用方法组合使用，例如先选先锋式（avant-garde）方法，再对选定的业务线运用因素递进（原文 p44）。
- 横轴“普及度与采用速度”沿用了图 5-2 ABCD 框架的两个维度（普及度、速度）；原文没有单独解释本图横轴，从版式看，越外层的色带在横轴方向延伸得越远。

## 层级（历史解释；局部修正见上）

三层因素由内到外同心嵌套：基础因素（最内，绿）→ 影响因素（中，蓝）→ 持续因素（最外，橙）；外层以内层为前提。三类企业不是上下级关系，而是按“满足到第几层”划分的类别，类型 3 包含类型 2 的全部层级，类型 2 包含类型 1 的全部层级。

## 线条含义（历史解释；局部修正见上）

从原点射出的 3 条黑色细实线箭头，箭头所在的色带表示该类企业达到的因素层级，穿过的内侧色带表示同时满足的内层因素（关系清单中“止于”记为显式，“穿过”记为推断）。灰色粗虚线箭头没有连接任何元素，只表示“就绪度有利程度”递增的方向。两条深青色坐标轴的箭头表示数值增加的方向；纵轴左侧的分段双向箭头标示各层因素在纵轴上的范围。

## 易误读点（历史解释；局部修正见上）

- 箭头的长度和角度不是量化数据：三条箭头张开不同角度只是为了放下标签，图中没有刻度。
- 三类企业不是三个先后执行的步骤，而是评估结果的三种情形；“递进”指企业应由内向外逐层补齐因素。
- 外层不能跳过内层：没有满足基础因素，就谈不上影响因素与持续因素。
- 中文稿引用的 figs/zh/g212e_fig5-4_zh.png 被白块遮掉了三层色带、三条类型箭头及其标签，读者无法从中看出类型 1/2/3 与因素层级的对应，应以英文原图为准。

## 元素

```json
[
  {
    "id": "axis_levels",
    "label_en": "Levels of DTRA Factors →",
    "label_zh": "DTRA 因素层级",
    "type": "concept",
    "position": "左侧纵轴（深青色竖框）",
    "description_zh": "纵轴，自下而上依次为基础、影响、持续三层。"
  },
  {
    "id": "lvl_foundational",
    "label_en": "Foundational",
    "label_zh": "基础因素",
    "type": "concept",
    "parent": null,
    "order": 1,
    "position": "纵轴下段；绿色最内层",
    "description_zh": "组织建立最低可接受就绪度必须具备的因素（第 4.1 节，共 7 个）。"
  },
  {
    "id": "lvl_impact",
    "label_en": "Impact",
    "label_zh": "影响因素",
    "type": "concept",
    "parent": null,
    "order": 2,
    "position": "纵轴中段；蓝色中间层",
    "description_zh": "增强或放大主要因素有效性的因素（第 4.2 节，共 5 个）。"
  },
  {
    "id": "lvl_sustaining",
    "label_en": "Sustaining",
    "label_zh": "持续因素",
    "type": "concept",
    "parent": null,
    "order": 3,
    "position": "纵轴上段；橙色最外层",
    "description_zh": "使数字技术采用制度化、获得长期收益的因素（第 4.3 节，共 3 个）。"
  },
  {
    "id": "axis_ubiquity_velocity",
    "label_en": "Ubiquity & Velocity →",
    "label_zh": "普及度与采用速度",
    "type": "concept",
    "position": "底部横轴（深青色横框）",
    "description_zh": "横轴；两个维度与图 5-2 ABCD 框架的坐标轴相同。"
  },
  {
    "id": "conduciveness",
    "label_en": "How Conducive the Readiness is for Digital Technology Adoption →",
    "label_zh": "就绪度对数字技术采用的有利程度",
    "type": "metric",
    "position": "从原点斜向右上的灰色虚线箭头上",
    "description_zh": "沿虚线箭头方向递增。"
  },
  {
    "id": "type_1",
    "label_en": "Type 1",
    "label_zh": "类型 1",
    "type": "concept",
    "order": 1,
    "position": "最下方箭头，止于绿色层外缘",
    "description_zh": "只满足基础因素的企业。"
  },
  {
    "id": "type_2",
    "label_en": "Type 2",
    "label_zh": "类型 2",
    "type": "concept",
    "order": 2,
    "position": "中间箭头，止于蓝色层外缘",
    "description_zh": "满足基础与影响因素的企业。"
  },
  {
    "id": "type_3",
    "label_en": "Type 3",
    "label_zh": "类型 3",
    "type": "concept",
    "order": 3,
    "position": "最上方实线箭头，止于橙色层内",
    "description_zh": "满足基础、影响与持续因素的企业，最有利于启动数字技术采用。"
  }
]
```

## 关系

```json
[
  {
    "from": "type_1",
    "to": "lvl_foundational",
    "type": "maps_to",
    "label_zh": "满足（箭头止于绿色层）",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "type_2",
    "to": "lvl_foundational",
    "type": "maps_to",
    "label_zh": "满足（箭头穿过绿色层）",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "type_2",
    "to": "lvl_impact",
    "type": "maps_to",
    "label_zh": "满足（箭头止于蓝色层）",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "type_3",
    "to": "lvl_foundational",
    "type": "maps_to",
    "label_zh": "满足（箭头穿过绿色层）",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "type_3",
    "to": "lvl_impact",
    "type": "maps_to",
    "label_zh": "满足（箭头穿过蓝色层）",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "type_3",
    "to": "lvl_sustaining",
    "type": "maps_to",
    "label_zh": "满足（箭头止于橙色层）",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "lvl_foundational",
    "to": "lvl_impact",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "同心色带由内向外、纵轴自下而上；原文建议先基础、再影响"
  },
  {
    "from": "lvl_impact",
    "to": "lvl_sustaining",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "原文建议影响因素之后是持续因素"
  },
  {
    "from": "type_1",
    "to": "type_2",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "沿虚线箭头方向，就绪度的有利程度递增"
  },
  {
    "from": "type_2",
    "to": "type_3",
    "type": "sequence",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "类型 3 比类型 2、类型 1 更有利于启动采用"
  },
  {
    "from": "conduciveness",
    "to": "type_3",
    "type": "association",
    "label_zh": "有利程度最高",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "虚线箭头指向最外层，与止于最外层的类型 3 对应"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_factor_progression",
    "kind": "sequence",
    "name_zh": "因素递进（建议的渐进敏捷路径）",
    "steps": [
      "lvl_foundational",
      "lvl_impact",
      "lvl_sustaining"
    ],
    "description_zh": "原文 p44 的注：先基础因素，再影响因素，最后持续因素；实际中也可能采用混合方式。"
  },
  {
    "id": "f_types",
    "kind": "sequence",
    "name_zh": "就绪度有利程度递增",
    "steps": [
      "type_1",
      "type_2",
      "type_3"
    ]
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_types",
    "title_zh": "三类企业满足的因素层级（据原图箭头止点与正文）",
    "columns": [
      "企业类型",
      "基础因素",
      "影响因素",
      "持续因素",
      "箭头止于"
    ],
    "rows": [
      [
        "类型 1 Type 1",
        "✓",
        "—",
        "—",
        "绿色层（基础）"
      ],
      [
        "类型 2 Type 2",
        "✓",
        "✓",
        "—",
        "蓝色层（影响）"
      ],
      [
        "类型 3 Type 3",
        "✓",
        "✓",
        "✓",
        "橙色层（持续）"
      ]
    ],
    "cell_legend": [
      "✓ = 满足该层因素",
      "— = 未满足"
    ],
    "notes_zh": "由原图箭头的止点与第 5.4 节正文的三类定义整理，原图本身不是表格。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "绿色最内层四分之一圆",
    "meaning_zh": "基础因素层（Foundational）",
    "explicit": false
  },
  {
    "symbol": "蓝色中间环带",
    "meaning_zh": "影响因素层（Impact）",
    "explicit": false
  },
  {
    "symbol": "橙色最外环带",
    "meaning_zh": "持续因素层（Sustaining）",
    "explicit": false
  },
  {
    "symbol": "纵轴左侧的分段双向箭头 + 层名",
    "meaning_zh": "标出每层因素在纵轴上的范围，用来把色带与层名对上",
    "explicit": false
  },
  {
    "symbol": "从原点射出的黑色细箭头 + Type 标签",
    "meaning_zh": "一类企业；箭头所止的色带即该类企业满足到的因素层级",
    "explicit": false
  },
  {
    "symbol": "斜向灰色虚线箭头",
    "meaning_zh": "就绪度对数字技术采用越来越有利的方向",
    "explicit": false
  },
  {
    "symbol": "深青色底框 + “→”",
    "meaning_zh": "坐标轴标题，箭头表示沿该轴递增",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "radial",
  "description_zh": "左下角为原点的第一象限：纵轴向上、横轴向右；三层四分之一圆（略呈椭圆）色带由内到外为绿、蓝、橙；3 条类型箭头和 1 条斜向虚线箭头从原点向右上方呈扇形射出；纵轴标题在左侧深青色竖框内，横轴标题在底部深青色横框内。"
}
```

## 相关图

```json
[
  {
    "target": "G212/fig5-1",
    "relation": "detail_of",
    "note_zh": "本图展开四步路线图中的步骤 4（解决短板并启动数字技术采用）"
  },
  {
    "target": "G212/fig4-1",
    "relation": "related",
    "note_zh": "两图使用同一套三类因素（基础/影响/持续）；图 4-1 画出 15 个因素之间的依赖，本图只按层级概括"
  },
  {
    "target": "G212/fig5-3",
    "relation": "complements",
    "note_zh": "原文指出采用混合方式而不按因素递进时，可借助图 5-3 的缺失因素后果做决策"
  },
  {
    "target": "G212/fig5-2",
    "relation": "related",
    "note_zh": "本图横轴“普及度与采用速度”即 ABCD 框架的两个坐标维度；原文称采用方法与因素递进可以组合使用"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原文没有解释横轴“普及度与采用速度”在本图中的具体含义，key_points 中对横轴的说明仅依据版式和图 5-2 的同名维度。",
    "类型与层级的“穿过”关系（如类型 3 同时满足基础与影响因素）来自正文定义，图上只用箭头穿过色带表示。"
  ],
  "analyzed_from": [
    "英文 PDF 第 43 页原图截图（220 dpi）",
    "英文 PDF 第 43–44 页正文",
    "中文稿 G212e_数字技术采用就绪度评估.md 第 250–256、570–606 行（含图内标签对照表 L586–L599）",
    "figs/zh/g212e_fig5-4_zh.png",
    "figs/g212e_fig5-4_en.png（自动相似度 0.991）"
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
