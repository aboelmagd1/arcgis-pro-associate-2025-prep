import { lazy, Suspense, useState } from 'react';
import { NavLink, Route, Routes } from 'react-router-dom';
import {
  Home,
  Settings as Cog,
  Map,
  Moon,
  Sun,
  ListChecks,
  Timer,
  BarChart3,
  RefreshCw,
  Bookmark,
  BookOpen,
  FolderKanban,
  GitBranch,
  Layers,
  Sparkles,
  Menu,
  X,
  Compass,
} from 'lucide-react';
import { useI18n } from './i18n';

const HomePage = lazy(() => import('./pages/HomePage'));
const Overview = lazy(() => import('./pages/ExamOverview'));
const Bank = lazy(() => import('./pages/QuestionBank'));
const LearningModules = lazy(() => import('./pages/LearningModules'));
const ScenarioLibrary = lazy(() => import('./pages/ScenarioLibrary'));
const WorkflowsPage = lazy(() => import('./pages/WorkflowsPage'));
const FlashcardsPage = lazy(() => import('./pages/FlashcardsPage'));
const ReferencesPage = lazy(() => import('./pages/ReferencesPage'));
const Exam = lazy(() => import('./features/exam/ExamPage'));
const Analytics = lazy(() => import('./features/analytics/AnalyticsPage'));
const Revision = lazy(() => import('./features/analytics/RevisionPage'));
const Bookmarks = lazy(() => import('./features/bookmarks/BookmarksPage'));
const SettingsPage = lazy(() => import('./pages/SettingsPage'));

