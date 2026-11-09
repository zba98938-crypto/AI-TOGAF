# 安全蓝图

`profile_id`: security-blueprint-default；`artifact_id`: security-blueprint；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.2。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, security_component。关系类型：traces_to。

```json
{
  "entities": {
    "security_component": [
      "concern",
      "principle",
      "risk",
      "service",
      "scope"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 愿景蓝图不等于已完成的技术方案或已运行控制
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
      "id": "security-blueprint-default-domain",
      "type": "security_component",
      "name": "安全蓝图：订单范围",
      "attributes": {
        "concern": "订单完整性与履约连续性",
        "principle": "虚构订单案例中需验证的适用原则引用",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "service": "虚构订单案例中需验证的服务对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-blueprint-default-application",
      "type": "application",
      "name": "订单应用",
      "attributes": {
        "definition": "本例待治理或支撑的实现应用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "security-blueprint-default-mapping",
      "type": "traces_to",
      "source": "security-blueprint-default-domain",
      "target": "security-blueprint-default-application",
      "label": "本工作产品所涉及的实现对象；不从邻近推断安全授权",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-security-blueprint-default",
    "artifact_id": "security-blueprint",
    "profile_id": "security-blueprint-default",
    "title": "安全蓝图／虚构案例",
    "entity_ids": [
      "security-blueprint-default-domain",
      "security-blueprint-default-application"
    ],
    "relationship_ids": [
      "security-blueprint-default-mapping"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-blueprint-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-blueprint-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
