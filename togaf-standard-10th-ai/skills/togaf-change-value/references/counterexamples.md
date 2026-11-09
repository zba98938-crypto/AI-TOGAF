# togaf-change-value 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `environmental-is-assessment` | 对「信息系统年度环境评估」给出：Scope2转移到Scope3并不自动等于减排 | `missing-evidence` | Scope2转移到Scope3并不自动等于减排 | — |
| `environmental-debt-register` | 对「环境债务日志」给出：环境债务不是仅有碳排总量，责任和决策也需记录 | `missing-evidence` | 环境债务不是仅有碳排总量，责任和决策也需记录 | — |
| `dorp-record` | 对「冲刺DORP记录」给出：DORP不是只写会议纪要或四个空标题 | `empty-view` | DORP不是只写会议纪要或四个空标题 | — |
| `technical-debt-register` | 对「技术与架构债登记」给出：不是所有债务都必须EA处理 | `missing-evidence` | 不是所有债务都必须EA处理 | — |
| `sustainability-dual-entry-analysis` | 基础设施优化无任何业务用途回溯 | `dual-entry-trace-gap` |  | — |
| `shared-carbon-factor-catalog` | 因子缺单位/期间/来源或把制造kgCO2e/台当年度值 | `carbon-data-metadata-gap` | carbon-data-metadata-gap或boundary-unit-conflict | carbon-data-metadata-gap或boundary-unit-conflict |
| `incident-architecture-adjustment` | 需求变更引用不存在的目标 | `IAA-003` | IAA-003 [RC-1]: Requirement change must name an affected objective | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `environmental-is-assessment` | 在「信息系统年度环境评估」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `environmental-debt-register` | 在「环境债务日志」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `dorp-record` | 在「冲刺DORP记录」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `technical-debt-register` | 在「技术与架构债登记」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `sustainability-dual-entry-analysis` | 发现SERVER-B夜间支持紧急作业 | 撤回夜间停机建议，标冲突并调整恢复/业务要求；培训优化不受此事实直接影响 |
| `shared-carbon-factor-catalog` | FC-03发布v2地点因子0.35，v1仍存在 | 新增版本、适用期与变更理由；既有v1引用不被覆盖 |
| `incident-architecture-adjustment` | 只保留变更目标一种选项 | 分析结果变化：新增缺口options:cancellation；option_kinds：["cancel-change", "cancel-objective", "change-target"]→["change-target"] |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `environment-lifecycle-accounting` | 执行「信息系统年度环境评估」时跳过或误做：单位、期间、组织边界和来源齐全 | `missing-evidence` | 单位、期间、组织边界和来源齐全 | — |
| `dorp-record-method` | 执行「冲刺DORP记录分析方法」时跳过或误做：Demo/Outcome/Retrospective/Planning四项分别存在 | `missing-evidence` | Demo/Outcome/Retrospective/Planning四项分别存在 | — |
| `technical-debt-register-method` | 执行「技术与架构债登记分析方法」时跳过或误做：原因、后果、范围和负责人明确 | `view-edge-outside` | 原因、后果、范围和负责人明确 | — |
| `incident-architecture-adjustment-review` | 需求变更引用不存在的目标 | `IAA-003` | IAA-003 [RC-1]: Requirement change must name an affected objective | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
