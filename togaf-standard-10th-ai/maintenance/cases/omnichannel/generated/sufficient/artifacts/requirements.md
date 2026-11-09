# 需求与未决接受条件

**虚构验收案例，不代表真实企业事实。**

制品：需求目录（Requirements Catalog） · 模型 fictional-v1 · 视图 `requirements`

语境：`{"domains": ["business", "data", "application", "technology"], "landscape": "segment", "purpose": "project", "abstraction": "logical", "evolution": "target"}`

依据虚构材料表达候选设计；证据不足的结论保留缺口。

完整对象字段及关系见下方“模型表达”表；按视图规范选择记录式或行式布局。


图例／解释：虚构教学案例；稳定ID跨视图复用。候选设计和项目规则不表示官方模板或业务批准。


证据与缺口：

| 对象 | 来源 | 确定性 |
| --- | --- | --- |
| REQ-CONSISTENCY | CASE-REVIEW | assumed |
| REQ-OFFLINE | CASE-CHANGE, CASE-REVIEW | assumed |

- 门店在线销售与中央库存的当前交互尚未调查；影响：不能由线上订单接口推断门店在线行为；需要：门店在线流程、接口与失败处理材料。

- 已确认订单交给物流的具体接口和责任未提供；影响：只明确确认前不进入物流，交接规格待定；需要：物流接收契约与责任方。

- 最大断连时间未知；影响：阻断离线候选方案接受与运营状态进入；需要：断连上限与存储容量依据。

- 可容忍的数据丢失窗口未知；影响：阻断离线候选方案接受与运营状态进入；需要：持久成功标准、故障演练与数据丢失容忍。

- 冲突、补偿与回退责任待确认；影响：阻断离线候选方案接受与运营状态进入；需要：业务与运营责任人的交接接受记录。

方法检查：

- 目标与解决方案不要混写成需求。
- 未确认需求保留候选状态。

这些检查是评审问题，生成文件不自动表示已通过业务评审。

## 逐字段表达

表格按所选对象类型分组；相邻行不表示依赖或包含。嵌套字段保持结构化原值。

### requirement

| ID | 类型 | 名称 | statement | priority | owner | acceptance | status | source_role | 证据 | 确定性 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-CONSISTENCY | requirement | 库存一致性与承诺标准待明确 | 中央原子预占后才确认，总承诺不得超过可用；线上确认p95≤300ms | 待排序 | 库存业务负责人 | 固定虚构1000请求集：不超量且确认p95≤300ms | fictional-input-provided | 未提供 | ["CASE-REVIEW"] | assumed |
| REQ-OFFLINE | requirement | 门店断连仍可受理销售 | 离线仅持久受理待中央确认，限量及期限按POLICY-STOCK | 新增约束 | 门店运营 | 额度、超时、重放、冲突及回退演练 | fictional-input-provided | stated-fictional-requirement | ["CASE-CHANGE", "CASE-REVIEW"] | assumed |


表达位置见 [requirements.coverage.json](requirements.coverage.json)。
