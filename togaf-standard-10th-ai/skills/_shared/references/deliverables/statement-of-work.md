# 架构工作说明书（Statement of Work）

ID：`statement-of-work` · 主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md) · 常用 ADM：A。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **背景与目标**：说明架构工作目的及成功条件。
- **范围与交付**：明确制品、深度、边界和验收。
- **方法与计划**：安排活动、资源、迭代和依赖。
- **治理与变更**：定义评审、责任、约束和变更流程。

## 组装与引用

- [项目语境图](../artifacts/project-context-diagram.md)。
- [利益相关者目录](../artifacts/stakeholder-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 不虚构工期预算和签署。
- 交付选择匹配决策需要。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-statement-of-work",
  "deliverable_id": "statement-of-work",
  "title": "架构工作说明书 · 星河零售虚构案例",
  "view_ids": [
    "v-project-context-diagram",
    "v-stakeholder-catalog"
  ],
  "entity_ids": [
    "stakeholder",
    "project",
    "wp-data",
    "wp-app"
  ],
  "sections": {
    "背景与目标": "工作目的是提出可靠订单确认方案并支撑范围和投资决策。",
    "范围与交付": "交付愿景、跨域视图、需求、差距和迁移建议；不承诺物流伙伴内部改造。",
    "方法与计划": "按关注点迭代，数据与接口优先，实际工期资源预算需另行确认。",
    "治理与变更": "业务发起方验收价值范围，架构负责人评审一致性，变更按记录裁决。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable statement-of-work --out ./architecture-output --render
```

## 来源

G248, G188, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.20. Statement of Architecture Work](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_20)
  - 概念：架构工作说明的条目标题。
  - 边界：工作范围、验收及典型内容在子节。
