# 访谈收集切换为工作坊后的适用清单

所有业务材料、人员、目标和授权均为明示虚构；执行结果只覆盖下述情景。

方法：`business-scenario-checklist-review`。来源：G176 §10、§11.3。
可复用材料：[四类场景JSON](../method-case-materials/business-scenario-checklist-review.json)。

## 决策与原始业务资料

原计划使用访谈，改成工作坊后是否还能沿用全部清单已处理的结论？

|证据 ID|原始业务材料|
|---|---|
|INTERVIEWS|虚构试点记录包含问题清单、公开数据预处理、场景草稿、参与者、匿名措施和访谈收集材料；本轮只审收集阶段，未采用工作坊。|

充分输入的精确结构如下；数值与ID来自本案例材料，不从执行结果反推。

```json
{
  "source_ids": [
    "INTERVIEWS"
  ],
  "stages": [
    "gather"
  ],
  "uses_workshop": false,
  "responses": {
    "gather-01": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-02": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-03": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-04": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-05": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-06": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-07": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-08": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-09": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    },
    "gather-09c": {
      "status": "done",
      "evidence": [
        "INTERVIEWS"
      ]
    }
  },
  "role_assignments": []
}
```

## 来源规则与项目规则

1. **来源规则**：G176 §11.3允许访谈等收集方式，If workshop之后的准备项有条件适用；原文空白复选框不是项目完成声明。
2. **项目规则**：本案例采用明确的来源ID、结构字段和有界状态；执行器检查可观察契约，业务充分性另由推理审阅说明。
3. **项目规则**：变化场景只改变材料中列出的事实；未变字段不被重新编造，所有批准与实际运行效果均保持未授予。

## 转换与推理

1. 收集阶段范围明确，不自动声称规划、文档和评审阶段完成。
2. 访谈是收集方式any-of的一项，以访谈记录支撑，不要求工作坊同时完成。
3. 未采用工作坊时条件项为condition-not-met；改用工作坊使其重新适用。
4. done缺证据须保留missing-evidence；状态字段自身不能构成完成证明。

## 输出与追溯

下列预期在执行前由业务材料独立编写；实际执行只对这些明确字段作比较。

```json
{
  "open_item_ids": [],
  "gap_reasons": [],
  "condition_not_met_count": 6
}
```

访谈收集范围内各项有模拟记录，工作坊六条件项不适用。

机械可复核字段、缺口和引用；业务结论不由计算器输出自动批准。完整输入、预期与实际结果见本轮方法证据目录。

## 修改演练

本次替换的业务字段如下；需按新事实重评。

- `uses_workshop`：false → true

改成工作坊后六项变为未审，原访谈记录不能支持工作坊准备。

变化后需重新执行原方法；原结论只保留到未改变的事实范围。

```json
{
  "open_item_ids": [
    "gather-w1",
    "gather-w2",
    "gather-w3",
    "gather-w4",
    "gather-w5",
    "gather-w6"
  ],
  "condition_not_met_count": 0
}
```

## 反例与输入不足

- 缺输入：删除公开数据收集的证据，不能由done标签填补。 预期 `missing-evidence`，这是结果中的缺口原因，不是伪装为抛异常。
- 结构反例：passed不是清单合法状态，拒绝泛化测试状态。 预期 `BSC-002`，此项由执行器实际拒绝。

缺输入的预期结果：

```json
{
  "gap_reasons": [
    "missing-evidence"
  ]
}
```

## 评审记录

- 已将本案来源规则与明确的项目约定分开。
- 已核对充分、缺输入、变化及结构反例四类材料的实际结果。
- 已核对缺输入没有被补为通过、零值或真实授权。
- 收集阶段范围明确，不自动声称规划、文档和评审阶段完成。
- 访谈是收集方式any-of的一项，以访谈记录支撑，不要求工作坊同时完成。
- 未采用工作坊时条件项为condition-not-met；改用工作坊使其重新适用。
- done缺证据须保留missing-evidence；状态字段自身不能构成完成证明。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
