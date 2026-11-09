# 架构存储库结构

ID：`architecture-repository-structure`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig5-1。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

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

对象类型：repository_asset, repository_container, repository_external, repository_partition。

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
| `project:adopts` | repository_external → repository_partition | 采纳外部材料 |
| `project:contains` | * → * | 组成或位于之内 |
| `project:delivers_outcomes` | repository_partition → repository_partition | 业务成果交付 |
| `project:enables` | * → * | 使能 |
| `project:governs` | repository_partition → repository_partition | 治理作用 |
| `project:steers` | repository_external → repository_partition | 引导能力 |
| `project:structured_by` | repository_partition → repository_partition | 按框架结构化 |
| `project:visibility_escalation` | repository_external → repository_partition | 可见性与上报 |

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

- [架构存储库结构](../profiles/architecture-repository-structure.md)

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
      "description": "专用拓扑验收示例：G186/fig5-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "ent-enterprise",
      "type": "repository_container",
      "name": "企业存储库",
      "attributes": {
        "definition": "比架构库更宽的企业级存储范围",
        "container_role": "enterprise"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ent-archrepo",
      "type": "repository_container",
      "name": "架构存储库",
      "attributes": {
        "definition": "含七分区与架构能力，不等于全景本身",
        "container_role": "architecture"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-metamodel",
      "type": "repository_partition",
      "name": "架构元模型",
      "attributes": {
        "definition": "规定全景制品如何按框架结构化",
        "partition_role": "metamodel"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-landscape",
      "type": "repository_partition",
      "name": "架构全景",
      "attributes": {
        "definition": "战略/分段/能力三层；只是分区之一",
        "partition_role": "landscape"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-solutions",
      "type": "repository_partition",
      "name": "解决方案全景",
      "attributes": {
        "definition": "解决方案构建块容器",
        "partition_role": "solutions"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-reference",
      "type": "repository_partition",
      "name": "参考库",
      "attributes": {
        "definition": "组织参考材料",
        "partition_role": "reference"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-standards",
      "type": "repository_partition",
      "name": "标准库",
      "attributes": {
        "definition": "业务/数据/应用/技术标准",
        "partition_role": "standards"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-requirements",
      "type": "repository_partition",
      "name": "架构需求库",
      "attributes": {
        "definition": "驱动与需求材料",
        "partition_role": "requirements"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-governance",
      "type": "repository_partition",
      "name": "治理库",
      "attributes": {
        "definition": "决策日志、合规与能力评估",
        "partition_role": "governance"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-capability",
      "type": "repository_partition",
      "name": "架构能力",
      "attributes": {
        "definition": "技能、方法与能力资产",
        "partition_role": "capability"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ext-refs",
      "type": "repository_external",
      "name": "外部参考模型",
      "attributes": {
        "definition": "位于架构库外侧，被采纳而非内含",
        "external_role": "reference-model"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ext-std",
      "type": "repository_external",
      "name": "外部标准",
      "attributes": {
        "definition": "位于架构库外侧",
        "external_role": "standard"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ext-board",
      "type": "repository_external",
      "name": "架构委员会",
      "attributes": {
        "definition": "治理可见性与上报，并引导架构能力",
        "external_role": "board"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "asset-strategic",
      "type": "repository_asset",
      "name": "战略架构入口",
      "attributes": {
        "definition": "全景中的战略层入口，不是整个库",
        "asset_kind": "landscape-entry"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "c-ent-arch",
      "source": "ent-enterprise",
      "target": "ent-archrepo",
      "type": "project:contains",
      "label": "企业库包含架构库",
      "attributes": {
        "meaning": "企业库包含架构库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-meta",
      "source": "ent-archrepo",
      "target": "part-metamodel",
      "type": "project:contains",
      "label": "架构库包含元模型",
      "attributes": {
        "meaning": "架构库包含元模型"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-land",
      "source": "ent-archrepo",
      "target": "part-landscape",
      "type": "project:contains",
      "label": "架构库包含全景分区",
      "attributes": {
        "meaning": "架构库包含全景分区"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-sol",
      "source": "ent-archrepo",
      "target": "part-solutions",
      "type": "project:contains",
      "label": "架构库包含解决方案全景",
      "attributes": {
        "meaning": "架构库包含解决方案全景"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-ref",
      "source": "ent-archrepo",
      "target": "part-reference",
      "type": "project:contains",
      "label": "架构库包含参考库",
      "attributes": {
        "meaning": "架构库包含参考库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-std",
      "source": "ent-archrepo",
      "target": "part-standards",
      "type": "project:contains",
      "label": "架构库包含标准库",
      "attributes": {
        "meaning": "架构库包含标准库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-req",
      "source": "ent-archrepo",
      "target": "part-requirements",
      "type": "project:contains",
      "label": "架构库包含需求库",
      "attributes": {
        "meaning": "架构库包含需求库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-gov",
      "source": "ent-archrepo",
      "target": "part-governance",
      "type": "project:contains",
      "label": "架构库包含治理库",
      "attributes": {
        "meaning": "架构库包含治理库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-arch-cap",
      "source": "ent-archrepo",
      "target": "part-capability",
      "type": "project:contains",
      "label": "架构库包含架构能力",
      "attributes": {
        "meaning": "架构库包含架构能力"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-land-asset",
      "source": "part-landscape",
      "target": "asset-strategic",
      "type": "project:contains",
      "label": "全景包含战略入口",
      "attributes": {
        "meaning": "全景包含战略入口"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-struct",
      "source": "part-metamodel",
      "target": "part-landscape",
      "type": "project:structured_by",
      "label": "全景制品按框架结构化",
      "attributes": {
        "meaning": "全景制品按框架结构化"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-enable",
      "source": "part-landscape",
      "target": "part-solutions",
      "type": "project:enables",
      "label": "全景使能解决方案全景",
      "attributes": {
        "meaning": "全景使能解决方案全景"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-gov",
      "source": "part-governance",
      "target": "part-landscape",
      "type": "project:governs",
      "label": "治理库治理全景",
      "attributes": {
        "meaning": "治理库治理全景"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-adopt-std",
      "source": "ext-std",
      "target": "part-standards",
      "type": "project:adopts",
      "label": "外部标准被采纳",
      "attributes": {
        "meaning": "外部标准被采纳"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-adopt",
      "source": "ext-refs",
      "target": "part-reference",
      "type": "project:adopts",
      "label": "外部参考被采纳",
      "attributes": {
        "meaning": "外部参考被采纳"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-vis",
      "source": "ext-board",
      "target": "part-governance",
      "type": "project:visibility_escalation",
      "label": "可见性与上报",
      "attributes": {
        "meaning": "可见性与上报"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-steer",
      "source": "ext-board",
      "target": "part-capability",
      "type": "project:steers",
      "label": "引导并管理能力",
      "attributes": {
        "meaning": "引导并管理能力"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "r-out",
      "source": "part-solutions",
      "target": "part-requirements",
      "type": "project:delivers_outcomes",
      "label": "业务成果交付",
      "attributes": {
        "meaning": "业务成果交付"
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
      "project:governs": {
        "meaning": "治理作用",
        "source_types": [
          "repository_partition"
        ],
        "target_types": [
          "repository_partition"
        ]
      },
      "project:enables": {
        "meaning": "使能",
        "source_types": [
          "*"
        ],
        "target_types": [
          "*"
        ]
      },
      "project:adopts": {
        "meaning": "采纳外部材料",
        "source_types": [
          "repository_external"
        ],
        "target_types": [
          "repository_partition"
        ]
      },
      "project:visibility_escalation": {
        "meaning": "可见性与上报",
        "source_types": [
          "repository_external"
        ],
        "target_types": [
          "repository_partition"
        ]
      },
      "project:steers": {
        "meaning": "引导能力",
        "source_types": [
          "repository_external"
        ],
        "target_types": [
          "repository_partition"
        ]
      },
      "project:delivers_outcomes": {
        "meaning": "业务成果交付",
        "source_types": [
          "repository_partition"
        ],
        "target_types": [
          "repository_partition"
        ]
      },
      "project:structured_by": {
        "meaning": "按框架结构化",
        "source_types": [
          "repository_partition"
        ],
        "target_types": [
          "repository_partition"
        ]
      }
    }
  },
  "view": {
    "id": "v-architecture-repository-structure",
    "artifact_id": "architecture-repository-structure",
    "profile_id": "architecture-repository-structure",
    "title": "架构存储库结构／来源结构专用示例",
    "entity_ids": [
      "ent-enterprise",
      "ent-archrepo",
      "part-metamodel",
      "part-landscape",
      "part-solutions",
      "part-reference",
      "part-standards",
      "part-requirements",
      "part-governance",
      "part-capability",
      "ext-refs",
      "ext-std",
      "ext-board",
      "asset-strategic"
    ],
    "relationship_ids": [
      "c-ent-arch",
      "c-arch-meta",
      "c-arch-land",
      "c-arch-sol",
      "c-arch-ref",
      "c-arch-std",
      "c-arch-req",
      "c-arch-gov",
      "c-arch-cap",
      "c-land-asset",
      "r-struct",
      "r-enable",
      "r-gov",
      "r-adopt-std",
      "r-adopt",
      "r-vis",
      "r-steer",
      "r-out"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-repository-structure --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
