# 解决方案构建块（SBBs）

ID：`solution-building-blocks` · 主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md) · 常用 ADM：E G。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **实现边界**：定义实际组件、配置、版本和运行职责。
- **ABB 与需求映射**：说明实现哪些架构规定。
- **接口与依赖**：记录产品、环境、数据和外部契约。
- **验证与生命周期**：提供候选或实际验证、支持和退出安排。

## 组装与引用

- [应用组合目录](../artifacts/application-portfolio-catalog.md)。
- [技术组合目录](../artifacts/technology-portfolio-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

ABB 规定职责、接口、质量与约束；SBB 表达候选或实际实现及 ABB 映射。构建块作为交付内容不意味着与制品成为互斥类别。

## 评审与不足

- 候选产品不是已部署 SBB。
- 一个 SBB 可实现多个 ABB。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-solution-building-blocks",
  "deliverable_id": "solution-building-blocks",
  "title": "解决方案构建块 · 星河零售虚构案例",
  "view_ids": [
    "v-application-portfolio-catalog",
    "v-technology-portfolio-catalog"
  ],
  "entity_ids": [
    "app-web",
    "app-oms",
    "app-stock",
    "app-old",
    "tech-platform",
    "tech-db",
    "tech-old",
    "abb",
    "sbb"
  ],
  "sections": {
    "实现边界": "候选订单服务和库存适配模块部署到目标运行节点，版本为候选 v1。",
    "ABB 与需求映射": "该 SBB 拟实现订单确认 ABB，并满足库存一致性及最小访问需求。",
    "接口与依赖": "依赖库存接口、订单存储及运行平台；产品与支持周期待厂商确认。",
    "验证与生命周期": "尚无已部署证据；需通过并发、恢复、权限及升级验证后再评估采用。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable solution-building-blocks --out ./architecture-output --render
```

## 来源

G248, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.19. Solution Building Blocks](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_19)
  - 概念：SBB是资料库中实现特定的构建块。
  - 逻辑：具体特征见第5章。
  - 决策：按实现需要与ABB匹配并追溯资料库。
  - 边界：SBB与逻辑ABB身份不同，不因同名而合并。
