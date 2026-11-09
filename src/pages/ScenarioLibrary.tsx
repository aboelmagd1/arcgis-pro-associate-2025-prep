import { useState, useEffect } from 'react';
import { Search, Filter, Bookmark, ExternalLink, CheckCircle2, XCircle, Strikethrough, Eye, EyeOff } from 'lucide-react';
import { useI18n } from '../i18n';
import { loadAllScenarios } from '../services/content';
import { loadProgress, saveProgress } from '../storage/store';
import type { Question } from '../types/content';

export default function ScenarioLibrary() {
  const { lang } = useI18n();
  const [scenarios, setScenarios] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Filters
  const [search, setSearch] = useState('');
  const [domainFilter, setDomainFilter] = useState('all');
  const [diffFilter, setDiffFilter] = useState('all');

  // Interactive user state per scenario
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, 'A' | 'B' | 'C' | 'D'>>({});
  const [struckOptions, setStruckOptions] = useState<Record<string, Record<string, boolean>>>({});
  const [revealedRationales, setRevealedRationales] = useState<Record<string, boolean>>({});
  const [bookmarks, setBookmarks] = useState<string[]>(() => loadProgress().bookmarks);

  useEffect(() => {
    loadAllScenarios()
      .then(data => {
        setScenarios(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const toggleBookmark = (id: string) => {
    const prog = loadProgress();
    const has = prog.bookmarks.includes(id);
    prog.bookmarks = has ? prog.bookmarks.filter(b => b !== id) : [...prog.bookmarks, id];
    saveProgress(prog);
    setBookmarks(prog.bookmarks);
  };

  const toggleStrike = (scenarioId: string, optId: string) => {
    setStruckOptions(prev => {
      const cur = prev[scenarioId] ?? {};
      return {
        ...prev,
        [scenarioId]: { ...cur, [optId]: !cur[optId] }
      };
    });
  };

  const handleSelectOption = (scenarioId: string, optId: 'A' | 'B' | 'C' | 'D') => {
    setSelectedAnswers(prev => ({ ...prev, [scenarioId]: optId }));
    setRevealedRationales(prev => ({ ...prev, [scenarioId]: true }));
  };

  const filtered = scenarios.filter(sc => {
    if (domainFilter !== 'all' && sc.domain !== domainFilter) return false;
    if (diffFilter !== 'all' && sc.difficulty !== diffFilter) return false;
    if (search.trim()) {
      const q = search.toLowerCase();
      const matchText = (sc.question?.en ?? '') + (sc.question?.ar ?? '') + (sc.context?.en ?? '') + (sc.tools.join(' '));
      if (!matchText.toLowerCase().includes(q)) return false;
    }
    return true;
  });

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <p className="text-slate-500 animate-pulse">{lang === 'ar' ? 'جاري تحميل مكتبة السيناريوهات التطبيقية (150 سيناريو)...' : 'Loading 150 scenario challenges...'}</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-rose-300 bg-rose-50 p-6 text-rose-800 dark:border-rose-900 dark:bg-rose-950/40 dark:text-rose-200">
        <p className="font-bold">{lang === 'ar' ? 'فشل تحميل السيناريوهات' : 'Failed to load scenarios'}: {error}</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-amber-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl">
        <div className="space-y-2">
          <span className="inline-block rounded-full bg-amber-500/20 px-3 py-1 text-xs font-semibold text-amber-300">
            {lang === 'ar' ? 'بنك السيناريوهات المعقدة (150 سيناريو موثق)' : 'Comprehensive Scenario Bank (150 Scenarios)'}
          </span>
          <h1 className="text-2xl font-black sm:text-3xl">
            {lang === 'ar' ? 'مكتبة سيناريوهات الاختبار التطبيقية' : 'Applied Scenario Practice Library'}
          </h1>
          <p className="max-w-2xl text-xs text-slate-300 sm:text-sm">
            {lang === 'ar'
              ? 'مجموعة مكثفة من المسائل العملية ومحاكاة بيئة العمل الواقعية في ArcGIS Pro، مع شطب الخيارات والتفسيرات التفصيلية لكل مشتت.'
              : 'Real-world workplace GIS dilemmas testing workflow decisions, tool parameters, and error resolution with option elimination and full distractor rationales.'}
          </p>
        </div>

        {/* Search & Filters */}
        <div className="mt-6 grid grid-cols-1 gap-3 sm:grid-cols-3 pt-4 border-t border-slate-700/60">
          <div className="relative">
            <Search size={15} className="absolute left-3 top-2.5 text-slate-400" />
            <input
              type="text"
              value={search}
              onChange={e => setSearch(e.target.value)}
              placeholder={lang === 'ar' ? 'ابحث في السيناريو أو الأداة...' : 'Search scenarios or tools...'}
              className="w-full rounded-xl border border-slate-700 bg-slate-950/60 py-2 pl-9 pr-3 text-xs text-white placeholder-slate-400 focus:border-amber-500 focus:outline-none"
            />
          </div>

          <div className="flex items-center gap-2">
            <Filter size={15} className="text-slate-400 shrink-0" />
            <select
              value={domainFilter}
              onChange={e => setDomainFilter(e.target.value)}
              aria-label="Domain Filter"
              className="w-full rounded-xl border border-slate-700 bg-slate-950/60 p-2 text-xs text-white focus:border-amber-500 focus:outline-none"
            >
              <option value="all">{lang === 'ar' ? 'كافة النطاقات (4)' : 'All Domains (4)'}</option>
              <option value="Data Management">{lang === 'ar' ? 'إدارة البيانات (48)' : 'Data Management (48)'}</option>
              <option value="Visualization">{lang === 'ar' ? 'العرض البصري (38)' : 'Visualization (38)'}</option>
              <option value="Analysis and Geoprocessing">{lang === 'ar' ? 'التحليل والمعالجة (37)' : 'Analysis & GP (37)'}</option>
              <option value="Layouts and Sharing">{lang === 'ar' ? 'اللوحات والمشاركة (27)' : 'Layouts & Sharing (27)'}</option>
            </select>
          </div>

          <select
            value={diffFilter}
            onChange={e => setDiffFilter(e.target.value)}
            aria-label="Difficulty Filter"
            className="w-full rounded-xl border border-slate-700 bg-slate-950/60 p-2 text-xs text-white focus:border-amber-500 focus:outline-none"
          >
            <option value="all">{lang === 'ar' ? 'كافة الصعوبات' : 'All Difficulties'}</option>
            <option value="Beginner">{lang === 'ar' ? 'مبتدئ (Beginner)' : 'Beginner'}</option>
            <option value="Intermediate">{lang === 'ar' ? 'متوسط (Intermediate)' : 'Intermediate'}</option>
            <option value="Advanced">{lang === 'ar' ? 'متقدم (Advanced)' : 'Advanced'}</option>
          </select>
        </div>

        <div className="mt-3 text-right text-xs text-slate-400">
          {lang === 'ar' ? `عرض ${filtered.length} من 150 سيناريو` : `Showing ${filtered.length} of 150 scenarios`}
        </div>
      </div>

      {/* Scenarios Grid */}
      <div className="space-y-6">
        {filtered.map(sc => {
          const selected = selectedAnswers[sc.id];
          const isBookmarked = bookmarks.includes(sc.id);
          const isRevealed = !!revealedRationales[sc.id];
          const strikes = struckOptions[sc.id] ?? {};

          return (
            <div
              key={sc.id}
              className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition dark:border-slate-800 dark:bg-slate-900/90 space-y-4"
            >
              {/* Badges & Actions */}
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3 dark:border-slate-800">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="font-mono text-xs font-black text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/40 px-2 py-0.5 rounded border border-amber-200 dark:border-amber-900/50">
                    {sc.id}
                  </span>
                  <span className="rounded bg-slate-100 px-2 py-0.5 text-[11px] font-bold text-slate-700 dark:bg-slate-800 dark:text-slate-300">
                    {sc.domain}
                  </span>
                  <span className="rounded bg-slate-100 px-2 py-0.5 text-[11px] text-slate-600 dark:bg-slate-800 dark:text-slate-400">
                    {sc.difficulty}
                  </span>
                  <span className="rounded bg-slate-100 px-2 py-0.5 text-[11px] text-slate-600 dark:bg-slate-800 dark:text-slate-400">
                    {sc.type}
                  </span>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={() => toggleBookmark(sc.id)}
                    className={`rounded-lg p-1.5 transition ${
                      isBookmarked ? 'bg-amber-500 text-slate-950' : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                    }`}
                    title={isBookmarked ? 'Remove bookmark' : 'Bookmark scenario'}
                  >
                    <Bookmark size={15} />
                  </button>
                  <button
                    onClick={() => setRevealedRationales(prev => ({ ...prev, [sc.id]: !prev[sc.id] }))}
                    className="flex items-center gap-1 rounded-lg border border-slate-200 px-2.5 py-1 text-xs text-slate-600 hover:bg-slate-100 dark:border-slate-800 dark:text-slate-400 dark:hover:bg-slate-800 transition"
                  >
                    {isRevealed ? <EyeOff size={13} /> : <Eye size={13} />}
                    <span>{isRevealed ? (lang === 'ar' ? 'إخفاء الشرح' : 'Hide') : (lang === 'ar' ? 'كشف الشرح' : 'Explain')}</span>
                  </button>
                </div>
              </div>

              {/* Tools Tags */}
              {sc.tools && sc.tools.length > 0 && (
                <div className="flex flex-wrap gap-1.5">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 self-center">
                    {lang === 'ar' ? 'الأدوات:' : 'Tools:'}
                  </span>
                  {sc.tools.map((t, idx) => (
                    <span
                      key={idx}
                      className="rounded-md bg-sky-50 dark:bg-sky-950/40 text-sky-700 dark:text-sky-300 border border-sky-200 dark:border-sky-900/40 px-2 py-0.5 font-mono text-[11px]"
                    >
                      {t}
                    </span>
                  ))}
                </div>
              )}

              {/* Scenario Context Card */}
              {sc.context && (
                <div className="rounded-xl border border-sky-200 bg-sky-50/60 p-4 dark:border-sky-900/40 dark:bg-sky-950/20 space-y-2">
                  <div className="text-[10px] font-bold uppercase tracking-wider text-sky-700 dark:text-sky-400">
                    {lang === 'ar' ? 'سياق السيناريو وبيئة العمل' : 'Workplace Scenario Context'}
                  </div>
                  <p className="text-xs sm:text-sm leading-relaxed text-slate-800 dark:text-slate-200 font-medium">
                    {lang === 'ar' ? sc.context.ar : sc.context.en}
                  </p>
                </div>
              )}

              {/* Question Text */}
              <div className="text-sm sm:text-base font-bold text-slate-900 dark:text-white">
                {lang === 'ar' ? sc.question.ar : sc.question.en}
              </div>

              {/* Options List */}
              <div className="space-y-2">
                {sc.options.map(opt => {
                  const isStruck = !!strikes[opt.id];
                  const isChosen = selected === opt.id;
                  const isCorrect = opt.id === sc.correctAnswer;
                  let borderStyle = 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700';
                  let bgStyle = 'bg-white dark:bg-slate-900';

                  if (selected) {
                    if (isCorrect) {
                      borderStyle = 'border-emerald-500 dark:border-emerald-500';
                      bgStyle = 'bg-emerald-50/70 dark:bg-emerald-950/30';
                    } else if (isChosen) {
                      borderStyle = 'border-rose-500 dark:border-rose-500';
                      bgStyle = 'bg-rose-50/70 dark:bg-rose-950/30';
                    }
                  }

                  return (
                    <div
                      key={opt.id}
                      onClick={() => handleSelectOption(sc.id, opt.id)}
                      className={`flex items-start justify-between gap-3 rounded-xl border p-3.5 cursor-pointer transition ${borderStyle} ${bgStyle} ${
                        isStruck ? 'opacity-40' : ''
                      }`}
                    >
                      <div className="flex items-start gap-3">
                        <span
                          className={`flex h-6 w-6 shrink-0 items-center justify-center rounded-lg font-mono text-xs font-bold ${
                            isChosen
                              ? isCorrect
                                ? 'bg-emerald-500 text-slate-950'
                                : 'bg-rose-500 text-white'
                              : 'bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300'
                          }`}
                        >
                          {opt.id}
                        </span>
                        <span className={`text-xs sm:text-sm leading-relaxed ${isStruck ? 'line-through text-slate-400' : 'text-slate-800 dark:text-slate-200'}`}>
                          {lang === 'ar' ? opt.text.ar : opt.text.en}
                        </span>
                      </div>

                      <div className="flex items-center gap-1.5 shrink-0" onClick={e => e.stopPropagation()}>
                        <button
                          onClick={() => toggleStrike(sc.id, opt.id)}
                          className={`rounded p-1 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 ${
                            isStruck ? 'text-amber-500 bg-amber-50 dark:bg-amber-950/40' : ''
                          }`}
                          title="Eliminate / Strikethrough option"
                        >
                          <Strikethrough size={14} />
                        </button>
                        {selected && isCorrect && <CheckCircle2 size={16} className="text-emerald-500" />}
                        {selected && isChosen && !isCorrect && <XCircle size={16} className="text-rose-500" />}
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Rationale & Explanation Card */}
              {isRevealed && (
                <div className="mt-4 rounded-xl border border-emerald-500/30 bg-emerald-50/50 p-4 dark:border-emerald-900/40 dark:bg-emerald-950/20 space-y-3">
                  <div>
                    <span className="text-xs font-bold uppercase tracking-wider text-emerald-700 dark:text-emerald-400">
                      {lang === 'ar' ? 'التفسير العلمي المعتمد والإجابة الصحيحة:' : 'Official Rationale & Correct Answer:'}
                    </span>
                    <p className="mt-1 text-xs sm:text-sm leading-relaxed text-slate-800 dark:text-slate-200">
                      {lang === 'ar' ? sc.explanation.ar : sc.explanation.en}
                    </p>
                  </div>

                  {/* Distractors breakdown */}
                  {sc.incorrectOptionsExplanation && (
                    <div className="border-t border-emerald-200/60 pt-3 dark:border-emerald-900/40 space-y-1.5">
                      <span className="text-[11px] font-bold text-slate-500 dark:text-slate-400">
                        {lang === 'ar' ? 'لماذا الخيارات الأخرى غير صحيحة؟' : 'Why other options are incorrect:'}
                      </span>
                      {Object.entries(sc.incorrectOptionsExplanation[lang] ?? {}).map(([optKey, text]) => (
                        <div key={optKey} className="text-xs text-slate-600 dark:text-slate-400 flex items-start gap-1.5">
                          <span className="font-mono font-bold text-rose-500 shrink-0">{optKey}:</span>
                          <span>{text}</span>
                        </div>
                      ))}
                    </div>
                  )}

                  {/* Reference */}
                  {sc.references && sc.references.length > 0 && (
                    <div className="pt-2">
                      <a
                        href={sc.references[0].url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1 text-[11px] font-semibold text-sky-600 hover:underline dark:text-sky-400"
                      >
                        <ExternalLink size={12} /> {sc.references[0].title}
                      </a>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

