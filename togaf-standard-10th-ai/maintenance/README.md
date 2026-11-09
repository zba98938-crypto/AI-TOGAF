# 当前语料的维护与深度解析

最新目录整理授权：用户进一步要求统一skills并删除根目录旧副本。唯一维护版本为本目录下的 `skills/`；根目录测试、工具和工作台统一引用它。旧资料目录归并记录见[迁移清单](../sources/README.md)，skills归并及验证见[记录](../quality/skills-consolidation.md)。下述只读约束属于此前资料解析阶段，已授权的归并和路径修复单独留痕。

此前资料解析约束：只修改 `togaf-standard-10th-ai/`，原始来源与外部工程只读。当前skills统一授权允许修复根目录 `tests/`、`tools/`、`workbench/` 中的引用并删除根 `skills/`；原始出版物内容保持不变。

目标保持四项完整范围：补齐基础标准正文范围；完成此前未逐章校订的16份指南；完成此前111张待审原文图；验证跨指南的任务—决策—制品链。优先 G184、G186、G188、G248，不把优先分片当作全部目标完成。

`chapter-review-data/` 保存当前维护记录。既有10份记录按原字节复制，来源及指纹见 `baseline-provenance.json`；新记录在本目录编写。`work/<指南>/` 可保存本次正文分片、原图核对证据和辅助程序，不进入默认知识检索。已发布阅读层仍在 `chapters/`、`architecture/` 等原入口。

正文记录须包含本节完整修订中文、精确英文内容单元、实际来源块、章节特有的规则和例外、误译修正以及源文冲突。图审须核对实际标签、连线端点/方向、多重性、包含范围和相关正文；原文无法判定的内容保留未知。资料转换、结构校验、语义审查和案例业务接受分别取证。

基础标准来源记录在 `fundamental/`，执行性跨指南案例记录在 `cases/`。官方来源访问受限时保留真实状态，不将已有系列指南中的转述冒充缺失的标准正文。后续发布须同时更新当前全文入口、章节目录、图解、知识关系、默认检索和质量清单；不能只修改维护数据即宣称发布完成。

## 当前实施与发布

当前范围为26份指南、六卷基础标准（43章3附录）及G226/W242C。`publish.py`同时发布PDF指南和网页/补充来源；`publish_extended.py`核对实际来源块和图表覆盖；`link_execution_graph.py`建立有来源性质区分的任务方法关系。

目录内`skills/`保存17个入口及共享执行器、本地规范、字体、来源和示例。`build_skill_package.py`直接维护唯一版本的语料绑定，保留历史上游指纹，不再从根目录复制；`close_skill_sources.py`闭合来源，`close_skill_links.py`闭合阅读链接并保留改写历史。可迁移包和安装依赖说明在`release/`，不安装到外部技能目录。

[当前状态](../quality/completion-status.md)及[逐项实施清单](../quality/implementation-ledger.md)区分已实现、验证、作者复核和最终独立语义验收。六卷874个编号小节和G226的75节正文已译写；不同评审人校核未授予。案例当前为五版49对PNG/SVG，详见[逐图复核](cases/omnichannel/current-delivery-review.md)。旧19对报告仅对应历史指纹。

正文维护入口：`publish_chinese_texts.py`按基础网页来源块发布六卷；`publish_supplementary_chinese.py`按PDF来源节发布G226，逐页保全W242C中文原文。`record_body_author_reviews.py`保存本轮作者实际重点对照观察，不构造不同评审人认证。发布后重新闭合skills来源及阅读链接，再封存和迁移验证。

## 台账证据维护

[七类能力缺口核查](../quality/seven-gap-reconciliation.md)分别登记全量方法、图形来源与生成验收、ADM交付物、案例、正式语言和独立验收。表列资料交付计划的工程完成字段不覆盖这些能力的全范围业务接受。

`python3 -B togaf-standard-10th-ai/maintenance/verify_implementation_ledger.py`只读核对台账的证据指纹，以及报告明确声明的`input_sha256`、`inputs`、`source_files`；发现过期、缺失或空台账时返回非零。未登记输入的证据标记`not-recorded`，不能推断输入已经复核。可用`--out <新报告路径>`保存结果。

台账生成、只读校验和总状态共用`report_outcome.py`：识别布尔`passed`、枚举`result/status`及`counts.failed/failures/errors`。失败信号优先于成功字段；阻断、跳过和格式错误不能支持done。零失败本身不证明执行成功；conditional行要求明确通过。无验证结果字段的来源文档仍可作为静态证据，不冒充测试报告。

报告更新后先保留旧台账并审查变更依据，再运行`update_implementation_ledger.py`和`update_status.py`，最后重跑上述只读检查。刷新台账不会重新执行旧测试，也不会授予来源、视觉或业务验收；当前状态生成器会再次检查证据，过期时将工程完成字段降为false。
