"""Native editor uses real HTTP, immutable SQLite versions and local worker outputs."""
import base64
import copy
import hashlib
import http.client
import json
from pathlib import Path
import sys
import tempfile
import threading
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from workbench.server import create_server

BPMN = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" id="D" targetNamespace="urn:workbench:test">
 <process id="P" isExecutable="false"><startEvent id="S"/><endEvent id="E"/><sequenceFlow id="F" sourceRef="S" targetRef="E"/></process>
</definitions>'''
UML = '''<?xml version="1.0" encoding="UTF-8"?>
<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:version="2.5.1" xmi:id="M" name="订单模型">
 <packagedElement xmi:type="uml:Class" xmi:id="C" name="订单"/>
</uml:Model>'''


def source(text=BPMN, language='bpmn'):
    return {'language': language, 'version': '2.0.2' if language == 'bpmn' else '2.5.1', 'xml': text}


class NativeWorkbenchHTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='togaf-native-workbench-test-')
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

    def request(self, method, path, data=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.port, timeout=30)
        body = json.dumps(data, ensure_ascii=False).encode() if data is not None else None
        connection.request(method, path, body=body, headers={'Content-Type': 'application/json'} if body else {})
        response = connection.getresponse()
        raw = response.read()
        mime = response.getheader('Content-Type', '')
        result = json.loads(raw) if 'application/json' in mime else raw
        status = response.status
        connection.close()
        return status, result

    def create(self, native=None, **kwargs):
        payload = {'name': '原生测试项目', **kwargs}
        if native is not None:
            payload['native'] = native
        status, project = self.request('POST', '/api/projects', payload)
        self.assertEqual(status, 201, project)
        return project

    def save(self, project, **kwargs):
        return self.request('POST', f'/api/projects/{project["id"]}/versions', {
            'base_version': project['head_version'], 'model': project['model'], 'layout': project['layout'],
            'message': '原文编辑', **kwargs})

    def enqueue(self, project, **kwargs):
        return self.request('POST', f'/api/projects/{project["id"]}/generate', {
            'version': project['head_version'], 'kind': 'native', **kwargs})

    def wait_job(self, identity):
        deadline = time.monotonic() + 60
        while time.monotonic() < deadline:
            status, result = self.request('GET', '/api/jobs/' + identity)
            self.assertEqual(status, 200, result)
            if result['status'] in ('succeeded', 'blocked', 'failed'):
                return result
            time.sleep(.03)
        self.fail('Native generation did not terminate within 60 seconds')

    def output(self, job, name):
        entry = next(x for x in job['outputs'] if x['name'] == name)
        status, result = self.request('GET', entry['url'])
        self.assertEqual(status, 200)
        return result

    def test_exact_utf8_bom_crlf_and_version_source_binding(self):
        text = '\ufeff' + BPMN.replace('\n', '\r\n')
        project = self.create(source(text))
        expected = hashlib.sha256(text.encode('utf-8')).hexdigest()
        self.assertEqual(project['native']['xml'], text)
        self.assertEqual(project['native']['source_sha256'], expected)
        self.assertEqual(project['versions'][0]['native_sha256'], expected)
        self.assertEqual(project['model']['entities'], [])
        self.assertEqual(project['model']['relationships'], [])
        self.assertEqual(project['model']['project']['approval_status'], 'unknown')
        self.assertTrue(project['validation']['valid'])
        self.assertFalse(project['validation']['native']['conformance_complete'])
        changed_text = text.replace('id="P"', 'id="P" name="用户修改"')
        status, changed = self.save(project, native=source(changed_text))
        self.assertEqual(status, 201, changed)
        self.assertNotEqual(project['head_version'], changed['head_version'])
        self.assertEqual(project['versions'][0]['model_hash'], changed['versions'][-1]['model_hash'])
        before = self.request('GET', f'/api/projects/{project["id"]}/versions/{project["head_version"]}')[1]
        self.assertEqual(before['native']['xml'], text)
        diff = self.request('GET', f'/api/projects/{project["id"]}/diff?from={project["head_version"]}&to={changed["head_version"]}')[1]
        raw = next(x for x in diff['changes'] if x['group'] == 'native' and x['id'] == 'xml')
        self.assertEqual((raw['before'], raw['after']), (text, changed_text))

    def test_legacy_save_preserves_native_and_explicit_null_removes_only_new_version(self):
        project = self.create(source())
        status, legacy = self.save(project)
        self.assertEqual(status, 201, legacy)
        self.assertEqual(legacy['native'], project['native'])
        status, removed = self.save(legacy, native=None)
        self.assertEqual(status, 201, removed)
        self.assertIsNone(removed['native'])
        old = self.request('GET', f'/api/projects/{project["id"]}/versions/{project["head_version"]}')[1]
        self.assertEqual(old['native'], project['native'])
        plain = self.create()
        self.assertIsNone(plain['native'])
        self.assertTrue(plain['validation']['valid'])
        self.assertEqual(self.enqueue(plain)[0], 422)

    def test_invalid_drafts_save_but_generation_and_accept_fail(self):
        for text in ('<definitions>', '<!DOCTYPE x [<!ENTITY e SYSTEM "file:///etc/passwd">]><x>&e;</x>', BPMN.replace('targetRef="E"', 'targetRef="missing"')):
            with self.subTest(text=text[:45]):
                project = self.create(source(text))
                diagnostic = project['validation']['native']
                self.assertFalse(project['validation']['valid'])
                self.assertFalse(diagnostic['valid'])
                self.assertTrue(diagnostic['validation_errors'])
                self.assertEqual(self.save(project, native=source(text))[0], 201)
                for kind in ('native', 'project'):
                    status, rejected = self.enqueue(project, kind=kind)
                    self.assertEqual(status, 422, rejected)
                    self.assertEqual(rejected['error'], 'native_validation_failed')
                url = f'/api/projects/{project["id"]}/reviews'
                body = {'version': project['head_version'], 'author': '本地测试', 'comment': '未签署'}
                self.assertEqual(self.request('POST', url, {**body, 'action': 'submit'})[0], 201)
                status, rejected = self.request('POST', url, {**body, 'action': 'accept'})
                self.assertEqual(status, 422, rejected)
                self.assertEqual(rejected['error'], 'native_validation_failed')
                current = self.request('GET', '/api/projects/' + project['id'])[1]
                self.assertEqual(current['review_states'][project['head_version']], 'in_review')
                self.assertEqual(current['jobs'], [])

    def test_contract_rejects_versions_fingerprints_and_arbitrary_resource_fields(self):
        for change in ({'version': '2.0'}, {'language': 'archimate'}, {'source_sha256': '0' * 64},
                       {'package_root': '/etc'}, {'input': '../../source'}, {'xml': 5}):
            with self.subTest(change=change):
                value = {**source(), **change}
                self.assertEqual(self.request('POST', '/api/native/validate', {'native': value})[0], 400)
                self.assertEqual(self.request('POST', '/api/projects', {'name': '拒绝输入', 'native': value})[0], 400)
        self.assertEqual(self.request('POST', '/api/native/validate', {})[0], 400)
        project = self.create(source())
        for change in ({'kind': 'shell'}, {'auto_layout': 'true'}, {'render': 'true'}):
            self.assertEqual(self.enqueue(project, **change)[0], 400)
        non_utf8 = source(BPMN.replace('encoding="UTF-8"', 'encoding="GBK"'))
        self.assertFalse(self.request('POST', '/api/native/validate', {'native': non_utf8})[1]['valid'])

    def test_missing_material_and_uncovered_capability_are_separate(self):
        text = UML.replace('<packagedElement xmi:type="uml:Class" xmi:id="C" name="订单"/>',
                           '<packagedElement xmi:type="uml:Class" xmi:id="C" name="订单"><ownedAttribute xmi:id="A" name="属性"><type href="library.uml#T"/></ownedAttribute></packagedElement>')
        status, diagnostic = self.request('POST', '/api/native/validate', {'native': source(text, 'uml')})
        self.assertEqual(status, 200, diagnostic)
        self.assertTrue(diagnostic['valid'])
        self.assertFalse(diagnostic['conformance_complete'])
        self.assertEqual(diagnostic['validation_errors'], [])
        self.assertTrue(diagnostic['missing_material'])
        self.assertTrue(diagnostic['capability_uncovered'])
        self.assertTrue(all(i['category'] == 'missing_material' for i in diagnostic['missing_material']))
        self.assertTrue(all(i['category'] == 'capability_uncovered' for i in diagnostic['capability_uncovered']))
        for reference in ('file:///etc/passwd#T', 'javascript:alert(1)', 'data:text/plain,source', '../outside.uml#T', '/etc/passwd#T', '%2e%2e/outside.uml#T'):
            with self.subTest(reference=reference):
                unsafe = text.replace('library.uml#T', reference)
                rejected = self.request('POST', '/api/native/validate', {'native': source(unsafe, 'uml')})[1]
                self.assertFalse(rejected['valid'])
                self.assertIn('native-unsafe-reference', [i['code'] for i in rejected['validation_errors']])

    def test_exchange_worker_preserves_exact_source_and_package_hashes(self):
        text = '\ufeff' + BPMN.replace('\n', '\r\n')
        project = self.create(source(text))
        status, queued = self.enqueue(project)
        self.assertEqual(status, 202, queued)
        job = self.wait_job(queued['id'])
        self.assertEqual(job['status'], 'succeeded', job)
        self.assertEqual(job['version'], project['head_version'])
        expected = project['native']['source_sha256']
        self.assertEqual(job['native_source_sha256'], expected)
        self.assertFalse(job['full_language_acceptance'])
        self.assertEqual(self.output(job, 'native.bpmn'), text.encode('utf-8'))
        package = self.output(job, 'native-package.json')
        self.assertEqual(base64.b64decode(package['native_xml']), text.encode('utf-8'))
        self.assertEqual(package['native_sha256'], expected)
        manifest = self.output(job, 'manifest.json')
        self.assertEqual(manifest['native_source_sha256'], expected)
        self.assertEqual(manifest['preview']['status'], 'not-requested')
        for name, expected_hash in manifest['output_sha256'].items():
            with self.server.app.output_root(job['id']).joinpath(name).open('rb') as stream:
                self.assertEqual(hashlib.sha256(stream.read()).hexdigest(), expected_hash)

    def test_no_di_preview_is_blocked_without_rewriting_bpmn(self):
        project = self.create(source())
        status, queued = self.enqueue(project, render=True)
        self.assertEqual(status, 202, queued)
        job = self.wait_job(queued['id'])
        self.assertEqual(job['status'], 'blocked', job)
        self.assertEqual(job['native_preview']['category'], 'missing_material')
        self.assertFalse(job['auto_layout'])
        self.assertEqual(self.output(job, 'native.bpmn'), BPMN.encode())
        self.assertFalse(job['native_preview']['derived_layout'])
        self.assertNotIn('native-preview.png', [i['name'] for i in job['outputs']])

    def test_uml_requires_explicit_layout_and_renders_after_user_selection(self):
        project = self.create(source(UML, 'uml'))
        blocked = self.wait_job(self.enqueue(project, render=True)[1]['id'])
        self.assertEqual(blocked['status'], 'blocked', blocked)
        self.assertEqual(blocked['native_preview']['category'], 'missing_material')
        rendered = self.wait_job(self.enqueue(project, render=True, auto_layout=True)[1]['id'])
        self.assertEqual(rendered['status'], 'succeeded', rendered)
        self.assertTrue(rendered['native_preview']['derived_layout'])
        self.assertFalse(rendered['full_language_acceptance'])
        self.assertEqual(self.output(rendered, 'native.uml'), UML.encode())
        self.assertTrue(self.output(rendered, 'native-preview.png').startswith(b'\x89PNG\r\n\x1a\n'))
        svg = self.output(rendered, 'native-preview.svg').decode('utf-8')
        self.assertIn('data-native-id="C"', svg)
        self.assertIn('订单', svg)

    def test_existing_umldi_is_preserved_and_uncovered_preview_stays_explicit(self):
        text = UML.replace('xmlns:uml=', 'xmlns:umldi="http://www.omg.org/spec/UML/20161101/UMLDI" xmlns:uml=')
        text = text.replace('</uml:Model>', '<umldi:UMLDiagram xmi:id="DI"/></uml:Model>')
        project = self.create(source(text, 'uml'))
        job = self.wait_job(self.enqueue(project, render=True, auto_layout=True)[1]['id'])
        self.assertEqual(job['status'], 'blocked', job)
        self.assertEqual(job['native_preview']['category'], 'capability_uncovered')
        self.assertEqual(self.output(job, 'native.uml'), text.encode())
        self.assertFalse(job['native_preview']['derived_layout'])

    def test_restart_restores_native_source_and_queued_exchange_kind(self):
        project = self.create(source(UML, 'uml'))
        self.stop()
        self.start(start_worker=False)
        status, queued = self.enqueue(project, auto_layout=True)
        self.assertEqual(status, 202, queued)
        self.stop()
        self.start()
        current = self.request('GET', '/api/projects/' + project['id'])[1]
        self.assertEqual(current['native'], project['native'])
        self.assertEqual(current['jobs'][0]['kind'], 'native')
        self.assertTrue(current['jobs'][0]['auto_layout'])
        job = self.wait_job(queued['id'])
        self.assertEqual(job['status'], 'succeeded', job)
        self.assertEqual(self.output(job, 'native.uml'), UML.encode())


if __name__ == '__main__':
    unittest.main()
