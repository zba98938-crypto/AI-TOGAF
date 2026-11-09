# 存储库并行候选容器

ID：`repository-parallel-candidates`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig5-3。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

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

- [存储库并行候选容器](../profiles/repository-parallel-candidates.md)

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact repository-parallel-candidates --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
