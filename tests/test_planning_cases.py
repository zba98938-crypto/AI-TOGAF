"""Business changes and missing facts must survive actual six-profile outputs."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from planning_case_examples import PROFILE_IDS,ASSIGNMENT,example,install
from registry import load
from enterprise.planning_cases import run_profile_cases,verify_output


class PlanningBusinessCasesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory(prefix='six-planning-oracles-')
        cls.directory=Path(cls.temp.name)
        cls.results={pid:run_profile_cases(pid,cls.directory/pid) for pid in PROFILE_IDS}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_all_eighteen_scenarios_generate_and_pass_raw_business_oracles(self):
        self.assertEqual(18,sum(len(v['rows']) for v in self.results.values()))
        self.assertTrue(all(v['status']=='pass' for v in self.results.values()))
        for result in self.results.values():
            missing=next(r for r in result['rows'] if r['variant']=='missing')
            self.assertNotEqual('candidate-only',missing['business_readiness'])
            self.assertFalse(missing['independent_business_acceptance'])

    def test_builder_preserves_six_examples_and_unrelated_source_registration(self):
        profiles=load()[2]
        for pid in PROFILE_IDS:self.assertEqual(profiles[pid]['example'],example(pid))
        caps={'profiles':[copy.deepcopy(profiles[p]) for p in PROFILE_IDS], 'figure_profiles':[{'id':'protected-source','status':'unchanged'}]}
        first=copy.deepcopy(install(caps));self.assertEqual(first,install(caps))
        self.assertEqual([{'id':'protected-source','status':'unchanged'}],caps['figure_profiles'])

    def evidence(self,pid,variant):
        p=self.directory/pid/variant
        m=json.loads((p/'model.json').read_text());raw=json.loads((p/'raw-business-material.json').read_text())
        manifest=json.loads((p/'generated/manifest.json').read_text());entry=next(e for e in manifest['artifacts'] if e['profile_id']==pid)
        payload=json.loads((p/'generated'/entry['json']).read_text())
        text=(p/'generated'/entry['path']).read_text();issues=json.loads((p/'validation.json').read_text())
        analysis=json.loads((p/'analysis.json').read_text()) if (p/'analysis.json').exists() else None
        return raw,m,payload,text,issues,analysis

    def test_unknown_score_cannot_be_replaced_with_zero(self):
        pid='c220-business-value-risk-matrix';data=list(self.evidence(pid,'missing'))
        data[2]['entities'][0]['attributes']['value_index']=0
        with self.assertRaisesRegex(AssertionError,'index not recomputed'):verify_output(pid,*data)

    def test_changed_score_cannot_reuse_old_output(self):
        pid='c220-business-value-risk-matrix';data=list(self.evidence(pid,'change'))
        data[2]['entities'][0]['attributes']['value_index']=4.1
        with self.assertRaisesRegex(AssertionError,'index not recomputed'):verify_output(pid,*data)

    def test_new_cross_domain_dependency_cannot_disappear(self):
        pid='c220-consolidated-gaps-solutions-dependencies-matrix';data=list(self.evidence(pid,'change'))
        data[2]['entities'][0]['attributes']['dependency_refs'].remove('WP-AUDIT')
        with self.assertRaisesRegex(AssertionError,'dependency changed'):verify_output(pid,*data)

    def test_increment_direction_is_semantic(self):
        pid='c220-architecture-definition-increments-table';data=list(self.evidence(pid,'change'))
        edge=data[2]['relationships'][0];edge['source'],edge['target']=edge['target'],edge['source']
        with self.assertRaisesRegex(AssertionError,'direction differs'):verify_output(pid,*data)

    def test_role_workload_increase_cannot_keep_old_capacity_decision(self):
        data=list(self.evidence(ASSIGNMENT,'change'))
        data[5]['assignment_reviews'][0]['capacity_state']='sufficient-for-declared-workload'
        with self.assertRaisesRegex(AssertionError,'capacity disagrees'):verify_output(ASSIGNMENT,*data)


if __name__=='__main__':unittest.main()
