"""Conservative internal acceptance-record verifier (not an official TOGAF rubric).

Public API: evaluate_acceptance(entry, gate, root, current=None).
No writes or input mutation; the root adapter reads evidence files. Thus this is a
side-effect-free evaluator, not a mathematically pure function over mutable disk.
current is a nonempty mapping of current runtime/resource names to SHA256 values.

Gate v1: schema_version, category, id, reviewer {id, role}, scope
{capabilities:[{category,id}], purpose}, runtime_fingerprints, dimensions.
All seven dimensions require status, rationale and evidence [{path, sha256,
record_id}]. Evidence is UTF-8 JSON {schema_version:'acceptance-review-records-v1',
records:[...]}. Selected records require id, dimension, status, reviewer, scope,
observations (nonempty strings) and assets [{path,sha256}]. Assets are actual
reviewed nonempty files; records cannot cite themselves as assets.
Definition also requires source_comparisons [{source_path, locator, conclusion}]
whose source_path is a hashed asset. Visual requires original_assets/output_assets
(path lists drawn from assets), plus opened_assets [{path,sha256,reviewer_id,
opened:true,observations:[...]}] covering every declared original and output image.
Only visual may be not-applicable, and only when caller explicitly supplies
visual_applicable=False (or output_kind='table' without a conflicting True).
The caller derives this contract from registry data, never from gate claims.

This verifies identity, scope, integrity and explicit review attestations, NOT
reviewer honesty, cryptographic signatures, source authority or semantic truth.
Missing/invalid evidence leaves pending; existing descriptive facts are untouched.
"""
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

DIMENSIONS = ('definition', 'model', 'analysis', 'generation', 'modification', 'review', 'visual')
_HEX = re.compile(r'^[0-9a-f]{64}$')


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _reviewer(value):
    return isinstance(value, dict) and _text(value.get('id')) and _text(value.get('role'))


def _scope(scope, identity):
    return (isinstance(scope, dict) and _text(scope.get('purpose'))
            and isinstance(scope.get('capabilities'), list)
            and any(isinstance(x, dict) and (x.get('category'), x.get('id')) == identity
                    for x in scope['capabilities']))


def _strings(value):
    return isinstance(value, list) and bool(value) and all(_text(x) for x in value)


def _fingerprints(value):
    return (isinstance(value, dict) and bool(value)
            and all(_text(k) and isinstance(v, str) and _HEX.fullmatch(v)
                    for k, v in value.items()))


