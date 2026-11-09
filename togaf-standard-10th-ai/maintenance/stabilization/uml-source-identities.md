# UML 来源身份增量

本组在 `codex/standards-next` 记录官方来源身份，规范原文、既有 5,779 个义务 ID、共享 binding 和历史证据不改写。新增内容是来源定位与诊断元数据；完整 UML 2.5.1 设计时能力、专业验收与组织批准仍未完成。

`standards_coverage.py` 为 UML XML 源条目增加 `source_identity` 和 `owner_identity`：源文件、完整 prefix-independent XML 路径、原生 ID、同路径/native ID 的 occurrence、内部 key 与独立来源 SHA-256。即时 owner 的完整身份保留 State/Vertex 子规则的区别，原有裸 `owner_id` 字段继续兼容。内部 key 不随来源哈希改变；哈希仍作为新旧证据是否适用的独立条件。原有 obligation IDs 没有迁移或重命名。

每个 UML/XMI 机器来源的 `source_identity_provenance` 清单保留全部 XML native ID 重复组，包括非独立义务的 comment 和 OpaqueExpression。官方 UML.xmi 共有 8 组、16 个元素；当前义务台账仍保留 5 组、10 个带路径区分的条目。每个重复元素记录其身份、owner/classifier 身份、来源行、canonical XML 片段和片段哈希；原始文件字节仍是权威数据，C14N 片段是定位材料。

10 处裸 native ID 引用继续返回 `ambiguous-source-reference`，`resolved_target=null`，并记录全部候选及同一 XML operation 内的上下文候选。上下文仅表示语法包含关系，尚未成为规范类型、所有权或执行适配的证据；没有自动选第一个/最后一个候选，没有全局 ID 修复，也没有 Vertex OCL 更正。

`source_availability` 记录已核对的本地文件；全局 native ID 唯一性、歧义引用、语义验收及设计时完成状态单独记录。现有 source defects、fail-closed 的 `source_scope_complete=false`、`verified_obligations=0` 和 `completeness=incomplete` 保持不变。可访问文件和完整身份清单不关闭规范歧义。

独立测试在 `tests/test_uml_source_identity.py`：固定现有全部义务 ID 的校验指纹；检查 8/16 XML 重复和 owner 身份；验证裸引用与本地 href fragment 保持歧义；验证同 owner/name 下 occurrence 区分以及 namespace prefix 变化保持身份；确认相同 precondition 不合并、不同 State/Vertex 正文原样保留；确认已获来源不提升全局身份或语义完成状态。现有标准覆盖、正式标准证据门禁和原生证据测试也实际执行。

当前本组证据目录为 `output/uml-source-identity-next-01/`，包含实际 `execution.log`、逐项 `test-evidence.json` 和重新生成的 UML/BPMN 台账。来源差异审计及后续显式适配方案在 `output/uml-source-defects-audit-01/identity-plan.md`；其中 Vertex 的正确定位为物理 PDF p406、印刷 p364、14.5.13.6（标题在 p405）。签名、说明名和 body 名称的不一致继续待裁定；`redefinedElement` 同时是 inherited derived `[0..*]` 特征，未据此自动替换为参数 `redefiningElement`。
