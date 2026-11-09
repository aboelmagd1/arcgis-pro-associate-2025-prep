import { createContext, useContext, useEffect, useState, type ReactNode } from 'react';
import { loadPrefs, savePrefs, type Prefs } from '../storage/store';
import type { Lang } from '../types/content';

const dict = {
  en: {
    app: 'ArcGIS Pro Associate 2025',
    home: 'Home',
    overview: 'Exam Blueprint',
    modules: 'Learning Modules',
    bank: 'Question Bank',
    scenarios: 'Scenario Library',
    workflows: 'Workflows',
    flashcards: 'Flashcards',
    references: 'Reference Hub',
    exam: 'Exam Simulator',
    analytics: 'Analytics',
    revision: 'Smart Revision',
    bookmarks: 'Bookmarks',
    settings: 'Settings',
    lang: 'Language',
    theme: 'Theme',
    export: 'Export progress (JSON)',
    import: 'Import progress',
    reset: 'Reset local progress',
    resetConfirm: 'Delete all locally stored progress? This cannot be undone.',
    imported: 'Progress imported.',
    importFail: 'Import failed: the file is not valid exported progress.',
    storageNote: 'Progress is stored in this browser on this device only. Export it to move it elsewhere; it never syncs automatically.',
    disclaimer: 'Independent study aid for Esri ArcGIS Pro Associate 2025 (EAPA_2025). Not affiliated with Esri; not real exam questions; no pass guarantee.',
    status: 'Ready for Exam Preparation',
    statusBody: 'Complete 2025 preparation suite active: 250 verified MCQs, 150 real-world scenarios, 30 practical workflows, 12 learning modules, 100 flashcards, and top 52 data management tools.',
    homeTitle: 'Esri ArcGIS Pro Associate 2025 (EAPA_2025) Master Preparation Platform',
    bankNote: 'Browse mode (answers revealed on demand). Questions loaded',
    loadFail: 'Could not load the question file.',
    empty: 'No questions available yet.',
    difficulty: 'Difficulty',
    all: 'All',
    show: 'Show answer',
    bookmark: 'Bookmark',
    hide: 'Hide answer',
    questions: 'Questions',
    duration: 'Duration',
    format: 'Format',
    version: 'Software',
  },
  ar: {
    app: 'محترف ArcGIS Pro 2025',
    home: 'الرئيسية',
    overview: 'مخطط الاختبار',
    modules: 'الوحدات التعليمية',
    bank: 'بنك الأسئلة',
    scenarios: 'مكتبة السيناريوهات',
    workflows: 'سير العمل التطبيقي',
    flashcards: 'البطاقات التعليمية',
    references: 'مركز المراجع',
    exam: 'محاكي الاختبار',
    analytics: 'التحليلات',
    revision: 'المراجعة الذكية',
    bookmarks: 'المفضلة',
    settings: 'الإعدادات',
    lang: 'اللغة',
    theme: 'المظهر',
    export: 'تصدير التقدم (JSON)',
    import: 'استيراد التقدم',
    reset: 'مسح التقدم المحلي',
    resetConfirm: 'هل تريد حذف كل التقدم المخزن محلياً؟ لا يمكن التراجع عن ذلك.',
    imported: 'تم استيراد التقدم.',
    importFail: 'فشل الاستيراد: الملف ليس تقدماً مصدّراً صالحاً.',
    storageNote: 'يُخزَّن التقدم في هذا المتصفح وعلى هذا الجهاز فقط. صدّره لنقله إلى مكان آخر؛ لا تتم المزامنة تلقائياً.',
    disclaimer: 'أداة دراسة مستقلة لاختبار Esri ArcGIS Pro Associate 2025 (EAPA_2025). غير تابعة لشركة Esri؛ ليست أسئلة الاختبار الحقيقية؛ لا ضمان للنجاح.',
    status: 'جاهز للتحضير للاختبار',
    statusBody: 'المنصة المتكاملة لعام 2025 نشطة: 250 سؤال اختيار من متعدد، 150 سيناريو عملي، 30 سير عمل تطبيقي، 12 وحدة تعليمية، 100 بطاقة تعليمية، ودليل أهم 52 أداة لإدارة البيانات.',
    homeTitle: 'المنصة الشاملة للتحضير لشهادة Esri ArcGIS Pro Associate 2025 (EAPA_2025)',
    bankNote: 'وضع التصفح (تظهر الإجابات عند الطلب). عدد الأسئلة المحمّلة',
    loadFail: 'تعذر تحميل ملف الأسئلة.',
    empty: 'لا توجد أسئلة متاحة بعد.',
    difficulty: 'مستوى الصعوبة',
    all: 'الكل',
    show: 'إظهار الإجابة',
    bookmark: 'إضافة إلى المفضلة',
    hide: 'إخفاء الإجابة',
    questions: 'الأسئلة',
    duration: 'المدة',
    format: 'الصيغة',
    version: 'البرنامج',
  },
};
export type Key = keyof typeof dict.en;
interface Ctx extends Prefs { t: (k: Key) => string; setLang: (l: Lang) => void; setTheme: (t: Prefs['theme']) => void; }
const C = createContext<Ctx>(null!);
export const useI18n = () => useContext(C);

export function I18nProvider({ children }: { children: ReactNode }) {
  const [p, setP] = useState<Prefs>(loadPrefs);
  useEffect(() => {
    document.documentElement.lang = p.lang; document.documentElement.dir = p.lang === 'ar' ? 'rtl' : 'ltr';
    document.documentElement.classList.toggle('dark', p.theme === 'dark'); savePrefs(p);
  }, [p]);
  return <C.Provider value={{ ...p, t: k => dict[p.lang][k], setLang: lang => setP({ ...p, lang }), setTheme: theme => setP({ ...p, theme }) }}>{children}</C.Provider>;
}
