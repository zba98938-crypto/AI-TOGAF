# 数字技术采用定位

ID：`digital-adoption-position`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §5.1；图5-2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

选择怎样的数字技术采用方式？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 选择怎样的数字技术采用方式？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- ubiquity
- velocity
- rationale

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：adoption_option。

```json
{
  "adoption_option": [
    "ubiquity",
    "velocity",
    "rationale",
    "scope",
    "tradeoffs"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "ubiquity": {
    "meaning": "数字技术采用的普及广度",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "velocity": {
    "meaning": "数字技术采用的速度",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rationale": {
    "meaning": "分析或选择的理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "tradeoffs": {
    "meaning": "已考虑的权衡",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 明确普及度与采用速度
2. 比较 ABCD 四种方式
3. 阐明选择理由和范围
4. 与就绪度结果结合

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- ABCD 不是由低到高的优劣或成熟度等级
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- ABCD 不是由低到高的优劣或成熟度等级


## 视图和交付物

- [数字技术采用定位](../profiles/digital-adoption-position-default.md)
- [ABCD 采用定位象限](../profiles/dtra-adoption-quadrant.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「数字技术采用定位」给出：ABCD 不是由低到高的优劣或成熟度等级",
    "expected": "missing-evidence",
    "why": "ABCD 不是由低到高的优劣或成熟度等级"
  },
  "modification_example": {
    "change": "在「数字技术采用定位」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "digital-adoption-position-default-A",
      "type": "adoption_option",
      "name": "先锋式",
      "attributes": {
        "ubiquity": "低",
        "velocity": "高",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "top-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-adoption-position-default-B",
      "type": "adoption_option",
      "name": "大爆炸式",
      "attributes": {
        "ubiquity": "高",
        "velocity": "高",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "top-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-adoption-position-default-C",
      "type": "adoption_option",
      "name": "凝聚式",
      "attributes": {
        "ubiquity": "高",
        "velocity": "低",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "bottom-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-adoption-position-default-D",
      "type": "adoption_option",
      "name": "谨慎式",
      "attributes": {
        "ubiquity": "低",
        "velocity": "低",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "bottom-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-digital-adoption-position-default",
    "artifact_id": "digital-adoption-position",
    "profile_id": "digital-adoption-position-default",
    "title": "数字技术采用定位／虚构案例",
    "entity_ids": [
      "digital-adoption-position-default-A",
      "digital-adoption-position-default-B",
      "digital-adoption-position-default-C",
      "digital-adoption-position-default-D"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact digital-adoption-position --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
