# 主数据交换模式

ID：`mdm-exchange-pattern`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §6.1.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

主数据交换由哪些应用与责任控制？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 主数据交换由哪些应用与责任控制？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- pattern
- authority
- producer

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：master_exchange。

```json
{
  "master_exchange": [
    "pattern",
    "authority",
    "producer",
    "consumer",
    "consistency",
    "trigger"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "pattern": {
    "meaning": "交换模式及来源定义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "authority": {
    "meaning": "决策或数据权威及授权范围",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "producer": {
    "meaning": "数据或消息提供方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "consumer": {
    "meaning": "数据或消息消费方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "consistency": {
    "meaning": "一致性与时效要求",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "trigger": {
    "meaning": "触发事件或判据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 声明 PoA 与 PoC 等来源术语
2. 识别权威提供方与消费方
3. 建模请求更新和通知
4. 核对一致性边界

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 缩写必须随来源定义，不凭名称猜测语义
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 缩写必须随来源定义，不凭名称猜测语义


## 视图和交付物

- [主数据交换模式](../profiles/mdm-exchange-pattern-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「主数据交换模式」给出：缩写必须随来源定义，不凭名称猜测语义",
    "expected": "missing-evidence",
    "why": "缩写必须随来源定义，不凭名称猜测语义"
  },
  "modification_example": {
    "change": "在「主数据交换模式」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "mdm-exchange-pattern-default-producer",
      "type": "master_exchange",
      "name": "源方／提交活动",
      "attributes": {
        "pattern": "以本地存储和时效要求选择交换模式",
        "authority": "虚构订单案例中需验证的决策或数据权威及授权范围",
        "producer": "虚构客户主数据服务",
        "consumer": "虚构订单应用",
        "consistency": "关键身份更新需确认，批量副本单独标记时效",
        "trigger": "订单一致性校验失败时暂停切换",
        "order": 1,
        "actor": "源应用或数据管家",
        "action": "提交更新",
        "input": "已授权的变更",
        "output": "待校验内容",
        "validation": "校验身份和版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "mdm-exchange-pattern-default-consumer",
      "type": "master_exchange",
      "name": "目标方／校验活动",
      "attributes": {
        "pattern": "以本地存储和时效要求选择交换模式",
        "authority": "虚构订单案例中需验证的决策或数据权威及授权范围",
        "producer": "虚构客户主数据服务",
        "consumer": "虚构订单应用",
        "consistency": "关键身份更新需确认，批量副本单独标记时效",
        "trigger": "订单一致性校验失败时暂停切换",
        "order": 2,
        "actor": "目标数据管理服务",
        "action": "校验并确认",
        "input": "待校验内容",
        "output": "受控确认",
        "validation": "按契约验证字段与一致性"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "mdm-exchange-pattern-default-submit",
      "type": "traces_to",
      "source": "mdm-exchange-pattern-default-producer",
      "target": "mdm-exchange-pattern-default-consumer",
      "label": "提交有版本的更新请求",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "order": 1
      }
    },
    {
      "id": "mdm-exchange-pattern-default-reply",
      "type": "traces_to",
      "source": "mdm-exchange-pattern-default-consumer",
      "target": "mdm-exchange-pattern-default-producer",
      "label": "返回受控结果或明确拒绝",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "order": 2
      }
    }
  ],
  "view": {
    "id": "v-mdm-exchange-pattern-default",
    "artifact_id": "mdm-exchange-pattern",
    "profile_id": "mdm-exchange-pattern-default",
    "title": "主数据交换模式／虚构案例",
    "entity_ids": [
      "mdm-exchange-pattern-default-producer",
      "mdm-exchange-pattern-default-consumer"
    ],
    "relationship_ids": [
      "mdm-exchange-pattern-default-submit",
      "mdm-exchange-pattern-default-reply"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact mdm-exchange-pattern --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
