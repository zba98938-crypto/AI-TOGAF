# 能力评估（Capability Assessment）

ID：`capability-assessment` · 主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md) · 常用 ADM：A B E。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **评估目的**：声明业务能力、EA 成熟度或采用就绪度的评估对象。
- **量尺与证据**：列出维度、评分解释、证据及置信度。
- **现状与目标**：比较同尺度差距并记录分歧。
- **改进行动**：给出优先级、责任和复评安排。

## 组装与引用

- [业务能力地图](../artifacts/business-capability-map.md)。
- [能力/组织矩阵](../artifacts/capability-organization-matrix.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 三类量尺不能混算。
- 示例模型没有通用及格线。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-capability-assessment",
  "deliverable_id": "capability-assessment",
  "title": "能力评估 · 星河零售虚构案例",
  "view_ids": [
    "v-business-capability-map",
    "v-capability-organization-matrix"
  ],
  "entity_ids": [
    "cap-fulfillment",
    "cap-order",
    "cap-stock",
    "cap-delivery",
    "assessment"
  ],
  "sections": {
    "评估目的": "评估订单、库存和交付业务能力；不混用 EA 成熟度或数字采用就绪度。",
    "量尺与证据": "当前只有虚构情景，重要性与绩效需分别访谈评分，地图未着热力色。",
    "现状与目标": "已知示例差距是人工协调和单节点限制；真实绩效与目标等级待确认。",
    "改进行动": "先验证数据与接口，再迁移订单服务，最后用业务指标复评。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable capability-assessment --out ./architecture-output --render
```

## 来源

G248, G211, G203, G212, G233，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.10. Capability Assessment](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_10)
  - 概念：能力评估的条目标题。
  - 边界：评估层次、目的和内容在子节。
