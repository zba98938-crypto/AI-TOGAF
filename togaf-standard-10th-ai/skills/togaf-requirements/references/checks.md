# togaf-requirements 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（2 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `bi-requirements-profile` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：analytics_requirement, guide:bi_requirement_provenance, ops:bi_usage, ops:functional_coverage |
| `architecture-backlog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:backlog_item, guide:sprint |

## 需人工判（27 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `bi-requirements-profile` | 未取得外部完整需求电子表格时不能声称覆盖其全部条目 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 本地16例不得标原文逐条需求 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 缺配套源时official_requirement_id保持unknown | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 不宣称完整需求数量或全集覆盖 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 来源冲突明确登记 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 参考方向不是目标或达标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 每指标有单位/时间/依据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 无ROI公式则不计算 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 数据民主化不放开机密数据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 源表ID全集覆盖且不重复 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 已见必须有具体实现/证据，计划不算已实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 不适用必须有范围理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 参考表行不是软件组件或独立制品 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 保留本地翻译不确定 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-requirements-profile` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog` | 业务优先级有证据；编号顺序不等同关系方向 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog` | 每个选中项能关联冲刺目标、估算依据和验收条件 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog` | 依赖无环；依赖可在冲刺内先完成或有既成证据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog` | 容量单位一致；未知不能计零 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog` | 未完成工作保留原ID并回流；历史冲刺记录不重写 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog-method` | 业务优先级有证据；编号顺序不等同关系方向 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog-method` | 每个选中项能关联冲刺目标、估算依据和验收条件 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog-method` | 依赖无环；依赖可在冲刺内先完成或有既成证据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog-method` | 容量单位一致；未知不能计零 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-backlog-method` | 未完成工作保留原ID并回流；历史冲刺记录不重写 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（5 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `bi-requirements-profile`：未取得外部完整需求电子表格时不能声称覆盖其全部条目
- `architecture-backlog`：不把速率当项目完成度
- `architecture-backlog`：不固定1–4周为所有组织规则
- `architecture-backlog`：业务待办与冲刺待办是同族两视图，不复制身份或双计制品
- `architecture-backlog`：本例优先级和人日是项目规则，不是TOGAF权重
