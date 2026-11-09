# togaf-implementation-governance 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `security-audit-record` | 对「安全审计记录」给出：生成审计表不能证明渗透测试或控制运行已经完成 | `missing-evidence` | 生成审计表不能证明渗透测试或控制运行已经完成 | — |
| `environmental-decision-log` | 对「环境决策日志」给出：低环境影响方案是否采用仍取决于明确权衡，不能伪造批准 | `approval-without-evidence` | 低环境影响方案是否采用仍取决于明确权衡，不能伪造批准 | — |
| `change-profile-governance-checklist` | 对「变革画像治理检查清单」给出：名称、来源表格和成功输出不等于业务结论已核实 | `missing-evidence` | 名称、来源表格和成功输出不等于业务结论已核实 | — |
| `decision-delegation-register` | 对「决策授权与可逆性登记」给出：七级不是TOGAF成熟度评分 | `missing-evidence` | 七级不是TOGAF成熟度评分 | — |
| `sustainable-procurement-strategy` | 将“零碳”宣传单独作为完整足迹证据 | `procurement-transparency-gap` |  | — |
| `cloud-environmental-data-contract` | 设备子集10000大于同边界Scope3总9000；或要求把两种Scope2相加 | `scope3-subset-exceeds-total` | scope3-subset-exceeds-total或scope2-bases-not-additive | scope3-subset-exceeds-total或scope2-bases-not-additive |
| `solution-delivery-notebook` | 规格S-1追溯到不存在的需求R-NONE | `SDN-004` | SDN-004 [S-1]: Every specification must trace to a requirement | — |
| `product-constraint-register` | 待办B-3引用另一产品的约束 | `PCC-004` | PCC-004 [B-3]: Constraint belongs to another product | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `security-audit-record` | 在「安全审计记录」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `environmental-decision-log` | 在「环境决策日志」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `change-profile-governance-checklist` | 在「变革画像治理检查清单」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `decision-delegation-register` | 在「决策授权与可逆性登记」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `sustainable-procurement-strategy` | B提交排放/抵消独列和设备去向，但仍无五年TCO | 仅关闭已补资料缺口，仍不能完整比较或自动选B |
| `cloud-environmental-data-contract` | Scope3设备子集从6000更新为7000，总额仍9000 | 子集更新且仍不相加；两种Scope2与抵消保持独立 |
| `solution-delivery-notebook` | 删除控制C-1 | 分析结果变化：新增缺口RK-1:control |
| `product-constraint-register` | 为B-3补记有证据的豁免D-1 | 分析结果变化：blocked_item_ids：["B-3"]→[] |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `change-profile-governance-review` | 执行「按变革画像逐项核查规划、实施和价值条件」时跳过或误做：无通过证据不得标通过 | `missing-evidence` | 无通过证据不得标通过 | — |
| `decision-delegation-register-method` | 执行「决策授权与可逆性登记分析方法」时跳过或误做：七名称来自外部方法；权责描述与组织约定一致 | `missing-evidence` | 七名称来自外部方法；权责描述与组织约定一致 | — |
| `solution-delivery-notebook-review` | 规格S-1追溯到不存在的需求R-NONE | `SDN-004` | SDN-004 [S-1]: Every specification must trace to a requirement | — |
| `product-constraint-conformance-review` | 待办B-3引用另一产品的约束 | `PCC-004` | PCC-004 [B-3]: Constraint belongs to another product | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
