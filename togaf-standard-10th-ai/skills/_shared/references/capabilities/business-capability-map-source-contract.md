# G211 基础工作产品契约

稳定工作产品 ID：`business-capability-map`；规范：`capability-decomposition`。复用基础制品，不新增重复制品族。

```json
{
  "id": "business-capability-map",
  "registration_class": "base-artifact-work-product-binding",
  "guide": "G211",
  "source_refs": [
    "G211/fig3-3",
    "G211 §3–5"
  ],
  "owner": "togaf-strategy-capabilities",
  "profile_id": "capability-decomposition",
  "decision": "企业能力范围、分解及差距集中在哪里？",
  "required_inputs": [
    "带来源的业务范围、对象定义及类型化关系"
  ],
  "analysis_steps": [
    "先定义能力边界与一致命名",
    "以同层粒度分组并显式分解",
    "按单一已定义量尺叠加热力指标"
  ],
  "required_attributes": {
    "capability": [
      "definition",
      "category",
      "level"
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
        "id": "capability-decomposition-fulfillment",
        "type": "capability",
        "name": "订单履约",
        "attributes": {
          "definition": "使已确认订单按承诺交付，排除市场获客",
          "category": "核心",
          "level": 1
        },
        "evidence": [
          "example-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "capability-decomposition-order",
        "type": "capability",
        "name": "订单管理",
        "attributes": {
          "definition": "建立并维持准确订单状态",
          "category": "核心",
          "level": 2
        },
        "evidence": [
          "example-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "capability-decomposition-delivery",
        "type": "capability",
        "name": "交付管理",
        "attributes": {
          "definition": "管理发运承诺和交付结果",
          "category": "核心",
          "level": 2
        },
        "evidence": [
          "example-source"
        ],
        "certainty": "assumed"
      }
    ],
    "relationships": [
      {
        "id": "capability-decomposition-decomp-order",
        "type": "decomposes",
        "source": "capability-decomposition-fulfillment",
        "target": "capability-decomposition-order",
        "label": "履约能力分解为订单管理",
        "evidence": [
          "example-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "capability-decomposition-decomp-delivery",
        "type": "decomposes",
        "source": "capability-decomposition-fulfillment",
        "target": "capability-decomposition-delivery",
        "label": "履约能力分解为交付管理",
        "evidence": [
          "example-source"
        ],
        "certainty": "assumed"
      }
    ],
    "view": {
      "id": "v-capability-decomposition",
      "artifact_id": "business-capability-map",
      "profile_id": "capability-decomposition",
      "title": "能力分解地图／虚构案例",
      "entity_ids": [
        "capability-decomposition-fulfillment",
        "capability-decomposition-order",
        "capability-decomposition-delivery"
      ],
      "relationship_ids": [
        "capability-decomposition-decomp-order",
        "capability-decomposition-decomp-delivery"
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
python skills/_shared/scripts/verify_artifact_profiles.py --profile capability-decomposition --out output/g211-contract --render
```
