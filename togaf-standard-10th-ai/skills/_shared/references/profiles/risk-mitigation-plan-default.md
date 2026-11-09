# 风险缓解计划

`profile_id`: risk-mitigation-plan-default；`artifact_id`: risk-mitigation-plan；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.6。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：risk_treatment。关系类型：traces_to。

```json
{
  "entities": {
    "risk_treatment": [
      "risk",
      "action",
      "owner",
      "due_date",
      "control",
      "expected_residual"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 计划中的控制不能被写成已经有效运行
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

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
      "id": "risk-mitigation-plan-default-step1",
      "type": "risk_treatment",
      "name": "风险缓解计划：准备",
      "attributes": {
        "risk": "虚构订单案例中需验证的风险对象引用",
        "action": "补齐订单与发运追溯并演练回退",
        "owner": "虚构业务负责人",
        "due_date": "2026-12-15",
        "control": "访问认证和操作审计",
        "expected_residual": "待演练和控制验证后重新评价",
        "order": 1,
        "start": "2026-11-02",
        "end": "2026-11-13"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk-mitigation-plan-default-step2",
      "type": "risk_treatment",
      "name": "风险缓解计划：验证",
      "attributes": {
        "risk": "虚构订单案例中需验证的风险对象引用",
        "action": "补齐订单与发运追溯并演练回退",
        "owner": "虚构业务负责人",
        "due_date": "2026-12-15",
        "control": "访问认证和操作审计",
        "expected_residual": "待演练和控制验证后重新评价",
        "order": 2,
        "start": "2026-11-16",
        "end": "2026-11-27"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "risk-mitigation-plan-default-dependency",
      "type": "traces_to",
      "source": "risk-mitigation-plan-default-step2",
      "target": "risk-mitigation-plan-default-step1",
      "label": "后项以准备结果为进入条件；工期是虚构演示",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-risk-mitigation-plan-default",
    "artifact_id": "risk-mitigation-plan",
    "profile_id": "risk-mitigation-plan-default",
    "title": "风险缓解计划／虚构案例",
    "entity_ids": [
      "risk-mitigation-plan-default-step1",
      "risk-mitigation-plan-default-step2"
    ],
    "relationship_ids": [
      "risk-mitigation-plan-default-dependency"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile risk-mitigation-plan-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile risk-mitigation-plan-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
