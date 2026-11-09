# togaf-migration-roadmap 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `rollback-plan` | 对「回退计划」给出：回退不是仅写恢复备份，应说明业务与数据恢复条件 | `missing-evidence` | 回退不是仅写恢复备份，应说明业务与数据恢复条件 | — |
| `implementation-factor-catalog` | 只写“成熟度低”无具体观察或证据 | `factor-evidence-gap` |  | — |
| `portfolio-theme-work-package-register` | WP-ID依赖WP-SIGN形成循环；或一包同时keep/improve | `dependency-cycle` | dependency-cycle或ambiguous-change-kind | dependency-cycle或ambiguous-change-kind |
| `portfolio-estimate-sufficiency-check` | 缺应急系数却生成10%默认值 | `missing-project-contingency` |  | — |
| `project-work-package-authorization` | 无授权却请求开始 | `authorization-not-ready` |  | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `rollback-plan` | 在「回退计划」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `implementation-factor-catalog` | 新增演练结果证明东仓已掌握集成 | 技能缺口可关闭，专家每周8小时容量不自动变多 |
| `portfolio-theme-work-package-register` | WP-SIGN新增等待数据责任批准的前置WP-GOV | 新增前置记录，签收不能沿旧依赖序列启动 |
| `portfolio-estimate-sufficiency-check` | 本轮估算106万改125万，覆盖比从2改4 | 估算变化25%超过缓冲、比值未下降；收益递减信号均未达到，继续针对高不确定项调查 |
| `project-work-package-authorization` | DEL-APPS-v2已接受且PM确认规则并发授权 | 状态改为authorized-in-fixture，可在虚构案例开始；不授予真实人工作权限 |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `dependency-topological-order` | 依赖图中 A→B→C→A 成环，仍输出 A、B、C 的顺序 | `cycle` | 存在环却直接给出顺序，未报告环 | — |
| `transition-operability-check` | 过渡架构仅给出「完成 70%」，未说明人员、系统、数据、控制与回退 | `transition-operability-gap` | 只给进度百分比就判定过渡可运营 | — |
| `work-package-prioritization` | 五项准则各给 20% 权重，但无任何来源或裁决记录 | `missing-evidence` | 权重无来源却直接加权算出总分 | — |
| `benefit-realization-trigger` | 以计划收益 12% 作为实测值参与偏差计算 | `measurement-evidence-gap` | 把计划值当实测值计算偏差 | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
