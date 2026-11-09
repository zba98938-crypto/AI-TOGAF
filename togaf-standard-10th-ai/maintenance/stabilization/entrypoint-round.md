# 当前入口维护命令

`activate_current_outputs.py` 只消费显式轮次清单，不导入历史激活脚本或兼容覆盖层。默认进行完整准备并保留结果；`--apply` 才切换入口。生产命令要求 Git HEAD 与清单中的源码提交相同，源码与测试保持干净。

```sh
python3 -B togaf-standard-10th-ai/maintenance/activate_current_outputs.py \
  --round output/<轮次>/entrypoint-round.json --out output/<轮次>/entrypoint-preparation
python3 -B togaf-standard-10th-ai/maintenance/activate_current_outputs.py \
  --round output/<轮次>/entrypoint-round.json --out output/<轮次>/entrypoint-activation --apply
```

清单的 `schema_version` 是 `current-entrypoint-round/1`。所有文件路径均以仓库根目录为基准；每个引用格式为 `{"path":"相对文件路径","sha256":"64位小写SHA-256"}`。

| 字段 | 内容 |
|---|---|
| `round_id` | 本轮稳定标识，仅字母、数字、点、下划线和连字符 |
| `source_commit` | 冻结源码的40位 Git 提交哈希 |
| `prerequisites` | 必须恰好包含 `source_freeze`、`source_closure`、`package_verification`、`engineering_verification`、`model_evaluation` 五个文件引用 |
| `entries` | `current_map` 与 `catalogue` 文件引用，哈希记录切换前的原字节 |
| `output_paths` | 原当前输出清单的全部键，值为新成果文件或目录的仓库相对路径 |
| `targets` | 完整目标文件引用数组；目录内每个文件、图册链接及预览资源都必须有指纹 |
| `catalogue` | 正整数 `expected_rows`；`replacements` 数组，每项含 `map_key`、以斜杠结尾的 `from` 与 `to` 链接前缀 |
| `ui` | `atlas` 文件引用、非空 `search_term`、正整数 `expected_search_rows` |

五份前置报告必须带有对应 `stage`、同一 `round_id`、同一 `source_commit` 和严格布尔值 `passed:true`。`source_freeze` 还包含非空 `files` 源码指纹映射，命令重新读取并核对每个源文件。`model_evaluation` 要求 `required_items`、`executed_items` 和 `passed_items` 均为507、`unexecuted_items` 为0、`actor_scorer_independent:true`；这些报告应由正式验证器对逐项证据检查后生成。该命令不将自述、登记数量或历史结果提升为执行证据。

源冻结通过 `--entry-inputs` 接收完整 `stabilization-entry-inputs/1` 对象：同一 `round_id` 以及精确 `current_map`/`catalogue` 两份引用。这些必要入口即使位于 ignored 输出目录，也纳入 `freeze.files`，完整对象保存为 `freeze.entry_inputs`。激活清单的 `entries` 必须与它完全一致，不能在冻结后另选入口。最终只读检查可复用 `verify_git_identity(repo, source_commit, *, freeze_ref=None, freeze_data=None, round_id=None, replacements=None)`；引用与已验证数据二选一，只有来自成功激活的这两个路径及实际 after 指纹可作为 `replacements`，其他源码仍核对冻结字节，新增源码和重命名绕过均拒绝。

冻结后生成的包清单、构建来源/历史、轮次清单和下游状态/台账允许产生 Git 变更，但必须在已核验的 `source_freeze` 中通过 `excluded_generated_paths` 或 `excluded_generated_prefixes` 精确列出。可选范围限于冻结生成器声明的六个 JSON/Markdown 文件和 `skills/build-history/`、`maintenance/stabilization/rounds/` 两个专用生成目录；不得与冻结文件重叠。源码文件扩展名、目录扩大、重命名来源越出该范围、旧轮次或过期冻结指纹均拒绝。检查使用 NUL 分隔的 Git 文件记录，逐一验证未追踪文件与重命名两端，准备和实际切换前各执行一次。实际允许的变更写入 `post_freeze_generated_changes`，不配置兼容或绕过开关。

新输出清单的值按当前清单所在目录生成相对路径，保留现有键与 JSON 形式。图册链接前缀分别与原清单、新成果目录核对，允许仓库内合法的 `..`；绝对路径、协议、跨仓库路径、控制字符、嵌套编码及任何符号链接路径均拒绝。链接解析逐段检查，包含 `symlink/../` 的路径也被拒绝。缺文件、过期指纹、缺目标指纹、残留旧链接或行数不符均阻断准备。

切换前保存两份原入口的完整字节，使用维护锁排斥第二次切换，再以同目录临时文件和 `os.replace` 替换。替换、后置 UI 检查或可处理的中断失败时恢复原入口并保存失败结果。并发用户编辑产生的未知字节不被覆盖，结果明确记录恢复冲突。不可捕获的进程强杀或主机断电可能留下维护锁及部分切换；应先利用该次 `before/` 快照与 `preparation.json` 核对并恢复，再重新建立轮次证据，不应直接删除锁后继续切换。

固定 `verify_current_output_ui.mjs` 由本地测试控制器使用现有 Chromium 执行，记录 `runtime_mode:local-test-controller`、实际浏览器路径/版本、自有 PID、截图、逐项检查和清理结果。它验证完整图册行数、实际搜索、Tab/Enter 导航、ADM 折叠面板及导航焦点、全部图像加载和390px布局；只允许加载清单中指纹一致的本机资源。该检查不是模型会话的受控渲染接口，也不替代其隔离验收。专业验收和组织批准始终保留 `pending_signature`。

`prepared:true` 只表示准备成功，准备结果的 `applied` 与 `passed` 仍为假。正式切换在全部前置证据及实际 UI 检查通过后才记录 `applied:true`、`passed:true`。输出目录必须是仓库 `output/` 下未存在的新目录；旧轮次文件不得覆盖。

`entry_files` 为两份入口分别记录仓库相对 `path`、`before_sha256` 与最终实际 `after_sha256`。成功、回滚和并发编辑冲突都在 `finally` 中记录实际字节；只有真实成功激活证据可授权最终只读检查接受这两处切换后的指纹。
