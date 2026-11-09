# G242/fig3-2 · 数字可持续性的关键文化轴

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-2.md) · [JSON](../../architecture/diagrams/G242/fig3-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 35 页

![英文原图](../assets/G242/fig3-2-p0035.png)

PDF 坐标：`[112.7, 36.0, 499.3, 265.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Organization,
Skills and Education
Management, and
Work Culture
Programs
Digital
Sobriety
Communication
Frugal Innovation
```

## 概要（历史解释；局部修正见上）

以数字节制为中心目标，从组织文化、技能教育、沟通与节俭创新四个维度推进文化转型。

## 目的（历史解释；局部修正见上）

把“发展可持续数字文化”这一抽象功能拆成四个可操作、可评估的维度，并明确四者共同服务于“数字节制”这一目标。它为 3.3.1–3.3.4 各小节提供结构，也提示文化转型不是单一培训活动，而是组织、能力、传播与创新方式的组合。

## 阅读顺序（历史解释；局部修正见上）

先看中心的浅紫色框“Digital Sobriety（数字节制）”，它是四个象限共同指向的目标。再按顺时针或任意顺序读四个象限：左上组织/管理与工作文化、右上技能与教育计划、右下节俭式创新、左下沟通。四个象限没有坐标轴标签，也没有箭头，位置只表示并列分组，不表示先后或高低。

## 关键含义（历史解释；局部修正见上）

- 四个维度是：组织、管理与工作文化；技能与教育计划；沟通；节俭式创新。
- 中心“数字节制（Digital Sobriety）”不是第五个维度，而是四者共同服务的共同目标。
- 组织/管理与工作文化维度承载管理层承诺、目标设定、集体碳目标与榜样作用（正文 3.3.1）。
- 技能与教育计划对应员工培训，使其理解能源—气候问题并形成节制习惯。
- 沟通负责在组织内外传播转型意义与良好实践；节俭式创新负责以更少资源满足同样需求。
- 四个维度并列，没有优先级或成熟度刻度；图不能用来判断组织当前处于哪个阶段。

## 层级（历史解释；局部修正见上）

无层级。一个中心目标框 + 四个平级象限标签；象限由白色十字线划分，中心框压在十字交点上。

## 线条含义（历史解释；局部修正见上）

图中只有构成 2×2 的白色分隔线，没有箭头，也没有连接线。中心框与四象限的关系由“居于中央、四向包围”隐含表达（关系清单中标为推断）。

## 易误读点（历史解释；局部修正见上）

- 这不是带两个变量的 2×2 矩阵：没有横纵轴名称、没有刻度，四个象限不是“高/低”组合。
- 四个象限没有先后顺序，不能按阅读顺序当作转型四步。
- 中心“数字节制”不是第五个文化轴，而是四轴共同指向的目标。
- 不要把“节俭式创新（Frugal Innovation）”理解为单纯省钱，它指以更少资源实现同等效用。

## 元素

```json
[
  {
    "id": "digital_sobriety",
    "label_en": "Digital Sobriety",
    "label_zh": "数字节制",
    "type": "goal",
    "parent": null,
    "position": "图形中心，压在十字交点上",
    "description_zh": "四个文化维度共同指向的目标。"
  },
  {
    "id": "axis_org",
    "label_en": "Organization, Management, and Work Culture",
    "label_zh": "组织、管理与工作文化",
    "type": "group",
    "parent": null,
    "position": "左上象限",
    "description_zh": "3.3.1 节展开的维度。"
  },
  {
    "id": "axis_skills",
    "label_en": "Skills and Education Programs",
    "label_zh": "技能与教育计划",
    "type": "group",
    "parent": null,
    "position": "右上象限",
    "description_zh": "员工培训与能力建设维度。"
  },
  {
    "id": "axis_communication",
    "label_en": "Communication",
    "label_zh": "沟通",
    "type": "group",
    "parent": null,
    "position": "左下象限",
    "description_zh": "内外沟通与动员维度。"
  },
  {
    "id": "axis_frugal",
    "label_en": "Frugal Innovation",
    "label_zh": "节俭式创新",
    "type": "group",
    "parent": null,
    "position": "右下象限",
    "description_zh": "以更少资源实现同等效用的创新维度。"
  }
]
```

## 关系

```json
[
  {
    "from": "axis_org",
    "to": "digital_sobriety",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "象限围绕中心，表示该维度服务于数字节制目标。"
  },
  {
    "from": "axis_skills",
    "to": "digital_sobriety",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上。"
  },
  {
    "from": "axis_communication",
    "to": "digital_sobriety",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上。"
  },
  {
    "from": "axis_frugal",
    "to": "digital_sobriety",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "同上。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "中心浅紫圆角框",
    "meaning_zh": "四个维度共同指向的目标：数字节制",
    "explicit": false
  },
  {
    "symbol": "白色十字分隔线",
    "meaning_zh": "把文化转型划分为四个并列维度，不代表坐标轴",
    "explicit": false
  },
  {
    "symbol": "深蓝底色 + 青色文字",
    "meaning_zh": "统一的视觉风格，不编码强弱或优先级",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "1 个深蓝色大方块被白色十字分成 2×2 四格；四个标签分别位于左上、右上、左下、右下；中心浅紫色圆角框横跨十字交点，写“Digital Sobriety”。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-1",
    "relation": "detail_of",
    "note_zh": "本图细化图 3-1 中“发展可持续数字文化”这一业务功能"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四个象限没有坐标轴名称，图本身不能说明象限位置是否另有含义；按并列分组理解。",
    "原图未给各维度的具体活动，需结合 3.3.1–3.3.4 正文。"
  ],
  "analyzed_from": [
    "英文 PDF 第 35 页原图截图（1214×742）",
    "英文 PDF 第 34–35 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 469–488 行",
    "figs/zh/g242_fig3-2_zh.png",
    "figs/g242_fig3-2_en.png（缩略图相似度核对）"
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
