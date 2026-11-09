import { useRef, useState } from 'react';
import { useI18n } from '../i18n';
import { exportProgress, importProgress, resetProgress } from '../storage/store';

export default function SettingsPage() {
  const { t } = useI18n(); const file = useRef<HTMLInputElement>(null); const [msg, setMsg] = useState('');
  const download = () => { const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([exportProgress()], { type: 'application/json' })); a.download = 'eapa-progress.json'; a.click(); };
  const onImport = async (f?: File) => { if (!f) return;
    try { importProgress(await f.text()); setMsg(t('imported')); } catch { setMsg(t('importFail')); } };
  const btn = 'rounded border px-3 py-2 text-sm';
  return (<div className="space-y-4">
    <h1 className="text-2xl font-bold">{t('settings')}</h1>
    <p className="text-sm">{t('storageNote')}</p>
    <div className="flex flex-wrap gap-2">
      <button className={btn} onClick={download}>{t('export')}</button>
      <button className={btn} onClick={() => file.current?.click()}>{t('import')}</button>
      <button className={`${btn} border-red-500 text-red-600`} onClick={() => { if (confirm(t('resetConfirm'))) resetProgress(); }}>{t('reset')}</button>
      <input ref={file} type="file" accept="application/json" hidden onChange={e => onImport(e.target.files?.[0])} />
    </div>
    <p role="status">{msg}</p>
  </div>);
}
