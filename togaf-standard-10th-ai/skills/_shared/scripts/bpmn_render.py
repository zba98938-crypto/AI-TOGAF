"""Render an explicit BPMNDI view with bpmn-js; no layout or missing DI is invented.

This gate covers visible process/collaboration notation, not the full BPMN semantic
or choreography suite. All model, DI and rendered element IDs are cross-checked.
"""
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path
from standards import ROOT, BPMN, Invalid, Incomplete, check_native, safe_xml, local, sha, write_new

DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
SHAPES = {'participant', 'lane', 'task', 'userTask', 'serviceTask', 'manualTask',
          'sendTask', 'receiveTask', 'scriptTask', 'businessRuleTask', 'callActivity',
          'subProcess', 'transaction', 'adHocSubProcess', 'startEvent', 'endEvent',
          'intermediateCatchEvent', 'intermediateThrowEvent', 'boundaryEvent',
          'exclusiveGateway', 'inclusiveGateway', 'parallelGateway',
          'eventBasedGateway', 'complexGateway', 'textAnnotation', 'group',
          'dataObjectReference', 'dataStoreReference', 'dataInput', 'dataOutput'}
EDGES = {'sequenceFlow', 'messageFlow', 'association', 'dataInputAssociation', 'dataOutputAssociation'}
CONTAINERS = {'subProcess', 'transaction', 'adHocSubProcess'}


def diagram_plan(data, package_root=None):
    """Require the single requested view to cover every visible semantic element."""
    report = check_native(data, 'bpmn', '2.0.2', package_root)
    if report['errors']:
        raise Invalid('; '.join(report['errors']))
    blockers = [b for b in report['blockers'] if not b.startswith('complete BPMN normative')]
    if blockers:
        raise Incomplete('; '.join(blockers))
    root = safe_xml(data)
    nodes = {e.get('id'): e for e in root.iter() if isinstance(e.tag, str) and e.get('id')}
    diagrams = list(root.iter('{'+DI+'}BPMNDiagram'))
    if len(diagrams) != 1:
        raise Incomplete('BPMNDI rendering requires exactly one explicit BPMNDiagram; no DI or automatic diagram selection is supported')
    planes = diagrams[0].findall('{'+DI+'}BPMNPlane')
    if len(planes) != 1:
        raise Invalid('BPMNDiagram requires one BPMNPlane')
    plane = planes[0]
    target = nodes.get(plane.get('bpmnElement'))
    if target is None or local(target.tag) not in {'process', 'collaboration'}:
        raise Incomplete('Only process and collaboration BPMNPlane notation is implemented; choreography is not covered')
    shape_map, edge_map = {}, {}
    for element in plane:
        kind = local(element.tag)
        if kind not in {'BPMNShape', 'BPMNEdge'}:
            continue
        ident = element.get('bpmnElement')
        semantic = nodes.get(ident)
        allowed = SHAPES if kind == 'BPMNShape' else EDGES
        if semantic is None or local(semantic.tag) not in allowed:
            raise Incomplete('Unsupported native notation element: '+str(ident))
        collection = shape_map if kind == 'BPMNShape' else edge_map
        if ident in collection:
            raise Invalid('Duplicate DI graphic for semantic element: '+str(ident))
        collection[ident] = element
        if kind == 'BPMNEdge':
            for waypoint in element:
                if local(waypoint.tag) == 'waypoint':
                    try:
                        if not all(math.isfinite(float(waypoint.get(k))) for k in ('x', 'y')):
                            raise ValueError()
                    except (TypeError, ValueError):
                        raise Invalid('BPMNEdge requires finite waypoints: '+str(ident))
    expected_shapes, expected_edges, hidden = set(), set(), []

    def lanes(lane_set):
        for lane in lane_set.findall('{'+BPMN+'}lane'):
            expected_shapes.add(lane.get('id'))
            for child in lane.findall('{'+BPMN+'}childLaneSet'):
                lanes(child)

    def container(owner):
        for element in owner:
            if not isinstance(element.tag, str) or not element.tag.startswith('{'+BPMN+'}'):
                continue
            kind, ident = local(element.tag), element.get('id')
            if kind == 'laneSet':
                lanes(element)
            elif kind in SHAPES:
                expected_shapes.add(ident)
                if kind in CONTAINERS and ident in shape_map and shape_map[ident].get('isExpanded') == 'true':
                    container(element)
                elif kind in CONTAINERS:
                    hidden.extend({'id': child.get('id'), 'type': local(child.tag), 'collapsed_parent_id': ident}
                                  for child in element.iterdescendants()
                                  if isinstance(child.tag, str) and child.get('id'))
            elif kind in EDGES:
                expected_edges.add(ident)
            elif kind in {'choreographyTask', 'subChoreography', 'callChoreography'}:
                raise Incomplete('Choreography notation is not implemented')

    if local(target.tag) == 'process':
        container(target)
    else:
        for participant in target.findall('{'+BPMN+'}participant'):
            expected_shapes.add(participant.get('id'))
            if participant.get('processRef'):
                container(nodes[participant.get('processRef')])
        for flow in target.findall('{'+BPMN+'}messageFlow'):
            expected_edges.add(flow.get('id'))
        for annotation in target:
            if local(annotation.tag) in {'textAnnotation', 'group'}:
                expected_shapes.add(annotation.get('id'))
            elif local(annotation.tag) == 'association':
                expected_edges.add(annotation.get('id'))
    if None in expected_shapes or None in expected_edges:
        raise Invalid('Visible semantic elements require explicit stable IDs')
    missing = sorted((expected_shapes-set(shape_map)) | (expected_edges-set(edge_map)))
    if missing:
        raise Incomplete('Missing BPMNDI shapes or edges for visible semantic elements: '+', '.join(missing))
    extras = sorted((set(shape_map)-expected_shapes) | (set(edge_map)-expected_edges))
    if extras:
        raise Incomplete('DI graphics outside the visible process/collaboration scope: '+', '.join(extras))
    if not shape_map:
        raise Incomplete('BPMNDI contains no visible shapes')
    return {'diagram_id': diagrams[0].get('id'), 'plane_id': plane.get('id'),
            'root_id': target.get('id'), 'shape_ids': sorted(shape_map),
            'edge_ids': sorted(edge_map), 'source_sha256': sha(data),
            'visible_names': {i: nodes[i].get('name') for i in set(shape_map)|set(edge_map) if nodes[i].get('name')},
            'hidden_native_elements': hidden,
            'native_validation': report}


