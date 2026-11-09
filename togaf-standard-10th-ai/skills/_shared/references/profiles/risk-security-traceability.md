# 风险与安全追溯模型

`profile_id`: risk-security-traceability；`artifact_id`: business-risk-register；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152/fig5-2。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G152/fig5-2",
  "layout_notes": "保留威胁、损失、风险、控制目标、需求、实施和资产追溯",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/risk-security-traceability.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, control, control_objective, loss_event, risk, risk_asset, security_requirement, threat_event, vulnerability。关系类型：causes_loss, derived_from, exploits, impacts_asset, implements_control, requires_control, risk_has_control。

```json
{
  "entities": {
    "risk": [
      "likelihood",
      "impact",
      "owner",
      "treatment"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 保留威胁、损失、风险、控制目标、需求、实施和资产追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "risk-security-traceability-threat",
      "type": "threat_event",
      "name": "未授权修改订单",
      "attributes": {
        "definition": "假设攻击者利用管理访问薄弱点"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-vulnerability",
      "type": "vulnerability",
      "name": "高权限操作缺少复核",
      "attributes": {
        "definition": "候选脆弱性，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-loss",
      "type": "loss_event",
      "name": "订单状态失真导致履约失败",
      "attributes": {
        "definition": "可能的业务损失场景"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-asset",
      "type": "risk_asset",
      "name": "订单完整性",
      "attributes": {
        "definition": "与履约承诺有关的业务资产"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-risk",
      "type": "risk",
      "name": "订单被篡改风险",
      "attributes": {
        "likelihood": "可能：虚构定性假设",
        "impact": "高履约影响：需责任方校准",
        "owner": "订单业务负责人",
        "treatment": "部署访问控制并验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-objective",
      "type": "control_objective",
      "name": "高权限操作可追责",
      "attributes": {
        "definition": "异常订单修改可被预防或检测"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-requirement",
      "type": "security_requirement",
      "name": "订单修改必须通过授权并留审计证据",
      "attributes": {
        "definition": "候选可验证安全需求"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-control",
      "type": "control",
      "name": "权限复核与操作审计",
      "attributes": {
        "definition": "候选控制，效果未证实"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-app",
      "type": "application",
      "name": "订单应用",
      "attributes": {
        "definition": "候选控制实现载体"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "risk-security-traceability-exploit",
      "type": "exploits",
      "source": "risk-security-traceability-threat",
      "target": "risk-security-traceability-vulnerability",
      "label": "威胁利用脆弱性",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-loss-cause",
      "type": "causes_loss",
      "source": "risk-security-traceability-threat",
      "target": "risk-security-traceability-loss",
      "label": "威胁事件可能造成损失",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-asset-impact",
      "type": "impacts_asset",
      "source": "risk-security-traceability-loss",
      "target": "risk-security-traceability-asset",
      "label": "损失影响订单业务资产",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-risk-asset",
      "type": "impacts_asset",
      "source": "risk-security-traceability-risk",
      "target": "risk-security-traceability-asset",
      "label": "风险作用于该资产",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-derive",
      "type": "derived_from",
      "source": "risk-security-traceability-requirement",
      "target": "risk-security-traceability-objective",
      "label": "需求由控制目标导出",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-require",
      "type": "requires_control",
      "source": "risk-security-traceability-requirement",
      "target": "risk-security-traceability-control",
      "label": "需求由候选控制实现",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-mitigation",
      "type": "risk_has_control",
      "source": "risk-security-traceability-risk",
      "target": "risk-security-traceability-control",
      "label": "风险关联候选缓解控制",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-security-traceability-implementation",
      "type": "implements_control",
      "source": "risk-security-traceability-app",
      "target": "risk-security-traceability-control",
      "label": "应用计划实现控制，未表示效果已验证",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-risk-security-traceability",
    "artifact_id": "business-risk-register",
    "profile_id": "risk-security-traceability",
    "title": "风险与安全追溯模型／虚构案例",
    "entity_ids": [
      "risk-security-traceability-threat",
      "risk-security-traceability-vulnerability",
      "risk-security-traceability-loss",
      "risk-security-traceability-asset",
      "risk-security-traceability-risk",
      "risk-security-traceability-objective",
      "risk-security-traceability-requirement",
      "risk-security-traceability-control",
      "risk-security-traceability-app"
    ],
    "relationship_ids": [
      "risk-security-traceability-exploit",
      "risk-security-traceability-loss-cause",
      "risk-security-traceability-asset-impact",
      "risk-security-traceability-risk-asset",
      "risk-security-traceability-derive",
      "risk-security-traceability-require",
      "risk-security-traceability-mitigation",
      "risk-security-traceability-implementation"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile risk-security-traceability --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile risk-security-traceability --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
