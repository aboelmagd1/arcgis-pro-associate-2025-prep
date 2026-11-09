import { useSearchParams } from 'react-router-dom';
import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { useI18n } from '../../i18n';
import { loadAllQuestionsAndScenarios } from '../../services/content';
import { dueRevision } from '../analytics/stats';
import { Bookmark, BookmarkCheck, Strikethrough, Sparkles, Timer, CheckCircle2, XCircle, Flag, RotateCcw, ExternalLink } from 'lucide-react';
import { loadProgress, saveProgress, toggleBookmark } from '../../storage/store';
import { DOMAINS, type Question, type OptionId } from '../../types/content';
import { buildExam, buildOfficialExam, grade, scorePct, updateRevision, type ExamItem } from './logic';

const T = {
  en: {
    title: 'Pearson VUE Exam Simulator',
    load: 'Could not load question bank.',
    fDomain: 'Domain',
    fDiff: 'Difficulty',
    fObj: 'Objective',
    all: 'All',
    dueOnly: 'Only questions due for revision',
    bmOnly: 'Only bookmarked questions',
    scenariosOnly: 'Only scenario-based questions (150)',
    bookmark: 'Bookmark',
    none: 'No questions available.',
    avail: 'Questions in pool',
    count: 'Number of questions',
    timed: 'Timed Mode (90 minutes for 75 Qs)',
    minutes: 'Minutes',
    start: 'Start Exam',
    note: 'Simulates the official Esri ArcGIS Pro Associate 2025 (EAPA_2025) examination under real-world testing conditions. Answers are hidden until final submission.',
    officialBadge: 'Official EAPA_2025 Benchmark',
    officialDesc: '75 Questions · 90 Minutes · Domain-weighted (32% Data Mgmt, 25% Viz, 25% Analysis, 18% Layouts)',
    q: 'Question',
    of: 'of',
    prev: 'Previous',
    next: 'Next',
    flag: 'Flag for Review',
    unflag: 'Remove Flag',
    submit: 'Submit Exam',
    left: 'Time Left',
    unanswered: 'unanswered',
    flagged: 'flagged',
    confirm: 'Submit your exam now? Unanswered: {u}, Flagged: {f}. Results cannot be changed once submitted.',
    score: 'Final Score',
    passIndicator: 'Passing threshold is approximately 70% based on historical Esri Associate benchmark standards.',
    passed: 'PASS — Candidate Meets Exam Standard',
    failed: 'DID NOT PASS — Further Review Recommended',
    byDomain: 'Performance by Blueprint Domain',
    review: 'Detailed Answer Key & Technical Rationales',
    yours: 'Your answer',
    correct: 'Correct answer',
    none2: 'No answer selected',
    again: 'New Exam Session',
    saved: 'Exam session performance recorded on this device.',
    refs: 'Official Esri References'
  },
  ar: {
    title: 'محاكي اختبار بيرسون فيو (Pearson VUE)',
    load: 'تعذر تحميل بنك الأسئلة والسيناريوهات.',
    fDomain: 'المجال',
    fDiff: 'الصعوبة',
    fObj: 'الهدف',
    all: 'الكل',
    dueOnly: 'الأسئلة المستحقة للمراجعة فقط',
    bmOnly: 'الأسئلة المفضلة فقط',
    scenariosOnly: 'سيناريوهات العمل الواقعية فقط (150)',
    bookmark: 'إضافة للمفضلة',
    none: 'لا توجد أسئلة متاحة مطابقة للمحددات.',
    avail: 'الأسئلة المتاحة في البنك',
    count: 'عدد الأسئلة',
    timed: 'وضع التوقيت الزمني (90 دقيقة لـ 75 سؤالاً)',
    minutes: 'الدقائق',
    start: 'ابدأ الاختبار الآن',
    note: 'يحاكي الاختبار الرسمي لشهادة Esri ArcGIS Pro Associate 2025 (EAPA_2025) وفق ظروف الاختبار الحقيقية. تُحجب الإجابات والتفسيرات حتى التسليم النهائي.',
    officialBadge: 'النموذج الرسمي المعياري EAPA_2025',
    officialDesc: '75 سؤالاً · 90 دقيقة · أوزان المجالات المعتمدة (32% إدارة البيانات، 25% العرض، 25% التحليل، 18% النشر)',
    q: 'السؤال',
    of: 'من',
    prev: 'السابق',
    next: 'التالي',
    flag: 'تحديد للمراجعة',
    unflag: 'إلغاء التحديد',
    submit: 'تسليم الاختبار',
    left: 'الوقت المتبقي',
    unanswered: 'بلا إجابة',
    flagged: 'محدد للمراجعة',
    confirm: 'هل ترغب في تسليم الاختبار الآن؟ الأسئلة المتروكة: {u}، والأسئلة المحددة: {f}. لن تتمكن من التعديل بعد التسليم.',
    score: 'النتيجة النهائية',
    passIndicator: 'درجة النجاح المعتادة لشهادات Esri Associate هي حوالي 70% وفق المعايير المعتمدة.',
    passed: 'ناجح (PASS) — مستواك مؤهل للاختبار الرسمي',
    failed: 'لم تجتز (DID NOT PASS) — يوصى بمراجعة المواضيع الضعيفة',
    byDomain: 'تقرير الأداء حسب محاور الاختبار',
    review: 'مراجعة الإجابات والتفسيرات العلمية الدقيقة',
    yours: 'إجابتك المختارة',
    correct: 'الإجابة الصحيحة المعتمدة',
    none2: 'لم يتم اختيار إجابة',
    again: 'بدء جلسة اختبار جديدة',
    saved: 'تم تسجيل نتائج المحاولة وإضافتها لسجل الأداء على هذا الجهاز.',
    refs: 'المراجع والتوثيق الرسمي من Esri'
  }
};

