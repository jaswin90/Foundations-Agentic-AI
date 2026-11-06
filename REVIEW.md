# Editorial review log

Every editorial pass is recorded here: what was found, the evidence, and what was changed.

## Review 0 — Setting up the book (2026-11-06)
- The site machinery was copied from *Introduction to LLM Engineering* (reader engine, charts, KaTeX, accounts and sync) so readers of both books get the same experience, and the authoring rules (`CLAUDE.md`) were adapted to agents: the same prose-first, motivation-first standard, the same per-chapter minimums.
- **Notation chosen up front.** Agents mix RL and language-model notation, which collide easily. Decisions: \(\pi_\theta\) is the policy (no hardware peak-FLOP symbol is needed in this book); \(\tau\) is a trajectory, so sampling temperature is \(T_s\); \(H\) is the horizon and \(t\) the agent step, so token positions use \(i\); \(\rho\) is per-step success and \(p\) per-attempt task success; \(\kappa\) is a price per token, so \(C\) is reserved for cost; \(\beta\) is the KL coefficient only.
- **Shared Firebase project.** Both books keyed progress by `ch01-mcq-01` etc., so sharing one `users/{uid}` document would have mixed them, and the LLM book's full-document write would have erased this book's data. This book now stores progress under `agenticAI`, and both books write with `mergeFields`.
