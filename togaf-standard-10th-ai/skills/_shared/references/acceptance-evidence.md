# 逐能力验收证据约定

本约定是技能包内部证据一致性门，不是TOGAF官方认证规则。登记、模型验证、程序运行、人工定性判断、独立审查和图像目视分别记载；没有完整证据的能力仍为pending，不以文件存在或摘要标签代替验收。

## 身份与适用维度

每条审核明确 `category` 与 `id`，类别为artifact-family、guide-work-product、view-template、analysis-method或deliverable。同一工作产品作为family和guide-work-product两种统计维度出现时，不自动互授通过。共享证据合法，但证据记录scope必须明确含被审能力。

定义、模型、分析、生成、修改、评审、视觉七维逐一给出证据。视觉是否适用由注册契约派生，不由申请通过的记录自称：表格和无独立图本体的方法可说明not-applicable；关联图形另按视图能力审查。其他维度不能通过not-applicable跳过。文档交付物仍须布局/视觉评审。

## 严格记录格式

审核输入为 `acceptance-gate-v1`，含能力身份、`reviewer: {id, role}`、`scope: {capabilities: [{category,id}], purpose}`、当前完整 `runtime_fingerprints` 与 `dimensions`。各维含 `status`、`rationale`、`evidence` 数组；证据引用为 `{path, sha256, record_id}`。路径必须在共用包内，不能越界、借绝对路径或符号链接逃逸。

证据文件必须是非空JSON，使用 `acceptance-review-records-v1`，其中records的所选记录含唯一id、dimension、status、reviewer、明确scope、实际observations及 `assets: [{path,sha256}]`。摘要文件自身不能充当其所审核资产；资产不存在、哈希变化、scope不含本能力、版本过期或旧弱格式均不通过。

- 定义passed必须有 `source_comparisons: [{source_path, locator, conclusion}]`，source_path为已核验hash的实际来源资产；来源对照不能凭‘已找到链接’替代。
- 视觉passed必须分别列原图/输出 `original_assets`、`output_assets`，每项均有资产hash和实际 `opened_assets` 记录（opened=true、reviewer_id、hash、具体observations）。文件存在、渲染完成、XML文本或几何检查不足以满足实际打开记录。
- 当前运行指纹来自实现及随包语义资源、能力/制品/交付表和元模型，不能从候选gate反向复制。证据文件和被审资产变动会使记录失效。

实现：[严格验收门](../scripts/acceptance_gate.py)；反例：验收门测试（历史材料已清理）。测试中的passed均为临时合成夹具，不会写入任何真实能力验收状态。

## 聚合规则

[状态聚合器](../scripts/audit_full_coverage.py)保留每个实际view_id及交付instance_id，不用一个同规范输出满足其他范围/状态。某次生成有草稿缺口、文件缺失或版本过期时不能归为当前完整生成。交付物的组装状态与章节内容证据状态另记；只有补充证据的末章不自动成为该章主题已满足。

定性方法案例的模型、修改反例和交叉审查挂接到各自维度；人工判断记录不冒充确定性计算结果，历史执行存在不冒充当前重跑通过。七维完整通过还必须经过严格gate，不能由分维度描述自动推断。

## 能力边界

门只核验身份、scope、资产一致性、版本时效和明确审核声明；它不能认证审核者身份/诚实性、来源权威或语义真值，也不创建真实机构批准。新增实际图像观察须说明打开的具体资产、哈希、观察者性质及范围；AI观察不能称为人工签署，不可外推到未打开的页面或未对照的原图。

## 当前执行与递归完整性

- `evidence_integrity.py`按证据类型递归检查，而非任意扫描业务JSON。执行／评审记录内部的案例哈希、输入、日志、输出及能力身份必须相符；禁止越界、符号链接逃逸与循环。
- `execution-batch/1`保存运行前后依赖、命令参数所指本地脚本与输入、stdout/stderr及输出SHA。`method-execution/2`还绑定当前运行依赖及每个变体输入；直接函数调用与完整模型绑定分开报告。
- `build_method_case_records.py`只写`method-structure-observation/2`和当前索引指针，不能生成专业通过评语。旧执行与评审保留原始哈希，正文更新后显式失效。
- 七维状态分别保存`has_evidence`、`evidence_current`、`verification_status`和`acceptance_status`。缺门禁为`not-submitted`，不是固定通过、固定失败或完成率；一个视图修改不能给全库授予修改证据。
- 重跑入口为`run_development_verification.py`；每次新建目录。`verify_methods.py`只授予实际运行的有限执行观察；`verify_method_reasoning.py`的数学断言与逐案AI复读亦不等于真实业务接受。
