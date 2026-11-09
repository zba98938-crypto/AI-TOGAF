# 风险缓解计划

ID：`risk-mitigation-plan`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.6。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

如何把风险降至可接受水平？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 如何把风险降至可接受水平？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- risk
- action
- owner

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：risk_treatment。

```json
{
  "risk_treatment": [
    "risk",
    "action",
    "owner",
    "due_date",
    "control",
    "expected_residual"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "risk": {
    "meaning": "风险对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "action": {
    "meaning": "拟采取的具体行动",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "due_date": {
    "meaning": "行动计划完成日期",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "control": {
    "meaning": "控制措施引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "expected_residual": {
    "meaning": "预期剩余风险及假设",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 比较提高控制转移规避延迟补偿等选项
2. 评价新架构带来的风险
3. 安排责任与验证
4. 复评剩余风险

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 计划中的控制不能被写成已经有效运行
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 计划中的控制不能被写成已经有效运行


## 视图和交付物

- [风险缓解计划](../profiles/risk-mitigation-plan-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「风险缓解计划」给出：计划中的控制不能被写成已经有效运行",
    "expected": "missing-evidence",
    "why": "计划中的控制不能被写成已经有效运行"
  },
  "modification_example": {
    "change": "在「风险缓解计划」的范围内新增或修改一项，检查下游是否随之变化",
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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact risk-mitigation-plan --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
