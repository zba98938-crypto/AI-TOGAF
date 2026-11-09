# G233/fig4-3 · 平衡计分卡

> 当前图示解析：[Markdown](../../architecture/diagrams/G233/fig4-3.md) · [JSON](../../architecture/diagrams/G233/fig4-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G233e.pdf`；SHA-256：`d5c62f9edb2465d10e59f0a1c9c23fb5d8a0b14e506cf7739a09886fbee07754`。

## 原图 · PDF 第 26 页

![英文原图](../assets/G233/fig4-3-p0026.png)

PDF 坐标：`[61.1, 36.0, 550.9, 228.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
in,
nz
-4
ie
a
oe
te
4
oe
SET a
=
a
a
oe
+
“Inte
perme"
Jjo-------- ts
Financial
ae
Jo--------
Ges
Gs-
_
```

## 概要（历史解释；局部修正见上）

把四个平衡计分卡维度各自的目标与可度量成果配对，用“成果实现目标”的虚线箭头连起来。

## 目的（历史解释；局部修正见上）

第 4.3.3 节说明平衡计分卡是“目标与可度量目的的来源”。作者把目标对齐到四个 BSC 维度，并把由某个目标实现的目的（度量/成果）链接到目标上，为后续能力规划提供可追踪的目标—成果链，也说明哪些能力实例的改进值得投入。

## 阅读顺序（历史解释；局部修正见上）

按四个象限读：左上客户、右上学习与成长、左下内部流程、右下财务。每个象限左侧是目标（Goals，同心圆靶心图标），右侧是带斜箭头的成果/度量（Outcomes，靶心带箭头图标）；虚线箭头一律从右侧度量指向左侧目标，表示“达到该度量即实现该目标”。

## 关键含义（历史解释；局部修正见上）

- 四个维度各有一对“目标—度量”：客户（提升客户留存 ← 重复购买客户增加 10%）、学习与成长（提升员工满意度 ← 员工流失率降低 15%）、内部流程（招聘合格新员工 ← 招聘时间缩短 50%）、财务（销售额增长 ← 使用优惠券的客户增加 10%）。
- 箭头一律从右侧的度量/成果指向左侧的目标，画法为虚线＋空心三角，语义是“实现/达成”，不是因果驱动；读图时不要反向理解为目标产生度量。
- 目标（Goal）与成果/度量（Outcome）是两种元素：目标用同心圆靶心图标，成果用靶心带斜箭头图标，与图 3-1 的 Goal/Outcome 记法一致。
- 四个维度覆盖财务结果、客户结果、内部流程能力与员工能力，构成一组互相支撑的目标体系；能力规划要回答的正是“哪些能力实例的改进能推动这些度量”。
- “招聘时间缩短 50%”与“招聘合格新员工”把人力资源议题放进内部流程维度，说明后台职能也会进入战略目标链。
- 平衡计分卡在能力规划中的角色是提供目标与可度量的目的，而不是直接给出能力清单；能力规划要把这些目标/度量继续映射到能力实例与价值流阶段。
- 四个维度之间没有画任何连线，图中不表达 BSC 经典的“学习→流程→客户→财务”因果链，不能凭版式推断因果。

## 层级（历史解释；局部修正见上）

两层：4 个 BSC 维度（虚线容器）→ 每个维度下的一个目标与一个度量。目标与度量之间是“实现”关系，不是上下级；维度之间是并列视角，不是层级。

## 线条含义（历史解释；局部修正见上）

四条虚线均带空心三角箭头，方向由右（度量/成果）指向左（目标），表示该可度量成果实现该目标（ArchiMate realization 的画法）；没有其他连线，维度之间不画关系。

## 易误读点（历史解释；局部修正见上）

- 不要把箭头读成“目标驱动度量”的因果方向；箭头指向目标，含义是“度量达成目标”。
- 不要把四个维度当成四个组织部门；它们是 BSC 的视角，同一组织同时受四个维度约束。
- 不要把“10% more customers have repeat purchases”与中文稿第 7.1 节（L651）的“使用优惠券的人数增加 1%”混为一谈：本图财务维度的度量是“使用优惠券的客户增加 10%”，正文另处的 1% 与图不一致。
- 中文稿 PNG 在“员工流失率降低 15%”处多了一块灰色遮挡，不要把它当作图中的高亮/删除语义。
- 不要把四个“目标”当成四个“度量”：左侧是意图，右侧才是可判定、可测量的成果。

## 元素

```json
[
  {
    "id": "dim_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "group",
    "parent": null,
    "order": 1,
    "position": "左上象限"
  },
  {
    "id": "dim_learning",
    "label_en": "Learning and Growth",
    "label_zh": "学习与成长",
    "type": "group",
    "parent": null,
    "order": 2,
    "position": "右上象限"
  },
  {
    "id": "dim_process",
    "label_en": "Internal Processes",
    "label_zh": "内部流程",
    "type": "group",
    "parent": null,
    "order": 3,
    "position": "左下象限"
  },
  {
    "id": "dim_financial",
    "label_en": "Financial",
    "label_zh": "财务",
    "type": "group",
    "parent": null,
    "order": 4,
    "position": "右下象限"
  },
  {
    "id": "goal_retention",
    "label_en": "Improved Customer Retention",
    "label_zh": "提升客户留存",
    "type": "goal",
    "parent": "dim_customer",
    "order": 1,
    "position": "象限左侧"
  },
  {
    "id": "metric_repeat",
    "label_en": "10% more customers have repeat purchases",
    "label_zh": "重复购买客户增加 10%",
    "type": "metric",
    "parent": "dim_customer",
    "order": 2,
    "position": "象限右侧"
  },
  {
    "id": "goal_satisfaction",
    "label_en": "Improve Employee Satisfaction",
    "label_zh": "提升员工满意度",
    "type": "goal",
    "parent": "dim_learning",
    "order": 1,
    "position": "象限左侧"
  },
  {
    "id": "metric_turnover",
    "label_en": "Reduce Employee Turnover by 15%",
    "label_zh": "员工流失率降低 15%",
    "type": "metric",
    "parent": "dim_learning",
    "order": 2,
    "position": "象限右侧"
  },
  {
    "id": "goal_hire",
    "label_en": "Hire Qualified New Employee",
    "label_zh": "招聘合格新员工",
    "type": "goal",
    "parent": "dim_process",
    "order": 1,
    "position": "象限左侧"
  },
  {
    "id": "metric_time_to_hire",
    "label_en": "50% reduction in time to hire",
    "label_zh": "招聘时间缩短 50%",
    "type": "metric",
    "parent": "dim_process",
    "order": 2,
    "position": "象限右侧"
  },
  {
    "id": "goal_sales",
    "label_en": "Increased Sales",
    "label_zh": "销售额增长",
    "type": "goal",
    "parent": "dim_financial",
    "order": 1,
    "position": "象限左侧"
  },
  {
    "id": "metric_coupons",
    "label_en": "10% increase in customers using coupons",
    "label_zh": "使用优惠券的客户增加 10%",
    "type": "metric",
    "parent": "dim_financial",
    "order": 2,
    "position": "象限右侧"
  }
]
```

## 关系

```json
[
  {
    "from": "metric_repeat",
    "to": "goal_retention",
    "type": "realization",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "重复购买客户增加 10% 实现“提升客户留存”；箭头指向目标。"
  },
  {
    "from": "metric_turnover",
    "to": "goal_satisfaction",
    "type": "realization",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "员工流失率降低 15% 实现“提升员工满意度”；箭头指向目标。"
  },
  {
    "from": "metric_time_to_hire",
    "to": "goal_hire",
    "type": "realization",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "招聘时间缩短 50% 实现“招聘合格新员工”；箭头指向目标。"
  },
  {
    "from": "metric_coupons",
    "to": "goal_sales",
    "type": "realization",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "使用优惠券的客户增加 10% 实现“销售额增长”；箭头指向目标。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_bsc",
    "title_zh": "平衡计分卡四维度：目标与度量",
    "columns": [
      "维度",
      "目标（Goal）",
      "目的/度量（Outcome）"
    ],
    "rows": [
      [
        "Customer 客户",
        "Improved Customer Retention 提升客户留存",
        "10% more customers have repeat purchases 重复购买客户增加 10%"
      ],
      [
        "Learning and Growth 学习与成长",
        "Improve Employee Satisfaction 提升员工满意度",
        "Reduce Employee Turnover by 15% 员工流失率降低 15%"
      ],
      [
        "Internal Processes 内部流程",
        "Hire Qualified New Employee 招聘合格新员工",
        "50% reduction in time to hire 招聘时间缩短 50%"
      ],
      [
        "Financial 财务",
        "Increased Sales 销售额增长",
        "10% increase in customers using coupons 使用优惠券的客户增加 10%"
      ]
    ],
    "notes_zh": "每行的虚线箭头均由右列（度量）指向左列（目标）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "虚线矩形框 + 左上角标题签",
    "meaning_zh": "平衡计分卡维度分区",
    "explicit": false
  },
  {
    "symbol": "同心圆靶心图标",
    "meaning_zh": "目标（Goal）",
    "explicit": false
  },
  {
    "symbol": "靶心带斜箭头图标",
    "meaning_zh": "成果/度量（Outcome）",
    "explicit": false
  },
  {
    "symbol": "虚线 + 空心三角箭头（右→左）",
    "meaning_zh": "实现/达成：右侧的可度量成果实现左侧目标",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "2×2 四象限：左上 Customer、右上 Learning and Growth、左下 Internal Processes、右下 Financial；每格一个虚线维度框，框内左侧目标、右侧度量，虚线箭头由右向左。"
}
```

## 相关图

```json
[
  {
    "target": "G233/fig7-1",
    "relation": "related",
    "note_zh": "图 7-1 对能力实例做红黄绿评估时，正文引用的正是本计分卡的“使用优惠券的客户增加 10%”这一成果（中文稿 L651 写作 1%，与图不符）"
  },
  {
    "target": "G233/figC-1",
    "relation": "related",
    "note_zh": "本图的“招聘合格新员工/招聘时间缩短 50%”与附录 C 招聘员工价值流的主题相关；本图本身不画该价值流，二者是主题关联而非图中的直接引用"
  },
  {
    "target": "G233/fig3-1",
    "relation": "related",
    "note_zh": "图中的 Goal/Outcome 图标与图 3-1 的 ArchiMate Goal/Outcome 元素一致，可视为其目标—成果关系的实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四个维度的排列顺序（客户、学习与成长在上，内部流程、财务在下）不是经典 BSC 的因果链顺序，图上也没有维度间连线，无法判断作者是否想表达因果。",
    "中文稿第 7.1 节（L651）把“使用优惠券的人数增加”写作 1%，本图为 10%；以图为准记录，差异写入 misreadings。",
    "中文 PNG 的灰色块是本地化渲染瑕疵，原图无此元素；其位置与“Reduce Employee Turnover by 15%”框重合。"
  ],
  "analyzed_from": [
    "英文 PDF 第 26 页图 4-3 截图（figctx 裁剪）与 2×2 放大分块",
    "英文 PDF 第 25–26 页正文",
    "中文稿 G233e_业务能力规划.md 第 300–326 行（含 12 条图内标签对照）",
    "figs/g233e_fig4-3_en.png 与 figs/zh/g233e_fig4-3_zh.png"
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
