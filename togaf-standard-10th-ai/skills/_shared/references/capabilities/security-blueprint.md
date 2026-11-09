# 安全蓝图

ID：`security-blueprint`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

愿景如何使利益相关者确信风险可接受？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 愿景如何使利益相关者确信风险可接受？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- concern
- principle
- risk

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：application, security_component。

```json
{
  "security_component": [
    "concern",
    "principle",
    "risk",
    "service",
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
  "concern": {
    "meaning": "利益相关者的具体关注点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "principle": {
    "meaning": "适用原则引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "risk": {
    "meaning": "风险对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "service": {
    "meaning": "服务对象引用",
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

1. 收集安全关注点
2. 建立业务风险和原则语境
3. 选择高层安全服务与边界
4. 追溯到后续阶段细化要求

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 愿景蓝图不等于已完成的技术方案或已运行控制
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 愿景蓝图不等于已完成的技术方案或已运行控制


## 视图和交付物

- [安全蓝图](../profiles/security-blueprint-default.md)
- [跨域安全关注点](../profiles/security-cross-domain.md)
- [安全与ADM概念整合](../profiles/security-adm-concept-map.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「安全蓝图」给出：愿景蓝图不等于已完成的技术方案或已运行控制",
    "expected": "missing-evidence",
    "why": "愿景蓝图不等于已完成的技术方案或已运行控制"
  },
  "modification_example": {
    "change": "在「安全蓝图」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "security-blueprint-default-domain",
      "type": "security_component",
      "name": "安全蓝图：订单范围",
      "attributes": {
        "concern": "订单完整性与履约连续性",
        "principle": "虚构订单案例中需验证的适用原则引用",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "service": "虚构订单案例中需验证的服务对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-blueprint-default-application",
      "type": "application",
      "name": "订单应用",
      "attributes": {
        "definition": "本例待治理或支撑的实现应用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "security-blueprint-default-mapping",
      "type": "traces_to",
      "source": "security-blueprint-default-domain",
      "target": "security-blueprint-default-application",
      "label": "本工作产品所涉及的实现对象；不从邻近推断安全授权",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-security-blueprint-default",
    "artifact_id": "security-blueprint",
    "profile_id": "security-blueprint-default",
    "title": "安全蓝图／虚构案例",
    "entity_ids": [
      "security-blueprint-default-domain",
      "security-blueprint-default-application"
    ],
    "relationship_ids": [
      "security-blueprint-default-mapping"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact security-blueprint --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
