# 价值流/能力矩阵（Value Stream/Capability Matrix）

ID：`value-stream-capability-matrix` · 主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

哪些能力使能哪些价值流或阶段？

主要受众：价值流负责人、触发方代表、跨职能能力负责人。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `value_stream`：名称、边界、来源及对象类型。
- `value_stage`：名称、边界、来源及对象类型。
- `capability`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `enabled_by`：价值流或阶段由能力使能。value_stream, value_stage → capability。

行：value_stream, value_stage；列：capability。模型关系从行到列。单元含义：列能力使能行价值流或阶段；允许代码：enables；空白：未记录，不能直接解释为不存在。同一单元可有多个有依据的代码。

## 分析与构造

1. 逐阶段走查价值交付。
2. 只选择直接支撑的能力层级。
3. 叠加有依据的差距或绩效指标。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- 能力多次出现是复用。
- 颜色未定义时不能解释为成熟度。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[业务能力目录](business-capabilities-catalog.md)、[价值流目录](value-stream-catalog.md)、[价值流阶段目录](value-stream-stages-catalog.md)、[能力/组织矩阵](capability-organization-matrix.md)、[战略/能力矩阵](strategy-capability-matrix.md)、[业务能力地图](business-capability-map.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-value-stream-capability-matrix",
  "artifact_id": "value-stream-capability-matrix",
  "title": "价值流/能力矩阵 · 星河零售虚构案例",
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
    "stage-order",
    "cap-order",
    "cap-stock",
    "stage-deliver",
    "cap-delivery"
  ],
  "relationship_ids": [
    "stage-cap-order",
    "stage-cap-stock",
    "stage-cap-delivery"
  ],
  "analysis": "哪些能力使能哪些价值流或阶段？ 本视图限定订单履约改造范围，展示案例设定的价值流/能力矩阵。逐阶段走查价值交付；实际项目需由相关责任方核实。",
  "legend": "列能力使能行价值流或阶段；单元代码：enables；未记录不等于不存在。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact value-stream-capability-matrix --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 546；方法指南：G248, G178, G233。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.4.14. Value Stream/Capability Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_14)
  - 概念：价值流/能力矩阵显示每一阶段所需能力。
  - 逻辑：阶段到能力的需要关系。
  - 决策：检查阶段是否缺能力支持。
  - 边界：需要关系不证明能力实例已经实现阶段结果。
