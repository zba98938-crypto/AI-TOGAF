"""A release must include new source files and use its actual dependency lock."""
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'togaf-standard-10th-ai/maintenance'))
import verify_release_current as release_check
import verify_portability
from verify_implementation_ledger import declared_inputs


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))


class ReleaseCurrentTest(unittest.TestCase):
    def fixture(self, root):
        package, release = root / 'skills', root / 'release'
        write(package / '_shared/package-lock.json', {'lockfileVersion': 3})
        source = package / '_shared/corpus/source.json'
        write(source, {'source': 'small verified fixture'})
        write(package / '_shared/corpus/source-map.json', {
            'logical_paths': {'source.json': 'source.json'},
            'file_sha256': {'source.json': release_check.sha(source)}})
        write(package / '_shared/corpus/retrieval/chunks.jsonl', {
            'id': 'fixture', 'source_path': 'source.json', 'source_sha256': release_check.sha(source)})
        write(package / '_shared/corpus/source-map.json', {
            'logical_paths': {'source.json': 'source.json'},
            'file_sha256': {'source.json': release_check.sha(source)},
            'retrieval_index_sha256': {'retrieval/chunks.jsonl': release_check.sha(package / '_shared/corpus/retrieval/chunks.jsonl')}})
        files = [{'path': str(p.relative_to(package)), 'sha256': release_check.sha(p)}
                 for p in sorted(package.rglob('*')) if p.is_file()]
        write(package / 'package-manifest.json', {'files': files})
        release.mkdir()
        archive = release / 'source.tar.gz'
        with tarfile.open(archive, 'w:gz') as target:
            for p in sorted(package.rglob('*')):
                if p.is_file():
                    target.add(p, arcname='skills/' + str(p.relative_to(package)))
        node = release / 'node.tar.gz'
        with tarfile.open(node, 'w:gz'):
            pass
        dependency_manifest = release / 'dependencies.json'
        write(dependency_manifest, {'lockfile_sha256': release_check.sha(package / '_shared/package-lock.json')})
        write(release / 'release-manifest.json', {
            'package': {'path': archive.name, 'sha256': release_check.sha(archive)},
            'optional_node_dependencies': {'path': node.name, 'sha256': release_check.sha(node),
                'manifest': dependency_manifest.name, 'manifest_sha256': release_check.sha(dependency_manifest)},
            'package_manifest_sha256': release_check.sha(package / 'package-manifest.json')})
        return package, release

    def test_new_source_file_invalidates_release_and_stored_evidence(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, release = self.fixture(root)
            with patch.multiple(release_check, C=root, P=package, R=release):
                report = release_check.verify()
                self.assertTrue(report['passed'], report['issues'])
                write(root / 'quality/release.json', report)
                write(package / '_shared/examples/new-teaching-case.json', {'case': 'added'})
                self.assertIn('unsealed source file _shared/examples/new-teaching-case.json', release_check.verify()['issues'])
                changed = [r for r in declared_inputs(root, root / 'quality/release.json') if not r['passed']]
                self.assertEqual(['skills'], [r['path'] for r in changed])

    def test_runtime_work_and_dependency_files_are_excluded_from_source_set(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, release = self.fixture(root)
            write(package / 'work/run.json', {'runtime': True})
            write(package / '_shared/node_modules/runtime.json', {})
            with patch.multiple(release_check, C=root, P=package, R=release):
                self.assertTrue(release_check.verify()['passed'])

    def test_changed_lockfile_and_archive_cannot_keep_current_status(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, release = self.fixture(root)
            with patch.multiple(release_check, C=root, P=package, R=release):
                report = release_check.verify()
                write(root / 'quality/release.json', report)
                write(package / '_shared/package-lock.json', {'lockfileVersion': 4})
                self.assertIn('dependency archive was prepared for a different lockfile', release_check.verify()['issues'])
                with (release / 'source.tar.gz').open('ab') as target:
                    target.write(b'changed')
                failed = [r['path'] for r in declared_inputs(root, root / 'quality/release.json') if not r['passed']]
                self.assertIn('skills/_shared/package-lock.json', failed)
                self.assertIn('release/source.tar.gz', failed)

    def test_explicit_release_directory_and_report_bind_actual_inputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, release = self.fixture(root)
            actual_release = root / 'round-release'
            release.rename(actual_release)
            output = root / 'round/report.json'
            with patch.multiple(release_check, C=root, P=package, R=release):
                self.assertEqual(0, release_check.main(actual_release, output))
                report = json.loads(output.read_text())
                self.assertIn('round-release/release-manifest.json', report['input_sha256'])
                self.assertNotIn('release/release-manifest.json', report['input_sha256'])
                original = output.read_bytes()
                with self.assertRaisesRegex(ValueError, 'path must be new'):
                    release_check.main(actual_release, output)
                self.assertEqual(original, output.read_bytes())

    def test_portability_refuses_previous_report_or_extraction_before_execution(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = root / 'previous.json'
            output.write_text('old evidence')
            with self.assertRaisesRegex(ValueError, 'Report path must be new'):
                verify_portability.main(root / 'release', root / 'new-extraction', output)
            self.assertFalse((root / 'new-extraction').exists())
            self.assertEqual('old evidence', output.read_text())
            extracted = root / 'old-extraction'
            extracted.mkdir()
            with self.assertRaisesRegex(ValueError, 'Extraction directory must be new'):
                verify_portability.main(root / 'release', extracted, root / 'new-report.json')
            self.assertFalse((root / 'new-report.json').exists())


if __name__ == '__main__':
    unittest.main()
