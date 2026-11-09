#!/usr/bin/env python3
"""Local deterministic verification/collection; native dispatch is an injected API."""
import argparse
import json
from pathlib import Path
from enterprise.material_review import ReviewInputs, collect_existing, ref, safe, write_new


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('verify-inputs', 'collect'))
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(); root = args.root.resolve()
    input_path = args.input if args.input.is_absolute() else root / args.input
    output_path = args.out if args.out.is_absolute() else root / args.out
    out = safe(output_path.absolute().relative_to(root).as_posix(), root)
    if args.command == 'verify-inputs':
        inputs = ReviewInputs(ref(input_path, root), root)
        result = {'schema_version': 'material-input-verification/1', 'passed': True,
                  'full_source_scope': inputs.full_source_scope, 'source_units': len(inputs.units),
                  'shards': len(inputs.shards), 'input_files': len(inputs.inputs), 'model_requests': 0,
                  'independent_review_complete': False}
    else:
        result = collect_existing(ref(input_path, root), root)
    write_new(out, result)
    print(json.dumps({k: v for k, v in result.items() if k not in ('unit_results', 'attempt_results')}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
