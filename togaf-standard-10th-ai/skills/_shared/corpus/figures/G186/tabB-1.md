# G186/tabB-1 · 表 B-1：利益相关者职责（组合）

> 当前图示解析：[Markdown](../../architecture/diagrams/G186/tabB-1.md) · [JSON](../../architecture/diagrams/G186/tabB-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G186e.pdf`；SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

## 原图 · PDF 第 151 页

![英文原图](../assets/G186/tabB-1-p0151.png)

PDF 坐标：`[48.2, 55.0, 563.8, 347.7]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
s
e
&
Senior Leaders
Portfolio Managers
Business Requirements
Owners
Implementers
Risk Owners
Business Partner
Customer
```

## 概要（历史解释；局部修正见上）

用 7 类利益相关者 × 16 类关注点的 X 矩阵，标出组合目的下谁对哪些关注点负有责任。

## 目的（历史解释；局部修正见上）

附录 B 的示例矩阵：为每种架构目的维护一组标准化的利益相关者类别、关注点类别及对应关系；表 B-1 展示“组合”目的下的对应关系，作为视角库和建议沟通方式的起点。

## 阅读顺序（历史解释；局部修正见上）

横轴是 16 个关注点，列标题竖排；纵轴是 7 类利益相关者。先按行读：某类利益相关者在本目的下被标记了哪些关注点。再按列读：某个关注点由哪些利益相关者共同负责。单元格有 X 表示存在职责/对应关系，空白表示本矩阵未标注。

## 关键含义（历史解释；局部修正见上）

- 矩阵有 7 类利益相关者：高层领导、组合经理、业务需求负责人、实施者、风险责任人、业务伙伴、客户。
- 矩阵有 16 类关注点：敏捷性、效率、价值、价值主张、变更成本、变更影响、对齐、可行性、可靠性、控制、规格、安全、信心、客户亲密度、可扩展性、业务连续性。
- 全表共 52 个 X；按行计数：高层领导 8、组合经理 10、业务需求负责人 8、实施者 6、风险责任人 7、业务伙伴 7、客户 6。
- “价值”和“变更成本”两列在本矩阵中没有任何 X；这不代表它们不重要，而是本“组合”目的矩阵未把这两类关注点分配给任何利益相关者类别，需在其他目的的矩阵或视角库中补齐。
- “变更影响”“安全”“信心”覆盖面较广，均被 6 类利益相关者标记；“客户亲密度”被 4 类标记。
- 客户行只有 6 个 X（敏捷性、价值主张、安全、信心、客户亲密度、业务连续性）；附录 B 注明架构可能不直接提供给客户，但必须从客户视角评估。
- 每行/每列的组合在附录 C 中会进一步转成一个视角（viewpoint），用于确定回应关注点所需的信息与沟通方式。

## 层级（历史解释；局部修正见上）

没有上下级：行是 7 类并列的利益相关者，列是 16 类并列的关注点；矩阵是两维交叉，不是树。

## 线条含义（历史解释；局部修正见上）

图中没有连线或箭头。行列交叉处的 X 表示该利益相关者类别与该关注点存在职责/对应关系；空白单元格表示未标注。灰色行底色只是表头/行标题的区分，不表示优先级。

## 易误读点（历史解释；局部修正见上）

- 不要把它读成 RACI 矩阵：X 不区分负责、批准、咨询、知情，只表示“有关系/有职责”。
- 空白单元格不等于该利益相关者不关心该关注点，只表示本表未标注。
- “价值”“变更成本”两列全空，不能据此得出组合目的不关心价值或变更成本；附录说明每种目的各有一张矩阵。
- 本表只适用于“组合”目的，不能直接套用到战略、项目或解决方案交付目的。
- Customer Intimacy 在附录 B 的术语是“客户亲密度”，不是“客户亲近”。

## 元素

```json
[
  {
    "id": "matrix",
    "label_en": "Stakeholder Responsibility (Portfolio)",
    "label_zh": "利益相关者职责矩阵（组合）",
    "type": "group",
    "parent": null,
    "level": 0,
    "description_zh": "表 B-1 的整体矩阵。"
  },
  {
    "id": "sh_senior_leaders",
    "label_en": "Senior Leaders",
    "label_zh": "高层领导",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 1
  },
  {
    "id": "sh_portfolio_managers",
    "label_en": "Portfolio Managers",
    "label_zh": "组合经理",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 2
  },
  {
    "id": "sh_business_requirements_owners",
    "label_en": "Business Requirements Owners",
    "label_zh": "业务需求负责人",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 3
  },
  {
    "id": "sh_implementers",
    "label_en": "Implementers",
    "label_zh": "实施者",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 4
  },
  {
    "id": "sh_risk_owners",
    "label_en": "Risk Owners",
    "label_zh": "风险责任人",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 5
  },
  {
    "id": "sh_business_partner",
    "label_en": "Business Partner",
    "label_zh": "业务伙伴",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 6
  },
  {
    "id": "sh_customer",
    "label_en": "Customer",
    "label_zh": "客户",
    "type": "stakeholder",
    "parent": "matrix",
    "level": 1,
    "order": 7
  },
  {
    "id": "cn_agility",
    "label_en": "Agility",
    "label_zh": "敏捷性",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 1
  },
  {
    "id": "cn_efficiency",
    "label_en": "Efficiency",
    "label_zh": "效率",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 2
  },
  {
    "id": "cn_value",
    "label_en": "Value",
    "label_zh": "价值",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 3
  },
  {
    "id": "cn_value_proposition",
    "label_en": "Value Proposition",
    "label_zh": "价值主张",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 4
  },
  {
    "id": "cn_change_cost",
    "label_en": "Change Cost",
    "label_zh": "变更成本",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 5
  },
  {
    "id": "cn_change_impact",
    "label_en": "Change Impact",
    "label_zh": "变更影响",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 6
  },
  {
    "id": "cn_alignment",
    "label_en": "Alignment",
    "label_zh": "对齐",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 7
  },
  {
    "id": "cn_feasibility",
    "label_en": "Feasibility",
    "label_zh": "可行性",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 8
  },
  {
    "id": "cn_dependability",
    "label_en": "Dependability",
    "label_zh": "可靠性",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 9
  },
  {
    "id": "cn_control",
    "label_en": "Control",
    "label_zh": "控制",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 10
  },
  {
    "id": "cn_specification",
    "label_en": "Specification",
    "label_zh": "规格",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 11
  },
  {
    "id": "cn_security",
    "label_en": "Security",
    "label_zh": "安全",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 12
  },
  {
    "id": "cn_confidence",
    "label_en": "Confidence",
    "label_zh": "信心",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 13
  },
  {
    "id": "cn_customer_intimacy",
    "label_en": "Customer Intimacy",
    "label_zh": "客户亲密度",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 14
  },
  {
    "id": "cn_scalability",
    "label_en": "Scalability",
    "label_zh": "可扩展性",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 15
  },
  {
    "id": "cn_business_continuity",
    "label_en": "Business Continuity",
    "label_zh": "业务连续性",
    "type": "requirement",
    "parent": "matrix",
    "level": 1,
    "order": 16
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_b1",
    "title_zh": "表 B-1 利益相关者职责（组合）逐格转录",
    "columns": [
      "利益相关者",
      "Agility 敏捷性",
      "Efficiency 效率",
      "Value 价值",
      "Value Proposition 价值主张",
      "Change Cost 变更成本",
      "Change Impact 变更影响",
      "Alignment 对齐",
      "Feasibility 可行性",
      "Dependability 可靠性",
      "Control 控制",
      "Specification 规格",
      "Security 安全",
      "Confidence 信心",
      "Customer Intimacy 客户亲密度",
      "Scalability 可扩展性",
      "Business Continuity 业务连续性"
    ],
    "rows": [
      [
        "Senior Leaders 高层领导",
        "X",
        "X",
        "",
        "X",
        "",
        "X",
        "X",
        "",
        "",
        "",
        "",
        "X",
        "",
        "X",
        "",
        "X"
      ],
      [
        "Portfolio Managers 组合经理",
        "X",
        "X",
        "",
        "X",
        "",
        "X",
        "X",
        "X",
        "",
        "",
        "",
        "",
        "X",
        "X",
        "X",
        "X"
      ],
      [
        "Business Requirements Owners 业务需求负责人",
        "X",
        "X",
        "",
        "X",
        "",
        "X",
        "",
        "",
        "",
        "",
        "X",
        "X",
        "X",
        "X",
        "",
        ""
      ],
      [
        "Implementers 实施者",
        "",
        "",
        "",
        "",
        "",
        "X",
        "",
        "X",
        "",
        "X",
        "X",
        "",
        "X",
        "",
        "X",
        ""
      ],
      [
        "Risk Owners 风险责任人",
        "",
        "",
        "",
        "",
        "",
        "X",
        "",
        "X",
        "X",
        "",
        "X",
        "X",
        "X",
        "",
        "X",
        ""
      ],
      [
        "Business Partner 业务伙伴",
        "X",
        "X",
        "",
        "",
        "",
        "X",
        "",
        "X",
        "",
        "",
        "X",
        "X",
        "X",
        "",
        "",
        ""
      ],
      [
        "Customer 客户",
        "X",
        "",
        "",
        "X",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "X",
        "X",
        "X",
        "",
        "X"
      ]
    ],
    "cell_legend": [
      "X = 该利益相关者类别对该关注点有职责/对应关系；空白 = 本矩阵未标注。",
      "原表没有区分负责/批准/咨询/知情，不能当 RACI 使用。"
    ],
    "notes_zh": "逐格核对英文 PDF 第 151 页表 B-1；共 7 行 × 16 列，52 个 X。“价值”“变更成本”两列全空。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "X",
    "meaning_zh": "该利益相关者类别对该关注点有职责/对应关系（本表未细分职责类型）",
    "explicit": false
  },
  {
    "symbol": "空白单元格",
    "meaning_zh": "本矩阵未标注对应关系",
    "explicit": false
  },
  {
    "symbol": "浅灰行标题列",
    "meaning_zh": "利益相关者类别标签，仅作行标识",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "grid",
  "description_zh": "表格：左上角为空白表头单元格，右侧 16 列竖排关注点标题，下方 7 行利益相关者；行标题列有浅灰底色，单元格内为 X 或空白。"
}
```

## 相关图

```json
[
  {
    "target": "G186/fig3-3",
    "relation": "related",
    "note_zh": "图 3-3 说明四种企业架构目的；表 B-1 是“组合”目的下的利益相关者/关注点示例矩阵。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "原表没有图例；X 的确切含义（负责/关注/需参与）由表题“Stakeholder Responsibility”与附录 B 正文推断，不能区分 RACI 角色。",
    "原表是位图，个别单元格的 X 位置靠像素比对确认；已逐格核对，但无法排除原书排版造成的轻微错位。"
  ],
  "analyzed_from": [
    "英文 PDF 第 151 页表 B-1 截图（整图与 2x2 放大块，按网格逐格像素核对）",
    "英文 PDF 第 151 页表题与尾注",
    "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 2080–2124 行"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": null,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
