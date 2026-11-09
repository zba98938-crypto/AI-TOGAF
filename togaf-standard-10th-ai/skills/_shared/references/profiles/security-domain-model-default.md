# 安全域模型

`profile_id`: security-domain-model-default；`artifact_id`: security-domain-model；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.2。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, security_domain。关系类型：traces_to。

```json
{
  "entities": {
    "security_domain": [
      "policy_authority",
      "classification",
      "assets",
      "boundary",
      "federation"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域
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
      "id": "security-domain-model-default-domain",
      "type": "security_domain",
      "name": "安全域模型：订单范围",
      "attributes": {
        "policy_authority": "虚构信息安全负责人",
        "classification": "内部受限：包含客户与订单信息",
        "assets": "虚构订单案例中需验证的受该政策或域管辖的资产引用",
        "boundary": "企业内订单服务与外部承运商接口",
        "federation": "虚构订单案例中需验证的跨组织联邦范围和协议"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-domain-model-default-application",
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
      "id": "security-domain-model-default-mapping",
      "type": "traces_to",
      "source": "security-domain-model-default-domain",
      "target": "security-domain-model-default-application",
      "label": "本工作产品所涉及的实现对象；不从邻近推断安全授权",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-security-domain-model-default",
    "artifact_id": "security-domain-model",
    "profile_id": "security-domain-model-default",
    "title": "安全域模型／虚构案例",
    "entity_ids": [
      "security-domain-model-default-domain",
      "security-domain-model-default-application"
    ],
    "relationship_ids": [
      "security-domain-model-default-mapping"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-domain-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-domain-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
