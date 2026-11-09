# Esri ArcGIS Pro Associate 2025 (EAPA_2025) Master Preparation Platform
## منصة التحضير المعتمدة لاختبار محترف آرك جي آي إس برو 2025

A production-grade, 100% bilingual (English & Arabic) learning management system and examination simulator designed specifically for the **Esri ArcGIS Pro Associate 2025 (`EAPA_2025`)** certification.

---

## 🌟 Key Features

### 1. Curated Content Bank (100% Bilingual EN + AR)
- **250 Verified MCQs**: Strict domain allocation aligned with the official blueprint:
  - **Data Management (32%)**: 80 questions (`DM-001` to `DM-080`)
  - **Visualization (25%)**: 63 questions (`VIZ-001` to `VIZ-063`)
  - **Analysis & Geoprocessing (25%)**: 62 questions (`AGP-001` to `AGP-062`)
  - **Layouts & Sharing (18%)**: 45 questions (`LS-001` to `LS-045`)
- **150 Practical GIS Scenarios**: Realistic situational challenges requiring technical decision making and problem solving:
  - Data Management: 48 scenarios (`DM-S-001` to `DM-S-048`)
  - Visualization: 38 scenarios (`VIZ-S-001` to `VIZ-S-038`)
  - Analysis & Geoprocessing: 37 scenarios (`AGP-S-001` to `AGP-S-037`)
  - Layouts & Sharing: 27 scenarios (`LS-S-001` to `LS-S-027`)
- **30 Practical Hands-on Workflows**: Step-by-step procedural guides from *Getting to Know ArcGIS Pro 3.2* with parameter tables, UI click paths, Quality Control (QC) rules, and common pitfalls.
- **12 Comprehensive Learning Modules**: Complete theoretical curriculum with interface click paths, comparison matrices, interactive lab checklists, and direct quiz launchers.
- **100 3D Interactive Flashcards**: Quick-recall cards with 3D flip animation, category filtering, and mastery tracking.
- **Top 52 Data Management Tools Encyclopedia**: ArcPy syntax, tool parameters, UI paths, and exam traps.
- **12 Tool Comparison Matrices**: Deep-dive comparisons (e.g., Define Projection vs Project, Clip vs Intersect, Spatial Join vs Add Join).
- **12 GIS Troubleshooting Guides**: Root causes, diagnostic steps, and resolution paths for common GIS failures.
- **4-Week Day-by-Day Study Planner**: Structured schedule covering all exam domains.

### 2. Pearson VUE-Style Exam Simulator
- **Official 75Q / 90min Simulation Preset**: Accurately mirrors the official exam format and domain weights (32/25/25/18%).
- **Option Elimination**: Strike-through tool to visually eliminate incorrect options during testing.
- **Flag for Review**: Bookmark uncertain questions and navigate via the question status grid.
- **Custom Exam Mode**: Filter by domain, difficulty, scenario-only, due-for-revision, or saved bookmarks.
- **Detailed Analytics & Explanations**: Full rationale for correct and incorrect options upon exam completion.

### 3. Analytics & Smart Revision
- **Readiness Score (0-100%)**: Diagnostic scoring based on completed attempts and question coverage.
- **Weak Topic Detection**: Identifies struggling objectives and provides direct practice links.
- **Spaced Repetition System**: Automatically schedules questions for review based on previous performance.

### 4. Zero Backend Architecture
- Static client-side application deployable on **GitHub Pages**.
- All data stored safely in browser `localStorage`.
- Full JSON export and import capabilities to backup and transfer progress between devices.
- Seamless Dark/Light theme and instant English/Arabic language switching (supporting LTR and RTL layouts).

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ or 20+
- npm 9+

### Installation & Local Development
```bash
# Navigate to the project directory
cd eapa-prep

# Install dependencies
npm install

# Start local development server
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## 🧪 Verification & Testing

Run the automated verification suite to ensure 100% data integrity and test coverage:

```bash
# Run strict content validation (verifies 250 MCQs, 150 scenarios, 30 workflows)
npm run validate:strict

# Run unit tests (exam logic, analytics stats, bookmarking)
npm test

# Build for production
npm run build
```

---

## 🌐 Deploying to GitHub Pages

1. Push this repository to GitHub with the default branch set to `main`.
2. Go to repository **Settings** > **Pages** > **Build and deployment** > **Source**, and select **GitHub Actions**.
3. Push to `main`; the included `.github/workflows/deploy.yml` workflow will automatically validate the content, build the static site, and deploy it to GitHub Pages.

---

## 📚 Official Esri References
- [Esri ArcGIS Pro Documentation](https://pro.arcgis.com/en/pro-app/latest/get-started/get-started.html)
- [ArcGIS Pro Tool Reference](https://pro.arcgis.com/en/pro-app/latest/tool-reference/main/arcgis-pro-tool-reference.html)
- [ArcPy Reference](https://pro.arcgis.com/en/pro-app/latest/arcpy/main/arcgis-pro-arcpy-reference.html)
- [Esri Technical Certification Program](https://www.esri.com/training/catalog/certification/)

---

## ⚖️ Disclaimer
*This platform is an independent study aid designed for candidate preparation. It is not affiliated with, endorsed by, or sponsored by Esri. Practice questions and scenarios are original educational materials and do not represent actual live exam questions.*
