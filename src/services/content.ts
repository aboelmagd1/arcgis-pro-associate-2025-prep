import type {
  Question,
  Workflow,
  LearningModule,
  ToolComparison,
  TroubleshootingGuide,
  Flashcard,
  DataManagementTool,
  StudyPlanner
} from '../types/content';

const url = (p: string) => `${import.meta.env.BASE_URL}data/${p}`;

/** Lazy-loads one question file. Throws a user-presentable Error on failure. */
export async function loadQuestions(file: string): Promise<Question[]> {
  const res = await fetch(url(`questions/${file}.json`));
  if (!res.ok) throw new Error(`missing-file:${file}`);
  const data = await res.json();
  if (!Array.isArray(data)) throw new Error(`invalid-file:${file}`);
  return data.filter(isValidQuestion);
}

export function isValidQuestion(q: any): q is Question {
  return !!q && typeof q.id === 'string' && q.options?.length === 4
    && ['A','B','C','D'].includes(q.correctAnswer) && !!q.question?.en && !!q.question?.ar;
}

export const QUESTION_FILES = ['data-management', 'visualization', 'analysis-geoprocessing', 'layouts-sharing'];

/** Loads every question file; a missing file is skipped, but all-missing is an error. */
export async function loadAllQuestions(): Promise<Question[]> {
  const r = await Promise.allSettled(QUESTION_FILES.map(loadQuestions));
  const ok = r.filter((x): x is PromiseFulfilledResult<Question[]> => x.status === 'fulfilled');
  if (!ok.length) throw new Error('no-question-files');
  return ok.flatMap(x => x.value);
}

/** Lazy-loads one scenario file. */
export async function loadScenarios(file: string): Promise<Question[]> {
  const res = await fetch(url(`scenarios/${file}.json`));
  if (!res.ok) throw new Error(`missing-scenario-file:${file}`);
  const data = await res.json();
  if (!Array.isArray(data)) throw new Error(`invalid-scenario-file:${file}`);
  return data.filter(isValidQuestion);
}

/** Loads all 150 scenario questions across the 4 domains. */
export async function loadAllScenarios(): Promise<Question[]> {
  const r = await Promise.allSettled(QUESTION_FILES.map(loadScenarios));
  const ok = r.filter((x): x is PromiseFulfilledResult<Question[]> => x.status === 'fulfilled');
  if (!ok.length) throw new Error('no-scenario-files');
  return ok.flatMap(x => x.value);
}

/** Loads combined MCQs and Scenarios (400 items total). */
export async function loadAllQuestionsAndScenarios(): Promise<Question[]> {
  const [questions, scenarios] = await Promise.all([loadAllQuestions(), loadAllScenarios()]);
  return [...questions, ...scenarios];
}

/** Loads the 30 practical GIS workflows. */
export async function loadWorkflows(): Promise<Workflow[]> {
  const res = await fetch(url('workflows/workflows.json'));
  if (!res.ok) throw new Error('missing-workflows');
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Loads the 12 structured learning modules. */
export async function loadModules(): Promise<LearningModule[]> {
  const res = await fetch(url('modules/modules.json'));
  if (!res.ok) throw new Error('missing-modules');
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Loads all 100 flashcards. */
export async function loadFlashcards(): Promise<Flashcard[]> {
  const res = await fetch(url('references/flashcards.json'));
  if (!res.ok) throw new Error('missing-flashcards');
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Loads the 12 tool comparison pairs. */
export async function loadToolComparisons(): Promise<ToolComparison[]> {
  const res = await fetch(url('references/tool-comparisons.json'));
  if (!res.ok) throw new Error('missing-tool-comparisons');
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Loads the 12 GIS troubleshooting guides. */
export async function loadTroubleshooting(): Promise<TroubleshootingGuide[]> {
  const res = await fetch(url('references/troubleshooting.json'));
  if (!res.ok) throw new Error('missing-troubleshooting');
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Loads the top 52 Data Management tools encyclopedia. */
export async function loadDataManagementTools(): Promise<DataManagementTool[]> {
  const res = await fetch(url('references/data-management-tools.json'));
  if (!res.ok) throw new Error('missing-data-management-tools');
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Loads the 4-week study planner. */
export async function loadStudyPlanner(): Promise<StudyPlanner> {
  const res = await fetch(url('references/study-planner.json'));
  if (!res.ok) throw new Error('missing-study-planner');
  return res.json();
}
