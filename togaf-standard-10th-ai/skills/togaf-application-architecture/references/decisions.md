# togaf-application-architecture 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：应用边界按「谁负责任命与变更」划分

- 判据：一个应用是**部署与变更的最小责任单元**。若两部分由不同团队独立发布、独立回滚、独立定 SLA，它们是两个应用；若必须同版本一起发布，即使物理分进程，也按一个应用建模再拆组件。
- 反例：按技术栈（前端／后端／数据库）拆成三个应用，会导致应用组合目录里每个业务功能对应三条记录，功能矩阵无法读；反过来把两个独立发布的系统合成一个，会掩盖真实的发布耦合。
- 影响：`application` 的 `boundary` 与 `owner`；`application-portfolio-catalog` 的行数；`application-function-matrix` 的格值。

## 判断 2：组件是应用内部的职责划分，不是独立资产

- 判据：组件没有独立生命周期、不单独对外承诺 SLA、不单独出现在采购合同里时，建成 `application_component`；只有前者成立时才升级为独立 `application`。
- 反例：把每个模块都建成应用，应用数从上几十膨胀到几百，组合分析与冗余识别失效。
- 影响：`application_component` 与 `application` 的类型选择；`application-communication-diagram` 的节点粒度。

## 判断 3：接口必须有发送方、接收方与版本

- 判据：任何跨应用的数据或调用关系，建成 `interface` 并填 `producer`、`consumer`、`protocol`、`payload`、`version` 五项。缺任一项时按缺口处理，不用一条无类型连线代替。
- 反例：只画一条「两个系统之间有数据流」的箭头，读者无法知道方向、协议、载荷，也无法在改造时判断谁必须改。
- 影响：`interface` 的五项必填；`interface-catalog`；`application-interaction-matrix` 的方向语义；`interface_sender` / `interface_receiver` 两条关系。

## 判断 4：单体与微服务的分界看数据边界与失败隔离，不看服务数量

- 判据：能否独立部署只是必要条件；还需**自有数据边界**与**失败隔离**（一个服务故障不拖垮其他）。三者缺一，拆出来的只是分布式单体。
- 反例：把一张表拆给三个服务共用，服务数增加了但数据边界没有，任一方改表结构仍需三方协调；或拆分后没有超时与降级，一个慢依赖拖垮全链。
- 影响：`microservice` 的 `business_function`、`development_resources`、`operations_resources`、`planned_state`、`value`；`service_boundary`；`ops:msa_readiness` 与 `ops:msa_governance`。

## 判断 5：MSA 参考图不能当定稿架构

- 判据：G21I 图 5-3 展示的是 **SOA 参考架构**，正文明确 MSA 专用参考模型仍在发展。引用该图时必须标注它是 SOA 参考，不得改称「MSA 定稿参考架构」。
- 反例：把该图作为本企业微服务目标架构的基准，会把 SOA 的服务编排假设带进来，与本项目的独立部署与数据边界要求冲突。
- 影响：`application-communication-diagram` 与 `software-engineering-diagram` 的引用说明；来源定位的表述。
