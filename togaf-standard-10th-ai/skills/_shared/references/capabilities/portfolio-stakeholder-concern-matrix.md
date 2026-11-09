# 组合利益相关者×关注点矩阵

ID：`portfolio-stakeholder-concern-matrix`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/tabB-1。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。



## 输入及缺口处理

必需：

- 视点问题与范围
- 带来源的对象、关系及定义

可选：

- 企业裁剪及例外说明

关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。

## 元素、属性与关系

对象类型：g186:concern, g186:stakeholder。

```json
{
  "*": [
    "definition"
  ]
}
```

{
  "definition": {
    "meaning": "对象在本视点中的可检查定义",
    "value_rule": "使用可追溯描述；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `g186:responsibility` | g186:concern,g186:stakeholder → g186:concern,g186:stakeholder | 显式包含或职责映射，不表示流程或批准 |

## 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

## 输出、检查与误读

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

- 关系端点及类型有效
- 专用拓扑检查通过
- 必要字段可追溯到实际输出

- 登记来源或成功生成不表示来源等价
- 参考示例的固定结构不直接强制所有企业采用


## 视图和交付物

- [组合利益相关者×关注点矩阵](../profiles/portfolio-stakeholder-concern-matrix.md)

- [communications-plan](../deliverables/communications-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "从所选对象删除必需的definition属性，保留其稳定ID及视图选择。",
    "expected": "missing-profile-attribute",
    "why": "缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。"
  },
  "modification_example": {
    "change": "修改同ID对象的definition，保持结构角色、类别和边界属性不变。",
    "expected": "reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G186/tabB-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "sh_senior_leaders",
      "type": "g186:stakeholder",
      "name": "高层领导",
      "attributes": {
        "definition": "Senior Leaders",
        "order": 1,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sh_portfolio_managers",
      "type": "g186:stakeholder",
      "name": "组合经理",
      "attributes": {
        "definition": "Portfolio Managers",
        "order": 2,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sh_business_requirements_owners",
      "type": "g186:stakeholder",
      "name": "业务需求负责人",
      "attributes": {
        "definition": "Business Requirements Owners",
        "order": 3,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sh_implementers",
      "type": "g186:stakeholder",
      "name": "实施者",
      "attributes": {
        "definition": "Implementers",
        "order": 4,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sh_risk_owners",
      "type": "g186:stakeholder",
      "name": "风险责任人",
      "attributes": {
        "definition": "Risk Owners",
        "order": 5,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sh_business_partner",
      "type": "g186:stakeholder",
      "name": "业务伙伴",
      "attributes": {
        "definition": "Business Partner",
        "order": 6,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sh_customer",
      "type": "g186:stakeholder",
      "name": "客户",
      "attributes": {
        "definition": "Customer",
        "order": 7,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_agility",
      "type": "g186:concern",
      "name": "敏捷性",
      "attributes": {
        "definition": "Agility",
        "order": 1,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_efficiency",
      "type": "g186:concern",
      "name": "效率",
      "attributes": {
        "definition": "Efficiency",
        "order": 2,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_value",
      "type": "g186:concern",
      "name": "价值",
      "attributes": {
        "definition": "Value",
        "order": 3,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_value_proposition",
      "type": "g186:concern",
      "name": "价值主张",
      "attributes": {
        "definition": "Value Proposition",
        "order": 4,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_change_cost",
      "type": "g186:concern",
      "name": "变更成本",
      "attributes": {
        "definition": "Change Cost",
        "order": 5,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_change_impact",
      "type": "g186:concern",
      "name": "变更影响",
      "attributes": {
        "definition": "Change Impact",
        "order": 6,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_alignment",
      "type": "g186:concern",
      "name": "对齐",
      "attributes": {
        "definition": "Alignment",
        "order": 7,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_feasibility",
      "type": "g186:concern",
      "name": "可行性",
      "attributes": {
        "definition": "Feasibility",
        "order": 8,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_dependability",
      "type": "g186:concern",
      "name": "可靠性",
      "attributes": {
        "definition": "Dependability",
        "order": 9,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_control",
      "type": "g186:concern",
      "name": "控制",
      "attributes": {
        "definition": "Control",
        "order": 10,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_specification",
      "type": "g186:concern",
      "name": "规格",
      "attributes": {
        "definition": "Specification",
        "order": 11,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_security",
      "type": "g186:concern",
      "name": "安全",
      "attributes": {
        "definition": "Security",
        "order": 12,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_confidence",
      "type": "g186:concern",
      "name": "信心",
      "attributes": {
        "definition": "Confidence",
        "order": 13,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_customer_intimacy",
      "type": "g186:concern",
      "name": "客户亲密度",
      "attributes": {
        "definition": "Customer Intimacy",
        "order": 14,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_scalability",
      "type": "g186:concern",
      "name": "可扩展性",
      "attributes": {
        "definition": "Scalability",
        "order": 15,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cn_business_continuity",
      "type": "g186:concern",
      "name": "业务连续性",
      "attributes": {
        "definition": "Business Continuity",
        "order": 16,
        "purpose": "portfolio"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "responsibility-0-0",
      "source": "sh_senior_leaders",
      "target": "cn_agility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-1",
      "source": "sh_senior_leaders",
      "target": "cn_efficiency",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-3",
      "source": "sh_senior_leaders",
      "target": "cn_value_proposition",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-5",
      "source": "sh_senior_leaders",
      "target": "cn_change_impact",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-6",
      "source": "sh_senior_leaders",
      "target": "cn_alignment",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-11",
      "source": "sh_senior_leaders",
      "target": "cn_security",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-13",
      "source": "sh_senior_leaders",
      "target": "cn_customer_intimacy",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-0-15",
      "source": "sh_senior_leaders",
      "target": "cn_business_continuity",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-0",
      "source": "sh_portfolio_managers",
      "target": "cn_agility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-1",
      "source": "sh_portfolio_managers",
      "target": "cn_efficiency",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-3",
      "source": "sh_portfolio_managers",
      "target": "cn_value_proposition",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-5",
      "source": "sh_portfolio_managers",
      "target": "cn_change_impact",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-6",
      "source": "sh_portfolio_managers",
      "target": "cn_alignment",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-7",
      "source": "sh_portfolio_managers",
      "target": "cn_feasibility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-12",
      "source": "sh_portfolio_managers",
      "target": "cn_confidence",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-13",
      "source": "sh_portfolio_managers",
      "target": "cn_customer_intimacy",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-14",
      "source": "sh_portfolio_managers",
      "target": "cn_scalability",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-1-15",
      "source": "sh_portfolio_managers",
      "target": "cn_business_continuity",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-0",
      "source": "sh_business_requirements_owners",
      "target": "cn_agility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-1",
      "source": "sh_business_requirements_owners",
      "target": "cn_efficiency",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-3",
      "source": "sh_business_requirements_owners",
      "target": "cn_value_proposition",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-5",
      "source": "sh_business_requirements_owners",
      "target": "cn_change_impact",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-10",
      "source": "sh_business_requirements_owners",
      "target": "cn_specification",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-11",
      "source": "sh_business_requirements_owners",
      "target": "cn_security",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-12",
      "source": "sh_business_requirements_owners",
      "target": "cn_confidence",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-2-13",
      "source": "sh_business_requirements_owners",
      "target": "cn_customer_intimacy",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-3-5",
      "source": "sh_implementers",
      "target": "cn_change_impact",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-3-7",
      "source": "sh_implementers",
      "target": "cn_feasibility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-3-9",
      "source": "sh_implementers",
      "target": "cn_control",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-3-10",
      "source": "sh_implementers",
      "target": "cn_specification",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-3-12",
      "source": "sh_implementers",
      "target": "cn_confidence",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-3-14",
      "source": "sh_implementers",
      "target": "cn_scalability",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-5",
      "source": "sh_risk_owners",
      "target": "cn_change_impact",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-7",
      "source": "sh_risk_owners",
      "target": "cn_feasibility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-8",
      "source": "sh_risk_owners",
      "target": "cn_dependability",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-10",
      "source": "sh_risk_owners",
      "target": "cn_specification",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-11",
      "source": "sh_risk_owners",
      "target": "cn_security",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-12",
      "source": "sh_risk_owners",
      "target": "cn_confidence",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-4-14",
      "source": "sh_risk_owners",
      "target": "cn_scalability",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-0",
      "source": "sh_business_partner",
      "target": "cn_agility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-1",
      "source": "sh_business_partner",
      "target": "cn_efficiency",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-5",
      "source": "sh_business_partner",
      "target": "cn_change_impact",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-7",
      "source": "sh_business_partner",
      "target": "cn_feasibility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-10",
      "source": "sh_business_partner",
      "target": "cn_specification",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-11",
      "source": "sh_business_partner",
      "target": "cn_security",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-5-12",
      "source": "sh_business_partner",
      "target": "cn_confidence",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-6-0",
      "source": "sh_customer",
      "target": "cn_agility",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-6-3",
      "source": "sh_customer",
      "target": "cn_value_proposition",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-6-11",
      "source": "sh_customer",
      "target": "cn_security",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-6-12",
      "source": "sh_customer",
      "target": "cn_confidence",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-6-13",
      "source": "sh_customer",
      "target": "cn_customer_intimacy",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "responsibility-6-15",
      "source": "sh_customer",
      "target": "cn_business_continuity",
      "type": "g186:responsibility",
      "label": "X：来源表已标注对应职责（非RACI）",
      "attributes": {
        "meaning": "X：来源表已标注对应职责（非RACI）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "entity_types": {},
    "relationship_types": {
      "g186:responsibility": {
        "source_types": [
          "g186:concern",
          "g186:stakeholder"
        ],
        "target_types": [
          "g186:concern",
          "g186:stakeholder"
        ],
        "meaning": "显式包含或职责映射，不表示流程或批准"
      }
    }
  },
  "view": {
    "id": "v-portfolio-stakeholder-concern-matrix",
    "artifact_id": "portfolio-stakeholder-concern-matrix",
    "profile_id": "portfolio-stakeholder-concern-matrix",
    "title": "组合利益相关者×关注点矩阵／来源结构专用示例",
    "entity_ids": [
      "sh_senior_leaders",
      "sh_portfolio_managers",
      "sh_business_requirements_owners",
      "sh_implementers",
      "sh_risk_owners",
      "sh_business_partner",
      "sh_customer",
      "cn_agility",
      "cn_efficiency",
      "cn_value",
      "cn_value_proposition",
      "cn_change_cost",
      "cn_change_impact",
      "cn_alignment",
      "cn_feasibility",
      "cn_dependability",
      "cn_control",
      "cn_specification",
      "cn_security",
      "cn_confidence",
      "cn_customer_intimacy",
      "cn_scalability",
      "cn_business_continuity"
    ],
    "relationship_ids": [
      "responsibility-0-0",
      "responsibility-0-1",
      "responsibility-0-3",
      "responsibility-0-5",
      "responsibility-0-6",
      "responsibility-0-11",
      "responsibility-0-13",
      "responsibility-0-15",
      "responsibility-1-0",
      "responsibility-1-1",
      "responsibility-1-3",
      "responsibility-1-5",
      "responsibility-1-6",
      "responsibility-1-7",
      "responsibility-1-12",
      "responsibility-1-13",
      "responsibility-1-14",
      "responsibility-1-15",
      "responsibility-2-0",
      "responsibility-2-1",
      "responsibility-2-3",
      "responsibility-2-5",
      "responsibility-2-10",
      "responsibility-2-11",
      "responsibility-2-12",
      "responsibility-2-13",
      "responsibility-3-5",
      "responsibility-3-7",
      "responsibility-3-9",
      "responsibility-3-10",
      "responsibility-3-12",
      "responsibility-3-14",
      "responsibility-4-5",
      "responsibility-4-7",
      "responsibility-4-8",
      "responsibility-4-10",
      "responsibility-4-11",
      "responsibility-4-12",
      "responsibility-4-14",
      "responsibility-5-0",
      "responsibility-5-1",
      "responsibility-5-5",
      "responsibility-5-7",
      "responsibility-5-10",
      "responsibility-5-11",
      "responsibility-5-12",
      "responsibility-6-0",
      "responsibility-6-3",
      "responsibility-6-11",
      "responsibility-6-12",
      "responsibility-6-13",
      "responsibility-6-15"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "X=已标注职责；空白=来源表未标注，不能据此断言无关注；非RACI，仅适用于组合目的。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact portfolio-stakeholder-concern-matrix --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
