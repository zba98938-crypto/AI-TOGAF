# MSA源、部署与执行单元追溯表

`profile_id`: msa-source-deployment-execution；`artifact_id`: software-distribution-diagram；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G21I §9.1–9.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "msa-source-deployment-execution",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。",
  "coverage_notice": "表或派生部署图不等于原图视觉验收。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:msa_unit。关系类型：guide:uses_neutral_library, guide:builds_deployment, guide:deploys_instance。

```json
{
  "entities": {
    "guide:msa_unit": [
      "unit_kind",
      "service_id",
      "function",
      "included_business_services",
      "libraries",
      "environment",
      "instances",
      "operating_condition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 部署单元不得包含多个微服务代码
- 公共库必须无业务逻辑
- 多实例复用同部署包ID
- 部署端点角色与关系方向一致

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/msa-source-deployment-execution/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/msa-source-deployment-execution/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构资格服务有独立源单元；可复用不含业务逻辑的脱敏日志库。单一部署包只包含资格服务代码，分别在节点A/B运行同代码实例，数据有效且健康后接流量；没有把两个服务打成一个部署包。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MSU-S",
      "type": "guide:msa_unit",
      "name": "资格源单元",
      "attributes": {
        "unit_kind": "source",
        "service_id": "MS-eligibility",
        "function": "实现借阅资格ABF",
        "included_business_services": [
          "MS-eligibility"
        ],
        "libraries": [
          "LIB-log"
        ],
        "environment": "源码库",
        "instances": "not-applicable",
        "operating_condition": "不含其他微服务业务代码或直接访问其数据"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "LIB-log",
      "type": "guide:msa_unit",
      "name": "通用日志库",
      "attributes": {
        "unit_kind": "library",
        "service_id": "business-neutral",
        "function": "通用脱敏日志格式化，无借阅规则",
        "included_business_services": [],
        "libraries": [],
        "environment": "共享基础库",
        "instances": "not-applicable",
        "operating_condition": "只有无业务功能库可被多个源单元复用"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MSU-D",
      "type": "guide:msa_unit",
      "name": "资格部署包",
      "attributes": {
        "unit_kind": "deployment",
        "service_id": "MS-eligibility",
        "function": "由资格源单元和日志库构建",
        "included_business_services": [
          "MS-eligibility"
        ],
        "libraries": [
          "LIB-log"
        ],
        "environment": "候选制品仓库",
        "instances": "one-deployment-unit",
        "operating_condition": "不混入其他微服务代码；独立测试/部署"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MSU-E1",
      "type": "guide:msa_unit",
      "name": "资格运行实例A",
      "attributes": {
        "unit_kind": "execution",
        "service_id": "MS-eligibility",
        "function": "执行同一资格部署包",
        "included_business_services": [
          "MS-eligibility"
        ],
        "libraries": [],
        "environment": "试点节点A",
        "instances": 1,
        "operating_condition": "接收健康检查；失败时由另一同代码实例接管"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MSU-E2",
      "type": "guide:msa_unit",
      "name": "资格运行实例B",
      "attributes": {
        "unit_kind": "execution",
        "service_id": "MS-eligibility",
        "function": "执行同一资格部署包",
        "included_business_services": [
          "MS-eligibility"
        ],
        "libraries": [],
        "environment": "试点节点B",
        "instances": 1,
        "operating_condition": "与A同代码；副本数据有效后才接流量"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [
    {
      "id": "MSR-lib",
      "type": "guide:uses_neutral_library",
      "source": "MSU-S",
      "target": "LIB-log",
      "label": "使用无业务日志库",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "MSR-build",
      "type": "guide:builds_deployment",
      "source": "MSU-S",
      "target": "MSU-D",
      "label": "构建一个独立资格服务包",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "MSR-A",
      "type": "guide:deploys_instance",
      "source": "MSU-D",
      "target": "MSU-E1",
      "label": "部署同代码实例A",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "MSR-B",
      "type": "guide:deploys_instance",
      "source": "MSU-D",
      "target": "MSU-E2",
      "label": "部署同代码实例B",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "guide:uses_neutral_library": {
        "source_types": [
          "guide:msa_unit"
        ],
        "target_types": [
          "guide:msa_unit"
        ],
        "meaning": "源单元使用无业务公共库"
      },
      "guide:builds_deployment": {
        "source_types": [
          "guide:msa_unit"
        ],
        "target_types": [
          "guide:msa_unit"
        ],
        "meaning": "源构建成部署单元，非业务流程顺序"
      },
      "guide:deploys_instance": {
        "source_types": [
          "guide:msa_unit"
        ],
        "target_types": [
          "guide:msa_unit"
        ],
        "meaning": "同一部署单元实例化为运行单元"
      }
    }
  },
  "states": [],
  "view": {
    "id": "v-msa-source-deployment-execution",
    "artifact_id": "software-distribution-diagram",
    "profile_id": "msa-source-deployment-execution",
    "title": "MSA源、部署与执行单元追溯表",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "MSU-S",
      "LIB-log",
      "MSU-D",
      "MSU-E1",
      "MSU-E2"
    ],
    "relationship_ids": [
      "MSR-lib",
      "MSR-build",
      "MSR-A",
      "MSR-B"
    ],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "表格表达正文操作语义，不声称原图复刻。未知显式保留，ID稳定。",
    "allow_mixed_evolution": true
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-source-deployment-execution --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-source-deployment-execution --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
