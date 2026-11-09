# togaf-vision-scenarios 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `business-scenario-document` | 对「业务场景文档」给出：业务场景不能由单张用例图替代，也不能预设技术答案 | `missing-evidence` | 业务场景不能由单张用例图替代，也不能预设技术答案 | — |
| `scenario-traceability-matrix` | 对「业务场景关联矩阵」给出：6项总体任务、5个迭代步骤与3个阶段是不同分解 | `missing-evidence` | 6项总体任务、5个迭代步骤与3个阶段是不同分解 | — |
| `stakeholder-influence-matrix` | 对「利益相关者影响力与影响程度矩阵」给出：来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权 | `missing-evidence` | 来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权 | — |
| `business-scenario-checklist-record` | 清单项状态写为passed | `BSC-002` | BSC-002 [plan-01]: status must be done, not-applicable or open | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `business-scenario-document` | 在「业务场景文档」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `scenario-traceability-matrix` | 在「业务场景关联矩阵」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `stakeholder-influence-matrix` | 在「利益相关者影响力与影响程度矩阵」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `business-scenario-checklist-record` | 删除规划阶段的角色分配 | 分析结果变化：新增缺口plan-01:role,plan-02:role,role:business-scenario-author,role:business-scenario-consultant,role:business-scenario-editor,role:project-manager |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `scenario-elicitation` | 执行「业务场景前提验证与归一化」时跳过或误做：前提未经检验时不能当业务事实 | `missing-evidence` | 前提未经检验时不能当业务事实 | — |
| `scenario-traceability-review` | 执行「业务场景关联矩阵」时跳过或误做：每个规范条目可追溯只读原始记录与转换步骤 | `dangling-reference` | 每个规范条目可追溯只读原始记录与转换步骤 | — |
| `business-scenario-checklist-review` | 清单项状态写为passed | `BSC-002` | BSC-002 [plan-01]: status must be done, not-applicable or open | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
