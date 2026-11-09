# 安全资源计划

ID：`security-resource-plan`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.1.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构工作需要哪些安全与风险人员？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 架构工作需要哪些安全与风险人员？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- role
- authority
- capacity

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：security_resource。

```json
{
  "security_resource": [
    "role",
    "authority",
    "capacity",
    "availability",
    "engagement"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "role": {
    "meaning": "承担职责的角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "authority": {
    "meaning": "决策或数据权威及授权范围",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "capacity": {
    "meaning": "可投入的资源容量",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "availability": {
    "meaning": "指定期间可用资源",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "engagement": {
    "meaning": "参与方式与节奏",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从范围和高风险关注点识别能力需求
2. 比较现有安全支持与专职投入
3. 明确角色授权
4. 安排参与与能力缺口措施

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 资源计划不等于把所有安全职责交给一位架构师
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 资源计划不等于把所有安全职责交给一位架构师


## 视图和交付物

- [安全资源计划](../profiles/security-resource-plan-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「安全资源计划」给出：资源计划不等于把所有安全职责交给一位架构师",
    "expected": "missing-evidence",
    "why": "资源计划不等于把所有安全职责交给一位架构师"
  },
  "modification_example": {
    "change": "在「安全资源计划」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "security-resource-plan-default-record",
      "type": "security_resource",
      "name": "安全资源计划：订单范围记录",
      "attributes": {
        "role": "虚构安全架构师",
        "authority": "虚构订单案例中需验证的决策或数据权威及授权范围",
        "capacity": "虚构订单案例中需验证的可投入的资源容量",
        "availability": 2,
        "engagement": "虚构订单案例中需验证的参与方式与节奏"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-security-resource-plan-default",
    "artifact_id": "security-resource-plan",
    "profile_id": "security-resource-plan-default",
    "title": "安全资源计划／虚构案例",
    "entity_ids": [
      "security-resource-plan-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact security-resource-plan --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
