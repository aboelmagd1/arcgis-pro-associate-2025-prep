import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
const strict = process.argv.includes('--strict');
const DOM = ['Data Management','Visualization','Analysis and Geoprocessing','Layouts and Sharing'];
const DIF = ['Beginner','Intermediate','Advanced'];
const TYP = ['Conceptual','Technical','Tool-based','Workflow-based','Troubleshooting','Best-practice'];
const root = 'public/data'; const errors: string[] = [];
const load = (dir: string): any[] => !existsSync(join(root, dir)) ? [] : readdirSync(join(root, dir)).filter(f => f.endsWith('.json')).flatMap(f => {
  try { const d = JSON.parse(readFileSync(join(root, dir, f), 'utf8')); if (!Array.isArray(d)) throw 0; return d.map((x: any) => ({ ...x, _f: f })); }
  catch { errors.push(`${dir}/${f}: invalid JSON or not an array`); return []; } });
function check(kind: 'questions' | 'scenarios') {
  const items = load(kind); const ids = new Set<string>(); const texts = new Set<string>(); let ok = 0;
  const by: Record<string, number> = {};
  for (const q of items) {
    const e = (m: string) => errors.push(`${kind}/${q._f} ${q.id ?? '?'}: ${m}`); const n = errors.length;
    if (!q.id) e('missing id'); else if (ids.has(q.id)) e('duplicate id'); else ids.add(q.id);
    if (!DOM.includes(q.domain)) e('bad domain'); if (!DIF.includes(q.difficulty)) e('bad difficulty'); if (!TYP.includes(q.type)) e('bad type');
    if (!q.objective) e('missing objective');
    if (!Array.isArray(q.options) || q.options.length !== 4 || new Set(q.options.map((o: any) => o.id)).size !== 4) e('need exactly 4 distinct options');
    else if (!q.options.some((o: any) => o.id === q.correctAnswer)) e('correctAnswer not among options');
    for (const l of ['en', 'ar']) { if (!q.question?.[l] || !q.explanation?.[l] || !q.options?.every((o: any) => o.text?.[l])) e(`missing ${l} content`); }
    if (kind === 'scenarios' && (!q.context?.en || !q.context?.ar)) e('scenario needs bilingual context');
    if (!q.references?.length || q.references.some((r: any) => !/^https:\/\//.test(r.url ?? ''))) e('needs references with https URLs');
    const key = (q.question?.en ?? '').toLowerCase().replace(/\W+/g, ' ').trim(); if (key && texts.has(key)) e('duplicate question text'); texts.add(key);
    if (errors.length === n) { ok++; const k = `${q.domain} | ${q.difficulty} | ${q.type}`; by[k] = (by[k] ?? 0) + 1; }
  }
  return { ok, by };
}
const q = check('questions'), s = check('scenarios'), w = load('workflows');
console.log(`Valid MCQs: ${q.ok}/250 · Valid scenarios: ${s.ok}/150 · Workflows: ${w.length}/30`);
for (const [k, v] of Object.entries(q.by)) console.log(`  MCQ ${k}: ${v}`);
for (const [k, v] of Object.entries(s.by)) console.log(`  Scenario ${k}: ${v}`);
if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
if (strict && (q.ok < 250 || s.ok < 150 || w.length < 30)) { console.error('Minimum content counts not met.'); process.exit(1); }
