# coding: utf-8
"""Bind metadata calculator snapshots to current project records, not names.

This is a project consistency check, not a TOGAF certification rule. Source
kind=example and operational evidence kind=observation are different axes.
"""

METHOD_ID = 'metadata-application-coverage-review'


def binding_issues(model, analysis):
    """Return structured errors; never mutate or silently migrate the model."""
    if analysis.get('method_id') != METHOD_ID:
        return []
    findings = []
    aid = analysis.get('id', 'metadata-analysis')

    def issue(code, identity, message):
        findings.append({'level': 'error', 'code': 'metadata-binding-' + code,
                         'id': str(aid) + ':' + str(identity),
                         'message': message + '；重新审查并同步当前模型与分析，禁止沿用旧结论。'})

    def index(rows, label):
        result = {}
        for record in rows:
            identity = record.get('id')
            if not identity or identity in result:
                issue('identity', label, '缺少或重复稳定ID')
            else:
                result[identity] = record
        return result

    data = analysis.get('inputs', {})
    entities = index(model.get('entities', []), 'entities')
    relations = index(model.get('relationships', []), 'relationships')
    known_sources = {s.get('id') for s in model.get('sources', [])}
    declared_sources = set(data.get('source_ids', []))
    for sid in declared_sources - known_sources:
        issue('source', sid, '分析来源不在当前模型sources中')

    # Evidence shape and inventories are checked by analysis_evidence.
    expected_entities = set()
    expected_relations = set()
    for key, typ in [('tools', 'g234:metadata-tool'), ('assets', 'metadata_asset')]:
        records = index(data.get(key, []), key)
        for identity, snapshot in records.items():
            expected_entities.add(identity)
            current = entities.get(identity)
            if not current or current.get('type') != typ:
                issue('entity', identity, '分析工具/资产缺少同ID同类型实体')
                continue
            attrs = current.get('attributes', {})
            from analysis_projection_binding import MISSING, _equal
            consumed = {'id', 'name', 'version', 'owner', 'evidence'} if key == 'tools' else {'id', 'name', 'category', 'category_name', 'owner', 'evidence'}
            for field in set(snapshot) | consumed:
                if field == 'id':
                    continue
                value = snapshot.get(field, MISSING)
                actual = current.get('name', MISSING) if field == 'name' else attrs.get(field, MISSING)
                if not _equal(actual, value):
                    issue('field', identity + '.' + field, '当前实体字段与分析快照不一致')
            if current.get('evidence') != snapshot.get('evidence'):
                issue('field', identity + '.evidence', '实体来源与分析来源不一致')
            if key == 'tools' and current.get('version') is not None and current['version'] != snapshot.get('version'):
                issue('field', identity + '.version', '实体工具版本与分析版本不一致')

    assessments = index(data.get('assessments', []), 'assessments')
    if not expected_entities and not assessments:
        issue('required', 'inputs', '覆盖分析没有可绑定的工具、资产或审查记录')
    computed = {}
    try:
        from metadata_coverage_analysis import review_metadata_coverage
        computed = {r['id']: r for r in review_metadata_coverage(data)['rows']}
    except (ValueError, KeyError, TypeError) as exc:
        issue('evaluation', aid, str(exc))
    for identity, snapshot in assessments.items():
        expected_entities.add(identity)
        current = entities.get(identity)
        if not current or current.get('type') != 'g234:function-coverage':
            issue('entity', identity, '审查快照缺少同ID功能覆盖实体')
            continue
        attrs = current.get('attributes', {})
        fields = {'assessment': snapshot, 'source_function_id': snapshot.get('function_id'),
                  'project_scope': data.get('scope'), 'architecture_state': data.get('architecture_state'),
                  'as_of': data.get('as_of')}
        if identity in computed:
            result = computed[identity]
            fields.update(analysis_result=result, coverage_status=result['status'],
                          source_group=result['group'], source_definition=result.get('source_definition'))
        for field, value in fields.items():
            if attrs.get(field) != value:
                issue('field', identity + '.' + field, '功能审查范围、状态、日期、快照或计算结果未同步')
        # Asset relation IDs are not prescribed: match semantic endpoints.
        actual_edges = [r for r in relations.values()
                        if r.get('type') == 'g234:coverage-of-asset' and r.get('source') == identity]
        wanted_assets = set(snapshot.get('required_asset_ids', []))
        if {r.get('target') for r in actual_edges} != wanted_assets or len(actual_edges) != len(wanted_assets):
            issue('asset-relations', identity, '审查资产关系与required_asset_ids不一致或重复')
        expected_relations.update(r['id'] for r in actual_edges)
        for binding in snapshot.get('bindings', []):
            bid = binding.get('id')
            expected_relations.add(bid)
            relation = relations.get(bid)
            if not relation or (relation.get('type'), relation.get('source'), relation.get('target')) != (
                    'g234:tool-coverage-claim', binding.get('tool_id'), identity):
                issue('claim-relation', bid, '工具声明关系缺失或端点/方向不一致')
                continue
            ra = relation.get('attributes', {})
            for field in ['tool_version', 'asset_ids', 'facet_ids']:
                if ra.get(field) != binding.get(field):
                    issue('claim-field', str(bid) + '.' + field, '声明关系字段与绑定不一致')
            # Existing examples use claimed_status; full binding projections use status.
            state_keys = [k for k in ['claimed_status', 'status'] if k in ra]
            if not state_keys or any(ra[k] != binding.get('status') for k in state_keys):
                issue('claim-field', bid, '声明关系状态与绑定不一致')
            for field in ['verification', 'plan', 'tool_id', 'id']:
                if field in ra and ra[field] != binding.get(field):
                    issue('claim-field', str(bid) + '.' + field, '声明关系扩展快照已过期')
        actual_claims = {r['id'] for r in relations.values()
                         if r.get('type') == 'g234:tool-coverage-claim' and r.get('target') == identity}
        if actual_claims != {b.get('id') for b in snapshot.get('bindings', [])}:
            issue('claim-relations', identity, '审查工具声明关系集合与绑定集合不一致')

    for view in model.get('views', []):
        if aid not in view.get('attributes', {}).get('analysis_ids', []):
            continue
        if set(view.get('entity_ids', [])) != expected_entities:
            issue('view-entities', view.get('id'), '完整覆盖评估视图的对象集合与分析范围不同')
        if set(view.get('relationship_ids', [])) != expected_relations:
            issue('view-relations', view.get('id'), '完整覆盖评估视图的关系集合与分析范围不同')
    return findings
