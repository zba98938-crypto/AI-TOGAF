# 架构需求规格（Architecture Requirements Specification）

ID：`architecture-requirements-specification` · 主责：[togaf-requirements](../../../togaf-requirements/SKILL.md) · 常用 ADM：A B C D。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **范围与来源**：记录需求覆盖范围和来源。
- **需求规格**：给出功能、质量及约束条件。
- **验收方法**：规定可执行的验证和接受条件。
- **追溯与变更**：关联架构、风险、实现与变更记录。

## 组装与引用

- [需求目录](../artifacts/requirements-catalog.md)。
- [约束目录](../artifacts/constraints-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 不得用方案名称替代需求结果。
- 优先级与批准状态独立。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-requirements-specification",
  "deliverable_id": "architecture-requirements-specification",
  "title": "架构需求规格 · 星河零售虚构案例",
  "view_ids": [
    "v-requirements-catalog",
    "v-constraints-catalog"
  ],
  "entity_ids": [
    "constraint-budget",
    "req-accuracy",
    "req-privacy",
    "control"
  ],
  "sections": {
    "范围与来源": "需求来自虚构订单履约场景及越权风险情景。",
    "需求规格": "一致性要求：确认前校验库存；安全要求：只按履约目的读取必要字段。",
    "验收方法": "分别通过并发、故障恢复、允许拒绝和审计检查验证，测试证据尚未提供。",
    "追溯与变更": "需求通过 app-oms、control 和 wp-app 关联到设计与工作包。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-requirements-specification --out ./architecture-output --render
```

## 来源

G248, G176, G186, G152，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.6. Architecture Requirements Specification](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_06)
  - 概念：架构需求规格的条目标题。
  - 边界：定量目的与内容在子节。
