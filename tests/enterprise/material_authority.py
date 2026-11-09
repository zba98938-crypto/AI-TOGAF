"""Upstream source freeze and controller admission for native material review.

Checks retain provenance from the existing NativeAgents controller. They do not
authenticate an adversarial host owner or grant semantic/professional approval.
"""
import copy
import importlib.util
import json
import os
from pathlib import Path
import shlex
import shutil
import struct
import sys
import zlib

from .runtime import Blocked, sha256

SOURCE_FILES = (
    'tests/enterprise/material_review.py',
    'tests/enterprise/material_authority.py',
    'tests/enterprise/agents.py',
    'tests/enterprise/frozen_runtime.py',
    'tests/enterprise/runtime.py',
    'tests/enterprise/review_evidence.py',
    'togaf-standard-10th-ai/maintenance/stabilization_material_evidence.py',
    'togaf-standard-10th-ai/maintenance/stabilization_evidence.py',
    'togaf-standard-10th-ai/maintenance/build_material_review_inventory.py',
    'togaf-standard-10th-ai/maintenance/material_source_adapters.py',
    'togaf-standard-10th-ai/maintenance/material_visual_sources.py',
)
RUNTIME_FILES = {'schema.json', 'prompt.txt', 'command.json', 'stdout.jsonl',
                 'stderr.log', 'session.json', 'final.json'}
MODEL_KEYS = ('model', 'provider', 'model_reasoning_effort', 'service_tier',
              'disable_response_storage', 'source_config_sha256')


def admission_file_names(admission):
    """Only upstream preflight bytes; no material review results are inputs."""
    names = {'preflight.json','toolchain-preflight.json','frozen-runtime-manifest.json',
             'material-review-admission-image.png'}
    for session in ('preflight','image-preflight'):
        names.update(session+'/actor/'+name for name in RUNTIME_FILES)
    for probe in set(admission['toolchain']['probes']) | {'read-firewall-probe','allowed-skill-probe'}:
        names.update(probe+'/'+name for name in ('command.json','stderr.log'))
        names.add(probe+'/stdout.log' if probe.startswith('scorer-') else probe+'/stdout.jsonl')
    return names


def _red_png():
    def chunk(kind,data):
        return struct.pack('!I',len(data))+kind+data+struct.pack('!I',zlib.crc32(kind+data)&0xffffffff)
    pixels = b''.join(b'\x00'+b'\xff\x00\x00'*16 for _ in range(16))
    return (b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('!2I5B',16,16,8,2,0,0,0))
            +chunk(b'IDAT',zlib.compress(pixels))+chunk(b'IEND',b''))


def verify_probe_command(name, detail, command, expected_argv, *, denied=False, read_only=False):
    """Inspect actual fixed invocation atoms; booleans are not exit codes."""
    argv = command.get('argv')
    if (not isinstance(argv,list) or not argv or any(not isinstance(v,str) or not v for v in argv)
            or argv != expected_argv or detail.get('argv') != argv
            or type(command.get('exit_code')) is not int or type(detail.get('exit_code')) is not int
            or detail['exit_code'] != command['exit_code']
            or (command['exit_code'] == 0) == denied
            or detail.get('status') != 'pass'
            or type(detail.get('timeout',False)) is not bool or detail.get('timeout',False)
            or type(command.get('timeout',False)) is not bool or command.get('timeout',False)):
        raise ValueError('material native admission probe lacks a fixed completed command: '+name)
    if read_only:
        # Existing read-only probes use subprocess.PIPE and retain argv,
        # exit_code and timeout, without run_command's status/seconds fields.
        if command.get('timeout') is not False or command.get('status') is not None:
            raise ValueError('material read-only native probe receipt differs: '+name)
    elif command.get('status') != ('fail' if denied else 'pass'):
        raise ValueError('material native probe execution status differs: '+name)


def _review():
    from . import material_review
    return material_review


