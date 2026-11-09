# 逻辑数据图（兼容默认）

`profile_id`: compat-logical-data-diagram；`artifact_id`: logical-data-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G234；G21B。

## 构图与定义状态

表示族：`er`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-logical-data-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：logical_entity。关系类型：logical_association。

```json
{
  "entities": {
    "logical_entity": [
      "attributes",
      "key",
      "normalization"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 数据类型保持产品中立
- 未知基数不能用默认一对多填充

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
      "id": "logical-customer",
      "type": "logical_entity",
      "name": "客户逻辑实体",
      "attributes": {
        "attributes": [
          {
            "name": "客户标识",
            "required": true
          },
          {
            "name": "联系信息",
            "required": false
          }
        ],
        "key": "客户标识",
        "normalization": "示例第三范式",
        "owner": "数据负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "logical-order",
      "type": "logical_entity",
      "name": "订单逻辑实体",
      "attributes": {
        "attributes": [
          {
            "name": "订单标识",
            "required": true
          },
          {
            "name": "客户标识",
            "required": true
          }
        ],
        "key": "订单标识",
        "normalization": "示例第三范式",
        "owner": "数据负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "logical-assoc",
      "type": "logical_association",
      "source": "logical-customer",
      "target": "logical-order",
      "label": "客户具有订单",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "cardinality": {
        "source": {
          "min": 1,
          "max": 1
        },
        "target": {
          "min": 0,
          "max": null
        }
      }
    }
  ],
  "view": {
    "id": "v-logical-data-diagram",
    "artifact_id": "logical-data-diagram",
    "title": "逻辑数据图 · 星河零售虚构案例",
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
      "logical-customer",
      "logical-order"
    ],
    "relationship_ids": [
      "logical-assoc"
    ],
    "analysis": "逻辑实体分别使用客户标识和订单标识；订单包含客户引用。不绑定数据库产品，属性可选性仍需真实业务确认。",
    "legend": "采用 ER 基数：|| 恰一，o{ 零至多；数量来自虚构案例明确设定。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-logical-data-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-logical-data-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-logical-data-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
