# togaf-architecture-workbench 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `architecture-project-wbs` | 对「架构项目工作分解」给出：架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F | `missing-evidence` | 架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F | — |
| `architecture-project-schedule` | 对「架构项目资源与进度」给出：没有依赖和工期证据不能宣称算出关键路径 | `missing-evidence` | 没有依赖和工期证据不能宣称算出关键路径 | — |
| `project-management-strategy` | 对「架构项目管理策略」给出：名称、来源表格和成功输出不等于业务结论已核实 | `missing-evidence` | 名称、来源表格和成功输出不等于业务结论已核实 | — |
| `project-status-highlight-report` | 对「架构项目状态要点报告」给出：名称、来源表格和成功输出不等于业务结论已核实 | `missing-evidence` | 名称、来源表格和成功输出不等于业务结论已核实 | — |
| `domain-architecture-alignment` | 安全关注点引用不存在的领域 | `DAA-002` | DAA-002 [DOM-SEC]: Security references unknown domain DOM-NONE | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `architecture-project-wbs` | 在「架构项目工作分解」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `architecture-project-schedule` | 在「架构项目资源与进度」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `project-management-strategy` | 在「架构项目管理策略」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `project-status-highlight-report` | 在「架构项目状态要点报告」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `domain-architecture-alignment` | 数据领域改为服务EA-2027的OBJ-1并引用共享对象 | 分析结果变化：关闭缺口DOM-DATA:shared-model |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `architecture-project-scheduling` | 执行「架构项目分解与排程」时跳过或误做：不完整依赖不能支持确定关键路径 | `missing-evidence` | 不完整依赖不能支持确定关键路径 | — |
| `reference-model-tailoring` | 执行「参考模型裁剪」时跳过或误做：参考分类不是项目实际组织或部署事实 | `missing-evidence` | 参考分类不是项目实际组织或部署事实 | — |
| `project-management-strategy-review` | 执行「架构项目管理策略审查」时跳过或误做：四核心方面来自§3.1.8，配置管理来自§4.2.1 | `missing-evidence` | 四核心方面来自§3.1.8，配置管理来自§4.2.1 | — |
| `project-highlight-review` | 执行「架构项目状态要点报告审查」时跳过或误做：要点报告是按时间驱动的沟通，不替代例外报告 | `missing-evidence` | 要点报告是按时间驱动的沟通，不替代例外报告 | — |
| `agile-collaboration-selection-switch` | 执行「四模式选择与周期切换」时跳过或误做：复核能力授权和回退条件，生成两布局并评审 | `missing-evidence` | 复核能力授权和回退条件，生成两布局并评审 | — |
| `domain-architecture-alignment-review` | 安全关注点引用不存在的领域 | `DAA-002` | DAA-002 [DOM-SEC]: Security references unknown domain DOM-NONE | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
