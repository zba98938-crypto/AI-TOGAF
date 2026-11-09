# 过渡架构模型

`profile_id`: transition-architecture-model-default；`artifact_id`: transition-architecture-model；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G248 §2；图2-2。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：transition, work_package。关系类型：implements_transition, traces_to, depends_on。

```json
{
  "entities": {
    "transition": [
      "definition",
      "operating_conditions"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 过渡架构不是仅有交付日期的里程碑
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
      "id": "transition-architecture-model-default-state0",
      "type": "transition",
      "name": "基线：旧平台",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 0
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-state1",
      "type": "transition",
      "name": "过渡1：只读副本",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-state2",
      "type": "transition",
      "name": "过渡2：分批写入",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-state3",
      "type": "transition",
      "name": "目标：统一履约",
      "attributes": {
        "definition": "本例具名运营状态，演进分类见标签",
        "operating_conditions": {
          "operations": "值班与服务责任明确",
          "data_consistency": "逐笔对账后切换",
          "dependencies": "身份与接口已就绪",
          "controls": "授权与审计持续",
          "rollback": "暂停新写并恢复旧平台"
        },
        "ordinal": 3
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-wp",
      "type": "work_package",
      "name": "接口及对账工作包",
      "attributes": {
        "definition": "实现第一过渡的候选工作包"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "transition-architecture-model-default-evolve1",
      "type": "traces_to",
      "source": "transition-architecture-model-default-state0",
      "target": "transition-architecture-model-default-state1",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-evolve2",
      "type": "traces_to",
      "source": "transition-architecture-model-default-state1",
      "target": "transition-architecture-model-default-state2",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-evolve3",
      "type": "traces_to",
      "source": "transition-architecture-model-default-state2",
      "target": "transition-architecture-model-default-state3",
      "label": "达到进入退出条件后演进；不是仅有日期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "transition-architecture-model-default-impl",
      "type": "implements_transition",
      "source": "transition-architecture-model-default-wp",
      "target": "transition-architecture-model-default-state1",
      "label": "工作包实现可运营过渡",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-transition-architecture-model-default",
    "artifact_id": "transition-architecture-model",
    "profile_id": "transition-architecture-model-default",
    "title": "过渡架构模型／虚构案例",
    "entity_ids": [
      "transition-architecture-model-default-state0",
      "transition-architecture-model-default-state1",
      "transition-architecture-model-default-state2",
      "transition-architecture-model-default-state3",
      "transition-architecture-model-default-wp"
    ],
    "relationship_ids": [
      "transition-architecture-model-default-evolve1",
      "transition-architecture-model-default-evolve2",
      "transition-architecture-model-default-evolve3",
      "transition-architecture-model-default-impl"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile transition-architecture-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile transition-architecture-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
