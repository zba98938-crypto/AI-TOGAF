# MSA双轨治理与豁免过程

主责 `togaf-technology-architecture`；既有制品 `microservice-technical-guidance`；视图规范 `msa-federated-governance-process`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚维修由业务赞助人审视投资价值，IT负责人要求生产访问和变更受控，EA委员会决定标准豁免。预约团队临时共享数据库的申请EX-1未获决定。项目架构师与团队拟在每次发布前四眼复核、最小权限保护管道、自动测试和持续监控。项目会议明确MSA控制支持IT治理；决策对齐EA；MSA过程扩展EA细节；EA规则约束MSA。此四关系是本项目映射，不是原图逐边转录。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| authority | 对该层决策负责的主体 |
| roles | 五类角色职责摘要，源表5-1 |
| decision | 治理实际决策/请求 |
| decision_status | 计划/待决等业务状态 |
| waiver | 请求/状态/决定证据/批准方 |
| controls | 可执行控制活动 |
| feedback | 持续监督/纠偏 |
| scope | 应用范围及时间 |
| mapping_origin | 项目映射与来源图分离 |
| evidence_detail | 决策证据或缺口 |

## 分析与质量检查

1. 界定企业护栏和MSA专属决定两条轨道
2. 区分五类角色职责与请求/决定权限
3. 核对每次发布控制和持续反馈
4. 偏离需显式申请并以委员会决定为准
5. 支持/对齐/扩展/约束分别记录方向

- 待决豁免不能被采用为已批准
- 四种关系不得统一为泛化依赖
- 治理有执行/反馈过程
- 项目图关系不冒称源图核实

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G21I §5.3、表5-1、§12.2
- G21I图5-3是SOA参考模型；不作为完成的MSA标准模型。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile msa-federated-governance-process --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
