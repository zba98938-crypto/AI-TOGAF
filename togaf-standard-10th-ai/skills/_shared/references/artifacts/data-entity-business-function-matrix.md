# 数据实体/业务功能矩阵（Data Entity/Business Function Matrix）

ID：`data-entity-business-function-matrix` · 主责：[togaf-information-data](../../../togaf-information-data/SKILL.md) · 原文域：业务、数据。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

哪些功能创建、读取、更新或删除哪些数据？

主要受众：业务信息和数据负责人、数据及应用架构师。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `data_entity`：名称、边界、来源及对象类型。
- `function`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `used_in_function`：功能对数据操作，code 为列功能执行的 CRUD。data_entity → function。

行：data_entity；列：function。模型关系从行到列。单元含义：列功能对行数据实体执行的 CRUD；关系仍从行实体到列功能；允许代码：C, R, U, D；空白：未记录，不能直接解释为不存在。同一单元可有多个有依据的代码。

## 分析与构造

1. 确定业务数据实体与功能粒度。
2. 逐项核实 CRUD 动作。
3. 检查权属与生命周期完整性。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- CRUD 动作主体是列功能。
- 不要求每个实体必须存在 D 操作。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[业务服务/功能目录](business-service-function-catalog.md)、[数据实体/数据组件目录](data-entity-data-component-catalog.md)、[应用/功能矩阵](application-function-matrix.md)、[应用/数据矩阵](application-data-matrix.md)、[业务足迹图](business-footprint-diagram.md)、[概念数据图](conceptual-data-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-data-entity-business-function-matrix",
  "artifact_id": "data-entity-business-function-matrix",
  "title": "数据实体/业务功能矩阵 · 星河零售虚构案例",
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
    "data-order",
    "fn-order"
  ],
  "relationship_ids": [
    "data-function"
  ],
  "analysis": "哪些功能创建、读取、更新或删除哪些数据？ 本视图限定订单履约改造范围，展示案例设定的数据实体/业务功能矩阵。确定业务数据实体与功能粒度；实际项目需由相关责任方核实。",
  "legend": "列功能对行数据实体执行的 CRUD；关系仍从行实体到列功能；单元代码：C,R,U,D；未记录不等于不存在。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact data-entity-business-function-matrix --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 523, 567；方法指南：G248, G190, G234。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.5.2. Data Entity/Business Function Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_04_02)
  - 概念：数据实体/业务职能矩阵支持数据归属、交换、差距及来源/记录/参考应用分析。
  - 逻辑：职能由有边界服务支持并通过流程实现；数据与所有组织关联。
  - 决策：按映射识别缺数据及明确数据责任和应用角色。
  - 边界：图中归属建议仍需真实组织接受；origin/record/reference不可混用。
