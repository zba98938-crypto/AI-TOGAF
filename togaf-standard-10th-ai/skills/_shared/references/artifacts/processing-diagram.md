# 处理图（Processing Diagram）

ID：`processing-diagram` · 主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md) · 原文域：应用。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

处理如何在应用组件间分配并完成一次交互？

主要受众：应用和业务功能负责人、集成及数据团队。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `application`：名称、边界、来源及对象类型。
- `process`：名称、边界、来源及对象类型。
- `data_entity`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `processing_step`：场景中有序处理消息。application → application。
- `accesses`：应用或处理访问数据。application, process → data_entity。

附加要求：`{"processing_step": ["order"]}`。

## 分析与构造

1. 选择典型处理场景。
2. 定义有序调用、输入输出和组件责任。
3. 走查异常、事务与一致性边界。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`sequence`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 序列只代表所选场景。
- 不能从排列推断全部运行路径。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[流程/事件/控制/产品目录](process-event-control-product-catalog.md)、[应用组合目录](application-portfolio-catalog.md)、[数据实体/数据组件目录](data-entity-data-component-catalog.md)、[应用/功能矩阵](application-function-matrix.md)、[应用/组织矩阵](application-organization-matrix.md)、[数据实体/业务功能矩阵](data-entity-business-function-matrix.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-processing-diagram",
  "artifact_id": "processing-diagram",
  "title": "处理图 · 星河零售虚构案例",
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
    "app-web",
    "app-oms",
    "app-stock"
  ],
  "relationship_ids": [
    "seq1",
    "seq2",
    "seq3"
  ],
  "analysis": "处理如何在应用组件间分配并完成一次交互？ 本视图限定订单履约改造范围，展示案例设定的处理图。选择典型处理场景；实际项目需由相关责任方核实。",
  "legend": "消息按 order 从上到下；实线箭头表示所选场景调用，不表达所有运行路径。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact processing-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 559；方法指南：G248, G248, G21I。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.7.6. Processing Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_06_06)
  - 概念：处理图关注代码/配置部署单元及其技术部署。
  - 逻辑：层分离、服务水平、地点与角色影响分组；单元含安装、运行状态执行、持久数据子单元，并部署于专用或共享技术。
  - 决策：以实际配置与使用模式选择分组，核查协议连接及服务粒度影响。
  - 边界：业务能力/服务/应用分组不同于它们身份合并；容量和工作量未知不能自动填充。
