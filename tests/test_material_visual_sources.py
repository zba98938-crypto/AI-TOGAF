"""Local PDF source/raster/crop integrity attacks; never semantic review evidence."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('material_visual_test_target',
    ROOT / 'togaf-standard-10th-ai/maintenance/material_visual_sources.py')
module = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(module)


class MaterialVisualSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(); cls.root = Path(cls.temp.name).resolve()
        for name in (module.PDF_PATH, module.EXTRACT_PATH):
            path = cls.root / name; path.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(ROOT/name, path)
        cls.reference = module.build(cls.root/'output/visual', cls.root)
        cls.original = module.read(cls.root/cls.reference['path'])

    @classmethod
    def tearDownClass(cls): cls.temp.cleanup()

    def attacked(self, label, manifest):
        path = self.root/'output'/('attacked-'+label+'.json'); path.write_text(json.dumps(manifest)+'\n')
        return module.reference(path, self.root)

    def test_all_pages_and_occurrences_reproduce_from_the_pinned_original(self):
        result = module.verify(self.reference, self.root)
        self.assertEqual((result['page_count'],result['occurrence_count'],result['visible_crops']), (40,310,310))
        self.assertEqual(result['provisional_types'], {'cover-page-image':1,'repeated-page-background':308,'unclassified-page-image':1})
        self.assertTrue(result['original_pdf_rerendered']); self.assertEqual(result['model_requests'],0)
        self.assertEqual(result['semantic_review_status'],'pending')

    def test_pdf_crop_clips_outside_page_and_preserves_pixel_geometry(self):
        clip, box = module.crop_geometry([-5,-3,45,20], [0,0,40,30], [80,60])
        self.assertEqual(clip,[0,0,40,20]); self.assertEqual(box,[0,0,80,40])
        self.assertEqual(module.crop_geometry([50,50,60,60],[0,0,40,30],[80,60]),(None,None))
        for bbox in ([10,0,0,20], [0,float('nan'),20,20], [0,True,20,20]):
            with self.subTest(bbox=bbox),self.assertRaises(ValueError): module.crop_geometry(bbox,[0,0,40,30],[80,60])

    def test_missing_duplicate_wrong_geometry_and_body_promotion_are_rejected(self):
        for label in ('missing-page','duplicate-page','missing-occurrence','geometry','background','signature','source','command'):
            value = copy.deepcopy(self.original)
            if label == 'missing-page': value['pages'].pop()
            elif label == 'duplicate-page': value['pages'][1] = value['pages'][0]
            elif label == 'missing-occurrence': value['pages'][0]['occurrences'].pop()
            elif label == 'geometry': value['pages'][0]['occurrences'][0]['crop_box_pixels'][0] += 1
            elif label == 'background': value['pages'][1]['occurrences'][0]['provisional_type'] = 'business-body-diagram'
            elif label == 'signature': value['real_organization_approval'] = 'approved'
            elif label == 'source': value['source']['sha256'] = 'a'*64
            else: value['render_command']['argv'].insert(1,'-aa')
            with self.subTest(label=label),self.assertRaises(ValueError): module.verify(self.attacked(label,value),self.root,rerender=False)

    def test_rehashed_fabricated_raster_and_crops_fail_actual_pdf_rerender(self):
        from PIL import Image
        value = copy.deepcopy(self.original); page = value['pages'][0]
        fake = Image.new('RGB', tuple(page['pixels']), 'white'); path = self.root/'output/visual/pages/fake-page.png'; fake.save(path)
        page['primary_image'] = module.reference(path,self.root)
        for index,record in enumerate(page['occurrences']):
            path = self.root/'output'/f'fake-crop-{index}.png'; fake.crop(record['crop_box_pixels']).save(path)
            record['crop_image'] = module.reference(path,self.root)
        with self.assertRaisesRegex(ValueError,'pinned original PDF'):
            module.verify(self.attacked('fake-pixels',value),self.root)

    def test_paths_and_source_drift_are_rejected(self):
        for name in ('../outside','/etc/passwd','https:example','a%2fb','a//b'):
            with self.subTest(name=name),self.assertRaises(ValueError): module.local(name,self.root)
        link = self.root/'outside-link'; link.symlink_to(self.root.parent,target_is_directory=True)
        with self.assertRaises(ValueError): module.local('outside-link/source.png',self.root)
        path = self.root/module.EXTRACT_PATH; old = path.read_bytes(); path.write_bytes(old+b' ')
        try:
            with self.assertRaisesRegex(ValueError,'fingerprint'): module.verify(self.reference,self.root,rerender=False)
        finally: path.write_bytes(old)


if __name__ == '__main__': unittest.main()
