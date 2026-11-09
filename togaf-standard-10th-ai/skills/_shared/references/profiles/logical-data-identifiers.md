# 逻辑实体属性与标识

`profile_id`: logical-data-identifiers；`artifact_id`: logical-data-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G190/figA-3；G190 Appendix A.2。

## 构图与定义状态

表示族：`er`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G190/figA-3",
  "layout_notes": "属性、标识、可选性、基数明确，物理实现另行追溯",
  "review_status": "source-located-awaiting-template-validation"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：logical_entity。关系类型：logical_association。

```json
{
  "entities": {
    "logical_entity": [
      "definition",
      "attributes",
      "identifier"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 属性、标识、可选性、基数明确，物理实现另行追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "logical-data-identifiers-customer",
      "type": "logical_entity",
      "name": "客户",
      "attributes": {
        "definition": "形成购买关系且承担订单责任的主体",
        "owner": "客户业务所有者",
        "identifier": "客户业务标识",
        "attributes": [
          {
            "name": "客户标识",
            "type": "string",
            "key": "PK",
            "optional": false
          },
          {
            "name": "名称",
            "type": "string",
            "optional": false
          }
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "logical-data-identifiers-account",
      "type": "logical_entity",
      "name": "账户",
      "attributes": {
        "definition": "客户访问订单服务的授权身份",
        "owner": "身份业务所有者",
        "identifier": "账户标识",
        "attributes": [
          {
            "name": "账户标识",
            "type": "string",
            "key": "PK",
            "optional": false
          },
          {
            "name": "客户标识",
            "type": "string",
            "key": "FK",
            "optional": false
          }
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "logical-data-identifiers-association",
      "type": "logical_association",
      "source": "logical-data-identifiers-customer",
      "target": "logical-data-identifiers-account",
      "label": "客户持有账户；基数按本例约束",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "cardinality": {
        "source": {
          "min": 1,
          "max": 2
        },
        "target": {
          "min": 1,
          "max": null
        }
      }
    }
  ],
  "view": {
    "id": "v-logical-data-identifiers",
    "artifact_id": "logical-data-diagram",
    "profile_id": "logical-data-identifiers",
    "title": "逻辑实体属性与标识／虚构案例",
    "entity_ids": [
      "logical-data-identifiers-customer",
      "logical-data-identifiers-account"
    ],
    "relationship_ids": [
      "logical-data-identifiers-association"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile logical-data-identifiers --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile logical-data-identifiers --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
