# -*- coding: utf-8 -*-
"""Portable wrapper preserving existing script interfaces and containing outputs."""
from pathlib import Path
import os,sys,runpy,json,subprocess,importlib.util
sys.dont_write_bytecode=True
S=Path(__file__).resolve().parent;ROOT=S.parent;PACKAGE=ROOT.parent
sys.path.insert(0,str(S));TMP=PACKAGE/'work/tmp';TMP.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(ROOT/'vendor'))
for k in ['TMPDIR','TMP','TEMP']:os.environ[k]=str(TMP)
# Python side effects are contained. Node/browser children inherit local temp paths.
def guard(event,args):
 def allowed(path):
  if isinstance(path,int):return
  p=Path(os.fsdecode(path)).resolve()
  if PACKAGE!=p and PACKAGE not in p.parents:raise PermissionError('Output must stay inside skill package: '+str(p))
 if event.startswith('socket.'):raise PermissionError('Skill wrapper is offline')
 if event=='open':
  p,mode,flags=args
  if (mode and any(c in mode for c in 'wax+')) or flags&(os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND):allowed(p)
 elif event in {'os.mkdir','os.remove','os.rmdir','os.chmod','os.utime'}:allowed(args[0])
 elif event in {'os.rename','os.symlink','os.link'}:allowed(args[0]);allowed(args[1])
sys.addaudithook(guard)
def main():
 if len(sys.argv)<2:raise SystemExit('Usage: local_tool.py query|validate|generate|analyze|adm|delivery|assignments|policy|doctor [existing script arguments]')
 command=sys.argv[1]
 if command=='doctor':
  modules=['jsonschema','yaml','PIL','fontTools','lxml','defusedxml'];checks={m:importlib.util.find_spec(m) is not None for m in modules};checks['node_modules']=(ROOT/'node_modules').is_dir();checks['font']=(ROOT/'assets/fonts/NotoSansSC.ttf').is_file();checks['corpus']=(ROOT/'corpus/retrieval/extended-chunks.jsonl').is_file()
  result={'passed':all(checks.values()),'checks':checks,'package_root':str(PACKAGE),'python':sys.version.split()[0]};print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['passed'] else 1
 names={'query':'corpus_query.py','validate':'validate.py','generate':'generate.py','analyze':'analyze.py','adm':'adm.py','delivery':'architecture_delivery.py','assignments':'assignment_projection.py','policy':'policy_consistency.py'}
 if command not in names:raise SystemExit('Unknown command: '+command)
 sys.argv=[names[command]]+sys.argv[2:];runpy.run_path(str(S/names[command]),run_name='__main__');return 0
if __name__=='__main__':raise SystemExit(main())
