# 用途与基础设施双入口分析

ID：`sustainability-dual-entry-analysis`。主责：[togaf-change-value](../../../togaf-change-value/SKILL.md)。

来源：G242 §3.5.2–3.5.3、表3-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

从哪里识别可放弃/优化用途与设备，如何形成可接受约束？

- 业务负责人
- 企业架构师
- 环境核算负责人
- 采购及供应商负责人
- HR与治理负责人
- 从哪里识别可放弃/优化用途与设备，如何形成可接受约束？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 组织、服务、业务用途及所评估期间/生命周期边界
- 原始访谈、使用数据、供应商记录及稳定证据ID
- 适用目标、职责和组织自定决策规则；未知项显式登记

可选：

- 历史评估、环境数据目录、采购契约及角色技能资料

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:dual_entry_opportunity。

```json
{
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
}
```

{
  "name": {
    "meaning": "机会记录",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "entry_point": {
    "meaning": "use或infrastructure，两入口分别输出",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "use_id": {
    "meaning": "业务用途稳定ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "application_data_path": {
    "meaning": "应用/数据映射路径",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "infrastructure_id": {
    "meaning": "设备/系统稳定ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "baseline_evidence": {
    "meaning": "初始使用/资源/环境依据及缺口",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "action": {
    "meaning": "优化或放弃候选",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "business_acceptance": {
    "meaning": "业务可接受性及授权",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "nonfunctional_change": {
    "meaning": "修订的非功能要求",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "constraints": {
    "meaning": "用途/数据/应用开发/基础设施四类约束",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "priority_basis": {
    "meaning": "排序规则与依据，不能无依据打分",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "dependencies": {
    "meaning": "共享依赖/退出影响",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "status": {
    "meaning": "待验证/候选，不能凭分析认定减排",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 取得与业务/技术协作的管理授权
2. 从业务用途和高影响基础设施分别建立候选清单
3. 沿应用/数据/设备向下或业务向上追溯共享影响
4. 核实业务接受性并修订非功能要求
5. 明确四类约束理由/检查/复评，并转入方案评审和治理

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 基础设施看似空闲不代表没有业务用途
- 共有设备和数据不能按单一用途全部删除
- 排序不等于碳量核算；未测量不填虚构减排值
- 低技术/人工替代也需同范围全生命周期比较

- 基础设施看似空闲不代表没有业务用途
- 共有设备和数据不能按单一用途全部删除
- 排序不等于碳量核算；未测量不填虚构减排值
- 低技术/人工替代也需同范围全生命周期比较


## 视图和交付物

- [用途与基础设施双入口机会清单](../profiles/sustainability-dual-entry-analysis-default.md)

- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "基础设施优化无任何业务用途回溯",
    "expected": "dual-entry-trace-gap"
  },
  "modification_example": {
    "change": "发现SERVER-B夜间支持紧急作业",
    "expected": "撤回夜间停机建议，标冲突并调整恢复/业务要求；培训优化不受此事实直接影响"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/sustainability-dual-entry-analysis.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact sustainability-dual-entry-analysis --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
