# 用途与基础设施双入口机会清单

`profile_id`: sustainability-dual-entry-analysis-default；`artifact_id`: sustainability-dual-entry-analysis；主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242 §3.5.2–3.5.3、表3-3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "sustainability-dual-entry-analysis-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:dual_entry_opportunity。关系类型：。

```json
{
  "entities": {
    "guide:dual_entry_opportunity": [
      "entry_point",
      "use_id",
      "application_data_path",
      "infrastructure_id",
      "baseline_evidence",
      "action",
      "business_acceptance",
      "nonfunctional_change",
      "constraints",
      "priority_basis",
      "dependencies",
      "status"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 基础设施看似空闲不代表没有业务用途
- 共有设备和数据不能按单一用途全部删除
- 排序不等于碳量核算；未测量不填虚构减排值
- 低技术/人工替代也需同范围全生命周期比较

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。",
  "sources": [
    {
      "id": "src-sustainability-dual-entry-analysis-default",
      "kind": "example",
      "description": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。 材料组 dual-entry",
      "locator": "examples/addenda/sustainability/raw-business-materials.json#dual-entry"
    }
  ],
  "entities": [
    {
      "id": "sustainability-dual-entry-analysis-default-1",
      "type": "guide:dual_entry_opportunity",
      "name": "培训视频节制",
      "attributes": {
        "entry_point": "use",
        "use_id": "USE-TRAIN",
        "application_data_path": [
          "APP-VIDEO",
          "DATA-VID"
        ],
        "infrastructure_id": "STORAGE-A",
        "baseline_evidence": "DU-02：默认4K且永久保存；碳足迹数据尚缺",
        "action": "优化为1080p；非合规视频90天后删除",
        "business_acceptance": "业务负责人在DU-02接受；需数据/安全审查",
        "nonfunctional_change": "降低非关键视频分辨率与保存期；法定记录仍7年",
        "constraints": {
          "use": "默认1080p，特殊需求申请",
          "data": "培训90天；法定记录7年单独分类",
          "application-development": "上传时必须元数据标保留类别",
          "infrastructure": "不因视频减少而删除共享STORAGE-A"
        },
        "priority_basis": "项目DU-04：已有业务接受先做；不声称减排量",
        "dependencies": [
          "STORAGE-A共享法定记录",
          "删除规则审查"
        ],
        "status": "candidate-awaiting-control-review"
      },
      "evidence": [
        "src-sustainability-dual-entry-analysis-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-dual-entry-analysis-default-2",
      "type": "guide:dual_entry_opportunity",
      "name": "报表服务器运行窗口",
      "attributes": {
        "entry_point": "infrastructure",
        "use_id": "USE-REPORT",
        "application_data_path": [
          "APP-REPORT",
          "DATA-REPORT"
        ],
        "infrastructure_id": "SERVER-B",
        "baseline_evidence": "DU-03使用日志08–18有作业；能耗测量待补",
        "action": "评估非工作窗口停机/按需启动",
        "business_acceptance": "非紧急报表次日上午交付被接受；紧急用途需核实",
        "nonfunctional_change": "用业务窗口替代默认24x7；保留恢复演练条件",
        "constraints": {
          "use": "非紧急报表在08–18执行",
          "data": "保留业务规定数据，不推断可删",
          "application-development": "作业必须可暂停并恢复",
          "infrastructure": "运维验证恢复时间后才能停机"
        },
        "priority_basis": "项目DU-04：运维验证后处理",
        "dependencies": [
          "启动可靠性",
          "潜在紧急业务用途"
        ],
        "status": "candidate-awaiting-operations-evidence"
      },
      "evidence": [
        "src-sustainability-dual-entry-analysis-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-sustainability-dual-entry-analysis-default",
    "artifact_id": "sustainability-dual-entry-analysis",
    "profile_id": "sustainability-dual-entry-analysis-default",
    "title": "用途与基础设施双入口机会清单",
    "entity_ids": [
      "sustainability-dual-entry-analysis-default-1",
      "sustainability-dual-entry-analysis-default-2"
    ],
    "relationship_ids": [],
    "analysis": "分别从培训用途向下追到共享存储，从服务器向上追到报表业务。两个入口保留独立清单和四类约束，避免删除共享法定记录；未提供排放数值时不伪算收益。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "dual-entry"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-dual-entry-analysis-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-dual-entry-analysis-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
