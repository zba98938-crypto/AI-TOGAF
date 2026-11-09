# G212/fig5-2 · ABCD 数字技术采用框架

> 当前图示解析：[Markdown](../../architecture/diagrams/G212/fig5-2.md) · [JSON](../../architecture/diagrams/G212/fig5-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G212e.pdf`；SHA-256：`1c6871264e1ca327066eec5783ec273014ce1615b13e0ef236e79b017ad4ac7b`。

## 原图 · PDF 第 40 页

![英文原图](../assets/G212/fig5-2-p0040.png)

PDF 坐标：`[125.6, 36.0, 486.4, 392.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Avant-Garde
Big-Bang
Enterprises that
Enterprises that have the
allow/enable some parts
willingness and ability to
(like an LOB, function, or
roll-out enterprise-wide
geography) to adopt first
adoption of digital
and fast, learning from and
technology, favoring a
passing on this experience
comprehensive approach
to others subsequently
coupled with speed
Discreet
Cohesive
Enterprises that take a
Enterprises that take along
cautious approach towards
every part and everyone
the adoption of digital
through a process of
technology by starting slow
consensus and integration
and steady, gradually
as a common mission,
building competence and
despite its impact on the
gaining experience
speed of adoption
Ubiquity (How Extensive is the Adoption)
```

## 本次原图核对

本次核对英文 PDF 第 40 页：左上 Avant-Garde，右上 Big-Bang，左下 Discreet，右下 Cohesive；横轴为普及度、纵轴为速度。旧中文重绘的 C/D 位置不可采用。

## 概要（历史解释；局部修正见上）

以普及度（横轴）和采用速度（纵轴）划分先锋、大爆炸、凝聚、谨慎四种采用方式。

## 目的（历史解释；局部修正见上）

第 5.1 节要求组织先选采用方法；作者用 ABCD 框架把“多广（普及度）× 多快（速度）”做成四象限，声称可适配各类组织，并强调选择必须有清晰论证——说明为什么选这种而非其他。

## 阅读顺序（历史解释；局部修正见上）

先看两根橙色轴：横轴向右表示普及度越来越高（数字实施越广），纵轴向上表示采用速度越来越快（时间是速度的函数）。四个象限按“低/高普及 × 高/低速度”定位：左上 Avant-Garde、右上 Big-Bang、左下 Discreet、右下 Cohesive。每个象限内先读方法名，再读下方说明；说明描述的是选择该方法的企业特征，不是步骤。

## 关键含义（历史解释；局部修正见上）

- 横轴是普及度（ubiquity），指数字实施的广度/广泛性；纵轴是采用速度（velocity），是时间的函数（正文 p39）。
- Avant-Garde（低普及、高速度）：允许部分业务线、职能或地域先采用，再把经验传递给其他部分。
- Big-Bang（高普及、高速度）：有意愿且有能力在全企业一次性铺开，偏好“一次到位”并兼顾速度。
- Cohesive（高普及、低速度）：通过共识与整合让每个部分作为共同使命参与，即使拖慢采用速度。
- Discreet（低普及、低速度）：谨慎起步、稳扎稳打，逐步积累能力与经验。
- 四个象限只是四种方法类型，不代表排名或评价：B 不比 A 好，C 也不比 B 好（原文注）。
- 方法选择需要论证“为什么”；图中不提供打分、门槛或选择算法。

## 层级（历史解释；局部修正见上）

只有一层：四个并列的方法类别，由两根坐标轴切成四个象限；象限之间没有上下级或包含关系，也不构成从 A 到 D 的演进。

## 线条含义（历史解释；局部修正见上）

两根橙色粗箭头是坐标轴：横轴向右、纵轴向上，箭头只表示该维度数值增加的方向，不是流程箭头。原点处的四向小箭头标示两轴相交，不连接任何象限。象限之间没有连线；四个方法的关系完全由“落在哪个象限”表达。

## 易误读点（历史解释；局部修正见上）

- A/B/C/D 不是等级：原文明确四个象限只是方法类型，B 不比 A 好、C 不比 B 好；字母顺序也不是成熟度顺序。
- 不要把四个象限读成“先 A 再 B 再 C 再 D”的路线；它们是根据两个维度区分的四种情形。
- “高速度”在上方、“高普及”在右方，是由轴箭头决定的；不要因为 Cohesive 在右下就误以为它速度高。
- 原点处的四向箭头不是“四象限互相影响”的关系线，只是坐标轴交点的装饰标记。
- 中文稿引用的 figs/g212_fig5-2.svg 把 Cohesive 与 Discreet 的左右位置对调，并换成粉彩配色；不能据它判断任一方法的坐标位置。

## 元素

```json
[
  {
    "id": "axis_ubiquity",
    "label_en": "Ubiquity (How Extensive is the Adoption)",
    "label_zh": "普及度（实施有多广）",
    "type": "other",
    "position": "底部横轴，橙色箭头向右",
    "description_zh": "数字技术采用的广度/广泛性；向右递增。"
  },
  {
    "id": "axis_velocity",
    "label_en": "Velocity (How Rapid is the Adoption)",
    "label_zh": "采用速度（多快）",
    "type": "other",
    "position": "左侧纵轴，橙色箭头向上",
    "description_zh": "预期的采用速度，是时间的函数；向上递增。"
  },
  {
    "id": "q_avant",
    "label_en": "Avant-Garde",
    "label_zh": "先锋式",
    "type": "group",
    "parent": null,
    "position": "左上（低普及、高速度）",
    "description_zh": "允许部分业务线、职能或地域先采用并快速推进，从实践中学习，随后把经验传递给其他部分。"
  },
  {
    "id": "q_bigbang",
    "label_en": "Big-Bang",
    "label_zh": "大爆炸式",
    "type": "group",
    "parent": null,
    "position": "右上（高普及、高速度）",
    "description_zh": "有意愿且有能力在全企业一次性铺开数字技术，偏好全面且快速的采用方式。"
  },
  {
    "id": "q_cohesive",
    "label_en": "Cohesive",
    "label_zh": "凝聚式",
    "type": "group",
    "parent": null,
    "position": "右下（高普及、低速度）",
    "description_zh": "通过共识与整合让组织的每个部分作为共同使命参与，即使影响采用速度。"
  },
  {
    "id": "q_discreet",
    "label_en": "Discreet",
    "label_zh": "谨慎式",
    "type": "group",
    "parent": null,
    "position": "左下（低普及、低速度）",
    "description_zh": "谨慎推进数字技术采用，起步缓慢而稳健，逐步积累能力与经验。"
  },
  {
    "id": "cross",
    "label_en": null,
    "label_zh": "原点四向箭头",
    "type": "other",
    "position": "两轴交点",
    "description_zh": "黑色四向小箭头，仅标示坐标轴相交，不表示象限间关系。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_quadrants",
    "title_zh": "ABCD 四象限（按原图位置与文字逐项转录）",
    "columns": [
      "象限位置",
      "方法",
      "速度",
      "普及度",
      "图内说明（英文原样）"
    ],
    "rows": [
      [
        "左上",
        "Avant-Garde 先锋式",
        "高",
        "低",
        "Enterprises that allow/enable some parts (like an LOB, function, or geography) to adopt first and fast, learning from and passing on this experience to others subsequently"
      ],
      [
        "右上",
        "Big-Bang 大爆炸式",
        "高",
        "高",
        "Enterprises that have the willingness and ability to roll-out enterprise-wide adoption of digital technology, favoring a comprehensive approach coupled with speed"
      ],
      [
        "右下",
        "Cohesive 凝聚式",
        "低",
        "高",
        "Enterprises that take along every part and everyone through a process of consensus and integration as a common mission, despite its impact on the speed of adoption"
      ],
      [
        "左下",
        "Discreet 谨慎式",
        "低",
        "低",
        "Enterprises that take a cautious approach towards the adoption of digital technology by starting slow and steady, gradually building competence and gaining experience"
      ]
    ],
    "notes_zh": "按象限位置（左上、右上、右下、左下）排列；速度与普及度两列据坐标轴判定。中文名取自中文稿 5.1 节；坐标轴原文：Ubiquity (How Extensive is the Adoption)、Velocity (How Rapid is the Adoption)。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "橙色粗箭头横轴",
    "meaning_zh": "普及度（实施有多广），向右递增",
    "explicit": true
  },
  {
    "symbol": "橙色粗箭头纵轴",
    "meaning_zh": "采用速度（多快），向上递增",
    "explicit": true
  },
  {
    "symbol": "灰色象限",
    "meaning_zh": "Avant-Garde（低普及、高速度）",
    "explicit": false
  },
  {
    "symbol": "深青色象限",
    "meaning_zh": "Big-Bang（高普及、高速度）",
    "explicit": false
  },
  {
    "symbol": "蓝灰色象限",
    "meaning_zh": "Cohesive（高普及、低速度）",
    "explicit": false
  },
  {
    "symbol": "近白色象限",
    "meaning_zh": "Discreet（低普及、低速度）",
    "explicit": false
  },
  {
    "symbol": "原点四向箭头",
    "meaning_zh": "标示两轴相交，无关系含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "一个 2×2 方格：左侧橙色纵轴（箭头向上）、底部橙色横轴（箭头向右），原点在左下；四象限自左上顺时针为 Avant-Garde（灰）、Big-Bang（深青）、Cohesive（蓝灰）、Discreet（近白）；原点处有四向小箭头。"
}
```

## 相关图

```json
[
  {
    "target": "G212/fig5-1",
    "relation": "detail_of",
    "note_zh": "本图展开四步路线图的步骤 1：选择采用方法"
  },
  {
    "target": "G212/fig5-4",
    "relation": "related",
    "note_zh": "图 5-4 的横轴沿用本图“普及度与采用速度”两个维度"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四个象限的填充色原图没有图例说明；本分析只按位置与色块区分，不推断颜色代表优劣（原文明确无排名）。",
    "中文稿 SVG 与英文原图的象限位置不一致，本分析以英文 PDF 第 40 页为准。"
  ],
  "analyzed_from": [
    "英文 PDF 第 40 页原图截图（2×2 放大分块）",
    "英文 PDF 第 39–40 页正文",
    "中文稿 G212e_数字技术采用就绪度评估.md 第 503–519 行",
    "figs/g212_fig5-2.svg 源码与文字"
  ],
  "date": "2026-10-31"
}
```

## 既有来源冲突

```json
[
  {
    "id": "source-g212-fig5-2",
    "figure_id": "G212/fig5-2",
    "status": "observed-conflict",
    "description": "正文§5.1定义C为高普及低变化、D为低普及低变化；本地中文重绘将底部C/D左右位置互换。",
    "evidence": [
      "G212 §5.1",
      "figs/g212_fig5-2.svg",
      "figs/ai/G212/fig5-2.json"
    ],
    "resolution": "采用正文定义：A左上、B右上、C右下、D左下；保留重绘冲突，不将图中位置误植为架构规则。"
  }
]
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "specific-findings-only",
  "all_source_pages_valid": true
}
```
