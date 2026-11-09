# 方案备选、跨域交接与运营条件

**虚构验收案例，不代表真实企业事实。**

制品：解决方案交付笔记本（Solution Delivery Notebook (Architecture Contract Template)） · 模型 fictional-v2 · 视图 `delivery-notebook`

语境：`{"domains": ["business", "data", "application", "technology"], "landscape": "segment", "purpose": "project", "abstraction": "logical", "evolution": "target"}`

依据虚构材料表达候选设计；证据不足的结论保留缺口。

完整对象字段及关系见下方“模型表达”表；按视图规范选择记录式或行式布局。


图例／解释：虚构教学案例；稳定ID跨视图复用。候选设计和项目规则不表示官方模板或业务批准。


证据与缺口：

| 对象 | 来源 | 确定性 |
| --- | --- | --- |
| DELIVERY-NOTE | CASE-REVIEW | assumed |

- 门店在线销售与中央库存的当前交互尚未调查；影响：不能由线上订单接口推断门店在线行为；需要：门店在线流程、接口与失败处理材料。

- 已确认订单交给物流的具体接口和责任未提供；影响：只明确确认前不进入物流，交接规格待定；需要：物流接收契约与责任方。

- 最大断连时间未知；影响：阻断离线候选方案接受与运营状态进入；需要：断连上限与存储容量依据。

- 可容忍的数据丢失窗口未知；影响：阻断离线候选方案接受与运营状态进入；需要：持久成功标准、故障演练与数据丢失容忍。

- 冲突、补偿与回退责任待确认；影响：阻断离线候选方案接受与运营状态进入；需要：业务与运营责任人的交接接受记录。

方法检查：

- 规格总追溯到某项需求。
- 控制总追溯到某项风险。
- 架构描述摘要仅供参考，不替代规格。
- 笔记本是交付沟通模板，不代表合同已签署。

这些检查是评审问题，生成文件不自动表示已通过业务评审。

## 逐字段表达

表格按所选对象类型分组；相邻行不表示依赖或包含。嵌套字段保持结构化原值。

### guide:solution-delivery-notebook

字段较多或对象字段不同，逐对象显示字段／值；缺失项仍保留。

#### 方案备选与需求、规格、风险配对 [DELIVERY-NOTE]

