#!/usr/bin/env python3
"""Independent losslessness, provenance, link, and semantic regression checks."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'togaf-standard-10th-ai'

def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


class DiagramCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=read(OUT/'figures/index.json')
        cls.index=read(OUT/'architecture/diagrams/index.json')
        cls.entries={e['id']:e for e in cls.index['diagrams']}
        cls.records={fid:read(OUT/e['json_path']) for fid,e in cls.entries.items()}

    def test_every_source_figure_and_independent_image_disposed(self):
        logical={e['id'] for e in self.source['figures']}
        independent={e['id'] for e in self.source['embedded_images'] if e.get('json_path')}
        excluded={e['id'] for e in self.index['excluded_decorative_images']}
        self.assertEqual(logical|independent,set(self.records)|excluded)
        self.assertFalse(set(self.records)&excluded)
        self.assertTrue(logical<=set(self.records))
        self.assertEqual(len(self.entries),self.index['counts']['diagrams'])
        self.assertEqual(len(self.source['figures']),self.index['counts']['source_logical_figures'])

    def test_lossless_elements_relations_tables_and_graph_integrity(self):
        all_ids=set()
        for fid,d in self.records.items():
            with self.subTest(figure=fid):
                source=read(OUT/d['source']['figure_record_path'])
                ids={n['id'] for n in d['nodes']}
                edgeids={e['id'] for e in d['edges']}
                self.assertEqual(len(ids),len(d['nodes']))
                self.assertEqual(len(edgeids),len(d['edges']))
                self.assertFalse(all_ids & (ids|edgeids));all_ids.update(ids|edgeids)
                self.assertEqual(d['source_tables'],source.get('tables',[]))
                self.assertEqual(d['source_flows'],source.get('flows',[]))
                if 'image_kind' not in source:
                    self.assertEqual({n['local_id']:n['source_element'] for n in d['nodes']+d.get('rejected_nodes',[]) if n['source_element'] is not None},
                                     {n['id']:n for n in source.get('elements',[])})
                    retained=sorted([e for e in d['edges']+d.get('rejected_edges',[]) if e['source_relation_index'] is not None],key=lambda e:e['source_relation_index'])
                    self.assertEqual([e['source_relation'] for e in retained],source.get('relationships',[]))
                    self.assertEqual([e['source_relation_index'] for e in retained],list(range(len(source.get('relationships',[])))))
                    for e in d.get('rejected_edges',[]):
                        self.assertNotIn(e['id'],edgeids)
                        self.assertEqual(e['semantic_state'],'rejected-unobserved')
                        self.assertTrue(e['rejection_reason_zh'])
                    for e in d['edges']:
                        if e['source_relation_index'] is None:
                            self.assertIsNone(e['source_relation'])
                            self.assertEqual(e['origin'],'newly-transcribed-source-connection')
                            self.assertIn('current-visual-review',e['evidence_refs'])
                for e in d['edges']:
                    self.assertIn(e['from'],ids);self.assertIn(e['to'],ids)
                    self.assertIn(e['visual']['from'],ids);self.assertIn(e['visual']['to'],ids)
                byid={n['id']:n for n in d['nodes']}
                for n in d['nodes']:
                    self.assertNotIn(n['id'],n['ancestors'])
                    self.assertEqual(n['depth'],len(n['ancestors']))
                    if n['group_parent']:
                        self.assertIn(n['group_parent'],ids)
                        self.assertIn(n['id'],byid[n['group_parent']]['children'])
                for view in d['hierarchy']['views'].values():
                    for h in view['links']:
                        self.assertIn(h['parent'],ids);self.assertIn(h['child'],ids)

    def test_skill_matrix_cells_are_not_lost_or_reinterpreted_as_scores(self):
        matrices=0;cells=0
        for fid,d in self.records.items():
            source=read(OUT/d['source']['figure_record_path'])
            if source.get('image_kind')!='skills-role-proficiency-matrix':continue
            matrices+=1
            byid={n['id']:n for n in d['nodes']}
            expected={(t['id'],ri+1,ci+1):(t['columns'][ci],row[0],v)
                for t in source['tables'] for ri,row in enumerate(t['rows']) for ci,v in enumerate(row[1:],1)}
            actual={}
            for e in d['edges']:
                c=e['table_cell'];key=(c['table_id'],c['row'],c['column'])
                self.assertNotIn(key,actual)
                self.assertEqual(e['predicate'],'requires_skill')
                actual[key]=(byid[e['from']]['label_en'],byid[e['to']]['label_en'],e['required_proficiency'])
            self.assertEqual(actual,expected);cells+=len(expected)
        self.assertGreater(matrices,0);self.assertGreater(cells,0)

    def test_source_hashes_and_review_binding(self):
        self.assertEqual(self.index['source_index_sha256'],sha(OUT/'figures/index.json'))
        self.assertEqual(self.index['pipeline_sha256'],sha(ROOT/'tools/togaf_corpus/architecture_diagrams.py'))
        self.assertEqual(self.index['review_data_sha256'],sha(ROOT/'tools/togaf_corpus/architecture-diagram-reviews.json'))
        checked_pdfs={}
        for fid,d in self.records.items():
            with self.subTest(figure=fid):
                s=d['source'];pdf=ROOT/s['pdf_path']
                if pdf not in checked_pdfs:checked_pdfs[pdf]=sha(pdf)
                self.assertEqual(s['pdf_sha256'],checked_pdfs[pdf])
                self.assertEqual(s['figure_record_sha256'],sha(OUT/s['figure_record_path']))
                for im in s['images']:self.assertEqual(im['image_sha256'],sha(OUT/im['image_path']))
                review=d['current_visual_review']
                if review:
                    self.assertEqual(review['source_pdf_sha256'],s['pdf_sha256'])
                    self.assertEqual(sorted(review['source_crop_sha256']),sorted(im['image_sha256'] for im in s['images']))

    def test_all_local_links_and_evidence_references_resolve(self):
        docs={}
        for fid,d in self.records.items():
            with self.subTest(figure=fid):
                evidence={e['id']:e for e in d['evidence']}
                self.assertEqual(len(evidence),len(d['evidence']))
                for item in d['nodes']+d['edges']+d.get('rejected_edges',[])+d['hierarchy']['containment_and_grouping']:
                    for ref in item['evidence_refs']:self.assertIn(ref,evidence)
                mdpath=OUT/self.entries[fid]['markdown_path']
                md=mdpath.read_text()
                for target in re.findall(r'\]\(([^)]+)\)',md):
                    path,_,anchor=target.partition('#');p=(mdpath.parent/path).resolve()
                    self.assertTrue(p.is_file(),target)
                    if anchor:
                        if p not in docs:docs[p]=p.read_text()
                        self.assertIn('id="'+anchor+'"',docs[p],target)
                for e in evidence.values():
                    for field in ['record_path','review_path']:
                        if e.get(field):self.assertTrue((OUT/e[field]).is_file(),e[field])

    def test_mermaid_preserves_all_nodes_and_all_relations(self):
        for fid,d in self.records.items():
            with self.subTest(figure=fid):
                base=OUT/self.entries[fid]['mermaid_path']
                for suffix,edgecount in [('.mmd',len(d['edges'])+len(d['hierarchy']['containment_and_grouping'])),
                    ('.relations.mmd',len(d['edges'])),
                    ('.hierarchy.mmd',sum(len(v['links']) for v in d['hierarchy']['views'].values()))]:
                    p=base.with_suffix(suffix);text=p.read_text()
                    declarations=re.findall(r'^  (n\d+)\[',text,re.M)
                    edges=re.findall(r'^  (n\d+) (?:<-->|-->|---|-\.->|-\.-)\|.*\| (n\d+)$',text,re.M)
                    self.assertEqual(len(declarations),len(d['nodes']),str(p))
                    self.assertEqual(len(edges),edgecount,str(p))
                    for s,t in edges:self.assertIn(s,declarations);self.assertIn(t,declarations)

    def test_corrected_relationship_meaning(self):
        retail=self.records['G233/fig4-1']
        # G233 PDF p22 explicitly says the nested departments report up to
        # their business units. This is organizational, not individual HR.
        self.assertEqual({r['predicate'] for r in retail['edges']},{'reports_to'})
        self.assertEqual(len(retail['hierarchy']['organizational_reporting_edge_ids']),23)
        self.assertEqual({r['reporting_scope'] for r in retail['edges']},{'organization_unit-to-organization_unit'})
        capability=self.records['G233/fig3-1']
        self.assertEqual(capability['edges'][8]['predicate'],'instantiates')
        self.assertEqual(capability['edges'][14]['from'],'G233/fig3-1#business_process')
        self.assertEqual(capability['edges'][14]['to'],'G233/fig3-1#business_capability_instance')
        roles=self.records['G249/fig4-1']
        role_edges={e['source_relation_index']:e for e in roles['edges'] if e['source_relation_index'] is not None}
        self.assertEqual(role_edges[12]['from'],'G249/fig4-1#isit_users')
        self.assertEqual(role_edges[13]['from'],'G249/fig4-1#solution_arch')
        info=self.records['G190/fig4-1']
        self.assertEqual(sum(e['predicate']=='uses' for e in info['edges']),9)
        self.assertEqual(sum(e['predicate']=='modifies' for e in info['edges']),4)
        for n in info['nodes']:
            if n['source_parent']:self.assertIsNone(n['visual_parent'])
        self.assertEqual(self.records['G238/fig3-1']['category'],'system-or-data-reference-architecture')
        self.assertTrue(self.records['G206/fig3-1']['hierarchy']['views']['organizational_reporting']['links'])

    def test_causal_source_conflict_keeps_literal_polarity_and_prose_separate(self):
        d=self.records['G242/fig1-2']
        edge=next(e for e in d['edges'] if e['source_relation_index']==11)
        self.assertEqual((edge['from'],edge['to']),('G242/fig1-2#cost_digital','G242/fig1-2#digital_usages'))
        self.assertEqual(edge['polarity'],'+')
        self.assertEqual(edge['source_conflict']['prose_polarity'],'-')
        self.assertIn(13,{e['source_relation_index'] for e in d['rejected_edges']})

    def test_uml_attributes_survive_current_retrieval_projection(self):
        from build_architecture import compact
        d=compact(self.records['G190/figA-4'])
        n=next(n for n in d['nodes'] if n['local_id']=='cls_customer')
        self.assertNotIn('source_element',n)
        self.assertEqual(n['attributes']['attributes'],['First Name: text','Last Name: text','Age: numeric','Address: text'])

    def test_matrix_boundary_ambiguity_does_not_become_not_applicable(self):
        d=self.records['G242/fig3-10']
        storage=d['tables'][0]['rows'][-1]
        self.assertIsNone(storage[3])
        self.assertTrue(d['tables'][0]['source_layout_uncertainties'])
        accounting={n['local_id'] for n in d['nodes'] if n.get('group_parent')=='G242/fig3-10#grp_carbon_accounting'}
        self.assertEqual(accounting,{'row_electricity','row_inventories','row_total','row_offset'})
        child=next(n for n in d['nodes'] if n['local_id']=='sub_dc1')
        self.assertEqual(child['hierarchy_kind'],'classified_under')
        self.assertIsNone(child['visual_parent'])

    def test_source_review_corrects_scope_and_connector_endpoints(self):
        levels=self.records['G249/fig4-2']
        self.assertIsNone(next(n for n in levels['nodes'] if n['local_id']=='service')['group_parent'])
        self.assertEqual(levels['edges'][6]['predicate'],'uses')
        for fid in ['G198/fig6-1','G198/fig6-2']:
            d=self.records[fid];edges={e['source_relation_index']:e for e in d['edges']}
            self.assertEqual((edges[1]['from'],edges[1]['to']),(fid+'#layer_ac',fid+'#layer_as'))
            self.assertEqual((edges[2]['from'],edges[2]['to']),(fid+'#layer_tech',fid+'#layer_ac'))
            self.assertTrue(all(edges[i]['predicate']=='covers_portion_of' for i in range(3,11)))
        skills=self.records['G198/fig6-2']
        self.assertEqual(next(e for e in skills['edges'] if e['source_relation_index']==13)['label_en'],'Knowledge')
        meta=self.records['G248/fig3-1'];edges={e['source_relation_index']:e for e in meta['edges'] if e['source_relation_index'] is not None}
        expected={2:('driver','organization_unit'),16:('organization_unit','business_service'),
                  26:('process','product'),49:('data_entity','business_information'),
                  51:('logical_data_component','data_entity'),53:('data_entity','business_service'),
                  54:('logical_application_component','logical_data_component'),
                  55:('physical_application_component','physical_data_component'),
                  61:('business_service','logical_technology_component')}
        for index,pair in expected.items():
            self.assertEqual((edges[index]['from'].split('#')[1],edges[index]['to'].split('#')[1]),pair)
        self.assertEqual({e['source_relation_index'] for e in meta['rejected_edges']},{8,14})
        self.assertTrue(any(e['source_relation_index'] is None and e['from'].endswith('#application_service') and e['to'].endswith('#data_entity') for e in meta['edges']))

    def test_retail_maps_keep_all_actual_arrow_directions(self):
        # Independently enumerated from G206 original figures 7-1 and 7-2.
        expected={
            ('global_retail','central_operations'),('global_retail','online_store'),('global_retail','retail_operations'),
            ('central_operations','hr'),('central_operations','finance'),('central_operations','it'),
            ('central_operations','product_design'),('central_operations','sales_marketing'),('central_operations','warehouse'),
            ('sales_marketing','product_design'),('sales_marketing','retail_operations'),('retail_operations','sales_marketing'),
            ('sales_marketing','retail_strategy_team'),('retail_strategy_team','sales_marketing'),
            ('retail_operations','retail_strategy_team'),('retail_operations','us_stores'),('retail_operations','uk_stores'),
            ('retail_operations','japan_stores'),('retail_operations','warehouse'),('warehouse','retail_operations'),
            ('online_store','warehouse'),('warehouse','online_store'),('online_store','web_services'),
            ('product_design','product_suppliers'),('product_design','quality_assurance'),('product_suppliers','quality_assurance'),
        }
        for fid in ['G206/fig7-1','G206/fig7-2']:
            edges=[e for e in self.records[fid]['edges'] if e['predicate']=='association']
            actual={(e['from'].split('#')[1],e['to'].split('#')[1]) for e in edges}
            self.assertEqual(actual,expected);self.assertEqual(len(edges),len(expected))
        generic=self.records['G206/fig3-2']
        edges={(e['from'].split('#')[1],e['to'].split('#')[1]) for e in generic['edges']}
        self.assertIn(('marketing','product_design_board'),edges)
        self.assertIn(('supply_chain','product_suppliers'),edges)
        self.assertNotIn(('abc_corporation','product_design_board'),edges)

    def test_agile_arrows_cross_dorp_bands_without_false_endpoints(self):
        expected_counts={'G210/fig3-2':4,'G210/fig3-3':9,'G210/fig3-4':14,'G210/fig3-5':4}
        for fid,count in expected_counts.items():
            edges=[e for e in self.records[fid]['edges'] if e['predicate']=='flow']
            self.assertEqual(len(edges),count)
            for e in edges:
                self.assertFalse(e['from'].split('#')[1].startswith('dorp_'))
                self.assertFalse(e['to'].split('#')[1].startswith('dorp_'))
                self.assertFalse(e['visual']['direction_is_semantic_not_pixel_geometry'])
        cross=self.records['G210/fig3-4']
        pairs={(e['from'].split('#')[1],e['to'].split('#')[1]) for e in cross['edges'] if e['predicate']=='flow'}
        self.assertIn(('abd_1','ea_2'),pairs)
        self.assertIn(('ea_1','asd_2'),pairs)
        modes=self.records['G210/fig3-1']
        self.assertEqual(modes['flows'][0]['kind'],'display_order')
        self.assertEqual(modes['source_flows'][0]['kind'],'sequence')

    def test_current_retrieval_omits_archived_flows_tables_and_legend(self):
        from build_architecture import compact
        for fid in ['G210/fig3-1','G176/fig5-1','G178/figA-2']:
            current=compact(self.records[fid])
            for field in ['source_flows','source_tables','source_legend']:
                self.assertNotIn(field,current)
            for field in ['flows','tables','legend']:
                self.assertEqual(current[field],compact(self.records[fid][field]))


if __name__=='__main__':unittest.main(verbosity=2)
