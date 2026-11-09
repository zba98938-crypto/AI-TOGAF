# G21B/fig5-1 · 自然人内核数据

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig5-1.md) · [JSON](../../architecture/diagrams/G21B/fig5-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 38 页

![英文原图](../assets/G21B/fig5-1-p0038.png)

PDF 坐标：`[48.2, 62.3, 563.8, 265.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Customer Data — Physical Person
Internal Identification
External Identification
Personal Identification
Data
Keys
Keys
Contact Data
Preferences/Consent
Relationships with Other
Data
Customers
```

## 概要（历史解释；局部修正见上）

自然人内核数据分六类：内部/外部标识键、个人标识数据、联系方式、偏好/同意、与其他客户的关系。

## 目的（历史解释；局部修正见上）

界定 C-MDM 对“自然人”客户应管理的核心数据范围（内核客户数据），为第 5.1 节确定主数据模型边界；每个分类的具体信息项在表 5-1 中展开。

## 阅读顺序（历史解释；局部修正见上）

先读顶部标题“Customer Data – Physical Person”，确认范围是自然人而非组织；再按从左到右、从上到下读六个分类框——上排是三类“识别/描述”数据（内部键、外部键、个人标识），下排是“联系/偏好/关系”数据。六个框是并列的分类，没有先后或主次；框内不再细分，细项见表 5-1。

## 关键含义（历史解释；局部修正见上）

- 自然人内核数据分六类：内部标识键、外部标识键、个人标识数据、联系方式数据、偏好/同意数据、与其他客户的关系。
- 标识键分内部与外部两套：内部键包括业务客户编码与 C-MDM 管理的唯一技术键；外部键如身份证号、外部数据提供方参考号，可用于确保唯一性并支持与外部数据提供方协作提升质量。
- 个人标识数据（名、姓、出生日期、出生地、家庭/婚姻状况、官方职业类别）是描述“这个人是谁”的属性。
- 偏好/同意数据记录客户是否授权组织为特定目的使用某范围数据；正文指出很多组织是在 2018 年因 GDPR 才把它引入 C-MDM。
- 关系数据描述客户与其他自然人的关系（父、母、子女、员工等），可指向 C-MDM 中的另一个自然人。
- 六个分类共同构成“内核”客户数据；组织/法人客户使用图 5-2 的另一套分类（法人描述替代个人标识数据）。

## 层级（历史解释；局部修正见上）

两层：第 1 层是“自然人内核数据”（淡黄色底板 + 标题）；第 2 层是六个并列的分类框。分类之间没有上下级，也没有画出的关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。六个框的并列与分组只由版式（2×3 网格 + 淡黄底板）表达；底板表示它们同属“自然人内核数据”这一范围。

## 易误读点（历史解释；局部修正见上）

- 六个分类不是流程步骤，也不表示数据从标识键流向关系数据。
- “内部标识键”与“外部标识键”不是同一事物的两种写法：前者由组织/C-MDM 管理，后者来自外部（身份证号、外部数据提供方等）。
- 偏好/同意数据不是可选项：正文把它列为核心范围，且与 GDPR 合规直接相关。
- 本图只给分类，不给字段清单；字段清单见表 5-1，不能只看图就设计数据模型。

## 元素

```json
[
  {
    "id": "pp_kernel",
    "label_en": "Customer Data – Physical Person",
    "label_zh": "客户数据——自然人",
    "type": "data",
    "parent": null,
    "level": 1
  },
  {
    "id": "pp_internal_keys",
    "label_en": "Internal Identification Keys",
    "label_zh": "内部标识键",
    "type": "data",
    "parent": "pp_kernel",
    "level": 2,
    "order": 1
  },
  {
    "id": "pp_external_keys",
    "label_en": "External Identification Keys",
    "label_zh": "外部标识键",
    "type": "data",
    "parent": "pp_kernel",
    "level": 2,
    "order": 2
  },
  {
    "id": "pp_personal_id",
    "label_en": "Personal Identification Data",
    "label_zh": "个人标识数据",
    "type": "data",
    "parent": "pp_kernel",
    "level": 2,
    "order": 3
  },
  {
    "id": "pp_contact",
    "label_en": "Contact Data",
    "label_zh": "联系方式数据",
    "type": "data",
    "parent": "pp_kernel",
    "level": 2,
    "order": 4
  },
  {
    "id": "pp_prefs",
    "label_en": "Preferences/Consent Data",
    "label_zh": "偏好/同意数据",
    "type": "data",
    "parent": "pp_kernel",
    "level": 2,
    "order": 5
  },
  {
    "id": "pp_relations",
    "label_en": "Relationships with Other Customers",
    "label_zh": "与其他客户的关系",
    "type": "data",
    "parent": "pp_kernel",
    "level": 2,
    "order": 6
  }
]
```

## 图例

```json
[
  {
    "symbol": "淡黄色底板",
    "meaning_zh": "自然人内核数据的整体范围",
    "explicit": false
  },
  {
    "symbol": "底板内的浅色框 + 顶部横线",
    "meaning_zh": "一个数据分类（细项见表 5-1）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "淡黄色大底板，顶部居中标题；内部 2 行 × 3 列六个等大分类框（上排：内部标识键、外部标识键、个人标识数据；下排：联系方式数据、偏好/同意数据、与其他客户的关系）。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig5-2",
    "relation": "complements",
    "note_zh": "图 5-1 是自然人客户的内核数据分类，图 5-2 是组织/法人客户的内核数据分类；两者共同构成第 5.1 节的内核数据范围。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中只给分类名，未给字段；字段级内容依据表 5-1，未在图中出现。",
    "“与其他客户的关系”是否包含组织客户之间的关系，图中未限定；正文表 5-1 举例为父、母、子女、员工等人际关系。"
  ],
  "analyzed_from": [
    "英文 PDF 第 38 页原图截图",
    "英文 PDF 第 38–39 页表 5-1",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 444–474 行",
    "figs/zh/g21be_fig5-1_zh.png 中文化图"
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
