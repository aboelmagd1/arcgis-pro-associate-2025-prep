import { emptyProgress, type UserProgress, type Lang } from '../types/content';

const PREFS = 'eapa.prefs', PROG = 'eapa.progress';
export interface Prefs { lang: Lang; theme: 'light' | 'dark'; }

export function loadPrefs(): Prefs {
  try {
    const p = JSON.parse(localStorage.getItem(PREFS) ?? '');
    if (p && (p.lang === 'en' || p.lang === 'ar')) return { lang: p.lang, theme: p.theme === 'dark' ? 'dark' : 'light' };
  } catch { /* fall through to defaults */ }
  return { lang: 'en', theme: 'light' };
}
export function savePrefs(p: Prefs) { try { localStorage.setItem(PREFS, JSON.stringify(p)); } catch { /* storage unavailable */ } }

/** Never silently discards data: a corrupted blob is kept under a backup key. */
export function loadProgress(): UserProgress {
  const raw = localStorage.getItem(PROG);
  if (!raw) return emptyProgress();
  try { const p = JSON.parse(raw); if (validateProgress(p)) return p; throw new Error('shape'); }
  catch { localStorage.setItem(PROG + '.corrupt.' + Date.now(), raw); return emptyProgress(); }
}
export const saveProgress = (p: UserProgress) => localStorage.setItem(PROG, JSON.stringify(p));
export const resetProgress = () => localStorage.removeItem(PROG);

export function validateProgress(p: any): p is UserProgress {
  return !!p && p.version === 1 && ['bookmarks','flagged','completedModules','attempts','revision'].every(k => Array.isArray(p[k]));
}
export function exportProgress(): string { return JSON.stringify(loadProgress(), null, 2); }
export function importProgress(text: string): UserProgress {
  let p: unknown; try { p = JSON.parse(text); } catch { throw new Error('invalid-json'); }
  if (!validateProgress(p)) throw new Error('invalid-progress');
  saveProgress(p); return p;
}

import { toggleId } from '../features/bookmarks/logic';
/** Toggles a bookmark in saved progress and returns the new list. */
export function toggleBookmark(id: string): string[] {
  const p = loadProgress(); p.bookmarks = toggleId(p.bookmarks, id);
  try { saveProgress(p); } catch { /* storage full or unavailable */ }
  return p.bookmarks;
}
