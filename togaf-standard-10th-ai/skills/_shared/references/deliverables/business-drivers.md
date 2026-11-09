# 业务驱动因素（Business Drivers）

ID：`business-drivers` · 主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md) · 常用 ADM：A。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **驱动因素**：描述外部或内部变化及证据。
- **业务影响**：分析机会、威胁和时限。
- **目标响应**：关联目标与架构工作的必要性。

## 组装与引用

- [驱动因素/目标/目的目录](../artifacts/driver-goal-objective-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 驱动不是期望结果。
- 市场或法规陈述有来源日期。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-business-drivers",
  "deliverable_id": "business-drivers",
  "title": "业务驱动因素 · 星河零售虚构案例",
  "view_ids": [
    "v-driver-goal-objective-catalog"
  ],
  "entity_ids": [
    "driver",
    "goal"
  ],
  "sections": {
    "驱动因素": "案例设定跨渠道订单增长；这是虚构输入，不是市场事实。",
    "业务影响": "增长增加人工协调和库存冲突风险，下一季度试运行窗口为示例约束。",
    "目标响应": "因此提出可靠订单确认与协同履约目标，而非直接指定采购产品。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable business-drivers --out ./architecture-output --render
```

## 来源

G248, G176, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`split-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.9. Business Principles, Business Goals, and Business Drivers](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_09)
  - 概念：业务原则、目标和驱动的条目标题。
  - 边界：上下文目的及内容差异在子节。
