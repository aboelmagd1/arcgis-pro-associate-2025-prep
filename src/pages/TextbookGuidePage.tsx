import { useState, useEffect, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  BookOpen,
  CheckSquare,
  ExternalLink,
  Play,
  ChevronDown,
  ChevronUp,
  Sparkles,
  Filter,
  Download,
  Globe,
  Layers,
  Search,
  CheckCircle2,
  AlertTriangle,
  Lightbulb,
  ArrowRight,
  Database,
  Palette,
  Cpu,
  Share2,
} from 'lucide-react';
import { useI18n } from '../i18n';
import { loadTextbookGuide } from '../services/content';
import type { TextbookData, TextbookChapter } from '../types/content';

export default function TextbookGuidePage() {
  const { lang } = useI18n();
  const navigate = useNavigate();
  const [data, setData] = useState<TextbookData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedDomain, setSelectedDomain] = useState<string>('all');
  const [expandedChapter, setExpandedChapter] = useState<number | null>(1);
  const [searchQuery, setSearchQuery] = useState('');

  // Persisted completion tracking for exercises
  const [completedExercises, setCompletedExercises] = useState<Record<string, boolean>>(() => {
    try {
      return JSON.parse(localStorage.getItem('eapa.completedGtkExercises') ?? '{}');
    } catch {
      return {};
    }
  });

  useEffect(() => {
    loadTextbookGuide()
      .then((res) => {
        setData(res);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const toggleExercise = (exId: string) => {
    const next = { ...completedExercises, [exId]: !completedExercises[exId] };
    setCompletedExercises(next);
    try {
      localStorage.setItem('eapa.completedGtkExercises', JSON.stringify(next));
    } catch {
      // storage unavailable
    }
  };

  const domainMap: Record<string, string> = {
    data: 'Data Management',
    viz: 'Visualization',
    analysis: 'Analysis and Geoprocessing',
    sharing: 'Layouts and Sharing',
  };

  const domainIcons: Record<string, any> = {
    'Data Management': Database,
    Visualization: Palette,
    'Analysis and Geoprocessing': Cpu,
    'Layouts and Sharing': Share2,
  };

  const domainBadgeColors: Record<string, string> = {
    'Data Management': 'bg-blue-100 text-blue-800 dark:bg-blue-950/60 dark:text-blue-300 border-blue-200 dark:border-blue-900',
    Visualization: 'bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300 border-amber-200 dark:border-amber-900',
    'Analysis and Geoprocessing': 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-200 dark:border-emerald-900',
    'Layouts and Sharing': 'bg-purple-100 text-purple-800 dark:bg-purple-950/60 dark:text-purple-300 border-purple-200 dark:border-purple-900',
  };

  const filteredChapters = useMemo(() => {
    if (!data) return [];
    return data.chapters.filter((ch) => {
      // Domain filter
      if (selectedDomain !== 'all') {
        const fullDomain = domainMap[selectedDomain] ?? selectedDomain;
        const matchesPrimary = ch.primaryDomain === fullDomain;
        const matchesSecondary = ch.domains.includes(fullDomain);
        if (!matchesPrimary && !matchesSecondary) return false;
      }
      // Search filter
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase();
        const matchesTitle =
          ch.title_en.toLowerCase().includes(q) ||
          ch.title_ar.toLowerCase().includes(q);
        const matchesScenario =
          ch.scenario_en.toLowerCase().includes(q) ||
          ch.scenario_ar.toLowerCase().includes(q);
        const matchesExercise = ch.exercises.some(
          (ex) =>
            ex.title_en.toLowerCase().includes(q) ||
            ex.title_ar.toLowerCase().includes(q) ||
            ex.tools.some((t) => t.toLowerCase().includes(q))
        );
        return matchesTitle || matchesScenario || matchesExercise;
      }
      return true;
    });
  }, [data, selectedDomain, searchQuery]);

  // Overall statistics
  const totalExercises = useMemo(() => {
    if (!data) return 0;
    return data.chapters.reduce((acc, ch) => acc + ch.exercises.length, 0);
  }, [data]);

  const completedCount = useMemo(() => {
    return Object.values(completedExercises).filter(Boolean).length;
  }, [completedExercises]);

  const progressPercent = totalExercises > 0 ? Math.round((completedCount / totalExercises) * 100) : 0;

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="flex items-center gap-3 text-slate-500">
          <div className="h-6 w-6 animate-spin rounded-full border-2 border-sky-500 border-t-transparent" />
          <p className="text-sm font-medium">
            {lang === 'ar'
              ? 'جارٍ تحميل دليل الكتاب والتمارين...'
              : 'Loading textbook companion & exercises...'}
          </p>
        </div>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="rounded-xl border border-rose-300 bg-rose-50 p-6 text-rose-800 dark:border-rose-900 dark:bg-rose-950/40 dark:text-rose-200">
        <p className="font-bold">
          {lang === 'ar' ? 'فشل تحميل دليل الكتاب' : 'Failed to load textbook guide'}: {error}
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6 pb-12">
      {/* Hero Header */}
      <div className="relative overflow-hidden rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-sky-950 p-6 md:p-8 text-white shadow-xl">
        <div className="relative z-10 space-y-4 max-w-4xl">
          <div className="inline-flex items-center gap-2 rounded-full bg-sky-500/20 px-3 py-1 text-xs font-semibold text-sky-300 ring-1 ring-inset ring-sky-500/30">
            <Sparkles size={14} className="text-sky-400" />
            <span>Esri Press Official Textbook Companion • EAPA_2025 Blueprint</span>
          </div>

          <h1 className="text-2xl md:text-4xl font-extrabold tracking-tight">
            {lang === 'ar'
              ? 'دليل كتاب Getting to Know ArcGIS Pro 3.2 والمختبرات التطبيقية'
              : 'Getting to Know ArcGIS Pro 3.2 Master Lab Companion'}
          </h1>

          <p className="text-xs md:text-sm text-slate-300 leading-relaxed max-w-3xl">
            {lang === 'ar'
              ? 'دليل تفصيلي شامل مرتب بنفس تسلسل فصول وتمارين كتاب Esri Press الرسمي (Michael Law & Amy Collins). يحتوي على شرح المشاريع الواقعية، ومسارات النقر في واجهة آرك برو، وأدوات التحليل، وفخاخ الامتحان، مع تصنيف دقيق يربط كل تمرين بمجالات الاختبار الأربعة.'
              : 'Comprehensive guide organized in the exact chapter-by-chapter sequence of the official Esri Press textbook by Michael Law & Amy Collins. Fully classified across the 4 EAPA_2025 exam domains with UI paths, real-world scenarios, and exam trap alerts.'}
          </p>

          {/* Progress bar */}
          <div className="pt-2 flex flex-col sm:flex-row items-start sm:items-center gap-3 max-w-lg">
            <div className="w-full bg-slate-800/80 rounded-full h-2.5 overflow-hidden border border-slate-700">
              <div
                className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
            <span className="text-xs font-mono font-bold text-emerald-400 whitespace-nowrap">
              {completedCount} / {totalExercises} {lang === 'ar' ? 'تمرين مكتمل' : 'Labs Done'} ({progressPercent}%)
            </span>
          </div>
        </div>
      </div>

      {/* Official Download & Resources Cards (Featuring the 2 user links) */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-sm font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center gap-2">
            <Download size={16} className="text-sky-500" />
            <span>{lang === 'ar' ? 'روابط تحميل البيانات والخرائط الرسمية للكتاب' : 'Official Textbook Exercise Data & Web Maps'}</span>
          </h2>
          <span className="text-xs text-slate-400 font-mono">ArcGIS Online Items</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Link 1: Official Exercise Data Package */}
          <div className="rounded-2xl border border-emerald-500/30 bg-gradient-to-br from-emerald-50/60 to-white dark:from-emerald-950/20 dark:to-slate-900 p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between">
            <div className="space-y-2">
              <div className="flex items-center justify-between gap-2">
                <span className="inline-flex items-center gap-1.5 rounded-lg bg-emerald-100 dark:bg-emerald-900/60 px-2.5 py-1 text-xs font-bold text-emerald-800 dark:text-emerald-300">
                  <Download size={13} />
                  <span>{lang === 'ar' ? 'حزمة البيانات والتمارين (.zip)' : 'Official Exercise Data (.zip)'}</span>
                </span>
                <span className="text-[11px] font-mono text-slate-400">ID: 0395a02959fa...</span>
              </div>
              <h3 className="text-sm font-bold text-slate-900 dark:text-white">
                {lang === 'ar'
                  ? 'Getting to Know ArcGIS Pro 3.2 – Exercise Data Package'
                  : 'Getting to Know ArcGIS Pro 3.2 – Exercise Data Package'}
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                {lang === 'ar'
                  ? 'الملف المضغوط الرسمي من Esri Press الذي يحتوي على كافة مشاريع (.aprx) وقواعد البيانات (.gdb) والصور والراستر المستخدمة في فصول الكتاب من 1 إلى 9.'
                  : 'The official Esri Press zip package containing all project files (.aprx), geodatabases (.gdb), shapefiles, rasters, and tables required for Chapters 1 through 9.'}
              </p>
              <div className="rounded-lg bg-emerald-50/90 dark:bg-emerald-950/40 p-2.5 text-[11px] text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-900/60">
                <span className="font-bold">{lang === 'ar' ? 'طريقة التثبيت:' : 'Installation Instruction:'}</span>{' '}
                {lang === 'ar'
                  ? 'قم بفك الضغط وضع المجلد في المسار C:\\EsriPress\\GTKPro لتفتح كافة المشاريع مباشرة دون فقدان مسارات البيانات.'
                  : 'Extract and place the folder in C:\\EsriPress\\GTKPro to run all project files without broken data source links.'}
              </div>
            </div>
            <div className="pt-4 mt-2 border-t border-emerald-100 dark:border-emerald-950 flex items-center justify-between">
              <a
                href="https://www.arcgis.com/home/item.html?id=0395a02959fa4de6bf4318aca4c3b3e8#overview"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 text-xs font-bold shadow transition"
              >
                <span>{lang === 'ar' ? 'فتح وتحميل البيانات على ArcGIS Online' : 'Download on ArcGIS Online'}</span>
                <ExternalLink size={13} />
              </a>
              <span className="text-[10px] text-slate-400 font-mono">Size: ~2.5 GB</span>
            </div>
          </div>

          {/* Link 2: Web Resources & Layers */}
          <div className="rounded-2xl border border-sky-500/30 bg-gradient-to-br from-sky-50/60 to-white dark:from-sky-950/20 dark:to-slate-900 p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between">
            <div className="space-y-2">
              <div className="flex items-center justify-between gap-2">
                <span className="inline-flex items-center gap-1.5 rounded-lg bg-sky-100 dark:bg-sky-900/60 px-2.5 py-1 text-xs font-bold text-sky-800 dark:text-sky-300">
                  <Globe size={13} />
                  <span>{lang === 'ar' ? 'خرائط وطبقات الويب المرافقة' : 'Web Maps & Feature Layers'}</span>
                </span>
                <span className="text-[11px] font-mono text-slate-400">ID: 7a6aaff321b5...</span>
              </div>
              <h3 className="text-sm font-bold text-slate-900 dark:text-white">
                {lang === 'ar'
                  ? 'Getting to Know ArcGIS Pro 3.2 – Web Maps & Shared Layers'
                  : 'Getting to Know ArcGIS Pro 3.2 – Web Maps & Shared Layers'}
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                {lang === 'ar'
                  ? 'عنصر ArcGIS Online المرافق الذي يحتوي على خرائط الويب الجاهزة وخدمات الطبقات السحابية المستخدمة في الفصل الأول (ArcGIS Online) والفصل التاسع (المشاركة والنشر).'
                  : 'ArcGIS Online companion item containing shared web maps, cloud feature layers, and hosted services used in Chapter 1 (ArcGIS Online exploration) and Chapter 9 (Publishing).'}
              </p>
              <div className="rounded-lg bg-sky-50/90 dark:bg-sky-950/40 p-2.5 text-[11px] text-sky-800 dark:text-sky-300 border border-sky-200 dark:border-sky-900/60">
                <span className="font-bold">{lang === 'ar' ? 'محتوى العنصر:' : 'Resource Features:'}</span>{' '}
                {lang === 'ar'
                  ? 'خرائط ويب تفاعلية، خدمات الرموز، ونماذج التسميات السحابية للتطبيق المباشر عبر المتصفح.'
                  : 'Interactive web maps, layer styling services, and cloud pop-up configurations for browser exercises.'}
              </div>
            </div>
            <div className="pt-4 mt-2 border-t border-sky-100 dark:border-sky-950 flex items-center justify-between">
              <a
                href="https://www.arcgis.com/home/item.html?id=7a6aaff321b5421db15626d4ea10b3ce#overview"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white px-4 py-2 text-xs font-bold shadow transition"
              >
                <span>{lang === 'ar' ? 'فتح عنصر الويب على ArcGIS Online' : 'View on ArcGIS Online'}</span>
                <ExternalLink size={13} />
              </a>
              <span className="text-[10px] text-slate-400 font-mono">Public Item</span>
            </div>
          </div>
        </div>
      </section>

      {/* Filter and Search Bar */}
      <section className="space-y-3">
        <div className="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">
          {/* Domain Filter Pills */}
          <div className="flex flex-wrap gap-2">
            <button
              onClick={() => setSelectedDomain('all')}
              className={`rounded-xl px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 ${
                selectedDomain === 'all'
                  ? 'bg-sky-600 text-white shadow-sm'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <Filter size={13} />
              <span>{lang === 'ar' ? 'كافة الفصول (1-9)' : 'All Chapters (1–9)'}</span>
            </button>
            <button
              onClick={() => setSelectedDomain('data')}
              className={`rounded-xl px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 ${
                selectedDomain === 'data'
                  ? 'bg-blue-600 text-white shadow-sm'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <Database size={13} />
              <span>{lang === 'ar' ? 'إدارة البيانات (32%)' : 'Data Management (32%)'}</span>
            </button>
            <button
              onClick={() => setSelectedDomain('viz')}
              className={`rounded-xl px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 ${
                selectedDomain === 'viz'
                  ? 'bg-amber-600 text-white shadow-sm'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <Palette size={13} />
              <span>{lang === 'ar' ? 'العرض البصري (25%)' : 'Visualization (25%)'}</span>
            </button>
            <button
              onClick={() => setSelectedDomain('analysis')}
              className={`rounded-xl px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 ${
                selectedDomain === 'analysis'
                  ? 'bg-emerald-600 text-white shadow-sm'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <Cpu size={13} />
              <span>{lang === 'ar' ? 'التحليل والمعالجة (25%)' : 'Analysis & GP (25%)'}</span>
            </button>
            <button
              onClick={() => setSelectedDomain('sharing')}
              className={`rounded-xl px-3 py-1.5 text-xs font-bold transition flex items-center gap-1.5 ${
                selectedDomain === 'sharing'
                  ? 'bg-purple-600 text-white shadow-sm'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <Share2 size={13} />
              <span>{lang === 'ar' ? 'التخطيطات والمشاركة (18%)' : 'Layouts & Sharing (18%)'}</span>
            </button>
          </div>

          {/* Search Input */}
          <div className="relative min-w-[240px]">
            <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              placeholder={lang === 'ar' ? 'بحث في الفصول أو الأدوات أو السيناريو...' : 'Search chapters, tools, or scenarios...'}
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 pl-9 pr-3 py-1.5 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:border-sky-500 focus:outline-none focus:ring-1 focus:ring-sky-500"
            />
          </div>
        </div>
      </section>

      {/* Chapters Accordion List (Ordered 1 to 9 exactly as in textbook) */}
      <section className="space-y-4">
        {filteredChapters.map((ch) => {
          const isExpanded = expandedChapter === ch.chapterNumber;
          const PrimaryIcon = domainIcons[ch.primaryDomain] || BookOpen;
          const chExercisesDone = ch.exercises.filter((ex) => !!completedExercises[ex.id]).length;
          const chTotal = ch.exercises.length;

          return (
            <div
              key={ch.chapterNumber}
              className="rounded-2xl border border-slate-200 bg-white shadow-sm transition dark:border-slate-800 dark:bg-slate-900 overflow-hidden"
            >
              {/* Chapter Header Bar */}
              <div
                onClick={() => setExpandedChapter(isExpanded ? null : ch.chapterNumber)}
                className="flex cursor-pointer flex-wrap items-center justify-between gap-3 p-5 hover:bg-slate-50 dark:hover:bg-slate-800/50 transition"
              >
                <div className="flex items-center gap-3.5">
                  <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-sky-500/10 font-mono text-sm font-black text-sky-600 dark:bg-sky-950/60 dark:text-sky-400 border border-sky-500/20">
                    Ch {ch.chapterNumber}
                  </span>
                  <div>
                    <div className="flex flex-wrap items-center gap-2 mb-1">
                      <span className={`inline-flex items-center gap-1 rounded-md px-2 py-0.5 text-[10px] font-bold border ${domainBadgeColors[ch.primaryDomain]}`}>
                        <PrimaryIcon size={11} />
                        <span>{ch.primaryDomain}</span>
                      </span>
                      <span className="text-[11px] font-mono text-slate-400">
                        {ch.examWeight}
                      </span>
                      <span className="text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold bg-emerald-50 dark:bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-900">
                        {chExercisesDone}/{chTotal} {lang === 'ar' ? 'تمارين مكتملة' : 'Labs Done'}
                      </span>
                    </div>
                    <h2 className="text-base sm:text-lg font-bold text-slate-900 dark:text-white">
                      {lang === 'ar' ? `الفصل ${ch.chapterNumber}: ${ch.title_ar}` : `Chapter ${ch.chapterNumber}: ${ch.title_en}`}
                    </h2>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      navigate(`/exam?preset=domain&domain=${encodeURIComponent(ch.primaryDomain)}`);
                    }}
                    className="flex items-center gap-1.5 rounded-lg bg-teal-600 px-3 py-1.5 text-xs font-bold text-white shadow-sm hover:bg-teal-500 transition"
                    title={lang === 'ar' ? 'بدء اختبار لأسئلة هذا المجال' : 'Practice questions for this domain'}
                  >
                    <Play size={13} />
                    <span>{lang === 'ar' ? 'اختبار المجال' : 'Domain Quiz'}</span>
                  </button>
                  <span className="text-slate-400 p-1">
                    {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                  </span>
                </div>
              </div>

              {/* Collapsible Content */}
              {isExpanded && (
                <div className="border-t border-slate-200 p-5 md:p-6 space-y-6 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/40">
                  {/* Real-World Project Scenario Box */}
                  <div className="rounded-2xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900 space-y-2">
                    <span className="text-[11px] font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400 flex items-center gap-1.5">
                      <Globe size={14} />
                      <span>{lang === 'ar' ? 'مشروع وسيناريو الفصل الواقعي (Project Scenario):' : 'Chapter Real-World Project Scenario:'}</span>
                    </span>
                    <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
                      {lang === 'ar' ? ch.scenario_ar : ch.scenario_en}
                    </p>
                  </div>

                  {/* Exercises List */}
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                        <CheckSquare size={14} className="text-emerald-500" />
                        <span>{lang === 'ar' ? 'التمارين التطبيقية خطوة بخطوة:' : 'Step-by-Step Hands-On Exercises:'}</span>
                      </h3>
                      <span className="text-xs text-slate-400">
                        {lang === 'ar' ? 'اضغط لتأكيد إنجاز التمرين في البرنامج' : 'Check off as you complete in Pro'}
                      </span>
                    </div>

                    <div className="space-y-3">
                      {ch.exercises.map((ex) => {
                        const isDone = !!completedExercises[ex.id];
                        return (
                          <div
                            key={ex.id}
                            className={`rounded-xl border p-4 transition ${
                              isDone
                                ? 'bg-emerald-50/70 border-emerald-300 dark:bg-emerald-950/20 dark:border-emerald-900/80'
                                : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800'
                            }`}
                          >
                            <div className="flex items-start justify-between gap-3 mb-2">
                              <label className="flex items-start gap-2.5 cursor-pointer">
                                <input
                                  type="checkbox"
                                  checked={isDone}
                                  onChange={() => toggleExercise(ex.id)}
                                  className="mt-0.5 h-4 w-4 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500 cursor-pointer"
                                />
                                <div>
                                  <h4 className={`text-xs sm:text-sm font-bold ${isDone ? 'line-through text-emerald-900 dark:text-emerald-300' : 'text-slate-900 dark:text-white'}`}>
                                    {lang === 'ar' ? ex.title_ar : ex.title_en}
                                  </h4>
                                </div>
                              </label>
                              <span className="rounded bg-slate-100 dark:bg-slate-800 px-2 py-0.5 text-[10px] font-mono text-slate-500">
                                {ex.domain}
                              </span>
                            </div>

                            {/* Objectives */}
                            <div className="space-y-1.5 pl-6 pt-1 text-xs text-slate-600 dark:text-slate-400">
                              <span className="font-semibold text-slate-700 dark:text-slate-300 block mb-1">
                                {lang === 'ar' ? 'الخطوات والأهداف الإجرائية:' : 'Exercise Objectives & Procedural Steps:'}
                              </span>
                              {(lang === 'ar' ? ex.objectives_ar : ex.objectives_en).map((obj, oIdx) => (
                                <div key={oIdx} className="flex items-start gap-2 leading-relaxed">
                                  <span className="text-sky-500 font-bold shrink-0">•</span>
                                  <span>{obj}</span>
                                </div>
                              ))}
                            </div>

                            {/* Tools and UI Path */}
                            <div className="mt-3 pl-6 pt-2 border-t border-slate-100 dark:border-slate-800 flex flex-wrap items-center justify-between gap-2 text-xs">
                              <div className="flex flex-wrap items-center gap-1.5">
                                <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400">
                                  {lang === 'ar' ? 'الأدوات:' : 'Tools:'}
                                </span>
                                {ex.tools.map((t, tIdx) => (
                                  <span
                                    key={tIdx}
                                    className="rounded-md bg-slate-100 dark:bg-slate-800 px-2 py-0.5 text-[11px] font-mono text-sky-700 dark:text-sky-300"
                                  >
                                    {t}
                                  </span>
                                ))}
                              </div>
                              <div className="rounded bg-slate-50 dark:bg-slate-950 px-2 py-1 font-mono text-[11px] text-slate-500 dark:text-slate-400 border border-slate-200/80 dark:border-slate-800/80">
                                {ex.uiPath}
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>

                  {/* Exam Focus & Traps Grid */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3 pt-2">
                    {/* Exam Focus */}
                    <div className="rounded-xl border border-sky-200 bg-sky-50/50 p-4 dark:border-sky-900/60 dark:bg-sky-950/20 space-y-1.5">
                      <span className="text-xs font-bold text-sky-800 dark:text-sky-300 flex items-center gap-1.5">
                        <Lightbulb size={15} />
                        <span>{lang === 'ar' ? 'ما يركز عليه اختبار EAPA_2025 في هذا الفصل:' : 'EAPA_2025 Exam Core Alignment:'}</span>
                      </span>
                      <p className="text-xs text-sky-900/90 dark:text-sky-200/90 leading-relaxed">
                        {lang === 'ar' ? ch.examFocus_ar : ch.examFocus_en}
                      </p>
                    </div>

                    {/* Exam Traps */}
                    <div className="rounded-xl border border-amber-200 bg-amber-50/50 p-4 dark:border-amber-900/60 dark:bg-amber-950/20 space-y-1.5">
                      <span className="text-xs font-bold text-amber-800 dark:text-amber-300 flex items-center gap-1.5">
                        <AlertTriangle size={15} />
                        <span>{lang === 'ar' ? 'فخاخ الاختبار الشائعة (Exam Traps):' : 'Common Exam Pitfalls & Traps:'}</span>
                      </span>
                      <p className="text-xs text-amber-900/90 dark:text-amber-200/90 leading-relaxed">
                        {lang === 'ar' ? ch.examTraps_ar : ch.examTraps_en}
                      </p>
                    </div>
                  </div>

                  {/* Chapter Actions */}
                  <div className="flex flex-wrap items-center justify-between gap-3 pt-3 border-t border-slate-200 dark:border-slate-800">
                    <div className="flex items-center gap-2">
                      <button
                        onClick={() => navigate(`/exam?preset=domain&domain=${encodeURIComponent(ch.primaryDomain)}`)}
                        className="inline-flex items-center gap-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white px-3.5 py-1.5 text-xs font-bold shadow-sm transition"
                      >
                        <Play size={13} />
                        <span>{lang === 'ar' ? `اختبار أسئلة ${ch.primaryDomain}` : `Quiz ${ch.primaryDomain}`}</span>
                      </button>
                      <button
                        onClick={() => navigate('/workflows')}
                        className="inline-flex items-center gap-1.5 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 px-3 py-1.5 text-xs font-medium text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                      >
                        <Layers size={13} />
                        <span>{lang === 'ar' ? 'تمارين سير العمل المشابهة' : 'Matching Workflows'}</span>
                      </button>
                    </div>
                    <span className="text-xs text-slate-400 font-mono">
                      Law & Collins • Chapter {ch.chapterNumber}
                    </span>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </section>
    </div>
  );
}
