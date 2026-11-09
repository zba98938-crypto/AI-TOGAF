// Fixed local-controller UI checks. This is not an Actor rendering interface.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {launchBrowser} from '../skills/_shared/scripts/browser_resolver.mjs';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const argv = process.argv.slice(2);
function require(value, message) { if (!value) throw Error(message); }
require(argv.length === 4 && argv[0] === '--input' && argv[2] === '--out', 'Use --input FILE --out NEW_DIRECTORY');
const input = path.resolve(argv[1]), out = path.resolve(argv[3]);
function inside(value, root = repo) { const rel = path.relative(root, value); return !rel.startsWith('..' + path.sep) && rel !== '..' && !path.isAbsolute(rel); }
async function safe(value, {exists = true} = {}) {
  require(path.isAbsolute(value) && inside(value) && path.normalize(value) === value, 'Path escapes repository');
  let cursor = repo;
  for (const component of path.relative(repo, value).split(path.sep).filter(Boolean)) {
    cursor = path.join(cursor, component);
    let stat;
    try { stat = await fs.lstat(cursor); } catch (error) { if (exists || error.code !== 'ENOENT') throw error; }
    require(!stat?.isSymbolicLink(), 'Symlink traversal is forbidden');
  }
  return value;
}
const sha = async value => createHash('sha256').update(await fs.readFile(value)).digest('hex');
await safe(input);
await safe(out, {exists: false});
require(inside(out, path.join(repo, 'output')), 'UI evidence must be in repository output');
await fs.mkdir(out); // Never overwrite a previous run.
const request = JSON.parse(await fs.readFile(input, 'utf8'));
const report = {schema_version: 'current-output-ui-verification/1', round_id: request.round_id,
  runtime_mode: 'local-test-controller', actor_sandbox_used: false,
  input_sha256: await sha(input), checks: [], blocked_requests: [], errors: [], passed: false};
