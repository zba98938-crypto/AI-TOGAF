# G21D/fig2-1 · 拟议的国际事务与贸易部门 L1–L3 要素的结构与内容概览

> 当前图示解析：[Markdown](../../architecture/diagrams/G21D/fig2-1.md) · [JSON](../../architecture/diagrams/G21D/fig2-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21De.pdf`；SHA-256：`220ead5fef846c52417b9b7a915ff4a64f327680b384c369840926b85958786a`。

## 原图 · PDF 第 25 页

![英文原图](../assets/G21D/fig2-1-p0025.png)

PDF 坐标：`[74.0, 132.3, 538.0, 310.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
e Open
If
-
-
Trade
/
International Affairs
\
Development and Aid -
Global Trade
Foreign Affairs
(International Development )
/
Humanitarian Aid
)
Export Control
Foreign Treaties
Import Control
-
y,
```

## 概要（历史解释；局部修正见上）

政府参考模型中“国际事务与贸易”部门的 L1–L3 分解：1 个部门、3 个功能、7 项服务。

## 目的（历史解释；局部修正见上）

第 2 章开篇用这张图概览“国际事务与贸易”部门（L1）下的功能（L2）与服务（L3），随后的表 2-1 逐项给出说明。它是 11 个部门图中的第一张，也是图 1-1 三层结构的第一个具体展开；附录 A 第 48 页把它与图 3-1、图 4-1 汇总在同一页。

## 阅读顺序（历史解释；局部修正见上）

最外层浅蓝色大框是 L1 部门，顶部白色粗体字是部门名称。框内三个等宽的白色圆角框是 L2 功能，从左到右依次为发展与援助、贸易、国际事务。每个功能框里自上而下排列的胶囊形小框是 L3 服务。图中没有连线或箭头，上下级关系完全由框的嵌套表达，同一功能内的服务是并列的。

## 关键含义（历史解释；局部修正见上）

- 本部门分为 3 个 L2 功能：发展与援助（2 项服务）、贸易（3 项）、国际事务（2 项），共 7 项 L3 服务，是 11 个部门图中服务最少的一个。
- 按表 2-1 的功能说明：发展与援助为欠发达经济体提供发展援助与人道主义援助；贸易通过促进海外贸易增加繁荣；国际事务通过提供海外外交建议、谈判伙伴关系与协议来维护国际关系。
- 三个功能对应部门定义中的三部分：对国际经济体的财政支持与援助计划（发展与援助）、与国际经济体的贸易（贸易）、条约与外交关系（国际事务）。
- 发展与援助下两项服务的区别：国际发展通过货物与服务的自愿转移援助发展中经济体；人道主义援助支持欠发达经济体实现增长并从冲突中恢复。
- 与进口有关的事务分在四个部门：本图贸易下的进口管制（监管货物进入本国的国际采购与流动，确保遵守国内外协议与准则）、海关检查与清关（图 7-1）、进口关税征收（图 8-1）、进口单证受理（图 4-1 的进口管理）。
- 国际安全不在本部门：国际安全援助与情报行动在国防与安全部门的情报与国际安全功能下（图 3-1）。

## 层级（历史解释；局部修正见上）

三层严格树形：L1 部门“国际事务与贸易”（最外层框）→ 3 个 L2 功能（白色圆角框）→ 7 个 L3 服务（胶囊框）。每项服务只属于一个功能，对应图 1-1 中“部门—功能—服务”的组成关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。服务框位于功能框内，表示该服务属于该功能；功能框位于部门框内，表示该功能属于本部门（图 1-1 用菱形组合线表示同样的组成关系）。元素清单用 parent/level 记录这种嵌套，因此关系清单为空。

## 易误读点（历史解释；局部修正见上）

- 部门名“International Affairs and Trade”包含两个功能的名称“International Affairs”“Trade”，但功能只是部门的组成部分，与部门不是同一个框。
- 同一功能内服务的上下次序不表示优先级或流程先后。
- 中文稿引用的中文化 PNG 字号不统一（“发展与援助”比另两个功能标题大），不能用字号判断层级，应以框的嵌套为准。
- 图框下方的浅灰色线条是 PDF 评估版水印的残影，不属于图的内容。

## 元素

```json
[
  {
    "id": "l1_international_affairs_trade",
    "label_en": "International Affairs and Trade",
    "label_zh": "国际事务与贸易",
    "type": "other",
    "notation_type": "GRM L1 部门（Sector）",
    "parent": null,
    "level": 1,
    "position": "最外层浅蓝色框，标题在顶部居中",
    "description_zh": "GRM 第 1 层“部门”，即政府的一个业务领域；词表没有对应类型，故用 other。"
  },
  {
    "id": "l2_development_aid",
    "label_en": "Development and Aid",
    "label_zh": "发展与援助",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_international_affairs_trade",
    "level": 2,
    "order": 1,
    "position": "左",
    "description_zh": "为欠发达经济体提供发展援助与人道主义援助（表 2-1）。"
  },
  {
    "id": "l2_trade",
    "label_en": "Trade",
    "label_zh": "贸易",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_international_affairs_trade",
    "level": 2,
    "order": 2,
    "position": "中",
    "description_zh": "通过促进海外贸易增加繁荣（表 2-1）。"
  },
  {
    "id": "l2_international_affairs",
    "label_en": "International Affairs",
    "label_zh": "国际事务",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_international_affairs_trade",
    "level": 2,
    "order": 3,
    "position": "右",
    "description_zh": "通过提供海外外交建议、谈判伙伴关系与协议来维护国际关系（表 2-1）。"
  },
  {
    "id": "l3_international_development",
    "label_en": "International Development",
    "label_zh": "国际发展",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_development_aid",
    "level": 3,
    "order": 1,
    "description_zh": "通过货物与服务的自愿转移援助发展中经济体。"
  },
  {
    "id": "l3_humanitarian_aid",
    "label_en": "Humanitarian Aid",
    "label_zh": "人道主义援助",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_development_aid",
    "level": 3,
    "order": 2,
    "description_zh": "支持欠发达经济体实现增长并从冲突中恢复。"
  },
  {
    "id": "l3_global_trade",
    "label_en": "Global Trade",
    "label_zh": "全球贸易",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_trade",
    "level": 3,
    "order": 1,
    "description_zh": "通过促进海外贸易、便利货物与服务流动来增加经济财富。"
  },
  {
    "id": "l3_export_control",
    "label_en": "Export Control",
    "label_zh": "出口管制",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_trade",
    "level": 3,
    "order": 2,
    "description_zh": "监管货物出口的国际销售与流动，确保遵守国内外协议与准则。"
  },
  {
    "id": "l3_import_control",
    "label_en": "Import Control",
    "label_zh": "进口管制",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_trade",
    "level": 3,
    "order": 3,
    "description_zh": "监管货物进入本国的国际采购与流动，确保遵守国内外协议与准则。"
  },
  {
    "id": "l3_foreign_affairs",
    "label_en": "Foreign Affairs",
    "label_zh": "外交事务",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_international_affairs",
    "level": 3,
    "order": 1,
    "description_zh": "通过外交协助、与国际政府磋商作出国际贡献。"
  },
  {
    "id": "l3_foreign_treaties",
    "label_en": "Foreign Treaties",
    "label_zh": "外交条约",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_international_affairs",
    "level": 3,
    "order": 2,
    "description_zh": "监督现有条约，谈判伙伴关系与正式协议。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "浅蓝色大圆角框 + 顶部白色粗体标题",
    "meaning_zh": "L1 部门（Sector）",
    "explicit": false
  },
  {
    "symbol": "白色圆角框 + 黑色粗体标题",
    "meaning_zh": "L2 功能（Function），属于所在部门",
    "explicit": false
  },
  {
    "symbol": "白色胶囊形小框（细灰边）",
    "meaning_zh": "L3 服务（Service），属于所在功能",
    "explicit": false
  },
  {
    "symbol": "框的嵌套",
    "meaning_zh": "组成/归属关系，与图 1-1 中菱形组合线表达的“部门—功能—服务”关系相同",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "最外层浅蓝色圆角框（顶部居中为部门标题，右上角为版权署名）内，三个等宽功能框从左到右并排：发展与援助（2 项）、贸易（3 项）、国际事务（2 项）；各框内服务自上而下单列排列。"
}
```

## 相关图

```json
[
  {
    "target": "G21D/fig1-1",
    "relation": "detail_of",
    "note_zh": "图 1-1 的三层结构（L1 部门—L2 功能—L3 服务）在“国际事务与贸易”部门的展开"
  },
  {
    "target": "G21D/fig3-1",
    "relation": "complements",
    "note_zh": "同一模板的相邻部门概览（国防与安全）；外交与条约在本图，国际安全援助与情报在图 3-1"
  },
  {
    "target": "G21D/appA-p48",
    "relation": "related",
    "note_zh": "附录 A 第 48 页（PDF 第 68 页）原样收录本图，与图 3-1、图 4-1 同页"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 25 页原图截图",
    "英文 PDF 第 25–26 页正文（第 2 章开篇、表 2-1）",
    "英文 PDF 第 68 页附录 A 图示（同内容面板，用于复核标签）",
    "中文稿 G21De_政府参考模型.md 第 209–248 行",
    "figs/zh/g21de_fig2-1_zh.png（逐项对照）"
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