type Phase = 'setup' | 'run' | 'done';

export default function ExamPage() {
  const { lang } = useI18n();
  const t = T[lang];
  const [sp] = useSearchParams();

  const [pool, setPool] = useState<Question[] | null>(null);
  const [err, setErr] = useState(false);
  const [phase, setPhase] = useState<Phase>('setup');

  // Configuration
  const [count, setCount] = useState(75);
  const [timed, setTimed] = useState(true);
  const [mins, setMins] = useState(90);
  const [isOfficialPreset, setIsOfficialPreset] = useState(true);
  const [onlyScenarios, setOnlyScenarios] = useState(sp.get('preset') === 'scenarios');

  // Exam runtime
  const [items, setItems] = useState<ExamItem[]>([]);
  const [i, setI] = useState(0);
  const [sel, setSel] = useState<Record<string, OptionId>>({});
  const [flags, setFlags] = useState<Set<string>>(new Set());
  const [strikes, setStrikes] = useState<Record<string, Record<string, boolean>>>({});
  const [left, setLeft] = useState(0);
  const startedAt = useRef('');

  // Filters
  const [dom, setDom] = useState(sp.get('domain') ?? 'all');
  const [dif, setDif] = useState('all');
  const [obj, setObj] = useState(sp.get('objective') ?? 'all');
  const [dueOnly, setDueOnly] = useState(sp.get('due') === '1');
  const [bmOnly, setBmOnly] = useState(sp.get('bookmarks') === '1');
  const [bm, setBm] = useState<string[]>(() => loadProgress().bookmarks);

  // Load all 400 questions (250 MCQs + 150 Scenarios)
  useEffect(() => {
    loadAllQuestionsAndScenarios()
      .then(p => {
        setPool(p);
        const preset = sp.get('preset');
        const domainParam = sp.get('domain');

        if (domainParam || preset === 'domain') {
          setIsOfficialPreset(false);
          setCount(25);
          setTimed(false);
          setMins(30);
          if (domainParam) setDom(domainParam);
        } else if (preset === 'scenarios') {
          setIsOfficialPreset(false);
          setOnlyScenarios(true);
          setCount(30);
          setTimed(true);
          setMins(36);
        } else if (preset === 'eapa75' || !preset) {
          setIsOfficialPreset(true);
          setCount(75);
          setTimed(true);
          setMins(90);
        }
      })
      .catch(() => setErr(true));
  }, [sp]);

  const filtered = useMemo(() => {
    if (!pool) return [];
    const bmIds = new Set(loadProgress().bookmarks);
    const dueIds = new Set(dueRevision(loadProgress().revision).map(r => r.questionId));

    return pool.filter(q => {
      if (dom !== 'all' && q.domain !== dom) return false;
      if (dif !== 'all' && q.difficulty !== dif) return false;
      if (obj !== 'all' && q.objective !== obj) return false;
      if (dueOnly && !dueIds.has(q.id)) return false;
      if (bmOnly && !bmIds.has(q.id)) return false;
      if (onlyScenarios && q.kind !== 'scenario') return false;
      return true;
    });
  }, [pool, dom, dif, obj, dueOnly, bmOnly, onlyScenarios, bm]);

  useEffect(() => {
    if (!isOfficialPreset) {
      setCount(c => Math.min(Math.max(1, c), Math.max(1, filtered.length)));
    }
  }, [filtered.length, isOfficialPreset]);

  useEffect(() => {
    if (!isOfficialPreset) {
      setMins(Math.max(1, Math.round(count * 1.2)));
    }
  }, [count, isOfficialPreset]);

  const startExam = (official: boolean = false) => {
    if (!pool) return;
    let chosenItems: ExamItem[];
    if (official) {
      chosenItems = buildOfficialExam(pool);
    } else {
      chosenItems = buildExam(filtered, count);
    }
    setItems(chosenItems);
    setSel({});
    setFlags(new Set());
    setStrikes({});
    setI(0);
    setLeft((official ? 90 : mins) * 60);
    startedAt.current = new Date().toISOString();
    setPhase('run');
  };

  const finish = useCallback(() => {
    const answers = grade(items, sel, flags);
    const p = loadProgress();
    p.attempts.push({
      id: String(Date.now()),
      startedAt: startedAt.current,
      finishedAt: new Date().toISOString(),
      mode: isOfficialPreset ? 'official_eapa_2025' : 'custom_practice',
      timed,
      answers
    });
    p.revision = updateRevision(p.revision, answers);
    p.flagged = [...new Set([...p.flagged, ...flags])];
    try {
      saveProgress(p);
    } catch {
      // storage quota
    }
    setPhase('done');
  }, [items, sel, flags, timed, isOfficialPreset]);

  // Timer countdown
  useEffect(() => {
    if (phase !== 'run' || !timed) return;
    if (left <= 0) {
      finish();
      return;
    }
    const id = setTimeout(() => setLeft(l => l - 1), 1000);
    return () => clearTimeout(id);
  }, [phase, timed, left, finish]);

  // Strikethrough toggling
  const toggleStrike = (qid: string, optId: string) => {
    setStrikes(prev => {
      const cur = prev[qid] ?? {};
      return { ...prev, [qid]: { ...cur, [optId]: !cur[optId] } };
    });
  };

  // Keyboard navigation during exam
  useEffect(() => {
    if (phase !== 'run' || !items[i]) return;
    const currentQ = items[i].q;
    const currentOrder = items[i].order;

    const onKey = (e: KeyboardEvent) => {
      const k = e.key.toUpperCase();
      if (['A', 'B', 'C', 'D'].includes(k)) {
        const idx = 'ABCD'.indexOf(k);
        if (currentOrder[idx]) {
          setSel(prev => ({ ...prev, [currentQ.id]: currentOrder[idx] }));
        }
      } else if (k === 'N' || e.key === 'ArrowRight') {
        if (i < items.length - 1) setI(i + 1);
      } else if (k === 'P' || e.key === 'ArrowLeft') {
        if (i > 0) setI(i - 1);
      } else if (k === 'F') {
        const next = new Set(flags);
        next.has(currentQ.id) ? next.delete(currentQ.id) : next.add(currentQ.id);
        setFlags(next);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [phase, items, i, flags]);

  const answers = useMemo(() => (phase === 'done' ? grade(items, sel, flags) : []), [phase, items, sel, flags]);

  if (err) return <p role="alert" className="text-rose-600 font-bold p-4">{t.load}</p>;
  if (!pool) return <div className="flex h-64 items-center justify-center text-slate-500 animate-pulse">Loading exam pool (400 questions)...</div>;

  const btn = 'rounded-xl border px-4 py-2 text-xs font-bold transition disabled:opacity-40';
  const card = 'rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900';

  // SETUP PHASE
  if (phase === 'setup') {
    return (
      <div className="space-y-6">
        {/* Banner */}
        <div className="rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl space-y-3">
          <div className="inline-flex items-center gap-1.5 rounded-full bg-sky-500/20 px-3 py-1 text-xs font-semibold text-sky-300">
            <Timer size={14} /> {lang === 'ar' ? 'محاكي Pearson VUE المعتمد لشهادة 2025' : 'Official Pearson VUE Exam Engine'}
          </div>
          <h1 className="text-2xl font-black sm:text-3xl">{t.title}</h1>
          <p className="max-w-2xl text-xs text-slate-300 sm:text-sm leading-relaxed">{t.note}</p>
        </div>

        {/* Preset Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Preset 1: Official 75Q Simulation */}
          <div
            onClick={() => {
              setIsOfficialPreset(true);
              setOnlyScenarios(false);
              setCount(75);
              setTimed(true);
              setMins(90);
              startExam(true);
            }}
            className="group cursor-pointer rounded-2xl border-2 border-sky-500 bg-gradient-to-br from-slate-900 via-slate-850 to-sky-950/40 p-6 text-white shadow-xl hover:border-sky-400 transition space-y-3 relative overflow-hidden"
          >
            <div className="flex items-center justify-between">
              <span className="rounded-full bg-sky-500 px-3 py-1 font-mono text-xs font-black text-slate-950 uppercase tracking-wider">
                {t.officialBadge}
              </span>
              <Sparkles size={18} className="text-sky-400" />
            </div>
            <h2 className="text-xl font-bold group-hover:text-sky-300 transition">
              {lang === 'ar' ? 'محاكاة الاختبار الرسمي الكامل (75 سؤالاً / 90 دقيقة)' : 'Official 75Q / 90-Min Exam Simulation'}
            </h2>
            <p className="text-xs text-slate-300 leading-relaxed">{t.officialDesc}</p>
            <div className="pt-2 flex items-center text-xs font-bold text-sky-400">
              <span>{lang === 'ar' ? 'ابدأ الاختبار الرسمي الآن' : 'Launch Official Simulation'} &rarr;</span>
            </div>
          </div>

          {/* Preset 2: 150 Scenario Drill */}
          <div
            onClick={() => {
              setIsOfficialPreset(false);
              setOnlyScenarios(true);
              setCount(35);
              setTimed(true);
              setMins(42);
            }}
            className="cursor-pointer rounded-2xl border border-slate-200 bg-white p-6 shadow-sm hover:border-amber-400 dark:border-slate-800 dark:bg-slate-900 transition space-y-3"
          >
            <div className="flex items-center justify-between">
              <span className="rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-300 dark:border-amber-900/40 px-3 py-1 font-mono text-xs font-bold">
                {lang === 'ar' ? 'تدريب السيناريوهات المركبة' : 'Workplace Scenarios Drill'}
              </span>
            </div>
            <h2 className="text-xl font-bold text-slate-900 dark:text-white">
              {lang === 'ar' ? 'تحدي سيناريوهات بيئة العمل (150 سيناريو)' : '150 Workplace Scenario Challenges'}
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
              {lang === 'ar'
                ? 'تدرب حصرياً على السيناريوهات الطويلة والمواقف المعقدة التي تتطلب اتخاذ قرارات تقنية وحل الأخطاء.'
                : 'Focus exclusively on applied scenario questions testing problem solving, error troubleshooting, and tool selection.'}
            </p>
          </div>
        </div>

        {/* Custom Exam Builder Card */}
        <div className={`${card} space-y-4`}>
          <h2 className="text-base font-bold text-slate-900 dark:text-white border-b border-slate-100 dark:border-slate-800 pb-2">
            {lang === 'ar' ? 'أو قم بتهيئة اختبار مخصص حسب رغبتك:' : 'Or Customize Your Practice Session:'}
          </h2>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div>
              <label className="block font-bold text-slate-500 mb-1">{t.fDomain}</label>
              <select
                className="w-full rounded-xl border border-slate-300 bg-white p-2 text-slate-900 dark:border-slate-700 dark:bg-slate-950 dark:text-white focus:outline-none"
                value={dom}
                onChange={e => {
                  setDom(e.target.value);
                  setIsOfficialPreset(false);
                }}
              >
                <option value="all">{t.fDomain}: {t.all}</option>
                {DOMAINS.map(d => <option key={d}>{d}</option>)}
              </select>
            </div>

            <div>
              <label className="block font-bold text-slate-500 mb-1">{t.fDiff}</label>
              <select
                className="w-full rounded-xl border border-slate-300 bg-white p-2 text-slate-900 dark:border-slate-700 dark:bg-slate-950 dark:text-white focus:outline-none"
                value={dif}
                onChange={e => {
                  setDif(e.target.value);
                  setIsOfficialPreset(false);
                }}
              >
                <option value="all">{t.fDiff}: {t.all}</option>
                {['Beginner', 'Intermediate', 'Advanced'].map(d => <option key={d}>{d}</option>)}
              </select>
            </div>

            <div>
              <label className="block font-bold text-slate-500 mb-1">{lang === 'ar' ? 'نوع الأسئلة' : 'Question Kind'}</label>
              <select
                className="w-full rounded-xl border border-slate-300 bg-white p-2 text-slate-900 dark:border-slate-700 dark:bg-slate-950 dark:text-white focus:outline-none"
                value={onlyScenarios ? 'scenarios' : 'all'}
                onChange={e => {
                  setOnlyScenarios(e.target.value === 'scenarios');
                  setIsOfficialPreset(false);
                }}
              >
                <option value="all">{lang === 'ar' ? 'أسئلة وسيناريوهات (400)' : 'MCQs & Scenarios (400)'}</option>
                <option value="scenarios">{lang === 'ar' ? 'سيناريوهات فقط (150)' : 'Scenarios Only (150)'}</option>
              </select>
            </div>
          </div>

          <div className="flex flex-wrap gap-4 text-xs pt-1">
            <label className="flex items-center gap-1.5 cursor-pointer">
              <input type="checkbox" checked={dueOnly} onChange={e => { setDueOnly(e.target.checked); setIsOfficialPreset(false); }} className="rounded" />
              <span>{t.dueOnly}</span>
            </label>
            <label className="flex items-center gap-1.5 cursor-pointer">
              <input type="checkbox" checked={bmOnly} onChange={e => { setBmOnly(e.target.checked); setIsOfficialPreset(false); }} className="rounded" />
              <span>{t.bmOnly}</span>
            </label>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2 border-t border-slate-100 dark:border-slate-800 text-xs">
            <div>
              <label className="block font-bold text-slate-500 mb-1">
                {t.count} ({t.avail}: {filtered.length})
              </label>
              <input
                type="number"
                min={1}
                max={Math.max(1, filtered.length)}
                value={count}
                onChange={e => {
                  setCount(Math.min(filtered.length, Math.max(1, Number(e.target.value) || 1)));
                  setIsOfficialPreset(false);
                }}
                className="w-full rounded-xl border border-slate-300 bg-white p-2 dark:border-slate-700 dark:bg-slate-950 text-slate-900 dark:text-white"
              />
            </div>

            <div>
              <label className="block font-bold text-slate-500 mb-1">
                {t.timed} ({mins} {t.minutes})
              </label>
              <div className="flex items-center gap-2">
                <input
                  type="checkbox"
                  checked={timed}
                  onChange={e => setTimed(e.target.checked)}
                  className="rounded"
                />
                {timed && (
                  <input
                    type="number"
                    min={1}
                    max={180}
                    value={mins}
                    onChange={e => setMins(Math.max(1, Number(e.target.value) || 1))}
                    className="w-24 rounded-xl border border-slate-300 bg-white p-2 dark:border-slate-700 dark:bg-slate-950 text-slate-900 dark:text-white"
                  />
                )}
              </div>
            </div>
          </div>

          <div className="pt-2">
            <button
              disabled={!filtered.length}
              onClick={() => startExam(false)}
              className="w-full rounded-xl bg-teal-600 py-3 text-xs font-bold text-white shadow-md hover:bg-teal-500 transition disabled:opacity-40"
            >
              {t.start} ({count} Questions)
            </button>
          </div>
        </div>
      </div>
    );
  }

  // RUNNING PHASE
  if (phase === 'run') {
    const { q, order } = items[i];
    const opt = (id: OptionId) => q.options.find(o => o.id === id)!;
    const unanswered = items.filter(x => !sel[x.q.id]).length;
    const isFlagged = flags.has(q.id);
    const strikesForQ = strikes[q.id] ?? {};

    return (
      <div className="space-y-4">
        {/* Top Status Bar */}
        <div className="flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900 text-xs">
          <div className="flex items-center gap-3">
            <span className="font-mono font-bold text-slate-500">
              {t.q} {i + 1} {t.of} {items.length}
            </span>
            <span className="rounded bg-sky-50 dark:bg-sky-950/40 text-sky-700 dark:text-sky-300 px-2 py-0.5 font-bold">
              {q.domain}
            </span>
            {q.kind === 'scenario' && (
              <span className="rounded bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 px-2 py-0.5 font-bold">
                Scenario
              </span>
            )}
          </div>

          <div className="flex items-center gap-3">
            {timed && (
              <span
                role="timer"
                className={`font-mono text-sm font-bold flex items-center gap-1 ${
                  left < 300 ? 'text-rose-500 animate-pulse' : 'text-slate-700 dark:text-slate-300'
                }`}
              >
                <Timer size={14} /> {Math.floor(left / 60)}:{String(left % 60).padStart(2, '0')}
              </span>
            )}
            <button
              onClick={() => {
                const next = new Set(flags);
                next.has(q.id) ? next.delete(q.id) : next.add(q.id);
                setFlags(next);
              }}
              className={`flex items-center gap-1 rounded-lg px-2.5 py-1 transition ${
                isFlagged ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <Flag size={13} /> {isFlagged ? t.unflag : t.flag}
            </button>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="h-1.5 rounded-full bg-slate-200 dark:bg-slate-800 overflow-hidden">
          <div
            className="h-1.5 bg-sky-500 transition-all duration-300"
            style={{ width: `${((items.length - unanswered) / items.length) * 100}%` }}
          />
        </div>

        {/* Question & Options Card */}
        <div className={`${card} space-y-4`}>
          {/* Scenario Context (if present) */}
          {q.context && (
            <div className="rounded-xl border border-sky-200 bg-sky-50/70 p-4 dark:border-sky-900/40 dark:bg-sky-950/20 text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-medium">
              <strong className="block text-[10px] font-bold uppercase tracking-wider text-sky-700 dark:text-sky-400 mb-1">
                {lang === 'ar' ? 'سياق السيناريو وبيئة العمل:' : 'Scenario Context:'}
              </strong>
              {lang === 'ar' ? q.context.ar : q.context.en}
            </div>
          )}

          {/* Question Text */}
          <h3 className="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-relaxed">
            {lang === 'ar' ? q.question.ar : q.question.en}
          </h3>

          {/* Options with Strikethrough option eliminator */}
          <div role="radiogroup" className="space-y-2.5">
            {order.map((id, k) => {
              const isSelected = sel[q.id] === id;
              const isStruck = !!strikesForQ[id];

              return (
                <div
                  key={id}
                  onClick={() => setSel({ ...sel, [q.id]: id })}
                  className={`flex items-start justify-between gap-3 rounded-xl border p-3.5 cursor-pointer transition ${
                    isSelected
                      ? 'border-sky-500 bg-sky-50 dark:border-sky-500 dark:bg-sky-950/40 ring-1 ring-sky-500'
                      : 'border-slate-200 bg-white hover:border-slate-300 dark:border-slate-800 dark:bg-slate-900/60'
                  } ${isStruck ? 'opacity-40' : ''}`}
                >
                  <label className="flex items-start gap-3 cursor-pointer flex-1">
                    <input
                      type="radio"
                      name={q.id}
                      checked={isSelected}
                      onChange={() => setSel({ ...sel, [q.id]: id })}
                      className="mt-1 text-sky-600 focus:ring-sky-500"
                    />
                    <span className={`text-xs sm:text-sm leading-relaxed ${isStruck ? 'line-through text-slate-400' : 'text-slate-800 dark:text-slate-200'}`}>
                      <strong className="font-mono text-slate-500 me-1">{'ABCD'[k]}.</strong> {opt(id).text[lang]}
                    </span>
                  </label>

                  <button
                    onClick={e => {
                      e.stopPropagation();
                      toggleStrike(q.id, id);
                    }}
                    className={`rounded p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 ${
                      isStruck ? 'text-amber-500 bg-amber-50 dark:bg-amber-950/40' : ''
                    }`}
                    title="Eliminate option"
                  >
                    <Strikethrough size={14} />
                  </button>
                </div>
              );
            })}
          </div>
        </div>

        {/* Navigation Buttons */}
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex gap-2">
            <button className={btn} disabled={i === 0} onClick={() => setI(i - 1)}>
              {t.prev} (P)
            </button>
            <button className={btn} disabled={i === items.length - 1} onClick={() => setI(i + 1)}>
              {t.next} (N)
            </button>
          </div>

          <button
            className={`${btn} bg-rose-600 text-white hover:bg-rose-500`}
            onClick={() => {
              if (confirm(t.confirm.replace('{u}', String(unanswered)).replace('{f}', String(flags.size)))) {
                finish();
              }
            }}
          >
            {t.submit}
          </button>
        </div>

        {/* Question Grid Navigator */}
        <div className={`${card} space-y-2`}>
          <div className="flex items-center justify-between text-xs text-slate-500">
            <span>Question Navigator:</span>
            <span>
              {items.length - unanswered}/{items.length} answered · {flags.size} flagged
            </span>
          </div>
          <div className="flex flex-wrap gap-1 max-h-36 overflow-y-auto p-1">
            {items.map((x, k) => {
              const answered = !!sel[x.q.id];
              const flagged = flags.has(x.q.id);
              const current = k === i;

              let style = 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400';
              if (flagged) style = 'bg-amber-400 text-slate-950 font-bold';
              else if (answered) style = 'bg-teal-600 text-white font-bold';

              return (
                <button
                  key={x.q.id}
                  onClick={() => setI(k)}
                  className={`h-7 w-7 rounded-lg text-xs font-mono transition ${style} ${
                    current ? 'ring-2 ring-sky-500 ring-offset-1 dark:ring-offset-slate-900' : ''
                  }`}
                >
                  {k + 1}
                </button>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  // REVIEW & DONE PHASE
  const pct = scorePct(answers);
  const isPassed = pct >= 70;
  const by = DOMAINS.map(d => {
    const a = answers.filter((_, k) => items[k].q.domain === d);
    return { d, n: a.length, c: a.filter(x => x.correct).length };
  }).filter(x => x.n);

  return (
    <div className="space-y-6">
      {/* Score Card Banner */}
      <div
        className={`rounded-2xl border p-6 text-white shadow-xl space-y-3 ${
          isPassed
            ? 'border-emerald-500/40 bg-gradient-to-br from-slate-900 via-slate-800 to-emerald-950/40'
            : 'border-rose-500/40 bg-gradient-to-br from-slate-900 via-slate-800 to-rose-950/40'
        }`}
      >
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <span
              className={`rounded-full px-3 py-1 font-mono text-xs font-black uppercase tracking-wider ${
                isPassed ? 'bg-emerald-500 text-slate-950' : 'bg-rose-500 text-white'
              }`}
            >
              {isPassed ? t.passed : t.failed}
            </span>
            <h1 className="text-3xl font-black mt-2">
              {t.score}: {pct}% ({answers.filter(a => a.correct).length}/{answers.length})
            </h1>
            <p className="text-xs text-slate-300 mt-1">{t.passIndicator}</p>
          </div>

          <button
            onClick={() => setPhase('setup')}
            className="flex items-center gap-1.5 rounded-xl bg-white px-4 py-2.5 text-xs font-bold text-slate-950 shadow hover:bg-slate-100 transition"
          >
            <RotateCcw size={15} /> {t.again}
          </button>
        </div>
      </div>

      {/* Domain Breakdown */}
      <div className={`${card} space-y-3`}>
        <h2 className="text-base font-bold text-slate-900 dark:text-white">{t.byDomain}</h2>
        <div className="space-y-2">
          {by.map(x => {
            const domainPct = Math.round((x.c / x.n) * 100);
            return (
              <div key={x.d} className="space-y-1">
                <div className="flex justify-between text-xs font-medium">
                  <span className="text-slate-700 dark:text-slate-300">{x.d}</span>
                  <span className="font-mono">
                    {x.c}/{x.n} ({domainPct}%)
                  </span>
                </div>
                <div className="h-2 rounded-full bg-slate-100 dark:bg-slate-800 overflow-hidden">
                  <div
                    className={`h-2 rounded-full ${domainPct >= 70 ? 'bg-emerald-500' : 'bg-amber-500'}`}
                    style={{ width: `${domainPct}%` }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Review Questions List */}
      <div className="space-y-4">
        <h2 className="text-lg font-bold text-slate-900 dark:text-white">{t.review}</h2>
        {items.map(({ q, order }, k) => {
          const a = answers[k];
          const isCorrect = a.correct;
          const userChoice = a.selected ? `${'ABCD'[order.indexOf(a.selected)]}. ${q.options.find(o => o.id === a.selected)!.text[lang]}` : t.none2;
          const correctChoice = `${'ABCD'[order.indexOf(q.correctAnswer)]}. ${q.options.find(o => o.id === q.correctAnswer)!.text[lang]}`;

          return (
            <article
              key={q.id}
              className={`rounded-2xl border p-5 shadow-sm space-y-3 transition ${
                isCorrect
                  ? 'border-emerald-200 bg-white dark:border-emerald-950 dark:bg-slate-900'
                  : 'border-rose-200 bg-white dark:border-rose-950 dark:bg-slate-900'
              }`}
            >
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-2 dark:border-slate-800 text-xs">
                <div className="flex items-center gap-2">
                  <span
                    className={`flex h-6 w-6 items-center justify-center rounded-lg font-mono font-bold text-xs ${
                      isCorrect ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300' : 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300'
                    }`}
                  >
                    {k + 1}
                  </span>
                  <span className="font-mono font-bold text-slate-500">{q.id}</span>
                  <span className="rounded bg-slate-100 px-2 py-0.5 text-[10px] text-slate-600 dark:bg-slate-800 dark:text-slate-400">
                    {q.domain}
                  </span>
                  {q.kind === 'scenario' && (
                    <span className="rounded bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 px-2 py-0.5 text-[10px] font-bold">
                      Scenario
                    </span>
                  )}
                </div>

                <div className="flex items-center gap-2">
                  {isCorrect ? (
                    <span className="inline-flex items-center gap-1 font-bold text-emerald-600 text-xs">
                      <CheckCircle2 size={15} /> Correct
                    </span>
                  ) : (
                    <span className="inline-flex items-center gap-1 font-bold text-rose-600 text-xs">
                      <XCircle size={15} /> Incorrect
                    </span>
                  )}
                  <button
                    onClick={() => setBm(toggleBookmark(q.id))}
                    className="rounded p-1 text-slate-400 hover:text-amber-500"
                    title="Bookmark"
                  >
                    {bm.includes(q.id) ? <BookmarkCheck size={15} className="text-amber-500" /> : <Bookmark size={15} />}
                  </button>
                </div>
              </div>

              {/* Context if scenario */}
              {q.context && (
                <div className="rounded-xl border border-sky-200 bg-sky-50/50 p-3 dark:border-sky-900/40 dark:bg-sky-950/20 text-xs text-slate-700 dark:text-slate-300">
                  {lang === 'ar' ? q.context.ar : q.context.en}
                </div>
              )}

              {/* Question */}
              <div className="text-sm font-bold text-slate-900 dark:text-white">
                {lang === 'ar' ? q.question.ar : q.question.en}
              </div>

              {/* User vs Correct */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                <div className={`rounded-xl p-2.5 ${isCorrect ? 'bg-emerald-50 text-emerald-900 dark:bg-emerald-950/30 dark:text-emerald-300' : 'bg-rose-50 text-rose-900 dark:bg-rose-950/30 dark:text-rose-300'}`}>
                  <strong>{t.yours}:</strong> {userChoice}
                </div>
                <div className="rounded-xl p-2.5 bg-emerald-50 text-emerald-900 dark:bg-emerald-950/30 dark:text-emerald-300">
                  <strong>{t.correct}:</strong> {correctChoice}
                </div>
              </div>

              {/* Rationale */}
              <div className="rounded-xl border border-slate-100 bg-slate-50/60 p-3 dark:border-slate-800 dark:bg-slate-950/40 text-xs text-slate-700 dark:text-slate-300 leading-relaxed">
                <strong className="block text-slate-900 dark:text-white mb-1">
                  {lang === 'ar' ? 'التفسير العلمي المعتمد:' : 'Official Technical Rationale:'}
                </strong>
                {lang === 'ar' ? q.explanation.ar : q.explanation.en}
              </div>

              {/* Distractor explanations */}
              {q.incorrectOptionsExplanation && (
                <div className="space-y-1 text-xs text-slate-500 dark:text-slate-400">
                  {(Object.entries(q.incorrectOptionsExplanation[lang] ?? {}) as [OptionId, string][]).map(([id, v]) => (
                    <div key={id} className="flex items-start gap-1.5">
                      <span className="font-mono font-bold text-rose-500">{'ABCD'[order.indexOf(id)]}:</span>
                      <span>{v}</span>
                    </div>
                  ))}
                </div>
              )}

              {/* Official Doc References */}
              {q.references && q.references.length > 0 && (
                <div className="pt-1">
                  <a
                    href={q.references[0].url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 text-[11px] font-semibold text-sky-600 hover:underline dark:text-sky-400"
                  >
                    <ExternalLink size={12} /> {q.references[0].title}
                  </a>
                </div>
              )}
            </article>
          );
        })}
      </div>
    </div>
  );
}
