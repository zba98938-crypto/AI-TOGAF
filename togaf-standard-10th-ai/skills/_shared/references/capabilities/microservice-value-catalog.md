# 微服务价值与资源目录

ID：`microservice-value-catalog`。主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G21I §7；G21I §11.3、§12.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

已实现和计划服务贡献什么价值？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 已实现和计划服务贡献什么价值？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_function
- value
- planned_state

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：microservice, ops:msa_value_resource。

```json
{
  "microservice": [
    "business_function",
    "value",
    "planned_state",
    "development_resources",
    "operations_resources",
    "owner"
  ],
  "ops:msa_value_resource": [
    "service_status",
    "ABF",
    "value",
    "development_resources",
    "operations_resources",
    "owner",
    "work_package_ref",
    "architecture_state_ref",
    "evidence_detail",
    "cost_and_return",
    "gap"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_function": {
    "meaning": "业务功能引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "value": {
    "meaning": "度量值或业务价值陈述，依语境声明",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "planned_state": {
    "meaning": "已实现或计划等实现状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "development_resources": {
    "meaning": "开发资源投入",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "operations_resources": {
    "meaning": "运营资源投入",
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

1. 盘点服务及状态
2. 关联业务功能与价值
3. 记录开发运营资源
4. 评估重复与持续收益
5. 区分已实现和计划服务
6. 逐服务确认一个ABF与业务价值
7. 开发/运营及已分配/计划四格分开记录单位时段
8. 关联工作包及命名过渡，检查运营计划缺口
9. 成本或ROI规则未提供则不计算

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 计划服务不能标为已交付，服务数量不等于业务价值
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 计划服务不能标为已交付，服务数量不等于业务价值


## 视图和交付物

- [微服务价值与资源目录](../profiles/microservice-value-catalog-default.md)
- [微服务业务价值与开发运营资源](../profiles/msa-value-resource-evidence.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「微服务价值与资源目录」给出：计划服务不能标为已交付，服务数量不等于业务价值",
    "expected": "missing-evidence",
    "why": "计划服务不能标为已交付，服务数量不等于业务价值"
  },
  "modification_example": {
    "change": "在「微服务价值与资源目录」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "microservice-value-catalog-default-record",
      "type": "microservice",
      "name": "微服务价值与资源目录：订单范围记录",
      "attributes": {
        "business_function": "订单履约分析",
        "value": 2,
        "planned_state": "计划，尚未交付",
        "development_resources": "虚构跨职能团队一组",
        "operations_resources": "虚构运营责任人，容量待估算",
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
    "id": "v-microservice-value-catalog-default",
    "artifact_id": "microservice-value-catalog",
    "profile_id": "microservice-value-catalog-default",
    "title": "微服务价值与资源目录／虚构案例",
    "entity_ids": [
      "microservice-value-catalog-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact microservice-value-catalog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
