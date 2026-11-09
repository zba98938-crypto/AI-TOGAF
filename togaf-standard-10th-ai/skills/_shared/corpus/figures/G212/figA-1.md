# G212/figA-1 · 李克特量表

> 当前图示解析：[Markdown](../../architecture/diagrams/G212/figA-1.md) · [JSON](../../architecture/diagrams/G212/figA-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G212e.pdf`；SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

## 原图 · PDF 第 49 页

![英文原图](../assets/G212/figA-1-p0049.png)

PDF 坐标：`[74.0, 185.1, 538.0, 403.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Strongly
Somewhat
Somewhat
Strongly
Agree
Agree
Agree
Neutral
Disagree
Disagree
Disagree
Evolve
Evolve
Evolve
Evolve
Evolve
Evolve
Evolve
Disseminate
Disseminate
Disseminate
Disseminate
Disseminate
Disseminate
Disseminate
Commit
Commit
Commit
Commit
Commit
Commit
Commit
Understand
Understand
Understand
Understand
Understand
Understand
Understand
Validate
Validate
Validate
Validate
Validate
Validate
Validate
Define
Define
Define
Define
Define
Define
```

## 概要（历史解释；局部修正见上）

七级李克特量表用 6 个累积层级的填充格数，表示从“非常同意”到“非常不同意”。

## 目的（历史解释；局部修正见上）

附录 A 的问卷要用李克特量表作答；作者用这张图说明每个等级不是抽象分数，而是对应“定义→验证→理解→承诺→传播→演进”六个层级被满足到哪一步，使评分有可解释的锚点。正文举例：若某特征已被定义、验证和理解，但没有承诺、传播与演进路径，就应评为“中立”。

## 阅读顺序（历史解释；局部修正见上）

先从左到右读 7 列，等级由“非常同意”逐级降到“非常不同意”。每一列内自下而上读 6 个层级：Define（定义）→ Validate（验证）→ Understand（理解）→ Commit（承诺）→ Disseminate（传播）→ Evolve（演进）。深青色格表示该层级“已存在/已满足”，白格表示“不存在/未满足”。数一列中有几格是深青色，就是该等级所对应的已满足层级数。

## 关键含义（历史解释；局部修正见上）

- 七个等级为 Strongly Agree、Agree、Somewhat Agree、Neutral、Somewhat Disagree、Disagree、Strongly Disagree，分值 7–1（中文稿表 A-1）。
- 六个层级是累积的：要判定某一级，必须先从 Define 起逐级满足到该级；图上深青色格总在下方连续出现，白格总在上方。
- 非常同意 = 6 层全部满足；同意 = 5 层（缺 Evolve）；比较同意 = 4 层（缺 Evolve、Disseminate）；中立 = 3 层（Understand、Validate、Define）。
- 比较不同意 = 2 层（Validate、Define）；不同意 = 1 层（仅 Define）；非常不同意 = 0 层。
- “中立”不是“没有意见”，而是“定义、验证、理解已具备，但没有承诺、传播与演进路径”——这是正文给出的解释。
- 李克特量表通常按序数尺度使用（背景知识），等级之间不保证等距，不宜把 1–7 直接当等距数值做平均或加减；原文也未给出按总分划分合格线的数值阈值（中文稿表 A-1 后说明）。

## 层级（历史解释；局部修正见上）

两层：7 个并列的等级（列）之下，各有同一套 6 个累积层级（行）。六个层级自下而上构成一条成熟度阶梯，上层隐含下层；七个等级之间没有上下级，只是同一量表的不同档位。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头。等级与层级的对应由“列”表达；某层级是否满足由该格的填充色表达（深青=已存在/已满足，白=不存在/未满足）。六个层级自下而上的累积顺序由填充图案表达：任何一列的深青格都从 Define 起连续向上，没有跳格。

## 易误读点（历史解释；局部修正见上）

- 深青格越多表示同意程度越高，不是“完成的工作越多”或“问题越严重”。
- “非常不同意”列全白，不是“全部满足”或“未填写”；它表示六个层级一个都不具备。
- 白色格不代表该层级不重要，只表示在该等级下尚未满足；例如“同意”列只有 Evolve 为白，下面五层仍满足。
- 六个层级是累积的，不能跳过下层直接判定上层；图上没有出现“下层白、上层深青”的列。
- 七级量表是序数尺度（背景知识），不能把 1–7 当作等距数值做平均或加减；原文未设总分合格线。
- 中文稿引用的 figs/zh/g212e_figA-1_zh.png 在“同意”列的“传播”格只填了一半，容易把 6 分误读为“传播未满足”。

## 元素

```json
[
  {
    "id": "sa",
    "label_en": "Strongly Agree",
    "label_zh": "非常同意",
    "type": "metric",
    "parent": null,
    "order": 1,
    "position": "第 1 列",
    "attributes": {
      "score": 7
    }
  },
  {
    "id": "a",
    "label_en": "Agree",
    "label_zh": "同意",
    "type": "metric",
    "parent": null,
    "order": 2,
    "position": "第 2 列",
    "attributes": {
      "score": 6
    }
  },
  {
    "id": "swa",
    "label_en": "Somewhat Agree",
    "label_zh": "比较同意",
    "type": "metric",
    "parent": null,
    "order": 3,
    "position": "第 3 列",
    "attributes": {
      "score": 5
    }
  },
  {
    "id": "n",
    "label_en": "Neutral",
    "label_zh": "中立",
    "type": "metric",
    "parent": null,
    "order": 4,
    "position": "第 4 列",
    "attributes": {
      "score": 4
    }
  },
  {
    "id": "swd",
    "label_en": "Somewhat Disagree",
    "label_zh": "比较不同意",
    "type": "metric",
    "parent": null,
    "order": 5,
    "position": "第 5 列",
    "attributes": {
      "score": 3
    }
  },
  {
    "id": "d",
    "label_en": "Disagree",
    "label_zh": "不同意",
    "type": "metric",
    "parent": null,
    "order": 6,
    "position": "第 6 列",
    "attributes": {
      "score": 2
    }
  },
  {
    "id": "sd",
    "label_en": "Strongly Disagree",
    "label_zh": "非常不同意",
    "type": "metric",
    "parent": null,
    "order": 7,
    "position": "第 7 列",
    "attributes": {
      "score": 1
    }
  },
  {
    "id": "lvl_define",
    "label_en": "Define",
    "label_zh": "定义",
    "type": "concept",
    "parent": null,
    "order": 1,
    "position": "每列最下一格",
    "description_zh": "最低层级：特征已被定义。"
  },
  {
    "id": "lvl_validate",
    "label_en": "Validate",
    "label_zh": "验证",
    "type": "concept",
    "parent": null,
    "order": 2,
    "position": "自下第 2 格",
    "description_zh": "定义之后被验证。"
  },
  {
    "id": "lvl_understand",
    "label_en": "Understand",
    "label_zh": "理解",
    "type": "concept",
    "parent": null,
    "order": 3,
    "position": "自下第 3 格",
    "description_zh": "验证之后被理解。"
  },
  {
    "id": "lvl_commit",
    "label_en": "Commit",
    "label_zh": "承诺",
    "type": "concept",
    "parent": null,
    "order": 4,
    "position": "自下第 4 格",
    "description_zh": "组织对特征作出承诺。"
  },
  {
    "id": "lvl_disseminate",
    "label_en": "Disseminate",
    "label_zh": "传播",
    "type": "concept",
    "parent": null,
    "order": 5,
    "position": "自下第 5 格",
    "description_zh": "承诺之后在组织内传播。"
  },
  {
    "id": "lvl_evolve",
    "label_en": "Evolve",
    "label_zh": "演进",
    "type": "concept",
    "parent": null,
    "order": 6,
    "position": "每列最上一格",
    "description_zh": "最高层级：具备演进路径。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_cumulative_levels",
    "kind": "sequence",
    "name_zh": "六个层级的累积阶梯",
    "steps": [
      "lvl_define",
      "lvl_validate",
      "lvl_understand",
      "lvl_commit",
      "lvl_disseminate",
      "lvl_evolve"
    ],
    "description_zh": "自下而上逐级满足；任一等级的深青格都从 Define 起连续向上，说明上层以下层为前提。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_likert",
    "title_zh": "七级李克特量表 × 六个累积层级（逐格转录）",
    "columns": [
      "层级（图内自上而下）",
      "Strongly Agree 非常同意",
      "Agree 同意",
      "Somewhat Agree 比较同意",
      "Neutral 中立",
      "Somewhat Disagree 比较不同意",
      "Disagree 不同意",
      "Strongly Disagree 非常不同意"
    ],
    "rows": [
      [
        "Evolve 演进",
        "已存在/已满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足"
      ],
      [
        "Disseminate 传播",
        "已存在/已满足",
        "已存在/已满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足"
      ],
      [
        "Commit 承诺",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足"
      ],
      [
        "Understand 理解",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "不存在/未满足",
        "不存在/未满足",
        "不存在/未满足"
      ],
      [
        "Validate 验证",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "不存在/未满足",
        "不存在/未满足"
      ],
      [
        "Define 定义",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "已存在/已满足",
        "不存在/未满足"
      ]
    ],
    "cell_legend": [
      "已存在/已满足 = 深青色实心格（Existent/Fulfilled）",
      "不存在/未满足 = 白色格（Nonexistent/Not Fulfilled）"
    ],
    "notes_zh": "行序与图一致（Evolve 在最上）；中文稿表 A-1 给出 7–1 分与各等级已具备层级的对应关系，与本表一致。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深青色实心方格",
    "meaning_zh": "Existent/Fulfilled（已存在/已满足）",
    "explicit": true
  },
  {
    "symbol": "白色方格（黑边）",
    "meaning_zh": "Nonexistent/Not Fulfilled（不存在/未满足）",
    "explicit": true
  },
  {
    "symbol": "列（自左向右）",
    "meaning_zh": "七级李克特等级，从非常同意到非常不同意",
    "explicit": false
  },
  {
    "symbol": "行（自下而上）",
    "meaning_zh": "六个累积层级：定义→验证→理解→承诺→传播→演进",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "7 列并排，列顶为等级名（部分换行）；每列内 6 个等宽方格自下而上为 Define、Validate、Understand、Commit、Disseminate、Evolve；底部为图例：深青块“Existent/Fulfilled”、白块“Nonexistent/Not Fulfilled”。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图未说明六个层级各自的操作性定义；本分析只按层级名与累积填充关系描述，不扩展定义。",
    "“Very Strongly Agree”之类中间档不存在：原图只有 7 档，且“Somewhat Agree/Disagree”位于 Neutral 两侧。",
    "中文稿中文化图在“同意”列的“传播”格有半格填充异常，按英文原图与表 A-1 应为整格已满足。"
  ],
  "analyzed_from": [
    "英文 PDF 第 49 页原图截图（2×2 放大分块，逐列核对填充格）",
    "英文 PDF 第 49 页正文（A.1 量表说明）",
    "中文稿 G212e_数字技术采用就绪度评估.md 第 699–745 行（含图内标签对照表与表 A-1）",
    "figs/zh/g212e_figA-1_zh.png",
    "figs/g212e_figA-1_en.png（自动相似度 0.973）"
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
