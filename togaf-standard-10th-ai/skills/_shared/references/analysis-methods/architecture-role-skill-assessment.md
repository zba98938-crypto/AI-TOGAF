# 角色技能差距评估

方法ID：`architecture-role-skill-assessment`。当前依据G249 §3–6；G198仅用于历史对照。

步骤与输入结构为项目操作约定；执行器只检查显式证据和规则，不能授予任职、治理授权或认证。

## 输入与步骤

1. 从实践委托确定任务与角色范围
2. 保留原文参考并明确裁剪目标及行为判据
3. 逐项核对人员正向行为证据；未知不评级
4. 区分技能差距与容量缺口
5. 将发展行动绑定任务、判据、复评与历史
6. 保持证据、职责、移交与授权边界

输入包括：架构实践委托与范围；任务、角色与可观察要求；绑定版本的量表；人员行为证据；独立的人力需求及可用容量。

## 执行与验收

`analyses[].method_id` 使用 `architecture-role-skill-assessment`；通过 `analyze.py model.json --evaluate <analysis-id>` 执行。

未知保留null或带ID缺口；非法等级拒绝；原文、裁剪与观察三种记录分别保留；四级技能熟练度不转换为Open CA三级认证或agent权限。

[任务与共享模型绑定示例](../profiles/architecture-work-assignment-review.md)展示完整输入；[角色技能矩阵](../profiles/ea-skill-role-proficiency.md)、[人员发展计划](../profiles/architecture-development-plan-default.md)给出输出契约。

字段、证据与复评约束见[G249运行时契约](../g249/runtime-contract.md)。

[区分人员熟练度、角色目标与团队容量](../method-cases/architecture-role-skill-assessment.md)演练项目行为锚点与证据不足；项目锚点不得冒充G249逐字定义。
