# MSA组织与生命周期就绪证据

`profile_id`: msa-readiness-evidence；`artifact_id`: microservice-technical-guidance；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G21I §5.2、§5.5、表5-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "msa-readiness-evidence",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "结构化表格，含完整属性、方向和证据；不是来源图模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:msa_readiness。关系类型：。

```json
{
  "entities": {
    "ops:msa_readiness": [
      "concern",
      "observation",
      "judgment",
      "owner",
      "action",
      "scope",
      "decision_consequence",
      "scoring",
      "evidence_detail"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 六关注点保持独立
- 缺退休责任不得标全生命周期完整
- 未知OSIMM不填分数
- 自治仍受企业护栏约束

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/msa-readiness-evidence/raw-brief.md",
  "analysis_path": "examples/addenda/operations/msa-readiness-evidence/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚维修准备把预约判断拆为服务。预约团队负责开发、部署与值班，却没人负责退役。两开发一轮值运维未完成恢复演练。团队可选框架，但须满足生产最小权限和可追溯变更。有自动构建测试，发布前复核和变化监控仍手工。先在一城试点，复盘组织影响再扩另一城。没有OSIMM模型或评估结果，不能给总分。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "READY-1",
      "type": "ops:msa_readiness",
      "name": "生命周期归属",
      "attributes": {
        "concern": "生命周期归属",
        "observation": "预约服务由预约团队负责开发、部署与值班；退役责任尚未分配",
        "judgment": "partial",
        "owner": "预约团队负责人",
        "action": "在试点前补齐退役和数据保留责任",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "decision_consequence": "未完事项约束试点进入；不得直接认定全企业就绪",
        "scoring": {
          "scheme": "none",
          "score": null,
          "basis": "G21I只引用OSIMM，未提供本地可用评分规则"
        },
        "evidence_detail": "虚构访谈2026-11-02，原料逐项说明"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "READY-2",
      "type": "ops:msa_readiness",
      "name": "技能与容量",
      "attributes": {
        "concern": "技能与容量",
        "observation": "两开发和一轮值运维能发布；无人完成故障恢复演练",
        "judgment": "partial",
        "owner": "工程负责人",
        "action": "导师支持恢复演练，记录技能与值班容量",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "decision_consequence": "未完事项约束试点进入；不得直接认定全企业就绪",
        "scoring": {
          "scheme": "none",
          "score": null,
          "basis": "G21I只引用OSIMM，未提供本地可用评分规则"
        },
        "evidence_detail": "虚构访谈2026-11-02，原料逐项说明"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "READY-3",
      "type": "ops:msa_readiness",
      "name": "自治与企业约束",
      "attributes": {
        "concern": "自治与企业约束",
        "observation": "团队能选框架；企业要求生产最小权限与可追溯变更",
        "judgment": "bounded-autonomy",
        "owner": "项目架构师",
        "action": "选择须映射护栏，偏离申请交评审委员会",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "decision_consequence": "未完事项约束试点进入；不得直接认定全企业就绪",
        "scoring": {
          "scheme": "none",
          "score": null,
          "basis": "G21I只引用OSIMM，未提供本地可用评分规则"
        },
        "evidence_detail": "虚构访谈2026-11-02，原料逐项说明"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "READY-4",
      "type": "ops:msa_readiness",
      "name": "敏捷与DevOps",
      "attributes": {
        "concern": "敏捷与DevOps",
        "observation": "有自动构建测试；发布前复核与变化监控仍靠手工",
        "judgment": "partial",
        "owner": "DevOps负责人",
        "action": "验证适当层级发布复核并补监控证据",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "decision_consequence": "未完事项约束试点进入；不得直接认定全企业就绪",
        "scoring": {
          "scheme": "none",
          "score": null,
          "basis": "G21I只引用OSIMM，未提供本地可用评分规则"
        },
        "evidence_detail": "虚构访谈2026-11-02，原料逐项说明"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "READY-5",
      "type": "ops:msa_readiness",
      "name": "试点学习",
      "attributes": {
        "concern": "试点学习",
        "observation": "先在一个城市试点预约服务，复盘后决定另一城扩展",
        "judgment": "planned",
        "owner": "业务赞助人",
        "action": "观察服务可运营性、组织影响及失败恢复",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "decision_consequence": "未完事项约束试点进入；不得直接认定全企业就绪",
        "scoring": {
          "scheme": "none",
          "score": null,
          "basis": "G21I只引用OSIMM，未提供本地可用评分规则"
        },
        "evidence_detail": "虚构访谈2026-11-02，原料逐项说明"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "READY-6",
      "type": "ops:msa_readiness",
      "name": "SOA成熟度",
      "attributes": {
        "concern": "SOA成熟度",
        "observation": "未取得OSIMM原模型和组织评估结果",
        "judgment": "unknown",
        "owner": "企业架构师",
        "action": "取得外部模型并单独立项评估，不用本表合成分数",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "decision_consequence": "未完事项约束试点进入；不得直接认定全企业就绪",
        "scoring": {
          "scheme": "none",
          "score": null,
          "basis": "G21I只引用OSIMM，未提供本地可用评分规则"
        },
        "evidence_detail": "虚构访谈2026-11-02，原料逐项说明"
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
    "id": "v-msa-readiness-evidence",
    "artifact_id": "microservice-technical-guidance",
    "profile_id": "msa-readiness-evidence",
    "title": "MSA组织与生命周期就绪证据",
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
      "READY-1",
      "READY-2",
      "READY-3",
      "READY-4",
      "READY-5",
      "READY-6"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-readiness-evidence --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-readiness-evidence --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
