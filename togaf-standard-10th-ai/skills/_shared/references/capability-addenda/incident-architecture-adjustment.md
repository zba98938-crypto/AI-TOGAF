# 事件后的架构调整记录（Architecture Adjustment after an Incident）

工作产品 `incident-architecture-adjustment` · 视图 `incident-architecture-adjustment-default` · 方法 `incident-architecture-adjustment-review` · 主责 [togaf-change-value](../../../togaf-change-value/SKILL.md) · 常用ADM：H Requirements。

来源：G186 §12.3。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

事件如何改变了利益相关者的风险偏好与需求，有哪些目标变更、取消目标或取消变更的选项？

## 字段

- `guide:incident-adjustment` 必填：`incident`（事件事实、日期与证据）、`objectives`（受影响目标）、`risk_appetite_before`（事件前风险偏好及权限方）、`risk_appetite_after`（事件后风险偏好及权限方）、`risk_tolerance`（风险容忍度及权限方）、`requirement_changes`（由偏好变化引起的需求变更及影响评估引用）、`options`（变更目标/取消目标/取消变更三类选项及其成本、确定性与后果）、`decision`（利益相关者决定状态、所选选项、权限与证据）
- 可选：`summary`（调整事项摘要）

## 步骤

1. 记录事件事实与证据
2. 记录事件前后的风险偏好与风险容忍度及权限方
3. 把偏好变化登记为需求变更并做影响评估
4. 提出目标与工作变更方案，说明成本、确定性与残余风险
5. 同时评估取消目标与取消变更的后果
6. 由利益相关者决定并留存证据

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 事件改变风险偏好即需求变更，架构须调整
- 超出风险偏好的风险常用转移或规避
- 可接受成本的变更可能很少；取消目标或取消变更是正常选项
- 不推断事件原因，不代替利益相关者决定

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate incident-architecture-adjustment-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile incident-architecture-adjustment-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `IAA-R1`：虚构事件INC-31：2026-10-18周末订单服务中断6小时，客服记录与监控截图已归档。
- `IAA-R2`：事件前风险委员会接受单次中断<4小时；事件后改为大促期间零中断容忍。目标OBJ-AV：大促期间订单可用。
- `IAA-R3`：方案X：双活改造，估算120万元、9个月，压测与供应商SLA支持其确定性，残余风险仍高于新偏好需购买业务中断保险。

基线结果（实际执行计算器所得）：

```json
{
  "appetite_changed": true,
  "option_kinds": [
    "cancel-change",
    "cancel-objective",
    "change-target"
  ],
  "decision_state": "pending",
  "gaps": [],
  "notice": "把事件后的风险偏好变化当作需求变更处理；不推断事件原因，不代替利益相关者决定。"
}
```

修改：只保留变更目标一种选项。分析结果变化：新增缺口options:cancellation；option_kinds：["cancel-change", "cancel-objective", "change-target"]→["change-target"]。修改后结果：

```json
{
  "appetite_changed": true,
  "option_kinds": [
    "change-target"
  ],
  "decision_state": "pending",
  "gaps": [
    {
      "id": "options:cancellation",
      "reason": "cancellation-options-not-assessed",
      "action": "来源提醒可接受成本的变更可能很少；评估取消目标与取消变更两种后果"
    }
  ],
  "notice": "把事件后的风险偏好变化当作需求变更处理；不推断事件原因，不代替利益相关者决定。"
}
```

反例：需求变更引用不存在的目标。实际拒绝：`IAA-003 [RC-1]: Requirement change must name an affected objective`

完整模型片段见 [能力注册](../capabilities/incident-architecture-adjustment.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
