# AI-TOGAF

TOGAF资料的唯一主目录为[togaf-standard-10th-ai](togaf-standard-10th-ai/README.md)。旧英文资料、中文稿和架构角色技能下载目录已按内容指纹归并，独有资料完整保留，重复副本删除。

正在进行[本地工程稳定化与 UML/BPMN 设计时补齐](togaf-standard-10th-ai/maintenance/stabilization/README.md)。旧质量报告和图册保留各自版本范围；本轮完整标准覆盖、独立资料复核、507 项评测及入口切换尚未完成，人工专业验收与真实组织批准待签署。

- [本轮完成状态与验证入口](togaf-standard-10th-ai/maintenance/stabilization/README.md) · [历史完成状态](togaf-standard-10th-ai/quality/completion-status.md)
- [统一原始来源与迁移记录](togaf-standard-10th-ai/sources/README.md)
- [ADM、制品、流程及层次关系](togaf-standard-10th-ai/skills/_shared/references/togaf-explained.md)
- [完整ADM流程图册](togaf-standard-10th-ai/architecture/adm-flow/index.html) · [阶段制品及来源说明](togaf-standard-10th-ai/architecture/adm-flow/README.md)：总览、内容关系、预备阶段、A–H、持续需求管理和实际迭代；可编辑源码、SVG与PNG。
- [当前可运行skills](togaf-standard-10th-ai/skills/README.md)

```bash
python3 -B togaf-standard-10th-ai/skills/_shared/scripts/local_tool.py query '业务能力 价值流' --limit 5
python3 -B togaf-standard-10th-ai/maintenance/verify.py
```

唯一维护的 skills 位于 `togaf-standard-10th-ai/skills/`，根目录旧副本已移除。根目录 `tools/`、`tests/`、`workbench/` 保留，统一引用该版本；不再维护第二套代码。

## 日常检查与正式留证

日常改动先运行 `python3 -B tools/daily_check.py`。它只执行少量回归和一次来源检索，不渲染图片、不安装依赖，也不在仓库中保存测试证据。需要完整工程留证时，按[稳定化轮次](togaf-standard-10th-ai/maintenance/stabilization/README.md)使用新的 `--out` 目录运行 `tests/verify_core.py --render`；正式轮次的旧证据保持不可变。

本地便携语料仅在来源变更后运行 `python3 -B togaf-standard-10th-ai/maintenance/build_skill_package.py` 刷新；未变化的文件会保留现有字节和修改时间。需要交付包时再运行 `seal_release.py --release-dir <新目录>`。仅需开发用源码归档时可加 `--source-only`，省去本机 Node 依赖压缩包；完整迁移验证仍需要含依赖的正式归档。建议把新归档目录放在项目目录之外，并按来源指纹和轮次记录决定保留哪些版本。

[skills归并记录与验证](togaf-standard-10th-ai/quality/skills-consolidation.md)保留旧版指纹、路径迁移和运行结果。`upstream-manifest.json`仅记录历史复制来源，不要求旧目录继续存在。
