# G242/fig1-2 · 表征 ICT 行业动态的因果回路图

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig1-2.md) · [JSON](../../architecture/diagrams/G242/fig1-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 22 页

![英文原图](../assets/G242/fig1-2-p0022.png)

PDF 坐标：`[74.0, 212.4, 538.0, 652.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Business n¢
fossils ene
&
non renew:
ile
+
Business
biosphere
+
+
+
Pollution (CO2,
Digital Usages
Infrastructure
—— waste.) ;energy
Addictive
ax
algorithm
Sufficiency
Digital
Digital
Price of energy & ae Cost of Digital
3
Performance
metals
+
6. \
Digital Margin “—_____ 4
Digital
Investments
Legend
Causal linkage A->B : change of element « A » triggers the change of « B »
+ + (positive): increase of « A » triggers the increase of « B »
+ = (negative): increase of « A » triggers the decrease of « B »
« Feedback loop » output variables influence input ones
+R: Reinforcing feedback loop: causes exponential dynamic in the evolution of variables
+B: Balancing feedback loop: causes balancing dynamics
```

## 概要（历史解释；局部修正见上）

数字使用与基础设施互相强化（R1），成本平衡回路（B1）被性能提升削弱，导致 ICT 指数增长。

## 目的（历史解释；局部修正见上）

作者用系统动力学而不是线性因果来解释 ICT 增长与排放：数字使用和基础设施之间是增强型回路，本应起刹车作用的成本/性能平衡回路在 ICT 中被削弱，因此行业呈现指数级动态。它把“为什么数字化越多、排放越高”从直觉变成可追踪的变量结构，并为后文“必须设置约束、走充足性路线”提供理论依据。

## 阅读顺序（历史解释；局部修正见上）

先找到中部的 Digital Usages 与 Infrastructure 两个核心变量，沿箭头读 R1：使用增加 → 基础设施增加（+），基础设施增加又推动使用增加（+）。再看下方的 B1：基础设施增加 → 数字成本增加（+），数字成本增加 → 基础设施减少（−）。最后看右下 R2：数字利润空间 → 数字投资（+）→ 数字性能（+）→ 数字利润空间（+）。箭头旁的 + 表示同向变化、− 表示反向变化，与数值大小无关。

## 关键含义（历史解释；局部修正见上）

- R1 是数字使用与基础设施之间的双向正反馈：用得多就建得多，建得多又被推广使用，形成自我加速。
- B1 本应平衡 R1：基础设施越多成本越高（+），成本越高越抑制基础设施（−）；但数字性能提升会压低成本（数字性能 → 数字成本为 −），使刹车变弱。
- R2 说明性能提升带来利润空间，利润再投资于性能，形成另一个增强回路，进一步强化当前不稳定的增长动态。
- 两类业务与数字使用之间都是双向正反馈：依赖化石能源的业务与再生生物圈的业务都会推动数字使用，数字使用也反过来扩大这两类业务。
- 污染节点是复合变量：CO2、废弃物、能源消耗、金属开采合一；依赖化石能源的业务与基础设施都增加污染（+），再生生物圈的业务减少污染（−）。
- 成瘾性算法与数字充足性都指向数字使用，原图均标为负号（−），即两者都抑制使用；这与“充足性减少使用”的直觉一致，但成瘾性算法标负与常识相反，按原图照录。
- 能源与金属价格上涨会推高数字成本（+），是外生的成本压力。
- 整体结论：增强回路未被有效平衡，产生指数动态；正文称生产与运行数字设备所需终端能源每年增长 6.2%。

## 层级（历史解释；局部修正见上）

无层级，是一张由 11 个变量构成的因果网络；R1、B1、R2 只是回路标记，不是变量或容器。变量之间没有上下级，只有带极性的因果关系。

## 线条含义（历史解释；局部修正见上）

全部为蓝色实线箭头，箭头指向被影响变量；箭尾旁或箭头旁的 +/− 表示极性：+ 为同向（A 增则 B 增），− 为反向（A 增则 B 减）。R1/B1/R2 旁的圆形箭头只标识回路及其类型（R 增强、B 平衡），不表示额外因果。回路方向按“从变量出发沿箭头回到该变量”读取。

## 易误读点（历史解释；局部修正见上）

- +/− 是因果极性，不是“好坏”或数值正负；− 只表示反向变化。
- R1、R2 是增强型回路、B1 是平衡型回路，字母不是变量名；不能把 R1 当作某个节点。
- 数字使用与两类业务之间各有两条独立箭头（一去一回），不是一条双向箭头，含义是互为强化。
- 原图中数字成本与数字利润空间之间两条箭头都标 +（成本↑→利润↑、利润↑→成本↑），按图照录；不要自行改成“成本↑→利润↓”。
- 中文稿当前引用的 figs/zh/g242_fig1-2_zh.svg 把“数字成本→基础设施”改成了“数字成本→数字使用”，B1 的构成与原图不同；理解原图时应以英文 PDF 为准。
- 图中的“污染”不是单一排放指标，而是 CO2、废弃物、能耗与金属开采的合并变量。
- 中文稿正文把 B1 解释为“成本越高，使用越少”，但原图的负号落在“数字成本 → 基础设施”上；图与正文措辞不完全一致，按图应读作成本抑制基础设施。

## 元素

```json
[
  {
    "id": "biz_fossil",
    "label_en": "Business needing fossils energy & non renewable",
    "label_zh": "依赖化石能源与非可再生能源的业务",
    "type": "concept",
    "parent": null,
    "position": "上部偏左",
    "description_zh": "以化石能源/不可再生资源为基础的业务类型变量。"
  },
  {
    "id": "biz_biosphere",
    "label_en": "Business regenerating biosphere",
    "label_zh": "再生生物圈的业务",
    "type": "concept",
    "parent": null,
    "position": "左上角",
    "description_zh": "以再生生物圈方式运营的业务类型变量。"
  },
  {
    "id": "digital_usages",
    "label_en": "Digital Usages",
    "label_zh": "数字使用",
    "type": "concept",
    "parent": null,
    "position": "中部偏左，网络核心",
    "description_zh": "核心变量；与基础设施构成 R1。"
  },
  {
    "id": "infrastructure",
    "label_en": "Infrastructure",
    "label_zh": "基础设施",
    "type": "concept",
    "parent": null,
    "position": "中部偏右",
    "description_zh": "数字基础设施；与数字使用构成 R1，与数字成本构成 B1。"
  },
  {
    "id": "pollution",
    "label_en": "Pollution (CO2, waste...); energy consumption, metal mining",
    "label_zh": "污染（CO2、废弃物……）；能源消耗、金属开采",
    "type": "concept",
    "parent": null,
    "position": "右上部",
    "description_zh": "复合环境影响变量。"
  },
  {
    "id": "addictive_algorithm",
    "label_en": "Addictive algorithm",
    "label_zh": "成瘾性算法",
    "type": "concept",
    "parent": null,
    "position": "左中部，数字使用下方",
    "description_zh": "影响数字使用的设计因素；原图标 −。"
  },
  {
    "id": "digital_sufficiency",
    "label_en": "Digital Sufficiency",
    "label_zh": "数字充足性",
    "type": "concept",
    "parent": null,
    "position": "左下部，数字使用下方",
    "description_zh": "节制/够用原则；原图标 −，抑制使用。"
  },
  {
    "id": "price_energy_metals",
    "label_en": "Price of energy & metals",
    "label_zh": "能源与金属价格",
    "type": "concept",
    "parent": null,
    "position": "左下",
    "description_zh": "外生成本驱动。"
  },
  {
    "id": "cost_digital",
    "label_en": "Cost of Digital",
    "label_zh": "数字成本",
    "type": "concept",
    "parent": null,
    "position": "中下",
    "description_zh": "数字服务/基础设施的成本；B1 的另一端。"
  },
  {
    "id": "digital_margin",
    "label_en": "Digital Margin",
    "label_zh": "数字利润空间",
    "type": "concept",
    "parent": null,
    "position": "下中",
    "description_zh": "数字业务的利润空间；R2 的起点。"
  },
  {
    "id": "digital_performance",
    "label_en": "Digital Performance",
    "label_zh": "数字性能",
    "type": "concept",
    "parent": null,
    "position": "右下偏上",
    "description_zh": "数字服务/设备性能；影响成本、利润与基础设施。"
  },
  {
    "id": "digital_investments",
    "label_en": "Digital Investments",
    "label_zh": "数字投资",
    "type": "concept",
    "parent": null,
    "position": "右下角",
    "description_zh": "对数字性能的再投资。"
  }
]
```

## 关系

```json
[
  {
    "id": "r01",
    "from": "biz_fossil",
    "to": "digital_usages",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "依赖化石能源的业务越多，数字使用越多。"
  },
  {
    "id": "r02",
    "from": "digital_usages",
    "to": "biz_fossil",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "数字使用扩大该类业务（箭尾在数字使用、箭头指向业务变量）。"
  },
  {
    "id": "r03",
    "from": "biz_biosphere",
    "to": "digital_usages",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "再生生物圈的业务也推动数字使用。"
  },
  {
    "id": "r04",
    "from": "digital_usages",
    "to": "biz_biosphere",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "数字使用反过来扩大再生生物圈业务。"
  },
  {
    "id": "r05",
    "from": "biz_fossil",
    "to": "pollution",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "沿顶部大弧线指向污染，箭头旁标 +。"
  },
  {
    "id": "r06",
    "from": "biz_biosphere",
    "to": "pollution",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "-",
    "description_zh": "沿最上方长弧线指向污染，箭头旁标 −。"
  },
  {
    "id": "r07",
    "from": "addictive_algorithm",
    "to": "digital_usages",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "-",
    "description_zh": "原图箭头旁标 −（与直觉相反，按图照录）。"
  },
  {
    "id": "r08",
    "from": "digital_sufficiency",
    "to": "digital_usages",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "-",
    "description_zh": "数字充足性抑制数字使用。"
  },
  {
    "id": "r09",
    "from": "digital_usages",
    "to": "infrastructure",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "R1 上半环：使用增加推动基础设施建设。"
  },
  {
    "id": "r10",
    "from": "infrastructure",
    "to": "digital_usages",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "R1 下半环：基础设施增加又带动使用。"
  },
  {
    "id": "r11",
    "from": "infrastructure",
    "to": "pollution",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "水平短箭头，箭头旁标 +。"
  },
  {
    "id": "r12",
    "from": "digital_usages",
    "to": "cost_digital",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "使用越多，数字成本越高。"
  },
  {
    "id": "r13",
    "from": "infrastructure",
    "to": "cost_digital",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "B1 上半环：基础设施越多成本越高。"
  },
  {
    "id": "r14",
    "from": "cost_digital",
    "to": "infrastructure",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "-",
    "description_zh": "B1 下半环：成本上升抑制基础设施。"
  },
  {
    "id": "r15",
    "from": "digital_performance",
    "to": "infrastructure",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": null,
    "description_zh": "无极性标记的斜线，箭头指向基础设施；性能提升推动更多基础设施部署。"
  },
  {
    "id": "r16",
    "from": "digital_performance",
    "to": "cost_digital",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "-",
    "description_zh": "水平箭头向左，箭头旁标 −：性能提升降低成本。"
  },
  {
    "id": "r17",
    "from": "price_energy_metals",
    "to": "cost_digital",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "能源与金属价格上涨推高数字成本。"
  },
  {
    "id": "r18",
    "from": "digital_margin",
    "to": "cost_digital",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "左侧弯曲线，箭头在数字成本端，标 +。"
  },
  {
    "id": "r19",
    "from": "cost_digital",
    "to": "digital_margin",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "右侧弯曲线，箭头在数字利润空间端，标 +。"
  },
  {
    "id": "r20",
    "from": "digital_performance",
    "to": "digital_margin",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "长斜线，箭头指向利润空间。"
  },
  {
    "id": "r21",
    "from": "digital_margin",
    "to": "digital_investments",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "R2：利润空间带来投资。"
  },
  {
    "id": "r22",
    "from": "digital_investments",
    "to": "digital_performance",
    "type": "causal",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "polarity": "+",
    "description_zh": "R2：投资提升性能。"
  }
]
```

## 有序流程

```json
[
  {
    "id": "loop_r1",
    "kind": "loop",
    "name_zh": "R1 数字使用—基础设施增强回路",
    "steps": [
      "digital_usages",
      "infrastructure"
    ],
    "loop_type": "reinforcing",
    "description_zh": "数字使用 ↑ → 基础设施 ↑ → 数字使用 ↑。"
  },
  {
    "id": "loop_b1",
    "kind": "loop",
    "name_zh": "B1 基础设施—数字成本平衡回路",
    "steps": [
      "infrastructure",
      "cost_digital"
    ],
    "loop_type": "balancing",
    "description_zh": "基础设施 ↑ → 数字成本 ↑ → 基础设施 ↓；性能提升压低成本后又削弱该刹车。"
  },
  {
    "id": "loop_r2",
    "kind": "loop",
    "name_zh": "R2 利润—投资—性能增强回路",
    "steps": [
      "digital_margin",
      "digital_investments",
      "digital_performance"
    ],
    "loop_type": "reinforcing",
    "description_zh": "利润空间 ↑ → 数字投资 ↑ → 数字性能 ↑ → 利润空间 ↑。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "Causal linkage A->B",
    "meaning_zh": "因果连接：A 的变化触发 B 的变化",
    "explicit": true
  },
  {
    "symbol": "+（positive）",
    "meaning_zh": "正相关：A 增加导致 B 增加",
    "explicit": true
  },
  {
    "symbol": "−（negative）",
    "meaning_zh": "负相关：A 增加导致 B 减少",
    "explicit": true
  },
  {
    "symbol": "« Feedback loop »",
    "meaning_zh": "反馈回路：输出变量反过来影响输入变量",
    "explicit": true
  },
  {
    "symbol": "R（Reinforcing feedback loop）",
    "meaning_zh": "增强型反馈回路：导致变量的指数动态",
    "explicit": true
  },
  {
    "symbol": "B（Balancing feedback loop）",
    "meaning_zh": "平衡型反馈回路：导致平衡动态",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "free",
  "description_zh": "自由布局的因果网络：Business 类变量在左上，Digital Usages 居中偏左，Infrastructure 居中偏右，Pollution 在右上；成本/利润/性能/投资构成右下回路群；图例位于底部。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig1-1",
    "relation": "follows",
    "note_zh": "图 1-1 给出数据量增长的规模，本图解释其背后的回路动力"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "medium",
  "uncertainties_zh": [
    "“Addictive algorithm → Digital Usages”在原图标为 −，与常识（成瘾性算法会增加使用）相反；放大核对了箭头旁符号，仍按图照录，可能为原图笔误。",
    "“Digital Performance → Infrastructure”这条线没有极性标记，方向按箭头位置判为指向基础设施，含义需结合正文理解。",
    "数字成本与数字利润空间之间的两条箭头都标 +；按图照录，但其中一条可能本意为 −。",
    "顶部两条长弧线（两类业务→污染）在图中相互交叉，只能按端点与 +/− 符号配对，存在配对错误的可能。",
    "原图分辨率有限，个别 +/− 与箭头归属靠放大判读。",
    "正文对 B1 的文字解释（成本高→使用少）与原图连线（成本高→基础设施少）不完全对应，可能影响对 B1 的复述。"
  ],
  "analyzed_from": [
    "英文 PDF 第 22 页原图截图（1115×1057）与 4 个 2×2 放大分块",
    "原图局部放大：数字使用簇、成本—利润、污染—性能、基础设施底部",
    "英文 PDF 第 22 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 200–236 行",
    "figs/zh/g242_fig1-2_zh.svg 源码",
    "figs/g242_fig1-2_en.png（缩略图相似度核对）"
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
