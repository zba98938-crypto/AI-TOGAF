# 架构存储库（Architecture Repository）

ID：`architecture-repository` · 主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md) · 常用 ADM：Preliminary H。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **结构与职责**：定义资产分类、维护方和访问规则。
- **资产索引**：提供可检索标识、版本、状态、路径和来源。
- **复用与引用**：明确模型、视图、构建块和交付物关系。
- **维护与治理**：定义更新、归档、基线和审查机制。

## 组装与引用

- [原则目录](../artifacts/principles-catalog.md)。
- [技术标准目录](../artifacts/technology-standards-catalog.md)。
- [需求目录](../artifacts/requirements-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

额外建立实际资产清单：标识、路径、版本、状态和来源。生成器索引实际输出视图与共享模型，不能用空文件夹代替存储库。

## 评审与不足

- 索引实际指向存在资产。
- 不能只交空文件夹或概念说明。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-repository",
  "deliverable_id": "architecture-repository",
  "title": "架构存储库 · 星河零售虚构案例",
  "view_ids": [
    "v-principles-catalog",
    "v-technology-standards-catalog",
    "v-requirements-catalog"
  ],
  "entity_ids": [
    "decision-stock",
    "standard",
    "decision",
    "repo",
    "viewpoint"
  ],
  "sections": {
    "结构与职责": "按模型、视图、构建块、交付物、标准和决策分类，架构团队维护。",
    "资产索引": "下方实际资产索引指向本次生成文件，版本为 0.1-example。",
    "复用与引用": "各视图复用 model.json 的稳定实体标识；交付物通过相对路径引用视图。",
    "维护与治理": "当前仅示例候选基线；发布、归档和权限规则需按目标项目落实。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-repository --out ./architecture-output --render
```

## 来源

G248, G184, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.5. Architecture Repository](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_05)
  - 概念：架构资料库的条目标题。
  - 边界：目的和详细内容引用在子节。
