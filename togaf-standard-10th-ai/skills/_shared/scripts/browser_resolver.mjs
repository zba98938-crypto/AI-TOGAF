// Resolve an existing browser; never download one during verification.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import puppeteer from 'puppeteer';

function unavailable(code,message,cause) {
  const error=new Error(`browser-unavailable: ${message}`,cause ? {cause} : undefined);
  error.code=code;
  return error;
}

export function resolveBrowser({env=process.env, platform=process.platform, home=os.homedir(),
  bundled=()=>puppeteer.executablePath(), executable=p=>{try {fs.accessSync(p,fs.constants.X_OK);return fs.statSync(p).isFile();}catch{return false;}}}={}) {
  if (env.TOGAF_BROWSER_PATH) {
    const explicit=path.resolve(env.TOGAF_BROWSER_PATH);
    if(!executable(explicit)) throw unavailable('BROWSER_EXECUTABLE_INVALID',`TOGAF_BROWSER_PATH is not executable: ${explicit}`);
    return {executablePath:explicit,source:'TOGAF_BROWSER_PATH'};
  }
  let cached;
  try{cached=bundled();}catch{}
  if(cached&&executable(cached))return {executablePath:cached,source:'puppeteer-installed'};
  const candidates=platform==='darwin' ? ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',path.join(home,'Applications/Google Chrome.app/Contents/MacOS/Google Chrome')] :
    platform==='win32' ? [path.join(env.PROGRAMFILES||'C:/Program Files','Google/Chrome/Application/chrome.exe'),
      path.join(env.LOCALAPPDATA||home,'Google/Chrome/Application/chrome.exe'),
      path.join(env.PROGRAMFILES||'C:/Program Files','Microsoft/Edge/Application/msedge.exe')] :
    ['/usr/bin/google-chrome','/usr/bin/google-chrome-stable','/usr/bin/chromium','/usr/bin/chromium-browser','/snap/bin/chromium'];
  for(const candidate of candidates)if(executable(candidate))return {executablePath:candidate,source:'local-installation'};
  throw unavailable('BROWSER_NOT_FOUND','install Chrome/Chromium or set TOGAF_BROWSER_PATH to an existing executable');
}
export async function launchBrowser(options={}) {
  const resolved=resolveBrowser();
  let browser;
  try { browser=await puppeteer.launch({pipe:true,...options,headless:true,executablePath:resolved.executablePath}); }
  catch(error) { throw unavailable('BROWSER_LAUNCH_FAILED',`cannot launch ${resolved.executablePath}: ${error.message}`,error); }
  try { browser.togafBrowser={...resolved,version:await browser.version()}; }
  catch(error) {
    try { await browser.close(); } catch {}
    throw unavailable('BROWSER_PROTOCOL_FAILED',`cannot query ${resolved.executablePath}: ${error.message}`,error);
  }
  return browser;
}
