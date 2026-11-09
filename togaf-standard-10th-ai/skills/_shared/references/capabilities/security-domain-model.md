# 安全域模型

ID：`security-domain-model`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些资产受同一安全策略管辖？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些资产受同一安全策略管辖？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- policy_authority
- classification
- assets

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：application, security_domain。

```json
{
  "security_domain": [
    "policy_authority",
    "classification",
    "assets",
    "boundary",
    "federation"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "policy_authority": {
    "meaning": "安全域内的政策制定与执行权威",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "classification": {
    "meaning": "安全分类标签",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "assets": {
    "meaning": "受该政策或域管辖的资产引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "boundary": {
    "meaning": "内外边界的含义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "federation": {
    "meaning": "跨组织联邦范围和协议",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 按相同安全属性与政策分组资产
2. 界定域内政策权威
3. 识别外部责任交换
4. 评估联邦合同与共同对象

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域


## 视图和交付物

- [安全域模型](../profiles/security-domain-model-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「安全域模型」给出：视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域",
    "expected": "missing-evidence",
    "why": "视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域"
  },
  "modification_example": {
    "change": "在「安全域模型」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "security-domain-model-default-domain",
      "type": "security_domain",
      "name": "安全域模型：订单范围",
      "attributes": {
        "policy_authority": "虚构信息安全负责人",
        "classification": "内部受限：包含客户与订单信息",
        "assets": "虚构订单案例中需验证的受该政策或域管辖的资产引用",
        "boundary": "企业内订单服务与外部承运商接口",
        "federation": "虚构订单案例中需验证的跨组织联邦范围和协议"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-domain-model-default-application",
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
      "id": "security-domain-model-default-mapping",
      "type": "traces_to",
      "source": "security-domain-model-default-domain",
      "target": "security-domain-model-default-application",
      "label": "本工作产品所涉及的实现对象；不从邻近推断安全授权",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-security-domain-model-default",
    "artifact_id": "security-domain-model",
    "profile_id": "security-domain-model-default",
    "title": "安全域模型／虚构案例",
    "entity_ids": [
      "security-domain-model-default-domain",
      "security-domain-model-default-application"
    ],
    "relationship_ids": [
      "security-domain-model-default-mapping"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact security-domain-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
