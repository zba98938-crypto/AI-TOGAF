# 架构定义文档（Architecture Definition Document）

ID：`architecture-definition-document` · 主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md) · 常用 ADM：B C D E。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **语境与关注点**：说明五维语境、范围和利益相关者。
- **基线架构**：引用有证据的现状视图。
- **目标架构**：说明跨域目标及权衡。
- **差距与过渡**：总结变化、依赖和过渡状态。
- **决策与未决项**：记录假设、冲突和需确认问题。

## 组装与引用

- [业务能力地图](../artifacts/business-capability-map.md)。
- [概念数据图](../artifacts/conceptual-data-diagram.md)。
- [应用通信图](../artifacts/application-communication-diagram.md)。
- [平台分解图](../artifacts/platform-decomposition-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 基线目标采用可比较范围。
- 各域引用相同实体标识。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-definition-document",
  "deliverable_id": "architecture-definition-document",
  "title": "架构定义文档 · 星河零售虚构案例",
  "view_ids": [
    "v-business-capability-map",
    "v-conceptual-data-diagram",
    "v-application-communication-diagram",
    "v-platform-decomposition-diagram"
  ],
  "entity_ids": [
    "cap-fulfillment",
    "cap-order",
    "cap-stock",
    "cap-delivery",
    "app-web",
    "app-oms",
    "app-stock",
    "app-old",
    "data-customer",
    "data-order",
    "tech-platform",
    "tech-db",
    "tech-old"
  ],
  "sections": {
    "语境与关注点": "范围为订单确认与仓储交接，面向履约负责人；五维语境见项目模型。",
    "基线架构": "基线为现有单节点订单应用，容量及人工协调方式为案例设定。",
    "目标架构": "目标由线上商城、订单和库存应用协作，统一客户和订单语义。",
    "差距与过渡": "差距涵盖容量、接口、数据一致性及访问控制；数据契约先行。",
    "决策与未决项": "现阶段保留候选方案，真实基线证据、预算和厂商支持周期待补充。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-definition-document --out ./architecture-output --render
```

## 来源

G248, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.3. Architecture Definition Document](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_03)
  - 概念：架构定义文档的条目标题。
  - 边界：定义及内容在子节。
