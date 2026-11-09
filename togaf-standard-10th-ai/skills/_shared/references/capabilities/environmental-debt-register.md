# 环境债务日志

ID：`environmental-debt-register`。主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242 §3.9.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些环境代价被推迟处理？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些环境代价被推迟处理？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- decision
- impact
- reason

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：environmental_debt。

```json
{
  "environmental_debt": [
    "decision",
    "impact",
    "reason",
    "owner",
    "remediation",
    "review_date"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decision": {
    "meaning": "决策结果、理由和状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "impact": {
    "meaning": "业务影响及其依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "reason": {
    "meaning": "接受或处置的理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "remediation": {
    "meaning": "消除债务的措施",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "review_date": {
    "meaning": "计划复评日期",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 识别设计运营中的环境债务
2. 记录接受理由与影响
3. 安排消除措施
4. 按证据复评

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 环境债务不是仅有碳排总量，责任和决策也需记录
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 环境债务不是仅有碳排总量，责任和决策也需记录


## 视图和交付物

- [环境债务日志](../profiles/environmental-debt-register-default.md)

- [change-request](../deliverables/change-request.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「环境债务日志」给出：环境债务不是仅有碳排总量，责任和决策也需记录",
    "expected": "missing-evidence",
    "why": "环境债务不是仅有碳排总量，责任和决策也需记录"
  },
  "modification_example": {
    "change": "在「环境债务日志」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "environmental-debt-register-default-record",
      "type": "environmental_debt",
      "name": "环境债务日志：订单范围记录",
      "attributes": {
        "decision": "虚构订单案例中需验证的决策结果、理由和状态",
        "impact": "高峰时段无法履约，影响当日发运承诺",
        "reason": "保障履约同时逐步消除重复处理",
        "owner": "虚构业务负责人",
        "remediation": "完成迁移后退役重复任务",
        "review_date": "2027-01-15"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-environmental-debt-register-default",
    "artifact_id": "environmental-debt-register",
    "profile_id": "environmental-debt-register-default",
    "title": "环境债务日志／虚构案例",
    "entity_ids": [
      "environmental-debt-register-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact environmental-debt-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