let browser, ownedProcess, profile;
try {
  require(request.schema_version === 'current-output-ui-request/1' && request.runtime_mode === 'local-test-controller'
    && request.repo_root === repo, 'Invalid fixed UI request');
  require(Number.isInteger(request.expected_rows) && request.expected_rows > 0
    && typeof request.search_term === 'string' && request.search_term
    && Number.isInteger(request.expected_search_rows) && request.expected_search_rows > 0, 'Invalid UI expectations');
  const allowed = new Map(Object.entries(request.allowed_files));
  require(allowed.size > 0, 'No fingerprinted local resources');
  for (const [filename, expected] of allowed) {
    await safe(filename);
    require(/^[0-9a-f]{64}$/.test(expected) && (await fs.stat(filename)).isFile()
      && await sha(filename) === expected, 'Resource fingerprint differs: ' + filename);
  }
  for (const entry of [request.catalogue, request.atlas]) {
    await safe(entry.path);
    require(path.extname(entry.path) === '.html' && allowed.get(entry.path) === entry.sha256, 'Invalid HTML entry reference');
  }
  profile = path.join(out, 'browser-profile');
  browser = await launchBrowser({userDataDir: profile, timeout: 30000,
    env: {...process.env, TMPDIR: out, TMP: out, TEMP: out},
    args: ['--disable-background-networking', '--disable-component-update', '--no-first-run']});
  ownedProcess = browser.process();
  report.browser = {...browser.togafBrowser, owned_pid: ownedProcess?.pid};
  const page = await browser.newPage();
  page.setDefaultTimeout(15000);
  page.on('pageerror', error => report.errors.push(String(error)));
  await page.setRequestInterception(true);
  page.on('request', async resource => {
    let permit = false;
    try {
      const url = new URL(resource.url());
      if (url.protocol === 'file:') {
        const filename = fileURLToPath(url);
        await safe(filename);
        permit = allowed.has(filename) && await sha(filename) === allowed.get(filename);
      } else if (url.protocol === 'data:') {
        permit = ['image', 'font'].includes(resource.resourceType());
      } else if (resource.url() === 'about:blank') {
        permit = true;
      }
    } catch {}
    if (!permit) report.blocked_requests.push({url: resource.url().slice(0, 240), resource_type: resource.resourceType()});
    try { await (permit ? resource.continue() : resource.abort('blockedbyclient')); } catch {}
  });
  const goto = filename => page.goto(pathToFileURL(filename).href, {waitUntil: 'networkidle0', timeout: 30000});
  const visibleRows = () => page.$$eval('tr[data-search]', nodes => nodes.filter(node => !node.hidden && getComputedStyle(node).display !== 'none').length);
  await page.setViewport({width: 1440, height: 1000, deviceScaleFactor: 1});
  await goto(request.catalogue.path);
  require(await page.$$eval('tr[data-search]', nodes => nodes.length) === request.expected_rows, 'Catalogue inventory differs');
  require(await visibleRows() === request.expected_rows, 'Initial catalogue rows are hidden');
  await page.focus('#q');
  await page.keyboard.type(request.search_term);
  await page.waitForFunction(expected => [...document.querySelectorAll('tr[data-search]')].filter(row => !row.hidden && getComputedStyle(row).display !== 'none').length === expected, {}, request.expected_search_rows);
  require(await visibleRows() === request.expected_search_rows, 'Search row count differs');
  report.checks.push({id: 'catalogue-search', passed: true, total_rows: request.expected_rows,
    search_term: request.search_term, visible_rows: request.expected_search_rows});
  await page.screenshot({path: path.join(out, 'catalogue-search.png')});
  await page.keyboard.press('Tab');
  const focused = await page.evaluate(() => ({tag: document.activeElement?.tagName, href: document.activeElement?.href}));
  require(focused.tag === 'A' && allowed.has(fileURLToPath(focused.href)), 'Tab does not reach a fingerprinted result link');
  await Promise.all([page.waitForNavigation({waitUntil: 'networkidle0'}), page.keyboard.press('Enter')]);
  require(page.url() === focused.href, 'Keyboard result navigation failed');
  report.checks.push({id: 'catalogue-keyboard-navigation', passed: true, target: path.relative(repo, fileURLToPath(focused.href))});
  await goto(request.atlas.path);
  require(await page.$$eval('details', nodes => nodes.length) > 0, 'Atlas has no native disclosure panels');
  await page.$eval('details', panel => { panel.open = false; });
  await page.focus('details summary');
  await page.keyboard.press('Enter');
  require(await page.$eval('details', panel => panel.open), 'Enter does not open atlas panel');
  await page.keyboard.press('Enter');
  require(!(await page.$eval('details', panel => panel.open)), 'Enter does not close atlas panel');
  const navigation = await page.$$eval('nav a[href^="#"]', nodes => nodes.find(node => document.getElementById(node.hash.slice(1))?.tagName === 'DETAILS')?.getAttribute('href'));
  require(navigation, 'Atlas has no panel navigation');
  await page.click('nav a[href="' + navigation + '"]');
  require(await page.evaluate(hash => {
    const panel = document.getElementById(hash.slice(1));
    return panel.open && document.activeElement === panel.querySelector('summary');
  }, navigation), 'Atlas navigation does not open and focus panel');
  report.checks.push({id: 'atlas-keyboard-and-navigation', passed: true});
  const imageCount = await page.$$eval('img', nodes => { for (const image of nodes) image.loading = 'eager'; return nodes.length; });
  require(imageCount > 0, 'Atlas contains no diagram previews');
  await page.waitForFunction(() => [...document.images].every(image => image.complete && image.naturalWidth > 0));
  report.checks.push({id: 'atlas-diagram-previews', passed: true, images: imageCount});
  await page.screenshot({path: path.join(out, 'atlas-desktop.png')});
  await page.setViewport({width: 390, height: 844, deviceScaleFactor: 1});
  for (const [name, entry] of [['catalogue', request.catalogue], ['atlas', request.atlas]]) {
    await goto(entry.path);
    const geometry = await page.evaluate(() => ({viewport: innerWidth, width: document.documentElement.scrollWidth}));
    require(geometry.width <= geometry.viewport + 1, 'Mobile document overflows: ' + name);
    report.checks.push({id: name + '-mobile-layout', passed: true, ...geometry});
    await page.screenshot({path: path.join(out, name + '-mobile.png')});
  }
  require(report.blocked_requests.length === 0 && report.errors.length === 0, 'Page requested disallowed resources or raised errors');
  for (const [filename, expected] of allowed) require(await sha(filename) === expected, 'Resource changed during UI verification');
  report.passed = true;
} catch (error) {
  report.errors.push(String(error));
} finally {
  if (browser) {
    try { await browser.close(); } catch (error) { report.errors.push('Browser cleanup: ' + error); ownedProcess?.kill('SIGKILL'); }
  }
  if (profile) await fs.rm(profile, {recursive: true, force: true});
  let running = false;
  if (ownedProcess?.pid) { try { process.kill(ownedProcess.pid, 0); running = true; } catch {} }
  report.cleanup = {browser_root_terminated: !running, profile_removed: profile ? !(await fs.stat(profile).catch(() => null)) : true};
  if (running || !report.cleanup.profile_removed || report.errors.length) report.passed = false;
  report.completed_at = new Date().toISOString();
  await fs.writeFile(path.join(out, 'result.json'), JSON.stringify(report, null, 2) + '\n', {flag: 'wx'});
}
console.log(JSON.stringify({passed: report.passed, runtime_mode: report.runtime_mode, checks: report.checks.length, errors: report.errors}));
if (!report.passed) process.exitCode = 1;
