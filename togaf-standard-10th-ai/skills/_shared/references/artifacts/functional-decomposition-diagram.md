# 功能分解图（Functional Decomposition Diagram）

ID：`functional-decomposition-diagram` · 主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

业务功能如何分解为一致边界的子功能？

主要受众：业务及流程负责人、服务消费者、执行与控制角色。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `function`：`definition`、`level`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `decomposes`：整体分解为同类型部分。capability, function → capability, function。

## 分析与构造

1. 确定功能分类依据。
2. 逐层进行整体到部分分解。
3. 检查同层覆盖与重叠。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`map`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。卡片位置只用于排版；分解或依赖由显式关系表示。热力颜色需量尺和实际评分依据。

## 质量与常见误读

- 分解线不表示执行顺序。
- 功能树不等于组织层级。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[业务服务/功能目录](business-service-function-catalog.md)、[应用/功能矩阵](application-function-matrix.md)、[数据实体/业务功能矩阵](data-entity-business-function-matrix.md)、[业务足迹图](business-footprint-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-functional-decomposition-diagram",
  "artifact_id": "functional-decomposition-diagram",
  "title": "功能分解图 · 星河零售虚构案例",
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
    "fn-order",
    "fn-validate"
  ],
  "relationship_ids": [
    "fn-child"
  ],
  "analysis": "业务功能如何分解为一致边界的子功能？ 本视图限定订单履约改造范围，展示案例设定的功能分解图。确定功能分类依据；实际项目需由相关责任方核实。",
  "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact functional-decomposition-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 526；方法指南：G248, G248, G233。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.4.19. Functional Decomposition Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_19)
  - 概念：职能分解图在一页表达相关组织能力的职能视角。
  - 逻辑：可叠热图表示变革范围与分期决定。
  - 决策：先分解职能，再按证据叠加范围/决定。
  - 边界：文本使用capabilities不证明职能与能力实体同一，热图不自动生成无依据评级。
