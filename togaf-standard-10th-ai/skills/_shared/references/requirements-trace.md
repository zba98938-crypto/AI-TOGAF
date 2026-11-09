# 持续需求追溯与变更检查

用于任意共享模型，连接 ADM 中持续维护的需求、架构设计、实施工作和验收证据。依据 G186 §5.1.4（需求库）、§5.1.5（合规与价值）、§6.1.1（持续利益相关者参与与需求管理）；字段和机器检查是本项目约定。

## 使用

```sh
python "$TOGAF_SKILLS/_shared/scripts/requirements_trace.py" model.json --report trace.json
python "$TOGAF_SKILLS/_shared/scripts/requirements_trace.py" model.json --requirement req-privacy --mode delivery --strict --report delivery-trace.json
```

先校验共享模型，再输出逐需求的来源目标、设计对象、工作包、验收准则、关联视图及交付物。`--scope`、`--state` 精确选择命名范围/状态；选择为空或拼错不会成为通过。默认返回结构错误的非零退出码，`--strict` 同时因追溯缺口退出非零。报告不修改模型和批准状态。

`planning` 检查需求的 statement、owner、priority、acceptance、来源、目标追溯、设计分配和验证计划。`delivery` 另检查工作包和已记录的实际验证结果。按本次决策选择检查时点；A 阶段的早期需求可以尚未分配设计，先保留缺口，而不是为通过检查捏造设计。

## 显式关联

| 链条 | 模型表示 |
| --- | --- |
| 需求由目标、业务属性等导出 | `requirement --derived_from--> goal`；或有来源与理由的 `traces_to` 连接利益相关者/目标 |
| 架构对象受需求约束 | `requirement --specifies--> architecture object`；或 `architecture object --satisfies--> requirement` |
| 安全需求到控制 | `security_requirement --requires_control--> control` |
| 实施工作 | 工作包直接 `satisfies`/`traces_to` 需求，或工作包 `changes_object` 已分配设计对象；应用可用 `migrated_by` |
| 验收计划与结果 | `acceptance_criterion.attributes.requirement_ids` 显式绑定需求 ID |

任意图可达不算满足。具名范围/状态冲突会列入 `cross_context_ids`，不借用另一状态的设计/结果补覆盖。没有命名状态的对象按显式关系视为共享对象，需要专业评审确认适用性。`view_ids`、`deliverable_ids` 只是变更后的复核入口，不证明内容已更新。

验收准则属性示例（计划）：

```json
{"requirement_ids":["req-privacy"],"criterion":"越权读取被拒绝且无客户内容",
 "verification":"以跨店账号调用读取接口，核对响应与审计",
 "execution_status":"not-executed","observed_result":null}
```

执行状态支持 `unknown/not-executed/planned/passed/failed/inconclusive`。记录实际执行时另外提供 `observed_result` 与 `result_evidence`（引用共享 `sources`）；`rule_evidence` 或计划材料不能充当实际结果。虚构案例结果标为 `simulated-result`，不能达到真实交付证据完整。即使实际结果链完整，仍标为 `recorded-result-awaiting-review`，业务接受始终为 `not-assessed`。

## 变更处理

1. 保留需求稳定 ID 与版本/状态，记录触发材料和前后差异。
2. 运行此工具列出显式追溯；再用 `analyze.py --impact` 扩展候选影响范围。两者均需逐项判断实际影响。
3. 更新设计、工作包、验收准则及受影响制品；失效的观察结果不沿用到新版本。
4. 将需补信息和需复访阶段记入 ADM 执行记录；重生成受影响视图/交付物，再复核追溯。缺口不以自动批准关闭。
