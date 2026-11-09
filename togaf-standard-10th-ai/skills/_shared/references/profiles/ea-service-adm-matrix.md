# EA服务与ADM证据映射／图形

`profile_id`: ea-service-adm-matrix；`artifact_id`: ea-service-catalog；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G217 附录C.1–C.7、附录D；G217/figC-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.4。

{
  "id": "ea-service-adm-matrix",
  "version": "2.4",
  "source_verified": false,
  "source_topology": "ea-adm-matrix",
  "separate_detail_ledger": true,
  "review_status": "awaiting-source-and-business-review",
  "companion_table_profile_id": "ea-service-adm-evidence-map"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:ea_adm_mapping。关系类型：。

```json
{
  "entities": {
    "guide:ea_adm_mapping": [
      "service",
      "ADM_phase",
      "project_activity",
      "output",
      "owner",
      "mapping_origin",
      "evidence_detail",
      "source_mapping"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每条映射有来源与目的
- 制定准则和执行评估分开
- 未知保持unknown
- 不得把项目安排伪称原图精确对应

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/ea-service-adm-evidence-map/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/ea-service-adm-evidence-map/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构项目会议把价值评估用于愿景A，把消费者变化建议用于H，将合规准则准备作为G实施评审的输入。服务名称及候选目录来自G217，源图C-1具体逐格映射本轮未核实，因此这些映射只作为项目操作记录。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "EAM-01",
      "type": "guide:ea_adm_mapping",
      "name": "价值评估→阶段A",
      "attributes": {
        "service": "价值评估",
        "ADM_phase": "A",
        "project_activity": "比较跨馆试点目标与预期收益",
        "output": "愿景的价值假设与待验证指标",
        "owner": "EA顾问与业务负责人",
        "mapping_origin": "project-observation",
        "evidence_detail": "项目规划会明确A阶段使用；不是声称图C-1原格",
        "source_mapping": "unknown；待原图C-1对应格核查"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EAM-02",
      "type": "guide:ea_adm_mapping",
      "name": "变更建议→阶段H",
      "attributes": {
        "service": "变更建议",
        "ADM_phase": "H",
        "project_activity": "复核消费者增加对契约的影响",
        "output": "变更请求及影响建议",
        "owner": "接口负责人",
        "mapping_origin": "project-observation",
        "evidence_detail": "运营会议把变更建议安排在H的处理活动",
        "source_mapping": "unknown；待原图C-1对应格核查"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "EAM-03",
      "type": "guide:ea_adm_mapping",
      "name": "合规准则开发→阶段G输入",
      "attributes": {
        "service": "合规准则开发",
        "ADM_phase": "G",
        "project_activity": "将已制定的可执行准则作为实施评审输入",
        "output": "准则与检查证据要求",
        "owner": "治理负责人",
        "mapping_origin": "project-proposal",
        "evidence_detail": "本项目拟在G前准备准则；制定与合规评估结果不能混同",
        "source_mapping": "unknown；不推断图C-1仅映射G"
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
    "id": "v-ea-service-adm-matrix",
    "artifact_id": "ea-service-catalog",
    "profile_id": "ea-service-adm-matrix",
    "title": "EA服务与ADM证据映射／图形",
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
      "EAM-01",
      "EAM-02",
      "EAM-03"
    ],
    "relationship_ids": [],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "图形与表格复用同一ID；未知不等于无关系或不适用；项目映射不是原图逐格验收。",
    "allow_mixed_evolution": true
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-adm-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-adm-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
