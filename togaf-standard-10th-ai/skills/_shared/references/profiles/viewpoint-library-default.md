# 云帆物流视角库

`profile_id`: viewpoint-library-default；`artifact_id`: viewpoint-library；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G184 §8.2–8.4；G186 §6.3.1、§9.1.3、附录C表C-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "viewpoint-library-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "正文工作产品的字段表；不冒称原图复刻。reference/adaptive均保留全部列语义。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:viewpoint。关系类型：。

```json
{
  "entities": {
    "guide:viewpoint": [
      "concern",
      "stakeholders",
      "decision",
      "construction",
      "required_information",
      "source_models",
      "view_ids",
      "gaps",
      "selection_reason"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 视角定义构造规范，view_id标识具体实例，两者不混同
- 每项授权关注点都有所需信息及构造规则
- 附录C是空白参考库，填入内容是项目分析而非原指南答案

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-viewpoint-library-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：viewpoints",
      "locator": "examples/addenda/governance/raw-business-materials.json#viewpoints"
    }
  ],
  "entities": [
    {
      "id": "viewpoint-library-default-1",
      "type": "guide:viewpoint",
      "name": "组合成本与价值",
      "attributes": {
        "concern": "价值、变更成本、信心",
        "stakeholders": [
          "财务负责人"
        ],
        "decision": "是否为T1拨款",
        "construction": "按工作包列三年成本和同单位月节省，单列区间与假设，不把成本直接当效用评分",
        "required_information": [
          "工作包/差距",
          "成本币种与期间",
          "工时单位、期间、范围",
          "不确定性来源"
        ],
        "source_models": [
          "model-budget-v2"
        ],
        "view_ids": [
          "v-budget-options-T1"
        ],
        "gaps": [
          "measure.uncertainty尚缺，不能形成确定投资结论"
        ],
        "selection_reason": "VP-01需要同口径预算比较"
      },
      "evidence": [
        "src-viewpoint-library-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "viewpoint-library-default-2",
      "type": "guide:viewpoint",
      "name": "过渡可运营",
      "attributes": {
        "concern": "可行性、可靠性、控制",
        "stakeholders": [
          "运营负责人"
        ],
        "decision": "T1是否可独立上线",
        "construction": "逐T1业务场景映射人员/流程/应用/数据、依赖和回退证据",
        "required_information": [
          "T1范围",
          "进入退出条件",
          "恢复/回退演练",
          "关键外部依赖"
        ],
        "source_models": [
          "model-transition-v2"
        ],
        "view_ids": [
          "v-operability-T1"
        ],
        "gaps": [],
        "selection_reason": "VP-02明确暂停T2仍须发运"
      },
      "evidence": [
        "src-viewpoint-library-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "viewpoint-library-default-3",
      "type": "guide:viewpoint",
      "name": "签收信息用途与控制",
      "attributes": {
        "concern": "安全、控制、规格",
        "stakeholders": [
          "数据负责人"
        ],
        "decision": "签收信息用途是否被控制",
        "construction": "按信息用途关联使用服务、约束、控制和验证证据；使用/修改分别标明",
        "required_information": [
          "information.purpose",
          "uses/modifies",
          "control.test_evidence"
        ],
        "source_models": [
          "model-data-v2"
        ],
        "view_ids": [
          "v-data-purpose-T1"
        ],
        "gaps": [],
        "selection_reason": "VP-03要求可追溯使用范围"
      },
      "evidence": [
        "src-viewpoint-library-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-viewpoint-library-default",
    "artifact_id": "viewpoint-library",
    "profile_id": "viewpoint-library-default",
    "title": "云帆物流视角库",
    "entity_ids": [
      "viewpoint-library-default-1",
      "viewpoint-library-default-2",
      "viewpoint-library-default-3"
    ],
    "relationship_ids": [],
    "analysis": "从VP-01/02/03提取三组决策与关注点，复用成本/过渡/信息模型；成本缺少不确定性资料，预算视图只能作为待补草稿。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "viewpoints"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile viewpoint-library-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile viewpoint-library-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
