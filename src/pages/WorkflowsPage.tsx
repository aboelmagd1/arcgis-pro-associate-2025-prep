import { useState, useEffect } from 'react';
import { Search, Filter, CheckCircle2, ChevronDown, ChevronUp, ExternalLink, Wrench, AlertTriangle, ShieldCheck, HelpCircle } from 'lucide-react';
import { useI18n } from '../i18n';
import { loadWorkflows } from '../services/content';
import type { Workflow } from '../types/content';

export default function WorkflowsPage() {
  const { lang } = useI18n();
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Filters
  const [search, setSearch] = useState('');
  const [domainFilter, setDomainFilter] = useState('all');
  const [expandedId, setExpandedId] = useState<string | null>('WF-001');

  // Interactive step completion tracking in localStorage
  const [completedSteps, setCompletedSteps] = useState<Record<string, boolean>>(() => {
    try {
      return JSON.parse(localStorage.getItem('eapa.completedWorkflowSteps') ?? '{}');
    } catch {
      return {};
    }
  });

  useEffect(() => {
    loadWorkflows()
      .then(data => {
        setWorkflows(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const toggleStep = (wfId: string, stepNum: number) => {
    const key = `${wfId}_${stepNum}`;
    const next = { ...completedSteps, [key]: !completedSteps[key] };
    setCompletedSteps(next);
    try {
      localStorage.setItem('eapa.completedWorkflowSteps', JSON.stringify(next));
    } catch {
      // storage unavailable
    }
  };

  const filtered = workflows.filter(wf => {
    if (domainFilter !== 'all' && wf.domain !== domainFilter) return false;
    if (search.trim()) {
      const q = search.toLowerCase();
      const match = (wf.title?.en ?? '') + (wf.title?.ar ?? '') + (wf.objective?.en ?? '') + (wf.tools.join(' '));
      if (!match.toLowerCase().includes(q)) return false;
    }
    return true;
  });

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <p className="text-slate-500 animate-pulse">{lang === 'ar' ? 'جاري تحميل مسارات العمل التطبيقية (30 مساراً)...' : 'Loading 30 GIS workflows...'}</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-xl border border-rose-300 bg-rose-50 p-6 text-rose-800 dark:border-rose-900 dark:bg-rose-950/40 dark:text-rose-200">
        <p className="font-bold">{lang === 'ar' ? 'فشل تحميل مسارات العمل' : 'Failed to load workflows'}: {error}</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-teal-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl">
        <div className="space-y-2">
          <span className="inline-block rounded-full bg-teal-500/20 px-3 py-1 text-xs font-semibold text-teal-300">
            {lang === 'ar' ? 'دليل مسارات العمل التطبيقية (30 تحدياً عملياً)' : 'Applied GIS Workflow Guides (30 Walkthroughs)'}
          </span>
          <h1 className="text-2xl font-black sm:text-3xl">
            {lang === 'ar' ? 'التحديات ومسارات العمل الميدانية في ArcGIS Pro' : 'Practical ArcGIS Pro Workflow Walkthroughs'}
          </h1>
          <p className="max-w-2xl text-xs text-slate-300 sm:text-sm">
            {lang === 'ar'
              ? 'إرشادات تفصيلية خطوة بخطوة لكل عملية جغرافية، متضمنة مسارات الواجهة، والمعاملات الدقيقة، وفحوصات الجودة، وفخاخ الاختبار الشائعة.'
              : 'End-to-end procedural guides across all 4 exam domains with UI paths, exact tool parameters, quality control checks, and common exam mistakes.'}
          </p>
        </div>

        {/* Filter Controls */}
        <div className="mt-6 grid grid-cols-1 gap-3 sm:grid-cols-2 pt-4 border-t border-slate-700/60">
          <div className="relative">
            <Search size={15} className="absolute left-3 top-2.5 text-slate-400" />
            <input
              type="text"
              value={search}
              onChange={e => setSearch(e.target.value)}
              placeholder={lang === 'ar' ? 'ابحث في مسار العمل أو الأداة...' : 'Search workflows or tools...'}
              className="w-full rounded-xl border border-slate-700 bg-slate-950/60 py-2 pl-9 pr-3 text-xs text-white placeholder-slate-400 focus:border-teal-500 focus:outline-none"
            />
          </div>

          <div className="flex items-center gap-2">
            <Filter size={15} className="text-slate-400 shrink-0" />
            <select
              value={domainFilter}
              onChange={e => setDomainFilter(e.target.value)}
              aria-label="Domain Filter"
              className="w-full rounded-xl border border-slate-700 bg-slate-950/60 p-2 text-xs text-white focus:border-teal-500 focus:outline-none"
            >
              <option value="all">{lang === 'ar' ? 'كافة النطاقات (30 مساراً)' : 'All Domains (30 Workflows)'}</option>
              <option value="Data Management">{lang === 'ar' ? 'إدارة البيانات (10)' : 'Data Management (10)'}</option>
              <option value="Visualization">{lang === 'ar' ? 'العرض البصري (7)' : 'Visualization (7)'}</option>
              <option value="Analysis and Geoprocessing">{lang === 'ar' ? 'التحليل والمعالجة (7)' : 'Analysis & GP (7)'}</option>
              <option value="Layouts and Sharing">{lang === 'ar' ? 'اللوحات والمشاركة (6)' : 'Layouts & Sharing (6)'}</option>
            </select>
          </div>
        </div>

        <div className="mt-3 text-right text-xs text-slate-400">
          {lang === 'ar' ? `عرض ${filtered.length} من 30 مسار عمل` : `Showing ${filtered.length} of 30 workflows`}
        </div>
      </div>

      {/* Workflows Accordion */}
      <div className="space-y-4">
        {filtered.map(wf => {
          const isExpanded = expandedId === wf.id;
          const completedCount = wf.steps.filter(st => completedSteps[`${wf.id}_${st.stepNumber}`]).length;

          return (
            <div
              key={wf.id}
              className="rounded-2xl border border-slate-200 bg-white shadow-sm transition dark:border-slate-800 dark:bg-slate-900/90 overflow-hidden"
            >
              {/* Header */}
              <div
                onClick={() => setExpandedId(isExpanded ? null : wf.id)}
                className="flex cursor-pointer flex-wrap items-center justify-between gap-3 p-5 hover:bg-slate-50 dark:hover:bg-slate-800/50 transition"
              >
                <div className="flex items-center gap-3">
                  <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-teal-500/10 font-mono text-sm font-black text-teal-600 dark:bg-teal-950/60 dark:text-teal-400">
                    {wf.id}
                  </span>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="rounded bg-slate-100 px-2 py-0.5 text-[10px] font-bold text-slate-700 dark:bg-slate-800 dark:text-slate-300">
                        {wf.domain}
                      </span>
                      <span className="rounded bg-slate-100 px-2 py-0.5 text-[10px] text-slate-600 dark:bg-slate-800 dark:text-slate-400">
                        {wf.difficulty}
                      </span>
                    </div>
                    <h2 className="text-base font-bold text-slate-900 dark:text-white sm:text-lg">
                      {lang === 'ar' ? wf.title.ar : wf.title.en}
                    </h2>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <span className="text-xs font-mono font-semibold text-slate-500">
                    {completedCount}/{wf.steps.length} {lang === 'ar' ? 'خطوات مكتملة' : 'done'}
                  </span>
                  <span className="text-slate-400">
                    {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                  </span>
                </div>
              </div>

              {/* Collapsible Details */}
              {isExpanded && (
                <div className="border-t border-slate-200 p-5 space-y-6 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/30">
                  {/* Objective */}
                  <div className="rounded-xl border border-teal-200 bg-teal-50/60 p-4 dark:border-teal-900/40 dark:bg-teal-950/20">
                    <span className="text-xs font-bold uppercase tracking-wider text-teal-700 dark:text-teal-400">
                      {lang === 'ar' ? 'الهدف التشغيلي للمسار:' : 'Operational Workflow Objective:'}
                    </span>
                    <p className="mt-1 text-sm font-medium text-slate-800 dark:text-slate-200">
                      {lang === 'ar' ? wf.objective.ar : wf.objective.en}
                    </p>
                  </div>

                  {/* Starting Conditions & Tools */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div className="rounded-xl border border-slate-200 bg-white p-3.5 dark:border-slate-800 dark:bg-slate-900 space-y-1">
                      <span className="font-bold text-slate-500 dark:text-slate-400">
                        {lang === 'ar' ? 'متطلبات البيانات الأولية:' : 'Initial Data Requirements:'}
                      </span>
                      <p className="text-slate-700 dark:text-slate-300">
                        {lang === 'ar' ? wf.initialData.ar : wf.initialData.en}
                      </p>
                    </div>

                    <div className="rounded-xl border border-slate-200 bg-white p-3.5 dark:border-slate-800 dark:bg-slate-900 space-y-1">
                      <span className="font-bold text-slate-500 dark:text-slate-400">
                        {lang === 'ar' ? 'شروط البدء في المشروع:' : 'Starting Project Conditions:'}
                      </span>
                      <p className="text-slate-700 dark:text-slate-300">
                        {lang === 'ar' ? wf.startingConditions.ar : wf.startingConditions.en}
                      </p>
                    </div>
                  </div>

                  {/* Step by Step Walkthrough */}
                  <div className="space-y-3">
                    <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center gap-1.5">
                      <Wrench size={14} /> {lang === 'ar' ? 'الخطوات الإجرائية التفصيلية في ArcGIS Pro' : 'Step-by-Step Execution Sequence'}
                    </h3>

                    <div className="space-y-2.5">
                      {wf.steps.map(st => {
                        const isDone = !!completedSteps[`${wf.id}_${st.stepNumber}`];
                        return (
                          <div
                            key={st.stepNumber}
                            className={`rounded-xl border p-4 transition ${
                              isDone
                                ? 'border-emerald-300 bg-emerald-50/50 dark:border-emerald-900/50 dark:bg-emerald-950/20'
                                : 'border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900'
                            }`}
                          >
                            <div className="flex items-start justify-between gap-3">
                              <div className="flex items-start gap-3">
                                <button
                                  onClick={() => toggleStep(wf.id, st.stepNumber)}
                                  className={`mt-0.5 rounded p-1 transition ${
                                    isDone ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-300 hover:text-slate-500'
                                  }`}
                                  title={isDone ? 'Mark as incomplete' : 'Mark step as completed'}
                                >
                                  <CheckCircle2 size={18} />
                                </button>
                                <div className="space-y-1">
                                  <div className="flex items-center gap-2">
                                    <span className="font-mono text-xs font-bold text-teal-600 dark:text-teal-400">
                                      Step {st.stepNumber}:
                                    </span>
                                    <h4 className="text-xs sm:text-sm font-bold text-slate-900 dark:text-white">
                                      {lang === 'ar' ? st.title.ar : st.title.en}
                                    </h4>
                                  </div>
                                  <p className="text-xs leading-relaxed text-slate-700 dark:text-slate-300">
                                    {lang === 'ar' ? st.instruction.ar : st.instruction.en}
                                  </p>

                                  {/* UI Path */}
                                  {st.uiPath && (
                                    <div className="pt-1 text-[11px] font-mono text-sky-600 dark:text-sky-400">
                                      <strong className="text-slate-400">UI Path:</strong> {st.uiPath}
                                    </div>
                                  )}

                                  {/* Parameters */}
                                  {st.parameters && Object.keys(st.parameters).length > 0 && (
                                    <div className="pt-1 flex flex-wrap gap-1.5">
                                      {Object.entries(st.parameters).map(([k, v]) => (
                                        <span
                                          key={k}
                                          className="rounded bg-slate-100 px-2 py-0.5 font-mono text-[10px] text-slate-700 dark:bg-slate-800 dark:text-slate-300 border border-slate-200 dark:border-slate-700"
                                        >
                                          <strong>{k}:</strong> {String(v)}
                                        </span>
                                      ))}
                                    </div>
                                  )}
                                </div>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  {/* Quality Control & Mistakes Grid */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    {/* Expected Output & QC */}
                    <div className="rounded-xl border border-emerald-200 bg-emerald-50/40 p-4 dark:border-emerald-900/40 dark:bg-emerald-950/20 space-y-2">
                      <div className="flex items-center gap-1.5 font-bold text-emerald-800 dark:text-emerald-300">
                        <ShieldCheck size={16} /> {lang === 'ar' ? 'المخرج المتوقع وفحص الجودة (QC)' : 'Expected Output & Quality Control'}
                      </div>
                      <p className="text-slate-700 dark:text-slate-300 leading-relaxed">
                        {lang === 'ar' ? wf.expectedOutput.ar : wf.expectedOutput.en}
                      </p>
                      <div className="pt-2 border-t border-emerald-200 dark:border-emerald-900/40 text-[11px] text-emerald-700 dark:text-emerald-400">
                        <strong>QC Check:</strong> {lang === 'ar' ? wf.qualityControl.ar : wf.qualityControl.en}
                      </div>
                    </div>

                    {/* Common Mistakes */}
                    <div className="rounded-xl border border-amber-200 bg-amber-50/40 p-4 dark:border-amber-900/40 dark:bg-amber-950/20 space-y-2">
                      <div className="flex items-center gap-1.5 font-bold text-amber-800 dark:text-amber-300">
                        <AlertTriangle size={16} /> {lang === 'ar' ? 'الأخطاء الشائعة وفخاخ الاختبار' : 'Common Mistakes & Exam Traps'}
                      </div>
                      <p className="text-slate-700 dark:text-slate-300 leading-relaxed">
                        {lang === 'ar' ? wf.commonMistakes.ar : wf.commonMistakes.en}
                      </p>
                      {wf.alternativeApproaches && (
                        <div className="pt-2 border-t border-amber-200 dark:border-amber-900/40 text-[11px] text-amber-700 dark:text-amber-400">
                          <strong>Alternative:</strong> {lang === 'ar' ? wf.alternativeApproaches.ar : wf.alternativeApproaches.en}
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Reference Documentation Link */}
                  {wf.references && wf.references.length > 0 && (
                    <div className="pt-2">
                      <a
                        href={wf.references[0].url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1 text-xs font-semibold text-sky-600 hover:underline dark:text-sky-400"
                      >
                        <ExternalLink size={13} /> {wf.references[0].title}
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

