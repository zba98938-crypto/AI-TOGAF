#!/usr/bin/env python3
"""Audit explicit requirement traces in any shared model; never infer acceptance."""
import argparse
import hashlib
import json
from pathlib import Path

REQUIREMENT_TYPES = {'requirement', 'security_requirement', 'analytics_requirement'}
ORIGIN_TYPES = {'goal', 'objective', 'driver', 'stakeholder', 'business_attribute',
                'control_objective', 'legal_requirement', 'business_scenario', 'scenario_goal'}
NON_DESIGN_TYPES = REQUIREMENT_TYPES | ORIGIN_TYPES | {
    'work_package', 'acceptance_criterion', 'change_request', 'evidence', 'gap',
    'decision_record', 'measure', 'outcome', 'benefit'}
SYNTHETIC_KINDS = {'example', 'assumption', 'figure-interpretation'}


def audit(model, requirement_ids=None, scope_id=None, state_id=None, mode='planning'):
    """Return structural errors and actionable trace gaps without mutating input.

    Planning checks origin, ownership, acceptance plan and explicit architecture
    allocation. Delivery additionally checks work allocation and observed results.
    These are project checks, not a mandated TOGAF artifact set or approval gate.
    """
    if mode not in {'planning', 'delivery'}:
        raise ValueError('mode must be planning or delivery')
    errors, gaps = [], []
    def issue(collection, code, identity, message):
        collection.append({'code': code, 'id': identity, 'message': message})
    def index(group):
        result = {}
        for item in model.get(group, []):
            if item['id'] in result:
                issue(errors, 'trace-duplicate-id', item['id'], 'Duplicate identity in ' + group)
            result[item['id']] = item
        return result
    entities, sources = index('entities'), index('sources')
    relationships, views, deliverables = index('relationships'), index('views'), index('deliverables')
    states = {x['id']: x for x in model.get('states', [])}
    def context_value(obj, key):
        return obj.get(key, states.get(obj.get('state_id'), {}).get(key))
    if scope_id is not None and scope_id not in {x['id'] for x in model.get('scopes', [])}:
        issue(errors, 'trace-unknown-scope', scope_id, 'Unknown scope selector')
    if state_id is not None and state_id not in {x['id'] for x in model.get('states', [])}:
        issue(errors, 'trace-unknown-state', state_id, 'Unknown state selector')
    def refs(value, identity, field):
        if not isinstance(value, list) or any(not isinstance(x, str) for x in value):
            issue(errors, 'trace-invalid-refs', identity, field + ' must be an array of IDs')
            return []
        if len(value) != len(set(value)):
            issue(errors, 'trace-duplicate-ref', identity, field + ' contains duplicate IDs')
        return list(dict.fromkeys(value))
    def evidence(ids, identity, field='evidence'):
        ids = refs(ids, identity, field)
        for sid in ids:
            if sid not in sources:
                issue(errors, 'trace-unknown-evidence', identity, 'Unknown source ' + sid)
        return [sid for sid in ids if sid in sources]
    selected = [e for e in entities.values() if e.get('type') in REQUIREMENT_TYPES
                and (scope_id is None or context_value(e, 'scope_id') == scope_id)
                and (state_id is None or e.get('state_id') == state_id)]
    if requirement_ids is not None:
        requested = refs(requirement_ids, 'selection', 'requirement_ids')
        for rid in requested:
            if rid not in entities or entities[rid].get('type') not in REQUIREMENT_TYPES:
                issue(errors, 'trace-invalid-requirement', rid, 'Not a registered requirement object')
            elif entities[rid] not in selected:
                issue(errors, 'trace-selection-conflict', rid, 'Requirement outside selected scope/state')
        selected = [e for e in selected if e['id'] in requested]
    if not selected:
        issue(gaps, 'trace-empty-selection', 'selection', 'No requirements in selected scope; not a coverage pass')
    edges = []
    for rel in relationships.values():
        if rel.get('source') not in entities or rel.get('target') not in entities:
            issue(errors, 'trace-dangling-endpoint', rel['id'], 'Relationship endpoint is missing')
        else:
            edges.append(rel)
    criteria = [e for e in entities.values() if e.get('type') == 'acceptance_criterion']
    criterion_bindings = {}
    for c in criteria:
        ids = refs(c.get('attributes', {}).get('requirement_ids', []), c['id'], 'requirement_ids')
        for rid in ids:
            if rid not in entities or entities[rid].get('type') not in REQUIREMENT_TYPES:
                issue(errors, 'trace-invalid-criterion-binding', c['id'], 'Not a requirement: ' + rid)
        criterion_bindings[c['id']] = ids
    rows = []
    for req in selected:
        rid = req['id']; attrs = req.get('attributes', {})
        row = {'requirement_id': rid, 'name': req.get('name', rid),
               'scope_id': context_value(req, 'scope_id'), 'state_id': req.get('state_id'),
               'origin_ids': [], 'architecture_ids': [], 'work_package_ids': [],
               'criterion_ids': [], 'relationship_ids': [], 'cross_context_ids': [],
               'view_ids': [], 'deliverable_ids': [], 'verification_results': []}
        for field in ('statement', 'owner', 'priority', 'acceptance'):
            if not attrs.get(field) or (isinstance(attrs[field], str) and not attrs[field].strip()):
                issue(gaps, 'trace-missing-' + field, rid, 'Supply requirement ' + field)
        if not evidence(req.get('evidence', []), rid):
            issue(gaps, 'trace-missing-source', rid, 'Record source of the requirement')
        def compatible(obj):
            # Named states/scopes must not silently borrow evidence from a different
            # version. State-less objects remain shared, not inferred target copies.
            for key in ('scope_id', 'state_id'):
                if context_value(req, key) and context_value(obj, key) and context_value(req, key) != context_value(obj, key):
                    row['cross_context_ids'].append(obj['id'])
                    return False
            return True
        def usable(rel):
            return compatible(rel) and bool(evidence(rel.get('evidence', []), rel['id']))
        for rel in edges:
            typ, src, dst = rel['type'], rel['source'], rel['target']
            if rid not in (src, dst):
                continue
            other = entities[dst if src == rid else src]
            if not compatible(other) or not usable(rel):
                continue
            category = None
            if other['type'] in ORIGIN_TYPES and (
                    typ == 'traces_to' or (typ == 'derived_from' and src == rid)):
                category = 'origin_ids'
            elif other['type'] not in NON_DESIGN_TYPES and (
                    (typ == 'specifies' and src == rid) or
                    (typ in {'satisfies', 'supports_metadata_requirement'} and dst == rid) or
                    (typ == 'requires_control' and src == rid)):
                category = 'architecture_ids'
            elif other['type'] == 'work_package' and (
                    typ == 'traces_to' or (typ == 'satisfies' and dst == rid)):
                category = 'work_package_ids'
            if category:
                row[category].append(other['id']); row['relationship_ids'].append(rel['id'])
        # Only a documented work-package link to an allocated architecture object
        # counts; graph reachability through arbitrary edges is not satisfaction.
        for rel in edges:
            src, dst, typ = rel['source'], rel['target'], rel['type']
            wp = None
            if src in row['architecture_ids'] and entities[dst]['type'] == 'work_package' and typ in {'migrated_by', 'traces_to'}:
                wp = entities[dst]
            elif dst in row['architecture_ids'] and entities[src]['type'] == 'work_package' and typ in {'changes_object', 'traces_to'}:
                wp = entities[src]
            if wp and compatible(wp) and usable(rel):
                row['work_package_ids'].append(wp['id']); row['relationship_ids'].append(rel['id'])
        for criterion in criteria:
            if rid not in criterion_bindings[criterion['id']] or not compatible(criterion):
                continue
            cid = criterion['id']; ca = criterion.get('attributes', {})
            row['criterion_ids'].append(cid)
            if not ca.get('criterion') or not ca.get('verification'):
                issue(gaps, 'trace-incomplete-verification-plan', cid, 'Supply criterion and verification procedure')
            status = ca.get('execution_status', 'unknown')
            result = {'criterion_id': cid, 'execution_status': status, 'evidence_status': 'not-observed'}
            if status not in {'unknown', 'not-executed', 'planned', 'passed', 'failed', 'inconclusive'}:
                issue(errors, 'trace-invalid-execution-status', cid, 'Unknown execution status')
            if status in {'passed', 'failed', 'inconclusive'}:
                result_refs = evidence(ca.get('result_evidence', []), cid, 'result_evidence')
                observed = ca.get('observed_result')
                if observed is None or observed == '' or not result_refs:
                    issue(gaps, 'trace-result-evidence-missing', cid, 'Claimed execution needs observed_result and result_evidence')
                elif model.get('project', {}).get('is_example') or any(sources[s]['kind'] in SYNTHETIC_KINDS for s in result_refs):
                    if not model.get('project', {}).get('is_example'):
                        issue(errors, 'trace-synthetic-execution', cid, 'Synthetic evidence cannot prove real project execution')
                    result['evidence_status'] = 'simulated-result'
                else:
                    result['evidence_status'] = 'recorded-result-awaiting-review'
                if status != 'passed':
                    issue(gaps, 'trace-verification-not-passed', cid, 'Observed verification is failed or inconclusive')
            elif ca.get('observed_result') is not None:
                issue(errors, 'trace-unexecuted-observation', cid, 'Unexecuted plan cannot contain an observed result')
            row['verification_results'].append(result)
        for field, code, message in (
                ('origin_ids', 'trace-missing-origin', 'Link requirement to its goal, stakeholder or originating constraint'),
                ('architecture_ids', 'trace-missing-design', 'Allocate requirement to explicit architecture objects'),
                ('criterion_ids', 'trace-missing-criterion', 'Bind an acceptance_criterion with requirement_ids')):
            if not row[field]: issue(gaps, code, rid, message)
        if mode == 'delivery':
            if not row['work_package_ids']:
                issue(gaps, 'trace-missing-work-package', rid, 'Identify work implementing the allocated architecture')
            if not row['verification_results'] or any(
                    r['execution_status'] != 'passed' or r['evidence_status'] != 'recorded-result-awaiting-review'
                    for r in row['verification_results']):
                issue(gaps, 'trace-delivery-unverified', rid, 'Actual result evidence is incomplete; plans and simulations do not establish delivery')
        traced = {rid, *row['architecture_ids'], *row['work_package_ids'], *row['criterion_ids']}
        row['view_ids'] = [v['id'] for v in views.values()
                           if traced.intersection(v.get('entity_ids', [])) and compatible(v)]
        row['deliverable_ids'] = [d['id'] for d in deliverables.values()
            if traced.intersection(d.get('entity_ids', [])) or set(row['view_ids']).intersection(d.get('view_ids', []))]
        for key in ('origin_ids', 'architecture_ids', 'work_package_ids', 'criterion_ids',
                    'relationship_ids', 'cross_context_ids', 'view_ids', 'deliverable_ids'):
            row[key] = sorted(set(row[key]))
        rows.append(row)
    # IDs and codes are stable for automation; repeated evidence checks are coalesced.
    errors = list({(e['code'], e['id'], e['message']): e for e in errors}.values())
    gaps = list({(e['code'], e['id'], e['message']): e for e in gaps}.values())
    return {'schema_version': '1.0', 'mode': mode, 'rows': rows, 'errors': errors, 'gaps': gaps,
            'summary': {'requirements': len(rows), 'errors': len(errors), 'gaps': len(gaps),
                        'trace_complete': bool(rows) and not errors and not gaps,
                        'business_acceptance': 'not-assessed'},
            'notice': 'Explicit trace and evidence inventory only. A relationship is not proof of satisfaction; views are references, not accepted deliverables.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('--requirement', action='append')
    parser.add_argument('--scope'); parser.add_argument('--state')
    parser.add_argument('--mode', choices=['planning', 'delivery'], default='planning')
    parser.add_argument('--report', type=Path)
    parser.add_argument('--strict', action='store_true', help='Exit nonzero for trace gaps as well as errors')
    args = parser.parse_args()
    if args.report and args.model.resolve() == args.report.resolve():
        parser.error('report must not overwrite the input model')
    from strict_json import load as load_json
    try:
        model = load_json(args.model)
    except (OSError, ValueError) as exc:
        parser.exit(1, str(exc) + '\n')
    from validate import validate
    model_errors = [x for x in validate(model) if x['level'] == 'error']
    if model_errors:
        report = {'errors': model_errors, 'gaps': [], 'summary': {'trace_complete': False, 'business_acceptance': 'not-assessed'}}
    else:
        report = audit(model, args.requirement, args.scope, args.state, args.mode)
    report['model_sha256'] = hashlib.sha256(args.model.read_bytes()).hexdigest()
    payload = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True); args.report.write_text(payload)
    print(payload, end='')
    return int(bool(report['errors']) or (args.strict and bool(report['gaps'])))


if __name__ == '__main__':
    raise SystemExit(main())
