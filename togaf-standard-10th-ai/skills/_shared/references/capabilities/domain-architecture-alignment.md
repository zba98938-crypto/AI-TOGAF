# 领域架构融入整体EA核对

ID：`domain-architecture-alignment`。主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G186 §12.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

各领域架构是否服务同一EA项目与目标、引用共享模型，安全是否作为关注点贯穿其他域？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 各领域架构是否服务同一EA项目与目标、引用共享模型，安全是否作为关注点贯穿其他域？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'kind', 'meaning': '领域类别', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'project_id', 'meaning': '所属EA项目ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'objective_ids', 'meaning': '服务的EA项目目标ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'model_id', 'meaning': '共享架构模型ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'shared_entity_ids', 'meaning': '引用的共享模型对象ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'treated_as', 'meaning': '安全的处理方式：concern或其他', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'referenced_domain_ids', 'meaning': '安全关注点所引用的其他领域ID', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:domain-architecture, guide:ea-project-scope。

```json
{
  "guide:domain-architecture": [
    "kind",
    "project_id",
    "objective_ids"
  ],
  "guide:ea-project-scope": [
    "objective_ids",
    "model_id"
  ]
}
```

{
  "kind": {
    "meaning": "领域类别",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "project_id": {
    "meaning": "所属EA项目ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "objective_ids": {
    "meaning": "服务的EA项目目标ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "model_id": {
    "meaning": "共享架构模型ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "shared_entity_ids": {
    "meaning": "引用的共享模型对象ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "treated_as": {
    "meaning": "安全的处理方式：concern或其他",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "referenced_domain_ids": {
    "meaning": "安全关注点所引用的其他领域ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 登记EA项目及其目标与共享模型
2. 登记每个领域架构所属项目、服务目标及共享对象
3. 标出按另一个项目工作或目的不在EA目标内的领域
4. 把安全作为关注点并引用其所涉其他领域
5. 修正后再进入跨域评审

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 领域必须融入整体EA，整体EA也须契合领域
- 安全架构只在参照其他域时存在，按关注点处理
- 对齐核对不评价领域方案质量

- 名称、来源表格和成功输出不等于业务结论已核实
- 领域必须融入整体EA，整体EA也须契合领域
- 安全架构只在参照其他域时存在，按关注点处理
- 对齐核对不评价领域方案质量


## 视图和交付物

- [领域架构融入整体EA核对](../profiles/domain-architecture-alignment-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "安全关注点引用不存在的领域",
    "expected": "DAA-002",
    "why": "DAA-002 [DOM-SEC]: Security references unknown domain DOM-NONE"
  },
  "modification_example": {
    "change": "数据领域改为服务EA-2027的OBJ-1并引用共享对象",
    "expected": "分析结果变化：关闭缺口DOM-DATA:shared-model"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/domain-architecture-alignment.md)
[完整操作案例](../../references/capability-addenda/domain-architecture-alignment.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "DAA-R1",
      "kind": "example",
      "description": "虚构EA项目EA-2027：目标OBJ-1缩短履约时长、OBJ-2降低合规风险，共享模型M-1。",
      "locator": "raw-materials.json#DAA-R1"
    },
    {
      "id": "DAA-R2",
      "kind": "example",
      "description": "数据领域团队按自建“数据中台项目DP-9”推进，目标为“建设统一数据平台”；安全团队计划单独编写安全架构文档。",
      "locator": "raw-materials.json#DAA-R2"
    }
  ],
  "entities": [
    {
      "id": "EA-2027",
      "type": "guide:ea-project-scope",
      "name": "EA项目EA-2027",
      "attributes": {
        "objective_ids": [
          "OBJ-1",
          "OBJ-2"
        ],
        "model_id": "M-1"
      },
      "evidence": [
        "DAA-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DOM-BIZ",
      "type": "guide:domain-architecture",
      "name": "业务架构",
      "attributes": {
        "kind": "business",
        "project_id": "EA-2027",
        "objective_ids": [
          "OBJ-1"
        ],
        "shared_entity_ids": [
          "cap-fulfilment"
        ]
      },
      "evidence": [
        "DAA-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DOM-DATA",
      "type": "guide:domain-architecture",
      "name": "数据架构",
      "attributes": {
        "kind": "data",
        "project_id": "DP-9",
        "objective_ids": [
          "OBJ-DP"
        ],
        "shared_entity_ids": []
      },
      "evidence": [
        "DAA-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DOM-SEC",
      "type": "guide:domain-architecture",
      "name": "安全架构",
      "attributes": {
        "kind": "security",
        "project_id": "EA-2027",
        "objective_ids": [
          "OBJ-2"
        ],
        "shared_entity_ids": [
          "req-privacy"
        ],
        "treated_as": "standalone-document",
        "referenced_domain_ids": []
      },
      "evidence": [
        "DAA-R2"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "domain-architecture-alignment-baseline",
    "artifact_id": "domain-architecture-alignment",
    "profile_id": "domain-architecture-alignment-default",
    "title": "领域架构融入整体EA核对／虚构星河零售",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "EA-2027",
      "DOM-BIZ",
      "DOM-DATA",
      "DOM-SEC"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行domain-architecture-alignment-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "domain-architecture-alignment-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "domain-architecture-alignment-analysis",
      "method_id": "domain-architecture-alignment-review",
      "inputs": {
        "source_ids": [
          "DAA-R1",
          "DAA-R2"
        ],
        "ea_project": {
          "id": "EA-2027",
          "objective_ids": [
            "OBJ-1",
            "OBJ-2"
          ]
        },
        "domains": [
          {
            "id": "DOM-BIZ",
            "name": "业务架构",
            "kind": "business",
            "project_id": "EA-2027",
            "objective_ids": [
              "OBJ-1"
            ],
            "shared_entity_ids": [
              "cap-fulfilment"
            ],
            "evidence": [
              "DAA-R1"
            ]
          },
          {
            "id": "DOM-DATA",
            "name": "数据架构",
            "kind": "data",
            "project_id": "DP-9",
            "objective_ids": [
              "OBJ-DP"
            ],
            "shared_entity_ids": [],
            "evidence": [
              "DAA-R2"
            ]
          },
          {
            "id": "DOM-SEC",
            "name": "安全架构",
            "kind": "security",
            "project_id": "EA-2027",
            "objective_ids": [
              "OBJ-2"
            ],
            "shared_entity_ids": [
              "req-privacy"
            ],
            "treated_as": "standalone-document",
            "referenced_domain_ids": [],
            "evidence": [
              "DAA-R2"
            ]
          }
        ]
      }
    }
  ]
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact domain-architecture-alignment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
