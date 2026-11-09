import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Bookmark } from 'lucide-react';
import { useI18n } from '../../i18n';
import { loadAllQuestions } from '../../services/content';
import { loadProgress, toggleBookmark } from '../../storage/store';
import type { Question } from '../../types/content';

const T = {
  en: { title: 'Bookmarks', empty: 'No bookmarks yet. Use the bookmark button in the Question Bank or the exam review.', load: 'Could not load questions.',
    remove: 'Remove bookmark', practice: 'Practice bookmarked questions', missing: 'Bookmarked question no longer exists in the content:', correct: 'Correct answer' },
  ar: { title: 'المفضلة', empty: 'لا توجد أسئلة مفضلة بعد. استخدم زر الإشارة المرجعية في بنك الأسئلة أو في مراجعة الاختبار.', load: 'تعذر تحميل الأسئلة.',
    remove: 'إزالة من المفضلة', practice: 'تدرّب على الأسئلة المفضلة', missing: 'السؤال المفضل لم يعد موجوداً في المحتوى:', correct: 'الإجابة الصحيحة' },
};
export default function BookmarksPage() {
  const { lang } = useI18n(); const t = T[lang];
  const [qs, setQs] = useState<Question[] | null>(null); const [err, setErr] = useState(false);
  const [ids, setIds] = useState<string[]>(() => loadProgress().bookmarks);
  useEffect(() => { loadAllQuestions().then(setQs).catch(() => setErr(true)); }, []);
  if (err) return <p role="alert" className="text-red-600">{t.load}</p>;
  if (!qs) return <p>…</p>;
  const byId = new Map(qs.map(q => [q.id, q]));
  return (<div className="space-y-3">
    <h1 className="text-2xl font-bold">{t.title} ({ids.length})</h1>
    {!ids.length ? <p>{t.empty}</p> : <Link className="inline-block rounded bg-teal-700 px-3 py-2 text-sm text-white" to="/exam?bookmarks=1">{t.practice}</Link>}
    {ids.map(id => { const q = byId.get(id);
      return (<article key={id} className="rounded border bg-white p-3 dark:border-slate-700 dark:bg-slate-800">
        {q ? <><div className="text-xs text-slate-500">{q.id} · {q.objective} · {q.difficulty}</div><p className="my-1 font-medium">{q.question[lang]}</p>
          <p className="text-sm">{t.correct}: {q.options.find(o => o.id === q.correctAnswer)!.text[lang]}</p><p className="mt-1 text-sm">{q.explanation[lang]}</p></>
          : <p className="text-sm">{t.missing} {id}</p>}
        <button className="mt-2 flex items-center gap-1 text-sm underline" onClick={() => setIds(toggleBookmark(id))}><Bookmark size={14} />{t.remove}</button></article>); })}
  </div>);
}
