# EA 团队容量计划

ID：`ea-team-capacity-plan`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §13。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

团队容量能否支撑所选架构服务？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 团队容量能否支撑所选架构服务？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- role
- skill
- demand

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：ea_capacity。

```json
{
  "ea_capacity": [
    "role",
    "skill",
    "demand",
    "availability",
    "allocation",
    "period"
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
  "skill": {
    "meaning": "技能项或类别",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "demand": {
    "meaning": "指定期间的资源需求",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "availability": {
    "meaning": "指定期间可用资源",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "allocation": {
    "meaning": "资源分配",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "period": {
    "meaning": "分析期间",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 估计服务需求与参与节奏
2. 盘点角色技能和可用量
3. 比较供需
4. 安排招聘发展或裁剪

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 人数不等于可用容量，技能熟练度不等于工时
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 人数不等于可用容量，技能熟练度不等于工时


## 视图和交付物

- [EA 团队容量计划](../profiles/ea-team-capacity-plan-default.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「EA 团队容量计划」给出：人数不等于可用容量，技能熟练度不等于工时",
    "expected": "missing-evidence",
    "why": "人数不等于可用容量，技能熟练度不等于工时"
  },
  "modification_example": {
    "change": "在「EA 团队容量计划」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "ea-team-capacity-plan-default-step1",
      "type": "ea_capacity",
      "name": "EA 团队容量计划：准备",
      "attributes": {
        "role": "虚构安全架构师",
        "skill": "数据与应用架构追溯",
        "demand": 2,
        "availability": 2,
        "allocation": "按已声明的订单工作负载比例分摊",
        "period": "2026年第四季度",
        "order": 1,
        "start": "2026-11-02",
        "end": "2026-11-13"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ea-team-capacity-plan-default-step2",
      "type": "ea_capacity",
      "name": "EA 团队容量计划：验证",
      "attributes": {
        "role": "虚构安全架构师",
        "skill": "数据与应用架构追溯",
        "demand": 2,
        "availability": 2,
        "allocation": "按已声明的订单工作负载比例分摊",
        "period": "2026年第四季度",
        "order": 2,
        "start": "2026-11-16",
        "end": "2026-11-27"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "ea-team-capacity-plan-default-dependency",
      "type": "traces_to",
      "source": "ea-team-capacity-plan-default-step2",
      "target": "ea-team-capacity-plan-default-step1",
      "label": "后项以准备结果为进入条件；工期是虚构演示",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-ea-team-capacity-plan-default",
    "artifact_id": "ea-team-capacity-plan",
    "profile_id": "ea-team-capacity-plan-default",
    "title": "EA 团队容量计划／虚构案例",
    "entity_ids": [
      "ea-team-capacity-plan-default-step1",
      "ea-team-capacity-plan-default-step2"
    ],
    "relationship_ids": [
      "ea-team-capacity-plan-default-dependency"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact ea-team-capacity-plan --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
