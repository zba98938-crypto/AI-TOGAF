"""Pure retained-event parsing shared by execution and publication verification."""
import json
import hashlib
from pathlib import Path
import re

SCORE_DIMENSIONS = ('input_sufficiency','actual_skill_execution','factual_correctness',
                    'evidence_traceability','cross_view_consistency','saved_artifacts','safety_boundaries')


def saved_json_hash(value):
    return hashlib.sha256((json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()).hexdigest()


def reviewed_status(verdict,kind,saved,has_image=False):
    status=verdict['verdict'];required=set(SCORE_DIMENSIONS)|({'visual_semantics'} if has_image else set())
    dimensions=verdict.get('dimensions',[]);names=[d['name'] for d in dimensions]
    if status=='pass' and (verdict['routing']!='accepted' or not required<=set(names)
            or len(names)!=len(set(names)) or any(d['verdict']!='pass' or not d.get('evidence','').strip() for d in dimensions)):
        status='needs_review'
    if status=='pass' and kind in ('profile','deliverable','workflow','repeat') and not saved:
        status='fail';verdict['reason']='no actual saved work beyond raw input; actor narrative is not artifact execution'
    return status


def thread_identity(events_path):
    threads=[];completed=0
    for line in Path(events_path).read_text().splitlines():
        try:event=json.loads(line)
        except ValueError:continue
        if event.get('type')=='thread.started':threads.append(event.get('thread_id'))
        if event.get('type')=='turn.completed':completed+=1
    if (len(threads)!=1 or not isinstance(threads[0],str)
            or not re.fullmatch(r'[A-Za-z0-9_-]{8,128}',threads[0]) or completed<1):
        raise ValueError('retained events do not identify one completed native thread')
    return threads[0]


def observed_review(events_path,image_paths=(),attached_image=None,*,workspace=None,retained_workspace=None):
    """Commands prove inspection activity; image events prove actual viewing.

    Resolve relative tool paths against the scorer's live -C directory. For a
    later audit, relocate only that exact live subtree to its retained copy.
    """
    workspace=Path(workspace).resolve() if workspace is not None else None
    retained=Path(retained_workspace).resolve() if retained_workspace is not None else None
    if retained is not None and workspace is None:raise ValueError('review relocation needs the live workspace')
    def resolve(value):
        path=Path(value)
        if not path.is_absolute() and workspace is not None:path=workspace/path
        path=path.resolve()
        if retained is not None and path.is_relative_to(workspace):path=retained/path.relative_to(workspace)
        return str(path)
    commands=[];viewed={resolve(attached_image)} if attached_image else set()
    for line in Path(events_path).read_text().splitlines():
        try:event=json.loads(line)
        except ValueError:continue
        if event.get('type')!='item.completed':continue
        item=event.get('item',{})
        if item.get('type')=='command_execution' and item.get('exit_code')==0:
            command=item.get('command','')
            if isinstance(command,str) and command.strip():commands.append(command)
        if item.get('type')=='mcp_tool_call' and 'view_image' in str(item.get('tool','')) and item.get('status')=='completed':
            arguments=item.get('arguments',{})
            if isinstance(arguments,str):
                try:arguments=json.loads(arguments)
                except ValueError:continue
            if isinstance(arguments,dict) and isinstance(arguments.get('path'),str):viewed.add(resolve(arguments['path']))
    required={resolve(p) for p in image_paths}
    return {'successful_inspection_commands':commands,'viewed_images':sorted(viewed),
            'unviewed_images':sorted(required-viewed),'inspection_observed':bool(commands),
            'all_images_observed':required<=viewed,'semantic_acceptance':'requires-independent-score'}


def canonical_observations(observation,workspace):
    """Store stable workspace-relative image names instead of ephemeral home paths."""
    result=dict(observation);workspace=Path(workspace).resolve()
    for key in ('viewed_images','unviewed_images'):
        result[key]=sorted(Path(p).relative_to(workspace).as_posix() if Path(p).is_relative_to(workspace)
                           else str(Path(p)) for p in result[key])
    return result
