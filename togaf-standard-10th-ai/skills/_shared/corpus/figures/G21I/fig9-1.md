# G21I/fig9-1 · 微服务的开发、部署与执行

> 当前图示解析：[Markdown](../../architecture/diagrams/G21I/fig9-1.md) · [JSON](../../architecture/diagrams/G21I/fig9-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Ie.pdf`；SHA-256：`279f6c06124f49a147a168591965805115b2fc976eea2664e41e491ac5d163bf`。

## 原图 · PDF 第 41 页

![英文原图](../assets/G21I/fig9-1-p0041.png)

PDF 坐标：`[74.0, 499.8, 538.0, 685.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
a” S°G
```

## 概要（历史解释；局部修正见上）

微服务从源单元与库构建为部署单元，再部署为一个或多个执行单元，运行在执行环境中。

## 目的（历史解释；局部修正见上）

第 9 章（阶段 D：技术架构）用本图说明微服务的开发、部署与执行，支撑“微服务独立开发、可独立部署”这一特征；阶段 D 需要规定微服务的部署机制和执行环境。

## 阅读顺序（历史解释；局部修正见上）

从左到右读：左侧上下两组输入是源单元和库，经“构建”箭头得到中间的部署单元，再经“部署”箭头得到右侧的执行单元；执行单元下方的长方形是执行环境。每种图形都画成多层叠放，表示有多个。

## 关键含义（历史解释；局部修正见上）

- 每个微服务有自己的源单元，包含实现该微服务 ABF 的代码；源单元不与其他微服务的源单元共享代码，也不能访问它们的数据。
- 源单元可以使用库，但库只提供与业务无关的功能；构建时库与源单元一起进入部署单元。
- 每个微服务有一个部署单元，由它的源单元和所用的库构建而成；一个部署单元不能包含多个微服务的代码。
- 部署单元部署为一个执行单元；在大规模系统中，部署为运行相同代码的多个执行单元。
- 执行单元运行在执行环境中；阶段 D 的补充步骤之一是规定微服务的部署机制和执行环境。
- 编程语言、库、开发工具和构建机制的选择可交给各微服务的 DevOps 团队，但可能在一定程度上受技术架构约束。

## 层级（历史解释；局部修正见上）

没有嵌套。层叠的图形只表示同类对象有多个；执行环境画在执行单元下方，表示承载关系，不是包含框。

## 线条含义（历史解释；局部修正见上）

只有两个大块箭头，均从左指向右：“构建”从源单元和库指向部署单元，“部署”从部署单元指向执行单元。执行单元与执行环境之间没有连线，承载关系由上下位置表达（关系清单中标为推断）。

## 易误读点（历史解释；局部修正见上）

- 层叠图形表示“有多个”，不表示版本历史或层级。
- 库不是共享的业务代码：原文规定库只用于与业务无关的功能，微服务之间不共享业务代码。
- 一个部署单元可以对应多个执行单元（运行相同代码的副本），但一个部署单元不能包含多个微服务的代码。
- 原图左上方的空心大字是英文 PDF 的“Evaluation Copy”水印，不是图的内容。

## 元素

```json
[
  {
    "id": "source_units",
    "label_en": "Source Units",
    "label_zh": "源单元",
    "type": "artifact",
    "order": 1,
    "position": "左上",
    "description_zh": "每个微服务一个，包含实现其 ABF 的代码。"
  },
  {
    "id": "libraries",
    "label_en": "Libraries",
    "label_zh": "库",
    "type": "artifact",
    "order": 1,
    "position": "左下",
    "description_zh": "只提供与业务无关的功能。"
  },
  {
    "id": "deployment_units",
    "label_en": "Deployment Units",
    "label_zh": "部署单元",
    "type": "artifact",
    "order": 2,
    "position": "中",
    "description_zh": "每个微服务一个，由源单元和所用库构建。"
  },
  {
    "id": "execution_units",
    "label_en": "Execution Units",
    "label_zh": "执行单元",
    "type": "technology",
    "order": 3,
    "position": "右上",
    "description_zh": "部署单元的运行实例，可为一个或多个。"
  },
  {
    "id": "execution_env",
    "label_en": "Execution Environment",
    "label_zh": "执行环境",
    "type": "technology",
    "position": "右下"
  }
]
```

## 关系

```json
[
  {
    "from": "source_units",
    "to": "deployment_units",
    "type": "flow",
    "label_en": "Build",
    "label_zh": "构建",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "cardinality": "1:1",
    "description_zh": "每个微服务的源单元构建为该微服务的一个部署单元"
  },
  {
    "from": "libraries",
    "to": "deployment_units",
    "type": "flow",
    "label_en": "Build",
    "label_zh": "构建",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "源单元所用的库一并构建进部署单元（与源单元共用同一个“构建”箭头）"
  },
  {
    "from": "deployment_units",
    "to": "execution_units",
    "type": "flow",
    "label_en": "Deploy",
    "label_zh": "部署",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "cardinality": "1:1..*",
    "description_zh": "一个部署单元部署为一个执行单元，大规模时为运行相同代码的多个执行单元"
  },
  {
    "from": "execution_env",
    "to": "execution_units",
    "type": "serving",
    "label_zh": "承载",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "执行环境画在执行单元下方"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_lifecycle",
    "kind": "sequence",
    "name_zh": "微服务的开发、部署与执行",
    "steps": [
      "source_units",
      "deployment_units",
      "execution_units"
    ],
    "description_zh": "构建时库与源单元一起进入部署单元；执行单元运行在执行环境中。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_cardinality",
    "title_zh": "各单元的数量规则（据原文 p42）",
    "columns": [
      "对象",
      "与微服务的对应",
      "规则"
    ],
    "rows": [
      [
        "源单元",
        "每个微服务 1 个",
        "不与其他微服务的源单元共享代码，不能访问其数据"
      ],
      [
        "库",
        "可选，可被使用",
        "只用于与业务无关的功能"
      ],
      [
        "部署单元",
        "每个微服务 1 个",
        "由源单元及其所用库构建；不能包含多个微服务的代码"
      ],
      [
        "执行单元",
        "每个部署单元 1 个或多个",
        "大规模系统中为运行相同代码的多个执行单元"
      ]
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "层叠的折角文档",
    "meaning_zh": "源单元（源代码）",
    "explicit": false
  },
  {
    "symbol": "层叠的波浪边图形",
    "meaning_zh": "库",
    "explicit": false
  },
  {
    "symbol": "层叠圆",
    "meaning_zh": "部署单元（构建产物）",
    "explicit": false
  },
  {
    "symbol": "层叠六边形",
    "meaning_zh": "执行单元（运行实例）",
    "explicit": false
  },
  {
    "symbol": "长方形",
    "meaning_zh": "执行环境",
    "explicit": false
  },
  {
    "symbol": "多层叠放",
    "meaning_zh": "同类对象有多个",
    "explicit": false
  },
  {
    "symbol": "带文字的大块箭头",
    "meaning_zh": "构建 / 部署两个步骤，箭头指向产物",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "左列上下两组：源单元（层叠折角文档）在上，库（层叠波浪边图形）在下；中间是“构建”箭头和部署单元（3 个层叠圆）；右侧是“部署”箭头和执行单元（3 个层叠六边形），执行单元下方是横向长方形“执行环境”。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 41 页原图截图（220 dpi）",
    "英文 PDF 第 41–42 页正文",
    "中文稿 G21Ie_微服务架构.md 第 575–612 行（含图内标签对照表 L587–L597）",
    "figs/zh/g21ie_fig9-1_zh.png",
    "figs/g21ie_fig9-1_en.png（自动相似度 0.988）"
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
