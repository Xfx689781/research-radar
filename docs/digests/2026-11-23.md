# Research digest · 2026-11-23
<!-- {% raw %} -->

New papers posted from about 2026-11-22 to 2026-11-23 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Overview and recent progress on the classical Bernoulli free boundary problem](https://arxiv.org/abs/2611.26636)** (Partial differential equations): This is an overview article about a mathematical problem in which the shape of a region is itself unknown and must be found along with the physical quantity filling it. The text is a short summary and does not spell out specific results, so it gives only the general purpose: to survey the field and highlight recent advances.
- **[Autonomous quantum machine learning via Riemannian gradient-based optimization](https://arxiv.org/abs/2611.27815)** (Quantum information and computing): Most quantum machine learning today trains a model by repeatedly measuring a quantum circuit and then adjusting parameters on a normal computer, and that back-and-forth is a bottleneck. This paper proposes training the model so that the update steps happen inside the quantum system itself, with no measurements or classical feedback during training. The authors report theoretical convergence guarantees, an analysis of how circuit depth grows, and numerical simulations suggesting the approach can learn with shallow circuits and few training examples.
- **[Hidden Semi-Markov Models for Fully Functional Time Series](https://arxiv.org/abs/2611.26838)** (Statistical methods and applications): The paper studies data where each observation is an entire curve, such as a brain-wave recording, and where an unseen "state" (for example, a sleep stage) switches over time. The standard model assumes each state's duration fades away at a fixed rate, which can be too restrictive. The authors let the time spent in each state follow a more flexible duration distribution, such as a negative binomial, or leave it unspecified, and show how to fit this model with established algorithms. They apply it to overnight pediatric EEG recordings.

## Probability

### [Stochastic Differential Equations on the Simplex](https://arxiv.org/abs/2611.27309)
*Paolo Guasoni, Eberhard Mayerhofer* · `math.PR` · arXiv:2611.27309v1 · relevance 0.29

- **In one sentence**: The paper builds a class of simplex-valued diffusion processes as solutions to stochastic differential equations driven by antisymmetric Brownian motion, covering multivariate Jacobi processes and general simplex polynomial diffusions, and establishes weak solutions plus global strong existence and pathwise uniqueness from strictly positive starting points under a boundary non-attainment condition.
- **In plain words**: This paper studies random processes that move around inside a simplex, the set of possible splits of a whole into parts that are non-negative and sum to one, such as shares of a portfolio or proportions of a mixture. The authors write down a way to define such moving splits using random noise that is constrained to be antisymmetric across pairs of parts. They show that, starting from strictly positive shares, the process has a well-defined solution that stays uniquely determined and does not hit the edges of the simplex under a stated sufficient condition.
- **Why it matters**: Processes that live on the simplex appear in finance, population genetics and compositional data analysis, so a general and well-posed framework is useful for those models. The text does not say how the framework is applied, so its practical reach beyond the stated special cases is unclear from this abstract alone.
- **Background needed**: - Simplex: the set of non-negative numbers that add up to one, e.g. three shares of a pie summing to 100%.
- Stochastic differential equation: a rule for how a quantity changes over time, with a random noise term; solutions are random paths.
- Brownian motion: the standard model of continuous random jitter, as in pollen grains moving in water.
- Jacobi process: a known random process confined to an interval, here generalized to several shares at once.
- Weak vs. strong solution: a weak solution exists in some probabilistic sense; a strong solution is defined pathwise for a given noise source. Pathwise uniqueness means the path is determined by the noise.
- Boundary non-attainment: the process never reaches the edge where a share becomes exactly zero (or one), under the stated condition. · level: research-level

<details><summary>Original abstract</summary>

We propose a framework for simplex-valued diffusion processes, formulated as solutions to stochastic differential equations driven by antisymmetric Brownian motion. Our edge-wise representation includes the multivariate Jacobi processes and the general class of continuous simplex-valued polynomial diffusions. Also, it allows bounded, locally Lipschitz state-dependent drift rates and edge weights. We establish weak solutions, as well as global strong existence and pathwise uniqueness for strictly positive initial states under a sufficient boundary non-attainment condition.

</details>

### [Isolation in Random Graphs](https://arxiv.org/abs/2611.26781)
*Laurentiu Ploscaru* · `math.CO` · arXiv:2611.26781v1 · relevance 0.21

- **In one sentence**: The paper studies isolation and F-isolation numbers in the binomial random graph G(n,p), proving first-order asymptotics, two-point concentration for the ordinary isolation number, and a phase transition in the gap between domination and isolation numbers.
- **In plain words**: The paper looks at random networks where each pair of nodes is linked independently with some probability p. It asks how few "chosen" nodes are needed so that every other node is either chosen or next to a chosen node (the domination number), and how that changes when the leftover nodes are allowed to contain only a limited kind of structure, such as no edges (isolation). The authors give sharp estimates for these quantities and find a point where the two counts separate in a predictable way.
- **Why it matters**: The results pin down how a basic network-covering quantity behaves in random graphs, which is a standard model for large, irregular real-world networks. The text does not say what applications it may have beyond this theory, so the wider relevance is unclear from the abstract alone.
- **Background needed**: - A graph is a set of nodes (vertices) joined by links (edges).
- G(n,p) is the random graph on n nodes where each possible link appears independently with probability p.
- "With high probability" means the chance of the stated event tends to 1 as n grows.
- A dominating set is a set of nodes such that every other node is adjacent to one in the set; the domination number is the smallest such set's size.
- An isolated set is a set of nodes with no edges between chosen nodes; the isolation number is the largest such set that dominates the rest, in the usual definition. F-isolation generalises this by allowing the leftover nodes to induce a graph with no copy of a fixed forest F (a forest is a graph with no cycles).
- Two-point concentration means the quantity takes one of two adjacent integer values with high probability.
- Asymptotic notation (o(1), log n) describes behaviour as the number of nodes grows large. · level: research-level

<details><summary>Original abstract</summary>

We study isolation in the binomial random graph $G(n,p)$. When $p=o(1)$ and $np\to\infty$, allowing an $F$-free graph on the undominated vertices gives the same first-order asymptotics for every fixed forest $F$ as the domination number $\gamma(G)$ in $G(n,p)$. For the ordinary isolation number $\iota(G)$ ($F$ is an edge) we prove two-point concentration when $p$ is bounded away from $1$ and $np^2/(\log n)^3\to\infty$. We also identify a transition in the gap $\gamma(G)-\iota(G)$ when $\log(1/p)=o(\log n)$. This gap tends to infinity in probability when $p$ is well below $(\log\log n/\log n)^2$ and is at most one with high probability when $p$ is well above this scale. Finally, for every fixed graph $F$, we show that the classical minimum degree bound for domination is asymptotically sharp for $F$-isolation, even for regular host graphs.

</details>

## Differential geometry

### [Projectively Flat Spherically Symmetric Sprays of Constant Curvature](https://arxiv.org/abs/2611.27723)
*Yajing Gui, Benling Li* · `math.DG` · arXiv:2611.27723v1 · relevance 0.11

- **In one sentence**: The paper classifies projectively flat, spherically symmetric sprays of constant curvature by solving the equations that constant curvature imposes on the projective factor p(r,s), and shows that the spray cases from constant-flag-curvature Finsler metrics (K=0, -1, 1) fall within this classification.
- **In plain words**: The paper studies a family of geometric rules for how straight-line-like paths behave on curved, direction-dependent spaces (Finsler geometry). The authors work out the conditions that keep the curvature constant for these rules and solve them, sorting every possible case into four explicit families. They also check that the known examples with constant flag curvature of zero, negative, and positive values all appear among these four families.
- **Why it matters**: A complete classification is a clean, checkable result: it tells specialists exactly which spherically symmetric projectively flat sprays have constant curvature, and it confirms that the standard constant-flag-curvature examples are covered. The text does not describe applications beyond this geometric setting, so any wider connection is uncertain.
- **Background needed**: - Finsler metric: a way of measuring length in which the length depends on both position and direction, generalizing Riemannian geometry.
- Spray: a system of second-order equations describing geodesics (the natural 'straightest' paths) on a Finsler space.
- Projectively flat: the paths can be matched to straight lines in some coordinates, up to reparametrization; the projective factor p(r,s) measures this deviation.
- Spherically symmetric: the rules are unchanged under rotations about a point.
- Flag curvature K: a generalization of sectional curvature; constant K means the same value everywhere and in every direction. K=0 is flat, K=1 is like a sphere, K=-1 is like a hyperbolic plane.
- Classification: a complete list of all possible cases, here four explicit families of p(r,s). · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study projectively flat spherically symmetric sprays of constant curvature. We derive a system of equations that is equivalent to the constant-curvature condition for such sprays and solve it to obtain a complete classification of the projective factor \(p(r,s)\) into four explicit families. We further show that the sprays induced by projectively flat spherically symmetric Finsler metrics of constant flag curvature \(K=0\), \(K=-1\), and \(K=1\) are all special cases of our classification, thereby confirming that the sprays induced by these constant-flag-curvature Finsler metrics are fully contained in our framework.

</details>

### [A local symmetry forces positivity for projectively induced Kahler-Einstein metrics](https://arxiv.org/abs/2611.27345)
*Filippo Salis* · `math.DG` · arXiv:2611.27345v1 · relevance 0.10

- **In one sentence**: A projectively induced Kähler–Einstein metric is shown to have positive Einstein constant whenever it admits at least one nonzero local real-holomorphic Killing field, with no completeness or global group-action assumption, and the argument extends to a non-Einstein obstruction under uniformly negative Ricci curvature and to compact equivariant continuations.
- **In plain words**: The paper studies curved geometric shapes that sit inside a flat-style projective space in a way that respects a special kind of Kähler structure, and asks whether they must be "positively curved" in a certain sense. The authors show that if such a shape has even a local symmetry (a smooth flow that preserves the geometry in a neighbourhood, though not necessarily everywhere), then it must be positively curved. The proof works by extending this local symmetry to a global one on a continuation of the shape and then applying standard tools from analysis on curved spaces.
- **Why it matters**: The general question of whether Kähler–Einstein submanifolds of projective space must have positive curvature is open, and this gives a partial answer under a local symmetry hypothesis. The text does not indicate further applications beyond this setting, so its wider significance is best judged by specialists.
- **Background needed**: - Kähler manifold: a complex-geometric space with a compatible metric and symplectic form, the natural setting for complex curvature.
- Einstein metric: a metric whose Ricci curvature is a constant multiple of the metric; the constant's sign (positive, zero, negative) classifies the shape.
- Projective space and submanifolds: complex projective space is the standard model of a positively curved complex space; a submanifold inherits a metric from it.
- Killing field: an infinitesimal symmetry, a flow that preserves the metric; "real-holomorphic" means it also respects the complex structure.
- Moment map and Hamiltonian potential: a function attached to a symmetry that measures how it acts; here it is bounded.
- Maximum principle and Liouville theorem (Omori–Yau, Yau): analytic tools saying bounded solutions of certain equations on complete spaces must be constant, which rules out the sign cases.
- Calabi rigidity: a result saying local symmetries of such metrics extend to projective-type symmetries. · level: research-level

<details><summary>Original abstract</summary>

We prove that a projectively induced Kahler-Einstein metric has positive Einstein constant as soon as it admits one nonzero local real-holomorphic Killing field. Neither completeness nor a prescribed global group action is assumed. This gives a partial answer, under a local symmetry hypothesis, to the general positivity problem for Kahler-Einstein submanifolds of (finite-dimensional) projective space. The key observation is that, by Calabi rigidity, a local real-holomorphic Killing field is induced by a projective unitary vector field whose tangency propagates along any connected global Kahler immersion, without a simple-connectivity assumption. Applied to Hulin's complete continuation, this produces a global Killing field with a bounded Hamiltonian potential given by the ambient projective moment map. The resulting Laplace equation, the Omori--Yau maximum principle and Yau's Liouville theorem exclude both negative and zero Einstein curvature. We also prove a non-Einstein obstruction under uniformly negative Ricci curvature and obtain compact equivariant continuations.

</details>

## Partial differential equations

### [Overview and recent progress on the classical Bernoulli free boundary problem](https://arxiv.org/abs/2611.26636)
*Xavier Fern\'andez-Real* · `math.AP` · arXiv:2611.26636v1 · relevance 0.42

- **In one sentence**: A survey of the classical Bernoulli (one-phase) free boundary problem, a PDE problem where the unknown includes the boundary of the region itself, with emphasis on recent progress.
- **In plain words**: This is an overview article about a mathematical problem in which the shape of a region is itself unknown and must be found along with the physical quantity filling it. The text is a short summary and does not spell out specific results, so it gives only the general purpose: to survey the field and highlight recent advances.
- **Why it matters**: The text does not say which recent results are covered, so its specific importance cannot be judged from it. Free boundary problems of this kind are generally studied in connection with models of phase change and fluid flow, but the abstract itself does not confirm those links.
- **Background needed**: - Partial differential equation (PDE): an equation relating a function to its rates of change in space; used to model heat, fluids, and electric potentials.
- Free boundary problem: a PDE problem where the edge of the region where the solution lives is not known in advance and must be determined as part of the solution.
- One-phase (Bernoulli) problem: a free boundary problem in which the function is zero on one side of the unknown boundary and positive on the other, with a condition linking its gradient to the boundary's movement.
- Survey: an overview of existing work rather than a report of new findings. · level: research-level

<details><summary>Original abstract</summary>

This survey gives an overview of the Bernoulli or one-phase free boundary problem, with emphasis on recent progress.

</details>

### [On the fully nonlinear degenerate parabolic quenching problem](https://arxiv.org/abs/2611.27774)
*Seunghyun Kim, Jos\'{e} Miguel Urbano* · `math.AP` · arXiv:2611.27774v1 · relevance 0.19

- **In one sentence**: The paper studies a fully nonlinear, degenerate parabolic quenching problem with a free boundary, proving existence of nonnegative viscosity solutions with prescribed boundary data, optimal upper growth along the free boundary, and matching non-degeneracy estimates.
- **In plain words**: The paper looks at a time-dependent equation that describes how a quantity spreads and changes, where the region with positive values has a moving edge (the free boundary). The authors show that a suitable solution exists, that it cannot grow faster than a certain rate near that edge, and that it cannot become flat in a way that breaks the scaling. The work is mathematical rather than an applied experiment.
- **Why it matters**: Quenching problems, where a solution reaches zero in finite time or at a boundary, appear in models of combustion and similar processes, so sharp growth and non-degeneracy bounds help describe how solutions behave at the edge. The text does not claim applications beyond this, so the wider connections are uncertain.
- **Background needed**: - Partial differential equation (PDE): an equation relating a function to its rates of change in space and time.
- Parabolic equation: a PDE of heat-flow type, evolving forward in time.
- Free boundary: the moving interface between the region where the solution is positive and where it is zero.
- Quenching: a solution reaching zero (or a boundary value) in finite time while a source term acts.
- Fully nonlinear, uniformly elliptic operator: a rule for combining second derivatives that is non-linear but bounded in a controlled way.
- Degenerate: the equation's strength drops to zero in some places, here through the gradient term.
- Viscosity solution: a weak notion of solution that works for non-smooth functions.
- Non-degeneracy estimate: a lower bound showing the solution cannot stay arbitrarily close to zero near the free boundary.
- Scaling and barrier arguments: standard tools that compare the solution with explicit sub- and super-solutions. · level: research-level

<details><summary>Original abstract</summary>

We study the fully nonlinear degenerate parabolic free boundary problem $$|Du|^\kappa F(D^2u)-u_t=u^{\gamma-1} \qquad \textrm{in} \quad \{u>0\},$$ where $\kappa>0$, $0<\gamma<1$, and $F$ is a convex or concave uniformly elliptic operator with $F(0)=0$. We establish the existence of a nonnegative viscosity solution with prescribed continuous nonnegative boundary data and prove its optimal upper growth along the free boundary, together with matching non-degeneracy estimates in parabolic cylinders adapted to the scaling. Our approach combines a weak Bernstein estimate with barrier arguments to obtain local compactness and boundary attainment. To obtain the optimal growth rate, we further use persistence of positivity for limits with vanishing absorption coefficients to identify the homogeneous equation across the zero set, and then combine the optimal spatial regularity estimate of \cite{LLYZ25} with an iteration argument.

</details>

## Harmonic analysis

### [Freedom is all you need](https://arxiv.org/abs/2611.27943)
*Julian Bushelli, James Eldred Pascoe* · `math.FA` · arXiv:2611.27943v1 · relevance 0.14

- **In one sentence**: The paper begins a representation theory that relates a generic free functional calculus (for functions of tuples of noncommuting operators, over a category) to the classical noncommutative functional calculus of Taylor, Voiculescu and others, with a view to learning about categories and to analytic properties on direct-sum-closed, similarity-invariant domains.
- **In plain words**: The paper is about how to apply functions to matrices, and to more general mathematical objects that do not commute, in a way that keeps track of their structure. The author starts a framework that links a newer, very general version of this "free" calculus to older, established versions. The text claims that on certain well-behaved domains, such functions are automatically analytic (smooth in the complex-number sense), and it offers a speculative link to why very large neural-network-like systems can generalize well even when they overfit.
- **Why it matters**: The work is mainly theoretical and its abstract mentions the link to neural networks only as a "hypothetical explanation," so the connection is unproven and should be treated cautiously. It may matter to researchers in operator theory and to anyone studying why overparameterized models generalize, but the text alone does not show how far these ideas extend.
- **Background needed**: - Functional calculus: a way of defining f(A) for a function f and a matrix or operator A, extending ordinary function evaluation.
- Matrices and operators need not commute (AB may differ from BA), which is what makes "noncommutative" calculus harder than the usual one.
- Analytic function: one that can be locally written as a convergent power series, a strong form of smoothness from complex analysis.
- Category: an abstract framework of objects and the maps between them, used to organize mathematical structures.
- Similarity (change of coordinates): replacing a matrix by an equivalent one written in a different basis; "locally similarity invariant" means results do not depend on that choice.
- Direct sum: placing matrices block-diagonally; "direct-sum closed" means the domain is preserved under this operation.
- Overfitting: a model fitting training data so closely that it may perform poorly on new data; "beneficial overfitting" refers to cases where it still generalizes well. · level: research-level

<details><summary>Original abstract</summary>

The functional calculus allows for the rigorous analysis of functions of matrices or even operators. The free functional calculus gives the natural class of functions over any category. We initiate the representation theory for taking a generic free functional calculus to the classical nc functional calculus going back to Taylor, Voiculescu and many others, with an eye towards learning of categories. The functional calculus on direct sum closed and locally similarity (i.e. change of coordinates) invariant domains inherits the niceties of complex analysis and large-scale parallel networks, such as automatic analyticity, free universal monodromy, which gives a hypothetical explanation for beneficial overfitting.

</details>

### [The Ritt problem is decidable](https://arxiv.org/abs/2611.27008)
*Jason Fang, James Freitag, Matthew Harrison-Trainor* · `math.AC` · arXiv:2611.27008v1 · relevance 0.14

- **In one sentence**: The paper gives a positive answer to the Ritt problem, which asks whether there is an algorithm that decides in finite time if a given decomposition-type question about polynomial or rational functions can be solved.
- **In plain words**: This paper settles an old question about functions built by composing simpler functions. The question is whether a computer could always determine, in a finite number of steps, if a given function can be broken down in a certain way. The authors answer yes, meaning such a procedure exists.
- **Why it matters**: The text is only a one-sentence abstract, so the exact scope and method are not shown. It is a claimed resolution of a named open problem, and its significance rests on the full argument, which is not included here.
- **Background needed**: - Functions can be composed: feeding the output of one function into another, such as f(g(x)).
- Ritt's problem concerns decomposing a function into a composition of simpler pieces, following work by J. F. Ritt in the 1920s and 1930s.
- "Decidable" means a procedure exists that always returns a correct yes-or-no answer in finitely many steps.
- The abstract does not specify which class of functions is meant, so the precise statement must be checked in the full paper. · level: research-level

<details><summary>Original abstract</summary>

We give an affirmative solution to the Ritt problem.

</details>

## Complex analysis

### [An affine surface with 3-step nilpotent fundamental group](https://arxiv.org/abs/2611.27475)
*Sergey Polevoy, Vasily Rogov* · `math.AG` · arXiv:2611.27475v1 · relevance 0.09

- **In one sentence**: The paper constructs a smooth complex affine surface whose fundamental group is virtually 3-step nilpotent but not virtually 2-step nilpotent, giving a negative answer to the quasi-projective version of Campana's nilpotency problem.
- **In plain words**: The paper is about shapes called complex affine surfaces, which are smooth algebraic objects built from complex numbers, and about a "loop structure" attached to them, called the fundamental group, that records how loops can be traced on the surface. The authors build one specific surface whose loop structure is nilpotent of step 3 (up to passing to a finite-index piece), but not of step 2. This answers a question in the negative.
- **Why it matters**: It settles a question posed by Campana about which loop structures can arise from these surfaces, so it narrows what the theory can say. The text given does not say how widely the question matters beyond this specific area.
- **Background needed**: - Complex affine surface: a smooth two-dimensional complex algebraic variety with no points at infinity, roughly a surface cut out by polynomial equations.
- Fundamental group: the group of loops on a space up to continuous deformation; it captures the space's basic loop structure.
- Nilpotent group: a group that becomes trivial after repeatedly taking commutators; the "step" is how many times you must do this. "Virtually" means true after passing to a finite-index subgroup.
- Campana's nilpotency problem: a question asking which fundamental groups of such varieties must be nilpotent; the quasi-projective version concerns affine-type (non-compact) varieties.
- Only the abstract is provided, so the construction details are not available. · level: research-level

<details><summary>Original abstract</summary>

We construct a smooth complex affine surface $Y$ such that $\pi_1(Y)$ is virtually $3$-step nilpotent, but not virtually $2$-step nilpotent. This gives a negative answer to the quasi-projective version of Campana's nilpotency problem.

</details>

### [Local connectivity of Julia sets of Newton maps of trigonometric and hyperbolic functions](https://arxiv.org/abs/2611.26654)
*Molla Basir Ahamed, Sayantan Chakraborty* · `math.DS` · arXiv:2611.26654v1 · relevance 0.07

- **In one sentence**: The paper proves local connectivity of Julia sets (the boundaries of the basins of attraction) for Newton maps of sin, cos, sinh and cosh, by verifying repelling petals at infinity for the cosine map and by showing the hyperbolic family is conjugate to the sine map.
- **In plain words**: The paper studies a standard root-finding method, Newton's method, applied to four trigonometric and hyperbolic functions, and asks how the regions of starting points that converge to each answer are shaped at their edges. For the cosine case, the authors check directly that certain half-plane regions far from the origin behave repulsively in the way the known criterion requires, which lets them conclude that the edges of the basins are locally connected (they do not pinch apart into disconnected pieces). They also show that a family of hyperbolic-function Newton maps is just the sine case in disguise, so the sine result carries over to them.
- **Why it matters**: Local connectivity is a key property that makes the boundary of a dynamical system easier to describe and to draw, and this extends such results to several transcendental functions that were not covered before. The text does not say how far the methods extend beyond these four maps, so wider impact is uncertain.
- **Background needed**: - Newton's method: an iterative rule z → z − f(z)/f'(z) that tries to find roots of f; here the map is written as z + cot z for cos and z − tan z for sin.
- Dynamical plane and basins: starting points are colored by where iteration converges; a Julia set is the boundary between regions of different long-term behaviour.
- Immediate basin: the component of the attracting region that contains an attracting point; "unbounded" means it extends to infinity.
- Transcendental meromorphic function: a function with essential singularities at infinity (such as sin or exp) that is analytic except for poles.
- Local connectivity: the boundary is made of pieces that connect locally, with no isolated fragments pinching off; the tame-basin criterion is a sufficient test for this.
- Repelling petal: a region near infinity where iterates move away from the point at infinity, used to control dynamics there.
- Affine conjugacy: two maps are the same up to a change of coordinates by a linear rescaling and shift. · level: research-level

<details><summary>Original abstract</summary>

We study the Newton maps of $\sin z$, $\cos z$, $\sinh z$, and $\cosh z$, each of which is transcendental meromorphic and has infinitely many unbounded immediate attracting basins. We first verify directly that, for the cosine Newton map $N_{\cos}(z) = z + \cot z$, the half-planes $\{\pm \operatorname{Im} z > M\}$ are repelling petals at infinity for every $M \ge 2$. These explicit petals allow us to apply the tame-basin criterion of Bara\'nski, Fagella, Jarque, and Karpi\'nska and obtain local connectivity of the spherical boundary of each immediate basin of $N_{\cos}$. We also show that the Newton map of $Ae^{\lambda z} + Be^{-\lambda z}$, where $AB\lambda \neq 0$, is affinely conjugate to the sine Newton map $N_{\sin}(z) = z - \tan z$. The published local-connectivity theorem for $J(N_{\sin})$ therefore applies to this entire family, including the cosine and the two hyperbolic Newton maps. We describe the invariant lines and basin geometry of the four maps and illustrate the corresponding dynamical planes numerically.

</details>

## Operator algebras and spectral theory

### [On the AF embedding problem](https://arxiv.org/abs/2611.27471)
*Christopher Schafhauser* · `math.OA` · arXiv:2611.27471v1 · relevance 0.17

- **In one sentence**: A survey of the AF-embedding problem for C*-algebras, centred on the author's result that separable exact UCT C*-algebras with a faithful quasidiagonal trace embed into a unital simple AF algebra.
- **In plain words**: This paper is a survey about when a mathematical object called a C*-algebra can be placed inside a simpler kind, namely an "approximately finite dimensional" (AF) algebra, which is built up as a limit of finite-dimensional pieces. It mainly summarises the author's earlier work, which shows that a fairly broad class of these algebras can indeed be embedded into a simple AF algebra under certain conditions. The text also mentions some other results but gives no further detail in the given excerpt.
- **Why it matters**: The question of which algebras sit inside tame, well-understood ones is central to classification programmes in operator algebras. The text does not indicate wider applications, so its reach beyond this specialist area is unclear.
- **Background needed**: - C*-algebra: an algebra of bounded operators on a Hilbert space, a basic object in operator algebra theory and quantum physics.
- AF algebra: a direct limit (an increasing union, roughly) of finite-dimensional matrix algebras; these are the "simplest" infinite C*-algebras.
- Embedding: placing one algebra inside another as a subalgebra.
- Exact, UCT, quasidiagonal, trace, simple: technical regularity conditions on C*-algebras that control their structure.
- Survey: an overview of existing results rather than new proofs. · level: research-level

<details><summary>Original abstract</summary>

This article gives a survey of the AF-embedding problem for $C^*$-algebras. The problem asks when a given $C^*$-algebra $A$ embeds into an \emph{approximately finite dimensional} (AF) $C^*$-algebra (a direct limit of finite dimensional $C^*$-algebras). This is largely based on my paper ``Subalgebras of simple AF algebras,'' which shows that separable, exact $C^*$-algebras satisfying the UCT and admitting a faithful, quasidiagonal trace embed into a unital, simple AF algebra. Some other results are also discussed.

</details>

### [Rigidity in the Lichnerowicz inequality for word-length semigroups](https://arxiv.org/abs/2611.27204)
*Melchior Wirth* · `math.OA` · arXiv:2611.27204v1 · relevance 0.15

- **In one sentence**: The paper shows that for word-length semigroups on group von Neumann algebras, equality in two noncommutative Lichnerowicz-type spectral gap bounds (the complete Γ2 constant of Junge–Zeng and the geometric Ricci constant of Junge–LaRacuente–Li) holds exactly when the group's Cayley graph is a partial cube.
- **In plain words**: The paper studies how fast a random-walk-like process (a quantum Markov semigroup) on a group settles down to equilibrium, measured by a number called the spectral gap. It asks when two known bounds on that speed become exact, and gives a geometric answer: equality happens precisely when the group's Cayley graph (a map of the group where neighbouring elements are joined by edges) can be drawn isometrically inside a hypercube. So a purely geometric property of the graph is characterized by an operator-algebra condition.
- **Why it matters**: It links a geometric notion of graphs that embed in hypercubes to sharp constants in noncommutative geometry and quantum Markov dynamics, giving a new operator-algebraic test for a combinatorial property. The text does not indicate further applications, so the wider significance is unclear from this abstract alone.
- **Background needed**: - Group von Neumann algebra: a noncommutative algebra built from a group, playing the role of functions on the group.
- Cayley graph: a graph whose vertices are group elements, with edges between elements differing by a generator.
- Word-length semigroup: a family of operators governed by how many generators a group element needs to be written, a discrete analogue of heat flow.
- Spectral gap: the smallest nonzero eigenvalue of the generator; it controls how quickly the process mixes toward equilibrium.
- Lichnerowicz inequality: a classical bound relating the spectral gap to curvature-type constants; here extended to quantum settings.
- Complete Γ2 criterion and geometric Ricci criterion: two noncommutative curvature-type constants from the cited work of Junge, Zeng, LaRacuente and Li.
- Partial cube: a graph that embeds isometrically (distances preserved) into a hypercube. · level: research-level

<details><summary>Original abstract</summary>

We give an operator-algebraic characterization of Cayley graphs that are partial cubes, that is, embed isometrically into a hypercube. More precisely, noncommutative versions of the Lichnerowicz inequality control the spectral gap of the generator of a quantum Markov semigroup by the constant in the complete $\Gamma_2$-criterion of Junge and Zeng or the constant in the geometric Ricci criterion of Junge, LaRacuente and Li. We show that for word-length semigroups on group von Neumann algebras, equality in either of these inequalities occurs exactly when the Cayley graph is a partial cube.

</details>

## Algebra

### [On coherence of enveloping algebras of infinite-dimensional Lie algebras](https://arxiv.org/abs/2611.27824)
*Susan J. Sierra, James Timmins* · `math.RA` · arXiv:2611.27824v1 · relevance 0.22

- **In one sentence**: The paper determines when enveloping algebras of infinite-dimensional Lie algebras (loop algebras and Witt-type algebras in particular) are coherent, and shows related graded and filtered rings inherit coherence.
- **In plain words**: The paper studies a property called "coherence" for a family of algebraic structures built from infinite-dimensional symmetry objects (Lie algebras). Coherence roughly says that certain systems of equations behave nicely, so that the solutions form a well-controlled collection. The authors find that for loop algebras, coherence holds exactly when the underlying finite-dimensional algebra is nilpotent, and they report several related results.
- **Why it matters**: Coherence is a basic regularity property in ring theory, and the paper sharpens which infinite-dimensional algebras have it. The results also show that a homomorphic image of U(W), used in earlier work by the first author and Walton to prove non-Noetherianity, is not coherent. The text does not say more about wider applications.
- **Background needed**: - Lie algebra: a vector space with a bracket operation, used to describe continuous symmetries.
- Universal enveloping algebra U(g): a ring built from a Lie algebra g that encodes its representations.
- Coherent ring: a ring in which finitely generated ideals have finitely presented syzygies (informally, the relations among relations are controlled).
- Noetherian ring: every ideal is finitely generated; non-Noetherian means this fails.
- Loop algebra: functions from a circle (or Laurent polynomials) with values in a finite-dimensional Lie algebra.
- Nilpotent: repeated brackets eventually vanish.
- Witt algebra: the algebra of derivations of Laurent polynomials in one variable.
- Graded and filtered rings; Rees ring: standard tools for organizing a ring by degree or by a growing sequence of subspaces. · level: research-level

<details><summary>Original abstract</summary>

We investigate when the universal enveloping algebra $U(\mathfrak{g})$ of an infinite-dimensional Lie algebra $\mathfrak{g}$ is coherent. We show that if $\mathfrak{g}$ is the loop algebra of a finite-dimensional Lie algebra $\mathfrak{h}$ then $U(\mathfrak{g})$ is coherent exactly when $\mathfrak{h}$ is nilpotent. As a consequence, we show that $U(\mathfrak{g})$ is not coherent if $\mathfrak{g}$ is complex, simple, $\mathbb{Z}$-graded, of polynomially bounded growth, and not isomorphic to the Witt algebra $W = \mathrm{Der} \mathbb{C}[t,t^{-1}]$ or its one-sided version. We also demonstrate that the homomorphic image of $U(W)$ used to prove non-Noetherianity of $U(W)$ in previous work of the first author and Walton is not coherent. On the other hand, we establish that two closely related connected graded rings are graded coherent. Finally, we prove that any exhaustively filtered ring is coherent if its Rees ring is graded coherent.

</details>

### [Large orbits of $p$-groups on conjugacy classes of arbitrary finite groups](https://arxiv.org/abs/2611.27916)
*Thomas Michael Keller* · `math.GR` · arXiv:2611.27916v1 · relevance 0.19

- **In one sentence**: The paper removes the solvability hypothesis from a known result: for a p-group acting coprimely and faithfully on a finite group H, some conjugacy class of H has stabilizer of order at most |P|^(1/2), and the paper also gives nonsolvable examples where this bound is attained.
- **In plain words**: This is about symmetries of finite mathematical structures. A group of symmetries of a certain power-of-a-prime size acts on a finite group, and the question is how many of that group's pieces it can keep fixed. The paper shows that, even when the underlying group is not solvable, there is always a piece whose set of symmetries that fix it is small, no bigger than the square root of the symmetry group's size.
- **Why it matters**: A bound of this kind is a structural statement that tells mathematicians how large orbits must be, which matters for the representation theory of finite groups. The text does not indicate applications beyond this area, so its wider significance is unclear.
- **Background needed**: - Finite group: a set of elements with a combining rule, finitely many elements.
- p-group: a group whose size is a power of a prime p.
- Acting coprimely and faithfully: a p-group acts by symmetries whose order is prime to the size of H, with no nontrivial element doing nothing.
- Conjugacy class and stabilizer: the conjugacy class is the set of elements that are rearrangements of one another; the stabilizer is the set of group symmetries that leave a given class unchanged.
- Solvable group: a group built up in a layered way from abelian (commutative) pieces; the paper removes this assumption.
- Classification of finite simple groups: a complete list of the basic building blocks of finite groups, used in the proof.
- Irreducible character: a basic building block of how a group can be represented by matrices. · level: research-level

<details><summary>Original abstract</summary>

Let $P$ be a $p$-group that acts faithfully and coprimely on a finite group $H$. In a previous paper it was shown that if $H$ is solvable, then there exists a conjugacy class $c$ of $H$ whose stabilizer in $P$ has order at most $|P|^{1/2}$, and that this bound is best possible. In this paper we remove the hypothesis that $H$ is solvable. As a consequence, there always exists an irreducible character of $H$ whose inertia group in $P$ has order at most $|P|^{1/2}$. The proof depends on the classification of finite simple groups. Its main new ingredient is a result on quasiprimitive linear actions of $p$-nilpotent groups which shows that the elements acting as field automorphisms can be ignored when one looks for vectors with small stabilizers. We also present a new family of examples, with nonsolvable $H$, in which the bound is attained.

</details>

## Representation theory

### [The $n!$ theorem via quaternionic rotation of Cherednik algebras](https://arxiv.org/abs/2611.27113)
*Stephen Griffeth* · `math.RT` · arXiv:2611.27113v1 · relevance 0.13

- **In one sentence**: The paper gives a new proof of the "n! theorem" for rational Cherednik algebras, using their representation theory and a quaternion-driven analogue of rotating complex structures.
- **In plain words**: The paper concerns a known result, the "n! theorem," which is a statement about certain algebraic structures built from symmetries of objects, here the symmetric group on n items. The authors offer a new proof of it, based on studying the representations of Cherednik algebras and on a mathematical device that mirrors rotating a complex structure, using the quaternions. The summary text itself does not give the details of how the argument runs.
- **Why it matters**: The text describes a new proof of an existing theorem rather than a new result, so its main interest is methodological: it links the theory of Cherednik algebras with quaternion actions. The abstract alone does not show how far the method reaches beyond this theorem.
- **Background needed**: - Symmetric group S_n: the group of all rearrangements of n objects, which has n! elements.
- Representation theory: studying abstract groups or algebras by how they act as matrices on vector spaces.
- Cherednik algebras: a family of noncommutative algebras attached to reflection groups, depending on parameters, studied in representation theory and related to special functions.
- Quaternions: a four-dimensional number system extending the complex numbers, with a noncommutative multiplication.
- Complex structure: an operation that acts like multiplication by i on a real vector space; "rotating" it means varying it continuously within a family. · level: research-level

<details><summary>Original abstract</summary>

We give a proof of the $n!$ theorem based on the representation theory of Cherednik algebras and an analog of the rotation of complex structures arising from an action of the quaternions.

</details>

### [The weighted fundamental lemma for non-split groups](https://arxiv.org/abs/2611.26750)
*Cass Halleck-Dub\'e* · `math.RT` · arXiv:2611.26750v1 · relevance 0.12

- **In one sentence**: The paper proves the Weighted Fundamental Lemma for Lie algebras for general unramified quasi-split groups, adapting the Chaudouard–Laumon global geometric method from the split case and deducing Waldspurger's nonstandard version via a parallel reduction.
- **In plain words**: This is a paper in pure mathematics about symmetry groups and the trace formula, a tool that compares averages of functions over different groups. The author extends a known result from the case of "split" groups to a broader class called quasi-split groups. The method is to study a geometric family of objects (Higgs bundles over a curve) and count points over finite fields to establish an identity between orbital integrals.
- **Why it matters**: The text claims the result completes Moeglin and Waldspurger's stabilization of the twisted trace formula and makes the endoscopic classification for classical groups unconditional, with further consequences in automorphic theory. I have not checked these claims against the full paper, and the abstract gives no independent evidence of their scope.
- **Background needed**: - Representation theory: studies how symmetry groups act on vector spaces and function spaces.
- Reductive group and quasi-split group: a type of algebraic symmetry group with a well-behaved structure; quasi-split is a slightly generalized class.
- Orbital integral: an integral of a function over the conjugacy classes of a group, used to compare groups.
- Fundamental lemma: a local identity between orbital integrals on different groups, a key ingredient of the endoscopy program (Langlands).
- Weighted version and Lie algebra version: variants of the lemma, with extra weighting terms and working with Lie algebras instead of group elements.
- Trace formula and endoscopy: a global tool relating automorphic forms to comparisons with simpler groups.
- Higgs bundle, Hitchin base, Deligne–Mumford stack: objects from algebraic geometry on curves used as the geometric setting.
- Frobenius point count: counting solutions over finite fields as a route to an identity. · level: research-level

<details><summary>Original abstract</summary>

In this work, we prove the Weighted Fundamental Lemma for Lie algebras for general (quasi-split) unramified $G$. The strategy is to adapt the proof of Chaudouard--Laumon from the split case. In particular, we define the notion of a $\xi$-stable Higgs bundle for a quasi-split reductive group scheme $G$ on a curve, and prove that the stack of such form a proper, finite-type Deligne--Mumford stack over the Hitchin base when $G$ has anisotropic center. We then adapt the global cohomological theorem of Chaudouard--Laumon to the quasi-split setting, and perform the required Frobenius-point count to obtain an identity of adelic orbital integrals. A local-to-global argument deduces the WFL for Lie algebras. In the last chapter, we perform a parallel reduction to deduce Waldspurger's nonstandard WFL from a global version which follows from the same geometric theory. Our work implies the Twisted Weighted Fundamental Lemma in good characteristic, which completes Moeglin--Waldspurger's stabilization of the twisted Arthur--Selberg trace formula. We therefore render unconditional the endoscopic classification for classical groups and an array of downstream consequences in automorphic theory.

</details>

## Number theory

### [Splitting types of Richelot isogenies over finite fields and a newform of weight four](https://arxiv.org/abs/2611.27775)
*Hung Dang* · `math.NT` · arXiv:2611.27775v1 · relevance 0.17

- **In one sentence**: Exact counts of factorizations of square-free sextics over finite fields into three quadratics, split by how each quadratic factors over F_q, with the counts expressed through a twisted second moment of the Legendre family and the weight-4 newform of level 8.
- **In plain words**: The paper counts ways to split a degree-six polynomial over a finite field (a number system with finitely many elements) into three quadratic pieces, and it sorts these splittings by how each piece breaks down further. Each count is given by a formula involving a fixed cubic polynomial and a number attached to a particular modular form, a special kind of symmetric function from number theory. The authors also derive consequences about how often certain pairs of these pieces share a square class, and about which points of order two on an associated elliptic curve can be halved.
- **Why it matters**: The result gives closed formulas for counts that otherwise require heavy computation, and ties a concrete counting problem about genus-2 curves to a known modular form. The text does not say how the work bears on wider questions, so its broader significance is unclear from this text alone.
- **Background needed**: - Finite field F_q: a finite set of q elements with addition and multiplication, where q is a prime power.
- Square-free sextic: a degree-six polynomial with no repeated roots.
- Quadratic factor: a degree-two polynomial; "splitting" means whether it factors into linear pieces over F_q.
- Genus-2 curve and (2,2)-isogeny: a curve of genus 2 (roughly, two holes) and a structured map between such curves/Jacobians, built here by the Richelot construction.
- Legendre family of elliptic curves: a standard one-parameter family of elliptic curves; a "twisted second moment" is an averaged sum over this family.
- Hypergeometric function over F_q: a finite-field analogue of special functions, here evaluated by earlier work of Ahlgren and Ono.
- Newform of weight 4 and level 8: a modular form with specified symmetry and conductor; its trace of Frobenius t_q is an integer tied to point counts.
- Square class and resultant: whether a number is a square in F_q, and a quantity measuring whether two polynomials share a root.
- Points of order two and divisibility by two: elements of an elliptic curve killed by doubling, and whether they are doubles of other points. · level: research-level

<details><summary>Original abstract</summary>

A factorization $f=uvw$ of a square-free sextic over a finite field $\mathbb{F}_q$ of odd characteristic into three monic quadratics defines a genus-2 curve with a rational $(2,2)$-isogeny kernel, and the Richelot construction attaches to it three dual quadratics $U,V,W$. We determine, for every odd prime power $q$, the number of such factorizations with prescribed splitting behaviour over $\mathbb{F}_q$ of all six quadratics. Each of the $64$ counts is $q(q-1)(q+1-n_f)/64$ times $C(q)\pm t_q$, where $n_f$ is the number of roots of $f$ in $\mathbb{F}_q$, $C$ is an explicit monic cubic, and $t_q$ is the trace of Frobenius attached to the newform $\eta(2z)^{4}\eta(4z)^{4}$ of weight $4$ and level $8$. The proof reduces the counts by elementary means to a twisted second moment of the Legendre family of elliptic curves, which is a value of a hypergeometric function over $\mathbb{F}_q$ evaluated by Ahlgren and Ono for primes. As consequences, the number of factorizations whose three pairwise resultants lie in one square class is a polynomial in $q$, with proportion $1/4+3/(4q^{2})+O(q^{-4})$. When the quotient is a product of two elliptic curves conjugate over $\mathbb{F}_{q^2}$, we prove that the splitting of the factors $u,v,w$ over $\mathbb{F}_q$ decides which points of order two of the elliptic factor are divisible by two.

</details>

### [An explicit Cassels--Tate pairing in characteristic $2$ and the parity of $2$-Selmer ranks](https://arxiv.org/abs/2611.27040)
*Abhishek Shukla* · `math.NT` · arXiv:2611.27040v1 · relevance 0.17

- **In one sentence**: For an ordinary elliptic curve over a global field of characteristic 2 with a rational 2-torsion point, the paper gives an explicit formula for the Cassels–Tate pairing on the 2-torsion of the Tate–Shafarevich group as a sum of local Artin–Schreier symbols, relates it to Kramer's and Milne's pairings, and derives parity results for 2-Selmer ranks via local root numbers.
- **In plain words**: This is research in pure mathematics about elliptic curves, the smooth curves that carry a group structure and whose rational points form a finite-generated group. The paper studies curves over number-like fields in characteristic 2 (a setting where arithmetic works mod 2) and asks how to tell the size of a hidden obstruction group, the Tate–Shafarevich group, from local data. It proves an explicit formula for a pairing that detects this obstruction and shows that the parity of a certain count of rational points plus obstruction size can be read off from local terms.</plain>
<why>Parity questions about ranks and obstructions are central to the Birch and Swinnerton-Dyer picture, so an explicit, computable pairing is useful for examples. The text links the local terms to root numbers, which may connect to the known parity conjectures, but the summary does not show how far this extends beyond the stated cases.</why>
<background>
- Elliptic curve: a curve with a group law whose rational points form a finitely generated group.
- Rank: the number of independent rational points of infinite order.
- Tate–Shafarevich group (Sha): a finite-looking group of curve-torsors measuring failure of a local-global principle; its 2-torsion part is what is studied.
- Selmer group: a computable group that bounds rank and Sha.
- Cassels–Tate pairing: an alternating pairing on Sha whose kernel detects its size modulo divisible parts.
- Global field of characteristic 2: a function field over a finite field, or a finite extension of F_2((t)).
- Artin–Schreier symbol: a local pairing in characteristic p, analogous to Hilbert symbols in characteristic 0.
- Root number: a sign (±1) attached to each place from the L-function, whose product governs rank parity conjecturally.
- Ordinary curve: one whose 2-torsion behaves as in the generic case in characteristic 2.
</background>
<difficulty>research-level</difficulty>

<details><summary>Original abstract</summary>

Let $K$ be a global field of characteristic $2$ and $\varphi\colon E\to E'$ the Verschiebung of an ordinary elliptic curve $E/K$ with a rational point of order $2$. We prove an explicit formula for the homogeneous-space Cassels--Tate pairing on $\Sha(E/K)[\varphi]$ as a sum of local Artin--Schreier symbols, show that it coincides with Kramer's descent pairing and, on $\Sha(E/K)[\varphi]$, with the pairing induced by Milne's flat duality, and deduce that it is non-degenerate on $\Sha(E/K)[\varphi]/\hat\varphi(\Sha(E'/K)[2])$. For every ordinary elliptic curve $A/K$ we express the parity of $\mathrm{rk}\,A(K)+\dim\Sha(A/K)[2]$ by local terms (after Kramer), and identify these with local root numbers at places of semistable or potentially multiplicative reduction, and in further cases using curves with finite $\Sha$. We determine $\Sha$ in examples, and extend the formula to rational points of any prime order $\ell$, the new case being $\ell=\operatorname{char}K$.

</details>

## Algebraic geometry

### [Combinatorial relative orientability for toric and tropical geometry](https://arxiv.org/abs/2611.27238)
*Nathan Tiggemann* · `math.AG` · arXiv:2611.27238v1 · relevance 0.25

- **In one sentence**: The paper gives a combinatorial criterion for relative orientability of vector bundles over smooth proper toric varieties, shows it is compatible with tropicalization, and applies this to a quadratically enriched Bernstein-Khovanskii-Kushnirenko theorem and to k-phase structures on tropical hypersurfaces.
- **In plain words**: Many counting problems in geometry ask how many solutions a system of equations has, and the answer is often a single number computed from a special invariant of a shape. This paper studies when that invariant can be made well-defined over any number field, and it translates the question into a simpler combinatorial form using tropical geometry, a method that replaces shapes with piecewise-linear skeletons. The authors describe the needed "orientability" condition in purely combinatorial terms, show it survives this translation, and use it to prove a refined version of a known counting theorem.
- **Why it matters**: It offers a way to carry enumerative counts from tropical geometry, where they are combinatorial and easier to handle, over arbitrary fields, which is the setting of the refined counting theory. The text does not say how far this will reach beyond the examples given, so the broader impact is uncertain.
- **Background needed**: - Enumerative geometry: counting solutions to geometric problems, such as how many curves satisfy given conditions.
- Vector bundle: a family of vector spaces attached smoothly to each point of a space; its top Chern class is an invariant whose degree gives a count.
- Orientation: a consistent choice of direction or sign; "relative orientability" is the condition that such a choice exists across a bundle.
- Toric variety: a geometric space built from combinatorial data (polytopes and fans), which makes computations discrete.
- Tropical geometry: a piecewise-linear analogue of algebraic geometry that turns polynomial problems into combinatorial ones.
- A^1-homotopy theory and Chow-Witt groups: tools from modern algebraic topology that refine counts over arbitrary fields, often yielding values in quadratic forms rather than integers.
- Bernstein-Khovanskii-Kushnirenko theorem: a classical result relating the number of solutions of polynomial systems to the volumes of their Newton polytopes. · level: research-level

<details><summary>Original abstract</summary>

Many problems in enumerative geometry are solved by computing the degree of the top Chern class of a suitable vector bundle. Results from $\mathbb{A}^1$-homotopy theory allow to answer enumerative questions over arbitrary fields, replacing the top Chern class by the Euler class in Chow-Witt groups. For its degree to be well-defined, one needs the vector bundle to be relatively oriented. Another way to solve enumerative problems is to translate them to tropical geometry, where they become combinatorial problems. In this paper, we give a combinatorial description of relative orientability for vector bundles over smooth proper toric varieties. We show that it behaves well under tropicalization, establishing a tropical version of relative orientability, which will allow to the use of tropical geometry to answer enumerative questions over arbitrary fields. As a demonstration, we prove a quadratically enriched version of the Bernstein-Khovanskii-Kushnirenko theorem via tropical geometry. Lastly, we define the notion of $k$-phase structures on tropical hypersurfaces, generalizing the real case.

</details>

### [Classification of strongly $F$-regular and $F$-pure surface singularities with imperfect residue fields](https://arxiv.org/abs/2611.27597)
*Tatsuro Kawakami, Kenta Sato* · `math.AG` · arXiv:2611.27597v1 · relevance 0.12

- **In one sentence**: The paper classifies strongly F-regular and F-pure normal surface singularities over possibly imperfect residue fields, characterizing strong F-regularity via the weighted dual graph and geometric reducedness of exceptional components of the minimal resolution, and extending Hara's algebraically closed case.
- **In plain words**: This paper studies certain well-behaved kinds of corner-shaped points on surfaces defined by polynomial equations, which are described by algebra over number-like fields that need not be "perfect." The authors show how these points can be recognized from a diagram (a weighted dual graph) that records how the point is resolved into simpler pieces, together with whether those pieces remain reduced under field extension. The result generalizes an earlier classification that assumed the underlying field was algebraically closed.
- **Why it matters**: It completes and extends a known classification in positive characteristic commutative algebra to a broader setting, which matters for specialists in singularity theory and the F-singularity program. The text does not indicate applications beyond this area, so wider significance is uncertain.
- **Background needed**: - Singularity: a point where a surface defined by polynomial equations fails to be smooth.
- Residue field: the field of coefficients left after evaluating at the singular point; "imperfect" means some p-th roots are missing, which matters in characteristic p.
- F-regular / F-pure: properties defined using the Frobenius map (raising to the p-th power) in characteristic p, signaling mild, well-behaved singularities.
- Minimal resolution: replacing the singular point by a smooth surface with a minimal set of curves (exceptional components) lying over it.
- Dual graph: a diagram of those curves and their intersections, with weights recording self-intersection data.
- Rational double point: a simple class of singularities, the mildest type in the classification.
- Hara's classification: an earlier result for the case of algebraically closed fields. · level: research-level

<details><summary>Original abstract</summary>

We study strongly $F$-regular and $F$-pure normal surface singularities whose residue fields are not necessarily perfect. We characterize strong $F$-regularity in terms of the weighted dual graph and geometric reducedness of the exceptional components of the minimal resolution, extending Hara's classification over algebraically closed residue fields. We also determine the possible dual graphs of $F$-pure surface singularities and give converse criteria. Notably, the exceptional components of an $F$-pure surface singularity are geometrically reduced unless the singularity is a rational double point.

</details>

## Topology

### [Persistent Mayer Path Homology and Mayer Path Laplacian](https://arxiv.org/abs/2611.26982)
*Dilan Karaguler, Guowei Wei* · `math.AT` · arXiv:2611.26982v1 · relevance 0.16

- **In one sentence**: The paper introduces persistent Mayer path homology and Mayer path Laplacians for filtered directed graphs, proving functoriality, barcode stability, eigenvalue stability, and results for N=3 that relate Betti numbers to vertices, squares, and triangles.
- **In plain words**: The paper extends a method for describing the shape of networks with one-way connections, such as directed graphs. It replaces the usual rule that applying the boundary operation twice gives zero with a weaker rule that applying it N times gives zero. The authors then track these shape features as a graph grows through a range of distance thresholds, and they test the approach on a molecule, cucurbit[7]uril.
- **Why it matters**: The text claims the new method detects feed-forward loops that the older path homology misses, and that in the molecule it changes at almost four times as many filtration values as path homology after the bonded framework forms. Its relevance beyond these examples is not established in the text, so the broader reach of the method is uncertain.
- **Background needed**: - Graph: dots (vertices) joined by lines (edges); a directed graph has one-way arrows.
- Homology: a counting method that finds loops and holes in a shape; Betti numbers count them.
- Boundary operator: a rule mapping a shape to its edges; in ordinary homology applying it twice gives zero.
- Nilpotent of order N: applying the rule N times gives zero, a weaker condition than applying it twice.
- Path homology: a version of homology adapted to directed graphs.
- Laplacian: a matrix whose eigenvalues (spectrum) encode the same shape information.
- Persistent homology: tracking features as a threshold (filtration) increases, summarized in barcodes.
- Feed-forward loop: a small directed pattern in which one node points to a second, which points to a third, and the first also points to the third.
- Functoriality and stability: mathematical guarantees that the results behave consistently under maps between graphs and under small perturbations. · level: research-level

<details><summary>Original abstract</summary>

In topological data analysis, path homology accounts for directed graph while combinatorial Laplacian extends homology groups to spectral theory. However, these approaches are built on a boundary operator with condition $\partial^2=0$. Mayer homology replaces this condition with $N$-nilpotent boundary map $\partial^N=0$. By using the primitive $N$-th root of unity in the boundary operator, it relates each degree $n$ to the degrees $n-q$ and $n+N-q$. This work introduces persistent Mayer path homology. We show that Mayer path homology is functorial for strict digraph maps, which gives persistent Mayer path homology for filtered digraphs, and prove that its barcodes are stable under perturbations. For $N=3$ we derive formulas that reduce $\beta_0^{3,1}$ and $\beta_2^{3,2}$ to the classes of vertices identified by squares and the rank of a small matrix indexed by triangles. We also introduce the Mayer path Laplacian and its persistence theory, prove that their kernels recover (persistent) Mayer path homology, show that they distinguish digraphs with the same Mayer path Betti numbers, and prove a stability bound for the eigenvalues of the persistent up-Laplacian. We demonstrate that persistent Mayer path homology detects the formation of feed-forward loops, whose formation is not detected by ordinary path homology. In an application to cucurbit[7]uril, filtered by an interatomic distance normalized by van der Waals radii, Mayer path homology separates contacts that only close cycles from contacts that close feed-forward triangles, and changes at almost four times as many filtration values as path homology after the bonded framework is formed.

</details>

### [A simple approach to ends of manifolds and the Freudenthal compactification](https://arxiv.org/abs/2611.26989)
*Rodrigo Hern\'andez-Guti\'errez, Carlos Rios-Mendoza* · `math.GN` · arXiv:2611.26989v1 · relevance 0.12

- **In one sentence**: A short expository paper giving an alternative definition of the Freudenthal end-compactification of non-compact manifolds via filters of open sets with compact boundaries that have a base of connected subsets, and proving equivalence with the classical construction.
- **In plain words**: This paper is about a standard way of describing the "ends" of a non-compact shape, meaning the different ways it can run off toward infinity. The author offers a simpler set of definitions for these ends and shows they give the same result as the established construction. The text also works through an example of a non-metrizable manifold and gives a new proof of a known characterization.
- **Why it matters**: The text presents itself as a clarification of existing machinery rather than a new result, so its main value is pedagogical and for specialists who use ends in topology. Its connection to wider applications is not discussed in the text, so I cannot say more about that.
- **Background needed**: - Manifold: a space that locally looks like ordinary Euclidean space, such as a surface.
- Non-compact: the space is unbounded or has no finite "edge" in the sense of compactness.
- Compactness and compact boundary: a set that is closed and bounded in a suitable sense; here the boundary of a region is compact.
- Filter: a collection of sets that is closed under taking supersets and finite intersections; used to pin down "going off to infinity."
- Compactification: adding limit points to a space so that it becomes compact.
- Freudenthal end-compactification: the standard way of adding one point (or more) for each end of the space.
- Metrizable: whether the topology can be described by a distance function. · level: research-level

<details><summary>Original abstract</summary>

In this note we give an alternative definition of the Freudenthal end-compactification of a non-compact manifold by defining ends to be the filters of open subsets with compact boundaries that have a base of connected subsets. We start by defining these notions and proving that the resulting compactification is equivalent to the Freudenthal compactification. In particular, we explicitly discuss the equivalence between our definitions and those from two different approaches: maximal binding families and inverse limits. After that, we give an example of a non-metrizable manifold, showing how these new definitions make it easier to identify ends and understand the topology of the end-compactification. We also prove a well-known metrization theorem, showing an application of our definition. Finally, we also give an alternative proof of the topological characterization of the Freudenthal compactification.

</details>

## Dynamical systems

### [Recurrent sets and Lyapunov functions: from topological dynamics to weak KAM theory](https://arxiv.org/abs/2611.27887)
*Olga Bernardi, Mattia Sensi, Jim Wiseman* · `math.DS` · arXiv:2611.27887v1 · relevance 0.18

- **In one sentence**: A survey linking Lyapunov functions and Conley's chain recurrent sets in topological dynamics, covering recent weak KAM results for homeomorphisms and their ties to the stationary Hamilton-Jacobi equation, with examples from epidemiology and a prey-predator model.
- **In plain words**: This is a review of how two ways of describing long-run behaviour in dynamical systems, namely "recurrent" sets where motion keeps returning near itself and "Lyapunov functions" that act like energy-style measures that decrease along trajectories, are closely related. It summarises recent progress, connects it to a type of equation from physics and geometry, and tests the ideas on two concrete models: a disease compartment model and a predator-prey model with a fast-slow structure and an Allee effect (where small populations struggle to grow).
- **Why it matters**: The text presents this as a survey of the state of the art rather than a single new result, so its value lies in organising existing work. It may matter to people studying stability and long-term behaviour in ecology or epidemiology, and to researchers linking dynamics with Hamilton-Jacobi equations, but the text does not say more about specific applications.
- **Background needed**: - Dynamical system: a rule that describes how a state evolves over time, such as populations changing year to year.
- Recurrent set: a region that a system's motion keeps returning to, at least approximately, so it persists in the long run.
- Chain recurrence (Conley): a looser notion of return that allows small jumps, introduced by Charles Conley.
- Lyapunov function: a function that decreases along trajectories and certifies stability, similar to an energy that settles to a minimum.
- Homeomorphism: a continuous, reversible transformation of a space, the discrete-time setting studied here.
- Weak KAM theory: a modern framework from Hamiltonian mechanics linking long-run motion to solutions of Hamilton-Jacobi equations.
- Hamilton-Jacobi equation: a partial differential equation from physics and optimal control.
- Fast-slow system: a model with variables changing on very different timescales. · level: research-level

<details><summary>Original abstract</summary>

The aim of this survey is to clarify the intimate relations between Lyapunov functions and chain recurrent sets. The study of this subject comes from a seminal paper by Conley and has had recent advances by the so-called Weak KAM Theory for homeomorphisms. We provide a survey of the state of the art, presenting recent improvements and connections with the stationary Hamilton-Jacobi equation. Finally, in order to illustrate the distinctions between recurrent sets in a non-trivial case as well as their dependence on a parameter, we discuss a compartmental model from mathematical epidemiology and a fast-slow version of a prey-predator model with Allee effect.

</details>

### [Non-local ergodic measures in symplectic dynamics](https://arxiv.org/abs/2611.27429)
*Jaime Paradela* · `math.DS` · arXiv:2611.27429v1 · relevance 0.15

- **In one sentence**: For a product of two symplectomorphisms (one with a basic set, the other acting on a compact surface with a non-degenerate elliptic equilibrium), the paper shows that under a local domination condition, typical real-analytic perturbations produce a large normally hyperbolic lamination carrying an ergodic natural invariant measure.
- **In plain words**: This is a mathematical study of systems that evolve in a rule-governed, energy-conserving way, such as idealized planetary or fluid motion. The authors ask whether, after a small generic nudge to the rules, the long-run behaviour of the system is "mixing" in a precise sense: a single typical trajectory eventually samples the space in the same proportions as the whole. They report that, under a stated local condition, such ergodic behaviour appears on a large structured set.
- **Why it matters**: Ergodicity in conservative systems is a central and hard question in dynamics, and the abstract highlights a new geometric source of "semi-local" ergodicity. Its relevance beyond this setting is claimed by the authors as robustness, but the text alone does not show wider consequences.
- **Background needed**: - Symplectomorphism: a smooth map that preserves the geometry of phase space, the standard model for conservative mechanics.
- Invariant measure: a way of assigning sizes to sets that the dynamics does not change; ergodic means almost every trajectory visits regions in the proportions given by this measure.
- Basic set and elliptic equilibrium: a chaotic, hyperbolic piece of the dynamics, and a fixed point where nearby orbits circle around it.
- Normal hyperbolicity and lamination: a structured family of invariant sets with stable and unstable directions, rather than a single orbit.
- KAM theory: tools showing that quasi-periodic, stable motion survives small perturbations.
- Real-analytic perturbation: a small change to the system that is smooth in a strong sense; "typical" means for most such changes. · level: research-level

<details><summary>Original abstract</summary>

We consider the direct product of two symplectomorphisms, one of which exhibits a basic set and the other one acts on a compact surface and has a non-degenerate elliptic equilibrium. Under a local domination condition we show that a typical real-analytic perturbation of this system displays a large normally hyperbolic lamination on which the natural invariant measure is ergodic. The proof, which introduces a novel geometric source of semi-local ergodicity, combines tools ranging from KAM theory to geometric measure theory and is robust enough to be of interest in more general configurations.

</details>

## Combinatorics

### [Small spherical 7-designs in prime dimensions](https://arxiv.org/abs/2611.26879)
*Andriy Bondarenko, Dmytro Mitin* · `math.CO` · arXiv:2611.26879v1 · relevance 0.14

- **In one sentence**: The paper constructs antipodal spherical 7-designs on the unit sphere in dimension p-1 for every prime p at least 29, with 42(p-1)(p+2)^2 points, using eigenlines of finite Weil operators.
- **In plain words**: The paper is about placing a finite set of points evenly over the surface of a high-dimensional sphere, so that averaging simple polynomial functions over those points gives the same answer as averaging over the whole sphere. The authors give an explicit construction of such point sets for every prime dimension index p of at least 29, and the point sets are "antipodal", meaning each point comes with its opposite. The abstract reports the number of points used but, as given here, does not discuss how close these sets are to the smallest possible.
- **Why it matters**: Spherical designs are used in areas such as numerical integration, coding theory and quantum information, where small, evenly spread point sets are valuable. The text does not say how the construction compares with existing designs or what applications it affects, so its wider importance is unclear from the abstract alone.
- **Background needed**: - A spherical t-design is a finite set of points on a sphere whose average of every polynomial of degree at most t equals the average over the whole sphere.
- A 7-design means this holds up to degree 7.
- Antipodal means that for every point in the set, its opposite point is also in the set.
- S^(p-1) denotes the unit sphere in p-dimensional space.
- Weil operators are objects from harmonic analysis over finite fields; eigenlines are the one-dimensional invariant subspaces attached to them.
- Prime dimensions are used here because the construction depends on properties of prime numbers. · level: research-level

<details><summary>Original abstract</summary>

For every prime $p\ge 29$, we construct an antipodal spherical $7$-design on $S^{p-1}$ with $42(p-1)(p+2)^2$ points. The construction uses eigenlines of finite Weil operators.

</details>

### [Extremal problems for graphs with bounded $k$-th binding number](https://arxiv.org/abs/2611.27699)
*Ao Fan, Ruifang Liu* · `math.CO` · arXiv:2611.27699v1 · relevance 0.12

- **In one sentence**: The paper determines the maximum number of edges and the maximum spectral radius among n-vertex graphs whose k-th binding number is below r, and characterizes the extremal graphs, generalizing known k=1 results.
- **In plain words**: This paper is about graphs, which are networks of points joined by lines. It asks: if a network is restricted so that a certain connectivity-type score (the k-th binding number) stays below a threshold, how many links can it have at most, and what shape does the best such network take? The authors give exact answers for both the number of links and a matrix-based measure of the network (its spectral radius), and they describe the networks that achieve these limits.
- **Why it matters**: Results of this kind tell us which structures are forced by a bound on a graph parameter, and the binding number is tied to whether a graph can be split into matching-type pieces. The authors say their method, which links neighborhood inequalities to the complement of the graph, may carry over to other Turán-type problems, but the text does not show how far that goes.
- **Background needed**: - A graph is a set of vertices joined by edges; its size is the number of edges.
- A perfect matching pairs up all vertices using disjoint edges; a k-factor is a spanning subgraph where every vertex has degree k.
- The binding number measures how many neighbours sets of vertices tend to have; a bound on it guarantees such pairings or factors exist.
- Turán-type problems ask for the largest number of edges a graph can have while avoiding a given property.
- The spectral radius is the largest eigenvalue of the adjacency matrix, a single number summarizing the graph's structure.
- The complement of a graph has the same vertices and exactly the edges that the original lacks. · level: research-level

<details><summary>Original abstract</summary>

The binding number of a graph, introduced by Woodall [J. Combin. Theory, Ser. B, 1973], is a central topic in structural and extremal graph theory. Recently, Chen et al. introduced the $k$-th binding number $\beta^k(G)$. Anderson [J. Combin. Theory, Ser. B, 1971] proved that every graph $G$ of even order with $\beta^1(G)\ge\frac43$ contains a perfect matching, and that the bound $\frac43$ is best possible. For $k\ge2$, Chen et al. proved that $\beta^k(G)\ge1$ guarantees a $k$-factor whenever $kn$ is even, and that the bound $1$ is best possible. The above facts reveal a fundamental distinction between the higher-order binding number and the classical binding number. This distinction makes extremal problems for graphs with bounded $k$-th binding number particularly intriguing. For positive integers $n,$ $k$ and $r$, we in this paper determine the maximum size and spectral radius among all graphs $G$ of order $n$ satisfying $\beta^k(G)<r$, and characterize the corresponding extremal graphs, respectively. In particular, when $k=1$, our results imply the corresponding extremal results of Fan and Lin [Electron. J. Combin., 2024] and Liu, Chen and Fan [Electron. J. Combin., 2026]. Our proofs develop a structural framework that relates higher-order neighborhood inequalities to the structure of the complements of graphs. This framework may provide an approach to Tur\'{a}n-type problem involving the $k$-th binding number, and the approach may be of independent interest.

</details>

## Numerical analysis

### [Convergence of a finite element Chorin projection method for the stochastic Navier--Stokes equations](https://arxiv.org/abs/2611.27969)
*Franziska Weber* · `math.NA` · arXiv:2611.27969v1 · relevance 0.16

- **In one sentence**: Convergence analysis of a fully discrete finite element Chorin projection scheme for the stochastic incompressible Navier--Stokes equations with multiplicative noise and homogeneous Dirichlet boundary conditions, showing convergence of a subsequence to a martingale solution in two and three dimensions.
- **In plain words**: This paper studies a computer method for simulating fluid flow (like water or air) that is incincompressible and also randomly disturbed by noise. The authors show that their numerical scheme produces velocity approximations with controlled moments, and that as the grid and time steps are refined under a coupling condition, a subsequence of the approximations converges to a random-solution notion called a martingale solution. They also run numerical tests in two dimensions with smooth and vortex-sheet starting conditions.
- **Why it matters**: Random forcing in fluid models arises in turbulence and geophysical settings, so having a proof that a practical computational scheme converges to a meaningful solution gives confidence in such simulations. The text does not indicate applications beyond this general context, and the scope is limited to the stated assumptions and coupling condition.
- **Background needed**: - Navier--Stokes equations: the standard equations describing viscous fluid motion.
- Incompressible: the fluid volume does not change, so the velocity field is divergence free.
- Stochastic / multiplicative noise: randomness whose strength depends on the state of the system.
- Finite element method: approximating a continuous problem by piecewise simple functions on a mesh.
- Chorin projection method: a splitting scheme that first advances velocity, then projects it back onto divergence-free fields using a pressure correction.
- Martingale solution: a weak notion of solution for random equations, defined on a new probability space if needed.
- Convergence of a subsequence: only some sub-sequence of the numerical approximations is shown to converge, not necessarily the whole sequence.
- Tightness and Aldous' criterion: tools from probability that ensure a family of random processes has convergent subsequences. · level: research-level

<details><summary>Original abstract</summary>

We analyze a fully discrete finite element projection method for the stochastic incompressible Navier--Stokes equations with homogeneous Dirichlet boundary conditions and multiplicative noise. We show solvability and uniform moment estimates for the intermediate and the corrected velocity approximations under the assumption that the initial data is square-integrable and divergence free, and that the deterministic forcing term is bounded in $L^{q}(0,T;H^{-1}(D))$ for a sufficiently large $q$. Under standard stability and approximation assumptions on the finite element spaces and a coupling condition on the spatial and temporal discretization parameters, we prove convergence of a subsequence to a martingale solution of the stochastic Navier--Stokes equations. The analysis combines the complementary spatial and temporal estimates of the predicted and the corrected velocity approximations and uses the numerical dissipation to identify their common limit. We establish tightness of the piecewise constant temporal interpolations of the velocity field approximations using Aldous' criterion combined with the uniform discrete moment estimates. The convergence result holds in two and three space dimensions as it does not rely on any additional regularity of the limiting martingale solution beyond the one naturally available from the energy inequality. Finally, we demonstrate the performance of the scheme in numerical experiments in two space dimensions for smooth and vortex sheet initial data.

</details>

### [A Validation-Driven Bilevel Optimization Method for Mesh-Free PDE Solvers and Its Error Analysis](https://arxiv.org/abs/2611.27347)
*Yongcun Song, Shangzhi Zeng, Jin Zhang et al.* · `math.OC` · arXiv:2611.27347v1 · relevance 0.14

- **In one sentence**: The paper proposes a validation-driven bilevel optimization framework for tuning design parameters of mesh-free PDE solvers (Kansa, random feature/extreme learning machine, and physics-informed neural network methods), with an approximate implicit hypergradient method for nonlinear PDEs and error bounds for the resulting approximations.
- **In plain words**: Mesh-free methods solve equations that describe physical systems by fitting a flexible formula at scattered sample points instead of on a grid. Their accuracy depends on several settings chosen beforehand, and this paper treats choosing those settings as an optimization problem: coefficients are fitted on training points, while the settings are chosen to minimize errors on separate held-out validation points. The authors describe a cheaper way to estimate how the validation error changes with the settings for nonlinear equations, and they derive bounds on the resulting errors.
- **Why it matters**: Choosing solver settings is often done by trial and error, and the text says existing strategies are largely tied to particular solver classes; a method meant to work across several solver types could be useful. The text reports experiments on several nonlinear PDEs, including a high-dimensional one, but the abstract alone does not show how large the gains are or how it compares with other tuning methods.
- **Background needed**: - PDE (partial differential equation): an equation relating a function to its rates of change, used to model heat, waves, fluids and similar systems.
- Mesh-free solver: a method that works from scattered sample points rather than a fixed grid or mesh.
- Collocation residual: the amount by which a candidate solution fails to satisfy the equation at a sample point.
- Bilevel optimization: a nested problem where an outer choice (here, solver settings) is made by judging the result of an inner fitting step.
- Validation set: held-out points used to check performance on data not used for fitting.
- Hypergradient: the gradient of the outer objective with respect to outer settings, needed to tune them by gradient-based methods.
- Gauss-Newton method: an iterative method for nonlinear least-squares fitting; "damped" means its steps are shrunk for stability.
- Adjoint system: an auxiliary linear system used to compute hypergradients efficiently; here it is ill-conditioned and indefinite, meaning it is numerically hard to solve.
- Preconditioning and minimum residual iterations: standard numerical techniques for solving difficult linear systems approximately.
- Kansa, random feature / extreme learning machine, and physics-informed neural network solvers: three families of mesh-free methods. · level: research-level

<details><summary>Original abstract</summary>

Mesh-free partial differential equation (PDE) solvers construct discrete systems from residuals at sampled points. These solvers fit coefficients in a parameterized trial representation and select solver-design parameters governing the representation, training-residual weighting, and regularization. These parameters strongly affect solution accuracy, yet existing selection strategies are largely tailored to particular solver classes. To address this limitation, we formulate a unified validation-driven bilevel optimization framework applicable across different solver classes, in which the lower level fits coefficients using training collocation residuals, while the upper level selects solver-design parameters using held-out validation residuals. For nonlinear PDEs, however, solving the nonlinear lower-level problem to high accuracy is costly, while the adjoint system is typically ill-conditioned and indefinite. To address this issue, we propose an efficient implicit hypergradient method that approximates the lower-level response using finite, warm-started damped Gauss-Newton (GN) updates. For the adjoint solve, we use the damped GN matrix to compute an initial adjoint and to precondition a finite number of minimum residual iterations. To quantify the errors introduced by these approximations, we derive local hypergradient error bounds that separate the contributions of the finite lower-level solve, adjoint damping, and the final adjoint residual. Combining this analysis with validation sampling bounds and residual stability, we relate validation residuals to PDE solution accuracy and establish error bounds for the computed PDE solution. Numerical experiments on several nonlinear PDEs, including a high-dimensional problem, demonstrate the accuracy and efficiency of the proposed method across Kansa, random feature and extreme learning machine, and physics-informed neural network solvers.

</details>

## Logic and foundations

### [Bridging Badiou's Gaps: Topos Theory and the Bodies of Mathematical Expression](https://arxiv.org/abs/2611.27280)
*Antti Veilahti* · `math.CT` · arXiv:2611.27280v1 · relevance 0.11

- **In one sentence**: A philosophical reconstruction of Alain Badiou's use of topos theory (forcing, Kripke-Joyal semantics, and his typology of change) reframed in categorical terms, arguing that a topos can be read as a "body of mathematical expression" and that Badiou's reduction to localic, set-theoretic form loses conceptual content.
- **In plain words**: The paper revisits how the philosopher Alain Badiou used a branch of advanced mathematics, topos theory, in his two major books. The author argues that Badiou shrank this mathematics to a narrow set-theoretic version, and that a fuller categorical version changes how his ideas about subjects, change, and events can be understood. The paper says it introduces no new mathematical results; its aim is to show what is lost when the mathematics is reduced in this way.
- **Why it matters**: It connects the philosophy of mathematics, the reception of set theory and category theory, and debates over whether logic should be treated as foundational. Readers interested in how Badiou's philosophy depends on specific mathematical choices may find it useful; the text itself gives no evidence about how widely its reading is accepted.
- **Background needed**: - Set theory: the standard foundation in which mathematical objects are built from collections (sets).
- Category theory: a framework that studies objects through the maps between them rather than their inner contents.
- Topos (plural topoi): a category behaving somewhat like a generalized universe of sets, with its own internal logic; the text notes Johnstone's description of it as a "universe of discourse."
- Localic form: a simpler, order-based version of a topos, which the author argues Badiou relied on.
- Forcing: Paul Cohen's technique for building new mathematical models in which some statement is true or false, used to settle questions such as the continuum hypothesis.
- Kripke-Joyal semantics: a way of interpreting logic inside a topos, analogous to truth conditions in a model.
- Badiou's concepts: "event," "subject," "body," and "democratic materialism," from Being and Event (2006 English edition of 1988 work) and Logics of Worlds. · level: research-level

<details><summary>Original abstract</summary>

This article develops a second stage of an argument begun in 2013, revisiting Alain Badiou's use of topos theory in Being and Event and Logics of Worlds. The previous article diagnosed Badiou's reduction of topos theory to its atomistic, localic form as the scientific scapegoat in his attack on 'democratic materialism'. Now I ask what follows when this logicist illusion is dispelled and the categorical alternative is taken seriously, particularly with respect to forcing, semantic expression, and mathematical subjectification that constitute the key elements of Badiou's earlier work. I thus reconstruct Badiou's own arguments in a corrected form, while transferring them to a categorical framework. The aim is not to introduce new mathematical results, but to identify what is conceptually lost through their reduction to set-theoretic formalism. In particular, I describe Cohen's forcing argument in the context of Grothendieck topoi and Kripke-Joyal semantics, thereby explicating the geometric structures implicit in Badiou's thinking. This reconstruction further brings into view a different way of understanding Badiou's concepts of subject, body, and change. Rather than treating a topos as merely a formal container for mathematical objects, I propose reading it as a body of mathematical expression, aligning with Johnstone's characterization of a topos as a 'universe of discourse'. At the same time, the geometrization of logic allows Badiou's own four-fold typology of change - when applied to topos theory itself as a mathematical 'event' - to be anchored to various historical definitions of a topos. In this way, the article bridges Badiou's two major works while clarifying how his own limited expression of mathematical formalism embodies his 'dialectical', ultimately singular concept of the event, and the way it clouds his philosophical understanding of locality and temporality.

</details>

### [The Power Of Enumerations](https://arxiv.org/abs/2611.27239)
*Karthik Ravishankar* · `math.LO` · arXiv:2611.27239v1 · relevance 0.08

- **In one sentence**: The paper studies the computational strength of enumeration reducibility for generic and random sets, showing limits on what enumerations of typical sets can compute and mapping which Turing degrees can sit above quasiminimal enumeration degrees.
- **In plain words**: This is work in computability theory, which asks how much information one infinite binary sequence can extract from another. The authors look at "enumerations" (a looser way of extracting information than step-by-step computation) applied to sets that are "typical" in a precise sense, such as generic or random sets. They find that such enumerations can recover typical sets at low levels but not at higher ones, and they settle a question of Slaman and Sorbi by showing some quasiminimal degrees have no minimal Turing degrees above them.
- **Why it matters**: The results sharpen the boundary between what typical sets can and cannot do, and they answer an open question posed by named researchers in the area. The text does not say more about wider applications, so the broader significance is unclear from this abstract alone.
- **Background needed**: - Turing degree: a measure of how hard a set of numbers is to compute from another set; degrees form a structure that is studied in its own right.
- Enumeration reducibility: a weaker way to extract information, based on listing (enumerating) the elements of a set rather than deciding membership step by step.
- Generic and random sets: sets that avoid all "definable" special patterns (generic) or pass all statistical tests of typicality (random); the levels 1, 2, 3 refer to how many layers of definability are avoided.
- Weak n-random / n-generic: variants of these notions at specific levels of the hierarchy.
- Quasiminimal degree: an enumeration degree that is non-total with no non-total degrees strictly below it, roughly "close to the bottom" among non-computable-in-the-usual-sense degrees.
- Minimal Turing degree: a nonzero Turing degree with nothing nonzero strictly beneath it.
- PA degrees: degrees that compute solutions to a certain combinatorial principle (Peano arithmetic's completeness-type problem).
- Dimension 1 sets: sets of maximal information density in a specific measure-type sense. · level: research-level

<details><summary>Original abstract</summary>

We study the computational strength of enumerations of generic and random sets, particularly its interplay with computing these `typical' sets. We show that, while enumerations of $2$-generics can compute $2$-generics, this fails at higher levels---every $3$-generic has an enumeration which computes no weak $3$-generic. The analogous statement holds for randoms---every weak $2$-random has an enumeration which computes no $1$-random. We then analyze the total degrees above a quasiminimal enumeration degree, showing certain restrictions as well as certain positive results on the possible Turing degrees in such a cone. This answers a question of Slaman and Sorbi, by showing that there are quasiminimals with no minimal Turing degrees above them. We also show that while every total degree above some quasiminimals compute dimension $1$ sets, the total degrees above any quasiminimal fail to be a subset of the PA degrees.

</details>

## Mathematical physics

### [Brane Tilings and Polygons with Two Interior Points](https://arxiv.org/abs/2611.27861)
*Rak-Kyeong Seong* · `hep-th` · arXiv:2611.27861v1 · relevance 0.11

- **In one sentence**: A complete classification of brane tilings, quiver gauge theories, and their mesonic moduli spaces for toric Calabi-Yau 3-folds whose toric diagrams are convex lattice polygons with exactly two interior lattice points.
- **In plain words**: This paper is a catalogue in theoretical physics and geometry. It looks at a specific family of shapes (convex polygons with exactly two points inside them on a grid) that encode certain curved higher-dimensional spaces used in string theory. For each shape, the authors list every matching physics model (called a "toric phase") and the associated data, finding 45 shapes and 323 models in total.
- **Why it matters**: The text presents this as a complete classification, which is a useful reference for researchers studying how geometry determines physical theories. Its connection to broader physics or mathematics is not spelled out in the text, so the wider significance is unclear from this abstract alone.
- **Background needed**: - Toric Calabi-Yau 3-fold: a six-real-dimensional curved space, built from a polygon on a grid, studied in string theory.
- Toric diagram: a lattice polygon whose interior points and shape encode the geometry.
- Brane tiling (dimer model): a tiling of a torus by hexagon-like cells that encodes a gauge theory.
- Quiver gauge theory: a diagram of nodes (gauge groups) and arrows (matter fields), with a superpotential describing interactions.
- 4d N=1 supersymmetry: a four-dimensional physics framework with partial supersymmetry.
- Mesonic moduli space: the space of gauge-invariant combinations of fields, described via a Hilbert series and plethystic logarithm (counting tools for generators and relations).
- GL(2,Z) and lattice translations: integer changes of coordinates that identify equivalent polygons. · level: research-level

<details><summary>Original abstract</summary>

We fully classify the brane tilings and the 4d N=1 supersymmetric quiver gauge theories corresponding to toric Calabi-Yau 3-folds whose toric diagrams are convex lattice polygons with two interior lattice points. There are 45 such polygons up to GL(2,Z) transformations and lattice translations: 5 triangles, 19 quadrilaterals, 16 pentagons and 5 hexagons. We identify all 323 toric phases corresponding to these toric Calabi-Yau 3-folds. For every toric phase, we present the brane tiling with its quiver and superpotential, the perfect matching matrix and the F- and D-term charge matrices. For each brane tiling, we study the mesonic moduli space of the corresponding abelian 4d N=1 theory through its Hilbert series and plethystic logarithm, and identify its generators and their leading relations. We also identify the mesonic global symmetry for each brane tiling and determine the superconformal U(1)R charges.

</details>

### [The moments and asymptotic spectral distribution of the Grassmannian ensemble](https://arxiv.org/abs/2611.27914)
*Aryan Gadhave, Asghar Ghorbanpour, Liam Hickey et al.* · `quant-ph` · arXiv:2611.27914v1 · relevance 0.07

- **In one sentence**: The paper computes all tracial moments and mixed reduced-state moments of partial traces of projections onto random subspaces (Grassmannian ensemble) via Weingarten calculus, proves almost-sure convergence of the spectral distribution to a rescaled Marchenko-Pastur law, gives an alternative free-probability proof, and expands the average entanglement entropy asymptotically.</one_liner>
<parameter name="plain">The paper studies random "density matrices," which are mathematical descriptions of the state of a quantum system split into two parts. These are built by picking a random subspace of a combined two-part space and tracing out one part. The authors compute the statistics of these random objects exactly and show that, for large systems, the spread of their eigenvalues settles into a predictable shape.
- **Why it matters**: Random-state models like this are used to ask what a "typical" quantum state looks like, including how much entanglement it carries, so exact results are useful benchmarks. The text supports these claims as mathematical results; any link to specific physics applications is not spelled out in the given text.
- **Background needed**: - Density matrix: a matrix describing a quantum state; its eigenvalues are nonnegative and sum to one.
- Partial trace: averaging out one subsystem to get the state of the other.
- Grassmannian: the space of all subspaces of a fixed dimension; a random point is a random subspace.
- Weingarten calculus: a method for integrating polynomial functions of random unitary matrices.
- Marchenko-Pastur law: the limiting eigenvalue distribution of certain large random matrices.
- Asymptotic freeness: a notion of independence for large random matrices from free probability theory.
- Entanglement entropy: a measure of how strongly two subsystems are correlated quantum mechanically. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study random density matrices constructed by taking partial traces of projections onto random subspaces of a bipartite Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_{B}$ distributed according to the pushforward measure of the action of the unitary group on the Grassmannian $\text{Gr}_{n}(\mathcal{H}_A \otimes \mathcal{H}_{B})$. This ensemble models a `typical' quantum subspace. All tracial moments of the density operator, as well as mixed tracial moments of reduced density operators, are computed explicitly using Weingarten calculus. There are several consequences of these results. In particular, we prove that the empirical spectral distribution of the density operator converges almost surely to a rescaled Marchenko-Pastur law. We also prove that this ensemble can be written as a sum of asymptotically free random density operators, leading to an alternative proof of the convergence of the spectral distribution. Finally, we compute the asymptotic expansion of the average entanglement entropy.

</details>

## Optimization and control

### [Small noise limit for Entropic Variational Mean-Field Games](https://arxiv.org/abs/2611.27695)
*Alessandro Cosenza, Luca Nenna* · `math.AP` · arXiv:2611.27695v1 · relevance 0.25

- **In one sentence**: The paper proves that the small-noise limit of second-order variational mean-field games, studied through an entropy-minimization (Lagrangian) formulation, Gamma-converges to a deterministic first-order problem, and derives a first-order energy expansion for the original Eulerian problem that selects among deterministic minimizers.
- **In plain words**: The paper studies models of many interacting agents that each choose a path while being pushed by random noise, and asks what happens as the noise is made very small. It shows that these noisy models settle, in a precise mathematical sense, onto a simpler deterministic version of the problem. The authors also note that this gives a new route to the known fact that a noisy transport problem (the Schrödinger problem) converges to ordinary optimal transport.
- **Why it matters**: The work connects the theory of mean-field games (large populations of rational agents) with entropic optimal transport, and it also says which deterministic solution is singled out when several are possible. The text does not describe applications beyond these mathematical connections.
- **Background needed**: - Mean-field game: a model of a very large number of agents, each optimizing a cost while reacting to the average behavior of the rest.
- Second-order (noisy) versus first-order (deterministic): the noisy version includes diffusion; the deterministic version has none.
- Small-noise Gamma-limit: a standard way to show that a family of problems converges to a limit problem, including convergence of minimizers.
- Entropy minimization / Schrödinger problem: a regularized optimal transport problem where a relative-entropy penalty plays the role of noise.
- Optimal transport: finding the cheapest way to move one distribution of mass into another.
- Eulerian vs Lagrangian: describing a flow by fields at fixed points in space versus by tracking individual paths. · level: research-level

<details><summary>Original abstract</summary>

We study second order variational mean-field games with quadratic Hamiltonian. In analogy with entropic optimal transport, Benamou, Carlier, Di Marino and the second author recently proposed an entropy-minimization formulation of the problem, which could be interpreted as the Lagrangian counterpart of the classical Eulerian approach. We investigate the small-noise $\Gamma$-limit for the Lagrangian entropy-minimization formulation and establish $\Gamma$-convergence of second order mean-field games towards their deterministic first order counterpart. This also translates into another (dynamical) proof of the convergence of the Schr\"odinger problem to optimal transport. Moreover, we study the original Eulerian problem and prove a first order energy expansion, which establishes a selection principle for minimizers of the deterministic problem.

</details>

### [Approximating technique for the solution to the ${H}^{\infty}$ -optimal control problem](https://arxiv.org/abs/2611.27520)
*Gabriela Marinoschi* · `math.AP` · arXiv:2611.27520v1 · relevance 0.23

- **In one sentence**: The paper proposes an approximation scheme that builds a sequence of infinite-dimensional systems whose H-infinity optimal control solutions converge to that of the original problem, with an example computing the associated Riccati equation and feedback controller.
- **In plain words**: The paper is about designing a feedback controller that keeps a system stable even when it is affected by unknown disturbances or modelling errors. The exact solution to this kind of problem is hard to compute, so the author builds a series of simpler, approximate versions of the system. The text states that the solutions to these simpler problems converge to the solution of the original problem, and it ends with a worked example.
- **Why it matters**: Robust control, the goal of keeping a system well-behaved under uncertainty, matters for engineering systems such as aircraft, machines and industrial processes. The paper is a follow-up to earlier work by the same author, and its main value is a computational route to a hard problem; the text does not indicate how it performs on large practical systems.
- **Background needed**: - Feedback controller: a rule that measures a system's state and adjusts its inputs to steer it.
- Robust stabilization: keeping a system stable despite disturbances or uncertainty in its model.
- H-infinity control: a standard robust-control framework that limits how much a disturbance can amplify the system's output, measured in worst case.
- Riccati equation: a matrix equation whose solution gives the controller in many linear control problems.
- Infinite-dimensional system: a system whose state is a function (for example, a temperature spread over a rod) rather than a finite list of numbers; approximations reduce it to finite or simpler forms.
- Convergence: the approximate solutions get closer and closer to the true solution as the approximation is refined. · level: research-level

<details><summary>Original abstract</summary>

This paper continues the results published in [G. Marinoschi, Appl. Math. Optimiz. 94:44, 1-29, 2026], by presenting an approximating method of calculating the solution to the $H^{\infty }$-optimal control problem, which solves the robust stabilization of a system by a feedback controller, and to the associated Riccati equation. This method generates a sequence of infinite dimensional systems approximating the original system and the solution to the approximating $H^{\infty }$-optimal control problem is proved to converge to the solution of the original $H^{\infty }$-optimal control problem. An example for calculating the solution to the Riccati equation and the feedback controller is provided at the end.

</details>

## Statistics theory

### [Pathwise Factorization and Uncertainty Quantification for Impedance Obstacles with Random Boundaries](https://arxiv.org/abs/2611.26761)
*George Pelekanos, Koung Hee Leem* · `math.NA` · arXiv:2611.26761v1 · relevance 0.09

- **In one sentence**: A factorization method for locating two-dimensional impedance obstacles with random boundaries from finitely many noisy multistatic measurements, with finite-sample guarantees, simultaneous confidence bands, and a combined-field integral equation solver.
- **In plain words**: The paper studies how to find the shape and location of a hidden object that scatters sound waves when its edge is not fixed but random, using only a limited set of noisy measurements. The authors build a sampling-type reconstruction method and prove that its statistical error can be controlled for a finite amount of data. They also use it to give confidence bands and a estimate of the probability that a given point lies inside the random object.
- **Why it matters**: Reconstructing objects from scattered waves with honest error bars matters for imaging and nondestructive testing, where a single answer is less useful than a stated level of uncertainty. The text reports a coverage check against a high-accuracy Monte Carlo reference, but its practical reach beyond this setting is not stated.
- **Background needed**: - Acoustic scattering: how sound waves bounce off an object and what the far-field measurements record.
- Impedance obstacle: an object whose surface partly absorbs or reflects waves, described by a boundary condition.
- Factorization method: an inverse-scattering technique that tests sampling points against an operator built from the measurements to decide whether each point is inside the object.
- Multistatic data: measurements taken from several transmitter and receiver positions.
- Uncertainty quantification: attaching confidence statements to reconstructed quantities, such as confidence bands and variance estimates.
- Finite-sample guarantee: a bound on error that holds for a specific, limited amount of data rather than only as the data grow without limit.
- Bi-Lipschitz domain: a shape whose boundary is not too wiggly or sharp, which keeps the mathematics well behaved.
- Monte Carlo reference: a large random-sampling computation used as the accurate benchmark. · level: research-level

<details><summary>Original abstract</summary>

We develop a factorization method with finite-sample statistical guarantees for two-dimensional acoustic scattering by impedance obstacles whose boundary is random and whose data are finitely many noisy multistatic measurements. In the two-dimensional far-field normalization, the symmetrization must act on a phase-rotated far-field operator; we prove the optical and range identities for every realization of a compact family of uniformly bi-Lipschitz domains, with jointly measurable regularized indicators. A quadrature-weighted finite-sample analysis separates angular approximation, measurement noise, test-vector error, and regularization, and yields a consistency theorem for empirical means and variances, joint in all data parameters. Bounded indicators admit simultaneous confidence bands, a diagonal threshold recovers the probability that a sampling point lies in the random obstacle, and a nested design yields unbiased variance components. Computations use a combined-field integral equation proved invertible at all frequencies, and the finite-grid guarantees are examined in a coverage study against a high-accuracy Monte Carlo reference.

</details>

### [An Asymptotic One-Sample Surrogate for Non-Gaussian ERM with General Convex Regularization](https://arxiv.org/abs/2611.27754)
*Tianjian Zhang, Cosme Louart, Malik Tiomoko et al.* · `math.ST` · arXiv:2611.27754v1 · relevance 0.07

- **In one sentence**: The paper builds a one-Gaussian-vector surrogate for convex empirical risk minimization with non-Gaussian features and nonsmooth penalties, calibrates it to the true joint feature-label law, and proves that the ERM minimizer and surrogate agree in normalized means, prediction variances, and prediction and classification risks under a Poincaré inequality and regularity conditions.
- **In plain words**: The paper studies a common way of fitting statistical models: pick the settings that minimize an average error on data, possibly with a penalty that keeps the answer simple. Real data are not Gaussian (bell-curve shaped), which makes exact analysis hard, so the authors replace the problem with a simpler stand-in built from a single Gaussian random vector. They show that this stand-in can be tuned to the real data distribution and that its predictions match those of the real fitted model in the averages and spreads that matter for prediction and classification error.
- **Why it matters**: Having a tractable Gaussian stand-in for penalized fitting methods such as the Lasso lets researchers compute prediction and classification risk formulas for realistic, non-Gaussian data. The text does not say how far the results extend beyond the stated assumptions, so the practical reach is uncertain.
- **Background needed**: - Empirical risk minimization (ERM): choosing model settings that minimize average error on a training sample.
- Convex penalty: an added cost that discourages complicated solutions; the Lasso uses an absolute-value penalty that pushes some settings exactly to zero.
- Gaussian (normal) distribution: the bell-curve distribution, which is mathematically convenient.
- Asymptotic: describing behavior as the amount of data grows large.
- Poincaré inequality: a condition on a distribution that limits how spread out or uneven its fluctuations can be; used here to get the Gaussian approximation.
- Calibration: adjusting the surrogate's coefficients so it matches the real data's joint behavior.
- Hamilton-Jacobi argument: a technique from PDE and optimization theory; here it is used to compare the two minimizers.
- Anti-concentration: a condition ensuring projections of the features are not too concentrated on small sets. · level: research-level

<details><summary>Original abstract</summary>

We study convex empirical risk minimization (ERM) with non-Gaussian features and nonsmooth penalties through a surrogate driven by a single Gaussian vector. The surrogate preserves the penalty and calibrates its coefficients using the actual joint law of the feature-label model. We prove that this population calibration exists and is unique. We prove a Gaussian approximation for fresh prediction scores when the data satisfy a Poincar\'e inequality. Together with regularity conditions on the losses, this approximation yields agreement between the ERM minimizer and its surrogate in normalized means and prediction variances, as well as formulas for prediction and classification risks. The result covers general uniformly strongly convex penalties and pure Lasso under projection anti-concentration. The core proof relies on a cavity Hamilton-Jacobi argument that compares the main statistics of the two minimizers without differentiating the penalty.

</details>

## Statistical methods and applications

### [Hidden Semi-Markov Models for Fully Functional Time Series](https://arxiv.org/abs/2611.26838)
*Jake Hoover, Adam B Kashlak, Giseon Heo* · `stat.ME` · arXiv:2611.26838v1 · relevance 0.23

- **In one sentence**: The paper extends hidden semi-Markov models, with data-driven sojourn times, to fully functional time series, embeds the hidden semi-Markov chain in a larger Markov chain so that Baum-Welch and Viterbi fitting apply, and works in the setting of Gaussian measures on locally convex topological vector spaces, illustrated on pediatric EEG signals from overnight polysomnography.
- **In plain words**: The paper studies data where each observation is an entire curve, such as a brain-wave recording, and where an unseen "state" (for example, a sleep stage) switches over time. The standard model assumes each state's duration fades away at a fixed rate, which can be too restrictive. The authors let the time spent in each state follow a more flexible duration distribution, such as a negative binomial, or leave it unspecified, and show how to fit this model with established algorithms. They apply it to overnight pediatric EEG recordings.
- **Why it matters**: Modeling how long a hidden state lasts matters in fields that analyze biological signals like sleep EEG, where stages have realistic durations. The text does not report fitting performance or comparisons against the standard model, so its practical advantage is not established here.
- **Background needed**: - Time series: data recorded in sequence over time.
- Functional time series: each observation is a whole curve or function, not a single number.
- Hidden Markov model: a model where an unseen state drives the data and the state changes by a simple chance rule that depends only on the current state.
- Semi-Markov extension: lets the time spent in a state follow an arbitrary duration distribution (the "sojourn time").
- Negative binomial distribution: a flexible count distribution often used for durations.
- Baum-Welch and Viterbi algorithms: standard procedures for estimating model parameters and for finding the most likely hidden state sequence.
- Gaussian measures on locally convex spaces: a probability framework for random curves in very general function spaces.
- Polysomnography: an overnight sleep study recording brain waves and other signals. · level: research-level

<details><summary>Original abstract</summary>

Functional time series have a wide range of practical applications to modeling complex datasets such as Electroencephalogram (EEG) and other biological signals. Often latent states are hidden within the data dictating how a system is behaving and changing over time. The Hidden Markov Model (HMM) is one common and highly applicable latent state space model where the hidden state sequence evolves as a Markov chain. While the HMM has had much success modeling discrete, multivariate, and fully functional time series, it is also restricted by the Markov property which causes hidden states to persist only at geometrically decaying rates. This work investigates the implementation of hidden semi-Markov models for modeling fully functional time series data. This allows for the hidden state sequence to persist in a given state for a data-driven sojourn time, which can be parametrized by a discrete distribution (e.g. negative binomial) or left non-parametric. For efficient fitting of such a model, the hidden semi-Markov chain is embedded into a larger state space Markov chain and classic methods like the Baum-Welch and Viterbi algorithms are applied. We furthermore consider functional time series in the general setting of Gaussian measures in locally convex topological vector spaces. This is applied to a time series of pediatric EEG signals collected via overnight polysomnography.

</details>

### [A generalized Bayesian method for identifying local and global changepoints in dynamic network data](https://arxiv.org/abs/2611.26955)
*Yuhui Wang, Michael Jauch, Joshua Daniel Loyal* · `stat.ME` · arXiv:2611.26955v1 · relevance 0.10

- **In one sentence**: A generalized Bayesian changepoint method with a multinomial log loss and a low-rank, sparsity-inducing prior detects local and global structural shifts in dynamic networks, with Pólya-Gamma Gibbs sampling for posterior computation.
- **In plain words**: The paper addresses how to spot the moments when a network that changes over time, such as who emails whom or which countries are in conflict, shifts its overall pattern. The authors use a statistical method that looks at both the full record of connections and simple summary measures of the network, and it reports where change points likely occur, with uncertainty attached. The text reports that simulations on benchmark network models show it is often more accurate and flexible than competing methods, and it is applied to an email network and an international conflict network.
- **Why it matters**: Dynamic network data appear in communication, social, and political studies, where knowing when a network's structure changes can matter. The method's stated appeal is its uncertainty quantification and its linear computational cost in the number of observed edges, though the text does not say how it performs on data beyond the cases it describes.
- **Background needed**: - Network data: a set of nodes (people, countries) and edges (links between them), often stored as an adjacency matrix (a grid marking which pairs are linked).
- Changepoint analysis: detecting the time points where the statistical behavior of a sequence of observations shifts.
- Bayesian inference: combining prior beliefs with data to get a posterior distribution that expresses uncertainty about unknown quantities.
- Generalized Bayesian method: a Bayesian-style update that uses a chosen loss function instead of a full probability model of the data, so it does not assume a specific data-generating process.
- Low-rank structure and sparsity: assumptions that the underlying patterns can be described by a few hidden factors and that most parameters are zero.
- Gibbs sampler and Pólya-Gamma augmentation: computational techniques for drawing samples from a complicated posterior distribution. · level: research-level

<details><summary>Original abstract</summary>

We introduce a generalized Bayesian approach to multiple changepoint analysis in dynamic network data based on a multinomial log loss function and a prior distribution that imposes low-rank structure and sparsity on the model parameters. The method can detect local and global changes in network structure by incorporating information from both the full adjacency matrices and network summary statistics. Moreover, the proposed method is agnostic to the true data-generating process. From the generalized posterior distribution, we can make simultaneous inferences with meaningful uncertainty quantification about the locations of changepoints as well as deduce the network attributes and summary statistics that characterize them. For posterior simulation, we develop an efficient Gibbs sampler based on P\'olya-Gamma data augmentation with a computational cost that grows linearly with the number of observed edges in the dynamic network. Simulations across several benchmark network models show that the proposed method is often more accurate and flexible than competitors. We demonstrate the practical value of the method through applications to an email communication network and an international conflict network.

</details>

## AI industry news

### [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence)
** · `openai.com` · OpenAI News · relevance 0.11

- **In one sentence**: A news piece arguing that perplexity, a standard language-model metric, could give developers a shared yardstick for judging emerging AI capabilities.
- **In plain words**: This short article looks at perplexity, a score used to measure how well an AI language model predicts text. It suggests the score might help developers agree on a common way to judge what new AI systems can do. The text provided is only a one-line summary, so it does not show specific experiments, numbers, or results.
- **Why it matters**: Agreeing on how to measure AI abilities matters for comparing models and tracking progress. The text does not say whether this idea has been adopted, so its practical impact is unclear.
- **Background needed**: - Language model: an AI system trained to predict the next word in a piece of text.
- Perplexity: a score for how "surprised" a model is by real text; lower usually means better prediction.
- Evaluation benchmark: a standard test used to compare AI systems fairly.
- Emerging capabilities: new skills that appear as models grow larger or are trained differently. · level: intermediate

<details><summary>Original abstract</summary>

How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

</details>

### [Why data centers are at the center of the Big Tech backlash](https://techcrunch.com/2026/11/22/why-data-centers-are-at-the-center-of-the-big-tech-backlash/)
*Anthony Ha* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: A short piece previewing journalist Paris Marx's book "Hyperscale," which examines the growing public pushback against Big Tech and the data centers that power it.
- **In plain words**: This article looks at why huge computer facilities called data centers have become a focus of anger toward large technology companies. It introduces journalist Paris Marx's new book, "Hyperscale," in which he discusses the topic. The text is brief and mainly describes the book rather than reporting new facts or findings.
- **Why it matters**: Data centers are the physical base for AI and cloud services, so local and political reactions to them may affect where and how that infrastructure gets built. The text gives only a short preview, so it does not show the specific arguments or evidence the book makes.
- **Background needed**: - Data center: a large building full of servers that store and process internet, cloud, and AI computing.
- Hyperscale: a term for the very largest data centers, run by a few giant cloud companies such as Amazon, Microsoft, and Google.
- Big Tech backlash: public criticism of large technology companies over issues like power use, land, jobs, and their influence.
- Paris Marx: a journalist and host of a technology-critique podcast, known for writing about the business side of tech.
- The article is a short author preview; the full book's claims are not described in the text. · level: introductory

<details><summary>Original abstract</summary>

Journalist Paris Marx unpacks his new book "Hyperscale."

</details>

### [Anthropic’s 7 founders cashed out nearly $2B in record-breaking IPO](https://techcrunch.com/2026/11/19/anthropics-7-founders-cashed-out-nearly-2b-in-record-breaking-ipo/)
*Julie Bort* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: A short news item reporting that Anthropic's seven founders each received about $280 million at an upgraded $83-per-share IPO price, which the company says raised nearly $105 billion.
- **In plain words**: This is a news item about Anthropic, an AI company, going public by selling shares on the stock market (an IPO, or initial public offering). The article says the founders each made about $280 million from selling shares at the raised price of $83 per share, and that the company itself took in nearly $105 billion.
- **Why it matters**: It is a notable financial event for the AI industry, since the reported sums are very large. The text gives only the headline figures, so it says nothing about the company's products, research, or future earnings.
- **Background needed**: - An IPO is when a private company first sells its shares to the public on a stock exchange.
- Shares are units of ownership; the price per share times the number sold sets the total raised.
- Founders often sell some of their own shares at an IPO, which is what "cashed out" means here.
- The article gives only the per-founder amount, the price, and the total raised; it does not explain the share count, lock-up rules, or valuation.
- Figures come from the article itself and have not been checked against filings. · level: introductory

<details><summary>Original abstract</summary>

At the upgraded $83/share IPO price, Anthropic's seven founders each pocketed $280 million, while the company nabbed nearly $105 billion.

</details>

### [Introducing harness adapters: adapt your favorite model to your harness to improve performance and cost](https://huggingface.co/blog/harness-adapters-at-scale)
** · `huggingface.co` · Hugging Face - Blog · relevance 0.06

- **In one sentence**: A news item announcing "harness adapters," a method for tuning a chosen AI model to work with a specific surrounding software setup (the "harness") with the stated aim of better performance and lower cost.
- **In plain words**: The article is about a way to make an AI model fit better into the software wrapper that runs it, which is often called a harness. The title says the goal is better results and lower running costs, but the article body is empty, so I cannot say what was built, how it works, or how well it performed.
- **Why it matters**: Getting an AI model to work well inside its surrounding tools is a practical issue for anyone building AI products, since cost and reliability depend on it. Without the article text, I cannot confirm any results or claims beyond the title.
- **Background needed**: - AI model: a large program trained on data that generates text or takes actions in response to input.
- Harness: the surrounding software that feeds a model prompts, tools, and data and collects its outputs.
- Adapter: a small add-on that adjusts a model so it works with a particular setup, without retraining the whole model.
- Performance and cost: how accurately or usefully the system works, and how much computing it consumes to do so.
- Note: the source text is missing, so this brief relies only on the title. · level: intermediate

<details><summary>Original abstract</summary>



</details>

### [The fallout from Nvidia’s Jensen Huang scandal continues](https://techcrunch.com/podcast/the-fallout-from-nvidias-jensen-huang-scandal-continues/)
*Theresa Loconsolo, Anthony Ha, Kirsten Korosec, Tim De Chant* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.04

- **In one sentence**: A news piece reporting that Nvidia, despite turmoil after it reportedly ousted CEO Jensen Huang, posted healthy earnings growth, will stop selling its H200 chips in China, and dismissed some unspecified calls to act.
- **In plain words**: The article covers Nvidia, the company that makes the chips used to train and run AI systems. It says the company is dealing with the fallout from removing its long-time chief executive, Jensen Huang, yet still reported strong growth in its latest earnings report. It also says Nvidia will stop selling its H200 chips in China.
- **Why it matters**: Nvidia is a central supplier of AI hardware, so changes in its leadership and its China sales can affect the wider AI industry. The text is short and cut off, so it does not explain why Huang was ousted, what the calls were, or the reasons for the China decision; those details would be needed to judge the impact.
- **Background needed**: - Nvidia designs graphics processors (GPUs) that are the main hardware for building and running AI models.
- Jensen Huang co-founded Nvidia and has led it as chief executive for decades; the article says he was ousted.
- An earnings report is the company's regular public summary of revenue and profit for a period.
- H200 is a specific Nvidia AI chip; export rules limit which advanced chips can be sold to China.
- The article is a brief excerpt, so many claims are not explained and should be checked against fuller coverage. · level: introductory

<details><summary>Original abstract</summary>

In the midst of dealing with the fallout from its ouster of CEO Jensen Huang, Nvidia delivered its latest earnings report this week, with healthy growth and promises that the good times will continue. At the same time, the chipmaker said it will stop selling its H200 chips in China, and it dismissed calls to […]

</details>

## Model architectures and training

### [Turnout: Adaptive Attention Switching for Efficient Reasoning](https://arxiv.org/abs/2611.27500)
*Anna Kuzina, Mart van Baalen, Paul N. Whatmough et al.* · `cs.LG` · arXiv:2611.27500v1 · relevance 0.33

- **In one sentence**: Turnout is a post-hoc linearization method for a pretrained full-attention language model that keeps both attention paths and uses an RL-trained policy to decide per layer when to switch to a fixed-size linear path during long reasoning generations, trading memory use against answer correctness.
- **In plain words**: Language models normally store a growing memory of everything they have generated so far, which gets expensive when they write long chains of reasoning. This paper converts an existing model to use a fixed-size memory instead, which saves memory but usually makes answers less accurate. The authors keep the original path, add a trained shortcut path, and learn a rule that decides when each layer should switch between them, trained with a reward for both correct answers and low memory use.
- **Why it matters**: Long reasoning tasks are costly for memory, so a method that reduces memory while limiting the accuracy loss could matter for deploying such models. The text reports that the learned switching policy gives a better accuracy-efficiency tradeoff than fixed switching and static hybrid baselines, but the text gives no further detail on size of gains, so its practical weight is unclear.</why>
<parameter name="background">- Transformer attention: the mechanism language models use to look back at earlier tokens.
- Key-value (KV) cache: the stored record of earlier tokens that grows as a response gets longer.
- Linear attention: a variant with a fixed-size state instead of a growing cache, cheaper in memory but often less accurate.
- Linearization / distillation: converting a trained model to the cheaper variant by training the new path to imitate the original.
- Hybrid model: a model that mixes full and linear attention layers.
- Reinforcement learning (RL) policy: a learned decision rule, here trained with a reward that balances correctness and memory use.
- Pareto frontier: the set of trade-offs where you cannot improve accuracy without spending more memory.
- **Background needed**:  · level: research-level
- Matched keywords: transformer, attention, linear attention, distillation

<details><summary>Original abstract</summary>

Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state. This change reduces memory consumption but often hurts accuracy. In reasoning tasks, which require long generations, this effect is especially pronounced. In this work we introduce Turnout, a method that mitigates accuracy loss as a result of linearization, while maintaining its memory-reduction benefits. We apply post-hoc linearization to a pretrained full-attention model, training a linear path through distillation while leaving the original full-attention path unchanged. During response generation, the resulting hybrid model retains both paths and uses a learned policy to control when each layer switches from full to linear attention. We train the policy with reinforcement learning using a reward that balances answer correctness and memory use. Empirical evaluation of our method shows that the learned adaptive policy achieves a better accuracy-efficiency Pareto frontier on reasoning tasks compared to fixed switching and static hybrid baselines.

</details>

### [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973)
*Chang Nie, Chaoyou Fu, Songlin Liu et al.* · `cs.CL` · arXiv:2611.27973v1 · relevance 0.30

- **In one sentence**: MemOnce proposes a memory architecture for LLMs that stores a small set of final-layer hidden states as compact memory, decodes them back into KV caches on demand, and uses sparse retrieval with indices computed once across layers to cut memory growth and latency in long-context continual use.
- **In plain words**: Chatbots that talk with someone over a long time have to keep track of everything said so far, and the usual method stores a growing pile of working notes that eats up computer memory and slows responses. This paper proposes a design that keeps only a small, compressed set of summaries, rebuilds the detailed working notes from them only when needed, and pulls up just the relevant pieces. The authors report that adapting a 4-billion-parameter Qwen3.5 model this way cut the stored memory state by about 1313 times and prefill (the initial processing of input) latency by 6.9 times at a 1-million-token context.
- **Why it matters**: Memory cost is a main limit on running language models over very long or ongoing conversations, so a method that shrinks it while keeping detail could matter for practical deployment. The text is only an abstract, though, so the reported gains are the authors' own claims and have not been checked against independent tests or full experimental details.
- **Background needed**: - Transformer language models store a "KV cache": per-token attention keys and values for every layer, which grows with context length.
- Linear-time architectures compress history into a fixed-size state, which is cheaper but can lose fine detail.
- Hidden states are the internal numerical representations a model produces at each layer.
- Sparse attention means attending to only a selected subset of past items instead of all of them.
- Prefill latency is the delay before the model starts generating, while it processes the input.
- Context length (for example 1M tokens) is how much text the model can consider at once. · level: research-level
- Matched keywords: attention, pretraining, architecture

<details><summary>Original abstract</summary>

Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures compress history into fixed-size states, but struggle to retain fine-grained details. We introduce MemOnce, a foundation architecture that learns scalable memory states for language models. MemOnce is based on two core designs: (a) Memory encoder-decoder: it caches only a small subset of final-layer hidden states as compact memory representations and dynamically decodes them back into KV caches for attention layers; (b) Memory sparse attention: for each continual input, MemOnce adaptively retrieves relevant memory representations, with the sparse indices computed only once across layers. Coupling these two designs enables efficient on-the-fly memory loading and KV cache decoding, drastically reducing the GPU memory footprint and achieving linear-time complexity. We conduct extensive experiments to show that MemOnce outperforms Transformers and other architectures across varying model sizes, context lengths, and training paradigms (pretraining and post-training adaptation). In particular, adapting Qwen3.5-4B with MemOnce reduces memory state cache by 1313$\times$ and prefill latency by 6.9$\times$ at 1M context, and improves throughput by 3.5$\times$ and overall memory performance by +5.77%. Finally, MemOnce generalizes zero-shot to downstream representation tasks, achieving competitive results against specialized models.

</details>

## Machine learning theory

### [Renormalized Entropy from Symmetries: Simplicity Bias and Neural Heat Death](https://arxiv.org/abs/2611.27889)
*Vasco Portilheiro, Samuel Liebana, Andrew Saxe et al.* · `cs.LG` · arXiv:2611.27889v1 · relevance 0.30

- **In one sentence**: The paper derives the equilibrium distribution over functions learned by neural networks under Langevin dynamics with Gaussian regularization, takes the regularization to zero, and uses a renormalization procedure to obtain a symmetry-induced entropy term that favors low-rank, singular, or inactive-neuron functions in linear and homogeneous-activation networks.
- **In plain words**: Neural networks have built-in redundancies: some changes to their internal settings leave the function they compute unchanged. This paper asks how those redundancies steer which functions a network tends to end up with when it is trained with random noise and a mild penalty. The authors find that, at a small positive noise level, these redundancies create a preference for simpler functions, and in some cases the preferred networks are ones whose output shrinks toward zero.
- **Why it matters**: Understanding which functions training favors, beyond just fitting the data, bears on why overparameterized networks generalize. The text presents the result as an analytic derivation with explicit entropy terms for specific architectures; its broader relevance to practical training is not established in the text.
- **Background needed**: - Parameter symmetry: changing weights in a specific way without changing the network's output (e.g., rescaling connected neurons).
- Langevin dynamics: a noisy version of gradient descent, where random jitter is added to each update; it settles into an equilibrium distribution.
- Gaussian regularization: a penalty on large weights that pulls parameters toward zero.
- Entropy (here): a measure of how many parameter settings lead to a given function; "favoring" a function means it has more such settings in equilibrium.
- Renormalization: a technique for handling quantities that blow up in a limit by subtracting out divergent parts.
- Neural tangent kernel: a linearized approximation of how a network's output changes with its parameters; used to interpret "simplicity."
- Low-rank function: one whose underlying weight matrix has few independent directions. · level: research-level
- Matched keywords: neural tangent kernel, implicit bias

<details><summary>Original abstract</summary>

Neural networks have parameter symmetries: parameter transformations that do not affect the represented function. How do these symmetries affect the functions that neural networks ultimately learn? We study the implicit bias arising from these symmetries by calculating the equilibrium distribution over represented functions under Langevin dynamics with Gaussian regularization. To isolate the effect of symmetries on this distribution, we study the limit in which the strength of the regularization is taken to zero. In certain cases, we show that the zero-regularization and infinite-time limits commute. In the low temperature limit, we recover known effective regularizations. At positive temperature, a renormalization procedure allows us to derive a novel entropy which predicts symmetry-induced preference for certain functions. For linear networks, we obtain explicit entropy terms that favor singular and low-rank functions. For networks with homogeneous activations, we find entropy terms that favor inactive neurons, which can lead to neural "heat death" in which equilibrium mass concentrates on networks with vanishing output. We interpret these results through the neural tangent kernel, as a simplicity bias selecting for functions that vary slowly under variations in the parameters.

</details>

### [Verifying and Strengthening Neural Tangent Kernel Theory](https://arxiv.org/abs/2611.27487)
*Hao Zhu* · `cs.LG` · arXiv:2611.27487v1 · relevance 0.26

- **In one sentence**: A Lean 4 machine-checked formalisation of the two-layer neural tangent kernel (NTK) convergence theorem for tanh networks, which also tightens the standard concentration-width bounds and flags a sup-norm Hessian issue that the L2 parameter geometry is proposed to resolve.
- **In plain words**: The paper checks, line by line with a computer proof assistant, a known explanation of why very wide neural networks trained by gradient descent reliably fit their training data. The authors prove that, under stated conditions and with high probability, training follows a unique path and the leftover error shrinks exponentially over time. They also report that some of the standard steps can be made tighter, though the required network widths remain impractically large.
- **Why it matters**: Machine-checked proofs of a widely cited theory are rare, so this shows which assumptions and steps the standard argument actually needs. The reported improvements are numerical comparisons of bound constants and are specific to this setup, so their wider significance is unclear from the text alone.
- **Background needed**: - Neural network: a function built from layers of weighted sums and simple nonlinear activations (here tanh), whose weights are tuned during training.
- Gradient descent / gradient flow: repeatedly nudging weights downhill on an error measure; gradient flow is the continuous-time version.
- Neural tangent kernel (NTK): a fixed similarity measure between inputs that describes how the network behaves when it is very wide and its weights barely move ("lazy training").
- Concentration bounds: results saying random quantities stay close to their averages with high probability; wider networks make this more reliable.
- Positive definiteness / non-degeneracy (λ0 > 0): the kernel matrix has no zero directions, which is what makes the error shrink exponentially.
- Lean 4: a proof assistant in which every step of a mathematical argument is checked by the computer. · level: research-level
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

Writing Neural tangent kernel (NTK) theory explains why very wide neural networks trained by gradient methods converge in the lazy-training regime. Its standard proof combines matrix concentration, random Gram matrices, continuous-time dynamics, spectral perturbation, and a bootstrap argument, but has lacked machine-checked verification. We present a Lean\~4 formalisation for two-layer networks, proving an end-to-end theorem: for a smooth bounded activation (instantiated with $\sigma=\tanh$), frozen biases, paired $\pm 1$ initialisation, and explicit width conditions, gradient flow exists uniquely with probability at least $1-\delta$, and $$ \|r(t)\|^2 \leq \|y\|^2 e^{-\lambda_0 t/2}. $$ The sole data assumption is population NTK non-degeneracy, $\lambda_0>0$. Initial coercivity, kernel drift, the movement bootstrap, the residual ODE, and flow existence and uniqueness are formally proved. The formalisation also sharpens the standard analysis in two ways. First, replacing the conventional matrix-Bernstein variance proxy with the classical row-covariance proxy yields estimated concentration-width certificates for $\tanh$ that are $36$--$53\times$ smaller at $(m,d)=(16,8)$ and $94$--$121\times$ smaller at $(32,16)$. Lean certifies the inequality; the ratios are numerical. Second, the network Hessian has operator norm $\Theta(\sqrt{p})$ on the sup-norm parameter ball (a paper calculation), preventing the expected $O(1/\sqrt{p})$ linearisation bound via sup-norm Taylor estimates. An $L^2$ parameter geometry resolves this issue. Required widths remain polynomial but far beyond practical scales, limiting applicability.

</details>

## Large language models

### [Partially canonical axes in large language model representations](https://arxiv.org/abs/2611.26920)
*Andrea Gregor de Varda, Ferdinando D'Elia, Greta Tuckute et al.* · `cs.CL` · arXiv:2611.26920v1 · relevance 0.14

- **In one sentence**: Across 12 LLMs from six model families, the native coordinate axes of hidden representations align better with other models, with human brain responses, and with interpretable linguistic features than randomly rotated axes do, though they fall short of the best achievable alignment.
- **In plain words**: Researchers asked whether the individual "directions" inside large language models carry meaning or are just arbitrary labels that could be swapped out without consequence. They compared each model's built-in axes with versions of the same data rotated to random angles. The built-in axes matched other models, human brain activity during language, and simple linguistic features better, but not as well as the best possible alignment.
- **Why it matters**: If single units in these networks partly track consistent, recognizable patterns, that bears on how much we can read meaning off individual neurons and on the claim that models and brains share representational structure. The text does not show how far these results generalize beyond the models and measures tested, so the implications remain unclear.
- **Background needed**: - Hidden representation: the list of numbers a neural network produces internally for each word or token.
- Coordinate axis: one of the individual numbers in that list, i.e., one "unit" or dimension.
- Rotation: changing the axes of a space without changing the relative arrangement of points; a random rotation keeps the overall geometry but scrambles which axis is which.
- Canonical vs. arbitrary axes: canonical means the axes are special and meaningful; arbitrary means any rotation would be equally valid.
- Alignment with brain responses: measured by how well the model's activity predicts recorded human brain signals during language.
- Interpretable linguistic features: properties such as part of speech or syntactic role that humans can name. · level: research-level

<details><summary>Original abstract</summary>

Large language models (LLMs) develop rich internal representations of language, but whether their individual coordinate axes carry meaning, or whether meaning is encoded only in directions in representation space, is still an open question. A common assumption is that individual axes in LLMs are arbitrary. We here challenge this view: across 12 LLMs from six model families, the native axes are reliably more aligned with other models' representations, with human brain responses to language, and with interpretable linguistic features than randomly rotated axes that preserve the same geometry. The native axes nonetheless fall well short of the best achievable alignment, so LLM coordinates are not fully arbitrary but also not fully canonical: they are partially canonical. A theory of how LLMs represent language must explain both the population geometry they learn and why individual units acquire patterns of response profiles that recur across systems.

</details>

### [Explicit Style Extraction for Personalized Long-Form Text Generation](https://arxiv.org/abs/2611.27211)
*Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam et al.* · `cs.CL` · arXiv:2611.27211v1 · relevance 0.13

- **In one sentence**: SP-Refine makes style extraction an explicit inference-time step for personalized long-form generation, using a 28-aspect StylePrism taxonomy to build a user profile that guides drafting and two rounds of self-revision on LongLaMP tasks.
- **In plain words**: Language models asked to write in a specific person's voice usually just get a few of that person's past texts and must guess what matters about their style. This paper has the model first write down an explicit profile of the user's habits, using a fixed list of 28 style aspects, and then drafts and revises text against that profile. Across three long-form writing tasks and three models, the method beat the standard retrieval-based baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average.
- **Why it matters**: Personal writing assistance depends on capturing how a person writes, and this shows that making the style profile explicit can help. The text does not establish how well the profiles generalize beyond the benchmark or to real users, so the practical reach is uncertain.
- **Background needed**: - Retrieval-augmented generation: the model is given a few relevant past examples in its prompt before writing.
- LongLaMP: a benchmark of personalized long-form writing tasks.
- ROUGE and METEOR: automatic scores that measure word overlap between generated and reference text.
- Inference-time method: improves output at the moment of writing, without retraining the model.
- Ablation: a test that removes a component to see whether it matters.
- Oracle variant: a version that peeks at the reference answer, used to find the upper limit of gains. · level: research-level

<details><summary>Original abstract</summary>

Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an explicit step: the model first fills StylePrism with the user's patterns, quoted evidence, and habits to avoid, then drafts from the user's samples and revises the draft twice against this profile, guided by its own style scores. On the three long-form tasks of LongLaMP with three LLMs, SP-Refine outperforms LongLaMP's retrieval-augmented baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average and by up to 35.8%. Annotating users' own texts with the extracted profiles shows that StylePrism captures concrete, checkable habits, from the order of rhetorical moves to a reviewer's sign-off. Ablations show that the profile helps as revision guidance, not as a replacement for the samples: writing from the profile alone is worse in all 27 comparisons, while a single implicit-inference call is a cheaper alternative that comes close. Oracle variants that let the reviser see the reference, together with reference-free controls, show that larger refinement gains require information unavailable at inference time.

</details>

## Computer vision

### [PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation](https://arxiv.org/abs/2611.27266)
*Junyi He, Xu Peng, Chengming Xu et al.* · `cs.CV` · arXiv:2611.27266v1 · relevance 0.18

- **In one sentence**: PP-CFG is a few-step diffusion distillation method that keeps positive and negative text conditions separate, combines their attention with opposite signs, and uses a learned mixer over guidance scale and timestep to keep adjustable classifier-free guidance and runtime negative prompting in image and video generators.
- **In plain words**: Modern AI image and video generators often build the result step by step, and speeding them up by using fewer steps tends to make it harder to control how strongly the prompt is followed or to tell the model what to leave out. This paper proposes a way to keep those controls working when generation is cut to about four steps. The authors report results on two existing models, Wan2.1 for video and Qwen-Image for images, including a video quality score of 81.46 in four steps and higher target-removal rates on their own 1,000-case test set.
- **Why it matters**: Fast generation with working user controls matters for making these tools cheaper and more responsive. The text supports claims of gains on its own benchmarks and across two models, but it does not show independent validation or comparisons beyond the listed teachers and DMD baselines, so the broader significance is still open.
- **Background needed**: - Diffusion model: an AI that creates images or videos by gradually removing noise over many steps.
- Distillation: training a smaller or faster model to imitate a slower one, here cutting the process to a few steps.
- Classifier-free guidance (CFG): a dial that sets how strongly the output follows the text prompt.
- Negative prompt: text describing what should be removed or avoided in the output.
- Attention: the mechanism that lets parts of the model weigh and relate different inputs.
- DMD and LCM: two specific distillation methods for making few-step generators.
- VBench: a standard benchmark score for video generation quality.
- Teacher-student distance: how far the fast model's outputs differ from the slower original. · level: research-level

<details><summary>Original abstract</summary>

Few-step diffusion distillation reduces sampling cost but often weakens adjustable classifier-free guidance (CFG) and runtime negative prompting. We introduce PP-CFG, an architecture that keeps positive and negative text conditions separate and combines their attention responses with opposite signs within a shared visual backbone. Its Scale-Time Polarity Mixer refines each condition using the guidance scale and denoising timestep, allowing prompt influence to vary throughout generation. The student retains a continuous scale input and selectable negative prompts with one visual backbone pass per step. We evaluate PP-CFG on Wan2.1 for video generation with distribution matching distillation (DMD), and on Qwen-Image with both latent consistency model (LCM) distillation and DMD. PP-CFG achieves 81.46 VBench in four steps and lower video teacher-student distances across guidance scales than step-distilled DMD. On NegElement-1K, our benchmark of 1,000 matched image and video prompt cases, it achieves higher target-removal rates than the corresponding teachers. These experiments support the method's generality across attention architectures, generation modalities, and distillation objectives while retaining competitive generation quality.

</details>

### [Learning 3D MRI Representations with Generative Adversarial Networks](https://arxiv.org/abs/2611.27057)
*Sujeet Lahane, Sapna Mishra, Akash Suryavanshi et al.* · `cs.CV` · arXiv:2611.27057v1 · relevance 0.15

- **In one sentence**: The paper proposes R2RG, a reconstruction-based representation learning method that pairs 3D convolutional neural networks with an auto-encoding GAN and a composite loss, evaluated on 3D MRI datasets with small sample sizes.
- **In plain words**: Medical scans such as brain MRIs are 3D, but many learning methods either need large datasets or flatten the scans into 2D slices, losing depth information. This paper presents R2RG, a method that learns compact summaries of 3D brain MRI scans by training a network to rebuild the original scan, with an adversarial (GAN) setup helping the rebuilt images look realistic. The authors report better performance across several datasets, including smaller ones, and better results than contrastive methods on classifying Parkinson's and Alzheimer's disease.
- **Why it matters**: Labeled medical data is scarce and expensive, so methods that work with small 3D datasets could matter for clinical imaging research. The text reports gains over contrastive methods on two disease classification tasks, but it gives only the high-level claims here, so the size and reliability of those gains cannot be judged from this summary alone.
- **Background needed**: - Representation learning: training a model to turn raw data into compact numerical features that can be reused for other tasks.
- Reconstruction-based learning: the model learns by compressing an input and then rebuilding it; the quality of the rebuild drives learning.
- Convolutional neural network (CNN): a type of neural network good at finding local patterns; a 3D version works on volumes such as MRI scans rather than flat images.
- GAN (generative adversarial network): two networks compete, one generating images and one judging them, which tends to push outputs toward realism.
- Contrastive learning: a method that learns by pulling similar examples together and pushing different ones apart.
- MRI: magnetic resonance imaging, a scan that produces 3D images of soft tissue such as the brain.
- Overfitting: when a model memorizes small training data and performs poorly on new data. · level: research-level

<details><summary>Original abstract</summary>

Learning representations of visual images is a challenging task. It requires extracting abstract patterns from high-dimensional data without explicit supervision. This becomes pronounced with 3D MR imaging due to sparse features, higher dimensional inputs, and smaller datasets. Many state-of-the-art representation learning algorithms successfully rely on transformers and diffusion-based architectures. However, these methods struggle with smaller datasets. In effect, solution methods relax the problem by slicing 3D volumes and solving the problem for 2D medical imaging, resulting in a loss of spatial 3D information. We present R2RG, a representation learning method based on Convolutional Neural Networks (CNNs), with Generative Adversarial Networks (GANs) honing the reconstruction task. Our key insights lie in exploiting architectural biases in 3D CNNs, combined with data-efficient auto-encoding GANs and a composite loss function to enhance reconstruction fidelity and stabilize training. Our experiments on three standard datasets and a locally collected dataset show that R2RG not only achieves superior performance but also generalizes to heterogeneous and smaller datasets. Furthermore, representations learned with R2RG outperform those learned with contrastive-based representation learning methods on Parkinson's and Alzheimer's disease classification. Our work demonstrates that reconstruction-based representation learning is a promising direction for 3D medical imaging under limited data availability.

</details>

## Reinforcement learning

### [Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27368)
*Dennis Gross, J{\o}rn Eirik Betten, Helge Spieker* · `cs.MA` · arXiv:2611.27368v1 · relevance 0.23

- **In one sentence**: The paper proposes DisQ, a test-case selection method that uses a "Q-value gap" (disagreement between agents' value estimates) to pick states likely to expose coordination failures in value-based cooperative multi-agent RL policies, and reports improved failure detection over random and genetic-algorithm search in most of four benchmark environments.
- **In plain words**: Teams of software agents trained with reinforcement learning to work toward a shared goal can behave unsafely in ways that the reward signal does not capture, and those failures are hard to explain. This paper asks how to find such failures efficiently by testing only the situations most likely to reveal them. The authors use a signal they call the Q-value gap, which flags a situation when the agents' estimates of the reward they can still earn differ by more than a set threshold, and they run tests only on flagged situations.
- **Why it matters**: Safety testing for multi-agent systems has received less attention than testing single agents, and a test-selection method that skips states without a flagged gap could reduce the cost of finding failures. The text reports gains only in most, not all, evaluated configurations, so the practical reach beyond these four benchmarks is unclear.
- **Background needed**: - Reinforcement learning: an agent learns by trial and reward, choosing actions to maximize expected total reward.
- Multi-agent (cooperative) RL: several agents act at every step to optimize one shared objective.
- Q-value: a learned estimate of the future reward an action will yield from a given situation; a Q-learning agent keeps such estimates.
- Coordination failure: agents' individual choices work against each other, even though each looks reasonable alone.
- Test case selection: choosing which situations to run a system in, since exhaustive testing is too costly.
- Baselines: random testing (picking situations at random) and genetic-algorithm search (evolving candidate situations toward failures). · level: research-level
- Matched keywords: reinforcement learning, Q-learning

<details><summary>Original abstract</summary>

Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the reward, and these behaviors are hard to explain. However, testing CMARL policies for safety has received less attention than the safety testing of single-agent RL policies. In this paper, we propose DisQ, a test case selection method that identifies failure-revealing states in value-based CMARL by exploiting a signal specific to trained Q-learning agents. The signal is the Q-value gap, an explainable metric that flags a state when the agents' estimates of the achievable return diverge by more than a calibrated threshold. DisQ selects such states for execution and skips those without a gap. Our experiments in four CMARL benchmark environments show that, in most of the evaluated configurations, DisQ improves failure detection over single-agent RL testing methods applied to CMARL, namely random testing and search-based testing with genetic algorithms. Our main contributions are the Q-value gap, an indicator of potential miscoordination computable from a single state without executing the system, and DisQ, a test case selection method that adapts existing single-agent testing methods to CMARL.

</details>

### [Decision Models Are General-Purpose Process Reward Models](https://arxiv.org/abs/2611.27068)
*Jiajun Fan, Qinglong Zheng, Ziwen Wang et al.* · `cs.AI` · arXiv:2611.27068v1 · relevance 0.20

- **In one sentence**: DM-PRM turns a general-purpose yes/no decision model into a zero-shot process reward model that scores each step of a language agent's trajectory and adds the standardised scores to the policy-gradient advantage, reportedly lifting GRPO and GiGPO on ALFWorld and WebShop.
- **In plain words**: Language-model agents that carry out multi-step tasks, such as household chores or online shopping, usually get only one score at the end of an attempt, so every step gets the same credit. This paper proposes asking a general-purpose model one yes/no question about each step, with no extra labelled data, training or separate critic, and using those answers to give each step its own credit. The authors report that this improves several existing training methods on two benchmarks and helps agents stop wasting actions and explore more.
- **Why it matters**: Assigning credit to individual steps is a long-standing problem in reinforcement learning, and a method that needs no step labels or fine-tuning could make it cheaper to apply. The results are reported on two benchmarks with one model size, so how well they carry over to other tasks and models is not yet shown.
- **Background needed**: - Reinforcement learning (RL): training by trial and error, where an agent improves from reward signals.
- Reward per episode vs. per step: a single end-of-task score versus a score for each action taken.
- Policy-gradient methods: RL algorithms that adjust the agent's action probabilities in the direction that earned higher reward.
- Advantage: how much better an action turned out than expected, used to decide how strongly to reinforce it.
- Process reward model (PRM): a scorer that judges intermediate steps, not just final outcomes.
- Critic and PPO: a learned value estimator and a common policy-gradient algorithm that uses it.
- GRPO, GiGPO, HGPO, GraphGPO: related recent methods for training language agents with group-based comparisons of rollouts.
- Zero-shot: applied without task-specific training or labels.
- ALFWorld and WebShop: benchmark environments for household tasks and web shopping. · level: research-level
- Matched keywords: reinforcement learning, reward model

<details><summary>Original abstract</summary>

Reinforcement learning (RL) from verifiable outcomes gives a language agent one reward per episode: every step is credited alike, and nothing about the task is learned when all rollouts fail. The last mile, step-level credit, usually requires step labels, a learned critic, costly LLM judges or hand-written rules. We introduce DM-PRM, which turns a general-purpose decision model -- one answering yes/no questions with probabilities -- into a general-purpose process reward model (PRM), zero-shot: no step labels, no fine-tuning, no critic. DM-PRM asks one question per step and adds the standardised answers to the advantage. It plugs into any policy-gradient method; one model, with one question text per environment, serves household tasks, web shopping and multiple RL methods. With Qwen2.5-1.5B it lifts GRPO by over twenty points on ALFWorld and over ten on WebShop, overtakes GiGPO on ALFWorld and learns in far fewer iterations; it also improves GiGPO and GraphGPO on both benchmarks and reaches the highest success of our comparison, ahead of critic-based PPO and of state-of-the-art GiGPO, HGPO and GraphGPO. Its scores locate useful steps in failed rollouts, and trained agents drop idle actions and explore instead of circling. DM-PRM shows that step credit need not be learned: it can be asked for.

</details>

## AI safety and alignment

### [Preserving Pretrained CFG Structure in RL for Diffusion Models with Conditional Contrast Regularization](https://arxiv.org/abs/2611.27288)
*Yunfei Zheng, Xiaolong Wang, Dandan Zheng et al.* · `cs.LG` · arXiv:2611.27288v1 · relevance 0.29

- **In one sentence**: The paper proposes Conditional Contrast Regularization (CCR), which keeps reinforcement-learning fine-tuning of diffusion models anchored to the structure of the pretrained classifier-free guidance correction, to improve the reward-quality trade-off.
- **In plain words**: Image-generating AI models are often fine-tuned with reinforcement learning to score higher on a target reward, but this can quietly make overall image quality worse, a pattern the authors call reward hacking. The authors use a geometric view of the update directions to show that the pretrained guidance direction carries quality-relevant information that reward-driven updates can lose, and they add a regularizer that keeps the model close to that structure.
- **Why it matters**: Reward hacking, where a model games its scoring signal at the expense of real quality, is a central concern in AI alignment, and this work offers a concrete, measurable way to check and limit it in one setting. The text reports results across several rewards and backbones, but the evidence here is a summary only, so how far the approach generalizes beyond these experiments is not established.
- **Background needed**: - Diffusion models generate images by gradually removing noise, guided by a text prompt.
- Reinforcement learning (RL) fine-tuning adjusts a trained model to maximize a score (a reward) from a judging function.
- Classifier-Free Guidance (CFG) is a standard technique that pushes generated images to follow the prompt more closely, by contrasting conditional and unconditional predictions.
- "Correction vector" here means the direction in prediction space by which a model's output is shifted; the paper compares the RL correction with the CFG correction by projecting one onto the other.
- A frozen reference model is the original pretrained model, kept unchanged to serve as a baseline during fine-tuning.
- Reward hacking means optimizing a score in ways that do not improve, and may harm, the thing the score was meant to measure. · level: research-level
- Matched keywords: alignment, reward hacking

<details><summary>Original abstract</summary>

Reinforcement Learning (RL) has become an important component in the post-training of diffusion models. In practice, however, standard RL often improves the target reward without reliably preserving holistic generation quality, leading to unstable reward-quality trade-offs that we view as a form of reward hacking. Since Classifier-Free Guidance (CFG) is known to improve visual clarity, prompt alignment, and perceptual quality in generation, we investigate whether its underlying structure can serve as a useful prior during RL. We present a unified geometric view that interprets both CFG and RL as correction vectors in a common prediction space, and identify the projection of the RL-induced correction onto the pretrained CFG correction as a useful diagnostic of quality-related structural preservation. Geometric analysis and rotation intervention further show that the pretrained CFG direction carries information useful for generation quality that reward-driven RL updates do not necessarily preserve. Based on this insight, we propose Conditional Contrast Regularization (CCR), which uses the frozen reference model's conditional contrast as a local structural prior during RL. Experiments across multiple reward settings and backbones show that CCR more consistently preserves generation quality while maintaining competitive reward, yielding a better reward-quality trade-off than standard RL and generic regularization methods.

</details>

### [The Assistant Persona Differs Across Languages in Activation Space](https://arxiv.org/abs/2611.27504)
*Daniel Yoo, Naama Rozen, Evan Harris* · `cs.CL` · arXiv:2611.27504v1 · relevance 0.24

- **In one sentence**: The paper extracts the assistant persona direction in 31 languages in Qwen3-32B and finds these activation-space axes differ across languages, correlate with language resource level, and affect how strongly persona-based jailbreaks can be steered.
- **In plain words**: Large language models are less safe when used in languages with less training data. This study looks inside a model to ask whether its internal "helpful assistant" setting is the same across languages. The authors found that the internal direction for this persona differs noticeably between languages, and that the differences track how much data each language has.
- **Why it matters**: It offers a mechanistic, inside-the-model explanation for why safety gaps across languages exist, rather than only documenting them from outputs. It suggests multilingual alignment work may need to target the assistant persona directly, though the text alone does not show whether this would fix the gap.
- **Background needed**: - Language models store behavior as patterns of numbers called activations, which can be read as points in a high-dimensional space.
- A "direction" in that space is a consistent pattern linked to a concept, here the assistant persona.
- Cosine similarity measures how closely two directions point the same way; 1 means identical, 0 means unrelated.
- "Steering" means nudging the model's activations along a direction to change its behavior.
- A "jailbreak" is a prompt that tricks a model into ignoring its safety rules.
- "Resource level" refers to how much text data exists for a language on the web or in training sets.
- The study covers one model (Qwen3-32B), so results may not generalize to other models. · level: research-level
- Matched keywords: alignment, jailbreak

<details><summary>Original abstract</summary>

Large language models behave differently across languages, and are noticeably less safe in lower-resource languages. This gap is well established behaviorally, but not mechanistically. Directions in activation space, including the assistant persona direction, are almost always extracted from English and assumed to generalize across languages. We extract the assistant persona direction in 31 languages in Qwen3-32B, and find that the resulting axes differ substantially: their cosine similarity to the English axis ranges from 0.378 to 0.911. Moreover, each language's assistant persona direction and its magnitude are correlated with the language's resource level. We also find that the model's default assistant state is farther from the helpful assistant pole in lower-resource languages. Finally, steering against a language's own axis amplifies persona-based jailbreak more than steering against the English axis. These results indicate that the model does not carry a single assistant representation across languages. More broadly, the assistant persona may need to be an explicit target of multilingual alignment.

</details>

## Interpretability

### [Parasite Features: Causal Abstraction Through Spurious Pathways](https://arxiv.org/abs/2611.26711)
*Denis Sutter, Qing Yao, Sasha Boguraev et al.* · `cs.LG` · arXiv:2611.26711v1 · relevance 0.29

- **In one sentence**: The paper shows that Distributed Alignment Search, a causal-abstraction interpretability method, can be fooled by "parasite features": pairs of representation directions that jointly mimic a claimed algorithm without the model actually using the feature.
- **In plain words**: Researchers study how to tell what computation a neural network is really doing inside. One popular test checks whether a simple, human-readable algorithm matches the network's internal behavior. This paper reports that the test can be passed by a misleading pair of internal directions that only look like the intended feature, and the authors demonstrate this on syntactic agreement and two-digit addition tasks.
- **Why it matters**: It matters because interpretability claims often rest on these equivalence tests, so a method that can be spuriously satisfied could lead researchers to wrongly conclude a model uses a given feature. The text frames it as a caution for best practices rather than a claim that existing findings are wrong.
- **Background needed**: - Mechanistic interpretability: reverse-engineering what computations a neural network performs internally.
- Causal abstraction: a framework saying a network "implements" an algorithm if swapping or intervening on its internal parts behaves the same way as the algorithm.
- Distributed Alignment Search (DAS): a method that learns a linear map to find directions in a network's internal state that correspond to a high-level variable.
- Representation space: the set of internal numerical activations a network uses; a "direction" is a particular combination of those numbers.
- Spurious feature: something that passes a test for the wrong reason. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Causal Abstraction defines a notion of \emph{equivalence} between a neural network and an algorithm, thus serving as a powerful framework for mechanistic interpretability. In this paper, however, we show the existence of a class of \emph{spurious features} which straightforwardly pass such equivalence tests. Suppose there are two directions in a model's representation space where: (i) one discriminates the input based on some feature, and (ii) the other steers the model towards a certain output. Interpretability methods based on Causal Abstraction (e.g., Distributed Alignment Search) can \emph{spuriously} simulate these directions' combined behavior by leveraging pathways passing through them, giving the impression that the model implements this feature. In such cases, we say the method discovered a \defn{parasite feature}. Experimentally, we show that Distributed Alignment Search finds parasite features using linear alignment maps in two tasks: syntactic agreement and two-digit addition. Our paper highlights an important consideration for Causal Abstraction and contributes to the ongoing debate about best practices for mechanistic interpretability.

</details>

### [WaXup: Weight Averaging of Experts as Data Augmentation for Robust Introspection](https://arxiv.org/abs/2611.27353)
*Marc Bo\"elle, Lucas Dixon, Alexandre Ram\'e* · `cs.CL` · arXiv:2611.27353v1 · relevance 0.25

- **In one sentence**: WaXup augments the training data for trainable introspection (models trained to describe their own finetuned behaviors) by linearly interpolating weights of finetuned expert models, and reports better and more robust descriptions on three benchmarks.
- **In plain words**: Researchers want language models that can explain, in plain words, what they were trained to do, so people can check them for hidden or unwanted behaviors. This paper proposes WaXup, which creates extra training examples by averaging the settings (weights) of several specialized versions of a model. The authors report that this improves the accuracy and robustness of these self-descriptions on three test sets, including one built with models deliberately trained to hide their behaviors.
- **Why it matters**: As language models grow more capable, checking what they have learned is getting harder, and self-explanation is one proposed route to auditing them. The work matters for AI safety auditing, though the text alone does not show how well it would hold up on the most capable or real-world systems.
- **Background needed**: - Finetuning: further training a pretrained model on a specific task, producing a specialized "expert" version.
- Mechanistic interpretability: studying a model's internal workings directly, which the abstract says is struggling to keep pace with larger models.
- Trainable introspection: training a model to answer questions in natural language about what it learned during finetuning.
- Weight space and interpolation: each model is a long list of numbers (weights); averaging two such lists gives a model "in between" the two.
- Linear mode connectivity: the observed property that averaged finetuned models often keep the behaviors of the originals.
- Data augmentation: creating extra training examples to make learning more robust; MiXup is the framework this builds on.
- AuditBench: a suite of models adversarially trained to conceal their behaviors, used to test alignment auditing. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

As the capabilities of large language models keep improving, traditional mechanistic interpretability methods struggle to keep pace. In contrast, trainable introspection methods emerge as a promising alternative; they repurpose the model itself as a self-diagnostic tool, trained to verbalize what it has learned during finetuning in natural language. While training on datasets of finetuned experts achieves encouraging results, it currently lacks robustness and generalization. Building on the data augmentation framework of MiXup, we introduce WaXup, a method that augments the introspection training set through linear interpolation in the weight space. This is motivated by the linear mode connectivity property: weight averaged experts interpolate the behaviors of the initial experts. We evaluate WaXup on three benchmarks: hidden-behavior models, a meta-dataset of real-world NLP tasks and AuditBench, a challenging alignment auditing suite of models adversarially trained to conceal their behaviors. WaXup improves the accuracy of generated descriptions as well as robustness to various distribution shifts. We hope to improve the reliability of trainable introspection methods towards better and safer models.

</details>

## AI for mathematics

### [Budget-Aware Predict-and-Verify Theorem Proving with Heterogeneous LLM Solvers](https://arxiv.org/abs/2611.26906)
*Wei Jiang, Ziran Liu, Wei Wang* · `cs.AI` · arXiv:2611.26906v1 · relevance 0.23

- **In one sentence**: BudgetPV is an agentic predict-and-verify system that uses a cross-solver predictor, trained with two different loss objectives for early and late allocation stages, to route unresolved Lean subgoals across heterogeneous LLM provers under a compute budget.
- **In plain words**: Computer programs that try to prove math statements can use several AI models, some strong but costly and some cheap but weaker. This paper describes a way to decide which model should try each unproven piece of a problem, and when to spend more effort on pieces that failed earlier, so that less total computing is used. The authors report that their method needed less generation compute than giving every piece the same allocation to solve the same number of pieces, across four benchmark sets.
- **Why it matters**: Running expensive AI models on every sub-problem is a practical cost problem for automated proof tools, and budget-aware routing is a reasonable way to address it. The text does not say how large the savings are or how the method compares with other routing approaches, so its wider significance is unclear from this summary alone.
- **Background needed**: - Theorem proving: a computer checks that a mathematical statement follows from axioms, here using the Lean proof assistant, which verifies each step.
- Subgoal: a smaller claim that must be proved to finish a larger proof.
- LLM solver: a large language model that generates candidate proof steps; solvers differ in ability and in cost per attempt.
- Predict-and-verify: the system predicts which solver is likely to succeed, then the proof checker verifies the attempt.
- Uniform allocation: giving every subgoal the same computing effort, used here as the baseline.
- Cross-entropy: a standard training loss for classification; class weighting makes rare classes count more; calibrated probabilities mean predicted odds match actual success rates.
- Benchmarks named: Lean Workbook, miniF2F, ProofNet, PutnamBench (collections of formal math problems). · level: research-level
- Matched keywords: Lean, theorem proving

<details><summary>Original abstract</summary>

Large language model (LLM) theorem solvers differ in both proving capability and inference cost. Applying an expensive solver to every subgoal wastes computation when cheaper models are sufficient, while always starting from the cheapest solver wastes attempts on subgoals that require stronger models. We present BudgetPV, an agentic budget-aware predict-and-verify system that allocates computation across unresolved subgoals and heterogeneous LLM solvers. BudgetPV uses a cross-solver predictor to guide solver selection for each subgoal and revises the allocation as verification feedback becomes available. The allocation problem changes as proving progresses. Early decisions mainly determine which solver should handle an untried subgoal, while later decisions determine which previously attempted subgoals should receive additional computation. We train the predictor with two objectives for these two stages. Class-weighted cross-entropy improves assignment to less frequent stronger solvers during the initial stage, while plain cross-entropy provides better calibrated probabilities for later allocation among previously attempted subgoals. We evaluate BudgetPV on Lean Workbook, miniF2F, ProofNet, and PutnamBench using three progressively expanded solver settings: a strong but expensive solver alone, adding a medium-cost solver with intermediate solving capability, and further adding a cheap solver with lower solving capability. BudgetPV requires less LLM generation computation than uniform allocation to solve the same number of subgoals across the evaluated settings. The experiments further show the computation savings obtained as medium- and lower-cost solvers are added.

</details>

### [Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning Using Executable Symbolic Representations](https://arxiv.org/abs/2611.27203)
*Yu-Bin Liu, Shi-Ju Ran* · `cs.LG` · arXiv:2611.27203v1 · relevance 0.15

- **In one sentence**: The paper introduces GSM-AB, a benchmark that separately varies operand digit length and operation count, and reports that executable symbolic representations (Lean, plus a Python program-of-thought control) slow accuracy decline in LLM arithmetic reasoning compared with natural-language reasoning.
- **In plain words**: Large language models often score well on math tests without showing whether they stay accurate as problems get bigger or more involved. This paper builds a controlled test where the size of the numbers and the number of steps can be changed separately. It reports that having models write their reasoning as code-like formal statements (Lean, and Python as a control) makes accuracy fall more slowly as problems grow.
- **Why it matters**: Reliability on multi-step calculations matters for any use of AI in science, finance, or engineering, and this paper ties the choice of reasoning format to how accuracy scales. Its significance beyond these experiments is not established by the text, which gives only the abstract-level findings and no full details on sample sizes or variance.
- **Background needed**: - Large language model (LLM): an AI system trained on text that generates answers and reasoning in words.
- Arithmetic reasoning: working through multi-step calculations correctly.
- Natural-language reasoning vs. executable representation: the model either explains steps in ordinary English, or writes them in a formal, machine-checkable form (Lean is a proof-and-programming language; Python-PoT means the model writes a Python program to compute the answer).
- Accuracy scaling: how accuracy changes as a problem gets harder along some axis.
- Operand digit length: how many digits the numbers in a problem have.
- Operation count: how many calculation steps a problem requires.
- Control condition: a comparison setup used to check whether a result is specific to one method. · level: intermediate
- Matched keywords: Lean

<details><summary>Original abstract</summary>

High accuracy on mathematical benchmarks does not establish whether reasoning remains reliable as problem complexity increases. We examine how executable symbolic representations change accuracy scaling in large language models compared with natural-language reasoning. To address this limitation, we introduce the GSM Arithmetic Benchmark (GSM-AB), a controlled benchmark that independently varies operand digit length and operation count to probe numerical scale and compositional complexity. We find that executable representations can improve accuracy and slow its decline as complexity increases. Lean reduces average sensitivity to operand digit length at every tested model size. By contrast, slower degradation with increasing operation count emerges at the larger model sizes. A Python program-of-thought (Python-PoT) control shows a similar operation-axis pattern, suggesting that this finding is not specific to Lean. These findings show that reasoning representation shapes arithmetic accuracy scaling and support executable symbolic representations for more reliable reasoning on complex arithmetic tasks.

</details>

## Robotics and embodied AI

### [Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter](https://arxiv.org/abs/2611.27845)
*Songyang Liu, Yu Hou, Yuqing Hu et al.* · `cs.RO` · arXiv:2611.27845v1 · relevance 0.20

- **In one sentence**: A runtime safety filter, built on a camera-estimated scene model and a target-conditioned control barrier function quadratic program, screens operator commands so a teleoperated Unitree G1 humanoid's tool avoids a non-target electrical switch during switching tasks.
- **In plain words**: Electrical switching means flipping switches in substations or panels, which is hazardous for people. This paper looks at letting a humanoid robot do it through a remote operator wearing virtual reality, where a slightly imprecise command could hit a neighbouring switch. The proposed filter checks each command against a model of the scene built from the robot's head camera and only changes commands that would cause a collision with the wrong switch.
- **Why it matters**: Robots that take over hazardous switching could reduce worker exposure to electrical risk, and the approach of screening human commands with a safety filter may be relevant to other teleoperated manipulation tasks. The text reports only small-scale tests (ten real-world rounds and nine simulated runs), so how well it generalises to real substations is unclear.
- **Background needed**: - Teleoperation: a human remotely controls a robot, here through virtual reality.
- Humanoid robot: a human-shaped robot; the Unitree G1 is the platform used.
- Scene model: a computer's estimate of where objects are, built from camera images.
- Control barrier function (CBF): a mathematical safety boundary that a robot's motion must stay inside.
- Quadratic program (QP): a standard optimisation step that finds the closest safe command to the one given.
- Safety filter: a layer that passes safe commands unchanged and corrects unsafe ones.
- Reported results: in real tests, all 10 target operations succeeded with no wrong switch touched; in simulation, 9/9 safe completions versus 5/9 for raw teleoperation. · level: research-level

<details><summary>Original abstract</summary>

Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch. This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of a humanoid robot. The filter integrates a scene model estimated from the robot head camera and a target-conditioned control barrier function quadratic program that keeps the tool away from the non-target switch while passing safe commands unchanged. In real-world experiments on a Unitree G1 humanoid robot, with six rounds at each of two standing positions, target operations succeed in all ten rounds with an unchanged target and no non-target actuation. A simulation study achieves 9/9 safe completions, compared with 5/9 for raw teleoperation, demonstrating the feasibility of the method for humanoid switching operations.

</details>

### [HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots](https://arxiv.org/abs/2611.27181)
*Jinlin Gan, Mingzhe Li, Junsheng Zhang et al.* · `cs.RO` · arXiv:2611.27181v1 · relevance 0.18

- **In one sentence**: The paper introduces Humanoids, a benchmark with synthetic and annotated real-world data for monocular 3D humanoid robot pose estimation, and HumanoidPose, a framework that adds robot-specific articulation modeling and kinematic grounding.
- **In plain words**: Humanoid robots need to know their own 3D body posture, and a single camera image is a cheap way to estimate it from the outside. Existing pose-estimation tools were built for human bodies or for fixed industrial arms, so this paper builds a dataset and test set for humanoid robots and a method designed around their body structure. The authors report strong results on their benchmark and on another humanoid benchmark, including transfer to real-world images without extra training on them.
- **Why it matters**: As humanoid robots move into everyday settings, watching their posture from a camera could support monitoring, motion analysis, and robot learning. The text reports ablations suggesting that robot-specific articulation modeling and kinematic grounding each help, but the claims rest on the authors' own benchmarks, and the data and code are only promised for future release.
- **Background needed**: - Pose estimation: inferring the positions of a body's joints in 3D from an image.
- Monocular: from a single camera, with no depth sensor or multiple views.
- Human pose estimation (HPE) is the mature field for people; robot pose estimation (RPE) mostly covers fixed arms.
- Kinematics: the geometry of joints and links that determines where a body part can be given its joint angles.
- Synthetic data: computer-generated training images with known labels.
- Zero-shot transfer: working on new data types without being trained on them.
- Ablation study: removing one component at a time to see how much it contributes. · level: research-level

<details><summary>Original abstract</summary>

As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation (HPE), while not being fully addressed by either paradigm: RPE primarily focuses on non-humanoid robots, particularly fixed-base manipulators, whereas HPE is built upon human-specific skeletal topologies, body models, and motion priors. Despite recent progress in humanoid 2D keypoint detection and HPE adaptation, humanoid-native 3D pose recovery remains insufficiently studied, and a dedicated benchmark with suitable training data and evaluation protocols is still lacking. To address this gap, we introduce Humanoids, a benchmark for monocular 3D humanoid robot pose estimation, and propose HumanoidPose, a framework for this task. Humanoids provides synthetic 3D supervision across diverse humanoid embodiments, manually annotated real-world 2D data, and real-world RGB sequences paired with robot states for 3D evaluation on a physical Roban humanoid. HumanoidPose combines human-inspired visual perception with robot articulation modeling and explicit kinematic grounding. Experiments on Humanoids and the DHRP-H1 benchmark demonstrate strong performance in articulation recovery and 3D pose estimation, including zero-shot transfer to real-world 2D and 3D evaluation. Ablation studies further show the contribution of robot-native articulation modeling and explicit kinematic grounding. The dataset and code will be publicly released to support future research in the community.

</details>

## Security and cryptography

### [Post-Quantum Migration in Brownfield 5G Core Networks: Verified Hybrid Key Establishment, Performance, and Rollback](https://arxiv.org/abs/2611.27735)
*Shubham Verma* · `cs.CR` · arXiv:2611.27735v1 · relevance 0.11

- **In one sentence**: A deployment-level method for adding hybrid post-quantum/classical key establishment to a controlled 5G Core Service-Based Interface segment via external boundary proxies, evaluated on Open5GS AMF-NRF with packet-level verification, latency measurements, and rollback tests.
- **In plain words**: Mobile phone core networks use encryption to protect messages between their internal software parts, and that encryption may eventually be broken by quantum computers. This paper looks at how to switch those connections to a stronger mix of old and new encryption without rewriting the software itself, by placing separate helper components at the boundary. The authors tested this on one link in an open-source 5G core and report that the new setup works, can be reversed, and adds a measurable delay of about 3.4 milliseconds to registrations.
- **Why it matters**: Operators running existing networks cannot easily replace every component at once, so a migration path that does not touch application code may matter for planning the shift to quantum-resistant encryption. The evidence is limited to one link in one open-source test setup, so it is unclear how the results would carry over to commercial deployments.
- **Background needed**: - 5G Core: the software that manages mobile network sessions and subscribers, split into network functions (NFs).
- Service-Based Interface (SBI): the internal messaging links between those network functions, usually carried over TLS.
- TLS: the protocol that encrypts connections and sets up keys at the start of each session.
- Post-quantum cryptography (PQC): encryption designed to resist attacks from future quantum computers.
- Hybrid key establishment: combining a classical key exchange with a post-quantum one, so security holds if either is unbroken.
- X25519MLKEM768: a specific hybrid key exchange that pairs the X25519 classical method with the ML-KEM post-quantum method.
- Brownfield: an existing, already-deployed system, as opposed to a new build.
- Boundary proxy (BCEE): an external component that handles the encryption on behalf of a network function.
- Rollback: returning to the previous configuration if the change causes problems. · level: intermediate

<details><summary>Original abstract</summary>

Migrating brownfield 5G Core networks to post-quantum cryptography (PQC) is difficult because deployed network functions, base images, and TLS libraries evolve under different upgrade constraints. This paper evaluates a deployment-controlled migration strategy that enables hybrid post-quantum/traditional key establishment through externally deployed Boundary Cryptographic Execution Entities (BCEEs), without modifying participating network function source code. The approach is evaluated using the Open5GS AMF-NRF Service-Based Interface as a representative 5G Core scenario. Classical and hybrid configurations are compared under an unchanged mediation topology. Packet-level analysis confirms successful negotiation of X25519MLKEM768, and functional validation demonstrates that representative SBI procedures remain operational through the mediated path. In 120 NF-registration transactions, the median AMF-facing registration latency increased from 22.968 ms under the classical state to 26.351 ms under the hybrid state, reflecting a 3.383 ms (14.73 percent) increase, with a whole-block 95 percent confidence interval of [1.193, 7.872] ms. At the mediated TLS boundary, the hybrid configuration shows a 4.599 ms higher median segment-local TLS-establishment time than the classical configuration. These two reported differences reflect system-level runtime effects and do not isolate key-encapsulation cost. Packet evidence verifies rollback from hybrid-mediated operation to classical mediated operation and, separately, restoration of the native direct path. NF-facing compatibility legs remained plaintext and outside the hybrid post-quantum scope. The results demonstrate a packet-verifiable and manually reversible brownfield mechanism for introducing hybrid post-quantum key establishment on a controlled 5G SBI segment.

</details>

### [Enhancing Metaverse Security using Explainable AI-based Intrusion Detection Framework](https://arxiv.org/abs/2611.27199)
*Esha Kuppanda, Shalaka Mahadik, Pranav M. Pawar et al.* · `cs.CR` · arXiv:2611.27199v1 · relevance 0.08

- **In one sentence**: The paper compares machine learning models for intrusion detection in Internet of Things (IoT) based "Metaverse of Things" networks, uses explainable AI (SHAP and LIME) to pick out influential features, and reports high accuracy on three public security datasets (ToN-IoT, CIC-IoT-2023, BoT-IoT).
- **In plain words**: Connected devices that feed into virtual-world platforms can be broken into by attackers, and older security tools struggle with the large volume and complexity of the data. This paper tests several machine learning models for spotting intrusions and uses explanation tools to show which data features drive each model's decisions. The authors report accuracy of 99.83% on one dataset, 96.45% on another (using XGBoost), and 99.99% on a third (using Random Forest and Extra Trees).
- **Why it matters**: Security for networks of connected devices is an ongoing concern, and the paper ties model accuracy to explanations that people can inspect, which may matter for trust in automated security tools. The text does not show how these results hold up in live networks or against new attacks, so its practical value is uncertain.
- **Background needed**: - Intrusion detection system (IDS): software that watches network traffic and flags suspicious activity.
- Internet of Things (IoT): everyday devices (sensors, cameras, smart gadgets) connected to the internet.
- Metaverse of Things: connected devices linked to immersive virtual environments.
- Machine learning (ML): methods that learn patterns from example data to make predictions, here labeling traffic as normal or malicious.
- Explainable AI (XAI): techniques that show why a model made a given decision.
- SHAP and LIME: two common XAI tools that rank how much each input feature contributed to a prediction.
- Accuracy: share of traffic records labeled correctly; high accuracy on a benchmark does not guarantee real-world performance.
- Benchmark datasets: shared collections of recorded network traffic used to compare methods. · level: intermediate

<details><summary>Original abstract</summary>

The MoT virtual environment, called the Metaverse of Things (MoT), combines machine learning (ML) and Internet of Things (IoT) to offer significant business opportunities in various sectors such as entertainment, healthcare, and education. In addition to its benefits, the MoT poses risks to privacy and security through unauthorized access, which threatens trustworthiness. While traditional intrusion detection systems (IDS) exist to handle this challenge, they struggle with high-dimensional data and poor interpretability. To address this challenge, the research conducted a thorough analysis of different ML models and proposed the optimal model to secure the MoT environment. The research employed explainable artificial intelligence (XAI) to identify the most effective features that contributed to optimal model selection. The research presented an optimal framework combining ML and XAI to safeguard MoT networks from the most recent cyberthreats. The research used three advanced benchmark security datasets: ToN-IoT, CIC-IoT-2023, and BoT-IoT, to examine the XAI-based intrusion detection framework. The XAI-based intrusion detection framework achieved 99.83% accuracy on ToN-IoT and 96.45% on CIC-IoT-2023 using the XGBoost model. On the BoT-IoT dataset, the Random Forest (RF) and Extra Trees (ET) classifiers reached 99.99% accuracy. The Shapley Additive Explanations (SHAP) and Local Interpretable Model-Agnostic Explanations (LIME) techniques used for XAI further enhanced feature relevance and user confidence in the optimal model.

</details>

## Algorithms and complexity

### [No Polynomial-Time Algorithm For Tarski Fixed Points Unless Cryptographic Assumptions Fail](https://arxiv.org/abs/2611.27977)
*Eleni Batziou, John Fearnley, Alexandros Hollender et al.* · `cs.CC` · arXiv:2611.27977v1 · relevance 0.24

- **In one sentence**: The paper gives a subexponential-time reduction from UEOPL to Tarski fixed-point finding, yielding conditional quasi-polynomial time lower bounds that match known query lower bounds.
- **In plain words**: The paper studies how hard it is to find a "Tarski fixed point," a point that stays put under a certain kind of order-preserving rule applied to a grid of possibilities. The authors show that a known hard search problem (UEOPL) can be translated into this one, so any fast method for Tarski would also give a fast method for UEOPL. Because UEOPL is believed to resist fast solutions under standard cryptographic assumptions, this suggests Tarski fixed points cannot be found in polynomial time either.
- **Why it matters**: It moves the hardness of Tarski fixed points from query-counting arguments to running-time claims conditional on cryptographic assumptions, and the lower bounds line up with previously known query bounds. Whether this changes practical algorithms is not addressed in the text.
- **Background needed**: - Fixed point: an input that maps to itself under a function.
- Tarski fixed point: the guarantee (from Tarski's theorem) that an order-preserving map on a lattice has a fixed point; the computational task is to find one.
- Polynomial vs. quasi-polynomial time: polynomial time grows like a fixed power of input size; quasi-polynomial grows a bit faster (like n to the power of log n) but is still far below exponential.
- Reduction: a way of converting instances of one problem into instances of another, so that solving the second solves the first.
- UEOPL: a search problem on directed graphs (Unique End of Potential Line) used as a standard hard problem in complexity theory.
- Cryptographic assumptions: unproven but widely believed hardness conjectures; the lower bounds are conditional on these.
- Query lower bound: a limit on how many times an algorithm must probe the function, as opposed to total running time. · level: research-level

<details><summary>Original abstract</summary>

We study the time complexity of finding a Tarski fixed point. We provide a subexponential-time reduction from the Unique End of Potential Line (UEOPL) problem to the problem of finding a Tarski fixed point. Using a range of known cryptographic lower bounds for UEOPL, our reduction implies a range of conditional lower bounds on the running time of any algorithm that finds a Tarski fixed point. The strongest of these give quasi-polynomial-time lower bounds for the problem. We also obtain a similar quasi-polynomial-time lower bound for Tarski based instead on a weak exponential-time type hypothesis for UEOPL. These running time lower bounds match the recently discovered quasi-polynomial query lower bounds for the problem.

</details>

### [Compiling Existential-Positive Queries to Bounded-Variable Fragments](https://arxiv.org/abs/2611.26869)
*Christoph Berkholz, Hubie Chen* · `cs.LO` · arXiv:2611.26869v1 · relevance 0.16

- **In one sentence**: The paper studies the formula-size cost of rewriting existential-positive first-order queries into the bounded-variable fragment of positive first-order logic, giving exponential upper bounds, polynomial bounds in some signature/variable regimes, and an unconditional exponential lower bound proved via a link to circuit complexity.
- **In plain words**: Database and logic queries can be written with many variables or with fewer. Using fewer variables makes evaluation faster (in polynomial time), but the rewritten query can become much longer. This paper measures how much longer the rewritten query must be in the existential-positive case, where the query uses only "there exists", "and", and "or".
- **Why it matters**: It addresses a real trade-off between query simplicity and query length, which matters for query optimisation. The unconditional exponential lower bound is claimed to be the first of its kind for this kind of compilation, and the text says the link to circuit complexity may be of future interest; the text does not show further applications.
- **Background needed**: - First-order logic: formulas built from variables, quantifiers ("for all", "there exists"), and connectives like "and" and "or".
- Existential-positive fragment: formulas using only "there exists", "and", "or", with no negation or "for all".
- Bounded-variable fragment: formulas that may reuse a fixed number k of variable names; such formulas can be evaluated in polynomial time.
- Formula size: the length of a formula; an exponential blow-up means the size can grow like 2 to a power of the input size.
- Lower bound: a proof that some rewriting must be at least a certain size, no matter how clever the rewriting.
- Circuit complexity: the study of how large Boolean circuits (networks of logic gates) must be to compute functions. · level: research-level

<details><summary>Original abstract</summary>

A crucial property of bounded-variable fragments of first-order logic is that they can be evaluated in polynomial time. It is therefore a useful preprocessing step to rewrite, if possible, a first-order query to a logically equivalent one with a minimum number of variables. However, it may occur that reducing the number of variables causes an increase in formula size. We investigate this trade-off for the existential-positive fragment of first-order queries, where variable minimisation is decidable in general. In particular, we study the blow-up in the formula size when compiling existential-positive queries to the bounded variable fragment of positive first-order logic. While the increase of the formula size is always at most exponential, we identify situations (based on the signature and the number of variables) where only a polynomial blow-up is needed. In all other cases, we show that an exponential lower bound on the formula size of the compiled formula that matches the general upper bound. This exponential lower bound is unconditional, and is the first unconditional lower bound for formula size with respect to the studied compilation; it is proved via establishing a novel interface with circuit complexity which may be of future interest.

</details>

## Programming languages and formal methods

### [Perceived Differences in Activity and Experience Between Developing Software With and Without AI](https://arxiv.org/abs/2611.27947)
*Rubash Mali, Juho Leinonen, John Edwards* · `cs.SE` · arXiv:2611.27947v1 · relevance 0.20

- **In one sentence**: A study of how software engineers perceive their activities and experience differ when developing with generative AI tools versus traditionally, and how those differences vary with years of programming experience.
- **In plain words**: This paper asks how programming work feels and looks different when engineers use AI tools compared with writing code the traditional way, and whether that depends on how long someone has been programming. Based on engineers' self-reports, they say they talk less with peers about technical problems, break problems down less, search documentation less, use a debugger less, and switch tasks more. They also report less deep focus and less sense of control over their code and design. Engineers who started programming before generative AI existed reported larger changes.
- **Why it matters**: The authors connect these findings to a practical concern: how the next generation of engineers will be trained, and whether experienced engineers will adapt to AI-assisted work. The text is based on perceptions reported by engineers, so it shows how people feel their work has changed rather than measuring productivity or code quality directly.
- **Background needed**: - Generative AI: software that produces text or code in response to prompts, such as coding assistants.
- Software engineering activities: writing, refactoring (restructuring code without changing what it does), and debugging (finding and fixing errors).
- Decomposition: breaking a large problem into smaller parts.
- Task switching: moving attention back and forth between different tasks.
- Experience gradient: the pattern where the effect grows with years of prior experience, as described in the paper.
- The study relies on self-reported perceptions, so the findings describe how engineers perceive change, not objective outcomes. · level: intermediate

<details><summary>Original abstract</summary>

The fundamental changes in software engineering driven by generative AI will have profound effects not only on the number of available software engineering jobs but also on what software engineering itself looks like. As the career evolves, questions arise about what the skillset and interests of the next generation of software engineers will be and whether long-time engineers will continue to be attracted to the career. In this paper, we contribute to answering these questions by studying how software development with AI tools is perceived to differ from traditional development and how the differences are modulated by years of programming experience. We find that, in terms of programming activities, engineers report less talking with peers about technical problems, less decomposition, less searching of documentation, and less using a debugger, while they report more task switching. We also find experiential differences, including less deep focus and less sense of control over code and design. We call these the different craft results, in contrast to core code-production activities such as writing, refactoring, and fixing code, which show only small mean differences. We also find that these differences are amplified by years of programming experience (an experience gradient), with software engineers who started programming before the age of generative AI perceiving greater changes in both activity and developer experience. We discuss our findings and their implications on training of the next generation of engineers and on engineers who may have difficulty transitioning to the AI-infused world of software engineering.

</details>

### [Compositional Temporal Specifications for Interaction Trees](https://arxiv.org/abs/2611.27553)
*Linyu Yang, Jianwei Yin, Mingshuai Chen* · `cs.PL` · arXiv:2611.27553v1 · relevance 0.07

- **In one sentence**: The paper introduces iBuchi, a shallowly embedded temporal specification language over Choice Trees for reasoning about the ordering of observable interactions in Interaction Trees, integrated into the Dijkstra Monads Forever framework and mechanized in Rocq.
- **In plain words**: Programs that interact with their surroundings, such as reading input or sending output, are judged not only by their final answer but also by the order in which those interactions happen over time. This paper gives a reusable way to write down and check such time-ordered requirements for programs represented as Interaction Trees. The authors formalize the framework in the Rocq proof assistant and test it on several non-trivial case studies.
- **Why it matters**: Verifying the timing and order of a program's interactions matters for software that must behave correctly over long runs, such as servers or controllers. The text says the framework is compositional, so temporal properties can be combined with ordinary pre- and post-condition style specifications, though the text does not report direct comparisons with other tools.
- **Background needed**: - Interaction Trees: a way to represent a program's behaviour as a possibly infinite tree of its observable interactions with the environment.
- Choice Trees: the tree structure of possible interaction choices that iBuchi is built on.
- Temporal specifications: requirements about the order of events over time, such as "a request is eventually answered".
- Linear Temporal Logic (LTL): a standard logic for stating such ordering requirements, with operators like "always" and "eventually".
- Hoare-style specifications: pre- and post-condition statements used to verify programs.
- Dijkstra Monads: a framework for verifying effectful programs using monads and weakest-precondition-style reasoning.
- Rocq: a proof assistant used to write and mechanically check formal proofs. · level: research-level

<details><summary>Original abstract</summary>

The correctness of modern effectful programs depends not only on their final results but also on the temporal evolution of observable interactions with their environments. Interaction Trees (ITrees) provide a reusable denotational semantics for such programs by representing effectful computations as potentially infinite trees of observable interactions. However, reusable temporal reasoning over ITrees remains largely unexplored. This paper presents a compositional temporal specification framework for ITrees. We introduce iBuchi, a shallowly embedded temporal specification language based on Choice Trees, which represents finite and infinite interaction traces and supports expressive temporal operators, including sequencing, branching, conjunction, repetition, and Linear Temporal Logic modalities. We define trace- and tree-level satisfaction relations between iBuchi specifications and ITrees, together with compositional reasoning principles for modular verification of effectful programs. We integrate iBuchi into the Dijkstra Monads Forever framework, thereby enabling temporal specifications to compose with conventional Hoare-style specifications and supporting a generator-based encoding of future conditions. We have formally developed and verified our framework in Rocq and demonstrated its expressiveness and compositionality through several non-trivial case studies.

</details>

## Systems and networking

### [Bring Cloud-Native Networking to FreeBSD Jails: Porting Calico from Linux](https://arxiv.org/abs/2611.27320)
*Soma Sakaguchi, Shintaro Suzuki, Yuki Nakata et al.* · `cs.OS` · arXiv:2611.27320v1 · relevance 0.13

- **In one sentence**: The paper describes porting Calico, a widely used Kubernetes-style container networking plugin, to FreeBSD Jails by swapping Linux networking components for FreeBSD equivalents (ipfw, routing sockets, and vnet).
- **In plain words**: Software "containers" let many isolated programs share one computer, and a networking plugin decides how they talk to each other and to the outside world. Linux has mature plugins for this, but FreeBSD's equivalent isolation feature, called Jails, did not have a standard option, so users often set networking up by hand. This paper reports on adapting one popular plugin, Calico, to run on FreeBSD by replacing Linux-only parts with FreeBSD's own tools.
- **Why it matters**: It matters for anyone who wants FreeBSD to work in modern container platforms rather than as a manual special case. The text is a short abstract, so it does not report measured results, and I cannot tell from it how complete or performant the port is.
- **Background needed**: - Containers: isolated environments that share one operating system kernel.
- FreeBSD Jails: FreeBSD's built-in container-like isolation.
- CNI plugin: a standard add-on that sets up network connections for containers in orchestration tools such as Kubernetes.
- Calico: a widely adopted CNI plugin that applies networking and security policy rules.
- iptables / ipfw: packet-filtering rule systems on Linux and FreeBSD respectively.
- Netlink / routing sockets: the kernel interfaces programs use to read and change network settings.
- Network namespaces / vnet: per-container private network stacks on Linux and FreeBSD respectively. · level: intermediate

<details><summary>Original abstract</summary>

While Linux containers benefit from a rich ecosystem of Container Network Interface (CNI) plugins such as Calico and Cilium, FreeBSD Jails lacked native, standardized solutions for advanced networking. As a result, users have relied on manual, error-prone configurations, limiting scalability and integration with modern orchestration platforms. This paper introduces porting Calico, a widely adopted CNI plugin, to the FreeBSD operating system. Our approach replaced Linux-specific components with FreeBSD-native equivalents: iptables with ipfw, netlink sockets with routing sockets, and Linux network namespaces with FreeBSD's vnet. This work aims to bridge the gap between Linux and BSD container networking. By providing scalable, policy-driven capabilities that are compatible with existing Linux-centric infrastructure, FreeBSD can participate more fully in the broader container networking ecosystem.

</details>

### [Contention-Aware Flexible Execution for Machine Learning Workloads](https://arxiv.org/abs/2611.26840)
*Marco Kurzynski, Shaizeen Aga, Di Wu* · `cs.DC` · arXiv:2611.26840v1 · relevance 0.12

- **In one sentence**: A characterization of how concurrently running GPU kernels slow each other down on AMD MI300X hardware, followed by CAFEML, a contention-aware scheduler that tunes operator overlap and resource allocation for ML training and inference, reporting up to 13% end-to-end speedup without kernel rewrites.
- **In plain words**: Modern AI software runs many small computing tasks (called kernels) at the same time on a graphics processor, and they compete for shared parts of the chip such as memory and cache, so each can slow down. The authors measured this slowdown in detail on a current AMD datacenter GPU, then used those findings to change when and how tasks are overlapped. Their scheduling changes alone reportedly gave up to a 13% speedup across training and inference workloads.
- **Why it matters**: AI workloads run on expensive datacenter hardware, so a speedup obtained only by changing scheduling, not by rewriting code, could matter for cost and efficiency. The text does not say how the results would transfer to other hardware or software stacks, so that remains open.
- **Background needed**: - GPU: a chip with many parallel cores, widely used for AI.
- Kernel: a single program or computing task launched on a GPU.
- Concurrent execution: running several kernels at once so they share the chip's cores, caches and memory bandwidth.
- Contention: competition for the same limited resource, which slows each task.
- Operator: one step of an ML model's computation (e.g., a matrix multiply).
- Training vs. inference (prefill and decode): building a model vs. using it to generate outputs; prefill and decode are two phases of generating text.
- Scheduling heuristic: a rule of thumb for deciding the order and placement of tasks. · level: research-level

<details><summary>Original abstract</summary>

Concurrent kernel execution is a ubiquitous paradigm in artificial intelligence (AI) and machine learning (ML) across both training and inference. That said, concurrency causes potential slowdown as concurrent kernels contend for limited GPU resources (cores, caches, memory bandwidth), which are shared between these kernels rather than exclusively available to one, as in isolated execution. This raises an important research question: to what extent does concurrency slow down kernel execution and how can it be mitigated. To answer this question, our work presents two studies. First, we characterize concurrent kernel execution extensively for the first time, to our knowledge. We conduct not just performance analysis of concurrent kernels but also memory behavior under concurrency on state-of-the-art AMD Instinct MI300X GPUs designed for datacenter AI, using the AMD-internal millisecond sampler. Based on the observations, we share insights on the slowdown along two dimensions (memory vs. compute bound, large vs. small kernels) to inform future optimizations. Second, we put the derived insights to use, aiming to deliver higher performance via targeted, flexible overlap of ML operators. Frameworks today make the simple decision of early-first for concurrent kernels, which is suboptimal. Noticing the opportunity that ML dataflow has inherent flexibility in which operators can be overlapped and how hardware resources can be allocated, we deduce simple heuristics to tune both overlap anchors and resource allocation for concurrent kernels to improve performance. We evaluate our proposed contention-aware flexible execution (termed CAFEML) across a variety of ML scenarios (inference decode, inference prefill, training) and demonstrate a speedup of up to 13% end-to-end with simple scheduling changes and no kernel rewrites.

</details>

## Human-computer interaction

### [AROMA: Understanding AI Support For Mental Well-being through Role Theory](https://arxiv.org/abs/2611.26843)
*Issac Ting, Ethan Pan, Koustuv Saha et al.* · `cs.HC` · arXiv:2611.26843v1 · relevance 0.05

- **In one sentence**: The paper proposes AROMA, a role-based framework that annotates over 7,515 conversations from 13 datasets to derive eight observed "Role States" for AI mental well-being supporters, and uses them to analyze context, structure, timing, and prompting for better role alignment.
- **In plain words**: AI chatbots that offer emotional support sometimes act outside what they were meant to do, which can hurt the person they are talking with. Standard tests check only whether these tools work in narrow, specific tasks, and they do not explain why the gap between intended and actual behavior happens. The authors labeled thousands of real support conversations, grouped the behavior into eight recurring "role states" based on what the AI was observed doing, and used these to compare AI and human supporters.
- **Why it matters**: As AI tools for mental well-being spread, a shared way to describe what role they actually play could help explain failures that narrow testing misses. The text does not show how well the framework works outside the studied datasets, so its practical value remains to be tested.
- **Background needed**: - Role theory: the idea that people behave according to expected social parts (e.g., friend, counselor), and trouble arises when actual behavior departs from those expectations.
- Annotation: human or systematic labeling of conversation text with categories, used here to build the framework.
- "Observed, not prescribed" behavior: the categories come from what supporters were seen doing, not from rules about what they should do.
- Prompting: the written instructions given to a language model to steer its responses; the paper proposes a prompting strategy to improve role alignment.
- Relational harm: damage to the trust or relationship between a user and a supporter. · level: intermediate

<details><summary>Original abstract</summary>

AI supporters for mental well-being are becoming more prevalent. When these AI supporters start acting in ways beyond their expected function it leads to relational harm. Standard approaches to evaluating such AI supporters are limited to inspecting their efficacy in narrow task-specific settings, which do not explain these discrepancies in expected and actual behavior. To address this gap, we propose the AROMA (A Role-Oriented Model of Analysis) framework to provide a common role taxonomy for different support contexts. We developed AROMA using a theory-informed annotation of over 7,515 conversations from 13 datasets and propose eight "Role States" based on observed-not prescribed-behavior. We show these Role States vary according to the context of support; depict unique structural and temporal characteristics of AI supporters vis-a-vis Humans; and inform novel AI support prompting strategy for better role alignment. This framework provides a new lens to understand AI support failures.

</details>

### [A Frugal AI Framework for India: Responsible and Right-sized AI](https://arxiv.org/abs/2611.27189)
*Balaraman Ravindran, K. S. Venkataraghavan, Gokul S Krishnan et al.* · `cs.CY` · arXiv:2611.27189v1 · relevance 0.04

- **In one sentence**: A CeRAI (IIT Madras) white paper proposes "Responsible Frugal AI" for India, combining frugal engineering with Responsible AI across four dimensions (data, compute, model, operations), seven levers, a seven-point adoption checklist and eleven policy statements.
- **In plain words**: This white paper argues that India should not try to copy the huge, expensive AI models built in the United States or China, nor simply adopt foreign AI with local tweaks. Instead it proposes a third approach: pick the smallest, cheapest AI that does the job well enough, check that it is reliable and governed responsibly, and keep resource use in check. The text is a framework and set of recommendations; it does not report experimental results.
- **Why it matters**: India must serve a very large and diverse population with limited budgets and uneven infrastructure, so questions about cost, energy and public value of AI matter there. The text is a policy and framework proposal, so its practical impact depends on how far its checklist and policy statements are adopted; the excerpt gives no evidence of that yet.
- **Background needed**: - "Frugal engineering": designing products to be cheap, simple and sufficient rather than maximal.
- "Foundation model": a very large general-purpose AI model trained on huge datasets, costly in computing power and money.
- "Compute": the processing power, usually in data centres, needed to train and run AI.
- "Responsible AI": practices for making AI fair, safe, transparent and accountable.
- "Digital public infrastructure": shared government-run digital systems (such as identity or payment platforms) that others can build on.
- "Vernacular-first": designing for local languages first.
- "Sovereignty": a country's ability to control, inspect and adapt the AI systems it relies on.
- "Joule": a unit of energy, used here to mean energy efficiency. · level: introductory

<details><summary>Original abstract</summary>

India's AI debate often swings between two insufficient options: replicating the compute-intensive, capital-heavy foundation-model programmes of the United States or China, or remaining a downstream adopter of foreign AI with localised interfaces and safeguards. Neither serves a country that must deliver AI to a very large, diverse population across uneven infrastructure and within constrained budgets. This white paper from the Centre for Responsible AI (CeRAI), IIT Madras, proposes a third path: Responsible Frugal AI, which applies principle-based frugal engineering alongside Responsible AI. Responsible Frugal AI is right-sized AI: it fixes the functional requirement first, asks whether AI is needed at all, and then chooses the smallest sufficient model, meeting the requirement with minimal resources while keeping a verified margin, robustness and responsible governance. The framework applies frugality across four dimensions (data, compute, model and operations) through seven levers spanning the AI lifecycle, each with practices and measures. It calls for public AI rails, vernacular-first design, measured resource use, human oversight for high-stakes decisions, and a cap on total resource consumption so that efficiency gains are not cancelled out by rising usage. We argue that India is resource-imbalanced rather than resource-poor, and that frugal principles offer the most viable route to population-scale deployment, fit naturally with India's digital public infrastructure, and make sovereignty operational by preserving India's capacity to specify, deploy, govern, inspect and adapt its AI systems. A seven-point adoption checklist and eleven policy statements translate the framework into practice, positioning AI in India as a responsible, frugal public-value system that maximises social value per rupee and per joule.

</details>

## Information theory

### [Coding Length and Optimal Power Allocation in Correlated Block Fading](https://arxiv.org/abs/2611.27694)
*Haoran Xu, Huazhong Zhao* · `cs.IT` · arXiv:2611.27694v1 · relevance 0.06

- **In one sentence**: For a Gaussian block-fading channel with correlated fades and a receive array whose size grows, the paper characterizes when outage capacity is the right rate and gives the exact limiting rate under a per-codeword energy constraint when the block-length-to-array-size ratio is large enough, with a 1/ratio leading loss term and power-allocation examples for correlated fading.
- **In plain words**: The paper studies how fast data can be sent reliably over a wireless link whose signal strength fluctuates in correlated bursts, such as fading caused by moving obstacles. The sender knows only the statistical pattern of the fading, not the actual fades, and the receiver uses many antennas so that errors must become exponentially rare. The authors find when the usual "outage" estimate of the rate is accurate, when it overestimates the true rate, and how the sender should split its energy across the blocks.
- **Why it matters**: It refines a standard engineering estimate (outage rate) by quantifying exactly when and by how much it is too optimistic, which matters for designing reliable wireless links. The text does not discuss specific applications beyond wireless communication, so broader connections are unclear.
- **Background needed**: - Block fading: the channel gain stays constant within a block and changes between blocks.
- Outage: the event that the channel is too weak to support a chosen rate; outage rate is the rate that can be met except in that event.
- Error exponent: how quickly the probability of decoding error shrinks as the code or array grows.
- Channel dispersion: a measure of how much random variation in a Gaussian channel affects the achievable rate at finite block length.
- Power allocation: how a fixed total energy is divided among the blocks of a codeword.
- Autoregressive (AR(1)) fading: fading where each block's gain is correlated with the previous one, with correlation measured by the lag-one coefficient. · level: research-level

<details><summary>Original abstract</summary>

A codeword spans a fixed number of correlated Gaussian fading blocks. The receiver knows the gains and the transmitter knows only their law. At fixed average signal-to-noise ratio, we require the decoding error probability to decay exponentially with the number of receive antennas. When does outage predict the achievable rate? If block length grows faster than the number of antennas, outage gives the limiting optimal rate. If both grow to infinity at a fixed positive ratio of block length to array size, outage strictly overestimates the limiting rate. We determine the critical ratio above which positive rates are possible. For sufficiently large finite ratios, we find the exact limiting rate over all codes satisfying a total energy constraint on each codeword. The leading rate loss is inversely proportional to the ratio. Its coefficient depends on Gaussian channel dispersion at the most likely fade causing outage and on how quickly the outage rate decreases as the required error exponent increases. In the long-block limit, equal power loses rate on every window of three or more blocks under stationary first-order autoregressive fading with positive lag-one correlation. In a different three-block channel with identical marginal gains, tightening the reliability requirement first makes it optimal to leave the middle block unused and later to use it again.

</details>

### [$L^1$ stability of the entropy power inequality in $\mathbb{R}^d$ without moment assumptions](https://arxiv.org/abs/2611.27790)
*Norman El Fartass, Lampros Gavalakis, Ioannis Kontoyiannis* · `cs.IT` · arXiv:2611.27790v1 · relevance 0.04

- **In one sentence**: The paper proves qualitative stability of Shannon's entropy power inequality in R^d in L^1 and Ruzsa distance without moment assumptions, using an optimal transport argument, majorization of density rearrangements, and Christ's stability result for sharp Young's inequality.
- **In plain words**: The paper studies a basic inequality about how the "spread" of random quantities adds up when they are combined. It asks what happens when the inequality is almost tight, and it shows that the two random vectors involved must then be close to Gaussian-like in a precise sense. The result holds in any number of dimensions and does not require the random quantities to have finite moments, which is a technical restriction that earlier results needed.
- **Why it matters**: Stability results say that near-equality in a sharp inequality forces near-extremal structure, which matters for understanding when the bound is tight and for making it usable in practice. The text does not say what applications it may have, and it describes the result as qualitative, meaning it gives no explicit rate of closeness.
- **Background needed**: - Differential entropy: a measure of spread or uncertainty for a continuous random vector, the continuous analogue of Shannon entropy.
- Entropy power inequality: a sharp bound saying the entropy power (a rescaled exponential of entropy) of a sum of independent random vectors is at least the sum of their entropy powers; equality holds only for Gaussians.
- Stability: if a near-equality holds, the objects are close to the equality case; "qualitative" means closeness is shown without a quantitative rate.
- L^1 distance: the total absolute difference between two probability densities; Ruzsa distance is a distance between random vectors used in additive combinatorics and information theory.
- Moments: averages of powers of a random variable (such as variance); "no moment assumptions" means the result works even for heavy-tailed distributions.
- Optimal transport: a way of moving one distribution into another at minimal cost, used here as a proof tool.
- Young's inequality: a sharp inequality about convolutions of functions, whose stability is used as an ingredient.
- de Bruijn's identity: a formula linking the rate of change of entropy under added Gaussian noise to Fisher information. · level: research-level

<details><summary>Original abstract</summary>

We establish qualitative stability in $L^1$ and Ruzsa distance for Shannon's entropy power inequality in $\mathbb{R}^d$, without any moment assumptions. The proof uses the optimal transport argument by Rioul (2017), majorization bounds of density rearrangements, and the stability of the sharp form of Young's inequality due to Christ (2019). Along the way we also extend recent one-dimensional results on de Bruijn's identity, the continuity of differential entropy, and the equality case of the entropy power inequality to random vectors of any dimension.

</details>

## High-energy theory and gravity

### [Type-II quasinormal modes of dilaton--Euler--Heisenberg AdS black holes](https://arxiv.org/abs/2611.27195)
*Chao-Ming Zhang, Fu-Wen Shu, Yun Soo Myung et al.* · `gr-qc` · arXiv:2611.27195v1 · relevance 0.20

- **In one sentence**: Computes coupled gravitational, dilaton and electromagnetic quasinormal modes (ℓ=0,1,2) of a magnetically charged dilaton–Euler–Heisenberg black hole in AdS, using direct integration and Chebyshev pseudospectral methods, and links the ℓ=0 dilaton modes to the black hole's thermodynamic phase transition.
- **In plain words**: The paper studies how a charged black hole in a curved, AdS-type universe "rings down" after being disturbed, much like a struck bell settling. The ringing has characteristic frequencies and decay rates, and here the authors compute them for a mix of gravity, a scalar field (the dilaton) and electromagnetism. They report that all computed modes decay for non-extremal black holes, so the black hole is stable against these perturbations, and that the ringing frequencies shift in a specific way with charge and with temperature near a thermodynamic phase transition.
- **Why it matters**: The work is a theoretical calculation within a specific model, so its direct relevance is to gravity theory and black hole physics rather than to observation. Its proposed link between quasinormal modes and a thermodynamic phase transition is the most distinctive part, and its significance depends on how well that connection holds beyond this model; the text alone does not show that.
- **Background needed**: - Black hole quasinormal modes: characteristic complex frequencies at which a black hole rings after a disturbance; the real part gives the oscillation rate and the imaginary part gives how fast it decays.
- AdS (anti-de Sitter) spacetime: a universe with negative curvature that acts like a box, so perturbations behave differently than in flat space.
- Dilaton: an extra scalar field that couples to electromagnetism in this model; the Euler–Heisenberg term is a nonlinear correction to electromagnetism from quantum effects.
- Multipole ℓ: the angular "shape" of a perturbation (ℓ=0 monopole, ℓ=1 dipole, ℓ=2 quadrupole).
- Type-II perturbations: coupled gravitational, dilaton and electromagnetic disturbances treated together.
- Thermodynamic phase transition: an abrupt change in a system's state (here, between small and large black holes) as temperature or pressure varies.
- Numerical methods: direct integration of equations and Chebyshev pseudospectral methods, two ways of solving the equations on a computer. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we investigate Type-II quasinormal modes (QNMs) of a magnetically charged dilaton--Euler--Heisenberg black hole in anti-de Sitter (AdS) spacetime. The Type-II includes coupled gravitational, dilaton and electromagnetic perturbations. Its coupled equations are derived for $\ell=0,1,2$ modes and the QNM frequencies are calculated by employing direct integration and Chebyshev pseudospectral methods, giving consistent results. For nondegenerate dipole ($\ell=1$) mode at fixed curvature, the nonlinear correction starts at order $Q^2$ for electromagnetic-led branch and at order $Q^4$ for scalar-led branch. In this case, stronger AdS curvature enhances reduction of the electromagnetic-led real frequency for positive coupling, while gravitational-led quadrupole real frequency changes weakly with charge. As the curvature weakens, the dipole frequencies approach the AdS normal-mode scale and their damping decreases. We find that all modes computed have negative imaginary parts for nonextremal black holes, implying this black hole is stable against Type-II perturbations. Furthermore, we explore the connection between thermodynamic phase transition and QNMs for $\ell=0$ dilaton. For a subcritical isobaric process, the QNM real frequency of $\ell=0$ dilaton decreases with increasing temperature of small black holes, while it increases with increasing temperature of large black holes. At coexistence, the damping rate for large black holes is about 4.28 times that for small black holes.

</details>

### [Onset of quantum chaos in a family of two-dimensional conformal field theories](https://arxiv.org/abs/2611.26694)
*Felix M. Haehl, Moshe Rozali* · `hep-th` · arXiv:2611.26694v1 · relevance 0.16

- **In one sentence**: In a family of two-dimensional K3 sigma models near the Kummer orbifold point, first-order splittings of degenerate non-BPS scaling dimensions along generic blow-up deformation directions follow GOE statistics, unlike the singlet deformation, which keeps extra degeneracies and shows weaker rigidity.
- **In plain words**: This paper studies a family of two-dimensional quantum field theories, which are idealized models of physics on a surface. At a special point, many energy levels coincide exactly. The authors nudge the theory in small directions and measure how these levels split apart, then check whether the pattern of spacings looks like the random-matrix statistics familiar from chaotic quantum systems.
- **Why it matters**: The question of when a quantum field theory starts to look "chaotic" in its spectrum is an active topic linking quantum field theory, gravity-inspired models, and random matrix theory. The comparison with the well-known singlet deformation, which keeps extra symmetries and degeneracies, suggests that symmetry content controls how random the spectrum looks. The text does not establish any broader implication beyond this model family.
- **Background needed**: - Two-dimensional conformal field theory: a quantum theory on a 2D surface with scale invariance; its states have "scaling dimensions" playing the role of energy levels.
- Sigma model with K3 target space: a string-theory-inspired model whose fields live on a K3 surface, a special four-dimensional shape.
- Supersymmetry (N=(4,4)): an extra symmetry pairing bosons and fermions; BPS operators are protected states whose dimensions do not change, while non-BPS ones can shift.
- Orbifold point: a special geometric point where the space is a quotient by a symmetry group (here T^4/Z_2).
- Marginal deformation: a small change to the theory that leaves its scale invariance intact; the coupling is the size of this change.
- First-order splitting: the leading shift in energy levels for small coupling, computed from degenerate perturbation theory.
- Random matrix theory and GOE (Gaussian orthogonal ensemble): a statistical model for spacings of levels in chaotic systems; diagnostics include the gap ratio and rigidity of unfolded spectra.
- Unfolding: rescaling a spectrum so the average level density is uniform before comparing statistics. · level: research-level

<details><summary>Original abstract</summary>

We exhibit random matrix statistics in the scaling dimensions of non-BPS primary operators in a family of two-dimensional conformal field theories. Specifically, we consider the sigma model with K3 target space and $\mathcal N=(4,4)$ supersymmetry in a neighborhood of the Kummer orbifold point $\mathbb T^4/\mathbb Z_2$. At the free-fermion radius, the spin-zero spectrum of the $\mathbb Z_2^4$-invariant sector is exactly degenerate at integer energies. The exactly marginal blow-up deformations that preserve this symmetry form a four-dimensional space, whose directions we parametrize by unit quaternions. Along each deformation direction, we compute the first-order splitting of the degenerate levels, i.e., the leading anomalous dimensions as the coupling goes to zero. In sectors where all exact symmetries are resolved, including a hidden $\mathbb Z_2$ at the even levels, the non-zero first-order shifts along a generic direction follow the Gaussian orthogonal ensemble (GOE), as we verify by computing several spectral diagnostics. We compare quantitatively with the well-known singlet deformation, which has enhanced symmetry: even after all its known symmetries are resolved, its first-order spectrum has exact degeneracies, its gap ratio approaches the GOE value only slowly as the energy increases, and its unfolded spectrum lacks the long-range rigidity of the GOE.

</details>

## Statistical physics

### [Large deviations, effective dynamics, and dynamical phase transitions in random maps](https://arxiv.org/abs/2611.26704)
*\'Angela Tajuelo-Valbuena, Jorge Hidalgo, Ricardo Guti\'errez et al.* · `cond-mat.stat-mech` · arXiv:2611.26704v1 · relevance 0.20

- **In one sentence**: The paper extends the Doob transform and spectral large-deviation methods, previously used for deterministic chaotic maps, to random maps, to build effective dynamics for rare trajectories and to identify dynamical phase transitions.
- **In plain words**: The paper studies rare behaviour in systems that evolve in discrete steps with a random element, such as unusually long-lasting or unusually active runs of a process. The authors show how to reshape the dynamics so that these rare runs become typical and can be simulated directly, rather than being nearly impossible to sample. They also use the mathematical structure of a modified operator to see which starting states lead the system into one behaviour regime or another.
- **Why it matters**: Rare fluctuations and sudden switches between behaviour regimes matter in many physical and biological settings, so a general way to sample them is useful. The text itself is a summary of methods and does not report specific numerical results or applications, so its practical reach beyond these model systems is unclear from the abstract alone.
- **Background needed**: - Random map: a rule that updates a system's state in discrete time steps, with some randomness at each step.
- Large deviation theory: the study of how unlikely it is for a long-run average to deviate from its usual value, and how those unlikely outcomes are shaped.
- Doob transform: a mathematical reweighting that turns a rare-event process into a new process in which those events are the ordinary ones.
- Tilted operator: a modified version of the system's averaging rule, weighted to favour a chosen kind of rare behaviour; its spectrum (set of characteristic values) reveals how the system behaves.
- Dynamical phase transition: an abrupt change in the typical type of trajectory as a control parameter or bias crosses a threshold, analogous to melting or boiling but for paths over time. · level: research-level

<details><summary>Original abstract</summary>

Large deviation theory provides a natural framework to characterize rare fluctuations of time-averaged observables in deterministic and stochastic systems. Building on previous results for deterministic chaotic maps, here we extend the Doob transform to random maps, constructing an effective dynamics in which rare events become typical. This makes it possible to directly reproduce the dynamics of rare trajectories that are exponentially difficult to sample under the original dynamics. We further apply spectral large-deviation methods to characterize dynamical phase transitions in random maps. The spectral structure of the tilted operator provides insight into the mechanisms underlying these transitions and, in particular, allows us to identify the appropriate initial states that select one dynamical phase or another. Our results extend the connection between large deviation theory, spectral methods, and effective dynamics to random chaotic maps, providing a general framework to study rare events and dynamical phase transitions in these systems.

</details>

### [Cup and Cap Topological Neural Network](https://arxiv.org/abs/2610.03169)
*Marta Niedostatek, Ferran Hernandez Caralt, Runyue Wang et al.* · `cond-mat.dis-nn` · arXiv:2610.03169v2 · relevance 0.15

- **In one sentence**: The paper proposes the Cup and Cap Topological Neural Network (CCNN), which uses cup and cap products from algebraic topology to move signals between simplicial dimensions in one layer and learn node features that account for higher-order (e.g. triangle) interactions, and reports competitive results on TopoBench datasets.
- **In plain words**: Standard neural networks for data shaped like networks or meshes mostly pass information between neighbouring nodes and edges. This paper proposes a new architecture that also lets information jump across several levels of structure in a single step, such as from points to the triangles they form. The authors test it on benchmark datasets and report performance that is competitive with other networks built on similar shapes.
- **Why it matters**: Topological deep learning is an active area, and the paper targets a specific stated limitation: existing methods can only move features one dimension per layer. Whether the reported gains matter more broadly is not clear from the text alone, since it claims only competitive performance.
- **Background needed**: - Simplicial complex: a data structure built from points (nodes), links between them (edges), filled triangles, and higher analogues.
- Cochain: an assignment of values (signals) to the simplices of one dimension, such as numbers on nodes.
- Boundary operator and Hodge Laplacian: standard tools that move signals between neighbouring dimensions, typically one step at a time.
- Cup and cap products: operations from algebraic topology that combine signals across dimensions, allowing jumps of more than one level.
- Many-body interaction: a relationship involving more than two items at once, such as three nodes forming a triangle.
- TopoBench: a benchmark suite used to compare topological neural networks. · level: research-level

<details><summary>Original abstract</summary>

Topological Deep Learning (TDL) is designed to learn features associated not only with nodes but also with edges, triangles and higher dimensional simplices. However, most TDL approaches, being based on boundary operators and Hodge Laplacians, have the limitation that features and signals cannot be lifted or lowered across more than one dimension per layer. To overcome this limitation, in this work, we propose the adoption of the cup and cap products. Specifically, we formulate the Cup and Cap Topological Neural Network (CCNN), a topological deep learning architecture designed to learn node-based variables (or 0-cochains) by taking into account their many-body interactions (e.g. triangles) present in the data. We validate CCNN by assessing its performance on the TopoBench datasets, demonstrating its competitive performance with respect to other simplicial complex neural networks.

</details>

## Condensed matter

### [Topological phases protected by half-chiral symmetry](https://arxiv.org/abs/2611.26693)
*Chen-Shen Lee, Itamar Kimchi* · `cond-mat.mes-hall` · arXiv:2611.26693v1 · relevance 0.21

- **In one sentence**: The paper proposes new topological phases protected by "half-chiral" symmetry, where chiral (sublattice) symmetry holds on only one sublattice, defined algebraically via a constraint PHP=0, with real-space invariants and a half-chiral Kekulé honeycomb model showing higher-order boundary modes.
- **In plain words**: Materials in which electrons hop between two interleaved sets of sites can host edge states pinned at zero energy, and these are robust because of a symmetry that forbids same-type hops. This paper looks at a case where that symmetry holds only on one of the two sets, as can happen in some layered or orbital-based materials. The authors build a new way to classify and protect such phases and give a model in two dimensions where a single zero-energy mode sits at one corner.
- **Why it matters**: It extends the familiar idea of topological protection to a symmetry that is an algebraic constraint rather than a group-theory operator, which may matter for designing edge or corner states in real materials such as graphene on hexagonal boron nitride. The text does not report experiments, so any link to devices is speculative.
- **Background needed**: - Topological phase: a property of a material's electronic structure that stays fixed under small changes, so edge states are robust.
- Bipartite lattice / sublattice: a lattice whose sites split into two groups (A and B) where hopping only occurs between groups.
- Chiral (sublattice) symmetry: forbidding hops within the same group, which pins certain edge modes at zero energy (e.g. the SSH chain).
- Hamiltonian H: a matrix describing the energies and hopping of electrons; P projects onto one sublattice, so PHP=0 means no hopping within that sublattice.
- Higher-order topology: boundary modes appear at corners or hinges rather than along edges.
- Graphene and hBN: atomically thin layers forming a honeycomb lattice; hBN can make the two sublattices unequal. · level: research-level

<details><summary>Original abstract</summary>

Chiral (or sublattice) symmetry describes bipartite systems such as the Su-Schrieffer-Heeger (SSH) chain where same-sublattice A-A and B-B hoppings are forbidden, enabling the protection of topological phases. Here we identify new topological phases protected by half-chiral symmetry wherein chiral symmetry is preserved on only one sublattice, as may occur with sublattice imbalance (e.g. graphene-hBN) or localized orbitals (e.g. zincblende). Unlike conventional symmetry operators described by group theory, half-chiral symmetry is an algebraic constraint on the sublattice-projected Hamiltonian such as $PHP=0$, requiring a new framework for topological protection. We develop such a framework, identifying real-space bulk topological invariants and corresponding topological boundary modes that stick to zero energy. In two dimensions we construct a half-chiral Kekule honeycomb model and show that its unusual higher-order topology protects a single zero-energy mode at a single corner.

</details>

### [Comparing weakly interacting and free quantum dynamics locally](https://arxiv.org/abs/2611.27707)
*Jorge Acu\~na Flores, Joscha Henheik, Marius Lemm et al.* · `math-ph` · arXiv:2611.27707v1 · relevance 0.15

- **In one sentence**: Using Lieb-Robinson bounds to show that weakly interacting many-body quantum dynamics can be locally approximated by free (non-interacting) one-body dynamics, yielding quantum diffusion results for weakly interacting Fermi systems and free-correlator approximations for low-spin-down Fermi-Hubbard models.
- **In plain words**: This paper studies how particles in a crowded quantum system spread and interact over time. The authors show that, over long but finite stretches of time, a local piece of a weakly interacting system behaves much like a simpler system where the particles ignore each other. They use this to carry over known results for non-interacting particles to two settings: spreading of quantum information in weakly interacting, weakly disordered fermions, and spin correlations in the Fermi-Hubbard model when spin-down particles are sparse.
- **Why it matters**: Many-body quantum transport is hard to analyze directly, so reducing it to the easier non-interacting case on finite time scales is a useful technical bridge. The text ties the Fermi-Hubbard result to numerical observations of short-time entanglement patterns by Bippus et al., but the text does not say how far that connection goes.
- **Background needed**: - Quantum many-body system: many interacting quantum particles on a lattice.
- Lieb-Robinson bound: a limit on how fast influence or information can spread through a local quantum system, analogous to a speed-of-light bound.
- Non-interacting (free, one-body) dynamics: particles that do not affect each other, so each evolves separately and is easier to solve.
- Quantum diffusion: spreading of quantum information or operators at a rate like random walks, which is slower than ballistic spreading.
- Operator spreading and OTOC (out-of-time-ordered correlator): diagnostics measuring how local quantum operators grow and scramble over time.
- Fermi-Hubbard model: a standard lattice model of interacting electrons with spin, often used in condensed matter physics.
- Perturbative regime: results valid when the interaction strength is small. · level: research-level

<details><summary>Original abstract</summary>

Lieb-Robinson bounds (LRBs) have become a standard tool for perturbative results in quantum many-body physics, including gap stability and many-body adiabatic theory. Here, we use LRBs to locally approximate weakly interacting many-body dynamics with one-body dynamics on large, perturbative time scales. This allows us to use one-body transport results to establish the expected many-body transport behavior on finite time scales in the following two illustrative settings: (i) We prove quantum diffusion, as quantified by a certain operator spreading diagnostic, in weakly interacting and weakly disordered Fermi systems in dimensions $D\geq2$ on large finite time scales based on the non-interacting diffusion result of Black, Drogin, and Hern\'andez [arXiv:2506.06468]. (ii) We show for Fermi-Hubbard models with initially low spin-down density, that all local multi-time spin-up correlation functions are approximated by their free counterparts. In particular, we obtain an OTOC (out-of-time-ordered correlator) counterpart to the patterns of short-time entanglement related to lattice path counts observed numerically by Bippus et al. [Phys. Rev. B 113, 035152 (2026)].

</details>

## Particle physics

### [Probing Compressed Dark Sectors at a Muon Collider through Dilepton Signatures and Machine Learning](https://arxiv.org/abs/2611.27518)
*Mohamed Belfkir, Ayoub Hmissou, Larbi Rahili* · `hep-ph` · arXiv:2611.27518v1 · relevance 0.19

- **In one sentence**: A phenomenology study proposing that machine-learning classifiers (BDT and XGBoost) applied to dilepton final states at a future muon collider could help find inert-doublet-model scalar dark matter in compressed mass spectra via the process μ+μ− → AH with A → HZ*, Z* → ℓ+ℓ−.
- **In plain words**: The paper asks whether a possible future particle collider that smashes muons together could spot a hidden kind of dark matter. The idea is that a heavier particle turns into a lighter dark matter particle and a pair of leptons (electrons or muons), and the authors train computer classifiers to pick that signal out from ordinary background events. The text describes the approach and the aim of the study; it does not report the sensitivity numbers in the excerpt provided.
- **Why it matters**: Dark matter is still unidentified, and the model considered here is one of the simplest extensions of the Standard Model that offers a dark matter candidate. Whether a muon collider could test these compressed-mass scenarios, which are hard to probe at other colliders, is a question of interest to the particle physics community, though the excerpt alone does not show how strong the result is.
- **Background needed**: - Standard Model: the current established theory of known particles and forces.
- Dark matter: unseen matter inferred from gravity in galaxies and cosmology; its particle identity is unknown.
- Inert doublet model: a simple extension that adds a second Higgs-like scalar doublet, whose lightest neutral part can be a dark matter candidate.
- Relic abundance: the amount of dark matter left over from the early universe; the model struggles to match it in some regions.
- Compressed spectrum: the heavy and light particles have very similar masses, so the decay products carry little energy and are hard to separate from background.
- Muon collider: a proposed machine colliding muons, which are heavier cousins of electrons, at high energy.
- Dilepton signature: a pair of oppositely charged leptons used as the detectable trace of the event.
- Boosted decision trees and XGBoost: machine-learning methods that combine many simple yes/no rules to sort signal from background. · level: research-level

<details><summary>Original abstract</summary>

The inert doublet model (IDM), a minimal extension of the Standard Model (SM), provides a scalar dark matter (DM) candidate that belongs to the additional Higgs doublet. The model faces challenges in achieving the correct relic abundance for compressed spectra and DM masses in the high-mass range. In this work we investigate the prospects of detecting dark matter candidates at future high-energy muon colliders. Focusing on the process $\mu^+ \mu^- \to AH$ with subsequent decay $A \to H Z^*$ and $Z^* \to \ell^+\ell^-$, we explore the sensitivity of machine learning techniques, specifically Boosted Decision Trees (BDT) and XGBoost, to distinguish the signal from Standard Model backgrounds. We demonstrate that the combination of advanced multivariate analysis with high-luminosity muon collisions enhances the discovery potential for inert scalars in compressed mass spectra scenarios.

</details>

### [From Resonance Properties to High-Energy Behavior: The $R$ Ratio from Lattice QCD](https://arxiv.org/abs/2611.27586)
*Nan Wang, Long-cheng Gui, Jun Hua et al.* · `hep-lat` · arXiv:2611.27586v1 · relevance 0.17

- **In one sentence**: A lattice QCD study that uses Bayesian spectral reconstruction of Euclidean correlators near the physical pion mass to obtain the R-ratio, checking the rho-resonance decay constant f_rho and a Gaussian-smeared R-ratio against experiment across several volumes.
- **In plain words**: This paper asks whether computer simulations of the strong force, run on a discrete grid of space and time, can reproduce measured particle-collision data. The authors reconstruct the "R-ratio", a measure of how often electron-positron collisions produce hadrons at each energy, from simulated correlators. They report that the reconstructed curve follows the smooth high-energy trend seen in experiment and that the rho-meson peak yields a decay constant close to the experimental reference.
- **Why it matters**: Predicting the R-ratio from first principles is a long-standing test of quantum chromodynamics at low energies, so agreement with experiment would matter for that test. The text claims the same framework could extend to other hadronic channels, inclusive decay rates and hadronic tensors, but these extensions are not shown here.
- **Background needed**: - Lattice QCD: simulating the strong nuclear force on a discrete four-dimensional grid of space and time, on finite computer volumes.
- Hadrons: particles made of quarks, such as pions and the rho meson.
- R-ratio: the ratio of hadron production to muon-pair production in electron-positron collisions; a standard test of the strong force theory.
- Euclidean correlators: simulation outputs computed in imaginary time; they must be mathematically converted back to real-energy spectra, which is an ill-posed problem that Bayesian methods address.
- Resonance: a short-lived particle seen as a bump in the energy spectrum; the decay constant f_rho describes how strongly the rho couples to its source.
- Finite-volume effects: distortions caused by simulating in a box of limited size; the paper compares boxes up to about 10 fm across.
- Gaussian smearing: a blurring of the spectrum with a chosen width (here 0.6 GeV) so that lattice and experimental curves can be compared on equal footing. · level: research-level

<details><summary>Original abstract</summary>

We investigate resonance properties and inclusive spectral behavior through Bayesian reconstruction of the $R$-ratio from Euclidean lattice correlators near the physical pion mass. Without additional Gaussian smearing, the reconstructed spectrum already captures the smooth high-energy behavior observed in experiment. Direct integration of the $\rho$ peak determines $f_\rho$ with approximately $1\%$ statistical precision and close agreement with the experimental reference, providing access to resonance properties without resolving individual finite-volume levels. With a common Gaussian width of $\sigma=0.6$~GeV, the lattice and experimental $R$-ratios show good overall agreement over $0.25$--$2.50$~GeV. Comparisons among ensembles with spatial extents up to approximately $10$~fm demonstrate that finite-volume effects can be controlled across these complementary observables. These results demonstrate a unified framework for studying resonance and inclusive physics from lattice QCD, with potential applications to other hadronic channels, inclusive decay rates, and hadronic tensors.

</details>

## Nuclear physics

### [Nuclear Shell Model on the Light Front](https://arxiv.org/abs/2611.26895)
*Zhenkai Fu, Adam Freese, Gerald A. Miller* · `nucl-th` · arXiv:2611.26895v1 · relevance 0.17

- **In one sentence**: The paper analytically solves a light-front harmonic oscillator model of nuclear shell structure and electromagnetic form factors, finds longitudinal-quantum-number-dependent shell splitting traced to the longitudinal confinement interaction via Hellmann-Feynman, and applies it to 48Ca and 208Pb.
- **In plain words**: Atomic nuclei are often described with simple models that ignore relativity, where particles fill energy levels called shells. This paper uses a relativistic version of that picture, built on a "light-front" way of slicing up time and space, and solves it with exact formulas. It finds that the relativistic model reduces to the familiar simple model in the appropriate limit, but also splits the shells in a way that depends on an extra quantum number, and it applies this to calcium-48 and lead-208.
- **Why it matters**: The text reports a clear, tractable calculation that attributes a specific shell splitting to one interaction term, and reports that form factors (how a nucleus scatters electrons or other probes) differ substantially between relativistic and non-relativistic treatments. Its broader significance for nuclear physics is not established by the excerpt alone, so the reader should treat the claims as the authors' own findings.
- **Background needed**: - Atomic nucleus: a dense core of protons and neutrons; its particles occupy discrete energy "shells," similar to electron shells in atoms.
- Shell model: a simplified model where each nucleon moves in an average field and fills energy levels in order.
- Harmonic oscillator: an idealized system with evenly spaced energy levels, often used as a starting approximation for nuclei.
- Non-relativistic approximation: treating particles as moving much slower than light, ignoring relativity.
- Light-front formulation: a relativistic framework that uses a particular choice of time coordinate, which makes certain calculations simpler.
- Form factor: a function describing the internal charge or current spread of a particle or nucleus, probed by scattering.
- Hellmann-Feynman theorem: a standard result relating how an energy changes with a parameter to the expectation value of that parameter's term in the energy operator.
- Longitudinal confinement: the part of the interaction that keeps quarks or nucleons bound along the direction of motion in this model. · level: research-level

<details><summary>Original abstract</summary>

Light-front descriptions of nuclear structure provide a relativistic framework that can potentially deepen our understanding of nuclear structure by revealing effects that are absent from traditional non-relativistic treatments. To utilize this framework, we start from the light-front harmonic oscillator to analytically calculate the shell structure and electromagnetic form factors. The relativistic shell model shows that the light-front result recovers the nonrelativistic oscillator limit while introducing shell splitting that depends on the longitudinal excitation quantum number. We derive the resulting effects on the shell model and use the Hellmann-Feynman theorem to identify the longitudinal confinement interaction as the origin of this splitting. We illustrate these results through applications to $^{48}\mathrm{Ca}$ and $^{208}\mathrm{Pb}$. In addition, we demonstrate a substantial difference between form factors calculated using non-relativistic and light-front treatments, a difference that further underscores the importance of including relativistic effects in the description of nuclear structure. Our findings demonstrate a tractable approach to relativistic nuclear calculations and show how extending nuclear models beyond the non-relativistic approximation can yield meaningful physical insight.

</details>

### [Nuclear Precision and Multimessenger Constraints on Neutron-Star Structure](https://arxiv.org/abs/2611.27669)
*Hisham Anwer, A. Adel, E. Omar* · `nucl-th` · arXiv:2611.27669v1 · relevance 0.10

- **In one sentence**: The paper bounds how much neutron-star core structure remains unconstrained by nuclear-physics data, introduces a radius–Love-number compensation mechanism that weakens nuclear constraints on tides, and estimates how much pulsar-radius and binary-tide measurements would reduce the remaining variance across four equation-of-state families.
- **In plain words**: Neutron stars are extremely dense remnants of collapsed stars, and their interiors are described by an "equation of state," a rule linking pressure and density. This paper asks how much freedom in the core remains even after laboratory nuclear measurements, and how astronomical observations could narrow it. The authors report that a pulsar radius measured to 0.3 km, combined with a binary tidal measurement to 10%, would remove 44 to 68 percent of the current variance in the logarithmic tidal deformability (Love number) across four data-based families of models.
- **Why it matters**: It offers a quantitative way to ask whether laboratory nuclear precision and astrophysical observations together can pin down neutron-star cores, which bears on dense-matter physics. The text gives only the abstract-level figures, so the strength of the conclusion depends on modelling assumptions not shown here.
- **Background needed**: - Neutron star: a city-sized, extremely dense stellar remnant left after a supernova.
- Equation of state (EOS): a formula relating pressure to density inside matter; different EOS predict different star sizes.
- Love number (tidal deformability): how easily a star's shape is distorted by a companion's gravity, measured in binary systems.
- Radius–Love compensation: the idea that changes in star radius and tidal response can offset each other, so nuclear data constrain tides less than expected.
- Variance: a measure of spread or remaining uncertainty among plausible models.
- Multimessenger astronomy: combining different signals, such as gravitational waves, X-rays, and radio pulses. · level: research-level

<details><summary>Original abstract</summary>

Neutron-star cores retain structural freedom beyond the constraints supplied by nuclear measurements. We quantify this freedom through an observable-dependent variance ceiling and identify radius--Love compensation as a mechanism suppressing nuclear constraints on tides. Across four data-conditioned equation-of-state families, a pulsar radius measured to 0.3 km paired with a binary tide measured to 10\% removes 44--68\% of the current logarithmic Love-number variance. The framework connects laboratory precision and complementary stellar measurements to core structure.

</details>

## Quantum information and computing

### [Autonomous quantum machine learning via Riemannian gradient-based optimization](https://arxiv.org/abs/2611.27815)
*Kasidit Srimahajariyapong, Thiparat Chotibut, Suwannachad Suwannajitt et al.* · `quant-ph` · arXiv:2611.27815v1 · relevance 0.25

- **In one sentence**: The paper proposes autonomous quantum machine learning, where Riemannian gradient-based training runs entirely on quantum hardware without measurements or classical feedback, with an exponential convergence guarantee and numerical tests on phase classification and hidden-symmetry unitary learning.
- **In plain words**: Most quantum machine learning today trains a model by repeatedly measuring a quantum circuit and then adjusting parameters on a normal computer, and that back-and-forth is a bottleneck. This paper proposes training the model so that the update steps happen inside the quantum system itself, with no measurements or classical feedback during training. The authors report theoretical convergence guarantees, an analysis of how circuit depth grows, and numerical simulations suggesting the approach can learn with shallow circuits and few training examples.
- **Why it matters**: Removing the measure-and-update loop targets a real scalability limit of near-term quantum learning, and the paper claims the model can find hidden symmetries in data without being told about them. The evidence described here is theoretical plus numerical simulations, so how well this carries over to real hardware is not established by the text.
- **Background needed**: - Quantum circuit: a sequence of operations on quantum bits (qubits) whose parameters can be tuned.
- Quantum measurement: reading out a quantum state yields classical numbers, but it disturbs the state and must be repeated many times to estimate values.
- Classical optimization loop: the usual training method, where a normal computer adjusts circuit parameters step by step based on measured results.
- Gradient descent: repeatedly nudging parameters in the direction that reduces an error measure; a Riemannian version does this while respecting the geometric constraints of quantum operations (such as unitarity).
- Unitary: a reversible quantum operation that preserves total probability.
- Symmetry: a transformation that leaves the problem unchanged; here the model is said to discover such symmetries in data on its own.
- Circuit depth: the number of sequential layers of operations, a rough measure of how long a circuit runs and how susceptible it is to noise.
- Convergence: the training error approaches a minimum; here the paper claims exponential convergence for small step sizes. · level: research-level

<details><summary>Original abstract</summary>

Quantum machine learning models typically rely on repeated quantum measurements and classical optimization during training, making the quantum-to-classical information-extraction process a fundamental bottleneck for scalability. We propose a framework for autonomous self-training quantum machine learning, based on Riemannian gradient optimization, in which the optimization proceeds entirely within the quantum domain without requiring quantum measurements or classical feedback. We derive the Riemannian gradient update rules for a broad class of learning tasks and identify sufficient conditions under which the resulting training dynamics can be realized fully autonomously. Within this regime, we establish an exponential convergence guarantee, in the training iterations, for sufficiently small step sizes, and further analyze the training cost in terms of the growth of the circuit depth. Importantly, we further show that the trained model can automatically discover symmetries hidden in the training data without $\textit{a priori}$ specification. For the canonical examples of quantum phase classification and unitary learning with a hidden symmetry, our numerical study indicates that learning can be achieved at low circuit depths with only a few distinct training examples. Our results thus establish autonomous quantum machine learning as a promising paradigm that removes the classical optimization loop while retaining strong theoretical guarantees and practical performances.

</details>

### [Practical insights into controlling exponential concentration in quantum machine learning](https://arxiv.org/abs/2611.27486)
*Fernando Mondragon-Sampedro, Diego Alvarez-Estevez* · `quant-ph` · arXiv:2611.27486v1 · relevance 0.19

- **In one sentence**: A comparative empirical study of exponential concentration (outputs becoming insensitive to inputs as system size grows) across fidelity quantum kernels, projected quantum kernels, and quantum extreme learning, using an expectation-value variance framework to examine the roles of measurement locality, entanglement, expressivity, and bandwidth scaling.
- **In plain words**: Quantum machine learning models can fail when their outputs stop changing meaningfully as the quantum system gets bigger, so they can no longer tell different inputs apart. This paper compares three kinds of quantum models to see how this happens and what affects it. The authors report that global fidelity-based kernels concentrate strongly, local-measurement approaches reduce but do not remove the effect, and scaling the input bandwidth can help in moderate cases but loses its benefit for highly expressive circuits.</plain>
<parameter name="why">Exponential concentration is a known obstacle to training quantum machine learning models at scale, so practical guidance on which design choices help is useful to people building these models. The text does not indicate how these findings would transfer to hardware or to real-world tasks, so that connection remains open.</why>
<parameter name="background">- Quantum machine learning: using quantum circuits as feature maps or models for learning from data.
- Quantum kernel: a similarity measure between data points computed by a quantum circuit; fidelity kernels compare quantum states directly.
- Exponential concentration: as qubit count grows, measured outputs cluster around one value, shrinking their variance so differences between inputs become hard to detect.
- Observable and variance: an observable is a quantity measured on a quantum state; its variance across inputs signals whether it can distinguish them.
- Entanglement: correlations between qubits that have no classical counterpart; more of it generally adds to the system's complexity.
- Expressivity: how broadly a circuit can represent different functions or states.
- Bandwidth scaling: rescaling the input data before encoding it into the circuit, which controls how sharply the output varies with input.
- Quantum extreme learning: using a fixed quantum system as a reservoir whose measured outputs feed a simple trained readout.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Quantum Machine Learning (QML) models are often limited by exponential concentration, where quantum observables become insensitive to input variations as system size increases. In this work, we provide a comparative empirical study of this phenomenon across Fidelity Quantum Kernels (FQK), Projected Quantum Kernels (PQK), and Quantum Extreme Learning (QEL), within a unified observable-based framework based on expectation-value variance. We investigate how measurement locality, entanglement, and circuit expressivity shape concentration across different architectures. Global fidelity-based kernels exhibit strong concentration driven by Hilbert space dimensionality, whereas local-observable approaches reduce but do not eliminate this effect. In PQK and QEL, concentration is primarily governed by entanglement and quantum dynamical expressivity, with reservoir depth emerging as a key factor in QEL architectures. We further study bandwidth scaling as a general mechanism for controlling encoding expressivity across all models. Our results indicate that bandwidth scaling effectively reduces concentration in moderate regimes by restricting the effective expressivity of the encoding, though this protective effect diminishes in highly expressive structural settings.

</details>

## Optics and atomic physics

### [Coherence Lengths of Laser Pointers](https://arxiv.org/abs/2611.26878)
*Vaishnavi Rao Namakkal Ranga Rao, Marissa R. Godoy, Mark D. Sotnikov et al.* · `physics.optics` · arXiv:2611.26878v1 · relevance 0.15

- **In one sentence**: The paper measures the temporal coherence lengths of several low-cost green laser pointers (three diode lasers and one frequency-doubled DPSS laser) using a noncollinear-beam interferometer read out by a CMOS detector array, noting that the devices operate in a multimodal regime.
- **In plain words**: Laser pointers are cheap, but how "pure" their light is varies, and that affects how far apart two parts of the beam can travel and still interfere. The authors tested several inexpensive green laser pointers with a homemade interferometer, a device that splits and recombines light to detect such interference. They found the coherence length, a rough measure of this interference distance, varies from device to device but can often exceed 10 cm.
- **Why it matters**: The work is modest in scope: it measures everyday devices and is framed as a teaching template for advanced undergraduate labs. It may also suggest that consumer laser pointers could be used in interference-based applications, though the text does not develop this.
- **Background needed**: - Coherence: how consistently a light wave keeps its phase; highly coherent light produces clear interference fringes.
- Coherence length: the maximum path difference over which a beam still interferes with itself; longer means more coherent.
- Interferometer: an instrument that splits light into two paths, recombines them, and reads the pattern of bright and dark fringes.
- Multimodal laser: a laser emitting light at several closely spaced wavelengths at once, which shortens coherence length.
- Diode laser and DPSS (diode-pumped solid-state) laser: common laser types; a frequency-doubled DPSS laser halves the wavelength to produce green light.
- CMOS detector array: the same kind of light-sensing chip used in digital cameras. · level: intermediate

<details><summary>Original abstract</summary>

We report on the coherence lengths of low-cost green laser pointers in the midst of multimodal behavior using an optical interferometer based on noncollinear beam geometries and a CMOS detector array. Examined devices include three diode lasers and a frequency-doubled neodymium-emission diode-pumped solid state (DPSS) laser. Coherence length measurements are variable among devices, but values can nevertheless regularly exceed 10 cm. The work serves as a template for an advanced undergraduate physics laboratory experiment and may inspire new kinds of laser pointer devices utilizing interference effects as operative principles.

</details>

### [Test of gravitational redshift by optical clocks at different latitudes](https://arxiv.org/abs/2611.27588)
*Ingo Nosske, Chetan Vishwakarma, Tim L\"ucke et al.* · `physics.atom-ph` · arXiv:2611.27588v1 · relevance 0.13

- **In one sentence**: Two Earth-fixed optical atomic clocks at different latitudes are compared against the gravitational redshift predicted by general relativity, using independent geodetic height data, reaching a 4.6×10⁻⁵ uncertainty and arguing that a latitude separation boosts sensitivity to possible violations.
- **In plain words**: The paper checks a prediction of Einstein's general relativity: clocks sitting in a stronger gravitational field tick more slowly. The authors compared two optical atomic clocks on Earth placed at different latitudes, and found that the frequency difference between them matches the predicted gravitational effect. The text says the test is accurate to about 4.6 parts in 100,000, roughly twice as good as earlier ground-based tests.
- **Why it matters**: The text claims that clocks separated in latitude, not just in height, are about three times more sensitive to a hypothetical violation of the gravitational redshift, and that this could let ground-based tests approach space-based precision. Whether this holds in practice depends on details of the geodetic measurements that the summary does not provide.
- **Background needed**: - Gravitational redshift: clocks deeper in a gravity well run slower, so their light frequency is lower when compared with a clock higher up.
- Kinematic time dilation: clocks moving relative to each other also run at different rates; this effect has already been tested very precisely.
- Geopotential: the combined gravity-plus-rotation energy surface that defines "height" in geodesy; a clock's position relative to it sets its predicted rate.
- Centrifugal potential: the effect of Earth's rotation, which changes the apparent "height" of a location depending on latitude.
- Optical atomic clocks: very precise clocks that count oscillations of laser light emitted by atoms; they are the instruments used for such comparisons.
- Uncertainty level: the fraction of the predicted effect that the measurement could resolve, so smaller means a stricter test. · level: research-level

<details><summary>Original abstract</summary>

General relativity predicts that frequency comparisons between clocks are affected by both gravitational and kinematic time dilation. While the kinematic contribution has been tested with high accuracy, experimental tests of the gravitational redshift remain comparatively less stringent. Here, we measure the frequency shift between two Earth-fixed optical atomic clocks at different potentials and compare it to the redshift predicted by general relativity using independent geodetic measurements. The observed shift agrees with the prediction, testing the gravitational redshift at the $4.6 \times 10^{-5}$ uncertainty level, improving ground-based tests by a factor two. Previous ground-based tests separated the clocks mainly vertically. For clocks at different latitudes, their height difference is governed not only by the gravitational potentials at their locations but also by the centrifugal potentials caused by Earth's rotation. As both contributions can partially cancel, the gravitational contribution can be considerably larger than their height difference suggests. In this work, a separation of the clocks by $4^\circ$ in latitude enhances their sensitivity to a gravitational redshift violation threefold, to the equivalent of an approximately 1200 m difference in height for small latitudinal separation. Our results establish Earth's rotation as a so far unexploited resource for advancing ground-based tests of the gravitational redshift towards the sensitivity of previous space-based experiments.

</details>

## Fluids and plasma

### [Hot-Layer Ignition in High-Gain Inertial Confinement Fusion](https://arxiv.org/abs/2611.27760)
*M. Lourmande, B. Canaud* · `physics.plasm-ph` · arXiv:2611.27760v1 · relevance 0.13

- **In one sentence**: A proposed analytical criterion and three-zone model for "hot-layer ignition," in which alpha-particle energy deposited in the shocked deuterium-tritium shell of very high-gain inertial confinement fusion targets independently ignites the shell and recompresses the hot spot, checked with 1D simulations.
- **In plain words**: This paper looks at how fusion fuel can burn inside a tiny pellet squeezed by lasers or similar drivers. The authors describe a way the outer shell of the fuel, which has been shocked and heated, can ignite on its own, separately from the hot centre, and then squeeze that centre again. Using a simplified model and computer simulations, they report that this effect boosts the total energy released by about 50 percent.
- **Why it matters**: Energy gain is the central measure of whether fusion power from compressed pellets is practical, so a mechanism that adds roughly 50 percent to the output would matter if it holds up. The text rests on a simple model and 1D simulations only, so its size in real, more complex targets is not established here.
- **Background needed**: - Inertial confinement fusion (ICF): a small fuel capsule is compressed and heated very quickly, usually by lasers, so that fusion reactions occur.
- Deuterium and tritium: heavy forms of hydrogen, the usual fusion fuel.
- Hot spot: the hot, low-density centre of the compressed fuel that starts the burn.
- Shocked shell: the denser outer layer of fuel heated by a shock wave during compression.
- Alpha particles: helium nuclei released by fusion; they deposit their energy locally and help heat the fuel.
- Ignition: the point where fusion heating runs away and sustains burning.
- Gain: the ratio of fusion energy released to the energy put in.
- 1D simulation: a computer model that tracks changes along one spatial direction only, which simplifies the real three-dimensional physics. · level: research-level

<details><summary>Original abstract</summary>

Ignition of the shocked deuterium tritium shell is identified during the thermonuclear combustion of very high-gain targets in inertial confinement fusion (ICF). This mechanism is due to the local energy deposition of the fusion alphas created in this shocked shell, independently of hot-spot ignition, and generates sufficient energy to fully recompress the hot spot. A new analytical criterion for the ignition of the hot layer is presented. A simple three zone model, based on the thick layer hot-spot model, reproduces this mechanism, which breaks down into successive stages: ignition of the hot spot, compression of the shocked shell, ignition of the shocked shell, and subsequent recompression of the hot spot. 1D numerical simulations highlight the onset of this hot layer ignition thereby satisfying the analytical ignition criterion. It is shown that this mechanism amplifies the energy released by the combustion of the target by approximately 50 %.

</details>

### [A 3D PINN-Based Framework for Patient-Specific Pulmonary Hemodynamics Using Windkessel Models](https://arxiv.org/abs/2611.27351)
*Celia Taboada, Luis Nu\~nez, Ang\'elica Casero et al.* · `math.NA` · arXiv:2611.27351v1 · relevance 0.12

- **In one sentence**: A physics-informed neural network (PINN) framework that solves pulsatile blood flow in patient-specific pulmonary artery geometry with a three-parameter Windkessel outlet model, validated on 2D channels and used for inverse parameter identification on synthetic data.
- **In plain words**: This paper looks at a way to simulate blood flow in the lung's arteries without building the usual detailed mesh of the vessel shape that standard computer fluid simulations need. The authors train a neural network so that it follows the physics of fluid flow directly, and they add a simple model of the downstream vessels as the outlet condition. They report that it reproduces flow, pressure and velocity in tests on simple channels and a patient-based artery, and that it can recover the outlet model's settings from synthetic data.
- **Why it matters**: Mesh-based simulations are expensive and slow to set up, which limits their use in clinics, so a meshless alternative that can be fitted to patient data is of interest for digital twin work. The text itself notes that residual biases in local pressure and robustness to noisy clinical data are still open, so the approach is not yet shown to be ready for clinical use.
- **Background needed**: - Computational fluid dynamics (CFD): simulating fluid flow by dividing space into a mesh and solving equations on it.
- Physics-informed neural network (PINN): a neural network trained so that its outputs also satisfy the governing equations of physics, without a fixed mesh.
- Windkessel model: a simple electrical-style analogy (resistors and capacitor) for how downstream vessels resist and store blood flow, used as an outlet boundary condition.
- Lumped-parameter model: representing a complex system by a few aggregate parameters rather than full detail.
- Inverse problem: inferring model settings (here the three Windkessel parameters) from observed data.
- Digital twin: a computer model tuned to an individual patient's data. · level: research-level

<details><summary>Original abstract</summary>

Cardiovascular fluid dynamics modeling relies heavily on mesh-based numerical methods such as Computational Fluid Dynamics (CFD). While accurate, these methods entail significant computational costs and complex meshing workflows that limit their translation to clinical practice. Physics-Informed Neural Networks (PINNs) are a promising meshless alternative that embeds the governing equations directly into neural network training. In this work, we propose a PINN framework for pulsatile blood flow in patient-specific geometries with dynamic lumped-parameter Windkessel (RCR) outlet conditions representing distal vascular impedance. Coupling the Windkessel ODE to a 3D network raises two difficulties: the ODE alone does not fix the pressure level, and the local pressure variations that drive the flow are orders of magnitude smaller than the basal pressure imposed by the outlet. We address them by decomposing pressure into a time-dependent basal part and a spatially varying part, an initial condition and gauge for the Windkessel equation, a global mass-balance constraint, and a periodic Fourier embedding of time. Validated on 2D canonical channels (steady and pulsatile, with and without RCR outlet), the framework is then applied to a patient-specific right pulmonary artery, reproducing outlet flow, mean pressure, and the velocity and dynamic pressure fields with errors on the order of the data resolution. Finally, we solve the inverse problem of identifying the three Windkessel parameters of the outlet from synthetic data, recovering them with errors of about 0.3% from deliberately wrong initial values. Residual biases in the local pressure field and the need to test robustness to noisy clinical data remain open, but the results support PINNs as complementary tools for meshless hemodynamics and patient-specific digital twins.

</details>

## Biological physics

### [Receptor Abundance Alone Underpredicts Red Blood Cell Adhesion in Gaucher Disease](https://arxiv.org/abs/2611.27960)
*Zhaojie Chai, Pierre A. Buffet, Melanie Franco et al.* · `physics.bio-ph` · arXiv:2611.27960v1 · relevance 0.05

- **In one sentence**: A stochastic bond-level simulation of red blood cell adhesion via Lu/BCAM-laminin bonds, calibrated on control donors, finds that receptor abundance alone underpredicts adhesion in Gaucher disease and that receptor activation state better explains the shortfall.
- **In plain words**: Red blood cells in Gaucher disease, an inherited condition affecting fat metabolism, stick to blood vessel walls more than normal, and they carry more of a sticky surface receptor called Lu/BCAM. The authors built a computer model of cells that form random molecular bonds with a protein called laminin, tuned it on healthy donors, and asked whether the higher receptor count alone could explain the extra sticking. It could not: the measured adhesion was about 1.6 to 1.7 times higher than predicted, and matching the data needed far more receptors able to bind, which lines up with a larger rise in the phosphorylated (chemically switched-on) form of the receptor.
- **Why it matters**: The result suggests that counting how many receptors a cell has may miss what matters for sticking, and that the active state of those receptors may be more important. The same modelling approach is also applied to sickle cell disease, where the model is said to track the drop in adhesion under hydroxyurea, a treatment, and the abstract notes that stiffening the membrane could keep cells trapped at the spleen's narrow slits; how far these links hold is not established from the abstract alone.
- **Background needed**: - Red blood cells can stick to vessel walls through surface receptors binding to matching proteins on the wall.
- Lu/BCAM is a receptor on red cells that binds laminin, a protein in the tissue lining blood vessels.
- Gaucher disease is an inherited disorder that causes abnormal adhesion and other problems in blood cells.
- Phosphorylation is a chemical tag that switches a protein's activity on or off; a phosphorylated receptor is more likely to bind.
- Stochastic simulation models events, such as bond formation, as random processes rather than fixed outcomes.
- Shear stress is the drag force from blood flowing past a surface.
- Hydroxyurea is a drug used in sickle cell disease; the spleen's narrow slits filter out stiff or misshapen cells. · level: research-level

<details><summary>Original abstract</summary>

Red blood cells (RBCs) in Gaucher disease (GD) adhere abnormally to vessel walls and carry more Lutheran/basal cell adhesion molecule (Lu/BCAM), a laminin receptor. Whether receptor abundance sets this adhesion is untested. We simulated RBCs carrying stochastic Lu/BCAM-laminin bonds, calibrated a population on control donors, and predicted GD adhesion from the 1.3-fold receptor rise. On laminin and endothelium the data exceed the prediction 1.6- to 1.7-fold. Matching them requires 2.4- and 4.6-fold more binding-competent receptors, compatible with the estimated 5.7-fold rise in phosphorylated receptors. Neither a stiffer membrane nor higher bond affinity removes the shortfall at high shear stress. In sickle cell disease, given active-receptor counts, the model predicts the fall in adhesion under hydroxyurea within 1.4-fold, while total receptors rise. Adhesion likely follows receptor state more than abundance. Stiffening instead retains cells at a splenic slit.

</details>

## Climate, atmosphere and Earth

### [Carbon dioxide responses shape estimates of Amazon forest vulnerability under solar geoengineering](https://arxiv.org/abs/2611.26908)
*Anupama K Xavier, Chris Jones* · `physics.ao-ph` · arXiv:2611.26908v1 · relevance 0.07

- **In one sentence**: Uses a CO2-dependent forest-sustainability threshold in a shared climate phase space to test whether stratospheric aerosol injection (SAI) reduces Amazon forest vulnerability under high-emission and mitigation scenarios.
- **In plain words**: The Amazon rainforest may be pushed toward loss by heat and changing rainfall. This study asks whether spraying reflective particles into the upper atmosphere, a proposed way to cool the planet, would lower that risk. The authors find that it cools the region substantially but leaves much of the drying and longer dry seasons in place.
- **Why it matters**: Solar geoengineering is often discussed as a way to limit climate damage, so whether it protects a major forest matters for policy. The result also shows that the answer depends heavily on how much extra CO2 is assumed to help plants resist stress, which is itself uncertain.
- **Background needed**: - Stratospheric aerosol injection (SAI): releasing tiny reflective particles high in the atmosphere to reflect sunlight and cool Earth; it does not cut greenhouse gases.
- Forest vulnerability: the risk that a forest shifts toward dieback, based on climate conditions such as temperature, rainfall and dry-season length.
- Climate phase space: a way of plotting climate variables against each other (e.g., warming versus drying) so that different scenarios can be compared on the same chart.
- Threshold: a boundary in those conditions beyond which forest loss is expected; here it is made to depend on CO2 level, since higher CO2 can help plants use water more efficiently.
- Scenarios: mitigation (low emissions), high-emission, and SAI cases used as model experiments.
- Grid cells: small map squares used in climate models; the paper reports the share of cells crossing the threshold. · level: research-level

<details><summary>Original abstract</summary>

The Amazon rainforest is vulnerable to warming and changes in rainfall, yet whether solar geoengineering can reduce conditions associated with forest loss remains uncertain. Stratospheric aerosol injection (SAI) can offset greenhouse-gas-driven warming without fully restoring regional hydroclimate. Here we assess Amazon forest vulnerability under mitigation, high-emission and SAI scenarios using a Carbon dioxide-dependent forest-sustainability threshold in a common climate phase space. By late century, SAI reduces projected Amazon warming from 5.49 degree Celsius under high emissions to 2.45 degree Celsius, but substantial drying and longer dry seasons persist. Under SAI, 44.7 percentage of analysed grid cells exceed the present-day threshold, compared with 8.7 percentage when the future Carbon dioxide-dependent threshold is considered. This contrast reveals that apparent forest protection depends strongly on the assumed resilience benefits of elevated Carbon dioxide. Our findings highlight the importance of hydroclimatic changes and Carbon dioxide-dependent vegetation responses in assessing the potential of solar geoengineering to reduce Amazon forest vulnerability.

</details>

### [Spatiotemporal Landslide Runout Reconstruction from Sparse Observations with LAPIS-SHRED](https://arxiv.org/abs/2611.27132)
*Xingyue Zhang, Yuxuan Bao, Jeffrey Keck et al.* · `cs.CE` · arXiv:2611.27132v1 · relevance 0.06

- **In one sentence**: The paper applies LAPIS-SHRED, a latent-space temporal inference framework trained on physics-based simulation ensembles, to reconstruct spatiotemporal landslide runout trajectories near Mount St. Helens from sparse sensor data.
- **In plain words**: Landslides move fast and are rarely watched in real time, so scientists usually only see the mud or debris left behind afterward. This paper describes a method that uses a small number of sensor readings, taken at one moment, to rebuild how a landslide moved over time, and then checks the result against the deposits the slide actually left.
- **Why it matters**: Better reconstruction of how landslides travel could help with hazard assessment where monitoring is sparse. The text reports that the method's spatial match to observed deposits (r = 0.843) is close to that of the calibrated simulator it was trained on (r = 0.853), so it is a reconstruction tool rather than a replacement for the simulator; its value beyond this one site is not shown in the text.
- **Background needed**: - Landslide runout: how far and how fast a slide travels after it fails.
- Physics-based simulation ensemble: many computer runs of a landslide model with varied inputs, used as training data.
- Sensor observations / single timepoint: the method uses 32 measurements taken at one moment.
- Backward vs. forward reconstruction: inferring past motion from a single snapshot versus predicting future motion from a short early record.
- NRMSE (normalized root-mean-square error): a standardized measure of error; lower is better. Here below 5.8%.
- Spatial correlation (r): how closely two maps agree, from 0 (none) to 1 (perfect).
- Latent space: a compressed internal representation a model learns from data.
- SHRED-type models: neural networks that map a few sensor readings to a full spatial field over time. · level: research-level

<details><summary>Original abstract</summary>

Reconstructing the spatiotemporal evolution of landslide runout from limited observations is a central challenge in geohazard assessment: transient flow dynamics are rarely observed directly, and available data are often confined to post-event deposits or brief monitoring windows. We apply LAPIS-SHRED (LAtent Phase Inference from Short time sequence using SHallow REcurrent Decoders) to reconstruct runout events near Mount St. Helens, USA. Trained on physics-based simulation ensembles, the framework supports both backward reconstruction from single frame and forward prediction from short initial window across different runout regimes. Using 32 sensor observations from a single timepoint, LAPIS-SHRED recovers complete runout trajectories with NRMSE below 5.8%, robust across varying observational and training conditions. Validation against observed deposits yields spatial correlation of r = 0.843 against the calibrated simulator's r = 0.853. These results suggest that latent-space temporal inference offers a viable pathway for spatiotemporal landslide reconstruction under extreme observational constraints typical of field settings.

</details>

## Cosmology

### [Beyond the Peak: Constraining early dark energy with the damping tail](https://arxiv.org/abs/2611.27069)
*Hao Wang, Gen Ye, Yun-Song Piao* · `astro-ph.CO` · arXiv:2611.27069v1 · relevance 0.16

- **In one sentence**: The paper argues that the post-peak "tail" of an early dark energy scalar field, not just its peak amplitude and location, carries observable information about a multiscale potential (axion-like plus α-attractor-like regimes), and tests this against CMB, BAO and supernova data.
- **In plain words**: Cosmologists have proposed a short burst of extra "dark energy" in the early universe as a way to ease a disagreement about how fast the universe is expanding today (the Hubble tension). This paper looks at what happens after that burst fades, which the authors call the "EDE tail," and argues it can be used as an extra test of the underlying field. Using a model with two different regimes of a field's potential, they report a better fit to high-resolution cosmic microwave background data and a somewhat higher inferred expansion rate.
- **Why it matters**: The Hubble tension is one of the main open puzzles in cosmology, and early dark energy is one of the leading proposed fixes, so a new observable that distinguishes between versions of the idea is of interest. The text does not show how strongly the tension is reduced, and the framework is described as phenomenological and representative, so its wider significance remains to be judged.
- **Background needed**: - The Hubble tension: measurements of the universe's current expansion rate from the early universe (CMB) and from nearby stars and galaxies disagree.
- Early dark energy (EDE): a hypothetical scalar field that briefly contributes energy shortly before the universe recombined, changing the sound-wave scale that CMB data measure.
- Scalar field potential: the energy landscape a field rolls over; its shape determines how the field evolves.
- Axion-like and α-attractor potentials: two families of field shapes studied in theory; the paper combines them.
- Damping tail: the high-multipole end of the CMB power spectrum, where small-scale fluctuations are smoothed out.
- Reflection and asymmetric oscillations: the field bouncing off a boundary of its landscape and oscillating unevenly, which reshapes the tail.
- CMB, BAO and supernova data: standard cosmological datasets used to test models. · level: research-level

<details><summary>Original abstract</summary>

Early dark energy is commonly characterized by the amplitude and location of its primary energy-injection peak. We show that its post-peak evolution, which we call the \emph{EDE tail}, provides an additional observable probe of the underlying scalar dynamics and can materially affect its ability to alleviate the Hubble tension. We construct a simple phenomenological framework in which distinct regions of a multiscale scalar potential govern the dynamics at different field scales. As a representative realization, we consider a potential that combines axion-like and $\alpha$-attractor-like regimes, thereby allowing the EDE tail to be reshaped through reflection and asymmetric oscillations. Confronting this framework with cosmic microwave background, baryon acoustic oscillation, and supernova observations, we find an improved fit to the high-$\ell$ CMB data together with a higher inferred bestfit $H_0$. Our results show that the EDE tail retains observable information about the underlying scalar potential that is not captured by the conventional peak parameters alone. This provides a complementary route for constructing and observationally distinguishing EDE scenarios, and potentially for further alleviating the Hubble tension.

</details>

### [Dark Energy Based on Modified Gravity: Where the Future Lies?](https://arxiv.org/abs/2611.27228)
*Shin'ichi Nojiri, Sergei D. Odintsov, V. K. Oikonomou et al.* · `gr-qc` · arXiv:2611.27228v1 · relevance 0.16

- **In one sentence**: The paper argues that some realistic F(R) gravity dark-energy models, which fit recent DESI data, can drift into anti-gravity or ghost-graviton regimes in the future, and proposes a scalar-field potential barrier at small curvature to prevent this without fine-tuning initial conditions.
- **In plain words**: The paper looks at dark energy, the unknown cause of the universe's accelerating expansion, and asks where it may be heading. Some models that match recent measurements from the DESI survey could, in the far future, push the universe into strange states such as "anti-gravity." The authors propose adding a barrier in the model that blocks this outcome, and suggest ways to test the idea using how galaxies move and a effect on light from hot gas (the kSZ effect).
- **Why it matters**: Recent DESI data hint that dark energy may have been "phantom" in the recent past and then changed behavior, so the future predictions of models that fit this data matter for testing gravity. The text does not show how strongly the barrier idea would hold up beyond the models considered, so its wider significance is uncertain.
- **Background needed**: Dark energy: the unknown component driving the universe's accelerated expansion. Equation of state: a number describing how dark energy's pressure relates to its energy density; "phantom" means it is more negative than the cosmological-constant value, and "quintessence" means it is less negative. DESI: a large galaxy-survey project whose recent data constrain dark energy. F(R) gravity: a modification of Einstein's general relativity in which the gravitational Lagrangian is a function of the Ricci curvature R, which can mimic dark energy. Scalar field: a field whose value can vary in space and time, used here as the driver of the modified gravity. Potential barrier: a hill-shaped energy profile for that field that stops it from rolling into a bad region. Ghost graviton: a gravitational mode with negative kinetic energy, signaling an unphysical instability. Peculiar velocity: a galaxy's motion relative to the smooth cosmic expansion. kSZ (kinetic Sunyaev-Zel'dovich) effect: a shift in cosmic microwave background light as it passes through moving hot gas. · level: research-level

<details><summary>Original abstract</summary>

Based on current observational data, there is a strong possibility that dark energy was in a phantom regime in the near past, and a transition from a phantom to a quintessential regime may have occurred. Since then, many scenarios compatible with the DESI data have been proposed. In particular, there exist several realistic models in the framework of $F(R)$ gravity. In this paper, we show that such realistic models of $F(R)$ gravity may produce an anti-gravity or ghost graviton in the future. The problem could be avoided by further changing the parameters and fine-tuning the initial conditions, but we propose to introduce a potential barrier of the scalar field for the small scalar curvature region, which prevents the Universe from evolving into the anti-gravity or having a ghost graviton region, without the fine-tuning of the initial conditions. We also discuss how this regime can be tested using peculiar velocity and kSZ effect probes.

</details>

## Galaxies

### [The role of gas on the collisional runaway path to supermassive black hole seeds](https://arxiv.org/abs/2611.26885)
*Boris Cuevas, Basti\'an Reinoso, Andr\'es Escala et al.* · `astro-ph.GA` · arXiv:2611.26885v1 · relevance 0.18

- **In one sentence**: Coupled N-body and SPH simulations (AMUSE, BRIDGE) of dense, gas-embedded star clusters test how gas fraction (0–20%) speeds up runaway stellar collisions and boosts the mass of the resulting black hole seed.
- **In plain words**: Astronomers still do not know how the enormous black holes seen in the early universe, already billions of times the Sun's mass, formed so quickly. This paper uses computer simulations of tightly packed star clusters that contain some leftover gas, and checks how that gas changes the chance that stars merge into one very massive object that could seed a black hole. The authors report that, in most of their 48 runs, more gas led to a more massive black hole and an earlier collapse of the cluster's core.
- **Why it matters**: It offers one proposed route for building black hole seeds that could grow into the supermassive black holes observed at high redshift. The text does not establish that this route is what actually happened in nature, and the authors themselves say their simulations do not fully resolve the key gas-friction effect.
- **Background needed**: - Supermassive black holes: millions to billions of solar masses, found in galaxy centres; their origin in the early universe is unresolved.
- Seed black hole: an initial black hole that later grows by swallowing gas and merging.
- Runaway collision: in a dense star cluster, stars collide and merge, and the merged object grows fast and can collapse into a black hole.
- Core collapse: the cluster's dense central region shrinks under its own gravity over time.
- N-body simulation: tracks gravitational pulls between many individual stars; SPH (smoothed particle hydrodynamics) models gas as particles.
- AMUSE and BRIDGE: software framework and coupling method that let the star and gas parts interact gravitationally.
- Plummer distribution: a standard mathematical model for a spherical star cluster.
- Dynamical friction: energy loss of moving bodies through a surrounding medium, which makes heavier objects sink toward the centre; the text says it is most efficient in the transonic regime (speeds near the local sound speed) but is not fully resolved here. · level: research-level

<details><summary>Original abstract</summary>

The origin of supermassive black holes (SMBHs) remains unclear, despite observational evidence for their rapid formation in the early Universe, as evidenced by active galactic nuclei (AGN) at high redshift. In this paper, we investigate stellar dynamics in dense, gas-embedded clusters. We explore how gas influences the runaway collision process and the subsequent formation of SMBH seeds in a global instability scenario. We perform a series of coupled N-body and SPH simulations using the AMUSE framework, with the stellar and gaseous components interacting gravitationally via the BRIDGE method. We use 12 initial condition models with equal-mass stars following Plummer distributions, with total masses ranging from $10^3$ to $5 \times 10^5~M_{\odot}$, virial radii from $0.005$ to $0.1$ pc, and stellar masses of $1$, $10$ and $50$ $M_{\odot}$. For each model, we perform four simulations with gas fractions ranging from 0\% to 20\%, resulting in a total of 48 simulations. The gas is sampled with the same spatial distribution as the stars, with a mass ratio per particle of $m_{\rm SPH}/m = 0.01$, where $m$ is the stellar mass. We find that in most of our simulations, higher gas fractions lead to the formation of more massive black hole, as the core collapses earlier, triggering collisions through gas--star interactions. Our results show increases in BH mass of $\sim 8\%$ for low gas fractions, to $\sim 44\%$ at 20\% gas fraction. The core collapse time is also shortened, with the strongest reduction at $20\%$ gas fraction ($\sim 27\%$). The transonic regime of our initial conditions is where dynamical friction is most efficient in principle. Although our simulations do not fully resolve this effect, gas--star interactions are the principal mechanism driving the enhancement in BH formation efficiency, in the absence of other dissipation mechanisms.

</details>

### [An early interaction between the Sagittarius dwarf and the Milky Way I: Fossil signatures in the phase-space structure of the disc](https://arxiv.org/abs/2611.27898)
*Payel Das, Jason A. S. Hunt* · `astro-ph.GA` · arXiv:2611.27898v1 · relevance 0.14

- **In one sentence**: Four N-body plus hydrodynamic simulations (one isolated Milky-Way-like host, three with a Sagittarius-like satellite on a polar, unbound orbit) test whether a single early disc crossing leaves age-resolved vertical heating fingerprints in the thin disc.
- **In plain words**: About 5 to 7 billion years ago, the Sagittarius dwarf galaxy may have passed through the Milky Way's disc once. This paper uses computer simulations to ask whether that single passage left a lasting mark on the stars that were already present, by making them puffier and jostling them vertically. The authors find that stars alive at the time of the passage are thicker and move up and down faster than in a control run, while younger stars are unaffected.
- **Why it matters**: If a single encounter leaves datable traces in the disc, stellar ages and vertical motions could be used to date past collisions with satellite galaxies. The paper compares its best-matching run with an observed dispersion jump in the outer low-alpha disc of the Milky Way (Das et al. 2024), but the authors say the mapping from jump size to perturber mass is only good to about a factor of 1.5, so the link is suggestive rather than settled.
- **Background needed**: - Galactic disc: the flattened, rotating plane of stars in the Milky Way; the thin disc is its youngest, thinnest part.
- Sagittarius dwarf: a small satellite galaxy being absorbed by the Milky Way, and the proposed perturber here.
- N-body plus hydro simulation: a computer model that tracks gravitating particles (stars, dark matter, gas) and gas dynamics over time.
- Pericentre: the closest point of a satellite's orbit to the host's centre.
- Unbound polar orbit: the satellite passes through once on a path perpendicular to the disc plane and is not captured.
- Velocity dispersion: a measure of how widely stellar velocities spread; a higher value means stars are moving more randomly, i.e. the disc is "heated".
- Age-velocity dispersion relation: how the velocity spread of stars changes with their age; older stars are usually more dispersed.
- Alpha abundance: the ratio of certain chemical elements in stars, used to separate older, thicker-disc populations from younger ones. · level: research-level

<details><summary>Original abstract</summary>

Several independent lines of evidence point to an early encounter between the Milky Way and the Sagittarius dwarf galaxy $5$-$7$ Gyr ago. We present four controlled $N$-body+hydro simulations, one of an isolated host galaxy and three of a single interaction between a Milky-Way-like host and a Sagittarius-like satellite on an unbound polar orbit. Relative to the fiducial satellite (with total mass $0.7\times10^{11}$ M$_\odot$), one run increases the satellite's mass by a factor of $1.5$ and another its crossing speed by a factor of $1.4$, giving pericentric speeds of $466$-$634$ km s$^{-1}$ at pericentric radii of $R\simeq15$-$18$ kpc. Comparing the present-day, phase-space structure in radial bins by age of newly-formed thin-disc stars across the runs, we find that stars that existed at the time of the passage are thickened by up to $\sim37$ per cent in mass-enclosed height and heated by up to $\sim5$ km s$^{-1}$ in vertical velocity dispersion relative to the control, while stars formed after the passage are unaffected. The heating signature is also evident when comparing the age-vertical velocity dispersion relation against a heating relation with a power law of $0.38$, obtained by fitting the isolated host. A single, disc crossing from an early interaction thus suffices to leave lasting, datable fossils in the age-resolved vertical structure of a galactic disc. The fiducial run's dispersion jump of $\sim4$ km s$^{-1}$ matches best with that observed in the outer low-$\alpha$ disc of the Milky Way (Das et al. 2024), corresponding to a perturber mass of $0.7\times10^{11}$ M$_\odot$, with a velocity of $466$ km s$^{-1}$ at a pericentric radius of $16.7$ kpc, though the inversion from jump amplitude to perturber mass is good only to a factor of $\sim1.5$.

</details>

## Exoplanets and planetary science

### [Hints of planet formation in progress around DR Tau from observations with LBT SHARK-NIR and SHARK-VIS](https://arxiv.org/abs/2611.27643)
*D. Mesa, G. Li Causi, R. Gratton et al.* · `astro-ph.EP` · arXiv:2611.27643v1 · relevance 0.14

- **In one sentence**: High-contrast narrow-band imaging of the DR Tau protoplanetary disk with LBT SHARK-VIS and SHARK-NIR searches for accreting embedded companions via H-alpha and Paschen-beta emission, finding two stable compact features whose emission is likely reflected starlight rather than accretion.
- **In plain words**: Young planets are thought to form inside the thick, dusty disks of gas around newborn stars, but they are very hard to photograph there. This study pointed a large telescope's cameras at the disk around a young star called DR Tau, looking for the specific light a growing planet might give off as it pulls in gas. It found two compact spots that stay put over seven years and move in a way consistent with orbiting the star, but the light they give off appears to be starlight bounced off dust rather than the planet's own glow.
- **Background needed**: - Protoplanetary disk: a rotating disk of gas and dust around a young star, where planets form.
- Sub-stellar object: a body too small to be a star, such as a planet or brown dwarf.
- Accretion: a growing object pulling in surrounding gas; hot infalling gas glows at specific wavelengths.
- H-alpha and Paschen-beta: specific colors of light (visible red and near-infrared) emitted by hot hydrogen gas; they are used as markers of accretion.
- Narrow-band vs broad-band filters: narrow filters pass only a tiny slice of color, broad filters pass a wide range.
- High-contrast imaging: techniques for seeing a faint object next to a much brighter star, often by blocking the star's glare.
- Keplerian rotation: orbital motion that follows the expected speed for an object orbiting a central mass.
- MJup: Jupiter masses, a unit for the mass of planets.
- Signal-to-noise (S/N): a measure of how clearly a signal stands out from random background fluctuations; here values of 6 to 13 are modest. · level: research-level

<details><summary>Original abstract</summary>

Protoplanetary disks are the primary sites of planet formation. However, the direct imaging of protoplanets still embedded within their parental disks remains a significant challenge, with only a small number of confirmed detections to date and several candidates awaiting verification. We search for embedded planets in the protoplanetary disk of the young star DRTau by targeting accretion signatures from forming sub-stellar objects. Using narrow-band imaging, we observe both visible Halpha and near-infrared Paschen-beta (Pabeta) emission to identify actively accreting companions. To this end, we performed high-contrast observations of DRTau using the SHARK-VIS (0.40-0.95 micron) and SHARK-NIR (0.96-1.70 micron) imagers at the LBT. The study uses a combination of narrow-band filters to isolate accretion signatures and broad-band filters for multi-wavelength characterization in both the visible and near-infrared. Our observations recover the primary disk structures previously identified in the literature, albeit at low signal-to-noise (S/N). We identify two compact features with S/N between 6 and 13 in both narrow- and broad-band filters. The first, an elongated structure, matches previous SPHERE detections, while the second, more compact feature, is now confirmed despite its low S/N in earlier datasets. A comparison over a seven-year baseline confirms the stability of both structures. Their observed orbital motion is consistent with Keplerian rotation, potentially suggesting the presence of an undetected planetary-mass companion (few MJup) at the location of the second feature. However, our analysis does not confirm Halpha or Pabeta emission originating from localized accretion. Instead, we conclude that the observed flux is likely stellar light reflected by dust at these locations and discuss alternative mechanisms that could account for such detections.

</details>

### [2026 QQ8: Earth's temporary flyby of maximum lunation](https://arxiv.org/abs/2611.27770)
*Grigori Fedorets, Marco Micheli, Samantha Hemmelgarn et al.* · `astro-ph.EP` · arXiv:2611.27770v1 · relevance 0.09

- **In one sentence**: Astrometric, photometric and dynamical study of asteroid 2026 QQ8, a natural temporary Earth companion on a long-duration flyby orbit near the theoretical maximum-lunation limit, with a solar radiation pressure check to rule out an artificial origin.
- **In plain words**: Sometimes a small asteroid drifts close enough to Earth that it is briefly caught by our planet's gravity and orbits us for a while before escaping, like a short-term moon. This paper looks at one such object, 2026 QQ8, which was newly discovered. The authors tracked its position and brightness, modelled its path, and checked whether sunlight pushing on it matched a natural rock rather than a man-made object; they concluded it is natural and has a rocky, S-type surface.
- **Why it matters**: The text describes it as only the third known temporary Earth companion on a flyby orbit and the first of long duration, with an orbit close to the theoretical upper limit for such captures. This adds to a very small set of observed examples, which is useful for understanding how Earth's gravity briefly traps passing rocks; the text does not go beyond this.
- **Background needed**: - Temporary captured companion: an asteroid that Earth's gravity holds for a time before it leaves, unlike a permanent moon.
- Astrometry: precise measurement of an object's position over time, used to work out its orbit.
- Photometry and spectrophotometry: measuring brightness and colour across wavelengths, used to infer surface composition; S-type asteroids are stony, silicate-rich bodies.
- Solar radiation pressure: the small push sunlight exerts on an object, which depends on its size, shape and mass; used here to tell natural rocks from artificial objects.
- Orbit of maximum lunation: a special orbit in which the captured object stays with Earth for the longest possible time, set by the influence of the Moon.
- Dynamical study: computer modelling of how gravity from Earth, Moon and Sun moves the object. · level: research-level

<details><summary>Original abstract</summary>

Aims: On a rare occasion, asteroids are temporarily captured by the Earth to become the planet's interim companions. The discovery of asteroid 2026~QQ$_8$ provided an opportunity to study this class of objects, adding to the sparse discovery catalogue of Earth's temporary companions. Methods: We performed astrometric, photometric, and dynamical studies of 2026~QQ$_8$, and measured its solar radiation pressure signal to discern between a natural and an artificial origin. Results: We find 2026 QQ$_8$ to be of natural origin, with solar radiation pressure signal commensurable with natural objects and spectrophotometry of an S-type object. 2026 QQ$_8$ is Earth's third discovered otemporarily-captured companion on a flyby orbit, and the first long-duration one, owing this to being on the so-called "orbit of maximum lunation". Its unusual orbit lies close to the theoretical upper duration limit of an object captured in the Earth-Moon system, and has now been observed for the first time.

</details>

## High-energy astrophysics

### [Modelling scintillation in Fast Radio Bursts](https://arxiv.org/abs/2611.27527)
*L. Nicotera, T. Sprenger, O. Wucknitz et al.* · `astro-ph.HE` · arXiv:2611.27527v1 · relevance 0.17

- **In one sentence**: Simulation-based study of how reliably the scintillation bandwidth of fast radio bursts can be recovered from frequency autocorrelation functions under finite observing bandwidth, including averaging of multiple ACFs and a test on Effelsberg observations of FRB 20240114A.
- **In plain words**: Fast radio bursts are millisecond flashes of radio waves from distant galaxies. As they travel through clumpy material in space, their radio spectra get a pattern of bright and dim patches, called scintles, a bit like shimmer on a pool bottom. This paper uses simulations to ask how accurately the typical width of that pattern can be measured when only a few patches fit inside the receiver's frequency range, and reports that averaging several measurements helps.
- **Why it matters**: The width of the scintillation pattern tells us about the scattering material along the line of sight, so measuring it well matters for interpreting these bursts. The text supports a practical framework for uncertainty estimates, but its broader significance beyond FRB modelling is not established from the text alone.
- **Background needed**: - Fast radio burst (FRB): a very brief, very bright radio pulse from outside the Milky Way; some repeat.
- Scintillation: brightness variations caused by turbulent plasma along the path, similar to twinkling stars.
- Scintle: one bright patch in the scintillation pattern across frequency.
- Scintillation bandwidth (nu_s): the typical frequency width of a scintle; it relates to how much scattering material is present.
- Autocorrelation function (ACF): a curve showing how similar a spectrum is to a shifted copy of itself; its width gives the scintillation bandwidth.
- Lorentzian profile: the expected bell-like shape of a well-behaved ACF.
- Finite scintle error (FSE): an empirical prescription for the uncertainty of the measured bandwidth.
- Bootstrap resampling: estimating uncertainty by repeatedly resampling the data. · level: research-level

<details><summary>Original abstract</summary>

Fast Radio Bursts (FRBs) are bright, ms-duration, extragalactic radio transients. Propagation through inhomogeneities in the ionised medium produces scintillation, observed as frequency-dependent intensity variations in their spectra, with bright patches, called scintles. The characteristic scintillation bandwidth probes scattering material along the line of sight. Measuring this scale can be challenging when the observing bandwidth of the burst spectra contains a few scintles. We study the uncertainties associated with recovering $\nu_s$ from frequency autocorrelation functions (ACFs) under finite-bandwidth conditions. We examine the recovery of $\nu_s$ from individual ACFs and investigate if averaging multiple independent ACFs provides a more robust measurement. Using simulations, we reproduce observational conditions to investigate the modelling of scintillation in ACFs and the associated measurement uncertainties. We use these simulations to test the finite scintle error (FSE) prescription and assess its applicability to real observations. We test the resulting modelling framework on Effelsberg Ultra Broad Band receiver observations of the repeating FRB 20240114A. As the number of scintles decreases, individual ACFs develop fluctuations that deviate from the expected Lorentzian profile. This results in increased scatter in the recovered $\nu_s$ and a less reliable FSE prescription. Averaging multiple independent ACFs mitigates these effects and improves the recovery of $\nu_s$ in the low-scintle regime. Our results provide a framework for ACF modelling and uncertainty estimation in FRBs. For individual bursts, the FSE is effective with sufficient scintles; we find $\eta = 0.055$ more suitable for FRB analysis and update the FSE accordingly. For repeaters, averaging multiple ACFs and bootstrap resampling improve the recovery and uncertainty estimation of $\nu_s$.

</details>

### [From Binary Wind to Radio Burst: Dispersion-Measure Evolution after Accretion-induced Collapse](https://arxiv.org/abs/2611.26696)
*Smadar Naoz, Victoria M. Kaspi* · `astro-ph.HE` · arXiv:2611.26696v1 · relevance 0.13

- **In one sentence**: An angle-dependent toy model of aspherical accretion-induced white-dwarf collapse ejecta expanding through a shaped circumstellar wind, showing how the dispersion measure of repeating fast radio bursts can rise or fall over decades depending on upstream ionization.
- **In plain words**: Some repeating radio bursts from space show their "dispersion measure," a measure of how much electrically charged gas lies along the line of sight, slowly changing over years. This paper studies a possible cause: a white dwarf star collapsing into a neutron star, whose debris pushes through a lopsided pocket of gas left by its companion star. The authors model how this debris changes the measured value over time in two kinds of surroundings, one diffuse and one dense and cloud-like.
- **Why it matters**: Measured changes in this value are used to probe the environment around these bursts, so a model that explains both increasing and decreasing trends could help interpret them. The work is a simplified toy model, so its relevance to real sources is suggestive rather than established.
- **Background needed**: - Fast radio bursts (FRBs): brief, bright radio flashes from distant galaxies; some repeat.
- Dispersion measure (DM): the total amount of free electrons along the path of a radio signal; radio waves at different frequencies arrive at slightly different times, and the delay gives DM.
- Secular DM variation: a slow, steady change in DM over years, possibly from changing gas around the source.
- White dwarf: the dense, dead core of a Sun-like star. Accretion-induced collapse: a white dwarf that gains mass from a companion and collapses into a neutron star.
- Ejecta, shock, and wind bubble: material thrown off by the collapse, the wave it drives into surrounding gas, and the cavity carved out by earlier stellar winds.
- Ionized vs. neutral gas: whether the surrounding gas already has free electrons; shocks can strip electrons from neutral gas and raise DM.
- The model is a simplified, idealized calculation, not a fit to any specific source. · level: research-level

<details><summary>Original abstract</summary>

Secular changes in the dispersion measures (DMs) of repeating fast radio bursts probe the source-local plasma. Such DM time variability has been interpreted with spherical, single-density-profile models. Accretion-induced collapse (AIC) of a white dwarf may instead follow binary interaction and occur inside a finite, anisotropic circumstellar structure. Here, we construct an angle-dependent toy model of aspherical AIC ejecta propagating through a pre-AIC free wind, shocked-wind bubble, swept-up external shell, and polar cavity, exploring a diffuse environment (number density of $1~{\rm cm^{-3}}$, located at $10~$pc) and a compact cloud (number density of $500~{\rm cm^{-3}}$, located at $0.3~$pc), bracketing ionized and initially neutral upstream gas. The unshocked ejecta initially yield ${\rm DM}\propto t^{-2}$, while crossings of the finite wind-bubble interfaces produce breaks and curvature in ${\rm DM}(t)$. In initially neutral models, shock ionization can overcome geometric dilution: the total DM reverses from decline to growth after approximately $10$--$20$ yr and later turns over as the finite reservoir is processed. Ionized-upstream models instead generally decline or flatten. Without fitting individual sources, our models span both signs and the approximate magnitudes of the secular DM-variation rates measured among repeaters. In this dynamical framework, DM evolution is set by shock propagation through the circumsource density and ionization structure, rather than the contemporaneous burst rate, distinguishing it from photoionization-driven scenarios. Consequently, in our model, an instantaneous \(d{\rm DM}/dt\) is not a unique indicator of source age. We suggest that the observed distribution of secular DM variation slope amplitudes and signs will be important for distinguishing among different models of DM variations in repeating FRBs.

</details>

## Stars and the Sun

### [Characterisation of B-type stars in four young Galactic open clusters. II. Photometric variability with TESS and identification of pulsating stars](https://arxiv.org/abs/2611.27680)
*Federica Nardini, Dominic M. Bowman, Julia Bodensteiner et al.* · `astro-ph.SR` · arXiv:2611.27680v1 · relevance 0.14

- **In one sentence**: Photometric study with TESS full-frame images of 82 B-type stars in five young Galactic open clusters (h and χ Persei, NGC 457, NGC 581, NGC 1960), classifying pulsator types and checking binarity, with light curves extracted for 63 stars.
- **In plain words**: This paper looks at hot, massive young stars grouped in star clusters about 15 to 30 million years old. The authors used brightness measurements from NASA's TESS space telescope to track how each star's light rises and falls over time. They found that most of the stars pulse, meaning their brightness changes because their surfaces swell and shrink, and they sorted them into pulsation types.
- **Why it matters**: Pulsations change how massive stars evolve, and clusters are useful test cases because their stars share an age and composition. The paper also suggests pulsations do not much hide close companion stars from spectroscopic detection, except in Be stars, where the authors argue the velocity threshold should be higher; how far this generalises beyond these five clusters is not established by the text.
- **Background needed**: - B-type stars: hot, luminous, massive stars, much hotter than the Sun.
- Open cluster: a loose group of stars born together from the same gas cloud, so they share roughly the same age and chemistry.
- Pulsation: a star's surface periodically expanding and contracting, seen as regular brightness changes.
- Beta Cephei stars: a class of B-type pulsators with short pulsation periods.
- Be stars: B-type stars that show emission lines from a surrounding gas disc, usually spinning rapidly.
- TESS: a NASA satellite that measures the brightness of many stars over time; full-frame images cover whole sky regions.
- Photometry / light curve: a record of a star's brightness versus time.
- Spectroscopic binary: two stars orbiting each other, detected by periodic shifts in spectral lines (radial velocity). · level: research-level

<details><summary>Original abstract</summary>

Pulsations and binarity are important properties of massive stars and influence their structure and evolution. Young open clusters are ideal laboratories to study massive stars, since they are mostly coeval and chemically homogeneous. We analyse 82 B-type stars in the Galactic open clusters $h$ and $\chi$ Persei, NGC 457, NGC 581, and NGC 1960, which have ages between 15 and 30 Myr. We extract light curves using both simple aperture photometry and a point-spread-function-based method that minimises contamination from crowded fields in full-frame images from the Transiting Exoplanet Survey Satellite (TESS) mission. We successfully extract light curves for 63 stars. The majority have photometric variability caused by pulsations, showing how pulsations are a common property of young B-type stars in clusters. We classify stars into different pulsator types based on their spectral type and frequency spectrum. The most common pulsator class are beta Cephei stars, with 29 stars in total, and we discover pulsation modes in almost all stars with a spectral type of B2 or earlier. All Be stars show pulsations, which supports the consensus of the ubiquity of pulsations in these stars. Finally, we confirm that the majority of early B-type stars are in binary systems, except for two pulsating Be stars and a star with rotational modulation. This indicates that pulsations do not significantly bias the spectroscopic detection of short-period binaries, except for Be stars where the spectroscopic radial velocity variability threshold should be higher than the typical value of 20 km s$^{-1}$.

</details>

### [Accretor Luminosity as Probe of Orbital Evolution and Magnetic Braking in AM CVn Binaries](https://arxiv.org/abs/2611.26973)
*Tin Long Sunny Wong, Peter Scherbak, Jim Fuller* · `astro-ph.SR` · arXiv:2611.26973v1 · relevance 0.05

- **In one sentence**: Uses the cooling luminosity of the white dwarf accretor in AM CVn binaries as a probe of orbital evolution, finding that extra magnetic-braking angular momentum loss beyond gravitational waves is needed, and testing several magnetic braking prescriptions.
- **In plain words**: AM CVn systems are tiny pairs of stars in which a white dwarf (a dense, burnt-out star) steals helium-rich material from a companion orbiting very closely, completing an orbit in under about an hour. The brightness of the white dwarf depends on how fast material is being fed to it, so measuring it tells us how the pair's orbit has been shrinking or widening over time. The authors find that observed white dwarfs look brighter (younger) than predicted if the orbit shrinks only by gravitational-wave emission, and that adding extra angular momentum loss from magnetic braking of the donor star fits better.
- **Why it matters**: Orbital evolution of these binaries is hard to observe directly, so using accretor brightness as a clock offers an indirect test of how stars lose spin and angular momentum. The paper's finding that some popular magnetic braking formulas fail while others need large boosts suggests the physics is not yet settled, though the results depend on the models used and the text does not show how robust they are.
- **Background needed**: - AM CVn binaries: ultracompact systems (orbits under about 70 minutes) where a white dwarf accretes helium-rich matter from a semidegenerate donor.
- Orbital period: the time for the two stars to complete one orbit; shorter periods mean the stars are closer together.
- Accretor: the white dwarf that receives the transferred material.
- Gravitational-wave emission: energy and angular momentum lost by orbiting masses, which shrinks the orbit and is the baseline mechanism here.
- Magnetic braking: loss of angular momentum from a star's magnetized wind, which slows its spin and can shrink or change the orbit; several formalisms (Rappaport et al. 1983, Matt et al. 2015, CARB) are tested.
- Evolved cataclysmic variable (CV) channel: one of several proposed evolutionary routes that produce AM CVn systems.
- Cooling luminosity: how brightly a white dwarf radiates as it cools; a hotter, brighter accretor implies recent heating from accretion. · level: research-level

<details><summary>Original abstract</summary>

AM CVn binaries are ultracompact systems with orbital periods $P_{\rm orb} \lesssim 70$ min, where a white dwarf accretes from a He-rich semidegenerate donor. At short orbital periods ($P_{\rm orb} \lesssim 20$ min), rapid accretion reheats the accretor. As the system widens and the mass transfer rate decreases, the accretor follows standard white dwarf cooling at longer orbital periods ($P_{\rm orb} \gtrsim 30$ min). The accretor cooling luminosity then acts as a powerful probe into the orbital evolution of the binary. Recent observations show that the accretor appears brighter (younger) at long orbital periods, compared to models where orbital angular momentum loss is solely set by gravitational wave emission. We show that additional angular momentum loss, which we ascribe to magnetic braking of the donor, can better reproduce observations of accretor luminosity. We test and constrain various proposed magnetic braking formalisms, for the white dwarf, helium star, and evolved cataclysmic variable (CV) channels for AM CVn formation. None of the magnetic braking formalisms in their original form can reproduce the observations, but the widely popular magnetic braking proposed by Rappaport et al. 1983 boosted by a factor $\approx 5$, or the saturated magnetic braking proposed by Matt et al. 2015 boosted by a factor of $\approx 150$, yields satisfactory results. We also find that the CARB formalism, recently applied to the evolved CV channel, is strongly in tension with observations of accretor luminosity. Our models motivate UV spectroscopy observations, and dedicated WD atmosphere models for AM CVn accretors.

</details>

## Chemical physics

### [Molecular structure breaks universality in screening behavior of electrolyte solutions](https://arxiv.org/abs/2611.27955)
*Anna T. Bui, Connie J. Fairchild, Dominic P. W. Thomas et al.* · `cond-mat.stat-mech` · arXiv:2611.27955v1 · relevance 0.13

- **In one sentence**: Using machine-learned classical density functional theory, the paper computes numerically exact screening decay lengths for electrolyte models of increasing molecular complexity and finds that solvent and ion structure break the apparent universal scaling of screening in concentrated electrolytes.
- **In plain words**: Salt water shields electric charges over a certain distance, called the screening length. For dilute salt solutions this follows a well-known universal rule, but experiments on concentrated solutions have seemed to show a single common pattern, and researchers disagree about why. This paper uses a machine-learning-assisted theory to calculate these lengths for a range of simplified models, from simple charged spheres up to models with more realistic solvent and ion shapes.
- **Why it matters**: The result suggests that the apparent universal pattern seen in concentrated electrolytes may not come from equilibrium physics alone, which bears on the debate over "anomalous underscreening." The text does not show how far these model results carry over to real experimental systems, so that link remains to be tested.
- **Background needed**: - Electrolyte: a liquid, such as salt dissolved in water, containing charged ions.
- Screening: charges in a liquid are partly hidden by surrounding ions, so their electric pull fades over a characteristic distance (the screening or decay length).
- Debye–Hückel theory: the standard, simple description of screening that works well for dilute solutions.
- Underscreening: observed screening that is weaker than the simple theory predicts at high concentration.
- Classical density functional theory: a statistical method for computing how molecules arrange themselves near charges in a liquid, without simulating every molecule.
- Machine learning here is used to help build the functional that the theory needs; the text does not give details.
- Re-entrant behavior: a trend that changes direction and then changes back as a parameter varies. · level: research-level

<details><summary>Original abstract</summary>

Electrostatic screening is one of the most fundamental phenomena in electrolyte solutions. While dilute electrolytes are described by the universal Debye--H\"uckel theory, recent experiments have reported an apparently universal scaling law for screening lengths in concentrated electrolytes, fueling ongoing debate over anomalous underscreening. Yet, liquid state theory has been unable to determine whether molecular details of the solvent, the ions, or both should preserve or break such universality. Using machine-learned classical density functional theory, we compute numerically exact decay lengths across a hierarchy of electrolyte models of increasing molecular complexity. We find that molecular details qualitatively reshape screening: solvent attraction generates a new monotonic decay mode, solvent polarity produces re-entrant behavior, and ionic structure alone can drastically alter screening-length exponents. Consequently, no single scaling law describes screening universally across these molecularly distinct electrolytes. Our results challenge equilibrium interpretations of experimentally observed universality in concentrated electrolytes.

</details>

### [Length and Sequence-Dependent Dipolar and Electronic Properties of $\alpha$-helical Polypeptides](https://arxiv.org/abs/2611.26892)
*Faezeh Shabani, Florian G\"unther, Sibylle Gemming* · `physics.chem-ph` · arXiv:2611.26892v1 · relevance 0.05

- **In one sentence**: Density-functional tight-binding calculations examine how chain length, sequence, and external electric fields shape the dipole moments and frontier orbital energies of three α-helical polypeptide families.
- **In plain words**: This is a computer-simulation study of short man-made protein-like chains that coil into helices, a shape found in many natural proteins. The authors asked how making the chain longer, or swapping in different amino acids, changes its electrical charge balance (dipole) and the energy levels that govern how it could accept or give up electrons. They report that longer helices gain a larger overall dipole and that the backbone's aligned carbonyl groups drive most of this effect.
- **Why it matters**: Understanding how helix length and sequence control electronic behavior could guide the design of peptide-based materials for bio-electronic interfaces, biosensors, and electron-transfer systems. The text frames this as a foundational blueprint, but it is a theoretical study of idealized models, so any practical device use would require experimental testing that this text does not describe.
- **Background needed**: - α-helix: a coiled, spiral backbone shape in proteins, held together by hydrogen bonds between nearby residues.
- Polypeptide: a chain of amino acids linked together; here, short idealized chains of alanine, leucine, cysteine and lysine.
- Dipole moment: a measure of how unevenly electric charge is spread across a molecule, like a tiny built-in positive and negative end.
- HOMO-LUMO gap: the energy difference between the highest occupied and lowest empty electron energy levels; it roughly indicates how easily a molecule is electronically excited.
- Density-functional tight-binding (DFTB): a fast, approximate quantum-chemistry method for estimating molecular electronic structure.
- Stark effect: a shift in energy levels caused by an electric field.
- The text gives no experimental validation details, and the reported ~5 eV local gap is a computed value for the model systems. · level: research-level

<details><summary>Original abstract</summary>

Helical polypeptides combine the chemical tunability of synthetic macromolecules with the highly ordered backbone architecture of natural proteins. Here, density-functional tight-binding calculations are used to determine how chain length and sequence chemistry govern the dipolar and electronic properties of three $\alpha$-helical polypeptide families: polyalanine [AAAAA]$_n$, leucine-modified [AAAAL]$_n$, and cysteine-capped, lysine-containing C[AAAAK]$_n$. Increasing chain length produces systematic shifts and splitting of the molecular orbital levels together with an approximately additive increase in the molecular dipole. Analysis of the C[AAAAK]$_3$ helix shows that aligned backbone carbonyl groups provide the dominant contribution to the macro dipole, whose growing electrostatic potential is consistent with an intrinsic Stark-like contribution to the length-dependent orbital-energy evolution. Side-chain and terminal modifications introduce localized perturbations to frontier electronic states while preserving this global backbone-driven trend. Residue-resolved frontier levels additionally form a staircase-like energy landscape along the helical scaffold: individual peptide units retain large local HOMO-LUMO gaps of approximately 5 eV, whereas spatially proximate hydrogen-bonded residues exhibit smaller inter-residue energy separations. Application of external electrostatic fields modifies the frontier-level separation in a direction-dependent manner and induces structural distortions predominantly near the flexible termini, while the helical core remains comparatively robust. By establishing these fundamental sequence-structure-property relationships, this work provides a foundational blueprint for the rational design of peptide-based biomacromolecules tailored for next-generation bio-electronic interfaces, biosensors, and artificial electron-transfer systems.

</details>

## Materials science

### [Designing Perovskites for Chemical Looping Hydrogen Production](https://arxiv.org/abs/2611.27580)
*Ivana Stani\v{c}i\'c, Alfred Juhlin Onbeck, Anders Hellman et al.* · `cond-mat.mtrl-sci` · arXiv:2611.27580v1 · relevance 0.10

- **In one sentence**: An autonomous active-learning loop (Wasserstein autoencoder plus deep-ensemble surrogate) searched perovskite compositions for hydrogen production capacity in chemical looping, raising the mean capacity of acquired candidates from 0.41 to 2.05 mmol H2/g over 50 cycles, then ranking 20 candidates with cost, supply and environmental criteria.
- **In plain words**: This work is about finding better solid materials for making hydrogen through a cyclic chemical process, where a metal-oxide-type solid repeatedly gives up and takes back oxygen. The search space of possible mixtures is huge, so the authors used a computer system that proposed new mixtures, learned from the results, and chose what to test next. Across seven runs, the average hydrogen yield of the chosen mixtures rose substantially, and the authors then picked 20 candidates that also balance raw-material price, supply risk and environmental impact.
- **Why it matters**: Finding practical materials faster could support cleaner hydrogen production, which matters for decarbonizing industry. The text reports computational results only, with no experimental validation mentioned, so the real-world performance of the candidates remains to be shown; the authors do say the method may transfer to other chemical looping processes.
- **Background needed**: - Perovskites: a family of crystal structures with a general formula ABO3, where different metal elements can be swapped into the A and B sites to tune properties.
- Chemical looping: a two-step cycle in which a solid oxygen carrier is reduced and then reoxidized, here used to split water and produce hydrogen.
- Hydrogen production capacity (HPC): the amount of hydrogen produced per gram of material, in mmol/g.
- Active learning: an iterative method in which a model predicts promising candidates, they are evaluated, and the model is updated to choose the next batch.
- Autoencoder: a neural network that compresses data into a smaller representation; a Wasserstein autoencoder is a variant that shapes this representation in a specific mathematical way.
- Deep ensemble: several neural networks trained separately whose spread of predictions indicates uncertainty.
- Multi-objective ranking: combining several criteria (here performance, price, supply resilience, and health and environmental impact) into one ordering. · level: research-level

<details><summary>Original abstract</summary>

Perovskites are promising materials for chemical looping hydrogen production (CLHP) due to their compositional flexibility and tunable redox properties. However, cation substitution opens a vast compositional space, making screening for new high-performing materials computationally demanding. Here, an autonomous active-learning framework combining a Wasserstein autoencoder (WAE) with a deep ensemble surrogate model was used to search for perovskites with a high hydrogen production capacity (HPC). In seven independent runs of 50 cycles, the mean HPC of the acquired compositions rose from 0.41 mmol H$_2$ g$^{-1}$ in the starting set to 2.05 mmol H$_2$ g$^{-1}$, and the best compositions reached 2.65-2.99 mmol H$_2$ g$^{-1}$. All runs enriched Sn on the B-site, mostly combined with Ti and with Mg, Ce, K and Y on the A-site. Twenty diverse candidates (2.22-2.84 mmol H$_2$ g$^{-1}$) were then selected by a multi-objective ranking that also accounts for raw-material price, supply resilience and potential environmental and health impacts. The approach links materials discovery with practical deployment constraints, and the methodology is transferable to other chemical looping processes.

</details>

### [Edge-dislocation interactions with sub 3 nm vacancy and interstitial clusters in FeCr alloys: Mechanisms, Obstacle strength and Fate](https://arxiv.org/abs/2611.27583)
*Layatmika Sahoo, Suchandrima Das* · `cond-mat.mtrl-sci` · arXiv:2611.27583v1 · relevance 0.09

- **In one sentence**: Molecular dynamics simulations of an edge dislocation passing through relaxed sub-3 nm vacancy and mixed Fe-Cr interstitial clusters in Fe-3Cr, Fe-5Cr and Fe-10Cr at 300 K, quantifying obstacle strength, survival and Cr segregation to test low-dose hardening models.
- **In plain words**: Metal alloys used in nuclear reactors get harder and more brittle under radiation, even when microscopes show no visible defects at low doses. This paper uses computer simulations of atoms to test how very small clusters of missing atoms (vacancies) and extra atoms (interstitials) in iron-chromium alloys block a moving line defect called a dislocation. The simulated vacancy clusters were always strong blockers and were never cut through, while most interstitial clusters were weaker and were usually absorbed, with a few surviving.
- **Why it matters**: Hardening models often ignore defects too small to see, so their strength values may be inflated when fitted to visible defects only; this work offers defect-specific strengths that could inform those models. The text reports these as simulation results at 300 K and upper bounds, so their direct relevance to real reactor materials is not established here.
- **Background needed**: - Dislocation: a line-like crystal defect whose movement lets metals deform; obstacles that block it make the metal harder.
- Irradiation hardening: radiation creates tiny defect clusters that block dislocations, raising strength and reducing ductility.
- Molecular dynamics (MD): simulating how each atom moves under interatomic forces, limited to very short times and small boxes.
- Vacancy vs. interstitial: a vacancy is a missing atom; an interstitial is an extra atom squeezed between normal lattice sites.
- Platelet and loop: flat, disc-like defect clusters; loops are closed rings of extra or missing atom planes, with Burgers vectors such as 1/2<111> or <100>.
- Obstacle strength (alpha): a dimensionless measure of how strongly an obstacle resists dislocation motion in standard hardening models.
- Transmission electron microscopy (TEM): an imaging method that resolves defects only above a certain size.
- Fe-Cr alloys: iron with chromium additions, studied for structural materials in nuclear systems. · level: research-level

<details><summary>Original abstract</summary>

Fe-Cr alloys harden at irradiation doses where transmission electron microscopy (TEM) shows no defects, implicating defects too small to be resolved. Their obstacle strength is unknown, so hardening models ignore them and fit measured hardening to visible defects alone. Here, molecular dynamics drives an edge dislocation through relaxed 1-3 nm vacancy and mixed Fe-Cr interstitial clusters in Fe-3Cr, Fe-5Cr and Fe-10Cr at 300 K. Vacancy clusters relax into platelets whose strength rises with size to about 350 MPa at 2.9 nm, following strong-obstacle scaling independently of Cr content, and always survive dislocation passage. Interstitial clusters relax into $\frac{1}{2}\langle 111 \rangle$, mixed or $\langle 100 \rangle$ loops. They are mostly weaker than platelets of the same size, their strength varies up to fivefold with the local Cr arrangement, and most are absorbed. Only $\langle 100 \rangle$ loops in Fe-5Cr and Fe-10Cr often survive. During pinning, Cr collects at the junction between these loops and the dislocation; atom tracking for one loop shows that more than half comes from the loop itself. Surviving loops are not stronger than absorbed ones: strength and survival are thus distinct. Computed dispersed-barrier strengths ($\alpha \approx$ 0.02-0.25) are upper bounds that lie below the $\alpha$ values obtained in earlier studies by fitting hardening to TEM-visible loops. These earlier values are therefore inflated by TEM-invisible defects. Wherever small vacancy clusters form, they are more effective obstacles than interstitial clusters of the same size. These defect-specific strengths and fates provide a physical basis for models of low-dose hardening.

</details>

## Soft matter and polymers

### [Decoupling Entropic and Enthalpic Elasticity in Crosslinked Polymer Nanocomposites](https://arxiv.org/abs/2611.27259)
*Chiranjit Majhi, Sivasurender Chandran, Krishnacharya Khare* · `cond-mat.soft` · arXiv:2611.27259v1 · relevance 0.09

- **In one sentence**: Using temperature-dependent thermomechanical measurements on crosslinked PDMS silica and titania nanocomposites, the authors separate entropic and enthalpic elasticity and find that the effective crosslink density at the particle interface drops by about an order of magnitude when particles lie closer than a critical mean separation.
- **In plain words**: Rubber-like materials can be stiffened by mixing in tiny particles, but it is unclear how much of that stiffening comes from changes in the polymer's stretching behavior versus changes in its internal energy. This paper splits the two contributions apart by measuring how the material responds to temperature. It finds that adding particles raises the effective number of crosslinks at low loadings, then levels off, and that the particle-adjacent regions contribute less stretch-related elasticity when particles are crowded together.
- **Why it matters**: The work addresses how nanoparticles change the mechanics of elastomers at the interface, which matters for designing tougher or stiffer rubber-like materials. The reported trends were checked with two particle types and with X-ray scattering on one of them, though the text does not establish how far the conclusions extend to other systems.
- **Background needed**: - Elastomer: a rubbery polymer network, here poly(dimethylsiloxane), a silicone.
- Crosslinks: chemical bridges tying polymer chains together; crosslink density is how many per unit volume.
- Elasticity has two parts: entropic (chains resisting being uncoiled, driven by disorder) and enthalpic (energy stored in bonds and interactions).
- Nanocomposite: a polymer with nanoscale filler particles (here silica or titania).
- Volume fraction: the fraction of the material's volume occupied by particles.
- Thermomechanical measurement: tracking how stiffness changes with temperature to infer the energy versus entropy split.
- Interface region: the thin layer of polymer around each particle whose properties differ from the bulk.
- X-ray scattering: a probe of nanoscale structure, used here to check particle arrangement. · level: research-level

<details><summary>Original abstract</summary>

Nanoparticle-induced local interface regions significantly enhance the bulk mechanical behavior of polymer nanocomposites, yet their energetic contribution in crosslinked elastomer networks remains poorly understood. Here, we decouple the entropic and enthalpic contributions to the elasticity of crosslinked poly(dimethylsiloxane) nanocomposites using temperature-dependent thermomechanical measurements. While the measured bulk elastic modulus exhibits a monotonic increase with nanoparticle volume fraction $\phi_{\rm n}$, we observe that the effective crosslink density initially increases before saturating at larger $\phi_{\rm n}$. These results are independently validated across two nanoparticle systems (silica and titania) and directly confirmed by X-ray scattering experiments on silica-based composites, highlighting the generality of the observation. The trends in effective crosslink density indicate that the elastic response is predominantly entropy-driven at low nanoparticle concentrations, whereas enthalpic contributions become increasingly significant at higher loadings. Assuming a linear superposition of interface and bulk contributions, these results reveal that the effective crosslink density at the particle interface decreases by an order of magnitude below a critical mean interparticle separation, indicating that localized particle proximity and clustering constrain the entropic elasticity at higher loadings.

</details>

### [Lacrymaria-like dynamics: compression and length change in active slender bodies](https://arxiv.org/abs/2611.27577)
*Cl\'ement Moreau, Yukinori Nishigami, Johann H\'erault et al.* · `cond-mat.soft` · arXiv:2611.27577v1 · relevance 0.07

- **In one sentence**: A planar N-link model of active filaments in which both bending angles and segment lengths evolve under resistive-force drag, used to study how axial compression couples to bending for swimming, crawling, and Lacrymaria-like neck dynamics.
- **In plain words**: Many tiny swimming or crawling organisms, such as the single-celled Lacrymaria olor, stretch and shorten their slender bodies as they move, but most computer models treat these bodies as if they cannot change length. This paper builds a model in which both the bending and the length of each segment of a flexible filament change over time, with the surrounding fluid's drag acting on each piece. The authors report that passive stretchiness usually slows swimming, while prescribed length waves can speed up, slow down, or redirect movement depending on their timing and wavelength relative to the bending.
- **Why it matters**: Length change is common in microscopic organisms but is usually ignored in locomotion models, so a model that includes it may help explain how such organisms move and search their surroundings. The text does not show how far these results carry over to real cells, so their applicability should be treated as open.
- **Background needed**: - Elastohydrodynamics: how elastic bodies (like flexible filaments or cilia) deform and move through a viscous fluid where inertia is negligible.
- Resistive force theory: an approximation that treats the fluid drag on each small piece of a slender body as proportional to its local velocity, with different coefficients along and across the body.
- N-link model: a filament approximated as a chain of N rigid segments joined by hinges; here the segment lengths are also allowed to vary.
- Passive vs active: passive compressibility means the body stretches or compresses according to its elasticity; active means the organism drives length changes itself (here via prescribed rest-length waves).
- Follower forces: forces whose direction moves with the body as it bends, used here to drive oscillations.
- Lacrymaria olor: a single-celled protist with a long, extensible neck used to explore its surroundings. · level: research-level

<details><summary>Original abstract</summary>

Length change is central to the behaviour of many active slender bodies, yet most elastohydrodynamic models of microscopic locomotion treat filaments as effectively inextensible. Here we introduce a compressible $N$-link formulation for planar active filaments, in which both bending angles and segment lengths are dynamical variables coupled through local hydrodynamic drag, modelled using resistive force theory. We first use the model to test whether passive extensibility can improve bending-driven swimming and crawling. Across the parameter ranges studied, passive compressibility usually reduces locomotion speed, indicating that axial compliance alone is not a robust mechanism for propulsion enhancement. We then prescribe active rest-length waves and show that compression can either enhance, suppress, or redirect locomotion depending on its phase, wavelength, and frequency relative to bending. Finally, motivated by the extensible neck dynamics of \textit{Lacrymaria olor}, we apply the method to clamped and free filaments driven by oscillatory follower forces. These examples show that elastic compression-bending coupling can reorganise swimming, exploration, and locomotion in strongly deforming active filaments.

</details>

## AI for chemistry and materials

### [Beyond the Ground State: Assessing the Machine-Learned Skala Functional in {\Delta}SCF Calculations of Molecular Excitation Energies](https://arxiv.org/abs/2611.27711)
*Egor Trushin, Thomas D. K\"uhne* · `physics.chem-ph` · arXiv:2611.27711v1 · relevance 0.18

- **In one sentence**: This paper benchmarks the machine-learned Skala exchange-correlation functional against PBE, r²SCAN and PBE0 for molecular excitation energies and singlet-triplet gaps computed with the ΔSCF approach, under both UKS and ROKS formalisms.
- **In plain words**: Computer simulations of molecules use an approximate rule, called a density functional, to estimate their energies. This paper tests a newly machine-learned version, Skala, on how much energy a molecule needs to jump to an excited state, a question it was not primarily built for. Skala was most accurate on some tests and less accurate on others, depending on the type of excitation and how the calculation is set up.
- **Why it matters**: Excited-state energies matter for predicting colour, light absorption and photochemistry, so a functional that transfers beyond ground-state energies would be useful. The text reports mixed results, including negative singlet-triplet splittings for most ST-gap molecules with Skala under one common-orbital setup, so its transferability is supported only in part and should be read with that caveat.
- **Background needed**: - Density functional theory (DFT): a common method that estimates molecular energies from electron density; the exchange-correlation (XC) functional is the approximate piece that carries most of the difficulty.
- Skala: a machine-learned XC functional, described here as trained mainly on ground-state energies.
- Excitation energy: the energy needed to lift a molecule from its ground state to an excited state.
- ΔSCF: a shortcut that gets an excited-state energy by optimising the electron arrangement for the excited state and taking the energy difference.
- UKS / ROKS: two ways of handling open-shell (unpaired-electron) systems in Kohn-Sham DFT.
- Singlet-triplet gap: the energy difference between two spin states of a molecule; a "inverted" gap means the ordering is reversed from the usual one.
- MAE (mean absolute error): the average size of the error against reference values.
- QUEST benchmark sets: reference collections of excitation energies used to compare methods.
- PBE, r²SCAN, PBE0: established functionals used as baselines. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

We assess the transferability of the machine-learned Skala exchange-correlation (XC) functional beyond ground-state energetics using molecular vertical excitation energies and singlet-triplet gaps calculated with the $\Delta$-self-consistent-field ($\Delta$SCF) approach. We compare Skala with PBE, r$^2$SCAN, and PBE0 on subsets covering small-molecule excitations (QUEST1), inverted singlet-triplet gaps (ST-gap), and intramolecular charge-transfer excitations (QUEST6). Both spin-unrestricted Kohn-Sham (UKS) and restricted open-shell Kohn-Sham (ROKS) formalisms are considered. On QUEST1, Skala achieves the lowest mean absolute errors (MAEs) for singlet and triplet excitation energies with both formalisms, although PBE0 and r$^2$SCAN provide more accurate singlet-triplet gaps through error cancellation. For ST-gap, Skala yields the lowest gap MAEs with both UKS and ROKS. Evaluating the mixed-spin and triplet energy components on the same orbitals optimized for the ROKS open-shell singlet yields negative splittings for seven of eight ST-gap molecules with Skala. Separate triplet optimization increases the gaps, but six remain negative. All three conventional functionals give positive common-orbital splittings and optimized gaps for all eight molecules. For QUEST6, treated with UKS only, Skala yields more accurate singlet excitation energies than PBE and r$^2$SCAN but remains less accurate than PBE0. Across QUEST1 and ST-gap, Skala yields lower MAEs with UKS than ROKS. Overall, these results support Skala's transferability to molecular excited states while highlighting its dependence on the excitation class and open-shell treatment.

</details>

### [Prediction of lattice thermal conductivity of half-Heusler compounds by machine learning and transfer-function calibration](https://arxiv.org/abs/2611.26788)
*Shivam Randive, Ojaswini Randive, Heet Lungaria et al.* · `cond-mat.mtrl-sci` · arXiv:2611.26788v1 · relevance 0.15

- **In one sentence**: The paper quantifies a systematic overestimate of calculated versus measured lattice thermal conductivity across cubic 18-electron half-Heusler compounds and proposes a temperature-dependent transfer function, combined with a machine-learning model, to correct screening predictions.
- **In plain words**: Researchers who search for new materials that turn heat into electricity often estimate how well each candidate conducts heat through its crystal lattice, using computer calculations or machine-learning models trained on them. These estimates describe a perfect single crystal, while real lab samples are polycrystalline and have grain boundaries and defects that block heat, so the estimates run high. This paper measures that gap across a whole family of compounds, finds it shrinks as temperature rises, and fits a simple correction that removes most of the average error.
- **Why it matters**: Screening lists for thermoelectric materials depend on these heat-conduction estimates, so a known, correctable bias could make candidate rankings more reliable. The text reports that the corrected predictions approach the spread between independent labs, but it does not show that the method has been applied to new materials in practice.
- **Background needed**: - Thermoelectric materials convert heat differences into electrical voltage and vice versa; good ones conduct electricity well but heat poorly.
- Lattice thermal conductivity (kappa_L) is the part of heat conduction carried by atomic vibrations (phonons) through the crystal framework.
- Half-Heusler compounds are a family of crystals with a common three-part atomic arrangement; "18 valence electrons" refers to a count of outer electrons per formula unit that groups them by bonding type.
- First-principles calculations use quantum-mechanics equations on an ideal, defect-free crystal, with no inputs beyond atomic species and structure.
- Polycrystalline samples are made of many small grains; grain boundaries and point defects scatter phonons and lower measured conductivity.
- A transfer function here means an empirical correction that maps calculated values onto measured ones, with a fitted temperature dependence.
- High-throughput screening evaluates many candidate compounds computationally before any synthesis. · level: research-level
- Matched keywords: crystal structure

<details><summary>Original abstract</summary>

High-throughput searches for half-Heusler thermoelectrics increasingly rely on lattice thermal conductivity ($\kappa_L$) from first-principles calculations, or from machine-learning models trained on them. These calculations describe an ideal single crystal, whereas measurements are made on polycrystalline samples, in which grain boundaries and defects scatter heat as well. The resulting gap between calculated and measured $\kappa_L$ has been noted for individual compounds but not, to our knowledge, quantified across a materials class, so the values used for screening carry an unknown, systematic bias. Here we quantify and correct this bias for cubic half-Heusler compounds with 18 valence electrons. Using a curated literature corpus that keeps calculated and measured values apart, we show that calculations overestimate measured $\kappa_L$ in most bonding families, and that the excess shrinks with temperature. Scattering by defects, added to the intrinsic scattering between lattice vibrations, would give such a trend, but the data do not single out one cause. A simple transfer function with this temperature dependence removes the median offset, and refitting its magnitude within a bonding family lowers the median error further, though not consistently compound by compound. Combined with a machine-learning model that predicts the calculated value from crystal structure, and tested on chemistries withheld from all fitting, the method predicts measured $\kappa_L$ in this class about as closely as independent laboratories agree with one another, and provides testable predictions for compounds not yet measured.

</details>

## Biochemistry

### [Nonheme Fe Enzyme-Catalyzed Enantioselective and Regiodivergent C(sp3)-H Amidation: Biocatalytic Asymmetric Synthesis of 1,2- and 1,3-Diamine Derivatives](https://www.biorxiv.org/content/10.64898/2026.11.17.767434v1)
*Chen, H.; Liu, H.; Zhao, L.-P. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.17.767434 v1 · relevance 0.06

- **In one sentence**: Directed evolution of the plant nonheme iron enzyme ACCO yields biocatalysts that perform enantioselective, regiodivergent C(sp3)-H amidation of N-(benzoyloxy)urea substrates to give cyclic ureas, precursors to 1,2- and 1,3-diamines.
- **In plain words**: Chemists want to add nitrogen-containing groups onto specific carbon-hydrogen bonds in organic molecules, and to do it with control over which hydrogen is replaced and which mirror-image form (enantiomer) results. This paper reports that a plant enzyme, 1-aminocyclopropane-1-carboxylic acid oxidase (ACCO), was reshaped by repeated rounds of laboratory evolution so it does this reaction on a range of carbon sites, producing cyclic ureas that can be converted into diamine building blocks. The authors also report that the evolved enzymes can be used at gram scale in whole cells.
- **Why it matters**: Selective, mirror-image-controlled C-H functionalization is hard to do with ordinary chemical catalysts, so an enzyme route that can switch between 1,2- and 1,3-diamine products from the same starting material is of interest to synthetic chemists. The text does not show how widely these methods will transfer to other molecules or to industrial use.
- **Background needed**: - C-H bond: a carbon-hydrogen bond; converting these directly into other bonds avoids extra synthesis steps.
- Nonheme iron enzyme: an iron-containing protein that is not built around the heme ring; it can activate oxygen-based reagents to break C-H bonds.
- Directed evolution: repeatedly mutating an enzyme and keeping the best variants, mimicking natural selection in the lab.
- Enantioselectivity: preferentially making one of two mirror-image molecular forms, which matters for drug-like compounds.
- Regiodivergent: the same starting material can be steered to different reaction sites by changing the catalyst.
- Hydrogen atom transfer (HAT): a step where a hydrogen atom moves from carbon to another species, leaving a carbon-centered radical (a reactive carbon with an unpaired electron).
- Diamine: a molecule with two amine (nitrogen) groups; cyclic ureas here are related protected forms.
- Turnover number: how many product molecules one enzyme molecule makes before it stops working. · level: research-level

<details><summary>Original abstract</summary>

Nonheme Fe enzyme-catalyzed asymmetric, site-selective C-H amidation remains underexplored. Here we report the repurposing and directed evolution of the plant-derived nonheme Fe enzyme 1-aminocyclopropane-1-carboxylic acid oxidase (ACCO) into a family of biocatalysts for highly regio- and enantioselective C(sp3)-H amidation. Engineered ACCO variants catalyzed the asymmetric synthesis of cyclic ureas from N-(benzoyloxy)urea substrates, which are readily prepared from aliphatic amines, through the activation of benzylic, allylic, propargylic, and unactivated aliphatic C(sp3)-H bonds, including enantioconvergent amidation of racemic tertiary C(sp3)-H substrates. Directed evolution further generated complementary enzymes that selectively promoted either 1,5- or 1,6-hydrogen atom transfer, enabling catalyst-controlled, regiodivergent enantioselective synthesis of both 1,2- and 1,3-diamine derivatives from common precursors. The evolved biocatalysts exhibited total turnover numbers of up to 4,500 and were readily applicable to gram-scale whole-cell biotransformations. Mechanistic investigations supported a stepwise mechanism involving a carbon-centered radical intermediate. Kinetic isotope effect and isotopically labeled substrate studies indicated C(sp3)-H bond cleavage as the rate-limiting step, while stereochemical analyses revealed that the overall enantioselectivity is determined by the C-N bond-forming radical rebound rather than hydrogen atom transfer. These results established nonheme Fe enzymes as a versatile platform for selective C-H amidation and further expanded the scope of new-to-nature nonheme Fe biocatalysis for asymmetric C-H functionalization.

</details>

### [Synthesis of Cellulose Nanofiber Hydrogel Beads from Typha angustifolia for the Immobilization of Protease](https://www.biorxiv.org/content/10.64898/2026.11.18.767499v1)
*Ameh, B. E.; Egwim, E. C.; Ossamulu, F. i.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.18.767499 v1 · relevance 0.05

- **In one sentence**: Cellulose nanofibers extracted from invasive Typha angustifolia are formed into aldehyde-modified, PVA-blended, glutaraldehyde-crosslinked hydrogel beads that covalently immobilize crude protease, raising its specific activity and shifting its thermal and pH optima.
- **In plain words**: Cattail-like water plants of the species Typha angustifolia spread aggressively and cause problems for wetlands and irrigation channels. This study turned their plant fiber into small, water-swollen gel beads that hold an enzyme (a protein that speeds up chemical reactions), and the researchers measured how well the enzyme still worked when attached.
- **Why it matters**: Reusing an invasive plant as a biodegradable support for industrial enzymes could add value to weed removal, and attaching enzymes to a solid support is a common way to make them easier to recover and reuse. The text reports only lab measurements on one enzyme preparation, so its practical value for industry is not yet shown.
- **Background needed**: - Cellulose: the main structural fiber in plant cell walls; cellulose nanofibers are very thin strands of it.
- Hydrogel: a soft, water-filled gel network; here, formed into beads.
- Immobilization: fixing an enzyme onto a solid carrier so it stays in place and can be reused.
- Protease: an enzyme that breaks down proteins.
- Specific activity: enzyme activity per milligram of protein (U/mg); higher means more active.
- Crosslinking with glutaraldehyde: chemically linking polymer chains together to strengthen the gel; aldehyde groups from periodate oxidation provide sites where the enzyme attaches.
- Optimum temperature and pH: the conditions where the enzyme works best; the paper reports these shifting upward for the immobilized form.
- Half-life: the time over which the enzyme keeps half its activity under operating conditions. · level: intermediate

<details><summary>Original abstract</summary>

Typha angustifolia, an invasive aquatic macrophyte, poses a persistent challenge to wetland and irrigation management, yet its cellulose-rich biomass represents an underexploited feedstock for value-added biomaterials. This study reports the synthesis of cellulose nanofiber (CNF) hydrogel beads from T. angustifolia and evaluates their performance as a support matrix for protease immobilization. Cellulose was isolated by chlorite delignification and alkaline treatment, oxidized with sodium periodate to introduce aldehyde functional groups, blended with polyvinyl alcohol (PVA), and crosslinked with glutaraldehyde to form hydrogel beads. The beads exhibited a high water-absorption capacity of 399.67 {plus minus} 0.53% and a mechanical strength of 1.27 MPa. Covalent immobilization of crude protease onto the beads increased specific activity nearly threefold, from 24.56 {plus minus} 0.39 U/mg for the free enzyme to 59.20 {plus minus} 1.06 U/mg for the immobilized enzyme, corresponding to a loading efficiency of 50.61%. The immobilized enzyme also displayed broadened thermal and pH optima, shifting from 40 {degree sign}C to 50 {degree sign}C and from pH 8.0 to 9.0, respectively, and an extended operational half-life from 4.40 h to 11.37 h. These findings support the valorization of invasive Typha biomass into a robust, biodegradable support system with potential application in industrial biocatalysis.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Koopman Analysis Reveals Collective Modes Governing Cellular Dynamics](https://www.biorxiv.org/content/10.64898/2026.11.18.767672v1)
*Dutta, S.; Yu, W.; Zheng, Z. et al.* · `biophysics` · bioRxiv doi:10.64898/2026.11.18.767672 v1 · relevance 0.10

- **In one sentence**: The paper applies Koopman operator theory to whole-cell dynamical models to identify collective, slow and fast modes that govern cell-cycle and cell-state transition dynamics and relate them to gene regulatory structure and cell-cycle processes.
- **In plain words**: Living cells change their behavior over time in complicated, non-linear ways that are hard to analyze with standard tools. This paper uses a mathematical method called Koopman analysis, which rewrites such a system so it behaves linearly across its whole range, and applies it to computer models of whole cells. The authors report that the resulting patterns of coordinated gene behavior ("modes") map onto processes such as mitosis, the spindle checkpoint, and DNA replication and repair.
- **Why it matters**: The work offers a way to describe a very high-dimensional cell model with a few dominant slow modes, which may help simplify models of cell division and cell-state change. Its broader value depends on how well these modes hold up beyond the models studied, and the text alone does not show that.
- **Background needed**: - Nonlinear system: one where outputs do not change in proportion to inputs, so simple prediction fails.
- Linearization: approximating or rewriting a system so it can be analyzed with linear math; most methods only work near a single point, whereas Koopman theory aims to work globally.
- Koopman operator: a mathematical tool that tracks how measurements of a system evolve, turning nonlinear motion into linear motion in a larger function space.
- Normal modes: independent patterns of collective motion in physical systems such as vibrating molecules or crystals.
- Slow manifold: a low-dimensional space where a system's long-term behavior settles.
- Gene regulatory network: the web of genes that switch each other on or off.
- Cell cycle: the sequence of stages a cell goes through to divide, including mitosis and DNA replication. · level: research-level

<details><summary>Original abstract</summary>

Living systems are complex nonlinear systems that operate far from thermodynamic equilibrium, and this nonlinearity makes their dynamics difficult to analyze. Several linearization techniques have been developed to address this problem, but most are local. Koopman operator theory is a powerful alternative that linearizes a system globally. Here we show that it not only achieves global linearization but also reveals collective modes that govern the dynamics of complex, out-of-equilibrium nonlinear systems. Applying the approach to whole-cell dynamical models, we find that these collective modes have physical and biological significance and relate to distinct processes in the cell cycle and in cell-state transitions. Collective and normal modes are widespread in many-body systems, particularly in condensed matter (e.g., magnons, phonons, hydrodynamic modes) and in macromolecular dynamics (e.g., normal mode analysis). By demonstrating that such modes also exist in cell-state transition dynamics, and in non-equilibrium nonlinear systems more generally, we offer a new theoretical-physics perspective on these systems. The collective modes separate into slow and fast modes. Long-term dynamics are governed by a few dominant slow modes that form a slow manifold of much lower dimension than the original state space. Thus, although the cell is a very high-dimensional system, its cell-cycle dynamics ultimately reduce to a low-dimensional space. Each mode comprises the coordinated behavior of groups of genes and reflects the structure of the underlying gene regulatory network. The modes can also be decomposed into terms that behave like damped harmonic oscillators, drawing an analogy between the modes of a nonlinear system and the normal modes of many-body systems. Finally, our analysis suggests that the dominant modes are closely associated with biological processes in the cell cycle, including mitosis, spindle checkpoint signaling, and DNA replication and repair.

</details>

### [Microbiome complexity shapes host transcriptional networks across the ileum-liver axis](https://www.biorxiv.org/content/10.64898/2026.11.16.767119v1)
*Halkhoree, A. C.; Grannell, A.; Pearson, C. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.16.767119 v1 · relevance 0.09

- **In one sentence**: A transcriptomic survey of mouse terminal ileum across germ-free, defined 12-strain microbiota (MM12), and specific-pathogen-free conditions, examining how microbiome complexity shapes host gene co-expression networks along the ileum-liver axis.
- **In plain words**: This study asks how the community of microbes living in the gut changes the way genes switch on and off in the lower part of the small intestine, the ileum, and possibly in the liver connected to it. The researchers compared mice with no microbes, mice with a simple set of 12 known bacterial strains, and mice with a normal, full microbial community. The text provided describes the setup and goal; it does not include the results.
- **Why it matters**: Gut microbes are known to affect nutrient absorption, bile acid handling and immunity, and the gut and liver are linked, so how microbial complexity tunes gene activity in the ileum may matter for understanding gut-liver health. The excerpt gives only the aims and design, so the size or meaning of any effect cannot be judged from it.
- **Background needed**: - Transcriptome: the full set of gene activity readings in a tissue sample, used to see which genes are active.
- Co-expression network: a map of genes that rise and fall together, suggesting they work in the same process.
- Germ-free (GF) mice: raised without any microbes, used as a baseline to see what microbes do.
- MM12 (Oligo-Mouse-Microbiota-12): mice colonised with a defined set of 12 bacterial strains, a simplified community.
- Specific pathogen free (SPF): mice with a standard, controlled microbiome that excludes known pathogens.
- Ileum: the final section of the small intestine, where nutrients and bile acids are absorbed.
- Bile acids: digestive molecules made by the liver and modified by gut bacteria. · level: research-level

<details><summary>Original abstract</summary>

The microbiome plays an increasingly recognised role in development, metabolism and immunity across all segments of the small and large intestine, as well as more distant organs such as the liver. In the terminal ileum - a key site of nutrient absorption - the presence of microbes dictates the development of secondary lymphoid structures (Peyers patches), mediates bile acid metabolism, and impacts absorption. In part, coordinated regulatory networks in the gut impact liver function and immunity through gut-liver connectivity and the movement of immune cells and bioactive small molecules that includes bile acids and other bacterial metabolites. We aimed to examine the extent of microbiome involvement in ileal transcription, where subtle changes in co-expression networks can be tuned by microbiome diversity, composition and function. We surveyed ileal transcriptomes across mouse models which vary in microbiome complexity ranging from germ-free (GF, n = 15), the Oligo-Mouse-Microbiota-12 (MM12, n = 15), and specific pathogen free (SPF, n = 15).

</details>

## Neuroscience

### [Sex-dependent gating of astrocyte-driven nociceptive plasticity](https://www.biorxiv.org/content/10.64898/2026.11.18.767473v1)
*Klinger, L.; Uhrik, L.; Ravagnan, E. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.18.767473 v1 · relevance 0.08

- **In one sentence**: In rats, chemogenetic activation of distinct spinal astrocyte GPCR pathways produced sex-dependent nociceptive synaptic plasticity, gated by gonadal hormones and perineuronal extracellular matrix.
- **In plain words**: This study looks at why pain signaling in the spinal cord may respond differently in males and females. Researchers used genetically engineered control of support cells called astrocytes in rats and found that, in males, activating certain pathways weakened or strengthened pain-relay connections, while in females the same activation did not produce a measurable change. Females still developed mechanical hypersensitivity similar to males, so changes in connection strength and pain behavior were not tied together in a simple way.
- **Why it matters**: It suggests that sex, sex hormones, and the surrounding scaffolding of the nerve tissue (the extracellular matrix) can change whether spinal circuits undergo astrocyte-driven plasticity, which may matter for sex differences in pain research. The text does not establish how these findings translate to human pain, so that link remains unclear.
- **Background needed**: - Nociception: the nervous system's detection and signaling of potentially harmful stimuli, which underlies pain.
- Synaptic plasticity: long-lasting strengthening or weakening of connections between nerve cells; a proposed basis for learning and for pain sensitization.
- Astrocytes: star-shaped glial (support) cells in the nervous system that influence nearby synapses.
- GPCRs (G-protein-coupled receptors): cell-surface receptors that relay signals inside cells; Gq is one such signaling pathway.
- Chemogenetics: a method using engineered receptors switched on by a designed drug, letting researchers activate specific cells on demand.
- Gonadectomy / ovariectomy: surgical removal of the gonads (testes or ovaries), used to study hormone effects; testosterone treatment tests hormone replacement.
- Perineuronal nets: specialized extracellular matrix structures wrapping some neurons, which can limit plasticity.
- Mechanical hypersensitivity: increased pain response to touch or pressure, measured behaviorally in animals. · level: research-level

<details><summary>Original abstract</summary>

Sex differences in pain are well established, yet how nociceptive processing is differentially regulated across sexes remains poorly understood. Here, we show that spinal astrocytes provide pathway-specific control of acute nociceptive synaptic plasticity in rats. Chemogenetic activation of distinct astrocytic G-protein-coupled receptor pathways induced synaptic depression or potentiation at spinal nociceptive synapses in males, but failed to evoke detectable plasticity in females. Despite this lack of astrocyte-induced synaptic plasticity, females developed mechanical hypersensitivity comparable to males, revealing a dissociation between synaptic plasticity and pain-related behavior. Gonadectomy prevented astrocyte-induced plasticity in males, whereas testosterone treatment enabled Gq-dependent synaptic depression in ovariectomized females. Females exhibited more prominent perineuronal net labeling, and enzymatic degradation of extracellular matrix (ECM) components enabled Gq-dependent synaptic depression in females. Together, these findings identify hormonal status and ECM organization as important determinants of the susceptibility of spinal nociceptive circuits to astrocyte-driven synaptic plasticity.

</details>

### [Common organization of collective dynamics across divergent self-organized neural architectures](https://www.biorxiv.org/content/10.64898/2026.11.18.767733v1)
*Zhao, Z.; Yang, L.; Nemenman, I. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.18.767733 v1 · relevance 0.07

- **In one sentence**: Using brain organoids and cluster-and-cable neuronal networks, the authors show that burst-like population activity in both self-organized architectures comprises several collective patterns, with recurrent sequences capturing only part of a conserved, broader organization that persists under increased network activity.
- **In plain words**: Researchers grew two different kinds of lab-made neural tissue: layered, cortex-like organoids and networks of cell clusters linked by long fibre-like cables. They recorded the group activity of the cells and found that bursts of firing in both tissues were made up of several repeating group patterns, not one fixed script. Although the specific patterns differed between the two tissues, their overall organization was similar, and it did not change when the networks were pushed to be more active with drugs.
- **Why it matters**: It suggests that the way neurons coordinate as a group may follow shared principles even when the tissue's wiring is built very differently, which is useful for thinking about how brain-like networks organize themselves. The text does not establish links to specific brain function or disease, so any such connection remains uncertain.
- **Background needed**: - Brain organoids: small 3D tissue cultures grown from stem cells that partly mimic brain tissue.
- Self-organization: cells build their own structure and connections without being explicitly designed.
- Bursts: brief, synchronized waves of firing across many neurons.
- Activation sequences: neurons that tend to fire in a reproducible order.
- Graded participation: neurons join such sequences to different degrees rather than all-or-nothing.
- Pharmacological manipulation: using drugs to change how active the network is. · level: research-level

<details><summary>Original abstract</summary>

Brain organoids and other model neuronal networks build synaptic circuits through self-organization, and different protocols yield markedly different architectures, letting us test how collective dynamics depend on large-scale organization. We compared organoids of layered cortical-like structure against networks of cell-body clusters joined by axonal cables, quantifying the reproducible patterns of population activity in each. Bursts occurred in both architectures and comprised several collective patterns in each, so no single recurring template describes them. Recurrent activation sequences capture only part of this organization, sequence participation is graded, and neurons that rarely join a sequence still contribute to the shared dynamics. The patterns also pick out overlapping neuronal groups with propagation-like spatial order. Although the patterns differed between tissue models, their organization was conserved, and remained unchanged under pharmacological increases in network activity. Recurrent sequences therefore represent one manifestation of a broader collective organization that emerges across distinct self-organized neural architectures.

</details>

## Genetics and genomics

### [Single-cell study of the FCG rat model and cross-species comparison reveal stronger gene regulation by sex chromosome complement in the medial septum](https://www.biorxiv.org/content/10.64898/2026.11.19.767942v1)
*Turnbill, V.; Zhang, G.; Harris, E. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767942 v1 · relevance 0.09

- **In one sentence**: Single-cell transcriptomic study of the medial septum in a new four-core-genotype (FCG) rat model, compared with the FCG mouse, finding that sex chromosome complement (XX vs. XY) dominates sex-biased gene regulation, with gonadal effects acting in concert.
- **In plain words**: Men and women differ in many brain-related conditions, but it is hard to tell whether this comes from sex chromosomes or from sex hormones made by the gonads. This study used a specially bred rat model that separates these two sources and measured gene activity in individual cell types of the medial septum, a brain region involved in anxiety, memory, and related functions. The authors report that the chromosome makeup had a stronger effect on gene activity than the gonads, and that this pattern was broadly shared with a mouse version of the model, even though the specific genes differed between species.
- **Why it matters**: It challenges the common view that gonadal hormones mainly drive sex differences in the brain, which matters for how sex differences are studied in brain disease. The authors link the sex-biased genes and networks to conditions such as anxiety, Alzheimer's disease, epilepsy, and schizophrenia, but the text does not show whether these links translate into treatments.
- **Background needed**: - Sex chromosomes: typically XX (female) or XY (male); genes on them can act differently from hormones.
- Gonads: ovaries or testes, which produce sex hormones.
- Four core genotypes (FCG) model: animals whose sex chromosomes and gonads are varied independently, so the two effects can be separated.
- Medial septum: a small brain region linked to anxiety, memory, and behavior.
- Single-cell gene expression analysis: measuring which genes are active in each individual cell, then grouping cells by type.
- Gene regulatory networks and transcription factors: sets of genes controlled together by shared switch-like proteins.
- Cross-species comparison: checking whether a finding in one animal also holds in another. · level: research-level

<details><summary>Original abstract</summary>

Sex differences are prominent in neuropsychiatric, neurological, and neurodegenerative conditions. While both gonads (ovaries vs. testes) and sex chromosome complement (SCC; XX vs. XY) contribute to sex differences, these effects are hard to differentiate in humans and gonadal contributions have been considered dominant in the brain. The four core genotypes (FCG) mouse model distinguishes between SCC and gonadal effects but whether findings are conserved across species remains unclear. Here, we present the first application of the novel FCG-derived rat model to explore cell-type-specific sex differences in the medial septum (MS), which shows robust structural sex differences, and convergence/divergence between species. Differential gene expression, pathway, transcription factor, and gene regulatory network analyses show dominant SCC effects and concordant gonadal effects on gene and network regulation in rat MS cell types. Comparison between the FCG rat and mouse models find convergence across species on the dominance of the SCC in regulating gene expression in concert with gonadal effects in the MS, despite divergence in individual sex-biased genes. In both species, the sex-biased, cell-type-specific MS genes and networks are associated with diverse diseases relevant to MS functions, such as anxiety, Alzheimers Disease, epilepsy, and schizophrenia, that can be targeted by proposed therapeutic candidates. Our cross-species investigation identifies a conserved dominance of SCC effects in sex-biased gene expression in the MS, thereby challenging the classical gonad-centric view of sexual differentiation in the brain and highlighting the MS as an important region for the study of sex differences driven by the sex chromosome complement.

</details>

### [A genetic toolkit of visible mutants for Caenorhabditis briggsae](https://www.biorxiv.org/content/10.64898/2026.11.19.767928v1)
*Johnsen, R.; Mah, A.; Thillainathan, B. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.19.767928 v1 · relevance 0.08

- **In one sentence**: This paper reports 183 visible mutants of the nematode Caenorhabditis briggsae, mapped to six linkage groups, with 23 loci matched to C. elegans orthologs and several genes confirmed by rescue or sequence evidence.
- **In plain words**: Researchers studying a small roundworm, Caenorhabditis briggsae, built a collection of 183 mutant strains that show easy-to-spot changes in appearance or behavior, such as body shape or movement. They worked out where many of these mutations sit on the worm's chromosomes, using crosses between strains and genetic markers. The collection and its supporting data are offered as a shared tool for comparing this worm with its close relative C. elegans.
- **Why it matters**: Visible mutants are the basic tools geneticists use to link a gene to a trait, so a documented collection makes a less-studied relative of a major model organism easier to work with. The paper also corrects some earlier gene assignments and ties several genes to their known counterparts in C. elegans, which may help comparative studies of how genes evolve; the text does not describe broader applications.
- **Background needed**: - Caenorhabditis elegans is a tiny roundworm that is a major model in biology; C. briggsae is a closely related species used for comparison.
- A "mutant" is an organism with a changed gene, here producing a visible change in shape, movement or similar traits.
- EMS is a chemical that randomly causes mutations in the worm's DNA; screens look for the resulting visible changes.
- "Linkage groups" are sets of genes that sit on the same chromosome and tend to be inherited together; mapping them uses crosses and genetic markers.
- "Complementation tests" check whether two mutations affect the same gene; "orthologs" are genes in different species that descend from a common ancestor.
- Transgene rescue means inserting a working copy of a gene to see if it reverses the mutant trait, which confirms the gene's identity. · level: research-level

<details><summary>Original abstract</summary>

Caenorhabditis briggsae is a widely used model for comparative genetic studies involving C. elegans. Genetic analysis in C. briggsae depends on mutations with clear, easily recognizable phenotypes, yet most mutants reported so far have been mentioned only as names and linkage groups, without underlying experimental data. This study reports 183 C. briggsae mutants belonging to 11 phenotypic classes, which represent the most comprehensive collection to date. Almost all mutants were recovered in EMS screens of the reference strain AF16. Our analysis revealed that 121 mutations define 55 loci and 62 remain unassigned. A combination of complementation tests, linkage tests, two- and three-factor crosses, and polymorphism-based mappings helped place 51 loci and 15 further mutations to the six linkage groups. We report the supporting data, map distances, linkage groups, and corrections to several earlier assignments. Twenty-three loci correspond to molecularly identified orthologs of C. elegans genes, including six for which we report genetic, rescue, or sequence evidence here. The levamisole-resistant mutants fall into at least three complementation groups, two of which correspond to Cbr-unc-38 and Cbr-unc-29 (levamisole-sensitive nicotinic acetylcholine receptor a and non-a subunit, respectively). Transgene rescue experiments identify Cbr-dpy-1 (mucin-like), Cbr-sma-6 (TGFb type receptor kinase), and Cbr-unc-4 (homeodomain transcription factor), genes that have long been in use as genetic markers. In all cases, molecularly identified genes are located on the same chromosome as their C. elegans orthologs, although gene order within chromosomes differs. The strains, map, and underlying data provide a resource for genetic and comparative studies in Caenorhabditis nematodes.

</details>

## Cell and molecular biology

### [Palmitic acid overload does not promote full-blown dysfunction in SGBS adipocytes which is reflected in their secretome](https://www.biorxiv.org/content/10.64898/2026.11.19.767488v1)
*Angelini, S.; Stifani, G.; La Runa, G. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.19.767488 v1 · relevance 0.10

- **In one sentence**: In cultured SGBS human adipocytes, a 96-hour palmitic acid exposure raised MCP-1, IL-6, IL-8 and adiponectin signals and increased lipid droplets and cell size, but did not impair insulin signalling in the cells or in co-cultured myotubes.
- **In plain words**: Eating too much saturated fat is linked to obesity and poor metabolic health, but it is unclear how much it harms the fat cells themselves. The researchers grew a human fat-cell line (SGBS) in palmitic acid, a common saturated fat, for four days and checked the cells and the chemical messages they released. The fat cells stored more fat and grew larger, and released more of some inflammation-related signals, but they did not lose their normal response to insulin, and the released messages did not block insulin signalling in muscle cells.
- **Why it matters**: It suggests that a saturated fat overload alone may not be enough to make human fat cells fully dysfunctional in this model, which is relevant to how obesity-related insulin resistance develops. The text does not show how this maps onto whole-body or in-person metabolism, and the model lacks the stromal vascular fraction, so the findings are limited to this cell system.
- **Background needed**: - Adipocytes: fat-storing cells; their behaviour in a dish is studied as a model for body fat.
- SGBS cells: a human pre-fat cell line used in laboratory studies.
- Palmitic acid (PA): a common saturated fat; bovine serum albumin (BSA) was used as the control carrier.
- Insulin signalling: a chain of molecular steps (including Akt and AS160 phosphorylation) that lets cells take up sugar; impaired signalling is a hallmark of insulin resistance.
- NF-kB and cytokines (MCP-1, IL-6, IL-8): inflammation pathways and signalling proteins; adiponectin is a fat-derived hormone linked to insulin sensitivity.
- Secretome: the full set of molecules a cell releases into its surroundings.
- Myotubes: immature muscle cells grown in a dish, used to test insulin response.
- Stromal vascular fraction: other cell types found in fat tissue, absent in this model. · level: research-level

<details><summary>Original abstract</summary>

Background: Energy excess, and particularly long-chain saturated fatty acid (SFA) overload, are instrumental in promoting obesity and hampering metabolic health. However, SFA contribution to human adipocyte metabolic and endocrine dysfunction remains elusive. Nonetheless, we have already provided evidence that a 48-hour palmitic acid (PA) exposure is not sufficient to hamper Simpson-Golabi Behmel Syndrome (SGBS) adipocytes insulin signalling. Objective: This study aims at evaluating whether a 96-hour exposure to PA is able to disrupt SGBS adipocyte metabolic health and induce the release of a secretome capable of hampering insulin signalling in skeletal muscle cells. Methods: SGBS adipocytes were treated with either 1000 uM PA or bovine serum albumin (BSA) for 96 hours followed by the assessment of the NFkB signalling and the expression of genes associate with inflammation and adipocyte metabolic stress. Furthermore, adipocytes were labelled with BODIPY and lipid droplet as well as cell size semi-quantified using ImageJ. Insulin-induced phosphorylation of Akt and Akt substrate of 160 kDa (AS160) was assessed by Western Blot. The effect of PA on SGBS secretome was assessed by both ELISA as well as MILLIPLEX. Finally, human immortalised myotubes were co-cultured with BSA or PA-treated SGBS adipocytes for 24 hours followed by the assessment of insulin signalling at the Akt level. Results: PA did not activate the NFkB signalling pathway, but induced the expression of MCP-1 while tending to upregulate IL-6 mRNA levels. Despite 96-hour PA exposure leading to an increase in lipid droplet and cell size, this was not coupled with an impairment in insulin signalling. Nevertheless, this SFA promoted an increase in IL-6 and IL-8 secretion while tending to enhance the release of adiponectin by SGBS adipocytes. Finally, the secretome from PA-treated SGBS adipocyte did not impair insulin-induced phosphorylation of Akt relative to controls in myotubes. Conclusions: Thus, in the absence of the stromal vascular fraction, direct exposure of SGBS adipocytes to PA overload is not sufficient to elicit overt dysfunction. The absence of full-blown adipocyte dysfunction is reflected in the secretome of these cells which failed to disrupt skeletal muscle insulin signalling.

</details>

### [Extra-sheath transplantation of human retinal organoids (hROs): effects on visual recovery and retinal repair following optic nerve injury](https://www.biorxiv.org/content/10.64898/2026.11.18.767615v1)
*Luo, Y.; Chen, X.; Kang, J. et al.* · `developmental biology` · bioRxiv doi:10.64898/2026.11.18.767615 v1 · relevance 0.09

- **In one sentence**: In C57 mice with optic nerve crush, transplanting day-30 human retinal organoids at the injury site was associated with better optic-disc and ganglion cell layer preservation, higher flash VEP P2 amplitudes, and improved optomotor responses, though circuit integration was not demonstrated.
- **In plain words**: This study looks at whether small lab-grown balls of human retina cells, placed where the optic nerve was crushed in mice, can help protect the nerve cells that carry vision from the eye to the brain. The mice that received the grafts kept more of the retina's nerve-cell layer and showed stronger brain responses to light and better head-turning responses to moving stripes than mice with the crush alone. The authors state that they did not prove the transplanted tissue actually wired into the visual circuit.
- **Why it matters**: Optic nerve injury can cause lasting vision loss with few treatments, so a strategy that protects nerve cells and tracks with visual function is of clear interest. The text, however, is a single mouse study, and the authors note that graft tracing, synaptic validation and prespecified electrophysiology are still needed before any claim about donor-derived circuit reconstruction.
- **Background needed**: - Retinal ganglion cells: the eye's output neurons whose long fibers form the optic nerve to the brain.
- Optic nerve crush: an experimental injury in mice that damages these fibers and mimics traumatic nerve injury.
- Retinal organoids: three-dimensional tissue clusters grown from stem cells that develop retina-like layers.
- Microelectrode array: a flat dish of tiny electrodes used to record spontaneous electrical activity from cells.
- Immunostaining markers: antibody labels for specific cell types (RBPMS for ganglion cells, TUJ1 for neurites, IBA1 for microglia, immune cells of the nervous system).
- Electroretinogram (ERG) and flash visual evoked potential (VEP): recordings of electrical responses from the retina and the visual areas of the brain to light flashes; the b-wave reflects mainly inner retina activity, while P2 reflects signals reaching the visual cortex.
- Optomotor response: a reflex where an animal turns its head to follow moving stripes, used to measure spatial vision.
- Light-dark box: a test based on the mouse's preference for dark spaces; it is a non-specific measure of behavior. · level: research-level

<details><summary>Original abstract</summary>

Traumatic optic nerve injury interrupts retinal ganglion cell output and can produce permanent visual disability, yet a therapeutic strategy that couples retinal protection with recovery of visual-pathway activity remains unavailable. Here, we evaluated human retinal organoid transplantation at the site of optic nerve crush in C57 mice. Human retinal organoids derived from embryonic stem cells were used at day 30 and showed retinal-lineage immunoreactivity together with spontaneous microelectrode-array activity. Across post-surgical days 7, 14, and 28, transplantation was associated with preservation of optic-disc appearance and ganglion cell layer thickness. The structural benefit became statistically distinguishable from the crush group at day 28 and remained incomplete relative to the uninjured or sham group. Serial RBPMS and TUJ1 immunostaining further supported attenuation of retinal ganglion cell body and neurite loss, while IBA1 staining indicated an altered microglial response. Full-field electroretinographic b-wave responses showed no detectable between-group differences, arguing against a major outer-retinal effect. In contrast, flash visual evoked potential P2 amplitude was higher in transplanted than in crush-only mice at all measured time points, consistent with improved visual-pathway responsiveness. Transplant recipients also showed enhanced optomotor responses across tested spatial-frequency and contrast conditions. Light-dark behavior shifted toward greater dark-compartment occupancy and activity, although this assay remains non-specific for visual recovery. Together, these findings support a model in which hROs transplantation at an optic nerve injury site promotes multi-level functional preservation after optic nerve crush. Definitive evidence for donor-derived circuit reconstruction will require graft tracing, synaptic validation, and prespecified electrophysiologic analyses.

</details>

## Immunology and microbiology

### [Spatiotemporal Dynamics and Environmental Drivers of Maize Microbiome Structure across Diverse Agroecosystems in Georgia, USA](https://www.biorxiv.org/content/10.64898/2026.11.19.767978v1)
*AMO, A. E.; Yang, C.; Johnson, M. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.19.767978 v1 · relevance 0.11

- **In one sentence**: A statewide field survey of 35 Georgia maize fields at two growth stages, using 16S rRNA amplicon sequencing, compares bacterial communities across soil, rhizosphere, root interior and stalk interior and links them to predicted functions, network structure and environmental variables.
- **In plain words**: Researchers looked at the communities of bacteria living in and around corn plants grown across Georgia. They collected samples from the soil, the area right around the roots, inside the roots, and inside the stalks, at an early and a later stage of growth. The study reports that soil and root-zone bacteria were more varied and more spatially structured, while the bacteria inside roots and stalks changed noticeably as the plants grew.
- **Why it matters**: Understanding how these plant-associated microbes shift with plant development and local conditions may eventually inform crop management, but the text presents this as ecological insight rather than a direct farming tool. The link to practical crop outcomes is not established in the text.
- **Background needed**: - Microbiome: the full community of microorganisms (mostly bacteria here) living in a given habitat.
- 16S rRNA amplicon sequencing: a method that reads a standard bacterial gene segment to identify and count bacterial types; ASVs are the resulting distinct sequence variants.
- Compartments: soil, rhizosphere (soil right next to roots), root interior and stalk interior.
- Growing degree days (GDD): a measure of accumulated warmth used to track plant development stage.
- Alpha diversity: variety within one sample; beta diversity: how different communities are from each other.
- PICRUSt2: a tool that predicts likely metabolic functions from bacterial gene-marker data, so predictions are inferred, not directly measured.
- Keystone taxa: groups that have an outsized influence on a community's network of interactions.
- Modularity and connectivity: measures of how a network of co-occurring microbes is divided into clusters and how densely linked it is. · level: research-level

<details><summary>Original abstract</summary>

The understanding of how microbial communities differ across soils, environments, plant tissues, and developmental stages is key to the improvement of crop productivity and resilience. Here, we conducted a statewide survey of maize (Zea mays L.) microbiomes across 35 fields at 16 locations in Georgia, USA, sampling soil, rhizosphere, root interior, and stalk interior at two developmental stages (600 and 1400 growing degree days, GDD). More than 38000 ASVs were produced after amplicon sequencing of 16S rRNA genes. The phyla shown to be dominant are Proteobacteria, Actinobacteriota, Chloroflexi, Planctomycetota, and Acidobacteriota. Based on alpha and beta diversity analyses, the below-ground compartments (soil and rhizosphere) revealed higher diversity and stronger spatial structuring when compared to the above-ground sample types, whereas root and stalk interior microbiomes revealed marked shifts across growth stages. Amino acid metabolism, secondary metabolite biosynthesis, and energy-related pathways predictions (via PICRUSt2) show stage-dependent enrichment. Network analyses show persistent keystone taxa (Proteobacteria and Actinobacteriota) mediating microbial stability, coupled with an increase in modularity and connectivity as we move from early to late growth stages. Some environmental variables, such as temperature, humidity, soil potassium, and soil sodium, showed significant correlation with microbial diversity indicative of a compartment-specific environmental sensitivity. Collectively, our results show that in maize, microbial community composition, interaction, and potential functionality are both impacted by developmental stages and environmental heterogeneity. This study provides a fundamental framework for understanding the microbiome dynamics in field-grown maize across various agroecological conditions. It equally provides ecological insights relevant to microbiome-informed crop management.

</details>

### [Spatial Transcriptomics Reveals Host Gene Expression Patterns Associated with Naegleria fowleri Infection in the Murine Brain](https://www.biorxiv.org/content/10.64898/2026.11.18.767516v1)
*Dainis, J.; Bailey, M.; Sievert, M. A. C. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.18.767516 v1 · relevance 0.10

- **In one sentence**: Spatially resolved transcriptomics of mouse brains at several time points after intranasal Naegleria fowleri inoculation maps region-specific host gene expression, including inflammatory and immune-cell signatures.
- **In plain words**: This paper looks at a rare and almost always fatal brain infection caused by a free-living amoeba that enters through the nose. The researchers infected mice, then measured which genes were switched on in different parts of their brains at several points in time. They found strong inflammatory gene activity that differed by brain region and by stage of infection, including in areas where no amoebae were detected.
- **Why it matters**: The disease kills more than 97% of those infected, and little is known about where and when the brain's immune response develops. The map of gene activity across brain regions and time offers a starting point for later work on the cells and molecules driving brain inflammation, though the text itself does not show any direct treatment implications.
- **Background needed**: - Naegleria fowleri: a free-living amoeba found in warm fresh water that can enter the body through the nose and travel to the brain.
- Primary amoebic meningoencephalitis (PAM): the brain and lining infection it causes; mortality is above 97% per the text.
- Intranasal inoculation: experimental infection of mice by dropping the organism into the nose.
- Transcriptomics: measuring which genes are active (their RNA output) in a tissue.
- Spatial transcriptomics: gene activity measured while keeping track of where in the tissue each signal came from.
- Neuroinflammation: inflammation within the brain, involving immune cells such as macrophages, neutrophils and natural killer T cells.
- Cell-type signatures: patterns of gene activity that suggest which cell types are present, computed from the data rather than directly observed. · level: research-level

<details><summary>Original abstract</summary>

Primary Amoebic Meningoencephalitis (PAM), caused by the free-living amoebae Naegleria fowleri, is a devastating disease with a mortality rate exceeding 97%. Despite its severity, the spatial and temporal characteristics of the host immune response to infection within the brain remain poorly understood. Here, we used spatially resolved transcriptomic profiling to characterize region-specific gene expression patterns in brain tissue collected at multiple time points following intranasal inoculation of N. fowleri in mice. Our analysis revealed pronounced pro-inflammatory transcriptional signatures that varied across brain regions and over the course of infection. Cell type-associated gene expression profiles suggested the involvement of several immune cell populations, including macrophages, neutrophils, and natural killer T cells, alongside transcriptional changes associated with neural cell populations. Notably, inflammatory transcriptional signatures also were detected in brain regions without detectable amoebae, indicating that host responses extend beyond regions of apparent parasite localization. Collectively, these findings provide a spatial and temporal characterization of the host transcriptional response during experimental PAM, highlighting inflammatory gene expression signatures and putative immune and neural cell populations associated with disease progression. This study provides a foundation for future investigations into the cellular and molecular processes underlying neuroinflammation during N. fowleri infection.

</details>

## Cancer biology

### [Media matters: A resource for understanding the determinants of migratory potential of malignant and non-malignant cells](https://www.biorxiv.org/content/10.64898/2026.11.18.767665v1)
*Kim, B.; Lopez, A.; Osuna, M. F. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.18.767665 v1 · relevance 0.07

- **In one sentence**: A high-throughput wound-healing/invasion phenotypic screen of over 60 malignant and non-malignant epithelial cell lines (pancreas, colon, skin, breast, prostate, lung) that links migration to glycolysis, oxidative phosphorylation, and culture media conditions.
- **In plain words**: Cells that move are central both to healing a wound and to cancer spreading through the body. This study tested more than 60 normal and cancerous cell lines from several organs to see how fast each one moves and invades, and how that depends on their energy supply and the nutrients in their growth liquid. Surprisingly, normal lung, skin and pancreas cells often moved faster than their cancer counterparts.
- **Why it matters**: The work offers a public-style reference of migration data across many cell types and suggests that blocking energy pathways could affect normal and cancer cells differently, which may matter for drugs aimed at stopping metastasis or at healing-related diseases. The text does not show that any of these findings lead to a treatment, so the translational value remains to be tested.
- **Background needed**: - Migration/invasion assays: a scratch-closing test in which cells in a dish fill a gap, measured at high throughput.
- Metastasis: cancer cells leaving the original tumour and forming new tumours elsewhere.
- Migrastatic therapy: a drug aimed at slowing cell movement rather than killing cells.
- Glycolysis and oxidative phosphorylation: two ways cells produce energy from sugar, one without oxygen and one using mitochondria.
- Serum and calcium: components of growth media; the study varied them to mimic lower-nutrient conditions.
- In vivo: experiments in living animals; here they tested metastatic spread for lung and pancreatic cancer cells. · level: intermediate

<details><summary>Original abstract</summary>

Cell mobility is critical for homeostatic processes such as wound repair and diseases like cancer metastasis. While the advent of migrastatic and antimetastatic therapies has promise, the identification and translation of pathways important for migratory plasticity into druggable targets approved in clinical trials are considerably lacking. To better understand why, we developed an unbiased high-throughput wound-healing/invasion assay to screen for the migratory potential of >60 non-malignant and malignant cell lines derived from the pancreas, colon, skin, breast, prostate, and lung. The goal of this phenotypic screen was to provide a resource of migration/invasion potential and insight into the differential properties not only between malignant and non-malignant cells but also the various carcinomas. Surprisingly, we found non-malignant epithelial cells of the lung, skin, and pancreas migrated/invaded faster than their malignant counterparts. We observed perturbation of glucose metabolism, via inhibition of glycolysis, restricted the migration of non-malignant but not cancer cells, whereas inhibition of oxidative phosphorylation limited the mobility of malignant more than normal cells of the lung, skin, and pancreas. Short-term acclimation of cancer cells in low-nutrient media, containing low/no serum, low calcium, and physiological concentrations of glucose, increased in vitro migration/invasion and in vivo metastatic potential of lung but not pancreatic carcinomas. Phenotypic and metabolic screens presented here could identify prospective therapeutics not only for cancer metastasis, but also diseases driven by the dysregulation of wound-healing/regeneration.

</details>

### [A KRASG12D-based organoid model for early oncogenic transformation of the mammary epithelium](https://www.biorxiv.org/content/10.64898/2026.11.17.766834v1)
*Jones, D. J.; Rao, L. E.; West, J. J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.17.766834 v1 · relevance 0.07

- **In one sentence**: A mouse mammary epithelial organoid model in which Cre-induced KRASG12D expression produces neoplastic, lumen-less growth, competition between mutant and wild-type cells, and reduced apoptosis.
- **In plain words**: Cancer often starts with a single cell gaining a harmful mutation, and that early stage is hard to watch in living tissue. The authors grew small three-dimensional balls of healthy mouse breast cells (organoids) and switched on a cancer-linked mutation, KRAS G12D, in some of them. The mutant organoids grew abnormally without forming the normal hollow central cavity, and mutant cells gained ground over normal cells grown alongside them.
- **Why it matters**: The text suggests a lab system for watching the very first steps of tumor formation, which is hard to study directly, and the authors propose it could support prevention and drug testing work. Its usefulness for those goals is untested in this text, so it should be read as a proposed platform rather than a demonstrated one.
- **Background needed**: - Organoids: small, lab-grown 3D clusters of cells that mimic parts of an organ.
- KRAS: a gene that normally helps control cell growth; the G12D change is a common cancer-linked mutation that keeps it switched on.
- Cre-mediated expression: a genetic switch that turns a gene on in chosen cells, here used to activate the mutant KRAS.
- Lumen: the hollow central space that healthy mammary organoids form as they mature.
- Apoptosis: programmed cell death, a normal way cells are removed.
- Heterotypic organoid: an organoid containing a mix of two cell types, here mutant and non-mutant cells. · level: research-level

<details><summary>Original abstract</summary>

Modeling cancer initiation, progression, and metastasis has greatly impacted our understanding of fundamental cell and molecular mechanisms driving disease and has led to breakthrough treatments that greatly improve patient outcomes. Understanding the earliest stages of tumor formation is particularly important for uncovering the root causes of oncogenic transformation and tumor evolution. It has been historically difficult to model the cellular dynamics that drive the earliest stages of tumor evolution, largely due to difficulties in culturing and manipulating normal primary cells in 3-dimensional environments, triggering oncogenesis, and observing the resulting effects. Recent advances in 3D organoid culture provide a promising avenue to address these challenges. In this study, we have developed a Kras based organoid model of early tumorigenesis. In our model, oncogenic transformation was triggered by Cre-mediated expression of oncogenic KRASG12D in otherwise healthy murine-derived mammary epithelial organoids. While normal organoids displayed controlled organoid growth and morphogenesis, induction of KRASG12D caused neoplastic organoid growth that occurred with the absence of lumen formation. Gene expression analysis revealed up regulation of several KRAS effectors, and a broad repertoire of genes associated with tumor development and human breast cancer. Induction of oncogenic Kras in our model resulted in heterotypic organoids that possessed KRASG12D + cells growing alongside KRASG12D- cells. In this context, amplification of KRASG12D + cells occurred at the expense of KRASG12D- cells. Finally we observed that neoplastic growth of KRASG12D expressing organoids was associated with a suppression of apoptosis. We believe that our organoid model provides a platform that is suitable to examine the earliest stages of tumor development and can be expanded to study several questions related to cancer biology, prevention studies, therapeutic development, and beyond.

</details>

## Ecology and evolution

### [From individual movement to ecosystem response: how landscape structure shapes herbivore impacts](https://www.biorxiv.org/content/10.64898/2026.11.19.766513v1)
*Suarez, D. L.; Guisoni, N.; Laguna, M. F.* · `ecology` · bioRxiv doi:10.64898/2026.11.19.766513 v1 · relevance 0.10

- **In one sentence**: A spatially explicit stochastic individual-based model of two herbivore populations with different movement and foraging strategies, sharing renewable resources across heterogeneous landscapes, examined with Monte Carlo simulations to see how movement and landscape structure shape resource depletion and population dynamics.
- **In plain words**: This paper asks how individual animals moving around a landscape add up to changes in the plants they eat across the whole area. The authors built a computer simulation with two kinds of grazing animals that move and feed differently, on land where food is unevenly spread, and ran many randomised trials. They report that movement mainly sets where plants get depleted, and that more productive land can sometimes lead to a larger relative loss of plant biomass.
- **Why it matters**: The findings suggest that more food does not automatically protect an ecosystem from grazing, and that plant biomass can fall well before visible loss of vegetation cover, which matters for reading early warning signs in rangelands. The text is a model study only, with no field data mentioned, so its relevance to real landscapes is untested from the given text alone.
- **Background needed**: - Individual-based model: a simulation that tracks each animal separately and lets patterns emerge from their local behaviour.
- Stochastic: includes random chance, so outcomes vary between runs.
- Monte Carlo simulation: running the model many times with random inputs to see the range of likely outcomes.
- Consumer–resource dynamics: how grazers (consumers) and plants (resources) affect each other's numbers.
- Heterogeneous landscape: an environment where food and conditions vary from place to place.
- Refuge: a place where prey can hide from predators, which here affects herbivore survival.
- Biomass vs. occupancy: total plant mass versus how much ground the plants cover. · level: research-level

<details><summary>Original abstract</summary>

Understanding how local interactions generate large-scale ecological dynamics is a central challenge in ecology. In heterogeneous environments, consumer movement links resource distribution with exploitation, producing responses that may not be predicted from consumer abundance or resource availability alone. Here, we develop a spatially explicit stochastic individual-based model of two herbivore populations with contrasting movement and foraging strategies that share renewable resources. The model incorporates heterogeneous resources, consumer movement and feeding, resource regeneration, predation, and refuge availability. Using Monte Carlo simulations, we examine how herbivore pressure and landscape structure shape population dynamics and resource depletion. Movement strongly determines the spatial pattern of depletion, while resource vulnerability depends on the overlap between resource distribution and consumer activity. Counterintuitively, increasing the extent of a productive region increases initial resource biomass but can also increase relative resource loss. Additional resources sustain consumer activity where herbivores concentrate, showing that greater resource availability does not necessarily buffer ecosystems against herbivory. Resource biomass can also decline substantially before major reductions in vegetation occupancy become apparent. These results demonstrate how individual behaviour and landscape structure jointly shape ecosystem responses. The model provides a framework for investigating how spatially coupled consumer-resource interactions generate ecological dynamics.

</details>

### [Synchronized Seasonal Shifts in the Climate, Diet, and Gut Microbiome of a Rainforest Lemur (Eulemur rufifrons)](https://www.biorxiv.org/content/10.64898/2026.11.18.767713v1)
*Stephens, J. N.; Weisrock, D. W.; Raheimanjato, J. P. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.18.767713 v1 · relevance 0.09

- **In one sentence**: A 10-month field study of wild red-fronted brown lemurs in Ranomafana National Park links monthly rainfall, temperature and diet diversity to shifts in gut bacterial communities, including trade-offs between carbohydrate- and fiber-degrading bacteria.
- **In plain words**: Wild lemurs in a Madagascar rainforest face large seasonal changes in weather and food. The researchers followed one lemur species for ten months and tracked its gut bacteria alongside local rain, temperature and what the animals ate. They report that the gut bacteria changed together with the climate and diet, which may help the animals cope with lean periods.
- **Why it matters**: It offers a field-based look at whether gut microbes can help wild animals adjust to environmental stress such as climate change, a question relevant to endangered species. The text does not show how far these patterns hold beyond this one species and site, so the broader conclusions remain tentative.
- **Background needed**: - The gut microbiome is the community of bacteria living in the digestive tract, which helps break down food.
- Phenotypic plasticity means an organism can change its traits in response to its environment without genetic change.
- Frugivory means eating mostly fruit; folivory means eating mostly leaves, which are high in fiber and harder to digest.
- Carbohydrate- and fiber-metabolizing bacteria are microbes that break down sugars and plant fiber, respectively.
- Madagascar's wet and dry seasons drive large swings in rainfall, temperature and fruit supply.
- The abstract alone gives no sample sizes or statistical details, so the strength of the findings cannot be judged from this text. · level: intermediate

<details><summary>Original abstract</summary>

Gut microbiome (GM) flexibility extends the adaptive potential of host species in the face of rapid ecological change. Madagascar's endemic primates offer a powerful natural system to study GM plasticity as the island experiences substantial environmental change throughout the year. This is especially true in the eastern rainforests, which experience marked variation in temperature, rainfall, and fruit availability between the wet and dry seasons. To elucidate interactions between climate, diet, and the GM, we conducted a 10-month study of the ecologically flexible red-fronted brown lemur (Eulemur rufifrons) in Ranomafana National Park. We detected significant shifts in gut microbial communities correlated with monthly rainfall, temperature, and dietary diversity. Trade-offs between abundances of carbohydrate- and fiber-metabolizing bacteria reflected shifts between frugivory and folivory, suggesting that the GM buffers energetic and/or nutritional imbalances when resources are scarce. Finally, we observed synchronized shifts in climate and the GM despite deviation from normal seasonal patterns, demonstrating the GM's rapid response to environmental cues. Our results suggest that the GM contributes to phenotypic plasticity across seasons, enabling endangered primates to better cope with environmental stressors like climate change.

</details>

## Plant biology

### [Inhibition of carbon fixation activates ROS-linked autophagy in the single-celled green alga Chlamydomonas reinhardtii](https://www.biorxiv.org/content/10.64898/2026.11.17.767326v1)
*Gamez-Arcas, S.; Mallen-Ponce, M. J.; Munoz-Palacios, I. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.17.767326 v1 · relevance 0.06

- **In one sentence**: In the green alga Chlamydomonas reinhardtii, blocking the Calvin-Benson-Bassham enzyme PRK triggers light-dependent ROS accumulation and autophagic flux, and loss of ATG8 worsens ROS, photosynthetic dysfunction and cell death under carbon-fixation inhibition.
- **In plain words**: Plants and algae use sunlight to turn carbon dioxide into sugar, and they also recycle their own cell parts through a process called autophagy. This paper asks how these two systems connect in a single-celled green alga. The authors blocked a key enzyme of carbon fixation (PRK), either with a drug or by genetic knockout, and found that this caused harmful reactive oxygen species to build up in light and switched on autophagy.
- **Why it matters**: The work suggests autophagy helps protect photosynthetic cells when carbon fixation stalls, and that it aids recovery after prolonged stress. This links energy capture, cellular "rust" (oxidative) signaling and self-recycling, which may matter for understanding how crops and algae cope with light stress, though the text does not establish applications.
- **Background needed**: - Photosynthesis: light energy is used to fix CO2 into sugars via the Calvin-Benson-Bassham (CBB) cycle inside chloroplasts.
- PRK (phosphoribulokinase): an enzyme in the CBB cycle; blocking it stops carbon fixation.
- Reactive oxygen species (ROS): chemically reactive oxygen molecules that can damage cells at high levels but also act as signals.
- Autophagy: a cellular recycling system that packages damaged or unneeded components for breakdown. ATG8 is a protein essential to this process, so an atg8 knockout cannot perform normal autophagy.
- Autophagic flux: the rate at which material moves through the autophagy pathway, not just how many autophagy structures are present.
- Chlamydomonas reinhardtii: a single-celled green alga widely used as a lab model organism. · level: research-level

<details><summary>Original abstract</summary>

Autophagy is a central mechanism that promotes stress acclimation and nutrient recycling, thereby contributing to metabolic homeostasis. However, how photosynthetic carbon assimilation is integrated with autophagy remains poorly understood. Here, we establish a functional link between carbon fixation, redox signaling, and autophagy in the green microalga Chlamydomonas reinhardtii. Pharmacological inhibition of phosphoribulokinase (PRK), a key enzyme of the Calvin-Benson-Bassham cycle, induced chloroplast stress, reactive oxygen species (ROS) accumulation, and autophagic flux specifically in the light. Consistently, genetic loss of PRK caused light-dependent ROS accumulation and autophagy activation, which was enhanced by carbon limitation and attenuated by ROS scavenging. To determine the physiological relevance of this response, we generated an atg8 knockout mutant and an atg8 prk double mutant. Loss of ATG8 increased ROS accumulation, photosynthetic dysfunction, and cell death when carbon fixation was inhibited, supporting a protective role for autophagy against light-driven metabolic stress. Although both prk and atg8 prk cells were unable to grow under high light, only prk cells resumed growth after transfer to permissive conditions, indicating that autophagy contributes to recovery from prolonged impairment of photosynthetic carbon metabolism. Our findings identify autophagy as a component of the regulatory network linking photosynthetic carbon assimilation with redox homeostasis and cellular acclimation to light stress.

</details>

### [A trade-off shaping leaf mesophyll architecture emerges from a stochastic geometry model](https://www.biorxiv.org/content/10.64898/2026.11.18.767598v1)
*Rahimi-Majd, M.; M. Borsuk, A.; Masoomy, H. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.18.767598 v1 · relevance 0.05

- **In one sentence**: A computational stochastic-tessellation framework reconstructs 2D paradermal slices of spongy mesophyll from 40 vascular plant species using leaf porosity, cell-arm length and cell-arm diameter, and a stochastic-geometry model links porosity and cell-arm statistics to cell wall construction cost.
- **In plain words**: Leaves contain a spongy inner layer of cells with air gaps between them, and its layout affects how well a plant can take in carbon dioxide for photosynthesis. The authors built a computer model that generates realistic-looking slices of this spongy layer for 40 plant species, using three measured quantities. They also wrote a mathematical model that matches these simulations and suggests how much cell wall material the layer needs, depending mainly on how porous the leaf is.
- **Why it matters**: The work offers a simple, few-parameter way to describe leaf internal structure and its material cost, which could help people reason about designing leaves that balance carbon uptake against building cost. The text does not show any direct application yet, so its usefulness for crops or other plant work remains to be tested.
- **Background needed**: - Mesophyll: the photosynthetic tissue inside a leaf, here the spongy layer with air spaces.
- Porosity: the fraction of the leaf slice that is air rather than cell material.
- Paradermal slice: a flat, two-dimensional cross-section taken parallel to the leaf surface.
- Stochastic tessellation: dividing a space into cell-like regions using random processes, a standard tool in geometry.
- Cell arms: the branch-like extensions of spongy cells that connect to neighbors; their number (one to three) and shape are modeled.
- Cell wall construction cost: the material and energy a plant spends building cell walls, modeled here as a geometric quantity. · level: research-level

<details><summary>Original abstract</summary>

Leaf mesophyll architecture has a great impact on plant functions, including photosynthesis. Yet, understanding the principles governing growth, stability, and interspecific variation of leaf mesophyll architecture remains elusive. Here, we develop a computational framework based on stochastic space tessellation to simulate two-dimensional paradermal slices of leaf spongy mesophyll across 40 vascular plant species using three data-derived parameters: leaf porosity, cell arm length, and cell arm diameter. The framework successfully reconstructs leaf slices while preserving six biological, topological, and cell-level traits, with one- to three-armed cell geometries generally outperforming circular cells. Importantly, we further develop a theoretical model based on stochastic geometry that closely agrees with the simulations and reveals that leaf porosity strongly influences cell wall construction cost, while cell-arm statistics shape this relationship. Our parsimoniously parameterized model provides a basis for optimizing leaf architecture to maximize carbon dioxide uptake while minimizing cell wall construction costs.

</details>

## Bioengineering and synthetic biology

### [Dual photoresponsive hydrogel surfaces enabling integrated single-cell analysis of morphology and gene expression](https://www.biorxiv.org/content/10.64898/2026.11.18.767535v1)
*Li, X.; Uehara, R.; Mizuno, K. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.18.767535 v1 · relevance 0.05

- **In one sentence**: A dual light-responsive hydrogel surface traps single cells at uniform density, tracks their shape changes over time, and releases chosen cells by localized light-triggered degradation for downstream single-cell gene expression analysis.
- **In plain words**: Cells in the body and in the lab differ from one another, and it is hard to watch how a single cell changes its shape over time and then check which genes it is using. This paper describes a gel-based surface that holds individual cells in place with light, lets researchers film them, and then frees only the cells they picked by shining light on a small spot to dissolve the gel there. The authors used this to link changing cell shapes to gene activity, and to look at gene changes linked to invasive cancer cell behavior.
- **Why it matters**: Being able to connect what a cell looks like over time with what genes it is running could help explain why some cells in a tumor behave differently from others. The provided text describes the workflow and its demonstration on invasive cancer cells but does not give quantitative results, so the strength of the findings cannot be judged from this summary alone.
- **Background needed**: - Hydrogel: a water-swollen, soft polymer network, similar to gel used in contact lenses, that can hold cells.
- Photoactivatable / photodegradable material: a material that changes behavior (sticks cells down, or dissolves) when hit with light of a specific wavelength.
- Single-cell gene expression analysis: measuring which genes a single cell is actively switching on, usually by reading its RNA.
- Morphological dynamics: changes in a cell's shape and size over time, which can be observed by microscopy.
- Invasive cancer cell behavior: cancer cells that move through surrounding tissue, a key step in metastasis.
- Real-time image processing: software that automatically analyzes microscope images as they are captured. · level: research-level

<details><summary>Original abstract</summary>

Integrated single-cell analysis linking time-resolved cellular phenotypic dynamics with gene expression is essential for understanding cellular heterogeneity but remains technically challenging. Here, we report a dual photoresponsive hydrogel that combines a photoactivatable cell-trapping material with a photodegradable hydrogel, enabling light-directed single-cell capture, time-resolved imaging, and the on-demand release of selected cells for downstream gene expression analysis. This approach allows cells to be arrayed at a high density with uniform spacing, facilitating high-throughput monitoring of morphological dynamics. Cells exhibiting phenotypes of interest can be precisely retrieved by localized hydrogel degradation induced by secondary light irradiation and subsequently subjected to single-cell gene expression analysis. Using this workflow in combination with high-throughput real-time image processing technology, we directly link dynamic morphological features to gene expression and demonstrated the ability of the workflow to examine transcriptional alterations associated with invasive cancer cell behavior.

</details>

### [Enhancing the Efficacy of Oncolytic Viruses by Engineering Virus Host Interactions Using CRISPR Cas13d](https://www.biorxiv.org/content/10.64898/2026.11.20.768134v1)
*Ameil, Z.; Kooshki Zamani, N.; Khalid, Z. et al.* · `synthetic biology` · bioRxiv doi:10.64898/2026.11.20.768134 v1 · relevance 0.05

- **In one sentence**: The paper builds a doxycycline-inducible CRISPR Cas13d system carried inside an oncolytic herpes simplex virus 1 (oHSV1) to switch off tumor-cell antiviral genes during infection, and tests guide RNA library effects in three mouse and human tumor cell lines.
- **In plain words**: Oncolytic viruses are viruses engineered to infect and kill cancer cells, but tumor cells can fight back with their own antiviral defenses. This work describes a way to temporarily switch off selected host antiviral genes using a gene-editing-style tool, controlled by a drug (doxycycline) that turns the system on. The authors report that the approach works in reporter tests and shows guide-dependent differences in fluorescence across several tumor cell lines.
- **Why it matters**: Enhancing how well oncolytic viruses replicate in tumors is a practical goal for cancer therapy, and a controllable, programmable way to probe host-virus interactions could help researchers test which defenses matter. The text reports only lab cell-culture results, with no animal or clinical outcomes, so its relevance to treatment is still unknown.
- **Background needed**: - Oncolytic virus: a virus engineered to replicate in and destroy cancer cells.
- HSV1 (herpes simplex virus type 1): the virus used as the backbone here.
- CRISPR Cas13d: a programmable enzyme that is guided by RNA to cut other RNA molecules, lowering the amount of a target protein; it is different from DNA-editing CRISPR.
- Guide RNA (gRNA): a short RNA sequence that tells the enzyme which target to cut.
- Tet On / Tet Off: genetic switches that turn gene activity on or off in the presence of doxycycline, an antibiotic-derived drug.
- Antiviral factors: host proteins that block viral replication.
- Reporter assay: a test that uses a glowing or measurable marker to show whether a genetic element is working.
- Cell lines named: EMT6 and CT26 (mouse tumor lines), 786-O (human kidney cancer line). · level: research-level

<details><summary>Original abstract</summary>

Oncolytic herpes simplex virus type 1 (oHSV1) is a promising cancer therapy, but tumor cell antiviral responses can restrict viral replication. Strategies for temporally controlled targeting of antiviral factors remain limited. Here, we developed an inducible CRISPR Cas13d platform to modulate host responses during HSV1 infection. We screened 13 pharmacological inhibitors across tumor models to identify pathways associated with restricted infection. Reporter assays identified Cas13d as the preferred effector over Cas13b, while endogenous-target experiments demonstrated Cas13d mediated reductions in target protein abundance. We optimized guide RNA expression using RNA polymerase III promoters, selected p7SK, and established doxycycline-responsive Tet On and Tet Off systems. The platform was incorporated into HSV1 to generate a gRNA library targeting 15 host antiviral genes, together with two non-targeting controls. Doxycycline-dependent reporter readouts demonstrated inducible activity. Evaluation in EMT6, CT26, and 786 O cells revealed guide-dependent differences in fluorescence. These findings establish a programmable framework for investigating virus host interactions during oncolytic HSV infection.

</details>

## Mathematical biology (arXiv)

### [One-Step Self-Assembling Lipopolymer Coatings Enable Direct Longitudinal Biosensing in Native Biological Matrices](https://arxiv.org/abs/2611.27422)
*Pascal R\"uedi, Sarina Seiter, Stephan Handschin et al.* · `q-bio.QM` · arXiv:2611.27422v1 · relevance 0.05

- **In one sentence**: A one-step, self-assembling lipid-polymer (lipopolymer) surface coating for microfluidic immunoassays that resists sticky background in undiluted serum and enables digital holographic counting of tetraspanin-positive extracellular vesicles from lung cancer cell models.
- **In plain words**: Lab tests that detect biological molecules often get confused by "sticky" stray material in blood or serum that clings to the test surface. This paper describes a simple coating, made of fat-based particles that assemble themselves on the inside of a tiny channel within minutes, which helps the surface resist that clinging and attach detection probes. Using this coating with a microscope-based imaging device, the authors tracked how fast lung cancer cells released small vesicles over time, using 50 microliters of sample without first purifying it.
- **Why it matters**: Being able to watch cells release signaling particles continuously, in their own fluid and without a purification step, could make biosensing less of a one-time endpoint test. The text does not show how broadly the approach will generalize beyond the cell models and sample types described, so its wider impact remains to be tested.
- **Background needed**: - Biosensing: detecting a specific molecule or particle in a sample, often by letting it bind to a probe fixed on a surface.
- Non-specific binding (cross-reactivity): unwanted sticking of other molecules to the surface, which creates false signals; a bigger problem in tiny channels because the surface-to-volume ratio is high.
- Antifouling coating: a layer that resists this sticking; PEGylated lipids (fats with chains of polyethylene glycol) are a common example.
- Self-assembly: molecules organizing into a structure on their own, without a chemical reaction bonding them to the surface.
- Microfluidics: systems that handle tiny volumes of fluid in micrometer-scale channels, often made of glass or PDMS (a silicone polymer).
- Digital in-line holography: imaging that reconstructs 3D positions of particles from interference patterns, allowing individual particles to be counted.
- Extracellular vesicles: tiny membrane-bound packets released by cells; tetraspanins are surface proteins used as markers for them.
- Label-free: detection without attaching a dye or tag to the target. · level: research-level

<details><summary>Original abstract</summary>

Sample-driven cross-reactivity remains a fundamental bottleneck for sensitive and selective biosensing in complex biological environments, particularly in microfluidic systems where high surface-to-volumes ratios amplify non-specific interactions. Here, we address this challenge with a one-step, biomimetic surface functionalization strategy based on engineered lipid-based nanocarriers that self-assemble within minutes into immunoassay-ready, antifouling interfaces that couple pegylated-lipid passivation with biorthogonal, site-specific probe conjugation. This approach enables rapid, tuneable, and reproducible surface functionalization, which suppresses sample-specific cross-reactivity even in undiluted serum, and supports direct, label-free digital biosensing assays directly in native biological environments. When integrated into an optofluidic platform combining digital in-line holography and microfluidics, this approach allows time-resolved quantification of tetraspanin-positive extracellular vesicle secretion dynamics from two-dimensional and three-dimensional lung cancer cell models using 50 {\mu}L of sample within 10 min, without isolation or purification. Because the presented surface functionalization proceeds via self-assembly rather than covalent surface modification, this one-step modular-approach is intrinsically decoupled from device fabrication and applies to both glass and PDMS, coating the entire microfluidic channel, thereby establishing a general route for integrating biomimetic nanostructures into robust, high-performance immunoassays, advancing biosensing beyond end-point measurements, and towards rapid and continuous real-time monitoring.

</details>

### [Self-organized fractional silencing of pyramidal neurons under global depolarization in a spatial neuron-glial microcircuit model](https://arxiv.org/abs/2611.27847)
*Stanislav V. Lagosha, Andrey Yu. Verisokin, Darya V. Verveyko et al.* · `q-bio.NC` · arXiv:2611.27847v1 · relevance 0.04

- **In one sentence**: A two-dimensional computational model of a neuron-astrocyte-vascular unit, with Hodgkin-Huxley neurons, astrocyte-regulated extracellular potassium, glutamate spillover and noradrenergic modulation, examines how inhibitory and pyramidal cells enter depolarization block and how spatial microclusters and localized astrocytic damage produce persistent pathological activity.
- **In plain words**: This paper uses a computer model of a small patch of brain tissue to study how seizure-like bursts and spreading waves of electrical silence can arise. The model tracks nerve cells, the support cells called astrocytes that clear potassium, the blood-vessel-linked tissue around them, and the chemicals they release. The authors report that inhibitory cells fail first under high potassium, and that above a certain stimulation level the network breaks into small groups of cells firing stubbornly fast.
- **Why it matters**: The work is a model-based study, so its findings are predictions to be tested rather than established facts. It may matter for understanding epilepsy and cortical spreading depolarization, and for asking how localized damage to astrocytes could spread into wider tissue harm, but the text does not show direct links to clinical data.
- **Background needed**: - Neurons communicate through electrical spikes; "depolarization" means a cell's electrical state shifts so it can no longer fire normally.
- "Depolarization block" (DB) is a state in which a cell is held too positive to fire, effectively silenced.
- Inhibitory interneurons calm the network; pyramidal neurons are the main excitatory cells. Losing inhibition tilts the balance toward excess activity.
- Extracellular potassium rises when neurons fire heavily; astrocytes normally soak it up. Too much potassium can push cells into block.
- Hodgkin-Huxley models are detailed equations describing how a neuron's membrane voltage changes with ion flows.
- The neurogliovascular unit (NGVU) is the functional grouping of neurons, glia (astrocytes) and blood vessels.
- Epileptiform discharges are seizure-like firing patterns; cortical spreading depolarization is a slow wave of widespread electrical silencing that occurs in brain injury and migraine. · level: research-level

<details><summary>Original abstract</summary>

Pathological transitions in nervous tissue, including epileptiform discharges and cortical spreading depolarization, depend on the interplay between cellular and interstitial mechanisms. We develop a biophysically detailed two-dimensional model of the neurogliovascular unit (NGVU) integrating neuronal populations in the Hodgkin-Huxley formalism, astrocyte-regulated extracellular potassium dynamics, extracellular neurotransmitter spillover, and noradrenergic neuromodulation. Numerical simulations show that inhibitory interneurons enter depolarization block (DB) at significantly lower extracellular potassium concentrations and stimulation intensities than pyramidal neurons. Early loss of inhibition shifts the local excitation-inhibition balance and triggers network hyperexcitability. In the spatially extended network, exceeding a critical stimulation threshold induces a transition from heterogeneous but spatially uniform firing to network fragmentation into stable active microclusters with self-sustained high-frequency firing. Pyramidal neurons with lower excitatory synaptic input receive less recurrent excitation, which protects them from DB. By continuously releasing potassium ions and glutamate into the extracellular space, pyramidal neurons drive strong depolarization in more densely connected neighbors and push them into deep DB. Simulations of localized astrocytic dysfunction predict a spatial limit for potassium clearance defects. Small damaged cores are fully compensated by diffusion and uptake by surrounding healthy astrocyte units. However, above a critical damage size, activity-dependent potassium buildup and firing positive feedback disrupt homeostasis in surrounding units, promoting persistent depolarized centers with self-sustained, spatially segregated pathological activity.

</details>

## Epidemiology

### [Depressive Symptom Trajectories and Incident Cognitive Impairment by Outcome Ascertainment](https://www.medrxiv.org/content/10.64898/2026.11.18.26368449v1)
*Liu, X. L.; Guo, Z. L.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368449 v1 · relevance 0.07

- **In one sentence**: Harmonized analysis of four national aging cohorts (91,043 adults aged 50+) testing whether links between depressive symptom trajectories and incident cognitive impairment depend on how rigorously cognitive outcomes were ascertained, from self-report to clinical consensus diagnosis.
- **In plain words**: Researchers asked whether depression is linked to later memory and thinking problems, and whether the answer changes depending on how carefully those thinking problems were checked. They followed older adults in China, the US, England and Europe, grouping them by how their depressive symptoms changed over time. Associations were weak or absent when cognitive problems were judged from self-report, but grew stronger as the outcome was checked more rigorously, up to a clinical diagnosis.
- **Why it matters**: If the strength of the depression–cognition link depends on how outcomes are measured, then trials and projections that rely on self-report may understate the potential benefit of treating depression. The text reports this pattern as exploratory, so it is a hypothesis to test in other data rather than settled fact.
- **Background needed**: - Cohort study: following a large group of people over years and recording who later develops a condition.
- Depressive symptom trajectory: a pattern of mood symptoms over time, such as persistently low, persistently high, getting worse, or improving.
- Group-based trajectory modeling: a statistical method that sorts people into groups with similar symptom patterns.
- Hazard ratio (HR) and odds ratio (OR): measures of how much more likely an outcome is in one group compared with another; values above 1 mean higher risk.
- Meta-analysis and meta-regression: combining results from several studies, and testing whether a study feature (here, outcome rigor) explains differences between them.
- Cognitive impairment: a range from mild memory and thinking problems to dementia.
- Clinical consensus diagnosis (HCAP): an expert panel's assessment after detailed testing, the most rigorous of the five levels described. · level: research-level

<details><summary>Original abstract</summary>

Importance: Dementia prevention frameworks treat depression as a leading modifiable risk factor, but cohort estimates of the association vary widely; whether this variation reflects how cognitive outcomes are ascertained is unknown. Objective: To examine whether associations between depressive symptom trajectories and incident cognitive impairment vary by outcome ascertainment rigor. Design, Setting, and Participants: This harmonized cohort study included 91,043 adults aged 50 years or older from 4 national longitudinal aging cohorts (CHARLS [China], HRS [US], ELSA [England], and SHARE [16 European countries]); baseline waves spanned 2006 to 2011, with follow-up through 2023. Exposure: Depressive symptom trajectory classes (persistent low, persistent high, incident worsening, remitting) derived using group-based trajectory modeling. Main Outcomes and Measures: Incident cognitive impairment ascertained under a 5-level hierarchy of increasing rigor, from self-report (level 1) to clinical consensus diagnosis (level 5; Harmonized Cognitive Assessment Protocol [HCAP]). Cohort-specific Cox models were pooled by random-effects meta-analysis; meta-regression tested ascertainment rigor as a moderator of heterogeneity. Results: Under nonadjudicated outcomes, the incident-worsening trajectory was associated with incident cognitive impairment in CHARLS (HR, 1.31; 95% CI, 1.06-1.62) and SHARE (HR, 1.99; 95% CI, 1.87-2.13) but not HRS (HR, 1.05; 95% CI, 0.95-1.16) or ELSA (HR, 1.10; 95% CI, 0.95-1.27); the persistent-high trajectory was not significant under any nonadjudicated outcome (HR range, 1.07-1.15). Under clinical consensus diagnosis (n = 3,196), all non-low trajectories were independently associated with mild cognitive impairment or dementia (OR range, 1.66-2.29; dementia-only persistent high: OR, 3.32; 95% CI, 1.85-5.95). Effect sizes increased stepwise with ascertainment rigor (meta-regression slope, 0.314 log HR per level; P < .001; residual I2 = 0%; R2 = 100%; exploratory). Findings were robust to lagged, weighted, and competing-risk analyses; biological aging acceleration did not differ across trajectories. Conclusions and Relevance: The detectability and magnitude of depression-related cognitive risk depend on outcome ascertainment rigor. Prevention trials and burden projections relying on self-reported outcomes may underestimate the benefit of depression treatment.

</details>

### [Epidemiology of Cardiac Structure and Function Among African Caribbeans in Tobago: A Population-based Cohort Study](https://www.medrxiv.org/content/10.64898/2026.11.18.26368418v1)
*Deb Nath, N.; Miljkovic, I.; Katz, R. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368418 v1 · relevance 0.06

- **In one sentence**: A population-based cohort study of 924 African Caribbean adults in Tobago reporting the prevalence of echocardiographic cardiac structure and function abnormalities, stratified by age, sex, and heart failure stage.
- **In plain words**: Heart failure is a condition where the heart struggles to pump blood well, and people of African descent are known to be at higher risk. This study looked at heart ultrasound scans from 924 adults in Tobago, an island in the Caribbean, to see how common early heart changes were. It found that most participants had an enlarged or thickened heart wall pattern, that women and older adults had more of these structural changes, and that men were more often in the symptomatic heart failure stage.
- **Why it matters**: Little was known about heart structure in this population, so these figures can help local public health planning for cardiovascular care. The text does not say whether these findings would apply to other groups, and it reports prevalence at one point in time, so it does not show what causes the changes.
- **Background needed**: - Heart failure: the heart cannot pump or fill with blood as well as it should.
- Echocardiography: an ultrasound scan of the heart used to measure its size, wall thickness, and pumping.
- Left ventricle: the main pumping chamber of the heart.
- LV mass index and concentric remodeling: the heart wall becomes thicker relative to chamber size.
- Ejection fraction (LVEF): the share of blood pumped out with each beat; low values suggest weak pumping.
- Global longitudinal strain (GLS): a measure of how much the heart muscle stretches and squeezes; more negative values are normal.
- Diastolic dysfunction (DD): the heart relaxes or fills abnormally between beats; E/e' and E/A ratios are measures used to estimate this.
- Heart failure stages A to C: Stage A is at risk without symptoms, Stage B has heart changes without symptoms, and Stage C has symptoms.
- Prevalence: the share of people with a condition at a given time. · level: intermediate

<details><summary>Original abstract</summary>

Background: Individuals of African genetic ancestry are at high risk for heart failure (HF), which is often preceded by cardiac structural and functional abnormalities. Nevertheless, little is known about cardiac structure and function among Afro-Caribbeans residing in Tobago. This study aimed to investigate the epidemiology of cardiac structure and function among African Caribbeans in Tobago. Methods: A total of 924 participants (41-83 years) underwent clinical evaluation and transthoracic echocardiography. Images were analyzed for left ventricular (LV) mass index (MI), left atrial volume index, diastolic dysfunction (DD), LV ejection fraction (LVEF), global longitudinal strain (GLS), E/e' ratio, E/A ratio, and other echocardiographic measures. Cardiac structure and function were evaluated by age, sex, and HF stage. Results: The mean age was 61.7 years, with 61.4% women, 47.8% obesity, and 20.2% diabetes. Average systolic blood pressure was approximately 140 mmHg, and 76.7% had hypertension. Abnormal LV geometry was present in 77.1% of participants, predominantly concentric remodeling (69.5%). The prevalence of DD was 13.4%, LVEF <50% was 1.5%, and abnormal GLS ([&le;]-18%) was 5.2%. Women had significantly higher E/e' ratios and a higher prevalence of Stage A and Stage B HF, whereas men had a higher prevalence of symptomatic (Stage C) HF. Participants aged 65-83 years had significantly higher E/e' ratio, concentric remodeling, and LV hypertrophy than those aged 41-57 years. Conclusions: Women and older adults have higher LV structural abnormalities and DD than men and younger adults. These results will be helpful to inform public health priorities related to cardiovascular health in Tobago.

</details>

## Infectious diseases

Nothing notable this time.

## Public and global health

### [Ni Binti Ni Mama: Participatory, human-centred development of a targeted nurturing care model for teenage mothers and their children in Kakamega County, Kenya - a mixed-methods study](https://www.medrxiv.org/content/10.64898/2026.11.17.26368359v1)
*Morema, E. N.; Shisanya, M. S.; Oronje, S. K. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.17.26368359 v1 · relevance 0.06

- **In one sentence**: A mixed-methods needs assessment (57 teenage mothers, interviews, health-worker interviews) and a stakeholder workshop that together produced a targeted nurturing care model for teenage mothers and their children in Kakamega County, Kenya, with a draft community health volunteer training module piloted with 21 volunteers.
- **In plain words**: This study looks at how teenage mothers in rural western Kenya care for their babies and young children, and at what support would help them. The researchers surveyed 57 teenage mothers, interviewed some mothers and health workers, and then ran a workshop with local health managers and university experts to design a support programme. Health services were widely used, but early learning activities such as reading and picture books were rare, and most mothers had skipped meals for lack of money.
- **Why it matters**: Teenage mothers are a group that often falls between health, education and social services, and the paper shows a concrete way to apply a global early-childhood care framework to them. The text does not show whether the model improves outcomes; the authors say a feasibility evaluation and direct involvement of the teenage mothers themselves are still to come, so its value is for now as a design and needs record.
- **Background needed**: - Nurturing care: a global framework (from WHO and partners) covering health, nutrition, safety, responsive caregiving and early learning for young children.
- "Targeted" support level: extra help aimed at groups facing extra barriers, beyond services for everyone.
- Mixed-methods: combining numbers (questionnaires, scores) with interviews analysed for themes.
- Welch's t-test: a statistical test for comparing two group averages when their spread differs.
- Community health volunteers: trained lay workers who visit homes to give health advice.
- Social Cognitive Theory: a behaviour-change theory emphasising learning from others, self-confidence and environment.
- Participatory, human-centred design: involving the people affected in shaping the solution, which the authors say was only partly done here.
- Sub-Saharan Africa: the region south of the Sahara; Kakamega is a county in western Kenya. · level: intermediate

<details><summary>Original abstract</summary>

Teenage mothers and their children face multiple barriers to nurturing care, yet few models translate the Nurturing Care Frameworks targeted support level into practice for this group in sub-Saharan Africa. We describe the participatory, human-centred development of Ni Binti Ni Mama ( she is a girl, she is a mother), a targeted nurturing care model for teenage mothers in Kakamega County, Kenya. In phase one, a needs assessment combined a structured questionnaire and observation checklist covering the five nurturing care components (57 teenage mothers of infants), in-depth interviews with five mothers and five key informant interviews with health workers. Component scores were compared across groups using Welchs t-tests; qualitative data were analysed thematically. In phase two, a stakeholder workshop with the sub-county health management team and university experts generated and prioritised strategies; a draft community health volunteer training module was tried out with 21 volunteers. The mean overall nurturing care score was 69.1% (SD 10.3). Uptake of maternal and child health services was high (good health score 88.1%), whereas early learning scored lowest (40.4%): 28.1% of children had a picture book and 15.8% of mothers had read or looked at pictures with their child the previous day. Most mothers (75.4%) had skipped meals for lack of money. Responsive caregiving was lower among mothers reporting emotional stress (76.4% vs 86.0%; p=0.005). Interviews described economic dependence, absent fathers, family conflict, peer stigma and food insecurity. The resulting model, framed by Social Cognitive Theory, combines community health volunteer home visits, school and family sensitisation, teen mothers clubs and peer mentorship, lactation support for school re-entry, and linkage to youth-friendly services and economic support. Teenage mothers informed the model through their needs and preferences but did not participate in design decisions; their direct involvement and a feasibility evaluation are the next steps.

</details>

### [Long-term cooking fuel use patterns following a clean cooking intervention: Follow-up of the multi-country HAPIN trial](https://www.medrxiv.org/content/10.64898/2026.11.17.26368324v1)
*Williams, K. N.; Kearns, K.; Mugel, S. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.17.26368324 v1 · relevance 0.04

- **In one sentence**: A four-year post-trial follow-up of the multi-country HAPIN cohort (India, Guatemala, Rwanda) examining exclusive and any LPG cooking-fuel use after a time-limited clean cooking intervention, and factors linked to continued use.
- **In plain words**: Many households in poorer countries still cook over smoky open fires or basic stoves, which harms health. This study checked what happened after a research project that gave families free gas (LPG) stoves and fuel for 18 months ended. Families mostly did not keep using gas only: by year four, 82% of intervention households in India, 50% in Guatemala and 10% in Rwanda used gas at least sometimes, and very few used it exclusively.
- **Why it matters**: The health and environmental benefits of cleaner stoves only arrive if families keep using them most of the time, so this speaks to whether short-term aid programs can last. The paper's conclusion is that affordability and access policies would be needed, though the text reports associations and does not test whether such policies would work.
- **Background needed**: - HAPIN: a large randomized trial testing whether free clean stoves reduce household air pollution and health harms in India, Guatemala, Rwanda.
- LPG: liquefied petroleum gas, a bottled cooking gas that burns far cleaner than wood or charcoal.
- Exclusive use: cooking only with the clean stove, not mixing it with older fuels ("stove stacking").
- Logistic regression: a statistical method estimating how factors such as wealth or household size relate to the odds of an outcome; "aOR" is an adjusted odds ratio, where values above 1 mean higher odds.
- Socioeconomic status quartiles (Q1 lowest, Q4 highest) are wealth groupings.
- Control participants: households that did not get the stove during the trial; they were offered compensation at the end. · level: intermediate

<details><summary>Original abstract</summary>

Introduction: The exposure and health benefits of clean cooking depend on sustained, exclusive use, yet few studies have assessed fuel use after trial support ends. We conducted a prospective follow-up of the Household Air Pollution Intervention Network (HAPIN) trial cohort to assess cooking fuel use for 4 years post-trial in India, Guatemala, and Rwanda. Methods: Intervention households in the HAPIN trial received a free liquefied petroleum gas (LPG) stove, fuel, and behavioral support for 18 months. At trial completion, control participants in Guatemala and Rwanda were offered a free LPG stove or alternative compensation, and in India, a free LPG stove and 18 months of free fuel. We surveyed 2,169 participants annually for four years on exclusive and any LPG use, examined post-trial use trajectories, and assessed factors associated with post-trial LPG use using logistic regression. Results: Despite near-exclusive use during the trial, post-trial, few intervention participants used LPG exclusively (29% in India, <3% in Guatemala, near 0% in Rwanda). By year 4, 82% (India), 50% (Guatemala), and 10% (Rwanda) of intervention participants used any LPG. Sustained use was highest in India; non-use was most common in Rwanda; delayed use (starting years 3-4) was most common in Guatemala. Intervention assignment (aOR 1.8 [1.3-2.7], driven by Guatemala), socioeconomic status (up to aOR 40.9 [15.7-106.6] for Q4, relative to Q1), perceived ability to use LPG (aOR 3.9 [2.6-5.7]), household size (aOR 0.86 [0.79-0.93] per member), and country (aOR 5.4 [2.3-12.5] for India; aOR 1.9 [1.3-2.7] for Guatemala, relative to Rwanda) were significantly associated with post-trial LPG use. Only 27% of Guatemalan and 7% of Rwandan control participants chose an LPG stove (or electric, in Guatemala) as compensation, citing unaffordability and inaccessibility. Conclusions: A time-limited intervention, though successful in promoting LPG preference and sustained non-exclusive use in India and Guatemala, is unlikely to sustain the exclusive clean fuel use needed for long-term environmental and health benefits without policies supporting affordability and accessibility.

</details>

## Psychiatry and neurology

### [Carotid Artery Stenosis is Associated with Restless Legs Syndrome in the Absence of Stroke](https://www.medrxiv.org/content/10.64898/2026.11.17.26368361v1)
*Ogulnick, J. V.; Shin, W.; Mathew, J.* · `neurology` · medRxiv doi:10.64898/2026.11.17.26368361 v1 · relevance 0.10

- **In one sentence**: A TriNetX retrospective propensity-matched case-control study (58,382 per arm) finds bilateral internal carotid artery stenosis/occlusion (ICD-10 I65.23) is associated with a small increase in restless legs syndrome diagnosis (G25.81), adjusted OR 1.09 (95% CI 1.002-1.186), after excluding prior stroke/TIA.
- **In plain words**: This study asks whether narrowing of the large arteries in the neck that supply the brain is linked to restless legs syndrome, an urge to move the legs that is often worse at night. Using a large database of health records, the researchers compared people with severe narrowing or blockage of both neck arteries against similar people with hardening of the arteries but no such narrowing. People with the neck-artery problem were slightly more likely to have a restless legs diagnosis, though the difference was small.</plain>
<parameter name="why>Restless legs syndrome is common and its causes are not fully understood, so a possible vascular link is worth checking. The effect is small, and the text does not show whether the link is causal; the authors themselves say prospective studies are needed to test causality and whether treating the arteries changes the risk.
- **Background needed**: - Restless legs syndrome (RLS): a neurological condition causing an uncomfortable urge to move the legs, often at rest or at night, usually diagnosed from symptoms.
- Internal carotid artery stenosis (CAS): narrowing of the main arteries on each side of the neck that carry blood to the brain; "occlusion" means fully blocked.
- Atherosclerosis: build-up of fatty plaque that hardens and narrows arteries.
- Hypoperfusion: reduced blood flow to tissue; microemboli: tiny clots or debris traveling in the blood.
- Basal ganglia dopaminergic pathways: brain circuits using dopamine, a chemical messenger, that are thought to be involved in RLS.
- Retrospective case-control with propensity score matching: comparing existing records of two groups matched on many traits to reduce confounding; it shows association, not cause.
- Odds ratio (OR): a measure of how much more likely an outcome is in one group; 1.09 means about 9% higher odds.
- ICD-10 codes: standard diagnosis codes used in medical records. · level: research-level

<details><summary>Original abstract</summary>

Background: Restless legs syndrome (RLS) is a common neurological disorder with established links to atherosclerotic disease and secondary causes such as ischemic stroke. Hypothesizing that internal carotid artery stenosis (CAS) could induce secondary RLS through chronic hypoperfusion or microemboli to dopaminergic subcortical structures, even without overt stroke, we investigated the association between bilateral CAS and RLS. Methods: A retrospective propensity score-matched case-control study was conducted using the TriNetX Global Health Research Network. Cases (n=58,382) had bilateral CAS/occlusion (ICD-10-CM I65.23); controls (n=58,382) had atherosclerosis without CAS. Patients were excluded for prior stroke/TIA, iron deficiency, antipsychotic use, and other secondary RLS causes. Cases and controls were 1:1 matched on age, race/ethnicity, chronic kidney disease, peripheral neuropathy, peripheral artery disease, Parkinson's disease, and SSRI use. The outcome was RLS diagnosis (G25.81), assessed via conditional logistic regression. Results: RLS was diagnosed in 1,154 (1.977%) patients with bilateral CAS/occlusion versus 1,060 (1.816%) controls, yielding an absolute risk difference of 0.161% (95% CI 0.005-0.317%; p=0.0437). The adjusted odds ratio was 1.09 (95% CI 1.002-1.186), indicating a modest but significant association. Conclusion: Severe bilateral CAS/occlusion is associated with a small but statistically significant increase in RLS risk, independently of overt cerebrovascular events and known confounders. These findings support a potential vascular contribution to RLS pathogenesis, possibly through subclinical hypoperfusion affecting basal ganglia dopaminergic pathways. Prospective studies are needed to explore causality, dose-dependency, and the impact of carotid revascularization.

</details>

### [Targeting Frontostriatal Reward System Connectivity and Anhedonia in Youth Depression using Continuous Theta Burst Stimulation Plus Positive Affect Training: Preliminary Evidence and Reward Network Engagement from an Open-Label Trial](https://www.medrxiv.org/content/10.64898/2026.11.17.26368292v1)
*Karim, H. T.; Ryan, N. D.; Jones, N. P. et al.* · `psychiatry and clinical psychology` · medRxiv doi:10.64898/2026.11.17.26368292 v1 · relevance 0.08

- **In one sentence**: Open-label trial of 10 days of personalized cTBS to the dmPFC plus positive affect training in 50 depressed youth, testing whether changes in dmPFC–nucleus accumbens resting connectivity track changes in anhedonia.
- **In plain words**: Anhedonia, the loss of interest or pleasure, is a core feature of depression, and it is linked to an overly strong connection between a brain area near the front of the head (dmPFC) and a reward-related area (nucleus accumbens). In this open-label study with 50 young people with depression, researchers gave magnetic pulses to the frontal target twice a day for 10 days, combined with exercises meant to boost positive feelings. About 42% responded, and mood, anhedonia and anxiety scores improved, though the brain connection did not change on average.
- **Why it matters**: It is a small, uncontrolled trial, so it cannot show the treatment caused the improvements, but it links a specific brain-circuit change to symptom change, which is useful for designing future controlled studies. The authors also suggest that accurately aiming the stimulation at the intended network matters for results.
- **Background needed**: - Anhedonia: reduced ability to feel pleasure or interest; a key symptom of depression.
- dmPFC (dorsomedial prefrontal cortex): a region in the front of the brain involved in regulating thoughts and emotions.
- Nucleus accumbens (NAcc): a deep brain hub in the reward system.
- Functional connectivity (FC): how strongly two brain regions' activity rises and falls together, measured here with resting-state fMRI (brain scanning while at rest).
- cTBS (continuous theta burst stimulation): a brief, patterned form of transcranial magnetic stimulation that uses magnetic pulses through the scalp to modulate nearby brain activity; it is typically used to dampen activity.
- Open-label: no placebo or blinded control group; everyone knew they were treated.
- Responder: a participant whose symptoms improved by a predefined amount.
- Electric field modeling: a computer estimate of where the magnetic stimulation actually reaches in the brain.
- Mutual information: a statistical measure of how much two patterns share. · level: research-level

<details><summary>Original abstract</summary>

Anhedonia is a hallmark of depression, involves disrupted positive affect (PA), and has been linked to hyperconnectivity between the dorsomedial prefrontal cortex (dmPFC) and nucleus accumbens (NAcc). In previous work, a single session of continuous theta burst stimulation (cTBS) to the dmPFC reduced NAcc-dmPFC functional connectivity (FC), with corresponding improvement in PA. We investigated whether cTBS to dmPFC plus PA-enhancing training is associated with decreased anhedonia, depression, and NAcc-dmPFC FC, and whether FC change corresponds to anhedonia improvement. Fifty youth (15-25 years) with current depression received cTBS (2x/day, 10 days, personalized dmPFC target) plus intersession PA training. Resting-state fMRI and symptom severity were collected pre/post cTBS+PA. In all, 42% of participants responded, and depression, anhedonia, and anxiety improved. Participants with greater decrease in FC experienced more improvement in anhedonia, although NAcc-dmPFC FC remained unchanged on average. Responders exhibited greater improvement than non-responders in anhedonia and anxiety but not FC. Additionally, mutual information modeling revealed that those with greater similarity between the actual target network (based on electrical field modeling) and the intended reward network exhibited a greater decrease in FC. cTBS+PA shows some promise as an intervention for anhedonic depression in youth, with individual differences in FC change relevant to clinical outcomes and precise network targeting a critical issue for modulating the intended network and achieving clinical improvement. Clinicaltrials.gov: NCT05487885

</details>

## Oncology

Nothing notable this time.

## Health informatics and medical AI

### [Using a large language model as the primary coder in health content analysis: a verification framework, per-variable reliability and proposed reporting items.](https://www.medrxiv.org/content/10.64898/2026.11.16.26368259v1)
*Ozakinci, G.; Schlegel, I.* · `health informatics` · medRxiv doi:10.64898/2026.11.16.26368259 v1 · relevance 0.08

- **In one sentence**: A proposed framework and reporting checklist (18 items) for using a large language model as the main coder in health content analysis of Instagram and TikTok posts, with per-variable reliability checks against independent human coding.
- **In plain words**: Researchers often study health claims on social media by having people read and label thousands of posts. This paper describes using a large language model (an AI text system) to do that labelling instead, and checking its work against human coders. Most variables matched human judgement well, but those requiring graded judgement did not, and the authors suggest the AI likely undercounts misinformation.
- **Why it matters**: As AI tools are increasingly used to code research data, there is no shared standard for reporting how well they performed, so this paper's attempt to set out what to check and report may be useful to other researchers. The worth of the proposed checklist will depend on whether other fields adopt it, which the text does not show.
- **Background needed**: - Content analysis: a research method where trained coders read material (here, social media posts) and assign labels to each item according to a written instrument.
- Coder agreement: how often two coders give the same label; the paper uses Gwet's AC1, a chance-corrected agreement statistic chosen because the outcome categories were very uneven (skewed).
- Calibration: refining the coding rules until human coders agree; here two ambiguous rules were rewritten and agreement on the main outcome rose from 0.456 to 0.977.
- Reliability threshold: a pre-set cut-off (0.80 here) below which a variable is treated as unreliable and reported only as exploratory.
- Large language model (LLM): an AI system trained on text that generates and classifies language; the paper notes its outputs cannot be reproduced computationally in the way a fixed script can.
- Enriched sample: a deliberately over-selected subset of items (here, outcome-heavy posts) used to test performance where the target cases are rare. · level: intermediate

<details><summary>Original abstract</summary>

Objective: To describe and evaluate a framework for using a large language model (LLM) as the primary coder in health content analysis, and to propose reporting items for LLM assisted studies, because no reporting standard exists. Methods: An LLM coded 6,982 Instagram and TikTok posts using a human written, human calibrated instrument. The framework has six components: human authorship of the instrument; two round human calibration; source discipline; quote anchored coding; verification in a representative and an outcome enriched sample, blinded in both directions; and per variable reliability reporting against a prespecified threshold, with the consequence of failure fixed in advance. Agreement was measured with Gwets AC1, prespecified because the outcome distribution was heavily skewed. Results: Agreement between the two human coders on the primary outcome rose from AC1 0.456 to 0.977 after two ambiguous rules were rewritten. LLM human agreement was 0.847 in the representative sample (N = 150) and 0.868 in the enriched sample (N = 50). Five of eight conditional variables fell below the 0.80 threshold and became exploratory: variables asking whether a defined textual feature was present met it, whereas those requiring graded judgement did not. The human coder identified misinformation more often than the LLM, so prevalence estimates are likely underestimates. Agreement on female targeting was lower for self-identified ethnic minority creators (0.744 versus 0.902). Conclusion: LLM coding cannot be computationally reproduced, so its reliability must be shown empirically: per variable agreement with independent human coding, the direction of remaining error, and a prespecified response to shortfall. The authors propose 18 reporting items for LLM assisted content analysis.

</details>

### [ClinDataBench: Benchmarking Large Language Model Agents in Clinical Trial Analysis Dataset Construction](https://www.medrxiv.org/content/10.64898/2026.11.17.26368316v1)
*Li, Z.; Luo, Y.; Feng, Y. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.17.26368316 v1 · relevance 0.08

- **In one sentence**: ClinDataBench is a benchmark that tests LLM coding agents on building CDISC ADaM analysis datasets, Define-XML metadata, and a reproducible rebuild program from SDTM clinical trial data and a statistical analysis plan, scored by a standard validator plus separate checks of derivation correctness, in an exploratory pilot with six models.
- **In plain words**: Before a new drug is approved, the FDA reviews trial results that are packaged as standardized data tables, which programmers currently build by hand from raw trial data and a written analysis plan. This paper asks whether AI coding agents could do that job, and builds a test using a public pilot study to check their output. In a small pilot with six models, most closed models and one open model produced all the required datasets, but a package with the fewest validator warnings still got a key set of calculations wrong, so the warning count alone is not a reliable measure of correctness.
- **Why it matters**: Regulatory submissions depend on these datasets being right, so an honest measure of whether AI agents can produce them matters for how the pharmaceutical industry might adopt such tools. The finding that a clean validator report can hide wrong calculations is a useful caution for anyone judging AI output by automated checks; the pilot is small and exploratory, so its results should not be read as settled.
- **Background needed**: - CDISC: a set of data standards used for clinical trial data submitted to regulators such as the FDA.
- SDTM and ADaM: SDTM holds raw, standardized trial data; ADaM holds the analysis-ready datasets derived from it.
- SAP (statistical analysis plan): the written document that specifies how trial results are to be calculated.
- Define-XML: a machine-readable file describing the variables and derivations in the datasets.
- Validator (Pinnacle 21 Community): software that checks datasets against the standard's structural rules; it does not check whether each value is computed correctly.
- LLM agent: a large language model that runs multi-step tasks, such as writing and running code, in a sandboxed environment.
- Self-Refine and CRITIC: revision strategies where a model improves its own output, with CRITIC using a validator report as feedback. · level: research-level

<details><summary>Original abstract</summary>

A new drug reaches patients only after the U.S. Food and Drug Administration (FDA) has reviewed its trial evidence, which every application carries as analysis datasets in the Clinical Data Interchange Standards Consortium (CDISC) Analysis Data Model (ADaM) format that programmers derive by hand from raw trial data, a statistical analysis plan (SAP) and dataset specifications. Coding agents built on large language models (LLMs) could take over this work, and a slow-changing industry will adopt them only with evidence of what they get right and wrong. However, work on large language models (LLMs) for CDISC data stops short of evaluating a complete, conformant and reproducible package, and the standard validator checks structure rather than whether each value is derived correctly. We introduce ClinDataBench, built on the public CDISC pilot study: an agent receives 22 Study Data Tabulation Model (SDTM) domains, the statistical analysis plan (SAP) and specifications, and must deliver 13 Analysis Data Model (ADaM) datasets, Define-XML metadata and a program that rebuilds them offline. Agents run in containers whose only network route is their model API, restricting online access to published reference outputs during execution. A host-only evaluator scores conformance under the Pinnacle 21 Community (P21) validator, selected derivations, clean reconstruction and effort separately. We compare three settings: Base, which submits the agent's first package; Self-Refine, which revises it without external validation feedback; and CRITIC, which revises it with the agent's own validator report. In an exploratory pilot with six models, the three closed models and DeepSeek delivered all 13 datasets in every setting and eleven of their twelve packages rebuilt semantically, while two other open-weight models delivered no complete package. Validator findings ranged from 15 to 64 dataset-rule pairs. Four of six CRITIC workflows had usable validator comparisons, and each reduced its finding count. None reduced its failed derivation count. The package with the fewest findings carried none of the 234 efficacy summary records in the form the specifications define, showing that lower validator finding counts do not necessarily indicate more correct derivations.

</details>

## Econometrics and applied economics

### [The Rise of Agents and the Human Labor Market](https://arxiv.org/abs/2611.27210)
*Nicola Borri, Anton Cheremukhin, Yukun Liu et al.* · `econ.GN` · arXiv:2611.27210v1 · relevance 0.08

- **In one sentence**: Using OpenRouter token-consumption data and Lightcast job-posting text, the paper estimates how firm-level exposure to aggregate agentic AI usage, measured via stock-return comovement, predicts subsequent declines in U.S. job-posting growth, including an event study around the Claude Code 2.0 release.
- **In plain words**: The paper asks whether AI "agents" (AI systems that carry out multi-step tasks on their own) are reducing how many jobs companies advertise. It builds a firm-level exposure score by checking how each public company's stock moves with weekly total agentic AI usage, then compares that with changes in job postings. It finds that firms more exposed to agentic AI post fewer new jobs in the following months, with the drop concentrated in non-senior roles.
- **Why it matters**: Labor-market effects of AI are a major open question for economists and policymakers, and this is one of the first attempts, as the authors claim, to measure economy-wide agentic AI effects across many AI models. The results are correlational and rest on the authors' own constructed measures, so they should be read as suggestive evidence rather than settled causal proof.
- **Background needed**: - Job postings: online job advertisements; their growth is a common early signal of hiring demand.
- Agentic AI: AI systems that plan and execute multi-step tasks with limited human input, as opposed to single question-and-answer use.
- Tokens: the units of text that AI models process; total token consumption is a proxy for how much AI is being used.
- Stock-return comovement ("beta"): how much a firm's share price moves together with a market-wide factor; here the factor is aggregate agentic AI usage.
- Event study: comparing outcomes before and after a specific event, here the release of Claude Code 2.0.
- Standard deviation: a unit describing typical spread; "one-standard-deviation higher exposure" means a moderately large change in the score. · level: research-level

<details><summary>Original abstract</summary>

We provide the first economy-wide and cross-AI model evidence on the effects of agentic AI on labor demand. We combine proprietary OpenRouter data covering about two quadrillion tokens of realized AI consumption (2 percent of global AI token consumption) across more than 400 AI models, including 1.1 quadrillion agentic tokens, with the full text of 34.8 million U.S. job postings for public firms from Lightcast. We compute our measure of firm-level exposure to aggregate agentic AI consumption (agentic beta) using the comovement of U.S. public firms' stock returns with realized weekly aggregate agentic AI token consumption. We find that a one-standard-deviation increase in a firm's exposure to agentic AI predicts 2.11 percent lower growth in job postings over the next six months and 3.20 percent over nine months. We then conduct an event study based on the release of Claude Code 2.0, which significantly expanded the capabilities of AI agents, and show that a one-standard-deviation higher pre-release exposure to agentic AI predicts 4.73 percent lower posting growth over six months post the release. Furthermore, we show that the decrease in job postings is concentrated among non-senior jobs and is statistically insignificant for senior jobs. In contrast, we find no statistically significant relation between broad AI realized consumption exposure and subsequent job posting growth once agentic exposure is controlled for. Finally, we validate our market-implied agentic exposure measure using independent evidence from firms' mentions of AI deployment in securities filings and earnings calls.

</details>

### [Partially Identified Ambiguity](https://arxiv.org/abs/2602.07634)
*Cheaheon Lim* · `econ.TH` · arXiv:2602.07634v3 · relevance 0.06

- **In one sentence**: The paper asks whether conditional Gamma-minimax (a robust Bayesian rule that conditions on observed data) satisfies Aumann plausibility under partial identification, and characterizes when it does via a "partially identified ambiguity" condition on the prior set.
- **In plain words**: Economists often model a situation with a set of possible beliefs instead of a single belief, especially when the data cannot pin down a parameter exactly. This paper asks whether it is sound to update that set of beliefs by conditioning on the observed data. The authors find that this update can break a set-valued version of the rational-expectations requirement, and that the requirement holds only under a specific structural condition on the set of beliefs.
- **Why it matters**: It bears on how robust Bayesian methods should be applied when data only partly identify a parameter, a common situation in econometrics. The text does not show how widely the recommendation would change practice, so its practical reach is uncertain from the abstract alone.
- **Background needed**: - Partial identification: data narrow a parameter to a set of values (the identified set), not a single value.
- Prior set and robust Bayesian analysis: instead of one prior belief, the analyst uses a set of priors and judges decisions by their worst case.
- Gamma-minimax: a decision rule that picks the action with the best worst-case expected payoff across the prior set.
- Conditioning on data: updating beliefs after observing data, as in Bayes' rule.
- Aumann expectation: the average of random sets, a set-valued generalization of expectation.
- Aumann plausibility: a set-valued analogue of the rational-expectations property, meaning beliefs conditioned on data should agree with the ex ante view in an appropriate sense. · level: research-level

<details><summary>Original abstract</summary>

This paper addresses the normative question of whether one should condition on the data when performing robust Bayesian analysis under partial identification. We provide an ex ante representation of the conditional Gamma-minimax criterion and show that it can violate Aumann plausibility, a set-valued generalization of the rational expectations property. Our main characterization result establishes that Aumann plausibility holds if and only if the decision maker's prior set exhibits partially identified ambiguity. The latter condition requires the prior set to equal the Aumann expectation of a random set of distributions supported on the parameter's identified sets. We interpret these results as suggesting that conditional Gamma-minimax should only be used under partially identified ambiguity. The implications for various robust Bayesian methods are discussed.

</details>

## Economic theory

### [Exchange rights and vacancy priorities](https://arxiv.org/abs/2611.27684)
*\"Ozg\"un Ekici, M. Bumin Yenmez* · `econ.TH` · arXiv:2611.27684v1 · relevance 0.05

- **In one sentence**: The paper studies strategy-proof, individually rational allocation rules for policies that combine permitted position exchanges with priority-based allocation of announced vacancies, and introduces a "propose-and-trade" rule that protects exchange rights and vacancy priorities.
- **In plain words**: The paper looks at how institutions such as school or job assignments can let people swap positions while also filling newly opened seats according to priority rankings. It asks when a fair, hard-to-game procedure can exist for this mixed setting. The authors propose a new procedure, "propose-and-trade," and show it works whenever the rules contain no conflict cycles, a kind of circular clash between priorities and swap permissions.
- **Why it matters**: Many real allocation systems mix swaps with priority-based vacancy filling, so a clear characterization of when a non-manipulable rule can protect both kinds of claims is useful for designing them. The text says the axioms also characterize deferred acceptance and top trading cycles in their classic settings, which connects the work to two well-known matching mechanisms; the wider practical impact is not established by the abstract.
- **Background needed**: - Allocation mechanism: a rule that assigns positions to participants based on their reported preferences.
- Strategy-proof: no participant can gain by misreporting their preferences.
- Individually rational: no participant ends up worse off than their starting position.
- Priorities: rankings that decide who gets a vacancy when several people compete for it.
- Deferred acceptance and top trading cycles: two classic mechanisms for matching and trading, used as benchmarks here.
- Core allocation: an assignment that no group of participants could improve by forming its own exchanges.
- Conflict cycle: a circular chain of exchange permissions and priorities that clash, making a clean rule impossible. · level: research-level

<details><summary>Original abstract</summary>

Many institutions let incumbents exchange positions while allocating announced vacancies by priority, withdrawing positions released by vacancy recipients. A policy specifies permitted exchanges, vacancy eligibility, and priorities. A strategy-proof, individually rational rule protecting exchange rights and vacancy priorities exists precisely for policies without conflict cycles. Restricting protection to first choices does not enlarge this class. We introduce the propose-and-trade rule, which satisfies these properties and selects the applicant-optimal core allocation under every conflict-free policy. We identify when propose-and-trade is the unique strategy-proof, individually rational rule protecting first choices. These axioms characterize deferred acceptance and top trading cycles in their classic settings. Under a policy with a conflict cycle, propose-and-trade is manipulable but protects exchange rights and first-choice claims. Replacing it with any strategy-proof rule makes some applicant worse off at some profile. We show when priority reform alone can eliminate conflict cycles and when eligibility or exchange permissions must change.

</details>

## Game theory and algorithmic economics

### [Stinespring's Dilation, Universal-NOT, and Limitations of Quantum Uncoupled Learning](https://arxiv.org/abs/2611.27251)
*Emmanouil-Vasileios Vlatakis-Gkaragkounis, Pucheng Xiong* · `quant-ph` · arXiv:2611.27251v1 · relevance 0.09

- **In one sentence**: The paper shows that quantum versions of uncoupled learning dynamics (players who see only their own payoff and update quantum strategy states through physically valid channels) cannot reach Nash equilibrium in certain conjugation games without some memory, and characterizes when small classical or quantum memory helps.
- **In plain words**: The paper studies how two players, each choosing a quantum state as their strategy, can learn toward a stable outcome when each only sees the other's current state and their own payoff. It shows that in a specific family of games, a memoryless update rule that must be physically realizable cannot make the learner reach the equilibrium. It also shows that a small amount of classical memory fixes this for any finite set of target strategies, but no finite memory suffices for all possible pure qubit targets.
- **Why it matters**: It identifies a concrete case where the physical requirement that quantum updates be realizable, not just the lack of information, blocks learning, which matters for decentralized learning in quantum systems. The text does not show links to specific applications, so the broader significance is uncertain.
- **Background needed**: - Nash equilibrium: a set of strategies where no player gains by changing alone.
- Uncoupled learning: each player updates using only their own payoff, not the opponent's full strategy or payoffs.
- Qubit: the quantum analogue of a bit; a pure qubit state is a point on a sphere of possible states.
- Quantum channel: a physically allowed way to transform a quantum state (it must be consistent with quantum mechanics).
- Stinespring's dilation theorem: a result stating that any physical channel can be realized by adding an environment and applying a unitary (reversible) operation.
- Universal-NOT: an operation that tries to flip an unknown quantum state; its best achievable accuracy is limited by quantum mechanics (the Bužek, Hillery, Werner bound).
- Conjugation game: a game where the best response for one player is the transpose of the other's strategy. · level: research-level

<details><summary>Original abstract</summary>

Uncoupled learning, in which players know only their own payoff, are a standard model of decentralized learning toward Nash equilibrium. We study their quantum counterpart, where strategies are quantum states and, in each round, a player receives a physical copy of their opponent's current strategy and updates their own state by a quantum channel. This adds to uncoupledness a constraint with no classical analogue: every update must be physically realizable. In fact, this constraint is decisive in conjugation games, in which Bob has a strictly dominant pure strategy and Alice's unique best response is its transpose. In this work, we show some limitations of uncoupled (learning) dynamics in finding the Nash equilibrium for conjugation games. First, we prove that no autonomous, memoryless, uncoupled dynamics converge to Nash equilibrium in a family of four single-qubit conjugation games. Specifically, any memoryless channel that keeps all four equilibria fixed will leave Alice's strategy frozen. This result also extends to $4^n$ games on $n$-qubit registers. Second, we show that this barrier disappears with a small classical memory: for any finite family of $L$ pure targets, a guess-and-test rule with $O(\log L)$ classical bits converges to equilibrium, with an explicit bound on its convergence rate. Finally, we prove that no finite memory, classical or quantum, suffices for the continuum of all pure-qubit targets. Our proof of the impossibility for memoryless channels relies on Stinespring's dilation theorem, while the impossibility for finite-memory channels relies on the optimal universal-NOT (in)fidelity bound by Bu\v{z}ek, Hillery, and Werner.

</details>

### [Learning under Bounded Manipulation for Quadratic Incentive Design](https://arxiv.org/abs/2611.26736)
*Arda G\"u\c{c}l\"u, Subhonmesh Bose, Tamer Ba\c{s}ar* · `cs.GT` · arXiv:2611.26736v1 · relevance 0.07

- **In one sentence**: A repeated quadratic incentive design game in which a leader estimates a follower's private type from noisy actions while the follower strategically deviates to manipulate those estimates, with a minimax regret bound of order max{log T, min{C_T, T}} under a manipulation budget C_T.
- **In plain words**: A "leader" (for example, a principal setting pay or rewards) tries to learn something private about a "follower" (an agent) by watching what the follower does, then sets incentives based on that guess. The follower knows how the leader learns, so he can act slightly differently from his best short-term choice to steer what the leader concludes later. The paper measures how much this manipulation costs the leader and shows how that cost scales with how much the follower is allowed to manipulate.
- **Why it matters**: It addresses a practical concern in learning-based incentive design: an agent who knows the learning rule can game it, so a learner's performance depends on the agent's strategic ability and not only on noise. The text does not say how it relates to specific applications, so its wider significance beyond this model is unclear.
- **Background needed**: - Incentive design (Stackelberg-style game): a leader commits to a rule, and a follower responds to maximize his own payoff.
- Quadratic/affine incentive rule: the leader's payment is a linear function of the follower's action, with the leader's estimate of the follower's type as a parameter.
- Regret: how much worse a learner does compared with an oracle that knows the true private type from the start; minimax regret is the best worst-case guarantee over all policies.
- Manipulation budget C_T: a cap on the total squared deviation the follower may add over T rounds, beyond his myopic best response.
- Log T rate: the usual slow growth of error for learning from noisy data; the extra term shows the cost of manipulation.
- Information-theoretic lower bound: a limit that holds for any policy, no matter how clever, given the information available. · level: research-level

<details><summary>Original abstract</summary>

We study a repeated quadratic incentive design game in which a leader learns a follower's private type from noisy observations of the follower's actions and uses her estimates in an affine incentive rule. The follower knows the leader's learning policy, which incorporates past observations to produce estimates of the follower's type, and can deviate from his myopic best response to influence the leader's future estimates. We ask how the follower's ability to manipulate these observations affects the leader's performance. Under a manipulation budget $C_T$ constraining the expected cumulative squared deviation of the follower's actions from his myopic best response, we establish a minimax regret rate of order $\max\{\log T, \min\{C_T,T\}\}$ for approximately rational followers. Our information-theoretic lower bound applies to a general class of causal estimation and manipulation policies for the leader and the follower. We provide a simple learning policy that achieves the lower bound. Finally, we show that under a fixed learning rule, increasing the manipulation budget of the follower can counterintuitively reduce the leader's regret.

</details>

## Mathematical finance

### [A Solvency II-Based Framework for Pricing Structural Longevity Risk under an Affine Mortality Model](https://arxiv.org/abs/2611.26670)
*Madiha Bouhouche (INSEA), Said Khalil (TREE, INSEA) et al.* · `q-fin.PR` · arXiv:2611.26670v1 · relevance 0.05

- **In one sentence**: The paper proposes a Solvency II Cost-of-Capital pricing framework for structural longevity risk, using a continuous-time affine mortality model with a latent longevity factor, closed-form survival probabilities, and a comparison of trend-based versus mortality-level stress scenarios on Belgian data.
- **In plain words**: The paper looks at how an insurer or pension provider should put a price on the risk that people live longer than expected, a risk that can't easily be removed by trading in the market. The authors build a model of how mortality rates change over time and use it to estimate the capital an insurer must hold against that risk under European insurance rules. They find that the size of the capital charge depends strongly on how the adverse scenario is defined: a stress applied to mortality levels gives much larger capital-cost figures than a stress applied to the long-term trend.
- **Why it matters**: Longevity risk affects pensions and annuities worldwide, and how regulators and insurers price capital against it matters for their solvency. The text's main takeaway is that the choice of adverse scenario changes the result considerably, which is a useful caution for practitioners; the text does not say how the approach would perform beyond the Belgian application shown.
- **Background needed**: - Longevity risk: the danger that people live longer than an insurer or pension fund assumed, so payments last longer than planned.
- Solvency II: the European insurance regulatory regime that requires insurers to hold capital against risks.
- Best Estimate: the probability-weighted present value of future cash flows.
- Risk Margin and Cost-of-Capital: an extra amount added to reserves, equal to the cost of holding the capital required for non-hedgeable risk.
- Solvency Capital Requirement (SCR) and Value-at-Risk (VaR): the capital buffer needed to survive a severe loss, and a standard measure of how large that loss could be at a given confidence level.
- Affine mortality model: a mathematical model in which the mortality rates depend linearly on hidden (latent) factors, which keeps calculations tractable.
- Stress test: a deliberately adverse scenario used to see how a result changes under pressure. · level: research-level

<details><summary>Original abstract</summary>

This paper develops a Solvency II-based pricing framework for structural longevity risk in incomplete longevity markets. The valuation scheme relies on the Cost-of-Capital principle underlying the Risk Margin and combines it with a continuous-time affine mortality model. Mortality dynamics are specified in calendar time, with age-dependent mortality patterns linked to a latent longevity factor driving long-term mortality improvements. The affine structure preserves closed-form survival probabilities and provides a tractable basis for repeated Best Estimate, Solvency Capital Requirement and Risk Margin calculations. We derive the conditional distribution of one-year discounted Best Estimate variations, obtaining analytical expressions for their asymmetry and Value-at-Risk under the Gaussian affine specification. Within this setting, we introduce a stress-based assessment by applying adverse shocks to the deterministic parameters governing the longevity trend. The trend-based stress is compared with a mortality-level stress and with a Value-at-Risk-based capital assessment. The methodology links stochastic mortality modelling, prudential capital valuation and longevity-linked payoff assessment within a unified actuarial framework. A numerical application based on Belgian mortality data illustrates the implementation and shows that the mortality-level stress produces substantially larger scenario-based capital-cost measures than the trend-based stress. These findings highlight the sensitivity of longevity risk valuation to the specification of adverse mortality scenarios. The approach offers a transparent and operational basis for assessing and pricing structural longevity risk under a Solvency II Cost-of-Capital perspective.

</details>

### [Risk sharing for background risk models with infinite mean](https://arxiv.org/abs/2611.27485)
*Ziting Miao, Yuyu Chen, Han Li* · `q-fin.RM` · arXiv:2611.27485v1 · relevance 0.04

- **In one sentence**: The paper studies when risk sharing among dependent infinite-mean losses, under linear and conditional mean sharing with background risk models, increases risk in the usual stochastic order, and compares diversified portfolios built from Pareto marginals and Archimedean copulas.
- **In plain words**: The paper asks whether pooling and splitting a risk among several parties always helps, as it usually does when risks are independent and have a finite average size. It focuses on losses so extreme that their average is infinite, and where the losses move together. The authors show that in these cases sharing can make the overall risk larger, and they state conditions under which keeping the original risk or a less spread-out portfolio is preferred.
- **Why it matters**: Standard advice that diversification reduces risk may fail for heavy-tailed losses, which matters for insurance, reinsurance and catastrophe planning. The text does not say how these results would be applied in practice, so the practical reach is uncertain.
- **Background needed**: - Risk sharing: dividing a random loss among several agents, for example by splitting it linearly or by having each pay a conditional expected share.
- Infinite mean: a loss whose long-run average is unbounded, so very large losses are common enough to dominate averages.
- Stochastic order: a way of saying one random quantity tends to be larger than another across all thresholds.
- Positive dependence: losses that tend to be large or small together.
- Copula: a function that describes how dependent variables are linked, separate from their individual distributions.
- Pareto and Archimedean copulas: common heavy-tailed distribution and dependence families used in these models.
- Background risk: an extra unshared risk that each agent faces alongside the risk being shared.
- Law-invariant monotone risk measure: a rule for assigning a risk score that depends only on the loss distribution and increases with losses. · level: research-level

<details><summary>Original abstract</summary>

Risk sharing is usually viewed as beneficial for risk-averse agents facing independent risks with finite means, but this situation can be reversed for infinite-mean losses. In this paper, we explore the effects of risk sharing for positively dependent infinite-mean losses using background risk models. Under both linear and conditional mean risk sharing, we show that risk sharing of infinite-mean losses can increase the risk in the sense of usual stochastic order. Our results cover classical multivariate loss distributions, including the Pareto-Clayton and the Fr\'echet-Gumbel models. For linear risk sharing, we further derive stochastic dominance relations between diversified portfolios, including those with Pareto marginals coupled by convex mixtures of commonly used Archimedean copulas. For conditional mean risk sharing, we additionally discuss peakedness and stochastic order relations for stable distributions. Consequently, under the stated conditions, retaining the original risk or a less diversified portfolio is preferred under every law-invariant monotone risk measure that is well defined for infinite-mean models.

</details>

## Financial markets

### [Nonlinear Shrinkage for Higher Moments Estimation in Large Portfolios](https://arxiv.org/abs/2611.27274)
*Paul Ruelloux, Christian Bongiorno, Damien Challet* · `q-fin.PM` · arXiv:2611.27274v1 · relevance 0.07

- **In one sentence**: The paper extends covariance-cleaning filters (cross-validated shrinkage and the Average Oracle approach) to even-order co-moment tensors, such as cokurtosis, and tests them on large equity portfolios drawn from Russell 1000 constituents.
- **In plain words**: Investors care about more than how much a portfolio's returns vary; they also care about how often extreme moves happen, which depends on relationships among many assets at once. Those relationships are estimated from historical data, and with many assets the estimates are very noisy. The authors propose cleaning these estimates using tensor decompositions (a way of organizing multi-way tables of numbers), and they report that the cleaned estimates are more accurate out of sample than the raw ones.
- **Why it matters**: Portfolio risk models that ignore higher moments can misjudge the chance of large losses, so more reliable estimates matter for large-scale risk management and portfolio construction. The text reports improvements on historical Russell 1000 data only, so how well the gains carry over to other markets or periods is not shown here.
- **Background needed**: - Variance measures how spread out returns are; covariance measures how pairs of assets move together.
- Higher moments add further risk measures: skewness (asymmetry) and kurtosis (how heavy the tails are, i.e., how often extreme outcomes occur).
- Coskewness and cokurtosis extend these to groups of assets, and are stored as multi-dimensional arrays called tensors.
- Shrinkage/covariance cleaning means adjusting noisy sample estimates toward more stable structure to reduce estimation error.
- Out-of-sample testing checks performance on data not used to build the estimate, which is the fair test of forecasting accuracy.
- Frobenius error is a standard way of measuring the overall size of the gap between an estimate and the target. · level: research-level

<details><summary>Original abstract</summary>

Portfolio risk is not limited to the variance of returns. The moments of portfolio returns depend directly on the covariance matrix and higher-order co-dependences (coskewness, cokurtosis, etc.). In practice, however, these objects are extremely noisy, especially for large portfolios. Here we introduce filtering methods based on tensor decompositions that extend cross-validated covariance cleaning and the Average Oracle methodology to even-order co-moment tensors. Using returns on historical Russell 1000 constituents, we find that the proposed filters improve out-of-sample estimation accuracy relative to sample estimators, both for correlation and cokurtosis tensors, as measured by relative squared Frobenius errors. These improvements translate into lower relative errors on portfolio volatility and kurtosis, and into lower out-of-sample volatility and kurtosis when the portfolio objective penalizes both variance and the fourth moment.

</details>

### [Are Calibrated Decision Models Calibrated on Markets? Geolocated News, Markov Switching and a System One Model for Nasdaq-100 Allocation](https://arxiv.org/abs/2611.26716)
*Jakub Zaj\k{a}c, Micha{\l} Dyrek* · `q-fin.ST` · arXiv:2611.26716v1 · relevance 0.04

- **In one sentence**: A test of whether a language-model-based probability forecaster (Jev) and a two-regime Markov-switching model are well calibrated on Nasdaq-100 four-week-ahead declines from January 2025 onward, with a half-Kelly allocation comparison.
- **In plain words**: The paper asks whether a tool that outputs probabilities for yes/no questions gives honest odds when used to decide how much of a stock index to hold. Every Friday the authors ask whether the Nasdaq-100 will close lower four weeks later, and compare several models over 88 weeks in 2025 and 2026. The main finding is that the raw forecasts are too pessimistic, and simply shifting them toward the historical base rate fixes most of the miscalibration, though no model beats the base rate at predicting direction.
- **Why it matters**: Position sizing depends on probabilities of loss, not just on predicting up or down, so whether a forecaster's stated odds match real outcomes matters for risk decisions. The paper is a single, fairly short test over one test window, so its specific numbers should be read as suggestive rather than settled.
- **Background needed**: - Calibration: a forecaster is well calibrated if events it gives a 30% chance happen about 30% of the time.
- Expected calibration error (ECE): an average gap between stated probabilities and observed frequencies; lower is better.
- Base rate: how often the event happens historically (here, about 4% for declines over 10%).
- Markov-switching model: a statistical model that assumes the market alternates between hidden regimes, such as calm and turbulent.
- Platt scaling and isotonic regression: standard methods that recalibrate raw probabilities using past outcomes.
- Half-Kelly allocation: a position-sizing rule based on expected edge and odds, scaled down by half to reduce risk.
- AUC: a score from 0 to 1 for how well a model ranks risky cases above safe ones; 0.5 is no better than chance.
- PostGIS: a geographic database extension used to build location-based news features.
- Sharpe ratio: return earned per unit of risk taken. · level: research-level

<details><summary>Original abstract</summary>

Portfolio allocation is driven by probabilities of losses, not only by forecasts of the direction (up/down) of the market. A decision model such as Jev returns a probability for a yes/no question and has been reported to be well calibrated on a set of benchmarks. However, the model's calibration against realised market outcomes has not been tested. In this study, every Friday we ask whether the Nasdaq-100 will close lower four weeks later and compare a two-regime Markov-switching model estimated on data from 1990 to 2026, Jev reading weekly headlines and geolocated news features computed with spatial queries in PostGIS, and their combination. A knowledge probe shows that Jev knows events up to late 2024, so we evaluate it on 88 weeks from January 2025 onwards. None of the models predicts the direction better than the historical base rate. A key finding is that raw Jev overestimates the probability of a decline: its mean forecast is 0.48 against an observed frequency of 0.38, and its ECE is 0.10. A prior shift to the historical base rate, which uses no outcomes from the test period, lowers the ECE to 0.015. In contrast, Platt scaling, isotonic regression and the combination with the Markov model all make the forecasts worse. In a half-Kelly allocation, the raw Jev strategy returns 3.1% per year, whereas after the prior shift it returns 14.5%; a simple buy-and-hold strategy in QQQ returns 15.3% per year. The Markov model forecasts large declines (more than 10%) well, with an AUC of 0.81, and its strategy has the highest Sharpe ratio over 1999-2026. Asked about such a large decline (base rate 4%), raw Jev forecasts 16-24% on average, and the same prior shift removes this offset. The practical lesson is that decision-model probabilities must be anchored to the base rate of the market event before they are used to size positions.

</details>

## Signal processing

### [DNN-Assisted Deterministic Policy Learning for Adaptive IRS-NOMA-OWC Networks](https://arxiv.org/abs/2611.26742)
*Ahrar N. Hamad, Ahmad A. Qidan, Taisir E. H. El-Gorashi et al.* · `cs.IT` · arXiv:2611.26742v1 · relevance 0.07

- **In one sentence**: A two-stage deep neural network and deep reinforcement learning framework (DNN-DRL with a deterministic policy gradient method) jointly tunes power allocation and intelligent reflecting surface mirror orientations in an indoor IRS-assisted NOMA optical wireless network, with the decoding order updated online.
- **In plain words**: This paper looks at how to send data to several moving people in a room using light (optical wireless) instead of radio. A mirror-like panel (an intelligent reflecting surface) bounces light around obstacles, and the system must decide how much power to give each user and where to aim the mirrors. The authors use a neural network to estimate where users are and a learning-based controller to pick the settings, and report that it beats several baselines in sum rate and fairness while converging faster.</plain>
<parameter name="why">Light-based indoor links can be blocked when a person stands in the line of sight, so reflecting surfaces are one proposed fix. The text claims gains over standard reinforcement learning methods, conventional optimization and no-IRS setups, but these comparisons are only summarized in the abstract, so the size and conditions of the gains are not clear from the text alone.</why>
<parameter name="background">- Optical wireless communication (OWC): sending data with visible or infrared light, such as LED lighting.
- Line-of-sight (LoS) blockage: a signal fails when something stands between transmitter and receiver.
- Intelligent reflecting surface (IRS): a programmable surface whose elements redirect signals toward receivers.
- Non-orthogonal multiple access (NOMA): several users share one channel at once, with power split between them and decoded in a set order.
- Sum rate and fairness: total data throughput across users, and how evenly it is shared.
- Quality of service (QoS): minimum performance each user must get.
- Deep neural network (DNN): a learned function that maps inputs (e.g., sensor data) to estimates.
- Deep reinforcement learning (DRL): a method where a controller learns good actions by trial and reward; deterministic policy gradient is one specific variant.
- Non-convex optimization: a hard problem with many local best answers, so standard solvers may struggle.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Intelligent reflecting surface (IRS) has been considered a promising technology in optical wireless communication (OWC) networks due to its potential to overcome the line-of-sight (LoS) blockage issue and enhance coverage. In this paper, a dynamic IRS-assisted indoor non-orthogonal multiple access (NOMA)-OWC network is modeled, and an optimization problem is formulated to maximize the sum rate subject to the quality-of-service (QoS) requirements of multiple mobile users, by jointly optimizing the power allocation and the IRS mirror orientations, from which the user's decoding order is induced rather than being fixed. Since the problem is non-convex and the channel conditions vary with user mobility, conventional optimization methods may incur considerable computational overhead. Therefore, a two-stage deep neural network-deep reinforcement learning (DNN-DRL) framework is proposed. In the first stage, the DNN estimates the user's positions and orientations in real time, removing the need for perfect knowledge of the user state. In the second stage, a deterministic policy gradient (DPG)-based DRL algorithm uses these estimates to jointly optimize the power allocation and IRS mirror orientations, with the decoding order updated according to the resulting effective channel gains. The results show that the proposed framework approaches the performance upper bounds and outperforms standard DRL algorithms, conventional optimization methods, and deployments without IRS in terms of sum rate and fairness, while achieving faster convergence. Furthermore, online adaptation of the decoding order maintains higher QoS satisfaction than a fixed decoding order, particularly under high user mobility.

</details>

### [From Pilots to Position: Experimental Near-Field Localization for ISAC](https://arxiv.org/abs/2611.27503)
*Yunxin Li, Emiel Vanspranghels, Jialun Kou et al.* · `eess.SP` · arXiv:2611.27503v1 · relevance 0.06

- **In one sentence**: An experimental study of near-field target localization using OFDM pilot signals from a distributed multi-transmitter, multi-receiver communication testbed, comparing coherent backprojection and noncoherent delay-TDOA fusion at 3.4 GHz.
- **In plain words**: The paper asks whether a wireless system built for communication can also work out where an object is, by reusing the reference signals it already sends. The authors built a test setup with two transmitters and four receivers and measured 16 fixed target positions. Both of their methods located the target to within about 19 cm on average.
- **Why it matters**: It offers real hardware measurements rather than only simulations, which helps show what accuracy communication-style signals can deliver in practice. It may matter for future wireless networks that need to sense their surroundings without dedicated sensing equipment, though the text reports only static targets and a single test setup.
- **Background needed**: - ISAC (integrated sensing and communication): using one wireless system to both send data and sense objects.
- OFDM: a common modulation scheme that splits a signal across many frequency slices.
- Pilot signals: known reference signals sent alongside data, used to estimate the radio channel.
- Near-field: the close range where the wave's curvature matters, so simple far-field angle models break down.
- Multistatic: several separated transmitters and receivers observing the same target.
- TDOA (time difference of arrival): locating a source from differences in arrival times at receivers.
- Coherent vs. noncoherent: coherent methods use the signal's phase, noncoherent ones use only its strength or timing.
- Backprojection: scoring each candidate location by how well it explains the measured signals. · level: intermediate

<details><summary>Original abstract</summary>

Integrated sensing and communication (ISAC) enables wireless systems to reuse communication signals for environmental sensing, potentially reducing the need for dedicated sensing resources. However, the achievable localization accuracy of communication-centric waveforms under practical hardware constraints remains an important challenge. In this paper, we experimentally investigate near-field target localization using OFDM pilot signals in a distributed communication system. We consider both coherent and noncoherent localization approaches, exploiting multistatic propagation delays and time-difference-of-arrival (TDOA) information extracted from pilot-based channel estimates. A hardware setup comprising two transmitters and four receivers was developed and configured to operate at 3.4 GHz with 198 MHz occupied bandwidth to evaluate localization performance under realistic propagation and synchronization conditions. Experimental results across 16 static target positions demonstrate mean localization errors of 19.8 cm and 18.8 cm for coherent backprojection and noncoherent delay-TDOA fusion, respectively. Furthermore, we investigate the impact of occupied bandwidth on localization accuracy of the two proposed algorithms. These findings provide experimental insights into the capabilities and practical limitations of OFDM pilot-based sensing, supporting resource-efficient localization in future ISAC systems.

</details>

## Audio and speech

### [PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions](https://arxiv.org/abs/2611.27601)
*Sulong Yang, Zhi Zeng, Xiupeng Wu et al.* · `cs.SD` · arXiv:2611.27601v1 · relevance 0.11

- **In one sentence**: PromptTTSD is an open-source spoken dialogue synthesis model that generates multi-turn, multi-speaker conversational speech with open-ended natural-language style control and zero-shot voice cloning, trained on a new dataset (PromptDialog) extracted from multi-narrator audiobooks.
- **In plain words**: Current systems that turn written dialogue scripts into spoken conversations struggle to make each line sound right for its context, such as shifting tone as a conversation changes. This paper builds a large dataset by pulling conversational speech out of audiobooks and using an AI language model to write style descriptions from the surrounding story text, then trains a speech model on it. The authors report that the resulting model keeps basic speech quality high, competes with proprietary systems on following free-form style instructions, and fits the context of multi-turn dialogues better.
- **Why it matters**: Making synthetic speech follow open-ended style instructions in conversation is a practical goal for audiobooks, games, and virtual assistants. The text gives only the paper's own comparisons, so how well the gains hold in independent or real-world use is not established.
- **Background needed**: - Text-to-speech (TTS): software that generates spoken audio from written text.
- Spoken dialogue synthesis: producing a multi-turn conversation between several voices from a script.
- Zero-shot voice cloning: copying a voice from a short sample without extra training for that voice.
- Style prompt: a natural-language description such as "tired, quiet voice," used to steer how speech sounds.
- Forced alignment: matching written text to timestamps in recorded audio so the speech can be cut into pieces.
- Audiobook data: used here as a source of paired text and speech, where narration describes how lines are spoken.
- Proprietary models: commercial systems whose internals are not public, used here as comparison points. · level: research-level

<details><summary>Original abstract</summary>

Spoken dialogue synthesis aims to generate multi-turn conversational speech from dialogue scripts while maintaining speaker consistency and contextual appropriateness. However, existing models largely lack fine-grained controllability, which is critical for capturing the dynamic, context-dependent style shifts in natural conversations. While prompt-based TTS has enabled such control for single-speaker speech, existing datasets heavily rely on predefined tags, which fundamentally limits their capacity to capture open-ended styles. To address this gap, we propose a scalable pipeline for extracting conversational speech from multi-narrator audiobooks, featuring an improved two-stage alignment algorithm to preserve dialogue continuity, paired with LLM-based extraction of style descriptions directly from narrative text. We release PromptDialog, a large-scale multi-speaker conversational speech dataset comprising 8,383 hours of Chinese speech and 120 hours of English speech, with open-ended style descriptions for 79% of utterances. We further introduce PromptTTSD, a spoken dialogue synthesis model built via a prompt-aware fine-tuning strategy that integrates style prompts into text-speech interleaved sequences. PromptTTSD is an open-source spoken dialogue synthesis model that supports both zero-shot voice cloning and natural language style control. Experiments demonstrate that PromptTTSD not only maintains strong fundamental synthesis capabilities but also achieves competitive open-ended style control compared with proprietary models, and substantially improves contextual appropriateness in multi-turn dialogues.

</details>

### [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784)
*Sivashankar Selvarajan, Piyush Verma, Sumit Kumar et al.* · `cs.SD` · arXiv:2611.27784v1 · relevance 0.09

- **In one sentence**: A company report introducing ARCAS 290M, a single frozen 290M-parameter detector for AI-generated speech, claiming zero-shot generalization across ten public benchmarks, commercial comparisons, and multiple languages and channels.
- **In plain words**: Cloning someone's voice now takes only a few seconds of recorded audio, and tools that spot fake speech often stop working when the fake comes from a different generator, phone line, or language. This paper describes a single detection model, ARCAS 290M, that its authors say works across many such conditions without being retuned for each test set. The authors report strong scores on public benchmarks and leaderboards, though the text gives only summary claims rather than the detailed numbers.
- **Why it matters**: Voice-cloning fraud and fake media are a practical concern for banks, platforms, and newsrooms, so a detector that holds up outside its training conditions would matter if the claims hold. The text is promotional and summary-level, so the results should be treated as the authors' claims until independent evaluation and full methods are available.
- **Background needed**: - AI-generated audio (deepfake speech): speech made by software that imitates a real person or invents a voice.
- Text-to-speech (TTS) and voice conversion: two ways of producing synthetic speech; codec language models are a newer generator type.
- Detector generalization: a detector trained on one dataset often performs worse on new generators, channels (phone, Bluetooth), or languages.
- Zero-shot: tested on data it was not specifically tuned for.
- Equal error rate (EER): a standard error score where lower is better; the rate at which genuine and fake items are mistaken equally often.
- Benchmarks and leaderboards: shared public test sets (e.g., ASVspoof5) and ranking sites used to compare systems.
- Foundation model: a large general-purpose model meant to be reused across many tasks. · level: intermediate

<details><summary>Original abstract</summary>

Voice cloning now needs only seconds of audio, and detectors tuned to one dataset often fail when the generator, channel, or language changes. We introduce ARCAS 290M, Neural Defend's foundation model for detecting AI-generated audio. A single frozen production model, with no benchmark-specific fine-tuning, generalizes across text-to-speech, voice-conversion, and codec-language-model generators, telephone and Bluetooth channels, recording conditions, and languages. We evaluate it on the complete official test sets of ten public benchmarks, scoring every recording exactly as released, and against commercial systems on independent leaderboards. ARCAS 290M ranks first among all systems on the Podonos leaderboard and has the lowest equal error rate among commercial detectors on ASVspoof5. It separates real from AI-generated speech almost perfectly on ASVspoof5, SpeechFake, and ShiftySpeech, and detects nearly all AI-generated speech in Hindi, Tamil, Bengali, and Telugu. On every benchmark with a published zero-shot comparison, including in-the-wild audio, partial fakes, and the conditions hardest for the field, it surpasses the strongest reported detector by a wide margin. These results establish ARCAS 290M as a general-purpose foundation for AI-generated audio detection in fraud prevention, platform safety, and media verification.

</details>

## Control systems

### [Learned Network Dynamics for Model Predictive Traffic Signal Control under Incidents](https://arxiv.org/abs/2611.27435)
*Dang Viet Anh Nguyen, Carlos Lima Azevedo, Tomer Toledo et al.* · `cs.LG` · arXiv:2611.27435v1 · relevance 0.17

- **In one sentence**: GNN-MPC is a receding-horizon traffic-signal controller that plans with graph-neural-network dynamics conditioned on signal actions, coordinates phases across intersections via approximate best responses with an acceptance test, and is evaluated under non-recurrent incidents in microscopic simulation.
- **In plain words**: This paper looks at how to time traffic lights in a city grid when an incident, such as a crash or lane closure, changes how traffic flows. The authors use a learned model of how queues respond to light changes, and they say the model must also see queues that stretch beyond the short lanes where sensors sit. In computer simulations, their controller cut travel time and completed more trips than the controllers it was compared against.
- **Why it matters**: Traffic signals are a practical case of controlling a networked system with hidden state, and the paper argues that both observing unmeasured queues and predicting how they respond to control matter. The results come from simulation only, so they show what the method does in those models rather than on real roads.
- **Background needed**: - Model predictive control (MPC): at each step, plan a sequence of future actions using a model, apply only the first action, then re-plan.
- Traffic signal phases: the set of green-light combinations that an intersection cycles through.
- Queues and store-and-forward models: simple traffic models that move vehicles in blocks through links; the paper uses calibrated versions as a baseline.
- Graph neural networks (GNNs): neural networks that operate on nodes (intersections, lanes) and their connections, so information passes between neighbors.
- Best-response coordination: each intersection picks its best phase given its neighbors' current choices; approximate versions are used for speed.
- MaxPressure: a known, fairly simple traffic-signal control rule used as a comparison point.
- Microscopic simulation: software that models each vehicle individually. · level: research-level

<details><summary>Original abstract</summary>

Model predictive control (MPC) of urban traffic signals relies on a model of how queues respond to signal decisions, which is hard to specify and calibrate in heterogeneous networks, particularly when incidents change capacities and turning shares. Measurements add a second limitation: the controlled lanes at the stop line are often short, so queues extending upstream of them fall outside lane-level measurements. We propose GNN-MPC, a receding-horizon controller that plans with action-conditioned network dynamics learned by graph neural networks. Phase sequences are coordinated across intersections by approximate best responses, with an acceptance test that keeps the predicted cost no higher than that of the initial plan. In microscopic simulation under non-recurrent incidents, GNN-MPC reduces travel time and increases completed trips relative to all tested controllers, on a homogeneous grid and a heterogeneous 21-intersection network. Controlled comparisons on the heterogeneous network distinguish the roles of observation and prediction. With nearly as many vehicles entering the network, GNN-MPC reduces travel time by 13% relative to MaxPressure with the same upstream measurement, and GNN-MPC without the upstream representation does not reproduce its performance. Under the same traffic measurements, planner and objective, replacing the learned dynamics with calibrated store-and-forward predictors increases travel time by 31-34%. Observing hidden demand and predicting its response to control are thus complementary requirements of network-level predictive control.

</details>

### [Nonholonomic Event-Triggered Source Seeking](https://arxiv.org/abs/2611.26802)
*Victor Hugo Pereira Rodrigues, Tiago Roux Oliveira, Miroslav Krstic* · `math.OC` · arXiv:2611.26802v1 · relevance 0.10

- **In one sentence**: The paper proposes an event-triggered source seeking controller for nonholonomic unicycle vehicles, separating continuous periodic probing from aperiodic updates of the seeking correction, with a time-periodic Lyapunov analysis giving practical exponential convergence and a positive minimum dwell time that excludes Zeno behavior.
- **In plain words**: The paper looks at how a robot vehicle can find the location of an unknown signal source (such as a peak of some field) while only updating its steering correction at certain moments, rather than all the time. The vehicle keeps making small probing movements continuously so it can sense which way the source lies, but it recalculates and sends its correction only when a trigger condition is met. The authors show that the vehicle gets to a neighborhood of the source and that the updates cannot pile up infinitely fast.
- **Why it matters**: Reducing how often a controller computes and transmits updates matters for vehicles with limited communication or processing power. The text claims the analysis also handles source fields whose curvature differs in different directions, which earlier Lie-bracket methods did not cover; the broader practical impact is not established in the text.
- **Background needed**: - Source seeking: steering a vehicle toward a peak of an unknown field using only measurements, without a map.
- Nonholonomic unicycle: a wheeled vehicle that cannot slide sideways, so its turning and forward motion are constrained.
- Gradient estimation: inferring the direction of increase of the field by wiggling the vehicle (probing) and demodulating the measured signal.
- Event-triggered control: updating the control only when a measured error crosses a threshold, instead of at fixed times, to save computation and communication.
- Zeno behavior: an unphysical case where triggers occur infinitely often in finite time; a positive minimum dwell time between triggers rules this out.
- Lyapunov function: a energy-like function used to prove that a system settles toward a target.
- Averaging / Lie-bracket analysis: approximation methods that treat fast periodic motion as an average effect. · level: research-level

<details><summary>Original abstract</summary>

This paper introduces an event-triggered source seeking control (ET-SSC) strategy for autonomous vehicles modeled as nonholonomic unicycles. The key feature of the proposed design is the separation between the continuous probing motion required for gradient extraction and the event-triggered update of the source-seeking correction. This separation enables aperiodic computation and transmission of the correction while the periodic probing signals remain continuously active. The triggering mechanism acts on a low-pass-filtered gradient estimate, obtained by high-pass (washout) filtering, demodulation, and low-pass filtering of the measured signal, and combines a relative and an absolute threshold. Stability is proved with a time-periodic Lyapunov function constructed along the exponentially stable periodic solution of the filtered closed loop, establishing practical exponential convergence of the vehicle to a neighborhood of the unknown source. The guaranteed minimum dwell time is strictly positive and independent of the probing frequency, which excludes Zeno behavior. Unlike available Lie-bracket analyses of the forward-velocity design, the proposed averaging-based analysis accommodates anisotropic quadratic source fields with distinct spatial curvatures. The resulting ET-SSC framework therefore provides a resource-aware implementation in which the source-seeking correction is updated aperiodically while the information-generating probing motion remains continuous.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 33 | 32 | 2 |
| Differential geometry | 20 | 20 | 2 |
| Partial differential equations | 57 | 57 | 2 |
| Harmonic analysis | 21 | 21 | 2 |
| Complex analysis | 12 | 12 | 2 |
| Operator algebras and spectral theory | 15 | 15 | 2 |
| Algebra | 29 | 29 | 2 |
| Representation theory | 19 | 19 | 2 |
| Number theory | 21 | 21 | 2 |
| Algebraic geometry | 24 | 24 | 2 |
| Topology | 13 | 13 | 2 |
| Dynamical systems | 17 | 17 | 2 |
| Combinatorics | 57 | 57 | 2 |
| Numerical analysis | 33 | 33 | 2 |
| Logic and foundations | 6 | 6 | 2 |
| Mathematical physics | 41 | 40 | 2 |
| Optimization and control | 36 | 35 | 2 |
| Statistics theory | 12 | 12 | 2 |
| Statistical methods and applications | 28 | 28 | 2 |
| AI industry news | 30 | 18 | 5 |
| Model architectures and training | 57 | 57 | 2 |
| Machine learning theory | 14 | 14 | 2 |
| Large language models | 58 | 58 | 2 |
| Computer vision | 132 | 132 | 2 |
| Reinforcement learning | 25 | 25 | 2 |
| AI safety and alignment | 30 | 30 | 2 |
| Interpretability | 7 | 7 | 2 |
| AI for mathematics | 9 | 9 | 2 |
| Robotics and embodied AI | 89 | 89 | 2 |
| Security and cryptography | 35 | 35 | 2 |
| Algorithms and complexity | 28 | 28 | 2 |
| Programming languages and formal methods | 19 | 19 | 2 |
| Systems and networking | 28 | 28 | 2 |
| Human-computer interaction | 14 | 14 | 2 |
| Information theory | 9 | 9 | 2 |
| High-energy theory and gravity | 48 | 48 | 2 |
| Statistical physics | 37 | 35 | 2 |
| Condensed matter | 52 | 51 | 2 |
| Particle physics | 45 | 45 | 2 |
| Nuclear physics | 16 | 16 | 2 |
| Quantum information and computing | 73 | 72 | 2 |
| Optics and atomic physics | 33 | 33 | 2 |
| Fluids and plasma | 22 | 22 | 2 |
| Biological physics | 3 | 3 | 1 |
| Climate, atmosphere and Earth | 5 | 5 | 2 |
| Cosmology | 12 | 11 | 2 |
| Galaxies | 29 | 27 | 2 |
| Exoplanets and planetary science | 13 | 10 | 2 |
| High-energy astrophysics | 19 | 17 | 2 |
| Stars and the Sun | 20 | 16 | 2 |
| Chemical physics | 12 | 10 | 2 |
| Materials science | 32 | 30 | 2 |
| Soft matter and polymers | 19 | 18 | 2 |
| AI for chemistry and materials | 17 | 13 | 2 |
| Biochemistry | 16 | 12 | 2 |
| Pharmacology and drug discovery | 5 | 4 | 0 |
| Computational and systems biology | 67 | 61 | 2 |
| Neuroscience | 68 | 62 | 2 |
| Genetics and genomics | 32 | 27 | 2 |
| Cell and molecular biology | 45 | 41 | 2 |
| Immunology and microbiology | 56 | 50 | 2 |
| Cancer biology | 34 | 30 | 2 |
| Ecology and evolution | 31 | 27 | 2 |
| Plant biology | 21 | 17 | 2 |
| Bioengineering and synthetic biology | 23 | 19 | 2 |
| Mathematical biology (arXiv) | 15 | 12 | 2 |
| Epidemiology | 18 | 14 | 2 |
| Infectious diseases | 5 | 1 | 0 |
| Public and global health | 12 | 8 | 2 |
| Psychiatry and neurology | 20 | 16 | 2 |
| Oncology | 7 | 3 | 0 |
| Health informatics and medical AI | 17 | 13 | 2 |
| Econometrics and applied economics | 4 | 3 | 2 |
| Economic theory | 3 | 3 | 1 |
| Game theory and algorithmic economics | 9 | 8 | 2 |
| Mathematical finance | 11 | 8 | 2 |
| Financial markets | 6 | 5 | 2 |
| Signal processing | 17 | 15 | 2 |
| Audio and speech | 8 | 6 | 2 |
| Control systems | 32 | 30 | 2 |

<!-- {% endraw %} -->
