# 架构构建块（ABBs）

ID：`architecture-building-blocks` · 主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md) · 常用 ADM：B C D E。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **职责与边界**：描述需要具备的能力、服务和边界。
- **功能与接口**：规定输入输出和接口语义。
- **质量与约束**：引用需求、原则和可验证质量条件。
- **复用与实现**：说明依赖、可复用范围和候选 SBB。

## 组装与引用

- [需求目录](../artifacts/requirements-catalog.md)。
- [解决方案概念图](../artifacts/solution-concept-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

ABB 规定职责、接口、质量与约束；SBB 表达候选或实际实现及 ABB 映射。构建块作为交付内容不意味着与制品成为互斥类别。

## 评审与不足

- ABB 不等于产品选择。
- 每项关键规定应可追溯到需求。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-building-blocks",
  "deliverable_id": "architecture-building-blocks",
  "title": "架构构建块 · 星河零售虚构案例",
  "view_ids": [
    "v-requirements-catalog",
    "v-solution-concept-diagram"
  ],
  "entity_ids": [
    "req-accuracy",
    "req-privacy",
    "service-order",
    "abb"
  ],
  "sections": {
    "职责与边界": "订单确认 ABB 负责可靠校验并形成订单承诺，边界不包含物流执行。",
    "功能与接口": "输入为客户、商品和数量；输出为确认或可恢复失败结果，库存接口需版本契约。",
    "质量与约束": "ABB 追溯 req-accuracy，验证并发库存确认及错误恢复。",
    "复用与实现": "候选 SBB 为订单服务模块和库存适配模块，尚未完成选型或验证。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-building-blocks --out ./architecture-output --render
```

## 来源

G248, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.1. Architecture Building Blocks](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_01)
  - 概念：ABB交付内容是企业资料库中的架构文档和模型。
  - 逻辑：详细特征见第5章。
  - 决策：按逻辑架构需要选择并追溯资料库资产。
  - 边界：ABB不同于实现特定的SBB，不以文件存在证明可复用。
