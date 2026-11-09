# 合并差距、方案和依赖矩阵

跨域差距由哪些候选方案覆盖，哪些依赖影响工作包？

这是依据C220用途形成的项目操作契约。字段、布局及判据不声称为官方规定。

## 来源

- C220 05-architecture-content §3.6.8.4. Consolidated Gaps, Solutions, and Dependencies Matrix；来源块：C220-web-2025:05-architecture-content:b00525, C220-web-2025:05-architecture-content:b00526, C220-web-2025:05-architecture-content:b00527, C220-web-2025:05-architecture-content:b00528, C220-web-2025:05-architecture-content:b00529, C220-web-2025:05-architecture-content:b00530

## 分析与证据

- 跨域差距由哪些候选方案覆盖，哪些依赖影响工作包？
- 把各域差距合并分组，比较覆盖一个或多个差距的候选方案及依赖，支持E/F工作包和迁移。
- 未评价的候选方案或依赖不默认空集合；有依据的无依赖判断需要说明。
- 候选设计、指数和生成结果不自动构成组织接受或实际批准。

字段：name, solution_refs, dependency_refs。未提供字段保持未知。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.8.4. Consolidated Gaps, Solutions, and Dependencies Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#_consolidated_gaps_solutions_and_dependencies_matrix)
  - 概念：合并差距、方案和依赖矩阵汇总各域差距并评价候选解决方式。
  - 逻辑：一个方案/依赖可对应一个或多个差距；依赖驱动项目安排。
  - 决策：整合差距后评估方案覆盖及依赖。
  - 边界：潜在方案不等于选定或批准方案，差距合并不能丢失来源。
