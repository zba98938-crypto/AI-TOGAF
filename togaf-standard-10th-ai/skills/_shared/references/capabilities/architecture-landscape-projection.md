# 架构全景投影

ID：`architecture-landscape-projection`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig3-1；G186/fig3-2。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

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

对象类型：capability, landscape_dimension, landscape_projection, landscape_slice。

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
| `project:contains` | * → * | 组成或位于之内 |
| `project:projects_to` | * → * | 按轴或切片投影 |

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

- [架构全景投影](../profiles/architecture-landscape-projection.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-landscape-projection --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