| 字段 | 值 |
| --- | --- |
| ID | DELIVERY-NOTE |
| 类型 | guide:solution-delivery-notebook |
| 名称 | 方案备选与需求、规格、风险配对 |
| work_package_id | WP-OFFLINE |
| solution_concept_ref | interface-network |
| implementation_strategy | 受控试点；先明确接受条件和异常责任，再验证接口并决定是否进入候选运营状态 |
| stakeholders | [{"id": "SH-OPS", "name": "门店运营", "requirement_ids": ["REQ-CONSISTENCY", "REQ-OFFLINE"]}] |
| requirements | [{"id": "REQ-CONSISTENCY", "stakeholder_ids": ["SH-OPS"], "statement": "中央原子预占后才确认，总承诺不得超过可用；线上确认p95≤300ms"}, {"id": "REQ-OFFLINE", "stakeholder_ids": ["SH-OPS"], "statement": "离线仅持久受理待中央确认，限量及期限按POLICY-STOCK"}] |
| specifications | [{"applies_to": "APP-ORDER / APP-STOCK", "id": "SPEC-ONLINE", "requirement_id": "REQ-CONSISTENCY", "spec_type": "候选接口与业务契约", "statement": "A在中央原子预占后确认，虚构p95=160ms；B待中央确认p95=420ms；本次300ms线上目标下推荐A，生产性能仍待测。"}, {"applies_to": "APP-STORE / IF-RECOVERY", "id": "SPEC-OFFLINE", "requirement_id": "REQ-OFFLINE", "spec_type": "候选恢复与订单状态契约", "statement": "离线持久受理待确认，按v2限量和期限核验，重连去重且中央重新验库存；超限、过期和冲突转人工。"}] |
| risks | [{"description": "断连积压、重复执行、库存冲突及恢复后未对账", "id": "RISK-STOCK"}] |
| controls | [{"applies_to": "APP-STOCK", "id": "CTRL-STOCK", "risk_id": "RISK-STOCK", "statement": "候选持久队列、检查点、冲突检测及人工补偿"}] |
| gaps | [] |
| architecture_summary | {"application": {"view_ids": ["application-catalog", "interface-network"]}, "business": {"view_ids": ["capability-map", "requirements"]}, "information": {"reason": "本次政策及恢复目标已由虚构材料给定；完整数据模型、安全和生产验证仍待工程补充。", "status": "needs-input", "view_ids": ["order-states", "offline-data-boundary"]}, "infrastructure": {"reason": "部署拓扑和容量未提供，本例只表达逻辑接口候选；上线前仍需基础设施分析", "status": "needs-input"}, "security": {"reason": "安全与隐私要求未提供，保留待评审输入；不宣称安全充分", "status": "needs-input"}} |
| recovery_contract | {"central_receiver_ref": "APP-STOCK", "durable_ack": "记录持久成功后才答复受理；故障窗口与可接受丢失量待验证", "interface_ref": "IF-RECOVERY", "local_record_ref": "LOCAL-ORDER-RECORD", "policy": {"capability_id": "CAP-RESERVE", "confirmation": "central-atomic-reservation-only", "logistics_entry": "ORDER-CONFIRMED", "max_pending_hours": 8, "offline_item_limit": 1, "origin": "explicit-fictional-business-material", "policy_id": "POLICY-STOCK", "policy_version": "v2", "real_business_approval": "not-granted"}, "reconciliation": "中央重验库存后确认；同事件不同订单隔离，运营人工逐笔核对", "replay": "按event_id/order_id去重；超过当前policy期限隔离", "rollback": "停止新的离线受理；保留本地记录与检查点，逐笔核对后恢复在线", "status": "fictional-design-evidenced-production-unverified", "verification_scenarios": ["断连仍能受理", "重连重放", "重复事件不重复生效", "库存不足转异常", "存储故障与丢失窗口", "恢复后长期未对账", "停止离线受理并回退"]} |
| decision_agenda | [{"evidence": ["CASE-MANDATE", "CASE-BASELINE"], "goal": "打通线上订单、门店库存和物流履约", "id": "DEC-STRATEGY", "needed_input": ["渠道价值/服务目标", "预算与人员工作量", "库存风险接受者"], "options": ["先在线试点后评估离线", "并行验证在线与离线方案"], "question": "先受控试点还是扩大渠道承诺范围？", "role_ref": "ROLE-CHIEF", "status": "pending-decision", "tradeoff": "并行可提前暴露离线风险但增加设计、门店改造与运行投入；成本收益未估算"}, {"evidence": ["FICTIONAL-POLICY"], "id": "DEC-CROSS-SEGMENT", "needed_input": ["实际责任人签认与工程验证"], "proposed_boundary": "订单区分受理与最终确认；库存提供承诺条件；物流仅使用已确认订单；异常与恢复责任待确认", "question": "订单、库存、物流之间由谁承诺和接受风险？", "role_ref": "ROLE-EA", "status": "fictional-policy-provided-real-approval-not-granted"}, {"evidence": ["FICTIONAL-POLICY"], "id": "DEC-STOCK", "needed_input": ["实际责任人签认与工程验证"], "proposed_boundary": "待确认记录与可履约记录分开；冲突进入异常处理，不把异步等同于避免超卖", "question": "允许怎样的库存、断连及恢复行为？", "role_ref": "ROLE-SEG", "status": "fictional-policy-provided-real-approval-not-granted"}] |
| policy | {"capability_id": "CAP-RESERVE", "confirmation": "central-atomic-reservation-only", "logistics_entry": "ORDER-CONFIRMED", "max_pending_hours": 8, "offline_item_limit": 1, "origin": "explicit-fictional-business-material", "policy_id": "POLICY-STOCK", "policy_version": "v2", "real_business_approval": "not-granted"} |
| operations | {"escalation": "超额/过期隔离并人工联系，不自动发货", "max_pending_hours": 8, "owner": "虚构库存运营负责人", "pending_item_limit": 1} |
| validation_scenarios | [{"accept_quantity": 1, "exception_quantity": 2, "id": "TEST-LIMIT", "policy_version": "v2"}, {"boundary_hours": 8, "id": "TEST-EXPIRY", "policy_version": "v2"}, {"expect": "同事件同订单幂等，不同订单隔离", "id": "TEST-DUPLICATE", "policy_version": "v2"}, {"expect": "只允许确认订单进入物流", "id": "TEST-FULFIL", "policy_version": "v2"}] |
| decision | {"approval": "not-granted", "basis": "fictional 1000-request experiment; p95 A160/B420 vs target300; both central no-overcommit", "offline": "received-pending-central-confirmation", "scope": "online pilot only", "selected_online_option": "A-central-synchronous", "unproven": ["production latency", "cost", "scaling"]} |
| 证据 | ["CASE-REVIEW"] |
| 确定性 | assumed |


表达位置见 [delivery-notebook.coverage.json](delivery-notebook.coverage.json)。
