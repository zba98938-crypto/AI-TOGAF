"""Independent OCL truth tables, including OclVoid and invalid sentinel values."""
import base64
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'togaf-standard-10th-ai/skills/_shared/scripts'))
from uml_backend import JARS, ROOT


@unittest.skipUnless(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME', ''))/'bin/java').is_file(),
                     'set existing JAVA_HOME to execute independent OCL truth tables')
class OCLValueSemanticsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The expected four-valued truth table is independent of the backend
        # implementation and has no dependency on generated profile examples.
        values = ('false', 'true', 'null', 'invalid')
        # OCL 2.4 §11.5.4. Rows/columns use values above; these literal
        # matrices are independent of the executable visitor's branching.
        tables = {
            'and': (('false','false','false','false'),
                    ('false','true','null','invalid'),
                    ('false','null','null','invalid'),
                    ('false','invalid','invalid','invalid')),
            'or': (('false','true','null','invalid'),
                   ('true','true','true','true'),
                   ('null','true','null','invalid'),
                   ('invalid','true','invalid','invalid')),
            'xor': (('false','true','null','invalid'),
                    ('true','false','null','invalid'),
                    ('null','null','null','invalid'),
                    ('invalid','invalid','invalid','invalid')),
            'implies': (('true','true','true','true'),
                        ('false','true','null','invalid'),
                        ('null','true','null','invalid'),
                        ('invalid','true','invalid','invalid')),
        }
        cls.expected = {a+' '+op+' '+b: table[i][j]
                        for op, table in tables.items()
                        for i, a in enumerate(values) for j, b in enumerate(values)}
        cls.expected.update({'not '+a: b for a, b in zip(values, ('true','false','null','invalid'))})
        cls.expected.update({
            'true':'true','false':'false','null':'null','invalid':'invalid',
            'null = null':'true','invalid = invalid':'invalid','1':'non-boolean',
            "'not null' = 'not null'":'true',
            "'null and invalid'":'non-boolean',
            'let n : Boolean = null in not n':'null',
            'let n : Boolean = null in n or false':'null',
        })
        with tempfile.TemporaryDirectory(prefix='uml-value-oracle-') as tmp:
            tmp = Path(tmp)
            model = tmp/'probe.uml'
            model.write_bytes(b'<uml:Model xmlns:uml="http://www.eclipse.org/uml2/5.0.0/UML" '
                              b'xmlns:xmi="http://www.omg.org/XMI" xmi:id="M" name="TruthTable"/>')
            rows = [('Model', body, body) for body in cls.expected]
            rules = tmp/'rules.tsv'
            rules.write_text('\n'.join('\t'.join(base64.b64encode(value.encode()).decode()
                                               for value in row) for row in rows)+'\n')
            queries = tmp/'queries.tsv'; queries.write_text('')
            run = subprocess.run([str(Path(os.environ['JAVA_HOME'])/'bin/java'), '-Xmx512m',
                                  '--class-path', str(JARS/'*'), str(ROOT/'scripts/UmlValidate.java'),
                                  str(model), str(rules), str(JARS), str(queries)],
                                 capture_output=True, text=True, timeout=120, check=True)
            cls.report = json.loads(run.stdout)

    def test_each_truth_table_expression_is_actually_evaluated(self):
        self.assertEqual(len(self.expected), len(self.report['ocl_rules']))
        self.assertEqual(len(self.expected), self.report['ocl_parsed'])
        self.assertEqual(0, self.report['ocl_unmapped'])
        self.assertEqual(len(self.expected), self.report['ocl_evaluations'])
        for row in self.report['ocl_rules']:
            with self.subTest(expression=row['id']):
                actual = self.expected[row['id']]
                self.assertEqual(1, row['applicable'])
                self.assertEqual([{'id': 'M', 'value_kind': actual}],
                                 row['evaluation_outcomes'])

    def test_null_invalid_and_false_have_disjoint_counts_and_ids(self):
        fields = {'true': ('true_evaluations', None), 'false': ('violations', 'violation_ids'),
                  'null': ('null_evaluations', 'null_ids'),
                  'invalid': ('invalid_evaluations', 'invalid_ids'),
                  'non-boolean': ('non_boolean_evaluations', 'non_boolean_ids')}
        for row in self.report['ocl_rules']:
            expected = self.expected[row['id']]
            for kind, (counter, ids) in fields.items():
                with self.subTest(expression=row['id'], kind=kind):
                    self.assertEqual(int(expected == kind), row[counter])
                    if ids: self.assertEqual(['M'] if expected == kind else [], row[ids])
            self.assertEqual(row['applicable'], sum(row[counter] for counter, _ in fields.values()))

    def test_truth_table_execution_does_not_claim_full_standard_conformance(self):
        self.assertFalse(self.report['official_full_conformance'])
        adapted = {row['id'] for row in self.report['ocl_rules'] if row['literal_ast_adapter']}
        self.assertEqual({'not null','not invalid'} |
                         {a+' '+op+' '+b for a in ('null','invalid')
                          for b in ('null','invalid') for op in ('and','or','xor','implies')}, adapted)

    def test_adapter_basis_is_pinned_without_full_language_claim(self):
        from uml_backend import boolean_semantics_adapter, OCL_PUBLICATION_SHA256
        adapter = boolean_semantics_adapter()
        self.assertEqual(OCL_PUBLICATION_SHA256, adapter['basis']['sha256'])
        self.assertEqual('11.5.4 Boolean', adapter['basis']['clause'])
        self.assertTrue(adapter['source_body_preserved'])
        self.assertFalse(adapter['official_full_conformance'])



if __name__ == '__main__': unittest.main()
