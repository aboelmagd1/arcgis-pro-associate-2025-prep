import type { ExamAttempt, Question, RevisionRecord } from '../../types/content';

export interface Row { key: string; n: number; correct: number; pct: number; }
const row = (key: string, n: number, correct: number): Row => ({ key, n, correct, pct: n ? Math.round((correct / n) * 100) : 0 });

/** Only answered questions count toward accuracy; skipped ones are reported separately. */
export function summarize(attempts: ExamAttempt[], meta: Map<string, Question>) {
  const all = attempts.flatMap(a => a.answers.filter(x => x.selected !== null && meta.has(x.questionId)));
  const skipped = attempts.flatMap(a => a.answers).filter(x => x.selected === null).length;
  const group = (f: (q: Question) => string): Row[] => {
    const m = new Map<string, { n: number; c: number }>();
    for (const a of all) { const k = f(meta.get(a.questionId)!); const v = m.get(k) ?? { n: 0, c: 0 }; v.n++; if (a.correct) v.c++; m.set(k, v); }
    return [...m].map(([k, v]) => row(k, v.n, v.c)).sort((a, b) => a.key.localeCompare(b.key));
  };
  const correct = all.filter(a => a.correct).length;
  return {
    attempted: all.length, correct, incorrect: all.length - correct, skipped, accuracy: all.length ? Math.round((correct / all.length) * 100) : 0,
    byDomain: group(q => q.domain), byObjective: group(q => q.objective), byDifficulty: group(q => q.difficulty), byType: group(q => q.type), byKind: group(q => q.kind),
    history: attempts.map(a => { const n = a.answers.length; const c = a.answers.filter(x => x.correct).length; return { id: a.id, at: a.finishedAt, n, pct: n ? Math.round((c / n) * 100) : 0 }; }),
  };
}
/** Weak = at least minN answers and accuracy below threshold; lowest accuracy first. Never invents data. */
export function weakTopics(rows: Row[], minN = 2, threshold = 70): Row[] {
  return rows.filter(r => r.n >= minN && r.pct < threshold).sort((a, b) => a.pct - b.pct || b.n - a.n);
}
export const dueRevision = (rev: RevisionRecord[], now = new Date()) => rev.filter(r => new Date(r.dueAt).getTime() <= now.getTime());
export const lastWrong = (rev: RevisionRecord[]) => rev.filter(r => !r.lastResult);
