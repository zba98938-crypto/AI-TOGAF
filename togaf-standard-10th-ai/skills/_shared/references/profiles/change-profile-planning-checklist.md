# 变革画像规划检查

`profile_id`: change-profile-planning-checklist；`artifact_id`: change-profile-governance-checklist；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G248 §9表9-1；G248 §11表11-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.2。

{
  "id": "change-profile-planning-checklist",
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
      "id": "check-planning-01",
      "type": "guide:governance-check",
      "name": "客户需求是否已被清晰理解并达成一致？",
      "attributes": {
        "source_check_id": "planning-01",
        "step": 1,
        "adm_phase": "阶段 A：愿景",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "符合示例判据",
        "evidence_locator": "虚构访谈INT-01：居民需线下/线上统一预约",
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
      "id": "check-planning-02",
      "type": "guide:governance-check",
      "name": "架构成熟度是否达到该变革所需水平？",
      "attributes": {
        "source_check_id": "planning-02",
        "step": 1,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-03",
      "type": "guide:governance-check",
      "name": "对企业业务模式与运营模式的影响是否已识别并处理？",
      "attributes": {
        "source_check_id": "planning-03",
        "step": 1,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-04",
      "type": "guide:governance-check",
      "name": "功能与非功能需求是否均已定义？",
      "attributes": {
        "source_check_id": "planning-04",
        "step": 1,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-05",
      "type": "guide:governance-check",
      "name": "是否理解并应用了每个变革单元的架构画像？",
      "attributes": {
        "source_check_id": "planning-05",
        "step": 2,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-06",
      "type": "guide:governance-check",
      "name": "KPI 是否已定义？",
      "attributes": {
        "source_check_id": "planning-06",
        "step": 3,
        "adm_phase": "阶段 A：愿景",
        "change_profile": "functional",
        "applicability": "纳入",
        "response": "符合示例判据",
        "evidence_locator": "项目规则KPI-01：预约冲突次数按周观察，目标由负责人另定",
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
      "id": "check-planning-07",
      "type": "guide:governance-check",
      "name": "是否已创建拟议解决方案概览/草图？",
      "attributes": {
        "source_check_id": "planning-07",
        "step": 4,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-08",
      "type": "guide:governance-check",
      "name": "预期解决方案组件的复用/购买/创建属性是否已批准？",
      "attributes": {
        "source_check_id": "planning-08",
        "step": 4,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-09",
      "type": "guide:governance-check",
      "name": "粗略量级（ROM）大纲计划与估算是否完成？",
      "attributes": {
        "source_check_id": "planning-09",
        "step": 4,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-10",
      "type": "guide:governance-check",
      "name": "愿景是否已获所有相关利益相关者签署？",
      "attributes": {
        "source_check_id": "planning-10",
        "step": 4,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-11",
      "type": "guide:governance-check",
      "name": "是否审查了所有企业与分段指南（原则、政策与标准），并批准了任何偏离？",
      "attributes": {
        "source_check_id": "planning-11",
        "step": 4,
        "adm_phase": "阶段 A：愿景",
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
      "id": "check-planning-12",
      "type": "guide:governance-check",
      "name": "与拟议解决方案相关的所有业务能力是否已识别？",
      "attributes": {
        "source_check_id": "planning-12",
        "step": 5,
        "adm_phase": "阶段 B：业务",
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
      "id": "check-planning-13",
      "type": "guide:governance-check",
      "name": "与拟议解决方案相关的所有参与者、流程与业务服务是否已描述？",
      "attributes": {
        "source_check_id": "planning-13",
        "step": 5,
        "adm_phase": "阶段 B：业务",
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
      "id": "check-planning-14",
      "type": "guide:governance-check",
      "name": "与拟议解决方案相关的所有信息实体是否已描述？",
      "attributes": {
        "source_check_id": "planning-14",
        "step": 5,
        "adm_phase": "阶段 B：业务",
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
      "id": "check-planning-15",
      "type": "guide:governance-check",
      "name": "所有服务水平绩效与质量要求是否已识别？",
      "attributes": {
        "source_check_id": "planning-15",
        "step": 5,
        "adm_phase": "阶段 B：业务",
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
      "id": "check-planning-16",
      "type": "guide:governance-check",
      "name": "所有业务运营支持、维护与治理流程及资源是否已识别？",
      "attributes": {
        "source_check_id": "planning-16",
        "step": 5,
        "adm_phase": "阶段 B：业务",
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
      "id": "check-planning-17",
      "type": "guide:governance-check",
      "name": "所有相关业务原则、政策与标准是否已审查，并批准了任何偏离？",
      "attributes": {
        "source_check_id": "planning-17",
        "step": 5,
        "adm_phase": "阶段 B：业务",
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
      "id": "check-planning-18",
      "type": "guide:governance-check",
      "name": "所有逻辑数据实体是否已在 ERD 中定义？",
      "attributes": {
        "source_check_id": "planning-18",
        "step": 5,
        "adm_phase": "阶段 C：数据",
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
      "id": "check-planning-19",
      "type": "guide:governance-check",
      "name": "所有逻辑数据存储机制与位置是否已识别？",
      "attributes": {
        "source_check_id": "planning-19",
        "step": 5,
        "adm_phase": "阶段 C：数据",
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
      "id": "check-planning-20",
      "type": "guide:governance-check",
      "name": "所有逻辑消息交换格式与内容是否已定义？",
      "attributes": {
        "source_check_id": "planning-20",
        "step": 5,
        "adm_phase": "阶段 C：数据",
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
      "id": "check-planning-21",
      "type": "guide:governance-check",
      "name": "所有逻辑数据查询机制与控制是否已定义？",
      "attributes": {
        "source_check_id": "planning-21",
        "step": 5,
        "adm_phase": "阶段 C：数据",
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
      "id": "check-planning-22",
      "type": "guide:governance-check",
      "name": "所有数据管理与治理流程及资源是否已识别？",
      "attributes": {
        "source_check_id": "planning-22",
        "step": 5,
        "adm_phase": "阶段 C：数据",
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
      "id": "check-planning-23",
      "type": "guide:governance-check",
      "name": "所有数据原则、政策与标准是否已审查，并批准了任何偏离（例如个人数据）？",
      "attributes": {
        "source_check_id": "planning-23",
        "step": 5,
        "adm_phase": "阶段 C：数据",
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
      "id": "check-planning-24",
      "type": "guide:governance-check",
      "name": "所有逻辑应用组件及其提供的接口是否已识别？",
      "attributes": {
        "source_check_id": "planning-24",
        "step": 5,
        "adm_phase": "阶段 C：应用",
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
      "id": "check-planning-25",
      "type": "guide:governance-check",
      "name": "所有逻辑应用交互模式是否已识别？",
      "attributes": {
        "source_check_id": "planning-25",
        "step": 5,
        "adm_phase": "阶段 C：应用",
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
      "id": "check-planning-26",
      "type": "guide:governance-check",
      "name": "所有逻辑应用执行环境、域与位置是否已识别？",
      "attributes": {
        "source_check_id": "planning-26",
        "step": 5,
        "adm_phase": "阶段 C：应用",
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
      "id": "check-planning-27",
      "type": "guide:governance-check",
      "name": "所有应用运营支持、维护、治理流程与资源是否已识别？",
      "attributes": {
        "source_check_id": "planning-27",
        "step": 5,
        "adm_phase": "阶段 C：应用",
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
      "id": "check-planning-28",
      "type": "guide:governance-check",
      "name": "所有相关应用与软件原则、政策与标准是否已审查，并批准了任何偏离？",
      "attributes": {
        "source_check_id": "planning-28",
        "step": 5,
        "adm_phase": "阶段 C：应用",
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
      "id": "check-planning-29",
      "type": "guide:governance-check",
      "name": "所有逻辑技术组件及其接口是否已定义？",
      "attributes": {
        "source_check_id": "planning-29",
        "step": 5,
        "adm_phase": "阶段 D：技术",
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
      "id": "check-planning-30",
      "type": "guide:governance-check",
      "name": "所有逻辑技术交互模式是否已识别？",
      "attributes": {
        "source_check_id": "planning-30",
        "step": 5,
        "adm_phase": "阶段 D：技术",
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
      "id": "check-planning-31",
      "type": "guide:governance-check",
      "name": "所有逻辑技术执行环境、域与位置是否已识别？",
      "attributes": {
        "source_check_id": "planning-31",
        "step": 5,
        "adm_phase": "阶段 D：技术",
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
      "id": "check-planning-32",
      "type": "guide:governance-check",
      "name": "所有技术运营支持、维护、治理流程与资源是否已识别？",
      "attributes": {
        "source_check_id": "planning-32",
        "step": 5,
        "adm_phase": "阶段 D：技术",
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
      "id": "check-planning-33",
      "type": "guide:governance-check",
      "name": "所有技术原则、政策与标准是否已审查，并批准了任何偏离？",
      "attributes": {
        "source_check_id": "planning-33",
        "step": 5,
        "adm_phase": "阶段 D：技术",
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
      "id": "check-planning-34",
      "type": "guide:governance-check",
      "name": "所需安全组件、位置与政策是否已识别？",
      "attributes": {
        "source_check_id": "planning-34",
        "step": 5,
        "adm_phase": "阶段 X：安全",
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
      "id": "check-planning-35",
      "type": "guide:governance-check",
      "name": "所有安全运营支持、维护、治理流程与资源是否已识别？",
      "attributes": {
        "source_check_id": "planning-35",
        "step": 5,
        "adm_phase": "阶段 X：安全",
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
      "id": "check-planning-36",
      "type": "guide:governance-check",
      "name": "所有安全原则、政策与标准是否已审查，并批准了任何偏离？",
      "attributes": {
        "source_check_id": "planning-36",
        "step": 5,
        "adm_phase": "阶段 X：安全",
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
      "id": "check-planning-37",
      "type": "guide:governance-check",
      "name": "所有过渡架构是否已识别？",
      "attributes": {
        "source_check_id": "planning-37",
        "step": 6,
        "adm_phase": "阶段 E：机会与解决方案",
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
      "id": "check-planning-38",
      "type": "guide:governance-check",
      "name": "每个相关过渡架构的活动是否已识别？",
      "attributes": {
        "source_check_id": "planning-38",
        "step": 6,
        "adm_phase": "阶段 E：机会与解决方案",
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
      "id": "check-planning-39",
      "type": "guide:governance-check",
      "name": "相关利益相关者是否已签署过渡架构？",
      "attributes": {
        "source_check_id": "planning-39",
        "step": 6,
        "adm_phase": "阶段 E：机会与解决方案",
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
      "id": "check-planning-40",
      "type": "guide:governance-check",
      "name": "每个相关过渡架构的所有解决方案组件及其交互是否已识别？",
      "attributes": {
        "source_check_id": "planning-40",
        "step": 7,
        "adm_phase": "阶段 E：机会与解决方案",
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
      "id": "check-planning-41",
      "type": "guide:governance-check",
      "name": "相关利益相关者是否已签署每个过渡架构的解决方案组件规格？",
      "attributes": {
        "source_check_id": "planning-41",
        "step": 7,
        "adm_phase": "阶段 E：机会与解决方案",
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
      "id": "check-planning-42",
      "type": "guide:governance-check",
      "name": "所有相关原则、政策与标准是否已审查，并批准了任何偏离？",
      "attributes": {
        "source_check_id": "planning-42",
        "step": 7,
        "adm_phase": "阶段 E：机会与解决方案",
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
      "id": "check-planning-43",
      "type": "guide:governance-check",
      "name": "所有解决方案组件提供方是否已识别，连同其大纲合同与承诺？",
      "attributes": {
        "source_check_id": "planning-43",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
      "id": "check-planning-44",
      "type": "guide:governance-check",
      "name": "风险是否已识别并评估？",
      "attributes": {
        "source_check_id": "planning-44",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
      "id": "check-planning-45",
      "type": "guide:governance-check",
      "name": "所有运营支持、维护、治理流程与资源是否已识别？",
      "attributes": {
        "source_check_id": "planning-45",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
      "id": "check-planning-46",
      "type": "guide:governance-check",
      "name": "预期价值是否已最终确定？",
      "attributes": {
        "source_check_id": "planning-46",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
      "id": "check-planning-47",
      "type": "guide:governance-check",
      "name": "详细计划与估算是否已完成？",
      "attributes": {
        "source_check_id": "planning-47",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
      "id": "check-planning-48",
      "type": "guide:governance-check",
      "name": "相关利益相关者是否已批准详细计划与估算？",
      "attributes": {
        "source_check_id": "planning-48",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
      "id": "check-planning-49",
      "type": "guide:governance-check",
      "name": "相关利益相关者是否已批准拟议大纲合同与承诺？",
      "attributes": {
        "source_check_id": "planning-49",
        "step": 8,
        "adm_phase": "阶段 F：迁移规划",
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
    "id": "v-change-profile-planning-checklist",
    "artifact_id": "change-profile-governance-checklist",
    "profile_id": "change-profile-planning-checklist",
    "title": "变革画像规划检查",
    "entity_ids": [
      "check-planning-01",
      "check-planning-02",
      "check-planning-03",
      "check-planning-04",
      "check-planning-05",
      "check-planning-06",
      "check-planning-07",
      "check-planning-08",
      "check-planning-09",
      "check-planning-10",
      "check-planning-11",
      "check-planning-12",
      "check-planning-13",
      "check-planning-14",
      "check-planning-15",
      "check-planning-16",
      "check-planning-17",
      "check-planning-18",
      "check-planning-19",
      "check-planning-20",
      "check-planning-21",
      "check-planning-22",
      "check-planning-23",
      "check-planning-24",
      "check-planning-25",
      "check-planning-26",
      "check-planning-27",
      "check-planning-28",
      "check-planning-29",
      "check-planning-30",
      "check-planning-31",
      "check-planning-32",
      "check-planning-33",
      "check-planning-34",
      "check-planning-35",
      "check-planning-36",
      "check-planning-37",
      "check-planning-38",
      "check-planning-39",
      "check-planning-40",
      "check-planning-41",
      "check-planning-42",
      "check-planning-43",
      "check-planning-44",
      "check-planning-45",
      "check-planning-46",
      "check-planning-47",
      "check-planning-48",
      "check-planning-49"
    ],
    "relationship_ids": [],
    "analysis": "原料：社区服务预约上线采用Functional画像，只有访谈、KPI草案和部署演练记录。先按源表筛建议项，再逐项核对证据。可支持的三项仍只为示例，其他项保持待证据/待裁剪；不能据此批准上线。",
    "legend": "同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile change-profile-planning-checklist --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile change-profile-planning-checklist --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
