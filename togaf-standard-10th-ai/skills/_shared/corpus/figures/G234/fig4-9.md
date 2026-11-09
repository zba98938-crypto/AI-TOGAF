# G234/fig4-9 · 元数据集成模式

> 当前图示解析：[Markdown](../../architecture/diagrams/G234/fig4-9.md) · [JSON](../../architecture/diagrams/G234/fig4-9.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G234e.pdf`；SHA-256：`34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G234/fig4-9-p0028.png)

PDF 坐标：`[61.1, 481.0, 550.9, 584.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Pattern 4 Manualingestion
Pattern? Pushing Metadata
Pattern 3 Pulling Metadata
Environment A
Environment,
Environment
Metadata
ment
data
ent
=
=
2
Tool
Pari
=
i
Environment
Environment 8
Environment
a &
a &
7 2
=
=
=
4
l
```

## 概要（历史解释；局部修正见上）

三种元数据交换模式：人工导出上传、源端推送、工具端代理拉取。

## 目的（历史解释；局部修正见上）

正文把元数据交换方式归纳为手工摄取、推送、拉取三类，并说明三者对运营效率、供应商支持、安全审计的影响；本图用同一套环境 A/B 场景并列画出三条路径，便于选型。

## 阅读顺序（历史解释；局部修正见上）

从左到右读三个面板，它们不是先后步骤而是三种可选模式。每个面板内先看 Environment A（上）与 Environment B（下）：三台数据库汇入 Int（集成组件）或 Agent（代理），再看右侧 Metadata Management Tool。箭头线型区分人工（灰色虚线 + 人物）、系统推送（黑色虚线 + API）、拉取（黑色实线 + 代理）。

## 关键含义（历史解释；局部修正见上）

- 模式 1 手工摄取：各环境由 Int 导出，经人工上传到元数据管理工具；人物图标即人工环节，效率最低但供应商依赖最少。
- 模式 2 推送元数据：源端按协作契约（格式、数据结构、频率）主动把约定范围推给工具，经 API 传输，责任在源端。
- 模式 3 拉取元数据：工具把代理部署到源端，代理采集或推断后回传；通常用于技术与运营元数据。
- 三种模式都画了两个环境（A/B），说明同一组织内不同来源可采用不同模式，不必统一。
- 业务元数据仍需人工投入（正文），因此模式 1 不会被完全取代。
- Int 是源端集成组件，不是元数据存储库；API 是推送接口徽标，Agent 是部署在源端的采集代理。

## 层级（历史解释；局部修正见上）

三个并列模式（Pattern 1/2/3）；每个模式下 Environment A 与 Environment B 两个并列环境，各环境内三台数据库 → Int/Agent；右侧工具为共同目标端。

## 线条含义（历史解释；局部修正见上）

灰色虚线 + 人物 = 人工导出/上传；黑色虚线 + API = 系统推送；黑色实线 + Agent = 工具拉取。数据库到 Int 的细灰箭头是环境内部汇聚，不属于跨系统交换。

## 易误读点（历史解释；局部修正见上）

- 不要把三个面板当成实施步骤或成熟度阶段，它们是三种可选交换方式。
- 不要把模式 3 的 Agent 当成独立工具；它部署在源端，受中央工具控制。
- 不要把模式 1 的箭头当成系统自动流转；人物图标表示必须有人工导出与上传。
- 中文 SVG 丢失了模式 1 的人工上传箭头，不能据它认为 Int 直接连到工具。

## 元素

