# 迁移与价值的可执行项目规则

以下是本项目对 G186/G188 的依赖与规划、G248 的过渡状态、G176 的决策比较、G184 的价值反馈的可执行辅助。它们不构成 TOGAF 统一算法、默认权重或阈值。定性判断仍由技能执行。

共享模型的 `analyses[]` 可使用以下四个 `method_id`，再通过 `analyze.py model.json --evaluate 分析ID` 运行。输入规范及可运行正例、修改与反例见 method-runtime（历史材料已清理）。每个输入都必须明确规则来源；不得用生成的排序或文档清单代替批准与实际效果。

| 方法 | 输入要点 | 输出与限制 |
| --- | --- | --- |
| dependency-topological-order | work_packages 含 id/evidence；dependencies 含 source/target/kind/evidence，source 是前置，target 是后继；kind 区分 hard/soft | 硬依赖批次、未满足的软依赖；检测环与未知端点，不从批次推断日历工期或关键路径 |
| transition-operability-check | transition_id；people/systems/data/controls/rollback 五项 conditions；结构化 rollback.trigger、owner、verification、evidence | `document_gate_complete` 表示项目清单齐备；`runtime_operability` 始终 not-verified，不能以完成百分比推导可运营性 |
| work-package-prioritization | criteria 的 weight/weight_evidence、min/max/scale_evidence 和 higher_is_better=true；工作包逐项 scores/score_evidence；显式 sensitivity.relative_weight_delta 与 evidence | 先将已转为越高越好的偏好分数按声明量表归一化，再按和为 1 的权重评分；输出并列组及每权重正负扰动情景。成本不得直接作为偏好分，局部敏感性不代表所有权重组合稳定 |
| benefit-realization-trigger | target/baseline/observed 各含 value/metric_id/unit/scope/basis/period/evidence；观测 kind 为 observed 或 simulated-observation；direction；事先声明 trigger 规则 | 同口径及目标适用窗口一致才比较；正数基准的相对偏差、基线改善、绝对偏差与严格触发边界。无观察返回未观察，计划/估算拒绝，不产生因果归因或正式接受 |

回退触发必须显式记录 metric、operator（gt/ge/lt/le）、threshold、period、consecutive_periods、denominator_policy（unknown-on-zero 或 not-a-ratio）。这些字段齐备只证明条件可以结构化解释，不能证明其阈值适宜、演练有效或真实运行安全。

收益方法的目标与观测 period 必须完全一致，基线可来自不同历史期间，但指标、单位、范围及计算依据必须一致。模拟观察保留 simulated-observation。相对触发要求 target 和 baseline 为正，零基准不自动计算增长率；需要绝对变化的项目应另行声明算法。输出不提供自动批准字段。
