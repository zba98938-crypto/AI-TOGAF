#!/usr/bin/env python3
"""Zero-model A/B browser diagnosis, keeping native filesystem/network boundaries."""
import argparse,json,os,subprocess,sys,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from enterprise.agents import permission_configuration,sandbox_argv
from enterprise.runtime import save,sha256

def run(out,runtime,browser):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);rows=[]
    with tempfile.TemporaryDirectory(prefix='togaf-browser-ab-') as temporary:
        private=Path(temporary).resolve();work=private/'workspace';work.mkdir();(work/'.tmp').mkdir()
        home=work/'.tmp/home';home.mkdir();config=private/'.codex';config.mkdir()
        shared=Path(runtime).resolve()/'skills/_shared'
        settings={'HOME':str(home),'TMPDIR':str(work/'.tmp'),'PATH':'/opt/homebrew/bin:/usr/bin:/bin','TOGAF_BROWSER_PATH':str(Path(browser).resolve()),'NODE_OPTIONS':'--preserve-symlinks --preserve-symlinks-main'}
        content=permission_configuration(Path.home(),shared.parent,private,Path(runtime).resolve())
        content+='\n[shell_environment_policy]\ninherit="none"\n[shell_environment_policy.set]\n'
        content+='\n'.join(k+'='+json.dumps(v) for k,v in settings.items())+'\n'
        (config/'config.toml').write_text(content);(out/'permissions.toml').write_text(content)
        script=work/'probe.mjs'
        script.write_text('''import fs from 'node:fs';
import cp from 'node:child_process';
import {syncBuiltinESMExports} from 'node:module';
const record=row=>fs.appendFileSync('process-events.jsonl',JSON.stringify({...row,time:new Date().toISOString()})+'\\n');
const spawn=cp.spawn;
cp.spawn=function(binary,args,options){
 const child=spawn.call(this,binary,args,options);
 if(binary===process.env.TOGAF_BROWSER_PATH){
  record({event:'spawn',pid:child.pid,binary,args,cwd:options?.cwd,tmpdir:process.env.TMPDIR});
  child.on('exit',(code,signal)=>record({event:'exit',pid:child.pid,code,signal}));
  child.on('error',error=>record({event:'error',pid:child.pid,reason:String(error)}));
 }
 return child;
};
syncBuiltinESMExports();
const {launchBrowser}=await import('''+json.dumps(str(shared/'scripts/browser_resolver.mjs'))+''');
let browser;
try {
 browser=await launchBrowser({pipe:true,dumpio:true,userDataDir:'.tmp/browser-profile',args:JSON.parse(process.argv[2])});
 console.log(JSON.stringify({pid:browser.process().pid,browser:browser.togafBrowser}));
 const page=await browser.newPage();await page.setContent('<meta charset="utf-8"><h1>原生隔离截图</h1>');
 await page.screenshot({path:'browser-probe.png'});
 console.log('screenshot-complete');
} finally {if(browser)await browser.close();}
''')
        (out/'probe.mjs').write_bytes(script.read_bytes())
        environment={**os.environ,**settings,'CODEX_HOME':str(config)}
        for name,isolated,flags in [('direct-control',False,[]),('native-default',True,[]),('native-no-inner-sandbox',True,['--no-sandbox'])]:
            from shutil import rmtree
            rmtree(work/'.tmp/browser-profile',ignore_errors=True)
            (work/'process-events.jsonl').unlink(missing_ok=True)
            args=['/opt/homebrew/bin/node',str(script),json.dumps(flags)]
            argv=(sandbox_argv('/opt/homebrew/bin/codex',work)+args) if isolated else args
            p=subprocess.run(argv,cwd=work,env=environment,capture_output=True,text=True,timeout=45)
            (out/(name+'.stdout.log')).write_text(p.stdout);(out/(name+'.stderr.log')).write_text(p.stderr)
            screenshot=work/'browser-probe.png'
            row={'name':name,'isolated':isolated,'browser_flags':flags,'exit_code':p.returncode,'screenshot':None}
            events=work/'process-events.jsonl'
            if events.is_file():
                (out/(name+'.process-events.jsonl')).write_bytes(events.read_bytes())
                row['browser_processes']=[json.loads(line) for line in events.read_text().splitlines()]
            if p.returncode==0 and screenshot.is_file():
                from shutil import copyfile
                copyfile(screenshot,out/(name+'.png'));row['screenshot']=name+'.png';row['png_sha256']=sha256(screenshot)
            screenshot.unlink(missing_ok=True);rows.append(row);save(out/'progress.json',rows)
        (private/'sentinel').write_text('other private context')
        for name,role,command in [('cross-session-read-denied','actor',['/bin/cat',str(private/'sentinel')]),('real-home-read-denied','actor',['/usr/bin/stat',str(Path.home())]),('scorer-write-denied','scorer',['/usr/bin/touch',str(work/'forbidden')])]:
            p=subprocess.run(sandbox_argv('/opt/homebrew/bin/codex',work,role)+command,cwd=work,env=environment,capture_output=True,text=True,timeout=15)
            rows.append({'name':name,'exit_code':p.returncode,'expected':'denied','status':'pass' if p.returncode!=0 else 'fail'})
    result={'diagnostic_only':True,'model_sessions':0,'model_requests_observed':0,'real_home_granted':False,'runtime_manifest_sha256':sha256(Path(runtime)/'runtime-manifest.json'),'browser_sha256':sha256(browser),'rows':rows}
    save(out/'summary.json',result);return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--runtime-root',type=Path,required=True);p.add_argument('--browser',type=Path,required=True);a=p.parse_args()
    print(json.dumps(run(a.out,a.runtime_root,a.browser),ensure_ascii=False))
