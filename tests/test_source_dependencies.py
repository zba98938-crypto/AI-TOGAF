"""Original source bytes, recursive assets and publication rejection paths."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(REPO/'togaf-standard-10th-ai/skills/_shared/scripts'),
              str(REPO/'togaf-standard-10th-ai/maintenance')]
from source_dependencies import dependency_evidence,local_dependencies
from source_closure import sha256,verify_source_closure
import close_skill_sources as builder


class MarkdownSourceDependencyTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project=Path(self.tmp.name)/'project'
        self.shared=self.project/'skills/_shared'
        self.corpus=self.shared/'corpus'
        self.corpus.mkdir(parents=True)
        for name,value in [('C',self.project),('D',self.corpus),('S',self.shared)]:
            p=patch.object(builder,name,value);p.start();self.addCleanup(p.stop)

    def write(self,root,name,text):
        path=root/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8');return path

    def relocation(self,names):
        rows=[{'old_path':'historical/'+name.removeprefix('sources/retained/'),
               'local_path':name,'sha256':sha256(self.project/name)} for name in names]
        return {'files':rows,'logical_paths':{r['old_path']:r['local_path'] for r in rows}}

    def close(self,migration=None,previous=None):
        return builder.close_markdown_dependencies(migration or {'files':[],'logical_paths':{}},previous)

    def bind(self):
        document=self.corpus/'root.md'
        record={'id':'source','source_path':'root.md','source_sha256':sha256(document)}
        index=self.write(self.corpus,'retrieval/main.jsonl',json.dumps(record)+'\n')
        mapping={p.relative_to(self.corpus).as_posix():p.relative_to(self.corpus).as_posix()
                 for p in self.corpus.rglob('*') if p.is_file() and p.name!='source-map.json'}
        result={'logical_paths':mapping,'file_sha256':{name:sha256(self.corpus/name) for name in mapping},
                'retrieval_index_sha256':{'retrieval/main.jsonl':sha256(index)},
                'markdown_dependencies':dependency_evidence(self.corpus)[0]}
        self.write(self.corpus,'source-map.json',json.dumps(result))
        return result

    def test_recursion_longer_than_old_eight_pass_limit_and_cycle_preserves_bytes(self):
        self.write(self.corpus,'root.md','[start](chain/0.md)\n')
        originals={}
        for number in range(11):
            text='[next]('+str(number+1)+'.md)\n' if number<10 else '[back](0.md) ![图](figure.svg)\n'
            originals[number]=self.write(self.project,f'chain/{number}.md',text).read_bytes()
        self.write(self.project,'chain/figure.svg','<svg>原始图</svg>')
        graph=self.close()
        self.assertEqual(13,len(graph))
        self.assertEqual([],local_dependencies(self.corpus)[1])
        for number,content in originals.items():self.assertEqual(content,(self.corpus/f'chain/{number}.md').read_bytes())

    def test_retained_assets_require_both_migration_identity_and_fingerprint(self):
        asset='sources/retained/book/figs/figure.svg'
        self.write(self.project,asset,'<svg>历史原字节</svg>')
        self.write(self.corpus,'root.md',f'![图]({asset})\n')
        with self.assertRaisesRegex(ValueError,'no migration fingerprint'):self.close()
        relocation=self.relocation([asset])
        self.close(relocation)
        self.assertEqual((self.project/asset).read_bytes(),(self.corpus/asset).read_bytes())
        relocation['files'][0]['sha256']='a'*64
        with self.assertRaisesRegex(ValueError,'fingerprint mismatch'):self.close(relocation)

    def test_conflicting_migration_records_and_logical_mapping_block_copy(self):
        asset='sources/retained/book/a.svg'
        self.write(self.project,asset,'<svg/>');self.write(self.corpus,'root.md',f'![图]({asset})')
        relocation=self.relocation([asset]);relocation['files'].append({**relocation['files'][0],'sha256':'a'*64})
        with self.assertRaisesRegex(ValueError,'fingerprint conflict'):self.close(relocation)
        relocation=self.relocation([asset]);relocation['logical_paths'][relocation['files'][0]['old_path']]='sources/other.svg'
        with self.assertRaisesRegex(ValueError,'path conflict'):self.close(relocation)

    def test_real_missing_dependency_cannot_be_removed_from_evidence(self):
        self.write(self.corpus,'root.md','![missing](missing.svg)')
        with self.assertRaisesRegex(ValueError,'missing or unrecorded'):self.close()
        self.bind()
        report=verify_source_closure(self.corpus)
        self.assertFalse(report['passed']);self.assertIn('markdown-dependency-missing',{r['code'] for r in report['issues']})

    def test_parent_links_inside_corpus_percent_encoding_and_title_are_valid(self):
        self.write(self.corpus,'nested/root.md','![图](../figure%20one.svg "中文标题") [标题](<../figure one.svg>)')
        self.write(self.project,'figure one.svg','<svg/>')
        graph=self.close()
        self.assertEqual(['figure one.svg']*2,[r['package_path'] for r in graph])
        self.assertEqual([],local_dependencies(self.corpus)[1])

    def test_dangerous_protocol_absolute_encoded_escape_and_symlink_are_rejected(self):
        outside=self.write(self.project,'private.svg','private')
        (self.corpus/'escape.svg').symlink_to(outside)
        for destination in ('file:///etc/passwd','javascript:alert','data:text/plain,secret','/etc/passwd',
                            '../../../private.svg','%2e%2e/%2e%2e/private.svg','escape.svg','bad%5cpath'):
            with self.subTest(destination=destination):
                self.write(self.corpus,'root.md',f'[bad]({destination})')
                with self.assertRaisesRegex(ValueError,'Unsafe Markdown'):self.close()

    def test_external_citations_are_retained_without_access(self):
        original='[文献](https://example.invalid/a) [邮件](mailto:example@example.invalid) [锚点](#local)\n'
        document=self.write(self.corpus,'root.md',original)
        self.assertEqual([],self.close());self.assertEqual(original,document.read_text())

    def test_unrecorded_existing_packaged_bytes_are_not_accepted_as_source(self):
        self.write(self.corpus,'root.md','![图](source-tools/figure.svg)')
        figure=self.write(self.corpus,'source-tools/figure.svg','<svg/>')
        with self.assertRaisesRegex(ValueError,'unrecorded'):self.close()
        self.close(previous={'source-tools/figure.svg':sha256(figure)})

    def test_recorded_reading_derivation_is_not_overwritten_by_recursive_source_copy(self):
        self.write(self.corpus,'root.md','[chapter](chapters/chapter.md)')
        self.write(self.project,'chapters/chapter.md','![historical relative image](old/figure.svg)')
        derived=self.write(self.corpus,'chapters/chapter.md','![portable image](../figures/figure.svg)')
        self.write(self.project,'figures/figure.svg','<svg/>')
        original=derived.read_bytes()
        self.close(previous={'chapters/chapter.md':sha256(derived)})
        self.assertEqual(original,derived.read_bytes())
        self.assertEqual([],local_dependencies(self.corpus)[1])

    def test_relocation_without_originals_passes_and_transitive_tamper_fails(self):
        self.write(self.corpus,'root.md','[child](nested/child.md)')
        self.write(self.project,'nested/child.md','![图](figure.svg)')
        self.write(self.project,'nested/figure.svg','<svg/>')
        self.close();self.bind()
        report=verify_source_closure(self.corpus);self.assertTrue(report['passed'],report['issues'])
        relocated=Path(self.tmp.name)/'moved/_shared/corpus';shutil.copytree(self.corpus,relocated)
        shutil.rmtree(self.project)
        self.assertTrue(verify_source_closure(relocated)['passed'])
        (relocated/'nested/figure.svg').write_text('tamper')
        self.assertFalse(verify_source_closure(relocated)['passed'])

    def test_inventory_omission_and_shared_dependency_tampering_block_publication(self):
        self.write(self.corpus,'root.md','[reference](../references/local.md)')
        reference=self.write(self.shared,'references/local.md','来源说明')
        self.close();manifest=self.bind()
        self.assertTrue(verify_source_closure(self.corpus)['passed'])
        manifest['markdown_dependencies']=[];self.write(self.corpus,'source-map.json',json.dumps(manifest))
        self.assertFalse(verify_source_closure(self.corpus)['passed'])
        self.bind();reference.write_text('tampered')
        self.assertFalse(verify_source_closure(self.corpus)['passed'])

    def test_shared_markdown_is_recursive_and_unsafe_or_missing_grandchildren_block(self):
        self.write(self.corpus,'root.md','[reference](../references/local.md)')
        reference=self.write(self.shared,'references/local.md','![missing](missing.svg)')
        with self.assertRaisesRegex(ValueError,'shared Markdown dependency missing'):self.close()
        reference.write_text('[unsafe](file:///etc/passwd)')
        with self.assertRaisesRegex(ValueError,'Unsafe Markdown'):self.close()
        reference.write_text('[next](nested/deep.md)')
        self.write(self.shared,'references/nested/deep.md','![图](../../corpus/figure.svg)')
        self.write(self.project,'figure.svg','<svg/>')
        graph=self.close();self.assertEqual(3,len(graph));self.bind()
        report=verify_source_closure(self.corpus);self.assertTrue(report['passed'],report['issues'])
        (self.corpus/'figure.svg').unlink()
        self.assertFalse(verify_source_closure(self.corpus)['passed'])

    def test_reference_style_and_html_image_dependencies_are_copied_and_checked(self):
        text='![图][asset]\n[asset]: figure.svg "标题"\n<img src="nested/html.svg">\n'
        self.write(self.corpus,'root.md',text)
        self.write(self.project,'figure.svg','<svg/>');self.write(self.project,'nested/html.svg','<svg/>')
        graph=self.close();self.assertEqual({'figure.svg','nested/html.svg'},{r['package_path'] for r in graph})
        self.bind();self.assertTrue(verify_source_closure(self.corpus)['passed'])
        (self.corpus/'nested/html.svg').unlink();self.assertFalse(verify_source_closure(self.corpus)['passed'])

    def test_internal_file_and_directory_symlink_aliases_cannot_disappear_during_packaging(self):
        figure=self.write(self.corpus,'real/figure.svg','<svg/>')
        (self.corpus/'alias.svg').symlink_to(figure)
        (self.corpus/'alias-directory').symlink_to(figure.parent,target_is_directory=True)
        for name in ('alias.svg','alias-directory/figure.svg'):
            self.write(self.corpus,'root.md',f'![图]({name})')
            with self.assertRaisesRegex(ValueError,'Unsafe Markdown'):self.close()
            self.bind();self.assertFalse(verify_source_closure(self.corpus)['passed'])

    def test_documented_manifest_self_reference_has_no_circular_fingerprint(self):
        self.write(self.corpus,'root.md','[map](source-map.json)')
        graph=self.close()
        self.assertEqual('source-map-self-reference',graph[0]['kind'])
        self.assertNotIn('sha256',graph[0])
        self.bind();report=verify_source_closure(self.corpus)
        self.assertTrue(report['passed'],report['issues'])
        self.assertIn('source-map.json',report['input_sha256'])


if __name__=='__main__':unittest.main()
