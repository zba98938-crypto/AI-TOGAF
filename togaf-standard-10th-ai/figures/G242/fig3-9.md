# G242/fig3-9 · GHG Protocol 的范围与价值链排放概览 [Value Chain]

> 当前图示解析：[Markdown](../../architecture/diagrams/G242/fig3-9.md) · [JSON](../../architecture/diagrams/G242/fig3-9.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G242e.pdf`；SHA-256：`517339a5e3f509f08699c10b929f5ae14b6bca356b55e76163ffe437d54d5d19`。

## 原图 · PDF 第 60 页

![英文原图](../assets/G242/fig3-9-p0060.png)

PDF 坐标：`[125.6, 36.0, 486.4, 280.4]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
6000060
Scope 2
Scope 1
INDIRECT
DIRECT
Scope 3
Scope 3
INDIRECT
INDIRECT
4
one
iaertn
& cS]
at
—" ei
—F
oorne
E
anette
ie}
aetna
genes
=
“Doers
Perpnoril
yy
ream
vit
porting company
ownstream
ties
```

## 概要（历史解释；局部修正见上）

用 GHG Protocol 的价值链图说明排放分三个范围，并标出信息系统相关活动落在哪些环节。

## 目的（历史解释；局部修正见上）

为 3.6 节建立共同语言：先分清直接排放（范围 1）、购电相关间接排放（范围 2）和价值链间接排放（范围 3），再说明 ICT 的特点——范围 1 很小、范围 2 与数据中心和办公设备用电密切相关、一半以上碳足迹在范围 3。

## 阅读顺序（历史解释；局部修正见上）

从左到右看底部三段：上游活动 → 报告公司 → 下游活动。中间的报告公司只有两类直接排放源（公司设施、公司车辆，青绿色范围 1 箭头）；左侧灰色环形箭头是范围 2，只包含“自用购入的电力、蒸汽、供热与制冷”；其余紫色箭头都是范围 3：左侧上游 8 项活动，右侧下游 7 项活动。每项活动用图标加英文小字标出，顶部云朵里的六个圆是《京都议定书》控制的温室气体。

## 关键含义（历史解释；局部修正见上）

- 范围 1 是报告公司自有设施与车辆的直接排放；图中只有“company facilities”和“company vehicles”两项，对应正文所说 ICT 对范围 1 影响较小（空调制冷剂泄漏、应急发电机燃料）。
- 范围 2 只有一项——“purchased electricity, steam, heating & cooling for own use”；对信息系统而言即数据中心与办公硬件用电，这是 ICT 减排最直接的杠杆（购电结构、PUE）。
- 范围 3 分上下游两侧共 15 项活动：上游含采购商品与服务、资本货物、燃料与能源相关活动、运输配送、运营废弃物、商务差旅、员工通勤、租赁资产；下游含运输配送、售出产品加工、使用、报废处理、租赁资产、特许经营、投资。
- 同一名称可同时出现在上下游：图中“transportation and distribution”和“leased assets”各出现两次，分属上游与下游，不是重复错误。
- “purchased goods and services”与“capital goods”是 ICT 硬件制造排放的归属处，也是正文强调的范围 3 主体（设备制造、云服务、外包）。
- 顶部六种气体（CO₂、CH₄、N₂O、HFCs、PFCs、SF₆）说明核算统一折算为 CO₂ 当量，而不仅是 CO₂。
- 三段式（上游/报告公司/下游）提醒：组织的排放责任跨越自身边界，范围 3 由其他利益相关者运营，因而更不透明、受监管更少（正文原话）。

## 层级（历史解释；局部修正见上）

三层：第 1 层是三个价值链位置（上游活动、报告公司、下游活动）；第 2 层是四个排放范围（范围 1、范围 2、上游范围 3、下游范围 3）；第 3 层是各范围内的具体活动（范围 1 两项、范围 2 一项、范围 3 共十五项）。顶部六种温室气体是独立于范围的横向分类。

## 线条含义（历史解释；局部修正见上）

四个粗色带箭头（灰=范围 2、青绿=范围 1、紫=上游/下游范围 3）是“范围”本身的图形，不是活动之间的连线：色带把若干活动圈在其中，箭头向上指向范围标签并延伸向顶部气体云，表示这些活动的排放计入该范围并最终以温室气体形式进入大气。底部三段色带（深紫/青/深紫）只是位置坐标，不表示流向。

## 易误读点（历史解释；局部修正见上）

- 范围 2 的灰色箭头是环形回路，不代表“循环利用”；它只是把购电项圈起来并向上指。
- 范围 3 的两个紫色箭头分别位于左右两侧，不是“从上游流向下游”的一条连续箭头；上下游是并列的两组活动。
- “purchased electricity”只属于范围 2，不属于范围 3；不要因为它在左侧就归入上游范围 3。
- 中文稿第 1007 行引用的是自绘 SVG（四个并列色块），它把“其他影响（金属、水、土方、废弃物）”画成第四个范围，原图没有这个范围；阅读原图时不要把它当作范围 4。
- 图中没有“范围 4”，也不要把它读成 GHG Protocol 的“避免排放（Scope 4）”概念。

## 元素

```json
[
  {
    "id": "ghg_gases",
    "label_en": "CO₂, CH₄, N₂O, HFCs, PFCs, SF₆",
    "label_zh": "六种温室气体（CO₂、CH₄、N₂O、HFCs、PFCs、SF₆）",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "图顶部，灰色云朵内一排圆标"
  },
  {
    "id": "gas_co2",
    "label_en": "CO₂",
    "label_zh": "二氧化碳 CO₂",
    "type": "concept",
    "parent": "ghg_gases",
    "level": 2,
    "order": 1
  },
  {
    "id": "gas_ch4",
    "label_en": "CH₄",
    "label_zh": "甲烷 CH₄",
    "type": "concept",
    "parent": "ghg_gases",
    "level": 2,
    "order": 2
  },
  {
    "id": "gas_n2o",
    "label_en": "N₂O",
    "label_zh": "一氧化二氮 N₂O",
    "type": "concept",
    "parent": "ghg_gases",
    "level": 2,
    "order": 3
  },
  {
    "id": "gas_hfcs",
    "label_en": "HFCs",
    "label_zh": "氢氟碳化物 HFCs",
    "type": "concept",
    "parent": "ghg_gases",
    "level": 2,
    "order": 4
  },
  {
    "id": "gas_pfcs",
    "label_en": "PFCs",
    "label_zh": "全氟碳化物 PFCs",
    "type": "concept",
    "parent": "ghg_gases",
    "level": 2,
    "order": 5
  },
  {
    "id": "gas_sf6",
    "label_en": "SF₆",
    "label_zh": "六氟化硫 SF₆",
    "type": "concept",
    "parent": "ghg_gases",
    "level": 2,
    "order": 6
  },
  {
    "id": "scope_2",
    "label_en": "Scope 2 INDIRECT",
    "label_zh": "范围 2 间接排放",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左侧中部，灰色环形带上端"
  },
  {
    "id": "scope_1",
    "label_en": "Scope 1 DIRECT",
    "label_zh": "范围 1 直接排放",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "中央，青绿色向上箭头上端"
  },
  {
    "id": "scope_3_upstream",
    "label_en": "Scope 3 INDIRECT",
    "label_zh": "范围 3 间接排放（上游）",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "左侧偏下，紫色向上箭头上端"
  },
  {
    "id": "scope_3_downstream",
    "label_en": "Scope 3 INDIRECT",
    "label_zh": "范围 3 间接排放（下游）",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "右侧偏上，紫色向上箭头上端"
  },
  {
    "id": "purchased_goods",
    "label_en": "purchased goods and services",
    "label_zh": "采购的商品与服务",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 1,
    "position": "上游最左，工厂图标"
  },
  {
    "id": "capital_goods",
    "label_en": "capital goods",
    "label_zh": "资本货物",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 2,
    "position": "上游左二，卡车图标"
  },
  {
    "id": "fuel_energy",
    "label_en": "fuel and energy related activities",
    "label_zh": "燃料与能源相关活动",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 3,
    "position": "上游左三，油表图标"
  },
  {
    "id": "transport_up",
    "label_en": "transportation and distribution",
    "label_zh": "运输与配送（上游）",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 4,
    "position": "上游左四，货船图标"
  },
  {
    "id": "waste_ops",
    "label_en": "waste generated in operations",
    "label_zh": "运营产生的废弃物",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 5,
    "position": "上游左五，垃圾桶图标"
  },
  {
    "id": "business_travel",
    "label_en": "business travel",
    "label_zh": "商务差旅",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 6,
    "position": "上游中部，飞机图标"
  },
  {
    "id": "employee_commuting",
    "label_en": "employee commuting",
    "label_zh": "员工通勤",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 7,
    "position": "上游中部，火车图标"
  },
  {
    "id": "leased_assets_up",
    "label_en": "leased assets",
    "label_zh": "租赁资产（上游）",
    "type": "process",
    "parent": "scope_3_upstream",
    "level": 2,
    "order": 8,
    "position": "上游右侧，楼房图标，紫色箭头尖端所指"
  },
  {
    "id": "purchased_electricity",
    "label_en": "purchased electricity, steam, heating & cooling for own use",
    "label_zh": "自用购入的电力、蒸汽、供热与制冷",
    "type": "process",
    "parent": "scope_2",
    "level": 2,
    "order": 1,
    "position": "上游与报告公司之间，插头图标，灰色环形带的起点"
  },
  {
    "id": "company_facilities",
    "label_en": "company facilities",
    "label_zh": "公司设施",
    "type": "process",
    "parent": "scope_1",
    "level": 2,
    "order": 1,
    "position": "报告公司中央，建筑图标"
  },
  {
    "id": "company_vehicles",
    "label_en": "company vehicles",
    "label_zh": "公司车辆",
    "type": "process",
    "parent": "scope_1",
    "level": 2,
    "order": 2,
    "position": "公司设施下方，卡车图标"
  },
  {
    "id": "transport_down",
    "label_en": "transportation and distribution",
    "label_zh": "运输与配送（下游）",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 1,
    "position": "下游最左，货船图标"
  },
  {
    "id": "processing_sold",
    "label_en": "processing of sold products",
    "label_zh": "售出产品的加工",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 2,
    "position": "下游左二，工厂图标"
  },
  {
    "id": "use_sold",
    "label_en": "use of sold products",
    "label_zh": "售出产品的使用",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 3,
    "position": "下游中部，灯泡图标"
  },
  {
    "id": "end_of_life",
    "label_en": "end-of-life treatment of sold products",
    "label_zh": "售出产品的报废处理",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 4,
    "position": "下游中右，回收桶图标"
  },
  {
    "id": "leased_assets_down",
    "label_en": "leased assets",
    "label_zh": "租赁资产（下游）",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 5,
    "position": "下游右二，楼房图标"
  },
  {
    "id": "franchises",
    "label_en": "franchises",
    "label_zh": "特许经营",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 6,
    "position": "下游右三，店铺图标"
  },
  {
    "id": "investments",
    "label_en": "investments",
    "label_zh": "投资",
    "type": "process",
    "parent": "scope_3_downstream",
    "level": 2,
    "order": 7,
    "position": "下游最右，钞票图标，紫色箭头尖端所指"
  },
  {
    "id": "upstream_activities",
    "label_en": "Upstream activities",
    "label_zh": "上游活动",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "底部左侧深紫色横带"
  },
  {
    "id": "reporting_company",
    "label_en": "Reporting company",
    "label_zh": "报告公司",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "底部中央青色横带"
  },
  {
    "id": "downstream_activities",
    "label_en": "Downstream activities",
    "label_zh": "下游活动",
    "type": "group",
    "parent": null,
    "level": 1,
    "position": "底部右侧深紫色横带"
  }
]
```

## 关系

```json
[
  {
    "id": "r_s2_to_gases",
    "from": "scope_2",
    "to": "ghg_gases",
    "type": "flow",
    "label_en": "Scope 2 INDIRECT",
    "label_zh": "范围 2 间接排放",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "灰色环形色带向上指向范围 2 标签并延伸至顶部气体云；表示该范围的排放以温室气体形式进入大气，不是两项活动之间的数据流"
  },
  {
    "id": "r_s1_to_gases",
    "from": "scope_1",
    "to": "ghg_gases",
    "type": "flow",
    "label_en": "Scope 1 DIRECT",
    "label_zh": "范围 1 直接排放",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "青绿色粗箭头由公司车辆向上穿过公司设施指向气体云"
  },
  {
    "id": "r_s3up_to_gases",
    "from": "scope_3_upstream",
    "to": "ghg_gases",
    "type": "flow",
    "label_en": "Scope 3 INDIRECT",
    "label_zh": "范围 3 间接排放（上游）",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "左侧紫色色带向上，箭头尖端止于“leased assets”，上方为范围 3 标签"
  },
  {
    "id": "r_s3down_to_gases",
    "from": "scope_3_downstream",
    "to": "ghg_gases",
    "type": "flow",
    "label_en": "Scope 3 INDIRECT",
    "label_zh": "范围 3 间接排放（下游）",
    "explicit": true,
    "line": "thick",
    "arrow": "forward",
    "description_zh": "右侧紫色色带向上，箭头尖端止于“investments”，上方为范围 3 标签"
  },
  {
    "id": "r_up_band",
    "from": "scope_3_upstream",
    "to": "upstream_activities",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "上游范围位于“Upstream activities”横带之上"
  },
  {
    "id": "r_rep_band",
    "from": "scope_1",
    "to": "reporting_company",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "范围 1 与范围 2 位于“Reporting company”横带之上"
  },
  {
    "id": "r_down_band",
    "from": "scope_3_downstream",
    "to": "downstream_activities",
    "type": "association",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "下游范围位于“Downstream activities”横带之上"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_value_chain",
    "kind": "sequence",
    "name_zh": "价值链阅读顺序",
    "steps": [
      "upstream_activities",
      "reporting_company",
      "downstream_activities"
    ],
    "description_zh": "底部三段从左到右：上游 → 报告公司 → 下游，是阅读坐标而非时间流。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "青绿色向上箭头",
    "meaning_zh": "范围 1：直接排放",
    "explicit": true
  },
  {
    "symbol": "灰色环形向上箭头",
    "meaning_zh": "范围 2：购电相关的间接排放",
    "explicit": true
  },
  {
    "symbol": "紫色向上箭头（左右各一）",
    "meaning_zh": "范围 3：价值链间接排放（上游/下游）",
    "explicit": true
  },
  {
    "symbol": "深紫色横带“Upstream activities / Downstream activities”",
    "meaning_zh": "价值链位置（上游/下游）",
    "explicit": true
  },
  {
    "symbol": "青色横带“Reporting company”",
    "meaning_zh": "报告公司自身",
    "explicit": true
  },
  {
    "symbol": "顶部灰云中的圆标",
    "meaning_zh": "六种温室气体（CO₂、CH₄、N₂O、HFCs、PFCs、SF₆）",
    "explicit": false
  },
  {
    "symbol": "图标+小字",
    "meaning_zh": "具体价值链活动；位置决定其归属范围",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "横向三段：左侧上游活动、中间报告公司、右侧下游活动；范围色带自下而上生长，顶部一排云朵与六个气体圆标；范围 2 灰带从购电项向左上绕成环形。"
}
```

## 相关图

```json
[
  {
    "target": "G242/fig3-10",
    "relation": "basis_for",
    "note_zh": "图 3-10 用黄/蓝两色区分范围 2 与范围 3，并注明“范围定义见图 3-9”。"
  },
  {
    "target": "G242/fig3-11",
    "relation": "related",
    "note_zh": "图 3-11 的碳足迹层级同样以 CO₂ 当量为统一折算框架。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四个范围色带的“箭头”在严格意义上不是两元素之间的连线，而是范围归类图形；关系清单按“色带向上指向气体云”记录，并已在描述中说明。",
    "原图右下角的浅灰铅笔笔触为 TOGAF 版式装饰，不是文字。",
    "原图未标注作者/版权；图题只写 GHG Protocol，未在图上给出 WRI 标识。"
  ],
  "analyzed_from": [
    "英文 PDF 第 60 页（印刷页 42）原图截图、2×2 放大分块与整页概览",
    "英文 PDF 第 59–60 页正文",
    "中文稿 G242e_环境可持续的信息系统.md 第 996–1014 行",
    "figs/g242_fig3-9.svg 源码"
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
