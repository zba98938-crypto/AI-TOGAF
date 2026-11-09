# 项目工作包授权记录

ID：`project-work-package-authorization`。主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G188 §2.3、§3.4.1–3.4.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

项目WBS工作能否开始，产品、前提和授权是否齐备？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 项目WBS工作能否开始，产品、前提和授权是否齐备？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 范围、五维语境、所用目标与交付物版本
- 原始计划/访谈/验收/估算及来源ID
- 组织授权和容差规则；缺失时不代推

可选：

- 历史项目及组织模板

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:project_authorization。

```json
{
  "guide:project_authorization": [
    "project_task_id",
    "wbs_parent",
    "work_package_kind",
    "deliverable",
    "preconditions",
    "cost_time_tolerance",
    "quality_configuration",
    "reporting",
    "authority",
    "authorization",
    "evidence_refs",
    "next_action"
  ],
  "project": [
    "scope",
    "sponsor",
    "start",
    "end",
    "budget",
    "status"
  ]
}
```

{
  "name": {
    "meaning": "授权事项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "project_task_id": {
    "meaning": "项目任务稳定ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "wbs_parent": {
    "meaning": "WBS父项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "work_package_kind": {
    "meaning": "必须明确project-wbs-leaf，非TOGAF变革包",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "deliverable": {
    "meaning": "应交付产品及范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "preconditions": {
    "meaning": "前置产品验收与其他进入条件",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "cost_time_tolerance": {
    "meaning": "成本/工期/容差及项目规则出处",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "quality_configuration": {
    "meaning": "质量准则、版本/配置要求",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "reporting": {
    "meaning": "检查点频率和信息分发",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "authority": {
    "meaning": "谁有权授权以及授权范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "authorization": {
    "meaning": "未授权/授权证据，不能从空闲推断",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "next_action": {
    "meaning": "允许开始或缺口处理",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 识别PM项目工作包及其WBS/产品范围
2. 核实前置产品验收及所有进入条件
3. 确认成本/工期/容差、质量配置及报告要求
4. 取得权限范围内PM明确授权并留记录
5. 完成并接受产品后才允许后续工作包重新走授权

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 依赖完成不等于已授权，团队空闲不等于允许开始
- PM工作包与变革工作包分开建模
- 无授权记录不得转为已开始或已完成

- 依赖完成不等于已授权，团队空闲不等于允许开始
- PM工作包与变革工作包分开建模
- 无授权记录不得转为已开始或已完成


## 视图和交付物

- [项目工作包授权记录](../profiles/project-work-package-authorization-default.md)

- [statement-of-work](../deliverables/statement-of-work.md)
- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "无授权却请求开始",
    "expected": "authorization-not-ready"
  },
  "modification_example": {
    "change": "DEL-APPS-v2已接受且PM确认规则并发授权",
    "expected": "状态改为authorized-in-fixture，可在虚构案例开始；不授予真实人工作权限"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/project-work-package-authorization.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-project-work-package-authorization-default",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 authorization",
      "locator": "examples/addenda/project-management/raw-business-materials.json#authorization"
    }
  ],
  "entities": [
    {
      "id": "project-work-package-authorization-default-1",
      "type": "guide:project_authorization",
      "name": "接口数据分析授权",
      "attributes": {
        "project_task_id": "PM-WP-DATA",
        "wbs_parent": "WBS-RELATIONS",
        "work_package_kind": "project-wbs-leaf",
        "deliverable": "DEL-DATA：接口数据分析；依赖DEL-APPS-v2",
        "preconditions": [
          {
            "id": "DEL-APPS-v2",
            "accepted": false,
            "evidence": "AU-02待业务签字"
          }
        ],
        "cost_time_tolerance": {
          "duration": 3,
          "duration_unit": "workday",
          "effort": 40,
          "effort_unit": "person-hour",
          "cost": 8000,
          "currency": "CNY",
          "time_tolerance": 1,
          "cost_tolerance": 1000,
          "rule_status": "项目提案，待PM确认"
        },
        "quality_configuration": "应用关系与CRUD分开；存储库data-analysis-v1；验收引用AC-DATA",
        "reporting": "每周检查点；异常向PM报告",
        "authority": "项目经理；依据项目章程，范围待核实",
        "authorization": "not-authorized",
        "evidence_refs": [
          "AU-01",
          "AU-02",
          "AU-03"
        ],
        "next_action": "前置产品未接受且无明确授权，不开始；先取得签字和PM授权"
      },
      "evidence": [
        "src-project-work-package-authorization-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-work-package-authorization-default",
    "artifact_id": "project-work-package-authorization",
    "profile_id": "project-work-package-authorization-default",
    "title": "项目工作包授权记录",
    "entity_ids": [
      "project-work-package-authorization-default-1"
    ],
    "relationship_ids": [],
    "analysis": "AU-02前置交付物未获接受，也没有PM明确授权；团队空闲不能替代任一条件。成本/时间容差仍是提案。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "authorization"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact project-work-package-authorization --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
