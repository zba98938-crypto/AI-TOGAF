# G249 任务、角色、技能与证据运行契约

G249 提供人的角色、技能和熟练度框架。本文件、数据字段、任务路由和运行检查是项目操作设计，不是官方规定的算法，也不把生成图表等同于人员胜任力。复用现有 `architecture-role-skill-assessment` 方法、`architecture-role-catalog`、`architecture-skill-matrix`、`architecture-development-plan` 和团队容量计划，不新增 71 个 AI 技能。

官方依据：G249 §3 的授权、任务与技能经验匹配、正式认可和发展路径；§4 的岗位/角色/任务区别与人员多角色；§5 的角色参考矩阵；§6 的企业裁剪。专业实施细节仍属于 §2 所述业务、技术和服务管理专业人员。Open CA 认证等级独立于四级熟练度。

## 调用与输入

在标准项目模型的 `analyses` 中使用 `method_id: architecture-role-skill-assessment`，通过正常入口运行：

```sh
python skills/_shared/scripts/analyze.py model.json --evaluate g249-assessment
```

完整虚构原料见 [role-skill-inputs.json](../../examples/g249-omnichannel/role-skill-inputs.json)。该文件由综合案例构建器补齐共享架构对象快照和模型绑定；单独调用 `evaluate(analysis)` 可检查输入，但不证明它与某个项目模型一致。正式生成和项目评审应始终传入模型。

| 输入 | 关键字段及含义 |
|---|---|
| `source_ids` | 本次材料清单；所有 evidence 引用必须存在，传入模型时必须也在 model.sources 中 |
| `scope`, `as_of` | 评审范围和 ISO 日期；不能用运行机器当天日期替代明确业务时点 |
| `mandate` | id、scope、decision_owner、evidence；表示声明的委托依据，不由工具授予权限 |
| `roles` | id、名称、类别和范围；类别不等于固定人事职级 |
| `tasks` | id、scope、decision、outcome、role_refs、required_skill_ids、method_ids、artifact_ids、evidence；workload_hours 未知保持 null |
| `requirements` | id、task_ref、role_ref、skill_id、assessment_kind、assessment_state、proficiency、scale_id、behavioral_criteria、tailoring_reason、evidence |
| `assessments` | id、person_ref、skill_id、task_refs、observed_on、assessor、assessment_kind、assessment_state、proficiency、scale_id、behavioral_evidence、evidence |
| `assignments` | id、person_ref、role_ref、task_refs、requirement_refs、assessment_refs、mandate_ref、authority、valid_from、valid_until、available_hours、evidence；support 为待评审专家支持方案 |
| `development` | id、person、role、skill_id、task_refs、requirement_refs、current_proficiency、target_proficiency、scale_id、behavioral_gap、action、owner、due、success_criteria、reassessment（assessor/due_on/criteria/status: planned或completed）、history、evidence |
| `interpretations` | 歧义来源词的 id、skill_id、definition、adopted_by、evidence；例如 Optimistic/ Pessimistic Patterns，原文未给定义，不自行改写成特定技术模式 |
| `scales` | 自定义量表 id 为 project-name-vN，anchors 为含 value: 1/2/3/4 与 meaning 的四条记录，evidence 为采用依据；官方量表为 G249-table5-1 |

行为证据记录形如 `{"criterion":"独立完成异常接口设计并经评审","demonstrated":true,"evidence":["SRC-REVIEW"]}`。criterion 对应要求中的行为判据。工具核验已声明记录及追溯，不从叙述自动猜测 demonstrated 或评级，也不能核验文档叙述是否真实。

`source_reference_target/reference` 只表示原表参考目标，必须给出 `reference_role_ref` 且数值与官方格子匹配。`tailored_target/proposed|adopted` 才是项目目标。人员记录只能使用 `observed_assessment`；状态为 unassessed、evidence_insufficient 时 proficiency 必须 null，assessed 或 superseded 的评级需行为、评审人和日期证据。未提供三级证据不意味着已经证明二级。不同量表的数字不可直接比较。

## 推理、输出及边界

