# 架构愿景（Architecture Vision）

ID：`architecture-vision` · 主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md) · 常用 ADM：A。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **问题与价值**：说明问题、受益方及预期价值。
- **范围与边界**：明确五维语境和不在范围项。
- **高层方案**：引用能力与解决方案概念及选项。
- **可行性与风险**：总结能力、就绪度、约束和假设。
- **成功与下一步**：给出可验证成功条件和架构工作建议。

## 组装与引用

- [利益相关者目录](../artifacts/stakeholder-catalog.md)。
- [项目语境图](../artifacts/project-context-diagram.md)。
- [解决方案概念图](../artifacts/solution-concept-diagram.md)。
- [收益图](../artifacts/benefits-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 愿景不冒充完整目标设计。
- 价值承诺有责任方和依据。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-vision",
  "deliverable_id": "architecture-vision",
  "title": "架构愿景 · 星河零售虚构案例",
  "view_ids": [
    "v-stakeholder-catalog",
    "v-project-context-diagram",
    "v-solution-concept-diagram",
    "v-benefits-diagram"
  ],
  "entity_ids": [
    "cap-fulfillment",
    "cap-order",
    "cap-stock",
    "cap-delivery",
    "goal",
    "stakeholder"
  ],
  "sections": {
    "问题与价值": "跨渠道增长使人工协调压力增加；客户和履约团队期望可靠快速确认。",
    "范围与边界": "范围包括订单确认与仓储交接；物流伙伴内部系统变更不在项目范围。",
    "高层方案": "候选方案为订单应用协调库存，通过接口提供可靠承诺。",
    "可行性与风险": "当前单节点、数据身份和权限存在待验证假设；技术采用就绪度未正式评分。",
    "成功与下一步": "示例成功目标为确认中位数从 20 降至 5 分钟，需真实基线及业务批准。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-vision --out ./architecture-output --render
```

## 来源

G248, G176, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.8. Architecture Vision](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_08)
  - 概念：架构愿景的条目标题。
  - 边界：目的及典型内容在子节。
