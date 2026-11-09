import { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { useI18n } from '../../i18n';
import { loadAllQuestionsAndScenarios } from '../../services/content';
import { loadProgress } from '../../storage/store';
import type { Question } from '../../types/content';
import { summarize, weakTopics, type Row } from './stats';
import { Award, Target, AlertTriangle, Play, Sparkles, CheckCircle2 } from 'lucide-react';

const T = {
  en: {
    title: 'Performance & Readiness Analytics',
    load: 'Could not load questions.',
    empty: 'No exam attempts recorded yet. Complete an exam in the simulator and your diagnostics will appear here.',
    attempted: 'Questions Answered',
    correct: 'Correct Answers',
    incorrect: 'Incorrect',
    acc: 'Overall Accuracy',
    skipped: 'Skipped',
    readiness: 'Exam Readiness Index',
    readinessSub: 'Calculated from cumulative accuracy, blueprint domain coverage, and question pool mastery.',
    readyBadge: 'READY FOR PEARSON VUE',
    trackBadge: 'ON TRACK — FURTHER DRILL RECOMMENDED',
    studyBadge: 'NEEDS COMPREHENSIVE STUDY',
    domain: 'Blueprint Domain Performance',
    diff: 'Performance by Difficulty Level',
    type: 'Performance by Question Type',
    obj: 'Performance by Blueprint Objective',
    weak: 'Weak Topics & Priority Knowledge Gaps',
    weakNone: 'No weak topics detected (accuracy is at least 70% across all tested objectives). Excellent work!',
    practice: 'Practice Topic Now',
    hist: 'Simulation Attempt History',
    note: 'All performance statistics are calculated locally from exam sessions recorded on this device.'
  },
  ar: {
    title: 'لوحة تحليلات الأداء والجاهزية للاختبار',
    load: 'تعذر تحميل الأسئلة.',
    empty: 'لا توجد محاولات اختبار مسجلة بعد. أكمل جلسة في المحاكي وستظهر تشخيصاتك هنا فوراً.',
    attempted: 'الأسئلة المجاب عنها',
    correct: 'الإجابات الصحيحة',
    incorrect: 'الإجابات الخاطئة',
    acc: 'نسبة الدقة الإجمالية',
    skipped: 'الأسئلة المتروكة',
    readiness: 'مؤشر الجاهزية للاختبار الرسمي',
    readinessSub: 'محسوب استناداً إلى دقة الإجابات، وتغطية نطاقات المنهج الأربعة، ونسبة استيعاب بنك الأسئلة.',
    readyBadge: 'مؤهل وجاهز لاجتياز اختبار PEARSON VUE',
    trackBadge: 'في المسار الصحيح — يوصى بمزيد من التدريب',
    studyBadge: 'يحتاج إلى مذاكرة ومراجعة مكثفة',
    domain: 'الأداء حسب نطاقات الاختبار المعتمدة',
    diff: 'الأداء حسب مستويات الصعوبة',
    type: 'الأداء حسب نوع الأسئلة',
    obj: 'الأداء حسب الأهداف التفصيلية للاختبار',
    weak: 'المواضيع الضعيفة والفجوات المعرفية ذات الأولوية',
    weakNone: 'لم يتم رصد أي مواضيع ضعيفة (الدقة 70% أو أعلى في كافة الأهداف المختبرة). عمل ممتاز!',
    practice: 'تدرّب على هذا الهدف الآن',
    hist: 'سجل جلسات المحاكاة السابقة',
    note: 'كافة الإحصائيات محسوبة محلياً من جلسات الاختبار المسجلة على هذا الجهاز دون إرسال أي بيانات.'
  }
};

const Bars = ({ rows }: { rows: Row[] }) => (
  <ul className="space-y-2.5">
    {rows.map(r => (
      <li key={r.key} className="space-y-1">
        <div className="flex justify-between text-xs font-medium">
          <span className="text-slate-700 dark:text-slate-300">{r.key}</span>
          <span className="font-mono">
            {r.correct}/{r.n} · {r.pct}%
          </span>
        </div>
        <div className="h-2 rounded-full bg-slate-100 dark:bg-slate-800 overflow-hidden">
          <div
            className={`h-2 rounded-full transition-all duration-300 ${
              r.pct >= 70 ? 'bg-emerald-500' : r.pct >= 50 ? 'bg-amber-500' : 'bg-rose-500'
            }`}
            style={{ width: `${r.pct}%` }}
          />
        </div>
      </li>
    ))}
  </ul>
);

export default function AnalyticsPage() {
  const { lang } = useI18n();
  const t = T[lang];
  const [qs, setQs] = useState<Question[] | null>(null);
  const [err, setErr] = useState(false);

  useEffect(() => {
    loadAllQuestionsAndScenarios().then(setQs).catch(() => setErr(true));
  }, []);

  const attempts = useMemo(() => loadProgress().attempts, []);
  const s = useMemo(() => (qs ? summarize(attempts, new Map(qs.map(q => [q.id, q]))) : null), [qs, attempts]);

  // Calculate Exam Readiness Index (0 - 100)
  const readinessScore = useMemo(() => {
    if (!s || s.attempted === 0) return 0;
    const accuracyComponent = Math.min(100, s.accuracy) * 0.5; // 50%
    const poolCoverage = Math.min(100, Math.round((s.attempted / Math.max(1, (qs?.length ?? 400))) * 100)) * 0.3; // 30%
    const domainPassCount = s.byDomain.filter(d => d.pct >= 70).length;
    const domainComponent = Math.round((domainPassCount / Math.max(1, s.byDomain.length)) * 100) * 0.2; // 20%
    return Math.min(100, Math.round(accuracyComponent + poolCoverage + domainComponent));
  }, [s, qs]);

  if (err) return <p role="alert" className="text-rose-600 font-bold p-4">{t.load}</p>;
  if (!qs) return <div className="flex h-64 items-center justify-center text-slate-500 animate-pulse">Loading analytics...</div>;

  const card = 'rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900';

  if (!attempts.length) {
    return (
      <div className="space-y-6">
        <div className="rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl space-y-2">
          <h1 className="text-2xl font-black">{t.title}</h1>
          <p className="text-xs text-slate-300">{t.note}</p>
        </div>
        <div className={`${card} text-center py-12 space-y-4`}>
          <Target size={40} className="mx-auto text-slate-400" />
          <p className="text-slate-600 dark:text-slate-400 max-w-md mx-auto text-sm">{t.empty}</p>
          <Link
            to="/exam?preset=eapa75"
            className="inline-flex items-center gap-2 rounded-xl bg-sky-500 px-5 py-2.5 text-xs font-bold text-slate-950 shadow hover:bg-sky-400 transition"
          >
            <Play size={15} /> {lang === 'ar' ? 'ابدأ أول اختبار تجريبي' : 'Launch First Mock Exam'}
          </Link>
        </div>
      </div>
    );
  }

  const weak = weakTopics(s!.byObjective);

  let readinessBadge = t.studyBadge;
  let readinessColor = 'border-rose-500/40 bg-gradient-to-br from-slate-900 via-slate-800 to-rose-950/40 text-rose-400';
  if (readinessScore >= 80) {
    readinessBadge = t.readyBadge;
    readinessColor = 'border-emerald-500/40 bg-gradient-to-br from-slate-900 via-slate-800 to-emerald-950/40 text-emerald-400';
  } else if (readinessScore >= 60) {
    readinessBadge = t.trackBadge;
    readinessColor = 'border-amber-500/40 bg-gradient-to-br from-slate-900 via-slate-800 to-amber-950/40 text-amber-400';
  }

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl space-y-2">
        <h1 className="text-2xl font-black sm:text-3xl">{t.title}</h1>
        <p className="text-xs text-slate-300 leading-relaxed">{t.note}</p>
      </div>

      {/* Exam Readiness Index Score Card */}
      <div className={`rounded-2xl border p-6 shadow-xl space-y-3 ${readinessColor}`}>
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <Award size={18} />
              <span className="font-mono text-xs font-black uppercase tracking-wider">{readinessBadge}</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-black text-white">
              {t.readiness}: {readinessScore}/100
            </h2>
            <p className="text-xs text-slate-300 max-w-xl">{t.readinessSub}</p>
          </div>

          <Link
            to="/exam?preset=eapa75"
            className="flex items-center gap-1.5 rounded-xl bg-white px-4 py-2.5 text-xs font-bold text-slate-950 shadow hover:bg-slate-100 transition"
          >
            <Play size={14} /> {lang === 'ar' ? 'اختبار تجريبي جديد' : 'New Mock Exam'}
          </Link>
        </div>
      </div>

      {/* Cumulative Metrics Grid */}
      <dl className="grid grid-cols-2 gap-3 sm:grid-cols-5">
        {[
          [t.attempted, s!.attempted],
          [t.correct, s!.correct],
          [t.incorrect, s!.incorrect],
          [t.skipped, s!.skipped],
          [t.acc, `${s!.accuracy}%`]
        ].map(([k, v]) => (
          <div key={String(k)} className={`${card} text-center space-y-1`}>
            <dt className="text-[11px] font-bold text-slate-500 dark:text-slate-400">{k}</dt>
            <dd className="text-2xl font-black font-mono text-slate-900 dark:text-white">{v}</dd>
          </div>
        ))}
      </dl>

      {/* Weak Topics Section */}
      <section className={`${card} space-y-3`}>
        <div className="flex items-center gap-2 text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
          <AlertTriangle size={16} className="text-amber-500" />
          <h2>{t.weak}</h2>
        </div>
        {weak.length ? (
          <ul className="space-y-2">
            {weak.map(w => (
              <li
                key={w.key}
                className="flex flex-wrap items-center justify-between gap-3 rounded-xl border border-amber-200 bg-amber-50/50 p-3 text-xs dark:border-amber-900/40 dark:bg-amber-950/20"
              >
                <div>
                  <strong className="text-slate-900 dark:text-white block">{w.key}</strong>
                  <span className="font-mono text-amber-700 dark:text-amber-400 text-[11px]">
                    {w.correct}/{w.n} correct ({w.pct}%)
                  </span>
                </div>
                <Link
                  className="rounded-lg bg-amber-500 px-3 py-1.5 font-bold text-slate-950 shadow-sm hover:bg-amber-400 transition"
                  to={`/exam?objective=${encodeURIComponent(w.key)}`}
                >
                  {t.practice} &rarr;
                </Link>
              </li>
            ))}
          </ul>
        ) : (
          <div className="flex items-center gap-2 text-xs text-emerald-600 dark:text-emerald-400 py-2">
            <CheckCircle2 size={16} /> {t.weakNone}
          </div>
        )}
      </section>

      {/* Domain Breakdown */}
      <section className={`${card} space-y-3`}>
        <h2 className="text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
          {t.domain}
        </h2>
        <Bars rows={s!.byDomain} />
      </section>

      {/* Objective Breakdown */}
      <section className={`${card} space-y-3`}>
        <h2 className="text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
          {t.obj}
        </h2>
        <Bars rows={s!.byObjective} />
      </section>

      {/* Difficulty Breakdown */}
      <section className={`${card} space-y-3`}>
        <h2 className="text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
          {t.diff}
        </h2>
        <Bars rows={s!.byDifficulty} />
      </section>

      {/* Question Type Breakdown */}
      <section className={`${card} space-y-3`}>
        <h2 className="text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
          {t.type}
        </h2>
        <Bars rows={s!.byType} />
      </section>

      {/* History */}
      <section className={`${card} space-y-3`}>
        <h2 className="text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
          {t.hist}
        </h2>
        <ul className="space-y-1.5 text-xs divide-y divide-slate-100 dark:divide-slate-800">
          {s!.history.map((h, k) => (
            <li key={h.id} className="pt-1.5 flex justify-between items-center text-slate-700 dark:text-slate-300">
              <span className="font-mono">
                #{k + 1} · {new Date(h.at).toLocaleDateString(lang)} {new Date(h.at).toLocaleTimeString(lang)}
              </span>
              <span
                className={`font-mono font-bold px-2 py-0.5 rounded ${
                  h.pct >= 70 ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300' : 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300'
                }`}
              >
                {h.pct}% ({h.n} Qs)
              </span>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
