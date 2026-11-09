# togaf-vision-scenarios 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（3 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `business-scenario-document` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：scenario |
| `stakeholder-influence-matrix` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：stakeholder |
| `business-scenario-checklist-record` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:scenario-checklist-stage |

## 需人工判（35 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `business-scenario-document` | 业务场景不能由单张用例图替代，也不能预设技术答案 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-document` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-document` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-document` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-document` | 业务场景各步骤清单和SMART目的分别记录，勾选完成不等于场景被接受 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 矩阵关联不等于流程控制顺序或 CRUD | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 每个规范条目可追溯只读原始记录与转换步骤 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 复合陈述不得丢失子句 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 每个痛点至少一个成果 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 矩阵关系没有未经原文授权的CRUD/顺序/责任编码 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 同ID复用、重名不同ID不合并 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-matrix` | 单一制品请求仍可输出本矩阵和最小必要追溯，不强制全套成果 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `stakeholder-influence-matrix` | 来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `stakeholder-influence-matrix` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `stakeholder-influence-matrix` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `stakeholder-influence-matrix` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-record` | 勾选项须有证据；不适用须有理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-record` | 工作坊条件项只在采用工作坊时适用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-record` | 一人可担任多个G176角色；角色数不等于人数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-record` | 清单完成不表示业务场景被接受 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-elicitation` | 前提未经检验时不能当业务事实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-elicitation` | 问题陈述为“如何做”或不可行动时须有追问记录，不直接转为需求 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-review` | 每个规范条目可追溯只读原始记录与转换步骤 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-review` | 复合陈述不得丢失子句 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-review` | 每个痛点至少一个成果 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-review` | 矩阵关系没有未经原文授权的CRUD/顺序/责任编码 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-review` | 同ID复用、重名不同ID不合并 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `scenario-traceability-review` | 单一制品请求仍可输出本矩阵和最小必要追溯，不强制全套成果 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-review` | 勾选项须有证据；不适用须有理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-review` | 工作坊条件项只在采用工作坊时适用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-review` | 一人可担任多个G176角色；角色数不等于人数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-scenario-checklist-review` | 清单完成不表示业务场景被接受 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（10 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `business-scenario-document`：业务场景不能由单张用例图替代，也不能预设技术答案
- `scenario-traceability-matrix`：6项总体任务、5个迭代步骤与3个阶段是不同分解
- `scenario-traceability-matrix`：矩阵有一条关联不代表实际控制流
- `scenario-traceability-matrix`：把全部流程和全部参与者自动连满会制造事实
- `stakeholder-influence-matrix`：来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权
- `business-scenario-checklist-record`：名称、来源表格和成功输出不等于业务结论已核实
- `business-scenario-checklist-record`：勾选项须有证据；不适用须有理由
- `business-scenario-checklist-record`：工作坊条件项只在采用工作坊时适用
- `business-scenario-checklist-record`：一人可担任多个G176角色；角色数不等于人数
- `business-scenario-checklist-record`：清单完成不表示业务场景被接受
