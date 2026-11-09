# G152/fig4-1 · 安全作为横切关注点

> 当前图示解析：[Markdown](../../architecture/diagrams/G152/fig4-1.md) · [JSON](../../architecture/diagrams/G152/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G152e.pdf`；SHA-256：`919c53bfa4259a4b3a9686762f37c0576a1cd2f8e77e74648826d9f9c84ed6e0`。

## 原图 · PDF 第 28 页

![英文原图](../assets/G152/fig4-1-p0028.png)

PDF 坐标：`[151.3, 223.2, 460.7, 589.8]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Security
_
Business
Va
Data
X
Va
Application
X
Va
Technology
```

## 概要（历史解释；局部修正见上）

安全不是第五个架构域，而是一条纵向贯穿业务、数据、应用、技术四个架构域的横切关注点。

## 目的（历史解释；局部修正见上）

用最简的叠加图说明安全架构的定位：TOGAF ADM 的四个架构域是横向分层，安全架构则以一条竖列同时穿过四层，因此被称为横切关注点；它为四个域提供安全、隐私与运营风险视角，并影响/输入四个域。

## 阅读顺序（历史解释；局部修正见上）

自上而下先读四条横条：Business、Data、Application、Technology，这是企业架构的四个域。然后把视线移到中间那条白色竖列 Security：它从 Business 上方一直延伸到 Technology 下方，压住四条横条，表示安全同时作用于四个域，而不是其中某一层。图中没有任何箭头，关系完全由“覆盖/穿过”表达。

## 关键含义（历史解释；局部修正见上）

- 四个架构域自上而下为 Business、Data、Application、Technology，与 TOGAF ADM 的四个架构域一致。
- Security 是一条竖向列，覆盖全部四条横条，并且上下都超出堆叠范围，强调它不受任一架构域边界限制。
- Security 列画在四条横条之上（白色填充遮住横条中段），是“横切/穿透”的视觉表达，不是四条横条在此断开。
- 正文据此说明安全架构与四个域都交互，因而称为横切关注点；它影响并向 Business、Data、Application、Technology 四个架构提供输入。
- 安全架构不只是数据集，而是视图、视角与制品的连贯集合，包含安全、隐私与运营风险视角，并以 ISM 与 ERM 过程为基础。
- 安全架构可能常在企业架构范围之外组织，但其部分内容必须与架构整合开发；第 5 章逐一说明这些接触点。

## 层级（历史解释；局部修正见上）

两层：底层是四个并列的架构域（上下堆叠，无包含关系）；上层是一条跨域的 Security 列。Security 与四个域是“横切/作用于”的关系，不是四个域之上的第五层，也不是某一个域的子元素。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头。四条横条的上下排列表示架构域的分层顺序；Security 竖列与四条横条的交叉覆盖表示横切关系。白色列遮住横条中段只是绘制层次（前景/背景），不表示中断或缺口。

## 易误读点（历史解释；局部修正见上）

- 不要把 Security 读成第五个架构域或最上面/最下面的一层：它是纵列，贯穿全部四层。
- 四条横条在 Security 列处看不见，不是断开了；那是白色前景遮挡。
- 四个架构域不是时间顺序或流程步骤，只是分层堆叠。
- 图内没有箭头，不能推断“安全 → 业务”这样的单向流；正文用“impacts and informs”描述的是影响与输入，方向需按正文理解。
- 中文稿当前引用的 figs/g152_fig4-1.svg 改成了 5 个并排框 + 底部横条，并多出“交付运营”，不能据它理解原图的纵向穿透结构。

## 元素

```json
[
  {
    "id": "business",
    "label_en": "Business",
    "label_zh": "业务架构",
    "type": "architecture",
    "parent": null,
    "level": 1,
    "order": 1,
    "position": "最上层横条"
  },
  {
    "id": "data",
    "label_en": "Data",
    "label_zh": "数据架构",
    "type": "architecture",
    "parent": null,
    "level": 2,
    "order": 2,
    "position": "第二层横条"
  },
  {
    "id": "application",
    "label_en": "Application",
    "label_zh": "应用架构",
    "type": "architecture",
    "parent": null,
    "level": 3,
    "order": 3,
    "position": "第三层横条"
  },
  {
    "id": "technology",
    "label_en": "Technology",
    "label_zh": "技术架构",
    "type": "architecture",
    "parent": null,
    "level": 4,
    "order": 4,
    "position": "最下层横条"
  },
  {
    "id": "security",
    "label_en": "Security",
    "label_zh": "安全（横切关注点）",
    "type": "architecture",
    "parent": null,
    "position": "纵贯四层的白色竖列",
    "description_zh": "代表安全架构：安全、隐私与运营风险视角的视图/视角/制品集合。"
  }
]
```

## 关系

```json
[
  {
    "id": "r1",
    "from": "security",
    "to": "business",
    "type": "influence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none",
    "description_zh": "由竖列覆盖该横条表达横切影响。"
  },
  {
    "id": "r2",
    "from": "security",
    "to": "data",
    "type": "influence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r3",
    "from": "security",
    "to": "application",
    "type": "influence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  },
  {
    "id": "r4",
    "from": "security",
    "to": "technology",
    "type": "influence",
    "explicit": false,
    "line": "implicit",
    "arrow": "none"
  }
]
```

## 图例

```json
[
  {
    "symbol": "灰色横向圆角长条",
    "meaning_zh": "一个企业架构域（Business / Data / Application / Technology）",
    "explicit": false
  },
  {
    "symbol": "白色竖向圆角长列",
    "meaning_zh": "Security——横切四个架构域的关注点",
    "explicit": false
  },
  {
    "symbol": "Security 列覆盖在横条之上并上下超出",
    "meaning_zh": "安全穿透并超出任一架构域的边界",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "四条等宽横条自上而下堆叠；一条白色圆角竖列位于画面中部，纵向覆盖四条横条并上下伸出；整体无标题、无图例。"
}
```

## 相关图

```json
[
  {
    "target": "G152/fig1-1",
    "relation": "complements",
    "note_zh": "图 1-1 的总览把安全放在 ESA 区域，本图进一步说明安全在四个架构域中的横切位置。"
  },
  {
    "target": "G152/fig5-2",
    "relation": "related",
    "note_zh": "第 5 章随后用 ArchiMate 模型（图 5-2）展示安全与风险概念如何落到具体元素，是本图“接触点”的展开。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "图中没有箭头与图例；“Security 影响四个域”的方向依据正文 impacts and informs，而非图内符号。",
    "Security 列上下超出堆叠范围是否有额外含义（如超出架构范围组织），图内无说明，未作推断。"
  ],
  "analyzed_from": [
    "英文 PDF 第 28 页原图截图（220 dpi）及 2x2 放大分块",
    "英文 PDF 第 28 页正文",
    "中文稿 G152e_将风险与安全融入TOGAF企业架构.md 第 306–308 行",
    "figs/g152_fig4-1.svg 源码"
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
