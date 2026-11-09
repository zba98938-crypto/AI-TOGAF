# 环境决策日志

ID：`environmental-decision-log`。主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G242 §3.8–4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

环境标准怎样进入架构决策？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 环境标准怎样进入架构决策？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- options
- environmental_criteria
- evidence

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：environmental_decision。

```json
{
  "environmental_decision": [
    "options",
    "environmental_criteria",
    "evidence",
    "tradeoff",
    "decision",
    "authority"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "options": {
    "meaning": "被比较的备选方案",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "environmental_criteria": {
    "meaning": "环境评价准则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "tradeoff": {
    "meaning": "环境与其他质量的权衡",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decision": {
    "meaning": "决策结果、理由和状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "authority": {
    "meaning": "决策或数据权威及授权范围",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 明确备选与评价边界
2. 比较环境及其他质量属性
3. 记录权衡和决策依据
4. 追溯执行与复评

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 低环境影响方案是否采用仍取决于明确权衡，不能伪造批准
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 低环境影响方案是否采用仍取决于明确权衡，不能伪造批准


## 视图和交付物

- [环境决策日志](../profiles/environmental-decision-log-default.md)
- [数字节制文化四维图](../profiles/sustainability-culture-quadrant.md)

- [compliance-assessment](../deliverables/compliance-assessment.md)
- [business-principles](../deliverables/business-principles.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「环境决策日志」给出：低环境影响方案是否采用仍取决于明确权衡，不能伪造批准",
    "expected": "approval-without-evidence",
    "why": "低环境影响方案是否采用仍取决于明确权衡，不能伪造批准"
  },
  "modification_example": {
    "change": "在「环境决策日志」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "environmental-decision-log-default-record",
      "type": "environmental_decision",
      "name": "环境决策日志：订单范围记录",
      "attributes": {
        "options": "虚构订单案例中需验证的被比较的备选方案",
        "environmental_criteria": "虚构订单案例中需验证的环境评价准则",
        "evidence": "虚构场景说明，非实测证据",
        "tradeoff": "虚构订单案例中需验证的环境与其他质量的权衡",
        "decision": "虚构订单案例中需验证的决策结果、理由和状态",
        "authority": "虚构订单案例中需验证的决策或数据权威及授权范围"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-environmental-decision-log-default",
    "artifact_id": "environmental-decision-log",
    "profile_id": "environmental-decision-log-default",
    "title": "环境决策日志／虚构案例",
    "entity_ids": [
      "environmental-decision-log-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact environmental-decision-log --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
