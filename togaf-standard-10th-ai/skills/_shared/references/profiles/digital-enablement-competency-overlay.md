# 五支柱十二胜任力与本地责任

`profile_id`: digital-enablement-competency-overlay；`artifact_id`: digital-business-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H §4.2.2、§4.5.2–4.5.3 表4-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "digital-enablement-competency-overlay",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:competency_overlay。关系类型：。

```json
{
  "entities": {
    "guide:competency_overlay": [
      "source_row_id",
      "pillar",
      "competency",
      "dpbok_context",
      "context_kind",
      "local_roles",
      "current_evidence",
      "needed_competency",
      "gap",
      "action",
      "next_review",
      "reference_identity"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 12行完整且不重复
- 同一胜任力允许多个角色
- 不能把context IV打4分
- 所有缺口有关联行动

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "明确虚构项目裁剪与真实参考来源分离；源图视觉核验另记。",
  "raw_input": "examples/addenda/reference-models/raw-business-materials.json",
  "analysis_path": "examples/addenda/reference-models/analysis.md",
  "sources": [
    {
      "id": "raw",
      "kind": "example",
      "description": "虚构松川市养老服务数字化试点；实际原料见本包raw-business-materials.json；补充场景参数均明示，不代表真实审批。",
      "locator": "raw-business-materials.json"
    },
    {
      "id": "grm",
      "kind": "local-translation",
      "description": "G21D本地正文目录摘录，官方定义/图形复核另记；保留参考身份。",
      "locator": "references/source-tables/government-reference-catalog.json"
    },
    {
      "id": "dbrm",
      "kind": "local-translation",
      "description": "G21H本地正文五表摘录；原始空格/破折号保留，项目裁剪与源映射分离。",
      "locator": "references/source-tables/dbrm-reference-mappings.json"
    }
  ],
  "entities": [
    {
      "id": "CM-G21H-T4-1-R01",
      "type": "guide:competency_overlay",
      "name": "架构与组合管理",
      "attributes": {
        "source_row_id": "G21H-T4-1-R01",
        "pillar": "数字原则与战略",
        "competency": "架构与组合管理",
        "dpbok_context": "语境 IV：持久企业",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "EA-LEAD"
        ],
        "current_evidence": "架构草案；见R06/R07",
        "needed_competency": "架构与组合管理在本试点范围的可验证工作能力",
        "gap": "组合排序未定",
        "action": "由EA-LEAD补充组合排序未定的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R02",
      "type": "guide:competency_overlay",
      "name": "信息管理",
      "attributes": {
        "source_row_id": "G21H-T4-1-R02",
        "pillar": "数字原则与战略",
        "competency": "信息管理",
        "dpbok_context": "语境 IV：持久企业",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "DATA-STEWARD"
        ],
        "current_evidence": "字段字典；见R06/R07",
        "needed_competency": "信息管理在本试点范围的可验证工作能力",
        "gap": "保留规则未定",
        "action": "由DATA-STEWARD补充保留规则未定的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R03",
      "type": "guide:competency_overlay",
      "name": "数字价值构思",
      "attributes": {
        "source_row_id": "G21H-T4-1-R03",
        "pillar": "数字原则与战略",
        "competency": "数字价值构思",
        "dpbok_context": "语境 I：个人/创始人",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "P-OWNER"
        ],
        "current_evidence": "访谈与用例；见R06/R07",
        "needed_competency": "数字价值构思在本试点范围的可验证工作能力",
        "gap": "收益基线未测",
        "action": "由P-OWNER补充收益基线未测的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R04",
      "type": "guide:competency_overlay",
      "name": "治理、风险、安全与合规",
      "attributes": {
        "source_row_id": "G21H-T4-1-R04",
        "pillar": "数字治理",
        "competency": "治理、风险、安全与合规",
        "dpbok_context": "语境 IV：持久企业",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "SEC-LEAD"
        ],
        "current_evidence": "授权草案；见R06/R07",
        "needed_competency": "治理、风险、安全与合规在本试点范围的可验证工作能力",
        "gap": "缺控制/恢复演练",
        "action": "由SEC-LEAD补充缺控制/恢复演练的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R05",
      "type": "guide:competency_overlay",
      "name": "协调机制（含流程管理与 ITSM）",
      "attributes": {
        "source_row_id": "G21H-T4-1-R05",
        "pillar": "数字产品与服务",
        "competency": "协调机制（含流程管理与 ITSM）",
        "dpbok_context": "语境 III：团队之团队",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "COORD"
        ],
        "current_evidence": "交接会议；见R06/R07",
        "needed_competency": "协调机制（含流程管理与 ITSM）在本试点范围的可验证工作能力",
        "gap": "跨组异常升级需演练",
        "action": "由COORD补充跨组异常升级需演练的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R06",
      "type": "guide:competency_overlay",
      "name": "投资与寻源（含项目管理）",
      "attributes": {
        "source_row_id": "G21H-T4-1-R06",
        "pillar": "数字产品与服务",
        "competency": "投资与寻源（含项目管理）",
        "dpbok_context": "语境 III：团队之团队",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "PROCUREMENT"
        ],
        "current_evidence": "候选寻源清单；见R06/R07",
        "needed_competency": "投资与寻源（含项目管理）在本试点范围的可验证工作能力",
        "gap": "容量与成本依据待补",
        "action": "由PROCUREMENT补充容量与成本依据待补的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R07",
      "type": "guide:competency_overlay",
      "name": "产品管理",
      "attributes": {
        "source_row_id": "G21H-T4-1-R07",
        "pillar": "数字产品与服务",
        "competency": "产品管理",
        "dpbok_context": "语境 II：团队",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "P-OWNER"
        ],
        "current_evidence": "产品待办；见R06/R07",
        "needed_competency": "产品管理在本试点范围的可验证工作能力",
        "gap": "验收反馈待复核",
        "action": "由P-OWNER补充验收反馈待复核的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R08",
      "type": "guide:competency_overlay",
      "name": "组织与文化因素",
      "attributes": {
        "source_row_id": "G21H-T4-1-R08",
        "pillar": "敏捷数字交付模型",
        "competency": "组织与文化因素",
        "dpbok_context": "语境 III：团队之团队",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "TEAM-LEAD"
        ],
        "current_evidence": "协作值班表；见R06/R07",
        "needed_competency": "组织与文化因素在本试点范围的可验证工作能力",
        "gap": "跨团队责任需复核",
        "action": "由TEAM-LEAD补充跨团队责任需复核的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R09",
      "type": "guide:competency_overlay",
      "name": "工作执行",
      "attributes": {
        "source_row_id": "G21H-T4-1-R09",
        "pillar": "敏捷数字交付模型",
        "competency": "工作执行",
        "dpbok_context": "语境 II：团队",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "DELIVERY"
        ],
        "current_evidence": "工作待办；见R06/R07",
        "needed_competency": "工作执行在本试点范围的可验证工作能力",
        "gap": "依赖完成证据待补",
        "action": "由DELIVERY补充依赖完成证据待补的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R10",
      "type": "guide:competency_overlay",
      "name": "运营",
      "attributes": {
        "source_row_id": "G21H-T4-1-R10",
        "pillar": "敏捷数字交付模型",
        "competency": "运营",
        "dpbok_context": "语境 II：团队",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "OPS"
        ],
        "current_evidence": "轮值表；见R06/R07",
        "needed_competency": "运营在本试点范围的可验证工作能力",
        "gap": "缺中断恢复演练",
        "action": "由OPS补充缺中断恢复演练的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R11",
      "type": "guide:competency_overlay",
      "name": "敏捷开发与持续交付实践",
      "attributes": {
        "source_row_id": "G21H-T4-1-R11",
        "pillar": "敏捷数字交付模型",
        "competency": "敏捷开发与持续交付实践",
        "dpbok_context": "语境 I：个人/创始人",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "DELIVERY"
        ],
        "current_evidence": "构建草案；见R06/R07",
        "needed_competency": "敏捷开发与持续交付实践在本试点范围的可验证工作能力",
        "gap": "持续发布控制尚未验证",
        "action": "由DELIVERY补充持续发布控制尚未验证的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "CM-G21H-T4-1-R12",
      "type": "guide:competency_overlay",
      "name": "数字基础设施及相关实践",
      "attributes": {
        "source_row_id": "G21H-T4-1-R12",
        "pillar": "数字平台",
        "competency": "数字基础设施及相关实践",
        "dpbok_context": "语境 I：个人/创始人",
        "context_kind": "organizational-scaling-context-not-maturity-level",
        "local_roles": [
          "PLATFORM"
        ],
        "current_evidence": "试验环境；见R06/R07",
        "needed_competency": "数字基础设施及相关实践在本试点范围的可验证工作能力",
        "gap": "生产发布权限待确认",
        "action": "由PLATFORM补充生产发布权限待确认的业务证据后复评",
        "next_review": "相应工作材料或演练记录取得时，具体日待项目确认",
        "reference_identity": "G21H表4-1参考对应；不代表已具备/通过胜任力"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "view": {
    "id": "v-digital-enablement-competency-overlay",
    "artifact_id": "digital-business-reference-tailoring",
    "profile_id": "digital-enablement-competency-overlay",
    "title": "五支柱十二胜任力与本地责任",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "CM-G21H-T4-1-R01",
      "CM-G21H-T4-1-R02",
      "CM-G21H-T4-1-R03",
      "CM-G21H-T4-1-R04",
      "CM-G21H-T4-1-R05",
      "CM-G21H-T4-1-R06",
      "CM-G21H-T4-1-R07",
      "CM-G21H-T4-1-R08",
      "CM-G21H-T4-1-R09",
      "CM-G21H-T4-1-R10",
      "CM-G21H-T4-1-R11",
      "CM-G21H-T4-1-R12"
    ],
    "relationship_ids": [],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile digital-enablement-competency-overlay --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile digital-enablement-competency-overlay --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
