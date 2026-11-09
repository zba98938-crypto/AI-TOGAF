# togaf-business-models-processes 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `customer-journey` | 对「客户旅程」给出：客户旅程不是内部流程图，体验陈述需证据 | `missing-evidence` | 客户旅程不是内部流程图，体验陈述需证据 | — |
| `customer-persona` | 对「客户画像」给出：虚构人物叙述不能冒充真实用户研究结果 | `missing-evidence` | 虚构人物叙述不能冒充真实用户研究结果 | — |
| `government-reference-tailoring` | 对「政府参考模型裁剪」给出：参考部门分类不是实际组织架构，版本中的部门计数应核对 | `missing-evidence` | 参考部门分类不是实际组织架构，版本中的部门计数应核对 | — |
| `digital-business-reference-tailoring` | 对「数字业务参考模型裁剪」给出：参考模型裁剪不表示全量采用，也不等于最终技术架构 | `missing-evidence` | 参考模型裁剪不表示全量采用，也不等于最终技术架构 | — |
| `four-box-business-model` | 对「四框业务模型」给出：四框不能用九块画布或六维立方体的字段替代，利润公式需要明确变量而非捏造收益 | `missing-attribute` | 四框不能用九块画布或六维立方体的字段替代，利润公式需要明确变量而非捏造收益 | — |
| `business-model-cube` | 对「业务模型立方体」给出：中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级 | `missing-evidence` | 中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级 | — |
| `operating-model` | 对「运营模式」给出：两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序 | `missing-evidence` | 两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序 | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `customer-journey` | 在「客户旅程」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `customer-persona` | 在「客户画像」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `government-reference-tailoring` | 在「政府参考模型裁剪」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `digital-business-reference-tailoring` | 在「数字业务参考模型裁剪」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `four-box-business-model` | 在「四框业务模型」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `business-model-cube` | 在「业务模型立方体」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `operating-model` | 在「运营模式」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `government-reference-catalog-overlay-method` | 执行「government-reference-catalog-overlay参考裁剪分析」时跳过或误做：用节点属性表达本地覆盖并保持参考身份 | `missing-attribute` | 用节点属性表达本地覆盖并保持参考身份 | — |
| `dbrm-mapping-suite-method` | 执行「dbrm-mapping-suite参考裁剪分析」时跳过或误做：项目补充映射另标project-only，不反写来源 | `missing-evidence` | 项目补充映射另标project-only，不反写来源 | — |
| `digital-enablement-competency-mapping-method` | 执行「digital-enablement-competency-mapping参考裁剪分析」时跳过或误做：用多角色协作和行动填补缺口，不把语境当成熟度级别 | `missing-evidence` | 用多角色协作和行动填补缺口，不把语境当成熟度级别 | — |
| `operating-model-submodel-analysis-method` | 执行「operating-model-submodel-analysis参考裁剪分析」时跳过或误做：核对资源缺口并调整范围或补充能力 | `view-edge-outside` | 核对资源缺口并调整范围或补充能力 | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
