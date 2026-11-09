# G238/fig1-1 · 本文档使用的 ArchiMate 建模元素

> 当前图示解析：[Markdown](../../architecture/diagrams/G238/fig1-1.md) · [JSON](../../architecture/diagrams/G238/fig1-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G238e.pdf`；SHA-256：`87e00e009377a887627417ceffc28b1f480bfaf57c9c84ee6f8757cc5c1c9444`。

## 原图 · PDF 第 11 页

![英文原图](../assets/G238/fig1-1-p0011.png)

PDF 坐标：`[112.7, 480.3, 499.3, 596.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business ()
Function
```

## 概要（历史解释；局部修正见上）

本文档只使用四个 ArchiMate 元素——业务功能、应用功能、利益相关者、目标——并标明它们所属的方面。

## 目的（历史解释；局部修正见上）

在进入参考模型前先固定记法：告诉读者后续所有模型都只用这四类元素，且业务/应用功能与动机方面的符号、颜色各不相同，避免把后面的方框图误读成流程或组织图。

## 阅读顺序（历史解释；局部修正见上）

先看左侧两条横向灰带：Business 带内是黄色圆角矩形“Business Function”，Application 带内是青色圆角矩形“Application Function”；两者右上角都带同一个功能（旗帜）图标，只能靠颜色和所在灰带区分。再看右侧 Motivation 带：上下两个淡紫色切角框分别是 Stakeholder（双圆图标）和 Goal（靶心图标）。图中没有箭头。

## 关键含义（历史解释；局部修正见上）

- 全图只有四个元素：Business Function、Application Function、Stakeholder、Goal；没有流程、服务、数据、应用组件等元素，所以后文参考模型只做功能分解。
- 颜色即方面：业务层用黄色、应用层用青色、动机方面用淡紫色；形状本身不区分元素类型，功能与应用功能都是圆角矩形。
- 每个元素右上角的小图标才是 ArchiMate 类型标记：功能为旗帜状图标，Stakeholder 为双圆，Goal 为同心圆靶心。
- Stakeholder 与 Goal 属于动机方面，回答能力“为何存在、为谁服务”，与业务/应用功能不在同一分类维度。
- 该图是记法图例而非架构模型：没有连线、没有层级关系，后续图 2-1、4-1、4-2、4-3 复用这里的符号。
- 图 1-1 只声明了文档使用的元素子集，不代表 ArchiMate 标准的全部元素。

## 层级（历史解释；局部修正见上）

两层：外层是三个方面的分组带（Business、Application、Motivation），带内是元素符号示例。元素示例之间没有上下级；方面带只是分类容器，不是架构层级。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。业务功能/应用功能与动机元素之间的关系、以及功能之间的组成关系都不在本图表达。

## 易误读点（历史解释；局部修正见上）

- 不要把 Business / Application / Motivation 三条带读成自下而上的架构分层或成熟度等级，它们只是 ArchiMate 的方面分类。
- 不要因为业务功能和应用功能形状相同就认为二者可互换：区别在颜色与所在方面带，后续模型里也沿用这一约定。
- 不要把这四类当成文档涉及的全部 ArchiMate 元素；正文只声明“本文档使用的元素”。
- 中文稿引用的 figs/g238_archimate_legend.svg 丢掉了方面带、图标和正确配色，不能据此理解原图的分类逻辑。

## 元素

```json
[
  {
    "id": "band_business",
    "label_en": "Business",
    "label_zh": "业务层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左上灰带",
    "description_zh": "ArchiMate 业务方面的分组带。"
  },
  {
    "id": "band_application",
    "label_en": "Application",
    "label_zh": "应用层",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左下灰带",
    "description_zh": "ArchiMate 应用方面的分组带。"
  },
  {
    "id": "band_motivation",
    "label_en": "Motivation",
    "label_zh": "动机方面",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右侧竖带",
    "description_zh": "ArchiMate 动机方面的分组带。"
  },
  {
    "id": "business_function",
    "label_en": "Business Function",
    "label_zh": "业务功能",
    "type": "function",
    "parent": "band_business",
    "level": 2,
    "position": "Business 带内左侧",
    "description_zh": "记法示例；正文定义：基于选定标准（通常是所需业务资源/胜任力）的业务行为集合。"
  },
  {
    "id": "application_function",
    "label_en": "Application Function",
    "label_zh": "应用功能",
    "type": "function",
    "parent": "band_application",
    "level": 2,
    "position": "Application 带内左侧",
    "description_zh": "记法示例；正文定义：可由应用组件执行的自动化行为。"
  },
  {
    "id": "stakeholder",
    "label_en": "Stakeholder",
    "label_zh": "利益相关者",
    "type": "stakeholder",
    "parent": "band_motivation",
    "level": 2,
    "position": "Motivation 带内上方",
    "description_zh": "记法示例；代表个人、团队或组织在架构影响方面的利益角色。"
  },
  {
    "id": "goal",
    "label_en": "Goal",
    "label_zh": "目标",
    "type": "goal",
    "parent": "band_motivation",
    "level": 2,
    "position": "Motivation 带内下方",
    "description_zh": "记法示例；对组织及其利益相关者而言关于意图、方向或期望终态的高层陈述。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色横带 + 左上角标题 Business / Application",
    "meaning_zh": "ArchiMate 方面分组：业务层、应用层",
    "explicit": true
  },
  {
    "symbol": "灰色竖带 + 左上角标题 Motivation",
    "meaning_zh": "ArchiMate 动机方面分组",
    "explicit": true
  },
  {
    "symbol": "黄色圆角矩形 + 右上角旗帜图标",
    "meaning_zh": "业务功能 Business Function",
    "explicit": true
  },
  {
    "symbol": "青色圆角矩形 + 右上角旗帜图标",
    "meaning_zh": "应用功能 Application Function",
    "explicit": true
  },
  {
    "symbol": "淡紫色切角框 + 右上角双圆图标",
    "meaning_zh": "利益相关者 Stakeholder",
    "explicit": true
  },
  {
    "symbol": "淡紫色切角框 + 右上角靶心图标",
    "meaning_zh": "目标 Goal",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "左侧上下两条横向灰带（Business 在上、Application 在下），灰带内各放一个功能示例；右侧一条竖向灰带（Motivation），带内上下排列 Stakeholder 与 Goal。"
}
```

## 相关图

```json
[
  {
    "target": "G238/fig2-1",
    "relation": "legend_for",
    "note_zh": "图 2-1 的业务/应用功能框沿用本图给出的两种功能符号。"
  },
  {
    "target": "G238/fig4-1",
    "relation": "legend_for",
    "note_zh": "图 4-1 的 Stakeholder 与 Goal 使用本图给出的动机方面符号。"
  },
  {
    "target": "G238/fig4-2",
    "relation": "legend_for",
    "note_zh": "图 4-2 的业务功能分解使用本图的功能符号。"
  },
  {
    "target": "G238/fig4-3",
    "relation": "legend_for",
    "note_zh": "图 4-3 的应用功能分解使用本图的功能符号。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原图未画出元素之间的连线，因此 relationships 为空；四类元素只是记法示例，不是某个具体架构的实例。",
    "原图右下角没有可见的版权行，attribution 留空。"
  ],
  "analyzed_from": [
    "英文 PDF 第 11 页图 1-1 截图与 2×2 放大分块",
    "英文 PDF 第 11 页 1.1 节正文",
    "中文稿 G238e_信息架构_商业智能与分析.md 第 94–112 行",
    "figs/g238_archimate_legend.svg 源码"
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
