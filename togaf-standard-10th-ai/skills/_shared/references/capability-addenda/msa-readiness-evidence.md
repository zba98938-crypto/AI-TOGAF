# MSA组织与生命周期就绪证据

主责 `togaf-technology-architecture`；既有制品 `microservice-technical-guidance`；视图规范 `msa-readiness-evidence`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚维修准备把预约判断拆为服务。预约团队负责开发、部署与值班，却没人负责退役。两开发一轮值运维未完成恢复演练。团队可选框架，但须满足生产最小权限和可追溯变更。有自动构建测试，发布前复核和变化监控仍手工。先在一城试点，复盘组织影响再扩另一城。没有OSIMM模型或评估结果，不能给总分。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| concern | 逐项就绪关注点 |
| observation | 实际观察/未取得材料 |
| judgment | 文字判断，不是成熟度分数 |
| owner | 行动责任 |
| action | 补证据和能力行动 |
| scope | 组织/服务/时点 |
| decision_consequence | 对试点/采用的限制 |
| scoring | scheme/score/basis，未提供模型时none/null |
| evidence_detail | 访谈或试验定位 |

## 分析与质量检查

1. 按单服务全过程检查归属、技能、自治、DevOps与试点学习
2. 分别记录已知、部分和未知，不按条数计成熟度
3. 将每个不足转为责任、行动和进入试点条件
4. OSIMM按独立来源调用，不用ACMM或项目表替代

- 六关注点保持独立
- 缺退休责任不得标全生命周期完整
- 未知OSIMM不填分数
- 自治仍受企业护栏约束

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G21I §5.2、§5.5、表5-1
- 这是项目就绪证据表，不是OSIMM实施或成熟度评分器。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile msa-readiness-evidence --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
