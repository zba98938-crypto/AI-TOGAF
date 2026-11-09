# G210/fig3-5 · 使用冲刺的敏捷改进型企业

> 当前图示解析：[Markdown](../../architecture/diagrams/G210/fig3-5.md) · [JSON](../../architecture/diagrams/G210/fig3-5.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G210e.pdf`；SHA-256：`289803b369a49bc7f49c0d587b7f4af87899eebea8d834a6f52cbb2c3a657a58`。

## 原图 · PDF 第 29 页

![英文原图](../assets/G210/fig3-5-p0029.png)

PDF 坐标：`[48.2, 36.0, 563.8, 324.3]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
DORP.
DORP
DORP
DORP.
Sprint 0
Sprint 1
Sprint 2
Sprint ...
Business
Cross-
MVP
Cross-
Cross-
MVP
Vision
Functional
Functional
wvp }
Functional
Teams
\-7
NS
Teams
\ 4
Ne
Teams
\n-7
NS
MVP = Minimum Viable Product.
DORP = Demo, Outcome, Retrospective, Planning, & Releases
```

## 概要（历史解释；局部修正见上）

多个跨职能团队各自具备 EA 能力，按冲刺轮转交付 MVP，冲刺末统一协调。

## 目的（历史解释；局部修正见上）

展示最高成熟度的“跨职能敏捷”：不再有专门的业务开发、企业架构或解决方案团队，而是若干混合的跨职能团队，每个团队都具备三种能力，各自在冲刺中产出解决方案，并在冲刺末协调。它是图 3-2 至 3-4 逐级合并泳道的终点。

## 阅读顺序（历史解释；局部修正见上）

从左往右读时间轴：业务愿景进入冲刺 0 的 DORP；之后从冲刺 1 起，每个冲刺由一组“Cross-Functional Teams”（三张叠放卡＝多个团队）承担，并以 DORP 收尾、交付一个 MVP（白圆，外圈虚线）。橙色竖条是 DORP 关口，不是团队；团队卡是同一个标签的重复出现，表示同一类团队在连续冲刺中滚动工作。

## 关键含义（历史解释；局部修正见上）

- 全图只有一条泳道：不再区分业务开发、EA、解决方案三类团队，同一批跨职能团队承担全部工作（与图 3-4 的三泳道形成对比）。
- 叠放的三张卡表示多个跨职能团队同时工作；正文说“若干跨职能团队各自具备一定企业架构能力，在每个冲刺中创建解决方案”。
- 从冲刺 1 起每个冲刺结束交付一个 MVP（最小可行产品），图中没有单独的 MVA/MVBD 标记——三种能力在同一团队内即时协作，不再需要跨团队的中间交付物。
- 团队在冲刺末协调（正文 p29 / 中文稿 L399），所以图把协调落在 DORP 节点上，而不是另画协作连线或箭头。
- 冲刺 0 只有业务愿景输入、没有 MVP；序列开放（Sprint …），可继续任意次。
- 与图 3-2 至 3-4 对比：DORP 竖条始终保留，但柱内只剩 MVP，说明交付物从“架构/业务/解决方案三类”收敛为“产品增量”。

## 层级（历史解释；局部修正见上）

单层时间轴：每个冲刺位置上是并列的一组跨职能团队（三张叠放卡，彼此同级），MVP 标记从属于对应的 DORP 竖条。团队内部的三类能力在本图中一律未画，只在正文说明。

## 线条含义（历史解释；局部修正见上）

蓝色实线箭头一律自左向右，依次连接“业务愿景 → 冲刺 0 的 DORP → 跨职能团队 → DORP 1 → 跨职能团队 → DORP 2 → 跨职能团队 → DORP …”，箭头落在团队卡或最后一根 DORP 竖条上，表示成果的先后传递。图中没有任何虚线、双向箭头或反馈回路；团队之间的协调不是画出来的关系，而是通过 DORP 隐含。

## 易误读点（历史解释；局部修正见上）

- 不要把三张叠放卡读成三个冲刺的团队：它们是同一冲刺内并行的多个团队。
- 不要因为“Cross-Functional Teams”重复出现就以为是不同团队：同一标签重复表示同一类团队在连续冲刺中工作。
- 不要在本图里寻找 MVA/MVBD：最高成熟度下三种能力在同一团队内即时产出，图只保留 MVP 这一种交付标记。
- 不要以为 DORP 竖条是团队或阶段：它是冲刺末的收口关口。
- 中文稿当前引用的 figs/g210_fig3-5.svg 把它改成“跨职能冲刺团队 A/B + 三条能力条”，没有冲刺、DORP 与 MVP，不能据此理解本图。

## 元素

```json
[
  {
    "id": "sprint_0",
    "label_en": "Sprint 0",
    "label_zh": "冲刺 0",
    "type": "time",
    "parent": null,
    "order": 1,
    "position": "第 1 根竖条左上方"
  },
  {
    "id": "sprint_1",
    "label_en": "Sprint 1",
    "label_zh": "冲刺 1",
    "type": "time",
    "parent": null,
    "order": 2,
    "position": "第 2 根竖条左上方"
  },
  {
    "id": "sprint_2",
    "label_en": "Sprint 2",
    "label_zh": "冲刺 2",
    "type": "time",
    "parent": null,
    "order": 3,
    "position": "第 3 根竖条左上方"
  },
  {
    "id": "sprint_ellipsis",
    "label_en": "Sprint ...",
    "label_zh": "冲刺 …",
    "type": "time",
    "parent": null,
    "order": 4,
    "position": "第 4 根竖条左上方"
  },
  {
    "id": "dorp_0",
    "label_en": "DORP 0",
    "label_zh": "DORP 0",
    "type": "event",
    "parent": null,
    "order": 1,
    "position": "第 1 根竖条",
    "description_zh": "冲刺 0 的 DORP，柱内无 MVP。"
  },
  {
    "id": "dorp_1",
    "label_en": "DORP 1",
    "label_zh": "DORP 1",
    "type": "event",
    "parent": null,
    "order": 2,
    "position": "第 2 根竖条",
    "description_zh": "柱内为 MVP 标记。"
  },
  {
    "id": "dorp_2",
    "label_en": "DORP 2",
    "label_zh": "DORP 2",
    "type": "event",
    "parent": null,
    "order": 3,
    "position": "第 3 根竖条",
    "description_zh": "柱内为 MVP 标记。"
  },
  {
    "id": "dorp_ellipsis",
    "label_en": "DORP ...",
    "label_zh": "DORP …",
    "type": "event",
    "parent": null,
    "order": 4,
    "position": "第 4 根竖条",
    "description_zh": "柱内为 MVP 标记。"
  },
  {
    "id": "business_vision",
    "label_en": "Business Vision",
    "label_zh": "业务愿景",
    "type": "artifact",
    "parent": null,
    "position": "最左端方框",
    "description_zh": "整条时间轴的输入，对应正文“冲刺零定义初始业务变革需求”。"
  },
  {
    "id": "cft_1",
    "label_en": "Cross-Functional Teams",
    "label_zh": "跨职能团队",
    "type": "organization_unit",
    "parent": null,
    "position": "冲刺 1 列、三张叠放卡"
  },
  {
    "id": "cft_2",
    "label_en": "Cross-Functional Teams",
    "label_zh": "跨职能团队",
    "type": "organization_unit",
    "parent": null,
    "position": "冲刺 2 列、三张叠放卡"
  },
  {
    "id": "cft_ellipsis",
    "label_en": "Cross-Functional Teams",
    "label_zh": "跨职能团队",
    "type": "organization_unit",
    "parent": null,
    "position": "冲刺 … 列、三张叠放卡"
  },
  {
    "id": "mvp_1",
    "label_en": "MVP",
    "label_zh": "MVP（最小可行产品）",
    "type": "artifact",
    "parent": "dorp_1",
    "position": "DORP 1 柱内下部"
  },
  {
    "id": "mvp_2",
    "label_en": "MVP",
    "label_zh": "MVP（最小可行产品）",
    "type": "artifact",
    "parent": "dorp_2",
    "position": "DORP 2 柱内下部"
  },
  {
    "id": "mvp_ellipsis",
    "label_en": "MVP",
    "label_zh": "MVP（最小可行产品）",
    "type": "artifact",
    "parent": "dorp_ellipsis",
    "position": "DORP … 柱内下部"
  }
]
```

## 关系

```json
[
  {
    "id": "r_vision_d0",
    "from": "business_vision",
    "to": "dorp_0",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r_d0_cft1",
    "from": "dorp_0",
    "to": "cft_1",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "从冲刺 0 柱右侧进入第一组跨职能团队卡"
  },
  {
    "id": "r_cft1_d1",
    "from": "cft_1",
    "to": "dorp_1",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r_d1_cft2",
    "from": "dorp_1",
    "to": "cft_2",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r_cft2_d2",
    "from": "cft_2",
    "to": "dorp_2",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r_d2_cft3",
    "from": "dorp_2",
    "to": "cft_ellipsis",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "id": "r_cft3_dn",
    "from": "cft_ellipsis",
    "to": "dorp_ellipsis",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "最后一组卡连到最后一根柱，柱内为 MVP"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_sprints",
    "kind": "sequence",
    "name_zh": "冲刺序列",
    "steps": [
      "sprint_0",
      "sprint_1",
      "sprint_2",
      "sprint_ellipsis"
    ]
  },
  {
    "id": "f_teams",
    "kind": "sequence",
    "name_zh": "跨职能团队逐冲刺交付",
    "steps": [
      "cft_1",
      "cft_2",
      "cft_ellipsis"
    ]
  }
]
```

## 图例

```json
[
  {
    "symbol": "MVP = Minimum Viable Product",
    "meaning_zh": "MVP＝最小可行产品",
    "explicit": true
  },
  {
    "symbol": "DORP = Demo, Outcome, Retrospective, Planning, & Releases",
    "meaning_zh": "DORP＝演示、成果、回顾、规划与发布",
    "explicit": true
  },
  {
    "symbol": "纵向橙色竖条 + 顶端 DORP 编号",
    "meaning_zh": "一个冲刺的收口关口（DORP）",
    "explicit": false
  },
  {
    "symbol": "三张叠放卡片",
    "meaning_zh": "同一冲刺内多个并行的跨职能团队",
    "explicit": false
  },
  {
    "symbol": "白圆 + 虚线外圈",
    "meaning_zh": "该冲刺的 MVP 成果；虚线外圈表示可交付但非总是必需",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "横向单泳道：左端一个“Business Vision”方框，其后 4 根纵向橙色竖条等距排列（DORP 0/1/2/…），竖条之间放三组叠放的“Cross-Functional Teams”卡；冲刺名标在各竖条左上方；竖条内下方为 MVP 标记；底部左侧为两行缩写图例。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "三张叠放卡表示“多个团队”属推断（正文称“若干跨职能团队”），图中没有数量或团队名称。",
    "MVP 标记由白圆与偏移的虚线圆叠成，虚线外圈按图例理解为“可交付但非总是必需”。"
  ],
  "analyzed_from": [
    "figctx.py G210/fig3-5 的 220 dpi 原图裁切（英文 PDF p29）与 2x2 放大分块",
    "英文 PDF p28–p29 正文与图题",
    "中文稿 G210e_以敏捷冲刺应用TOGAF_ADM.md L376–L399",
    "figs/g210_fig3-5.svg 源码（对比重绘版式与文字）"
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
