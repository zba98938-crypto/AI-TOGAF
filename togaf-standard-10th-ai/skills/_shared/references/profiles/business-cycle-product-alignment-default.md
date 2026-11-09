# 业务周期与工作产品时点

`profile_id`: business-cycle-product-alignment-default；`artifact_id`: business-cycle-product-alignment；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §4.3.2、§10.3、§11.4；G186 §4、§8.1、§11.2、§14。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "business-cycle-product-alignment-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "正文工作产品的字段表；不冒称原图复刻。reference/adaptive均保留全部列语义。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:cycle_product。关系类型：。

```json
{
  "entities": {
    "guide:cycle_product": [
      "business_event",
      "decision",
      "consumer",
      "required_by",
      "planned",
      "actual",
      "product_view_refs",
      "dependency",
      "status",
      "recovery_action",
      "rule_source"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- ADM阶段顺序不决定业务消费时点
- 30天/季度是G186的实践建议，项目日期必须由实际日历确认
- 计划早于期限不证明实际已按时交付

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-business-cycle-product-alignment-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：cycle",
      "locator": "examples/addenda/governance/raw-business-materials.json#cycle"
    }
  ],
  "entities": [
    {
      "id": "business-cycle-product-alignment-default-1",
      "type": "guide:cycle_product",
      "name": "2027预算选项",
      "attributes": {
        "business_event": "2026-11-20预算会",
        "decision": "T1拨款",
        "consumer": "财务负责人",
        "required_by": "2026-11-13",
        "planned": "2026-11-16",
        "actual": "unknown",
        "product_view_refs": [
          "v-budget-options-T1"
        ],
        "dependency": "成本估算、不确定性说明与主题工作包",
        "status": "late：计划比消费期限晚3日",
        "recovery_action": "安排11月12日候选评审；若未能提供则预算结论明确缺口",
        "rule_source": "CY-01财务约定；日期不是TOGAF规定"
      },
      "evidence": [
        "src-business-cycle-product-alignment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-cycle-product-alignment-default-2",
      "type": "guide:cycle_product",
      "name": "项目拨款准备",
      "attributes": {
        "business_event": "2026-12-04项目拨款会",
        "decision": "范围/契约批准",
        "consumer": "PMO与发起人",
        "required_by": "2026-12-03",
        "planned": "2026-12-02",
        "actual": "unknown",
        "product_view_refs": [
          "v-contract-T1"
        ],
        "dependency": "预算、范围、依赖与规格",
        "status": "timely：计划早于期限1日，尚无实际交付证据",
        "recovery_action": "维持计划，核实前置输入",
        "rule_source": "CY-02及项目确认的会前1日要求"
      },
      "evidence": [
        "src-business-cycle-product-alignment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-cycle-product-alignment-default-3",
      "type": "guide:cycle_product",
      "name": "首月价值回顾",
      "attributes": {
        "business_event": "2027-02-10运营价值回顾",
        "decision": "继续T2或调整路线",
        "consumer": "组合负责人",
        "required_by": "2027-02-10",
        "planned": "2027-02-08",
        "actual": "unknown",
        "product_view_refs": [
          "v-value-realization-assessment-default"
        ],
        "dependency": "T1首月运营测量与比较基线",
        "status": "timely：计划早2日",
        "recovery_action": "锁定数据口径与责任，不能以G合规报告替代",
        "rule_source": "CY-03运营约定"
      },
      "evidence": [
        "src-business-cycle-product-alignment-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-cycle-product-alignment-default",
    "artifact_id": "business-cycle-product-alignment",
    "profile_id": "business-cycle-product-alignment-default",
    "title": "业务周期与工作产品时点",
    "entity_ids": [
      "business-cycle-product-alignment-default-1",
      "business-cycle-product-alignment-default-2",
      "business-cycle-product-alignment-default-3"
    ],
    "relationship_ids": [],
    "analysis": "把预算/拨款/价值回顾倒排到消费日期；发现组合选项计划迟3天，已有项目表未表达这一消费缺口，需调整。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "cycle"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-cycle-product-alignment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-cycle-product-alignment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
