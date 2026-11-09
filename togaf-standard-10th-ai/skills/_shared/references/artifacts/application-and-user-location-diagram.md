# 应用与用户位置图（Application and User Location Diagram）

ID：`application-and-user-location-diagram` · 主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md) · 原文域：业务、应用。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

用户从哪里访问部署在哪里的应用？

主要受众：应用和业务功能负责人、集成及数据团队。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `actor`：`jurisdiction`。
- `application`：名称、边界、来源及对象类型。
- `location`：`jurisdiction`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `uses_application`：主体使用应用，不等于授权。actor, role → application。
- `located_at`：对象位于地点。environment, application, technology, hardware, actor → location。

## 分析与构造

1. 区分用户位置与应用位置。
2. 映射访问路径和跨区域访问。
3. 检查时延、驻留及访问限制。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`flowchart`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 用户所属组织不能代替地理位置。
- 远程访问不等于同站点部署。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[位置目录](location-catalog.md)、[组织/参与者目录](organization-actor-catalog.md)、[应用组合目录](application-portfolio-catalog.md)、[参与者/角色矩阵](actor-role-matrix.md)、[应用/功能矩阵](application-function-matrix.md)、[应用/组织矩阵](application-organization-matrix.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-application-and-user-location-diagram",
  "artifact_id": "application-and-user-location-diagram",
  "title": "应用与用户位置图 · 星河零售虚构案例",
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
    "actor-customer",
    "app-web",
    "app-oms",
    "loc-cloud",
    "loc-east"
  ],
  "relationship_ids": [
    "customer-web",
    "loc-app",
    "loc-user"
  ],
  "analysis": "用户从哪里访问部署在哪里的应用？ 本视图限定订单履约改造范围，展示案例设定的应用与用户位置图。区分用户位置与应用位置；实际项目需由相关责任方核实。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact application-and-user-location-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 508, 547；方法指南：G248, G206, G248。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.6.8. Application and User Location Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_05_08)
  - 概念：应用和用户地点图展示使用、托管、开发、测试及发布的地理分布。
  - 逻辑：地理用户、应用执行及薄客户端分布影响实例、许可、支持中心、管理工具、服务器及带宽估算。
  - 决策：核查位置及用户活动，结合真实使用数据作估算。
  - 边界：图支持估算，不提供未经测量的工作量、容量或性能保证。
