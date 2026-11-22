# Research digest · 2026-11-22

Covers papers posted from about 2026-11-15 to 2026-11-22 (UTC).

> Relevance = TF-IDF cosine similarity to your interest description, plus a keyword bonus. It measures how close the wording is to what you care about, not how good a paper is. AI summaries are written from the abstract only; check the paper before relying on them.

## Must-read this week

- **[DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play](https://arxiv.org/abs/2611.24836v1)** (Embodied AI and robotics): Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models.
- **[From Pen-and-Paper to Machine-Checked Proofs: Lean for System Identification](https://arxiv.org/abs/2611.18220v1)** (AI for mathematics): Mathematical proofs in scientific papers are often long and intricate, relying on chains of references to earlier results.

## Machine learning theory

### [Bellman Residual Bracketing: Resolving the Sample Complexity of Discounted and Average-Reward RL](https://arxiv.org/abs/2611.19566v1)
*Matthew Zurek, Yudong Chen* · `cs.LG` · arXiv:2611.19566v1 · relevance 0.32

- **In one sentence**: We study the sample complexity of the empirical planning or plug-in approach for reinforcement learning (RL) with a generative model. (first sentence of the abstract; no AI summary)
- Matched keywords: sample complexity, minimax

<details><summary>Original abstract</summary>

We study the sample complexity of the empirical planning or plug-in approach for reinforcement learning (RL) with a generative model. We show the discounted plug-in approach finds an $\varepsilon$-optimal policy with $O(SA (1-γ)^{-3} \varepsilon^{-2} \log(SA/δ))$ samples, where $S, A, γ, δ$ are the state and action sizes, discount factor, and failure probability, respectively. In the average-reward setting, we show that discounted plug-in and direct (undiscounted) plug-in achieve $O(SAH\varepsilon^{-2}\log(SA/δ))$ and $O(SAD\varepsilon^{-2}\log(SA/δ))$ complexities, respectively, where $H$ upper-bounds the optimal bias span and $D$ is the diameter. Combining with our lower bounds for nonadaptive generative models, these results resolve the minimax sample complexity of discounted RL and average-reward RL --- in both the span- and diameter-based classes --- up to constant factors. Our main technical contribution is a novel Bellman residual bracketing technique which improves the efficiency of prior absorbing-MDP-based concentration analyses.

</details>

### [What Interpolators Store and What They Express: An Information-Theoretic Framework for Benign Overfitting and Label-Free Model Selection](https://arxiv.org/abs/2611.23630v1)
*Nikolaos Nikolaou* · `cs.LG` · arXiv:2611.23630v1 · relevance 0.31

- **In one sentence**: Overparameterized learners can fit noisy training labels perfectly and still predict well, which neither classical complexity measures nor information-theoretic generalization bounds explain. (first sentence of the abstract; no AI summary)
- Matched keywords: benign overfitting, double descent

<details><summary>Original abstract</summary>

Overparameterized learners can fit noisy training labels perfectly and still predict well, which neither classical complexity measures nor information-theoretic generalization bounds explain. We develop an information-theoretic framework that separates two things an interpolating learner does with its sample: storage, the information the trained model retains about its training labels, and expression, the information about the sample that reaches its predictions at fresh inputs. We first characterize the ideal model: for a loss l, the least complex l-sufficient representation is the Bayes act, whose entropy is the minimal sufficient complexity; this generalizes, and corrects, an earlier "lossless maximal compression" view of boosting. We then show that every interpolator stores exactly nH(Y|X) bits of label noise, so storage, and bounds built on it (including CMI bounds), cannot tell interpolators apart. Expression can: excess risk is bounded above and below by the expressed information V, the entropy over training samples of the prediction at an input, plus a modal-bias term, exactly so for binary labels. Benign overfitting is therefore vanishing expression, a picture that covers nearest-neighbour rules, averaging, minimum-norm least squares and double descent, and that links V to classical bias-variance decompositions and to model disagreement. Finally, V gives a model-selection criterion that needs no held-out labels. Among overparameterized learners on 15 noisy datasets, V estimated from two disjoint halves has 60% less regret than holdout validation at the same cost and matches 5-fold cross-validation at a quarter of its cost; at matched cost it also beats selection by conditional mutual information. We characterize when it fails and give remedies. Code: https://github.com/nnikolaou/GLMC

</details>

### [Offline KL-Regularized Reinforcement Learning with Stochastic Transitions](https://arxiv.org/abs/2611.17603v1)
*Andrew Liu* · `cs.LG` · arXiv:2611.17603v1 · relevance 0.25

- **In one sentence**: KL-regularized reinforcement learning is the objective behind RL fine-tuning of language models, and its data are often collected by the reference policy itself. (first sentence of the abstract; no AI summary)
- Matched keywords: sample complexity, minimax

<details><summary>Original abstract</summary>

KL-regularized reinforcement learning is the objective behind RL fine-tuning of language models, and its data are often collected by the reference policy itself. However, beyond bandits and deterministic transitions, little is known about how much offline data it needs. In this work, we study finite discounted Markov decision processes with unknown stochastic transitions, $K$ state-action pairs and effective horizon $H$. For data that cover the regularized optimum with concentrability $C\geq 4$, every estimator needs $Ω(KCH^3/(ε\max\{ε,β\}))$ samples on some instances when $ε$ is small, where $β$ is the temperature. Under a fixed design, pessimistic soft value iteration with a variance-aware penalty attains this rate with high probability, up to logarithmic factors, when $β\geq 1.4H$. When the data come from the reference policy itself, we show that it covers the optimum up to a power law whose exponent grows as $H/β$; in the same temperature range, this power law alone gives the estimator a sample complexity polynomial in $1/ε$, with no coverage assumption. For $β\geq H$ the power can also increase the sample size needed by a factor polynomial in $1/ε$. Finally, the plug-in estimator, which is minimax optimal with a generative model, can fail on reference data at small temperatures when many actions are rarely seen, while the pessimistic estimator does not.

</details>

## Probability

### [Existence and Uniqueness of Mild Solutions to Rough Stochastic Partial Differential Equations driven by Fractional Brownian Motion with Hurst Index $H > 1/4$](https://arxiv.org/abs/2611.26580v1)
*Maksim Vaskouski, Maksim Firsau* · `math.PR` · arXiv:2611.26580v1 · relevance 0.22

- **In one sentence**: In this paper we prove a theorem on the unique solvability of the Cauchy problem for a stochastic partial differential equation driven by the fractional Brownian motion with Hurst index $H>\frac{1}{4}$. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

In this paper we prove a theorem on the unique solvability of the Cauchy problem for a stochastic partial differential equation driven by the fractional Brownian motion with Hurst index $H>\frac{1}{4}$.

</details>

### [Convergence of replicator-mutator particle systems via bounded Wasserstein distance](https://arxiv.org/abs/2611.24472v1)
*Giacomo Borghi* · `math.PR` · arXiv:2611.24472v1 · relevance 0.21

- **In one sentence**: Interacting particle systems with selection and mutation mechanisms arise in biological modeling, evolutionary optimization, and particle filtering methods. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Interacting particle systems with selection and mutation mechanisms arise in biological modeling, evolutionary optimization, and particle filtering methods. In this work we will consider the paradigmatic replicator-mutator PDE, which combines a diffusive component with a source term that depends on an external potential. We derive quantitative error estimates for the distance between the empirical measure of an unweighted particle system and the solution of the PDE. The proof uses a Wasserstein-1 distance with a bounded ground cost, which allows us to treat unbounded potentials on an unbounded state space. The key tools are the optimal coupling of newly resampled particles and, for the time-continuous limit, the use of a discrete-time killing resampling.

</details>

### [Parameter estimation for discretely observed rough fractional interacting particle systems](https://arxiv.org/abs/2611.24287v1)
*Chiara Amorino, Augustin Puel, Radomyra Shevchenko* · `math.ST` · arXiv:2611.24287v1 · relevance 0.21

- **In one sentence**: We study parametric inference for interacting particle systems driven by independent fractional Brownian motions, based on discrete observations of all particles over a fixed time horizon. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

We study parametric inference for interacting particle systems driven by independent fractional Brownian motions, based on discrete observations of all particles over a fixed time horizon. Our goal is to estimate an unknown drift parameter in the joint limit as the number of particles increases and the observation mesh vanishes. For $H>\frac 12$, we construct contrast based estimators by extending the discrete time least squares approach of Neuenkirch and Tindel to the interacting setting. For the rough regime $H\in(\frac 14,\frac 12)$, we introduce a modified contrast and use the stochastic sewing lemma to handle the first order approximations available from discrete observations. Our analysis combines the propagation of chaos for the associated fractional McKean Vlasov equation with estimates controlling the temporal discretization error. When the Hurst parameter and the diffusion coefficient are known, we establish strong consistency and asymptotic normality of the proposed estimators. The asymptotic results reveal an interplay between the number of particles and the temporal discretization: the convergence rate with respect to the observation mesh changes at $H=\frac 34$, while the asymptotic normality holds in both regimes considered. We further develop a joint estimation procedure for the drift parameter, the Hurst parameter, and the diffusion coefficient, extending quadratic-variation methods for fractional Brownian motion to the interacting particle framework. Numerical experiments illustrate the performance of the proposed estimators.

</details>

## Differential geometry

### [Displaceability of monotone Lagrangians in $\mathbb{C}P^3(\sqrt{2})$ and $Q^4(\sqrt{2})$](https://arxiv.org/abs/2611.25699v1)
*Han Lou, Shuo Zhang* · `math.SG` · arXiv:2611.25699v1 · relevance 0.25

- **In one sentence**: We show that the generalized Polterovich submanifold $L_{0, 2}^P$ in $\mathbb{C}P^3(\sqrt{2})$ and the Chekanov-Oakley-Usher Lagrangian $L_{1, 2}^{Q, \mathrm{Ch}}$ in the quadric $Q^4(\sqrt{2})$ are displaceable. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

We show that the generalized Polterovich submanifold $L_{0, 2}^P$ in $\mathbb{C}P^3(\sqrt{2})$ and the Chekanov-Oakley-Usher Lagrangian $L_{1, 2}^{Q, \mathrm{Ch}}$ in the quadric $Q^4(\sqrt{2})$ are displaceable. Since $L_{0, 2}^P$ and $L_{1, 2}^{Q, \mathrm{Ch}}$ are in the zero level set of the moment maps of the $\mathrm{SO}(3)$-actions on $\mathbb{C}P^3(\sqrt{2})$ and $Q^4(\sqrt{2})$, the main idea is to construct Hamiltonian diffeomorphisms mapping $L_{0, 2}^P$ and $L_{1, 2}^{Q, \mathrm{Ch}}$ to nonzero level sets of the moment maps.

</details>

### [Equivariant Flow Matching on Homogeneous Spaces](https://arxiv.org/abs/2611.22492v1)
*Finn M. Sherry, Gijs Bellaard* · `math.DG` · arXiv:2611.22492v1 · relevance 0.19

- **In one sentence**: Flow matching enables the training of networks that can flow samples from an initial to a target distribution. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Flow matching enables the training of networks that can flow samples from an initial to a target distribution. The network is regressed against simple vector fields that are conditioned on end points in the target distribution. In the Euclidean case, these conditional vector fields induce flows along straight lines. Various generalisations have been proposed to perform flow matching on spaces where straight lines are not well-defined, such as Riemannian manifolds and Lie groups. Riemannian flow matching applies to many domains, but typically requires expensive simulation, while flow matching on Lie groups is simulation-free but only works on Lie groups. In this work, we develop equivariant flow matching on homogeneous spaces, which generalises flow matching on Lie groups, while remaining simulation-free. We also derive all generators connecting pairs of position-orientations, generalising, and perform a similar derivation for event-velocity space, the Lorentzian analogue of position-orientation space, so that we can perform flow matching on these spaces.

</details>

## Mathematical physics

### [Link invariants in nilpotent group gauge theories](https://arxiv.org/abs/2611.18237v1)
*Thomas Nicosanti, Pavel Putrov, Johann Quenta-Raygada* · `hep-th` · arXiv:2611.18237v1 · relevance 0.20

- **In one sentence**: We consider 3-dimensional topological gauge theories with nilpotent gauge groups, both finite, that is Dijkgraaf-Witten theories, and continuous, that is Chern-Simons theories. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

We consider 3-dimensional topological gauge theories with nilpotent gauge groups, both finite, that is Dijkgraaf-Witten theories, and continuous, that is Chern-Simons theories. Abelian topological quantum field theories are exactly those which do not detect the Borromean rings, and nilpotent gauge groups provide the natural next steps beyond the abelian case. We show that the untwisted Dijkgraaf-Witten theory with gauge group $G$ detects Brunnian links with up to $n+1$ components, but no Brunnian links with more components, if and only if $G$ is $n$-step nilpotent. Moreover, the expectation values of such links are determined by their Milnor invariants. We also study the properties of Chern-Simons theories with nilpotent Lie groups and draw parallels with those of the Dijkgraaf-Witten theories. Finally, we conjecture, using the Lazard correspondence, a relation between expectation values of line operators in the two types of theories, and test it in examples.

</details>

### [On the Power-Law Duality in Wigner-Yang Quantum Mechanics](https://arxiv.org/abs/2611.19246v1)
*Georg Junker, Hassan Hassanabadi* · `math-ph` · arXiv:2611.19246v1 · relevance 0.20

- **In one sentence**: In this work we first revisit the Hooke-Newton duality and its generalisation to arbitrary power laws in classical and quantum mechanics. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

In this work we first revisit the Hooke-Newton duality and its generalisation to arbitrary power laws in classical and quantum mechanics. We then consider Wigner-Yang quantum mechanics on the real line, which is a deformation of standard Heisenberg-Schrödinger quantum mechanics closely related to Dunkl's differential-difference operator formalism. We consider the corresponding eigenvalue problem for the harmonic potential and a Coulomb-like potential. We observe that the Hooke-Newton duality is also applicable to these deformed quantum systems allowing us to solve the eigenvalue problem of one by mapping it onto the other system. This approach is then generalised to arbitrary power-law potentials in Wigner-Yang quantum mechanics. Whereas in standard quantum mechanics the classical re-scaling of angular momenta has to be applied to Langer-modified quantum angular momenta, Wigner-Yang quantum mechanics requires a rescaling of deformation parameters similar to the Langer-type modification but involving the reflection operator. The energy coupling-constant exchange, however, remains the same in all three cases, classical mechanics, quantum mechanics and Wigner-Yang quantum mechanics.

</details>

## Complex analysis

### [The Holomorphic Reduction of Pseudoconvex Homogeneous Manifolds](https://arxiv.org/abs/2611.24922v1)
*Bruce Gilligan* · `math.CV` · arXiv:2611.24922v1 · relevance 0.20

- **In one sentence**: Suppose $G$ is a connected complex Lie group and $H$ is a closed complex subgroup. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Suppose $G$ is a connected complex Lie group and $H$ is a closed complex subgroup. Then there exists a closed complex subgroup $J$ of $G$ containing $H$ such that the fibration $π:G/H \to G/J$ is the holomorphic reduction of $G/H$, i.e., $G/J$ is holomorphically separable and ${\mathcal O}(G/H) \cong π^*{\mathcal O}(G/J)$. In this paper we prove that if $G/H$ is pseudoconvex, i.e., if $G/H$ admits a continuous plurisubharmonic exhaustion function, then $G/J$ is Stein and $J/H$ has no non-constant holomorphic functions.

</details>

### [On the solution of a question for meromorphic functions sharing three values IM and a fourth value CM in the complex plane](https://arxiv.org/abs/2611.25948v1)
*Xiao-Min Li, Jun Wang, Hong-Xun Yi* · `math.CV` · arXiv:2611.25948v1 · relevance 0.14

- **In one sentence**: In 1926, Nevanlinna (Acta Math. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

In 1926, Nevanlinna (Acta Math. {\bf 48} (1926), no. 3-4, 367-391) proved that if two distinct and non-constant meromorphic functions $f$ and $g$ share $a_1,$ $a_2,$ $a_3,$ $a_4$ CM in the complex plane, where $a_1,$ $a_2,$ $a_3,$ $a_4$ are four distinct complex values in the extended complex plane, then $f$ is a Möbius transformation of $g$, two of the shared values, say $a_1$ and $a_2$, are Picard exceptional values, and the cross ratio $\left(a_1, a_2, a_3, a_4\right)=-1.$ Later on, Gundersen (Trans. Amer. Math. Soc. {\bf 277} (1983), no. 2, 545-567. Correction: {\bf 304} (1987), 847-850) proved that if two non-constant meromorphic functions share two values CM and share two other values IM, then the functions share all four values CM. In 1992, Gundersen (Complex Var. Elliptic Equ. {\bf 20} (1992), no. 1-4, 99-106) proposed the following famous question: if two non-constant meromorphic functions share three distinct values IM and share a fourth value CM, then do the functions necessarily share all four values CM? This question is a long-standing question in the studies of the Nevanlinna's value distribution theory of meromorphic functions, and has not been completely resolved by now. In this paper, we completely resolve the question, and prove that if two distinct and non-constant meromorphic functions $f$ and $g$ share $a_1,$ $a_2,$ $a_3$ IM and $\infty$ CM, where $a_1,$ $a_2,$ $a_3$ are three distinct and finite complex values in the complex plane, then $f$ and $g$ also share $a_1,$ $a_2,$ $a_3$ CM.

</details>

## AI for mathematics

### [From Pen-and-Paper to Machine-Checked Proofs: Lean for System Identification](https://arxiv.org/abs/2611.18220v1)
*Manas Mejari, Dario Piga, Marco Forgione* · `eess.SY` · arXiv:2611.18220v1 · relevance 0.37

- **In one sentence**: Mathematical proofs in scientific papers are often long and intricate, relying on chains of references to earlier results. (first sentence of the abstract; no AI summary)
- Matched keywords: Lean, theorem proving, formalization, proof assistant

<details><summary>Original abstract</summary>

Mathematical proofs in scientific papers are often long and intricate, relying on chains of references to earlier results. This makes it difficult for readers and reviewers to verify each and every step. Interactive theorem proving offers a complement: the theorem and its proof are written as code, and every inference is checked by a small, trusted piece of software called the kernel. This paper serves as an introduction to the Lean 4 proof assistant for a system identification and control audience, assuming no prior exposure to formal methods. We first show how a Lean proof is read using two elementary examples: the first on identifiability, the second on set invariance. We then illustrate how Lean can be used to analyse results from the literature, taking as example a classic lemma on the inversion of the noise filter in prediction-error identification (Ljung, 1999, Lemma 3.1). Since in Lean every step must be justified, the formalization brings to light a subtle point: the original claim of that lemma holds almost surely, although not for every realisation, as its statement may suggest. A simple counterexample makes this concrete. Finally, the paper discusses guidelines and perspectives on the use of Lean in system identification research.

</details>

### [Turing Agent: Agentic Formal Verification for Mathematical Research](https://arxiv.org/abs/2611.21299v1)
*Yang Chen, Qianyi Wang, Ronghui Yang et al.* · `cs.AI` · arXiv:2611.21299v1 · relevance 0.27

- **In one sentence**: Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. (first sentence of the abstract; no AI summary)
- Matched keywords: formalization, formal verification

<details><summary>Original abstract</summary>

Large language models (LLMs) are rapidly advancing mathematical discovery, moving beyond benchmark-level problem solving to tackle frontier research problems. This progress is ushering mathematics into an era of proof abundance, raising a fundamental challenge: how can we ensure the correctness of the ever-growing volume of AI-generated proofs and transform them into trustworthy, machine-verified mathematical knowledge? We introduce Turing Agent, an agent harness designed to orchestrate end-to-end formal verification of research-level mathematics. Its wo-scale architecture integrates theorem formalization and proof formalization agents, empowered by structured proof decomposition, parallel verification, accumulated proof experience, and selective semantic review. Leveraging our collaborations with theoretical computer science (TCS) researchers, we focus our evaluation on TCS, a particularly demanding domain characterized by intricate quantification, complex dependencies, and stringent semantic requirements. Against direct generation and general-purpose coding harnesses, including Codex CLI and Claude Code, Turing Agent achieves approximately 57-62% faithful formalization success on Formal TCS Bench and 83% overall pass@1 on a TCS-focused subset of RLMEval, using GLM-5.3 and DeepSeek-V4-Pro. Notably, Turing Agent, built on DeepSeek, successfully completes the formal verification of three previously unresolved TCS tasks from OpenAI's October 2026 collection. One particularly challenging TCS problem required about a hundred formally verified auxiliary claims. Moreover, by actively exploring and refining the formalization process, Turing Agent can uncover simpler alternative proofs, expose unnecessary dependencies in original proofs, and generate reusable mathematical knowledge as a byproduct of verification.

</details>

### [How rigid is maximum cardinality search? Stability and locality of MCS orderings under edge updates, verified in Lean](https://arxiv.org/abs/2611.18369v1)
*Md Thoriqul Islam Thonmay, Gregory Morse* · `cs.DS` · arXiv:2611.18369v1 · relevance 0.22

- **In one sentence**: For which sets F of edge modifications do a graph G and the modified graph share a maximum cardinality search (MCS) ordering? (first sentence of the abstract; no AI summary)
- Matched keywords: Lean, mathlib

<details><summary>Original abstract</summary>

For which sets F of edge modifications do a graph G and the modified graph share a maximum cardinality search (MCS) ordering? We prove that they do whenever, along every proper common MCS prefix, each unchosen vertex's neighbour count in the second graph exceeds its count in the first by zero or one. In particular, inserting or deleting any matching, or flipping a single edge, preserves a common ordering, and under the same hypothesis every common MCS prefix extends to a full common ordering without backtracking. Neither part of the hypothesis can simply be dropped: inserting a triangle, a P_4 or a 2P_3 shows that the +1 bound cannot be relaxed to +2, and a disjoint mixed insert/delete pair shows that the one-directional condition is needed. For the canonical ordering (smallest-index tie-breaking) under a single-edge update, an insertion can first change the ordering only strictly between the endpoints' positions, and a deletion only at the later endpoint; when no break fires, the ordering is unchanged. A boolean-adjacency executable refines the abstract probe-then-repair update. All of these results, including the four obstructions, are proved in Lean 4 over Mathlib, re-checked by independent kernel checkers, and registered in the Palomar registry. On paper we further show that the first break of an insertion is located in O((deg(v)+1) log n) time, independent of the window length. We claim no worst-case asymptotic speedup over recomputation.

</details>

## Embodied AI and robotics

### [DiWALI: Diffusion Policy Learning in World Models via Latent Action Inference from Human and Robot Play](https://arxiv.org/abs/2611.24836v1)
*Akshay L Chandra, Iman Nematollahi, Lingyue Zhao et al.* · `cs.RO` · arXiv:2611.24836v1 · relevance 0.38

- **In one sentence**: Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. (first sentence of the abstract; no AI summary)
- Matched keywords: manipulation, world model, reinforcement learning

<details><summary>Original abstract</summary>

Learning robot manipulation is constrained by the availability of action-labeled robot data, for both imitation and world models. Humans can demonstrate skills in seconds, but their demonstrations lack the required robot actions. We introduce DiWALI, a framework that learns and improves diffusion policies within a world model trained on human and robot play. DiWALI infers latent actions from consecutive frames using an inverse dynamics model, enabling world model training without action labels, and grounds them in robot commands through a decoder trained separately on robot play. Skill policies are trained over latent actions from action-free human demonstrations and improved with reinforcement learning in imagination. On the CALVIN benchmark, DiWALI policies trained solely from human demonstrations substantially outperform baselines trained with robot demonstrations. Incorporating human play into the world model training also yields stronger policies after fine-tuning than using the same amount of robot play alone. Experiments on a physical robot show that skills learned primarily from human demonstrations are further improved in imagination with a world model trained on human and robot play. Together, these results demonstrate that human experience can support both manipulation skill acquisition and subsequent policy improvement, reducing reliance on action-labeled robot data. Videos, dataset and code are available at https://diwali.cs.uni-freiburg.de.

</details>

### [JEPA4R: Embodied JEPA World Models with 4D Point Planning](https://arxiv.org/abs/2611.19771v1)
*Jiarui Dong, Zhiheng Liang, Yanjun Li et al.* · `cs.RO` · arXiv:2611.19771v1 · relevance 0.37

- **In one sentence**: Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. (first sentence of the abstract; no AI summary)
- Matched keywords: embodied, manipulation, world model

<details><summary>Original abstract</summary>

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. Two challenges remain: 2D images leave the metric geometry that manipulation acts on implicit and entangled with appearance, and what these models imagine stays hidden, as they are mostly judged in simulation by short-horizon latent planning. We present JEPA4R, a JEPA world model that observes single-depth-camera point clouds, predicts and plans in their latent space, and acts through a policy head on its frozen latents; we call this 4D point planning. A decoder on the frozen world model shows what it imagines as 4D point clouds, with a mean point error within 1.1 cm over 200 steps. Under the policy-learning protocols of OGBench and CortexBench, JEPA4R leads pixel JEPA models on OGBench Cube-Single, Cube-Double, Cube-Triple and Scene, and ranks first on MetaWorld and Adroit Relocate with 98.4% and 88.0%, above the runner-up, R3M, at 96.0% and 65.3%. Trained only in a digital twin, JEPA4R and its policy heads run zero-shot on the real arm with both a gripper and a dexterous hand.

</details>

## Theoretical physics

### [Nonequilibrium Statistical Mechanics: Physical Concepts & Mathematical Tools](https://arxiv.org/abs/2611.26394v1)
*Sagar Chakraborty* · `cond-mat.stat-mech` · arXiv:2611.26394v1 · relevance 0.23

- **In one sentence**: As anything not in equilibrium is, by definition, nonequilibrium, there is no universally agreed-upon set of topics that can constitute an exhaustive presentation of nonequilibrium statistical mechanics. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

As anything not in equilibrium is, by definition, nonequilibrium, there is no universally agreed-upon set of topics that can constitute an exhaustive presentation of nonequilibrium statistical mechanics. At the same time, nonequilibrium statistical mechanics has transcended traditional physics to become a powerful language for complex systems. Prompted by an enthusiastic curiosity about complex systems, these cursory lecture notes attempt to elucidate some introductory concepts and techniques used in classical nonequilibrium statistical mechanics, which find successful applications not only in foundational physics, but also across other fields such as biology, ecology, economics, and sociology. Except for the specific synthesis and presentation of the material, which assumes basic familiarity with equilibrium statistical mechanics, the author claims no originality.

</details>

### [An infrared-safe $S$-matrix for $\mathcal N=4$ super Yang-Mills](https://arxiv.org/abs/2611.21713v1)
*Maria Nocchi, Leonardo Rastelli* · `hep-th` · arXiv:2611.21713v1 · relevance 0.19

- **In one sentence**: Scattering amplitudes of massless gauge theories are not observables: they are infrared divergent, and the standard regulators are tied either to perturbation theory or the planar limit. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Scattering amplitudes of massless gauge theories are not observables: they are infrared divergent, and the standard regulators are tied either to perturbation theory or the planar limit. We study $\mathcal N=4$ super Yang-Mills theory on rigid AdS$_4$ with Dirichlet boundary conditions, where the role of the amplitude is played by correlation functions of boundary operators. These are finite, and they are defined at any coupling and for any gauge group. Among them, the four-point function of the flavor-current supermultiplet is the counterpart of the $2\to2$ amplitude of the elementary supergluon states, and arguably the simplest non-trivial observable of the theory. In this paper, we compute it at weak coupling to one loop. The tree-level correlator follows directly from the microscopic theory, and the one-loop correlator, which we obtain from AdS unitarity, takes a remarkably simple form in Mellin space. In the flat-space limit, it reproduces the one-loop scattering amplitude, with the infrared divergences re-emerging as logarithms.

</details>

## Chemistry and materials

### [Reward misalignment as an opportunity for materials discovery](https://arxiv.org/abs/2611.26186v1)
*Ryotaro Okabe, Shoki Kishida, Abhijatmedhi Chotrattanapituk et al.* · `cond-mat.mtrl-sci` · arXiv:2611.26186v1 · relevance 0.17

- **In one sentence**: Reward misalignment is usually regarded as a failure of artificial intelligence. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Reward misalignment is usually regarded as a failure of artificial intelligence. In materials discovery with generative AI models, however, disagreement between predefined rewards and expert judgment may reveal materials that the rewards overlook. We investigate this possibility using electronic flat bands as a prime example. Experts mostly agree with a numerical bandwidth score, but their disagreements are systematic and cannot be explained by an estimated 5% rate of mistaken labels. We learn the experts' preferences from pairwise comparisons and use them to guide a crystal diffusion model. The learned preferences and numerical score agree on the flattest bands but diverge elsewhere. For example, the preferences favor KCo2As2 and CoGa, reported compounds with partially flat bands that the score would discard. The framework also extends to synthesizability and phonon properties. Our findings suggest that reward misalignment can expose opportunities for materials discovery beyond what fixed rewards are designed to find.

</details>

### [Application of Pretrained Universal Machine Learning Force-Fields for Phase Transitions Prediction in ZrO2](https://arxiv.org/abs/2611.23535v1)
*Rajan Khadka, Axel van de Walle, Patrick Tepesch* · `cond-mat.mtrl-sci` · arXiv:2611.23535v1 · relevance 0.16

- **In one sentence**: Pretrained universal machine-learning force fields can reduce the cost of finite-temperature molecular dynamics relative to density functional theory. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Pretrained universal machine-learning force fields can reduce the cost of finite-temperature molecular dynamics relative to density functional theory. However, most benchmarks test only static properties and do not assess whether these models reproduce the correct phase-transition sequence. Here, we benchmark ten open-source universal machine-learning force fields for zirconia (ZrO$_2$) using phonon dispersion calculations and variable-cell isothermal-isobaric molecular dynamics. Zirconia is a useful test because it has three thermodynamically stable crystalline phases prior to melting, following the sequence monoclinic-tetragonal-cubic. Four models reproduce this sequence: 7net-l3i5, MatterSim-v1.0.0-1M, MACE-mpa, and MACE-D3. Models with orthorhombic-tetragonal energy errors above about 10 meV/atom (7net-0, CHGNet, and MACE) instead produce an orthorhombic intermediate and predict monoclinic-orthorhombic-tetragonal-cubic-liquid upon heating. ORB-based models fail to sustain stable variable-cell dynamics because their phonon frequencies are compressed by 30-60% relative to the density functional theory reference. Across all ten models, two ground-state diagnostics predict finite-temperature behavior. Relative polymorph energetics should agree with the matched density functional theory reference within about 6 meV/atom, and the phonon spectrum should not show systematic softening. These diagnostics are practical screening metrics for assessing pretrained force fields for phase-transition predictions.

</details>

## Computational and systems biology

### [Constructing Gene Regulatory Network using Chatterjee's Rank Correlation with Single-cell Transcriptomic Data](https://www.biorxiv.org/content/10.1101/2025.09.17.676530v4)
*Gupta, S.; Chaudhuri, A.; Raghuraman, V. et al.* · `bioinformatics` · bioRxiv doi:10.1101/2025.09.17.676530 v4 · relevance 0.17

- **In one sentence**: Constructing gene regulatory networks (GRNs) from single-cell RNA sequencing (scRNA-seq) data is critical for understanding cellular systems, yet existing methods rely either on strong modeling assumptions or on computationally intensive algorithms. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Constructing gene regulatory networks (GRNs) from single-cell RNA sequencing (scRNA-seq) data is critical for understanding cellular systems, yet existing methods rely either on strong modeling assumptions or on computationally intensive algorithms. We introduce a multiple testing framework for GRN construction based on Chatterjee's rank correlation coefficient, a nonparametric measure of dependence that captures non-linear and non-monotone relationships. The framework overcomes several limitations of traditional methods by offering a transparent, scalable, and computationally efficient alternative to recent black-box machine learning models. Because cells in scRNA-seq data are not independent observations, we develop a data-driven algorithm for estimating robust testing cutoffs. We further exploit the asymmetric nature of Chatterjee's correlation to propose a new test for asymmetric predictive associations, yielding biologically meaningful and directionally informed GRNs. In simulations, our method matches or outperforms state-of-the-art approaches in recovering true gene-gene dependencies and asymmetric associations, particularly for complex, non-linear dependencies. Application to real scRNA-seq data shows its utility for dissecting complex regulatory networks.

</details>

### [DRAFT: graph-recurrent learning of dynamic gene regulatory networks along single-cell multi-omics trajectories](https://www.biorxiv.org/content/10.64898/2026.11.17.767145v1)
*Zhang, Z.; Santhi Sekhar, P.; van Nierop y Sanchez, P. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.17.767145 v1 · relevance 0.16

- **In one sentence**: Single-cell multi-omics data offer an opportunity to resolve how gene regulatory networks (GRNs) are rewired during cell-fate transitions, but most existing methods infer static snapshots, ignore temporal dependencies or assume linear regulation. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Single-cell multi-omics data offer an opportunity to resolve how gene regulatory networks (GRNs) are rewired during cell-fate transitions, but most existing methods infer static snapshots, ignore temporal dependencies or assume linear regulation. Here we present DRAFT, a deep learning framework that combines graph attention with recurrent temporal memory to infer dynamic GRNs from time-resolved single-cell multi-omics data. On simulated data, DRAFT outperforms existing methods in accuracy and temporal smoothness. In mouse cellular reprogramming and Drosophila adult spermatogenesis, it recovers interactions supported by independent ChIP-seq, perturbation and Hi-C data, together with known stage-specific regulators. By inferring regulatory activity from dynamic network structure rather than expression alone, DRAFT identifies regulators whose activity precedes their transcriptional peak, including the candidate early germline regulator Mondo. Germline-specific Mondo knockdown alters germline stem cell number and expression of the predicted targets kuz and mamo. DRAFT also enables nonlinear alignment of co-developing lineages and reveals stage-specific cell-cell communication.

</details>

### [Gene network topologies for heterogeneity restoration during self-renewal](https://www.biorxiv.org/content/10.64898/2026.11.16.767011v1)
*Chakravarty, S.; Ramarolahy, R. T. C.; Hong, T.* · `systems biology` · bioRxiv doi:10.64898/2026.11.16.767011 v1 · relevance 0.16

- **In one sentence**: The ability for a subset of cells to establish a heterogeneous cell population with multi-lineage competency is crucial for the self-renewal capacity of tissues and organs. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

The ability for a subset of cells to establish a heterogeneous cell population with multi-lineage competency is crucial for the self-renewal capacity of tissues and organs. Restoration of heterogeneous gene expression patterns has been observed in pluripotent and multi-potent stem cells, and the heterogeneity restoration can influence the potential of differentiation into multiple cell types. Similarly, cancer cells can acquire the capacity to establish non-genetic heterogeneity that plays a role in cancer progression and resistance to therapeutics. Specific models of gene regulatory networks have been proposed to explain heterogeneity restoration. However, due to the lack of systematic analysis, it is unclear which network topologies are more efficient for this multicellular function, and what intrinsic and extrinsic factors can determine the optimal choice of network topology. In this work, we use mathematical models describing gene expression of single cells and their underlying population dynamics to examine the influence of network topology on the recovery of multimodal expression patterns originating from a homogeneous population. We found that feedback loops are a key factor contributing to heterogeneity restoration. Negative and positive feedback loops support the existence of heterogeneity restoration, but only positive feedback can accelerate the process with low cost of single-cell-level variations of expression. Furthermore, networks with mixed feedback were the most robust ones for heterogeneity restoration with respect to changes in both kinetic rate constants and noise levels. Using experimentally validated network databases, we showed that genes involved in feedback loops are enriched with functions related to cell fate decisions, and we identified examples of realistic gene regulatory networks cell fate dynamics. Our results suggest multiple potential evolutionary paths towards gene circuits governing heterogeneity restoration and key factors contributing to the dynamics of this process. We expect that this systematic study will enable future discoveries of new gene regulatory networks governing progenitor and cancer cell dynamics as well as therapeutic strategies targeting heterogeneity-enabling circuits.

</details>

## Economics

### [Aggregating Rankings of Coalitions to Rank Individuals](https://arxiv.org/abs/2611.19021v1)
*Takahiro Suzuki* · `econ.TH` · arXiv:2611.19021v1 · relevance 0.17

- **In one sentence**: We develop an ordinal framework for aggregating a profile of rankings of coalitional performances to determine the ranking of individuals. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

We develop an ordinal framework for aggregating a profile of rankings of coalitional performances to determine the ranking of individuals. From university ratings to the assessment of team-sports players, we often evaluate individuals based on their coalitional performances. Although such evaluation has been addressed by cooperative game theory, it is only recently that its ordinal counterpart, social ranking theory (Moretti, 2015), has emerged. As most of the literature considers a single coalitional ranking (which corresponds to a real-valued characteristic function), we extend the model to allow a profile of coalitional rankings (which corresponds to a multidimensional characteristic function). We tackle the aggregation problem by introducing three families of inter-profile axioms, each representing how the rankings should interact or contribute to the output. After revealing fundamental impossibilities concerning the reconciliation of different families, we characterize a new solution, Pareto-extension Lex-cel (PEL), via some weaker versions of the inter-profile axioms. PEL extends Lex-cel, which is a central solution in social ranking theory, by analogy with Sen's Pareto extension rule. Our results develop the connection between classical Arrovian aggregation, cooperative game theory, and social ranking theory.

</details>

### [Menu Design Meets Market Design: Strategic Simplicity vs. Choice Complexity](https://arxiv.org/abs/2611.17984v1)
*Gian Caspari, Paul Ergün Hild, Michael Hilweg-Waldeck et al.* · `econ.GN` · arXiv:2611.17984v1 · relevance 0.12

- **In one sentence**: Strategic simplicity removes the incentive to misreport preferences, but it does not ensure that participants can identify what they prefer. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

Strategic simplicity removes the incentive to misreport preferences, but it does not ensure that participants can identify what they prefer. We study this distinction in a laboratory experiment on serial dictatorships, where optimal play only requires choosing one's favorite bundle of real-effort tasks. Participants make fifteen incentivized choices among bundles that vary in how many tasks they combine. They choose either from a large menu or through a series of binary choices. Having made all choices, they unexpectedly reconsider each assignment against a previously rejected alternative. We find that roughly one in six choices is reversed and almost one in five involves an objectively dominated bundle. Simplifying the choice architecture does not help. Binary decomposition even raises reversal rates among low-ability participants and further inflates their confidence about their choices.

</details>

### [Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data](https://arxiv.org/abs/2611.22984v1)
*Nan Liu, Yanbo Liu, Yuya Sasaki et al.* · `econ.EM` · arXiv:2611.22984v1 · relevance 0.11

- **In one sentence**: This paper studies the identification, estimation, and inference of long-term quantile treatment effects (LTQTEs) when short-term experimental data are supplemented with long-term observational data. (first sentence of the abstract; no AI summary)

<details><summary>Original abstract</summary>

This paper studies the identification, estimation, and inference of long-term quantile treatment effects (LTQTEs) when short-term experimental data are supplemented with long-term observational data. Under a latent unconfoundedness framework, we establish identification of the LTQTE curve and derive the corresponding efficient influence functions. Building on these influence functions, we propose a semiparametrically efficient estimation procedure and develop a multiplier bootstrap method for uniform inference on the LTQTE curve, yielding valid simultaneous confidence bands over a continuum of quantile indices.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Machine learning theory | 75 | 75 | 3 |
| Probability | 184 | 184 | 3 |
| Differential geometry | 150 | 150 | 2 |
| Mathematical physics | 258 | 258 | 2 |
| Complex analysis | 53 | 53 | 2 |
| AI for mathematics | 140 | 140 | 3 |
| Embodied AI and robotics | 278 | 278 | 2 |
| Theoretical physics | 494 | 494 | 2 |
| Chemistry and materials | 291 | 291 | 2 |
| Computational and systems biology | 524 | 524 | 3 |
| Economics | 89 | 89 | 3 |
