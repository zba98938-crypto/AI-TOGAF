"""Pure full-material gate: recompute retained native evidence, never counters."""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[2]


def collection_module():
    tests = str(REPO / 'tests')
    if tests not in sys.path:
        sys.path.insert(0, tests)
    from enterprise import material_review
    return material_review


def material_checks(round_data, root=REPO):
    """Return a read-only assessment; explicit unsupported inputs stay uncovered."""
    reference = round_data.get('material_review')
    if not reference:
        return {'complete': False, 'status': 'pending', 'required_units': None, 'reviewed_units': 0,
                'reason': 'No current-version retained independent material collection.'}
    module = collection_module()
    try:
        packet = module.load(module.verify_ref(reference, root))
        if packet.get('source_commit') != round_data.get('source_commit'):
            raise ValueError('material collection belongs to another source revision')
        expected = round_data.get('material_input_manifest')
        if expected is not None and packet.get('input_manifest') != expected:
            raise ValueError('material collection belongs to another explicit input round')
        if packet.get('fixture_execution') is not True:
            authority = round_data.get('material_review_authority')
            if not authority or packet.get('authority') != authority or expected is None:
                raise ValueError('material native review lacks explicit frozen round/input/runtime authority')
        data = module.collect_existing(reference, root, expected_round=round_data)
        return {'complete': data['complete'], 'status': 'pass' if data['complete'] else 'incomplete',
                'required_units': data['required_units'], 'reviewed_units': data['reviewed_units'],
                'pending_units': data['pending_units'], 'executed_shards': data['executed_shards'],
                'total_shards': data['total_shards'], 'full_source_scope': data['full_source_scope'],
                'fixture_execution': data['fixture_execution'], 'evidence': reference,
                'human_professional_acceptance': 'pending_signature', 'real_organization_approval': 'pending_signature'}
    except (OSError, ValueError, KeyError, TypeError, IndexError, AttributeError, ImportError) as exc:
        return {'complete': False, 'status': 'invalid', 'required_units': None, 'reviewed_units': 0,
                'reason': str(exc), 'evidence': reference}
