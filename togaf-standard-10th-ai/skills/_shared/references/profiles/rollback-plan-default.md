# 回退计划

`profile_id`: rollback-plan-default；`artifact_id`: rollback-plan；主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G152 §5.7。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：rollback_step。关系类型：traces_to。

```json
{
  "entities": {
    "rollback_step": [
      "trigger",
      "decision_owner",
      "prerequisite",
      "data_recovery",
      "sequence",
      "verification"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 回退不是仅写恢复备份，应说明业务与数据恢复条件
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
      "id": "rollback-plan-default-step1",
      "type": "rollback_step",
      "name": "回退计划：准备",
      "attributes": {
        "trigger": "订单一致性校验失败时暂停切换",
        "decision_owner": "虚构发布经理",
        "prerequisite": "保留旧平台可写能力并完成对账",
        "data_recovery": "核对切换窗口内订单与付款记录后恢复",
        "sequence": "停止新写入→订单对账→恢复旧平台→验证订单履约",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
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
      "id": "rollback-plan-default-step2",
      "type": "rollback_step",
      "name": "回退计划：验证",
      "attributes": {
        "trigger": "订单一致性校验失败时暂停切换",
        "decision_owner": "虚构发布经理",
        "prerequisite": "保留旧平台可写能力并完成对账",
        "data_recovery": "核对切换窗口内订单与付款记录后恢复",
        "sequence": "停止新写入→订单对账→恢复旧平台→验证订单履约",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
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
      "id": "rollback-plan-default-dependency",
      "type": "traces_to",
      "source": "rollback-plan-default-step2",
      "target": "rollback-plan-default-step1",
      "label": "后项以准备结果为进入条件；工期是虚构演示",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-rollback-plan-default",
    "artifact_id": "rollback-plan",
    "profile_id": "rollback-plan-default",
    "title": "回退计划／虚构案例",
    "entity_ids": [
      "rollback-plan-default-step1",
      "rollback-plan-default-step2"
    ],
    "relationship_ids": [
      "rollback-plan-default-dependency"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile rollback-plan-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile rollback-plan-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
