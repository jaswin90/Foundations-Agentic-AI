# Notation used throughout *Foundations of Agentic AI*

Every chapter must use these symbols. If a new symbol is needed, add it here first and check it does not collide with an existing one. The same table is rendered on the site at `docs/notation.html` (regenerate with `python3 tools/build_notation.py`).

## Decision processes and agents
| Symbol | Meaning |
|---|---|
| \(\mathcal S, \mathcal A, \mathcal O\) | state, action and observation spaces |
| \(s_t, a_t, o_t, r_t\) | environment state, action, observation and reward at step \(t\) |
| \(t\) | agent step index, \(t = 1,\dots,H\) |
| \(H\) | horizon: number of agent steps (model calls that may act) in an episode |
| \(P(s'\mid s,a)\), \(Z(o\mid s)\) | transition kernel; observation kernel |
| \(R(s,a)\), \(\gamma\) | reward function; discount factor |
| \(b_t\) | belief state, a distribution over \(\mathcal S\) given the history |
| \(h_t\) | history \((o_1,a_1,\dots,a_{t-1},o_t)\) |
| \(c_t\) | context: the token string the model is conditioned on at step \(t\) |
| \(\tau\) | trajectory (episode) \((c_1,a_1,o_2,\dots)\); \(R(\tau)\) its return |
| \(\pi\), \(\pi_\theta\) | policy; policy given by a model with parameters \(\theta\) |
| \(\pi_{\text{ref}}\) | reference policy (for KL regularisation) |
| \(V^\pi, Q^\pi, A^\pi\) | state value, action value and advantage under \(\pi\) |
| \(\mathcal G\) | goal or task specification |

## Language models
| Symbol | Meaning |
|---|---|
| \(\mathcal V\), \(\lvert\mathcal V\rvert\) | token vocabulary and its size |
| \(x_i\), \(x_{&lt;i}\) | token at position \(i\); the tokens before it |
| \(p_\theta(x_i\mid x_{&lt;i})\) | the model's next-token distribution |
| \(n\) | a number of tokens; \(n_{\text{in}}, n_{\text{out}}\) prompt and generated tokens of one call |
| \(n_{\max}\) | context-window size in tokens |
| \(z\), \(T_s\) | logits; sampling temperature |
| \(N\) | number of model parameters |
| \(\mathcal L\) | training loss |
| \(y\), \(y_w, y_l\) | a model response; preferred and dispreferred responses |
| \(r_\phi\) | learned reward model with parameters \(\phi\) |
| \(\beta\) | KL-regularisation coefficient (RLHF, DPO) |
| \(\sigma\) | logistic function \(\sigma(u)=1/(1+e^{-u})\) |
| \(\psi\) | latent task or concept inferred in context (Ch. 3) |
| \(\xi\) | Toolformer filtering threshold on loss reduction (Ch. 8) |
| \(\omega\) | logit margin of the correct choice over each plausible alternative (Ch. 8) |
| \(N\) (Ch. 8) | number of plausible tools in a selection; elsewhere, parameters |
| \(Z(x)\) | partition function of the KL-regularised optimum (Ch. 3); distinct from the observation kernel \(Z(o\mid s)\) by its argument |

## Reliability, search and evaluation
| Symbol | Meaning |
|---|---|
| \(\rho\) | per-step success probability |
| \(p\) | per-attempt success probability of a whole task |
| \(k\) | number of samples, attempts or candidates |
| pass@\(k\) | probability at least one of \(k\) attempts succeeds |
| pass^\(k\) | probability all \(k\) independent attempts succeed |
| \(m\) | number of tasks in an evaluation set |
| \(M\), \(N\) (Ch. 12) | numbers of agent applications and of systems to integrate |
| \(q\) (Ch. 12) | probability a third-party server is malicious; elsewhere \(q\) is a query |
| \(\mathcal P_U\), \(\mathcal P_\tau\) | permissions of principal \(U\); permissions authorised by credential \(\tau\) (Ch. 12) |
| \(\hat p\) | estimated success rate on \(m\) tasks |
| \(b\) | branching factor of a search tree |
| \(\epsilon\) | error rate (of a verifier, judge or step) |
| \(\epsilon_-,\epsilon_+\) | a verifier's false-negative and false-positive rates (Ch. 6) |
| \(A(n)\) | accuracy of best-of-\(n\) selection (Ch. 6) |
| \(b_{\text{prop}}\), \(\Lambda\) | proposals per node and depth of a search tree (Ch. 6) |
| \(\hat Q(s,a)\), \(N(s)\), \(N(s,a)\), \(c_{\text{uct}}\) | MCTS value estimate, visit counts and exploration constant (Ch. 6) |
| \(r\), \(\delta\) | probability an error is detected; extra steps to recover (Ch. 2) |
| \(\epsilon_f\) | per-step rate of fatal (undetected) errors (Ch. 14) |
| \(\varrho\) | correlation (shared-draw probability) among ensemble members (Ch. 15) |
| \(\rho_s\), \(r_g\) | success probability of a chain stage; fraction of stage failures a gate catches (Ch. 16) |
| \(f\) (Ch. 15), \(S(n)\) | parallelisable fraction of work; Amdahl speed-up with \(n\) workers |
| \(\Lambda\) (Ch. 14), \(p_m\), \(r_m\) | steps per milestone; milestone success probability; probability a failed milestone is detected |
| \(C_{\text{ck}}\), \(M_{\text{int}}\), \(\tau_c\), \(\Omega\) | checkpoint cost; mean time between interruptions; checkpoint interval; overhead fraction (Ch. 14) |
| \(U\), \(c\), \(F\) | value of success; cost of one more step or attempt; cost of a failure (Ch. 2, 6) |
| \(q_t\), \(\varphi\) | belief that the goal is achieved; rate of false success claims (Ch. 2) |
| \(D\) | difficulty of a problem in reasoning tokens (Ch. 5) |
| \(\mu,\nu\) | per-round probabilities that revision fixes a wrong answer / breaks a right one (Ch. 7) |
| \(a_k\), \(a^*\) | accuracy after \(k\) revision rounds; its fixed point \(\mu/(\mu+\nu)\) (Ch. 7) |
| \(B\) | reasoning budget in tokens (Ch. 5) |

## Training (Part VI)
| Symbol | Meaning |
|---|---|
| \(m_i\) | loss mask on token \(i\): 1 if written by the agent, 0 if from the environment (Ch. 17); distinct from \(m\), the number of tasks |
| \(\mathcal D_{\text{demo}}\), \(\mathcal D_{\text{pref}}\) | demonstration and preference datasets (Ch. 17); distinct from the document collection \(\mathcal D\) |
| \(\pi^*\), \(\hat\pi\) | expert policy and learned (cloned) policy (Ch. 17) |
| \(\hat r_\theta\), \(\hat\Delta\) | DPO implicit reward \(\beta\log(\pi_\theta/\pi_{\text{ref}})\) and implicit margin (Ch. 17) |
| \(W_0\), \(A\), \(B\), \(d_r\), \(\alpha_{\text{lo}}\), \(d_1,d_2\) | frozen weight, LoRA factors, LoRA rank, LoRA scale, matrix dimensions (Ch. 17) |

| \(\mathcal X\) | distribution of tasks for training (Ch. 18) |
| \(V^\pi(x)\), \(V_\psi\) | value (expected return) of policy \(\pi\) from task or prefix \(x\); learned value network (Ch. 18) |
| \(b(x)\), \(\hat A_i\) | baseline; advantage estimate for token or trajectory \(i\) (Ch. 18); distinct from best-of-\(n\) accuracy \(A(n)\) |
| \(w_i(\theta)\), \(\epsilon_{\text{clip}}\) | PPO per-token probability ratio; clip range (Ch. 18) |
| \(\lambda_{\text{gae}}\), \(\delta_t\) | GAE parameter; temporal-difference error (Ch. 18); distinct from arrival rate \(\lambda\) and recovery steps \(\delta\) |
| \(\Phi(s)\) | shaping potential (Ch. 18) |

| \(n\), \(c\) (Ch. 19) | runs per task and successes among them, in pass@\(k\) estimators; elsewhere \(n\) counts tokens |
| \(\sigma^2_{\text{task}}\), \(\overline{p(1-p)}\) | between-task variance of success probabilities; mean within-task Bernoulli variance (Ch. 19) |
| \(b\), \(c\) (Ch. 19) | discordant counts in McNemar's test (only A, only B succeeds) |
| \(q\) (Ch. 19) | rate at which a judge accepts outputs |

## Retrieval and memory
| Symbol | Meaning |
|---|---|
| \(q\) | a query |
| \(\mathcal D\), \(d\) | a document collection; one document or chunk |
| \(e(\cdot)\), \(d_e\) | embedding map and embedding dimension |
| \(\operatorname{sim}(u,v)\) | similarity, usually cosine \(u^\top v/(\lVert u\rVert\lVert v\rVert)\) |
| \(K\) | number of retrieved items (top-\(K\)) |
| \(\alpha_{\text{rec}},\alpha_{\text{imp}},\alpha_{\text{rel}}\) | weights of recency, importance and relevance in memory retrieval (Ch. 13) |
| \(N_{\mathcal D}\), \(\mathrm{tf}(u,d)\), \(\mathrm{df}(u)\) | collection size; count of term \(u\) in \(d\); documents containing \(u\) (Ch. 9) |
| \(k_1\), \(b_{\text{BM}}\) | BM25 term-saturation and length-normalisation parameters (Ch. 9) |
| \(T_e\), \(\mathcal L_{\text{con}}\) | contrastive temperature and loss for embeddings (Ch. 9) |
| \(k_{\text{rrf}}\) | reciprocal-rank-fusion constant (Ch. 9) |
| \(\zeta\) | score separation of a relevant item from distractors, in standard deviations (Ch. 9) |

## Cost and latency
| Symbol | Meaning |
|---|---|
| \(\kappa_{\text{in}}, \kappa_{\text{out}}, \kappa_{\text{cache}}\) | price per token of input, output and cached input (quoted per million tokens) |
| \(C\) | cost of a call, episode or workload in dollars |
| \(C_{\text{err}}\), \(C_{\text{appr}}\), \(p_{\text{catch}}\) | cost of a wrong action; cost of an approval; probability a reviewer catches a wrong action (Ch. 8) |
| \(\lambda\) | arrival rate of requests or tasks |
| \(\ell\) | latency of a call or an episode; \(\ell_{\text{tool}}\) of a tool call |
| \(\ell_{\text{model}}\), \(\Delta\ell\) | time of one model step; extra decode time per additional parallel call (Ch. 8) |
| \(\rho_{\text{tool}}\), \(n_r\) | per-attempt success probability of a tool call; maximum attempts (Ch. 8) |
| \(\eta\), \(w\), \(h\) | cache read price and write price relative to \(\kappa_{\text{in}}\); cache hit rate (Ch. 4) |
| \(v_{\text{pre}}, v_{\text{dec}}\) | prefill and decode speeds in tokens per second |

## Reference values (illustrative, used for arithmetic)
- Frontier model: \(\kappa_{\text{in}}=\$3\), \(\kappa_{\text{out}}=\$15\), \(\kappa_{\text{cache}}=\$0.30\) per million tokens; \(n_{\max}=200{,}000\); \(v_{\text{dec}}=60\) tokens/s; \(v_{\text{pre}}=5{,}000\) tokens/s.
- Small model: \(\kappa_{\text{in}}=\$0.25\), \(\kappa_{\text{out}}=\$1.25\) per million tokens; \(v_{\text{dec}}=150\) tokens/s.
- One English word ≈ 1.3 tokens; one page of prose ≈ 650 tokens.
