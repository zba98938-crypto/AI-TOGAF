# 能力与项目连续谱

`profile_id`: capability-project-continuum；`artifact_id`: capability-project-continuum；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig8-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "capability-project-continuum",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G186/fig8-1",
  "source_topology": "capability-continuum",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "按显式关系与状态读取；来源解释不代表本地组织事实。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：g186:continuum, g186:continuum_label。关系类型：。

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
      "description": "专用拓扑验收示例：G186/fig8-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "continuum",
      "type": "g186:continuum",
      "name": "能力与项目连续谱",
      "attributes": {
        "definition": "0–10无单位；标签仅有阅读顺序，无精确分段值、时间或成熟度含义",
        "scale_min": 0,
        "scale_max": 10,
        "unit": "unitless"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-0",
      "type": "g186:continuum_label",
      "name": "维持：与他人持平",
      "attributes": {
        "definition": "维持：与他人持平",
        "order": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-1",
      "type": "g186:continuum_label",
      "name": "维持：保持相同优势",
      "attributes": {
        "definition": "维持：保持相同优势",
        "order": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-2",
      "type": "g186:continuum_label",
      "name": "改进：创造竞争优势",
      "attributes": {
        "definition": "改进：创造竞争优势",
        "order": 3
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-3",
      "type": "g186:continuum_label",
      "name": "改进：创造新收入流",
      "attributes": {
        "definition": "改进：创造新收入流",
        "order": 4
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "extensions": {
    "entity_types": {},
    "relationship_types": {}
  },
  "view": {
    "id": "v-capability-project-continuum",
    "artifact_id": "capability-project-continuum",
    "profile_id": "capability-project-continuum",
    "title": "能力与项目连续谱／来源结构专用示例",
    "entity_ids": [
      "continuum",
      "position-0",
      "position-1",
      "position-2",
      "position-3"
    ],
    "relationship_ids": [],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-project-continuum --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-project-continuum --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
