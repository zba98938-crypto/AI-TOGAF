# MSA数据分布、分片与批次条件表

`profile_id`: msa-data-distribution-conditions；`artifact_id`: data-dissemination-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21I §3.3、§8.1、§10.4.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "msa-data-distribution-conditions",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:msa_data_distribution。关系类型：。

```json
{
  "entities": {
    "guide:msa_data_distribution": [
      "data",
      "store",
      "owner_service",
      "replica_role",
      "shard_strategy",
      "external_provider",
      "transfer_direction",
      "frequency_trigger",
      "freshness_limit",
      "security",
      "retention",
      "migration",
      "access_rule"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每副本有源与陈旧性处理
- 批流标频次或触发
- 实体密级不能低于属性最高
- 不默认跨库共享

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/msa-data-distribution-conditions/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/msa-data-distribution-conditions/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构资格服务为保持运行独立性每晚经受控导出取得读者资格快照；两分片按项目readerId哈希策略，保留2版本。快照超过24小时拒绝肯定资格并转人工。缓存不超过快照有效期，属性密级按项目internal<confidential取最高；没有直接跨服务数据库访问。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MSD-01",
      "type": "guide:msa_data_distribution",
      "name": "借阅资格服务本地读者快照",
      "attributes": {
        "data": "reader_eligibility_snapshot",
        "store": "eligibility-read-store",
        "owner_service": "MS-eligibility",
        "replica_role": "独立服务本地只读副本",
        "shard_strategy": "项目选择按readerId哈希分2片；不是TOGAF规定",
        "external_provider": "读者主数据服务",
        "transfer_direction": "主数据导出→资格快照",
        "frequency_trigger": "每晚02:00受控批次；失败重试并通知值班",
        "freshness_limit": "项目规定≤24小时；过期拒绝返回肯定资格并转人工",
        "security": {
          "readerId": "internal",
          "eligibilityReason": "confidential",
          "entity_level": "confidential",
          "rule": "项目密级顺序，取最高属性"
        },
        "retention": "保留最近2版本用于恢复；时间依据为项目试点",
        "migration": "上线前全量受控导入，之后增量批次",
        "access_rule": "不直接访问另一微服务数据库；消费已发布导出契约"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MSD-02",
      "type": "guide:msa_data_distribution",
      "name": "资格缓存",
      "attributes": {
        "data": "eligibility_response_cache",
        "store": "eligibility-cache",
        "owner_service": "MS-eligibility",
        "replica_role": "同服务缓存，不是新的业务实体",
        "shard_strategy": "不分片；项目流量试验后复评",
        "external_provider": "本服务快照",
        "transfer_direction": "快照计算→本服务缓存",
        "frequency_trigger": "按查询生成；快照版本更新失效",
        "freshness_limit": "不超过当前快照版本的有效期",
        "security": {
          "readerId": "internal",
          "eligibilityReason": "confidential",
          "entity_level": "confidential",
          "rule": "沿用项目最高属性规则"
        },
        "retention": "随快照失效；不长期保留原始证件",
        "migration": "无需跨服务库迁移，版本切换清空",
        "access_rule": "仅本服务进程可访问"
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
    "id": "v-msa-data-distribution-conditions",
    "artifact_id": "data-dissemination-diagram",
    "profile_id": "msa-data-distribution-conditions",
    "title": "MSA数据分布、分片与批次条件表",
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
      "MSD-01",
      "MSD-02"
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-data-distribution-conditions --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-data-distribution-conditions --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
