import { useState, useEffect, useCallback } from 'react';
import { Shuffle, ArrowLeft, ArrowRight, RotateCw, CheckCircle2, Filter, Sparkles } from 'lucide-react';
import { useI18n } from '../i18n';
import { loadFlashcards } from '../services/content';
import type { Flashcard } from '../types/content';

export default function FlashcardsPage() {
  const { lang } = useI18n();
  const [cards, setCards] = useState<Flashcard[]>([]);
  const [loading, setLoading] = useState(true);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [masteredIds, setMasteredIds] = useState<number[]>(() => {
    try {
      return JSON.parse(localStorage.getItem('eapa.masteredCards') ?? '[]');
    } catch {
      return [];
    }
  });

  useEffect(() => {
    loadFlashcards()
      .then(data => {
        setCards(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  const categories = ['All', ...Array.from(new Set(cards.map(c => c.category)))];

  const filteredCards = selectedCategory === 'All'
    ? cards
    : cards.filter(c => c.category === selectedCategory);

  const currentCard = filteredCards[currentIndex] ?? filteredCards[0];

  const handleNext = useCallback(() => {
    setIsFlipped(false);
    setCurrentIndex(prev => (prev + 1) % filteredCards.length);
  }, [filteredCards.length]);

  const handlePrev = useCallback(() => {
    setIsFlipped(false);
    setCurrentIndex(prev => (prev - 1 + filteredCards.length) % filteredCards.length);
  }, [filteredCards.length]);

  const handleShuffle = () => {
    setIsFlipped(false);
    const shuffled = [...cards].sort(() => Math.random() - 0.5);
    setCards(shuffled);
    setCurrentIndex(0);
  };

  const toggleMastered = (id: number) => {
    const next = masteredIds.includes(id)
      ? masteredIds.filter(m => m !== id)
      : [...masteredIds, id];
    setMasteredIds(next);
    try {
      localStorage.setItem('eapa.masteredCards', JSON.stringify(next));
    } catch {
      // storage unavailable
    }
  };

  // Keyboard navigation
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight' || e.key === 'n') handleNext();
      else if (e.key === 'ArrowLeft' || e.key === 'p') handlePrev();
      else if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        setIsFlipped(f => !f);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [handleNext, handlePrev]);

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <p className="text-slate-500 animate-pulse">{lang === 'ar' ? 'جاري تحميل البطاقات التعليمية (100 بطاقة)...' : 'Loading 100 flashcards...'}</p>
      </div>
    );
  }

  if (!currentCard) {
    return <div className="p-8 text-center text-slate-500">No flashcards found.</div>;
  }

  const isMastered = masteredIds.includes(currentCard.id);

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      {/* Header Banner */}
      <div className="rounded-2xl border border-sky-500/20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 p-6 text-white shadow-xl text-center space-y-2">
        <div className="inline-flex items-center gap-1.5 rounded-full bg-sky-500/20 px-3 py-1 text-xs font-semibold text-sky-300">
          <Sparkles size={14} /> {lang === 'ar' ? 'بنك الحفظ والاسترجاع السريع (100 بطاقة)' : 'Rapid Recall Drill (100 Master Flashcards)'}
        </div>
        <h1 className="text-2xl font-black sm:text-3xl">
          {lang === 'ar' ? 'البطاقات التعليمية التفاعلية' : 'Interactive 3D Flashcards'}
        </h1>
        <p className="text-xs text-slate-300 max-w-xl mx-auto">
          {lang === 'ar'
            ? 'احفظ الفروق بين الامتدادات، وأسماء الأدوات، ودوال Arcade، وقواعد الطوبولوجيا عبر البطاقات القلابة ثلاثية الأبعاد.'
            : 'Memorize tool distinctions, file extensions, Arcade functions, and topology rules with interactive flip cards.'}
        </p>

        {/* Category Filter */}
        <div className="mt-4 flex flex-wrap items-center justify-center gap-2 pt-3 border-t border-slate-700/60">
          <Filter size={14} className="text-slate-400" />
          <select
            value={selectedCategory}
            onChange={e => {
              setSelectedCategory(e.target.value);
              setCurrentIndex(0);
              setIsFlipped(false);
            }}
            className="rounded-xl border border-slate-700 bg-slate-950/80 px-3 py-1.5 text-xs text-white focus:border-sky-500 focus:outline-none"
          >
            {categories.map(cat => (
              <option key={cat} value={cat}>
                {cat === 'All' ? (lang === 'ar' ? 'كافة التصنيفات (100)' : 'All Topics (100)') : cat}
              </option>
            ))}
          </select>
          <span className="text-xs text-slate-400 font-mono">
            {masteredIds.length}/100 {lang === 'ar' ? 'متقنة' : 'mastered'}
          </span>
        </div>
      </div>

      {/* Progress & Counter */}
      <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-2 font-mono">
        <span>
          Card {currentIndex + 1} / {filteredCards.length}
        </span>
        <span className="rounded bg-slate-100 px-2 py-0.5 dark:bg-slate-800">
          {lang === 'ar' ? currentCard.category_ar : currentCard.category}
        </span>
      </div>

      {/* 3D Flashcard Flip Container */}
      <div
        onClick={() => setIsFlipped(!isFlipped)}
        className="group min-h-[300px] sm:min-h-[340px] w-full cursor-pointer perspective-1000 select-none"
      >
        <div
          className={`relative h-full min-h-[300px] sm:min-h-[340px] w-full rounded-3xl border transition-transform duration-500 transform-style-3d shadow-xl p-8 flex flex-col justify-between ${
            isFlipped
              ? 'border-emerald-500/40 bg-gradient-to-br from-slate-900 via-slate-800 to-emerald-950/30'
              : 'border-slate-200 bg-white dark:border-slate-800 dark:bg-gradient-to-br dark:from-slate-900 dark:via-slate-850 dark:to-slate-900'
          }`}
        >
          {/* Top Tag & Flip indicator */}
          <div className="flex items-center justify-between text-xs">
            <span
              className={`rounded-full px-2.5 py-0.5 font-bold uppercase tracking-wider text-[10px] ${
                isFlipped
                  ? 'bg-emerald-500/20 text-emerald-400'
                  : 'bg-sky-500/10 text-sky-600 dark:text-sky-400'
              }`}
            >
              {isFlipped ? (lang === 'ar' ? 'الإجابة والشرح (Answer)' : 'Answer & Rationale') : (lang === 'ar' ? 'السؤال / المفهوم (Prompt)' : 'Question / Prompt')}
            </span>

            <span className="flex items-center gap-1 text-[11px] text-slate-400">
              <RotateCw size={12} className="animate-spin-slow" />
              <span>{lang === 'ar' ? 'انقر للقلب' : 'Click to flip'}</span>
            </span>
          </div>

          {/* Center Card Content */}
          <div className="my-auto py-4 text-center space-y-3">
            <div className="text-base sm:text-xl font-bold leading-relaxed text-slate-900 dark:text-white">
              {isFlipped
                ? (lang === 'ar' ? currentCard.back_ar : currentCard.back_en)
                : (lang === 'ar' ? currentCard.front_ar : currentCard.front_en)}
            </div>

            {/* Bilingual secondary translation */}
            <div className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 font-normal">
              {isFlipped
                ? (lang === 'ar' ? currentCard.back_en : currentCard.back_ar)
                : (lang === 'ar' ? currentCard.front_en : currentCard.front_ar)}
            </div>
          </div>

          {/* Bottom Card Controls */}
          <div className="flex items-center justify-between pt-4 border-t border-slate-100 dark:border-slate-800/60 text-xs">
            <button
              onClick={e => {
                e.stopPropagation();
                toggleMastered(currentCard.id);
              }}
              className={`flex items-center gap-1.5 rounded-lg px-3 py-1.5 font-semibold transition ${
                isMastered
                  ? 'bg-emerald-500 text-slate-950 font-bold'
                  : 'text-slate-400 hover:text-emerald-500 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <CheckCircle2 size={15} />
              <span>{isMastered ? (lang === 'ar' ? 'تم الإتقان' : 'Mastered') : (lang === 'ar' ? 'تحديد كمتقن' : 'Mark Mastered')}</span>
            </button>

            <span className="text-[11px] text-slate-400">
              {lang === 'ar' ? 'مسافة = قلب | أسهم = تنقل' : 'Space: Flip | Arrows: Nav'}
            </span>
          </div>
        </div>
      </div>

      {/* Controls Bar */}
      <div className="flex items-center justify-center gap-4 pt-2">
        <button
          onClick={handlePrev}
          className="flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-xs font-bold text-slate-700 shadow-sm hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-200 dark:hover:bg-slate-800 transition"
        >
          <ArrowLeft size={16} /> {lang === 'ar' ? 'السابق' : 'Previous'}
        </button>

        <button
          onClick={() => setIsFlipped(f => !f)}
          className="flex items-center gap-2 rounded-xl bg-sky-500 px-6 py-2.5 text-xs font-bold text-slate-950 shadow hover:bg-sky-400 transition"
        >
          <RotateCw size={15} /> {lang === 'ar' ? 'اقلب البطاقة' : 'Flip Card'}
        </button>

        <button
          onClick={handleNext}
          className="flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-xs font-bold text-slate-700 shadow-sm hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-200 dark:hover:bg-slate-800 transition"
        >
          {lang === 'ar' ? 'التالي' : 'Next'} <ArrowRight size={16} />
        </button>

        <button
          onClick={handleShuffle}
          className="rounded-xl border border-slate-200 bg-white p-2.5 text-slate-500 shadow-sm hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 transition"
          title="Shuffle cards"
        >
          <Shuffle size={16} />
        </button>
      </div>
    </div>
  );
}

