# 应用交互矩阵（Application Interaction Matrix）

ID：`application-interaction-matrix` · 主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md) · 原文域：应用。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

应用之间交换什么以及向谁发起交互？

主要受众：应用和业务功能负责人、集成及数据团队。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `application`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `communicates_with`：应用向另一应用发起通信。application → application。

行：application；列：application。模型关系从行到列。单元含义：行应用向列应用发起交互，单元保留接口或消息引用；允许代码：sync, async, batch；空白：未记录，不能直接解释为不存在。同一单元可有多个有依据的代码。

## 分析与构造

1. 按应用边界列轴。
2. 采集方向、接口和通信模式。
3. 识别高耦合和不可达依赖。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- 对称矩阵不能掩盖方向。
- 调用不自动等于数据所有权。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[应用组合目录](application-portfolio-catalog.md)、[应用/功能矩阵](application-function-matrix.md)、[应用/组织矩阵](application-organization-matrix.md)、[角色/应用矩阵](role-application-matrix.md)、[应用/数据矩阵](application-data-matrix.md)、[应用/技术矩阵](application-technology-matrix.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-application-interaction-matrix",
  "artifact_id": "application-interaction-matrix",
  "title": "应用交互矩阵 · 星河零售虚构案例",
  "context": {
    "domains": [
      "business",
      "data",
      "application",
      "technology"
    ],
    "landscape": "segment",
    "purpose": "project",
    "abstraction": "logical",
    "evolution": "target"
  },
  "entity_ids": [
    "app-oms",
    "app-stock"
  ],
  "relationship_ids": [
    "app-interaction"
  ],
  "analysis": "应用之间交换什么以及向谁发起交互？ 本视图限定订单履约改造范围，展示案例设定的应用交互矩阵。按应用边界列轴；实际项目需由相关责任方核实。",
  "legend": "行应用向列应用发起交互，单元保留接口或消息引用；单元代码：sync,async,batch；未记录不等于不存在。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact application-interaction-matrix --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 549；方法指南：G248, G21I, G248。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.6.6. Application Interaction Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_05_06)
  - 概念：应用交互矩阵表示应用通信，相当于接口目录/通信图的矩阵投影。
  - 逻辑：双轴均可含应用服务、逻辑组件和物理组件；分别为服务消费服务、逻辑通信逻辑、物理通信物理。
  - 决策：保留实体层次、端点及关系方向。
  - 边界：不同层次关系不可互换；空单元格不自动证明无交互。
