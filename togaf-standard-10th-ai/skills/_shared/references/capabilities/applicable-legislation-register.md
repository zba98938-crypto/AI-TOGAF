# 适用法律法规登记册

ID：`applicable-legislation-register`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.6。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些法规适用于本次架构范围？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些法规适用于本次架构范围？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- jurisdiction
- version
- applicability

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：legal_obligation。

```json
{
  "legal_obligation": [
    "jurisdiction",
    "version",
    "applicability",
    "business_function",
    "data_scope",
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
  "jurisdiction": {
    "meaning": "适用司法辖区",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "version": {
    "meaning": "来源或规范版本",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "applicability": {
    "meaning": "适用性判据与判断理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_function": {
    "meaning": "业务功能引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "data_scope": {
    "meaning": "受条款影响的数据范围",
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

1. 识别功能数据和司法辖区
2. 记录适用条款与版本
3. 关联架构要求和责任
4. 安排法规变化复核

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 法规适用不能仅由系统部署地推断
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 法规适用不能仅由系统部署地推断


## 视图和交付物

- [适用法律法规登记册](../profiles/applicable-legislation-register-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「适用法律法规登记册」给出：法规适用不能仅由系统部署地推断",
    "expected": "missing-evidence",
    "why": "法规适用不能仅由系统部署地推断"
  },
  "modification_example": {
    "change": "在「适用法律法规登记册」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "applicable-legislation-register-default-record",
      "type": "legal_obligation",
      "name": "适用法律法规登记册：订单范围记录",
      "attributes": {
        "jurisdiction": "虚构项目适用辖区，需责任方核实",
        "version": "示例2026.1",
        "applicability": "本例订单功能处理客户联系信息",
        "business_function": "订单履约分析",
        "data_scope": "虚构订单案例中需验证的受条款影响的数据范围",
        "owner": "虚构业务负责人"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-applicable-legislation-register-default",
    "artifact_id": "applicable-legislation-register",
    "profile_id": "applicable-legislation-register-default",
    "title": "适用法律法规登记册／虚构案例",
    "entity_ids": [
      "applicable-legislation-register-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact applicable-legislation-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
