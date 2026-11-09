# togaf-information-data 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `data-quality-assessment` | 对「数据质量评估」给出：不同质量维度不能无依据地加总成一个精确分数 | `missing-evidence` | 不同质量维度不能无依据地加总成一个精确分数 | — |
| `metadata-dictionary` | 对「元数据字典」给出：资产名称相同不保证含义相同，字典不是所有数据值的副本 | `missing-evidence` | 资产名称相同不保证含义相同，字典不是所有数据值的副本 | — |
| `data-usage-documentation` | 对「数据使用文档」给出：存在使用关系不等于已获访问授权 | `missing-evidence` | 存在使用关系不等于已获访问授权 | — |
| `metadata-policy-documentation` | 对「元数据规则与政策文档」给出：政策描述与可执行验证规则需分别标识 | `missing-evidence` | 政策描述与可执行验证规则需分别标识 | — |
| `data-issue-register` | 对「数据问题文档／登记册」给出：未经验证的根因只能标为假设 | `missing-evidence` | 未经验证的根因只能标为假设 | — |
| `business-technical-asset-mapping` | 对「业务与技术资产关联」给出：概念相近不等于同一资产，关联不是自动实现关系 | `missing-evidence` | 概念相近不等于同一资产，关联不是自动实现关系 | — |
| `metadata-repository-design` | 对「元数据存储库设计」给出：部署一个存储库不自动建立数据治理 | `missing-evidence` | 部署一个存储库不自动建立数据治理 | — |
| `metadata-model` | 对「元数据模型」给出：图4-5的参考资产不是每个项目必须全选的模型 | `missing-evidence` | 图4-5的参考资产不是每个项目必须全选的模型 | — |
| `metadata-asset-coverage` | 对「元数据资产覆盖矩阵」给出：参考图空格不表示禁止、不存在或无需管理 | `empty-view` | 参考图空格不表示禁止、不存在或无需管理 | — |
| `metadata-validation-workflow` | 对「元数据校验工作流」给出：协作式的最终一致性不等于没有治理 | `missing-evidence` | 协作式的最终一致性不等于没有治理 | — |
| `metadata-integration-model` | 对「元数据集成模型」给出：集成组织方式与手工推送拉取采集方式是两个独立维度 | `missing-evidence` | 集成组织方式与手工推送拉取采集方式是两个独立维度 | — |
| `metadata-ingestion-options` | 对「元数据采集备选方案」给出：三种机制是备选方案，不是三个固定先后阶段 | `missing-evidence` | 三种机制是备选方案，不是三个固定先后阶段 | — |
| `metadata-inference-design` | 对「技术元数据推断方案」给出：采集模式不必然需要读取实际业务数据 | `missing-evidence` | 采集模式不必然需要读取实际业务数据 | — |
| `customer-mdm-model` | 对「客户主数据模型」给出：统一客户标识不等于无条件合并不同业务语境 | `missing-evidence` | 统一客户标识不等于无条件合并不同业务语境 | — |
| `mdm-integration-style` | 对「主数据集成风格」给出：参考集成风格不是指定厂商产品 | `missing-evidence` | 参考集成风格不是指定厂商产品 | — |
| `mdm-exchange-pattern` | 对「主数据交换模式」给出：缩写必须随来源定义，不凭名称猜测语义 | `missing-evidence` | 缩写必须随来源定义，不凭名称猜测语义 | — |
| `bi-transition-architecture` | 对「BI 与分析演进架构」给出：不同状态是同一架构的演进视图，不机械当成独立制品种类 | `mixed-evolution` | 不同状态是同一架构的演进视图，不机械当成独立制品种类 | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `data-quality-assessment` | 在「数据质量评估」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-dictionary` | 在「元数据字典」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `data-usage-documentation` | 在「数据使用文档」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-policy-documentation` | 在「元数据规则与政策文档」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `data-issue-register` | 在「数据问题文档／登记册」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `business-technical-asset-mapping` | 在「业务与技术资产关联」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-repository-design` | 在「元数据存储库设计」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-model` | 在「元数据模型」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-asset-coverage` | 在「元数据资产覆盖矩阵」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-validation-workflow` | 在「元数据校验工作流」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-integration-model` | 在「元数据集成模型」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-ingestion-options` | 在「元数据采集备选方案」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `metadata-inference-design` | 在「技术元数据推断方案」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `customer-mdm-model` | 在「客户主数据模型」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `mdm-integration-style` | 在「主数据集成风格」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `mdm-exchange-pattern` | 在「主数据交换模式」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `bi-transition-architecture` | 在「BI 与分析演进架构」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `metadata-requirement-method` | 执行「元数据需求与范围分析」时跳过或误做：参考资产清单不是强制全选 | `missing-evidence` | 参考资产清单不是强制全选 | — |
| `metadata-integration-tradeoff` | 执行「元数据集成与采集权衡」时跳过或误做：组织模型和采集机制不能混为一维 | `missing-evidence` | 组织模型和采集机制不能混为一维 | — |
| `mdm-identity-analysis` | 执行「客户主数据身份与集成分析」时跳过或误做：统一客户视图不是无条件合并所有记录 | `missing-evidence` | 统一客户视图不是无条件合并所有记录 | — |
| `bi-transition-method` | 执行「BI 与分析演进规划」时跳过或误做：参考目标平台不直接指定厂商 | `missing-evidence` | 参考目标平台不直接指定厂商 | — |
| `mdm-operational-ten-questions-method` | 执行「C-MDM十问运营诊断分析」时跳过或误做：将缺口映射行动、责任、影响；不得按yes比例冒充成熟度 | `missing-evidence` | 将缺口映射行动、责任、影响；不得按yes比例冒充成熟度 | — |
| `mdm-four-plateau-operations-method` | 执行「C-MDM四平台态运营计划分析」时跳过或误做：选择演进触发，不强制固定四期 | `missing-evidence` | 选择演进触发，不强制固定四期 | — |
| `mdm-match-merge-arbitration-method` | 执行「C-MDM匹配、合并与人工仲裁分析」时跳过或误做：执行前验证可取消合并与历史语义 | `missing-evidence` | 执行前验证可取消合并与历史语义 | — |
| `msa-data-distribution-conditions-method` | 执行「MSA数据分布、分片与批次条件表分析」时跳过或误做：核查数据流与运行独立性冲突 | `missing-evidence` | 核查数据流与运行独立性冲突 | — |
| `bi-stage-operability-and-exit-method` | 执行「BI多阶段运营与退出条件分析」时跳过或误做：退出前逐项验证旧需求与恢复、治理、元数据 | `missing-evidence` | 退出前逐项验证旧需求与恢复、治理、元数据 | — |
| `mdm-business-function-coverage-method` | 执行「C-MDM业务功能参考覆盖分析」时跳过或误做：对缺口形成具体补证/实现/复评行动，不合成成熟度分数 | `missing-evidence` | 对缺口形成具体补证/实现/复评行动，不合成成熟度分数 | — |
| `mdm-application-function-coverage-method` | 执行「C-MDM应用功能参考覆盖分析」时跳过或误做：对缺口形成具体补证/实现/复评行动，不合成成熟度分数 | `missing-evidence` | 对缺口形成具体补证/实现/复评行动，不合成成熟度分数 | — |
| `bi-value-chain-controls-method` | 执行「BI数据价值链、语义与控制分析」时跳过或误做：不因价值链存在就认定数据正确/及时 | `missing-evidence` | 不因价值链存在就认定数据正确/及时 | — |
| `bi-model-operating-monitoring-method` | 执行「BI分析模型运营监控与处置分析」时跳过或误做：形成运行监控记录后再评审实际表现 | `missing-evidence` | 形成运行监控记录后再评审实际表现 | — |
| `metadata-application-coverage-review` | 执行「元数据应用功能覆盖审查」时跳过或误做：源表每行有一个处置结果；遗漏为未知 | `missing-evidence` | 源表每行有一个处置结果；遗漏为未知 | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
