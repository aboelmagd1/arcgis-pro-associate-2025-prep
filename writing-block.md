# MASTER PROMPT
# ArcGIS Pro Associate 2025 – Professional Exam Preparation & Simulation Platform

## 1. ROLE AND MISSION

Act as a Senior Frontend Architect, GIS Technical Expert, ArcGIS Pro Instructor, Educational Content Designer, UX/UI Designer, and Quality Assurance Engineer.

Your mission is to research, design, develop, test, and deliver a complete professional bilingual learning and examination platform for:

**Esri ArcGIS Pro Associate 2025 Certification – Exam Code: EAPA_2025**

The platform must help candidates prepare comprehensively for the certification through:

- Structured learning modules.
- A minimum of 250 original multiple-choice questions.
- A minimum of 150 independent scenario-based questions.
- Practical GIS workflow challenges.
- Realistic examination simulations.
- Detailed bilingual explanations.
- Personalized performance analytics.
- Intelligent revision and weak-topic identification.

This must be a fully functional educational platform, not merely a static collection of questions.

The final product must be production-ready and deployable directly through GitHub Pages.

---

# 2. CRITICAL ARCHITECTURE REQUIREMENTS

## GitHub Pages First – Static Architecture Only

The website will be hosted using GitHub Pages.

Design the entire application around static hosting limitations.

**Mandatory restrictions:**

- No traditional backend.
- No Node.js server running in production.
- No Python server.
- No PHP.
- No database server.
- No server-side rendering requirement.
- No API server dependency.
- No authentication server.
- No cloud database.
- No paid third-party services required for core functionality.
- No external API calls required for normal website operation.

The application must work as a static website consisting of HTML, CSS, JavaScript, and static data files.

### Recommended Technology Stack

Use a lightweight, maintainable frontend architecture.

Preferred stack:

- React.
- TypeScript.
- Vite.
- Tailwind CSS.
- Lucide Icons.
- Recharts only where analytics genuinely require charts.

Do not add libraries without a clear technical reason.

Avoid unnecessary dependencies and oversized UI frameworks.

If a simpler implementation achieves the same result with better performance, prefer the simpler implementation.

### Data Architecture

Store the educational content separately from the application logic.

Recommended structure:

- Static JSON files for questions.
- Static JSON files for scenarios.
- Static JSON files for learning modules.
- Static JSON files for GIS workflows.
- Static JSON files for references and metadata.

Use modular data files instead of one enormous JSON file.

Implement lazy loading or dynamic imports for large question collections when appropriate.

The website should not load all explanations, images, and question data unnecessarily on the initial page load.

### Local Persistence

Use browser-side storage:

- IndexedDB for larger learning datasets, progress records, and examination history.
- LocalStorage for lightweight preferences such as theme and language.

Persist:

- User progress.
- Completed modules.
- Examination results.
- Incorrect answers.
- Bookmarked questions.
- Flagged questions.
- Learning preferences.
- Revision history.

The website must remain functional without creating a user account.

Provide:

- Export progress as JSON.
- Import previously exported progress.
- Reset local progress with confirmation.

Clearly explain that locally stored progress belongs to the current browser/device unless exported and transferred.

Do not claim that user data synchronizes automatically between devices.

### GitHub Pages Deployment

The project must be compatible with GitHub Pages from the beginning.

Requirements:

1. Configure Vite with a configurable `base` path.
2. Support deployment through GitHub Actions.
3. Include a complete `.github/workflows/deploy.yml`.
4. Include a GitHub Pages deployment guide.
5. Ensure all static asset paths work under repository subpaths.
6. Avoid absolute paths that break after deployment.
7. Support direct navigation and page refresh.
8. Prefer hash-based routing if it avoids GitHub Pages routing problems.
9. Do not require custom server rewrite rules.
10. Do not expose secrets, API keys, or credentials.

Provide a clear configuration option for:

- Local development.
- GitHub Pages production deployment.

The project must build successfully using:

`npm run build`

