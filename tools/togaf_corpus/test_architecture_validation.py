#!/usr/bin/env python3
"""Contract regressions for authored evidence identity and original source data."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from validate import Report
from validate_architecture import ArchitectureValidator, validate_relation_history, validate_role_required_fields

ROOT=Path(__file__).resolve().parents[2]
CORPUS=ROOT/'togaf-standard-10th-ai'


def first_record(filename):
    with (CORPUS/'retrieval'/filename).open(encoding='utf-8') as handle:
        return json.loads(next(line for line in handle if line.strip()))


class AtomicJsonWriteTests(unittest.TestCase):
    def test_source_metadata_surrogates_round_trip_without_losing_document(self):
        from build_architecture import write
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'source.json'
            value={'pdf_metadata':{'title':'原文\ud800 / \udfff'},'pages':[{'raw_text':'source text'}]}
            write(path,value)
            self.assertEqual(json.loads(path.read_text(encoding='utf-8')),value)
            self.assertIn(b'\\ud800 / \\udfff',path.read_bytes())

    def test_failed_publish_preserves_previous_json_and_cleans_temporary_file(self):
        from build_architecture import write
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'source.json';path.write_text('{"previous":true}\n')
            before=path.read_bytes()
            with patch('build_architecture.os.replace',side_effect=OSError('simulated publish failure')):
                with self.assertRaises(OSError):write(path,{'replacement':True})
            self.assertEqual(path.read_bytes(),before)
            self.assertEqual(list(Path(folder).iterdir()),[path])


class RetrievalContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=first_record('chunks.jsonl')
        cls.authored=first_record('architecture-chunks.jsonl')

    def check_records(self,source,authored):
        # Only the two retrieval artifacts are varied; the published schema is
        # read as is by the same CLI validator used for the full corpus.
        with tempfile.TemporaryDirectory() as folder:
            corpus=Path(folder);(corpus/'retrieval').mkdir()
            for filename,record in [('chunks.jsonl',source),('architecture-chunks.jsonl',authored)]:
                (corpus/'retrieval'/filename).write_text(json.dumps(record)+'\n',encoding='utf-8')
            validator=ArchitectureValidator.__new__(ArchitectureValidator)
            validator.root=ROOT;validator.corpus=corpus;validator.report=Report()
            validator.retrieval_schemas()
            return validator.report

    def test_real_source_and_authored_records_obey_published_contract(self):
        report=self.check_records(self.source,self.authored)
        self.assertEqual(report.errors,[])
        self.assertEqual(report.counts['source_chunks_schema_checked'],1)
        self.assertEqual(report.counts['architecture_chunks_schema_checked'],1)

    def test_authored_record_cannot_claim_original_text(self):
        changed=deepcopy(self.authored);changed['quality']['original_text']=True
        report=self.check_records(self.source,changed)
        self.assertTrue(any(e['type']=='retrieval-schema-invalid' and e['field']=='quality/original_text' for e in report.errors))

    def test_authored_record_cannot_omit_original_pdf_locators(self):
        changed=deepcopy(self.authored);del changed['source_locators']
        report=self.check_records(self.source,changed)
        self.assertTrue(any(e['type']=='retrieval-schema-invalid' and 'source_locators' in e['detail'] for e in report.errors))

    def test_original_source_cannot_lose_its_pdf_page(self):
        changed=deepcopy(self.source);changed['pdf_pages']=[]
        report=self.check_records(changed,self.authored)
        self.assertTrue(any(e['type']=='retrieval-schema-invalid' and e['field']=='pdf_pages' for e in report.errors))

    def test_original_pdf_locator_cannot_have_an_invalid_hash(self):
        changed=deepcopy(self.authored);changed['source_locators'][0]['sha256']='not-a-source-fingerprint'
        report=self.check_records(self.source,changed)
        self.assertTrue(any(e['type']=='retrieval-schema-invalid' and e['field']=='source_locators/0/sha256' for e in report.errors))


class DiagramHistoryTests(unittest.TestCase):
    def setUp(self):
        # Two inherited assertions; one later disproved by inspecting the PDF.
        self.original=[{'from':'a','to':'b','type':'association'},
                       {'from':'b','to':'c','type':'triggering'}]
        self.active=[{'id':'edge1','source_relation_index':0,'source_relation':self.original[0]}]
        self.rejected=[{'id':'edge2','source_relation_index':1,'source_relation':self.original[1],
                        'semantic_state':'rejected-unobserved','rejection_reason_zh':'原图未观察到这条线。'}]

    def check_history(self,active,rejected):
        report=Report();validate_relation_history(self.original,active,rejected,report,'test-figure');return report

    def test_rejection_preserves_source_history(self):
        self.assertEqual(self.check_history(self.active,self.rejected).errors,[])

    def test_silent_deletion_of_disproved_assertion_is_detected(self):
        report=self.check_history(self.active,[])
        self.assertTrue(any(e['type']=='diagram-source-edge-index-loss-or-duplicate' for e in report.errors))

    def test_claim_in_active_and_rejected_is_detected(self):
        report=self.check_history(self.active+self.rejected,self.rejected)
        self.assertTrue(any(e['type']=='diagram-source-edge-index-loss-or-duplicate' for e in report.errors))

    def test_rewritten_historical_payload_is_detected(self):
        rejected=deepcopy(self.rejected);rejected[0]['source_relation']['type']='association'
        report=self.check_history(self.active,rejected)
        self.assertTrue(any(e['type']=='diagram-source-edge-loss' for e in report.errors))

    def test_new_edge_needs_a_new_source_transcription_origin(self):
        extra={'id':'new-edge','source_relation_index':None,'source_relation':None}
        report=self.check_history(self.active+[extra],self.rejected)
        self.assertTrue(any(e['type']=='diagram-additional-edge-origin-missing' for e in report.errors))
        extra.update(origin='newly-transcribed-source-connection',evidence_refs=['current-visual-review'])
        self.assertEqual(self.check_history(self.active+[extra],self.rejected).errors,[])


class RoleOmissionTests(unittest.TestCase):
    def setUp(self):
        self.role=json.loads((CORPUS/'architecture/roles/G234-data-custodian.json').read_text())
        specs=json.loads((ROOT/'tools/togaf_corpus/role-additional-profiles.json').read_text())['profiles']
        self.spec=next(s for s in specs if s['code']=='G234' and s['key']=='data-custodian')

    def check_fields(self,role,spec):
        report=Report();validate_role_required_fields(role,spec,report);return report

    def test_source_omissions_stay_explicit_and_empty(self):
        report=self.check_fields(self.role,self.spec)
        self.assertEqual(report.errors,[])
        self.assertEqual(report.counts['role_fields_explicitly_not_specified_checked'],2)

    def test_missing_field_is_not_an_explicit_source_omission(self):
        changed=deepcopy(self.role);del changed['responsibilities']
        self.assertTrue(self.check_fields(changed,self.spec).errors)

    def test_removed_populated_source_requirement_cannot_be_relabeled_as_unspecified(self):
        changed=deepcopy(self.role)
        spec=deepcopy(self.spec);spec['requirements']=[['source specifies a requirement']]
        self.assertTrue(self.check_fields(changed,spec).errors)

    def test_unreviewed_blank_core_role_is_rejected(self):
        self.assertTrue(self.check_fields(self.role,None).errors)


class RasterSkillLabelsTests(unittest.TestCase):
    def test_g198_all_labels_and_column_order_against_visual_transcription(self):
        # Independently read from the seven original PDF crops, 2026-11-07.
        # The numerical matrix is independently checked by color in the main
        # validator; this catches copied-label or role-column mistakes.
        expected={
            'image-p0016-01':['Leadership','Teamwork','Inter-personal','Oral Communications','Written Communications','Logical Analysis','Stakeholder Management','Risk Management'],
            'image-p0016-02':['Business Case','Business Scenario','Organization','Business Process','Strategic Planning','Budget Management','Visioning','Business Metrics','Business Culture','Legacy Investments','Business Functions'],
            'image-p0017-01':['Business Modeling','Business Process Design','Role Design','Organization Design','Data Design','Application Design','Systems Integration','IT Industry Standards','Services Design','Architecture Principles Design','Architecture Views & Viewpoints Design','Building Block Design','Solutions Modeling','Benefits Analysis','Business Interworking','Systems Behavior','Project Management','Modeling Skills','Enterprise Architecture Tools'],
            'image-p0017-02':['Program Management','Project Management','Managing Business Change','Change Management','Value Management'],
            'image-p0018-01':['IT Application Development Methodologies & Tools','Programming Languages','Brokering Applications','Information Consumer Applications','Information Provider Applications','Storage Management','Networks','Web-based Services','Asset Management','Service Level Agreements','Systems','COTS','Enterprise Continuums','Migration Planning','Management Utilities','Infrastructure','Application Deployment','End-user Support'],
            'image-p0018-02':['Software Engineering','Security','Systems & Network Management','Transaction Processing','Identity Management','User Interface','International Operations','Data Interchange','Data Management','Graphics & Image','Operating System Services','Network & Communications Infrastructure','Compute Infrastructure'],
            'image-p0019-01':['Contract Law','Data Protection Law','Procurement Law','Fraud','Commercial Law'],
        }
        columns=['Architecture Board Member','Architecture Sponsor','Enterprise Architecture Manager','Technology Architect','Data Architect','Application Architect','Business Architect','Program/Project Manager','IT Designer','Solution Architect']
        skills=json.loads((CORPUS/'architecture/roles/skills.json').read_text())['G198']
        actual={name:[] for name in expected}
        for skill in skills['skills']:
            actual[skill['evidence']['image_record_id'].split('/')[1]].append(skill['label_en'])
        self.assertEqual(actual,expected)
        for name,labels in expected.items():
            record=json.loads((CORPUS/'figures/G198'/(name+'.json')).read_text())
            matrix=next(t for t in record['tables'] if t['id'].startswith('skills-matrix'))
            self.assertEqual([r[0] for r in matrix['rows']],labels)
            self.assertEqual(matrix['columns'][1:],columns)


if __name__=='__main__':unittest.main(verbosity=2)
