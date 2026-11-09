# EA 团队容量计划

`profile_id`: ea-team-capacity-plan-default；`artifact_id`: ea-team-capacity-plan；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §13。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ea_capacity。关系类型：traces_to。

```json
{
  "entities": {
    "ea_capacity": [
      "role",
      "skill",
      "demand",
      "availability",
      "allocation",
      "period"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 人数不等于可用容量，技能熟练度不等于工时
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
      "id": "ea-team-capacity-plan-default-step1",
      "type": "ea_capacity",
      "name": "EA 团队容量计划：准备",
      "attributes": {
        "role": "虚构安全架构师",
        "skill": "数据与应用架构追溯",
        "demand": 2,
        "availability": 2,
        "allocation": "按已声明的订单工作负载比例分摊",
        "period": "2026年第四季度",
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
      "id": "ea-team-capacity-plan-default-step2",
      "type": "ea_capacity",
      "name": "EA 团队容量计划：验证",
      "attributes": {
        "role": "虚构安全架构师",
        "skill": "数据与应用架构追溯",
        "demand": 2,
        "availability": 2,
        "allocation": "按已声明的订单工作负载比例分摊",
        "period": "2026年第四季度",
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
      "id": "ea-team-capacity-plan-default-dependency",
      "type": "traces_to",
      "source": "ea-team-capacity-plan-default-step2",
      "target": "ea-team-capacity-plan-default-step1",
      "label": "后项以准备结果为进入条件；工期是虚构演示",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-ea-team-capacity-plan-default",
    "artifact_id": "ea-team-capacity-plan",
    "profile_id": "ea-team-capacity-plan-default",
    "title": "EA 团队容量计划／虚构案例",
    "entity_ids": [
      "ea-team-capacity-plan-default-step1",
      "ea-team-capacity-plan-default-step2"
    ],
    "relationship_ids": [
      "ea-team-capacity-plan-default-dependency"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-team-capacity-plan-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-team-capacity-plan-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