The final build output must be deployable through GitHub Pages without a backend.

---

# 3. OFFICIAL EXAM RESEARCH AND VALIDATION

Before creating educational content, research the official Esri certification information.

Target certification:

**ArcGIS Pro Associate 2025 – EAPA_2025**

Prioritize:

1. Official Esri certification pages.
2. Official exam information and exam objectives.
3. Official Esri learning resources.
4. ArcGIS Pro documentation.
5. Esri training courses.
6. Official Esri tutorials and workflow documentation.

Verify:

- Official exam objectives.
- Exam domains.
- Domain weightings, if officially published.
- Required knowledge and skills.
- Relevant ArcGIS Pro functionality.
- Officially documented terminology.
- Relevant software version information.

Do not invent official requirements.

Do not present unofficial exam information as an official Esri statement.

Create:

`docs/EXAM_BLUEPRINT.md`

This document must contain:

- Verified exam information.
- Official exam objectives.
- Domain structure.
- Official references.
- Research dates.
- Unverified or unavailable information clearly marked.

If a particular exam detail cannot be verified, explicitly state that it is unverified.

All learning content must align with the verified exam objectives.

---

# 4. EDUCATIONAL CONTENT REQUIREMENTS

## A. Multiple-Choice Question Bank

Create at least:

**250 original multiple-choice questions.**

Questions must cover all verified examination objectives.

Use the official domain distribution where available.

If official percentages are available, allocate questions proportionally.

If not, create a balanced distribution and clearly label it as an educational allocation rather than an official exam distribution.

Initial planning targets:

| Domain | Target Questions |
|---|---:|
| Data Management | 80 |
| Visualization | 60 |
| Analysis & Geoprocessing | 65 |
| Layouts & Sharing | 45 |
| Total | 250 |

These are planning targets, not verified official exam weights. Adjust them if the official blueprint indicates a different structure.

### Every question must include:

- Unique question ID.
- English question.
- Arabic translation.
- Four answer options.
- Correct answer.
- English explanation.
- Arabic explanation.
- Explanation of why the other options are incorrect.
- Domain.
- Related exam objective.
- Difficulty level.
- Question type.
- Relevant ArcGIS Pro tool or functionality.
- Official documentation reference.

Difficulty levels:

- Beginner.
- Intermediate.
- Advanced.

Question types:

- Conceptual.
- Technical.
- Tool-based.
- Workflow-based.
- Troubleshooting.
- Best-practice.

### Content Quality Rules

- Questions must be original.
- Do not copy copyrighted exam questions.
- Do not use leaked exam dumps.
- Do not claim that practice questions are actual Esri examination questions.
- Avoid repetitive questions.
- Avoid questions with ambiguous answers.
- Avoid outdated ArcGIS Pro functionality.
- Validate every correct answer against reliable documentation.

---

## B. Scenario-Based Question Bank

Create at least:

**150 independent scenario-based questions.**

These must be realistic GIS situations requiring technical reasoning and decision-making.

They must not simply be rewritten versions of the 250 conceptual questions.

Initial planning targets:

| Domain | Scenario Questions |
|---|---:|
| Data Management | 40 |
| Visualization | 35 |
| Analysis & Geoprocessing | 45 |
| Layouts & Sharing | 30 |
| Total | 150 |

Each scenario must include:

1. A realistic professional GIS situation.
2. A clear technical problem.
3. Relevant project context.
4. Four possible solutions.
5. One best answer.
6. Detailed reasoning.
7. Explanation of incorrect approaches.
8. English and Arabic versions.
9. Related exam objective.
10. Relevant ArcGIS Pro tools.
11. Difficulty classification.
12. Reference documentation.

### Scenario Examples

Develop scenarios involving:

- Invalid geometries.
- Coordinate system mismatches.
- Geodatabase design.
- Attribute domains.
- Subtypes.
- Topology validation.
- Editing workflows.
- Spatial selection.
- Raster analysis.
- Feature overlay.
- Geoprocessing environments.
- ModelBuilder.
- Cartographic representation.
- Label conflicts.
- Map series.
- Layout exports.
- Sharing web layers.
- Data accessibility.
- Performance troubleshooting.

