# togaf-business-models-processes 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：业务模式画布不是战略，也不是流程

- 判据：`business_model_component` 解释「创造、交付、获取价值的逻辑」，九区是分析框架；战略回答「选哪条路」，流程回答「怎么执行」。三者层级不同。
- 反例：把九区当作战略规划模板去填五年目标，或把九区内容直接当作流程清单，都会让画布失去「检查价值逻辑是否自洽」的用途。
- 影响：`business-model-canvas` 与 `four-box-business-model` 的适用范围；与 `togaf-strategy-capabilities` 的交接。

## 判断 2：九区留空必须标「未确定」，不能默认成立

- 判据：任一区块无法给出内容时，写「未确定」并登记缺口；留空会被读者当作「不适用」或「已确认无此项」。
- 反例：成本结构区块留空，读者以为该业务没有成本压力；实际是尚未核算。
- 影响：`business_model_component` 的 `detail` 与 `assumptions`；缺口清单；画布的可评审性。

## 判断 3：功能分解与流程分解是两条线

- 判据：`function` 回答「组织具备什么能力去做什么」，可独立于时间；`process` 回答「事情按什么顺序发生」。功能分解不表达时序，流程分解不表达职责归属。
- 反例：把「采购」既当功能又当流程画在同一层级，导致功能清单里混入时序步骤，能力映射时无法对齐。
- 影响：`functional-decomposition-diagram` 与 `process-flow-diagram` 的对象类型；`application-function-matrix` 的行定义。

## 判断 4：客户画像必须有证据，不能由内部假设代替

- 判据：`persona` 的 `evidence` 必须指向访谈、调研、行为数据或可核来源；纯内部推想的画像标记为假设并注明验证方式。
- 反例：会议室里编出三个人物志，直接用于旅程设计，结果设计出的体验无人使用。
- 影响：`customer-persona`；`customer-journey` 的 `pain_point` 是否有据；`missing-evidence` 检查。

## 判断 5：价值链、价值流、精益价值流按问题选择

- 判据：价值链看企业内部活动结构（主要／支持活动）；价值流看对接收者的成果序列；精益价值流看流动与浪费，需要 LT/PT 等度量。
- 反例：用价值链回答「客户在多长时间内拿到货」，或用精益价值流描述多方价值交换，都会答错问题。
- 影响：`value-chain-diagram`、`value-stream-map`、`lean-value-stream` 三个制品族的选择；与 `togaf-value-streams` 的边界。
