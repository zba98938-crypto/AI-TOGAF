# 过渡架构模型

ID：`transition-architecture-model`。主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G248 §2；图2-2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

变革中间状态是否可运营且衔接目标？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 变革中间状态是否可运营且衔接目标？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- state_id
- operating_conditions
- work_packages

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：transition, transition_architecture, work_package。

```json
{
  "transition": [
    "definition",
    "operating_conditions"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "state_id": {
    "meaning": "具体架构状态的稳定标识",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "operating_conditions": {
    "meaning": "可运营状态的明确条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "work_packages": {
    "meaning": "实现该状态的工作包",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "dependencies": {
    "meaning": "实现及运行依赖",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "controls": {
    "meaning": "必须持续有效的控制",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rollback": {
    "meaning": "回退条件与方案",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `implements_transition` | work_package → transition | 工作包实现可运营过渡状态 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `depends_on` | software_module,work_package → software_module,work_package | 对象依赖目标作为前置 |

## 分析步骤

1. 命名基线过渡目标
2. 描述每个状态的运营条件
3. 关联工作包及实现
4. 检查依赖控制数据一致性和回退

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 过渡架构不是仅有交付日期的里程碑
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 过渡架构不是仅有交付日期的里程碑


## 视图和交付物

- [过渡架构模型](../profiles/transition-architecture-model-default.md)
- [过渡架构与工作包追溯](../profiles/transition-building-block-trace.md)

- [architecture-roadmaps](../deliverables/architecture-roadmaps.md)
- [solution-building-blocks](../deliverables/solution-building-blocks.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「过渡架构模型」给出：过渡架构不是仅有交付日期的里程碑",
    "expected": "transition-operability-gap",
    "why": "过渡架构不是仅有交付日期的里程碑"
  },
  "modification_example": {
    "change": "在「过渡架构模型」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "transition-architecture-model-default-state0",
      "type": "transition",
      "name": "基线：旧平台",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 0
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-state1",
      "type": "transition",
      "name": "过渡1：只读副本",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-state2",
      "type": "transition",
      "name": "过渡2：分批写入",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-state3",
      "type": "transition",
      "name": "目标：统一履约",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 3
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-wp",
      "type": "work_package",
      "name": "接口及对账工作包",
      "attributes": {
        "definition": "实现第一过渡的候选工作包"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "transition-architecture-model-default-evolve1",
      "type": "traces_to",
      "source": "transition-architecture-model-default-state0",
      "target": "transition-architecture-model-default-state1",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-evolve2",
      "type": "traces_to",
      "source": "transition-architecture-model-default-state1",
      "target": "transition-architecture-model-default-state2",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-evolve3",
      "type": "traces_to",
      "source": "transition-architecture-model-default-state2",
      "target": "transition-architecture-model-default-state3",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-impl",
      "type": "implements_transition",
      "source": "transition-architecture-model-default-wp",
      "target": "transition-architecture-model-default-state1",
      "label": "工作包实现可运营过渡",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-transition-architecture-model-default",
    "artifact_id": "transition-architecture-model",
    "profile_id": "transition-architecture-model-default",
    "title": "过渡架构模型／虚构案例",
    "entity_ids": [
      "transition-architecture-model-default-state0",
      "transition-architecture-model-default-state1",
      "transition-architecture-model-default-state2",
      "transition-architecture-model-default-state3",
      "transition-architecture-model-default-wp"
    ],
    "relationship_ids": [
      "transition-architecture-model-default-evolve1",
      "transition-architecture-model-default-evolve2",
      "transition-architecture-model-default-evolve3",
      "transition-architecture-model-default-impl"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact transition-architecture-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
