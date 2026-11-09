# 精益价值流

ID：`lean-value-stream`。主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G178/figA-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

识别信息物料流中的等待、返工和浪费

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 识别信息物料流中的等待、返工和浪费
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- function
- lead_time
- processing_time

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：actor, application, lean_process。

```json
{
  "lean_process": [
    "function",
    "lead_time",
    "processing_time",
    "complete_accurate",
    "unit",
    "queue"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "function": {
    "meaning": "参考功能或实际功能映射",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "lead_time": {
    "meaning": "在本工作产品范围中明确定义的 lead_time 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "processing_time": {
    "meaning": "在本工作产品范围中明确定义的 processing_time 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "complete_accurate": {
    "meaning": "在本工作产品范围中明确定义的 complete_accurate 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "unit": {
    "meaning": "度量单位",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "queue": {
    "meaning": "在本工作产品范围中明确定义的 queue 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `information_flow` | actor,application,lean_process → actor,application,lean_process | 精益图中的信息传递；与工作物料推进及流程先后独立 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `work_flow` | lean_process → lean_process | 工作或物料在精益流程间推进；推拉规则与队列需明示 |

## 分析步骤

1. 确定产品范围和时间边界
2. 记录信息流与工作流
3. 逐流程采集LT/PT与完整准确率
4. 统一时间单位和工作日口径
5. 分析瓶颈和改进机会

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比


## 视图和交付物

- [精益价值流](../profiles/lean-value-stream-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「精益价值流」给出：精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比",
    "expected": "missing-evidence",
    "why": "精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比"
  },
  "modification_example": {
    "change": "在「精益价值流」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact lean-value-stream --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