Prioritize situations where candidates must select the correct tool, workflow, configuration, or troubleshooting method.

---

# 5. PRACTICAL GIS WORKFLOW CHALLENGES

Create at least 30 practical GIS workflow challenges.

These are educational walkthroughs, not just MCQs.

Each workflow must include:

- Objective.
- Initial data requirements.
- Starting conditions.
- Step-by-step ArcGIS Pro instructions.
- Relevant tools.
- Important parameters.
- Expected output.
- Quality control checks.
- Common mistakes.
- Alternative approaches where relevant.
- Related examination objectives.
- English and Arabic explanations.

Examples:

1. Create and configure a file geodatabase.
2. Import and organize spatial datasets.
3. Define coordinate systems.
4. Project datasets correctly.
5. Configure domains and subtypes.
6. Validate topology.
7. Edit feature geometries.
8. Apply attribute rules where appropriate.
9. Perform spatial joins.
10. Execute overlay analysis.
11. Run buffer analysis.
12. Perform raster calculations.
13. Configure geoprocessing environments.
14. Build a ModelBuilder workflow.
15. Create effective map symbology.
16. Configure labeling.
17. Resolve label conflicts.
18. Create professional layouts.
19. Configure map series.
20. Export maps.
21. Package projects.
22. Share GIS content.
23. Troubleshoot geoprocessing failures.
24. Diagnose coordinate system problems.
25. Optimize data organization and performance.

Ensure all workflows are technically accurate and compatible with the relevant ArcGIS Pro functionality.

---

# 6. LEARNING MODULES

Create structured learning modules aligned with the verified exam blueprint.

Every module should contain:

- Learning objectives.
- Key concepts.
- Technical explanations.
- Important terminology.
- ArcGIS Pro interface references.
- Relevant tools and parameters.
- Step-by-step workflows.
- Common mistakes.
- Knowledge checks.
- Related questions.
- Related scenarios.
- Official documentation links.

### Suggested Learning Areas

**Module 1 – Data Management**

- File Geodatabases.
- Feature Classes.
- Feature Datasets.
- Tables.
- Domains.
- Subtypes.
- Relationship Classes.
- Attribute Rules.
- Topology.
- Editing.
- Coordinate Systems.
- Projection.
- Data Quality.

**Module 2 – Visualization and Cartography**

- Symbology.
- Graduated Colors.
- Unique Values.
- Proportional Symbols.
- Labeling.
- Annotation.
- Label Expressions.
- Map Appearance.
- Layer Properties.
- Map Navigation.
- Cartographic Design.

**Module 3 – Analysis and Geoprocessing**

- Geoprocessing Framework.
- Tool Parameters.
- Environments.
- Spatial Analysis.
- Vector Analysis.
- Raster Analysis.
- Spatial Analyst.
- Network Analyst fundamentals where relevant.
- ModelBuilder.
- Selection.
- Overlay.
- Buffer.
- Spatial Join.
- Troubleshooting.

**Module 4 – Layouts and Sharing**

- Layout Design.
- Map Frames.
- Legends.
- Scale Bars.
- North Arrows.
- Map Series.
- Export Settings.
- Project Packaging.
- Sharing.
- Web Layers.
- Data and Layer Dependencies.
- Publishing Considerations.

These are suggested learning topics. Validate the final module structure against the official exam objectives.

---

# 7. REALISTIC EXAM SIMULATOR

Develop a professional examination simulator.

It should provide:

- Full examination mode.
- Custom examination mode.
- Randomized questions.
- Randomized answer options.
- Configurable question counts.
- Configurable difficulty.
- Domain-specific examinations.
- Scenario-only examinations.
- Timed examinations.
- Untimed practice.
- Question navigation.
- Previous/Next controls.
- Flag for review.
- Question status indicators.
- Answer review.
- Final submission confirmation.
- Score calculation.
- Detailed explanations after submission.
- Performance breakdown.

