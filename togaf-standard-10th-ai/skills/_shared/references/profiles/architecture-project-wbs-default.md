# 架构项目工作分解

`profile_id`: architecture-project-wbs-default；`artifact_id`: architecture-project-wbs；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.2。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.2。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "version": "2.2"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：architecture_task。关系类型：project:wbs_decomposes。

```json
{
  "entities": {
    "architecture_task": [
      "deliverable",
      "work_package",
      "owner",
      "effort",
      "dependency",
      "acceptance"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务原料：接口与信息使用架构定义：{\"deliverable\": \"DEL-APP-SPEC-v1，两个仓的接口和信息使用说明\", \"work_package\": \"PM-WBS-1，架构项目任务；非TOGAF变革工作包\", \"owner\": \"架构项目经理\", \"effort\": {\"value\": 8, \"unit\": \"person-day\", \"basis\": \"虚构团队估算3+5人日\"}, \"dependency\": \"输入应用清单版本2需被业务接受\", \"acceptance\": \"12应用覆盖，接口方向和信息使用/修改分开表达，所有未知附ID与责任\", \"definition\": \"分配工作与验收；估算不代表承诺\"}；确认应用范围与职责：{\"deliverable\": \"DEL-APPS-v2，两个仓12应用的职责目录\", \"work_package\": \"PM-WBS-1.1，WBS叶任务\", \"owner\": \"业务分析师\", \"effort\": {\"value\": 3, \"unit\": \"person-day\", \"basis\": \"本项目估算\"}, \"dependency\": \"仓储负责人提供在用系统清单\", \"acceptance\": \"范围内12应用有唯一ID、职责、负责人；双方业务代表确认边界\", \"definition\": \"形成被接受的输入；不能因团队空闲视作已获开始授权\"}；分析接口与信息使用：{\"deliverable\": \"DEL-APP-SPEC-v1，接口和信息使用表\", \"work_package\": \"PM-WBS-1.2，WBS叶任务\", \"owner\": \"应用与数据架构师\", \"effort\": {\"value\": 5, \"unit\": \"person-day\", \"basis\": \"本项目估算\"}, \"dependency\": \"消费已接受DEL-APPS-v2，未知接口指派调查责任\", \"acceptance\": \"所有12应用覆盖；接口证据可追溯，未知带ID，CRUD与信息使用/修改不混同\", \"definition\": \"依赖和授权另有记录；相邻图形不代表自动顺序\"}"
    }
  ],
  "entities": [
    {
      "id": "architecture-project-wbs-default-root",
      "type": "architecture_task",
      "name": "接口与信息使用架构定义",
      "attributes": {
        "deliverable": "DEL-APP-SPEC-v1，两个仓的接口和信息使用说明",
        "work_package": "PM-WBS-1，架构项目任务；非TOGAF变革工作包",
        "owner": "架构项目经理",
        "effort": {
          "value": 8,
          "unit": "person-day",
          "basis": "虚构团队估算3+5人日"
        },
        "dependency": "输入应用清单版本2需被业务接受",
        "acceptance": "12应用覆盖，接口方向和信息使用/修改分开表达，所有未知附ID与责任",
        "definition": "分配工作与验收；估算不代表承诺"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-project-wbs-default-child0",
      "type": "architecture_task",
      "name": "确认应用范围与职责",
      "attributes": {
        "deliverable": "DEL-APPS-v2，两个仓12应用的职责目录",
        "work_package": "PM-WBS-1.1，WBS叶任务",
        "owner": "业务分析师",
        "effort": {
          "value": 3,
          "unit": "person-day",
          "basis": "本项目估算"
        },
        "dependency": "仓储负责人提供在用系统清单",
        "acceptance": "范围内12应用有唯一ID、职责、负责人；双方业务代表确认边界",
        "definition": "形成被接受的输入；不能因团队空闲视作已获开始授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-project-wbs-default-child1",
      "type": "architecture_task",
      "name": "分析接口与信息使用",
      "attributes": {
        "deliverable": "DEL-APP-SPEC-v1，接口和信息使用表",
        "work_package": "PM-WBS-1.2，WBS叶任务",
        "owner": "应用与数据架构师",
        "effort": {
          "value": 5,
          "unit": "person-day",
          "basis": "本项目估算"
        },
        "dependency": "消费已接受DEL-APPS-v2，未知接口指派调查责任",
        "acceptance": "所有12应用覆盖；接口证据可追溯，未知带ID，CRUD与信息使用/修改不混同",
        "definition": "依赖和授权另有记录；相邻图形不代表自动顺序"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "architecture-project-wbs-default-part0",
      "type": "project:wbs_decomposes",
      "source": "architecture-project-wbs-default-root",
      "target": "architecture-project-wbs-default-child0",
      "label": "架构项目WBS整体任务分解为可验收子任务；不是E/F变革工作包依赖，也不是批准关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-project-wbs-default-part1",
      "type": "project:wbs_decomposes",
      "source": "architecture-project-wbs-default-root",
      "target": "architecture-project-wbs-default-child1",
      "label": "架构项目WBS整体任务分解为可验收子任务；不是E/F变革工作包依赖，也不是批准关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-architecture-project-wbs-default",
    "artifact_id": "architecture-project-wbs",
    "profile_id": "architecture-project-wbs-default",
    "title": "架构项目工作分解／虚构案例",
    "entity_ids": [
      "architecture-project-wbs-default-root",
      "architecture-project-wbs-default-child0",
      "architecture-project-wbs-default-child1"
    ],
    "relationship_ids": [
      "architecture-project-wbs-default-part0",
      "architecture-project-wbs-default-part1"
    ],
    "analysis": "从本例原始职责、权限、契约与验收材料形成明确分解。关系类型为命名空间项目语义，来源仅指导方法。父子结构不赋予批准或执行先后。",
    "legend": "嵌套只表示已声明的project:wbs_decomposes关系；候选事实、实际批准与实现状态分开。"
  },
  "extensions": {
    "relationship_types": {
      "project:wbs_decomposes": {
        "source_types": [
          "architecture_task"
        ],
        "target_types": [
          "architecture_task"
        ],
        "meaning": "架构项目WBS整体任务分解为可验收子任务；不是E/F变革工作包依赖，也不是批准关系"
      }
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-project-wbs-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-project-wbs-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
