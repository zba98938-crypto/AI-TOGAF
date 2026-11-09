# G21H/fig6-1 · 按 ADM 阶段的 TOGAF 内容框架

> 当前图示解析：[Markdown](../../architecture/diagrams/G21H/fig6-1.md) · [JSON](../../architecture/diagrams/G21H/fig6-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21He.pdf`；SHA-256：`40881f73b66ae8cfabc279aba8fe3767182ac3e865823054d0aca58f6292a470`。

## 原图 · PDF 第 43 页

![英文原图](../assets/G21H/fig6-1-p0043.png)

PDF 坐标：`[61.1, 352.8, 550.9, 644.2]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business Architecture
Information Systems Architecture
Strategy
Technology
Data
Architecture
Application
Operational
```

## 概要（历史解释；局部修正见上）

按 ADM 阶段/内容类别把 TOGAF 内容框架排成三大块，右侧纵贯架构变更管理。

## 目的（历史解释；局部修正见上）

第 6.2 节要说明 DBRM 的 TOGAF ADM 生命周期要素如何与 TOGAF 内容框架对接。这张图把内容框架按 ADM 阶段归并成四个视觉块（原则/愿景/需求、架构定义、架构实现，加上纵贯的架构变更管理），让读者一眼看出每个阶段产出哪类内容，为表 6-1 的 DBRM 要素—ADM 阶段—内容框架映射提供总图。

## 阅读顺序（历史解释；局部修正见上）

自上而下读三个大色块：顶部橙色“架构原则、愿景与需求”里，Preliminary 与 Architecture Requirements 并排，Architecture Vision 通栏在下；中部灰色“架构定义”里，先是一条 Motivation 横带，下面并排三个架构列——Business Architecture（内含 Strategy、Operational 上下两块）、Information Systems Architecture（内含 Data、Application 左右两块）、Technology Architecture；底部暗红“架构实现”里，Opportunities, Solutions & Migration Planning 与 Implementation Governance 左右并排。最后看最右侧的浅黄竖带“架构变更管理”，它从顶部一直贯到底部，不属于任何一个大色块。

## 关键含义（历史解释；局部修正见上）

- 四个内容块：Architecture Principles, Vision and Requirements（橙）、Architecture Definition（灰）、Architecture Realization（暗红），加上右侧纵贯全图的 Architecture Change Management（浅黄竖带）。
- 顶部块内部：Preliminary 与 Architecture Requirements 左右并排，Architecture Vision 通栏放在它们下面；三者都嵌在橙色大块内。
- 架构定义块内部：Motivation 是一条通栏横带，位于三个架构列之上；三个架构列从左到右为 Business Architecture、Information Systems Architecture、Technology Architecture。
- Business Architecture 内部再分上下两块：Strategy 在上、Operational 在下；Information Systems Architecture 内部再分左右两块：Data 在左、Application 在右；Technology Architecture 不再细分。
- 架构实现块内部左右并排：Opportunities, Solutions & Migration Planning 在左，Implementation Governance 在右。
- 架构变更管理画成纵贯全高的右侧竖带，而不是底部的一个块：表示变更管理横切所有阶段，不是 ADM 走完之后的最后一步。
- 图内没有任何箭头或连线，全部关系由嵌套（大块包小块）与相邻（并排/上下）表达；层级本身就是信息。
- 与 ADM 的对应：Preliminary→预备；Architecture Vision→阶段 A；Business Architecture/Motivation→阶段 B；Information Systems Architecture→阶段 C；Technology Architecture→阶段 D；Architecture Realization（机会/解决方案与迁移规划）→阶段 E/F；Implementation Governance→阶段 G；Architecture Change Management→阶段 H；Architecture Requirements 贯穿需求管理。

## 层级（历史解释；局部修正见上）

两到三层。第 1 层是四个内容块（原则/愿景/需求、架构定义、架构实现、架构变更管理）；第 2 层是各块内的内容区（Preliminary、Architecture Requirements、Architecture Vision；Motivation、三个架构域；机会/解决方案与迁移规划、实施治理）；第 3 层只出现在 Business Architecture（Strategy、Operational）与 Information Systems Architecture（Data、Application）内部。架构变更管理没有子块，是与前三个内容块并列的竖带。

## 线条含义（历史解释；局部修正见上）

图中没有任何连线或箭头，因此没有方向语义。关系只有两种：①包含——大色块包住内部横条/竖块（如橙色块包含 Preliminary、Architecture Requirements、Architecture Vision）；②相邻——同一层内左右并排或上下堆叠（如 Data 与 Application 并排，Strategy 与 Operational 上下）。右侧“架构变更管理”以一条细竖线与主区隔开，是独立的竖带，不是主区的子块。

## 易误读点（历史解释；局部修正见上）

- 不要把四个块读成严格的 ADM 阶段顺序：它们是内容类别；Preliminary 与 Architecture Requirements 是并排的，Architecture Vision 在它们下方，而不是“先预备、再需求、再愿景”的一条竖线。
- “Motivation”是架构定义内的一条横带，不是与业务架构、信息系统架构、技术架构并列的第四个架构域。
- Business Architecture 里的“Strategy/Operational”不是两个 ADM 阶段，而是业务架构内部的两个内容块，对应 DBRM 的战略域/运营域；不要把它们读成阶段 B 之后还有两个阶段。
- 右侧“架构变更管理”不是 ADM 的最后一步底部块，而是纵贯全图、适用于所有阶段的横切内容；它在视觉上覆盖三层，位置本身就说明这一点。
- 图中没有箭头，不要自行补出阶段之间的流向或反馈；阶段顺序与迭代关系见正文 6.2 节与表 6-1。
- 中文化 PNG 右侧“架构变更管理”被缩成极小横排，容易漏读成装饰条；应以英文原图的竖排大字为准。

## 元素

```json
[
  {
    "id": "aprv",
    "label_en": "Architecture Principles, Vision and Requirements",
    "label_zh": "架构原则、愿景与需求",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "顶部橙色大块"
  },
  {
    "id": "preliminary",
    "label_en": "Preliminary",
    "label_zh": "预备阶段",
    "type": "phase",
    "parent": "aprv",
    "level": 2,
    "order": 1,
    "position": "橙色块内左上"
  },
  {
    "id": "arch_requirements",
    "label_en": "Architecture Requirements",
    "label_zh": "架构需求",
    "type": "artifact",
    "parent": "aprv",
    "level": 2,
    "order": 2,
    "position": "橙色块内右上，与预备阶段并排"
  },
  {
    "id": "arch_vision",
    "label_en": "Architecture Vision",
    "label_zh": "架构愿景",
    "type": "artifact",
    "parent": "aprv",
    "level": 2,
    "order": 3,
    "position": "橙色块内通栏横条，位于前两者下方"
  },
  {
    "id": "arch_definition",
    "label_en": "Architecture Definition",
    "label_zh": "架构定义",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "中部灰色大块"
  },
  {
    "id": "motivation",
    "label_en": "Motivation",
    "label_zh": "动机",
    "type": "artifact",
    "parent": "arch_definition",
    "level": 2,
    "order": 1,
    "position": "架构定义块内顶部通栏灰条"
  },
  {
    "id": "business_architecture",
    "label_en": "Business Architecture",
    "label_zh": "业务架构",
    "type": "architecture",
    "parent": "arch_definition",
    "level": 2,
    "order": 2,
    "position": "架构定义块内左侧深蓝列"
  },
  {
    "id": "strategy",
    "label_en": "Strategy",
    "label_zh": "战略",
    "type": "artifact",
    "parent": "business_architecture",
    "level": 3,
    "order": 1,
    "position": "业务架构内上方蓝块"
  },
  {
    "id": "operational",
    "label_en": "Operational",
    "label_zh": "运营",
    "type": "artifact",
    "parent": "business_architecture",
    "level": 3,
    "order": 2,
    "position": "业务架构内下方蓝块"
  },
  {
    "id": "isa",
    "label_en": "Information Systems Architecture",
    "label_zh": "信息系统架构",
    "type": "architecture",
    "parent": "arch_definition",
    "level": 2,
    "order": 3,
    "position": "架构定义块内中间深绿列"
  },
  {
    "id": "data",
    "label_en": "Data",
    "label_zh": "数据",
    "type": "artifact",
    "parent": "isa",
    "level": 3,
    "order": 1,
    "position": "信息系统架构内左侧绿块"
  },
  {
    "id": "application",
    "label_en": "Application",
    "label_zh": "应用",
    "type": "artifact",
    "parent": "isa",
    "level": 3,
    "order": 2,
    "position": "信息系统架构内右侧绿块"
  },
  {
    "id": "tech_arch",
    "label_en": "Technology Architecture",
    "label_zh": "技术架构",
    "type": "architecture",
    "parent": "arch_definition",
    "level": 2,
    "order": 4,
    "position": "架构定义块内右侧深灰列，不再细分"
  },
  {
    "id": "arch_realization",
    "label_en": "Architecture Realization",
    "label_zh": "架构实现",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "底部暗红大块"
  },
  {
    "id": "opportunities",
    "label_en": "Opportunities, Solutions & Migration Planning",
    "label_zh": "机会、解决方案与迁移规划",
    "type": "phase",
    "parent": "arch_realization",
    "level": 2,
    "order": 1,
    "position": "架构实现块内左侧红块"
  },
  {
    "id": "implementation_gov",
    "label_en": "Implementation Governance",
    "label_zh": "实施治理",
    "type": "phase",
    "parent": "arch_realization",
    "level": 2,
    "order": 2,
    "position": "架构实现块内右侧红块，较宽"
  },
  {
    "id": "change_mgmt",
    "label_en": "Architecture Change Management",
    "label_zh": "架构变更管理",
    "type": "phase",
    "parent": null,
    "level": 1,
    "position": "最右侧浅黄竖带，从上贯到下",
    "description_zh": "原图为竖排大字；中文版被缩成极小横排，几乎不可读。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "橙色大块",
    "meaning_zh": "内容类别：架构原则、愿景与需求",
    "explicit": false
  },
  {
    "symbol": "灰色大块",
    "meaning_zh": "内容类别：架构定义",
    "explicit": false
  },
  {
    "symbol": "暗红大块",
    "meaning_zh": "内容类别：架构实现",
    "explicit": false
  },
  {
    "symbol": "右侧浅黄竖带 + 竖排文字",
    "meaning_zh": "架构变更管理，横切所有阶段",
    "explicit": false
  },
  {
    "symbol": "大块内的小色块/横条",
    "meaning_zh": "该内容类别下的内容区或架构域；嵌套表示包含",
    "explicit": false
  },
  {
    "symbol": "并排/上下相邻",
    "meaning_zh": "同一层级内的并列内容，无先后顺序",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "浅黄外框内自上而下三个大色块：橙色（原则/愿景/需求）、灰色（架构定义）、暗红（架构实现）；最右侧一条浅黄竖带从上贯到下，竖排“Architecture Change Management”。架构定义块内三个架构列并排，业务架构与信息系统架构内部再分小块。"
}
```

## 相关图

```json
[
  {
    "target": "G21H/fig6-2",
    "relation": "complements",
    "note_zh": "同属第 6 章 TOGAF 标准采用：图 6-1 按 ADM 阶段组织内容框架，图 6-2 给出架构景观的三层分类模型；两图分别回答“阶段产出什么”与“架构景观如何分层”。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "右侧“架构变更管理”竖带在主图之外，是否算作第四个内容块还是横切覆盖层，图中没有边框说明；本分析按横切层处理（与三个内容块并列但不属于任何一块）。",
    "原图没有把 Preliminary、Architecture Requirements、Architecture Vision 与具体阶段字母连起来，ADM 阶段对应关系（A/B/C/D/E-F/G/H、需求管理）是依据 6.2 节正文与表 6-1 补出的，不是图内文字。",
    "中文版“架构变更管理”缩得极小，若只读中文图可能完全漏掉这一层。"
  ],
  "analyzed_from": [
    "英文 PDF 第 43 页 figure 截图（220 dpi）",
    "英文 PDF 第 43 页正文",
    "中文稿 G21He_TOGAF数字业务参考模型.md 第 624–698 行（含图内标签对照表与表 6-1）",
    "figs/g21he_fig6-1_en.png 与 figs/zh/g21he_fig6-1_zh.png 目视比较"
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
