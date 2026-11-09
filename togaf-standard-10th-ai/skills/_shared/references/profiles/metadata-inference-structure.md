# 技术元数据推断架构

`profile_id`: metadata-inference-structure；`artifact_id`: metadata-inference-design；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234/fig4-10。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "metadata-inference-structure",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G234/fig4-10",
  "source_topology": "metadata-inference",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "剖析与结构化来源可跨 DATA→METADATA"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_profiling, inference_source, metadata_management, metadata_zone。关系类型：project:metadata_uplinks, project:profiling_reads, project:structure_lifts。

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

- 剖析与结构化来源可跨 DATA→METADATA
- 访问条件与成本必须带来源

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G234/fig4-10；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "zone-meta",
      "type": "metadata_zone",
      "name": "METADATA",
      "attributes": {
        "definition": "元数据管理分区",
        "zone": "METADATA"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "zone-data",
      "type": "metadata_zone",
      "name": "DATA",
      "attributes": {
        "definition": "数据与剖析分区",
        "zone": "DATA"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "mgmt",
      "type": "metadata_management",
      "name": "元数据管理",
      "attributes": {
        "definition": "接收上行技术元数据",
        "access_condition": "仅已批准模式",
        "cost": "目录维护工时",
        "zone": "METADATA"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "prof",
      "type": "data_profiling",
      "name": "数据剖析",
      "attributes": {
        "definition": "读取来源并上推结构",
        "access_condition": "抽样须独立批准",
        "cost": "百万文件扫描成本",
        "zone": "DATA"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "src-s",
      "type": "inference_source",
      "name": "结构化来源",
      "attributes": {
        "definition": "模式可从字典采集",
        "data_structure": "structured",
        "schema_access": "可读字段模式",
        "content_access": "无需读取实际值",
        "governance_claim": "schema-available",
        "access_condition": "字典只读",
        "cost": "低"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "src-h",
      "type": "inference_source",
      "name": "半结构化来源",
      "attributes": {
        "definition": "有结构但不保证稳定",
        "data_structure": "semi-structured",
        "schema_access": "逐文件结构",
        "content_access": "仅抽样",
        "governance_claim": "partial",
        "access_condition": "抽样批准",
        "cost": "中"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "src-u",
      "type": "inference_source",
      "name": "非结构化来源",
      "attributes": {
        "definition": "须先抽取最低结构",
        "data_structure": "unstructured",
        "schema_access": "无稳定字段模式",
        "content_access": "内容扫描需隐私评估",
        "governance_claim": "ungoverned-until-scanned",
        "access_condition": "内容扫描批准",
        "cost": "高"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "read-s",
      "source": "prof",
      "target": "src-s",
      "type": "project:profiling_reads",
      "label": "剖析读取结构化",
      "attributes": {
        "meaning": "剖析读取结构化"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "read-h",
      "source": "prof",
      "target": "src-h",
      "type": "project:profiling_reads",
      "label": "剖析读取半结构化",
      "attributes": {
        "meaning": "剖析读取半结构化"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "read-u",
      "source": "prof",
      "target": "src-u",
      "type": "project:profiling_reads",
      "label": "剖析读取非结构化",
      "attributes": {
        "meaning": "剖析读取非结构化"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lift-uh",
      "source": "src-u",
      "target": "src-h",
      "type": "project:structure_lifts",
      "label": "非结构化上推半结构",
      "attributes": {
        "meaning": "非结构化上推半结构"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "lift-hs",
      "source": "src-h",
      "target": "src-s",
      "type": "project:structure_lifts",
      "label": "半结构上推结构",
      "attributes": {
        "meaning": "半结构上推结构"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "up-p",
      "source": "prof",
      "target": "mgmt",
      "type": "project:metadata_uplinks",
      "label": "剖析结果上行",
      "attributes": {
        "meaning": "剖析结果上行"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "up-s",
      "source": "src-s",
      "target": "mgmt",
      "type": "project:metadata_uplinks",
      "label": "结构化技术元数据上行",
      "attributes": {
        "meaning": "结构化技术元数据上行"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:metadata_uplinks": {
        "meaning": "元数据上行",
        "source_types": [
          "data_profiling",
          "inference_source"
        ],
        "target_types": [
          "metadata_management"
        ]
      },
      "project:profiling_reads": {
        "meaning": "剖析读取来源",
        "source_types": [
          "data_profiling"
        ],
        "target_types": [
          "inference_source"
        ]
      },
      "project:structure_lifts": {
        "meaning": "结构上推",
        "source_types": [
          "inference_source"
        ],
        "target_types": [
          "inference_source"
        ]
      }
    }
  },
  "view": {
    "id": "v-metadata-inference-structure",
    "artifact_id": "metadata-inference-design",
    "profile_id": "metadata-inference-structure",
    "title": "技术元数据推断架构／来源结构专用示例",
    "entity_ids": [
      "zone-meta",
      "zone-data",
      "mgmt",
      "prof",
      "src-s",
      "src-h",
      "src-u"
    ],
    "relationship_ids": [
      "read-s",
      "read-h",
      "read-u",
      "lift-uh",
      "lift-hs",
      "up-p",
      "up-s"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-inference-structure --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-inference-structure --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
