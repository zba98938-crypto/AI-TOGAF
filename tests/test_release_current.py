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
from verify_implementation_ledger import declared_inputs


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))


class ReleaseCurrentTest(unittest.TestCase):
    def fixture(self, root):
        package, release = root / 'skills', root / 'release'
        write(package / '_shared/package-lock.json', {'lockfileVersion': 3})
        write(package / '_shared/corpus/source-map.json', {'logical_paths': {}})
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


if __name__ == '__main__':
    unittest.main()
