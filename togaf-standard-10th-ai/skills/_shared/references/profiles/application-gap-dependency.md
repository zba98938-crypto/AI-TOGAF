# 应用差距与迁移依赖

`profile_id`: application-gap-dependency；`artifact_id`: application-migration-diagram；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G233/fig7-2。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G233/fig7-2",
  "layout_notes": "应用与能力归属、显式差距、退役事件、交付物及定向集成；工作包依赖为项目补充，不从来源位置推导。",
  "review_status": "corrected-structure-awaiting-independent-review",
  "verification_evidence": "reviews/source-verification/application-gap-dependency.json",
  "semantic_layout": "application-change-topology",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, application, data_entity, gap, event, deliverable_component, work_package。关系类型：g233:integration_flow, addresses_gap, depends_on。

```json
{
  "entities": {
    "application": [
      "change_kind",
      "dependency"
    ],
    "gap": [
      "description"
    ],
    "event": [
      "event_kind"
    ],
    "work_package": [
      "output"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 新增、整合、退役、优化保留各自语义
- 退役事件不能替换为差距
- 应用数据副本具有独立ID和容器归属
- 工作包依赖必须为显式项目关系；不把来源图解释为甘特图

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
      "id": "application-gap-dependency-incentive",
      "type": "capability",
      "name": "客户激励管理",
      "attributes": {},
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-delivery",
      "type": "capability",
      "name": "交付管理",
      "attributes": {},
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-crm",
      "type": "application",
      "name": "客户关系管理",
      "attributes": {
        "change_kind": "retain",
        "dependency": "项目候选变更，须在执行前验证关联价值流",
        "parent_id": "application-gap-dependency-incentive"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "application-gap-dependency-crm-concept",
      "evolution": "baseline"
    },
    {
      "id": "application-gap-dependency-store",
      "type": "application",
      "name": "在线订单渠道",
      "attributes": {
        "change_kind": "create",
        "dependency": "项目候选变更，须在执行前验证关联价值流",
        "parent_id": "application-gap-dependency-incentive"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "application-gap-dependency-store-concept",
      "evolution": "target"
    },
    {
      "id": "application-gap-dependency-legacy",
      "type": "application",
      "name": "遗留工厂WMS",
      "attributes": {
        "change_kind": "retire",
        "dependency": "项目候选变更，须在执行前验证关联价值流"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "application-gap-dependency-legacy-concept",
      "evolution": "baseline"
    },
    {
      "id": "application-gap-dependency-modern",
      "type": "application",
      "name": "统一仓储应用",
      "attributes": {
        "change_kind": "consolidate",
        "dependency": "项目候选变更，须在执行前验证关联价值流"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "application-gap-dependency-modern-concept",
      "evolution": "target"
    },
    {
      "id": "application-gap-dependency-tracking",
      "type": "application",
      "name": "运输跟踪应用",
      "attributes": {
        "change_kind": "optimize",
        "dependency": "项目候选变更，须在执行前验证关联价值流",
        "parent_id": "application-gap-dependency-delivery"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "application-gap-dependency-tracking-concept",
      "evolution": "target"
    },
    {
      "id": "application-gap-dependency-promotion-crm",
      "type": "data_entity",
      "name": "促销数据（crm副本）",
      "attributes": {
        "parent_id": "application-gap-dependency-crm",
        "authority": "候选：CRM为权威，渠道为消费副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-promotion-store",
      "type": "data_entity",
      "name": "促销数据（store副本）",
      "attributes": {
        "parent_id": "application-gap-dependency-store",
        "authority": "候选：CRM为权威，渠道为消费副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-retire",
      "type": "event",
      "name": "退役应用事件",
      "attributes": {
        "event_kind": "retirement",
        "parent_id": "application-gap-dependency-legacy",
        "condition": "库存整合与所有受影响价值流验证后方可触发"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-signature",
      "type": "deliverable_component",
      "name": "电子签收终端",
      "attributes": {
        "parent_id": "application-gap-dependency-delivery",
        "output": "签收记录回传"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-api-gap",
      "type": "gap",
      "name": "新增渠道到CRM集成",
      "attributes": {
        "parent_id": "application-gap-dependency-incentive",
        "description": "新增渠道到CRM集成；差距尚未弥合"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-inventory-gap",
      "type": "gap",
      "name": "并入遗留仓库库存",
      "attributes": {
        "parent_id": "application-gap-dependency-modern",
        "description": "并入遗留仓库库存；差距尚未弥合"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-signature-gap",
      "type": "gap",
      "name": "签收应用增强",
      "attributes": {
        "parent_id": "application-gap-dependency-signature",
        "description": "签收应用增强；差距尚未弥合"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-integrate",
      "type": "work_package",
      "name": "整合库存与接口",
      "attributes": {
        "output": "可回退库存迁移与接口验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-retire-wp",
      "type": "work_package",
      "name": "受控退役遗留仓储",
      "attributes": {
        "output": "退役事件及所有受影响价值流验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "application-gap-dependency-api",
      "source": "application-gap-dependency-store",
      "target": "application-gap-dependency-crm",
      "type": "g233:integration_flow",
      "label": "新增API调用；渠道→CRM",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-signature-flow",
      "source": "application-gap-dependency-signature",
      "target": "application-gap-dependency-tracking",
      "type": "g233:integration_flow",
      "label": "签收数据回传；交付物→运输应用",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-inventory-work",
      "source": "application-gap-dependency-integrate",
      "target": "application-gap-dependency-inventory-gap",
      "type": "addresses_gap",
      "label": "工作包处理库存整合差距",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-api-work",
      "source": "application-gap-dependency-integrate",
      "target": "application-gap-dependency-api-gap",
      "type": "addresses_gap",
      "label": "工作包处理接口差距",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-gap-dependency-retire-dependency",
      "source": "application-gap-dependency-retire-wp",
      "target": "application-gap-dependency-integrate",
      "type": "depends_on",
      "label": "项目约定：受控退役以整合验证完成为前置",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-application-gap-dependency",
    "artifact_id": "application-migration-diagram",
    "profile_id": "application-gap-dependency",
    "title": "应用差距与迁移依赖／虚构案例",
    "entity_ids": [
      "application-gap-dependency-incentive",
      "application-gap-dependency-delivery",
      "application-gap-dependency-crm",
      "application-gap-dependency-store",
      "application-gap-dependency-legacy",
      "application-gap-dependency-modern",
      "application-gap-dependency-tracking",
      "application-gap-dependency-promotion-crm",
      "application-gap-dependency-promotion-store",
      "application-gap-dependency-retire",
      "application-gap-dependency-signature",
      "application-gap-dependency-api-gap",
      "application-gap-dependency-inventory-gap",
      "application-gap-dependency-signature-gap",
      "application-gap-dependency-integrate",
      "application-gap-dependency-retire-wp"
    ],
    "relationship_ids": [
      "application-gap-dependency-api",
      "application-gap-dependency-signature-flow",
      "application-gap-dependency-inventory-work",
      "application-gap-dependency-api-work",
      "application-gap-dependency-retire-dependency"
    ],
    "analysis": "对照G233图7-2的变化结构，保留新增接口、库存整合、退役事件和签收增强；新增工作包依赖是明确声明的项目规则，并非图中已有连线。",
    "legend": "青色应用；绿色波浪标识差距；粉色事件表示退役；绿色带底座为交付物。工作包及其依赖为项目补充。",
    "allow_mixed_evolution": true
  },
  "extensions": {
    "relationship_types": {
      "g233:integration_flow": {
        "source_types": [
          "application",
          "deliverable_component"
        ],
        "target_types": [
          "application"
        ],
        "meaning": "项目记录的定向API调用或数据回传；调用者/发送者到接收应用，不表示依赖排期"
      }
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile application-gap-dependency --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile application-gap-dependency --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
