import assert from 'node:assert/strict';
import { summarize, weakTopics, dueRevision, lastWrong } from '../src/features/analytics/stats';
const mk = (id: string, objective: string, domain = 'Data Management'): any => ({ id, objective, domain, difficulty: 'Beginner', type: 'Conceptual', kind: 'mcq' });
const meta = new Map<string, any>([['a', mk('a', 'CS')], ['b', mk('b', 'CS')], ['c', mk('c', 'Domains')], ['d', mk('d', 'Domains')]]);
const ans = (id: string, selected: string | null, correct: boolean) => ({ questionId: id, selected, correct, flagged: false, ms: 0 });
const attempts: any = [{ id: '1', finishedAt: 'x', answers: [ans('a', 'A', false), ans('b', 'A', false), ans('c', 'A', true), ans('d', null, false)] },
  { id: '2', finishedAt: 'y', answers: [ans('a', 'A', true), ans('c', 'A', true)] }];
const s = summarize(attempts, meta);
assert.equal(s.attempted, 5); assert.equal(s.correct, 3); assert.equal(s.skipped, 1); assert.equal(s.accuracy, 60);
assert.deepEqual(s.byObjective.map(r => [r.key, r.n, r.pct]), [['CS', 3, 33], ['Domains', 2, 100]]);
assert.deepEqual(weakTopics(s.byObjective).map(r => r.key), ['CS']);
assert.equal(weakTopics(s.byObjective, 4).length, 0, 'insufficient data -> no weak topics');
assert.equal(summarize([], meta).accuracy, 0);
const rev: any = [{ questionId: 'a', box: 0, lastResult: false, dueAt: '2026-01-01T00:00:00Z' }, { questionId: 'b', box: 2, lastResult: true, dueAt: '2099-01-01T00:00:00Z' }];
assert.equal(dueRevision(rev, new Date('2026-06-01')).length, 1); assert.equal(lastWrong(rev).length, 1);
console.log('stats tests passed');
