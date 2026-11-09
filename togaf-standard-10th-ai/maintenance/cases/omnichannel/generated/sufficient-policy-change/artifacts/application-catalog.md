# 候选应用边界与责任

**虚构验收案例，不代表真实企业事实。**

制品：应用组合目录（Application Portfolio Catalog） · 模型 fictional-v2 · 视图 `application-catalog`

语境：`{"domains": ["business", "data", "application", "technology"], "landscape": "segment", "purpose": "project", "abstraction": "logical", "evolution": "target"}`

依据虚构材料表达候选设计；证据不足的结论保留缺口。

完整对象字段及关系见下方“模型表达”表；按视图规范选择记录式或行式布局。


图例／解释：虚构教学案例；稳定ID跨视图复用。候选设计和项目规则不表示官方模板或业务批准。


证据与缺口：

| 对象 | 来源 | 确定性 |
| --- | --- | --- |
| APP-ORDER | CASE-REVIEW | assumed |
| APP-STORE | CASE-REVIEW | assumed |
| APP-STOCK | CASE-REVIEW | assumed |

- 门店在线销售与中央库存的当前交互尚未调查；影响：不能由线上订单接口推断门店在线行为；需要：门店在线流程、接口与失败处理材料。

- 已确认订单交给物流的具体接口和责任未提供；影响：只明确确认前不进入物流，交接规格待定；需要：物流接收契约与责任方。

- 最大断连时间未知；影响：阻断离线候选方案接受与运营状态进入；需要：断连上限与存储容量依据。

- 可容忍的数据丢失窗口未知；影响：阻断离线候选方案接受与运营状态进入；需要：持久成功标准、故障演练与数据丢失容忍。

- 冲突、补偿与回退责任待确认；影响：阻断离线候选方案接受与运营状态进入；需要：业务与运营责任人的交接接受记录。

方法检查：

- 产品名称不能替代应用边界。
- 候选退役不是已批准决策。

这些检查是评审问题，生成文件不自动表示已通过业务评审。

## 逐字段表达

表格按所选对象类型分组；相邻行不表示依赖或包含。嵌套字段保持结构化原值。

### application

| ID | 类型 | 名称 | owner | lifecycle | criticality | cost | version | 证据 | 确定性 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APP-ORDER | application | 线上订单应用 | 订单分段 | 候选目标 | 待业务评价 | 待估算 | 候选v2 | ["CASE-REVIEW"] | assumed |
| APP-STORE | application | 门店销售应用 | 门店运营 | 候选目标 | 待业务评价 | 待估算 | 候选v2 | ["CASE-REVIEW"] | assumed |
| APP-STOCK | application | 库存服务 | 库存分段 | 候选目标 | 待业务评价 | 待估算 | 候选v2 | ["CASE-REVIEW"] | assumed |


表达位置见 [application-catalog.coverage.json](application-catalog.coverage.json)。
