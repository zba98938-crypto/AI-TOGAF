# 存储库状态与视图树

ID：`repository-state-view-tree`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig5-2。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

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

对象类型：g186:repository_node。

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
| `g186:contains` | g186:repository_node → g186:repository_node | 显式包含或职责映射，不表示流程或批准 |

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

- [存储库状态与视图树](../profiles/repository-state-view-tree.md)

- [architecture-repository](../deliverables/architecture-repository.md)


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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact repository-state-view-tree --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
