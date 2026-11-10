export type Lang = 'en' | 'ar';
export type L10n = Record<Lang, string>;
export const DOMAINS = ['Data Management','Visualization','Analysis and Geoprocessing','Layouts and Sharing'] as const;
export type Domain = typeof DOMAINS[number];
export const DIFFICULTIES = ['Beginner','Intermediate','Advanced'] as const;
export type Difficulty = typeof DIFFICULTIES[number];
export const QTYPES = ['Conceptual','Technical','Tool-based','Workflow-based','Troubleshooting','Best-practice'] as const;
export type QType = typeof QTYPES[number];
export type OptionId = 'A'|'B'|'C'|'D';

export interface Reference { title: string; url: string; kind: 'official' | 'original' | 'unverified'; }
export interface Option { id: OptionId; text: L10n; }

/** Shared by MCQs and scenarios. Scenarios add `context`. */
export interface Question {
  id: string;                    // e.g. DM-001, DM-S-001
  kind: 'mcq' | 'scenario';
  domain: Domain;
  objective: string;             // must match an official objective in docs/EXAM_BLUEPRINT.md
  difficulty: Difficulty;
  type: QType;
  tools: string[];
  context?: L10n;                // required when kind === 'scenario'
  question: L10n;
  options: [Option, Option, Option, Option];
  correctAnswer: OptionId;
  explanation: L10n;
  incorrectOptionsExplanation: Record<Lang, Partial<Record<OptionId, string>>>;
  references: Reference[];
}

export interface AttemptAnswer { questionId: string; selected: OptionId | null; correct: boolean; flagged: boolean; ms: number; }
export interface ExamAttempt { id: string; startedAt: string; finishedAt: string; mode: string; timed: boolean; answers: AttemptAnswer[]; }
export interface RevisionRecord { questionId: string; box: number; dueAt: string; lastResult: boolean; }
export interface UserProgress {
  version: 1; bookmarks: string[]; flagged: string[]; completedModules: string[];
  attempts: ExamAttempt[]; revision: RevisionRecord[];
}
export const emptyProgress = (): UserProgress => ({ version: 1, bookmarks: [], flagged: [], completedModules: [], attempts: [], revision: [] });

export interface WorkflowStep {
  stepNumber: number;
  title: L10n;
  instruction: L10n;
  uiPath: string;
  tool: string;
  parameters: Record<string, string>;
}

export interface Workflow {
  id: string;
  domain: Domain;
  difficulty: Difficulty;
  tools: string[];
  relatedObjectives: string[];
  references: Reference[];
  title: L10n;
  objective: L10n;
  initialData: L10n;
  startingConditions: L10n;
  steps: WorkflowStep[];
  expectedOutput: L10n;
  qualityControl: L10n;
  commonMistakes: L10n;
  alternativeApproaches: L10n;
}

export interface ComparisonTable {
  title_en: string;
  title_ar: string;
  headers_en: string[];
  headers_ar: string[];
  rows_en: string[][];
  rows_ar: string[][];
}

export interface UiPathItem {
  label_en: string;
  label_ar: string;
  path: string;
}

export interface LearningModule {
  id: string;
  week: number;
  domain: string;
  domainTitle_en: string;
  domainTitle_ar: string;
  title_en: string;
  title_ar: string;
  summary_en: string;
  summary_ar: string;
  ui_paths: Array<string | UiPathItem>;
  key_concepts_en: string[];
  key_concepts_ar: string[];
  key_concepts_refs?: Array<{ title_en: string; title_ar: string; url: string }>;
  comparison_table?: ComparisonTable;
  flashcards?: Array<{ q_en: string; a_en: string; q_ar: string; a_ar: string }>;
  lab_checklist: Array<{ id?: string; task_en: string; task_ar: string }>;
  doc_hubs?: Reference[];
}

export interface ToolComparison {
  id: string;
  title: L10n;
  domain: string;
  toolA: { name: string; syntax: string };
  toolB: { name: string; syntax: string };
  keyDifference: L10n;
  useCaseA: L10n;
  useCaseB: L10n;
  examTrap?: L10n;
}

export interface TroubleshootingGuide {
  id: string;
  title: L10n;
  domain: string;
  symptom: L10n;
  rootCause: L10n;
  resolutionSteps: Array<{ step: number; text: L10n }>;
  preventionTip: L10n;
}

export interface Flashcard {
  id: number;
  category: string;
  category_ar: string;
  front_en: string;
  front_ar: string;
  back_en: string;
  back_ar: string;
}

export interface DataManagementTool {
  id: string;
  category: string;
  name: string;
  name_ar: string;
  doc_url: string;
  arcpy_syntax: string;
  ui_path: string;
  description: L10n;
  exam_trap: L10n;
}

export interface StudyPlannerDay {
  day: number;
  task: L10n;
}

export interface StudyPlannerWeek {
  weekNumber: number;
  domain: string;
  title: L10n;
  focusModules: string[];
  targetWorkflows: string[];
  dailyTasks: StudyPlannerDay[];
}

export interface StudyPlanner {
  title: L10n;
  examOverview: {
    code: string;
    title: string;
    questions: number;
    timeMinutes: number;
    passingScore: string;
    domainWeights: Record<string, number>;
  };
  weeks: StudyPlannerWeek[];
}

