import { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { useI18n } from '../../i18n';
import { loadAllQuestions } from '../../services/content';
import { loadProgress } from '../../storage/store';
import type { Question } from '../../types/content';
import { dueRevision, lastWrong } from './stats';

const T = {
  en: { title: 'Revision Center', empty: 'Nothing to revise yet. Questions you answer in the simulator enter the schedule automatically.', due: 'Due for review now', wrong: 'Last answered incorrectly',
    go: 'Practice due questions', rule: 'Schedule: a wrong or skipped answer returns after 1 day; each further correct answer lengthens the gap (2, 4, 8, 16, 32 days).', box: 'Box', flagged: 'Flagged questions', load: 'Could not load questions.' },
  ar: { title: 'مركز المراجعة', empty: 'لا شيء للمراجعة بعد. الأسئلة التي تجيب عنها في المحاكي تدخل الجدول تلقائياً.', due: 'مستحقة للمراجعة الآن', wrong: 'أُجيب عنها خطأً آخر مرة',
    go: 'تدرّب على الأسئلة المستحقة', rule: 'الجدول: الإجابة الخاطئة أو المتروكة تعود بعد يوم؛ وكل إجابة صحيحة إضافية تطيل الفاصل (2 و4 و8 و16 و32 يوماً).', box: 'المرحلة', flagged: 'أسئلة معلَّمة', load: 'تعذر تحميل الأسئلة.' },
};
export default function RevisionPage() {
  const { lang } = useI18n(); const t = T[lang];
  const [qs, setQs] = useState<Question[] | null>(null); const [err, setErr] = useState(false);
  useEffect(() => { loadAllQuestions().then(setQs).catch(() => setErr(true)); }, []);
  const p = useMemo(loadProgress, []); const due = dueRevision(p.revision); const wrong = lastWrong(p.revision);
  if (err) return <p role="alert" className="text-red-600">{t.load}</p>;
  if (!qs) return <p>…</p>;
  const byId = new Map(qs.map(q => [q.id, q]));
  if (!p.revision.length) return <div className="space-y-2"><h1 className="text-2xl font-bold">{t.title}</h1><p>{t.empty}</p></div>;
  return (<div className="space-y-4">
    <h1 className="text-2xl font-bold">{t.title}</h1><p className="text-sm">{t.rule}</p>
    <p>{t.due}: <b>{due.length}</b> · {t.wrong}: <b>{wrong.length}</b> · {t.flagged}: <b>{p.flagged.length}</b></p>
    {due.length > 0 && <Link className="inline-block rounded bg-teal-700 px-3 py-2 text-sm text-white" to="/exam?due=1">{t.go}</Link>}
    <ul className="space-y-2">{due.map(r => { const q = byId.get(r.questionId); return q && (<li key={r.questionId} className="rounded border bg-white p-3 text-sm dark:border-slate-700 dark:bg-slate-800">
      <span className="text-xs text-slate-500">{q.id} · {q.objective} · {t.box} {r.box}</span><p>{q.question[lang]}</p></li>); })}</ul>
  </div>);
}
