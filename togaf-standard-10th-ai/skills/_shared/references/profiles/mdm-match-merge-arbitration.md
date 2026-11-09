# C-MDM匹配、合并与人工仲裁

`profile_id`: mdm-match-merge-arbitration；`artifact_id`: customer-mdm-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §3、§5.2.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "mdm-match-merge-arbitration",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:mdm_match_case。关系类型：。

```json
{
  "entities": {
    "guide:mdm_match_case": [
      "rule",
      "record_refs",
      "key_comparison",
      "proposal",
      "matching_basis",
      "manual_arbitration",
      "decision_status",
      "merge_lineage",
      "unmerge_plan",
      "historical_policy"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 姓名相同不作为唯一合并依据
- merge状态需人工证据及实际谱系
- 概率/阈值必须有项目来源
- 历史原值与源ID保留

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/mdm-match-merge-arbitration/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/mdm-match-merge-arbitration/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构两对记录：R17与R92姓名相同但已核实证件不同；R18与R54已核实证件相同但地址与采集日期不同。项目规则仅把同证件视为候选，需人工核实后才合并。没有概率分数和匹配阈值；必须能取消错合并。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MATCH-01",
      "type": "guide:mdm_match_case",
      "name": "同名不同证件",
      "attributes": {
        "rule": "project-exact-identifier",
        "record_refs": [
          "甲馆:R17",
          "乙馆:R92"
        ],
        "key_comparison": {
          "name": "相同",
          "verified_identifier": "不同"
        },
        "proposal": "do-not-merge",
        "matching_basis": "已核实标识不同；姓名相同不足以确认",
        "manual_arbitration": "管家保持分离，记录差异，未改变历史借阅",
        "decision_status": "proposed",
        "merge_lineage": [],
        "unmerge_plan": "本例未合并，无需反向拆分",
        "historical_policy": "保留源记录、来源、时间及原交易关系"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MATCH-02",
      "type": "guide:mdm_match_case",
      "name": "同证件地址冲突",
      "attributes": {
        "rule": "project-exact-identifier",
        "record_refs": [
          "甲馆:R18",
          "丙馆:R54"
        ],
        "key_comparison": {
          "verified_identifier": "相同",
          "address": "冲突",
          "address_dates": "不同"
        },
        "proposal": "manual-review",
        "matching_basis": "证件相同仅产生候选，地址取值需源/时间与使用目的",
        "manual_arbitration": "管家先核实证件及两次地址时间；通过后可合并身份但保留地址历史",
        "decision_status": "proposed",
        "merge_lineage": [
          {
            "candidate": "MRG-02",
            "sources": [
              "甲馆:R18",
              "丙馆:R54"
            ],
            "state": "not-executed"
          }
        ],
        "unmerge_plan": "保存来源ID到黄金ID映射、原值与版本；错合并时恢复两个源身份并修正消费者关联",
        "historical_policy": "当前地址不得回写历史交易解释"
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
    "id": "v-mdm-match-merge-arbitration",
    "artifact_id": "customer-mdm-model",
    "profile_id": "mdm-match-merge-arbitration",
    "title": "C-MDM匹配、合并与人工仲裁",
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
      "MATCH-01",
      "MATCH-02"
    ],
    "relationship_ids": [],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "表格表达正文操作语义，不声称原图复刻。未知显式保留，ID稳定。",
    "allow_mixed_evolution": true
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-match-merge-arbitration --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-match-merge-arbitration --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
