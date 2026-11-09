# EA服务N／P／D语境矩阵

`profile_id`: ea-service-emergence-npd；`artifact_id`: ea-service-catalog；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G217 §4.4.1–4.4.5，图4-3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "ea-service-emergence-npd",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:ea_service_context。关系类型：。

```json
{
  "entities": {
    "guide:ea_service_context": [
      "service",
      "context",
      "emergence",
      "meaning",
      "local_depth",
      "evidence_detail",
      "mapping_origin",
      "source_cell_status",
      "resources"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- D有深化说明
- P/D前应有已引入历史
- 未引入不能误用D
- 项目映射不得标为原图逐格复刻

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/ea-service-emergence-npd/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/ea-service-emergence-npd/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构数字借阅团队回顾：创始阶段已做价值评估；团队阶段引入变更建议，价值评估范围沿用；团队之团队阶段价值评估增加跨产品依赖风险；持久企业阶段两者继续深化且首次引入合规准则服务。这里只声称项目映射，原图逐格关系尚未核实。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "EA-01",
      "type": "guide:ea_service_context",
      "name": "价值评估／语境1",
      "attributes": {
        "service": "价值评估",
        "context": "Context 1",
        "emergence": "N",
        "meaning": "首次引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-02",
      "type": "guide:ea_service_context",
      "name": "价值评估／语境2",
      "attributes": {
        "service": "价值评估",
        "context": "Context 2",
        "emergence": "P",
        "meaning": "之前已引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-03",
      "type": "guide:ea_service_context",
      "name": "价值评估／语境3",
      "attributes": {
        "service": "价值评估",
        "context": "Context 3",
        "emergence": "D",
        "meaning": "执行深度增加",
        "local_depth": "两个产品共同评估依赖/风险",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-04",
      "type": "guide:ea_service_context",
      "name": "价值评估／语境4",
      "attributes": {
        "service": "价值评估",
        "context": "Context 4",
        "emergence": "D",
        "meaning": "执行深度增加",
        "local_depth": "两个产品共同评估依赖/风险",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-05",
      "type": "guide:ea_service_context",
      "name": "变更建议／语境1",
      "attributes": {
        "service": "变更建议",
        "context": "Context 1",
        "emergence": "not-introduced",
        "meaning": "本项目该语境未引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-06",
      "type": "guide:ea_service_context",
      "name": "变更建议／语境2",
      "attributes": {
        "service": "变更建议",
        "context": "Context 2",
        "emergence": "N",
        "meaning": "首次引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-07",
      "type": "guide:ea_service_context",
      "name": "变更建议／语境3",
      "attributes": {
        "service": "变更建议",
        "context": "Context 3",
        "emergence": "P",
        "meaning": "之前已引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-08",
      "type": "guide:ea_service_context",
      "name": "变更建议／语境4",
      "attributes": {
        "service": "变更建议",
        "context": "Context 4",
        "emergence": "D",
        "meaning": "执行深度增加",
        "local_depth": "两个产品共同评估依赖/风险",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-09",
      "type": "guide:ea_service_context",
      "name": "合规准则开发／语境1",
      "attributes": {
        "service": "合规准则开发",
        "context": "Context 1",
        "emergence": "not-introduced",
        "meaning": "本项目该语境未引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-10",
      "type": "guide:ea_service_context",
      "name": "合规准则开发／语境2",
      "attributes": {
        "service": "合规准则开发",
        "context": "Context 2",
        "emergence": "not-introduced",
        "meaning": "本项目该语境未引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-11",
      "type": "guide:ea_service_context",
      "name": "合规准则开发／语境3",
      "attributes": {
        "service": "合规准则开发",
        "context": "Context 3",
        "emergence": "not-introduced",
        "meaning": "本项目该语境未引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EA-12",
      "type": "guide:ea_service_context",
      "name": "合规准则开发／语境4",
      "attributes": {
        "service": "合规准则开发",
        "context": "Context 4",
        "emergence": "N",
        "meaning": "首次引入",
        "local_depth": "基本服务范围",
        "evidence_detail": "虚构团队服务演进会议记录；N/P/D词义来自G217",
        "mapping_origin": "project-tailoring-not-source-cell-transcription",
        "source_cell_status": "not-verified",
        "resources": "责任EA角色每周复核；容量待项目确认"
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
    "id": "v-ea-service-emergence-npd",
    "artifact_id": "ea-service-catalog",
    "profile_id": "ea-service-emergence-npd",
    "title": "EA服务N／P／D语境矩阵",
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
      "EA-01",
      "EA-02",
      "EA-03",
      "EA-04",
      "EA-05",
      "EA-06",
      "EA-07",
      "EA-08",
      "EA-09",
      "EA-10",
      "EA-11",
      "EA-12"
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-emergence-npd --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-emergence-npd --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
