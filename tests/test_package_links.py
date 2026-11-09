"""Portable Markdown closure must retain real failures and source identity."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
AUTHORING = REPO / 'togaf-standard-10th-ai'
sys.path.insert(0, str(AUTHORING / 'skills/_shared/scripts'))
import package_links
import verify_skill_packages

spec = importlib.util.spec_from_file_location('close_skill_links', AUTHORING / 'maintenance/close_skill_links.py')
closure = importlib.util.module_from_spec(spec)
spec.loader.exec_module(closure)


class PackageLinksTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='togaf-package-links-')
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name).resolve() / 'project'
        self.skills = self.project / 'skills'
        self.corpus = self.skills / '_shared/corpus'
        self.corpus.mkdir(parents=True)
        for name, value in [('C', self.project), ('P', self.skills), ('D', self.corpus)]:
            p = patch.object(closure, name, value)
            p.start()
            self.addCleanup(p.stop)

    def write(self, relative, content):
        path = self.project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        return path

    def close(self):
        with contextlib.redirect_stdout(io.StringIO()):
            result = closure.main()
        return result, json.loads((self.skills / 'reading-link-manifest.json').read_text())

    def retained(self, figure='figs/zh/figure.svg', *, fingerprint=True):
        text = f'![说明 [C220] 与 [来源]]({figure})\n'
        original = self.write('sources/retained/togaf-standard-10th-zh/G248.md', text)
        self.write('sources/retained/togaf-standard-10th-zh/' + figure, '<svg>retained-original</svg>')
        derived = self.write('skills/_shared/corpus/chapters/G248.md', text)
        self.write('skills/_shared/corpus/chapters/G248.json', json.dumps({
            'legacy_translation': {'path': 'togaf-standard-10th-zh/G248.md',
                                   'sha256': hashlib.sha256(original.read_bytes()).hexdigest() if fingerprint else 'wrong'}
        }))
        return original, derived, text

    def test_nested_labels_are_checked_without_losing_normal_links(self):
        self.write('skills/readme.md', '![图 [C220]](missing.svg) [normal](also-missing.md)\n')
        broken = package_links.broken_markdown_links(self.skills)
        self.assertEqual(['missing.svg', 'also-missing.md'], [x['target'] for x in broken])

    def test_retained_images_are_copied_with_labels_and_original_unchanged(self):
        for figure in ['figs/figure.svg', 'figs/zh/figure.svg']:
            with self.subTest(figure=figure):
                original, derived, text = self.retained(figure)
                result, report = self.close()
                self.assertEqual(0, result)
                copied = self.corpus / 'sources/retained/togaf-standard-10th-zh' / figure
                self.assertEqual('<svg>retained-original</svg>', copied.read_text())
                self.assertEqual(text, original.read_text())
                self.assertEqual(text.replace(f']({figure})', f'](../sources/retained/togaf-standard-10th-zh/{figure})'), derived.read_text())
                self.assertEqual([], package_links.broken_markdown_links(self.skills))
                self.assertIn(copied.relative_to(self.skills).as_posix(), report['copied_dependencies'])
                _, repeated = self.close()
                self.assertEqual(report['rewrites'], repeated['rewrites'])

    def test_unverified_retained_source_cannot_supply_a_picture(self):
        _, derived, text = self.retained(fingerprint=False)
        result, report = self.close()
        self.assertEqual(1, result)
        self.assertEqual(text, derived.read_text())
        self.assertEqual('figs/zh/figure.svg', report['unresolved'][0]['target'])
        self.assertFalse((self.corpus / 'sources/retained').exists())

    def test_genuinely_missing_link_remains_an_error(self):
        self.write('skills/_shared/corpus/chapters/missing.md', '![caption [source]](figs/absent.svg)\n')
        result, report = self.close()
        self.assertEqual(1, result)
        self.assertEqual(1, len(report['unresolved']))
        self.assertEqual(1, len(package_links.broken_markdown_links(self.skills)))

    def test_package_verification_excludes_only_top_level_work(self):
        self.write('skills/work/generated.md', '![runtime](not-rendered.png)\n')
        self.write('skills/_shared/corpus/maintenance/work/evidence.md', '![required](missing-source.png)\n')
        self.assertEqual(2, len(package_links.broken_markdown_links(self.skills)))
        with patch.object(verify_skill_packages, 'SKILLS', self.skills):
            report = verify_skill_packages.check_links()
        self.assertEqual('fail', report['status'])
        self.assertEqual(1, report['broken_count'])
        self.assertEqual('_shared/corpus/maintenance/work/evidence.md', report['broken'][0]['file'])
        self.write('skills/_shared/corpus/maintenance/work/missing-source.png', 'image')
        with patch.object(verify_skill_packages, 'SKILLS', self.skills):
            self.assertEqual('pass', verify_skill_packages.check_links()['status'])

    def test_closure_does_not_skip_nested_work_evidence(self):
        self.write('skills/work/generated.md', '![runtime](not-rendered.png)\n')
        self.write('skills/_shared/corpus/maintenance/work/evidence.md', '![required [original]](absent.svg)\n')
        result, report = self.close()
        self.assertEqual(1, result)
        self.assertEqual([{'file': '_shared/corpus/maintenance/work/evidence.md', 'target': 'absent.svg'}], report['unresolved'])


if __name__ == '__main__':
    unittest.main()
