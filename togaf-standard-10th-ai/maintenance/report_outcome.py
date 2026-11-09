"""Normalize the validation report formats used by maintenance and test runners.

Only report-level outcome fields are interpreted. Domain objects and expected
negative-case payloads are not recursively treated as failed validations.
Explicit failure always overrides a conflicting success signal. Zero failures
alone does not establish that a validation ran or passed.
"""
import json

PASSED = frozenset({'pass', 'passed', 'passed-with-explicit-limits'})
FAILED = frozenset({'fail', 'failed', 'error', 'errored'})
INCOMPLETE = frozenset({'blocked', 'pending', 'incomplete', 'partial', 'skipped',
                        'uncovered', 'not-executed', 'not-run', 'not-dispatched',
                        'needs-review', 'needs_review'})
BLOCKING = frozenset({'failed', 'incomplete', 'invalid'})
EXTERNAL_ACCEPTANCE_ITEMS = frozenset({'INDEPENDENT-SEMANTIC', 'REAL-BUSINESS'})
# Actual report-level formats: verify_methods.py uses failed; validate.py uses
# errors; maintenance/pipeline validators use error_count; test suite runners
# use failures. Several of those producers also publish failure/error lists.
# These names are interpreted only at the report root, never in domain results
# or expected negative-case records. Empty lists/zero counts are not success.
FAILURE_FIELDS = ('failed', 'failures', 'errors', 'error_count')
FAILURE_LIST_FIELDS = frozenset({'failed', 'failures', 'errors'})


def report_outcome(report):
    signals = []
    if not isinstance(report, dict):
        return {'state': 'unknown', 'passed': None, 'signals': []}

    def add(field, state, value):
        signals.append({'field': field, 'state': state, 'value': value})

    # Package verification uses all_applicable_pass; unittest summaries may
    # use successful. Approval/acceptance fields are deliberately separate.
    for field in ('passed', 'all_applicable_pass', 'successful'):
        if field in report:
            value = report[field]
            add(field, ('passed' if value else 'failed') if isinstance(value, bool) else 'invalid', value)
    for field in ('result', 'status'):
        if field not in report:
            continue
        value = report[field]
        if isinstance(value, str):
            token = value.strip().lower()
            state = 'passed' if token in PASSED else 'failed' if token in FAILED else 'incomplete' if token in INCOMPLETE else 'invalid'
            add(field, state, value)
        # Structured result payloads are not report status declarations.
        elif not isinstance(value, (dict, list)):
            add(field, 'invalid', value)
    for field in FAILURE_FIELDS:
        if field not in report:
            continue
        value = report[field]
        if field in FAILURE_LIST_FIELDS and isinstance(value, list):
            if value:
                add(field, 'failed', value)
        elif type(value) is not int or value < 0:
            add(field, 'invalid', value)
        elif value:
            add(field, 'failed', value)
    counts = report.get('counts', {})
    if isinstance(counts, dict):
        for field in ('failed', 'failures', 'errors', 'skipped', 'blocked', 'uncovered'):
            if field not in counts:
                continue
            value = counts[field]
            if type(value) is not int or value < 0:
                add('counts.' + field, 'invalid', value)
            elif value:
                add('counts.' + field, 'failed' if field in {'failed', 'failures', 'errors'} else 'incomplete', value)
    for state in ('failed', 'invalid', 'incomplete', 'passed'):
        if any(signal['state'] == state for signal in signals):
            return {'state': state, 'passed': state == 'passed', 'signals': signals}
    return {'state': 'unknown', 'passed': None, 'signals': signals}


def file_outcome(path):
    if not path.is_file():
        return {'state': 'invalid', 'passed': False, 'signals': [{'field': 'file', 'state': 'invalid', 'value': 'missing'}]}
    if path.suffix != '.json':
        return report_outcome(None)
    try:
        return report_outcome(json.loads(path.read_text()))
    except (OSError, ValueError) as exc:
        return {'state': 'invalid', 'passed': False, 'signals': [{'field': 'file', 'state': 'invalid', 'value': str(exc)}]}


def ledger_state(declared_state, outcomes):
    """Conditional rows require affirmative validation; pending stays pending.

    Static done rows may cite source documents with no validation outcome, but
    an explicit failed/incomplete/invalid report must make them pending.
    """
    if declared_state not in {'done', 'conditional'}:
        return declared_state
    if not outcomes or any(outcome['state'] in BLOCKING for outcome in outcomes):
        return 'pending'
    if declared_state == 'conditional' and not all(outcome['state'] == 'passed' for outcome in outcomes):
        return 'pending'
    return 'done'


def engineering_complete(items, evidence_passed=True):
    """Derive the scoped aggregate from rows, never from a stored summary flag."""
    relevant = [item for item in items if item['id'] not in EXTERNAL_ACCEPTANCE_ITEMS]
    return bool(relevant) and evidence_passed and all(item.get('state') == 'done' for item in relevant)