```json
[
  {
    "id": "p1_title",
    "label_en": "Pattern 1 – Manual Ingestion",
    "label_zh": "模式 1——手工摄取",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "左面板标题"
  },
  {
    "id": "p1_env_a",
    "label_en": "Environment A",
    "label_zh": "环境 A",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "左面板上方"
  },
  {
    "id": "p1_dbs_a",
    "label_zh": "数据库（3 台，无标签）",
    "type": "group",
    "parent": "p1_env_a",
    "level": 3,
    "position": "环境 A 内左侧"
  },
  {
    "id": "p1_int_a",
    "label_en": "Int",
    "label_zh": "集成组件（Int）",
    "type": "application",
    "parent": "p1_env_a",
    "level": 3,
    "position": "环境 A 内右侧"
  },
  {
    "id": "p1_person_a",
    "label_zh": "人工操作者（环境 A）",
    "type": "actor",
    "parent": null,
    "level": 2,
    "position": "环境 A 与工具之间",
    "description_zh": "原图仅人物图标，无文字标签；表示导出与上传的人工环节。"
  },
  {
    "id": "p1_env_b",
    "label_en": "Environment B",
    "label_zh": "环境 B",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "左面板下方"
  },
  {
    "id": "p1_dbs_b",
    "label_zh": "数据库（3 台，无标签）",
    "type": "group",
    "parent": "p1_env_b",
    "level": 3
  },
  {
    "id": "p1_int_b",
    "label_en": "Int",
    "label_zh": "集成组件（Int）",
    "type": "application",
    "parent": "p1_env_b",
    "level": 3
  },
  {
    "id": "p1_person_b",
    "label_zh": "人工操作者（环境 B）",
    "type": "actor",
    "parent": null,
    "level": 2,
    "position": "环境 B 与工具之间"
  },
  {
    "id": "p1_tool",
    "label_en": "Metadata Management Tool",
    "label_zh": "元数据管理工具",
    "type": "application",
    "parent": null,
    "level": 2,
    "position": "左面板右侧"
  },
  {
    "id": "p2_title",
    "label_en": "Pattern 2 – Pushing Metadata",
    "label_zh": "模式 2——推送元数据",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "中面板标题"
  },
  {
    "id": "p2_env_a",
    "label_en": "Environment A",
    "label_zh": "环境 A",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "中面板上方"
  },
  {
    "id": "p2_dbs_a",
    "label_zh": "数据库（3 台，无标签）",
    "type": "group",
    "parent": "p2_env_a",
    "level": 3
  },
  {
    "id": "p2_int_a",
    "label_en": "Int",
    "label_zh": "集成组件（Int）",
    "type": "application",
    "parent": "p2_env_a",
    "level": 3
  },
  {
    "id": "p2_env_b",
    "label_en": "Environment B",
    "label_zh": "环境 B",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "中面板下方"
  },
  {
    "id": "p2_dbs_b",
    "label_zh": "数据库（3 台，无标签）",
    "type": "group",
    "parent": "p2_env_b",
    "level": 3
  },
  {
    "id": "p2_int_b",
    "label_en": "Int",
    "label_zh": "集成组件（Int）",
    "type": "application",
    "parent": "p2_env_b",
    "level": 3
  },
  {
    "id": "p2_tool",
    "label_en": "Metadata Management Tool",
    "label_zh": "元数据管理工具",
    "type": "application",
    "parent": null,
    "level": 2,
    "position": "中面板右侧"
  },
  {
    "id": "p2_api_a",
    "label_en": "API",
    "label_zh": "API",
    "type": "service",
    "parent": null,
    "level": 3,
    "position": "工具左上"
  },
  {
    "id": "p2_api_b",
    "label_en": "API",
    "label_zh": "API",
    "type": "service",
    "parent": null,
    "level": 3,
    "position": "工具右下"
  },
  {
    "id": "p3_title",
    "label_en": "Pattern 3 – Pulling Metadata",
    "label_zh": "模式 3——拉取元数据",
    "type": "note",
    "parent": null,
    "level": 1,
    "position": "右面板标题"
  },
  {
    "id": "p3_env_a",
    "label_en": "Environment A",
    "label_zh": "环境 A",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "右面板上方"
  },
  {
    "id": "p3_dbs_a",
    "label_zh": "数据库（3 台，无标签）",
    "type": "group",
    "parent": "p3_env_a",
    "level": 3
  },
  {
    "id": "p3_agent_a",
    "label_en": "Agent",
    "label_zh": "代理",
    "type": "application",
    "parent": "p3_env_a",
    "level": 3
  },
  {
    "id": "p3_env_b",
    "label_en": "Environment B",
    "label_zh": "环境 B",
    "type": "group",
    "parent": null,
    "level": 2,
    "position": "右面板下方"
  },
  {
    "id": "p3_dbs_b",
    "label_zh": "数据库（3 台，无标签）",
    "type": "group",
    "parent": "p3_env_b",
    "level": 3
  },
  {
    "id": "p3_agent_b",
    "label_en": "Agent",
    "label_zh": "代理",
    "type": "application",
    "parent": "p3_env_b",
    "level": 3
  },
  {
    "id": "p3_tool",
    "label_en": "Metadata Management Tool",
    "label_zh": "元数据管理工具",
    "type": "application",
    "parent": null,
    "level": 2,
    "position": "右面板右侧"
  }
]
```

