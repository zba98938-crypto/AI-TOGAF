# 领域架构融入整体EA核对

`profile_id`: domain-architecture-alignment-default；`artifact_id`: domain-architecture-alignment；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G186 §12.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "domain-architecture-alignment-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:domain-architecture, guide:ea-project-scope。关系类型：。

```json
{
  "entities": {
    "guide:domain-architecture": [
      "kind",
      "project_id",
      "objective_ids"
    ],
    "guide:ea-project-scope": [
      "objective_ids",
      "model_id"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 领域必须融入整体EA，整体EA也须契合领域
- 安全架构只在参照其他域时存在，按关注点处理
- 对齐核对不评价领域方案质量

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "DAA-R1",
      "kind": "example",
      "description": "虚构EA项目EA-2027：目标OBJ-1缩短履约时长、OBJ-2降低合规风险，共享模型M-1。",
      "locator": "raw-materials.json#DAA-R1"
    },
    {
      "id": "DAA-R2",
      "kind": "example",
      "description": "数据领域团队按自建“数据中台项目DP-9”推进，目标为“建设统一数据平台”；安全团队计划单独编写安全架构文档。",
      "locator": "raw-materials.json#DAA-R2"
    }
  ],
  "entities": [
    {
      "id": "EA-2027",
      "type": "guide:ea-project-scope",
      "name": "EA项目EA-2027",
      "attributes": {
        "objective_ids": [
          "OBJ-1",
          "OBJ-2"
        ],
        "model_id": "M-1"
      },
      "evidence": [
        "DAA-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DOM-BIZ",
      "type": "guide:domain-architecture",
      "name": "业务架构",
      "attributes": {
        "kind": "business",
        "project_id": "EA-2027",
        "objective_ids": [
          "OBJ-1"
        ],
        "shared_entity_ids": [
          "cap-fulfilment"
        ]
      },
      "evidence": [
        "DAA-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DOM-DATA",
      "type": "guide:domain-architecture",
      "name": "数据架构",
      "attributes": {
        "kind": "data",
        "project_id": "DP-9",
        "objective_ids": [
          "OBJ-DP"
        ],
        "shared_entity_ids": []
      },
      "evidence": [
        "DAA-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DOM-SEC",
      "type": "guide:domain-architecture",
      "name": "安全架构",
      "attributes": {
        "kind": "security",
        "project_id": "EA-2027",
        "objective_ids": [
          "OBJ-2"
        ],
        "shared_entity_ids": [
          "req-privacy"
        ],
        "treated_as": "standalone-document",
        "referenced_domain_ids": []
      },
      "evidence": [
        "DAA-R2"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "domain-architecture-alignment-baseline",
    "artifact_id": "domain-architecture-alignment",
    "profile_id": "domain-architecture-alignment-default",
    "title": "领域架构融入整体EA核对／虚构星河零售",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "EA-2027",
      "DOM-BIZ",
      "DOM-DATA",
      "DOM-SEC"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行domain-architecture-alignment-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "domain-architecture-alignment-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "domain-architecture-alignment-analysis",
      "method_id": "domain-architecture-alignment-review",
      "inputs": {
        "source_ids": [
          "DAA-R1",
          "DAA-R2"
        ],
        "ea_project": {
          "id": "EA-2027",
          "objective_ids": [
            "OBJ-1",
            "OBJ-2"
          ]
        },
        "domains": [
          {
            "id": "DOM-BIZ",
            "name": "业务架构",
            "kind": "business",
            "project_id": "EA-2027",
            "objective_ids": [
              "OBJ-1"
            ],
            "shared_entity_ids": [
              "cap-fulfilment"
            ],
            "evidence": [
              "DAA-R1"
            ]
          },
          {
            "id": "DOM-DATA",
            "name": "数据架构",
            "kind": "data",
            "project_id": "DP-9",
            "objective_ids": [
              "OBJ-DP"
            ],
            "shared_entity_ids": [],
            "evidence": [
              "DAA-R2"
            ]
          },
          {
            "id": "DOM-SEC",
            "name": "安全架构",
            "kind": "security",
            "project_id": "EA-2027",
            "objective_ids": [
              "OBJ-2"
            ],
            "shared_entity_ids": [
              "req-privacy"
            ],
            "treated_as": "standalone-document",
            "referenced_domain_ids": [],
            "evidence": [
              "DAA-R2"
            ]
          }
        ]
      }
    }
  ]
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile domain-architecture-alignment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile domain-architecture-alignment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
