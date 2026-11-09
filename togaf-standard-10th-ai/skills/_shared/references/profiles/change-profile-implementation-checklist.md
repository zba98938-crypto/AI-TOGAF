# 变革画像实施检查

`profile_id`: change-profile-implementation-checklist；`artifact_id`: change-profile-governance-checklist；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G248 §9表9-1；G248 §11表11-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.2。

{
  "id": "change-profile-implementation-checklist",
  "version": "2.2",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:governance-check。关系类型：。

```json
{
  "entities": {
    "guide:governance-check": [
      "source_check_id",
      "step",
      "adm_phase",
      "change_profile",
      "applicability",
      "response",
      "evidence_locator",
      "owner",
      "action",
      "transition_id"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构业务案例；采用来源结构及术语，不代表真实实施或批准。",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构社区服务机构的访谈、记录和项目约定"
    }
  ],
  "entities": [
    {
      "id": "check-implementation-01",
      "type": "guide:governance-check",
      "name": "物理解决方案组件提供方是否已同意并签署合同，并承诺约定的交付方法？",
      "attributes": {
        "source_check_id": "implementation-01",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "待裁剪",
        "response": "源指南未建议纳入，项目保留待裁剪",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-02",
      "type": "guide:governance-check",
      "name": "物理解决方案组件是否已获取，并按其规格与合同进行测试？",
      "attributes": {
        "source_check_id": "implementation-02",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "待裁剪",
        "response": "源指南未建议纳入，项目保留待裁剪",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-03",
      "type": "guide:governance-check",
      "name": "物理解决方案组件是否已实施到其运营环境，以支持约定的服务水平？",
      "attributes": {
        "source_check_id": "implementation-03",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "符合示例判据",
        "evidence_locator": "虚构演练DEP-01：预约组件在过渡A环境运行",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-04",
      "type": "guide:governance-check",
      "name": "物理解决方案组件是否已在其运营环境中测试并保证，且支持服务水平协议？",
      "attributes": {
        "source_check_id": "implementation-04",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-05",
      "type": "guide:governance-check",
      "name": "风险是否已处理并得到适当缓解？",
      "attributes": {
        "source_check_id": "implementation-05",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-06",
      "type": "guide:governance-check",
      "name": "相关利益相关者是否已签署已实施的解决方案组件与服务？",
      "attributes": {
        "source_check_id": "implementation-06",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-07",
      "type": "guide:governance-check",
      "name": "物理解决方案组件及相关运营服务是否已被服务运营方接纳进入运营管理与支持？",
      "attributes": {
        "source_check_id": "implementation-07",
        "step": 9,
        "adm_phase": "阶段 G：实施治理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-08",
      "type": "guide:governance-check",
      "name": "所有合同承诺、测试与服务水平是否已评审并保证？",
      "attributes": {
        "source_check_id": "implementation-08",
        "step": 10,
        "adm_phase": "阶段 H：变革管理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-09",
      "type": "guide:governance-check",
      "name": "KPI 是否已达成？",
      "attributes": {
        "source_check_id": "implementation-09",
        "step": 10,
        "adm_phase": "阶段 H：变革管理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "check-implementation-10",
      "type": "guide:governance-check",
      "name": "新解决方案是否交付了预期或高于预期的价值？",
      "attributes": {
        "source_check_id": "implementation-10",
        "step": 10,
        "adm_phase": "阶段 H：变革管理",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "待证据",
        "evidence_locator": "未提供对应证据",
        "owner": "社区服务项目负责人",
        "action": "核实结果证据并决定通过/返工/豁免；不自动批准",
        "transition_id": "community-transition-a"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-change-profile-implementation-checklist",
    "artifact_id": "change-profile-governance-checklist",
    "profile_id": "change-profile-implementation-checklist",
    "title": "变革画像实施检查",
    "entity_ids": [
      "check-implementation-01",
      "check-implementation-02",
      "check-implementation-03",
      "check-implementation-04",
      "check-implementation-05",
      "check-implementation-06",
      "check-implementation-07",
      "check-implementation-08",
      "check-implementation-09",
      "check-implementation-10"
    ],
    "relationship_ids": [],
    "analysis": "原料：社区服务预约上线采用Functional画像，只有访谈、KPI草案和部署演练记录。先按源表筛建议项，再逐项核对证据。可支持的三项仍只为示例，其他项保持待证据/待裁剪；不能据此批准上线。",
    "legend": "同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile change-profile-implementation-checklist --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile change-profile-implementation-checklist --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
