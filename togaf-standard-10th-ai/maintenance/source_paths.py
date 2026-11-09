"""Resolve historical source identities to verified files inside the AI corpus."""
from pathlib import Path
from functools import lru_cache
import json
C=Path(__file__).resolve().parents[1];ROOT=C.parent
@lru_cache(maxsize=1)
def relocation():
 p=C/'sources/relocation-manifest.json'
 return json.loads(p.read_text())['logical_paths'] if p.exists() else {}
def resolve(path):
 p=Path(path).resolve()
 try:logical=p.relative_to(ROOT).as_posix()
 except ValueError:return p
 local=relocation().get(logical)
 if local:
  target=(C/local).resolve()
  if C not in target.parents:raise ValueError('Source mapping escapes AI folder: '+logical)
  return target
 return p
