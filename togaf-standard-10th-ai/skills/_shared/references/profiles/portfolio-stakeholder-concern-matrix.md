# 组合利益相关者×关注点矩阵

`profile_id`: portfolio-stakeholder-concern-matrix；`artifact_id`: portfolio-stakeholder-concern-matrix；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/tabB-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "portfolio-stakeholder-concern-matrix",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G186/tabB-1",
  "source_topology": "stakeholder-concern-matrix",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "按显式关系与状态读取；来源解释不代表本地组织事实。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：g186:concern, g186:stakeholder。关系类型：g186:responsibility。

```json
{
  "entities": {
    "*": [
      "definition"
    ]
  },
  "relationships": {
    "*": [
      "meaning"
    ]
  }
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 按显式关系与状态读取；来源解释不代表本地组织事实。
- 折叠不等于空；选中不等于差异；不从布局推断语义。

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile portfolio-stakeholder-concern-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile portfolio-stakeholder-concern-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
