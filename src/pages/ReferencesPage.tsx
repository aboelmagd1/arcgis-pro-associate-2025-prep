import { useState, useEffect } from 'react';
import { Search, ExternalLink, Scale, AlertOctagon, Calendar, Database, ShieldAlert, Code2, Wrench } from 'lucide-react';
import { useI18n } from '../i18n';
import {
  loadToolComparisons,
  loadTroubleshooting,
  loadDataManagementTools,
  loadStudyPlanner
} from '../services/content';
import type {
  ToolComparison,
  TroubleshootingGuide,
  DataManagementTool,
  StudyPlanner
} from '../types/content';

export default function ReferencesPage() {
  const { lang } = useI18n();
  const [activeTab, setActiveTab] = useState<'comparisons' | 'dmTools' | 'troubleshoot' | 'planner'>('comparisons');

  const [comparisons, setComparisons] = useState<ToolComparison[]>([]);
  const [troubleshooting, setTroubleshooting] = useState<TroubleshootingGuide[]>([]);
  const [dmTools, setDmTools] = useState<DataManagementTool[]>([]);
  const [planner, setPlanner] = useState<StudyPlanner | null>(null);
  const [loading, setLoading] = useState(true);
  const [toolSearch, setToolSearch] = useState('');

  useEffect(() => {
    Promise.all([
      loadToolComparisons(),
      loadTroubleshooting(),
      loadDataManagementTools(),
      loadStudyPlanner()
    ])
      .then(([comp, tb, dm, pl]) => {
        setComparisons(comp);
        setTroubleshooting(tb);
        setDmTools(dm);
        setPlanner(pl);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  const filteredDmTools = dmTools.filter(t => {
    if (!toolSearch.trim()) return true;
    const q = toolSearch.toLowerCase();
    return (
      t.name.toLowerCase().includes(q) ||
      t.name_ar.toLowerCase().includes(q) ||
      t.category.toLowerCase().includes(q) ||
      t.arcpy_syntax.toLowerCase().includes(q) ||
      (t.description?.en ?? '').toLowerCase().includes(q)
    );
  });

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <p className="text-slate-500 animate-pulse">{lang === 'ar' ? 'جاري تحميل المراجع والموسوعة...' : 'Loading reference hub...'}</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl">
        <div className="space-y-2">
          <span className="inline-block rounded-full bg-sky-500/20 px-3 py-1 text-xs font-semibold text-sky-300">
            {lang === 'ar' ? 'المكتبة المرجعية الشاملة للاختبار' : 'Master Reference & Troubleshooting Hub'}
          </span>
          <h1 className="text-2xl font-black sm:text-3xl">
            {lang === 'ar' ? 'الموسوعة الكارتوغرافية وجداول المقارنة السريعة' : 'Geospatial Encyclopedia & Decision Matrices'}
          </h1>
          <p className="max-w-2xl text-xs text-slate-300 sm:text-sm">
            {lang === 'ar'
              ? 'مقارنات دقيقة بين الأدوات المتشابهة، موسوعة أكثر 52 أداة في إدارة البيانات مع أكواد ArcPy، أدلة استكشاف الأخطاء، وخطة المذاكرة للأربعة أسابيع.'
              : 'Direct comparison pairs, Top 52 Data Management tools with ArcPy syntax and exam traps, GIS troubleshooting guides, and the 4-week study roadmap.'}
          </p>
        </div>

        {/* Tab Navigation */}
        <div className="mt-6 flex flex-wrap gap-2 pt-4 border-t border-slate-700/60">
          <button
            onClick={() => setActiveTab('comparisons')}
            className={`flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition ${
              activeTab === 'comparisons' ? 'bg-sky-500 text-slate-950 shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <Scale size={15} /> {lang === 'ar' ? 'مقارنة الأدوات (12 زوجاً)' : 'Tool Comparisons (12)'}
          </button>
          <button
            onClick={() => setActiveTab('dmTools')}
            className={`flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition ${
              activeTab === 'dmTools' ? 'bg-sky-500 text-slate-950 shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <Database size={15} /> {lang === 'ar' ? 'موسوعة أدوات البيانات (52 أداة)' : 'Top 52 Data Management Tools'}
          </button>
          <button
            onClick={() => setActiveTab('troubleshoot')}
            className={`flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition ${
              activeTab === 'troubleshoot' ? 'bg-sky-500 text-slate-950 shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <AlertOctagon size={15} /> {lang === 'ar' ? 'استكشاف الأخطاء (12 دليلاً)' : 'Troubleshooting (12)'}
          </button>
          <button
            onClick={() => setActiveTab('planner')}
            className={`flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition ${
              activeTab === 'planner' ? 'bg-sky-500 text-slate-950 shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <Calendar size={15} /> {lang === 'ar' ? 'خطة الأسابيع الأربعة' : '4-Week Study Planner'}
          </button>
        </div>
      </div>

      {/* TAB 1: TOOL COMPARISONS */}
      {activeTab === 'comparisons' && (
        <div className="space-y-4">
          <div className="text-xs text-slate-500 dark:text-slate-400">
            {lang === 'ar' ? 'المقارنات الحرجة لأكثر المفاهيم والأدوات تكراراً في أسئلة الامتحان:' : 'Critical concept pairs commonly tested on the EAPA_2025 examination:'}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {comparisons.map(tc => (
              <div
                key={tc.id}
                className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900 space-y-4 flex flex-col justify-between"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between gap-2 border-b border-slate-100 pb-2 dark:border-slate-800">
                    <span className="font-mono text-xs font-black text-sky-600 dark:text-sky-400 bg-sky-50 dark:bg-sky-950/40 px-2 py-0.5 rounded">
                      {tc.id}
                    </span>
                    <span className="rounded bg-slate-100 px-2 py-0.5 text-[10px] font-bold text-slate-600 dark:bg-slate-800 dark:text-slate-300">
                      {tc.domain}
                    </span>
                  </div>

                  <h3 className="text-base font-bold text-slate-900 dark:text-white">
                    {lang === 'ar' ? tc.title.ar : tc.title.en}
                  </h3>

                  {/* Tool A vs Tool B Cards */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                    <div className="rounded-xl border border-sky-200 bg-sky-50/50 p-2.5 dark:border-sky-900/40 dark:bg-sky-950/20">
                      <strong className="text-sky-700 dark:text-sky-300">{tc.toolA.name}</strong>
                      <div className="mt-1 font-mono text-[10px] text-slate-600 dark:text-slate-400 break-all">
                        {tc.toolA.syntax}
                      </div>
                      <p className="mt-1 text-slate-700 dark:text-slate-300 text-[11px] leading-relaxed">
                        {lang === 'ar' ? tc.useCaseA.ar : tc.useCaseA.en}
                      </p>
                    </div>

                    <div className="rounded-xl border border-amber-200 bg-amber-50/50 p-2.5 dark:border-amber-900/40 dark:bg-amber-950/20">
                      <strong className="text-amber-700 dark:text-amber-300">{tc.toolB.name}</strong>
                      <div className="mt-1 font-mono text-[10px] text-slate-600 dark:text-slate-400 break-all">
                        {tc.toolB.syntax}
                      </div>
                      <p className="mt-1 text-slate-700 dark:text-slate-300 text-[11px] leading-relaxed">
                        {lang === 'ar' ? tc.useCaseB.ar : tc.useCaseB.en}
                      </p>
                    </div>
                  </div>

                  {/* Key Difference */}
                  <div className="text-xs leading-relaxed text-slate-700 dark:text-slate-300 pt-1">
                    <strong className="text-slate-900 dark:text-white">
                      {lang === 'ar' ? 'الفرق الجوهري:' : 'Decisive Difference:'}
                    </strong>{' '}
                    {lang === 'ar' ? tc.keyDifference.ar : tc.keyDifference.en}
                  </div>
                </div>

                {/* Exam Trap */}
                {tc.examTrap && (
                  <div className="rounded-xl border border-rose-200 bg-rose-50/50 p-2.5 text-xs text-rose-800 dark:border-rose-900/40 dark:bg-rose-950/20 dark:text-rose-200 flex items-start gap-1.5">
                    <ShieldAlert size={15} className="shrink-0 mt-0.5 text-rose-500" />
                    <span>
                      <strong>{lang === 'ar' ? 'فخ الاختبار:' : 'Exam Trap:'}</strong>{' '}
                      {lang === 'ar' ? tc.examTrap.ar : tc.examTrap.en}
                    </span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 2: TOP 52 DATA MANAGEMENT TOOLS */}
      {activeTab === 'dmTools' && (
        <div className="space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div className="text-xs text-slate-500 dark:text-slate-400">
              {lang === 'ar'
                ? `موسوعة أهم 52 أداة في نطاق إدارة البيانات (32% من وزن الاختبار) مدعومة بأكواد ArcPy وفخاخ الاختبار:`
                : `Top 52 essential tools in Domain 1 (Data Management - 32% weight) with ArcPy syntax and traps:`}
            </div>
            <div className="relative w-full sm:w-64">
              <Search size={14} className="absolute left-3 top-2.5 text-slate-400" />
              <input
                type="text"
                value={toolSearch}
                onChange={e => setToolSearch(e.target.value)}
                placeholder={lang === 'ar' ? 'ابحث عن أداة أو دالة بايثون...' : 'Search tools or ArcPy...'}
                className="w-full rounded-xl border border-slate-300 bg-white py-1.5 pl-8 pr-3 text-xs text-slate-900 placeholder-slate-400 focus:border-sky-500 focus:outline-none dark:border-slate-700 dark:bg-slate-900 dark:text-white"
              />
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredDmTools.map(tool => (
              <div
                key={tool.id}
                className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900 space-y-3 flex flex-col justify-between"
              >
                <div className="space-y-2">
                  <div className="flex items-start justify-between gap-2 border-b border-slate-100 pb-2 dark:border-slate-800">
                    <div>
                      <span className="font-mono text-[10px] font-bold text-sky-600 dark:text-sky-400 bg-sky-50 dark:bg-sky-950/40 px-2 py-0.5 rounded">
                        {tool.category}
                      </span>
                      <h4 className="text-base font-bold text-slate-900 dark:text-white mt-1">
                        {tool.name}
                      </h4>
                      {tool.name_ar && (
                        <span className="text-xs font-semibold text-sky-600 dark:text-sky-400">
                          {tool.name_ar}
                        </span>
                      )}
                    </div>
                    {tool.doc_url && (
                      <a
                        href={tool.doc_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="rounded-lg p-1.5 text-slate-400 hover:text-sky-500 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                        title="Official Documentation"
                      >
                        <ExternalLink size={15} />
                      </a>
                    )}
                  </div>

                  {/* ArcPy Syntax */}
                  {tool.arcpy_syntax && (
                    <div className="rounded-lg border border-slate-200 bg-slate-50 p-2 font-mono text-[11px] text-sky-700 dark:border-slate-800 dark:bg-slate-950 dark:text-sky-300 overflow-x-auto">
                      <code>{tool.arcpy_syntax}</code>
                    </div>
                  )}

                  {/* UI Path */}
                  {tool.ui_path && (
                    <div className="text-[11px] font-mono text-slate-500 dark:text-slate-400">
                      <strong>UI Path:</strong> {tool.ui_path}
                    </div>
                  )}

                  {/* Description */}
                  <p className="text-xs leading-relaxed text-slate-700 dark:text-slate-300">
                    {lang === 'ar' ? tool.description.ar : tool.description.en}
                  </p>
                </div>

                {/* Exam Trap */}
                {tool.exam_trap && (tool.exam_trap.en || tool.exam_trap.ar) && (
                  <div className="rounded-xl border border-amber-200 bg-amber-50/50 p-2.5 text-xs text-amber-900 dark:border-amber-900/40 dark:bg-amber-950/20 dark:text-amber-200">
                    <strong className="text-amber-700 dark:text-amber-400">
                      {lang === 'ar' ? 'فخ الاختبار:' : 'Exam Trap:'}
                    </strong>{' '}
                    {lang === 'ar' ? tool.exam_trap.ar : tool.exam_trap.en}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: TROUBLESHOOTING GUIDES */}
      {activeTab === 'troubleshoot' && (
        <div className="space-y-4">
          <div className="text-xs text-slate-500 dark:text-slate-400">
            {lang === 'ar' ? 'أدلة تشخيص واستكشاف أشهر أخطاء ومشاكل ArcGIS Pro:' : 'Diagnostic workflows for common errors and operational failures in ArcGIS Pro:'}
          </div>

          <div className="space-y-4">
            {troubleshooting.map(tb => (
              <div
                key={tb.id}
                className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900 space-y-3"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-2 dark:border-slate-800">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-xs font-black text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/40 px-2 py-0.5 rounded">
                      {tb.id}
                    </span>
                    <h3 className="text-base font-bold text-slate-900 dark:text-white">
                      {lang === 'ar' ? tb.title.ar : tb.title.en}
                    </h3>
                  </div>
                  <span className="rounded bg-slate-100 px-2 py-0.5 text-[10px] font-bold text-slate-600 dark:bg-slate-800 dark:text-slate-300">
                    {tb.domain}
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                  <div className="rounded-xl border border-rose-200 bg-rose-50/40 p-3 dark:border-rose-900/40 dark:bg-rose-950/20 space-y-1">
                    <strong className="text-rose-700 dark:text-rose-400">
                      {lang === 'ar' ? 'العَرَض الملاحظ (Symptom):' : 'Observed Symptom:'}
                    </strong>
                    <p className="text-slate-700 dark:text-slate-300 leading-relaxed">
                      {lang === 'ar' ? tb.symptom.ar : tb.symptom.en}
                    </p>
                  </div>

                  <div className="rounded-xl border border-amber-200 bg-amber-50/40 p-3 dark:border-amber-900/40 dark:bg-amber-950/20 space-y-1">
                    <strong className="text-amber-700 dark:text-amber-400">
                      {lang === 'ar' ? 'السبب الجذري للمشكلة (Root Cause):' : 'Root Cause:'}
                    </strong>
                    <p className="text-slate-700 dark:text-slate-300 leading-relaxed">
                      {lang === 'ar' ? tb.rootCause.ar : tb.rootCause.en}
                    </p>
                  </div>
                </div>

                {/* Resolution Steps */}
                <div className="space-y-1.5 pt-1">
                  <strong className="text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400">
                    {lang === 'ar' ? 'خطوات الحل خطوة بخطوة:' : 'Step-by-Step Resolution:'}
                  </strong>
                  <div className="space-y-1.5">
                    {tb.resolutionSteps.map(st => (
                      <div
                        key={st.step}
                        className="flex items-start gap-2.5 rounded-lg border border-slate-100 bg-slate-50 p-2 text-xs text-slate-800 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-200"
                      >
                        <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-sky-500/10 font-mono text-[10px] font-bold text-sky-600 dark:text-sky-400">
                          {st.step}
                        </span>
                        <span className="leading-relaxed">{lang === 'ar' ? st.text.ar : st.text.en}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Prevention Tip */}
                <div className="rounded-xl border border-emerald-200 bg-emerald-50/40 p-2.5 text-xs text-emerald-900 dark:border-emerald-900/40 dark:bg-emerald-950/20 dark:text-emerald-300">
                  <strong>{lang === 'ar' ? 'نصيحة وقائية:' : 'Prevention Tip:'}</strong>{' '}
                  {lang === 'ar' ? tb.preventionTip.ar : tb.preventionTip.en}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 4: 4-WEEK STUDY PLANNER */}
      {activeTab === 'planner' && planner && (
        <div className="space-y-6">
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900 space-y-3">
            <h3 className="text-lg font-bold text-slate-900 dark:text-white">
              {lang === 'ar' ? planner.title.ar : planner.title.en}
            </h3>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-3 text-center dark:border-slate-800 dark:bg-slate-950">
                <span className="text-slate-400">Exam Code</span>
                <div className="font-mono text-base font-bold text-sky-600 dark:text-sky-400">{planner.examOverview.code}</div>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-3 text-center dark:border-slate-800 dark:bg-slate-950">
                <span className="text-slate-400">Questions</span>
                <div className="font-mono text-base font-bold text-sky-600 dark:text-sky-400">{planner.examOverview.questions} Qs</div>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-3 text-center dark:border-slate-800 dark:bg-slate-950">
                <span className="text-slate-400">Time Limit</span>
                <div className="font-mono text-base font-bold text-sky-600 dark:text-sky-400">{planner.examOverview.timeMinutes} Mins</div>
              </div>
              <div className="rounded-xl border border-slate-200 bg-slate-50 p-3 text-center dark:border-slate-800 dark:bg-slate-950">
                <span className="text-slate-400">Passing Score</span>
                <div className="font-mono text-base font-bold text-emerald-600 dark:text-emerald-400">{planner.examOverview.passingScore}</div>
              </div>
            </div>
          </div>

          <div className="space-y-4">
            {planner.weeks.map(wk => (
              <div
                key={wk.weekNumber}
                className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900 space-y-4"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3 dark:border-slate-800">
                  <div>
                    <span className="text-xs font-bold text-sky-600 dark:text-sky-400">
                      {wk.domain}
                    </span>
                    <h4 className="text-base font-bold text-slate-900 dark:text-white">
                      {lang === 'ar' ? wk.title.ar : wk.title.en}
                    </h4>
                  </div>
                  <div className="flex gap-1.5">
                    {wk.focusModules.map(m => (
                      <span key={m} className="rounded bg-sky-50 dark:bg-sky-950/40 text-sky-600 dark:text-sky-400 px-2 py-0.5 text-xs font-mono font-bold">
                        {m}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="space-y-2">
                  <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                    {lang === 'ar' ? 'الجدول اليومي المقترح:' : 'Daily Schedule:'}
                  </span>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                    {wk.dailyTasks.map(t => (
                      <div
                        key={t.day}
                        className="flex items-start gap-2.5 rounded-xl border border-slate-100 bg-slate-50 p-2.5 text-xs text-slate-800 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-200"
                      >
                        <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-md bg-teal-500/10 font-mono text-[10px] font-bold text-teal-600 dark:text-teal-400">
                          D{t.day}
                        </span>
                        <span className="leading-relaxed">{lang === 'ar' ? t.task.ar : t.task.en}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

