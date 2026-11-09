# 项目工作包授权记录

`profile_id`: project-work-package-authorization-default；`artifact_id`: project-work-package-authorization；主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md)。

来源：G188 §2.3、§3.4.1–3.4.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "project-work-package-authorization-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:project_authorization。关系类型：。

```json
{
  "entities": {
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
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 依赖完成不等于已授权，团队空闲不等于允许开始
- PM工作包与变革工作包分开建模
- 无授权记录不得转为已开始或已完成

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-work-package-authorization-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-work-package-authorization-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
