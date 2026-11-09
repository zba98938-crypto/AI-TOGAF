# SOA 分层参考

ID：`soa-layered-reference`。主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G21I/fig5-3。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。



## 输入及缺口处理

必需：

- 视点问题与范围
- 带来源的对象、关系及定义

可选：

- 企业裁剪及例外说明

关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。

## 元素、属性与关系

对象类型：soa_concern, soa_layer。

```json
{
  "*": [
    "definition"
  ]
}
```

{
  "definition": {
    "meaning": "对象在本视点中的可检查定义",
    "value_rule": "使用可追溯描述；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `project:cross_cuts_soa` | soa_concern → soa_layer | 跨层关注覆盖 |
| `project:maps_to` | soa_layer → soa_layer | 层间映射 |

## 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

## 输出、检查与误读

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

- 关系端点及类型有效
- 专用拓扑检查通过
- 必要字段可追溯到实际输出

- 登记来源或成功生成不表示来源等价
- 参考示例的固定结构不直接强制所有企业采用


## 视图和交付物

- [SOA 分层参考](../profiles/soa-layered-reference.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-building-blocks](../deliverables/architecture-building-blocks.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "从所选对象删除必需的definition属性，保留其稳定ID及视图选择。",
    "expected": "missing-profile-attribute",
    "why": "缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。"
  },
  "modification_example": {
    "change": "修改同ID对象的definition，保持结构角色、类别和边界属性不变。",
    "expected": "reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G21I/fig5-3；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "layer-consumer-interface",
      "type": "soa_layer",
      "name": "消费者接口",
      "attributes": {
        "definition": "SOA 参考层：消费者接口",
        "layer": "consumer-interface"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "layer-business-process",
      "type": "soa_layer",
      "name": "业务流程",
      "attributes": {
        "definition": "SOA 参考层：业务流程",
        "layer": "business-process"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "layer-services",
      "type": "soa_layer",
      "name": "服务",
      "attributes": {
        "definition": "SOA 参考层：服务",
        "layer": "services"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "layer-service-component",
      "type": "soa_layer",
      "name": "服务组件",
      "attributes": {
        "definition": "SOA 参考层：服务组件",
        "layer": "service-component"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "layer-operational-systems",
      "type": "soa_layer",
      "name": "运营系统",
      "attributes": {
        "definition": "SOA 参考层：运营系统",
        "layer": "operational-systems"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "concern-integration",
      "type": "soa_concern",
      "name": "集成",
      "attributes": {
        "definition": "跨层关注：集成",
        "concern": "integration"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "concern-qos",
      "type": "soa_concern",
      "name": "服务质量",
      "attributes": {
        "definition": "跨层关注：服务质量",
        "concern": "qos"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "concern-information",
      "type": "soa_concern",
      "name": "信息",
      "attributes": {
        "definition": "跨层关注：信息",
        "concern": "information"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "concern-governance",
      "type": "soa_concern",
      "name": "治理",
      "attributes": {
        "definition": "跨层关注：治理",
        "concern": "governance"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "map-consumer-interface",
      "source": "layer-consumer-interface",
      "target": "layer-business-process",
      "type": "project:maps_to",
      "label": "层间映射",
      "attributes": {
        "meaning": "层间映射"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "map-business-process",
      "source": "layer-business-process",
      "target": "layer-services",
      "type": "project:maps_to",
      "label": "层间映射",
      "attributes": {
        "meaning": "层间映射"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "map-services",
      "source": "layer-services",
      "target": "layer-service-component",
      "type": "project:maps_to",
      "label": "层间映射",
      "attributes": {
        "meaning": "层间映射"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "map-service-component",
      "source": "layer-service-component",
      "target": "layer-operational-systems",
      "type": "project:maps_to",
      "label": "层间映射",
      "attributes": {
        "meaning": "层间映射"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-integration-consumer-interface",
      "source": "concern-integration",
      "target": "layer-consumer-interface",
      "type": "project:cross_cuts_soa",
      "label": "横切 集成",
      "attributes": {
        "meaning": "横切 集成"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-integration-business-process",
      "source": "concern-integration",
      "target": "layer-business-process",
      "type": "project:cross_cuts_soa",
      "label": "横切 集成",
      "attributes": {
        "meaning": "横切 集成"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-integration-services",
      "source": "concern-integration",
      "target": "layer-services",
      "type": "project:cross_cuts_soa",
      "label": "横切 集成",
      "attributes": {
        "meaning": "横切 集成"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-integration-service-component",
      "source": "concern-integration",
      "target": "layer-service-component",
      "type": "project:cross_cuts_soa",
      "label": "横切 集成",
      "attributes": {
        "meaning": "横切 集成"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-integration-operational-systems",
      "source": "concern-integration",
      "target": "layer-operational-systems",
      "type": "project:cross_cuts_soa",
      "label": "横切 集成",
      "attributes": {
        "meaning": "横切 集成"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-qos-consumer-interface",
      "source": "concern-qos",
      "target": "layer-consumer-interface",
      "type": "project:cross_cuts_soa",
      "label": "横切 服务质量",
      "attributes": {
        "meaning": "横切 服务质量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-qos-business-process",
      "source": "concern-qos",
      "target": "layer-business-process",
      "type": "project:cross_cuts_soa",
      "label": "横切 服务质量",
      "attributes": {
        "meaning": "横切 服务质量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-qos-services",
      "source": "concern-qos",
      "target": "layer-services",
      "type": "project:cross_cuts_soa",
      "label": "横切 服务质量",
      "attributes": {
        "meaning": "横切 服务质量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-qos-service-component",
      "source": "concern-qos",
      "target": "layer-service-component",
      "type": "project:cross_cuts_soa",
      "label": "横切 服务质量",
      "attributes": {
        "meaning": "横切 服务质量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-qos-operational-systems",
      "source": "concern-qos",
      "target": "layer-operational-systems",
      "type": "project:cross_cuts_soa",
      "label": "横切 服务质量",
      "attributes": {
        "meaning": "横切 服务质量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-information-consumer-interface",
      "source": "concern-information",
      "target": "layer-consumer-interface",
      "type": "project:cross_cuts_soa",
      "label": "横切 信息",
      "attributes": {
        "meaning": "横切 信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-information-business-process",
      "source": "concern-information",
      "target": "layer-business-process",
      "type": "project:cross_cuts_soa",
      "label": "横切 信息",
      "attributes": {
        "meaning": "横切 信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-information-services",
      "source": "concern-information",
      "target": "layer-services",
      "type": "project:cross_cuts_soa",
      "label": "横切 信息",
      "attributes": {
        "meaning": "横切 信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-information-service-component",
      "source": "concern-information",
      "target": "layer-service-component",
      "type": "project:cross_cuts_soa",
      "label": "横切 信息",
      "attributes": {
        "meaning": "横切 信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-information-operational-systems",
      "source": "concern-information",
      "target": "layer-operational-systems",
      "type": "project:cross_cuts_soa",
      "label": "横切 信息",
      "attributes": {
        "meaning": "横切 信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-governance-consumer-interface",
      "source": "concern-governance",
      "target": "layer-consumer-interface",
      "type": "project:cross_cuts_soa",
      "label": "横切 治理",
      "attributes": {
        "meaning": "横切 治理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-governance-business-process",
      "source": "concern-governance",
      "target": "layer-business-process",
      "type": "project:cross_cuts_soa",
      "label": "横切 治理",
      "attributes": {
        "meaning": "横切 治理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-governance-services",
      "source": "concern-governance",
      "target": "layer-services",
      "type": "project:cross_cuts_soa",
      "label": "横切 治理",
      "attributes": {
        "meaning": "横切 治理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-governance-service-component",
      "source": "concern-governance",
      "target": "layer-service-component",
      "type": "project:cross_cuts_soa",
      "label": "横切 治理",
      "attributes": {
        "meaning": "横切 治理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "x-governance-operational-systems",
      "source": "concern-governance",
      "target": "layer-operational-systems",
      "type": "project:cross_cuts_soa",
      "label": "横切 治理",
      "attributes": {
        "meaning": "横切 治理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:cross_cuts_soa": {
        "meaning": "跨层关注覆盖",
        "source_types": [
          "soa_concern"
        ],
        "target_types": [
          "soa_layer"
        ]
      },
      "project:maps_to": {
        "meaning": "层间映射",
        "source_types": [
          "soa_layer"
        ],
        "target_types": [
          "soa_layer"
        ]
      }
    }
  },
  "view": {
    "id": "v-soa-layered-reference",
    "artifact_id": "soa-layered-reference",
    "profile_id": "soa-layered-reference",
    "title": "SOA 分层参考／来源结构专用示例",
    "entity_ids": [
      "layer-consumer-interface",
      "layer-business-process",
      "layer-services",
      "layer-service-component",
      "layer-operational-systems",
      "concern-integration",
      "concern-qos",
      "concern-information",
      "concern-governance"
    ],
    "relationship_ids": [
      "map-consumer-interface",
      "map-business-process",
      "map-services",
      "map-service-component",
      "x-integration-consumer-interface",
      "x-integration-business-process",
      "x-integration-services",
      "x-integration-service-component",
      "x-integration-operational-systems",
      "x-qos-consumer-interface",
      "x-qos-business-process",
      "x-qos-services",
      "x-qos-service-component",
      "x-qos-operational-systems",
      "x-information-consumer-interface",
      "x-information-business-process",
      "x-information-services",
      "x-information-service-component",
      "x-information-operational-systems",
      "x-governance-consumer-interface",
      "x-governance-business-process",
      "x-governance-services",
      "x-governance-service-component",
      "x-governance-operational-systems"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact soa-layered-reference --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
