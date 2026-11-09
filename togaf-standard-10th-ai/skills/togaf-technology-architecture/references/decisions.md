# togaf-technology-architecture 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：技术标准与技术的分界

- 判据：`technology_standard` 是可被引用与版本的**约束**（某协议版本、某安全基线）；`technology` 是**具体产品与实现**（某厂商某版本的中间件）。标准约束多个技术，技术遵循一个或多个标准。
- 反例：把「Oracle 19c」写成技术标准，会让标准目录变成厂商目录，退出该厂商时整个标准体系需要重写。
- 影响：`technology-standards-catalog` 与 `technology-portfolio-catalog` 的内容；`implements_standard` 边；退役影响分析的范围。

## 判断 2：OT/IT 边界必须显式，不能靠部署图推断

- 判据：L3（MES／LIMS 等运营管理）与 L4（ERP 等经营计划）之间必须显式标出边界与穿越点；生产网（L0–L2）与环境网分区必须写在 `network_zone` / `ics_zone` 上，不能靠图的位置暗示。
- 反例：把 SCADA 与 ERP 画在同一层，读者会以为二者可直接互连；实际中间隔着 DMZ 与数据交换。
- 影响：`platform-decomposition-diagram` 与 `network-and-communications-diagram`；`deployment_node` 的 `environment`；安全域与信任边界的建模前置。

## 判断 3：技术退役必须有替代关系与日期

- 判据：任何标为 EOL 的技术，必须给 `support_end` 与替代技术（`replaced_by`）；只写「已弃用」不构成可执行信息。
- 反例：某中间件标「停用」，但无替代与截止日，结果是被下游应用继续引用，且无人能判断何时必须迁移。
- 影响：`technology` 的 `lifecycle`、`support_end`；`application-migration-diagram` 的迁移对象；新依赖的合规审查。

## 判断 4：云迁移不等于减排，核算范围要跟着走

- 判据：迁移到云时，排放从 Scope 1/2 变为上游 Scope 3（云服务商）。判断减排必须比较**同一核算边界**下的总量，而不是比较自有数据中心的直接排放。
- 反例：把自有机房电耗清零就宣布减排 30%，但未计入云服务商的上游排放，实际总量可能不降反升。
- 影响：`environment_measure` 的 `scope`、`boundary_id`、`allocation`；与 `togaf-change-value` 的环境债登记；`shared-carbon-factor-catalog` 的因子适用边界。

## 判断 5：互操作问题定位到具体层

- 判据：互操作障碍必须归入语义（同一词不同义）、协议（传输与格式）、或数据（主数据不一致）三层之一，并指明受影响接口。泛泛的「集成困难」不是问题定位。
- 反例：把「上下游系统对不上」记成一条互操作问题，既无法分配责任也无法验收修复；拆到三层后通常发现是主数据编码不一致。
- 影响：`interoperability_issue` 的记录粒度；`interoperability-assessment` 的结论；与 `togaf-information-data` 的主数据治理交接。
