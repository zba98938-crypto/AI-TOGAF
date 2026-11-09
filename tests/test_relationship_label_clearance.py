"""Regression checks for near parallel shafts and short stage connectors."""
import copy
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'togaf-standard-10th-ai').is_dir())
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from registry import load
from verify_artifact_profiles import inputs,substantive_change
from profile_render import render_profile
from label_geometry_oracle import inspect


class RelationshipLabelClearanceTests(unittest.TestCase):
    def checked_geometry(self,svg):
        # Deliberately omit companion coverage: the SVG alone must retain a
        # unique owner for every badge, including both forward and return edges.
        result=inspect(svg)
        self.assertEqual([],result['unmapped_badge_owners'])
        self.assertEqual([],result['ambiguous_badge_owners'])
        self.assertEqual([],result['contradictory_badge_owners'])
        self.assertTrue(all(b['id'] in result['relationship_paths'] for b in result['badge_records']))
        return result

    def variants(self,pid):
        profile=load()[2][pid]
        for layout in ('reference','adaptive'):
            for modified in (False,True):
                model,view=inputs(profile)
                if modified:substantive_change(model,view)
                unchanged=copy.deepcopy(model)
                svg,coverage=render_profile(model,view,profile,layout)
                self.assertEqual(unchanged,model)
                self.assertEqual([],coverage['errors'])
                yield layout,modified,svg

    def test_short_horizontal_stage_labels_do_not_need_a_ledger_crossing_leader(self):
        for pid in ('capability-change-overlay','capability-increment-analysis-default','capability-instance-model-default'):
            for layout,modified,svg in self.variants(pid):
                with self.subTest(profile=pid,layout=layout,modified=modified):
                    result=self.checked_geometry(svg)
                    self.assertEqual([],result['arrow_conflicts'])
                    self.assertEqual([],result['other_shaft_conflicts'])
                    self.assertFalse(any(p.get('owner_relationship_id')==pid+'-next' for p in result['annotation_leaders']))

    def test_near_parallel_forward_and_return_lines_keep_labels_clear(self):
        for layout,modified,svg in self.variants('compat-process-flow-diagram'):
            with self.subTest(layout=layout,modified=modified):
                result=self.checked_geometry(svg)
                self.assertEqual([],result['arrow_conflicts'])
                self.assertEqual([],result['other_shaft_conflicts'])
                self.assertEqual({'event-activity','activity-decision','decision-pack','decision-confirm'},
                                 {b['id'] for b in result['badge_records']})
                self.assertEqual('M760 229.0 L778 229.0 L778 426.0 L800 426.0',result['relationship_paths']['activity-decision']['d'])
                self.assertEqual('M800 402.0 L782 402.0 L782 205.0 L760 205.0',result['relationship_paths']['decision-confirm']['d'])

    def test_oracle_rejects_a_badge_covering_another_relationship_shaft(self):
        _,_,svg=next(self.variants('compat-process-flow-diagram'))
        self.assertEqual([],self.checked_geometry(svg)['other_shaft_conflicts'])
        root=ET.fromstring(svg)
        rows=list(root.iter())
        badge=next(e for index,e in enumerate(rows) if e.tag.endswith('}rect') and e.get('fill')=='white' and e.get('stroke')=='none'
                   and index+1<len(rows) and rows[index+1].tag.endswith('}text') and rows[index+1].text=='[4]')
        badge.set('x','766.5');badge.set('y','279.5')
        self.assertTrue(inspect(ET.tostring(root,encoding='unicode'))['other_shaft_conflicts'])

    def test_oracle_rejects_ambiguous_numbered_ledger_owners(self):
        svg='<svg xmlns="http://www.w3.org/2000/svg"><path data-relationship-id="a" d="M0 0 L50 0"/><rect x="10" y="20" width="31" height="22" fill="white" stroke="none"/><text>[1]</text><g data-relationship-id="a"><text>[1] A</text></g><g data-relationship-id="b"><text>[1] B</text></g></svg>'
        result=inspect(svg)
        self.assertEqual(['a','b'],result['ambiguous_badge_owners'][0]['candidate_relationship_ids'])
        self.assertIsNone(result['badge_records'][0]['id'])
        self.assertTrue(result['unmapped_badge_owners'])


if __name__=='__main__':unittest.main()
