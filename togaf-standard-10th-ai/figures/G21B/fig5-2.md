# G21B/fig5-2 · 组织/法人内核数据

> 当前图示解析：[Markdown](../../architecture/diagrams/G21B/fig5-2.md) · [JSON](../../architecture/diagrams/G21B/fig5-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Be.pdf`；SHA-256：`8e64887f7a080d3d882f38078297bd7873a9072b71a12c39b9e77349890f37a2`。

## 原图 · PDF 第 39 页

![英文原图](../assets/G21B/fig5-2-p0039.png)

PDF 坐标：`[48.2, 235.3, 563.8, 438.6]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Customer Data — Organization
Internal Identification
External Identification
Legal Person Description
Keys
Keys
Contact Data
Preferences/Consent
Relationships/Group
Data
Membership
```

## 概要（历史解释；局部修正见上）

组织客户内核数据六类：内部/外部标识键、法人描述、联系方式、偏好/同意、关系/集团成员。

## 目的（历史解释；局部修正见上）

界定 C-MDM 对“组织”（法人实体）客户应管理的核心数据范围，与图 5-1 的自然人范围并列；说明同一套 C-MDM 要同时容纳 B2C 与 B2B 两类客户，且法人数据需要额外的官方注册标识与规模/业务领域描述。

## 阅读顺序（历史解释；局部修正见上）

先确认标题是“Customer Data – Organization”，再与图 5-1 对照读：上排仍是内部标识键、外部标识键，但第三格换成“法人描述”；下排是联系方式、偏好/同意、关系/集团成员。六个框并列，无先后；字段级内容见表 5-2。

## 关键含义（历史解释；局部修正见上）

- 组织客户同样有内部标识键（业务客户编码、唯一技术键）与外部标识键（组织官方编号、数据提供方参考号、国家登记 ID 等）。
- 法人描述包含组织名称、替代名称（经营名称）、成立日期、规模参数（dimensioning data，如官方权重类别）与组织业务领域；中文稿表 5-2 特别标注英文原文仍沿用“First name”“Date of birth”等自然人字段名。
- 联系方式数据包括相关自然人及其联系方式（可链接到 C-MDM 中的另一自然人）、相关地址与相关电子邮箱。
- 偏好/同意数据与自然人相同，记录组织授权/不授权使用某范围数据。
- 关系/集团成员描述组织与其他实体的关系（如母公司、子公司、集团成员），对应自然人图中的“与其他客户的关系”。
- 图 5-2 与图 5-1 结构完全同构，差别只在第三格（法人描述 vs 个人标识数据）与第六格（关系/集团成员 vs 与其他客户的关系）。

## 层级（历史解释；局部修正见上）

两层：第 1 层是“组织客户内核数据”；第 2 层是六个并列分类。分类之间无上下级、无连线。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头；六个分类的并列与同属关系只由 2×3 网格与淡黄底板表达。

## 易误读点（历史解释；局部修正见上）

- 不要把“法人描述”当作一个字段：它是名称、替代名称、成立日期、规模参数、业务领域等一组属性的分类。
- 英文原图表 5-2 中仍出现“First name”“Date of birth”字样，是原文沿用自然人模板的措辞，实际含义是组织名称与成立日期（中文稿已注明）。
- 组织客户的“关系/集团成员”不是人际父子关系，而是法人之间的集团/股权/成员关系。
- 图只给分类，不给字段；设计数据模型须结合表 5-2。

## 元素

```json
[
  {
    "id": "org_kernel",
    "label_en": "Customer Data – Organization",
    "label_zh": "客户数据——组织",
    "type": "data",
    "parent": null,
    "level": 1
  },
  {
    "id": "org_internal_keys",
    "label_en": "Internal Identification Keys",
    "label_zh": "内部标识键",
    "type": "data",
    "parent": "org_kernel",
    "level": 2,
    "order": 1
  },
  {
    "id": "org_external_keys",
    "label_en": "External Identification Keys",
    "label_zh": "外部标识键",
    "type": "data",
    "parent": "org_kernel",
    "level": 2,
    "order": 2
  },
  {
    "id": "org_legal_desc",
    "label_en": "Legal Person Description",
    "label_zh": "法人描述",
    "type": "data",
    "parent": "org_kernel",
    "level": 2,
    "order": 3
  },
  {
    "id": "org_contact",
    "label_en": "Contact Data",
    "label_zh": "联系方式数据",
    "type": "data",
    "parent": "org_kernel",
    "level": 2,
    "order": 4
  },
  {
    "id": "org_prefs",
    "label_en": "Preferences/Consent Data",
    "label_zh": "偏好/同意数据",
    "type": "data",
    "parent": "org_kernel",
    "level": 2,
    "order": 5
  },
  {
    "id": "org_group",
    "label_en": "Relationships/Group Membership",
    "label_zh": "关系/集团成员",
    "type": "data",
    "parent": "org_kernel",
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
    "meaning_zh": "组织/法人内核数据的整体范围",
    "explicit": false
  },
  {
    "symbol": "底板内的浅色框 + 顶部横线",
    "meaning_zh": "一个数据分类（细项见表 5-2）",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "淡黄色大底板，顶部居中标题；内部 2 行 × 3 列六个分类框（上排：内部标识键、外部标识键、法人描述；下排：联系方式数据、偏好/同意数据、关系/集团成员）。"
}
```

## 相关图

```json
[
  {
    "target": "G21B/fig5-1",
    "relation": "complements",
    "note_zh": "图 5-1 与图 5-2 结构同构，分别覆盖自然人客户与组织/法人客户的内核数据。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中只给分类名，字段级内容依据表 5-2；表 5-2 中“First name/Date of birth”沿用了自然人字段名，本分析按中文稿注释理解为组织名称/成立日期。",
    "“关系/集团成员”的具体关系类型（母子公司、集团成员等）图中未列出。"
  ],
  "analyzed_from": [
    "英文 PDF 第 39 页原图截图",
    "英文 PDF 第 39 页正文与表 5-2 开头",
    "中文稿 G21Be_信息架构_客户主数据管理.md 第 483–515 行",
    "figs/zh/g21be_fig5-2_zh.png 中文化图"
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
