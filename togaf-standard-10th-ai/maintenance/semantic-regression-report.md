# 已发布语料与本地案例的语义回归

执行结果：**passed**；36 项，36 通过，0 失败。

执行时间：2026-11-08T09:59:10.095192+00:00

重跑：`python3 togaf-standard-10th-ai/maintenance/semantic-regression.py`

7 张已发布图及其当前检索；本地全渠道案例 build/validate/evaluate；已识别误读的正例与内存反例。

| 检查 | 结果 | 实际观察 |
|---|---|---|
| PUB-G188/fig4-2 | passed | {"rejected_ADM_sequences": 9, "communication_plan_producer": "G188/fig4-2#adm_soaw", "scope": "图中关系；不消除邻近正文的源文冲突"} |
| RAG-G188/fig4-2 | passed | {"rejected_ADM_sequences": 9, "communication_plan_producer": "G188/fig4-2#adm_soaw", "scope": "图中关系；不消除邻近正文的源文冲突", "retrieval_parts": 55} |
| PUB-G188/fig5-1 | passed | {"rejected_ADM_sequences": 9, "communication_plan_producer": "G188/fig5-1#adm_soaw", "scope": "图中关系；不消除邻近正文的源文冲突"} |
| RAG-G188/fig5-1 | passed | {"rejected_ADM_sequences": 9, "communication_plan_producer": "G188/fig5-1#adm_soaw", "scope": "图中关系；不消除邻近正文的源文冲突", "retrieval_parts": 47} |
| PUB-G206/fig2-1 | passed | {"anonymous_points": 84, "annotations": 8, "fabricated_communities": 0} |
| RAG-G206/fig2-1 | passed | {"anonymous_points": 84, "annotations": 8, "fabricated_communities": 0, "retrieval_parts": 55} |
| PUB-G212/figA-1 | passed | {"cells": 42, "fulfilled": 21, "unfulfilled": 21, "official_numeric_scores": 0, "neutral": "Define/Validate/Understand fulfilled; Commit/Disseminate/Evolve unfulfilled"} |
| RAG-G212/figA-1 | passed | {"cells": 42, "fulfilled": 21, "unfulfilled": 21, "official_numeric_scores": 0, "neutral": "Define/Validate/Understand fulfilled; Commit/Disseminate/Evolve unfulfilled", "retrieval_parts": 5} |
| PUB-G217/figC-1 | passed | {"rows": 24, "data_cells": 240, "phase_columns": ["Preliminary Phase", "Phase A", "Phase B", "Phase C", "Phase D", "Phase E", "Phase F", "Phase G", "Phase H", "ADM Architecture Requirements Management"], "source_Xs": 64, "classification_band_G_X": "preserved; not a new service"} |
| RAG-G217/figC-1 | passed | {"rows": 24, "data_cells": 240, "phase_columns": ["Preliminary Phase", "Phase A", "Phase B", "Phase C", "Phase D", "Phase E", "Phase F", "Phase G", "Phase H", "ADM Architecture Requirements Management"], "source_Xs": 64, "classification_band_G_X": "preserved; not a new service", "retrieval_parts": 14} |
| PUB-G249/fig4-1 | passed | {"domain_labels": 2, "shared_gray_scope": 1, "unsupported_role_cardinalities": 0} |
| RAG-G249/fig4-1 | passed | {"domain_labels": 2, "shared_gray_scope": 1, "unsupported_role_cardinalities": 0, "retrieval_parts": 12} |
| PUB-G249/fig4-2 | passed | {"r0005_cardinality": "unspecified:1..*", "from_cardinality": null, "to_cardinality": "1..*", "explicit_connector": false} |
| RAG-G249/fig4-2 | passed | {"r0005_cardinality": "unspecified:1..*", "from_cardinality": null, "to_cardinality": "1..*", "explicit_connector": false, "retrieval_parts": 16} |
| NEG-ADM-SEQUENCE | passed | {"rejected": true, "reason": "Nine invented ADM sequences must remain rejected"} |
| NEG-COMM-PLAN | passed | {"rejected": true, "reason": "Communication Plan must originate at SoAW in this figure: [{\"id\": \"G188/fig5-1#r0015\", \"source_relation_index\": 14, \"source_relation_id\": null, \"from\": \"G188/fig5-1#adm_risks\", \"to\": \"G188/fig5-1#d_communication_plan\", \"predicate\": \"produces\", \"predicate_zh\": \"产生/交付\", \"direction\": \"subject-to-object\", \"label_en\": null, \"label_zh\": null, \"description_zh\": \"沟通计划与已批准SoAW共用从Develop Statement of Architecture Work引出的点线分支；不是从风险识别过程引出。正文4.2.1的不同说法另记源文冲突。\", \"visual\": {\"explicit_connection\": true, \"line_style\": \"dotted\", \"arrow\": \"forward\", \"from\": \"G188/fig5-1#adm_soaw\", \"to\": \"G188/fig5-1#d_communication_plan\", \"direction_is_semantic_not_pixel_geometry\": true}, \"semantic_basis\": \"current-source-review\", \"status\": \"source-reviewed-correction\", \"cardinality\": null, \"polarity\": null, \"required_proficiency\": null, \"source_relation\": {\"from\": \"…（完整实际结果见 JSON） |
| NEG-COMMUNITY | passed | {"rejected": true, "reason": "Anonymous source points acquired fabricated names"} |
| NEG-SCORE | passed | {"rejected": true, "reason": "No official numeric score may be inferred: \"sa\""} |
| NEG-42-CELLS | passed | {"rejected": true, "reason": "Expected six conditions by seven answers (42 cells)"} |
| NEG-SAME-COUNT-SWAP | passed | {"rejected": true, "reason": "Cumulative filled/empty pattern changed: {\"condition\": \"Evolve\", \"actual\": [\"不存在/未满足\", \"已存在/已满足\", \"不存在/未满足\", \"不存在/未满足\", \"不存在/未满足\", \"不存在/未满足\", \"不存在/未满足\"]}"} |
| NEG-64-X | passed | {"rejected": true, "reason": "Reviewed X coordinates changed: [[], [1, 2, 6, 9, 10], [1, 2, 6, 7, 8, 10], [], [1, 2, 3, 4, 5, 7, 9], [1, 2, 9], [], [2, 3, 4, 5, 9], [3, 4, 5, 9], [3, 4, 5, 6, 7], [8, 9], [], [3, 4, 5, 6, 7, 8, 9], [], [8], [8], [], [6, 7, 8], [2, 9], [3, 4, 5, 6], [3, 4, 5, 7, 8, 9], [3], [], [9]]"} |
| NEG-X-COORDINATE | passed | {"rejected": true, "reason": "Reviewed X coordinates changed: [[], [1, 2, 6, 9, 10], [1, 2, 6, 7, 8, 10], [], [1, 2, 3, 4, 5, 7, 9], [1, 2, 9], [], [2, 3, 4, 5, 9], [3, 4, 5, 9], [3, 4, 5, 6, 7], [8, 9], [7], [3, 4, 5, 6, 7, 8, 9], [], [8], [8], [], [6, 7, 8], [2, 9], [3, 4, 5, 6], [3, 4, 5, 7, 8, 9], [3], [], [9]]"} |
| NEG-TWO-DOMAIN-BOXES | passed | {"rejected": true, "reason": "Separate domain box interpretation returned: \"左侧灰色大框\""} |
| NEG-INVENTED-CARDINALITY | passed | {"rejected": true, "reason": "Unprinted containing-end cardinality invented: \"1..* → 1..*\""} |
| CASE-BASELINE | passed | {"structural_errors": [], "gap_count": 12, "assignment": {"id": "ASSIGN-A", "state": "needs-evidence", "requirements": [{"requirement_ref": "REQ-SKILL-SOL", "state": "unproven", "missing_behavioral_criteria": ["独立完成异常接口设计并经评审", "评审断连、重连、幂等重放和库存冲突的恢复设计"]}], "capacity_state": "unresolved", "period_state": "not-covered", "approval": "not-granted", "support": {"provider": "PERSON-EXPERT", "mode": "共同评审异常场景及接口契约，不替代甲的能力证据", "requirement_refs": ["REQ-SKILL-SOL"], "assessment_refs": ["OBS-EXPERT"], "available_hours": 8, "evidence": ["CASE-EXPERT"]}, "support_reviews": [{"requirement_ref": "REQ-SKILL-SOL", "state": "expert-evidence-unproven"}]}, "business_approval": "not-granted"} |
| CASE-99-requirements | passed | {"rejected": true, "code": "G249-LEVEL", "binding_errors": 0, "message": "G249-LEVEL [REQ-SKILL-CH]: Proficiency must be an integer 1..4 or null"} |
| CASE-99-assessments | passed | {"rejected": true, "code": "G249-LEVEL", "binding_errors": 0, "message": "G249-LEVEL [OBS-A]: Proficiency must be an integer 1..4 or null"} |
| CASE-MISSING-null | passed | {"hard_exception": false, "rejected_as_complete": true, "binding_errors": 0, "requirement": {"id": "REQ-SKILL-CH", "task_ref": "TASK-CH", "role_ref": "ROLE-CHIEF", "skill_id": "G249:skill:business:strategic-planning", "proficiency": null, "scale_id": "G249-table5-1", "behavioral_criteria": ["把战略约束转成可复议决定"], "state": "needs-input"}, "gap": {"id": "REQ-SKILL-CH:proficiency", "reason": "missing-input", "action": "补充 proficiency 的事实、责任或规则；保留草稿。"}, "semantic_boundary": "待补草稿有效；不得宣称等级齐备或人员达标。不是缺字段必抛异常。"} |
| CASE-MISSING-absent | passed | {"hard_exception": false, "rejected_as_complete": true, "binding_errors": 0, "requirement": {"id": "REQ-SKILL-CH", "task_ref": "TASK-CH", "role_ref": "ROLE-CHIEF", "skill_id": "G249:skill:business:strategic-planning", "proficiency": null, "scale_id": "G249-table5-1", "behavioral_criteria": ["把战略约束转成可复议决定"], "state": "needs-input"}, "gap": {"id": "REQ-SKILL-CH:proficiency", "reason": "missing-input", "action": "补充 proficiency 的事实、责任或规则；保留草稿。"}, "semantic_boundary": "待补草稿有效；不得宣称等级齐备或人员达标。不是缺字段必抛异常。"} |
| CASE-TRAINING | passed | {"development": {"id": "DEV-A", "state": "needs-input", "rating_change": "not-inferred"}, "missing_reassessment": true, "current_proficiency": null, "assessments_unchanged": true, "binding_errors": 0} |
| CASE-OFFICIAL-chief | passed | {"rejected_by": "model.validate/proficiency_semantics", "errors": [{"level": "error", "code": "source-role-column", "id": "REF-REQ-SKILL-EA", "message": "Chief和通用Segment没有表5-2独立列；应保留项目裁剪要求。"}], "binding_errors": 0, "note": "此项调用模型校验；不将 evaluate 单独冒称完整的模型校验。"} |
| CASE-OFFICIAL-segment | passed | {"rejected_by": "model.validate/proficiency_semantics", "errors": [{"level": "error", "code": "source-role-column", "id": "REF-REQ-SKILL-EA", "message": "Chief和通用Segment没有表5-2独立列；应保留项目裁剪要求。"}], "binding_errors": 0, "note": "此项调用模型校验；不将 evaluate 单独冒称完整的模型校验。"} |
| CASE-LATERAL | passed | {"accepted_relationships": [{"source": "ROLE-SOL", "id": "LATERAL-A", "type": "architecture_guidance", "target": "ROLE-SOL-PEER", "scope": "候选接口相互评审", "evidence": ["CASE-REVIEW"]}, {"source": "ROLE-SOL-PEER", "id": "LATERAL-B", "type": "collaborates_with", "target": "ROLE-SOL", "scope": "候选接口相互评审", "evidence": ["CASE-REVIEW"]}], "hierarchy_policy": null, "gaps": 16, "binding_errors": 0, "boundary": "允许有证据的同级专业指导与协调；缺少职责细节仍待补，不代表组织批准。"} |
| CASE-REPORT-CYCLE | passed | {"rejected": true, "code": "ROLE-REPORT-CYCLE", "binding_errors": 0} |
| RUNTIME-SUITE | passed | null |
| BOUNDARY-READONLY | passed | {"files_hashed": 40133, "changed": [], "network": "blocked by audit hook", "write_allowlist": ["togaf-standard-10th-ai/maintenance/semantic-regression-report.json", "togaf-standard-10th-ai/maintenance/semantic-regression-report.md"]} |

边界与解释：

- 这些是项目回归断言；本轮未重新逐页视觉审阅全部官方出版物。
- 通过只确认已列语义边界与反例行为，不确认真实人员胜任、培训有效、业务方案充分或组织批准。
- 缺等级实际行为为 missing-input/needs-input，拒绝判为完备而非必抛异常；99 为 G249-LEVEL 硬拒绝。
- 历史 source_element/source_relation 保留在审计文件，当前检索不得复用旧错误语义；不能要求全文删除历史字符串。
- 脚本不联网，只写两个 maintenance 报告，未调用 case 主程序或生成器。

所有输入 SHA-256、反例变更与完整实际结果见 [JSON 报告](semantic-regression-report.json)。
