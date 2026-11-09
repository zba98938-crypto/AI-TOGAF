# 本地工程稳定化维护

本轮工作使用本地 `codex/project-stabilization` 分支，不配置或推送远端。阶段提交与运行证据分别保存；运行输出、临时目录、依赖和发布归档按 Git 排除规则保留在本机。大型历史资料的位置、大小和 SHA-256 见 [初始资料基线](local-material-baseline-20261109.json)。

本轮尚未完成 UML 2.5.1 / BPMN 2.0.2 全部设计时义务、全量独立资料复核或 507 项独立 Actor/scorer 评测。旧 `quality/` 报告和历史输出只证明各自记录的版本及范围。本轮源码、包、评测和入口须使用同一份显式轮次清单；独立模型复核、人工专业验收与真实组织批准分别记录，后两项保持待签署。

## 已形成的阶段改动

- 正式四象限测试区分业务边与字面值 `data-annotation-leader="true"` 的注释引线；保留模型、关系、箭头、布局和颜色断言，兼容覆盖层退出正式流程。
- 包构建和发布共用全量检索来源闭包检查，查询只读取包内解析后的来源；来源可达不提升历史译文的语义验收状态。
- 入口维护命令按显式清单验证来源、目标、链接、指纹、冻结源码及实际 UI，失败保留旧入口。当前真实入口尚未由本轮切换。
- 原生 UML/BPMN XML 作为可选权威内容保存，工作台版本与生成任务绑定原文字节指纹。诊断、导出和预览复用已有机制；BPMN 派生布局必须显式选择并单独保存。
- 标准覆盖台账从正文与机器来源生成稳定条目，按构造、属性、引用、约束、图形和交换分别记录。有限正反例通过不代表完整标准实现。
- 固定协议的受控本地渲染进程保留原生浏览器失败历史。源码和依赖变化后旧准入失效，须重新进行零模型功能、隔离、超时和清理验证。

## 正式执行顺序

`源码与测试冻结 → 来源闭包 → 封装及解包验证 → 完整工程验证与507项评测 → 当前入口切换 → 总报告 → 台账 → 完成状态 → 最终只读检查`

使用 [stabilization_evidence.py](../stabilization_evidence.py) 的 `freeze / record / report / ledger / status / acceptance-pack / final-readonly` 命令维护证据链。[总报告生成器](../write_adm_completion_report.py) 的正式入口为 `--round <轮次清单> --out <新结果路径>`，不得混入历史目录参数或兼容模式。每次执行使用新目录，旧记录原字节保留。

冻结前准备 `stabilization-entry-inputs/1` JSON，包含本轮 `round_id` 及精确 `entries.current_map`、`entries.catalogue` 两个 `{path, sha256}` 引用。路径为仓库内规范相对路径，分别指向实际 JSON 映射和 HTML 图册。冻结会将这两个被忽略的生成文件也纳入旧字节基线。

资料复核轮次还须在冻结时传入 `--material-input-manifest <全量review-input-manifest.json>`，有视觉衍生材料时同时传入 `--material-visual-manifest <视觉来源清单.json>`。冻结前会从已获取的资料重建完整单元、候选和分片，核对所有输入指纹并把被忽略的原文、图像、清单和复核验证器纳入同一冻结文件表。后续复核权限清单绑定该冻结和独立的实际原生运行准入；运行结果不作为上游冻结输入，夹具执行不会计入资料语义复核。

```bash
python3 -B togaf-standard-10th-ai/maintenance/stabilization_evidence.py freeze \
  --round-id <本轮ID> --entry-inputs <入口旧字节清单.json> --out <新冻结结果.json>
JAVA_HOME=/Users/Shared/ai-togaf-java-20261106-01 \
TOGAF_BROWSER_PATH=/Users/Shared/ai-togaf-browser-20261106-01/chrome-headless-shell-mac-arm64/chrome-headless-shell \
python3 -B tests/run_unit_regressions.py tests --out <新单元结果目录>
JAVA_HOME=/Users/Shared/ai-togaf-java-20261106-01 \
TOGAF_BROWSER_PATH=/Users/Shared/ai-togaf-browser-20261106-01/chrome-headless-shell-mac-arm64/chrome-headless-shell \
python3 -B tests/verify_core.py --render --out <新完整工程结果目录>
python3 -B tests/diagnose_controlled_render.py \
  --browser /Users/Shared/ai-togaf-browser-20261106-01/chrome-headless-shell-mac-arm64/chrome-headless-shell \
  --out <新零模型准入目录>
python3 -B tests/verify_native_toolchain.py --runtime-root <本轮冻结运行环境> \
  --render-mode controlled-local --render-admission <本轮准入目录/summary.json> \
  --out <新原生权限诊断目录>
```

原生运行环境只能复用已安装依赖和保留的离线 wheels、Java、浏览器；不得触发下载或安装新软件。实际运行命令与输入指纹保存在各阶段原始证据中。全量单元门禁要求实际执行数大于零，失败、错误、跳过均为零。507 项门禁重新核验逐项输入、成果、会话、独立评分、事件及当前源码绑定，未执行项不计通过。

评测沿用当前配置的模型服务、模型与推理设置，按并发 `1 → 2 → 4` 提升。最多四批，每批四小时及 1,000 会话，总计十六小时及 4,000 会话；中断恢复、修复重试及批间停顿沿用原预算。保留超时、限流、资源和质量停止规则，记录实际会话与模型用量。

包装生成后 Git HEAD 保持冻结提交；只允许冻结声明的精确生成清单或指定生成历史路径变化。新增源码、未声明文件、扩大排除范围、重命名绕过和未经授权的入口差异均阻断。最终只读核验完成前不提交下游生成结果，避免改变冻结的源码提交身份。

来源附件闭包使用[递归依赖规则](source-dependency-round.md)，完整方法回归由 `verify_core.py` 显式传入仓库内 `tests/method_fixtures.py`。未配置已保留 Java 环境导致的跳过仍是验证失败，不可用兼容覆盖层豁免。

## 证据与业务验收

预冻结运行位于仓库根目录 `output/project-stabilization-20261109/`，其中失败、过期和有限范围结果不能作为最终准入。正式轮次清单必须逐项引用新运行结果及 SHA-256，报告、台账和完成状态不反向作为上游执行依据。 标准证据使用明确的 `standard_capabilities.uml/bpmn` 台账引用、`standard_test_evidence` 执行结果引用及 `standard_test_log` 日志引用；日志必须是结果目录内的 `execution.log`。校验会从当前规范与实现重新生成整份台账，并逐项核对实际测试记录和日志。

业务验收包收集复现、来源、决策依据、交付物、异常路径和评测结果，附人工专业验收、业务负责人验收及真实组织批准的签署表。技术门禁未全部满足时只生成待完善包，不能标为可签署或完整完成。
