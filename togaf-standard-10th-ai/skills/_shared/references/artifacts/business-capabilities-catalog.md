# 业务能力目录（Business Capabilities Catalog）

ID：`business-capabilities-catalog` · 主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

企业需要具备哪些稳定的业务能力？

主要受众：战略及投资决策方、能力负责人。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `capability`：`definition`、`owner`、`level`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `decomposes`：整体分解为同类型部分。capability, function → capability, function。

## 分析与构造

1. 按业务对象与业务结果命名。
2. 建立不依赖组织或系统的分解。
3. 用业务专家验证覆盖与边界。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- 能力不是流程步骤。
- 同一能力的实例不应作为子能力。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[能力/组织矩阵](capability-organization-matrix.md)、[战略/能力矩阵](strategy-capability-matrix.md)、[价值流/能力矩阵](value-stream-capability-matrix.md)、[业务能力地图](business-capability-map.md)、[业务足迹图](business-footprint-diagram.md)、[组织地图](organization-map.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-business-capabilities-catalog",
  "artifact_id": "business-capabilities-catalog",
  "title": "业务能力目录 · 星河零售虚构案例",
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
    "cap-fulfillment",
    "cap-order",
    "cap-stock",
    "cap-delivery"
  ],
  "relationship_ids": [
    "cap-child-order",
    "cap-child-stock",
    "cap-child-delivery"
  ],
  "analysis": "企业需要具备哪些稳定的业务能力？ 本视图限定订单履约改造范围，展示案例设定的业务能力目录。按业务对象与业务结果命名；实际项目需由相关责任方核实。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact business-capabilities-catalog --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 510；方法指南：G248, G211, G233。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.4.8. Business Capabilities Catalog](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_08)
  - 概念：业务能力目录列为特定目的可能拥有的能力。
  - 逻辑：能力与目的关联。
  - 决策：据定义辨别能力身份。
  - 边界：may possess不证明组织现有能力已实现。
