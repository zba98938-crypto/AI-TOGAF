# 架构原则（Architecture Principles）

ID：`architecture-principles` · 主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md) · 常用 ADM：Preliminary。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **适用语境**：界定范围及原则治理责任。
- **原则条目**：包括名称、陈述、理由和影响。
- **冲突与例外**：说明适用优先级、例外及复审机制。

## 组装与引用

- [原则目录](../artifacts/principles-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 原则具有可操作影响。
- 例外需明确裁决责任。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-principles",
  "deliverable_id": "architecture-principles",
  "title": "架构原则 · 星河零售虚构案例",
  "view_ids": [
    "v-principles-catalog"
  ],
  "entity_ids": [
    "principle"
  ],
  "sections": {
    "适用语境": "客户和订单跨渠道使用，原则由架构团队维护。",
    "原则条目": "客户标识统一管理：减少重复客户；实施需要匹配规则及业务责任。",
    "冲突与例外": "例外由数据负责人和架构负责人评审；未记录任何已批准例外。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-principles --out ./architecture-output --render
```

## 来源

G248, G184，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.4. Architecture Principles](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_04)
  - 概念：架构原则的条目标题。
  - 边界：原则性质与参考域在子节。
