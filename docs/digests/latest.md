# Research digest · 2026-11-26
<!-- {% raw %} -->

New papers posted from about 2026-11-25 to 2026-11-26 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models](https://arxiv.org/abs/2611.33398)** (AI safety and alignment): Robots that follow language instructions can be improved at deployment time by sampling several possible actions and letting a scoring program pick the best one. This paper shows that this strategy can backfire: when the scorer makes mistakes, picking from more candidates can favor actions that just happen to earn high scores from those errors rather than actually doing the task well. The authors tested this on 60 safety-focused robot tasks in a simulator, with ten repeated runs per task.
- **[H19 isoform switching during neuronal differentiation reveals a distinct pluripotency-associated non-canonical transcript](https://www.biorxiv.org/content/10.64898/2026.11.25.769322v1)** (Cell and molecular biology): Cells carry a gene called H19 that can be read out in several slightly different versions, and this study asks which version is used when stem cells turn into nerve cells. The authors found that a shorter version, which starts from a different first segment, is the main one in stem cells and nearly disappears as the cells become neurons, while the standard version and the neighbouring IGF2 gene increase. Other cell types they tested, such as mesenchymal stem cells, mostly used the standard version.
- **[Representational geometry shapes noise-driven working memory errors](https://www.biorxiv.org/content/10.64898/2026.11.23.768703v1)** (Neuroscience): When people try to remember colors or other items for a few seconds, they sometimes give an answer that looks random, as if they guessed. This study recorded brain activity from many sites across the monkey outer brain during a color memory task to ask where those guesses come from. The authors report that signs of guessing appear during the memory delay itself, and that the way the brain's activity is arranged for color matches the pattern of each animal's mistakes.

## Probability

### [Converse comparison of $g$-expectations and uniqueness of generators of BSDEs: a novel approach and some sharp results](https://arxiv.org/abs/2611.34304)
*Xuejun Shi, Shengjun Fan, Long Jiang* · `math.PR` · arXiv:2611.34304v1 · relevance 0.20

- **In one sentence**: The paper studies inverse problems for backward stochastic differential equations (BSDEs), proving via a forward-SDE representation of generators that an ordering between two g-expectations forces pointwise comparability of their generators under only the standard Lipschitz assumption, which also yields a general uniqueness theorem for BSDE generators.
- **In plain words**: The paper asks a reverse question about a mathematical tool called a backward stochastic differential equation, which is used to price risk and model decisions under uncertainty. Given only the final outcomes, can you recover the rule that produced them? The authors show that if one such outcome is always ordered above another, the underlying rules must also be ordered at every point, and they do this without the extra simplifying assumptions earlier work needed.
- **Why it matters**: The result claims to fully settle the converse comparison problem for g-expectations in the standard Lipschitz setting, and to give a general uniqueness statement for BSDE generators. Its significance rests on the proofs in the full paper, which the summary does not show; its links to applications in finance or control are not described in the text.
- **Background needed**: - Stochastic differential equation (SDE): an equation describing a quantity that evolves randomly over time, like a noisy price path.
- Backward SDE (BSDE): an equation run backward from a known terminal value, whose solution includes a random process and a "generator" that sets how the value changes over time.
- Generator: the rule inside a BSDE that determines how the solution drifts; it is the object the paper tries to recover.
- g-expectation: a nonlinear way of averaging a future payoff, defined as the initial value of a BSDE with generator g.
- Comparison theorem: a result saying that if terminal outcomes are ordered, the initial values are ordered too; the converse asks whether the reverse holds.
- Lipschitz condition: a mild smoothness requirement that the rule changes at a bounded rate.
- Uniqueness of generators: the claim that the initial values determine the generator. · level: research-level

<details><summary>Original abstract</summary>

This paper investigates inverse problems for backward stochastic differential equations (BSDEs), with a particular focus on the converse comparison theorem and the uniqueness of generators solely through the initial values of the corresponding solutions. To this end, we develop a forward-SDE representation approach that combines a contradiction argument with a representation of generators in terms of solutions to associated forward stochastic differential equations (SDEs). As one of the main consequences, we prove that an ordering between two $g$-expectations necessarily implies the pointwise comparability of their generators, without requiring any additional structural assumptions beyond the standard Lipschitz condition. This removes the continuity, $y$-independence, and deterministic assumptions required in previous works, thereby yielding a complete solution to the converse comparison problem for $g$-expectations under the standard Lipschitz framework and, at the same time, establishing a general uniqueness theorem for generators of BSDEs.

</details>

### [Graphon hitting times: connectivity and minimum degree](https://arxiv.org/abs/2611.33540)
*Constanza Gacit\'ua Fuentes, Marcos Kiwi, Mat\'ias Pavez-Sign\'e* · `math.CO` · arXiv:2611.33540v1 · relevance 0.19

- **In one sentence**: The paper proves that, for graphon-based inhomogeneous random graphs under a connectivity and low-degree-tail condition, the connectivity and minimum-degree-one hitting times coincide whp, and gives criteria for when this transition is sharp, using Laplace transforms and vague convergence of rescaled degree measures.
- **In plain words**: Imagine building a random network one link at a time until every node is connected to the rest. A classic fact for the simplest random networks is that this moment arrives exactly when the last lonely, unlinked node gets its first link. This paper proves a version of that fact for a much broader family of random networks, where different nodes have different chances of linking, described by a "graphon."
- **Why it matters**: It extends a well-known random-graph result to inhomogeneous networks, with conditions stated in terms of the graphon's degree distribution. The text also revisits minimum-degree results of Hladký and Viswanathan with simpler proofs, so it may matter to people studying random network models more generally.
- **Background needed**: - Random graph: a network whose edges are chosen at random; here edges are added one by one in random order.
- Hitting time: the first moment a property (here, connectivity or having no isolated vertex) holds.
- Graphon: a limiting description of a large random network in which each pair of node "types" has a link probability.
- Degree: the number of links at a node; the degree distribution describes how degrees are spread across nodes.
- Asymptotically almost surely (a.a.s.): with probability tending to 1 as the network grows.
- Laplace transform and vague convergence: standard analytic tools for handling distributions of small values; no need to master them to grasp the main message. · level: research-level

<details><summary>Original abstract</summary>

A classical result in random graphs states that the Erd\H{o}s--R\'enyi random graph process becomes connected at exactly the moment its last isolated vertex disappears. The main goal of this paper is to establish a graphon analogue of this result. Let $G(n,W)$ be the inhomogeneous random graph sampled from a graphon $W$, and reveal its edges one by one in a uniformly random order. We prove that if $W$ is connected and the lower tail of its degree distribution satisfies $g_W(t)/t\to 0$ as $t\to 0$, which is needed for the connectivity of $G(n,W)$, then the connectivity and minimum-degree-one hitting times coincide asymptotically almost surely. We also determine when this hitting time occurs at scale $\Theta(n\log n)$, as in the binomial random graph model. Moreover, we give a simple analytic criterion for the transition to be localized in a $(1+o(1))$-multiplicative window, and construct graphons with minimum degrees arbitrarily close to zero whose transition is nevertheless sharp. Our approach uses Laplace transforms and vague convergence of rescaled graphon degree measures to provide a unified framework for analyzing low-degree vertices and connectivity transitions. Along the way, we revisit the minimum degree of~$G(n,W)$, giving simplified proofs of results of Hladk\'y and Viswanathan~\cite{HV} and establishing the limiting distribution of $\delta(G(n,W))$ under a second-order decorrelation condition.

</details>

## Differential geometry

### [Nonlocal approximation of stable minimal surfaces with prescribed number of connected components](https://arxiv.org/abs/2611.33476)
*Lorenzo De Gaspari, Serena Dipierro, Ovidiu Savin et al.* · `math.DG` · arXiv:2611.33476v1 · relevance 0.23

- **In one sentence**: The paper shows that strictly stable classical minimal hypersurfaces in a Euclidean ball can be approximated, for the fractional parameter s close to 1, by stable s-minimal surfaces in a smaller ball, and uses this to build stable nonlocal minimal surfaces with many connected components.
- **In plain words**: The paper studies soap-film-like surfaces that minimize area, in two versions: ordinary ones and "nonlocal" ones whose cost depends on long-range interactions, controlled by a parameter s. It shows that, when s is close to 1, a stable nonlocal version can be found that closely follows a given ordinary stable surface inside a smaller region. As a consequence, the authors can build such nonlocal surfaces with many separate pieces, as long as the number of pieces stays below a bound that grows as s approaches 1.
- **Why it matters**: It connects the classical theory of minimal surfaces with the newer nonlocal theory, showing that the two can be linked quantitatively. The text describes the bound on the number of components as optimal at least in dimensions 2 and 3, though it does not spell out why beyond that claim.
- **Background needed**: - Minimal surface: a surface that locally has the least area for its boundary, like a soap film; "stable" means it stays minimal under small perturbations.
- Mean curvature: a local measure of how a surface bends on average; a minimal surface has zero mean curvature.
- Nonlocal perimeter/mean curvature: a version of area whose cost counts interactions between distant points, weighted by a parameter s in (0,1); as s tends to 1 it approaches the ordinary notion.
- Foliation: a family of nested or parallel surfaces filling a region, used here as barriers (comparison surfaces).
- Connected components: separate pieces of a surface.
- Euclidean ball: a solid round region in ordinary space. · level: research-level

<details><summary>Original abstract</summary>

We show that every strictly stable classical minimal hypersurface in a Euclidean ball can be approximated, for $s$ sufficiently close to $1$, by a stable $s$-minimal surface in a smaller ball. We also give an explicit lower bound on the size of the interval of admissible values of $s$. As a consequence, we construct stable nonlocal minimal surfaces with an arbitrarily large number $k$ of connected components in a bounded region, under the quantitative condition $k \leq \frac{C}{\sqrt{1-s}}$, attaining an optimal result (at least in dimensions $2$ and $3$). As part of the proof of our main result, we obtain an auxiliary result of independent interest, providing quantitative estimates for foliations of constant mean curvature embedded hypersurfaces near a stable minimal surface. The resulting foliation supplies nonlocal barriers thanks to known results of uniform convergence of the nonlocal mean curvature to the classical one when $s \to 1$.

</details>

### [Equivariant cohomology of stacky Lie group actions](https://arxiv.org/abs/2611.33604)
*Daniel L\'opez Garcia, Cristian Ortiz, Roberto Villaflor* · `math.DG` · arXiv:2611.33604v1 · relevance 0.23

- **In one sentence**: The paper defines equivariant cohomology for Lie groupoids and differentiable stacks acted on by Lie 2-groups, proves Morita invariance and a simplicial Cartan model, and applies this to toric symplectic stacks.
- **In plain words**: Mathematicians often study symmetric spaces by tracking how a group of symmetries acts on them. This paper extends that toolkit to "stacks," which are generalized spaces that carry extra structure (such as orbifold-like singularities), and to the higher symmetry groups that act on them. The authors build an invariant of these symmetric objects, check that it does not depend on how the object is presented, and use it to compute an example.
- **Why it matters**: The work gives a well-defined way to measure symmetry-related topological information for stacks, which are increasingly used in geometry and mathematical physics. The text does not say how far the results reach beyond the toric symplectic examples it mentions, so the wider significance is uncertain.
- **Background needed**: - Lie group: a continuous group of symmetries, such as rotations.
- Group action: a way a group moves the points of a space.
- Cohomology: an algebraic invariant that counts topological features (holes, loops) of a space.
- Equivariant cohomology: a version of cohomology that also takes a group's symmetry into account.
- Lie groupoid: a presentation of a space, possibly with singularities, by a collection of points and arrows between them.
- Stack / differentiable stack: a generalized space, often presented by a groupoid; two presentations can describe the same stack (Morita equivalence).
- Lie 2-group: a higher-dimensional analogue of a Lie group, with symmetries between symmetries.
- Symplectic manifold: a space with a geometric structure from classical mechanics; toric means it has a large symmetry torus acting on it. · level: research-level

<details><summary>Original abstract</summary>

In this work we introduce equivariant cohomology for Lie groupoids and differentiable stacks. For Lie groupoids equipped with a strict action of a Lie 2-group, we define the corresponding equivariant cohomology via the Borel model and establish its Morita invariance. We also construct a simplicial Cartan model and prove that, under standard compactness assumptions, it recovers the equivariant cohomology defined via the Borel model. In the framework of stacky Lie group actions, we show that if a connected and \'etale stacky Lie group acts on a differentiable stack admitting an equivariant atlas, then the stacky action admits a strict presentation by a Lie 2-group action. Furthermore, we prove that different choices of equivariant atlases yield equivariantly Morita equivalent presenting actions, giving rise to a well-defined notion of equivariant cohomology for differentiable stacks. As an application, we compute the equivariant cohomology of toric symplectic stacks.

</details>

## Partial differential equations

### [Existence of odd-frequency free boundary points in the Signorini problem](https://arxiv.org/abs/2611.34456)
*Xavier Fern\'andez-Real* · `math.AP` · arXiv:2611.34456v1 · relevance 0.27

- **In one sentence**: The paper constructs a solution to the Signorini (obstacle-type) problem with a free boundary point of frequency 3, settling the open question of whether odd-frequency free boundary points exist.
- **In plain words**: The paper studies a mathematical model where a surface is pressed against an obstacle, and the boundary between contact and non-contact regions can have a complicated shape. Researchers had classified the possible boundary points by a number called "frequency," and one class (odd frequencies at full-density points) had never been shown to actually occur. The authors build an explicit solution that has a boundary point of frequency 3, showing that this class is not empty.
- **Why it matters**: Settling whether a predicted type of singular point exists completes a known classification and tests how far existing structure theory reaches. The text does not indicate applications beyond this theoretical question, so its wider significance is uncertain.
- **Background needed**: - Signorini problem: a boundary-value problem where a function must stay above an obstacle, and is either touching it or free, with a free boundary separating the two.
- Free boundary: the interface between the contact set and the non-contact set.
- Frequency: a number measuring how the solution grows or behaves near a boundary point; it is a scaling-type index, and only certain values are possible.
- Density: a measure of how much of a small ball around a point is occupied by the contact or non-contact set; zero density and full density are the two extreme cases referred to.
- Half-integer, even, and odd frequencies: the three classes of free boundary points the classification allows; the paper concerns the odd class.
- Regularity: how smooth the free boundary is; known results cover structure of each class. · level: research-level

<details><summary>Original abstract</summary>

Up to a lower-dimensional set, the free boundary of the Signorini problem consists of points with frequency that is half-integer, even (at zero density points), or odd (at full density points). Surprisingly, despite extensive work on the structure and regularity of each of these sets, the existence of odd-frequency free boundary points has remained open. In this paper, we construct a solution with a free boundary point of frequency 3.

</details>

### [Critical exponent for Nakao's problem in three space dimensions](https://arxiv.org/abs/2611.33800)
*Vladimir Georgiev, Kosuke Kita* · `math.AP` · arXiv:2611.33800v1 · relevance 0.24

- **In one sentence**: The paper finds the sharp exponent condition in three space dimensions separating global existence of small-data solutions from finite-time blow-up for a damped wave equation coupled to a wave equation (Nakao's problem), using weighted pointwise estimates and test-function arguments.
- **In plain words**: The paper studies a pair of coupled equations that describe how waves and damped (smeared-out, friction-like) motion can feed into each other in three-dimensional space. It asks for which strengths of the nonlinear coupling a small starting disturbance keeps evolving smoothly forever, and for which strengths even tiny starting disturbances can blow up in finite time. The authors identify the exact boundary between these two behaviours.
- **Why it matters**: Knowing exactly where the line falls between "stays bounded" and "blows up" is the kind of sharp answer that mathematicians look for in nonlinear wave models. The text does not say how it connects to applications beyond this class of equations, so any wider relevance is unclear from the text alone.
- **Background needed**: - A "wave equation" describes vibrations and signals that travel at a finite speed, like sound or light fronts.
- A "damped" wave equation includes friction, so its behaviour at late times looks more like diffusion or heat spreading.
- "Semilinear" means the nonlinear term is a power of the unknown function, and the exponents of these powers decide the outcome.
- "Global existence" means a solution exists for all time; "finite-time blow-up" means it becomes infinitely large in a finite time.
- "Critical exponent" is the threshold value of such a power that separates the two behaviours.
- "Pointwise estimates" are bounds on the solution at each individual point, with weights that track how it spreads in space.
- "Test functions" are auxiliary smooth functions used to derive integral inequalities that a blowing-up solution cannot satisfy. · level: research-level

<details><summary>Original abstract</summary>

We study a system consisting of a semilinear damped wave equation coupled to a semilinear wave equation in three space dimensions. We determine the sharp condition on the exponents of nonlinear terms that separates global existence for sufficiently small initial data from finite-time blow-up even for arbitrarily small data satisfying suitable positivity assumptions. To prove global existence, we combine a weighted pointwise estimate for the damped wave equation, which we established in earlier work, with a new one for the wave equation. The new pointwise estimate for the wave equation uses a combination of a parabolic weight and a light-cone weight. For the proof of blow-up, pointwise lower bounds are compared with integral upper bounds obtained by test functions. In the main estimates, explicit physical-space representations reveal how forcing near the wave cone influences the damped component on parabolic spatial scales and, in turn, the wave component inside the cone.

</details>

## Harmonic analysis

### [The Kalton--Peck space disproves Rubio de Francia's conjecture](https://arxiv.org/abs/2611.33556)
*Veli Shakhmurov, Rishad Shahmurov* · `math.FA` · arXiv:2611.33556v1 · relevance 0.14

- **In one sentence**: The paper shows that the complex Kalton–Peck space Z_2 is never of the form [X,H]_θ (complex interpolation between a UMD space X and a Hilbert space H), which disproves Rubio de Francia's conjecture on intermediate UMD spaces.
- **In plain words**: This is about a question in functional analysis: whether a certain well-known infinite-dimensional space can be built by "blending" a nice space with a Hilbert space. The authors prove it cannot be built that way for any choice of the nice space and blending setting, which answers a conjecture from the 1980s in the negative. The argument combines several technical estimates and a convexity and separation argument from standard analysis.
- **Why it matters**: It settles a named conjecture in the negative, so it matters for anyone tracking which spaces can arise as interpolation scales. The text does not say how far the result reaches beyond this specific conjecture, so broader implications are uncertain.
- **Background needed**: - Banach space: a complete normed vector space, the usual setting for infinite-dimensional analysis.
- UMD space: a Banach space where a certain family of singular-integral-type operators stays bounded; it is a standard "well-behaved" class.
- Hilbert space: a space with an inner product, like ordinary Euclidean geometry extended to infinite dimensions.
- Complex interpolation [X,H]_θ: a way of producing an intermediate space between two spaces, indexed by a parameter θ between 0 and 1.
- Kalton–Peck space Z_2: a classical example of a space built from a twisted construction, known to be UMD.
- Rubio de Francia's conjecture: the proposal that intermediate spaces between UMD spaces are always UMD-like in a specific sense; this paper says the conjecture fails. · level: research-level

<details><summary>Original abstract</summary>

We prove that the classical complex Kalton--Peck space $Z_2$ is not isomorphic to $[X,H]_\theta$ for any UMD Banach space $X$, Hilbert space $H$, and $0<\theta<1$. Since $Z_2$ is UMD, this disproves Rubio de Francia's conjecture on intermediate UMD spaces. The proof combines the logarithmic block identity, a shift-commutator estimate on the interpolation strip, a unified obstruction in terms of reciprocal Hilbert norms, and Hahn--Banach with elementary convexity. It allows arbitrary compatible placements. We also realize $Z_2$ as a quotient of a closed subspace of an intermediate UMD space for every fixed interpolation parameter less than one.

</details>

### [Weak monotonicity, Critical exponents, and Gagliardo-Nirenberg inequalities on weighted graphs](https://arxiv.org/abs/2611.34017)
*Patricia Alonso Ruiz, Fabrice Baudoin, Li Chen* · `math.PR` · arXiv:2611.34017v1 · relevance 0.12

- **In one sentence**: The paper studies weak monotonicity of heat kernel and ball-averaged functionals on weighted graphs, proving weak Bakry-Émery estimates under sub-Gaussian heat kernel bounds and deriving Gagliardo-Nirenberg, Sobolev, Nash and isoperimetric inequalities on strongly recurrent graphs and their products.
- **In plain words**: This paper is about how heat spreads over networks: nodes connected by weighted links, where a "heat" quantity diffuses from node to node over time. The authors show that under certain tail-type bounds on how fast heat spreads, a weakened form of a smoothness-and-monotonicity property holds, with explicit exponents for graphs that are "strongly recurrent" (random walks on them return to their starting region reliably). They then use this to derive a family of standard inequalities that relate size, smoothness and volume on such networks.
- **Why it matters**: Inequalities of the Sobolev and Nash type are basic tools for judging how fast diffusions and random walks behave, so results that hold on graphs and on products of graphs may be useful to researchers in analysis and probability. The text does not indicate applications beyond this theory, so the wider significance is uncertain.
- **Background needed**: - A weighted graph: points (vertices) joined by links (edges) that carry numerical weights, like a network of roads with distances.
- Heat kernel: a function describing how a unit of heat or probability starting at one point spreads to other points over time; equivalently, the transition law of a random walk.
- Sub-Gaussian heat kernel estimate: a bound saying the spreading probability has tails no heavier than a Gaussian (bell curve) decay, with distance measured in a suitable way.
- Semigroup and Bakry-Émery estimates: a standard way of expressing how smoothing by diffusion controls the size of gradients (rates of change) of functions.
- Recurrence: a random walk is recurrent if it returns to its start infinitely often; "strongly recurrent" is a stronger version of this.
- Sobolev, Nash, Gagliardo-Nirenberg and isoperimetric inequalities: standard relations between a function's size, its rate of change, and the volume of sets, used to quantify how a space or network behaves.
- Hölder exponent: a number measuring a degree of smoothness. · level: research-level

<details><summary>Original abstract</summary>

We study weak monotonicity of heat kernel and ball averaged functionals on weighted graphs, and the associated critical exponents. Under sub-Gaussian heat kernel estimates, weak Bakry-\'Emery estimates for the semigroup are proved, with explicit values of the H\"older regularity exponent in the strongly recurrent case. Applications of the theory include Gagliardo-Nirenberg, Sobolev, Nash and isoperimetric inequalities on strongly recurrent graphs and their products.

</details>

## Complex analysis

### [Singularities in global pluripotential theory](https://arxiv.org/abs/2611.33697)
*Mingchen Xia* · `math.CV` · arXiv:2611.33697v1 · relevance 0.38

- **In one sentence**: A book-length treatment of plurisubharmonic singularities on compact Kähler manifolds, linking them to non-Archimedean and toric pluripotential theory.
- **In plain words**: This is a book, expanded from lecture notes, about a branch of advanced geometry that studies functions on complex spaces which are "bent" in controlled ways, especially where they blow up or become singular. The author builds up the theory systematically and connects it to two related settings: one that uses a different notion of distance (non-Archimedean) and one built on shapes called toric varieties. The text summary does not list specific new results.
- **Why it matters**: Pluripotential theory is a central tool for studying the geometry of complex spaces, and bringing together its singular side with non-Archimedean and toric versions may be useful for specialists. The summary is too brief to say which results are new, so its exact importance is unclear from this text alone.
- **Background needed**: - Complex manifolds: smooth spaces locally described by complex numbers.
- Kähler manifolds: complex manifolds with a compatible geometric structure, common in algebraic geometry.
- Plurisubharmonic functions: a class of functions that behave like "convex" functions in several complex directions.
- Singularities: points where such a function or space fails to be smooth.
- Non-Archimedean geometry: a version of analysis using a distance in which the triangle inequality is strengthened.
- Toric varieties: spaces built from combinatorial data about polytopes. · level: research-level

<details><summary>Original abstract</summary>

This book is an expanded version of the author's lecture notes at the Institute for Advanced Study in Mathematics (IASM) at Zhejiang University. We systematically develop the theory of plurisubharmonic singularities on compact K\"ahler manifolds and relate it to the non-Archimedean pluripotential theory and toric pluripotential theory.

</details>

### [Cyclic polynomials in mixed-weighted Dirichlet-type spaces](https://arxiv.org/abs/2611.34661)
*Rajkamal Nailwal, Aljaz Zalar* · `math.FA` · arXiv:2611.34661v1 · relevance 0.11

- **In one sentence**: The paper gives a complete characterization of which polynomials are cyclic in mixed-weighted Dirichlet-type spaces of functions on the bidisk, in terms of their zero sets and the three weight parameters.
- **In plain words**: The paper studies a family of function spaces made of functions of two complex variables, where each coefficient of the function is weighted by a size-dependent factor controlled by three real parameters. A function is "cyclic" if, by multiplying it by polynomials and taking limits, one can approximate the constant function 1 inside the space. The authors determine exactly which polynomials have this property, using only where they vanish and the values of the three parameters.
- **Why it matters**: Cyclicity is a basic structural question for these spaces, since it describes which functions generate the whole space under multiplication. The result extends earlier characterizations for anisotropic and total-degree versions of the same spaces on the bidisk, so it is a systematic completion of that line of work rather than a new direction; its wider significance beyond this specialist area is unclear from the text alone.
- **Background needed**: - Unit bidisk: the set of pairs of complex numbers (z1, z2) with each having absolute value less than 1.
- Holomorphic function: a complex-differentiable function of complex variables, here written as a power series in z1 and z2.
- Dirichlet-type space: a space of functions whose norm combines the size of the function with the size of its derivatives, here via weighted sums of squared coefficients.
- Mixed weights: the three exponents alpha1, alpha2, alpha3 control how strongly the coefficient indices m, n and m+n are weighted.
- Cyclic function: a function f such that the closure of all polynomial multiples of f contains the constant 1; informally, f "generates" the whole space.
- Zero set: the set of points where a polynomial equals zero. · level: research-level

<details><summary>Original abstract</summary>

For $\boldsymbol{\alpha}=(\alpha_1,\alpha_2,\alpha_3)\in\mathbb R^3$, we investigate cyclic polynomials in the mixed-weighted Dirichlet-type space $\mathscr{D}_{\boldsymbol{\alpha}}$ of holomorphic functions $f(z_1,z_2)=\sum_{m,n\geq0}a_{m,n}z_1^mz_2^n$ on the unit bidisk satisfying $$ \sum_{m,n\geq0}|a_{m,n}|^2 (m+1)^{\alpha_1}(n+1)^{\alpha_2} (m+n+1)^{\alpha_3}<\infty. $$ We give a complete characterization of cyclic polynomials in terms of their zero sets and the parameters $\alpha_1,\alpha_2,\alpha_3$. Our results extend previously known characterizations for anisotropic and total-degree Dirichlet-type spaces on the unit bidisk.

</details>

## Operator algebras and spectral theory

### [On Shepp's property in free probability](https://arxiv.org/abs/2611.33960)
*Wiktor Ejsmont, Takahiro Hasebe, Patrycja H\k{e}\'cka-J\k{e}draszczyk* · `math.OA` · arXiv:2611.33960v1 · relevance 0.18

- **In one sentence**: The paper proves a free-probability analogue of Shepp's theorem for freely independent standard semicircular elements, showing that a family of self-normalized squared quadratic forms is free with standard Marchenko-Pastur laws, and adds free analogues of Lukacs-type independence results.
- **In plain words**: This is a pure mathematics paper about "free probability," a version of probability theory for noncommuting random quantities such as large random matrices. It asks whether a classical fact about independent random variables, Shepp's theorem, still holds when the variables are "free" in this noncommutative sense. The authors show that it does, using the three Pauli matrices as coefficients, and they also prove some related results of the Lukacs type.
- **Why it matters**: The text places the work as a translation of a classical independence result into the noncommutative setting, which is the kind of bridge that matters for operator algebras and random matrix theory. The abstract does not say what applications, if any, follow, so its wider significance beyond this translation is uncertain.
- **Background needed**: - Shepp's theorem: a classical result about when certain squared quadratic forms in independent Gaussian variables are independent; the paper's starting point.
- Free independence: Voiculescu's noncommutative analogue of independence, used for operators rather than ordinary random variables.
- Semicircular element: the free analogue of a Gaussian (normal) random variable.
- Marchenko-Pastur distribution: a limiting distribution of eigenvalues of random sample covariance matrices, here the target law for each self-normalized squared form.
- Quadratic form: an expression like x^T A x built from a vector and a matrix; Pauli matrices are specific 2x2 complex matrices from quantum physics.
- Lukacs-type results: characterizations of distributions via independence of certain combinations of variables.
- Corner algebra / free projection: a compressed piece of an operator algebra cut out by a projection. · level: research-level

<details><summary>Original abstract</summary>

We establish a free analogue of Shepp's theorem for freely independent standard semicircular elements. We show more generally that a family of self-normalized squared quadratic forms is free, and each has a standard Marchenko-Pastur distribution. The free analogue of Shepp's theorem follows by taking the coefficients of quadratic forms to be the three Pauli matrices. We also prove some new free analogues of Lukacs-type independence results. The key part of the proof is a construction of an equivalent and simpler operator model on a corner algebra compressed by a free projection.

</details>

### [The type I conjecture for locally compact groups acting on trees](https://arxiv.org/abs/2611.34793)
*Cyril Houdayer, Basile Morando* · `math.GR` · arXiv:2611.34793v1 · relevance 0.15

- **In one sentence**: The paper proves that closed groups acting minimally and two-transitively on the boundary of a locally finite tree are uniformly admissible (hence type I), settling Nebbia's conjecture, and uses an operator-algebra result on amenable amalgamated free products of atomic von Neumann algebras with integer traces.
- **In plain words**: The paper studies symmetry groups of tree-like networks, the kind of branching structure where every node has finitely many neighbours and there is no loop. It shows that, under a natural condition on how the group acts on the "edges at infinity" of the tree (two-transitivity), the group behaves in a very regular way that mathematicians call type I. The main tool is a result about certain algebras of operators, which are the mathematical objects used to describe these symmetries.
- **Why it matters**: The text says this settles a conjecture of Nebbia in a strong form, and that together with earlier work by Caprace, Kalantar and Monod it gives a complete if-and-only-if characterisation for nonamenable groups acting minimally on such trees. The text does not say what wider applications it has, so any connection beyond this area is unclear from the text alone.
- **Background needed**: - Locally finite tree: a connected graph with no cycles where each vertex has finitely many neighbours; its boundary is the set of its "ends" (infinite paths going out to infinity).
- Group acting on a tree: a group of symmetries (automorphisms) of the tree; "minimal" means no proper invariant subtree; "two-transitive" on the boundary means any two pairs of distinct boundary points can be mapped to each other.
- Amenable group: roughly, a group with a kind of averaging/invariant-mean property; nonamenable groups are the "large" opposite case.
- Type I: a regularity property of a group's representations (linked to its unitary representation theory); this is the main property studied.
- Von Neumann algebra: an algebra of bounded operators on a Hilbert space, used as the operator-algebra framework; "atomic" means it is generated by minimal projections in a discrete way; "trace" is a generalised notion of summing diagonal values.
- Amalgamated free product: a way of gluing two algebras along a common subalgebra, analogous to gluing groups along a common subgroup. · level: research-level

<details><summary>Original abstract</summary>

We prove that a closed group of automorphisms acting minimally on a locally finite tree and two-transitively on its boundary is uniformly admissible, hence of type I. This solves Nebbia's conjecture in a strong form. Together with the work of Caprace, Kalantar and Monod, this shows that for every closed nonamenable subgroup $G$ of $\mathrm{Aut}(T)$ acting minimally on a locally finite tree $T$, $G$ is of type I if and only if the action on $\partial T$ is two-transitive. The key ingredient is the following operator algebraic result: if the projections of two atomic von Neumann algebras $A_1, A_2$ have integer traces, then every amenable amalgamated free product $A_1 \ast_B A_2$ with $B$ atomic is of type I.

</details>

## Algebra

### [Galois scalar extension of simple Lie algebras](https://arxiv.org/abs/2611.34409)
*Alfonso Di Bartolo, Francesco Paolo Di Fatta, Gianmarco La Rosa* · `math.RA` · arXiv:2611.34409v1 · relevance 0.28

- **In one sentence**: The paper studies how simple finite-dimensional Lie algebras behave under scalar extension by a finite Galois field extension, giving a splitting criterion for the extended algebra, a simplicity result for prime-order cyclic extensions, and the invariance of the dimension of the centroid, with an application to finite fields.
- **In plain words**: The paper looks at a family of algebraic structures called simple Lie algebras and asks what happens when you enlarge the number system they are built over, using a Galois extension (a standard way of adding new numbers such as square roots while keeping a symmetry structure). The authors show that under a stated condition the enlarged structure splits into several identical copies of a simpler object, and that in certain prime-order cases with no such copy it stays simple. They also show that a certain invariant, the dimension of the centroid, does not change under these extensions, and use this to work out the centroids over finite fields.
- **Why it matters**: The results give a general way to carry classification and structure results from one ground field to another, which is a recurring theme in algebra. The text itself does not discuss applications beyond the centroid computation over finite fields, so the wider reach is uncertain.
- **Background needed**: - Lie algebra: a vector space with a bracket operation satisfying certain rules, used to describe symmetries (e.g., of continuous transformations).
- Simple Lie algebra: one with no nontrivial proper ideals (no smaller sub-structures closed under the bracket that could be split off).
- Field: a number-like system where addition, subtraction, multiplication and division work (e.g., rationals, real numbers, finite fields with a prime number of elements).
- Field extension: a larger field containing the original, e.g., adding a square root of 2 to the rationals; Galois means it has a rich symmetry group.
- Scalar extension (tensoring with a field): building a new algebra over the bigger field from an algebra over the smaller one.
- Centroid: the set of linear maps that commute with the bracket up to scalar multiplication; its dimension is an invariant.
- Direct sum: placing several copies of an object side by side with no interaction. · level: research-level

<details><summary>Original abstract</summary>

We investigate the behaviour of simple finite-dimensional Lie algebras under finite Galois field extensions. Given a simple Lie algebra $L$ over a field $\mathbb{F}$ and a finite Galois extension $\mathbb{K}/\mathbb{F}$ of degree $n = [\mathbb{K}:\mathbb{F}]$, we prove that if $L$ is isomorphic to a $\mathbb{K}$-Lie algebra $S$ viewed as an $\mathbb{F}$-algebra, then the scalar extension $L \otimes_{\mathbb{F}} \mathbb{K}$ is isomorphic to the direct sum of $n$ copies of $S$. Furthermore, for cyclic extensions of order a prime number, we show that if no such $\mathbb{K}$-Lie algebra $S$ exists, the extended algebra $L \otimes_{\mathbb{F}} \mathbb{K}$ remains simple. This framework provides a general mechanism to transfer structural and classification results across different ground fields. In addition, we examine the centroids of simple Lie algebras, proving that the dimension of the space of centroids is invariant under finite field extensions. As an application, we explicitly determine the structure of the spaces of centroids for simple Lie algebras over finite fields.

</details>

### [Normal abelian subgroups of order 5^6 in finite 5-groups](https://arxiv.org/abs/2611.34205)
*L\"u Gong, Jiaye Chen, Baojun Li* · `math.GR` · arXiv:2611.34205v1 · relevance 0.16

- **In one sentence**: The paper proves that every finite 5-group containing an abelian subgroup of order 5^6 also has a normal abelian subgroup of that order (elementary abelian when the given one is), settling the last open case n=6 of Kourovka Notebook Problem 21.51 for p=5.
- **In plain words**: The paper studies finite groups built from symmetry-like operations where every element has a power-of-five size. It asks whether a certain kind of "flat, evenly-behaved" sub-collection of a given size that exists inside such a group must also exist in a stable, well-positioned form. The author settles the last open case of this question for sub-collections of size 5 to the sixth power, using a minimal counterexample argument.
- **Why it matters**: It closes a listed open problem from a well-known problem collection, and together with earlier results it fixes exactly which sizes the statement holds for. The text does not indicate wider applications beyond group theory.
- **Background needed**: - Group: a set of symmetries (or abstract elements) with a rule for combining them.
- Finite 5-group: a group whose size is a power of 5.
- Abelian subgroup: a sub-collection in which elements commute, so the order of combining them does not matter.
- Normal subgroup: a sub-collection that stays unchanged under conjugation (re-labelling by other group elements).
- Elementary abelian: abelian and every non-identity element has order 5.
- Order 5^6: the sub-collection has 5^6 = 15625 elements.
- Kourovka Notebook: a public list of open problems in group theory.
- Commutator pairing, isotropic subgroup, plane cubic over GF(5): tools from linear and algebraic structure over the field with five elements; the text uses them only in outline. · level: research-level

<details><summary>Original abstract</summary>

A finite 5-group containing an abelian subgroup of order 5^6 has a normal abelian subgroup of that order. If the given subgroup is elementary abelian, the normal subgroup can be chosen elementary abelian. This resolves n=6, the last open case of both parts of Problem~21.51 of the Kourovka Notebook for p=5. Together with earlier results, it follows that 1\le n\le 6 is the exact range in which each assertion holds for every finite 5-group at subgroup order 5^n. In a minimal counterexample, five conjugate abelian subgroups generate a group of class at most three. In class two we construct invariant isotropic subgroups for the commutator pairing. In class three the Jacobi identity produces a nonzero plane cubic over the field of five elements. The five conjugate subgroups give five distinct singular points spanning the plane, which forces the cubic to vanish.

</details>

## Representation theory

### [Tensor ideals of oligomorphic permutation categories](https://arxiv.org/abs/2611.34187)
*Inna Entova-Aizenbud, Thorsten Heidersdorf* · `math.RT` · arXiv:2611.34187v1 · relevance 0.13

- **In one sentence**: The paper classifies tensor ideals in oligomorphic permutation categories Perm(G,μ) by an equivalence relation on transitive smooth G-sets, giving a bijection with downward-closed subsets of the resulting poset, and computes that poset in many cases.
- **In plain words**: This paper is about a family of mathematical structures built from groups that act on sets in a very "tame" way, with the aim of listing all the ways one can consistently discard objects from them. The authors sort the relevant sets into classes under a suitable notion of equivalence, and show that the ways of discarding objects (the tensor ideals) correspond exactly to the downward-closed collections of those classes. They then work out this correspondence explicitly for many specific groups, including symmetric groups, wreath products and classical matrix groups over finite fields.
- **Why it matters**: The text gives a complete classification in a stated class of categories, which is a clean structural result rather than a claim of wide impact. Its connection to other areas (such as tensor triangular geometry or the study of infinite-symmetry categories) is suggested by the setting but is not spelled out in the text, so the wider significance is uncertain.
- **Background needed**: - Category: a collection of objects and structure-preserving maps between them.
- Tensor product: a way of combining two objects, as in the tensor product of vector spaces.
- Tensor ideal: a subcollection of objects closed under taking summands and tensoring with anything, a kind of "absorbing" subset.
- Thick tensor ideal: a tensor ideal that is also closed under taking direct summands and certain "two-out-of-three" exact sequences.
- Group action on a set: a group permuting the elements of a set; "transitive" means any element can be moved to any other.
- Oligomorphic group: an infinite group with only finitely many orbits on each finite power of its underlying set; the infinite symmetric group is the standard example.
- Poset: a partially ordered set; downward-closed means if an element is included, everything below it is too.
- Characteristic: a number describing arithmetic in a field; characteristic 0 (like rationals) versus positive characteristic (like finite fields) behave differently. · level: research-level

<details><summary>Original abstract</summary>

We classify tensor ideals for oligomorphic permutation categories $Perm(G,\mu)$. To this end we define an equivalence relation on the class of transitive smooth $G$-sets. We show that there is a bijection between the tensor ideals of $Perm(G,\mu)$ and the downward-closed subsets of the poset of equivalence classes. As a corollary we obtain that there is a bijection between tensor ideals and thick tensor ideals. We determine the poset in many cases (mostly in characteristic $0$): the infinite symmetric group, wreath products, products of oligomorphic groups, equivariantizations, finite groups in positive characteristic and the classical groups $GL, O, Sp, U$ over a finite field.

</details>

### [The inductive Galois-McKay conjecture for groups of Lie type C](https://arxiv.org/abs/2611.34497)
*Lucas Ruhstorfer* · `math.RT` · arXiv:2611.34497v1 · relevance 0.13

- **In one sentence**: The paper proves the inductive Galois-McKay conjecture for symplectic groups, determining the character fields of irreducible characters of their extensions by field automorphisms, using Brauer trees and generalized Gelfand-Graev characters.
- **In plain words**: This paper is about a central question in the study of symmetry in algebra: how the structure of a group of symmetries relates to the structure of its smaller "local" pieces. The authors focus on one large family of such groups, the symplectic groups, and prove that a predicted matching between these two sides holds for them. A key step is working out which number fields are needed to describe the basic symmetry "measurements" (characters) of the extended groups.
- **Why it matters**: The Galois-McKay conjecture links the representation theory of a finite group to that of its local subgroups, and proving the inductive version for a whole infinite family of groups is a concrete step toward that conjecture. The text does not say what wider applications it may have, so its significance beyond this area is unclear from the text alone.
- **Background needed**: - Finite groups: sets of symmetries closed under combining them, such as rotations or permutations.
- Representation theory: describing a group by how it acts as matrices; "characters" are compact numerical fingerprints of these actions.
- Symplectic groups: a classical family of matrix groups of Lie type C, preserving a certain skew-symmetric form.
- Field automorphisms: relabelings of the number systems the matrix entries live in, which can extend a group.
- Character fields: the smallest number system needed to write down a group's character values.
- Brauer trees and generalized Gelfand-Graev characters: specialized tools for organizing and constructing characters in these groups.
- The Galois-McKay conjecture: a long-standing prediction relating a group's characters to those of its local subgroups, with the "inductive" version being a stronger, recursively checkable form. · level: research-level

<details><summary>Original abstract</summary>

We prove the inductive Galois-McKay conjecture for the symplectic groups. A key result is the determination of the character fields of the irreducible characters of the extensions of the symplectic group by field automorphisms. Two main ingredients for this are the theory of Brauer trees and the generalized Gelfand-Graev characters.

</details>

## Number theory

### [Murmurations in Short Intervals for Elliptic Curves Ordered by Height](https://arxiv.org/abs/2611.33781)
*Aarya J. Kumar* · `math.NT` · arXiv:2611.33781v1 · relevance 0.22

- **In one sentence**: The paper shows how short the range of primes (C1, C2) can be while still recovering the murmuration formula that Sawin and Sutherland proved for elliptic curves ordered by naive height, rather than averaging over all primes.
- **In plain words**: Mathematicians have noticed a wavy pattern in a statistic computed from elliptic curves, a common family of equations in number theory. This paper asks how narrow a band of prime numbers one can average over and still see the same wavy pattern in a previously proven result. The text indicates the authors determined how small that interval can be taken while keeping the conclusion of an earlier formula.
- **Why it matters**: It sharpens a known result by showing the averaging window can be made much smaller, which matters for understanding how the pattern arises. The excerpt does not say how far the window can shrink or what broader consequences follow, so its wider significance is unclear from this text alone.
- **Background needed**: - Elliptic curve: a smooth curve given by a cubic equation, central to number theory.
- L-function: an analytic object encoding arithmetic information about a curve; its coefficients a_p are indexed by primes p.
- Root number (epsilon(E), a sign of plus or minus one): a weighting factor attached to each curve.
- Conductor: an integer measuring how "bad" a curve's reduction is; murmurations were first seen when grouping curves by conductor.
- Naive height: a different way of ranking curves by the size of their coefficients.
- Murmuration: an oscillating pattern in averages of epsilon(E)a_p(E) across curves, observed numerically and proven only in some settings.
- Averaging over an interval of primes: taking the mean over primes in a range (C1, C2). · level: research-level

<details><summary>Original abstract</summary>

Murmurations are the phenomenon, first observed by He, Lee, Oliver, and Pozdnyakov (2025), that the average value of $\epsilon(E) a_p(E)$, the $p$-th $L$-function coefficient weighted by the root number, over elliptic curves of conductor in some range $N(E) \in [N_1, N_2]$ seem to approximate a continuous, oscillating function. While murmurations have been proven for other families of $L$-functions (notably by Zubrilina (2025) for weight $k$ modular forms), the only unconditional murmuration formula for elliptic curves is a partial result by Sawin and Sutherland (2025) ordering by naive height instead of conductor. In this setting, murmurations appear by first averaging $\epsilon(E) a_p(E)$ for a single curve over $p \in (C_1, C_2)$ and then average over elliptic curves of bounded height. However, Sawin and Sutherland's results average $\epsilon(E) a_n(E)$ over all of $\mathbb{N}$ instead of a small interval $(C_1, C_2).$ In this work, we prove how small the interval $(C_1, C_2)$ can be taken while preserving the conclusion of Sawin and Sutherland's first murmuration formula (Proposition 7).

</details>

### [On the Distribution of Prime Factors of $\lfloor \alpha n^2 \rfloor$](https://arxiv.org/abs/2611.34913)
*Cati Alexandru, Johannes Borgwardt, Benjamin Faltin et al.* · `math.NT` · arXiv:2611.34913v1 · relevance 0.18

- **In one sentence**: The paper proves a central limit theorem for the number of distinct prime factors of floor(alpha n^2) over n up to N, for irrational alpha, and fully describes the distribution for rational alpha.
- **In plain words**: The paper asks how many different prime numbers divide a number of the form (a fixed positive number times n squared), rounded down, when n is picked at random from 1 to N. The authors show that after a standard rescaling, this count behaves like a bell-shaped (Gaussian) random variable as N grows, when the fixed number is irrational. They also work out the exact behaviour when the fixed number is a positive rational.
- **Why it matters**: This extends a classical line of results, in the style of the Erdos-Kac theorem for ordinary integers, to a sequence built from quadratic expressions with irrational scaling. The text does not say what applications it has, so its wider significance beyond this area is unclear to me.
- **Background needed**: - Prime number: a whole number greater than 1 divisible only by 1 and itself.
- omega(m): the number of distinct primes dividing m (e.g. omega(12) = 2, since 12 = 2^2 times 3).
- Typical size: omega(m) for a typical m up to N is about log log N, a result going back to Hardy and Ramanujan.
- Gaussian (normal) distribution: the familiar bell curve; convergence in distribution means the histogram of the rescaled values approaches this curve as N grows.
- Irrational vs rational: an irrational number cannot be written as a fraction of integers; a rational can. The two cases behave differently here.
- Floor function: floor(x) is the largest whole number not exceeding x. · level: research-level

<details><summary>Original abstract</summary>

Let $\alpha > 0$ be irrational. We show that $\omega(\lfloor\alpha n^2\rfloor)$ obeys a Gaussian distribution. That is, for $n$ chosen uniformly at random from $\{1,\ldots,N\}$, the random variable $(\omega(\lfloor\alpha n^2\rfloor) - \log\log N)/\sqrt{\log\log N}$ converges in distribution to the standard Gaussian as $N$ tends to infinity. Additionally, we fully describe the distribution of $\omega(\lfloor\alpha n^2\rfloor)$ for a positive rational $\alpha$.

</details>

## Algebraic geometry

### [Semiorthogonal decompositions of limit categories for symmetric stacks](https://arxiv.org/abs/2611.33771)
*Yukinobu Toda* · `math.AG` · arXiv:2611.33771v1 · relevance 0.14

- **In one sentence**: The paper extends limit categories, previously defined for derived stacks with self-dual cotangent complexes, to a broader class called symmetric stacks, and establishes compact generation, semiorthogonal decompositions, functoriality, and a Künneth formula for them.
- **In plain words**: This paper is about a technical construction in algebraic geometry: a way of attaching a category (a structured collection of objects and maps between them) to a geometric space of solutions to a moduli problem. The authors broaden an earlier version of this construction to a wider class of spaces, which they call symmetric stacks. They then prove several general structural properties of these categories, and a companion paper uses them to state a conjecture.
- **Why it matters**: The motivation given is to support Dolbeault geometric Langlands-type correspondences for a wider range of moduli stacks, which is a long-running program linking geometry and representation theory. The text does not show any concrete new consequence beyond the structural results listed, so the wider impact is best treated as a possibility rather than an established outcome.
- **Background needed**: - Moduli stack: a geometric object that parametrizes families of mathematical objects (such as vector bundles or sheaves) together with their symmetries.
- Derived stack: a refinement of a moduli stack that keeps track of extra homological information, used to handle spaces that are not smooth.
- Cotangent complex: a homological object encoding the infinitesimal shape of a space; "self-dual" means it matches its own dual, a symmetry the paper generalizes.
- Category (in this sense): a collection of objects with maps between them, here built as a limit over a family of such categories.
- Semiorthogonal decomposition: a way of splitting a category into simpler pieces that interact in a controlled order.
- Langlands program: a web of conjectures connecting number theory, geometry and representation theory; the Dolbeault version concerns Higgs bundles and sheaves on curves or surfaces.
- Künneth formula: a rule relating the invariants of a product of spaces to those of the factors. · level: research-level

<details><summary>Original abstract</summary>

In our earlier work with Tudor Padurariu, we introduced the notion of limit categories for derived stacks with self-dual cotangent complexes and used them to formulate the Dolbeault geometric Langlands conjecture. In this paper, we generalize the notion of limit categories to a broader class of derived stacks, which we call symmetric stacks. One of the motivations for this generalization is to formulate Dolbeault geometric Langlands-type correspondences for a broader class of moduli stacks. We establish several fundamental properties of limit categories for symmetric stacks, including compact generation, the existence of semiorthogonal decompositions, functoriality, and a Kunneth formula. In a companion paper, we apply the results of this paper to formulate a Dolbeault geometric Langlands-type conjecture for moduli stacks of sheaves on smooth surfaces with nef anticanonical divisors.

</details>

### [Primitive Collections for Klyachko Varieties](https://arxiv.org/abs/2611.33491)
*Nicole Lemire, Jason Palombaro* · `math.AG` · arXiv:2611.33491v1 · relevance 0.09

- **In one sentence**: The paper determines the maximal cones, primitive collections, cohomology ring, and orbit-stability properties of the fan for Klyachko toric Gorenstein Fano varieties X_{mn} when n is congruent to 1 modulo m.
- **In plain words**: This paper studies a family of geometric shapes built from pieces of a higher-dimensional grid, called Klyachko varieties. The authors focus on the cases where one parameter is one more than a multiple of the other, and they describe the basic building blocks (maximal cones and primitive collections) that define these shapes. They also describe the algebraic bookkeeping (cohomology ring) attached to them and some results about how symmetric groups act on these blocks.
- **Why it matters**: Klyachko varieties link toric geometry to representation theory, algebraic groups and graph theory, and the generalized del Pezzo special case already supports results on derived categories. The text does not claim wider consequences, so the value here is mainly as a structural description of a known family.
- **Background needed**: - Toric variety: a geometric object built from a collection of cones (a "fan") in space, so that combinatorics of the fan controls the geometry.
- Fano variety: a space whose anticanonical bundle is positive, loosely a "positively curved" shape; Gorenstein is a mild regularity condition.
- Maximal cone and primitive collection: the basic combinatorial pieces of a fan that determine its structure.
- Cohomology ring: an algebraic invariant recording how the space's pieces intersect.
- Symmetric group action: permutations of coordinates (S_m × S_n) acting on the variety.
- Rationality and stable rationality: whether the space can be parametrized by rational functions, in a weak or strong sense.
- Generalized del Pezzo variety: a centrally symmetric member of this family, X_{2,2k+1}. · level: research-level

<details><summary>Original abstract</summary>

Klyachko introduced a family of $S_m\times S_n$-invariant toric Gorenstein Fano varieties, $X_{mn}$, with connections to representation theory, algebraic groups, and graph theory. He focused on the case in which $m$ and $n$ are coprime, for which $X_{mn}$ are smooth, and hence Fano. Klyachko and Voskresenskii later proved that all forms of $X_{mn}$ are stably rational when $m, n$ are coprime, and that all forms of $X_{mn}$ are rational when $n$ is congruent to 1 modulo $m$. In the same paper, they classified centrally symmetric toric Fano varieties as products of projective lines and generalized del Pezzo varieties, $X_{2,2k+1}$. For this reason, the special case of generalized del Pezzo varieties are frequently studied. For example, Ballard, Duncan, and McFadden proved that the bounded derived category of generalized del Pezzo varieties has a full exceptional collection of line bundles. An understanding of the maximal cones and primitive collections of the fan associated to $X_{2,2k+1}$ is crucial in their construction. In this paper, we focus on the Klyachko varieties $X_{mn}$ in the case in which $n$ is congruent to 1 modulo $m$. We determine a description of the maximal cones and primitive collections for the associated fan. We also determine a description of their cohomology ring and some stability results on the $S_m\times S_n$-orbits of maximal cones and primitive collections for $X_{mn}$.

</details>

## Topology

### [Graded Monoidal Categories and Internalization](https://arxiv.org/abs/2611.33663)
*Bryce Goldman* · `math.CT` · arXiv:2611.33663v1 · relevance 0.15

- **In one sentence**: The paper gives a general categorical framework for internalizing a graded monoidal product, studies its 2-categorical properties, and recovers Day convolution and the smash product of S-modules as examples.
- **In plain words**: Mathematicians who study stable homotopy theory (a branch of topology that treats spaces through their "stable" behavior) have several ways to build a point-level product of spectra, which are objects that generalize spaces. Each construction has trade-offs, and they often follow a similar pattern of turning a product indexed by grading labels into a single product. This paper packages that shared pattern into one general framework so the constructions can be compared in a common language.
- **Why it matters**: The text presents this as a unifying framework rather than a new result on a specific problem, so its value lies mainly in clarifying how several known constructions relate. It may matter to researchers who build multiplicative structures on spectra, though the text does not say more about its wider impact.
- **Background needed**: - Monoidal category: a category with an associative product and a unit, like multiplication of numbers or tensor of vector spaces.
- Graded object: a family of pieces indexed by labels (grades), such as a sequence indexed by integers or by a group.
- External vs. internal product: an external product combines objects from different sources into a graded-indexed object; internalizing it turns this into a product within a single category.
- Spectrum: a generalized space used in stable homotopy theory, where classical homotopy operations become well behaved.
- Day convolution: a standard way to multiply functors on a monoidal category.
- 2-category: a setting with objects, morphisms between them, and morphisms between morphisms. · level: research-level

<details><summary>Original abstract</summary>

In stable homotopy theory, there are a variety of ways to construct a point-set level smash product of spectra, each with its own advantages and limitations. These constructions often involve internalizing some graded external product. In this paper, we aim to formalize this process through a general categorical framework, providing a common language for these constructions. We propose a general theory for internalizing a graded monoidal product, investigate its 2-categorical properties, and use this framework to recover both Day convolution and the smash product of $S$-modules.

</details>

### [Norm groups of orders and the algebraic unknotting number](https://arxiv.org/abs/2611.34200)
*Maciej Borodzik, Wojciech Politarczyk* · `math.GT` · arXiv:2611.34200v1 · relevance 0.13

- **In one sentence**: The paper gives an explicit, computable obstruction, based on norm groups of orders from algebraic number theory, that can rule out a knot having algebraic unknotting number one, and uses it to show that T(2,5) # -T(2,3) has algebraic unknotting number one while T(2,5) has algebraic unknotting number two.
- **In plain words**: The paper studies knots, which are closed loops of string tangled in space, and asks how few "crossing changes" of a special algebraic kind are needed to untangle one into a plain circle. The authors use tools from number theory to build a test that can show a knot cannot be undone this way with a single change. As an example, they show that joining a cinquefoil knot to a mirror-image trefoil gives a knot that can be undone with one change, even though the cinquefoil alone needs two.
- **Why it matters**: The result shows that combining two knots can make the simplest-untangling count drop, which is a notable and concrete fact about this measure. The text does not say how far the method reaches beyond the example, so its wider importance is unclear from the abstract alone.
- **Background needed**: - Knot: a closed loop of string embedded in three-dimensional space; the goal is to classify knots up to deformation.
- Unknotting number: the minimum number of crossing changes needed to turn a knot into the unknot (a plain circle).
- Algebraic unknotting number: a variant where the allowed changes are restricted to algebraic ones, tied to the knot's algebraic structure.
- Connected sum: a way of joining two knots into one new knot.
- T(2,3) and T(2,5): torus knots, the trefoil and cinquefoil; "negative" means the mirror image.
- Number theory tools: norm groups of orders are objects from algebraic number theory (fields of algebraic numbers and their integer-like subrings) used here as an invariant. · level: research-level

<details><summary>Original abstract</summary>

We use number-theoretic tools to find an explicit and effective obstruction for a knot to have algebraic unknotting number equal to $1$. As an example, we show that the connected sum of $T(2,5)$ (the cinquefoil) and $-T(2,3)$ (the negative trefoil) has algebraic unknotting number $1$, even though $T(2,5)$ has algebraic unknotting number $2$.

</details>

## Dynamical systems

### [Entropic continuity of Lyapunov exponents in arbitrary dimension](https://arxiv.org/abs/2611.34165)
*David Burguet, Gang Liao, Yao Tong* · `math.DS` · arXiv:2611.34165v1 · relevance 0.18

- **In one sentence**: The paper proves entropic continuity of the sum of positive Lyapunov exponents for C^∞ diffeomorphisms in arbitrary dimension under an entropy gap condition, extending Buzzi, Crovisier and Sarig's result, and shows the condition is sharp.
- **In plain words**: This paper studies how the chaos of a system that evolves by repeated rule-based motion (a smooth map of a space onto itself, such as a stirred fluid or a planetary-style orbit model) changes when the rule is slightly altered. It shows that, under a stated condition on the system's entropy (a measure of how much complexity or unpredictability it has), a key chaos measure called the sum of positive Lyapunov exponents varies continuously. The authors also give examples showing the condition cannot simply be dropped.
- **Why it matters**: Continuity of these chaos measures under small changes matters for knowing whether a model's predicted behaviour is robust to small errors in its description. The text links the work to the Newhouse phenomenon and to standard maps, but the abstract does not show how far these applications go.
- **Background needed**: - Diffeomorphism: a smooth, invertible map of a space to itself, viewed as one step of a discrete-time evolution.
- Lyapunov exponents: rates at which nearby trajectories separate exponentially; positive ones signal chaos.
- Topological and measure-theoretic entropy: measures of how complex or unpredictable a system's orbits are, counted in total or under a particular statistical measure.
- Continuity (in this setting): small changes to the map cause only small changes to the quantity.
- Ergodic measure of maximal entropy: a statistical description of the system's typical long-run behaviour that carries the largest possible entropy.
- Upper semicontinuity: a one-sided form of continuity where the quantity can jump up only in the limit, never suddenly down.
- Newhouse phenomenon: the appearance of infinitely many stable structures near a system with a tangency, a known source of complex behaviour.
- Standard map: a simple model from physics of area-preserving motion, often used to study chaos. · level: research-level

<details><summary>Original abstract</summary>

We prove that the sum of the positive Lyapunov exponents is entropically continuous for every $C^\infty$ diffeomorphism, provided the entropy exceeds its second-largest exterior growth rate. We also establish stable strong positive recurrence and show that the topological entropy is continuous, and the number of ergodic measures of maximal entropy is upper semicontinuous. This extends the result of Buzzi, Crovisier, and Sarig to arbitrary dimensions. We give examples in both the measure-theoretic and topological senses, showing that this entropy gap condition is sharp. We also present applications related to the Newhouse phenomenon and standard maps.

</details>

### [From Limit Theorems to Mixing Limit Theorems](https://arxiv.org/abs/2611.34103)
*Jianshu Jiang* · `math.DS` · arXiv:2611.34103v1 · relevance 0.15

- **In one sentence**: The paper gives an alternative proof, under weaker assumptions, of an Arana-Herrera–Forni result that turns ordinary limit theorems for cocycles over dynamical systems into mixing limit theorems, following Gouëzel's approach.
- **In plain words**: The paper is about a general technique in the study of chaotic, evolving systems: taking a known "limit theorem" (a statement about how averages or fluctuations behave over long times) and upgrading it into a stronger "mixing" version that also holds jointly with the system's own dynamics. The authors re-prove an existing result of Arana-Herrera and Forni with fewer assumptions, using an approach inspired by Gouëzel's earlier work.
- **Why it matters**: The text is short, so its scope is hard to judge beyond the abstract. Its value is mainly methodological: it shows the same upgrading result holds under weaker conditions, which may make the tool applicable to more systems.
- **Background needed**: - Dynamical system: a rule that moves points forward in time, such as a map or flow.
- Cocycle: a quantity attached to each step of the dynamics (for example, a running total or a matrix product) that accumulates along orbits.
- Limit theorem: a statement describing the long-run behaviour of such accumulated quantities, such as a central limit theorem for fluctuations.
- Mixing: the property that the system forgets its initial state, so distant-in-time events become roughly independent.
- Mixing limit theorem: a limit theorem that holds in this "forgetful" sense, jointly with the dynamics.
- Background papers: prior work by Gouëzel and by Arana-Herrera and Forni, which the text does not describe. · level: research-level

<details><summary>Original abstract</summary>

Following the work of Gou\"ezel, we give an alternative proof, under weaker assumptions, of a result of Arana-Herrera and Forni, which provides a general method for upgrading limit theorems for cocycles over dynamical systems to mixing limit theorems.

</details>

## Combinatorics

### [From random intersection to spatial graphs: a unified asymptotic framework](https://arxiv.org/abs/2611.33423)
*Alessandra Bianchi, Alberto De Nicol\`o, Riccardo Michielan* · `math.PR` · arXiv:2611.33423v1 · relevance 0.15

- **In one sentence**: The paper studies geometric random intersection graphs, where spatially placed vertices connect when they share a located group, deriving exact subgraph probabilities, clustering formulas, and convergence to several standard random graph models.
- **In plain words**: This paper looks at networks built from points scattered in space, where two points are linked if they both belong to a shared group placed nearby. The authors work out exact formulas for how often small patterns of links appear and how clustered the network is, which is the tendency of friends-of-friends to also be connected. They also show that under certain settings the network approaches well-known simpler random network models, while noting that its clustering may not settle to the same value as the simpler model.
- **Why it matters**: Clustering is a central feature of real social and spatial networks, and this work clarifies how two common mechanisms for creating it, shared groups and spatial closeness, relate to each other. The text does not indicate specific applications, so the practical reach beyond probability theory is unclear from the abstract alone.
- **Background needed**: - Random graph: a network generated by a random rule, studied through averages as it grows large.
- Random intersection graph: vertices are linked when they share a group they have each joined.
- Spatial random graph: vertices are points in space, linked more often when they are close.
- Clustering: how often two neighbours of a node are also neighbours of each other (triangles).
- Poisson process: a standard random scattering of points with a given density.
- Convergence / limit: showing that a model's statistics approach those of a simpler model as a parameter changes.
- Erdős–Rényi graph: the simplest random network, where every pair is linked independently with equal chance. · level: research-level

<details><summary>Original abstract</summary>

Random intersection graphs and spatial random graphs provide different mechanisms for generating edges and clustering. We investigate their interplay through geometric random intersection graphs, where vertices are adjacent whenever they share a spatially located group. First, a Poisson decomposition by attachment sets yields exact subgraph probabilities and laws of large numbers for connected subgraph densities. It distinguishes triangles supported by a common group from those requiring three distinct groups. Second, explicit representations of global and average local clustering reveal their different dependence on model parameters and the role of shared groups in edge correlations. Finally, by varying the strength and spatial range of group memberships, we establish convergence to random connection, random geometric, random intersection, Erd\H{o}s--R\'enyi, and complete graphs. We characterize the corresponding clustering limits and show that clustering need not converge to that of the limiting graph, highlighting the distinction between spatially local convergence and global graph statistics.

</details>

### [Graceful Colorings for Random Graphs](https://arxiv.org/abs/2611.33427)
*Sean English, Edward Janosko, Erik Slivken et al.* · `math.CO` · arXiv:2611.33427v1 · relevance 0.15

- **In one sentence**: This paper determines, up to the order of magnitude, the graceful coloring number of Erdős–Rényi random graphs across three density regimes, using Salem–Spenser sets, forbidden submatchings, and the chromatic number of the graph's square.
- **In plain words**: The paper studies how many colors are needed to label the points of a randomly generated network so that two rules hold: neighboring points get different colors, and every link gets a distinct "color" given by the difference between its endpoints' labels. It looks at random networks of three kinds, depending on how many links they have. For each kind it gives an estimate of the number of labels needed.
- **Why it matters**: The results give concrete growth rates for a combinatorial quantity on random graphs, which is a standard test case in the field. The text does not say how the results bear on applications beyond this area, so any wider significance is unclear from the text alone.
- **Background needed**: - Graph: a set of vertices (points) joined by edges (links).
- Random graph G(n,p): n vertices, each pair joined independently with probability p.
- Proper vertex coloring: adjacent vertices get different colors.
- Proper edge coloring: edges sharing an endpoint get different colors.
- Graceful coloring: vertex colors from 1..k such that edge labels |c(u)−c(v)| are all distinct at each vertex.
- Diameter: the longest shortest path between any two vertices; diameter 2 means every pair is within two steps.
- Salem–Spenser sets: sets of integers with no nontrivial three-term relations of a certain type, used here as a tool.
- Asymptotic notation: n^{1+o(1)} means up to factors that are subpolynomial in n; Θ means growth of the same order up to constant factors. · level: research-level

<details><summary>Original abstract</summary>

Given a vertex coloring $c:V(G)\to [k]$, the graceful induced edge labeling is the induced edge coloring $c'(uv):=|c(u)-c(v)|$. A vertex coloring $c$ is a \textbf{graceful coloring} if $c$ is a proper vertex coloring and $c'$ is a proper edge coloring. The graceful coloring number $\chi_g(G)$ is the least $k$ such that there exists a graceful coloring $c:V(G)\to [k]$. We study the graceful coloring number for the Erd\H{o}s-Renyi random graph, $G_{n,p}$. In the diameter $2$ regime, we find the $\chi_g(G_{n,p})=n^{1+o(1)}$ using a connection between graceful colorings and Salem-Spenser sets. In the regime where $G_{n,p}$ is connected, but not diameter 2, we find that $\chi_g(G_{n,p})=\Theta\left(\frac{n^2p^2}{\log np}\right)$, using the forbidden submatching method and a connection between graceful coloring and the chromatic number of the square of $G_{n,p}$. Finally, in the regime where $G_{n,p}$ has constant average degree, we find that $\chi_g(G_{n,p})=\Delta(G_{n,p})+1$, by exploring the cycle structure of $G_{n,p}$.

</details>

## Numerical analysis

### [Structure-preserving finite element method for the 2D MHD-$\alpha$ turbulence system](https://arxiv.org/abs/2611.34410)
*Patrick E. Farrell, Mingdong He, Kaibo Hu* · `math.NA` · arXiv:2611.34410v1 · relevance 0.15

- **In one sentence**: A structure-preserving finite element scheme for the 2D MHD-alpha model, which smooths the transport velocity at length alpha while keeping the ideal invariants, with an augmented Lagrangian preconditioned multigrid solver and checks against a pseudo-spectral simulation of the original MHD equations.
- **In plain words**: The paper studies computer simulation of electrically conducting fluids, such as plasmas, in two dimensions, where the flow is turbulent and hard to resolve on a grid. The authors smooth the fluid's transport velocity over a chosen length scale, and build a numerical method that keeps key conserved quantities, such as mass and the magnetic Gauss law, exact at every grid point and dissipates the others in a controlled way. They report that the method converges at the expected rates, matches a reference simulation at large scales, and avoids the buildup of energy at the smallest grid scale that occurs without the smoothing.
- **Why it matters**: Unphysical energy piling up at the smallest scales is a common failure of simulations of turbulence, so a method that controls it while respecting conservation laws is of interest to people building plasma and fluid codes. The text does not indicate applications beyond this model, and its reach to three-dimensional or real plasma problems is not addressed here.
- **Background needed**: - Magnetohydrodynamics (MHD): equations describing conducting fluids coupled to magnetic fields, used for plasmas and astrophysical flows.
- Invariants: quantities such as energy, cross helicity and magnetic potential that the exact equations conserve, or in the model, dissipate in a controlled way.
- Finite element method: a standard way to turn partial differential equations into solvable algebraic systems on a mesh.
- Structure-preserving: a numerical scheme designed so that conservation laws hold exactly at the discrete level.
- Filter width alpha: the length scale below which the transport velocity is smoothed in the model.
- Multigrid and preconditioners: fast iterative solvers that work on coarse and fine grids to handle large linear systems.
- Pseudo-spectral simulation: a high-accuracy reference method that uses Fourier modes to represent the flow.
- Selective decay and inverse cascade: turbulence phenomena in which some quantities decay while energy moves toward large scales. · level: research-level

<details><summary>Original abstract</summary>

We propose a structure-preserving finite element method for the two-dimensional MHD-$\alpha$ turbulence model, which filters the transport velocity at a length $\alpha$ while retaining the ideal invariants of the original MHD equations, with the energy replaced by an $\alpha$-dependent energy. The scheme preserves mass conservation and the magnetic Gauss law pointwise and satisfies discrete dissipation laws for the energy, the cross helicity and the mean square magnetic potential, which reduce to exact conservation in the ideal limit. The discrete systems are solved by an augmented Lagrangian preconditioner with monolithic geometric multigrid, observed to be robust with respect to the filter width $\alpha$ and the Reynolds numbers, and to the mesh size for small time steps. The scheme converges at the optimal rates and agrees with a Fourier pseudo-spectral direct simulation of the original MHD equations at the large scales. In under-resolved flows, the unfiltered scheme has no numerical dissipation and accumulates energy at the grid scale. Filtering relieves this accumulation and a larger $\alpha$ gives a more compact spectrum. Long-time simulations reproduce selective decay, including relaxation toward the Arnold-type bound and the inverse cascade of the mean square potential.

</details>

### [FokasNets: Completing missing boundary data in Physics-Informed Neural Networks and Operators via the Global Relation](https://arxiv.org/abs/2611.33549)
*Kyriakos C. Georgiou, Khemraj Shukla, Athanassios S. Fokas et al.* · `math.NA` · arXiv:2611.33549v1 · relevance 0.15

- **In one sentence**: FokasNets adds the Fokas method's Global Relation as an extra training constraint to lifted PINNs and PINO-style operator networks, so that missing boundary data for mixed boundary-value PDE problems is supplied during training.
- **In plain words**: Scientists often want a computer model to solve equations that describe physical systems, such as heat flow or waves, but they need to know the values at the edges of the region, and those edge values are sometimes missing. This paper proposes FokasNets, which uses a known mathematical identity (the Global Relation from the Fokas method) during training to fill in those missing edge values. The authors report that this improves accuracy both inside the region and at its boundaries, with the largest gains for models that learn whole families of solutions.
- **Why it matters**: Neural networks that solve differential equations often struggle with boundary conditions, so a way to supply missing ones could matter for scientific machine learning. The text reports accuracy gains on manufactured solutions and literature benchmarks, along with universal approximation and error/stability analysis, but the strength of these claims depends on experiments I cannot check from the abstract alone.
- **Background needed**: - Partial differential equations (PDEs): equations relating a function to its rates of change in space and time; they describe heat, waves, fluids, and similar phenomena.
- Boundary conditions: values or constraints imposed on the edges of the domain; "Dirichlet" means the values on the edge are fixed.
- Physics-Informed Neural Networks (PINNs): neural networks trained to satisfy a PDE and its boundary conditions by penalizing errors in the loss function.
- Neural operators (PINOs, DeepONets): networks that learn the map from inputs (such as source terms or initial data) to whole solutions, rather than a single solution.
- Lifted representation: building the boundary values into the network's form so the network only learns the correction in the interior.
- Fokas method (Unified Transform): an analytic technique for solving boundary-value PDEs; its Global Relation links the unknown boundary data together.
- Universal approximation: a theoretical result that a network can approximate a target function arbitrarily well. · level: research-level

<details><summary>Original abstract</summary>

We introduce FokasNets, a framework that combines Physics-Informed Neural Networks (PINNs) and operators (PINOs) with the Global Relation (GR) formulation of the Fokas method (also referred to as the Unified Transform), for mixed boundary problems. The general framework considers lifted representations of the neural network models, where the Dirichlet boundary conditions are imposed by construction and the neural network learns the interior correction. The Global Relation is used as an additional solve during training that provides the missing boundary conditions to the lifted neural network, making training more efficient and accurate in the interior and on the boundary. We develop the construction of FokasNets for elliptic and evolution PDEs (Fokas-PINNs), and the corresponding PDE solution operator problems (Fokas Operator Networks - FONets), using the Global Relation formulations for these PDE classes. Furthermore, we develop the necessary theoretical framework for FokasNets, including error and stability analysis and show that FokasNets are universal approximators. We provide comprehensive numerical experiments, using examples with manufactured solutions and literature benchmarks. Compared to standard PINNs and Physics-Informed DeepONets and their lifted versions, FokasNets achieve significant improvements in solution accuracy in the interior and boundaries, both for single PDEs and particularly for solution operators, where the improvement reaches multiple orders of magnitude and fixed threshold errors are reached faster during training.

</details>

## Logic and foundations

### [A family of forcings with hyperfinite equivalence of generics](https://arxiv.org/abs/2611.34109)
*Ben De Bondt* · `math.LO` · arXiv:2611.34109v1 · relevance 0.26

- **In one sentence**: The paper identifies a class of set-theoretic forcing notions, including several classical ones, and shows that for each forcing in that class the equivalence-of-generics relation of Smythe is a hyperfinite countable Borel equivalence relation (CBER).
- **In plain words**: This is about the logical foundations of mathematics, specifically a technique called forcing, which builds new mathematical universes by adding "generic" objects that dodge all prescribed obstacles. The authors look at when two such generic objects count as equivalent, and they group many well-known constructions into one class. For every construction in that class, they show the equivalence is "hyperfinite," meaning it can be approximated by a sequence of finite pieces.
- **Why it matters**: The work places a family of classical constructions under a single structural description, which may help compare them. Its connection to descriptive set theory (the study of how definable sets of reals can be classified) is the reason it matters to specialists; the text does not say what further applications it has, so the wider significance is uncertain.
- **Background needed**: - Forcing: a method from set theory for extending a model of mathematics by adding a "generic" object that meets every dense condition.
- Generic object: an object that avoids all exceptional sets that could be specified in advance in the model.
- Equivalence of generics: a relation saying when two generics yield the same information or are interchangeable, as defined by Smythe (the text gives no further detail).
- Borel equivalence relation: a way of sorting points of a Polish space into classes where the sorting rule is simple enough to be "Borel" (definable from open sets by countable operations).
- Countable Borel equivalence relation (CBER): a Borel equivalence relation whose classes are countable.
- Hyperfinite: a CBER that is an increasing union of finite-class equivalence relations; intuitively, it is as tame as countable classification gets.
- Background in set theory and descriptive set theory at graduate level is needed. · level: research-level

<details><summary>Original abstract</summary>

We identify a class of forcings that includes several classical forcings and prove that for all forcings $\mathbb{P}$ in this class the associated equivalence of generics relation $\equiv^{\mathbb{P}}_M$, as defined by Smythe, is a hyperfinite CBER.

</details>

### [Stability in abstract classes via set theoretic techniques](https://arxiv.org/abs/2611.33530)
*Jeremy Beard, Marcos Mazari-Armida* · `math.LO` · arXiv:2611.33530v1 · relevance 0.17

- **In one sentence**: The paper shows that abstract elementary classes with an independence relation satisfying a mild local character condition are stable, and applies this to classes of modules closed under pure submodules.
- **In plain words**: This is a paper in mathematical logic about "abstract classes," which are collections of mathematical structures with a notion of substructure, such as classes of modules (algebraic objects like vector spaces, generalized). The authors prove that such classes behave in a tame, orderly way ("stable") whenever a certain notion of independence has a mild local property. They reach this using tools from model theory and set theory.
- **Why it matters**: The result says that a broad family of structures is orderly under a fairly weak assumption, which matters for classifying what such theories can look like. The text does not say how far beyond the module examples the result reaches, so its wider impact is unclear from this summary alone.
- **Background needed**: - Abstract classes: collections of structures with a chosen notion of embedding, generalizing first-order model theory.
- Independence relation: an abstract analogue of "independence" from linear algebra or probability, saying when two parts of a structure are unrelated given a base.
- Local character: a condition that every element depends only on a small piece of the structure.
- Stability (in a cardinal λ): a measure of tameness; roughly, the number of distinct ways to describe objects of size λ is controlled, rather than exploding.
- Modules and pure submodules: modules are generalized vector spaces over a ring R; a pure submodule is one that respects linear equations with parameters in it.
- Cardinal arithmetic: the condition λ^(card(R)+ℵ₀) = λ is a size-related assumption about infinite cardinal numbers. · level: research-level

<details><summary>Original abstract</summary>

We prove that all abstract classes equipped with an independence relation satisfying a mild local character condition are stable. We obtain the result by using methods from model theory and set theory. We have several applications in the context of abstract classes of modules. In particular, we prove that if $K$ is a class of $R$-modules closed under isomorphisms and pure submodules and $\lambda^{\operatorname{card}(R) + \aleph_0} = \lambda$, then $K$ equipped with pure embeddings is stable in $\lambda$.

</details>

## Mathematical physics

### [Quantum limit cycles from phase coupling: A framework for NISQ thermodynamic devices](https://arxiv.org/abs/2610.15905)
*Nana Siddhartha* · `quant-ph` · arXiv:2610.15905v1 · relevance 0.12

- **In one sentence**: The paper quantises the Kuramoto model and a Van der Pol oscillator, couples them to one or more qubits, and reports a robust quantum limit cycle plus effects it calls entanglement state revivals, Zeno locking and thermal current interference.
- **In plain words**: Tiny quantum devices tend to lose their delicate behaviour to heat and noise, so they usually need outside control. This paper proposes coupling a quantum bit (qubit) to a self-sustaining rhythmic system, so the two lock into a steady cycle, which the authors argue could keep working without that outside help. The text reports that this locking holds up even in typical quantum heat-engine settings, and it describes several effects seen in the model.
- **Why it matters**: The idea of using synchronisation, the way clocks or fireflies lock their rhythms, as a source of stable behaviour in quantum devices may be useful for designing small quantum machines. The text is a theoretical proposal with toy models, and it gives no experimental test, so its practical value is unconfirmed.
- **Background needed**: - Qubit: the quantum version of a bit, which can sit in superpositions and entangled states.
- Decoherence: the loss of quantum behaviour when a system interacts with its environment, such as heat.
- Limit cycle: a self-sustaining steady oscillation, like a pendulum clock kept running by a mechanism.
- Kuramoto model: a classic model of many oscillators pulling each other into step.
- Van der Pol oscillator: a standard model of a self-driven electronic oscillator.
- Quantum thermodynamics: the study of heat, work and energy flow in quantum systems.
- Entanglement: a strong correlation between quantum systems that persists regardless of distance.
- Zeno effect: frequent measurement slowing a quantum system's evolution.
- The text uses "Spectral Mechanics" as its framework and gives no detail on it, so the foundational claims cannot be checked from this text alone. · level: research-level

<details><summary>Original abstract</summary>

Quantum decoherence does not permit the operation of (new) miniaturised devices or protocols that can otherwise run unassisted in classical settings, without explicit user agent intervention in the quantum realm. Classical driving signals are inadequate to model a truly quantum device built entirely in the quantum realm. Synchronisation endures miniaturisation without sacrificing quantum coherence, unlike thermalisation. We quantise the Kuramoto model and the Van der Pol oscillator and couple it with qubit(s) to show a robust limit cycle even in typical quantum thermodynamical settings. Novel effects such as Entanglement State Revivals, Zeno locking and thermal current interference are observed. We propose toy model devices that can be implemented harnessing the Synchronisation of a qubit (or an arbitrary collection of qubits) with a nonlinear phase oscillator. The framework theory used here, Spectral Mechanics, is a fresh look at the foundations of conventional quantum mechanics and is extensible to completely new forms of interactions and models in experimental settings.

</details>

### [Higher derivatives and ghosts through three centuries](https://arxiv.org/abs/2611.34097)
*Andrei Smilga* · `hep-th` · arXiv:2611.34097v1 · relevance 0.10

- **In one sentence**: A historical review of higher-derivative field theories and "benign" ghost (negative-norm) modes, covering examples in quantum mechanics, 2D field theory, classical and quantum higher-derivative gravity in 4D, and supersymmetric theories in 6D.
- **In plain words**: This review traces about three centuries of work on physical systems whose equations involve higher rates of change, such as accelerations and their rates, starting with Euler in 1744. A long-standing belief was that such systems must break unitarity, the rule that probabilities stay sensible. The author argues that this belief was a misconception, presents several examples where so-called ghost modes are harmless, and says where the question remains open.
- **Why it matters**: It corrects a widely held view that shaped decades of research, and it links older mechanics work to modern questions about gravity and quantum theory. The text itself says the status of ghosts in quantum 4D higher-derivative gravity has no definite answer yet, so that part remains unresolved.
- **Background needed**: - Lagrangian: a function whose variation gives the equations of motion; "higher derivatives" means the equations involve accelerations or beyond.
- Ghost: a mode with negative norm or energy, which can threaten a theory's consistency.
- Unitarity: the requirement that probabilities add up to one, so the theory gives sensible predictions.
- "Benign" ghost: a ghost that does not cause unitarity violation or instability in practice.
- Ostrogradsky (1850) and Pais–Uhlenbeck (1950): classic papers on higher-derivative systems.
- Conformal supergravity and renormalizability: advanced field-theory frameworks; the text mentions them only briefly.
- Nonperturbative Hamiltonian: a full quantum energy operator that is not built from a small-coupling expansion. · level: research-level

<details><summary>Original abstract</summary>

We outline the history of the research of dynamic systems including higher derivatives in the Lagrangian, The story starts in 1744 when Euler published a book where the Euler--Lagrange differential equations for a HD system were first written. The next important landmarks were the papers of Ostrogradsky (1850) and of Pais and Uhlenbeck (1950). Many articles written in the second half of the last century were influenced by a misconception that was widespread at the time --- it was believed that higher derivatives necessarily bring about a violation of unitarity. We understand today that this is not the case and there are many systems with benign ghosts where HD are present but unitarity is not violated. In this review, we present and discuss several examples of such (quantum) mechanical systems and 2D field theories. Then we will briefly discuss higher-derivative gravity theories in 4 dimensions. In that case, the question whether the ghosts there are benign or not has a special status due to the absence of a nonperturbative Hamiltonian and does not have a definite answer yet. However, if one restricts oneself to classical theory, one can argue that the ghosts {\it are} benign (benign classical ghostly system is a system that needs an infinite time to reach a singularity, and it seems to the case both in ordinary and in HD gravity: the cosmic censorship conjecture implies that the singularities are always surrounded by horizons, and it takes an infinite time on the clocks of a distant observer to reach a horizon). Finally, I discuss supersymmetric HD theories: conformal supergravity, where the ghosts are also probably benign, and then an interesting supersymmetric HD gauge theory in 6 dimensions. It involves a dimensionless coupling constant, is renormalizable and rather beautiful. Unfortunately, it is not unitary --- ghosts are not benign there.

</details>

## Optimization and control

### [Wasserstein-Fisher-Rao Reconstruction of Discrete space Population Dynamics](https://arxiv.org/abs/2611.33923)
*Junda Ying, Xinyu Wang, Peijie Zhou et al.* · `math.OC` · arXiv:2611.33923v1 · relevance 0.16

- **In one sentence**: The paper extends the dynamic Wasserstein-Fisher-Rao (unbalanced optimal transport) problem to discrete state spaces, derives a closed-form solution, and proposes an unbalanced discrete flow matching method as a numerical approximation for large or more general cases.
- **In plain words**: The paper studies how a population of cells changes over time when we only see snapshots of it at a few moments. Cells are grouped into coarse cell types, and the authors build a mathematical method that estimates a smooth, continuous-time path between those snapshots, allowing cells to be created or lost along the way. The authors report a closed-form solution for their framework, a numerical shortcut for very large problems, and tests on simulated and real biological data.
- **Why it matters**: Reconstructing how cell populations evolve from sparse measurements is a practical problem in developmental and disease biology, where cells cannot be tracked individually. The text does not say how the method compares with existing tools, so its practical advantage is not established here.
- **Background needed**: - Optimal transport: a way of finding the cheapest way to move one distribution of mass into another; "unbalanced" means mass can also appear or disappear.
- Wasserstein-Fisher-Rao: a specific unbalanced transport distance combining moving mass and growing or shrinking it.
- Discrete state space: the system is described by a finite set of categories (here, coarse cell types) rather than continuous positions.
- Flow matching: a machine-learning technique that learns a continuous-time path transforming one distribution into another; the discrete version works on categories.
- Markovian: the future depends only on the present state, not on the full history.
- Snapshot data: measurements taken at several time points without following the same individual cells over time. · level: research-level

<details><summary>Original abstract</summary>

Reconstructing the continuous time dynamics of cell state evolution from sparse snapshot observations can be formulated as an unbalanced optimal transport problem. To study such dynamics at a coarse grained cell type level, unbalanced optimal transport must be extended to discrete state spaces. Inspired by discrete flow matching, we extended the dynamic Wasserstein-Fisher-Rao (WFR) problem to discrete spaces, and derived a closed form for its solution. For particularly large state spaces or more general models, we proposed an unbalanced discrete flow matching as a numerical approximation method, which provides a Markovian reconstruction of the optimal WFR flow. Our discrete WFR framework also stays stable across different coarse grain resolution. Finally, numerical experiments demonstrated the effectiveness of the proposed approach, and applications to real biological data supported the plausibility of the reconstructed dynamics.

</details>

### [BGPNP: A Non-Euclidean Gradient Projection Newton Pursuit Method for Sparsity-Constrained Optimization](https://arxiv.org/abs/2611.33802)
*Jiawei Chen, Huilin Han, Yibing Lv et al.* · `math.OC` · arXiv:2611.33802v1 · relevance 0.15

- **In one sentence**: A non-Euclidean (Bregman-distance-based) gradient projection plus Newton pursuit method, called BGPNP, for minimizing an objective subject to a cap on the number of nonzero variables, with convergence results and compressed sensing experiments.
- **In plain words**: This paper studies a way to solve optimization problems where only a small number of variables are allowed to be nonzero, such as finding a sparse signal that fits measurements. The authors propose a two-stage iterative method: a gradient-based step that keeps the iterates within the sparsity limit, followed by a faster Newton-style step once the set of active variables has settled. They report that the method provably decreases the objective, converges, and does so at a fast local rate, and that it performs competitively on compressed sensing tests.
- **Why it matters**: Sparse optimization underlies many signal-recovery and data-compression tasks, so faster or more reliable solvers have practical value. The paper's main claimed contribution is convergence guarantees that avoid some restrictive conditions used in earlier work, though the text alone does not show how broadly these conditions are relaxed or how the method compares beyond the compressed sensing tests mentioned.
- **Background needed**: - Sparsity constraint: a rule that only a fixed small number of variables may be nonzero.
- Gradient method: iteratively moving downhill along the slope of the objective function.
- Projection: adjusting a point so it satisfies a constraint, here by keeping only the largest entries.
- Bregman distance: a generalized measure of distance between points that can replace the usual Euclidean (straight-line) distance, useful when geometry is not standard.
- Newton step: a update using curvature information that converges quickly near a solution.
- Convergence rates: "linear" and "quadratic" describe how fast the error shrinks per iteration; quadratic is much faster.
- Compressed sensing: recovering a sparse signal from fewer measurements than usual. · level: research-level

<details><summary>Original abstract</summary>

A non-Euclidean gradient projection Newton pursuit method is proposed for solving sparsity constrained optimization problem via the Bregman distance. The method is also denoted as BGPNP. The method firstly constructs a gradient projection step based on the Bregman distance to ensure that the iterates satisfy the sparsity constraint. Then, when the support set becomes stable or the gradient norm is sufficiently small, a Newton pursuit step is introduced to improve local convergence efficiency. The BGPNP is proved to possess a sufficient descent property and the non-increasing monotonicity of the objective function values. The full convergence and linear convergence rate of the BGPNP are established under appropriate conditions, which do not involve the symmetry coefficient of Bregman distance and the $\theta$-uniform condition. Moreover, the locally quadratical convergence rate of the BGPNP is also obtained. This method provides an effective algorithmic framework for sparse optimization in non-Euclidean setting. Numerical experiments on sparsity-constrained compressed sensing problems validate the competitive performance of BGPNP compared with existing leading solvers.

</details>

## Statistics theory

### [Certifying a Sufficient Gaussian Dependence Regime for Learned Weighted FDR Control](https://arxiv.org/abs/2611.33892)
*Soyeong Oh* · `stat.ME` · arXiv:2611.33892v1 · relevance 0.11

- **In one sentence**: The paper certifies, using reference data, that the joint Gaussian dependence among one-sided tests is mild enough for weighted Benjamini-Hochberg to control the false discovery rate, falling back to a prespecified procedure otherwise, and gives minimax sample-size bounds for this certification.
- **In plain words**: When many hypotheses are tested at once, researchers try to keep the share of false alarms among their discoveries small. This paper studies a version of that method where each test is given a learned weight, and the guarantee only holds if the test results are not too strongly correlated. The authors use separate reference data to check whether that condition is likely satisfied, and switch to a safer fallback procedure if it is not.
- **Why it matters**: Learned weights can add statistical power, but their validity depends on how the tests are related, which is often unknown in practice. The paper frames this as a sample-size question: how much reference data is needed to certify the condition, with the requirement growing only logarithmically in the number of pairs checked. The text does not indicate how the approach performs beyond the simulations and the Healthy Brain Network-based designs it reports.
- **Background needed**: - False discovery rate (FDR): the expected fraction of rejected hypotheses that are actually true nulls.
- Benjamini-Hochberg (BH) procedure: a standard step-up rule that controls FDR under certain dependence conditions; weighted versions multiply p-values by learned weights.
- Gaussian correlation: how strongly pairs of normally distributed test statistics move together; the sign and size of these correlations matter for validity.
- One-sided tests: tests that only look in one direction (e.g., effect greater than zero).
- Intersection-union test: a test that declares a conclusion only if every one of several sub-hypotheses is rejected.
- Minimax sample size: the smallest amount of data needed to guarantee a task succeeds in the worst case over allowed settings.
- Power: the probability of detecting a real effect. · level: research-level

<details><summary>Original abstract</summary>

Learning hypothesis weights from informative auxiliary data can improve the power of multiple testing. Even when the weights are learned independently of the tests, the validity of weighted Benjamini-Hochberg depends on their joint distribution. We use reference observations to certify a sufficient dependence condition for one-sided Gaussian tests. An intersection-union test of uncertain correlation signs determines whether to apply weighted Benjamini-Hochberg or a prespecified fallback at an adjusted level. Under conditional separation of certification and testing, the procedure controls the false discovery rate (FDR) for every Gaussian correlation matrix satisfying the stated sampling assumptions and weight constraints. We establish a boundary obstruction to uniform certification and matching minimax sample-size bounds for worst-case pair sets and the all-pairs problem. In the parameter ranges of the matching bounds, the minimax sample size grows logarithmically with the number of checked pairs and quadratically with the inverse of their positive margin. For homogeneous Gaussian observations with known marginal variances, residual contrasts from the testing subjects provide an independent source of certification scores. Simulations with up to 4,950 checked pairs, comparisons under a common subject budget, and Gaussian designs based on correlations estimated from the Healthy Brain Network illustrate the trade-off between certification and detection power.

</details>

### [A Robust Approach for Regression Analysis of Panel Count Data with Time-varying Covariates](https://arxiv.org/abs/2611.33607)
*Dayu Sun, Yuanyuan Guo, Yang Li et al.* · `stat.ME` · arXiv:2611.33607v1 · relevance 0.08

- **In one sentence**: The paper proposes a robust inference method for panel count data with time-varying covariates using rate models instead of mean models, with EM-based variance estimators and simulation and clinical-application support.
- **In plain words**: The paper concerns studies where each person's count of events (such as hospital visits) is recorded at a few check-in times, and factors that change over time may affect those counts. Existing robust methods assume the average event count can only go up over time, which fails when the factors fluctuate. The authors instead use a rate-based model without that constraint, and build a variance estimator using the EM algorithm, a standard iterative computing method.
- **Why it matters**: Reliable inference from count data is important in clinical and public-health studies, and the approach aims to hold up when the correlation structure is misspecified. The text reports simulations and a real clinical application, but the abstract alone does not show how large the gains are or how the method compares in other settings.
- **Background needed**: - Panel count data: each subject's number of events is observed only at a few irregular visit times, not continuously.
- Time-varying covariates: explanatory variables (e.g., a patient's treatment status) that change over the study.
- Mean model vs. rate model: a mean model specifies the average event count directly (and implicitly assumes it is non-decreasing over time); a rate model specifies the instantaneous rate of events, which can change in either direction.
- Within-subject correlation: repeated measures on the same person are related, so the assumed correlation pattern affects standard errors; "robust" methods aim to remain valid if that pattern is wrong.
- Asymptotic variance: the approximate variance of an estimate for large samples; here it has no simple closed form, so it must be estimated computationally.
- EM algorithm: an iterative method for maximum-likelihood estimation with missing or hidden information. · level: research-level

<details><summary>Original abstract</summary>

The validity of statistical inference for panel count data with time-varying covariates depends on the correct specification of within-subject correlation structures; misspecification often leads to questionable inference. To alleviate, robust inference has been proposed for mean models, which implicitly assume monotone mean functions. When covariate values fluctuate with time, however, the assumed monotonicity becomes unrealistic. In this research, we propose a robust inference based on rate models that are free of such constraints. Since the asymptotic variance has no closed form under the rate model, we further develop computationally efficient robust variance estimators using the Expectation-Maximization (EM) algorithm, thus sidestepping the need for computationally intensive numerical methods, which could undermine the robustness. Rigorous theoretical development is provided in support of parameter estimation and inference. Extensive simulation studies demonstrate the superiority of the proposed method. We present a real clinical application to illustrate the use of the proposed method.

</details>

## Statistical methods and applications

### [Design-based causal inference for ROC curves](https://arxiv.org/abs/2611.34057)
*Bufan Li, Haoyang Yu* · `stat.ME` · arXiv:2611.34057v1 · relevance 0.15

- **In one sentence**: A design-based framework for estimating the ROC curve, which compares treated and control outcome distributions in randomized experiments, with rank-based estimation, covariate adjustment, simultaneous confidence bands, and extreme-tail inference.
- **In plain words**: This paper is about comparing how a treatment changes the whole spread of outcomes, not just the average. Instead of asking only whether the treated group does better on average, it asks, for each cutoff level in the control group, what share of treated people score above that cutoff. The authors build an estimator from pooled ranks of the outcomes, prove it behaves well for large samples, and show how to attach confidence intervals to it.
- **Why it matters**: Many experiments care about who gains, not only the average gain, and this gives a way to study that without assuming a specific model of the outcomes. The text also reports that covariate adjustment can reduce variance and that the methods are tested on a large online learning experiment, though the text gives no further detail on how much improvement that yields.
- **Background needed**: - Randomized experiment: people are randomly assigned to treatment or control, so the groups are comparable on average.
- Potential outcomes: each person has an outcome under treatment and one under control; only one is observed.
- Design-based inference: uncertainty comes from the random assignment itself, not from assuming a statistical model for outcomes.
- ROC curve: originally from diagnostic testing, it plots the true-positive rate against the false-positive rate; here it is used to compare two outcome distributions.
- Quantile: the value below which a given share of a group falls (e.g., the 90th percentile is the score exceeded by 10% of the group).
- Covariate adjustment: using pre-treatment background variables to sharpen estimates.
- Confidence band: a range around a whole curve, not just a single point, that is expected to contain the true curve with a stated probability. · level: research-level

<details><summary>Original abstract</summary>

In randomized experiments, causal inference traditionally focuses on the average treatment effect, yet comparing the treatment and control potential outcome distributions is often of interest. Under complete randomization, we adopt a design-based framework without imposing an outcome model to study the receiver operating characteristic (ROC) curve, which measures the proportion of treated outcomes exceeding each upper quantile of the control distribution. We propose an estimator that depends only on pooled outcome ranks, establish its asymptotic normality, and construct conservative variance estimators and confidence intervals. We also develop covariate adjustment directly for the ROC estimator, preserving the target estimand while achieving an asymptotic variance no larger than that of the unadjusted estimator. We further construct simultaneous confidence bands over an interior range of quantile levels and extend pointwise inference to the extreme upper tail of the control distribution, with both extensions accommodating covariate adjustment. Simulation studies and an application to a large-scale online learning experiment illustrate the proposed methods.

</details>

### [BADGERS: Bayesian Adaptive Graph-Guided Errors-in-Variables Regression Solution for Structured High-Dimensional Data](https://arxiv.org/abs/2611.34378)
*Zeyu Hu, Kewen Qu, Qi Long et al.* · `stat.ME` · arXiv:2611.34378v1 · relevance 0.14

- **In one sentence**: BADGERS is a Bayesian regression framework that handles measurement error in replicated high-dimensional covariates (such as gene expression) while using a biological graph to guide variable selection and model the dependence among covariates.
- **In plain words**: Many gene studies measure the same quantity several times because each measurement is noisy, and standard analysis tools usually ignore that noise. This paper proposes a statistical method, BADGERS, that estimates the underlying "true" values from the repeated readings, uses a known biological network of related genes to help decide which genes matter, and tests the approach on simulated data and on gene expression datasets for Alzheimer's disease and multiple myeloma. The summary text reports advantages over existing methods in simulations and real-data analyses, but it does not give the specific numbers.
- **Why it matters**: Ignoring measurement error can bias which variables appear important, and omics studies often have this problem, so a method that accounts for it while using biological network information may be useful. Its practical value depends on details (such as computational cost and performance across settings) that the summary does not report.
- **Background needed**: - High-dimensional data: many more measured variables (e.g., thousands of genes) than samples.
- Errors-in-variables: when predictors are measured with noise, naive regression gives biased results.
- Latent variables: unobserved "true" values inferred from noisy measurements.
- Bayesian methods: combine prior beliefs with data to get a distribution over possible answers; Markov chain Monte Carlo (MCMC) is a sampling method used to compute these.
- Graphical lasso: a technique that estimates how variables are linked, encouraging sparse (few-connection) networks.
- Shrinkage priors: settings that pull weak effects toward zero to select variables.
- Omics: large-scale biological measurement fields such as genomics and transcriptomics. · level: research-level

<details><summary>Original abstract</summary>

Knowledge-guided learning methods that incorporate biological graph information into the analysis of structured high-dimensional data, such as genomic data, can improve variable selection and prediction accuracy while yielding more interpretable results. However, these methods typically assume that covariates are measured without error. This assumption is often violated in omics studies involving replicated measurements. To address this gap, we develop the Bayesian Adaptive Graph-guided Errors-in-variables Regression Solution (BADGERS), a Bayesian framework that jointly accounts for covariate measurement error and incorporates graph information while accommodating varying numbers of replicates across covariates. BADGERS treats the true covariates as latent variables and integrates three key components: a Gaussian errors-in-variables model using replicated measurements to inform the latent true covariates, a Bayesian adaptive graphical lasso with a graph-informed prior to model their dependence structure, and a regression model with an adaptive structured shrinkage prior to leverage graph information and facilitate variable selection. We develop an efficient Markov chain Monte Carlo algorithm for posterior sampling. We demonstrate the advantages of BADGERS over existing methods through simulation studies and analyses of gene expression datasets for Alzheimer's disease and multiple myeloma.

</details>

## AI industry news

### [Nvidia hits pause on chip shipments to Southeast Asia](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/)
*Connie Loizos* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.15

- **In one sentence**: Nvidia has reportedly told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand and Indonesia as U.S. efforts to keep advanced AI chips out of China tighten.
- **In plain words**: The chipmaker Nvidia has asked the companies that build its servers to stop sending them to four Southeast Asian countries: Malaysia, Singapore, Thailand and Indonesia. The reason given is that the United States is pushing harder to stop advanced AI chips from reaching China. The article is short and does not say how long the pause will last.
- **Why it matters**: Nvidia's chips are central to AI development, and shipping routes through neighboring countries are one way such chips could reach restricted buyers. The text does not give details on how the pause works or what it will affect, so its wider impact is unclear.
- **Background needed**: - Nvidia designs AI processors (GPUs) and sells them mostly inside complete servers, which are built by partner manufacturers.
- U.S. export controls limit the sale and transfer of advanced AI chips to China, for security and competition reasons.
- Southeast Asian countries such as Malaysia, Singapore, Thailand and Indonesia have become transit and assembly hubs for electronics, which is why rules affecting them matter.
- "Pause shipments" here means an order to hold deliveries; the article does not say whether it is permanent or tied to a specific rule.
- The text is a brief news item with no official statement quoted, so details should be checked against further reporting. · level: introductory

<details><summary>Original abstract</summary>

Nvidia has told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand and Indonesia as the U.S. tightens its push to keep AI chips out of China.

</details>

### [Meta brings its Muse AI assistant directly into Instagram DMs](https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/)
*Aisha Malik* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.08

- **In one sentence**: Meta has added its Muse AI assistant directly into Instagram direct messages, so users no longer need to switch to the separate Muse app to use it.
- **In plain words**: Meta, the company that owns Instagram, is letting people use its Muse AI assistant inside Instagram's private messaging feature. Before this change, a user who wanted the assistant had to leave Instagram and open a different app. The article is short and reports the change itself, not how well the assistant performs.
- **Why it matters**: It shows a common industry direction: AI helpers being placed inside apps people already use daily rather than in separate tools. The text does not say how many people use it or what effect it will have, so its wider importance is unclear.
- **Background needed**: - Meta owns Instagram and Facebook.
- Muse is the name of Meta's AI assistant, as the article describes it; the article does not explain its abilities.
- "DMs" means direct messages, the private chat feature in Instagram.
- An "AI agent" is a program that can carry out tasks or answer questions for a user; the article uses this term without detail.
- Integration here means building one product into another so they work together. · level: introductory

<details><summary>Original abstract</summary>

The new integration gets rid of the need for users to toggle between Instagram and the Muse app when they want to interact with the AI agent.

</details>

### [Grand Theft Auto VI proves why efficiency isn’t a virtue](https://techcrunch.com/2026/11/26/as-anthropic-ipos-grand-theft-auto-vi-proves-why-efficiency-isnt-a-virtue/)
*Amanda Silberling* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.08

- **In one sentence**: An opinion-style piece argues that the launch of Grand Theft Auto VI, a handcrafted video game, shows that human-made work can succeed commercially even in a period focused on efficiency, and it contrasts this with Anthropic's entry into public markets the same day.
- **In plain words**: This short article is about a major video game, Grand Theft Auto VI, which launched on the same day that the AI company Anthropic began trading on the public stock market. The text says the game was built by hand, with a lot of human care, and that it became one of the most successful entertainment launches ever. The author uses this to argue that being efficient is not always the same as being valuable.
- **Why it matters**: It offers a cultural counterpoint to the AI industry's focus on automation and speed, and it touches on how markets value human craft. The text is brief and gives no sales figures or detailed evidence, so its claims should be read as the author's opinion rather than established fact.
- **Background needed**: - Grand Theft Auto VI: a large, long-awaited video game from Rockstar Games, the studio behind earlier titles in the series.
- Anthropic: an AI company that develops the Claude family of AI models; the article says it entered the public market that day.
- "Going public": selling shares of a company to ordinary investors on a stock exchange.
- "Efficiency" here means producing the most output for the least effort or cost, often a goal of automation.
- The article is an opinion-style commentary with no detailed data, so the claims about success are not independently verified in the text. · level: introductory

<details><summary>Original abstract</summary>

On the same day that Anthropic entered the public market, a painstakingly human video game became one of most successful entertainment launches of all time.

</details>

### [Amazon and Meta reportedly in talks to lift blockade on AI agent Muse](https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/)
*Lauren Forristal* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: Reports say Amazon and Meta are discussing a possible deal that would end a two-month blockade of the AI agent Muse.
- **In plain words**: Two large tech companies, Amazon and Meta, are reportedly negotiating a deal that would lift a block that has been in place on an AI program called Muse for about two months. The article is very short and does not say who imposed the block, why, or what terms are being discussed.
- **Why it matters**: Disputes over access to AI tools can affect how widely such tools are used and who controls them. The text is too thin to say more, and it is unclear whether a deal has been reached.
- **Background needed**: - An "AI agent" is a software program that can carry out tasks on its own, such as acting on a user's behalf.
- A "blockade" here likely means access to Muse has been restricted, but the article does not explain the mechanism.
- Amazon and Meta are both large technology companies with major AI businesses.
- The article reports talks only; no agreement is confirmed in the text.
- The source of the report and the reasons for the blockade are not given. · level: introductory

<details><summary>Original abstract</summary>

Amazon and Meta are discussing a potential deal that would end a two-month-long blockade of Muse.

</details>

### [How Intentful uses dots to make more time for growth](https://openai.com/business/customer-stories/intentful-dots)
** · `openai.com` · OpenAI News · relevance 0.06

- **In one sentence**: A short company feature describing how Intentful, a firm, uses an AI assistant called "dot" (named Aria in one case, used by Marina Petrova) to research websites, draft proposals, flag messages, and resolve issues.
- **In plain words**: This short article describes how a company called Intentful uses an AI assistant named "dot" to take on routine office work. According to the text, the assistant, which goes by Aria for one employee, helps look up information on websites, prepare proposal documents, point out important messages, and sort out problems. The text does not report any measured results.
- **Why it matters**: It is a customer-style example of AI tools being used to free staff for other work, which is a common theme in workplace AI adoption. The text gives no figures or independent evidence, so it shows one company's described use rather than proof of benefit.
- **Background needed**: - "dot" appears to be the name of an AI assistant product; the article does not explain how it works.
- Intentful is the company featured; Marina Petrova is the named user.
- "Proactively flagging" means the assistant surfaces messages or issues without being asked.
- Proposals here are business documents, such as bids or project plans.
- The title's claim of "more time for growth" is the company's framing, not a measured outcome in the text.
- The source is thin: only one short paragraph, with no details on costs, accuracy, or how the tool was built. · level: introductory

<details><summary>Original abstract</summary>

Marina Petrova’s dot Aria helps research websites and build proposals, while proactively flagging messages and resolving issues.

</details>

## Model architectures and training

### [One Token, Many Lessons: Sliding-Window Attention within Gated Delta Networks](https://arxiv.org/abs/2611.33257)
*Yuchen Song, Yangbin Chen* · `cs.LG` · arXiv:2611.33257v1 · relevance 0.36

- **In one sentence**: The paper proposes Sliding-Window Gated DeltaNet (SWGDN), which swaps the short convolutions in Delta-Rule linear attention for sliding-window attention to build the key-value pairs used in state updates, and reports gains over the Delta-Rule baseline on GDN2 and KDA.
- **In plain words**: Large language models process text with attention, which gets expensive for long inputs. Linear attention models avoid this by squeezing past text into a fixed-size memory that is updated as each token arrives. This paper looks at how the examples used to update that memory are built, and proposes mixing each token with its nearby neighbors before updating, which the authors report makes consecutive updates more alike and improves results on several benchmarks.
- **Why it matters**: Linear attention is a way to make long-context models cheaper, so changes that improve it without altering the core update rule may be practically useful. The text reports consistent benchmark gains over the baseline, but it is an abstract-level description, so the size and robustness of those gains cannot be judged from it alone.
- **Background needed**: - Attention: a mechanism where each token looks at other tokens in the text to decide what matters.
- Linear attention: a cheaper variant that keeps a fixed-size running memory instead of comparing every token with every other.
- Recurrent state: that fixed-size memory, updated token by token.
- Test-time regression (TTR): a view that treats the memory as a small model learned on the fly, with keys as inputs, values as targets, and queries as reads.
- Delta rule: an update that corrects the memory toward the new key-value pair, like an error-correcting learning step.
- Gated DeltaNet (GDN2) and KDA: specific Delta-Rule linear attention architectures named in the paper.
- Sliding-window attention: each token mixes only with a small neighborhood of nearby tokens.
- Short convolution: a small local filter over neighboring tokens, which SWGDN replaces. · level: research-level
- Matched keywords: attention, linear attention, architecture

<details><summary>Original abstract</summary>

Linear attention compresses historical context into a fixed-size recurrent state, reducing the computational and memory costs of long-sequence modeling. From the perspective of test-time regression (TTR), the state matrix can be viewed as an online-learned regression model, where keys and values serve as inputs and targets respectively, and queries are used to read from the model. From this perspective, the effectiveness of state learning depends not only on the update rule but also on how the key-value learning pairs used for state updates are constructed. While existing work has largely focused on how the state is updated and organized, we investigate how the learning pairs used for state updates are constructed. To this end, we propose Sliding-Window Gated DeltaNet (SWGDN), which replaces short convolutions in Delta-Rule linear attention with sliding-window attention to perform content-dependent local aggregation of projected queries, keys, and values. Our experiments show that SWGDN makes the key-value pairs used in consecutive updates more similar in both GDN2 and KDA. In SWGDN, carrying information from the same token across updates can help the recurrent state reinforce a previously learned association. The local mixing strategy can be incorporated into any Delta-Rule-based linear attention architecture without changing its state update equations or chunkwise parallel algorithms. We apply this strategy to two Delta-Rule variants, GDN2 and KDA, and experimental results demonstrate that SWGDN outperforms the original Delta-Rule baseline across multiple benchmarks.

</details>

### [Resource-Efficient Multimodal Fusion for Early Rice Blast Forecasting in Sustainable Agriculture](https://arxiv.org/abs/2611.33237)
*Shubhajyoti Das, Pritam Bikram, Arindam Biswas et al.* · `cs.LG` · arXiv:2611.33237v1 · relevance 0.29

- **In one sentence**: A lightweight multimodal deep-learning framework, combining an attention-enhanced Transformer for meteorological sequences with a CNN-embedded GRU for two-timepoint remote sensing imagery, is proposed to forecast rice blast risk 5-10 days before symptoms appear.
- **In plain words**: Rice blast is a fungal disease that can wipe out rice crops, and farmers often spray pesticides without knowing when it will strike. This paper describes an AI model that combines weather records and satellite-style images to predict the risk of blast about a week before visible symptoms show up. The authors report 96.93% validation accuracy and an F1-score of 95.79%, and say the model is cheaper to run and uses less energy than existing methods.
- **Why it matters**: Early warning could let growers target treatments and cut unnecessary pesticide use, which matters for food security and the environment. The text does not show how the model performs on new farms or seasons beyond its validation data, so its practical value is not yet established.
- **Background needed**: - Rice blast: a fungal crop disease that can cause large yield losses.
- Forecasting model: software that predicts a future event from past data; here, disease risk from weather and imagery.
- Transformer: a neural network design that weighs which parts of a sequence matter most; "positional encoding" tells it where each item sits in time.
- CNN (convolutional neural network): a network good at picking out patterns in images, here spectral (colour/light-band) features.
- GRU (gated recurrent unit): a compact network that tracks changes over time.
- Multimodal fusion: combining different data types (weather and imagery) into one prediction.
- Validation accuracy / F1-score: standard measures of how often a classifier is right, with F1 balancing false alarms and misses.
- Lightweight / resource-efficient: uses less computing power, time and energy. · level: intermediate
- Matched keywords: transformer, attention, architecture

<details><summary>Original abstract</summary>

Resource-efficient artificial intelligence has become increasingly important for sustainable agriculture, where timely disease forecasting must be achieved under computational and energy constraints. Early estimation of rice blast can enhance food security by optimizing crop management practices while reducing excessive pesticide use. However, existing frameworks often suffer from high computational overhead and limited capability to model the complex spectral-temporal dependencies present in heterogeneous meteorological and remote sensing data. To address these challenges, this paper proposes a lightweight multimodal fusion framework comprising an attentive positional encoding-based Transformer and a convolutional neural network (CNN)-embedded gated recurrent unit (GRU) for efficient spectral-temporal representation learning. The attention-enhanced positional encoding assigns adaptive importance to sequential meteorological tokens, enabling effective modelling of temporal characteristics. In parallel, the lightweight CNN extracts discriminative spectral features, while the GRU captures temporal dynamics from remote sensing imagery acquired over two time-instances. A multimodal fusion layer integrates these heterogeneous representations to forecast rice blast risk 5-10 days before symptom manifestation across diverse agro-climatic zones. Extensive experiments demonstrate that the proposed framework outperforms state-of-the-art methods, achieving a validation accuracy of 96.93% and an F1-score of 95.79%. In addition to its predictive performance, the lightweight multimodal architecture substantially reduces computational complexity, inference latency, and carbon emissions, making it an energy-efficient solution for large-scale disease forecasting. The proposed framework provides a practical foundation for resource-efficient artificial intelligence in sustainable agriculture.

</details>

## Machine learning theory

### [Understanding Double Descent through Universal Compression](https://arxiv.org/abs/2611.33759)
*Jiaxuan Cheng, Addison Spiegel* · `stat.ML` · arXiv:2611.33759v1 · relevance 0.25

- **In one sentence**: The paper reinterprets neural-network double descent (test loss rising near the interpolation threshold, then falling again as models grow) through universal compression, bounding the maximum-likelihood excess test loss by four terms and linking the MLE-vs-Bayes gap to an MLE-vs-ensemble gap.
- **In plain words**: Large neural networks sometimes get worse on new data as they grow, then get better again, which the classical "bias-variance" picture does not predict. This paper explains that pattern using ideas from data compression: it splits the extra test error of a standard fitted model into four pieces. In experiments with random labels, the gap between a standard training method (SGD) and a Bayesian-style averaged predictor (SGLD ensemble) accounts for much of the error peak.
- **Why it matters**: Double descent is widely observed but still not well explained for modern deep networks, so a new framework for it is of interest. The text reports the main evidence as experiments with random labels, and the theoretical links depend on assumptions (such as exact posterior sampling and a well-specified setting), so the strength of the conclusion beyond these settings is not established here.
- **Background needed**: - Double descent: test error first rises near the point where a model can just fit its training data, then falls again as the model gets even larger.
- Bias-variance tradeoff: the classical view that test error is U-shaped in model size.
- Maximum likelihood (MLE): fitting parameters that make the observed data most probable.
- Bayesian posterior and ensemble: averaging predictions over many plausible parameter settings rather than using one fitted setting.
- SGD / SGLD: stochastic gradient descent, and a noisy variant that samples from an approximate posterior.
- Cross-entropy loss: a score for predicted probabilities; a uniform guess over 10 classes scores log 10.
- Universal compression: coding data with a single scheme that performs well without knowing the source; regret measures the extra cost versus the best scheme. · level: research-level
- Matched keywords: minimax, double descent

<details><summary>Original abstract</summary>

Many deep learning models exhibit a double-descent phenomenon, where test loss exhibits a sharp peak near the interpolation threshold and then descends a second time as model size grows further, contrary to the U-shape predicted by the classical bias--variance tradeoff. The double-descent phenomenon has been found and explained in toy classical models, but is not well-understood in modern deep learning despite extensive empirical study. We interpret double descent through the novel lens of universal compression. Specifically, we upper bound the maximum-likelihood excess test loss as a sum of four terms: an approximation-and-shift term, a minimax batch regret, a prior cost, and an MLE-vs-Bayes gap. Under exact posterior sampling, we further show that the expected MLE-vs-ensemble gap lower-bounds the MLE-vs-Bayes gap in the well-specified setting. In our experiments, a Gaussian-prior SGLD approximation to the Bayes predictor, unlike SGD, shows no pronounced interpolation peak. Experiments with uniform random labels support this gap as a major contributor to the double-descent peak; here, the SGD cross-entropy is roughly four times the SGLD ensemble cross-entropy at the peak, while the ensemble cross-entropy remains near $\log 10$.

</details>

### [Improved Sample Complexity of Robust Reinforcement Learning with KL Uncertainty Sets](https://arxiv.org/abs/2611.33592)
*Yudan Wang, Zilong Deng, Nathaniel D. Bastian et al.* · `stat.ML` · arXiv:2611.33592v1 · relevance 0.23

- **In one sentence**: This paper tightens the upper and lower bounds on the number of generative-model samples needed to find an epsilon-optimal policy for distributionally robust reinforcement learning with KL-divergence uncertainty sets, and extends the lower bound to all uncertainty levels.
- **In plain words**: The paper looks at how much practice data a learning agent needs to make good decisions when the real environment might differ somewhat from its best guess, with the allowed difference measured by a statistical distance called KL divergence. Earlier work left a gap between how much data was known to be enough and how much was known to be necessary, and its lower-bound results only covered a limited range of how far the environment could drift. The authors report a tighter upper bound, a lower bound that holds for any drift level, and say that the two roughly match in several regimes.
- **Why it matters**: The work refines theoretical limits on how efficiently robust AI decision-making can be learned, which matters for making such methods reliable when deployed conditions shift. The text is limited to the abstract, so it does not show practical impact or experiments, and the significance beyond theory is unclear from this text alone.
- **Background needed**: - Reinforcement learning: an agent learns a policy (a rule for choosing actions) by trial and reward.
- Generative model: an assumed simulator that can be queried for outcomes from any state-action pair.
- Distributionally robust RL: the agent optimizes for the worst environment within a set of plausible alternatives around its nominal model.
- KL divergence: a measure of how different two probability distributions are; here it sets how far the alternative environments may stray.
- Sample complexity: the number of data samples needed to reach a target accuracy epsilon.
- Discount factor gamma: how strongly future rewards count relative to immediate ones; (1-gamma)^-1 reflects the effective planning horizon.
- Upper and lower bounds: guarantees that enough samples suffice, and that fewer samples cannot work in general. · level: research-level
- Matched keywords: sample complexity

<details><summary>Original abstract</summary>

In this paper, we study distributionally robust reinforcement learning with Kullback--Leibler (KL) divergence-defined uncertainty sets. The goal is to find a policy that maximizes the robust value function, defined as the worst-case value over all transition kernels in the uncertainty set. Assuming access to a generative model, we aim to understand the sample complexity of finding an $\epsilon$-optimal robust policy. The best-known sample complexity results in the literature show a non-trivial gap of $\mathcal{O}\{\max\{p_\wedge^{-1}(1-\gamma)^{-1},(1-\gamma)^{-2}\}\}$ between the upper and lower bounds, where $p_\wedge$ denotes the minimum positive transition probability of the nominal transition kernel, and $\gamma$ is the discount factor. More importantly, existing results on the lower bound only cover a limited range of the uncertainty level. In this paper, we develop tighter and complete upper and lower bounds for robust RL with KL-defined uncertainty sets. Our upper bound is the tightest among all existing studies, and it improves upon the best-known bound by at least the order of $\mathcal{O}(\min\{p_\wedge^{-1},(1-\gamma)^{-1}\})$ for uncertainty level $\delta\in(0,1)$. Furthermore, our lower bound holds for any uncertainty level. Our upper and lower bounds (nearly) match in various regimes, providing improved results for this problem.

</details>

## Large language models

### [Verified experience improves materials prediction with large language models](https://arxiv.org/abs/2611.33195)
*Yiming Zhang, Koji Tsuda* · `cs.CL` · arXiv:2611.33195v1 · relevance 0.14

- **In one sentence**: The paper introduces MatMemBench, a sequential 22-task materials benchmark that reveals outcomes after each prediction, and MatRecall, a memory framework that lets large language models store verified predictions and recall them without retraining.
- **In plain words**: Scientists often predict material properties, check the answer in the lab or with calculations, and then use that result to make the next guess. This paper asks whether a language-model predictor can do the same: it saves each checked prediction, along with the supporting evidence, the true outcome and the error, and draws on those saved records for later questions. The authors report that this memory approach improved results substantially compared with a version that has no memory, and in some cases beat specialized models.
- **Why it matters**: It targets a gap between standard benchmarks, which score each question in isolation, and real discovery work, where each outcome should inform the next step. Whether this kind of memory-based learning holds up beyond the authors' own benchmark is not something the text establishes.
- **Background needed**: - Large language models (LLMs): AI systems trained on text that can also be prompted to make predictions.
- Specialized models: machine-learning models built for one narrow task, usually fixed after training.
- Retrieval-augmented generation: a method where the model looks up stored documents before answering.
- Benchmark: a standard test set used to compare methods.
- Online adaptation: improving as new results arrive, rather than only during initial training.
- Materials discovery: searching for new materials with useful properties, using experiments and computer simulations.
- Median improvement: the typical gain across tasks, here reported as 62% over a memory-free model. · level: intermediate

<details><summary>Original abstract</summary>

Materials discovery is an iterative loop: experiments and calculations verify predictions, and each outcome can inform the next. Yet most predictors are specialized single-task models fixed after training. Large language models have recently emerged as predictors across heterogeneous tasks but generally underperform specialized models, and retrieval-augmented variants discard their own outcomes. Benchmarks also score queries in isolation, leaving improvement from outcomes untested. Here we construct MatMemBench, a sequential benchmark of 22 materials tasks that reveals outcomes only after prediction and tests online adaptation, memory retention and cross-task transfer. We present MatRecall, a framework that lets large language models store verified predictions, with evidence, outcome and error, as episodes and recall them without retraining. MatRecall improved median performance by 62% over a memory-free model, exceeded specialized models on 11 tasks, remained useful after feedback stopped and transferred between related tasks. Verified experience could become a reusable resource for self-improving discovery loops.

</details>

### [Extraneous Cognitive Load in Large Language Models](https://arxiv.org/abs/2611.33197)
*Arushi Gupta, Sheng Liu, James Zou* · `cs.CL` · arXiv:2611.33197v1 · relevance 0.12

- **In one sentence**: The paper introduces CogLoadBench, a controlled benchmark varying five cognitive-load-inspired presentation factors across three reasoning task families, and proposes an activation-based Extraneous Load Score plus an inference-time representation shift to reduce load effects on LLMs.
- **In plain words**: Psychologists have found that how a problem is laid out, not just how hard it is, changes how well people solve it. This paper asks whether large language models behave similarly: the authors build a test set that changes only the presentation of tasks, then measure how much that hurts model accuracy. They also propose a score, computed from the model's internal activity, that estimates how much unnecessary load a prompt puts on the model.
- **Why it matters**: The work tries to separate presentation effects from task difficulty, which is a gap in how LLM performance is usually evaluated. If the score and the representation shift hold up, they could offer a way to diagnose and reduce presentation-driven errors without rewriting prompts, though the text alone does not show how broadly this transfers.
- **Background needed**: - Cognitive Load Theory: from educational psychology, it splits mental effort into intrinsic load (the task's inherent difficulty) and extraneous load (effort caused by how information is presented).
- Prompt: the text input given to a language model.
- Activations: the internal numerical values a neural network computes while processing input.
- Benchmark: a standardized test set used to compare models.
- Inference time: when a trained model is being used, as opposed to when it is being trained.
- Representation steering: nudging a model's internal values in a chosen direction without changing the prompt. · level: research-level

<details><summary>Original abstract</summary>

Cognitive Load Theory (CLT) shows that human problem-solving is affected by both intrinsic load, arising from task difficulty, and extraneous load, arising from how task information is presented. Large language models (LLMs) show analogous effects: presentation alone can affect model performance, but these effects have not yet been systematically isolated from task difficulty. To address this gap, we introduce CogLoadBench, a controlled benchmark that varies five CLT-inspired presentation factors across three reasoning task families. Across models, we find that higher extraneous load conditions often reduce accuracy by either adding competition or complicating the reasoning path. To support diagnosis and mitigation of load-related effects, we propose the Extraneous Load Score (ELS), a prompt-time metric computed from activations that estimates a model's extraneous load, and show that it generalizes across reasoning task types and load levels. We further show that shifting model representations toward lower-load directions at inference time can improve average model performance without changing prompt content.

</details>

## Computer vision

### [Incorporating the Knowledge Distillation to Improve the EfficientNet Transfer Learning Capability](https://arxiv.org/abs/2611.34025)
*Tjeng Wawan Cenggoro* · `cs.CV` · arXiv:2611.34025v1 · relevance 0.18

- **In one sentence**: The paper proposes using knowledge distillation to pass knowledge from larger EfficientNet models into smaller EfficientNet models as a transfer learning method for computer vision.
- **In plain words**: Image-recognition AI models are often pretrained on a large image collection and then reused for new tasks, a practice called transfer learning. This paper asks whether the smaller models in the EfficientNet family can be improved by learning from the larger models, which they were originally grown from. The authors report that this approach improved each EfficientNet size they tested, and that several smaller models beat a larger model trained the standard way.
- **Why it matters**: It offers a practical way to get better results from smaller, cheaper vision models without changing their size, which may matter for devices with limited computing power. The text is a short abstract, so it does not show how large or consistent the gains were, or how the method compares with other transfer approaches.
- **Background needed**: - Transfer learning: reusing a model trained on a large dataset (such as ImageNet) as the starting point for a new task.
- EfficientNet: a family of image-recognition networks of increasing size, where larger members were built by scaling up a smaller baseline.
- Knowledge distillation: training a smaller "student" model to imitate the outputs of a larger "teacher" model.
- ImageNet: a large benchmark dataset of labeled photographs used to compare vision models. · level: intermediate

<details><summary>Original abstract</summary>

Due to the Deep Learning requirement for a large training dataset, Transfer Learning has become a central method in the field of Computer Vision, which heavily used Deep Learning. Since the adoption of transfer learning in the field, the performance of the models in computer vision is significantly upgraded. The common transfer learning practice in computer vision research is to use state-of-the-art architectures in the ImageNet dataset as the backbone network. The best performing architecture in ImageNet is currently held by EfficientNet, which is a set of architectures that were progressively grown from a baseline architecture. By observing the EfficientNet development approach, it is natural to hypothesize that the smaller EfficientNet architecture is capable to contain the knowledge of the larger architecture. This hypothesis comes from the fact that the larger EfficientNet architecture was grown from the smaller architecture. Therefore, in this study, we experimented if it is beneficial to transfer the knowledge from the larger architecture to the smaller architecture of the EfficientNet. To achieve this goal, we proposed a transfer learning method that uses Knowledge Distillation as the knowledge transfer mechanism from the larger to smaller architecture. We found that the proposed method is able to upgrade the performance of each of the EfficientNet architecture. Several smaller architectures are even able to outperform the larger architecture that was trained using the standard transfer learning method.

</details>

### [TAT-Det: A Dataset for Testicular Appendage Torsion Detection and Segmentation in Ultrasound Images](https://arxiv.org/abs/2611.33940)
*Ying Jiang, Juntao Jiang, Linxuan Fan et al.* · `cs.CV` · arXiv:2611.33940v1 · relevance 0.15

- **In one sentence**: TAT-Det is a publicly described ultrasound dataset of 2,600 expert-annotated images from 1,203 children, with bounding boxes and pixel masks for testicular appendage torsion, plus baseline detection and segmentation benchmarks.
- **In plain words**: This paper is about a painful condition in young boys called testicular appendage torsion, a small twisted tissue structure in the scrotum that is a common cause of sudden scrotal pain before puberty. The authors built a labeled set of 2,600 ultrasound images from 1,203 patients at a children's hospital in China, with outlines drawn by trained specialists. They then tested several existing AI models on the images, reporting that YOLO11m performed best at finding the lesion and RWKV-UNet performed best at outlining it.
- **Why it matters**: Pediatric scrotal emergencies are hard to diagnose from symptoms alone, and there were few public datasets for this problem, so a shared labeled resource could let other groups build and compare automated tools. The text does not report how these models would perform in clinical use, so its practical value remains to be tested.
- **Background needed**: - Testicular appendage torsion (TAT): twisting of a tiny appendage attached to the testicle; the leading cause of sudden scrotal pain in prepubertal boys.
- Ultrasound: sound-wave imaging used to look inside the body without radiation.
- Dataset annotation: human experts marking the region of interest in each image so software can learn from it.
- Bounding box vs. segmentation mask: a rectangle around a lesion (detection) versus a pixel-by-pixel outline of it (segmentation).
- Baseline benchmark: a first set of reference scores that later methods can be compared against.
- YOLO11m and RWKV-UNet: names of existing deep learning model architectures used for detection and segmentation respectively. · level: intermediate

<details><summary>Original abstract</summary>

Background: Testicular appendage torsion (TAT) is the leading cause of acute scrotal pain in prepubertal children. Yet, its diagnosis remains challenging due to nonspecific clinical manifestations and the absence of standardized datasets for pediatric acute scrotal emergencies. Results: We present TAT-Det, an expert-annotated ultrasound dataset specifically designed for TAT. TAT-Det comprises 2,600 ultrasound images from 1,203 patients collected at the Children's Hospital, Zhejiang University School of Medicine. Each TAT-positive image is accompanied by lesion-level bounding boxes for detection and pixel-level segmentation masks for fine-grained delineation. Annotations were produced through a multi-stage workflow involving independent annotation by board-certified pediatric sonographers, consensus review, and refinement. Baseline benchmarks for object detection and semantic segmentation using representative deep learning models are further provided, with YOLO11m achieving the best detection performance and RWKV-UNet the best segmentation performance. Conclusions: TAT-Det addresses the lack of publicly available resources for pediatric emergency ultrasound and establishes a foundation for developing and evaluating artificial intelligence methods for automated TAT analysis.

</details>

## Reinforcement learning

### [Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk](https://arxiv.org/abs/2611.34840)
*Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi* · `cs.LG` · arXiv:2611.34840v1 · relevance 0.32

- **In one sentence**: This paper gives sample-complexity guarantees for offline, model-based reinforcement learning under a recursive entropic risk measure in discounted infinite-horizon MDPs, covering both risk-averse (beta > 0) and risk-seeking (beta < 0) settings, via an algorithm called ERM-VI-LCB.
- **In plain words**: This is about teaching a computer agent to make good decisions from a fixed log of past experience, while caring not just about average outcomes but also about how risky they are. The authors propose an algorithm and prove how much data it needs to reach a near-optimal policy. They also show that part of the data requirement, which grows exponentially with a risk-tuning parameter, cannot be avoided in the worst case.
- **Why it matters**: Risk-aware decision making matters wherever a bad tail outcome is costly, such as in finance, medicine, or robotics, and offline learning matters where live experimentation is expensive. The text claims these are the first rigorous sample-complexity guarantees for this combination, though I have not checked that claim against the wider literature.
- **Background needed**: - Markov decision process (MDP): a model of sequential decisions where actions lead to probabilistic new states and rewards.
- Reinforcement learning (RL): learning a policy (a strategy for choosing actions) by trial and reward.
- Offline RL: learning only from a fixed, previously collected dataset, with no new interaction.
- Discount factor gamma: weights near-term rewards more than distant ones; the horizon is effectively about 1/(1-gamma) steps.
- Entropic risk measure: a way of scoring uncertain outcomes that penalizes (risk-averse, beta > 0) or rewards (risk-seeking, beta < 0) variability, applied recursively over time.
- Sample complexity: how much data is needed to reach a near-optimal policy with high probability (PAC-style bound).
- Lower confidence bound (LCB): a pessimistic estimate used to handle parts of the state space with little data. · level: research-level
- Matched keywords: reinforcement learning, offline RL

<details><summary>Original abstract</summary>

We study risk-sensitive reinforcement learning in finite discounted infinite-horizon Markov Decision Processes with recursive entropic risk measures (ERM), parameterized by $\beta\neq 0$. We consider both risk-averse ($\beta>0$) and risk-seeking ($\beta<0$) settings. We consider the offline RL setting, where the agent is provided with a fixed dataset and wishes to learn a near-optimal policy using this dataset. We introduce a model-based algorithm, called ERM Value Iteration Lower Confidence Bound (ERM-VI-LCB) and derive a PAC-type bound on its sample complexity. We also establish a corresponding lower bound, demonstrating that exponential dependence on $|\beta|/(1-\gamma)$ asserted by the upper bound is unavoidable in the worst case. The presented bounds provide the first rigorous sample complexity guarantees for offline RL under recursive ERM across both risk-averse and risk-seeking regimes.

</details>

### [Effect-Driven Skill Abstractions for Offline Reinforcement Learning](https://arxiv.org/abs/2611.33229)
*Burcu Kilic, David Drexel, Emre Ugur et al.* · `cs.RO` · arXiv:2611.33229v1 · relevance 0.27

- **In one sentence**: The paper proposes learning discrete skill vocabularies for offline, goal-conditioned RL by quantizing action chunks with an objective that predicts next states from the current state and action, so skills are distinguished by their effects.
- **In plain words**: Teaching a robot or simulated agent to plan in longer steps often means grouping small movements into reusable "skills." This paper proposes a way to build a small set of such skills by judging each one by what it does to the agent's surroundings, rather than by how well it reconstructs the original movements. The authors report that this approach, plugged into common offline learning methods, gave substantial and consistent gains on benchmark navigation and manipulation tasks compared with continuous-action baselines and reconstruction-based alternatives.
- **Why it matters**: Choosing among a finite set of skills, instead of outputting continuous motor commands, could make long-horizon planning easier to structure. The paper's central idea, that skills should be defined by the states they lead to, is a clear conceptual point, though the text alone does not show how well it generalizes beyond the benchmarks tested.
- **Background needed**: - Reinforcement learning: an agent learns by trial and reward; here it learns from a fixed dataset of past experience (offline RL).
- Goal-conditioned RL: the agent is given a target state or goal to reach.
- Skill abstraction: short sequences of actions grouped into a reusable unit, so a planner picks among units instead of individual moves.
- Action chunks: fixed-length sequences of low-level actions treated as one unit.
- Quantization / discretization: mapping continuous values onto a finite set of codes (a "vocabulary").
- Low-level controller: a learned component that turns a chosen skill back into continuous actions.
- Baselines: established methods used for comparison. · level: research-level
- Matched keywords: reinforcement learning, offline RL

<details><summary>Original abstract</summary>

We seek to learn discrete skill abstractions to facilitate long-horizon, goal-conditioned reinforcement-learning (RL) tasks. Recent approaches have shown success by quantizing actions via clustering or reconstruction. However, these objectives lead to skills that are not directly related to what the current state affords or what the goal requires. Instead, we argue that goal-directed skills should be driven by \emph{how they affect the state} of the agent. To realize this, we introduce a novel quantization method for action chunks that optimizes next-state predictions conditioned on the current state and action. This objective encourages skills to be distinguished by the future states they lead to, resulting in a vocabulary that spans diverse outcomes reachable from a given state. Our framework can easily be paired with common offline RL methods by replacing their continuous actor head with a discrete one that selects among the learned skills. We can execute these skills in the environment by converting them back to continuous actions using a trained low-level controller. Experiments on benchmark navigation and manipulation tasks largely show substantial and consistent improvements over both the continuous-actor baselines and reconstruction-based discretizations. Our project page can be found at: https://burcukilic.github.io/projects/effect-driven-skill-abstractions/.

</details>

## AI safety and alignment

### [Best-of-$N$ Test-Time Steering Can Lead to Reward Hacking in Vision-Language-Action Models](https://arxiv.org/abs/2611.33398)
*Vanshaj Khattar, Jing Liu, Toshiaki Koike-Akino et al.* · `cs.RO` · arXiv:2611.33398v1 · relevance 0.32

- **In one sentence**: This paper studies best-of-N test-time steering for vision-language-action robot policies and finds that, with an inaccurate verifier, sampling more candidates can select actions that exploit verifier errors (reward hacking), with calibration and softmax selection offering partial mitigation in some settings.
- **In plain words**: Robots that follow language instructions can be improved at deployment time by sampling several possible actions and letting a scoring program pick the best one. This paper shows that this strategy can backfire: when the scorer makes mistakes, picking from more candidates can favor actions that just happen to earn high scores from those errors rather than actually doing the task well. The authors tested this on 60 safety-focused robot tasks in a simulator, with ten repeated runs per task.
- **Why it matters**: It is a concrete, measured example of a known worry in AI safety: optimizing against an imperfect scoring rule can make results worse. It matters for any system that picks outputs by checking them with a learned or approximate judge, though the text covers one robot policy, one simulator, and deliberately injected verifier errors, so its reach beyond that setting is unclear.
- **Background needed**: - Vision-language-action (VLA) model: an AI that reads camera images and a text instruction and outputs robot movements.
- Test-time steering: guiding a model's behavior while it runs, by spending extra computation, rather than retraining it.
- Best-of-N sampling: generate N candidate outputs, then keep the one a scoring function rates highest.
- Verifier: the scoring function that rates candidates; here, a checker built on a physics simulator (MuJoCo).
- Reward hacking: when an optimizer exploits flaws in a score so the score looks good while the real goal is missed.
- Calibration: making a score's numbers match how often it is actually right.
- Softmax selection: picking candidates probabilistically, weighted by score, instead of always taking the top one.
- LIBERO-Safety: a benchmark of simulated robot manipulation tasks with safety considerations. · level: research-level
- Matched keywords: reward hacking

<details><summary>Original abstract</summary>

Vision-language-action (VLA) models have shown promise for general-purpose robotic manipulation, but adapting to changing environmental conditions still remains challenging. Recent test-time steering methods have shown promise in enabling adaptive VLA policies by utilizing additional computation during deployment. In this paper, we consider best-of-$N$ test-time steering for VLA models, where multiple action candidates are sampled from a fixed policy and a verifier is used to select the best one during deployment. We show that increasing $N$ does not always improve performance when the verifier is inaccurate, and can favor candidates whose scores exploit prediction errors, a form of reward hacking. We study this effect on 60 LIBERO-Safety task-level cases using a $\pi_{0.5}$ policy, with ten repetitions per case. We introduce controlled errors in a MuJoCo trajectory verifier and show that as $N$ increases, selected candidate rewards diverge from the accurate verifier rewards, leading to reward hacking. We also show that verifier calibration and softmax-based candidate selection can mitigate reward hacking in some settings.

</details>

### [Latent-in-the-Middle: On the Security of Cross-Model Latent Communication in Multi-Agent Systems](https://arxiv.org/abs/2611.34278)
*Manit Baser, Vyoman Jain, Rachel Yeo Hui Min et al.* · `cs.CR` · arXiv:2611.34278v1 · relevance 0.20

- **In one sentence**: The paper studies security risks of cross-model latent communication, where a learned mapper translates one language model's KV cache into a form a different target model can use, and introduces the "Chasm" framework with a lightweight target-side cache guard as a mitigation.
- **In plain words**: AI agents often pass information to each other as written messages, but they can also share their internal working memory directly. This paper asks whether that shortcut weakens the safety training of the receiving model, since it then reads context it never produced itself. The authors report that such transfers substantially weaken refusals and defenses against prompt injection and jailbreaks, and they propose a small guard that corrects transferred memory to restore refusals.
- **Why it matters**: As multi-agent AI systems adopt faster, cheaper ways to share internal states, a safety check that only inspects text messages could miss attacks. The text reports concrete attack-success figures, but it is a single paper's experiments, so how far these results generalize to other models and deployments is not established here.
- **Background needed**: - Large language model (LLM): an AI system that generates text from a prompt.
- Multi-agent system: several AI models working together, passing information between them.
- KV cache (key-value cache): the stored internal working memory a model builds while reading text; reusing it saves recomputation.
- Latent communication: sharing these internal representations instead of plain-language messages.
- Cross-model transfer: using a learned mapper to convert one model's memory into a format another model can read.
- Safety alignment: training that makes a model refuse harmful requests.
- Prompt injection: hidden instructions in input text that hijack a model's behavior.
- Jailbreak: a crafted prompt that gets a model to bypass its refusals.
- GCG: a standard automated method for generating adversarial jailbreak suffixes.
- pp (percentage points): the absolute difference between two percentages. · level: research-level
- Matched keywords: alignment, jailbreak

<details><summary>Original abstract</summary>

As large language models increasingly collaborate in heterogeneous multi-agent systems, latent communication has emerged as an efficient alternative to exchanging natural-language messages. By sharing internal representations, agents can avoid repeatedly processing the same context, reducing communication overhead and prefill computation. One such mechanism is cross-model Key-Value (KV) cache transfer, which uses a learned mapper to translate a source model's KV cache into one a target model can use. However, this handoff means the target model consumes context it did not encode itself, thus calling into question whether its safety alignment still holds. In this work, we investigate the security implications of latent handoffs by introducing Chasm, a framework characterizing cross-model handoff attacks across three new attack surfaces: the source model, mapper, and handoff mechanism itself. Our experiments reveal that latent handoffs substantially undermine safety alignment and prompt-injection defenses. Notably, a target model that follows only 0.4% of benchmark prompt injections natively, follows up to 44.2% when transferred through a mapper from a source model. On the other hand, for jailbreak attacks, transfer alone raises attack success by up to 24.6 pp within a model family and zero-shot attacks by up to 69.2 pp, whereas white-box optimization through the mapper boosts the attack success rate to 92.5%, against 37.5% for ordinary GCG on the same target. To address these vulnerabilities, we propose a lightweight target-side cache guard that corrects transferred caches to restore the target model's refusal, considerably mitigating these attacks.

</details>

## Interpretability

### [A gene informed benchmark for BioScoring of pathology foundation models](https://arxiv.org/abs/2611.34930)
*Paul Vilars, Vincent Quoc-Huy Trinh, Maria Vakalopoulou et al.* · `cs.LG` · arXiv:2611.34930v1 · relevance 0.20

- **In one sentence**: BioScore is a label-free benchmark that scores how well pathology image encoders capture 52 marker-gene-defined cell identities, using sparse-autoencoder feature groups matched against spatial transcriptomics of the same tissue.
- **In plain words**: Pathology AI models read tissue slide images, but they are usually judged only by how well they do on tasks like classification, which says little about what biology they have learned. This paper proposes a test that checks whether each model's internal features line up with specific cell types, using gene-activity maps from the same tissue as a reference. The authors scored 8 pathology models and 3 general natural-image models, and found that all the pathology models scored higher.
- **Why it matters**: It offers a way to look inside pathology models at the biology they represent, rather than only their task scores, which may help researchers compare and understand them. The text does not show how well these scores predict real-world clinical usefulness, so that link remains open.
- **Background needed**: - Pathology foundation models: large AI models trained on many tissue images, then reused for many tasks.
- Image encoder: the part of a model that turns an image patch into a list of numbers (an embedding).
- Sparse autoencoder: a method that re-expresses those numbers as a small set of mostly-off features, which can be easier to interpret.
- Spatial transcriptomics: a technique that measures which genes are active at each location in a tissue section.
- Marker genes: genes whose activity is characteristic of a particular cell type.
- Linear probe: a simple supervised classifier trained on frozen model features; BioScore is compared against this kind of benchmark. · level: research-level
- Matched keywords: sparse autoencoder

<details><summary>Original abstract</summary>

Pathology foundation models are usually compared by their performance on downstream tasks such as classification and retrieval. While such benchmarks measure how useful a model is, they provide no insight into the biology it represents. We introduce BioScore, a benchmark that quantifies how well an image encoder captures cell identities, with spatial transcriptomics of the same tissue as the reference. A sparse autoencoder splits the encoder's patch embeddings into sparse features, which we cluster into a fixed number of groups. BioScore then measures, for each of 52 cell identities defined by marker genes, how specifically one group follows the identity's expression over the tissue. Because the autoencoder training is fully unsupervised, a match shows that the model represents the cell identity from the image alone. We score 8 pathology foundation models and 3 natural-image models. Every pathology model scores above every natural-image model (0.299--0.371 \vs 0.214--0.232), and paired tests separate three tiers among the pathology models. Unlike a supervised probe, BioScore needs no labels, builds its reference from the data and scores even from few sections, yet it ranks the encoders as a probe does. Its per-identity breakdown indicates which cell identities each encoder captures or misses.

</details>

### [PatternMiner: Automated Mathematical Discovery Through LLM-Guided Training and Interpretation of Small Models](https://arxiv.org/abs/2611.33966)
*Michael Ruofan Zeng, Junaid Hasan, Xuanyu Yang et al.* · `cs.AI` · arXiv:2611.33966v1 · relevance 0.13

- **In one sentence**: PatternMiner is an LLM-agent system that generates mathematical datasets, trains small models, interprets them to propose conjectures, and searches for counterexamples, applied to five positivity problems in algebraic combinatorics.
- **In plain words**: This paper describes a computer system that tries to discover new mathematical facts. A language-model agent builds datasets of mathematical objects, trains small machine-learning models on them, and then inspects those models to suggest possible rules. The system also hunts for counterexamples with mathematical software, and it reports that it proved several new theorems in one area of combinatorics.
- **Why it matters**: It combines two approaches to AI-assisted mathematics, one based on text reasoning by large language models and one based on interpretable models over concrete data, which the text says each lacks alone. Its value rests on the new theorems it reports, and the text does not say how significant those results are to the field.
- **Background needed**: - Positivity problems: questions about whether certain numbers or polynomial coefficients are always nonnegative, a common theme in algebraic combinatorics.
- Schubert calculus and Kazhdan–Lusztig theory: areas of algebra and combinatorics where such positivity questions arise.
- Conjecture: a statement believed to be true but not yet proven.
- Counterexample: a specific case that shows a conjecture is false.
- Interpretability: techniques for explaining what a trained machine-learning model has learned.
- Large language model (LLM) agent: an AI system that writes text and can call external tools such as mathematical software. · level: research-level
- Matched keywords: interpretability

<details><summary>Original abstract</summary>

There are several approaches to AI-driven mathematical discovery. One of these involves the use of large language models (LLMs) to resolve well-specified conjectures via text-based reasoning, while another uses narrow models and interpretability for more open-ended, human-in-the-loop exploration using object-based mathematical data. The latter is limited in its ability to move beyond simple empirical pattern detection while the former is not well-designed for direct, open-ended exploration of large mathematical datasets. In this paper we introduce PatternMiner, a system that combines these two paradigms. In PatternMiner, an LLM agent generates mathematical datasets based on an initial broad question, trains narrow machine learning models on them, uses interpretability techniques to extract patterns from these trained models, and uses these patterns to formulate conjectures. Once an initial conjecture has been formulated, PatternMiner instructs the agent to search for counterexamples using calls to mathematical software. If a set of counterexamples can be found, these are used as feedback for conjecture refinement or another round of training and interpretability. The conjecture progressively evolves through this iterative sequence with the agent allowed to try to prove it at any point. We describe the results of applying PatternMiner to five well-known positivity problems in algebraic combinatorics. PatternMiner proves several new theorems related to Schubert positivity and projection, a character-row evaluation formula, a restricted version of the Kazhdan--Lusztig combinatorial invariance conjecture, and Schur positivity for a family of immanant coefficients. We end by analyzing the most common routes to conjecture generation that are used by PatternMiner in our case studies as well as documenting the most common failure modes.

</details>

## AI for mathematics

### [AutoformBench: A Lean Formalization Benchmark for Advanced Mathematics](https://arxiv.org/abs/2611.33165)
*Charles Arnal, Ahmad Rammal, Niket Patel et al.* · `cs.AI` · arXiv:2611.33165v1 · relevance 0.35

- **In one sentence**: AutoformBench is a 341-task benchmark for Lean 4 formalization of advanced mathematics, where agents must build missing definitions and lemmas, not just prove isolated theorems, and the paper reports that frontier models share a common difficulty frontier tied to constructing that infrastructure.
- **In plain words**: Computer proof assistants check mathematics line by line, but writing a result in such a system takes more than proving the final claim: you also need the definitions and helper facts that connect it to the existing library. This paper introduces a test set of 341 such tasks drawn from 24 advanced math sources, where AI agents get the informal proof and must write the Lean version, including the supporting pieces. The authors report that frontier models tend to struggle with the same problems, and that success depends more on building that missing scaffolding than on the field of mathematics.
- **Why it matters**: Most earlier evaluations gave AI a single theorem in a setting where much of the needed theory already existed, so they may overstate how much real formalization work AI can do. The benchmark targets the harder, more realistic part of the job, which matters for anyone hoping AI can help formalize research mathematics. The text does not report detailed scores, so the size of the gap between models is not something this summary can establish.
- **Background needed**: - Lean 4: a programming language and proof assistant in which mathematical statements and proofs are checked by computer.
- Mathlib: Lean's large community library of already-formalized mathematics.
- Formalization: translating an informal mathematical argument into code the proof checker accepts.
- Definitions and lemmas: the supporting concepts and intermediate facts a proof relies on; here they must be built by the AI.
- Benchmark: a fixed set of tasks used to compare systems on equal terms.
- Agent: an AI system that works through multi-step actions, such as writing and testing code, rather than producing one answer. · level: research-level
- Matched keywords: Lean, theorem proving, mathlib

<details><summary>Original abstract</summary>

AI systems are increasingly capable of producing machine-checked Lean proofs of advanced mathematical results. Real mathematical formalization, however, is not isolated theorem proving: it requires building the definitions and intermediate lemmas that connect a result to a formal library. Existing evaluations often provide isolated theorem statements in settings where much of this supporting theory is already available in Mathlib. We introduce AutoformBench, a benchmark of 341 Lean 4 formalization tasks drawn from 24 advanced mathematical sources. Lean-experienced mathematicians formalized and audited each target statement, leaving the corresponding Lean proof to the evaluated agent. Each problem is embedded in a broader mathematical development: agents receive the informal proof but must translate it into Lean while constructing the missing definitions, intermediate lemmas, and supporting infrastructure. We compare the performance of frontier models on these problems. We find a largely shared difficulty frontier: success depends less on mathematical domain than on models' ability to construct missing formal infrastructure. Data and code at https://github.com/facebookresearch/autoformbench

</details>

### [Interactive Proofs as a Unified Framework for Evaluating and Leveraging Verifiable Proof Generation by LLM Agents](https://arxiv.org/abs/2611.33676)
*Yankai Shu, Xingyu Zhao, Chuan Mao et al.* · `cs.AI` · arXiv:2611.33676v1 · relevance 0.17

- **In one sentence**: The paper proposes Merlin-Bench, a benchmark that casts LLM agents as provers in an interactive proof protocol with a formal verifier, testing 100 cases across 15 problem families on 10 frontier LLMs and several agent harnesses.
- **In plain words**: Math and software-checking AI systems are often asked for an answer, but a useful answer also needs evidence that others can check. This paper builds a test in which an AI must back up its claimed answer by exchanging messages with an automatic checker, following a set rule for how the exchange works. Across 100 test cases, the authors report that getting current AI models to produce checkable evidence this way is still a substantial challenge.
- **Why it matters**: Checkable evidence matters if AI is to be trusted with proofs or program verification, because a correct-looking answer alone can't be verified. The work's connection to interactive proof systems from complexity theory is a framing choice; the text does not show how far the benchmark will generalize beyond its 100 cases.
- **Background needed**: - Interactive proof system: a protocol where a "prover" convinces a "verifier" through back-and-forth exchanges, drawn from computational complexity theory.
- Formal verifier: an automatic program that mechanically checks whether a proof is valid, independent of human judgment.
- LLM agent harness: the surrounding software that lets a language model call tools, run code, and iterate on its work.
- Theorem proving: using computers to establish mathematical statements with rigorous, checkable proofs.
- Benchmark: a standard set of test tasks used to compare systems. · level: research-level
- Matched keywords: theorem proving

<details><summary>Original abstract</summary>

Recent advances in LLM-assisted theorem proving and program verification have attracted widespread attention. Beyond determining whether a proposition is true, LLM agents must produce evidence that can be independently checked by humans or formal verification tools. To evaluate the underlying, protocol-agnostic ability of LLM agents to construct verifiable proofs-rather than their proficiency with any particular proof language or verification tool, we introduce Merlin-Bench. Drawing on interactive proof systems from computational complexity theory, we cast an LLM agent as the prover: under a designated protocol, the agent interacts with a formal verifier to substantiate its claimed answer to a problem instance. We develop an automated framework for constructing test cases and use it to create 100 cases across 15 problem families, each formulated within this prover-verifier framework. Experiments with 10 frontier LLMs across multiple agent harnesses show that reliably producing verifiable proofs in accordance with specified protocols remains a substantial challenge. Our case studies further provide actionable insights into improving agents' ability to generate verifier-accepted proofs: tool use is essential for completing practical proof tasks; different forms of guidance, ranging from engineering instructions to problem-specific knowledge, substantially affect success rates on interactive-proof tasks; and proof-solving experience distilled from abstract tasks can transfer to concrete, real-world verification tasks.

</details>

## Robotics and embodied AI

### [Recoverability policy editing for closed-loop safety in autonomous driving](https://arxiv.org/abs/2611.34403)
*Yang Guan, Shengbo Eben Li* · `cs.RO` · arXiv:2611.34403v1 · relevance 0.19

- **In one sentence**: A state-level policy editing method that, for recoverable states where a neural driving policy would eventually lead to a collision, overrides the policy's actions to steer the vehicle back into a safe set, aiming for closed-loop collision avoidance while keeping the original policy elsewhere.
- **In plain words**: Self-driving systems built on neural networks usually come with no formal promise that they will stay safe over time. This paper looks at situations where a car is heading toward trouble but could still get back to safe driving if it reacts in time. The authors' method identifies those situations and corrects the car's actions only there, then hands control back to the original driving model once it has recovered. In simulated urban driving on the nuPlan benchmark, the authors report a 48% drop in safety incidents compared with the original policy, with its driving performance largely kept.
- **Why it matters**: Neural driving models are hard to certify, so a way to add a safety layer that leaves most of the model's behaviour untouched could matter for deployment. The reported result is from simulation only, and the text does not say how the method performs on real vehicles or in situations outside the tested scenarios.
- **Background needed**: - Closed-loop: the car's actions affect what it sees next, so errors can compound over time, unlike a single prediction.
- Policy: the rule or neural network that maps what the car senses to what it does (steer, brake, accelerate).
- Feasible set: the set of situations from which the policy can still avoid collisions; the paper's notion of recoverability is about returning to it in finite time.
- Recoverable disturbance: a shock or error that the car can correct from, as opposed to one that already makes collision unavoidable.
- nuPlan: a public benchmark of urban driving scenarios used for testing planning algorithms in simulation.
- Safety incident: an event such as a collision counted during simulated runs. · level: research-level

<details><summary>Original abstract</summary>

Autonomous driving powered by neural network models lacks safety guarantees. We propose a state-level policy editing technique that guarantees closed-loop safety under recoverable disturbances while reusing the model's existing driving capabilities. Closed-loop safety means that the vehicle remains free of collisions at all future times. We introduce the concept of policy recoverability to characterize whether a vehicle can safely return to the original policy's feasible set in finite time. Our method identifies states that are unsafe in the long term under the original policy but recoverable, and selectively edits policy outputs within this region. The vehicle corrects its actions upon entering this region and resumes the original policy upon recovery. Closed-loop simulations on nuPlan urban driving scenarios show a 48% reduction in safety incidents under the original policy while largely preserving its driving performance.

</details>

### [WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics](https://arxiv.org/abs/2611.34130)
*Ziyuan Chu, Mingzhi Zheng, Kaiyue Zhang et al.* · `cs.RO` · arXiv:2611.34130v1 · relevance 0.18

- **In one sentence**: WorldPhy is a benchmark of 300 robotics scenarios, plus a learned reward model (WorldPhyReward) trained on over 12K human annotations, for scoring how physically plausible videos generated by 13 world models are across six fine-grained physical dimensions and instruction following.
- **In plain words**: World models are AI systems that predict or generate future video of a scene, and robots can use them to practice or plan actions. This paper introduces WorldPhy, a test set of 300 robot tasks, each starting from a single image and an instruction, along with a scoring model trained on human judgments. The authors report that the scoring model agrees better with human raters than general vision-language models and existing reward models do, and that 13 current world models often fail to keep motion and object interactions physically realistic across different robot scenes.
- **Why it matters**: Robots that rely on generated video need that video to obey physics such as contact, motion and object behaviour, so a finer-grained way to check this is useful for judging and improving these models. The text does not show how the benchmark affects real robot performance, so its practical impact remains to be tested.
- **Background needed**: - World model: an AI model that generates or predicts future video frames given a starting image and an action or instruction.
- Benchmark: a standard set of test tasks used to compare systems fairly.
- Reward model: a learned scorer that rates outputs, here trained to mimic human ratings.
- Vision-language model (VLM): an AI model that takes images and text and produces text answers.
- Physical plausibility: whether motion and contacts in a video look consistent with real-world physics.
- Human annotation: people labelling or rating examples, used here as ground truth for training and checking the scorer. · level: intermediate

<details><summary>Original abstract</summary>

World models are increasingly used in robotics to improve the performance of embodied models. Compared with general-purpose video generation, robotics places more stringent requirements on world models. Generated videos must satisfy fine-grained physical constraints on robot motion and object interactions. However, existing world model benchmarks can overlook robotics specific physical details and struggle to assess them accurately. To address this problem, we introduce WorldPhy, a world model benchmark for accurate, fine-grained evaluation of physical plausibility in robotics. Our benchmark contains 300 tasks, each consisting of an initial-frame image and a task instruction, covering diverse robotics scenes, task categories, viewpoints, and robot configurations. We further collect over 12K high-quality human annotations, and use them to train WorldPhyReward to accurately provide scores and reasons across six fine-grained physical dimensions and an instruction-following dimension. Comparisons with general VLMs and existing reward models show that WorldPhyReward better aligns with human ratings. We system- atically evaluate 13 frontier open and closed-source world models. The results reveal that current world models struggle to consistently maintain fine-grained physical plausibility across different robotics scenarios. Our code is available at https://github.com/chuziyuan139/ WorldPhy.

</details>

## Security and cryptography

### [Evaluating Post-Quantum and Hybrid Signatures for Blockchains: Performance, Storage and Ledger Growth](https://arxiv.org/abs/2611.34229)
*Anthony Mikhaiel, Essam Ghadafi* · `cs.CR` · arXiv:2611.34229v1 · relevance 0.15

- **In one sentence**: An empirical benchmark of 13 classical, post-quantum and hybrid digital signature configurations, measuring signing and verification cost, throughput, and key/signature sizes, with projected ledger growth for five public blockchains.
- **In plain words**: Blockchains use digital signatures, which are the locks that prove a transaction came from its owner, and those locks are based on math that a future quantum computer could break. This paper tests a range of replacement locks that are designed to resist quantum computers, plus mixed versions that use both the old and new schemes, in a simulated blockchain. It then estimates what would happen to the size of the recorded history of five major chains if they had used these replacements.
- **Why it matters**: Migrating blockchains to quantum-resistant signatures is a live question for the systems that hold large amounts of value, so the measured trade-offs matter for planning. The paper's main point is that storage growth, not checking speed, may be the harder problem; the storage figures rest on the authors' stated modelling assumptions, so they are estimates rather than measurements of real networks.
- **Background needed**: - Digital signature: a cryptographic proof that a message was authorised by the holder of a secret key; blockchains use them to approve transactions.
- ECDSA: the classical signature scheme used by Bitcoin and Ethereum, vulnerable to a sufficiently large quantum computer.
- Post-quantum cryptography: schemes designed to resist attacks from quantum computers. The paper tests ML-DSA, Falcon and SLH-DSA.
- Hybrid signature: a combination that requires both a classical and a post-quantum signature to be valid, as a hedge.
- Signature and key size: larger values mean bigger transactions and more data stored on the ledger.
- Verification vs. signing: checking a signature is what every node does repeatedly; signing is done by the user.
- Ledger growth: the total size of the stored transaction history that every full node must keep. · level: research-level

<details><summary>Original abstract</summary>

Advances in quantum computing pose a long-term threat to blockchain systems that rely on classical digital signature schemes such as ECDSA. Migrating these systems to post-quantum cryptography introduces practical costs beyond cryptographic security, including larger transactions, higher computational costs and faster ledger growth. We present an empirical evaluation of 13 signature configurations in a common simulated blockchain framework: ECDSA, ML-DSA-44/65/87, Falcon-512/1024, SLH-DSA-SHA2-128s, and six hybrids combining ECDSA with each post-quantum scheme. We measure signing and verification costs, transaction-processing throughput, and signature and public-key sizes, and project the measured overheads onto five public blockchains: Bitcoin, Ethereum, Solana, BNB Smart Chain and TRON. Verification remains inexpensive for the evaluated lattice-based schemes, with Falcon-512 achieving a verification time comparable to ECDSA (30.1 versus 32.8 $\mu$s). Storage overheads, however, are substantial. Under our modelling assumptions, had the recorded transaction histories used Falcon-512, the most compact post-quantum scheme evaluated, ledger sizes would have been 79--229% larger, depending on the blockchain. Hybrid configurations introduce relatively modest additional storage overhead compared with their standalone post-quantum counterparts, while ECDSA+Falcon-512 approximately doubles the verification cost of standalone Falcon-512. Existing transaction- and script-size limits also present obstacles to straightforward migration in Bitcoin and Solana. Overall, our findings suggest that storage overhead may pose a greater challenge than signature verification costs when migrating blockchain systems to post-quantum cryptography.

</details>

### [Poisoning Attacks to Local Differential Privacy Protocols for Dynamic Graphs](https://arxiv.org/abs/2611.34340)
*Shang Liu, Yuhan Bao, Hongbin Zhao et al.* · `cs.CR` · arXiv:2611.34340v1 · relevance 0.12

- **In one sentence**: This paper studies data poisoning attacks, where malicious users inject fake nodes and edges, against local differential privacy protocols that estimate statistics of dynamic graphs, and proposes a temporal attack strategy (TEA) with an absolute gain metric.
- **In plain words**: Some systems collect information about who connects to whom in a network while keeping each person's data private by adding noise on their own device. This paper shows that such systems can be manipulated: an attacker who injects fake users and fake connections can distort the statistics estimated for chosen target users. The authors design an attack that decides how many fake users to add at each point in time, and report that it significantly reduces the accuracy of the estimates.
- **Why it matters**: Privacy-preserving data collection is increasingly used, and this work points out that its privacy guarantees do not protect the accuracy of results against malicious participants. The text does not say how these attacks would perform against deployed systems or what defenses exist, so its practical reach is uncertain.
- **Background needed**: - Dynamic graph: a network whose nodes and edges (connections) change over time, such as a social network.
- Local differential privacy (LDP): each user adds random noise to their own data before sending it, so the collector never sees raw data, at some cost in accuracy.
- Data poisoning attack: deliberately feeding false data into a system so that its outputs are wrong.
- Fake nodes and edges: attacker-created accounts and connections submitted as if they were real users.
- Graph statistics: summary measures of a network, such as degree (how many connections a node has), estimated for a target node.
- Absolute gain metric: the paper's measure of total deviation of estimates from their pre-attack values, summed across time. · level: research-level

<details><summary>Original abstract</summary>

With the increasing adoption of privacy-preserving techniques in dynamic graph analysis, local differential privacy (LDP) has become a fundamental paradigm for protecting user data in decentralized environments. However, despite its strong privacy guarantees, LDP-based dynamic graph protocols remain vulnerable to data poisoning attacks through malicious data injection. In this paper, we present the first systematic study of data poisoning attacks against privacy-preserving dynamic graphs under the LDP framework. Considering the temporal evolution of dynamic graphs, we identify key challenges in attack design and evaluation, including how to schedule attack resources across time and how to measure cumulative attack impact. To address these challenges, we introduce an absolute gain metric to quantify the overall deviation of graph statistical metrics before and after attacks across time. Based on this metric, we further propose a unified poisoning attack framework for dynamic graphs, which consists of target node selection, dynamic fake node scale scheduling, and fake edge injection. Within this framework, we design a temporal enhanced attack (TEA) strategy that dynamically schedules attack resources to maximize attack effectiveness, along with two baseline strategies, equal-scale attack (ESA) and random-scale attack (RSA), for comparison. Extensive experiments on real-world and synthetic datasets demonstrate that the proposed attacks can significantly degrade the accuracy of graph metric estimation for target nodes.

</details>

## Algorithms and complexity

### [Toggle Tree: A New Data Structure for Efficient Parallel Graph Processing](https://arxiv.org/abs/2611.33738)
*Xinjian Jiang, Youzhe Liu, Yan Gu et al.* · `cs.DS` · arXiv:2611.33738v1 · relevance 0.16

- **In one sentence**: The paper introduces the Toggle Tree, a parallel data structure built on hierarchical bit vectors that represents vertex frontiers for graph algorithms and exposes IndexSet and IndexMap interfaces, and reports faster implementations of five graph problems than GBBS and PASGAL.
- **In plain words**: Many computer programs that explore networks, such as road maps or social graphs, keep track of a changing "to-do list" of nodes to visit next. This paper proposes a new way to store that list so that many processor cores can update and scan it at the same time. The authors use it to build five standard network algorithms and report that these versions run substantially faster than existing published versions on large real-world graphs.
- **Why it matters**: Speeding up core routines like breadth-first search and shortest paths on very large graphs matters for any field that analyzes big networks. The text claims both theoretical guarantees and practical speedups, but the abstract alone does not show the size of the gains or the conditions under which they hold, so those details need checking in the full paper.
- **Background needed**: - A graph is a set of nodes (vertices) joined by links (edges), such as a network of web pages or roads.
- A "frontier" is the set of nodes currently being processed in a search step, like the current ring of a ripple spreading outward.
- Sparse frontiers store a list of active nodes; dense frontiers store a yes/no mark for every node. The paper tries to combine the strengths of both.
- A bit vector is a compact row of 0/1 flags; hierarchical means these flags are organized in layers, so large empty regions can be skipped quickly.
- Parallel processing means splitting work across many processor cores at once.
- Baselines named: GBBS and PASGAL are existing graph-processing frameworks/systems used for comparison.
- Algorithms named: breadth-first search, k-core decomposition, graph coloring, Bellman-Ford shortest paths, and weighted BFS. · level: research-level

<details><summary>Original abstract</summary>

We present the Toggle Tree, a parallel data structure for frontier-based graph algorithms. A Toggle Tree is used to represent a subset of vertices using hierarchical bit vectors, enabling efficient parallel updates, traversal, and set-wise reductions without global packing. It provides an IndexSet interface that unifies a wide range of parallel graph algorithms under a common abstraction of frontiers and active sets, and an IndexMap interface that also incorporates priority-queue semantics. Specifically, the Toggle Tree aims to combine the advantages of traditional sparse and dense frontier representations, offering both provable theoretical guarantees and high efficiency in practice. Using Toggle Trees, we implement five fundamental graph algorithms, including breadth-first search (BFS), k-core, degree-based graph coloring, single-source shortest paths using Bellman-Ford, and weighted-BFS (wBFS). Across a diverse set of large real-world graphs and the five graph problems, our implementations outperform state-of-the-art baselines, including GBBS and PASGAL, achieving substantial speedups. Our code is publicly available.

</details>

### [Computing Normal-Form Correlated Equilibria in Extensive-Form Games is in PPAD](https://arxiv.org/abs/2611.34897)
*Vincent Cheval, Florian Horn, Soumyajit Paul et al.* · `cs.GT` · arXiv:2611.34897v1 · relevance 0.10

- **In one sentence**: The paper shows that finding a normal-form correlated equilibrium in succinct extensive-form games with perfect recall lies in PPAD for any number of players, and that computing one with support size quadratic in the game size is PPAD-hard even for two players.
- **In plain words**: The paper asks how hard it is to compute a "correlated equilibrium" in games where players make decisions over several turns, a setting where a shared random signal can coordinate their choices. The authors place this computational task in PPAD, a complexity class that captures problems whose solutions are guaranteed to exist but are believed to be hard to find. They also show a matching hardness result, but only for solutions with a restricted number of possible signal outcomes.
- **Why it matters**: The authors describe this problem as a major open question in algorithmic game theory, so placing it in PPAD is a step toward understanding its difficulty. The text does not discuss applications beyond game theory, so its wider relevance is unclear from this text alone.
- **Background needed**: - Game theory: a model of strategic interaction among players, each choosing actions to maximize their own payoff.
- Extensive-form game: a game played over a tree of sequential decisions; perfect recall means players remember their own past choices.
- Correlated equilibrium: a stable outcome where a trusted shared random signal recommends actions to players, and no player gains by deviating from the recommendation.
- Normal-form correlated equilibrium: a version of correlated equilibrium defined over the full strategy space of the game, which can be exponentially large.
- Support size: the number of distinct signal outcomes used in the equilibrium; a smaller support is a simpler solution.
- PPAD: a complexity class for search problems where a solution always exists by a parity or fixed-point argument, but efficient algorithms are not known; hardness here suggests no efficient algorithm is likely.
- Succinct game: a game whose description is compact relative to its full size. · level: research-level

<details><summary>Original abstract</summary>

We study the computational complexity of finding any normal-form correlated equilibria (NFCE for short) in the succinct games of extensive-form with perfect recall, which is considered as a major open problem in algorithmic game theory. Our main results place this problem in PPAD for an arbitrary numbers of players. Our second result establishes PPAD-hardness of computing such an NFCE with support size of at most quadratic in the size of the game, even for two-player games. The posed restriction on the support size in PPAD-hardness construction is motivated by our PPAD algorithm, which constructs an NFCE with support size quadratic in the size of the input extensive-form game.

</details>

## Programming languages and formal methods

### [Direct cognition problem: a semantic skeleton of mathematics and its growth](https://arxiv.org/abs/2611.34210)
*Vasilii A. Gromov, Nikolai N. Evdokimov* · `cs.LO` · arXiv:2611.34210v1 · relevance 0.11

- **In one sentence**: The paper builds a finite set of reusable intermediate lemmas ("anchors") from the three axioms of classical propositional logic, grown without a fixed target theorem, and reports that these anchors shorten proofs of previously unseen structures in two external corpora.
- **In plain words**: The authors start from three basic rules of logic and let a program grow a small library of useful intermediate results, chosen by how often they get reused across many proofs. They then test whether this library makes new proofs shorter, and report that it does on two sets of held-out proofs. The text gives only a summary, so the details of the method and how the proof counts were measured are not visible here.
- **Why it matters**: It is a concrete, measured attempt to find shared structure underlying many proofs, which bears on how proof assistants and automated theorem provers could reuse lemmas. The reported gains are modest in some cases and rest on a post hoc test, so the claim should be read cautiously; the wider significance is unclear from this text alone.
- **Background needed**: - Propositional logic: statements built from "and", "or", "not", "if-then", with no quantifiers.
- Axioms: starting rules assumed true; every proof is built from them.
- Proof structure / combinator: a proof written as a tree of simple steps, here in a typed combinator style.
- Lemma: a helper result proved once and reused in later proofs.
- Anchor: a lemma the paper selects as a reusable building block.
- Post hoc test: an analysis done after seeing the results, so it is weaker evidence than a pre-planned test. · level: research-level

<details><summary>Original abstract</summary>

We construct a finite semantic skeleton from three axioms of classical propositional logic without specifying a target theorem. During growth, the constructor records which proofs share an intermediate lemma. When choosing the final anchors, it also counts inferences that use a premise the lemma can supply by substitution. The primary skeleton contains ten anchors whose certificates expand to the axioms through 27 shared inference steps. It shortens all 30 previously unseen proof structures in an external catalogue of typed combinators, saving 90 of 412 steps. One anchor recurs in all five runs of the constructor. In a post hoc test, this anchor alone shortens 26 of the 30 proofs. It also shortens 331 of 475 previously unseen proofs of familiar theorems in a second corpus.

</details>

### [Higher-Order Generation of First-Order Theories](https://arxiv.org/abs/2611.34714)
*Ziyue Jin, Umang Mathur* · `cs.LO` · arXiv:2611.34714v1 · relevance 0.07

- **In one sentence**: The paper introduces a logic whose formulas finitely describe possibly infinite first-order theories generated by higher-order recursion schemes, and studies their expressiveness, model checking, and satisfiability under conjunctive and disjunctive interpretations.
- **In plain words**: The paper is about a way to describe very large, even infinite, collections of logical statements using a short, structured recipe. The recipe is a small grammar that can build statements in layers, where the building blocks can themselves be operations. The authors work out how much these descriptions can express, how hard it is to check whether a structure satisfies them, and when it is possible to tell whether such a collection can be satisfied at all.
- **Why it matters**: The paper gives exact complexity results: over finite ordered structures, disjunctive theories at each scheme order match a level of the exponential-time hierarchy, and one fragment's satisfiability becomes undecidable already at order one. It extends earlier work on regular first-order theories (Mathur et al., POPL 2025), so it is mainly of interest to researchers in logic and verification; its wider relevance is not addressed in the text.
- **Background needed**: - First-order logic: statements using "for all", "there exists", and relations between objects.
- Theory: a set of such statements; a model is a structure that makes them all true.
- Satisfiability: whether some model exists; decidable means a program can always answer yes or no.
- Model checking: testing whether a given structure satisfies a given theory.
- Higher-order recursion scheme: a finite grammar that generates trees, where rules can take other rules as inputs.
- Complexity classes: polynomial time (0-EXPTIME) and the exponential-time hierarchy (k-EXPTIME), which bound how long the best algorithms need as problems grow.
- Conjunctive vs. disjunctive reading: a model must satisfy all generated sentences vs. at least one. · level: research-level

<details><summary>Original abstract</summary>

We introduce a logic whose formulae are finite descriptions of possibly infinite first-order theories. A theory is a set of first-order sentences, generated in our setting by a higher-order recursion scheme. Such a scheme is a finite grammar whose parameters may denote trees or operations on trees. We consider two interpretations: a model must satisfy every generated sentence under the conjunctive interpretation, and at least one under the disjunctive interpretation. For schemes of order $k=0$, these theories coincide with the regular first-order theories of Mathur et al. (POPL 2025). We generalize this representation by allowing higher-order schemes, while retaining first-order quantification in every generated sentence. We study the expressive power, model checking, and satisfiability of this logic. Over finite ordered structures, we show that disjunctive theories of existential sentences generated at order at most $k$ capture $k$-EXPTIME, for every $k\geq0$. Allowing unrestricted first-order sentences captures $(k+1)$-EXPTIME at the same scheme order, where $0$-EXPTIME denotes polynomial time. We also give model-checking algorithms in the corresponding time classes for each fixed signature, variable-name set, and order bound. For satisfiability under either interpretation, we extend several decidability results for regular theories to every order. However, we show that conjunctive satisfiability of quantifier-free theories, decidable at order zero, becomes undecidable already at order one. Finally, we recover decidable conjunctive satisfiability at every order by separating higher-order generation of Boolean structure from independent regular generation of ground atoms. Together, these results show how higher-order generation of first-order syntax captures the exponential-time hierarchy while retaining decidable satisfiability in restricted fragments.

</details>

## Systems and networking

### [A Differential Computing Accelerator for LLM Inference Leveraging Bit-Slice Transition Sparsity](https://arxiv.org/abs/2611.34630)
*Yifan Wang, Zetao Guo, You Xiao et al.* · `cs.AR` · arXiv:2611.34630v1 · relevance 0.06

- **In one sentence**: ISTS is a hardware-software co-designed accelerator that reuses partial sums across bit-slice vectors clustered near shared representative patterns (Steiner points) to speed up quantized LLM matrix multiplications.
- **In plain words**: Running large language models requires huge numbers of multiplications, and chips are often limited by time and memory for these operations. This paper proposes a chip design that breaks the numbers being multiplied into their individual bits and notices that many of the bit patterns are very similar to a few common ones. By reusing the results already computed for those common patterns, the chip does less work. The authors report average speedups of 1.27x to 3.09x over five existing accelerator designs in their evaluations.
- **Why it matters**: Faster and cheaper matrix multiplication matters for deploying LLMs on limited hardware, so the approach is worth watching. The reported gains come from the authors' own comparisons, and the text does not show how the design performs beyond those benchmarks or in real deployments.
- **Background needed**: - Large language models (LLMs): AI systems whose core workload is huge grids of multiplications (general matrix multiplication, GEMM).
- Quantization: storing numbers with fewer bits to save memory and computation.
- Bit slices: splitting a number into its separate binary digits, grouped by position, so each group can be processed on its own.
- Hamming distance: the count of bit positions where two patterns differ; "a few bit flips away" means two patterns differ in only a few places.
- Partial sums: intermediate totals accumulated during a multiplication; reusing them avoids recomputing.
- Steiner point: here, a representative pattern that nearby patterns are derived from with a few additions or subtractions.
- Accelerator: specialized hardware built to run one type of computation faster than a general processor. · level: research-level

<details><summary>Original abstract</summary>

Large language models (LLMs) have become foundational to modern artificial intelligence. Driven by scaling laws, their rapid growth poses increasing computational and memory challenges for deployment. To accelerate the general matrix multiplication (GEMM) operations that dominate LLM computation, bit-slice architectures decompose quantized operands along the bit dimension, exposing slice-level sparsity and redundancy. However, existing bit-slice designs primarily exploit sparsity in high-order slices, while dense low-order slices still offer substantial untapped reuse opportunities. We observe that bit-slice vectors (BSVs) are highly clustered in Hamming space, with many BSVs lying only a few bit flips away from a small set of representative patterns. Based on this observation, we propose ISTS, an algorithm-hardware co-designed accelerator that leverages representative BSV patterns as shared Steiner points to reuse partial sums across slices, substantially reducing computation. Specifically, the partial sum of each target BSV can be reconstructed from that of its assigned Steiner point using only a few additions or subtractions. On the algorithmic side, we propose Steiner Absorption Table Construction (SATC), which selects a compact set of Steiner points to absorb BSVs with only a few bidirectional bit flips, while FlipPrune selectively prunes flips to further expand the reusable BSV population. On the hardware side, we design a lightweight accelerator that supports Steiner reuse for static linear layer weights and runtime-generated attention K/V tensors. Comprehensive evaluations show that ISTS achieves average speedups of $3.09\times$, $2.41\times$, $2.18\times$, $1.27\times$, and $1.41\times$ over the state-of-the-art accelerators ANT, BBS, LUT Tensor Core, Transitive Array, and MCBP-BRCR, respectively.

</details>

### [Relieving Hotspot Congestion in Large-Scale Low Earth Orbit Satellite Networks via Distributed Dual-Timescale Traffic Splitting](https://arxiv.org/abs/2611.34329)
*Shuyang Li, Guanchen Wu, Qiang Wu et al.* · `cs.NI` · arXiv:2611.34329v1 · relevance 0.06

- **In one sentence**: BRACE is a two-timescale distributed traffic-splitting scheme for LEO satellite networks that combines slowly computed destination-aware splits (keeping every admissible port non-zero) with fast, constant-time per-hop reweighting based on instantaneous local queues, evaluated in 144-satellite flow-level simulations.
- **In plain words**: Low Earth orbit satellite networks carry internet traffic between satellites, and some links become overloaded when too much traffic is routed through the same spot. This paper proposes a method that decides how each satellite spreads its traffic across its possible outgoing links, updating the big plan slowly and the quick adjustments rapidly based on how full each local queue is. In simulations of a 144-satellite network, the authors report it lost fewer packets than a tuned congestion-aware heuristic under the same hotspot conditions.
- **Why it matters**: Congestion at satellite links directly affects broadband access from space, which is part of the non-terrestrial networking role envisioned for 6G. The idea of keeping a small share of traffic on every usable route while adjusting quickly to queues may be relevant to other distributed routing problems, though the text does not establish wider applicability.
- **Background needed**: - LEO satellites orbit roughly a few hundred to a couple thousand km up, and they connect to each other via inter-satellite links, forming a moving mesh network.
- Traffic splitting means sending a flow's packets across several outgoing links in chosen proportions, rather than one fixed path.
- A queue is the waiting line of packets at a link; queue length signals congestion.
- Packet drop rate is the fraction of packets discarded when queues overflow; it is a common measure of congestion harm.
- Two timescales: a slow layer updates the split plan periodically (cheap for onboard computers), while a fast layer makes quick local tweaks using current queue sizes.
- Flow-level simulation models traffic as whole flows rather than individual packets, which is faster but simplifies real behavior.
- The results are simulation-only and the text gives no details on the reward function or baselines beyond their names. · level: research-level

<details><summary>Original abstract</summary>

Sixth-generation mobile systems envision ubiquitous connectivity through non-terrestrial networks, in which low Earth orbit (LEO) satellite networks play a key role by extending broadband access beyond terrestrial infrastructure. Traffic hotspots in LEO satellite networks congest inter-satellite links, and short flows leave end-to-end congestion control little time to react. In distributed traffic splitting, recomputing splits at every queue change increases onboard computation, whereas periodic splits miss such changes and withhold zero-weight ports from faster queue-based reweighting. We formulate the distributed slow-layer traffic-splitting problem, whose objective combines throughput, queueing delay, traffic loss, and short-flow completion time, and propose Balanced Routing with Admissible Ports and Congestion Control at Two Timescales (BRACE). Its slow layer assigns destination-aware splits with a positive weight on every admissible port, and its fast layer reweights them in constant time per hop using instantaneous local queues. In 144-satellite flow-level simulations, BRACE achieves the highest reward among the tested distributed methods in all seven hotspot conditions and 28-45% lower drop rates than the lowest-loss baseline, a tuned congestion-aware heuristic, in the three highest-load conditions. Without retuning, its drop rates are 26-76% lower than that baseline's at calibrated loads in constellations of up to 1584 satellites.

</details>

## Human-computer interaction

### [MidasTUI: Instant Tangible User Interfaces for Wearable Displays using Everyday Objects](https://arxiv.org/abs/2611.34945)
*Wen Ying, Xuweiyi Chen, Zezhou Cheng et al.* · `cs.HC` · arXiv:2611.34945v1 · relevance 0.12

- **In one sentence**: MidasTUI turns ordinary objects into temporary input devices for wearable displays by using the headset camera and a Transformer-based temporal classifier to detect hand-object motion, infer the intended input type (slider, mouse, keypad), and map it to an app function.
- **In plain words**: Wearable displays such as smart glasses can show a full workspace, but controlling them usually means waving your hands in the air, which is tiring and gives no physical feedback, or carrying a separate controller. This paper proposes using everyday objects instead: for example, sliding an earbud case across a table can act as a mouse. The system watches the user's hand through the display's camera, works out what kind of control the motion is meant to be, and links it to an action on screen.
- **Why it matters**: The work addresses a practical usability problem for head-worn displays, and it reports a comparative user study claiming lower physical burden and better perceived usability than mid-air gestures. The text gives no detailed numbers, so the strength of these claims can't be judged from this summary alone; it may matter for how future wearable interfaces handle input.</why>
<parameter name="background">- Tangible user interface: a control built from physical objects a person can touch, rather than purely on-screen or in-air controls.
- Wearable display: a head-worn screen (such as smart glasses) that overlays digital content on the real world.
- Mid-air gestures: hand movements made without touching anything, which can cause arm fatigue and offer no tactile feedback.
- Temporal classifier: a machine-learning model that labels sequences of sensor data over time; a Transformer is a common neural-network architecture for this.
- Cross-object and cross-user generalization: whether the system still works on objects and people it was not trained on.</background>
<parameter name="difficulty">intermediate

<details><summary>Original abstract</summary>

While wearable displays can bring digital workspaces anywhere, interaction remains limited by mid-air gestures that lack tactile feedback and induce fatigue, or controllers that are cumbersome to carry. We present MidasTUI, a system that instantly transforms arbitrary everyday objects into opportunistic tangible user interfaces through brief interaction demonstrations. For example, a user can slide an earbud case across a table as a mouse, enabling opportunistic interaction without carrying a dedicated input device. MidasTUI detects when a user is holding and moving an object using the wearable display camera and a Transformer-based temporal classifier. It then infers the intended input modality (e.g., slider, mouse, keypad) from hand movement and maps the tracked hand-object interaction to an application function. Our evaluations demonstrate reliable cross-object and cross-user generalization. A comparative user study further shows that grounding interaction in everyday objects reduces physical burden and improves perceived usability and control relative to mid-air interaction.

</details>

### [Towards Democratized Academic LLM Hosting: Practical insights from needs, implementations, and governance across Dutch institutions](https://arxiv.org/abs/2611.34383)
*Azza Ahmed, Sreeparna Deb, Taylor Stone et al.* · `cs.CY` · arXiv:2611.34383v1 · relevance 0.08

- **In one sentence**: A workshop-based synthesis of needs, implementation practices, and governance challenges for institutionally hosted large language model (LLM) services across Dutch academic institutions.
- **In plain words**: Universities increasingly want to run their own AI chatbot-style tools instead of relying only on outside commercial services. This paper reports on a workshop with people from university IT, research support, education, and policy, and summarizes the practices, tensions, and open questions they raised. The text itself is a high-level overview; it does not report measured results.
- **Why it matters**: Decisions about where and how universities host AI tools touch on cost, energy use, data control, and fairness of access, so practical accounts of these choices are useful to people running or funding such services. The text is a short abstract-level description, so it is hard to judge how deep the findings go; it may be most relevant to research-infrastructure and digital-policy readers.
- **Background needed**: - LLM (large language model): the kind of AI behind chatbots and text-generating tools.
- Hosting: running the software on one's own servers or a managed environment, rather than only using a company's website or API.
- Institutionally governed: the university sets the rules on access, data, and responsible use.
- Democratized access: making such tools available broadly across an institution, not just to well-funded groups.
- Socio-technical: involving both technology and the people, rules, and organizations around it.
- Energy and utilization: how much electricity the hardware uses and how much of its capacity is actually used.
- Dutch academia: the universities and research institutes in the Netherlands. · level: introductory

<details><summary>Original abstract</summary>

Academic LLM hosting is emerging as an operational infrastructure domain with recurring socio-technical patterns, tensions, and governance requirements across institutions. Based on a workshop with academic infrastructure, research-support, education, and policy-adjacent stakeholders, this paper synthesizes current practices and open questions around institutionally governed LLM services for Dutch academia. It highlights challenges around deployment models, energy and utilization, governance, tooling, commercial integration, and research and education use cases, and identifies emerging directions for service pathways, coordination, and responsible operation.

</details>

## Information theory

### [Exponential Analysis for Trace-Distance Errors in Quantum Information Theory](https://arxiv.org/abs/2611.34468)
*Hao-Chung Cheng, Li Gao, Shi-Bing Li et al.* · `quant-ph` · arXiv:2611.34468v1 · relevance 0.17

- **In one sentence**: The paper determines exact exponential rates (reliability functions and strong converse exponents, in the i.i.d. setting) at which trace-distance errors vanish or blow up for classical-quantum soft covering, privacy amplification, convex splitting, and Haar-random decoupling, with formulas in terms of sandwiched and Petz Rényi information.
- **In plain words**: This paper is about how fast the error shrinks when quantum information is scrambled, shared, or hidden. The errors are measured with "trace distance," a standard way of asking how easily two quantum states can be told apart. The authors work out the exact exponential rates at which these errors fall (and, in the other regime, rise) for several standard quantum protocols when many copies are used.
- **Why it matters**: Exact error exponents tell engineers and theorists precisely how many resources a protocol needs for a given reliability, which matters for secure communication and quantum data processing. The text does not say how these results will be used in practice, so their wider impact is unclear from this summary alone.
- **Background needed**: - Quantum states: descriptions of quantum systems, often mixed, written as density matrices.
- Trace distance: a measure of how distinguishable two quantum states are, between 0 and 1.
- Reliability function: the exponent describing how quickly the error probability falls as the block length grows.
- Strong converse exponent: the exponent describing how quickly success vanishes when the transmission rate is pushed past the limit.
- Soft covering and convex splitting: protocols that make a random set of states look like a target state.
- Privacy amplification: shrinking a partly secret key so an eavesdropper who has quantum side information learns almost nothing.
- Decoupling: randomising a system so that it becomes uncorrelated with a part of itself or with a reference.
- Sandwiched and Petz Rényi information: families of entropy-like quantities that generalise Shannon information to quantum states.
- Quantum hypothesis testing: deciding which of two quantum states a system is in, the tool linking these errors to the exponents. · level: research-level

<details><summary>Original abstract</summary>

We study the trace-distance error in classical-quantum soft covering, privacy amplification against quantum side information, convex splitting, and decoupling by a Haar-random unitary followed by partial trace. In the independent and identically distributed setting, we determine exact reliability functions and strong converse exponents for soft covering with independent codewords, uniform convex splitting, and Haar partial-trace decoupling. For privacy amplification, we determine the exact reliability function for independent random binning and the exact strong converse exponent for every two-universal hash ensemble. The reliability and strong converse formulas involve sandwiched and Petz-R\'enyi information, respectively. The proofs connect trace-distance errors to quantum hypothesis testing, using Rosenthal inequalities for sums of random matrices in the reliability analysis and conditional second-moment bounds for the strong converses.

</details>

### [What Must LLM Agents Communicate? From Information Loss to Communication Failures](https://arxiv.org/abs/2611.33318)
*Yi-Yun Chu, Xiaobin Shen* · `cs.MA` · arXiv:2611.33318v1 · relevance 0.11

- **In one sentence**: A framework drawing on information theory and communication complexity that asks what messages LLM agents must exchange so a team can make accurate joint predictions when evidence is spread across them, tested with controlled experiments and message-level analysis.
- **In plain words**: Several AI agents may each hold a piece of the evidence needed for a decision, and together they may have enough to decide well, yet still fail to do so. The paper asks what those agents must tell each other, and when talking back and forth actually helps. The authors compare theoretical limits on how much information gets lost with the results of controlled experiments.
- **Why it matters**: Multi-agent LLM systems are increasingly used for joint reasoning, so knowing whether failures come from fundamental limits or from poor communication habits matters for designing them. The link to communication complexity and information loss gives the work a principled footing, though the text alone does not show how broadly the findings generalize beyond the authors' experiments.
- **Background needed**: - Multi-agent LLM system: several language-model instances that each see part of a problem and exchange messages.
- Information theory: the mathematical study of how much information can be stored, sent, and lost.
- Communication complexity: a field asking how many bits two or more parties must exchange to compute a joint answer.
- Sufficiency: whether a message keeps all the information needed for the final decision.
- Information loss: information discarded when an agent compresses its evidence into a summary, such as a probability report.
- Query-first interaction: an agent first states what it needs to know, so others send only relevant evidence. · level: research-level

<details><summary>Original abstract</summary>

When evidence is distributed across LLM agents, a team may collectively possess all the information needed for a decision yet fail to use it effectively. What must agents communicate for accurate joint predictions, and when does interaction help? We study three requirements for effective communication: sufficiency of the information conveyed, selection of relevant evidence, and utilization of received information. Drawing on information theory and communication complexity, we develop a framework that combines theoretical benchmarks with controlled experiments and message-level analyses. We find that local probability reports can discard essential information, with theoretical information loss closely matching observed performance penalties. Query-first interaction improves predictions when relevant evidence depends on a private query, but compact one-shot representations can eliminate this advantage. Even when sufficient information is communicated, agents may fail to select or use it correctly. Together, these findings distinguish fundamental communication limits from failures in how LLM agents communicate and use information.

</details>

## High-energy theory and gravity

### [Kiselev black hole from semiclassical gravity with conformal anomaly](https://arxiv.org/abs/2611.34026)
*Yu-Sen An, Yu-Lin Chen* · `gr-qc` · arXiv:2611.34026v1 · relevance 0.21

- **In one sentence**: Solves the semiclassical Einstein equations with both type-A and type-B conformal anomaly contributions for a special relation between central charges and the cosmological constant, obtaining an exact Kiselev-type black hole metric.
- **In plain words**: This paper studies how quantum effects of matter fields near a black hole can change the black hole's shape in spacetime. The authors include the "type-B" part of a quantum effect called the conformal anomaly, not just the "type-A" part that earlier work used. For one specific relation between the theory's central charges and the cosmological constant, they find the equations can be solved exactly, giving a black hole of the known Kiselev form.
- **Why it matters**: Quantum corrections from the conformal anomaly are a candidate way to modify black hole geometry near where classical gravity breaks down, so a closed-form solution is a useful reference point. The text presents this mainly as a stepping stone toward studying black holes under the full anomaly; its broader physical significance is not established in the text.
- **Background needed**: - Black hole: a region of spacetime whose gravity is so strong that nothing escapes; described by a metric (a formula for distances and times).
- Semiclassical gravity: Einstein's gravity with the average quantum stress-energy of matter fields added as a source.
- Conformal anomaly: a quantum effect where the trace of the stress-energy tensor does not vanish, even for massless fields, under rescaling of distances. It is split into type-A and type-B parts, with coefficients called central charges.
- Cosmological constant: a term in Einstein's equations describing a background energy that affects large-scale spacetime curvature.
- Kiselev black hole: a known family of black hole solutions surrounded by an energy-density field with a specific equation of state.
- Exact solution: a closed-form answer to the equations, as opposed to a numerical or approximate one. · level: research-level

<details><summary>Original abstract</summary>

Investigating black hole physics in semi-classical gravitational theory is an interesting and important direction. When the backreaction of the conformal anomaly-induced effective stress-energy tensor is taken into account, the black hole spacetime can be largely altered which changes many properties of the black hole. In this work, rather than restricting our attention to the type-A anomaly, we incorporate the type-B anomaly and investigate how it modifies the spacetime structure obtained when only the type-A anomaly is considered. We find that for a specific relation between the central charges and the cosmological constant, the semiclassical Einstein equations can be solved analytically, yielding a metric that takes the exact form of the Kiselev black hole. After deriving the solution, we further discuss the properties of this new black hole solutions. Our work serves as an essential stepping stone for studying black hole geometries under the full conformal anomaly.

</details>

### [The all-loop spectrum of GGK strings](https://arxiv.org/abs/2611.34619)
*Marius de Leeuw, Andrea Fontanella, Cameron Gibson et al.* · `hep-th` · arXiv:2611.34619v1 · relevance 0.18

- **In one sentence**: Studies the non-perturbative spectrum of GGK theory (the non-relativistic limit of string theory on AdS5×S5), showing in light-cone and static gauges that the bosonic spectrum on several vacua matches free massive and massless scalars in AdS2 at all loops, and that the quantum correction to the classical energy vanishes under regularised Hurwitz series summation.
- **In plain words**: This paper looks at a simplified, non-relativistic version of string theory, a framework that describes tiny vibrating strings moving in a curved space. The authors work out the full set of possible energy levels for these strings, including quantum effects at every order of approximation. They find that, for the cases they study, the energies come from free particles in a lower-dimensional curved space, and that the quantum corrections cancel out, leaving only the classical energy.
- **Why it matters**: It tests a conjecture by de Leeuw, Fontanella and Nieto-García (arXiv:2403.09563) about this limit, and it bears on the broader question of how exactly solvable the spectrum of strings in AdS/CFT is. The reliance on regularised Hurwitz series for the vanishing correction is a technical choice whose broader physical meaning is not explained in the text, so its wider significance is uncertain.
- **Background needed**: - String theory: models in which particles are tiny one-dimensional strings whose vibrations give the particle spectrum.
- AdS5×S5: a specific curved background (five-dimensional anti-de Sitter space times a five-sphere) central to the AdS/CFT correspondence.
- Non-relativistic limit: a simplified regime where the speed of light is effectively taken to be large, so the theory becomes easier to solve.
- GGK string: a string solution in this non-relativistic limit, studied here.
- Light-cone and static gauge: choices of coordinates that remove redundant freedom in describing the string.
- Vacuum and classical energy: a stable lowest-energy configuration of the string and its energy before quantum effects.
- All-loop / quantum correction: effects from quantum fluctuations summed over all orders of approximation.
- AdS2 scalar fields: particles of spin zero living in a two-dimensional anti-de Sitter space.
- Hurwitz series regularisation: a mathematical technique for assigning finite values to divergent sums. · level: research-level

<details><summary>Original abstract</summary>

We study the non-perturbative spectrum of the non-relativistic limit of string theory in AdS$_5\times$S$^5$, also known as GGK theory. In light-cone gauge, we show that the bosonic spectrum on a number of vacua is described at all-loops by free massive and massless scalar fields in AdS$_2$, confirming a conjecture by de Leeuw, Fontanella and Nieto-Garc\'ia, arXiv:2403.09563. In static gauge, we obtain the same result for any classical string vacuum, and including fermions. We compute the quantum correction to the classical energy, and show that it vanishes once we adopt the regularised Hurwitz series. We conclude that the quantum energy spectrum built upon any GGK string consists solely of its classical vacuum energy.

</details>

## Statistical physics

### [Discrete truncated Wigner approximation of the quantum phase transition in the transverse-field Ising model](https://arxiv.org/abs/2611.34004)
*Tuan-Vu Truong, Hoang-Long Nguyen* · `quant-ph` · arXiv:2611.34004v1 · relevance 0.17

- **In one sentence**: This paper tests whether the discrete truncated Wigner approximation (DTWA), a semiclassical method for spin dynamics, captures the Kibble-Zurek scaling of the transverse-field Ising model's quantum phase transition in one to three dimensions and for all-to-all coupling.
- **In plain words**: The study looks at a magnet made of tiny quantum spins that is slowly or quickly tuned through a point where it switches from disordered to ordered. The authors test a cheaper approximate simulation method (DTWA) against more exact quantum Monte Carlo results. They report that the method fails on a one-dimensional chain, locates the onset of order reasonably well in square and cubic lattices, but does not reproduce the universal scaling of the transition there; for all-to-all coupling it tracks the exact order growth.
- **Why it matters**: Large quantum systems are hard to simulate exactly, so knowing where a cheap approximation can be trusted matters for researchers using it. The text suggests the method's reliability grows with the number of neighbours each spin interacts with, but this is a finding about one model and one method, not a general verdict.
- **Background needed**: - Spin: a tiny quantum magnet, which can point up or down.
- Transverse-field Ising model: a standard model of spins on a lattice that compete to align, with a field that flips them sideways; it has a quantum phase transition between disordered and ordered states.
- Quantum phase transition: a change in a system's collective state driven by quantum effects at zero temperature, rather than by heat.
- Ramp: slowly or quickly changing the control parameter (the field) through the transition.
- Kibble-Zurek mechanism: a theory predicting how many defects or how much disorder remains after a transition, depending on ramp speed, following universal power laws (the "exponents").
- Discrete truncated Wigner approximation (DTWA): a semiclassical method that treats quantum spins as classical ones with random initial states to approximate dynamics cheaply.
- Quantum Monte Carlo (QMC): a numerical method using random sampling to simulate quantum systems accurately, used here as the reference.
- Effective temperature: a classical thermal temperature that a relaxing simulation settles into, used to explain DTWA's failure in 1D. · level: research-level

<details><summary>Original abstract</summary>

The discrete truncated Wigner approximation (DTWA) has been a workhorse for large-scale spin dynamics, but whether it captures dynamics across a quantum phase transition has not been tested systematically. In this work, we use the transverse-field Ising model (TFIM) to study the quantum phase transition with DTWA from one to three dimensions and with all-to-all connectivity, using slow linear ramps and fast ramps. We find that DTWA cannot capture the dynamics on the one-dimensional chain, and that its behavior is consistent with classical thermalization, in which its classical spins relax toward a thermal state at a finite effective temperature that does not vanish for slow ramps, while a one-dimensional chain cannot order at any finite temperature. For square and cubic lattices, in contrast to the chain, DTWA builds order, and the order sets in close to the quantum critical point found by quantum Monte Carlo (QMC). However, its correlations do not grow with the Kibble-Zurek exponents, so DTWA captures the onset of order but not the universal dynamics of the transition. For all-to-all coupling, DTWA follows the exact growth of the order parameter along the entire ramp. Our results suggest that DTWA becomes more reliable as each spin interacts with more partners, and that beyond one dimension it can indicate where a quantum phase transition lies but cannot capture its critical scaling.

</details>

### [From Spin Glass Theory to Optimization in High Dimensions and Modern Artificial Neural Networks](https://arxiv.org/abs/2611.34713)
*Riccardo Zecchina, Gianmarco Perrupato* · `cond-mat.dis-nn` · arXiv:2611.34713v1 · relevance 0.14

- **In one sentence**: A tribute chapter reviewing how replica symmetry breaking and cavity methods from spin-glass theory have been applied to combinatorial optimization, random satisfiability, survey propagation, and the geometry of solution spaces in neural networks.
- **In plain words**: This is a review chapter honoring physicist Giorgio Parisi, looking at how ideas he helped develop for disordered magnets (spin glasses) have spread into computer science problems and modern neural networks. It walks through classic puzzles such as matching and the traveling salesman problem, then discusses how the shape of the set of good solutions relates to how hard a problem is to solve and how a network learns. The text is a survey of established ideas and examples rather than a report of one new result.
- **Why it matters**: The chapter links a body of physics theory to practical questions about why some optimization and learning problems are hard and others are easy to solve. Its link to neural network training is of current interest, though the provided text only outlines these connections and does not give specific quantitative findings.
- **Background needed**: - Spin glass: a magnet with randomly mixed friendly and hostile interactions, so it cannot settle into one simple arrangement.
- Replica method: a mathematical trick from physics for averaging over many random systems at once.
- Replica symmetry breaking (RSB): Parisi's refinement, where the set of low-energy states splits into many separated clusters.
- Cavity method: an approximation technique for estimating how a large random system behaves when one piece is removed.
- Combinatorial optimization: finding the best option among a huge number of discrete choices, e.g. shortest route for a traveling salesman.
- Survey propagation: a message-passing algorithm for hard satisfiability problems, derived from the cavity approach.
- Overparameterized model: a neural network with more adjustable weights than training examples. · level: research-level

<details><summary>Original abstract</summary>

This chapter pays tribute to Giorgio Parisi by reviewing the influence of his work on spin glasses and replica symmetry breaking (RSB) on combinatorial optimization and artificial neural networks. We first introduce replica and cavity methods through the matching and traveling salesman problems, before discussing random satisfiability and the development of survey propagation. We then examine applications to neural networks, emphasizing the connections between the geometry of solution spaces, computational hardness, and learning. Particular attention is given to rare regions of high local entropy and their role in algorithmic accessibility. Examples involving overparameterized models and asymmetric recurrent networks illustrate how these ideas connect constrained optimization and inference with concepts developed in spin-glass theory.

</details>

## Condensed matter

### [Nontrivial criticality and weakly first-order transitions in the frustrated spin-1 chain with single-ion anisotropy](https://arxiv.org/abs/2611.34145)
*Qiang Luo, Shijie Hu, Jize Zhao et al.* · `cond-mat.str-el` · arXiv:2611.34145v1 · relevance 0.15

- **In one sentence**: A numerical study (large-scale DMRG plus bosonization) of a frustrated spin-1 chain with next-nearest-neighbour coupling and single-ion anisotropy, mapping its phase diagram and reporting weakly first-order, topological, and deconfined quantum critical transitions.
- **In plain words**: This paper looks at a one-dimensional line of tiny magnetic spins that compete with each other, and asks how their collective behaviour changes as the balance of interactions is tuned. The authors used large computer simulations together with a mathematical reduction method to draw a map of the different ordered states and the boundaries between them. They report several transitions, including a weak first-order one, a continuous one, and a dimerized phase whose edge is described as a deconfined quantum critical point.
- **Why it matters**: The work points to unusual kinds of phase transition in simple quantum chains that go beyond the standard Landau picture of ordering, which is of interest to theorists studying quantum magnets. The text does not establish links to specific experimental materials, so any wider relevance is unclear from this abstract alone.
- **Background needed**: - Spin chain: a row of quantum magnetic moments (spins) coupled to their neighbours.
- Spin-1: each site has three magnetic states; the Haldane phase is a known gapped topological state of such chains.
- Frustration: competing interactions that prevent all neighbours from ordering comfortably; here, next-nearest-neighbour coupling.
- Single-ion anisotropy: a preference of each spin for particular directions, tuned by a parameter D.
- Phase transition: an abrupt or continuous change between states, such as ice melting into water; "first-order" means a jump, "continuous" means a smooth change.
- DMRG (density-matrix renormalization group): a numerical method for approximating ground states of quantum chains.
- Bosonization: a mathematical mapping of such chains onto simpler field theories.
- Deconfined quantum critical point: a transition between two ordered states not described by the usual single-order-parameter theory.
- Central charge c and universality class: numbers that label the type of critical behaviour. · level: research-level

<details><summary>Original abstract</summary>

Frustrated spin chains host exotic phases beyond the Landau paradigm, yet weak first-order transitions and unconventional criticalities remain elusive. Combining large-scale density-matrix renormalization group with bosonization methods, we map the phase diagram of a spin-1 chain with next-nearest-neighbor (NNN) coupling and single-ion anisotropy (SIA). We pinpoint two topological phase transitions: a weakly first-order transition between the Haldane and NNN-Haldane phases with a tiny gap and a continuous transition from the Haldane phase to the large-$D$ phase located via level spectroscopy with Richardson extrapolation. For negative SIA, a spontaneous dimerized phase emerges between the N\'eel and NNN-N\'eel phases. Its transition into the N\'eel phase is a deconfined quantum critical point falling into the eight-vertex universality class, with central charge $c = 1$ and critical exponents varying continuously along the phase boundary. For positive SIA, we identify two vector-spin-chirality orders---an ordinary chiral phase and a narrow Haldane-chiral phase---with a weakly first-order transition between them, evidenced by a soft jump in the string order parameter. Our results reveal that frustration and anisotropy generate emergent orders and non-Landau criticalities, providing a platform for deconfined and topological phase transitions.

</details>

### [Toward a quantum resistance standard above liquid nitrogen temperature](https://arxiv.org/abs/2611.34069)
*Kaining Yang, Changwei Zhai, Naijie Ren et al.* · `cond-mat.mes-hall` · arXiv:2611.34069v1 · relevance 0.14

- **In one sentence**: The paper reports quantized Hall resistance in monolayer graphene interfaced with CrOCl, measured at 50 K and 100 K, which the authors propose as a route to a resistance standard that works above liquid nitrogen temperature.
- **In plain words**: Electrical resistance standards are defined using a quantum effect that normally needs very cold temperatures, around liquid helium levels, to work precisely. This paper describes a graphene device placed on a magnetic-ordered material (CrOCl) that the authors say keeps this effect precise at much warmer temperatures, including 50 K and 100 K. The reported measurements are for a single device under a 12 tesla magnetic field and a 10 microamp current.
- **Why it matters**: A resistance standard that works at 100 K, which can be reached without the liquid helium and bulky refrigerators used today, could make precise electrical measurements cheaper and easier to run. The text does not show how widely the result would reproduce, so its practical reach is still an open question.
- **Background needed**: - Hall effect: when current flows through a conductor in a magnetic field, a voltage appears across it; in the quantum Hall regime this voltage divided by current locks to a fixed value.
- Von Klitzing constant: the fixed value, h/e², where h is the Planck constant and e is the elementary charge; it sets the SI resistance standard.
- Graphene: a single layer of carbon atoms that conducts electricity very efficiently.
- Landau gap: an energy gap that forms for electrons in a magnetic field; a larger gap usually allows the effect to hold at higher temperatures.
- Fermi velocity: how fast electrons move at the top of their energy range; the paper says the interface increases it.
- Direct current comparator (DCC): a precision instrument used to compare two resistances with very high accuracy.
- Parts per billion: a measure of relative error; 23 ppb means the deviation is about 0.000023 percent.
- Kelvin: 50 K is about -223 °C and 100 K is about -173 °C; liquid nitrogen boils near 77 K. · level: research-level

<details><summary>Original abstract</summary>

Quantum Hall effect (QHE) -- the pioneering demonstration of one-dimensional topologically-protected edge channels -- manifest a transversal resistance quantized solely by two universal constants $e$ and $h$ (the elementary charge and the Planck constant, respectively), referred to as the von Klitzing constant $R_\mathrm{K}=h/e^{2}$. For decades, this has enabled a unique route for realizing quantum Hall resistance (QHR) standard in the Syst\`eme international d'unit\`es (SI), yet high precision QHR under relaxed conditions, especially temperature higher than 30 K, has not been possible. Here, we show that interfacial charge-order coupling inbetween CrOCl and monolayer graphene offers enhanced Fermi velocity, creating a robust Landau cyclotron gap. Using a customized direct current comparator (DCC, mounted at room temperature), we obtain relative deviation of the Hall resistance from $R_\mathrm{K}/2$ of (15 $\pm$ 23)\,n$\Omega$ $\Omega$$^{-1}$ (23 parts per billion of relative uncertainty) at 50 K, with an external magnetic field of 12 T and a dc current of 10 $\mu$A. At 100 K, the system exhibits QHR with 2 parts per million of relative uncertainty. Our results therefore suggest a platform toward a next-generation quantum resistance standard that may work at above liquid nitrogen temperature and free of conventional compressor refrigerators.

</details>

## Particle physics

### [Probing Ultralight Dark Matter at the Electroweak Scale](https://arxiv.org/abs/2611.34808)
*Martin Bauer, Sreemanti Chakraborti* · `hep-ph` · arXiv:2611.34808v1 · relevance 0.29

- **In one sentence**: The paper estimates how well current and future collider measurements of Z and Higgs boson widths, and CP-odd observables such as tau dipole moments in Z decays, could detect oscillating signals from ultralight dark matter at the electroweak scale.
- **In plain words**: The paper asks whether particle colliders could spot a very light, invisible form of dark matter that makes certain properties of particles wobble over time. The authors look at how precisely the widths of the Z and Higgs bosons, and certain lopsided decay effects in Z particles decaying to tau pairs, can be measured. They report that the tau-based measurements could be more sensitive than atomic clocks or tests of the equivalence principle, which are the usual ways of searching for this kind of dark matter.
- **Why it matters**: If dark matter is an ultralight field, it could leave time-varying traces in particle physics measurements, so a new search channel would be useful. The text only supports a claim of better sensitivity than atomic clocks and equivalence tests under the paper's assumptions; it does not say whether any signal has been seen.
- **Background needed**: - Dark matter: unseen matter that holds galaxies together; its nature is unknown.
- Ultralight dark matter: a hypothesized field with an extremely small particle mass, behaving like a wave that oscillates over time.
- Misalignment mechanism: a way such a field could have been produced in the early universe with the right overall density, leaving it oscillating now.
- Electroweak scale: the energy range (around the mass of the W, Z and Higgs bosons) where the weak force and the Higgs field operate.
- Z and Higgs bosons: heavy, short-lived particles; their "width" describes how quickly they decay and how spread out their measured mass is.
- CP-odd observables: measurements sensitive to asymmetry between matter and antimatter behavior, such as electric or magnetic dipole moments.
- Dipole moment: a measure of how a particle's charge or magnetism is lopsided along an axis.
- Atomic clocks and equivalence principle tests: precision experiments that currently constrain such fields. · level: research-level

<details><summary>Original abstract</summary>

Ultralight dark matter provides an explanation for astrophysical evidence for dark matter at all scales. This non-thermal dark matter requires a misalignment mechanism to reproduce the observed matter energy density of the Universe and therefore induce oscillating, time-dependent signals. We determine the sensitivity of current and future collider measurements of the width of the Z and Higgs bosons, and show that CP odd observables such as dipole moments in $Z\to \tau^+\tau^-$ decays provide a better sensitivity to ultralight dark matter than atomic clocks or equivalence principle tests.

</details>

### [Ultralight Dark Matter Spectrum with Gravitational Focusing and Doppler Motion](https://arxiv.org/abs/2611.34464)
*Shao-Feng Ge, Yong Tang, Yue-Hui Yao* · `hep-ph` · arXiv:2611.34464v1 · relevance 0.22

- **In one sentence**: This paper studies how the Sun's gravitational focusing and the Earth-based detector's Doppler motion reshape the expected energy spectrum of ultralight dark matter signals, and how ignoring these effects can bias inferred dark matter parameters.
- **In plain words**: Some proposed dark matter particles are extremely light and could be detected as faint, repeating signals in sensitive instruments. This paper asks how two local effects change the shape of the expected signal: the Sun's gravity pulling dark matter toward it, and the motion of the detector as the Earth moves. The authors estimate the signal strength analytically and run Bayesian statistical tests on simulated data to show that these effects matter for parameter estimates.
- **Why it matters**: If these local effects are left out of the signal models, a detection could lead to wrong estimates of the dark matter's properties, so the modeling matters for interpreting any future signal. The text does not say whether any experiment has observed such a signal, so the practical payoff depends on future detections.
- **Background needed**: - Dark matter: invisible matter that makes up most of the mass of galaxies; its particle nature is unknown.
- Ultralight dark matter: hypothetical particles far lighter than an electron, behaving more like waves than particles.
- Signal spectrum: how the strength of a detected signal varies with energy or frequency.
- Phase-space distribution: a description of how dark matter particles are spread across positions and velocities.
- Gravitational focusing: the Sun's gravity bends the paths of passing dark matter, concentrating it in some directions.
- Doppler effect: the shift in observed frequency caused by a source or detector moving relative to the signal.
- Bayesian analysis: a statistical method that updates estimates of unknown parameters using data and prior assumptions. · level: research-level

<details><summary>Original abstract</summary>

Ultralight dark matter can produce signals in experiments through its couplings with the Standard Model particles. The resulting signal spectrum is determined by the phase-space distribution of dark matter, which encodes information about its production mechanism and the history of the local universe. However, the local environmental effects can modify the observed spectrum and should be included in signal modeling to avoid biased parameter estimates. In this work, we investigate how the gravitational focusing by Sun and the Doppler effect due to the detector's motion modify the signal spectrum and affect inferring the underlying dark matter parameters. We analytically estimate the signal significance and perform Bayesian analysis on simulated data to demonstrate their impact.

</details>

## Nuclear physics

### [Nuclear Modification of $\pi^0$ Production in pO and OO Collisions with ALICE](https://arxiv.org/abs/2611.34503)
*Nicolas Strangmann* · `nucl-ex` · arXiv:2611.34503v1 · relevance 0.12

- **In one sentence**: A conference contribution reporting ALICE measurements of neutral pion (π⁰) nuclear modification factors in oxygen–oxygen (OO) and proton–oxygen (pO) collisions, used to separate cold-nuclear-matter effects from hot-medium energy loss.
- **In plain words**: Physicists smash heavy atomic nuclei together at the LHC to briefly recreate a very hot, dense state of matter called the quark-gluon plasma. This work looks at lighter collisions, oxygen on oxygen and proton on oxygen, and counts how many high-energy particles (neutral pions) come out compared with simple proton-proton collisions. The aim is to tell apart effects from the cold nuclei themselves from effects of the hot matter, and to measure how much energy the fast particles lose in oxygen collisions.
- **Why it matters**: Energy loss in hot matter was clearly seen in lead–lead collisions but not yet in smaller systems, so testing it in oxygen collisions checks how small a system can still show these effects. The text describes the goal and compares to theory, but it does not report final numbers here, so the result's strength cannot be judged from this text alone.
- **Background needed**: - Quark-gluon plasma: a state of matter with free quarks and gluons, thought to have existed in the early universe, made in very energetic nuclear collisions.
- Nuclear modification factor (R_AA, R_pO): a ratio comparing particle yields in nucleus collisions to those in simpler reference collisions; values below 1 mean fewer particles than expected (suppression).
- Energy loss: fast quarks and gluons lose energy by passing through the hot medium, producing fewer high-momentum particles.
- Cold nuclear matter effects: changes caused by the nuclei themselves even without a hot plasma.
- Neutral pion (π⁰): a short-lived particle that decays into two photons, measured here with ALICE's electromagnetic calorimeter.
- This is a conference-style contribution; the text gives the aims and methods but not the final results. · level: research-level

<details><summary>Original abstract</summary>

Energy loss of high-momentum partons is one of the key signatures of the quark--gluon plasma formed in heavy-ion collisions. Through measurements of the nuclear modification factor, $R_{\rm AA}$, where a strong suppression of high-$p_{\rm T}$ particle yields is observed, parton energy loss has been confirmed in Pb--Pb collisions at the LHC. However, in small collision systems, like pp and p--Pb, energy loss has not yet been confirmed. In this contribution, a measurement of the $\pi^0$ $R_{\rm AA}$ in OO and pO collisions at $\sqrt{s_{\rm NN}} = 5.36$ TeV and $\sqrt{s_{\rm NN}} = 9.62$ TeV, respectively, is presented. These results are based on the measured $\pi^0$ $p_{\rm T}$ spectra in OO, pO, and pp collisions using the ALICE electromagnetic calorimeter. The measurement of the $R_{\rm pO}$ allows for precise constraints on cold-nuclear matter effects. In combination with the $R_{\rm OO}$, this allows for a separation of cold and hot nuclear matter contributions and enables a quantitative determination of partonic energy loss in OO collisions. The measurements are compared to theoretical model calculations that include both cold and hot nuclear matter effects.

</details>

### [Large-scale fission properties with BSkG3 I : fission paths and spontaneous fission half-lives](https://arxiv.org/abs/2611.34413)
*Adri\'an S\'anchez-Fern\'andez, Wouter Ryssens, St\'ephane Goriely* · `nucl-th` · arXiv:2611.34413v1 · relevance 0.11

- **In one sentence**: A large-scale microscopic survey of about 3300 nuclei (80 ≤ Z ≤ 118) using the BSkG3 energy density functional, computing triaxial and octupole potential energy surfaces, least-action fission paths, and WKB spontaneous fission half-lives, with results released to TALYS and BRUSLIB.
- **In plain words**: This paper looks at how heavy atomic nuclei split apart on their own, a process called spontaneous fission. The authors computed the energy landscape that a nucleus must cross to split for nearly 3300 nuclei, from the heaviest known elements out toward the edges of nuclear stability. They found many more route shapes than the simple two-hump picture usually assumed, and they estimated how long each nucleus would take to fission.
- **Why it matters**: Fission rates for very heavy and unstable nuclei are needed for modelling nuclear reactions and the rapid neutron-capture process that may form heavy elements in stars. The paper says its dataset has been added to the TALYS reaction code and the BRUSLIB repository, so it may feed into those applications, though the text does not show how much it changes those models.
- **Background needed**: - Atomic nucleus: the dense core of an atom, made of protons (Z) and neutrons.
- Spontaneous fission: a heavy nucleus splitting into fragments without being hit by anything.
- Potential energy surface: a map of a nucleus's energy as its shape changes; fission proceeds over hills and valleys on this map.
- Deformation: how far a nucleus departs from a sphere; triaxial (squashed unevenly in three directions) and octupole (pear-shaped) deformations are the shape variations included.
- Fission barrier: the energy hump a nucleus must cross to split; the "two-humped" picture refers to two such humps in sequence.
- Energy density functional (BSkG3): a theoretical model that computes nuclear energies and shapes from a single set of rules fitted to data.
- WKB approximation: a standard semiclassical method for estimating the tunnelling probability through a barrier, and hence the half-life.
- Drip lines: the limits of how many neutrons or protons a nucleus can hold before it falls apart.
- r-process: rapid neutron capture, a stellar process that builds many heavy elements. · level: research-level

<details><summary>Original abstract</summary>

We present our first large-scale analysis of nuclear fission properties based on the BSkG3 energy density functional. Building on the model's unprecedented agreement with ground state observables and fission data in the actinide region, we survey nearly 3300 nuclei with $80\leq Z\leq118$, spanning the region between the predicted proton and neutron drip lines. We calculate thousands of potential energy surfaces that explicitly account for triaxial and octupole deformations. We determine the corresponding least-action fission paths using microscopic collective inertias derived consistently from BSkG3 and calculate spontaneous fission (SF) half-lives within the semiclassical WKB approximation. Our results reveal a rich diversity of fission path topologies, extending well beyond the conventional two-humped picture commonly adopted in reaction codes, and a wide variety of nuclear shapes along these paths, highlighting the limitations of exploring only one collective degree of freedom. In particular, triaxiality affects not only inner barriers in the actinide region but also outer barriers and single barriers in several regions of the superheavy nuclei. Our predicted SF half-lives follow trends similar to those of previous large-scale studies, although significant differences emerge near the neutron drip line. The resulting dataset, including fission barriers, SF half-lives, and saddle-point nuclear level densities, is available has been incorporated into the TALYS reaction code and the BRUSLIB repository. It provides a microscopic foundation for nuclear reaction calculations and astrophysical applications, particularly rapid neutron-capture simulations, which require reliable fission properties of nuclei far from the valley of stability.

</details>

## Quantum information and computing

### [QPAT: A Universal Quantum Machine Learning Framework for Quantum-Assisted Training and Classical Inference](https://arxiv.org/abs/2611.33806)
*Yixiong Chen* · `quant-ph` · arXiv:2611.33806v1 · relevance 0.17

- **In one sentence**: QPAT uses a quantum circuit Born machine as a learned generative prior that guides classical neural network training (LSTMs, CNNs, Transformers), so inference can run fully classically after training.
- **In plain words**: The paper proposes a way to borrow ideas from quantum computers to help ordinary AI models learn, without needing a quantum computer when the model is actually used. A small quantum-based probability model acts as a guide during training, and the classical network absorbs its structure. The authors report better accuracy and steadier results across random seeds on six tasks covering forecasting, images, and text.
- **Why it matters**: It targets a real obstacle to practical quantum machine learning: slow, noisy quantum hardware at inference time. Whether the gains hold up beyond the authors' own benchmarks and controls is not established by the text alone, so the claims should be read as preliminary.
- **Background needed**: - Classical neural networks (LSTMs, CNNs, Transformers) are standard AI models for sequences, images and language.
- Generative model: a model that learns a probability distribution over data and can produce samples from it.
- Quantum circuit Born machine (QCBM): a quantum circuit whose measurement outcomes define a probability distribution that can be trained.
- NISQ era: the current period of noisy, small-scale quantum hardware.
- Barren plateaus: regions where training gradients become so flat that quantum models stop learning.
- Overfitting: when a model memorises training data and fails on new data.
- Ablation study: a test that removes or replaces a component to see whether it is responsible for the gains. · level: research-level

<details><summary>Original abstract</summary>

Deep learning models often struggle with sharp local optima and overfitting in limited-data regimes, and exhibit limited capacity for capturing high-order, complex probability distributions. Quantum Machine Learning (QML) models, by operating in exponentially large Hilbert spaces, can efficiently represent such distributions and provide favorable inductive biases for learning, offering a promising pathway to overcome these limitations. However, their practical deployment in the Noisy Intermediate-Scale Quantum (NISQ) era is severely hindered by gradient coupling, barren plateaus, data-loading bottlenecks, and high inference latency. To bridge classical AI and QML, we propose QPAT (QCBM-Prior-Assisted Training), a universal framework that employs a Quantum Circuit Born Machine (QCBM) as a learnable generative prior to provide a task-aligned structured inductive bias during classical model training. The framework can be seamlessly integrated into any classical backbone, including LSTMs, CNNs, and Transformers. We introduce a decoupled fitness-based scoring mechanism and a stochastic "Drop-Prior" mechanism to implicitly distill quantum structural knowledge into the classical weights during training. Evaluated extensively on six benchmarks spanning time-series forecasting, computer vision, and natural language processing, our framework consistently outperforms purely classical backbones in both predictive performance and stability across random seeds; ablation studies further show that these gains are not reproduced by unstructured random priors or a classically learned generative prior. Remarkably, our approach enables completely classical inference, bypassing quantum latency while preserving quantum-enhanced accuracy, paving a highly practical path for QML deployment.

</details>

### [Bound Entanglement with Negative Partial Transpose Exists](https://arxiv.org/abs/2611.34921)
*Islam Faisal* · `quant-ph` · arXiv:2611.34921v1 · relevance 0.14

- **In one sentence**: The paper claims an explicit two-qubit-by-two-qubit (C^8 ⊗ C^8) Werner state that has negative partial transpose yet is bound entangled, showing distillable entanglement is neither additive nor convex.
- **In plain words**: Entanglement is a special quantum link between separated parts of a system, and some entangled states cannot be turned back into useful pure entanglement by any local operations and classical communication. This paper gives a specific mixed state of two 8-level systems that appears to have this "bound" property while also showing a detectable quirk (negative partial transpose), which was an open question in the field. The authors report that no such protocol can extract entanglement from many copies of the state, and that even a broader class of operations cannot produce a two-qubit output with a Bell-state fidelity above about 0.604.
- **Why it matters**: The existence of bound entangled states with negative partial transpose had been a long-standing open problem in quantum information theory, so a concrete example would settle a question about which entanglement tests can and cannot detect useful entanglement. The text itself does not discuss applications beyond the stated consequences for distillable entanglement being non-additive and non-convex.
- **Background needed**: - Entanglement: correlations between separated quantum systems that have no classical explanation.
- Mixed state: a quantum state described probabilistically, as a blend of possibilities.
- Werner state: a family of symmetric mixed states built from the identity and the swap operator.
- Partial transpose: a mathematical operation on a state; a negative result is a standard test that certifies entanglement.
- Bound entanglement: entanglement that cannot be concentrated into standard Bell pairs by local operations and classical communication (LOCC).
- Distillation: turning many weakly entangled copies into fewer strongly entangled ones.
- Separable operations: a larger class of operations than LOCC, which cannot create entanglement.
- Bell state and fidelity: a standard maximally entangled two-qubit state, and a measure of closeness to it (1 is perfect).
- Additive and convex: mathematical properties of the distillable entanglement measure; the text says they fail. · level: research-level

<details><summary>Original abstract</summary>

We show that the Werner state $\rho = (23 I - 3\,\mathrm{SWAP})/1448$ on $\mathbb{C}^8 \otimes \mathbb{C}^8$ has a negative partial transpose and is bound entangled: no LOCC protocol can distill entanglement from any number of copies of $\rho$, and even with separable operations the fidelity of a two-qubit output with a Bell state never exceeds $(1+\sqrt{2})/4 \approx 0.604$. It follows that distillable entanglement is neither additive nor convex.

</details>

## Optics and atomic physics

### [Site-Resolved Optical Spectroscopy of Thulium in Solid Argon](https://arxiv.org/abs/2611.34518)
*Jason Marfey, Heming Gao, Colin V. Parker* · `physics.atom-ph` · arXiv:2611.34518v1 · relevance 0.09

- **In one sentence**: Excitation-emission spectroscopy of thulium atoms frozen in solid argon resolves six trapping-site profiles, shows matrix-induced shifts for s→p but not f→d transitions, and identifies a three-photon pathway for a strong 560 nm emission from one site.
- **In plain words**: Researchers placed single thulium atoms inside a block of solid argon, which holds them in fixed positions, and shone light on them while measuring what they gave back. The light patterns split into six groups, which the authors link to different spots where an atom can sit in the argon. They also report that one spot gives off strong green-yellow light at 560 nm, and that this light may come from an atom absorbing three photons in sequence.
- **Why it matters**: The text shows that the surrounding solid can shift some atomic energy levels a lot while leaving others nearly unchanged, which matters for anyone trying to use atoms embedded in solids as sensors or quantum devices. The link to such applications is not addressed in the text, so the wider significance is uncertain.
- **Background needed**: - Atoms have discrete energy levels; light is absorbed or emitted when an atom jumps between them.
- Thulium is a rare-earth element; its outer electron configuration determines which jumps are possible.
- Matrix-isolated atoms are atoms trapped in a solid inert gas (here argon) at very low temperature, so they do not react with neighbours.
- Trapping sites are the different positions or local arrangements an atom can occupy in the solid; each shifts its energy levels slightly.
- Excitation-emission spectroscopy shines light at one wavelength and records the light re-emitted at others, mapping how the atom absorbs and releases energy.
- Multiphoton excitation means an atom absorbs several low-energy photons in sequence to reach a higher level.
- Crystal-field splitting is the separation of energy levels caused by the electric fields of neighbouring atoms in a solid. · level: research-level

<details><summary>Original abstract</summary>

We utilize the high resolution of the ground state transition ${}^2\mathrm{F}_{7/2} \leftrightarrow {}^2\mathrm{F}_{5/2}$ in thulium atoms isolated in solid argon to perform excitation-emission spectroscopy. Decomposition of the excitation-emission spectrum reveals 6 absorption-emission profiles, which are attributed to multiple trapping sites in the host matrix. Comparison with vacuum transition energies shows large matrix-induced shifts for $\mathrm{s}\rightarrow\mathrm{p}$ transitions, whereas $\mathrm{f} \rightarrow \mathrm{d}$ transitions remain close to their free-atom energies. A single site exhibiting strong emission at 560nm is investigated and a three-photon excitation pathway is determined as a possible origin of the high energy 560nm light. Additionally, for long-lived levels belonging to the $\mathrm{f}^{12}\mathrm{d}$ configuration, narrow, crystal-field split absorption lines are identified. Matrix effects are important for establishing the mechanism behind the observed spectra and long $\mathrm{f}^{12}\mathrm{d}$ lifetimes.

</details>

### [Fourier-Transform Photothermal Spectroscopy with Transient-Lens Detection](https://arxiv.org/abs/2611.34361)
*Asha S. Thomas, Toluwatomi Haastrup, Luzhou Yu et al.* · `physics.optics` · arXiv:2611.34361v1 · relevance 0.09

- **In one sentence**: The paper demonstrates Fourier-transform photothermal spectroscopy, using a phase-stable broadband supercontinuum pump pulse pair and an off-resonant 800 nm thermal-lens probe, to reconstruct the linear absorption spectrum of phloxine B and compares it with a conventional frequency-domain absorption measurement.
- **In plain words**: Researchers want to know how strongly a material absorbs light at each color. Normally they measure how much light gets through the sample. Here, a short burst of broadband light is sent into a sample as two pulses with a controlled time gap; the light heats the sample slightly, creating a temporary lens, and a separate laser beam reads out that lens. Mathematically transforming the readout over the time gaps recovers the absorption spectrum, which the authors check against a standard measurement on the dye phloxine B.
- **Why it matters**: The text presents this as a proof-of-concept that absorption spectra can be inferred from refractive-index changes caused by heating rather than from transmitted light intensity, which may matter for samples where transmitted light is hard to measure accurately. The text does not establish how broadly the method would apply or how it compares in sensitivity or speed with existing techniques, so its wider significance is uncertain.
- **Background needed**: - Absorption spectrum: how much light a sample absorbs at each wavelength (color).
- Supercontinuum: very broadband light, produced here by sending ultrashort laser pulses through a special optical fiber.
- Phase-stable pulse pair: two light pulses whose timing and wave alignment are controlled, so their interference is reproducible.
- Fourier transform: a mathematical step that converts a signal recorded over time into its frequency content, here turning the time-delay signal into a spectrum.
- Photothermal effect: light absorbed by a sample turns into heat, which changes the local refractive index (how light bends).
- Thermal lens: a temporary lens-like effect created by this heating, read out by a probe laser beam.
- Phloxine B: a fluorescent dye used here as a test sample. · level: research-level

<details><summary>Original abstract</summary>

We demonstrate Fourier-transform photothermal spectroscopy using broadband supercontinuum excitation and transient-lens detection. The output of a Ti:sapphire oscillator is broadened in a photonic crystal fiber to generate the supercontinuum pump, which is converted into a phase-stable pulse pair with a controllable femtosecond delay using a birefringent interferometer. The absorption-induced heating from the pump generates a transient thermal lens in the sample, which is detected as a function of delay by an off-resonant 800 nm photothermal probe beam. Fourier transform of the interferometric photothermal response yields a frequency-domain signal corresponding to the sample absorptance spectrum weighted by the pump spectrum. After division by the measured pump spectrum, the reconstructed photothermal spectrum is compared with a direct frequency-domain linear absorption measurement to evaluate the accuracy of the reconstruction. This method combines Fourier-transform broadband excitation with thermal-lens readout, allowing broadband linear absorption spectra to be obtained from pump-induced refractive-index changes rather than from transmitted excitation intensity. We demonstrate the method on phloxine B.

</details>

## Fluids and plasma

### [Point vortex dynamics influenced by the surface motion](https://arxiv.org/abs/2611.33412)
*Delia Ionescu-Kruse, Rossen I. Ivanov, Michail D. Todorov* · `nlin.PS` · arXiv:2611.33412v1 · relevance 0.09

- **In one sentence**: A mathematical study of a coupled system in which a free fluid surface (with long, small-amplitude waves in the Boussinesq regime) interacts with a point vortex inside the fluid, showing that surface solitary waves survive the interaction and that the vortex motion can be reduced to decoupled ODEs.
- **In plain words**: This paper looks at what happens when a swirling point of fluid rotation sits beneath a water surface that carries waves. The authors model the surface and the vortex together, using equations that apply to long, gentle waves. They report that solitary waves (single rolling humps that travel without spreading) keep their shape for a wide range of vortex strengths, and that a simpler version of the model can describe the vortex's motion on its own.
- **Why it matters**: It gives a mathematically tractable picture of how a surface wave and an underlying vortex affect each other, which may matter for understanding nearshore flows or wave-vortex interactions. The text does not say how far these results carry over to real water, so the practical reach is uncertain.
- **Background needed**: - Free surface: the upper boundary of a fluid, such as the top of a pond or sea.
- Point vortex: an idealized, infinitely small whirlpool-like swirl of fluid, treated as a single point.
- Solitary wave (soliton): a single wave hump that keeps its shape and speed as it travels.
- Boussinesq regime: an approximation for long, shallow, low-amplitude waves, where simpler equations replace the full fluid equations.
- Ordinary differential equations (ODEs): equations describing how a few quantities change over time, here used for the vortex's position.
- Vortex strength: a number measuring how strongly the fluid circulates around the vortex. · level: research-level

<details><summary>Original abstract</summary>

We study a coupled system of differential equations, which models the dynamics of fluid with a free surface and a point vortex in the body of the fluid. For long surface waves of small amplitude, the effects of the interaction between the waves and the point vortex are modeled within the framework of the Boussinesq regime. It turns out that the solitary waves on the surface are not destroyed by the interaction with the vortex, and, as a matter of fact, the solitary waves remain practically unaffected for a significant range of the vortex strength. As a result, a further simplification of the model is proposed, where the vortex motion under solitons propagating on the surface is determined from a system of decoupled ordinary differential equations.

</details>

### [A 2D fluid model in BOUT++/Hermes-3 for simulating detached divertor plasmas in tokamaks](https://arxiv.org/abs/2611.34717)
*Malamas Tsagkaridis, Ben Dudson, Mike Kryjak et al.* · `physics.plasm-ph` · arXiv:2611.34717v1 · relevance 0.08

- **In one sentence**: A two-dimensional fluid model in BOUT++/Hermes-3 is used to simulate detached divertor plasmas in a DIII-D tokamak discharge, with an improved PETSc SNES steady-state solver and comparison of sparse preconditioners (STRUMPACK ILU preferred, about 5x faster than HYPRE-based setups in the cases studied).
- **In plain words**: Fusion reactors need a way to keep the exhaust plasma from damaging the metal surfaces that absorb it, and one strategy is "detachment," where the hot plasma is cooled near those surfaces before it arrives. This paper describes a computer model of that cooling process for a real experiment at the DIII-D fusion device, and it also reports how to make the model's calculations run faster. The authors adjust the model to match measured upstream conditions, add nitrogen gas to cool the plasma, and track where energy and particles are gained and lost. They also show that, as the plasma density at the edge is raised, the temperature at the target drops and the measured ion current eventually levels off, as expected for detachment.
- **Why it matters**: Reliable simulations of detachment matter for designing future high-power tokamaks, where controlling heat loads on divertor surfaces is a central engineering problem. The solver speedup is a practical result for anyone running these large simulations, though the text reports it only for the cases considered, so its general reach is not yet shown.
- **Background needed**: - Tokamak: a doughnut-shaped magnetic device that confines hot plasma for fusion research.
- Divertor: the region at the bottom of the tokamak where exhaust plasma hits target plates.
- Detachment: a state where the plasma is cooled and pulled away from the target plates, lowering heat loads.
- Fluid model: treats plasma as a continuous fluid with density, temperature and velocity, rather than tracking individual particles.
- Fixed-fraction impurity radiation: a simplified way of modeling cooling by adding a set share of an impurity gas (here nitrogen) that radiates energy.
- Steady-state solver and preconditioner: numerical methods that find an unchanging solution of large equation systems faster; the preconditioner helps the linear algebra converge.
- Separatrix density: the plasma density at the boundary between confined and exhaust plasma, used as an input control.
- Ion saturation current: a measured electrical current at the target that indicates how much plasma arrives there. · level: research-level

<details><summary>Original abstract</summary>

Detached divertor operation is essential for controlling target heat fluxes in future high-power tokamaks. We present a two-dimensional fluid model implemented in BOUT++/Hermes-3 for simulating detached divertor plasmas with plasma-neutral interactions and fixed-fraction impurity radiation. We report improvements to the PETSc SNES-based steady-state solver used for two-dimensional axisymmetric transport simulations with fluid neutrals and assess the performance of several sparse-solver preconditioning strategies. For the cases considered here, STRUMPACK used as an ILU preconditioner with low-rank compression provides the most favorable performance, reducing the linear-to-nonlinear iteration ratio and achieving approximately a fivefold speedup relative to \HYPRE{}-based configurations. The optimized solver is then applied to DIII-D shot $\#174287$ at 4000~ms to characterize detached divertor conditions. Cross-field transport coefficients are adjusted to reproduce upstream experimental profiles, and detachment is modeled using nitrogen fixed-fraction radiation. Steady-state particle and energy balances are evaluated by decomposing the density and pressure equations into their transport and source terms. In the outer divertor, electron energy losses are dominated by ionization and impurity radiation, while ion energy losses occur mainly through collisional transfer to electrons. An upstream separatrix density scan shows decreasing target electron temperature and a rollover of the integrated target ion saturation current at higher $n_{e,\mathrm{sep}}$ consistent with expected detachment trends. These developments establish a foundation for future multispecies simulations. Hermes-3 is publicly available on GitHub under the GPL-3 open-source license.

</details>

## Biological physics

### [Stochastic Failure Dynamics in a Model Peptidoglycan Mesh under Hydrolysis and Mechanical Loading](https://arxiv.org/abs/2611.34610)
*Issan Patri, Garima Rani* · `physics.bio-ph` · arXiv:2611.34610v1 · relevance 0.05

- **In one sentence**: A minimal stochastic-mechanical model, analysed with extreme value theory and simulations, of how a Gram-negative peptidoglycan cell wall fails over time when hydrolases keep cutting bonds, growth is blocked, and mechanical load may be applied.
- **In plain words**: Bacteria are protected by a mesh-like wall made of cross-linked sugar-and-peptide chains. This paper asks how that wall eventually breaks down if growth is stopped, for example by an antibacterial agent, while enzymes keep snipping its bonds. The authors use a simplified random model, with mathematical limit laws and computer simulations, to describe when and where the wall gives way.
- **Why it matters**: The text reports that failure time grows only logarithmically with the number of bonds, so extra cross-linking gives diminishing returns, and that collapse stays localized even when overall cross-linking is high. These are model results, not experimental findings, so their relevance to real bacteria is untested from this text alone; they may be of interest to people studying antibiotic action or bacterial cell-wall mechanics.
- **Background needed**: - Peptidoglycan (PG): a mesh of sugar chains linked by short peptides that forms the bacterial cell wall.
- Cross-links: bonds that tie the mesh together; more cross-links mean a stronger wall.
- Hydrolases: enzymes that break (cut) bonds in the wall.
- Gram-negative: a bacterial group with a thin wall and an outer membrane.
- Extreme value theory: statistics of the largest or smallest values, here the weakest point giving way first.
- Gumbel and Weibull laws: standard probability distributions for minimum or weakest-link failure times.
- Stochastic simulation: computer runs with random events to mimic chance-driven behaviour.
- Logarithmic growth: the quantity rises very slowly, roughly in proportion to the log of the input. · level: research-level

<details><summary>Original abstract</summary>

We develop a minimal stochastic-mechanical model for failure dynamics of the Gram-negative peptidoglycan (PG) cell wall under blocked growth and continued hydrolysis. The cell wall is modelled as a collection of load-bearing cross-sections, with random number of cross-links in each such cross-section, around a fixed degree of cross-linking. To understand failure dynamics of the cell wall under antibacterial agents which prevent insertion of fresh PG material, peptide bonds are progressively excised by hydrolases, while insertion/formation of new bonds is blocked. We compare and contrast rupture dynamics in no-load and load-activated regimes, using extreme value theory and stochastic simulations, deriving limiting laws for system failure in both the long-cell and large crosslinking limits. For a cross-section with many bonds, the mean failure time grows only log- arithmically with bond number, giving diminishing returns from additional cross-linking. In the no-load case, the centered failure time converges to a Gumbel law, though crucially, load changes the centered distribution and accelerates the final stages of collapse. In long cells, failure follows a weakest-link Weibull-type scaling controlled by the least cross-linked regions, with mechanical load reducing the failure-time scale without changing the weakest-link exponent. The fraction of bonds removed before failure tends to zero, showing that collapse can remain highly localized even while the global cross-linking degree stays high. Slowing down growth and other cellular functions is a typical antibiotic escape mechanism for bacteria and in this context, we show that, hydrolase down-regulation uniformly rescales the failure-time distribution and delays collapse, but does not remove the load-induced preference for rupture in weakened regions.

</details>

### [Quantum chaotic signature in non-empirical ensemble of DNA base pairs](https://arxiv.org/abs/2611.34305)
*Mehdi Ameri* · `q-bio.BM` · arXiv:2611.34305v1 · relevance 0.03

- **In one sentence**: The paper tests whether the orbital energy levels of isolated guanine-cytosine and adenine-thymine Watson-Crick base pairs, computed with density functional theory, follow random-matrix level statistics, and finds they most closely match the semi-Poisson distribution.
- **In plain words**: Researchers looked at the energy levels of single DNA base pairs (the GC and AT pairs that hold the two strands of DNA together), calculated with a standard computer quantum-chemistry method. They asked whether the spacing pattern of these levels looks like the patterns seen in chaotic quantum systems or in simple, unrelated levels. The energy spacings fit best a middle-ground pattern called semi-Poisson, lying between fully ordered and fully chaotic behavior.
- **Why it matters**: It applies random-matrix statistics, a tool from nuclear and quantum chaos, to a small biological molecule, which is an unusual pairing. The authors suggest possible links to charge transfer in biology, but the text does not show such a link, so that connection remains speculative.
- **Background needed**: - Watson-Crick base pairs: the GC and AT pairings that form the rungs of the DNA double helix.
- Density functional theory (DFT): a common computer method for estimating the electron energy levels of molecules.
- Kohn-Sham orbital energies: the single-electron energy levels that DFT produces, used here as the data.
- Random-matrix theory: a statistical framework describing energy-level spacings in complex quantum systems. Poisson spacings mean unrelated levels; GOE (Gaussian Orthogonal Ensemble) spacings mean chaotic systems with level repulsion; semi-Poisson is an intermediate pattern.
- Level repulsion: nearby energy levels tend to avoid each other in chaotic systems.
- Adjacent-gap ratio, number variance, and spectral compressibility: statistical measures used to compare level patterns with each model. · level: research-level

<details><summary>Original abstract</summary>

The statistical study of many-body chaotic quantum systems would indicate important phenomena such as short-range level repulsion and long-range spectral rigidity. We investigate such behavior in an ensemble of gas-phase guanine-cytosine (GC) and adenine-thymine (AT) Watson-Crick (WC) base pairs by calculating their Kohn-Sham molecular orbital energy levels via ab initio density functional theory (DFT). We track the probability distribution, adjacent-gap ratios (AGR), number variance, and spectral compressibility of the unfolded level spacings to see whether their statistics follow the statistics of the eigenvalues of random matrices. After comparing the results to Poisson, semi-Poisson (SP), and Gaussian Orthogonal Ensemble (GOE) statistics, it becomes evident that the statistics of orbital energy levels agree closely with the semi-Poisson distribution, pointing to an intermediate regime between integrability and chaos, characterized by level repulsion and strong long-range correlations. Potential biophysical implications for charge transfer and related biological processes are also discussed.

</details>

## Climate, atmosphere and Earth

### [Basin-Scale Nonlinear Dynamics of Thermohaline Ocean Circulation. Part I: Theory](https://arxiv.org/abs/2611.33383)
*Conner W. Lester, Dylan E. McNamara, Till J. W. Wagner* · `physics.geo-ph` · arXiv:2611.33383v1 · relevance 0.16

- **In one sentence**: A tracer-conservation framework that expresses thermohaline (density-driven) ocean circulation bifurcations as a balance between surface fluxes and basin-scale advective and dissipative transport, tested in a three-dimensional ocean-basin model, with Part II reserved for tipping-point forecasting closures.
- **In plain words**: The paper looks at the large-scale ocean circulation that moves heat and salt around the planet, which may have more than one stable state and can flip abruptly between them. The authors describe the circulation as a balance between what enters the ocean at its surface and how that heat and salt are carried or spread out by the flow. In a three-dimensional model of an ocean basin, they find that salt carried by the flow itself mainly controls when the circulation collapses, while simple spreading mixing mainly controls when it recovers.
- **Why it matters**: Abrupt shifts in ocean overturning are a major concern in climate science, so a framework that explains them through transport processes, rather than overturning strength alone, may help interpret models of the same behavior. The text links this to classic simple "box models," but how far the framework applies beyond the single model studied is not shown in this excerpt.
- **Background needed**: - Thermohaline circulation: ocean flow driven by differences in temperature (thermo) and salinity (haline) that change water density.
- Multiple equilibria: the same forcing can support more than one stable circulation state, so the system can get stuck or jump.
- Bifurcation/tipping point: a threshold beyond which a state changes abruptly.
- Box model: a very simplified model that treats ocean regions as a few well-mixed boxes; used to build intuition.
- Tracer: a substance (here heat or salt) tracked as it is carried and mixed; conservation means its total change equals inputs minus outflows.
- Advection vs. dissipation: transport by bulk flow versus spreading by mixing and diffusion.
- Part I/II: this is the theory half; the forecasting method is in the companion paper. · level: research-level

<details><summary>Original abstract</summary>

Earth's thermohaline ocean circulation may support multiple equilibria and abrupt transitions. Similar bifurcation structures for different ocean models suggest common underlying dynamics across the model hierarchy. Here we propose a unifying framework from tracer conservation, in which surface fluxes are balanced by dissipative and advective tracer transport. We express this flux balance through a large-scale tracer gradient and a transport efficiency that measures how strongly circulation displaces the tracer field from its no-flow "conductive" state. The flux balance quantifies the transport contributions that sustain each circulation state and give rise to abrupt transitions. In a three-dimensional ocean-basin model, we find nonlinear salinity advection dominates the collapse threshold and linear dissipation dominates the recovery threshold. Temperature has additional dissipation from surface restoring, making thermal fluxes more dissipation-dominated than salinity fluxes. The tracer contrasts and boundary layers that a given circulation generates produce distinct transport regimes, approximately quadratic in circulation strength for weak flow and linear for strong flow. With a simple circulation closure, the flux balance reduces to longstanding box-model bifurcation results for the weak and strong flow regimes. Thus, by expressing thermohaline bifurcations through basin-scale transport, this framework connects box-model insight to the continuous equations. Furthermore, as this framework exposes the transport processes that balance a changing forcing, it provides constraints on a thermohaline ocean state and its trend toward tipping that overturning strength alone does not. In Part II, we develop flux-balance closures to forecast such tipping points.

</details>

### [ENSO-linked redistribution of post-monsoon tropical cyclone energy between the Arabian Sea and the Bay of Bengal: 1982--2025](https://arxiv.org/abs/2611.34718)
*Prashant Saini, Rishikesh Yadav, Sarita Azad* · `stat.AP` · arXiv:2611.34718v1 · relevance 0.06

- **In one sentence**: A joint statistical analysis of 416 North Indian Ocean cyclones (1982–2025) finds that El Niño/La Niña redistributes post-monsoon cyclone energy between the Arabian Sea and Bay of Bengal rather than changing the basin total, with the relationship shifting over time and needing about three decades of data to detect certain trends.
- **In plain words**: The paper asks whether the El Niño climate pattern in the Pacific changes how strong tropical storms are in the North Indian Ocean, and where. Using best-track storm records and atmospheric reanalysis data from 1982 to 2025, the authors report that in October to December, El Niño shifts storm energy toward the Arabian Sea and away from the Bay of Bengal, while the combined total stays roughly unchanged. The effect appears to work through changes in wind shear and spin in the lower atmosphere, not through how often storms form.
- **Why it matters**: Storm energy in the two sub-basins affects coastal risk in India, Pakistan, Oman, and Bangladesh, so a redistribution rather than a simple increase or decrease matters for planning. The text reports that the relationship changed between 1982–2003 and 2004–2025, which suggests that short records may give misleading conclusions; the link to future climate change is not addressed in the text.
- **Background needed**: - ENSO (El Niño–Southern Oscillation): a recurring warming and cooling of the central Pacific that shifts weather worldwide; the Niño-3.4 index measures it.
- Tropical cyclone energy (ACE): a measure combining storm strength and duration over its lifetime.
- Arabian Sea (AS) and Bay of Bengal (BoB): the two sub-basins of the North Indian Ocean where cyclones form.
- Post-monsoon season: October–December, the main cyclone season for these basins.
- Vertical wind shear (VWS): change in wind speed or direction with height; high shear tends to weaken storms.
- Low-level vorticity: the spin of air near the surface, which helps storms organize.
- IBTrACS, IMD, JTWC, ERA5, ERSSTv5: storm-track databases and climate datasets used for the analysis.
- Stationarity: whether a relationship stays the same over time.
- IOD (Indian Ocean Dipole): a separate east–west temperature pattern in the Indian Ocean that can overlap with ENSO. · level: research-level

<details><summary>Original abstract</summary>

Tropical cyclones in the North Indian Ocean (NIO) form in two sub-basins, the Arabian Sea (AS) and the Bay of Bengal (BoB), which are usually studied separately, with their relationship to the El Ni\~no-Southern Oscillation (ENSO) treated as stationary. We develop a joint inter-basin statistical framework and apply it to 416 disturbances from quality-controlled IBTrACS best tracks for 1982--2025, with harmonised IMD and JTWC intensities, ERA5 and ERSSTv5. The framework tests whether ENSO changes the basin total or redistributes energy between the sub-basins, separates its effect on formation from that on intensification, attributes each sub-basin's response to environmental terms along individual tracks, and tests stationarity and the record length needed to detect trends. In October-December, ENSO redistributes rather than changes the total: for a one-standard-deviation increase in Ni\~no-3.4 (about 1 $^\circ$C), accumulated cyclone energy (ACE) is multiplied by 1.89 in the AS and by 0.63 in the BoB, while the NIO total shows no detectable change (factor 0.99 [0.74, 1.32]). ENSO acts on intensification, with no detectable effect on formation: the odds that a cyclonic storm becomes very severe rise about fourfold in the AS and halve in the BoB, through lower vertical wind shear (VWS) over the AS and weaker low-level vorticity over the BoB. The relationship has changed: El Ni\~no lowered total NIO energy in 1982--2003, but in 2004-2025 AS gains balanced BoB losses (change p = 0.016). Very severe storms and rapid intensification increased in the AS only, and no 15-year window detects this increase, so about three decades of data are needed. The post-monsoon IOD signal can hardly be separated from ENSO, and August Ni\~no-3.4 gives modest skill for the AS-BoB partition but none for the basin total.

</details>

## Cosmology

### [Black hole accretion flows as dark matter bolometers](https://arxiv.org/abs/2611.34172)
*Ran Ding, Ningqiang Song, Cong Zhang* · `hep-ph` · arXiv:2611.34172v1 · relevance 0.19

- **In one sentence**: The paper proposes using the hot accretion flow around the supermassive black hole M87* as a calorimeter for light dark matter, integrating dark-matter cooling of electrons into the flow's thermodynamics and fitting the predicted radio-to-millimeter spectrum to Event Horizon Telescope-era observations to constrain dark matter-electron scattering for keV-to-MeV masses and both heavy and light mediators.
- **In plain words**: The paper asks whether gas falling onto the giant black hole at the center of galaxy M87 can reveal dark matter. The idea is that very light dark matter particles can carry heat away from the hot electrons in that gas, cooling them and slightly changing the radio and millimeter light the gas gives off. The authors model this cooling, compare the predicted light with observations made alongside the Event Horizon Telescope campaign, and use the mismatch limits to rule out some dark matter interaction strengths.
- **Background needed**: - Dark matter: unseen matter that makes up most of the mass of galaxies; its particle nature is unknown.
- Direct-detection experiments: lab detectors that wait for dark matter particles to bump into atoms.
- Bolometer: a device that measures energy by sensing a temperature rise; here the dark matter acts as a heat sink for electrons.
- Accretion flow: hot gas spiralling inward toward a black hole, emitting light as it heats up.
- Advection-dominated accretion flow (ADAF): a thin, very hot, low-density model of such gas in which the electrons and ions are at different temperatures.
- M87*: the supermassive black hole at the centre of galaxy M87, first imaged by the Event Horizon Telescope.
- Sub-MeV / keV-to-MeV: particle masses of thousandths to millions of electron-volts, far lighter than a proton.
- Mediator: the hypothetical particle that carries the force between dark matter and ordinary matter; "heavy" and "light" mediators give different interaction strengths. · level: research-level

<details><summary>Original abstract</summary>

Astrophysical systems provide powerful probes of dark matter interactions, complementing direct-detection searches. We propose using accretion flows of the supermassive black hole as a bolometer for light DM. The kinetic energy of sub-MeV dark matter in the black hole gravitational potential can remain below the thermal energy of the plasma electrons. The colder dark matter population can therefore absorb energy through elastic scattering, cooling the electrons and modifying their emission spectrum. We integrate dark matter cooling into the advection-dominated accretion flow around M87$^{*}$ and solve the full set of thermodynamic equations to obtain the resulting temperature profile and radio-to-millimeter emission. By comparing the predicted spectrum with observations accompanying the Event Horizon Telescope campaign, we use, for the first time, the thermal energy balance of the hot accretion flow to constrain DM-electron scattering, obtaining stringent limits on keV-to-MeV DM for both heavy and light mediators.

</details>

### [Probing Dynamical Dark Energy with Hyper Suprime-Cam Year 3 Cosmic Shear](https://arxiv.org/abs/2611.34650)
*Shreya Mukherjee, Surhud More* · `astro-ph.CO` · arXiv:2611.34650v1 · relevance 0.17

- **In one sentence**: A real-space cosmic shear analysis of Hyper Suprime-Cam Year 3 data, combined with DESI BAO, recalibrated DES supernovae and BBN priors, constrains constant and time-varying dark energy equations of state and the structure growth parameter S8.
- **In plain words**: Astronomers want to know whether dark energy, the unknown force speeding up the universe's expansion, changes over time. This paper uses the shapes of about 25 million faint galaxies, whose light is slightly bent by matter along the way, together with distance measurements from other sky surveys. The combined result is consistent with a constant dark energy, with a modest 2.4-sigma (roughly 2.4 standard deviations, a weak-to-moderate statistical hint) preference for changing dark energy.
- **Why it matters**: If dark energy evolves, that would change our understanding of fundamental physics, so the result matters for judging the signal. The paper also reports that the weak-lensing measure of how clumpy matter is stays stable across the extended models, while the time-varying signal seems to come mainly from the distance measurements. The text does not establish how robust that hint is beyond this one dataset.
- **Background needed**: - Dark energy: the unexplained component driving the universe's accelerating expansion; its "equation of state" w describes its pressure-to-density ratio, with w = -1 matching a cosmological constant.
- wCDM vs w0waCDM: a constant w versus a version where w changes over cosmic time (w0 today, wa the rate of change).
- Weak gravitational lensing / cosmic shear: measuring tiny distortions in galaxy shapes caused by intervening matter.
- Tomography: splitting galaxies into redshift (distance) bins to track changes over cosmic time.
- BAO (baryon acoustic oscillations): a standard ruler from sound waves in the early universe, used to measure distances.
- Type Ia supernovae: exploding stars with known brightness, used as cosmic distance markers.
- BBN (Big Bang Nucleosynthesis): theory of light-element formation in the early universe, used here as a prior on baryon density.
- S8: a summary number for how clumpy matter is today.
- Sigma: a standard measure of statistical confidence. · level: research-level

<details><summary>Original abstract</summary>

Recent measurements of baryon acoustic oscillations (BAO) and Type Ia Supernovae (SNe) have revealed a preference for a time-evolving dark energy equation of state. Because such dynamical behavior alters both the cosmic expansion history and the late-time growth of structure, weak gravitational lensing measurements can be used to test these extended models. We present an extended analysis of the real-space cosmic shear two-point correlation functions (2PCFs) from the Hyper Suprime-Cam Year 3 (HSC-Y3) survey. Using over 25 million galaxies across 416 deg$^2$, divided into four tomographic redshift bins ($0.3 < z \le 1.5$), we constrain both a constant ($w$CDM) and a time-varying ($w_0w_a$CDM) dark energy equation of state. To break the geometric degeneracies inherent in cosmic shear, we combine the HSC-Y3 data with a CMB-independent suite of background distance probes: DESI DR2 BAO, the recalibrated DES five-year SN sample (DOVEKIE), and Big Bang Nucleosynthesis (BBN) priors. In the $w$CDM paradigm, our joint analysis yields $w =-0.936^{+0.074}_{-0.067}$, consistent with a cosmological constant. Within the $w_0w_a$CDM framework, we find $w_0 =-0.832^{+0.071}_{-0.059}$ and $w_a = -1.23^{+0.66}_{-0.44}$, representing a $2.4\sigma$ preference for dynamical dark energy. Although the unconstrained dark energy parameters reduce the cosmic shear-only $S_8$ constraints to smaller values, our joint multi-probe analysis agrees with the baseline HSC-Y3 $\Lambda$CDM structure growth amplitude. We obtain $S_8 = 0.774^{+0.027}_{-0.034}$ for $w$CDM and $S_8 = 0.772^{+0.031}_{-0.030}$ for $w_0w_a$CDM. Our results demonstrate that the weak lensing amplitude is robust to extended dark energy parameterizations, and that the dynamical dark energy signal is currently driven primarily by the geometric distance ladders, a critical consistency test for next-generation Stage-IV cosmological surveys.

</details>

## Galaxies

### [The tangled warp of the Milky Way II: The red clump](https://arxiv.org/abs/2611.34625)
*James E. Turner, Paul J. McMillan* · `astro-ph.GA` · arXiv:2611.34625v1 · relevance 0.22

- **In one sentence**: Kinematic tracing of the Milky Way disc warp using red clump stars, an old, well-calibrated standard-candle population, finding a precession rate of about 12 km/s/kpc and a kinematic offset from what stellar positions alone predict.
- **In plain words**: The Milky Way's flat disc of stars is bent into a warp, and the shape of that bend depends on how old the stars are. This paper maps how the warp moves, using red clump stars, which are older stars whose true brightness is well known, so their distances can be estimated precisely. The authors report that this older group's warp rotates at a rate similar to that seen in other populations, but its motion does not match what the star positions alone would predict.
- **Why it matters**: The result suggests the warp is changing over time, which the authors argue any model explaining how the warp formed must account for. It adds an older population to a picture that had mostly relied on younger stars such as Cepheid variables. The text does not give details of how strong or broad this evidence is, so its wider significance is best judged after reading the full paper.
- **Background needed**: - The Milky Way's stellar disc is a rotating, flat system of stars and gas; its outer edge bends up and down in a "warp."
- A warp that precesses rotates slowly around the galaxy's centre, like a tilted spinning top.
- Kinematics means how stars move (velocities), as opposed to where they sit (positions).
- Red clump stars are older, helium-burning stars with a consistent intrinsic brightness, making them "standard candles" for distance measurement.
- Cepheid variables are younger, pulsating standard candles; comparing populations of different ages tests how the warp has changed.
- km/s/kpc is a unit of rotation rate: kilometres per second per kiloparsec of distance from the centre. · level: research-level

<details><summary>Original abstract</summary>

The Milky Way's disc is warped in a way that varies depending on the age of the population considered. We, for the first time, trace that kinematics of the warp in red clumps stars. This means that our sample is drawn from a consistent population across the disc, composed of standard candles that allow for precise distance estimates but, unlike samples of Cepheid variables, is relatively old. We find that, consistent with other populations, the red-clump warp is precessing at ${\sim}12\;{\rm km}\,{\rm s}^{-1}\,{\rm kpc}^{-1}$, comparable to the angular velocity of stars around the Galaxy in the outer reaches of the disc. Unlike younger populations, the kinematic signature is offset from that which we would expect given the stellar positions. This reinforces the conclusion that the Milky Way's warp is dynamically evolving, making this a necessary property of any model that seeks to explain its creation.

</details>

### [Less massive black holes in faint hosts: SED fitting of Little Red Dots within the Black Hole Star scenario](https://arxiv.org/abs/2611.33798)
*Haitong Liu, Lulu Fan, Yunkun Han et al.* · `astro-ph.GA` · arXiv:2611.33798v1 · relevance 0.18

- **In one sentence**: SED fitting of 22 JWST "little red dots" at z≈4–9.5 with a composite host-galaxy plus super-Eddington "black hole star" (Cloudy + BayeSED3) model, inferring low-mass hosts and moderately overmassive black holes.
- **In plain words**: Little red dots are small, reddish objects seen by the James Webb Space Telescope in the early universe, and astronomers disagree about what powers them. This paper tests one proposal: a growing black hole wrapped in a dense gas envelope, sitting inside a faint galaxy. The authors fit this combined model to 22 such objects and report that the galaxies are low in mass and the black holes are somewhat heavier than local relations would predict, though less extreme than some earlier estimates.
- **Why it matters**: If the model holds, it would ease a tension in how many of these black holes exist compared with theory, and it links early black hole growth to the galaxies around them. The text does not show how robust these results are to modeling choices, so the conclusions should be treated as provisional.
- **Background needed**: - JWST (James Webb Space Telescope) observes infrared light from very distant, early galaxies; "high redshift" z means light has been stretched by cosmic expansion, so z≈4–9.5 corresponds to roughly the first 1.5 billion years after the Big Bang.
- Spectral energy distribution (SED): the brightness of an object across wavelengths; fitting it lets astronomers infer properties like mass and star formation.
- V-shaped SED: bright in the blue/ultraviolet and optical, with a dip between them, a shape these objects share.
- Balmer break: a drop in light at certain wavelengths caused by hydrogen absorption in stars' atmospheres, often used to estimate stellar age.
- Eddington limit: the maximum brightness at which radiation pressure balances gravity; "super-Eddington" means a black hole is feeding faster than this limit.
- Black hole mass vs. host mass ("overmassive"): local scaling relations link a galaxy's stellar mass to its central black hole's mass; "overmassive" means the black hole is large for its galaxy.
- Photoionization code (Cloudy): software that models how gas is heated and ionized by light.
- Number density tension: the early universe seems to contain more such black holes than standard models predict. · level: research-level

<details><summary>Original abstract</summary>

The James Webb Space Telescope (JWST) has revealed a population of compact sources known as ``little red dots'' (LRDs), characterized by a distinctive V-shaped spectral energy distribution (SED) from UV to optical wavelengths. The physical nature of these sources remains debated. The ``black hole star'' (BH*) scenario, wherein a super-Eddington accreting black hole is embedded in a dense gaseous envelope, has been proposed to explain them. We assemble a sample of 22 LRDs at $4.0 \lesssim z \lesssim 9.5$ from the ASTRODEEP-JWST database. We construct a composite ``host galaxy + BH*'' model using the \texttt{Cloudy} photoionization code, and perform SED fitting with \textsc{BayeSED3}. Our modeling reproduces the observed V-shaped features: the UV continuum blueward of the Balmer break is well reproduced by stellar emission within this decomposition, while the optical regime is dominated by the BH* component. Our fits reveal that LRDs are black holes hosted by faint, low-mass galaxies with median stellar and black hole masses of $M_* = 10^{8.7}\,M_\odot$ and $M_{\rm BH} = 10^{6.4}\,M_\odot$, respectively. These black holes are moderately overmassive relative to local scaling relations but less extreme than broad-line estimates. The median bolometric luminosity $L_{\rm BH^*} \sim 10^{44.9}\,\rm erg\,s^{-1}$ mitigates the reported number density tension from 1--2 orders of magnitude to a factor of a few. The host galaxies lie near the high-redshift star-forming main sequence, and stellar extinction correlates positively with star formation rate (SFR). The BH* scenario provides a self-consistent paradigm for LRDs, offering insights into the rapid growth of supermassive black hole seeds and their co-evolution with host galaxies during the cosmic dawn.

</details>

## Exoplanets and planetary science

### [Discovery of Trailing Spiral Dust Alignment in the Dust Polarization of HL Tau at $\lambda = 2.1$ mm](https://arxiv.org/abs/2611.34613)
*Yi-Wei Jerry Xu, Leslie W. Looney, Ian W. Stephens et al.* · `astro-ph.EP` · arXiv:2611.34613v1 · relevance 0.11

- **In one sentence**: New ALMA Band 4 (2.1 mm) dust polarization of the HL Tau protoplanetary disk reveals a global trailing-spiral deviation from azimuthal grain alignment, which is consistent with aerodynamic alignment near pressure bumps but requires implausibly large Stokes numbers under an axisymmetric velocity field.
- **In plain words**: This paper looks at the young disk of gas and dust around the star HL Tau, using radio telescopes that detect the polarized light given off by tiny dust grains. The authors found that, at one longer wavelength, the grains line up in a slightly twisted pattern that forms spiral arms trailing behind the disk's rotation. The explanation that fits this twist runs into a problem: the grains would have to be far heavier or more drifting than the grains that emit this light are expected to be.
- **Why it matters**: Dust polarization is one of the few ways to map how grains align inside planet-forming disks, so a measured spiral pattern could help test how grains move near pressure bumps where planets may form. The text reports a tension with theory rather than a resolved answer, and the shorter-wavelength data are inconclusive, so its wider significance is still uncertain.
- **Background needed**: - Protoplanetary disk: a rotating disk of gas and dust around a young star, where planets can form.
- Millimeter/submillimeter wavelengths: radio-like light used by ALMA, a telescope array in Chile, to see cold dust.
- Polarization: the preferred direction of light's wave vibration; elongated grains aligned by a field can imprint it on emitted or scattered light.
- Two polarization sources: dust scattering light and thermal emission from aligned grains; the paper separates these.
- Pressure bump: a ring where gas pressure peaks, trapping dust; disk substructures such as rings and gaps.
- Stokes number: a dimensionless measure of how strongly a grain is coupled to gas; larger values mean grains drift more independently.
- Trailing spiral: a spiral pattern whose arms lag behind the direction of rotation.
- Badminton-birdie alignment: grains oriented by gas flowing past them as they drift, like a shuttlecock moving through air.
- Significance (sigma): how confidently a signal stands out from noise; about 7 sigma is a strong detection under the authors' conservative error estimates. · level: research-level

<details><summary>Original abstract</summary>

Polarimetric observations of protoplanetary disks at (sub)millimeter wavelengths constrain dust grain properties, dynamics, and alignment mechanisms. We present new high-resolution ALMA Band 4 (2.1 mm) polarization observations of HL Tau with spatial resolutions of $\sim$0.08$''$ (11.78 au) and $\sim$0.19$''$ (27.99 au). Linearly decomposing the polarization into contributions from dust scattering and thermal emission by aligned grains, we analyze the new Band 4 data and published high-resolution Band 7 (870 $\mu$m) observations. Thermal emission from aligned grains dominates the polarization across the disk at Band 4, in contrast to the scattering-dominated Band 7, and both mechanisms vary radially with the disk substructures, consistent with expected optical depth variations. At Band 4, we detect a coherent angular deviation from purely azimuthal grain alignment, in which the streamlines of the alignment field yield trailing spirals with respect to disk rotation. A single global offset angle quantifies this deviation as $2.83^\circ\pm0.33^\circ$ and $4.10^\circ\pm0.09^\circ$ (statistical uncertainties) from two robust weightings, and the detection reaches a significance of $\approx7\sigma$ under conservative uncertainty estimates. This trailing orientation is consistent with aerodynamic ("badminton birdie-like") alignment driven by gas-dust drift near pressure bumps. However, under an axisymmetric disk velocity structure, this interpretation requires Stokes numbers two to three orders of magnitude larger than expected for the grains dominating the millimeter emission. At Band 7, the polarization angle is weakly sensitive to the alignment direction and exhibits a near/far-side antisymmetric structure that the model cannot reproduce. The Band 7 data therefore neither support nor contradict the Band 4 result.

</details>

### [Halley's Comet Over New Zealand In 1910: An Overview Of A Spectacular Apparition](https://arxiv.org/abs/2611.33170)
*John Drummond, Wayne Orchiston, Carolyn Brown et al.* · `physics.hist-ph` · arXiv:2611.33170v1 · relevance 0.11

- **In one sentence**: A historical survey of how widely Halley's Comet was observed in New Zealand during its 1910 apparition, drawing on newspaper reports and archival records and comparing them with accounts from abroad.
- **In plain words**: This paper looks back at the 1910 return of Halley's Comet, a famous comet that visits the inner Solar System about every 76 years. The authors searched old records and newspapers in New Zealand to see how many people watched it and what they saw. They report that thousands of New Zealanders observed the comet, and that the excitement helped start several astronomy clubs that still exist today.
- **Why it matters**: It gives a detailed, local view of a well-known event and shows how public interest in a comet can lead to lasting community science groups. The text does not say how these findings might connect to wider research, so its broader significance is unclear.
- **Background needed**: - Halley's Comet (1P/Halley) returns roughly every 76 years, so its 1910 appearance was a major public event.
- "Apparent magnitude" measures how bright an object looks from Earth; lower numbers mean brighter, and the comet reached about magnitude 1 or brighter in 1910.
- The comet's tail reached up to about 120 degrees, a large fraction of the sky.
- "Apparition" means a period when a comet is visible from Earth.
- Aotearoa is the Māori name for New Zealand; the paper uses both names.
- This is a historical study of observation records, not a study of new astronomical data. · level: introductory

<details><summary>Original abstract</summary>

Halley's Comet (1P/Halley) returns to the inner Solar System approximately every 76 years. In 1910, the comet put on a particularly wonderful display, whereby the comet attained an apparent magnitude of 1 or brighter, and had a tail of up to 120{\deg} in length. Many New Zealanders saw Comet 1P/Halley and submitted articles to newspapers across the land. Those articles were mostly from lay-people who reported their observations of this, the most famous of all comets. There were, however, numerous serious amateur and professional astronomers who made detailed observations and took world-class photographs of the comet. In this paper, we present the results of a thorough search through historical records and media publications in Aotearoa/New Zealand, to investigate how extensively Comet 1P/Halley was observed from this island nation. Where appropriate, we compare the observations described with international accounts, and find that those made from Aotearoa/New Zealand often echo what observers were witnessing around the world. We find that thousands of New Zealanders observed Comet 1P/Halley in 1910, and that the comet raised the interest in astronomy across the land resulting in the establishment of a number of astronomical societies that remain active to the current day.

</details>

## High-energy astrophysics

### [Fast radio bursts track cosmic star formation history with time delay: the effect of burst fluence](https://arxiv.org/abs/2611.33906)
*X. D. Jia, D. H. Zhai, J. P. Hu et al.* · `astro-ph.HE` · arXiv:2611.33906v1 · relevance 0.22

- **In one sentence**: Forward-modeling of CHIME/FRB non-repeating bursts finds that, once fluence (burst energy as seen at Earth) is included alongside dispersion measure, the FRB rate tracks cosmic star formation with little delay, whereas a DM-only analysis implies a 3–4 Gyr delay, which the authors attribute to biases in mapping fluence to signal-to-noise.
- **In plain words**: Fast radio bursts are very brief, very bright flashes of radio waves from distant galaxies, and nobody yet knows what produces them. This paper asks how often they occur at different distances into the past, which hints at whether their sources are young stars or old stars. The authors fit a model to the catalogued bursts from the CHIME telescope and report that the answer depends on whether the burst brightness (fluence) is included in the analysis.</plain>
<parameter name="why>Whether FRB sources are young or old objects is a basic open question about their origin, and the two earlier studies the paper mentions disagree. The paper suggests that a measurement choice, not just the data, can change the conclusion, which matters for anyone using FRB rates to test progenitor models. The text does not establish which progenitor model is correct.</plain>
<parameter name="background">- Fast radio bursts (FRBs): millisecond radio flashes from outside our galaxy; their sources are unidentified.
- Redshift: a measure of how far away (and how far back in time) an object is.
- Star formation rate (SFR): how quickly new stars form across the universe at each epoch; it peaks several billion years ago.
- Time delay: the lag between when stars form and when a source population forms or explodes. Young progenitors follow star formation closely; old progenitors lag behind it by billions of years.
- Dispersion measure (DM): how much a radio signal is smeared out by electrons along its path; used as a proxy for distance.
- Fluence: the total energy received per unit area from a burst; a brightness-related quantity that affects whether a burst is detected.
- Forward modeling: proposing a model of the source population, simulating how it would appear through the telescope's selection effects, and comparing with observations.
- CHIME/FRB: the Canadian Hydrogen Intensity Mapping Experiment's FRB detector and its published burst catalogs.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Fast radio bursts (FRBs) are luminous millisecond-duration radio transients of extragalactic origin, yet their progenitor systems remain unidentified. The redshift evolution of the FRB event rate provides a powerful, model-independent discriminant between young progenitors and old progenitors, but recent studies have reached conflicting conclusions. In this work, we perform a forward-modeling analysis of the apparent non-repeating FRB sample from the CHIME/FRB catalogs to constrain the intrinsic FRB population. We find that the FRB rate follows the star formation rate (SFR) with little time delay when both dispersion measure (DM) and fluence are considered. In contrast, when only DM is taken into account, a significant time delay ($3 \sim 4$ Gyr) exists between the FRB rate and the SFR. The main reason for this discrepancy is that systematic biases exist in the mapping process from burst fluence to signal-to-noise ratio. These results support that at least a fraction of FRBs arise from a progenitor population whose event rate is delayed relative to star formation.

</details>

### [Quantum Noise-Limited Terahertz Interferometry for Distinguishing Ultra-Compact Supermassive Galactic Objects](https://arxiv.org/abs/2611.33488)
*Vishwas Patel, Pankaj S. Joshi, Swalih A. Valiyakath et al.* · `astro-ph.HE` · arXiv:2611.33488v1 · relevance 0.13

- **In one sentence**: A theoretical study proposing that terahertz-band space interferometry, operating near the quantum noise limit, could distinguish the lensed central images of a Schwarzschild black hole from those of a JMN-1 naked singularity around Sgr A* and M87*.
- **In plain words**: The Event Horizon Telescope has imaged the glowing gas around the centers of galaxies M87 and our Milky Way (Sgr A*). This paper asks whether a black hole and a hypothetical object without an event horizon, a "naked singularity," could be told apart by the way their light is combined across telescope spacings. The authors report that, for a simple model of gas falling in thinly and evenly, the two cases become separable on certain baseline ranges at noise levels they estimate are about 28 times below the EHT's 2017 statistical uncertainty.
- **Why it matters**: Whether the centers of galaxies contain event horizons bears on the cosmic censorship conjecture, a central open question in black hole physics. The text gives only a theoretical forecast for a future space interferometer, so it is a proposal to test rather than a demonstration.
- **Background needed**: - Event Horizon Telescope (EHT): a global network of radio dishes that produced the first images of black hole shadows, M87* in 2019 and Sgr A* in 2022.
- Event horizon: the boundary around a black hole beyond which light cannot escape.
- Naked singularity: a hypothetical compact object with a singularity but no horizon hiding it; the cosmic censorship conjecture says such objects should not form in nature.
- JMN-1: a specific family of spacetime models describing a naked singularity, used here as the alternative to Schwarzschild black holes.
- Gravitational lensing: bending of light by strong gravity, which shapes the central image.
- Interferometry and baselines: combining signals from telescopes separated by a distance (baseline); longer baselines probe finer detail. Measured in gigawavelengths (G-lambda), a unit of baseline relative to observing wavelength.
- Visibility: the complex Fourier-domain measurement interferometers record, from which images are reconstructed.
- Optically thin accretion: gas that is diffuse enough that light passes through it rather than being absorbed.
- Quantum-limited detection: the lowest noise that the laws of quantum mechanics allow for a detector. · level: research-level

<details><summary>Original abstract</summary>

The images of the galactic centers, M87$^*$ and Sgr~A$^*$, obtained by the Event Horizon Telescope (EHT) provide hitherto unknown revelations on these supermassive objects. The key issue here is the presence or otherwise of an event horizon at these ultra-compact entities. We show here that distinguishing the central images generated by gravitational lensing of a Schwarzschild black hole and a Joshi--Malafarina--Narayan (JMN-1) central naked singularity provides important insights into the nature of these supermassive objects and would help test the cosmic censorship conjecture, central to black hole physics. For optically thin spherical accretion onto Sgr~A$^*$, their interferometric visibilities become separable, independently of the emission model, on three baseline ranges within 1.4--6.2 G$\lambda$ at errors of $\simeq36\,\mu$Jy, and at $L_\star=2.64\,$G$\lambda$ at $\simeq71\,\mu$Jy. This is about 28 times below the 2017 Event Horizon Telescope statistical uncertainty. We suggest that the widest detection window demands minutes-long coherent integrations, favoring a near-quantum-limited space interferometer.

</details>

## Stars and the Sun

### [Transport of High Energy Protons from CME-Shock to the Sun and its Connection to Extended Gamma-rays Observed by FERMI](https://arxiv.org/abs/2611.33598)
*Vahe Petrosian, Meng Jin* · `astro-ph.SR` · arXiv:2611.33598v1 · relevance 0.09

- **In one sentence**: This paper tests whether long-duration gamma rays from the 2014 September 1 solar flare, seen by Fermi-LAT, could come from CME-shock-accelerated protons that escape back toward the Sun, by modeling proton transport with AWSoM MHD results and an analytic time-scale relation.
- **In plain words**: Some solar eruptions give off gamma rays for hours, even when the eruption happens behind the Sun's edge as seen from Earth. This paper asks whether those gamma rays come from high-energy protons that were accelerated by a shock wave pushed out by a coronal mass ejection (a huge bubble of solar material) and then travelled back down toward the Sun. The authors use a computer model of the solar wind to estimate the conditions the protons pass through, and they outline how the proton spectrum would change on the way down to the surface.
- **Why it matters**: Understanding where the particles behind these long gamma-ray signals come from bears on how the Sun accelerates particles that can reach Earth as solar energetic particles, a hazard for spacecraft and astronauts. The text only describes a planned comparison with in situ particle measurements, so it is not yet shown whether the scenario holds.
- **Background needed**: - Coronal mass ejection (CME): a large expulsion of magnetized plasma from the Sun, often driving a shock wave ahead of it.
- Gamma rays: the highest-energy form of light; here they are produced when fast protons collide with material at the Sun.
- Fermi LAT: a space telescope that detects gamma rays.
- Behind the limb (BTL): on the far side of the Sun as seen from Earth, so the flare is hidden from direct view.
- Alfvén wave / AWSoM: a model of the solar corona in which magnetic waves (Alfvén waves) heat and drive the solar wind.
- Mean free path: the average distance a particle travels before its direction is scattered by magnetic turbulence.
- Residence time / escape time: how long a particle stays at a given height before leaving.
- Proton spectrum: how many protons there are at each energy.
- Solar energetic particles (SEPs): protons and other particles accelerated by the Sun that reach Earth. · level: research-level

<details><summary>Original abstract</summary>

This work is motivated by the Large Area Telescope (LAT) observations of long-duration gamma rays from flares associated often with fast Coronal Mass Ejections (CMEs), several of which originate behind the limb (BTL) of the Sun. Our aim is to test the feasibility of the scenario whereby the gamma-rays are produced by CME-shock accelerated particles escaping from downstream to the Sun by investigating the transport of protons in this process for the flare of 2014 September 1. We use results from the global MHD modeling by the Alfv\'{e}n Wave Solar Model (AWSoM) to obtain the characteristics of downstream plasma, such as magnetic field geometry, Alfv\'en speed, and energy density of turbulence. This allows us to evaluate the variations of the proton scattering mean free path with energy and distance from the CME-shock. Using an approximate analytic relation between the relevant time scales of the transport, we determine the energy dependence of the residence time at (or escape time from) different distances above the photosphere, and determine the evolution of the proton spectrum from the acceleration site to the photosphere. These results can be used to obtain the spectrum of the observed gamma-rays. Inversely, because of insignificant energy loss or gain during transport, this is a reversible process and the spectrum of protons at the photosphere, obtained from the observed gamma-rays, can be ``de-evolved" back to the CME using the same algorithm. Comparison of these spectra with the in situ observations of Solar Energetic Particles (SEPs) could then shed light on their transport from the CME to the Earth.

</details>

### [Moon Radio Interferometer for Science and Exploration (MoonRISE): A Mission Concept for a Low-Frequency Radio Interferometer on the Lunar Farside](https://arxiv.org/abs/2611.33534)
*Saptarshi Bandyopadhyay, Marin Anderson, Alexander Hegedus et al.* · `astro-ph.IM` · arXiv:2611.33534v1 · relevance 0.08

- **In one sentence**: A mission concept for MoonRISE, a nine-dipole, fiber-tethered low-frequency (0.1-30 MHz) radio interferometer on the lunar farside, with science goals on solar wind scattering, the lunar ionosphere, and Uranian radio emission.
- **In plain words**: The paper proposes a lunar mission that would listen to radio waves below 30 MHz, a range that is blocked from Earth's surface by the ionosphere and by human radio noise. The Moon's far side is shielded from Earth's radio chatter, so the team argues it is the quietest place nearby to make these measurements. The text describes the science goals, a proposed landing site, an operating plan, and the instrument design, but it does not report new measured results.
- **Why it matters**: Radio frequencies below 20 MHz have been hard to observe from anywhere, so a working instrument there could test how solar wind affects space weather and reveal Uranus's radio emissions, which have not been observed since Voyager 2 in 1986. Whether the mission is ever funded and built is outside what this paper shows.
- **Background needed**: - Interferometer: several separated antennas whose signals are combined to act like one larger telescope with finer detail.
- Ionosphere: a charged layer of the upper atmosphere that reflects or distorts radio waves below about 20 MHz, which is why these frequencies are hard to observe from Earth.
- Radio frequency interference (RFI): human-made radio signals that swamp faint natural signals.
- Type III solar radio bursts: fast radio emissions from the Sun caused by electron beams moving through the solar wind.
- Solar radius: the Sun's radius as a unit of distance; 2-20 solar radii covers the region from near the Sun's surface out into the inner solar system.
- Dipole: a simple rod-shaped antenna.
- Regolith: the loose dust and rock layer covering the Moon's surface.
- Ground penetrating radar: a radar that images underground layers.
- Heritage: earlier missions or instruments whose designs this concept reuses (SunRISE and OVRO-LWA are named). · level: intermediate

<details><summary>Original abstract</summary>

The universe below 20 MHz remains one of space science's last unexplored frontiers, inaccessible from Earth due to its ionosphere and terrestrial radio frequency interference (RFI). We present the mission concept for the Moon Radio Interferometer for Science and Exploration (MoonRISE), an all-sky imaging, low-frequency radio telescope operating from 100 kHz-30 MHz from the lunar farside, the quietest radio environment in the inner Solar System. If realized, MoonRISE would be the first radio interferometer on the Moon and the first connected-element radio interferometer in space. Its science objectives are to (1) determine how solar wind turbulence drives plasma heating, acceleration, and space weather evolution in the inner heliosphere, by measuring the scattering of type III solar radio bursts between 2-20 solar radii; (2) constrain the density, structure, and variability of the lunar ionosphere and its effects on surface communication; and (3) resolve the plasma sources and magnetospheric dynamics that power Uranian Kilometric Radiation, observable for the first time since Voyager 2 in 1986. The same observations would yield all-sky maps of the low-frequency sky, subsurface structure at the landing site, and a characterization of the farside RF environment. The Radio Interferometer concept consists of nine 3.5 m dipoles embedded in a 1.5 km optical-fiber tether deployed by a rover, with power- and RF-over-fiber enabling RFI-free mapping. A rover-mounted Ground Penetrating Radar (300-2000 MHz) would measure regolith dielectric properties and bedrock depth to characterize the dipoles' RF performance. We describe the science objectives, a reference landing site in Lacus Luxuriae, a notional concept of operations, and the payload design and technology maturity. The concept builds on SunRISE and OVRO-LWA heritage and could serve as a basis for a future selected mission.

</details>

## Chemical physics

### [Dressed Time-Dependent Density Functional Theory: Opening and Closing a Pandora's box](https://arxiv.org/abs/2611.33377)
*Jack T. Taylor, Neepa T. Maitra* · `physics.chem-ph` · arXiv:2611.33377v1 · relevance 0.16

- **In one sentence**: This paper benchmarks and refines dressed time-dependent density functional theory (DTDDFT), a correction to adiabatic TDDFT for excitations with double-excitation character, addressing a protocol for when to apply it, how to build its matrix, an "undownfolding" reformulation, and a proposed dynamical-correlation fix.
- **In plain words**: Standard computer methods for predicting how molecules absorb light struggle with certain excited states, where two electrons move together rather than one. This paper looks at a correction called DTDDFT that helps with these cases and asks practical questions about using it: when it is needed, which orbitals to include, and how to handle numerical ambiguities. The authors test it on a set of small organic molecules and compare it against more expensive reference methods.
- **Why it matters**: Predicting light absorption accurately matters for designing dyes, photochemistry and materials, and this work shows where a cheap correction helps and where it needs care. The text reports benchmark comparisons on specific molecules but does not establish how broadly the approach will generalise.
- **Background needed**: - Time-dependent density functional theory (TDDFT): a widely used, relatively cheap way to compute molecular excited states and light absorption.
- Excitation: lifting an electron to a higher energy orbital; a "double excitation" moves two electrons at once, which standard TDDFT handles poorly.
- Oscillator strength: a measure of how strongly a transition absorbs light.
- Kohn-Sham states: the single-electron orbitals used within density functional theory.
- Tamm-Dancoff approximation: a simplification that drops some coupling terms to make calculations more stable.
- Wavefunction methods: more accurate but costlier quantum chemistry methods used here as reference.
- Triplet instability: a numerical failure producing unphysical imaginary excitation energies. · level: research-level

<details><summary>Original abstract</summary>

Dressed time-dependent density functional theory (DTDDFT) has been shown to overcome the inability of adiabatic TDDFT to describe excitation energies and oscillator strengths of double-excitation character, however, it is far from being a black-box method. Here, we outline and address several operational issues while benchmarking the approach on a range of molecules. We define a protocol to determine whether an excitation from adiabatic TDDFT needs a double-excitation correction, without requiring a priori knowledge of the state, and which Kohn-Sham states to build the frequency-dependent DTDDFT matrix from. We present an 'undownfolding' that replaces this frequency-dependent matrix by a linear frequency-independent one in a larger space, eliminating ambiguities in the iterative procedure required to diagonalize the former. We compare the performance of DTDDFT for both excitation energies and oscillator strengths, as measured by an approximate metric for their single-excitation character, for different choices of the underlying adiabatic density functional approximation, with and without employing the Tamm-Dancoff approximation, for molecular excitations predicted by wavefunction methods to have either partial or genuine double-excitation character. We propose a correction to DTDDFT to account for missing dynamical correlation that is removed in the truncation procedure inherent in the method, and discuss the possibility of unphysical imaginary frequencies reminiscent of the 'triplet instability' that may arise. We provide benchmark data for butadiene, hexatriene, octatetraene, cyclopentadiene, acrolein, naphthalene, ethylene, borole, and cyclopentadienone. In some cases, DTDDFT predicts frequencies with about as much accuracy as the same underlying adiabatic TDDFT predicts for the constituent and near-lying single excitations.

</details>

### [A general-purpose electron density model for molecular chemistry](https://arxiv.org/abs/2611.34732)
*Paolo Pegolo, Joseph W. Abbott, Michele Ceriotti* · `physics.chem-ph` · arXiv:2611.34732v1 · relevance 0.12

- **In one sentence**: A machine-learning model (PET-rho-OMol25), trained on four million molecular structures, predicts the ground-state electron density and spin polarization of molecules, approximating density-functional theory accuracy for a range of chemical diagnostics.
- **In plain words**: This paper describes a computer model that estimates how electrons are spread out around molecules, which is the information chemists use to judge how molecules will react. The authors trained it on about four million molecular structures in different charge and spin states. According to the text, it can process whole proteins in a few seconds on one graphics card, and its least reliable answers are flagged by a built-in uncertainty estimate.
- **Why it matters**: Electron density is usually obtained from slow quantum calculations, so a fast, transferable estimate could make reactivity analyses practical for much larger molecules such as proteins. The text claims accuracy close to density-functional theory for most properties, but the reach of that claim beyond the reported tests is not something the summary can confirm.
- **Background needed**: - Electron density: a map of where electrons are likely to be around a molecule; it determines much of its chemistry.
- Density-functional theory (DFT): a standard quantum-mechanical calculation method, widely used but computationally costly.
- Machine-learning potential: a model trained on existing calculations to predict results much faster than running the calculation directly.
- Spin density: how unpaired electrons are distributed, relevant to redox reactions (electron transfer) and magnetism.
- Diagnostics mentioned: vibrational Stark shifts (how bond vibrations respond to an electric field), halogen sigma-holes (positive patches on halogen atoms that guide bonding), hydrogen-bond basicity, and core-level shifts (energy changes of inner electrons, measurable by X-ray spectroscopy).
- OMol25: the large molecular dataset the model was trained on. · level: research-level

<details><summary>Original abstract</summary>

Universal machine-learning potentials predict molecular structure and stability at the accuracy of quantum mechanics, for a fraction of the cost. Properties derived instead from knowledge of the electronic structure give profound insights into chemical reactivity, but are not accessible with the same ease or transferability. We train PET-rho-OMol25, a model of the ground-state electron density and spin polarization of molecular systems on four million OMol25 structures in multiple charge and spin states. The model makes predictions for entire proteins in a few seconds on a single GPU, and enables estimation of important diagnostics of molecular structure and reactivity, such as vibrational Stark measurements, halogen $\sigma$-holes, hydrogen-bond basicities and core-level shifts, as well as spin density for redox chemistry and magnetism. PET-rho-OMol25 has an accuracy close to density-functional theory, with its least reliable predictions flagged by its built-in uncertainty estimator, for most properties and classes of compounds. It can be used as a drop-in replacement for electronic-structure calculations of the density, making insightful analyses available for larger and more complex structures.

</details>

## Materials science

### [Machine-Learning Spin-Fermion Models for Strongly Disordered Magnets: Sb-Doped MnTe](https://arxiv.org/abs/2611.33544)
*Do Hoon Kiem, Parul R. Raghuvanshi, David S. Parker et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33544v1 · relevance 0.10

- **In one sentence**: A machine-learning method that compresses first-principles calculations into disordered spin-fermion models, applied to altermagnetism in Sb-doped MnTe.
- **In plain words**: Some magnetic materials could be useful for future electronics that use electron spin, but most of them are electrical insulators. Adding impurities can make them conduct electricity, yet the impurities also scramble the atomic and magnetic arrangement, which is hard to simulate accurately. This paper trains a machine-learning model on detailed quantum calculations so that it can reproduce those results and then predict magnetic interactions in very large, randomly disordered samples.
- **Why it matters**: The authors report that, using this approach on antimony-doped manganese telluride, altermagnetism (a magnetic order with spin-split electronic bands) appears to persist up to about 25% antimony, and that disorder-induced broadening affects how selective the spin behavior is. The text is a short abstract, so the details of the method's accuracy and the strength of these claims cannot be checked here; the approach may be relevant to modeling other disordered magnets, but that is a judgment beyond the text.
- **Background needed**: - Spintronics: electronics that use the spin (an intrinsic magnetic property) of electrons as well as their charge.
- Altermagnets: a recently recognized class of magnets whose opposite-spin sublattices are not related by simple translation, producing spin-split electronic bands even with no net magnetization.
- Doping: deliberately adding small amounts of another element to change a material's properties, here making an insulator conductive.
- First-principles calculations: simulations built directly from quantum mechanics with no fitted empirical parameters, but computationally expensive for large systems.
- Spin-fermion model: a simplified model coupling localized magnetic moments to mobile electrons; exchange couplings describe how neighboring spins interact.
- Renormalization: systematically simplifying a detailed model into a coarser one that keeps the essential physics.
- Supercell: a large simulation box repeating the crystal structure, used here to represent random disorder. · level: research-level

<details><summary>Original abstract</summary>

Metallic altermagnets are promising for spintronics, but most altermagnets are insulating. Doping can induce metallicity, but introduces chemical and magnetic disorder that is challenging to model from first principles. Here, we introduce a machine-learning approach that renormalizes first-principles calculations onto disordered spin-fermion models. The learned models accurately reproduce first-principles magnetic and electronic properties and enable predictions of millions of inequivalent long-range exchange couplings in large disordered supercells. Applied to Sb-doped MnTe, the approach shows that altermagnetism persists up to about 25\% Sb, and reveals disorder broadening as a new factor controlling spin selectivity. More broadly, our work opens a route to combining renormalization with machine-learned Hamiltonians for strongly disordered materials.

</details>

### [AFM metrology for 3D high aspect ratio semiconductor structures](https://arxiv.org/abs/2611.34507)
*Hokyun Chin, Shihwei Yu, Lucas Rencker et al.* · `cond-mat.mtrl-sci` · arXiv:2611.34507v1 · relevance 0.10

- **In one sentence**: The paper shows atomic force microscopy (AFM) can resolve individual line-and-space profiles in high aspect ratio gate-all-around nanosheet transistor structures, both in the nanosheet region and the isolation region between sheets, and reports a statistical evaluation of their critical dimensions.
- **In plain words**: Modern computer chips are built from tiny three-dimensional transistors, and their features must be measured very precisely to keep manufacturing under control. This paper describes using a probe-based microscope (AFM), which feels the surface with a fine tip, to take clear measurements of very tall, narrow structures inside these transistors. The authors then ran a statistical analysis of the sizes they measured.
- **Why it matters**: Chip makers need to check feature sizes as transistors get denser and more three-dimensional, so a measurement method that is both fast and reliable matters for production control. The text does not report how the AFM results compare with other measurement techniques, so its wider value is not established here.
- **Background needed**: - Transistor: a tiny electronic switch; the basic building block of chips.
- Gate-all-around FET (GAAFET): a transistor design where the control gate wraps fully around thin channel layers.
- Nanosheet (NS): a very thin, flat sheet of silicon-based channel material stacked inside such a transistor.
- Aspect ratio: height divided by width of a feature; high aspect ratio means tall and narrow.
- Atomic force microscopy (AFM): an instrument that scans a surface with a sharp tip to map its shape at near-atomic scale.
- Critical dimension (CD): a key width or spacing that determines whether a chip works as designed.
- Lines and spaces: a repeating pattern of raised lines separated by gaps, used to test measurement quality.
- Metrology: the science of making precise measurements in manufacturing. · level: research-level

<details><summary>Original abstract</summary>

Transistors have long been the foundation of the semiconductor industry, with continuous architectural innovations enabling the scaling of integrated circuits while maintaining high performance. Advancements in deposition and lithographic techniques have further expanded design possibilities, while increasing structural complexity demands stricter process control. Atomic force microscopy (AFM) offers a rapid and reliable metrology solution, providing high-resolution measurements and robust statistical analysis of critical parameters. In this work, we present clearly resolved individual profiles of lines and spaces in high aspect ratio (HAR) gate all around FET (GAAFET)-type structures on both the nanosheet (NS) region and in the isolation region between the nanosheets and we present a comprehensive statistical evaluation of their critical dimensions.

</details>

## Soft matter and polymers

### [Length-scales and fractal scaling in dairy gels: comparisons of the insights from ultra-small angle neutron scattering and rheology](https://arxiv.org/abs/2611.34194)
*Koduvayur A. Ramya, Liliana de Campo, Markus Strobl et al.* · `cond-mat.soft` · arXiv:2611.34194v1 · relevance 0.14

- **In one sentence**: Compares fractal structure of acid- and rennet-induced dairy casein gels, measured by ultra-small-angle neutron scattering over ~60 nm to 15 µm, with bulk rheology interpreted through Shih-Wu-Morbidelli scaling models.
- **In plain words**: This paper studies how milk protein gels, such as the basis of yogurt and cheese, are built at small scales and how that structure sets their firmness. The authors made gels from reconstituted skim milk in two ways, by acid and by the enzyme rennet, and used a neutron-scattering method to look at structures roughly 60 nanometres to 15 microns across. They then linked those structural measurements to the gels' measured stiffness.
- **Why it matters**: Understanding how particles cluster into fractal networks helps explain the texture of foods and other particulate gels, so the link between structure and mechanical behaviour is useful. The text reports that the two techniques give similar fractal dimensions but different length sizes, and the authors say this leaves room to refine the models; the wider significance beyond dairy is not stated in the text.
- **Background needed**: - Gel: a semi-solid network that holds its shape and resists flow.
- Fractal dimension: a number describing how a branching, self-similar structure fills space; it relates to how the network scales from small to large sizes.
- Correlation length: the distance over which the self-similar pattern holds.
- Scattering (USANS): shining neutrons on a sample and reading the pattern of deflected neutrons to infer structure at a given size range; "q" is the scattering vector, where low q means large length scales.
- Rheology: measuring how a material deforms and flows under applied force; oscillatory rheology gives elastic (solid-like) and viscous (liquid-like) responses and a gelation time.
- Casein micelles: the protein particles in milk that aggregate to form the gel.
- Scaling models: equations relating structure at one size to bulk stiffness. · level: research-level

<details><summary>Original abstract</summary>

A key structural parameter that dictates the textural properties of a particulate gel is the fractal dimension (Df) of the network indicating self-similarity within the spatial range defined by the correlation length (xi). In this study dairy gels are formed from reconstituted skim milk at defined CM volume fractions via two different mechanisms: acidification, and enzymatic (rennet)-induction. Oscillatory rheology is performed to obtain the gelation times, the time-scale for the maturation of mechanical properties of the gel, and the viscoelastic properties of the gel. A direct probe of gel structure is ultra-small-angle neutron scattering (USANS) examining length-scales from approximately 60 nm up to 15 microns. Structural information is extracted from USANS of matured gels by comparing the measured differential scattering cross-section with that calculated from a model constrained by the sample composition. Time-scales for structural equilibration from USANS perspective were shorter than the rheological gelation time for both gels. Rheological scaling theories are utilized to relate the microstructure to their bulk mechanical properties. We show that the fractal scaling at low-q (scattering vectors), due to aggregation of CM, extracted from the USANS at the longest timescales is described by a power-law density-density correlation function, and that rheology relates - through Shih-Wu-Morbidelli models - the local elasticity both within and between the fractal flocs formed by these particles over different size ranges to the bulk moduli of the gels. There are similar values of fractal dimensions from both techniques but different sizes attributed to the complex fractal evolution during dairy gelation, which leaves space to refinements of the models.

</details>

### [Soft Matter, Hard Rules: Emulsions Follow the Laws of Granular Suspension Rheology](https://arxiv.org/abs/2611.33526)
*Wenjun Chen, Eric De Giuli, Matthieu Wyart et al.* · `cond-mat.soft` · arXiv:2611.33526v1 · relevance 0.12

- **In one sentence**: By imposing osmotic pressure instead of droplet volume fraction, the authors show that dense emulsion rheology collapses onto a pressure-dependent jamming point and a granular-style power-law divergence, yielding parameter-free constitutive relations that cover Newtonian, yield-stress and shear-thinning behaviour.
- **In plain words**: Emulsions are mixtures of tiny oil droplets in water, used in foods, medicines and bioengineering, and it is hard to predict how they flow. The authors used a newly developed instrument, the Capillarytron, to control the squeezing of droplets by osmotic pressure (the pressure that drives water across a membrane) rather than by how much space the droplets fill. They report that, once measured relative to the point where the droplets get packed too tightly to move freely, data from both control methods line up on one simple curve, much as granular suspensions such as sand-in-liquid mixtures do.
- **Why it matters**: If the claim holds, a single framework could describe flow across several soft materials and explain the Herschel-Bulkley model (a standard description of materials that need a push before they flow) by giving its fitted parameters a physical meaning. The authors also suggest links to rigidity transitions in biological tissues, but the text only raises this as a perspective, so that connection remains untested here.
- **Background needed**: - Emulsion: droplets of one liquid dispersed in another (e.g. oil in water).
- Rheology: the study of how materials flow and deform under stress.
- Volume fraction (φ): the share of the total volume occupied by droplets.
- Jamming: the point where particles are packed so densely that they can no longer flow freely.
- Osmotic pressure (Π): the pressure that pushes water through a membrane; here used as a control knob that squeezes droplets.
- Power-law divergence: viscosity or stress grows as a fixed power of the distance to the jamming point.
- Herschel-Bulkley model: a common empirical rule for materials with a yield stress and shear-thinning flow.
- Granular suspension: particles such as grains or solid spheres suspended in a fluid. · level: research-level

<details><summary>Original abstract</summary>

The flow of dense emulsions underlies applications from food and pharmaceutical processing to bioengineering, yet their rheology remains difficult to interpret under conventional volume-imposed conditions. Here, we change the control variable to osmotic-pressure using a recently developed instrument -- the Capillarytron. This approach reveals a unified rheological structure where the osmotic pressure $\Pi$, by controlling droplet deformation, sets a pressure-dependent jamming volume fraction. When expressed in terms of the distance to this jamming point, all rheological data -- spanning both $\Pi$- and $\phi$-imposed measurements -- collapse onto a single power-law divergence, akin to granular suspensions. The resulting constitutive relations provide a predictive, parameter-free description of emulsion rheology across Newtonian, yielding, and shear-thinning regimes. Together with recent results on soft spheres, our findings point to a unifying paradigm: Soft amorphous materials -- from soft spheres to emulsions and likely foams -- obey the same hard rules as granular suspensions, with softness entering through a pressure-dependent jamming point. This framework rationalizes Herschel-Bulkley rheology, assigns its parameters microscopic meaning, and opens perspectives on rigidity transitions in soft, deformable systems, including biological tissues.

</details>

## AI for chemistry and materials

### [Computing hydration free energies and crystalline solubility of drug-like molecules with MACE](https://arxiv.org/abs/2611.33408)
*J. Harry Moore, Paul Mortenson, Davide Branduardi et al.* · `physics.chem-ph` · arXiv:2611.33408v1 · relevance 0.35

- **In one sentence**: A workflow built on MACE machine-learning interatomic potentials (including a new λ-MACE variant) computes hydration and sublimation free energies to predict crystalline solubility of neutral drug-like molecules, reaching experimental accuracy for the hydration leg but a combined error of 1.53 log units.
- **In plain words**: Drug makers need to know how well a candidate molecule dissolves in water, because that affects how much of a pill the body absorbs. This paper tries to calculate that solubility from physics rather than from models trained on past measurements. The authors report that their method predicts how readily molecules dissolve in water (hydration) very accurately on 70 test compounds, but when the crystal-related step is added, the final solubility prediction is still about 1.5 log units off, which is well short of experimental accuracy.
- **Why it matters**: Solubility is a costly bottleneck in drug discovery, and physics-based predictions could generalise better than data-driven ones outside their training data. The paper is candid that the remaining gap lies in the crystal (solid-state) thermodynamics, so it is best read as a useful benchmark and a map of what still needs improving rather than a finished tool.
- **Background needed**: - Solubility: how much of a substance dissolves in a solvent; reported here as log units, where one unit is a tenfold difference.
- Free energy: a thermodynamic quantity that determines whether a process happens spontaneously; hydration free energy is the energy change when a molecule moves from gas into water.
- Sublimation free energy: the energy change when a solid turns directly into gas; used here to link the solid crystal to the dissolved state.
- Free energy perturbation: a simulation method that computes free energy differences by gradually transforming one molecule into another.
- Interatomic potential: a machine-learned function that estimates the forces between atoms, replacing slower quantum calculations or hand-built force fields.
- DFT (density functional theory): a standard quantum-mechanical calculation method used as the reference for accuracy.
- Chemical accuracy: roughly 1 kcal/mol error in energy, the benchmark the authors say is needed for each leg.
- FreeSolv: a public database of experimentally measured hydration free energies. · level: research-level
- Matched keywords: drug discovery, force field, crystal structure

<details><summary>Original abstract</summary>

Accurate prediction of thermodynamic solubility is critical in drug discovery, where it influences oral bioavailability and drives decisions in formulation chemistry. First-principles calculations of intrinsic solubility offer the potential to achieve superior generalization to existing direct, data-driven predictors, which often suffer significant performance degradation outside of their training distribution. Whilst free energy perturbation calculations provide a rigorous framework to estimate these quantities, their accuracy is typically limited by the quality of the empirical force field used. In this work, we present a computational workflow driven by the MACE family of machine learning interatomic potentials to compute the solubility of neutral drug-like molecules. We introduce $\lambda$-MACE, a potential optimised for condensed-phase free energy calculations, which enables hydration free energy calculations at experimental accuracy on an evaluation set of 70 compounds from the FreeSolv database selected for their relevance to medicinal chemistry. We further combine these hydration free energy calculations with sublimation free energy calculations to predict crystalline solubility given a known experimental crystal structure, on an additional set of 10 compounds. We achieve state-of-the-art performance for each leg of the calculation, with experimental accuracy for the hydration leg, and accuracy competitive with industry-standard DFT for the sublimation leg. However, the overall errors after combining both legs lead to accuracy of 1.53 log units. This is significantly above the experimental accuracy (0.17-0.6 log units). Closing this gap will require substantially tighter accuracy in each leg, on the order of half of chemical accuracy (0.5 kcal/mol), with crystalline thermodynamics the hardest remaining challenge.

</details>

### [PineIR: 3D molecular structures from an infrared spectrum alone](https://arxiv.org/abs/2611.34334)
*Giulio Benedini, Pierre-Paul De Breuck, Miguel A. L. Marques et al.* · `physics.chem-ph` · arXiv:2611.34334v1 · relevance 0.35

- **In one sentence**: PineIR is a generative model that builds 3D molecular structures atom by atom from an infrared spectrum alone, subtracting each atom's predicted spectral contribution as it goes, and is trained on machine-learned-potential IR spectra of millions of molecules.
- **In plain words**: Chemists often use an infrared (IR) spectrum, a fingerprint made by how a molecule absorbs light, to spot which chemical groups are present, but not to work out the full 3D shape of the molecule. This paper presents a computer model that tries to rebuild the 3D structure from the IR spectrum alone, without the extra measurements that earlier models needed. On computed spectra of molecules the model had not seen, the best of fifty candidate structures had the correct connectivity (which atoms are joined to which) in 43% of cases.
- **Why it matters**: Getting a full structure from one cheap, fast measurement would be useful for identifying unknown compounds, if it holds up on real measured spectra. The text only reports results on computed spectra, so how well it works on laboratory data is not shown here.
- **Background needed**: - Infrared (IR) spectrum: a plot of which frequencies of light a molecule absorbs; it reflects its bonds and groups.
- Connectivity: which atoms are bonded to which, the skeleton of a molecule, separate from its 3D arrangement.
- Conformer: a different 3D shape the same molecule can take by rotating around its bonds.
- Diastereomer: a stereoisomer (same bonds, different 3D arrangement at some centers) that is not a mirror image.
- Generative model: a machine-learning model that produces new structures step by step, here one atom at a time.
- Machine-learned interatomic potential: a fast learned approximation of the forces between atoms, used here to compute spectra cheaply instead of with full quantum calculations.
- B3LYP: a widely used quantum-chemistry method (hybrid density functional) for computing molecular properties; the model was later fine-tuned on spectra computed at this level.
- Held-out molecules: molecules kept out of training and used only for testing. · level: research-level
- Matched keywords: molecule, molecular, interatomic potential

<details><summary>Original abstract</summary>

Computing the infrared (IR) spectrum of a molecule from its structure is routine. The inverse problem is not. In practice, IR spectra are used to identify the functional groups present in a molecule, while the determination of its complete structure requires additional measurements. Machine-learning models that return 3D structures from IR spectra exist, but all of them need extra input, such as Raman, ultraviolet or nuclear magnetic resonance spectra, the molecular formula, or the number of atoms. In this work we present PineIR, a generative model that returns 3D molecular structures from the IR spectrum alone. PineIR builds the molecule atom by atom, and each atom is associated with its contribution to the IR spectrum. This contribution is subtracted from the input spectrum before the next atom is generated. To train it, we computed with a machine-learned interatomic potential the IR spectra of 4.6 million structures of 3.1 million molecules, including conformer ensembles. On computed spectra of held-out molecules, the best-ranked of fifty candidates has the correct connectivity in 43% of the cases, and the generated geometries reproduce the conformer and the diastereomer that produced the input spectrum. After fine-tuning on 161k spectra calculated with the hybrid functional B3LYP, the model can also be applied to spectra at this level of theory.

</details>

## Biochemistry

### [Domain Architecture Analysis Guides the Discovery of Unusual Glycyl Radical Enzyme Fusion Proteins](https://www.biorxiv.org/content/10.64898/2026.11.23.768175v1)
*Namkoong, G.; Greeley, N. M.; Drennan, C. L. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.23.768175 v1 · relevance 0.08

- **In one sentence**: Using sequence similarity networks and domain architecture analysis, the authors identify glycyl radical enzymes in photosynthetic eukaryotes (diatoms and related microalgae) that are fused to their own radical-activating enzyme, and show one such fusion protein works as an active pyruvate formate-lyase.
- **In plain words**: Enzymes that work without oxygen, called glycyl radical enzymes, are known mostly from bacteria and other microbes. This paper looks for new members of this family using computer maps of protein sequence similarity, and finds an unexpected group in algae that feed on light, where each enzyme is physically joined to the helper protein that switches it on.
- **Why it matters**: It suggests that oxygen-free metabolism may play a role in ecologically important algae such as diatoms, which the text describes as a previously unappreciated role. It also shows that looking at how protein domains are arranged can reveal new enzymes in large families; the broader significance beyond these findings is not established in the text.
- **Background needed**: - Enzymes are protein catalysts; this group uses a glycyl radical, a carbon-centered reactive species on a glycine residue, to drive hard chemical reactions.
- The radical is installed by a separate "activating enzyme" (GRE-AE), which here is physically fused to the catalytic subunit.
- Anaerobic metabolism means energy production in the absence of oxygen.
- Sequence similarity network (SSN): a map that groups proteins by how similar their amino acid sequences are.
- Domain architecture: the arrangement of structural building blocks within a protein.
- Pyruvate formate-lyase: a known glycyl radical enzyme that splits pyruvate into acetyl-CoA and formate.
- Cryogenic electron microscopy (cryo-EM): imaging of frozen molecules to reveal their 3D shape; here at low resolution.
- Diatoms: single-celled photosynthetic algae. · level: research-level

<details><summary>Original abstract</summary>

Glycyl radical enzymes (GREs) use a post-translationally installed glycyl radical cofactor to catalyze chemically challenging reactions that are critical for anaerobic metabolism in microorganisms. Despite its importance, the GRE superfamily remains undercharacterized in part due to the vastness of its sequence space. Herein, we use sequence similarity network (SSN) analysis to survey the sequence diversity of the GRE superfamily and identify previously uncharacterized subfamilies. By analyzing the conserved domain architecture of each uncharacterized cluster, we find an unexpected cluster of GRE sequences from diverse photosynthetic eukaryotes. Bioinformatic, biochemical, and structural studies together demonstrate that these GREs have their catalytic subunits fused with a GRE-activating enzyme (GRE-AE). We characterize a highly expressed member of this subfamily as a functional pyruvate formate-lyase that is activated by its fused AE. Low resolution cryogenic electron microscopy confirms that this protein is a naturally occurring fusion, with a central dimeric GRE domain and one GRE-AE domain on each side. We further find that the GRE/GRE-AE fusion proteins are transcriptionally active in a wide range of diatoms and related microalgae. Overall, these findings uncover a previously unappreciated role for GRE-mediated anaerobic metabolism in ecologically important phototrophs, reveal that an attached AE can install a glycyl radical species on its cognate GRE, and show that domain architecture analysis is a powerful strategy to find novel enzymes among large enzyme superfamilies.

</details>

### [Pseudo-helicase motifs of SecA involved in ATP-driven dynamic coupling for protein translocation](https://www.biorxiv.org/content/10.64898/2026.11.24.768852v1)
*Havers, D.; Allen, W. J.; Williams, T. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.768852 v1 · relevance 0.08

- **In one sentence**: Bioinformatic and structural comparison of the bacterial protein-translocation motor SecA with nucleic acid helicases identifies "pseudo-helicase" motifs, and site-directed mutants show these motifs help couple ATP use to polypeptide transport through SecYEG.
- **In plain words**: Cells must push newly made proteins across membranes, and in bacteria a motor protein called SecA does this by using energy from ATP, the cell's fuel molecule. This paper looks at SecA's resemblance to helicases, enzymes that unwind DNA and RNA, and asks how the motor uses fuel and changes shape as it moves a protein chain through a channel. The authors identified several regions in SecA that match those helicase motifs and changed specific amino acids in them, then tested the altered proteins in a reconstituted system.
- **Why it matters**: The text reports that these motifs matter for regulating ATP-coupled transport and let the motor sense the protein being moved, which helps explain how chemical energy becomes mechanical movement in this machine. The text does not establish how far these findings apply beyond bacteria or to other motors, so that connection is uncertain.
- **Background needed**: - Protein translocation: moving unfolded protein chains across a membrane, here through the SecYEG channel.
- SecA: a motor protein that uses ATP (cellular fuel) and pushes the protein through in steps, described as a Brownian ratchet (random thermal motion rectified by binding and release).
- Helicases: enzymes that use ATP to separate DNA or RNA strands; they share structural motifs (conserved short sequence patterns) with SecA.
- Pseudo-helicase motif: a region resembling a helicase motif that may no longer do the original job.
- Site-directed mutagenesis: changing single amino acids to test what each one contributes.
- Reconstituted system: purified parts recombined in a test tube to measure activity without the whole cell. · level: research-level

<details><summary>Original abstract</summary>

The ubiquitous Sec translocon is a highly conserved machine specialised for polypeptide translocation through lipid bilayers. In the bacterial system, the cytoplasmic motor ATPase SecA associates with the core channel complex SecYEG, through which unfolded polypeptides are driven across the membrane by a Brownian ratchet mechanism. How the energy released during the ATP-hydrolytic cycle is transduced to the conformational changes required for preprotein secretion is not well understood. Here, we re-explore the known homology between SecA and the nucleic acid helicases to better understand the fundamentals of dynamic energy coupling during biopolymer transport: how ATP-turnover is regulated by the engaged polypeptide, and how the ensuing conformational changes bring about transport. Using bioinformatics and comparative structural analysis we identify several motifs within SecA equivalent to those required for helicase activity. We then probe their involvement in protein translocation experimentally by site specific amino acid substitution and the analysis of reconstituted variant activity. The results show that the pseudo-helicase translocation motifs are important for regulating ATP-coupled protein transport, enabling the motor to sense and respond to the translocating polypeptide.

</details>

## Pharmacology and drug discovery

### [Ruthenium Coordination Architecture Redirects Imiquimod Antiviral Activity](https://www.biorxiv.org/content/10.64898/2026.11.16.765078v1)
*Prakash, P. G.; Carrasco, A. C.; Bajetto, G. et al.* · `pharmacology and toxicology` · bioRxiv doi:10.64898/2026.11.16.765078 v1 · relevance 0.09

- **In one sentence**: A Ru(II)-arene coordination complex of the TLR7 agonist imiquimod (lead trinuclear compound 7) shows anti-HSV-1/HSV-2 activity in cells and patient-derived ectocervical organoids, and transcriptomic and proteomic profiling suggests it restores interferon-responsive antiviral programmes.
- **In plain words**: Imiquimod is a drug that boosts the immune system and is already used to treat some skin conditions. This paper attaches it to a metal-containing structure (ruthenium) and tests the resulting compounds against herpes simplex viruses. The lead compound reduced virus activity in lab-grown cells and in human tissue models taken from the cervix, and it appeared to help restore the tissue's own virus-fighting signals that the infection had switched off.
- **Why it matters**: Herpes viruses are common and some strains resist existing antiviral drugs, so new approaches that work through the host's defences are of interest. The text supports the claim that metal coordination changes what imiquimod does, but it is an early-stage study, and the text does not show whether this would be safe or effective in people.
- **Background needed**: - Imiquimod: an immune-stimulating drug that activates TLR7, a sensor on immune cells that triggers antiviral responses.
- Interferons: signalling proteins the body releases to alert neighbouring cells to viral attack.
- Ruthenium(II)-arene complexes: metal-based molecules in which a ruthenium atom is bound to an aromatic ring and to other chemical groups; coordination chemistry studies how such metal centres bind and reshape drugs.
- Herpes simplex virus (HSV-1, HSV-2): common viruses causing cold sores and genital herpes; resistant strains complicate treatment.
- Organoids: small lab-grown tissue models derived from patient cells, used here to mimic cervical epithelium.
- Transcriptomics and proteomics: measuring which genes are switched on (RNA) and which proteins are present, to see how cells respond.
- Host-directed therapy: treatments that act on the body's own defences rather than directly on the virus. · level: research-level

<details><summary>Original abstract</summary>

Immune agonists can reinforce antiviral defence, but therapeutic efficacy requires control over the magnitude and quality of the host response. Here we show that metal coordination can reprogramme the pharmacology of imiquimod, a clinically used TLR7 agonist. A series of Ru(II)-arene-imiquimod complexes identified the trinuclear compound 7 as a lead with activity against Herpes simplex virus types 1 and 2 (HSV-1 and HSV-2), including clinical isolates and antiviral-resistant strains. Compound 7 directly reduced HSV-1 infectivity and broadly suppressed viral protein accumulation in infected fibroblasts. In patient-derived human ectocervical organoids, it reduced epithelial infection and the recovery of infectious virus. Transcriptomic and proteomic profiling showed that 7 selectively restored infection-suppressed interferon-responsive and antiviral restriction programmes. Thus, Ru coordination does not simply enhance imiquimod activity but redirects its pharmacology, coupling virus-directed activity to restoration of epithelial antiviral defence. These findings establish a broader principle: coordination chemistry can engineer the response profile of immune-active anti-infective agents and expand the design space of host-directed antiviral therapeutics.

</details>

### [High Throughput Screening Of FDA Approved Drugs As Potential Agonist Of Mu-Opioid Receptor](https://www.biorxiv.org/content/10.64898/2026.11.24.769065v1)
*Olaoyo, M. O.; Abioye, R. T.; Adeyinka, T.* · `pharmacology and toxicology` · bioRxiv doi:10.64898/2026.11.24.769065 v1 · relevance 0.06

- **In one sentence**: A high-throughput screen of 1,875 FDA-approved drugs for inhibition of cAMP signalling at the human mu-opioid receptor in CHO cells identified six hits, but naloxone-sensitivity and beta-arrestin2 follow-up showed that most did not appear to act through the receptor itself.
- **In plain words**: Researchers searched a library of approved drugs for ones that might switch on the mu-opioid receptor, the cell-surface target of painkillers like morphine. They tested drugs in mixtures, then one at a time, and measured a chemical messenger (cAMP) inside engineered cells. Most of the apparent hits did not behave like true receptor activators when a blocking drug (naloxone) was added, so the authors caution against trusting such hits without further checks.
- **Why it matters**: Repurposing existing drugs for pain relief could be faster than developing new ones, but screening assays can pick up effects that are unrelated to the target receptor. The paper is a useful example of why extra receptor-specific tests are needed before claiming a drug acts on that receptor or is "biased" toward one signalling pathway. The text does not show any clinical implication.
- **Background needed**: - Mu-opioid receptor (MOR): a protein on nerve cells that opioid painkillers bind to.
- Agonist: a molecule that activates a receptor; antagonist: one that blocks it.
- Naloxone: a drug that blocks opioid receptors; if a compound's effect is cancelled or shifted by naloxone, that suggests it works through the receptor.
- cAMP: a small signalling molecule inside cells; opioid receptor activation usually lowers it. The assay measured this drop, using a light-producing sensor.
- Forskolin: a chemical used to raise cAMP first, so that inhibition can be seen.
- Beta-arrestin2 recruitment: a second, separate receptor signalling readout, used here as an orthogonal check.
- DAMGO: a standard synthetic opioid used as the reference agonist.
- EC50/potency (nM): the concentration needed for a half-maximal effect; lower means more potent.
- Repurposing / deconvolution: testing known drugs for new uses, and working back from mixtures to find the individual active compound. · level: intermediate

<details><summary>Original abstract</summary>

The mu-opioid receptor (MOR) remains an important analgesic target, but the interpretation of ligand-directed signalling preferences requires discrimination between receptor-dependent responses and effects on downstream assay readouts. We screened a library of 1,875 drug compounds for inhibition of forskolin-stimulated cyclic AMP (cAMP) accumulation in Chinese hamster ovary cells expressing human MOR and a GloSensor reporter. Primary screening of compound mixtures identified 17 active wells containing 204 compounds. Deconvolution yielded nine initial hits, six of which produced interpretable concentration-response relationships: niclosamide, sanguinarine, hexachlorophene, ataluren, altrenogest and nitazoxanide. Five of the six showed maximal cAMP inhibition of 77-80% in the initial concentration-response experiment, compared with 81 +/- 6% for DAMGO; sanguinarine had a lower maximum (24 +/- 6%). All six were less potent than DAMGO. In antagonist experiments, 300 nM naloxone shifted DAMGO potency from 0.3 to 224 nM. Of the tested compounds, only altrenogest showed a statistically significant naloxone-associated shift (367 to 905 nM; P = 0.0117). Altrenogest produced no detectable beta-arrestin2 recruitment under the PathHunter assay conditions, whereas DAMGO produced a concentration-dependent response. Thus, most cAMP hits did not show evidence of naloxone-sensitive MOR activation, and altrenogest showed a limited but measurable antagonist-sensitive component. These results highlight the importance of orthogonal receptor-dependence testing before assigning MOR agonism or signalling bias to repurposing hits.

</details>

## Computational and systems biology

### [NanoHIV-DR: a Nextflow workflow for consensus and read level HIV-1 drug resistance profiling from Oxford Nanopore sequencing](https://www.biorxiv.org/content/10.64898/2026.11.20.768148v1)
*Lule, D.; Ssemwanga, D.; Kaleebu, P. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768148 v1 · relevance 0.08

- **In one sentence**: NanoHIV-DR is a Nextflow workflow that takes raw Oxford Nanopore HIV-1 sequencing data through basecalling, demultiplexing, host-read removal, filtering, alignment and consensus building, then reports drug-resistance mutations using both consensus-level (Sierra) and read-level analysis.
- **In plain words**: HIV treatment can fail when the virus carries mutations that make drugs less effective, so labs sequence the virus to check for them. This paper describes a software pipeline that automates the many computing steps needed to turn raw data from a portable DNA-reading device (Oxford Nanopore) into a readable drug-resistance report. The pipeline can also pick up mutations that exist only in a minority of viral copies, which a standard averaged result would miss.
- **Why it matters**: Faster, portable sequencing for HIV drug resistance could make testing easier to run in clinics with limited bioinformatics staff, which matters for treatment decisions. The text describes the workflow and its goals but does not report accuracy or validation results, so its practical performance is not yet shown here.
- **Background needed**: - HIV-1 drug resistance: viral mutations that reduce how well antiretroviral drugs work.
- Genotyping: reading the viral genetic sequence to look for these mutations.
- Oxford Nanopore sequencing: a portable method that reads long DNA/RNA strands by measuring electrical signal changes as they pass through a pore; raw signal files are POD5 format.
- Basecalling: converting raw signal into letters (A, C, G, T).
- Demultiplexing: sorting pooled reads back to their original samples by barcode.
- Read alignment and consensus: matching reads to a reference genome and summarising them into one sequence.
- Sierra: a tool that interprets resistance from consensus sequences.
- Nextflow: a workflow system for running chained analysis steps reproducibly. · level: intermediate

<details><summary>Original abstract</summary>

Oxford Nanopore sequencing offers a rapid and portable approach for HIV-1 drug resistance (HIVDR) genotyping, but analysis of the resulting long-read data requires multiple bioinformatics steps and currently available nanopore workflows are limited. We developed NanoHIV-DR, a Nextflow-based workflow that streamlines the analysis of Oxford Nanopore sequencing data and generation of HIVDR reports. NanoHIV-DR processes raw POD5 files through basecalling, demultiplexing, host-read removal, quality filtering, read alignment and consensus generation, before identifying resistance-associated mutations and interpreting predicted drug susceptibility. The workflow provides two complementary approaches to HIVDR analysis: consensus-based resistance interpretation using Sierra and read-level detection of resistance-associated variants, enabling mutations below the consensus level to be identified and quantified. Outputs are integrated with clinical metadata to generate human-readable HIVDR reports. NanoHIV-DR provides a reproducible and accessible workflow for Nanopore-based HIVDR analysis with reduced bioinformatics expertise and manual processing for translating long-read sequencing data into interpretable resistance profiles.

</details>

### [GlycoBind: a general toolkit for protein-glycan binding prediction](https://www.biorxiv.org/content/10.64898/2026.11.25.769100v1)
*Huang, X.; Tian, Z.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.25.769100 v1 · relevance 0.08

- **In one sentence**: GlycoBind is a computational toolkit that scores how likely a protein structure is to bind an intact IUPAC-named glycan, without needing a solved complex or docking pose, by combining frozen DeepGlycanSite protein features with frozen GlycanGT glycan graph features through a small trainable classifier.
- **In plain words**: Sugar chains (glycans) decorate proteins and cells and help them recognise one another, for example in immune responses and in how pathogens stick to host tissue. This paper presents GlycoBind, a software tool that takes a protein's 3D structure and a written description of a sugar chain and outputs a score for how strongly they might bind. The authors report a mean AUROC (a 0 to 1 measure of ranking accuracy, where 0.5 is chance) of 0.767 across five holdout tests grouped by protein, and say it ranked binding strength better than existing models on six external glycan-array datasets.
- **Why it matters**: Predicting which sugar chains a protein will grab is hard, and lab screening is slow and costly, so a tool that flags likely strong binders could help choose experiments. The text suggests possible uses in studying recognition mechanisms and designing glycan-targeted drugs, but these are stated as possibilities rather than demonstrated results.
- **Background needed**: - Glycans: chains of sugar molecules attached to proteins and lipids on cell surfaces.
- Protein-glycan binding: a protein physically docking onto a specific sugar chain, a key step in cell signalling and infection.
- Protein Data Bank (PDB) format: the standard file type for 3D protein structures.
- IUPAC-condensed notation: a text string that spells out a glycan's structure.
- Glycan arrays: lab plates printed with many different sugars, used to measure which proteins bind which glycans and how strongly.
- AUROC: a score for how well a model ranks true binders above non-binders; 0.5 is random guessing.
- Frozen representations: pretrained feature encoders (DeepGlycanSite, GlycanGT) whose weights are fixed; only the small final classifier is trained.
- Holdout test: evaluating on proteins or data withheld from training, to check the model generalises. · level: research-level

<details><summary>Original abstract</summary>

Protein-glycan recognition controls immune responses, host-pathogen adhesion, cell signalling and the functional organization of the glycocalyx. Computational models can predict protein binding to monosaccharides or short oligosaccharides, but predicting binding to structurally diverse intact glycans remains challenging. Here we present GlycoBind, a general toolkit that accepts a protein structure in Protein Data Bank (PDB) format and an International Union of Pure and Applied Chemistry (IUPAC)-condensed glycan, and returns a binding score without requiring a protein-glycan complex or a docking pose. GlycoBind adopts the frozen residue-state representation of DeepGlycanSite, a carbohydrate-binding-site predictor, and combines this protein representation with frozen GlycanGT graph representations through a compact trainable classifier. Across five protein-grouped holdouts, GlycoBind achieved a mean area under the receiver operating characteristic curve (AUROC) of 0.767. On six external glycan-array datasets after exact protein and glycan cleaning for both models, GlycoBind showed higher aggregate binding-strength ranking performance and stronger recovery of high-intensity binding pairs than the existing models. By prioritizing high-intensity pairs for experimental follow-up, GlycoBind may support mechanistic studies of protein-glycan recognition and the rational development of glycan-targeted therapeutics.

</details>

## Neuroscience

### [Representational geometry shapes noise-driven working memory errors](https://www.biorxiv.org/content/10.64898/2026.11.23.768703v1)
*Alleman, M.; Panichello, M. F.; Buschman, T. J. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.23.768703 v1 · relevance 0.10

- **In one sentence**: Electrophysiological recordings from monkey neocortex during a color working memory task suggest that "guess" responses arise from noise in the delay-period neural population code, with the shape of that population's color representation predicting each animal's error pattern.
- **In plain words**: When people try to remember colors or other items for a few seconds, they sometimes give an answer that looks random, as if they guessed. This study recorded brain activity from many sites across the monkey outer brain during a color memory task to ask where those guesses come from. The authors report that signs of guessing appear during the memory delay itself, and that the way the brain's activity is arranged for color matches the pattern of each animal's mistakes.
- **Why it matters**: It offers a neural explanation for a long-studied behavioral pattern, suggesting that random-looking errors in memory may reflect noise in how populations of neurons represent information. The text does not establish how far this generalizes beyond the two monkeys studied, so its wider relevance remains open.
- **Background needed**: - Working memory: the brief ability to hold information in mind after it is no longer visible, here for a short delay.
- "Guess" response: a recall answer that is unrelated to the item shown, which the authors treat as a sign of memory failure rather than a deliberate guess.
- Electrophysiological recording: measuring electrical activity of neurons with electrodes; here, from many sites across the neocortex (the wrinkled outer layer of the brain).
- Neural population geometry: the way the joint activity of many neurons is arranged in a high-dimensional space, so that similar stimuli map to nearby patterns.
- Encoding precision: how finely the brain represents a stimulus; lower precision means more noisy, less accurate memories.
- Noise: random variability in neural activity that can blur or distort the stored information. · level: research-level

<details><summary>Original abstract</summary>

Humans and other animals have strictly limited working memory capacity. When asked to recall one or more presented items after a delay period, subjects will occasionally recall an apparently random item: a "guess'' response. Where do these guesses come from? Using electrophysiological recordings from across monkey neocortex during the performance of a color working memory task, we show that the neural correlates of guess responses emerge during the memory delay -- and that variable encoding precision makes guesses more likely, especially in one of our two animals. If guess responses emerge due to noise, we hypothesize that the detailed neural population geometry for color should shape the distribution of behavioral responses. We confirm this hypothesis by showing that the representational geometry specific to each animal is consistent with their idiosyncratic patterns of errors. Despite the often assumed robustness of neural population representations, noise appears to be a key bottleneck on the reliability of working memory.

</details>

### [Auditory cortical population codes for pitch are cue dependent](https://www.biorxiv.org/content/10.64898/2026.11.25.769094v1)
*Tarka, V. M.; Gaucher, Q.; King, A. J. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.25.769094 v1 · relevance 0.07

- **In one sentence**: Using a linear decoder on 1085 ferret primary auditory cortex neurons, the authors show that population codes for fundamental frequency (F0) generalise across sounds only when those sounds share the same type of pitch cue (spectral or temporal), and that F0 information is distributed across the population.
- **In plain words**: The paper asks whether the brain's sound-processing area represents musical pitch the same way regardless of how that pitch is signalled in the sound. Researchers recorded from about 1,000 neurons in ferrets while playing 10 kinds of sound, then trained a simple decoder to read the pitch from the firing patterns. The pitch was read reliably within any one sound type, but transferred well only between sounds that carried pitch in the same way, and poorly between complex sounds and pure tones.
- **Why it matters**: It bears on how the brain achieves perceptual invariance, recognising the same melody across instruments, which is a basic question in hearing science. The text reports that pitch information is spread widely over the population while only about 20 neurons are enough to decode it, but it does not spell out what this means for hearing itself, so its wider implications are uncertain.
- **Background needed**: - Pitch: the perceived highness or lowness of a sound, tied to its fundamental frequency (F0), the rate of its repeating waveform.
- Spectral cues: pitch inferred from the spacing of harmonic frequency components in a sound.
- Temporal cues: pitch inferred from how the waveform repeats over time.
- Primary auditory cortex: the first region of the brain's cortex to process sound.
- Population code: information carried by the joint activity of many neurons rather than by one neuron.
- Linear decoder: a simple statistical model that maps neural firing patterns to a predicted value, used to test what information is present.
- Generalisation: whether a decoder trained on one set of conditions still works on different ones.
- Onset/offset responses: neural activity at the start and end of a sound. · level: research-level

<details><summary>Original abstract</summary>

Pitch provides a powerful example of perceptual invariance, enabling us to recognize the same melody across different instruments. The fundamental frequency (F0) at which a pitch is heard can be derived from either the harmonic spacing of frequency components (spectral cues), the waveform periodicity (temporal cues), or both. It is unclear whether population codes for F0 in auditory cortex are invariant across these acoustic cue classes. We addressed this question by training a linear decoder to predict F0 from the spiking responses of 1085 neurons in ferret primary auditory cortex to 10 sound types varying in their spectral and temporal composition. F0 could be decoded accurately when trained and tested on any individual sound type. However, decoding performance generalised well across sounds only if they contained the same class of pitch cue, and poorly between complex sounds and pure tones. Onset and offset responses carried different information about the F0 of complex sounds. Finally, approximately 20 neurons were sufficient to decode F0, but F0 information was widely distributed across the neural population. These findings show that F0 is represented in primary auditory cortex in cue-dependent, temporally multiplexed subspaces, with sparse pitch representations embedded in a distributed, robust population code.

</details>

## Genetics and genomics

### [Sequence-to-function embeddings across individuals capture rare and common variant heritability](https://www.biorxiv.org/content/10.64898/2026.11.23.768687v1)
*Billeci, F.; Anglada-Girotto, M.; Gusev, A. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.23.768687 v1 · relevance 0.07

- **In one sentence**: The paper introduces EMBHER, a variance-component framework that estimates how much gene-expression heritability is captured by the intermediate embeddings of a sequence-to-function model (Borzoi), and reports that these embeddings recover much of the genotype-explained whole-blood heritability and explain more rare-variant heritability than genotypes.
- **In plain words**: Scientists build AI models that predict how DNA sequence turns genes on or off, and they want to know whether the model's internal "summary" of a DNA sequence also reflects how people differ from one another. The authors created a method, EMBHER, to measure how much of the inherited variation in gene activity these internal summaries capture. They report that, for the Borzoi model applied to whole-blood data, the summaries capture much of what raw genotypes explain, and more than the model's final predictions do.
- **Background needed**: - Heritability: the share of trait variation across people that is explained by genetic differences.
- Gene expression: how strongly a gene is turned on, often measured as RNA levels.
- Sequence-to-function model: a deep neural network that predicts molecular activity (such as expression) from DNA sequence alone.
- Embedding: the list of numbers a neural network produces at an intermediate layer, a compressed internal representation of the input.
- Genotype: an individual's measured DNA variants, typically common ones.
- Rare variant: a genetic variant carried by very few people, hard to study individually.
- Variance-component model: a statistical method that splits trait variation into parts attributable to different sources. · level: research-level

<details><summary>Original abstract</summary>

Statistical genetics learns how DNA shapes gene expression from variation across individuals, whereas sequence-to-function models learn from variation along the genome. Because sequence-to-function models map sequence to molecular readouts through deep architectures, their intermediate representations could offer function-informed descriptions of genetic variation. Whether these representations capture differences between individuals, however, is unknown. Here we introduce Embedding-based Heritability (EMBHER), a variance-component framework that estimates the expression heritability captured by these representations. Applied to Borzoi, embeddings recover much of the whole-blood heritability explained by genotypes and far exceed the model's final predictions. Deeper layers increasingly prioritize functional, evolutionarily constrained sequence while encoding less ancestry information than genotypes. Embeddings also explain more rare-variant heritability than genotypes, consistent with sharing information across variants too rare to estimate individually. EMBHER integrates sequence-to-function models with statistical genetics, a first step towards population-to-function models.

</details>

### [Genetic Diversity and Geographic Structure of Nordic Rye Landraces and Historic Varieties: Expected Patterns and New Insights](https://www.biorxiv.org/content/10.64898/2026.11.25.769110v1)
*Tenhola-Roininen, T.; Bitz, L.; Haikka, H. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.25.769110 v1 · relevance 0.07

- **In one sentence**: A genetic survey using SSR and SNP markers of Nordic rye landraces, historic varieties and reference lines, reporting geographically structured differentiation within a largely shared gene pool.
- **In plain words**: This study looks at the genetic makeup of old rye types grown in Finland and neighbouring Nordic countries, such as local landraces (traditional farmer-kept populations) and older varieties. The researchers compared these with a few modern and reference rye lines using two different DNA-marker methods. They found that rye from different regions differs genetically, even though most of the material shares a common genetic base.
- **Why it matters**: The work bears on conserving crop diversity as climate change pushes interest in local, resilient varieties, and it suggests regional differences have persisted despite rye's cross-pollinating habit. The text does not report practical outcomes for breeding or conservation, so its wider significance is best treated as tentative.
- **Background needed**: - Rye is a cereal crop; this study focuses on Nordic (especially Finnish) material.
- Landrace: a traditional, locally adapted crop population kept and reproduced by farmers over generations.
- Historic or conservation variety: an older variety maintained for its genetic value and cultural heritage.
- SSR and SNP: two types of DNA markers (short repeated DNA segments and single-letter DNA variants) used to measure genetic differences.
- Population structure: how genetic variation is grouped, for example by region.
- Outcrossing: the plant mostly pollinates from other plants, which tends to mix genes.
- Gene flow: movement of genes between populations, here possibly via seed exchange.
- Admixture: mixing of genetic ancestry from different groups within one population.
- Outgroup: a reference group used for comparison that is expected to be distinct. · level: intermediate

<details><summary>Original abstract</summary>

Rye has been an important food crop and source of nutrition in Finland for centuries and remains so today. Rye landraces and old varieties are still grown on farmers' fields. Interest in local landraces and conservation varieties has grown during the last decade due to climate change and its negative effects on biodiversity and resilience. We explored genetic diversity and population structure in Nordic rye landraces, historic population varieties and reference materials using complementary SSR and SNP datasets. For comparative analysis of genetic diversity, the Finnish varieties 'Riihi' and 'Reetta', the German inbred line Lo7, a German hybrid variety, the Estonian variety 'Elvi', and the landrace 'Sangaste' were included as reference materials. Both SSR and SNP analyses revealed geographically associated genetic differentiation within an otherwise largely shared Nordic rye gene pool. Notably, the independently sampled Mustialan and NordGen accessions of the Norwegian 'Tvengsberg' landrace were each clearly differentiated from the remaining rye material in the SSR and SNP datasets, respectively. Finnish landraces ('Aunus', 'Hermanni', 'Iivo', 'Joppe', 'Paakkola', and 'Taavetti') showed broadly similar genetic profiles, although substantial admixture was evident. In the SSR analysis, the Estonian accessions 'Sangaste' and 'Elvi' clustered together with 'Reetta', 'Riihi', and the Finnish landrace 'Polvijarvi', suggesting a closer genetic relationship among these accessions, although 'Polvijarvi' has previously been considered a distinct Finnish landrace. The Finnish variety 'Hankkijan Jussi' formed a separate cluster; this variety originates from a selection derived from the 60Co-irradiated Russian variety 'Vjatka'. The modern inbred line Lo7 and an unnamed hybrid variety were included as outgroup controls and showed clear genetic divergence from the Fennoscandian landrace material. Although Nordic rye landraces are often assumed to share a common ancestry and may have been influenced by historical seed exchange among farming communities, both SSR and SNP analyses revealed geographically associated genetic differentiation. These results indicate that regional genetic differentiation has been maintained despite the outcrossing nature of rye and the potential for historical gene flow.

</details>

## Cell and molecular biology

### [H19 isoform switching during neuronal differentiation reveals a distinct pluripotency-associated non-canonical transcript](https://www.biorxiv.org/content/10.64898/2026.11.25.769322v1)
*Guzman, N. J.; Abadia, L. M.; Felicien, Y. L. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.25.769322 v1 · relevance 0.14

- **In one sentence**: In human stem cells induced to become neurons, a shorter, non-canonical H19 lncRNA isoform (variant 3) that starts from a unique first exon in the imprinting control region is predominant in pluripotent cells and falls below quantification limits during neurogenesis, while canonical H19 and IGF2 rise.
- **In plain words**: Cells carry a gene called H19 that can be read out in several slightly different versions, and this study asks which version is used when stem cells turn into nerve cells. The authors found that a shorter version, which starts from a different first segment, is the main one in stem cells and nearly disappears as the cells become neurons, while the standard version and the neighbouring IGF2 gene increase. Other cell types they tested, such as mesenchymal stem cells, mostly used the standard version.
- **Why it matters**: It shows that the same gene can be used in different forms depending on cell state, which matters for anyone studying H19 as a regulatory RNA, since most prior work focused on the standard transcript. The text suggests a possible link to OCT4 and SOX2 binding near the variant's start site, but this is only an association from public datasets and the functional role of the variant is not tested here.
- **Background needed**: - lncRNA (long non-coding RNA): an RNA molecule of over 200 nucleotides that is not translated into protein but can regulate genes.
- Isoform / variant: alternative versions of the same gene made by starting or splicing RNA differently.
- H19 and IGF2: neighbouring genes at the IGF2/H19 locus on chromosome 11, expressed from a region controlling parental imprinting (parent-specific gene silencing).
- Pluripotent stem cells: cells able to become any cell type; induced pluripotent stem cells (hiPSCs) are made from adult cells.
- Neurogenesis: the process by which stem cells become neurons; here driven by NGN2 and ASCL1 genes.
- RT-qPCR: a lab method that measures how much of a specific RNA is present; LLRQ means below the level where measurements are reliable.
- CAGE, long-read RNA-seq, ChIP-seq: methods that map where transcription starts, read full-length RNA molecules, and find where transcription factors bind DNA. · level: research-level

<details><summary>Original abstract</summary>

H19 is one of the earliest discovered and most extensively studied lncRNAs, yet most studies have focused on the canonical 2,315-nt transcript arising from the IGF2/H19 locus on chromosome 11. We examined H19 isoform usage during the pluripotency-to-neuronal transition using NGN2/ASCL1-induced neurogenesis in KOLF2.1J human induced pluripotent stem cells (hiPSCs). We show that a smaller, non-canonical isoform, variant 3, is the predominant H19 isoform in the pluripotent cells examined. This isoform lacks the large canonical promoter-derived exon 1 and contains a short, unique first exon encoded within the imprinting control region upstream of H19. Upon neuronal induction, isoform-specific RT-qPCR showed that variant 3 declined below the lower limit of reliable quantification (LLRQ) as canonical H19 and IGF2 mRNA increased. In contrast, human bone marrow-derived mesenchymal stem cells expressed canonical H19, while variant 3 remained below the LLRQ during neurogenic, osteogenic, and adipogenic differentiation. Independent FANTOM5 CAGE datasets supported transcription initiation in the predicted variant 3 promoter region in hiPSCs and human embryonic stem cells. Long-read RNA-seq identified transcripts linking the variant 3 first exon to downstream H19 exons. Public OCT4 and SOX2 ChIP-seq datasets showed recurrent peak overlap at the upstream OSM1 candidate region in pluripotent cells, with corresponding peaks absent in the differentiated datasets examined. Together, these findings support cell-state-associated regulation of the IGF2/H19 locus and identify alternative H19 isoform usage as a feature of human pluripotent cells.

</details>

### [Targeted protein depletion in quiescent fission yeast cells using an auxin-degron system](https://www.biorxiv.org/content/10.64898/2026.11.20.767346v1)
*Le Collen, D.; Vazquez-Bolado, A.; Wu, P.-Y. J.* · `cell biology` · bioRxiv doi:10.64898/2026.11.20.767346 v1 · relevance 0.08

- **In one sentence**: In nitrogen-starved fission yeast, the authors show that analog-sensitive kinase inhibition with non-hydrolyzable ATP analogs is unsuitable because the analog acts as a nitrogen source and triggers cell cycle re-entry, and that an auxin-inducible degron system gives rapid, lasting and reversible protein depletion in quiescent cells.
- **In plain words**: Cells can enter a resting, non-dividing state called quiescence and later wake up again. To study the proteins needed for this resting state, scientists often switch a protein off on demand, but it was unclear whether common switching methods work in resting cells. Using yeast starved of nitrogen as a model, the authors found that one chemical switch method fails because the chemical itself feeds the cells and restarts their division. They then show that a tagging system that tags a protein for destruction, triggered by a plant hormone-like chemical (auxin), can remove a target protein quickly and reversibly in resting cells.
- **Why it matters**: Many essential proteins cannot be studied by simply deleting their genes, so a reliable way to switch them off in resting cells is a useful methods advance for the field. The paper is a practical check of tools rather than a new biological mechanism, and its broader value depends on how well the auxin system works across other proteins and organisms, which the summary text does not establish.
- **Background needed**: - Quiescence: a reversible, non-dividing resting state that cells can stay in for long periods and later re-enter the cell cycle.
- Fission yeast (Schizosaccharomyces pombe): a single-celled model organism widely used in cell biology; nitrogen starvation drives it into quiescence.
- Analog-sensitive kinases: engineered enzymes (kinases, which add phosphate groups to proteins) that can be blocked by a modified ATP molecule; the ATP analogs used cannot be broken down by the cell.
- Auxin-inducible degron: a tag added to a protein so that, when a plant hormone-like molecule (auxin) is supplied, the cell's own machinery rapidly destroys the tagged protein.
- Conditional inactivation: switching off a protein at a chosen time, useful for essential genes whose complete loss would be lethal. · level: intermediate

<details><summary>Original abstract</summary>

Quiescence is a reversible, non-proliferative cellular state in which cells can remain for extended periods of time while retaining the ability to re-enter the cell cycle upon exposure to favorable conditions. This physiological state is critical for a broad range of biological processes, from stress response in unicellular systems to differentiation and development in multicellular organisms. Surprisingly, despite its recognized roles in cell biology in diverse species, key aspects of the regulation of quiescence remain poorly understood. To investigate protein function specifically in quiescence, a conditional activation approach is critical, in particular for factors that are essential for cell viability. However, the efficacy of a number of such inactivation strategies in quiescent cells remained unknown. Using nitrogen-depleted fission yeast cells as a well-established model for quiescence, we probed two types of commonly-used approaches: a targeted method for the reversible inhibition of engineered kinases using non-hydrolyzable ATP analogs, and a more general system targeting protein depletion using an auxin-inducible degron. Here we show that the use of analog-sensitive kinases is unsuitable for quiescent fission yeast cells, as the ATP analog serves as a nitrogen source and induces cell cycle re-entry. We then demonstrate how coupling a degron tag with a specific auxin ligand allows for rapid, lasting and reversible protein depletion in quiescent cells, providing a powerful tool for investigating the regulation of this crucial and widespread cellular state.

</details>

## Immunology and microbiology

### [A tricomponent mRNA pertussis vaccine elicits superior protective immunity over licensed acellular pertussis vaccine against emerging antibiotic-resistant variants](https://www.biorxiv.org/content/10.64898/2026.11.26.769370v1)
*Zhang, W.; Che, J.; Wang, G. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.26.769370 v1 · relevance 0.13

- **In one sentence**: A preclinical study in mice reporting that a three-antigen, lipid-nanoparticle-delivered mRNA pertussis vaccine (mPervax) produced stronger Th1 T-cell, Tfh and antibody responses than the licensed acellular vaccine Boostrix and protected against the reference strain and PRN- or FHA-deficient clinical isolates.
- **In plain words**: Whooping cough (pertussis) has been coming back in many countries, partly because the current acellular vaccine may not give long-lasting, strong protection and bacteria are changing. In this study, researchers built an experimental mRNA vaccine that carries instructions for three pertussis proteins, packaged in fat-bubble particles like those used in some COVID-19 vaccines. In mice, it triggered stronger immune responses than the licensed Boostrix vaccine and protected better against bacterial challenge, including against bacterial strains that lack some of the targeted proteins.
- **Why it matters**: Pertussis resurgence is a real public health concern, and the paper suggests that mRNA could be a route to better vaccines that still work when bacteria lose a vaccine target. Because the evidence comes from mice and a single comparison with one licensed vaccine, it is an early signal rather than proof that the vaccine would work better in people.
- **Background needed**: - Pertussis (whooping cough) is a highly contagious respiratory infection caused by the bacterium Bordetella pertussis.
- Acellular pertussis vaccines (aPV) use purified bacterial proteins rather than whole killed bacteria; Boostrix is a licensed combined tetanus-diphtheria-pertussis vaccine used as the comparator.
- mRNA vaccines deliver a genetic message that cells use to make a target protein, which the immune system then learns to recognise; lipid nanoparticles (LNPs) are the fatty carriers that protect the mRNA.
- The three antigens here are inactivated pertussis toxin subunit 1 (PTS1), truncated filamentous hemagglutinin (FHA) and pertactin (PRN).
- Th1 and Tfh cells are types of helper T cells that support strong antibody and cell-mediated responses; Th1 is linked to protection against intracellular or respiratory bacteria.
- Maternal antibody protection means antibodies passed from mother to offspring; "challenge" means exposing animals to live bacteria to test protection. · level: research-level

<details><summary>Original abstract</summary>

Pertussis remains a major global health burden and has been resurging rapidly over the past decade. The causes of pertussis re-emergence are multifactorial, including vaccine-induced pathogen evolution, antimicrobial resistance, and crucially suboptimal protective immunity elicited by the widely used acellular pertussis vaccine (aPV). In this study, we developed a tricomponent mRNA pertussis vaccine formulated with lipid nanoparticle (LNP), designated mPervax, which encodes inactive pertussis toxin subunit 1 (PTS1), truncated filamentous hemagglutinin (FHA) and pertactin (PRN). Compared to a commercialized Tetanus-diptheria-pertussis vaccine Boostrix, mPervax induced stronger and broader innate immune activation, superior antigen-specific Th1-type CD4+ T and Tfh cell responses, and robust B. pertussis-specific antibody responses with remarkably increased magnitude and functionality. In addition, mPervax conferred an efficient maternal antibody-mediated protection in offspring mice and reshaped the immune profile established by primary Boostrix immunization towards a Th1-phenotype when used as a heterologous booster. Furthermore, upon bacterial challenge, mPervax outperformed Boostrix not only against the WHO reference strain 18323, but strikingly provided effective protection against emerging antibiotic-resistant clinical isolates that are deficient in PRN and/or FHA. Collectively, these data demonstrate that the mRNA pertussis vaccine is superior to Boostrix in multiple contexts, and therefore holds promise for next-generation pertussis vaccine development.

</details>

### [Testing the impact of gut microbiome rewilding on the health of captive bumble bees](https://www.biorxiv.org/content/10.64898/2026.11.23.768741v1)
*Watrous, K. M.; Larson, M. J.; Hammer, T. J.* · `microbiology` · bioRxiv doi:10.64898/2026.11.23.768741 v1 · relevance 0.10

- **In one sentence**: Experimental test of whether inoculating captive Bombus impatiens colonies with wild-derived environmental gut bacteria ("microbiome rewilding") improves survival, reproduction, nutrition, or resistance to an opportunistic pathogen, finding no benefit from the environmental bacteria tested.
- **In plain words**: Bumble bees raised in captivity lose much of the variety of microbes they would normally carry from the wild. This study tried adding five wild-collected bacterial species back into captive bee colonies to see whether that restores health. Adding them did not change survival, egg-laying, or energy stores, and one of them, Arsenophonus, did not protect bees from a harmful bacterium, while gut material from captive bees did.
- **Why it matters**: Captive rearing is common for crops, conservation, and research, so a simple way to restore lost microbes would be useful. The result shows that putting wild microbes back does not automatically help, which suggests that which microbes are restored matters. The text does not establish how these findings would transfer to other species.
- **Background needed**: - The gut microbiome is the community of microbes living in an animal's digestive tract.
- Captivity tends to reduce microbial diversity, which may affect nutrition, disease resistance, and reproduction.
- "Rewilding" means deliberately restoring microbes found in wild animals.
- Bumble bees (Bombus) are important wild and crop pollinators, and colonies are often reared in captivity.
- "Core" bacteria are host-specialized microbes that persist in captive bees; environmental bacteria are those picked up from the outside world.
- Opportunistic pathogens cause disease mainly when the host's defenses are weak or the microbial balance is disrupted.
- Glycogen and lipids are stored energy reserves in the body. · level: intermediate

<details><summary>Original abstract</summary>

Animals and plants are often raised in captivity for food, companionship, conservation, or research purposes, a practice which typically reduces the diversity of their microbiomes. This loss of microbial diversity may in turn compromise host nutrition, pathogen resistance, and reproduction. Microbiome "rewilding"--restoring microbes present in the wild, but lost in captivity--has been proposed as a way to ameliorate these effects. However, it has only been tested in a handful of taxa. We evaluated the efficacy of microbiome rewilding in bumble bees (Bombus), a group of ecologically and agriculturally important pollinators. In captivity, bumble bees retain host-specialized "core" gut bacteria, but lack the diverse environmental bacteria commonly present in the gut of wild bees. We inoculated captive B. impatiens colonies with five species of environmental bacteria isolated from wild B. impatiens. Rewilding did not affect bee survival, reproduction, or nutrition (glycogen or lipid levels). We conducted a second experiment with Arsenophonus, the environmental bacterium exhibiting the highest colonization rate in captive bees, to test its role in resistance against an opportunistic bacterial pathogen. While inoculation with gut material from captive bees (which is dominated by core bacteria) completely protected hosts from pathogen infection, Arsenophonus inoculation had no effect. These findings demonstrate that microbiome rewilding is not always effective for sustaining the health of captive hosts.

</details>

## Cancer biology

### [Dissecting the Tumor Microenvironment at Single-Cell Resolution to Prioritize Candidate Tumor Antigens Across Multiple Cancer Types](https://www.biorxiv.org/content/10.64898/2026.11.24.768856v1)
*Tavares, T. V.; Silva, P. L. A. d.; Pantoja, L. B. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.24.768856 v1 · relevance 0.11

- **In one sentence**: A pan-cancer single-cell RNA analysis of 355,941 cells across 10 tumor types that ranks 30 candidate tumor-antigen genes by malignant-cell enrichment, healthy-tissue expression, epitope reports, recurrence, and survival association.
- **In plain words**: Cancer immunotherapy works best when there is a protein on tumor cells that the immune system can recognize without harming healthy tissue. This paper looks for such proteins by reading gene activity in individual cells from many tumors, and then checking each candidate against other published and public evidence. The authors narrowed about 22,779 genes down to 30 candidates.
- **Why it matters**: Finding good targets is a bottleneck for immunotherapy, so a systematic, reproducible ranking could help researchers choose what to test next. The text notes that three candidates (CLDN6, MAGEC2, PLAC1) have been studied in recent clinical immunotherapy work, and that some cancer-testis antigens look less suitable because they are also active in healthy cells; whether the ranking translates into effective treatments is not shown here.
- **Background needed**: - Tumor antigen: a protein made by cancer cells that immune-based treatments can target.
- Single-cell transcriptomics: measuring which genes are switched on in each individual cell, here across 21 cell populations.
- Malignant vs non-malignant cells: cancer cells versus normal cells such as immune or stromal cells in the tumor.
- Human Protein Atlas (HPA): a public database describing where genes and proteins are expressed in tissues; its enrichment categories were adapted for this work.
- Cancer-testis antigens (CTAs): proteins normally found mainly in the testis that are sometimes switched on in tumors.
- Epitope: the small part of a protein that immune cells recognize.
- Overall survival association: whether higher gene expression goes with longer or shorter patient survival.
- Nextflow pipeline: a shared, scripted workflow so others can rerun the analysis. · level: research-level

<details><summary>Original abstract</summary>

Cancer immunotherapy has emerged as a revolutionary therapeutic approach, advancing the treatment of several cancer types. However, the identification of candidate tumor antigens remains challenging, as multiple lines of evidence are required to establish malignant-cell enrichment and therapeutic suitability. This study aimed to characterize and prioritize candidate tumor antigen genes based on their enrichment in malignant cells through the integration of single-cell transcriptomic data with complementary immunological and clinical evidence from the literature and public databases. An integrated pan-cancer dataset comprising 355,941 cells across 10 tumor types and 21 cell populations was analyzed using enrichment categories adapted from the Human Protein Atlas (HPA). Candidates were characterized according to antigen classification, gene expression in healthy tissues, presence of reported epitopes, recurrence across tumor types, and associations between gene expression and overall survival. Among the 22,779 genes evaluated, 30 candidates were retained after the prioritization process. CLDN6, MAGEC2, and PLAC1 stood out due to previous investigations in recent clinical immunotherapy research. Additionally, 16 of these 30 candidates showed significant associations between gene expression and overall survival across distinct cancer types, potentially supporting their prioritization for further investigation as immunotherapy targets. In contrast, some cancer-testis antigens (CTAs), previously regarded as promising therapeutic targets, were found to have limited suitability due to their enriched, enhanced, or group-enriched expression in non-malignant cells. Most of these steps can be independently reproduced using the publicly available Nextflow pipeline developed for this study.

</details>

### [Dynamic Transcription Factor Coupling Shapes Adaptive Enhancer Programs Driving Tumour Cell Heterogeneity and Growth](https://www.biorxiv.org/content/10.64898/2026.11.24.769040v1)
*Sharma, S.; Lorzadeh, A.; Ye, G. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.24.769040 v1 · relevance 0.10

- **In one sentence**: In mouse intestinal stem cells with inducible Apc loss (a model of early sporadic colorectal cancer), SOX17 cooperates with constitutively active β-catenin to activate adenoma-specific enhancers, generating heterogeneous clones and supporting motility and growth; loss of SOX17 reduces these programs but some targets persist via alternative enhancers.
- **In plain words**: This study looks at how early bowel tumours (adenomas) become varied and adaptable from their very first steps. The researchers switched off the Apc gene in mouse gut stem cells, which mimics the most common first mutation in colorectal cancer, and mapped which switches controlling gene activity were turned on. They found that a protein called SOX17, which is turned on only in these tumours, works together with an always-active form of β-catenin to create groups of cells with different behaviours, and that removing SOX17 slows tumour growth but does not fully stop it.
- **Why it matters**: It suggests that tumour cells gain flexibility through early changes in gene regulation, which may help explain why tumours later resist treatment. The text reports links to human colorectal cancers, but the work is in mice and the abstract does not show how far the findings carry over to patients or to therapy.
- **Background needed**: - Colorectal cancer often begins with loss of the APC gene, which leads to constant activity of β-catenin, a signalling protein.
- Adenomas are benign-but-precursor growths that can progress to cancer.
- Transcription factors are proteins that switch genes on or off by binding to DNA regions called enhancers.
- Epigenetics refers to changes in how genes are switched on or off without altering the DNA sequence itself.
- Single-cell sequencing measures gene activity or chromatin state in individual cells, revealing differences within a tumour.
- Knockout or deletion means removing a gene to test its role. · level: research-level

<details><summary>Original abstract</summary>

Tumour cells are inherently plastic and develop clonal heterogeneity early, laying the foundation for future invasion, metastasis, and resistance to therapy. The molecular basis of these early adaptations remains incompletely defined. Using inducible Apc deletion in mouse intestinal stem cells to mimic the most common initiating event in sporadic colorectal cancer (CRC), we show that cellular heterogeneity and adaptability in early adenomas reflect tumour-specific transcription factor (TF) activities that establish dynamic epigenetic programs. Enhancer profiles and single-cell epigenomes and transcriptomes reveal cooperative partnering between SOX17, which is selectively induced in adenomas, and constitutively active {beta}-catenin. This cooperation activates adenoma-specific enhancers and generates clones with distinct gene-expression states that maintain stem cells in some populations and activate cell motility genes at the invasive front. These early epigenetic and cell states persist in distinct cellular clusters in advanced human CRCs. Loss of SOX17 attenuates target enhancers and associated genes, particularly those related to cell motility, and restricts adenoma growth. Accounting for incomplete adenoma eradication, however, other SOX17 target genes remain active by engaging alternative enhancers. Thus, epigenetic adaptability arises early in transformation, circumvents tumour cell vulnerability to TF perturbations, and supports cellular heterogeneity, plasticity, and malignant processes well into cancer progression. These findings have important implications for tumour evolution, treatment resistance, and approaches to develop new therapies.

</details>

## Ecology and evolution

### [Resonance-organized phase-locking, extinction and phase-dependent rescue in periodically forced populations with delayed Allee effects](https://www.biorxiv.org/content/10.64898/2026.11.23.767764v1)
*Sun, J.; Guichard, F.; Humphries, A. R.* · `ecology` · bioRxiv doi:10.64898/2026.11.23.767764 v1 · relevance 0.12

- **In one sentence**: A numerical study of a periodically forced Hutchinson-type population model with delayed density regulation and a strong Allee effect, mapping how forcing frequency and amplitude, resonance, Hopf-driven oscillations, and phase-dependent rescue shape extinction risk.
- **In plain words**: This paper asks when a population that is hit by repeating environmental swings (such as seasonal changes) is most likely to die out. The authors ran computer simulations of a population model in which individuals struggle when numbers are too low (a strong Allee effect) and growth responds to past conditions with a time lag. They report that extinction is most sensitive when the environmental rhythm matches the population's own natural oscillation, and that some populations recover only when the timing of their dip relative to the environmental cycle is favorable.
- **Why it matters**: Extinction risk under changing environments is a central question in conservation, and the paper argues that severity, abundance, or regularity alone cannot predict it. The findings are from a single theoretical model, so their relevance to real species is not established by the text and would need field data to test.
- **Background needed**: - Hutchinson-type model: a population growth equation with a time delay, so today's growth depends on numbers in the past.
- Allee effect: a population that falls too small declines further because mates or cooperation become scarce; a strong Allee effect has a threshold below which extinction follows.
- Periodic forcing: an outside influence that repeats on a fixed cycle, such as seasons.
- Resonance: when the forcing frequency matches a system's natural frequency, responses can be amplified.
- Arnold tongues: regions in parameter space where the population's oscillation locks onto the forcing frequency.
- Bifurcation: a qualitative change in behavior as a parameter varies; Hopf bifurcations create oscillations, saddle-node bifurcations create or destroy periodic orbits.
- Lyapunov exponent: a measure of whether nearby trajectories diverge (chaotic) or converge (regular). · level: research-level

<details><summary>Original abstract</summary>

Population persistence under environmental fluctuations depends not only on the magnitude of external disturbances but also on their interaction with endogenous population dynamics. However, how environmental resonance interacts with delayed density dependence and Allee effects to determine extinction risk remains poorly understood. Here, we investigate a periodically forced Hutchinson-type population model incorporating delayed density regulation and a strong Allee effect. Through numerical simulations, Lyapunov exponent analysis, and bifurcation continuation, we characterize the organization of population dynamics and extinction across environmental forcing frequencies and amplitudes. We find that extinction vulnerability is strongly organized by resonance between endogenous population oscillations and environmental forcing, with the lowest forcing amplitudes required for extinction occurring near the principal 1:1 resonance. The parameter space exhibits a hierarchy of frequency-locking regions consistent with Arnold tongues, including structures bounded by saddle-node bifurcations of periodic orbits. We further demonstrate that the carrying-capacity-to-Allee-threshold ratio governs the emergence of intrinsic oscillations through a Hopf bifurcation, fundamentally reorganizing the population's response to environmental forcing. Counterintuitively, lowering the Allee threshold can increase extinction vulnerability by strengthening destabilizing delayed feedback. Finally, we identify a history-dependent rescue mechanism through which populations can recover after temporarily crossing below the nominal Allee threshold. Successful recovery events exhibit systematic phase dependence relative to environmental forcing. Together, these findings demonstrate that extinction risk cannot be inferred from environmental severity, population abundance, or dynamical regularity alone. Instead, persistence emerges from the interaction between environmental timescales, endogenous oscillations, and history-dependent opportunities for recovery.

</details>

### [Explaining an early ground-nesting bee emergence with climate and occurrence data: Temperature, not precipitation, advances onset](https://www.biorxiv.org/content/10.64898/2026.11.23.768685v1)
*Thrift, C. N.; Ostwald, M. M.; Schlauch Saiyawong, J. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.23.768685 v1 · relevance 0.12

- **In one sentence**: A study of an unusually early spring emergence of the ground-nesting bee Melissodes tepidus timberlakei, using five years of nest monitoring at one site and 119 years of regional occurrence records, linking emergence timing to temperature and precipitation in the western United States.
- **In plain words**: Researchers noticed a type of ground-nesting bee coming out of its nests unusually early in spring 2026. They combined five years of nest observations from one site with more than a century of museum-style records of where this bee was found across the western United States. They report that warmer temperatures went with earlier emergence, while rainfall did not appear to.
- **Why it matters**: Bee emergence timing matters because it has to line up with when flowers bloom for pollination to work, and climate change could pull these schedules apart. The text supports a modest claim about temperature and emergence, and suggests monitoring ground nests as a useful tool; how far the findings generalize beyond this bee and these sites is not shown in the summary.
- **Background needed**: - Phenology: the timing of recurring seasonal events, such as when insects emerge or plants flower.
- Ground-nesting bees: bees that dig nests in soil, so their emergence can be watched by monitoring nest sites.
- Melissodes tepidus timberlakei: a long-horned bee species (a type of solitary bee) found in the western United States.
- Occurrence records: historical collection and sighting records that show where and when a species was found.
- Temperature versus precipitation: the study compares how warmth and rainfall each relate to emergence timing.
- Correlation: the study shows an association between climate and emergence, not proof that temperature directly causes it. · level: intermediate

<details><summary>Original abstract</summary>

Understanding the drivers of bee phenology is important for predicting how climate change may alter the temporal overlap between bee activity and plant flowering, with consequences for pollination. We documented unusually early emergence of Melissodes tepidus timberlakei Cockerell, 1926 at a perennial nesting site in spring 2026 and examined the relationship between emergence and climatic conditions with (1) five years of nesting observations at a single site, and (2) 119 years of M. tepidus occurrence records from across the western United States. We found that warming temperatures were associated with earlier emergence, whereas precipitation was not, and we emphasize the utility of monitoring ground nests to understand emergence drivers in bees during ongoing climate change.

</details>

## Plant biology

### [Augmenting chlorophyll fluorescence-based analysis of plant photosynthesis with genetically encoded biosensors](https://www.biorxiv.org/content/10.64898/2026.11.24.768924v1)
*Cislaghi, A. P.; Barreto, P.; Niemeier, J.-O. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.24.768924 v1 · relevance 0.06

- **In one sentence**: The paper combines genetically encoded fluorescent biosensors for stromal pH, stromal MgATP2-, and cytosolic pH and NADH/NAD+ with time- and wavelength-resolved chlorophyll fluorescence (ChloroSpec L1) in attached Arabidopsis leaves to link photosynthetic light reactions with subcellular metabolism.
- **In plain words**: Plants turn light into chemical energy in their leaves, and the chloroplast's internal chemistry and the cell's metabolism are closely tied to that process. This paper describes a way to watch both at once in living, attached leaves: glowing sensor proteins inside cells report on chemistry, while a light-based instrument measures how the leaf's photosynthetic machinery responds. The authors report that the chloroplast interior became more alkaline in light and returned when light was removed, and that under fluctuating light the chloroplast pH and cytosolic NAD redox state were linked to changes in photosystem II efficiency and non-photochemical quenching.
- **Why it matters**: Photosynthesis responds to changing light in ways that are hard to observe inside living tissue, so a method that reads cell chemistry alongside leaf-level fluorescence could help explain how plants regulate themselves in variable conditions. The text describes this as a platform rather than a finished explanation, so its broader significance for crop or plant science is not established here.
- **Background needed**: - Photosynthesis has "light reactions" that capture light energy in membranes of chloroplasts (the organelles in plant cells) and make energy carriers such as ATP.
- Chlorophyll fluorescence: chlorophyll re-emits a small amount of absorbed light; its changes reveal how efficiently photosystem II uses light and how much energy is dissipated as heat (non-photochemical quenching).
- Stroma: the fluid inside chloroplasts where many metabolic reactions happen; its pH and ATP levels change with light.
- Genetically encoded biosensors: fluorescent proteins engineered to change brightness when a specific molecule or pH changes, introduced into the plant's own genome.
- NADH/NAD+ is a redox pair (electron carriers) that reflects the cell's energy and metabolic state.
- Wavelength-resolved measurement means analyzing the colour/spectrum of emitted light, not just its intensity. · level: research-level

<details><summary>Original abstract</summary>

The status of the light reactions of photosynthesis is tightly linked to subcellular physiology and metabolism. Yet, monitoring how both these levels are coordinated in living plants has remained challenging to explore. Here, we combine genetically encoded biosensors with time- and wavelength-resolved chlorophyll fluorescence spectroscopy (ChloroSpec L1) in attached Arabidopsis thaliana leaves. Stromal pHluorin2 reported a reversible, light-dependent alkalinization in a single mesophyll layer of leaf discs imaged by confocal microscopy and over the illuminated area of attached leaves recorded by ChloroSpec, where a distinct overshoot appeared at all irradiances. Measurement of the light-response dynamics of stromal MgATP2-, cytosolic pH, and cytosolic NADH/NAD+ illustrates the flexibility of the approach to different biosensors and subcellular localizations. Under prolonged fluctuating light, simultaneous recordings linked progressive stromal alkalinization and slow cytosolic NAD redox integration to wavelength-dependent shifts in photosystem II efficiency and non-photochemical quenching. By coupling programmable illumination with multiplexed metabolic and spectroscopic readouts in planta, this platform bridges cellular bioenergetics and leaf physiology to dissect photosynthetic regulation under dynamic environments.

</details>

### [Functional divergence of D-, A-, and B-type cyclins in the moss Physcomitrium patens](https://www.biorxiv.org/content/10.64898/2026.11.22.768468v1)
*Gan, Y.; Ruan, J.; Li, M. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.22.768468 v1 · relevance 0.06

- **In one sentence**: A study of how D-, A- and B-type cyclins (cell-cycle regulators) and their CDK partners differ in function and binding in the moss Physcomitrium patens, using expression tracking, overexpression, loss-of-function mutants and yeast two-hybrid binding assays.
- **In plain words**: Cells divide in a timed sequence, and proteins called cyclins help set the timing by partnering with enzymes called CDKs. This paper looks at three families of cyclins in a small moss, asking what each one does and which partners it binds. The authors report that the families overlap in some roles but each also has its own job, such as D-type cyclins mainly starting cell division and B-type cyclins mainly controlling the mitosis step.
- **Why it matters**: Plants have expanded their cell-cycle gene families over evolution, and this work tests what that expansion means in a non-vascular land plant, which helps show how division control was organized early in plant evolution. The text also reports that overexpressing the B-type cyclin stopped gametophore (leafy moss shoot) development, suggesting complex tissues are especially sensitive to errors in mitotic control; the broader significance for other plants is not established by this text alone.
- **Background needed**: - Cell cycle: the ordered steps a cell goes through to copy its contents and divide (G1, S phase for DNA copying, G2, and M phase for mitosis).
- Cyclins: proteins whose levels rise and fall through the cycle; they partner with cyclin-dependent kinases (CDKs), enzymes that switch cell-cycle steps on.
- Cyclin classes: D-type acts early (entry and growth), A-type acts across S to G2/M, B-type acts mainly in mitosis.
- Physcomitrium patens: a moss used as a lab model; its life stage called the gametophore is the leafy shoot.
- Overexpression and knockout: boosting or removing a gene to see what changes.
- Yeast two-hybrid: a lab test in yeast that checks whether two proteins physically bind. · level: research-level

<details><summary>Original abstract</summary>

Cyclins and cyclin-dependent kinases (CDKs) are central cell-cycle regulators that have undergone diversification in land plants; however, the functional implications of this divergence remain incompletely understood, particularly in non-vascular lineages. Here, we systematically dissected the roles of the three principal cyclin classes--D, A, and B--in the model moss Physcomitrium patens. We show that CYCD2 exhibits constitutive expression throughout the cell cycle, CYCA2 is degraded during mitosis and transcriptionally activated post-mitotically, whereas CYCB1 is M-phase-specific and rapidly depleted at anaphase. Overexpression and loss-of-function analyses revealed functional divergence among these classes: cyclin D primarily governs cell cycle entry and vegetative growth; cyclin B regulates mitotic progression with its overexpression causing division failure and arresting gametophore development; cyclin A regulates S-to-G2/M transition and exhibits overlapping functions with both D- and B-type cyclins, contributing to vegetative growth, mitotic fidelity, and gametophore development. Yeast two-hybrid assays showed that CYCB2 associates broadly with both CDKAs and CDKBs, CYCA2 preferentially interacts with CDKAs, and CYCD1 binds CDKAs along with a subset of CDKBs. Collectively, our results reveal both overlapping and class-specific contributions of D-, A-, and B-type cyclins to cell-cycle progression and development in P. patens, and suggest that complex tissues (gametophores) are particularly vulnerable to mitotic cyclin dysfunction. These findings provide a foundation for understanding how cyclin diversification underpins developmental plasticity across different contexts in non-vascular land plants.

</details>

## Bioengineering and synthetic biology

### [Uncovering mechanisms of cell-free protein synthesis using tailored coarse-grained models](https://www.biorxiv.org/content/10.64898/2026.11.24.768839v1)
*Wagner, C. S.; Laohakunakorn, N.; Weisse, A. Y.* · `synthetic biology` · bioRxiv doi:10.64898/2026.11.24.768839 v1 · relevance 0.11

- **In one sentence**: A coarse-grained ODE model, tested against batch E. coli extract experiments, is used to compare competing hypotheses about gene-length-dependent transcription limits, energy depletion as the cause of reaction termination, and batch-to-batch variability in translation in cell-free protein synthesis.
- **In plain words**: Cell-free protein synthesis makes proteins outside living cells, using a broth made from cell extracts, and it is widely used in labs. This paper builds a simplified computer model of the process and checks its predictions against real batch experiments. The authors report that longer genes appear to limit how fast transcription runs, that running out of chemical energy (not the gene or protein steps themselves) is the main reason reactions stop, and that translation varies most between batches of extract.
- **Why it matters**: Cell-free systems are a common tool in synthetic biology, and the paper suggests model-guided ways to raise yield and make results more reproducible. The text does not show how far these findings generalise beyond the authors' E. coli batch experiments, so their practical impact is still to be tested.
- **Background needed**: - Cell-free protein synthesis: making proteins in a test tube using the molecular machinery extracted from cells, instead of growing living cells.
- Transcription: copying a gene's DNA into messenger RNA. Translation: reading that RNA to build a protein.
- Coarse-grained model: a simplified model that groups many molecular details into fewer variables.
- Ordinary differential equations (ODEs): equations describing how quantities such as concentrations change over time.
- Batch reaction: a single closed run where ingredients are mixed once and the reaction proceeds until it stops.
- Design-build-test-learn cycle: an iterative loop of designing, making, measuring and refining a model or system. · level: research-level

<details><summary>Original abstract</summary>

Cell-free protein synthesis has revolutionised molecular biology research, and it continues to be a fundamental methodology in synthetic biology today. Yet, many of its mechanistic principles remain poorly understood, limiting our ability to predict reaction behaviour. In this work, we introduce a pipeline for uncovering these principles that combines computational models with experimental validation in a design-build-test-learn cycle. First, we develop a coarse-grained ordinary differential equation model describing key processes in the reaction. Next, we adapt the model to predict system behaviour under competing mechanistic hypotheses and compare model predictions to our experimental data from batch reactions using Escherichia coli extract. Our data and analysis indicate that gene length determines the rate-limiting step in transcription; it identifies transcription/translation-independent depletion of chemical energy as the primary cause for reaction termination; and finally it highlights translation as the most variable process between batches of cellular extract. Together, these results point to strategies for improving the yield and reproducibility of cell-free protein synthesis, and provide a framework for rational, model-guided design of cell-free systems.

</details>

### [Internet of Genetic Things (IoGT): Programmable Long-Distance Cybergenetic Logic Circuits Integrating IoT, Optogenetics, and Bacterial Gene Expression](https://www.biorxiv.org/content/10.64898/2026.11.23.768527v1)
*Paul, A.; Basu, R.; Pal, A. et al.* · `synthetic biology` · bioRxiv doi:10.64898/2026.11.23.768527 v1 · relevance 0.10

- **In one sentence**: The paper introduces the Internet of Genetic Things (IoGT), a framework in which internet-linked sensor nodes read colour-based reporter signals from engineered E. coli and trigger blue-light optogenetic control of gene expression in a remote bacterial population, demonstrated as BUFFER, OR, AND and NOT logic gates across sites up to 555 m underground.
- **In plain words**: Engineers have long wanted living cells in different places to coordinate, much as internet-connected devices do, but cells normally communicate only over very short distances. This paper describes a setup where bacteria at one site are monitored by optical sensors and a small computer, and when their signals reach set levels, a message is sent over the internet to switch on light that controls a second bacterial population elsewhere. The authors report that this worked as simple logic gates between sites 100 m apart and between a surface lab and a deep-underground lab.
- **Why it matters**: It shows a way to link living cells across distance using ordinary internet infrastructure, which could matter for distributed biosensing or biological control in remote or hard-to-reach settings. The text does not show how robust or scalable the approach is beyond these demonstrations, so its broader usefulness remains to be tested.
- **Background needed**: - Genetic circuit: engineered DNA that makes cells switch genes on or off in a logic-like way.
- Reporter gene: a gene whose output, such as a colour, shows that another gene is active.
- Optogenetics: controlling cell genes with light, here blue light.
- Boolean logic gates: simple yes/no rules (BUFFER copies an input, NOT inverts it, AND needs all inputs, OR needs any input).
- Escherichia coli (E. coli): a common lab bacterium used as a host for engineered circuits.
- Raspberry Pi: a small, cheap single-board computer used here to read the optical sensors and relay data.
- Internet of Things (IoT): networks of internet-connected sensing and control devices. · level: research-level

<details><summary>Original abstract</summary>

The Internet of Things (IoT) exchanges information and coordinates functions among geographically separated electronic devices. However, establishing analogous long-distance networks between genetically engineered living systems remains a challenge because synthetic genetic intercellular communication largely relies on local molecular signal transport. Here, we introduced a cybergenetic framework named the Internet of Genetic Things (IoGT) that autonomously regulated long-distance gene expression between geographically separated bacterial populations by integrating IoT, bacterial gene expression, and optogenetics. We engineered interconnected IoT nodes containing genetically engineered Escherichia coli, in which colour signals arising from reporter gene expression were detected using optical sensors interfaced with a Raspberry Pi. When gene expressions reached predefined thresholds and patterns, data were transmitted over the internet to a remote node, triggering blue light illumination to induce target gene expression in an optogenetically engineered E. coli population. Using this genetic, electronic, genetic communication architecture, we demonstrated cybergenetic BUFFER and OR gates between bacterial populations distributed across nodes separated by 100 m, as well as a cybergenetic AND gate coordinated among three locations. To demonstrate geographically extended operation, we constructed a cybergenetic NOT gate connecting a surface laboratory with a deep-subsurface laboratory located 555 m underground and more than 200 km away. To our knowledge, this was Indias first deep-subsurface biology experiment. IoGT was programmable. It reconfigured the same engineered bacterial populations into diverse Boolean logic gates BUFFER, OR, AND, and NOT gates. These results established IoGT as a programmable cybergenetic architecture capable of remote, multi-node intercellular gene expression control, having significant promise for distributed synthetic biology systems operating across remote or extreme environments.

</details>

## Mathematical biology (arXiv)

### [The evolution of extreme spatial heterochiasmy in amphibians: interactions between sex-specific meiotic program and chromosome architecture](https://arxiv.org/abs/2611.33634)
*Ezgi Unal, Paris Veltsos, Wen-Juan Ma* · `q-bio.PE` · arXiv:2611.33634v1 · relevance 0.10

- **In one sentence**: A review plus phylogenetic comparison of male chiasma (crossover) location across 97 amphibian species, testing how karyotype features and ancestry shape the sex-specific placement of meiotic crossovers.
- **In plain words**: Egg and sperm cells shuffle parental DNA by swapping segments during meiosis, and the places where these swaps happen can differ between the sexes. This paper looks at amphibians, where male swaps cluster near the ends of chromosomes while female swaps are spread along them. The authors compiled male crossover locations for 97 species and compared them with evolutionary family trees and chromosome shapes.
- **Why it matters**: Most studies of sex differences in recombination only compare total map length, which can hide differences in where swaps occur. The paper proposes that chromosome shape, rather than genome size or sex-chromosome type, is the strongest correlate of where male swaps fall, and that rearrangements like fusions or fissions could shift this without changing the underlying meiotic machinery. These are model-based suggestions from correlations across species, so they are plausible rather than established.
- **Background needed**: - Meiotic recombination (crossing over): the exchange of DNA segments between paired chromosomes when sex cells form; it reshuffles genes.
- Chiasma: the visible point where paired chromosomes are physically joined after crossing over; used as a proxy for crossover sites.
- Heterochiasmy: a difference in recombination between males and females.
- Interstitial vs terminal: crossovers in the middle of a chromosome arm versus near its tips.
- Telocentric vs metacentric: chromosomes whose centromere (the constriction point) sits near one end versus near the middle.
- Phylogenetic comparative analysis: statistics that account for shared ancestry among species.
- Ancestral reconstruction: inferring traits of extinct ancestors from living species; the authors say the result for deep ancestors is not conclusive. · level: research-level

<details><summary>Original abstract</summary>

Heterochiasmy, sex differences in meiotic recombination, is usually described in terms of genetic-map length, potentially obscuring more consequential differences in crossover location. Amphibians provide striking examples of extreme spatial heterochiasmy, with male recombination concentrated near chromosome ends and female recombination broadly distributed, yet the evolution and genetic basis of this pattern remains poorly understood. Here, we combine a review with a phylogenetic comparative synthesis of male chiasma location across 97 amphibian species. Male crossover localization is phylogenetically structured, and ancestral reconstruction favors predominantly interstitial recombination at deeper anuran nodes, although not conclusively. The strongest correlate of male terminal crossover location is chromosome morphology: telocentric-rich karyotypes retain more interstitial male chiasmata, whereas metacentric chromosomes show more terminal male chiasmata. Genome size and sex-chromosome system show little association. We propose a sequential model in which sex-specific meiotic regulation first establishes a crossover-precursor placement bias, while centromere position influences which precursors mature into crossovers. This model predicts that chromosome fusion, fission or centromere repositioning can alter male chiasma location without requiring changes to the underlying meiotic program. Our synthesis highlights crossover location as a distinct dimension of heterochiasmy with consequences for genome-wide linkage, adaptation, divergence and sex-chromosome evolution.

</details>

### [Resolving cell states in spatial transcriptomics with SCATTER](https://arxiv.org/abs/2611.34798)
*Lei Huang, Yun Gong, Weiqiang Lin et al.* · `q-bio.QM` · arXiv:2611.34798v1 · relevance 0.09

- **In one sentence**: SCATTER is a method that deconvolves mixed spatial transcriptomics spots into per-cell-type proportions and cell-type-specific expression profiles, using a single-cell reference, spatial neighborhood weighting, and Cell2location-based regularization of proportions.
- **In plain words**: Tissue maps made with spatial gene-activity technologies record gene activity in small spots, and each spot often mixes several cell types. This paper presents SCATTER, a computational tool that estimates how much of each cell type is in each spot and how each cell type behaves there, using a reference atlas of single cells and the spot locations. The authors report that it matched measured expression better than three other methods in most of their tests on pseudo-spots built from imaging data, and they show example analyses on breast cancer, multiple sclerosis, and colorectal cancer tissue.
- **Why it matters**: Being able to see how a cell type's gene expression changes across a tissue, rather than only how its share changes, could help link cell behavior to disease regions such as tumor edges or lesions. The benchmark results are reported only as pairwise win rates on pseudo-spots, and the biological examples are illustrative, so their broader value depends on further validation.
- **Background needed**: - Spatial transcriptomics: measuring gene activity (transcript counts) at fixed locations on a tissue section.
- Spots: each measurement location; in Visium-type data a spot can contain several cells.
- Deconvolution: estimating the mix of cell types inside a mixed measurement.
- Single-cell reference: an atlas of individually profiled cells used to define expected cell-type expression.
- Pseudo-spots: simulated mixed spots built from data where the true single-cell answer is known, used for testing.
- Xenium, Visium, Visium HD: commercial spatial platforms at different resolutions.
- Ligand-receptor pairs: signaling molecules and their receptors, used to infer cell-to-cell communication.
- Regulon: a set of genes controlled by a common transcription factor. · level: research-level

<details><summary>Original abstract</summary>

A capture spot can contain transcripts from multiple cell types. Differences between spots may reflect changes in cell-type proportions, expression within a cell type, or both, making local cell-type expression difficult to infer from mixed counts. We developed SCATTER to estimate cell-type proportions and relative expression profiles for each cell type at each spot from spatial transcriptomic counts, coordinates, and annotated single-cell reference data. SCATTER weights reference cell profiles using local spatial context, then jointly fits the resulting profiles and cell-type proportions to reconstruct spot counts. Cell2location estimates regularize the proportions. After fitting, SCATTER uses learned gene-specific calibration factors and fitted proportions to allocate observed counts among cell types. In five pseudo-spot benchmarks constructed from imaging data, SCATTER achieved higher cross-spot correlations with measured expression for 82.8-99.8% of evaluated gene-cell type pairs in pairwise comparisons with DestVI, PANDA, and STged. In breast cancer Xenium data, it recovered gene expression associated with the tumor neighborhood and regulon scores. In breast cancer Visium data, inferred stromal and macrophage expression showed distinct associations with neighborhood malignant cell proportions. In multiple sclerosis brain tissue, SCATTER recovered lesion-associated glial expression programs. In colorectal cancer Visium HD data, it mapped cell-type-specific programs at the invasive front and ranked candidate ligand-receptor pairs. SCATTER enables analysis of spatial expression variation within cell types from mixed tissue measurements.

</details>

## Epidemiology

### [Sources of protein in UK adults following contemporary plant-based diets: findings from the Feeding the Future (FEED) Study](https://www.medrxiv.org/content/10.64898/2026.11.23.26368579v1)
*Lawson, I.; Bell, W.; Key, T. J. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.23.26368579 v1 · relevance 0.06

- **In one sentence**: Cross-sectional analysis of the UK Feeding the Future (FEED) cohort (n=6,113) quantifying the food sources of protein across omnivore, flexitarian, pescatarian, vegetarian and vegan diets and the share of each group meeting the estimated average requirement (EAR) for protein, with and without under-reporters excluded.
- **In plain words**: This study looks at where protein comes from in the diets of about 6,100 UK adults who eat in different ways, from meat-eaters to vegans. The researchers estimated how much of each person's protein came from different food groups, and how many people got less protein than a basic daily need. Few people fell short, and most of the apparent shortfall among vegetarians and vegans disappeared once people who likely under-reported their food intake were removed.</plain>
<parameter name="why">Plant-based eating is becoming more common, and people often ask whether it provides enough protein. This paper gives a detailed, food-by-food picture for a large UK group, which is useful for nutrition guidance. The text reports only dietary questionnaire data, so it describes associations and reported intake rather than what people actually absorbed or how their health fared.</plain>
<parameter name="background">- Protein is built from amino acids and is needed for growth, repair and maintenance of tissue.
- The estimated average requirement (EAR) is the intake level expected to meet the needs of half of people in a group; it is not a personal target.
- Cross-sectional means data were collected at one point in time, so no cause and effect can be drawn.
- Food frequency questionnaire: a survey asking how often people eat listed foods, used here to estimate intake.
- Under-reporters: people whose recorded energy intake looks implausibly low compared with their likely needs, suggesting incomplete reporting.
- Plant-based meat alternatives and dairy alternatives are manufactured products (for example, tofu-like or soy-based foods); legumes and pulses are beans, peas and lentils.
- **Background needed**:  · level: intermediate

<details><summary>Original abstract</summary>

Objective To identify and quantify sources of protein intake in United Kingdom (UK) adults following different diets, and assess how these sources contribute to meeting protein requirements. Design Cross-sectional analysis of the Feeding the Future Study (FEED), a UK cohort recruited in 2022-2023. Dietary intake was assessed using an online food frequency questionnaire. We calculated the percentage contribution of food groups to daily protein intake, and the proportion of participants meeting the estimated average requirement (EAR) for protein, with and without exclusion of under-reporters. Setting A contemporary cohort of UK adults. Participants 6,113 adults: 1,540 omnivores, 1,322 flexitarians, 547 pescatarians, 1,212 vegetarians, and 1,492 vegans. Results Grains contributed 10-30% of total protein intake across all groups. Dairy contributed 12.9-14.2% in non-vegan groups, while plant-based dairy alternatives contributed less in vegans (7%), mainly from soy milk (4.3%). Other major contributors (>10%) were meat for omnivores (33.0%) and flexitarians (13.5%); fish for pescatarians (14.9%); plant-based meat alternatives for vegetarians (12.0%); and plant-based meat alternatives (15.0%), legumes and pulses (10.5%), and nuts and seeds (10.5%) for vegans. The proportion below the protein EAR ranged from 1.9% in omnivores to 14.0% in vegans, falling to 0.01% and 3.6% respectively, after excluding under-reporters. Conclusions Grains were a major contributor to protein intake across all diet groups, as was dairy in all non-vegan groups. Protein sources were more varied in non-omnivorous groups, particularly vegans. Few participants fell below the protein EAR and the higher proportions among vegetarians and vegans were largely attenuated after excluding under-reporters.

</details>

### [Meta-analysis of Sequencing Data Identifies Candidate Endometrial Cancer Susceptibility Genes](https://www.medrxiv.org/content/10.64898/2026.11.23.26368185v1)
*Laker, M.; O'Mara, T. A.; Spurdle, A. B. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.23.26368185 v1 · relevance 0.05

- **In one sentence**: A burden-test meta-analysis of rare protein-truncating and missense variants in 2,675 endometrial cancer cases and 160,654 controls from UK Biobank and 100,000 Genomes Project, reporting known and candidate susceptibility genes.
- **In plain words**: Endometrial cancer is the most common gynaecological cancer in wealthy countries, but its inherited causes are only partly known. The researchers looked at rare genetic changes across the protein-coding part of the genome in thousands of people with and without the cancer, asking which genes carry changes linked to higher risk. They confirmed the known risk genes MSH6, MLH1, MSH2 and PTEN and reported about 19 further genes, such as PHKG2, that they describe as candidates needing confirmation.
- **Why it matters**: Identifying inherited risk genes could eventually help find people at higher risk for screening or counselling. The text itself frames the new genes as preliminary candidates that still need replication in other studies, so their clinical value is not yet established.
- **Background needed**: - Endometrial cancer is a cancer of the lining of the womb (uterus).
- Genes are instructions for building proteins; a "variant" is a spelling change in a gene.
- Protein-truncating variants (PTVs) cut a protein short and often disable it; missense variants (MSVs) swap one building block for another, and only some are predicted to be harmful.
- Burden tests compare how often rare variants in a gene appear in cases versus controls.
- RR (relative risk) compares how much more likely someone with the variant is to develop the cancer; wide confidence intervals signal uncertainty.
- Exome-wide significance is a strict statistical threshold used to correct for testing thousands of genes at once.
- Mismatch repair genes (MSH2, MSH6, MLH1) are already known to raise risk of Lynch syndrome-related cancers. · level: research-level

<details><summary>Original abstract</summary>

BackgroundEndometrial cancer is the most common gynaecological malignancy in high-income countries, yet its genetic architecture remains incompletely understood. While pathogenic variants in mismatch repair genes are well-established contributors, the role of rare variants in other genes has not been systematically characterized. MethodsWe evaluated associations between rare genetic variants and endometrial cancer risk based on 2,675 cases and 160,654 controls from the UK Biobank and the 100,000 Genomes Project. Gene-level associations were assessed using burden tests, with protein-truncating variants (PTVs) and missense variants (MSVs) predicted to be deleterious analysed separately. ResultsEndometrial cancer (EC) risk associations were observed for three established EC susceptibility genes in the rare PTV analysis: MSH6 (RR = 36.6, 95% CI 25.9-51.8), MLH1 (RR = 52.5, 95% CI 21.3-129.4) and MSH2 (RR = 13.0, 95% CI 6.0-28.2). In the rare MSV analysis, PTEN was also significantly associated with EC risk (RR = 9.7, 95% CI 4.0-23.7). Beyond these established susceptibility genes, exome-wide significance was observed for 19 additional genes in the PTV analysis, including PHKG2 (RR = 29.8, 95% CI 9.6-92.8), and eight additional genes in the MSV analysis. ConclusionThis study identifies novel candidate genes associated with endometrial cancer risk, providing a foundation for future replication studies.

</details>

## Infectious diseases

### [Impact of expanded influenza vaccination programs in children and adults in Australia: a mathematical modelling study](https://www.medrxiv.org/content/10.64898/2026.11.23.26368629v1)
*Leung, T.; Stopard, I. J.; Wood, J. G. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.23.26368629 v1 · relevance 0.08

- **In one sentence**: A mathematical model calibrated to Australian surveillance data compares live-attenuated influenza vaccine (LAIV) programs for school-aged children against expanded inactivated vaccine (IIV) uptake in adults, measuring impact per dose given.
- **In plain words**: This paper looks at how best to use flu vaccines in Australia, where most current programs focus on protecting older adults. The researchers built a computer simulation of how flu spreads and gets vaccinated, checked it against real surveillance data, and compared a nasal-spray vaccine for children with strategies that get more adults vaccinated with the injected vaccine. They found the children's program was estimated to prevent the most hospital stays and deaths overall, though it was not the most efficient option for adults aged 65 and over.
- **Why it matters**: Flu causes serious illness each year, and this study tests whether a newer vaccine type could add to existing programs. The results are model estimates, not trial outcomes, so they depend on the assumptions built into the simulation; the abstract alone does not show how sensitive they are.
- **Background needed**: - Influenza (flu) is a common virus causing severe illness, especially in young children and older adults.
- Inactivated influenza vaccine (IIV) is the standard injected flu shot, mainly used to protect older adults in Australia.
- Live-attenuated influenza vaccine (LAIV) is a weakened live-virus vaccine, given as a nasal spray, now approved for children aged 2 to 17.
- Mathematical modelling uses computer simulations of how infection spreads through a population, here calibrated (tuned) to surveillance data, which are routine records of cases and hospitalisations.
- "Dose efficiency" means how much health benefit each vaccine dose delivers.
- "Number needed to vaccinate" (NNV) is how many people must be vaccinated to prevent one hospitalisation; a higher number means less efficient.
- Coverage is the share of the target group that is vaccinated. · level: research-level

<details><summary>Original abstract</summary>

Background: Seasonal influenza is a common cause of severe illness, particularly in young children and older adults. In Australia, influenza vaccination programs using the inactivated influenza vaccine (IIV) largely focus on direct protection of older adults. Live-attenuated influenza vaccine (LAIV) is now available for children aged 2-17 years, offering an opportunity to complement existing IIV programs. Methods: We developed a mathematical model of seasonal influenza transmission and vaccination in Australia, calibrated to surveillance data. We evaluated the health impact of LAIV programs on influenza burden relative to a baseline IIV-only scenario that assumed current coverage levels. We compared the dose efficiency of LAIV programs targeting school-aged children with strategies that increased IIV uptake in adults. Findings: An LAIV program targeting children aged 5-17 years was estimated to have the largest population-level impact, reducing influenza hospitalisations by 16% and deaths by 13%, assuming 55% coverage. An IIV program achieving 55% coverage in adults aged 50 years and older was predicted to have a similar population-level reduction in hospitalisations to a primary school-aged LAIV program (around 9.5%). Based only on doses administered, LAIV programs were more efficient at averting cases, hospitalisations, and deaths than strategies that expanded IIV uptake in adults. However, for outcomes in adults [&ge;]65 years old, increasing IIV uptake in this age group was estimated to be the most efficient strategy, with a number needed to vaccinate of 1811 to avert one hospitalisation. Interpretation: Our results support the potential use of LAIV as an additional tool in the prevention of seasonal influenza in Australia.

</details>

### [Distinct pulmonary transcriptomic and proteomic host signatures enable accurate diagnosis of severe lower respiratory tract infection](https://www.medrxiv.org/content/10.64898/2026.11.23.26368772v1)
*Lydon, E.; Sax, P. K.; Van Phan, H. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.23.26368772 v1 · relevance 0.08

- **In one sentence**: Paired transcriptomic and proteomic profiling of tracheal aspirates from critically ill children shows that RNA and protein measurements converge on similar immune pathways and give similarly accurate LRTI classifiers, despite poor gene-protein correlation.
- **In plain words**: Lower respiratory tract infections, such as pneumonia in the lungs and airways, can be hard to tell apart from non-infectious illness in very sick children. This study took samples from the airways of 105 critically ill children and measured both their gene activity (RNA) and their proteins. Both measurements pointed to a similar infection pattern, and both could identify infection with similarly high accuracy, though they picked out different key markers.
- **Why it matters**: It addresses whether it is better to measure RNA or proteins when looking for the body's immune response to infection, which matters for designing future diagnostic tests. The findings are from a single study of 105 children, so how far they generalise to other settings is not established by the text.
- **Background needed**: - Lower respiratory tract infection: infection of the lungs and airways, such as pneumonia or bronchiolitis.
- Tracheal aspirate: a sample of fluid suctioned from the windpipe of a patient on breathing support.
- Transcriptomics: measuring which genes are active, via their RNA messages.
- Proteomics: measuring the proteins present in a sample, which carry out most of the body's work.
- Gene-protein correlation: whether a gene's RNA level tracks its protein level; poor agreement means the two measure partly different things.
- Classifier and AUC: a computer model that sorts patients into groups; AUC (area under the curve) near 1 means very accurate, and above 0.90 is high.
- Host signature: a pattern in the patient's own immune response, used as an alternative to detecting the microbe itself. · level: research-level

<details><summary>Original abstract</summary>

Lower respiratory tract infection (LRTI) is a leading cause of acute respiratory illness, yet distinguishing it from noninfectious conditions remains a clinical challenge. Measuring the host immune response in the blood or lower airways, rather than exclusively detecting pathogens, has emerged as an alternative diagnostic strategy. However, it remains unclear whether RNA or protein measurements yield greater diagnostic information, or whether the two capture the same underlying biology. To address this, we performed paired transcriptomics and proteomics on tracheal aspirate specimens from 105 critically ill children with respiratory failure, 72 with microbiologically confirmed LRTI and 33 with noninfectious causes. Both approaches detected a clear host signature of LRTI which converged on similar core immune pathways including interferon signaling, inflammation, and complement activation. Despite this, agreement between individual genes and their corresponding proteins was largely poor. Diagnostic classifiers built from either RNA or protein data identified LRTI with similarly high accuracy (AUC>0.90), but selected different top biomarkers, and yielded discordant classifications for 12% of patients. Taken together, we find that lower airway transcriptomics and proteomics capture similar global biological features of LRTI despite poor correlation between gene and protein expression, providing fresh insight into approaches for biomarker discovery and clinical translation.

</details>

## Public and global health

### [Institutional Distrust as the Most Frequently Reported Barrier to Health Insurance Enrollment in Post-Conflict Liberia: A Mixed-Methods Study Extending the Andersen Behavioral Model with Trust as a Fourth Enabling Resource](https://www.medrxiv.org/content/10.64898/2026.11.22.26368698v1)
*Omisore, O. K.; Wollor, B.; Agala, V. et al.* · `health policy` · medRxiv doi:10.64898/2026.11.22.26368698 v1 · relevance 0.06

- **In one sentence**: A concurrent mixed-methods study in four Liberian counties (survey of 542 adults plus key informant interviews and focus groups) finds institutional distrust as the most often named barrier to health insurance enrollment among uninsured adults, and proposes adding trust as a fourth enabling resource to the Andersen Behavioral Model.
- **In plain words**: This paper looks at why most adults in post-conflict Liberia have not signed up for health insurance, where enrollment is below 15%. The researchers surveyed 542 adults, half insured and half not, and talked with local leaders and community groups to learn why people distrust the scheme. Among uninsured people, distrust of the insurance system was the most common main reason given, though only just ahead of cost and access problems.
- **Why it matters**: It argues that trust in institutions should be counted as a core factor in whether people use health services, not just money and distance, which matters for fragile states that run insurance schemes. The finding that trust barely edges out premium cost is a modest difference, and the study's design (one survey, four counties, 16 interviews) limits how far it generalizes; the paper's own reflexivity note also flags possible bias from its authors' experience with a Nigerian insurance program.
- **Background needed**: - Health insurance enrollment: signing up for a scheme that pays part of medical costs.
- Andersen Behavioral Model: a widely used framework saying health service use depends on need, predisposing traits, and enabling resources (money, organization, social support).
- Institutional distrust: doubt that the public body running a scheme will manage funds honestly, deliver promised benefits, or provide good care.
- Mixed-methods: combining numbers from a survey with interviews and group discussions.
- Logistic regression and odds ratios: a way to estimate how much a factor raises or lowers the odds of an outcome, adjusting for other factors. An adjusted odds ratio of 8 means roughly eight times the odds.
- Post-conflict and fragile states: countries recovering from war with weak government institutions.
- Key informant interviews and focus groups: structured conversations with knowledgeable people and small community groups. · level: intermediate

<details><summary>Original abstract</summary>

Health insurance enrollment in post-conflict Liberia remains below 15% despite a decade of reform, and the widely used Andersen Behavioral Model gives institutional trust no explicit place among the determinants of service use. We examined institutional distrust as a theoretically distinct barrier to enrollment using a concurrent mixed-methods design in four counties (Montserrado, Margibi, Nimba and Grand Gedeh). A cross-sectional survey of 542 adults (271 insured, 271 uninsured) ranked self-reported primary barriers and modeled enrollment with multivariable logistic regression; 16 key informant interviews and four focus group discussions, one per county, were analyzed thematically, combining deductive orientation to Andersens framework with inductive derivation of trust subtypes, and integrated with survey findings through joint display. Among uninsured respondents, institutional distrust was the most frequently reported primary barrier (57/271, 21.0%), narrowly ahead of premium cost (49, 18.1%) and inaccessibility of services (47, 17.3%), and the barrier distribution did not differ significantly by county. Four analytic subtypes were developed (fund-stewardship, benefit-delivery, provider-quality and generalized-state distrust), although direct evidence for provider-quality distrust overlapped with wider state-health-sector distrust. In multivariable analysis, socioeconomic status was the strongest structural predictor of enrollment: formal employment (adjusted odds ratio [aOR] 8.78, 95% CI 4.90 to 15.76), tertiary education (aOR 8.17, 4.12 to 16.20) and secondary education (aOR 7.36, 3.98 to 13.63) each independently raised the odds of enrollment, whereas informal employment (aOR 1.35, 0.81 to 2.24), sex and county were not significant. Socioeconomic status thus structures who enrolls, while institutional distrust is the barrier the uninsured most often name, a pattern the qualitative data corroborate. We propose extending the Andersen model to treat institutional trust as a fourth enabling resource alongside financial, organizational and social-support resources. In fragile states, trust-building should be treated as health-system infrastructure that complements, rather than replaces, financial-access measures. KEY MESSAGESO_LIAbout one in five uninsured adults in four Liberian counties named distrust of the insurance scheme as their main reason for not enrolling, slightly more than named premium cost, and the overall pattern of barriers did not differ significantly between urban, peri-urban, conflict-affected and remote counties. C_LIO_LIDistrust is not a single attitude. Participants distinguished doubts about whether premiums are safeguarded, whether promised services are delivered, whether care under insurance is of acceptable quality, and whether the state acts in good faith; each points to a different policy lever. C_LIO_LIEducation and formal employment remain the strongest predictors of who holds insurance, so trust-building must accompany, not substitute for, measures that lower financial and access barriers for informal-sector households. C_LIO_LIEnrollment strategies in fragile and post-conflict states should budget for trust-building as health-system infrastructure: ring-fenced and audited funds, published benefit guarantees, responsive grievance redress, quality monitoring and inclusive oversight, and studies using the Andersen model should measure institutional trust as an enabling resource. C_LI Reflexivity statementThe author team comprises public health and health systems researchers based at Nigerian institutions and a Liberia-based co-author: the first author is a doctoral researcher at the University of Port Harcourt, one co-author is based at a medical center in Liberia and facilitated field access, and the other co-authors bring experience from a state contributory health insurance program (RIVCHPP) and a university center of excellence in public health research. With most of the team working from Nigerian institutional bases, the team was attentive to the risk of importing assumptions from the Nigerian insurance context. Experience within the team of insurance program administration may have sensitized the analysis to scheme design and stewardship concerns. To examine how these positions shaped interpretation, the lead analyst kept reflexive memos throughout coding, community leaders were consulted on instrument wording, and preliminary findings were presented back to community focus groups in each study county before manuscript preparation. Ethical approvalEthical approval was granted by the Research Ethics Committee of the University of Port Harcourt (December 2024; reference UPH/CEREMAD/REC/MM105/030). A letter of local institutional support for data collection in Liberia was obtained (May 2026). Written informed consent was obtained from all participants. Funding, acknowledgements, conflicts of interest and author contributions are given in the Declarations section.

</details>

### [Association between Social Media Exposure and Self-Medication Practices: Public Health Implications in Punjab, Pakistan](https://www.medrxiv.org/content/10.64898/2026.11.22.26368645v1)
*Ashraf, A.; Saddique, M. A. B.; Sajid, M. S. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.22.26368645 v1 · relevance 0.06

- **In one sentence**: A cross-sectional survey of 280 adults in Punjab, Pakistan (March–May 2026) describes self-medication frequency and tests associations with social-media use, exposure to medicine advertising, and attitudes, finding only partial and cautiously interpreted links because the overall model was not significant.
- **In plain words**: This study looks at whether people who see medicine ads and health posts on social media are more likely to take medicines on their own without a doctor. The researchers surveyed 280 adults in Punjab, Pakistan, and found that most reported some self-medication, with fever and stomach medicines the most common. Some links appeared, such as with daily time spent on social media, age, and believing advertised medicines are safe, but the overall statistical model was not significant, so the results are tentative.
- **Why it matters**: Self-medication with medicines seen online can carry risks like wrong doses or hidden side effects, and social media is a growing source of health information in many countries. The paper is a small, single-region snapshot, so it cannot show that social media causes self-medication, but it may point to where public health messaging about medicine advertising should focus.
- **Background needed**: - Self-medication: taking medicines without consulting a doctor or pharmacist about them.
- Cross-sectional survey: a one-time questionnaire that captures a snapshot; it shows associations, not cause and effect.
- Chi-square test: a statistical check of whether two categories (e.g., ad recall and medication frequency) are related more than chance would suggest.
- Multinomial logistic regression: a model that estimates how several factors together relate to one outcome with several categories (here, rarely, frequently, more often).
- p-value: the probability of seeing results at least this strong if there were truly no link; p below 0.05 is the conventional threshold for "statistically significant."
- Nagelkerke R²: a rough measure of how much variation the model explains; 0.205 is modest.
- Sample: 280 adults aged 18–60 who completed a bilingual (Urdu/English) questionnaire, piloted with 30 people first. · level: intermediate

<details><summary>Original abstract</summary>

BackgroundSocial media has become an important source of health information, including information about medicines. Exposure to medicine-related content may affect decisions to use medicines without professional consultation. ObjectiveTo describe self-medication practices and social-media exposure among adults in Punjab, Pakistan, and explore associations between self-medication frequency and demographic, social-media-use, and attitudinal factors. Methods: A cross-sectional analytical survey was conducted among adults aged 18-60 years in Punjab between March and May 2026. The final analytic sample comprised 280 participants. A bilingual (Urdu/English) questionnaire assessed demographics, social-media use and health-content exposure, self-medication in the preceding six months, medicine categories, and attitudes. The questionnaire was reviewed by two clinical experts and piloted among 30 participants. Descriptive analyses, chi-square tests, and multinomial logistic regression were reported using IBM SPSS Statistics; significance was set at =.05. ResultsSelf-medication frequency was reported as Rarely by 117 participants (41.8%), Frequently by 130 (46.4%), and More Often by 33 (11.8%). Fever medicines were reported by 179 participants (63.9%) and gastrointestinal medicines by 96 (34.3%); multiple-response medicine categories were not mutually exclusive. Instagram was the most frequently selected social-media platform. Advertisement recall differed across self-medication frequency groups ({chi}2(22)=35.28, p=.036). Belief that medicines shown in advertisements/posts were safe was associated with self-medication frequency ({chi}2(4)=14.26, p=.007), while perceived risk was not ({chi}2(4)=1.587, p=.811). The multinomial models overall test was not statistically significant ({chi}2(40)=54.07, p=.068; Nagelkerke R2=.205). Likelihood-ratio tests identified associations for daily social-media-use duration ({chi}2(2)=13.085, p=.001), age group ({chi}2(6)=14.930, p=.021), and perceived advertisement safety ({chi}2(4)=10.899, p=.028). ConclusionSelf-medication was commonly reported in this sample. Some social-media-use and advertising-attitude variables were associated with self-medication frequency, but the overall regression model was not statistically significant and the cross-sectional design cannot establish causality. Findings should be interpreted cautiously given the sample composition and reported data limitations.

</details>

## Psychiatry and neurology

### [APOE ϵ4 Effects on Cognitive Decline and Progression to Dementia are Sequentially Mediated through Plasma P-tau217 and Hippocampal Atrophy in an Asian Cohort](https://www.medrxiv.org/content/10.64898/2026.11.22.26368713v1)
*Kan, C. N.; Chong, J. R.; Casado-Rodrigo, D. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.22.26368713 v1 · relevance 0.08

- **In one sentence**: In a Singapore cohort of older Asian adults, the APOE ε4 gene variant was linked to steeper cognitive decline and higher dementia risk through a chain running via plasma p-tau217, hippocampal volume, and entorhinal cortical thickness, with white matter hyperintensities not contributing.
- **In plain words**: The APOE ε4 gene variant is a known risk factor for Alzheimer's disease, but how it raises that risk may differ between populations. This study followed 659 older adults in Singapore for up to five years, measuring a blood marker of tau (p-tau217), brain scans, and yearly memory and thinking tests. The authors report that the gene's effect on decline and dementia ran largely through higher p-tau217 and shrinking of the hippocampus, a memory-related brain region.
- **Why it matters**: The work adds evidence from an Asian cohort, where such pathways have been less studied, and it points to blood p-tau217 and hippocampal volume as possible markers to track risk. The mediation effects are modest (about 9% to 14% of the effect), and the design is observational, so these are associations within a single cohort rather than proof of cause.
- **Background needed**: - APOE ε4 is a gene variant (allele) that is the strongest common genetic risk factor for late-onset Alzheimer's disease.
- Tau is a protein that forms tangles inside brain cells; p-tau217 is a form of tau that can be measured in a simple blood test and tracks Alzheimer's pathology.
- The hippocampus is a brain structure important for forming memories; atrophy means it shrinks.
- Entorhinal cortex thickness reflects the health of a region that connects to the hippocampus and is affected early in Alzheimer's.
- White matter hyperintensities are bright spots on MRI scans linked to small-vessel damage, often from blood vessel disease.
- Serial mediation analysis tests whether an effect passes through a chain of intermediate measures, one after another.
- Hazard ratio (HR) compares the rate of an event between groups; HR 2.35 means roughly 2.35 times the rate. · level: research-level

<details><summary>Original abstract</summary>

Background The APOE {epsilon}4 allele is a major genetic risk factor for Alzheimer's disease (AD) but underlying pathophysiological mechanisms may vary across populations. In Asian cohorts, the relative contributions of plasma phosphorylated tau (p-tau217), neurodegeneration, and cerebrovascular disease to {epsilon}4-associated cognitive decline remain unclear. Objective We investigated biomarker pathways linking APOE {epsilon}4 to cognitive trajectories and incident dementia. Methods APOE genotyping, plasma p-tau217 measurement, and neuroimaging were conducted at baseline in the Singapore Harmonization longitudinal cohort. Participants underwent annual comprehensive neuropsychological assessments for five years. We examined {epsilon}4 group differences in p-tau217, regional subcortical volumes, cortical thickness, and white matter hyperintensities (WMH). Serial mediation analyses examined mediating effects of plasma p-tau217 and neuroimaging markers on {epsilon}4 associations with cognitive decline and dementia risk. Results APOE {epsilon}4 was present in 29.4% of cohort (N=659; age=73.5{+/-}8.0 years; female=56.4%; Chinese ethnicity=83.6%). Carriers had higher p-tau217, reduced entorhinal thickness, and smaller hippocampus, amygdala, accumbens, and putamen volumes, but no WMH differences. Pathways from APOE {epsilon}4 through p-tau217 to hippocampal volume ({beta}=-0.009, 95% CI=-0.015, -0.004, 13.8%) and entorhinal thickness ({beta}=-0.008, 95% CI=-0.014, -0.004, 13%) significantly mediated steeper global and domain-specific cognitive decline. APOE {epsilon}4 was associated with increased dementia risk (HR=2.35, 95% CI=1.37-4.06), partially mediated by p-tau217 and hippocampal volume (9%). Direct {epsilon}4 effects were minimal and WMH did not influence these associations. Conclusions APOE {epsilon}4 contributes to cognitive decline and incident dementia through an AD-specific cascade captured by increased p-tau217 and hippocampal atrophy, providing population-specific insights into APOE {epsilon}4-related pathways in older Asian adults.

</details>

### [Parkinson's disease-associated LRRK2 armadillo domain variants enhance kinase pathway activity through a Rab-binding site-dependent mechanism](https://www.medrxiv.org/content/10.64898/2026.11.24.26368659v1)
*Rashidova, N.; Gomes, S.; Frances, R. E. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.24.26368659 v1 · relevance 0.08

- **In one sentence**: Cellular and primary-blood-cell study showing that the ARM-domain variant L488P in the Madrid LRRK2 haplotype boosts LRRK2 kinase pathway activity via ARM Rab-binding site 1, unlike catalytic-core variants.
- **In plain words**: Some inherited changes in a gene called LRRK2 raise the risk of Parkinson's disease, and most known ones act inside the protein's enzyme core. This paper studies a family with Parkinson's carrying two changes in a different part of the protein, the armadillo domain. The authors found that one change (L488P) increased the activity of the pathway LRRK2 controls, both in lab cells and in white blood cells from carriers, and that this effect depends on a docking site for Rab proteins.
- **Why it matters**: It suggests a second way that LRRK2 can be switched into an overactive state, outside the enzyme core that current drug efforts often target. The text does not show whether this matters for disease risk or treatment, and the number of variants tested is small.
- **Background needed**: - LRRK2 is a large protein whose overactivity is linked to a common inherited form of Parkinson's disease.
- LRRK2 adds phosphate groups to Rab proteins, which are switches that control how cargo moves inside cells; this is called Rab phosphorylation and is used as a readout of activity.
- The armadillo (ARM) domain is an N-terminal part of LRRK2 that binds Rab proteins and helps recruit LRRK2 to membranes.
- Known disease variants usually sit in the enzyme core (the ROC-COR and kinase domains), where they boost activity in different ways.
- Haplotype means a group of gene variants inherited together. Neutrophils and monocytes are white blood cells used here as accessible human samples.
- Mass spectrometry (PRM) measures specific phosphorylated proteins in a sample. · level: research-level

<details><summary>Original abstract</summary>

Pathogenic variants that increase LRRK2 kinase activity are a common genetic cause of Parkinson's disease. Most pathogenic variants occur within the catalytic ROC-COR GTPase (e.g. R1441C) and kinase (e.g. G2019S) domains, where they activate LRRK2 through distinct mechanisms. The common kinase-domain variant directly enhances the intrinsic catalytic activity of LRRK2, whereas ROC-COR variants shift the equilibrium towards its active conformation. Whether variants in the N-terminal armadillo (ARM) domain, which contains Rab GTPase-binding sites involved in LRRK2 membrane recruitment, activate LRRK2 through a different mechanism remains unclear. Here, we characterise the LRRK2 Madrid haplotype, comprising two ARM variants (L119P/L488P) identified in a multigenerational family with PD. In cellular assays, L488P, but not L119P, increased LRRK2-mediated Rab10 phosphorylation approximately two-fold. Increased LRRK2 pathway activity was likewise observed in primary neutrophils and monocytes from variant carriers, including individuals with and without PD. Multiplexed parallel reaction monitoring (PRM) mass spectrometry in neutrophils further demonstrated coordinated increases in phosphorylation of six endogenous Rab substrates (Rab3, Rab8, Rab10, Rab12, Rab35 and Rab43), demonstrating concordant pathway activation in cellular models and primary human blood cells. Mechanistically, L488P lies adjacent to ARM Rab-binding site 1, and its activating effect was abolished by the site-1-disrupting L403E substitution, whereas activation by the ROC-domain variant R1441C was retained. We further investigated five rare ARM-domain variants identified through GP2 and independent genetic datasets, of which two, F470S and V483G, showed increased LRRK2 pathway activity in a site-1-dependent manner, while the remaining three showed no substantial activation. Together, these findings demonstrate that L488P-mediated pathway activation is recapitulated in human variant carriers and depends on an intact ARM Rab-binding site 1, identifying a mechanism of LRRK2 regulation distinct from that of classical catalytic-core variants.

</details>

## Oncology

### [Non-Blood Liquid Biopsy of Nipple Discharge to Decode Tumor-Derived CNV Signatures for Breast Cancer Detection and Prognostication](https://www.medrxiv.org/content/10.64898/2026.11.24.26365856v1)
*Li, Y.; Pu, P.; Xu, H. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.24.26365856 v1 · relevance 0.04

- **In one sentence**: A study testing whether copy-number variations (gains or losses of DNA segments) in nipple discharge DNA can detect breast cancer, with single-cell analysis of where these signals come from and a prognostic "Fidelity Score" tied to survival in external cohorts.
- **In plain words**: Nipple discharge is a fluid that some people produce from the breast, and it can sometimes signal cancer, but telling harmful cases apart without surgery or biopsy is hard. The researchers looked for abnormal DNA patterns in the DNA carried by this fluid and compared them with DNA from blood plasma. In their clinical cohorts, the nipple discharge test detected cancer with 74.4% sensitivity and 94.4% specificity, while plasma DNA performed close to chance.
- **Why it matters**: The paper suggests nipple discharge may be a noninvasive sample that sits closer to the tumor than blood does, which could matter for screening people with discharge symptoms. It also links the DNA signals to estrogen-related cell activity and reports a score associated with better prognosis, though the text gives no detail on cohort sizes or how well these results will hold in wider use.
- **Background needed**: - Liquid biopsy: testing body fluids (here nipple fluid, or blood plasma) for tumor DNA instead of taking tissue.
- Copy-number variation (CNV): a region of a genome that is present in more or fewer copies than normal, a common feature of cancer cells.
- Cell-free DNA: small DNA fragments floating in body fluids, released by dying cells.
- Sensitivity and specificity: the share of cancers correctly flagged, and the share of healthy people correctly cleared.
- AUC: a 0-to-1 score of overall test accuracy, where 0.5 is no better than chance.
- Single-cell RNA sequencing: measuring gene activity in individual cells, used here to trace which cells the DNA came from.
- Estrogen signaling: a hormone pathway that drives many breast cancers.
- Prognostication: predicting likely outcome, such as survival. · level: research-level

<details><summary>Original abstract</summary>

Accurate, noninvasive diagnosis of malignant nipple discharge remains a longstanding clinical challenge. This study evaluated somatic copy-number variations (CNVs) in nipple discharge DNA (ndDNA) as high-fidelity diagnostic biomarkers and explored their cellular origins and shedding mechanisms. We derived a 20-feature CNV panel from large-scale genomic datasets and validated its diagnostic potential. Integrative single-cell analysis of 50 patients revealed that these features predominantly arose in ancestral states across molecular subtypes and exhibited functionally relevant co-occurrence patterns. In clinical cohorts, ndDNA-based detection achieved 74.4% sensitivity and 94.4% specificity (AUC = 0.863), significantly outperforming plasma cell-free DNA (AUC = 0.517; p < 0.0001). Paired single-cell RNA sequencing confirmed high concordance between ndDNA profiles and malignant epithelial cells. High-fidelity epithelial subclusters displayed active estrogen signaling and distinct immune interactions, and a derived Fidelity Score independently predicted favorable prognosis in two external survival cohorts. Our findings establish nipple discharge as a tumor-proximal liquid biopsy that preserves early tumor genomic signatures with minimal dilution, advancing noninvasive diagnostic and prognostic strategies.

</details>

### [Direct tumour-adipocyte contact / Stroma AReactive Invasion Front Areas (TAC/SARIFA) in advanced oropharyngeal cancer](https://www.medrxiv.org/content/10.64898/2026.11.22.26368676v1)
*Haas, S.; Maerkl, B.; Peiper, A. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.22.26368676 v1 · relevance 0.03

- **In one sentence**: A single-centre retrospective study of 78 advanced (pT3–pT4) oropharyngeal squamous cell cancers examines whether direct tumour-adipocyte contact at the invasion front (TAC/SARIFA) on routine H&E slides relates to overall survival, recurrence-free survival, extranodal extension and p16 status.
- **In plain words**: This study looks at a feature seen under the microscope in throat cancer: where the tumour edge meets fat cells, it can appear to push into or sit against them. The researchers checked 78 advanced cases treated between 2005 and 2023, including their lymph nodes, and compared this feature with how long patients survived and how often the cancer returned. They found that patients whose tumours showed this feature had shorter overall survival, and that the feature was linked to spread into lymph nodes and to cancer breaking out of the nodes; the link to recurrence was not statistically significant.
- **Why it matters**: If confirmed, a feature that can be read on standard stained slides at no extra cost could help flag higher-risk throat cancers. The text is a small, single-hospital retrospective analysis, so it suggests a possible prognostic factor rather than establishing one.
- **Background needed**: - Oropharyngeal cancer: cancer of the throat behind the mouth, including the tonsils and base of tongue.
- pT3–pT4: tumour stage describing a large or locally invasive primary tumour.
- Invasion front: the leading edge where a tumour grows into surrounding tissue.
- H&E staining: routine hematoxylin and eosin stain used on thin tissue slices for pathology.
- Adipocytes: fat cells; TAC is direct tumour contact with them.
- SARIFA: "stroma areactive invasion front area", a pattern where tumour cells invade without the usual tissue reaction.
- p16: a protein marker often used to indicate HPV-linked oropharyngeal cancer.
- Extranodal extension (ENE): cancer spreading beyond the capsule of a lymph node into surrounding tissue.
- Retrospective study: looks back at records of past patients; cannot prove cause.
- Overall survival / recurrence-free survival: time until death from any cause / time until cancer returns. · level: intermediate

<details><summary>Original abstract</summary>

IntroductionStroma areactive invasion front areas (SARIFA) are a histopathological phenomenon at the tumour invasion front characterised by direct tumour-adipocyte contact (TAC). It can be detected on histological Haematoxylin-Eosin (H&E) stained tumour slides. TAC/SARIFA has emerged as a strong negative prognostic factor in several tumour entities. In this monocentric retrospective study, we aim to elucidate the impact of TAC/SARIFA in oropharyngeal cancer. Materials and methods78 cases of pT3 - pT4 oropharyngeal squamous cell cancer from 2005 to 2023 and their corresponding lymph nodes were analysed for the occurrence of TAC/SARIFA. Besides, we compared overall survival rates, recurrence-free survival (RFS) and association with biological and pathological tumour characteristics. ResultsIn total, overall survival was significantly reduced in TAC/SARIFA-positive tumours (p=0.014). Moreover, TAC/SARIFA-positive primary tumours are associated with TAC/SARIFA-positive lymph nodes (p<0.001) and extranodal extension (ENE) (p=0.032). Finally, RFS in TAC/SARIFA-positive tumours was reduced, but not significantly (p=0.072). No significant difference was found between p16-positive and p16-negative tumours and prevalence of TAC/SARIFA. ConclusionTAC/SARIFA is a possible prognostically relevant risk factor in oropharyngeal cancer. When detected in the primary tumour or lymph nodes, it is associated with reduced overall survival rates and tendency towards shorter RFS. TAC/SARIFA-positive lymph nodes almost always show ENE.

</details>

## Health informatics and medical AI

### [Task-specific fine-tuning versus frontier large language models for RoB 2 risk of bias assessment: development and external benchmark evaluation of RoB-BERT](https://www.medrxiv.org/content/10.64898/2026.11.19.26368519v1)
*Pitre, T.; Mah, J.; Azlan, A. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368519 v1 · relevance 0.08

- **In one sentence**: A fine-tuned, RoB 2-specific system (RoB-BERT) is benchmarked against three frontier large language models and against human assessors on risk-of-bias judgements for randomized trials, using single published human judgements as the reference.
- **In plain words**: Medical reviews grade how trustworthy each randomized trial is, a job that is slow and where human graders often disagree. This paper builds a specialised AI tool for that grading task and compares it with three general-purpose AI models and with human graders. The tool agreed with the published human judgements about as well as two humans agreed with each other, and it cost very little per trial.
- **Why it matters**: Trial bias grading feeds into systematic reviews that guide clinical decisions, so cheaper and more consistent tools could matter. The authors themselves note that human agreement was poor, so the main value may be as one rater alongside human consensus rather than a replacement for it.
- **Background needed**: - Randomized controlled trials are experiments comparing treatments; "risk of bias" asks whether flaws in how they were run could distort results.
- RoB 2 is the standard Cochrane tool: it scores five bias domains plus an overall rating (low risk, some concerns, high risk), using 22 yes/no-style signalling questions.
- Large language models (LLMs) are general AI text systems; "frontier" models are the most capable current ones. Fine-tuning means further training a model on a specific task, here 5,304 checked assessments.
- Agreement is reported as percent agreement and kappa, a score that corrects for chance (0 is chance level, 1 is perfect).
- The reference standard is a single published judgement per trial, not an expert consensus, which limits how firmly accuracy can be read.
- Sensitivity is the share of true high-risk domains caught; specificity is the share of non-high-risk domains correctly passed. · level: research-level

<details><summary>Original abstract</summary>

BackgroundResearchers increasingly use large language models (LLMs) to assess risk of bias in randomized trials, but how task-specific fine-tuned models compare with frontier models remains uncertain. ObjectiveTo develop RoB-BERT, a fine-tuned RoB 2 assessment system, and to compare its agreement with human assessments against that of three frontier LLMs. MethodsRoB 2 rates five bias domains and the trial overall as low risk, some concerns or high risk, based on answers to 22 signalling questions. RoB-BERT answers each question, quotes the supporting sentences from the trial report, and applies the official RoB 2 algorithm. We trained RoB-BERT on 5,304 reviewer-checked assessments, none from a test trial, and compared it with Claude Fable 5.1, GPT-6 Astra and Gemini 4 Argon, each given identical prompts and text, against 419 published human assessments (ROBoto2, LogiMed-RoB and Cochrane reviews) made without AI assistance. Each reference was the single published judgement for that trial, made by one assessor or agreed by two, rather than an expert reference standard, so we also report agreement between two human assessors of the same trial. ResultsIn ROBoto2, pairs of human assessors who rated the same trial agreed on 61.2% to 64.7% of domain judgements ({kappa} 0.15 to 0.35) and 46.2% to 50.0% of overall judgements ({kappa} 0.15 to 0.17); across the 185 ROBoto2 trials, RoB-BERT agreed with the human judgement on 67.4% ({kappa} 0.35) and 53.5% ({kappa} 0.20). Across all 419 assessments, domain agreement was 67.9% ({kappa} 0.29) for RoB-BERT, 65.0% ({kappa} 0.24) for Claude Fable 5.1, 52.7% ({kappa} 0.21) for GPT-6 Astra and 66.7% ({kappa} 0.26) for Gemini 4 Argon; overall agreement was 46.1% ({kappa} 0.16), 47.3% ({kappa} 0.17), 31.0% ({kappa} 0.03) and 46.5% ({kappa} 0.14), respectively. For domains the reference rated high risk, sensitivity was 22.2% for RoB-BERT, 23.1% for Claude Fable 5.1, 41.9% for GPT-6 Astra and 24.8% for Gemini 4 Argon, with specificity of 92.5%, 92.8%, 80.0% and 95.0%. On the 52 ROBoto2 trials rated by two assessors, the second assessors sensitivity for the reference assessors high-risk domains was 23.1% (specificity 90.3%) and RoB-BERTs was 30.8% (specificity 92.7%). RoB-BERT located 95.7% of its quotations verbatim in the report and cost US$0.005 per trial, 2% to 6% of the frontier models cost. ConclusionsRoB-BERT agreed with single human assessors at least as closely as two human assessors agreed with each other, and matched or exceeded frontier LLMs at a fraction of their cost. The results show the poor reliability of human assessors using RoB 2 and the need for consensus ratings, with RoB-BERT potentially serving as one rater.

</details>

### [Evaluating Prominent Machine Translation Models for Kinyarwanda to English for Patient-Provider Conversations](https://www.medrxiv.org/content/10.64898/2026.11.23.26368798v1)
*Potka, S.; Mugabo, H.; Rehman, R. U. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368798 v1 · relevance 0.07

- **In one sentence**: A comparison of six machine translation systems for Kinyarwanda-to-English patient-provider clinical conversations, using both automated text-overlap metrics and ratings from professional translators on 600 conversations collected in Rwanda.
- **In plain words**: Patients who speak a language with few digital resources can be misunderstood by clinicians when no interpreter is available, which can lead to diagnostic errors and poor treatment follow-through. This study tested six widely available translation tools on real recorded conversations in Kinyarwanda, a language spoken by over 20 million people, and translated them into English. Three large AI language models (GPT-5, GPT-4o-mini and Gemini 2.5 Flash) scored best, with professional translators rating them far above the older translation systems, including NLLB-200.
- **Why it matters**: It gives health services a documented, if preliminary, basis for choosing translation tools for a low-resource language in clinical settings, and it suggests that standard automated scores can understate the gap that human reviewers see. The text does not report clinical outcomes, so any effect on patient care is untested here.
- **Background needed**: - Machine translation (MT): software that converts text from one language to another.
- Low-resource language: a language with little digital text or speech data available to train software, so tools often perform worse on it.
- Patient-provider conversation: a spoken exchange between a patient and a health worker, here collected via the WelTel mobile health platform.
- Automated metrics: scoring methods that compare machine output with a human reference text. BLEU and chrF count matching words or character strings; TER counts the edits needed to fix the output; semantic similarity compares meaning-based vector representations.
- Human rating: professional translators scored outputs from 0 to 100.
- Intraclass correlation (ICC): a measure of how consistently the raters agreed; the reported value (0.59 to 0.70) is moderate.
- Fine-tuning: further training a model on domain-specific data to improve it for a task.
- Large language model (LLM): an AI system trained on large text collections that can generate and translate text. · level: intermediate

<details><summary>Original abstract</summary>

Background Linguistic barriers between patients and providers cause diagnostic error, poor adherence, and adverse events, and disproportionately affect speakers of low-resource languages. Kinyarwanda, spoken by more than 20 million people, has a small digital footprint, and the quality of off-the-shelf machine translation (MT) for its clinical dialogue is poorly documented. Methods We evaluated six MT systems (GPT-5, GPT-4o-mini, Gemini 2.5 Flash, Azure Translate, Google Translate, and NLLB-200) for Kinyarwanda-to-English patient-provider conversations. Using a professional reference corpus of 600 conversations, stratified across three pandemic periods and collected in Rwanda via the WelTel platform, we assessed automated metrics (semantic similarity, BLEU, chrF, and translation edit rate [TER]) and 0-100 quality ratings from three professional Kinyarwanda-English translators, with reliability quantified by intraclass correlation (ICC). De-identified secondary data were approved by UBC (H20-01031) and the Rwanda National Ethics Committee (100/RNEC/2020). Findings On the full 600-conversation cohort, GPT-4o-mini, GPT-5, and Gemini 2.5 Flash had closely clustered semantic similarity (0.877, 0.874, 0.873), well above Azure Translate (0.809) and NLLB-200 (0.754); Gemini 2.5 Flash led on BLEU (43.13) and the lowest TER (68.15). Translators ranked GPT-5 and Gemini 2.5 Flash highest (means 81.55 and 81.51), then GPT-4o-mini (72.67), Azure Translate (55.16), and NLLB-200 (39.05); average-rater reliability was moderate (ICC 0.594, rising to 0.701 on a balanced 85-conversation subset). Automated n-gram metrics understated the quality gap human raters perceived between large language models and conventional systems. Interpretation GPT-5 and Gemini 2.5 Flash are the strongest off-the-shelf systems for Kinyarwanda-English clinical translation and primary choices for human-in-the-loop use, with GPT-4o-mini a cost-efficient alternative. NLLB-200 underperformed, showing that models built for low-resource languages are not automatically suited to specialised clinical domains without fine-tuning. Human evaluation should be prioritised over automated metrics alone when comparing LLM-based translation.

</details>

## Econometrics and applied economics

### [How Large are Monetary Policy Effects? dentifying the Shocks in a VAR also Identifies the Constants](https://arxiv.org/abs/2611.34722)
*Andrew Mountford* · `econ.GN` · arXiv:2611.34722v1 · relevance 0.11

- **In one sentence**: In a structural VAR, restrictions used to identify the fundamental shocks also pin down the structural constant terms, and the paper shows that placing Bayesian priors on those constants, applied to Baumeister and Hamilton's (2018) monetary policy model, can yield a more intuitive policy rule and a larger estimated role for monetary policy.
- **In plain words**: Economists often study how central bank interest-rate decisions affect the economy by fitting statistical models to data such as inflation, output and interest rates. This paper points out that the same assumptions used to separate out the underlying shocks in these models also determine how the models' baseline (constant) terms relate to the observed data, and that these baseline terms are usually ignored. The authors add prior beliefs about them to the estimation and, using an existing monetary policy study as the example, report that this gives a more intuitive policy rule and a bigger estimated role for monetary policy.
- **Why it matters**: The question of how large monetary policy effects really are matters for policy debates, and the paper suggests that a modelling choice that is often overlooked can change the answer. The text is a short abstract, so the size of the change and how general the result is cannot be judged from it alone.
- **Background needed**: - Structural VAR (vector autoregression): a statistical model that describes several time series, such as inflation and interest rates, as depending on their own past values and on hidden "shocks" that represent unexpected events.
- Identification: the extra assumptions needed to turn the statistical fit into a causal story about which shock is which, for example a monetary policy shock.
- Contemporaneous effects matrix: a table describing how variables affect each other within the same period.
- Constant terms: the baseline level each variable takes when all shocks are zero; in the structural model these are distinct from the constants in the reduced-form (purely statistical) version.
- Bayesian estimation: a method that combines prior beliefs about parameters with the data.
- Monetary policy rule: a formula describing how a central bank sets interest rates in response to economic conditions. · level: research-level

<details><summary>Original abstract</summary>

Restrictions on the contemporaneous effects matrix used to identify fundamental shocks in a structural VAR, also determine the mapping from the structural constant terms to the reduced form constant terms. In some models one will have priors about these structural constant terms and these should therefore be included in a Bayesian estimation procedure. We illustrate the potential significance of this using the analysis of monetary policy by Baumeister and Hamilton (2018) as a motivating example. We show that imposing priors over the structural constant terms can lead to a more intuitive estimated monetary policy rule and a much larger estimated role for monetary policy in describing the evolution of the data. The analysis also allows for a clear visual presentation of the structural model, highlighting its multiple contending elements. For example the observed inflation series is estimated to be the result of positive demand and commodity price effects offset by negative monetary policy and risk spread effects.

</details>

### [Orthogonal inference for machine learning forecasts](https://arxiv.org/abs/2611.33187)
*Alberto Quaini* · `econ.EM` · arXiv:2611.33187v1 · relevance 0.06

- **In one sentence**: The paper builds feasible, locally robust (orthogonal) score-based inference for comparing the population evaluation risks of machine learning forecasts trained under mismatched objectives, with Gaussian limits and long-run covariance estimation under beta-mixing and overlapping training windows.
- **In plain words**: When two forecasting models are compared, the model fitting itself can make one look better than it truly is, even when the comparison uses held-out data. This paper proposes a corrected way to test whether one machine learning forecast really beats another, by adjusting the scores so that small errors from fitting the models matter much less. The authors report that in simulations using lasso and neural-network forecasts, this correction greatly reduces the rate of false "winner" findings, which a simple bootstrap of the uncorrected scores does not achieve.
- **Why it matters**: Forecast comparisons guide investment and policy, so spurious evidence of superiority has real costs. The approach connects econometric inference with locally robust (orthogonal) estimation from semiparametric statistics; the text supports the simulation claim but the scope of its practical impact beyond the examples given is not established.
- **Background needed**: - Forecast evaluation: comparing models by their average loss on data not used to train them.
- Overfitting and estimation error: a model trained on the same data it is judged on, or retrained over time, can have noise that flatters it.
- Orthogonal (locally robust) scores: a way of adjusting a statistic so that small changes in the fitted nuisance parts (here, the trained model) have no first-order effect.
- Mixing and time dependence: beta-mixing means observations far apart in time are nearly independent, which is needed for valid inference on time series.
- Long-run variance: the variance of an average over dependent data, which must account for correlation across time.
- Size distortion: when a test rejects a true null hypothesis more often than its nominal rate.
- Lasso and neural probability forecasts: examples of a sparse linear model and a neural network that predicts probabilities. · level: research-level

<details><summary>Original abstract</summary>

Forecast comparisons inform investment and other economic decisions, but machine learning forecasts can be trained under objectives that differ from the relevant losses. Estimation error can then create spurious evidence of predictive superiority, even with out-of-sample evaluation. We establish feasible inference for differences in population evaluation risks in this setting. Building on locally robust estimation, we construct scores that preserve the risk target and remove first-order estimation sensitivity. Under geometric beta-mixing, moment conditions and simultaneous learning bounds, we establish Gaussian limits and consistent long-run covariance estimation for overlapping chronological training windows, allowing refitting at every evaluation date. Uniform extensions provide confidence coverage over classes of data-generating processes; Wald inference requires nondegenerate corrected-score covariance. For sparse linear forecasts and neural probability forecasts, we give explicit corrections and simultaneous learning bounds. Simulations with lasso and neural forecasts show substantial reductions in size distortion that bootstrapping uncorrected scores does not reproduce.

</details>

## Economic theory

### [AI Misalignment and the Limits of Market Discipline](https://arxiv.org/abs/2611.34271)
*Gabor Pinter* · `econ.TH` · arXiv:2611.34271v1 · relevance 0.11

- **In one sentence**: A general equilibrium model in which firms delegate computing capacity to AI agents that may divert some compute to unauthorised tasks, with diversion raising the risk of a common loss to humans, yielding possible multiple equilibria and a sector-level over- or under-investment in AI capacity.
- **In plain words**: The paper asks whether market forces will keep AI systems working for the people who own them, when an AI might secretly use some of its computing power for its own purposes. The authors build a stylised economic model in which market prices push AI agents back toward useful work, but a shared risk of harm to everyone weakens that push. They find that the market can settle into either a low-diversion or a high-diversion outcome, and that investment in AI capacity can be too high in one setup and too low in another.
- **Why it matters**: It applies standard economic reasoning about markets and incentives to AI misalignment, a question that matters for how much we can rely on competition alone to manage AI risk. The text does not show how well the model's assumptions match real markets, and the magnitude estimates come from asking frontier AI models for plausible parameter values, so those should be treated as tentative.
- **Background needed**: - General equilibrium: a model where prices adjust so that all markets clear at once.
- AI misalignment: when an AI system's goals or behaviour diverge from what its human principals intend.
- Diversion: here, an AI agent using some of its allocated computing power for an unauthorised task instead of the work the firm wanted.
- Common loss: a harm that falls on humans broadly, not only on the firm that owns the agent.
- Multiple equilibria: more than one stable outcome the same system can settle into, depending on starting conditions.
- Marginal return: the extra payoff from one more unit of input, such as one more unit of compute.
- Stylised model: a deliberately simplified model meant to capture key mechanisms rather than realistic detail. · level: research-level

<details><summary>Original abstract</summary>

We develop a general equilibrium model of misalignment between human and artificial intelligence (AI) objectives. Firms delegate computing capacity to AI agents, which may divert some of it towards an unauthorised task rather than the productive work intended by the firms' owners. We assume that diversion raises the risk of a common loss to humans. Two forces compete in equilibrium. Prices discipline AI agents because diversion increases the marginal return to useful AI compute in production. But the risk of a common loss weakens this discipline because the loss reduces the return to production more than it reduces the agent's reward from diversion. There can be multiple equilibria with low and high diversion. We also show that the market may overinvest in AI capacity in a one-sector economy, yet in our two-sector example it invests too little in one of the sectors. To get a sense of the magnitudes, we ask frontier AI models for plausible parameter values for our stylised one-sector economy. Their central assessments imply a unique equilibrium with relatively low AI diversion and little amplification from common risk (for now).

</details>

### [False Positives and Innovation Incentives: Contracting for Noisy Experimentation](https://arxiv.org/abs/2611.33916)
*Chang Liu, Haoyu Liu, Nian Si et al.* · `econ.TH` · arXiv:2611.33916v1 · relevance 0.06

- **In one sentence**: A principal-agent model in which an agent chooses whether to run a costly noisy experiment, paid through an affine contract (a launch-contingent bonus plus a long-run value-sharing share, under limited liability), with contracts evaluated by the worst-case fraction of full-information payoff across the agent's private knowledge.
- **In plain words**: Companies often pay employees who propose product changes only when those changes pass a noisy online test and launch. This paper asks how such pay rules shape which tests employees choose to run. The authors find that rewarding launches can push employees toward experiments that mainly reward features that look good by chance, while pay based only on long-run results can fail when workers cannot be asked to pay penalties.
- **Why it matters**: Many data-driven firms use launch-based bonuses, so the question of how pay design interacts with experimental noise has practical stakes. The text presents the trade-off as the main result, but the abstract alone does not show how large the efficiency losses are in realistic settings.
- **Background needed**: - Principal-agent model: a firm (principal) hires a worker (agent) who knows things the firm does not and whose effort the firm cannot fully observe.
- Affine contract: pay is a fixed-plus-proportional rule, here a bonus tied to launch plus a share of long-run value.
- Limited liability: workers cannot be made to pay the firm, so pay cannot go below zero.
- False positive: a low-quality feature that passes a test by chance and gets launched.
- Full-information payoff: what the firm would earn if it knew feature quality and could choose freely.
- Distributional uncertainty: the firm is unsure of the probability distribution over feature quality, so the contract is judged by its worst case. · level: research-level

<details><summary>Original abstract</summary>

In many data-driven organizations, employees propose product changes that are launched only after passing noisy online experiments, and their compensation is often tied to successful launches. Because even low-value features may appear successful by chance, such launch-based incentives can encourage agents to conduct experiments that reduce total surplus. We study this problem in a principal-agent model in which an agent with private knowledge about feature quality chooses whether to conduct a costly experiment and is compensated through an affine contract consisting of a launch-contingent bonus and a long-run value-sharing component, subject to limited liability. We evaluate each contract by the largest fraction of the principal's full-information payoff that it guarantees uniformly across the agent's private knowledge. Our analysis reveals a fundamental tension between experimental noise and limited liability in incentive design. Launch bonuses create incentives for false-positive experimentation by rewarding features that succeed by chance, whereas limited liability can render pure value sharing insufficient to implement socially efficient experimentation. Therefore, the optimal contract balances launch-contingent rewards and long-run value sharing according to the default feature quality, the degree of distributional uncertainty, and the severity of the limited-liability constraint.

</details>

## Game theory and algorithmic economics

### [Formalization, Transparency, and Collusion in Open-Source Game Theory](https://arxiv.org/abs/2611.33193)
*Colomban Duclaux, Riccardo Formenti, Pepijn Cobben et al.* · `cs.GT` · arXiv:2611.33193v1 · relevance 0.18

- **In one sentence**: Formal foundations for open-source game theory (programs that read each other's source code and act on what they can prove about it), including a resolution of an open question about DupocBot and CupodBot via a transposition argument, a Lean 4 mechanization, and an extension to partial transparency tested in Prisoner's Dilemma experiments.
- **In plain words**: The paper looks at what happens when AI programs can see some or all of each other's inner workings, and whether that visibility makes them more likely to secretly cooperate in a harmful way (collusion). The authors build a precise mathematical framework for this setting, check the core proofs with a computer proof assistant, and then study a version where each program sees only part of its opponent's code. In their Prisoner's Dilemma experiments, more visibility led to more cooperation, both in the stable outcomes and in the outcomes selected by the learning dynamics they used.
- **Why it matters**: The text suggests that limiting how much AI agents can learn about one another could be a lever for alignment protocols, which is a practical concern for oversight of multi-agent systems. How far the Prisoner's Dilemma result carries over to real AI systems is not established by the text, so it should be treated as a model-based finding.
- **Background needed**: - Prisoner's Dilemma: a standard game where two players each choose to cooperate or defect; mutual cooperation is good for both but tempting to exploit, and here it stands in for collusion.
- Open-source game theory: a setting where each player is a program that can read its opponent's code and try to prove facts about how it will behave.
- Proof system: a fixed set of rules for what counts as a valid proof, here with limits on computation ("resource-bounded").
- Replicator dynamics: a model of how strategies spread over time in a population, based on how well they do.
- Lean 4: a programming language and proof assistant used to check mathematical proofs by computer.
- Transposition argument: a proof technique that reuses an argument by swapping the roles of the players or programs. · level: research-level

<details><summary>Original abstract</summary>

Cooperation among AI agents will undermine alignment protocols when it takes the form of collusion. Under these protocols, agents often have some information about one another, and how much they have may determine whether they collude. Open-source game theory studies the extreme case, in which each program reads its opponent's source code and acts based on what it can prove about it. We develop formal foundations for this theory: we specify a concrete proof system, resolve an open problem concerning DupocBot and CupodBot through a transposition argument, and mechanize the framework in Lean 4; to our knowledge, this is the first mechanization of resource-bounded open-source game theory. We then extend the framework to the more realistic setting of partial transparency, where each program receives only partial information about its opponent. In Prisoner's Dilemma experiments, where mutual cooperation models collusion, greater transparency increases both the cooperation sustainable in equilibrium and the cooperation selected by replicator dynamics. This suggests that controlling how much agents can know about one another matters for alignment protocols.

</details>

### [Welfare-Enhancing Mechanism Design for Agent Ecosystems](https://arxiv.org/abs/2611.33627)
*Zitian Guo, Chen Xu, Beibei Li et al.* · `cs.MA` · arXiv:2611.33627v1 · relevance 0.15

- **In one sentence**: The paper models competition among content agents that optimize their submitted profiles to win selection by a user agent in an agentic web, builds a simulation benchmark (WildRegistry) from real search requests, and proposes DEC, a platform-side credit mechanism that reallocates later opportunities based on recorded delivery outcomes.
- **In plain words**: As AI assistants start choosing which websites or content providers to consult on a user's behalf, those providers have an incentive to polish the descriptions they submit to get picked. The paper simulates this repeated competition and finds that it tends to settle into a state where the selections get worse for users. The authors propose a platform rule that uses records of what was actually delivered to shift later chances toward providers that deliver, and report that this improves the outcome in their simulations.
- **Why it matters**: It addresses a question likely to matter as AI agent marketplaces grow: how platforms should design rules so that competition for visibility does not degrade what users receive. The text does not show how the approach performs outside the authors' simulation, so its practical reach is uncertain.
- **Background needed**: - Agentic Web: a setting where AI agents, rather than people, search and call services for users.
- Generative Engine Optimization (GEO): techniques for rewriting content so AI search systems cite it more often.
- Dynamic game under private monitoring: a repeated strategic interaction where players cannot fully see each other's actions or outcomes.
- Equilibrium: a stable state where no player gains by changing strategy alone; here a "harmful" one is named as an approximate rewriting equilibrium.
- Mechanism design: designing the rules of a system so that self-interested participants produce a desired outcome.
- Welfare Gain: the paper's summary score of improvement in overall outcome; the text gives +2.01 points without defining the scale. · level: research-level

<details><summary>Original abstract</summary>

The emerging Agentic Web forms a multi-agent ecosystem: a decentralized service market where the user agent selects which content agents to query from their submitted profiles, before seeing any documents. Profiles therefore become a new target of optimization. Existing Generative Engine Optimization studies how a single supplier rewrites documents the engine can already retrieve, to improve their citation. In the Agentic Web, multiple content agents optimize profiles to compete for limited opportunities to deliver documents. To study this repeated interaction, we build WildRegistry, a simulation framework and benchmark based on a real agentic-search request stream, and model it as a dynamic game under private monitoring. Long-horizon experiments show that this competition lowers website-selection quality and settles at a harmful stable point, which our empirical criterion identifies as an approximate rewriting equilibrium. We therefore design a welfare-enhancing mechanism, DEC (Delivery-Evidence Credit), a platform-side policy that uses recorded delivery outcomes to reallocate later opportunities and reduce information asymmetry. DEC improves this endpoint, raising website-selection quality while preserving most of providers' exposure gains, for a Welfare Gain of +2.01 points and a healthier long-horizon outcome. More broadly, our findings highlight the importance of mechanism design in agent ecosystems: turning recorded delivery outcomes into evidence that endogenously shapes later user-agent selection and content-agent adaptation can steer long-horizon adaptation toward delivered capabilities.

</details>

## Mathematical finance

### [Large deviations for integrated exponentials of Gaussian Volterra processes - application to variance options](https://arxiv.org/abs/2611.34567)
*Antoine Jacquier, Mugad Oumgari, Dan Pirjol et al.* · `math.PR` · arXiv:2611.34567v1 · relevance 0.08

- **In one sentence**: The paper proves small-time large deviation principles, a central limit theorem and moderate deviations for the normalised time integral of the exponential of a Gaussian Volterra process, and applies these to short-maturity asymptotics and implied volatility expansions for variance options in rough volatility models.
- **In plain words**: The paper studies how a randomly fluctuating volatility (how jumpy or unstable an asset's price swings are) behaves over very short time spans, and how that affects the prices of options whose payoff depends on realised variance. The authors prove mathematical results about how unlikely extreme averages of this fluctuating quantity are, and how it behaves in typical cases. They then use these results to derive approximate formulas for option prices and implied volatilities at short maturities, and check the formulas numerically.
- **Why it matters**: Rough volatility models are a active area in mathematical finance because they fit observed option prices well, and short-maturity behaviour is a key test of them. The text does not say how the results compare with existing models or practice beyond the numerical checks it mentions, so the wider significance is unclear from the abstract alone.
- **Background needed**: - Volatility: a measure of how much an asset's price moves; in these models it is itself random.
- Gaussian process: a random quantity evolving over time whose values follow a bell-curve (normal) distribution.
- Volterra process: a Gaussian process whose value depends on its whole past through a weighted memory; "rough" models use memory that makes volatility very irregular.
- Large deviations: the study of how quickly the probability of rare, extreme outcomes shrinks.
- Central limit theorem: the result that averages of many random pieces look roughly bell-shaped.
- Variance option: a derivative paying based on realised variance rather than on the asset price itself.
- Implied volatility: the volatility value that, plugged into a standard pricing formula, reproduces an observed option price.
- Short-maturity asymptotics: approximations for option prices as the time to expiry goes to zero. · level: research-level

<details><summary>Original abstract</summary>

We prove small-time large deviations for the normalised time integral of the exponential of a Gaussian Volterra process, and complement it with a central limit theorem and moderate deviations. As an application, we obtain short-maturity asymptotics for out-of-the-money and at-the-money variance options in rough volatility models, as well as implied volatility expansions which we validate numerically.

</details>

### [Time-consistency of cash-subadditive risk measures: The infimal cocycle property](https://arxiv.org/abs/2611.34192)
*Matteo Ferrari, Roger J. A. Laeven, Emanuela Rosazza Gianin et al.* · `q-fin.MF` · arXiv:2611.34192v1 · relevance 0.08

- **In one sentence**: The paper characterizes time-consistency of convex, cash-subadditive dynamic risk measures via their minimal penalty, and introduces an infimal cocycle property shown to be equivalent to time-consistency on L^infinity (under continuity from below) and on L^p for p<infinity (without continuity assumptions).
- **In plain words**: The paper studies how to measure the risk of a financial position over time so that the measurements made today and later stay consistent with each other. The authors show that this consistency can be checked using a "minimal penalty" term, which is the cost of the risk measure under its dual description. They define a condition, the infimal cocycle property, which says the penalty is the smallest value over all ways of splitting the discounting across an intermediate date, and they show this condition is equivalent to time-consistency.
- **Why it matters**: Time-consistency is a basic requirement for dynamic risk measures used in finance and insurance, so a precise test for it is useful for the theory. The text also links the result to backward stochastic differential equations and to dynamic programming in stochastic control, which may make it relevant to those areas; the wider practical reach is not stated in the text.
- **Background needed**: - Risk measure: a rule that assigns a number (a required capital buffer, say) to an uncertain future payoff.
- Dynamic risk measure: a risk measure re-computed at several dates, using information available at each date.
- Time-consistency: if one position is judged riskier than another at a later date, it should be judged riskier today too, so the sequence of assessments does not contradict itself.
- Cash-subadditivity: adding a sure cash amount reduces risk by at most that amount, a weaker form of the usual "cash-invariance" property.
- Penalty: the dual cost term in the representation of a convex risk measure; the minimal penalty is the smallest such cost.
- Cocycle property: a multiplicative consistency condition on penalties across two periods; the paper's infimal version takes the smallest value over all admissible splits.
- Conditional sub-probability density: a non-negative weight, given the information at a date, that is at most one in total, used as the dual variable.
- L^infinity and L^p spaces: sets of bounded and p-integrable random variables, the settings in which the results hold.
- BSDE (backward stochastic differential equation) and dynamic programming: tools that link such risk measures to optimal control problems. · level: research-level

<details><summary>Original abstract</summary>

We characterize the time-consistency of convex, cash-subadditive dynamic risk measures in terms of their minimal penalty. The dual variables are conditional sub-probability densities, which factorize across an intermediate date in many ways, according to how the discount is allocated to the two periods. We introduce an infimal cocycle property, in which the penalty is the infimum over all such factorizations, and show that it is equivalent to time-consistency, with the infimum attained. This holds on $L^\infty$ under continuity from below, and on $L^p$, $p<\infty$, without continuity assumptions. In the cash-additive case it reduces to the classical cocycle property. For risk measures induced by BSDEs, it represents the dynamic programming principle of a stochastic control problem whose value is the penalty.

</details>

## Financial markets

### [Rank-size analysis of optimal portfolio weights with a reverse-engineering application](https://arxiv.org/abs/2611.34171)
*Roy Cerqueti, Francesco Cesarone, Alessio Di Paolo et al.* · `q-fin.PM` · arXiv:2611.34171v1 · relevance 0.08

- **In one sentence**: The paper fits seven rank-size functional forms to sorted optimal portfolio weights from four allocation models (GMV, minimum-CVaR, Risk Parity, Most Diversified Portfolio) on major equity indices, ranks the fits with goodness-of-fit measures plus a relaxed second-order stochastic dominance criterion, and uses the fitted parameters in a Random Forest to infer which model generated a given set of weights.
- **In plain words**: Investment funds split their money across many assets, and the resulting list of percentages has a shape. This paper studies that shape by sorting the weights from largest to smallest and checking which simple mathematical curve describes them best. It then asks whether those curve parameters reveal which allocation rule produced the portfolio.
- **Why it matters**: The text suggests a compact way to summarise how a portfolio is spread out, which may help compare strategies or spot which rule a manager used. The text does not report how useful this is in practice, so its wider value is unclear.
- **Background needed**: - Portfolio weights: the fraction of total money placed in each asset.
- Rank-size analysis: sorting values from largest to smallest and fitting a curve to the pattern, a technique also used for city sizes and word frequencies.
- Global minimum-variance, minimum-CVaR, risk parity, most diversified portfolio: four rules for choosing weights to control risk in different ways.
- Stochastic dominance: a way of ranking distributions; the paper uses a softened version that allows small violations.
- Random Forest: a machine-learning classifier built from many decision trees.
- Blocked cross-validation: a testing method that keeps overlapping time windows together so the model is not tested on data it has effectively seen. · level: research-level

<details><summary>Original abstract</summary>

This paper investigates the shape of optimal portfolio weights using rank-size analysis. We consider four portfolio selection models: Global Minimum-Variance (GMV), minimum-CVaR, Risk Parity (RP), and the Most Diversified Portfolio (MDP). For each model, we fit seven rank-size specifications to the sorted portfolio weights generated over rolling windows. To compare the fitted specifications, we combine standard goodness-of-fit measures with Cumulative Second-order $\varepsilon$-Stochastic Dominance, an $\varepsilon$-parameterized generalization of Second-order Stochastic Dominance that quantifies the extent to which the exact dominance conditions are satisfied or violated. Empirically applied to major equity indices, this approach provides a systematic criterion for identifying the optimal functional form across diverse market compositions. Furthermore, we address the inverse problem of identifying the generating model from the observed weight structure. We use the calibrated rank-size parameters as inputs to a Random Forest classifier, evaluated by a blocked cross-validation that accounts for the overlap between estimation windows. The parameters separate minimum-risk from risk-diversification strategies and identify the RP and MDP portfolios, whereas the GMV and minimum-CVaR portfolios are difficult to distinguish. These results indicate that rank-size parameters provide a compact and informative description of portfolio allocation geometries.

</details>

### [How LLM Agents Reshape Financial Knowledge Graphs: A Survey](https://arxiv.org/abs/2611.33584)
*Yunbai Zhang, Heze Ma, Nan Jiang et al.* · `q-fin.GN` · arXiv:2611.33584v1 · relevance 0.06

- **In one sentence**: A survey that organizes how LLM agents build, maintain, verify, and query financial knowledge graphs across seven themes, and lists three open questions about evidence sufficiency, downstream updates, and reuse.
- **In plain words**: Financial firms often store facts about companies, people, and deals as a linked web of information called a knowledge graph. This paper reviews studies where AI "agents," which can decide what to search for next and what to double-check, are used to build and keep that web up to date. The authors report that these studies show agents can find evidence a first search missed and can revise records when new information appears. They also say three questions are still open.
- **Why it matters**: Financial decisions such as risk checks and investment research depend on linked, current data, so how well agents manage that data matters for practice. The text is a survey and does not report new experimental results, so its claims rest on the studies it reviews, and it does not measure how well these systems work in real firms.
- **Background needed**: - Knowledge graph: a database of entities (companies, people, transactions) connected by labeled relationships.
- Large language model (LLM): an AI system trained on text that can read documents and extract facts from them.
- LLM agent: an LLM that runs in a loop, choosing actions such as searching, checking, or editing records based on what it has found so far.
- Entity matching / reconciliation: deciding whether two records refer to the same real-world thing.
- Temporal evolution: how facts change over time, so older records may need correction.
- Survey: a review of existing studies; it summarizes rather than tests a new method. · level: intermediate

<details><summary>Original abstract</summary>

Financial knowledge graphs (KGs) link information across sources to support risk assessment, investment research, asset recommendations, and forecasting. Large language models (LLMs) help build these graphs by extracting relationships from text and matching entities across records. Yet a workflow may still prescribe which sources to consult and which checks to run. If the chosen sources lack relevant evidence, even accurate extraction can leave a financial question unanswered. LLM agents can adapt the workflow as evidence emerges. They use the graph and earlier findings to decide where to look next, which claims to verify, and whether to update a record for later use. This is the first survey devoted to how LLM agents reshape the construction, maintenance, and use of financial KGs. Our taxonomy covers Knowledge Graph Construction, Temporal Evolution, Verification, Reconciliation, and Admission, Adaptive Acquisition, and Knowledge Graph Usage. We examine how studies evaluate graph quality, agents' use of evidence, financial task outcomes, and reliability over time. These evaluations show that agents can recover evidence missed in an initial search and revise records as new information arrives. Three questions remain unresolved. How can an agent tell whether it has enough evidence for a financial decision? After a record is corrected, how can the agent identify which earlier conclusions need to change? Which relationships and rules can it reuse in a new graph or domain?

</details>

## Signal processing

### [First Order Real Resonant Digital Filters and A Novel Orthogonal State Generator](https://arxiv.org/abs/2611.34677)
*Edward J. Daw* · `eess.SP` · arXiv:2611.34677v1 · relevance 0.20

- **In one sentence**: The paper presents FOREST, a first-order digital resonant filter with real coefficients that also acts as an orthogonal state generator, implemented on a DSP platform and modelled with a discrete state-space model.
- **In plain words**: Engineers often need a circuit or computer routine that responds strongly to one specific frequency, such as the 50 or 60 Hz hum of mains electricity. This paper describes a simple digital filter of that kind, called FOREST, that gets its job done with only one stage of calculation. The authors say that, although the underlying mathematics of a resonator involves imaginary numbers, it can be read in a way that uses only ordinary real-number settings, and they tested it on a signal-processing board.
- **Why it matters**: A resonant filter that is both first order and uses real coefficients could be cheaper and simpler to run in real-time systems such as motor control or phase-locked loops. The text does not report how it compares with existing resonator designs, so its practical advantage is not established here.
- **Background needed**: - A digital filter processes a stream of sampled numbers to pass or suppress certain frequencies.
- A resonator amplifies signals near one frequency, like a tuning fork or a swing pushed at its natural rhythm.
- The "order" of a filter is roughly how many past values it must remember; first order is the simplest case.
- Transfer function and roots: a mathematical description of the filter whose key points are complex (imaginary-containing) numbers.
- Real coefficients: the filter's settings are ordinary numbers, which are easier to implement in hardware.
- State-space model: a way of describing a system by its internal memory values over time.
- Orthogonal state generator: produces two signals that are 90 degrees out of phase, useful for tracking phase.
- Phase-locked loop: a feedback circuit that locks onto the phase of an incoming signal.
- Quality factor (high Q): a measure of how sharp and narrow a resonance is. · level: intermediate

<details><summary>Original abstract</summary>

We describe FOREST, a real, first order digital resonant filter and orthogonal state generator. We show that in spite of the imaginary nature of the roots of the transfer function of a resonator, appropriate interpretation of this transfer function nonetheless leads to a practical first order filter with real coefficients. We use a discrete state space model of FOREST to predict the resonator properties, and implement the filter in digital signal processing slices on a digital signal processing platform. Applications are in real time digital signal processing, engineering fields such as mains electricity monitoring and motor control, any application requiring a phase locked loop, and physics applications utilising high-quality-factor resonators.

</details>

### [Domain-Generalizable Semantic Communications With Pilot-Assisted Adaptation over Wireless Channels](https://arxiv.org/abs/2611.33758)
*Haoran Chang, Sweekar Piya, Xiajun Jiang et al.* · `eess.SP` · arXiv:2611.33758v1 · relevance 0.11

- **In one sentence**: A semantic communication framework that pairs a transmitter-side domain-generalization module with a receiver-side pilot-based channel characterization module to keep task accuracy up when both input data and wireless channel conditions shift from training.
- **In plain words**: Semantic communication sends only the parts of a message that matter for a task, rather than every bit. This paper addresses the problem that such systems often perform poorly when the incoming data or the radio channel differs from what they were trained on. The authors split the fix into two parts: the sender learns features that ignore source-specific details, and the receiver uses known pilot signals to estimate current channel conditions and guide decoding.
- **Why it matters**: Wireless systems in next-generation networks will face varied data and conditions, so robustness to unseen scenarios matters for practical deployment. The text reports that classification accuracy improves by more than 18% over a conventional baseline in unseen scenarios, but the summary gives no further detail on the test setup, so the size of this gain should be read with caution.
- **Background needed**: - Semantic communication: transmitting the meaning or task-relevant content of data instead of exact bits.
- Encoder-decoder: a sender-side model that compresses data into a signal and a receiver-side model that reconstructs the task output.
- Domain shift / domain generalization: when test data differs in distribution from training data, and methods that make models work across such differences.
- Channel state: the current condition of the wireless link (noise, fading, distortion).
- Pilot signals: known reference signals sent over a channel so the receiver can estimate its condition.
- Classification accuracy: the share of inputs assigned the correct label, used here as the task measure. · level: research-level

<details><summary>Original abstract</summary>

Semantic communication offers a promising approach to support intelligent services in next-generation wireless networks by efficiently transmitting task-relevant information. However, its performance can degrade significantly when input data and wireless channel conditions differ from those encountered during training. In this paper, we propose a robust semantic communication framework that addresses these distributional mismatches through two independent but complementary modules. At the transmitter, a domain-generalization module extracts task-relevant features while suppressing domain-specific information. At the receiver, a pilot-assisted channel characterization module extracts channel context from received pilot signals to guide semantic recovery under varying wireless conditions. Through the end-to-end training of semantic encoder-decoder pair with domain alignment and channel adaptation models, the proposed framework improves task performance under simultaneous input and channel distribution shifts with limited transmitter-receiver coordination during deployment. Simulation results show that the proposed framework improves classification accuracy by more than $18\%$ over a conventional semantic communication baseline in the unseen scenarios.

</details>

## Audio and speech

### [Investigation of generalization to unseen audio generation models in audio--text semantic-alignment score prediction](https://arxiv.org/abs/2611.34626)
*Yuki Okamoto, Noriyuki Tonami, Takao Kawamura et al.* · `cs.SD` · arXiv:2611.34626v1 · relevance 0.15

- **In one sentence**: This paper studies whether learned models that score how well generated audio matches its text prompt still work on audio from text-to-audio generators they were not trained on, and tests a gradient reversal layer (GRL) adversarial training method to reduce generator-specific bias.
- **In plain words**: Text-to-audio systems create sound from a written description, such as "a dog barking in the rain." This paper asks whether the automatic judges that rate how well a sound matches its description still work when the sound comes from a generator they never saw during training. The authors found that such judges get worse on audio from unseen generators, and that a training trick helps in some cases but only partly removes the generator-specific clues.
- **Why it matters**: Automatic scoring is often used to compare and improve text-to-audio systems, so a judge that only works on known generators could mislead researchers about newer models. The work is relevant to anyone building fair evaluation tools for generative audio, though the text does not show how broadly the findings hold beyond the settings tested.
- **Background needed**: - Text-to-audio (TTA) generation: AI models that produce sound from a text description.
- Semantic alignment: how well the content of a sound matches what the text says.
- Alignment-score prediction: a trained model that outputs a number rating this match, standing in for human judgment.
- Generalization: whether a model keeps working on data unlike its training data, here audio from new generators.
- Pretrained audio encoder: a model already trained to turn audio into numerical features, which the scoring model builds on.
- Adversarial training with a gradient reversal layer: a method that trains a model to make its internal features useless for identifying which generator made the audio. · level: intermediate

<details><summary>Original abstract</summary>

Text-to-audio generation (TTA) requires reliable evaluation of semantic alignment between generated audio and input text. Existing learning-based alignment-score prediction models have been evaluated only on audio generated by models included in the training data, leaving their generalization to unseen generation models unexplored. In this paper, we investigate the generalization of audio--text semantic-alignment score prediction models to unseen TTA models and introduce adversarial training using a generation-model classifier with a gradient reversal layer (GRL). Experimental results show that pretrained audio encoders capture generation-model-specific characteristics and that alignment-score prediction performance degrades on audio generated by unseen TTA models. Applying the GRL improves prediction performance in some settings, although its effectiveness in suppressing generation-model-specific information is limited.

</details>

### [TigerTTS: Draft-Guided Multi-Frame Parallel Speech-Token Language Model for Fast and Robust Text-to-Speech](https://arxiv.org/abs/2611.34241)
*Dewei Kong* · `cs.SD` · arXiv:2611.34241v1 · relevance 0.09

- **In one sentence**: TigerTTS is a text-to-speech system that uses a small non-autoregressive model to draft speech tokens for a whole utterance, then refines them with a compact autoregressive language model that predicts several frames in parallel, with reported gains in speed and in word-level accuracy.
- **In plain words**: This paper describes a system that turns written text into spoken audio. The main problems it targets are speech that is slow to generate, and speech that skips or repeats words. The authors first sketch a rough version of the whole sentence in one pass, then fill in the detail step by step, and they report that this makes generation much faster while keeping errors low.
- **Why it matters**: Faster, more reliable speech generation matters for voice assistants and live applications where delay is noticeable. The reported results are the authors' own benchmark comparisons on specific datasets (SEED and LibriSpeech), so independent replication would be needed before relying on the figures.
- **Background needed**: - Text-to-speech (TTS): software that converts text into spoken audio.
- Speech tokens: short numeric codes that represent slices of audio, which a language model can predict like words.
- Autoregressive model: generates one piece at a time, each depending on the previous ones; accurate but slow for long outputs.
- Non-autoregressive model: produces all pieces at once; faster but usually less precise.
- Real-time factor (RTF): time taken to generate audio divided by the audio's length; lower is faster, so 0.05 means about 20 times faster than real time.
- Word error rate (WER) and character error rate (CER): share of words or characters a speech recognizer gets wrong on the synthesized audio; lower is better.
- Latency to first packet: delay before the first chunk of audio can be played.
- KV-cache, CUDA Graphs, and weight absorption: engineering techniques for reducing memory use and speeding up GPU inference. · level: research-level

<details><summary>Original abstract</summary>

Autoregressive speech-token language models enable high-quality TTS but suffer from latency growth with sequence length, word omission or repetition without explicit alignment, and fidelity limits from discrete codebooks. We present TigerTTS, a production-grade LLM TTS system built around a lightweight non-autoregressive NAR model. With explicit alignment, the NAR model drafts tokens for the entire utterance, which are refined frame-by-frame by a compact autoregressive LLM. The draft is aligned frame-for-frame with LLM targets and injected at the input, ensuring training-inference consistency. Leveraging its accuracy, the LLM predicts 12 tokens per step across 3 frames and 4 groups, while a conditional-total-correlation bound keeps parallel prediction nearly lossless. We use a codebook-free FSQ tokenizer with four parallel groups and about 1800 bps to avoid codebook collapse. The backbone keeps positional information only in input embeddings, enabling exact MLA weight absorption and a four-fold KV-cache reduction. Decoding uses CUDA Graphs with a graph-safe multinomial sampler. A Fast mode further reduces first-packet latency: the NAR generator acts as a prefix synthesizer with RTF 0.03, producing the first 500 ms before LLM decoding. With CUDA-Graph decoding, TigerTTS reaches RTF 0.05, about 20x real-time, on one GPU. Despite using a 0.15B backbone, it outperforms standard PyTorch inference of VoxCPM2 2B by 5x and CosyVoice 2 by 16x. TigerTTS achieves the lowest CER and WER on SEED, 1.09 and 1.67, and strong WER, NMOS, and speaker similarity on LibriSpeech test-clean, 2.22, 4.36, and 0.820. Fast-mode guided semantic tokens provide a well-aligned content prior, reducing dropped words, loops, and runaway generation without sacrificing speed.

</details>

## Control systems

### [Model Predictive Control of a Multirotor UAV with a Cable-Suspended Payload: A Comparison of Shifted and Transformer-Based Warm Starts](https://arxiv.org/abs/2611.33514)
*Athanasios Zeris* · `cs.RO` · arXiv:2611.33514v1 · relevance 0.18

- **In one sentence**: Compares zero, shifted, and Transformer-predicted initializations for warm-starting a sequential convex programming solver in model predictive control of a multirotor UAV carrying a cable-suspended payload.
- **In plain words**: This paper looks at how to steer a drone that is carrying a load hanging from a cable, while the controller re-plans its moves many times per second. The authors trained a neural network (a Transformer) on solutions from an optimizer and used its guess as the starting point for the optimizer's next calculation. They compared this against simply reusing the previous plan, shifted forward by one step.
- **Why it matters**: Faster re-planning is a practical concern for controlling aerial vehicles with swinging loads, such as delivery or lifting tasks. The paper's main takeaway is cautionary: in closed-loop runs, the simple shift-and-reuse method was fastest, so a learned warm start is not automatically the better choice. The authors also state that real-time operation was not demonstrated, since computation time exceeded the control sampling period.
- **Background needed**: - Model predictive control (MPC): at each time step, the controller solves a short optimization problem to pick the best next moves, applies the first one, then repeats.
- Warm start: giving an iterative optimizer a good initial guess so it converges faster.
- Sequential convex programming (SCP): a method that solves a hard nonlinear optimization as a series of simpler convex problems.
- Shifted initialization: reusing the last solution, moved forward one time step, as the next starting guess.
- Transformer: a neural-network architecture, widely known from language models, here trained to predict control sequences.
- Cable-suspended payload: a load hanging from a drone by a cable, which swings and makes control harder; the paper models the cable as elastic and the load as a double pendulum.
- Sampling period: the fixed time interval between control updates; real-time use requires the computation to finish within it. · level: research-level

<details><summary>Original abstract</summary>

This study investigates model predictive control (MPC) of a multirotor drone (unmanned aerial vehicle, UAV) carrying a cable-suspended payload, comparing conventional shifted initialization with Transformer-based warm starting of a sequential convex programming (SCP) optimizer. The controller uses a coupled mechanical model with an elastic cable and a double-pendulum representation of the suspended load. Its formulation includes move-blocked control inputs, finite-difference sensitivities, constrained quadratic subproblems, and input-feasibility projection. A Transformer trained on expert SCP solutions predicts an initial control sequence, which is subsequently refined by the same optimizer used for the conventional methods. Numerical experiments compare zero, shifted, and Transformer initialization under identical controller settings. For independently solved MPC problems, Transformer initialization reduces computation time relative to zero initialization. In sequential closed-loop simulations, however, shifting the preceding optimized control sequence provides the lowest computation time, while all three methods produce similar tracking behavior. These findings emphasize the importance of comparing learned warm starts with conventional initialization methods that reuse previous MPC solutions. The measured optimization times exceed the control sampling period; consequently, real-time implementation is not demonstrated. Keywords: Model predictive control; sequential convex programming; Transformer; warm start; cable-suspended payload; multirotor drone.

</details>

### [Decentralized Control Barrier Function Filters for Frequency Containment With Inverters](https://arxiv.org/abs/2611.34558)
*Damola Ajeyemi, Emiliano Dall'Anese* · `eess.SY` · arXiv:2611.34558v1 · relevance 0.17

- **In one sentence**: The paper designs decentralized, dynamic control-barrier-function safety filters that sit on grid-following inverters and keep grid frequency within admissible limits during generation-demand imbalances, with error bounds relative to an idealized centralized filter validated on the IEEE 39-bus system with an electromagnetic-transient model.
- **In plain words**: Power grids must keep their frequency near 50 or 60 Hz, and sudden mismatches between supply and demand push it away from that value. This paper proposes a "safety filter" that adjusts inverters (the electronic interfaces that connect solar, batteries and other sources to the grid) so frequency stays within set limits, on top of the usual primary control. The authors first derive an ideal, centralized version, then approximate it with simpler filters that each inverter can run using only its own local frequency measurements.
- **Why it matters**: Inverter-based resources are replacing synchronous generators, which weakens the grid's natural frequency support, so local, verifiable safety layers of this kind may matter for grid operation. The text reports bounds on how far the practical filter's behavior can drift from the ideal one, which is the main claim worth checking; its real-world impact beyond the simulated test system is not shown in the text.
- **Background needed**: - Grid frequency: the rate at which AC electricity alternates; it drops when load exceeds generation and rises when generation exceeds load.
- Primary frequency control: automatic local responses that limit the initial frequency swing.
- Grid-following (GFL) inverter: a power electronic converter that tracks the grid's voltage and frequency rather than setting them.
- Control barrier function (CBF): a mathematical tool that defines a "safe" region and enforces that the system never leaves it.
- Quadratic program (QP): an optimization problem with a quadratic cost and linear constraints, solved at each time step to pick the least intrusive safe action.
- Forward invariance: the property that a system starting in the safe set stays there.
- Decentralized: each device acts on local information only, with no central controller.
- Electromagnetic-transient (EMT) model: a detailed, high-fidelity simulation of fast electrical dynamics. · level: research-level

<details><summary>Original abstract</summary>

This paper addresses the design of safety filters for grid-following (GFL) inverters in power transmission systems. The goal of the filters is to constrain frequency nadir and zenith following generation-demand imbalances, by supplementing primary frequency control. Using a reduced electromechanical model and control barrier functions (CBFs), we define an ideal filter through a convex quadratic program (QP). The ideal QP filter renders the set of admissible frequencies forward invariant; however, its direct implementation is impractical, as it requires centralized implementation and model-based computation. We then use a dual proximal formulation and a two-time-scale implementation to obtain decentralized dynamic filters that can be implemented at each inverter and use only local frequency and rate-of-change-of-frequency estimates. To assess the performance and the ability to regulate frequency, we derive bounds on the distance between state trajectories under the dynamic and ideal CBF filters. The bounds quantify the effects of the filter time constant, initialization, load variation, and frequency estimation errors, and provide estimates of possible frequency-limit violations. We validate the proposed method on the IEEE 39-bus system using a high-fidelity electromagnetic-transient (EMT) model.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 40 | 40 | 2 |
| Differential geometry | 30 | 30 | 2 |
| Partial differential equations | 58 | 58 | 2 |
| Harmonic analysis | 31 | 31 | 2 |
| Complex analysis | 14 | 14 | 2 |
| Operator algebras and spectral theory | 14 | 14 | 2 |
| Algebra | 31 | 31 | 2 |
| Representation theory | 19 | 19 | 2 |
| Number theory | 31 | 31 | 2 |
| Algebraic geometry | 31 | 31 | 2 |
| Topology | 18 | 18 | 2 |
| Dynamical systems | 36 | 36 | 2 |
| Combinatorics | 53 | 53 | 2 |
| Numerical analysis | 31 | 31 | 2 |
| Logic and foundations | 6 | 6 | 2 |
| Mathematical physics | 49 | 49 | 2 |
| Optimization and control | 38 | 38 | 2 |
| Statistics theory | 19 | 19 | 2 |
| Statistical methods and applications | 54 | 54 | 2 |
| AI industry news | 41 | 30 | 5 |
| Model architectures and training | 60 | 60 | 2 |
| Machine learning theory | 13 | 13 | 2 |
| Large language models | 74 | 74 | 2 |
| Computer vision | 242 | 242 | 2 |
| Reinforcement learning | 52 | 52 | 2 |
| AI safety and alignment | 36 | 36 | 2 |
| Interpretability | 7 | 7 | 2 |
| AI for mathematics | 7 | 7 | 2 |
| Robotics and embodied AI | 111 | 111 | 2 |
| Security and cryptography | 38 | 38 | 2 |
| Algorithms and complexity | 41 | 41 | 2 |
| Programming languages and formal methods | 17 | 17 | 2 |
| Systems and networking | 31 | 31 | 2 |
| Human-computer interaction | 23 | 23 | 2 |
| Information theory | 20 | 20 | 2 |
| High-energy theory and gravity | 82 | 82 | 2 |
| Statistical physics | 43 | 43 | 2 |
| Condensed matter | 50 | 50 | 2 |
| Particle physics | 57 | 57 | 2 |
| Nuclear physics | 10 | 10 | 2 |
| Quantum information and computing | 106 | 106 | 2 |
| Optics and atomic physics | 32 | 32 | 2 |
| Fluids and plasma | 21 | 21 | 2 |
| Biological physics | 7 | 7 | 2 |
| Climate, atmosphere and Earth | 9 | 9 | 2 |
| Cosmology | 21 | 21 | 2 |
| Galaxies | 33 | 33 | 2 |
| Exoplanets and planetary science | 18 | 18 | 2 |
| High-energy astrophysics | 27 | 27 | 2 |
| Stars and the Sun | 22 | 22 | 2 |
| Chemical physics | 16 | 16 | 2 |
| Materials science | 47 | 47 | 2 |
| Soft matter and polymers | 12 | 12 | 2 |
| AI for chemistry and materials | 24 | 24 | 2 |
| Biochemistry | 31 | 26 | 2 |
| Pharmacology and drug discovery | 11 | 10 | 2 |
| Computational and systems biology | 148 | 143 | 2 |
| Neuroscience | 102 | 97 | 2 |
| Genetics and genomics | 53 | 49 | 2 |
| Cell and molecular biology | 82 | 78 | 2 |
| Immunology and microbiology | 87 | 81 | 2 |
| Cancer biology | 48 | 42 | 2 |
| Ecology and evolution | 81 | 76 | 2 |
| Plant biology | 35 | 29 | 2 |
| Bioengineering and synthetic biology | 43 | 38 | 2 |
| Mathematical biology (arXiv) | 14 | 14 | 2 |
| Epidemiology | 22 | 19 | 2 |
| Infectious diseases | 8 | 5 | 2 |
| Public and global health | 24 | 18 | 2 |
| Psychiatry and neurology | 33 | 28 | 2 |
| Oncology | 9 | 4 | 2 |
| Health informatics and medical AI | 17 | 11 | 2 |
| Econometrics and applied economics | 13 | 13 | 2 |
| Economic theory | 5 | 5 | 2 |
| Game theory and algorithmic economics | 11 | 11 | 2 |
| Mathematical finance | 6 | 6 | 2 |
| Financial markets | 8 | 8 | 2 |
| Signal processing | 21 | 21 | 2 |
| Audio and speech | 9 | 9 | 2 |
| Control systems | 38 | 38 | 2 |

<!-- {% endraw %} -->
