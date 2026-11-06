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
| \(\hat p\) | estimated success rate on \(m\) tasks |
| \(b\) | branching factor of a search tree |
| \(\epsilon\) | error rate (of a verifier, judge or step) |

## Retrieval and memory
| Symbol | Meaning |
|---|---|
| \(q\) | a query |
| \(\mathcal D\), \(d\) | a document collection; one document or chunk |
| \(e(\cdot)\), \(d_e\) | embedding map and embedding dimension |
| \(\operatorname{sim}(u,v)\) | similarity, usually cosine \(u^\top v/(\lVert u\rVert\lVert v\rVert)\) |
| \(K\) | number of retrieved items (top-\(K\)) |

## Cost and latency
| Symbol | Meaning |
|---|---|
| \(\kappa_{\text{in}}, \kappa_{\text{out}}, \kappa_{\text{cache}}\) | price per token of input, output and cached input (quoted per million tokens) |
| \(C\) | cost of a call, episode or workload in dollars |
| \(\lambda\) | arrival rate of requests or tasks |
| \(\ell\) | latency of a call or an episode; \(\ell_{\text{tool}}\) of a tool call |
| \(v_{\text{pre}}, v_{\text{dec}}\) | prefill and decode speeds in tokens per second |

## Reference values (illustrative, used for arithmetic)
- Frontier model: \(\kappa_{\text{in}}=\$3\), \(\kappa_{\text{out}}=\$15\), \(\kappa_{\text{cache}}=\$0.30\) per million tokens; \(n_{\max}=200{,}000\); \(v_{\text{dec}}=60\) tokens/s; \(v_{\text{pre}}=5{,}000\) tokens/s.
- Small model: \(\kappa_{\text{in}}=\$0.25\), \(\kappa_{\text{out}}=\$1.25\) per million tokens; \(v_{\text{dec}}=150\) tokens/s.
- One English word ≈ 1.3 tokens; one page of prose ≈ 650 tokens.
