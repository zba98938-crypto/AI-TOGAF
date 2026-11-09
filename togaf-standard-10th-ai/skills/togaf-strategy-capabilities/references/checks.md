# togaf-strategy-capabilities 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（3 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `capability-instance-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：capability, capability_instance |
| `balanced-scorecard` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：goal, outcome |
| `smart-objective-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:goal, guide:smart-objective |

## 需人工判（15 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `capability-instance-model` | 同一能力的多个实例不等于多个新能力或子能力 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-instance-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-instance-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-instance-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `balanced-scorecard` | 目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `balanced-scorecard` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `balanced-scorecard` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `balanced-scorecard` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `smart-objective-assessment` | 13类目标是示例类别，不是封闭清单 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `smart-objective-assessment` | SMART只检查结构，现实性与数值合理性由责任人判断 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `smart-objective-assessment` | 目的须追溯到组织业务目标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-decomposition-method` | 流程步骤不作为子能力 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `smart-objective-review` | 13类目标是示例类别，不是封闭清单 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `smart-objective-review` | SMART只检查结构，现实性与数值合理性由责任人判断 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `smart-objective-review` | 目的须追溯到组织业务目标 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（6 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `capability-instance-model`：同一能力的多个实例不等于多个新能力或子能力
- `balanced-scorecard`：目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链
- `smart-objective-assessment`：名称、来源表格和成功输出不等于业务结论已核实
- `smart-objective-assessment`：13类目标是示例类别，不是封闭清单
- `smart-objective-assessment`：SMART只检查结构，现实性与数值合理性由责任人判断
- `smart-objective-assessment`：目的须追溯到组织业务目标
