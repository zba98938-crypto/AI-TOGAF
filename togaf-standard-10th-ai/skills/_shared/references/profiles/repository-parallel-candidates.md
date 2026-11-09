# 存储库并行候选容器

`profile_id`: repository-parallel-candidates；`artifact_id`: repository-parallel-candidates；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig5-3。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "repository-parallel-candidates",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G186/fig5-3",
  "source_topology": "repository-tree",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "按显式关系与状态读取；来源解释不代表本地组织事实。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：g186:repository_node。关系类型：g186:contains。

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

- 按显式关系与状态读取；来源解释不代表本地组织事实。
- 折叠不等于空；选中不等于差异；不从布局推断语义。

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G186/fig5-3；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "c_workshop",
      "type": "g186:repository_node",
      "name": "Austin Workshop Candidate",
      "attributes": {
        "definition": "工作坊架构的候选容器。",
        "parent_id": null,
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_components",
      "type": "g186:repository_node",
      "name": "Components",
      "attributes": {
        "definition": "组件视图文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_connections",
      "type": "g186:repository_node",
      "name": "Connections",
      "attributes": {
        "definition": "连接视图文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_catalogues",
      "type": "g186:repository_node",
      "name": "Catalogues",
      "attributes": {
        "definition": "目录视图文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_matrices",
      "type": "g186:repository_node",
      "name": "Matrices",
      "attributes": {
        "definition": "矩阵视图文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_diagrams",
      "type": "g186:repository_node",
      "name": "Diagrams",
      "attributes": {
        "definition": "图视图文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_3d_views",
      "type": "g186:repository_node",
      "name": "3D Views",
      "attributes": {
        "definition": "三维视图文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_workshop_charts",
      "type": "g186:repository_node",
      "name": "Charts",
      "attributes": {
        "definition": "图表文件夹。",
        "parent_id": "c_workshop",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_portfolio",
      "type": "g186:repository_node",
      "name": "Austin Portfolio Candidate",
      "attributes": {
        "definition": "组合目的的候选架构容器。",
        "parent_id": null,
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_project_controls",
      "type": "g186:repository_node",
      "name": "Austin Workshop Project Controls Candidate (Project)",
      "attributes": {
        "definition": "项目目的的候选架构容器。",
        "parent_id": null,
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c_field_data",
      "type": "g186:repository_node",
      "name": "Austin Workshop Field Data Capture Candidate (Solution Delivery)",
      "attributes": {
        "definition": "解决方案交付目的的候选架构容器。",
        "parent_id": null,
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "contains-c_workshop_components",
      "source": "c_workshop",
      "target": "c_workshop_components",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contains-c_workshop_connections",
      "source": "c_workshop",
      "target": "c_workshop_connections",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contains-c_workshop_catalogues",
      "source": "c_workshop",
      "target": "c_workshop_catalogues",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contains-c_workshop_matrices",
      "source": "c_workshop",
      "target": "c_workshop_matrices",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contains-c_workshop_diagrams",
      "source": "c_workshop",
      "target": "c_workshop_diagrams",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contains-c_workshop_3d_views",
      "source": "c_workshop",
      "target": "c_workshop_3d_views",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "contains-c_workshop_charts",
      "source": "c_workshop",
      "target": "c_workshop_charts",
      "type": "g186:contains",
      "label": "包含（不表示时间或依赖）",
      "attributes": {
        "meaning": "包含（不表示时间或依赖）"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "entity_types": {},
    "relationship_types": {
      "g186:contains": {
        "source_types": [
          "g186:repository_node"
        ],
        "target_types": [
          "g186:repository_node"
        ],
        "meaning": "显式包含或职责映射，不表示流程或批准"
      }
    }
  },
  "view": {
    "id": "v-repository-parallel-candidates",
    "artifact_id": "repository-parallel-candidates",
    "profile_id": "repository-parallel-candidates",
    "title": "存储库并行候选容器／来源结构专用示例",
    "entity_ids": [
      "c_workshop",
      "c_workshop_components",
      "c_workshop_connections",
      "c_workshop_catalogues",
      "c_workshop_matrices",
      "c_workshop_diagrams",
      "c_workshop_3d_views",
      "c_workshop_charts",
      "c_portfolio",
      "c_project_controls",
      "c_field_data"
    ],
    "relationship_ids": [
      "contains-c_workshop_components",
      "contains-c_workshop_connections",
      "contains-c_workshop_catalogues",
      "contains-c_workshop_matrices",
      "contains-c_workshop_diagrams",
      "contains-c_workshop_3d_views",
      "contains-c_workshop_charts"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile repository-parallel-candidates --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile repository-parallel-candidates --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
