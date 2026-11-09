# 业务目标与目的（Business Goals and Objectives）

ID：`business-goals-objectives` · 主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md) · 常用 ADM：A B。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **目标体系**：区分目标层次及业务范围。
- **可衡量目的**：定义指标、目标值、期限及责任。
- **架构贡献**：关联能力、服务和收益假设。

## 组装与引用

- [驱动因素/目标/目的目录](../artifacts/driver-goal-objective-catalog.md)。
- [目标/目的/服务图](../artifacts/goal-objective-service-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 量化目标具备基线单位和期限。
- 贡献关系不等于已实现因果。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-business-goals-objectives",
  "deliverable_id": "business-goals-objectives",
  "title": "业务目标与目的 · 星河零售虚构案例",
  "view_ids": [
    "v-driver-goal-objective-catalog",
    "v-goal-objective-service-diagram"
  ],
  "entity_ids": [
    "metric",
    "goal",
    "objective"
  ],
  "sections": {
    "目标体系": "增长驱动改善履约体验，细化为缩短订单确认时间。",
    "可衡量目的": "示例基线 20 分钟，目标 5 分钟，试运行结束评估，由履约负责人负责。",
    "架构贡献": "订单、库存和交付能力支持目标，相关性尚未构成已证实因果。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable business-goals-objectives --out ./architecture-output --render
```

## 来源

G248, G176, G233，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`split-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.9. Business Principles, Business Goals, and Business Drivers](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_09)
  - 概念：业务原则、目标和驱动的条目标题。
  - 边界：上下文目的及内容差异在子节。
