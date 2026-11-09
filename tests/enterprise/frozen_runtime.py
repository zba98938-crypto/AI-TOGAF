"""Freeze skills/dependencies outside the denied home, with byte-level provenance.
Not a claim of OS hermeticity: system loader/browser libraries remain OS dependencies.
"""
import hashlib,json,shutil,subprocess,sys
from pathlib import Path
from .runtime import Blocked,save,sha256

def hashes(root,exclude=()):
    root=Path(root);return {str(p.relative_to(root)):sha256(p) for p in sorted(root.rglob('*')) if p.is_file() and not any(part in exclude for part in p.relative_to(root).parts)}

def dependency_hashes(root):
    shared=Path(root)/'skills/_shared'
    return {prefix+'/'+k:v for prefix in ('node_modules','.venv') for k,v in hashes(shared/prefix,('__pycache__',)).items()}

def binary_record(path):
    path=Path(path).resolve()
    if path.is_relative_to(Path.home().resolve()):raise Blocked('tool binary resolves inside denied real home: '+str(path))
    return {'path':str(path),'sha256':sha256(path)}

def admission_location(path,label,platform=None,home=None):
    """New runtime/tool admission, not retroactive invalidation of archived hashes."""
    path=Path(path).resolve();platform=platform or sys.platform;home=Path(home or Path.home()).resolve()
    if path.is_relative_to(home):raise Blocked(label+" resolves inside denied real home")
    if platform=="darwin" and path.is_relative_to(Path("/tmp").resolve()):raise Blocked(label+" under denied /tmp conflicts with native tool realpath; use scoped read-only /Users/Shared")
    return path

def build(source,destination,java_home=None,reuse_runtime=None,browser_home=None):
    source=Path(source).resolve();destination=admission_location(destination,"frozen runtime")
    if destination.is_relative_to(Path.home().resolve()):raise Blocked('frozen runtime must be outside real home')
    if destination.exists():raise Blocked('runtime destination must be new; freeze cannot overwrite an existing runtime')
    java=admission_location(java_home,"Java runtime") if java_home else None
    if not java or not (java/'bin/java').is_file() or java.is_relative_to(Path.home().resolve()):raise Blocked('isolated Java21 outside real home required')
    python=binary_record(sys.executable);node=binary_record(shutil.which('node'))
    codex=binary_record(shutil.which('codex'))
    if sys.platform=="darwin" and destination.is_relative_to(Path("/tmp").resolve()):raise Blocked("macOS frozen runtime must be outside denied /tmp; use a scoped path such as /Users/Shared")
    prior=verify(reuse_runtime) if reuse_runtime else None
    destination.mkdir(parents=True);shared=destination/'skills/_shared'
    shutil.copytree(source,destination/'skills',ignore=shutil.ignore_patterns('.venv','__pycache__','.DS_Store'),symlinks=False)
    subprocess.run([python['path'],'-m','venv',str(shared/'.venv')],check=True,timeout=60)
    wheels=destination/'wheels';wheels.mkdir()
    with (destination/'dependency-build.log').open('w') as stream:
        if prior:
            if sha256(Path(reuse_runtime)/'skills/_shared/requirements.txt')!=sha256(shared/'requirements.txt'):raise Blocked('reused wheels require identical requirement bytes')
            for wheel in (Path(reuse_runtime)/'wheels').iterdir():
                if wheel.is_file():shutil.copy2(wheel,wheels/wheel.name)
            if hashes(wheels)!=prior['wheel_hashes']:raise Blocked('reused wheel hash mismatch')
        else:
            subprocess.run([str(shared/'.venv/bin/python'),'-m','pip','download','-r',str(shared/'requirements.txt'),'-d',str(wheels)],stdout=stream,stderr=stream,check=True,timeout=300)
        subprocess.run([str(shared/'.venv/bin/python'),'-m','pip','install','--no-index','--find-links',str(wheels),'-r',str(shared/'requirements.txt')],stdout=stream,stderr=stream,check=True,timeout=120)
    manifest={'schema_version':'frozen-runtime/2','source':str(source),'source_hashes':hashes(source,('.venv','node_modules','__pycache__','.DS_Store')),'frozen_hashes':hashes(destination/'skills',('.venv','node_modules','__pycache__','.DS_Store')),'dependency_hashes':dependency_hashes(destination),'wheel_hashes':hashes(wheels),'java_home':str(java),'java_hashes':hashes(java),'tool_binaries':{'python':python,'node':node},'python':str(shared/'.venv/bin/python'),'dependencies_sha256':sha256(shared/'package-lock.json'),'home_configuration_copied':False,'system_dependency_boundary':'base Python, Node loader and browser/system libraries are external OS dependencies; binary paths/hashes recorded, not claimed fully hermetic'}
    manifest['tool_binaries']['codex']=codex
    if browser_home:
        browser_home=admission_location(browser_home,"browser distribution");candidates=list(browser_home.rglob('chrome-headless-shell'))
        candidates=[p for p in candidates if p.is_file()]
        if len(candidates)!=1:raise Blocked('exactly one pinned headless browser executable required')
        manifest['browser_home']=str(browser_home);manifest['browser_hashes']=hashes(browser_home)
        manifest['tool_binaries']['browser']=binary_record(candidates[0])
    if reuse_runtime:manifest['parent_manifest_sha256']=sha256(Path(reuse_runtime)/'runtime-manifest.json')
    if manifest['source_hashes']!=manifest['frozen_hashes']:raise Blocked('frozen source copy hash mismatch')
    save(destination/'runtime-manifest.json',manifest);return manifest

def verify(destination):
    destination=Path(destination).resolve()
    if destination.is_relative_to(Path.home().resolve()):raise Blocked('runtime resolves inside denied real home')
    try:manifest=json.loads((destination/'runtime-manifest.json').read_text())
    except (OSError,ValueError):raise Blocked('frozen runtime manifest missing')
    if manifest.get('schema_version')!='frozen-runtime/2':raise Blocked('runtime must be resealed with dependency-byte provenance')
    if hashes(destination/'skills',('.venv','node_modules','__pycache__','.DS_Store'))!=manifest['frozen_hashes']:raise Blocked('frozen skill revision changed after sealing')
    if sha256(destination/'skills/_shared/package-lock.json')!=manifest['dependencies_sha256']:raise Blocked('frozen dependency lock changed')
    if dependency_hashes(destination)!=manifest['dependency_hashes']:raise Blocked('frozen dependency bytes changed')
    if hashes(destination/'wheels')!=manifest['wheel_hashes']:raise Blocked('frozen wheel bytes changed')
    binaries=manifest['tool_binaries']
    for row in binaries.values():
        if binary_record(row['path'])!=row:raise Blocked('external runtime binary changed')
    for p in (destination/'skills').rglob('*'):
        if p.is_symlink() and not p.resolve().is_relative_to(destination) and str(p.resolve())!=binaries['python']['path']:raise Blocked('dependency symlink escapes isolated runtime: '+str(p))
    java=Path(manifest.get('java_home','')).resolve()
    if java.is_relative_to(Path.home().resolve()) or not (java/'bin/java').is_file() or hashes(java)!=manifest['java_hashes']:raise Blocked('isolated Java bytes/provenance changed')
    if 'browser_home' in manifest:
        browser=Path(manifest['browser_home']).resolve()
        if browser.is_relative_to(Path.home().resolve()) or hashes(browser)!=manifest.get('browser_hashes'):raise Blocked('pinned browser distribution bytes changed')
    return manifest
