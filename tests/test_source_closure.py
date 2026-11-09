"""All retrieval records require package-local byte-preserved sources."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(REPO / 'togaf-standard-10th-ai/skills/_shared/scripts'),
                str(REPO / 'togaf-standard-10th-ai/maintenance')]
from source_closure import SourceResolver, sha256, source_requirements, verify_source_closure
import corpus_query
import close_skill_sources
import build_skill_package
import seal_release


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False) + '\n', encoding='utf-8')


class SourceClosureTest(unittest.TestCase):
    def fixture(self, root):
        source = root / 'retained/source.md'
        source.parent.mkdir(parents=True)
        source.write_text('业务来源：历史译文保持未验收。', encoding='utf-8')
        logical = 'historical/source.md'
        record = {'id': 'old-translation', 'text': source.read_text(), 'source_path': logical,
                  'source_sha256': sha256(source), 'content_role': 'translation',
                  'quality': {'status': 'translation-unverified'}}
        save(root / 'retrieval/chunks.jsonl', record)
        source_map = {'logical_paths': {logical: 'retained/source.md'},
                      'file_sha256': {'retained/source.md': sha256(source)},
                      'retrieval_index_sha256': {'retrieval/chunks.jsonl': sha256(root / 'retrieval/chunks.jsonl')}}
        save(root / 'source-map.json', source_map)
        return source, logical, record, source_map

    def test_complete_closure_after_independent_directory_relocation(self):
        with tempfile.TemporaryDirectory() as temporary:
            original = Path(temporary) / 'original'
            self.fixture(original)
            expected = verify_source_closure(original)
            self.assertTrue(expected['passed'], expected['issues'])
            relocated = Path(temporary) / 'relocated'
            shutil.copytree(original, relocated)
            shutil.rmtree(original)
            actual = verify_source_closure(relocated)
            self.assertTrue(actual['passed'], actual['issues'])
            self.assertEqual(expected['input_sha256'], actual['input_sha256'])
            self.assertEqual('not-established-by-source-accessibility', actual['semantic_acceptance'])

    def test_unmapped_missing_source_in_any_index_blocks_closure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            save(root / 'retrieval/new-index.jsonl', {
                'id': 'missing', 'source_path': 'missing.md', 'source_sha256': 'a' * 64})
            report = verify_source_closure(root)
            self.assertFalse(report['passed'])
            self.assertEqual(2, report['counts']['records'])
            self.assertIn('source-file-missing', {r['code'] for r in report['issues']})

    def test_two_record_fingerprints_for_one_identity_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, _, record, _ = self.fixture(root)
            save(root / 'retrieval/second.jsonl', {**record, 'id': 'conflict', 'source_sha256': 'a' * 64})
            self.assertIn('source-fingerprint-conflict', {r['code'] for r in verify_source_closure(root)['issues']})

    def test_tampering_preserves_existence_and_reports_unavailable_bytes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, logical, record, _ = self.fixture(root)
            source.write_text('changed')
            resolved = SourceResolver(root).resolve(logical, record['source_sha256'])
            self.assertTrue(resolved['exists'])
            self.assertFalse(resolved['source_available'])
            self.assertEqual('source-fingerprint-mismatch', resolved['reason'])
            self.assertFalse(verify_source_closure(root)['passed'])

    def test_missing_manifest_fingerprint_blocks_release_gate(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, _, _, source_map = self.fixture(root)
            source_map.pop('file_sha256')
            save(root / 'source-map.json', source_map)
            self.assertIn('source-map-fingerprint-missing', {r['code'] for r in verify_source_closure(root)['issues']})

    def test_removed_or_changed_index_cannot_claim_full_source_closure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, _, record, _ = self.fixture(root)
            save(root / 'retrieval/chunks.jsonl', {**record, 'text': 'changed searchable content'})
            self.assertIn('retrieval-index-set-or-fingerprint-mismatch',
                          {r['code'] for r in verify_source_closure(root)['issues']})

    def test_mapping_escape_and_dangerous_protocol_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'corpus'
            _, logical, _, source_map = self.fixture(root)
            for target in ['../private.md', '/etc/passwd', 'file:///etc/passwd',
                           'https://example.invalid/source.md', '//host/source.md', 'bad\\path']:
                with self.subTest(target=target):
                    source_map['logical_paths'][logical] = target
                    resolved = SourceResolver(root, source_map).resolve(logical)
                    self.assertFalse(resolved['exists'])
                    self.assertFalse(resolved['source_available'])
            for identity in ['../private.md', '/etc/passwd', 'file:///etc/passwd',
                             'https://example.invalid/source.md', '//host/source.md', 'bad\\path']:
                self.assertFalse(SourceResolver(root, source_map).resolve(identity)['source_available'])

    def test_symlink_source_map_and_index_escape_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'corpus'
            source, logical, _, _ = self.fixture(root)
            outside = Path(temporary) / 'private.md'
            outside.write_text('private bytes')
            source.unlink()
            source.symlink_to(outside)
            self.assertEqual('outside-package-source', SourceResolver(root).resolve(logical)['reason'])
            index = root / 'retrieval/chunks.jsonl'
            index.unlink()
            index.symlink_to(outside)
            self.assertIn('retrieval-index-outside-package', {r['code'] for r in verify_source_closure(root)['issues']})
            with patch.object(corpus_query, 'CORPUS', root), self.assertRaisesRegex(ValueError, 'index escapes'):
                corpus_query.query('private')
            (root / 'source-map.json').unlink()
            (root / 'source-map.json').symlink_to(outside)
            with self.assertRaisesRegex(ValueError, 'source map escapes'):
                SourceResolver(root)

    def test_fragment_and_mapped_historical_parent_identity(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, _, record, source_map = self.fixture(root)
            source_map['logical_paths']['../g226.pdf'] = 'retained/source.md'
            resolved = SourceResolver(root, source_map).resolve('../g226.pdf#page=2', record['source_sha256'])
            self.assertTrue(resolved['source_available'])
            self.assertEqual('retained/source.md#page=2', resolved['package_path'])

    def test_query_uses_one_resolution_and_preserves_translation_quality(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            with patch.object(corpus_query, 'CORPUS', root):
                match = corpus_query.query('业务来源')[0]
            self.assertTrue(match['source_exists_in_package'])
            self.assertEqual(match['resolved_source']['exists'], match['source_exists_in_package'])
            self.assertEqual(match['resolved_source']['source_available'], match['source_available'])
            self.assertEqual('translation-unverified', match['quality']['status'])
            self.assertEqual('translation-unverified', match['translation_status'])
            self.assertEqual('not-established-by-source-accessibility', match['semantic_acceptance'])

    def test_invalid_index_record_and_empty_index_never_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            save(root / 'retrieval/chunks.jsonl', {'id': 'bad', 'source_path': 'file'})
            self.assertIn('invalid-source-record', {r['code'] for r in source_requirements(root)['issues']})
            (root / 'retrieval/chunks.jsonl').write_text('')
            self.assertIn('retrieval-records-empty', {r['code'] for r in verify_source_closure(root)['issues']})

    def test_migration_and_index_fingerprints_both_bind_materialized_source(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'sources/retained/original.md'
            source.parent.mkdir(parents=True)
            source.write_text('source')
            logical, digest = 'historical/original.md', sha256(source)
            relocation = {'logical_paths': {logical: 'sources/retained/original.md'},
                          'files': [{'old_path': logical, 'local_path': 'sources/retained/original.md',
                                     'sha256': digest}]}
            with patch.object(close_skill_sources, 'C', root):
                actual, destination = close_skill_sources.indexed_source(logical, digest, relocation)
                self.assertEqual(source.resolve(), actual)
                self.assertEqual('sources/retained/original.md', destination)
                relocation['files'][0]['sha256'] = 'a' * 64
                with self.assertRaisesRegex(ValueError, 'Migration/index fingerprint conflict'):
                    close_skill_sources.indexed_source(logical, digest, relocation)
                relocation['logical_paths'][logical] = '../outside.md'
                with self.assertRaisesRegex(ValueError, 'escapes project'):
                    close_skill_sources.indexed_source(logical, digest, relocation)

    def test_builder_syncs_complete_index_set_and_removes_stale_index(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / 'retrieval'
            destination = root / 'skills/_shared/corpus/retrieval'
            for name in ['chunks.jsonl', 'new-index.jsonl']:
                save(source / name, {'source': name})
            save(destination / 'stale.jsonl', {})
            executable = root / 'skills/_shared/scripts/local_tool.py'
            executable.parent.mkdir(parents=True)
            executable.write_text('# small fixture')
            bind = SimpleNamespace(main=lambda: None)
            closure = SimpleNamespace(main=lambda: None)
            with patch.multiple(build_skill_package, C=root, DEST=root / 'skills'), \
                    patch.dict(sys.modules, {'bind_foundation_contracts': bind, 'close_skill_sources': closure}):
                build_skill_package.main()
            self.assertEqual({'chunks.jsonl', 'new-index.jsonl'}, {p.name for p in destination.glob('*.jsonl')})
            for name in ['chunks.jsonl', 'new-index.jsonl']:
                self.assertEqual((source / name).read_bytes(), (destination / name).read_bytes())

    def test_refresh_restores_only_valid_recorded_portable_reading_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / 'skills'
            document = package / '_shared/corpus/chapters/chapter.md'
            document.parent.mkdir(parents=True)
            document.write_text('![来源图](figs/old.svg)\n')
            target = package / '_shared/corpus/retained/figure.svg'
            target.parent.mkdir(parents=True)
            target.write_text('<svg/>')
            row = {'file': '_shared/corpus/chapters/chapter.md', 'old': 'figs/old.svg',
                   'new': '../retained/figure.svg'}
            save(package / 'reading-link-manifest.json', {'rewrites': [row]})
            with patch.object(build_skill_package, 'DEST', package):
                build_skill_package.restore_portable_reading_links()
                self.assertEqual('![来源图](../retained/figure.svg)\n', document.read_text())
                document.write_text('![来源图](figs/old.svg)\n')
                target.unlink()
                with self.assertRaisesRegex(ValueError, 'dependency missing or outside'):
                    build_skill_package.restore_portable_reading_links()

    def test_sealing_checks_full_closure_before_writing_any_archive(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / 'skills'
            corpus = package / '_shared/corpus'
            source, _, _, _ = self.fixture(corpus)
            source.unlink()
            with patch.multiple(seal_release, C=root, P=package, R=root / 'release'):
                with self.assertRaisesRegex(ValueError, 'Retrieval source closure failed'):
                    seal_release.main()
            self.assertFalse((root / 'release').exists())
            self.assertFalse((package / 'build-provenance.json').exists())

    def test_build_repair_chain_preserves_historical_upstream_and_prior_records(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / 'skills'
            save(package / 'upstream-manifest.json', {'files': [], 'history': 'original bytes'})
            save(package / 'source.json', {'version': 1})
            original = (package / 'upstream-manifest.json').read_bytes()
            with patch.multiple(seal_release, C=root, P=package, R=root / 'release'), \
                    patch.object(seal_release, 'git_provenance', return_value={
                        'baseline_revisions': ['baseline'], 'current_revision': 'current'}):
                first = seal_release.record_build_provenance()
                first_path = package / first['record']['path']
                first_bytes = first_path.read_bytes()
                save(package / 'source.json', {'version': 2})
                second = seal_release.record_build_provenance()
            self.assertEqual(original, (package / 'upstream-manifest.json').read_bytes())
            self.assertEqual(first_bytes, first_path.read_bytes())
            current = json.loads((package / second['record']['path']).read_text())
            self.assertEqual(first['record'], current['previous_record'])
            self.assertEqual(['baseline'], current['git']['baseline_revisions'])
            self.assertEqual(sha256(package / 'source.json'), current['source_files']['source.json'])
            with patch.object(seal_release, 'P', package):
                self.assertTrue(seal_release.include(first_path))
                self.assertTrue(seal_release.include(package / 'build-provenance.json'))

    def test_changed_prior_build_record_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / 'skills'
            save(package / 'upstream-manifest.json', {'files': []})
            with patch.multiple(seal_release, C=root, P=package, R=root / 'release'), \
                    patch.object(seal_release, 'git_provenance', return_value={'baseline_revisions': ['baseline']}):
                first = seal_release.record_build_provenance()
                seal_release.record_build_provenance()
                (package / first['record']['path']).write_text('changed old record')
                with self.assertRaisesRegex(ValueError, 'Previous build history changed'):
                    seal_release.record_build_provenance()

    def test_sealing_refuses_existing_release_directory_without_writing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            release = root / 'release'
            release.mkdir()
            evidence = release / 'release-manifest.json'
            evidence.write_text('original release evidence')
            with patch.multiple(seal_release, C=root, P=root / 'skills', R=root / 'legacy-release'):
                with self.assertRaisesRegex(ValueError, 'Release directory must be new'):
                    seal_release.main(release)
            self.assertEqual('original release evidence', evidence.read_text())


if __name__ == '__main__':
    unittest.main()
