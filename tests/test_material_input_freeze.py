"""Freeze ignored review inputs without treating a synthetic closure as reviewed."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

REPO=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('material_input_freeze_gate',
    REPO/'togaf-standard-10th-ai/maintenance/stabilization_evidence.py')
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)


class MaterialInputFreezeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name).resolve()
        subprocess.run(['git','init','-q'],cwd=self.root,check=True)
        (self.root/'.gitignore').write_text('output/\nfreeze*.json\n')
        (self.root/'source.py').write_text('retained source\n')
        subprocess.run(['git','add','.gitignore','source.py'],cwd=self.root,check=True)
        subprocess.run(['git','-c','user.name=Local test','-c','user.email=local@example.invalid',
                        'commit','-qm','fixture'],cwd=self.root,check=True)
        output=self.root/'output';output.mkdir()
        (output/'input-manifest.json').write_text('{"fixture":true}\n')
        (output/'source.html').write_text('<p>Retained synthetic source</p>\n')
        (output/'shard.json').write_text('{"synthetic-unit":"source locator"}\n')
        (output/'visual.json').write_text('{"fixture-visual":true}\n')
        (output/'current.json').write_text('{"atlas":"old"}\n')
        (output/'catalogue.html').write_text('<!doctype html><p>Old atlas</p>\n')
        self.entries={'schema_version':'stabilization-entry-inputs/1','round_id':'current','entries':{
            'current_map':gate.reference(output/'current.json',self.root),
            'catalogue':gate.reference(output/'catalogue.html',self.root)}}
        self.input_ref=gate.reference(output/'input-manifest.json',self.root)
        self.visual_ref=gate.reference(output/'visual.json',self.root)
        self.required={p.relative_to(self.root).as_posix():gate.sha(p) for p in output.iterdir()}
        self.resolver=patch.object(gate,'material_freeze_refs',return_value=self.required)
        self.resolver.start();self.addCleanup(self.resolver.stop)

    def tearDown(self):self.temp.cleanup()

    def freeze(self,**options):
        return gate.freeze('current',self.root/'freeze.json',self.root,entry_inputs=self.entries,
            material_input_manifest=self.input_ref,visual_source_manifest=self.visual_ref,**options)

    def test_ignored_source_manifest_shards_and_visual_bytes_are_frozen(self):
        result=self.freeze()
        self.assertEqual({'input_manifest':self.input_ref,'visual_source_manifest':self.visual_ref},
                         result['bound_material_review_inputs'])
        self.assertTrue(set(self.required)<=set(result['files']))
        gate.verify_frozen(result,self.root)
        (self.root/'output/source.html').write_text('<p>Changed source</p>\n')
        with self.assertRaisesRegex(ValueError,'frozen source changed'):gate.verify_frozen(result,self.root)

    def test_omitted_acquired_input_cannot_be_hidden_by_recounting_freeze_files(self):
        result=self.freeze();changed=copy.deepcopy(result)
        del changed['files']['output/shard.json']
        with self.assertRaisesRegex(ValueError,'omits acquired material'):
            gate.verify_frozen(changed,self.root)

    def test_missing_or_conflicting_input_fails_before_freeze_is_written(self):
        (self.root/'output/source.html').write_text('different bytes')
        with self.assertRaisesRegex(ValueError,'bytes differ'):self.freeze()
        self.assertFalse((self.root/'freeze.json').exists())

    def test_noncanonical_input_or_symlink_is_rejected(self):
        self.required['../outside']='a'*64
        with self.assertRaisesRegex(ValueError,'noncanonical'):self.freeze()
        del self.required['../outside']
        source=self.root/'output/source.html';source.unlink();source.symlink_to(self.root/'source.py')
        self.required['output/source.html']=gate.sha(self.root/'source.py')
        with self.assertRaisesRegex(ValueError,'symlink'):self.freeze()

    def test_visual_input_without_material_manifest_does_not_create_a_baseline(self):
        with self.assertRaisesRegex(ValueError,'require an explicit material'):
            gate.freeze('current',self.root/'freeze.json',self.root,visual_source_manifest=self.visual_ref)
        self.assertFalse((self.root/'freeze.json').exists())

    def test_explicit_input_manifest_must_belong_to_reconstructed_closure(self):
        del self.required[self.input_ref['path']]
        with self.assertRaisesRegex(ValueError,'outside its reconstructed closure'):self.freeze()
        self.assertFalse((self.root/'freeze.json').exists())


if __name__=='__main__':unittest.main()
