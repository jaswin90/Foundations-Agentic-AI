# Foundations of Agentic AI

A free, interactive, web-native textbook on **agentic AI**: agents as decision processes, the language model inside the agent, context engineering, reasoning and planning, tool use, retrieval, code and computer-use agents, protocols, memory, multi-agent systems, training agents with imitation and reinforcement learning, evaluation, security and production. It is written for readers with a strong mathematical background (PhD level) and data-science experience but little software engineering, and it aims at AI-lab / FAANG interview depth.

**Read it:** https://jaswin90.github.io/Foundations-Agentic-AI/

Companion book: [Introduction to LLM Engineering](https://jaswin90.github.io/LLM-Engineering/) (inference and serving). The two books share the same reader engine and, optionally, the same Firebase project for accounts; this book stores its progress under its own `agenticAI` field.

## Repository layout

| Path | Contents |
|---|---|
| `BOOK_SKELETON.md` | The plan: 22 chapters in 7 parts, with a status table |
| `CLAUDE.md`, `NOTATION.md`, `REVIEW.md` | Authoring rules, the book-wide notation table, and the editorial review log |
| `docs/` | The website (GitHub Pages root) |
| `docs/assets/js/book.js` | Reader engine: TOC, theme, MCQ and Q&A components, progress store |
| `docs/assets/js/auth.js` | Accounts (email/password, Google) and Firestore sync |
| `docs/assets/js/charts.js` | Dependency-free SVG chart renderer |
| `tools/` | `build_notation.py` (regenerates the notation page), `check_pages.py` (Playwright checks) |
| `.github/workflows/pages.yml` | Deploys `docs/` to GitHub Pages |
