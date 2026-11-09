"""Real temporary HTTP/SQLite/subprocess tests; no historical output fixtures."""
import copy
import hashlib
import http.client
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workbench.server import create_server, MAX_BODY, Workbench


class WorkbenchHTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='togaf-workbench-test-')
        self.data = Path(self.tmp.name) / 'data'
        self.start()

    def start(self, **kwargs):
        self.server = create_server(port=0, data_dir=self.data, **kwargs)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_port

    def stop(self):
        self.server.shutdown()
        self.thread.join(5)
        self.server.server_close()
        self.server.app.close()

    def tearDown(self):
        self.stop()
        self.tmp.cleanup()

    def request(self, method, path, data=None, headers=None, raw=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.port, timeout=20)
        body = json.dumps(data, ensure_ascii=False).encode() if data is not None else raw
        all_headers = {'Content-Type': 'application/json'} if method == 'POST' else {}
        all_headers.update(headers or {})
        connection.request(method, path, body=body, headers=all_headers)
        response = connection.getresponse()
        content = response.read()
        mime = response.getheader('Content-Type', '')
        result = json.loads(content) if 'application/json' in mime else content
        status = response.status
        connection.close()
        return status, result

    def create(self, **kwargs):
        status, result = self.request('POST', '/api/projects', dict(name='临时项目', **kwargs))
        self.assertEqual(status, 201, result)
        self.assertTrue(result['validation']['valid'])
        return result

    def save(self, project, model=None, **kwargs):
        return self.request('POST', f'/api/projects/{project["id"]}/versions', dict(
            base_version=project['head_version'], model=model or project['model'], layout={}, message='edit', **kwargs))

    def wait_job(self, identity):
        deadline = time.monotonic() + 35
        while time.monotonic() < deadline:
            status, job = self.request('GET', '/api/jobs/' + identity)
            self.assertEqual(status, 200, job)
            if job['status'] in ('succeeded', 'failed'):
                return job
            time.sleep(.03)
        self.fail('Generation did not terminate')

    def test_health_catalog_and_projects(self):
        self.assertEqual(self.request('GET', '/api/health')[1]['status'], 'ok')
        status, catalog = self.request('GET', '/api/catalog')
        self.assertEqual(status, 200)
        self.assertIn('trust-framework-default', [t['id'] for t in catalog['templates']])
        first = self.create()
        second = self.create(model=first['model'])
        self.assertNotEqual(first['id'], second['id'])
        self.assertEqual(first['model'], second['model'])
        self.assertEqual(first['layout'], {})
        self.assertEqual(first['jobs'], [])
        self.assertEqual(self.request('GET', '/api/projects/' + first['id'])[1], first)
        projects = self.request('GET', '/api/projects')[1]['projects']
        self.assertEqual(len(projects), 2)
        self.assertEqual(self.request('POST', '/api/projects', {'name': 'x', 'template': '../../bad'})[0], 400)
        self.assertEqual(self.request('GET', '/api/projects/missing')[0], 404)

    def test_validation_rejects_errors_without_mutation_or_inferred_approval(self):
        project = self.create()
        bad = copy.deepcopy(project['model'])
        bad['entities'][0]['approval_status'] = 'approved'
        bad['entities'][0]['approval_evidence'] = []
        status, result = self.request('POST', '/api/validate', {'model': bad})
        self.assertEqual(status, 200)
        self.assertFalse(result['valid'])
        self.assertIn('approval-without-evidence', [i['code'] for i in result['issues']])
        self.assertEqual(self.save(project, bad)[0], 422)
        self.assertEqual(self.request('POST', '/api/projects', {'name': 'bad', 'model': bad})[0], 422)
        current = self.request('GET', '/api/projects/' + project['id'])[1]
        self.assertEqual(current['head_version'], project['head_version'])
        self.assertEqual(current['model'], project['model'])
        self.assertEqual(len(current['versions']), 1)
        status, result = self.request('POST', '/api/validate', {'model': []})
        self.assertEqual(status, 200)
        self.assertFalse(result['valid'])

    def test_save_conflict_immutable_versions_and_full_diff(self):
        project = self.create()
        model = copy.deepcopy(project['model'])
        model['project']['name'] = '用户显式改名'
        model['sources'][0]['description'] += ' edited'
        model['entities'][0]['name'] += ' edited'
        model['sources'].append({'id': 'extra', 'kind': 'assumption', 'description': 'new assumption'})
        status, updated = self.request('POST', f'/api/projects/{project["id"]}/versions', {
            'base_version': project['head_version'], 'model': model,
            'layout': {'nodes': {'n': {'x': 22, 'y': -8}}}, 'message': 'explicit edits'})
        self.assertEqual(status, 201, updated)
        self.assertNotEqual(updated['head_version'], project['head_version'])
        self.assertEqual(self.save(project)[0], 409)
        url = f'/api/projects/{project["id"]}/versions/{project["head_version"]}'
        original = self.request('GET', url)[1]
        self.assertEqual(original['model'], project['model'])
        self.assertEqual(original['layout'], {})
        self.assertEqual(original['model_hash'], hashlib.sha256(json.dumps(
            project['model'], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest())
        status, diff = self.request('GET', f'/api/projects/{project["id"]}/diff?from={project["head_version"]}&to={updated["head_version"]}')
        self.assertEqual(status, 200)
        self.assertEqual({c['group'] for c in diff['changes']}, {'project', 'sources', 'entities', 'layout'})
        added = next(c for c in diff['changes'] if c['id'] == 'extra')
        self.assertEqual(added['kind'], 'added')
        self.assertIsNone(added['before'])
        status, reverted = self.save(updated, project['model'])
        self.assertEqual(status, 201, reverted)
        self.assertNotEqual(reverted['head_version'], project['head_version'])
        diff = self.request('GET', f'/api/projects/{project["id"]}/diff?from={updated["head_version"]}&to={reverted["head_version"]}')[1]
        self.assertEqual(next(c for c in diff['changes'] if c['id'] == 'extra')['kind'], 'removed')
        self.assertEqual(self.request('PUT', url, {'model': model})[0], 405)
        self.assertEqual(self.request('GET', f'/api/projects/{project["id"]}/diff')[0], 400)

    def test_concurrent_save_exactly_one_wins(self):
        project = self.create()
        results = []
        barrier = threading.Barrier(2)

        def save():
            barrier.wait()
            results.append(self.save(project)[0])

        threads = [threading.Thread(target=save) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(10)
        self.assertEqual(sorted(results), [201, 409])

    def test_review_state_machine_and_old_version_binding(self):
        project = self.create()
        url = f'/api/projects/{project["id"]}/reviews'

        def review(action, version=project['head_version']):
            return self.request('POST', url, dict(version=version, action=action, author='本地评审人', comment='local statement'))

        self.assertEqual(review('accept')[0], 409)
        status, comment = review('comment')
        self.assertEqual(status, 201)
        self.assertEqual(comment['state'], 'draft')
        self.assertEqual(review('submit')[1]['state'], 'in_review')
        self.assertEqual(review('submit')[0], 409)
        status, updated = self.save(project)
        self.assertEqual(status, 201)
        status, accepted = review('accept')
        self.assertEqual(status, 201, accepted)
        self.assertEqual(accepted['version_hash'], project['head_version'])
        self.assertEqual(review('request_changes')[0], 409)
        detail = self.request('GET', '/api/projects/' + project['id'])[1]
        self.assertEqual(detail['review_state'], 'draft')
        self.assertEqual(detail['review_states'][project['head_version']], 'accepted')
        self.assertEqual(detail['model'], project['model'])
        self.assertEqual(len(detail['reviews']), 3)
        current_version = updated['head_version']
        self.assertEqual(review('submit', current_version)[0], 201)
        self.assertEqual(review('request_changes', current_version)[1]['state'], 'changes_requested')
        self.assertEqual(review('submit', current_version)[0], 409)
        self.assertEqual(review('comment', current_version)[1]['state'], 'changes_requested')

    def test_generation_success_download_and_no_traversal_or_symlinks(self):
        project = self.create()
        status, queued = self.request('POST', f'/api/projects/{project["id"]}/generate', {'version': project['head_version']})
        self.assertEqual(status, 202)
        self.assertEqual(queued['status'], 'queued')
        job = self.wait_job(queued['id'])
        self.assertEqual(job['status'], 'succeeded', job)
        self.assertEqual(job['version'], project['head_version'])
        names = [o['name'] for o in job['outputs']]
        self.assertIn('manifest.json', names)
        self.assertIn('workbench-layout.json', names)
        output = next(o for o in job['outputs'] if o['name'] == 'model.json')
        self.assertEqual(self.request('GET', output['url'])[1], project['model'])
        base = f'/api/jobs/{job["id"]}/files/'
        for traversal in ('../input.json', '%2e%2e/input.json', '%2fetc/passwd', '..%5cinput.json'):
            self.assertIn(self.request('GET', base + traversal)[0], (403, 404))
        root = self.server.app.output_root(job['id'])
        (root / 'escape').symlink_to(ROOT / 'togaf-standard-10th-ai/skills' / '_shared' / 'artifacts.json')
        (root / 'escape-dir').symlink_to(ROOT / 'togaf-standard-10th-ai/skills' / '_shared', target_is_directory=True)
        self.assertEqual(self.request('GET', base + 'escape')[0], 404)
        self.assertEqual(self.request('GET', base + 'escape-dir/artifacts.json')[0], 404)
        jobs = self.request('GET', '/api/projects/' + project['id'])[1]['jobs']
        self.assertEqual(jobs[0]['id'], job['id'])
        self.assertEqual(jobs[0]['status'], 'succeeded')
        self.assertNotIn('escape', [o['name'] for o in jobs[0]['outputs']])

    def test_generation_failure_and_timeout_are_not_success(self):
        project = self.create()
        model = copy.deepcopy(project['model'])
        model['views'] = []
        model['entities'] = []
        model['relationships'] = []
        empty = self.create(model=model)
        status, queued = self.request('POST', f'/api/projects/{empty["id"]}/generate', {'version': empty['head_version']})
        self.assertEqual(status, 202)
        failed = self.wait_job(queued['id'])
        self.assertEqual(failed['status'], 'failed', failed)
        self.assertIn('没有选择', failed['error'])
        self.assertEqual(failed['outputs'], [])
        self.assertEqual(self.request('GET', f'/api/jobs/{queued["id"]}/files/model.json')[0], 409)
        self.server.app.job_timeout = .001
        status, queued = self.request('POST', f'/api/projects/{project["id"]}/generate', {'version': project['head_version']})
        timed = self.wait_job(queued['id'])
        self.assertEqual(timed['status'], 'failed')
        self.assertIn('timed out', timed['error'])

    def test_restart_persists_data_resumes_queue_and_fails_interrupted_jobs(self):
        project = self.create()
        self.stop()
        self.start(start_worker=False)
        url = f'/api/projects/{project["id"]}/generate'
        queued = self.request('POST', url, {'version': project['head_version']})[1]
        interrupted = self.request('POST', url, {'version': project['head_version']})[1]
        with self.server.app.db() as db:
            db.execute("UPDATE jobs SET status='running' WHERE id=?", (interrupted['id'],))
        self.stop()
        self.start()
        persisted = self.request('GET', '/api/projects/' + project['id'])[1]
        self.assertEqual(persisted['model'], project['model'])
        self.assertEqual(len(persisted['jobs']), 2)
        self.assertEqual(self.wait_job(queued['id'])['status'], 'succeeded')
        failed = self.request('GET', '/api/jobs/' + interrupted['id'])[1]
        self.assertEqual(failed['status'], 'failed')
        self.assertIn('restarted', failed['error'])

    def test_origin_host_content_type_and_body_limits(self):
        path = '/api/projects'
        for origin in ('https://evil.example', 'null', f'http://127.0.0.1:{self.port + 1}', f'http://localhost:{self.port}'):
            self.assertEqual(self.request('POST', path, {'name': 'x'}, {'Origin': origin})[0], 403)
        for host in ('evil.example', '127.0.0.1', f'127.0.0.1:{self.port + 1}', f'127.0.0.1:{self.port}@evil.example'):
            self.assertEqual(self.request('GET', '/api/health', headers={'Host': host})[0], 403)
        self.assertEqual(self.request('POST', path, {'name': 'x'}, {'Content-Type': 'text/plain'})[0], 415)
        self.assertEqual(self.request('POST', path, {'name': 'x'}, {'Sec-Fetch-Site': 'cross-site'})[0], 403)
        self.assertEqual(self.request('POST', path, {'name': 'x'}, {'Origin': f'http://127.0.0.1:{self.port}'})[0], 201)
        self.assertEqual(self.request('POST', path, headers={'Content-Length': str(MAX_BODY + 1)}, raw=b'')[0], 413)
        self.assertEqual(self.request('OPTIONS', path)[0], 405)
        for raw in (b'{', b'[]', b'{"name":"x","name":"y"}', b'{"model":NaN}', b'{"model":1e999}', b'\xff'):
            self.assertEqual(self.request('POST', path, raw=raw)[0], 400, raw)
        self.assertEqual(self.request('POST', path, raw=b'{}', headers={'Transfer-Encoding': 'chunked'})[0], 400)

    def test_single_instance_and_serial_generation(self):
        with self.assertRaises(ValueError):
            create_server(port=0, data_dir=self.data)
        project = self.create()
        url = f'/api/projects/{project["id"]}/generate'
        first = self.request('POST', url, {'version': project['head_version']})[1]
        second = self.request('POST', url, {'version': project['head_version']})[1]
        one, two = self.wait_job(first['id']), self.wait_job(second['id'])
        self.assertEqual(one['status'], 'succeeded', one)
        self.assertEqual(two['status'], 'succeeded', two)
        self.assertGreaterEqual(two['started_at'], one['finished_at'])

    def test_worker_denies_network_and_out_of_job_writes(self):
        directory = Path(self.tmp.name) / 'sandbox-job'
        directory.mkdir()
        out = directory / 'outputs'
        out.mkdir()
        model = directory / 'input.json'
        model.write_text('{}')
        outside = Path(self.tmp.name) / 'forbidden.txt'
        for attempt in ("__import__('socket').socket().connect(('203.0.113.1', 80))",
                        f"__import__('pathlib').Path({str(outside)!r}).write_text('forbidden')"):
            script = f'''import sys
sys.path.insert(0, {str(ROOT)!r})
from workbench.server import generation_worker
import generate
def attempt(*args, **kwargs):
    {attempt}
generate.generate = attempt
generation_worker({str(model)!r}, {str(out)!r})
'''
            result = subprocess.run([sys.executable, '-c', script], capture_output=True, text=True, timeout=15)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('PermissionError', result.stderr)
            self.assertFalse(outside.exists())

    def test_static_security_and_no_arbitrary_file_access(self):
        for path in ('/../skills/_shared/artifacts.json', '/%2e%2e/skills/_shared/artifacts.json', '/api/../server.py', '/%5cetc/passwd'):
            self.assertEqual(self.request('GET', path)[0], 403)
        self.assertEqual(self.request('GET', '/server.py')[0], 404)
        self.assertEqual(self.request('GET', '/api/jobs/unknown')[0], 404)
        with self.assertRaises(ValueError):
            create_server(host='0.0.0.0', port=0, data_dir=self.data)
        with self.assertRaises(ValueError):
            Workbench(ROOT / 'togaf-standard-10th-ai/skills' / '_shared' / 'workbench-test', start_worker=False)


if __name__ == '__main__':
    unittest.main()
