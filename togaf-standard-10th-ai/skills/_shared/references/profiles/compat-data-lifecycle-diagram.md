# 数据生命周期图（兼容默认）

`profile_id`: compat-data-lifecycle-diagram；`artifact_id`: data-lifecycle-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G234；G152。

## 构图与定义状态

表示族：`state`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-data-lifecycle-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_state。关系类型：transitions_to。

```json
{
  "entities": {
    "data_state": [
      "retention",
      "owner",
      "entry",
      "exit"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 保留期须有业务或法规依据
- 生命周期不等于 CRUD 操作清单

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构兼容案例；不是正式定义或来源图复刻。",
  "sources": [
    {
      "id": "case",
      "kind": "example",
      "description": "全量验收使用的虚构业务情景；数字、主体和架构均非真实项目事实。"
    },
    {
      "id": "assumption",
      "kind": "assumption",
      "description": "方案和收益因果假设，需在真实项目中验证。"
    }
  ],
  "entities": [
    {
      "id": "data-active",
      "type": "data_state",
      "name": "活动数据",
      "attributes": {
        "retention": "业务处理中",
        "owner": "数据负责人",
        "entry": "订单创建",
        "exit": "交易完成"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-archive",
      "type": "data_state",
      "name": "归档数据",
      "attributes": {
        "retention": "政策规定窗口",
        "owner": "数据负责人",
        "entry": "交易完成",
        "exit": "允许销毁"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-destroyed",
      "type": "data_state",
      "name": "已销毁",
      "attributes": {
        "retention": "不再保留内容",
        "owner": "数据负责人",
        "entry": "到期且无法律保留",
        "exit": "终态"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "data-archive-edge",
      "type": "transitions_to",
      "source": "data-active",
      "target": "data-archive",
      "label": "交易结束归档",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-destroy-edge",
      "type": "transitions_to",
      "source": "data-archive",
      "target": "data-destroyed",
      "label": "到期且无保留义务后销毁",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-data-lifecycle-diagram",
    "artifact_id": "data-lifecycle-diagram",
    "title": "数据生命周期图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "data-active",
      "data-archive",
      "data-destroyed"
    ],
    "relationship_ids": [
      "data-archive-edge",
      "data-destroy-edge"
    ],
    "analysis": "数据从创建到保留和销毁经历哪些状态？ 本视图限定订单履约改造范围，展示案例设定的数据生命周期图。按数据类别定义状态；实际项目需由相关责任方核实。",
    "legend": "状态节点；箭头表示满足标签条件后的状态转换。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-data-lifecycle-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-lifecycle-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-lifecycle-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
