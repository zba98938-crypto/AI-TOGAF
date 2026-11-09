# togaf-ea-capability 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `architecture-maturity-model` | 对「架构成熟度模型」给出：ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级 | `missing-evidence` | ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级 | — |
| `architecture-maturity-scorecard` | 对「架构成熟度评分卡」给出：加权等级与各级达成百分比是互补结果，不能互相替代 | `missing-evidence` | 加权等级与各级达成百分比是互补结果，不能互相替代 | — |
| `digital-adoption-position` | 对「数字技术采用定位」给出：ABCD 不是由低到高的优劣或成熟度等级 | `missing-evidence` | ABCD 不是由低到高的优劣或成熟度等级 | — |
| `digital-readiness-questionnaire` | 对「数字技术就绪度问卷」给出：问卷答案不是客观测量值，需说明参与者与共识过程 | `missing-evidence` | 问卷答案不是客观测量值，需说明参与者与共识过程 | — |
| `digital-readiness-assessment` | 对「数字技术就绪度评估」给出：没有来源或用户规则时不创建统一总分合格线 | `missing-evidence` | 没有来源或用户规则时不创建统一总分合格线 | — |
| `readiness-consequence-analysis` | 对「就绪度因素后果分析」给出：背景重复因素列表不表示全连接依赖，后果未自带概率和严重度 | `duplicate-id` | 背景重复因素列表不表示全连接依赖，后果未自带概率和严重度 | — |
| `adoption-factor-progression` | 对「采用因素递进路线」给出：射线长度和角度不是定量评分，因素层次不等于 ADM 阶段 | `missing-evidence` | 射线长度和角度不是定量评分，因素层次不等于 ADM 阶段 | — |
| `ea-service-catalog` | 对「企业架构服务目录」给出：候选服务不是每个 EA 团队必须提供的服务清单 | `missing-evidence` | 候选服务不是每个 EA 团队必须提供的服务清单 | — |
| `ea-value-map` | 对「EA 与企业价值地图」给出：相关性或贡献假设不能直接断言为确定收益因果 | `missing-evidence` | 相关性或贡献假设不能直接断言为确定收益因果 | — |
| `ea-team-capacity-plan` | 对「EA 团队容量计划」给出：人数不等于可用容量，技能熟练度不等于工时 | `missing-evidence` | 人数不等于可用容量，技能熟练度不等于工时 | — |
| `enterprise-framework-alignment-catalog` | 因框架知名就标企业已采用 | `reject-unsupported-commitment` |  | — |
| `business-cycle-product-alignment` | 无消费方期限，只写“阶段F完成” | `missing-evidence` | missing-consumer-deadline拒绝准时判定 | missing-consumer-deadline拒绝准时判定 |
| `value-realization-assessment` | 实际为全部站点而基线只有城西站 | `missing-evidence` | incomparable-measurement-scope；停止差额计算 | incomparable-measurement-scope；停止差额计算 |
| `project-learning-record` | 仅写“沟通不好，要加强沟通”无预期实际和证据 | `learning-evidence-gap` |  | — |
| `sustainability-capability-assessment` | 无评分模型却给成熟度3/5 | `unsourced-maturity-rating` |  | — |
| `ea-point-of-view-register` | 对「EA观点文件与影响经营登记」给出：名称、来源表格和成功输出不等于业务结论已核实 | `missing-evidence` | 名称、来源表格和成功输出不等于业务结论已核实 | — |
| `architecture-repository-structure` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `architecture-landscape-projection` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `repository-state-view-tree` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `repository-parallel-candidates` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `capability-project-continuum` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `portfolio-stakeholder-concern-matrix` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `repository-target-baseline-comparison` | 从所选对象删除必需的definition属性，保留其稳定ID及视图选择。 | `missing-profile-attribute` | 缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | — |
| `dtra-adm-phase-alignment` | 文化评分写为9 | `DAP-002` | DAP-002 [culture]: Rating must be 1-7 (G212 Table A-1) | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `architecture-maturity-model` | 在「架构成熟度模型」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `architecture-maturity-scorecard` | 在「架构成熟度评分卡」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `digital-adoption-position` | 在「数字技术采用定位」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `digital-readiness-questionnaire` | 在「数字技术就绪度问卷」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `digital-readiness-assessment` | 在「数字技术就绪度评估」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `readiness-consequence-analysis` | 在「就绪度因素后果分析」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `adoption-factor-progression` | 在「采用因素递进路线」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `ea-service-catalog` | 在「企业架构服务目录」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `ea-value-map` | 在「EA 与企业价值地图」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `ea-team-capacity-plan` | 在「EA 团队容量计划」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `enterprise-framework-alignment-catalog` | 风险部门新增正式架构风险字段与月度回执 | 缺口关闭为已建立接触点，附使用证据；不改变COBIT未知状态 |
| `business-cycle-product-alignment` | 组合选项计划从11月16改为11月12 | 迟3天变提前1天；实际仍unknown |
| `value-realization-assessment` | 人工签收实际工时620改为480且保持口径 | 观察改善320小时，目标超额20小时；归因仍未证实，晚送率仍未达成 |
| `project-learning-record` | 下一项目采用模板后同范围清单确认8天、返工1次 | 记录试点结果和可比性，改进证据增强但不能由单例证明普遍因果 |
| `sustainability-capability-assessment` | 环境职责经确认并有首次评审记录 | 治理当前证据更新、缺口缩小，但六维仍无数字评分 |
| `ea-point-of-view-register` | 在「EA观点文件与影响经营登记」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `architecture-repository-structure` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `architecture-landscape-projection` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `repository-state-view-tree` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `repository-parallel-candidates` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `capability-project-continuum` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `portfolio-stakeholder-concern-matrix` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `repository-target-baseline-comparison` | 修改同ID对象的definition，保持结构角色、类别和边界属性不变。 | reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。 |
| `dtra-adm-phase-alignment` | 删除阶段B的文化行动 | 分析结果变化：新增缺口attention:culture |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `acmm-maturity-assessment` | 执行「ACMM 成熟度评价」时跳过或误做：无显式权重与规则不计算统一总分 | `missing-evidence` | 无显式权重与规则不计算统一总分 | — |
| `dtra-readiness-method` | 执行「DTRA 就绪度评价与后果」时跳过或误做：不自造统一总分通过线，采用类型不是成熟度 | `relation-endpoint-type` | 不自造统一总分通过线，采用类型不是成熟度 | — |
| `ea-service-emergence-npd-method` | 执行「EA服务N／P／D语境矩阵分析」时跳过或误做：记录项目证据与原图证据两个状态，不混称相同 | `mixed-evolution` | 记录项目证据与原图证据两个状态，不混称相同 | — |
| `ea-service-adm-evidence-map-method` | 执行「EA服务与ADM证据映射分析」时跳过或误做：未知原图格不推断不适用或唯一阶段 | `missing-evidence` | 未知原图格不推断不适用或唯一阶段 | — |
| `ea-point-of-view-review` | 执行「EA观点文件与影响经营登记审查」时跳过或误做：point of view经营不等同于viewpoint library | `missing-evidence` | point of view经营不等同于viewpoint library | — |
| `dtra-adm-phase-alignment-review` | 文化评分写为9 | `DAP-002` | DAP-002 [culture]: Rating must be 1-7 (G212 Table A-1) | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