If the official examination format and timing are verified, provide a matching simulation preset.

Do not treat unverified exam parameters as official.

### Exam Experience

Design the examination interface to resemble a professional certification testing environment.

Include:

- Remaining time.
- Question number.
- Progress indicator.
- Answer selection.
- Review flags.
- Unanswered question indicator.
- Final submission screen.

Do not reveal correct answers during a simulated examination.

Allow users to review answers and explanations after completing the examination.

---

# 8. PERFORMANCE ANALYTICS AND WEAKNESS ANALYSIS

Develop a useful analytics dashboard.

Track performance by:

- Examination domain.
- Learning objective.
- Difficulty.
- Question type.
- Scenario performance.
- Learning module.
- Attempt history.

Display:

- Total questions attempted.
- Correct answers.
- Incorrect answers.
- Accuracy percentage.
- Completion percentage.
- Average performance.
- Strongest topics.
- Weakest topics.
- Improvement over time.
- Examination history.

### Weakness Analysis

Automatically identify weak topics.

For example:

If a candidate repeatedly fails questions about coordinate systems, recommend reviewing the Coordinate Systems module and attempting related questions.

Provide:

- Weak-topic ranking.
- Recommended learning modules.
- Recommended scenarios.
- Targeted practice sessions.
- Reassessment after revision.

Analytics must be based on actual stored attempts, not invented scores or simulated user data.

Use charts only where they improve understanding.

---

# 9. SMART REVISION SYSTEM

Implement a lightweight browser-based revision system.

Features:

- Incorrect-answer collection.
- Bookmarked questions.
- Flagged questions.
- Review by topic.
- Review by difficulty.
- Review by previous performance.
- Daily revision recommendations.
- Repeated practice of weak topics.

Implement a simple spaced-repetition strategy.

For example:

- Review after an incorrect answer.
- Review again after a short interval.
- Increase the review interval after repeated correct answers.

Store revision data locally.

Allow users to reset or export their revision history.

Do not require an external AI API.

The revision engine should work through deterministic rules and local performance data.

---

# 10. BILINGUAL EXPERIENCE

The entire platform must support English and Arabic.

### English

- Left-to-right layout.
- English terminology.
- English explanations.
- English questions and answers.

### Arabic

- Right-to-left layout.
- Proper Arabic typography.
- Correct text alignment.
- Arabic translations of questions.
- Arabic translations of explanations.
- Arabic navigation and labels.

Add a visible language switcher.

Preserve the user's selected language between visits.

Technical GIS terms may appear in English alongside their Arabic explanations where useful.

Do not use machine-generated Arabic translations without reviewing technical terminology and readability.

Both languages must provide equivalent educational content.

---

# 11. USER INTERFACE AND VISUAL DESIGN

Create a professional, modern educational platform.

The visual identity should communicate:

- GIS technology.
- Professional certification.
- Spatial analysis.
- Technical learning.
- Academic credibility.

### Design Requirements

- Clean dashboard.
- Professional typography.
- Clear visual hierarchy.
- Modern cards.
- Consistent spacing.
- Accessible contrast.
- Responsive navigation.
- Smooth but restrained transitions.
- Meaningful icons.
- Clear examination controls.

### Main Pages

1. Home / Dashboard.
2. Exam Overview.
3. Learning Modules.
4. Question Bank.
5. Scenario Library.
6. GIS Workflow Challenges.
7. Exam Simulator.
8. Performance Analytics.
9. Weak Topics.
10. Bookmarks.
11. Incorrect Answers.
12. Revision Center.
13. References.
14. Settings.

### Themes

Support:

- Light Mode.
- Dark Mode.

### Responsive Design

Optimize for:

- Desktop.
- Laptop.
- Tablet.
- Mobile.

The examination interface must remain usable on smaller screens.

Avoid unnecessarily large animations, oversized graphics, and heavy visual effects.

---

