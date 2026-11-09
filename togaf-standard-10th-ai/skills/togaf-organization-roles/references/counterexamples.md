# togaf-organization-roles 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `architecture-skill-matrix` | 对「架构技能／角色矩阵」给出：G249 四级熟练度不等于组织成熟度，参考等级可以裁剪 | `missing-evidence` | G249 四级熟练度不等于组织成熟度，参考等级可以裁剪 | — |
| `architecture-development-plan` | 对「架构人员发展计划」给出：参加培训不自动提升为专家等级 | `missing-evidence` | 参加培训不自动提升为专家等级 | — |
| `sustainability-education-plan` | 仅20名ICT人员被标全员覆盖 | `all-staff-coverage-gap` |  | — |
| `architecture-role-catalog` | 角色关系引用不存在的角色 | `ROLE-REL` | ROLE-REL [REL-BROKEN]: Relationship target must be another declared role | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `architecture-skill-matrix` | 在「架构技能／角色矩阵」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `architecture-development-plan` | 在「架构人员发展计划」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `sustainability-education-plan` | 采购4人完成报告识别和合同练习，但全员理解验证仍未完成 | 采购能力证据更新，不能把全员状态标完成 |
| `architecture-role-catalog` | 把首席架构师满意度KPI改为企业批准目标4/5并附证据 | 分析结果变化：新增缺口KPI-CH-1:adopted_by；关闭缺口KPI-CH-1:target |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `architecture-role-skill-assessment` | 执行「角色技能差距评估」时跳过或误做：熟练度、团队容量和组织成熟度分开 | `missing-evidence` | 熟练度、团队容量和组织成熟度分开 | — |
| `architecture-role-catalog-review` | 角色关系引用不存在的角色 | `ROLE-REL` | ROLE-REL [REL-BROKEN]: Relationship target must be another declared role | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
