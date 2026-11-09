"""Bounded local import graph, per-role identity and byte-preserving exchange."""
import base64
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO/'togaf-standard-10th-ai/skills/_shared/scripts'
sys.path.insert(0,str(SCRIPTS))
sys.path.insert(0,str(REPO))
import bpmn_imports as imports
from standards import check_native, make_package, package_bytes, Invalid, Incomplete
from bpmn_import_resource_fixtures import BPMN,XSD,WSDL,ROOT,CHILD,document,imported,record,SOURCE_SHA256


class BPMNImportResourcesTests(unittest.TestCase):
    def check(self, data=ROOT, rows=None, **kwargs):
        return check_native(data,'bpmn','2.0.2',resources=rows if rows is not None else [record('shared/model.bpmn',CHILD)],**kwargs)

    def refs(self, report):
        return report['resource_closure']['references']

    def test_fixture_source_fingerprints_are_independently_bound(self):
        source=SCRIPTS.parent/'standards/sources/bpmn-2.0.2'
        for name,expected in SOURCE_SHA256.items():
            self.assertEqual(expected,hashlib.sha256((source/name).read_bytes()).hexdigest())

    def test_direct_identity_is_complete_but_cross_document_semantics_remains_uncovered(self):
        report=self.check()
        self.assertEqual([],report['errors'])
        self.assertEqual('complete',report['resource_closure']['status'])
        reference=self.refs(report)[0]
        self.assertEqual(('urn:shared','P','Process','Process','shared/model.bpmn'),tuple(reference[k] for k in ['namespace','native_id','expected_class','actual_class','target_document_path']))
        self.assertEqual('cross-document-role-uncovered',reference['semantic_status'])
        self.assertFalse(report['resource_closure']['full_standard_acceptance'])
        self.assertEqual(1,len(report['imported_document_validation']))

    def test_nested_document_base_allows_bounded_parent_segments(self):
        data=ROOT.replace(b'shared/model.bpmn',b'../shared/model.bpmn')
        self.assertEqual([],self.check(data,document_path='nested/main.bpmn')['errors'])
        self.assertEqual('shared/model.bpmn',imports.relative_location('nested/main.bpmn','../shared/./model.bpmn'))

    def test_transitive_imports_have_qualified_visibility(self):
        mid=document(imported('../other/model.bpmn','urn:other')+'<process id="P"/>','urn:shared')
        data=ROOT.replace(b'r:P',b's:P')
        report=self.check(data,[record('shared/model.bpmn',mid),record('other/model.bpmn',document('<process id="P"/>','urn:other'))])
        self.assertEqual([],report['errors'])
        self.assertEqual('other/model.bpmn',self.refs(report)[0]['target_document_path'])

    def test_same_raw_id_in_different_namespaces_does_not_alias(self):
        data=ROOT.replace(b'<collaboration',b'<process id="P"/><collaboration')
        report=self.check(data)
        self.assertEqual([],report['errors'])
        self.assertEqual('shared/model.bpmn',self.refs(report)[0]['target_document_path'])

    def test_same_namespace_and_id_in_two_imports_is_ambiguous(self):
        data=ROOT.replace(b'<collaboration',(imported('shared/other.bpmn')+'<collaboration').encode())
        report=self.check(data,[record('shared/model.bpmn',CHILD),record('shared/other.bpmn',CHILD)])
        self.assertEqual('ambiguous-id',self.refs(report)[0]['status'])
        self.assertTrue(report['errors'])

    def test_namespace_mismatch_missing_file_and_missing_id_are_distinct(self):
        mismatch=self.check(rows=[record('shared/model.bpmn',document('<process id="P"/>','urn:wrong'))])
        self.assertTrue(any('namespace mismatch' in x for x in mismatch['errors']))
        missing=self.check(rows=[])
        self.assertEqual([],missing['errors'])
        self.assertTrue(missing['diagnostic_groups']['missing_material'])
        absent=self.check(rows=[record('shared/model.bpmn',CHILD.replace(b'id="P"',b'id="Other"'))])
        self.assertEqual('missing-id',self.refs(absent)[0]['status'])

    def test_each_owner_field_checks_the_same_qname_independently(self):
        data=ROOT.replace(b'</definitions>',b'<messageEventDefinition id="M" messageRef="r:P"/></definitions>')
        report=self.check(data)
        refs=self.refs(report)
        self.assertEqual(2,len(refs))
        self.assertEqual({'processRef':'resolved-local-identity','messageRef':'type-mismatch'},{r['field']:r['status'] for r in refs})
        self.assertEqual('Message',next(r for r in refs if r['field']=='messageRef')['expected_class'])

    def test_qname_element_type_uses_parent_construct(self):
        data=document(imported()+'<partnerEntity id="PE"><participantRef>r:P</participantRef></partnerEntity>')
        good=document('<collaboration id="C"><participant id="P"/></collaboration>','urn:shared')
        report=self.check(data,[record('shared/model.bpmn',good)])
        self.assertEqual([],report['errors'])
        self.assertEqual('Participant',self.refs(report)[0]['expected_class'])
        bad=self.check(data)
        self.assertEqual('type-mismatch',self.refs(bad)[0]['status'])

    def test_call_activity_accepts_callable_element_subtype(self):
        data=document(imported()+'<process id="Main"><callActivity id="A" calledElement="r:P"/></process>')
        report=self.check(data)
        self.assertEqual([],report['errors'])
        self.assertEqual('CallableElement',self.refs(report)[0]['expected_class'])

    def test_unimported_namespace_cannot_alias_same_local_id(self):
        data=document('<process id="P"/><collaboration id="C"><participant id="A" processRef="r:P"/></collaboration>')
        self.assertEqual('namespace-not-imported',self.refs(self.check(data,[]))[0]['status'])

    def test_idref_cannot_cross_document(self):
        data=document(imported()+'<process id="Main"><task id="A"/><sequenceFlow id="F" sourceRef="P" targetRef="A"/></process>')
        self.assertTrue(any('dangling BPMN reference: P' in x for x in self.check(data)['errors']))

    def test_every_imported_document_runs_schema_and_local_semantics(self):
        for child,expected in [(CHILD.replace(b'<process id="P"',b'<process isExecutable="maybe" id="P"'),'isExecutable'),
                              (document('<process id="P"><startEvent id="S"><incoming>F</incoming></startEvent><task id="T"/><sequenceFlow id="F" sourceRef="T" targetRef="S"/></process>','urn:shared'),'startEvent has incoming'),
                              (b'<message xmlns="'+BPMN.encode()+b'" id="P"/>','root')]:
            with self.subTest(expected=expected):
                report=self.check(rows=[record('shared/model.bpmn',child)])
                self.assertTrue(any(expected in x for x in report['errors']),report['errors'])

    def test_no_explicit_context_never_probes_adjacent_disk(self):
        with patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('disk read')):
            report=check_native(ROOT,'bpmn','2.0.2')
            self.assertEqual([],report['errors'])
            self.assertTrue(report['diagnostic_groups']['missing_material'])

    def test_xsd_wsdl_and_other_import_types_are_uncovered_without_reads(self):
        for kind in (XSD,WSDL,'urn:custom'):
            with self.subTest(kind=kind),patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                data=document(imported('https://example.invalid/model',kind=kind))
                report=check_native(data,'bpmn','2.0.2',package_root=REPO)
                self.assertEqual([],report['errors'])
                self.assertEqual('unsupported-import-type',report['resource_closure']['imports'][0]['status'])
                self.assertTrue(report['diagnostic_groups']['capability_uncovered'])

    def test_import_xml_base_is_uncovered_without_silent_document_base_substitution(self):
        for value in ('../other/','https://example.invalid/','file:///etc/'):
            with self.subTest(value=value),patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                data=ROOT.replace(b'<definitions',('<definitions xml:base="'+value+'"').encode())
                report=check_native(data,'bpmn','2.0.2',package_root=REPO)
                self.assertEqual([],report['errors'])
                self.assertEqual('unsupported-xml-base',report['resource_closure']['imports'][0]['status'])
                self.assertEqual('incomplete',report['resource_closure']['status'])
        with patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
            invalid=check_native(ROOT.replace(b'<import',b'<import xml:base="../other/"'),'bpmn','2.0.2',package_root=REPO)
            self.assertTrue(any('base' in x and 'not allowed' in x for x in invalid['errors']))

    def test_resource_package_preflights_entire_total_before_root_decode(self):
        package=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',CHILD)])
        with patch.object(imports,'MAX_TOTAL_BYTES',len(ROOT)+len(CHILD)-1),patch.object(base64,'b64decode',side_effect=AssertionError('decode')):
            with self.assertRaises(Invalid):package_bytes(package,'bpmn','2.0.2')

    def test_invalid_import_paths_are_rejected_before_disk_reads(self):
        for path in ('../outside.bpmn','file:///etc/passwd','https://example.invalid/x','%2e%2e/x'):
            with self.subTest(path=path),patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                data=ROOT.replace(b'shared/model.bpmn',path.encode())
                report=check_native(data,'bpmn','2.0.2',package_root=REPO)
                self.assertTrue(report['errors'])

    def test_embedded_package_never_fills_missing_resource_from_cli_package_root(self):
        package=make_package(ROOT,'bpmn','2.0.2',resources=[])
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);(base/'shared').mkdir();(base/'shared/model.bpmn').write_bytes(CHILD)
            path=base/'package.json';path.write_text(json.dumps(package))
            code,report=self.cli('validate','--input',str(path),'--package-root',str(base))
            self.assertEqual(3,code);self.assertEqual([],report['errors'])
            self.assertEqual(0,report['resource_closure']['resource_count'])
            self.assertTrue(report['diagnostic_groups']['missing_material'])

    def test_relative_location_rejects_escape_protocol_and_encoding(self):
        for value in ('../../outside.bpmn','/tmp/model.bpmn','file:model.bpmn','https://example.invalid/a','//example.invalid/a',r'..\a','%2e%2e/a','%252e%252e/a','a%2fb','a?b','a#b','a\x00b'):
            with self.subTest(value=value),self.assertRaises(Invalid):imports.relative_location('nested/main.bpmn',value)

    def test_directory_locations_cannot_alias_embedded_files(self):
        for value in ('model.bpmn/','model.bpmn/.','.','..','shared/..'):
            with self.subTest(value=value),self.assertRaisesRegex(Invalid,'directory rather than a document'):
                imports.relative_location('nested/main.bpmn',value)

    def test_file_directory_conflicts_reject_before_decode_read_or_destination_creation(self):
        rows=[record('main.bpmn/child.bpmn',CHILD)]
        with patch.object(base64,'b64decode',side_effect=AssertionError('decode')):
            with self.assertRaisesRegex(Invalid,'file/directory path conflict'):imports.decode_resources(rows,root_document_path='main.bpmn')
            with self.assertRaisesRegex(Invalid,'file/directory path conflict'):imports.decode_resources([record('folder',CHILD),record('folder/child.bpmn',CHILD)])
        data=ROOT.replace(b'shared/model.bpmn',b'main.bpmn/child.bpmn')
        with tempfile.TemporaryDirectory() as tmp,patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
            report=check_native(data,'bpmn','2.0.2',package_root=Path(tmp))
            self.assertTrue(any('file/directory path conflict' in x for x in report['errors']))
        package=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',CHILD)])
        package['resources']=rows
        with patch.object(Path,'mkdir',side_effect=AssertionError('destination creation')):
            with self.assertRaisesRegex(Invalid,'file/directory path conflict'):imports.materialize_bundle(package,Path('unused-destination'))

    def test_explicit_disk_context_rejects_symbolic_link_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)/'package';base.mkdir()
            outside=Path(tmp)/'outside.bpmn';outside.write_bytes(CHILD)
            (base/'shared').symlink_to(Path(tmp),target_is_directory=True)
            data=ROOT.replace(b'shared/model.bpmn',b'shared/outside.bpmn')
            with patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                report=check_native(data,'bpmn','2.0.2',package_root=base)
                self.assertTrue(any('symbolic link escapes' in x for x in report['errors']))

    def test_symbolic_link_loop_is_classified_without_traceback_or_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);(base/'shared').mkdir();(base/'shared/model.bpmn').symlink_to('model.bpmn')
            with patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                report=check_native(ROOT,'bpmn','2.0.2',package_root=base)
                self.assertTrue(any('cannot be safely resolved' in x for x in report['errors']))
                self.assertEqual('invalid',report['resource_closure']['status'])
                self.assertEqual([],report['diagnostic_groups']['missing_material'])
            source=base/'main.bpmn';source.write_bytes(ROOT)
            code,result=self.cli('import','--input',str(source),'--package-root',str(base),'--out',str(base/'package.json'))
            self.assertEqual(1,code);self.assertEqual('error',result['status'])
            self.assertEqual(ROOT,source.read_bytes());self.assertFalse((base/'package.json').exists())

    def test_symbolic_link_ancestor_loop_is_an_invalid_path_not_missing_material(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);(base/'shared').symlink_to('shared',target_is_directory=True)
            with patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                report=check_native(ROOT,'bpmn','2.0.2',package_root=base)
            self.assertTrue(any('cannot be safely resolved' in x for x in report['errors']))
            self.assertEqual('invalid',report['resource_closure']['status'])
            self.assertEqual([],report['diagnostic_groups']['missing_material'])

    def test_missing_disk_resource_remains_a_material_gap_after_path_resolution(self):
        for kind in ('missing-parent','missing-file','dangling-in-package-link'):
            with self.subTest(kind=kind),tempfile.TemporaryDirectory() as tmp:
                base=Path(tmp)
                if kind!='missing-parent':(base/'shared').mkdir()
                if kind=='dangling-in-package-link':(base/'shared/model.bpmn').symlink_to('absent.bpmn')
                with patch.object(imports,'_read_resource_bytes',side_effect=AssertionError('read')):
                    report=check_native(ROOT,'bpmn','2.0.2',package_root=base)
                self.assertEqual([],report['errors'])
                self.assertEqual('incomplete',report['resource_closure']['status'])
                self.assertEqual('missing-material',report['resource_closure']['imports'][0]['status'])
                self.assertIn('BPMN imported resource missing: shared/model.bpmn declared by main.bpmn',report['diagnostic_groups']['missing_material'])

    def test_vendor_href_is_never_read_and_move_keeps_identical_material_diagnostics(self):
        from standards import safe_xml
        data=document('<process id="P"><extensionElements><v:note xmlns:v="urn:vendor" href="private.xml#Secret"/></extensionElements></process>')
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);private=base/'private.xml';private.write_bytes(b'<secret id="Secret"/>')
            original=safe_xml
            def guarded(value):
                if value==private.read_bytes():raise AssertionError('private href was read')
                return original(value)
            with patch('standards.safe_xml',side_effect=guarded):
                raw=check_native(data,'bpmn','2.0.2',package_root=base)
                package=make_package(data,'bpmn','2.0.2',package_root=base)
            embedded=check_native(package_bytes(package,'bpmn','2.0.2'),'bpmn','2.0.2',resources=package.get('resources',[]),document_path=package.get('document_path'))
            self.assertEqual([],raw['errors']);self.assertEqual([],embedded['errors'])
            self.assertEqual(raw['diagnostic_groups'],embedded['diagnostic_groups'])
            self.assertEqual([],raw['diagnostic_groups']['missing_material'])
            self.assertTrue(any('never read' in x for x in raw['blockers']))

    def test_cycles_are_finite_and_each_file_is_materialized_once(self):
        child=document(imported('../main.bpmn','urn:root')+'<process id="P"/>','urn:shared')
        package=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',child)])
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'bundle';result=imports.materialize_bundle(package,out)
            self.assertEqual({'main.bpmn','shared/model.bpmn'},set(result['outputs']))
            self.assertEqual(2,result['resource_closure']['document_count'])
            self.assertEqual(ROOT,(out/'main.bpmn').read_bytes())
            self.assertEqual(child,(out/'shared/model.bpmn').read_bytes())

    def test_resource_preflight_rejects_counts_and_total_before_decode(self):
        row=record('x.bpmn',b'12345678')
        with patch.object(base64,'b64decode',side_effect=AssertionError('allocated')):
            with self.assertRaises(Invalid):imports.decode_resources([row]*64)
            with patch.object(imports,'MAX_TOTAL_BYTES',10),self.assertRaises(Invalid):imports.decode_resources([row],root_size=3)

    def test_graph_depth_is_checked_before_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);(base/'shared').mkdir()
            middle=document(imported('next.bpmn')+'<process id="P"/>','urn:shared')
            (base/'shared/model.bpmn').write_bytes(middle)
            (base/'shared/next.bpmn').write_bytes(CHILD)
            original=imports._read_resource_bytes
            with patch.object(imports,'MAX_DEPTH',1),patch.object(imports,'_read_resource_bytes',wraps=original) as reads:
                report=check_native(ROOT,'bpmn','2.0.2',package_root=base)
                self.assertEqual(1,reads.call_count)
                self.assertTrue(any('depth/document budget' in x for x in report['errors']))

    def test_resources_reject_duplicate_path_main_collision_tamper_and_extra(self):
        row=record('shared/model.bpmn',CHILD)
        for rows in ([row,row],[record('main.bpmn',CHILD)],[{**row,'sha256':'0'*64}]):
            with self.subTest(rows=rows),self.assertRaises(Invalid):self.check(rows=rows)
        report=self.check(rows=[row,record('unreachable.bpmn',CHILD)])
        self.assertTrue(any('outside the explicit' in x for x in report['errors']))

    def test_native_package_root_resource_bytes_and_coordinates_are_preserved(self):
        child=CHILD.replace(b'</definitions>',b'<bpmndi:BPMNDiagram xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" id="D"><bpmndi:BPMNPlane id="Plane" bpmnElement="P"/></bpmndi:BPMNDiagram></definitions>')
        package=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',child)])
        self.assertEqual(ROOT,package_bytes(package,'bpmn','2.0.2'))
        self.assertEqual(child,imports.decode_resources(package['resources'])['shared/model.bpmn'])
        legacy=make_package(document('<process id="P"/>'),'bpmn','2.0.2')
        self.assertNotIn('resources',legacy)
        self.assertNotIn('document_path',legacy)
        self.assertEqual(document('<process id="P"/>'),package_bytes(legacy,'bpmn','2.0.2'))
        stale=copy.deepcopy(package);stale['native_sha256']='0'*64
        with self.assertRaises(Invalid):package_bytes(stale,'bpmn','2.0.2')
        for change in ({'payload_encoding':'xml'},{'resources':None},{'document_path':None}):
            with self.subTest(change=change),self.assertRaises(Invalid):package_bytes({**package,**change},'bpmn','2.0.2')

    def test_materialization_verifies_before_creating_destination(self):
        package=make_package(ROOT,'bpmn','2.0.2',resources=[])
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'new'
            with self.assertRaises(Incomplete):imports.materialize_bundle(package,out)
            self.assertFalse(out.exists())
            valid=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',CHILD)])
            out.mkdir();(out/'old').write_bytes(b'old bytes')
            with self.assertRaises(Invalid):imports.materialize_bundle(valid,out)
            self.assertEqual(b'old bytes',(out/'old').read_bytes())
            self.assertEqual(['old'],[p.name for p in out.iterdir()])

    def cli(self, *args):
        result=subprocess.run([sys.executable,'-B',str(SCRIPTS/'standards.py'),*args,'--language','bpmn','--version','2.0.2'],capture_output=True,text=True,timeout=30)
        return result.returncode,json.loads(result.stdout)

    def test_cli_nested_input_moved_package_export_and_render_refusal(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)/'source';(base/'nested').mkdir(parents=True);(base/'shared').mkdir()
            root=ROOT.replace(b'shared/model.bpmn',b'../shared/model.bpmn')
            (base/'nested/main.bpmn').write_bytes(root);(base/'shared/model.bpmn').write_bytes(CHILD)
            package=Path(tmp)/'moved/package.json';package.parent.mkdir()
            code,result=self.cli('import','--input',str(base/'nested/main.bpmn'),'--package-root',str(base),'--out',str(package))
            self.assertEqual(0,code,result)
            self.assertEqual('nested/main.bpmn',json.loads(package.read_text())['document_path'])
            import shutil;shutil.rmtree(base)
            code,result=self.cli('validate','--input',str(package),'--package-root',str(REPO))
            self.assertEqual(3,code,result);self.assertEqual([],result['errors'])
            out=Path(tmp)/'bundle'
            code,result=self.cli('export','--input',str(package),'--out',str(out),'--materialize')
            self.assertEqual(0,code,result);self.assertEqual(root,(out/'nested/main.bpmn').read_bytes())
            code,result=self.cli('render','--input',str(package),'--out',str(Path(tmp)/'preview.svg'),'--auto-layout')
            self.assertEqual(3,code,result);self.assertIn('remains uncovered',result['reason'])
            self.assertFalse((Path(tmp)/'preview.svg').exists())

    def test_cli_materialization_classifies_missing_and_uncovered_without_traceback(self):
        for data in (ROOT,document(imported('https://example.invalid/model',kind=XSD))):
            with self.subTest(data=data),tempfile.TemporaryDirectory() as tmp:
                base=Path(tmp);package=base/'package.json'
                package.write_text(json.dumps(make_package(data,'bpmn','2.0.2',resources=[])))
                code,result=self.cli('export','--input',str(package),'--out',str(base/'destination'),'--materialize')
                self.assertEqual(3,code,result);self.assertEqual('blocked',result['status'])
                self.assertFalse((base/'destination').exists())


