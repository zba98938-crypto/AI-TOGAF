# 企业框架接触与承诺目录

`profile_id`: enterprise-framework-alignment-catalog-default；`artifact_id`: enterprise-framework-alignment-catalog；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §7.1–7.2、§10.1、§13.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "enterprise-framework-alignment-catalog-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "正文工作产品的字段表；不冒称原图复刻。reference/adaptive均保留全部列语义。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:framework_touchpoint。关系类型：。

```json
{
  "entities": {
    "guide:framework_touchpoint": [
      "framework",
      "focus",
      "commitment_evidence",
      "actual_commitment",
      "owner",
      "touchpoint",
      "ea_input",
      "ea_output",
      "gap",
      "action"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不把框架目录当企业已采用清单
- 承诺深度由证据叙述，不凭空创建评分
- 框架重叠不表示包含或优先级，优先级须组织规则

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-enterprise-framework-alignment-catalog-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：frameworks",
      "locator": "examples/addenda/governance/raw-business-materials.json#frameworks"
    }
  ],
  "entities": [
    {
      "id": "enterprise-framework-alignment-catalog-default-1",
      "type": "guide:framework_touchpoint",
      "name": "项目拨款关卡",
      "attributes": {
        "framework": "企业PMO项目管理规程2026",
        "focus": "规划与执行",
        "commitment_evidence": "FW-01最近三次关卡记录",
        "actual_commitment": "已在使用，证据为本虚构案例",
        "owner": "PMO负责人",
        "touchpoint": "章程批准前／月度例外会",
        "ea_input": "范围、预算、资源与已知依赖",
        "ea_output": "架构契约、工作包依赖及例外影响",
        "gap": "关卡尚未引用具体view_id",
        "action": "融入：在章程模板新增架构契约和视图版本引用"
      },
      "evidence": [
        "src-enterprise-framework-alignment-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "enterprise-framework-alignment-catalog-default-2",
      "type": "guide:framework_touchpoint",
      "name": "风险季审",
      "attributes": {
        "framework": "企业ERM风险制度2026",
        "focus": "治理与风险",
        "commitment_evidence": "FW-02季度风险复核记录",
        "actual_commitment": "已在使用",
        "owner": "风险负责人",
        "touchpoint": "候选目标、路线批准前及季度复评",
        "ea_input": "风险偏好、风险登记、影响分析",
        "ea_output": "架构风险、控制与价值不确定性",
        "gap": "尚无架构风险移交字段",
        "action": "补位：定义风险ID、架构状态、控制责任和回执，再由风险部承接"
      },
      "evidence": [
        "src-enterprise-framework-alignment-catalog-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "enterprise-framework-alignment-catalog-default-3",
      "type": "guide:framework_touchpoint",
      "name": "COBIT采用声明",
      "attributes": {
        "framework": "COBIT，版本待核实",
        "focus": "信息系统治理",
        "commitment_evidence": "FW-03只有口头名称",
        "actual_commitment": "声明但无实质承诺证据",
        "owner": "未任命",
        "touchpoint": "未建立",
        "ea_input": "待获取采用范围/版本/负责人",
        "ea_output": "待确认对齐需求",
        "gap": "无法证明实际采用",
        "action": "先核实；不得把参考框架名当已存在治理能力"
      },
      "evidence": [
        "src-enterprise-framework-alignment-catalog-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-enterprise-framework-alignment-catalog-default",
    "artifact_id": "enterprise-framework-alignment-catalog",
    "profile_id": "enterprise-framework-alignment-catalog-default",
    "title": "企业框架接触与承诺目录",
    "entity_ids": [
      "enterprise-framework-alignment-catalog-default-1",
      "enterprise-framework-alignment-catalog-default-2",
      "enterprise-framework-alignment-catalog-default-3"
    ],
    "relationship_ids": [],
    "analysis": "FW-01/02已有实际流程，EA分别融入拨款和补齐风险移交；FW-03只有术语承诺，保留未知而不赋成熟度分。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "frameworks"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile enterprise-framework-alignment-catalog-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile enterprise-framework-alignment-catalog-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
