# 交付物章程与验收流程

`profile_id`: project-deliverable-charter-default；`artifact_id`: project-deliverable-charter；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G188 §3.1.8示例3-14、§3.2.2–3.2.3、§3.5.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "project-deliverable-charter-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:deliverable_charter。关系类型：。

```json
{
  "entities": {
    "guide:deliverable_charter": [
      "deliverable_id",
      "scope",
      "exclusions",
      "required_inputs",
      "acceptance_criteria",
      "acceptance_process",
      "decision_roles",
      "review_observations",
      "status",
      "evidence_refs",
      "next_action"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 文档与软件可有不同验收流程，不复制时长为TOGAF要求
- 生成、移交、评审与接受是不同状态
- 一项未满足准则不能被其他已满足项的数量抵消

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-project-deliverable-charter-default",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 charter",
      "locator": "examples/addenda/project-management/raw-business-materials.json#charter"
    }
  ],
  "entities": [
    {
      "id": "project-deliverable-charter-default-1",
      "type": "guide:deliverable_charter",
      "name": "应用关系与信息使用说明章程",
      "attributes": {
        "deliverable_id": "DEL-REL-v1",
        "scope": "城东/城西两仓订单与库存接口，12应用",
        "exclusions": [
          "薪酬系统"
        ],
        "required_inputs": [
          {
            "id": "DEL-APPS-v2",
            "status": "provided"
          },
          {
            "id": "DATA-INTERVIEWS",
            "status": "APP-12资料缺失"
          }
        ],
        "acceptance_criteria": [
          {
            "id": "AC-COVERAGE",
            "rule": "12应用全部覆盖",
            "required_total": 12,
            "observed": 11,
            "result": "not-met"
          },
          {
            "id": "AC-DIRECTION",
            "rule": "方向来自接口记录",
            "result": "needs-review"
          },
          {
            "id": "AC-USEMOD",
            "rule": "信息使用/修改分别表达",
            "result": "needs-review"
          },
          {
            "id": "AC-UNKNOWN",
            "rule": "未知带ID与责任人",
            "result": "needs-review"
          }
        ],
        "acceptance_process": [
          {
            "step": "初审",
            "duration": 5,
            "unit": "workday",
            "role": "业务代表"
          },
          {
            "step": "处理意见",
            "duration": 3,
            "unit": "workday",
            "role": "架构师"
          },
          {
            "step": "终审",
            "duration": 2,
            "unit": "workday",
            "role": "业务负责人",
            "outcomes": [
              "accept",
              "reject",
              "rework"
            ]
          }
        ],
        "decision_roles": "业务代表评审、架构师修订、业务负责人接受；项目经理记录",
        "review_observations": "APP-12接口缺失，当前只覆盖11应用",
        "status": "in-review; not-accepted",
        "evidence_refs": [
          "DC-01",
          "DC-02",
          "DC-03",
          "DC-04"
        ],
        "next_action": "补APP-12数据并复核其余条件；终审不预设通过"
      },
      "evidence": [
        "src-project-deliverable-charter-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-deliverable-charter-default",
    "artifact_id": "project-deliverable-charter",
    "profile_id": "project-deliverable-charter-default",
    "title": "交付物章程与验收流程",
    "entity_ids": [
      "project-deliverable-charter-default-1"
    ],
    "relationship_ids": [],
    "analysis": "从DC-01/02区分范围、排除、输入和四条验收准则；DC-03是项目5/3/2日流程，不照搬G188示例的2周等时长。11/12覆盖不满足准则。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "charter"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-deliverable-charter-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-deliverable-charter-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