## 关系

```json
[
  {
    "from": "p1_dbs_a",
    "to": "p1_int_a",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "环境 A 内三台数据库各有一条细灰箭头汇入 Int。"
  },
  {
    "from": "p1_int_a",
    "to": "p1_person_a",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "Int 导出元数据，交给人工处理。"
  },
  {
    "from": "p1_person_a",
    "to": "p1_tool",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "人工把导出文件上传到元数据管理工具。"
  },
  {
    "from": "p1_dbs_b",
    "to": "p1_int_b",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "p1_int_b",
    "to": "p1_person_b",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward"
  },
  {
    "from": "p1_person_b",
    "to": "p1_tool",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward"
  },
  {
    "from": "p2_dbs_a",
    "to": "p2_int_a",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "p2_int_a",
    "to": "p2_api_a",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward",
    "description_zh": "源端经 API 推送元数据。"
  },
  {
    "from": "p2_api_a",
    "to": "p2_tool",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward"
  },
  {
    "from": "p2_dbs_b",
    "to": "p2_int_b",
    "type": "flow",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "p2_int_b",
    "to": "p2_api_b",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward"
  },
  {
    "from": "p2_api_b",
    "to": "p2_tool",
    "type": "flow",
    "explicit": true,
    "line": "dashed",
    "arrow": "forward"
  },
  {
    "from": "p3_agent_a",
    "to": "p3_dbs_a",
    "type": "access",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "代理读取环境中的三台数据库，灰色箭头指向数据库。"
  },
  {
    "from": "p3_tool",
    "to": "p3_agent_a",
    "type": "assignment",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "工具向源端部署/控制代理。"
  },
  {
    "from": "p3_agent_b",
    "to": "p3_dbs_b",
    "type": "access",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "代理读取环境中的三台数据库，灰色箭头指向数据库。"
  },
  {
    "from": "p3_tool",
    "to": "p3_agent_b",
    "type": "assignment",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色虚线 + 人物图标",
    "meaning_zh": "人工导出/上传（手工摄取）",
    "explicit": false
  },
  {
    "symbol": "黑色虚线 + API 徽标",
    "meaning_zh": "源端通过接口推送元数据",
    "explicit": false
  },
  {
    "symbol": "黑色实线 + Agent 徽标",
    "meaning_zh": "工具在源端部署代理拉取元数据",
    "explicit": false
  },
  {
    "symbol": "细灰箭头（数据库 → Int）",
    "meaning_zh": "环境内元数据汇聚到集成组件",
    "explicit": false
  },
  {
    "symbol": "蓝色方框 Metadata Management Tool",
    "meaning_zh": "元数据管理工具/目标端",
    "explicit": true
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "三个等宽面板从左到右；每个面板上方 Environment A、下方 Environment B、右侧 Metadata Management Tool；模式 2 另有 API 徽标，模式 3 用 Agent 替换 Int。"
}
```

## 相关图

```json
[
  {
    "target": "G234/fig4-6",
    "relation": "related",
    "note_zh": "三种集成模型决定中央库与来源的主副本关系，图 4-9 决定具体交换通道"
  },
  {
    "target": "G234/fig4-10",
    "relation": "complements",
    "note_zh": "拉取模式常配合图 4-10 的技术元数据推断"
  },
  {
    "target": "G234/fig4-8",
    "relation": "related",
    "note_zh": "统一式存储库仍需通过本图三种模式与外部来源交换"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "模式 1 中人物与工具之间的虚线在原图中不清晰，按“人工上传”语义记录为人物 → 工具。",
    "模式 3 的粗黑线两端均有箭头观感，按“工具部署代理、代理回传”语义记为工具 → 代理单向；正文的“拉取”描述支持这一方向。",
    "图中三台数据库均无文字标签，以“数据库（3 台）”分组元素代表。"
  ],
  "analyzed_from": [
    "英文 PDF 第 28 页原图截图（2x2 与 3x3 放大分块）",
    "英文 PDF 第 28–29 页正文与图例",
    "中文稿 G234e_信息架构_元数据管理.md 第 425–463 行",
    "figs/g234e_fig4-9_en.png、figs/zh/g234e_fig4-9_zh.png、figs/zh/g234e_fig4-9_zh.svg"
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
