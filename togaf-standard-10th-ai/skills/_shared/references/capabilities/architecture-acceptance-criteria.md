# 架构成果验收准则

ID：`architecture-acceptance-criteria`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G188 §3.1–3.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

怎样判断架构成果足以支持决策？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 怎样判断架构成果足以支持决策？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- deliverable
- criterion
- verification

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：acceptance_criterion。

```json
{
  "acceptance_criterion": [
    "deliverable",
    "criterion",
    "verification",
    "reviewer",
    "evidence",
    "status"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "deliverable": {
    "meaning": "架构交付物引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "criterion": {
    "meaning": "单项判断准则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "verification": {
    "meaning": "验证方法与验收证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "reviewer": {
    "meaning": "评审责任人或角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "status": {
    "meaning": "该条记录的工作状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从目标与关注点定义准则
2. 指定检验和评审责任
3. 记录证据及未决项
4. 区分移交批准和生成完成

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 工件不要求各自成为独立文档，数量不是验收目标
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 工件不要求各自成为独立文档，数量不是验收目标


## 视图和交付物

- [架构成果验收准则](../profiles/architecture-acceptance-criteria-default.md)

- [compliance-assessment](../deliverables/compliance-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构成果验收准则」给出：工件不要求各自成为独立文档，数量不是验收目标",
    "expected": "missing-evidence",
    "why": "工件不要求各自成为独立文档，数量不是验收目标"
  },
  "modification_example": {
    "change": "在「架构成果验收准则」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "architecture-acceptance-criteria-default-record",
      "type": "acceptance_criterion",
      "name": "架构成果验收准则：订单范围记录",
      "attributes": {
        "deliverable": "本例架构定义文档",
        "criterion": "虚构订单案例中需验证的单项判断准则",
        "verification": "复演两笔虚构订单并核对库存付款和发运状态",
        "reviewer": "虚构业务与架构评审组",
        "evidence": "虚构场景说明，非实测证据",
        "status": "虚构订单案例中需验证的该条记录的工作状态"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-architecture-acceptance-criteria-default",
    "artifact_id": "architecture-acceptance-criteria",
    "profile_id": "architecture-acceptance-criteria-default",
    "title": "架构成果验收准则／虚构案例",
    "entity_ids": [
      "architecture-acceptance-criteria-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-acceptance-criteria --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
