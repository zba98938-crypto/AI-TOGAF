# togaf-strategy-capabilities 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `capability-instance-model` | 对「能力实例组成模型」给出：同一能力的多个实例不等于多个新能力或子能力 | `missing-evidence` | 同一能力的多个实例不等于多个新能力或子能力 | — |
| `balanced-scorecard` | 对「平衡计分卡目标与成果」给出：目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链 | `missing-evidence` | 目标和成果不同；原图四视角间没有因果边，不能补造学习到财务的因果链 | — |
| `smart-objective-assessment` | 目的O-1追溯到不存在的目标 | `SMART-002` | SMART-002 [O-1]: Objective must trace to a registered goal | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `capability-instance-model` | 在「能力实例组成模型」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `balanced-scorecard` | 在「平衡计分卡目标与成果」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `smart-objective-assessment` | 为O-2补负责人、行动、现实性证据与截止日期 | 分析结果变化：关闭缺口O-2:actionable,O-2:baseline,O-2:realistic,O-2:time-bound |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `capability-decomposition-method` | 执行「能力定义与分解」时跳过或误做：流程步骤不作为子能力 | `missing-evidence` | 流程步骤不作为子能力 | — |
| `smart-objective-review` | 目的O-1追溯到不存在的目标 | `SMART-002` | SMART-002 [O-1]: Objective must trace to a registered goal | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
