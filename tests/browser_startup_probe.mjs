// Standalone CDP pipe probe: no Puppeteer, model, package, port or network.
import fs from 'node:fs';
import {spawn} from 'node:child_process';
const binary=process.argv[2];
const args=['--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--use-mock-keychain','--password-store=basic','--disable-background-networking','--user-data-dir='+process.cwd()+'/.tmp/browser-profile','--remote-debugging-pipe','about:blank'];
const event=row=>fs.appendFileSync('process-events.jsonl',JSON.stringify({...row,time:new Date().toISOString()})+'\n');
const child=spawn(binary,args,{stdio:['ignore','pipe','pipe','pipe','pipe']});
event({event:'spawn',pid:child.pid,binary,args,home:process.env.HOME,tmpdir:process.env.TMPDIR});
child.stderr.pipe(process.stderr);
let id=0,buffer=Buffer.alloc(0),exitResult;
const pending=new Map();
const exited=new Promise(resolve=>child.on('exit',(code,signal)=>{exitResult={code,signal};event({event:'exit',pid:child.pid,...exitResult});for(const p of pending.values())p.reject(Error('browser exited '+JSON.stringify(exitResult)));resolve();}));
child.stdio[4].on('data',chunk=>{
 buffer=Buffer.concat([buffer,chunk]);let index;
 while((index=buffer.indexOf(0))>=0){const message=JSON.parse(buffer.subarray(0,index).toString());buffer=buffer.subarray(index+1);const p=pending.get(message.id);if(p){pending.delete(message.id);message.error?p.reject(Error(JSON.stringify(message.error))):p.resolve(message.result);}}
});
const send=(method,params={},sessionId)=>new Promise((resolve,reject)=>{const number=++id;pending.set(number,{resolve,reject});child.stdio[3].write(JSON.stringify({id:number,method,params,...(sessionId?{sessionId}:{})})+'\0');});
const timeout=setTimeout(()=>{event({event:'timeout'});child.kill('SIGKILL');},15000);
try{
 const version=await send('Browser.getVersion');event({event:'version',version});
 const target=await send('Target.createTarget',{url:'about:blank'});
 const {sessionId}=await send('Target.attachToTarget',{targetId:target.targetId,flatten:true});
 await send('Page.enable',{},sessionId);
 await send('Runtime.evaluate',{expression:'document.body.innerHTML="<h1>原生隔离最小截图</h1>"'},sessionId);
 const image=await send('Page.captureScreenshot',{format:'png'},sessionId);
 fs.writeFileSync('minimal-screenshot.png',Buffer.from(image.data,'base64'));event({event:'screenshot-complete'});
 await send('Browser.close');
}catch(error){event({event:'probe-failed',message:String(error)});console.error(String(error));process.exitCode=1;}
finally{
 clearTimeout(timeout);if(!exitResult)child.kill('SIGTERM');await exited;
}
