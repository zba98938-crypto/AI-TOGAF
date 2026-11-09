# 架构定义增量表

每个项目的增量交付分配到哪个过渡架构？

这是依据C220用途形成的项目操作契约。字段、布局及判据不声称为官方规定。

## 来源

- C220 05-architecture-content §3.6.8.5. Architecture Definition Increments Table；来源块：C220-web-2025:05-architecture-content:b00531, C220-web-2025:05-architecture-content:b00532, C220-web-2025:05-architecture-content:b00533, C220-web-2025:05-architecture-content:b00534, C220-web-2025:05-architecture-content:b00535

## 分析与证据

- 每个项目的增量交付分配到哪个过渡架构？
- 按指定时点的过渡架构分配项目增量交付；项目/工作包与过渡状态关系含increment_description。
- 连接工作包与过渡状态不等于已说明交付内容或实施完成。
- 候选设计、指数和生成结果不自动构成组织接受或实际批准。

字段：name, increment_description。未提供字段保持未知。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.8.5. Architecture Definition Increments Table](../../corpus/fundamental/analysis/05-architecture-content.md#_architecture_definition_increments_table)
  - 概念：架构定义增量表把项目增量交付分配到各过渡架构。
  - 逻辑：项目—增量—过渡架构—时间共同表达演进。
  - 决策：核对阶段交付与状态之间的关系。
  - 边界：计划时间和交付分配不等于已交付、已验收状态。
