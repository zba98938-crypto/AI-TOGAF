# 平台分解图（Platform Decomposition Diagram）

ID：`platform-decomposition-diagram` · 主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md) · 原文域：技术。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

平台由哪些技术服务和组件构成？

主要受众：平台、运维、安全及标准负责人。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `platform`：`responsibility`、`standard`。
- `technology`：`responsibility`、`standard`。
- `technology_service`：`responsibility`、`standard`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `contains`：平台组成。platform → technology。
- `realizes`：实现规定的服务或构建块。function, technology, sbb → business_service, technology_service, abb。

## 分析与构造

1. 确定平台边界和技术服务。
2. 按职责分解组件并关联实现。
3. 核对标准、版本及服务依赖。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`flowchart`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 组成关系与实现关系不同。
- 平台产品不等于全部技术架构。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

支撑交付物：[架构定义文档](../deliverables/architecture-definition-document.md)。

相关制品：[技术组合目录](technology-portfolio-catalog.md)、[应用/技术矩阵](application-technology-matrix.md)、[环境与位置图](environments-and-locations-diagram.md)、[软件分布图](software-distribution-diagram.md)、[解决方案概念图](solution-concept-diagram.md)、[企业可管理性图](enterprise-manageability-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-platform-decomposition-diagram",
  "artifact_id": "platform-decomposition-diagram",
  "title": "平台分解图 · 星河零售虚构案例",
  "context": {
    "domains": [
      "business",
      "data",
      "application",
      "technology"
    ],
    "landscape": "segment",
    "purpose": "project",
    "abstraction": "logical",
    "evolution": "target"
  },
  "entity_ids": [
    "platform",
    "tech-platform",
    "tech-service"
  ],
  "relationship_ids": [
    "platform-contains",
    "platform-realizes"
  ],
  "analysis": "平台由哪些技术服务和组件构成？ 本视图限定订单履约改造范围，展示案例设定的平台分解图。确定平台边界和技术服务；实际项目需由相关责任方核实。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact platform-decomposition-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 578；方法指南：G248, G248, G21I。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.7.5. Platform Decomposition Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_06_05)
  - 概念：平台分解图概览支持信息系统的基础设施平台。
  - 逻辑：显示企业应用，可细分硬件软件的逻辑/物理技术组件；按范围加入跨平台通信并可选产品版本/CPU细节。
  - 决策：选择概览或详细程度，核对平台到应用支持。
  - 边界：非正式概览允许但不是已验证容量；所需细节由关切决定。
