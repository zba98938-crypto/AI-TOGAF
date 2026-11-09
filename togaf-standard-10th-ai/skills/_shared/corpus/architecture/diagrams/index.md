# 架构图、关系与上下级分析

243条既有逻辑图逐条分析，并补充独立非装饰图片；原文图242、中文编者图1分别保留。

原图、完整节点关系、Mermaid及语义分析按图关联。所有节点保留，包含/分组、业务关系、组织汇报和治理范围分别记录。

```json
{
  "diagrams": 345,
  "source_logical_figures": 242,
  "editorial_figures": 1,
  "supplementary_non_decorative_images": 102,
  "decorative_images_disposed": 66,
  "nodes": 6225,
  "relations": 3725,
  "hierarchy_links": 4121,
  "reviewed_figures": 242,
  "content_audited_figures": 242,
  "source_transcribed_embedded_images": 102,
  "corrected_or_normalized_relations": 1891
}
```

[可浏览原图目录](gallery.html) · [机器索引](index.json)

|图|类型|元素|关系|包含/分组|PDF页|
|---|---|---:|---:|---:|---|
|[G152/fig1-1 · 核心安全与风险概念及其在 TOGAF ADM 中的位置](G152/fig1-1.md)|architecture-concept-or-system-model|52|29|43|[14]|
|[G152/fig3-1 · 业务风险领域与网络风险领域（业务栈）](G152/fig3-1.md)|system-or-data-reference-architecture|13|7|9|[22]|
|[G152/fig3-2 · SABSA 运营风险模型](G152/fig3-2.md)|process-or-method-model|24|17|16|[23]|
|[G152/fig3-3 · ISO 31000:2009 风险管理模型](G152/fig3-3.md)|process-or-method-model|8|16|3|[24]|
|[G152/fig4-1 · 安全作为横切关注点](G152/fig4-1.md)|architecture-concept-or-system-model|5|4|0|[28]|
|[G152/fig5-1 · SABSA 业务属性分类法示例](G152/fig5-1.md)|decomposition-or-organization-model|83|82|82|[40]|
|[G152/fig5-2 · 使用 ArchiMate 语言对风险与安全建模](G152/fig5-2.md)|architecture-model|22|22|8|[43]|
|[G176/fig3-1 · 创建业务场景](G176/fig3-1.md)|process-or-method-model|6|4|0|[18]|
|[G176/fig3-2 · 开发业务场景的阶段与步骤](G176/fig3-2.md)|mapping-or-assessment-matrix|15|12|10|[20]|
|[G176/fig5-1 · 业务场景的相对贡献](G176/fig5-1.md)|analytical-view|6|5|0|[29]|
|[G176/fig6-1 · 需求在整个 TOGAF ADM 中的相关性](G176/fig6-1.md)|process-or-method-model|13|20|0|[30]|
|[G178/fig1-1 · 价值流示例](G178/fig1-1.md)|process-or-method-model|6|4|5|[12]|
|[G178/fig1-2 · 价值流建模关系](G178/fig1-2.md)|architecture-metamodel|6|8|0|[13]|
|[G178/fig4-1 · 价值流示例](G178/fig4-1.md)|process-or-method-model|6|4|5|[18]|
|[G178/fig4-2 · 招聘员工价值流](G178/fig4-2.md)|process-or-method-model|6|4|5|[20]|
|[G178/fig4-3 · 价值流阶段到业务能力的交叉映射](G178/fig4-3.md)|mapping-or-assessment-matrix|29|20|20|[21]|
|[G178/fig4-4 · 招聘员工价值流热力图](G178/fig4-4.md)|mapping-or-assessment-matrix|31|21|21|[23]|
|[G178/figA-1 · 迈克尔·波特的价值链](G178/figA-1.md)|process-or-method-model|12|7|9|[25]|
|[G178/figA-2 · 价值网络图](G178/figA-2.md)|architecture-concept-or-system-model|7|50|0|[26]|
|[G178/figA-3 · 精益价值流](G178/figA-3.md)|architecture-evolution-or-plan|23|13|20|[27]|
|[G184/fig10-1 · 决策流程集成](G184/fig10-1.md)|process-or-method-model|7|7|0|[95]|
|[G184/fig10-2 · 执行流程集成](G184/fig10-2.md)|process-or-method-model|7|5|5|[97]|
|[G184/fig10-3 · 风格化架构开发甘特图](G184/fig10-3.md)|architecture-evolution-or-plan|16|18|11|[102]|
|[G184/fig11-1 · 业务价值驱动（示例）](G184/fig11-1.md)|decomposition-or-organization-model|13|13|0|[109]|
|[G184/fig11-2 · EA 价值驱动（示例）](G184/fig11-2.md)|decomposition-or-organization-model|12|12|0|[110]|
|[G184/fig11-3 · EA 能力模型示例（一）](G184/fig11-3.md)|decomposition-or-organization-model|7|0|4|[112]|
|[G184/fig11-4 · EA 能力模型示例（二）](G184/fig11-4.md)|decomposition-or-organization-model|30|0|26|[112]|
|[G184/fig12-1 · 可持续的 EA](G184/fig12-1.md)|architecture-concept-or-system-model|13|12|0|[118]|
|[G184/fig3-1 · 商业企业的语境](G184/fig3-1.md)|process-or-method-model|4|6|0|[23]|
|[G184/fig3-2 · EA 能力模型](G184/fig3-2.md)|decomposition-or-organization-model|8|5|4|[24]|
|[G184/fig4-1 · 运营模式](G184/fig4-1.md)|analytical-view|6|0|0|[35]|
|[G184/fig4-2 · 扩展企业](G184/fig4-2.md)|architecture-concept-or-system-model|19|4|9|[36]|
|[G184/fig4-3 · PMI 影响力矩阵](G184/fig4-3.md)|analytical-view|6|0|0|[40]|
|[G184/fig4-4 · Everett Rogers 创新采用模型（又称技术扩散模型）](G184/fig4-4.md)|analytical-view|10|0|0|[42]|
|[G184/fig5-1 · EA 团队常见的组织归属](G184/fig5-1.md)|decomposition-or-organization-model|67|57|64|[51, 52]|
|[G184/fig6-1 · 可能的治理层级](G184/fig6-1.md)|decomposition-or-organization-model|6|9|4|[61]|
|[G184/fig6-2 · 影响治理的外部与内部交互](G184/fig6-2.md)|architecture-concept-or-system-model|21|10|20|[65]|
|[G184/fig6-3 · ISO 31000 风险管理标准模型](G184/fig6-3.md)|process-or-method-model|8|16|3|[67]|
|[G184/fig7-1 · 框架族之间的关系（TOGAF 标准——ADM 技术图 3-1 [C220] 的抽象视图）](G184/fig7-1.md)|analytical-view|8|7|0|[70]|
|[G184/fig9-1 · EA 团队对齐的几种可能](G184/fig9-1.md)|decomposition-or-organization-model|67|57|64|[81, 82]|
|[G184/fig9-2 · EA 能力模型的分解](G184/fig9-2.md)|decomposition-or-organization-model|25|0|22|[83]|
|[G184/fig9-3 · 执行 EA 能力的团队](G184/fig9-3.md)|decomposition-or-organization-model|3|0|2|[84]|
|[G184/fig9-4 · 普遍接受的域](G184/fig9-4.md)|analytical-view|6|9|0|[90]|
|[G184/fig9-5 · 安全作为贯穿架构的横切关注点](G184/fig9-5.md)|architecture-concept-or-system-model|5|4|0|[91]|
|[G186/fig13-1 · 使用存储库管理路线图——识别变更](G186/fig13-1.md)|decomposition-or-organization-model|31|19|30|[132]|
|[G186/fig13-2 · 架构的影响分析](G186/fig13-2.md)|decomposition-or-organization-model|34|20|33|[133]|
|[G186/fig14-1 · 业务周期与按目的划分的架构](G186/fig14-1.md)|architecture-evolution-or-plan|13|8|4|[136]|
|[G186/fig3-1 · EA 全景的特征](G186/fig3-1.md)|analytical-view|4|3|0|[28]|
|[G186/fig3-2 · 带一个架构项目的 EA 全景](G186/fig3-2.md)|analytical-view|5|4|1|[29]|
|[G186/fig3-3 · 企业架构的目的](G186/fig3-3.md)|analytical-view|5|0|4|[30]|
|[G186/fig4-1 · 业务周期与四种架构目的的对应](G186/fig4-1.md)|architecture-evolution-or-plan|13|8|0|[41]|
|[G186/fig4-2 · 半座桥](G186/fig4-2.md)|illustrative-photo|0|0|0|[44]|
|[G186/fig5-1 · TOGAF 架构存储库](G186/fig5-1.md)|architecture-concept-or-system-model|36|15|32|[47]|
|[G186/fig5-10 · 开发支持解决方案交付的架构的示例项目计划](G186/fig5-10.md)|architecture-evolution-or-plan|105|11|99|[71]|
|[G186/fig5-2 · EA 存储库示例](G186/fig5-2.md)|decomposition-or-organization-model|21|20|20|[51]|
|[G186/fig5-3 · 多个候选架构](G186/fig5-3.md)|decomposition-or-organization-model|11|10|10|[52]|
|[G186/fig5-4 · 建模与分析工具中的参考材料](G186/fig5-4.md)|decomposition-or-organization-model|16|15|15|[53]|
|[G186/fig5-5 · 程式化的架构开发甘特图](G186/fig5-5.md)|mapping-or-assessment-matrix|16|18|11|[63]|
|[G186/fig5-6 · 问题解决方法（源自 Conklin 的棘手问题）](G186/fig5-6.md)|analytical-view|11|5|4|[63]|
|[G186/fig5-7 · 开发支持战略的架构的示例项目计划](G186/fig5-7.md)|architecture-evolution-or-plan|71|11|66|[65]|
|[G186/fig5-8 · 开发支持组合的架构的示例项目计划](G186/fig5-8.md)|architecture-evolution-or-plan|91|11|85|[67]|
|[G186/fig5-9 · 开发支持项目的架构的示例项目计划](G186/fig5-9.md)|architecture-evolution-or-plan|89|12|83|[69]|
|[G186/fig6-1 · 以 ADM 支持四种目的的“走查”重点](G186/fig6-1.md)|mapping-or-assessment-matrix|33|0|28|[]|
|[G186/fig8-1 · 能力与项目连续谱](G186/fig8-1.md)|architecture-evolution-or-plan|7|3|6|[90]|
|[G186/tabB-1 · 表 B-1：利益相关者职责（组合）](G186/tabB-1.md)|mapping-or-assessment-matrix|24|0|23|[151]|
|[G188/ex3-22 · 示例 3-22：项目 A 的工作分解结构（WBS）图](G188/ex3-22.md)|decomposition-or-organization-model|20|19|19|[55]|
|[G188/fig1-1 · 架构项目与 TOGAF ADM 的关系](G188/fig1-1.md)|process-or-method-model|11|24|7|[16]|
|[G188/fig2-1 · 企业架构的层级（TOGAF 架构全景摘要分类模型）](G188/fig2-1.md)|architecture-concept-or-system-model|25|5|19|[20]|
|[G188/fig2-2 · 架构项目生命周期（从 TOGAF ADM 视角）](G188/fig2-2.md)|process-or-method-model|36|23|12|[24]|
|[G188/fig3-1 · 本节结构与架构项目流程（箭头）](G188/fig3-1.md)|process-or-method-model|7|6|0|[31]|
|[G188/fig3-2 · 基于 PRINCE2 方法的项目管理团队简化图](G188/fig3-2.md)|decomposition-or-organization-model|10|10|4|[40]|
|[G188/fig3-3 · 架构项目的最终交付物](G188/fig3-3.md)|decomposition-or-organization-model|25|19|12|[74]|
|[G188/fig4-1 · TOGAF ADM 与 PRINCE2 映射（高层）](G188/fig4-1.md)|mapping-or-assessment-matrix|69|28|55|[79]|
|[G188/fig4-2 · TOGAF ADM 与 PRINCE2 映射（详细）](G188/fig4-2.md)|mapping-or-assessment-matrix|98|58|87|[83]|
|[G188/fig5-1 · TOGAF ADM 与 PMBOK 映射（高层）](G188/fig5-1.md)|mapping-or-assessment-matrix|89|31|73|[85]|
|[G188/img-p54 · 风险登记表示例（3.4.5 节未编号插图）](G188/img-p54.md)|mapping-or-assessment-matrix|2|0|0|[68]|
|[G18A/fig2-1 · 业务模型的抽象视图](G18A/fig2-1.md)|architecture-concept-or-system-model|20|6|16|[13]|
|[G18A/fig2-2 · 四框框架](G18A/fig2-2.md)|architecture-concept-or-system-model|5|4|2|[13]|
|[G18A/fig2-3 · 业务模型立方体](G18A/fig2-3.md)|analytical-view|7|6|0|[14]|
|[G18A/fig2-4 · 业务模型画布](G18A/fig2-4.md)|business-model-canvas|10|2|0|[15]|
|[G18A/fig4-1 · 战略、业务模型与架构之间的关系](G18A/fig4-1.md)|process-or-method-model|28|7|20|[18]|
|[G18A/fig7-1 · 零售商业务模型画布——现状](G18A/fig7-1.md)|business-model-canvas|33|2|31|[24]|
|[G18A/fig7-2 · 零售商业务模型画布——未来态](G18A/fig7-2.md)|business-model-canvas|33|2|31|[25]|
|[G18A/figA-1 · 业务模型画布](G18A/figA-1.md)|business-model-canvas|10|2|9|[29]|
|[G190/fig2-1 · 金融机构的简单信息地图](G190/fig2-1.md)|architecture-concept-or-system-model|6|7|0|[12]|
|[G190/fig4-1 · 业务能力与信息概念](G190/fig4-1.md)|architecture-concept-or-system-model|10|13|8|[14]|
|[G190/fig5-1 · 多个业务概念之间的示例关系](G190/fig5-1.md)|architecture-concept-or-system-model|11|5|4|[16]|
|[G190/figA-1 · 使用 ArchiMate 语言的信息地图](G190/figA-1.md)|architecture-model|9|10|0|[22]|
|[G190/figA-2 · 使用 ArchiMate 语言的“信息—业务能力”交叉映射](G190/figA-2.md)|architecture-model|14|6|8|[23]|
|[G190/figA-3 · UML 中的信息地图](G190/figA-3.md)|architecture-metamodel|6|7|0|[24]|
|[G190/figA-4 · 信息类型之间的关系](G190/figA-4.md)|architecture-metamodel|2|1|0|[25]|
|[G190/figA-5 · 实体关系图中的信息地图](G190/figA-5.md)|architecture-metamodel|6|7|0|[26]|
|[G198/fig6-1 · 分段架构与解决方案架构](G198/fig6-1.md)|process-or-method-model|61|92|54|[23]|
|[G198/fig6-2 · 分段架构师与解决方案架构师的技能差异](G198/fig6-2.md)|architecture-concept-or-system-model|58|89|48|[24]|
|[G206/fig2-1 · 网式组织图（Web-Styled Organigraph）](G206/fig2-1.md)|architecture-concept-or-system-model|92|103|0|[12]|
|[G206/fig3-1 · 标准组织架构图](G206/fig3-1.md)|decomposition-or-organization-model|18|17|0|[14]|
|[G206/fig3-2 · 通用组织地图](G206/fig3-2.md)|architecture-concept-or-system-model|18|20|0|[15]|
|[G206/fig7-1 · 零售业务组织地图](G206/fig7-1.md)|architecture-concept-or-system-model|17|26|0|[22]|
|[G206/fig7-2 · 组织单元与业务能力的交叉映射](G206/fig7-2.md)|architecture-concept-or-system-model|19|28|0|[23]|
|[G20F/fig3-1 · TOGAF ADM](G20F/fig3-1.md)|process-or-method-model|10|17|0|[18]|
|[G20F/fig4-1 · 架构全景的分级分类模型](G20F/fig4-1.md)|architecture-evolution-or-plan|13|0|8|[20]|
|[G20F/fig4-2 · 过渡架构](G20F/fig4-2.md)|process-or-method-model|8|8|0|[22]|
|[G20F/fig4-3 · ADM 过程层级示例](G20F/fig4-3.md)|decomposition-or-organization-model|37|57|30|[23]|
|[G20F/fig4-4 · ADM 层级与敏捷交付概念的映射](G20F/fig4-4.md)|mapping-or-assessment-matrix|129|102|122|[28]|
|[G20F/fig4-5 · 不同架构层级上的敏捷性](G20F/fig4-5.md)|process-or-method-model|18|12|12|[34]|
|[G20F/fig5-1 · 企业架构的传统阶段](G20F/fig5-1.md)|process-or-method-model|5|4|0|[36]|
|[G20F/fig5-2 · 敏捷环境中的企业架构阶段](G20F/fig5-2.md)|process-or-method-model|25|0|20|[36]|
|[G20F/fig5-3 · 商业模式画布（BMC）模板](G20F/fig5-3.md)|business-model-canvas|10|0|9|[38]|
|[G20F/fig5-4 · 架构支撑产品与冲刺待办列表定义](G20F/fig5-4.md)|process-or-method-model|53|8|25|[44]|
|[G20F/fig5-5 · 产品与项目](G20F/fig5-5.md)|decomposition-or-organization-model|6|1|4|[45]|
|[G210/fig3-1 · 敏捷企业架构的协作方式](G210/fig3-1.md)|analytical-view|8|0|4|[19]|
|[G210/fig3-2 · ADM 中的企业架构开发冲刺](G210/fig3-2.md)|architecture-evolution-or-plan|17|4|4|[24]|
|[G210/fig3-3 · ADM 中的架构与解决方案冲刺](G210/fig3-3.md)|architecture-evolution-or-plan|21|12|6|[26]|
|[G210/fig3-4 · 跨开发协作](G210/fig3-4.md)|architecture-evolution-or-plan|26|23|8|[27]|
|[G210/fig3-5 · 使用冲刺的敏捷改进型企业](G210/fig3-5.md)|architecture-evolution-or-plan|15|4|3|[29]|
|[G211/fig3-1 · ABC 公司组织架构图](G211/fig3-1.md)|decomposition-or-organization-model|17|16|0|[16]|
|[G211/fig3-2 · ABC 公司一级业务能力地图](G211/fig3-2.md)|mapping-or-assessment-matrix|21|0|18|[20]|
|[G211/fig3-3 · 人力资源管理能力分解](G211/fig3-3.md)|decomposition-or-organization-model|12|0|11|[21]|
|[G211/fig5-1 · ABC 公司业务能力热力图](G211/fig5-1.md)|mapping-or-assessment-matrix|21|0|18|[24]|
|[G211/fig5-2 · 能力/组织映射示例](G211/fig5-2.md)|mapping-or-assessment-matrix|8|5|6|[25]|
|[G211/fig5-3 · 能力/价值流映射示例](G211/fig5-3.md)|mapping-or-assessment-matrix|34|20|16|[26]|
|[G212/fig3-1 · 开展 DTRA 的五项关键收益](G212/fig3-1.md)|analytical-view|11|5|5|[25]|
|[G212/fig4-1 · 数字技术采用的影响因素](G212/fig4-1.md)|architecture-concept-or-system-model|16|17|0|[27]|
|[G212/fig5-1 · 数字技术采用的四步路线图](G212/fig5-1.md)|process-or-method-model|9|3|4|[39]|
|[G212/fig5-2 · ABCD 数字技术采用框架](G212/fig5-2.md)|analytical-view|7|0|0|[40]|
|[G212/fig5-3 · 缺失因素对数字技术采用的影响](G212/fig5-3.md)|mapping-or-assessment-matrix|19|0|15|[42]|
|[G212/fig5-4 · 因素递进](G212/fig5-4.md)|architecture-concept-or-system-model|9|3|0|[43]|
|[G212/fig6-1 · 将因素映射到 TOGAF ADM](G212/fig6-1.md)|mapping-or-assessment-matrix|33|39|28|[45]|
|[G212/figA-1 · 李克特量表](G212/figA-1.md)|mapping-or-assessment-matrix|13|0|0|[49]|
|[G217/fig2-1 · 文档化矩阵示例（系统成熟度 × 架构描述正式度）](G217/fig2-1.md)|process-or-method-model|19|13|7|[26]|
|[G217/fig4-1 · TOGAF 原则与 DPBoK 标准语境的映射](G217/fig4-1.md)|mapping-or-assessment-matrix|21|0|19|[39]|
|[G217/fig4-2 · 企业架构服务到 DPBoK 标准涌现模型的映射](G217/fig4-2.md)|mapping-or-assessment-matrix|28|0|18|[50]|
|[G217/fig4-3 · 企业架构服务涌现模型](G217/fig4-3.md)|mapping-or-assessment-matrix|23|0|0|[60]|
|[G217/figC-1 · 企业架构服务到 ADM 阶段的映射](G217/figC-1.md)|mapping-or-assessment-matrix|34|0|18|[84]|
|[G21B/fig1-1 · 组织能力的通用描述](G21B/fig1-1.md)|decomposition-or-organization-model|26|0|18|[12]|
|[G21B/fig1-2 · 数据管理支撑能力与 DMBoK DAMA 轮盘的对应关系](G21B/fig1-2.md)|architecture-concept-or-system-model|17|5|11|[14]|
|[G21B/fig2-1 · 本文档使用的 ArchiMate 建模记法元素](G21B/fig2-1.md)|notation-or-legend|17|0|11|[18]|
|[G21B/fig3-1 · C-MDM 能力的功能构成](G21B/fig3-1.md)|architecture-model|26|13|16|[22]|
|[G21B/fig4-1 · 架构愿景的利益相关者](G21B/fig4-1.md)|decomposition-or-organization-model|16|0|13|[30]|
|[G21B/fig4-2 · 参考 C-MDM 路线图步骤](G21B/fig4-2.md)|architecture-evolution-or-plan|42|42|31|[33]|
|[G21B/fig5-1 · 自然人内核数据](G21B/fig5-1.md)|decomposition-or-organization-model|7|0|6|[38]|
|[G21B/fig5-2 · 组织/法人内核数据](G21B/fig5-2.md)|decomposition-or-organization-model|7|0|6|[39]|
|[G21B/fig5-3 · C-MDM 详细业务功能参考模型](G21B/fig5-3.md)|architecture-model|41|0|33|[41]|
|[G21B/fig5-4 · C-MDM 详细应用功能参考模型](G21B/fig5-4.md)|architecture-model|48|0|47|[45]|
|[G21B/fig6-1 · C-MDM 集成风格](G21B/fig6-1.md)|system-or-data-reference-architecture|17|11|14|[49]|
|[G21B/fig6-2 · C-MDM 数据交换类型概览](G21B/fig6-2.md)|mapping-or-assessment-matrix|31|6|26|[50]|
|[G21B/fig6-3 · 整合式风格模式](G21B/fig6-3.md)|mapping-or-assessment-matrix|36|9|30|[51]|
|[G21B/fig6-4 · 协作式风格模式](G21B/fig6-4.md)|mapping-or-assessment-matrix|37|10|31|[51]|
|[G21B/fig6-5 · 集中式风格模式](G21B/fig6-5.md)|mapping-or-assessment-matrix|37|10|31|[52]|
|[G21B/tab4-6 · 表 4-6：C-MDM 路线图步骤（plateau）](G21B/tab4-6.md)|mapping-or-assessment-matrix|46|42|35|[34, 35, 36]|
|[G21D/appA-p48 · 附录 A：政府参考模型图示（第 48 页：国际事务与贸易、国防与安全、一般政府与地方服务）](G21D/appA-p48.md)|decomposition-or-organization-model|55|0|52|[68]|
|[G21D/appA-p49 · 附录 A 第 49 页：青少年与教育、健康与社区福祉](G21D/appA-p49.md)|decomposition-or-organization-model|44|0|42|[69]|
|[G21D/appA-p50 · 附录 A 第 50 页：司法、治安与内政；财政](G21D/appA-p50.md)|decomposition-or-organization-model|39|0|37|[70]|
|[G21D/appA-p51 · 附录 A 第 51 页：增长、住房与环境；政策、绩效、人口与创新](G21D/appA-p51.md)|decomposition-or-organization-model|51|0|49|[71]|
|[G21D/appA-p52 · 附录 A 第 52 页：共享服务；交通与运营](G21D/appA-p52.md)|decomposition-or-organization-model|52|0|50|[72]|
|[G21D/fig1-1 · 政府参考模型的结构](G21D/fig1-1.md)|architecture-metamodel|3|2|0|[23]|
|[G21D/fig10-1 · 拟议的政策、绩效、人口与创新部门 L1–L3 要素的结构与内容概览](G21D/fig10-1.md)|decomposition-or-organization-model|19|0|18|[55]|
|[G21D/fig11-1 · 拟议的共享服务部门 L1–L3 要素的结构与内容概览](G21D/fig11-1.md)|decomposition-or-organization-model|39|0|38|[59]|
|[G21D/fig12-1 · 拟议的交通与运营部门 L1–L3 要素的结构与内容概览](G21D/fig12-1.md)|decomposition-or-organization-model|13|0|12|[64]|
|[G21D/fig2-1 · 拟议的国际事务与贸易部门 L1–L3 要素的结构与内容概览](G21D/fig2-1.md)|decomposition-or-organization-model|11|0|10|[25]|
|[G21D/fig3-1 · 拟议的国防与安全部门 L1–L3 要素的结构与内容概览](G21D/fig3-1.md)|decomposition-or-organization-model|14|0|13|[28]|
|[G21D/fig4-1 · 拟议的一般政府与地方服务部门 L1–L3 要素的结构与内容概览](G21D/fig4-1.md)|decomposition-or-organization-model|30|0|29|[32]|
|[G21D/fig5-1 · 拟议的青少年与教育部门 L1–L3 要素的结构与内容概览](G21D/fig5-1.md)|decomposition-or-organization-model|18|0|17|[36]|
|[G21D/fig6-1 · 拟议的健康与社区福祉部门 L1–L3 要素的结构与内容概览](G21D/fig6-1.md)|decomposition-or-organization-model|26|0|25|[39]|
|[G21D/fig7-1 · 拟议的司法、治安与内政部门 L1–L3 要素的结构与内容概览](G21D/fig7-1.md)|decomposition-or-organization-model|16|0|15|[43]|
|[G21D/fig8-1 · 拟议的财政部门 L1–L3 要素的结构与内容概览](G21D/fig8-1.md)|decomposition-or-organization-model|23|0|22|[47]|
|[G21D/fig9-1 · 拟议的增长、住房与环境部门 L1–L3 要素的结构与内容概览](G21D/fig9-1.md)|decomposition-or-organization-model|32|0|31|[51]|
|[G21H/fig3-1 · DBRM 要素——高层视图](G21H/fig3-1.md)|architecture-concept-or-system-model|14|15|10|[24]|
|[G21H/fig4-1 · DBRM 要素——详细视图](G21H/fig4-1.md)|decomposition-or-organization-model|56|20|52|[27]|
|[G21H/fig5-1 · O-AA 构建块](G21H/fig5-1.md)|architecture-concept-or-system-model|38|3|37|[39]|
|[G21H/fig6-1 · 按 ADM 阶段的 TOGAF 内容框架](G21H/fig6-1.md)|decomposition-or-organization-model|17|0|13|[43]|
|[G21H/fig6-2 · TOGAF 架构景观分类模型汇总](G21H/fig6-2.md)|architecture-concept-or-system-model|11|0|0|[48]|
|[G21I/fig10-1 · 范围转型](G21I/fig10-1.md)|process-or-method-model|11|2|8|[44]|
|[G21I/fig4-1 · TOGAF 架构开发方法（ADM）](G21I/fig4-1.md)|process-or-method-model|10|17|0|[21]|
|[G21I/fig5-1 · SOA 治理支持 IT 治理与企业架构治理](G21I/fig5-1.md)|architecture-concept-or-system-model|4|5|0|[26]|
|[G21I/fig5-2 · MSA 治理参考模型](G21I/fig5-2.md)|process-or-method-model|7|6|6|[26]|
|[G21I/fig5-3 · SOA 参考架构](G21I/fig5-3.md)|architecture-concept-or-system-model|24|14|23|[28]|
|[G21I/fig6-1 · 界定企业架构的范围](G21I/fig6-1.md)|decomposition-or-organization-model|11|0|0|[32]|
|[G21I/fig6-2 · 项目架构](G21I/fig6-2.md)|architecture-concept-or-system-model|20|3|19|[33]|
|[G21I/fig9-1 · 微服务的开发、部署与执行](G21I/fig9-1.md)|process-or-method-model|17|4|12|[41]|
|[G233/fig3-1 · ArchiMate 业务能力元素与关系](G233/fig3-1.md)|architecture-model|16|19|2|[19]|
|[G233/fig4-1 · 零售公司组织架构图](G233/fig4-1.md)|decomposition-or-organization-model|24|23|23|[23]|
|[G233/fig4-2 · 零售组织商业模式画布](G233/fig4-2.md)|business-model-canvas|31|0|21|[24]|
|[G233/fig4-3 · 平衡计分卡](G233/fig4-3.md)|architecture-concept-or-system-model|12|4|8|[26]|
|[G233/fig4-4 · 业务对象视图](G233/fig4-4.md)|architecture-metamodel|10|10|0|[27]|
|[G233/fig5-1 · 价值流阶段示例（仓库订单履约价值流）](G233/fig5-1.md)|process-or-method-model|8|7|7|[31]|
|[G233/fig6-1 · 业务能力目录模型（示例）](G233/fig6-1.md)|decomposition-or-organization-model|27|8|24|[35]|
|[G233/fig6-2 · 把业务能力映射到价值流阶段](G233/fig6-2.md)|mapping-or-assessment-matrix|24|23|23|[35]|
|[G233/fig6-3 · 在线获取零售产品价值流](G233/fig6-3.md)|decomposition-or-organization-model|95|29|94|[39]|
|[G233/fig7-1 · 抽象化的在线获取零售产品价值流](G233/fig7-1.md)|process-or-method-model|26|4|21|[43]|
|[G233/fig7-2 · 新增激励管理应用](G233/fig7-2.md)|decomposition-or-organization-model|18|7|14|[44]|
|[G233/figB-1 · 迈克尔·波特的价值链（来源：《竞争优势》）](G233/figB-1.md)|architecture-concept-or-system-model|12|2|9|[52]|
|[G233/figC-1 · 带业务能力实例的招聘员工价值流](G233/figC-1.md)|decomposition-or-organization-model|79|29|78|[55]|
|[G234/fig2-1 · 本文档使用的 ArchiMate 建模元素](G234/fig2-1.md)|notation-or-legend|11|0|7|[12]|
|[G234/fig3-1 · 元数据管理能力——高层功能](G234/fig3-1.md)|decomposition-or-organization-model|18|0|16|[17]|
|[G234/fig4-1 · 元数据来源示意](G234/fig4-1.md)|decomposition-or-organization-model|64|0|54|[23]|
|[G234/fig4-10 · 技术元数据推断](G234/fig4-10.md)|architecture-concept-or-system-model|17|10|12|[29]|
|[G234/fig4-2 · 元数据需求收集示意](G234/fig4-2.md)|process-or-method-model|13|7|0|[24]|
|[G234/fig4-3 · 元数据质量保障方法](G234/fig4-3.md)|process-or-method-model|28|8|10|[25]|
|[G234/fig4-4 · 元数据管理 IT 方案](G234/fig4-4.md)|architecture-concept-or-system-model|34|1|28|[25]|
|[G234/fig4-5 · 关键元数据资产](G234/fig4-5.md)|mapping-or-assessment-matrix|39|0|30|[26]|
|[G234/fig4-6 · 元数据集成：集中式模型](G234/fig4-6.md)|architecture-concept-or-system-model|27|9|17|[27]|
|[G234/fig4-7 · 元数据集成：混合式模型](G234/fig4-7.md)|architecture-concept-or-system-model|24|9|14|[27]|
|[G234/fig4-8 · 元数据集成：统一式模型](G234/fig4-8.md)|architecture-concept-or-system-model|19|9|9|[28]|
|[G234/fig4-9 · 元数据集成模式](G234/fig4-9.md)|system-or-data-reference-architecture|46|22|30|[28]|
|[G234/fig5-1 · 元数据管理详细业务功能](G234/fig5-1.md)|decomposition-or-organization-model|46|0|44|[31]|
|[G234/fig5-2 · 元数据管理详细应用功能](G234/fig5-2.md)|decomposition-or-organization-model|31|0|30|[34]|
|[G238/fig1-1 · 本文档使用的 ArchiMate 建模元素](G238/fig1-1.md)|notation-or-legend|7|0|4|[11]|
|[G238/fig2-1 · BI 与分析能力——高层功能](G238/fig2-1.md)|decomposition-or-organization-model|20|0|18|[13]|
|[G238/fig3-1 · 步骤 1——现状架构](G238/fig3-1.md)|system-or-data-reference-architecture|15|13|11|[18]|
|[G238/fig3-2 · 步骤 2——引入新一代平台](G238/fig3-2.md)|system-or-data-reference-architecture|23|23|18|[20]|
|[G238/fig3-3 · 步骤 3——新一代平台成长](G238/fig3-3.md)|system-or-data-reference-architecture|23|27|18|[22]|
|[G238/fig3-4 · 步骤 4——目标架构](G238/fig3-4.md)|system-or-data-reference-architecture|23|23|18|[25]|
|[G238/fig4-1 · 利益相关者借助 BI 与分析能力追求的目标](G238/fig4-1.md)|decomposition-or-organization-model|17|0|14|[28]|
|[G238/fig4-2 · BI 与分析详细业务功能](G238/fig4-2.md)|decomposition-or-organization-model|55|0|54|[31]|
|[G238/fig4-3 · BI 与分析参考模型——详细层级](G238/fig4-3.md)|decomposition-or-organization-model|71|0|70|[35]|
|[G242/fig1-1 · 2010–2025 年全球年度产生的数据量](G242/fig1-1.md)|analytical-view|5|0|0|[21]|
|[G242/fig1-2 · 表征 ICT 行业动态的因果回路图](G242/fig1-2.md)|causal-model|12|21|0|[22]|
|[G242/fig2-1 · 本文档使用的 ArchiMate 建模记法元素](G242/fig2-1.md)|notation-or-legend|6|0|4|[26]|
|[G242/fig3-1 · 数字可持续性参考模型（高层版）——信息系统“健身计划”](G242/fig3-1.md)|architecture-concept-or-system-model|15|0|14|[31]|
|[G242/fig3-10 · 信息系统的年度环境评估（来源：The Shift Project Lean-ICT 工作组）](G242/fig3-10.md)|mapping-or-assessment-matrix|40|0|26|[61]|
|[G242/fig3-11 · 在不同层面度量信息系统的环境影响（来源：The Shift Project Lean-ICT 工作组）](G242/fig3-11.md)|process-or-method-model|18|3|13|[65]|
|[G242/fig3-12 · ICT 资产生命周期中信息系统生态系统的利益相关者](G242/fig3-12.md)|process-or-method-model|16|19|8|[67]|
|[G242/fig3-13 · 决策仓库](G242/fig3-13.md)|analytical-view|5|0|0|[77]|
|[G242/fig3-14 · AXA 企业架构治理委员会中数字可持续性评审的模板](G242/fig3-14.md)|mapping-or-assessment-matrix|20|0|15|[77]|
|[G242/fig3-15 · 分布式治理模型示意图（来源：The Shift Project Lean-ICT 工作组）](G242/fig3-15.md)|decomposition-or-organization-model|11|3|7|[78]|
|[G242/fig3-16 · 可持续信息系统的治理原则（来源：The Shift Project Lean-ICT 工作组）](G242/fig3-16.md)|analytical-view|9|0|0|[79]|
|[G242/fig3-2 · 数字可持续性的关键文化轴](G242/fig3-2.md)|analytical-view|5|4|0|[35]|
|[G242/fig3-3 · 风险、责任与 CIO 的角色](G242/fig3-3.md)|analytical-view|7|4|2|[41]|
|[G242/fig3-4 · 架构层与碳排放](G242/fig3-4.md)|architecture-concept-or-system-model|9|4|7|[47]|
|[G242/fig3-5 · 结合自上而下与自下而上的方法以捕获数字可持续性需求](G242/fig3-5.md)|process-or-method-model|14|6|6|[48]|
|[G242/fig3-6 · 数字可持续性举措中非功能需求的变化](G242/fig3-6.md)|analytical-view|16|3|13|[50]|
|[G242/fig3-7 · 为实现可持续而应施加的四类约束](G242/fig3-7.md)|architecture-concept-or-system-model|15|7|7|[51]|
|[G242/fig3-8 · 可持续信息系统的交付（来源：The Shift Project，工作组产出）](G242/fig3-8.md)|process-or-method-model|23|4|16|[56]|
|[G242/fig3-9 · GHG Protocol 的范围与价值链排放概览 [Value Chain]](G242/fig3-9.md)|process-or-method-model|32|7|24|[60]|
|[G242/fig5-1 · 数字可持续性参考模型（详细版）（来源：The Shift Project Lean-ICT 工作组）](G242/fig5-1.md)|decomposition-or-organization-model|44|0|43|[91]|
|[G248/fig2-1 · 企业变革画像](G248/fig2-1.md)|analytical-view|14|0|8|[14]|
|[G248/fig2-2 · TOGAF 过渡架构的实体关系图（ERD）](G248/fig2-2.md)|architecture-metamodel|6|10|0|[16]|
|[G248/fig2-3 · 包含 MVP 与 MMP 概念的 TOGAF 过渡架构 ERD](G248/fig2-3.md)|architecture-metamodel|9|17|0|[17]|
|[G248/fig3-1 · TOGAF 企业元模型 [C220]](G248/fig3-1.md)|architecture-metamodel|42|69|37|[19]|
|[G248/fig6-1 · 架构层级、角色与域关系的实体关系图](G248/fig6-1.md)|architecture-metamodel|20|24|1|[29]|
|[G249/fig4-1 · 架构角色及其关系](G249/fig4-1.md)|decomposition-or-organization-model|14|17|6|[16]|
|[G249/fig4-2 · 架构层级概念的实体关系图](G249/fig4-2.md)|architecture-metamodel|22|21|10|[21]|
|[G198/image-p0015-01 · 四个技能熟练等级的定义与颜色图例。等级1至4分别为背景、认知、知识、专家；各技能矩阵的数值和底色都使用该量表。](G198/image-p0015-01.md)|notation-or-legend|4|0|0|[15]|
|[G198/image-p0016-01 · 技能与架构角色熟练度矩阵：Generic Skills。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0016-01.md)|role-skill-matrix|18|80|0|[16]|
|[G198/image-p0016-02 · 技能与架构角色熟练度矩阵：Business Skills & Methods。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0016-02.md)|role-skill-matrix|21|110|0|[16]|
|[G198/image-p0017-01 · 技能与架构角色熟练度矩阵：Enterprise Architecture Skills。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0017-01.md)|role-skill-matrix|29|190|0|[17]|
|[G198/image-p0017-02 · 技能与架构角色熟练度矩阵：Program or Project Management Skills。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0017-02.md)|role-skill-matrix|15|50|0|[17]|
|[G198/image-p0018-01 · 技能与架构角色熟练度矩阵：IT General Knowledge Skills。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0018-01.md)|role-skill-matrix|28|180|0|[18]|
|[G198/image-p0018-02 · 技能与架构角色熟练度矩阵：Technical IT Skills。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0018-02.md)|role-skill-matrix|23|130|0|[18]|
|[G198/image-p0019-01 · 技能与架构角色熟练度矩阵：Legal Environment。行是技能，列是十种角色，单元格为原图1–4级要求。颜色依次为黄、绿、蓝、红；数值不得相加解释为技能总分。](G198/image-p0019-01.md)|role-skill-matrix|15|50|0|[19]|
|[G212/image-p0046-01 · 表6-1（架构影响）内的采用因素标签：Vision。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase A: Architecture Vision。](G212/image-p0046-01.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-02 · 表6-1（架构影响）内的采用因素标签：Sponsorship & Direction。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase A: Architecture Vision。](G212/image-p0046-02.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-03 · 表6-1（架构影响）内的采用因素标签：Business Rationale。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase B: Business Architecture。](G212/image-p0046-03.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-04 · 表6-1（架构影响）内的采用因素标签：Scope & Scale。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase B: Business Architecture。](G212/image-p0046-04.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-05 · 表6-1（架构影响）内的采用因素标签：Funding & Resources。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase B: Business Architecture。](G212/image-p0046-05.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-06 · 表6-1（架构影响）内的采用因素标签：Business Model Adaptability。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase B: Business Architecture。](G212/image-p0046-06.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-07 · 表6-1（架构影响）内的采用因素标签：Culture。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase B: Business Architecture。](G212/image-p0046-07.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-08 · 表6-1（架构影响）内的采用因素标签：Value Realization。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase C: Information Systems Architecture。](G212/image-p0046-08.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-09 · 表6-1（架构影响）内的采用因素标签：Skills & Competence¹。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase C: Information Systems Architecture。](G212/image-p0046-09.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-10 · 表6-1（架构影响）内的采用因素标签：Policy & Regulations。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase C: Information Systems Architecture。](G212/image-p0046-10.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-11 · 表6-1（架构影响）内的采用因素标签：Governance & Compliance¹。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase C: Information Systems Architecture。](G212/image-p0046-11.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0046-12 · 表6-1（架构影响）内的采用因素标签：Ecosystem¹。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase C: Information Systems Architecture。](G212/image-p0046-12.md)|architecture-phase-mapping|2|1|0|[46]|
|[G212/image-p0047-01 · 表6-1（架构影响）内的采用因素标签：IT Capability。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase D: Technology Architecture。](G212/image-p0047-01.md)|architecture-phase-mapping|2|1|0|[47]|
|[G212/image-p0047-02 · 表6-1（架构影响）内的采用因素标签：Technology Maturity。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase D: Technology Architecture。](G212/image-p0047-02.md)|architecture-phase-mapping|2|1|0|[47]|
|[G212/image-p0047-03 · 表6-1（架构影响）内的采用因素标签：Skills & Competence²。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase D: Technology Architecture。](G212/image-p0047-03.md)|architecture-phase-mapping|2|1|0|[47]|
|[G212/image-p0047-04 · 表6-1（架构影响）内的采用因素标签：Governance & Compliance²。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase D: Technology Architecture。](G212/image-p0047-04.md)|architecture-phase-mapping|2|1|0|[47]|
|[G212/image-p0047-05 · 表6-1（架构影响）内的采用因素标签：Ecosystem²。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase D: Technology Architecture。](G212/image-p0047-05.md)|architecture-phase-mapping|2|1|0|[47]|
|[G212/image-p0047-06 · 表6-1（架构影响）内的采用因素标签：Implementation Approach。该标签与同一表格行的ADM阶段相关；上标1指数据与应用能力，上标2指技术能力。 原图所在表格行明确对应 Phase F: Migration Planning。](G212/image-p0047-06.md)|architecture-phase-mapping|2|1|0|[47]|
|[G212/image-p0049-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0049-02.md)|assessment-response-form|7|6|0|[49]|
|[G212/image-p0049-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0049-03.md)|assessment-response-form|7|6|0|[49]|
|[G212/image-p0050-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-01.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0050-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-02.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0050-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-03.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0050-04 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-04.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0050-05 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-05.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0050-06 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-06.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0050-07 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0050-07.md)|assessment-response-form|7|6|0|[50]|
|[G212/image-p0051-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-01.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0051-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-02.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0051-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-03.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0051-04 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-04.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0051-05 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-05.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0051-06 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-06.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0051-07 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0051-07.md)|assessment-response-form|7|6|0|[51]|
|[G212/image-p0052-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0052-01.md)|assessment-response-form|7|6|0|[52]|
|[G212/image-p0052-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0052-02.md)|assessment-response-form|7|6|0|[52]|
|[G212/image-p0052-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0052-03.md)|assessment-response-form|7|6|0|[52]|
|[G212/image-p0052-04 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0052-04.md)|assessment-response-form|7|6|0|[52]|
|[G212/image-p0052-05 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0052-05.md)|assessment-response-form|7|6|0|[52]|
|[G212/image-p0053-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0053-01.md)|assessment-response-form|7|6|0|[53]|
|[G212/image-p0053-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0053-02.md)|assessment-response-form|7|6|0|[53]|
|[G212/image-p0053-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0053-03.md)|assessment-response-form|7|6|0|[53]|
|[G212/image-p0053-04 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0053-04.md)|assessment-response-form|7|6|0|[53]|
|[G212/image-p0053-05 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0053-05.md)|assessment-response-form|7|6|0|[53]|
|[G212/image-p0053-06 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0053-06.md)|assessment-response-form|7|6|0|[53]|
|[G212/image-p0054-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-01.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0054-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-02.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0054-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-03.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0054-04 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-04.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0054-05 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-05.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0054-06 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-06.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0054-07 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0054-07.md)|assessment-response-form|7|6|0|[54]|
|[G212/image-p0055-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0055-01.md)|assessment-response-form|7|6|0|[55]|
|[G212/image-p0055-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0055-02.md)|assessment-response-form|7|6|0|[55]|
|[G212/image-p0055-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0055-03.md)|assessment-response-form|7|6|0|[55]|
|[G212/image-p0055-04 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0055-04.md)|assessment-response-form|7|6|0|[55]|
|[G212/image-p0055-05 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0055-05.md)|assessment-response-form|7|6|0|[55]|
|[G212/image-p0055-06 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0055-06.md)|assessment-response-form|7|6|0|[55]|
|[G212/image-p0056-01 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0056-01.md)|assessment-response-form|7|6|0|[56]|
|[G212/image-p0056-02 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0056-02.md)|assessment-response-form|7|6|0|[56]|
|[G212/image-p0056-03 · 问卷的七点同意程度选项，从左到右由完全同意到完全不同意。七个空心圆表示待填写选项；不能当作已选答案或调查数据。对应题干请读同页紧邻上方文字。](G212/image-p0056-03.md)|assessment-response-form|7|6|0|[56]|
|[G21B/image-p0029-01 · 表4-2架构愿景维度的配图，所在行维度为 C-MDM Team。图案分别用于提示团队、单一真相来源、质量持续改进及伙伴关系；实际约束来自表格正文。](G21B/image-p0029-01.md)|architecture-context-symbol|1|0|0|[29]|
|[G21B/image-p0029-02 · 表4-2架构愿景维度的配图，所在行维度为 Single point of reputed truth system。图案分别用于提示团队、单一真相来源、质量持续改进及伙伴关系；实际约束来自表格正文。](G21B/image-p0029-02.md)|architecture-context-symbol|1|0|0|[29]|
|[G21B/image-p0029-03 · 表4-2架构愿景维度的配图，所在行维度为 Data quality and trust measures。图案分别用于提示团队、单一真相来源、质量持续改进及伙伴关系；实际约束来自表格正文。](G21B/image-p0029-03.md)|architecture-context-symbol|1|0|0|[29]|
|[G21B/image-p0029-04 · 表4-2架构愿景维度的配图，所在行维度为 Business positive impacts ensured, from payer to partner。图案分别用于提示团队、单一真相来源、质量持续改进及伙伴关系；实际约束来自表格正文。](G21B/image-p0029-04.md)|architecture-context-symbol|1|0|0|[29]|
|[G233/image-p0019-02 · 表3-1中的ArchiMate Application Component 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0019-02.md)|notation-or-legend|1|0|0|[19]|
|[G233/image-p0019-03 · 表3-1中的ArchiMate Application Component 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0019-03.md)|notation-or-legend|1|0|0|[19]|
|[G233/image-p0019-04 · 表3-1中的ArchiMate Application Process 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0019-04.md)|notation-or-legend|1|0|0|[19]|
|[G233/image-p0019-05 · 表3-1中的ArchiMate Application Process 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0019-05.md)|notation-or-legend|1|0|0|[19]|
|[G233/image-p0020-01 · 表3-1中的ArchiMate Capability 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-01.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-02 · 表3-1中的ArchiMate Capability 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-02.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-03 · 表3-1中的ArchiMate Business Event 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-03.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-04 · 表3-1中的ArchiMate Business Event 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-04.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-05 · 表3-1中的ArchiMate Business Object 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-05.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-06 · 表3-1中的ArchiMate Business Object 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-06.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-07 · 表3-1中的ArchiMate Data Object 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-07.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-08 · 表3-1中的ArchiMate Data Object 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-08.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-09 · 表3-1中的ArchiMate Business Process 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-09.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-10 · 表3-1中的ArchiMate Business Process 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-10.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-11 · 表3-1中的ArchiMate Business Role 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-11.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-12 · 表3-1中的ArchiMate Business Role 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-12.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-13 · 表3-1中的ArchiMate Goal 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-13.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-14 · 表3-1中的ArchiMate Goal 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-14.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-15 · 表3-1中的ArchiMate Outcome 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-15.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-16 · 表3-1中的ArchiMate Outcome 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-16.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-17 · 表3-1中的ArchiMate Resource 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-17.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0020-18 · 表3-1中的ArchiMate Resource 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0020-18.md)|notation-or-legend|1|0|0|[20]|
|[G233/image-p0021-01 · 表3-1中的ArchiMate Stakeholder 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0021-01.md)|notation-or-legend|1|0|0|[21]|
|[G233/image-p0021-02 · 表3-1中的ArchiMate Stakeholder 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0021-02.md)|notation-or-legend|1|0|0|[21]|
|[G233/image-p0021-03 · 表3-1中的ArchiMate Value 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0021-03.md)|notation-or-legend|1|0|0|[21]|
|[G233/image-p0021-04 · 表3-1中的ArchiMate Value 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0021-04.md)|notation-or-legend|1|0|0|[21]|
|[G233/image-p0021-05 · 表3-1中的ArchiMate Value Stream 元素的带标签图形。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0021-05.md)|notation-or-legend|1|0|0|[21]|
|[G233/image-p0021-06 · 表3-1中的ArchiMate Value Stream 元素的独立图标。这是记法示例，不是项目实体实例；含义与使用方式在表3-1同行。](G233/image-p0021-06.md)|notation-or-legend|1|0|0|[21]|
|[G234/image-p0028-02 · 元数据集成图的图例：堆叠圆柱图标表示 Existing Metadata Sources（既有元数据来源），用于解释邻近集成模型里的来源符号。](G234/image-p0028-02.md)|notation-or-legend|1|0|0|[28]|

## 关系读取规则

1. `nodes` 保存所有实体；`edges` 保存所有原始关系与本轮规范化后的方向。
2. `hierarchy.containment_and_grouping` 是图中的包含或分组；业务组成在 `semantic_hierarchy`。
3. `organizational_reporting_edge_ids` 只保存有明确汇报语义的边；`governance_edge_ids` 表示治理职责。
4. `instantiation_edge_ids` 表示类型与实例，不等同子类型分解。
5. `source_relation` 保留原字段，`corrections` 解释修改；不确定性沿用并显示，不凭空补齐。
6. `hierarchy.views` 为五种层级分别计算根、直接父子、最短根深度、多父项及循环状态。
7. 原图和可编辑语义图均保留；语义图的重排位置本身没有业务意义。
