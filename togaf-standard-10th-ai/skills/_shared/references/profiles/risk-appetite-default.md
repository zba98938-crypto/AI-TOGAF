# 风险偏好

`profile_id`: risk-appetite-default；`artifact_id`: risk-appetite；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.1.3。

## 构图与定义状态

表示族：`assessment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：risk_appetite。关系类型：。

```json
{
  "entities": {
    "risk_appetite": [
      "scope",
      "impact_scale",
      "likelihood_scale",
      "acceptance_boundary",
      "approval_authority"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 风险偏好不是一条任意高低分线，批准状态需要证据
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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
      "id": "risk-appetite-default-record",
      "type": "risk_appetite",
      "name": "风险偏好：订单范围记录",
      "attributes": {
        "scope": "虚构星河零售：在线下单至仓库发运",
        "impact_scale": "低／中／高，按履约中断与合同影响判断",
        "likelihood_scale": "罕见／可能／频繁，需事故与测试证据支持",
        "acceptance_boundary": "不接受无责任归属且无恢复方案的高履约影响风险",
        "approval_authority": "虚构风险委员会，当前未批准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-risk-appetite-default",
    "artifact_id": "risk-appetite",
    "profile_id": "risk-appetite-default",
    "title": "风险偏好／虚构案例",
    "entity_ids": [
      "risk-appetite-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile risk-appetite-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile risk-appetite-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
