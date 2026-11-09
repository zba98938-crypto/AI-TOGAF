# 业务场景文档

ID：`business-scenario-document`。主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G176 §3–4；G176 §7–§11。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构究竟为谁解决什么业务问题？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 架构究竟为谁解决什么业务问题？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- problem
- environment
- objectives

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：scenario。

```json
{
  "scenario": [
    "problem",
    "environment",
    "objectives",
    "human_actors",
    "computer_actors",
    "requirements"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "problem": {
    "meaning": "待解决问题及其业务证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "environment": {
    "meaning": "业务与技术环境",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "objectives": {
    "meaning": "期望业务结果及可衡量目的",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "human_actors": {
    "meaning": "人的参与者与角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "computer_actors": {
    "meaning": "计算机参与者与责任",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "requirements": {
    "meaning": "架构要求引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 形成并验证前提
2. 采集归一化问题目标参与者环境
3. 建立业务与技术模型
4. 反复评审并记录需求
5. 用business-scenario-checklist-record跟踪各步骤清单与角色
6. 用smart-objective-assessment把目的做成SMART

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 业务场景不能由单张用例图替代，也不能预设技术答案
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯
- 业务场景各步骤清单和SMART目的分别记录，勾选完成不等于场景被接受

- 业务场景不能由单张用例图替代，也不能预设技术答案


## 视图和交付物

- [业务场景文档](../profiles/business-scenario-document-default.md)

- [architecture-vision](../deliverables/architecture-vision.md)
- [statement-of-work](../deliverables/statement-of-work.md)
- [business-drivers](../deliverables/business-drivers.md)
- [request-for-architecture-work](../deliverables/request-for-architecture-work.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务场景文档」给出：业务场景不能由单张用例图替代，也不能预设技术答案",
    "expected": "missing-evidence",
    "why": "业务场景不能由单张用例图替代，也不能预设技术答案"
  },
  "modification_example": {
    "change": "在「业务场景文档」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "business-scenario-document-default-record",
      "type": "scenario",
      "name": "业务场景文档：订单范围记录",
      "attributes": {
        "problem": "订单信息割裂使发运状态无法及时通知客户",
        "environment": "虚构在线商店、仓库和承运商",
        "objectives": "一个工作日内完成发运并通知客户",
        "human_actors": "客户、仓库操作员、客服",
        "computer_actors": "在线商店、订单应用、仓库应用",
        "requirements": "虚构订单案例中需验证的架构要求引用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-scenario-document-default",
    "artifact_id": "business-scenario-document",
    "profile_id": "business-scenario-document-default",
    "title": "业务场景文档／虚构案例",
    "entity_ids": [
      "business-scenario-document-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-scenario-document --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
