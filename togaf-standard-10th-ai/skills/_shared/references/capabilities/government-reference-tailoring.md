# 政府参考模型裁剪

ID：`government-reference-tailoring`。主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21D §1–12；G21D §1.3、§2.1–12.1、§8.1、§11.1；G21D §1.3、§8.1、§11.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

怎样把政府参考分类映射到实际职责？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 怎样把政府参考分类映射到实际职责？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- sector
- function
- service

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：government_service, guide:government_overlay, guide:government_reference_node。

```json
{
  "government_service": [
    "sector",
    "function",
    "service",
    "scope",
    "applicability",
    "local_owner"
  ],
  "guide:government_overlay": [
    "reference_id",
    "reference_kind",
    "reference_path",
    "reference_description",
    "reference_version",
    "local_object_ids",
    "mapping_type",
    "applicability",
    "reason",
    "dependencies",
    "impact_scope",
    "source_locator",
    "review_action"
  ],
  "guide:government_reference_node": [
    "reference_level",
    "reference_path",
    "definition",
    "local_mapping",
    "applicability"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "sector": {
    "meaning": "参考政府部门分类",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "function": {
    "meaning": "参考功能或实际功能映射",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "service": {
    "meaning": "服务对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "applicability": {
    "meaning": "适用性判据与判断理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "local_owner": {
    "meaning": "本地责任部门或角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `guide:reference_classifies` | guide:government_reference_node → guide:government_reference_node | 目录规定的部门→功能→服务分类方向；不表示本地组织汇报、运行依赖或能力组成 |

## 分析步骤

1. 区分部门功能服务
2. 选择适用范围并映射本地服务
3. 识别跨部门共享
4. 记录偏差与理由

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 参考部门分类不是实际组织架构，版本中的部门计数应核对
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 参考部门分类不是实际组织架构，版本中的部门计数应核对


## 视图和交付物

- [养老业务的政府参考分类裁剪](../profiles/government-reference-tailoring-default.md)
- [政府参考目录与本地职责覆盖](../profiles/government-reference-catalog-overlay.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「政府参考模型裁剪」给出：参考部门分类不是实际组织架构，版本中的部门计数应核对",
    "expected": "missing-evidence",
    "why": "参考部门分类不是实际组织架构，版本中的部门计数应核对"
  },
  "modification_example": {
    "change": "在「政府参考模型裁剪」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "government-reference-tailoring-default-root",
      "type": "government_service",
      "name": "政府参考模型裁剪：本次范围",
      "attributes": {
        "sector": "参考模型中的共享服务分类",
        "function": "订单业务与数据支持",
        "service": "虚构订单案例中需验证的服务对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运",
        "applicability": "本例订单功能处理客户联系信息",
        "local_owner": "虚构订单案例中需验证的本地责任部门或角色",
        "definition": "按本例业务职责分解，排除不适用参考项",
        "level": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "government-reference-tailoring-default-child0",
      "type": "government_service",
      "name": "定义与规划",
      "attributes": {
        "sector": "参考模型中的共享服务分类",
        "function": "订单业务与数据支持",
        "service": "虚构订单案例中需验证的服务对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运",
        "applicability": "本例订单功能处理客户联系信息",
        "local_owner": "虚构订单案例中需验证的本地责任部门或角色",
        "definition": "本例定义与规划的职责边界",
        "level": 2,
        "parent_id": "government-reference-tailoring-default-root"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "government-reference-tailoring-default-child1",
      "type": "government_service",
      "name": "运营与治理",
      "attributes": {
        "sector": "参考模型中的共享服务分类",
        "function": "订单业务与数据支持",
        "service": "虚构订单案例中需验证的服务对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运",
        "applicability": "本例订单功能处理客户联系信息",
        "local_owner": "虚构订单案例中需验证的本地责任部门或角色",
        "definition": "本例运营与治理的职责边界",
        "level": 2,
        "parent_id": "government-reference-tailoring-default-root"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "government-reference-tailoring-default-part0",
      "type": "traces_to",
      "source": "government-reference-tailoring-default-root",
      "target": "government-reference-tailoring-default-child0",
      "label": "参考分类的从属项；不推断组织汇报",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "government-reference-tailoring-default-part1",
      "type": "traces_to",
      "source": "government-reference-tailoring-default-root",
      "target": "government-reference-tailoring-default-child1",
      "label": "参考分类的从属项；不推断组织汇报",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-government-reference-tailoring-default",
    "artifact_id": "government-reference-tailoring",
    "profile_id": "government-reference-tailoring-default",
    "title": "政府参考模型裁剪／虚构案例",
    "entity_ids": [
      "government-reference-tailoring-default-root",
      "government-reference-tailoring-default-child0",
      "government-reference-tailoring-default-child1"
    ],
    "relationship_ids": [
      "government-reference-tailoring-default-part0",
      "government-reference-tailoring-default-part1"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact government-reference-tailoring --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
