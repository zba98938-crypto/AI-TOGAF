"""Classify only the new optional operation-case input; preserve CLI compatibility."""
import contextlib,io,json,os,subprocess,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
REPO=Path(__file__).resolve().parents[1];sys.path.insert(0,str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'))
import uml_backend

class OperationCasesCliTests(unittest.TestCase):
    def invoke(self,case_bytes,expected,missing_model=False,missing_case=False,existing_output=True,source_missing=False):
        with tempfile.TemporaryDirectory(prefix='operation-cli-') as tmp:
            folder=Path(tmp);model=folder/'model.uml';cases=folder/'cases.json';out=folder/'existing-output.json'
            if not missing_model:model.write_text('<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:id="M"/>')
            if not missing_case:cases.write_bytes(case_bytes)
            if existing_output:out.write_bytes(b'previous-output-bytes\n')
            stdout=io.StringIO();argv=['uml_backend.py','--input',str(model),'--out',str(out),'--operation-cases',str(cases)]
            with patch.object(sys,'argv',argv),patch.object(uml_backend.subprocess,'run',side_effect=AssertionError('Java must not start')) as native,contextlib.redirect_stdout(stdout):
                if source_missing:
                    with patch.object(uml_backend,'multiplicity_case_records',side_effect=FileNotFoundError('pinned UML source missing')):code=uml_backend.main()
                else:code=uml_backend.main()
            self.assertEqual(3,code);self.assertEqual(0,native.call_count)
            row=json.loads(stdout.getvalue());self.assertEqual(expected,row['failure_category']);self.assertEqual('invalid' if expected=='validation-error' else 'incomplete',row['conformance_status'])
            if existing_output:self.assertEqual(b'previous-output-bytes\n',out.read_bytes())
            else:self.assertFalse(out.exists())
    def test_malformed_json_utf8_and_wrong_containers_are_validation_errors(self):
        for body in [b'{',b'\xff',b'{}',b'null',b'"list"',b'[null]']:
            with self.subTest(body=body):self.invoke(body,'validation-error')
        from uml_ocl_obligations import multiplicity_execution_catalog
        identity=multiplicity_execution_catalog()['operations'][0]['source_identity']['key']
        for fields in [{'result_probe':{}},{'arguments':[{'kind':[],'value':0}]}]:
            case={'id':'malformed-field','self':'M','obligation':identity,**fields}
            with self.subTest(fields=fields):self.invoke(json.dumps([case]).encode(),'validation-error')
    def test_missing_case_file_model_and_pinned_source_are_material_missing(self):
        self.invoke(b'[]','material-missing',missing_case=True)
        self.invoke(b'[]','material-missing',missing_model=True)
        self.invoke(b'[]','material-missing',source_missing=True)
    def test_unsupported_exact_obligation_is_capability_uncovered(self):
        self.invoke(json.dumps([{'id':'case','self':'M','obligation':'unsupported-exact-identity'}]).encode(),'capability-uncovered')
    def test_existing_output_is_preserved_before_starting_java(self):self.invoke(b'[]','validation-error')
    def test_failed_new_input_does_not_create_an_output(self):self.invoke(b'{','validation-error',existing_output=False)
    def test_existing_invalid_and_incomplete_api_types_remain_compatible(self):
        from standards import Invalid,Incomplete
        with self.assertRaises(Invalid):uml_backend.multiplicity_case_records({})
        with self.assertRaises(Incomplete):uml_backend.multiplicity_case_records([{'id':'x','self':'M','obligation':'unsupported'}])
    def test_legacy_cli_error_text_and_success_summary_are_preserved(self):
        from standards import Invalid
        with tempfile.TemporaryDirectory(prefix='operation-cli-legacy-') as folder:
            folder=Path(folder);model=folder/'input.uml';model.write_bytes(b'input');out=folder/'report.json';stdout=io.StringIO()
            report={'loaded_objects':1,'ocl_parsed':2,'ocl_unmapped':3,'ocl_evaluations':4,'conformance_status':'incomplete','existing_optional_field':'preserved'}
            with patch.object(sys,'argv',['uml_backend.py','--input',str(model),'--out',str(out)]),patch.object(uml_backend,'validate_mapped',return_value=report) as validate,contextlib.redirect_stdout(stdout):self.assertEqual(3,uml_backend.main())
            validate.assert_called_once_with(b'input',None,None);self.assertEqual(report,json.loads(out.read_text()));self.assertEqual({k:report[k] for k in ('loaded_objects','ocl_parsed','ocl_unmapped','ocl_evaluations','conformance_status')},json.loads(stdout.getvalue()))
            stdout=io.StringIO()
            with patch.object(sys,'argv',['uml_backend.py','--input',str(model),'--out',str(folder/'error.json')]),patch.object(uml_backend,'validate_mapped',side_effect=Invalid('legacy error')),contextlib.redirect_stdout(stdout):self.assertEqual(3,uml_backend.main())
            self.assertEqual('legacy error\n',stdout.getvalue())

NATIVE=bool(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME',''))/'bin/java').is_file())
@unittest.skipUnless(NATIVE,'set existing JAVA_HOME for actual new CLI success')
class ActualOperationCasesCliTests(unittest.TestCase):
    def test_valid_new_file_still_executes_java_and_returns_incomplete_exit_three(self):
        with tempfile.TemporaryDirectory(prefix='operation-cli-native-') as folder:
            folder=Path(folder);model=folder/'model.uml';model.write_text('<uml:Model xmlns:uml="http://www.omg.org/spec/UML/20131001" xmlns:xmi="http://www.omg.org/spec/XMI/20131001" xmi:id="M"/>');cases=folder/'cases.json';cases.write_text('[]');output=folder/'report.json'
            run=subprocess.run([sys.executable,str(uml_backend.ROOT/'scripts/uml_backend.py'),'--input',str(model),'--operation-cases',str(cases),'--out',str(output)],capture_output=True,text=True,timeout=120)
            self.assertEqual(3,run.returncode,run.stderr);self.assertEqual('',run.stderr);report=json.loads(output.read_text());summary=json.loads(run.stdout)
            self.assertEqual('incomplete',summary['conformance_status']);self.assertEqual(0,report['native_process']['exit_code']);self.assertEqual(0,report['operation_derived_capability']['requested_case_count'])

if __name__=='__main__':unittest.main()
