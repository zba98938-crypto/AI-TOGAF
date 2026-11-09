"""Storage controls preserve useful evidence while bounding disposable output."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import TestCase, mock
import json
import sqlite3
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'togaf-standard-10th-ai/skills/_shared/scripts'
MAINTENANCE = ROOT / 'togaf-standard-10th-ai/maintenance'
sys.path[:0] = [str(ROOT), str(SCRIPTS), str(MAINTENANCE)]

from workbench.server import APIError, Workbench
import build_skill_package
import generate as generator
import seal_release
import verify_portability


class WorkbenchStorageTests(TestCase):
    def test_existing_database_gets_prune_tracking_column(self):
        with tempfile.TemporaryDirectory() as temporary:
            data = Path(temporary) / 'data'
            data.mkdir()
            with sqlite3.connect(data / 'workbench.sqlite3') as db:
                db.execute('CREATE TABLE jobs (id TEXT PRIMARY KEY, project_id TEXT, version TEXT, '
                           'status TEXT, render INTEGER, created_at TEXT, started_at TEXT, '
                           'finished_at TEXT, error TEXT)')
            app = Workbench(data, start_worker=False)
            try:
                with app.db() as db:
                    columns = {row['name'] for row in db.execute('PRAGMA table_info(jobs)')}
                self.assertIn('outputs_pruned_at', columns)
            finally:
                app.close()

    def test_expired_failed_outputs_are_pruned_without_deleting_log_or_job(self):
        with tempfile.TemporaryDirectory() as temporary:
            app = Workbench(Path(temporary) / 'data', start_worker=False)
            try:
                project = app.create_project({'name': 'storage test'})
                job = app.enqueue(project['id'], {'version': project['head_version']})
                root = app.jobs_dir / job['id']
                output = root / 'outputs'
                output.mkdir(parents=True)
                (output / 'partial.bin').write_bytes(b'x' * 8192)
                (root / 'generation.log').write_text('diagnostic retained')
                old = (datetime.now(timezone.utc) - timedelta(days=8)).isoformat()
                with app.db() as db:
                    db.execute("UPDATE jobs SET status='failed', finished_at=? WHERE id=?", (old, job['id']))
                self.assertEqual(app.prune_failed_outputs(), 1)
                self.assertFalse(output.exists())
                self.assertEqual((root / 'generation.log').read_text(), 'diagnostic retained')
                with app.db() as db:
                    self.assertEqual(app.job(db, job['id'])['status'], 'failed')
            finally:
                app.close()

    def test_total_limit_rejects_new_jobs_and_per_job_limit_detects_growth(self):
        with tempfile.TemporaryDirectory() as temporary:
            app = Workbench(Path(temporary) / 'data', max_job_bytes=4096,
                            max_job_store_bytes=8192, start_worker=False)
            try:
                project = app.create_project({'name': 'storage test'})
                job = app.enqueue(project['id'], {'version': project['head_version']})
                output = app.output_root(job['id'])
                output.mkdir(parents=True)
                (output / 'large.bin').write_bytes(b'x' * 12288)
                self.assertIn('per-job', app.storage_issue(job['id']))
                with self.assertRaises(APIError) as caught:
                    app.enqueue(project['id'], {'version': project['head_version']})
                self.assertEqual(caught.exception.status, 507)
            finally:
                app.close()

    def test_generation_log_keeps_only_diagnostic_tail(self):
        with tempfile.TemporaryDirectory() as temporary:
            app = Workbench(Path(temporary) / 'data', max_job_bytes=16 * 1024,
                            start_worker=False)
            try:
                identity = 'diagnostic'
                root = app.jobs_dir / identity
                root.mkdir()
                log = root / 'generation.log'
                log.write_bytes(b'a' * 8192 + b'failure at end')
                app.trim_generation_log(identity)
                self.assertEqual(log.stat().st_size, 2048)
                self.assertTrue(log.read_bytes().endswith(b'failure at end'))
            finally:
                app.close()

    def test_completed_output_prune_requires_explicit_apply(self):
        with tempfile.TemporaryDirectory() as temporary:
            app = Workbench(Path(temporary) / 'data', start_worker=False)
            try:
                project = app.create_project({'name': 'storage test'})
                job = app.enqueue(project['id'], {'version': project['head_version']})
                output = app.output_root(job['id'])
                output.mkdir(parents=True)
                (output / 'result.bin').write_bytes(b'x' * 8192)
                old = (datetime.now(timezone.utc) - timedelta(days=31)).isoformat()
                with app.db() as db:
                    db.execute("UPDATE jobs SET status='succeeded', finished_at=? WHERE id=?", (old, job['id']))
                preview = app.prune_completed_outputs(30)
                self.assertFalse(preview['applied'])
                self.assertEqual(preview['total_bytes'], 8192)
                self.assertTrue(output.exists())
                applied = app.prune_completed_outputs(30, apply=True)
                self.assertTrue(applied['applied'])
                self.assertFalse(output.exists())
                with app.db() as db:
                    current = app.job(db, job['id'])
                self.assertEqual(current['status'], 'succeeded')
                self.assertTrue(current['outputs_pruned'])
            finally:
                app.close()

    def test_running_job_exceeding_limit_fails_and_discards_partial_outputs(self):
        xml = ('<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" '
               'targetNamespace="urn:storage"><process id="P"/></definitions>')
        with tempfile.TemporaryDirectory() as temporary:
            app = Workbench(Path(temporary) / 'data', max_job_bytes=4096,
                            max_job_store_bytes=1024 * 1024)
            try:
                project = app.create_project({'name': 'storage test',
                                              'native': {'language': 'bpmn', 'version': '2.0.2', 'xml': xml}})
                job = app.enqueue(project['id'], {'version': project['head_version'], 'kind': 'native'})
                deadline = time.monotonic() + 15
                while time.monotonic() < deadline:
                    with app.db() as db:
                        result = app.job(db, job['id'])
                    if result['status'] in ('succeeded', 'blocked', 'failed'):
                        break
                    time.sleep(.05)
                self.assertEqual(result['status'], 'failed', result)
                self.assertIn('storage limit', result['error'])
                self.assertFalse(app.output_root(job['id']).exists())
                self.assertTrue((app.jobs_dir / job['id'] / 'generation.log').is_file())
            finally:
                app.close()


class StagedGenerationTests(TestCase):
    def test_unrelated_existing_directory_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / 'unrelated'
            out.mkdir()
            (out / 'notes.txt').write_text('keep')
            with self.assertRaisesRegex(ValueError, 'not a generated delivery'):
                generator.staged_generate({}, out)
            self.assertEqual((out / 'notes.txt').read_text(), 'keep')

    def test_success_replaces_old_directory_and_discards_stale_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / 'delivery'
            out.mkdir()
            (out / 'stale.txt').write_text('old')
            (out / 'manifest.json').write_text('{"schema_version":"2.0"}')

            def fake_generate(model, staging, *args):
                (staging / 'current.txt').write_text('new')
                return {'artifacts': [], 'deliverables': [], 'rendered': False}

            with mock.patch.object(generator, 'generate', side_effect=fake_generate):
                generator.staged_generate({}, out)
            self.assertFalse((out / 'stale.txt').exists())
            self.assertEqual((out / 'current.txt').read_text(), 'new')
            self.assertEqual(list(Path(temporary).glob('.delivery.*')), [])

    def test_failed_generation_preserves_previous_delivery(self):
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / 'delivery'
            out.mkdir()
            (out / 'current.txt').write_text('keep')
            (out / 'manifest.json').write_text('{"schema_version":"2.0"}')

            def fail(model, staging, *args):
                (staging / 'partial.txt').write_text('discard')
                raise ValueError('invalid model')

            with mock.patch.object(generator, 'generate', side_effect=fail):
                with self.assertRaisesRegex(ValueError, 'invalid model'):
                    generator.staged_generate({}, out)
            self.assertEqual((out / 'current.txt').read_text(), 'keep')
            self.assertEqual(list(Path(temporary).glob('.delivery.*')), [])


class IncrementalCorpusCopyTests(TestCase):
    def test_unchanged_file_is_not_rewritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, target = root / 'source', root / 'target'
            source.write_text('same')
            target.write_text('same')
            before = target.stat().st_mtime_ns
            build_skill_package.copy_changed(source, target)
            self.assertEqual(target.stat().st_mtime_ns, before)
            source.write_text('changed')
            build_skill_package.copy_changed(source, target)
            self.assertEqual(target.read_text(), 'changed')


class ReleaseStorageTests(TestCase):
    def test_source_only_release_omits_node_archive(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package, release = root / 'skills', root / 'release'
            package.mkdir()
            (package / 'source.txt').write_text('portable source')
            (package / 'upstream-manifest.json').write_text(json.dumps({'files': [], 'skills': []}))
            for relative, value in (
                ('fundamental/chinese-text/index.json', {'volumes': [], 'counts': {}}),
                ('fundamental/web-2025/manifest.json', {'documents': []}),
                ('supplementary/chinese-text/G226.json', {'coverage': {}, 'body_complete': True}),
            ):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(value))
            with mock.patch.multiple(seal_release, C=root, P=package, R=release), \
                    mock.patch.object(seal_release, 'require_source_closure', return_value={'passed': True, 'counts': {}}), \
                    mock.patch.object(seal_release, 'record_build_provenance', return_value={'record': {'path': 'source.txt'}}):
                seal_release.main(source_only=True)
            report = json.loads((release / 'release-manifest.json').read_text())
            self.assertTrue(report['source_only'])
            self.assertIsNone(report['optional_node_dependencies'])
            self.assertTrue((release / report['package']['path']).is_file())
            self.assertEqual(list(release.glob('togaf-node-dependencies-*.tar.gz')), [])
            with self.assertRaisesRegex(ValueError, 'Source-only release'):
                verify_portability.main(release, root / 'extracted', root / 'portability.json')
            self.assertFalse((root / 'extracted').exists())
