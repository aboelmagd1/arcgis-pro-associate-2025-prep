import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Base path: relative by default; set VITE_BASE=/<repo-name>/ for GitHub Pages.
export default defineConfig({
  base: process.env.VITE_BASE ?? './',
  plugins: [react()],
  build: { chunkSizeWarningLimit: 300 },
});
