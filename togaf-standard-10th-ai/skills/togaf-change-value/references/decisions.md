# togaf-change-value 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：环境债与技术债是两个登记册

- 判据：`environmental_debt` 记录已产生但未处置的环境负担（能耗超标、待处置副产物、超期设备）；`technical_debt` 记录架构与实现层面的偿债项（临时方案、过时依赖）。两者驱动因素、责任方与度量都不同。
- 反例：把「服务器老旧耗电高」只记进技术债，环境报告里看不到；或把「代码质量差」记进环境债，环境责任方无从处置。
- 影响：`environmental-debt-register` 与 `technical-debt-register` 的字段不重叠；`sustainability-dual-entry-analysis` 的入口；G242 与 G217 的引用边界。

## 判断 2：债务不等于财务负债

- 判据：技术债与环境债都不自动产生会计意义上的负债金额。若要折算成本，必须另行声明换算规则与来源，且结果标为估算。
- 反例：把「技术债 120 万」写进财务报表，实际是根据工时估算的推测值，无会计依据。
- 影响：`technical_debt` 的 `cost_or_interest` 字段（须标估算）；`environmental_debt` 的度量单位；`measurement-basis-gap` 检查。

## 判断 3：计划收益不是已实现收益

- 判据：`guide:value_observation` 必须区分 `expected` 与 `finding`，并给出 `baseline`、观测窗与 `attribution`。没有实测值时只能报「未观测」。
- 反例：把立项时的预期写成观测结果，导致收益复评永远显示「达标」。
- 影响：`value-realization-assessment`；`benefit-realization-trigger` 的触发判定；`measurement-evidence-gap` 检查。

## 判断 4：效率改善要扣用量增长

- 判据：单位效率提升（如每笔交易能耗下降）不等于总量下降。结论必须同时给出单位指标与总量指标，并说明用量变化。
- 反例：单机效率提升 20%，但服务器数量翻倍，总能耗上升 60%，却报告「节能 20%」。
- 影响：`environment_measure` 的 `value` 与 `allocation`；`sustainability-dual-entry-analysis`；反弹效应的登记。

## 判断 5：变更影响必须含受影响视图与工作包

- 判据：任何变更请求必须列出受影响的视图、工作包与验收准则；三者之一为空时说明变更尚未被评估，不得进入实施。
- 反例：变更只写「调整数据模型」，未指出哪几张图、哪个工作包、哪条验收准则需要改，实施时遗漏导致图与模型脱节。
- 影响：`change_request` 的 `impact`；`analyze.py --impact` 的遍历；`architecture-roadmaps` 的重排。
