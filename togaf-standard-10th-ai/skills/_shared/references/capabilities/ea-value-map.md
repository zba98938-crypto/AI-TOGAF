# EA 与企业价值地图

ID：`ea-value-map`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §13。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

EA 服务如何为企业创造价值？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- EA 服务如何为企业创造价值？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- service
- consumer
- business_outcome

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：ea_value, goal。

```json
{
  "ea_value": [
    "service",
    "consumer",
    "business_outcome",
    "measure",
    "contribution",
    "evidence"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "service": {
    "meaning": "服务对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "consumer": {
    "meaning": "数据或消息消费方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_outcome": {
    "meaning": "企业业务成果",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "measure": {
    "meaning": "衡量贡献的指标",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "contribution": {
    "meaning": "贡献解释或假设",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 明确 EA 服务和业务受益者
2. 建立贡献假设
3. 选择度量与反馈
4. 检查业务周期对齐

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 相关性或贡献假设不能直接断言为确定收益因果
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 相关性或贡献假设不能直接断言为确定收益因果


## 视图和交付物

- [EA 与企业价值地图](../profiles/ea-value-map-default.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「EA 与企业价值地图」给出：相关性或贡献假设不能直接断言为确定收益因果",
    "expected": "missing-evidence",
    "why": "相关性或贡献假设不能直接断言为确定收益因果"
  },
  "modification_example": {
    "change": "在「EA 与企业价值地图」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "ea-value-map-default-record",
      "type": "ea_value",
      "name": "EA 与企业价值地图：订单范围记录",
      "attributes": {
        "service": "虚构订单案例中需验证的服务对象引用",
        "consumer": "虚构订单应用",
        "business_outcome": "提高履约可靠性",
        "measure": "虚构订单案例中需验证的衡量贡献的指标",
        "contribution": "架构通过明确信息责任和迁移约束提供贡献，因果待验证",
        "evidence": "虚构场景说明，非实测证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ea-value-map-default-target",
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
      "id": "ea-value-map-default-supports",
      "type": "traces_to",
      "source": "ea-value-map-default-record",
      "target": "ea-value-map-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-ea-value-map-default",
    "artifact_id": "ea-value-map",
    "profile_id": "ea-value-map-default",
    "title": "EA 与企业价值地图／虚构案例",
    "entity_ids": [
      "ea-value-map-default-record",
      "ea-value-map-default-target"
    ],
    "relationship_ids": [
      "ea-value-map-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact ea-value-map --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
