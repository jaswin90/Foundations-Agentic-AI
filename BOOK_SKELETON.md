# Foundations of Agentic AI — Book Skeleton (v1)
### Reasoning, tools, memory, planning, multi-agent systems, training and evaluation of LLM agents, for AI-lab and FAANG interviews

> **Reader.** PhD in mathematics, ~5 years of data science, little software or systems engineering.
> **Promise.** Explain every major agent technique of 2020–2026 and why it appeared when it did; reason quantitatively about an agent's reliability, cost and latency; design, evaluate and secure an agent system; pass agent-engineering and applied-AI interviews.
> **How it is written.** See `CLAUDE.md` (style), `NOTATION.md` (symbols) and `REVIEW.md` (editorial log). Companion: *Introduction to LLM Engineering* (inference and serving).

---

## The story the book tells

1. **Part I — What is an agent?** An agent is a policy acting in a partially observed world. A language model becomes such a policy when its output is parsed into actions and the results are written back into its context. The model brings priors from pre-training and instruction tuning; the context is its only working state. *Open question: a model that answers in one shot is often wrong. How do we make it think before it acts?*
2. **Part II — Reasoning and planning.** Chain of thought, self-consistency, reasoning models; search over thoughts and actions; reflection and verification. *Open question: thinking alone cannot read a file or book a flight. How does the agent act on the world?*
3. **Part III — Acting.** Tool calling, retrieval, code execution, computer use, and the protocols that connect agents to tools. *Open question: every observation lands in a finite context. What does the agent remember, and for how long?*
4. **Part IV — Memory and state.** Memory architectures; long-horizon agents that compact, delegate and checkpoint. *Open question: one agent with one context is a bottleneck. When do many agents help?*
5. **Part V — Many agents.** Multi-agent systems and the canonical architectures and frameworks. *Open question: prompting has limits. Can the agent learn from its own experience?*
6. **Part VI — Learning to act.** Imitation, preferences, RLHF and DPO; reinforcement learning with verifiable rewards over multi-turn trajectories. *Open question: how do we know an agent works, keep it safe, and run it at a price?*
7. **Part VII — Reliability, safety and production.** Evaluation, security, production engineering, and the agent system-design interview.

**Running examples.** The coding agent (fix a GitHub issue; SWE-bench), the support agent (airline policy and tools; τ-bench), the research agent (search, read, write a cited report). Reference prices: \$3 / \$15 / \$0.30 per million input / output / cached tokens.

**Per-chapter components.** Motivating opening → numbered sections (motivation → idea → math → example → consequence → bridge) → Looking ahead → summary → 30+ MCQs → 15+ interview questions → references. Target 9–14k words.

---

## Part I — What Is an Agent?

### Chapter 1 — From Cybernetics to Language Agents
**Motivating question.** Why did "agents", an idea as old as AI itself, suddenly become practical between 2022 and 2025, and what exactly changed?
**Arc.** The agent abstraction (sense → decide → act) → cybernetics and feedback (Wiener 1948) → symbolic planning (GPS, STRIPS, Shakey) and the frame problem → BDI and the agent-oriented 1990s → reinforcement learning (TD-Gammon, DQN, AlphaGo) and the sample-efficiency wall → language models as general priors → the first language agents (WebGPT, SayCan, ReAct, Toolformer) → the 2023 hype and why AutoGPT failed → function calling, reasoning models, coding and computer-use agents (2023–2026) → measuring agents (success, cost, latency, pass^k) → map of the book.
**Key references.** Wiener 1948; Newell & Simon 1961; Fikes & Nilsson 1971; Brooks 1986; Rao & Georgeff 1995; Tesauro 1995; Mnih 2015; Silver 2016; Nakano 2021; Ahn 2022; Yao 2022 (ReAct); Schick 2023; Park 2023; Wang 2023 (Voyager); Jimenez 2023; Yao 2024 (τ-bench); Kwa 2025 (METR).

### Chapter 2 — Agents as Decision Processes
**Motivating question.** What is the right mathematical object for an LLM agent, and what does that object predict about reliability?
**Arc.** MDPs → POMDPs and belief states → the LLM agent as a policy over strings; the context as a sufficient statistic (and when it is not) → workflows vs agents as restricted policy classes → compounding error \(\rho^H\) and its fixes → recovery and absorbing failure states → the cost and latency of an episode.

### Chapter 3 — The Language Model Inside the Agent
**Arc.** Next-token prediction → in-context learning as implicit Bayesian inference → instruction tuning and RLHF in brief → sampling and temperature → calibration and uncertainty → what a call costs (prefill, decode, caching; link to the companion book).

