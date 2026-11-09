# 预约试点中的角色、指导关系与任期

所有业务材料、人员、目标和授权均为明示虚构；执行结果只覆盖下述情景。

方法：`architecture-role-catalog-review`。来源：G249 §4、§4.1–4.4。
可复用材料：[四类场景JSON](../method-case-materials/architecture-role-catalog-review.json)。

## 决策与原始业务资料

林某的分析岗位是否因此成为企业架构管理岗位，以及月底之后能否继续视为当前任务授权？

|证据 ID|原始业务材料|
|---|---|
|MANDATE|企业、履约分段、双店解决方案分别承担接口决定责任；企业角色向分段提供专业指导，没有人事汇报声明。|
|KPI-POLICY|虚构实践负责人采用11月100%决定条目带评审依据的过程目标；它不是人员能力或绩效评级。|
|ASSIGNMENT|林某的岗位为分析师，11月1日至30日承担预约接口审查任务；没有12月续期材料。|

充分输入的精确结构如下；数值与ID来自本案例材料，不从执行结果反推。

```json
{
  "source_ids": [
    "MANDATE",
    "KPI-POLICY",
    "ASSIGNMENT"
  ],
  "as_of": "2026-11-08",
  "roles": [
    {
      "id": "EA",
      "name": "全渠道预约架构角色",
      "tier": "enterprise",
      "scope": "全渠道预约",
      "segment_scope": "全渠道预约",
      "primary_responsibility": "界定全渠道预约的变更与接口责任",
      "activities": [
        "维护全渠道预约的接口决定"
      ],
      "key_stakeholders": [
        "运营负责人"
      ],
      "evidence": [
        "MANDATE"
      ],
      "kpis": [
        {
          "id": "EA-KPI",
          "measure": "带评审依据的接口决定比例",
          "target": 100,
          "target_origin": "project-adopted",
          "unit": "%",
          "measurement_period": "2026年11月",
          "measurement_source": "决定登记册",
          "owner": "架构实践负责人",
          "formula_or_rule": "有评审依据条数/全部决定条数×100",
          "adopted_by": "虚构实践负责人",
          "evidence": [
            "KPI-POLICY"
          ]
        }
      ],
      "relationships": [
        {
          "id": "GUIDANCE",
          "type": "architecture_guidance",
          "target": "SEG",
          "scope": "预约接口一致性",
          "evidence": [
            "MANDATE"
          ]
        }
      ]
    },
    {
      "id": "SEG",
      "name": "门店履约架构角色",
      "tier": "segment",
      "scope": "门店履约",
      "segment_scope": "门店履约",
      "primary_responsibility": "界定门店履约的变更与接口责任",
      "activities": [
        "维护门店履约的接口决定"
      ],
      "key_stakeholders": [
        "运营负责人"
      ],
      "evidence": [
        "MANDATE"
      ],
      "kpis": [
        {
          "id": "SEG-KPI",
          "measure": "带评审依据的接口决定比例",
          "target": 100,
          "target_origin": "project-adopted",
          "unit": "%",
          "measurement_period": "2026年11月",
          "measurement_source": "决定登记册",
          "owner": "架构实践负责人",
          "formula_or_rule": "有评审依据条数/全部决定条数×100",
          "adopted_by": "虚构实践负责人",
          "evidence": [
            "KPI-POLICY"
          ]
        }
      ],
      "assignments": [
        {
          "id": "ASSIGN",
          "person_ref": "PERSON-LIN",
          "job_ref": "JOB-ANALYST",
          "task_refs": [
            "REVIEW-RESERVATION"
          ],
          "authority": "虚构实践负责人",
          "valid_from": "2026-11-01",
          "valid_until": "2026-11-30",
          "evidence": [
            "ASSIGNMENT"
          ]
        }
      ]
    },
    {
      "id": "SOL",
      "name": "双店预约试点架构角色",
      "tier": "solution",
      "scope": "双店预约试点",
      "segment_scope": "双店预约试点",
      "primary_responsibility": "界定双店预约试点的变更与接口责任",
      "activities": [
        "维护双店预约试点的接口决定"
      ],
      "key_stakeholders": [
        "运营负责人"
      ],
      "evidence": [
        "MANDATE"
      ],
      "kpis": [
        {
          "id": "SOL-KPI",
          "measure": "带评审依据的接口决定比例",
          "target": 100,
          "target_origin": "project-adopted",
          "unit": "%",
          "measurement_period": "2026年11月",
          "measurement_source": "决定登记册",
          "owner": "架构实践负责人",
          "formula_or_rule": "有评审依据条数/全部决定条数×100",
          "adopted_by": "虚构实践负责人",
          "evidence": [
            "KPI-POLICY"
          ]
        }
      ]
    }
  ]
}
```

## 来源规则与项目规则

1. **来源规则**：G249区分岗位、角色与任务，允许一人多角色；三类架构视角及首席特例不是通用人事职级总序。
2. **项目规则**：本案例采用明确的来源ID、结构字段和有界状态；执行器检查可观察契约，业务充分性另由推理审阅说明。
3. **项目规则**：变化场景只改变材料中列出的事实；未变字段不被重新编造，所有批准与实际运行效果均保持未授予。

## 转换与推理

1. 专业指导只覆盖预约接口，不推出人事管理关系。
2. 岗位、角色和任务以三个独立引用保存；一条任务分配不构成胜任认证。
3. 目标100%来自本项目材料；不是把G249示例3/5搬成企业目标。
4. 11月8日属于授权期，12月1日不属于；任期变化与角色定义是否齐全分开判断。

## 输出与追溯

下列预期在执行前由业务材料独立编写；实际执行只对这些明确字段作比较。

```json
{
  "gap_reasons": [],
  "row_states": [
    "defined-awaiting-hr-and-governance-review",
    "defined-awaiting-hr-and-governance-review",
    "defined-awaiting-hr-and-governance-review"
  ]
}
```

字段齐全只允许进入人力与治理评审。

机械可复核字段、缺口和引用；业务结论不由计算器输出自动批准。完整输入、预期与实际结果见本轮方法证据目录。

## 修改演练

本次替换的业务字段如下；需按新事实重评。

- `as_of`："2026-11-08" → "2026-12-01"

复核日改到12月1日，11月任务分配不再是当前授权。

变化后需重新执行原方法；原结论只保留到未改变的事实范围。

```json
{
  "gap_ids": [
    "ASSIGN:period"
  ]
}
```

## 反例与输入不足

- 缺输入：删除KPI取数来源，不能用目标值代替观察口径。 预期 `missing-input`，这是结果中的缺口原因，不是伪装为抛异常。
- 结构反例：把专业指导指向未登记角色，拒绝悬空关系。 预期 `ROLE-REL`，此项由执行器实际拒绝。

缺输入的预期结果：

```json
{
  "gap_ids": [
    "SEG-KPI:measurement_source"
  ],
  "row_states": [
    "defined-awaiting-hr-and-governance-review",
    "needs-input",
    "defined-awaiting-hr-and-governance-review"
  ]
}
```

## 评审记录

- 已将本案来源规则与明确的项目约定分开。
- 已核对充分、缺输入、变化及结构反例四类材料的实际结果。
- 已核对缺输入没有被补为通过、零值或真实授权。
- 专业指导只覆盖预约接口，不推出人事管理关系。
- 岗位、角色和任务以三个独立引用保存；一条任务分配不构成胜任认证。
- 目标100%来自本项目材料；不是把G249示例3/5搬成企业目标。
- 11月8日属于授权期，12月1日不属于；任期变化与角色定义是否齐全分开判断。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