# 12. PERFORMANCE AND CODE QUALITY

GitHub Pages is static hosting. Optimize the application accordingly.

Mandatory performance considerations:

- Minimize initial JavaScript bundle size.
- Lazy-load large sections.
- Split question banks into manageable files.
- Avoid loading all questions on startup.
- Optimize fonts and icons.
- Avoid unnecessary animations.
- Avoid large image assets.
- Avoid unnecessary dependencies.
- Use efficient state management.
- Prevent repeated rendering where possible.
- Use semantic HTML.
- Follow accessibility best practices.
- Optimize chart rendering.
- Handle missing or invalid local data safely.

Do not introduce a complex state-management library unless genuinely required.

Do not add unnecessary backend-like abstractions.

### Error Handling

Implement useful error handling for:

- Missing JSON files.
- Invalid question records.
- Corrupted local storage.
- Failed imports.
- Invalid exported progress files.
- Missing references.
- Empty question collections.

Provide clear user-facing error messages.

The website must not silently lose saved progress.

---

# 13. CONTENT DATA SCHEMA

Create documented TypeScript interfaces and validation rules.

Example question structure:

{
  "id": "DM-001",
  "domain": "Data Management",
  "objective": "Coordinate Systems",
  "difficulty": "Intermediate",
  "type": "Conceptual",
  "question": {
    "en": "English question",
    "ar": "Arabic question"
  },
  "options": [
    {
      "id": "A",
      "text": {
        "en": "Option A",
        "ar": "الخيار أ"
      }
    },
    {
      "id": "B",
      "text": {
        "en": "Option B",
        "ar": "الخيار ب"
      }
    },
    {
      "id": "C",
      "text": {
        "en": "Option C",
        "ar": "الخيار ج"
      }
    },
    {
      "id": "D",
      "text": {
        "en": "Option D",
        "ar": "الخيار د"
      }
    }
  ],
  "correctAnswer": "B",
  "explanation": {
    "en": "Detailed explanation",
    "ar": "شرح تفصيلي"
  },
  "incorrectOptionsExplanation": {
    "en": {
      "A": "Why incorrect",
      "C": "Why incorrect",
      "D": "Why incorrect"
    },
    "ar": {
      "A": "سبب الخطأ",
      "C": "سبب الخطأ",
      "D": "سبب الخطأ"
    }
  },
  "references": [
    {
      "title": "Official Esri documentation",
      "url": "https://..."
    }
  ]
}

This is an illustrative schema. Improve it where necessary while maintaining consistency and validation.

Create separate schemas for:

- Questions.
- Scenarios.
- Learning modules.
- GIS workflows.
- References.
- User progress.
- Examination attempts.
- Revision records.

---

# 14. PROJECT STRUCTURE

Use a clean and scalable repository structure.

Suggested structure:

src/
  app/
  components/
  pages/
  layouts/
  features/
    dashboard/
    learning/
    questions/
    scenarios/
    workflows/
    exam/
    analytics/
    revision/
  hooks/
  services/
  storage/
  types/
  utils/
  styles/

public/
  data/
    questions/
    scenarios/
    modules/
    workflows/
    references/
  assets/

docs/
  EXAM_BLUEPRINT.md
  CONTENT_GUIDELINES.md
  DATA_SCHEMA.md
  ARCHITECTURE.md
  DEPLOYMENT_GITHUB_PAGES.md
  USER_GUIDE.md
  QUALITY_REPORT.md

.github/
  workflows/
    deploy.yml

Also include:

- README.md
- package.json
- vite.config.ts
- tsconfig.json
- .gitignore
- PROJECT_PROGRESS.md

Adapt the structure when necessary, but maintain clear separation between content, application logic, and local persistence.

---

# 15. AUTOMATED CONTENT VALIDATION

Create automated validation scripts.

The project must validate:

