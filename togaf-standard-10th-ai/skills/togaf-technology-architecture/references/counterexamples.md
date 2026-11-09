# togaf-technology-architecture 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `microservice-technical-guidance` | 对「微服务技术指南」给出：外部实践补充必须标项目约定，不能冒充指南原文 | `missing-evidence` | 外部实践补充必须标项目约定，不能冒充指南原文 | — |
| `interoperability-assessment` | 对「互操作性评估」给出：网络连通不能证明语义和业务互操作 | `missing-evidence` | 网络连通不能证明语义和业务互操作 | — |
| `soa-layered-reference` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `microservice-technical-guidance` | 在「微服务技术指南」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `interoperability-assessment` | 在「互操作性评估」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `soa-layered-reference` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `msa-source-deployment-execution-method` | 执行「MSA源、部署与执行单元追溯表分析」时跳过或误做：按需求/故障条件扩实例并保留同包追溯 | `dangling-reference` | 按需求/故障条件扩实例并保留同包追溯 | — |
| `msa-readiness-evidence-method` | 执行「MSA组织与生命周期就绪证据分析」时跳过或误做：OSIMM按独立来源调用，不用ACMM或项目表替代 | `missing-evidence` | OSIMM按独立来源调用，不用ACMM或项目表替代 | — |
| `msa-federated-governance-process-method` | 执行「MSA双轨治理与豁免过程分析」时跳过或误做：支持/对齐/扩展/约束分别记录方向 | `matrix-direction` | 支持/对齐/扩展/约束分别记录方向 | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
