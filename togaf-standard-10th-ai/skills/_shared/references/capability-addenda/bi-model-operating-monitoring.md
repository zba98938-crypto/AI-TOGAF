# BI分析模型运营监控与处置

主责 `togaf-information-data`；既有制品 `bi-transition-architecture`；视图规范 `bi-model-operating-monitoring`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚M1/v0.1预测维修时长，影子试点供U2分析，不自动给客户承诺。服务经理要求每周看预测与实际耗时的绝对差中位数，单位分钟；没有实际值和合格阈值。故障类型标签质量未知。模型负责人收集准确性、输入分布、技术、安全、使用与人工改判信息。已知作业/数据失败先停止建议回人工；重训须版本测试和业务复核，不能自动投产。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| model_ref | 模型与版本 |
| business_use | 用途及人工/自动决策边界 |
| lifecycle | 生命周期、技术/业务责任和发布证据 |
| measure | 单位/时间/定义/依据/阈值/观测值 |
| data_quality | 样本与生产数据语义/质量 |
| monitoring | 准确性/漂移/技术/安全/使用多个关注点 |
| response | 触发/负责人/回退/再训练控制 |
| lineage | 数据特征模型消费与观测追溯 |
| evidence_detail | 项目监控约定与试验证据 |
| claim | 已测结果与候选方案分开 |

## 分析与质量检查

1. 由业务用途明确错误后果和运营责任
2. 选有项目依据的准确性/数据/技术/安全/使用观测
3. 给每指标单位、窗口、证据与阈值来源，未知保持未知
4. 按触发设计停止、人工回退、评审和新版本测试
5. 形成运行监控记录后再评审实际表现

- 未知阈值不能判模型通过
- 监测漂移不等于可自动重训投产
- 模型版本与数据/用途可追溯
- 监控包含处置责任和回退

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G238 表4-2高级分析模型工业化、运营平台；表4-3分析模型管理与监控
- 指南没有通用准确率/漂移阈值或训练算法。
- 本例项目指标不是TOGAF统一计算公式。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile bi-model-operating-monitoring --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
