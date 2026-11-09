"""Meaningful positive/negative fixtures for the independent path-delta audit."""
import json
from pathlib import Path
import tempfile
import xml.etree.ElementTree as ET

import business_path_delta_oracle as delta

HERE = Path(__file__).resolve().parent


def main():
    cases = []
    def check(name, ok):
        cases.append({"name":name,"passed":bool(ok)})
        assert ok, name
    horizontal = [((0.,0.),(10.,0.))]
    check("identical shaft contributes no new segment", delta.exposed_segments(horizontal,horizontal)==[])
    check("reversed shaft contributes no new segment", delta.exposed_segments(horizontal,[((10.,0.),(0.,0.))])==[])
    check("duplicate old shafts do not duplicate subtraction", delta.exposed_segments(horizontal,horizontal*2)==[])
    check("split old shaft intervals merge", delta.exposed_segments(horizontal,[((0.,0.),(4.,0.)),((4.,0.),(10.,0.))])==[])
    check("partial old shaft leaves exact remaining interval", delta.exposed_segments(horizontal,[((3.,0.),(7.,0.))])==[((0.,0.),(3.,0.)),((7.,0.),(10.,0.))])
    check("perpendicular crossing does not erase new geometry", delta.exposed_segments(horizontal,[((5.,-5.),(5.,5.))])==horizontal)
    check("collinear disjoint segment remains new", delta.exposed_segments(horizontal,[((20.,0.),(30.,0.))])==horizontal)
    check("diagonal collinear intervals subtract", delta.exposed_segments([((0.,0.),(10.,10.))],[((2.,2.),(8.,8.))])==[((0.,0.),(2.,2.)),((8.,8.),(10.,10.))])
    check("point crossing gives exact intersection", delta.centerline_contact((0,0),(10,0),(5,-5),(5,5))=={"kind":"point","point":(5.,0.)})
    check("parallel stroke proximity is not invented crossing", delta.centerline_contact((0,0),(10,0),(0,1),(10,1))["kind"]=="stroke-proximity")
    source = HERE/'annotation_fixtures'/'soa-qos-local-detour-feasibility.svg'
    owner = 'x-qos-consumer-interface'
    with tempfile.TemporaryDirectory(prefix='business-delta-',dir=HERE) as tmp:
        tmp=Path(tmp);before=tmp/'before';after=tmp/'after';before.mkdir();after.mkdir()
        original=ET.fromstring(source.read_text())
        old_path=next(e for e in original.iter() if delta.geometry.tag(e)=='path' and e.get('data-relationship-id')==owner)
        old_path.set('d','M1180,398 L1130,398 L1130,230 L1110,230')
        (before/'fixture.svg').write_text(ET.tostring(original,encoding='unicode'))
        (after/'fixture.svg').write_text(source.read_text())
        report=delta.audit(before,after)
        check("real compact SOA detour preserves attrs endpoints tangents",report['passed'] and report['changed_path_instances']==1)
        change=report['changes'][0]
        check("real compact SOA detour length delta is 40",abs(change['length_delta']-40)<1e-7)
        check("real compact SOA new exposed length is 55.4",abs(change['added_centerline_length']-55.4)<1e-7)
        check("new shaft and proven border contacts stay explicit deltas",change['geometry_delta_contacts_by_category']=={'shaft-or-other-path':2,'proven-context-border':2,'proven-context-background':1} and not change['forbidden_added_segment_conflicts'])
        check("new actual panel border crossing coordinates are exact",[p['point'] for p in change['new_proven_context_border_centerline_crossing_points']]==[(1110.,285.),(1130.,276.6)])
        check("endpoint card hierarchy is independently preserved",change['endpoint_card_hierarchy_preserved'])
        candidate=ET.fromstring(source.read_text());path=next(e for e in candidate.iter() if delta.geometry.tag(e)=='path' and e.get('data-relationship-id')==owner)
        path.set('stroke-width','2.4');(after/'fixture.svg').write_text(ET.tostring(candidate,encoding='unicode'))
        check("style change is rejected",not delta.audit(before,after)['passed'])
        candidate=ET.fromstring(source.read_text());path=next(e for e in candidate.iter() if delta.geometry.tag(e)=='path' and e.get('data-relationship-id')==owner)
        path.set('d',path.get('d').replace('M1180,398','M1179,398'));(after/'fixture.svg').write_text(ET.tostring(candidate,encoding='unicode'))
        check("endpoint change is rejected",not delta.audit(before,after)['passed'])
        candidate=ET.fromstring(source.read_text());ns='{http://www.w3.org/2000/svg}';group=ET.SubElement(candidate,ns+'g',{'data-entity-id':'injected-card'});ET.SubElement(group,ns+'rect',{'x':'1118','y':'288','width':'6','height':'8','fill':'white','stroke':'black'})
        (after/'fixture.svg').write_text(ET.tostring(candidate,encoding='unicode'));failed=delta.audit(before,after)
        check("new detour through actual card instance is rejected",not failed['passed'] and any(c['category']=='leaf-card' for c in failed['changes'][0]['forbidden_added_segment_conflicts']))
        own={'owner':'x','attrs':{'stroke':'black','stroke-width':'1.8'}};added=[((0.,0.),(10.,0.))]
        for kind in ('text','marker','badge','leader','glyph-or-other-path','other-context-rectangle'):
            obstacle={'category':kind,'index':1,'owner':'other','padding':.5}
            if kind in ('text','badge','other-context-rectangle'):obstacle['box']=(4.,-2.,6.,2.)
            else:obstacle['segments']=[((5.,-2.),(5.,2.))]
            forbidden,permitted=delta.measure_added_segments(added,own,[obstacle])
            check('new detour '+kind+' collision is rejected',len(forbidden)==1 and not permitted)
        forbidden,_=delta.measure_added_segments(added,own,[{'category':'marker','index':1,'owner':'x','padding':.5,'segments':[((5.,-2.),(5.,2.))]}])
        check('own marker is never exempted',len(forbidden)==1)
        forbidden,permitted=delta.measure_added_segments(added,own,[{'category':'shaft-or-other-path','index':1,'owner':'x','padding':.5,'fill':'black','segments':[((5.,-2.),(5.,2.))]}])
        check('own filled path remains a protected glyph',len(forbidden)==1 and not permitted)
        forbidden,permitted=delta.measure_added_segments(added,own,[{'category':'shaft-or-other-path','index':1,'owner':'x','padding':.5,'fill':'none','segments':[((5.,-2.),(5.,2.))]}])
        check('own unfilled shaft may underlie inline badge',not forbidden and not permitted)
        forbidden,_=delta.measure_added_segments(added,own,[{'category':'leader','index':1,'owner':'x','padding':.5,'segments':[((5.,-5.),(5.,5.))]}])
        check('own leader is only exempted near its initial anchor',len(forbidden)==1)
        for stroke_name,width,y,expected_collision in (('none','1',1.0,False),('none','50',1.0,False),('black','1',1.0,True),('none','1',.8,True)):
            painted=ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg"><rect x="4" y="'+str(y)+'" width="2" height="2" fill="#eef" stroke="'+stroke_name+'" stroke-width="'+width+'"/></svg>')
            actual=delta.geometry.inspect(ET.tostring(painted,encoding='unicode'));obstacles,_=delta.obstacle_records(painted,actual);forbidden,_=delta.measure_added_segments(added,own,obstacles)
            check('actual filled rect stroke='+stroke_name+' width='+width+' y='+str(y)+' keeps exact painted boundary',bool(forbidden)==expected_collision)
    result={'schema_version':'independent-business-path-delta-self-test/1','passed':all(c['passed'] for c in cases),'case_count':len(cases),'cases':cases,'audit_implementation_sha256':delta.sha(Path(delta.__file__)),'self_test_implementation_sha256':delta.sha(Path(__file__)),'png_view_count':0,**delta.FALSE_FLAGS}
    out=HERE/'business-path-delta-self-test-v5.json'
    if out.exists():raise SystemExit('Refusing to overwrite an existing self-test report')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
