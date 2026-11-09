"""Small, non-coercing numeric and local identity contracts for calculators."""
from decimal import Decimal
import math


def finite_number(value, field, minimum=None, maximum=None):
    """Accept JSON real numbers, never booleans or numeric strings."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError('invalid-number:' + field + ': finite real number required')
    # Integers are unbounded in Python; do not convert them just to check finiteness.
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('invalid-number:' + field + ': finite real number required')
    if minimum is not None and value < minimum:
        raise ValueError('invalid-number:' + field + ': below minimum')
    if maximum is not None and value > maximum:
        raise ValueError('invalid-number:' + field + ': above maximum')
    return value


def require_finite(value, path='value'):
    """Reject nonfinite numbers at input/output boundaries without rejecting flags."""
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('non-finite-number:' + path)
    if isinstance(value, Decimal) and not value.is_finite():
        raise ValueError('non-finite-number:' + path)
    if isinstance(value, dict):
        for key, child in value.items():
            require_finite(child, path + '.' + str(key))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            require_finite(child, path + '[' + str(index) + ']')
    return value


def stable_id(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('invalid-id:' + field + ': nonempty string required')
    return value


def unique_records(records, field, key='id', nonempty=False):
    """Identity is unique within this collection, not across unrelated domains."""
    if not isinstance(records, list) or any(not isinstance(r, dict) for r in records):
        raise ValueError('invalid-records:' + field + ': list of objects required')
    if nonempty and not records:
        raise ValueError('empty-records:' + field)
    identities = [stable_id(row.get(key), field + '.' + key) for row in records]
    if len(identities) != len(set(identities)):
        raise ValueError('duplicate-id:' + field)
    return records
