# 业务原则（Business Principles）

ID：`business-principles` · 主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md) · 常用 ADM：Preliminary A。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **业务语境**：明确业务价值及适用边界。
- **原则与影响**：说明业务决策原则、理由和组织影响。
- **执行与例外**：明确业务责任、冲突及复审。

## 组装与引用

- [原则目录](../artifacts/principles-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 业务原则不写成产品标准。
- 区分业务政策与架构约束。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-business-principles",
  "deliverable_id": "business-principles",
  "title": "业务原则 · 星河零售虚构案例",
  "view_ids": [
    "v-principles-catalog"
  ],
  "entity_ids": [
    "principle"
  ],
  "sections": {
    "业务语境": "本业务关注可靠承诺与客户权益，适用于订单履约。",
    "原则与影响": "统一客户标识与最小必要信息共同约束数据使用，不能仅靠工具解决。",
    "执行与例外": "业务负责人裁决体验与控制冲突，例外必须有范围、期限和风险责任。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable business-principles --out ./architecture-output --render
```

## 来源

G248, G184, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`split-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.9. Business Principles, Business Goals, and Business Drivers](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_09)
  - 概念：业务原则、目标和驱动的条目标题。
  - 边界：上下文目的及内容差异在子节。
