# 架构项目工作分解

ID：`architecture-project-wbs`。主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

怎样把架构成果分解为可管理工作？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 怎样把架构成果分解为可管理工作？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- deliverable
- work_package
- owner

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：architecture_task。

```json
{
  "architecture_task": [
    "deliverable",
    "work_package",
    "owner",
    "effort",
    "dependency",
    "acceptance"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "deliverable": {
    "meaning": "架构交付物引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "work_package": {
    "meaning": "工作包引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "effort": {
    "meaning": "投入估算及单位",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "dependency": {
    "meaning": "依赖对象及方向",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "acceptance": {
    "meaning": "验收准则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `project:wbs_decomposes` | architecture_task → architecture_task | 架构项目WBS整体任务分解为可验收子任务；不是E/F变革工作包依赖，也不是批准关系 |

## 分析步骤

1. 明确范围与排除项
2. 按成果分解工作
3. 核对遗漏和重复
4. 指定责任估算与验收

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F


## 视图和交付物

- [架构项目工作分解](../profiles/architecture-project-wbs-default.md)

- [statement-of-work](../deliverables/statement-of-work.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构项目工作分解」给出：架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F",
    "expected": "missing-evidence",
    "why": "架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F"
  },
  "modification_example": {
    "change": "在「架构项目工作分解」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-project-wbs --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
