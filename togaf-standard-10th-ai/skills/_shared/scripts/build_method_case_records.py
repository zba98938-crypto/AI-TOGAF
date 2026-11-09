"""Observe case structure in a new run; retain historical reviews without renewing them.

No professional cross-review, execution or calculator pass is generated here.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / 'examples/method-cases'
CROSS = ROOT / 'reviews/method-cross-review'
EXEC = ROOT / 'reviews/method-execution'
SECTIONS = [
    ('raw', '## 决策与原始业务资料'),
    ('steps', '## 转换与推理'),
    ('result', '## 输出与追溯'),
    ('modification', '## 修改演练'),
    ('counterexample', '## 反例与输入不足'),
    ('review', '## 评审记录'),
]
TAIL = '本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def section_lines(text, heading):
    start = text.index(heading)
    rest = text[start + len(heading):]
    nxt = len(rest)
    for _, other in SECTIONS:
        if other != heading and other in rest:
            nxt = min(nxt, rest.index(other))
    return rest[:nxt]


def source_ids(text):
    """Read the evidence table's first column only.

    Falling back to "any backticked token" pulled in method ids, assertion codes and
    section names, which then looked like cited evidence. The evidence table is the
    only place a source id is defined, so only that row shape counts.
    """
    rows = re.findall(r'^\|\s*`?([A-Za-z][\w.\-]*)`?\s*\|', text, re.M)
    seen = []
    for value in rows:
        value = value.strip()
        if value in ('证据 ID', '证据ID', '结果 ID', '结果ID', 'ID'):
            continue
        if value not in seen:
            seen.append(value)
    return seen


def result_ids(text):
    return [i for i in re.findall(r'`([A-Z]{2,6}-(?:R|GAP)?-?\d+)`', text)]


def assertion_codes(text):
    return sorted(set(re.findall(r'预期 `([a-z][a-z0-9-]+)`', text)))


def gap_ids(text):
    return sorted(set(re.findall(r'`([A-Z]{2,6}-GAP-\d+)`', text)))


def boundary_claims(text):
    hits = []
    for phrase in ['没有适用的统一计算器', '不外推', '不等于批准', '不是批准', '未观察', '未获批准', '不声明']:
        if phrase in text:
            hits.append(phrase)
    return hits


def build_observations(root=ROOT):
    """Record mechanically observable structure, never invent a review or a run.

    Existing execution and review files remain immutable historical evidence. The
    index retains them, including stale internal hashes, rather than relabeling them.
    """
    from datetime import datetime, timezone
    import uuid
    from evidence_integrity import verify_reference
    index = read_json(root / 'reviews/method-case-index.json')
    caps = read_json(root / 'capabilities.json')
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:10]
    directory = root / 'reviews/method-observations' / run_id
    directory.mkdir(parents=True, exist_ok=False)
    headings = [SECTIONS[0][1], '## 来源规则与项目规则'] + [h for _, h in SECTIONS[1:]]
    for item in index['methods']:
        mid = item['method_id']
        case = root / 'examples/method-cases' / (mid + '.md')
        text = case.read_text()
        present = [h for h in headings if h in text]
        record = {'schema_version': 'method-structure-observation/2', 'run_id': run_id,
                  'method_id': mid, 'case_path': str(case.relative_to(root)),
                  'case_sha256': sha(case), 'observation_kind': 'mechanical-structure-only',
                  'sections_present': present,
                  'order_preserved': [text.index(h) for h in present] == sorted(text.index(h) for h in present),
                  'assertion_codes_declared': assertion_codes(text),
                  'author_boundary_present': TAIL in text,
                  'execution_status': 'not-executed-by-this-tool',
                  'review_status': 'professional-review-pending',
                  'pending_checks': ['reasoning-sufficiency', 'source-fidelity', 'business-applicability'],
                  'limit': 'Structure observed, not a semantic review, calculator run, or business acceptance.'}
        output = directory / (mid + '.json')
        output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        item['canonical_case'] = str(case.relative_to(root))
        roles = item.setdefault('evidence', {})
        for role, heading in SECTIONS[:5]:
            rel = str(case.relative_to(root))
            roles[role] = [r for r in roles.get(role, []) if r.get('path') != rel]
            roles[role].insert(0, {'path': rel, 'sha256': sha(case),
                                  'selector': heading, 'basis': 'current case text, not an execution or review'})
        item['structure_observation'] = {'path': str(output.relative_to(root)), 'sha256': sha(output)}
        item['evidence_integrity'] = {
            role: [{'path': ref.get('path'), 'errors': verify_reference(ref, root, {'method_id': mid})}
                   for ref in refs] for role, refs in roles.items()}
    index['registry_sha256'] = sha(root / 'capabilities.json')
    index['notice'] = ('Current case text and mechanical observations; previous execution/review records are '
                       'retained with their original hashes. Presence never implies current semantic validation.')
    index['observation_run_id'] = run_id
    index.setdefault('summary', {})['mechanically_observed_cases'] = len(index['methods'])
    index['summary']['current_execution_claims_by_this_tool'] = 0
    index['summary']['semantic_review_claims_by_this_tool'] = 0
    index['summary']['registered_methods'] = len(caps['analysis_methods'])
    (root / 'reviews/method-case-index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')
    return {'run_id': run_id, 'observed': len(index['methods']), 'execution_granted': False,
            'semantic_review_granted': False}


def main():
    print(json.dumps(build_observations(), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