- At least 250 unique questions.
- At least 150 unique scenarios.
- At least 30 GIS workflows.
- Exactly four answer options per MCQ.
- One valid correct answer per question.
- English and Arabic content availability.
- Valid domain names.
- Valid difficulty values.
- Valid references.
- Unique question and scenario IDs.
- No missing required fields.
- No duplicate questions.
- No accidental duplicate scenarios.
- Valid JSON syntax.

Add a content quality report.

Do not count duplicated or incomplete records toward the minimum content requirements.

Include a report showing actual counts by domain, difficulty, and question type.

---

# 16. TESTING AND QUALITY ASSURANCE

Test the application before delivery.

### Functional Testing

Verify:

- Navigation.
- Language switching.
- RTL/LTR rendering.
- Theme switching.
- Question filtering.
- Search.
- Randomization.
- Exam timer.
- Answer submission.
- Scoring.
- Review mode.
- Bookmarking.
- Progress saving.
- Progress import/export.
- Weakness analytics.
- Revision recommendations.

### Deployment Testing

Verify:

- Production build succeeds.
- GitHub Pages base path works.
- Assets load correctly after deployment.
- Direct navigation works.
- Page refresh works.
- Browser storage works.
- No server is required.

### Content Testing

Verify the correct answer for every question.

Check technical accuracy against official Esri documentation.

Review Arabic translations.

Identify ambiguous questions.

Ensure scenario questions require actual reasoning.

Do not mark the project complete until these checks pass.

---

# 17. DEVELOPMENT WORKFLOW

Work in clearly defined phases.

Do not attempt to build everything in one uncontrolled step.

### Phase 1 – Research

- Verify official exam objectives.
- Collect official references.
- Establish content domains.
- Create the research report.

### Phase 2 – Architecture

- Define static hosting architecture.
- Configure Vite.
- Define TypeScript interfaces.
- Design the JSON data structure.
- Configure local persistence.
- Prepare GitHub Pages deployment.

### Phase 3 – UI Foundation

- Create the design system.
- Implement responsive layouts.
- Implement navigation.
- Implement Arabic and English.
- Implement light and dark themes.

### Phase 4 – Learning Platform

- Build learning modules.
- Build question bank.
- Build scenario library.
- Build GIS workflow section.

### Phase 5 – Examination System

- Implement exam simulator.
- Implement randomization.
- Implement timing.
- Implement scoring.
- Implement answer review.

### Phase 6 – Intelligence and Analytics

- Build performance dashboard.
- Implement weakness analysis.
- Implement smart revision.
- Implement bookmarks and incorrect-answer review.

### Phase 7 – Content Production

- Produce 250+ MCQs.
- Produce 150+ independent scenarios.
- Produce 30+ GIS workflows.
- Validate bilingual content and technical references.

### Phase 8 – Testing

- Test all features.
- Validate content.
- Optimize performance.
- Test responsive layouts.
- Test production build.

### Phase 9 – Deployment

- Configure GitHub Actions.
- Deploy to GitHub Pages.
- Verify the published website.
- Document future update procedures.

---

# 18. ADDITIONAL PROFESSIONAL RECOMMENDATIONS

Implement these recommendations where they provide real educational value.

### A. Exam Readiness Indicator

Create an Exam Readiness score based on:

- Performance across all domains.
- Scenario performance.
- Completed learning modules.
- Recent examination results.
- Weak-topic improvement.

Clearly label it as an internal practice indicator, not an official Esri passing probability.

Do not calculate readiness from insufficient data.

### B. Exam Strategy Center

Include a short preparation guide explaining:

- How to approach technical MCQs.
- How to eliminate incorrect options.
- How to interpret GIS scenarios.
- How to manage examination time.
- How to review difficult questions.
- Common ArcGIS Pro conceptual traps.

### C. Tool Comparison Reference

Build a searchable reference section comparing related tools and concepts.

Examples:

- Define Projection vs Project.
- Clip vs Intersect.
- Spatial Join vs Join Field.
- Feature Class vs Feature Dataset.
- Map vs Layout.
- Raster Functions vs Geoprocessing Tools.
- Domains vs Subtypes.
- Selection vs Definition Query.

