"""Verify every retrieval source using package-local paths and recorded bytes."""
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
import hashlib
import json
import re
from source_dependencies import dependency_evidence,has_symlink


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def _fingerprint(value):
    return isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value) is not None


def source_requirements(corpus):
    """Derive required identities from all indexes, including historical records."""
    corpus = Path(corpus)
    indexes = sorted((corpus / 'retrieval').glob('*.jsonl'))
    requirements, issues, records, index_hashes = {}, [], 0, {}
    if not indexes:
        issues.append({'code': 'retrieval-index-missing'})
    for index in indexes:
        if corpus.resolve() not in index.resolve().parents or not index.is_file() or has_symlink(index,corpus.resolve()):
            issues.append({'code': 'retrieval-index-outside-package', 'index': index.name})
            continue
        index_hashes[index.relative_to(corpus).as_posix()] = sha256(index)
        with index.open(encoding='utf-8') as stream:
            for line_number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                records += 1
                location = {'index': index.name, 'line': line_number}
                try:
                    row = json.loads(line)
                    logical, fingerprint = row['source_path'], row['source_sha256']
                    if not isinstance(logical, str) or not logical or not _fingerprint(fingerprint):
                        raise ValueError('source_path and SHA-256 are required')
                except (ValueError, KeyError, TypeError) as exc:
                    issues.append({'code': 'invalid-source-record', **location, 'detail': str(exc)})
                    continue
                entry = requirements.setdefault(logical, {'sha256': fingerprint, 'record_ids': []})
                entry['record_ids'].append(row.get('id', str(location)))
                if entry['sha256'] != fingerprint:
                    issues.append({'code': 'source-fingerprint-conflict', 'logical_path': logical,
                                   'record_id': row.get('id'), **location})
    if not records:
        issues.append({'code': 'retrieval-records-empty'})
    return {'records': records, 'requirements': requirements, 'issues': issues,
            'index_sha256': index_hashes}


class SourceResolver:
    """One operation uses one mapping and one digest per actual file."""
    def __init__(self, corpus, source_map=None):
        self.corpus = Path(corpus).resolve()
        path = self.corpus / 'source-map.json'
        if source_map is None and path.exists() and (self.corpus not in path.resolve().parents or has_symlink(path,self.corpus)):
            raise ValueError('source map escapes package')
        self.source_map = source_map if source_map is not None else (
            json.loads(path.read_text(encoding='utf-8')) if path.is_file() else {})
        self.mapping = self.source_map.get('logical_paths', {})
        self.fingerprints = self.source_map.get('file_sha256', {})
        if not isinstance(self.mapping, dict) or not isinstance(self.fingerprints, dict):
            raise ValueError('source map paths and fingerprints must be objects')
        self.digests = {}

    def resolve(self, logical, expected_sha256=None):
        result = {'logical_path': logical, 'exists': False, 'source_available': False}
        if not isinstance(logical, str) or not logical or '\x00' in logical or '\\' in logical:
            return {**result, 'reason': 'invalid-source-path'}
        base, separator, fragment = logical.partition('#')
        try:
            parsed = urlsplit(base)
        except ValueError:
            return {**result, 'reason': 'invalid-source-path'}
        if parsed.scheme or parsed.netloc or PurePosixPath(base).is_absolute():
            return {**result, 'reason': 'outside-package-source'}
        relative = self.mapping.get(base, base.removeprefix('togaf-standard-10th-ai/'))
        if not isinstance(relative, str) or not relative or '\x00' in relative or '\\' in relative or '#' in relative:
            return {**result, 'reason': 'invalid-source-path'}
        try:
            relative_url = urlsplit(relative)
        except ValueError:
            return {**result, 'reason': 'invalid-source-path'}
        if (relative_url.scheme or relative_url.netloc
                or PurePosixPath(relative).is_absolute() or '..' in PurePosixPath(relative).parts):
            return {**result, 'reason': 'outside-package-source'}
        lexical=self.corpus/relative
        candidate = lexical.resolve()
        if self.corpus not in candidate.parents:
            return {**result, 'reason': 'outside-package-source'}
        if has_symlink(lexical,self.corpus):
            return {**result,'reason':'source-symlink-not-packaged'}
        exists = candidate.is_file()
        result.update(package_path=relative + ('#' + fragment if separator else ''), exists=exists,
                      sha256=None, fingerprint_matches=None)
        if not exists:
            return {**result, 'reason': 'source-file-missing'}
        if candidate not in self.digests:
            self.digests[candidate] = sha256(candidate)
        result['sha256'] = self.digests[candidate]
        recorded = self.fingerprints.get(relative)
        expected = [x for x in (expected_sha256, recorded) if x is not None]
        if any(not _fingerprint(x) for x in expected):
            return {**result, 'fingerprint_matches': False, 'reason': 'invalid-source-fingerprint'}
        if len(set(expected)) > 1:
            return {**result, 'fingerprint_matches': False, 'reason': 'source-fingerprint-conflict'}
        result['fingerprint_matches'] = all(result['sha256'] == x for x in expected) if expected else None
        result['source_available'] = result['fingerprint_matches'] is not False
        if not result['source_available']:
            result['reason'] = 'source-fingerprint-mismatch'
        return result


