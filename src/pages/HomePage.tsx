import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {
  Timer,
  BookOpen,
  FolderKanban,
  GitBranch,
  Layers,
  Compass,
  BarChart3,
  Bookmark,
  CheckCircle2,
  ExternalLink,
  Sparkles,
  ArrowRight,
  Database,
  Palette,
  Cpu,
  Share2,
} from 'lucide-react';
import { useI18n } from '../i18n';
import { loadProgress } from '../storage/store';

export default function HomePage() {
  const { lang } = useI18n();
  const [readiness, setReadiness] = useState<number>(0);
  const [totalAttempts, setTotalAttempts] = useState<number>(0);
  const [bookmarkCount, setBookmarkCount] = useState<number>(0);

  useEffect(() => {
    const prog = loadProgress();
    const attempts = prog.attempts || [];
    const bookmarks = prog.bookmarks || [];
    setTotalAttempts(attempts.length);
    setBookmarkCount(bookmarks.length);

    if (attempts.length > 0) {
      const answered = attempts.flatMap((a) => a.answers.filter((ans) => ans.selected !== null));
      const correct = answered.filter((ans) => ans.correct).length;
      const score = answered.length > 0 ? Math.round((correct / answered.length) * 100) : 0;
      setReadiness(score);
    } else {
      setReadiness(0);
    }
  }, []);

  const domains = [
    {
      id: 'Data Management',
      domainKey: 'data',
      titleEn: 'Data Management',
      titleAr: 'إدارة البيانات',
      weight: '32%',
      modulesCovered: 'Modules 1, 2, 3, 4',
      modulesCoveredAr: 'الموديولات 1، 2، 3، 4',
      color: 'from-blue-600 to-cyan-600',
      badgeColor: 'bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300',
      icon: Database,
      descEn: 'Geodatabase schema, feature datasets, subtypes, domains, contingent values, topology rules, editing tools, coordinate systems, and geocoding.',
      descAr: 'بنية قواعد البيانات الجغرافية، النطاقات والأنواع الفرعية، القيم المشروطة، قواعد التوبولوجيا، أدوات التحرير، أنظمة الإحداثيات، والتكويد الجغرافي.',
      studyTopicsEn: [
        'File Geodatabase Architecture vs Shapefile (2GB limit & 10-char names)',
        'Coded Value & Range Domains + Split/Merge Policies',
        'Subtypes (Short/Long Int) & Contingent Values (Field Groups)',
        'Geodatabase Topology vs Map Topology & Arcade Attribute Rules',
        'GCS vs PCS, Datum Transformations, & Geocoding Locators',
      ],
      studyTopicsAr: [
        'معمارية File GDB ومقارنتها بـ Shapefile (حدود الـ 2GB وأسماء الحقول)',
        'مجالات السمات (Coded/Range) وسياسات التجزئة والدمج (Split/Merge)',
        'الأنواع الفرعية Subtypes والقيم المشروطة Contingent Values',
        'طوبولوجيا الجيوداتابيز وقواعد السمات التلقائية بلغة Arcade',
        'أنظمة الإحداثيات والتحويلات المكانية ومحددات العناوين Locators',
      ],
      qCount: 80,
      sCount: 48,
    },
    {
      id: 'Visualization',
      domainKey: 'viz',
      titleEn: 'Visualization & Cartography',
      titleAr: 'العرض البصري والخرائط',
      weight: '25%',
      modulesCovered: 'Modules 5, 6, 7',
      modulesCoveredAr: 'الموديولات 5، 6، 7',
      color: 'from-amber-500 to-orange-600',
      badgeColor: 'bg-amber-100 text-amber-800 dark:bg-amber-900/50 dark:text-amber-300',
      icon: Palette,
      descEn: 'Symbology types, 7 classification methods, visual variables, normalization, labeling expressions (Arcade), annotation, and 3D scenes.',
      descAr: 'أساليب الترميز، طرق التصنيف السبعة، المتغيرات البصرية، التعبير الحسابي للتسميات (Arcade)، التسميات التوضيحية، والمشاهد ثلاثية الأبعاد.',
      studyTopicsEn: [
        '7 Classification Methods (Jenks Natural Breaks, Quantile, Equal Interval, etc.)',
        'Visual Variables (Size, Rotation, Color, Transparency) & Normalization',
        'Label Classes, Conflict Resolution, & Arcade expressions',
        'Symbol Layer Drawing & Connecting road casings',
        '3D Global vs Local Scenes, Extrusion, & Voxel layers',
      ],
      studyTopicsAr: [
        'طرق تصنيف البيانات الـ 7 (Jenks Natural Breaks، الفئات المتساوية، النسبية...)',
        'المتغيرات البصرية (الحجم، الدوران، الشفافية) ومعايرة النسب Normalization',
        'فئات التسميات، فض تعارض النصوص، وتعبيرات Arcade الحسابية',
        'رسم طبقات الرموز ودمج تقاطعات الطرق Symbol Layer Drawing',
        'المشاهد ثلاثية الأبعاد (Global vs Local) والتجسيم الرأسي Extrusion',
      ],
      qCount: 63,
      sCount: 38,
    },
    {
      id: 'Analysis and Geoprocessing',
      domainKey: 'analysis',
      titleEn: 'Analysis & Geoprocessing',
      titleAr: 'التحليل والمعالجة الجغرافية',
      weight: '25%',
      modulesCovered: 'Modules 8, 9, 10',
      modulesCoveredAr: 'الموديولات 8، 9، 10',
      color: 'from-emerald-600 to-teal-600',
      badgeColor: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-300',
      icon: Cpu,
      descEn: 'Geoprocessing environment settings, spatial joins, overlay analysis, raster calculations, proximity, ModelBuilder automation, and ArcPy scripts.',
      descAr: 'بيئات المعالجة الجغرافية، الربط المكاني، التحليل التراكبي، حسابات الراستر، تحليلات القرب، أتمتة النماذج عبر ModelBuilder وسكربتات ArcPy.',
      studyTopicsEn: [
        'GP Environments (Extent, Output Coordinate System, Snap Raster, Mask)',
        'Spatial Joins vs Table Joins vs Relationship Classes',
        'Overlay Analysis (Intersect, Spatial Clip, Union, Erase, Symmetrical Diff)',
        'ModelBuilder Automation (Preconditions, Iterators, Model Parameters)',
        'Space-Time Pattern Mining (Create Space Time Cube & Emerging Hot Spots)',
      ],
      studyTopicsAr: [
        'بيئات المعالجة (Extent, Output Coordinate System, Snap Raster, Mask)',
        'المقارنة بين الربط المكاني Spatial Join وجداول Add Join وفئات العلاقات',
        'التحليل التراكبي المتقدم (Intersect, Spatial Clip, Union, Erase)',
        'أتمتة النماذج عبر ModelBuilder (الشروط المسبقة، حلقات التكرار Iterators)',
        'تحليل الأنماط الزمانية والمكانية (Space Time Cube و Emerging Hot Spots)',
      ],
      qCount: 62,
      sCount: 37,
    },
    {
      id: 'Layouts and Sharing',
      domainKey: 'sharing',
      titleEn: 'Layouts & Sharing',
      titleAr: 'التخطيطات والمشاركة',
      weight: '18%',
      modulesCovered: 'Modules 11, 12',
      modulesCoveredAr: 'الموديولات 11، 12',
      color: 'from-purple-600 to-indigo-600',
      badgeColor: 'bg-purple-100 text-purple-800 dark:bg-purple-900/50 dark:text-purple-300',
      icon: Share2,
      descEn: 'Map layouts, dynamic text, spatial and grid map series, publishing web layers, vector tile packages, and project (.aprx) sharing.',
      descAr: 'تخطيطات الطباعة، النصوص الديناميكية، سلاسل الخرائط الشبكية والمكانية، نشر طبقات الويب، حزم مربعات المتجهات، ومشاركة حزم المشاريع.',
      studyTopicsEn: [
        'Layout Elements (Map Frames, Scale Bars, North Arrows, Grids & Graticules)',
        'Dynamic Text Tags (Project, Map, & Layout metadata strings)',
        'Spatial Map Series vs Grid Index Map Series',
        'Sharing Web Layers (Feature, Tile, Map Image, Vector Tile Layers)',
        'Project (.ppkx) & Map (.mpkx) Packages & Validation Analyzers',
      ],
      studyTopicsAr: [
        'عناصر لوحة الإخراج (Map Frames, Scale Bars, North Arrows, شبكات الإحداثيات)',
        'النصوص الديناميكية Dynamic Text المستندة إلى سمات الخريطة والمشروع',
        'سلاسل الخرائط المكانية والشبكية (Spatial & Grid Map Series)',
        'نشر طبقات الويب (Web Feature, Tile, Map Image, Vector Tiles)',
        'حزم المشاريع والخرائط (.ppkx, .mpkx) وأداة فحص التجهيز للنشر Analyzer',
      ],
      qCount: 45,
      sCount: 27,
    },
  ];

  const quickFeatures = [
    {
      to: '/modules',
      titleEn: '12 Learning Modules',
      titleAr: '12 وحدة تعليمية تفاعلية',
      descEn: 'Step-by-step curriculum with UI paths, comparison tables, and lab checklists.',
      descAr: 'منهج منظم مع مسارات واجهة آرك برو، جداول المقارنة، وقوائم مراجعة التمارين.',
      icon: BookOpen,
      color: 'text-sky-600 dark:text-sky-400 bg-sky-50 dark:bg-sky-950/50',
    },
    {
      to: '/scenarios',
      titleEn: '150 Practical Scenarios',
      titleAr: '150 سيناريو عملي واقعي',
      descEn: 'Realistic GIS situational challenges with decision rationales and option eliminator.',
      descAr: 'تحديات جيومكانية واقعية تتطلب اتخاذ القرار مع تعليلات تفصيلية وأداة استبعاد الخيارات.',
      icon: FolderKanban,
      color: 'text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/50',
    },
    {
      to: '/workflows',
      titleEn: '30 Step-by-Step Workflows',
      titleAr: '30 سير عمل تطبيقي',
      descEn: 'Applied procedural walkthroughs from Getting to Know ArcGIS Pro with QC rules.',
      descAr: 'تمارين عملية تفصيلية من كتاب آرك جي آي إس برو مع معايير ضبط الجودة والأخطاء الشائعة.',
      icon: GitBranch,
      color: 'text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/50',
    },
    {
      to: '/flashcards',
      titleEn: '100 3D Flashcards',
      titleAr: '100 بطاقة تعليمية ثلاثية الأبعاد',
      descEn: 'Interactive flip cards for quick recall of ArcPy syntax, topology, and shortcuts.',
      descAr: 'بطاقات قلابة للمراجعة السريعة لأوامر ArcPy، قواعد التوبولوجيا، والاختصارات.',
      icon: Layers,
      color: 'text-purple-600 dark:text-purple-400 bg-purple-50 dark:bg-purple-950/50',
    },
    {
      to: '/references',
      titleEn: 'Top 52 Data Management Tools',
      titleAr: 'موسوعة أهم 52 أداة لإدارة البيانات',
      descEn: 'ArcPy syntax, parameters, UI click paths, exam traps, and tool comparisons.',
      descAr: 'صيغ ArcPy البرمجية، المعاملات، مسارات الواجهة، فخاخ الاختبار ومصفوفات المقارنة.',
      icon: Compass,
      color: 'text-cyan-600 dark:text-cyan-400 bg-cyan-50 dark:bg-cyan-950/50',
    },
    {
      to: '/exam?preset=eapa75',
      titleEn: 'Official 75Q Exam Simulator',
      titleAr: 'محاكي الاختبار الرسمي (75 سؤال)',
      descEn: '90-minute timed simulation with official 32/25/25/18% domain weighting.',
      descAr: 'محاكاة كاملة بمدة 90 دقيقة وتوزيع أوزان المجالات الرسمي مع حظر كشف الإجابات.',
      icon: Timer,
      color: 'text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-950/50',
    },
    {
      to: '/analytics',
      titleEn: 'Readiness & Analytics',
      titleAr: 'التحليلات ومستوى الجاهزية',
      descEn: 'Diagnostic score card, domain breakdown, and personalized weak topic practice.',
      descAr: 'بطاقة التقييم التشخيصية، توزيع الإتقان، وتدريبات مخصصة للنقاط الضعيفة.',
      icon: BarChart3,
      color: 'text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/50',
    },
    {
      to: '/bookmarks',
      titleEn: 'Saved Bookmarks & Review',
      titleAr: 'المفضلة والمراجعة المركزة',
      descEn: 'Quick access to bookmarked exam items and questions flagged during study.',
      descAr: 'وصول فوري للأسئلة المحفوظة في المفضلة والمميزة بعلامة للمراجعة.',
      icon: Bookmark,
      color: 'text-teal-600 dark:text-teal-400 bg-teal-50 dark:bg-teal-950/50',
    },
  ];

  return (
    <div className="space-y-8 pb-12">
      {/* Hero Section */}
      <section className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-slate-900 via-slate-800 to-sky-950 p-6 md:p-10 text-white shadow-xl">
        <div className="relative z-10 max-w-3xl space-y-4">
          <div className="inline-flex items-center gap-2 rounded-full bg-sky-500/20 px-3 py-1 text-xs font-semibold text-sky-300 ring-1 ring-inset ring-sky-500/30">
            <Sparkles size={14} className="text-sky-400" />
            <span>Esri ArcGIS Pro Associate 2025 • EAPA_2025</span>
          </div>

          <h1 className="text-3xl md:text-5xl font-extrabold tracking-tight leading-tight">
            {lang === 'ar' ? (
              <>
                منصة التحضير الشاملة لاختبار{' '}
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-cyan-300">
                  ArcGIS Pro Associate 2025
                </span>
              </>
            ) : (
              <>
                Master the{' '}
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-cyan-300">
                  Esri ArcGIS Pro Associate
                </span>{' '}
                2025 Certification
              </>
            )}
          </h1>

          <p className="text-slate-300 text-sm md:text-base leading-relaxed">
            {lang === 'ar'
              ? 'أداة تعليمية وتطبيقية متكاملة وثنائية اللغة بنسبة 100%، صُممت لتغطية أحدث معايير ومجالات اختبار EAPA_2025. تضم 250 سؤال اختيار من متعدد، 150 سيناريو عملي، 30 تمرين خطوة بخطوة، 12 وحدة تعليمية، و100 بطاقة ثلاثية الأبعاد.'
              : 'A rigorous, 100% bilingual (English & Arabic) learning and simulation platform built for the EAPA_2025 exam blueprint. Features 250 verified MCQs, 150 real-world scenarios, 30 practical workflows, 12 modules, and 100 3D flashcards.'}
          </p>

          <div className="flex flex-wrap items-center gap-3 pt-2">
            <Link
              to="/exam?preset=eapa75"
              className="inline-flex items-center gap-2 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 px-5 py-3 text-sm font-bold text-slate-950 shadow-lg hover:from-amber-400 hover:to-amber-500 transition-all hover:scale-[1.02]"
            >
              <Timer size={18} />
              <span>{lang === 'ar' ? 'بدء محاكي الاختبار الرسمي (75Q)' : 'Launch 75Q Pearson Simulation'}</span>
            </Link>

            <Link
              to="/modules"
              className="inline-flex items-center gap-2 rounded-xl bg-white/10 hover:bg-white/20 px-5 py-3 text-sm font-semibold text-white backdrop-blur-sm transition-all border border-white/10"
            >
              <BookOpen size={18} />
              <span>{lang === 'ar' ? 'استعراض الوحدات الـ 12' : 'Explore 12 Modules'}</span>
            </Link>

            <Link
              to="/scenarios"
              className="inline-flex items-center gap-2 rounded-xl bg-white/10 hover:bg-white/20 px-5 py-3 text-sm font-semibold text-white backdrop-blur-sm transition-all border border-white/10"
            >
              <FolderKanban size={18} />
              <span>{lang === 'ar' ? 'حل السيناريوهات (150)' : 'Practice 150 Scenarios'}</span>
            </Link>
          </div>
        </div>

        {/* Floating Readiness Widget */}
        <div className="mt-8 md:mt-0 md:absolute md:top-8 md:right-8 md:w-64 rounded-xl bg-slate-800/80 p-4 border border-slate-700/80 backdrop-blur-md">
          <div className="flex items-center justify-between text-xs text-slate-300 mb-2">
            <span className="font-semibold">{lang === 'ar' ? 'مستوى الجاهزية' : 'Readiness Score'}</span>
            <span className="font-bold text-sky-400 text-sm">{readiness}%</span>
          </div>
          <div className="h-2 w-full rounded-full bg-slate-700 overflow-hidden mb-3">
            <div
              className={`h-full rounded-full transition-all duration-500 ${
                readiness >= 75
                  ? 'bg-emerald-500'
                  : readiness >= 50
                  ? 'bg-amber-500'
                  : 'bg-sky-500'
              }`}
              style={{ width: `${Math.max(readiness, 5)}%` }}
            />
          </div>
          <div className="grid grid-cols-2 gap-2 text-center text-xs">
            <div className="rounded-lg bg-slate-900/60 p-2">
              <span className="block font-bold text-white">{totalAttempts}</span>
              <span className="text-[10px] text-slate-400">{lang === 'ar' ? 'محاولات' : 'Attempts'}</span>
            </div>
            <div className="rounded-lg bg-slate-900/60 p-2">
              <span className="block font-bold text-white">{bookmarkCount}</span>
              <span className="text-[10px] text-slate-400">{lang === 'ar' ? 'في المفضلة' : 'Saved'}</span>
            </div>
          </div>
        </div>
      </section>

      {/* Key Content Metrics Counter Bar */}
      <section className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
        <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 text-center">
          <span className="block text-2xl font-black text-sky-600 dark:text-sky-400">250</span>
          <span className="text-xs font-semibold text-slate-600 dark:text-slate-400">
            {lang === 'ar' ? 'أسئلة اختيار من متعدد' : 'Verified MCQs'}
          </span>
        </div>
        <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 text-center">
          <span className="block text-2xl font-black text-amber-500">150</span>
          <span className="text-xs font-semibold text-slate-600 dark:text-slate-400">
            {lang === 'ar' ? 'سيناريوهات عملية' : 'GIS Scenarios'}
          </span>
        </div>
        <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 text-center">
          <span className="block text-2xl font-black text-emerald-600 dark:text-emerald-400">30</span>
          <span className="text-xs font-semibold text-slate-600 dark:text-slate-400">
            {lang === 'ar' ? 'سير عمل تطبيقي' : 'Workflows'}
          </span>
        </div>
        <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 text-center">
          <span className="block text-2xl font-black text-purple-600 dark:text-purple-400">12</span>
          <span className="text-xs font-semibold text-slate-600 dark:text-slate-400">
            {lang === 'ar' ? 'وحدة تعليمية' : 'Learning Modules'}
          </span>
        </div>
        <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 text-center">
          <span className="block text-2xl font-black text-indigo-600 dark:text-indigo-400">100</span>
          <span className="text-xs font-semibold text-slate-600 dark:text-slate-400">
            {lang === 'ar' ? 'بطاقات ثلاثية الأبعاد' : '3D Flashcards'}
          </span>
        </div>
        <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 text-center">
          <span className="block text-2xl font-black text-cyan-600 dark:text-cyan-400">52</span>
          <span className="text-xs font-semibold text-slate-600 dark:text-slate-400">
            {lang === 'ar' ? 'أداة إدارة بيانات' : 'Top DM Tools'}
          </span>
        </div>
      </section>

      {/* 4 Exam Domains Grid */}
      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-slate-900 dark:text-white">
              {lang === 'ar' ? 'مجالات اختبار آرك جي آي إس برو 2025' : 'Official EAPA_2025 Exam Domains'}
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400">
              {lang === 'ar'
                ? 'توزيع أوزان الأسئلة والمحاور الأربعة المعتمدة من شركة Esri'
                : 'Weighted curriculum according to official Esri certification blueprints'}
            </p>
          </div>
          <Link
            to="/overview"
            className="text-xs font-semibold text-sky-600 dark:text-sky-400 hover:underline inline-flex items-center gap-1"
          >
            <span>{lang === 'ar' ? 'تفاصيل المخطط' : 'Blueprint Details'}</span>
            <ArrowRight size={14} />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {domains.map((dom) => {
            const Icon = dom.icon;
            return (
              <div
                key={dom.id}
                className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-start justify-between gap-3 mb-3">
                    <div className="flex items-center gap-3">
                      <div className={`p-2.5 rounded-xl text-white bg-gradient-to-br ${dom.color}`}>
                        <Icon size={20} />
                      </div>
                      <div>
                        <h3 className="font-bold text-base text-slate-900 dark:text-white">
                          {lang === 'ar' ? dom.titleAr : dom.titleEn}
                        </h3>
                        <span className="text-xs text-slate-400 font-mono">
                          {dom.qCount} MCQs • {dom.sCount} Scenarios
                        </span>
                      </div>
                    </div>
                    <span className={`rounded-full px-2.5 py-1 text-xs font-bold ${dom.badgeColor}`}>
                      {dom.weight}
                    </span>
                  </div>

                  <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-3">
                    {lang === 'ar' ? dom.descAr : dom.descEn}
                  </p>

                  {/* Core Study Checklist / What to Study */}
                  <div className="mb-4 rounded-xl bg-slate-50 dark:bg-slate-950/60 p-3 border border-slate-100 dark:border-slate-800">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-[11px] font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                        <BookOpen size={13} className="text-emerald-500" />
                        <span>{lang === 'ar' ? 'الموضوعات المطلوب مذاكرتها:' : 'Topics to Study:'}</span>
                      </span>
                      <span className="text-[10px] font-semibold text-emerald-700 dark:text-emerald-300 bg-emerald-50 dark:bg-emerald-950/70 px-2 py-0.5 rounded-md border border-emerald-200 dark:border-emerald-800">
                        {lang === 'ar' ? dom.modulesCoveredAr : dom.modulesCovered}
                      </span>
                    </div>
                    <ul className="space-y-1.5 text-[11px] text-slate-600 dark:text-slate-400">
                      {(lang === 'ar' ? dom.studyTopicsAr : dom.studyTopicsEn).map((topic, tIdx) => (
                        <li key={tIdx} className="flex items-start gap-1.5 leading-snug">
                          <CheckCircle2 size={12} className="text-emerald-500 shrink-0 mt-0.5" />
                          <span>{topic}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <div className="flex flex-wrap sm:flex-nowrap items-center gap-2 pt-3 border-t border-slate-100 dark:border-slate-800">
                  {/* زر المذاكرة Study */}
                  <Link
                    to={`/modules?domain=${dom.domainKey}`}
                    className="flex-1 min-w-[100px] text-center rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-2 text-xs transition-colors shadow-sm flex items-center justify-center gap-1.5"
                    title={lang === 'ar' ? 'فتح الوحدات التعليمية ومسارات التطبيق لهذا المجال' : 'Study modules for this domain'}
                  >
                    <BookOpen size={13} />
                    <span>{lang === 'ar' ? 'المذاكرة (Study)' : 'Study'}</span>
                  </Link>

                  {/* زر أسئلة المجال Practice Questions */}
                  <Link
                    to={`/questions?domain=${encodeURIComponent(dom.id)}`}
                    className="flex-1 min-w-[90px] text-center rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 py-2 text-xs font-semibold text-slate-700 dark:text-slate-300 transition-colors"
                  >
                    {lang === 'ar' ? 'أسئلة المجال' : 'MCQs'}
                  </Link>

                  {/* زر سيناريوهات المجال Scenarios */}
                  <Link
                    to={`/scenarios?domain=${encodeURIComponent(dom.id)}`}
                    className="flex-1 min-w-[90px] text-center rounded-lg bg-sky-50 dark:bg-sky-950/50 hover:bg-sky-100 dark:hover:bg-sky-900/50 py-2 text-xs font-semibold text-sky-700 dark:text-sky-300 transition-colors"
                  >
                    {lang === 'ar' ? 'السيناريوهات' : 'Scenarios'}
                  </Link>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Quick Launch Features */}
      <section className="space-y-4">
        <div>
          <h2 className="text-xl font-bold text-slate-900 dark:text-white">
            {lang === 'ar' ? 'أدوات المنصة التفاعلية' : 'Interactive Preparation Tools'}
          </h2>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            {lang === 'ar'
              ? 'مجموعة متكاملة من الأدوات الدراسية المصممة للتحضير السريع والعميق'
              : 'Complete suite of study aids tailored for quick retention and deep mastery'}
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {quickFeatures.map((feat) => {
            const Icon = feat.icon;
            return (
              <Link
                key={feat.to}
                to={feat.to}
                className="group rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-sm hover:shadow-md hover:border-sky-500 dark:hover:border-sky-500 transition-all flex flex-col justify-between"
              >
                <div>
                  <div className={`w-10 h-10 rounded-xl flex items-center justify-center mb-3 ${feat.color}`}>
                    <Icon size={20} />
                  </div>
                  <h3 className="font-bold text-sm text-slate-900 dark:text-white group-hover:text-sky-600 dark:group-hover:text-sky-400 transition-colors mb-1">
                    {lang === 'ar' ? feat.titleAr : feat.titleEn}
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
                    {lang === 'ar' ? feat.descAr : feat.descEn}
                  </p>
                </div>
                <div className="mt-4 flex items-center gap-1 text-xs font-semibold text-sky-600 dark:text-sky-400">
                  <span>{lang === 'ar' ? 'فتح الأداة' : 'Open'}</span>
                  <ArrowRight size={13} className="group-hover:translate-x-1 transition-transform" />
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      {/* Official Exam Reference Box & Study Guidelines */}
      <section className="rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900/60 p-6 space-y-4">
        <div className="flex items-center justify-between flex-wrap gap-2">
          <div className="flex items-center gap-2">
            <CheckCircle2 size={18} className="text-emerald-500" />
            <h3 className="font-bold text-sm text-slate-900 dark:text-white">
              {lang === 'ar' ? 'معلومات الاختبار الرسمية والتوصيات' : 'Official Exam Specifications & Recommendations'}
            </h3>
          </div>
          <span className="rounded bg-slate-200 dark:bg-slate-800 px-2 py-0.5 text-[11px] font-mono text-slate-700 dark:text-slate-300">
            Exam: EAPA_2025
          </span>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 text-xs">
          <div className="rounded-xl bg-white dark:bg-slate-900 p-3 border border-slate-200 dark:border-slate-800">
            <span className="text-slate-400 block mb-1">{lang === 'ar' ? 'عدد الأسئلة' : 'Question Count'}</span>
            <span className="font-bold text-slate-900 dark:text-white text-sm">75 Multiple Choice</span>
          </div>
          <div className="rounded-xl bg-white dark:bg-slate-900 p-3 border border-slate-200 dark:border-slate-800">
            <span className="text-slate-400 block mb-1">{lang === 'ar' ? 'المدة الزمنية' : 'Duration'}</span>
            <span className="font-bold text-slate-900 dark:text-white text-sm">90 Minutes (1.5h)</span>
          </div>
          <div className="rounded-xl bg-white dark:bg-slate-900 p-3 border border-slate-200 dark:border-slate-800">
            <span className="text-slate-400 block mb-1">{lang === 'ar' ? 'درجة النجاح التقريبية' : 'Passing Score'}</span>
            <span className="font-bold text-emerald-600 dark:text-emerald-400 text-sm">~70% - 75% Scaled</span>
          </div>
          <div className="rounded-xl bg-white dark:bg-slate-900 p-3 border border-slate-200 dark:border-slate-800">
            <span className="text-slate-400 block mb-1">{lang === 'ar' ? 'إصدار البرنامج' : 'Software Version'}</span>
            <span className="font-bold text-slate-900 dark:text-white text-sm">ArcGIS Pro 3.x</span>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-3 pt-2 text-xs text-slate-500 dark:text-slate-400 border-t border-slate-200 dark:border-slate-800">
          <span className="font-semibold text-slate-700 dark:text-slate-300">
            {lang === 'ar' ? 'مراجع Esri المعتمدة:' : 'Official Esri References:'}
          </span>
          <a
            href="https://pro.arcgis.com/en/pro-app/latest/get-started/get-started.html"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-1 hover:text-sky-600 dark:hover:text-sky-400 underline"
          >
            Get Started <ExternalLink size={11} />
          </a>
          <span>•</span>
          <a
            href="https://pro.arcgis.com/en/pro-app/latest/tool-reference/main/arcgis-pro-tool-reference.html"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-1 hover:text-sky-600 dark:hover:text-sky-400 underline"
          >
            Tool Reference <ExternalLink size={11} />
          </a>
          <span>•</span>
          <a
            href="https://pro.arcgis.com/en/pro-app/latest/arcpy/main/arcgis-pro-arcpy-reference.html"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-1 hover:text-sky-600 dark:hover:text-sky-400 underline"
          >
            ArcPy Reference <ExternalLink size={11} />
          </a>
          <span>•</span>
          <a
            href="https://www.esri.com/training/catalog/certification/"
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-1 hover:text-sky-600 dark:hover:text-sky-400 underline"
          >
            Esri Academy Certification <ExternalLink size={11} />
          </a>
        </div>
      </section>
    </div>
  );
}
