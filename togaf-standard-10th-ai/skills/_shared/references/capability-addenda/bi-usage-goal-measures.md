# BI用途待办、目标与可追溯度量

主责 `togaf-requirements`；既有制品 `bi-requirements-profile`；视图规范 `bi-usage-goal-measures`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚运营总监赞助两用例：U1缺件预警辅助调度主管上门前复核与调拨，使用预约/库存/站点。项目11月目标一个已在生产采用、有负责人证据的自动化检查功能，基线零，尚未测量。U2预测维修时长辅助服务经理选窗口，故障标签质量未知，价值尚定性。赞助人按重复决策价值与数据可得性先做U1后做U2，没有数字权重/ROI公式。业务分析师和数据工程师设计、平台部署、运营产品负责人维护。客户联系方式不进看板。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| user | 现实业务用户/角色 |
| pain | 业务痛点 |
| decision | 要改善的决策 |
| business_objects | 先业务对象再技术数据 |
| sponsor | 业务/IT赞助 |
| goal_reference | 带ID/源行的参考目标，参考身份不可删 |
| metric | 单位/时间/基线/目标/观测/规则/依据 |
| priority_rationale | 价值和复杂性或数据可得性的明确理由 |
| priority_rule | 项目排序规则，不借TOGAF名义自定权重 |
| lifecycle | 从设计到维护的组织 |
| data_access | 访问/隐私限制 |
| evidence_detail | 项目访谈证据 |
| gap | 缺口与未验证结论 |

## 分析与质量检查

1. 从用户痛点提炼决策及业务对象
2. 连接参考目标，但另设有来源的项目度量
3. 让赞助人提供价值/复杂性排序规则并保留理由
4. 定义从设计到持续维护的责任
5. 检查测量结果和目标/方向不同

- 参考方向不是目标或达标
- 每指标有单位/时间/依据
- 无ROI公式则不计算
- 数据民主化不放开机密数据

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G238 §3.1阶段B、表4-1、表4-2
- 附带17目标完整参考表，不强制每个项目追求全部目标。
- 缺失G238配套需求表；不把本地16例当官方全集。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile bi-usage-goal-measures --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
