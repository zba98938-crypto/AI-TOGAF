# 元数据模型

ID：`metadata-model`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-5、4-6。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些元数据对象和关系足以支撑需求？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些元数据对象和关系足以支撑需求？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- metadata_category
- definition
- attributes

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：metadata_asset。

```json
{
  "metadata_asset": [
    "metadata_category",
    "definition",
    "identifier",
    "domain",
    "owner"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "metadata_category": {
    "meaning": "业务、技术或运营元数据类别",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "attributes": {
    "meaning": "实体的属性定义清单",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "identifier": {
    "meaning": "对象标识与唯一性规则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "domain": {
    "meaning": "属性允许的值域或业务域",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从业务需求识别关键资产
2. 建立业务技术运营分类
3. 细化属性域和标识
4. 核查资产关联与生命周期

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 图4-5的参考资产不是每个项目必须全选的模型
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 图4-5的参考资产不是每个项目必须全选的模型


## 视图和交付物

- [元数据模型](../profiles/metadata-model-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「元数据模型」给出：图4-5的参考资产不是每个项目必须全选的模型",
    "expected": "missing-evidence",
    "why": "图4-5的参考资产不是每个项目必须全选的模型"
  },
  "modification_example": {
    "change": "在「元数据模型」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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
      "id": "metadata-model-default-term",
      "type": "metadata_asset",
      "name": "订单业务术语",
      "attributes": {
        "metadata_category": "业务元数据",
        "definition": "客户的商品购买与交付承诺",
        "identifier": "TERM-ORDER",
        "domain": "订单业务语义",
        "owner": "订单业务所有者"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-model-default-field",
      "type": "metadata_asset",
      "name": "订单状态字段",
      "attributes": {
        "metadata_category": "技术元数据",
        "definition": "承载订单状态的字段描述",
        "identifier": "FIELD-ORDER-STATUS",
        "domain": "已确认、已发运、已取消",
        "owner": "订单应用维护团队"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "metadata-model-default-maps",
      "type": "traces_to",
      "source": "metadata-model-default-term",
      "target": "metadata-model-default-field",
      "label": "业务术语映射技术字段；不是数据值副本",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-metadata-model-default",
    "artifact_id": "metadata-model",
    "profile_id": "metadata-model-default",
    "title": "元数据模型／虚构案例",
    "entity_ids": [
      "metadata-model-default-term",
      "metadata-model-default-field"
    ],
    "relationship_ids": [
      "metadata-model-default-maps"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact metadata-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
