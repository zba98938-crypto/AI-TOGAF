# 存储库版本比较 Target → Baseline

ID：`repository-target-baseline-comparison`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig13-1。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

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

对象类型：g186:comparison_item, g186:repository_snapshot。

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
| `g186:compares_from` | g186:repository_snapshot,g186:comparison_item → g186:repository_snapshot,g186:comparison_item | 显式包含或职责映射，不表示流程或批准 |
| `g186:compares_to` | g186:repository_snapshot,g186:comparison_item → g186:repository_snapshot,g186:comparison_item | 显式包含或职责映射，不表示流程或批准 |

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

- [存储库版本比较 Target → Baseline](../profiles/repository-target-baseline-comparison.md)
- [存储库版本比较 Baseline → Target](../profiles/repository-baseline-target-comparison.md)

- [requirements-impact-assessment](../deliverables/requirements-impact-assessment.md)
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
      "description": "专用拓扑验收示例：G186/fig13-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "snapshot-from",
      "type": "g186:repository_snapshot",
      "name": "Target",
      "attributes": {
        "definition": "比较起点，方向必须先于差异解释",
        "snapshot": "Target"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "snapshot-to",
      "type": "g186:repository_snapshot",
      "name": "Baseline",
      "attributes": {
        "definition": "比较终点，导航到同ID明细",
        "snapshot": "Baseline"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-0",
      "type": "g186:comparison_item",
      "name": "Project Controls",
      "attributes": {
        "definition": "项目控制",
        "from_values": {
          "definition": "Project Controls / revised"
        },
        "to_values": {
          "definition": "Project Controls / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-1",
      "type": "g186:comparison_item",
      "name": "Financial Management",
      "attributes": {
        "definition": "财务管理",
        "from_values": {
          "definition": "Financial Management / baseline"
        },
        "to_values": {
          "definition": "Financial Management / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-2",
      "type": "g186:comparison_item",
      "name": "Integrated Operations Outputs",
      "attributes": {
        "definition": "集成运营输出",
        "from_values": {
          "definition": "Integrated Operations Outputs / revised"
        },
        "to_values": {
          "definition": "Integrated Operations Outputs / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-3",
      "type": "g186:comparison_item",
      "name": "Consistent Estimation & Bidding",
      "attributes": {
        "definition": "一致估算与投标",
        "from_values": {
          "definition": "Consistent Estimation & Bidding / revised"
        },
        "to_values": {
          "definition": "Consistent Estimation & Bidding / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-4",
      "type": "g186:comparison_item",
      "name": "Contract Management",
      "attributes": {
        "definition": "合同管理",
        "from_values": {
          "definition": "Contract Management / revised"
        },
        "to_values": {
          "definition": "Contract Management / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-5",
      "type": "g186:comparison_item",
      "name": "Skills Development",
      "attributes": {
        "definition": "技能发展",
        "from_values": {
          "definition": "Skills Development / baseline"
        },
        "to_values": {
          "definition": "Skills Development / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-6",
      "type": "g186:comparison_item",
      "name": "EOD Reporting / Book Closure",
      "attributes": {
        "definition": "日终报告/账务关闭",
        "from_values": {
          "definition": "EOD Reporting / Book Closure / revised"
        },
        "to_values": {
          "definition": "EOD Reporting / Book Closure / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-7",
      "type": "g186:comparison_item",
      "name": "Fleet Management",
      "attributes": {
        "definition": "车队管理",
        "from_values": {
          "definition": "Fleet Management / baseline"
        },
        "to_values": {
          "definition": "Fleet Management / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "diff-8",
      "type": "g186:comparison_item",
      "name": "Customer Intimacy",
      "attributes": {
        "definition": "客户亲密度",
        "from_values": {
          "definition": "Customer Intimacy / revised"
        },
        "to_values": {
          "definition": "Customer Intimacy / baseline"
        },
        "from_children": [],
        "to_children": []
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "from-0",
      "source": "snapshot-from",
      "target": "diff-0",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-0",
      "source": "diff-0",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-1",
      "source": "snapshot-from",
      "target": "diff-1",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-1",
      "source": "diff-1",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-2",
      "source": "snapshot-from",
      "target": "diff-2",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-2",
      "source": "diff-2",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-3",
      "source": "snapshot-from",
      "target": "diff-3",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-3",
      "source": "diff-3",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-4",
      "source": "snapshot-from",
      "target": "diff-4",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-4",
      "source": "diff-4",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-5",
      "source": "snapshot-from",
      "target": "diff-5",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-5",
      "source": "diff-5",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-6",
      "source": "snapshot-from",
      "target": "diff-6",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-6",
      "source": "diff-6",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-7",
      "source": "snapshot-from",
      "target": "diff-7",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-7",
      "source": "diff-7",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "from-8",
      "source": "snapshot-from",
      "target": "diff-8",
      "type": "g186:compares_from",
      "label": "源架构导航",
      "attributes": {
        "meaning": "源架构导航"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "to-8",
      "source": "diff-8",
      "target": "snapshot-to",
      "type": "g186:compares_to",
      "label": "目标架构导航",
      "attributes": {
        "meaning": "目标架构导航"
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
      "g186:compares_to": {
        "source_types": [
          "g186:repository_snapshot",
          "g186:comparison_item"
        ],
        "target_types": [
          "g186:repository_snapshot",
          "g186:comparison_item"
        ],
        "meaning": "显式包含或职责映射，不表示流程或批准"
      },
      "g186:compares_from": {
        "source_types": [
          "g186:repository_snapshot",
          "g186:comparison_item"
        ],
        "target_types": [
          "g186:repository_snapshot",
          "g186:comparison_item"
        ],
        "meaning": "显式包含或职责映射，不表示流程或批准"
      }
    }
  },
  "view": {
    "id": "v-repository-target-baseline-comparison",
    "artifact_id": "repository-target-baseline-comparison",
    "profile_id": "repository-target-baseline-comparison",
    "title": "存储库版本比较 Target → Baseline／来源结构专用示例",
    "entity_ids": [
      "snapshot-from",
      "snapshot-to",
      "diff-0",
      "diff-1",
      "diff-2",
      "diff-3",
      "diff-4",
      "diff-5",
      "diff-6",
      "diff-7",
      "diff-8"
    ],
    "relationship_ids": [
      "from-0",
      "to-0",
      "from-1",
      "to-1",
      "from-2",
      "to-2",
      "from-3",
      "to-3",
      "from-4",
      "to-4",
      "from-5",
      "to-5",
      "from-6",
      "to-6",
      "from-7",
      "to-7",
      "from-8",
      "to-8"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact repository-target-baseline-comparison --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
