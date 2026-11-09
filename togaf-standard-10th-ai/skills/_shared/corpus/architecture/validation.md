# 架构解析验证

结果：**通过**；结构错误 0 项。

本报告核验来源、数值、结构完整性与检索可达性，不宣称全部中文解释或图关系已通过独立语义审校。

|检查项|数量|
|---|---:|
|指南架构分析|26|
|概念|94|
|概念关系|97|
|角色档案|56|
|角色技能要求|1216|
|原 PDF 数字技能单元格|426|
|原图色阶技能单元格|790|
|图示解析|345|
|图内节点|6225|
|图内关系|3725|
|包含与分组|4121|
|知识图节点|6525|
|知识图关系|9181|
|可完整检索的语义记录|640|
|架构检索块|4235|
|逐页原文短引|491|
|抽取正文或表格中的去重角色上下文|1924|
|可编辑 Mermaid 图文件|1035|
|Markdown 本地链接|5023|
|实际 CLI 查询|6|
|原文层检索块数据契约|4340|
|架构层检索块数据契约|4235|
|当前图片解析路由|345|
|全文JSON逐页图片路由|1487|
|覆盖清单的文档|26|
|覆盖清单的全部图像区域|417|
|已登记完整可见内容审校的图|242|
|独立图元文字/表格转录|102|

## 查询验证

- `企业架构师 技能` / `role` / G249：`architecture:G249:role:enterprise-architect:c009`、`architecture:G249:role:enterprise-architect:c010`、`architecture:G249:role:enterprise-architect:c003`。
- `首席架构师 职责` / `role` / G249：`architecture:G249:role:chief-architect:c001`、`architecture:G249:role:chief-architect:c003`、`architecture:G249:role:chief-architect:c002`。
- `能力实例 实例化` / `relationship` / G233：`architecture:relation:R006:c001`、`architecture:relation:R008:c001`、`architecture:relation:R007:c001`。
- `上下级 组织` / `diagram` / G206：`architecture:diagram:G206/fig2-1:c001`、`architecture:diagram:G206/fig2-1:c003`、`architecture:diagram:G206/fig2-1:c007`。
- `业务能力 价值流` / `diagram` / G233：`architecture:diagram:G233/fig6-2:c015`、`architecture:diagram:G233/fig6-2:c016`、`architecture:diagram:G233/fig6-2:c001`。
- `输入 输出 架构` / `architecture` / G186：`architecture:guide:G186:c002`、`architecture:guide:G186:c001`、`architecture:guide:G186:c003`。

## 验收边界

- 原文引用存在与指纹正确不等于全部中文释义经独立专业语义审校。
- 图像历史解释与本轮选择性视觉复核保持不同状态；本验证不重新目视确认全部箭头。
- 技能数值独立对照数字单元格或原图色阶，不把参考熟练度当作实际人员评分或通用岗位硬性门槛。
- 原图、派生结构、完整知识图和检索记录分别检查；实际项目事实仍需项目证据。

[完整检查数据](validation.json)
