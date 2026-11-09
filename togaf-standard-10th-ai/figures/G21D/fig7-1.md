# G21D/fig7-1 · 拟议的司法、治安与内政部门 L1–L3 要素的结构与内容概览

> 当前图示解析：[Markdown](../../architecture/diagrams/G21D/fig7-1.md) · [JSON](../../architecture/diagrams/G21D/fig7-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21De.pdf`；SHA-256：`220ead5fef846c52417b9b7a915ff4a64f327680b384c369840926b85958786a`。

## 原图 · PDF 第 43 页

![英文原图](../assets/G21D/fig7-1-p0043.png)

PDF 坐标：`[125.6, 132.3, 486.4, 456.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
-
~
{
/
Protection and Law
\
{
Criminal Justice and
\
Enforcement
Offender Management
Customs
Youth Offending
)
Immigration
Criminal Justice
Emergency Planning
Prison Monitoring
Fire Service
Police Authority
Health and Safety
Law Commission
Police Service
Criminal Compensation
.
Police Complaints
7
```

## 概要（历史解释；局部修正见上）

政府参考模型中“司法、治安与内政”部门的 L1–L3 分解：1 个部门、2 个功能、13 项服务。

## 目的（历史解释；局部修正见上）

第 7 章开篇用这张图概览“司法、治安与内政”部门（L1）下的功能（L2）与服务（L3），随后的表 7-1 逐项给出说明。它是图 1-1 三层结构在本部门的具体展开，与其余 10 个部门图采用同一模板，附录 A 第 50 页把它与图 8-1 汇总在同一页。

## 阅读顺序（历史解释；局部修正见上）

最外层浅蓝色大框是 L1 部门，顶部白色粗体字是部门名称。框内两个白色圆角框是 L2 功能，左为保护与执法，右为刑事司法与罪犯管理。每个功能框里自上而下排列的胶囊形小框是 L3 服务。图中没有连线或箭头，上下级关系完全由框的嵌套表达，同一功能内的服务是并列的。

## 关键含义（历史解释；局部修正见上）

- 本部门只有 2 个 L2 功能：保护与执法（6 项服务）、刑事司法与罪犯管理（7 项），共 13 项 L3 服务。
- 按表 7-1 的功能说明：保护与执法指保护与保障公众并确保法律得到强制遵守的服务；刑事司法与罪犯管理指对已犯罪或违法者实施司法。
- 保护与执法覆盖边境（海关、移民）、应急与安全（应急规划、消防服务、健康与安全）和一线警务（警务），对应第 7 章开篇所说的保护与执法服务。
- 刑事司法与罪犯管理覆盖司法实施及其监督与救济：青少年犯罪（监督青少年罪犯并防止再犯）、刑事司法（对已犯罪者实施司法，含提供公诉律师）、监狱监督、警察当局（协调执法服务）、法律委员会（审查现行法律并提出改革建议）、刑事赔偿（向犯罪受害者提供补偿）、警察投诉（评估对警察的不满以维持公众信心）。
- 警务相关服务分在两个功能里：一线的“警务（Police Service）”在保护与执法下，负责协调执法的“警察当局”和处理投诉的“警察投诉”在刑事司法与罪犯管理下。
- 图中没有单独的“法院”或“审判”服务；按表 7-1，对已犯罪者实施司法（包括提供公诉律师）归在“刑事司法”这一项。
- 与其他部门的分工：海关负责检查非法或应税货物与清关，进口关税的征收在财政部门（图 8-1），进口单证的受理在一般政府与地方服务部门（图 4-1）；应急规划与消防服务在本部门，院前急救在健康与社区福祉部门（图 6-1）。

## 层级（历史解释；局部修正见上）

三层严格树形：L1 部门“司法、治安与内政”（最外层框）→ 2 个 L2 功能（白色圆角框）→ 13 个 L3 服务（胶囊框）。每项服务只属于一个功能，对应图 1-1 中“部门—功能—服务”的组成关系。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头。服务框位于功能框内，表示该服务属于该功能；功能框位于部门框内，表示该功能属于本部门（图 1-1 用菱形组合线表示同样的组成关系）。元素清单用 parent/level 记录这种嵌套，因此关系清单为空。

## 易误读点（历史解释；局部修正见上）

- “Criminal Compensation（刑事赔偿）”按表 7-1 是向犯罪受害者提供补偿的计划，不是中文法律语境中国家对错误追诉的“刑事赔偿”。
- “Youth Offending（青少年犯罪）”是监督青少年罪犯并提供社区服务以防再犯的服务，不是犯罪统计。
- “Police Authority（警察当局）”按表 7-1 指协调执法服务的活动，并不泛指警察机关；一线警务是保护与执法下的“警务（Police Service）”。
- 同一功能内服务的上下次序不表示优先级或流程先后。
- 中文稿引用的中文化 PNG 字号混乱（两个功能标题字号相差很大），不能用字号判断层级，应以框的嵌套为准。
- 图框下方的浅灰色线条是 PDF 评估版水印的残影，不属于图的内容。

## 元素

```json
[
  {
    "id": "l1_judiciary_justice_home_affairs",
    "label_en": "Judiciary, Justice, and Home Affairs",
    "label_zh": "司法、治安与内政",
    "type": "other",
    "notation_type": "GRM L1 部门（Sector）",
    "parent": null,
    "level": 1,
    "position": "最外层浅蓝色框，标题在顶部",
    "description_zh": "GRM 第 1 层“部门”，即政府的一个业务领域；词表没有对应类型，故用 other。"
  },
  {
    "id": "l2_protection_law_enforcement",
    "label_en": "Protection and Law Enforcement",
    "label_zh": "保护与执法",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_judiciary_justice_home_affairs",
    "level": 2,
    "order": 1,
    "position": "左",
    "description_zh": "保护与保障公众并确保法律得到强制遵守的服务（表 7-1）。"
  },
  {
    "id": "l2_criminal_justice_offender_mgmt",
    "label_en": "Criminal Justice and Offender Management",
    "label_zh": "刑事司法与罪犯管理",
    "type": "function",
    "notation_type": "GRM L2 功能（Function）",
    "parent": "l1_judiciary_justice_home_affairs",
    "level": 2,
    "order": 2,
    "position": "右",
    "description_zh": "对已犯罪或违法者实施司法（表 7-1）。"
  },
  {
    "id": "l3_customs",
    "label_en": "Customs",
    "label_zh": "海关",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_protection_law_enforcement",
    "level": 3,
    "order": 1,
    "description_zh": "检查非法或应税货物，就配额与海关法规提供建议，含检查、清关、筛查与搜查。"
  },
  {
    "id": "l3_immigration",
    "label_en": "Immigration",
    "label_zh": "移民",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_protection_law_enforcement",
    "level": 3,
    "order": 2,
    "description_zh": "确认入境旅客获准入境并办理抵达通关。"
  },
  {
    "id": "l3_emergency_planning",
    "label_en": "Emergency Planning",
    "label_zh": "应急规划",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_protection_law_enforcement",
    "level": 3,
    "order": 3,
    "description_zh": "不可预见情形下的紧急援助，含应急资金、后勤支持与政府和社区服务的协调。"
  },
  {
    "id": "l3_fire_service",
    "label_en": "Fire Service",
    "label_zh": "消防服务",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_protection_law_enforcement",
    "level": 3,
    "order": 4
  },
  {
    "id": "l3_health_and_safety",
    "label_en": "Health and Safety",
    "label_zh": "健康与安全",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_protection_law_enforcement",
    "level": 3,
    "order": 5,
    "description_zh": "设计、开发与实施健康与安全计划。"
  },
  {
    "id": "l3_police_service",
    "label_en": "Police Service",
    "label_zh": "警务",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_protection_law_enforcement",
    "level": 3,
    "order": 6,
    "description_zh": "就规则与法规提供建议、改善公共安全、减少暴力与非法物质使用。"
  },
  {
    "id": "l3_youth_offending",
    "label_en": "Youth Offending",
    "label_zh": "青少年犯罪",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 1,
    "description_zh": "监督青少年罪犯，并提供社区服务以防再犯。"
  },
  {
    "id": "l3_criminal_justice",
    "label_en": "Criminal Justice",
    "label_zh": "刑事司法",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 2,
    "description_zh": "对已犯罪个人实施司法，包括提供公诉律师。"
  },
  {
    "id": "l3_prison_monitoring",
    "label_en": "Prison Monitoring",
    "label_zh": "监狱监督",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 3,
    "description_zh": "监督羁押刑事罪犯的设施。"
  },
  {
    "id": "l3_police_authority",
    "label_en": "Police Authority",
    "label_zh": "警察当局",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 4,
    "description_zh": "协调执法服务。"
  },
  {
    "id": "l3_law_commission",
    "label_en": "Law Commission",
    "label_zh": "法律委员会",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 5,
    "description_zh": "审查现行法律，必要时提出改革建议。"
  },
  {
    "id": "l3_criminal_compensation",
    "label_en": "Criminal Compensation",
    "label_zh": "刑事赔偿（犯罪被害人补偿）",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 6,
    "description_zh": "就犯罪相关费用向犯罪受害者提供补偿；中文稿译作“刑事赔偿”。"
  },
  {
    "id": "l3_police_complaints",
    "label_en": "Police Complaints",
    "label_zh": "警察投诉",
    "type": "service",
    "notation_type": "GRM L3 服务（Service）",
    "parent": "l2_criminal_justice_offender_mgmt",
    "level": 3,
    "order": 7,
    "description_zh": "评估对警察部队或个人的不满，以维持公众信心。"
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
  "description_zh": "最外层浅蓝色圆角框较窄（顶部为部门标题，版权署名在左下角），框内两个功能框左右并排：保护与执法（6 项）、刑事司法与罪犯管理（7 项）；各框内服务自上而下单列排列。"
}
```

## 相关图

```json
[
  {
    "target": "G21D/fig1-1",
    "relation": "detail_of",
    "note_zh": "图 1-1 的三层结构（L1 部门—L2 功能—L3 服务）在“司法、治安与内政”部门的展开"
  },
  {
    "target": "G21D/fig8-1",
    "relation": "complements",
    "note_zh": "同一模板的相邻部门概览（财政）；海关检查与清关在本图，进口关税征收在图 8-1"
  },
  {
    "target": "G21D/appA-p50",
    "relation": "related",
    "note_zh": "附录 A 第 50 页（PDF 第 70 页）原样收录本图，与图 8-1 同页"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [],
  "analyzed_from": [
    "英文 PDF 第 43 页原图截图",
    "英文 PDF 第 43–44 页正文（第 7 章开篇、表 7-1）及第 21–24 页（1.3–1.4 节）",
    "英文 PDF 第 70 页附录 A 图示（同内容面板，用于复核标签）",
    "中文稿 G21De_政府参考模型.md 第 648–698 行",
    "figs/zh/g21de_fig7-1_zh.png（逐项对照）"
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
