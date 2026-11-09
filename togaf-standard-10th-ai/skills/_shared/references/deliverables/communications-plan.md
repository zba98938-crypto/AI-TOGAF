# 沟通计划（Communications Plan）

ID：`communications-plan` · 主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md) · 常用 ADM：A G H。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **对象与关注点**：分组识别沟通受众及决策需要。
- **内容与渠道**：定义消息、视图、渠道及频率。
- **责任与反馈**：记录发送方、反馈和升级路径。

## 组装与引用

- [利益相关者目录](../artifacts/stakeholder-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 生成计划不授权实际发信。
- 不同受众视图追溯同一模型。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-communications-plan",
  "deliverable_id": "communications-plan",
  "title": "沟通计划 · 星河零售虚构案例",
  "view_ids": [
    "v-stakeholder-catalog"
  ],
  "entity_ids": [
    "stakeholder",
    "communication"
  ],
  "sections": {
    "对象与关注点": "业务发起方关注价值，履约团队关注流程，实施团队关注契约及切换。",
    "内容与渠道": "每次架构增量分别提供愿景、流程和接口视图，渠道由项目确定。",
    "责任与反馈": "架构负责人组织评审，记录反馈与未决项；本成果不发送任何消息。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable communications-plan --out ./architecture-output --render
```

## 来源

G248, G176, G184, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.12. Communications Plan](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_12)
  - 概念：沟通计划的条目标题。
  - 边界：目的和内容在子节。
