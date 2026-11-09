#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {launchBrowser} from '../../togaf-standard-10th-ai/skills/_shared/scripts/browser_resolver.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const folder=path.join(root,'togaf-standard-10th-ai/architecture');
const browser=await launchBrowser();
const report={checks:[],errors:[],html_sha256:createHash('sha256').update(await fs.readFile(path.join(folder,'explorer.html'))).digest('hex')};
try{
 const page=await browser.newPage();
 page.on('pageerror',e=>report.errors.push(String(e)));
 await page.setViewport({width:1440,height:1000,deviceScaleFactor:1});
 await page.goto(pathToFileURL(path.join(folder,'explorer.html')).href,{waitUntil:'networkidle0'});
 let cards=await page.$$eval('article',els=>els.length);if(cards!==24)throw Error('Initial cards '+cards);
 await page.select('#kind','角色');await page.select('#doc','G249');
 await page.type('#query','企业架构师');
 await page.waitForFunction(()=>document.querySelectorAll('article').length===1);
 await page.click('summary');
 const cells=await page.$$eval('article table tr',els=>els.length);if(cells!==72)throw Error('Expected header plus 71 skill rows; got '+cells);
 report.checks.push('G249 企业架构师全文职责/要求和71项技能可见');
 await page.screenshot({path:path.join(folder,'explorer-role.png'),fullPage:true});
 await page.evaluate(()=>{document.querySelector('#query').value='';document.querySelector('#query').dispatchEvent(new Event('input'))});
 await page.select('#kind','图示');await page.select('#doc','G233');
 await page.type('#query','fig3-1');
 await page.waitForFunction(()=>document.querySelectorAll('article').length===1);
 await page.waitForFunction(()=>document.querySelector('article img')?.naturalWidth>0);
 report.checks.push('G233架构元模型原图加载，MD/JSON入口存在');
 await page.screenshot({path:path.join(folder,'explorer-diagram.png'),fullPage:true});
 await page.setViewport({width:390,height:844,deviceScaleFactor:1});
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
 if(overflow)throw Error('Mobile horizontal overflow');
 report.checks.push('390px移动宽度无横向溢出');
}catch(e){report.errors.push(String(e));}finally{await browser.close();}
report.passed=report.errors.length===0;
await fs.writeFile(path.join(folder,'explorer-validation.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));if(!report.passed)process.exitCode=1;
