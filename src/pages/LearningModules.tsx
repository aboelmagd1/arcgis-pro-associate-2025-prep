import { useState, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import {
  BookOpen,
  CheckSquare,
  Layers,
  ExternalLink,
  Play,
  ChevronDown,
  ChevronUp,
  Sparkles,
  Filter,
  HelpCircle,
  Eye,
  EyeOff,
  CheckCircle2,
} from 'lucide-react';
import { useI18n } from '../i18n';
import { loadModules } from '../services/content';
import type { LearningModule, UiPathItem } from '../types/content';

export default function LearningModules() {
  const { lang } = useI18n();
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const domainQuery = searchParams.get('domain');

  const [modules, setModules] = useState<LearningModule[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedDomain, setSelectedDomain] = useState<string>(domainQuery ?? 'all');
  const [expandedId, setExpandedId] = useState<string | null>('M1');
  const [revealedFlashcards, setRevealedFlashcards] = useState<Record<string, boolean>>({});
  const [completedLabs, setCompletedLabs] = useState<Record<string, boolean>>(() => {
    try {
      return JSON.parse(localStorage.getItem('eapa.completedLabs') ?? '{}');
    } catch {
      return {};
    }
  });

  const domainMap: Record<string, string> = {
    data: 'Data Management',
    viz: 'Visualization',
    analysis: 'Analysis and Geoprocessing',
    sharing: 'Layouts and Sharing',
  };

  useEffect(() => {
    loadModules()
      .then((data) => {
        setModules(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (domainQuery) {
      setSelectedDomain(domainQuery);
    }
  }, [domainQuery]);

  useEffect(() => {
    if (modules.length > 0 && selectedDomain !== 'all') {
      const match = modules.find(
        (m) => m.domain === selectedDomain || domainMap[m.domain] === selectedDomain
      );
      if (match) {
        setExpandedId(match.id);
      }
    }
  }, [selectedDomain, modules]);

  const handleDomainFilter = (domainKey: string) => {
    setSelectedDomain(domainKey);
    if (domainKey === 'all') {
      setSearchParams({});
    } else {
      setSearchParams({ domain: domainKey });
    }
  };

  const toggleLabTask = (modId: string, taskIdx: number) => {
    const key = `${modId}_${taskIdx}`;
    const next = { ...completedLabs, [key]: !completedLabs[key] };
    setCompletedLabs(next);
    try {
      localStorage.setItem('eapa.completedLabs', JSON.stringify(next));
    } catch {
      // storage unavailable
    }
  };

  const toggleFlashcardAnswer = (cardKey: string) => {
    setRevealedFlashcards((prev) => ({
      ...prev,
      [cardKey]: !prev[cardKey],
    }));
  };

  const filteredModules =
    selectedDomain === 'all'
      ? modules
      : modules.filter((m) => m.domain === selectedDomain || domainMap[m.domain] === selectedDomain);

  const startModuleQuiz = (domain: string) => {
    const fullDomain = domainMap[domain] ?? domain;
    navigate(`/exam?preset=domain&domain=${encodeURIComponent(fullDomain)}`);
  };

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="flex items-center gap-3 text-slate-500">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-sky-500 border-t-transparent" />
          <p className="text-sm font-medium">
            {lang === 'ar' ? 'جارٍ تحميل المناهج والموديولات التعليمية...' : 'Loading learning modules...'}
          </p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-rose-300 bg-rose-50 p-6 text-rose-800 dark:border-rose-900 dark:bg-rose-950/40 dark:text-rose-200">
        <p className="font-bold">
          {lang === 'ar' ? 'فشل تحميل الوحدات التعليمية' : 'Failed to load modules'}: {error}
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div className="space-y-2 max-w-3xl">
            <div className="inline-flex items-center gap-1.5 rounded-full bg-sky-500/20 px-3 py-1 text-xs font-semibold text-sky-300">
              <Sparkles size={14} />{' '}
              {lang === 'ar' ? 'المنهج الشامل المعتمد 2025' : 'Official 2025 Comprehensive Curriculum'}
            </div>
            <h1 className="text-2xl font-black sm:text-3xl">
              {lang === 'ar' ? 'خطة الدراسة والوحدات التعليمية (12 موديول)' : '12-Module Certification Curriculum'}
            </h1>
            <p className="text-xs text-slate-300 sm:text-sm leading-relaxed">
              {lang === 'ar'
                ? 'تغطية شاملة وثنائية اللغة لكافة محاور ونطاقات شهادة ArcGIS Pro Associate 2025، مدعومة بمسارات الواجهة وجداول المقارنة وقوائم الفحص العملي.'
                : 'Complete bilingual syllabus covering all EAPA_2025 exam domains with official UI paths, comparative matrices, and interactive hands-on lab checklists.'}
            </p>
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => navigate('/exam?preset=eapa75')}
              className="flex items-center gap-2 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 px-4 py-2.5 text-xs font-bold text-slate-950 shadow-md hover:from-amber-400 hover:to-amber-500 transition-all"
            >
              <Play size={16} /> {lang === 'ar' ? 'محاكاة اختبار كامل (75Q)' : 'Launch 75Q Mock Exam'}
            </button>
          </div>
        </div>

        {/* Domain Filter Pills */}
        <div className="mt-6 flex flex-wrap gap-2 pt-4 border-t border-slate-700/60">
          <button
            onClick={() => handleDomainFilter('all')}
            className={`rounded-lg px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 ${
              selectedDomain === 'all'
                ? 'bg-sky-500 text-slate-950 shadow-sm'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <Filter size={13} /> {lang === 'ar' ? 'كافة الوحدات (12)' : 'All Modules (12)'}
          </button>
          <button
            onClick={() => handleDomainFilter('data')}
            className={`rounded-lg px-3 py-1.5 text-xs font-bold transition ${
              selectedDomain === 'data' || selectedDomain === 'Data Management'
                ? 'bg-sky-500 text-slate-950 shadow-sm'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            {lang === 'ar' ? 'إدارة البيانات (32%)' : 'Data Management (32%)'}
          </button>
          <button
            onClick={() => handleDomainFilter('viz')}
            className={`rounded-lg px-3 py-1.5 text-xs font-bold transition ${
              selectedDomain === 'viz' || selectedDomain === 'Visualization'
                ? 'bg-sky-500 text-slate-950 shadow-sm'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            {lang === 'ar' ? 'العرض البصري (25%)' : 'Visualization (25%)'}
          </button>
          <button
            onClick={() => handleDomainFilter('analysis')}
            className={`rounded-lg px-3 py-1.5 text-xs font-bold transition ${
              selectedDomain === 'analysis' || selectedDomain === 'Analysis and Geoprocessing'
                ? 'bg-sky-500 text-slate-950 shadow-sm'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            {lang === 'ar' ? 'التحليل والمعالجة (25%)' : 'Analysis & GP (25%)'}
          </button>
          <button
            onClick={() => handleDomainFilter('sharing')}
            className={`rounded-lg px-3 py-1.5 text-xs font-bold transition ${
              selectedDomain === 'sharing' || selectedDomain === 'Layouts and Sharing'
                ? 'bg-sky-500 text-slate-950 shadow-sm'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            {lang === 'ar' ? 'اللوحات والمشاركة (18%)' : 'Layouts & Sharing (18%)'}
          </button>
        </div>
      </div>

      {/* Modules Accordion / Cards List */}
      <div className="space-y-4">
        {filteredModules.map((mod) => {
          const isExpanded = expandedId === mod.id;
          const labCount = mod.lab_checklist ? mod.lab_checklist.length : 0;
          const labDoneCount = mod.lab_checklist
            ? mod.lab_checklist.filter((_, idx) => !!completedLabs[`${mod.id}_${idx}`]).length
            : 0;

          return (
            <div
              key={mod.id}
              className="rounded-2xl border border-slate-200 bg-white shadow-sm transition dark:border-slate-800 dark:bg-slate-900 overflow-hidden"
            >
              {/* Header Bar */}
              <div
                onClick={() => setExpandedId(isExpanded ? null : mod.id)}
                className="flex cursor-pointer flex-wrap items-center justify-between gap-3 p-5 hover:bg-slate-50 dark:hover:bg-slate-800/50 transition"
              >
                <div className="flex items-center gap-3">
                  <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-sky-500/10 font-mono text-sm font-black text-sky-600 dark:bg-sky-950/60 dark:text-sky-400">
                    {mod.id}
                  </span>
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <span className="rounded bg-slate-100 px-2 py-0.5 text-[10px] font-bold text-slate-600 dark:bg-slate-800 dark:text-slate-300">
                        {lang === 'ar' ? `الأسبوع ${mod.week}` : `Week ${mod.week}`}
                      </span>
                      <span className="text-xs font-semibold text-sky-600 dark:text-sky-400">
                        {lang === 'ar' ? mod.domainTitle_ar : mod.domainTitle_en}
                      </span>
                      {labCount > 0 && (
                        <span className="text-[10px] text-slate-400 font-mono hidden sm:inline">
                          ({labDoneCount}/{labCount} {lang === 'ar' ? 'تمرين مكتمل' : 'labs done'})
                        </span>
                      )}
                    </div>
                    <h2 className="text-base font-bold text-slate-900 dark:text-white sm:text-lg">
                      {lang === 'ar' ? mod.title_ar : mod.title_en}
                    </h2>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      startModuleQuiz(mod.domain);
                    }}
                    className="flex items-center gap-1.5 rounded-lg bg-teal-600 px-3 py-1.5 text-xs font-bold text-white shadow-sm hover:bg-teal-500 transition"
                    title={lang === 'ar' ? 'بدء اختبار أسئلة هذا المجال' : 'Practice questions for this domain'}
                  >
                    <Play size={13} /> {lang === 'ar' ? 'اختبار الوحدة' : 'Quiz'}
                  </button>
                  <span className="text-slate-400 p-1">
                    {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                  </span>
                </div>
              </div>

              {/* Collapsible Content */}
              {isExpanded && (
                <div className="border-t border-slate-200 p-5 md:p-6 space-y-6 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/40">
                  {/* Summary */}
                  <div>
                    <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 flex items-center gap-1.5">
                      <BookOpen size={14} /> {lang === 'ar' ? 'ملخص النظرية والمفاهيم' : 'Theory & Architectural Summary'}
                    </h3>
                    <p className="text-sm leading-relaxed text-slate-700 dark:text-slate-300 bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 shadow-sm">
                      {lang === 'ar' ? mod.summary_ar : mod.summary_en}
                    </p>
                  </div>

                  {/* UI Navigation Paths */}
                  {mod.ui_paths && mod.ui_paths.length > 0 && (
                    <div className="space-y-2">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center gap-1.5">
                        <Layers size={14} /> {lang === 'ar' ? 'مسارات الواجهة في ArcGIS Pro' : 'ArcGIS Pro UI Navigation Paths'}
                      </h3>
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        {mod.ui_paths.map((item, idx) => {
                          const isObj = typeof item === 'object' && item !== null;
                          const obj = isObj ? (item as UiPathItem) : null;
                          const label = obj ? (lang === 'ar' ? obj.label_ar : obj.label_en) : '';
                          const pathStr = obj ? obj.path : String(item);

                          return (
                            <div
                              key={idx}
                              className="rounded-xl border border-slate-200 bg-white p-3 shadow-sm dark:border-slate-800 dark:bg-slate-900 flex flex-col justify-between gap-2"
                            >
                              {label && (
                                <div className="text-xs font-bold text-slate-900 dark:text-slate-100 flex items-center gap-1.5">
                                  <span className="h-2 w-2 rounded-full bg-sky-500 shrink-0"></span>
                                  <span>{label}</span>
                                </div>
                              )}
                              <div className="rounded-lg bg-slate-50 dark:bg-slate-950/80 p-2 font-mono text-[11px] text-sky-700 dark:text-sky-300 border border-slate-100 dark:border-slate-800 break-words">
                                {pathStr}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  {/* Key Concepts List */}
                  <div>
                    <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">
                      {lang === 'ar' ? 'المفاهيم الأساسية المستهدفة في الاختبار' : 'Key Tested Concepts'}
                    </h3>
                    <ul className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                      {(lang === 'ar' ? mod.key_concepts_ar : mod.key_concepts_en).map((c, idx) => (
                        <li
                          key={idx}
                          className="flex items-start gap-2.5 rounded-xl border border-slate-200 bg-white p-3 text-xs text-slate-800 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-200 shadow-sm leading-relaxed"
                        >
                          <span className="text-sky-500 font-bold shrink-0 mt-0.5">•</span>
                          <span>{c}</span>
                        </li>
                      ))}
                    </ul>
                  </div>

                  {/* Comparison Matrix Table */}
                  {mod.comparison_table && (
                    <div className="space-y-2">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                        {lang === 'ar' ? mod.comparison_table.title_ar : mod.comparison_table.title_en}
                      </h3>
                      <div className="overflow-x-auto rounded-xl border border-slate-200 shadow-sm dark:border-slate-800">
                        <table className="w-full text-left text-xs">
                          <thead className="bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-bold">
                            <tr>
                              {(lang === 'ar'
                                ? mod.comparison_table.headers_ar
                                : mod.comparison_table.headers_en
                              ).map((h, i) => (
                                <th
                                  key={i}
                                  className="p-3 border-b border-slate-200 dark:border-slate-700 whitespace-nowrap"
                                >
                                  {h}
                                </th>
                              ))}
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-200 dark:divide-slate-800 bg-white dark:bg-slate-900">
                            {(lang === 'ar'
                              ? mod.comparison_table.rows_ar
                              : mod.comparison_table.rows_en
                            ).map((row, rIdx) => (
                              <tr key={rIdx} className="hover:bg-slate-50 dark:hover:bg-slate-800/40">
                                {row.map((cell, cIdx) => (
                                  <td
                                    key={cIdx}
                                    className="p-3 text-slate-700 dark:text-slate-300 leading-relaxed min-w-[150px]"
                                  >
                                    {cell}
                                  </td>
                                ))}
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}

                  {/* Hands-On Lab Checklist */}
                  {mod.lab_checklist && mod.lab_checklist.length > 0 && (
                    <div className="space-y-3 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                      <div className="flex items-center justify-between">
                        <h3 className="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400 flex items-center gap-1.5">
                          <CheckSquare size={15} />{' '}
                          {lang === 'ar'
                            ? 'قائمة الفحص العملي للمهارات (Hands-On Lab Checklist)'
                            : 'Hands-On Practical Lab Checklist'}
                        </h3>
                        <span className="text-xs font-mono font-bold text-slate-500">
                          {labDoneCount} / {labCount} {lang === 'ar' ? 'مكتمل' : 'Completed'}
                        </span>
                      </div>
                      <div className="space-y-2">
                        {mod.lab_checklist.map((lab, lIdx) => {
                          const key = `${mod.id}_${lIdx}`;
                          const isDone = !!completedLabs[key];
                          return (
                            <label
                              key={lIdx}
                              className={`flex items-start gap-3 rounded-xl p-2.5 text-xs cursor-pointer transition border ${
                                isDone
                                  ? 'bg-emerald-50/70 border-emerald-200 text-emerald-950 dark:bg-emerald-950/20 dark:border-emerald-900 dark:text-emerald-300 line-through'
                                  : 'border-slate-100 hover:bg-slate-50 dark:border-slate-800 dark:hover:bg-slate-800/60 text-slate-800 dark:text-slate-200'
                              }`}
                            >
                              <input
                                type="checkbox"
                                checked={isDone}
                                onChange={() => toggleLabTask(mod.id, lIdx)}
                                className="mt-0.5 h-4 w-4 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500 cursor-pointer"
                              />
                              <span className="flex-1 leading-relaxed">
                                {lang === 'ar' ? lab.task_ar : lab.task_en}
                              </span>
                            </label>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  {/* Module-Specific Targeted Flashcards */}
                  {mod.flashcards && mod.flashcards.length > 0 && (
                    <div className="space-y-3 rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-purple-600 dark:text-purple-400 flex items-center gap-1.5">
                        <HelpCircle size={15} />{' '}
                        {lang === 'ar'
                          ? 'أسئلة المراجعة السريعة للوحدة (Knowledge Check)'
                          : 'Module Rapid Knowledge Checks'}
                      </h3>
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                        {mod.flashcards.map((card, cIdx) => {
                          const cardKey = `${mod.id}_card_${cIdx}`;
                          const isRevealed = !!revealedFlashcards[cardKey];
                          const questionText = lang === 'ar' ? card.q_ar : card.q_en;
                          const answerText = lang === 'ar' ? card.a_ar : card.a_en;

                          return (
                            <div
                              key={cIdx}
                              className="rounded-xl border border-slate-200 bg-slate-50/60 p-4 dark:border-slate-800 dark:bg-slate-950/60 flex flex-col justify-between gap-3"
                            >
                              <div>
                                <span className="inline-block text-[10px] font-bold text-purple-600 dark:text-purple-400 mb-1">
                                  {lang === 'ar' ? `سؤال مراجعة ${cIdx + 1}` : `Recall Card ${cIdx + 1}`}
                                </span>
                                <p className="text-xs font-semibold text-slate-900 dark:text-slate-100 leading-relaxed">
                                  {questionText}
                                </p>
                              </div>

                              <div>
                                {isRevealed ? (
                                  <div className="rounded-lg bg-white p-3 text-xs text-slate-700 dark:bg-slate-900 dark:text-slate-300 border border-purple-200 dark:border-purple-900/60 leading-relaxed">
                                    <div className="flex items-center gap-1 text-[10px] font-bold text-emerald-600 dark:text-emerald-400 mb-1">
                                      <CheckCircle2 size={12} />
                                      <span>{lang === 'ar' ? 'الإجابة النموذجية:' : 'Answer Key:'}</span>
                                    </div>
                                    {answerText}
                                  </div>
                                ) : (
                                  <button
                                    onClick={() => toggleFlashcardAnswer(cardKey)}
                                    className="flex items-center gap-1.5 rounded-lg bg-purple-50 hover:bg-purple-100 dark:bg-purple-950/40 dark:hover:bg-purple-900/40 px-3 py-1.5 text-xs font-semibold text-purple-700 dark:text-purple-300 transition w-full justify-center border border-purple-200 dark:border-purple-800"
                                  >
                                    <Eye size={13} />
                                    <span>{lang === 'ar' ? 'كشف الإجابة النموذجية' : 'Reveal Answer'}</span>
                                  </button>
                                )}

                                {isRevealed && (
                                  <button
                                    onClick={() => toggleFlashcardAnswer(cardKey)}
                                    className="mt-2 flex items-center gap-1 text-[11px] text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
                                  >
                                    <EyeOff size={12} />
                                    <span>{lang === 'ar' ? 'إخفاء الإجابة' : 'Hide Answer'}</span>
                                  </button>
                                )}
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}

                  {/* Official Documentation Hub Links */}
                  {mod.doc_hubs && mod.doc_hubs.length > 0 && (
                    <div className="pt-2 flex flex-wrap gap-2">
                      {mod.doc_hubs.map((hub, hIdx) => (
                        <a
                          key={hIdx}
                          href={hub.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="inline-flex items-center gap-1.5 rounded-lg border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold text-slate-600 hover:text-sky-600 hover:border-sky-300 shadow-sm dark:border-slate-800 dark:bg-slate-900 dark:text-slate-400 dark:hover:text-sky-300 transition"
                        >
                          <ExternalLink size={12} /> {hub.title}
                        </a>
                      ))}
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
