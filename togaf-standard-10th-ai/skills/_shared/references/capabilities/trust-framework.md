# 信任框架

ID：`trust-framework`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

谁基于什么条件信任谁？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 谁基于什么条件信任谁？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_basis
- legal_basis
- direction

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：goal, trust_party。

```json
{
  "trust_party": [
    "business_basis",
    "legal_basis",
    "direction",
    "conditions",
    "scope"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_basis": {
    "meaning": "信任所依据的业务关系",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "legal_basis": {
    "meaning": "信任所依据的法律协议",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "direction": {
    "meaning": "有向或双向关系的明确读法",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "conditions": {
    "meaning": "关系或规则成立的条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 识别业务关系各方
2. 记录业务法律与政策依据
3. 声明单向双向或不存在的信任
4. 限定条件与责任

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 数字证书可以传递既有信任，不能创造业务信任
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 数字证书可以传递既有信任，不能创造业务信任


## 视图和交付物

- [信任框架](../profiles/trust-framework-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「信任框架」给出：数字证书可以传递既有信任，不能创造业务信任",
    "expected": "missing-evidence",
    "why": "数字证书可以传递既有信任，不能创造业务信任"
  },
  "modification_example": {
    "change": "在「信任框架」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "trust-framework-default-record",
      "type": "trust_party",
      "name": "信任框架：订单范围记录",
      "attributes": {
        "business_basis": "承运商受托履行配送合同",
        "legal_basis": "虚构配送与数据处理协议",
        "direction": "零售商向承运商传递受限订单数据",
        "conditions": "仅限有合同与明确用途的订单处理",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "trust-framework-default-target",
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
      "id": "trust-framework-default-supports",
      "type": "traces_to",
      "source": "trust-framework-default-record",
      "target": "trust-framework-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-trust-framework-default",
    "artifact_id": "trust-framework",
    "profile_id": "trust-framework-default",
    "title": "信任框架／虚构案例",
    "entity_ids": [
      "trust-framework-default-record",
      "trust-framework-default-target"
    ],
    "relationship_ids": [
      "trust-framework-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact trust-framework --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
