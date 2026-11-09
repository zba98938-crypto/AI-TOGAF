# 概念数据图（兼容默认）

`profile_id`: compat-conceptual-data-diagram；`artifact_id`: conceptual-data-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G21B。

## 构图与定义状态

表示族：`er`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-conceptual-data-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_entity。关系类型：data_association。

```json
{
  "entities": {
    "data_entity": [
      "definition",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 未知基数保留待核实且不用 ER 断言绘制
- 概念模型不强制主外键

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
      "id": "data-customer",
      "type": "data_entity",
      "name": "客户",
      "attributes": {
        "definition": "可识别的购买主体数据",
        "owner": "客户数据负责人",
        "classification": "受限联系信息",
        "retention": "示例：合同完成后按已确认政策处置",
        "authority": "客户主数据服务",
        "latency": "待确认",
        "delivery_mode": "受控查询",
        "purpose": "受控订单履约或已声明分析"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-order",
      "type": "data_entity",
      "name": "订单",
      "attributes": {
        "definition": "购买商品和履约承诺的数据记录",
        "owner": "销售负责人",
        "classification": "内部交易数据",
        "retention": "依据经确认的业务政策",
        "authority": "订单应用",
        "latency": "近实时",
        "delivery_mode": "业务事件",
        "purpose": "受控订单履约或已声明分析"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "data-assoc",
      "type": "data_association",
      "source": "data-customer",
      "target": "data-order",
      "label": "客户提交订单",
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
    "id": "v-conceptual-data-diagram",
    "artifact_id": "conceptual-data-diagram",
    "title": "概念数据图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "conceptual",
      "evolution": "target"
    },
    "entity_ids": [
      "data-customer",
      "data-order"
    ],
    "relationship_ids": [
      "data-assoc"
    ],
    "analysis": "本虚构场景明确：一个订单属于一个客户；一个客户可以有零至多个订单。基数来自案例设定，不推广到其他业务。",
    "legend": "采用 ER 基数：|| 恰一，o{ 零至多；数量来自虚构案例明确设定。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-conceptual-data-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-conceptual-data-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-conceptual-data-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
