# G212/fig5-1 · 数字技术采用的四步路线图

> 当前图示解析：[Markdown](../../architecture/diagrams/G212/fig5-1.md) · [JSON](../../architecture/diagrams/G212/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G212e.pdf`；SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

## 原图 · PDF 第 39 页

![英文原图](../assets/G212/fig5-1-p0039.png)

PDF 坐标：`[48.2, 158.5, 460.7, 459.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Step 4: Address Shortcomings and Initiate
Digital Technology Adoption
Step 3: Identify Factors Needing Management Attention
Step 2: Perform Digital Technology Readiness Assessment
Step 1: Select the Adoption Approach
.
ne
```

## 概要（历史解释；局部修正见上）

用一条上升的箭头把数字技术采用概括为四个前后相继的步骤。

## 目的（历史解释；局部修正见上）

第 5 章开篇先给全局：作者用一条上升箭头把后面 5.1–5.4 节要展开的四步一次列出，让读者先看到路线，再逐节深入；正文说明四个步骤随后会详细解释。

## 阅读顺序（历史解释；局部修正见上）

从箭头左下端读起，沿箭杆向右上：第一个圆点对应 Step 1，依次到箭头尖端的 Step 4。圆点只是步骤位置标记，标签排在圆点右侧；箭头方向就是步骤先后。图中没有坐标轴，曲线的上升只是示意“推进”，不带数值含义。

## 关键含义（历史解释；局部修正见上）

- 四步依次为：选择采用方法 → 执行数字技术就绪度评估 → 识别需要管理关注的因素 → 弥补短板并启动数字技术采用。
- 四步与后文一一对应：步骤 1 展开为图 5-2 的 ABCD 框架，步骤 3 对应图 5-3 的缺失因素后果，步骤 4 对应图 5-4 的因素递进。
- 箭头自左下向右上，只表示单向推进；图中没有回到前一步的反馈箭头。
- 路线图只给步骤名称，没有时间、责任人或交付物；这些内容不在本图，需看各节正文。
- 第 4 步把“弥补短板”和“启动采用”合为一步，说明评估结果必须落到行动，而不是止于诊断。
- 图中的四个圆点大小相同，不表示工作量、优先级或阶段长度。

## 层级（历史解释；局部修正见上）

只有一层：4 个并列步骤按顺序排在一条箭头上；没有子步骤或分组。

## 线条含义（历史解释；局部修正见上）

一条深青色粗箭头从页面左下弯向右上，箭头尖端指向 Step 4，表示四步的单向推进；4 个灰色圆点贴在箭杆上，分别标记 Step 1–4 的位置，圆点与文字之间没有引线。箭头是唯一的连线，没有分支、汇合或回路。

## 易误读点（历史解释；局部修正见上）

- 这四步不是 TOGAF ADM 的四个阶段，而是本指南给出的数字技术采用路线图；不要与 ADM 阶段 A–D 对应。
- 曲线的上升不表示后一步“价值更高”或“难度更大”，图中没有纵轴或刻度。
- 灰色圆点不是评分、里程碑日期或完成状态，只是步骤在箭杆上的位置标记。
- 第 1 步“选择采用方法”不是选技术产品，而是按 ABCD 框架选择组织的采用方式（见 5.1 节）。

## 元素

```json
[
  {
    "id": "s1_approach",
    "label_en": "Step 1: Select the Adoption Approach",
    "label_zh": "步骤 1：选择采用方法",
    "type": "phase",
    "parent": null,
    "order": 1,
    "position": "左下，箭头起点"
  },
  {
    "id": "s2_assess",
    "label_en": "Step 2: Perform Digital Technology Readiness Assessment",
    "label_zh": "步骤 2：执行数字技术就绪度评估",
    "type": "phase",
    "parent": null,
    "order": 2,
    "position": "中下"
  },
  {
    "id": "s3_factors",
    "label_en": "Step 3: Identify Factors Needing Management Attention",
    "label_zh": "步骤 3：识别需要管理关注的因素",
    "type": "phase",
    "parent": null,
    "order": 3,
    "position": "中上"
  },
  {
    "id": "s4_address",
    "label_en": "Step 4: Address Shortcomings and Initiate Digital Technology Adoption",
    "label_zh": "步骤 4：弥补短板并启动数字技术采用",
    "type": "phase",
    "parent": null,
    "order": 4,
    "position": "右上，箭头尖端"
  }
]
```

## 关系

```json
[
  {
    "from": "s1_approach",
    "to": "s4_address",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "一根箭头贯通四步；箭杆上的 4 个圆点依次对应步骤 1–4，箭头尖端指向步骤 4"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_four_steps",
    "kind": "sequence",
    "name_zh": "数字技术采用四步路线",
    "steps": [
      "s1_approach",
      "s2_assess",
      "s3_factors",
      "s4_address"
    ],
    "description_zh": "自左下向右上单向推进，无反馈回路。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深青色粗箭头（向右上弯曲）",
    "meaning_zh": "四步的单向推进方向",
    "explicit": false
  },
  {
    "symbol": "灰色圆点",
    "meaning_zh": "步骤在路线上的位置标记（非评分/非里程碑日期）",
    "explicit": false
  },
  {
    "symbol": "Step 1–4 标签",
    "meaning_zh": "四个步骤的名称，按圆点由下往上排序",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "一条粗箭头自左下角起，先陡后缓地弯向右上，箭头尖端在右上方；4 个灰点沿箭杆由下往上排列，Step 1 标签在左下，Step 2–4 依次向右上错落，形成阶梯式文字块。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "曲线上升没有坐标轴或刻度，只能作方向性理解；“上升”不构成量化结论。",
    "四个圆点在箭杆上的间距不完全相等，但图中未说明间距含义，本分析不据此推断阶段长度。"
  ],
  "analyzed_from": [
    "英文 PDF 第 39 页原图截图（2×2 放大分块）",
    "英文 PDF 第 39 页正文",
    "中文稿 G212e_数字技术采用就绪度评估.md 第 487–502 行",
    "figs/zh/g212e_fig5-1_zh.png",
    "figs/g212e_fig5-1_en.png（自动相似度 0.991）"
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
