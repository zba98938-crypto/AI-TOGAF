"""Regression tests for F02/F04; fixtures are independent of historical outputs."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'togaf-standard-10th-ai/skills' / '_shared' / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from analyze import evaluate
from strict_json import loads, dumps
from validate import validate

EVIDENCE = ['test-source']


def fixtures():
    return {
        'risk-explicit-rule': dict(formula='likelihood-times-impact', rule_evidence=EVIDENCE,
            likelihood=dict(value=2, scale='adopted-0-5', evidence=EVIDENCE),
            impact=dict(value=4, scale='adopted-0-5', evidence=EVIDENCE)),
        'weighted-normalized-decision': dict(rule_evidence=EVIDENCE,
            criteria=[dict(id='cost', weight=1, min=0, max=100, direction='minimize')],
            options=[dict(id='A', scores=dict(cost=20)), dict(id='B', scores=dict(cost=80))]),
        'preference-weighted-decision': dict(rule_evidence=EVIDENCE,
            criteria=[dict(id='cost', weight=2), dict(id='benefit', weight=1)],
            options=[dict(id='A', scores=dict(cost=5, benefit=2)),
                     dict(id='B', scores=dict(cost=2, benefit=5))]),
        'maturity-weighted': dict(rule_evidence=EVIDENCE, scale=dict(min=0, max=5),
            factors=[dict(id='A', value=1, weight=1, evidence=EVIDENCE, achieved_levels=[1]),
                     dict(id='B', value=4, weight=3, evidence=EVIDENCE, achieved_levels=[1,2,3,4])],
            levels=[1,2,3,4,5]),
        'environmental-delta': dict(boundary='same year and service', method_evidence=EVIDENCE,
            rows=[dict(id='emissions', added=69, retired=460, reported_net=-391,
                       unit='kgCO2e', scope='Scope 3', period='2026', evidence=EVIDENCE)]),
        'lean-serial-flow': dict(boundary='serial process', rule_evidence=EVIDENCE,
            aggregation_rule='serial-conditional-first-pass', working_hours_per_day=8,
            steps=[dict(id='step', evidence=EVIDENCE, lead_time=dict(value=1,unit='working-day'),
                        process_time=dict(value=1,unit='hour'), complete_accurate_percent=90)]),
        'dependency-topological-order': dict(rule_evidence=EVIDENCE,
            work_packages=[dict(id='A',evidence=EVIDENCE),dict(id='B',evidence=EVIDENCE)],
            dependencies=[dict(source='A',target='B',kind='hard',evidence=EVIDENCE)]),
        'work-package-prioritization': dict(rule_evidence=EVIDENCE,
            criteria=[dict(id='value',weight=1,min=1,max=5,higher_is_better=True,
                           weight_evidence=EVIDENCE,scale_evidence=EVIDENCE)],
            work_packages=[dict(id='A',scores=dict(value=5),score_evidence=dict(value=EVIDENCE)),
                           dict(id='B',scores=dict(value=1),score_evidence=dict(value=EVIDENCE))],
            sensitivity=dict(evidence=EVIDENCE,relative_weight_delta=.1)),
    }


def analysis(method, inputs):
    return dict(id='test-analysis', method_id=method, inputs=inputs)


def model_with(record):
    context=dict(domains=['business'],landscape='segment',purpose='project',abstraction='logical',evolution='target')
    return dict(schema_version='2.0',project=dict(id='numeric-test',name='Synthetic numeric regression',
        version='1',context=context,is_example=True,approval_status='candidate',implementation_status='not-started'),
        sources=[dict(id='test-source',kind='example',description='Synthetic project rule')],
        entities=[],relationships=[],views=[],deliverables=[],gaps=[],analyses=[record])


def set_path(record, path, value):
    for key in path[:-1]:record=record[key]
    record[path[-1]]=value


def public_examples():
    """Current executable methods plus authored inputs for standalone routes."""
    from method_fixtures import direct_cases
    caps=json.loads((SCRIPTS.parent/'capabilities.json').read_text())
    records={}
    for profile in caps['profiles']:
        for record in profile.get('example',{}).get('analyses',[]):
            records.setdefault(record['method_id'],copy.deepcopy(record['inputs']))
    for case in direct_cases():
        if not case['reject']:
            records.setdefault(case['method_id'],copy.deepcopy(case['inputs']))
    registered={m.get('calculator_id') or m.get('calculator') for m in caps['analysis_methods']}-{None}
    return records,registered|{'weighted-normalized-decision','environmental-delta','lean-serial-flow'}


class NumericContracts(unittest.TestCase):
    def result(self, method, inputs=None):
        return evaluate(analysis(method, inputs if inputs is not None else fixtures()[method]))['result']

    def test_valid_results_and_boundaries_preserved(self):
        self.assertEqual(self.result('risk-explicit-rule')['inherent_risk'],8)
        self.assertEqual(self.result('preference-weighted-decision')['ranking'],['A','B'])
        self.assertEqual(self.result('preference-weighted-decision')['results'][0]['weighted_sum'],12)
        self.assertAlmostEqual(self.result('weighted-normalized-decision')['results'][0]['score'],.8)
        self.assertEqual(self.result('maturity-weighted')['weighted_level'],3.25)
        self.assertEqual(self.result('maturity-weighted')['level_attainment_percent']['1'],100)
        self.assertEqual(self.result('environmental-delta')['rows'][0]['calculated_net'],-391)
        self.assertEqual(self.result('lean-serial-flow')['total_lead_time_minutes'],480)
        self.assertEqual(self.result('dependency-topological-order')['batches'],[['A'],['B']])
        self.assertEqual(self.result('work-package-prioritization')['scores'],dict(A=1,B=0))
        pref=fixtures()['preference-weighted-decision']
        for criterion in pref['criteria']:criterion.pop('weight')
        self.assertEqual(self.result('preference-weighted-decision',pref)['ranking'],['A','B'])
        risk=fixtures()['risk-explicit-rule'];risk['likelihood']['value']=0
        self.assertEqual(self.result('risk-explicit-rule',risk)['inherent_risk'],0)

    def test_every_arithmetic_input_rejects_non_numbers_and_nonfinite(self):
        paths={
            'risk-explicit-rule':[('likelihood','value'),('impact','value')],
            'weighted-normalized-decision':[('criteria',0,'weight'),('criteria',0,'min'),('criteria',0,'max'),('options',0,'scores','cost')],
            'preference-weighted-decision':[('criteria',0,'weight'),('options',0,'scores','cost')],
            'maturity-weighted':[('scale','min'),('scale','max'),('factors',0,'weight'),('factors',0,'value'),('levels',0),('factors',0,'achieved_levels',0)],
            'environmental-delta':[('rows',0,'added'),('rows',0,'retired'),('rows',0,'reported_net')],
            'lean-serial-flow':[('working_hours_per_day',),('steps',0,'lead_time','value'),('steps',0,'process_time','value'),('steps',0,'complete_accurate_percent')],
            'work-package-prioritization':[('criteria',0,'weight'),('criteria',0,'min'),('criteria',0,'max'),('work_packages',0,'scores','value'),('sensitivity','relative_weight_delta')],
        }
        for method, fields in paths.items():
            for path in fields:
                for bad in [True,False,float('nan'),float('inf'),-float('inf'),'2',None]:
                    with self.subTest(method=method,path=path,value=repr(bad)):
                        value=fixtures()[method];set_path(value,path,bad)
                        with self.assertRaises(ValueError):self.result(method,value)

    def test_local_id_domains_reject_blanks_duplicates_and_non_strings(self):
        cases={'weighted-normalized-decision':['criteria','options'],
               'preference-weighted-decision':['criteria','options'],
               'maturity-weighted':['factors'],'lean-serial-flow':['steps'],
               'dependency-topological-order':['work_packages'],
               'work-package-prioritization':['criteria','work_packages']}
        for method, collections in cases.items():
            for collection in collections:
                for bad in ['', '  ', None, True, 12]:
                    with self.subTest(method=method,collection=collection,bad=bad):
                        value=fixtures()[method];value[collection][0]['id']=bad
                        with self.assertRaises(ValueError):self.result(method,value)
                value=fixtures()[method];value[collection].append(copy.deepcopy(value[collection][0]))
                with self.subTest(method=method,collection=collection,duplicate=True):
                    with self.assertRaises(ValueError):self.result(method,value)
        value=fixtures()['weighted-normalized-decision'];value['options'][1]=dict(id='A',eligible=False,reason='fails declared hard constraint')
        with self.assertRaises(ValueError):self.result('weighted-normalized-decision',value)

    def test_identity_domains_and_boolean_flags_remain_valid(self):
        value=fixtures()['weighted-normalized-decision'];value['options'][0]['id']='cost'
        value['options'][1]=dict(id='B',eligible=False,reason='hard constraint')
        result=self.result('weighted-normalized-decision',value)
        self.assertEqual(result['ranking'],['cost'])
        self.assertFalse(result['results'][1]['eligible'])

    def test_finite_inputs_cannot_produce_nonfinite_results(self):
        cases=[('risk-explicit-rule',('likelihood','value'),1e308),
               ('preference-weighted-decision',('criteria',0,'weight'),1e308),
               ('maturity-weighted',('factors',1,'weight'),1e308),
               ('lean-serial-flow',('steps',0,'lead_time','value'),1e308)]
        for method,path,value in cases:
            with self.subTest(method=method):
                data=fixtures()[method];set_path(data,path,value)
                with self.assertRaises(ValueError):self.result(method,data)
        data=fixtures()['weighted-normalized-decision'];data['criteria'][0].update(min=-1e308,max=1e308)
        with self.assertRaises(ValueError):self.result('weighted-normalized-decision',data)
        data=fixtures()['environmental-delta'];data['rows'][0].update(added=1e308,retired=-1e308)
        with self.assertRaises(ValueError):self.result('environmental-delta',data)
        data=fixtures()['work-package-prioritization'];data['criteria'][0].update(min=-1e308,max=1e308)
        with self.assertRaises(ValueError):self.result('work-package-prioritization',data)

    def test_existing_weight_and_range_rejections_remain(self):
        for method in ['weighted-normalized-decision','preference-weighted-decision','maturity-weighted']:
            collection='factors' if method=='maturity-weighted' else 'criteria'
            for weight in [0,-1]:
                with self.subTest(method=method,weight=weight):
                    data=fixtures()[method]
                    for row in data[collection]:row['weight']=weight
                    with self.assertRaises(ValueError):self.result(method,data)
        data=fixtures()['weighted-normalized-decision'];data['criteria'][0]['max']=0
        with self.assertRaises(ValueError):self.result('weighted-normalized-decision',data)
        data=fixtures()['risk-explicit-rule'];data['likelihood']['value']=-1
        with self.assertRaises(ValueError):self.result('risk-explicit-rule',data)

    def test_nested_identity_helpers_and_iterative_option_identity(self):
        from evidence_analysis import unique
        for bad in ['', '   ', None, True]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):unique([dict(id=bad)],'TEST','records')
        data=dict(constraint_review=dict(evidence_refs=EVIDENCE), constraints=[],iterations=[
            dict(option_id='A',iteration=1,subsystem='service',goal='goal',hypothesis='candidate',
                 evidence_refs=EVIDENCE,decision_owner='owner',assessment='assessed',status='retain'),
            dict(option_id='A',iteration=2,subsystem='service',goal='goal',hypothesis='candidate',
                 evidence_refs=EVIDENCE,decision_owner='owner',assessment='assessed',status='selected')])
        self.assertEqual(self.result('set-based-options-review',data)['selected_ids'],['A'])
        # Reusing an option ID across iterations is intentional; its compound key is unique.
        invalid=copy.deepcopy(data);invalid['iterations'].append(copy.deepcopy(data['iterations'][0]))
        with self.assertRaises(ValueError):self.result('set-based-options-review',invalid)
        invalid=copy.deepcopy(data);invalid['constraints']=[dict(id='C'),dict(id='C')]
        with self.assertRaises(ValueError):self.result('set-based-options-review',invalid)
        invalid=copy.deepcopy(data);invalid['iterations'][0]['option_id']='  '
        with self.assertRaises(ValueError):self.result('set-based-options-review',invalid)

    def test_all_dispatches_have_input_and_output_finiteness_guard(self):
        from unittest.mock import patch
        # A non-arithmetic review must also reject hidden nonfinite metadata.
        with self.assertRaises(ValueError):
            self.result('smart-objective-review',dict(hidden=float('inf')))
        with patch('analyze.risk_assessment',return_value=dict(nested=[dict(value=float('inf'))])):
            with self.assertRaises(ValueError):self.result('risk-explicit-rule')

    def test_every_public_route_accepts_its_example_and_rejects_nonfinite_metadata(self):
        examples,expected=public_examples()
        self.assertEqual(set(examples),expected)
        for method,inputs in examples.items():
            with self.subTest(method=method,valid=True):
                result=self.result(method,copy.deepcopy(inputs))
                # Serialization is a second independent boundary for returned numbers.
                dumps(result)
            for bad in [float('nan'),float('inf'),-float('inf')]:
                with self.subTest(method=method,bad=repr(bad)):
                    data=copy.deepcopy(inputs);data['extra_metadata']={'measure':bad}
                    with self.assertRaisesRegex(ValueError,'non-finite-number'):
                        self.result(method,data)

    def test_remaining_quantity_fields_and_project_tolerances(self):
        examples,_=public_examples()
        paths={
            'environmental-annual-accounting':[
                ('boundary','comparison_horizon_years'),('offsets','provider','value')],
            'project-management-strategy-review':[('topics',3,'delegated_tolerances',0,'value')],
            'project-highlight-review':[('schedule_tolerance','value')],
            'transition-operability-check':[
                ('rollback','trigger','threshold'),('rollback','trigger','consecutive_periods')],
            'benefit-realization-trigger':[
                ('baseline','value'),('target','value'),('observed','value'),('trigger','adverse_deviation_percent')],
        }
        for method,fields in paths.items():
            for path in fields:
                for bad in [True,False,float('nan'),float('inf'),'2']:
                    with self.subTest(method=method,path=path,bad=repr(bad)):
                        data=copy.deepcopy(examples[method]);set_path(data,path,bad)
                        with self.assertRaises(ValueError):self.result(method,data)

    def test_delegated_tolerance_ids_are_unique_in_each_topic(self):
        examples,_=public_examples()
        for invalid in ['duplicate','','  ',True]:
            data=copy.deepcopy(examples['project-management-strategy-review'])
            controls=next(x for x in data['topics'] if x['topic']=='project-controls')
            if invalid=='duplicate':controls['delegated_tolerances'].append(copy.deepcopy(controls['delegated_tolerances'][0]))
            else:controls['delegated_tolerances'][0]['id']=invalid
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):self.result('project-management-strategy-review',data)

    def test_malformed_input_shapes_and_transition_identity_are_value_errors(self):
        for malformed in [None,[],True,'analysis']:
            with self.subTest(analysis=malformed):
                with self.assertRaises(ValueError):evaluate(malformed)
        data=fixtures()['risk-explicit-rule'];data['likelihood']=[]
        with self.assertRaises(ValueError):
            self.result('risk-explicit-rule',data)
        data=fixtures()['weighted-normalized-decision'];data['options'][0]['scores']=[]
        with self.assertRaisesRegex(ValueError,'invalid-input:weighted-normalized-decision'):
            self.result('weighted-normalized-decision',data)
        examples,_=public_examples()
        for invalid in [' ',True,12]:
            data=copy.deepcopy(examples['change-profile-checklist']);data['transition_id']=invalid
            with self.subTest(transition_id=invalid):
                with self.assertRaises(ValueError):self.result('change-profile-checklist',data)

    def test_strict_json_rejects_constants_exponent_overflow_and_bad_output(self):
        for token in ['NaN','Infinity','-Infinity','1e999','-1e999']:
            with self.subTest(token=token):
                with self.assertRaises(ValueError):loads('{"value":'+token+'}')
        for value in [float('nan'),float('inf'),-float('inf')]:
            with self.assertRaises(ValueError):dumps(dict(value=value))
        self.assertEqual(loads('{"flag":true,"value":1.5}'),dict(flag=True,value=1.5))
        self.assertTrue(any(i['code']=='non-finite-number' for i in validate(dict(hidden=float('nan')))))

    def run_cli(self, script, model, extra):
        return subprocess.run([sys.executable,str(SCRIPTS/script),str(model)]+extra,
            cwd=str(model.parent),capture_output=True,text=True,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))

    def test_public_analyze_valid_and_numeric_id_rejections(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'model.json'
            for method in ['risk-explicit-rule','preference-weighted-decision']:
                data=fixtures()[method];path.write_text(json.dumps(model_with(analysis(method,data))))
                result=self.run_cli('analyze.py',path,['--evaluate','test-analysis'])
                self.assertEqual(result.returncode,0,result.stderr)
                if method=='risk-explicit-rule':data['likelihood']['value']=True
                else:data['options'][1]['id']='A'
                path.write_text(json.dumps(model_with(analysis(method,data))))
                result=self.run_cli('analyze.py',path,['--evaluate','test-analysis'])
                self.assertEqual(result.returncode,2,result.stdout+result.stderr)
                self.assertNotIn('Traceback',result.stderr)
            data=fixtures()['risk-explicit-rule'];data['likelihood']=[]
            path.write_text(json.dumps(model_with(analysis('risk-explicit-rule',data))))
            result=self.run_cli('analyze.py',path,['--evaluate','test-analysis'])
            self.assertEqual(result.returncode,2,result.stdout+result.stderr)
            self.assertIn('likelihood',result.stderr)
            self.assertNotIn('Traceback',result.stderr)

    def test_public_model_loaders_reject_nonstandard_json_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'model.json'
            for token in ['NaN','Infinity','-Infinity','1e999']:
                for script,args,code in [('analyze.py',['--evaluate','test-analysis'],2),
                    ('validate.py',[],1),('generate.py',['--all','--out',str(Path(tmp)/'out')],1),
                    ('requirements_trace.py',[],1)]:
                    with self.subTest(script=script,token=token):
                        path.write_text('{"invalid":'+token+'}')
                        result=self.run_cli(script,path,args)
                        self.assertEqual(result.returncode,code,result.stdout+result.stderr)
                        self.assertNotIn('Traceback',result.stderr)

    def test_lifecycle_loaders_share_strict_json_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'model.json';path.write_text('{"invalid":1e999}')
            commands=[['adm.py','init','--model',str(path),'--id','cycle','--scope','test','--out',str(Path(tmp)/'cycle.json')],
                      ['architecture_delivery.py','init','--model',str(path),'--cycle',str(path),'--out',str(Path(tmp)/'plan.json')]]
            for script,*args in commands:
                with self.subTest(script=script):
                    result=subprocess.run([sys.executable,str(SCRIPTS/script)]+args,cwd=tmp,capture_output=True,text=True,
                                          env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
                    self.assertEqual(result.returncode,1,result.stdout+result.stderr)
                    self.assertNotIn('Traceback',result.stderr)
            self.assertFalse((Path(tmp)/'cycle.json').exists())
            self.assertFalse((Path(tmp)/'plan.json').exists())


if __name__ == '__main__':
    unittest.main()
