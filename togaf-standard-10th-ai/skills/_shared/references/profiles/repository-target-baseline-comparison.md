# 存储库版本比较 Target → Baseline

`profile_id`: repository-target-baseline-comparison；`artifact_id`: repository-target-baseline-comparison；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig13-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "repository-target-baseline-comparison",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G186/fig13-1",
  "source_topology": "repository-comparison",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "按显式关系与状态读取；来源解释不代表本地组织事实。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：g186:comparison_item, g186:repository_snapshot。关系类型：g186:compares_from, g186:compares_to。

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile repository-target-baseline-comparison --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile repository-target-baseline-comparison --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
