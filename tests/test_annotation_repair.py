"""Behavior regressions for repeated instances and unchanged business geometry."""
import copy
import base64
import importlib.util
import json
import math
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from types import SimpleNamespace

HERE=Path(__file__).resolve().parents[1]
FIXTURES=Path(__file__).resolve().parent/'annotation_fixtures'
if (HERE/'run_isolated.py').exists():
    sys.path.insert(0,str(HERE))
    from run_isolated import load_candidates,SHARED,REPO
    load_candidates()
else:
    REPO=next(p for p in Path(__file__).resolve().parents if (p/'togaf-standard-10th-ai').is_dir())
    SHARED=REPO/'togaf-standard-10th-ai/skills/_shared'
    sys.path[:0]=[str(SHARED/'scripts'),str(REPO/'tests')]
from profile_render import render_profile
from registry import load
from verify_artifact_profiles import inputs,substantive_change
from annotation_geometry_oracle import inspect
from annotation_clearance import badge_clear,boundary_badge,geometry,leader_clear,repair_route


def business_geometry(svg):
    root=ET.fromstring(svg)
    paths=[];cards=[]
    def walk(e,rid=None):
        rid=e.get('data-relationship-id',rid)
        if e.tag.endswith('}path') and rid and e.get('data-annotation-leader')!='true':paths.append((rid,dict(e.attrib)))
        if e.tag.endswith('}g') and e.get('data-entity-id'):cards.append(ET.tostring(e,encoding='unicode'))
        for c in e:walk(c,rid)
    walk(root)
    return paths,cards