export default function App() {
  const { t, lang, setLang, theme, setTheme } = useI18n();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navLinkClass = ({ isActive }: { isActive: boolean }) =>
    `flex items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-medium transition-all ${
      isActive
        ? 'bg-sky-600 text-white shadow-sm'
        : 'text-slate-700 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'
    }`;

  const mobileNavLinkClass = ({ isActive }: { isActive: boolean }) =>
    `flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-all ${
      isActive
        ? 'bg-sky-600 text-white shadow-sm'
        : 'text-slate-700 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'
    }`;

  const navItems = [
    { to: '/', label: t('home'), icon: Home },
    { to: '/overview', label: t('overview'), icon: Map },
    { to: '/modules', label: t('modules'), icon: BookOpen },
    { to: '/scenarios', label: t('scenarios'), icon: FolderKanban },
    { to: '/workflows', label: t('workflows'), icon: GitBranch },
    { to: '/questions', label: t('bank'), icon: ListChecks },
    { to: '/flashcards', label: t('flashcards'), icon: Layers },
    { to: '/references', label: t('references'), icon: Compass },
    { to: '/exam', label: t('exam'), icon: Timer, highlight: true },
    { to: '/analytics', label: t('analytics'), icon: BarChart3 },
    { to: '/revision', label: t('revision'), icon: RefreshCw },
    { to: '/bookmarks', label: t('bookmarks'), icon: Bookmark },
  ];

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100 flex flex-col font-sans">
      {/* Top Navbar */}
      <header className="sticky top-0 z-40 border-b border-slate-200 bg-white/95 backdrop-blur-md dark:border-slate-800 dark:bg-slate-900/95 shadow-sm">
        <div className="mx-auto flex max-w-7xl items-center justify-between gap-3 px-4 py-2.5">
          {/* Logo / Brand */}
          <NavLink to="/" className="flex items-center gap-2 group flex-shrink-0">
            <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-sky-600 text-white shadow-sm group-hover:bg-sky-500 transition-colors">
              <Sparkles size={18} />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-sm tracking-tight text-slate-900 dark:text-white">
                  {lang === 'ar' ? 'محترف آرك جي آي إس برو' : 'ArcGIS Pro Associate'}
                </span>
                <span className="rounded bg-sky-100 px-1.5 py-0.5 text-[10px] font-bold text-sky-800 dark:bg-sky-900/60 dark:text-sky-300">
                  2025
                </span>
              </div>
              <p className="text-[10px] text-slate-500 dark:text-slate-400">
                {lang === 'ar' ? 'منصة التحضير المعتمدة EAPA_2025' : 'Official EAPA_2025 Prep Suite'}
              </p>
            </div>
          </NavLink>

          {/* Desktop Navigation Links */}
          <nav className="hidden xl:flex items-center gap-1 overflow-x-auto py-1" aria-label="Main Navigation">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === '/'}
                  className={navLinkClass}
                >
                  <Icon size={14} />
                  <span>{item.label}</span>
                </NavLink>
              );
            })}
          </nav>

          {/* Controls & Quick Action */}
          <div className="flex items-center gap-1.5 flex-shrink-0">
            <NavLink
              to="/exam?preset=eapa75"
              className="hidden sm:inline-flex items-center gap-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold px-2.5 py-1.5 text-xs shadow-sm transition-colors"
              title={lang === 'ar' ? 'بدء محاكي 75 سؤال / 90 دقيقة' : 'Start 75Q / 90m Simulation'}
            >
              <Timer size={14} />
              <span>{lang === 'ar' ? 'بدء الاختبار (75Q)' : 'Simulate 75Q'}</span>
            </NavLink>

            {/* Language Toggle */}
            <button
              onClick={() => setLang(lang === 'en' ? 'ar' : 'en')}
              className="flex items-center gap-1 rounded-lg border border-slate-300 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 px-2 py-1.5 text-xs font-semibold hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors"
              aria-label={t('lang')}
              title={lang === 'en' ? 'التبديل إلى العربية' : 'Switch to English'}
            >
              <span className="text-sky-600 dark:text-sky-400 font-bold">
                {lang === 'en' ? 'عربي' : 'EN'}
              </span>
            </button>

            {/* Theme Toggle */}
            <button
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
              className="rounded-lg border border-slate-300 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 p-1.5 text-slate-700 hover:bg-slate-200 dark:text-slate-300 dark:hover:bg-slate-700 transition-colors"
              aria-label={t('theme')}
            >
              {theme === 'dark' ? <Sun size={15} /> : <Moon size={15} />}
            </button>

            {/* Settings */}
            <NavLink
              to="/settings"
              className={({ isActive }) =>
                `rounded-lg p-1.5 transition-colors ${
                  isActive
                    ? 'bg-sky-600 text-white'
                    : 'text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'
                }`
              }
              title={t('settings')}
            >
              <Cog size={16} />
            </NavLink>

            {/* Mobile Menu Button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="xl:hidden rounded-lg p-1.5 text-slate-700 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800"
              aria-label="Toggle Navigation Menu"
            >
              {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
            </button>
          </div>
        </div>

        {/* Secondary Sub-nav for medium screens */}
        <div className="hidden md:flex xl:hidden border-t border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-900/80 px-4 py-1.5 overflow-x-auto gap-1">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink
                key={item.to}
                to={item.to}
                end={item.to === '/'}
                className={navLinkClass}
              >
                <Icon size={13} />
                <span className="whitespace-nowrap">{item.label}</span>
              </NavLink>
            );
          })}
        </div>

        {/* Mobile Dropdown Menu */}
        {mobileMenuOpen && (
          <div className="xl:hidden border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 space-y-1 shadow-lg max-h-[80vh] overflow-y-auto">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === '/'}
                  onClick={() => setMobileMenuOpen(false)}
                  className={mobileNavLinkClass}
                >
                  <Icon size={18} />
                  <span>{item.label}</span>
                </NavLink>
              );
            })}
          </div>
        )}
      </header>

      {/* Main Content Area */}
      <main className="mx-auto w-full max-w-7xl flex-1 p-4 md:p-6">
        <Suspense
          fallback={
            <div className="flex h-64 items-center justify-center">
              <div className="flex items-center gap-3 text-slate-500 dark:text-slate-400">
                <div className="h-6 w-6 animate-spin rounded-full border-2 border-sky-500 border-t-transparent" />
                <span className="text-sm font-medium">
                  {lang === 'ar' ? 'جارٍ تحميل المحتوى...' : 'Loading content...'}
                </span>
              </div>
            </div>
          }
        >
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/overview" element={<Overview />} />
            <Route path="/modules" element={<LearningModules />} />
            <Route path="/questions" element={<Bank />} />
            <Route path="/scenarios" element={<ScenarioLibrary />} />
            <Route path="/workflows" element={<WorkflowsPage />} />
            <Route path="/flashcards" element={<FlashcardsPage />} />
            <Route path="/references" element={<ReferencesPage />} />
            <Route path="/exam" element={<Exam />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/revision" element={<Revision />} />
            <Route path="/bookmarks" element={<Bookmarks />} />
            <Route path="/settings" element={<SettingsPage />} />
            <Route path="*" element={<HomePage />} />
          </Routes>
        </Suspense>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-200 bg-white py-6 dark:border-slate-800 dark:bg-slate-900/50 mt-auto">
        <div className="mx-auto max-w-7xl px-4 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-500 dark:text-slate-400">
          <div className="flex items-center gap-2">
            <span className="font-semibold text-slate-700 dark:text-slate-300">
              ArcGIS Pro Associate 2025 (EAPA_2025)
            </span>
            <span>•</span>
            <span>{t('disclaimer')}</span>
          </div>
          <div className="flex items-center gap-4">
            <a
              href="https://pro.arcgis.com"
              target="_blank"
              rel="noreferrer"
              className="hover:text-sky-600 dark:hover:text-sky-400 transition-colors"
            >
              Esri ArcGIS Pro Docs
            </a>
            <span>•</span>
            <a
              href="https://www.esri.com/training/catalog/certification/"
              target="_blank"
              rel="noreferrer"
              className="hover:text-sky-600 dark:hover:text-sky-400 transition-colors"
            >
              Esri Academy
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
