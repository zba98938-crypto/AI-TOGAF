# G184/fig4-3 · PMI 影响力矩阵

> 当前图示解析：[Markdown](../../architecture/diagrams/G184/fig4-3.md) · [JSON](../../architecture/diagrams/G184/fig4-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G184e.pdf`；SHA-256：`85fe5653767b184c3c8c9c1bef9f5738adbb2bf6661fb50ee95e72d16bc9f614`。

## 原图 · PDF 第 40 页

![英文原图](../assets/G184/fig4-3-p0040.png)

PDF 坐标：`[125.6, 485.2, 486.4, 721.5]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text

```

## 概要（历史解释；局部修正见上）

按影响力与影响程度高低把利益相关者分入四个象限：重点管理、令其满意、随时告知、监督。

## 目的（历史解释；局部修正见上）

第 4.2.6 节要求领导者理解企业的问责模型与决策模型，以便在利益相关者之间做权衡决策。作者引用 PMI 的 2×2 矩阵，用来梳理企业内各成员的期望、利益、在 EA 中的角色以及在 EA 能力中的角色，并据此确定与每类利益相关者打交道的方式。

## 阅读顺序（历史解释；局部修正见上）

先看两个轴：左侧向上的灰色箭头是“影响力水平（Level of Influence）”，底部向右的灰色箭头是“影响程度（Level of Impact）”。四个象限按两轴高低组合：左上“令其满意”（影响力高、影响程度低）、右上“重点管理”（两者都高）、左下“监督”（两者都低）、右下“随时告知”（影响力低、影响程度高）。轴只有方向，没有刻度；图中没有标出具体的利益相关者。

## 关键含义（历史解释；局部修正见上）

- 两个维度：影响力水平与影响程度；每个利益相关者按两者高低落入一个象限，象限名称就是对其采取的管理策略。
- 重点管理（Manage Closely）：影响力和影响程度都高，需要投入最多精力、密切合作。
- 令其满意（Keep Satisfied）：影响力高但影响程度低，要满足其需要，但不必在细节上频繁打扰。
- 随时告知（Keep Informed）：影响程度高但影响力低，要持续通报情况。
- 监督（Monitor）：两者都低，只需关注其变化。以上四条策略的含义按 PMBOK 的通常用法解释，原图只给出名称。
- 正文说这个矩阵涵盖企业内各成员的期望、利益、在 EA 中的角色和在 EA 能力中的角色；问责模型在 EA 能力的赞助与对它的期望之间取得平衡，是跨利益相关者做权衡决策的关键。
- 正文示例：GAAP 变更是按期还是提前采用，由 CFO 与法律顾问共同决定；某台机器是否升级推荐的安全软件，由数据中心管理员与信息安全人员共同决定；EA 能力团队通常处在这些层级之间。
- 正文建议还可用 SCORE、RACI 等模型识别和记录角色与问责；角色和问责应对应到关注点而不是项目，并明确组织边界与决策边界。

## 层级（历史解释；局部修正见上）

没有上下级。四个象限是同级的利益相关者类别，位置由两轴的高低组合决定。

## 线条含义（历史解释；局部修正见上）

图中只有两个轴向箭头，表示数值递增方向，不是流程或因果。四个象限之间没有连线；关系清单为空，每个象限的两轴取值写在元素属性和表格中。

## 易误读点（历史解释；局部修正见上）

- “令其满意”在左上（影响力高、影响程度低），“随时告知”在右下（影响力低、影响程度高），二者容易记反。
- Influence 与 Impact 中文都可译作“影响”，但是两个不同的轴：纵轴是影响力（Influence），横轴是影响程度（Impact）。
- 图中没有刻度，也没有标出具体利益相关者；它是分类框架，不是某个企业的利益相关者分布图。
- 本图回答“如何与各类利益相关者打交道”，不是 RACI 那样的责任分配矩阵，也不规定决策权。
- 中文稿第 4.2.6 节（L243–245）把英文本节压缩为一段，没有收录本图，也没有提到 PMI 矩阵和 SCORE/RACI。

## 元素

```json
[
  {
    "id": "axis_influence",
    "label_en": "Level of Influence",
    "label_zh": "影响力水平",
    "type": "metric",
    "position": "左侧纵轴（向上箭头）",
    "attributes": {
      "direction": "自下而上递增"
    }
  },
  {
    "id": "axis_impact",
    "label_en": "Level of Impact",
    "label_zh": "影响程度",
    "type": "metric",
    "position": "底部横轴（向右箭头）",
    "attributes": {
      "direction": "自左向右递增"
    }
  },
  {
    "id": "q_keep_satisfied",
    "label_en": "Keep Satisfied",
    "label_zh": "令其满意",
    "type": "concept",
    "position": "左上（影响力高、影响程度低）",
    "attributes": {
      "influence": "High",
      "impact": "Low"
    }
  },
  {
    "id": "q_manage_closely",
    "label_en": "Manage Closely",
    "label_zh": "重点管理",
    "type": "concept",
    "position": "右上（影响力高、影响程度高）",
    "attributes": {
      "influence": "High",
      "impact": "High"
    }
  },
  {
    "id": "q_monitor",
    "label_en": "Monitor",
    "label_zh": "监督",
    "type": "concept",
    "position": "左下（影响力低、影响程度低）",
    "attributes": {
      "influence": "Low",
      "impact": "Low"
    }
  },
  {
    "id": "q_keep_informed",
    "label_en": "Keep Informed",
    "label_zh": "随时告知",
    "type": "concept",
    "position": "右下（影响力低、影响程度高）",
    "attributes": {
      "influence": "Low",
      "impact": "High"
    }
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_quadrants",
    "title_zh": "四个象限（按原图转录）",
    "columns": [
      "象限（策略）",
      "影响力水平",
      "影响程度",
      "位置"
    ],
    "rows": [
      [
        "令其满意 Keep Satisfied",
        "高",
        "低",
        "左上"
      ],
      [
        "重点管理 Manage Closely",
        "高",
        "高",
        "右上"
      ],
      [
        "监督 Monitor",
        "低",
        "低",
        "左下"
      ],
      [
        "随时告知 Keep Informed",
        "低",
        "高",
        "右下"
      ]
    ],
    "notes_zh": "原图每个象限只有策略名称，没有说明文字；轴只有方向箭头，没有 Low/High 刻度，高低由箭头方向读出。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "左侧向上的灰色箭头 Level of Influence",
    "meaning_zh": "影响力水平，越往上越高",
    "explicit": true
  },
  {
    "symbol": "底部向右的灰色箭头 Level of Impact",
    "meaning_zh": "影响程度，越往右越高",
    "explicit": true
  },
  {
    "symbol": "灰色象限 + 粗体文字",
    "meaning_zh": "一类利益相关者及对其采取的管理策略；四块同色，颜色没有编码含义",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "2×2 网格，四个等大的灰色象限；左侧是向上的灰色箭头（Level of Influence），底部是向右的灰色箭头（Level of Impact）。"
}
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "四种策略的中文译名（重点管理、令其满意、随时告知、监督）参照 PMBOK 中文版的常见译法，由解析者拟定；中文稿未收录本图。",
    "原图只给策略名称，key_points 中对各策略含义的解释按 PMBOK 的通常用法补充。"
  ],
  "analyzed_from": [
    "英文 PDF 第 40 页原图截图（220 dpi）",
    "英文 PDF 第 40 页正文（第 4.2.6 节）、第 45 页第 4 章尾注 [2]",
    "中文稿 G184e_领导者指南_建立并演进EA能力.md 第 243–245 行（本图未被中文稿引用）"
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
