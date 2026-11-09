// bpmn-moddle is an exchange backend, not a full BPMN conformance oracle.
import fs from 'node:fs';
import { BpmnModdle } from 'bpmn-moddle';
const [input, output] = process.argv.slice(2);
if (!input) throw new Error('input XML required');
const moddle = new BpmnModdle();
const { rootElement, warnings } = await moddle.fromXML(fs.readFileSync(input, 'utf8'));
const inventory = [], seen = new Set();
function visit(value) {
  if (!value || typeof value !== 'object' || seen.has(value)) return;
  seen.add(value);
  if (value.$type) inventory.push({id:value.id ?? null, type:value.$type});
  for (const [key,child] of Object.entries(value)) {
    if (key.startsWith('$')) continue;
    if (Array.isArray(child)) child.forEach(visit); else visit(child);
  }
}
visit(rootElement);
if (output) {
  const {xml} = await moddle.toXML(rootElement, {format:true});
  fs.writeFileSync(output, xml);
}
console.log(JSON.stringify({backend:'bpmn-moddle',version:'10.3.1',inventory,warnings:warnings.map(w=>String(w.message))}));
