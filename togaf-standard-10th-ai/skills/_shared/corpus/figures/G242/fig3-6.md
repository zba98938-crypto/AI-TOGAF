# G242/fig3-6 · 数字可持续性举措中非功能需求的变化

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-6.md) · [JSON](../../architecture/diagrams/G242/fig3-6.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 50 页

![英文原图](../assets/G242/fig3-6-p0050.png)

PDF 坐标：`[61.1, 36.0, 550.9, 256.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
=:
‘\
```

## 概要（历史解释；局部修正见上）

可持续举措要求降低可用性、存储与能耗，保持安全与性能，同时提高耐用、可维护、可拆解、可移植、互操作与稳健性。

## 目的（历史解释；局部修正见上）

把“敢于约束信息系统”翻译成可执行的非功能需求变化清单：哪些质量属性要下调、哪些保持不变、哪些必须上调。它给架构师一张谈判底牌——可持续不是全面降级，而是用更少的可用性/存储/能耗换取更长的寿命、更好的可维护性与稳健性。

## 阅读顺序（历史解释；局部修正见上）

从左到右读三栏。左栏红色箭头向右下，表示这些需求要降低：Availability、Storage Capacity、Energy Needs。中栏深蓝箭头水平向右，表示维持不变：Safety、Performance。右栏绿色箭头向右上，表示这些需求要提高：Longevity、Maintainability、Dismantlability/Repairability、Portability/Interoperability、Robustness。箭头只标趋势，没有刻度。

## 关键含义（历史解释；局部修正见上）

- 要降低的三项是可用性、存储容量与能源需求，对应正文“敢于约束系统及其使用”的直接代价。
- 要保持的是安全性与性能：可持续转型不以牺牲安全和基本性能为代价。
- 要提高的五项是长寿性、可维护性、可拆解性/可维修性、可移植性/互操作性、稳健性，均指向延长设备寿命、便于维修与迁移。
- 箭头方向是唯一编码：右下=降低、水平=不变、右上=提高；图中没有数值刻度或目标值。
- 这组变化把“节制”从口号变成架构质量属性，可直接写入非功能需求与新 ICT 项目的要求。
- 右栏五项彼此支撑：可维修、可拆解、可移植与互操作共同服务于长寿性，稳健性则保证约束之下系统仍可靠。

## 层级（历史解释；局部修正见上）

无层级。三条竖虚线把画面分成三个并列分区，每个分区内若干需求标签上下排列；标签之间没有上下级，也没有连线。

## 线条含义（历史解释；局部修正见上）

图中没有连接线。两条竖向虚线只分隔三栏；三支粗箭头是趋势标注（红↘降低、深蓝→维持、绿↗提高），不是变量之间的流向或因果。

## 易误读点（历史解释；局部修正见上）

- 箭头不是流程或影响关系，只表示该栏需求的变化方向。
- 中栏水平箭头表示“维持不变”，不是“继续增加”；不要把它与右栏的上升混为一谈。
- 降低可用性不等于降低安全性：安全性与性能在中栏保持不变。
- 同一栏内标签的上下顺序不代表优先级。
- 中文稿当前引用的 figs/zh/g242_fig3-6_zh.png 把中栏的水平箭头几乎擦掉，容易误读为“中栏没有趋势”；英文原图中该箭头清晰可见。

## 元素

```json
[
  {
    "id": "col_decrease",
    "label_en": null,
    "label_zh": "要求降低的一组",
    "type": "group",
    "parent": null,
    "position": "左栏"
  },
  {
    "id": "trend_decrease",
    "label_en": null,
    "label_zh": "红色右下箭头（降低）",
    "type": "note",
    "parent": "col_decrease",
    "position": "左栏顶部"
  },
  {
    "id": "availability",
    "label_en": "Availability",
    "label_zh": "可用性",
    "type": "requirement",
    "parent": "col_decrease",
    "order": 1,
    "position": "左栏第 1 项"
  },
  {
    "id": "storage_capacity",
    "label_en": "Storage Capacity",
    "label_zh": "存储容量",
    "type": "requirement",
    "parent": "col_decrease",
    "order": 2,
    "position": "左栏第 2 项"
  },
  {
    "id": "energy_needs",
    "label_en": "Energy Needs",
    "label_zh": "能源需求",
    "type": "requirement",
    "parent": "col_decrease",
    "order": 3,
    "position": "左栏第 3 项"
  },
  {
    "id": "col_stable",
    "label_en": null,
    "label_zh": "要求维持的一组",
    "type": "group",
    "parent": null,
    "position": "中栏"
  },
  {
    "id": "trend_stable",
    "label_en": null,
    "label_zh": "深蓝水平箭头（维持）",
    "type": "note",
    "parent": "col_stable",
    "position": "中栏顶部"
  },
  {
    "id": "safety",
    "label_en": "Safety",
    "label_zh": "安全性",
    "type": "requirement",
    "parent": "col_stable",
    "order": 1,
    "position": "中栏第 1 项"
  },
  {
    "id": "performance",
    "label_en": "Performance",
    "label_zh": "性能",
    "type": "requirement",
    "parent": "col_stable",
    "order": 2,
    "position": "中栏第 2 项"
  },
  {
    "id": "col_increase",
    "label_en": null,
    "label_zh": "要求提高的一组",
    "type": "group",
    "parent": null,
    "position": "右栏"
  },
  {
    "id": "trend_increase",
    "label_en": null,
    "label_zh": "绿色右上箭头（提高）",
    "type": "note",
    "parent": "col_increase",
    "position": "右栏顶部"
  },
  {
    "id": "longevity",
    "label_en": "Longevity",
    "label_zh": "长寿性",
    "type": "requirement",
    "parent": "col_increase",
    "order": 1,
    "position": "右栏第 1 项"
  },
  {
    "id": "maintainability",
    "label_en": "Maintainability",
    "label_zh": "可维护性",
    "type": "requirement",
    "parent": "col_increase",
    "order": 2,
    "position": "右栏第 2 项"
  },
  {
    "id": "dismantlability",
    "label_en": "Dismantlability/Repairability",
    "label_zh": "可拆解性/可维修性",
    "type": "requirement",
    "parent": "col_increase",
    "order": 3,
    "position": "右栏第 3 项"
  },
  {
    "id": "portability",
    "label_en": "Portability/Interoperability",
    "label_zh": "可移植性/互操作性",
    "type": "requirement",
    "parent": "col_increase",
    "order": 4,
    "position": "右栏第 4 项"
  },
  {
    "id": "robustness",
    "label_en": "Robustness",
    "label_zh": "稳健性",
    "type": "requirement",
    "parent": "col_increase",
    "order": 5,
    "position": "右栏第 5 项"
  }
]
```

## 关系

```json
[
  {
    "from": "col_decrease",
    "to": "trend_decrease",
    "type": "other",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Decrease",
    "label_zh": "降低",
    "description_zh": "红色右下箭头作为整栏注解，不连接两个变量。"
  },
  {
    "from": "col_stable",
    "to": "trend_stable",
    "type": "other",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Unchanged",
    "label_zh": "维持",
    "description_zh": "深蓝水平箭头作为整栏注解。"
  },
  {
    "from": "col_increase",
    "to": "trend_increase",
    "type": "other",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "label_en": "Increase",
    "label_zh": "提高",
    "description_zh": "绿色右上箭头作为整栏注解。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_nfr_trend",
    "title_zh": "非功能需求变化方向（按原图三栏转录）",
    "columns": [
      "趋势",
      "非功能需求（英文）",
      "非功能需求（中文）"
    ],
    "rows": [
      [
        "降低（红↘）",
        "Availability",
        "可用性"
      ],
      [
        "降低（红↘）",
        "Storage Capacity",
        "存储容量"
      ],
      [
        "降低（红↘）",
        "Energy Needs",
        "能源需求"
      ],
      [
        "维持（深蓝→）",
        "Safety",
        "安全性"
      ],
      [
        "维持（深蓝→）",
        "Performance",
        "性能"
      ],
      [
        "提高（绿↗）",
        "Longevity",
        "长寿性"
      ],
      [
        "提高（绿↗）",
        "Maintainability",
        "可维护性"
      ],
      [
        "提高（绿↗）",
        "Dismantlability/Repairability",
        "可拆解性/可维修性"
      ],
      [
        "提高（绿↗）",
        "Portability/Interoperability",
        "可移植性/互操作性"
      ],
      [
        "提高（绿↗）",
        "Robustness",
        "稳健性"
      ]
    ],
    "cell_legend": [
      "红↘=降低，深蓝→=维持，绿↗=提高"
    ],
    "notes_zh": "原图无刻度或目标值，只给方向。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "红色箭头（指向右下）",
    "meaning_zh": "该组非功能需求应降低",
    "explicit": false
  },
  {
    "symbol": "深蓝色箭头（水平向右）",
    "meaning_zh": "该组非功能需求维持不变",
    "explicit": false
  },
  {
    "symbol": "绿色箭头（指向右上）",
    "meaning_zh": "该组非功能需求应提高",
    "explicit": false
  },
  {
    "symbol": "竖向虚线",
    "meaning_zh": "分隔三组趋势，不代表坐标轴",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "横向三栏，由两条竖向虚线分隔：左栏三项（红↘箭头）、中栏两项（深蓝→箭头）、右栏五项（绿↗箭头）；每栏箭头位于顶部，需求标签为深蓝底白字横条，自上而下排列。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-5",
    "relation": "follows",
    "note_zh": "图 3-5 识别出的放弃/优化机会需要落到本图的非功能需求修订"
  },
  {
    "target": "G242/fig3-7",
    "relation": "precedes",
    "note_zh": "本图给出需求变化方向，图 3-7 给出实现这些变化的四类约束"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "三支箭头只是趋势标注，原图没有图例解释颜色；按箭头方向解读为降低/维持/提高。",
    "中栏水平箭头在原图清晰，但中文 PNG 中几乎丢失；以英文原因为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 50 页原图截图（1518×657）",
    "英文 PDF 第 49–50 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 786–809 行",
    "figs/zh/g242_fig3-6_zh.png",
    "figs/g242_fig3-6_en.png（缩略图相似度核对）"
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
