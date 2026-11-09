# 互操作性评估

ID：`interoperability-assessment`。主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G217 §4.4.4、附录C.4表C-5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

跨系统和组织交换能否满足业务要求？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 跨系统和组织交换能否满足业务要求？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- parties
- interaction
- information

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：interoperability_issue。

```json
{
  "interoperability_issue": [
    "parties",
    "interaction",
    "information",
    "protocol",
    "constraint",
    "evidence"
  ],
  "equipment": [
    "equipment_class",
    "work_center_ref",
    "criticality",
    "maintenance_plan_ref"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "parties": {
    "meaning": "交互各方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "interaction": {
    "meaning": "跨方交互及其目的",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "information": {
    "meaning": "被使用或修改的信息引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "protocol": {
    "meaning": "交互协议",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "constraint": {
    "meaning": "适用约束",
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

1. 界定交互各方及业务目的
2. 检查信息含义接口协议
3. 分析组织与技术约束
4. 提出证据支持的改进

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 网络连通不能证明语义和业务互操作
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 网络连通不能证明语义和业务互操作


## 视图和交付物

- [互操作性评估](../profiles/interoperability-assessment-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「互操作性评估」给出：网络连通不能证明语义和业务互操作",
    "expected": "missing-evidence",
    "why": "网络连通不能证明语义和业务互操作"
  },
  "modification_example": {
    "change": "在「互操作性评估」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "interoperability-assessment-default-record",
      "type": "interoperability_issue",
      "name": "互操作性评估：订单范围记录",
      "attributes": {
        "parties": "虚构订单案例中需验证的交互各方",
        "interaction": "虚构订单案例中需验证的跨方交互及其目的",
        "information": "订单和发运信息",
        "protocol": "项目约定的受控API",
        "constraint": "虚构订单案例中需验证的适用约束",
        "evidence": "虚构场景说明，非实测证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-interoperability-assessment-default",
    "artifact_id": "interoperability-assessment",
    "profile_id": "interoperability-assessment-default",
    "title": "互操作性评估／虚构案例",
    "entity_ids": [
      "interoperability-assessment-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact interoperability-assessment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
