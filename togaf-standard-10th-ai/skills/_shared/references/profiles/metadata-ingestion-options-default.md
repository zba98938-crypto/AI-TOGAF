# 元数据采集备选方案

`profile_id`: metadata-ingestion-options-default；`artifact_id`: metadata-ingestion-options；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-9。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：metadata_component, metadata_repository, metadata_source。关系类型：pulls_metadata, pushes_metadata, traces_to。

```json
{
  "entities": {
    "metadata_component": [
      "mechanism",
      "responsibility",
      "frequency",
      "protocol",
      "security",
      "cost"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 三种机制是备选方案，不是三个固定先后阶段
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
      "id": "metadata-ingestion-options-default-repository",
      "type": "metadata_repository",
      "name": "元数据管理工具",
      "attributes": {
        "scope": "订单业务元数据与技术模式",
        "authority": "定义审核后发布"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-source",
      "type": "metadata_source",
      "name": "订单源应用",
      "attributes": {
        "scope": "提供模式与定义，不提供客户实际订单内容"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-manual",
      "type": "metadata_component",
      "name": "手工采集候选",
      "attributes": {
        "mechanism": "手工",
        "responsibility": "数据管家采集并提交",
        "frequency": "变更申请时",
        "protocol": "受控录入",
        "security": "最小授权、审计和敏感字段限制",
        "cost": "人工维护与审核投入"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-push",
      "type": "metadata_component",
      "name": "推送采集候选",
      "attributes": {
        "mechanism": "推送",
        "responsibility": "源应用主动通知变更",
        "frequency": "模式变更后",
        "protocol": "受控推送API",
        "security": "最小授权、审计和敏感字段限制",
        "cost": "连接器维护及重试"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-pull",
      "type": "metadata_component",
      "name": "拉取采集候选",
      "attributes": {
        "mechanism": "拉取",
        "responsibility": "中央工具发起模式读取",
        "frequency": "每日一次",
        "protocol": "只读模式接口",
        "security": "最小授权、审计和敏感字段限制",
        "cost": "轮询负载及访问控制"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "metadata-ingestion-options-default-manual-source",
      "type": "traces_to",
      "source": "metadata-ingestion-options-default-manual",
      "target": "metadata-ingestion-options-default-source",
      "label": "方案适用订单源应用；三方案相互独立",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-manual-repo",
      "type": "traces_to",
      "source": "metadata-ingestion-options-default-manual",
      "target": "metadata-ingestion-options-default-repository",
      "label": "方案向元数据工具提供受控元数据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-push-source",
      "type": "traces_to",
      "source": "metadata-ingestion-options-default-push",
      "target": "metadata-ingestion-options-default-source",
      "label": "方案适用订单源应用；三方案相互独立",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-push-repo",
      "type": "traces_to",
      "source": "metadata-ingestion-options-default-push",
      "target": "metadata-ingestion-options-default-repository",
      "label": "方案向元数据工具提供受控元数据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-pull-source",
      "type": "traces_to",
      "source": "metadata-ingestion-options-default-pull",
      "target": "metadata-ingestion-options-default-source",
      "label": "方案适用订单源应用；三方案相互独立",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-pull-repo",
      "type": "traces_to",
      "source": "metadata-ingestion-options-default-pull",
      "target": "metadata-ingestion-options-default-repository",
      "label": "方案向元数据工具提供受控元数据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-push-flow",
      "type": "pushes_metadata",
      "source": "metadata-ingestion-options-default-source",
      "target": "metadata-ingestion-options-default-repository",
      "label": "推送：源主动提交元数据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-ingestion-options-default-pull-control",
      "type": "pulls_metadata",
      "source": "metadata-ingestion-options-default-repository",
      "target": "metadata-ingestion-options-default-source",
      "label": "拉取：目标主动发起读取请求",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-metadata-ingestion-options-default",
    "artifact_id": "metadata-ingestion-options",
    "profile_id": "metadata-ingestion-options-default",
    "title": "元数据采集备选方案／虚构案例",
    "entity_ids": [
      "metadata-ingestion-options-default-repository",
      "metadata-ingestion-options-default-source",
      "metadata-ingestion-options-default-manual",
      "metadata-ingestion-options-default-push",
      "metadata-ingestion-options-default-pull"
    ],
    "relationship_ids": [
      "metadata-ingestion-options-default-manual-source",
      "metadata-ingestion-options-default-manual-repo",
      "metadata-ingestion-options-default-push-source",
      "metadata-ingestion-options-default-push-repo",
      "metadata-ingestion-options-default-pull-source",
      "metadata-ingestion-options-default-pull-repo",
      "metadata-ingestion-options-default-push-flow",
      "metadata-ingestion-options-default-pull-control"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-ingestion-options-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-ingestion-options-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
