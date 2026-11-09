# DBRM四域十要素适用性

`profile_id`: dbrm-element-applicability；`artifact_id`: digital-business-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H §1.2、§1.4、§3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "dbrm-element-applicability",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:dbrm_applicability。关系类型：。

```json
{
  "entities": {
    "guide:dbrm_applicability": [
      "dbrm_domain_id",
      "dbrm_domain",
      "element_id",
      "element",
      "reference_identity",
      "local_mapping",
      "local_evidence",
      "applicability",
      "gap",
      "tailoring_reason",
      "relationship_boundary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 四域十要素完整
- 不生成成熟度分数
- 参考图未定向关系不能改成因果

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
      "id": "DM-DBRM-digital-1",
      "type": "guide:dbrm_applicability",
      "name": "客户聚焦",
      "attributes": {
        "dbrm_domain_id": "DBRM-digital",
        "dbrm_domain": "数字域",
        "element_id": "DBRM-digital-1",
        "element": "客户聚焦",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "受理等待不确定与无障碍需求",
        "local_evidence": "R03",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-digital-2",
      "type": "guide:dbrm_applicability",
      "name": "数字企业",
      "attributes": {
        "dbrm_domain_id": "DBRM-digital",
        "dbrm_domain": "数字域",
        "element_id": "DBRM-digital-2",
        "element": "数字企业",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "线上状态查询与人工渠道协同",
        "local_evidence": "R03",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-strategic-1",
      "type": "guide:dbrm_applicability",
      "name": "战略语境",
      "attributes": {
        "dbrm_domain_id": "DBRM-strategic",
        "dbrm_domain": "战略域",
        "element_id": "DBRM-strategic-1",
        "element": "战略语境",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "跨科室协同及公众可访问性",
        "local_evidence": "R04",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-strategic-2",
      "type": "guide:dbrm_applicability",
      "name": "业务动机",
      "attributes": {
        "dbrm_domain_id": "DBRM-strategic",
        "dbrm_domain": "战略域",
        "element_id": "DBRM-strategic-2",
        "element": "业务动机",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "可靠确认目标；未给数值收益",
        "local_evidence": "R04",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-strategic-3",
      "type": "guide:dbrm_applicability",
      "name": "业务服务与产品",
      "attributes": {
        "dbrm_domain_id": "DBRM-strategic",
        "dbrm_domain": "战略域",
        "element_id": "DBRM-strategic-3",
        "element": "业务服务与产品",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "养老申请与状态查询服务",
        "local_evidence": "R04",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-structural-1",
      "type": "guide:dbrm_applicability",
      "name": "生态与业务模型",
      "attributes": {
        "dbrm_domain_id": "DBRM-structural",
        "dbrm_domain": "结构域",
        "element_id": "DBRM-structural-1",
        "element": "生态与业务模型",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "财政、待遇台和协作平台边界",
        "local_evidence": "R04",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-structural-2",
      "type": "guide:dbrm_applicability",
      "name": "运营模式",
      "attributes": {
        "dbrm_domain_id": "DBRM-structural",
        "dbrm_domain": "结构域",
        "element_id": "DBRM-structural-2",
        "element": "运营模式",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "客户可访问性优先及人力约束",
        "local_evidence": "R08",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-structural-3",
      "type": "guide:dbrm_applicability",
      "name": "业务能力模型",
      "attributes": {
        "dbrm_domain_id": "DBRM-structural",
        "dbrm_domain": "结构域",
        "element_id": "DBRM-structural-3",
        "element": "业务能力模型",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "受理/核验；不直接把政府功能当能力",
        "local_evidence": "R04",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-operational-1",
      "type": "guide:dbrm_applicability",
      "name": "业务运营环境",
      "attributes": {
        "dbrm_domain_id": "DBRM-operational",
        "dbrm_domain": "运营域",
        "element_id": "DBRM-operational-1",
        "element": "业务运营环境",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "受理流程、字段和角色交接",
        "local_evidence": "R09",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
      "id": "DM-DBRM-operational-2",
      "type": "guide:dbrm_applicability",
      "name": "数字使能",
      "attributes": {
        "dbrm_domain_id": "DBRM-operational",
        "dbrm_domain": "运营域",
        "element_id": "DBRM-operational-2",
        "element": "数字使能",
        "reference_identity": "G21H四域十要素；不是TOGAF架构域",
        "local_mapping": "平台、权限和交付责任草案",
        "local_evidence": "R07",
        "applicability": "candidate-applicable",
        "gap": "尚需本地责任人复核，未计算数字成熟度",
        "tailoring_reason": "R03–R09试点范围；保留全部参考要素以明确覆盖边界",
        "relationship_boundary": "图3-1只表关系存在；本表不赋方向或类型"
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
    "id": "v-dbrm-element-applicability",
    "artifact_id": "digital-business-reference-tailoring",
    "profile_id": "dbrm-element-applicability",
    "title": "DBRM四域十要素适用性",
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
      "DM-DBRM-digital-1",
      "DM-DBRM-digital-2",
      "DM-DBRM-strategic-1",
      "DM-DBRM-strategic-2",
      "DM-DBRM-strategic-3",
      "DM-DBRM-structural-1",
      "DM-DBRM-structural-2",
      "DM-DBRM-structural-3",
      "DM-DBRM-operational-1",
      "DM-DBRM-operational-2"
    ],
    "relationship_ids": [],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dbrm-element-applicability --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dbrm-element-applicability --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
