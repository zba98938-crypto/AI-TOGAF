# 精益价值流

`profile_id`: lean-value-stream-default；`artifact_id`: lean-value-stream；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G178/figA-3。

## 构图与定义状态

表示族：`lean-flow`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "bands": [
    "信息流",
    "工作流",
    "时间与质量指标"
  ]
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：actor, application, lean_process。关系类型：information_flow, work_flow。

```json
{
  "entities": {
    "lean_process": [
      "function",
      "lead_time",
      "processing_time",
      "complete_accurate",
      "unit",
      "queue"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比
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
      "id": "lean-value-stream-default-customer",
      "type": "actor",
      "name": "线上客户",
      "attributes": {
        "definition": "提交已确认订单并接收履约状态"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-system",
      "type": "application",
      "name": "订单应用",
      "attributes": {
        "definition": "向仓库传递受控订单并接收发运结果"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-confirm",
      "type": "lean_process",
      "name": "核对订单",
      "attributes": {
        "function": "虚构履约团队",
        "lead_time": 480,
        "processing_time": 10,
        "complete_accurate": 0.95,
        "unit": "分钟",
        "queue": 12,
        "working_minutes_per_day": 480,
        "metric_evidence": "虚构示例，非实测"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-pick",
      "type": "lean_process",
      "name": "拣配商品",
      "attributes": {
        "function": "虚构履约团队",
        "lead_time": 960,
        "processing_time": 30,
        "complete_accurate": 0.98,
        "unit": "分钟",
        "queue": 35,
        "working_minutes_per_day": 480,
        "metric_evidence": "虚构示例，非实测"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-ship",
      "type": "lean_process",
      "name": "交接发运",
      "attributes": {
        "function": "虚构履约团队",
        "lead_time": 480,
        "processing_time": 15,
        "complete_accurate": 0.99,
        "unit": "分钟",
        "queue": 8,
        "working_minutes_per_day": 480,
        "metric_evidence": "虚构示例，非实测"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "lean-value-stream-default-submit",
      "type": "information_flow",
      "source": "lean-value-stream-default-customer",
      "target": "lean-value-stream-default-system",
      "label": "确认的购买需求",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-schedule",
      "type": "information_flow",
      "source": "lean-value-stream-default-system",
      "target": "lean-value-stream-default-confirm",
      "label": "经校验的订单信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-result",
      "type": "information_flow",
      "source": "lean-value-stream-default-ship",
      "target": "lean-value-stream-default-system",
      "label": "已交接商品及发运标识",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-notify",
      "type": "information_flow",
      "source": "lean-value-stream-default-system",
      "target": "lean-value-stream-default-customer",
      "label": "可追踪发运状态",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lean-value-stream-default-work0",
      "type": "work_flow",
      "source": "lean-value-stream-default-confirm",
      "target": "lean-value-stream-default-pick",
      "label": "推式工作流；队列记录在下游流程",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "queue_rule": "待处理工作项数，不是人员数"
      }
    },
    {
      "id": "lean-value-stream-default-work1",
      "type": "work_flow",
      "source": "lean-value-stream-default-pick",
      "target": "lean-value-stream-default-ship",
      "label": "推式工作流；队列记录在下游流程",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "queue_rule": "待处理工作项数，不是人员数"
      }
    }
  ],
  "view": {
    "id": "v-lean-value-stream-default",
    "artifact_id": "lean-value-stream",
    "profile_id": "lean-value-stream-default",
    "title": "精益价值流／虚构案例",
    "entity_ids": [
      "lean-value-stream-default-customer",
      "lean-value-stream-default-system",
      "lean-value-stream-default-confirm",
      "lean-value-stream-default-pick",
      "lean-value-stream-default-ship"
    ],
    "relationship_ids": [
      "lean-value-stream-default-submit",
      "lean-value-stream-default-schedule",
      "lean-value-stream-default-result",
      "lean-value-stream-default-notify",
      "lean-value-stream-default-work0",
      "lean-value-stream-default-work1"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile lean-value-stream-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile lean-value-stream-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
