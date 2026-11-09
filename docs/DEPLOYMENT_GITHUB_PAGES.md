# Deploying to GitHub Pages
1. Push to a GitHub repo with default branch `main`.
2. Settings > Pages > Source: **GitHub Actions**.
3. Push; `.github/workflows/deploy.yml` validates content, builds with `VITE_BASE=/<repo-name>/`, and publishes `dist`.
Local dev: `npm install && npm run dev`. Pages-style local build: `VITE_BASE=/<repo-name>/ npm run build && npm run preview`.
Routing is hash-based (`/#/overview`), so refresh and direct links work without server rewrites.
