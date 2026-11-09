# 逻辑数据图（Logical Data Diagram）

ID：`logical-data-diagram` · 主责：[togaf-information-data](../../../togaf-information-data/SKILL.md) · 原文域：数据。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

业务数据如何形成独立于具体产品的逻辑结构？

主要受众：业务信息和数据负责人、数据及应用架构师。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `logical_entity`：`attributes`、`key`、`normalization`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `logical_association`：逻辑实体关联。logical_entity → logical_entity。

## 分析与构造

1. 细化实体属性、标识和可选性。
2. 显式关联及两端基数。
3. 核查一致性和逻辑规范化选择。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`er`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。两端基数已确认才使用 ER 符号；未知时退为明确标注的关系图。

## 质量与常见误读

- 数据类型保持产品中立。
- 未知基数不能用默认一对多填充。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-logical-data-diagram",
  "artifact_id": "logical-data-diagram",
  "title": "逻辑数据图 · 星河零售虚构案例",
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
    "logical-customer",
    "logical-order"
  ],
  "relationship_ids": [
    "logical-assoc"
  ],
  "analysis": "逻辑实体分别使用客户标识和订单标识；订单包含客户引用。不绑定数据库产品，属性可选性仍需真实业务确认。",
  "legend": "采用 ER 基数：|| 恰一，o{ 零至多；数量来自虚构案例明确设定。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact logical-data-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 572；方法指南：G248, G190, G234, G21B。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.5.5. Logical Data Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_04_05)
  - 概念：逻辑数据图展示关键实体关系的逻辑视图。
  - 逻辑：细节与受众区别于业务概念图。
  - 决策：核查逻辑关系能支持设计关切。
  - 边界：本节未定义完整字段、基数或物理表规范。
