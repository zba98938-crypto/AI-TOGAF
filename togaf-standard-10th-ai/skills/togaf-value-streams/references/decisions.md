# togaf-value-streams 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据（什么条件下适用）、反例（什么时候不该用）、影响（波及哪些制品或字段）。

## 判断 1：价值流 / 价值链 / 价值网络三选一

- 判据：问题是「给某个接收者交付什么成果」时用**价值流**（`value-stream-definition`）；问题是「企业内部哪些主要活动与支持活动支撑价值」时用**价值链**（`porter-value-chain`）；问题是「多个参与者之间如何交换有形或无形价值」时用**价值网络**（`value-network-default`）。
- 反例：用价值链代替价值流去回答「客户拿到什么」，会把内部活动顺序误当成客户价值顺序；用价值流去描述多方交换，会把网络压成一条线，丢失双向与多向依赖。
- 影响：`value_stream` / `value_stage` / `value_network_actor` 的对象类型选择，以及 `value-stream-map` 与 `value-chain-diagram` 两个制品族的产出。

## 判断 2：阶段粒度停在「价值增加」而不是「作业步骤」

- 判据：一个阶段必须能说出「进入条件、退出条件、客户价值项」。若一段工作无法给出这三者，它是作业步骤，属于流程，不属于价值流阶段。
- 反例：把「录入订单」「校验地址」「打印面单」拆成三个阶段，是把流程步骤当阶段，阶段数虚高而每个阶段没有独立价值。
- 影响：`value_stage` 的 `entry_condition`、`exit_condition`、`value_item` 三个必填字段；`value-stream-capability-matrix` 的列数。

## 判断 3：能力使能不等于流程执行

- 判据：阶段需要「具备什么能力才能完成」时连 `enabled_by`；阶段需要「由哪个流程把它做出来」时连流程实现。前者是条件，后者是执行。
- 反例：把「仓储能力」画成价值流阶段内的一个流程框，会让读者以为仓储是一个动作；反过来把「拣货流程」画成使能能力，会让读者以为不用执行就自动具备。
- 影响：`value-stream-enabling-capabilities` 的边类型；`value-stream-capability-matrix` 的格值语义。

## 判断 4：精益价值流的 LT/PT 只在串行链上求和

- 判据：只有当工作流为单一串行链（每阶段恰好一个后继与前驱）时，才可累加 `lead_time` 与 `processing_time`；存在并行、返工或断开时只能逐段列出。
- 反例：三个并行分支各 2 天，直接相加得 6 天并声称总 LT，实际是 2 天。
- 影响：`lean_process` 的 `lead_time`、`processing_time`、`complete_accurate`、`queue`；`lean-serial-flow` 分析的 `total_lead_time_minutes` 与 `activity_ratio_percent`。

## 判断 5：颜色与热力不代表绩效结论

- 判据：热力图每一格必须能指向已声明的 `scale` 与 `dimension`；颜色只表达该量表上的位置。没有量表时只能出表格并标注未定标。
- 反例：用红黄绿表达「这个阶段不好」，但不给量表也不给评分依据，读者无法复核，也无法区分「能力弱」与「流程慢」。
- 影响：`value-stream-capability-heatmap` 的 `score` / `scale` / `target` 字段；`attribute-not-expressed` 与 `unknown-scale-not-invented` 两类检查。
