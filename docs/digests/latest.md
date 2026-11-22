# Research digest · 2026-11-22
<!-- {% raw %} -->

New papers posted from about 2026-11-21 to 2026-11-22 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Gene regulatory networks and the organization of cell differentiation in multicellular organisms](https://www.biorxiv.org/content/10.64898/2026.11.18.767571v1)** (Computational and systems biology): Across their development, clonal multicellular organisms generate new cell types from less differentiated cell types.
- **[Bianchi cosmologies with four-dimensional groups of motion in New General Relativity](https://arxiv.org/abs/2611.26474v1)** (Theoretical physics): We study the dynamics of the most general metric teleparallel spacetimes of Bianchi types II, III and IX, which admit a four-dimensional symmetry group, in the 1-parameter family of New General Relativity.
- **[Conformal parity](https://arxiv.org/abs/2611.25497v1)** (Differential geometry): We call a Riemannian metric on a four-manifold, as well as the underlying conformal structure, conformally even/odd if its self-dual and anti-self- dual Weyl tensors acting on bivectors have, at each point, equal/opposite spectra.

## Machine learning theory

### [Differentially Private Score Estimation with Applications to Score-Based Generative Models](https://arxiv.org/abs/2611.25536v1)
*Mengxiao Gao, Elly K. H. Hung, Yuchen Wu et al.* · `stat.ML` · arXiv:2611.25536v1 · relevance 0.25

- **In one sentence**: Estimating the score function of a distribution plays a central role in statistics and machine learning, with applications in distribution estimation, sampling, and score-based generative modeling. (first sentence of the abstract; AI summaries are off)
- Matched keywords: minimax, score-based

<details><summary>Original abstract</summary>

Estimating the score function of a distribution plays a central role in statistics and machine learning, with applications in distribution estimation, sampling, and score-based generative modeling. However, learning scores from sensitive data raises privacy concerns. These concerns are particularly pronounced in score-based generative modeling, where trained models may memorize individual training examples and expose sensitive information through membership inference and data extraction attacks. Although non-private score estimation has been extensively studied, the statistical limits of its private counterpart remain less understood. In this work, we study score estimation under $(α,β)$-differential privacy for $d$-dimensional sub-Gaussian distributions with locally $γ$-Hölder-continuous scores. We develop a sampling-based private score estimator using quadratic B-splines and the exponential mechanism, and we implement our proposal through projected Langevin Monte Carlo with runtime polynomial in the sample size $n$. The proposed estimator satisfies $(α,β)$-differential privacy, and achieves expected density-weighted squared error $\mbox{polylog}(n) \max(n^{-2γ/(d+2γ+2)},\,(nα)^{-2γ/(d+γ+1)})$. We also establish a nearly matching private minimax lower bound, thereby characterizing the privacy-accuracy trade-off for score estimation. As an application, we construct a differentially private diffusion model whose privacy guarantee is independent of the number of denoising steps. We show that, with an appropriate discretization scheme, the resulting diffusion model attains nearly minimax optimal expected total variation error among all private distribution estimators. We validate our theoretical findings through experiments on both synthetic and real-world datasets.

</details>

### [Deviations from the NTK Regime in CNNs under Joint Depth-Width Scaling](https://arxiv.org/abs/2611.25624v1)
*Maria Matveev, Pascal Esser, Gitta Kutyniok et al.* · `cs.LG` · arXiv:2611.25624v1 · relevance 0.24

- **In one sentence**: The concentration and training-time constancy of the neural tangent kernel (NTK) depend on the interplay between network width, depth, and initialization. (first sentence of the abstract; AI summaries are off)
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

The concentration and training-time constancy of the neural tangent kernel (NTK) depend on the interplay between network width, depth, and initialization. While joint depth-width scaling has been studied in fully-connected, residual, and recurrent networks, its effects in convolutional neural networks (CNNs) remain less understood. We investigate these effects numerically in CNNs, examining NTK dispersion at initialization and kernel rotation during training. Let depth $L$ be the number of convolutional layers, and width $C$ the number of channels per layer. We find that NTK dispersion increases with $L/C$ in the critical and chaotic initialization regimes, but remains small in the ordered regime. At critical initialization, dispersion curves approximately collapse as a function of $L/C$, suggesting a nontrivial joint scaling regime. During training, kernel rotation generally increases with $L/C$, even in the ordered regime where initial dispersion is small. Together, these results suggest that $L/C$ may govern NTK deviations from the infinite-width limit in certain regimes, and that NTK concentration at initialization and stability during training exhibit different scaling behaviors.

</details>

## Probability

### [Generic arm separation for planar percolation models](https://arxiv.org/abs/2611.26458v1)
*Loïc Gassmann, Ioan Manolescu, Maran Mohanarangan* · `math.PR` · arXiv:2611.26458v1 · relevance 0.15

- **In one sentence**: Arm separation is an important technical tool in the study of critical and near-critical planar percolation systems. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Arm separation is an important technical tool in the study of critical and near-critical planar percolation systems. When combined with RSW estimates, it proves quasi-multiplicativity of arm-event probabilities, links the derivatives of different events and allows the identification of universal arm exponents. We provide a very generic statement of arm separation that applies to arbitrary planar percolation models. Our argument is based on exploring configurations conditioned on the existence of arms in such a way that "exposed" arms are revealed with positive probability. The exploration algorithm is independent of the percolation model and applies to all polychromatic arm events. As an application, we prove a strong arm-separation result for critical planar FK-percolation.

</details>

### [Dynamical edge universality and the Airy$_β$ line ensemble](https://arxiv.org/abs/2611.25364v1)
*Jiaoyang Huang, Shengjing Xu, Yulei Xu* · `math.PR` · arXiv:2611.25364v1 · relevance 0.14

- **In one sentence**: We prove dynamical edge universality for three families of interacting particle systems for every $β>0$: $β$-Dyson Brownian motion with an analytic potential, weighted $β$-corners processes, and a class of discrete-time Markov chains. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We prove dynamical edge universality for three families of interacting particle systems for every $β>0$: $β$-Dyson Brownian motion with an analytic potential, weighted $β$-corners processes, and a class of discrete-time Markov chains. Our results apply to general non-equilibrium initial data and show that the Airy$_β$ line ensemble emerges at positive times whenever the limiting density has a regular square-root edge. More precisely, after centering at the moving deterministic edge and rescaling space and time on the $n^{-2/3}$ and $n^{-1/3}$ scales, respectively, the trajectories of the top $k$ particles converge jointly in distribution to the top $k$ curves of the Airy$_β$ line ensemble, for every fixed $k$, in the topology of uniform convergence on compact time intervals. The proof combines dynamical loop equations with characteristic-flow estimates to establish local laws near the moving edge and upper bounds on the extremal particle. We then identify the stochastic evolution of every subsequential limit of the rescaled Stieltjes transform and establish convergence through the pole-evolution characterization of the Airy$_β$ line ensemble.

</details>

## Differential geometry

### [Conformal parity](https://arxiv.org/abs/2611.25497v1)
*Andrzej Derdzinski, Sinhwi Kim, JeongHyeong Park* · `math.DG` · arXiv:2611.25497v1 · relevance 0.19

- **In one sentence**: We call a Riemannian metric on a four-manifold, as well as the underlying conformal structure, conformally even/odd if its self-dual and anti-self- dual Weyl tensors acting on bivectors have, at each point, equal/opposite spectra. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We call a Riemannian metric on a four-manifold, as well as the underlying conformal structure, conformally even/odd if its self-dual and anti-self- dual Weyl tensors acting on bivectors have, at each point, equal/opposite spectra. The term mixed parity refers to the simultaneous occurrence of both of these conditions, an obvious example being the conformally flat case. After listing various known classes of conformally even metrics, we construct examples of conformally odd ones which are not of mixed parity, as well as some metrics of mixed parity that are not conformally flat. The former examples are provided by left-invariant metrics on Lie groups, and realize uncountably many local conformal-equivalence types. The latter also include some arising from Lie groups, as well as certain 1+3 Riemannian products that are not locally conformally homogeneous.

</details>

### [Affine Boosted Gauss Curvature Flow](https://arxiv.org/abs/2611.25390v1)
*Andrews. Ben, Rajpal. Devesh* · `math.DG` · arXiv:2611.25390v1 · relevance 0.17

- **In one sentence**: We prove convexity in the affine orbit of entropies associated to Gauss curvature flow for sub-affine powers. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We prove convexity in the affine orbit of entropies associated to Gauss curvature flow for sub-affine powers. This allows the construction of an affine boosted Gauss curvature flow, which keeps the evolving hypersurface at the affine minimizer of the Gaussian entropy. The modified flow has bounded isoperimetric ratio, and after rescaling it converges along a sequence of times to self-similar solutions of the Gauss curvature flow. The construction also proves existence of new self-similar solutions to Gauss curvature flow in the sub-affine regime.

</details>

## Mathematical physics

Nothing notable this time.

## Complex analysis

Nothing notable this time.

## AI for mathematics

### [Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents](https://arxiv.org/abs/2611.25599v1)
*Meghana Aparna Sistla, Alaia Solko-Breslin, Somesh Jha et al.* · `cs.CR` · arXiv:2611.25599v1 · relevance 0.18

- **In one sentence**: Autonomous AI agents are increasingly deployed for long-running tasks that execute arbitrary shell commands or programs. (first sentence of the abstract; AI summaries are off)
- Matched keywords: Lean, formal verification

<details><summary>Original abstract</summary>

Autonomous AI agents are increasingly deployed for long-running tasks that execute arbitrary shell commands or programs. However, these actions can result in unauthorized network requests or persistent, malicious changes to the user's file system, processes, or privileges. Existing defense mechanisms rely on either LLM-based monitors, which lack provable safety guarantees, or stateless policy enforcement layers, which miss multi-step data flows and execution side-effects unmodeled by the policy language (e.g., network calls initiated inside a Python script). We introduce Tether, a framework for runtime enforcement of stateful security policies over the observed side-effects of an agent's actions. Tether executes each proposed action in an ephemeral, isolated sandbox, inferring abstract action semantics from observed system calls. Tether then enforces stateful policies over these inferred semantics, permitting actions to proceed only if they comply with the policy. Policies and action semantics are defined in an embedded DSL in Lean 4 capable of expressing diverse constraints, including information flow control (IFC), access control, and network security policies. Because actions can propagate labels from sources to destinations, a single rule can enforce fine-grained IFC policies across multi-step execution flows of arbitrary length. Expressing policies in Lean enables formal verification that they satisfy global security invariants (e.g., preventing network access after reading a sensitive file). We evaluate Tether on realistic coding-agent benchmarks across both benign and adversarial trajectories. With a single policy shared across all tasks, Tether blocks 100% of in-scope attacks while maintaining a benign false-positive rate under 5%.

</details>

### [Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy](https://arxiv.org/abs/2611.26172v1)
*Ilia Zavidnyi, Alexander Kovrigin, Arina Puchkova et al.* · `cs.LG` · arXiv:2611.26172v1 · relevance 0.13

- **In one sentence**: Reasoning models often become more accurate when they can generate longer answers at test time. (first sentence of the abstract; AI summaries are off)
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Reasoning models often become more accurate when they can generate longer answers at test time. This behavior is known as test-time scaling. However, RL with verifiable rewards (RLVR) usually trains them with a fixed rollout cap. We find that this cap changes model behavior, not only training cost. After training, models use few additional tokens beyond the training budget. They outperform the base models near that budget, but their accuracy stops improving and falls below the base model at larger budgets. The rollout cap thus becomes a learned constraint, that limits model's test-time scaling. We call this effect budget internalization. We observe it across Qwen3.5-4B, Gemma4-E2B, and Nemotron-3-Nano-4B and two reasoning training tasks: mathematical reasoning and diverse, procedurally generated problems. This effect also transfers from math training to science and coding tasks. Training-objective level ablations on Qwen3.5-4B show that most changes recover little test-time scaling. Stronger KL regularization and lower training-data truncation preserve more scaling, but stronger KL reduces in-budget accuracy. Forcing an answer on truncated training rollouts largely removes budget internalization, but also removes most of the in-budget gain. SFT on artificially truncated traces reproduces budget internalization, whereas SFT on naturally short traces does not, which shows that the effect is not specific to RL. This result links budget internalization to length-censored post-training rather than to an RL-specific objective term. Thus, a rollout cap does not only control training cost. It can trade low-budget gains for lower performance when additional inference compute is available.

</details>

## Embodied AI and robotics

### [MoRE: Mixture-of-Experts for Multi-Physics Robotic World Models](https://arxiv.org/abs/2611.25336v1)
*Ziyu Zhu, Shaowei Liu, Albert J. Zhai et al.* · `cs.RO` · arXiv:2611.25336v1 · relevance 0.34

- **In one sentence**: A robotic world model should predict how objects evolve under robot actions and physical dynamics. (first sentence of the abstract; AI summaries are off)
- Matched keywords: manipulation, world model

<details><summary>Original abstract</summary>

A robotic world model should predict how objects evolve under robot actions and physical dynamics. While recent 3D world models have shown strong predictive capabilities, they still struggle with the heterogeneous dynamics arising from diverse object interactions. To address this in a unified framework, we decompose robotic interactions into distinct physical regimes and assign each to a specialized motion expert. We introduce MoRE, a 3D world model with a mixture of motion experts organized around rigid, deformable, and prehensile dynamics. This design enables a single model to capture diverse physical behaviors while preserving regime-specific priors. Trained on mixed simulation and real-world data, MoRE integrates with Model Predictive Control (MPC) to support diverse manipulation tasks. Experiments show that MoRE improves prediction accuracy across physics regimes, leading to stronger real-world MPC performance. Code, data, and project website are available at https://alwaysleepy.github.io/MoRE-WM-site/.

</details>

### [Verify2Act: Critic-Guided Latent World Models for Verifying Language-Conditioned Manipulation Plans](https://arxiv.org/abs/2611.25243v1)
*Chrisantus Eze, Christopher Crick* · `cs.RO` · arXiv:2611.25243v1 · relevance 0.34

- **In one sentence**: Vision-Language Models (VLMs) can propose multi-step manipulation plans, but they have no grounded model of how a scene will change, and the pixel-level world models that could check those plans are slow and drift over long horizons. (first sentence of the abstract; AI summaries are off)
- Matched keywords: manipulation, world model

<details><summary>Original abstract</summary>

Vision-Language Models (VLMs) can propose multi-step manipulation plans, but they have no grounded model of how a scene will change, and the pixel-level world models that could check those plans are slow and drift over long horizons. We present Verify2Act, a modular verification framework that separates semantic action proposal from latent physical verification. A VLM proposes candidate plans, a latent world model (V2A-WM) imagines each of them in the DINOv2 feature space, and a dual-head critic checks the imagined rollouts for temporal consistency and goal satisfaction before anything is executed. V2A-WM extends recent flow-matching world models with cross-attention action grounding and a causal temporal history window. We deploy the full system on a low-cost robot arm, training the world model and critic only on data generated in a digital twin. Across six language-conditioned tasks, Verify2Act reaches 83.3\% task success, compared with 61.7\% for a latent world model without our architectural changes, 53.3\% for the VLM alone, and 46.7\% for a pixel-diffusion world model. It verified every plan it executed and incurred no planning-induced failures: all of its failed episodes were caused by low-level grasp or placement slips. In simulation, Verify2Act obtains the highest five-task chain success on CALVIN among the compared baselines with 30$\times$ fewer reflective VLM calls than pixel-diffusion verification, and the highest success on cluttered nut assembly.

</details>

## Theoretical physics

### [Bianchi cosmologies with four-dimensional groups of motion in New General Relativity](https://arxiv.org/abs/2611.26474v1)
*Manuel Hohmann, Paul Martin Kull, Margus Saal* · `gr-qc` · arXiv:2611.26474v1 · relevance 0.16

- **In one sentence**: We study the dynamics of the most general metric teleparallel spacetimes of Bianchi types II, III and IX, which admit a four-dimensional symmetry group, in the 1-parameter family of New General Relativity. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We study the dynamics of the most general metric teleparallel spacetimes of Bianchi types II, III and IX, which admit a four-dimensional symmetry group, in the 1-parameter family of New General Relativity. We first show that in each of these classes the most general metric teleparallel geometry is described by four free functions of time, while another four functions of time describe the most general energy-momentum tensor compatible with the same symmetries. We then derive the field equations of New General Relativity for this class of geometries. Finally, we present some solutions to these field equations. Our results show that both solutions resembling features of the standard Friedmann-Lemaître-Robertson-Walker cosmology of General Relativity and deviations thereof exist.

</details>

### [Revisiting Kerr-Newman-(A)dS Black Holes in \(f(R)\) Gravity: A Kerr-Schild Approach](https://arxiv.org/abs/2611.25992v1)
*Göksel Daylan Esmer, Saliha Türkmen* · `gr-qc` · arXiv:2611.25992v1 · relevance 0.15

- **In one sentence**: It is known that, in the constant-curvature regime, the field equations of $f(R)$ gravity reduce to the Einstein form with an effective cosmological constant, establishing a direct correspondence between stationary and axisymmetric black hole solutions in $f(R)$ gravity and their counterparts in gen… (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

It is known that, in the constant-curvature regime, the field equations of $f(R)$ gravity reduce to the Einstein form with an effective cosmological constant, establishing a direct correspondence between stationary and axisymmetric black hole solutions in $f(R)$ gravity and their counterparts in general relativity, including the Kerr--Newman--(A)dS family. Within this framework, we revisit the derivation of these metrics using the Kerr--Schild approach for illustrative purposes. The Maxwell equations are solved independently of the Kerr--Schild function, allowing the electromagnetic source to be determined before addressing the gravitational field equations. We then investigate the possibility of non-constant-curvature solutions, taking quadratic $f(R)$ gravity as a representative model. Remarkably, the field equations within the Kerr--Schild ansatz force the Ricci scalar to be constant, reducing the resulting geometries to the familiar Kerr--Newman--(A)dS family. Thus, our analysis extends the recently established no-go result for uncharged black holes to electrically charged configurations within the framework considered here.

</details>

## Chemistry and materials

### [Molecular Dynamics Simulation of the Solidification of AlCoCuFeNi High-Entropy Alloy Nanowire](https://arxiv.org/abs/2611.25836v1)
*O. I. Kushnerov* · `cond-mat.mtrl-sci` · arXiv:2611.25836v1 · relevance 0.16

- **In one sentence**: Molecular dynamics simulation of the solidification behavior of an AlCoCuFeNi high-entropy alloy nanowire was performed using an embedded atom model potential at cooling rates of 10^11, 10^12, and 10^13 K/s. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Molecular dynamics simulation of the solidification behavior of an AlCoCuFeNi high-entropy alloy nanowire was performed using an embedded atom model potential at cooling rates of 10^11, 10^12, and 10^13 K/s. Periodic boundary conditions were applied along the nanowire axis to model an effectively infinite nanowire. The crystallization process was characterized through the temperature dependence of the potential energy. Structural evolution was analyzed using adaptive common-neighbor analysis (CNA) and radial distribution functions (RDF). The results show that the final structure changes from amorphous to crystalline with decreasing cooling rate, demonstrating the strong influence of cooling conditions on phase formation in nanoscale high-entropy alloy systems.

</details>

### [Intelligent Imaging of Thermal Transport in Nanostructures](https://arxiv.org/abs/2611.25779v1)
*Xin Qian, Te-Huan Liu, Xiaobo Li et al.* · `cond-mat.mtrl-sci` · arXiv:2611.25779v1 · relevance 0.15

- **In one sentence**: The ability to measure thermal properties and visualize heat transport processes with high spatial resolution is becoming increasingly important for materials discovery, next-generation electronics, and advanced manufacturing. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The ability to measure thermal properties and visualize heat transport processes with high spatial resolution is becoming increasingly important for materials discovery, next-generation electronics, and advanced manufacturing. As critical dimensions and architectures of novel materials and high performance electronics shrink and become more heterogeneous, thermal transport is no longer governed by bulk material properties alone, but by local variations in microstructure, such as interfaces and defects, while the operating conditions can also play a role. With the development of non-contact pump-probe thermoreflectance techniques, specific heat, thermal conductivity, and interface conductance can be mapped either through wide-field thermos-reflectance images or by scanning technique. However, key challenges remain such as the balance between imaging throughput and measurement accuracy, the extraction of multiple parameters with high confidence, and non-intrusive subsurface characterization, etc. This Review highlights recent advancements in artificial intelligence (AI)-assistance in high-throughput data processing, visualizing interfacial thermal transport, and nonintrusive subsurface analysis, and offers outlooks for future research directions such as spectral mapping of heat carriers, three-dimensional property mapping, and AI-agentic experimental designs. We anticipate this Review will motivate future efforts in combining AI with experimental techniques to achieve unprecedented capabilities for thermal characterization of nanoscale materials and device characterization, facilitating materials discovery and electronics revolution.

</details>

## Computational and systems biology

### [Gene regulatory networks and the organization of cell differentiation in multicellular organisms](https://www.biorxiv.org/content/10.64898/2026.11.18.767571v1)
*Meraz-Segura, L. F.; Guerrero Vaca, A. C.; Alcaraz Barrera, R. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.18.767571 v1 · relevance 0.18

- **In one sentence**: Across their development, clonal multicellular organisms generate new cell types from less differentiated cell types. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Across their development, clonal multicellular organisms generate new cell types from less differentiated cell types. Differentiation pathways arrange into a hierarchical, tree-like organization: regressions from specialized to undifferentiated cell types rarely occur and undifferentiated cell types often have the potential to produce, when subject to distinct stimuli, two or more differently specialized cell types. How cell type transitions acquire such a peculiar disposition requires an explanation that must reside in the properties of gene regulatory networks (GRNs); after all, GRNs orchestrate the changes in gene activity that define cell types. We studied vast numbers of small dynamic model networks to search for elementary GRNs that could yield the simplest hierarchical, developmental-like, differentiation patterns. We found that only a small minority of GRNs are compatible with hierarchical cell type transitions. Importantly, GRNs that yielded developmental-like differentiation patterns shared common traits: One is the presence of tangles of cycles of positive interactions. Genes in such a tangle produce an all-or-none one-way response to a signal. Another such trait is mutual inhibition between genes associated to different specialized cell types, enforcing their mutually exclusive activation. Moreover, these regulatory patterns are more abundant in published experimentally sustained developmental GRNs than as expected by chance. In addition, we show that it is easy to maintain hierarchical cellular differentiation throughout evolution, even when undergoing changes in gene regulatory interactions and developmental mechanisms. Our work supports the prevalence of design principles that organize hierarchically differentiation pathways in clonal multicellular organisms.

</details>

### [Breadth over Depth: Predictor-Agnostic Consensus for Improved Antibody--Antigen Structure Prediction](https://www.biorxiv.org/content/10.64898/2026.11.17.767212v1)
*Ullanat, V.; Gupta, A.; Li, R. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.17.767212 v1 · relevance 0.11

- **In one sentence**: Antibody-antigen structure prediction commonly relies on sampling a single co-folding predictor deeply and selecting its highest-confidence output using model-specific confidence scores. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Antibody-antigen structure prediction commonly relies on sampling a single co-folding predictor deeply and selecting its highest-confidence output using model-specific confidence scores. We introduce AbPoolRank, a predictor-agnostic structural selector that ranks mixed pools using cross-pose agreement, within-source reproducibility and interface geometry, without native confidence, predictor identities or predictor-specific parameters. On 103 cluster-disjoint, post-2021 antibody-antigen complexes from SAbDab2, three structures each from Boltz-2, Promera, Protenix-v2, ESMFold2-Fast and OpenDDE form a 15-structure pool that reaches 58.0% medium-or-better Success@1 (DockQ [&ge;] 0.49), exceeding confidence-based selection from every individual predictor sampled 100 times (26-52%). Existing ranking methods did not rescue deep single-predictor sampling or surpass our selector on mixed pools, with no method exceeding 51.5% on 100 structures from one co-folder and AbPoolRank matching the strongest single-structure methods while significantly outperforming consensus methods. AbPoolRank trained without one predictor lost at most 3.0 percentage points, and the frozen model accepted full MSA-conditioned ESMFold2, a sixth predictor absent from method development, without retraining or loss of accuracy. Diversification also improved the accuracy-compute frontier, with the 15-structure pool using 1.8-fold less aggregate GPU time than the most accurate single-predictor setting in our compute benchmark and 3.3-fold less than sampling that predictor 100 times. Together, these results show that shallow sampling across complementary co-folders, coupled with a confidence-free selector, provides an accurate and computationally efficient inference strategy for antibody-antigen structure prediction.

</details>

## Economics

Nothing notable this time.

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Machine learning theory | 10 | 10 | 2 |
| Probability | 24 | 23 | 2 |
| Differential geometry | 22 | 21 | 2 |
| Mathematical physics | 33 | 33 | 0 |
| Complex analysis | 6 | 5 | 0 |
| AI for mathematics | 21 | 21 | 2 |
| Embodied AI and robotics | 56 | 56 | 2 |
| Theoretical physics | 68 | 67 | 2 |
| Chemistry and materials | 35 | 34 | 2 |
| Computational and systems biology | 148 | 147 | 2 |
| Economics | 16 | 16 | 0 |

<!-- {% endraw %} -->
