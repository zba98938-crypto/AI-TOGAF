# G21I/fig6-1 · 界定企业架构的范围

> 当前图示解析：[Markdown](../../architecture/diagrams/G21I/fig6-1.md) · [JSON](../../architecture/diagrams/G21I/fig6-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21Ie.pdf`；SHA-256：`279f6c06124f49a147a168591965805115b2fc976eea2664e41e491ac5d163bf`。

## 原图 · PDF 第 32 页

![英文原图](../assets/G21I/fig6-1-p0032.png)

PDF 坐标：`[164.2, 36.0, 447.8, 296.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
(© The Open Group
Breadth
Time
Enterprise Strategic Architecture
Segment
‘Segment
Architecture
Architecture
```

## 概要（历史解释；局部修正见上）

企业架构分三个层级：企业战略架构覆盖全局，其下是多个分段架构，再下是更多能力架构，MSA 位于能力架构层。

## 目的（历史解释；局部修正见上）

第 6 章（阶段 A：架构愿景）用本图说明 MSA 在企业架构中的位置：企业架构团队通常已有战略架构，可能指出哪些分段应采用微服务/云原生方法；架构师再开发分段架构；分段架构之下是各个能力架构，MSA 层就在这里。由此界定 MSA 架构工作的范围。

## 阅读顺序（历史解释；局部修正见上）

看左侧的三条坐标轴：“层级”向下表示越来越具体，“时间”向右，“广度”斜向纵深。再自上而下看三层块：顶部一整块黄色板是企业战略架构，横跨全部广度和时间；中间是多个绿色分段架构块；底部是更多、更小的紫色能力架构块。越往下，块越多、越小，每块覆盖的广度和时间越窄。

## 关键含义（历史解释；局部修正见上）

- 企业战略架构只有一块，覆盖企业的全部广度和整个时间跨度；原文称它是企业的概要性正式描述，为运营与变更活动提供组织框架，给出高管层的长期方向。
- 战略架构可能指出哪些分段应采用微服务/云原生方法、要求分段之间使用交互标准，但基本不会规定具体的微服务，也不会规定支撑它们的详细基础设施。
- 分段架构在战略架构之下，数量更多，各自详细、正式地描述企业内的某个领域，在项目群或组合层面用来组织和协调变更活动。
- 能力架构在分段架构之下，数量最多、块最小；原文指出 MSA 层预期位于能力架构中。
- 原文强调 MSA 只涉及整体系统或企业架构中的一层，企业架构通常处在比 MSA 高得多的层级；各职能/项目架构必须与总体企业架构保持一致，并继承其治理与变更管理。
- 块向“时间”方向重复排列，表示不同时期各有一组分段架构和能力架构；越低层的块在时间方向上越短。

## 层级（历史解释；局部修正见上）

三个层级自上而下：企业战略架构（1 块）→ 分段架构（多块）→ 能力架构（更多块）。下层块位于上层块的正下方，表示它们属于上层架构所界定的那部分企业；图中前排可见 2 个分段块、3 个能力块，其后还有成排的块向时间与广度方向延伸。

## 线条含义（历史解释；局部修正见上）

图中的 3 条深蓝色箭头是坐标轴，不是元素之间的关系。层级之间没有连线，上下关系由垂直堆叠表达（关系清单中记为推断）：上层为下层设定框架和约束。

## 易误读点（历史解释；局部修正见上）

- “层级”轴向下表示更具体、范围更窄，不表示更不重要。
- 本图不是甘特图；“时间”轴表示各层架构覆盖的时间跨度，块不对应具体日期。
- MSA 不在战略层或分段层，而是在能力架构层；企业架构通常不会规定单个微服务。
- 后排未标名称的绿色、紫色块与前排同类，分别是更多的分段架构和能力架构，不是别的东西。

## 元素

```json
[
  {
    "id": "axis_breadth",
    "label_en": "Breadth",
    "label_zh": "广度",
    "type": "concept",
    "position": "左上，斜向右上的坐标轴"
  },
  {
    "id": "axis_time",
    "label_en": "Time",
    "label_zh": "时间",
    "type": "time",
    "position": "水平向右的坐标轴"
  },
  {
    "id": "axis_level",
    "label_en": "Level",
    "label_zh": "层级",
    "type": "concept",
    "position": "左侧竖直向下的坐标轴"
  },
  {
    "id": "esa",
    "label_en": "Enterprise Strategic Architecture",
    "label_zh": "企业战略架构",
    "type": "architecture",
    "level": 1,
    "position": "顶部黄色大板"
  },
  {
    "id": "seg_1",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "architecture",
    "level": 2,
    "position": "中层前排左（较宽）",
    "description_zh": "其后还有未标名称的绿色块向时间、广度方向延伸，同为分段架构。"
  },
  {
    "id": "seg_2",
    "label_en": "Segment Architecture",
    "label_zh": "分段架构",
    "type": "architecture",
    "level": 2,
    "position": "中层前排右"
  },
  {
    "id": "cap_1",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "level": 3,
    "position": "底层前排左",
    "description_zh": "其后还有成排未标名称的紫色块，同为能力架构；MSA 层位于这一层。"
  },
  {
    "id": "cap_2",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "level": 3,
    "position": "底层前排中"
  },
  {
    "id": "cap_3",
    "label_en": "Capability Architecture",
    "label_zh": "能力架构",
    "type": "architecture",
    "level": 3,
    "position": "底层前排右"
  }
]
```

## 关系

```json
[
  {
    "from": "esa",
    "to": "seg_1",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "垂直堆叠：战略架构为分段架构提供组织框架与方向"
  },
  {
    "from": "esa",
    "to": "seg_2",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "seg_1",
    "to": "cap_1",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward",
    "description_zh": "能力块位于该分段块正下方"
  },
  {
    "from": "seg_1",
    "to": "cap_2",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  },
  {
    "from": "seg_2",
    "to": "cap_3",
    "type": "governs",
    "explicit": false,
    "line": "implicit",
    "arrow": "forward"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_levels",
    "title_zh": "三个架构层级（据原图与第 6 章正文）",
    "columns": [
      "层级",
      "图中表示",
      "覆盖范围",
      "原文要点（转述）"
    ],
    "rows": [
      [
        "企业战略架构 Enterprise Strategic Architecture",
        "顶部一整块黄色板",
        "企业全部广度、整个时间跨度",
        "企业的概要性正式描述，组织框架，高管层长期方向；可指定哪些分段用微服务/云原生方法，但不规定具体微服务"
      ],
      [
        "分段架构 Segment Architecture",
        "中层多个绿色立方块",
        "企业内某一领域，时间跨度较短",
        "某一领域的详细正式描述，在项目群/组合层面组织和协调变更"
      ],
      [
        "能力架构 Capability Architecture",
        "底层更多更小的紫色立方块",
        "更窄的范围与更短的时间跨度",
        "位于分段架构之下，MSA 层预期位于其中；须与总体企业架构一致，可能受遗留接口/应用约束"
      ]
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "黄色大板",
    "meaning_zh": "企业战略架构",
    "explicit": false
  },
  {
    "symbol": "绿色立方块",
    "meaning_zh": "分段架构",
    "explicit": false
  },
  {
    "symbol": "紫色小立方块",
    "meaning_zh": "能力架构",
    "explicit": false
  },
  {
    "symbol": "深蓝色坐标轴箭头",
    "meaning_zh": "广度、时间、层级三个维度的方向",
    "explicit": false
  },
  {
    "symbol": "块的大小",
    "meaning_zh": "该架构覆盖的广度和时间跨度",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "左上角为坐标原点：“广度”轴斜向右上，“时间”轴水平向右，“层级”轴竖直向下。右侧三层立体块自上而下：黄色大板、绿色分段块、紫色能力块；后两层向右上方（时间、广度方向）成排延伸。"
}
```

## 相关图

```json
[
  {
    "target": "G21I/fig6-2",
    "relation": "overview_of",
    "note_zh": "本图给出三个架构层级；图 6-2 展开 MSA 所在的一个项目级（能力层）架构的内部结构"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "后排未标名称的分段块和能力块数量较多且相互遮挡，未逐个列为元素，只在描述中说明。",
    "能力块与分段块的对应（cap_1、cap_2 在 seg_1 下，cap_3 在 seg_2 下）按前排块的水平位置推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 32 页原图截图（220 dpi）",
    "英文 PDF 第 31–32 页正文",
    "中文稿 G21Ie_微服务架构.md 第 405–438 行（含图内标签对照表 L419–L428）",
    "figs/zh/g21ie_fig6-1_zh.png",
    "figs/g21ie_fig6-1_en.png（自动相似度 0.987）"
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
