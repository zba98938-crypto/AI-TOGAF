# 主数据交换模式

`profile_id`: mdm-exchange-pattern-default；`artifact_id`: mdm-exchange-pattern；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §6.1.2。

## 构图与定义状态

表示族：`sequence`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：master_exchange。关系类型：traces_to。

```json
{
  "entities": {
    "master_exchange": [
      "pattern",
      "authority",
      "producer",
      "consumer",
      "consistency",
      "trigger"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 缩写必须随来源定义，不凭名称猜测语义
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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-exchange-pattern-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-exchange-pattern-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
