# 从明确选择的模型内容组装交付物

v2交付物可以声明 `assembly`，使章节正文从所选模型记录及分析结果生成。原有 `sections` 字符串保留为人工背景，不再作为模型结果或验收证明。未启用组装的v1与旧v2文件继续兼容；推荐制品缺失仍使用原有警告。

```json
{
  "id": "delivery-principles",
  "deliverable_id": "architecture-principles",
  "title": "项目架构原则",
  "view_ids": ["view-project-principles"],
  "entity_ids": [],
  "sections": {},
  "approval_status": "candidate",
  "implementation_status": "not-started",
  "assembly": {
    "rules_version": "1.0",
    "mode": "strict",
    "analysis_ids": [],
    "active_groups": [],
    "section_bindings": {}
  }
}
```

`view_ids` 引用实际视图实例，不能填制品族或规范ID。组装器只读取这些视图，以及 `section_bindings` 明确增加的视图/对象/分析ID。它不会按 `related_deliverables` 把全库可选能力自动纳入。单项交付物的生成器应先获取 `dependency_closure(model, deliverable_instance)`，生成其中的实际视图和分析。

规则在 [deliverable-assembly-rules.json](../capability-addenda/deliverable-assembly-rules.json)，包括22项交付物的全部章节、核心支撑与条件组。条件组只在相应规范的实际视图被选择，或 `active_groups` 明确声明适用时启用。章节和条件组指定了 `profile_ids` 时按规范精确匹配，不能用同制品族的其他规范代替。核心最低支撑可以按声明的制品族或规范选项匹配。能力评估分别支持业务能力、ACMM、DTRA或可持续六维输入，不强迫不同评估分支使用同一量尺或同时选全。

`assembly.section_bindings` 以正式章节标题为键，每项可含 `view_ids`、`entity_ids`、`analysis_ids`。显式绑定不匹配该章项目选择器（含关联条件组）时，必须额外给出 `override: {"reason":"项目选择理由", "owner":"责任人", "evidence":["已有来源ID"]}`；无理由绑定不能把地点目录冒充ABB职责。任何出现的override均核对完整性及来源存在性，理由和来源定位进入该章正文。这是可追溯项目裁剪，不声明内容等价、官方允许或已批准。没有专门章节匹配的明确选择记录会在最后一节标为补充模型证据，不会丢弃。生成正文包含对象实际属性、关系方向和每端基数、命名状态、来源定位及分析输入哈希。改变对象字段后正文随之改变；计算只执行明确选择且有可执行方法的分析。未知方法或不足输入产生带ID的缺口。

可选的 `scope_id` 和 `state_ids` 将交付物约束到指定范围及命名状态。所选视图缺少相应声明或超出范围时，组装器报告缺口，不静默扩大范围。一个范围/状态的视图不能因制品族相同而替代另一个实际视图。

核心支撑需要裁剪时，使用 `tailoring` 记录 `requirement_id`、`reason`、`owner`、`evidence`，依据ID必须存在于模型来源。裁剪只记录项目选择，不推断批准或TOGAF的普遍豁免。没有依据或责任人的裁剪仍产生缺口。

`assemble(model, deliverable_instance, contract, rules)` 返回：

- `section_blocks`：正式章节标题、动态Markdown及对象/关系/来源/视图/分析ID。
- `required_view_ids`、`required_analysis_ids`：此次交付物的明确依赖闭包。
- `analysis_results`：只包含本次选择分析的实际计算结果与输入哈希。
- `gaps`：带交付物、对象和缺口ID的不足输入、规则冲突或不可计算事项。
- `status`：`blocked`、`draft-with-gaps`、`assembled-awaiting-review`，或未启用时的 `legacy-unassembled`。
- `assembly_provenance`：实际模型版本、模型哈希、规则版本及规则哈希。
- `section_coverage`：每章实际绑定的view/analysis/entity及 `bound-not-business-accepted`、`narrative-only-unverified` 或 `unbound` 状态；最后一章的补充证据不自动满足其章节主题。
- `unbound_section_titles`、`content_status`：显式未绑定章节及内容证据状态。即使无编码阻断，仍可能为 `sections-unbound-review-required`；全部绑定也只能是 `all-sections-bound-business-review-pending`，不是业务完整通过。

## 选择加入的项目章节事实

路灯17章案例（历史材料已清理）演示 `project:section_evidence`：在模型extensions声明含义，section_bindings只引用该章实际实体。该类型是项目结构契约，不是官方新工作产品。attributes须有匹配的deliverable_id/section_title，非空decision/scope/owner/acceptance/status、显式unknowns数组及可定位的来源ID。缺字段或跨章误绑会阻断严格组装；一般既有实体不受此项目契约影响。

使用该类型的章节会额外输出project_record_findings和未决输入表，组装结果含unresolved_project_record_ids。已知存在未知输入时只计候选有内容记录，不算内容已完成。声明无未知也只是待业务评审，不能把空unknowns当作已批准。完整交付物所需核心视图若不在附录范围，应明确裁剪并说明限制，不允许悄悄以附录冒充完整文档。

严格模式出现缺口时返回 `blocked`，生成器必须拒绝发布交付正文；草稿模式返回 `draft-with-gaps`，把相同缺口写入正文并保留警告。`assembled-awaiting-review` 只表示本次结构化组装没有编码规则缺口，不能推断业务评审、签署、批准或实施完成。模型事实和人工背景矛盾时仍须架构师评审；组装器没有自动自然语言事实验证能力。

本轮独立审计见22交付物与106工作产品去向（历史材料已清理），记录修复前的10个直接无依据章及补充证据归属边界。当前覆盖口径更严格：补充证据不冒充本章依据，因此实际未绑定数应读取最新生成记录，不能直接沿用旧计数。

工程证据见 组装测试记录（历史材料已清理）及 测试代码（历史材料已清理）。之前仅复制章节及附链接的问题、逐22项依据和修改探针保存在 整合审计（历史材料已清理），作为修复前记录。
