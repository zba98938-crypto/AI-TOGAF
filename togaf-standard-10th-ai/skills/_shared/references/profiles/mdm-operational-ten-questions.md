# C-MDM十问运营诊断

`profile_id`: mdm-operational-ten-questions；`artifact_id`: customer-mdm-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B 附录A.1–A.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "mdm-operational-ten-questions",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:mdm_diagnostic_answer。关系类型：。

```json
{
  "entities": {
    "guide:mdm_diagnostic_answer": [
      "question_number",
      "question",
      "answer",
      "evidence_detail",
      "consequence",
      "action",
      "owner",
      "scope",
      "scoring"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 十问各一条且编号不重复
- 未知必须有需补证据行动
- 不适用必须有范围理由
- 无总分/权重/合格线

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/mdm-operational-ten-questions/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/mdm-operational-ten-questions/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构三馆读者主数据试点：已有用例清单但未连路线；同意请求流程未知；有0.2愿景/四平台态草案；架构师与管家参与但所有者未定；字典无变更历史；问题簿有负责人；没有量化质量证据；暂不使用外部数据。逐问判断须保留这些证据与未知，不计算总分。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MDM-Q01",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断1",
      "attributes": {
        "question_number": 1,
        "question": "用例是否被管理并驱动C-MDM愿景与路线图？",
        "answer": "partial",
        "evidence_detail": "用例清单存在但无优先级到路线的引用",
        "consequence": "未证明的能力不能标通过",
        "action": "补用例—路线追溯",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q02",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断2",
      "attributes": {
        "question_number": 2,
        "question": "C-MDM是否加速集中同意/偏好及数据法规客户请求管理？",
        "answer": "unknown",
        "evidence_detail": "仅知道有同意字段，无客户请求记录",
        "consequence": "未证明的能力不能标通过",
        "action": "访谈隐私负责人并收集请求流程",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q03",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断3",
      "attributes": {
        "question_number": 3,
        "question": "是否定义C-MDM战略愿景与路线图？",
        "answer": "yes",
        "evidence_detail": "版本0.2愿景和四平台态草案已记录",
        "consequence": "按试点范围保留判断",
        "action": "业务负责人审阅并说明批准状态",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q04",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断4",
      "attributes": {
        "question_number": 4,
        "question": "是否有架构师/管理员/管家/所有者组成的运营数据管理团队？",
        "answer": "partial",
        "evidence_detail": "有架构师和管家，数据所有者未正式参与",
        "consequence": "未证明的能力不能标通过",
        "action": "明确跨馆所有者参与职责",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q05",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断5",
      "attributes": {
        "question_number": 5,
        "question": "是否识别业务数据所有者并让其参与？",
        "answer": "no",
        "evidence_detail": "三馆均认为另一馆拥有黄金记录",
        "consequence": "未证明的能力不能标通过",
        "action": "指定按属性负责的业务所有者",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q06",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断6",
      "attributes": {
        "question_number": 6,
        "question": "是否识别客户数据管家？",
        "answer": "yes",
        "evidence_detail": "试点管家已在值班安排列名",
        "consequence": "按试点范围保留判断",
        "action": "验证可用容量",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q07",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断7",
      "attributes": {
        "question_number": 7,
        "question": "客户数据文档是否共享并维护？",
        "answer": "partial",
        "evidence_detail": "字典共享但无变更历史",
        "consequence": "未证明的能力不能标通过",
        "action": "补版本/责任和更新工作流",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q08",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断8",
      "attributes": {
        "question_number": 8,
        "question": "客户数据/质量问题是否捕获并妥善管理？",
        "answer": "yes",
        "evidence_detail": "问题簿有编号、负责人和复核日期",
        "consequence": "按试点范围保留判断",
        "action": "持续核对关闭证据",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q09",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断9",
      "attributes": {
        "question_number": 9,
        "question": "是否量测质量并管理改进？",
        "answer": "no",
        "evidence_detail": "只有“质量好”的口头判断",
        "consequence": "未证明的能力不能标通过",
        "action": "定义业务质量规则与观测口径",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDM-Q10",
      "type": "guide:mdm_diagnostic_answer",
      "name": "诊断10",
      "attributes": {
        "question_number": 10,
        "question": "外部数据是否为改进关键轴？",
        "answer": "not-applicable-with-reason",
        "evidence_detail": "试点只使用本馆合法采集的数据，外部数据无已识别用例",
        "consequence": "按试点范围保留判断",
        "action": "如将来增加来源重评",
        "owner": "跨馆数据治理负责人",
        "scope": "三馆试点，2026-11",
        "scoring": "none；十问无综合分数"
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
    "id": "v-mdm-operational-ten-questions",
    "artifact_id": "customer-mdm-model",
    "profile_id": "mdm-operational-ten-questions",
    "title": "C-MDM十问运营诊断",
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
      "MDM-Q01",
      "MDM-Q02",
      "MDM-Q03",
      "MDM-Q04",
      "MDM-Q05",
      "MDM-Q06",
      "MDM-Q07",
      "MDM-Q08",
      "MDM-Q09",
      "MDM-Q10"
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-operational-ten-questions --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-operational-ten-questions --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
