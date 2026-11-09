# G21I/fig5-1 · SOA 治理支持 IT 治理与企业架构治理

> 当前图示解析：[Markdown](../../architecture/diagrams/G21I/fig5-1.md) · [JSON](../../architecture/diagrams/G21I/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Ie.pdf`；SHA-256：`279f6c06124f49a147a168591965805115b2fc976eea2664e41e491ac5d163bf`。

## 原图 · PDF 第 26 页

![英文原图](../assets/G21I/fig5-1-p0026.png)

PDF 坐标：`[125.6, 36.0, 486.4, 248.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Supports
Supports
Extends
Constrains
```

## 概要（历史解释；局部修正见上）

MSA/云原生治理扩展 IT 治理、受企业架构治理约束；IT 治理与企业架构治理相互对齐并共同支持企业治理。

## 目的（历史解释；局部修正见上）

第 5.3 节（预备阶段的治理与支持策略）用本图给出 MSA 治理与企业架构治理、IT 治理之间关系的高层视图，说明 MSA 团队要走两条并行的治理轨道：只对本 MSA 生效的自主治理决策，同时不越出企业设定的护栏。

## 阅读顺序（历史解释；局部修正见上）

自上而下分三层读：顶部是企业治理；中间是并列的 IT 治理（左）和企业架构治理（右），两者用双向箭头“对齐”，并各有一条向上箭头“支持”企业治理；底部是 MSA/云原生治理，左侧箭头向上“扩展”IT 治理，右侧箭头从企业架构治理向下“约束”它。箭头所指为关系的宾语。

## 关键含义（历史解释；局部修正见上）

- IT 治理和企业架构治理是同级的两个治理领域，二者相互对齐，并共同支持企业治理。
- MSA/云原生治理与上层有两种不同的关系：它扩展 IT 治理（在 IT 治理之上增加 MSA 专属的治理内容），同时受企业架构治理约束。
- “约束”对应正文所说的护栏：开发团队可以自由选择最合适的技术与方法，但必须遵守企业架构师制定的总体治理规则，或显式申请豁免；不遵守会使技术混乱与不稳定制度化。
- 正文强调 MSA 这类分布式架构的治理与传统企业架构（包括聚焦 SOA 的企业架构）大不相同；治理是应用要求的过程，应由架构师与实施团队并肩持续开展。
- 正文列出 MSA 需要的治理工具：变更发布前适当层级的评审（“四眼”原则）、生产管道的最小权限、稳健的变更监控、监控与测试的高度自动化。
- 图题仍写“SOA 治理”，图内最底层却是“MSA/云原生治理”；原文同页说明 MSA 治理参考模型与 SOA 治理参考模型大体相同，只是范围限于 MSA 过程（图 5-2）。

## 层级（历史解释；局部修正见上）

三层：企业治理在最上层；IT 治理与企业架构治理在中层，二者同级；MSA/云原生治理在最下层。上下位置表示治理的层次，没有框中框的包含关系。

## 线条含义（历史解释；局部修正见上）

5 条蓝色粗箭头，均带标签：IT 治理→企业治理“支持”；企业架构治理→企业治理“支持”；IT 治理↔企业架构治理“对齐”（双向）；MSA/云原生治理→IT 治理“扩展”（箭头朝上）；企业架构治理→MSA/云原生治理“约束”（箭头朝下）。

## 易误读点（历史解释；局部修正见上）

- “约束”的方向是企业架构治理约束 MSA/云原生治理，不是反过来；“扩展”的方向是 MSA/云原生治理扩展 IT 治理。
- IT 治理与企业架构治理是同级、相互对齐的关系，不是上下级。
- 图题中的“SOA”不代表图在讲 SOA 治理，图中的对象是 MSA/云原生治理。
- 未被引用的 figs/g21i_fig5-1.svg 与本图同号，画的却是“MSA 在各 ADM 阶段的关注点”，不能当作本图使用。

## 元素

```json
[
  {
    "id": "corp_gov",
    "label_en": "Corporate Governance",
    "label_zh": "企业治理",
    "type": "concept",
    "level": 1,
    "position": "顶部通栏"
  },
  {
    "id": "it_gov",
    "label_en": "IT Governance",
    "label_zh": "IT 治理",
    "type": "concept",
    "level": 2,
    "position": "中层左"
  },
  {
    "id": "ea_gov",
    "label_en": "Enterprise Architecture Governance",
    "label_zh": "企业架构治理",
    "type": "concept",
    "level": 2,
    "position": "中层右"
  },
  {
    "id": "msa_gov",
    "label_en": "MSA/Cloud-Native Governance",
    "label_zh": "微服务架构/云原生治理",
    "type": "concept",
    "level": 3,
    "position": "底部通栏",
    "description_zh": "MSA 团队自己的治理，只适用于本 MSA。"
  }
]
```

## 关系

```json
[
  {
    "from": "it_gov",
    "to": "corp_gov",
    "type": "serving",
    "label_en": "Supports",
    "label_zh": "支持",
    "explicit": true,
    "line": "thick",
    "arrow": "forward"
  },
  {
    "from": "ea_gov",
    "to": "corp_gov",
    "type": "serving",
    "label_en": "Supports",
    "label_zh": "支持",
    "explicit": true,
    "line": "thick",
    "arrow": "forward"
  },
  {
    "from": "it_gov",
    "to": "ea_gov",
    "type": "association",
    "label_en": "Aligns",
    "label_zh": "对齐",
    "explicit": true,
    "line": "thick",
    "arrow": "both",
    "description_zh": "双向箭头"
  },
  {
    "from": "msa_gov",
    "to": "it_gov",
    "type": "specialization",
    "label_en": "Extends",
    "label_zh": "扩展",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "箭头朝上指向 IT 治理：MSA/云原生治理在 IT 治理基础上扩展"
  },
  {
    "from": "ea_gov",
    "to": "msa_gov",
    "type": "governs",
    "label_en": "Constrains",
    "label_zh": "约束",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "箭头朝下指向 MSA/云原生治理：企业架构治理设定护栏"
  }
]
```

## 图例

```json
[
  {
    "symbol": "圆角蓝框",
    "meaning_zh": "治理领域",
    "explicit": false
  },
  {
    "symbol": "带标签的蓝色箭头",
    "meaning_zh": "治理领域之间的关系，箭头指向关系的宾语",
    "explicit": false
  },
  {
    "symbol": "双向箭头",
    "meaning_zh": "相互对齐",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "三层：顶部一个通栏宽框（企业治理）；中间左右两个窄框（IT 治理、企业架构治理）；底部一个通栏宽框（MSA/云原生治理）。左右两侧各有一条竖向箭头列，中间一条水平双向箭头。"
}
```

## 相关图

```json
[
  {
    "target": "G21I/fig5-2",
    "relation": "complements",
    "note_zh": "同在第 5.3 节：本图说明 MSA 治理在整体治理体系中的位置，图 5-2 给出 MSA 治理参考模型本身的组成"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "“扩展”记为 specialization（MSA/云原生治理是 IT 治理的扩展），属解析者对关系类型的选择；原文没有进一步解释。",
    "中文稿 README 提到的“G21I 图 2-1/5-1 错配”没有留下具体记录；从现状推断，这两个自拟 SVG 曾分别被当作图 2-1、图 5-1 引用，修正后图 5-1 改引中文化 PNG，两个 SVG 都成了未被引用的文件。"
  ],
  "analyzed_from": [
    "英文 PDF 第 26 页原图截图（220 dpi）及像素扫描（确认 5 个箭头头部的位置与方向）",
    "英文 PDF 第 25–26 页正文；全文检索 SVG 中的术语",
    "中文稿 G21Ie_微服务架构.md 第 108–128、270–306 行（含图内标签对照表 L293–L304）",
    "中文稿 README.md 第 19 行、QA-文档对比核查报告.md 第 34 行",
    "figs/zh/g21ie_fig5-1_zh.png、figs/g21ie_fig5-1_en.png、figs/g21i_fig5-1.svg 与 figs/g21i_fig2-1.svg 源码"
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
