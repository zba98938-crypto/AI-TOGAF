#!/usr/bin/env python3
"""Minimal dependency-free browser A/B reproducer with actual process signals."""
import argparse,json,os,shutil,subprocess,tempfile
from pathlib import Path
from enterprise.agents import permission_configuration,sandbox_argv
def run(out,browser):
    out.mkdir(parents=True,exist_ok=False);rows=[]
    script=Path(__file__).with_name('browser_startup_probe.mjs')
    shutil.copyfile(script,out/script.name)
    with tempfile.TemporaryDirectory(prefix='togaf-minimal-browser-') as tmp:
        private=Path(tmp).resolve();work=private/'workspace';work.mkdir();(work/'.tmp/home').mkdir(parents=True);config=private/'.codex';config.mkdir()
        settings={'HOME':str(work/'.tmp/home'),'TMPDIR':str(work/'.tmp'),'PATH':'/opt/homebrew/bin:/usr/bin:/bin','NODE_OPTIONS':'--preserve-symlinks --preserve-symlinks-main'}
        content=permission_configuration(Path.home(),browser.parent,private)+'\n[shell_environment_policy]\ninherit="none"\n[shell_environment_policy.set]\n'+'\n'.join(k+'='+json.dumps(v) for k,v in settings.items())+'\n'
        (config/'config.toml').write_text(content);(out/'permissions.toml').write_text(content);shutil.copyfile(script,work/script.name)
        env={**os.environ,**settings,'CODEX_HOME':str(config)}
        for isolated in (False,True):
            name='native' if isolated else 'direct';shutil.rmtree(work/'.tmp/browser-profile',ignore_errors=True)
            args=['/opt/homebrew/bin/node',str(work/script.name),str(browser)]
            p=subprocess.run((sandbox_argv('/opt/homebrew/bin/codex',work)+args) if isolated else args,cwd=work,env=env,capture_output=True,text=True,timeout=30)
            (out/(name+'.stdout.log')).write_text(p.stdout);(out/(name+'.stderr.log')).write_text(p.stderr)
            for filename in ('process-events.jsonl','minimal-screenshot.png'):
                source=work/filename
                if source.exists():shutil.move(source,out/(name+'-'+filename))
            rows.append({'isolated':isolated,'exit_code':p.returncode,'name':name})
    (out/'summary.json').write_text(json.dumps({'rows':rows,'model_sessions':0,'dependency':'Node builtins and exact Chromium binary only','upstream_submission':'not-submitted'},indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--browser',type=Path,required=True);a=p.parse_args();run(a.out.resolve(),a.browser.resolve())
