# 架构项目资源与进度

`profile_id`: architecture-project-schedule-default；`artifact_id`: architecture-project-schedule；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.2.6–3.2.7。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：architecture_activity。关系类型：traces_to。

```json
{
  "entities": {
    "architecture_activity": [
      "duration",
      "resource",
      "predecessor",
      "start",
      "end",
      "milestone"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 没有依赖和工期证据不能宣称算出关键路径
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
      "id": "architecture-project-schedule-default-step1",
      "type": "architecture_activity",
      "name": "架构项目资源与进度：准备",
      "attributes": {
        "duration": 2,
        "resource": "虚构订单案例中需验证的所需资源",
        "predecessor": "业务与数据定义评审",
        "start": "2026-11-02",
        "end": "2026-11-13",
        "milestone": "完成候选接口和控制评审",
        "order": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-project-schedule-default-step2",
      "type": "architecture_activity",
      "name": "架构项目资源与进度：验证",
      "attributes": {
        "duration": 2,
        "resource": "虚构订单案例中需验证的所需资源",
        "predecessor": "业务与数据定义评审",
        "start": "2026-11-16",
        "end": "2026-11-27",
        "milestone": "完成候选接口和控制评审",
        "order": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "architecture-project-schedule-default-dependency",
      "type": "traces_to",
      "source": "architecture-project-schedule-default-step2",
      "target": "architecture-project-schedule-default-step1",
      "label": "后项以准备结果为进入条件；工期是虚构演示",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-architecture-project-schedule-default",
    "artifact_id": "architecture-project-schedule",
    "profile_id": "architecture-project-schedule-default",
    "title": "架构项目资源与进度／虚构案例",
    "entity_ids": [
      "architecture-project-schedule-default-step1",
      "architecture-project-schedule-default-step2"
    ],
    "relationship_ids": [
      "architecture-project-schedule-default-dependency"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-project-schedule-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-project-schedule-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