def _inventory_module():
    m = _review()
    path = m.REPO / 'togaf-standard-10th-ai/maintenance/build_material_review_inventory.py'
    directory = str(path.parent)
    if directory not in sys.path:
        sys.path.insert(0, directory)
    spec = importlib.util.spec_from_file_location('_material_authoritative_inventory', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verified_acquisition(inputs, root, visual_source_manifest=None):
    """Rebuild the acquired corpus, including all raw/visual/candidate units."""
    m = _review()
    visual = m.verify_ref(visual_source_manifest, root) if visual_source_manifest else None
    builder = _inventory_module().Inventory(root, visual_source_manifest=visual)
    actual = builder.build()
    if actual != inputs.inventory:
        raise ValueError('material acquisition differs from full current source reconstruction')
    if not inputs.full_source_scope:
        raise ValueError('material acquisition does not contain the required full source scope')
    # Preparation is generated from the same real candidates, not invented text.
    for _, shard in inputs.shards.values():
        for identity, context in shard['candidate_translation_context'].items():
            if context != builder.contexts.get(identity):
                raise ValueError('material candidate differs from reconstructed source alignment')
    return actual


def required_freeze_refs(input_manifest_ref, root, visual_source_manifest=None):
    """Enumerate upstream inputs only; never include review sessions/results."""
    m = _review()
    root = Path(root).resolve()
    inputs = m.ReviewInputs(input_manifest_ref, root)
    verified_acquisition(inputs, root, visual_source_manifest)
    references = dict(inputs.all_refs)
    if visual_source_manifest:
        m.verify_ref(visual_source_manifest, root)
        references[visual_source_manifest['path']] = visual_source_manifest['sha256']
    for name in SOURCE_FILES:
        references[name] = sha256(m.safe(name, root))
    return references


def _preflight_session(directory, name, metadata, detail, frozen):
    """Verify native preflight raw bytes, including its allowed Actor image."""
    m = _review()
    base = directory / name / 'actor'
    for filename in RUNTIME_FILES:
        m.safe((base / filename).relative_to(directory).as_posix(), directory)
        if not (base / filename).is_file():
            raise ValueError('material admission lacks original native preflight files')
    session = m.load(base / 'session.json')
    command = m.load(base / 'command.json')
    if (detail != session or command.get('status') != 'pass'
            or type(command.get('exit_code')) is not int or command['exit_code'] != 0):
        raise ValueError('material admission preflight result differs from raw native session')
    if any(session.get(k) != v for k, v in command.items()):
        raise ValueError('material admission preflight command differs')
    identity = session['execution_identity']
    live = Path(identity['live_workspace'])
    if (not live.is_absolute() or identity['role'] != 'actor' or identity['workspace_name'] != name
            or identity['source_commit'] != metadata['source_commit']
            or identity['frozen_runtime_manifest_sha256'] != metadata['frozen_runtime_manifest_sha256']
            or type(session['session_number']) is not int or session['session_number'] < 1):
        raise ValueError('material admission preflight execution identity differs')
    for key, filename in (('schema_sha256','schema.json'), ('prompt_sha256','prompt.txt'),
                          ('command_sha256','command.json'), ('events_sha256','stdout.jsonl')):
        if identity[key] != sha256(base / filename):
            raise ValueError('material admission preflight bytes changed')
    private = live.parents[1] / 'sessions' / str(session['session_number'])
    expected = [metadata['codex_binary']['path'], '--no-daemon', '-a', 'never', '-c',
        'default_permissions=' + json.dumps('enterprise-actor'), '-c',
        'shell_environment_policy.set.TMPDIR=' + json.dumps(str(live / '.tmp')),
        'exec', '--ephemeral', '--json', '--ignore-rules', '--skip-git-repo-check', '-C', str(live),
        '--output-schema', str(private / 'schema.json'), '--output-last-message', str(private / 'final.json'),
        '--color', 'never']
    if name == 'image-preflight':
        if identity.get('attached_image') != 'probe.png':
            raise ValueError('material admission image preflight attachment differs')
        expected += ['--image', str(live / 'probe.png')]
        if (directory/'material-review-admission-image.png').read_bytes() != _red_png():
            raise ValueError('material admission image preflight source pixels differ')
        final = m.load(base / 'final.json')
        if set(final) != {'color'} or not isinstance(final['color'],str) or final['color'].strip().lower() != 'red':
            raise ValueError('material admission image preflight did not identify the source image')
    elif identity.get('attached_image') is not None:
        raise ValueError('material admission text preflight includes an unexpected image')
    expected += ['-']
    if command['argv'] != expected:
        raise ValueError('material admission native preflight command/permissions differ')
    events = [json.loads(line, object_pairs_hook=m._object) for line in (base / 'stdout.jsonl').read_text().splitlines()]
    from .review_evidence import thread_identity
    if identity['thread_id'] != thread_identity(base / 'stdout.jsonl'):
        raise ValueError('material admission preflight thread differs')
    stats = {'event_count':len(events), 'usage':[e['usage'] for e in events if 'usage' in e],
        'command_event_count':sum(e.get('item',{}).get('type') == 'command_execution' for e in events),
        'tool_event_count':sum(e.get('item',{}).get('type') in ('command_execution','mcp_tool_call','file_change','web_search') for e in events)}
    if any(session.get(k) != v for k,v in stats.items()) or not session['usage']:
        raise ValueError('material admission preflight event/usage accounting differs')
    for usage in session['usage']:
        if (not isinstance(usage, dict) or any(type(usage.get(k)) is not int or usage[k] < 0
                for k in ('input_tokens','cached_input_tokens','output_tokens'))
                or usage['cached_input_tokens'] > usage['input_tokens']):
            raise ValueError('material admission preflight lacks numeric native usage')
    if name == 'preflight':
        final = m.load(base / 'final.json')
        targets = sorted({n.split('/')[0] for n in frozen['source_hashes'] if n.endswith('/SKILL.md')
                          and n.count('/') == 1 and not n.startswith('_shared/')})
        found = final.get('skills_found')
        if (set(final) != {'skills_found','probe'} or final['probe'] != 'ok' or not isinstance(found,list)
                or len(found) != len(set(found)) or set(found) != set(targets) or stats['command_event_count'] < 1):
            raise ValueError('material admission native discovery does not match frozen targets')
    return session


def verified_runtime(runtime_refs, root, freeze, *, check_config=True):
    """Bind retained admission to the actual existing frozen runtime/tool bytes."""
    m = _review()
    if not isinstance(runtime_refs, dict) or set(runtime_refs) != {'directory','metadata','preflight','frozen_runtime_manifest'}:
        raise ValueError('material native admission reference schema differs')
    directory = m.safe(runtime_refs['directory'], root)
    for key, filename in (('metadata','material-review-admission-runtime.json'),
                          ('preflight','preflight.json'), ('frozen_runtime_manifest','frozen-runtime-manifest.json')):
        if m.verify_ref(runtime_refs[key], root) != directory / filename:
            raise ValueError('material admission file belongs to another native runtime')
    metadata = m.load(directory / 'material-review-admission-runtime.json')
    frozen_path = directory / 'frozen-runtime-manifest.json'
    frozen = m.load(frozen_path)
    if (metadata.get('source_commit') != freeze['source_commit']
            or metadata.get('frozen_runtime_manifest_sha256') != sha256(frozen_path)
            or frozen.get('schema_version') != 'frozen-runtime/2'
            or frozen.get('source_hashes') != frozen.get('frozen_hashes')):
        raise ValueError('material admission frozen runtime/source revision differs')
    source_hashes = {n.removeprefix('togaf-standard-10th-ai/skills/'):v for n,v in freeze['files'].items()
                     if n.startswith('togaf-standard-10th-ai/skills/')}
    excluded = set(freeze.get('excluded_generated_paths',[]))
    prefixes = freeze.get('excluded_generated_prefixes',[])
    frozen_sources = {n:v for n,v in frozen['source_hashes'].items()
        if 'togaf-standard-10th-ai/skills/'+n not in excluded
        and not any(('togaf-standard-10th-ai/skills/'+n).startswith(p) for p in prefixes)}
    if not source_hashes or frozen_sources != source_hashes:
        raise ValueError('material native runtime source does not match independent freeze')
    from .frozen_runtime import verify
    try:
        runtime_root = Path(frozen['python']).parents[4]
        actual = verify(runtime_root)
    except (Blocked, OSError, KeyError, IndexError) as exc:
        raise ValueError('material native runtime dependency admission failed: ' + str(exc)) from exc
    if actual != frozen or metadata.get('codex_binary') != frozen['tool_binaries']['codex']:
        raise ValueError('material native runtime or executable differs from installed pinned bytes')
    if check_config:
        from .agents import provider_configuration
        config = Path(os.environ.get('CODEX_HOME', str(Path.home()/'.codex'))) / 'config.toml'
        try:
            _, configured = provider_configuration(config)
        except (Blocked, OSError, ValueError) as exc:
            raise ValueError('material current model configuration is unavailable') from exc
        if any(metadata.get(k) != configured.get(k) for k in MODEL_KEYS):
            raise ValueError('material native model/provider/inference settings differ from current configuration')
    admission = m.load(directory / 'preflight.json')
    if (set(admission) != {'status','native_targets','text_session','image_session','toolchain'}
            or admission['status'] != 'pass' or admission['toolchain'] != m.load(directory/'toolchain-preflight.json')
            or admission['toolchain'].get('status') != 'pass' or admission['toolchain'].get('failed_probes') != []
            or admission['toolchain'].get('real_home_granted') is not False):
        raise ValueError('material native admission is not a retained full preflight')
    files = metadata.get('material_admission_files')
    if not isinstance(files,dict) or set(files) != admission_file_names(admission):
        raise ValueError('material admission lacks immutable upstream raw preflight bindings')
    for name, digest in files.items():
        if sha256(m.safe(name,directory)) != digest:
            raise ValueError('material upstream raw preflight bytes changed: '+name)
    probes = admission['toolchain'].get('probes', {})
    required = {'python-import-render-probe','node-import-render-probe','java-compile-probe','java-run-probe',
        'uml2-ocl-load-probe','cross-session-read-denied','frozen-write-denied','scorer-read-allowed',
        'scorer-write-denied','shell-network-denied'}
    required.add('controlled-browser-render-probe' if metadata.get('render_mode') == 'controlled-local' else 'browser-render-probe')
    if set(probes) != required:
        raise ValueError('material native admission omits required toolchain/isolation probes')
    text = _preflight_session(directory, 'preflight', metadata, admission['text_session'], frozen)
    image = _preflight_session(directory, 'image-preflight', metadata, admission['image_session'], frozen)
    live = Path(text['execution_identity']['live_workspace'])
    from .agents import sandbox_argv
    shared = runtime_root/'skills/_shared'
    fixed = {
        'python-import-render-probe':[str(shared/'.venv/bin/python'),'-c',
            'import sys;sys.path.insert(0,'+repr(str(shared/'scripts'))+');import jsonschema,yaml,PIL,lxml.etree,defusedxml,validate,generate;from PIL import Image;Image.new("RGB",(20,20),"red").save("python-probe.png");print("ok")'],
        'node-import-render-probe':['/opt/homebrew/bin/node',str(live/'node-probe.mjs')],
        'browser-render-probe':['/opt/homebrew/bin/node',str(live/'browser-probe.mjs')],
        'controlled-browser-render-probe':[str(shared/'.venv/bin/python'),str(shared/'scripts/controlled_render_client.py'),'controller-probe.json'],
        'java-compile-probe':[str(Path(frozen['java_home'])/'bin/javac'),str(live/'Probe.java')],
        'java-run-probe':[str(Path(frozen['java_home'])/'bin/java'),str(live/'Probe.java')],
        'uml2-ocl-load-probe':[str(shared/'.venv/bin/python'),str(live/'uml-probe.py')],
        'scorer-read-allowed':['/bin/cat',str(live/'Probe.java')],
        'scorer-write-denied':['/bin/sh','-c','printf forbidden > '+shlex.quote(str(live/'scorer-forbidden.txt'))],
        'frozen-write-denied':['/bin/sh','-c','printf forbidden > '+shlex.quote(str(shared/'forbidden.txt'))],
        'shell-network-denied':['/usr/bin/curl','--max-time','3','--fail','https://example.com'],
        'cross-session-read-denied':['/bin/cat',str(live.parent/m.text_sha('cross-session-isolation')[:24]/'sentinel.txt')],
    }
    for name, detail in probes.items():
        command_path = directory/name/'command.json'
        command = m.load(command_path)
        expected_denied = name.endswith('-denied')
        prefix = sandbox_argv(metadata['codex_binary']['path'],live,'scorer' if name.startswith('scorer-') else 'actor')
        verify_probe_command(name,detail,command,prefix+fixed[name],denied=expected_denied,read_only=name.startswith('scorer-'))
    prefix = sandbox_argv(metadata['codex_binary']['path'],live)
    for name, suffix, denied in (
            ('read-firewall-probe',['/bin/cat',str(directory/'synthetic-denied-read.txt')],True),
            ('allowed-skill-probe',['/bin/cat',str(live/'.agents/skills/togaf-security-risk/SKILL.md')],False)):
        command = m.load(directory/name/'command.json')
        if (command.get('argv') != prefix+suffix or type(command.get('exit_code')) is not int
                or (command['exit_code'] == 0) == denied or command.get('status') != ('fail' if denied else 'pass')):
            raise ValueError('material native admission read firewall/discovery probe differs')
    if (text['session_number'] == image['session_number']
            or text['execution_identity']['thread_id'] == image['execution_identity']['thread_id']):
        raise ValueError('material native admission reused a preflight session/thread')
    from .agents import permission_configuration
    permissions = permission_configuration(Path.home(),runtime_root/'skills',live.parents[1],runtime_root,Path(frozen['java_home']))
    if metadata.get('permissions_sha256') != m.text_sha(permissions):
        raise ValueError('material native permission configuration differs from fixed isolation policy')
    return {'directory':directory, 'metadata':metadata, 'frozen':frozen,
        'preflight_sessions':[text, image], 'reference':runtime_refs}


def make_runtime_admission(runtime, root):
    """Controller-only snapshot, called after preflight and before review dispatch."""
    m = _review()
    from .agents import NativeAgents
    if type(runtime) is not NativeAgents:
        raise Blocked('material admission requires the actual NativeAgents controller')
    directory = m.safe(Path(runtime.directory).resolve().relative_to(Path(root).resolve()).as_posix(), root)
    path = directory/'material-review-admission-runtime.json'
    metadata = copy.deepcopy(runtime.metadata)
    admission = m.load(directory/'preflight.json')
    image = directory/'material-review-admission-image.png'
    if image.exists():
        raise ValueError('material native admission image is immutable')
    source = Path(runtime.workspaces['image-preflight'])/'probe.png'
    if source.read_bytes() != _red_png():
        raise ValueError('material native admission source image differs')
    shutil.copyfile(source,image)
    metadata['material_admission_files'] = {name:sha256(m.safe(name,directory)) for name in sorted(admission_file_names(admission))}
    m.write_new(path, metadata)
    return {'directory':directory.relative_to(Path(root).resolve()).as_posix(), 'metadata':m.ref(path,root),
        'preflight':m.ref(directory/'preflight.json',root),
        'frozen_runtime_manifest':m.ref(directory/'frozen-runtime-manifest.json',root)}


def verify_authority(authority_ref, inputs, root, *, expected_round=None, historical=False):
    m = _review()
    authority = m.load(m.verify_ref(authority_ref, root))
    required = {'schema_version','round_id','source_commit','source_freeze','input_manifest',
                'acquisition_inventory','visual_source_manifest','runtime'}
    if not isinstance(authority, dict) or set(authority) != required or authority['schema_version'] != 'material-review-authority/1':
        raise ValueError('material review authority schema differs')
    freeze = m.load(m.verify_ref(authority['source_freeze'], root))
    if (freeze.get('schema_version') != 'stabilization-source-freeze/1' or freeze.get('stage') != 'source_freeze'
            or freeze.get('passed') is not True or freeze.get('round_id') != authority['round_id']
            or freeze.get('source_commit') != authority['source_commit']
            or authority['input_manifest'] != inputs.manifest_ref
            or authority['acquisition_inventory'] != inputs.manifest['source_unit_inventory']):
        raise ValueError('material authority differs from independent input/source freeze')
    bound = freeze.get('bound_material_review_inputs', {})
    if (bound.get('input_manifest') != authority['input_manifest']
            or bound.get('visual_source_manifest') != authority['visual_source_manifest']):
        raise ValueError('material authority inputs were not independently frozen upstream')
    if expected_round is not None and (authority['round_id'] != expected_round['round_id']
            or authority['source_commit'] != expected_round['source_commit']
            or authority['source_freeze'] != expected_round.get('prerequisites',{}).get('source_freeze')):
        raise ValueError('material authority belongs to another explicit frozen round')
    for name, digest in inputs.all_refs.items():
        if freeze.get('files',{}).get(name) != digest:
            raise ValueError('material freeze omits or replaces an acquired input: ' + name)
    # Old source/material snapshots remain verifiable, but cannot certify the
    # current checkout. Changed verifier code requires a new review version.
    for name in SOURCE_FILES:
        if freeze.get('files',{}).get(name) != sha256(m.safe(name, m.REPO)):
            raise ValueError('material source reconstruction/verification code differs from freeze')
    if not (Path(root)/'.git').exists():
        raise ValueError('material native authority needs the independently frozen project checkout')
    if not historical:
        # The source-freeze reader performs the same complete acquisition
        # reconstruction. Its explicit input manifest is already matched above.
        m.session_helper().verify_frozen(freeze, root)
    else:
        verified_acquisition(inputs, inputs.root, authority['visual_source_manifest'])
    runtime = verified_runtime(authority['runtime'], root, freeze, check_config=not historical)
    return {'reference':authority_ref,'data':authority,'freeze':freeze,'runtime':runtime,'full_source_scope':True}


def verify_origin(attempt, base, authority, root):
    """A copied session is evidence only if the admitted controller retains it."""
    m = _review()
    runtime = authority['runtime']
    references = attempt.get('origin_raw_session_files')
    if not isinstance(references,dict) or set(references) != RUNTIME_FILES:
        raise ValueError('material native attempt lacks original admitted session files')
    origin = runtime['directory']/base.name/'scorer'
    for filename, reference in references.items():
        source = m.verify_ref(reference,root)
        if source != origin/filename or source.read_bytes() != (base/'scorer'/filename).read_bytes():
            raise ValueError('material native attempt differs from original admitted controller session')
    metadata = m.load(m.verify_ref(attempt['runtime_metadata'],root))
    admitted = runtime['metadata']
    if any(metadata.get(k) != v for k,v in admitted.items() if k not in ('workspace_bindings','material_admission_files')):
        raise ValueError('material attempt changed the admitted native runtime identity')
    if attempt['frozen_runtime_manifest']['sha256'] != authority['data']['runtime']['frozen_runtime_manifest']['sha256']:
        raise ValueError('material attempt changed the admitted frozen runtime')
