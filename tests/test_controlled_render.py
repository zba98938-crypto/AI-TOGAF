"""Independent adversarial boundary checks for the local graphic transport."""
import json
import os
import tempfile
import unittest
import sys
import time
from pathlib import Path
from unittest.mock import patch
from enterprise.local_render import (LocalRenderController, parts, validate_graphic, read_session,
                                    write_session, owned_processes, publish_session, rollback_session,
                                    OutputCleanupError)
from enterprise.runtime import Budget, Blocked

SVG = b'<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"><text x="20" y="50">safe</text></svg>'


class ControlledRenderTests(unittest.TestCase):
    def test_output_set_reservation_rejects_every_collision_without_partial_results(self):
        for collision in range(4):
            with self.subTest(collision=collision), tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)/'session'; root.mkdir(); results=root/'results'; results.mkdir()
                protected=Path(tmp)/'protected'; protected.write_bytes(b'protected unchanged')
                names=['results/job.'+suffix for suffix in ('svg','png','json','browser.png')]
                conflict=root/names[collision]; conflict.symlink_to(protected)
                fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY)
                try:
                    with self.assertRaises(OSError):
                        publish_session(fd,{name:b'new result' for name in names})
                    self.assertEqual({p.name for p in results.iterdir()},{conflict.name})
                    self.assertTrue(conflict.is_symlink())
                    self.assertEqual(protected.read_bytes(),b'protected unchanged')
                finally: os.close(fd)

    def test_output_write_failure_removes_reserved_files_and_preserves_unrelated_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'results').mkdir(); (root/'results/other.svg').write_bytes(SVG)
            fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY)
            real_write=os.write; calls=[]
            def fail_after_partial(fd,data):
                calls.append(fd)
                if len(calls)==1: return real_write(fd,data[:4])
                raise OSError('synthetic disk write failure')
            try:
                with patch('enterprise.local_render.os.write',side_effect=fail_after_partial):
                    with self.assertRaisesRegex(OSError,'disk write failure'):
                        publish_session(fd,{'results/job.svg':SVG,'results/job.png':b'png'})
                self.assertEqual({p.name for p in (root/'results').iterdir()},{'other.svg'})
                self.assertEqual((root/'results/other.svg').read_bytes(),SVG)
            finally: os.close(fd)

    def test_output_cleanup_preserves_replacements_and_reports_uncertified_ownership(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'session';root.mkdir();(root/'results').mkdir()
            protected=Path(tmp)/'protected';protected.write_bytes(b'unchanged')
            fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY)
            try:
                receipts=publish_session(fd,{'results/job.svg':SVG,'results/job.png':b'png'})
                replaced=root/'results/job.png'; replaced.unlink(); replaced.symlink_to(protected)
                with self.assertRaisesRegex(OutputCleanupError,'ownership changed'):
                    rollback_session(fd,receipts)
                self.assertTrue(replaced.is_symlink())
                self.assertFalse((root/'results/job.svg').exists())
                self.assertEqual(protected.read_bytes(),b'unchanged')
            finally: os.close(fd)

    def test_output_cleanup_handles_replacement_at_atomic_move_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'session';root.mkdir();(root/'results').mkdir()
            evidence=Path(tmp)/'trusted';evidence.mkdir()
            protected=Path(tmp)/'protected';protected.write_bytes(b'unchanged')
            fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY); real_rename=os.rename; injected=[]
            def replace_before_move(source,target,**kwargs):
                if source=='job.png' and not injected:
                    injected.append(source)
                    os.unlink(source,dir_fd=kwargs['src_dir_fd'])
                    os.symlink(protected,source,dir_fd=kwargs['src_dir_fd'])
                return real_rename(source,target,**kwargs)
            try:
                receipts=publish_session(fd,{'results/job.svg':SVG,'results/job.png':b'png'},evidence)
                with patch('enterprise.local_render.os.rename',side_effect=replace_before_move):
                    with self.assertRaisesRegex(OutputCleanupError,'ownership changed'):
                        rollback_session(fd,receipts,evidence)
                self.assertTrue(injected)
                self.assertTrue((root/'results/job.png').is_symlink())
                self.assertFalse((root/'results/job.svg').exists())
                self.assertEqual(protected.read_bytes(),b'unchanged')
                self.assertFalse(list(evidence.iterdir()))
            finally: os.close(fd)

    def test_output_cleanup_restore_collision_preserves_both_replacement_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'session';root.mkdir();(root/'results').mkdir()
            evidence=Path(tmp)/'trusted';evidence.mkdir()
            protected=Path(tmp)/'protected';protected.write_bytes(b'unchanged')
            fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY);real_rename=os.rename;injected=[]
            def replace_and_occupy(source,target,**kwargs):
                if source=='job.png' and not injected:
                    injected.append(source);parent=kwargs['src_dir_fd']
                    os.unlink(source,dir_fd=parent);os.symlink(protected,source,dir_fd=parent)
                    real_rename(source,target,**kwargs)
                    occupant=os.open(source,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600,dir_fd=parent)
                    with os.fdopen(occupant,'wb') as stream:stream.write(b'new occupant')
                    return
                return real_rename(source,target,**kwargs)
            try:
                receipts=publish_session(fd,{'results/job.svg':SVG,'results/job.png':b'png'},evidence)
                with patch('enterprise.local_render.os.rename',side_effect=replace_and_occupy):
                    with self.assertRaisesRegex(OutputCleanupError,'retained without deletion'):
                        rollback_session(fd,receipts,evidence)
                self.assertEqual((root/'results/job.png').read_bytes(),b'new occupant')
                retained=list(evidence.glob('render-rollback-*/*'))
                self.assertEqual(len(retained),1);self.assertTrue(retained[0].is_symlink())
                self.assertEqual(os.readlink(retained[0]),str(protected))
                self.assertFalse((root/'results/job.svg').exists())
                self.assertEqual(protected.read_bytes(),b'unchanged')
            finally: os.close(fd)

    def test_output_set_publication_returns_only_current_owned_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'results').mkdir()
            fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY)
            try:
                payloads={'results/job.svg':SVG,'results/job.png':b'png bytes'}
                receipts=publish_session(fd,payloads)
                self.assertEqual([item['path'] for item in receipts],list(payloads))
                for name,data in payloads.items(): self.assertEqual((root/name).read_bytes(),data)
                rollback_session(fd,receipts)
                self.assertFalse(list((root/'results').iterdir()))
            finally: os.close(fd)

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
