# 因素与主要后果矩阵

`profile_id`: dtra-factor-consequence；`artifact_id`: readiness-consequence-analysis；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212/fig5-3。

## 构图与定义状态

表示族：`matrix`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G212/fig5-3",
  "layout_notes": "每个缺失因素对应主要后果，背景重复列表不形成全连接",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/dtra-factor-consequence.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：consequence, readiness_factor。关系类型：has_consequence。

```json
{
  "entities": {},
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每个缺失因素对应主要后果，背景重复列表不形成全连接

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "dtra-factor-consequence-factor",
      "type": "readiness_factor",
      "name": "赞助与方向",
      "attributes": {
        "category": "基础",
        "rating": 4,
        "evidence": "虚构访谈：发起人尚未承诺"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-consequence-consequence",
      "type": "consequence",
      "name": "决策和资源缺乏持续支持",
      "attributes": {
        "definition": "条件性主要后果；发生概率待分析"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "dtra-factor-consequence-factor-consequence",
      "type": "has_consequence",
      "source": "dtra-factor-consequence-factor",
      "target": "dtra-factor-consequence-consequence",
      "label": "因素不足可能导致该后果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-dtra-factor-consequence",
    "artifact_id": "readiness-consequence-analysis",
    "profile_id": "dtra-factor-consequence",
    "title": "因素与主要后果矩阵／虚构案例",
    "entity_ids": [
      "dtra-factor-consequence-factor",
      "dtra-factor-consequence-consequence"
    ],
    "relationship_ids": [
      "dtra-factor-consequence-factor-consequence"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-factor-consequence --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-factor-consequence --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
