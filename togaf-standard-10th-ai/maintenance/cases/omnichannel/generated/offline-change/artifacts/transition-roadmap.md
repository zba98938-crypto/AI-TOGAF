# 候选运营过渡与工作包

**虚构验收案例，不代表真实企业事实。**

制品：过渡架构模型（Transition Architecture Model） · 模型 2 · 视图 `transition-roadmap`

语境：`{"domains": ["business", "data", "application", "technology"], "landscape": "segment", "purpose": "project", "abstraction": "logical", "evolution": "target"}`

依据虚构材料表达候选设计；证据不足的结论保留缺口。

| ID | 类型 | 名称 | 属性 |
| --- | --- | --- | --- |
| WP-ONLINE | work_package | 在线试点准备 | {"owner": "方案团队", "start": "2026-11-09", "end": "2026-11-20", "status": "候选；日期仅教学计划"} |
| TRANS-ONLINE | transition | 受控在线试点 | {"definition": "保留在线同步与异步两种候选，等待业务一致性要求", "operating_conditions": {"operations": "试点值守及人工异常处理", "data_consistency": "待业务定义", "dependencies": "接口验证及库存业务接受标准", "controls": "重复请求识别与审计待验证", "rollback": "停止新试点订单，保留存量记录并对账"}, "ordinal": 1, "start": "2026-11-09", "end": "2026-11-20"} |
| WP-OFFLINE | work_package | 断连与恢复演练 | {"owner": "方案团队", "start": "2026-11-21", "end": "2026-12-04", "status": "候选；日期仅教学计划", "source_role": "authored-design-candidate"} |
| TRANS-OFFLINE | transition | 断连受理与恢复对账试点 | {"definition": "条件满足后增加离线受理，不预先承诺超卖或恢复指标", "operating_conditions": {"operations": "断连订单和异常补偿责任待确认", "data_consistency": "本地额度、中央冲突与重放幂等待业务接受", "dependencies": "持久记录、恢复接口及冲突演练", "controls": "检查点、审计及重放去重", "rollback": "停止离线受理，保留队列，逐笔对账后恢复在线"}, "ordinal": 2, "start": "2026-11-21", "end": "2026-12-04", "source_role": "authored-design-candidate"} |

![过渡架构模型](transition-roadmap.svg)

独立图片：[transition-roadmap.png](transition-roadmap.png)。可编辑源与模型见同目录。

图例／解释：虚构教学案例；稳定ID跨视图复用。候选设计和项目规则不表示官方模板或业务批准。

| 关系 ID | 起点 | 语义 | 终点 | 说明 | 属性／代码／端基数 | 证据／确定性 |
| --- | --- | --- | --- | --- | --- | --- |
| WP-TO-ONLINE | WP-ONLINE | implements_transition | TRANS-ONLINE | 准备运营状态 | {"attributes": {}} | CASE-REVIEW / assumed |
| WP-TO-OFFLINE | WP-OFFLINE | implements_transition | TRANS-OFFLINE | 验证后进入候选运营状态 | {"attributes": {}} | CASE-CHANGE, CASE-REVIEW / assumed |
| WP-DEP | WP-OFFLINE | depends_on | WP-ONLINE | 依赖已验证的在线契约 | {"attributes": {}} | CASE-CHANGE, CASE-REVIEW / assumed |


证据与缺口：

| 对象 | 来源 | 确定性 |
| --- | --- | --- |
| WP-ONLINE | CASE-REVIEW | assumed |
| TRANS-ONLINE | CASE-REVIEW | assumed |
| WP-OFFLINE | CASE-CHANGE, CASE-REVIEW | assumed |
| TRANS-OFFLINE | CASE-CHANGE, CASE-REVIEW | assumed |

- 库存一致性、承诺和恢复目标未明确，方案不能定优；影响：接口、风险及试点进入条件未定；需要：业务接受标准与服务水平。

- 门店在线销售与中央库存的当前交互尚未调查；影响：不能由线上订单接口推断门店在线行为；需要：门店在线流程、接口与失败处理材料。

- 已确认订单交给物流的具体接口和责任未提供；影响：只明确确认前不进入物流，交接规格待定；需要：物流接收契约与责任方。

- 最大断连时间未知；影响：阻断离线候选方案接受与运营状态进入；需要：断连上限与存储容量依据。

- 可容忍的数据丢失窗口未知；影响：阻断离线候选方案接受与运营状态进入；需要：持久成功标准、故障演练与数据丢失容忍。

- 恢复和对账服务目标未知；影响：阻断离线候选方案接受与运营状态进入；需要：恢复时限与未对账告警规则。

- 本地额度与超卖政策未定；影响：阻断离线候选方案接受与运营状态进入；需要：业务承诺、额度与冲突接受决定。

- 冲突、补偿与回退责任待确认；影响：阻断离线候选方案接受与运营状态进入；需要：业务与运营责任人的交接接受记录。

- ASSIGN-A只覆盖至2026-11-30，离线工作包候选结束2026-12-04；后半段配置未确定；影响：不能认定完整交付期有人员覆盖；工时与专家支持也未证明充分；需要：续任/替代人员、可用容量和工作量。

- 原教学输入称专家4级但现有行为证据不足，当前等级保持未评价；影响：不能仅凭专家头衔确认支持能力；需要：任务相关的广泛经验、实际应用与评审证据。

方法检查：

- 过渡架构不是仅有交付日期的里程碑。
- 必需属性具有明确值或被登记为阻断缺口。
- 来源与项目事实、参考内容、假设保持可区分。
- 结论回应本规范的决策问题并可追溯。

这些检查是评审问题，生成文件不自动表示已通过业务评审。

表达完整性见 [transition-roadmap.coverage.json](transition-roadmap.coverage.json)。来源结构模板的核实状态见布局文件；生成不改变该状态。
