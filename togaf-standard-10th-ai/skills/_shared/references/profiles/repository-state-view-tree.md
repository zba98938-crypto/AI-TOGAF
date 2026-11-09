# 存储库状态与视图树

`profile_id`: repository-state-view-tree；`artifact_id`: repository-state-view-tree；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig5-2。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "repository-state-view-tree",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G186/fig5-2",
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
      "description": "专用拓扑验收示例：G186/fig5-2；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "aw_architecture",
      "type": "g186:repository_node",
      "name": "Austin Workshop Architecture",
      "attributes": {
        "definition": "示例架构的根容器。",
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
      "id": "aw_components",
      "type": "g186:repository_node",
      "name": "Components",
      "attributes": {
        "definition": "组件视图文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_connections",
      "type": "g186:repository_node",
      "name": "Connections",
      "attributes": {
        "definition": "连接视图文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_catalogues",
      "type": "g186:repository_node",
      "name": "Catalogues",
      "attributes": {
        "definition": "目录视图文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_matrices",
      "type": "g186:repository_node",
      "name": "Matrices",
      "attributes": {
        "definition": "矩阵视图文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_diagrams",
      "type": "g186:repository_node",
      "name": "Diagrams",
      "attributes": {
        "definition": "图视图文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_3d_views",
      "type": "g186:repository_node",
      "name": "3D Views",
      "attributes": {
        "definition": "三维视图文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_charts",
      "type": "g186:repository_node",
      "name": "Charts",
      "attributes": {
        "definition": "图表文件夹。",
        "parent_id": "aw_architecture",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_candidate",
      "type": "g186:repository_node",
      "name": "Austin Workshop Candidate",
      "attributes": {
        "definition": "候选状态容器，未展开。",
        "parent_id": "aw_architecture",
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_target",
      "type": "g186:repository_node",
      "name": "Austin Workshop Target",
      "attributes": {
        "definition": "目标状态容器。",
        "parent_id": "aw_architecture",
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "aw_current",
      "type": "g186:repository_node",
      "name": "Austin Workshop Current",
      "attributes": {
        "definition": "现状状态容器，未展开。",
        "parent_id": "aw_architecture",
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_components",
      "type": "g186:repository_node",
      "name": "Components",
      "attributes": {
        "definition": "目标状态的组件视图。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_connections",
      "type": "g186:repository_node",
      "name": "Connections",
      "attributes": {
        "definition": "目标状态的连接视图。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_catalogues",
      "type": "g186:repository_node",
      "name": "Catalogues",
      "attributes": {
        "definition": "目标状态的目录视图。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_matrices",
      "type": "g186:repository_node",
      "name": "Matrices",
      "attributes": {
        "definition": "目标状态的矩阵视图。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_diagrams",
      "type": "g186:repository_node",
      "name": "Diagrams",
      "attributes": {
        "definition": "目标状态的图视图。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_3d_views",
      "type": "g186:repository_node",
      "name": "3D Views",
      "attributes": {
        "definition": "目标状态的三维视图。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_charts",
      "type": "g186:repository_node",
      "name": "Charts",
      "attributes": {
        "definition": "目标状态的图表。",
        "parent_id": "aw_target",
        "node_kind": "view-folder",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_annual_current",
      "type": "g186:repository_node",
      "name": "Austin Workshop Annual Transition (Current Year)",
      "attributes": {
        "definition": "本年度过渡状态。",
        "parent_id": "aw_target",
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_annual_next",
      "type": "g186:repository_node",
      "name": "Austin Workshop Annual Transition (Next Year)",
      "attributes": {
        "definition": "下一年度过渡状态。",
        "parent_id": "aw_target",
        "node_kind": "state-container",
        "disclosure": "visible-source-excerpt; folded contents unknown"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "awt_transition",
      "type": "g186:repository_node",
      "name": "Austin Workshop Transition",
      "attributes": {
        "definition": "未标注年度的过渡状态。",
        "parent_id": "aw_target",
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
      "id": "contains-aw_components",
      "source": "aw_architecture",
      "target": "aw_components",
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
      "id": "contains-aw_connections",
      "source": "aw_architecture",
      "target": "aw_connections",
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
      "id": "contains-aw_catalogues",
      "source": "aw_architecture",
      "target": "aw_catalogues",
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
      "id": "contains-aw_matrices",
      "source": "aw_architecture",
      "target": "aw_matrices",
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
      "id": "contains-aw_diagrams",
      "source": "aw_architecture",
      "target": "aw_diagrams",
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
      "id": "contains-aw_3d_views",
      "source": "aw_architecture",
      "target": "aw_3d_views",
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
      "id": "contains-aw_charts",
      "source": "aw_architecture",
      "target": "aw_charts",
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
      "id": "contains-aw_candidate",
      "source": "aw_architecture",
      "target": "aw_candidate",
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
      "id": "contains-aw_target",
      "source": "aw_architecture",
      "target": "aw_target",
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
      "id": "contains-aw_current",
      "source": "aw_architecture",
      "target": "aw_current",
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
      "id": "contains-awt_components",
      "source": "aw_target",
      "target": "awt_components",
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
      "id": "contains-awt_connections",
      "source": "aw_target",
      "target": "awt_connections",
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
      "id": "contains-awt_catalogues",
      "source": "aw_target",
      "target": "awt_catalogues",
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
      "id": "contains-awt_matrices",
      "source": "aw_target",
      "target": "awt_matrices",
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
      "id": "contains-awt_diagrams",
      "source": "aw_target",
      "target": "awt_diagrams",
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
      "id": "contains-awt_3d_views",
      "source": "aw_target",
      "target": "awt_3d_views",
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
      "id": "contains-awt_charts",
      "source": "aw_target",
      "target": "awt_charts",
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
      "id": "contains-awt_annual_current",
      "source": "aw_target",
      "target": "awt_annual_current",
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
      "id": "contains-awt_annual_next",
      "source": "aw_target",
      "target": "awt_annual_next",
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
      "id": "contains-awt_transition",
      "source": "aw_target",
      "target": "awt_transition",
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
    "id": "v-repository-state-view-tree",
    "artifact_id": "repository-state-view-tree",
    "profile_id": "repository-state-view-tree",
    "title": "存储库状态与视图树／来源结构专用示例",
    "entity_ids": [
      "aw_architecture",
      "aw_components",
      "aw_connections",
      "aw_catalogues",
      "aw_matrices",
      "aw_diagrams",
      "aw_3d_views",
      "aw_charts",
      "aw_candidate",
      "aw_target",
      "aw_current",
      "awt_components",
      "awt_connections",
      "awt_catalogues",
      "awt_matrices",
      "awt_diagrams",
      "awt_3d_views",
      "awt_charts",
      "awt_annual_current",
      "awt_annual_next",
      "awt_transition"
    ],
    "relationship_ids": [
      "contains-aw_components",
      "contains-aw_connections",
      "contains-aw_catalogues",
      "contains-aw_matrices",
      "contains-aw_diagrams",
      "contains-aw_3d_views",
      "contains-aw_charts",
      "contains-aw_candidate",
      "contains-aw_target",
      "contains-aw_current",
      "contains-awt_components",
      "contains-awt_connections",
      "contains-awt_catalogues",
      "contains-awt_matrices",
      "contains-awt_diagrams",
      "contains-awt_3d_views",
      "contains-awt_charts",
      "contains-awt_annual_current",
      "contains-awt_annual_next",
      "contains-awt_transition"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile repository-state-view-tree --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile repository-state-view-tree --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
