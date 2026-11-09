"""JSON model I/O that rejects nonstandard constants and float overflow."""
import json
from pathlib import Path
from numeric_contracts import finite_number, require_finite


def _constant(value):
    raise ValueError('invalid-json-number:' + value)


def _float(value):
    return finite_number(float(value), 'JSON number ' + value)


def loads(value):
    return json.loads(value, parse_constant=_constant, parse_float=_float)


def load(path):
    return loads(Path(path).read_text(encoding='utf-8'))


def dumps(value, **kwargs):
    require_finite(value)
    kwargs['allow_nan'] = False
    return json.dumps(value, **kwargs)