def verify_source_closure(corpus):
    """Shared mandatory gate for build, seal, release and relocated extraction."""
    corpus = Path(corpus).resolve()
    required = source_requirements(corpus)
    issues = list(required['issues'])
    sources = []
    try:
        resolver = SourceResolver(corpus)
        if not (corpus / 'source-map.json').is_file():
            issues.append({'code': 'source-map-missing'})
        if resolver.source_map.get('missing_required_sources'):
            issues.append({'code': 'source-map-recorded-missing-files'})
        if resolver.source_map.get('retrieval_index_sha256') != required['index_sha256']:
            issues.append({'code': 'retrieval-index-set-or-fingerprint-mismatch'})
        if ('required_source_count' in resolver.source_map
                and resolver.source_map['required_source_count'] != len(required['requirements'])):
            issues.append({'code': 'required-source-count-mismatch'})
        for logical, entry in sorted(required['requirements'].items()):
            resolved = resolver.resolve(logical, entry['sha256'])
            sources.append({**resolved, 'expected_sha256': entry['sha256'],
                            'record_ids': entry['record_ids']})
            relative = resolved.get('package_path', '').partition('#')[0]
            if relative not in resolver.fingerprints:
                issues.append({'code': 'source-map-fingerprint-missing', 'logical_path': logical})
            if not resolved['source_available']:
                issues.append({'code': resolved.get('reason', 'source-unavailable'), 'logical_path': logical})
        for logical, relative in sorted(resolver.mapping.items()):
            resolved = resolver.resolve(logical)
            if relative not in resolver.fingerprints:
                issues.append({'code': 'source-map-fingerprint-missing', 'logical_path': logical})
            if not resolved['source_available']:
                issues.append({'code': resolved.get('reason', 'source-unavailable'), 'logical_path': logical})
        dependencies,dependency_issues=dependency_evidence(corpus)
        issues.extend(dependency_issues)
        if resolver.source_map.get('markdown_dependencies',[])!=dependencies:
            issues.append({'code':'markdown-dependency-inventory-or-fingerprint-mismatch'})
        for row in dependencies:
            if (row['scope']=='corpus' and row.get('kind')!='source-map-self-reference'
                    and row['package_path'] not in resolver.fingerprints):
                issues.append({'code':'markdown-dependency-fingerprint-missing','document':row['document'],
                               'package_path':row['package_path']})
        file_hashes = {path.relative_to(corpus).as_posix(): digest
                       for path, digest in resolver.digests.items()}
    except (OSError, ValueError, TypeError) as exc:
        issues.append({'code': 'invalid-source-map', 'detail': str(exc)})
        file_hashes = {}
        dependencies=[]
    inputs = {**required['index_sha256'], **file_hashes}
    if (corpus / 'source-map.json').is_file() and corpus in (corpus / 'source-map.json').resolve().parents:
        inputs['source-map.json'] = sha256(corpus / 'source-map.json')
    return {'schema_version': 'retrieval-source-closure/1', 'passed': not issues,
            'counts': {'indexes': len(required['index_sha256']), 'records': required['records'],
                       'required_sources': len(required['requirements']),
                       'source_files_checked': len(file_hashes), 'issues': len(issues)},
            'markdown_dependency_count':len(dependencies),
            'issues': issues, 'sources': sources, 'input_sha256': inputs,
            'semantic_acceptance': 'not-established-by-source-accessibility'}


def require_source_closure(corpus):
    report = verify_source_closure(corpus)
    if not report['passed']:
        raise ValueError('Retrieval source closure failed: ' + json.dumps(report['issues'][:10], ensure_ascii=False))
    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path, default=Path(__file__).resolve().parents[1] / 'corpus')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    if args.out is not None and args.out.exists():
        parser.error('--out must be new; previous evidence is immutable')
    report = verify_source_closure(args.corpus)
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'passed': report['passed'], 'counts': report['counts'], 'issues': report['issues'][:10]}, ensure_ascii=False))
    return int(not report['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
