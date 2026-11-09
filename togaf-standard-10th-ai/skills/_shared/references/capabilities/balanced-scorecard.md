# 平衡计分卡目标与成果

ID：`balanced-scorecard`。主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G233/fig4-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

从四个视角识别可追溯目标与可度量成果以驱动能力改进

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 从四个视角识别可追溯目标与可度量成果以驱动能力改进
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- perspective
- definition
- metric

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：goal, outcome。

```json
{
  "goal": [
    "perspective",
    "definition"
  ],
  "outcome": [
    "perspective",
    "metric",
    "unit",
    "baseline",
    "target",
    "period"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "perspective": {
    "meaning": "在本工作产品范围中明确定义的 perspective 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "metric": {
    "meaning": "度量方法和计算定义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "unit": {
    "meaning": "度量单位",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "target": {
    "meaning": "期望结果或目标值",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "period": {
    "meaning": "分析期间",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "baseline": {
    "meaning": "比较基线及状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `realizes` | function,outcome,sbb,technology → abb,business_service,goal,technology_service | 实现规定的服务、构建块或目标；成果到目标表示达成，不表示目标导致成果。 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 分别提出客户学习成长内部流程财务目标
2. 定义成果度量基线目标单位与期间
3. 用成果实现目标关系连接
4. 继续追溯能力实例
5. 检验指标可验证性

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链


## 视图和交付物

- [平衡计分卡目标与成果](../profiles/balanced-scorecard-default.md)

- [capability-assessment](../deliverables/capability-assessment.md)
- [architecture-roadmaps](../deliverables/architecture-roadmaps.md)
- [business-goals-objectives](../deliverables/business-goals-objectives.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「平衡计分卡目标与成果」给出：目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链",
    "expected": "missing-evidence",
    "why": "目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链"
  },
  "modification_example": {
    "change": "在「平衡计分卡目标与成果」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "balanced-scorecard-default-goal0",
      "type": "goal",
      "name": "提升重复购买",
      "attributes": {
        "perspective": "客户",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome0",
      "type": "outcome",
      "name": "重复购买比例提高",
      "attributes": {
        "perspective": "客户",
        "metric": "期间重复购买客户占比",
        "unit": "%",
        "baseline": 20,
        "target": 22,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-goal1",
      "type": "goal",
      "name": "提升人员稳定性",
      "attributes": {
        "perspective": "学习与成长",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome1",
      "type": "outcome",
      "name": "员工流失率降低",
      "attributes": {
        "perspective": "学习与成长",
        "metric": "期间员工离职人数除期初人数",
        "unit": "%",
        "baseline": 10,
        "target": 8.5,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-goal2",
      "type": "goal",
      "name": "提高订单履约效率",
      "attributes": {
        "perspective": "内部流程",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome2",
      "type": "outcome",
      "name": "平均确认时间下降",
      "attributes": {
        "perspective": "内部流程",
        "metric": "确认订单耗时算术平均",
        "unit": "分钟",
        "baseline": 20,
        "target": 10,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-goal3",
      "type": "goal",
      "name": "增加可持续销售",
      "attributes": {
        "perspective": "财务",
        "definition": "本例候选战略意图，需责任人确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-outcome3",
      "type": "outcome",
      "name": "销售额增长",
      "attributes": {
        "perspective": "财务",
        "metric": "同口径期间商品销售额",
        "unit": "万元",
        "baseline": 100,
        "target": 110,
        "period": "2026Q4 对2026Q3；虚构同口径期间"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "balanced-scorecard-default-realize0",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome0",
      "target": "balanced-scorecard-default-goal0",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-realize1",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome1",
      "target": "balanced-scorecard-default-goal1",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-realize2",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome2",
      "target": "balanced-scorecard-default-goal2",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "balanced-scorecard-default-realize3",
      "type": "realizes",
      "source": "balanced-scorecard-default-outcome3",
      "target": "balanced-scorecard-default-goal3",
      "label": "可度量成果实现目标；不是跨视角因果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-balanced-scorecard-default",
    "artifact_id": "balanced-scorecard",
    "profile_id": "balanced-scorecard-default",
    "title": "平衡计分卡目标与成果／虚构案例",
    "entity_ids": [
      "balanced-scorecard-default-goal0",
      "balanced-scorecard-default-outcome0",
      "balanced-scorecard-default-goal1",
      "balanced-scorecard-default-outcome1",
      "balanced-scorecard-default-goal2",
      "balanced-scorecard-default-outcome2",
      "balanced-scorecard-default-goal3",
      "balanced-scorecard-default-outcome3"
    ],
    "relationship_ids": [
      "balanced-scorecard-default-realize0",
      "balanced-scorecard-default-realize1",
      "balanced-scorecard-default-realize2",
      "balanced-scorecard-default-realize3"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact balanced-scorecard --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
