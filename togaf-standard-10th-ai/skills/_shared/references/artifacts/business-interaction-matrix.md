# 业务交互矩阵（Business Interaction Matrix）

ID：`business-interaction-matrix` · 主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

哪些组织向哪些组织提供什么业务交互？

主要受众：业务及流程负责人、服务消费者、执行与控制角色。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `organization`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `business_interaction`：提供方向接收方交换服务或产品。organization → organization。

行：organization；列：organization。模型关系从行到列。单元含义：行组织向列组织提供的产品或服务；允许代码：exchange；空白：未记录，不能直接解释为不存在。同一单元可有多个有依据的代码。

## 分析与构造

1. 统一交互边界。
2. 记录提供方、接收方及交换内容。
3. 定位责任断点和循环依赖。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- 对角线需按业务边界解释。
- 方向不可由相邻位置推断。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[组织/参与者目录](organization-actor-catalog.md)、[应用/组织矩阵](application-organization-matrix.md)、[能力/组织矩阵](capability-organization-matrix.md)、[业务足迹图](business-footprint-diagram.md)、[组织分解图](organization-decomposition-diagram.md)、[组织地图](organization-map.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-business-interaction-matrix",
  "artifact_id": "business-interaction-matrix",
  "title": "业务交互矩阵 · 星河零售虚构案例",
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
    "org-sales",
    "org-warehouse"
  ],
  "relationship_ids": [
    "business-interaction"
  ],
  "analysis": "哪些组织向哪些组织提供什么业务交互？ 本视图限定订单履约改造范围，展示案例设定的业务交互矩阵。统一交互边界；实际项目需由相关责任方核实。",
  "legend": "行组织向列组织提供的产品或服务；单元代码：exchange；未记录不等于不存在。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact business-interaction-matrix --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 515；方法指南：G248, G206, G248。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.4.12. Business Interaction Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_12)
  - 概念：业务交互矩阵表达组织与职能的交互和依赖。
  - 逻辑：源列Organization、Function、Service及服务通信/依赖关系。
  - 决策：区分通信与依赖并核查交互事实。
  - 边界：源列表Organization用词与Organization Unit保持可追溯，不从空格推断无交互。
