# togaf-technology-architecture 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（3 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `microservice-technical-guidance` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：microservice_guideline, ops:msa_readiness, ops:msa_governance |
| `microservice-technical-guidance` | 声称治理决定或豁免已批准时具备范围内授权与决定证据 | `msa-authorization-evidence-gap` | `msa-authorization` | 模型含类型：ops:msa_governance |
| `interoperability-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：interoperability_issue, equipment |

## 需人工判（19 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `microservice-technical-guidance` | 外部实践补充必须标项目约定，不能冒充指南原文 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 六关注点保持独立 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 缺退休责任不得标全生命周期完整 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 未知OSIMM不填分数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 自治仍受企业护栏约束 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 待决豁免不能被采用为已批准 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 四种关系不得统一为泛化依赖 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 治理有执行/反馈过程 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 项目图关系不冒称源图核实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-technical-guidance` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `interoperability-assessment` | 网络连通不能证明语义和业务互操作 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `interoperability-assessment` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `interoperability-assessment` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `interoperability-assessment` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `soa-layered-reference` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `soa-layered-reference` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `soa-layered-reference` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（4 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `microservice-technical-guidance`：外部实践补充必须标项目约定，不能冒充指南原文
- `interoperability-assessment`：网络连通不能证明语义和业务互操作
- `soa-layered-reference`：登记来源或成功生成不表示来源等价
- `soa-layered-reference`：参考示例的固定结构不直接强制所有企业采用
