import { useEffect, useMemo, useState } from 'react';
import { Bookmark, BookmarkCheck } from 'lucide-react';
import { useI18n } from '../i18n';
import { loadQuestions } from '../services/content';
import { loadProgress, toggleBookmark } from '../storage/store';
import { DIFFICULTIES, type Question } from '../types/content';

export default function QuestionBank() {
  const { t, lang } = useI18n();
  const [qs, setQs] = useState<Question[] | null>(null); const [err, setErr] = useState('');
  const [bm, setBm] = useState<string[]>(() => loadProgress().bookmarks); const [diff, setDiff] = useState('all'); const [open, setOpen] = useState<string | null>(null);
  useEffect(() => { loadQuestions('data-management').then(setQs).catch(() => setErr(t('loadFail'))); }, []);
  const list = useMemo(() => (qs ?? []).filter(q => diff === 'all' || q.difficulty === diff), [qs, diff]);
  if (err) return <p role="alert" className="text-red-600">{err}</p>;
  if (!qs) return <p>…</p>;
  if (!qs.length) return <p>{t('empty')}</p>;
  return (<div className="space-y-3">
    <h1 className="text-2xl font-bold">{t('bank')}</h1>
    <p className="text-sm text-slate-500">{t('bankNote')} ({qs.length})</p>
    <select className="rounded border p-2 dark:bg-slate-800" value={diff} onChange={e => setDiff(e.target.value)} aria-label={t('difficulty')}>
      <option value="all">{t('all')}</option>{DIFFICULTIES.map(d => <option key={d}>{d}</option>)}</select>
    {list.map(q => (<article key={q.id} className="rounded border bg-white p-3 dark:border-slate-700 dark:bg-slate-800">
      <div className="flex items-center justify-between text-xs text-slate-500"><span>{q.id} · {q.difficulty} · {q.type}</span>
        <button aria-pressed={bm.includes(q.id)} aria-label={t('bookmark')} title={t('bookmark')} onClick={() => setBm(toggleBookmark(q.id))}>{bm.includes(q.id) ? <BookmarkCheck size={18} className="text-teal-600" /> : <Bookmark size={18} />}</button></div>
      <p className="my-2 font-medium">{q.question[lang]}</p>
      <ul className="space-y-1">{q.options.map(o => <li key={o.id}>
        <span className={open === q.id && o.id === q.correctAnswer ? 'font-semibold text-teal-700 dark:text-teal-400' : ''}>{o.id}. {o.text[lang]}</span></li>)}</ul>
      <button className="mt-2 text-sm underline" onClick={() => setOpen(open === q.id ? null : q.id)}>{open === q.id ? t('hide') : t('show')}</button>
      {open === q.id && <div className="mt-2 space-y-1 text-sm"><p>{q.explanation[lang]}</p>
        {(Object.entries(q.incorrectOptionsExplanation[lang]) as [string, string][]).map(([k, v]) => <p key={k}><b>{k}:</b> {v}</p>)}
        <p className="text-xs">{q.references.map(r => <a key={r.url} className="underline" href={r.url} target="_blank" rel="noreferrer">{r.title}</a>)}</p></div>}
    </article>))}
  </div>);
}
