# 业务与技术资产关联

ID：`business-technical-asset-mapping`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §3、§4.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

业务概念落在哪些技术资产上？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 业务概念落在哪些技术资产上？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- metadata_category
- business_meaning
- technical_locator

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：goal, metadata_asset。

```json
{
  "metadata_asset": [
    "metadata_category",
    "business_meaning",
    "technical_locator",
    "owner",
    "source"
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
  "business_meaning": {
    "meaning": "业务概念的含义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "technical_locator": {
    "meaning": "技术资产定位符",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "source": {
    "meaning": "该条内容的输入来源",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 识别业务与技术资产身份
2. 定义关联类型与粒度
3. 记录源头和转换
4. 验证覆盖与多义映射

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 概念相近不等于同一资产，关联不是自动实现关系
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 概念相近不等于同一资产，关联不是自动实现关系


## 视图和交付物

- [业务与技术资产关联](../profiles/business-technical-asset-mapping-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务与技术资产关联」给出：概念相近不等于同一资产，关联不是自动实现关系",
    "expected": "missing-evidence",
    "why": "概念相近不等于同一资产，关联不是自动实现关系"
  },
  "modification_example": {
    "change": "在「业务与技术资产关联」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "business-technical-asset-mapping-default-record",
      "type": "metadata_asset",
      "name": "业务与技术资产关联：订单范围记录",
      "attributes": {
        "metadata_category": "业务元数据",
        "business_meaning": "客户购买的产品、数量及履约承诺",
        "technical_locator": "虚构订单应用的订单实体（示意）",
        "owner": "虚构业务负责人",
        "source": "虚构业务场景与需求材料"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-technical-asset-mapping-default-target",
      "type": "goal",
      "name": "可靠履约",
      "attributes": {
        "definition": "在承诺时间内交付且状态可追溯"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "business-technical-asset-mapping-default-supports",
      "type": "traces_to",
      "source": "business-technical-asset-mapping-default-record",
      "target": "business-technical-asset-mapping-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-technical-asset-mapping-default",
    "artifact_id": "business-technical-asset-mapping",
    "profile_id": "business-technical-asset-mapping-default",
    "title": "业务与技术资产关联／虚构案例",
    "entity_ids": [
      "business-technical-asset-mapping-default-record",
      "business-technical-asset-mapping-default-target"
    ],
    "relationship_ids": [
      "business-technical-asset-mapping-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-technical-asset-mapping --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
