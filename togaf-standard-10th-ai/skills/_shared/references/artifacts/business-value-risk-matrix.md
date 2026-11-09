# 业务价值与风险矩阵

依据预先制定的价值和风险准则，怎样评价项目？

这是依据C220用途形成的项目操作契约。字段、布局及判据不声称为官方规定。

## 来源

- C220 05-architecture-content §3.6.9.2. Business Value and Risk Matrix；来源块：C220-web-2025:05-architecture-content:b00546, C220-web-2025:05-architecture-content:b00547, C220-web-2025:05-architecture-content:b00548, C220-web-2025:05-architecture-content:b00549, C220-web-2025:05-architecture-content:b00550

## 分析与证据

- 依据预先制定的价值和风险准则，怎样评价项目？
- 价值和风险分别建立指数；由高层在方案已知前制定并批准准则及权重。
- 未评价指数保持未知；不补0、等权或批准。项目assessed状态须有先验准则日期、权重、原始评分与来源，可复算后仍需实际评审。
- 候选设计、指数和生成结果不自动构成组织接受或实际批准。

字段：name, value_index, risk_index, criteria_basis。未提供字段保持未知。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.9.2. Business Value and Risk Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#_business_value_and_risk_matrix)
  - 概念：业务价值/风险矩阵以分别加权的价值和风险指数评价项目。
  - 逻辑：价值可考虑原则、财务、战略和竞争；风险可考虑规模复杂性、技术、组织容量及失败影响。
  - 决策：高级管理层在知道选项前制定并批准指数、准则及权重，再应用真实证据。
  - 边界：不得从样例自动产生分数、组织容量或管理批准；先知选项后调权重违背本节决策顺序。
