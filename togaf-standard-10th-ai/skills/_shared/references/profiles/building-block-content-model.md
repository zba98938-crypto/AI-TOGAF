# 构建块内容元模型

`profile_id`: building-block-content-model；`artifact_id`: building-block-description；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G248/fig3-1。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.3。

{
  "source_verified": false,
  "source_figure": "G248/fig3-1",
  "layout_notes": "视觉包含不自动成为组成，逻辑物理与ABB/SBB实现分开",
  "review_status": "source-topology-repaired-awaiting-independent-review",
  "source_topology": "content-metamodel",
  "version": "2.3",
  "full_source_concepts": [
    "actor",
    "application_service",
    "assumption",
    "business_capability",
    "business_information",
    "business_service",
    "capability_general",
    "constraint",
    "contract",
    "control",
    "course_of_action",
    "data_entity",
    "driver",
    "event",
    "function",
    "gap",
    "goal",
    "location",
    "logical_application_component",
    "logical_data_component",
    "logical_technology_component",
    "measure",
    "objective",
    "organization_unit",
    "physical_application_component",
    "physical_data_component",
    "physical_technology_component",
    "principle",
    "process",
    "product",
    "requirement",
    "role",
    "service_quality",
    "technology_service",
    "value_stream",
    "work_package"
  ]
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:metamodel_entity。关系类型：guide:metamodel_relation。

```json
{
  "entities": {
    "*": [
      "definition"
    ]
  },
  "relationships": {
    "*": [
      "meaning",
      "forward_label",
      "inverse_label",
      "notation"
    ]
  }
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 视觉包含不自动成为组成，逻辑物理与ABB/SBB实现分开

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G248/fig3-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "principle",
      "type": "guide:metamodel_entity",
      "name": "原则 / Principle",
      "attributes": {
        "definition": "实体类型：原则",
        "source_concept": "principle",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "constraint",
      "type": "guide:metamodel_entity",
      "name": "约束 / Constraint",
      "attributes": {
        "definition": "实体类型：约束",
        "source_concept": "constraint",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assumption",
      "type": "guide:metamodel_entity",
      "name": "假设 / Assumption",
      "attributes": {
        "definition": "实体类型：假设",
        "source_concept": "assumption",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "requirement",
      "type": "guide:metamodel_entity",
      "name": "需求 / Requirement",
      "attributes": {
        "definition": "实体类型：需求",
        "source_concept": "requirement",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "location",
      "type": "guide:metamodel_entity",
      "name": "位置 / Location",
      "attributes": {
        "definition": "实体类型：位置",
        "source_concept": "location",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "gap",
      "type": "guide:metamodel_entity",
      "name": "差距 / Gap",
      "attributes": {
        "definition": "实体类型：差距",
        "source_concept": "gap",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "work_package",
      "type": "guide:metamodel_entity",
      "name": "工作包 / Work Package",
      "attributes": {
        "definition": "实体类型：工作包",
        "source_concept": "work_package",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability_general",
      "type": "guide:metamodel_entity",
      "name": "能力 / Capability",
      "attributes": {
        "definition": "实体类型：能力",
        "source_concept": "capability_general",
        "domain": "general",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "driver",
      "type": "guide:metamodel_entity",
      "name": "驱动因素 / Driver",
      "attributes": {
        "definition": "实体类型：驱动因素",
        "source_concept": "driver",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "goal",
      "type": "guide:metamodel_entity",
      "name": "目标 / Goal",
      "attributes": {
        "definition": "实体类型：目标",
        "source_concept": "goal",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "objective",
      "type": "guide:metamodel_entity",
      "name": "目的 / Objective",
      "attributes": {
        "definition": "实体类型：目的",
        "source_concept": "objective",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "measure",
      "type": "guide:metamodel_entity",
      "name": "度量 / Measure",
      "attributes": {
        "definition": "实体类型：度量",
        "source_concept": "measure",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "course_of_action",
      "type": "guide:metamodel_entity",
      "name": "行动方案 / Course of Action",
      "attributes": {
        "definition": "实体类型：行动方案",
        "source_concept": "course_of_action",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "product",
      "type": "guide:metamodel_entity",
      "name": "产品 / Product",
      "attributes": {
        "definition": "实体类型：产品",
        "source_concept": "product",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "organization_unit",
      "type": "guide:metamodel_entity",
      "name": "组织单元 / Organization Unit",
      "attributes": {
        "definition": "实体类型：组织单元",
        "source_concept": "organization_unit",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business_capability",
      "type": "guide:metamodel_entity",
      "name": "业务能力 / Business Capability",
      "attributes": {
        "definition": "实体类型：业务能力",
        "source_concept": "business_capability",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value_stream",
      "type": "guide:metamodel_entity",
      "name": "价值流 / Value Stream",
      "attributes": {
        "definition": "实体类型：价值流",
        "source_concept": "value_stream",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business_information",
      "type": "guide:metamodel_entity",
      "name": "业务信息 / Business Information",
      "attributes": {
        "definition": "实体类型：业务信息",
        "source_concept": "business_information",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "function",
      "type": "guide:metamodel_entity",
      "name": "功能 / Function",
      "attributes": {
        "definition": "实体类型：功能",
        "source_concept": "function",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "actor",
      "type": "guide:metamodel_entity",
      "name": "参与者 / Actor",
      "attributes": {
        "definition": "实体类型：参与者",
        "source_concept": "actor",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "process",
      "type": "guide:metamodel_entity",
      "name": "流程 / Process",
      "attributes": {
        "definition": "实体类型：流程",
        "source_concept": "process",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "role",
      "type": "guide:metamodel_entity",
      "name": "角色 / Role",
      "attributes": {
        "definition": "实体类型：角色",
        "source_concept": "role",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "event",
      "type": "guide:metamodel_entity",
      "name": "事件 / Event",
      "attributes": {
        "definition": "实体类型：事件",
        "source_concept": "event",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "service_quality",
      "type": "guide:metamodel_entity",
      "name": "服务质量 / Service Quality",
      "attributes": {
        "definition": "实体类型：服务质量",
        "source_concept": "service_quality",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contract",
      "type": "guide:metamodel_entity",
      "name": "合同 / Contract",
      "attributes": {
        "definition": "实体类型：合同",
        "source_concept": "contract",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "control",
      "type": "guide:metamodel_entity",
      "name": "控制 / Control",
      "attributes": {
        "definition": "实体类型：控制",
        "source_concept": "control",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business_service",
      "type": "guide:metamodel_entity",
      "name": "业务服务 / Business Service",
      "attributes": {
        "definition": "实体类型：业务服务",
        "source_concept": "business_service",
        "domain": "business",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data_entity",
      "type": "guide:metamodel_entity",
      "name": "数据实体 / Data Entity",
      "attributes": {
        "definition": "实体类型：数据实体",
        "source_concept": "data_entity",
        "domain": "data",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "logical_data_component",
      "type": "guide:metamodel_entity",
      "name": "逻辑数据组件 / Logical Data Component",
      "attributes": {
        "definition": "实体类型：逻辑数据组件",
        "source_concept": "logical_data_component",
        "domain": "data",
        "abstraction": "logical",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "physical_data_component",
      "type": "guide:metamodel_entity",
      "name": "物理数据组件 / Physical Data Component",
      "attributes": {
        "definition": "实体类型：物理数据组件",
        "source_concept": "physical_data_component",
        "domain": "data",
        "abstraction": "physical",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application_service",
      "type": "guide:metamodel_entity",
      "name": "应用服务 / Application Service",
      "attributes": {
        "definition": "实体类型：应用服务",
        "source_concept": "application_service",
        "domain": "application",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "logical_application_component",
      "type": "guide:metamodel_entity",
      "name": "逻辑应用组件 / Logical Application Component",
      "attributes": {
        "definition": "实体类型：逻辑应用组件",
        "source_concept": "logical_application_component",
        "domain": "application",
        "abstraction": "logical",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "physical_application_component",
      "type": "guide:metamodel_entity",
      "name": "物理应用组件 / Physical Application Component",
      "attributes": {
        "definition": "实体类型：物理应用组件",
        "source_concept": "physical_application_component",
        "domain": "application",
        "abstraction": "physical",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "technology_service",
      "type": "guide:metamodel_entity",
      "name": "技术服务 / Technology Service",
      "attributes": {
        "definition": "实体类型：技术服务",
        "source_concept": "technology_service",
        "domain": "technology",
        "abstraction": "type",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "logical_technology_component",
      "type": "guide:metamodel_entity",
      "name": "逻辑技术组件 / Logical Technology Component",
      "attributes": {
        "definition": "实体类型：逻辑技术组件",
        "source_concept": "logical_technology_component",
        "domain": "technology",
        "abstraction": "logical",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "physical_technology_component",
      "type": "guide:metamodel_entity",
      "name": "物理技术组件 / Physical Technology Component",
      "attributes": {
        "definition": "实体类型：物理技术组件",
        "source_concept": "physical_technology_component",
        "domain": "technology",
        "abstraction": "physical",
        "model_kind": "entity-type",
        "associated_with_all": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "r_wp_capability",
      "source": "work_package",
      "target": "capability_general",
      "type": "guide:metamodel_relation",
      "label": "交付 / 由……交付",
      "attributes": {
        "forward_label": "Delivers",
        "inverse_label": "Is delivered by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "produces",
        "meaning": "交付 / 由……交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_driver_goal",
      "source": "driver",
      "target": "goal",
      "type": "guide:metamodel_relation",
      "label": "创建 / 应对",
      "attributes": {
        "forward_label": "Creates",
        "inverse_label": "Addresses",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "produces",
        "meaning": "创建 / 应对"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_driver_coa",
      "source": "driver",
      "target": "course_of_action",
      "type": "guide:metamodel_relation",
      "label": "激励",
      "attributes": {
        "forward_label": "Motivates",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "激励"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_goal_objective",
      "source": "goal",
      "target": "objective",
      "type": "guide:metamodel_relation",
      "label": "被具体化 / 实现",
      "attributes": {
        "forward_label": "Is made specific",
        "inverse_label": "Realizes",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "association",
        "meaning": "被具体化 / 实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_goal_coa",
      "source": "goal",
      "target": "course_of_action",
      "type": "guide:metamodel_relation",
      "label": "由……实现 / 实现",
      "attributes": {
        "forward_label": "Is realized by",
        "inverse_label": "Realizes",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "由……实现 / 实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_objective_measure",
      "source": "objective",
      "target": "measure",
      "type": "guide:metamodel_relation",
      "label": "对照……跟踪 / 为……设定绩效标准",
      "attributes": {
        "forward_label": "Is tracked against",
        "inverse_label": "Sets performance criteria for",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "association",
        "meaning": "对照……跟踪 / 为……设定绩效标准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_product",
      "source": "course_of_action",
      "target": "product",
      "type": "guide:metamodel_relation",
      "label": "影响",
      "attributes": {
        "forward_label": "Influences",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "影响"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_orgunit",
      "source": "course_of_action",
      "target": "organization_unit",
      "type": "guide:metamodel_relation",
      "label": "影响",
      "attributes": {
        "forward_label": "Influences",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "影响"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_orgunit_motivates",
      "source": "course_of_action",
      "target": "organization_unit",
      "type": "guide:metamodel_relation",
      "label": "激励 / 受……激励",
      "attributes": {
        "forward_label": "Motivates",
        "inverse_label": "Is motivated by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "激励 / 受……激励"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_capability",
      "source": "course_of_action",
      "target": "business_capability",
      "type": "guide:metamodel_relation",
      "label": "影响",
      "attributes": {
        "forward_label": "Influences",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "影响"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_valuestream",
      "source": "course_of_action",
      "target": "value_stream",
      "type": "guide:metamodel_relation",
      "label": "影响",
      "attributes": {
        "forward_label": "Influences",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "影响"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_businessinfo",
      "source": "course_of_action",
      "target": "business_information",
      "type": "guide:metamodel_relation",
      "label": "影响",
      "attributes": {
        "forward_label": "Influences",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "影响"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_coa_function",
      "source": "course_of_action",
      "target": "function",
      "type": "guide:metamodel_relation",
      "label": "影响 / 受……影响",
      "attributes": {
        "forward_label": "Influences",
        "inverse_label": "Is influenced by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "influence",
        "meaning": "影响 / 受……影响"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_product_orgunit",
      "source": "organization_unit",
      "target": "product",
      "type": "guide:metamodel_relation",
      "label": "由……生产 / 交付",
      "attributes": {
        "forward_label": "Is produced by",
        "inverse_label": "Delivers",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "produces",
        "meaning": "由……生产 / 交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_product_function",
      "source": "function",
      "target": "product",
      "type": "guide:metamodel_relation",
      "label": "由……生产 / 交付",
      "attributes": {
        "forward_label": "Is produced by",
        "inverse_label": "Delivers",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "produces",
        "meaning": "由……生产 / 交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_orgunit_actor",
      "source": "organization_unit",
      "target": "actor",
      "type": "guide:metamodel_relation",
      "label": "包含",
      "attributes": {
        "forward_label": "Contains",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "composition",
        "meaning": "包含"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_orgunit_function",
      "source": "organization_unit",
      "target": "function",
      "type": "guide:metamodel_relation",
      "label": "拥有并治理 / 由……拥有",
      "attributes": {
        "forward_label": "Owns and governs",
        "inverse_label": "Is owned by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "governs",
        "meaning": "拥有并治理 / 由……拥有"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_function_orgunit_owned",
      "source": "function",
      "target": "organization_unit",
      "type": "guide:metamodel_relation",
      "label": "由……拥有并治理",
      "attributes": {
        "forward_label": "Is owned and governed by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "dependency",
        "meaning": "由……拥有并治理"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_orgunit_capability",
      "source": "organization_unit",
      "target": "business_capability",
      "type": "guide:metamodel_relation",
      "label": "使能",
      "attributes": {
        "forward_label": "Enables",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "serving",
        "meaning": "使能"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_orgunit_process",
      "source": "organization_unit",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "参与",
      "attributes": {
        "forward_label": "Participates in",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "association",
        "meaning": "参与"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_capability_valuestream",
      "source": "business_capability",
      "target": "value_stream",
      "type": "guide:metamodel_relation",
      "label": "使能 / 受……使能",
      "attributes": {
        "forward_label": "Enables",
        "inverse_label": "Is enabled by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "使能 / 受……使能"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_capability_process",
      "source": "business_capability",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "由……运营化 / 运营化",
      "attributes": {
        "forward_label": "Is operationalized by",
        "inverse_label": "Operationalizes",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "association",
        "meaning": "由……运营化 / 运营化"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_valuestream_capability",
      "source": "value_stream",
      "target": "business_capability",
      "type": "guide:metamodel_relation",
      "label": "由……运营化",
      "attributes": {
        "forward_label": "Is operationalized by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "association",
        "meaning": "由……运营化"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_valuestream_process",
      "source": "value_stream",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "由……触发、涉及",
      "attributes": {
        "forward_label": "Is triggered by, Involves",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "association",
        "meaning": "由……触发、涉及"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_businessinfo_process",
      "source": "process",
      "target": "business_information",
      "type": "guide:metamodel_relation",
      "label": "使用 / 被……使用",
      "attributes": {
        "forward_label": "Uses",
        "inverse_label": "Is used by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "access",
        "meaning": "使用 / 被……使用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_businessinfo_service",
      "source": "business_information",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "用于派生 / 派生自",
      "attributes": {
        "forward_label": "Used to derive",
        "inverse_label": "Is derived from",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "produces",
        "meaning": "用于派生 / 派生自"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_process_service",
      "source": "process",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "交付",
      "attributes": {
        "forward_label": "Delivers",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "produces",
        "meaning": "交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_function_capability",
      "source": "function",
      "target": "business_capability",
      "type": "guide:metamodel_relation",
      "label": "支持",
      "attributes": {
        "forward_label": "Supports",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "支持"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_capability_function",
      "source": "business_capability",
      "target": "function",
      "type": "guide:metamodel_relation",
      "label": "由……实现",
      "attributes": {
        "forward_label": "Is realized by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "由……实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_function_actor",
      "source": "function",
      "target": "actor",
      "type": "guide:metamodel_relation",
      "label": "与……交互、执行",
      "attributes": {
        "forward_label": "Interacts with, Performs",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "endpoint-inferred-awaiting-review",
        "source_relation_kind": "association",
        "meaning": "与……交互、执行"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_function_service_interface",
      "source": "function",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "提供受治理的访问接口",
      "attributes": {
        "forward_label": "Provides governed interface to access",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "提供受治理的访问接口"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_function_service_supply",
      "source": "function",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "供应或消费 / 被供应或消费",
      "attributes": {
        "forward_label": "Supplies or consumes",
        "inverse_label": "Is supplied or consumed by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "consumes",
        "meaning": "供应或消费 / 被供应或消费"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_function_coa",
      "source": "function",
      "target": "course_of_action",
      "type": "guide:metamodel_relation",
      "label": "受……约束",
      "attributes": {
        "forward_label": "Is bounded by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "dependency",
        "meaning": "受……约束"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_actor_orgunit",
      "source": "actor",
      "target": "organization_unit",
      "type": "guide:metamodel_relation",
      "label": "隶属于",
      "attributes": {
        "forward_label": "Belongs to",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "assignment",
        "meaning": "隶属于"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_actor_service",
      "source": "actor",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "消费",
      "attributes": {
        "forward_label": "Consumes",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "consumes",
        "meaning": "消费"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_actor_process_task",
      "source": "actor",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "在其中执行任务 / 在……中执行任务",
      "attributes": {
        "forward_label": "Performs a task in",
        "inverse_label": "Performs task in",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "assignment",
        "meaning": "在其中执行任务 / 在……中执行任务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_actor_process_trigger",
      "source": "actor",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "触发、参与",
      "attributes": {
        "forward_label": "Triggers, Participates in",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "association",
        "meaning": "触发、参与"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_process_process",
      "source": "process",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "编排、分解",
      "attributes": {
        "forward_label": "Orchestrates, Decomposes",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "composition",
        "meaning": "编排、分解"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_role_process",
      "source": "role",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "执行、参与",
      "attributes": {
        "forward_label": "Performs, Participates in",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "assignment",
        "meaning": "执行、参与"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_process_role",
      "source": "process",
      "target": "role",
      "type": "guide:metamodel_relation",
      "label": "由……执行、涉及",
      "attributes": {
        "forward_label": "Is performed by, Involves",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "assignment",
        "meaning": "由……执行、涉及"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_process_event",
      "source": "process",
      "target": "event",
      "type": "guide:metamodel_relation",
      "label": "生成、解决",
      "attributes": {
        "forward_label": "Generates, Resolves",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "produces",
        "meaning": "生成、解决"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_event_process",
      "source": "event",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "由……解决、由……生成",
      "attributes": {
        "forward_label": "Is resolved by, Is generated by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "association",
        "meaning": "由……解决、由……生成"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_process_service_support",
      "source": "process",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "支持、由……实现",
      "attributes": {
        "forward_label": "Supports, Is realized by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "支持、由……实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_control_process",
      "source": "control",
      "target": "process",
      "type": "guide:metamodel_relation",
      "label": "确保……正确运行",
      "attributes": {
        "forward_label": "Ensures correct operation of",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "governs",
        "meaning": "确保……正确运行"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_process_control",
      "source": "process",
      "target": "control",
      "type": "guide:metamodel_relation",
      "label": "受……指导",
      "attributes": {
        "forward_label": "Is guided by",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "dependency",
        "meaning": "受……指导"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_quality_contract",
      "source": "service_quality",
      "target": "contract",
      "type": "guide:metamodel_relation",
      "label": "适用于 / 满足",
      "attributes": {
        "forward_label": "Applies to",
        "inverse_label": "Meets",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "association",
        "meaning": "适用于 / 满足"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_contract_service",
      "source": "contract",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "治理、度量 / 受……治理与度量",
      "attributes": {
        "forward_label": "Governs, measures",
        "inverse_label": "Is governed and measured by",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "governs",
        "meaning": "治理、度量 / 受……治理与度量"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_quality_service",
      "source": "service_quality",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "适用于 / 满足",
      "attributes": {
        "forward_label": "Applies to",
        "inverse_label": "Meets",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "association",
        "meaning": "适用于 / 满足"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_service_actor",
      "source": "business_service",
      "target": "actor",
      "type": "guide:metamodel_relation",
      "label": "被提供给",
      "attributes": {
        "forward_label": "Is provided to",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "被提供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_data_service",
      "source": "data_entity",
      "target": "business_service",
      "type": "guide:metamodel_relation",
      "label": "实现",
      "attributes": {
        "forward_label": "Realizes",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_service_app",
      "source": "business_service",
      "target": "application_service",
      "type": "guide:metamodel_relation",
      "label": "使用 / 自动化其中部分或全部",
      "attributes": {
        "forward_label": "Uses",
        "inverse_label": "Automates some or all of",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "consumes",
        "meaning": "使用 / 自动化其中部分或全部"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_data_ldc",
      "source": "data_entity",
      "target": "logical_data_component",
      "type": "guide:metamodel_relation",
      "label": "驻留于 / 封装",
      "attributes": {
        "forward_label": "Resides within",
        "inverse_label": "Encapsulates",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "composition",
        "meaning": "驻留于 / 封装"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_ldc_pdc",
      "source": "logical_data_component",
      "target": "physical_data_component",
      "type": "guide:metamodel_relation",
      "label": "由……实现 / 实现",
      "attributes": {
        "forward_label": "Is realized by",
        "inverse_label": "Realizes",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "由……实现 / 实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_data_appservice",
      "source": "data_entity",
      "target": "application_service",
      "type": "guide:metamodel_relation",
      "label": "通过……访问与更新",
      "attributes": {
        "forward_label": "Is accessed and updated through",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "access",
        "meaning": "通过……访问与更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_data_lac",
      "source": "data_entity",
      "target": "logical_application_component",
      "type": "guide:metamodel_relation",
      "label": "被……使用 / 使用",
      "attributes": {
        "forward_label": "Used by",
        "inverse_label": "Uses",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "access",
        "meaning": "被……使用 / 使用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_data_pac",
      "source": "data_entity",
      "target": "physical_application_component",
      "type": "guide:metamodel_relation",
      "label": "被……使用 / 使用",
      "attributes": {
        "forward_label": "Used by",
        "inverse_label": "Uses",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "access",
        "meaning": "被……使用 / 使用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_appservice_lac",
      "source": "application_service",
      "target": "logical_application_component",
      "type": "guide:metamodel_relation",
      "label": "通过……实现 / 实现",
      "attributes": {
        "forward_label": "Is realized through",
        "inverse_label": "Implements",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "通过……实现 / 实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_lac_pac",
      "source": "logical_application_component",
      "target": "physical_application_component",
      "type": "guide:metamodel_relation",
      "label": "由……实现 / 实现",
      "attributes": {
        "forward_label": "Is realized by",
        "inverse_label": "Realizes",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "由……实现 / 实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_appservice_techservice",
      "source": "application_service",
      "target": "technology_service",
      "type": "guide:metamodel_relation",
      "label": "由……服务 / 服务",
      "attributes": {
        "forward_label": "Is served by",
        "inverse_label": "Serves",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "由……服务 / 服务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_lac_ltc",
      "source": "logical_application_component",
      "target": "logical_technology_component",
      "type": "guide:metamodel_relation",
      "label": "由……服务 / 服务",
      "attributes": {
        "forward_label": "Is served by",
        "inverse_label": "Serves",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "由……服务 / 服务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_pac_ptc",
      "source": "physical_application_component",
      "target": "physical_technology_component",
      "type": "guide:metamodel_relation",
      "label": "由……服务 / 服务",
      "attributes": {
        "forward_label": "Is served by",
        "inverse_label": "Serves",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "由……服务 / 服务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_appservice_techservice_impl",
      "source": "application_service",
      "target": "technology_service",
      "type": "guide:metamodel_relation",
      "label": "实现在……之上",
      "attributes": {
        "forward_label": "Is implemented on",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "dependency",
        "meaning": "实现在……之上"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_ltc_techservice",
      "source": "logical_technology_component",
      "target": "technology_service",
      "type": "guide:metamodel_relation",
      "label": "由……供应 / 供应",
      "attributes": {
        "forward_label": "Is supplied by",
        "inverse_label": "Supplies",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "由……供应 / 供应"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_ltc_ptc",
      "source": "logical_technology_component",
      "target": "physical_technology_component",
      "type": "guide:metamodel_relation",
      "label": "由……实现 / 实现",
      "attributes": {
        "forward_label": "Is realized by",
        "inverse_label": "Realizes",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "realization",
        "meaning": "由……实现 / 实现"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r_ltc_appservice",
      "source": "logical_technology_component",
      "target": "application_service",
      "type": "guide:metamodel_relation",
      "label": "为……提供平台",
      "attributes": {
        "forward_label": "Provides platform for",
        "inverse_label": "来源未单列反向标签（不推断）",
        "notation": "unarrowed",
        "interpretation_status": "source-label-interpreted",
        "source_relation_kind": "serving",
        "meaning": "为……提供平台"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "entity_types": {
      "guide:metamodel_entity": "来源元模型的实体类型，非企业实例；原类型名称保存在source_concept"
    },
    "relationship_types": {
      "guide:metamodel_relation": {
        "source_types": [
          "guide:metamodel_entity"
        ],
        "target_types": [
          "guide:metamodel_entity"
        ],
        "meaning": "无箭头的来源元模型关联；正反读法与解释状态显式保留，不将几何方向当作业务方向。"
      }
    }
  },
  "view": {
    "id": "v-building-block-content-model",
    "artifact_id": "building-block-description",
    "profile_id": "building-block-content-model",
    "title": "构建块内容元模型／来源结构专用示例",
    "entity_ids": [
      "principle",
      "constraint",
      "assumption",
      "requirement",
      "location",
      "gap",
      "work_package",
      "capability_general",
      "driver",
      "goal",
      "objective",
      "measure",
      "course_of_action",
      "product",
      "organization_unit",
      "business_capability",
      "value_stream",
      "business_information",
      "function",
      "actor",
      "process",
      "role",
      "event",
      "service_quality",
      "contract",
      "control",
      "business_service",
      "data_entity",
      "logical_data_component",
      "physical_data_component",
      "application_service",
      "logical_application_component",
      "physical_application_component",
      "technology_service",
      "logical_technology_component",
      "physical_technology_component"
    ],
    "relationship_ids": [
      "r_wp_capability",
      "r_driver_goal",
      "r_driver_coa",
      "r_goal_objective",
      "r_goal_coa",
      "r_objective_measure",
      "r_coa_product",
      "r_coa_orgunit",
      "r_coa_orgunit_motivates",
      "r_coa_capability",
      "r_coa_valuestream",
      "r_coa_businessinfo",
      "r_coa_function",
      "r_product_orgunit",
      "r_product_function",
      "r_orgunit_actor",
      "r_orgunit_function",
      "r_function_orgunit_owned",
      "r_orgunit_capability",
      "r_orgunit_process",
      "r_capability_valuestream",
      "r_capability_process",
      "r_valuestream_capability",
      "r_valuestream_process",
      "r_businessinfo_process",
      "r_businessinfo_service",
      "r_process_service",
      "r_function_capability",
      "r_capability_function",
      "r_function_actor",
      "r_function_service_interface",
      "r_function_service_supply",
      "r_function_coa",
      "r_actor_orgunit",
      "r_actor_service",
      "r_actor_process_task",
      "r_actor_process_trigger",
      "r_process_process",
      "r_role_process",
      "r_process_role",
      "r_process_event",
      "r_event_process",
      "r_process_service_support",
      "r_control_process",
      "r_process_control",
      "r_quality_contract",
      "r_contract_service",
      "r_quality_service",
      "r_service_actor",
      "r_data_service",
      "r_service_app",
      "r_data_ldc",
      "r_ldc_pdc",
      "r_data_appservice",
      "r_data_lac",
      "r_data_pac",
      "r_appservice_lac",
      "r_lac_pac",
      "r_appservice_techservice",
      "r_lac_ltc",
      "r_pac_ptc",
      "r_appservice_techservice_impl",
      "r_ltc_techservice",
      "r_ltc_ptc",
      "r_ltc_appservice"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。按专用线型、区域与编号语义读取；工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile building-block-content-model --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile building-block-content-model --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
