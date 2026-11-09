# 候选应用边界与责任

**虚构验收案例，不代表真实企业事实。**

制品：应用组合目录（Application Portfolio Catalog） · 模型 1 · 视图 `application-catalog`

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

- 库存一致性、承诺和恢复目标未明确，方案不能定优；影响：接口、风险及试点进入条件未定；需要：业务接受标准与服务水平。

- 门店在线销售与中央库存的当前交互尚未调查；影响：不能由线上订单接口推断门店在线行为；需要：门店在线流程、接口与失败处理材料。

- 已确认订单交给物流的具体接口和责任未提供；影响：只明确确认前不进入物流，交接规格待定；需要：物流接收契约与责任方。

- 原教学输入称专家4级但现有行为证据不足，当前等级保持未评价；影响：不能仅凭专家头衔确认支持能力；需要：任务相关的广泛经验、实际应用与评审证据。

方法检查：

- 产品名称不能替代应用边界。
- 候选退役不是已批准决策。

这些检查是评审问题，生成文件不自动表示已通过业务评审。

## 逐字段表达

表格按所选对象类型分组；相邻行不表示依赖或包含。嵌套字段保持结构化原值。

### application

| ID | 类型 | 名称 | owner | lifecycle | criticality | cost | version | 证据 | 确定性 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APP-ORDER | application | 线上订单应用 | 订单分段 | 候选目标 | 待业务评价 | 待估算 | 候选v1 | ["CASE-REVIEW"] | assumed |
| APP-STORE | application | 门店销售应用 | 门店运营 | 候选目标 | 待业务评价 | 待估算 | 候选v1 | ["CASE-REVIEW"] | assumed |
| APP-STOCK | application | 库存服务 | 库存分段 | 候选目标 | 待业务评价 | 待估算 | 候选v1 | ["CASE-REVIEW"] | assumed |


表达位置见 [application-catalog.coverage.json](application-catalog.coverage.json)。
