# 架构项目资源与进度

ID：`architecture-project-schedule`。主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.2.6–3.2.7；G210 §3.3–3.3.8。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构工作在资源约束下怎样安排？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 架构工作在资源约束下怎样安排？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- duration
- resource
- predecessor

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：architecture_activity, guide:agile_sprint, guide:agile_activity, guide:dorp_gate, guide:agile_context。

```json
{
  "architecture_activity": [
    "duration",
    "resource",
    "predecessor",
    "start",
    "end",
    "milestone"
  ],
  "milestone": [
    "due_date",
    "exit_criteria",
    "owner",
    "dependency"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "duration": {
    "meaning": "活动持续时间及单位",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "resource": {
    "meaning": "所需资源",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "predecessor": {
    "meaning": "前置活动",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "start": {
    "meaning": "计划或实际开始时间",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "end": {
    "meaning": "计划或实际结束时间",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "milestone": {
    "meaning": "里程碑定义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `guide:agile_handoff` | guide:agile_activity,guide:agile_context → guide:agile_activity,guide:agile_context | 前冲刺成果经DORP评审移交后续冲刺，有方向 |
| `guide:agile_continues` | guide:agile_activity,guide:agile_context → guide:agile_activity,guide:agile_context | 同泳道下一冲刺的滚动延续，不等于一个ADM阶段 |
| `guide:agile_collaborates` | guide:agile_activity,guide:agile_context → guide:agile_activity,guide:agile_context | 同冲刺不同团队的对称协作、敏捷治理与支持；不是有向数据流 |
| `guide:agile_finalizes` | guide:agile_activity,guide:agile_context → guide:agile_activity,guide:agile_context | 仅EA模式形成最终产品架构后安排实施，本图不伪造实施任务 |

## 分析步骤

1. 确定活动依赖与估算依据
2. 比较资源可用量
3. 形成里程碑和滚动计划
4. 分析关键路径与缓冲

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 没有依赖和工期证据不能宣称算出关键路径
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 没有依赖和工期证据不能宣称算出关键路径


## 视图和交付物

- [架构项目资源与进度](../profiles/architecture-project-schedule-default.md)
- [企业架构开发敏捷冲刺协作图](../profiles/agile-ea-development.md)
- [解决方案协作冲刺协作图](../profiles/agile-solution-collaboration.md)
- [跨开发协作冲刺协作图](../profiles/agile-cross-development.md)
- [跨职能敏捷冲刺协作图](../profiles/agile-cross-functional.md)

- [statement-of-work](../deliverables/statement-of-work.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构项目资源与进度」给出：没有依赖和工期证据不能宣称算出关键路径",
    "expected": "missing-evidence",
    "why": "没有依赖和工期证据不能宣称算出关键路径"
  },
  "modification_example": {
    "change": "在「架构项目资源与进度」的范围内新增或修改一项，检查下游是否随之变化",
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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-project-schedule --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
