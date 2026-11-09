# 信息概念关系网络

`profile_id`: information-concept-network；`artifact_id`: information-map；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G190/fig2-1。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G190/fig2-1",
  "layout_notes": "信息概念是业务语义；关系名称必须明确",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/information-concept-network.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：information。关系类型：traces_to。

```json
{
  "entities": {
    "information": [
      "definition",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 信息概念是业务语义；关系名称必须明确

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
      "id": "information-concept-network-customer",
      "type": "information",
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
      "id": "information-concept-network-account",
      "type": "information",
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
      "id": "information-concept-network-association",
      "type": "traces_to",
      "source": "information-concept-network-customer",
      "target": "information-concept-network-account",
      "label": "客户持有账户；基数按本例约束",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-information-concept-network",
    "artifact_id": "information-map",
    "profile_id": "information-concept-network",
    "title": "信息概念关系网络／虚构案例",
    "entity_ids": [
      "information-concept-network-customer",
      "information-concept-network-account"
    ],
    "relationship_ids": [
      "information-concept-network-association"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-concept-network --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-concept-network --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
