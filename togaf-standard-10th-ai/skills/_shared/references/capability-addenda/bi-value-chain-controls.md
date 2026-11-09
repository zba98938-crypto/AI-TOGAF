# BI数据价值链、语义与控制

主责 `togaf-information-data`；既有制品 `bi-transition-architecture`；视图规范 `bi-value-chain-controls`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚U1读取库存应用。每批原始库存保存不变；TECH-1只统一日期类型，异常隔离。BUS-1以需求量大于可用量识别候选缺件；业务视图经SEM-1解释时点/站点，调度人复核后调拨。库存源及时性未测；看板显示观测时间，过期转人工。每层保留批次/规则/用途血缘和负责人；不进入客户联系方式。流程是项目设计，非强制所有项目有五层。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| layer_kind | source/raw/prepared/information/business-view语义 |
| input_refs | 输入ID/明确外部来源 |
| transformation_rule | 技术/业务/语义规则及版本 |
| business_purpose | 该层服务用途 |
| owner | 业务或技术责任 |
| quality_controls | 质量和失败处理 |
| protection_controls | 访问、隐私与保留规则 |
| metadata_lineage | 数据/规则/作业/用途血缘 |
| scope | 数据和时点范围 |
| reference_identity | 项目裁剪，非强制部署模式 |
| evidence_detail | 访谈/规则/试验定位 |

## 分析与质量检查

1. 从业务决策反推数据和语义
2. 逐层区分原始、技术准备和业务信息转换
3. 记录输入输出及有向派生关系
4. 检查质量、安全、元数据和运营责任贯穿全链
5. 不因价值链存在就认定数据正确/及时

- 原始层不得修改源内容
- 有向关系和input_refs一致
- 技术规则与业务规则分开
- 每层有质量/保护/血缘责任

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G238 表4-2价值链设计、表4-3存储/处理/监控
- 关系表完整表达流向；对应图形布局仍由来源图规范单独验证。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile bi-value-chain-controls --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
