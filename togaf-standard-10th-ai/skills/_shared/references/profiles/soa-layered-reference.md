# SOA 分层参考

`profile_id`: soa-layered-reference；`artifact_id`: soa-layered-reference；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G21I/fig5-3。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "soa-layered-reference",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G21I/fig5-3",
  "source_topology": "soa-layered",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "五层加四种跨层关注点"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：soa_concern, soa_layer。关系类型：project:cross_cuts_soa, project:maps_to。

```json
{
  "entities": {
    "*": [
      "definition"
    ]
  },
  "relationships": {
    "*": [
      "meaning"
    ]
  }
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 五层加四种跨层关注点
- 参考层按用途裁剪，不要求机械复制

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile soa-layered-reference --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile soa-layered-reference --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
