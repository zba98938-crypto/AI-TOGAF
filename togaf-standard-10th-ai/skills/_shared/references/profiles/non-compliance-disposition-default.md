# 不合规影响与处置登记

`profile_id`: non-compliance-disposition-default；`artifact_id`: non-compliance-disposition；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G186 §15.2.2表15-2；G184 §6.2、§6.5。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "non-compliance-disposition-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "正文工作产品的字段表；不冒称原图复刻。reference/adaptive均保留全部列语义。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:noncompliance_disposition。关系类型：。

```json
{
  "entities": {
    "guide:noncompliance_disposition": [
      "subject",
      "violated_spec",
      "original_value_basis",
      "evidence_refs",
      "impact",
      "options",
      "recommendation",
      "decision_owner",
      "decision",
      "expiry",
      "review_date",
      "review_owner",
      "follow_up"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 永久豁免实质改变目标，必须转目标变更
- 更换指标/范围来获得通过会使评估失效
- 建议、批准和落实是三个独立事实

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-non-compliance-disposition-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：disposition",
      "locator": "examples/addenda/governance/raw-business-materials.json#disposition"
    }
  ],
  "entities": [
    {
      "id": "non-compliance-disposition-default-1",
      "type": "guide:noncompliance_disposition",
      "name": "签收延迟临时处置候选",
      "attributes": {
        "subject": "DELIVERY-API-v3 / TARGET-T1-v2",
        "violated_spec": "SPEC-60S",
        "original_value_basis": "城西站、同一业务日、签收可查询时延P95（秒）",
        "evidence_refs": [
          "NC-01",
          "NC-02"
        ],
        "impact": "93秒超过60秒，晚送达风险；样本只覆盖城西站，其他站影响未评估",
        "options": [
          {
            "action": "enforce",
            "impact": "10工作日修复，延后上线，保留60秒目标"
          },
          {
            "action": "temporary-waiver",
            "impact": "30日人工查询补偿，仍有晚送达风险；目标保持60秒"
          },
          {
            "action": "change-target",
            "impact": "若改为120秒必须重新分析客户影响并重走目标批准，当前无足够证据"
          }
        ],
        "recommendation": "temporary-waiver",
        "decision_owner": "运营、数据、财务授权利益相关者",
        "decision": "pending；尚不可执行",
        "expiry": "2026-12-01",
        "review_date": "2026-11-09",
        "review_owner": "运营负责人",
        "follow_up": "批准后方可开始豁免；每周一复评；到期未关闭重新升级，不永久续期"
      },
      "evidence": [
        "src-non-compliance-disposition-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-non-compliance-disposition-default",
    "artifact_id": "non-compliance-disposition",
    "profile_id": "non-compliance-disposition-default",
    "title": "不合规影响与处置登记",
    "entity_ids": [
      "non-compliance-disposition-default-1"
    ],
    "relationship_ids": [],
    "analysis": "沿原P95/城西站口径分析三项选择，建议有期限豁免；尚未获得授权批准，不能把建议写作已豁免。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "disposition"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile non-compliance-disposition-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile non-compliance-disposition-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
