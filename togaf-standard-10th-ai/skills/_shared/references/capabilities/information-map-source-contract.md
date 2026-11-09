# G190 基础工作产品契约

稳定工作产品 ID：`information-map`；规范：`information-concept-network`。复用基础制品，不新增重复制品族。

```json
{
  "id": "information-map",
  "registration_class": "base-artifact-work-product-binding",
  "guide": "G190",
  "source_refs": [
    "G190/fig2-1",
    "G190 §3–5"
  ],
  "owner": "togaf-information-data",
  "profile_id": "information-concept-network",
  "decision": "哪些业务信息概念需要共同理解及管理？",
  "required_inputs": [
    "带来源的业务范围、对象定义及类型化关系"
  ],
  "analysis_steps": [
    "从业务语言构造信息主题",
    "按概念关联而非数据库结构组织",
    "映射业务能力、价值流和责任方"
  ],
  "required_attributes": {
    "information": [
      "definition",
      "owner"
    ]
  },
  "example": {
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
  },
  "counterexample": {
    "input": "删除已选对象的必需业务属性",
    "expected": "missing-profile-attribute",
    "why": "缺定义、范围或责任时不得声称完整工作产品。"
  },
  "modification_example": {
    "change": "修改同ID对象的definition，并核对两种布局中的正文与覆盖位置",
    "expected": "新定义出现在保存输出；旧定义不作为当前事实。"
  },
  "evidence_policy": "执行verify_artifact_profiles.py逐profile的原始、修改及反例；来源等价和业务批准分别评审。"
}
```

执行原始输入、实质修改与必需属性反例：

```sh
python skills/_shared/scripts/verify_artifact_profiles.py --profile information-concept-network --out output/g190-contract --render
```
