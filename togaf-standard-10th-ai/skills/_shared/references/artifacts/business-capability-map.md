# 业务能力地图（Business Capability Map）

ID：`business-capability-map` · 主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

企业能力范围、分解及差距集中在哪里？

主要受众：战略及投资决策方、能力负责人。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `capability`：`definition`、`level`、`category`、`score`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `decomposes`：整体分解为同类型部分。capability, function → capability, function。

## 分析与构造

1. 先定义能力边界与一致命名。
2. 以同层粒度分组并显式分解。
3. 按单一已定义量尺叠加热力指标。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`map`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。卡片位置只用于排版；分解或依赖由显式关系表示。热力颜色需量尺和实际评分依据。

## 质量与常见误读

- 颜色须有量尺及证据。
- 能力实例不能画成子能力。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

支撑交付物：[架构定义文档](../deliverables/architecture-definition-document.md)、[能力评估](../deliverables/capability-assessment.md)。

相关制品：[业务能力目录](business-capabilities-catalog.md)、[能力/组织矩阵](capability-organization-matrix.md)、[战略/能力矩阵](strategy-capability-matrix.md)、[价值流/能力矩阵](value-stream-capability-matrix.md)、[业务足迹图](business-footprint-diagram.md)、[组织地图](organization-map.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-business-capability-map",
  "artifact_id": "business-capability-map",
  "title": "业务能力地图 · 星河零售虚构案例",
  "context": {
    "domains": [
      "business",
      "data",
      "application",
      "technology"
    ],
    "landscape": "segment",
    "purpose": "project",
    "abstraction": "conceptual",
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
  "analysis": "一级履约能力分解到订单、库存和交付。同层是静态能力；没有真实评分，因此不叠加成熟度颜色。",
  "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact business-capability-map --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 511；方法指南：G248, G211, G233。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.3.5. Business Capability Map](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_02_05)
  - 概念：能力地图展示企业为达目的所需能力。
  - 逻辑：能力与企业目的关联。
  - 决策：核查需要的能力范围。
  - 边界：所需能力不表示已有实现或成熟等级。
- [C220 3.6.4.26. Business Capability Map](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_26)
  - 概念：能力地图显示目的所需能力，可分解子能力。
  - 逻辑：父子能力分解保持能力身份。
  - 决策：核对能力范围及分解。
  - 边界：分解不表示活动先后、人员等级或实现状态。