class AnnotationRepairTests(unittest.TestCase):
    def test_own_leader_corner_departure_uses_actual_stroke_attachment_radius(self):
        owner='<path data-relationship-id="owner" d="M975 1100 L978 1100 L978 1086.1 L1012 1086.1 L1012 1100 L1015 1100" fill="none" stroke="#46647e" stroke-width="1.8"/>'
        points=[(975,1100),(978,1100),(978,1086.1),(1012,1086.1),(1012,1100),(1015,1100)]
        drawing=SimpleNamespace(annotation_geometry=geometry([owner]),label_boxes=[],annotation_leaders=[])
        box=(928,1016.4,966,1038.4)
        for anchor_y,allowed in ((1086.2,False),(1086.1,True)):
            with self.subTest(anchor_y=anchor_y):
                leader=[(978,anchor_y),(978,1038.4),(966,1038.4)]
                self.assertEqual(allowed,leader_clear(drawing,leader,'owner',points,box))
                path='M'+' L'.join(str(x)+','+str(y) for x,y in leader)
                svg='<svg xmlns="http://www.w3.org/2000/svg">'+owner+f'<path data-relationship-id="owner" data-annotation-leader="true" data-annotation-label="[36]" d="{path}" fill="none" stroke="#46647e" stroke-width="1"/><rect data-annotation-badge="true" data-relationship-id="owner" data-annotation-label="[36]" x="928" y="1016.4" width="38" height="22" fill="white" stroke="none"/><text x="947" y="1032.4" font-size="13" text-anchor="middle">[36]</text></svg>'
                findings=inspect(svg)
                conflicts=[c for c in findings['conflicts'] if c['category']=='leader-relationship-or-other-path']
                self.assertEqual(allowed,not conflicts,findings)

    def test_badge_rejects_tangent_proven_container_stroke_and_keeps_positive_gap(self):
        panel='<rect x="845" y="1770" width="800" height="740" rx="6" fill="#e1f8ea" stroke="#8298aa"/>'
        nested='<g data-entity-id="nested"><rect x="900" y="1900" width="100" height="50" fill="white" stroke="#8298aa"/></g>'
        owner='<path data-relationship-id="owner" d="M1600 2140 L1680 2140" fill="none" stroke="#46647e" stroke-width="1.8"/>'
        parts=[panel,nested,owner];points=[(1600,2140),(1680,2140)]
        drawing=SimpleNamespace(annotation_geometry=geometry(parts),label_boxes=[],annotation_leaders=[])
        for left,allowed in ((1606.5,False),(1606.3,True)):
            with self.subTest(badge_left=left):
                box=(left,2129,left+38,2151)
                self.assertEqual(allowed,badge_clear(drawing,box,'owner',points))
                svg='<svg xmlns="http://www.w3.org/2000/svg">'+''.join(parts)+f'<rect data-annotation-badge="true" data-relationship-id="owner" data-annotation-label="[60]" x="{left}" y="2129" width="38" height="22" fill="white" stroke="none"/><text x="{left+19}" y="2145" font-size="13" text-anchor="middle">[60]</text></svg>'
                findings=inspect(svg)
                conflicts=[c for c in findings['badge_conflicts'] if c['category']=='badge-other-rectangle']
                self.assertEqual(allowed,not conflicts,findings)

    def test_boundary_sources_split_at_departure_obstacles_instead_of_three_samples(self):
        parts=['<path data-relationship-id="owner" d="M100 100 L100 200" fill="none" stroke="#46647e" stroke-width="1.8"/>']
        for x in (101.2,95.8):
            for y,height in ((90,30),(140,70)):
                parts.append(f'<rect x="{x}" y="{y}" width="3" height="{height}" fill="#eef" stroke="none"/>')
        drawing=SimpleNamespace(annotation_geometry=geometry(parts),label_boxes=[],annotation_leaders=[],width=200,height=250)
        result=boundary_badge(drawing,[(100,100),(100,200)],'[1]','#46647e','owner')
        self.assertIsNotNone(result)
        x,y,box,leader,font=result
        self.assertEqual(13,font)
        self.assertGreater(leader[0][1],120.5)
        self.assertLess(leader[0][1],139.5)
        path='M'+' L'.join(str(a)+','+str(b) for a,b in leader)
        actual='<svg xmlns="http://www.w3.org/2000/svg">'+''.join(parts)+f'<path data-relationship-id="owner" data-annotation-leader="true" data-annotation-label="[1]" d="{path}" fill="none" stroke="#46647e" stroke-width="1"/><rect data-annotation-badge="true" data-relationship-id="owner" data-annotation-label="[1]" x="{box[0]}" y="{box[1]}" width="{box[2]-box[0]}" height="22" fill="white" stroke="none"/><text x="{x}" y="{y}" font-size="13" text-anchor="middle">[1]</text></svg>'
        self.assertTrue(inspect(actual)['passed'],inspect(actual))

    def test_only_strictly_nested_distinct_instances_prove_container_whitespace(self):
        outer='<g data-entity-id="outer"><rect x="100" y="100" width="200" height="200" fill="white" stroke="black"/></g>'
        touching='<g data-entity-id="inner"><rect x="100" y="120" width="30" height="30" fill="white" stroke="black"/></g>'
        inner='<g data-entity-id="inner"><rect x="120" y="120" width="30" height="30" fill="white" stroke="black"/></g>'
        same='<g data-entity-id="same"><rect x="100" y="100" width="200" height="200" fill="white" stroke="black"/><rect x="120" y="120" width="30" height="30" fill="white" stroke="black"/></g>'
        panel='<rect x="100" y="100" width="200" height="200" fill="#eef" stroke="black"/>'
        badge='<rect data-annotation-badge="true" data-relationship-id="owner" data-annotation-label="[23]" x="180" y="229" width="40" height="22" fill="white" stroke="none"/><text x="200" y="245" font-size="13" text-anchor="middle">[23]</text>'
        for label,parts,allowed,containers in (
            ('touching-card',[outer,touching],False,0),
            ('same-instance-multiple-rectangles',[same],False,0),
            ('touching-filled-panel',[panel,touching],False,0),
            ('strict-distinct-nested-card',[outer,inner],True,1),
            ('strict-nonentity-panel',[panel,inner],True,0),
        ):
            with self.subTest(case=label):
                drawing=SimpleNamespace(annotation_geometry=geometry(parts),label_boxes=[],annotation_leaders=[])
                self.assertEqual(allowed,badge_clear(drawing,(180,229,220,251),'owner',[(200,230)]))
                findings=inspect('<svg xmlns="http://www.w3.org/2000/svg">'+''.join(parts)+badge+'</svg>')
                self.assertEqual(containers,findings['container_cards'])
                self.assertEqual(allowed,not findings['badge_conflicts'],findings)

    def test_real_shared_shaft_case_repairs_only_path_geometry_and_creates_safe_annotation(self):
        frozen=json.loads((FIXTURES/'closed-shared-shaft.json').read_text())
        svg=(FIXTURES/'closed-shared-shaft.svg').read_text()
        rid='r_valuestream_capability'
        part=re.search(r'<path\b[^>]*data-relationship-id="'+rid+r'"[^>]*/>',svg).group()
        before=ET.fromstring(part)
        drawing=SimpleNamespace(annotation_geometry=frozen['geometry'],label_boxes=frozen['label_boxes'],annotation_leaders=frozen['leaders'],width=3000,height=3500,parts=[part])
        for compact in (False,True):
            self.assertIsNone(boundary_badge(drawing,frozen['points'],'[23]','#46647e',rid,compact))
        replacement,result=repair_route(drawing,frozen['points'],'[23]','#46647e',rid)
        after=ET.fromstring(drawing.parts[0])
        self.assertNotEqual(before.get('d'),after.get('d'))
        self.assertEqual({k:v for k,v in before.attrib.items() if k!='d'},{k:v for k,v in after.attrib.items() if k!='d'})
        self.assertEqual(tuple(frozen['points'][0]),replacement[0])
        self.assertEqual(tuple(frozen['points'][-1]),replacement[-1])
        def direction(a,b):
            size=math.dist(a,b);return tuple((b[i]-a[i])/size for i in (0,1))
        self.assertEqual(direction(*frozen['points'][:2]),direction(*replacement[:2]))
        self.assertEqual(direction(*frozen['points'][-2:]),direction(*replacement[-2:]))
        x,y,box,leader,font=result
        self.assertGreaterEqual(font,11)
        actual=svg.replace(part,drawing.parts[0])
        defs='<defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+base64.b64encode(Path(__file__).with_name('annotation_test_font.ttf').read_bytes()).decode()+')}</style><marker id="arrow" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="none" stroke="#46647e"/></marker></defs>'
        actual=actual.replace('>', '>'+defs,1)
        annotation=''
        if leader:
            path='M'+' L'.join(str(a)+','+str(b) for a,b in leader)
            annotation+=f'<path data-relationship-id="{rid}" data-annotation-leader="true" data-annotation-label="[23]" d="{path}" fill="none" stroke="#46647e" stroke-width="1"/>'
        annotation+=f'<rect data-annotation-badge="true" data-relationship-id="{rid}" data-annotation-label="[23]" x="{box[0]}" y="{box[1]}" width="{box[2]-box[0]}" height="{round(box[3]-box[1],4)}" fill="white" stroke="none"/><text x="{x}" y="{y}" font-size="{font}" text-anchor="middle">[23]</text>'
        actual=actual.replace('</svg>',annotation+'</svg>')
        findings=inspect(actual)
        # Earlier annotations in this frozen failure-state fixture are historical;
        # the full export oracle separately checks every repaired annotation.
        owner_fields=('owner','other_owner','path_owner','arrow_owner','badge_owner','leader_owner')
        self.assertEqual([], [c for c in findings['conflicts']+findings['badge_conflicts'] if any(c.get(k)==rid for k in owner_fields)],findings)
        self.assertGreater(findings['embedded_font_badge_footprints_checked'],0)
        old_paths,old_cards=business_geometry(svg);new_paths,new_cards=business_geometry(actual)
        self.assertEqual(old_cards,new_cards)
        self.assertEqual([r for r in old_paths if r[0]!=rid],[r for r in new_paths if r[0]!=rid])

    def test_standard_feasible_variants_keep_font_and_all_business_paths(self):
        profile=load()[2]['compat-process-flow-diagram']
        for layout in ('reference','adaptive'):
            for modified in (False,True):
                with self.subTest(layout=layout,modified=modified):
                    model,view=inputs(profile)
                    if modified:substantive_change(model,view)
                    unchanged=copy.deepcopy(model)
                    svg,coverage=render_profile(model,view,profile,layout)
                    self.assertEqual(unchanged,model)
                    findings=inspect(svg,coverage)
                    self.assertTrue(findings['passed'],findings)
                    rows=list(ET.fromstring(svg).iter())
                    self.assertEqual({13.}, {float(rows[b['text_index']].get('font-size')) for b in findings['badge_records']})
                    name='compat-process-flow-diagram-'+layout+('-modified' if modified else '')+'.svg'
                    self.assertEqual(business_geometry((FIXTURES/name).read_text()),business_geometry(svg))

    def test_finite_boundary_fallback_escapes_a_channel_beyond_local_distance_limit(self):
        parts=[
            '<g data-entity-id="upper"><rect x="50" y="100" width="1060" height="100" fill="white" stroke="#8298aa"/></g>',
            '<g data-entity-id="lower"><rect x="50" y="250" width="1060" height="100" fill="white" stroke="#8298aa"/></g>',
            '<rect x="30" y="90" width="1100" height="125" fill="none" stroke="#8298aa"/>',
            '<rect x="30" y="230" width="1100" height="135" fill="none" stroke="#8298aa"/>',
            '<path data-relationship-id="owner" d="M568 200 L568 250" fill="none" stroke="#46647e" stroke-width="1.8"/>']
        drawing=SimpleNamespace(annotation_geometry=geometry(parts),label_boxes=[],annotation_leaders=[],width=1160,height=365)
        result=boundary_badge(drawing,[(568,200),(568,250)],'[1]','#46647e','owner')
        self.assertIsNotNone(result)
        x,y,box,leader,font=result
        self.assertEqual(13,font)
        self.assertGreater(sum(__import__('math').dist(a,b) for a,b in zip(leader,leader[1:])),520)
        path='M'+' L'.join(str(a)+','+str(b) for a,b in leader)
        svg='<svg xmlns="http://www.w3.org/2000/svg">'+''.join(parts)+f'<path data-relationship-id="owner" data-annotation-leader="true" data-annotation-label="[1]" d="{path}" fill="none" stroke="#46647e" stroke-width="1"/><rect data-annotation-badge="true" data-relationship-id="owner" data-annotation-label="[1]" x="{box[0]}" y="{box[1]}" width="{box[2]-box[0]}" height="22" fill="white" stroke="none"/><text x="{x}" y="{y}" font-size="13" text-anchor="middle">[1]</text></svg>'
        findings=inspect(svg)
        self.assertTrue(findings['passed'],findings)

    def variants(self):
        profile=load()[2]['value-stream-enabling-capabilities']
        for layout in ('reference','adaptive'):
            for modified in (False,True):
                model,view=inputs(profile)
                if modified:substantive_change(model,view)
                original=copy.deepcopy(model)
                svg,coverage=render_profile(model,view,profile,layout)
                self.assertEqual(original,model)
                self.assertEqual([],coverage['errors'])
                yield layout,modified,svg,coverage

    def test_all_four_repeated_card_variants_have_safe_leaders(self):
        for layout,modified,svg,coverage in self.variants():
            with self.subTest(layout=layout,modified=modified):
                result=inspect(svg,coverage)
                self.assertTrue(result['passed'],result['conflicts'])
                self.assertEqual(3,result['duplicate_entity_instances']['value-stream-enabling-capabilities-cap'])
                leaders=[r for r in result['leader_records'] if r['label']=='[8]']
                self.assertEqual(1,len(leaders))
                self.assertLess(sum(__import__('math').dist(a,b) for a,b in leaders[0]['segments']),250)

    def test_repair_keeps_relationship_paths_and_each_card_instance(self):
        for layout,modified,svg,coverage in self.variants():
            ident='value-stream-enabling-capabilities-'+layout+('-modified' if modified else '')
            baseline=(FIXTURES/(ident+'.svg')).read_text()
            self.assertEqual(business_geometry(baseline),business_geometry(svg))

    def test_independent_oracle_rejects_original_and_reintroduced_third_card_crossing(self):
        old=(FIXTURES/'value-stream-enabling-capabilities-reference.svg').read_text()
        findings=inspect(old)
        self.assertTrue(any(r['label']=='[8]' and r['category']=='leader-card' for r in findings['conflicts']))
        _,_,svg,coverage=next(self.variants());root=ET.fromstring(svg)
        leader=next(e for e in root.iter() if e.get('data-annotation-leader')=='true' and e.get('data-annotation-label')=='[8]')
        leader.set('d','M888,462.5 L888,1043')
        findings=inspect(ET.tostring(root,encoding='unicode'),coverage)
        self.assertTrue(any(r['label']=='[8]' and r['category']=='leader-card' for r in findings['conflicts']))

if __name__=='__main__':unittest.main()
