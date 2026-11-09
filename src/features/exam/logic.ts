import type { AttemptAnswer, OptionId, Question, RevisionRecord } from '../../types/content';

export interface ExamItem { q: Question; order: OptionId[]; }
export const INTERVAL_DAYS = [1, 2, 4, 8, 16, 32]; // spaced-repetition boxes

export function shuffle<T>(a: T[], rnd: () => number = Math.random): T[] {
  const r = [...a];
  for (let i = r.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; }
  return r;
}
/** Random questions, random option order. Never returns more than the pool holds. */
export function buildExam(pool: Question[], count: number, rnd: () => number = Math.random): ExamItem[] {
  return shuffle(pool, rnd).slice(0, Math.max(0, count)).map(q => ({ q, order: shuffle(q.options.map(o => o.id), rnd) }));
}

/** Official 75-question EAPA_2025 exam generator with exact blueprint domain weights:
 * Data Management: 32% (24 Qs), Visualization: 25% (19 Qs), Analysis & GP: 25% (19 Qs), Layouts & Sharing: 18% (13 Qs).
 */
export function buildOfficialExam(pool: Question[], rnd: () => number = Math.random): ExamItem[] {
  const dm = shuffle(pool.filter(q => q.domain === 'Data Management'), rnd).slice(0, 24);
  const viz = shuffle(pool.filter(q => q.domain === 'Visualization'), rnd).slice(0, 19);
  const agp = shuffle(pool.filter(q => q.domain === 'Analysis and Geoprocessing'), rnd).slice(0, 19);
  const ls = shuffle(pool.filter(q => q.domain === 'Layouts and Sharing'), rnd).slice(0, 13);
  const combined = shuffle([...dm, ...viz, ...agp, ...ls], rnd);
  return combined.map(q => ({ q, order: shuffle(q.options.map(o => o.id), rnd) }));
}
export function grade(items: ExamItem[], sel: Record<string, OptionId>, flags: Set<string>, ms: Record<string, number> = {}): AttemptAnswer[] {
  return items.map(({ q }) => ({ questionId: q.id, selected: sel[q.id] ?? null, correct: sel[q.id] === q.correctAnswer, flagged: flags.has(q.id), ms: ms[q.id] ?? 0 }));
}
export const scorePct = (a: AttemptAnswer[]) => (a.length ? Math.round((a.filter(x => x.correct).length / a.length) * 100) : 0);

/** Wrong or unanswered -> box 0 (due after 1 day). Correct -> next box, longer interval. */
export function updateRevision(rev: RevisionRecord[], answers: AttemptAnswer[], now = new Date()): RevisionRecord[] {
  const map = new Map(rev.map(r => [r.questionId, r]));
  for (const a of answers) {
    const prev = map.get(a.questionId);
    const box = a.correct ? Math.min((prev?.box ?? -1) + 1, INTERVAL_DAYS.length - 1) : 0;
    map.set(a.questionId, { questionId: a.questionId, box, lastResult: a.correct, dueAt: new Date(now.getTime() + INTERVAL_DAYS[box] * 86400000).toISOString() });
  }
  return [...map.values()];
}
