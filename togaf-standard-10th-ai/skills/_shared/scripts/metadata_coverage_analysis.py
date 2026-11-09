# coding: utf-8
"""Project coverage against G234 table 5-2, without inferring implementation.

The source-derived functional universe lives inside skills. Operational evidence
rules are explicit project conventions, not TOGAF maturity or product scores.
"""
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from evidence_analysis import require, unique, evidence, sources

ROOT = Path(__file__).resolve().parents[1]
STATUSES = ('implemented', 'planned', 'unknown', 'not-applicable')


def universe():
    path = ROOT / 'references/source-tables/metadata-application-coverage-requirements.json'
    contract = json.loads(path.read_text())
    source = json.loads((ROOT / 'references/source-tables/metadata-functions.json').read_text())
    table = next(t for t in source['tables'] if t['table'] == '表5-2')
    require(contract['source_sha256'] == table['source_sha256'], 'MC-SOURCE', 'source-version', 'Source version changed; review checklist before evaluating coverage')
    rows = {'application-function-' + str(r['line']): r for r in table['rows']}
    rules = unique(contract['functions'], 'MC-SOURCE', 'functions')
    require(set(rows) == set(rules), 'MC-SOURCE', 'functions', 'Source universe and operational checklist differ; review source changes first')
    for fid, rule in rules.items():
        require(rule['source_definition'] == rows[fid]['values'][2] and rule['name'] == rows[fid]['values'][1], 'MC-SOURCE', fid, 'Portable source definition differs from checklist')
        require(rule['group'] == re.split(r'[（(]', rows[fid]['values'][0])[0], 'MC-SOURCE', fid, 'Source functional grouping differs from checklist')
        unique(rule['facets'], 'MC-SOURCE', fid + ':facets')
    return contract, rules, hashlib.sha256(path.read_bytes()).hexdigest()


