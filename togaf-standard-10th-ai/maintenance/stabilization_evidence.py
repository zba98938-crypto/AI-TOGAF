#!/usr/bin/env python3
"""Explicit-round evidence gates. Reports/ledgers/status never authorize upstream work."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

REPO=Path(__file__).resolve().parents[2]
STAGES=('source_freeze','source_closure','package_verification','engineering_verification',
        'model_evaluation','entrypoint_activation','total_report','ledger','completion_status','final_readonly')
DOWNSTREAM={'stabilization-report/1','stabilization-ledger/1','stabilization-status/1'}


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def safe(name,root=REPO):
    if (not isinstance(name,str) or not name or Path(name).is_absolute()
            or any(p in ('','.','..') for p in name.split('/'))
            or any(c in name for c in ('\\','\x00',':','%'))):
        raise ValueError('noncanonical repository-relative evidence path')
    root=Path(root).resolve();path=root
    for part in Path(name).parts:
        path=path/part
        if path.is_symlink():raise ValueError('evidence symlink is forbidden: '+name)
    if not path.resolve().is_relative_to(root):raise ValueError('evidence path escapes repository')
    return path


def reference(path,root=REPO):
    path=Path(path).resolve()
    return {'path':path.relative_to(root).as_posix(),'sha256':sha(path)}


def verified_file(ref,root=REPO):
    if not isinstance(ref,dict) or set(ref)!={'path','sha256'} or not re.fullmatch('[0-9a-f]{64}',ref.get('sha256','')):
        raise ValueError('invalid evidence reference')
    path=safe(ref['path'],root)
    if not path.is_file():raise ValueError('evidence reference is not a file')
    if sha(path)!=ref['sha256']:raise ValueError('evidence bytes differ: '+ref['path'])
    return path


def read_ref(ref,root=REPO):
    path=verified_file(ref,root)
    return path,json.loads(path.read_text())


def write_new(path,data):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x') as stream:json.dump(data,stream,ensure_ascii=False,indent=2);stream.write('\n')


def freeze(round_id,out,root=REPO,entry_inputs=None):
    root=Path(root).resolve()
    if not re.fullmatch('[A-Za-z0-9_.-]+',round_id):raise ValueError('invalid round_id')
    changed=subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True)
    if changed.strip():raise ValueError('source freeze requires a clean Git checkout')
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
    names=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')[:-1]
    # Packaging manifests and downstream publications are generated after source freeze.
    excluded={'togaf-standard-10th-ai/skills/package-manifest.json',
              'togaf-standard-10th-ai/skills/build-provenance.json',
              'togaf-standard-10th-ai/quality/completion-status.json',
              'togaf-standard-10th-ai/quality/completion-status.md',
              'togaf-standard-10th-ai/quality/implementation-ledger.json',
              'togaf-standard-10th-ai/quality/implementation-ledger.md'}
    files={n:sha(safe(n,root)) for n in names if n not in excluded
           and not n.startswith(('togaf-standard-10th-ai/skills/build-history/',
                                 'togaf-standard-10th-ai/maintenance/stabilization/rounds/'))}
    source_manifest_name='togaf-standard-10th-ai/skills/_shared/standards/sources/manifest.json'
    source_manifest=safe(source_manifest_name,root)
    bound_sources={}
    if source_manifest.is_file():
        for item in json.loads(source_manifest.read_text()):
            if item.get('status') not in ('acquired','derived'):continue
            name=str(Path(source_manifest_name).parent/item['file'])
            path=verified_file({'path':name,'sha256':item['sha256']},root)
            bound_sources[name]={'sha256':sha(path),'bytes':path.stat().st_size}
            files[name]=item['sha256']
    # The live map/catalogue are generated, ignored files. Their exact old bytes
    # are still upstream inputs and must be frozen before a later atomic switch.
    if entry_inputs is not None:
        if (not isinstance(entry_inputs,dict)
                or set(entry_inputs)!={'schema_version','round_id','entries'}
                or entry_inputs['schema_version']!='stabilization-entry-inputs/1'
                or entry_inputs['round_id']!=round_id
                or set(entry_inputs['entries'])!={'current_map','catalogue'}):
            raise ValueError('invalid current-round entry input manifest')
        entries=entry_inputs['entries'];entry_names=[]
        for key,suffix in (('current_map','.json'),('catalogue','.html')):
            ref=entries[key]
            path=verified_file(ref,root)
            if path.suffix!=suffix or not path.is_file():raise ValueError('invalid entry input type')
            if key=='current_map' and not isinstance(json.loads(path.read_text()),dict):raise ValueError('entry map must be an object')
            if ref['path'] in excluded or ref['path'].startswith(('togaf-standard-10th-ai/skills/build-history/',
                    'togaf-standard-10th-ai/maintenance/stabilization/rounds/')):
                raise ValueError('entry input cannot be an excluded downstream publication')
            entry_names.append(ref['path']);files[ref['path']]=ref['sha256']
        if len(set(entry_names))!=2:raise ValueError('entry input paths must be distinct')
    result={'schema_version':'stabilization-source-freeze/1','stage':'source_freeze',
            'round_id':round_id,'source_commit':commit,'passed':bool(files),'files':files,
            'excluded_generated_paths':sorted(excluded),'excluded_generated_prefixes':[
                'togaf-standard-10th-ai/skills/build-history/',
                'togaf-standard-10th-ai/maintenance/stabilization/rounds/']}
    result['bound_standard_materials']=bound_sources
    if entry_inputs is not None:result['entry_inputs']=entry_inputs
    write_new(out,result);return result


def verify_frozen(data,root=REPO,replacements=None):
    files=data.get('files')
    if not isinstance(files,dict) or not files:raise ValueError('empty frozen source map')
    replacements=replacements or {}
    if not set(replacements)<=set(files):raise ValueError('activation replaces a non-frozen input')
    changed=[n for n,digest in files.items() if sha(safe(n,root))!=replacements.get(n,digest)]
    if changed:raise ValueError('frozen source changed: '+', '.join(changed[:10]))
    if (Path(root)/'.git').exists():
        tracked=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')[:-1]
        excluded=set(data.get('excluded_generated_paths',[]));prefixes=data.get('excluded_generated_prefixes',[])
        required={n for n in tracked if n not in excluded and not any(n.startswith(p) for p in prefixes)}
        if not required<=set(files):raise ValueError('frozen source map omits tracked source inputs')
        # Reuse the same exact generated-file scope and rename/untracked checks
        # used by activation, rather than accepting an unchanged HEAD alone.
        checker=Path(__file__).with_name('activate_current_outputs.py')
        spec=importlib.util.spec_from_file_location('_stabilization_activation_identity',checker)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        module.verify_git_identity(Path(root),data['source_commit'],freeze_data=data,
                                   round_id=data['round_id'],replacements=replacements)


def activated_files(round_data,root=REPO,activation=None):
    """Only the two actual, byte-bound entrypoint writes can differ after freeze."""
    if activation is None:
        ref=round_data.get('prerequisites',{}).get('entrypoint_activation')
        if not ref:return {}
        _,envelope=read_ref(ref,root)
        _,activation=read_ref(envelope['evidence'],root)
    if not (activation.get('schema_version')=='current-output-activation/1'
            and activation.get('applied') is True and activation.get('passed') is True
            and activation.get('round_id')==round_data['round_id']
            and activation.get('source_commit')==round_data['source_commit']):
        raise ValueError('activation is not an applied current-round result')
    _,freeze_data=read_ref(round_data['prerequisites']['source_freeze'],root)
    entries=activation.get('entry_files',{})
    if set(entries)!={'current_map','catalogue'}:raise ValueError('activation entry file map incomplete')
    replacements={}
    for key,entry in entries.items():
        name=entry['path']
        if name in replacements or freeze_data['files'].get(name)!=entry['before_sha256']:
            raise ValueError('activation before bytes differ from frozen entrypoint')
        if (activation['before_sha256'][key]!=entry['before_sha256']
                or activation['after_sha256'][key]!=entry['after_sha256']
                or activation['proposed_sha256'][key]!=entry['after_sha256']
                or sha(safe(name,root))!=entry['after_sha256']):
            raise ValueError('activation after bytes differ from actual entrypoint')
        replacements[name]=entry['after_sha256']
    return replacements


def local_gate(name):
    path=Path(__file__).with_name('stabilization_'+name+'_evidence.py')
    spec=importlib.util.spec_from_file_location('_stabilization_'+name+'_evidence',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def review_parser():
    path=Path(__file__).resolve().parents[2]/'tests/enterprise/review_evidence.py'
    spec=importlib.util.spec_from_file_location('_stabilization_review_parser',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def current_source_closure(corpus):
    path=Path(__file__).resolve().parents[1]/'skills/_shared/scripts/source_closure.py'
    if str(path.parent) not in sys.path:sys.path.insert(0,str(path.parent))
    spec=importlib.util.spec_from_file_location('_stabilization_source_closure',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module.verify_source_closure(corpus)


def package_pass(data,root=REPO):
    expected={'extracted-archive-content-hashes','full-retrieval-source-closure','doctor','query',
        'Chinese-body-query','validate','generate-render','policy','ADM-source-steps','ADM-policy-v2-stale',
        'G226-Chinese-body-query','ADM-formal-cycle','ADM-formal-generate','ADM-formal-v2-stale','ADM-flow',
        'native-bpmn-render','native-uml-render','original-project-read-rejected'}
    checks=data.get('checks',[]);names=[r.get('id') for r in checks]
    if (data.get('schema_version')!='portable-runtime-verification/3' or data.get('passed') is not True
            or set(names)!=expected or len(names)!=len(expected) or any(r.get('passed') is not True for r in checks)
            or data.get('counts')!={'checks':len(expected),'passed':len(expected),'failed':0}):return False
    inputs=data.get('input_sha256',{})
    if not inputs:raise ValueError('package verification input bindings missing')
    for name,digest in inputs.items():verified_file({'path':name,'sha256':digest},root)
    releases=[safe(n,root) for n in inputs if n.endswith('/release-manifest.json')]
    if len(releases)!=1:raise ValueError('package verification needs one exact release manifest')
    release_path=releases[0];release=json.loads(release_path.read_text());release_root=release_path.parent
    package=Path(root)/'togaf-standard-10th-ai/skills';manifest_path=package/'package-manifest.json'
    required={release_path,manifest_path}
    for key in ('package','optional_node_dependencies'):
        item=release[key];archive=safe(item['path'],release_root);required.add(archive)
        if sha(archive)!=item['sha256'] or archive.stat().st_size!=item['bytes']:
            raise ValueError('sealed archive bytes differ')
    if {safe(n,root) for n in inputs}!=required:raise ValueError('package verification input set differs from actual release')
    sealed=json.loads(manifest_path.read_text())
    if release['package_manifest_sha256']!=sha(manifest_path):raise ValueError('release source manifest differs')
    checker=Path(__file__).with_name('seal_release.py')
    spec=importlib.util.spec_from_file_location('_stabilization_archive_verifier',checker)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    source_files={r['path']:r for r in sealed['files']}
    if len(source_files)!=len(sealed['files']):raise ValueError('sealed source file identities duplicate')
    actual={p.relative_to(package).as_posix() for p in package.rglob('*') if module.include(p,package)}
    if actual!=set(source_files):raise ValueError('sealed package source file set differs from current source')
    archive_expected={'skills/'+n:r['sha256'] for n,r in source_files.items()}
    archive_expected['skills/package-manifest.json']=sha(manifest_path)
    if not module.verify_archive(release_root/release['package']['path'],archive_expected)['passed']:
        raise ValueError('sealed archive content differs')
    relocated=(Path(root)/'togaf-standard-10th-ai'/data['relocated_directory']).resolve()
    if not relocated.is_dir():raise ValueError('relocated package evidence directory missing')
    for name,record in source_files.items():
        for base in (package,relocated):
            path=verified_file({'path':name,'sha256':record['sha256']},base)
            if path.stat().st_size!=record['bytes']:raise ValueError('sealed/relocated source byte count differs')
    if current_source_closure(relocated/'_shared/corpus').get('passed') is not True:
        raise ValueError('relocated full source closure no longer passes')
    return True


def verify_session_evidence(base,role,session,metadata,expected_workspace,artifacts=None):
    """Bind a completed thread to the exact fixed native command and workspace."""
    if role not in ('actor','scorer'):raise ValueError('invalid session role')
    base=Path(base);directory=base/role;command_path=directory/'command.json'
    command=json.loads(command_path.read_text())
    if command.get('status')!='pass' or command.get('exit_code')!=0:
        raise ValueError('native session command did not pass')
    if any(session.get(k)!=v for k,v in command.items()):raise ValueError('session differs from retained command')
    identity=session.get('execution_identity',{});number=session['session_number']
    name=base.name if role=='actor' else base.name+'-scoring'
    binding=metadata['workspace_bindings'][name]
    live=Path(binding['live_path'])
    if not live.is_absolute() or live!=Path(identity.get('live_workspace','')):
        raise ValueError('session live workspace binding differs')
    if safe(binding['retained_path'],base.parent)!=Path(expected_workspace).resolve():
        raise ValueError('session retained workspace binding differs')
    if (identity.get('role')!=role or identity.get('workspace_name')!=name
            or identity.get('source_commit')!=metadata['source_commit']
            or identity.get('frozen_runtime_manifest_sha256')!=metadata['frozen_runtime_manifest_sha256']):
        raise ValueError('session role/version binding differs')
    for key,filename in (('command_sha256','command.json'),('events_sha256','stdout.jsonl'),
                         ('schema_sha256','schema.json'),('prompt_sha256','prompt.txt')):
        if identity.get(key)!=sha(directory/filename):raise ValueError('session retained bytes differ: '+filename)
    argv=command.get('argv',[])
    binary=metadata['codex_binary']
    if not argv or str(Path(argv[0]).resolve())!=binary['path']:
        raise ValueError('session native executable differs')
    if sha(Path(binary['path']))!=binary['sha256']:raise ValueError('session native executable bytes changed')
    private=live.parents[1]/'sessions'/str(number)
    expected=[argv[0],'--no-daemon','-a','never','-c','default_permissions='+json.dumps('enterprise-'+role),
              '-c','shell_environment_policy.set.TMPDIR='+json.dumps(str(live/'.tmp')),
              'exec','--ephemeral','--json','--ignore-rules','--skip-git-repo-check','-C',str(live),
              '--output-schema',str(private/'schema.json'),'--output-last-message',str(private/'final.json'),
              '--color','never']
    image=identity.get('attached_image')
    if image is not None:
        if role!='scorer':raise ValueError('business Actor was given a scoring image')
        saved=safe(image,expected_workspace)
        if not image.startswith('actual-output/') or not artifacts or image.removeprefix('actual-output/') not in artifacts:
            raise ValueError('scorer attachment is not an actual delivered artifact')
        record=artifacts[image.removeprefix('actual-output/')]
        if saved.suffix.lower()!='.png' or sha(saved)!=record['sha256'] or saved.stat().st_size!=record['bytes']:
            raise ValueError('scorer attachment bytes differ')
        expected+=['--image',str(live/image)]
    expected+=['-']
    if argv!=expected:raise ValueError('native session command/permissions differ')
    thread=review_parser().thread_identity(directory/'stdout.jsonl')
    if identity.get('thread_id')!=thread:raise ValueError('session thread differs from retained events')
    events=[]
    for line in (directory/'stdout.jsonl').read_text().splitlines():
        try:events.append(json.loads(line))
        except ValueError:continue
    stats={'event_count':len(events),'usage':[e['usage'] for e in events if 'usage' in e],
           'command_event_count':sum(e.get('item',{}).get('type')=='command_execution' for e in events),
           'tool_event_count':sum(e.get('item',{}).get('type') in ('command_execution','mcp_tool_call','file_change','web_search') for e in events)}
    if any(session.get(k)!=v for k,v in stats.items()):raise ValueError('session event/usage statistics differ')
    return thread,saved if image is not None else None


def verify_review_observations(base,row,artifacts,scoring_root,scorer_session):
    parser=review_parser();identity=scorer_session['execution_identity']
    for name,record in artifacts.items():
        path=safe('actual-output/'+name,scoring_root)
        if sha(path)!=record['sha256'] or path.stat().st_size!=record['bytes']:
            raise ValueError('independent scorer inspected changed artifact bytes: '+name)
    observation=parser.observed_review(Path(base)/'scorer/stdout.jsonl',
        [Path(scoring_root)/'actual-output'/name for name in artifacts if Path(name).suffix.lower()=='.png'],
        identity.get('attached_image'),workspace=identity['live_workspace'],retained_workspace=scoring_root)
    observation=parser.canonical_observations(observation,scoring_root)
    if observation!=row.get('review_observations'):raise ValueError('claimed review differs from retained inspection/image events')
    if row.get('status')=='pass' and (not observation['inspection_observed'] or not observation['all_images_observed']):
        raise ValueError('passing review lacks actual inspection/image events')
    return observation


def model_evidence(path,data,root=REPO,source_commit=None):
    """Recount the 507 unique cases and verify retained Actor/scorer/output bytes."""
    directory=Path(path).parent
    inventory=json.loads((directory/'coverage-inventory.json').read_text())
    expected_rows={r['id']:r for r in inventory['native_cases']}
    expected=set(expected_rows)
    rows=data.get('rows',[]);ids=[r.get('id') for r in rows]
    issues=[];executed=0;passes=0;all_sessions=set();all_threads=set()
    if len(expected)!=507 or len(inventory['native_cases'])!=507 or len(ids)!=len(set(ids)) or set(ids)!=expected:issues.append('507-unique-case-set-mismatch')
    revision_path=directory/'source-sha256.json'
    try:
        revision=json.loads(revision_path.read_text())
        if not revision:raise ValueError('empty campaign source map')
        for name,digest in revision.items():
            if sha(safe(name,root))!=digest:raise ValueError('campaign revision changed: '+name)
    except (OSError,ValueError) as exc:
        issues.append(str(exc));revision={}
    settings=None;runtime_cache={}
    for row in rows:
        if row.get('status')=='uncovered':continue
        candidates=list(directory.glob('agents-*/'+str(row['id'])+'/result.json'))
        match=next((p for p in candidates if json.loads(p.read_text())==row),None)
        if match is None:issues.append(str(row['id'])+': missing exact retained result');continue
        base=match.parent
        try:
            runtime=base.parent
            if runtime not in runtime_cache:
                metadata=json.loads((runtime/'runtime.json').read_text())
                frozen_path=runtime/'frozen-runtime-manifest.json'
                frozen=json.loads(frozen_path.read_text())
                if metadata['frozen_runtime_manifest_sha256']!=sha(frozen_path):raise ValueError('retained frozen runtime differs')
                if frozen.get('source_hashes')!=frozen.get('frozen_hashes') or not frozen.get('dependency_hashes'):
                    raise ValueError('frozen source/dependency binding incomplete')
                if frozen['source_hashes']!={n.removeprefix('togaf-standard-10th-ai/skills/'):v for n,v in revision.items() if n.startswith('togaf-standard-10th-ai/skills/')}:
                    raise ValueError('runtime source does not match campaign revision')
                if source_commit and metadata.get('source_commit')!=source_commit:raise ValueError('runtime commit differs from frozen round')
                current_settings={k:metadata.get(k) for k in ('model','provider','model_reasoning_effort','service_tier','disable_response_storage','source_config_sha256')}
                if not all(current_settings[k] for k in ('model','provider','source_config_sha256')):raise ValueError('configured model provenance missing')
                if settings is not None and current_settings!=settings:raise ValueError('model settings changed between batches')
                settings=current_settings
                if metadata.get('render_mode')=='controlled-local':
                    cleanup=metadata.get('controlled_renderer_cleanup',{})
                    if not metadata.get('render_admission_sha256') or not cleanup.get('all_tasks_cleaned') or not cleanup.get('private_directory_cleaned'):
                        raise ValueError('controlled renderer admission/cleanup not retained')
                runtime_cache[runtime]=(metadata,frozen)
            metadata,_=runtime_cache[runtime]
            binding=json.loads((base/'case-binding.json').read_text())
            for field in ('id','kind','target','owner'):
                if binding[field]!=expected_rows[row['id']][field]:raise ValueError('case identity differs: '+field)
            expected_case=expected_rows[row['id']]
            if (hashlib.sha256(binding['request'].encode()).hexdigest()!=expected_case['request_sha256']
                    or binding['raw_input_sha256']!=expected_case['raw_input_sha256']):
                raise ValueError('case request/original input differs from source-derived inventory')
            if binding.get('source_commit')!=metadata.get('source_commit') or binding.get('frozen_runtime_manifest_sha256')!=metadata['frozen_runtime_manifest_sha256']:
                raise ValueError('case version binding differs')
            actor=json.loads((base/'actor/session.json').read_text())
            scorer=json.loads((base/'scorer/session.json').read_text())
            numbers=(actor['session_number'],scorer['session_number'])
            if any(not isinstance(n,int) or isinstance(n,bool) or n<1 for n in numbers) or numbers[0]==numbers[1] or any(n in all_sessions for n in numbers):raise ValueError('Actor/scorer session identity reused')
            all_sessions.update(numbers)
            if actor['exit_code']!=0 or scorer['exit_code']!=0:raise ValueError('session did not complete')
            if row.get('actor')!=actor or row.get('scorer')!=scorer:raise ValueError('session result binding differs')
            artifacts=json.loads((base/'artifact-index.json').read_text())
            for name,record in artifacts.items():
                item=safe(name,base/'workspace')
                if sha(item)!=record['sha256'] or item.stat().st_size!=record['bytes']:raise ValueError('saved artifact differs: '+name)
            if 'raw-input.json' not in artifacts:raise ValueError('original Actor input missing')
            if artifacts['raw-input.json']['sha256']!=binding['raw_input_sha256']:raise ValueError('Actor changed original input')
            scoring_root=runtime/(str(row['id'])+'-scoring')/'workspace'
            actor_thread,_=verify_session_evidence(base,'actor',actor,metadata,base/'workspace')
            scorer_thread,image=verify_session_evidence(base,'scorer',scorer,metadata,scoring_root,artifacts)
            if actor_thread==scorer_thread or any(t in all_threads for t in (actor_thread,scorer_thread)):
                raise ValueError('Actor/scorer native thread identity reused')
            all_threads.update((actor_thread,scorer_thread))
            rubric=json.loads((scoring_root/'rubric.json').read_text())
            if review_parser().saved_json_hash(rubric.get('rubric'))!=expected_case['rubric_sha256']:
                raise ValueError('independent rubric differs from source-derived inventory')
            if rubric.get('artifact_index')!=artifacts or rubric.get('business_request')!=binding['request']:
                raise ValueError('retained independent rubric differs')
            for field,key in (('kind','case_kind'),('target','expected_route'),('owner','owner')):
                if rubric.get(key)!=binding[field]:raise ValueError('scoring case identity differs')
            if sha(scoring_root/'actual-output/raw-input.json')!=binding['raw_input_sha256']:
                raise ValueError('scorer original input differs')
            if sha(scoring_root/'actor-events.jsonl')!=sha(base/'actor/stdout.jsonl'):
                raise ValueError('scorer inspected different Actor events')
            if not (base/'actor/stdout.jsonl').is_file() or not (base/'scorer/stdout.jsonl').is_file():raise ValueError('tool events missing')
            scorer_final=json.loads((base/'scorer/final.json').read_text())
            if scorer_final!=row.get('scorer_output'):raise ValueError('raw independent scoring result differs')
            if json.loads((base/'actor/final.json').read_text())!=row.get('actor_output'):
                raise ValueError('raw Actor result differs')
            observation=verify_review_observations(base,row,artifacts,scoring_root,scorer)
            saved=[n for n in artifacts if n not in ('raw-input.json','AGENTS.md')]
            if set(saved)!=set(row.get('saved_artifacts',[])):raise ValueError('actual saved artifacts differ')
            parser=review_parser();derived=json.loads(json.dumps(scorer_final))
            status=parser.reviewed_status(derived,row['kind'],saved,has_image=image is not None)
            if status=='pass' and (not observation['inspection_observed'] or not observation['all_images_observed']):
                status='needs_review'
                derived['reason']+='; runtime events do not establish evidence inspection and viewing of every delivered image'
            if status!=row.get('status') or derived!=row.get('score'):
                raise ValueError('derived independent verdict differs from retained evidence')
            executed+=1;passes+=row.get('status')=='pass'
        except (OSError,ValueError,KeyError,TypeError) as exc:issues.append(str(row['id'])+': '+str(exc))
    return {'required_items':507,'executed_items':executed,'passed_items':passes,
            'unexecuted_items':507-executed,'actor_scorer_independent':not issues and executed==507,
            'model_settings':settings,'source_revision_sha256':sha(revision_path) if revision_path.is_file() else None,
            'issues':issues,'passed':data.get('status')=='pass' and executed==passes==507 and not issues}


def record(round_data,stage,evidence,out,root=REPO):
    if stage not in STAGES[1:6]:raise ValueError('unsupported execution stage')
    evidence_path=Path(evidence).resolve();data=json.loads(evidence_path.read_text())
    if data.get('schema_version') in DOWNSTREAM:raise ValueError('downstream report cannot authorize an upstream stage')
    replacements=activated_files(round_data,root,data) if stage=='entrypoint_activation' else {}
    refs=round_data.get('prerequisites',{})
    for previous in STAGES[:STAGES.index(stage)]:
        checked=verified_stage(refs[previous],previous,round_data,root,replacements)
        if checked.get('passed') is not True:raise ValueError('upstream stage not passed for this round: '+previous)
    passed,detail=validate_execution(stage,evidence_path,data,round_data,root)
    result={'schema_version':'stabilization-execution-stage/1','stage':stage,'round_id':round_data['round_id'],
            'source_commit':round_data['source_commit'],'passed':passed,'evidence':reference(evidence_path,root),**detail}
    write_new(out,result);return result


def validate_execution(stage,path,data,round_data,root=REPO):
    """Pure execution gate reused by records, reports and final read-only checks."""
    if data.get('schema_version') in DOWNSTREAM:raise ValueError('downstream publication is not execution evidence')
    detail={}
    if stage=='source_closure':
        passed=data.get('schema_version')=='retrieval-source-closure/1' and data.get('passed') is True and data.get('counts',{}).get('issues')==0 and data.get('counts',{}).get('records',0)>0
        corpus=Path(root)/'togaf-standard-10th-ai/skills/_shared/corpus'
        if data!=current_source_closure(corpus):raise ValueError('source closure differs from actual full-index check')
        for name,digest in data.get('input_sha256',{}).items():
            if sha(safe(name,corpus))!=digest:raise ValueError('source closure input changed: '+name)
    elif stage=='package_verification':
        passed=package_pass(data,root)
    elif stage=='engineering_verification':passed=local_gate('engineering').engineering_pass(path,data,root)
    elif stage=='model_evaluation':detail=model_evidence(path,data,root,round_data['source_commit']);passed=detail['passed']
    elif stage=='entrypoint_activation':
        activated_files(round_data,root,data)
        passed=data.get('applied') is True and data.get('passed') is True and data.get('round_id')==round_data['round_id']
    else:raise ValueError('unsupported execution stage')
    return passed,detail


def verified_stage(ref,stage,round_data,root=REPO,replacements=None):
    _,data=read_ref(ref,root)
    if data.get('stage')!=stage or data.get('round_id')!=round_data['round_id'] or data.get('source_commit')!=round_data['source_commit']:
        raise ValueError('execution stage/round/revision differs')
    if stage=='source_freeze':
        if data.get('schema_version')!='stabilization-source-freeze/1':raise ValueError('invalid source freeze schema')
        verify_frozen(data,root,replacements)
        if data.get('passed') is not True:raise ValueError('source freeze did not pass')
    else:
        if data.get('schema_version')!='stabilization-execution-stage/1':raise ValueError('execution envelope schema differs')
        path,raw=read_ref(data['evidence'],root)
        passed,detail=validate_execution(stage,path,raw,round_data,root)
        if data.get('passed')!=passed or any(data.get(k)!=v for k,v in detail.items()):
            raise ValueError('execution envelope differs from actual evidence')
    return data


def assess_report(round_data,root=REPO):
    """Produce a stage assessment even when necessary execution is still pending."""
    rows=[]
    try:replacements=activated_files(round_data,root);activation_error=None
    except (OSError,ValueError,KeyError,TypeError) as exc:replacements={};activation_error=str(exc)
    for stage in STAGES[:6]:
        ref=round_data.get('prerequisites',{}).get(stage)
        if ref is None:rows.append({'stage':stage,'status':'pending','passed':False});continue
        try:
            data=verified_stage(ref,stage,round_data,root,replacements)
            if stage=='entrypoint_activation' and activation_error:raise ValueError(activation_error)
            rows.append({'stage':stage,'passed':data.get('passed') is True,'status':'pass' if data.get('passed') is True else 'incomplete','evidence':ref})
        except (OSError,ValueError,KeyError) as exc:rows.append({'stage':stage,'status':'invalid','passed':False,'reason':str(exc),'evidence':ref})
    standards=round_data.get('standard_capabilities',{})
    standard_complete=False;standard_checks={}
    if standards:
        try:standard_complete,standard_checks=local_gate('standard').standard_checks(round_data,root)
        except (OSError,ValueError,KeyError,TypeError,ImportError) as exc:standard_checks={'error':str(exc)}
    material_check={'complete':False,'status':'pending','required_units':None,'reviewed_units':0}
    material_ref=round_data.get('material_review')
    if material_ref:
        try:
            _,materials=read_ref(material_ref,root)
            _,inventory=read_ref(materials['source_unit_inventory'],root)
            material_check={'complete':False,'status':'uncovered',
                'required_units':len(inventory.get('units',[])),'reviewed_units':0,'evidence':material_ref,
                'reason':'Native material review result collection and execution verification are not implemented in this revision.'}
        except (OSError,ValueError,KeyError,TypeError) as exc:
            material_check={'complete':False,'status':'invalid','reason':str(exc),'evidence':material_ref}
    result={'schema_version':'stabilization-report/1','round_id':round_data['round_id'],
            'stage':'total_report','source_commit':round_data['source_commit'],'stages':rows,'standard_capabilities':standards,
            'standard_checks':standard_checks,
            'material_review':material_check,'source_material_review_complete':material_check['complete'],
            'engineering_stable':all(r['passed'] for r in rows[:4]),
            'standard_capabilities_complete':standard_complete,
            'technical_scope_complete':all(r['passed'] for r in rows) and standard_complete and material_check['complete'],
            'independent_model_review':'recorded separately from human acceptance',
            'human_professional_acceptance':'pending_signature','real_organization_approval':'pending_signature',
            'all_work_complete':False,'input_round_manifest':'explicit; no historical default directory'}
    return result


def report(round_data,out,root=REPO):
    result=assess_report(round_data,root);write_new(out,result);return result


def publication(ref,round_data,schema,stage,root=REPO):
    path,data=read_ref(ref,root)
    if (data.get('schema_version')!=schema or data.get('stage')!=stage
            or data.get('round_id')!=round_data['round_id']
            or data.get('source_commit')!=round_data['source_commit']):
        raise ValueError('publication belongs to another stage/round/revision: '+stage)
    return path,data


def build_ledger(round_data,root=REPO):
    ref=round_data['prerequisites']['total_report']
    _,data=publication(ref,round_data,'stabilization-report/1','total_report',root)
    if data!=assess_report(round_data,root):raise ValueError('report differs from canonical upstream assessment')
    requirements=[{'id':r['stage'],'status':r['status'],'passed':r['passed'],'evidence':r.get('evidence')} for r in data['stages']]
    for language in ('uml','bpmn'):
        complete=data.get('standard_checks',{}).get(language,{}).get('complete') is True
        requirements.append({'id':language+'-complete-design-time','status':'pass' if complete else 'incomplete','passed':complete,'evidence':data.get('standard_capabilities',{}).get(language)})
    complete=data.get('source_material_review_complete') is True
    requirements.append({'id':'independent-source-material-review','status':'pass' if complete else 'incomplete','passed':complete,'evidence':data.get('material_review',{}).get('evidence')})
    pack_ref=round_data.get('acceptance_pack');pack_ready=False
    if pack_ref:
        pack=verified_acceptance_pack(pack_ref,round_data,root)
        pack_ready=pack.get('ready_for_signature') is True
    requirements.append({'id':'pending-signature-business-acceptance-pack','status':'pass' if pack_ready else 'incomplete','passed':pack_ready,'evidence':pack_ref})
    for requirement in requirements:
        if requirement['evidence']:read_ref(requirement['evidence'],root)
    result={'schema_version':'stabilization-ledger/1','stage':'ledger','round_id':round_data['round_id'],
            'source_commit':round_data['source_commit'],'total_report':ref,'requirements':requirements,
            'engineering_stable':data.get('engineering_stable') is True,
            'technical_delivery_complete':all(r['passed'] for r in requirements),
            'real_organization_approval':'pending_signature','human_professional_acceptance':'pending_signature',
            'upstream_evidence_is_read_only':True}
    return result


def ledger(round_data,out,root=REPO):
    result=build_ledger(round_data,root);write_new(out,result);return result


def build_status(round_data,root=REPO):
    ref=round_data['prerequisites']['ledger']
    _,data=publication(ref,round_data,'stabilization-ledger/1','ledger',root)
    if data!=build_ledger(round_data,root):raise ValueError('ledger differs from canonical complete requirement set')
    publication(data['total_report'],round_data,'stabilization-report/1','total_report',root)
    for item in data['requirements']:
        if item.get('evidence'):read_ref(item['evidence'],root)
    complete=data.get('technical_delivery_complete') is True and all(i['passed'] is True for i in data['requirements'])
    result={'schema_version':'stabilization-status/1','stage':'completion_status','round_id':round_data['round_id'],
            'source_commit':round_data['source_commit'],'ledger':ref,'engineering_stable':data.get('engineering_stable') is True,
            'technical_delivery_complete':complete,'all_requested_delivery_complete':complete,
            'human_professional_acceptance':'pending_signature','real_organization_approval':'pending_signature',
            'organization_approval_complete':False,'unfinished_requirements':[i['id'] for i in data['requirements'] if not i['passed']]}
    return result


def completion_status(round_data,out,root=REPO):
    result=build_status(round_data,root);write_new(out,result);return result


def build_acceptance_pack(round_data,root=REPO):
    """Derive readiness from actual current materials, keeping signatures pending."""
    report_ref=round_data['prerequisites']['total_report']
    _,data=publication(report_ref,round_data,'stabilization-report/1','total_report',root)
    if data!=assess_report(round_data,root):raise ValueError('acceptance report differs from canonical upstream assessment')
    materials=round_data.get('acceptance_materials',[])
    if not isinstance(materials,list):raise ValueError('acceptance materials must be a list')
    required={'reproduction','sources','decisions','deliverables','exception_paths','evaluation_results'}
    roles=set()
    for item in materials:
        if (not isinstance(item,dict) or set(item)!={'role','description','evidence'}
                or item['role'] not in required or not isinstance(item['description'],str)
                or not item['description'].strip()):raise ValueError('invalid acceptance material')
        path=verified_file(item['evidence'],root)
        if not path.stat().st_size:raise ValueError('acceptance material is empty: '+item['evidence']['path'])
        if path.suffix.lower()=='.json':
            material=json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(material,(dict,list)) or not material:
                raise ValueError('acceptance JSON material has no substantive records: '+item['evidence']['path'])
        elif path.suffix.lower() in {'.md','.txt','.html','.csv','.tsv'}:
            if not path.read_text(encoding='utf-8').strip():
                raise ValueError('acceptance text material is empty: '+item['evidence']['path'])
        roles.add(item['role'])
    result={'schema_version':'business-acceptance-pack/1','stage':'business_acceptance_pack',
            'round_id':round_data['round_id'],'source_commit':round_data['source_commit'],'total_report':report_ref,
            'materials':materials,'missing_material_roles':sorted(required-roles),
            'technical_scope_complete':data.get('technical_scope_complete') is True,
            'ready_for_signature':required<=roles and data.get('technical_scope_complete') is True,
            'independent_model_review':'recorded in technical evidence; not a human signature',
            'signatures':{'professional_reviewer':None,'business_owner':None,'organization_authority':None},
            'real_organization_approval':'pending_signature'}
    return result


def acceptance_pack_markdown(data):
    """The six material references and the three unsigned rows are authoritative."""
    report_ref=data['total_report']
    markdown=['# 待签署业务验收包','',f'轮次：`{data["round_id"]}`；冻结源码：`{data["source_commit"]}`。','',
              '独立模型复核、人工专业验收与真实组织批准分别记录。本包未授予真实组织批准。','',
              '技术范围状态：'+('满足本轮验收门禁' if data.get('technical_scope_complete') else '仍有未完成门禁，见总报告')+'。','',
              f'- 总报告：`{report_ref["path"]}`，SHA-256 `{report_ref["sha256"]}`。']
    for item in data['materials']:
        description=item['description'].replace('\r',' ').replace('\n',' ')
        markdown.append(f'- {item["role"]}：{description}；`{item["evidence"]["path"]}`；SHA-256 `{item["evidence"]["sha256"]}`。')
    markdown+=['','异常与未完成项须先复现、定位、记录决定，再按新源码版本重验；旧版本结果保留，不计入新版本覆盖。','',
               '| 签署职责 | 姓名/职务 | 审核意见及范围 | 日期 | 签名 |','|---|---|---|---|---|',
               '| 人工专业验收 | 待填写 | 待填写 | 待填写 | 待签署 |',
               '| 业务负责人验收 | 待填写 | 待填写 | 待填写 | 待签署 |',
               '| 真实组织批准 | 待填写 | 待填写 | 待填写 | 待签署 |','']
    return '\n'.join(markdown)


def verified_acceptance_pack(ref,round_data,root=REPO):
    """Neither a ready label nor a copied signing sheet can authorize the pack."""
    path,data=publication(ref,round_data,'business-acceptance-pack/1','business_acceptance_pack',root)
    expected=build_acceptance_pack(round_data,root)
    if data!=expected:raise ValueError('acceptance pack differs from canonical materials/report/readiness')
    markdown_name=path.with_suffix('.md').relative_to(Path(root).resolve()).as_posix()
    markdown_path=safe(markdown_name,root)
    if markdown_path==path or not markdown_path.is_file():raise ValueError('acceptance signing sheet is missing')
    if markdown_path.read_bytes()!=acceptance_pack_markdown(expected).encode('utf-8'):
        raise ValueError('acceptance material references or unsigned signing sheet differ')
    return data


def acceptance_pack(round_data,out,root=REPO):
    """Generate both canonical records before any professional signature."""
    result=build_acceptance_pack(round_data,root)
    out=Path(out)
    markdown_path=Path(out).with_suffix('.md')
    if out==markdown_path or out.exists() or markdown_path.exists():
        raise FileExistsError('acceptance JSON or signing sheet already exists')
    write_new(out,result)
    with markdown_path.open('x',encoding='utf-8') as stream:stream.write(acceptance_pack_markdown(result))
    return result


def final_readonly(round_data,out,root=REPO):
    """Read the one-way evidence graph. Only the new verification result is written."""
    refs=round_data['prerequisites'];checks=[];canonical_report=None;canonical_status=None
    replacements=activated_files(round_data,root)
    for stage in STAGES[:-1]:
        if stage not in refs:
            checks.append({'stage':stage,'passed':False,'reason':'missing current-round evidence'});continue
        try:
            _,data=read_ref(refs[stage],root)
            if data.get('stage')!=stage or data.get('round_id')!=round_data['round_id'] or data.get('source_commit')!=round_data['source_commit']:
                raise ValueError('stage/round/revision differs')
            if stage=='source_freeze':verified_stage(refs[stage],stage,round_data,root,replacements)
            if stage in STAGES[1:6]:
                verified_stage(refs[stage],stage,round_data,root,replacements)
                if data.get('passed') is not True:raise ValueError('execution stage did not pass')
            elif stage=='total_report':
                if data!=assess_report(round_data,root):raise ValueError('final report differs from canonical upstream assessment')
                for row in data['stages']:
                    if row.get('evidence')!=refs.get(row['stage']):raise ValueError('report upstream reference differs')
                canonical_report=data
            elif stage=='ledger':
                if data!=build_ledger(round_data,root):raise ValueError('final ledger differs from canonical requirement set')
                if data['total_report']!=refs['total_report']:raise ValueError('ledger report reference differs')
                for row in data['requirements']:
                    if row.get('evidence'):read_ref(row['evidence'],root)
            elif stage=='completion_status':
                if data!=build_status(round_data,root):raise ValueError('final status differs from canonical upstream assessment')
                if data['ledger']!=refs['ledger']:raise ValueError('status ledger reference differs')
                _,ledger_data=read_ref(refs['ledger'],root)
                if data['technical_delivery_complete']!=ledger_data['technical_delivery_complete']:raise ValueError('completion contradicts ledger')
                canonical_status=data
            checks.append({'stage':stage,'passed':True,'evidence':refs[stage]})
        except (OSError,ValueError,KeyError,TypeError) as exc:
            if stage in ('total_report','ledger','completion_status'):raise ValueError('invalid downstream publication: '+str(exc)) from exc
            checks.append({'stage':stage,'passed':False,'reason':str(exc)})
    graph_complete=len(checks)==len(STAGES)-1 and all(c['passed'] for c in checks)
    scope_complete=canonical_report is not None and canonical_report.get('technical_scope_complete') is True
    delivery_complete=graph_complete and scope_complete and canonical_status is not None and canonical_status.get('technical_delivery_complete') is True
    result={'schema_version':'stabilization-final-readonly/1','stage':'final_readonly','round_id':round_data['round_id'],
            'source_commit':round_data['source_commit'],'passed':graph_complete,
            'graph_integrity_complete':graph_complete,'technical_scope_complete':scope_complete,
            'technical_delivery_complete':delivery_complete,'all_requested_delivery_complete':delivery_complete,
            'unfinished_requirements':canonical_status['unfinished_requirements'] if canonical_status is not None else ['completion-status-not-verified'],
            'passed_scope':'read-only evidence graph integrity; technical delivery is recorded separately',
            'checks':checks,'upstream_writes':0,'human_professional_acceptance':'pending_signature','real_organization_approval':'pending_signature'}
    write_new(out,result);return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    freeze_parser=sub.add_parser('freeze');freeze_parser.add_argument('--round-id',required=True);freeze_parser.add_argument('--out',type=Path,required=True)
    freeze_parser.add_argument('--entry-inputs',type=Path,required=True,
                               help='Explicit two-entry before-byte manifest for this round')
    for name in ('record','report','ledger','status','acceptance-pack','final-readonly'):
        p=sub.add_parser(name);p.add_argument('--round',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
        if name=='record':p.add_argument('--stage',choices=STAGES[1:6],required=True);p.add_argument('--evidence',type=Path,required=True)
    args=parser.parse_args()
    if args.command=='freeze':result=freeze(args.round_id,args.out,entry_inputs=json.loads(args.entry_inputs.read_text()))
    else:
        data=json.loads(args.round.read_text())
        commands={'report':report,'ledger':ledger,'status':completion_status,'acceptance-pack':acceptance_pack,'final-readonly':final_readonly}
        result=record(data,args.stage,args.evidence,args.out) if args.command=='record' else commands[args.command](data,args.out)
    print(json.dumps({k:v for k,v in result.items() if k not in {'files','stages'}},ensure_ascii=False))
    return 0 if args.command in ('report','ledger','status','acceptance-pack') or result.get('passed') is True else 3


if __name__=='__main__':raise SystemExit(main())
