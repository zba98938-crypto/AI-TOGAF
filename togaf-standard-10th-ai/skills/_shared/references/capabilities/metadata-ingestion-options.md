# 元数据采集备选方案

ID：`metadata-ingestion-options`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-9。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

选择手工、推送还是拉取元数据？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 选择手工、推送还是拉取元数据？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- mechanism
- responsibility
- frequency

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：metadata_component, metadata_repository, metadata_source。

```json
{
  "metadata_component": [
    "mechanism",
    "responsibility",
    "frequency",
    "protocol",
    "security",
    "cost"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "mechanism": {
    "meaning": "手工、推送或拉取等机制",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "responsibility": {
    "meaning": "各方责任及边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "frequency": {
    "meaning": "执行或交换频率",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "protocol": {
    "meaning": "交互协议",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "security": {
    "meaning": "安全要求与处理",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "cost": {
    "meaning": "成本及估算边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `pulls_metadata` | metadata_repository → metadata_source,metadata_repository | 目标发起拉取；响应数据流需另记 |
| `pushes_metadata` | metadata_source,metadata_repository → metadata_repository | 源主动向目标推送 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 识别源系统与采集责任
2. 区分控制命令和回传信息
3. 比较人工API代理机制
4. 权衡时效负担安全

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 三种机制是备选方案，不是三个固定先后阶段
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 三种机制是备选方案，不是三个固定先后阶段


## 视图和交付物

- [元数据采集备选方案](../profiles/metadata-ingestion-options-default.md)
- [元数据采集三种模式](../profiles/metadata-manual-push-pull.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「元数据采集备选方案」给出：三种机制是备选方案，不是三个固定先后阶段",
    "expected": "missing-evidence",
    "why": "三种机制是备选方案，不是三个固定先后阶段"
  },
  "modification_example": {
    "change": "在「元数据采集备选方案」的范围内新增或修改一项，检查下游是否随之变化",
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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact metadata-ingestion-options --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