def review_metadata_coverage(data):
    contract, functions, digest = universe()
    known = sources(data, 'MC-001', 'coverage')
    evidence_records = unique(data.get('evidence_records', []), 'MC-EVIDENCE', 'evidence-records')
    require(set(evidence_records) == known, 'MC-EVIDENCE', 'evidence-records', 'Every source ID requires an explicit evidence kind')
    allowed_kinds = {'observation', 'plan', 'tailoring', 'scope', 'asset-inventory', 'tool-inventory', 'project-rule', 'unverified', 'reference'}
    require(all(r.get('kind') in allowed_kinds for r in evidence_records.values()), 'MC-EVIDENCE', 'evidence-records', 'Unknown evidence kind')
    gaps = []

    def gap(ident, reason, action='补齐对应范围的证据或明确裁剪；未知不计作已实现'):
        gaps.append({'id': ident, 'reason': reason, 'action': action})

    def refs(values, ident, kinds=None):
        if not values:
            gap(ident + ':evidence', 'missing-evidence')
            return False
        evidence(values, known, 'MC-EVIDENCE', ident)
        if kinds and any(evidence_records[e]['kind'] not in kinds for e in values):
            gap(ident + ':evidence-kind', 'wrong-evidence-kind', '引用来源种类不支持此判断；参考图与产品介绍不能替代项目测试/计划/裁剪证据')
            return False
        return True

    def fields(record, names, ident):
        missing = [k for k in names if record.get(k) in [None, '', [], {}]]
        for field in missing:
            gap(ident + ':' + field, 'missing-' + field)
        return not missing

    def iso(value, ident):
        require(isinstance(value, str), 'MC-DATE', ident, 'ISO date required')
        try:
            return date.fromisoformat(value)
        except ValueError:
            raise ValueError('MC-DATE [' + ident + ']: Invalid ISO date')

    header_ok = fields(data, ['scope', 'architecture_state', 'as_of', 'owner'], 'coverage')
    header_ok = refs(data.get('scope_evidence'), 'coverage:scope') and header_ok
    as_of = iso(data['as_of'], 'coverage') if data.get('as_of') else None
    tools = unique(data.get('tools', []), 'MC-002', 'tools')
    assets = unique(data.get('assets', []), 'MC-002', 'assets')
    tool_valid, asset_valid = {}, {}
    categories = {c['id'] for c in contract['creation_categories']}
    for tid, tool in tools.items():
        tool_valid[tid] = fields(tool, ['name', 'version', 'owner'], tid)
        tool_valid[tid] = refs(tool.get('evidence'), tid) and tool_valid[tid]
    for aid, asset in assets.items():
        asset_valid[aid] = fields(asset, ['name', 'category', 'owner'], aid)
        asset_valid[aid] = refs(asset.get('evidence'), aid) and asset_valid[aid]
        require(asset.get('category') in categories, 'MC-ASSET', aid, 'Use source category or explicitly extend the checklist; do not silently coerce category')
    entries = unique(data.get('assessments', []), 'MC-003', 'assessments')
    byfunction = {}
    for entry in entries.values():
        fid = entry.get('function_id')
        require(fid in functions, 'MC-FUNCTION', entry['id'], 'Unknown source function')
        require(fid not in byfunction, 'MC-FUNCTION', entry['id'], 'Duplicate function assessment in same scope and state')
        byfunction[fid] = entry
    rows = []
    for fid, function in functions.items():
        entry = byfunction.get(fid)
        start = len(gaps)
        if entry is None:
            gap(fid + ':assessment', 'source-function-unassessed')
            rows.append({'id': fid + ':unassessed', 'function_id': fid, 'group': function['group'], 'name': function['name'], 'status': 'unknown', 'cells': [], 'gaps': gaps[start:]})
            continue
        ident = entry['id']
        claim = entry.get('declared_status', 'unknown')
        require(claim in STATUSES, 'MC-STATUS', ident, 'Unknown declared status')
        common = {'id': ident, 'function_id': fid, 'group': function['group'], 'name': function['name'], 'declared_status': claim, 'source_definition': function['source_definition'], 'required_asset_ids': entry.get('required_asset_ids', []), 'bindings': entry.get('bindings', [])}
        if claim == 'not-applicable':
            require(not entry.get('bindings'), 'MC-NA', ident, 'Not-applicable cannot also claim project implementation or plans')
            valid = fields(entry.get('exclusion', {}), ['reason', 'authority', 'scope'], ident + ':exclusion')
            valid = refs(entry.get('exclusion', {}).get('evidence'), ident + ':exclusion', {'tailoring'}) and valid and header_ok
            rows.append({**common, 'status': 'not-applicable' if valid else 'unknown', 'exclusion': entry.get('exclusion'), 'cells': [], 'gaps': gaps[start:]})
            continue
        scope_ok = fields(entry, ['coverage_scope', 'required_asset_ids', 'owner'], ident)
        scope_ok = refs(entry.get('requirement_evidence'), ident + ':requirement') and scope_ok and header_ok
        required_assets = entry.get('required_asset_ids', [])
        require(isinstance(required_assets, list) and len(set(required_assets)) == len(required_assets) and set(required_assets) <= set(assets), 'MC-ASSET', ident, 'Unknown or duplicate required asset IDs')
        facets = {f['id']: f for f in function['facets']}
        excluded = unique(entry.get('excluded_facets', []), 'MC-TAILOR', ident + ':facets')
        for facet, reason in excluded.items():
            require(facet in facets, 'MC-TAILOR', ident, 'Unknown excluded facet')
            valid = fields(reason, ['reason', 'authority'], ident + ':' + facet)
            valid = refs(reason.get('evidence'), ident + ':' + facet, {'tailoring'}) and valid
            scope_ok = scope_ok and valid
        required_facets = set(facets) - set(excluded)
        if not required_facets:
            gap(ident + ':required-facets', 'all-facets-excluded-use-explicit-function-exclusion')
            scope_ok = False
        if function.get('creation_category_check'):
            exclusions = unique(entry.get('excluded_categories', []), 'MC-TAILOR', ident + ':categories')
            require(set(exclusions) <= categories, 'MC-TAILOR', ident, 'Unknown excluded creation category')
            covered_categories = {assets[a]['category'] for a in required_assets}
            require(not (covered_categories & set(exclusions)), 'MC-TAILOR', ident, 'A category cannot be included and excluded in the same requirement')
            for category in sorted(categories - covered_categories - set(exclusions)):
                gap(ident + ':category:' + category, 'unscoped-source-creation-category')
                scope_ok = False
            for category, reason in exclusions.items():
                valid = fields(reason, ['reason', 'authority'], ident + ':' + category)
                valid = refs(reason.get('evidence'), ident + ':' + category, {'tailoring'}) and valid
                scope_ok = scope_ok and valid
        checks = {}
        bindings = unique(entry.get('bindings', []), 'MC-BINDING', ident)
        for bid, binding in bindings.items():
            tid = binding.get('tool_id')
            require(tid in tools, 'MC-TOOL', bid, 'Unknown tool identity')
            require(binding.get('tool_version') == tools[tid].get('version'), 'MC-VERSION', bid, 'Binding and tool versions differ; reassess after a tool upgrade')
            aids, fids = binding.get('asset_ids', []), binding.get('facet_ids', [])
            require(isinstance(aids, list) and bool(aids) and len(set(aids)) == len(aids) and set(aids) <= set(required_assets), 'MC-BINDING', bid, 'Binding assets must be inside explicit requirement scope')
            require(isinstance(fids, list) and bool(fids) and len(set(fids)) == len(fids) and set(fids) <= required_facets, 'MC-BINDING', bid, 'Binding facets must be inside explicit requirement scope')
            state = binding.get('status')
            require(state in STATUSES[:3], 'MC-STATUS', bid, 'Bindings can be implemented, planned or unknown; tailor at requirement level')
            valid = tool_valid[tid] and all(asset_valid[a] for a in aids)
            if state == 'implemented':
                check = binding.get('verification', {})
                valid = fields(check, ['method', 'observed_at', 'environment', 'result', 'acceptance_observations'], bid + ':verification') and valid
                valid = refs(check.get('evidence'), bid + ':verification', {'observation'}) and valid
                if check.get('observed_at'):
                    observed = iso(check['observed_at'], bid)
                    require(as_of is None or observed <= as_of, 'MC-DATE', bid, 'Future observation cannot support current implemented state')
                require(check.get('result') in ['pass', 'fail', 'inconclusive', None], 'MC-RESULT', bid, 'Unknown verification result')
                valid = valid and check.get('result') == 'pass'
                if check.get('result') in ['fail', 'inconclusive']:
                    gap(bid + ':verification-result', 'verification-not-passed')
                observations = unique(check.get('acceptance_observations', []), 'MC-OBSERVATION', bid)
                expected = {(a, f) for a in aids for f in fids}
                seen = set()
                for oid, observation in observations.items():
                    pair = (observation.get('asset_id'), observation.get('facet_id'))
                    require(pair in expected and pair not in seen, 'MC-OBSERVATION', oid, 'Unknown or duplicate asset/facet observation')
                    seen.add(pair)
                    confirmed = fields(observation, ['observed_behavior'], oid)
                    confirmed = refs(observation.get('evidence'), oid, {'observation'}) and confirmed
                    valid = valid and confirmed
                if seen != expected:
                    gap(bid + ':observation-coverage', 'missing-per-asset-facet-observation')
                    valid = False
            elif state == 'planned':
                plan = binding.get('plan', {})
                valid = fields(plan, ['owner', 'target_date', 'milestone', 'scope'], bid + ':plan') and valid
                valid = refs(plan.get('evidence'), bid + ':plan', {'plan'}) and valid
                planned_scope = plan.get('scope', [])
                require(isinstance(planned_scope, list) and all(isinstance(p, dict) for p in planned_scope), 'MC-PLAN', bid, 'Plan scope must list asset/facet pairs')
                planned_pairs = [(p.get('asset_id'), p.get('facet_id')) for p in planned_scope]
                if len(set(planned_pairs)) != len(planned_pairs) or set(planned_pairs) != {(a, f) for a in aids for f in fids}:
                    gap(bid + ':plan-scope', 'plan-does-not-cover-binding-scope')
                    valid = False
                if plan.get('target_date'):
                    due = iso(plan['target_date'], bid)
                    if as_of and due < as_of:
                        gap(bid + ':plan-overdue', 'planned-milestone-overdue', '复核延期与当前计划；过期计划不成为已实现证据')
            else:
                gap(bid + ':unknown', 'binding-not-verified')
                valid = False
            effective = state if valid and scope_ok else 'unknown'
            for aid in aids:
                for facet in fids:
                    checks.setdefault((aid, facet), []).append({'binding_id': bid, 'tool_id': tid, 'tool_version': binding['tool_version'], 'status': effective, 'claimed_status': state})
        cells = []
        for aid in required_assets:
            for facet in sorted(required_facets):
                candidates = checks.get((aid, facet), [])
                statuses = {c['status'] for c in candidates}
                # Any explicitly failed observation makes disagreement reviewable,
                # even if a second tool reports a passing implementation.
                contradicted = any(bindings[c['binding_id']].get('verification', {}).get('result') == 'fail' for c in candidates)
                status = 'unknown' if contradicted else 'implemented' if 'implemented' in statuses else 'planned' if 'planned' in statuses else 'unknown'
                if status != 'implemented':
                    gap(ident + ':' + aid + ':' + facet, 'conflicting-failed-observation' if contradicted else 'planned-not-yet-implemented' if status == 'planned' else 'no-supported-implementation-or-plan')
                cells.append({'asset_id': aid, 'facet_id': facet, 'facet_name': facets[facet]['name'], 'status': status, 'binding_refs': candidates})
        states = {c['status'] for c in cells}
        status = 'unknown' if not cells or not scope_ok or 'unknown' in states else 'planned' if 'planned' in states else 'implemented'
        if claim != status:
            gap(ident + ':declared-status', 'declared-status-differs-from-evidence', '保留原声明并将结论改为证据所支持的状态；不覆盖声明历史')
        rows.append({**common, 'required_facets': sorted(required_facets), 'excluded_facets': list(excluded.values()), 'status': status, 'cells': cells, 'gaps': gaps[start:]})
    counts = {status: sum(r['status'] == status for r in rows) for status in STATUSES}
    groups = {g: {status: sum(r['group'] == g and r['status'] == status for r in rows) for status in STATUSES} for g in dict.fromkeys(f['group'] for f in functions.values())}
    return {'scope': data.get('scope'), 'architecture_state': data.get('architecture_state'), 'as_of': data.get('as_of'), 'source_universe': {'source': 'G234 表5-2', 'checklist_sha256': digest, 'function_ids': list(functions)}, 'rows': rows, 'status_counts': counts, 'group_status_counts': groups, 'gaps': gaps, 'notice': '四态是明确的项目审查规则；实现只在所列资产、功能方面、工具版本、环境和日期成立。功能地图不是实现证据；缺证据为未知。数量仅用于清点，不输出TOGAF评分、加权总分、合格线或默认覆盖率。'}
