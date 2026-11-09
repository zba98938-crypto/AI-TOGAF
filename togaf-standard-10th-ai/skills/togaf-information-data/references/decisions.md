# togaf-information-data 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：信息概念不是数据库表

- 判据：`information` 表达业务语言里的概念（「客户」「订单」「批次」），可以对应零到多个数据实体；`data_entity` 表达可被系统存储的结构。一个概念跨多实体、一个实体承载多概念都正常。
- 反例：把信息地图直接画成表结构，业务方看不懂，且表合并拆分时整张图要重画；反过来把概念当实体，会出现「客户信息表」这种既非业务概念也非物理表的中间物。
- 影响：`information-map` 与 `conceptual-data-diagram` 的对象类型；`information_concept` 与 `data_entity` 的映射边。

## 判断 2：概念模型停在业务语义，逻辑模型才给标识与基数

- 判据：`conceptual-data-diagram` 只表达实体与业务关系，不指定主键与外键；`logical-data-diagram` 才补 `identifier` 与具体基数。客户主数据须在逻辑层处理身份唯一性与匹配合并。
- 反例：在概念图里就开始讨论外键，会把实现选择当业务事实固定下来，后续换实现时图全部作废。
- 影响：`information-bounded-cardinality` 与 `logical-data-identifiers` 两个规范的适用范围；`er` 渲染器的基数要求。

## 判断 3：副本不等于权威源

- 判据：每个数据实体必须有一个 `authority`（权威源）。其他系统里的同结构数据是副本，须标 `delivery_mode` 与 `latency`，并且不得被当作权威值参与冲突裁决。
- 反例：三处都有「客户地址」，谁最后更新就用谁，导致地址口径漂移且无法审计。
- 影响：`data_entity` 的 `authority`、`delivery_mode`、`latency`；`data-dissemination-diagram`；`master_repository` 与 `master_exchange` 的职责划分。

## 判断 4：未知基数不自动变成一对多

- 判据：基数未确认时写 `unknown`，不要默认 `1..*`；有界基数（如 `1..2`）必须保留上界，不能压缩成 `many`。
- 反例：把「一个订单可能对应 1 到 2 个发票」写成 `0..*`，会让下游误以为可以无限开票。
- 影响：`cardinality` 字段；`invalid-cardinality` 与 `unknown-cardinality` 检查；`sequence` 等渲染器的属性可见性。

## 判断 5：主数据匹配合并要留候选与撤销路径

- 判据：身份匹配必须记录匹配依据（哪些字段、什么规则、置信度），合并必须可撤销并保留合并血缘；同名或同电话不足以直接合并。
- 反例：两家供应商名称只差一个「市」字就自动合并，导致采购记录串账且无法拆回。
- 影响：`master_data` 的 `business_identity`、`matching`、`ownership`；`guide:mdm_match_case`；`mdm-match-merge-arbitration-method` 的判定依据。
