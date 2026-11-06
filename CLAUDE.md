# CLAUDE.md — authoring instructions for *Foundations of Agentic AI*

This repository is a **book**, published as a static website from `docs/` (GitHub Pages, auto-deployed by `.github/workflows/pages.yml` on every push that touches `docs/`). Read this file, `NOTATION.md`, `BOOK_SKELETON.md` and `REVIEW.md` before writing or editing any chapter. The site machinery (reader engine, charts, KaTeX, accounts and sync) is shared with the companion book *Introduction to LLM Engineering* (`jaswin90/LLM-Engineering`); keep the two compatible.

## 1. Reader and promise
- Reader: PhD in mathematics, ~5 years of data science, little software or systems engineering. Assume fluency in linear algebra, probability, optimisation and basic Markov chains. Assume no knowledge of reinforcement-learning practice, operating systems, networking, web protocols or security engineering.
- Goal: the reader can explain every major agent technique and why it appeared when it did, reason quantitatively about an agent's reliability, cost and latency, design, evaluate and secure an agent system, and pass AI-lab and FAANG interviews for agent / applied-AI engineering roles.

## 2. It must read like a book
1. **Prose first.** At least 75% of each chapter is continuous prose. Boxes, tables and bullet lists *support* the prose; they never replace it.
2. **Paragraphs develop ideas.** A typical paragraph is 4–8 sentences: claim → reasoning → example → consequence.
3. **Every section follows the arc: motivation → idea → mathematics → worked example → consequences → bridge.** Open with the problem that makes the idea necessary; end with the new question it raises.
4. **Never use a concept before it is motivated and defined.** If a forward reference is unavoidable, give an informal one-sentence definition and say which chapter makes it precise.
5. **Chapter opening.** An unnumbered "Why this chapter" section: where we are in the story, the question this chapter answers, learning objectives, and which earlier chapters it uses.
6. **Chapter closing.** "Looking ahead" names the open problem the next chapter solves. Then summary, MCQs, interview questions, references.
7. **Tell the evolution.** Techniques as a causal chain: bottleneck → idea → new bottleneck. Give dates and say who did it and why it was needed *then*.
8. **Figures are discussed, not just captioned.** The body text refers to every figure ("Figure 3.2 shows…") and walks the reader through it.
9. **Software-engineering bridges.** When a systems concept appears (process, sandbox, API, JSON schema, queue, database, token, permission), explain it in mathematical language in a "For the mathematician" box.
10. **Tone.** Precise, warm, direct. "We" for derivations. No hype, no filler, no unexplained jargon, no anthropomorphising beyond what the mathematics supports. British spelling (optimisation, behaviour, modelling).

## 3. Consistency
- **Notation:** only the symbols in `NOTATION.md`. Add new symbols there before using them and check for collisions. In particular: \(\pi_\theta\) = policy, \(H\) = horizon (number of agent steps), \(\tau\) = trajectory, \(\rho\) = per-step success probability, \(T_s\) = sampling temperature, \(n\) = number of tokens, \(k\) = number of samples/attempts, \(\kappa\) = price per token.
- **Running examples** (use these unless a different system is the point):
  1. **The coding agent** — fixes a GitHub issue in a Python repository (SWE-bench style): reads files, runs tests, edits code.
  2. **The support agent** — an airline customer-service agent with tools for bookings and refunds and a policy document (τ-bench style).
  3. **The research agent** — answers an open question by searching the web, reading pages and writing a cited report.
- **Reference model and prices** (illustrative, used for all cost arithmetic unless stated): a frontier model at \(\kappa_{\text{in}}=\$3\), \(\kappa_{\text{out}}=\$15\), \(\kappa_{\text{cache}}=\$0.30\) per million tokens; 200k-token context window; decode at 60 tokens/s; prefill at 5,000 tokens/s. A small model at \(\$0.25\) / \(\$1.25\) per million. State clearly that real prices vary and change.
- Cross-reference as "§3.4", "Chapter 5", "Figure 3.2".

## 4. Required components per chapter
- Learning objectives; opening motivation; numbered sections; at least 4 inline SVG diagrams and 2 data charts where the topic allows; at least 2 worked examples (`div.box.example`) and 2 drills (`details.drill`); "Looking ahead"; summary.
- **MCQs:** 30 or more (`div.mcq` with `data-id` like `ch03-mcq-07`, `data-topic` naming the section such as "§3.5 Sampling", options in `ol.opts`, correct options marked `data-correct`, explanation in `.explain`).
- **Interview questions:** 15 or more (`details.qa` with `data-id`, a level pill `warm|core|deep|design`, model answer in `.answer`).
- **References:** primary sources with arXiv links at the end, cited inline with `<span class="cite">`. Add key sources to `docs/references.html`.
- **Length:** 9,000–14,000 words including questions.

## 5. Technical conventions
- Chapters live in `docs/chapters/chNN.html`, registered in `CHAPTERS` in `docs/assets/js/book.js` (set `ready: true`).
- Math: KaTeX (vendored). `\( … \)` inline, `\[ … \]` display. Never `$` delimiters (`$` is for prices). Escape `<` as `&lt;` in math.
- Diagrams: inline `<svg class="dg">` with the `book.css` classes (`bx`, `bx2`, `bx3`, `ln`, `ln-acc`, `t-sm`, `t-on`, `fill-acc`…). Never put KaTeX inside SVG; use `<tspan>` for subscripts. Charts: `figure.chart` with a JSON `script.chart-spec` (see `docs/assets/js/charts.js`); colour slots `s1`, `s2`, `s3` first.
- Wide tables go inside `div.table-wrap`.
- Never rename published `data-id`s (readers' progress is keyed on them).
- Progress for this book is stored under the `agenticAI` field of the shared Firebase document `users/{uid}`; never write outside it.

## 6. Before pushing
1. Serve `docs/` locally and run `tools/check_pages.js` (Playwright): no page errors, no `.katex-error`, no horizontal overflow at 390 px, all charts rendered, every figure inside `article`. Look at screenshots of new figures. Keep screenshots in the scratchpad, never in the repo.
2. Recompute every quantitative claim from its formula before publishing.
3. Update `BOOK_SKELETON.md` (status) and add a `REVIEW.md` entry for any editorial pass.
4. Commit and push to the working branch. Site: https://jaswin90.github.io/Foundations-Agentic-AI/.
