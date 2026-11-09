# 资料复核上游授权与来源绑定

正式完成状态必须由独立的源码冻结、完整资料输入和原生运行准入共同支持。`fixture_execution=false`、文档 ID、摘要计数和重新计算的文件哈希均不能替代这些证据。夹具保留为确定性验证，所有单元始终为 pending。

## 先冻结来源，后创建运行准入

`tests/enterprise/material_authority.py` 提供：

* `required_freeze_refs(input_manifest_ref, root, visual_source_manifest=None)`：参数为 `{path, sha256}` 引用，返回完整 `{path: sha256}`。从实际项目资料重建 `Inventory`，逐字比较完整 inventory、候选来源上下文，核验输入、来源、分片、视觉材料和验证器源码。不会读取或枚举资料评审会话结果。
* `make_runtime_admission(runtime, root)`：只接受确切的 `NativeAgents` 控制器。已有原生 preflight 成功后、资料评审开始前，保存不可覆盖的 `material-review-admission-runtime.json` 和实际 preflight 图像，绑定所有上游原始准入文件；返回 runtime 引用对象。该函数不启动模型、批次或预算。
* `verify_authority(...)`：核验来源冻结、当前真实输入重建、已安装冻结依赖与工具字节、当前配置的模型设置、固定权限、完整准入原始命令与原生会话。

先调用正式 freeze 的 `material_input_manifest`、`visual_source_manifest` 参数（CLI 为 `--material-input-manifest`、`--material-visual-manifest`）。freeze 将全部引用纳入 `files`，并记录：

```json
{"bound_material_review_inputs": {"input_manifest": {"path": "...", "sha256": "..."}, "visual_source_manifest": null}}
```

随后运行现有 `NativeAgents.preflight()`，保存运行准入，创建本轮显式 authority。authority 可以在源码冻结后生成；其来源必须引用同一冻结，不能新增或替代已冻结的资料输入。

## authority schema

```json
{
  "schema_version": "material-review-authority/1",
  "round_id": "explicit-round",
  "source_commit": "40-character-git-commit",
  "source_freeze": {"path": "...", "sha256": "..."},
  "input_manifest": {"path": "...", "sha256": "..."},
  "acquisition_inventory": {"path": "...", "sha256": "..."},
  "visual_source_manifest": null,
  "runtime": {
    "directory": "relative-native-runtime-directory",
    "metadata": {"path": ".../material-review-admission-runtime.json", "sha256": "..."},
    "preflight": {"path": ".../preflight.json", "sha256": "..."},
    "frozen_runtime_manifest": {"path": ".../frozen-runtime-manifest.json", "sha256": "..."}
  }
}
```

所有字段精确匹配；视觉参数也可为已核验引用。`acquisition_inventory` 必须等于 input manifest 内的 `source_unit_inventory`。正式 round 必须显式提供 `material_input_manifest`、`material_review_authority` 和 `prerequisites.source_freeze`；collector 的 `authority` 必须等于本轮引用。

`dispatch(..., authority=reference)` 使用已准入的同一个原生控制器与 `CampaignBudget`。每次 attempt 额外保存 `origin_raw_session_files`，涵盖原始 schema、prompt、command、stdout、stderr、session、final；副本必须与准入 runtime 目录内的原始文件逐字相同。原生读取收据、逐图查看、逐项来源定位、重查线程、模型用量和共享预算继续由原有检查重算。准入的两个原生会话也必须在共享预算中，且不能被资料评审重用。

旧包没有 authority 或原始命令 provenance 时，正式验证返回 invalid，不升级为完成。历史原字节继续保留。改动来源或验证器后的结果属于新版本，旧结果不关闭当前覆盖；历史复查仍需原输入快照及可验证的旧冻结运行。

## 验证范围与当前限制

新反例验证夹具翻标并重封装、假 frozen identity、假 acquisition、冻结漏项、本轮绑定错误、跨 runtime 复制、原始会话篡改和模型身份漂移。旧攻击中的 34 个文档 ID 与人造伪 PDF 不能通过完整实际来源重建。

来源闭包判定针对完整已获取的正文、原始文本块、图像和候选单元。PDF 提取与图像记录本身不证明全部物理页面没有未提取内容；分类和候选译文仍需独立语义复核，未知、缺译文、缺图、未复查发现继续 pending。

准入记录来自本地测试控制器与明确轮次引用，属于可重算的执行 provenance，不是对恶意本机所有者的密码学认证。未启动本轮原生资料评审或 507 项评测，不能用确定性测试或来源准备提升完成状态。人工专业验收与真实组织批准仍待签署。
