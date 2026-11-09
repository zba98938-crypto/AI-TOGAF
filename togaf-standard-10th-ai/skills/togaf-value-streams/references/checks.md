# togaf-value-streams 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（2 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `value-network` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：value_network_actor |
| `lean-value-stream` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：lean_process |

## 需人工判（9 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `value-network` | 价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-network` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-network` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-network` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `lean-value-stream` | 精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `lean-value-stream` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `lean-value-stream` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `lean-value-stream` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-stream-definition-method` | 价值链与价值流用途和结构不同 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（2 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `value-network`：价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值
- `lean-value-stream`：精益流程单元不是业务架构价值阶段，不能用相同能力交叉映射替代；无统一单位不计算活动比
