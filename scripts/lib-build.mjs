import { readFileSync, writeFileSync } from 'node:fs';
const IDS = ['A', 'B', 'C', 'D'];
/** rows: [id, difficulty, type, tools, qEn, qAr, opts[[en,ar]x4], answerIndex, expEn, expAr, why[[en,ar]x3 in option order, skipping the correct one]] */
export function appendQuestions(file, rows, ref, objective, domain = 'Data Management') {
  const add = rows.map(([id, difficulty, type, tools, qen, qar, opts, ans, een, ear, why]) => {
    if (opts.length !== 4 || why.length !== 3) throw new Error(id + ': need 4 options and 3 explanations');
    const wrong = IDS.filter((_, i) => i !== ans);
    return { id, kind: 'mcq', domain, objective, difficulty, type, tools, question: { en: qen, ar: qar },
      options: opts.map((o, i) => ({ id: IDS[i], text: { en: o[0], ar: o[1] } })), correctAnswer: IDS[ans], explanation: { en: een, ar: ear },
      incorrectOptionsExplanation: { en: Object.fromEntries(wrong.map((w, i) => [w, why[i][0]])), ar: Object.fromEntries(wrong.map((w, i) => [w, why[i][1]])) }, references: [ref] };
  });
  const cur = JSON.parse(readFileSync(file, 'utf8')).filter(q => !add.some(a => a.id === q.id));
  writeFileSync(file, JSON.stringify([...cur, ...add], null, 2)); console.log('total', cur.length + add.length);
}