### Chapter 4 — Context Engineering
**Arc.** The context window as a budget → system prompts and role → few-shot and many-shot → structured output → prompt caching economics → context rot and position effects → compaction preview.

## Part II — Reasoning and Planning
### Chapter 5 — Chain of Thought and Test-Time Reasoning
CoT (Wei 2022), zero-shot CoT (Kojima 2022), self-consistency (Wang 2022) with majority-vote analysis, least-to-most, reasoning models (o1, DeepSeek-R1), test-time scaling laws (Snell 2024), faithfulness of CoT.
### Chapter 6 — Search and Planning
Best-of-n and verifiers, Tree of Thoughts, MCTS/LATS, plan-and-execute, LLM+P and classical planners, cost of search.
### Chapter 7 — Reflection, Critique and Self-Correction
Self-Refine, Reflexion, CRITIC, "LLMs cannot self-correct reasoning yet", generator–verifier gap, process reward models.

## Part III — Acting: Tools and Environments
### Chapter 8 — Tool Use and Function Calling
Toolformer, Gorilla, function calling APIs, JSON Schema and constrained decoding, parallel calls, tool design (agent–computer interfaces).
### Chapter 9 — Retrieval and Knowledge
BM25, dense retrieval and embeddings, ANN indexes, rerankers, RAG (Lewis 2020), agentic and iterative retrieval, GraphRAG, evaluation.
### Chapter 10 — Code as Action
CodeAct, PAL, sandboxes and isolation, SWE-agent, Agentless, coding agents, SWE-bench and its variants.
### Chapter 11 — Computer Use and Web Agents
WebShop, Mind2Web, WebArena, OSWorld, grounding and set-of-marks, screenshots vs accessibility trees, latency.
### Chapter 12 — Protocols and Interoperability
MCP (2024), agent-to-agent protocols (2025), OAuth and delegated authorisation, tool discovery.

## Part IV — Memory and State
### Chapter 13 — Memory Architectures
CoALA taxonomy, generative agents' retrieval score, MemGPT, episodic/semantic/procedural memory, skill libraries (Voyager).
### Chapter 14 — Long-Horizon Agents
Compaction, note-taking, sub-agents, checkpoints and resumption, METR time horizons, error recovery.

## Part V — Many Agents
### Chapter 15 — Multi-Agent Systems
Debate, CAMEL, ChatDev/MetaGPT, AutoGen, orchestrator–workers, when and why many agents help (and cost).
### Chapter 16 — Agent Architectures and Frameworks
Prompt chaining, routing, parallelisation, orchestrator–workers, evaluator–optimiser; graphs and state machines; durable execution.

## Part VI — Learning to Act
### Chapter 17 — Learning from Demonstrations and Preferences
Behaviour cloning on trajectories (FireAct, AgentTuning), RLHF, Bradley–Terry, DPO derivation, rejection sampling.
### Chapter 18 — Reinforcement Learning for Agents
Policy gradient, PPO, GRPO, RLVR, multi-turn credit assignment, environments, reward hacking.

## Part VII — Reliability, Safety and Production
### Chapter 19 — Evaluating Agents
Benchmarks (SWE-bench, τ-bench, GAIA, WebArena, OSWorld, METR), pass@k vs pass^k, confidence intervals, LLM-as-judge.
### Chapter 20 — Safety and Security
Prompt injection (direct/indirect), sandboxing and least privilege, CaMeL and dual-LLM designs, misalignment evaluations.
### Chapter 21 — Agents in Production
Cost and latency models, routing between models, caching, observability and tracing, guardrails, human-in-the-loop.
### Chapter 22 — The Agent System Design Interview
Worked case studies and rubrics.

---

## Status

| Chapter | Status | Words | MCQs | QAs |
|---|---|---|---|---|
| 1 From Cybernetics to Language Agents | ✅ v1 | ≈12,500 | 32 | 16 |
| 2 Agents as Decision Processes | ✅ v1 | ≈9,300 | 31 | 16 |
| 3 The Language Model Inside the Agent | ✅ v1 | ≈9,000 | 31 | 16 |
| 4 Context Engineering | ✅ v1 | ≈10,500 | 31 | 16 |
| 5 Chain of Thought and Test-Time Reasoning | ✅ v1 | ≈10,000 | 31 | 16 |
| 6 Search and Planning | ✅ v1 | ≈9,000 | 31 | 16 |
| 7 Reflection, Critique and Self-Correction | ✅ v1 | ≈9,000 | 31 | 17 |
| 8 Tool Use and Function Calling | ✅ v1 | ≈9,000 | 31 | 16 |
| 9–22 | planned | | | |
