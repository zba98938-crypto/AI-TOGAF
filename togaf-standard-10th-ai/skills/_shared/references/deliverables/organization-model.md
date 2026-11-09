# 企业架构组织模型（Organization Model (for EA)）

ID：`organization-model` · 主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md) · 常用 ADM：Preliminary。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **使命与服务**：说明 EA 能力目的及服务对象。
- **组织与职责**：定义团队、角色、决策权和协作。
- **技能与容量**：评估所需技能、资源及缺口。
- **治理与绩效**：定义治理接口、度量和改进。

## 组装与引用

- [组织地图](../artifacts/organization-map.md)。
- [角色目录](../artifacts/role-catalog.md)。
- [参与者/角色矩阵](../artifacts/actor-role-matrix.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 架构组织模型不同于全企业组织地图。
- 职责与决策权分别写明。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-organization-model",
  "deliverable_id": "organization-model",
  "title": "企业架构组织模型 · 星河零售虚构案例",
  "view_ids": [
    "v-organization-map",
    "v-role-catalog",
    "v-actor-role-matrix"
  ],
  "entity_ids": [
    "cap-fulfillment",
    "cap-order",
    "cap-stock",
    "cap-delivery",
    "org-enterprise",
    "org-sales",
    "org-warehouse",
    "org-partner",
    "role-buyer",
    "role-picker"
  ],
  "sections": {
    "使命与服务": "EA 服务支持业务发起方作出跨域履约改造决策。",
    "组织与职责": "架构团队协调各域；业务、数据和实施负责人分别承担价值、数据和交付责任。",
    "技能与容量": "需要业务、数据、应用、技术、安全及沟通技能，实际人数容量待确认。",
    "治理与绩效": "以决策支持和变革成效评价团队，不按模型数量作为唯一指标。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable organization-model --out ./architecture-output --render
```

## 来源

G248, G184, G198, G249，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.16. Organizational Model for Enterprise Architecture](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_16)
  - 概念：EA组织模型的条目标题。
  - 边界：组织边界与内容在子节。
