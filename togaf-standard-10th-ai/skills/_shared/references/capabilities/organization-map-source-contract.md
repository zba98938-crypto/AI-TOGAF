# G206 基础工作产品契约

稳定工作产品 ID：`organization-map`；规范：`organization-work-network`。复用基础制品，不新增重复制品族。

```json
{
  "id": "organization-map",
  "registration_class": "base-artifact-work-product-binding",
  "guide": "G206",
  "source_refs": [
    "G206/fig3-2",
    "G206 §5 表5-1"
  ],
  "owner": "togaf-organization-roles",
  "profile_id": "organization-work-network",
  "decision": "组织边界、协作、能力责任与外部关系如何分布？",
  "required_inputs": [
    "带来源的业务范围、对象定义及类型化关系"
  ],
  "analysis_steps": [
    "识别价值交付涉及的内外部组织",
    "表达合作与责任边界",
    "结合能力责任检查孤岛及共享"
  ],
  "required_attributes": {
    "organization": [
      "category",
      "boundary",
      "definition"
    ],
    "capability": [
      "definition"
    ],
    "information": [
      "definition"
    ]
  },
  "example": {
    "notice": "虚构业务案例；采用来源结构及术语，不代表真实实施或批准。",
    "sources": [
      {
        "id": "case-source",
        "kind": "example",
        "description": "虚构访谈：运营负责订单处理、承运方负责履约协调，二者使用订单信息；运营在确认后将订单信息交接承运方。结构链不证明实际发生或批准。"
      }
    ],
    "entities": [
      {
        "id": "organization-work-network-enterprise",
        "type": "organization",
        "name": "星河零售",
        "attributes": {
          "category": "企业",
          "boundary": "选定企业生态范围，不表示法律母公司或汇报上级",
          "definition": "在线销售与履约的共同业务语境"
        },
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-ops",
        "type": "organization",
        "name": "在线运营",
        "attributes": {
          "category": "业务单元",
          "boundary": "内部",
          "definition": "管理在线订单和客户例外"
        },
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-carrier",
        "type": "organization",
        "name": "承运合作方",
        "attributes": {
          "category": "外部伙伴",
          "boundary": "企业外部合同边界",
          "definition": "按合同交付商品"
        },
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-order-capability",
        "type": "capability",
        "name": "订单处理能力",
        "attributes": {
          "definition": "运营负责确认订单与交接"
        },
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-delivery-capability",
        "type": "capability",
        "name": "履约协调能力",
        "attributes": {
          "definition": "合作方负责协调委托履约"
        },
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-order-information",
        "type": "information",
        "name": "订单信息",
        "attributes": {
          "definition": "用于订单确认与委托履约的信息概念；不是物理表"
        },
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      }
    ],
    "relationships": [
      {
        "id": "organization-work-network-works",
        "type": "collaborates_with",
        "source": "organization-work-network-ops",
        "target": "organization-work-network-carrier",
        "label": "共同处理履约例外；不是汇报",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-info",
        "type": "organization_information_exchange",
        "source": "organization-work-network-ops",
        "target": "organization-work-network-carrier",
        "label": "确认订单后运营向承运合作方交接订单信息（虚构访谈声明）",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed",
        "attributes": {
          "information_ref": "订单概念",
          "derivation_path": "在线运营←订单处理能力→订单信息←履约协调能力→承运合作方；路径只证明关联，交换方向另由访谈声明",
          "condition": "确认订单后",
          "information_ref_id": "organization-work-network-order-information",
          "derivation_relationship_ids": [
            "organization-work-network-order-owned",
            "organization-work-network-order-used",
            "organization-work-network-delivery-owned",
            "organization-work-network-delivery-used"
          ]
        }
      },
      {
        "id": "organization-work-network-value",
        "type": "organization_value_exchange",
        "source": "organization-work-network-carrier",
        "target": "organization-work-network-ops",
        "label": "履约服务：按委托完成交付",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed",
        "attributes": {
          "value_item": "配送履约服务",
          "condition": "合同服务范围内；不推断付款方向"
        }
      },
      {
        "id": "organization-work-network-order-owned",
        "type": "owned_by",
        "source": "organization-work-network-order-capability",
        "target": "organization-work-network-ops",
        "label": "订单处理能力由在线运营负责",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-order-used",
        "type": "uses_information",
        "source": "organization-work-network-order-capability",
        "target": "organization-work-network-order-information",
        "label": "订单处理使用订单信息",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-delivery-owned",
        "type": "owned_by",
        "source": "organization-work-network-delivery-capability",
        "target": "organization-work-network-carrier",
        "label": "履约协调能力由承运合作方负责",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      },
      {
        "id": "organization-work-network-delivery-used",
        "type": "uses_information",
        "source": "organization-work-network-delivery-capability",
        "target": "organization-work-network-order-information",
        "label": "履约协调使用订单信息",
        "evidence": [
          "case-source"
        ],
        "certainty": "assumed"
      }
    ],
    "view": {
      "id": "v-organization-work-network",
      "artifact_id": "organization-map",
      "profile_id": "organization-work-network",
      "title": "组织工作网络",
      "entity_ids": [
        "organization-work-network-enterprise",
        "organization-work-network-ops",
        "organization-work-network-carrier",
        "organization-work-network-order-capability",
        "organization-work-network-delivery-capability",
        "organization-work-network-order-information"
      ],
      "relationship_ids": [
        "organization-work-network-works",
        "organization-work-network-info",
        "organization-work-network-value",
        "organization-work-network-order-owned",
        "organization-work-network-order-used",
        "organization-work-network-delivery-owned",
        "organization-work-network-delivery-used"
      ],
      "analysis": "先区分组织、能力和独立信息概念，按owned_by及uses_information追溯两端关联；定向信息交换仅依据另行声明的虚构访谈，不能由共用信息自动推断。",
      "legend": "同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。"
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
python skills/_shared/scripts/verify_artifact_profiles.py --profile organization-work-network --out output/g206-contract --render
```
