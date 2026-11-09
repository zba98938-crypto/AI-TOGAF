# togaf-migration-roadmap 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：硬依赖与软依赖必须分开

- 判据：**硬依赖**是技术上不可并行的前置（数据迁移必须先于新系统切流）；**软依赖**是经验上更好但可承受并行的偏好（先培训再好上线）。只有硬依赖能决定批次。
- 反例：把所有「最好先做」的偏好都当硬依赖，整条路线被串行化，工期翻倍且没有任何技术理由。
- 影响：`dependency-topological-order` 的 `hard`/`soft` 标记；`crossed_soft_edges` 字段；批次数。

## 判断 2：过渡架构必须「可运营」，不能用进度百分比代替

- 判据：过渡状态必须同时具备人员、系统、数据、控制、回退五项条件；缺项即判不可运营。百分比只能描述完成量，不能描述可运行性。
- 反例：把「完成 70%」作为过渡架构的验收依据，实际该状态下旧系统已停、新系统未通，业务无法运转。
- 影响：`transition` 的 `definition` 与 `operating_conditions`；`transition-operability-check` 的输出；`architecture-roadmaps` 的阶段划分。

## 判断 3：权重必须有来源，否则不出总分

- 判据：`work-package-prioritization` 中每条准则的权重必须指向裁决记录、政策或历史基准。缺来源时不计算加权总分，只列准则与候选。
- 反例：五项准则各 20%，理由是「平均一点」；这种权重不承载任何偏好信息，算出的排序无法用于决策。
- 影响：`portfolio-estimate-sufficiency-check`；`ranking` 与 `sensitivity` 输出；决策记录的必要性。

## 判断 4：计划值不是实测值

- 判据：`benefit-realization-trigger` 只比较实测与目标。没有实测值时报「未观测」，不得用计划值代入计算偏差。
- 反例：用立项时的 12% 预期收益算「已达成」，把尚未发生的收益记为已实现。
- 影响：`value-realization-assessment`；`guide:value_observation` 的 `baseline` 与 `finding`；复评触发判定。

## 判断 5：回退必须具备可验证的触发条件

- 判据：每个回退步骤必须有 `trigger`、`decision_owner`、`prerequisite`、`verification` 四项。触发条件必须是可观测的事件或阈值，不能是「出现问题」。
- 反例：触发条件写「系统异常时回退」，无人能判定何时该按下按钮，结果是该回退时无人决策。
- 影响：`rollback_step` 的六项字段（含 `data_recovery` 与 `sequence`）；`rollback-plan` 制品；过渡架构的可运营性判定。
