# 架构全景投影

`profile_id`: architecture-landscape-projection；`artifact_id`: architecture-landscape-projection；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig3-1；G186/fig3-2。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "architecture-landscape-projection",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G186/fig3-1",
  "source_topology": "architecture-landscape",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "三轴投影；时效性不作第四轴"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, landscape_dimension, landscape_projection, landscape_slice。关系类型：project:contains, project:projects_to。

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

- 三轴投影；时效性不作第四轴
- 项目切片在全景内，不是第二个存储库

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G186/fig3-1, G186/fig3-2；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "land-volume",
      "type": "landscape_projection",
      "name": "EA 全景",
      "attributes": {
        "definition": "全部潜在架构内容的体积，不是某一个架构或存储库",
        "recency": "正文讨论的第四特征，本图不画轴"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "axis-breadth",
      "type": "landscape_dimension",
      "name": "广度（主题）",
      "attributes": {
        "definition": "按领域、组织或举措界定的覆盖范围",
        "axis": "breadth"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "axis-abs",
      "type": "landscape_dimension",
      "name": "详细程度",
      "attributes": {
        "definition": "展开到回答当前问题所需即可",
        "axis": "abstraction"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "axis-time",
      "type": "landscape_dimension",
      "name": "时间（规划期）",
      "attributes": {
        "definition": "从当前到目标架构的时间点",
        "axis": "time"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "slice-project",
      "type": "landscape_slice",
      "name": "当前架构项目切片",
      "attributes": {
        "definition": "全景内的项目范围，不是第二个存储库",
        "breadth": "履约域",
        "abstraction": "逻辑",
        "time": "本预算年"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "obj-capability",
      "type": "capability",
      "name": "预约改约能力",
      "attributes": {
        "definition": "同一对象可按三轴投影回模型",
        "breadth": "履约域",
        "abstraction": "逻辑",
        "time": "本预算年"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "p-b",
      "source": "land-volume",
      "target": "axis-breadth",
      "type": "project:projects_to",
      "label": "沿广度投影",
      "attributes": {
        "meaning": "沿广度投影"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "p-a",
      "source": "land-volume",
      "target": "axis-abs",
      "type": "project:projects_to",
      "label": "沿抽象投影",
      "attributes": {
        "meaning": "沿抽象投影"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "p-t",
      "source": "land-volume",
      "target": "axis-time",
      "type": "project:projects_to",
      "label": "沿时间投影",
      "attributes": {
        "meaning": "沿时间投影"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "p-s",
      "source": "land-volume",
      "target": "slice-project",
      "type": "project:contains",
      "label": "项目切片位于全景内",
      "attributes": {
        "meaning": "项目切片位于全景内"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "p-o",
      "source": "obj-capability",
      "target": "slice-project",
      "type": "project:projects_to",
      "label": "对象投影到本项目切片",
      "attributes": {
        "meaning": "对象投影到本项目切片"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:contains": {
        "meaning": "组成或位于之内",
        "source_types": [
          "*"
        ],
        "target_types": [
          "*"
        ]
      },
      "project:projects_to": {
        "meaning": "按轴或切片投影",
        "source_types": [
          "*"
        ],
        "target_types": [
          "*"
        ]
      }
    }
  },
  "view": {
    "id": "v-architecture-landscape-projection",
    "artifact_id": "architecture-landscape-projection",
    "profile_id": "architecture-landscape-projection",
    "title": "架构全景投影／来源结构专用示例",
    "entity_ids": [
      "land-volume",
      "axis-breadth",
      "axis-abs",
      "axis-time",
      "slice-project",
      "obj-capability"
    ],
    "relationship_ids": [
      "p-b",
      "p-a",
      "p-t",
      "p-s",
      "p-o"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-landscape-projection --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-landscape-projection --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
