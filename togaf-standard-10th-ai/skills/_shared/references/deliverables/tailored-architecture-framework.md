# 裁剪后的架构框架（Tailored Architecture Framework）

ID：`tailored-architecture-framework` · 主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md) · 常用 ADM：Preliminary。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **裁剪语境**：描述企业目的、规模、成熟度与已有方法。
- **方法与治理**：定义 ADM 使用方式及其他框架接口。
- **内容与视点**：选择元模型、制品、视点及表示法。
- **工具与维护**：明确存储库、质量检查及改进责任。

## 组装与引用

- [原则目录](../artifacts/principles-catalog.md)。
- [需求目录](../artifacts/requirements-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 裁剪须解释目的。
- ADM 不必强制串行或全量产出。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-tailored-architecture-framework",
  "deliverable_id": "tailored-architecture-framework",
  "title": "裁剪后的架构框架 · 星河零售虚构案例",
  "view_ids": [
    "v-principles-catalog",
    "v-requirements-catalog"
  ],
  "entity_ids": [
    "principle",
    "standard",
    "viewpoint"
  ],
  "sections": {
    "裁剪语境": "面向单个跨域履约改造项目，采用分段、项目目的和逻辑层表达。",
    "方法与治理": "ADM 按决策需要迭代，需求贯穿；治理和运营反馈进入 G/H。",
    "内容与视点": "选择客户信息、能力、应用、技术和风险控制关系，按受众定义视点。",
    "工具与维护": "使用本地模型与相对路径资产索引，脚本检查后进行业务和图形评审。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable tailored-architecture-framework --out ./architecture-output --render
```

## 来源

G248, G184, G186, G20F, G210，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.21. Tailored Architecture Framework](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_21)
  - 概念：裁剪架构框架的条目标题。
  - 边界：两级裁剪及内容在子节。