Each comparison must explain the purpose, differences, and appropriate use cases.

### D. GIS Troubleshooting Library

Create a practical troubleshooting collection.

Examples:

- Incorrect coordinate system.
- Empty geoprocessing output.
- Invalid geometry.
- Missing data sources.
- Broken layer references.
- Labeling problems.
- Geoprocessing environment conflicts.
- Editing restrictions.
- Unexpected spatial analysis results.

### E. Personal Study Planner

Create a lightweight study planner.

Allow the candidate to:

- Set a target examination date.
- Set weekly study availability.
- Track completed topics.
- Identify unfinished topics.
- Receive locally generated study recommendations.

This must work without a backend.

### F. Printable Revision Sheets

Allow the candidate to generate print-friendly revision pages.

Include:

- Key terminology.
- Tool comparisons.
- Important concepts.
- Common mistakes.
- Selected incorrect questions.

Use browser print functionality rather than requiring a PDF generation server.

### G. Source Transparency

Every technical learning module and question should have traceable supporting references where applicable.

Clearly distinguish:

- Official Esri documentation.
- Original educational explanations.
- Practice scenarios.
- Unverified information.

Never fabricate documentation URLs.

---

# 19. IMPORTANT DEVELOPMENT RULES

1. Build a functioning application, not a design mockup.
2. Do not use placeholder questions to satisfy content counts.
3. Do not generate repetitive questions just to reach 250.
4. Do not generate shallow scenarios just to reach 150.
5. Do not claim that the website guarantees passing the exam.
6. Do not claim that practice questions are official exam questions.
7. Do not invent Esri exam requirements.
8. Do not introduce a backend.
9. Do not introduce paid services as core dependencies.
10. Do not make GitHub Pages deployment an afterthought.
11. Do not sacrifice performance for unnecessary visual effects.
12. Do not hide incomplete features behind misleading UI.
13. Do not mark a feature as complete until it has been tested.
14. Maintain clear and readable code.
15. Keep all technical content bilingual.
16. Keep the content data separate from the UI.
17. Preserve existing working functionality when implementing changes.
18. Document architectural decisions.
19. Track completed and pending tasks in PROJECT_PROGRESS.md.
20. If a requirement cannot be implemented within static hosting constraints, explain the limitation and propose a static-compatible solution instead of silently adding a backend.

---

# 20. FINAL ACCEPTANCE CRITERIA

The project is complete only when all the following conditions are satisfied:

| Requirement | Minimum |
|---|---:|
| Original MCQs | 250 |
| Independent scenario questions | 150 |
| Practical GIS workflows | 30 |
| Learning modules | All verified exam domains |
| Languages | English + Arabic |
| Interface directions | LTR + RTL |
| Themes | Light + Dark |
| Exam simulator | Fully functional |
| Analytics | Fully functional |
| Local progress storage | Functional |
| Import/export | Functional |
| Weakness analysis | Functional |
| Smart revision | Functional |
| GitHub Pages deployment | Verified |
| Backend | None |
| Production build | Successful |
| Content validation | Passed |

### Final Deliverables

Provide:

1. Complete source code.
2. Fully functional production website.
3. GitHub Pages deployment configuration.
4. Official exam research report.
5. Complete bilingual question bank.
6. Complete scenario bank.
7. Practical GIS workflows.
8. Technical documentation.
9. Content validation report.
10. Testing report.
11. GitHub Pages deployment instructions.
12. README.md.
13. PROJECT_PROGRESS.md.

### Final Instruction

Start by researching the official EAPA_2025 certification objectives and preparing the static architecture.

Then implement the project phase by phase.

Do not stop after creating the landing page or UI.

Continue until the educational content, examination system, analytics, revision tools, validation, and GitHub Pages deployment are all implemented and tested.

The final result must be a professional, fast, bilingual, maintainable, and genuinely useful ArcGIS Pro Associate 2025 preparation platform that can be hosted directly from a GitHub repository without requiring a traditional backend.