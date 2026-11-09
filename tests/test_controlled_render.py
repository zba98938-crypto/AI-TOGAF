"""Independent adversarial boundary checks for the local graphic transport."""
import json
import os
import tempfile
import unittest
import sys
import time
from pathlib import Path
from unittest.mock import patch
from enterprise.local_render import LocalRenderController, parts, validate_graphic, read_session, write_session, owned_processes
from enterprise.runtime import Budget, Blocked

SVG = b'<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"><text x="20" y="50">safe</text></svg>'


class ControlledRenderTests(unittest.TestCase):
    def test_process_inspection_failure_cannot_certify_empty_cleanup(self):
        from subprocess import CompletedProcess
        for result in (CompletedProcess([],1,'','denied'),CompletedProcess([],0,'','')):
            with patch('enterprise.local_render.subprocess.run',return_value=result):
                with self.assertRaisesRegex(RuntimeError,'inspection unavailable'):
                    owned_processes(123,Path('/synthetic-task'))

    def test_live_private_output_counts_toward_campaign_resource_stop(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);out=root/'retained';out.mkdir();private=root/'private';private.mkdir()
            (private/'browser-cache').write_bytes(b'x'*2048)
            budget=Budget(out,max_hours=1,output_gib=1024/(1024**3),min_free_gib=0)
            budget.live_output_roots=(private,)
            with patch('enterprise.runtime.owned_resources',return_value={'rss_bytes':0,'browser_roots':0}):
                with self.assertRaisesRegex(Blocked,'output limit'):budget.check(force=True)
            self.assertTrue(budget.cancel.is_set())
            self.assertGreaterEqual(budget.samples[0]['output_bytes'],2048)

    def test_paths_refuse_absolute_escape_protocol_encoded_and_noncanonical(self):
        for name in ('/etc/passwd', '../other/secret.svg', 'a/../b.svg', './a.svg', 'a//b.svg',
                     'file:a.svg', 'https://example.com/a.svg', 'a%2fb.svg', 'a\\b.svg', 'a\0b.svg'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                parts(name)

    def test_source_and_output_symlink_escape_is_denied(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'session'; root.mkdir()
            outside = Path(tmp)/'protected'; outside.mkdir()
            (outside/'secret.svg').write_bytes(SVG)
            (root/'source.svg').symlink_to(outside/'secret.svg')
            (root/'out').symlink_to(outside, target_is_directory=True)
            fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaises(OSError): read_session(fd, 'source.svg')
                with self.assertRaises(OSError): write_session(fd, 'out/overwrite.svg', SVG)
                self.assertFalse((outside/'overwrite.svg').exists())
                self.assertEqual((outside/'secret.svg').read_bytes(), SVG)
            finally: os.close(fd)

    def test_named_pipe_and_oversized_inputs_are_denied_without_blocking(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); os.mkfifo(root/'pipe.svg')
            (root/'large.svg').write_bytes(b'x'*100)
            fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaises(ValueError): read_session(fd, 'pipe.svg')
                with self.assertRaises(ValueError): read_session(fd, 'large.svg', 50)
            finally: os.close(fd)

    def test_cross_session_and_external_hardlinks_are_denied(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'session'; root.mkdir()
            other = Path(tmp)/'other'; other.mkdir()
            (other/'secret.svg').write_bytes(SVG)
            os.link(other/'secret.svg', root/'linked.svg')
            fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
            try:
                with self.assertRaises(ValueError): read_session(fd, 'linked.svg')
                self.assertEqual((other/'secret.svg').read_bytes(), SVG)
            finally: os.close(fd)

    def test_active_content_external_resources_and_entities_are_denied(self):
        samples = [
            b'<script>alert(1)</script>', b'<foreignObject><p>html</p></foreignObject>',
            b'<image href="file:///etc/passwd"/>', b'<use href="https://example.com/x.svg"/>',
            b'<text onclick="alert(1)">x</text>', b'<style>@import "https://example.com/x";</style>',
            b'<style>text{fill:url(/etc/passwd)}</style>', b'<style>text{fill:u\\rl(/etc/passwd)}</style>',
            b'<set attributeName="href" to="/etc/passwd"/>',
            b'<style></style>u\\rl(/etc/passwd)',
        ]
        for content in samples:
            data = b'<svg xmlns="http://www.w3.org/2000/svg">'+content+b'</svg>'
            with self.subTest(content=content), self.assertRaises(ValueError): validate_graphic('svg', data)
        with self.assertRaises(ValueError):
            validate_graphic('svg', b'<!DOCTYPE svg [<!ENTITY x SYSTEM "file:///etc/passwd">]>'+SVG)

    def test_fixed_schema_refuses_commands_urls_arguments_and_arbitrary_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'session'; root.mkdir()
            (root/'protected.txt').write_text('synthetic protected content')
            controller = LocalRenderController(Path(tmp), sys.executable, Path(tmp)/'evidence')
            controller.register(root)
            controller.stop.set(); controller.thread.join()
            session = controller.sessions[str(root.resolve())]
            cases = [
                {'kind':'svg', 'source':'protected.txt'},
                {'kind':'svg', 'source':'../other/secret.svg'},
                {'kind':'svg', 'source':'/etc/passwd'},
                {'kind':'svg', 'source':'a.svg', 'command':'touch protected.txt'},
                {'kind':'svg', 'source':'a.svg', 'url':'https://example.com'},
                {'kind':'svg', 'source':'a.svg', 'browser_args':['--no-sandbox']},
                {'kind':'shell', 'source':'a.svg'},
            ]
            for i, task in enumerate(cases):
                identity = '%032x' % i
                (root/'.render/inbox'/(identity+'.json')).write_text(json.dumps(task))
                result = controller.handle(session, identity)
                self.assertEqual(result['status'], 'refused')
                self.assertTrue(result['cleaned'])
            self.assertEqual((root/'protected.txt').read_text(), 'synthetic protected content')
            self.assertFalse(list((root/'.render/results').iterdir()))
            self.assertTrue(controller.close()['private_directory_cleaned'])

    def test_mermaid_links_html_configuration_and_scripts_are_denied(self):
        for source in ('flowchart LR\nA-->B\nclick A "https://example.com"',
                       '%%{init:{"securityLevel":"loose"}}%%\nflowchart LR\nA-->B',
                       'flowchart LR\nA[<img src="file:///etc/passwd">]',
                       'flowchart LR\nA[https://example.com]'):
            with self.subTest(source=source), self.assertRaises(ValueError):
                validate_graphic('mmd', source.encode())

    def test_local_svg_fragments_and_chinese_mermaid_are_accepted(self):
        validate_graphic('svg', SVG.replace(b'<text', b'<path fill="url(#arrow)"/><text'))
        validate_graphic('mmd', 'flowchart LR\n A[业务需求] --> B[架构评审]'.encode())
        validate_graphic('uml-class-layout',b'<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001"/>')
        with self.assertRaises(ValueError):validate_graphic('uml-class-layout',SVG)
        with self.assertRaises(ValueError):validate_graphic('uml-class-layout',b'<model href="file:///etc/passwd"/>')

    def test_pending_queue_is_bounded_without_launching_a_worker(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'session';root.mkdir()
            controller=LocalRenderController(Path(tmp),sys.executable,Path(tmp)/'evidence')
            controller.register(root)
            for i in range(65):
                (root/'.render/inbox'/('%032x.json'%i)).write_text('{}')
            deadline=time.monotonic()+2
            while not controller.events and time.monotonic()<deadline:
                time.sleep(.02)
            result=controller.close()
            self.assertEqual(result['tasks'],1)
            self.assertEqual(result['refused'],1)
            self.assertIn('queue limit',controller.events[0]['reason'])
            self.assertTrue(controller.sessions[str(root.resolve())]['quota_exceeded'])


if __name__ == '__main__':
    unittest.main()
