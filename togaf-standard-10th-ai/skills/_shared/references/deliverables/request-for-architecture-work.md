# 架构工作请求（Request for Architecture Work）

ID：`request-for-architecture-work` · 主责：[togaf-change-value](../../../togaf-change-value/SKILL.md) · 常用 ADM：Preliminary H A。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **请求与动机**：描述发起方、业务问题和触发。
- **范围与约束**：初步界定目标、边界、时间和依赖。
- **预期成果**：提出决策问题、价值和交付建议。
- **受理与优先级**：记录受理方、候选优先级和下一步。

## 组装与引用

- [项目语境图](../artifacts/project-context-diagram.md)。
- [驱动因素/目标/目的目录](../artifacts/driver-goal-objective-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 工作请求不同于已承诺工作说明书。
- 优先级有裁决方。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-request-for-architecture-work",
  "deliverable_id": "request-for-architecture-work",
  "title": "架构工作请求 · 星河零售虚构案例",
  "view_ids": [
    "v-project-context-diagram",
    "v-driver-goal-objective-catalog"
  ],
  "entity_ids": [
    "driver",
    "stakeholder",
    "project"
  ],
  "sections": {
    "请求与动机": "业务发起方因跨渠道增长请求分析可靠订单履约方案。",
    "范围与约束": "初步范围为确认、库存和仓储交接，物流伙伴作为外部依赖。",
    "预期成果": "需要愿景、跨域目标、差距和路线图，重点回答价值与可行性问题。",
    "受理与优先级": "架构负责人受理并提出候选优先级；没有已批准预算承诺。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable request-for-architecture-work --out ./architecture-output --render
```

## 来源

G248, G186, G188，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.17. Request for Architecture Work](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_17)
  - 概念：架构工作请求的条目标题。
  - 边界：发起来源及高层内容在子节。