class BPMNResourceEditorTests(unittest.TestCase):
    def native(self, rows=None):
        return {'language':'bpmn','version':'2.0.2','xml':ROOT.decode('utf-8'),
                'resources':rows if rows is not None else [record('shared/model.bpmn',CHILD)],'document_path':'main.bpmn'}

    def test_editor_diagnostics_generation_and_capacity_are_separate(self):
        from workbench.native import normalize,diagnose,generate
        from workbench.server import MAX_BODY
        self.assertEqual(8*1024*1024,MAX_BODY)
        native=normalize(self.native())
        report=diagnose(native)
        self.assertTrue(report['valid']);self.assertFalse(report['conformance_complete'])
        self.assertEqual([],report['missing_material'])
        self.assertTrue(diagnose(normalize(self.native([])))['missing_material'])
        with tempfile.TemporaryDirectory() as tmp,patch('bpmn_render.render_native',side_effect=AssertionError('browser launch')):
            result=generate(native,Path(tmp),render=True,auto_layout=True)
            self.assertEqual('blocked',result['job_status'])
            self.assertEqual(CHILD,(Path(tmp)/'native-resources/shared/model.bpmn').read_bytes())
            package=json.loads((Path(tmp)/'native-package.json').read_text())
            self.assertEqual(ROOT,package_bytes(package,'bpmn','2.0.2'))
        with patch('workbench.native.MAX_EDITOR_BODY',100),patch.object(base64,'b64decode',side_effect=AssertionError('decode')):
            with self.assertRaisesRegex(ValueError,'editor request capacity'):normalize(self.native())

    def test_editor_unpack_preserves_package_integrity_and_refuses_uneditable_bindings(self):
        from workbench.native import unpack_package
        package=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',CHILD)])
        native=unpack_package(package)
        self.assertEqual(ROOT.decode('utf-8'),native['xml'])
        self.assertEqual(package['resources'],native['resources'])
        tampered={**package,'inventory_sha256':'0'*64}
        with self.assertRaises(Invalid):unpack_package(tampered)
        bound={**package,'bindings':[{'namespace':'urn:test','native_id':'A','project_id':'local-A'}]}
        with self.assertRaisesRegex(Incomplete,'bindings are not covered'):unpack_package(bound)
        for bindings in (None,[None],['x'],[{'namespace':5,'native_id':'A','project_id':'P'}],[{'namespace':'urn:test','native_id':[],'project_id':'P'}]):
            with self.subTest(bindings=bindings),self.assertRaises(Invalid):unpack_package({**package,'bindings':bindings})

    def test_http_unpack_uses_shared_integrity_and_returns_explicit_binding_status(self):
        from workbench.server import create_server
        import threading,http.client
        with tempfile.TemporaryDirectory() as tmp:
            server=create_server(port=0,data_dir=Path(tmp)/'data')
            thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
            def request(package):
                conn=http.client.HTTPConnection('127.0.0.1',server.server_port,timeout=20)
                conn.request('POST','/api/native/unpack',body=json.dumps({'package':package}).encode(),headers={'Content-Type':'application/json'})
                response=conn.getresponse();value=json.loads(response.read());status=response.status;conn.close();return status,value
            try:
                package=make_package(ROOT,'bpmn','2.0.2',resources=[record('shared/model.bpmn',CHILD)])
                status,value=request(package);self.assertEqual(200,status,value);self.assertEqual(package['resources'],value['native']['resources'])
                status,value=request({**package,'inventory_sha256':'0'*64});self.assertEqual(400,status,value)
                status,value=request({**package,'bindings':[{'namespace':'urn:test','native_id':'A','project_id':'local-A'}]})
                self.assertEqual(422,status,value);self.assertEqual('native_capability_uncovered',value['error'])
            finally:server.shutdown();thread.join(5);server.server_close();server.app.close()

    def test_editor_immutable_versions_preserve_resources_after_restart(self):
        from workbench.server import create_server
        with tempfile.TemporaryDirectory() as tmp:
            data=Path(tmp)/'data';server=create_server(port=0,data_dir=data)
            try:
                project=server.app.create_project({'name':'导入资源测试','native':self.native()})
                original=project['head_version']
                changed=self.native([record('shared/model.bpmn',CHILD.replace('订单'.encode(),'新版订单'.encode()))])
                after=server.app.save_version(project['id'],{'base_version':original,'model':project['model'],'layout':project['layout'],'message':'资源修订','native':changed})
                self.assertNotEqual(original,after['head_version'])
            finally:server.server_close();server.app.close()
            server=create_server(port=0,data_dir=data)
            try:
                with server.app.db() as db:
                    before=server.app.version(db,project['id'],original)
                    current=server.app.version(db,project['id'],after['head_version'])
                self.assertEqual(record('shared/model.bpmn',CHILD),before['native']['resources'][0])
                self.assertEqual(changed['resources'],current['native']['resources'])
                self.assertEqual('main.bpmn',before['native']['document_path'])
                self.assertEqual(ROOT.decode(),before['native']['xml'])
            finally:server.server_close();server.app.close()


if __name__=='__main__':unittest.main()
