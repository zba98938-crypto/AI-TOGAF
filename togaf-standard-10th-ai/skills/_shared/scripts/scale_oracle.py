#!/usr/bin/env python3
"""Read persisted measurements; independently reconcile a declared toy process.

No operating claim: units are t, kWh and CNY. Measured losses, tail assay and
byproduct output are inputs, never solved as a residual to force a balance.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path


def audit(directory):
    directory = Path(directory)
    paths = [directory / 'activities.json', directory / 'outputs.json']
    activities, outputs = [json.loads(p.read_text()) for p in paths]
    violations = []
    if not activities or not outputs:
        violations.append({'category': 'integrity', 'reason': 'empty-measurements'})

    def check(category, identity, actual, expected):
        if abs(Decimal(str(actual)) - Decimal(str(expected))) > Decimal('0.000001'):
            violations.append({'category': category, 'id': identity,
                               'actual': str(actual), 'expected': str(expected)})

    def d(row, key):
        return Decimal(str(row[key]))

    indexed = {o['id']: o for o in outputs}
    if len(indexed) != len(outputs) or len({a['id'] for a in activities}) != len(activities):
        violations.append({'category': 'integrity', 'reason': 'duplicate-id'})
    if set(indexed) != {a['id'] for a in activities}:
        violations.append({'category': 'integrity', 'reason': 'activity/output-id-set'})
    for a in activities:
        o = indexed.get(a['id'])
        if o is None:
            continue
        if o['site'] != a['site']:
            violations.append({'category': 'integrity', 'id': a['id'], 'reason': 'site'})
        identity = a['id']
        check('material', identity, d(o, 'product_t') + d(o, 'tail_t'), d(a, 'feed_t'))
        check('material', identity, d(o, 'product_p2o5_t'), d(o, 'product_t') * d(a, 'product_assay'))
        check('material', identity, d(o, 'tail_p2o5_t'), d(o, 'tail_t') * d(a, 'tail_assay'))
        check('material', identity, d(o, 'product_p2o5_t') + d(o, 'tail_p2o5_t'),
              d(a, 'feed_t') * d(a, 'feed_assay'))
        check('energy', identity, d(o, 'electric_kwh'), d(a, 'power_kw') * d(a, 'hours'))
        check('energy', identity, d(o, 'useful_kwh') + d(a, 'measured_loss_kwh'),
              d(o, 'electric_kwh') + d(a, 'heat_input_kwh'))
        check('amount', identity, d(o, 'invoice_cny'),
              d(a, 'shipped_t') * d(a, 'price_cny_per_t') * (1 + d(a, 'tax_rate')))
        check('inventory', identity, d(o, 'closing_product_t'),
              d(a, 'opening_product_t') + d(o, 'product_t') - d(a, 'shipped_t'))
        check('byproduct', identity, d(o, 'gypsum_produced_t'), d(a, 'gypsum_weighed_t'))
        check('byproduct', identity, d(o, 'closing_gypsum_t'),
              d(a, 'opening_gypsum_t') + d(o, 'gypsum_produced_t') - d(a, 'gypsum_dispatched_t'))
    return {'passed': not violations, 'activities': len(activities), 'outputs': len(outputs),
            'violations': violations,
            'inputs_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'notice': 'Independent arithmetic of persisted synthetic measurements, not plant engineering validation.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    result = audit(parser.parse_args().directory)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
