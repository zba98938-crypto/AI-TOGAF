# BI分析模型运营监控与处置

`profile_id`: bi-model-operating-monitoring；`artifact_id`: bi-transition-architecture；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G238 表4-2高级分析模型工业化、运营平台；表4-3分析模型管理与监控。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "bi-model-operating-monitoring",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "结构化表格，含完整属性、方向和证据；不是来源图模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:bi_model_operations。关系类型：。

```json
{
  "entities": {
    "ops:bi_model_operations": [
      "model_ref",
      "business_use",
      "lifecycle",
      "measure",
      "data_quality",
      "monitoring",
      "response",
      "lineage",
      "evidence_detail",
      "claim"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 未知阈值不能判模型通过
- 监测漂移不等于可自动重训投产
- 模型版本与数据/用途可追溯
- 监控包含处置责任和回退

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/bi-model-operating-monitoring/raw-brief.md",
  "analysis_path": "examples/addenda/operations/bi-model-operating-monitoring/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚M1/v0.1预测维修时长，影子试点供U2分析，不自动给客户承诺。服务经理要求每周看预测与实际耗时的绝对差中位数，单位分钟；没有实际值和合格阈值。故障类型标签质量未知。模型负责人收集准确性、输入分布、技术、安全、使用与人工改判信息。已知作业/数据失败先停止建议回人工；重训须版本测试和业务复核，不能自动投产。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MON-1",
      "type": "ops:bi_model_operations",
      "name": "维修时长模型M1",
      "attributes": {
        "model_ref": "M1/version-0.1",
        "business_use": "U2预约窗口建议；影子试点仅供分析，不自动承诺时长",
        "lifecycle": {
          "state": "shadow-pilot",
          "owner": "模型负责人",
          "business_owner": "服务经理",
          "release_evidence": "候选报告ML-01，尚未生产批准"
        },
        "measure": {
          "name": "预测绝对误差中位数",
          "unit": "minute",
          "window": "2026-11试点每周",
          "value": null,
          "definition": "每维修单预测与实际耗时绝对差的中位数；仅项目选择",
          "basis": "虚构服务经理约定M-01",
          "threshold": null
        },
        "data_quality": "故障标签未知，先评估样本来源和实际耗时定义",
        "monitoring": {
          "accuracy": "按周观察误差，阈值待经理决定",
          "drift": "记录输入故障类型分布变化；阈值未知",
          "technical": "服务可用/作业失败",
          "security": "访问异常/泄露线索",
          "usage": "经理是否使用建议及人工改判原因"
        },
        "response": {
          "trigger": "已知作业失败或数据问题先停止发布建议；未知阈值不得制造合格结论",
          "owner": "模型负责人和服务经理",
          "fallback": "恢复人工窗口估计",
          "retraining": "经业务复核及版本测试后提出新候选；不自动重训投产"
        },
        "lineage": "训练/验证数据版本、特征规则、模型版本、消费U2、观测记录尚待汇集",
        "evidence_detail": "虚构M-01与ML-01草案",
        "claim": "候选监控方案；无实际准确率/漂移通过结论"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [],
  "view": {
    "id": "v-bi-model-operating-monitoring",
    "artifact_id": "bi-transition-architecture",
    "profile_id": "bi-model-operating-monitoring",
    "title": "BI分析模型运营监控与处置",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "MON-1"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-model-operating-monitoring --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-model-operating-monitoring --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
