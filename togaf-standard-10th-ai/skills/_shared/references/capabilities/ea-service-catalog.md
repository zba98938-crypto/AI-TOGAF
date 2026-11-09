# 企业架构服务目录

ID：`ea-service-catalog`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G217 附录B–C；G217 §4.4.1–4.4.5，图4-3；G217 附录C.1–C.7、附录D。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

EA 团队应提供哪些决策支持服务？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- EA 团队应提供哪些决策支持服务？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- consumer
- decision
- output

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：ea_service, guide:ea_service_context, guide:ea_adm_mapping。

```json
{
  "ea_service": [
    "consumer",
    "decision",
    "output",
    "adm_phase",
    "owner",
    "service_level"
  ],
  "guide:ea_service_context": [
    "service",
    "context",
    "emergence",
    "meaning",
    "local_depth",
    "evidence_detail",
    "mapping_origin",
    "source_cell_status",
    "resources"
  ],
  "guide:ea_adm_mapping": [
    "service",
    "ADM_phase",
    "project_activity",
    "output",
    "owner",
    "mapping_origin",
    "evidence_detail",
    "source_mapping"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "consumer": {
    "meaning": "数据或消息消费方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decision": {
    "meaning": "决策结果、理由和状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "output": {
    "meaning": "活动输出",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "adm_phase": {
    "meaning": "适用 ADM 阶段",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "service_level": {
    "meaning": "服务水准与度量",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 选择候选服务
2. 明确消费者决策和成果
3. 映射 ADM 与能力
4. 核对团队容量与服务约定
5. 按服务梳理首次出现与后续范围
6. N只用于首次引入，P表示沿用，D要求明确新增深度
7. 记录项目证据与原图证据两个状态，不混称相同
8. 先明确服务输出与消费者决策
9. 由项目活动确定使用阶段
10. 分别登记来源映射和项目映射
11. 未知原图格不推断不适用或唯一阶段

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 候选服务不是每个 EA 团队必须提供的服务清单
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 候选服务不是每个 EA 团队必须提供的服务清单


## 视图和交付物

- [企业架构服务目录](../profiles/ea-service-catalog-default.md)
- [EA服务N／P／D语境矩阵](../profiles/ea-service-emergence-npd.md)
- [EA服务与ADM证据映射](../profiles/ea-service-adm-evidence-map.md)
- [EA服务与ADM证据映射／图形](../profiles/ea-service-adm-matrix.md)
- [EA服务×ADM来源参考矩阵](../profiles/ea-service-adm-reference-matrix.md)
- [EA服务×ADM来源参考矩阵](../profiles/ea-service-adm-reference-table.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「企业架构服务目录」给出：候选服务不是每个 EA 团队必须提供的服务清单",
    "expected": "missing-evidence",
    "why": "候选服务不是每个 EA 团队必须提供的服务清单"
  },
  "modification_example": {
    "change": "在「企业架构服务目录」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "ea-service-catalog-default-record",
      "type": "ea_service",
      "name": "企业架构服务目录：订单范围记录",
      "attributes": {
        "consumer": "虚构订单应用",
        "decision": "虚构订单案例中需验证的决策结果、理由和状态",
        "output": "经过校验并发布的新定义",
        "adm_phase": "B、C、E",
        "owner": "虚构业务负责人",
        "service_level": "在决策节点前提供足够架构证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-ea-service-catalog-default",
    "artifact_id": "ea-service-catalog",
    "profile_id": "ea-service-catalog-default",
    "title": "企业架构服务目录／虚构案例",
    "entity_ids": [
      "ea-service-catalog-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact ea-service-catalog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
