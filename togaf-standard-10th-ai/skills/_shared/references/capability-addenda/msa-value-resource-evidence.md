# 微服务业务价值与开发运营资源

主责 `togaf-application-architecture`；既有制品 `microservice-value-catalog`；视图规范 `msa-value-resource-evidence`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚维修容量表CAP-11：试点已实现预约时段判断，一个ABF；11月开发已分配12人日、运营16人时，12月计划开发5人日、运营20人时。备件可用判断尚计划，11月两类资源为零分配；12月计划9开发人日，运营工时未知。预约服务关联WP-appointment/T-pilot，备件关联WP-parts/T-expanded（外部引用，非本例已定义架构状态）。尚无成本单价或ROI口径。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| service_status | 目录中的实际/计划状态 |
| ABF | 单原子业务功能 |
| value | 可由利益相关者理解的业务价值 |
| development_resources | allocated/planned各自value/unit/period |
| operations_resources | allocated/planned各自value/unit/period |
| owner | 生命周期责任方 |
| work_package_ref | 工作包外部引用 |
| architecture_state_ref | 相关过渡范围外部引用，不冒充v2 state_id |
| evidence_detail | 资源记录定位 |
| cost_and_return | 未知成本与未算ROI边界 |
| gap | 资源或价值证据不足 |

## 分析与质量检查

1. 区分已实现和计划服务
2. 逐服务确认一个ABF与业务价值
3. 开发/运营及已分配/计划四格分开记录单位时段
4. 关联工作包及命名过渡，检查运营计划缺口
5. 成本或ROI规则未提供则不计算

- 四格都存在；unknown不等于0
- 人日与人时不无规则相加
- 未来计划不改为已分配
- 不自创成本率或ROI公式

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G21I §11.3、§12.1
- 本例工作包/过渡ID为明确外部引用；完整工作包或过渡架构由既有规范组装。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile msa-value-resource-evidence --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
