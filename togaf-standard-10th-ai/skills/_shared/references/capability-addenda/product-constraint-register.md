# 产品边界与企业约束登记（Product Boundary and Enterprise Constraint Register）

工作产品 `product-constraint-register` · 视图 `product-constraint-register-default` · 方法 `product-constraint-conformance-review` · 主责 [togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md) · 常用ADM：G。

来源：G186 §12.1。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

架构定义了哪些产品、边界与产品负责人约束，哪些待办项与约束冲突，是否有阶段G豁免？

## 字段

- `guide:product-constraint-register` 必填：`products`（产品、边界、产品负责人及架构依据）、`constraints`（对产品的企业约束及架构依据）、`backlog_items`（产品待办项及冲突约束）、`dispensations`（阶段G豁免：约束、权限、理由、到期日与证据）
- 可选：`purpose`（本登记的用途与范围说明）

## 步骤

1. 从组合或项目架构列出产品、边界与产品负责人
2. 登记对产品的企业约束及架构依据
3. 标记与约束冲突的待办项
4. 冲突项只有在阶段G有证据豁免时放行，否则阻止
5. 豁免到期前复核

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺
- 产品负责人的局部偏好不能越过企业约束
- 豁免须有权限方、理由、到期日与证据

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate product-constraint-register-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile product-constraint-register-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `PCC-R1`：虚构架构定义：订单服务边界含下单与支付确认，产品负责人李某；库存预占只能经库存服务（约束K-1）。
- `PCC-R2`：促销团队待办B-3要求直接写库存表以加快秒杀；B-4同样冲突，但架构委员会已于10月批准临时豁免D-1至2027-01-31。

基线结果（实际执行计算器所得）：

```json
{
  "findings": [
    {
      "backlog_item_id": "B-3",
      "constraint_id": "K-1",
      "state": "blocked-local-preference",
      "meaning": "产品负责人的局部偏好不能越过企业约束；只有阶段G有证据的豁免才可放行"
    },
    {
      "backlog_item_id": "B-4",
      "constraint_id": "K-1",
      "state": "dispensation-recorded",
      "meaning": "豁免已记录，仍需在到期前复核"
    }
  ],
  "blocked_item_ids": [
    "B-3"
  ],
  "gaps": [],
  "notice": "检查约束可追溯与豁免记录；不评价产品价值，不替代阶段G治理决定。"
}
```

修改：为B-3补记有证据的豁免D-1。分析结果变化：blocked_item_ids：["B-3"]→[]。修改后结果：

```json
{
  "findings": [
    {
      "backlog_item_id": "B-3",
      "constraint_id": "K-1",
      "state": "dispensation-recorded",
      "meaning": "豁免已记录，仍需在到期前复核"
    },
    {
      "backlog_item_id": "B-4",
      "constraint_id": "K-1",
      "state": "dispensation-recorded",
      "meaning": "豁免已记录，仍需在到期前复核"
    }
  ],
  "blocked_item_ids": [],
  "gaps": [],
  "notice": "检查约束可追溯与豁免记录；不评价产品价值，不替代阶段G治理决定。"
}
```

反例：待办B-3引用另一产品的约束。实际拒绝：`PCC-004 [B-3]: Constraint belongs to another product`

完整模型片段见 [能力注册](../capabilities/product-constraint-register.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
