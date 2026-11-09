import { useI18n } from '../i18n';
// Source: official Esri EAPA 2025 Exam Information Guide (see docs/EXAM_BLUEPRINT.md)
const domains = [
  { n: 'Data Management', ar: 'إدارة البيانات', w: 32 },
  { n: 'Visualization', ar: 'التصور', w: 25 },
  { n: 'Analysis and Geoprocessing', ar: 'التحليل والمعالجة الجغرافية', w: 25 },
  { n: 'Layouts and Sharing', ar: 'التخطيطات والمشاركة', w: 18 },
];
export default function ExamOverview() {
  const { t, lang } = useI18n();
  return (<div className="space-y-4">
    <h1 className="text-2xl font-bold">{t('overview')}</h1>
    <dl className="grid grid-cols-2 gap-2 sm:grid-cols-4">
      {[[t('questions'), '75'], [t('duration'), '90 min'], [t('format'), 'MCQ'], [t('version'), 'ArcGIS Pro 3.3']].map(([k, v]) =>
        <div key={k} className="rounded border bg-white p-3 dark:border-slate-700 dark:bg-slate-800"><dt className="text-xs text-slate-500">{k}</dt><dd className="font-semibold">{v}</dd></div>)}
    </dl>
    <ul className="space-y-2">{domains.map(d => (
      <li key={d.n} className="rounded border bg-white p-3 dark:border-slate-700 dark:bg-slate-800">
        <div className="flex justify-between"><span>{lang === 'ar' ? d.ar : d.n}</span><span>{d.w}%</span></div>
        <div className="mt-2 h-2 rounded bg-slate-200 dark:bg-slate-700"><div className="h-2 rounded bg-teal-600" style={{ width: `${d.w * 3}%` }} /></div>
      </li>))}</ul>
  </div>);
}
