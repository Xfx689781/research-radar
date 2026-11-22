# Research digest · 2026-11-22
<!-- {% raw %} -->

New papers posted from about 2026-11-21 to 2026-11-22 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Digitization of Analogue Gauges using Computer Vision](https://arxiv.org/abs/2611.26262v1)** (Computer vision): Analogue gauges remain prevalent in manufacturing industries for measuring physical quantities, yet manual monitoring by operators introduces human error and operational inefficiency.
- **[DRAFT: graph-recurrent learning of dynamic gene regulatory networks along single-cell multi-omics trajectories](https://www.biorxiv.org/content/10.64898/2026.11.17.767145v1)** (Computational and systems biology): Single-cell multi-omics data offer an opportunity to resolve how gene regulatory networks (GRNs) are rewired during cell-fate transitions, but most existing methods infer static snapshots, ignore temporal dependencies or assume linear regulation.
- **[Gene regulatory networks and the organization of cell differentiation in multicellular organisms](https://www.biorxiv.org/content/10.64898/2026.11.18.767571v1)** (Computational and systems biology): Across their development, clonal multicellular organisms generate new cell types from less differentiated cell types.

## Probability

### [Generic arm separation for planar percolation models](https://arxiv.org/abs/2611.26458v1)
*Loïc Gassmann, Ioan Manolescu, Maran Mohanarangan* · `math.PR` · arXiv:2611.26458v1 · relevance 0.15

- **In one sentence**: The paper proves a model-independent arm-separation statement for arbitrary planar percolation models, using an exploration argument that reveals arms with positive probability, and applies it to get a strong arm-separation result for critical planar FK-percolation.
- **In plain words**: Percolation is a simple random model of a porous material: each spot is open or closed at random, and one asks when open paths connect distant places. The authors study how several separate open or closed paths ('arms') can be made to stay apart from one another in a plane, a property that underpins precise estimates of how likely such connections are near the critical point. They give a general version of this separation property that does not depend on the particular random model, and they check it on a more complicated model called FK-percolation, which comes from statistical physics. The abstract does not report numerical values or further consequences beyond the statement and this application.
- **Why it matters**: Arm-separation results are a standard tool for deriving exponents and scaling behaviour in two-dimensional critical random systems, so a statement that works across many models could make those tools easier to reuse. The abstract does not say how widely the result will be adopted, so its impact beyond this setting is uncertain.
- **Background needed**: ['Percolation: sites or edges are randomly open or closed, and the question is when open clusters span large distances.', 'Critical point: the threshold probability at which large connected clusters first appear; behaviour there is scale-invariant.', 'Arm events: events that several disjoint paths of given colours (open or closed) cross a region from one place to another.', 'RSW (Russo–Seymour–Welsh) estimates: bounds saying crossing events are not too unlikely across scales.', 'Quasi-multiplicativity and arm exponents: probabilities of multiple arms factor up to constants across scales, and the decay rates are universal numbers.', 'FK-percolation: a generalisation of percolation tied to the Potts model in statistical physics.', 'Conditioning and exploration: revealing random configuration step by step to control dependence between events.'] · level: research-level

<details><summary>Original abstract</summary>

Arm separation is an important technical tool in the study of critical and near-critical planar percolation systems. When combined with RSW estimates, it proves quasi-multiplicativity of arm-event probabilities, links the derivatives of different events and allows the identification of universal arm exponents. We provide a very generic statement of arm separation that applies to arbitrary planar percolation models. Our argument is based on exploring configurations conditioned on the existence of arms in such a way that "exposed" arms are revealed with positive probability. The exploration algorithm is independent of the percolation model and applies to all polychromatic arm events. As an application, we prove a strong arm-separation result for critical planar FK-percolation.

</details>

### [Dynamical edge universality and the Airy$_β$ line ensemble](https://arxiv.org/abs/2611.25364v1)
*Jiaoyang Huang, Shengjing Xu, Yulei Xu* · `math.PR` · arXiv:2611.25364v1 · relevance 0.14

- **In one sentence**: The paper proves that for every β>0, three families of interacting particle systems (β-Dyson Brownian motion with analytic potential, weighted β-corners processes, and a class of discrete-time Markov chains), started from general non-equilibrium data, have their top k particles near the moving spectral edge converge, after edge-centering and n^{-2/3} space / n^{-1/3} time rescaling, to the top k curves of the Airy_β line ensemble, using dynamical loop equations and characteristic-flow estimates.
- **In plain words**: The paper studies systems of many randomly moving particles that repel each other, such as eigenvalues of large random matrices evolving over time. When the particles spread out in a square-root-shaped pattern, the particles at the outer edge behave in a universal way, and the authors prove this holds over time for three model families, starting from fairly general initial configurations. Zooming in on the leading few particles at the edge, their paths converge to a known random object called the Airy_β line ensemble.
- **Why it matters**: It extends edge universality, a central theme in random matrix theory, from equilibrium snapshots to the full time evolution of the particles, covering all values of the repulsion parameter β>0. Its relevance to other areas rests on the universality claim, but the abstract does not discuss specific applications.
- **Background needed**: ['Random matrices and eigenvalues: a large matrix with random entries has eigenvalues that spread into a limiting density, and this paper is about the particles at the edge of that spread.', 'The parameter β: it controls how strongly the particles repel each other (β=1, 2, 4 correspond to classical symmetric, Hermitian and quaternion ensembles).', 'Universality: many different random models share the same small-scale limiting behaviour, so the detailed model matters less than general features.', 'Airy process / line ensemble: the scaling limit of edge particles, a random infinite collection of continuous curves; the Airy_β version generalizes the Airy process to every β.', 'Dyson Brownian motion: a stochastic process in which eigenvalues evolve in time as diffusing particles with mutual repulsion.', 'Stieltjes transform and loop equations: analytic tools that encode the empirical particle density through a complex function and yield algebraic identities satisfied by moments of the system.', 'Scaling: space is rescaled by n^{-2/3} and time by n^{-1/3}, the standard edge scales.'] · level: research-level

<details><summary>Original abstract</summary>

We prove dynamical edge universality for three families of interacting particle systems for every $β>0$: $β$-Dyson Brownian motion with an analytic potential, weighted $β$-corners processes, and a class of discrete-time Markov chains. Our results apply to general non-equilibrium initial data and show that the Airy$_β$ line ensemble emerges at positive times whenever the limiting density has a regular square-root edge. More precisely, after centering at the moving deterministic edge and rescaling space and time on the $n^{-2/3}$ and $n^{-1/3}$ scales, respectively, the trajectories of the top $k$ particles converge jointly in distribution to the top $k$ curves of the Airy$_β$ line ensemble, for every fixed $k$, in the topology of uniform convergence on compact time intervals. The proof combines dynamical loop equations with characteristic-flow estimates to establish local laws near the moving edge and upper bounds on the extremal particle. We then identify the stochastic evolution of every subsequential limit of the rescaled Stieltjes transform and establish convergence through the pole-evolution characterization of the Airy$_β$ line ensemble.

</details>

## Differential geometry

### [Willmore stability of minimal surfaces in the n-sphere](https://arxiv.org/abs/2611.26238v1)
*Rob Kusner, Peng Wang* · `math.DG` · arXiv:2611.26238v1 · relevance 0.30

- **In one sentence**: We prove that the Lawson minimal surface $ξ_{g,1}$ in $S^3$ is strongly stable for the Willmore bending energy $W$ and remains strongly $W$-stable in $S^n$ for every $n \geq4$; our proof starts with a new lower bound on the area-index of $ξ_{m,k}$ for $m\geq k>1$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We prove that the Lawson minimal surface $ξ_{g,1}$ in $S^3$ is strongly stable for the Willmore bending energy $W$ and remains strongly $W$-stable in $S^n$ for every $n \geq4$; our proof starts with a new lower bound on the area-index of $ξ_{m,k}$ for $m\geq k>1$. Next we observe that each of the $ξ_{m,k}$ and the Karcher-Pinkall-Sterling minimal surfaces in $S^3$, as well as the equilateral minimal torus in $S^5$, is the unique $W$-minimizer in its conformal class, up to Möbius transformations of $S^n$. Finally, we show that although the equilateral minimal torus is $W$-stable in $S^n$ for every $n \geq5$, it is neither strongly $W$-stable nor a local $W$-minimizer: it has a 2-dimensional space of $W$-Jacobi fields on which almost everywhere the third-variation of $W$ is nonzero.

</details>

### [Displaceability of monotone Lagrangians in $\mathbb{C}P^3(\sqrt{2})$ and $Q^4(\sqrt{2})$](https://arxiv.org/abs/2611.25699v1)
*Han Lou, Shuo Zhang* · `math.SG` · arXiv:2611.25699v1 · relevance 0.24

- **In one sentence**: We show that the generalized Polterovich submanifold $L_{0, 2}^P$ in $\mathbb{C}P^3(\sqrt{2})$ and the Chekanov-Oakley-Usher Lagrangian $L_{1, 2}^{Q, \mathrm{Ch}}$ in the quadric $Q^4(\sqrt{2})$ are displaceable. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We show that the generalized Polterovich submanifold $L_{0, 2}^P$ in $\mathbb{C}P^3(\sqrt{2})$ and the Chekanov-Oakley-Usher Lagrangian $L_{1, 2}^{Q, \mathrm{Ch}}$ in the quadric $Q^4(\sqrt{2})$ are displaceable. Since $L_{0, 2}^P$ and $L_{1, 2}^{Q, \mathrm{Ch}}$ are in the zero level set of the moment maps of the $\mathrm{SO}(3)$-actions on $\mathbb{C}P^3(\sqrt{2})$ and $Q^4(\sqrt{2})$, the main idea is to construct Hamiltonian diffeomorphisms mapping $L_{0, 2}^P$ and $L_{1, 2}^{Q, \mathrm{Ch}}$ to nonzero level sets of the moment maps.

</details>

## Partial differential equations

### [Existence and Uniqueness of Mild Solutions to Rough Stochastic Partial Differential Equations driven by Fractional Brownian Motion with Hurst Index $H > 1/4$](https://arxiv.org/abs/2611.26580v1)
*Maksim Vaskouski, Maksim Firsau* · `math.PR` · arXiv:2611.26580v1 · relevance 0.27

- **In one sentence**: In this paper we prove a theorem on the unique solvability of the Cauchy problem for a stochastic partial differential equation driven by the fractional Brownian motion with Hurst index $H>\frac{1}{4}$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

In this paper we prove a theorem on the unique solvability of the Cauchy problem for a stochastic partial differential equation driven by the fractional Brownian motion with Hurst index $H>\frac{1}{4}$.

</details>

### [On the regularity of stationary solutions to free boundary problems](https://arxiv.org/abs/2611.25345v1)
*Daniel Restrepo* · `math.AP` · arXiv:2611.25345v1 · relevance 0.19

- **In one sentence**: The paper sharpens the regularity theory for Hölder-continuous stationary solutions of free boundary problems that are harmonic off their zero set, obtaining a √log-Lipschitz bound for a generalized phase-variable class (including the two-phase problem), a full Lipschitz bound in the one-phase case, and showing that a Lipschitz assumption in Kriventsov–Weiss's variational class can be weakened to any positive Hölder exponent.
- **In plain words**: Free boundary problems describe shapes where two regions (for example, a region with a substance and one without, or two different materials) meet along an interface whose position is part of the answer. This note asks how smooth the solutions must be when they are stationary, meaning they are balanced against small deformations of the domain. The authors show that a weaker starting assumption on smoothness suffices than was previously required, and they get a slightly weaker or stronger smoothness conclusion depending on whether there is one phase or two.
- **Why it matters**: Getting by with a weaker smoothness assumption makes the regularity result apply to a broader class of solutions, which matters for free boundary theory in general. I can only judge the significance from the abstract, so the wider impact is uncertain; the connections it may have to variational and geometric questions are not spelled out there.
- **Background needed**: ['Partial differential equations: equations relating a function to its rates of change in several variables.', 'Free boundary problem: a problem in which the region where the solution is nonzero (or where phases differ) is itself unknown and must be determined.', 'Hölder continuity: a measure of smoothness, where an exponent between 0 and 1 controls how closely nearby values must match; Lipschitz is the case of bounded slope.', "Harmonic function: a solution of Laplace's equation, the classic smooth 'equilibrium' function.", 'Stationary solution with inner variations: a solution that does not change to first order under small reparametrizations of the domain, i.e. a critical point of an energy.', 'One-phase versus two-phase problems: whether the solution is zero on one side of the interface or takes two distinct nonzero regimes.', 'Regularity: how smooth a solution is guaranteed to be; here, how its gradient or continuity is controlled.'] · level: research-level

<details><summary>Original abstract</summary>

In this note, we improve the regularity of Hölder continuous stationary solutions with respect to inner variations which are harmonic outside their zero set. We obtain a $\sqrt{\log}$-Lipschitz estimate for a class of solutions allowing a generalized phase variable and including the two-phase problem. In the case of the one-phase problem, we can improve to Lipschitz regularity. In particular, we show that the initial Lipschitz assumption in the class of variational solutions considered by Kriventsov and Weiss can be replaced by any positive Hölder exponent

</details>

## Harmonic analysis

### [Oscillatory integral operators of arbitrary signature: beyond the universal estimates](https://arxiv.org/abs/2611.26265v1)
*Fernando Ballesta-Yagüe, Jonathan Hickman, Hrit Roy* · `math.CA` · arXiv:2611.26265v1 · relevance 0.21

- **In one sentence**: We consider Hörmander oscillatory integral operators on $\mathbb{R}^n$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We consider Hörmander oscillatory integral operators on $\mathbb{R}^n$. In particular, we are interested in proving bounds with dependence on the signature of the phase. The sharp universal range of $L^p\to L^p$ estimates was obtained for any given signature by the second author and Iliopoulou. Under the mild non-compression hypotheses on the phase introduced in Chen et al., we prove $L^p\to L^p$ estimates that go beyond this universal range in odd dimensions. We also obtain the sharp universal range of $L^p\to L^q$ estimates for odd $n$. The techniques are based on the breakthrough work of Wang--Wu on the Fourier restriction conjecture.

</details>

### [Collineations of the diamond lattice in a Hilbert space](https://arxiv.org/abs/2611.25622v1)
*Janko Bračič* · `math.FA` · arXiv:2611.25622v1 · relevance 0.11

- **In one sentence**: Let $\mathscr{M}$ and $\mathscr{N}$ be non-trivial closed subspaces of a separable Hilbert space $\mathscr{H}$ such that $\mathscr{M}\cap\mathscr{N}=\{0\}$ and $\mathscr{M}+\mathscr{N}$ is dense in $\mathscr{H}$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Let $\mathscr{M}$ and $\mathscr{N}$ be non-trivial closed subspaces of a separable Hilbert space $\mathscr{H}$ such that $\mathscr{M}\cap\mathscr{N}=\{0\}$ and $\mathscr{M}+\mathscr{N}$ is dense in $\mathscr{H}$. We characterize when there exists an invertible operator on $\mathscr{H}$ which maps $\mathscr{M}$ onto $\mathscr{N}$ and $\mathscr{N}$ onto $\mathscr{M}$. We prove that such an operator exists if and only if $\mathscr{M}$ and $\mathscr{N}$ have a common algebraic complement. This happens if and only if either neither of the operators $(I-P)Q$ and $(I-Q)P$ is compact, or $P-Q$ is compact and $\dim(\mathscr{M}\cap\mathscr{N}^\perp)=\dim(\mathscr{M}^\perp\cap\mathscr{N})$, where $P$ and $Q$ are the orthogonal projections onto $\mathscr{M}$ and $\mathscr{N}$. Moreover, the operator can be chosen to be an involution. Consequently, the group of collineations of the diamond lattice $\{\{0\},\mathscr{M},\mathscr{N},\mathscr{H}\}$ which fix $\mathscr{M}$ and $\mathscr{N}$ is always complemented in the group of all its collineations.

</details>

## Complex analysis

### [On the solution of a question for meromorphic functions sharing three values IM and a fourth value CM in the complex plane](https://arxiv.org/abs/2611.25948v1)
*Xiao-Min Li, Jun Wang, Hong-Xun Yi* · `math.CV` · arXiv:2611.25948v1 · relevance 0.15

- **In one sentence**: The paper settles Gundersen's 1992 question by proving that two non-constant meromorphic functions sharing three finite values IM and infinity CM must also share those three finite values CM, which upgrades the sharing relation without extra hypotheses.
- **In plain words**: The question concerns two functions of a complex variable that take the same specific values at the same points, either counting multiplicity or ignoring it. Gundersen asked in 1992 whether agreeing on three values loosely and a fourth value strictly forces agreement on all four strictly, and this has been open for decades. The authors show that, for the special case where the fourth value is infinity, the answer is yes: agreement on three values loosely plus infinity strictly implies agreement on the three values strictly as well.
- **Why it matters**: It closes a well-known open problem in value distribution theory, so it matters to specialists in that area. The abstract covers only the special case with infinity as the strict value, so it does not by itself settle the general form of Gundersen's question for an arbitrary fourth value; that scope should be kept in view.
- **Background needed**: ['Meromorphic function: a function of a complex variable that is holomorphic except for isolated poles, which are its only infinities.', "Sharing a value: two functions share a value a if f(z)=a exactly when g(z)=a; 'IM' (ignoring multiplicity) only compares the points, while 'CM' (counting multiplicity) also matches how many times each point is hit.", 'Nevanlinna value distribution theory: the study of how often a meromorphic function takes given values, measured by counting functions and characteristic functions.', "Picard exceptional value: a value that a function omits entirely, or takes only finitely often in the sense of Picard's theorems.", "Cross ratio and Möbius transformation: the cross ratio is a four-point invariant of the Riemann sphere, and a Möbius transformation is a rational map of degree one that preserves it; these appear in Nevanlinna's classical four-value result.", "Gundersen's question: a 1992 open problem asking whether three values shared IM plus a fourth shared CM forces all four to be shared CM."] · level: research-level

<details><summary>Original abstract</summary>

In 1926, Nevanlinna (Acta Math. {\bf 48} (1926), no. 3-4, 367-391) proved that if two distinct and non-constant meromorphic functions $f$ and $g$ share $a_1,$ $a_2,$ $a_3,$ $a_4$ CM in the complex plane, where $a_1,$ $a_2,$ $a_3,$ $a_4$ are four distinct complex values in the extended complex plane, then $f$ is a Möbius transformation of $g$, two of the shared values, say $a_1$ and $a_2$, are Picard exceptional values, and the cross ratio $\left(a_1, a_2, a_3, a_4\right)=-1.$ Later on, Gundersen (Trans. Amer. Math. Soc. {\bf 277} (1983), no. 2, 545-567. Correction: {\bf 304} (1987), 847-850) proved that if two non-constant meromorphic functions share two values CM and share two other values IM, then the functions share all four values CM. In 1992, Gundersen (Complex Var. Elliptic Equ. {\bf 20} (1992), no. 1-4, 99-106) proposed the following famous question: if two non-constant meromorphic functions share three distinct values IM and share a fourth value CM, then do the functions necessarily share all four values CM? This question is a long-standing question in the studies of the Nevanlinna's value distribution theory of meromorphic functions, and has not been completely resolved by now. In this paper, we completely resolve the question, and prove that if two distinct and non-constant meromorphic functions $f$ and $g$ share $a_1,$ $a_2,$ $a_3$ IM and $\infty$ CM, where $a_1,$ $a_2,$ $a_3$ are three distinct and finite complex values in the complex plane, then $f$ and $g$ also share $a_1,$ $a_2,$ $a_3$ CM.

</details>

### [Matrix-point interpolation for positive real odd functions in one and several variables](https://arxiv.org/abs/2611.26240v1)
*Sanne ter Horst, Alma van der Merwe, Victor Vinnikov et al.* · `math.FA` · arXiv:2611.26240v1 · relevance 0.09

- **In one sentence**: The paper studies matrix-valued interpolation for positive real (odd) functions on the right half-plane, in one variable and in noncommutative several variables, characterizing when solutions may or must have a pole at infinity and giving numerical algorithms.
- **In plain words**: The problem asks for a smooth rule-based function that takes prescribed matrix values at a chosen point and also stays 'positive' on a half of the complex plane, a constraint that often arises in engineering and systems theory. The authors work out, in the one-variable case, exactly when such a function is allowed or forced to blow up at infinity, and in the several-variable case (with matrices that do not commute) they handle the simpler situation where it does not blow up. Their results also come with numerical methods for actually computing a solution.
- **Why it matters**: Interpolation with positivity constraints underlies many problems in control, signal processing and system identification, so clear criteria for solvability and a computational route are useful. The noncommutative multivariable extension links the work to operator theory and realization theory, though the abstract does not show how far the results reach beyond this setting.
- **Background needed**: ['Interpolation: finding a function that matches given values at given points.', 'Matrix-valued functions: each output is a grid of numbers, and matrices need not commute when multiplied.', 'Positive real functions: functions whose real part is nonnegative on a region, common in circuit and control theory.', 'Right half-plane: the set of complex numbers with positive real part.', "Pole at infinity: a point where the function's size grows without bound as the input goes far out; whether this is permitted determines which solutions exist.", 'Noncommutative several variables: functions of several matrix-valued inputs where the order of multiplication matters.'] · level: research-level

<details><summary>Original abstract</summary>

We study the single matrix point interpolation problem for positive real matrix valued functions on the right half-plane, both in the single variable setting and in the noncommutative multivariable setting. In the single variable case, a careful analysis is done for when the solution may or must have a pole at infinity. In the multivariable setting, as the pole structure at infinity can be more complicated, we focus on the case when there is no pole at infinity. The results also yield numerical algorithms for finding a solution.

</details>

## Operator algebras and spectral theory

### [Spectral asymptotics for vector-valued magnetic Schrödinger operators](https://arxiv.org/abs/2611.26479v1)
*Vincenzo Leone, Marianna Porfido, Abdelaziz Rhandi* · `math.AP` · arXiv:2611.26479v1 · relevance 0.15

- **In one sentence**: We consider vector-valued magnetic Schrödinger operators $-Δ_{a} +V$ with magnetic potential ${a}\in C^2(\mathbb{R}^d;\mathbb{R}^d)$ and electric potential $V$ given by a symmetric and positive semidefinite $m\times m$ matrix-valued function whose entries belong to $L^1_{\rm loc}(\mathbb{R}^d)$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We consider vector-valued magnetic Schrödinger operators $-Δ_{a} +V$ with magnetic potential ${a}\in C^2(\mathbb{R}^d;\mathbb{R}^d)$ and electric potential $V$ given by a symmetric and positive semidefinite $m\times m$ matrix-valued function whose entries belong to $L^1_{\rm loc}(\mathbb{R}^d)$. Assuming that $\|\operatorname{curl} {a}(\cdot)\|\operatorname{Id}_{\mathbb{R}^m} + V$ belongs to a certain matrix reverse Hölder class, we characterize necessary and sufficient conditions under which the spectrum of $-Δ_{a} +V$ is discrete, and study the eigenvalue asymptotics and exponential decay of eigenfunctions.

</details>

### [Spectral isometries and invertibility preservers on Banach algebras](https://arxiv.org/abs/2611.26462v1)
*Zakariae Aznay, Fadil Chabbabi* · `math.FA` · arXiv:2611.26462v1 · relevance 0.11

- **In one sentence**: We prove that every unital surjective complex-linear spectral isometry between complex unital semisimple Banach algebras is a Jordan isomorphism, thereby giving an affirmative answer to the spectrum-preserving form of Kaplansky's conjecture. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We prove that every unital surjective complex-linear spectral isometry between complex unital semisimple Banach algebras is a Jordan isomorphism, thereby giving an affirmative answer to the spectrum-preserving form of Kaplansky's conjecture. We also characterize surjective complex-linear maps between arbitrary unital Banach algebras that preserve invertibility in either direction, satisfy either spectral inclusion, or preserve the spectral radius. In particular, for a complex-linear bijection between semisimple Banach algebras, preservation of invertibility in either direction implies preservation in both directions, and either spectral inclusion implies equality of spectra, even without assuming unitality. As an application, we study preservers of the Fredholm essential spectrum and essential spectral radius.

</details>

## Algebra

### [Finite groups with a fixed-point-free automorphism satisfying an irreducible identity](https://arxiv.org/abs/2611.25886v1)
*Dietrich Burde, Wolfgang Alexander Moens* · `math.GR` · arXiv:2611.25886v1 · relevance 0.22

- **In one sentence**: For any given irreducible polynomial $f(x)=a_0+a_1\cdot x+\cdots+a_d\cdot x^d\in\mathbb{Z}[x]$, we study the structure of finite groups $(G,\cdot)$ that have a fixed-point-free-automorphism $α$ satisfying the condition \[ \{g^{a_0}\cdotα(g)^{a_1}\cdotsα^d(g)^{a_d}\mid g\in G\}=\{1\}. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

For any given irreducible polynomial $f(x)=a_0+a_1\cdot x+\cdots+a_d\cdot x^d\in\mathbb{Z}[x]$, we study the structure of finite groups $(G,\cdot)$ that have a fixed-point-free-automorphism $α$ satisfying the condition \[ \{g^{a_0}\cdotα(g)^{a_1}\cdotsα^d(g)^{a_d}\mid g\in G\}=\{1\}. \] We show that such a group $G$ is nilpotent of class at most $d^{2^d}$, provided that $|G|$ is coprime to an explicit, non-zero, integer invariant $ι(f(x))$ of $f(x)$. We do this by extending the solutions of the Frobenius conjecture. We also extend the solution of the restricted Burnside problem in prime exponent and the classification of the $n$-abelian groups.

</details>

### [Nonsolvable critical groups with the spectrum of $S_{10}$](https://arxiv.org/abs/2611.25766v1)
*D. V. Lytkina, V. D. Mazurov* · `math.GR` · arXiv:2611.25766v1 · relevance 0.14

- **In one sentence**: We classify the nonsolvable finite groups that are critical with respect to the spectrum of the symmetric group $S_{10}$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We classify the nonsolvable finite groups that are critical with respect to the spectrum of the symmetric group $S_{10}$. Up to isomorphism, there are exactly two such groups: $S_{10}$ and $(A_9\times C_3)\rtimes C_2$, where the involution acts on $A_9$ by conjugation by a transposition and on $C_3$ by inversion. The quotient of any nonsolvable group with this spectrum by its solvable radical is almost simple. All possible simple socles are treated without assuming that the radical is nilpotent. The final cases, $L_3(4)$ and $A_6$, are excluded using the canonical subgroup $K=[R(G)\cap G^\infty,G^\infty]$, actions on chief factors, and the required element orders $9,20,30$. In the $A_6$ case, the final contradiction is the existence of an element of order $16$. Reproducible certificates accompany the character-table and matrix calculations.

</details>

## Representation theory

### [On quasi-triangular Hopf algebras of square-free dimensions](https://arxiv.org/abs/2611.25676v1)
*Jiacheng Bao, Zhiqiang Yu, Ying Zheng* · `math.QA` · arXiv:2611.25676v1 · relevance 0.23

- **In one sentence**: Let $H$ be a quasi-triangular Hopf algebra of sqaure-free dimension over $\mathbb{C}$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Let $H$ be a quasi-triangular Hopf algebra of sqaure-free dimension over $\mathbb{C}$. In this note, we show that $H$ is semisimple and cocommutative. Equivalently, a braided finite tensor category $\mathcal{C}$ of square-free Frobenius--Perron dimension with a fiber functor is tensor equivalent to the representation category of a finite group.

</details>

### [Super quantum groups of divided powers à la Lusztig](https://arxiv.org/abs/2611.26505v1)
*Iván Angiono, Cristian Vay* · `math.QA` · arXiv:2611.26505v1 · relevance 0.19

- **In one sentence**: We construct super analogues of the quantum groups of divided powers introduced by Lusztig. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We construct super analogues of the quantum groups of divided powers introduced by Lusztig. We call them super analogues because the Lie-theoretical data governing their structure is comparable to that of contragredient Lie superalgebras. Indeed, we show that they admit PBW-type bases parametrized by root systems of super type, and that they also have Lusztig isomorphisms giving a representation of the corresponding Weyl groupoids. Moreover, we prove that our super objects are equipped with a Frobenius-type morphism whose kernel is the Drinfeld double of a finite-dimensional Nichols algebra of super type, a super analogue of Lusztig's small quantum group, and whose cokernel is the enveloping algebra of the semisimple Lie algebra determined by the Cartan roots of the Nichols algebra. We carry out our construction within the framework of Nichols algebras of diagonal type, specifically, those whose braiding is obtained by specializing at a root of unity. This allows us to consider a divided power integral form inside a large quantum group of De Concini--Kac--Procesi type and then, via specialization, obtain our desired object.

</details>

## Number theory

### [Rational Elliptic Period Relations Across Realizations: Complex Lattices, Local p-adic Periods, and Drinfeld Modules](https://arxiv.org/abs/2611.25399v1)
*Mohammadreza Mohajer* · `math.NT` · arXiv:2611.25399v1 · relevance 0.16

- **In one sentence**: We determine the algebraic relations among full de Rham comparison periods of elliptic curves over finite extensions of $\mathbb Q_p$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We determine the algebraic relations among full de Rham comparison periods of elliptic curves over finite extensions of $\mathbb Q_p$. The connected local monodromy group gives the transcendence degree and an explicit affine linear relation ideal for the full matrix in Fontaine's field $B_{\mathrm{dR}}$. After normalizing the holomorphic row and reducing to $\mathbb C_p$, the transcendence degree drops by one and the normalized determinant supplies the additional relation. Every polynomial relation of degree at most $d$ is detected modulo $t^{d+1}$. For $d\ge1$ this bound is sharp for each elliptic curve. A rational quasi-period row gives a Galois-stable Tate line. Together with an algebraic holomorphic period ratio it forces potential splitting, which identifies the exact ordinary CM obstruction. We compute the full Tate matrix. For ordinary non-CM curves with $p\ge5$, the standard quasi-period row is rational precisely at a zero of Katz's $E_{2,p}$. Away from the zeros the two full ratios are algebraically independent. At the zeros, a nonzero quasi-period and the normalized holomorphic ratio have algebraically independent images in $\mathbb C_p$. The complex question that motivates these results, the analogue for Drinfeld modules, and a conditional arithmetic consequence for Katz values complete the comparison.

</details>

### [Equivariant iterated Eisenstein integrals for congruence subgroups of level 2](https://arxiv.org/abs/2611.26597v1)
*Emiel Claasen, Mehregan Doroudiani, Claude Duhr et al.* · `hep-th` · arXiv:2611.26597v1 · relevance 0.11

- **In one sentence**: The paper constructs non-holomorphic modular objects, called equivariant iterated Eisenstein integrals, for the level-2 congruence subgroups Γ(2) and Γ_0(2), built from iterated Eisenstein integrals, their complex conjugates, and level-2 cyclotomic multiple zeta values, following Brown's SL_2(Z) construction.
- **In plain words**: Modular forms are highly symmetric functions on the complex upper half-plane, and their 'antiderivatives' (integrals) do not keep that symmetry on their own. This paper repairs the problem for a specific family of symmetry groups of level 2, by adding correction terms built from special constants called multiple zeta values, together with complex conjugates. The authors work with generating series valued in an infinite-dimensional algebraic group. When they restrict to the weight-2 case, they recover known single-valued multiple polylogarithms on a particular curve. The abstract does not state any further consequences beyond this construction.
- **Why it matters**: It extends a known construction from the full modular group to two important congruence subgroups, and it links iterated integrals of Eisenstein series to multiple polylogarithms and to physics-adjacent single-valued functions. The abstract does not explain the wider significance beyond these connections, and I have not checked how much new this is relative to prior work.
- **Background needed**: ['Modular forms: complex functions on the upper half-plane with transformation rules under a group of matrices (here SL_2(Z) and its subgroups).', 'Congruence subgroups of level N: subgroups defined by reducing matrix entries mod N; Γ(2) and Γ_0(2) are the level-2 cases.', 'Eisenstein series: standard explicit modular forms; their iterated integrals are repeated antiderivatives.', 'Multiple zeta values and cyclotomic variants: iterated sums or integrals producing special constants, with roots-of-unity versions at level N.', 'Non-holomorphic modular forms: modular objects that involve complex conjugation and are not holomorphic, needed to make the corrected objects transform cleanly.', 'Generating series and pro-unipotent Lie groups/algebras: a packaging device that encodes all iteration depths at once and tracks how the corrections compose.'] · level: research-level

<details><summary>Original abstract</summary>

The modular properties of holomorphic Eisenstein series for $\mathrm{SL}_2(\mathbb{Z})$ and its congruence subgroups do not carry over to their primitives. Instead, the transformation of iterated Eisenstein integrals under congruence subgroups of level $N$ introduces inhomogeneous terms comprising (among others) cyclotomic multiple zeta values of level $N$. We combine iterated Eisenstein integrals for the congruence subgroups of level $N=2$ of arbitrary iteration depth with their complex conjugates and (single-valued) level-2 cyclotomic multiple zeta values such that they define non-holomorphic modular forms. Our construction of these so-called equivariant iterated Eisenstein integrals for $Γ(2)$ and $Γ_0(2)$ proceeds at the level of generating series that take values in an infinite-dimensional (pro-unipotent) Lie group and closely follow Brown's analogous construction in the $\mathrm{SL}_2(\mathbb{Z})$ case. The required insertions of cyclotomic multiple zeta values are controlled by zeta generators for level 2 that normalise the corresponding (pro-nilpotent) Lie algebra of the generating series and whose Lie-bracket relations we determine systematically. Upon restriction to Eisenstein series of modular weight~2, we recover single-valued multiple polylogarithms on the genus 0 modular curve $Γ(2)\backslash \mathbb{H}$.

</details>

## Algebraic geometry

### [Surface sheaves on the quintic I. Expanded degenerations and virtual gluing](https://arxiv.org/abs/2611.26207v1)
*Artan Sheshmani* · `math.AG` · arXiv:2611.26207v1 · relevance 0.18

- **In one sentence**: We study the specialization of Donaldson-Thomas virtual cycles for surface sheaves on a Calabi Yau threefold degenerating to a simple normal crossing threefold, composed of two quasi Fano threefolds glued along a common (double) divisor. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We study the specialization of Donaldson-Thomas virtual cycles for surface sheaves on a Calabi Yau threefold degenerating to a simple normal crossing threefold, composed of two quasi Fano threefolds glued along a common (double) divisor. The compactification of the two relative sheaf moduli spaces involves construction of suitable moduli space of sheaves on expanded degenerations of each quasi Fano variety. On a fixed expanded fiber the matching datum is an equivalence of the derived restrictions of the component sheaves. We identify the corresponding deformation complexes and give valuative and obstruction-theoretic hypotheses under which the specialized virtual class is a sum over marked joining divisors. When a marked space is the full fiber product of proper relative factors over a smooth simple boundary moduli space, its class is a refined diagonal pullback. For the case of sheaves supported on hyperplane sections of the threefold we discuss construction of the proper relative family by descending the chartwise stable loci, and identify both marked pieces, including the one with zero boundary. To provide some examples, we carry out explicit constructions for the moduli space of surface structure sheaf and its twists. We also prove valuative results for specified sheaves with noninvertible hulls. In a sequel, Part II, we use the construction of degeneration technique in this article to compare quintic invariants with the predicted S-duality modularity of "M5-brane modified elliptic genus" provided by string theorists, Gaiotto Strominger and Yin.

</details>

### [Stein degree on birational log Calabi-Yau fibrations](https://arxiv.org/abs/2611.25501v1)
*Xintong Jiang, Santai Qu* · `math.AG` · arXiv:2611.25501v1 · relevance 0.11

- **In one sentence**: We prove uniform bounds for the Stein degrees of boundary divisors on generalised log Calabi-Yau fibrations of Fano type over arbitrary fields of characteristic zero. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We prove uniform bounds for the Stein degrees of boundary divisors on generalised log Calabi-Yau fibrations of Fano type over arbitrary fields of characteristic zero. The main ingredient is the birational case for which we provide two approaches.

</details>

## Topology

### [Kernel Regression using Persistence Diagrams](https://arxiv.org/abs/2611.25295v1)
*Saksham Aggarwal, James Nichols, Katharine Turner* · `math.ST` · arXiv:2611.25295v1 · relevance 0.21

- **In one sentence**: The paper builds a kernel-weighted local-averaging regression estimator that takes persistence diagrams as inputs, uses Wasserstein distance as the similarity measure, and proves consistency and convergence-rate bounds in the L² sense.
- **In plain words**: Data scientists often summarize the shape of a dataset as a 'persistence diagram', a compact list of loops, holes, and clusters that appear at different scales. This paper asks how to predict a single number from such a shape summary, using a method that predicts by averaging the outputs of similar past examples. The authors prove the method gets more accurate as data grows, give a bound on how fast that happens, and report experiments where it performs well, especially with little data. The abstract does not give the details of those experiments.
- **Why it matters**: Predicting outcomes from shape features is a practical need in areas like materials science and medical imaging, and this paper gives a theoretical footing for doing so directly in diagram space. The abstract alone does not show how the assumptions or rates compare with other approaches, so the strength of the contribution is hard to judge from it.
- **Background needed**: ['Persistent homology: a method that tracks topological features (connected pieces, loops, voids) across a range of scales, summarized as a persistence diagram.', 'Wasserstein distance: a way to measure how far apart two distributions or point sets are, here applied to two persistence diagrams.', 'Kernel regression: predicting a value by a weighted average of training outputs, where weights fall off with the distance between inputs.', 'Consistency: the property that an estimator converges to the true relationship as the sample size grows.', 'Convergence rate and L² error: how quickly the average squared prediction error shrinks with more data.'] · level: research-level

<details><summary>Original abstract</summary>

Persistence diagrams are widely used in topological data analysis to summarize topological and geometric structure in data. We study nonparametric regression where inputs are persistence diagrams and outputs are real-valued. Using kernel-based local averaging estimators defined directly over diagram space with Wasserstein distance, we establish consistency and derive bounds on the rate of convergence under suitable assumptions in the $L^2$-theory. We also present computational experiments that demonstrate strong performance of the proposed estimator, particularly in low data regimes.

</details>

### [An A $\infty$ -algebra structure for enriched Morse complexes](https://arxiv.org/abs/2611.25890v1)
*Jonathan Clivio, Robin Riegel* · `math.AT` · arXiv:2611.25890v1 · relevance 0.10

- **In one sentence**: We construct a homotopy coherent product structure extending the Chas-Sullivan product on chains of the free loop space of a manifold. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We construct a homotopy coherent product structure extending the Chas-Sullivan product on chains of the free loop space of a manifold. Our construction uses the framework of Morse homology with DG coefficients and perturbed Morse gradient trees. We define an operad given by moduli spaces of Morse gradient trees with a twisted differential. This Morse tree operad receives a map from a suspended A$\infty$-operad and in turn acts on Morse homology with DG coefficients associated to a fibration over a manifold with a fibrewise monoidal structure.

</details>

## Dynamical systems

### [Convergence of the Most Probable Transition Paths in Multiscale Systems](https://arxiv.org/abs/2611.26205v1)
*Qiqi Lian, Shanqi Liu, Jinqiao Duan* · `math.DS` · arXiv:2611.26205v1 · relevance 0.13

- **In one sentence**: This paper is devoted to study the convergence behavior of the most probable transition paths in a class of multiscale stochastic dynamical systems. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

This paper is devoted to study the convergence behavior of the most probable transition paths in a class of multiscale stochastic dynamical systems. First, based on Euler-Lagrange equations, we establish proximity and convergence results in the space of continuous functions endowed with the supremum norm. These results compare the most probable paths of the multiscale system with those of averaged system derived from the averaging principle. Next, we utilize a variational framework and analyze the Onsager-Machlup functionals using $Γ$-convergence. Together with the equi-coercivity of the functional family, we prove the convergence of both their minima and minimizers. Specifically, we show weak convergence of the minimizers in the Cameron-Martin space $H^1$, which implies their strong convergence in $L^2$.

</details>

### [Neural Conditional Gaussian Model: Efficient Data Assimilation with Sequential Uncertainty Quantification for Nonlinear Dynamics](https://arxiv.org/abs/2611.26463v1)
*Chuanqi Chen, Nan Chen* · `cs.LG` · arXiv:2611.26463v1 · relevance 0.11

- **In one sentence**: The paper learns a neural-network dynamical model that encodes partially observed nonlinear states into a latent space where the dynamics are conditional Gaussian, enabling closed-form data assimilation updates and a Gaussian decoder that propagates uncertainty back to physical variables.
- **In plain words**: Scientists often want to track the hidden state of a complicated system, such as weather, from noisy and incomplete measurements, and to know how uncertain their estimate is. Standard methods for this can be slow and usually need the exact equations governing the system. The authors train a neural network that translates the system into a simpler hidden representation where the update step can be computed directly, then translates back to the physical quantities together with an uncertainty estimate.
- **Why it matters**: Fast, uncertainty-aware state tracking matters in areas such as weather prediction and other data assimilation settings where the governing equations are incomplete. The abstract reports lower online cost and accurate estimation and forecasting on benchmark systems, but I cannot judge from the abstract how general these gains are beyond those benchmarks.
- **Background needed**: ['Data assimilation: combining a model of a system with incoming observations to estimate its current hidden state.', "Nonlinear filtering: estimating a hidden state over time when the system's rules are nonlinear, so the uncertainty does not stay simply Gaussian.", 'Gaussian (normal) distribution: a bell-shaped uncertainty described by a mean and a covariance (spread and correlations).', 'Conditional Gaussian structure: a model where some variables are Gaussian once others are known, which allows exact, cheap calculations.', 'Encoder-decoder network: one neural network maps data into a hidden (latent) space and another maps it back.', 'Negative log-likelihood training: fitting a model by rewarding predictions that assign high probability to the observed data.'] · level: research-level

<details><summary>Original abstract</summary>

Data assimilation (DA) in partially observed nonlinear systems requires repeated estimation of both hidden states and their uncertainty. Conventional nonlinear filtering can be computationally expensive and often relies on an explicit dynamical model. In this paper, we develop the Neural Conditional Gaussian Model (Neural CGM), a data-driven dynamical model that maps unobserved physical states into a learned latent space, where the dynamics of the latent states follow a conditional Gaussian structure. This structure allows closed-form DA updates in the latent space, while nonlinear encoder-decoder mappings retain the flexibility needed to represent complex dynamics in physical space. A key feature of Neural CGM is its treatment of uncertainty in DA. The latent posterior mean and covariance are mapped to the physical variables through a Gaussian decoder that combines local moment propagation with learned nonlinear corrections. The resulting physical-space posterior statistics depend on the sequentially updated latent distribution rather than on a separate post-processing estimate. The same statistics enter a Gaussian negative log-likelihood during training, so both the posterior mean and uncertainty affect the learned model. Because Neural CGM learns the dynamical model itself, it can also be used for state forecasting and simulation without explicit knowledge of the governing equations. Numerical experiments on benchmark nonlinear dynamical systems show accurate state estimation and forecasting while substantially reducing online assimilation cost relative to conventional nonlinear DA methods. Neural CGM is therefore suited to repeated state estimation, uncertainty quantification, and prediction from partial observations.

</details>

## Combinatorics

### [A very robust Ramsey theorem for hypergraph matchings](https://arxiv.org/abs/2611.25893v1)
*Peter Keevash, Peleg Michaeli* · `math.CO` · arXiv:2611.25893v1 · relevance 0.17

- **In one sentence**: A fundamental result in Ramsey theory due to Alon, Frankl and Lovász gives an exact formula for the $q$-colour Ramsey numbers of matchings in $r$-uniform hypergraphs: if $n\ge\mathsf{AFL}_r(\mathbf{t})=(r-1)\|\mathbf{t}\|_\infty+1+\sum_{j=1}^q(t_j-1)$ then in any $q$-edge-colouring of $K^r_n$ there… (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

A fundamental result in Ramsey theory due to Alon, Frankl and Lovász gives an exact formula for the $q$-colour Ramsey numbers of matchings in $r$-uniform hypergraphs: if $n\ge\mathsf{AFL}_r(\mathbf{t})=(r-1)\|\mathbf{t}\|_\infty+1+\sum_{j=1}^q(t_j-1)$ then in any $q$-edge-colouring of $K^r_n$ there is some colour $j$ with a matching of size $t_j$. We show that a very weak quasirandomness assumption suffices for this Ramsey property: we can replace $K^r_n$ by any $r$-graph $H$ on at least $\mathsf{AFL}_r(\mathbf{t})+o(n)$ vertices that is a sublinear connector, meaning that it has no balanced $r$-partite holes of linear size. This generalises the result for $r=2$ (ordinary graphs) that we proved previously using a compression algorithm based on Gallai-Edmonds decompositions. This structure theory is unavailable in the hypergraph setting, so we combine two other proof methods, namely (a) simultaneous optimisation in all colours by clustering vertices using fractional cover weights from LP duality, and (b) local-to-global structure via random sampling and Kahn's matching theorem.

</details>

### [Rational Designs and Prouhet--Tarry--Escott Problems](https://arxiv.org/abs/2611.25516v1)
*Ryutaro Misawa, Masanori Sawa, Filip Špiranec* · `math.CO` · arXiv:2611.25516v1 · relevance 0.10

- **In one sentence**: For every strength, we prove the existence of rational designs on spheres, orthogonal and unitary groups, real and complex Grassmannians, and ellipsoids that are defined by positive-definite quadratic forms with rational coefficients and have a rational point. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

For every strength, we prove the existence of rational designs on spheres, orthogonal and unitary groups, real and complex Grassmannians, and ellipsoids that are defined by positive-definite quadratic forms with rational coefficients and have a rational point. This answers Bannai's Problem for these spaces, solves the problem of Cui--Xia--Xiang on rational spherical $4$-designs on the unit circle, and proves Xiang's conjecture in the stronger form of existence in every dimension. To this end, we introduce the $(G,\mathcal{S})$-Prouhet--Tarry--Escott problem for an abelian group $G$ and a finite set of characters $\mathcal{S}$ and develop its existence and minimality theory. We also prove a general theorem transforming integer-weighted rational designs into equi-weighted designs on distinct rational points. On the unit circle $\mathbb{S}^1$, we determine the minimum sizes of rational spherical designs of strengths $4,5,6,7$ and show that they are respectively $2304,4608,9216,9216$. We also show that the minimum size of a rational spherical $5$-design on $\mathbb{S}^2$ is $192$. We further apply our framework to prove a conjecture of Thuswaldner--Ziegler on sums of distinct units and to answer Mahabaduge's problem on convex equilateral lattice polygons affirmatively.

</details>

## Numerical analysis

### [When and why can integral constraints improve the accuracy of physics-informed neural networks?](https://arxiv.org/abs/2611.25515v1)
*Myeong-Su Lee* · `math.NA` · arXiv:2611.25515v1 · relevance 0.13

- **In one sentence**: The paper derives stability estimates for PINN losses with and without integral constraints on several PDEs, showing that in certain parameter regimes the standard loss gives only weak control over some error components while the integral constraints restore uniform control, and supports this with numerical experiments.
- **In plain words**: Physics-informed neural networks learn approximate solutions to equations describing physical systems by penalizing mistakes in the equation during training. Some researchers have found that adding extra conditions obtained by summing or integrating the equation over a region helps accuracy, but the reason was not well understood. The authors compare error bounds with and without these integral conditions for several equations, and report that in some parameter settings the usual training loss barely controls certain kinds of error, while the integral conditions restore control; their experiments match this, though the abstract does not give details of the specific equations or error sizes.
- **Why it matters**: It offers a mathematical explanation for a practical training trick that people have used in scientific machine learning, which helps decide when the trick is worth adding. Whether the reasoning carries over to other equations or network designs is not stated in the abstract and would need the full paper to judge.
- **Background needed**: ['Partial differential equation (PDE): an equation relating a function to its rates of change in several variables, used to model heat, waves, fluid flow and similar physics.', 'Neural network as a function approximator: a model with adjustable weights that is trained to fit data or satisfy equations.', 'Physics-informed neural network (PINN): a network trained by minimizing the residual of the PDE (and boundary/initial conditions) at sample points, so the loss measures how well the physics is satisfied.', 'Loss function: the single number the training algorithm tries to make small.', 'Integral constraint: a condition obtained by integrating the governing equation over a domain, added as an extra term in the loss.', 'Stability estimate: a mathematical bound showing how much the output error can grow relative to the size of the loss, indicating how well the loss controls the error.'] · level: research-level

<details><summary>Original abstract</summary>

Adding constraints obtained by integrating governing equations to the loss has been reported to improve the accuracy of physics-informed neural networks (PINNs) in several applications, but mathematical understanding of these benefits remains limited. For several partial differential equations (PDEs), we derive stability estimates for losses with and without integral constraints. The comparison reveals that in certain parameter regimes, the standard loss has very weak control over specific error components, and that the integral constraints restore uniform control of these components. This explains when and why the constraints improve accuracy. Finally, numerical experiments support this interpretation. In parameter regimes where the standard loss is predicted to have weak control over those components, the two losses indeed show clear differences in accuracy. Conversely, in regimes where the standard loss retains sufficient control, both losses yield similar accuracy.

</details>

### [Variational integrators for time-dependent Lagrangian systems on Lie groups](https://arxiv.org/abs/2611.25313v1)
*Leonardo Colombo, María Emma Eyrea Irazú, David Martín de Diego et al.* · `math.NA` · arXiv:2611.25313v1 · relevance 0.12

- **In one sentence**: The paper builds structure-preserving variational time-stepping schemes for time-dependent Lagrangian systems evolving on Lie groups (such as rotations in SO(3)), proves their symplectic and momentum-preserving properties, gives a second-order error bound for a midpoint-Cayley variant, and analyzes long-time near-conservation via backward error analysis with an extended-phase-space formulation.
- **In plain words**: Many physical systems, such as spinning bodies or networks of orientations, have states that are rotations rather than ordinary numbers, and their laws can change with time. Computer simulations of these systems tend to drift away from the true behavior over long runs, so the authors design step-by-step computational rules that are derived from the system's variational (least-action) principle so they keep key physical quantities in line. They show the schemes preserve geometric structure and momentum, prove the method is second-order accurate, and argue that energy stays nearly constant over exponentially long times under stated assumptions. Numerical tests on a rotating rigid body and a rotation network are reported to match these predictions.
- **Why it matters**: Geometry-preserving integrators matter for long simulations in robotics, spacecraft attitude control, and multi-agent synchronization, where drift can accumulate into wrong answers. The paper's combination of time-dependence, Lie-group structure, and consensus stability may interest researchers in geometric numerical integration and control, though the practical reach beyond the stated assumptions is not established by the abstract.
- **Background needed**: ['Lagrangian mechanics: motion obtained from a least-action principle and the Euler-Lagrange equations.', 'Lie groups: smooth groups of transformations such as rotations SO(3); their tangent and cotangent spaces underlie the dynamics.', 'Symplectic maps: transformations that preserve the geometric area structure of phase space, which in turn controls long-run energy behavior.', "Noether's theorem: each continuous symmetry of the Lagrangian gives a conserved quantity, such as momentum.", 'Variational integrators: discrete-time schemes obtained by discretizing the action rather than the equations of motion.', 'Backward error analysis: interpreting a numerical method as the exact flow of a slightly modified equation to explain long-time accuracy.', 'Consensus dynamics: networked agents whose states are driven toward a common value, here rotations.'] · level: research-level

<details><summary>Original abstract</summary>

We develop fixed-step variational integrators for time-dependent Lagrangian systems on Lie groups, derive their reduced dynamics, and analyze their long-time behavior by backward error analysis. We derive the continuous Euler-Lagrange equations, energy balance, and Noether conservation laws, and construct time-indexed discrete Lagrangians using retractions, with the midpoint-Cayley scheme treated explicitly. On their regularity domains, the resulting phase-space maps are symplectic. For left-invariant discrete Lagrangians, they reduce to Lie-Poisson maps that preserve coadjoint orbits and, when $G$ is connected, every Casimir function. A variational error analysis establishes second-order accuracy of the midpoint-Cayley method. We also construct an exactly symplectic, projectable extension on $T^*(\mathbb R\times G)$ whose formal modified Hamiltonian is affine in the momentum conjugate to time and admits symmetry reduction. Under uniform analyticity, coefficient bounds, and domain-containment assumptions, optimal truncation yields exponentially accurate interpolation and near-conservation of the modified extended Hamiltonian over exponentially long intervals. For a connected attitude network on $SO(3)^N$ with damping and uniformly positive, non-increasing coupling weights, we prove local asymptotic stability of the static consensus set for the continuous dynamics and exact preservation of total spatial momentum by the discrete scheme. Numerical experiments on the network and on a time-dependent rigid body on $SO(3)$ illustrate second-order convergence and the extended energy balance.

</details>

## Logic and foundations

### [Invariance and Expressiveness: Modal Variations](https://arxiv.org/abs/2611.26244v1)
*Martin Otto* · `cs.LO` · arXiv:2611.26244v1 · relevance 0.21

- **In one sentence**: This contribution focuses on bisimulation invariance as the hallmark of modal model theory and of modal modelling. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

This contribution focuses on bisimulation invariance as the hallmark of modal model theory and of modal modelling. It exemplifies traditional as well as more recent ramifications \&\ extensions of classical results -- involving variant modes of bisimulation equivalence and matching modalities also beyond plain Kripke structures, and emphasising especially the technical challenges in finite model theory and other non-elementary settings. Main results to be discussed revolve about the theme of expressive completeness phenomena: beside expressive completeness under bisimulation invariance in relation to first-order background logics, in the style of van Benthem--Rosen characterisations, this also concerns maximality results under criteria form abstract model theory, in the style of Lindstroem theorems.

</details>

### [Proof Checking Continuous Reachability](https://arxiv.org/abs/2611.25303v1)
*Long Qian, André Platzer* · `cs.LO` · arXiv:2611.25303v1 · relevance 0.11

- **In one sentence**: The paper defines a proof format and a Lean4-based proof checker that certify Taylor-model reachability bounds for polynomial ODEs as proofs in differential dynamic logic (dL), and proves that such proofs can always be generated when the underlying approximation is correct.
- **In plain words**: Computer programs that predict where a system governed by continuous-change equations (like a moving robot or a physical process) will end up often give numerical answers that could be wrong by rounding or approximation errors. This paper asks how to independently check those answers: the authors design a format for writing down a formal proof of each predicted range, and a checker that verifies the proof with a computer proof assistant. They prove that whenever the original approximation was correct, a matching proof of this kind can be produced and checked. The checker is reported to verify benchmark problems from the ARCH competition, though the abstract gives few details beyond that.
- **Why it matters**: Trusting numerical tools for safety-critical claims is a real problem, and this work tries to close the gap by making their outputs independently checkable, similar to how SAT solvers' unsatisfiability answers are certified. The connection to formal verification of cyber-physical systems is clear, but the abstract does not indicate how broadly the approach scales beyond the benchmarks.
- **Background needed**: ['Ordinary differential equations (ODEs): equations describing how quantities change continuously over time.', 'Reachability: determining the set of states a system can reach from given starting conditions.', 'Taylor models: a way of representing a function as a polynomial plus a rigorous error bound, used to get guaranteed enclosures of ODE solutions.', 'Differential dynamic logic (dL): a logic for stating and proving properties of hybrid and continuous systems, supported by the KeYmaera X theorem prover.', 'Proof certificates: a result checked by a small trusted program, so the complex solver need not be trusted.', 'Lean4: a proof assistant used here to implement the checker with formal guarantees.', 'Completeness of a proof format: the guarantee that every correct computation has a corresponding checkable proof.'] · level: research-level

<details><summary>Original abstract</summary>

This paper introduces a proof format and proof checker for certifying reachability computations of ordinary differential equations (ODEs) with polynomial vector fields. Establishing a proof checking framework for certifying ODE reachability is similar to the checking of UNSAT proofs for propositional satisfiability solving, but it is even more important due to the challenges inherent in dealing with ODEs, and even more challenging due to the numerical nature of ODE reachability algorithms. The proofs are expressed in differential dynamic logic (dL), and can be independently verified with symbolic theorem provers for dL (e.g. KeYmaeraX). Such proofs are naturally generated by reachability algorithms based on Taylor models, a popular technique to obtain rigorous bounds on approximations of ODEs. This paper proves the completeness of such proofs - if an approximation was correctly computed by some (possibly untrusted) reachability algorithm via Taylor models, then a corresponding proof in dL can be automatically generated and checked to be correct in dL's proof calculus. A dedicated proof checker is implemented in Lean4 for improved performance, which is capable of formally verifying benchmarks in the ARCH competition.

</details>

## Mathematical physics

### [Dynamical Temperley-Lieb algebras from Quiver CFTs](https://arxiv.org/abs/2611.26285v1)
*Rob Klabbers, Elli Pomoni, Ana L. Retore et al.* · `hep-th` · arXiv:2611.26285v1 · relevance 0.09

- **In one sentence**: The one-loop dilatation operator of a superconformal planar gauge theory can be written as a sum of local generators. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The one-loop dilatation operator of a superconformal planar gauge theory can be written as a sum of local generators. The algebra these generators satisfy is a powerful organising principle for the spectrum. For SU(2)-like bosonic subsectors we show that this algebra can be read off directly from Feynman diagrams, which we identify as a natural graphical language for it. For N=4 super Yang-Mills this simply reproduces the Temperley-Lieb (TL) algebra of the XXX spin chain. After orbifolding and marginally deforming to N=2 superconformal quiver theories, the same recipe yields dynamical generalisations of the TL algebra. In these theories, the faces of the diagrams are coloured according to the quiver nodes, and separated by domain walls corresponding to bifundamental fields. There are two inequivalent SU(2)-like subsectors, which lead to two different TL algebras. One sector is built from the two bifundamental scalars and (in the simplest case) gives a dynamical TL algebra with a colour-dependent loop fugacity in its quadratic relation. The other sector is built from one bifundamental and one adjoint scalar, and (always) gives a novel algebra, in which the cubic TL relation becomes dynamical. In this latter case, we show that each generator of this new algebra is related to a standard XXZ TL generator by a colour-dependent twist. This twist is local and not an algebra homomorphism, and can be written as a dynamical Drinfeld twist. In both sectors, the TL structure provides a natural graphical approach to the spectral problem, as well as clarifying the structure of the irreducible representations of these chains. Finally, we give a preliminary description of the loop models associated to these algebras.

</details>

### [Twisting Spinning Particles with Superghost Backgrounds](https://arxiv.org/abs/2611.26554v1)
*Erik Fink, Jingqian Gou, Niklas Holbach et al.* · `hep-th` · arXiv:2611.26554v1 · relevance 0.05

- **In one sentence**: We construct twists of spinning particles in the classical BV formalism by giving constant backgrounds to the bosonic ghosts of local worldline supersymmetry, in analogy with Costello and Li's twist of supergravity, which gives a nonzero background to the ghost of local spacetime supersymmetry. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We construct twists of spinning particles in the classical BV formalism by giving constant backgrounds to the bosonic ghosts of local worldline supersymmetry, in analogy with Costello and Li's twist of supergravity, which gives a nonzero background to the ghost of local spacetime supersymmetry. We represent the superghosts on polynomial states and gauge selected worldline R symmetries, imposing the shifted R constraints absolutely and the unshifted ones relatively. On flat targets, the N=2 particle, its N=4 extension on a complex target and an N=8 particle with two fermion flavors give the de Rham, Dolbeault and polynomial linear BCOV complexes. The last two are the linearized field content of the open and closed B-model target-space theories. Pairings and interactions require target-space input beyond the reduced worldline differentials.

</details>

## Optimization and control

### [The FrontierOR Challenge: Agentic Algorithm Design for Operations Research](https://arxiv.org/abs/2611.26171v1)
*Hai Wang, Bretislav Hajek, Chonghe Jiang et al.* · `cs.AI` · arXiv:2611.26171v1 · relevance 0.15

- **In one sentence**: Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. Large language model (LLM) agents now write, test and improve code, but whether they can design algorithms that scale to realistic instances is open: in the FrontierOR benchmark's one-shot evaluation, the strongest model matches Gurobi, with an objective within 1% of Gurobi's and no slower, on only 39% of the large instances. The FrontierOR Challenge asks teams to build agentic workflows that design, test, and improve algorithms for many optimization problems at once. Stage 1 releases 60 of the benchmark's 180 audited problems, spanning six application categories and five formulation types, in weekly rounds of 15; Stage 2 introduces new problems outside the benchmark, with unseen instances. Two tracks are ranked separately: in the Main track we run the submitted algorithms in a network-isolated sandbox with open-source dependencies only; in the Self-hosted track teams solve the instances on their own machines, with any software, within a timed window. Every solution is checked for feasibility, and a feasible solution scores the ratio of its objective to a frozen known reference, averaged over hidden instances.

</details>

### [Hamiltonian Potential Optimization for Partially Observed Stochastic Optimal Control](https://arxiv.org/abs/2611.26295v1)
*Christian Bayer, Saifeddine Ben Naamia, Erik von Schwerin et al.* · `math.OC` · arXiv:2611.26295v1 · relevance 0.12

- **In one sentence**: The paper replaces the infinite-dimensional belief-space HJB equation for partially observed continuous-time control with a finite-dimensional optimization over parametrized Hamiltonian potentials, uses Gaussian belief updates with adjoint gradients, smooths switching-control Hamiltonians, and certifies policies with a primal-dual information-relaxation bound.
- **In plain words**: Controlling a system when you can only see noisy, partial measurements of it is hard, because the controller must reason about its own uncertainty as well as the system's state. The authors propose a way to design controllers by tuning a small set of adjustable functions of the current state and past measurements, rather than solving an intractable equation over all possible beliefs. They test this on standard textbook-style problems, including cases where the controller also chooses when to take measurements, and pair each policy with a computed lower bound so its quality can be checked.
- **Why it matters**: The approach trades an intractable exact formulation for a finite, gradient-trainable one, and the primal-dual bound gives a way to judge how close a policy is to optimal. Its relevance to wider practice depends on how well the numerical experiments, which the abstract describes only at a high level, hold up on harder problems; I am not sure how it compares with existing approximate methods.
- **Background needed**: ['Stochastic optimal control: choosing actions over time to minimize expected cost when the system is driven by random noise.', 'Partial observation: the controller sees only noisy measurements, so it must track a belief (a probability distribution) over the hidden state.', 'Hamilton-Jacobi-Bellman (HJB) equation: the partial differential equation whose solution gives optimal cost; in belief space it is infinite-dimensional and generally unsolvable directly.', 'Hamiltonian: a function combining cost and dynamics whose minimizer gives the control action at each moment.', 'Linear-quadratic-Gaussian (LQG) problems: linear dynamics, quadratic costs and Gaussian noise, a standard benchmark with known solutions.', 'Gaussian belief: a belief summarized by a mean and covariance, as in Kalman filtering.', 'Adjoint method: a backward sweep that computes gradients of a cost with respect to parameters efficiently.', 'Information relaxation: a technique that gives lower bounds on optimal cost by relaxing the requirement that decisions depend only on available information, plus a penalty term.', 'Primal-dual gap: the difference between an achievable policy cost (primal) and a lower bound (dual) certifies how suboptimal the policy can be.'] · level: research-level

<details><summary>Original abstract</summary>

We develop a Hamiltonian potential optimization method for partially observed stochastic optimal control with continuous-time state dynamics and discrete-time noisy observations, including controlled sensing. Rather than solving the infinite-dimensional belief-space Hamilton-Jacobi-Bellman equation, we optimize over parametrized potentials depending on the state variable and the available observation history. The associated Hamiltonian minimizers induce admissible continuous controls and, when observations are controlled, sensing decisions. An extended Hamiltonian incorporating a cost multiplier provides a common representation of the induced belief dynamics and running and observation costs. This construction yields a finite-dimensional optimization problem, with gradients computed by a forward simulation and a backward discrete adjoint sweep. The numerical implementation uses Gaussian beliefs represented by conditional means and covariances. For nonsmooth Hamiltonians arising from switching controls, we introduce smooth Hamiltonian approximations to enable gradient-based optimization. To assess the resulting policies, we develop belief-space information relaxation lower bounds. A separate optimization of the dual test functional provides a lower bound which, paired with the admissible policy cost, yields an a posteriori primal-dual diagnostic. Numerical experiments investigate scalar and multidimensional linear-quadratic-Gaussian problems, controlled sensing with and without control bounds, a nonquadratic obstacle penalty, and Hamiltonian smoothing for a discontinuous control selector.

</details>

## Statistics theory

### [Sharp minimax rates and adaptive estimation of latent proportions in bivariate Poisson mixtures](https://arxiv.org/abs/2611.26047v1)
*Essoham Ali* · `math.ST` · arXiv:2611.26047v1 · relevance 0.12

- **In one sentence**: We study estimation of the mean latent composition in a bivariate Poisson mixture. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We study estimation of the mean latent composition in a bivariate Poisson mixture. Conditional on an unobserved intensity S and proportion U, two counts are independent Poisson variables with respective means SU and S(1-U). The mixing law is unrestricted on the Cartesian product [a,b] x [0,1], where a and b are finite constants satisfying 0 < a < b, and dependence between S and U is allowed. Although the mixing distribution is identifiable, the usual ratio of mean counts estimates an intensity-weighted proportion and may be biased for theta = E[U]. We construct polynomial estimators based on factorial moments and establish the exact leading exponent of the minimax squared-error risk on the logarithmic scale, without claiming an exact multiplicative minimax constant. We also derive the sharp logarithmic separation exponent for testing zero latent covariance and construct an adaptive estimator achieving parametric squared-error risk on the zero-covariance submodel while retaining the optimal full-model logarithmic minimax exponent. Simulations illustrate the bias-variance trade-off, the role of polynomial regularization, and the distinction between theoretically guaranteed and empirically calibrated adaptation.

</details>

### [Inference in High-Dimensional Linear Mediation Models](https://arxiv.org/abs/2611.25864v1)
*Samriddha Lahiry, Rajarshi Mukherjee, Pragya Sur* · `math.ST` · arXiv:2611.25864v1 · relevance 0.06

- **In one sentence**: Mediation analysis plays an important role in psychology, epidemiology, and genomics. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Mediation analysis plays an important role in psychology, epidemiology, and genomics. Al- though high-dimensional mediation has been studied extensively, existing inferential methods typically rely on sparsity assumptions that may be difficult to justify when many individually weak mediators collectively produce a substantial effect. We study inference for both the over- all indirect effect and the effect transmitted through an individual mediator in a proportional high-dimensional regime, where the number of mediators and the sample size grow at compa- rable rates, without imposing sparsity on the mediator effects. Standard debiasing procedures for high-dimensional inference commonly rely on design-covariance information or additional structural assumptions on precision-matrix directions. In mediation models, however, the full outcome-design covariance depends on unknown mediator-model coefficients, creating an addi- tional challenge when such information or structure is unavailable. To address this challenge, we introduce an approximate debiasing procedure based on partial ridge regression and show that the resulting estimator is asymptotically bias-corrected and Gaussian. We also develop a cross-fitted estimator with a smaller asymptotic variance than its sample-split counterpart. In addition, we construct consistent estimators of the limiting variances of both the sample-split and cross-fitted estimators. Together, these results provide feasible inferential procedures for global and pathwise mediation effects.

</details>

## Statistical methods and applications

### [Faithful Generative Modeling for Censored Time-to-Event Data: From Distributional Fidelity to Statistical Inference](https://arxiv.org/abs/2611.25464v1)
*Yin Liu, Shanshan Zhao, Didong Li* · `stat.ME` · arXiv:2611.25464v1 · relevance 0.15

- **In one sentence**: Synthetic data has emerged as a powerful tool for data sharing, clinical trial simulation, and digital twin development, with growing applications in biomedical research and drug development. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Synthetic data has emerged as a powerful tool for data sharing, clinical trial simulation, and digital twin development, with growing applications in biomedical research and drug development. However, limited attention has been devoted to synthetic time-to-event data, which are central to clinical trials and survival analysis. In particular, theoretical guarantees for the distributional fidelity of synthetic survival data remain largely unexplored. More importantly, even when a generator achieves distributional fidelity, it remains unclear whether the downstream statistical analysis is reliable. To address these gaps, we propose a general two-stage generative framework for survival data (TSGSurv) that jointly generates observed times and covariates conditional on event status, and establish its distributional convergence rate. Focusing on the widely used Cox proportional hazards model, we establish conditions under which generator fidelity guarantees consistency of model coefficient estimates. We further characterize the limitations of naive inference based on synthetic data, and develop a variance correction and a distribution calibration procedure to recover valid inference of original data. We demonstrate the effectiveness of the proposed generative and inferential framework with extensive simulations and two real data applications.

</details>

### [Exact Bayesian layers via characteristic functions](https://arxiv.org/abs/2611.26426v1)
*William H. W. Thompson, Guillaume St-Onge, Laurent Hébert-Dufresne et al.* · `stat.ML` · arXiv:2611.26426v1 · relevance 0.09

- **In one sentence**: The paper introduces CF-Prop, a sampling-free way to propagate uncertainty through a Bayesian ReLU layer by working with characteristic functions, which lets the variational training objective be computed in closed form for non-Gaussian likelihoods and yields the CF-VI training algorithm.
- **In plain words**: Neural networks can be built to report how unsure they are, but the usual way of estimating that uncertainty relies on repeatedly running random samples, which is slow. Earlier fast methods assumed the output uncertainty follows a bell-shaped (Gaussian) curve, which can be wrong for real problems. The authors use a mathematical transform, the characteristic function, to track the exact shape of the output uncertainty without sampling, and they report that this gives better calibration on CIFAR-100 and better tail estimates on a heavy-tailed insurance claims dataset.
- **Why it matters**: It targets a practical gap: fast uncertainty estimates that do not assume the output is bell-shaped, which matters for skewed or heavy-tailed data such as insurance losses. The abstract reports the results but not the full experimental details, so the size and generality of the gains are best checked in the full paper; the link to other fields is mainly through risk modelling and calibrated prediction.
- **Background needed**: ['Bayesian neural network: a network whose weights are probability distributions rather than fixed numbers, so predictions come with uncertainty.', 'Variational inference: training by fitting a simpler distribution to the true posterior, by maximising a score called the evidence lower bound (ELBO).', 'Monte Carlo sampling: estimating quantities by averaging many random draws; accurate but costly.', 'ReLU layer: a standard network layer that outputs the positive part of its input (zero otherwise).', 'Characteristic function: a transform that fully describes a probability distribution, similar in spirit to a Fourier transform.', 'Likelihood: the assumed distribution of observed outcomes given the model, here Gaussian, Poisson or Gamma.', "Calibration error: how far a model's stated confidence is from how often it is actually right."] · level: research-level

<details><summary>Original abstract</summary>

Bayesian neural networks provide principled uncertainty estimates, but training them with Monte Carlo sampling can be expensive. Sampling-free variational inference algorithms make training Bayesian neural networks feasible, but existing approaches assume a Gaussian output distribution, which can be inaccurate in applied problems. Here, we introduce CF-Prop, an uncertainty propagation method that uses characteristic functions to compute the exact output distribution of a Bayesian ReLU layer, without any sampling, even in non-Gaussian settings. Because CF-Prop propagates characteristic functions, the evidence lower bound---the objective of variational training---can be computed in closed form for a broad class of likelihoods, including the Gaussian, Poisson, and Gamma. This allows to implement an efficient resulting variational inference algorithm, CF-VI. On CIFAR-100, CF-VI achieves the lowest calibration error of any tested method, improving on the next best method by about 35%. On a heavy-tailed insurance claim dataset, CF-VI accurately captures tail uncertainty that is severely underestimated by both other sampling-free methods and Monte Carlo methods.

</details>

## Machine learning theory

### [Class-Conditional Conformal Triage for ICAO Face-Image Compliance under Class Imbalance](https://arxiv.org/abs/2611.25342v1)
*Mustafa Vedat Yildirim, Inna Skarga-Bandurova* · `cs.LG` · arXiv:2611.25342v1 · relevance 0.29

- **In one sentence**: Automated ICAO/ISO face-image compliance analysers provide criterion-level pass/fail decisions, yet these verdicts do not quantify uncertainty when deciding whether to accept, reject, or retake a photograph. (first sentence of the abstract; AI summaries are off)
- Matched keywords: conformal prediction

<details><summary>Original abstract</summary>

Automated ICAO/ISO face-image compliance analysers provide criterion-level pass/fail decisions, yet these verdicts do not quantify uncertainty when deciding whether to accept, reject, or retake a photograph. We investigate conformal prediction as a triage layer for BioGaze, evaluating 14 compliance criteria on the synthetic TONO benchmark. Without retraining the analyser, we fit per-criterion logistic classifiers and compare marginal and label-conditional (Mondrian) conformal prediction with conventional abstention rules using subject-disjoint splits. Marginal conformal prediction achieved approximately 0.90 overall coverage but substantially under-covered violations, with a ten-partition mean of 0.37 for one criterion. The corresponding Mondrian means ranged from 0.89 to 0.92 across criteria. However, most of the reduction in criterion-level false positives came from the logistic layer (0.145 to 0.048), while tuned abstention rules achieved lower false-positive rates than Mondrian at comparable retake rates. Bonferroni correction for joint coverage across 14 criteria required retaking nearly all images. These findings show that class-conditional conformal prediction can achieve near-target empirical coverage for minority violation classes and reveal trade-offs between statistical coverage, classification performance, and retake requirements in multi-criterion face-image compliance assessment.

</details>

### [Deviations from the NTK Regime in CNNs under Joint Depth-Width Scaling](https://arxiv.org/abs/2611.25624v1)
*Maria Matveev, Pascal Esser, Gitta Kutyniok et al.* · `cs.LG` · arXiv:2611.25624v1 · relevance 0.24

- **In one sentence**: The concentration and training-time constancy of the neural tangent kernel (NTK) depend on the interplay between network width, depth, and initialization. (first sentence of the abstract; AI summaries are off)
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

The concentration and training-time constancy of the neural tangent kernel (NTK) depend on the interplay between network width, depth, and initialization. While joint depth-width scaling has been studied in fully-connected, residual, and recurrent networks, its effects in convolutional neural networks (CNNs) remain less understood. We investigate these effects numerically in CNNs, examining NTK dispersion at initialization and kernel rotation during training. Let depth $L$ be the number of convolutional layers, and width $C$ the number of channels per layer. We find that NTK dispersion increases with $L/C$ in the critical and chaotic initialization regimes, but remains small in the ordered regime. At critical initialization, dispersion curves approximately collapse as a function of $L/C$, suggesting a nontrivial joint scaling regime. During training, kernel rotation generally increases with $L/C$, even in the ordered regime where initial dispersion is small. Together, these results suggest that $L/C$ may govern NTK deviations from the infinite-width limit in certain regimes, and that NTK concentration at initialization and stability during training exhibit different scaling behaviors.

</details>

## Large language models

### [TRAC: Efficient Diffusion Language Models for Machine Translation via Length-Aware Decoding](https://arxiv.org/abs/2611.25643v1)
*Tianyuan Li, Xihan Yang, Chenglong Wang et al.* · `cs.CL` · arXiv:2611.25643v1 · relevance 0.24

- **In one sentence**: Machine translation with large language models requires both high translation quality and low generation latency. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Machine translation with large language models requires both high translation quality and low generation latency. Accelerating translation while preserving quality is therefore essential for practical deployment. Diffusion large language models (dLLMs) can generate tokens at arbitrary target positions through iterative denoising, offering a new paradigm for parallel translation beyond sequential autoregressive decoding. However, existing methods still incur redundant computation: fixed target generation lengths waste computation on unused positions, while confidence-only commitment delays medium-confidence tokens whose predictions have largely stabilized. To address these issues, we propose TRAC, a training-free adaptive decoding method for diffusion machine translation. TRAC adapts the target generation length using source length and translation direction, with a conservative fallback to the maximum length for empty or unusually short outputs. It preserves high-confidence commitment while identifying temporally stable medium-confidence tokens for early commitment using cross-step top-1 persistence and approximate Jensen-Shannon divergence over Top-$K$ distributions. On bidirectional Chinese-English translation across FLORES-200, WMT23, and NTREX-128, TRAC reduces model forward calls by 24.9% to 36.8% and achieves sentence-level generation speedups of 1.91 to 2.19 times over Fast-dLLM, with only a 0.02-point decrease in macro-average COMET. These results demonstrate that adaptive generation lengths and stability-aware token commitment improve the efficiency of diffusion machine translation.

</details>

### [Language models represent more about emphasis than they can tell you](https://arxiv.org/abs/2611.25808v1)
*Aarne Talman, Stergios Chatzikyriakidis* · `cs.CL` · arXiv:2611.25808v1 · relevance 0.12

- **In one sentence**: The paper tests how much word-level prominence (which word is emphasized in speech) can be recovered from text alone by frozen or fine-tuned text models, prompted LLMs, and speech models, and finds that LLM representations hold more of this information than prompting elicits.
- **In plain words**: When people speak, some words get more emphasis than others, and this depends partly on the words and partly on how the speaker chooses to read them. The authors asked how much of this emphasis a language model can work out from written text, whether it can say so when asked, and how much extra a recording of speech adds. Text models and prompted chatbots did about as well as a simple 'pick the usually-stressed word' baseline, while a linear probe (a small readout trained on the model's internal numbers) found more, and speech models did best.
- **Why it matters**: It shows a gap between what a model's internal representations contain and what it reports when prompted, which matters for anyone relying on prompting to read out model knowledge. The abstract does not say how far the finding extends beyond this task, so its wider significance is uncertain.
- **Background needed**: ['Prosodic prominence: the perceived emphasis on a word in speech, shown through pitch, loudness and length.', 'Three-way task: labelling each word into one of three prominence classes; 68.8% is the best text-model accuracy reported.', 'Word-majority baseline: always guessing the most common label for each word, a simple reference point.', 'Frozen vs. fine-tuned models: frozen models keep their original weights; fine-tuned models have been further trained on the task.', 'Prompting: asking a model a question in natural language, without changing its weights.', "Linear probe: a simple linear classifier trained on a model's internal activations to test what information they contain.", 'Representation vs. report: a model can encode information internally without it appearing in its answers.'] · level: intermediate

<details><summary>Original abstract</summary>

Prosodic prominence can largely be predicted from the words of a sentence, but part of it depends on how the speaker reads it. We study how much of prominence language models recover from text, whether they can report it when asked, and what the speech signal adds. On read English speech labelled for word-level prominence, we compare frozen and fine-tuned text models, prompted large language models (LLMs) and speech models on the same words. All text models end within about one point of each other, at best 68.8% on the 3-way task, and largely make the same errors. With the prompts we tested, LLMs do no better than a word-majority baseline, even with 500 examples. Linear probes find more in their representations. Speech models reach 84.7%. We argue that text determines only part of prominence, and that the rest has to be heard. LLMs encode what the text determines, but prompting does not bring it out: they represent more about where the emphasis falls than they tell you.

</details>

## Computer vision

### [Digitization of Analogue Gauges using Computer Vision](https://arxiv.org/abs/2611.26262v1)
*Erico Kayumba Mutonkole, Olasupo Ajayi, Omowunmi Isafiade* · `cs.CV` · arXiv:2611.26262v1 · relevance 0.23

- **In one sentence**: Analogue gauges remain prevalent in manufacturing industries for measuring physical quantities, yet manual monitoring by operators introduces human error and operational inefficiency. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Analogue gauges remain prevalent in manufacturing industries for measuring physical quantities, yet manual monitoring by operators introduces human error and operational inefficiency. This research developed and evaluated an automated gauge reading system using computer vision and deep learning techniques. Three hybrid approaches were implemented and compared: OpenCV with Scikit-Image (traditional computer vision), OpenCV with ResNet18, and OpenCV with VGG19 (deep learning approaches). A comprehensive dataset of 1,848 pressure gauge images (0-10 BAR range) was curated through web scraping, synthetic generation, and augmentation techniques. The experimental results demonstrate that ResNet18 significantly outperforms the alternatives, achieving an accuracy of 97.3%, compared to VGG19's 64.4% and Scikit-Image's 63.8%. The study validates the effectiveness of residual learning architectures for industrial gauge digitization, providing a robust foundation for Industry 5.0 automation applications.

</details>

### [TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling](https://arxiv.org/abs/2611.25847v1)
*Junchi Zhang, Zihan Gu, Jiangcan Jia et al.* · `cs.CV` · arXiv:2611.25847v1 · relevance 0.16

- **In one sentence**: TrajCal is a training-free method that uses scatter search to find one fixed timestep schedule for few-step flow-matching samplers, selected by how closely the few-step output matches a many-step reference, and reuses it across new inputs and image styles.
- **In plain words**: Modern image and video generators build their output through many small refinement steps, and each step runs a large neural network, which is slow. Faster versions take fewer steps but can distort the result compared with the slow, full version. The authors propose TrajCal, which searches for a good fixed schedule of step timings, scored by how well the quick output matches the slow reference, and reports better agreement at low step budgets while keeping visual quality competitive.
- **Why it matters**: Cutting the cost of generation without retraining the model is a practical goal for image and video tools. The abstract does not give the baselines, metrics, or budgets in detail, so its scale of gain is hard to judge from this text alone; the method may also be relevant to other few-step samplers, but the abstract does not claim that.
- **Background needed**: ['Flow matching: a generative method that turns noise into an image by following a learned velocity field over a sequence of steps.', 'Sampling steps and schedules: the number and timing of steps set the trade-off between speed and output quality; a schedule is the list of those timings.', 'Few-step sampling: generating with far fewer network evaluations than the standard many-step process, which can introduce errors.', 'Reference fidelity: how closely a fast output matches the output of a slow many-step reference run on the same input.', 'Scatter search: a population-based metaheuristic that combines and modifies candidate solutions to explore hard optimization problems.', 'Training-free: the method adjusts how sampling is done and does not retrain the generative model.'] · level: research-level

<details><summary>Original abstract</summary>

Flow matching enables high-quality image and video generation, but its iterative sampling process requires repeated evaluations of large neural networks. Existing few-step methods can distort the output and reduce its agreement with a many-step reference. We propose TrajCal, a training-free calibration framework for few-step sampling. Based on scatter search, a well-established metaheuristic for difficult optimization problems, TrajCal starts with diverse seed schedules, deforms and combines these candidates, and selects one fixed schedule by final output fidelity for reuse on new inputs. For both image and video generation, TrajCal achieves higher reference fidelity than all compared baselines at low evaluation budgets while maintaining competitive visual quality. The search is effective even with randomly generated seeds, while trajectory-based seeds further improve fidelity. For cross-style generalization, photography-calibrated schedules also improve fidelity on unseen image styles.

</details>

## Reinforcement learning

### [Decision-Focused Reinforcement Learning for LLM Post-Training](https://arxiv.org/abs/2611.25597v1)
*Haotian Zhai, Leqi Liu* · `cs.LG` · arXiv:2611.25597v1 · relevance 0.22

- **In one sentence**: The paper post-trains LLMs to produce optimization parameters by using negative downstream decision regret as the RL reward, with two reward-cost reduction schemes (heuristic warm-starting and randomized reward correction) for when exact evaluation is expensive.
- **In plain words**: An AI model that forecasts things, like demand, is usually trained to be accurate, but a forecast that is accurate on average can still lead to poor decisions when someone plans around it. The authors train a language model to make forecasts judged by the cost of the decisions they lead to, using a reward signal that penalizes extra cost compared with the best possible decision. On three synthetic problems and a knapsack task, they report gains over methods trained only on prediction error; on an inventory planning task using H&M sales and product descriptions, they report regret reductions of 31.4% versus a supervised fine-tuning baseline and 12.4% versus the strongest conventional forecasting baseline they tested.
- **Why it matters**: It targets the gap between prediction accuracy and decision quality, a theme in the 'predict-then-optimize' literature, and applies it to LLM post-training, where text context is used for forecasts. The abstract does not show how far the results generalize beyond the tested tasks, so the broader significance is uncertain.
- **Background needed**: ['Post-training of LLMs: fine-tuning a pretrained model with supervised examples and then with reinforcement learning.', 'Reinforcement learning basics: a policy is updated to increase expected reward, often via policy gradients.', 'Predict-then-optimize: a model forecasts parameters, which feed a downstream optimization problem that chooses a decision.', 'Decision regret: the extra cost of a decision made from a forecast compared with the decision made with perfect information.', 'Prediction loss versus decision cost: a forecast can have low error yet still produce a costly decision.', 'Reward approximation: exact reward evaluation requires solving the optimization problem, which can be expensive, so cheaper estimates are used.'] · level: research-level
- Matched keywords: reinforcement learning, policy gradient

<details><summary>Original abstract</summary>

Large language models (LLMs) have shown promise as predictors across various tasks, benefiting from their ability to use information from unstructured context. However, when predictions serve as parameters of downstream optimization problems, higher prediction accuracy does not necessarily translate into lower decision costs. We propose decision-focused reinforcement learning (DFRL), a framework for post-training LLMs to predict optimization parameters using negative downstream decision regret as reward. DFRL trains LLM predictors to minimize the costs of the decisions induced by their predictions, without requiring downstream convexity or differentiability, and integrates readily into existing RL post-training frameworks. To address expensive reward evaluation, we develop two approaches. Heuristic warm-starting uses inexpensive approximate rewards during an initial phase before switching to refinement with exact rewards. Reward correction combines inexpensive estimates with randomized exact evaluations, preserving the expected policy gradient while reducing the expected number of exact solves per update. Experiments on three synthetic optimization problems demonstrate improvements over prediction-loss baselines, while a larger knapsack experiment shows faster early improvement under short training budgets. On inventory planning with H&M transactions and product descriptions, our best configuration, in which the LLM reasons before predicting, reduces regret by 31.4% relative to the SFT baseline and 12.4% relative to the strongest evaluated conventional forecasting baseline.

</details>

### [Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models](https://arxiv.org/abs/2611.25742v1)
*Yajie Qi, Wei Wei, Lin Li et al.* · `cs.LG` · arXiv:2611.25742v1 · relevance 0.17

- **In one sentence**: Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. (first sentence of the abstract; AI summaries are off)
- Matched keywords: reinforcement learning

<details><summary>Original abstract</summary>

Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. Large language models (LLMs) can guide exploration by generating high-level goals, but methods using models without explicit task adaptation often rely on carefully designed prompts and may produce inconsistent or contextually inappropriate goals. We introduce CCGP-2M, a multimodal goal-preference dataset constructed from interaction trajectories in Craftax-Classic, and propose a vision-language model (VLM)-guided RL framework that learns environment-specific goal guidance from this dataset. The framework consists of two stages: offline VLM fine-tuning and online goal-guided RL. In the offline stage, we align the VLM with goal preferences using Kullback-Leibler Token-level Direct Preference Optimization (KLTDPO), which combines token-level KL regularization with distributionally robust reweighting. Experiments on Craftax-Classic show that our method collects diamonds earlier than state-of-the-art baselines, achieves the highest score and reward, and attains the highest success rates on most achievements.

</details>

## AI safety and alignment

### [Reinforcing Few-Step Diffusion Models via Shadow Posterior Matching](https://arxiv.org/abs/2611.25998v1)
*Jingqiao Xiu, Yicong Li* · `cs.LG` · arXiv:2611.25998v1 · relevance 0.22

- **In one sentence**: Few-step diffusion models are widely deployed for their efficiency. (first sentence of the abstract; AI summaries are off)
- Matched keywords: reward hacking

<details><summary>Original abstract</summary>

Few-step diffusion models are widely deployed for their efficiency. However, reinforcing them with black-box rewards, as is routine for multi-step models, faces two structural challenges. First, a few-step generator is a sampler rather than a score model, so its velocity is not the forward velocity of the generated distribution. Second, it must be anchored to the undistilled teacher, which shares no transitions with it. Existing few-step RL methods handle the latter with a marginal KL to the teacher, but each pays for the former in its reward credit. We propose Shadow Posterior Matching (SPM), which renoises generated samples into shadow inputs and obtains the credit from their shadow posterior. From the KL-regularized reward objective, we derive a regression loss that turns reward values into a reward direction while anchoring the generator's outputs to the teacher and aligning the shadow inputs with the deployed inputs. Applied to 4-step generators, SPM achieves higher rewards with less reward hacking than prior few-step RL methods.

</details>

### [Whose Safety? Addressing Anti-Blackness in the Age of AI Safety](https://arxiv.org/abs/2611.25302v1)
*Mírian Silva, Serena Oduro* · `cs.CY` · arXiv:2611.25302v1 · relevance 0.20

- **In one sentence**: "AI safety" has grown from a niche contingent of actors into the dominant framing for artificial intelligence (AI) assessment and evaluation, overshadowing AI ethics. (first sentence of the abstract; AI summaries are off)
- Matched keywords: AI safety

<details><summary>Original abstract</summary>

"AI safety" has grown from a niche contingent of actors into the dominant framing for artificial intelligence (AI) assessment and evaluation, overshadowing AI ethics. Through political and monetary influence, AI safety has shifted political focus within the US and abroad. The focus has shifted away from harms that currently affect the public toward threats framed as "existential risks". We argue that safety cannot be achieved while anti-Blackness is left unaddressed. We ground this argument in Sylvia Wynter's critique of the "overrepresentation" of Man: the modern, Western conception of the Human that is predicated on the subjugation and othering of Blackness. To analyze the state of addressing anti-Blackness in the age of AI safety, we conduct a two-stage, language model-assisted content analysis of 69,290 accepted main-track papers from ten leading machine learning (ML), natural language processing (NLP), and AI ethics conferences (2020--2025). Safety research grew from 0.5% of accepted papers in 2020 to 6.4% in 2025, overtaking ethics. Yet 94% of safety papers rely on automated metrics, and only 11% of safety papers mention harms that affect society directly, compared with 78% of ethics papers. Of the 2,182 safety papers, 8 mention race; none make it central, and none name Black or African-diaspora communities. Across all 254 identified as race-focused papers, only 3 describe racial harm in safety terms, and 55% appear at three ethics venues that publish 2.5% of the corpus. We offer this interdisciplinary examination of AI safety to argue that a just technological future depends on confronting anti-Blackness directly.

</details>

## Interpretability

### [X Hedging: towards an eXplainable artificial intelligence option Hedging framework](https://arxiv.org/abs/2611.25870v1)
*Bjørn André Aaslund, Johannes Berge, Ayoub Haida et al.* · `cs.LG` · arXiv:2611.25870v1 · relevance 0.18

- **In one sentence**: We propose X Hedging, an alternative to the Deep Hedging framework that addresses computational and explainability limitations of neural-network-based hedging strategies. (first sentence of the abstract; AI summaries are off)
- Matched keywords: explainability

<details><summary>Original abstract</summary>

We propose X Hedging, an alternative to the Deep Hedging framework that addresses computational and explainability limitations of neural-network-based hedging strategies. Deep Hedging leverages neural networks to learn flexible hedging policies but relies on opaque models and typically requires large training datasets, which can complicate interpretation and limit its effectiveness in data-constrained settings. X Hedging takes a step toward addressing these limitations by replacing neural networks with tree ensemble methods, specifically LightGBM, to estimate hedging strategies. This design provides a computationally efficient alternative while preserving strong hedging performance and moving toward more user-centered explainability. To integrate LightGBM into a reinforcement-learning-style hedging framework, we introduce an optimization approach that sequentially trains tree-ensemble models while introducing stochasticity through random training orders. In controlled experiments, X Hedging achieves performance comparable to Deep Hedging while offering greater user-centered explainability, improved computational efficiency, and substantially higher robustness when training data are limited. The numerical results demonstrate that tree-ensemble methods provide an effective computational alternative to neural networks for data-driven dynamic hedging.

</details>

### [Explainable AI for Solar PV Power Forecasting: From Model Selection to Trustworthy, Reproducible Deployment](https://arxiv.org/abs/2611.25894v1)
*Nuzhat Khan, Muhammad Paend Bakht, Ab Al-Hadi Ab Rahman et al.* · `cs.AI` · arXiv:2611.25894v1 · relevance 0.13

- **In one sentence**: Machine learning (ML) is now a standard tool for forecasting the output of solar photovoltaic (PV) plants, yet published accuracy figures are often hard to compare and harder to trust. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Machine learning (ML) is now a standard tool for forecasting the output of solar photovoltaic (PV) plants, yet published accuracy figures are often hard to compare and harder to trust. Many studies validate with random splits, report no reference forecast, and present feature attributions without saying what they can and cannot show. This paper reviews the main families of ML methods for PV power forecasting and resource assessment, from tree ensembles to deep and foundation models, and sets out a reproducible workflow that combines automated model search with explainable AI. The workflow is then tested on an openly available dataset: a 16.32 kWp plant in Porto, Portugal, forecast one day ahead from a 4 km numerical weather prediction grid. Over a full test year, the best models reach a normalised root mean square error (nRMSE) of 11.6% of installed capacity, about half the error of smart persistence. The choice of input features changed accuracy far more than the choice among strong algorithms, and shuffled cross-validation was mildly optimistic. After conformal calibration, the nominal 80% prediction intervals covered 81.7% of observations, against 64.5% before. SHAP rankings stayed stable when the model was retrained on different periods but shifted when correlated inputs were removed, so attributions should be read as properties of a model rather than of the plant. The paper closes with practical lessons and open problems, including deployment on edge hardware and the effect of a changing climate.

</details>

## AI for mathematics

### [Budget Internalization: Fixed-Budget RLVR Trades Test-Time Scaling for In-Budget Accuracy](https://arxiv.org/abs/2611.26172v1)
*Ilia Zavidnyi, Alexander Kovrigin, Arina Puchkova et al.* · `cs.LG` · arXiv:2611.26172v1 · relevance 0.13

- **In one sentence**: Reasoning models often become more accurate when they can generate longer answers at test time. (first sentence of the abstract; AI summaries are off)
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Reasoning models often become more accurate when they can generate longer answers at test time. This behavior is known as test-time scaling. However, RL with verifiable rewards (RLVR) usually trains them with a fixed rollout cap. We find that this cap changes model behavior, not only training cost. After training, models use few additional tokens beyond the training budget. They outperform the base models near that budget, but their accuracy stops improving and falls below the base model at larger budgets. The rollout cap thus becomes a learned constraint, that limits model's test-time scaling. We call this effect budget internalization. We observe it across Qwen3.5-4B, Gemma4-E2B, and Nemotron-3-Nano-4B and two reasoning training tasks: mathematical reasoning and diverse, procedurally generated problems. This effect also transfers from math training to science and coding tasks. Training-objective level ablations on Qwen3.5-4B show that most changes recover little test-time scaling. Stronger KL regularization and lower training-data truncation preserve more scaling, but stronger KL reduces in-budget accuracy. Forcing an answer on truncated training rollouts largely removes budget internalization, but also removes most of the in-budget gain. SFT on artificially truncated traces reproduces budget internalization, whereas SFT on naturally short traces does not, which shows that the effect is not specific to RL. This result links budget internalization to length-censored post-training rather than to an RL-specific objective term. Thus, a rollout cap does not only control training cost. It can trade low-budget gains for lower performance when additional inference compute is available.

</details>

### [Closing Performance Gap for Diffusion Language Models under Low Inference Budgets](https://arxiv.org/abs/2611.25763v1)
*Hao Wu, Sipeng Chen, Jingwen Fu et al.* · `cs.CL` · arXiv:2611.25763v1 · relevance 0.12

- **In one sentence**: Diffusion language models offer an architectural route to low-budget generation by updating multiple tokens in parallel, which can reduce the number of sequential decoding steps relative to token-by-token autoregressive decoding. (first sentence of the abstract; AI summaries are off)
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Diffusion language models offer an architectural route to low-budget generation by updating multiple tokens in parallel, which can reduce the number of sequential decoding steps relative to token-by-token autoregressive decoding. However, realizing this advantage at low budgets is challenging, as generation quality often declines when the number of denoising and refinement steps is reduced. Editable diffusion models address this quality loss through post-draft refinement, but useful intermediate results may still be lost before final submission. We introduce CaRR (Commitment-aware Refinement and Recovery), a training-free framework which improves submission quality from a fixed editable checkpoint through updated-context refill and trajectory-based recovery within its existing forward schedule. Token Commitment Remasking (TCR) remasks selected native pure replacements and refills them on the next scheduled edit forward using the updated context. Submission Commitment Recovery (SCR) uses the resulting refinement trajectory to recover supported candidates when the final response does not satisfy task-specific output requirements. Both modules operate within the native mask/edit schedule without additional backbone forwards. Experiments on code generation and mathematical reasoning show consistent gains in average accuracy over native ME-DLM across four inference budgets, with the largest gains under tight budgets. At one-eighth of the full scheduled forward budget, CaRR improves the six-metric average accuracy by 7.44 pp, including gains of 11.37 and 10.05 on MBPP and MBPP+.

</details>

## Robotics and embodied AI

### [Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models](https://arxiv.org/abs/2611.25980v1)
*John Won, Yonghoon Dong, Jinwoo Shin* · `cs.RO` · arXiv:2611.25980v1 · relevance 0.20

- **In one sentence**: World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world. Yet despite producing increasingly realistic videos, current world models often fail to capture how small action changes affect future observations. This limits their use in tasks such as robotic policy evaluation and model-based planning, where nearly identical actions can lead to qualitatively different outcomes. To address this, we propose AFFECT, an auxiliary training objective for learning the distribution of visual changes induced by action perturbations. Specifically, we inject temporally correlated noise into the actions of a policy trained on task-agnostic human teleoperation. We then train the world model so that its generated videos respond to this noise as the recorded videos do, without requiring repeated executions from the same initial state. Across OGBench simulation and real-world DROID and ALOHA-2 setups, AFFECT makes world-model rollouts more faithful to real outcomes. On DROID, the Pearson correlation between policy success rates in the world model and on the real robot rises from 0.47 to 0.79, alongside up to 23% lower FVD. These gains carry over to planning, where selecting actions with AFFECT-trained world models improves task success by up to 8.3%.

</details>

### [MoRE: Mixture-of-Experts for Multi-Physics Robotic World Models](https://arxiv.org/abs/2611.25336v1)
*Ziyu Zhu, Shaowei Liu, Albert J. Zhai et al.* · `cs.RO` · arXiv:2611.25336v1 · relevance 0.19

- **In one sentence**: MoRE is a 3D world model for robots that uses a mixture of motion experts, one each for rigid, deformable, and prehensile (grasping) dynamics, and plugs into model predictive control for manipulation.
- **In plain words**: A robot that plans its moves needs a model of how objects will move in response to its actions, but objects behave very differently: a rigid block, a squishy cloth, and a held object each follow different physics. The authors split these cases into separate 'expert' sub-models inside one network, so each type of motion gets its own specialized treatment. They report that this improves prediction accuracy across these regimes and gives better results when the model is used to control a real robot.
- **Why it matters**: Robots that must handle many kinds of objects need predictive models that do not blur together different physical behaviors, so this design choice is relevant to manipulation research. The abstract gives only a high-level summary, so the size of the gains and how broadly they hold are unclear without the full paper.
- **Background needed**: ['World model: a learned model that predicts how the environment will change after an action, used by robots to imagine outcomes before acting.', "Mixture of experts: a neural network design where a gating mechanism routes inputs to specialized sub-networks ('experts') rather than using one network for everything.", 'Rigid vs. deformable dynamics: rigid objects keep their shape when pushed, while deformable ones (cloth, dough, rope) bend and change shape, which needs different modeling.', "Prehensile manipulation: actions where the robot grasps and holds an object, so the object's motion is tied to the gripper.", 'Model Predictive Control (MPC): a planning method that repeatedly simulates candidate action sequences with a model, picks the best one, executes the first step, and replans.', 'Sim-to-real data: training on a mix of simulated and real-world recordings to cover more cases than real data alone provides.'] · level: research-level

<details><summary>Original abstract</summary>

A robotic world model should predict how objects evolve under robot actions and physical dynamics. While recent 3D world models have shown strong predictive capabilities, they still struggle with the heterogeneous dynamics arising from diverse object interactions. To address this in a unified framework, we decompose robotic interactions into distinct physical regimes and assign each to a specialized motion expert. We introduce MoRE, a 3D world model with a mixture of motion experts organized around rigid, deformable, and prehensile dynamics. This design enables a single model to capture diverse physical behaviors while preserving regime-specific priors. Trained on mixed simulation and real-world data, MoRE integrates with Model Predictive Control (MPC) to support diverse manipulation tasks. Experiments show that MoRE improves prediction accuracy across physics regimes, leading to stronger real-world MPC performance. Code, data, and project website are available at https://alwaysleepy.github.io/MoRE-WM-site/.

</details>

## Security and cryptography

### [Correctable Enrollment and One-Transaction Seed Proofs for Ethereum's Post-Quantum Transition](https://arxiv.org/abs/2611.25663v1)
*Xin Jin, Maximillian Liao, Handong Chen et al.* · `cs.CR` · arXiv:2611.25663v1 · relevance 0.12

- **In one sentence**: A quantum computer running Shor's algorithm can extract the private key of every Ethereum account whose public key is published, and accounts exposed by their own transactions hold 54.6% of execution-layer ETH. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

A quantum computer running Shor's algorithm can extract the private key of every Ethereum account whose public key is published, and accounts exposed by their own transactions hold 54.6% of execution-layer ETH. As the first such machine may stay secret, a migration cannot wait for visible thefts, and once keys are extractable, legacy signatures no longer tell owners from attackers. We design a migration in which owners enroll post-quantum keys cheaply with their existing signatures before ECDSA is retired at a scheduled time, while a zero-knowledge proof of the wallet's BIP-39 seed can correct any such enrollment until a common deadline afterward; an account nobody enrolled stays frozen and recoverable by seed proof without a deadline. Each proof binds the new key, a nonce and a fee cap, so neither a paying sponsor nor a reordering block builder can redirect or replay it. Validators switch to hash-based keys first, at a finalized checkpoint and under a stated bound on the attacker's voting power. We prove the account guarantees under explicit assumptions, model-check the rules, and implement the design in go-ethereum and a Lean consensus client. A three-layer recursive hash-based STARK yields a seed proof of about 190 KB that fits one transaction, verifies in 38 ms and takes a median of 111 s to generate on a laptop; four proofs aggregate into one. In a ten-node simulation with mainnet-derived accounts and fee demand, block space rather than proving sets the duration: the 4.45 million accounts with at least 0.1 ETH would migrate in 29.4 days if all enroll before ECDSA is retired and in 235 days if all recover after it in batches of four. In a mass enrollment, an enrollment waits a median of 19.1 minutes in the public mempool, longer than published estimates for a fast quantum computer to extract its key, so owners with a seed and an unexposed key should migrate by seed proof.

</details>

### [GPU-Accelerated Secure Inference for Drug--Target Interaction Prediction](https://arxiv.org/abs/2611.25664v1)
*Sikha Pentyala, Steven Golob, Daniil Filienko et al.* · `cs.CR` · arXiv:2611.25664v1 · relevance 0.11

- **In one sentence**: Deep learning models that predict drug--target interactions (DTI) can speed up drug discovery, but the candidate drugs they score are valuable intellectual property that their owners cannot reveal. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Deep learning models that predict drug--target interactions (DTI) can speed up drug discovery, but the candidate drugs they score are valuable intellectual property that their owners cannot reveal. Secure multiparty computation (MPC) lets two servers compute a prediction on a secret-shared drug, without either server learning the drug. However, secure inference of deep models is slow. Non-linear operations require communication between the servers, and MPC arithmetic does not map naturally to GPUs. In this paper, we present our solution to Track~III of the iDASH 2026 privacy and security competition, which asked for fast two-party secure DTI inference on GPUs. Our solution is built on the co-design of MPC-friendly models and MPC protocols. On the model side, we design SlimDTA, a DTI model that reduces the operations on the secret drug, and in particular the non-linear operations that require communication. On the protocol side, we build a GPU framework that evaluates the linear layers with additive secret sharing and the non-linear layers with function secret sharing, including a custom CUDA kernel for the comparisons. Our solution won first place in the competition, at under 10,ms per prediction on average, and its secure predictions match the plaintext model to within 0.02%.

</details>

## Algorithms and complexity

### [Running-Time Lower Bounds under FPT $\neq$ W[1]](https://arxiv.org/abs/2611.26080v1)
*Hendrik Molter* · `cs.DS` · arXiv:2611.26080v1 · relevance 0.20

- **In one sentence**: We revisit running-time lower bounds historically based on the Exponential Time Hypothesis. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We revisit running-time lower bounds historically based on the Exponential Time Hypothesis. Our case study asks how much of their quantitative content can be recovered under the assumption FPT $\neq$ W[1]. The reductions encode the choice of a clique in few bits and control the target parameter in terms of that encoding. This makes a sufficiently fast algorithm for the target problem yield a fixed-parameter algorithm for deciding whether a graph has a clique of the requested size. We obtain twelve lower bounds for deterministic algorithms across graph, string, and integer feasibility problems, including bounds that hold under structural restrictions. In several cases the same function of the parameter appears in the exponent as in the historical bound, with the additional requirement that the cutoff for any prescribed saving in the exponent be computable.

</details>

### [Approximation Algorithms for Asymmetric Multi-Path TSP](https://arxiv.org/abs/2611.26188v1)
*Manuel Christalla, Vera Traub* · `cs.DS` · arXiv:2611.26188v1 · relevance 0.18

- **In one sentence**: Asymmetric Multi-Path TSP is the generalization of the Asymmetric Traveling Salesperson Problem where we are looking for $k$ walks, each with prescribed start $s_i$ and prescribed end $t_i$, such that every vertex is visited by at least one of the walks. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Asymmetric Multi-Path TSP is the generalization of the Asymmetric Traveling Salesperson Problem where we are looking for $k$ walks, each with prescribed start $s_i$ and prescribed end $t_i$, such that every vertex is visited by at least one of the walks. The objective is to minimize the total length of all walks. In general, it is NP-hard to find any approximation for this problem in polynomial time (even if the approximation factor is allowed to depend on the number of vertices). We show that one can obtain an $O(k)$-approximation in time $n^{O(k)}$, answering an open question by Friggstad [2013]. For the special case where all tour start vertices $s_i$ are identical and all end vertices $t_i$ are identical, we obtain an $O(k)$-approximation in polynomial time, as well as an $(O(\frac{1}ε), 1+ε)$-bicriteria approximation. For the multi-depot setting, where $s_i =t_i$ for all $i$, we obtain a constant-factor approximation in polynomial time. Finally, our results imply improved constant-factor approximation algorithms for Asymmetric Regret-Bounded Vehicle Routing and unit-weight Path ATSP.

</details>

## Programming languages and formal methods

### [Static Analysis Guidance for Secure LLM Code Generation](https://arxiv.org/abs/2611.26312v1)
*Daniele Lunghi, Alberick Euraste Djiré, Zacharie Chenail-Larcher et al.* · `cs.SE` · arXiv:2611.26312v1 · relevance 0.13

- **In one sentence**: The paper compares two ways of feeding static-analyzer warnings into an LLM during code generation (as a code comment or in the user message, after rolling back on an alert) against iterative repair loops and a no-analyzer control, measuring functional and secure output on three Python benchmarks.
- **In plain words**: AI models that write code often produce programs with security holes, and tools that scan code for such problems can point them out. This paper tests a cheaper way to use those scanner reports: when the scanner flags a problem during writing, the model's draft is rolled back and the warning is fed back as a code comment or as part of the user's message. The authors report that this costs roughly 0.9 to 1.9 times the baseline's output, compared with up to 24 times for repeated fix-and-retry loops, and it raised the share of correct, secure programs in one tested setup from 52.5% to 64.4%.
- **Why it matters**: Scanner-guided generation is a practical middle ground between no feedback and costly repair loops, and the paper also reports when it backfires, such as when a warning conflicts with the task. Its results come from specific models and benchmarks, so how well they transfer to other settings is an open question.
- **Background needed**: ['Static analyzer: a tool that inspects code without running it and reports suspicious patterns, such as possible security flaws.', 'LLM code generation: a large language model writes program source code from a natural-language request.', 'Iterative repair loop: generate code, run the analyzer, ask the model to fix the reported issues, and repeat, which costs many extra model calls.', 'Rollback: discarding the partially generated output and restarting from the point where the alert appeared.', 'Functional vs. secure: a program can be correct for its task yet still contain a security vulnerability; benchmarks check both with test oracles.', 'Output tokens: the text units a model produces; a common proxy for compute cost.', "False or conflicting alerts: analyzer warnings that do not match the task's actual requirements, which can push the model toward a wrong program."] · level: intermediate

<details><summary>Original abstract</summary>

Static analyzers are cheap and widely deployed, which makes their reports a candidate feedback signal for secure LLM code generation. Existing approaches place the analyzer inside an iterative repair loop with intermediate steps, which is costly and makes it hard to isolate the report's effect on the model. We introduce two strategies that give the finding to the model during generation. When the analyzer raises an alert, generation is rolled back, and the finding is inserted either as a code comment (Comment) or in the user message (Steering). We compare them with two iterative approaches and a control without the analyzer, across three models and three Python benchmarks, and we measure security using each benchmark's oracle. Guidance during generation is cheap and can be effective, at 0.9 to 1.9 times the baseline's output tokens against up to 24.1 times for iterative approaches. With DeepSeek-V4.1-flash on RiskyPy, Steering raises the share of functional and secure programs from 52.5% to 64.4%, close to the best iterative approach (66.2%) while using less than a fifth of the tokens. A per-rule analysis shows that rules with a local fix benefit most, and replacing the XML parser is net-positive on two of the three models. The study also identifies when guidance should not be applied. Analyzers flag at most 5.6% of the functional but insecure programs on SecEvalPlus, leaving little guidance to act on. When a static analysis alert (warning or error) contradicts the task, models tend to follow the analyzer and break the program. The two Qwen2.5 models often fail when the fix requires restructuring the code. These results indicate that static-analysis guidance is worth applying with a capable model, on rules with a local fix, and after filtering alerts that conflict with the task specification.

</details>

### [On the semantics of conditional branching](https://arxiv.org/abs/2611.26400v1)
*Fredrik Dahlqvist* · `cs.LO` · arXiv:2611.26400v1 · relevance 0.12

- **In one sentence**: Motivated by the non-standard interpretations of if-then-else in probabilistic and quantum programs we review the different semantics of conditional branching and propose a unifying categorical structure for the interpretation of if-then-else. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Motivated by the non-standard interpretations of if-then-else in probabilistic and quantum programs we review the different semantics of conditional branching and propose a unifying categorical structure for the interpretation of if-then-else. We show that many semantically important categories possess this structure, covering inter alia classical, probabilistic, quantum or non-deterministic computations. We examine algebraic structures related to and generated by this categorical structure, in particular on collections of predicates. In this setting we show that the skew-associativity rules of GKATs and barycentric algebras are two instances of a common skew-associativity rule.

</details>

## Systems and networking

### [Matching Architecture to Workload: Comparing RISC-V Parallel Accelerators for Energy-Efficient Embedded Computing](https://arxiv.org/abs/2611.25947v1)
*Luca Colombo, Luigi Ghionda, Amirhossein Kiamarzi et al.* · `cs.DC` · arXiv:2611.25947v1 · relevance 0.09

- **In one sentence**: Embedded computing demands high performance and energy efficiency across workloads with widely different computational characteristics. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Embedded computing demands high performance and energy efficiency across workloads with widely different computational characteristics. Choosing the most suitable execution model therefore requires a quantitative understanding of how each model maps to different workload classes. In this paper, we compare three execution models for energy-efficient embedded computing: scalar multicore, stream ing multicore, and vector processing. We use three open-source RISC-V accelerators as representative implementations: the PULP Cluster, the Snitch Cluster, and Spatz, respectively. Their open-source hardware and software stacks enable a controlled comparison based on implementations in the same 12 nm technology and a common benchmark suite. Our results reveal that no single execution model performs best across all workload classes. Spatz delivers the greatest benefits for regular and highly vectorizable compute-intensive applications, achieving up to 4.29x higher performance and 5.17x greater energy efficiency than the other architectures. However, its effectiveness strongly depends on the availability of data-level parallelism and regular computation and memory-access patterns, making it the most sensitive to workload characteristics. The Snitch Cluster performs particularly well on applications with limited parallelism and streamable memory-access patterns, providing up to 5.53x higher performance and 1.45x greater energy efficiency. Conversely, the PULP Cluster is most effective on irregular and control-dominated applications, achieving improvements of up to 5.66x in performance and 2.80x in energy efficiency. Compared with Spatz, however, the greater flexibility offered by PULP and Snitch comes at a non-negligible cost in terms of both area and power.

</details>

### [From Seed to BLOOM: Autonomously Growing a Better Out-of-Order Core](https://arxiv.org/abs/2611.26517v1)
*Angela Cui, Ferran Hermida-Rivera, Jack Toubes et al.* · `cs.AR` · arXiv:2611.26517v1 · relevance 0.08

- **In one sentence**: Improving microprocessor performance while meeting ASIC implementation constraints like area and frequency is a complex and labor-intensive task that requires expertise across computer architecture, hardware design, and performance analysis and profiling. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Improving microprocessor performance while meeting ASIC implementation constraints like area and frequency is a complex and labor-intensive task that requires expertise across computer architecture, hardware design, and performance analysis and profiling. While large teams in industry can afford the engineering resources to target this problem across performance modeling, RTL design, and ASIC implementations, small teams of researchers and engineers cannot take on this huge engineering burden while keeping up with the pace of advancement in processor microarchitecture. Recent advancements in large language model (LLM) agents present a promising substrate to accelerate this traditionally human-intensive process. In this work, we build and evaluate MiracleGro, an agentic AI-based system that, without human intervention, analyzes cycle-level RTL behavior and synthesis results, identifies performance bottlenecks, and translates architectural ideas into RTL implementation in a leading open-source out-of-order superscalar application core, the Berkeley Out-of-Order Machine (BOOM). Taking into account cycle-exact performance, area, and critical path, MiracleGro automatically produces improved BOOM designs that drastically increase the human-optimized BOOM's performance on substantial workload suites such as SPEC CPU2017 with full reference inputs. MiracleGro achieves an 85% IPC speedup and a frequency improvement of 27% in SkyWater 130nm, resulting in a 2.34x wall-clock time speedup on the full SPEC CPU2017 intspeed benchmarks (30 trillion instructions). This result demonstrates the enormous opportunity to harness frontier models to improve state-of-the-art RTL-driven platforms for implementation-grounded microarchitecture research across hardware designs.

</details>

## Human-computer interaction

### [Rethinking Utility in Differentially Private Visualization: A Channel-Centric Perspective](https://arxiv.org/abs/2611.26396v1)
*Jing Yang, Sarayu Pacca, Zhaocong Yang et al.* · `cs.HC` · arXiv:2611.26396v1 · relevance 0.13

- **In one sentence**: This paper reframes existing findings on how differential privacy noise affects charts through the lens of visual channels (position, color, size and similar mark properties), and proposes a channel-read-mechanism hypothesis for when privacy-protected visualizations stay useful.
- **In plain words**: Differential privacy adds carefully calibrated random noise to data so that individuals cannot be picked out, but the noise can make charts harder to read. The authors argue that earlier studies of this effect were tied to specific chart types, so they look at the problem through 'visual channels', the properties such as position, length or color that encode data values. They synthesize prior work, rather than running new experiments, to suggest that a chart's usefulness under noise depends on both which channels carry the data and which privacy mechanism is used.
- **Why it matters**: It offers a common vocabulary for comparing privacy-preserving charts across chart types and points to gaps in how these tools are evaluated, which matters for anyone designing or judging privacy-protected dashboards. Because the paper is a synthesis from the abstract alone, the strength of its hypothesis rests on how well the cited prior studies support it, which I cannot check here.
- **Background needed**: ["Differential privacy (DP): a mathematical guarantee that results reveal little about any single person's record, achieved by adding random noise to data or outputs.", 'Visual channels: the visual properties of marks (position, length, color, size, shape) that encode data values in a chart.', 'Perceptual effectiveness: how accurately and quickly people read values from different channels; some channels are easier to read than others without noise.', 'Utility: how useful a visualization remains for its intended task after privacy noise is added.', 'Task-relevant reads: the specific judgments a viewer needs to make from a chart, such as comparing values or spotting a trend.'] · level: intermediate

<details><summary>Original abstract</summary>

Differential privacy (DP) is increasingly adopted to protect sensitive data in visualization, but understanding how privacy-induced noise affects visual representations remains fragmented. Prior work has examined the impact of DP noise on specific chart types, yet these findings are typically tied to particular chart types and evaluation settings, making it difficult to generalize across contexts. In parallel, visualization research has long established that visual channels, the visual properties of marks that encode data attributes, differ in perceptual effectiveness under noise-free conditions. However, these principles have not been systematically revisited under DP, where noise is deliberately introduced into the data to protect privacy. In this paper, we present a channel-centric perspective to reframe prior empirical and theoretical results. Our synthesis drawson prior findings to motivate a channel-read-mechanism hypothesis: the utility of DP visualizations may depend on the task-relevant reads made salient by visual channel configurations and DP mechanism choice jointly. Moreover, this perspective highlights the role of channel choice throughout the privacy-preserving visualization pipeline, from disclosure framing and DP algorithm design to utility evaluation and interpretation of noisy outputs. The synthesis also identifies gaps in the existing evaluation literature and highlights research opportunities for channel-aware DP visualization.

</details>

### [VideoTrail: Interactive Video Foraging Through Hierarchical Visualization](https://arxiv.org/abs/2611.25377v1)
*Catherine Yeh, Bryan Wang, Fernanda Viégas et al.* · `cs.HC` · arXiv:2611.25377v1 · relevance 0.09

- **In one sentence**: VideoTrail is a browser extension that replaces a plain video timeline with an AI-generated hierarchical map of segments, using semantic and structural cues as information scent to support goal-directed video navigation, evaluated in a 16-person user study.
- **In plain words**: People often have to watch long videos or scrub back and forth along a progress bar to find one specific moment, which is slow and hit-or-miss. VideoTrail is a browser add-on that uses AI to break a video into a nested outline of sections, with cues such as topics and on-screen text, so viewers can head toward the part they want. The authors report that in a study with 16 participants, it helped people find key moments more efficiently than a traditional timeline and allowed new ways of navigating, though the abstract gives no detailed figures.
- **Why it matters**: It applies a well-known idea from information foraging theory, where people follow scent cues toward likely targets, to the everyday problem of searching video, which may matter for education, lecture review and tutorial use. The abstract is thin on measured results, so how large or robust the benefit is remains unclear from this summary alone.
- **Background needed**: ["Scrubbing: dragging the playhead along a video's progress bar to skip ahead or review.", "Information foraging theory: a model from HCI saying people navigate information by following cues ('scent') that suggest where useful content lies.", 'Hierarchical visualization: showing information as nested levels, such as chapters containing sections, rather than one flat list.', 'Semantic cues: meaning-based signals such as topics or transcript text; structural cues: layout signals such as scene or section boundaries.', 'Multimodal: using more than one type of input, here visual frames and text.', 'Browser extension: a small add-on that adds features to a web browser without changing the video site itself.'] · level: intermediate

<details><summary>Original abstract</summary>

People often watch videos to find information, but locating relevant moments can be difficult and time-consuming. Existing strategies like scrubbing rely primarily on visual scanning and linear search, providing limited support for goal-directed navigation. We present VideoTrail, an AI-powered browser extension that supports information seeking in videos through a hierarchical visualization. Inspired by information foraging theory, VideoTrail surfaces semantic and structural cues as information scent, creating an explorable roadmap of segments. The system is multimodal and adaptive, prioritizing visual or textual scent based on the video's content. In a user study (N=16), VideoTrail helped participants efficiently locate key moments and enabled new navigation strategies compared to traditional timelines, highlighting how exposing an adaptive video structure can enhance goal-directed viewing.

</details>

## Information theory

### [Optimal Impure $(r,δ)$-Quantum Locally Recoverable Codes with Explicit Minimum Localities](https://arxiv.org/abs/2611.25859v1)
*Yang Li, Shitao Li, Gaojun Luo et al.* · `cs.IT` · arXiv:2611.25859v1 · relevance 0.11

- **In one sentence**: Quantum locally recoverable codes with $(r,δ)$-locality ($(r,δ)$-qLRCs) are quantum error-correcting codes in which $δ-1$ erased qudits can be recovered by accessing only $r$ other qudits. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Quantum locally recoverable codes with $(r,δ)$-locality ($(r,δ)$-qLRCs) are quantum error-correcting codes in which $δ-1$ erased qudits can be recovered by accessing only $r$ other qudits. The minimum locality of a qLRC is the least $r$ such that it has $(r,δ)$-locality. This paper aims to construct optimal impure $(r,δ)$-qLRCs with disjoint recovering sets and explicit minimum localities, where the optimality is measured by the Singleton-like bound of Guruswami, Kshirsagar, and Trivedi (GKT-optimal). Such qLRCs have particular advantages in recovering as many quantum erasures as possible while operating in parallel and with minimal qudit access overhead. We first characterize the recovering sets and the minimum locality of any CSS code by local relative distances, which are relative minimum distances of punctured codes with respect to shortened codes. We then construct impure qLRCs as CSS codes from nested pairs of generalized monomial-Cartesian codes. Grouping the monomials by their degree in the last variable, we reduce both their minimum distances and their local recovery to nested pairs of codes in the remaining variables, and the coordinates with the same values of these variables form disjoint recovering sets. In this way, we obtain four infinite families of GKT-optimal impure $(r,δ)$-qLRCs with disjoint recovering sets, and determine their minimum localities and the recovering sets attaining them for every admissible $δ$, except for a partial range of $δ$ in one family. These minimum localities need not be monotone in $δ$. In particular, two of the families contain GKT-optimal impure subfamilies of CSS codes CSS$(\mathcal{C},\mathcal{C})$ with $(r,δ)$-locality for some $r<n-δ+1$ at values of $δ$ for which $\mathcal{C}$ has no classical $(r',δ)$-locality for any $0<r'<n$, where $n$ is the length of $\mathcal{C}$.

</details>

### [Convex splitting by binary quantum hypothesis testing](https://arxiv.org/abs/2611.25496v1)
*Mark M. Wilde* · `quant-ph` · arXiv:2611.25496v1 · relevance 0.07

- **In one sentence**: How many independent quantum systems does it take to hide one system that is correlated with a reference? (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

How many independent quantum systems does it take to hide one system that is correlated with a reference? An observer can measure all the systems together with the reference to detect the correlation. We turn any such measurement into binary tests on a single system and the reference. For each test we bound the probability of declaring a signal when an independent pair was prepared. Averaging the largest signal acceptance probabilities allowed by these bounds controls the normalized trace distance in the convex-split lemma. A second bound gives a sufficient number of systems by minimizing the hypothesis-testing relative entropy over the state of the reference. Both bounds hold for density operators on separable Hilbert spaces. Comparing two distributions for the location of the hidden system gives one-shot bounds for private communication and one-way secret key distillation, including the public information available to an eavesdropper. For a fixed finite-alphabet model with separable quantum outputs and positive information advantage and variances, we recover the known Gaussian corrections to the attainable number of private or key bits from $n$ independent repetitions and bound the remaining loss by $\log_2 n+O(1)$ at fixed errors. The position-based key distillation protocol attains this bound with $O(n)$ public bits.

</details>

## High-energy theory and gravity

### [Bianchi cosmologies with four-dimensional groups of motion in New General Relativity](https://arxiv.org/abs/2611.26474v1)
*Manuel Hohmann, Paul Martin Kull, Margus Saal* · `gr-qc` · arXiv:2611.26474v1 · relevance 0.26

- **In one sentence**: The paper derives and partially solves the field equations of New General Relativity (a one-parameter family of teleparallel gravity theories) for spatially homogeneous Bianchi II, III and IX cosmological models that possess a four-dimensional symmetry group.
- **In plain words**: Physicists build models of how the universe expands, and the standard model uses Einstein's general relativity, where gravity is curvature of spacetime. This paper works in an alternative formulation, teleparallel gravity, where gravity is described by a different geometric quantity, and it studies a family of such theories called New General Relativity. The authors restrict to simple, highly symmetric universe shapes (Bianchi types II, III and IX) and show that the geometry and the matter content can each be described by a small set of functions of time. They then write down the equations these theories require and present some solutions, which the abstract says include cases resembling the standard expanding-universe model and cases that deviate from it.
- **Why it matters**: It tests whether alternative geometric descriptions of gravity can produce cosmologies that look like the standard one or differ from it in checkable ways, which matters for work on dark energy and modified gravity. The abstract does not indicate how the deviations compare with observations, so its relevance to real data is unclear from this summary alone.
- **Background needed**: ["General relativity: Einstein's theory in which gravity is spacetime curvature, described by the metric (the rule for measuring distances and times).", 'Teleparallel gravity: an equivalent-in-spirit reformulation that uses torsion (a twisting of the geometry) instead of curvature to describe gravity, with the metric as the main variable.', 'New General Relativity: a one-parameter family of teleparallel theories; the parameter selects a specific member of the family.', 'Bianchi models: spatially uniform but possibly anisotropic (direction-dependent) universe models, classified into types such as II, III and IX.', 'Friedmann-Lemaître-Robertson-Walker (FLRW) cosmology: the standard isotropic, homogeneous model of the expanding universe.', 'Field equations: the differential equations linking geometry to matter content; solving them gives the time evolution of the universe model.'] · level: research-level

<details><summary>Original abstract</summary>

We study the dynamics of the most general metric teleparallel spacetimes of Bianchi types II, III and IX, which admit a four-dimensional symmetry group, in the 1-parameter family of New General Relativity. We first show that in each of these classes the most general metric teleparallel geometry is described by four free functions of time, while another four functions of time describe the most general energy-momentum tensor compatible with the same symmetries. We then derive the field equations of New General Relativity for this class of geometries. Finally, we present some solutions to these field equations. Our results show that both solutions resembling features of the standard Friedmann-Lemaître-Robertson-Walker cosmology of General Relativity and deviations thereof exist.

</details>

### [From Integrability to Chaos in Tensionless AdS3 String Theory](https://arxiv.org/abs/2611.25576v1)
*Matthias R. Gaberdiel, Beat Nairz, Cheng Peng* · `hep-th` · arXiv:2611.25576v1 · relevance 0.22

- **In one sentence**: We study quantum-gravitational corrections to the planar integrable structure of the symmetric product orbifold $\text{Sym}^N(\mathbb{T}^4)$ that is dual to tensionless string theory on AdS$_3\times$S$^3\times \mathbb{T}^4$. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We study quantum-gravitational corrections to the planar integrable structure of the symmetric product orbifold $\text{Sym}^N(\mathbb{T}^4)$ that is dual to tensionless string theory on AdS$_3\times$S$^3\times \mathbb{T}^4$. We consider the deformation that switches on R-R flux in the bulk, and analyze the associated level spacing statistics. The leading non-planar corrections lift the planar degeneracies and produce signs of random-matrix behavior. Our results provide a controlled example of string interactions driving the onset of quantum chaos.

</details>

## Statistical physics

### [Nonequilibrium Statistical Mechanics: Physical Concepts & Mathematical Tools](https://arxiv.org/abs/2611.26394v1)
*Sagar Chakraborty* · `cond-mat.stat-mech` · arXiv:2611.26394v1 · relevance 0.30

- **In one sentence**: These are introductory lecture notes that present core concepts and mathematical techniques of classical nonequilibrium statistical mechanics, assuming prior knowledge of equilibrium statistical mechanics.
- **In plain words**: Statistical mechanics explains how the behavior of huge collections of particles relates to averages and probabilities, and most of its textbook tools assume the system has settled into equilibrium. These lecture notes gather the basic ideas and mathematical methods for the harder case of systems that are not settled, such as systems driven by flows of energy or matter. The author says the material is a synthesis and presentation of existing ideas, not new results, and notes that the same tools are used in biology, ecology, economics and sociology. The abstract does not state specific findings.
- **Why it matters**: It is a teaching resource for readers who want an entry point into nonequilibrium methods used across complex-systems fields; the abstract itself makes no claims of new results, so its value lies in pedagogy rather than discovery. I cannot tell from the abstract which specific cross-field applications the notes cover.
- **Background needed**: ['Equilibrium statistical mechanics: how microscopic states give rise to macroscopic quantities like temperature and pressure', 'Basic probability and averages over ensembles of states', 'The general idea of a system being driven away from equilibrium, for example by a temperature or energy gradient', 'Basic calculus and differential equations'] · level: intermediate

<details><summary>Original abstract</summary>

As anything not in equilibrium is, by definition, nonequilibrium, there is no universally agreed-upon set of topics that can constitute an exhaustive presentation of nonequilibrium statistical mechanics. At the same time, nonequilibrium statistical mechanics has transcended traditional physics to become a powerful language for complex systems. Prompted by an enthusiastic curiosity about complex systems, these cursory lecture notes attempt to elucidate some introductory concepts and techniques used in classical nonequilibrium statistical mechanics, which find successful applications not only in foundational physics, but also across other fields such as biology, ecology, economics, and sociology. Except for the specific synthesis and presentation of the material, which assumes basic familiarity with equilibrium statistical mechanics, the author claims no originality.

</details>

### [Attention Head Specialization: Phase Transitions in Sample Complexity](https://arxiv.org/abs/2611.26228v1)
*Léo Catteau, O. Duranthon, Lenka Zdeborová* · `cs.LG` · arXiv:2611.26228v1 · relevance 0.18

- **In one sentence**: Attention heads specialize into distinct functions during training, often emerging in stages together with sharp changes in model behavior. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Attention heads specialize into distinct functions during training, often emerging in stages together with sharp changes in model behavior. While this phenomenon has mostly been studied as a function of training time, we ask how head specialization depends on the amount of available training data. Empirically, we find that heads specialized to syntactic relations in BERT emerge as the dataset size increases. We then study this phenomenon in a solvable high-dimensional model of multi-head attention and establish that, in this model, head specialization is a genuine phase transition in sample complexity, corresponding to a non-analyticity in the test error and other observables. Depending on data structure and regularization, specialization can follow uninformative head differentiation or occur through a cascade of phase transitions that progressively recover weaker latent features, providing a statistical form of simplicity bias. Finally, we relate these statistical transitions to the stagewise emergence of specialized heads during online learning, disentangling statistical from dynamical origins of head specialization.

</details>

## Condensed matter

### [Scalable Simulation of Strongly Correlated Fermions with Neural Gaussian Tensor Networks](https://arxiv.org/abs/2611.26604v1)
*Runze Chi, Ao Chen, Garnet Kin-Lic Chan* · `cond-mat.str-el` · arXiv:2611.26604v1 · relevance 0.24

- **In one sentence**: Accurate simulations of strongly correlated electrons remain a central challenge in computational physics. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Accurate simulations of strongly correlated electrons remain a central challenge in computational physics. We introduce neural-network Gaussian projected entangled-pair states (NN-GPEPS), which exploit the locally-entangled subspace of Gaussian states to give an architecture more compatible with modern neural networks and an exact contraction cost of $O(N^{3/2})$ on two-dimensional lattices. For the Hubbard model at $U/t=8$ and $1/8$ hole doping, we obtain state-of-the-art variational energies in large lattices of up to 1024 sites. These results demonstrate an accurate approach to strongly correlated fermions by connecting neural networks with Gaussian tensor networks.

</details>

### [Topology-Enabled Self-Verification of Quantum Hall Resistance Standards](https://arxiv.org/abs/2611.26016v1)
*DaVonne Henry, Dominick S. Scaletta, Tamar M. Padwa et al.* · `cond-mat.mes-hall` · arXiv:2611.26016v1 · relevance 0.14

- **In one sentence**: The scaling of multi-element quantized Hall array resistance standards necessitates rigorous validation that internal quantization has not broken down without relying on the verification of dissipationless edge state transport. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The scaling of multi-element quantized Hall array resistance standards necessitates rigorous validation that internal quantization has not broken down without relying on the verification of dissipationless edge state transport. One proposed solution is to use a Symmetric Precision Quantization Reliability criterion, a mathematical framework that statistically assures such validation strictly through outer terminal measurements of Cn-symmetric designs. This criterion essentially bounds the likelihood of hidden localized defects arising from quantum Hall breakdown and has potential uses in quantum computing and semiconductor testing but is presented in the context of its application toward quantum electrical standards.

</details>

## Particle physics

### [Dark Matter Model Implications of a Candidate Sub-halo Near the Sun, and the Data Needed to Discriminate Among Them](https://arxiv.org/abs/2611.25359v1)
*Stefano Profumo, Sukanya Chakrabarti* · `astro-ph.GA` · arXiv:2611.25359v1 · relevance 0.19

- **In one sentence**: Pulsar-timing accelerations point to a localized mass concentration near the Sun, consistent with a dark matter sub-halo. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Pulsar-timing accelerations point to a localized mass concentration near the Sun, consistent with a dark matter sub-halo. We work out what such an object implies for the nature of dark matter, organizing the implications by their observable effect: suppression or enhancement of structure formation, internal structure and survival after formation, and emission or scattering by the constituents. We discuss ultralight wave dark matter, thermal and nonthermal warm dark matter, dark acoustic oscillations and dark matter-baryon scattering, elastic and inelastic self-interactions, invisible decays with recoil, primordial black holes, indirect detection, and a possible connection to the LUX-ZEPLIN high-energy recoil candidate. We then ask what new data would discriminate among these models. The existing accelerations are measured outside the tidal radius, where they are blind to the interior mass distribution, to the object's velocity, and to the sub-halo population. We identify four routes that lift these degeneracies: accelerations measured inside the halo, which separate point-mass, cuspy, and cored profiles; lensing and accretion, which test whether the mass is compact; the morphology of annihilation or decay emission, which probes the inner profile; and a search for a comoving stellar population, which tests whether the object is dark and measures its velocity. We also contrast this program with pulsar-timing-array searches for transiting dark matter substructure, which probe vastly lighter objects through a different observable.

</details>

### [Direct simulation Monte Carlo for dark matter production and phase-space evolution](https://arxiv.org/abs/2611.25812v1)
*Felix Kahlhoefer, Ann Cathrin Wesener* · `hep-ph` · arXiv:2611.25812v1 · relevance 0.18

- **In one sentence**: The paper introduces a Direct Simulation Monte Carlo approach that tracks an ensemble of stochastically interacting particles to solve phase-space Boltzmann equations for dark matter production, including freeze-out, decays, elastic scattering and number-changing processes, without a fixed momentum grid or thermally averaged cross sections.
- **In plain words**: Dark matter particles were produced in the early universe, and predicting how many remain requires tracking how their energies and momenta spread out as they interact. Standard methods use equations that are hard to solve when the particles are far from thermal equilibrium. The authors instead simulate a large collection of individual particles that collide and transform randomly, and they test this on a scenario where dark matter is made in two steps, producing a two-peaked energy distribution. The abstract presents this as a flexible, validated method; it does not report specific numerical results in the summary provided.
- **Why it matters**: Dark matter abundance and its effect on structure formation depend on details of the particle energy distribution that simplified calculations may miss, so a more general solver could matter for cosmology. The abstract does not show how large the practical gain is over existing codes, so its significance is best judged from the full paper.
- **Background needed**: ['Dark matter: hypothetical, weakly interacting matter that makes up most of the mass of galaxies and is inferred from gravity.', 'Freeze-out: the point in cosmic history when particles stop interacting often enough to stay in equilibrium with the hot plasma, fixing their remaining abundance.', 'Boltzmann equation: a kinetic equation describing how the number of particles at each momentum changes over time due to collisions and decays.', 'Phase-space distribution: a description of how many particles occupy each combination of position and momentum.', 'Monte Carlo simulation: a method that uses random sampling of individual particles and random event choices to estimate how a system evolves.', 'Thermal averaging: a common simplification that replaces energy-dependent interaction rates with one averaged value, which the paper avoids.'] · level: research-level

<details><summary>Original abstract</summary>

To study the early-universe production of dark matter particles beyond thermal equilibrium often requires solving several coupled Boltzmann equations at the phase-space level. We present a new method to address this challenge using Direct Simulation Monte Carlo (DSMC) based on stochastic interactions of an ensemble of particles. We implement and validate efficient algorithms to describe freeze-out, decays, elastic scattering and number-changing processes within the dark sector. These algorithms do not require a discretisation of momentum space on a pre-defined grid and do not rely on approximations such as thermally averaged cross sections. As illustrative example, we consider a scenario with two-step dark matter production, leading to a bimodal phase-space distribution, and consider the subsequent evolution under elastic and number-changing processes. We show that DSMC is a flexible approach to explore out-of-equilibrium processes and solve Boltzmann equations at the phase-space level in order to predict the abundance of dark matter particles and their effect on structure formation.

</details>

## Nuclear physics

### [Nucleon Short-Range Correlations and Supersoft Nuclear Symmetry Energy: Compatibility with Massive Neutron Stars and GW170817](https://arxiv.org/abs/2611.25913v1)
*Hai-Xiang Zhu, Bao-Jun Cai, Yu-Gang Ma* · `nucl-th` · arXiv:2611.25913v1 · relevance 0.09

- **In one sentence**: Massive neutron stars (NSs) require a sufficiently stiff core equation of state (EOS), while the relatively small tidal deformability inferred from GW170817 favors softer nuclear matter at intermediate densities. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Massive neutron stars (NSs) require a sufficiently stiff core equation of state (EOS), while the relatively small tidal deformability inferred from GW170817 favors softer nuclear matter at intermediate densities. Given the importance of the nuclear symmetry energy in neutron-rich matter, an intriguing question arises: Can the symmetry energy become supersoft at high densities while remaining compatible with these seemingly competing constraints? Within the nonlinear Walecka framework, we demonstrate that nucleon short-range correlations (SRCs), manifested as a high-momentum tail (HMT) in the nucleon momentum distribution, can accommodate such behavior without introducing additional interaction parameters. We derive for the first time analytical expressions for the symmetry energy curvature $K_{\rm{sym}}$ for both free Fermi gas (FFG) and HMT momentum distributions. Using model parameter sets that reproduce empirical nuclear matter properties around saturation density, we find that SRC-HMT yields substantially more negative $K_{\rm{sym}}$ than the FFG case, allowing the symmetry energy to reach a maximum at low supra-saturation densities and subsequently decrease while the total pressure remains sufficient to support massive NSs. The resulting EOSs also predict smaller NS radii and tidal deformabilities consistent with GW170817. These results connect the microscopic nucleon momentum distribution with the density dependence of the symmetry energy and macroscopic NS properties.

</details>

### [u3lib: An AI-Ready Computational Framework for U(3) Symmetry Algebra, Wigner Coupling, and Racah Recoupling Coefficients](https://arxiv.org/abs/2611.26558v1)
*Daniel Langr, Phong Dang, Tomas Dytrych et al.* · `nucl-th` · arXiv:2611.26558v1 · relevance 0.08

- **In one sentence**: u3lib is a C++ library for U(3)/SU(3) representation-theory calculations in nuclear structure and related applications. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

u3lib is a C++ library for U(3)/SU(3) representation-theory calculations in nuclear structure and related applications. It evaluates Wigner coupling and Racah recoupling coefficients using the procedure proposed in 2024 by Dang et al., which avoids the binomial coefficients and alternating sums used in earlier formulations. The library also provides irreducible representations (irreps), dimensions, Casimir invariants, conjugation, and tensor-product decompositions with outer multiplicities. It supports the canonical Gelfand-Tsetlin basis and the physical SU(3) $\supset$ SO(3) basis, including inner multiplicities and the transformation between the two bases. Generator routines return matrix elements in the canonical basis and reduced matrix elements in the physical basis. Python bindings mirror the C++ API. Domain skills supplied with the repository allow an AI assistant with code-execution access to call these routines from natural-language requests.

</details>

## Quantum information and computing

### [When the Noise Gets Noisy: Quantum Error Correction with Disordered Noise and Misinformed Decoding](https://arxiv.org/abs/2611.26506v1)
*Cory T. Aitchison, Lucas H. English, Benjamin Béri et al.* · `quant-ph` · arXiv:2611.26506v1 · relevance 0.21

- **In one sentence**: Experimental demonstrations of quantum error correction often exhibit noise that varies across space and time, and attempting to characterize this disorder has been shown to substantially improve decoding performance. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Experimental demonstrations of quantum error correction often exhibit noise that varies across space and time, and attempting to characterize this disorder has been shown to substantially improve decoding performance. However, theoretical studies of quantum error correction typically assume fixed, perfectly known, homogeneous noise. Here we model decoding with incomplete or inaccurate knowledge of disordered noise channels by treating physical error rates as random variables. We show that the decoding performance is set by a small number of information-theoretic functionals of the noise distribution: the entropy determines the threshold while Bhattacharyya coefficients bound the deep sub-threshold decay rate of logical failures. Furthermore, our results give a quantitative measure of the benefits of characterizing this noise. We numerically investigate both maximum-likelihood and minimum-weight-error decoding of surface codes, showing good agreement with theory across the code-capacity, phenomenological, and circuit-level noise settings, including with noise distributions seen in open-access superconducting devices. When it comes to error correction in realistic settings, reporting the average entropy and Bhattacharyya coefficient of noise distributions could therefore be more informative than the mean or median error rates of a device's components.

</details>

### [Algorithmic Quantum Sensing](https://arxiv.org/abs/2611.25572v1)
*Ishaan Kannan, Aditi Venkatesh, Jordan Cotler* · `quant-ph` · arXiv:2611.25572v1 · relevance 0.18

- **In one sentence**: We introduce a unified framework for sensing time-dependent fields through the lens of classical and quantum algorithms. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We introduce a unified framework for sensing time-dependent fields through the lens of classical and quantum algorithms. First, we develop three pulse sequence protocols, namely randomized, matched, and pooled spectroscopy, which outperform established approaches such as dynamical decoupling across a wide range of tasks. These protocols attain the optimal sensitivity for linear and nonlinear AC sensing on conventional spin or qubit platforms, improving existing devices by changing only their pulse sequences. We then introduce quantum computational spectroscopy (QCS), which couples quantum sensors to a quantum processor. QCS combines two new primitives: a quantum computational frequency comb that coherently converts any classical signal into a quantum oracle, and a family of quantum algorithms that use the oracle to extract signal information in superposition. Variations can be implemented on current platforms with only one memory ancilla. We show that the ultimate limit imposed by quantum mechanics lies polynomially beyond the Heisenberg limit, and that QCS achieves it. Attaining this new limit requires quantum computation, establishing a fundamental separation between conventional and quantum computational sensing. Moreover, QCS retains beyond-Heisenberg scaling for broadband signals under constant-strength sensor depolarization, while we prove that the same noise limits any protocol lacking quantum computation to standard-quantum-limit scaling. Our result provides the first asymptotic, beyond-quadratic quantum advantage in AC metrology when noise is aligned with the signal, proving that Lindblad span conditions do not apply to broadband quantum sensing. Our work builds an algorithmic theory for designing sensing protocols and establishes quantum sensing as a new frontier for quantum algorithms, with quantum advantages that surpass the Heisenberg limit and that persist under noise.

</details>

## Optics and atomic physics

### [Fast electrons and high energy photons produced in strong-field ionization of atoms as diagnostics of multi-petawatt laser beams](https://arxiv.org/abs/2611.26496v1)
*A. V. Khudov, N. V. Makarenko, A. A. Mironov et al.* · `physics.atom-ph` · arXiv:2611.26496v1 · relevance 0.16

- **In one sentence**: The authors numerically compute energy spectra and angular distributions of photoelectrons and X-ray photons from tunnel ionization of argon in focused multi-petawatt laser fields, and argue these observables track peak intensity and focal-spot field configuration as a diagnostic.
- **In plain words**: Very powerful lasers now produce light intensities so high that they tear electrons off atoms, and it is hard to measure exactly how intense the focused beam really is. This paper uses computer simulations of argon atoms hit by such beams to predict what the ejected electrons and emitted X-rays look like. The authors report that these electron and X-ray patterns change with the laser power, how tightly the beam is focused, and its polarization, which suggests they could be used to check the beam's properties.
- **Why it matters**: Knowing the true intensity inside the focal spot is needed to interpret experiments with the newest multi-petawatt lasers, so a reliable in-situ diagnostic would be useful. The abstract supports only a proposal with numerical predictions; whether it works in practice depends on experimental tests that the abstract does not describe.
- **Background needed**: ["Tunnel ionization: in a very strong laser field, the electric field bends the atom's binding barrier enough that an electron can leak out of the atom.", 'Petawatt: a power of 10^15 watts, delivered in very short pulses; focusing concentrates it to extreme intensities.', 'Photoelectrons: electrons ejected from atoms by light; their energy and direction carry information about the field.', 'High-energy photons: X-rays emitted during the strong-field process, which also depend on the field.', 'Focal spot and polarization: the intensity varies across the focused beam, and the direction the electric field oscillates (polarization) changes the outcome.', "Diagnostic: a measurement used to infer a hidden physical quantity, here the laser's peak intensity and field shape."] · level: research-level

<details><summary>Original abstract</summary>

We calculate numerically energy spectra and angular distributions of photoelectrons and X-ray photons emitted in the process of tunnel photoionization of argon by a focused laser beam of multi-petawatt power. By scanning the beam power and varying the degree of focusing and the field polarization, we show these distributions to be sensitive both to the peak laser intensity and to the field configuration in the focal spot. Investigated parameters of the laser beam correspond to those of several recently commissioned lasers of multi-petawatt power. These findings, in line with the earlier reported proposals, provide a basis for the development of a reliable ionization diagnostics of extremely intense laser fields.

</details>

### [Dephasing-free plasma acceleration with millijoule picosecond lasers](https://arxiv.org/abs/2611.26032v1)
*Alexander Pukhov* · `physics.plasm-ph` · arXiv:2611.26032v1 · relevance 0.13

- **In one sentence**: Laser-plasma accelerators reach gradients a thousand times above radio-frequency cavities, but need joule-class femtosecond lasers firing about once per second, and electrons outrun the wave. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Laser-plasma accelerators reach gradients a thousand times above radio-frequency cavities, but need joule-class femtosecond lasers firing about once per second, and electrons outrun the wave. A comb of laser lines spaced by the plasma frequency, each in its own mode of a matched channel, drives a wake moving at the speed of light. In particle-in-cell simulations a 175\,mJ, 0.5\,ps drive holds 21\,GV/m over 10\,mm with a 0.15\,rad phase drift; a test electron gains 208\,MeV, 2.6 times more than in one mode. Because the wave builds up resonantly, the required energy falls steeply with density: a 29\,mJ drive sustains 20\,GV/m, and a 10\,mJ drive, within reach of kilohertz industrial lasers, gives a test electron 170\,MeV over 30\,mm. A simulated stage transfers 5\,\% of the laser energy to the wake; the Manley--Rowe limit is about 18\,\% for five lines.

</details>

## Fluids and plasma

### [Scattering by Small Ice Crystals in Turbulence: From Orientation Statistics to Retrieval Biases](https://arxiv.org/abs/2611.25750v1)
*Himanshu Mishra, Mohd. Meraj Khan, T. Narayana Rao et al.* · `physics.flu-dyn` · arXiv:2611.25750v1 · relevance 0.08

- **In one sentence**: Ice-cloud retrievals from polarimetric radar, lidar and submillimeter radiometry commonly assume random orientation, horizontal alignment or a prescribed flutter angle. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Ice-cloud retrievals from polarimetric radar, lidar and submillimeter radiometry commonly assume random orientation, horizontal alignment or a prescribed flutter angle. We link the orientation dynamics of ice crystals to their scattering. Fluid-inertial torque turns small settling crystals broadside on, and turbulent velocity gradients turn them away, so their orientation depends on the dissipation rate. We combine a closed-form orientation distribution for overdamped spheroids, including rotational diffusion and turbulence intermittency, with orientation-averaged Rayleigh, Rayleigh--Gans, T-matrix and specular scattering. Turbulence enters the scattering only through the Legendre moments of the orientation distribution. In the Rayleigh regime the specific differential phase follows crystal alignment, so assuming perfectly horizontal crystals biases ice-water-content retrievals low. Combining the specific differential phase with differential reflectivity limits this bias to $25\%$ for a single size of the shapes studied. For size distributions that span the alignment transition the bound can fail, because the two observables weight sizes differently. Depolarization adds sensitivity to higher-order moments and to intermittency. At finite size the second orientation moment mainly controls the scattering cross sections and the asymmetry parameter, and for optically soft crystals its contribution vanishes $54.7^\circ$ from the vertical. Specular returns from partly aligned plates should persist for lidars pointed $3^\circ$ from nadir. An exploratory analysis of EarthCARE lidar data finds a weakly depolarizing, low-lidar-ratio signature most frequent near $-11^\circ$C, where plates grow. Degree-scale tilt widths inferred from glints and lidar require larger crystals, near or beyond the validity range of the model.

</details>

### [Energy transfers in decaying three-dimensional Hall-magnetohydrodynamics turbulence: Dependence on the Ion-Inertial Length and the Magnetic Prandtl Number](https://arxiv.org/abs/2611.25686v1)
*Pratik Patel, Sharad K. Yadav, Akanksha Gupta et al.* · `physics.plasm-ph` · arXiv:2611.25686v1 · relevance 0.08

- **In one sentence**: The paper uses pseudospectral direct numerical simulations of decaying 3D Hall-MHD turbulence, with shell-to-shell energy-transfer analysis, to show how kinetic and magnetic energy exchange depends on the ion-inertial length and the magnetic Prandtl number, and how the Hall term drives inverse and forward magnetic energy transfer.
- **In plain words**: Turbulence is the chaotic swirling seen in stirred liquids and in plasmas such as the solar wind, and it moves energy from big motions to small ones. This paper studies a version of turbulence in electrically conducting plasma where the 'Hall effect' (a term that matters when ions and electrons decouple at small scales) is included. Using large computer simulations, the authors track how energy flows between moving-fluid energy and magnetic energy, and how this depends on two plasma parameters.
- **Why it matters**: Energy transfer across scales is central to how plasmas heat and organize themselves, including in space and astrophysical settings, so knowing which way energy flows and whether it is local or non-local is useful. The abstract does not compare these results with observations, so any link to specific space or lab plasmas is something the authors would need to establish.
- **Background needed**: ['Magnetohydrodynamics (MHD): a fluid model treating a conducting fluid or plasma as coupled to magnetic fields.', 'Hall term: an extra term in plasma models that becomes important at scales near the ion-inertial length, where ions and electrons no longer move together.', 'Ion-inertial length d_i: the characteristic scale below which the Hall effect matters.', 'Magnetic Prandtl number Pr_m: the ratio of fluid viscosity to magnetic diffusivity, controlling how the velocity and magnetic fields dissipate relative to each other.', 'Energy cascade: energy moving from large to small length scales (forward) or the reverse (inverse), in turbulence.', 'Shell-to-shell energy transfer: a method of splitting the wavenumber spectrum into shells and measuring how much energy moves between them.', 'Pseudospectral direct numerical simulation (DNS): solving the governing equations directly on a grid with spectral accuracy, without a turbulence model.'] · level: research-level

<details><summary>Original abstract</summary>

We present a systematic study of energy transfers in three-dimensional (3D) decaying Hall-magnetohydrodynamics (HMHD) turbulence. Our study has been designed to investigate the dependence of these transfers on initial energy spectra, the ion-inertial length $d_{i}$, and the magnetic Prandtl number $Pr_{m}$. Using shell-to-shell decomposition, we compute the energy transfer rates for (a) kinetic-to-kinetic, (b) magnetic-to-magnetic, (c) kinetic-to-magnetic, and (d) magnetic-to-kinetic interactions by carrying out extensive pseudospectral direct numerical simulations (DNSs) of 3D HMHD and its MHD counterpart. Furthermore, we examine the magnetic-to-magnetic and current-density-to-magnetic energy transfers arising from the Hall term in this framework. Energy transfers between like fields -- namely, kinetic-to-kinetic and magnetic-to-magnetic -- are predominantly local and forward in direction, cascading energy from large to small length scales. This behavior is consistent with a self-similar flow structure in the inertial range. Cross-field transfers, between kinetic and magnetic energy, are found to be forward but non-local in character. At low and high $Pr_{m}$, the transfers become local, and the nonlinear energy transfer is significantly suppressed. Moreover, we observe that the Hall term drives both inverse and forward transfers of magnetic energy, associated with local and non-local transfer, respectively.

</details>

## Biological physics

### [Multi-Illumination Spectral Reflectance Reconstruction: A method for hyperspectral imaging using digital photography](https://arxiv.org/abs/2611.25520v1)
*Robert Heyck, Vincent Gillaspy, Stephen J. Hagen et al.* · `physics.bio-ph` · arXiv:2611.25520v1 · relevance 0.03

- **In one sentence**: The authors reconstruct spatially resolved spectral reflectance of samples from several ordinary photographs taken under known different illuminants, using an optimization that fits pixel values while penalizing rough reflectance spectra.
- **In plain words**: Color patterns on animals and objects carry information, but a normal camera records only three broad color channels, while a spectrometer measures full spectra at only one spot at a time. The authors photograph the same sample under several known light sources and computationally combine the images into a map of how much light each point reflects at each wavelength. The abstract reports high accuracy and that the method can predict how different visual systems would see the sample, though it gives no specific figures in the summary provided.
- **Why it matters**: Objective measurement of color patterns matters for studies of animal signaling, camouflage, and imaging applications, and a cheap camera-based route to full spectral maps could make such work easier. The abstract does not give quantitative accuracy results or comparisons, so the strength of the claim can't be judged from it alone.
- **Background needed**: ['Spectral reflectance: the fraction of light a surface reflects at each wavelength, which defines its color independent of who is looking.', 'Hyperspectral imaging: capturing a full spectrum at every pixel of an image, rather than a few color channels.', 'RGB cameras: standard cameras record only three broad bands (red, green, blue), which loses much spectral detail.', 'Illuminant spectral irradiance: the known distribution of light power across wavelengths emitted by each light source; knowing it is needed to convert camera readings back to reflectance.', 'Regularization: adding a penalty, here for non-smooth spectra, so that an underdetermined inverse problem has a sensible solution.', 'Visual systems: different animals have different photoreceptors, so the same reflectance can look different to them; the method is meant to model this.'] · level: intermediate

<details><summary>Original abstract</summary>

Quantitative measurement of complex coloration patterns is essential for many biological studies and practical applications. Although color perception depends on the observer's visual system, an objective characterization is possible by measuring the spectral reflectance across the sample surface. Traditional methods for measuring spectral reflectance are either limited in spatial resolution, as with spectrometer probes, or limited in spectral detail, as with digital cameras. We present a method for reconstructing spatially resolved spectral reflectance of samples from multiple images taken under different illuminants with known spectral irradiance. Using an optimization scheme that minimizes pixel-value error while regularizing for the smoothness of the reflectance spectrum, our method generates high-resolution hyperspectral images. We tested our method using both existing spectral reflectance datasets and original multi-illumination images taken in a custom photo-box, demonstrating high accuracy and simple implementation of the method, as well as the ability to infer how samples are perceived by different visual systems. Our method can be a useful tool for objective quantification of complex visual patterns in color-related biological research and imaging applications.

</details>

## Climate, atmosphere and Earth

### [Multi-scale dynamics of deep convective self-aggregation. Part II: scale-by-scale budget and mesoscale self-similarity](https://arxiv.org/abs/2611.25829v1)
*Lorenzo Silvestri, Paolina Bongioannini Cerlini, Andrea Cimarelli* · `physics.ao-ph` · arXiv:2611.25829v1 · relevance 0.07

- **In one sentence**: This work investigates deep convective self-aggregation in the space of scales, extending the physical-space analysis of Part I. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

This work investigates deep convective self-aggregation in the space of scales, extending the physical-space analysis of Part I. We introduce a novel theoretical framework by examining and deriving a generalized Yaglom equation for the second-order structure function $\langle δh_f^{\prime 2} \rangle$, the scale-dependent variance of Frozen Moist Static Energy (FMSE). Self-aggregation is found to be sustained by an inverse energy cascade driven by boundary-layer production and mediated by mesoscale circulations with horizontal scales $r \sim$(100-250 km). The inverse cascade of energy is found to be realized through a series of shallow and mid-level mesoscale circulations which behave in a self-similar way. Accordingly, the scale-energy variance exhibits an extraordinary collapse across all atmospheric layers onto a robust self-similar power law, $\langle δh_f^{\prime 2} \rangle \sim r^{6/5}$. In contrast, horizontal velocity increments show a degree of self-similarity ($\langle δu_r^{\prime 2} \rangle \sim r^{2/5}$) that retains a residual height dependence. Interestingly, the FMSE scaling breaks down at elevations lower than 750 m and at small local scales below 100 km, allowing us to identify the boundary layer top as a scale-dependent dividing layer where the strong stratification filters the interactions between the surface and free-troposphere, so that small scale dynamics of the low and high atmospheric layers are decoupled while those at large mesoscale are coupled. The derived scaling laws are also used to quantify the moisture-convection feedback via scale-dependent correlation coefficients that show that vertical transport strengthens with scale ($ρ_{mc\perp} \sim r^{2/5}$), while horizontal convergence weakens at the exact inverse rate ($ρ_{mc\parallel} \sim r^{-2/5}$).

</details>

### [Approximate Adjoint Models for Memory and Compute-Efficient Online Learning of Hybrid Models](https://arxiv.org/abs/2611.26095v1)
*Emilio González-Zamora, Pierre Tandeo, Laurent Debreu et al.* · `cs.LG` · arXiv:2611.26095v1 · relevance 0.05

- **In one sentence**: Differentiable programming enables online calibration of numerical models by minimizing errors accumulated along simulated trajectories. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Differentiable programming enables online calibration of numerical models by minimizing errors accumulated along simulated trajectories. This includes estimating physical parameters and training neural sub-models in hybrid configurations. Gradients are typically computed using adjoint methods, or backpropagation through time (BPTT), whose computational and memory costs grow with the length of the training window. This limits the duration and resolution of hybrid-model training, a major bottleneck for realistic geophysical applications. Approaches like truncated BPTT reduces memory use by discarding sensitivities across truncation boundaries, introducing gradient bias and neglecting long-range dependencies. We propose a class of gradient approximation methods that preserve the adjoint recurrence over the full trajectory while approximating only the pullback operators within it. Exact pullbacks are computed by automatic differentiation at sparse anchor states only. Between anchors, sensitivities propagate either through the identity (Zero-order) or through a reused, frozen pullback (Pullback Reuse). This approximation makes the parameter pullback constant within each chunk, allowing the gradient sum to factorize so that a single evaluation per chunk replaces one per time step. We evaluate both on three systems of increasing complexity, an incomplete Lorenz-63 model, a large-eddy closure for two-dimensional quasi-geostrophic turbulence, and bias correction in a multilayer quasi-geostrophic ocean model. Peak memory falls by up to an order of magnitude and runtime up to fourfold, with Pullback Reuse staying closest to the exact gradient direction. In all three cases, approximate gradients support hybrid-model training at comparable accuracy, showing that effective online learning does not require exact gradients.

</details>

## Cosmology

### [Breaking the background and linear degeneracies: Using nonlinear clustering to discriminate between dark energy models](https://arxiv.org/abs/2611.26460v1)
*Yunhao Gao, Baojiu Li, Jie Wang et al.* · `astro-ph.CO` · arXiv:2611.26460v1 · relevance 0.18

- **In one sentence**: We show that the traditional approach of parameterizing the background and linear-perturbation evolutions, through the equation-of-state parameter $w(a)$ and a time-dependent sound speed squared $\bar{c}^2_s(a)$, does not fully specify the cosmological behavior of dark energy theories. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We show that the traditional approach of parameterizing the background and linear-perturbation evolutions, through the equation-of-state parameter $w(a)$ and a time-dependent sound speed squared $\bar{c}^2_s(a)$, does not fully specify the cosmological behavior of dark energy theories. Using a new, fully nonlinear fluid framework, we perform spherical-collapse simulations of two clustering dark energy models with identical $w(a)$ and $\bar{c}^2_s(a)$, finding that their central dark-energy densities differ by up to 50\% for cluster-sized dark matter halos. We identify the departure of the local sound speed from $\bar{c}_s$ as the main driver of these differences. In contrast, all other theory-specific quantities in the fluid equations can be described by their background values to a very good approximation. The results demonstrate that nonlinear structure formation encodes critical additional information about the underlying dark energy theory, opening an avenue for discriminating between models using observables on small scales.

</details>

### [Splitting the action: A fully nonlinear fluid method for clustering dark energy](https://arxiv.org/abs/2611.26461v1)
*Yunhao Gao, Baojiu Li, Jie Wang et al.* · `astro-ph.CO` · arXiv:2611.26461v1 · relevance 0.16

- **In one sentence**: The paper introduces a fully nonlinear fluid description of clustering dark energy, obtained by splitting the dark-energy action into kinetic and potential parts, and uses spherical-collapse simulations of two k-essence models to study how dark-energy density perturbations grow during halo collapse as the sound speed and halo mass vary.
- **In plain words**: Dark energy is thought to drive the accelerating expansion of the universe, and some versions of it might also clump under gravity like matter, but these clumps are hard to simulate once they become dense. The authors propose a new way to write the equations for dark energy as a fluid, built by separating its underlying action into a motion part and an energy part, so that the equations do not rely on approximations that are only valid at large scales. They test this on simple spherical collapses of two example dark-energy models, following dark matter and dark energy together, and check how the clumping depends on the dark energy's sound speed and the halo's mass.
- **Why it matters**: Most current tools for clustering dark energy rely on approximations whose validity in the dense, nonlinear regime is unknown, so a method that avoids them could matter for testing these theories against future survey data. The abstract frames the work as a foundation for later full three-dimensional simulations using particle methods such as smoothed particle hydrodynamics, but it does not show that such extension has been done.
- **Background needed**: ['Dark energy: the unknown component driving the accelerating expansion of the universe; its equation of state describes its pressure relative to its energy density.', "Perturbations and clustering: small density variations that can grow under gravity into bound structures such as halos; 'nonlinear' means the growth has become large enough that simple linear approximations fail.", 'k-essence: a class of dark-energy models whose behaviour is governed by a scalar field with a non-standard kinetic term; the sound speed controls how quickly pressure fluctuations spread, and small sound speeds let the dark energy clump.', 'Action and fluid equations: the action is a single function from which field equations are derived; a fluid description treats the matter as a continuous medium with density, velocity and pressure rather than tracking the field directly.', 'Spherical collapse: an idealised model in which a uniform spherical overdensity collapses, used to test how structures form and how their density evolves.', 'Grid-based versus particle methods: grid solvers compute fields on fixed cells, while SPH represents the fluid by moving particles with smoothing kernels.'] · level: research-level

<details><summary>Original abstract</summary>

While the background evolution of dark energy is relatively straightforward to model, its perturbations, especially on nonlinear scales, generally require significantly more sophisticated treatment. Existing simulation methods for clustering dark energy --- a large class of interesting theories which are until now not well studied --- usually rely on grid-based solvers and perturbatively derived equations, whose validity in the nonlinear regime remains unknown. In this paper, we introduce a novel fluid method based on splitting the dark energy action into two parts: a kinetic part and a potential part. The resulting fluid equations are fully nonlinear and not reliant on simplifying approximations, making them suitable to describe the small-scale evolution of clustering dark energy theories, such as $k$-essence models with small sound speeds. We demonstrate the numerical implementation of this framework through spherical-collapse simulations of two representative $k$-essence models, evolving dark matter and dark energy simultaneously. The simulations are able to follow the development of dark-energy density perturbations throughout halo collapse, to $\mathcal{O}(\textrm{1}-10)$. By investigating their dependence on the dark-energy sound speed and dark-matter halo mass, we illustrate how dark-energy clustering responds to variations in the competing effects of pressure support and gravitational pull. These results demonstrate the applicability of this new framework to study nonlinear dark-energy clustering across a range of physical conditions, providing the foundation for its future extension to fully three-dimensional cosmological simulations through particle-based algorithms such as smooth particle hydrodynamics (SPH).

</details>

## Galaxies

### [The Cosmic Infrared Background from Population III.1 Supermassive Stars and Black Holes](https://arxiv.org/abs/2611.25355v1)
*Emir Tataroglu, Jonathan C. Tan, Rosalia D. O'Brien et al.* · `astro-ph.GA` · arXiv:2611.25355v1 · relevance 0.17

- **In one sentence**: We investigate the cosmic infrared background (CIB) that is expected to arise from the Population (Pop) III.1 supermassive black hole (SMBH) formation scenario, which involves early SMBH seeding via supermassive primordial star formation enabled by dark matter annihilation heating. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We investigate the cosmic infrared background (CIB) that is expected to arise from the Population (Pop) III.1 supermassive black hole (SMBH) formation scenario, which involves early SMBH seeding via supermassive primordial star formation enabled by dark matter annihilation heating. We model the emission from Pop III.1 supermassive stars, including their growth phase, flash ionization phase, and early black hole accretion phase, as well as accompanying emission from lower-mass Pop III.2 stars. The CIB is composed of stellar and SMBH accretion disk continuum radiation, nebular continuum emission, and Ly$α$ radiation redistributed through scattering in the neutral intergalactic medium. Based on the feedback regulated Pop III.1 model of Petkova et al. (2026), our fiducial model assumes $\sim 10^5\,M_\odot$ Pop III.1 stars forming by $z_{\rm flash}=20$ with a comoving number density of $\sim0.2\,{\rm cMpc}^{-3}$. For this model, the combined stellar contribution is less than $1\%$ of existing direct and diffuse CIB measurements. However, the contribution to the CIB from $z\sim6-20$ SMBH accretion is expected to be larger than the Pop III.1 stellar component for average Eddington ratios $λ_{\text{Edd}} \sim 0.01$. Latest CIB observations place constraints of $λ_{\text{Edd}} \lesssim 0.3$ for the fiducial Pop III.1 model during these epochs.

</details>

### [Chemical Cartography Across Time: The Age-Dependent Chemical Structure of the Milky Way with a Homogeneous Sample of 580,000 Giants from Five Surveys](https://arxiv.org/abs/2611.26550v1)
*Jeff Shen, Neige Frankel, David W. Hogg et al.* · `astro-ph.GA` · arXiv:2611.26550v1 · relevance 0.17

- **In one sentence**: Mapping the distribution of elements in the Milky Way and understanding how that distribution has changed over time can give us insight into the formation and evolution of our Galaxy. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Mapping the distribution of elements in the Milky Way and understanding how that distribution has changed over time can give us insight into the formation and evolution of our Galaxy. Here we use homogeneously estimated atmospheric parameters, elemental abundances, distances, and ages for ~580,000 giants from five major spectroscopic surveys---all simultaneously placed on a single, self-consistent scale by one model---allowing us, for the first time, to use a large sample of stars with uniform labels and ages that cumulatively span much of the disk to trace how the metallicity structure of the Milky Way depends on stellar age. Our chrono-chemical analysis shows that the radial metallicity gradient of the disk depends non-monotonically on age: it is shallow for the youngest stars, steepening to a maximum of ~-0.07 dex/kpc at intermediate ages (~5-6 Gyr), and flattening to near zero for the oldest stars. This "U-shaped" age dependence is driven largely by the low-alpha (thin-disk) population, with the high-alpha (thick-disk) sequence having weak gradients at all ages. In contrast to [Fe/H], the radial [Mg/Fe] gradient is weak (<~0.01 dex/kpc) at all ages. Together, these trends are consistent with an inside-out formation scenario in which the gradient of the star-forming gas has flattened over at least the last ~6 Gyr, while the near-zero gradient of the oldest stars reflects their formation in a well-mixed disk, efficient radial migration, or both.

</details>

## Exoplanets and planetary science

### [Dependence of Dust Growth on Magnetic field Strength in Protoplanetary Disks](https://arxiv.org/abs/2611.25602v1)
*Takashi Shimokawa, Masahiro Machida, Yoshihiro Kawasaki* · `astro-ph.EP` · arXiv:2611.25602v1 · relevance 0.16

- **In one sentence**: We performed one-dimensional calculations to investigate how the magnetorotational instability (MRI) affects dust growth in protoplanetary disks. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We performed one-dimensional calculations to investigate how the magnetorotational instability (MRI) affects dust growth in protoplanetary disks. We simultaneously solved the evolution of the dust size distribution and the vertical magnetic field. The dust size distribution is evolved taking into ac- count coagulation and fragmentation. For the magnetic field evolution, we considered both ambipolar diffusion and Ohmic dissipation. The MRI-driven turbulent viscosity was estimated self-consistently from the local magnetic field strength and non-ideal magnetohydrodynamics diffusivities. We found that MRI-driven turbulence becomes stronger for smaller initial plasma beta, and the enhanced tur- bulence promotes dust growth in MRI-active regions. However, dust growth is ultimately limited by radial drift, and the dependence of dust size on the magnetic field strength is significant only in the outer regions of the disk. In other words, over most of the disk, radial drift remains the dominant factor controlling the maximum dust size, and the magnetic field strength plays only a minor role in determining the overall dust size distribution.

</details>

### [Demographic inference in exoplanet chemistry is shaped by retrieval assumptions](https://arxiv.org/abs/2611.26548v1)
*Dwaipayan Dubey, Karan Molaverdikhani, Barbara Ercolano et al.* · `astro-ph.EP` · arXiv:2611.26548v1 · relevance 0.08

- **In one sentence**: Understanding the chemical diversity of exoplanet atmospheres is crucial for linking atmospheric composition to planetary formation history. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Understanding the chemical diversity of exoplanet atmospheres is crucial for linking atmospheric composition to planetary formation history. Atmospheric C/O can provide clues about where and how planets form, particularly through the accretion of gas and solids across disk snowlines. Since planetary migration can change orbital distances and hence equilibrium temperatures ($T_{eq}$), investigating C/O across different planetary populations may provide insights into their formation and evolution. As observational precision improves with the JWST, the limits of standard atmospheric retrieval methods that assume altitude-independent molecular abundances have become apparent. We present atmospheric retrievals for 20 transiting planets with published JWST transmission spectra, including complementary HST spectra for targets where such data are available, spanning gas giants, warm Neptunes, and temperate/warm sub-Neptunes, to test how population-level chemical inferences depend on retrieval assumptions. Free-chemistry retrievals show a visually non-monotonic C/O-$T_{eq}$ distribution, but this apparent pattern is not statistically robust and is sensitive to sample composition. When molecular abundances are constrained by a grid of disequilibrium models, the inferred C/O distribution becomes more restricted, showing that demographic chemical trends can depend strongly on the adopted retrieval parameterization. Several hot Jupiters converge to low C/O ($\leq$ 0.05), whereas colder, cloudy planets retain broad posteriors that reflect limited information content of their spectra. Our results suggest that population-level chemical trends inferred from free-chemistry retrievals should be interpreted with caution unless sample selection, residual structure, prior sensitivity, and chemical assumptions are explicitly tested.

</details>

## High-energy astrophysics

### [Impact of Effective Nucleon Mass and Symmetry Energy on Nuclear Pasta Phases and the Unified Equation of State of Neutron Stars](https://arxiv.org/abs/2611.25666v1)
*Shuying Li, Hong Shen, Jinniu Hu* · `nucl-th` · arXiv:2611.25666v1 · relevance 0.18

- **In one sentence**: We investigate how the effective nucleon mass and symmetry energy affect pasta phase properties and the unified equation of state (EOS) of neutron stars. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We investigate how the effective nucleon mass and symmetry energy affect pasta phase properties and the unified equation of state (EOS) of neutron stars. The nonuniform pasta structure is described within the self-consistent Thomas-Fermi approximation, while nucleonic interactions are treated in the relativistic mean-field framework with several typical parameter sets adopted. Our results indicate that the symmetry energy and its slope are crucial in determining the onset of pasta phases and their geometric configurations. In the high-density region where matter becomes uniform, the effective nucleon mass plays a dominant role. A larger effective nucleon mass tends to soften the EOS, which yields a smaller radius for a canonical $1.4 M_{\odot}$ neutron star and reduces the corresponding tidal deformability.

</details>

### [Strong Field Tidal Disruptions of Rotating Stars by Spinning Black Holes](https://arxiv.org/abs/2611.26043v1)
*Niles Mondal, Kowsona Chakraborty, Pratap Alte et al.* · `astro-ph.HE` · arXiv:2611.26043v1 · relevance 0.17

- **In one sentence**: We study tidal disruptions of rotating solar-type stars by a rapidly spinning supermassive black hole with general-relativistic smoothed-particle hydrodynamics. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We study tidal disruptions of rotating solar-type stars by a rapidly spinning supermassive black hole with general-relativistic smoothed-particle hydrodynamics. To capture strong-field effects, we place the pericentre at a few gravitational radii of a black hole, and compare with weak-field encounters at a larger pericentre around a lighter black hole. We vary the black hole spin, the orbital inclination and the stellar rotation, using rigidly and differentially rotating stars with spin aligned, anti-aligned or perpendicular to the orbital angular momentum. In the strong field, the black hole spin decides whether a core survives on equatorial and inclined orbits, and stellar rotation reduces the surviving core in every partial disruption. At the larger pericentre, as in Newtonian studies, anti-aligned rotation instead protects the star from disruption. In both cases the tide reverses an anti-aligned spin just before pericentre. The outcome differs because in the strong field the tide keeps acting on the reversed core long after pericentre. Deep encounters leave cores spinning above break-up, which shed mass and angular momentum as they settle. Full disruptions approach the canonical fallback law, whereas the late-time slope of partial disruptions is not universal and is set by the debris energy distribution near the surviving core.

</details>

## Stars and the Sun

### [Sherlock 'Chrones: The Curious Case of NGC 6791 and Asteroseismic Targets Therein Reveals Mixing Length Dependence on Evolutionary Stage](https://arxiv.org/abs/2611.25306v1)
*Eliza Frankel, Meridith Joyce, Jamie Tayar et al.* · `astro-ph.SR` · arXiv:2611.25306v1 · relevance 0.15

- **In one sentence**: As single-aged populations containing stars spanning a range of masses but otherwise with similar properties, star clusters provide valuable testbeds for stellar evolution theory. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

As single-aged populations containing stars spanning a range of masses but otherwise with similar properties, star clusters provide valuable testbeds for stellar evolution theory. The old, metal-rich, open cluster NGC 6791 is well studied, but the availability of asteroseismic observations of individual cluster members allows for a more in-depth analysis. Driven by mounting evidence that the solar assumption for convection used in almost all 1D stellar models is not adequate, and in light of the increased precision provided by modern data and asteroseismic constraints, we built and compared custom isochrones with varying values of the convective mixing length, $α_\text{MLT}$, to two clusters with well-determined ages: NGC 6791 and the well-studied, metal-poor globular cluster M92. For both clusters, we found that the best-fitting mixing length parameter decreases monotonically as a function of evolutionary phase, finding values between $0.98-1.10α_{\odot}$ for NGC 6791 and $1.16-1.21α_{\odot}$ for M92. In NGC 6791, this corresponds to an 18% decrease in the best fitting mixing length between the main sequence turn-off and upper end of the red giant branch. The degree of variation found within this one object is therefore comparable to variation across the literature in $α_\text{MLT}$ fits for other non-solar targets, calling single-valued $α_\text{MLT}$ fits to clusters into question. It is also consistent with $\log g$-$α_\text{MLT}$ trends predicted by higher-fidelity, 3D convection analyses. Our results therefore illustrate the need for more flexibility in our treatment of the mixing length in isochrones to properly model clusters.

</details>

### [3D Binary Evolution of a Merging Binary Black Hole Progenitor](https://arxiv.org/abs/2611.25310v1)
*David Dickson, Pablo Marchant, Jon Sundqvist et al.* · `astro-ph.SR` · arXiv:2611.25310v1 · relevance 0.11

- **In one sentence**: Mass transfer is a highly dynamical 3D process that spans evolutionary timescales in binary stars. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Mass transfer is a highly dynamical 3D process that spans evolutionary timescales in binary stars. It is key to the production of gravitational waves through formation of binary black holes and other double compact objects. We integrate global 3D hydrodynamics into stellar evolutionary modeling to resolve mass transfer across nuclear timescales. We employ the shellular approximation in the stellar evolution code MESA to map a 3D spatial structure by equipotential shells in the Roche geometry to maintain hydrostatic equilibrium across tidally-distorted surfaces. We employ the method of time-incremented multiscale evolution to alternate between stellar evolution and 3D hydrodynamics to span large timescales with dynamical feedback. We employ this framework to examine a likely merging binary black hole progenitor system of a low-metallicity 30Msol donor star and 9.3Msol black hole from the end of the main sequence to core Carbon depletion. We modeled two complete mass transfer phases in 3D while self-consistently accounting for stellar evolution. These comprised a thermal-timescale early Case B phase and a nuclear-timescale late Case B phase. The prescription of Kolb & Ritter (1990) closely predicted the results of 3D evolution, except at the end of the first phase of mass transfer; our 3D model remained well-contained by the outer Lagrange point, despite 1D predictions of substantial L3 overflow during this stage. We find incorporating 3D hydrodynamics during Case B mass transfer did not significantly impact expected merger times. Our model never overflowed L3 as predicted by 1D prescriptions. L2/L3 outflows formed even while underflowing those equipotentials. Our model suggests these outflows can be neglected for the evolution of similar systems, but were dense enough to potentially impact X-ray observations.

</details>

## Chemical physics

### [Witnessing Molecular Conformation via Optical Cycling Centers](https://arxiv.org/abs/2611.25851v1)
*Guo-Zhu Zhu, Taras Khvorost, Haowen Zhou et al.* · `physics.chem-ph` · arXiv:2611.25851v1 · relevance 0.11

- **In one sentence**: Molecular conformation plays a central role in determining molecular properties and dynamics. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Molecular conformation plays a central role in determining molecular properties and dynamics. Here, we report the production and conformer-resolved spectroscopy of cold calcium 3-hydroxyphenoxide radical (CaOC$_6$H$_4$-3-OH) in a cryogenic buffer-gas cell. Internal rotation of the hydroxyl group gives rise to distinct $anti$- and $syn$-conformers. The CaO moiety acts as an optical cycling center (OCC), enabling the $\widetilde A - \widetilde X$ and $\widetilde B - \widetilde X$ transitions of both conformers to be resolved by laser-induced fluorescence spectroscopy. Dispersed fluorescence measurements reveal diagonal vibrational branching fractions of 0.91-0.93, indicating favorable optical cycling characteristics. Following excitation of off-diagonal vibronic transitions near the calculated torsional barrier in the $\widetilde A$ state, the emission remains predominantly conformer specific, indicating that conformational identity is largely preserved over the excited-state fluorescence lifetime. These results demonstrate that a metal-centered OCC can serve as an intrinsic, site-specific optical reporter of molecular conformation, providing a foundation for repetitive optical readout and studies of conformational dynamics at the single-molecule level.

</details>

### [Triplet adiabatic potential energy surfaces for the O($^3$P) + C$_2$(X$^1Σ_g^+$, a$^3Π_u$) reaction and quasiclassical trajectory dynamics](https://arxiv.org/abs/2611.26233v1)
*A. Veselinova-Marinova, S. Gómez-Carrasco, L. González-Sánchez et al.* · `physics.chem-ph` · arXiv:2611.26233v1 · relevance 0.06

- **In one sentence**: We present three global adiabatic potential energy surfaces (PESs) for the O($^3$P) + C$_2$(X $^1Σ_g^+$, a $^3Π_u$) to CO(X$^1Σ^+$) + C($^3$P) reaction, computed at the icMRCI+Q/aug-cc-pVTZ level. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We present three global adiabatic potential energy surfaces (PESs) for the O($^3$P) + C$_2$(X $^1Σ_g^+$, a $^3Π_u$) to CO(X$^1Σ^+$) + C($^3$P) reaction, computed at the icMRCI+Q/aug-cc-pVTZ level. This reaction is relevant to combustion chemistry, atmospheric processes, and astrochemistry. Since the energy difference between the $^1Σ_g^+$ and $^3Π_u$ states of C$_2$ is smaller than the zero-point energy, both states mix upon interaction with the approaching O atom. Consequently, the PESs exhibit a double-well topography in the reactant valley. Beyond this feature, the three PESs display markedly different topographies. The 1 $^3A''$ PES features a deep minimum 7.16 eV below the O + C$_2$ entrance channel. In contrast, the 2 $^3A''$ and 1 $^3A'$ surfaces possess shallower collinear wells ($\approx$ 5.7 eV) and strong angular anisotropy arising from avoided crossings with higher-lying triplet states. The analytical fits reproduce the \textit{ab initio} data with root-mean-square (RMS) deviations of 0.022--0.028 eV over an energy interval exceeding 13 eV. Quasiclassical trajectory (QCT) calculations reveal higher reactivity on the barrierless $1\,^3A''$ surface compared to the $2\,^3A''$ PES, where an angle-dependent entrance barrier reduces the cross sections. Furthermore, cross sections for reactions initiated from C$_2$(X $^1Σ_g^+$) and C$_2$(a $^3Π_u$) are remarkably similar for the three PESs, regardless of the initial rovibrational state.

</details>

## Materials science

### [Reward misalignment as an opportunity for materials discovery](https://arxiv.org/abs/2611.26186v1)
*Ryotaro Okabe, Shoki Kishida, Abhijatmedhi Chotrattanapituk et al.* · `cond-mat.mtrl-sci` · arXiv:2611.26186v1 · relevance 0.19

- **In one sentence**: Reward misalignment is usually regarded as a failure of artificial intelligence. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Reward misalignment is usually regarded as a failure of artificial intelligence. In materials discovery with generative AI models, however, disagreement between predefined rewards and expert judgment may reveal materials that the rewards overlook. We investigate this possibility using electronic flat bands as a prime example. Experts mostly agree with a numerical bandwidth score, but their disagreements are systematic and cannot be explained by an estimated 5% rate of mistaken labels. We learn the experts' preferences from pairwise comparisons and use them to guide a crystal diffusion model. The learned preferences and numerical score agree on the flattest bands but diverge elsewhere. For example, the preferences favor KCo2As2 and CoGa, reported compounds with partially flat bands that the score would discard. The framework also extends to synthesizability and phonon properties. Our findings suggest that reward misalignment can expose opportunities for materials discovery beyond what fixed rewards are designed to find.

</details>

### [Intelligent Imaging of Thermal Transport in Nanostructures](https://arxiv.org/abs/2611.25779v1)
*Xin Qian, Te-Huan Liu, Xiaobo Li et al.* · `cond-mat.mtrl-sci` · arXiv:2611.25779v1 · relevance 0.14

- **In one sentence**: The ability to measure thermal properties and visualize heat transport processes with high spatial resolution is becoming increasingly important for materials discovery, next-generation electronics, and advanced manufacturing. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The ability to measure thermal properties and visualize heat transport processes with high spatial resolution is becoming increasingly important for materials discovery, next-generation electronics, and advanced manufacturing. As critical dimensions and architectures of novel materials and high performance electronics shrink and become more heterogeneous, thermal transport is no longer governed by bulk material properties alone, but by local variations in microstructure, such as interfaces and defects, while the operating conditions can also play a role. With the development of non-contact pump-probe thermoreflectance techniques, specific heat, thermal conductivity, and interface conductance can be mapped either through wide-field thermos-reflectance images or by scanning technique. However, key challenges remain such as the balance between imaging throughput and measurement accuracy, the extraction of multiple parameters with high confidence, and non-intrusive subsurface characterization, etc. This Review highlights recent advancements in artificial intelligence (AI)-assistance in high-throughput data processing, visualizing interfacial thermal transport, and nonintrusive subsurface analysis, and offers outlooks for future research directions such as spectral mapping of heat carriers, three-dimensional property mapping, and AI-agentic experimental designs. We anticipate this Review will motivate future efforts in combining AI with experimental techniques to achieve unprecedented capabilities for thermal characterization of nanoscale materials and device characterization, facilitating materials discovery and electronics revolution.

</details>

## Soft matter and polymers

### [Soft biological and bio-inspired materials](https://arxiv.org/abs/2611.25959v1)
*Livio Nicola Carenza, Giuseppe Negro, Adriano Tiribocchi* · `cond-mat.soft` · arXiv:2611.25959v1 · relevance 0.13

- **In one sentence**: This review surveys modeling approaches for active matter in soft biological and bio-inspired materials, focusing on active liquid crystal theory, topological defects, active turbulence, and the effects of geometric and topological confinement.
- **In plain words**: Living things and some engineered materials can use stored energy to move, reshape, and organize themselves, which makes them behave differently from ordinary soft matter like rubber or gels. This review looks at the mathematical models scientists use to describe these self-driven materials, especially a framework borrowed from liquid crystals that tracks how their molecular or cellular orientations line up. It also covers chaotic, swirling flow patterns called active turbulence, the role of defects where orientation patterns break down, and how confinement in tissues and cells can influence processes such as cell death and the shaping of embryos. The abstract describes the scope of the review rather than reporting new experimental results.
- **Why it matters**: Active matter is a growing bridge between physics, biology, and materials engineering, and models that explain both living tissue and synthetic swimmers could guide the design of robots and self-organizing materials. The abstract does not show specific new findings, so its value lies mainly in consolidating the field's theoretical toolkit.
- **Background needed**: ['Soft matter: materials such as gels, polymers, liquid crystals, and tissues that deform easily under small forces.', 'Active matter: systems whose constituents consume energy and generate their own motion, unlike passive materials that only respond to outside forces.', 'Liquid crystals: fluids whose elongated molecules share a preferred direction (orientation), which can be described by a continuous field.', 'Topological defects: points or lines where the orientation pattern cannot be smoothly continued, similar to a whirlpool or a hair whorl.', 'Active turbulence: chaotic, swirling flow produced by self-driven particles, distinct from the turbulence of ordinary fluids.', 'Confinement: restricting a material to a small or oddly shaped space, such as a cell or a tissue boundary, which can change its behavior.'] · level: research-level

<details><summary>Original abstract</summary>

Soft biological materials are a fascinating kind of matter characterized by the unique ability of consuming internal energy to perform complex tasks to preserve the life of the single organism or a whole community. Moreover, biologically inspired materials able to mimic specific features of biological systems can be exploited to design novel materials with vast potential applications in areas ranging from healthcare and robotics to energy and environmental sustainability. In this review, we focus on the modeling approaches used to capture the dynamics of this peculiar kind of active matter, starting from the observation of orientational symmetries and reviewing the basis of the so-called active liquid crystal theory, a celebrated model that was successfully used to interpret and investigate a number of different phenomena occurring in both biological and artificial realizations. We review the role of topological defects in biological systems and discuss the complex phenomenon of active turbulence, a chaotic dynamical regime observed in a variety of different realizations of systems of both biological and synthetic origin. Finally, we discuss how geometrical and topological confinement can also play an important role in many biological processes, from cellular apoptosis in epithelial tissue, to animal morphogenesis.

</details>

### [Topological trapping of active tracers in branched ring polymer matrices](https://arxiv.org/abs/2611.25528v1)
*Rahul Bag, Baburao Simma, Vrinda Garg et al.* · `cond-mat.soft` · arXiv:2611.25528v1 · relevance 0.10

- **In one sentence**: Langevin dynamics simulations compare passive and self-propelled (active) tracer diffusion in a matrix of branched ring polymers versus an unlinked mixture of linear rings at equal monomer density, finding that chain stiffness and connectivity trap active tracers and produce long-time subdiffusion and transient weak ergodicity breaking.
- **In plain words**: Many cells and synthetic materials are filled with tangled, branched large molecules that act like a crowded maze for anything moving through them. This paper uses computer simulations to ask how the shape and connectivity of these molecules, rather than just how crowded they are, change the movement of tiny particles, including self-propelled ones that move on their own like swimming microbes. The authors report that passive particles barely notice the difference, but self-propelled particles get stuck in cages formed by the connected branches when the chains are stiff, and an intermediate branch design traps them most effectively.
- **Why it matters**: It suggests that molecular topology alone can control how active particles get trapped, which may matter for understanding transport inside cells and for designing soft materials. The abstract is based only on simulations, so how well the findings carry over to real biological or synthetic systems is not shown here.
- **Background needed**: ['Tracer: a small particle followed to measure how a medium moves things through it.', 'Active (self-propelled) tracer: a particle that drives its own motion, like a swimming cell, rather than only being pushed around by thermal jiggling.', 'Passive tracer: a particle moving only from random thermal kicks.', 'Ring polymer: a large molecule closed into a loop; branched ring polymers have loops with side arms attached.', 'Packing fraction and monomer density: how much of the space is filled by the molecules; here the two systems are matched on this so only connectivity differs.', 'Subdiffusion: motion that spreads more slowly over time than ordinary random walking.', "Weak ergodicity breaking: a state where a particle's time average no longer matches its ensemble average, meaning it stays in one region for very long periods.", 'Leptokurtic displacement statistics: step-length distributions with more very short and very long jumps than a Gaussian, a sign of heterogeneous trapping.', 'Langevin dynamics: a simulation method that models particle motion with friction and random noise.', "Self-intermediate scattering function: a measure of how a particle's position decorrelates across a given length scale over time."] · level: research-level

<details><summary>Original abstract</summary>

Branched macromolecular architectures are ubiquitous in living systems and synthetic polymeric systems, create topologically complex media that strongly influence tracer dynamics beyond simple packing fraction-driven crowding effects. Motivated by biological systems such as amoebae, astrocytes, cytoskeletal assemblies, and cyclic bottlebrushes, we investigate active and passive tracer transport in polymeric environments of topologically distinct architectures. Here, using Langevin dynamics simulations, we focus on how polymer topology alters diffusion behavior in a branched-ring polymeric (BRP) environment. To isolate the role of intramolecular topology from monomer density, we specifically benchmark the BRP dynamics against an unlinked linear-ring polymer mixture (LRM). In general, we find that while passive tracers are largely unaffected by the polymer connectivity and bending rigidity, the self-propelled active tracers strongly distinguish between the two architectures. Increasing chain rigidity facilitates active diffusion in the unlinked LRM but strongly restricts mobility in the BRP matrix, driving a transition to pronounced long-time subdiffusion that becomes more prominent with propulsion strength. Different physical observables reveal that interconnected topological cages are formed in the stiff limit, leading to transient weak ergodicity breaking and leptokurtic displacement statistics. Further, the self-intermediate scattering function confirms that the short-range dynamics remain unaltered by the matrix connectivity, while relaxation at large spatial length scales is governed by the topological caging. Finally, varying the branch length and number, we identified an optimal branch architecture that maximizes active trapping. Our results establish that macromolecular connectivity and stiffness dominate the active transport even in the system of identical packing fraction.

</details>

## AI for chemistry and materials

### [From Benchmarks to the Bench: Preference, Correspondence and Selectivity in Bidirectional Drug-Target Screening](https://arxiv.org/abs/2611.26369v1)
*Jiangjie Qiu, Chengrui Xu, Xiaonan Wang* · `cs.LG` · arXiv:2611.26369v1 · relevance 0.41

- **In one sentence**: Identifying active molecules for known targets and potential targets for existing drugs is central to drug discovery and repurposing. (first sentence of the abstract; AI summaries are off)
- Matched keywords: molecule, molecular, drug discovery, protein

<details><summary>Original abstract</summary>

Identifying active molecules for known targets and potential targets for existing drugs is central to drug discovery and repurposing. Drug-target interaction (DTI) models can rank vast numbers of drug-target pairs, but limited experimental capacity restricts testing to a small number of candidates. We compared the bidirectional recommendations of 13 released systems across 711 molecular structures of FDA-approved drugs and 614 human proteins. For the same target or drug, pairs of models produced completely disjoint Top-10 molecule and protein lists in 77.8% and 70.1% of comparisons, respectively. Even where recommendations overlapped, agreement between some systems largely reflected recurring preferences for the same candidates. Published inhibition measurements for 79 molecules and 65 kinases revealed that some systems enriched active candidates, yet their hit yields changed little when recommendations were matched to different drugs or targets, whereas other systems lost substantially more hits. Some of the former systems also rarely ranked both molecules and kinases correctly when two drugs favoured different kinases. We further retrained the same architecture on the same data, with the training objective fixed and random seeds varied. Despite similar test performance, mean pairwise Top-10 overlap on a separate screening catalogue was about two candidates. Our study moves DTI model evaluation beyond benchmark performance to assess whether model predictions can guide meaningful experimental decisions in drug discovery and target identification.

</details>

### [Emergent Fatigue Dynamics from Foundational Interatomic Potentials](https://arxiv.org/abs/2611.26533v1)
*Jingye Tan, Benjamin A. Jasperson, Eric Rothchild et al.* · `cond-mat.mtrl-sci` · arXiv:2611.26533v1 · relevance 0.19

- **In one sentence**: Foundational machine-learned interatomic potentials are trained on large, diverse DFT datasets, but their validation rests on equilibrium states, which does not guarantee correct emergent behavior in large-scale molecular dynamics. (first sentence of the abstract; AI summaries are off)
- Matched keywords: molecular

<details><summary>Original abstract</summary>

Foundational machine-learned interatomic potentials are trained on large, diverse DFT datasets, but their validation rests on equilibrium states, which does not guarantee correct emergent behavior in large-scale molecular dynamics. Where no direct experimental validation is available, comparisons to physically motivated potentials are valuable for drawing insight. We distinguish static properties, which are thermally accessible, from emergent properties, which require work from an external fatigue stress to drive rare events, and compare the potentials on both. An EAM potential and the NequIP foundational potential both agree closely with reference data for many near-equilibrium properties, but NequIP predicts an anomalously low intrinsic stacking fault energy ($\sim7$ times lower than EAM) and thus predicts far more plastic deformation under fatigue cycling of a nanoscale flaw modeled after the classical Griffith crack problem. Per-atom energy distributions after loading show that the two potentials differ most at energies far above what is thermally accessible. We also document memory-related crashes and silent extrapolation as practical concerns for practitioners of these foundational model forms.

</details>

## Biochemistry

### [Unexpected properties of nucleotide condensates could facilitate the RNA world](https://www.biorxiv.org/content/10.64898/2026.11.18.767475v1)
*Hauf, S.; Baidya, L.; Nakamura, R. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.18.767475 v1 · relevance 0.07

- **In one sentence**: A key question in the RNA world hypothesis for the origin of life is the nature of the compartment that separates and protects the RNA from its environment. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

A key question in the RNA world hypothesis for the origin of life is the nature of the compartment that separates and protects the RNA from its environment. While membranes are a leading candidate for the initial compartment, biomolecular condensates have been proposed as an alternative, possibly simpler route to compartments. Here we show that bona fide liquid condensates form spontaneously when nucleotides (such as ATP) are mixed with divalent cations and a short-chain alcohol or diol in water. These condensates do not require any polymer to form, but can concentrate polymers like RNA and DNA, which show unexpected chemical behavior inside the condensates. Most surprisingly, RNA survives for days inside nucleotide condensates under acidic conditions that cause rapid and extensive hydrolysis in bulk. This effect is also observed for a phosphate-ester model substrate and therefore likely reflects the suppression of backbone cleavage. Coarse-grained simulations suggest that the condensate interior is bound together by magnesium-phosphate bridging interactions and is therefore highly depleted of water. At neutral pH, the same compartment reverses the course of a hammerhead ribozyme reaction, shifting it from cleavage toward religation. Finally, we observe that nucleotide droplets also spontaneously organize phospholipids at their surface, suggesting a possible evolutionary route from biomolecular condensates toward membranes. Thus, we believe that nucleotide condensates, which are built from the same building blocks as the genetic polymers themselves, overcome long-standing challenges with the RNA world hypothesis for the origin of life by protecting nucleic acids and reshaping their chemistry.

</details>

### [Paired Deep Mutational Scanning of Lck Activity and Inhibitor Sensitivity Enables the Engineering of Pharmacological Control of T Cell Receptor Signaling](https://www.biorxiv.org/content/10.64898/2026.11.13.766442v1)
*Potter, Z. E.; Graves, A. N.; Brown, J. L. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.13.766442 v1 · relevance 0.07

- **In one sentence**: Controlling signaling enzymes with small molecules is a central goal in chemical biology and is of great utility for engineering cell-derived immunotherapies. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Controlling signaling enzymes with small molecules is a central goal in chemical biology and is of great utility for engineering cell-derived immunotherapies. Yet strategies for conferring selective small-molecule sensitivity without disrupting a protein's native function remain limited. Here we present a generalizable approach to engineering small molecule-controlled multidomain protein kinases. Using deep mutational scanning of full-length Lck, a tyrosine kinase essential for T cell receptor (TCR) signaling, we measured the effect of nearly all single amino acid substitutions in the kinase domain on phosphotransferase activity. The resulting activity landscape defined the domain's tolerance to substitution, mapped the regulatory interfaces that tune phosphotransferase activity, and, by treating bulky substitutions as ligand proxies, nominated cryptic pockets where covalent liganding is predicted to allosterically inhibit Lck. In parallel screens, we measured the sensitization of each variant to five clinically approved, reversible drugs: dabrafenib, erlotinib, gefitinib, imatinib, and nilotinib. Together, these landscapes identified substitutions that preserved or enhanced activity while sensitizing Lck to inhibition. Sensitizing substitutions were distributed throughout the kinase domain, including positions more than 30 [A] from the ATP-binding site, implicating long-range allosteric networks linking distal perturbations to ATP-binding site conformation and inhibitor potency. Integrating the activity and sensitization landscapes yielded a nilotinib-sensitized variant, I312S, that supports TCR signaling and, upon drug treatment, selectively suppresses proximal signaling and IL-2 production in Jurkat cells even in the presence of endogenous Lck.

</details>

## Pharmacology and drug discovery

### [Lipid nanoparticle-delivered Cas13b ribonucleoproteins targeting survivin overcome gemcitabine resistance in pancreatic cancer](https://www.biorxiv.org/content/10.64898/2026.11.18.767627v1)
*Castano-Esteban, D.; Lopez-Valls, M.; Santos, M. et al.* · `pharmacology and toxicology` · bioRxiv doi:10.64898/2026.11.18.767627 v1 · relevance 0.04

- **In one sentence**: Pancreatic ductal adenocarcinoma (PDAC) remains one of the deadliest cancers, largely due to its poor response to chemotherapy and the development of drug resistance. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Pancreatic ductal adenocarcinoma (PDAC) remains one of the deadliest cancers, largely due to its poor response to chemotherapy and the development of drug resistance. Survivin (BIRC5), an inhibitor of apoptosis frequently overexpressed in PDAC, contributes to tumor cell survival and gemcitabine resistance, making it an attractive therapeutic target. Here, we developed a lipid nanoparticle (LNP)-based platform for the delivery of preassembled spCas13b ribonucleoproteins (RNPs) to achieve transient and sequence-specific RNA silencing in pancreatic cancer cells. We optimized ionizable lipid formulations for Cas13b RNP encapsulation and identified a formulation achieving approximately 80% encapsulation efficiency, with sustained colloidal stability and gene-silencing activity during seven days of storage at 4{degrees}C. LNP-delivered Cas13b RNPs efficiently silenced endogenous BIRC5 in three pancreatic cancer cell lines, reducing survivin protein levels and inducing apoptosis. In gemcitabine-resistant PANC-1 cells, BIRC5 silencing synergistically enhanced the cytotoxic effect of gemcitabine in vitro. This therapeutic combination was further evaluated in a PANC-1 xenograft model, where only the combined administration of BIRC5-targeting Cas13b RNP-LNPs and gemcitabine significantly inhibited tumor growth, without apparent systemic toxicity. Intratumoral administration also restricted nanoparticle distribution to the injected tumors. These findings establish LNP-mediated delivery of Cas13b RNPs as a new strategy for transient RNA-targeted therapy and provide proof of concept for combining survivin silencing by Cas13b with chemotherapy to address gemcitabine resistance in pancreatic cancer.

</details>

## Computational and systems biology

### [DRAFT: graph-recurrent learning of dynamic gene regulatory networks along single-cell multi-omics trajectories](https://www.biorxiv.org/content/10.64898/2026.11.17.767145v1)
*Zhang, Z.; Santhi Sekhar, P.; van Nierop y Sanchez, P. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.17.767145 v1 · relevance 0.19

- **In one sentence**: Single-cell multi-omics data offer an opportunity to resolve how gene regulatory networks (GRNs) are rewired during cell-fate transitions, but most existing methods infer static snapshots, ignore temporal dependencies or assume linear regulation. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Single-cell multi-omics data offer an opportunity to resolve how gene regulatory networks (GRNs) are rewired during cell-fate transitions, but most existing methods infer static snapshots, ignore temporal dependencies or assume linear regulation. Here we present DRAFT, a deep learning framework that combines graph attention with recurrent temporal memory to infer dynamic GRNs from time-resolved single-cell multi-omics data. On simulated data, DRAFT outperforms existing methods in accuracy and temporal smoothness. In mouse cellular reprogramming and Drosophila adult spermatogenesis, it recovers interactions supported by independent ChIP-seq, perturbation and Hi-C data, together with known stage-specific regulators. By inferring regulatory activity from dynamic network structure rather than expression alone, DRAFT identifies regulators whose activity precedes their transcriptional peak, including the candidate early germline regulator Mondo. Germline-specific Mondo knockdown alters germline stem cell number and expression of the predicted targets kuz and mamo. DRAFT also enables nonlinear alignment of co-developing lineages and reveals stage-specific cell-cell communication.

</details>

### [Gene regulatory networks and the organization of cell differentiation in multicellular organisms](https://www.biorxiv.org/content/10.64898/2026.11.18.767571v1)
*Meraz-Segura, L. F.; Guerrero Vaca, A. C.; Alcaraz Barrera, R. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.18.767571 v1 · relevance 0.19

- **In one sentence**: Across their development, clonal multicellular organisms generate new cell types from less differentiated cell types. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Across their development, clonal multicellular organisms generate new cell types from less differentiated cell types. Differentiation pathways arrange into a hierarchical, tree-like organization: regressions from specialized to undifferentiated cell types rarely occur and undifferentiated cell types often have the potential to produce, when subject to distinct stimuli, two or more differently specialized cell types. How cell type transitions acquire such a peculiar disposition requires an explanation that must reside in the properties of gene regulatory networks (GRNs); after all, GRNs orchestrate the changes in gene activity that define cell types. We studied vast numbers of small dynamic model networks to search for elementary GRNs that could yield the simplest hierarchical, developmental-like, differentiation patterns. We found that only a small minority of GRNs are compatible with hierarchical cell type transitions. Importantly, GRNs that yielded developmental-like differentiation patterns shared common traits: One is the presence of tangles of cycles of positive interactions. Genes in such a tangle produce an all-or-none one-way response to a signal. Another such trait is mutual inhibition between genes associated to different specialized cell types, enforcing their mutually exclusive activation. Moreover, these regulatory patterns are more abundant in published experimentally sustained developmental GRNs than as expected by chance. In addition, we show that it is easy to maintain hierarchical cellular differentiation throughout evolution, even when undergoing changes in gene regulatory interactions and developmental mechanisms. Our work supports the prevalence of design principles that organize hierarchically differentiation pathways in clonal multicellular organisms.

</details>

## Neuroscience

### [Universal barcoded connectomics for massively parallel single-neuron projection mapping in diverse vertebrate species](https://www.biorxiv.org/content/10.64898/2026.11.19.767886v1)
*Qi, H.; Wan, X.; Cheron, J. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.19.767886 v1 · relevance 0.11

- **In one sentence**: The authors adapt sequencing-based barcoded connectomics, which tags single neurons' long-range projections with DNA barcodes, so it works across seven vertebrate species from frogs to primates, and they report a single reagent set that functions across divergent species.
- **In plain words**: Neuroscientists learn how brains are wired mostly in a few well-studied animals, because detailed wiring maps are hard to make in others. This paper tries to make a fast, high-resolution wiring-mapping method work in seven vertebrate species, from frogs and birds to monkeys. The authors report a fix for a practical problem: getting the delivery viruses to infect the right cells and carry their tags properly in each species. They test this by mapping the projections of thousands of neurons in a songbird brain region, and say one set of reagents works across very different species.
- **Why it matters**: If the reagents work as described, they could let researchers compare the same kind of brain circuit across animals that are far apart on the evolutionary tree, which is hard to do today. The abstract does not give per-species results, success rates, or detailed comparisons, so how reliably the method transfers to each species cannot be judged from it alone.
- **Background needed**: ['Connectomics: mapping which neurons connect to which, often at the level of individual cells.', 'Viral tracing: a modified virus is injected into one brain area, spreads to connected neurons, and reveals their projections.', 'Barcoding: each virus particle carries a unique short DNA tag, so sequencing the tags shows which starting neurons reached which target sites, letting many neurons be traced in parallel.', 'Viral tropism: the tendency of a virus to infect certain cell types; it varies between species, which is a main obstacle to using one tool across animals.', 'Model species: animals such as mice, zebra finches or macaques that labs use because their biology is well studied.'] · level: intermediate

<details><summary>Original abstract</summary>

Neuroscience relies on diverse model species to understand animal behavior and brain function. Yet, tools for rapid, high-resolution brain connectivity mapping remain unavailable in most vertebrate species, slowing progress in many neuroscience models and rendering cross-species circuit comparisons challenging. Here, we overcome this barrier by establishing sequencing-based barcoded connectomics for rapid single-neuron tracing in seven vertebrate species ranging from frogs to birds to non-human primates. We develop a general solution to viral tropism and barcode trafficking, validate our reagents by mapping the projections of thousands of neurons in the songbird HVC, and discover a single set of reagents that functions across highly divergent species. Together, we provide ready-to-use barcoding reagents for diverse species and a simple framework for further adapting them if necessary, enabling high throughput single-neuron tracing across vertebrates.

</details>

### [Motor learning engages intrinsic plasticity in the human cortex](https://www.biorxiv.org/content/10.64898/2026.11.19.767269v1)
*Clennell, B.; Luo, B.; Lam, K. T. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.19.767269 v1 · relevance 0.10

- **In one sentence**: Learning is commonly explained by changes in synaptic strength. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Learning is commonly explained by changes in synaptic strength. In animals, however, learning also engages intrinsic plasticity -- changes in how readily neurons convert synaptic input into firing. Its contribution to human learning has been unclear, because conventional non-invasive measures of cortical excitability primarily reflect synaptic strength. Here we used controllable-pulse transcranial magnetic stimulation to estimate two biophysical indices of intrinsic excitability in human motor cortex, before and after motor training. Training produced signatures of increased intrinsic excitability, selectively in the cortical representation of the trained muscle, but not an untrained muscle. Individuals showing larger intrinsic excitability changes learned faster, independently of changes in motor-evoked potential amplitude, an index of synaptic excitability that increased following training but did not predict learning rate. An axon model reproduced the measured changes through small shifts in membrane excitability. These findings provide evidence that intrinsic plasticity is expressed in the intact human brain, and that it represents a behaviourally relevant component of learning-related cortical adaptation.

</details>

## Genetics and genomics

### [ChIMe-seq enables multimodal epigenetic profiling in single molecules and single cells](https://www.biorxiv.org/content/10.64898/2026.11.17.767085v1)
*Verity-Legg, J.; Joly-Smith, E.; Straver, R. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.17.767085 v1 · relevance 0.12

- **In one sentence**: Recent advances in single-cell and single-molecule sequencing have enabled high-resolution characterization of epigenetic states. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Recent advances in single-cell and single-molecule sequencing have enabled high-resolution characterization of epigenetic states. However, methods that jointly measure multiple layers of epigenetic regulation within the same molecules and cells remain limited. Here, we developed Chromatin Immuno-Methylation sequencing (ChIMe-seq), a multimodal approach that simultaneously profiles histone modifications, DNA methylation, and nucleosome positioning genome-wide in single molecules and single cells. In contrast to recent approaches that rely on enzymatic fragmentation, ChIMe-seq preserves long DNA molecules by using a methyltransferase to deposit exogenous methylation marks that report on proximal histone modifications. This enables integration of multiple epigenetic features within individual molecules and supports short-read, long-read, and single-cell sequencing. These multimodal measurements are integrated into a novel mathematical framework that captures the coupling between nucleosome positioning, histone modifications, and DNA methylation. Both single-molecule and single-cell analyses reveal that DNA methylation is linked to nucleosome density in a manner modulated by local histone modifications, whilst differences in nucleosome:DNA structures are observed depending on epigenetic context and cell-type. Together, these results establish ChIMe-seq as a framework to investigate multifaceted epigenetic coordination across scales, from single-nucleotide resolution to long-range chromatin organization in single molecules and single cells.

</details>

### [FULL-seq reveals isoform-specific regulatory architecture in single cells](https://www.biorxiv.org/content/10.64898/2026.11.17.767299v1)
*Wang, M.; Qi, J.; Monticolo, F. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.17.767299 v1 · relevance 0.12

- **In one sentence**: Gene regulation is commonly modeled at the gene level, yet genes express multiple isoforms from distinct transcription start sites whose regulatory architecture is not resolved by current approaches. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Gene regulation is commonly modeled at the gene level, yet genes express multiple isoforms from distinct transcription start sites whose regulatory architecture is not resolved by current approaches. Here we introduce FULL-seq, a scalable single-cell multiomic platform that jointly profiles chromatin accessibility and full-length transcript coverage from the same cell, enabling direct coupling of regulatory elements to alternative first exon (AFE) usage. FULL-seq achieves high sensitivity for both transcriptome and chromatin accessibility while providing transcript-wide coverage across mRNAs up to 15 kb with precise exon-level mapping. We uncover diverse promoter-AFE regulatory architectures, revealing distinct transcription factor programs across alternative first exons of the same gene, and show that gene-level annotation frameworks can obscure regulatory relationships in multi-promoter genes. Applying FULL-seq to human cancer cells further reveals metastasis-associated AFE programs that are not apparent from gene-level expression. These AFE programs were reproduced in independent colorectal cancer cell-line datasets, and CALB1 AFE activation was observed in a subset of liver metastases from an independent patient cohort. Furthermore, CRISPRi-mediated repression of metastasis-associated CALB1 AFEs reduced colorectal cancer cell migration. Together, our findings establish alternative promoter and first-exon usage as a functionally relevant layer of gene regulation and demonstrate that FULL-seq enables regulatory relationships and cellular phenotypes to be connected at the promoter-isoform level.

</details>

## Cell and molecular biology

### [Modelling Maternal-to-Zygotic Transition Dynamics to Identify Common Gene Expression Baselines in Zebrafish Development.](https://www.biorxiv.org/content/10.64898/2026.11.17.767246v1)
*grosse Holthaus, M.; Michaelis, P.; Schunck, F. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.17.767246 v1 · relevance 0.12

- **In one sentence**: We propose a semi-mechanistic ODE-based transcription model for zebrafish embryogenesis that captures common baseline expression dynamics by integrating the maternal-to-zygotic transition mechanism. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

We propose a semi-mechanistic ODE-based transcription model for zebrafish embryogenesis that captures common baseline expression dynamics by integrating the maternal-to-zygotic transition mechanism. We fitted this model to a time-course RNA-seq dataset of D. rerio spanning early developmental stages until 120 hpf. Using the inferred model parameters, we identified common gene expression pattern using fuzzy c-means clustering and compared these with clusters stemming from a shape-based approach using smooth trajectories. We show that the ODE-parameter-based approach improves to biological interpretability by linking clusters to underlying regulatory mechanism, such as the timing of zygotic genome activation, thereby generating more precise expression clusters. However, the results also revealed technical biases of the time-course data, originating from the poly(A) enrichment step.

</details>

### [Centimeter-sized Human Vitreous Organoids from Pluripotent Stem Cells](https://www.biorxiv.org/content/10.64898/2026.11.19.767433v1)
*Zhang, X.; Jin, K.; Lin, X. et al.* · `developmental biology` · bioRxiv doi:10.64898/2026.11.19.767433 v1 · relevance 0.12

- **In one sentence**: The vitreous, the largest intraocular tissue, provides a transparent light path and maintains the intraocular homeostasis. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The vitreous, the largest intraocular tissue, provides a transparent light path and maintains the intraocular homeostasis. The reconstitution of the vitreous in vitro or in vivo remains an unsolved biomedical challenge. Here, we discovered a common feature, the "growth edge", constituted primarily of fibroblasts and their secreted proteins in human and mouse vitreous development. By leveraging the transforming growth factor beta signaling, we then generated centimeter-scale vitreous-like organoids (VOs) through stepwise differentiation from human pluripotent stem cells (hPSCs). The VOs exhibited striking similarity to human vitreous in terms of physical transparency, vitreoretinal interface, molecular composition, biological profiles and regenerative transplantability. Lines of evidence supported that fibroblasts are the key cell hub for vitreous development. Finally, VOs with a transthyretin (TTR) mutation recapitulated the vitreous phenotypes of human patients with vitreous amyloidosis. Together, vitreous organoid technology opens avenues for future studies of human vitreous development, disease modeling, and regenerative therapeutics for a broad spectrum of human vitreoretinal diseases.

</details>

## Immunology and microbiology

### [Emergence of mobile fosA3-blaCTX-M-65 with mcr-1.1 and tet(X4) on conjugative plasmids in avian pathogenic Escherichia coli from industrial poultry in Pakistan](https://www.biorxiv.org/content/10.64898/2026.11.19.767496v1)
*Umair, M.; Fatima, F.; Mathias, J. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.19.767496 v1 · relevance 0.13

- **In one sentence**: The emergence of plasmid-mediated resistance to critically important antimicrobials poses a growing threat to global health. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The emergence of plasmid-mediated resistance to critically important antimicrobials poses a growing threat to global health. Here we report the first genomic evidence of plasmid-mediated fosA3 and blaCTX-M-65 coexisting with mcr-1.1 and tet(X4) in multidrug-resistant Escherichia coli from clinically healthy broiler chickens in Pakistan. Among 1,677 high-quality genomes collected through antimicrobial resistance surveillance in Punjab, Pakistan, three isolates recovered between 2022 and 2024 harboured all four resistance determinants. Hybrid genome assemblies showed that fosA3 and blaCTX-M-65 were co-located on IncHI2A plasmids, whereas mcr-1.1 and tet(X4) were carried on separate IncI2 and IncFIA/IncFIC plasmids, all predicted to be conjugative; in one isolate the tet(X4) contig did not circularise. The isolates belonged to sequence type 93 and exhibited resistance to fosfomycin, colistin, tigecycline and cefotaxime. Comparative genomic analysis revealed highly conserved IncHI2A plasmid backbones, with an additional integron-associated resistance region in the 2024 isolates, suggesting acquisition of accessory resistance determinants. Resistance to three last-line antimicrobial classes and a canonical virulence profile now coexist on conjugative plasmids in poultry E. coli, a combination that favours co-selection and argues for plasmid-resolved surveillance in poultry production.

</details>

### [An Infected Cryopreserved Precision-Cut Lung Slice Model for Drug Susceptibility Testing in Pneumocystis murina Pneumonia](https://www.biorxiv.org/content/10.64898/2026.11.19.767844v1)
*Pellegrino, M. R.; McLean, J. L.; Kottom, T. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.19.767844 v1 · relevance 0.12

- **In one sentence**: Precision-cut lung slices (PCLS) preserve native three-dimensional lung architecture and cellular complexity, providing a valuable ex vivo platform for studying pulmonary host-pathogen interactions. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Precision-cut lung slices (PCLS) preserve native three-dimensional lung architecture and cellular complexity, providing a valuable ex vivo platform for studying pulmonary host-pathogen interactions. However, existing PCLS infection models typically introduce microorganisms into previously uninfected tissue, while fresh PCLS prepared from infected lungs have limited experimental flexibility and scalability. To our knowledge, cryopreserved PCLS generated from lungs with an established in vivo pulmonary infection have not been described. Herein, we evaluated cryopreserved PCLS from mice with established Pneumocystis murina pneumonia (PCP) as an ex vivo platform for infection and therapeutic studies. PCLS were prepared from dexamethasone-immunosuppressed mice with established PCP, rested for 24 h, cryopreserved in a novel freezing medium for 12 days in liquid nitrogen, rapidly thawed, recovered for 24 h, and treated with pentamidine for 72 h. Viability was assessed in uninfected and PCP-infected PCLS before and after cryopreservation. Although post-thaw viability decreased in both groups, substantial viability was still retained, allowing further experimentation. qPCR showed that cryopreservation did not alter expression of the type I and type II alveolar epithelial markers podoplanin (Pdpn) and surfactant protein C (Sftpc) in either group. Importantly, pentamidine significantly reduced Pneumocystis mitochondrial small subunit (mtSSU) rRNA levels in thawed PCP-infected PCLS, demonstrating suitability for anti-Pneumocystis drug testing. These findings establish the first cryopreserved ex vivo PCP model using infected mouse PCLS, preserving endogenous fungal burden and infection-associated host responses while enabling flexible, scalable studies of Pneumocystis biology, host-pathogen interactions, therapeutic efficacy, and potentially other pulmonary infections.

</details>

## Cancer biology

### [ERM proteins antagonistically control cancer invasion and metastasis via mechanosensing regulation](https://www.biorxiv.org/content/10.64898/2026.11.16.767111v1)
*Amer, M.; McCann, J. V.; Napso Shogan, T. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.16.767111 v1 · relevance 0.13

- **In one sentence**: The paper reports that in breast cancer models the three ERM proteins (ezrin, radixin, moesin) rise together in highly metastatic cells yet act in opposite directions, with ezrin loss reducing and radixin or moesin loss enhancing invasion, colony formation, and lung metastasis, linked to changes in focal adhesions, FAK activation, and force transmission to the matrix.
- **In plain words**: Cancer spreads when cells break loose and travel to new organs, and they must sense and pull on their surroundings to do so. This study looks at three related proteins, ezrin, radixin and moesin, that help link a cell's internal skeleton to its outer membrane. The authors found that all three are more abundant in highly spreading breast cancer cells, but removing ezrin reduced spread in their tests while removing radixin or moesin increased it, with the effects tied to how strongly cells pull on their surroundings.
- **Why it matters**: It suggests that the three proteins are not simply interchangeable markers of cancer spread but can have opposing roles, which matters if anyone tries to target them therapeutically. The abstract does not say whether these findings hold in human tumours or other cancer types, so the translational reach is unclear.
- **Background needed**: ['Metastasis: the spread of cancer from its original site to distant organs, such as the lungs.', 'Anchorage dependence: normal cells need to attach to a surface to grow; metastatic cells must loosen this requirement.', 'Mechanosensing: how cells detect and respond to physical forces from their environment.', 'Focal adhesions: small anchor points where a cell grips the extracellular matrix, the mesh of proteins around cells.', 'ERM proteins: ezrin, radixin and moesin, which link the cell membrane to the actin cytoskeleton (the internal scaffold of the cell).', 'FAK (focal adhesion kinase): a signalling enzyme that becomes activated at focal adhesions and helps drive cell movement.', "Contractility: the ability of the cell's internal scaffold to pull, which generates the forces transmitted outward."] · level: research-level

<details><summary>Original abstract</summary>

Metastasis requires cancer cells to overcome anchorage dependence and rewire mechanosensing pathways. Here, we identify the ERM proteins ezrin, radixin, and moesin as key but antagonistic regulators of breast cancer metastasis. Expression profiling across matched low- and high-metastatic breast cancer models revealed consistent upregulation of all three ERM proteins in highly metastatic cells. Despite this, ezrin depletion reduced colony formation, invasion, and lung metastasis, whereas radixin or moesin depletion enhanced these phenotypes. Loss of radixin or moesin increased ezrin localization at the cell edge, while ezrin depletion reduced membrane-associated moesin, indicating a dynamic balance among ERM proteins. Ezrin depletion also increased focal adhesion size and number, FAK activation, and force transmission to the extracellular matrix, whereas radixin or moesin silencing produced opposite effects. Cellular force magnitude was inversely correlated with invasion, and pharmacological modulation of contractility reverted the effects of ERM depletion. These findings reveal an ERM-dependent mechanosensing checkpoint that regulates metastasis through control of adhesion dynamics and force transmission.

</details>

### [B7-H3 Orchestrates Fibro-Immune Spatial Organisation in Pancreatic Cancer](https://www.biorxiv.org/content/10.64898/2026.11.16.762837v1)
*Legrini, A.; Zhang, T.; McGuigan, M.-C. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.16.762837 v1 · relevance 0.12

- **In one sentence**: Pancreatic ductal adenocarcinoma (PDAC) remains one of the most lethal cancers in the western world and is largely resistant to treatment. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Pancreatic ductal adenocarcinoma (PDAC) remains one of the most lethal cancers in the western world and is largely resistant to treatment. A major barrier to effective treatment is the highly desmoplastic and immunosuppressive tumour microenvironment, where the organisation of tumour, stromal and resident immune cells limit immune infiltration. B7-H3 (CD276) is an emerging immune checkpoint marker investigated in phase I and Ib/2 clinical trials in PDAC, yet its biological role within the tumour environment remains poorly understood. We performed an integrated multiscale spatial profiling study to map B7-H3 expression across regional and single-cell spatial contexts in treatment-naive resected human PDAC. Furthermore, we explored the B7-H3 landscape in the neoadjuvant setting. Our results demonstrate that B7-H3 is not simply overexpressed in cancer but may act as a spatial organiser of the PDAC microenvironment, associated with a transition from epithelial-intrinsic tumour architecture to fibro-inflammatory immune states that underpin immune suppression, aggressive disease and poor prognosis. This fibro-inflammatory state appears conserved within the neoadjuvant landscape.

</details>

## Ecology and evolution

### [A unifying framework for structured population dynamics in modern coexistence theory](https://www.biorxiv.org/content/10.64898/2026.11.13.766574v1)
*Brennan, J.* · `ecology` · bioRxiv doi:10.64898/2026.11.13.766574 v1 · relevance 0.16

- **In one sentence**: The paper proposes a general framework for extending modern coexistence theory to account for variation among individuals within populations, and illustrates it with three case studies (influenza substrains, perennial plants, and prey with a foraging-predation risk tradeoff).
- **In plain words**: Ecologists often model a species as if every individual behaves the same way toward its competitors, but real populations contain varied individuals, and that variation can affect whether species can live together. The author proposes a single framework for building this within-population variation into the existing modern coexistence theory, which is meant to work across different areas of ecology. The abstract presents three example applications, but it does not report specific numerical results, so the strength of the findings cannot be judged from it alone.
- **Why it matters**: Several subfields of ecology have been working on this same question separately, so a shared framework could help them compare results and connect population-level and community-level processes. Whether it delivers on that promise depends on the detailed case studies, which the abstract only summarizes.
- **Background needed**: ['Coexistence theory asks why different species can persist together in the same place instead of one driving the others out.', 'Modern coexistence theory often separates stabilizing mechanisms (species limit their own growth more than that of rivals) from fitness differences (some species are simply better competitors).', 'Invasion tests check whether each species can increase when rare, which is a common way to decide whether coexistence is possible.', 'Structured populations are groups whose members differ in traits such as age, size, strain, or behavior, rather than being identical.', 'Niche overlap measures how much two species rely on the same resources.', 'A foraging-predation risk tradeoff means feeding more exposes an animal to predators, so animals must balance food gain against danger.'] · level: research-level

<details><summary>Original abstract</summary>

Variation within populations is ubiquitous in nature, yet many models and frameworks in community ecology assume that all individuals within a population interact with the community identically. Modern coexistence theory is no exception; however, several subfields of ecology have independently been integrating coexistence theory, each asking the same underlying question: how do structured population dynamics shape coexistence outcomes? Here, I propose a unifying framework for integrating population variation into modern coexistence theory that is applicable across all fields of ecology. The application of this framework is presented in three case studies: niche overlap and fitness differences between influenza substrains, mutual invasibility between competing perennial plants, and fluctuation-dependent invasion outcomes in apparently competing prey with a foraging-predation risk tradeoff. Together, these examples illustrate the framework's broad applicability, power to resolve the interaction between population and community level processes, and its potential to reveal novel ecological phenomena.

</details>

### [Phenotypic plasticity reshapes the evolution of species coexistence](https://www.biorxiv.org/content/10.64898/2026.11.19.767819v1)
*Venugopal, V.; Baruah, G.; Wittmann, M. J.* · `ecology` · bioRxiv doi:10.64898/2026.11.19.767819 v1 · relevance 0.10

- **In one sentence**: The paper builds a framework that combines modern coexistence theory with competition-induced phenotypic plasticity and evolution for two competing species, showing that the breadth of available resources determines whether divergent or convergent plasticity promotes or hinders coexistence.
- **In plain words**: Two species that compete for the same resources can either share the living space or one can wipe out the other; ecologists have good tools for predicting this, but those tools mostly ignore that organisms can change their traits within their lifetimes in response to competitors, as well as evolving over generations. The authors write down a mathematical framework that includes both kinds of change for two competing species, and study how it plays out when the range of available resources is broad versus narrow. From the abstract, they report that in broad environments, plastic changes that push the species apart speed up the move toward coexistence, while in narrower environments the same kind of change can instead lead to one species being excluded.
- **Why it matters**: It matters because it suggests that short-term, reversible trait responses can change where long-term evolution ends up, so studies that ignore plasticity may misjudge which species persist. The abstract does not show empirical tests, so its practical reach is unclear; it may connect to work on how biodiversity responds to rapid environmental change.
- **Background needed**: ['Coexistence theory: a framework asking when competing species can persist together, usually decomposed into niche difference (how much they differ in resource use) and fitness difference (how evenly matched they are).', 'Invasion growth rate: how fast a rare species grows when competing with the common one; a positive value means it can recover and so coexist.', 'Phenotypic plasticity: an individual changing its traits (such as feeding or behaviour) during its life in response to its surroundings, as opposed to genetic change over generations.', 'Evolution of coexistence components: the idea that natural selection can shift niche and fitness differences over time, so coexistence can emerge or fail through evolution.', "Divergent versus convergent plasticity: whether competition pushes the two species' traits further apart or closer together.", 'Resource breadth: how many different resource types are available; narrow environments offer fewer options, so competitors overlap more.'] · level: research-level

<details><summary>Original abstract</summary>

Modern coexistence theory (MCT) has been the mainstay of recent research on coexistence of competing species. Competition not only drives evolutionary changes in traits that affect coexistence, but also induces rapid plastic changes. However, a generalised framework that integrates plasticity and evolution into MCT is lacking. We formulate such a framework for a system of two competing species and analyse how breadth of available resources modulates the effect of competition-induced plasticity on the evolution of coexistence components (niche and fitness difference). We find that, in broad environments, divergent plasticity accelerates evolution towards positive invasion growth rates for both species, facilitating coexistence, whereas convergent plasticity hinders this process. Surprisingly, in narrower environments, divergent plasticity can hinder coexistence, leading to exclusion, whereas convergent plasticity can facilitate coexistence. Our results show that plasticity reshapes the eco-evolutionary trajectories to coexistence, highlighting the importance of integrating short-term plastic responses with long-term evolutionary dynamics.

</details>

## Plant biology

### [The intracellular respiratory burst of plant immunity signaling](https://www.biorxiv.org/content/10.64898/2026.11.18.767486v1)
*Barreto, P.; Feitosa-Araujo, E.; Knorr, L. S. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.18.767486 v1 · relevance 0.14

- **In one sentence**: Pattern-triggered immunity (PTI) is classically associated with an extracellular respiratory burst generated by plasma membrane-localized NADPH oxidases (RBOHs). (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Pattern-triggered immunity (PTI) is classically associated with an extracellular respiratory burst generated by plasma membrane-localized NADPH oxidases (RBOHs). Here, we identify an ancient RBOH-independent intracellular respiratory burst driven by central carbon metabolism. Using in vivo biosensors, we demonstrate that receptor activation rapidly triggers sugar catabolism via glycolysis, shifting the NAD pool toward its reduced state. This redox pressure drives a burst in mitochondrial respiratory flux and oxygen consumption. Consequent mitochondrial reactive oxygen species (ROS) production activates ANAC017-mediated retrograde signaling to induce broader PTI gene expression. This intracellular respiratory burst represents a conserved early hallmark of immunity across land plants and links cellular carbon status to immune activation. It reveals functional parallels between plant immune metabolism and metabolic reprogramming during mammalian immune-cell activation.

</details>

### [Comparative Analysis of Orthologous ANK-NLR-WRKY Proteins in Wheat Species: Evolutionary Divergence and Structural Characteristics](https://www.biorxiv.org/content/10.64898/2026.11.18.767528v1)
*Venter, E.; Mkhize, N. S.* · `plant biology` · bioRxiv doi:10.64898/2026.11.18.767528 v1 · relevance 0.08

- **In one sentence**: The plant nucleotide-binding leucine-rich repeat (NLR) immune receptors are known to play a crucial role in plant host defence against a variety of biotic stresses. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

The plant nucleotide-binding leucine-rich repeat (NLR) immune receptors are known to play a crucial role in plant host defence against a variety of biotic stresses. Several NLR proteins contain integrated domains (NLR-ID) like ankyrin (ANK) and WRKY transcription factor domains and are important evolutionary adaptations in plant immunity. They are responsible for the perception of effector molecules from invading pathogens and pests and subsequent activation of plant immune responses. However, the functional roles these ANK-NLR-WRKY proteins play in wheat (Triticum aestivum) against various pathogens and pests remain poorly understood. Computational tools employed for comparative sequence and phylogenetic analyses revealed that TaAdnr1 is highly conserved across diploid (T. urartu), tetraploid (T. dicoccoides), and hexaploid (T. aestivum) wheat species, including its well characterised orthologue YrU1 from T. urartu. Three-dimensional (3D) protein structural modelling using AlphaFold2 supported strong conservation in the multiple domains of these NLR orthologues, more specifically within the integrated WRKY domain. This conservation may suggest a strong evolutionary maintenance of TaADNR1. Furthermore, this may also suggest TaADNR1 reflects specificity in effector recognition and regulation. Therefore, the integration of functional genomics studies, sequence analysis, evolutionary analysis and structural modelling possesses the potential to provide new insights into the pleiotropic roles of integrated domain NLRs in wheat.

</details>

## Bioengineering and synthetic biology

### [Quantification of cannabidiolic acid in Cannabis sativa using a two-component allosteric protein biosensor](https://www.biorxiv.org/content/10.64898/2026.11.17.767439v1)
*Guo, Z.; Luna-Flores, C.; Thomson, R. E. S. et al.* · `synthetic biology` · bioRxiv doi:10.64898/2026.11.17.767439 v1 · relevance 0.12

- **In one sentence**: Cannabidiol (CBD) is an important medicinal cannabinoid which accumulates in the Cannabis sativa plant as the precursor cannabidiolic acid (CBDA). (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Cannabidiol (CBD) is an important medicinal cannabinoid which accumulates in the Cannabis sativa plant as the precursor cannabidiolic acid (CBDA). Measurement of CBDA levels is important for crop valuation, harvest optimisation, and quality control. However, its quantification typically requires laboratory-based analytical methods that are not readily deployable at the point of need. Here, we report the development of an engineered protein biosensor for selective CBDA detection based on chemically induced dimerization of engineered nanobody domains. Here a cannabidiol-responsive nanobody pair was incorporated into a two-component beta-lactamase-based biosensor architecture, such that ligand binding ultimately results in reconstitution of beta-lactamase activity quantified in a simple colorimetric assay. The resulting sensor displayed high affinity for CBD (KD = 1.9 +/- 0.2 nM) and CBDA (KD = 32 +/- 4 nM). Structure analysis informed a single substitution mutation of ligand-binding nanobody to shift its selectivity in favour of CBDA. This minimal modification inverted sensor specificity, generating a CBDA-selective biosensor that showed no detectable activation either by CBD or the immediate biosynthetic precursor, cannabigerolic acid (CBGA). The engineered sensor exhibited nanomolar affinity for CBDA (KD = 21 +/- 2.4 nM), an 8.4-fold dynamic range, and a limit of detection of 0.5 nM. Sensor performance was validated using crude extracts from CBDA-producing biomass and achieved 95.6% agreement with LCMS-based quantification.

</details>

### [Biochemical selection on conserved glycans yield a cross-species AAV capsid for efficient panretinal intravitreal delivery](https://www.biorxiv.org/content/10.64898/2026.11.17.767272v1)
*Wang, J.-H.; Cui, M.; Zhao, W. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.17.767272 v1 · relevance 0.09

- **In one sentence**: Inherited retinal diseases are leading candidates for gene therapy, but photoreceptor-directed adeno-associated virus (AAV) vectors still require subretinal injection, which treats only part of the retina and carries surgical risk. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Inherited retinal diseases are leading candidates for gene therapy, but photoreceptor-directed adeno-associated virus (AAV) vectors still require subretinal injection, which treats only part of the retina and carries surgical risk. Intravitreal delivery is simple and panretinal, yet inner-retinal barriers block most capsids, and capsids selected in one species rarely translate. Mapping retinal glycans across seven mammals, we found heparan sulfate (HS) marking the inner limiting membrane and terminal N-acetylglucosamine (GlcNAc) enriched on photoreceptor segments. These invariants defined a two-part design principle, attenuated HS binding with strong terminal GlcNAc engagement, implemented as a sequential in vitro selection, Conserved Receptor-Selection Technology (CReST). Its lead GlcNAc-selected capsid, AAV2.IvtB, increased retinal transgene expression 6.5-fold over AAV2.7m8 in mice and photoreceptor transduction 2.5-fold in pigs, acting through terminal GlcNAc engagement. It partially preserved photoreceptors in rd10 mice and suppressed laser-induced choroidal neovascularization. CReST is a receptor-guided, animal-free route to capsids with a defined, conserved mechanism.

</details>

## Mathematical biology (arXiv)

⚠️ Fetch failed: HTTP Error 429: Unknown Error

## Epidemiology

### [Perinatal suicide risk factors: A network analysis](https://www.medrxiv.org/content/10.64898/2026.11.18.26368387v1)
*Zivin, K.; Zhong, C.; Kahsay, E. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368387 v1 · relevance 0.11

- **In one sentence**: Purpose Suicide during pregnancy or after birth (the perinatal period) represents a leading, preventable cause of United States maternal deaths. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Purpose Suicide during pregnancy or after birth (the perinatal period) represents a leading, preventable cause of United States maternal deaths. This study aimed to understand the complex relationship between perinatal status and life circumstances among perinatal suicide decedents in the United States and generate insights regarding suicide risk. Methods This cross-sectional study used decedent data from the 2003-2023 National Violent Death Reporting System suicide mortality registry (N=20,217). We applied psychometric network analysis using 18 binary life circumstances indicators representing four domains: relationships, health, socioeconomic status, and risk factors for suicide. We generated two networks for the overall sample and perinatal sample and assessed network structure, bridge centralities, and stability. Results The analytic sample included 1,297 perinatal and 18,920 non-perinatal decedents. The network of the overall sample was stable. Perinatal status did not appear at the center of the network but connected primarily with intimate partner problems. The network of the perinatal sample was modestly stable. Postpartum status was not at the center of the network but connected to depressed mood and mental health diagnoses. In both networks, depressed mood had the highest bridge betweenness, and there was a consistent link between physical health domains and socioeconomic domains. Conclusion Suicide prevention strategies targeting childbearing-aged women should incorporate factors beyond pregnancy, including physical health, intimate partner relationships, and socioeconomic challenges.

</details>

### [Elevated maternal hemoglobin levels during pregnancy are associated with autism spectrum disorder in the offspring: A population-based cohort study](https://www.medrxiv.org/content/10.64898/2026.11.15.26368133v1)
*Dichter, A.; Tzoref, A.; Meiri, G. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.15.26368133 v1 · relevance 0.08

- **In one sentence**: Background Autism spectrum disorder (ASD) is an increasingly prevalent neurodevelopmental condition with multifactorial origins, including potential prenatal environmental contributions. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Background Autism spectrum disorder (ASD) is an increasingly prevalent neurodevelopmental condition with multifactorial origins, including potential prenatal environmental contributions. Maternal anemia (decreased hemoglobin [Hb] levels) has long been associated with adverse offspring neurodevelopmental outcomes. Yet, evidence regarding elevated levels of antenatal hemoglobin levels, in relation to ASD risk remains limited. This study evaluated the association between maternal Hb levels during pregnancy and the risk of ASD diagnosis in offspring. Methods This large-scale, population-based retrospective cohort study used electronic health records from births of members of Clalit Health Services (CHS), the largest health maintenance organization in Israel, between 2011 and 2021. The study included 303,234 singleton live births to Jewish mothers who had at least one measured prenatal Hb value and were CHS members. Exclusion criteria were children with known genetic disorders and births <25 weeks of gestation. Maternal Hb, and red blood cells (RBC) levels during the first and second trimesters were categorized as low (<2.5th percentile), normal (reference), or high (>97.5th percentile). The main outcome was a diagnosis of ASD in the offspring, as recorded in medical files. Statistical analyses adjusted for maternal age, socioeconomic status, gestational diabetes, BMI, and other clinical and demographic factors. Results Among the 303,234 births, 8,106 (2.7%) children were diagnosed with ASD. High maternal Hb levels were associated with elevated odds of ASD diagnosis (aOR=1.22; 95% CI=1.08:1.37), with the strongest association observed for first-trimester measurements (aOR=1.31; 95% CI=1.14-1.49). This association persisted in the sibling-matched analysis (aOR=1.64; 95% CI=1.08-2.47) and was not modified by maternal RBC levels, suggesting that it was not explained by familial factors or RBC counts. The main limitations of this study include the lack of available data on maternal smoking, and the absence of detailed information on maternal nutritional status. Conclusions These findings suggest that elevated antenatal Hb levels may be relevant to offspring neurodevelopment. Further studies are needed to replicate these findings and clarify the biological mechanisms underlying this association.

</details>

## Infectious diseases

### [The effect of smallpox vaccination: unique insights gained from Danish post-honeymoon epidemics 200 years ago](https://www.medrxiv.org/content/10.64898/2026.11.16.26368180v1)
*Eilersen, A.; Poder, S.; Goedknegt, M. J. F. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.16.26368180 v1 · relevance 0.10

- **In one sentence**: BackgroundHistorically, the Variola virus caused deadly smallpox epidemics in children. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

BackgroundHistorically, the Variola virus caused deadly smallpox epidemics in children. In Copenhagen, transmission was halted by 1810 when [~]90% of children were vaccinated following the introduction of a mandatory single-dose vaccine program. A 14-year honeymoon period followed, but in 1824 smallpox re-emerged as a milder disease of adults. We set out to study smallpox epidemics between 1824 and 1835 when all smallpox patients in Copenhagen were quarantined. MethodWe analyze data from 3795 smallpox patients reported by the treating physicians between 1824 and 1835. The data include age, vaccination status, and outcome. We estimate age-specific case fatality ratios (CFR) and vaccine effectiveness (VE) against mortality. FindingsFor the four outbreaks while quarantine was mandatory (1824-1834), the CFR was [~]1% among the vaccinated and [~]25% among the unvaccinated, corresponding to a VE of [~]95%. For the fifth outbreak in 1835, we found that CFR was low among the vaccinated but increased with age, which is evidence of waning vaccine protection. Almost no cases were over 40 years of age, suggesting lifelong immunity from smallpox infection. InterpretationAs the unvaccinated CFR was high and comparable to the pre-vaccine era, the milder post-honeymoon smallpox disease cannot be explained by genetic changes in the virus. Rather, high coverage with an effective vaccine combined with waning vaccine protection in adulthood explains the changing face of smallpox. We demonstrates how high vaccine coverage can disguise an outbreak of highly pathogenic smallpox as the milder Variola minor.

</details>

### [Upper respiratory microbiome and host immune signatures associated with SARS-CoV-2 susceptibility and illness in a human challenge model](https://www.medrxiv.org/content/10.64898/2026.11.16.26368138v1)
*Hurst, J. H.; Wanchai, V.; Shi, P. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.16.26368138 v1 · relevance 0.08

- **In one sentence**: In a controlled SARS-CoV-2 human challenge study of 34 healthy young adults, the authors compare nasal and throat microbiome composition and host gene expression before and after inoculation to identify pre-exposure signatures associated with infection, symptoms, and viral load.
- **In plain words**: Some people catch a respiratory virus after exposure while others do not, and the reasons are not well understood. Researchers deliberately exposed healthy volunteers to SARS-CoV-2 and sampled their noses and throats for two weeks, both before and after exposure. They found that people who later became infected already differed in their nasal immune activity and in the mix of bacteria living in their noses before any virus was given.
- **Why it matters**: Because the study records people before they are exposed, it can look for early markers of susceptibility rather than only describing infection after the fact. The links it reports are correlations among many measured features, so they point to possible microbe-immune interactions worth testing rather than establishing a cause; the abstract alone does not show how strong or reproducible these links are.
- **Background needed**: ['Microbiome: the community of bacteria and other microbes living on body surfaces; here, the nose and throat.', 'Commensal bacteria: harmless microbes that normally live in the body and can influence local immunity.', 'Human challenge study: volunteers are deliberately infected under controlled conditions so that infection timing is known.', 'Gene expression: measuring how actively genes are switched on in a tissue sample, used here as a readout of immune activity.', 'Interferon response: an early antiviral alarm signal produced by cells when a virus is detected.', 'Neutrophils: a type of white blood cell that responds quickly to infection and inflammation.', "Relative abundance: the share of a sample's microbes that belong to a given species, not an absolute count.", 'Viral load: the amount of virus detected in a sample, often used as a rough measure of infection intensity.'] · level: research-level

<details><summary>Original abstract</summary>

The upper respiratory tract (URT) microbiome modulates the local mucosal immune environment, with potential implications for respiratory viral infection susceptibility and outcomes. We leveraged a first-in-human SARS-CoV-2 challenge study in 34 healthy young adults, 18 of whom became infected, to characterize host gene expression and microbiome composition and dynamics in nasal and throat samples collected before viral inoculation and over the subsequent 14 days. Compared with participants who remained uninfected, participants who became infected had elevated baseline nasal expression of gene modules related to interferon, innate inflammatory, and neutrophil responses, as well as a delayed transcriptional response to viral challenge. Baseline nasal microbiome composition differed modestly by subsequent infection status, with lower relative abundances of Corynebacterium accolens and higher abundances of Dolosigranulum pigrum and Staphylococcus aureus among participants who became infected. Integrated analyses of microbiome and host gene expression data identified coordinated networks of microbiome features and host immune modules that distinguished infected from uninfected participants, including prior to inoculation. Notably, immune modules associated with infection susceptibility were positively correlated with S. aureus abundance and negatively correlated with the abundances of common nasal commensals, Corynebacterium spp. and Staphylococcus epidermidis, linking altered nasal microbiome community structure with the heightened inflammatory state associated with infection susceptibility. Symptom burden and viral load were similarly linked to distinct networks of microbiome and host gene expression features within nasal samples. Taken together, these findings highlight potential microbiome-host interactions within the nasal mucosa that may contribute to differences in respiratory viral infection outcomes.

</details>

## Public and global health

### [Does educational attainment change the association between meat intake and obesity? A case-study from urban Brazil.](https://www.medrxiv.org/content/10.64898/2026.11.16.26368245v1)
*Laurentino, J.; Palmeira, P.; Levasseur, P.* · `health economics` · medRxiv doi:10.64898/2026.11.16.26368245 v1 · relevance 0.10

- **In one sentence**: Brazil is one of the higher meat producer and consumer worldwide. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Brazil is one of the higher meat producer and consumer worldwide. Recently, the sustainability of the meat market is questioned on regard to its high contribution to climate change and public health concerns such as obesity. Hence, further public policies are likely to regulate the meat market and simultaneously reduce meat production and consumption. However, in the context of middle-income countries marked by strong inequalities such as Brazil, the nutritional effect of such market regulation is uncertain. Indeed, one can hypothesize that meat intake plays a protective role against poor nutritious food intake and weight gain among underprivileged settings. To test this hypothesis, this study analyzes household cross-sectional yearly surveys collected from 2018 to 2023 in the 27 Brazilian State capitals. As expected, multivariate estimates show education-specific associations between meat intake and obesity. Among the most educated individuals, declaring not consuming any meat the previous day before the survey is associated with lower body mass index (BMI) and obesity risk, as observed in previous epidemiological studies. By contrast, declaring consuming meat the previous day before the survey appears to be protective against weight gain among poorly educated individuals. We also observe education-specific meat substitution behaviors that help explain these findings. In facts, meat is more likely to be replaced by sweets and ready-to-eat meals among poorly educated individuals compared to more educated ones. We conclude that, everything being equals, meat market regulation policy might worsen public health concerns for under-privileged individuals. Important investments in the education sector and anti-poverty programs are thus needed to limit the raise of nutritional inequalities.

</details>

### [Determinants of Tuberculosis Diagnosis Delays among Patients Attending Public Health Facility of Metekel Zone, Northwest Ethiopia, 2024 unmatched Case-Control Study](https://www.medrxiv.org/content/10.64898/2026.11.17.26368197v1)
*Denat, A. T.; Burusso, A. B.; Yimenu, T. N.* · `public and global health` · medRxiv doi:10.64898/2026.11.17.26368197 v1 · relevance 0.09

- **In one sentence**: Background: Tuberculosis Diagnosis delays among tuberculosis patients can worsen infection transmission, disease severity, and mortality risk. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Background: Tuberculosis Diagnosis delays among tuberculosis patients can worsen infection transmission, disease severity, and mortality risk. Identifying factors influencing delays is crucial due to its persistence across healthcare levels and communities. The study identify determinants of tuberculosis diagnosis delay among patients attending public health facility of Metekel zone, Northwest Ethiopia:2023 Methods: An unmatched case-control study was conducted in Metekel zone health facilities from March to April 2023, involving 210 tuberculosis patients (103 cases, 107 controls) selected through systematic sampling. Data collected through structured questionnaires and STATA used for analysis, including bi-variable and multi-variable logistic regressions. Variables with p-value < 0.25 in bi-variable analysis were included in the final model after checking model fitness and multicollinearity. Results: Overall, 210 tuberculosis patients were included in the study. The following independent variables were associated diagnosis delay of tuberculosis: TB patients who travel greater than 10km (AOR: 2.941, (95 % CI: 1.509, 5.731); TB patients who are living at rural area (AOR: 4.135, 95 % CI :1.759, 9.723); TB patients who prior visit in holly-water and traditional medicine [AOR: 2.978, (95% CI: 1.292, 6.863); poor knowledge about TB [AOR: 2.826, (95% CI: 1.404, 5.687)]. Conclusion: Tuberculosis diagnosis delay is a major challenge to eliminate tuberculosis by breaking the chain of transmission. This study can be attributed to factors including place of residence being rural, poor knowledge about tuberculosis, non-health facility initial actions upon symptom onset, and far distance to health institutions. Recognizing these determinants helps in identifying and addressing barriers inhibiting early diagnosis, potentially improving healthcare access and promoting more timely diagnosis and treatment for tuberculosis patients.

</details>

## Psychiatry and neurology

### [Microstructure predicts cognition following deep brain stimulation in Parkinson's disease](https://www.medrxiv.org/content/10.64898/2026.11.19.26368410v1)
*Chen, L.; Witt, L.; Calvano, A. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368410 v1 · relevance 0.12

- **In one sentence**: Deep brain stimulation of the subthalamic nucleus (STN-DBS) effectively treats motor and non-motor symptoms in advanced Parkinson's disease (PD). (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Deep brain stimulation of the subthalamic nucleus (STN-DBS) effectively treats motor and non-motor symptoms in advanced Parkinson's disease (PD). However, 15-20 % of patients experience postoperative cognitive decline and identifying preoperative markers remains an unmet clinical need. In this prospective open-label study, we employed NODDI-DTI to investigate whether cerebral microstructure predicts cognitive outcomes following STN-DBS. Forty PD patients underwent diffusion MRI and neuropsychological assessments at preoperative baseline and 6-month follow-up. A whole-brain voxel-wise analysis related microstructural metrics to postoperative cognitive change. Compromised microstructure within three large-scale networks - the frontoparietal/attentional, default mode/limbic, and ventral associative/visual networks - was associated with greater postoperative cognitive decline. These findings suggest that both disease-related network degeneration and stimulation acting on compromised circuits may contribute to postoperative cognitive decline. In conclusion, preoperative evaluation of microstructural integrity may help identify patients at risk for postoperative cognitive decline, supporting individualised counselling and targeted behavioural monitoring after STN-DBS.

</details>

### [Plasma neurodegeneration biomarkers and clinical progression in early sporadic Parkinson's disease](https://www.medrxiv.org/content/10.64898/2026.11.18.26368420v1)
*Tropea, T. F.; Coughlin, D. G.; Brooker, S. M. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.18.26368420 v1 · relevance 0.11

- **In one sentence**: Objectives: Plasma neurodegeneration biomarkers offer an opportunity to characterize Parkinson's disease (PD) biology. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Objectives: Plasma neurodegeneration biomarkers offer an opportunity to characterize Parkinson's disease (PD) biology. The objective of this study was to investigate such biomarkers in deeply-phenotyped participants in Parkinson's Precision Medicine Initiative (PPMI). Methods: Baseline plasma samples from early (<2 years since diagnosis) sporadic PD participants with a positive CSF alpha-synuclein seed amplification assay (aSyn-SAA) and healthy controls (HC) with a negative aSyn-SAA test were utilized. Plasma P-tau217 (Roche Diagnostics), neurofilament light chain (NfL, Quanterix), glial fibrillary acidic protein (GFAP, Quanterix), and (PD only) amyloid-beta (A{beta}) levels (40 and 42, C2N Diagnostics) were measured. Clinical features at baseline and over up to 11 years were compared across biomarker tertiles in models controlling for age, sex, and baseline outcome variable. Results: The cohort was 97 HC and 523 PD and participants. Median [IQR] biomarker values (pg/mL) for HC and PD were P-tau217: 0.14 [0.06 -0.75], 0.15 [0.06 -0.90]; NfL: 10.6 [3.13 -49.85], 12.26 [3.77-62.67]; GFAP: 66.56 [19.75 -403.48], 87.19 [14.55 -531.82]; and in PD A{beta}40: 391.32 [209.95 -538.38]; A{beta}42: 42.74[27.75 -68.55]. No biomarkers differed between HC and PD. In PD, biomarkers were associated with age. In PD only, higher baseline levels of P-tau217 and NfL were associated with greater hazards of a worse cognitive and balance outcome. P-tau217, NfL, and GFAP levels were associated with change in cognitive score over time. Interpretation: Plasma P-tau217, NfL and GFAP levels in early, sporadic PD with confirmed synucleinopathy predict future cognitive and functional impairment, and these findings can inform clinical research design and clinical care.

</details>

## Oncology

### [Transcriptomic and Genomic Sequencing of South African Colorectal Cancer Patients Reveal Population-Specific Insights and Variants](https://www.medrxiv.org/content/10.64898/2026.11.19.26368287v1)
*Kader, Z.; Abdulla, N.; Bebington, B. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.19.26368287 v1 · relevance 0.07

- **In one sentence**: Colorectal cancer (CRC) genomic studies have largely underrepresented African populations, limiting understanding of disease biology in these groups. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Colorectal cancer (CRC) genomic studies have largely underrepresented African populations, limiting understanding of disease biology in these groups. This study addressed this gap by generating integrated genomic and transcriptomic data from South African (SA) CRC patients, establishing a foundation for future cancer studies. Bulk RNA sequencing of 32 samples identified several differentially expressed genes between tumour and normal samples, with AGAP3, AMPD2, ANKRD10, and SALL4 showing strong diagnostic performance (average sensitivity 99.9%, specificity 94.22%, PPV 99.9%, NPV 89.5%). SALL4 performed best and was validated using TCGA data and Kaplan-Meier survival analysis. Consensus Molecular Subtype classification revealed a distinct distribution, with enrichment of metabolic (CMS3, 30%) and mesenchymal (CMS4, 30%) subtypes and under-representation of canonical CMS2 (21%). APC mutation rates were lower than in European patients (~55% vs ~75%). Functional analysis identified inflammatory pathways as primary drivers of carcinogenesis, with viral influences exacerbating the inflammatory tumour microenvironment. Altered neural pathways in tumour samples suggested a consequential gut-brain axis loop as cancer infiltrates enervated tissue, an increasingly relevant field to which these data contribute. Whole-genome sequencing of 12 samples revealed pathogenic and likely pathogenic variants with transcriptomic differential expression; SMPD1, PERM1, PRRT2, and RP1 emerged as potential multi-omics markers, while novel mutations (KDM6A, C2CD2, TAF2, SLC6A16, OR5M10, PITRM1, TRIM64B, CARD11) were identified as previously unrecognised contributors to CRC progression in African samples. These findings expand genomic resources for African cancer research and provide new insights into the molecular landscape and tumourigenesis mechanisms of CRC in SA patients, supporting the development of population-specific precision oncology approaches.

</details>

### [LCatlas: A Point-Of-Care Tool for Predicting Immunotherapy Outcomes in Non-Small Cell Lung Cancer](https://www.medrxiv.org/content/10.64898/2026.11.18.26368446v1)
*Park, S. Y.; Leyba, A.; Yeung, W. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.18.26368446 v1 · relevance 0.07

- **In one sentence**: Non-small cell lung cancer (NSCLC) remains a leading cause of cancer mortality, with a minority of patients experiencing durable responses to first-line immune checkpoint inhibitors (ICIs). (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Non-small cell lung cancer (NSCLC) remains a leading cause of cancer mortality, with a minority of patients experiencing durable responses to first-line immune checkpoint inhibitors (ICIs). Currently, there are no easily accessible tools to predict clinical benefit to first-line immunotherapy. To address this gap, we developed LCatlas (https://www.lcatlas.org), a point-of-care web application designed to predict immunotherapy outcomes and inform evidence-based treatment decisions. Using data from 79 NSCLC patients receiving first-line immunotherapy, we extracted demographic, clinical, and molecular features from electronic medical records and compared three independent approaches, statistical model (logistic regression), machine learning (XGboost), and AI model (TabTransformer) to identify the most effective predictor. LCatlas accepts nine variables, gender, smoking history, bone/pleura/liver metastasis, PDL1 tumor staining, albumin level, hemoglobin level, lymphocyte count, neutrophil count, and platelet count, to predict responses to both immunotherapy and immunotherapy plus chemotherapy. LCatlas cross-validation yielded an area under the curve (AUC) of 79% [72% - 85%], with sensitivity of 87% [72% - 95%] and specificity of 78% [64% - 89%], outperforming previous studies including high-volume data-driven deep-learning approaches. In a validation cohort consisting of 28 individuals, it demonstrated a prediction accuracy of 82%. LCatlas may serve as a valuable point-of-care tool by identifying patients likely to experience extended immunotherapy or combination therapy using readily available medical data. Its evidence-based approach can optimize personalized treatment planning and thereby promote quality and safety of care.

</details>

## Health informatics and medical AI

### [The ITE-Transformer: A pre-trained foundation model for predicting individualized treatment effects from electronic health records](https://www.medrxiv.org/content/10.64898/2026.11.19.26368479v1)
*Arceri, C.; Angelis, E.; Heesen, P. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368479 v1 · relevance 0.14

- **In one sentence**: Transformer-based foundation models have shown strong potential for modeling longitudinal electronic health records (EHRs), yet existing models focus primarily on risk prediction rather than treatment effect estimation, which limits evidence generation. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Transformer-based foundation models have shown strong potential for modeling longitudinal electronic health records (EHRs), yet existing models focus primarily on risk prediction rather than treatment effect estimation, which limits evidence generation. Here, we introduce the ITE-Transformer, a transformer-based framework that combines self-supervised representation learning from longitudinal patient trajectories with doubly robust causal machine learning for predicting individualized treatment effects (ITEs). As a result, our ITE-Transformer allows to study counterfactual questions of how an individual patient's outcome may differ under alternative treatment strategies. The ITE-Transformer learns temporally contextualized representations of patients' diagnosis and medication histories and subsequently uses these representations to predict treatment assignment, treatment-specific outcome risks, and patient-specific ITEs. The ITE-Transformer is trained using structured EHR data from ~350,000 participants in the All of Us Research Program and evaluated in two clinically different comparative-effectiveness tasks: (i) GLP-1 receptor agonists versus DPP-4 inhibitors among patients with type 2 diabetes, with major adverse cardiovascular events as the outcome, and (ii) immunotherapy versus chemotherapy in a pan-cancer cohort, with all-cause mortality as the outcome. Across both applications, the ITE-Transformer improves the discrimination and calibration of treatment assignment and outcome models compared with existing tabular machine learning approaches and an otherwise identical transformer trained without self-supervised pre-training. The ITE-Transformer further identifies substantial heterogeneity in predicted ITEs and yields interpretable patterns of treatment response associated with patients' diagnoses, medication histories, and comorbidities. Together, our work demonstrates how clinical foundation models can be developed for analyzing heterogeneity in treatment effects and thus support real-world evidence generation.

</details>

### [The Shrinking Grace Period and the Downsizing of Ransomware Victims: Exploitation Timelines and Breach Size Among US Health Care Providers, 2016-2026](https://www.medrxiv.org/content/10.64898/2026.11.17.26368300v1)
*Nakagawa, R.; Yasuhara, Y.; Shimoyama, A. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.17.26368300 v1 · relevance 0.11

- **In one sentence**: Objectives: To examine how quickly software vulnerabilities are exploited after public disclosure, and whether hacking breaches at US health care providers changed in size after 2021, a period in which earlier studies had found attacks concentrating on large organizations. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Objectives: To examine how quickly software vulnerabilities are exploited after public disclosure, and whether hacking breaches at US health care providers changed in size after 2021, a period in which earlier studies had found attacks concentrating on large organizations. Methods: Retrospective analysis of public data. We linked the CISA Known Exploited Vulnerabilities catalog (1,748 entries) with CVE publication dates to measure time to confirmed exploitation by half-year of publication (2021-2025). We also analyzed 8,029 breach reports submitted to the HHS Office for Civil Rights, focusing on hacking/IT incidents at health care providers. Results: Median time to confirmed exploitation was 24 days for vulnerabilities published from late 2021 to mid 2022, 0 days for those published in the second half of 2022, and 6 days in 2023-2025, with no further shortening across 2023-2025 (P = .40). About a quarter were exploited on or before the day of disclosure. Among provider hacking breaches, the share affecting fewer than 5,000 people fell from 42% in 2016 to 32% in 2022 (trend P = .004) and rose to 46% in 2025 (P < .001). Conclusions: The window between disclosure and exploitation had narrowed to about a week before generative AI was widely available. After 2022, breaches moved toward smaller events, reversing the earlier concentration on large organizations. Defenses that depend on patching speed will not protect small providers.

</details>

## Econometrics and applied economics

⚠️ Fetch failed: HTTP Error 429: Unknown Error

## Economic theory

⚠️ Fetch failed: HTTP Error 429: Unknown Error

## Game theory and algorithmic economics

⚠️ Fetch failed: HTTP Error 429: Unknown Error

## Mathematical finance

⚠️ Fetch failed: HTTP Error 429: Unknown Error

## Financial markets

### [Trading Before a Committed Rebalance](https://arxiv.org/abs/2611.25762v1)
*Khizar Qureshi* · `q-fin.TR` · arXiv:2611.25762v1 · relevance 0.07

- **In one sentence**: An institution must complete a portfolio adjustment, but traders who prepare inventory for it can choose whether to participate. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

An institution must complete a portfolio adjustment, but traders who prepare inventory for it can choose whether to participate. We study how public forecasts affect the institution's cost in a Bayesian execution game with optional activation, transient impact, and uniform-price terminal completion. The curvature of equilibrium cost as a function of the posterior target mean determines the value of information. In the scalar model, information benefits every fixed participation roster. Optional supply can reverse this ranking at entry, at full participation, and in a smooth interior with lognormal activation costs. For centered scalar targets, information weakly lowers cost relative to no information, strictly when the posterior mean is nonzero with positive probability. Centered Gaussian precision gains are always beneficial. An exact symmetric finite-population equilibrium identifies how information resolution and individual strategic size interact near entry. A portfolio extension gives a matrix criterion for the fixed-roster ranking, which can fail under general cross-impact. Even with isotropic execution, shared activation allows equally accurate signals about target magnitude and composition to have opposite execution values under one unchanged prior. Intraday ETF price data is used to characterize target uncertainty and trading conditions without identifying activation or institutional costs.

</details>

### [Bond yield dynamics: a multi-country multi-horizon string model](https://arxiv.org/abs/2611.26466v1)
*Paul Ruelloux* · `q-fin.ST` · arXiv:2611.26466v1 · relevance 0.06

- **In one sentence**: This article extends the forward rate curve model of Baaquie and Bouchaud (2004) and Le Coz and Bouchaud (2024) to the multi-country setting of government bond markets. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

This article extends the forward rate curve model of Baaquie and Bouchaud (2004) and Le Coz and Bouchaud (2024) to the multi-country setting of government bond markets. Cross-country blocks of correlation matrices of realized yield changes are found to display significant asymmetry between maturities. In the framework of the proposed model, this amounts to give to each country an idiosyncratic time scale. Each time scale describes how the perceived time between future dates depends on the dates themselves. The differences between these time scales structure the interactions between curves and reproduce the characteristic asymmetry of cross-country correlation matrices. The proposed model captures the full set of cross-curve correlations simultaneously at both daily and intra-day frequencies. When calibrated on government bonds issued by nine countries of the euro-zone, the typical reconstruction error is 1.7%.

</details>

## Signal processing

### [Decision Fusion in Wireless Networks: A Tutorial and Survey of Classical and Learning-Based Methods](https://arxiv.org/abs/2611.26442v1)
*Mohamed Abdelkader, Arafat Al-Dweik, Sobia Jangsher et al.* · `eess.SP` · arXiv:2611.26442v1 · relevance 0.10

- **In one sentence**: Decision fusion combines local decisions from distributed sensors to support reliable detection of phenomena in wireless networks. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Decision fusion combines local decisions from distributed sensors to support reliable detection of phenomena in wireless networks. The effectiveness of decision fusion depends on sensing accuracy, reporting-channel reliability, and available communications and computation resources. This article surveys decision-fusion techniques for wireless sensor networks and emerging communication systems, bringing together their theoretical foundations and practical implementation requirements. We review network architectures and hard, soft, and quantized reporting strategies, and examine statistical, learning-based, game-theoretic, and heuristic fusion approaches. Advanced fusion techniques, including relay-aware combining, link-adaptive regeneration, branch selection, and likelihood approximations, are discussed with emphasis on their assumptions, information requirements, and limitations. The survey examines tradeoffs among detection performance, computational complexity, communications overhead, energy consumption, and latency. The tradeoffs are considered across representative sensing applications and emerging technologies, including massive machine-type communication, ultra-reliable low-latency communication, uncrewed aerial vehicle-assisted networks, and the massive Internet of Things. The reviewed literature highlights the importance of jointly considering sensing quality, reporting reliability, and fusion processing when selecting a suitable strategy. Finally, we identify research directions in resource-aware optimization, uncertainty calibration, and robust learning-based fusion under heterogeneous data, missing reports, and changing wireless conditions. Particular attention is given to convergence, generalization, and the costs of training and inference.

</details>

### [Channel-Aware Codebook Design for Task-Oriented Token Communication Over Wireless Networks](https://arxiv.org/abs/2611.26038v1)
*Chenliang Wu, Zhicheng Liu, Zhouxiang Zhao et al.* · `eess.SP` · arXiv:2611.26038v1 · relevance 0.08

- **In one sentence**: This paper investigates the adaptive codebook design for task-oriented token communication over wireless networks with dynamic channels. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

This paper investigates the adaptive codebook design for task-oriented token communication over wireless networks with dynamic channels. This paper proposes the channel-aware codebook (CAC), a joint channel- and reconstruction-driven framework that reorders the labels of a frozen 14-bit VQGAN codebook. In the considered framework, a balanced geometric partition forms prefix groups, a prefix bijection places the groups on the label hypercube, and bijective suffix assignments place the codewords within each group. The problem is formulated to minimize the expected full-image perceptual distortion of the frozen decoder under a binary symmetric channel, averaged over a design set of bit error rates (BERs) and retaining simultaneous token errors. An offline algorithm alternates prefix and suffix exchanges and screens and confirms candidates on paired batches under a fixed decoder-evaluation budget. The assignment preserves the error-free reconstruction and the payload and deploys as static lookup tables without retraining. Under the binary symmetric channel at BER $0.01$, it reduces LPIPS by $12.3\%$ and improves COCO AP by $14.1\%$ ($1.72$ points) relative to the native labels, and it lowers LPIPS by a further $4.5\%$ relative to a related assignment adaptation at the same payload.

</details>

## Audio and speech

### [Joint Language Modeling for In-the-Wild Speech-Scene Generation with Distinct Token Representations](https://arxiv.org/abs/2611.25503v1)
*Semin Kim, Ju Yeon Kang, Sunghwan Ahn et al.* · `eess.AS` · arXiv:2611.25503v1 · relevance 0.10

- **In one sentence**: The paper proposes an LLM-based system that jointly generates separate speech and environmental-sound token streams, extracted from mixed recordings by a source-aware neural audio codec, so that speech and background audio form one coherent acoustic scene, including for real-world recordings without isolated sources.
- **In plain words**: The task is to produce a realistic audio scene in which someone speaks clearly and the surrounding sounds, such as traffic or a room's ambience, fit with that setting. The authors treat speech and background sound as two separate sequences of compressed audio codes and have a language model generate both, interleaved, from a text description of the scene and the words to be spoken. Because the training data comes directly from mixed real recordings rather than artificially layered clips, the approach can be adapted to messy, in-the-wild audio; the abstract reports gains in intelligibility, scene relevance and audio quality over existing methods, but gives no specific figures here.
- **Why it matters**: Generating speech and its environment together, rather than as a simulated mix, could matter for audio content creation, dubbing, and training data for speech systems that must cope with noisy settings. The abstract does not show how large the improvements are or how well they hold beyond the authors' tests, so the practical significance is not yet clear.
- **Background needed**: ['Neural audio codec: a model that compresses audio into a short sequence of discrete tokens and can reconstruct sound from them.', 'Language model generation over tokens: large language models can be trained to predict audio tokens, as they predict words in text.', 'Interleaved generation: producing two token streams alternately, so each can take the other into account as it is built.', 'Speech-scene generation: creating a full soundscape with clear speech plus background sounds that match a scene description.', 'Simulated versus in-the-wild data: simulated scenes mix separately recorded sources, while in-the-wild recordings are natural and cannot be cleanly separated, which is why extracting sources from mixtures matters.', 'Intelligibility and scene relevance: standard goals in evaluating generated speech (can it be understood) and generated scenes (do they match the description).'] · level: research-level

<details><summary>Original abstract</summary>

Speech-scene generation aims to synthesize intelligible target speech together with diverse environmental sounds as a coherent acoustic scene. The task is considered challenging in two respects. Speech and environmental audio differ substantially in their semantic and acoustic characteristics, yet existing approaches typically model the complete scene using a single mixed acoustic representation. At the same time, the two sounds are closely related in real-world speech scenes, whereas conventional approaches usually rely on simulated scenes mixed from independently recorded sources. We propose a large language model (LLM)-based framework for joint modeling of distinct speech and environment token streams. A source-aware neural audio codec extracts temporally aligned speech and environment tokens from mixed audio, and a pretrained LLM generates both token streams in an interleaved fashion conditioned on the natural-language scene description and speech content. This formulation preserves source-specific representations while modeling the token streams within a shared generative context. Since both streams are extracted directly from mixed recordings, the model can also be adapted to in-the-wild speech scenes without isolated sources. Our experimental results demonstrate that the proposed framework improves speech intelligibility, scene relevance, and audio quality over existing speech-scene generation techniques, with consistent gains from real-world adaptation. We further investigate the effects of distinct token representations and interleaved generation, and analyze whether the environmental sound remains stable while speech is active and how the two streams interact.

</details>

### [UMelCodec: An Ultra-Low-Bitrate and Lightweight Mel-Domain Neural Speech Codec](https://arxiv.org/abs/2611.25569v1)
*Hui-Peng Du, Yang Ai, Zhen-Hua Ling* · `eess.AS` · arXiv:2611.25569v1 · relevance 0.06

- **In one sentence**: Ultra-low-bitrate speech coding is crucial for bandwidth-constrained communication and compact storage, but preserving intelligibility, naturalness, and fine-grained acoustic details at bitrates of only a few hundred bps remains challenging. (first sentence of the abstract; AI summaries are off)

<details><summary>Original abstract</summary>

Ultra-low-bitrate speech coding is crucial for bandwidth-constrained communication and compact storage, but preserving intelligibility, naturalness, and fine-grained acoustic details at bitrates of only a few hundred bps remains challenging. Existing purely acoustic codecs generally operate at relatively high bitrates, whereas incorporating semantic representations can reduce the bitrate, but at the cost of increased complexity. Therefore, we propose UMelCodec, a purely acoustic neural speech codec operating in the mel domain at an ultra-low bitrate of 325 bps with a lightweight architecture. UMelCodec consists of two stages. In the first mel-domain coding stage, alias-free Snake-ConvNeXt (AF-SC) encoder-decoder backbones model temporal and harmonic structures, a factorized single-codebook vector quantizer (VQ) enables ultra-low-bitrate quantization, and a multi-scale mel-spectrogram discriminator (MSMD) improves mel-spectrogram reconstruction. In the second waveform synthesis stage, a lightweight modified discrete cosine transform (MDCT)-based neural vocoder predicts the MDCT spectrum from the reconstructed mel spectrogram and recovers the waveform through inverse MDCT. Experiments on LibriTTS dataset demonstrate that UMelCodec outperforms strong baselines across most objective reconstruction metrics while maintaining competitive subjective naturalness. In terms of model complexity and inference efficiency, UMelCodec has only 19.67 M parameters, requires 1.93 G MACs, and supports real-time inference on both GPU and CPU platforms.

</details>

## Control systems

### [The Prediction-to-Decision Gap: First-Action Informativity in Data-Driven Predictive Control](https://arxiv.org/abs/2611.25319v1)
*Aihui Liu, Magnus Jansson* · `eess.SY` · arXiv:2611.25319v1 · relevance 0.16

- **In one sentence**: The paper asks whether data-compatible ARX models agree on the first input an unconstrained quadratic MPC would apply, shows that first-action agreement and multi-step prediction agreement are logically distinct, gives structural conditions for action agreement without unique identification, and approximates the action disagreement via local sensitivities and parameter covariance.
- **In plain words**: Model predictive control repeatedly plans a sequence of control inputs but only uses the first one before planning again. The authors ask whether the recorded data are enough to pin down that single first input, even when the data do not pin down the whole underlying model. They report that agreement on the first action and agreement on long-range predictions can come apart, and they offer a way to measure how much the uncertain model shifts that first action.
- **Why it matters**: It targets a gap between how well a learned model predicts the future and whether it leads to the same decision, which matters for anyone deploying data-driven controllers. The abstract does not show practical impact beyond the analytical and numerical examples it mentions, so its reach beyond ARX models with unconstrained quadratic MPC is unclear.
- **Background needed**: ['Model predictive control (MPC): at each time step, optimize a sequence of future inputs over a horizon, apply only the first, then re-optimize.', 'ARX model: a linear model that predicts the current output from past outputs and past inputs, plus exogenous (external) inputs.', 'System identification: estimating model parameters from recorded input-output data; a model is identified when the data determine its parameters uniquely.', 'Parameter covariance: a measure of how uncertain the estimated parameters are, typically from the fitting procedure.', 'Local sensitivity: how much an output (here, the first control action) changes when a parameter changes slightly, approximated by derivatives.', "Mean-squared deviation: the average of squared differences, used here to measure how far alternative models' actions stray from the fitted model's action."] · level: research-level

<details><summary>Original abstract</summary>

Model predictive control (MPC) applies only the first input of an optimized sequence before replanning. Do the available data determine this input? We define first-action informativity as agreement across data-compatible models at a fixed history and reference, with common MPC settings. For autoregressive models with exogenous inputs (ARX) and unconstrained quadratic MPC, we show that first-action agreement and prediction agreement under a fixed input sequence do not imply one another. We give structural conditions for action agreement without requiring unique model identification. When actions disagree, we quantify their mean-squared deviation from the fitted model's input under a specific parameter distribution. We approximate this measure using local sensitivities and parameter covariance. Analytical and numerical examples illustrate how model uncertainty affects predictions and actions differently. The framework evaluates model uncertainty through its effect on the first action MPC is about to apply.

</details>

### [DeoPC: Data-Enabled Output-Feedback Predictive Control for State Regulation](https://arxiv.org/abs/2611.25465v1)
*Jingyuan Li, Dawei Shi, Ling Shi* · `eess.SY` · arXiv:2611.25465v1 · relevance 0.16

- **In one sentence**: The paper proposes DeoPC, a data-driven output-feedback model predictive controller that estimates an unknown linear system's internal state from past input-output data via SVD-based subspace methods and enforces constraints, with recursive feasibility and closed-loop stability shown under persistent excitation and initialization conditions.
- **In plain words**: Engineers often need to keep a machine's hidden internal condition within safe limits, but they can only see what goes in and what comes out, and they may not have a mathematical model of the machine. This paper builds a controller that reconstructs the hidden internal state from recent input and output records and then chooses future control actions that respect limits. The abstract reports theoretical guarantees that the controller keeps working and stays stable under stated data conditions, with and without bounded measurement noise, and tests it in simulation on an unstable batch reactor.
- **Why it matters**: It addresses a practical gap: controlling a system whose internal state is hidden and whose model is unknown, using only data. The approach may matter to process industries and anyone who wants model-free control with safety constraints, though the abstract does not show how it compares with existing data-driven methods on real hardware.
- **Background needed**: ['State: the set of internal variables that together determine how a system will evolve; often not directly measured.', 'Linear system: one whose input-output behaviour can be described by linear equations.', 'Output feedback: control that uses only measured outputs, not the full internal state.', 'Model predictive control (MPC): at each step, optimise a plan over a short future horizon subject to constraints, apply the first action, then repeat.', 'Recursive feasibility: the guarantee that the optimisation problem stays solvable at every future step, so the controller never gets stuck.', "Persistent excitation: the requirement that the recorded input data is varied enough to reveal the system's behaviour.", 'Singular value decomposition (SVD): a matrix factorisation used here to extract the dominant patterns in recorded data.', 'Batch reactor: a chemical vessel processed in discrete batches; used as a test case for an unstable process.'] · level: research-level

<details><summary>Original abstract</summary>

Constrained regulation of the internal state of an unknown linear system is challenging when only input-output measurements are available online. In this work, we develop a data-enabled output-feedback predictive control (DeoPC) framework for constrained state regulation using input-output data. Specifically, a data-driven state estimate is constructed from past input-output data via a subspace-based singular value decomposition. Based on this state representation, we formulate a predictive controller that directly penalizes the state and control effort while enforcing the system constraints. Under persistent excitation and initialization conditions, we establish recursive feasibility and closed-loop stability of DeoPC in both noise-free and bounded-noise settings. In addition, we show that DeoPC can be calibrated to the physical state coordinates using a few offline state measurements, or treated as a model predictive control tuning problem when no state measurements are available. The effectiveness of DeoPC is demonstrated through simulations on an unstable batch reactor system.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 24 | 24 | 2 |
| Differential geometry | 22 | 22 | 2 |
| Partial differential equations | 37 | 37 | 2 |
| Harmonic analysis | 26 | 26 | 2 |
| Complex analysis | 6 | 6 | 2 |
| Operator algebras and spectral theory | 11 | 11 | 2 |
| Algebra | 16 | 16 | 2 |
| Representation theory | 15 | 15 | 2 |
| Number theory | 22 | 22 | 2 |
| Algebraic geometry | 23 | 23 | 2 |
| Topology | 11 | 11 | 2 |
| Dynamical systems | 18 | 18 | 2 |
| Combinatorics | 45 | 45 | 2 |
| Numerical analysis | 18 | 18 | 2 |
| Logic and foundations | 5 | 5 | 2 |
| Mathematical physics | 32 | 32 | 2 |
| Optimization and control | 31 | 31 | 2 |
| Statistics theory | 17 | 17 | 2 |
| Statistical methods and applications | 27 | 27 | 2 |
| Machine learning theory | 10 | 10 | 2 |
| Large language models | 49 | 49 | 2 |
| Computer vision | 161 | 161 | 2 |
| Reinforcement learning | 33 | 33 | 2 |
| AI safety and alignment | 44 | 44 | 2 |
| Interpretability | 28 | 28 | 2 |
| AI for mathematics | 3 | 3 | 2 |
| Robotics and embodied AI | 76 | 76 | 2 |
| Security and cryptography | 40 | 40 | 2 |
| Algorithms and complexity | 24 | 24 | 2 |
| Programming languages and formal methods | 25 | 25 | 2 |
| Systems and networking | 34 | 34 | 2 |
| Human-computer interaction | 15 | 15 | 2 |
| Information theory | 17 | 17 | 2 |
| High-energy theory and gravity | 53 | 53 | 2 |
| Statistical physics | 25 | 25 | 2 |
| Condensed matter | 38 | 38 | 2 |
| Particle physics | 51 | 51 | 2 |
| Nuclear physics | 14 | 14 | 2 |
| Quantum information and computing | 75 | 75 | 2 |
| Optics and atomic physics | 27 | 27 | 2 |
| Fluids and plasma | 26 | 26 | 2 |
| Biological physics | 4 | 4 | 1 |
| Climate, atmosphere and Earth | 5 | 5 | 2 |
| Cosmology | 25 | 25 | 2 |
| Galaxies | 20 | 20 | 2 |
| Exoplanets and planetary science | 5 | 5 | 2 |
| High-energy astrophysics | 22 | 22 | 2 |
| Stars and the Sun | 15 | 15 | 2 |
| Chemical physics | 3 | 3 | 2 |
| Materials science | 31 | 31 | 2 |
| Soft matter and polymers | 8 | 8 | 2 |
| AI for chemistry and materials | 13 | 13 | 2 |
| Biochemistry | 30 | 30 | 2 |
| Pharmacology and drug discovery | 6 | 6 | 1 |
| Computational and systems biology | 104 | 104 | 2 |
| Neuroscience | 116 | 116 | 2 |
| Genetics and genomics | 62 | 62 | 2 |
| Cell and molecular biology | 70 | 70 | 2 |
| Immunology and microbiology | 84 | 84 | 2 |
| Cancer biology | 43 | 43 | 2 |
| Ecology and evolution | 47 | 47 | 2 |
| Plant biology | 24 | 24 | 2 |
| Bioengineering and synthetic biology | 30 | 30 | 2 |
| Mathematical biology (arXiv) | 0 | 0 | 0 |
| Epidemiology | 25 | 25 | 2 |
| Infectious diseases | 8 | 8 | 2 |
| Public and global health | 15 | 15 | 2 |
| Psychiatry and neurology | 30 | 30 | 2 |
| Oncology | 7 | 7 | 2 |
| Health informatics and medical AI | 17 | 17 | 2 |
| Econometrics and applied economics | 0 | 0 | 0 |
| Economic theory | 0 | 0 | 0 |
| Game theory and algorithmic economics | 0 | 0 | 0 |
| Mathematical finance | 0 | 0 | 0 |
| Financial markets | 6 | 6 | 2 |
| Signal processing | 28 | 28 | 2 |
| Audio and speech | 6 | 6 | 2 |
| Control systems | 30 | 30 | 2 |

<!-- {% endraw %} -->