1. 先识别委托、任务结果和角色责任，再按任务声明技能要求。71 项路由给出候选方法/制品，不能自动决定本项目目标等级。
2. 每项要求绑定任务、角色、技能、量表和行为判据；参考值未被采用时不会进入已满足判断。
3. 对显式选择的人员观察，核查人员一致、当前有效、任务适用、相同量表、已声明等级及逐项行为证据。只做序数比较，不减出“缺口分数”、不平均、不与容量相乘。
4. 任务分配必须覆盖该角色在选定任务上的全部已声明要求；遗漏要求产生缺口。专家支持单独核查人员、技能和行为证据，始终交责任方决定支持方案，不提高被支持者等级。
5. 容量仅在同一分配期间的可用小时和工作量都已提供时比较。无工作量为 unresolved，已知不足为 insufficient；能力和容量分别输出。
6. 发展计划连接具体行为缺口、行动和成功判据。标记完成必须关联同人同技能的新评审并保留历史；参加培训、完成活动不自动产生新等级。

发展计划的 `success_criteria` 与 `reassessment.criteria` 都须覆盖当前关联要求的 `behavioral_criteria`。要求带 `requirement_version` 或 `version` 时，发展计划用 `requirement_versions` 按要求 ID 记录采用的版本；条件或版本落后时返回 `development-criteria-outdated` 或版本缺口，不能维持“已满足”的判断。制品中未评价的现状保留 `current_proficiency: null`，并明确 `current_assessment_state: unassessed` 或 `evidence_insufficient`；这不是最低等级。

输出包括 `task_routes`、`requirement_reviews`、`assessment_reviews`、`assignment_reviews`、`development_reviews` 和带稳定 ID 的 `gaps`。`ready-for-owner-review` 仅表示声明资料满足当前操作契约，`approval` 始终为 `not-granted`。缺失输入保留草稿；悬空引用、错人证据、非法等级、互相矛盾的记录则拒绝执行。

## 共享模型绑定

`inputs.model_binding` 使用 `{"version":"g249-assessment-binding/1","context_ref":"G249-ASSESSMENT-CONTEXT"}`。模型中同 ID 的 `guide:g249-assessment-context` 实体，其 `attributes.assessment_inputs` 必须与完整 inputs 严格相等。`architecture-work-assignment-review` 视图引用这个实体与同一 analysis ID。

每个任务的 `model_object_refs` 指向项目现有对象；`inputs.model_objects` 保存这些对象的完整快照，其集合必须恰好覆盖所有任务引用。inputs.model_relationships 同时保存上述对象范围内（两端都在范围内）的全部关系快照，新增、删除或变更关系均需重新同步。对象版本、属性、证据或分析上下文发生变化后，旧快照不能继续通过 `analyze.py` 或生成链的绑定检查。更新时先复核业务影响，再同步上下文和快照。

`inputs.model_views` 保存任务 `artifact_ids` 对应的当前实际视图快照。角色声明需要某类制品时，必须存在该类视图；遗漏视图返回缺口，变更或删除已绑定视图会使旧分析失效。未声明此字段的旧输入可作草稿读取，并返回迁移缺口，不自动补快照或升级通过状态。示例和组合视图的 `supporting_views` 应与主视图一起装入模型。

## 角色关系与 KPI

`architecture-role-catalog-review` 的 `roles[].relationships` 使用以下类型，含 id、target、scope、evidence：

| 类型 | 语义与附加条件 |
|---|---|
| architecture_guidance | 专业指导，不自动是汇报线 |
| architecture_constraint | 上位架构对工作的约束，不自动赋予人事权限 |
| specialization | 角色类型特化，例如首席是企业架构师特例 |
| collaborates_with | 协作，允许跨类别和同类别 |
| reports_to | 明确的人事汇报，补 authority、valid_from、valid_until；已声明循环为结构错误 |
| handoff | 交接，补 deliverable_ref、acceptance_criteria、authority |

旧 `leads` 只产生 untyped-legacy-lead 缺口。可选 `hierarchy_policy` 只能为显式 project-adopted 的 strict-tier 策略，附 evidence、完整 tier_order 和 applies_to: [architecture_guidance]。它不能限制特化、协作或人事汇报。若在模型中采用该策略、as_of 或 tier_tailoring_reason，`policy_context_ref` 要指向一个 repository_asset，其 attributes.role_review_context 严格保存这些已提供字段。

人员分配 `roles[].assignments` 记录 person_ref、job_ref、task_refs、authority、valid_from、valid_until、evidence；角色定义本身不授予人员权限。KPI 除 measure、target、target_origin 和 evidence 外，应有 unit、measurement_period、measurement_source、owner、formula_or_rule；project-adopted 目标还需 adopted_by。缺测量口径或来源保留缺口，不因写出“3/5”就认为可衡量。

角色协作图的全局关系 ID、端点、类型、scope 和 evidence 与目录中的类型关系绑定；图形位置不能补造领导线。全部测试见 `tests/test_g249_reasoning.py`。