def evaluate_acceptance(entry, gate, root, current=None):
    """Return conservative status with concrete reasons; never raise for bad evidence.

    Callers must independently derive output_kind and current fingerprints rather
    than copying their values from the proposed gate. Paths are root-relative,
    fragments/absolute paths/traversal/symlink escapes are rejected.
    """
    reasons = []
    result = {'accepted': False, 'status': 'pending', 'reasons': reasons, 'dimensions': {}}
    if not isinstance(entry, dict) or not isinstance(gate, dict):
        reasons.append('entry-and-gate-must-be-objects')
        return result
    identity = (entry.get('category'), entry.get('id'))
    if not all(_text(x) for x in identity):
        reasons.append('entry-identity-missing')
    version = gate.get('schema_version')
    if version not in ('acceptance-gate-v1', 'acceptance-gate-v2'):
        reasons.append('strict-gate-schema-missing-or-unsupported')
    if (gate.get('category'), gate.get('id')) != identity:
        reasons.append('gate-capability-identity-mismatch')
    reviewer = gate.get('reviewer')
    if not _reviewer(reviewer):
        reasons.append('named-reviewer-and-role-required')
    if not _scope(gate.get('scope'), identity):
        reasons.append('gate-scope-does-not-include-capability')
    if not _fingerprints(current):
        reasons.append('current-runtime-fingerprints-required')
    if not _fingerprints(gate.get('runtime_fingerprints')) or gate.get('runtime_fingerprints') != current:
        reasons.append('runtime-fingerprint-missing-or-stale')
    try:
        base = Path(root).resolve(strict=True)
        if not base.is_dir():
            raise ValueError('root-not-directory')
    except (OSError, ValueError, TypeError, RuntimeError):
        reasons.append('evidence-root-unavailable')
        return result

    def file_bytes(ref, errors):
        if not isinstance(ref, dict):
            errors.append('evidence-reference-must-be-object')
            return None
        path, digest = ref.get('path'), ref.get('sha256')
        if (not _text(path) or '\\' in path or '#' in path or '?' in path
                or PurePosixPath(path).is_absolute() or '..' in PurePosixPath(path).parts
                or ':' in path or path.startswith('~')):
            errors.append('unsafe-evidence-path')
            return None
        if not isinstance(digest, str) or not _HEX.fullmatch(digest):
            errors.append('evidence-sha256-required:' + path)
            return None
        try:
            resolved = (base / path).resolve(strict=True)
            if not resolved.is_relative_to(base) or not resolved.is_file():
                errors.append('evidence-path-outside-root-or-not-file:' + path)
                return None
            content = resolved.read_bytes()
        except (OSError, ValueError, RuntimeError):
            errors.append('evidence-unreadable:' + path)
            return None
        if not content.strip():
            errors.append('empty-evidence:' + path)
            return None
        if hashlib.sha256(content).hexdigest() != digest:
            errors.append('evidence-hash-stale:' + path)
            return None
        return content

    dimensions = gate.get('dimensions')
    dimensions = dimensions if isinstance(dimensions, dict) else {}
    for dimension in DIMENSIONS:
        errors = []
        spec = dimensions.get(dimension)
        if not isinstance(spec, dict):
            spec = {}
        status = spec.get('status')
        if status not in ('passed', 'not-applicable'):
            errors.append('dimension-not-explicitly-passed')
        visual_optional = (entry.get('visual_applicable') is False or
                           ('visual_applicable' not in entry and entry.get('output_kind') == 'table'))
        # A project-convention definition may declare the dimension not applicable,
        # but that records absence of source proof rather than granting a pass.
        definition_optional = (dimension == 'definition'
                               and entry.get('evidence_class') == 'project-convention')
        if status == 'not-applicable' and not (
                (dimension == 'visual' and visual_optional) or definition_optional):
            errors.append('not-applicable-not-supported-by-entry-contract')
        if not _text(spec.get('rationale')):
            errors.append('dimension-rationale-required')
        refs = spec.get('evidence')
        if not isinstance(refs, list) or not refs:
            refs = []
            errors.append('dimension-evidence-required')
        for ref in refs:
            blob = file_bytes(ref, errors)
            if blob is None:
                continue
            from evidence_integrity import verify_reference
            context = {'method_id': identity[1]} if identity[0] == 'analysis-method' else {}
            errors.extend(verify_reference(ref, base, context))
            try:
                document = json.loads(blob)
            except (ValueError, UnicodeError):
                errors.append('review-evidence-not-json')
                continue
            expected_schema = 'acceptance-review-records-v2' if version == 'acceptance-gate-v2' else 'acceptance-review-records-v1'
            if not isinstance(document, dict) or document.get('schema_version') != expected_schema:
                errors.append('review-record-schema-required')
                continue
            records = document.get('records')
            records = records if isinstance(records, list) else []
            selected = [x for x in records if isinstance(x, dict) and x.get('id') == ref.get('record_id')]
            if not _text(ref.get('record_id')) or len(selected) != 1:
                errors.append('unique-review-record-id-required')
                continue
            record = selected[0]
            if record.get('dimension') != dimension or record.get('status') != status:
                errors.append('review-record-dimension-or-status-mismatch')
            if not _reviewer(record.get('reviewer')) or record.get('reviewer') != reviewer:
                errors.append('review-record-reviewer-mismatch')
            if not _scope(record.get('scope'), identity):
                errors.append('review-record-scope-does-not-include-capability')
            if not _strings(record.get('observations')):
                errors.append('substantive-review-observations-required')
            assets = record.get('assets')
            if not isinstance(assets, list) or not assets:
                assets = []
                errors.append('reviewed-assets-required')
            verified = {}
            for asset in assets:
                data = file_bytes(asset, errors)
                if data is not None:
                    if (base / asset['path']).resolve() == (base / ref['path']).resolve():
                        errors.append('review-record-cannot-be-its-own-reviewed-asset')
                    verified[asset['path']] = (asset['sha256'], data)
            if dimension == 'definition' and status == 'passed':
                # The class is derived from the registry by the caller and passed in
                # on the entry. It decides which kind of proof counts, so a profile
                # without an inspectable source figure is not forced to fabricate one.
                evidence_class = entry.get('evidence_class', 'source-figure')
                if evidence_class == 'source-text':
                    comparisons = record.get('text_comparisons')
                    if not isinstance(comparisons, list) or not comparisons:
                        errors.append('definition-text-comparison-required')
                    else:
                        for comparison in comparisons:
                            if (not isinstance(comparison, dict)
                                    or not _text(comparison.get('source_path'))
                                    or comparison.get('source_path') not in verified
                                    or not _text(comparison.get('locator'))):
                                errors.append('definition-text-comparison-incomplete')
                                continue
                            quote = comparison.get('quoted_clause')
                            body = verified[comparison['source_path']][1].decode('utf-8', 'ignore')
                            if not _text(quote) or quote not in body:
                                errors.append('definition-quote-not-found')
                            from source_quote import navigation_quote
                            if navigation_quote(quote):
                                errors.append('definition-quote-is-navigation')
                            if not _text(comparison.get('conclusion')):
                                errors.append('definition-text-comparison-incomplete')
                elif evidence_class == 'project-convention':
                    basis = record.get('convention_basis')
                    if (not isinstance(basis, dict)
                            or not all(_text(basis.get(k)) for k in
                                       ('rule_id', 'rationale', 'owner', 'decided_at'))):
                        errors.append('convention-basis-incomplete')
                    elif basis['owner'] != entry.get('owner'):
                        errors.append('convention-owner-mismatch')
                elif evidence_class == 'source-figure':
                    comparisons = record.get('source_comparisons')
                    if not isinstance(comparisons, list) or not comparisons:
                        errors.append('definition-source-comparison-required')
                    else:
                        for comparison in comparisons:
                            if (not isinstance(comparison, dict) or not _text(comparison.get('source_path'))
                                    or comparison.get('source_path') not in verified
                                    or not _text(comparison.get('locator')) or not _text(comparison.get('conclusion'))):
                                errors.append('definition-source-comparison-incomplete')
                else:
                    errors.append('evidence-class-required-from-entry-contract')
            if dimension == 'visual' and status == 'passed':
                originals, outputs = record.get('original_assets'), record.get('output_assets')
                kind = 'source-structure-equivalence'
                if version == 'acceptance-gate-v2':
                    kind = entry.get('visual_review_kind')
                    if kind not in ('source-structure-equivalence', 'business-layout', 'document-layout'):
                        errors.append('visual-kind-required-from-entry-contract')
                        continue
                    if record.get('visual_review_kind') != kind:
                        errors.append('visual-review-kind-mismatch')
                    if kind == 'document-layout' and entry.get('category') != 'deliverable':
                        errors.append('document-layout-requires-deliverable-contract')
                    if kind != 'source-structure-equivalence':
                        # Model/spec/page-index context is still hash-verified;
                        # a business layout or document need not invent an original image.
                        references = record.get('reference_assets')
                        if not _strings(references) or any(p not in verified for p in references):
                            errors.append('visual-reference-assets-required')
                        originals = []
                        if kind == 'document-layout' and (not _strings(record.get('page_ids'))
                                or len(record['page_ids']) != len(outputs or [])
                                or len(set(record['page_ids'])) != len(record['page_ids'])):
                            errors.append('document-page-coverage-required')
                if (kind == 'source-structure-equivalence' and not _strings(originals)) or not _strings(outputs):
                    errors.append('visual-original-and-output-assets-required')
                    continue
                if set(originals) & set(outputs):
                    errors.append('visual-original-and-output-must-be-distinct')
                opened = record.get('opened_assets')
                opened = opened if isinstance(opened, list) else []
                for path in set(originals + outputs):
                    if path not in verified:
                        errors.append('visual-asset-not-hash-verified:' + path)
                        continue
                    digest, data = verified[path]
                    image = (data.startswith(b'\x89PNG\r\n\x1a\n') or data.startswith(b'\xff\xd8\xff')
                             or data.startswith((b'GIF87a', b'GIF89a'))
                             or (data.startswith(b'RIFF') and data[8:12] == b'WEBP')
                             or b'<svg' in data[:1024])
                    if not image:
                        errors.append('visual-asset-not-recognized-image:' + path)
                    matches = [x for x in opened if isinstance(x, dict) and x.get('path') == path]
                    if (len(matches) != 1 or matches[0].get('opened') is not True
                            or matches[0].get('sha256') != digest
                            or not _reviewer(reviewer) or matches[0].get('reviewer_id') != reviewer['id']
                            or not _strings(matches[0].get('observations'))):
                        errors.append('visual-actual-opening-review-required:' + path)
        result['dimensions'][dimension] = {'status': status if not errors else 'pending', 'reasons': errors}
        reasons.extend(dimension + ':' + error for error in errors)
    # A not-applicable dimension records absence of proof, so it can never complete a
    # seven-dimension record. One exception is preserved: the visual dimension for a
    # table contract, which the registry itself derives as inapplicable (there is no
    # standalone figure to open). That case was already accepted before this change.
    blocking_na = sorted(
        dim for dim, value in result['dimensions'].items()
        if value['status'] == 'not-applicable'
        and not (dim == 'visual' and visual_optional))
    if blocking_na:
        reasons.append('not-applicable-dimensions-prevent-complete-acceptance:'
                       + ','.join(blocking_na))
    result['accepted'] = not reasons
    result['status'] = 'accepted-record-verified' if not reasons else 'pending'
    return result
