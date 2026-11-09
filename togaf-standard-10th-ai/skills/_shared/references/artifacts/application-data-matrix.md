# 应用/数据矩阵（Application/Data Matrix）

ID：`application-data-matrix` · 主责：[togaf-information-data](../../../togaf-information-data/SKILL.md) · 原文域：应用、数据。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

应用对数据实体承担什么操作及管理职责？

主要受众：业务信息和数据负责人、数据及应用架构师。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `application`：名称、边界、来源及对象类型。
- `data_entity`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `accesses`：应用或处理访问数据。application, process → data_entity。

行：application；列：data_entity。模型关系从行到列。单元含义：行应用对列数据执行操作或承担管理职责；允许代码：C, R, U, D, owner；空白：未记录，不能直接解释为不存在。同一单元可有多个有依据的代码。

## 分析与构造

1. 确认应用和数据粒度。
2. 记录 CRUD 与权威来源。
3. 识别多写冲突和未管理数据。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- 复制数据不自动成为权威来源。
- owner 与 CRUD 分开解释。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[应用组合目录](application-portfolio-catalog.md)、[数据实体/数据组件目录](data-entity-data-component-catalog.md)、[应用/功能矩阵](application-function-matrix.md)、[应用/组织矩阵](application-organization-matrix.md)、[数据实体/业务功能矩阵](data-entity-business-function-matrix.md)、[角色/应用矩阵](role-application-matrix.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-application-data-matrix",
  "artifact_id": "application-data-matrix",
  "title": "应用/数据矩阵 · 星河零售虚构案例",
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
    "data-order",
    "data-customer"
  ],
  "relationship_ids": [
    "app-data",
    "app-customer"
  ],
  "analysis": "应用对数据实体承担什么操作及管理职责？ 本视图限定订单履约改造范围，展示案例设定的应用/数据矩阵。确认应用和数据粒度；实际项目需由相关责任方核实。",
  "legend": "行应用对列数据执行操作或承担管理职责；单元代码：C,R,U,D,owner；未记录不等于不存在。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact application-data-matrix --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 553, 564；方法指南：G248, G21B, G234。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.5.3. Application/Data Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_04_03)
  - 概念：应用/数据矩阵显示逻辑应用组件对数据实体的创建、读取、更新、删除关系。
  - 逻辑：两轴为Logical Application Component和Data Entity。
  - 决策：逐应用逐数据核查实际CRUD及重复更新。
  - 边界：不能给每个单元格默认完整CRUD；master/reference等数据分类不是自动一致性政策。