def render_native(data, out, package_root=None):
    plan = diagram_plan(data, package_root)
    out = Path(out).resolve()
    base = out.with_suffix('') if out.suffix.lower() in {'.svg', '.png'} else out/'diagram'
    destinations = {'svg': base.with_suffix('.svg'), 'png': base.with_suffix('.png'),
                    'report': base.with_suffix('.render.json')}
    if any(p.exists() for p in destinations.values()):
        raise Invalid('Refusing to overwrite an existing BPMN rendering or evidence report')
    with tempfile.TemporaryDirectory(prefix='bpmn-notation-') as tmp:
        folder = Path(tmp)
        source, font = folder/'input.bpmn', folder/'font.ttf'
        source.write_bytes(data)
        from generate import subset_font
        subset_font(data.decode('utf-8'), font)
        spec = {**{k: v for k, v in plan.items() if k != 'native_validation'},
                'input': str(source), 'font': str(font), 'svg': str(folder/'diagram.svg'),
                'png': str(folder/'diagram.png'), 'report': str(folder/'render.json')}
        (folder/'spec.json').write_text(json.dumps(spec, ensure_ascii=False))
        run = subprocess.run([shutil.which('node') or 'node', str(ROOT/'scripts/bpmn_render.mjs'), str(folder/'spec.json')],
                             capture_output=True, text=True, timeout=120)
        if run.returncode:
            reason = (run.stderr or run.stdout)[-4000:]
            if run.returncode == 3:
                raise Incomplete('BPMN notation backend blocked: '+reason)
            raise Invalid('BPMN notation backend failed: '+reason)
        result = json.loads((folder/'render.json').read_text())
        result.update(operation='render', language='bpmn', version='2.0.2',
                      native_validation=plan['native_validation'],
                      conformance_status='incomplete', full_language_acceptance=False,
                      outputs={k: str(p) for k,p in destinations.items()},
                      source_sha256=sha(data))
        for kind in ('svg', 'png'):
            write_new(destinations[kind], (folder/('diagram.'+kind)).read_bytes())
        write_new(destinations['report'], json.dumps(result, ensure_ascii=False, indent=2).encode())
        return result
