# 主要与支持活动价值链

`profile_id`: porter-value-chain；`artifact_id`: value-chain-diagram；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G178/figA-1。

## 构图与定义状态

表示族：`value-chain`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G178/figA-1",
  "layout_notes": "四类支持活动覆盖五类主要活动；Margin不表示最后阶段",
  "review_status": "source-located-awaiting-template-validation",
  "margin": "价值减成本所得的经济贡献；本例未提供金额，不能计算利润",
  "verification_evidence": "reviews/source-verification/porter-value-chain.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：value_chain_activity。关系类型：。

```json
{
  "entities": {
    "value_chain_activity": [
      "category",
      "definition",
      "contribution"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 四类支持活动覆盖五类主要活动；Margin不表示最后阶段

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
      "id": "porter-value-chain-support0",
      "type": "value_chain_activity",
      "name": "基础设施",
      "attributes": {
        "category": "支持",
        "definition": "支撑价值创造的基础设施",
        "contribution": "支撑主要活动并管理间接成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-support1",
      "type": "value_chain_activity",
      "name": "人力资源管理",
      "attributes": {
        "category": "支持",
        "definition": "支撑价值创造的人力资源管理",
        "contribution": "支撑主要活动并管理间接成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-support2",
      "type": "value_chain_activity",
      "name": "技术开发",
      "attributes": {
        "category": "支持",
        "definition": "支撑价值创造的技术开发",
        "contribution": "支撑主要活动并管理间接成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-support3",
      "type": "value_chain_activity",
      "name": "采购",
      "attributes": {
        "category": "支持",
        "definition": "支撑价值创造的采购",
        "contribution": "支撑主要活动并管理间接成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-primary0",
      "type": "value_chain_activity",
      "name": "内部物流",
      "attributes": {
        "category": "主要",
        "definition": "面向价值创造的内部物流",
        "contribution": "形成客户价值并发生相应成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-primary1",
      "type": "value_chain_activity",
      "name": "运营",
      "attributes": {
        "category": "主要",
        "definition": "面向价值创造的运营",
        "contribution": "形成客户价值并发生相应成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-primary2",
      "type": "value_chain_activity",
      "name": "外部物流",
      "attributes": {
        "category": "主要",
        "definition": "面向价值创造的外部物流",
        "contribution": "形成客户价值并发生相应成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-primary3",
      "type": "value_chain_activity",
      "name": "市场与销售",
      "attributes": {
        "category": "主要",
        "definition": "面向价值创造的市场与销售",
        "contribution": "形成客户价值并发生相应成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "porter-value-chain-primary4",
      "type": "value_chain_activity",
      "name": "服务",
      "attributes": {
        "category": "主要",
        "definition": "面向价值创造的服务",
        "contribution": "形成客户价值并发生相应成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-porter-value-chain",
    "artifact_id": "value-chain-diagram",
    "profile_id": "porter-value-chain",
    "title": "主要与支持活动价值链／虚构案例",
    "entity_ids": [
      "porter-value-chain-support0",
      "porter-value-chain-support1",
      "porter-value-chain-support2",
      "porter-value-chain-support3",
      "porter-value-chain-primary0",
      "porter-value-chain-primary1",
      "porter-value-chain-primary2",
      "porter-value-chain-primary3",
      "porter-value-chain-primary4"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile porter-value-chain --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile porter-value-chain --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
