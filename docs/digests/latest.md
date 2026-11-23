# Research digest · 2026-11-23
<!-- {% raw %} -->

New papers posted from about 2026-11-22 to 2026-11-23 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Overview and recent progress on the classical Bernoulli free boundary problem](https://arxiv.org/abs/2611.26636)** (Partial differential equations): This is an overview article about a mathematical problem where you must find a function and also the unknown edge of the region where that function lives. The problem is named after Bernoulli and is often described as one-phase, since only one side of the boundary carries the interesting behavior. The text itself is only a short summary; it says the survey covers the field with emphasis on recent progress, but does not list specific results.
- **[Autonomous quantum machine learning via Riemannian gradient-based optimization](https://arxiv.org/abs/2611.27815)** (Quantum information and computing): Most quantum machine learning today trains by repeatedly measuring a quantum device and feeding the results to a classical computer, which tends to be a bottleneck. This paper proposes a way to let the training update happen inside the quantum system itself, with no measurements or classical feedback during training. The authors report a convergence guarantee, an analysis of how circuit depth grows, and numerical tests showing the model can pick up a hidden symmetry in the data.
- **[Hidden Semi-Markov Models for Fully Functional Time Series](https://arxiv.org/abs/2611.26838)** (Statistical methods and applications): The paper studies data that arrive as whole curves over time, such as brain-wave recordings, where an unseen "state" drives the pattern and changes now and then. Standard models assume each state's duration fades at a fixed rate, which can be too restrictive. The authors let each state last for a data-driven length of time, modeled either with a named counting distribution (such as the negative binomial) or without assuming a shape, and they fit it with established algorithms. They illustrate the approach on overnight sleep-study EEG recordings from children.

## Probability

### [Stochastic Differential Equations on the Simplex](https://arxiv.org/abs/2611.27309)
*Paolo Guasoni, Eberhard Mayerhofer* · `math.PR` · arXiv:2611.27309v1 · relevance 0.29

- **In one sentence**: The paper builds a class of simplex-valued diffusion processes as solutions to stochastic differential equations driven by antisymmetric Brownian motion, covering multivariate Jacobi processes and general simplex-valued polynomial diffusions, and establishes weak solutions plus global strong existence and pathwise uniqueness from strictly positive starts under a boundary non-attainment condition.
- **In plain words**: The paper studies random processes whose values always stay on a "simplex," meaning a set of numbers that are non-negative and add up to one, like a split of a whole into shares that move over time. The authors describe these moving shares with a single rule based on pairwise "edge" terms, and this rule includes several known families of such processes as special cases. They prove that, when the shares start strictly above zero and a stated boundary condition holds, the process exists for all time and is uniquely determined by its random driving noise.
- **Why it matters**: Processes that model shares of a whole (such as proportions or probabilities) appear in areas like population genetics and portfolio modelling, so a general and mathematically secure framework for them may be useful there. The text does not describe specific applications, so this connection is a guess rather than something the paper establishes.
- **Background needed**: - Simplex: the set of non-negative numbers that sum to one (a set of proportions).
- Stochastic differential equation: a rule for how a quantity changes over time, with a random noise term.
- Brownian motion: the standard model of continuous random jitter over time.
- Antisymmetric Brownian motion: a noise driver where pairwise noise terms flip sign when the two items are swapped, which keeps the total at one.
- Jacobi process: a known diffusion living on an interval or simplex, used as a benchmark family.
- Weak vs. strong solution: a weak solution exists in some probabilistic sense; a strong solution is built pathwise from the given noise.
- Pathwise uniqueness: for a given noise path, there is only one resulting trajectory.
- Boundary non-attainment: the process never reaches the edge of the simplex (a share hitting zero). · level: research-level

<details><summary>Original abstract</summary>

We propose a framework for simplex-valued diffusion processes, formulated as solutions to stochastic differential equations driven by antisymmetric Brownian motion. Our edge-wise representation includes the multivariate Jacobi processes and the general class of continuous simplex-valued polynomial diffusions. Also, it allows bounded, locally Lipschitz state-dependent drift rates and edge weights. We establish weak solutions, as well as global strong existence and pathwise uniqueness for strictly positive initial states under a sufficient boundary non-attainment condition.

</details>

### [Isolation in Random Graphs](https://arxiv.org/abs/2611.26781)
*Laurentiu Ploscaru* · `math.CO` · arXiv:2611.26781v1 · relevance 0.21

- **In one sentence**: The paper studies isolation and domination in the binomial random graph G(n,p), proving first-order asymptotics for F-isolation for forests F, two-point concentration of the isolation number for a range of p, and a transition in the gap between domination and isolation numbers.
- **In plain words**: This paper looks at random networks, where each pair of nodes is linked independently with some probability p. It asks how few "chosen" nodes are needed so that every other node is either chosen or next to a chosen node (domination), and a closely related question where the leftover nodes must not contain a certain small pattern. The authors give precise size estimates for these quantities and show when the gap between the two versions grows and when it stays very small.
- **Why it matters**: Domination and isolation are standard graph parameters, and random graphs are the usual testing ground for how such parameters behave in typical cases. The results pin down sharp asymptotic behaviour and identify a threshold in p where the behaviour changes; the text does not discuss applications beyond this.
- **Background needed**: - A graph is a set of nodes (vertices) joined by links (edges).
- G(n,p): a random graph on n nodes where each possible link appears independently with probability p.
- Dominating set: a set of nodes such that every node is in the set or adjacent to one in it; the domination number is the smallest such set's size.
- Isolating set: a set whose removal-style condition leaves the remaining nodes with no edges among them; the isolation number is the smallest such set. Here F-isolation generalises this, with the leftover graph required to be F-free (containing no copy of the small graph F).
- Forest: a graph with no cycles; an edge is the simplest forest.
- Asymptotic notation: o(1) means tending to zero, and "with high probability" means the chance of failure goes to zero as n grows.
- Two-point concentration: the value almost always falls on one of two adjacent integers.
- Minimum degree bound: a classical inequality relating domination to the smallest number of neighbours any node has. · level: research-level

<details><summary>Original abstract</summary>

We study isolation in the binomial random graph $G(n,p)$. When $p=o(1)$ and $np\to\infty$, allowing an $F$-free graph on the undominated vertices gives the same first-order asymptotics for every fixed forest $F$ as the domination number $\gamma(G)$ in $G(n,p)$. For the ordinary isolation number $\iota(G)$ ($F$ is an edge) we prove two-point concentration when $p$ is bounded away from $1$ and $np^2/(\log n)^3\to\infty$. We also identify a transition in the gap $\gamma(G)-\iota(G)$ when $\log(1/p)=o(\log n)$. This gap tends to infinity in probability when $p$ is well below $(\log\log n/\log n)^2$ and is at most one with high probability when $p$ is well above this scale. Finally, for every fixed graph $F$, we show that the classical minimum degree bound for domination is asymptotically sharp for $F$-isolation, even for regular host graphs.

</details>

## Differential geometry

### [Projectively Flat Spherically Symmetric Sprays of Constant Curvature](https://arxiv.org/abs/2611.27723)
*Yajing Gui, Benling Li* · `math.DG` · arXiv:2611.27723v1 · relevance 0.11

- **In one sentence**: The paper classifies projectively flat, spherically symmetric sprays of constant curvature by solving the system of equations that the constant-curvature condition reduces to, yielding four explicit families for the projective factor p(r,s), and shows that the spray of constant-flag-curvature Finsler metrics with K=0, -1, or 1 fall within this classification.
- **In plain words**: This is a pure-mathematics paper about the geometry of curved "spaces with a direction at every point," where distances can depend on which way you move. The authors describe the complete set of such geometries that have a particular kind of uniform curvature and a spherical symmetry, sorting them into four explicit families. They also check that the known examples with constant curvature values 0, -1 and 1 all appear among these families.
- **Why it matters**: The result gives a full list rather than isolated examples, which is useful for anyone studying Finsler geometry, a generalization of Riemannian geometry. The text does not say what applications the classification might have, so any wider connection is speculative.
- **Background needed**: - Riemannian geometry: the study of curved surfaces and spaces, where distances and angles are measured locally.
- Finsler metric: a generalization in which the length of a vector depends on its direction, not only its base point.
- Spray: a system of second-order equations describing the "straightest" paths (geodesics) in a Finsler space.
- Projective flatness: the geodesics can be matched to straight lines in some coordinates, up to reparametrization; the projective factor p(r,s) measures how this matching is done.
- Spherical symmetry: the geometry looks the same under all rotations about a central point.
- Constant (flag) curvature: the curvature has the same value at every point and in every direction; K=0 is flat, K=1 and K=-1 are the sphere-like and hyperbolic-like analogues. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study projectively flat spherically symmetric sprays of constant curvature. We derive a system of equations that is equivalent to the constant-curvature condition for such sprays and solve it to obtain a complete classification of the projective factor \(p(r,s)\) into four explicit families. We further show that the sprays induced by projectively flat spherically symmetric Finsler metrics of constant flag curvature \(K=0\), \(K=-1\), and \(K=1\) are all special cases of our classification, thereby confirming that the sprays induced by these constant-flag-curvature Finsler metrics are fully contained in our framework.

</details>

### [A local symmetry forces positivity for projectively induced Kahler-Einstein metrics](https://arxiv.org/abs/2611.27345)
*Filippo Salis* · `math.DG` · arXiv:2611.27345v1 · relevance 0.10

- **In one sentence**: A projectively induced Kähler–Einstein metric with at least one local real-holomorphic Killing field must have positive Einstein constant, with no completeness or global group-action assumption, and the argument goes through Calabi rigidity, Hulin's continuation, and an Omori–Yau/Yau maximum-principle and Liouville argument.
- **In plain words**: The paper studies curved geometric shapes that sit inside a flat-style projective space and carry a special kind of balanced, Kähler-type curvature. It asks whether such a shape must curve positively, and shows that if the shape has even a local symmetry (a smooth flow that preserves the geometry in a small region), then it must curve positively, ruling out zero and negative curvature. The authors say this is a partial answer to a broader open question.
- **Why it matters**: The positivity question for Kähler–Einstein submanifolds of projective space is a general problem in differential geometry, and this gives a partial answer under a local symmetry hypothesis. The text does not indicate wider applications beyond this area.
- **Background needed**: - Kähler manifold: a complex-geometry setting where the curvature is compatible with complex structure.
- Einstein constant: a single number describing how the Ricci curvature is scaled; its sign (positive, zero, negative) is the key quantity here.
- Projective space and projectively induced metrics: shapes sitting inside complex projective space, with the metric inherited from it.
- Killing field: an infinitesimal symmetry, a flow that preserves the metric; "real-holomorphic" means it also respects the complex structure.
- Moment map / Hamiltonian potential: a function attached to a symmetry that measures its effect.
- Calabi rigidity: a result saying local symmetries of such metrics extend to global ones in a controlled way.
- Maximum principle and Liouville theorem: standard analytic tools; a bounded solution of a Laplace-type equation on a complete space must be constant. · level: research-level

<details><summary>Original abstract</summary>

We prove that a projectively induced Kahler-Einstein metric has positive Einstein constant as soon as it admits one nonzero local real-holomorphic Killing field. Neither completeness nor a prescribed global group action is assumed. This gives a partial answer, under a local symmetry hypothesis, to the general positivity problem for Kahler-Einstein submanifolds of (finite-dimensional) projective space. The key observation is that, by Calabi rigidity, a local real-holomorphic Killing field is induced by a projective unitary vector field whose tangency propagates along any connected global Kahler immersion, without a simple-connectivity assumption. Applied to Hulin's complete continuation, this produces a global Killing field with a bounded Hamiltonian potential given by the ambient projective moment map. The resulting Laplace equation, the Omori--Yau maximum principle and Yau's Liouville theorem exclude both negative and zero Einstein curvature. We also prove a non-Einstein obstruction under uniformly negative Ricci curvature and obtain compact equivariant continuations.

</details>

## Partial differential equations

### [Overview and recent progress on the classical Bernoulli free boundary problem](https://arxiv.org/abs/2611.26636)
*Xavier Fern\'andez-Real* · `math.AP` · arXiv:2611.26636v1 · relevance 0.42

- **In one sentence**: A survey of the classical one-phase Bernoulli free boundary problem in PDE theory, highlighting recent progress on it.
- **In plain words**: This is an overview article about a mathematical problem where you must find a function and also the unknown edge of the region where that function lives. The problem is named after Bernoulli and is often described as one-phase, since only one side of the boundary carries the interesting behavior. The text itself is only a short summary; it says the survey covers the field with emphasis on recent progress, but does not list specific results.
- **Why it matters**: The provided text gives no specific findings, so its importance cannot be judged from it. Free boundary problems of this kind arise in models of shapes that change over time, such as fluid or heat flow with a moving interface, but the text does not say which applications this survey addresses.
- **Background needed**: - A partial differential equation (PDE) is an equation relating a function to its rates of change in space; PDEs model heat, fluids, and similar physical processes.
- A free boundary is an interface whose location is not known in advance and must be found as part of the solution.
- The Bernoulli (one-phase) problem asks for a function that is harmonic (smooth, with no local peaks or dips) in a region, with a condition on the boundary that links the function's slope to the boundary's shape.
- A survey is a review of existing work rather than presentation of new results. · level: research-level

<details><summary>Original abstract</summary>

This survey gives an overview of the Bernoulli or one-phase free boundary problem, with emphasis on recent progress.

</details>

### [On the fully nonlinear degenerate parabolic quenching problem](https://arxiv.org/abs/2611.27774)
*Seunghyun Kim, Jos\'{e} Miguel Urbano* · `math.AP` · arXiv:2611.27774v1 · relevance 0.19

- **In one sentence**: The paper studies a fully nonlinear, degenerate parabolic quenching free boundary problem with a power-type source term, proving existence of nonnegative viscosity solutions with prescribed boundary data, an optimal upper growth rate along the free boundary, and matching non-degeneracy estimates.
- **In plain words**: The paper looks at a time-dependent equation in which the unknown function must stay nonnegative and a moving boundary separates the region where it is positive from the region where it is zero. The authors show that a suitable solution exists with given boundary values, and they pin down how fast the solution can grow near that moving boundary. They also prove matching lower-bound estimates, so the growth rate is both an upper and a sharp limit.
- **Why it matters**: Free boundary problems of this type model heat flow or diffusion that switches off or "quenches" in some region, so sharp growth bounds at the moving edge describe how the process behaves there. The text does not say what applications the results target, so connections beyond the mathematics are uncertain.
- **Background needed**: - Parabolic equation: a PDE describing evolution over time, like heat spreading, with time derivative u_t.
- Free boundary: the unknown boundary between the region where the solution is positive and where it is zero; its location is part of the answer.
- Fully nonlinear operator F(D^2u): the equation depends nonlinearly on the second derivatives (curvature-like terms) of u, not just linearly.
- Degenerate: the coefficient |Du|^kappa vanishes where the gradient vanishes, which breaks standard smoothness arguments.
- Viscosity solution: a weak notion of solution for nonlinear equations that does not require the function to be differentiable everywhere.
- Uniform ellipticity, convex/concave operators: structural conditions that keep the equation well-behaved.
- Growth rate and non-degeneracy: how fast the solution rises away from the boundary, and a guarantee that it cannot be flat there.
- Bernstein estimate and barrier arguments: standard tools bounding derivatives of solutions and comparing them with explicit sub/supersolutions.
- Scaling: parabolic cylinders are adapted to the rescaling symmetry of the equation. · level: research-level

<details><summary>Original abstract</summary>

We study the fully nonlinear degenerate parabolic free boundary problem $$|Du|^\kappa F(D^2u)-u_t=u^{\gamma-1} \qquad \textrm{in} \quad \{u>0\},$$ where $\kappa>0$, $0<\gamma<1$, and $F$ is a convex or concave uniformly elliptic operator with $F(0)=0$. We establish the existence of a nonnegative viscosity solution with prescribed continuous nonnegative boundary data and prove its optimal upper growth along the free boundary, together with matching non-degeneracy estimates in parabolic cylinders adapted to the scaling. Our approach combines a weak Bernstein estimate with barrier arguments to obtain local compactness and boundary attainment. To obtain the optimal growth rate, we further use persistence of positivity for limits with vanishing absorption coefficients to identify the homogeneous equation across the zero set, and then combine the optimal spatial regularity estimate of \cite{LLYZ25} with an iteration argument.

</details>

## Harmonic analysis

### [Freedom is all you need](https://arxiv.org/abs/2611.27943)
*Julian Bushelli, James Eldred Pascoe* · `math.FA` · arXiv:2611.27943v1 · relevance 0.14

- **In one sentence**: The paper begins a representation theory that relates a generic free functional calculus (a way of applying analytic functions to tuples of non-commuting matrices or operators, organised over a category) to the classical non-commutative functional calculus of Taylor, Voiculescu and others, with a stated aim of connecting this to learning over categories.
- **In plain words**: The paper is about a mathematical way of applying functions to matrices and operators, where the order of multiplication matters. The authors start a general framework that links a newer, broader version of this approach to the older, established version. The text says the setting also has properties such as automatic analyticity and a "universal monodromy", which the authors suggest may hint at why very large models can generalise well despite fitting training data closely.
- **Why it matters**: The link to "beneficial overfitting" in large parallel networks is only described as a hypothetical explanation in the abstract, so it should be read as a speculative motivation rather than a result. The connection to learning over categories is an aspiration stated by the authors and is not developed in the text provided.
- **Background needed**: - Functional calculus: defining f(A) for a matrix or operator A by applying a function f, generalising f(x) for numbers.
- Non-commutative (nc) setting: matrices do not commute in general, so AB and BA can differ; the order of entries matters.
- Free functional calculus: a version that works over all such tuples at once, organised using category theory (objects and structure-preserving maps).
- Direct-sum closed and similarity-invariant domains: sets of inputs closed under block-diagonal combination and unchanged under change of basis.
- Analyticity and monodromy: analytic means locally given by convergent power series; monodromy describes how analytic continuation around loops can change a function's value.
- Beneficial overfitting: a machine-learning observation that models fitting training data exactly can still predict well on new data. · level: research-level

<details><summary>Original abstract</summary>

The functional calculus allows for the rigorous analysis of functions of matrices or even operators. The free functional calculus gives the natural class of functions over any category. We initiate the representation theory for taking a generic free functional calculus to the classical nc functional calculus going back to Taylor, Voiculescu and many others, with an eye towards learning of categories. The functional calculus on direct sum closed and locally similarity (i.e. change of coordinates) invariant domains inherits the niceties of complex analysis and large-scale parallel networks, such as automatic analyticity, free universal monodromy, which gives a hypothetical explanation for beneficial overfitting.

</details>

### [The Ritt problem is decidable](https://arxiv.org/abs/2611.27008)
*Jason Fang, James Freitag, Matthew Harrison-Trainor* · `math.AC` · arXiv:2611.27008v1 · relevance 0.14

- **In one sentence**: The paper claims a positive answer to the Ritt problem, a question about whether polynomial or rational functions that decompose in a given way can be algorithmically decided, though the text gives no detail on the exact formulation or method.
- **In plain words**: This paper settles a long-standing question in algebra about breaking down polynomial formulas into simpler pieces, called "decomposition." The question asks whether a computer could always decide, in a finite procedure, if one such formula can be built from others through this kind of composition. The text says the answer is yes, but it is only a one-sentence abstract, so the details of the method are not given.
- **Why it matters**: Ritt's decomposition theory is a classic thread connecting algebra, complex dynamics and computer algebra, so a decidability result would matter to specialists there. The text is too thin to say how broad the consequences are, and I am unsure how the result is tied to harmonic analysis as the field label suggests.
- **Background needed**: - Polynomials and rational functions: formulas built from variables, addition, multiplication and division.
- Functional decomposition: writing a formula as a composition of simpler formulas, like f(g(x)).
- Ritt's theorems (1920s): classical results on how such decompositions relate to one another.
- Decidability: whether a yes/no question can always be settled by a finite, mechanical procedure.
- The text gives only the title and a one-sentence abstract, so the precise statement is unknown. · level: research-level

<details><summary>Original abstract</summary>

We give an affirmative solution to the Ritt problem.

</details>

## Complex analysis

### [An affine surface with 3-step nilpotent fundamental group](https://arxiv.org/abs/2611.27475)
*Sergey Polevoy, Vasily Rogov* · `math.AG` · arXiv:2611.27475v1 · relevance 0.09

- **In one sentence**: The paper constructs a smooth complex affine surface whose fundamental group is virtually 3-step nilpotent but not virtually 2-step nilpotent, answering the quasi-projective version of Campana's nilpotency problem in the negative.
- **In plain words**: The paper concerns how the loops inside a certain kind of geometric shape can be grouped and simplified. The author builds a specific smooth complex surface whose loops follow a rule that is more layered than a simpler rule that was conjectured to hold, which settles a question in the negative. The abstract gives only this construction and its conclusion, not the details of the argument.
- **Why it matters**: It settles a yes-or-no question (a version of Campana's nilpotency problem) by giving a counterexample, which narrows what can be true about these shapes. Its wider connections are to the study of fundamental groups of algebraic varieties; the text does not say more about applications.
- **Background needed**: - Complex affine surface: a smooth geometric surface described by polynomial equations over the complex numbers, with some points removed.
- Fundamental group: the group recording which loops on a space can be deformed into one another; it is a standard invariant of a shape.
- Nilpotent group: a group that becomes trivial after repeatedly taking commutators; "k-step nilpotent" measures how many layers of such commutators are needed.
- "Virtually" nilpotent: the group has a finite-index subgroup that is nilpotent.
- Campana's nilpotency problem: a conjecture relating the fundamental group of a complex variety to nilpotency; the quasi-projective version concerns non-compact varieties. · level: research-level

<details><summary>Original abstract</summary>

We construct a smooth complex affine surface $Y$ such that $\pi_1(Y)$ is virtually $3$-step nilpotent, but not virtually $2$-step nilpotent. This gives a negative answer to the quasi-projective version of Campana's nilpotency problem.

</details>

### [Local connectivity of Julia sets of Newton maps of trigonometric and hyperbolic functions](https://arxiv.org/abs/2611.26654)
*Molla Basir Ahamed, Sayantan Chakraborty* · `math.DS` · arXiv:2611.26654v1 · relevance 0.07

- **In one sentence**: The paper proves local connectivity of Julia sets (the boundaries of the chaotic region) for Newton maps of sin, cos, sinh and cosh, using explicit repelling petals at infinity for the cosine map and a conjugacy of the hyperbolic family to the sine map.
- **In plain words**: The paper studies a repeated "Newton's method" iteration applied to four standard trigonometric and hyperbolic functions, and asks how the boundary between points that settle into attracting regions and points that behave chaotically is shaped. The authors check directly that the cosine version has special repelling regions near infinity, which lets them apply an existing criterion showing that the boundary of each attracting region is "locally connected", meaning it has no pinched or isolated-looking pieces. They also show that a whole family of hyperbolic-function maps is just a rescaled copy of the sine case, so the known result for sine carries over to them.</plain>
<parameter name="why">Newton-type iterations are a common root-finding tool, so understanding where they converge or fail has mathematical interest. The text is limited to the mathematical statements and does not show any application beyond pure complex dynamics, so its wider significance is unclear.
- **Background needed**: Newton's method: an iterative formula that homes in on roots of a function. Complex dynamics: repeatedly applying a function to complex numbers and studying where the points go. Julia set: the boundary separating points with tame long-run behaviour from chaotic ones. Attracting basin: the set of starting points that converge to an attracting point. Local connectivity: a topological property saying the boundary is made of connected pieces with no gaps that cut it apart. Transcendental meromorphic function: a complex function that is not a polynomial or rational function, with only isolated poles. Conjugacy: rewriting one map in different coordinates so that it behaves identically. Repelling petal: a region near infinity where the iteration pushes points away. · level: research-level

<details><summary>Original abstract</summary>

We study the Newton maps of $\sin z$, $\cos z$, $\sinh z$, and $\cosh z$, each of which is transcendental meromorphic and has infinitely many unbounded immediate attracting basins. We first verify directly that, for the cosine Newton map $N_{\cos}(z) = z + \cot z$, the half-planes $\{\pm \operatorname{Im} z > M\}$ are repelling petals at infinity for every $M \ge 2$. These explicit petals allow us to apply the tame-basin criterion of Bara\'nski, Fagella, Jarque, and Karpi\'nska and obtain local connectivity of the spherical boundary of each immediate basin of $N_{\cos}$. We also show that the Newton map of $Ae^{\lambda z} + Be^{-\lambda z}$, where $AB\lambda \neq 0$, is affinely conjugate to the sine Newton map $N_{\sin}(z) = z - \tan z$. The published local-connectivity theorem for $J(N_{\sin})$ therefore applies to this entire family, including the cosine and the two hyperbolic Newton maps. We describe the invariant lines and basin geometry of the four maps and illustrate the corresponding dynamical planes numerically.

</details>

## Operator algebras and spectral theory

### [On the AF embedding problem](https://arxiv.org/abs/2611.27471)
*Christopher Schafhauser* · `math.OA` · arXiv:2611.27471v1 · relevance 0.17

- **In one sentence**: A survey of the AF-embedding problem for C*-algebras, centred on the author's result that separable, exact, UCT C*-algebras with a faithful quasidiagonal trace embed into a unital simple AF algebra.
- **In plain words**: This paper is a survey about when a mathematical object called a C*-algebra can be placed inside a simpler kind of algebra, one built up from finite-dimensional pieces in stages. The main content, as the text describes, comes from the author's earlier work, which shows that a broad class of these algebras (separable, exact, satisfying the UCT, with a faithful quasidiagonal trace) can be embedded in a unital simple AF algebra. The survey also covers some other results.
- **Why it matters**: Embedding a complicated structure into a simpler, well-understood one is a standard way to learn about the complicated structure, so the question matters within operator algebra theory. The text does not say more about wider applications, so I cannot say how far it reaches beyond this field.
- **Background needed**: - A C*-algebra: a collection of bounded linear operators on a Hilbert space (generalised "numbers" that can be added, multiplied and adjointed), used to model quantum systems and more abstract structures.
- Finite-dimensional algebra: a set of operators acting on a finite-dimensional space, essentially matrices.
- AF algebra: an "approximately finite" algebra, a limit of finite-dimensional matrix algebras glued together in stages.
- Embedding: placing one algebra inside another as a subalgebra that preserves the algebraic structure.
- Exact, UCT, quasidiagonal, trace: technical regularity conditions on C*-algebras; a trace is a way of assigning a "size" to elements, and quasidiagonality is an approximation property.
- Simple algebra: one with no nontrivial two-sided ideals (no proper "sub-pieces" that absorb multiplication). · level: research-level

<details><summary>Original abstract</summary>

This article gives a survey of the AF-embedding problem for $C^*$-algebras. The problem asks when a given $C^*$-algebra $A$ embeds into an \emph{approximately finite dimensional} (AF) $C^*$-algebra (a direct limit of finite dimensional $C^*$-algebras). This is largely based on my paper ``Subalgebras of simple AF algebras,'' which shows that separable, exact $C^*$-algebras satisfying the UCT and admitting a faithful, quasidiagonal trace embed into a unital, simple AF algebra. Some other results are also discussed.

</details>

### [Rigidity in the Lichnerowicz inequality for word-length semigroups](https://arxiv.org/abs/2611.27204)
*Melchior Wirth* · `math.OA` · arXiv:2611.27204v1 · relevance 0.15

- **In one sentence**: The paper characterizes when equality holds in noncommutative Lichnerowicz-type spectral gap inequalities (the complete Γ2 criterion and the geometric Ricci criterion) for word-length semigroups on group von Neumann algebras, showing equality occurs exactly when the Cayley graph is a partial cube.
- **In plain words**: The paper studies a mixing process on a group, where a random walk-like dynamics is measured by how quickly it settles down. It shows that for a specific family of such processes, a sharp equality case in two known bounds on how fast the process settles occurs exactly when the group's underlying network of connections can be drawn isometrically inside a hypercube. In other words, a geometric property of the network is detected by an operator-algebra quantity.
- **Why it matters**: It gives a new operator-algebraic test for a classical geometric property of graphs, the partial cube property, linking spectral gaps of quantum Markov semigroups to graph geometry. The text does not say what broader applications this may have, so its wider significance is uncertain.
- **Background needed**: - Group von Neumann algebra: a noncommutative algebra of operators built from a group, used as a setting for quantum probability.
- Quantum Markov semigroup: a family of maps describing how a quantum system evolves randomly over time.
- Spectral gap: a number measuring how fast such an evolution converges to equilibrium.
- Lichnerowicz inequality: a classical bound relating a spectral gap to curvature-like constants; the paper studies noncommutative versions.
- Cayley graph and word length: a group is drawn as a graph whose edges come from generators; word length is the minimal number of generators needed to spell an element.
- Partial cube: a graph that embeds isometrically (distances preserved) into a hypercube. · level: research-level

<details><summary>Original abstract</summary>

We give an operator-algebraic characterization of Cayley graphs that are partial cubes, that is, embed isometrically into a hypercube. More precisely, noncommutative versions of the Lichnerowicz inequality control the spectral gap of the generator of a quantum Markov semigroup by the constant in the complete $\Gamma_2$-criterion of Junge and Zeng or the constant in the geometric Ricci criterion of Junge, LaRacuente and Li. We show that for word-length semigroups on group von Neumann algebras, equality in either of these inequalities occurs exactly when the Cayley graph is a partial cube.

</details>

## Algebra

### [On coherence of enveloping algebras of infinite-dimensional Lie algebras](https://arxiv.org/abs/2611.27824)
*Susan J. Sierra, James Timmins* · `math.RA` · arXiv:2611.27824v1 · relevance 0.22

- **In one sentence**: The paper studies when universal enveloping algebras of infinite-dimensional Lie algebras are coherent, showing a sharp nilpotency criterion for loop algebras, non-coherence for a class of simple graded Lie algebras, and coherence results for related graded and filtered rings.
- **In plain words**: This paper is about a property called "coherence" for a certain kind of algebraic structure built from symmetry rules (Lie algebras). Coherence roughly means that certain systems of equations built from these structures behave nicely, so that their solutions are finitely describable. The authors determine exactly when this holds for loop algebras, show it fails for a broad family of simple infinite-dimensional algebras, and prove some positive results for related rings.
- **Why it matters**: The text gives the main results but not their wider consequences. It is a specialist result in ring theory, and it sits alongside earlier work on whether these algebras are Noetherian (every chain of ideals stabilizes), so it likely matters mainly to researchers in that area.
- **Background needed**: - Lie algebra: an algebra of infinitesimal symmetries, with a bracket operation.
- Universal enveloping algebra U(g): a ring built from a Lie algebra g that encodes its structure.
- Infinite-dimensional: the algebra has infinitely many independent directions, unlike finite-dimensional matrix Lie algebras.
- Loop algebra: functions from a circle (or Laurent polynomials) with values in a finite-dimensional Lie algebra h.
- Nilpotent: repeated brackets eventually vanish.
- Coherent ring: finitely generated one-sided ideals are finitely presented, a finiteness condition weaker than Noetherian.
- Graded and filtered rings: rings split into pieces by degree, or equipped with a nested sequence of subspaces; the Rees ring is a standard way to pass between the two.
- Witt algebra: the Lie algebra of derivations of Laurent polynomials, a standard example of an infinite-dimensional simple Lie algebra. · level: research-level

<details><summary>Original abstract</summary>

We investigate when the universal enveloping algebra $U(\mathfrak{g})$ of an infinite-dimensional Lie algebra $\mathfrak{g}$ is coherent. We show that if $\mathfrak{g}$ is the loop algebra of a finite-dimensional Lie algebra $\mathfrak{h}$ then $U(\mathfrak{g})$ is coherent exactly when $\mathfrak{h}$ is nilpotent. As a consequence, we show that $U(\mathfrak{g})$ is not coherent if $\mathfrak{g}$ is complex, simple, $\mathbb{Z}$-graded, of polynomially bounded growth, and not isomorphic to the Witt algebra $W = \mathrm{Der} \mathbb{C}[t,t^{-1}]$ or its one-sided version. We also demonstrate that the homomorphic image of $U(W)$ used to prove non-Noetherianity of $U(W)$ in previous work of the first author and Walton is not coherent. On the other hand, we establish that two closely related connected graded rings are graded coherent. Finally, we prove that any exhaustively filtered ring is coherent if its Rees ring is graded coherent.

</details>

### [Large orbits of $p$-groups on conjugacy classes of arbitrary finite groups](https://arxiv.org/abs/2611.27916)
*Thomas Michael Keller* · `math.GR` · arXiv:2611.27916v1 · relevance 0.19

- **In one sentence**: The paper removes the solvability assumption from a result that, for a p-group acting coprimely and faithfully on a finite group H, finds a conjugacy class (or irreducible character) whose stabilizer in P has order at most |P|^{1/2}, with the bound shown to be sharp, using the classification of finite simple groups and a new lemma on quasiprimitive linear actions of p-nilpotent groups.
- **In plain words**: This paper is about symmetries of finite group structures: a small group of symmetries (a "p-group," a group whose size is a power of a prime p) acts on another finite group, and the question is how many of those symmetries can leave some piece of the structure unchanged. A previous result handled the case where the group is solvable, a technical class of groups that can be built up step by step from simple pieces; this paper drops that restriction. The authors show the same bound holds in general, with a proof that relies on the classification of finite simple groups.
- **Why it matters**: The result gives a guaranteed size limit on how much of a symmetry group can fix a piece of structure, and the authors show the limit is sharp by giving new examples with nonsolvable groups where it is attained. The text does not say what wider applications it has, so its broader significance beyond this area is unclear to me.
- **Background needed**: - Finite group: a group with finitely many elements, such as the symmetries of a finite set.
- Group action: a way a group's elements permute or transform another object.
- p-group: a group whose number of elements is a power of a prime p.
- Coprime action: the acting group's order shares no prime factor with the acted-on group's order.
- Stabilizer: the set of symmetries that leave a given element (or class, or character) unchanged; its order is how many such symmetries there are.
- Conjugacy class and irreducible character: standard objects describing the internal structure of a finite group.
- Solvable group: a group that can be built from abelian (commutative) pieces in layers; nonsolvable groups are the more complex case.
- Classification of finite simple groups: a large, known list of the basic building blocks of finite groups, used as a deep tool in the proof. · level: research-level

<details><summary>Original abstract</summary>

Let $P$ be a $p$-group that acts faithfully and coprimely on a finite group $H$. In a previous paper it was shown that if $H$ is solvable, then there exists a conjugacy class $c$ of $H$ whose stabilizer in $P$ has order at most $|P|^{1/2}$, and that this bound is best possible. In this paper we remove the hypothesis that $H$ is solvable. As a consequence, there always exists an irreducible character of $H$ whose inertia group in $P$ has order at most $|P|^{1/2}$. The proof depends on the classification of finite simple groups. Its main new ingredient is a result on quasiprimitive linear actions of $p$-nilpotent groups which shows that the elements acting as field automorphisms can be ignored when one looks for vectors with small stabilizers. We also present a new family of examples, with nonsolvable $H$, in which the bound is attained.

</details>

## Representation theory

### [The $n!$ theorem via quaternionic rotation of Cherednik algebras](https://arxiv.org/abs/2611.27113)
*Stephen Griffeth* · `math.RT` · arXiv:2611.27113v1 · relevance 0.13

- **In one sentence**: The paper gives a new proof of the "n! theorem" for rational Cherednik algebras, using their representation theory together with an analogue of rotating complex structures coming from a quaternion action.
- **In plain words**: This paper is about a known result in algebra, the "n! theorem," which concerns the symmetric group of permutations of n objects and a family of structures called Cherednik algebras. The author gives a new proof of this result rather than announcing a new finding. The proof combines the study of how these algebras act on vector spaces with a mathematical trick that resembles rotating a complex structure, driven by an action of the quaternions.
- **Why it matters**: The text is short, so it is unclear exactly which parts of the n! theorem are reproved or how much the new route simplifies earlier arguments. Its value likely lies in offering an alternative proof that links representation theory with quaternion-based ideas, but the abstract alone does not show how far that connection extends.
- **Background needed**: - Representation theory: studying abstract algebraic objects by how they act on vector spaces, often as matrices.
- Symmetric group: the group of all rearrangements of n objects; its size is n!.
- Cherednik algebras: a family of noncommutative algebras that generalise objects tied to symmetric groups and reflection groups.
- Quaternions: an extension of complex numbers with three imaginary units, forming a non-commutative number system.
- Complex structure: a way of treating a real vector space as a complex one, via multiplication by i; "rotation" here is an analogy for changing such structures.
- The n! theorem: a result about the dimension or count of certain representations, tied to n!; the text does not state its exact form. · level: research-level

<details><summary>Original abstract</summary>

We give a proof of the $n!$ theorem based on the representation theory of Cherednik algebras and an analog of the rotation of complex structures arising from an action of the quaternions.

</details>

### [The weighted fundamental lemma for non-split groups](https://arxiv.org/abs/2611.26750)
*Cass Halleck-Dub\'e* · `math.RT` · arXiv:2611.26750v1 · relevance 0.12

- **In one sentence**: The paper proves the Weighted Fundamental Lemma for Lie algebras for general quasi-split unramified groups, adapting the Chaudouard–Laumon geometric proof from the split case, and deduces Waldspurger's nonstandard version and a twisted version used to complete Moeglin–Waldspurger's stabilization of the twisted trace formula.
- **In plain words**: This is a paper in pure mathematics about symmetry groups and the counting identities that link them, which underpin the study of how number-theoretic objects are organized. The author extends a known geometric proof, originally worked out for "split" groups, to a broader class of groups called quasi-split groups. The text reports that this yields an identity between certain adelic orbital integrals, which is the central claim, along with consequences for automorphic theory.
- **Why it matters**: The text claims the work makes certain results unconditional, including the endoscopic classification for classical groups and several downstream consequences. Whether these claims hold is for specialists to assess; the summary here relies only on the authors' stated implications.
- **Background needed**: - Representation theory: the study of symmetry groups through how they act on vector spaces.
- Reductive group and Lie algebra: a continuous symmetry group and its linearized version.
- Quasi-split and unramified groups: special classes of groups over local number fields with a controlled structure.
- Orbital integrals and trace formula: averages over group elements that feed into counting formulas linking automorphic forms.
- Fundamental lemma: a identity comparing orbital integrals across related groups, a key tool in the Langlands program.
- Higgs bundles and Hitchin base: geometric objects on a curve used as a tool in the proof.
- Deligne–Mumford stack: a generalized geometric space that allows symmetries of its points. · level: research-level

<details><summary>Original abstract</summary>

In this work, we prove the Weighted Fundamental Lemma for Lie algebras for general (quasi-split) unramified $G$. The strategy is to adapt the proof of Chaudouard--Laumon from the split case. In particular, we define the notion of a $\xi$-stable Higgs bundle for a quasi-split reductive group scheme $G$ on a curve, and prove that the stack of such form a proper, finite-type Deligne--Mumford stack over the Hitchin base when $G$ has anisotropic center. We then adapt the global cohomological theorem of Chaudouard--Laumon to the quasi-split setting, and perform the required Frobenius-point count to obtain an identity of adelic orbital integrals. A local-to-global argument deduces the WFL for Lie algebras. In the last chapter, we perform a parallel reduction to deduce Waldspurger's nonstandard WFL from a global version which follows from the same geometric theory. Our work implies the Twisted Weighted Fundamental Lemma in good characteristic, which completes Moeglin--Waldspurger's stabilization of the twisted Arthur--Selberg trace formula. We therefore render unconditional the endoscopic classification for classical groups and an array of downstream consequences in automorphic theory.

</details>

## Number theory

### [Splitting types of Richelot isogenies over finite fields and a newform of weight four](https://arxiv.org/abs/2611.27775)
*Hung Dang* · `math.NT` · arXiv:2611.27775v1 · relevance 0.17

- **In one sentence**: Counts factorizations of square-free sextics over finite fields into three quadratics tied to Richelot (2,2)-isogenies of genus-2 curves, with the counts expressed via the trace of a weight-4, level-8 newform and a twisted second moment of the Legendre family.
- **In plain words**: This paper studies a counting problem about polynomials over a finite field (a number system with finitely many elements). It asks how many ways a degree-six polynomial can be split into three quadratic pieces, and how those pieces split further, and it gives exact formulas for all 64 splitting patterns. The formulas turn out to involve a known modular object, a special function attached to a particular symmetric-looking curve family.
- **Why it matters**: The counts reduce to a known hypergeometric value that was evaluated by Ahlgren and Ono, which links an elementary counting question to deep arithmetic objects. The text also gives a consequence about the fraction of factorizations whose resultants share a square class, and a result about which two-torsion points are divisible by two on a split Jacobian; its wider significance beyond these links is not stated in the text.
- **Background needed**: - Finite field F_q: a finite set of q elements with addition and multiplication; q is a prime power.
- Square-free sextic: a degree-six polynomial with no repeated roots.
- Splitting over F_q: whether a polynomial factors into pieces with coefficients in F_q (its roots lie in the field).
- Genus-2 curve and Jacobian: a curve of genus 2 whose associated group of points is a higher-dimensional analogue of an elliptic curve.
- Richelot isogeny: a standard map between genus-2 Jacobians with a rational kernel of order four.
- Legendre family: a family of elliptic curves indexed by a parameter; its moments are sums of character values.
- Newform and trace of Frobenius: a modular form with Hecke eigenvalues; the trace counts points of an associated variety modulo q.
- Two-torsion points: points killed by 2 on a group; "divisible by two" asks whether such a point equals twice some point. · level: research-level

<details><summary>Original abstract</summary>

A factorization $f=uvw$ of a square-free sextic over a finite field $\mathbb{F}_q$ of odd characteristic into three monic quadratics defines a genus-2 curve with a rational $(2,2)$-isogeny kernel, and the Richelot construction attaches to it three dual quadratics $U,V,W$. We determine, for every odd prime power $q$, the number of such factorizations with prescribed splitting behaviour over $\mathbb{F}_q$ of all six quadratics. Each of the $64$ counts is $q(q-1)(q+1-n_f)/64$ times $C(q)\pm t_q$, where $n_f$ is the number of roots of $f$ in $\mathbb{F}_q$, $C$ is an explicit monic cubic, and $t_q$ is the trace of Frobenius attached to the newform $\eta(2z)^{4}\eta(4z)^{4}$ of weight $4$ and level $8$. The proof reduces the counts by elementary means to a twisted second moment of the Legendre family of elliptic curves, which is a value of a hypergeometric function over $\mathbb{F}_q$ evaluated by Ahlgren and Ono for primes. As consequences, the number of factorizations whose three pairwise resultants lie in one square class is a polynomial in $q$, with proportion $1/4+3/(4q^{2})+O(q^{-4})$. When the quotient is a product of two elliptic curves conjugate over $\mathbb{F}_{q^2}$, we prove that the splitting of the factors $u,v,w$ over $\mathbb{F}_q$ decides which points of order two of the elliptic factor are divisible by two.

</details>

### [An explicit Cassels--Tate pairing in characteristic $2$ and the parity of $2$-Selmer ranks](https://arxiv.org/abs/2611.27040)
*Abhishek Shukla* · `math.NT` · arXiv:2611.27040v1 · relevance 0.17

- **In one sentence**: For ordinary elliptic curves over a global field of characteristic 2 with a rational 2-torsion point, the paper gives an explicit formula for the Cassels–Tate pairing on the 2-torsion of Sha as a sum of local Artin–Schreier symbols, relates it to Kramer's and Milne's pairings, and derives a local-root-number formula for the parity of rk A(K) + dim Sha(A/K)[2], extended to rational points of any prime order ℓ.
- **In plain words**: This is research in arithmetic geometry about elliptic curves, the smooth curves defined by cubic equations whose rational solutions form a group. The paper studies a hidden-but-measurable piece of the group structure (the group Sha, which measures failures of a local-to-global principle) over function fields of characteristic 2, a setting where arithmetic works differently. It gives an explicit formula for a pairing that governs this piece and uses it to determine when the rank-plus-Sha quantity is odd or even, expressed through local terms.
- **Why it matters**: Parity results of this kind connect the rank of an elliptic curve's rational points to local invariants, and the text links these local terms to root numbers from the Birch and Swinnerton-Dyer framework. The characteristic-2 setting is a less-studied case, and the extension to any prime ℓ equal to the characteristic is described as new; the text does not establish broader consequences beyond these.
- **Background needed**: - Elliptic curve: a genus-one curve with a group law on its rational points.
- Global field of characteristic 2: a function field over a finite field or similar, where 1 + 1 = 0.
- Rank of E(K): the number of independent rational points of infinite order.
- Sha (Tate–Shafarevich group): classes that everywhere-locally solvable problems fail to be globally solvable; its size is conjecturally finite.
- 2-Selmer group: a finite-dimensional approximation to rational points used in descent; its dimension controls the parity question.
- Cassels–Tate pairing: an alternating pairing on Sha whose kernel and nondegeneracy relate to Sha's structure.
- Isogeny (Verschiebung): a group-preserving map between elliptic curves, here of degree 2.
- Artin–Schreier symbols: local tools for characteristic-2 fields, analogous to Hilbert symbols.
- Root number: a sign (±1) attached to an L-function, linked to the parity of rank via conjectures. · level: research-level

<details><summary>Original abstract</summary>

Let $K$ be a global field of characteristic $2$ and $\varphi\colon E\to E'$ the Verschiebung of an ordinary elliptic curve $E/K$ with a rational point of order $2$. We prove an explicit formula for the homogeneous-space Cassels--Tate pairing on $\Sha(E/K)[\varphi]$ as a sum of local Artin--Schreier symbols, show that it coincides with Kramer's descent pairing and, on $\Sha(E/K)[\varphi]$, with the pairing induced by Milne's flat duality, and deduce that it is non-degenerate on $\Sha(E/K)[\varphi]/\hat\varphi(\Sha(E'/K)[2])$. For every ordinary elliptic curve $A/K$ we express the parity of $\mathrm{rk}\,A(K)+\dim\Sha(A/K)[2]$ by local terms (after Kramer), and identify these with local root numbers at places of semistable or potentially multiplicative reduction, and in further cases using curves with finite $\Sha$. We determine $\Sha$ in examples, and extend the formula to rational points of any prime order $\ell$, the new case being $\ell=\operatorname{char}K$.

</details>

## Algebraic geometry

### [Combinatorial relative orientability for toric and tropical geometry](https://arxiv.org/abs/2611.27238)
*Nathan Tiggemann* · `math.AG` · arXiv:2611.27238v1 · relevance 0.25

- **In one sentence**: The paper gives a combinatorial criterion for relative orientability of vector bundles over smooth proper toric varieties, shows it is compatible with tropicalization, and applies this to a quadratically enriched Bernstein-Khovanskii-Kushnirenko theorem and to k-phase structures on tropical hypersurfaces.
- **In plain words**: Many counting problems in geometry ask how many solutions a system of equations has, and modern methods answer these by computing a single number attached to a geometric object. This paper translates the condition needed for that number to be well defined into a purely combinatorial form, meaning one checked with counting and graph-like data rather than heavy algebra. It then uses this translation to transfer the question to tropical geometry, a simplified piecewise-linear version of geometry, and proves an enriched version of a known counting theorem by that route.
- **Why it matters**: The work aims to let tropical geometry, which is combinatorial and easier to compute with, answer enumerative questions over arbitrary fields, not only over the real or complex numbers. The text does not claim wider impact beyond this, and the connection to broader applications is a plausible direction rather than a demonstrated result.
- **Background needed**: - Enumerative geometry: counting solutions to geometric problems, such as how many curves satisfy given conditions.
- Vector bundle: a family of vector spaces attached smoothly to each point of a space; "relatively oriented" means a consistent choice of orientation, which is needed for a count to have a well-defined sign.
- Chern class and Euler class: characteristic numbers of a vector bundle; the top Chern class's degree gives an enumerative count.
- Chow-Witt groups and A^1-homotopy theory: refined tools that give counts valid over any field, with extra quadratic (square-class) information.
- Toric variety: a geometric space built from combinatorial data (polytopes and fans).
- Tropical geometry: a piecewise-linear shadow of algebraic geometry, where problems become combinatorial.
- Bernstein-Khovanskii-Kushnirenko theorem: a classical result counting solutions of polynomial systems via the mixed volume of their Newton polytopes.
- Phase structure: extra sign data on tropical hypersurfaces, generalizing the real case. · level: research-level

<details><summary>Original abstract</summary>

Many problems in enumerative geometry are solved by computing the degree of the top Chern class of a suitable vector bundle. Results from $\mathbb{A}^1$-homotopy theory allow to answer enumerative questions over arbitrary fields, replacing the top Chern class by the Euler class in Chow-Witt groups. For its degree to be well-defined, one needs the vector bundle to be relatively oriented. Another way to solve enumerative problems is to translate them to tropical geometry, where they become combinatorial problems. In this paper, we give a combinatorial description of relative orientability for vector bundles over smooth proper toric varieties. We show that it behaves well under tropicalization, establishing a tropical version of relative orientability, which will allow to the use of tropical geometry to answer enumerative questions over arbitrary fields. As a demonstration, we prove a quadratically enriched version of the Bernstein-Khovanskii-Kushnirenko theorem via tropical geometry. Lastly, we define the notion of $k$-phase structures on tropical hypersurfaces, generalizing the real case.

</details>

### [Classification of strongly $F$-regular and $F$-pure surface singularities with imperfect residue fields](https://arxiv.org/abs/2611.27597)
*Tatsuro Kawakami, Kenta Sato* · `math.AG` · arXiv:2611.27597v1 · relevance 0.12

- **In one sentence**: The paper classifies strongly F-regular and F-pure normal surface singularities over possibly imperfect residue fields, via weighted dual graphs and geometric reducedness of exceptional curves on the minimal resolution, extending Hara's algebraically closed case.
- **In plain words**: The paper studies a certain family of mild "pinched" points on surfaces, the kind that show up where a smooth shape is folded or collapsed, and asks which of them behave well under a characteristic-p operation (the Frobenius map, which raises functions to the p-th power). The authors sort these points by the pattern of curves that appear when you resolve them, which can be drawn as a weighted graph. The text reports that the sorting works even when the underlying number field is not perfect, which earlier results assumed away.
- **Why it matters**: This extends a known classification by Hara from algebraically closed fields to the more general imperfect case, which is a natural step for the theory. The abstract's specific claim that F-pure exceptional curves are geometrically reduced unless the point is a rational double point is a concrete structural statement; its broader significance beyond this setting is not stated in the text.
- **Background needed**: - Singularity: a point where a surface fails to be smooth, like the tip of a cone.
- Normal surface singularity: a well-behaved singular point of a surface.
- Residue field: the field of numbers or values at a point; "imperfect" means some p-th roots are missing, which matters in characteristic p.
- Characteristic p and Frobenius: working with arithmetic mod a prime p, where raising to the p-th power is a special map.
- F-regular / F-pure: properties of singularities defined via the Frobenius map; they indicate mild singularities.
- Minimal resolution: replacing the singular point by a smooth surface with a minimal set of curves, whose intersection pattern forms the dual graph.
- Rational double point: a simple class of surface singularities with a well-known ADE-type dual graph.
- Geometrically reduced: a curve that stays free of repeated components after passing to a larger field. · level: research-level

<details><summary>Original abstract</summary>

We study strongly $F$-regular and $F$-pure normal surface singularities whose residue fields are not necessarily perfect. We characterize strong $F$-regularity in terms of the weighted dual graph and geometric reducedness of the exceptional components of the minimal resolution, extending Hara's classification over algebraically closed residue fields. We also determine the possible dual graphs of $F$-pure surface singularities and give converse criteria. Notably, the exceptional components of an $F$-pure surface singularity are geometrically reduced unless the singularity is a rational double point.

</details>

## Topology

### [Persistent Mayer Path Homology and Mayer Path Laplacian](https://arxiv.org/abs/2611.26982)
*Dilan Karaguler, Guowei Wei* · `math.AT` · arXiv:2611.26982v1 · relevance 0.16

- **In one sentence**: The paper extends path homology for directed graphs to a nilpotent "Mayer" variant, develops its persistent version over filtered digraphs with stability results, and introduces a Mayer path Laplacian whose kernels recover the homology.
- **In plain words**: This paper is about a mathematical tool for studying networks where connections have a direction, such as one-way links between points. The authors build a new version of a known method that counts loops and holes in such networks, and they track how these counts change as the network is gradually built up by a growing threshold. They also apply it to a molecule, cucurbit[7]uril, where it picks up closed triangular patterns that the older method misses.
- **Why it matters**: The work offers a finer way to describe directed structure, such as feed-forward loops, which the existing path homology does not detect. Its usefulness beyond the molecular example is not established in the text, so the wider significance remains unclear.
- **Background needed**: - Directed graph (digraph): a network of points (vertices) joined by one-way arrows (edges).
- Homology: a way of counting independent loops and holes in a shape or network, recorded as Betti numbers.
- Boundary operator: a rule that maps each structure to its outline; in ordinary homology applying it twice gives zero, and Mayer homology relaxes this to applying it N times gives zero.
- Path homology: a version of homology adapted to directed graphs.
- Persistent homology: tracking when loops appear and disappear as a network is built up through a growing filter value, summarized in barcodes.
- Laplacian: a matrix whose spectrum (eigenvalues) carries information about the shape; its kernel recovers homology.
- Feed-forward loop: a small directed pattern in which one node points to a second, which points to a third, and the first also points directly to the third.
- Cucurbit[7]uril: a ring-shaped molecule; distances between its atoms are scaled by van der Waals radii. · level: research-level

<details><summary>Original abstract</summary>

In topological data analysis, path homology accounts for directed graph while combinatorial Laplacian extends homology groups to spectral theory. However, these approaches are built on a boundary operator with condition $\partial^2=0$. Mayer homology replaces this condition with $N$-nilpotent boundary map $\partial^N=0$. By using the primitive $N$-th root of unity in the boundary operator, it relates each degree $n$ to the degrees $n-q$ and $n+N-q$. This work introduces persistent Mayer path homology. We show that Mayer path homology is functorial for strict digraph maps, which gives persistent Mayer path homology for filtered digraphs, and prove that its barcodes are stable under perturbations. For $N=3$ we derive formulas that reduce $\beta_0^{3,1}$ and $\beta_2^{3,2}$ to the classes of vertices identified by squares and the rank of a small matrix indexed by triangles. We also introduce the Mayer path Laplacian and its persistence theory, prove that their kernels recover (persistent) Mayer path homology, show that they distinguish digraphs with the same Mayer path Betti numbers, and prove a stability bound for the eigenvalues of the persistent up-Laplacian. We demonstrate that persistent Mayer path homology detects the formation of feed-forward loops, whose formation is not detected by ordinary path homology. In an application to cucurbit[7]uril, filtered by an interatomic distance normalized by van der Waals radii, Mayer path homology separates contacts that only close cycles from contacts that close feed-forward triangles, and changes at almost four times as many filtration values as path homology after the bonded framework is formed.

</details>

### [A simple approach to ends of manifolds and the Freudenthal compactification](https://arxiv.org/abs/2611.26989)
*Rodrigo Hern\'andez-Guti\'errez, Carlos Rios-Mendoza* · `math.GN` · arXiv:2611.26989v1 · relevance 0.12

- **In one sentence**: The paper gives a new, more direct definition of the Freudenthal end-compactification of non-compact manifolds, using filters of open sets with compact boundaries that have a base of connected subsets, and shows it agrees with the older definitions.
- **In plain words**: The paper is about the "ends" of a non-compact shape, meaning the different ways one can head off toward infinity or toward its missing edges. The authors offer a simpler recipe for describing these ends and add them to the shape to make it compact. They check that their recipe gives the same result as the established versions, and they apply it to an example and to a known theorem about when such spaces can be measured with a distance.
- **Why it matters**: Ends of manifolds are a classical tool in topology, the study of shapes up to stretching, so a cleaner definition can make standard arguments easier to follow and teach. The text does not claim wider impact beyond this clarification and its simpler proofs.
- **Background needed**: - Manifold: a space that locally looks like ordinary Euclidean space (for example, a surface).
- Non-compact: the space is unbounded or has missing points at its edges, so it does not close up into a finite whole.
- Compactification: adding points to a space so that it becomes compact (finite in a topological sense).
- Freudenthal compactification: a standard way of adding one point for each "end" of a space.
- Filter: a collection of sets that is closed under taking supersets and finite intersections; here it is used to encode a way of going to infinity.
- Compact boundary: the edge of an open region is a closed, bounded-type piece that is compact.
- Metrizable: a space whose topology can be induced by a distance function. · level: research-level

<details><summary>Original abstract</summary>

In this note we give an alternative definition of the Freudenthal end-compactification of a non-compact manifold by defining ends to be the filters of open subsets with compact boundaries that have a base of connected subsets. We start by defining these notions and proving that the resulting compactification is equivalent to the Freudenthal compactification. In particular, we explicitly discuss the equivalence between our definitions and those from two different approaches: maximal binding families and inverse limits. After that, we give an example of a non-metrizable manifold, showing how these new definitions make it easier to identify ends and understand the topology of the end-compactification. We also prove a well-known metrization theorem, showing an application of our definition. Finally, we also give an alternative proof of the topological characterization of the Freudenthal compactification.

</details>

## Dynamical systems

### [Recurrent sets and Lyapunov functions: from topological dynamics to weak KAM theory](https://arxiv.org/abs/2611.27887)
*Olga Bernardi, Mattia Sensi, Jim Wiseman* · `math.DS` · arXiv:2611.27887v1 · relevance 0.18

- **In one sentence**: A survey linking Lyapunov functions and Conley's chain recurrent sets in topological dynamics, with recent weak KAM results for homeomorphisms, connections to the stationary Hamilton-Jacobi equation, and examples from epidemiology and a prey-predator model with Allee effect.
- **In plain words**: This survey looks at how two ways of describing long-run behavior of a system fit together: "energy-like" measuring functions (Lyapunov functions) that always decrease along motion, and the sets where motion can keep returning near its starting point (chain recurrent sets). It reviews recent progress in this area, including work from the weak KAM framework, and shows how these ideas apply to a disease-spread model and a predator-prey model. The abstract does not give specific new theorems, so the details of the results are not visible from this summary.
- **Why it matters**: Lyapunov functions are a standard tool for proving that a system settles down or stays stable, so clarifying exactly which sets they can detect is useful for both theory and modeling. The text suggests links to Hamilton-Jacobi equations and to applied models, but it does not show how far these connections reach in practice.
- **Background needed**: - Dynamical system: a rule that describes how a state changes over time, such as populations or planetary motion.
- Lyapunov function: a measuring function that steadily decreases along trajectories, like a ball rolling downhill to a resting point.
- Recurrent set: a region the system keeps returning to, at least approximately, from its own points.
- Chain recurrence (Conley): a looser notion where returns are allowed through small jumps, which gives a robust way to classify long-run behavior.
- Homeomorphism: a continuous, reversible change of space, used as a discrete-time model of motion.
- Hamilton-Jacobi equation: a partial differential equation from mechanics and optimal control; weak KAM theory studies its generalized solutions.
- Compartmental epidemic model: a model that splits a population into groups such as susceptible, infected, and recovered.
- Allee effect: a effect where small populations grow poorly, so they can die out even when resources exist. · level: research-level

<details><summary>Original abstract</summary>

The aim of this survey is to clarify the intimate relations between Lyapunov functions and chain recurrent sets. The study of this subject comes from a seminal paper by Conley and has had recent advances by the so-called Weak KAM Theory for homeomorphisms. We provide a survey of the state of the art, presenting recent improvements and connections with the stationary Hamilton-Jacobi equation. Finally, in order to illustrate the distinctions between recurrent sets in a non-trivial case as well as their dependence on a parameter, we discuss a compartmental model from mathematical epidemiology and a fast-slow version of a prey-predator model with Allee effect.

</details>

### [Non-local ergodic measures in symplectic dynamics](https://arxiv.org/abs/2611.27429)
*Jaime Paradela* · `math.DS` · arXiv:2611.27429v1 · relevance 0.15

- **In one sentence**: For a direct product of two symplectomorphisms (one with a basic set, the other acting on a compact surface with a non-degenerate elliptic equilibrium), the paper shows that under a local domination condition, typical real-analytic perturbations yield a large normally hyperbolic lamination carrying an ergodic natural invariant measure.
- **In plain words**: The paper studies a idealized mathematical model of a system that evolves while preserving volume-like structure, built by combining two simpler systems. It shows that, after a typical small smooth perturbation, the combined system has a large, layered family of unstable-but-structured sets on which the natural measure of the dynamics cannot be split into smaller invariant pieces, meaning the motion mixes across that set in a single, indivisible way. The argument combines several tools, including KAM theory (which controls stable quasi-periodic motion) and geometric measure theory.
- **Why it matters**: Ergodicity, the property that a system's long-run behaviour is spread evenly over its available states, is a central question in dynamics and Hamiltonian mechanics. The abstract claims the proof introduces a new geometric source of semi-local ergodicity and may be adaptable to more general settings, but the text provided does not show how far that reach extends.
- **Background needed**: - Symplectomorphism: a map that preserves the geometric structure underlying Hamiltonian mechanics (in particular, phase-space volume).
- Direct product: running two independent systems side by side as one combined system.
- Basic set and elliptic equilibrium: a chaotic invariant set, and a fixed point where nearby orbits circle around in a stable way.
- Normally hyperbolic lamination: a layered family of invariant sets that is unstable in a controlled, transverse way.
- Ergodic measure: a natural way of measuring time spent in regions, where the system cannot be decomposed into smaller invariant pieces.
- KAM theory: results showing that stable quasi-periodic motion survives small perturbations.
- Real-analytic perturbation: a small change to the system that is smooth in a strong sense. · level: research-level

<details><summary>Original abstract</summary>

We consider the direct product of two symplectomorphisms, one of which exhibits a basic set and the other one acts on a compact surface and has a non-degenerate elliptic equilibrium. Under a local domination condition we show that a typical real-analytic perturbation of this system displays a large normally hyperbolic lamination on which the natural invariant measure is ergodic. The proof, which introduces a novel geometric source of semi-local ergodicity, combines tools ranging from KAM theory to geometric measure theory and is robust enough to be of interest in more general configurations.

</details>

## Combinatorics

### [Small spherical 7-designs in prime dimensions](https://arxiv.org/abs/2611.26879)
*Andriy Bondarenko, Dmytro Mitin* · `math.CO` · arXiv:2611.26879v1 · relevance 0.14

- **In one sentence**: The paper constructs an antipodal spherical 7-design on the unit sphere in dimension p-1 for every prime p at least 29, with 42(p-1)(p+2)^2 points, using eigenlines of finite Weil operators.
- **In plain words**: The paper is about placing a finite set of points evenly over the surface of a high-dimensional ball so that averaging certain smooth functions over those points gives the same answer as averaging over the whole surface. For every prime number p of at least 29, the authors give an explicit construction of such a point set on the sphere of dimension p-1. The text gives the number of points used but, in this excerpt, no comparison with other constructions.
- **Why it matters**: Good, evenly spread point sets on spheres are useful in numerical integration, coding theory and quantum information, so a construction with an explicit point count for a whole infinite family of dimensions is of interest. The excerpt does not show how this count compares with known bounds or what applications it has, so its wider significance is uncertain.
- **Background needed**: - A sphere here means the surface of a ball in many dimensions, not just the ordinary 3D sphere.
- A spherical t-design is a finite set of points whose average of every polynomial of degree at most t equals the average over the full sphere; 7-design means degree up to 7.
- Antipodal means the point set contains each point together with its opposite point.
- A prime p is a whole number divisible only by 1 and itself; the construction works for primes p of at least 29.
- Weil operators are objects from finite-field and harmonic analysis; "eigenlines" are the special directions they leave unchanged up to scaling. The excerpt does not explain these in detail.
- Reading the paper in full requires familiarity with representation theory and finite fields. · level: research-level

<details><summary>Original abstract</summary>

For every prime $p\ge 29$, we construct an antipodal spherical $7$-design on $S^{p-1}$ with $42(p-1)(p+2)^2$ points. The construction uses eigenlines of finite Weil operators.

</details>

### [Extremal problems for graphs with bounded $k$-th binding number](https://arxiv.org/abs/2611.27699)
*Ao Fan, Ruifang Liu* · `math.CO` · arXiv:2611.27699v1 · relevance 0.12

- **In one sentence**: The paper determines the maximum number of edges and the maximum spectral radius among n-vertex graphs whose k-th binding number is below a given r, and characterizes the extremal graphs, generalizing known k=1 results.
- **In plain words**: This is about graphs, meaning networks of points joined by lines, and a measure called the k-th binding number that indicates how robustly a network can be split into matching-like pieces. The authors ask how many connections such a network can have while keeping this measure below a fixed threshold. They give exact answers for the largest number of edges and for the largest spectral radius (a single number summarizing the network's connectivity), and they identify which graphs achieve these maxima.
- **Why it matters**: Extremal problems of this kind show exactly which structures are the densest possible under a constraint, which is a central theme in graph theory. The authors say their approach, which links neighborhood inequalities to the complement of a graph, may extend to other Turán-type problems involving the k-th binding number, but the text does not show how far that extends.
- **Background needed**: - A graph is a set of vertices (points) joined by edges (lines); its order is the number of vertices.
- A perfect matching pairs up all vertices using disjoint edges; a k-factor is a spanning subgraph where every vertex has degree k.
- The binding number measures how much neighborhoods of vertex sets expand; Anderson showed that binding number at least 4/3 guarantees a perfect matching, and this bound is sharp.
- The k-th binding number generalizes this to k-factors; Chen et al. showed that a value of at least 1 guarantees a k-factor when kn is even.
- Turán-type problems ask for the maximum number of edges in a graph avoiding a given property.
- The spectral radius is the largest eigenvalue of the adjacency matrix, a matrix recording which vertices are joined.
- Complement of a graph: the graph on the same vertices with exactly the missing edges. · level: research-level

<details><summary>Original abstract</summary>

The binding number of a graph, introduced by Woodall [J. Combin. Theory, Ser. B, 1973], is a central topic in structural and extremal graph theory. Recently, Chen et al. introduced the $k$-th binding number $\beta^k(G)$. Anderson [J. Combin. Theory, Ser. B, 1971] proved that every graph $G$ of even order with $\beta^1(G)\ge\frac43$ contains a perfect matching, and that the bound $\frac43$ is best possible. For $k\ge2$, Chen et al. proved that $\beta^k(G)\ge1$ guarantees a $k$-factor whenever $kn$ is even, and that the bound $1$ is best possible. The above facts reveal a fundamental distinction between the higher-order binding number and the classical binding number. This distinction makes extremal problems for graphs with bounded $k$-th binding number particularly intriguing. For positive integers $n,$ $k$ and $r$, we in this paper determine the maximum size and spectral radius among all graphs $G$ of order $n$ satisfying $\beta^k(G)<r$, and characterize the corresponding extremal graphs, respectively. In particular, when $k=1$, our results imply the corresponding extremal results of Fan and Lin [Electron. J. Combin., 2024] and Liu, Chen and Fan [Electron. J. Combin., 2026]. Our proofs develop a structural framework that relates higher-order neighborhood inequalities to the structure of the complements of graphs. This framework may provide an approach to Tur\'{a}n-type problem involving the $k$-th binding number, and the approach may be of independent interest.

</details>

## Numerical analysis

### [Convergence of a finite element Chorin projection method for the stochastic Navier--Stokes equations](https://arxiv.org/abs/2611.27969)
*Franziska Weber* · `math.NA` · arXiv:2611.27969v1 · relevance 0.16

- **In one sentence**: Convergence analysis of a fully discrete finite element Chorin projection scheme for the stochastic incompressible Navier--Stokes equations with multiplicative noise and Dirichlet boundary conditions, showing convergence of a subsequence to a martingale solution in two and three dimensions.
- **In plain words**: This paper studies a computer method for simulating fluid flow (like water or air) that is incompressible and also randomly disturbed by noise. The authors show that their step-by-step numerical scheme, under stated conditions linking the grid size in space to the time step, produces approximations that converge (along a subsequence) to a solution of the random fluid equations. They also run numerical tests in two dimensions on smooth and vortex-sheet starting conditions.
- **Why it matters**: Random fluid models are used when measurements or forces are uncertain, so having a method with a proven convergence guarantee matters for trusting such simulations. The text does not indicate applications beyond this general setting, and the stated results are limited to the conditions listed in the abstract.
- **Background needed**: - Navier--Stokes equations: the standard equations describing how viscous fluids move.
- Incompressible: the fluid does not compress, so velocity must be divergence free (no sources or sinks).
- Stochastic / multiplicative noise: random forcing whose strength can depend on the current state of the flow.
- Finite element method: splitting a domain into small pieces and approximating the solution piece by piece.
- Chorin projection method: a time-stepping approach that first predicts the velocity and then corrects it to enforce incompressibility.
- Martingale solution: a weak notion of solution for random equations, defined through probability laws rather than fixed paths.
- Tightness and Aldous' criterion: tools from probability for showing a family of random processes is not spreading out, so limits exist.
- Convergence of a subsequence: only part of the sequence of approximations is shown to converge. · level: research-level

<details><summary>Original abstract</summary>

We analyze a fully discrete finite element projection method for the stochastic incompressible Navier--Stokes equations with homogeneous Dirichlet boundary conditions and multiplicative noise. We show solvability and uniform moment estimates for the intermediate and the corrected velocity approximations under the assumption that the initial data is square-integrable and divergence free, and that the deterministic forcing term is bounded in $L^{q}(0,T;H^{-1}(D))$ for a sufficiently large $q$. Under standard stability and approximation assumptions on the finite element spaces and a coupling condition on the spatial and temporal discretization parameters, we prove convergence of a subsequence to a martingale solution of the stochastic Navier--Stokes equations. The analysis combines the complementary spatial and temporal estimates of the predicted and the corrected velocity approximations and uses the numerical dissipation to identify their common limit. We establish tightness of the piecewise constant temporal interpolations of the velocity field approximations using Aldous' criterion combined with the uniform discrete moment estimates. The convergence result holds in two and three space dimensions as it does not rely on any additional regularity of the limiting martingale solution beyond the one naturally available from the energy inequality. Finally, we demonstrate the performance of the scheme in numerical experiments in two space dimensions for smooth and vortex sheet initial data.

</details>

### [A Validation-Driven Bilevel Optimization Method for Mesh-Free PDE Solvers and Its Error Analysis](https://arxiv.org/abs/2611.27347)
*Yongcun Song, Shangzhi Zeng, Jin Zhang et al.* · `math.OC` · arXiv:2611.27347v1 · relevance 0.14

- **In one sentence**: The paper proposes a validation-driven bilevel optimization framework for tuning design parameters of mesh-free PDE solvers (Kansa, random feature/extreme learning machine, and physics-informed neural network methods), using an efficient implicit hypergradient with warm-started damped Gauss-Newton and preconditioned minimum residual adjoint solves, together with local error bounds.
- **In plain words**: Scientists often solve equations describing physical systems by fitting a flexible formula to points scattered in space instead of a grid. Those solvers depend on several settings that are hard to choose, and the paper describes a way to pick them automatically by checking performance on held-out check points. For nonlinear equations, the authors make the calculation cheaper with a limited number of approximate steps and derive bounds on how much error those shortcuts introduce.
- **Why it matters**: Choosing solver settings strongly affects accuracy, and the paper offers a method meant to work across several solver families rather than one. The text reports numerical experiments on several nonlinear problems, including a high-dimensional one, but the broader significance beyond these tests is not established from the text alone.
- **Background needed**: - PDE (partial differential equation): a mathematical rule relating how a quantity changes in space and time, used to model physical phenomena.
- Mesh-free solver: a method that approximates a solution from scattered sample points rather than a fixed grid.
- Residual: how far an approximate solution misses satisfying the equation at a point.
- Bilevel optimization: a nested problem where an outer choice (settings) is made by judging the result of an inner fitting step.
- Validation set: held-out points used to judge settings without training on them.
- Hypergradient: the gradient of the outer score with respect to the settings, needed to tune them efficiently.
- Gauss-Newton method: an iterative fitting technique for nonlinear least-squares problems; "damped" means steps are shortened for stability.
- Adjoint system: an auxiliary linear system used to compute the hypergradient; here it is solved iteratively with a preconditioner that speeds convergence.
- Physics-informed neural network (PINN): a neural network trained to satisfy a PDE and its boundary conditions. · level: research-level

<details><summary>Original abstract</summary>

Mesh-free partial differential equation (PDE) solvers construct discrete systems from residuals at sampled points. These solvers fit coefficients in a parameterized trial representation and select solver-design parameters governing the representation, training-residual weighting, and regularization. These parameters strongly affect solution accuracy, yet existing selection strategies are largely tailored to particular solver classes. To address this limitation, we formulate a unified validation-driven bilevel optimization framework applicable across different solver classes, in which the lower level fits coefficients using training collocation residuals, while the upper level selects solver-design parameters using held-out validation residuals. For nonlinear PDEs, however, solving the nonlinear lower-level problem to high accuracy is costly, while the adjoint system is typically ill-conditioned and indefinite. To address this issue, we propose an efficient implicit hypergradient method that approximates the lower-level response using finite, warm-started damped Gauss-Newton (GN) updates. For the adjoint solve, we use the damped GN matrix to compute an initial adjoint and to precondition a finite number of minimum residual iterations. To quantify the errors introduced by these approximations, we derive local hypergradient error bounds that separate the contributions of the finite lower-level solve, adjoint damping, and the final adjoint residual. Combining this analysis with validation sampling bounds and residual stability, we relate validation residuals to PDE solution accuracy and establish error bounds for the computed PDE solution. Numerical experiments on several nonlinear PDEs, including a high-dimensional problem, demonstrate the accuracy and efficiency of the proposed method across Kansa, random feature and extreme learning machine, and physics-informed neural network solvers.

</details>

## Logic and foundations

### [Bridging Badiou's Gaps: Topos Theory and the Bodies of Mathematical Expression](https://arxiv.org/abs/2611.27280)
*Antti Veilahti* · `math.CT` · arXiv:2611.27280v1 · relevance 0.11

- **In one sentence**: A philosophical reconstruction of Alain Badiou's use of topos theory (in Being and Event and Logics of Worlds), recasting his forcing, semantic-expression and subjectification arguments in a categorical framework and reading topoi as "bodies of mathematical expression."
- **In plain words**: The paper looks at how philosopher Alain Badiou used a branch of advanced mathematics, topos theory, to support his ideas about truth, subjects and change. The author argues Badiou relied on a narrow version of that mathematics, and that a fuller, geometric version changes what his concepts of subject, body and event can mean. The text says its aim is conceptual rather than to add new mathematical results.</plain>
<parameter name="why">It connects the philosophy of mathematics with the way Badiou's system of ideas is read, and it is a second stage of a debate begun in 2013. The excerpt does not show how much influence it has beyond specialist readers of Badiou.
- **Background needed**: - Alain Badiou: French philosopher whose work uses set theory and related mathematics to describe events, truth and subjects.
- Set theory: the standard foundation of mathematics, built from collections of objects.
- Forcing: Paul Cohen's technique for building new mathematical models by extending existing ones; Badiou uses it as a model of how new truths appear.
- Topos (plural topoi): a generalised kind of mathematical universe, studied in category theory, which can have its own internal logic.
- Category theory: a framework that studies mathematical structures through the relationships (maps) between them rather than their elements.
- Localic / Grothendieck topoi: specific families of topoi; "localic" versions are a narrower, more set-like case.
- Kripke-Joyal semantics: a way of assigning meaning to logical statements inside a topos.
- Johnstone's "universe of discourse": a description of a topos as a setting in which a body of mathematical reasoning takes place. · level: research-level

<details><summary>Original abstract</summary>

This article develops a second stage of an argument begun in 2013, revisiting Alain Badiou's use of topos theory in Being and Event and Logics of Worlds. The previous article diagnosed Badiou's reduction of topos theory to its atomistic, localic form as the scientific scapegoat in his attack on 'democratic materialism'. Now I ask what follows when this logicist illusion is dispelled and the categorical alternative is taken seriously, particularly with respect to forcing, semantic expression, and mathematical subjectification that constitute the key elements of Badiou's earlier work. I thus reconstruct Badiou's own arguments in a corrected form, while transferring them to a categorical framework. The aim is not to introduce new mathematical results, but to identify what is conceptually lost through their reduction to set-theoretic formalism. In particular, I describe Cohen's forcing argument in the context of Grothendieck topoi and Kripke-Joyal semantics, thereby explicating the geometric structures implicit in Badiou's thinking. This reconstruction further brings into view a different way of understanding Badiou's concepts of subject, body, and change. Rather than treating a topos as merely a formal container for mathematical objects, I propose reading it as a body of mathematical expression, aligning with Johnstone's characterization of a topos as a 'universe of discourse'. At the same time, the geometrization of logic allows Badiou's own four-fold typology of change - when applied to topos theory itself as a mathematical 'event' - to be anchored to various historical definitions of a topos. In this way, the article bridges Badiou's two major works while clarifying how his own limited expression of mathematical formalism embodies his 'dialectical', ultimately singular concept of the event, and the way it clouds his philosophical understanding of locality and temporality.

</details>

### [The Power Of Enumerations](https://arxiv.org/abs/2611.27239)
*Karthik Ravishankar* · `math.LO` · arXiv:2611.27239v1 · relevance 0.08

- **In one sentence**: The paper studies the computational strength of enumeration degrees of generic and random sets, showing limits on what enumerations of 3-generics and weak 2-randoms can compute and mapping which Turing degrees can lie above quasiminimal enumeration degrees, answering a question of Slaman and Sorbi.
- **In plain words**: This is about how much information can be extracted from "typical" infinite sets of binary digits, the kind that look random in a precise logical sense. The authors ask whether listing all the members of such a set (an "enumeration") can itself produce another typical set. They find that this works at low levels but fails at higher ones, and they also map which simpler kinds of computable information can sit above certain minimal-looking enumeration degrees.
- **Why it matters**: The results sharpen our picture of how randomness and genericity behave under the enumeration reducibility, a weaker notion of computing than Turing reducibility. The answer to the Slaman and Sorbi question is a concrete structural fact about this part of computability theory; the text does not indicate wider applications.
- **Background needed**: - Computability theory asks what can be computed from what, measured by "degrees" of information.
- Turing degree: the usual notion where a set can be computed from another using a program with oracle access.
- Enumeration degree: a weaker notion, where a set is obtained by listing (enumerating) the members of another set, with no direct test of non-membership.
- Generic and random sets: "typical" infinite sets that avoid all simply describable exceptional properties; k-generic and k-random indicate levels of this typicality, with weak versions being a looser notion.
- Quasiminimal degree: an enumeration degree with no nontrivial non-total degrees strictly below it, roughly a very low-complexity point.
- PA degrees: Turing degrees that compute completions of Peano arithmetic, a class of sets with specific logical strength.
- Dimension 1 sets: sets with a particular effective density measure, a finer complexity notion. · level: research-level

<details><summary>Original abstract</summary>

We study the computational strength of enumerations of generic and random sets, particularly its interplay with computing these `typical' sets. We show that, while enumerations of $2$-generics can compute $2$-generics, this fails at higher levels---every $3$-generic has an enumeration which computes no weak $3$-generic. The analogous statement holds for randoms---every weak $2$-random has an enumeration which computes no $1$-random. We then analyze the total degrees above a quasiminimal enumeration degree, showing certain restrictions as well as certain positive results on the possible Turing degrees in such a cone. This answers a question of Slaman and Sorbi, by showing that there are quasiminimals with no minimal Turing degrees above them. We also show that while every total degree above some quasiminimals compute dimension $1$ sets, the total degrees above any quasiminimal fail to be a subset of the PA degrees.

</details>

## Mathematical physics

### [Brane Tilings and Polygons with Two Interior Points](https://arxiv.org/abs/2611.27861)
*Rak-Kyeong Seong* · `hep-th` · arXiv:2611.27861v1 · relevance 0.11

- **In one sentence**: A complete classification of brane tilings, quiver gauge theories, and their mesonic moduli spaces for toric Calabi-Yau 3-folds whose toric diagrams are convex lattice polygons with exactly two interior lattice points (45 polygons, 323 toric phases).
- **In plain words**: This paper is a large catalogue in theoretical physics and geometry. It looks at shapes with exactly two interior grid points, which encode certain six-dimensional geometric spaces used in string theory, and at the physical theories linked to them. The authors list all 45 such shapes, find 323 distinct physical versions (toric phases) for them, and for each one give a diagram (a brane tiling), its equations, and some summary data about its symmetries.
- **Why it matters**: The text presents this as a full enumeration rather than a new physical principle, so its value is mainly as a reference dataset for researchers studying the link between geometry and supersymmetric gauge theories. Its broader significance beyond that community is not stated in the text.
- **Background needed**: - Toric Calabi-Yau 3-fold: a six-real-dimensional geometric space from string theory, built from a polygon on a grid.
- Toric diagram: a lattice polygon whose shape encodes the geometry; interior points count certain features.
- Brane tiling: a periodic graph on a torus that encodes a supersymmetric 4d gauge theory.
- Quiver gauge theory: a theory described by nodes (gauge groups) and arrows (matter fields), with a superpotential giving interaction terms.
- Toric phase: one of several distinct gauge theories that share the same underlying geometry.
- Mesonic moduli space and Hilbert series: the space of gauge-invariant combinations of fields, and a generating function counting them.
- Superconformal U(1)R charge: a symmetry charge fixed by the theory's conformal behaviour. · level: research-level

<details><summary>Original abstract</summary>

We fully classify the brane tilings and the 4d N=1 supersymmetric quiver gauge theories corresponding to toric Calabi-Yau 3-folds whose toric diagrams are convex lattice polygons with two interior lattice points. There are 45 such polygons up to GL(2,Z) transformations and lattice translations: 5 triangles, 19 quadrilaterals, 16 pentagons and 5 hexagons. We identify all 323 toric phases corresponding to these toric Calabi-Yau 3-folds. For every toric phase, we present the brane tiling with its quiver and superpotential, the perfect matching matrix and the F- and D-term charge matrices. For each brane tiling, we study the mesonic moduli space of the corresponding abelian 4d N=1 theory through its Hilbert series and plethystic logarithm, and identify its generators and their leading relations. We also identify the mesonic global symmetry for each brane tiling and determine the superconformal U(1)R charges.

</details>

### [The moments and asymptotic spectral distribution of the Grassmannian ensemble](https://arxiv.org/abs/2611.27914)
*Aryan Gadhave, Asghar Ghorbanpour, Liam Hickey et al.* · `quant-ph` · arXiv:2611.27914v1 · relevance 0.07

- **In one sentence**: The paper computes all tracial moments and mixed reduced-state moments of partial traces of projections onto random subspaces (a Grassmannian ensemble) via Weingarten calculus, proves almost-sure convergence of the spectral distribution to a rescaled Marchenko-Pastur law, gives an alternative free-probability proof, and expands the average entanglement entropy asymptotically.
- **In plain words**: The paper studies random "density matrices," which are mathematical descriptions of the state of a quantum system split into two parts. These are generated by picking a random subspace of the combined space, taking projections onto it, and tracing out one part. The authors compute the relevant averages exactly and show that, for large systems, the spread of eigenvalues settles into a known shape (a rescaled Marchenko-Pastur law); they also estimate the typical entanglement between the two parts.
- **Why it matters**: Random-state models of this kind are used to describe what a "typical" quantum state looks like, which matters for quantum information and statistical physics. The text gives a rigorous route to the large-size limit and an alternative proof via free probability, but its wider implications beyond these models are not stated in the text.
- **Background needed**: - Density matrix: a matrix describing a quantum state; its eigenvalues are nonnegative and sum to one.
- Partial trace: averaging out one subsystem to get the state of the other.
- Grassmannian: the space of all subspaces of a fixed dimension; a random subspace is a random draw from it.
- Tracial moments: averages of powers of a matrix's trace, which encode its eigenvalue distribution.
- Weingarten calculus: a standard technique for integrating polynomial functions of random unitary matrices.
- Marchenko-Pastur law: the limiting eigenvalue distribution of large random matrices of a certain type.
- Free probability: a framework for the behavior of large random matrices that are "asymptotically free" (statistically independent in a noncommutative sense).
- Entanglement entropy: a measure of how strongly two subsystems are correlated in a quantum state. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study random density matrices constructed by taking partial traces of projections onto random subspaces of a bipartite Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_{B}$ distributed according to the pushforward measure of the action of the unitary group on the Grassmannian $\text{Gr}_{n}(\mathcal{H}_A \otimes \mathcal{H}_{B})$. This ensemble models a `typical' quantum subspace. All tracial moments of the density operator, as well as mixed tracial moments of reduced density operators, are computed explicitly using Weingarten calculus. There are several consequences of these results. In particular, we prove that the empirical spectral distribution of the density operator converges almost surely to a rescaled Marchenko-Pastur law. We also prove that this ensemble can be written as a sum of asymptotically free random density operators, leading to an alternative proof of the convergence of the spectral distribution. Finally, we compute the asymptotic expansion of the average entanglement entropy.

</details>

## Optimization and control

### [Small noise limit for Entropic Variational Mean-Field Games](https://arxiv.org/abs/2611.27695)
*Alessandro Cosenza, Luca Nenna* · `math.AP` · arXiv:2611.27695v1 · relevance 0.25

- **In one sentence**: The paper proves that small-noise limits of second-order variational mean-field games, studied through an entropy-minimization (Lagrangian) formulation, Gamma-converge to a deterministic first-order problem, and derives a first-order energy expansion that selects particular minimizers in the deterministic Eulerian problem.
- **In plain words**: The paper studies models of many interacting agents that move under random noise and each try to minimize a cost, in the limit where the noise gets very small. It shows that as the noise shrinks, these randomized models converge in a precise mathematical sense to a noise-free deterministic version. The authors also say this gives a new, dynamical route to the known fact that a randomized transport problem (the Schrödinger problem) approaches classical optimal transport.
- **Why it matters**: Mean-field games describe large populations of strategic agents, and optimal transport is a standard way to move mass from one distribution to another. The text links the small-noise limit to both, and to a selection principle that picks out specific minimizers of the deterministic problem, but it does not discuss applications beyond these theoretical connections.
- **Background needed**: - Mean-field game: a model where a very large number of agents each optimize a cost that depends on the overall population distribution.
- Variational formulation: the equilibrium is characterized as the minimizer of a single energy or cost functional.
- Second-order vs first-order: second-order models include random noise (diffusion); first-order models are deterministic.
- Entropy minimization: a penalty measuring how far a random process departs from a reference, used as the cost in the Lagrangian (path-based) formulation.
- Eulerian vs Lagrangian: Eulerian tracks densities and velocity fields at fixed points in space; Lagrangian tracks individual paths.
- Gamma-convergence: a notion of convergence for minimization problems that ensures minimizers of the approximating problems approach minimizers of the limit problem.
- Schrödinger problem and optimal transport: the former is a noisy, entropy-regularized version of the latter, which is the deterministic cost-minimal way to move one distribution to another. · level: research-level

<details><summary>Original abstract</summary>

We study second order variational mean-field games with quadratic Hamiltonian. In analogy with entropic optimal transport, Benamou, Carlier, Di Marino and the second author recently proposed an entropy-minimization formulation of the problem, which could be interpreted as the Lagrangian counterpart of the classical Eulerian approach. We investigate the small-noise $\Gamma$-limit for the Lagrangian entropy-minimization formulation and establish $\Gamma$-convergence of second order mean-field games towards their deterministic first order counterpart. This also translates into another (dynamical) proof of the convergence of the Schr\"odinger problem to optimal transport. Moreover, we study the original Eulerian problem and prove a first order energy expansion, which establishes a selection principle for minimizers of the deterministic problem.

</details>

### [Approximating technique for the solution to the ${H}^{\infty}$ -optimal control problem](https://arxiv.org/abs/2611.27520)
*Gabriela Marinoschi* · `math.AP` · arXiv:2611.27520v1 · relevance 0.23

- **In one sentence**: The paper proposes an approximation scheme that builds a sequence of infinite-dimensional systems whose H-infinity optimal control solutions (and associated Riccati equations) converge to those of the original robust stabilization problem, with a worked example.
- **In plain words**: The paper is about designing a controller that keeps a dynamical system stable even when its behaviour is uncertain or disturbed, a problem known as H-infinity robust control. Because the exact solution is hard to compute directly, the author builds a sequence of simpler approximating systems and shows that their solutions approach the true one. A closing example shows how the solution to the governing equation and the controller are calculated in practice.
- **Why it matters**: Robust controllers of this kind matter for engineering systems that must tolerate modelling errors and outside disturbances, and a provable convergence result gives confidence that computed controllers approximate the real optimal one. The text does not indicate specific applications or how the method compares with existing numerical techniques, so its practical reach is unclear from the abstract alone.
- **Background needed**: - Control theory: a feedback controller adjusts a system's inputs based on its measured state to achieve a goal such as stability.
- Robust stabilization: keeping a system stable despite uncertainty or disturbances.
- H-infinity control: a standard framework that minimizes the worst-case effect of disturbances on the system's output.
- Riccati equation: a nonlinear matrix equation whose solution gives the optimal feedback controller in many linear-quadratic and H-infinity problems.
- Infinite-dimensional systems: systems whose state is a function (e.g., of space), not a finite list of numbers, such as heat or wave-type processes.
- Approximation and convergence: replacing a hard problem by a sequence of easier ones and proving the answers approach the true answer.
- Prior work: the paper continues results by G. Marinoschi published in Applied Mathematics and Optimization (2026). · level: research-level

<details><summary>Original abstract</summary>

This paper continues the results published in [G. Marinoschi, Appl. Math. Optimiz. 94:44, 1-29, 2026], by presenting an approximating method of calculating the solution to the $H^{\infty }$-optimal control problem, which solves the robust stabilization of a system by a feedback controller, and to the associated Riccati equation. This method generates a sequence of infinite dimensional systems approximating the original system and the solution to the approximating $H^{\infty }$-optimal control problem is proved to converge to the solution of the original $H^{\infty }$-optimal control problem. An example for calculating the solution to the Riccati equation and the feedback controller is provided at the end.

</details>

## Statistics theory

### [Pathwise Factorization and Uncertainty Quantification for Impedance Obstacles with Random Boundaries](https://arxiv.org/abs/2611.26761)
*George Pelekanos, Koung Hee Leem* · `math.NA` · arXiv:2611.26761v1 · relevance 0.09

- **In one sentence**: A factorization method for locating two-dimensional impedance obstacles with random boundaries from finitely many noisy multistatic measurements, with finite-sample guarantees, simultaneous confidence bands, and a combined-field integral equation computed on a finite grid.
- **In plain words**: The paper studies how to find the shape of an object that sound waves bounce off when that object's edge is not fixed but random, using only a limited number of noisy measurements. The authors build a statistical version of a known shape-recovery method and prove that its estimates come with finite-sample guarantees. They also describe confidence bands, a way to estimate the probability that a given point lies inside the random object, and a check of their error bounds against a high-accuracy Monte Carlo reference.
- **Why it matters**: Reliable shape recovery with honest uncertainty estimates matters for imaging and nondestructive testing, where the object's boundary is itself uncertain. The text does not discuss specific applications, so any connection beyond acoustic scattering is something I cannot confirm from this text alone.
- **Background needed**: - Acoustic scattering: how waves reflect off an obstacle, and what the reflected far-field data look like.
- Impedance obstacle: an object whose surface partly absorbs or reflects waves according to a boundary condition, rather than being a perfect reflector.
- Factorization method: an inverse-scattering technique that tests sampling points to decide whether they lie inside the unknown object.
- Random boundary and multistatic data: the object's shape varies across realizations, and measurements come from many transmitter-receiver pairs.
- Finite-sample guarantees and confidence bands: statements that hold for a fixed, limited amount of data, and bands that cover an unknown function at many points at once.
- Monte Carlo reference: a brute-force simulation used as a benchmark for checking approximate methods. · level: research-level

<details><summary>Original abstract</summary>

We develop a factorization method with finite-sample statistical guarantees for two-dimensional acoustic scattering by impedance obstacles whose boundary is random and whose data are finitely many noisy multistatic measurements. In the two-dimensional far-field normalization, the symmetrization must act on a phase-rotated far-field operator; we prove the optical and range identities for every realization of a compact family of uniformly bi-Lipschitz domains, with jointly measurable regularized indicators. A quadrature-weighted finite-sample analysis separates angular approximation, measurement noise, test-vector error, and regularization, and yields a consistency theorem for empirical means and variances, joint in all data parameters. Bounded indicators admit simultaneous confidence bands, a diagonal threshold recovers the probability that a sampling point lies in the random obstacle, and a nested design yields unbiased variance components. Computations use a combined-field integral equation proved invertible at all frequencies, and the finite-grid guarantees are examined in a coverage study against a high-accuracy Monte Carlo reference.

</details>

### [An Asymptotic One-Sample Surrogate for Non-Gaussian ERM with General Convex Regularization](https://arxiv.org/abs/2611.27754)
*Tianjian Zhang, Cosme Louart, Malik Tiomoko et al.* · `math.ST` · arXiv:2611.27754v1 · relevance 0.07

- **In one sentence**: The paper builds a one-Gaussian-vector surrogate for convex empirical risk minimization with non-Gaussian features and nonsmooth penalties, proves its penalty calibration is well defined, and shows via a cavity Hamilton-Jacobi argument that the ERM minimizer and surrogate match in normalized means, prediction variances, and risks.
- **In plain words**: The paper studies a common statistical fitting procedure: choosing model settings by minimizing a penalized loss over data. Real data are not Gaussian (bell-curve shaped), which makes exact analysis hard. The authors replace the fitted solution with a simpler stand-in built from a single Gaussian random vector, and show that under stated conditions the stand-in gives nearly the same summary numbers as the real fit.
- **Why it matters**: Being able to predict how a fitted model behaves on new data, without relying on Gaussian assumptions, matters for reliable risk estimates in high-dimensional statistics. The text does not show practical applications beyond these theoretical risk formulas, so its wider impact is uncertain.
- **Background needed**: - Empirical risk minimization (ERM): fitting model parameters by minimizing average loss on training data.
- Convex penalty: an extra term that discourages large or complex parameter values; Lasso is a common example that pushes some parameters exactly to zero.
- Gaussian approximation: replacing a random quantity with a normal (bell-curve) distribution with matching key features.
- Poincaré inequality: a condition on how spread out a random variable is, used to control its fluctuations.
- Hamilton-Jacobi equation: a PDE-type tool used here to compare two optimization solutions as data are varied.
- Prediction risk and classification risk: expected error of predictions and expected rate of wrong class labels on new data. · level: research-level

<details><summary>Original abstract</summary>

We study convex empirical risk minimization (ERM) with non-Gaussian features and nonsmooth penalties through a surrogate driven by a single Gaussian vector. The surrogate preserves the penalty and calibrates its coefficients using the actual joint law of the feature-label model. We prove that this population calibration exists and is unique. We prove a Gaussian approximation for fresh prediction scores when the data satisfy a Poincar\'e inequality. Together with regularity conditions on the losses, this approximation yields agreement between the ERM minimizer and its surrogate in normalized means and prediction variances, as well as formulas for prediction and classification risks. The result covers general uniformly strongly convex penalties and pure Lasso under projection anti-concentration. The core proof relies on a cavity Hamilton-Jacobi argument that compares the main statistics of the two minimizers without differentiating the penalty.

</details>

## Statistical methods and applications

### [Hidden Semi-Markov Models for Fully Functional Time Series](https://arxiv.org/abs/2611.26838)
*Jake Hoover, Adam B Kashlak, Giseon Heo* · `stat.ME` · arXiv:2611.26838v1 · relevance 0.23

- **In one sentence**: The paper extends hidden semi-Markov models to fully functional time series, embedding the semi-Markov chain in a larger Markov chain so that Baum-Welch and Viterbi fitting apply, and applies this to pediatric EEG data within a Gaussian-measure framework on locally convex spaces.
- **In plain words**: The paper studies data that arrive as whole curves over time, such as brain-wave recordings, where an unseen "state" drives the pattern and changes now and then. Standard models assume each state's duration fades at a fixed rate, which can be too restrictive. The authors let each state last for a data-driven length of time, modeled either with a named counting distribution (such as the negative binomial) or without assuming a shape, and they fit it with established algorithms. They illustrate the approach on overnight sleep-study EEG recordings from children.
- **Why it matters**: Allowing hidden states to last for realistic, flexible durations may give a better description of biological signals such as sleep EEG. The text does not report comparative results against existing models, so the practical gain is not established by this summary alone.
- **Background needed**: - Hidden Markov model: a model where an unobserved state switches over time, and each switch depends only on the current state.
- Markov property: the future depends only on the present state; this implies state durations decay geometrically, which is the restriction the paper relaxes.
- Semi-Markov model: a variant where the time spent in each state follows its own duration (sojourn time) distribution.
- Functional time series: each observation is a whole curve or function, not a single number.
- Baum-Welch and Viterbi algorithms: standard procedures for estimating model parameters and for finding the most likely hidden state sequence.
- Gaussian measures on locally convex spaces: a probabilistic framework for random functions in a broad mathematical setting.
- EEG and polysomnography: recordings of brain electrical activity during sleep. · level: research-level

<details><summary>Original abstract</summary>

Functional time series have a wide range of practical applications to modeling complex datasets such as Electroencephalogram (EEG) and other biological signals. Often latent states are hidden within the data dictating how a system is behaving and changing over time. The Hidden Markov Model (HMM) is one common and highly applicable latent state space model where the hidden state sequence evolves as a Markov chain. While the HMM has had much success modeling discrete, multivariate, and fully functional time series, it is also restricted by the Markov property which causes hidden states to persist only at geometrically decaying rates. This work investigates the implementation of hidden semi-Markov models for modeling fully functional time series data. This allows for the hidden state sequence to persist in a given state for a data-driven sojourn time, which can be parametrized by a discrete distribution (e.g. negative binomial) or left non-parametric. For efficient fitting of such a model, the hidden semi-Markov chain is embedded into a larger state space Markov chain and classic methods like the Baum-Welch and Viterbi algorithms are applied. We furthermore consider functional time series in the general setting of Gaussian measures in locally convex topological vector spaces. This is applied to a time series of pediatric EEG signals collected via overnight polysomnography.

</details>

### [A generalized Bayesian method for identifying local and global changepoints in dynamic network data](https://arxiv.org/abs/2611.26955)
*Yuhui Wang, Michael Jauch, Joshua Daniel Loyal* · `stat.ME` · arXiv:2611.26955v1 · relevance 0.10

- **In one sentence**: A generalized Bayesian method with a multinomial log loss, low-rank and sparsity-inducing priors, and Pólya-Gamma Gibbs sampling detects local and global changepoints in dynamic network data.
- **In plain words**: This paper looks at networks that change over time, such as who emails whom or which countries are in conflict with which, and asks when the overall pattern shifts. The authors built a statistical method that finds the moments of change, reports how uncertain each location is, and identifies which network features drive each change. They tested it on simulated networks and on two real datasets, an email network and an international conflict network.
- **Why it matters**: Spotting when a network's structure shifts matters in areas such as communication monitoring and international relations. The text claims the method is often more accurate and flexible than competitors on simulations, but the comparisons are only summarized here, so the strength of that claim should be checked in the full paper.
- **Background needed**: - Dynamic network data: a series of snapshots of who is linked to whom, taken at successive times.
- Adjacency matrix: a grid recording which pairs of nodes are connected.
- Changepoint: a time at which the statistical behavior of a series changes abruptly.
- Bayesian inference: combining prior beliefs with data to get a probability distribution over unknowns, here including changepoint locations.
- Generalized posterior: a Bayesian-style update that uses a chosen loss function instead of a full probability model, so it does not depend on knowing the true data-generating process.
- Low-rank structure and sparsity: assumptions that the network is governed by few underlying patterns and that most parameters are zero.
- Gibbs sampler: a simulation method that draws samples from a complicated posterior one piece at a time.
- Pólya-Gamma data augmentation: a technical trick that makes sampling from logistic-type models easier. · level: research-level

<details><summary>Original abstract</summary>

We introduce a generalized Bayesian approach to multiple changepoint analysis in dynamic network data based on a multinomial log loss function and a prior distribution that imposes low-rank structure and sparsity on the model parameters. The method can detect local and global changes in network structure by incorporating information from both the full adjacency matrices and network summary statistics. Moreover, the proposed method is agnostic to the true data-generating process. From the generalized posterior distribution, we can make simultaneous inferences with meaningful uncertainty quantification about the locations of changepoints as well as deduce the network attributes and summary statistics that characterize them. For posterior simulation, we develop an efficient Gibbs sampler based on P\'olya-Gamma data augmentation with a computational cost that grows linearly with the number of observed edges in the dynamic network. Simulations across several benchmark network models show that the proposed method is often more accurate and flexible than competitors. We demonstrate the practical value of the method through applications to an email communication network and an international conflict network.

</details>

## AI industry news

### [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence)
** · `openai.com` · OpenAI News · relevance 0.11

- **In one sentence**: A short piece arguing that perplexity, a standard language-model metric, could give developers a shared way to measure emerging AI capabilities.
- **In plain words**: The article looks at perplexity, a score that shows how well an AI language model predicts the next word in a text. It describes how this score can track progress in AI models and suggests it might help developers agree on a common way to judge new abilities. The text is brief and only gives this overview, so it does not report detailed experiments or specific results.
- **Why it matters**: Developers and researchers often disagree about how to compare AI systems, so a shared measure could make progress easier to discuss. Whether perplexity is suitable for judging newer abilities is an open question that the short text does not settle.
- **Background needed**: - Language model: an AI system trained to predict likely next words in text.
- Perplexity: a number where lower values mean the model is less "surprised" by real text, so it predicts better.
- Emerging capabilities: new skills that appear as models grow, such as reasoning or following instructions, which are harder to measure.
- Evaluation: the process of testing and scoring AI systems so they can be compared.
- Limitation: the text is a brief overview with no data, so details of its argument are unclear. · level: intermediate

<details><summary>Original abstract</summary>

How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

</details>

### [Finding faster quantum algorithms with agents and formal verification](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)
** · `deepmind.google` · Google DeepMind News · relevance 0.11

- **In one sentence**: A news piece describing the use of AI agent teams together with formal verification (machine-checked proofs of correctness) to improve quantum algorithms aimed at fusion energy and chemistry problems.
- **In plain words**: The article is about using teams of AI agents to find faster methods for running calculations on quantum computers, with applications in fusion energy and chemistry. The text is very short, so it only says that agent teams and formal verification were used to improve these algorithms; it does not describe the specific methods or the size of any improvement.
- **Why it matters**: Faster quantum algorithms could matter for simulating molecules and plasmas, which are hard for ordinary computers, but the text gives no results to judge how large the gain is. It may connect to wider efforts to use AI to speed up scientific software, though the article alone does not establish that.
- **Background needed**: - Quantum algorithm: a set of steps designed to run on a quantum computer, which uses quantum physics to process information differently from ordinary computers.
- Fusion energy: producing power by joining atomic nuclei, the process that powers the sun; simulating it is computationally demanding.
- Quantum chemistry: using computers to predict how molecules behave, useful for drug and materials design.
- Formal verification: using mathematical proof tools to show that a program or method is correct, rather than relying only on testing.
- AI agents: AI systems that carry out multi-step tasks, such as writing and checking code, with limited human direction.
- The article is brief and gives no numbers or technical details, so treat its claims as unverified until the original work is read. · level: intermediate

<details><summary>Original abstract</summary>

Using agent teams and formal verification to improve quantum algorithms for fusion and chemistry.

</details>

### [Amazon snaps up Decart’s AI optimization tech for $7.5B as it prepares to sell Trainium chips](https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.08

- **In one sentence**: Amazon is reportedly acquiring AI optimization technology and the research team of Decart for a reported $7.5 billion, as it prepares to sell its Trainium chips.
- **In plain words**: Amazon is reportedly buying a company called Decart, including its technology for making AI systems run more efficiently and the people who built it. The reported price is $7.5 billion. The article is short and gives few details beyond the deal itself and the headline's mention of Amazon's Trainium chips.
- **Why it matters**: Large acquisitions of AI efficiency talent and technology can signal where big cloud companies are investing to lower the cost of running AI. The article does not say how the technology will be used, so any link to Amazon's chip plans is only suggested by the headline.
- **Background needed**: - AI "optimization" means making models faster or cheaper to run, for example by using less computing power.
- Trainium is Amazon's own custom chip designed for training and running AI models, as an alternative to chips from other suppliers.
- An acquisition means one company buys another; "reported" means the price comes from press reports, not necessarily an official announcement.
- The article gives only a summary; details of the deal terms and the technology are not in the text. · level: introductory

<details><summary>Original abstract</summary>

Amazon is acquiring Decart’s AI optimization technology and research team in a reported $7.5 billion deal.

</details>

### [Why data centers are at the center of the Big Tech backlash](https://techcrunch.com/2026/11/22/why-data-centers-are-at-the-center-of-the-big-tech-backlash/)
*Anthony Ha* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.07

- **In one sentence**: A short piece previewing journalist Paris Marx's book "Hyperscale," which examines the public backlash against large tech companies' data centers.
- **In plain words**: This article is about growing public frustration with the huge computer facilities that power online services and AI, often called data centers. It introduces a new book by journalist Paris Marx, "Hyperscale," that digs into why these sites have become a flashpoint for criticism of Big Tech. The text itself is brief and does not spell out the specific arguments or evidence in detail.
- **Why it matters**: Data centers draw attention because they use large amounts of electricity and water and are being built quickly to support AI, so local and political pushback is plausible as a continuing issue. The text is too thin to say how strong the backlash is or what the book concludes.
- **Background needed**: - Data center: a large building full of servers that store data and run online services and AI models.
- Hyperscale: the term for the very largest data centers, built and run by a handful of major cloud companies.
- Big Tech: the largest technology firms, such as the major cloud and social media companies.
- Backlash: organized public opposition, which can involve local zoning fights, utility costs, or environmental concerns.
- Paris Marx: a tech writer and podcaster who critically examines the technology industry. · level: introductory

<details><summary>Original abstract</summary>

Journalist Paris Marx unpacks his new book "Hyperscale."

</details>

### [Sierra doubles valuation to $30B within six months as demand for AI in CX takes off](https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/)
*Ivan Mehta* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.06

- **In one sentence**: Sierra, a customer-experience AI startup co-founded by former Salesforce co-CEO Bret Taylor, reportedly raised $1.75 billion in a Series F round, reaching a $30 billion valuation.
- **In plain words**: A company called Sierra, which builds AI tools for businesses to handle customer service and similar interactions, announced it has raised $1.75 billion from investors. The news says its valuation, the estimated total worth of the company, has doubled to $30 billion within about six months. The article attributes this to strong demand for AI in customer experience.
- **Why it matters**: It is a sign of how strongly investors are backing AI tools for customer service, a large commercial market. The article is brief and reports the company's own announcement, so the figures and reasons for demand are not independently verified here.
- **Background needed**: - Series F: a late-stage funding round, usually after several earlier rounds, typically for a company that is already well established.
- Valuation: the estimated value of a company, often set by the price investors pay for shares; it is not the same as cash or profit.
- Customer experience (CX): all the interactions a customer has with a company, such as support chats, calls and help pages.
- Bret Taylor: former co-CEO of Salesforce, a large business software company, who co-founded Sierra.
- The article is a short news item with no details on products, customers, revenue or investors. · level: introductory

<details><summary>Original abstract</summary>

Enterprise customer experience company Sierra, co-founded by former Salesforce co-CEO Bret Taylor, said on Monday that it has raised $1.75 billion in a Series F round.

</details>

## Model architectures and training

### [Turnout: Adaptive Attention Switching for Efficient Reasoning](https://arxiv.org/abs/2611.27500)
*Anna Kuzina, Mart van Baalen, Paul N. Whatmough et al.* · `cs.LG` · arXiv:2611.27500v1 · relevance 0.33

- **In one sentence**: Turnout converts a pretrained full-attention transformer into a hybrid that can switch each layer between full and fixed-size linear attention during reasoning, with the switching policy learned by reinforcement learning under a reward for correctness and memory use.
- **In plain words**: Large language models remember what they have written so far in a memory store that keeps growing as they generate longer answers. This paper takes an existing model and swaps part of that growing memory for a fixed-size one, which saves memory but tends to make reasoning answers less accurate. The authors' method lets the model decide, layer by layer and during generation, when to use the full memory and when to use the cheaper one.
- **Why it matters**: Long reasoning chains make memory use a practical bottleneck, so a way to trade memory for accuracy in a controlled way could matter for running such models on limited hardware. The text reports that the learned policy gives a better accuracy-versus-efficiency trade-off than fixed or static baselines, but it gives no specific numbers here, so the size of the gain is unclear.
- **Background needed**: - Transformer attention: the mechanism in language models that looks back at earlier tokens; full attention stores a key-value cache that grows with output length.
- Linearization: replacing that growing cache with a fixed-size state, which uses less memory but can lose information.
- Post-hoc distillation: training a new, cheaper component to imitate an already-trained model, without retraining from scratch.
- Hybrid model: a model that contains both full and linear attention paths and can use either.
- Reinforcement learning: training a decision policy by rewarding good outcomes; here the reward balances answer correctness against memory use.
- Pareto frontier: the set of options where you cannot improve accuracy without spending more memory, or vice versa. · level: research-level
- Matched keywords: transformer, attention, linear attention, distillation

<details><summary>Original abstract</summary>

Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state. This change reduces memory consumption but often hurts accuracy. In reasoning tasks, which require long generations, this effect is especially pronounced. In this work we introduce Turnout, a method that mitigates accuracy loss as a result of linearization, while maintaining its memory-reduction benefits. We apply post-hoc linearization to a pretrained full-attention model, training a linear path through distillation while leaving the original full-attention path unchanged. During response generation, the resulting hybrid model retains both paths and uses a learned policy to control when each layer switches from full to linear attention. We train the policy with reinforcement learning using a reward that balances answer correctness and memory use. Empirical evaluation of our method shows that the learned adaptive policy achieves a better accuracy-efficiency Pareto frontier on reasoning tasks compared to fixed switching and static hybrid baselines.

</details>

### [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973)
*Chang Nie, Chaoyou Fu, Songlin Liu et al.* · `cs.CL` · arXiv:2611.27973v1 · relevance 0.30

- **In one sentence**: MemOnce proposes a language model architecture that stores compact final-layer hidden states as memory, decodes them back into attention KV caches on demand, and uses sparse retrieval whose indices are computed once and shared across layers, aiming for linear-time cost in long, continual use.
- **In plain words**: Chatbots and other language models normally keep a large working notebook of everything said so far, and that notebook grows quickly as conversations get longer. This paper proposes a different way to keep that memory: it saves only a small, compressed version of the model's internal notes and rebuilds the detailed working notes when they are needed. The authors report that, when they adapted a 4-billion-parameter Qwen3.5 model this way, the stored memory shrank about 1313 times and prefill latency (the initial processing delay before a reply) dropped 6.9 times at a 1-million-token context.
- **Why it matters**: Memory growth is a practical bottleneck for models used over long, repeated sessions, so a way to cut it while keeping detail could matter for deployment costs. The reported figures come from the authors' own experiments, and the text does not show how the approach performs on tasks beyond those described, so its wider significance is still unclear.
- **Background needed**: - Transformer language models store a KV cache: per-token key and value vectors for each layer, used so the model can look back at earlier text.
- That cache grows linearly with context length in GPU memory, and attention compute grows quadratically with it.
- Linear-time alternatives compress history into a fixed-size state, which is cheap but can lose fine detail.
- Sparse attention means each new input attends only to a selected subset of past memory rather than everything.
- Prefill latency is the delay before the model produces its first output token, while it processes the input.
- Results are reported by the authors; the text gives no independent validation. · level: research-level
- Matched keywords: attention, pretraining, architecture

<details><summary>Original abstract</summary>

Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures compress history into fixed-size states, but struggle to retain fine-grained details. We introduce MemOnce, a foundation architecture that learns scalable memory states for language models. MemOnce is based on two core designs: (a) Memory encoder-decoder: it caches only a small subset of final-layer hidden states as compact memory representations and dynamically decodes them back into KV caches for attention layers; (b) Memory sparse attention: for each continual input, MemOnce adaptively retrieves relevant memory representations, with the sparse indices computed only once across layers. Coupling these two designs enables efficient on-the-fly memory loading and KV cache decoding, drastically reducing the GPU memory footprint and achieving linear-time complexity. We conduct extensive experiments to show that MemOnce outperforms Transformers and other architectures across varying model sizes, context lengths, and training paradigms (pretraining and post-training adaptation). In particular, adapting Qwen3.5-4B with MemOnce reduces memory state cache by 1313$\times$ and prefill latency by 6.9$\times$ at 1M context, and improves throughput by 3.5$\times$ and overall memory performance by +5.77%. Finally, MemOnce generalizes zero-shot to downstream representation tasks, achieving competitive results against specialized models.

</details>

## Machine learning theory

### [Renormalized Entropy from Symmetries: Simplicity Bias and Neural Heat Death](https://arxiv.org/abs/2611.27889)
*Vasco Portilheiro, Samuel Liebana, Andrew Saxe et al.* · `cs.LG` · arXiv:2611.27889v1 · relevance 0.30

- **In one sentence**: The paper derives the equilibrium distribution over functions learned by neural networks under Langevin dynamics with Gaussian regularization, takes the regularization to zero, and uses a renormalization procedure to obtain a symmetry-induced entropy that favors low-rank, singular, or inactive-neuron functions.
- **In plain words**: Neural networks can be reparameterized in many ways that leave the function they compute unchanged, and this paper asks how those redundancies shape which functions a network ends up favoring. The authors model training as a random noisy process settling into equilibrium and study the case where the regularization is made very weak. They report an entropy term that pushes toward simpler functions, including, for homogeneous activations, a tendency for neurons to switch off, which they call neural "heat death" where the output vanishes.
- **Why it matters**: The work offers an explanation for implicit bias in neural networks, meaning why training tends to pick certain solutions without being told to, and links it to the neural tangent kernel. The text does not show how far these results extend beyond the linear and homogeneous-activation cases it treats, so its broader significance remains unclear from this summary alone.
- **Background needed**: - Parameter symmetry: changing a network's weights in a way that leaves the computed function identical (e.g., rescaling connected weights).
- Implicit bias: the tendency of training to prefer some solutions over others, even when many fit the data equally well.
- Langevin dynamics: gradient descent with added random noise, whose long-run behavior settles into an equilibrium distribution.
- Gaussian regularization: a penalty on large weights, here modeled as a Gaussian term; its strength is taken toward zero.
- Low-temperature limit: the regime where the noise is small, so the process concentrates near the lowest-cost settings.
- Entropy (here): a measure of how much parameter-space volume corresponds to a given function; more volume means more favored.
- Renormalization: a technique for removing divergent quantities so a finite, meaningful result remains.
- Neural tangent kernel: a linearized view of how a network's output changes with its parameters, used to describe which functions change slowly.
- Homogeneous activation: an activation such as ReLU where scaling the input scales the output by the same factor. · level: research-level
- Matched keywords: neural tangent kernel, implicit bias

<details><summary>Original abstract</summary>

Neural networks have parameter symmetries: parameter transformations that do not affect the represented function. How do these symmetries affect the functions that neural networks ultimately learn? We study the implicit bias arising from these symmetries by calculating the equilibrium distribution over represented functions under Langevin dynamics with Gaussian regularization. To isolate the effect of symmetries on this distribution, we study the limit in which the strength of the regularization is taken to zero. In certain cases, we show that the zero-regularization and infinite-time limits commute. In the low temperature limit, we recover known effective regularizations. At positive temperature, a renormalization procedure allows us to derive a novel entropy which predicts symmetry-induced preference for certain functions. For linear networks, we obtain explicit entropy terms that favor singular and low-rank functions. For networks with homogeneous activations, we find entropy terms that favor inactive neurons, which can lead to neural "heat death" in which equilibrium mass concentrates on networks with vanishing output. We interpret these results through the neural tangent kernel, as a simplicity bias selecting for functions that vary slowly under variations in the parameters.

</details>

### [Verifying and Strengthening Neural Tangent Kernel Theory](https://arxiv.org/abs/2611.27487)
*Hao Zhu* · `cs.LG` · arXiv:2611.27487v1 · relevance 0.26

- **In one sentence**: A Lean 4 machine-checked formalisation of the two-layer neural tangent kernel (NTK) convergence theorem for tanh networks under gradient flow, which also tightens the concentration-width bounds and identifies a Hessian-norm obstacle to the standard linearisation argument.
- **In plain words**: This work is about a mathematical explanation of why very wide neural networks, trained by repeatedly nudging their settings downhill, reliably fit their training data. The authors wrote out the full argument for a two-layer network in Lean, a proof assistant that checks each step by computer, and confirmed the main theorem: with high probability, training converges at an exponential rate under stated conditions. They also report that some of the standard bounds can be made much tighter, though the required network widths remain impractically large.
- **Why it matters**: Machine-checking a standard theory in machine learning is a useful test of whether its published proof steps hold as written, and the paper reports concrete places where the textbook analysis can be sharpened. The claimed improvements are numerical estimates for specific settings, and the paper itself notes the resulting widths are too large to matter in practice, so its direct practical impact appears limited.
- **Background needed**: - Neural network: a function built from layers of weighted sums and simple nonlinear steps, whose weights are tuned during training.
- Gradient descent / gradient flow: a method that adjusts weights step by step (or continuously in the limit) to reduce error.
- Neural tangent kernel (NTK): a simplified description of a wide network's behaviour during training, as if it were a fixed kernel method.
- Lazy training: the regime where weights barely move from initialisation while the network still fits the data.
- Concentration / random matrices: showing that random quantities stay close to their average with high probability, and how wide the network must be for this.
- Lean 4: a proof assistant language in which mathematical proofs are checked by computer.
- Operator norm and Hessian: measures of how strongly a function's sensitivity can change; used to control how far linear approximations are valid. · level: research-level
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

Writing Neural tangent kernel (NTK) theory explains why very wide neural networks trained by gradient methods converge in the lazy-training regime. Its standard proof combines matrix concentration, random Gram matrices, continuous-time dynamics, spectral perturbation, and a bootstrap argument, but has lacked machine-checked verification. We present a Lean\~4 formalisation for two-layer networks, proving an end-to-end theorem: for a smooth bounded activation (instantiated with $\sigma=\tanh$), frozen biases, paired $\pm 1$ initialisation, and explicit width conditions, gradient flow exists uniquely with probability at least $1-\delta$, and $$ \|r(t)\|^2 \leq \|y\|^2 e^{-\lambda_0 t/2}. $$ The sole data assumption is population NTK non-degeneracy, $\lambda_0>0$. Initial coercivity, kernel drift, the movement bootstrap, the residual ODE, and flow existence and uniqueness are formally proved. The formalisation also sharpens the standard analysis in two ways. First, replacing the conventional matrix-Bernstein variance proxy with the classical row-covariance proxy yields estimated concentration-width certificates for $\tanh$ that are $36$--$53\times$ smaller at $(m,d)=(16,8)$ and $94$--$121\times$ smaller at $(32,16)$. Lean certifies the inequality; the ratios are numerical. Second, the network Hessian has operator norm $\Theta(\sqrt{p})$ on the sup-norm parameter ball (a paper calculation), preventing the expected $O(1/\sqrt{p})$ linearisation bound via sup-norm Taylor estimates. An $L^2$ parameter geometry resolves this issue. Required widths remain polynomial but far beyond practical scales, limiting applicability.

</details>

## Large language models

### [Partially canonical axes in large language model representations](https://arxiv.org/abs/2611.26920)
*Andrea Gregor de Varda, Ferdinando D'Elia, Greta Tuckute et al.* · `cs.CL` · arXiv:2611.26920v1 · relevance 0.14

- **In one sentence**: Across 12 LLMs from six families, the native coordinate axes of hidden representations align better with other models, with human brain responses, and with interpretable linguistic features than randomly rotated axes do, though they fall short of the best achievable alignment ("partially canonical").
- **In plain words**: Researchers asked whether the individual numbered directions inside a large language model's internal state mean anything, or whether only combinations of them carry meaning. They compared each model's native axes with versions of the same data rotated to random orientations. The native axes matched other models, human brain activity during language, and simple linguistic features somewhat better than the rotated ones, but not as well as the best possible alignment.
- **Why it matters**: It challenges the common assumption that individual units in language models are arbitrary, which matters for interpretability work that inspects single neurons. The link to human brain responses is suggestive, but the text alone does not show how strong or useful that link is for theory.
- **Background needed**: - Hidden representation: the vector of numbers a model holds internally for a word or sentence.
- Coordinate axis: one of the individual numbered dimensions of that vector, the "neuron" or unit.
- Rotation: changing the orientation of the whole space, which preserves distances and overall geometry but scrambles which axis is which.
- Alignment: how closely two sets of representations match in structure, often measured by how well one predicts the other.
- Canonical vs arbitrary: "canonical" here means the axes pick out special, meaningful directions; "arbitrary" means any rotation would do equally well.
- Brain responses: recordings of human brain activity while people read or hear language, used as a comparison target. · level: research-level

<details><summary>Original abstract</summary>

Large language models (LLMs) develop rich internal representations of language, but whether their individual coordinate axes carry meaning, or whether meaning is encoded only in directions in representation space, is still an open question. A common assumption is that individual axes in LLMs are arbitrary. We here challenge this view: across 12 LLMs from six model families, the native axes are reliably more aligned with other models' representations, with human brain responses to language, and with interpretable linguistic features than randomly rotated axes that preserve the same geometry. The native axes nonetheless fall well short of the best achievable alignment, so LLM coordinates are not fully arbitrary but also not fully canonical: they are partially canonical. A theory of how LLMs represent language must explain both the population geometry they learn and why individual units acquire patterns of response profiles that recur across systems.

</details>

### [Explicit Style Extraction for Personalized Long-Form Text Generation](https://arxiv.org/abs/2611.27211)
*Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam et al.* · `cs.CL` · arXiv:2611.27211v1 · relevance 0.13

- **In one sentence**: SP-Refine makes style extraction an explicit inference-time step for personalized long-form generation, using a 28-aspect taxonomy (StylePrism) to build a user style profile that guides drafting and two rounds of self-revision on LongLaMP tasks.
- **In plain words**: Language models asked to write in a specific person's voice usually just receive a few of that person's past texts and have to guess what matters about their style. This paper proposes a fixed checklist of 28 style features in seven groups, has the model fill that checklist in from the user's writing, and then drafts and revises text against it. On three long-form writing tasks with three models, the method beat the standard retrieval-based baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average.
- **Why it matters**: Personalizing AI writing to individuals is a practical goal, and making style explicit rather than implicit may make it easier to inspect and control. The reported gains are measured on automatic overlap metrics only, and the ablations suggest the profile works best as revision guidance alongside the user's samples, so the benefit beyond these tasks is unclear.
- **Background needed**: - Retrieval-augmented generation (RAG): putting relevant example texts into a model's prompt before it writes.
- Long-form generation: producing multi-paragraph text such as articles or reviews, not short answers.
- ROUGE and METEOR: automatic scores that measure word overlap between generated text and a reference text.
- Inference-time method: a technique applied when the model is run, without retraining it.
- Ablation: a test that removes one part of a method to see how much it contributes.
- Oracle variant: a version that peeks at the answer, used to estimate an upper bound on gains. · level: intermediate

<details><summary>Original abstract</summary>

Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an explicit step: the model first fills StylePrism with the user's patterns, quoted evidence, and habits to avoid, then drafts from the user's samples and revises the draft twice against this profile, guided by its own style scores. On the three long-form tasks of LongLaMP with three LLMs, SP-Refine outperforms LongLaMP's retrieval-augmented baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average and by up to 35.8%. Annotating users' own texts with the extracted profiles shows that StylePrism captures concrete, checkable habits, from the order of rhetorical moves to a reviewer's sign-off. Ablations show that the profile helps as revision guidance, not as a replacement for the samples: writing from the profile alone is worse in all 27 comparisons, while a single implicit-inference call is a cheaper alternative that comes close. Oracle variants that let the reviser see the reference, together with reference-free controls, show that larger refinement gains require information unavailable at inference time.

</details>

## Computer vision

### [PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation](https://arxiv.org/abs/2611.27266)
*Junyi He, Xu Peng, Chengming Xu et al.* · `cs.CV` · arXiv:2611.27266v1 · relevance 0.18

- **In one sentence**: PP-CFG is a few-step diffusion distillation method that keeps positive and negative text conditions separate, combines their attention with opposite signs, and uses a learned scale-and-timestep mixer to keep adjustable classifier-free guidance and negative prompting working in four-step image and video generation.
- **In plain words**: AI image and video generators often make many small denoising passes to produce a picture, and speeding them up by squeezing the process into a few steps tends to remove the knobs that control how strongly the prompt is followed and what to avoid. This paper proposes PP-CFG, which keeps "what to include" and "what to exclude" prompts separate and combines them so that both controls still work in just a few steps. The authors report results on two existing models, Wan2.1 for video and Qwen-Image for images, plus a new 1,000-case test called NegElement-1K.
- **Why it matters**: Few-step generation is attractive because it is much cheaper to run, so keeping user control such as guidance strength and negative prompts could matter for practical tools. The text reports gains on a video quality benchmark and on removing unwanted elements, but these are the authors' own evaluations, and how well the approach holds up outside these models and tests is not shown here.
- **Background needed**: - Diffusion models generate images or video by starting from noise and removing it step by step.
- Sampling cost: each step needs a full pass through a large network, so fewer steps means faster output.
- Distillation: training a smaller or faster "student" model to imitate a slower "teacher" model.
- Classifier-free guidance (CFG): a setting that pushes output harder toward the prompt; a negative prompt describes what to avoid.
- DMD and LCM: two specific distillation methods for making few-step generators.
- VBench: a standard benchmark score for video generation quality; higher is better.
- Attention: the mechanism that lets the model weigh how parts of the text relate to parts of the image. · level: research-level

<details><summary>Original abstract</summary>

Few-step diffusion distillation reduces sampling cost but often weakens adjustable classifier-free guidance (CFG) and runtime negative prompting. We introduce PP-CFG, an architecture that keeps positive and negative text conditions separate and combines their attention responses with opposite signs within a shared visual backbone. Its Scale-Time Polarity Mixer refines each condition using the guidance scale and denoising timestep, allowing prompt influence to vary throughout generation. The student retains a continuous scale input and selectable negative prompts with one visual backbone pass per step. We evaluate PP-CFG on Wan2.1 for video generation with distribution matching distillation (DMD), and on Qwen-Image with both latent consistency model (LCM) distillation and DMD. PP-CFG achieves 81.46 VBench in four steps and lower video teacher-student distances across guidance scales than step-distilled DMD. On NegElement-1K, our benchmark of 1,000 matched image and video prompt cases, it achieves higher target-removal rates than the corresponding teachers. These experiments support the method's generality across attention architectures, generation modalities, and distillation objectives while retaining competitive generation quality.

</details>

### [Learning 3D MRI Representations with Generative Adversarial Networks](https://arxiv.org/abs/2611.27057)
*Sujeet Lahane, Sapna Mishra, Akash Suryavanshi et al.* · `cs.CV` · arXiv:2611.27057v1 · relevance 0.15

- **In one sentence**: The paper proposes R2RG, a reconstruction-based representation learning method that uses 3D convolutional networks with an auto-encoding GAN and a composite loss to learn features from small 3D MRI datasets.
- **In plain words**: Doctors' brain scans (MRI) are 3D volumes, but many AI tools analyze them as flat slices, losing depth information, and large AI models tend to need more data than medical datasets usually provide. This paper describes a method that learns compact summaries of whole 3D scans by training a network to rebuild the scan, with a GAN (a pair of networks that push each other to produce realistic output) helping sharpen the rebuilt image. The authors report better results than contrastive methods on Parkinson's and Alzheimer's classification, across three public datasets and one local dataset.
- **Why it matters**: Small medical datasets are a common bottleneck, and the paper's claim that reconstruction-based learning can work well with limited 3D data is worth checking against other studies. The text does not give enough detail to judge how large the gains are or how well the results hold beyond the reported datasets.
- **Background needed**: - Representation learning: training a model to turn raw data into compact numerical features that other tasks can use.
- MRI: magnetic resonance imaging, which produces 3D scans of tissue such as the brain.
- 3D CNN: a convolutional neural network that works on volumes rather than flat images, so it sees depth as well as width and height.
- Auto-encoder: a network that compresses an input into a small code and then tries to rebuild the original from that code.
- GAN: generative adversarial network, two networks trained against each other, one generating and one judging realism.
- Contrastive learning: a training approach that teaches a model to pull similar examples together and push different ones apart.
- Overfitting risk: with little data, large models can memorize training examples instead of learning general patterns. · level: research-level

<details><summary>Original abstract</summary>

Learning representations of visual images is a challenging task. It requires extracting abstract patterns from high-dimensional data without explicit supervision. This becomes pronounced with 3D MR imaging due to sparse features, higher dimensional inputs, and smaller datasets. Many state-of-the-art representation learning algorithms successfully rely on transformers and diffusion-based architectures. However, these methods struggle with smaller datasets. In effect, solution methods relax the problem by slicing 3D volumes and solving the problem for 2D medical imaging, resulting in a loss of spatial 3D information. We present R2RG, a representation learning method based on Convolutional Neural Networks (CNNs), with Generative Adversarial Networks (GANs) honing the reconstruction task. Our key insights lie in exploiting architectural biases in 3D CNNs, combined with data-efficient auto-encoding GANs and a composite loss function to enhance reconstruction fidelity and stabilize training. Our experiments on three standard datasets and a locally collected dataset show that R2RG not only achieves superior performance but also generalizes to heterogeneous and smaller datasets. Furthermore, representations learned with R2RG outperform those learned with contrastive-based representation learning methods on Parkinson's and Alzheimer's disease classification. Our work demonstrates that reconstruction-based representation learning is a promising direction for 3D medical imaging under limited data availability.

</details>

## Reinforcement learning

### [Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27368)
*Dennis Gross, J{\o}rn Eirik Betten, Helge Spieker* · `cs.MA` · arXiv:2611.27368v1 · relevance 0.23

- **In one sentence**: The paper proposes DisQ, a test-case selection method that uses a "Q-value gap" (disagreement between agents' value estimates in a state) to find failure-revealing states when testing value-based cooperative multi-agent reinforcement learning policies, and reports better failure detection than random and genetic-algorithm search in most evaluated configurations across four benchmarks.</one_liner>
<parameter name="plain">Teams of software agents trained with reinforcement learning to work together can behave unsafely in ways their reward signal does not capture, and such failures are hard to explain. This paper proposes a way to pick which situations to test by flagging states where the agents' estimates of the expected payoff diverge beyond a set threshold, and skipping states where they agree. In experiments on four standard benchmark environments, this selection found failures better than random testing and a genetic-algorithm search in most of the configurations tested.</plain>
<parameter name="why>The approach offers a checkable signal, computed from a single state without running the system, that may point to miscoordination before it causes harm. Its relevance beyond the four benchmark environments is not established by the text, and it applies only to value-based methods.</why>
<parameter name="background">- Reinforcement learning: an agent learns by trial and error to maximize a reward.
- Multi-agent (cooperative) RL: several agents act at each time step toward a shared goal.
- Q-value: a learned estimate of the total future reward from taking an action in a given state.
- Q-value gap (as used here): the difference between agents' value estimates in a state, flagged when it exceeds a calibrated threshold.
- Test case selection: choosing which situations to run a system on, since testing everything is too costly.
- Baselines: random testing, and search-based testing using genetic algorithms (methods that evolve candidate test inputs).</background>
<parameter name="difficulty">research-level
- Matched keywords: reinforcement learning, Q-learning

<details><summary>Original abstract</summary>

Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the reward, and these behaviors are hard to explain. However, testing CMARL policies for safety has received less attention than the safety testing of single-agent RL policies. In this paper, we propose DisQ, a test case selection method that identifies failure-revealing states in value-based CMARL by exploiting a signal specific to trained Q-learning agents. The signal is the Q-value gap, an explainable metric that flags a state when the agents' estimates of the achievable return diverge by more than a calibrated threshold. DisQ selects such states for execution and skips those without a gap. Our experiments in four CMARL benchmark environments show that, in most of the evaluated configurations, DisQ improves failure detection over single-agent RL testing methods applied to CMARL, namely random testing and search-based testing with genetic algorithms. Our main contributions are the Q-value gap, an indicator of potential miscoordination computable from a single state without executing the system, and DisQ, a test case selection method that adapts existing single-agent testing methods to CMARL.

</details>

### [Decision Models Are General-Purpose Process Reward Models](https://arxiv.org/abs/2611.27068)
*Jiajun Fan, Qinglong Zheng, Ziwen Wang et al.* · `cs.AI` · arXiv:2611.27068v1 · relevance 0.20

- **In one sentence**: DM-PRM turns a general yes/no decision model into a zero-shot, step-level process reward model that is added to the advantage in policy-gradient RL for language agents on ALFWorld and WebShop.
- **In plain words**: Training AI agents to complete multi-step tasks usually gives a single score at the very end, so the agent cannot tell which individual actions helped. This paper proposes asking a general yes/no question model about each step, with no extra labels or training, and using those answers as per-step feedback. The authors report gains over the GRPO baseline on household and web-shopping tasks, and say the method reaches the highest success rate in their comparison.
- **Why it matters**: Step-level credit is a long-standing difficulty in training agents from outcome-only rewards, and the idea of getting it from a off-the-shelf model with no labels could lower the cost of training. The text reports results for one small model (Qwen2.5-1.5B) on two benchmarks, so how well it carries over to other models and tasks is not shown here.
- **Background needed**: - Reinforcement learning (RL): training by trial and error, guided by reward signals.
- Policy-gradient methods: RL algorithms that adjust an agent's action probabilities according to how good its actions turned out.
- Advantage: how much better an action was than average, used to decide how strongly to reinforce it.
- Process reward model (PRM): a scorer that rates intermediate steps, not just final results.
- GRPO, PPO, GiGPO, HGPO, GraphGPO: named RL training methods; PPO uses a learned critic (value estimator), the others are compared against it.
- ALFWorld and WebShop: simulated benchmarks for household tasks and online shopping by language agents.
- Zero-shot: used without task-specific training or labelled examples. · level: research-level
- Matched keywords: reinforcement learning, reward model

<details><summary>Original abstract</summary>

Reinforcement learning (RL) from verifiable outcomes gives a language agent one reward per episode: every step is credited alike, and nothing about the task is learned when all rollouts fail. The last mile, step-level credit, usually requires step labels, a learned critic, costly LLM judges or hand-written rules. We introduce DM-PRM, which turns a general-purpose decision model -- one answering yes/no questions with probabilities -- into a general-purpose process reward model (PRM), zero-shot: no step labels, no fine-tuning, no critic. DM-PRM asks one question per step and adds the standardised answers to the advantage. It plugs into any policy-gradient method; one model, with one question text per environment, serves household tasks, web shopping and multiple RL methods. With Qwen2.5-1.5B it lifts GRPO by over twenty points on ALFWorld and over ten on WebShop, overtakes GiGPO on ALFWorld and learns in far fewer iterations; it also improves GiGPO and GraphGPO on both benchmarks and reaches the highest success of our comparison, ahead of critic-based PPO and of state-of-the-art GiGPO, HGPO and GraphGPO. Its scores locate useful steps in failed rollouts, and trained agents drop idle actions and explore instead of circling. DM-PRM shows that step credit need not be learned: it can be asked for.

</details>

## AI safety and alignment

### [Preserving Pretrained CFG Structure in RL for Diffusion Models with Conditional Contrast Regularization](https://arxiv.org/abs/2611.27288)
*Yunfei Zheng, Xiaolong Wang, Dandan Zheng et al.* · `cs.LG` · arXiv:2611.27288v1 · relevance 0.29

- **In one sentence**: The paper proposes Conditional Contrast Regularization (CCR), which uses the frozen pretrained model's classifier-free guidance direction as a structural prior to keep diffusion-model generation quality from degrading during reward-driven reinforcement learning.
- **In plain words**: Image-generating AI models are often fine-tuned with reinforcement learning to score higher on a target reward, but this can make outputs worse overall in ways the reward does not measure. The authors treat this as a form of reward hacking and examine whether a known guidance technique, classifier-free guidance (CFG), carries structure that can keep quality intact during training. They report that a geometric analysis and a rotation test suggest the pretrained guidance direction holds quality-related information that reward-driven updates do not necessarily keep, and their regularization method, CCR, is reported to give a better balance of reward and quality.
- **Why it matters**: Reward-driven fine-tuning that quietly degrades overall quality is a practical concern for deployed generative models, and using the pretrained model's own guidance as a constraint is a fairly direct idea. The text reports experiments across several reward settings and backbones, but I have only the abstract-level description, so the size and reliability of the gains are not something I can judge.
- **Background needed**: - Diffusion models generate images by gradually removing noise from random input, guided by a text prompt.
- Reinforcement learning (RL) here means adjusting the model to maximize a score (a "reward") from some judge, such as a preference or aesthetic scorer.
- Reward hacking means optimizing the score in ways that do not reflect the goal, so the score rises while quality falls.
- Classifier-free guidance (CFG) is a standard inference trick that pushes outputs to follow the prompt more strongly by contrasting conditional and unconditional predictions.
- "Correction vector" and "projection" refer to treating the change each method applies as an arrow in a shared space and measuring how much one arrow points along another.
- A "frozen reference model" is a copy of the original model whose weights are not updated, used as a fixed baseline.
- Regularization means adding a penalty that discourages the trained model from drifting too far from a reference. · level: research-level
- Matched keywords: alignment, reward hacking

<details><summary>Original abstract</summary>

Reinforcement Learning (RL) has become an important component in the post-training of diffusion models. In practice, however, standard RL often improves the target reward without reliably preserving holistic generation quality, leading to unstable reward-quality trade-offs that we view as a form of reward hacking. Since Classifier-Free Guidance (CFG) is known to improve visual clarity, prompt alignment, and perceptual quality in generation, we investigate whether its underlying structure can serve as a useful prior during RL. We present a unified geometric view that interprets both CFG and RL as correction vectors in a common prediction space, and identify the projection of the RL-induced correction onto the pretrained CFG correction as a useful diagnostic of quality-related structural preservation. Geometric analysis and rotation intervention further show that the pretrained CFG direction carries information useful for generation quality that reward-driven RL updates do not necessarily preserve. Based on this insight, we propose Conditional Contrast Regularization (CCR), which uses the frozen reference model's conditional contrast as a local structural prior during RL. Experiments across multiple reward settings and backbones show that CCR more consistently preserves generation quality while maintaining competitive reward, yielding a better reward-quality trade-off than standard RL and generic regularization methods.

</details>

### [The Assistant Persona Differs Across Languages in Activation Space](https://arxiv.org/abs/2611.27504)
*Daniel Yoo, Naama Rozen, Evan Harris* · `cs.CL` · arXiv:2611.27504v1 · relevance 0.24

- **In one sentence**: The paper extracts an "assistant persona" direction in activation space for 31 languages in Qwen3-32B and finds these directions differ across languages, track language resource level, and affect how strongly persona-based jailbreaks can be amplified by steering.
- **In plain words**: Large language models are known to be less safe in languages with less training data. This paper looks inside the model to ask whether its internal "helpful assistant" trait is the same across languages, and finds it is not. The model's internal representation of that persona shifts noticeably depending on the language, and the shift tracks how much data exists for that language.
- **Why it matters**: It offers a possible internal explanation for the well-documented gap in safety between languages, and suggests multilingual alignment may need to target the assistant persona directly. The text reports these findings for one model only, so how far they generalize to other models is not shown.
- **Background needed**: - Activation space: the set of internal numerical signals a neural network produces while processing text; a "direction" is a pattern within it that corresponds to a trait or behavior.
- Persona direction: a direction extracted by comparing activations when the model acts as an assistant versus other roles, used to steer behavior.
- Cosine similarity: a measure from 0 to 1 of how closely two directions point the same way; here, 0.378 to 0.911 relative to the English direction.
- Steering: adding or subtracting a direction during generation to push the model's behavior in a chosen direction.
- Jailbreak: a prompt or technique that gets a model to ignore its safety rules.
- Resource level: how much text data exists for a language online, used to gauge how well models learn it. · level: research-level
- Matched keywords: alignment, jailbreak

<details><summary>Original abstract</summary>

Large language models behave differently across languages, and are noticeably less safe in lower-resource languages. This gap is well established behaviorally, but not mechanistically. Directions in activation space, including the assistant persona direction, are almost always extracted from English and assumed to generalize across languages. We extract the assistant persona direction in 31 languages in Qwen3-32B, and find that the resulting axes differ substantially: their cosine similarity to the English axis ranges from 0.378 to 0.911. Moreover, each language's assistant persona direction and its magnitude are correlated with the language's resource level. We also find that the model's default assistant state is farther from the helpful assistant pole in lower-resource languages. Finally, steering against a language's own axis amplifies persona-based jailbreak more than steering against the English axis. These results indicate that the model does not carry a single assistant representation across languages. More broadly, the assistant persona may need to be an explicit target of multilingual alignment.

</details>

## Interpretability

### [Parasite Features: Causal Abstraction Through Spurious Pathways](https://arxiv.org/abs/2611.26711)
*Denis Sutter, Qing Yao, Sasha Boguraev et al.* · `cs.LG` · arXiv:2611.26711v1 · relevance 0.29

- **In one sentence**: The paper argues that Causal Abstraction methods such as Distributed Alignment Search can be fooled by "parasite features," pairs of representation directions that jointly mimic a target algorithm without the model actually implementing that feature, and demonstrates this on syntactic agreement and two-digit addition.
- **In plain words**: Researchers study how to tell whether an AI model has learned a specific rule or concept inside its internal workings. They show that a common test can be passed by a misleading shortcut: two internal directions that together produce the right behavior while the model does not really use the concept. They report that this happens in two tasks, grammar agreement and adding two-digit numbers.
- **Why it matters**: The text suggests this matters for how interpretability claims are checked, since a passing equivalence test may not show the model implements the feature. It is a methodological caution rather than a finding about any specific model's capabilities, and the scope of its impact beyond these two tasks is not established in the text.
- **Background needed**: - Neural networks represent information as patterns of numbers (vectors) inside their layers; a "direction" is one such axis in that space.
- Mechanistic interpretability: reverse-engineering which internal parts of a model carry which computations.
- Causal Abstraction: a framework asking whether a network's internal behavior matches a simpler, human-readable algorithm when parts are swapped or intervened on.
- Distributed Alignment Search (DAS): a method that learns a linear map to find directions in a network that correspond to an algorithm's variables.
- Spurious feature: an apparent explanation that works for the test but does not reflect the true mechanism.
- Syntactic agreement: a grammar rule matching, e.g., a verb's form to its subject's number. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Causal Abstraction defines a notion of \emph{equivalence} between a neural network and an algorithm, thus serving as a powerful framework for mechanistic interpretability. In this paper, however, we show the existence of a class of \emph{spurious features} which straightforwardly pass such equivalence tests. Suppose there are two directions in a model's representation space where: (i) one discriminates the input based on some feature, and (ii) the other steers the model towards a certain output. Interpretability methods based on Causal Abstraction (e.g., Distributed Alignment Search) can \emph{spuriously} simulate these directions' combined behavior by leveraging pathways passing through them, giving the impression that the model implements this feature. In such cases, we say the method discovered a \defn{parasite feature}. Experimentally, we show that Distributed Alignment Search finds parasite features using linear alignment maps in two tasks: syntactic agreement and two-digit addition. Our paper highlights an important consideration for Causal Abstraction and contributes to the ongoing debate about best practices for mechanistic interpretability.

</details>

### [WaXup: Weight Averaging of Experts as Data Augmentation for Robust Introspection](https://arxiv.org/abs/2611.27353)
*Marc Bo\"elle, Lucas Dixon, Alexandre Ram\'e* · `cs.CL` · arXiv:2611.27353v1 · relevance 0.25

- **In one sentence**: WaXup augments the training data for trainable introspection (models trained to describe their own finetuned behaviors) by linearly interpolating weights of finetuned expert models, and evaluates on hidden-behavior, real-world NLP meta-dataset, and AuditBench benchmarks.
- **In plain words**: The paper looks at whether a language model can be trained to explain, in plain words, what it has learned during finetuning, rather than relying on hard-to-read internal analysis. The authors propose WaXup, which creates extra training examples by averaging the weights of several finetuned "expert" models, on the idea that such averages behave like blends of the originals. They report that this improves the accuracy of the generated descriptions and makes them hold up better under changes in the data.
- **Why it matters**: Reliable self-explanation would help people audit AI systems, including models trained to hide their behaviors, so the reliability question matters for AI safety. The text is a short abstract, so I cannot judge how large the gains are or how far they generalize beyond the three benchmarks named.
- **Background needed**: - Finetuning: further training a pretrained model on a narrow task or behavior, producing an "expert" model.
- Mechanistic interpretability: trying to understand a model by analyzing its internal parts directly; the paper says this struggles to scale to more capable models.
- Introspection (trainable): training a model to report in natural language what its finetuning taught it.
- Data augmentation: creating extra training examples from existing ones to improve robustness.
- Weight-space interpolation / linear mode connectivity: blending the numerical parameters of two models; the idea is that the blend behaves roughly like a mix of the two originals.
- MiXup: the data augmentation framework the paper builds on.
- AuditBench: a test suite of models trained to conceal their behaviors, used to check alignment audits. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

As the capabilities of large language models keep improving, traditional mechanistic interpretability methods struggle to keep pace. In contrast, trainable introspection methods emerge as a promising alternative; they repurpose the model itself as a self-diagnostic tool, trained to verbalize what it has learned during finetuning in natural language. While training on datasets of finetuned experts achieves encouraging results, it currently lacks robustness and generalization. Building on the data augmentation framework of MiXup, we introduce WaXup, a method that augments the introspection training set through linear interpolation in the weight space. This is motivated by the linear mode connectivity property: weight averaged experts interpolate the behaviors of the initial experts. We evaluate WaXup on three benchmarks: hidden-behavior models, a meta-dataset of real-world NLP tasks and AuditBench, a challenging alignment auditing suite of models adversarially trained to conceal their behaviors. WaXup improves the accuracy of generated descriptions as well as robustness to various distribution shifts. We hope to improve the reliability of trainable introspection methods towards better and safer models.

</details>

## AI for mathematics

### [Budget-Aware Predict-and-Verify Theorem Proving with Heterogeneous LLM Solvers](https://arxiv.org/abs/2611.26906)
*Wei Jiang, Ziran Liu, Wei Wang* · `cs.AI` · arXiv:2611.26906v1 · relevance 0.23

- **In one sentence**: BudgetPV is an agentic predict-and-verify system that uses a cross-solver predictor, trained with two different loss objectives for early and late stages, to allocate inference budget across unresolved Lean subgoals and heterogeneous LLM provers.
- **In plain words**: Automated theorem provers use language models to write formal proofs, and some models are more capable but also more expensive to run. This paper studies how to decide which model should attempt each smaller piece of a proof, and how much extra effort to give pieces that remain unsolved. The authors report that their method needs less model computation than spreading effort evenly to reach the same number of solved subgoals on four benchmarks.
- **Why it matters**: Compute cost is a practical limit on automated proving, so a way to route work between cheap and strong models could matter for scaling these systems. The text reports savings relative to uniform allocation only; it does not say how large the gains are in absolute terms or how the method compares with other routing approaches.
- **Background needed**: - Theorem proving: a proof is checked by a formal system (here Lean) so correctness is verified automatically.
- Subgoal: a smaller intermediate claim that must be proved on the way to the full theorem.
- LLM solver: a language model used to generate proof attempts; solvers differ in skill and cost per attempt.
- Predict-and-verify: predict which solver is likely to succeed, try it, then check the result with the formal checker and update.
- Cross-entropy: a standard training loss for classifiers; class weighting makes rare classes count more during training.
- Calibrated probabilities: predicted probabilities that match how often the outcome actually occurs.
- Benchmarks named: Lean Workbook, miniF2F, ProofNet, PutnamBench (collections of formal math problems). · level: research-level
- Matched keywords: Lean, theorem proving

<details><summary>Original abstract</summary>

Large language model (LLM) theorem solvers differ in both proving capability and inference cost. Applying an expensive solver to every subgoal wastes computation when cheaper models are sufficient, while always starting from the cheapest solver wastes attempts on subgoals that require stronger models. We present BudgetPV, an agentic budget-aware predict-and-verify system that allocates computation across unresolved subgoals and heterogeneous LLM solvers. BudgetPV uses a cross-solver predictor to guide solver selection for each subgoal and revises the allocation as verification feedback becomes available. The allocation problem changes as proving progresses. Early decisions mainly determine which solver should handle an untried subgoal, while later decisions determine which previously attempted subgoals should receive additional computation. We train the predictor with two objectives for these two stages. Class-weighted cross-entropy improves assignment to less frequent stronger solvers during the initial stage, while plain cross-entropy provides better calibrated probabilities for later allocation among previously attempted subgoals. We evaluate BudgetPV on Lean Workbook, miniF2F, ProofNet, and PutnamBench using three progressively expanded solver settings: a strong but expensive solver alone, adding a medium-cost solver with intermediate solving capability, and further adding a cheap solver with lower solving capability. BudgetPV requires less LLM generation computation than uniform allocation to solve the same number of subgoals across the evaluated settings. The experiments further show the computation savings obtained as medium- and lower-cost solvers are added.

</details>

### [Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning Using Executable Symbolic Representations](https://arxiv.org/abs/2611.27203)
*Yu-Bin Liu, Shi-Ju Ran* · `cs.LG` · arXiv:2611.27203v1 · relevance 0.15

- **In one sentence**: The paper introduces GSM-AB, a benchmark that separately varies operand digit length and operation count, and reports that executable symbolic representations (Lean, plus a Python program-of-thought control) flatten accuracy decline in LLM arithmetic compared with natural-language reasoning.
- **In plain words**: Large language models often score well on math tests, but that does not show whether they stay accurate when the problems get bigger or have more steps. The authors built a controlled test where they could make the numbers longer and the chains of calculations longer, and compared having the model write its reasoning as runnable code-like formal statements against ordinary written reasoning. They report that the formal and code approaches lose accuracy more slowly as problems grow.
- **Why it matters**: It matters for anyone relying on AI for calculation-heavy work, since it suggests how the form of reasoning affects reliability and not just model size. The text does not show how broadly the effect holds beyond the benchmark and models tested, so the scope should be treated as provisional.
- **Background needed**: - LLM: a large language model, an AI system trained on text that generates answers word by word.
- Natural-language reasoning: the model writes out its steps in ordinary English.
- Executable symbolic representation: the model writes its steps in a formal language that a computer can run or check, here Lean (a proof-checking language) and Python.
- Program-of-thought (PoT): the model writes a program to compute the answer instead of doing the arithmetic in its head.
- Operand digit length: how many digits the numbers have.
- Operation count: how many calculation steps a problem requires.
- Scaling: how performance changes as the problem gets harder or the model gets bigger. · level: intermediate
- Matched keywords: Lean

<details><summary>Original abstract</summary>

High accuracy on mathematical benchmarks does not establish whether reasoning remains reliable as problem complexity increases. We examine how executable symbolic representations change accuracy scaling in large language models compared with natural-language reasoning. To address this limitation, we introduce the GSM Arithmetic Benchmark (GSM-AB), a controlled benchmark that independently varies operand digit length and operation count to probe numerical scale and compositional complexity. We find that executable representations can improve accuracy and slow its decline as complexity increases. Lean reduces average sensitivity to operand digit length at every tested model size. By contrast, slower degradation with increasing operation count emerges at the larger model sizes. A Python program-of-thought (Python-PoT) control shows a similar operation-axis pattern, suggesting that this finding is not specific to Lean. These findings show that reasoning representation shapes arithmetic accuracy scaling and support executable symbolic representations for more reliable reasoning on complex arithmetic tasks.

</details>

## Robotics and embodied AI

### [Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter](https://arxiv.org/abs/2611.27845)
*Songyang Liu, Yu Hou, Yuqing Hu et al.* · `cs.RO` · arXiv:2611.27845v1 · relevance 0.20

- **In one sentence**: A runtime safety filter that screens each operator command sent to a teleoperated humanoid robot, using a camera-based scene model and a target-conditioned control barrier function quadratic program, to stop the robot's tool from touching a non-target electrical switch during switching tasks.
- **In plain words**: Electrical switching, the job of flipping switches in power facilities, can expose workers to danger, so the paper looks at having a humanoid robot do it while a person operates it remotely in virtual reality. The problem is that a slightly imprecise command could make the robot's tool touch a neighbouring switch that should not be moved. The authors add a software filter that checks each command against a model of the scene built from the robot's head camera, lets safe commands through unchanged, and adjusts unsafe ones to keep the tool clear of the wrong switch.
- **Why it matters**: Worth attention because it tackles a concrete safety gap in remote robotic work around hazardous equipment, and it reports both real-robot and simulation tests. The text reports only limited trials (ten real rounds at two positions and nine simulated runs), so its broader usefulness for other tasks or sites is not established here.
- **Background needed**: - Teleoperation: a person controls a robot remotely, here through virtual reality.
- Humanoid robot: a human-shaped robot; this study uses a Unitree G1.
- Safety filter: a layer that checks and minimally edits commands before they reach the robot.
- Control barrier function: a mathematical rule that keeps a system inside a designated safe region.
- Quadratic program: a standard optimisation method that finds the closest safe command to the one given.
- Scene model: a computer's estimate of where objects are, built here from camera images.
- Raw teleoperation: the baseline where commands are sent to the robot without any safety check. · level: research-level

<details><summary>Original abstract</summary>

Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch. This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of a humanoid robot. The filter integrates a scene model estimated from the robot head camera and a target-conditioned control barrier function quadratic program that keeps the tool away from the non-target switch while passing safe commands unchanged. In real-world experiments on a Unitree G1 humanoid robot, with six rounds at each of two standing positions, target operations succeed in all ten rounds with an unchanged target and no non-target actuation. A simulation study achieves 9/9 safe completions, compared with 5/9 for raw teleoperation, demonstrating the feasibility of the method for humanoid switching operations.

</details>

### [HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots](https://arxiv.org/abs/2611.27181)
*Jinlin Gan, Mingzhe Li, Junsheng Zhang et al.* · `cs.RO` · arXiv:2611.27181v1 · relevance 0.18

- **In one sentence**: The paper introduces Humanoids, a benchmark with synthetic and real-world data for estimating the 3D whole-body pose of humanoid robots from single camera images, and HumanoidPose, a framework for that task that uses robot articulation modeling and kinematic grounding.
- **In plain words**: Humanoid robots are becoming more common, and it is useful to know their full 3D body posture from an ordinary camera image. Existing tools were built mainly for human bodies or for fixed robot arms, so this paper builds a dedicated dataset and test set for humanoid robots and a method called HumanoidPose. The authors report strong results on their benchmarks and on a physical Roban humanoid, including transfer to real-world images without extra training.
- **Why it matters**: Knowing where a robot's body is from a camera alone could help with monitoring, motion analysis, and training robots from video. The text does not say how it compares with other methods beyond the authors' own reported results, and the dataset and code are promised but not yet released.
- **Background needed**: - Pose estimation: finding the positions of a body's joints in an image, then turning them into 3D.
- Monocular: using a single camera, with no depth sensor or multiple views.
- Kinematics: the geometry of how linked parts (arms, legs) move around joints.
- Human pose estimation (HPE) assumes a human skeleton; robot pose estimation (RPE) has mostly targeted fixed arms.
- Synthetic data: computer-generated training images with known ground-truth positions.
- Zero-shot transfer: working on new data types without retraining on them. · level: research-level

<details><summary>Original abstract</summary>

As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation (HPE), while not being fully addressed by either paradigm: RPE primarily focuses on non-humanoid robots, particularly fixed-base manipulators, whereas HPE is built upon human-specific skeletal topologies, body models, and motion priors. Despite recent progress in humanoid 2D keypoint detection and HPE adaptation, humanoid-native 3D pose recovery remains insufficiently studied, and a dedicated benchmark with suitable training data and evaluation protocols is still lacking. To address this gap, we introduce Humanoids, a benchmark for monocular 3D humanoid robot pose estimation, and propose HumanoidPose, a framework for this task. Humanoids provides synthetic 3D supervision across diverse humanoid embodiments, manually annotated real-world 2D data, and real-world RGB sequences paired with robot states for 3D evaluation on a physical Roban humanoid. HumanoidPose combines human-inspired visual perception with robot articulation modeling and explicit kinematic grounding. Experiments on Humanoids and the DHRP-H1 benchmark demonstrate strong performance in articulation recovery and 3D pose estimation, including zero-shot transfer to real-world 2D and 3D evaluation. Ablation studies further show the contribution of robot-native articulation modeling and explicit kinematic grounding. The dataset and code will be publicly released to support future research in the community.

</details>

## Security and cryptography

### [Post-Quantum Migration in Brownfield 5G Core Networks: Verified Hybrid Key Establishment, Performance, and Rollback](https://arxiv.org/abs/2611.27735)
*Shubham Verma* · `cs.CR` · arXiv:2611.27735v1 · relevance 0.11

- **In one sentence**: The paper evaluates a deployment-controlled way to add hybrid post-quantum/classical key establishment to an existing Open5GS 5G Core AMF-NRF service-based interface, using external mediating entities (BCEEs) without changing the network functions' source code, and reports latency costs and packet-verified rollback.
- **In plain words**: Phone networks use encryption to protect messages sent between their internal software components, and that encryption may eventually be broken by quantum computers. This paper looks at how to upgrade an already-running 5G core network to a newer encryption method that combines a classical and a quantum-resistant scheme, without rewriting the software that is already deployed. The authors tested this on one link in a lab version of the network and reported that the upgrade works, can be reversed, and adds a modest delay.
- **Why it matters**: Operators running older network equipment face a hard upgrade problem as post-quantum standards arrive, so a way to retrofit protection from outside the software may be useful to them. The results are limited to one interface in an open-source lab setup, so they indicate feasibility rather than real-world readiness.
- **Background needed**: - 5G Core: the software that runs the central part of a mobile network, split into network functions that talk over service-based interfaces (SBI).
- AMF and NRF: two such network functions; the paper measures traffic between them.
- Open5GS: an open-source implementation of the 5G Core used for testing.
- TLS: the standard protocol that encrypts traffic between two programs; its key establishment is the handshake that sets up shared secret keys.
- Post-quantum cryptography (PQC): encryption designed to resist attacks from future quantum computers.
- Hybrid key establishment: combining a classical key exchange (X25519) with a post-quantum one (ML-KEM 768) so security holds if either is unbroken.
- Brownfield: an existing, already-deployed system that must be changed incrementally.
- Rollback: reverting to the previous configuration if the change causes problems.
- Median and confidence interval: a typical value and a range of plausible values for the true effect; the paper's ~3.4 ms latency increase has a wide interval of about 1.2 to 7.9 ms. · level: research-level

<details><summary>Original abstract</summary>

Migrating brownfield 5G Core networks to post-quantum cryptography (PQC) is difficult because deployed network functions, base images, and TLS libraries evolve under different upgrade constraints. This paper evaluates a deployment-controlled migration strategy that enables hybrid post-quantum/traditional key establishment through externally deployed Boundary Cryptographic Execution Entities (BCEEs), without modifying participating network function source code. The approach is evaluated using the Open5GS AMF-NRF Service-Based Interface as a representative 5G Core scenario. Classical and hybrid configurations are compared under an unchanged mediation topology. Packet-level analysis confirms successful negotiation of X25519MLKEM768, and functional validation demonstrates that representative SBI procedures remain operational through the mediated path. In 120 NF-registration transactions, the median AMF-facing registration latency increased from 22.968 ms under the classical state to 26.351 ms under the hybrid state, reflecting a 3.383 ms (14.73 percent) increase, with a whole-block 95 percent confidence interval of [1.193, 7.872] ms. At the mediated TLS boundary, the hybrid configuration shows a 4.599 ms higher median segment-local TLS-establishment time than the classical configuration. These two reported differences reflect system-level runtime effects and do not isolate key-encapsulation cost. Packet evidence verifies rollback from hybrid-mediated operation to classical mediated operation and, separately, restoration of the native direct path. NF-facing compatibility legs remained plaintext and outside the hybrid post-quantum scope. The results demonstrate a packet-verifiable and manually reversible brownfield mechanism for introducing hybrid post-quantum key establishment on a controlled 5G SBI segment.

</details>

### [Enhancing Metaverse Security using Explainable AI-based Intrusion Detection Framework](https://arxiv.org/abs/2611.27199)
*Esha Kuppanda, Shalaka Mahadik, Pranav M. Pawar et al.* · `cs.CR` · arXiv:2611.27199v1 · relevance 0.08

- **In one sentence**: The paper compares machine learning models for detecting intrusions in Internet of Things-based metaverse networks, uses explainable AI (SHAP and LIME) to identify the most useful features, and reports accuracy results on three benchmark security datasets (ToN-IoT, CIC-IoT-2023, BoT-IoT).
- **In plain words**: Connected devices that make up parts of virtual "metaverse" environments can be broken into by attackers, which threatens privacy and trust. This paper tests several machine learning models that flag suspicious network traffic, and uses tools that explain which data signals drove each decision. The authors report high detection accuracy on three public test datasets, with XGBoost performing best on two of them and Random Forest and Extra Trees on the third.
- **Why it matters**: Security for connected virtual environments is a growing concern as more sectors such as healthcare and education adopt them. The explanation side matters because a detector that gives reasons for its alerts is easier for operators to check, though the text does not show how well these explanations hold up in real deployments.
- **Background needed**: - Intrusion detection system (IDS): software that watches network traffic and flags suspected attacks.
- Metaverse of Things (MoT): virtual environments linked to physical Internet of Things devices such as sensors and cameras.
- Machine learning (ML): methods that learn patterns from example data rather than following hand-written rules.
- Explainable AI (XAI): techniques that show which inputs influenced a model's output.
- SHAP and LIME: two common XAI methods that score how much each feature contributed to a prediction.
- Accuracy: the share of traffic records labelled correctly; high accuracy on a benchmark does not by itself guarantee performance on live networks.
- Benchmark datasets: shared collections of recorded network traffic used to compare methods. · level: intermediate

<details><summary>Original abstract</summary>

The MoT virtual environment, called the Metaverse of Things (MoT), combines machine learning (ML) and Internet of Things (IoT) to offer significant business opportunities in various sectors such as entertainment, healthcare, and education. In addition to its benefits, the MoT poses risks to privacy and security through unauthorized access, which threatens trustworthiness. While traditional intrusion detection systems (IDS) exist to handle this challenge, they struggle with high-dimensional data and poor interpretability. To address this challenge, the research conducted a thorough analysis of different ML models and proposed the optimal model to secure the MoT environment. The research employed explainable artificial intelligence (XAI) to identify the most effective features that contributed to optimal model selection. The research presented an optimal framework combining ML and XAI to safeguard MoT networks from the most recent cyberthreats. The research used three advanced benchmark security datasets: ToN-IoT, CIC-IoT-2023, and BoT-IoT, to examine the XAI-based intrusion detection framework. The XAI-based intrusion detection framework achieved 99.83% accuracy on ToN-IoT and 96.45% on CIC-IoT-2023 using the XGBoost model. On the BoT-IoT dataset, the Random Forest (RF) and Extra Trees (ET) classifiers reached 99.99% accuracy. The Shapley Additive Explanations (SHAP) and Local Interpretable Model-Agnostic Explanations (LIME) techniques used for XAI further enhanced feature relevance and user confidence in the optimal model.

</details>

## Algorithms and complexity

### [No Polynomial-Time Algorithm For Tarski Fixed Points Unless Cryptographic Assumptions Fail](https://arxiv.org/abs/2611.27977)
*Eleni Batziou, John Fearnley, Alexandros Hollender et al.* · `cs.CC` · arXiv:2611.27977v1 · relevance 0.24

- **In one sentence**: The paper gives a subexponential-time reduction from UEOPL to Tarski fixed-point finding, yielding conditional quasi-polynomial time lower bounds that match known query lower bounds.
- **In plain words**: The paper studies how hard it is to find a "Tarski fixed point," a point where a monotone (order-preserving) map sends a set of options back to itself. The authors show that a known hard search problem, UEOPL, can be translated into this one with only modest overhead. Because of that link, if certain cryptographic assumptions hold, no algorithm can solve Tarski fixed-point finding in polynomial time, and the strongest versions rule out anything faster than quasi-polynomial time.
- **Why it matters**: It settles, conditionally, how fast the problem can be solved, and the running-time bounds agree with earlier lower bounds that counted queries rather than total steps. The result depends on cryptographic assumptions and the text does not say how far these bounds extend to other settings.
- **Background needed**: - Fixed point: an input that a function maps to itself.
- Tarski fixed point: a fixed point of a monotone map on a lattice (an ordered set where every pair has a meet and join), which always exists by Tarski's theorem but may be hard to find.
- Polynomial vs. quasi-polynomial vs. subexponential time: growth rates of running time in the input size; polynomial is considered efficient, and exponential is very slow.
- Reduction: a method of translating one problem into another so that solving the second solves the first, used here to transfer hardness.
- UEOPL: a search problem on a graph of paths with a unique end, known to be hard under cryptographic assumptions.
- Query complexity: counting how many times an algorithm must query the input, as opposed to total computation time.
- Conditional lower bound: a hardness result that holds only if a stated assumption (here, cryptographic) is true. · level: research-level

<details><summary>Original abstract</summary>

We study the time complexity of finding a Tarski fixed point. We provide a subexponential-time reduction from the Unique End of Potential Line (UEOPL) problem to the problem of finding a Tarski fixed point. Using a range of known cryptographic lower bounds for UEOPL, our reduction implies a range of conditional lower bounds on the running time of any algorithm that finds a Tarski fixed point. The strongest of these give quasi-polynomial-time lower bounds for the problem. We also obtain a similar quasi-polynomial-time lower bound for Tarski based instead on a weak exponential-time type hypothesis for UEOPL. These running time lower bounds match the recently discovered quasi-polynomial query lower bounds for the problem.

</details>

### [Compiling Existential-Positive Queries to Bounded-Variable Fragments](https://arxiv.org/abs/2611.26869)
*Christoph Berkholz, Hubie Chen* · `cs.LO` · arXiv:2611.26869v1 · relevance 0.16

- **In one sentence**: The paper studies how much formula size grows when an existential-positive first-order query is rewritten to use fewer variables within the bounded-variable fragment of positive first-order logic, giving polynomial and exponential bounds and an unconditional exponential lower bound proved via circuit complexity.
- **In plain words**: Database queries and logic formulas can often be rewritten to use fewer named variables, which makes them faster to evaluate. This paper examines the cost of that rewriting: the shorter-variable version may be much longer. The authors show the length increase is always at most exponential, can be only polynomial in some cases, and in other cases must be exponential, with a proof that does not rely on unproven assumptions.
- **Why it matters**: It clarifies a real trade-off between variable count and formula size that matters for query preprocessing. The link to circuit complexity is the part the authors flag as potentially of future interest; the text does not say how far that connection will extend.
- **Background needed**: - First-order logic: formulas built from variables, predicates (relations), quantifiers ("for all" and "there exists") and connectives.
- Existential-positive fragment: formulas using only "there exists", "and", "or" and no negation or "for all".
- Bounded-variable fragment: formulas restricted to a fixed number k of variables, which can be evaluated in polynomial time.
- Formula size: the length of a formula; blow-up means how much longer the rewritten version gets.
- Exponential vs. polynomial growth: exponential growth is far faster than polynomial growth as inputs get larger.
- Unconditional lower bound: a proof that a size increase is necessary, without relying on unproven complexity conjectures.
- Circuit complexity: the study of the minimum size of Boolean circuits needed to compute functions. · level: research-level

<details><summary>Original abstract</summary>

A crucial property of bounded-variable fragments of first-order logic is that they can be evaluated in polynomial time. It is therefore a useful preprocessing step to rewrite, if possible, a first-order query to a logically equivalent one with a minimum number of variables. However, it may occur that reducing the number of variables causes an increase in formula size. We investigate this trade-off for the existential-positive fragment of first-order queries, where variable minimisation is decidable in general. In particular, we study the blow-up in the formula size when compiling existential-positive queries to the bounded variable fragment of positive first-order logic. While the increase of the formula size is always at most exponential, we identify situations (based on the signature and the number of variables) where only a polynomial blow-up is needed. In all other cases, we show that an exponential lower bound on the formula size of the compiled formula that matches the general upper bound. This exponential lower bound is unconditional, and is the first unconditional lower bound for formula size with respect to the studied compilation; it is proved via establishing a novel interface with circuit complexity which may be of future interest.

</details>

## Programming languages and formal methods

### [Perceived Differences in Activity and Experience Between Developing Software With and Without AI](https://arxiv.org/abs/2611.27947)
*Rubash Mali, Juho Leinonen, John Edwards* · `cs.SE` · arXiv:2611.27947v1 · relevance 0.20

- **In one sentence**: A study of how software engineers perceive their activities and experience differ when developing with generative AI tools versus traditionally, with effects amplified by years of prior programming experience.
- **In plain words**: This paper asks how programmers feel their work has changed now that they use AI tools to write code, and whether that change depends on how long they have been programming. Based on engineers' reports, they talk less with peers about technical problems, search documentation less, use a debugger less, and switch tasks more. They also report less deep focus and less sense of control over their code and design, while core coding tasks like writing, refactoring and fixing code changed little.
- **Why it matters**: Software is a large field of employment, so changes in how the work feels and what skills it demands matter for hiring, training and career choices. The paper also suggests that engineers who began programming before generative AI may be affected more, which bears on how newcomers should be trained; the text does not show how well these perceptions match measured outcomes.
- **Background needed**: - Generative AI: software that produces text or code in response to prompts, such as coding assistants.
- Survey-style study: the findings rest on what engineers report they experienced, not on direct measurement of their work.
- "Decomposition": breaking a large problem into smaller parts.
- "Task switching": moving back and forth between different activities or problems.
- "Experience gradient": the pattern where the effect grows with years of prior programming experience.
- Debugger: a tool that steps through code to find errors.
- Refactoring: rewriting existing code to improve its structure without changing what it does. · level: intermediate

<details><summary>Original abstract</summary>

The fundamental changes in software engineering driven by generative AI will have profound effects not only on the number of available software engineering jobs but also on what software engineering itself looks like. As the career evolves, questions arise about what the skillset and interests of the next generation of software engineers will be and whether long-time engineers will continue to be attracted to the career. In this paper, we contribute to answering these questions by studying how software development with AI tools is perceived to differ from traditional development and how the differences are modulated by years of programming experience. We find that, in terms of programming activities, engineers report less talking with peers about technical problems, less decomposition, less searching of documentation, and less using a debugger, while they report more task switching. We also find experiential differences, including less deep focus and less sense of control over code and design. We call these the different craft results, in contrast to core code-production activities such as writing, refactoring, and fixing code, which show only small mean differences. We also find that these differences are amplified by years of programming experience (an experience gradient), with software engineers who started programming before the age of generative AI perceiving greater changes in both activity and developer experience. We discuss our findings and their implications on training of the next generation of engineers and on engineers who may have difficulty transitioning to the AI-infused world of software engineering.

</details>

### [Compositional Temporal Specifications for Interaction Trees](https://arxiv.org/abs/2611.27553)
*Linyu Yang, Jianwei Yin, Mingshuai Chen* · `cs.PL` · arXiv:2611.27553v1 · relevance 0.07

- **In one sentence**: The paper introduces iBuchi, a shallowly embedded temporal specification language over Choice Trees for reasoning about the ordering of observable interactions in Interaction Trees, with trace- and tree-level satisfaction relations, compositional proof principles, and an integration into the Dijkstra Monads Forever framework, all mechanized in Rocq.
- **In plain words**: Programs that talk to their surroundings, such as reading input or writing output, are judged not only by their final answer but also by the order in which those interactions happen over time. This paper gives a way to write precise rules about that order and to check programs against them, in a form that can be combined piece by piece. The authors built the framework in the Rocq proof assistant, a tool for machine-checked proofs, and report several non-trivial examples that show it can express such rules and be used modularly.
- **Why it matters**: Verifying that software behaves correctly over time, not just at its end, matters for systems that interact with users, networks or hardware. The work connects a temporal-logic style of specification with an existing framework for verifying effectful programs, so its value depends on how well it scales to real code, which the text does not fully show.
- **Background needed**: - Effectful program: a program that does things outside pure computation, such as input, output or communication.
- Interaction Trees: a data structure that represents such a program as a tree of possible interactions with its environment, possibly unending.
- Temporal specification: a rule about the order of events over time, such as "a request is eventually answered".
- Linear Temporal Logic (LTL): a standard notation for writing such ordering rules.
- Hoare-style specification: a rule saying that if a condition holds before a program runs, another holds after.
- Proof assistant (Rocq, formerly Coq): software that checks mathematical and program proofs mechanically. · level: research-level

<details><summary>Original abstract</summary>

The correctness of modern effectful programs depends not only on their final results but also on the temporal evolution of observable interactions with their environments. Interaction Trees (ITrees) provide a reusable denotational semantics for such programs by representing effectful computations as potentially infinite trees of observable interactions. However, reusable temporal reasoning over ITrees remains largely unexplored. This paper presents a compositional temporal specification framework for ITrees. We introduce iBuchi, a shallowly embedded temporal specification language based on Choice Trees, which represents finite and infinite interaction traces and supports expressive temporal operators, including sequencing, branching, conjunction, repetition, and Linear Temporal Logic modalities. We define trace- and tree-level satisfaction relations between iBuchi specifications and ITrees, together with compositional reasoning principles for modular verification of effectful programs. We integrate iBuchi into the Dijkstra Monads Forever framework, thereby enabling temporal specifications to compose with conventional Hoare-style specifications and supporting a generator-based encoding of future conditions. We have formally developed and verified our framework in Rocq and demonstrated its expressiveness and compositionality through several non-trivial case studies.

</details>

## Systems and networking

### [Bring Cloud-Native Networking to FreeBSD Jails: Porting Calico from Linux](https://arxiv.org/abs/2611.27320)
*Soma Sakaguchi, Shintaro Suzuki, Yuki Nakata et al.* · `cs.OS` · arXiv:2611.27320v1 · relevance 0.13

- **In one sentence**: The paper describes porting Calico, a popular Kubernetes-style container networking plugin, to FreeBSD Jails by swapping Linux networking components (iptables, netlink, network namespaces) for FreeBSD equivalents (ipfw, routing sockets, vnet).
- **In plain words**: Software "containers" let many isolated programs share one computer, and each needs its own network connection and rules about who can talk to whom. On Linux, a well-established add-on called Calico handles this automatically, but FreeBSD's version of containers, called Jails, had no comparable standard tool, so administrators often set things up by hand. This paper describes adapting Calico to run on FreeBSD by replacing the Linux pieces it depends on with FreeBSD's own built-in tools.
- **Why it matters**: It matters for anyone running FreeBSD servers who wants to use the same orchestration tools as Linux shops, and it could widen FreeBSD's role in cloud container setups. The text is a short abstract and does not report measured results, performance figures, or how complete the port is, so its practical impact is unclear from this text alone.
- **Background needed**: - Containers: lightweight isolated environments that share one operating system kernel.
- FreeBSD Jails: FreeBSD's built-in form of container isolation.
- CNI plugin: a standard add-on that tells a container platform how to connect containers to a network.
- Calico: a widely used CNI plugin that also enforces network access rules between containers.
- iptables / ipfw: packet-filtering tools on Linux and FreeBSD that decide which network traffic is allowed.
- Netlink sockets / routing sockets: the interfaces programs use to read and change network settings in the kernel (Linux and FreeBSD versions respectively).
- Network namespaces (Linux) / vnet (FreeBSD): ways to give each container its own separate network stack. · level: intermediate

<details><summary>Original abstract</summary>

While Linux containers benefit from a rich ecosystem of Container Network Interface (CNI) plugins such as Calico and Cilium, FreeBSD Jails lacked native, standardized solutions for advanced networking. As a result, users have relied on manual, error-prone configurations, limiting scalability and integration with modern orchestration platforms. This paper introduces porting Calico, a widely adopted CNI plugin, to the FreeBSD operating system. Our approach replaced Linux-specific components with FreeBSD-native equivalents: iptables with ipfw, netlink sockets with routing sockets, and Linux network namespaces with FreeBSD's vnet. This work aims to bridge the gap between Linux and BSD container networking. By providing scalable, policy-driven capabilities that are compatible with existing Linux-centric infrastructure, FreeBSD can participate more fully in the broader container networking ecosystem.

</details>

### [Contention-Aware Flexible Execution for Machine Learning Workloads](https://arxiv.org/abs/2611.26840)
*Marco Kurzynski, Shaizeen Aga, Di Wu* · `cs.DC` · arXiv:2611.26840v1 · relevance 0.12

- **In one sentence**: A characterization of how concurrently running GPU kernels slow each other down on AMD MI300X hardware, followed by CAFEML, a contention-aware scheduler that tunes operator overlap and resource allocation for ML workloads and reports up to 13% end-to-end speedup without kernel rewrites.
- **In plain words**: Modern AI software often runs several GPU computations at the same time so the chip stays busy, but these computations compete for shared parts of the chip such as memory and caches, so each one can slow down. The paper first measures how much this slowdown happens on a current AI-focused AMD GPU, then uses those findings to change when and how parts of an AI workload are overlapped. Its reported result is a speedup of up to 13% across inference and training scenarios, achieved by changing scheduling rather than rewriting the computation itself.
- **Why it matters**: Efficiency of the expensive GPUs used for AI training and serving directly affects cost and speed, so a scheduling-only gain of up to 13% is worth noting. The text does not show how the gain compares with other scheduling approaches or how broadly it holds across hardware beyond the MI300X.
- **Background needed**: - A GPU "kernel" is a single computation job sent to the graphics processor; ML frameworks run many of them.
- "Concurrent" execution means several kernels share the GPU at once, competing for cores, caches and memory bandwidth.
- "Overlap" means scheduling two operations to run at the same time.
- "End-to-end" speedup means the improvement over a whole task, not just one piece.
- Inference "prefill" and "decode" are the two phases of generating text with a language model.
- The "early-first" policy launches whichever kernel is ready first, which the authors call suboptimal. · level: research-level

<details><summary>Original abstract</summary>

Concurrent kernel execution is a ubiquitous paradigm in artificial intelligence (AI) and machine learning (ML) across both training and inference. That said, concurrency causes potential slowdown as concurrent kernels contend for limited GPU resources (cores, caches, memory bandwidth), which are shared between these kernels rather than exclusively available to one, as in isolated execution. This raises an important research question: to what extent does concurrency slow down kernel execution and how can it be mitigated. To answer this question, our work presents two studies. First, we characterize concurrent kernel execution extensively for the first time, to our knowledge. We conduct not just performance analysis of concurrent kernels but also memory behavior under concurrency on state-of-the-art AMD Instinct MI300X GPUs designed for datacenter AI, using the AMD-internal millisecond sampler. Based on the observations, we share insights on the slowdown along two dimensions (memory vs. compute bound, large vs. small kernels) to inform future optimizations. Second, we put the derived insights to use, aiming to deliver higher performance via targeted, flexible overlap of ML operators. Frameworks today make the simple decision of early-first for concurrent kernels, which is suboptimal. Noticing the opportunity that ML dataflow has inherent flexibility in which operators can be overlapped and how hardware resources can be allocated, we deduce simple heuristics to tune both overlap anchors and resource allocation for concurrent kernels to improve performance. We evaluate our proposed contention-aware flexible execution (termed CAFEML) across a variety of ML scenarios (inference decode, inference prefill, training) and demonstrate a speedup of up to 13% end-to-end with simple scheduling changes and no kernel rewrites.

</details>

## Human-computer interaction

### [AROMA: Understanding AI Support For Mental Well-being through Role Theory](https://arxiv.org/abs/2611.26843)
*Issac Ting, Ethan Pan, Koustuv Saha et al.* · `cs.HC` · arXiv:2611.26843v1 · relevance 0.05

- **In one sentence**: The paper proposes AROMA, a role-based framework that annotates over 7,515 conversations from 13 datasets to derive eight observed "Role States" for AI mental well-being supporters, and uses them to analyze context, structure, timing, and prompting for better role alignment.
- **In plain words**: AI chatbots that offer emotional support sometimes act outside the role they were meant to play, which can harm the relationship with the user. Standard tests only check how well these tools do narrow tasks, and they do not explain why behavior drifts from what was expected. The authors built a framework, called AROMA, by labeling thousands of real support conversations to describe the roles the AI actually takes on.
- **Why it matters**: The work offers a different way to understand failures of AI support, focusing on the roles an AI plays rather than only on task accuracy. Its practical reach is still uncertain from the summary alone, since the abstract does not report how the prompting strategy performed.
- **Background needed**: - Role theory: the idea from sociology that people (and now AI) are expected to behave according to a social role, and mismatches cause friction.
- Annotation: human labelers tag conversation text with categories; the paper annotates conversations using a theory-informed scheme.
- "Role States": categories describing behavior as observed in the data, not as the designers prescribed it.
- Prompting: instructions written to steer a language model's behavior; here, used to try to keep the AI in its intended role.
- Relational harm: damage to the trust or relationship between a user and a system. · level: intermediate

<details><summary>Original abstract</summary>

AI supporters for mental well-being are becoming more prevalent. When these AI supporters start acting in ways beyond their expected function it leads to relational harm. Standard approaches to evaluating such AI supporters are limited to inspecting their efficacy in narrow task-specific settings, which do not explain these discrepancies in expected and actual behavior. To address this gap, we propose the AROMA (A Role-Oriented Model of Analysis) framework to provide a common role taxonomy for different support contexts. We developed AROMA using a theory-informed annotation of over 7,515 conversations from 13 datasets and propose eight "Role States" based on observed-not prescribed-behavior. We show these Role States vary according to the context of support; depict unique structural and temporal characteristics of AI supporters vis-a-vis Humans; and inform novel AI support prompting strategy for better role alignment. This framework provides a new lens to understand AI support failures.

</details>

### [A Frugal AI Framework for India: Responsible and Right-sized AI](https://arxiv.org/abs/2611.27189)
*Balaraman Ravindran, K. S. Venkataraghavan, Gokul S Krishnan et al.* · `cs.CY` · arXiv:2611.27189v1 · relevance 0.04

- **In one sentence**: A CeRAI (IIT Madras) white paper proposing "Responsible Frugal AI," a policy and engineering framework for India that right-sizes AI systems across data, compute, model and operations through seven levers, a seven-point checklist and eleven policy statements.
- **In plain words**: This white paper argues that India should not try to copy the huge, expensive AI models built in the US or China, nor simply use foreign AI with local tweaks. Instead it proposes building the smallest AI system that reliably does the job, with careful safeguards and human oversight for high-stakes decisions. The authors describe a framework with seven practical levers, a checklist for adopting it, and eleven policy statements, but the text itself gives no test results or measured outcomes.
- **Why it matters**: It is a policy position about how a very large, resource-constrained country might deploy AI at population scale, tying into India's digital public infrastructure and ideas of technological sovereignty. Its practical impact is unclear from the text alone, since it is a framework proposal rather than an evaluated study.
- **Background needed**: - "Foundation model": a very large general-purpose AI model trained on huge datasets using lots of computing power.
- "Frugal engineering": designing products to meet the need with minimal cost and resources.
- "Responsible AI": practices aimed at making AI fair, safe, transparent and accountable.
- "Digital public infrastructure": shared government-backed digital systems (such as identity or payment platforms) that private services can build on.
- "Sovereignty" here means a country keeping the ability to understand, control and adapt its own AI systems.
- "Vernacular-first": designing for local languages before English.
- "Human oversight": a person reviewing or approving automated decisions in high-stakes cases. · level: introductory

<details><summary>Original abstract</summary>

India's AI debate often swings between two insufficient options: replicating the compute-intensive, capital-heavy foundation-model programmes of the United States or China, or remaining a downstream adopter of foreign AI with localised interfaces and safeguards. Neither serves a country that must deliver AI to a very large, diverse population across uneven infrastructure and within constrained budgets. This white paper from the Centre for Responsible AI (CeRAI), IIT Madras, proposes a third path: Responsible Frugal AI, which applies principle-based frugal engineering alongside Responsible AI. Responsible Frugal AI is right-sized AI: it fixes the functional requirement first, asks whether AI is needed at all, and then chooses the smallest sufficient model, meeting the requirement with minimal resources while keeping a verified margin, robustness and responsible governance. The framework applies frugality across four dimensions (data, compute, model and operations) through seven levers spanning the AI lifecycle, each with practices and measures. It calls for public AI rails, vernacular-first design, measured resource use, human oversight for high-stakes decisions, and a cap on total resource consumption so that efficiency gains are not cancelled out by rising usage. We argue that India is resource-imbalanced rather than resource-poor, and that frugal principles offer the most viable route to population-scale deployment, fit naturally with India's digital public infrastructure, and make sovereignty operational by preserving India's capacity to specify, deploy, govern, inspect and adapt its AI systems. A seven-point adoption checklist and eleven policy statements translate the framework into practice, positioning AI in India as a responsible, frugal public-value system that maximises social value per rupee and per joule.

</details>

## Information theory

### [Coding Length and Optimal Power Allocation in Correlated Block Fading](https://arxiv.org/abs/2611.27694)
*Haoran Xu, Huazhong Zhao* · `cs.IT` · arXiv:2611.27694v1 · relevance 0.06

- **In one sentence**: For a Gaussian block-fading channel with correlated fading across blocks and many receive antennas, the paper studies when outage probability predicts the achievable rate under an error-exponent requirement, and characterizes the optimal rate and power allocation across blocks.
- **In plain words**: The paper looks at how to send a message over a wireless link where the signal strength fluctuates in blocks that are correlated over time, and the receiver has many antennas. The sender knows only the statistics of these fluctuations, not the actual values, and the question is how fast information can be sent while keeping the chance of a decoding error shrinking exponentially. The authors find that a simple "outage" measure predicts the achievable rate only in some regimes, and they give an exact limiting rate for large enough block-length-to-antenna ratios along with how power should be spread across blocks.
- **Why it matters**: It clarifies when a common engineering shortcut (outage capacity) is accurate and when it overestimates what is achievable, which matters for designing reliable low-latency wireless links. The text does not say how it connects to specific deployed systems, so its practical reach is not established here.
- **Background needed**: - Block fading: the channel strength stays roughly constant within a block of symbols and changes between blocks.
- Outage: the event that the channel is too weak to support a target rate; outage probability is the chance of this.
- Error exponent: how fast the probability of decoding error falls as the code gets longer or the receiver gains more antennas.
- Receive antennas: multiple receiving elements whose signals are combined; the paper uses their number as the growing parameter.
- Dispersion: a measure of how much random variation in the channel affects the finite-length achievable rate, in the Gaussian case.
- Autoregressive (AR(1)) fading: a model where each block's fade is a damped copy of the previous one plus fresh randomness; "lag-one correlation" is how similar neighboring blocks are.
- Water-filling-style power allocation: deciding how much transmit energy to put into each block, subject to a total energy budget. · level: research-level

<details><summary>Original abstract</summary>

A codeword spans a fixed number of correlated Gaussian fading blocks. The receiver knows the gains and the transmitter knows only their law. At fixed average signal-to-noise ratio, we require the decoding error probability to decay exponentially with the number of receive antennas. When does outage predict the achievable rate? If block length grows faster than the number of antennas, outage gives the limiting optimal rate. If both grow to infinity at a fixed positive ratio of block length to array size, outage strictly overestimates the limiting rate. We determine the critical ratio above which positive rates are possible. For sufficiently large finite ratios, we find the exact limiting rate over all codes satisfying a total energy constraint on each codeword. The leading rate loss is inversely proportional to the ratio. Its coefficient depends on Gaussian channel dispersion at the most likely fade causing outage and on how quickly the outage rate decreases as the required error exponent increases. In the long-block limit, equal power loses rate on every window of three or more blocks under stationary first-order autoregressive fading with positive lag-one correlation. In a different three-block channel with identical marginal gains, tightening the reliability requirement first makes it optimal to leave the middle block unused and later to use it again.

</details>

### [$L^1$ stability of the entropy power inequality in $\mathbb{R}^d$ without moment assumptions](https://arxiv.org/abs/2611.27790)
*Norman El Fartass, Lampros Gavalakis, Ioannis Kontoyiannis* · `cs.IT` · arXiv:2611.27790v1 · relevance 0.04

- **In one sentence**: The paper proves qualitative stability of Shannon's entropy power inequality in R^d in L^1 and Ruzsa distance without any moment assumptions, using an optimal transport argument, majorization of density rearrangements, and Christ's stability result for sharp Young's inequality.
- **In plain words**: The paper studies a basic inequality about how the randomness (entropy) of adding two independent random quantities behaves, in any number of dimensions. It asks what happens when the inequality is nearly tight, and it shows that this near-equality is stable in a precise sense, without requiring the random quantities to have bounded size or finite moments. The authors also extend several earlier one-dimensional results on related facts about entropy to vectors of any dimension.
- **Why it matters**: Stability results say that if an inequality is almost an equality, the underlying distributions must be close to the extremal (Gaussian) case, which matters for theory of information and probability. The text does not indicate applications beyond this theoretical setting, so its wider significance is uncertain.
- **Background needed**: - Differential entropy: a measure of spread or uncertainty for a continuous random vector with a probability density.
- Entropy power inequality: a bound saying the entropy power of a sum of independent random vectors is at least the sum of their entropy powers; equality holds for Gaussians.
- Stability: if the inequality is nearly tight, the distributions are close to the extremal case.
- L^1 distance: the total absolute difference between two probability densities.
- Ruzsa distance: a measure of how far apart two random vectors are, in a sense relevant to sums of random variables.
- Moment assumptions: conditions that tails of a distribution are not too heavy (finite averages of powers of size); the paper drops these.
- Optimal transport: a method of moving one probability distribution into another at minimal cost, used here as a proof tool.
- Young's inequality: a classical bound on convolutions of functions; its sharp form has known extremal functions. · level: research-level

<details><summary>Original abstract</summary>

We establish qualitative stability in $L^1$ and Ruzsa distance for Shannon's entropy power inequality in $\mathbb{R}^d$, without any moment assumptions. The proof uses the optimal transport argument by Rioul (2017), majorization bounds of density rearrangements, and the stability of the sharp form of Young's inequality due to Christ (2019). Along the way we also extend recent one-dimensional results on de Bruijn's identity, the continuity of differential entropy, and the equality case of the entropy power inequality to random vectors of any dimension.

</details>

## High-energy theory and gravity

### [Type-II quasinormal modes of dilaton--Euler--Heisenberg AdS black holes](https://arxiv.org/abs/2611.27195)
*Chao-Ming Zhang, Fu-Wen Shu, Yun Soo Myung et al.* · `gr-qc` · arXiv:2611.27195v1 · relevance 0.20

- **In one sentence**: Computes Type-II quasinormal mode frequencies (coupled gravitational, dilaton and electromagnetic perturbations) of a magnetically charged dilaton-Euler-Heisenberg black hole in AdS for ℓ=0,1,2, and relates the ℓ=0 dilaton modes to thermodynamic phase transitions.</one_liner>
<parameter name="plain">The paper studies how a specific charged black hole in a curved "anti-de Sitter" universe vibrates after being disturbed, the way a struck bell rings and then fades. The authors compute the frequencies and fading rates of these vibrations for gravity, a scalar "dilaton" field, and electromagnetism acting together. They report that the black hole's vibrations die out, so it is stable, and they link some of the vibration behavior to changes between small and large black hole states.
- **Why it matters**: Quasinormal modes are a main way physicists describe how black holes settle down after disturbance, and the paper suggests a possible link between these vibrations and thermodynamic phase transitions. The text does not show how far this connection generalizes beyond this model, so its wider significance is uncertain.
- **Background needed**: - Black hole: a region of spacetime whose gravity prevents anything, including light, from escaping.
- Anti-de Sitter (AdS): a negatively curved spacetime often used as a theoretical testing ground.
- Quasinormal modes: characteristic vibration frequencies of a black hole; the real part gives the oscillation rate and the imaginary part gives how quickly it fades. Negative imaginary part means stable decay.
- Dilaton: an extra scalar field that can appear in some gravity theories.
- Euler-Heisenberg: a nonlinear correction to electromagnetism from quantum effects.
- Multipole ℓ: the angular shape of a vibration (ℓ=0 monopole, ℓ=1 dipole, ℓ=2 quadrupole).
- Numerical methods: direct integration and Chebyshev pseudospectral methods are ways of solving the equations on a computer.
- Thermodynamic phase transition: an abrupt change between states of a system, analogous to water boiling; here between small and large black holes. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we investigate Type-II quasinormal modes (QNMs) of a magnetically charged dilaton--Euler--Heisenberg black hole in anti-de Sitter (AdS) spacetime. The Type-II includes coupled gravitational, dilaton and electromagnetic perturbations. Its coupled equations are derived for $\ell=0,1,2$ modes and the QNM frequencies are calculated by employing direct integration and Chebyshev pseudospectral methods, giving consistent results. For nondegenerate dipole ($\ell=1$) mode at fixed curvature, the nonlinear correction starts at order $Q^2$ for electromagnetic-led branch and at order $Q^4$ for scalar-led branch. In this case, stronger AdS curvature enhances reduction of the electromagnetic-led real frequency for positive coupling, while gravitational-led quadrupole real frequency changes weakly with charge. As the curvature weakens, the dipole frequencies approach the AdS normal-mode scale and their damping decreases. We find that all modes computed have negative imaginary parts for nonextremal black holes, implying this black hole is stable against Type-II perturbations. Furthermore, we explore the connection between thermodynamic phase transition and QNMs for $\ell=0$ dilaton. For a subcritical isobaric process, the QNM real frequency of $\ell=0$ dilaton decreases with increasing temperature of small black holes, while it increases with increasing temperature of large black holes. At coexistence, the damping rate for large black holes is about 4.28 times that for small black holes.

</details>

### [Onset of quantum chaos in a family of two-dimensional conformal field theories](https://arxiv.org/abs/2611.26694)
*Felix M. Haehl, Moshe Rozali* · `hep-th` · arXiv:2611.26694v1 · relevance 0.16

- **In one sentence**: In a family of two-dimensional K3 sigma models near the Kummer orbifold point, first-order anomalous dimensions of non-BPS operators in a symmetry-restricted sector follow GOE random-matrix statistics, in contrast to the singlet deformation, which retains exact degeneracies and slower convergence to GOE.
- **In plain words**: This paper studies a quantum field theory describing a two-dimensional world whose extra dimensions are shaped like a K3 surface, a special geometric shape from string theory. The authors tilt the theory slightly in several directions and measure how the energy levels of its particles split apart at first order. They find that, once the obvious symmetries are accounted for, the splittings look like the statistics of random matrices, a pattern that appears in many complex quantum systems.
- **Why it matters**: Random-matrix level statistics are a widely used signature of quantum chaos, so finding them in a solvable string-inspired conformal field theory is of interest for understanding when such chaos appears. The text does not establish broader implications beyond the comparison with the singlet deformation, so the wider connections should be treated as open.
- **Background needed**: - Two-dimensional conformal field theory: a quantum theory on a 2D surface that looks the same under scaling; its states have "scaling dimensions," which play the role of energies.
- Sigma model with K3 target space: the 2D theory whose fields live on a K3 surface, a compact four-dimensional shape used in string theory.
- Supersymmetry N=(4,4): an extra symmetry relating bosonic and fermionic partners.
- BPS vs non-BPS operators: BPS states have protected dimensions; non-BPS ones can shift under deformation.
- Marginal deformation: a small change of the theory that does not change its scale behavior at leading order; the coupling parameter is often called a direction in a parameter space.
- Orbifold: a space obtained by quotienting by a symmetry group, here T^4/Z_2 (Kummer point).
- Anomalous dimension / first-order splitting: the leading shift in energy levels as the coupling goes to zero.
- Random matrix theory: statistics of eigenvalues of random symmetric matrices; the Gaussian orthogonal ensemble (GOE) is the standard case, with level repulsion and long-range rigidity.
- Spectral diagnostics: measures such as gap ratios and unfolded spectra used to test whether levels follow GOE. · level: research-level

<details><summary>Original abstract</summary>

We exhibit random matrix statistics in the scaling dimensions of non-BPS primary operators in a family of two-dimensional conformal field theories. Specifically, we consider the sigma model with K3 target space and $\mathcal N=(4,4)$ supersymmetry in a neighborhood of the Kummer orbifold point $\mathbb T^4/\mathbb Z_2$. At the free-fermion radius, the spin-zero spectrum of the $\mathbb Z_2^4$-invariant sector is exactly degenerate at integer energies. The exactly marginal blow-up deformations that preserve this symmetry form a four-dimensional space, whose directions we parametrize by unit quaternions. Along each deformation direction, we compute the first-order splitting of the degenerate levels, i.e., the leading anomalous dimensions as the coupling goes to zero. In sectors where all exact symmetries are resolved, including a hidden $\mathbb Z_2$ at the even levels, the non-zero first-order shifts along a generic direction follow the Gaussian orthogonal ensemble (GOE), as we verify by computing several spectral diagnostics. We compare quantitatively with the well-known singlet deformation, which has enhanced symmetry: even after all its known symmetries are resolved, its first-order spectrum has exact degeneracies, its gap ratio approaches the GOE value only slowly as the energy increases, and its unfolded spectrum lacks the long-range rigidity of the GOE.

</details>

## Statistical physics

### [Large deviations, effective dynamics, and dynamical phase transitions in random maps](https://arxiv.org/abs/2611.26704)
*\'Angela Tajuelo-Valbuena, Jorge Hidalgo, Ricardo Guti\'errez et al.* · `cond-mat.stat-mech` · arXiv:2611.26704v1 · relevance 0.20

- **In one sentence**: The paper extends the Doob transform and spectral large-deviation methods, previously used for deterministic chaotic maps, to random maps in order to construct effective dynamics for rare trajectories and identify dynamical phase transitions.
- **In plain words**: The paper studies unusual, rare behaviour over long runs of a simple iterated system whose update step includes randomness. Such rare histories are exponentially hard to observe by ordinary sampling. The authors build a modified dynamics in which these rare histories become typical, so they can be reproduced directly, and they use the spectrum of a modified operator to find which starting states lead the system into one behaviour regime or another.
- **Why it matters**: Rare fluctuations and sudden switches between behaviour regimes matter across statistical physics, and the text suggests the framework is general to random chaotic maps. The summary itself does not show concrete applications beyond these models, so the broader significance is not established here.
- **Background needed**: - Large deviation theory: the mathematics of how probable or improbable long-run averages are, and how fast their chance of occurring falls off.
- Map: a rule that updates a system's state in discrete steps (for example, x to f(x)); a random map adds noise to each step.
- Doob transform: a reweighting of a process that makes a chosen rare event the typical outcome, yielding an "effective dynamics".
- Tilted operator: a modified version of the update rule, weighted by an exponential factor, whose largest eigenvalue encodes the rate of rare events.
- Dynamical phase transition: an abrupt change in the character of typical rare trajectories as the observed quantity or the weighting is varied.
- Chaotic system: one highly sensitive to initial conditions, so its long-run behaviour is hard to predict. · level: research-level

<details><summary>Original abstract</summary>

Large deviation theory provides a natural framework to characterize rare fluctuations of time-averaged observables in deterministic and stochastic systems. Building on previous results for deterministic chaotic maps, here we extend the Doob transform to random maps, constructing an effective dynamics in which rare events become typical. This makes it possible to directly reproduce the dynamics of rare trajectories that are exponentially difficult to sample under the original dynamics. We further apply spectral large-deviation methods to characterize dynamical phase transitions in random maps. The spectral structure of the tilted operator provides insight into the mechanisms underlying these transitions and, in particular, allows us to identify the appropriate initial states that select one dynamical phase or another. Our results extend the connection between large deviation theory, spectral methods, and effective dynamics to random chaotic maps, providing a general framework to study rare events and dynamical phase transitions in these systems.

</details>

### [Cup and Cap Topological Neural Network](https://arxiv.org/abs/2610.03169)
*Marta Niedostatek, Ferran Hernandez Caralt, Runyue Wang et al.* · `cond-mat.dis-nn` · arXiv:2610.03169v2 · relevance 0.15

- **In one sentence**: The paper proposes the Cup and Cap Topological Neural Network (CCNN), which uses cup and cap products from algebraic topology to move signals between simplicial dimensions in one layer and learn node-level features that account for higher-order (e.g. triangle) interactions, and reports competitive results on TopoBench datasets.
- **In plain words**: Standard neural networks for data shaped like networks look mainly at nodes, edges and filled triangles, but the usual methods can only pass information one level up or down per layer. This paper introduces a way to move information across more than one level at once, using mathematical operations called cup and cap products. The authors test the resulting network on existing benchmark datasets and report that it performs competitively with other networks built on the same kind of structure.
- **Why it matters**: The work offers a new mathematical mechanism for passing information across several levels of a higher-order structure within one layer, which may matter for modelling group interactions in data. The text only reports competitive benchmark performance, so its practical advantage over existing methods is not established here.
- **Background needed**: - Simplicial complex: a way to describe data using nodes, edges (pairs), triangles (triples) and higher filled shapes, capturing group interactions.
- Topological deep learning: neural networks designed to work on these shapes rather than on plain graphs.
- Cochain: an assignment of values to the nodes, edges or triangles of such a shape; node-based variables are 0-cochains.
- Boundary operator and Hodge Laplacian: standard tools that move values between neighbouring dimensions, usually one step at a time.
- Cup and cap products: operations from algebraic topology that combine cochains across dimensions, allowing jumps of more than one dimension.
- TopoBench: a benchmark collection of datasets for topological neural networks. · level: research-level

<details><summary>Original abstract</summary>

Topological Deep Learning (TDL) is designed to learn features associated not only with nodes but also with edges, triangles and higher dimensional simplices. However, most TDL approaches, being based on boundary operators and Hodge Laplacians, have the limitation that features and signals cannot be lifted or lowered across more than one dimension per layer. To overcome this limitation, in this work, we propose the adoption of the cup and cap products. Specifically, we formulate the Cup and Cap Topological Neural Network (CCNN), a topological deep learning architecture designed to learn node-based variables (or 0-cochains) by taking into account their many-body interactions (e.g. triangles) present in the data. We validate CCNN by assessing its performance on the TopoBench datasets, demonstrating its competitive performance with respect to other simplicial complex neural networks.

</details>

## Condensed matter

### [Topological phases protected by half-chiral symmetry](https://arxiv.org/abs/2611.26693)
*Chen-Shen Lee, Itamar Kimchi* · `cond-mat.mes-hall` · arXiv:2611.26693v1 · relevance 0.21

- **In one sentence**: The paper proposes topological phases protected by "half-chiral" symmetry, where the sublattice (chiral) symmetry holds on only one sublattice, along with a real-space invariant framework and a 2D Kekulé honeycomb model with a single corner zero-energy mode.
- **In plain words**: Some materials have atoms arranged in two interlocking groups, and in certain textbook models hopping between atoms of the same group is forbidden, which pins certain states to zero energy. This paper looks at a weaker version where that rule holds only on one of the two groups, as might happen in graphene next to hexagonal boron nitride or in zincblende-type crystals. The authors build a way to classify and detect the protected edge or corner states in this setting and show, in a two-dimensional model, that a single zero-energy state can sit at one corner.
- **Why it matters**: It extends the well-known idea of sublattice-protected topology to a symmetry that is defined by an algebraic constraint rather than a group operation, which the authors say needs a new framework. It may be relevant to designing edge or corner states in engineered two-dimensional materials, but the text does not establish any experimental realization or practical application.
- **Background needed**: - Topological phase: a property of a material's electronic or wave structure that stays the same under smooth changes, often linked to robust edge or corner states.
- Chiral (sublattice) symmetry: in a lattice split into two sublattices A and B, hopping only connects A to B, which forces certain energies to zero.
- SSH chain: a simple one-dimensional chain model that is the standard example of this kind of topology.
- Hamiltonian: the matrix describing the energies and couplings of a system.
- Zero-energy mode: a state whose energy is exactly zero, here pinned by the symmetry.
- Higher-order topology: protected states that appear at corners or hinges rather than along a whole edge.
- Honeycomb lattice and Kekulé distortion: graphene-like hexagonal lattice and a pattern of bond-strength modulation that opens topological gaps.
- Real-space invariant: a topological index computed directly from atomic positions, without assuming a periodic crystal in momentum space. · level: research-level

<details><summary>Original abstract</summary>

Chiral (or sublattice) symmetry describes bipartite systems such as the Su-Schrieffer-Heeger (SSH) chain where same-sublattice A-A and B-B hoppings are forbidden, enabling the protection of topological phases. Here we identify new topological phases protected by half-chiral symmetry wherein chiral symmetry is preserved on only one sublattice, as may occur with sublattice imbalance (e.g. graphene-hBN) or localized orbitals (e.g. zincblende). Unlike conventional symmetry operators described by group theory, half-chiral symmetry is an algebraic constraint on the sublattice-projected Hamiltonian such as $PHP=0$, requiring a new framework for topological protection. We develop such a framework, identifying real-space bulk topological invariants and corresponding topological boundary modes that stick to zero energy. In two dimensions we construct a half-chiral Kekule honeycomb model and show that its unusual higher-order topology protects a single zero-energy mode at a single corner.

</details>

### [Comparing weakly interacting and free quantum dynamics locally](https://arxiv.org/abs/2611.27707)
*Jorge Acu\~na Flores, Joscha Henheik, Marius Lemm et al.* · `math-ph` · arXiv:2611.27707v1 · relevance 0.15

- **In one sentence**: Uses Lieb-Robinson bounds to show that, locally and on large perturbative time scales, weakly interacting many-body fermion dynamics (quantum diffusion of an operator-spreading diagnostic, and spin-up correlators in Fermi-Hubbard models with low spin-down density) match their non-interacting counterparts.</one_liner>
<parameter name="plain">The paper studies how quantum particles spread and interact in systems with many particles on a lattice. The authors show that when interactions are weak, the local behavior can be approximated by a simpler model where particles do not interact, and they use known results for that simpler model to draw conclusions about the full system over finite time windows.
- **Why it matters**: It gives a rigorous way to carry results from the easier non-interacting case over to weakly interacting systems, with two concrete applications. The second application is tied to numerical observations of entanglement patterns by Bippus et al., so it may help explain those observations, though the text does not establish that link beyond stating the correspondence.
- **Background needed**: - Lattice quantum many-body system: many quantum particles on a grid of sites, with local interactions.
- Lieb-Robinson bound: a mathematical limit saying information or influence spreads through a lattice at a roughly finite speed, so distant effects are negligible over short times.
- Perturbative: valid when a small parameter (here, interaction strength or disorder) is small, giving results as expansions.
- Quantum diffusion: spreading that resembles random walk or heat flow, here measured by an operator-spreading diagnostic.
- Out-of-time-ordered correlator (OTOC): a correlation function used to measure how quantum information scrambles over time.
- Fermi-Hubbard model: a standard lattice model of interacting electrons with spin up and spin down.
- Non-interacting (free) dynamics: the simpler case where particles do not interact, which is exactly solvable. · level: research-level

<details><summary>Original abstract</summary>

Lieb-Robinson bounds (LRBs) have become a standard tool for perturbative results in quantum many-body physics, including gap stability and many-body adiabatic theory. Here, we use LRBs to locally approximate weakly interacting many-body dynamics with one-body dynamics on large, perturbative time scales. This allows us to use one-body transport results to establish the expected many-body transport behavior on finite time scales in the following two illustrative settings: (i) We prove quantum diffusion, as quantified by a certain operator spreading diagnostic, in weakly interacting and weakly disordered Fermi systems in dimensions $D\geq2$ on large finite time scales based on the non-interacting diffusion result of Black, Drogin, and Hern\'andez [arXiv:2506.06468]. (ii) We show for Fermi-Hubbard models with initially low spin-down density, that all local multi-time spin-up correlation functions are approximated by their free counterparts. In particular, we obtain an OTOC (out-of-time-ordered correlator) counterpart to the patterns of short-time entanglement related to lattice path counts observed numerically by Bippus et al. [Phys. Rev. B 113, 035152 (2026)].

</details>

## Particle physics

### [Probing Compressed Dark Sectors at a Muon Collider through Dilepton Signatures and Machine Learning](https://arxiv.org/abs/2611.27518)
*Mohamed Belfkir, Ayoub Hmissou, Larbi Rahili* · `hep-ph` · arXiv:2611.27518v1 · relevance 0.19

- **In one sentence**: A study proposing that machine-learning classifiers (BDT and XGBoost) applied to dilepton final states at a future muon collider could help detect inert-doublet-model scalar dark matter in compressed mass spectra, via the process μ+μ− → AH with A → HZ*, Z* → ℓ+ℓ−.
- **In plain words**: Physicists are asking whether a future muon collider, a machine that smashes muons into each other, could spot a hidden kind of dark matter particle. The idea is to look for a specific pattern of two charged leptons (electron or muon pairs) that would show up when a heavier hidden particle decays into a lighter one plus a Z boson. Machine-learning tools are used to pick these signals out from ordinary background events.
- **Why it matters**: Dark matter is well established from its gravitational effects but its particle nature is unknown, and this work tests whether a proposed future collider could reach a region of the model that is hard to probe otherwise. The text does not give quantitative sensitivity results in the excerpt provided, so the strength of the claimed discovery potential cannot be judged from it.
- **Background needed**: - Standard Model: the established theory of known particles and forces.
- Inert doublet model: a simple extension adding a second Higgs-like field whose lightest neutral part could be dark matter.
- Compressed spectrum: the heavier and lighter hidden particles have nearly equal masses, so the decay products are soft and hard to separate from background.
- Relic abundance: the amount of dark matter left over from the early universe; the model struggles to match the observed amount in some regions.
- Muon collider: a proposed future collider using muons, which can give cleaner collisions than protons.
- Dilepton signature: a pair of oppositely charged leptons used as the detectable trace of the event.
- Boosted decision trees / XGBoost: machine-learning methods that combine many simple yes/no rules to classify events as signal or background. · level: research-level

<details><summary>Original abstract</summary>

The inert doublet model (IDM), a minimal extension of the Standard Model (SM), provides a scalar dark matter (DM) candidate that belongs to the additional Higgs doublet. The model faces challenges in achieving the correct relic abundance for compressed spectra and DM masses in the high-mass range. In this work we investigate the prospects of detecting dark matter candidates at future high-energy muon colliders. Focusing on the process $\mu^+ \mu^- \to AH$ with subsequent decay $A \to H Z^*$ and $Z^* \to \ell^+\ell^-$, we explore the sensitivity of machine learning techniques, specifically Boosted Decision Trees (BDT) and XGBoost, to distinguish the signal from Standard Model backgrounds. We demonstrate that the combination of advanced multivariate analysis with high-luminosity muon collisions enhances the discovery potential for inert scalars in compressed mass spectra scenarios.

</details>

### [From Resonance Properties to High-Energy Behavior: The $R$ Ratio from Lattice QCD](https://arxiv.org/abs/2611.27586)
*Nan Wang, Long-cheng Gui, Jun Hua et al.* · `hep-lat` · arXiv:2611.27586v1 · relevance 0.17

- **In one sentence**: Bayesian reconstruction of the lattice-QCD R-ratio from Euclidean correlators near the physical pion mass, checking the rho-meson resonance parameter f_rho and the smeared R-ratio against experiment over 0.25–2.50 GeV, with finite-volume effects compared across ensembles up to about 10 fm.
- **In plain words**: Physicists compute how often electrons and positrons annihilate into hadrons at a given collision energy, a quantity called the R-ratio, using large computer simulations of the strong force on a lattice of space-time points. This paper reports that a statistical reconstruction method applied to those simulations reproduces the smooth high-energy shape seen in experiments. It also finds that integrating the rho-meson peak gives a decay-related constant close to the experimental value, with about 1% statistical precision.
- **Why it matters**: Matching lattice simulations to measured collision data is a test of whether the underlying theory of the strong force is being computed correctly, and the R-ratio feeds into precision estimates in particle physics. The text does not establish how significant the agreement is beyond the stated comparisons, and the connections it mentions (other channels, decay rates, hadronic tensors) are proposals rather than demonstrated results.
- **Background needed**: - Strong force (QCD): the theory binding quarks and gluons into protons, neutrons and pions.
- Lattice QCD: simulating QCD on a discrete grid of space-time points on a computer.
- R-ratio: the ratio of hadron production to muon production in electron–positron collisions; a standard probe of the strong force.
- Euclidean correlators: lattice outputs in imaginary time that must be converted to real-energy spectra, which is an ill-posed inverse problem.
- Bayesian reconstruction: a statistical method for inferring the most probable spectrum from noisy data.
- Rho meson: a short-lived particle that dominates the low-energy R-ratio as a peak.
- f_rho: a decay constant describing how strongly the rho couples to its decay channel.
- Gaussian smearing: a blurring of the spectrum with a bell-shaped kernel of width sigma (here 0.6 GeV) to compare with experimental resolution.
- Finite-volume effects: distortions arising because the simulated box has a finite size. · level: research-level

<details><summary>Original abstract</summary>

We investigate resonance properties and inclusive spectral behavior through Bayesian reconstruction of the $R$-ratio from Euclidean lattice correlators near the physical pion mass. Without additional Gaussian smearing, the reconstructed spectrum already captures the smooth high-energy behavior observed in experiment. Direct integration of the $\rho$ peak determines $f_\rho$ with approximately $1\%$ statistical precision and close agreement with the experimental reference, providing access to resonance properties without resolving individual finite-volume levels. With a common Gaussian width of $\sigma=0.6$~GeV, the lattice and experimental $R$-ratios show good overall agreement over $0.25$--$2.50$~GeV. Comparisons among ensembles with spatial extents up to approximately $10$~fm demonstrate that finite-volume effects can be controlled across these complementary observables. These results demonstrate a unified framework for studying resonance and inclusive physics from lattice QCD, with potential applications to other hadronic channels, inclusive decay rates, and hadronic tensors.

</details>

## Nuclear physics

### [Nuclear Shell Model on the Light Front](https://arxiv.org/abs/2611.26895)
*Zhenkai Fu, Adam Freese, Gerald A. Miller* · `nucl-th` · arXiv:2611.26895v1 · relevance 0.17

- **In one sentence**: The paper analytically solves a light-front harmonic oscillator model of nuclear shell structure and electromagnetic form factors, finds shell splitting that depends on the longitudinal excitation quantum number, attributes it to the longitudinal confinement interaction via Hellmann-Feynman, and applies it to 48Ca and 208Pb.
- **In plain words**: This paper looks at how protons and neutrons are arranged inside atomic nuclei, using a version of quantum theory that treats space and time more evenly than the usual approach. The authors solved a simplified model exactly and compared it with the familiar non-relativistic picture. They report that the relativistic version reduces to the familiar one in the simple limit but splits energy levels in an extra way, and that predicted charge distributions (form factors) differ noticeably between the two approaches.
- **Why it matters**: Nuclear shell models and charge distributions are basic inputs to nuclear physics, so a tractable way to include relativistic effects could matter for interpreting experiments on nuclei like calcium-48 and lead-208. The text does not show how large these effects are compared with experimental precision, so its practical importance remains to be judged.
- **Background needed**: - Nuclear shell model: nucleons fill discrete energy levels, like electrons in atoms; the model explains magic numbers of stable nuclei.
- Harmonic oscillator: a simple model where particles sit in a parabolic potential with evenly spaced energy levels, often used as a first approximation.
- Non-relativistic treatment: ignores effects from particles moving at speeds comparable to light, the standard approach in nuclear structure.
- Light-front framework: a way of formulating relativistic quantum theory using "light-front" time, which simplifies calculations of particle structure.
- Form factor: a function describing how a particle's charge or current is spread out, measured by scattering electrons off nuclei.
- Hellmann-Feynman theorem: a standard result relating how energy changes with a parameter to the expectation value of that parameter's operator; here used to pinpoint which interaction causes the splitting.
- Longitudinal confinement: the part of the binding force acting along the direction of motion in the light-front picture. · level: research-level

<details><summary>Original abstract</summary>

Light-front descriptions of nuclear structure provide a relativistic framework that can potentially deepen our understanding of nuclear structure by revealing effects that are absent from traditional non-relativistic treatments. To utilize this framework, we start from the light-front harmonic oscillator to analytically calculate the shell structure and electromagnetic form factors. The relativistic shell model shows that the light-front result recovers the nonrelativistic oscillator limit while introducing shell splitting that depends on the longitudinal excitation quantum number. We derive the resulting effects on the shell model and use the Hellmann-Feynman theorem to identify the longitudinal confinement interaction as the origin of this splitting. We illustrate these results through applications to $^{48}\mathrm{Ca}$ and $^{208}\mathrm{Pb}$. In addition, we demonstrate a substantial difference between form factors calculated using non-relativistic and light-front treatments, a difference that further underscores the importance of including relativistic effects in the description of nuclear structure. Our findings demonstrate a tractable approach to relativistic nuclear calculations and show how extending nuclear models beyond the non-relativistic approximation can yield meaningful physical insight.

</details>

### [Nuclear Precision and Multimessenger Constraints on Neutron-Star Structure](https://arxiv.org/abs/2611.27669)
*Hisham Anwer, A. Adel, E. Omar* · `nucl-th` · arXiv:2611.27669v1 · relevance 0.10

- **In one sentence**: The paper defines an observable-dependent variance ceiling on neutron-star core structure and proposes radius–Love-number compensation as a mechanism that suppresses how well nuclear constraints pin down tidal deformability, tested across four data-conditioned equation-of-state families.
- **In plain words**: Neutron stars are extremely dense remnants of collapsed stars, and their interiors are hard to pin down even with lab nuclear data. This paper asks how much the core's structure can still vary after those lab constraints are applied, and how other stellar measurements could narrow it. The authors report that combining a pulsar radius measured to 0.3 km with a tidal measurement from a binary system to 10% would remove roughly 44 to 68% of the current uncertainty in the tidal response (the logarithmic Love number).
- **Why it matters**: The result gives a concrete estimate of how much two kinds of astronomical measurement could reduce uncertainty about dense matter, linking laboratory nuclear physics to stellar observations. The text does not show how these projected precisions compare with what current or planned instruments will deliver, so its practical impact is uncertain.
- **Background needed**: - Neutron star: the collapsed core of a massive star, roughly 20 km across, with matter denser than an atomic nucleus.
- Equation of state (EOS): a rule relating pressure to density for matter; choosing one fixes the star's size and structure.
- Tidal deformability / Love number: how easily a star's shape is stretched by a companion's gravity; it is sensitive to the EOS.
- Variance: a measure of spread or uncertainty in a quantity across plausible models.
- Multimessenger astronomy: combining different signals, such as gravitational waves, X-rays, and radio pulses, to study one object.
- Logarithmic quantity: uses the log of a value so that relative, rather than absolute, differences are compared. · level: research-level

<details><summary>Original abstract</summary>

Neutron-star cores retain structural freedom beyond the constraints supplied by nuclear measurements. We quantify this freedom through an observable-dependent variance ceiling and identify radius--Love compensation as a mechanism suppressing nuclear constraints on tides. Across four data-conditioned equation-of-state families, a pulsar radius measured to 0.3 km paired with a binary tide measured to 10\% removes 44--68\% of the current logarithmic Love-number variance. The framework connects laboratory precision and complementary stellar measurements to core structure.

</details>

## Quantum information and computing

### [Autonomous quantum machine learning via Riemannian gradient-based optimization](https://arxiv.org/abs/2611.27815)
*Kasidit Srimahajariyapong, Thiparat Chotibut, Suwannachad Suwannajitt et al.* · `quant-ph` · arXiv:2611.27815v1 · relevance 0.25

- **In one sentence**: The paper proposes autonomous quantum machine learning, where Riemannian gradient-based training runs entirely inside a quantum circuit without quantum measurements or a classical optimization loop, and reports convergence and circuit-depth analysis plus numerical tests on phase classification and unitary learning with a hidden symmetry.
- **In plain words**: Most quantum machine learning today trains by repeatedly measuring a quantum device and feeding the results to a classical computer, which tends to be a bottleneck. This paper proposes a way to let the training update happen inside the quantum system itself, with no measurements or classical feedback during training. The authors report a convergence guarantee, an analysis of how circuit depth grows, and numerical tests showing the model can pick up a hidden symmetry in the data.
- **Why it matters**: Removing the measure-and-feedback loop addresses a stated scalability bottleneck in quantum machine learning, so the idea is worth watching. The claims rest on theory and numerical simulations described in the text; it is unclear from this summary how the approach performs on real hardware or at larger scales.
- **Background needed**: - Quantum machine learning: training a model whose parameters set a quantum circuit's operations.
- Measurement bottleneck: quantum devices give limited classical information per run, so training usually needs many repeated measurements.
- Gradient optimization: adjusting parameters step by step in the direction that reduces a cost function.
- Riemannian gradient: a version of gradient descent adapted to curved mathematical spaces, such as the set of valid quantum operations (unitaries).
- Circuit depth: the number of sequential layers of gates in a quantum circuit; deeper circuits are harder to run on noisy hardware.
- Symmetry: a transformation that leaves the data's structure unchanged; here the model is said to find such symmetries without being told them.
- Exponential convergence: the error shrinks by a fixed fraction each training step. · level: research-level

<details><summary>Original abstract</summary>

Quantum machine learning models typically rely on repeated quantum measurements and classical optimization during training, making the quantum-to-classical information-extraction process a fundamental bottleneck for scalability. We propose a framework for autonomous self-training quantum machine learning, based on Riemannian gradient optimization, in which the optimization proceeds entirely within the quantum domain without requiring quantum measurements or classical feedback. We derive the Riemannian gradient update rules for a broad class of learning tasks and identify sufficient conditions under which the resulting training dynamics can be realized fully autonomously. Within this regime, we establish an exponential convergence guarantee, in the training iterations, for sufficiently small step sizes, and further analyze the training cost in terms of the growth of the circuit depth. Importantly, we further show that the trained model can automatically discover symmetries hidden in the training data without $\textit{a priori}$ specification. For the canonical examples of quantum phase classification and unitary learning with a hidden symmetry, our numerical study indicates that learning can be achieved at low circuit depths with only a few distinct training examples. Our results thus establish autonomous quantum machine learning as a promising paradigm that removes the classical optimization loop while retaining strong theoretical guarantees and practical performances.

</details>

### [Practical insights into controlling exponential concentration in quantum machine learning](https://arxiv.org/abs/2611.27486)
*Fernando Mondragon-Sampedro, Diego Alvarez-Estevez* · `quant-ph` · arXiv:2611.27486v1 · relevance 0.19

- **In one sentence**: A comparative empirical study of exponential concentration (observables becoming insensitive to inputs as system size grows) across fidelity quantum kernels, projected quantum kernels, and quantum extreme learning, examining how measurement locality, entanglement, expressivity, and bandwidth scaling affect it.
- **In plain words**: Quantum machine learning models can lose their ability to tell inputs apart as the quantum system gets bigger, a problem called exponential concentration. This paper compares three quantum learning approaches on this problem and tests whether shrinking the range of the input encoding can help. The authors report that global fidelity-based kernels suffer most, local measurements help but do not remove the effect, and shrinking the encoding helps only up to a point.
- **Why it matters**: Concentration is a known obstacle to scaling quantum machine learning, so practical guidance on which design choices reduce it is useful to people building these models. The text is a study of specific architectures rather than a general proof, so its findings may not carry over to all quantum models.
- **Background needed**: - Quantum machine learning: using quantum circuits as models that learn from data.
- Quantum kernel: a similarity measure between data points computed on a quantum device; used by classical learning methods such as support vector machines.
- Fidelity: a number measuring how closely two quantum states match.
- Observable and expectation value: a measurement quantity and its average outcome over repeated runs.
- Variance and concentration: if outputs barely vary across inputs, the model cannot separate them; exponential concentration means this gets exponentially worse with qubit count.
- Entanglement: quantum correlations between qubits; more entanglement can increase concentration.
- Expressivity: how wide a range of quantum states a circuit can reach.
- Bandwidth scaling: rescaling input data before encoding it into rotation angles, which controls how much the encoding varies.
- Quantum extreme learning: a fixed quantum "reservoir" processes inputs and only a simple readout is trained. · level: research-level

<details><summary>Original abstract</summary>

Quantum Machine Learning (QML) models are often limited by exponential concentration, where quantum observables become insensitive to input variations as system size increases. In this work, we provide a comparative empirical study of this phenomenon across Fidelity Quantum Kernels (FQK), Projected Quantum Kernels (PQK), and Quantum Extreme Learning (QEL), within a unified observable-based framework based on expectation-value variance. We investigate how measurement locality, entanglement, and circuit expressivity shape concentration across different architectures. Global fidelity-based kernels exhibit strong concentration driven by Hilbert space dimensionality, whereas local-observable approaches reduce but do not eliminate this effect. In PQK and QEL, concentration is primarily governed by entanglement and quantum dynamical expressivity, with reservoir depth emerging as a key factor in QEL architectures. We further study bandwidth scaling as a general mechanism for controlling encoding expressivity across all models. Our results indicate that bandwidth scaling effectively reduces concentration in moderate regimes by restricting the effective expressivity of the encoding, though this protective effect diminishes in highly expressive structural settings.

</details>

## Optics and atomic physics

### [Coherence Lengths of Laser Pointers](https://arxiv.org/abs/2611.26878)
*Vaishnavi Rao Namakkal Ranga Rao, Marissa R. Godoy, Mark D. Sotnikov et al.* · `physics.optics` · arXiv:2611.26878v1 · relevance 0.15

- **In one sentence**: The paper measures the coherence lengths of several low-cost green laser pointers (three diode lasers and one frequency-doubled DPSS laser) using a noncollinear-beam optical interferometer read out by a CMOS detector array, while noting their multimodal behavior.
- **In plain words**: Laser pointers are cheap, and this paper asks how far along the beam their light stays "in step" with itself, which determines how well it can produce interference patterns. The authors tested four green laser pointers with a simple interferometer and found that this distance varies from device to device but can regularly exceed 10 cm.
- **Why it matters**: The text is brief, so the main value is practical: it suggests these inexpensive devices can be used to teach coherence and interference measurements in an advanced undergraduate lab. It also hints at possible new laser-pointer designs that exploit interference, though the text does not develop that idea.
- **Background needed**: - Coherence length: the distance over which a light beam's waves stay correlated enough to interfere; longer means more "orderly" light.
- Interferometer: an instrument that splits a beam, recombines it, and reads the resulting bright and dark fringes to measure such properties.
- Multimodal laser: a laser emitting several closely spaced wavelengths at once, which shortens coherence length.
- Diode laser vs. DPSS laser: a diode laser is driven directly by electric current; a DPSS (diode-pumped solid-state) laser uses a diode to pump a crystal, and frequency doubling converts its infrared output to green.
- CMOS detector array: the same kind of light-sensitive chip found in digital cameras. · level: intermediate

<details><summary>Original abstract</summary>

We report on the coherence lengths of low-cost green laser pointers in the midst of multimodal behavior using an optical interferometer based on noncollinear beam geometries and a CMOS detector array. Examined devices include three diode lasers and a frequency-doubled neodymium-emission diode-pumped solid state (DPSS) laser. Coherence length measurements are variable among devices, but values can nevertheless regularly exceed 10 cm. The work serves as a template for an advanced undergraduate physics laboratory experiment and may inspire new kinds of laser pointer devices utilizing interference effects as operative principles.

</details>

### [Test of gravitational redshift by optical clocks at different latitudes](https://arxiv.org/abs/2611.27588)
*Ingo Nosske, Chetan Vishwakarma, Tim L\"ucke et al.* · `physics.atom-ph` · arXiv:2611.27588v1 · relevance 0.13

- **In one sentence**: Two Earth-fixed optical atomic clocks at different latitudes are compared against the gravitational redshift predicted by general relativity, using independent geodetic height and potential measurements, reaching a 4.6×10⁻⁵ uncertainty level.
- **In plain words**: The paper checks one of Einstein's predictions: clocks sitting at different heights tick at slightly different rates because of gravity. The authors compared two very precise optical clocks on Earth, using separately measured geodetic data for their positions, and found the observed frequency difference matches the prediction. They also argue that placing clocks at different latitudes, not just different heights, makes such a test about three times more sensitive.
- **Why it matters**: Ground-based tests of gravitational redshift have so far been less stringent than space-based ones, so a tighter Earth-based test is useful for checking general relativity. The text suggests Earth's rotation could be used as a resource for future tests, though the wider implications are not discussed in the text provided.
- **Background needed**: - Gravitational redshift: clocks lower in a gravitational field run slower compared with clocks higher up, as predicted by general relativity.
- Kinematic time dilation: clocks moving relative to each other tick at different rates; this effect has already been tested very precisely.
- Optical atomic clocks: clocks that count the oscillations of light emitted by atoms, currently the most precise timekeepers.
- Geopotential and geodesy: the gravitational and rotational energy landscape of the Earth, measured through surveying and geodetic methods.
- Centrifugal potential: the apparent outward effect of Earth's rotation, which depends on latitude and partly offsets gravity.
- Uncertainty level: the size of the remaining possible error in the comparison; smaller means a stricter test. · level: research-level

<details><summary>Original abstract</summary>

General relativity predicts that frequency comparisons between clocks are affected by both gravitational and kinematic time dilation. While the kinematic contribution has been tested with high accuracy, experimental tests of the gravitational redshift remain comparatively less stringent. Here, we measure the frequency shift between two Earth-fixed optical atomic clocks at different potentials and compare it to the redshift predicted by general relativity using independent geodetic measurements. The observed shift agrees with the prediction, testing the gravitational redshift at the $4.6 \times 10^{-5}$ uncertainty level, improving ground-based tests by a factor two. Previous ground-based tests separated the clocks mainly vertically. For clocks at different latitudes, their height difference is governed not only by the gravitational potentials at their locations but also by the centrifugal potentials caused by Earth's rotation. As both contributions can partially cancel, the gravitational contribution can be considerably larger than their height difference suggests. In this work, a separation of the clocks by $4^\circ$ in latitude enhances their sensitivity to a gravitational redshift violation threefold, to the equivalent of an approximately 1200 m difference in height for small latitudinal separation. Our results establish Earth's rotation as a so far unexploited resource for advancing ground-based tests of the gravitational redshift towards the sensitivity of previous space-based experiments.

</details>

## Fluids and plasma

### [Hot-Layer Ignition in High-Gain Inertial Confinement Fusion](https://arxiv.org/abs/2611.27760)
*M. Lourmande, B. Canaud* · `physics.plasm-ph` · arXiv:2611.27760v1 · relevance 0.13

- **In one sentence**: The paper proposes an analytical ignition criterion for a shocked deuterium-tritium shell (the "hot layer") in very high-gain inertial confinement fusion targets, showing via a three-zone model and 1D simulations that fusion alpha heating in this layer can independently ignite and recompress the hot spot, boosting target energy output by about 50%.
- **In plain words**: Inertial confinement fusion works by squeezing a small fuel capsule with lasers or X-rays so it heats up and fuses. This paper describes a way the fuel's outer shell, which has been shocked and heated, can itself catch fire from the energy carried by fusion particles, not just the central hot spot. Using a simplified model and computer simulations, the authors report that this effect could increase the total energy released by the target by roughly 50%.
- **Why it matters**: Energy gain is the central performance measure for fusion power experiments, so a mechanism that could add substantially to it is worth attention. The text does not say how far the result has been checked beyond these 1D simulations, so its relevance to real experiments remains uncertain.
- **Background needed**: - Inertial confinement fusion (ICF): compressing a small fuel pellet so its deuterium-tritium fuel fuses.
- Hot spot: the central, very hot, low-density region of the compressed fuel that starts the burn.
- Shocked shell: the denser outer layer of fuel that the implosion shock has heated and compressed.
- Ignition: the point where fusion heating becomes self-sustaining and burns through the fuel.
- Fusion alphas: helium nuclei released by fusion, which deposit energy in surrounding fuel.
- Recompression: squeezing the hot spot again after extra energy is added.
- Gain: the ratio of fusion energy released to the laser or driver energy put in.
- 1D simulation: a computer model that tracks only one spatial dimension (radius). · level: research-level

<details><summary>Original abstract</summary>

Ignition of the shocked deuterium tritium shell is identified during the thermonuclear combustion of very high-gain targets in inertial confinement fusion (ICF). This mechanism is due to the local energy deposition of the fusion alphas created in this shocked shell, independently of hot-spot ignition, and generates sufficient energy to fully recompress the hot spot. A new analytical criterion for the ignition of the hot layer is presented. A simple three zone model, based on the thick layer hot-spot model, reproduces this mechanism, which breaks down into successive stages: ignition of the hot spot, compression of the shocked shell, ignition of the shocked shell, and subsequent recompression of the hot spot. 1D numerical simulations highlight the onset of this hot layer ignition thereby satisfying the analytical ignition criterion. It is shown that this mechanism amplifies the energy released by the combustion of the target by approximately 50 %.

</details>

### [A 3D PINN-Based Framework for Patient-Specific Pulmonary Hemodynamics Using Windkessel Models](https://arxiv.org/abs/2611.27351)
*Celia Taboada, Luis Nu\~nez, Ang\'elica Casero et al.* · `math.NA` · arXiv:2611.27351v1 · relevance 0.12

- **In one sentence**: A physics-informed neural network (PINN) framework that solves pulsatile blood flow in patient-specific pulmonary artery geometry with a lumped RCR Windkessel outlet, validated on 2D channels and used for inverse identification of the three Windkessel parameters from synthetic data.
- **In plain words**: Doctors and engineers often simulate blood flow with detailed computer meshes, which are slow and hard to set up for each patient. This paper tests a different approach: a neural network trained to obey the fluid equations directly, without a mesh. The authors test it on simple channels, then on a patient's right pulmonary artery, and also use it to work backward and recover the parameters of a simplified model of the outlet from simulated data.
- **Why it matters**: Mesh-free methods could make patient-specific blood flow modeling faster and easier to use in clinics, which is the stated motivation for "digital twins." The paper is a method demonstration on one patient geometry and synthetic data, and the authors themselves note open issues (residual local pressure bias and untested robustness to noisy clinical data), so its clinical value is not yet shown.
- **Background needed**: - Computational fluid dynamics (CFD): simulating fluid flow by dividing space into a mesh and solving equations on it.
- Physics-informed neural network (PINN): a neural network trained so its outputs satisfy the governing equations, typically with a loss term penalizing equation violations, instead of using a mesh.
- Windkessel model: a simple electrical-style analogy (resistors and capacitors) that stands in for the downstream vessels and sets outlet pressure; RCR means two resistances around one capacitor.
- Basal pressure vs. local pressure: the overall pressure level versus the smaller spatial variations that actually drive flow.
- Inverse problem: inferring model parameters from observed data rather than predicting data from parameters.
- Digital twin: a computer model of a specific patient kept updated with their data. · level: research-level

<details><summary>Original abstract</summary>

Cardiovascular fluid dynamics modeling relies heavily on mesh-based numerical methods such as Computational Fluid Dynamics (CFD). While accurate, these methods entail significant computational costs and complex meshing workflows that limit their translation to clinical practice. Physics-Informed Neural Networks (PINNs) are a promising meshless alternative that embeds the governing equations directly into neural network training. In this work, we propose a PINN framework for pulsatile blood flow in patient-specific geometries with dynamic lumped-parameter Windkessel (RCR) outlet conditions representing distal vascular impedance. Coupling the Windkessel ODE to a 3D network raises two difficulties: the ODE alone does not fix the pressure level, and the local pressure variations that drive the flow are orders of magnitude smaller than the basal pressure imposed by the outlet. We address them by decomposing pressure into a time-dependent basal part and a spatially varying part, an initial condition and gauge for the Windkessel equation, a global mass-balance constraint, and a periodic Fourier embedding of time. Validated on 2D canonical channels (steady and pulsatile, with and without RCR outlet), the framework is then applied to a patient-specific right pulmonary artery, reproducing outlet flow, mean pressure, and the velocity and dynamic pressure fields with errors on the order of the data resolution. Finally, we solve the inverse problem of identifying the three Windkessel parameters of the outlet from synthetic data, recovering them with errors of about 0.3% from deliberately wrong initial values. Residual biases in the local pressure field and the need to test robustness to noisy clinical data remain open, but the results support PINNs as complementary tools for meshless hemodynamics and patient-specific digital twins.

</details>

## Biological physics

### [Receptor Abundance Alone Underpredicts Red Blood Cell Adhesion in Gaucher Disease](https://arxiv.org/abs/2611.27960)
*Zhaojie Chai, Pierre A. Buffet, Melanie Franco et al.* · `physics.bio-ph` · arXiv:2611.27960v1 · relevance 0.05

- **In one sentence**: A simulation study of red blood cell adhesion in Gaucher disease, testing whether the abundance of the Lu/BCAM laminin receptor alone explains the excess adhesion, and finding that receptor activity state appears to matter more than receptor count.
- **In plain words**: Gaucher disease is an inherited condition in which red blood cells stick abnormally to blood vessel walls. The authors built a computer model of red cells that form random molecular bonds with laminin, a protein in the vessel wall, and calibrated it on healthy donors. Using only the modest rise in the receptor count, the model underpredicted the observed sticking by roughly 1.6 to 1.7 times, so the extra adhesion seems to need more receptors that are active and able to bind.
- **Why it matters**: It suggests that counting how many receptors a cell carries can miss what drives disease-related sticking, which may matter for how cell adhesion is measured and treated. The text also reports a similar model result for sickle cell disease under hydroxyurea, but the connection to clinical outcomes is not established here.
- **Background needed**: - Red blood cells carry surface proteins that can bind to proteins lining blood vessels.
- Lu/BCAM is a surface receptor that binds laminin, a protein in vessel walls.
- Gaucher disease is an inherited enzyme deficiency that leads to abnormal cell adhesion and changes in red cells.
- Sickle cell disease is another inherited red cell disorder; hydroxyurea is a drug used to treat it.
- Phosphorylation is a chemical tag added to proteins that can switch their activity on or off.
- Shear stress is the force of blood flowing past a surface.
- Simulations model cells as objects with stochastic (randomly occurring) bonds, calibrated on control data and then used to predict disease cases. · level: research-level

<details><summary>Original abstract</summary>

Red blood cells (RBCs) in Gaucher disease (GD) adhere abnormally to vessel walls and carry more Lutheran/basal cell adhesion molecule (Lu/BCAM), a laminin receptor. Whether receptor abundance sets this adhesion is untested. We simulated RBCs carrying stochastic Lu/BCAM-laminin bonds, calibrated a population on control donors, and predicted GD adhesion from the 1.3-fold receptor rise. On laminin and endothelium the data exceed the prediction 1.6- to 1.7-fold. Matching them requires 2.4- and 4.6-fold more binding-competent receptors, compatible with the estimated 5.7-fold rise in phosphorylated receptors. Neither a stiffer membrane nor higher bond affinity removes the shortfall at high shear stress. In sickle cell disease, given active-receptor counts, the model predicts the fall in adhesion under hydroxyurea within 1.4-fold, while total receptors rise. Adhesion likely follows receptor state more than abundance. Stiffening instead retains cells at a splenic slit.

</details>

## Climate, atmosphere and Earth

### [Carbon dioxide responses shape estimates of Amazon forest vulnerability under solar geoengineering](https://arxiv.org/abs/2611.26908)
*Anupama K Xavier, Chris Jones* · `physics.ao-ph` · arXiv:2611.26908v1 · relevance 0.07

- **In one sentence**: Using a CO2-dependent forest-sustainability threshold in a shared climate phase space, this paper assesses how stratospheric aerosol injection (SAI) and other emission scenarios change Amazon forest vulnerability by late century.
- **In plain words**: The Amazon rainforest may be pushed toward loss by heat and changing rainfall. This paper asks whether deliberately reflecting some sunlight with aerosols high in the atmosphere could protect it. The authors report that this would cool the region substantially but leave it drier, with longer dry seasons, so many areas could still be at risk.
- **Why it matters**: It bears on whether solar geoengineering could be used to shield a major ecosystem, and it shows that the result depends heavily on whether higher carbon dioxide is assumed to help plants tolerate stress. The text does not show how robust this dependence is across models, so the conclusion should be treated as provisional.
- **Background needed**: - Amazon forest vulnerability: the risk that the forest shifts toward savanna or loss under heat and drought.
- Solar geoengineering (SAI): spraying reflective particles into the stratosphere to cool the planet; it offsets warming but does not fully restore rainfall patterns.
- Climate phase space: a way of plotting regions by temperature and rainfall together, so different scenarios can be compared on the same chart.
- Sustainability threshold: a line on that chart separating conditions the forest can tolerate from those linked to loss.
- CO2 fertilisation/resilience: higher carbon dioxide can help plants use water more efficiently, which may raise the threshold; this is the key assumption tested here.
- Grid cells: the small map squares climate models divide the region into; the percentages refer to these. · level: research-level

<details><summary>Original abstract</summary>

The Amazon rainforest is vulnerable to warming and changes in rainfall, yet whether solar geoengineering can reduce conditions associated with forest loss remains uncertain. Stratospheric aerosol injection (SAI) can offset greenhouse-gas-driven warming without fully restoring regional hydroclimate. Here we assess Amazon forest vulnerability under mitigation, high-emission and SAI scenarios using a Carbon dioxide-dependent forest-sustainability threshold in a common climate phase space. By late century, SAI reduces projected Amazon warming from 5.49 degree Celsius under high emissions to 2.45 degree Celsius, but substantial drying and longer dry seasons persist. Under SAI, 44.7 percentage of analysed grid cells exceed the present-day threshold, compared with 8.7 percentage when the future Carbon dioxide-dependent threshold is considered. This contrast reveals that apparent forest protection depends strongly on the assumed resilience benefits of elevated Carbon dioxide. Our findings highlight the importance of hydroclimatic changes and Carbon dioxide-dependent vegetation responses in assessing the potential of solar geoengineering to reduce Amazon forest vulnerability.

</details>

### [Spatiotemporal Landslide Runout Reconstruction from Sparse Observations with LAPIS-SHRED](https://arxiv.org/abs/2611.27132)
*Xingyue Zhang, Yuxuan Bao, Jeffrey Keck et al.* · `cs.CE` · arXiv:2611.27132v1 · relevance 0.06

- **In one sentence**: The paper applies LAPIS-SHRED, a latent-space temporal inference framework trained on physics-based simulation ensembles, to reconstruct landslide runout trajectories near Mount St. Helens from sparse sensor data, reporting NRMSE below 5.8% and a spatial correlation of 0.843 against deposit observations (versus 0.853 for the calibrated simulator).
- **In plain words**: Landslides move fast and are rarely watched as they happen, so scientists usually only see the mud and debris they leave behind. This paper tries to rebuild the full path a landslide took over time, starting from a small number of sensor readings taken at one moment or from a short early window of motion. The authors report that their method recovers complete runout paths with small errors, and that its match to observed deposits is close to that of the calibrated physics simulator it was trained on.
- **Why it matters**: Reconstructing how far and how fast a landslide travels matters for hazard planning, and few observations are often available after an event. The work is a test of whether machine learning trained on simulations can fill gaps in sparse field data; the text does not show how it performs on real, independent events beyond the deposit comparison.
- **Background needed**: - Runout: the distance and path a landslide or debris flow travels after it starts.
- Physics-based simulation ensemble: many computer runs of a flow model with varied inputs, used as training data.
- Sensor observations at a single timepoint: a snapshot of a few measurements, here 32 of them.
- Latent space: a compressed internal representation a model learns from data.
- NRMSE (normalized root-mean-square error): a scaled average size of prediction error; lower is better.
- Spatial correlation (r): how closely two maps match in pattern, from 0 (none) to 1 (perfect).
- Calibrated simulator: a physics model whose settings were tuned to match observations. · level: research-level

<details><summary>Original abstract</summary>

Reconstructing the spatiotemporal evolution of landslide runout from limited observations is a central challenge in geohazard assessment: transient flow dynamics are rarely observed directly, and available data are often confined to post-event deposits or brief monitoring windows. We apply LAPIS-SHRED (LAtent Phase Inference from Short time sequence using SHallow REcurrent Decoders) to reconstruct runout events near Mount St. Helens, USA. Trained on physics-based simulation ensembles, the framework supports both backward reconstruction from single frame and forward prediction from short initial window across different runout regimes. Using 32 sensor observations from a single timepoint, LAPIS-SHRED recovers complete runout trajectories with NRMSE below 5.8%, robust across varying observational and training conditions. Validation against observed deposits yields spatial correlation of r = 0.843 against the calibrated simulator's r = 0.853. These results suggest that latent-space temporal inference offers a viable pathway for spatiotemporal landslide reconstruction under extreme observational constraints typical of field settings.

</details>

## Cosmology

### [Beyond the Peak: Constraining early dark energy with the damping tail](https://arxiv.org/abs/2611.27069)
*Hao Wang, Gen Ye, Yun-Song Piao* · `astro-ph.CO` · arXiv:2611.27069v1 · relevance 0.16

- **In one sentence**: The paper argues that the post-peak "tail" of early dark energy (EDE), not just its peak amplitude and location, carries information about a multiscale scalar potential (combining axion-like and α-attractor-like regimes) and can improve fits to high-ℓ CMB data and the inferred H0.
- **In plain words**: Cosmologists have proposed a short-lived extra energy component in the early universe, called early dark energy, to help resolve a disagreement between two measurements of how fast the universe is expanding. Earlier work mainly looked at the size and timing of its burst of energy. This paper looks at what happens afterward, the "tail," and reports that this tail can be reshaped by the underlying field's behavior and gives a somewhat better fit to some observations.
- **Why it matters**: The Hubble tension, the mismatch between early- and late-universe measurements of the expansion rate, is an open problem, so a new observable that can distinguish models is of interest. The text supports only a modest claim: a better fit to high-ℓ CMB data and a higher best-fit H0 within this specific framework; whether it resolves the tension is not established here.
- **Background needed**: - The Hubble tension: early-universe measurements (from the cosmic microwave background, CMB) and late-universe measurements of the expansion rate H0 disagree.
- Early dark energy (EDE): a hypothetical component that briefly contributes energy shortly before recombination, raising the inferred expansion rate.
- Scalar field: a field whose value changes over time, with a potential energy that sets its dynamics.
- Axion-like and α-attractor potentials: two shapes of potential energy for a scalar field; the paper combines them in one model.
- High-ℓ CMB data: the small-scale fluctuations in the CMB, sensitive to the early universe's physics.
- Baryon acoustic oscillations (BAO) and supernovae: independent distance measurements used alongside the CMB. · level: research-level

<details><summary>Original abstract</summary>

Early dark energy is commonly characterized by the amplitude and location of its primary energy-injection peak. We show that its post-peak evolution, which we call the \emph{EDE tail}, provides an additional observable probe of the underlying scalar dynamics and can materially affect its ability to alleviate the Hubble tension. We construct a simple phenomenological framework in which distinct regions of a multiscale scalar potential govern the dynamics at different field scales. As a representative realization, we consider a potential that combines axion-like and $\alpha$-attractor-like regimes, thereby allowing the EDE tail to be reshaped through reflection and asymmetric oscillations. Confronting this framework with cosmic microwave background, baryon acoustic oscillation, and supernova observations, we find an improved fit to the high-$\ell$ CMB data together with a higher inferred bestfit $H_0$. Our results show that the EDE tail retains observable information about the underlying scalar potential that is not captured by the conventional peak parameters alone. This provides a complementary route for constructing and observationally distinguishing EDE scenarios, and potentially for further alleviating the Hubble tension.

</details>

### [Dark Energy Based on Modified Gravity: Where the Future Lies?](https://arxiv.org/abs/2611.27228)
*Shin'ichi Nojiri, Sergei D. Odintsov, V. K. Oikonomou et al.* · `gr-qc` · arXiv:2611.27228v1 · relevance 0.16

- **In one sentence**: The paper argues that some F(R) modified-gravity dark energy models compatible with DESI data can lead to anti-gravity or ghost-graviton behaviour in the future, and proposes a scalar-field potential barrier at small curvature to prevent this without fine-tuning initial conditions.
- **In plain words**: Dark energy is the unknown cause of the universe's accelerating expansion. Recent measurements hint that it may have been in an unusual "phantom" state in the recent past and then shifted to a more ordinary state. The paper shows that some realistic versions of a modified-gravity theory can drift into unphysical regimes in the future, and proposes a barrier in the underlying field that keeps the universe out of those regimes. It also suggests how such a regime could be checked using measurements of galaxy peculiar velocities and the kinematic Sunyaev-Zel'dovich effect.
- **Why it matters**: If viable dark energy models can fail in the future, that constrains which theories remain plausible as the data improve. The text does not establish how strongly the proposed barrier is favoured over other fixes, so its significance is best treated as provisional.
- **Background needed**: - Dark energy: the unknown component driving the accelerating expansion of the universe.
- Equation of state (w): the ratio of dark energy pressure to its energy density; w below -1 is the "phantom" regime, and w above -1 is "quintessence".
- DESI: a large galaxy-survey experiment whose data constrain dark energy's behaviour.
- F(R) gravity: a modification of Einstein's general relativity in which the Lagrangian is a function of the Ricci scalar curvature R.
- Scalar field: a field whose potential energy can act like dark energy; a potential barrier is a hill in that energy landscape.
- Ghost graviton: a gravitational mode with the wrong sign of kinetic energy, signalling instability.
- Peculiar velocity: the motion of galaxies relative to the smooth cosmic expansion; the kSZ effect is a distortion of the cosmic microwave background by moving electrons. · level: research-level

<details><summary>Original abstract</summary>

Based on current observational data, there is a strong possibility that dark energy was in a phantom regime in the near past, and a transition from a phantom to a quintessential regime may have occurred. Since then, many scenarios compatible with the DESI data have been proposed. In particular, there exist several realistic models in the framework of $F(R)$ gravity. In this paper, we show that such realistic models of $F(R)$ gravity may produce an anti-gravity or ghost graviton in the future. The problem could be avoided by further changing the parameters and fine-tuning the initial conditions, but we propose to introduce a potential barrier of the scalar field for the small scalar curvature region, which prevents the Universe from evolving into the anti-gravity or having a ghost graviton region, without the fine-tuning of the initial conditions. We also discuss how this regime can be tested using peculiar velocity and kSZ effect probes.

</details>

## Galaxies

### [The role of gas on the collisional runaway path to supermassive black hole seeds](https://arxiv.org/abs/2611.26885)
*Boris Cuevas, Basti\'an Reinoso, Andr\'es Escala et al.* · `astro-ph.GA` · arXiv:2611.26885v1 · relevance 0.18

- **In one sentence**: Coupled N-body and SPH simulations (via AMUSE, with BRIDGE gravitational coupling) of 48 dense, gas-embedded Plummer star clusters test how gas fractions from 0% to 20% change runaway stellar collisions and the resulting seed black hole mass and core collapse time.
- **In plain words**: Supermassive black holes, some billions of times the Sun's mass, already existed when the universe was young, and it is unclear how they formed. This paper simulates tightly packed star clusters that contain some gas, and asks whether the gas helps stars merge into one large object that could become a black hole seed. The authors report that more gas generally produced a more massive resulting black hole, with the core collapsing sooner.
- **Why it matters**: It offers a computer-model check on one proposed route to the early black holes seen in distant quasars, which is a open question in astronomy. The text does not show how strongly these simulated trends would hold in real clusters, so the link to actual observations remains uncertain.
- **Background needed**: - Supermassive black holes (SMBHs): black holes with millions to billions of solar masses, found at the centres of galaxies.
- Seed black hole: the first, much smaller black hole that later grows into an SMBH.
- Active galactic nuclei (AGN): very bright centres of galaxies powered by matter falling onto a black hole; seen at high redshift, i.e. when the universe was young.
- Star cluster core collapse: the dense central region of a cluster shrinks under its own gravity, speeding up collisions between stars.
- N-body simulation: a computer model that tracks the gravitational pull between many individual bodies.
- SPH (smoothed particle hydrodynamics): a method that represents gas as many particles.
- Plummer distribution: a standard mathematical model of a spherical star cluster's density profile.
- Gas fraction: the share of the cluster's total mass that is gas.
- Dynamical friction: energy loss by moving bodies as they drag through a surrounding medium; the text notes it is not fully resolved in the simulations. · level: research-level

<details><summary>Original abstract</summary>

The origin of supermassive black holes (SMBHs) remains unclear, despite observational evidence for their rapid formation in the early Universe, as evidenced by active galactic nuclei (AGN) at high redshift. In this paper, we investigate stellar dynamics in dense, gas-embedded clusters. We explore how gas influences the runaway collision process and the subsequent formation of SMBH seeds in a global instability scenario. We perform a series of coupled N-body and SPH simulations using the AMUSE framework, with the stellar and gaseous components interacting gravitationally via the BRIDGE method. We use 12 initial condition models with equal-mass stars following Plummer distributions, with total masses ranging from $10^3$ to $5 \times 10^5~M_{\odot}$, virial radii from $0.005$ to $0.1$ pc, and stellar masses of $1$, $10$ and $50$ $M_{\odot}$. For each model, we perform four simulations with gas fractions ranging from 0\% to 20\%, resulting in a total of 48 simulations. The gas is sampled with the same spatial distribution as the stars, with a mass ratio per particle of $m_{\rm SPH}/m = 0.01$, where $m$ is the stellar mass. We find that in most of our simulations, higher gas fractions lead to the formation of more massive black hole, as the core collapses earlier, triggering collisions through gas--star interactions. Our results show increases in BH mass of $\sim 8\%$ for low gas fractions, to $\sim 44\%$ at 20\% gas fraction. The core collapse time is also shortened, with the strongest reduction at $20\%$ gas fraction ($\sim 27\%$). The transonic regime of our initial conditions is where dynamical friction is most efficient in principle. Although our simulations do not fully resolve this effect, gas--star interactions are the principal mechanism driving the enhancement in BH formation efficiency, in the absence of other dissipation mechanisms.

</details>

### [An early interaction between the Sagittarius dwarf and the Milky Way I: Fossil signatures in the phase-space structure of the disc](https://arxiv.org/abs/2611.27898)
*Payel Das, Jason A. S. Hunt* · `astro-ph.GA` · arXiv:2611.27898v1 · relevance 0.14

- **In one sentence**: Four N-body plus hydrodynamic simulations (one isolated Milky-Way-like host, three with a Sagittarius-like satellite on a polar orbit) test how an early disc crossing heats and thickens the age-resolved thin disc, and compare the resulting dispersion jump with Milky Way observations.
- **In plain words**: About 5 to 7 billion years ago, the Sagittarius dwarf galaxy is thought to have passed through our Milky Way's disc. This paper runs computer simulations of that passage to see whether it left a lasting, datable mark on the up-and-down structure of the disc's stars. The authors report that stars already present during the passage were puffed up and made to move up and down faster, while stars born later were unaffected.
- **Why it matters**: If the signature holds, the vertical structure of stars of different ages could serve as a clock for when a past satellite encounter happened. The authors' best-matching model is tied to the Milky Way's outer low-alpha disc, but they note that converting the observed jump into a perturber mass is only accurate to about a factor of 1.5, so the link to the real galaxy remains approximate.
- **Background needed**: - Galaxies are made of stars, gas and dark matter; the Milky Way's disc is a thin, flat rotating layer of stars.
- N-body simulations model gravitating particles over time; hydro adds gas dynamics. They are used as controlled experiments.
- Sagittarius dwarf: a small satellite galaxy being absorbed by the Milky Way.
- Pericentre: the closest point of an orbit to the host's centre.
- Polar orbit: an orbit passing over the host's poles, so it crosses the disc plane.
- Velocity dispersion: the spread of stellar velocities; a larger value means stars are "hotter" (more agitated). Vertical dispersion refers to up-and-down motion.
- Age-velocity dispersion relation: how the velocity spread of stars changes with their age, which records heating over time.
- Alpha abundance: a chemical measure used to separate older, alpha-rich stars from younger, alpha-poor ones.
- Mass-enclosed height: the vertical distance above the disc plane within which a set fraction of a stellar population's mass lies. · level: research-level

<details><summary>Original abstract</summary>

Several independent lines of evidence point to an early encounter between the Milky Way and the Sagittarius dwarf galaxy $5$-$7$ Gyr ago. We present four controlled $N$-body+hydro simulations, one of an isolated host galaxy and three of a single interaction between a Milky-Way-like host and a Sagittarius-like satellite on an unbound polar orbit. Relative to the fiducial satellite (with total mass $0.7\times10^{11}$ M$_\odot$), one run increases the satellite's mass by a factor of $1.5$ and another its crossing speed by a factor of $1.4$, giving pericentric speeds of $466$-$634$ km s$^{-1}$ at pericentric radii of $R\simeq15$-$18$ kpc. Comparing the present-day, phase-space structure in radial bins by age of newly-formed thin-disc stars across the runs, we find that stars that existed at the time of the passage are thickened by up to $\sim37$ per cent in mass-enclosed height and heated by up to $\sim5$ km s$^{-1}$ in vertical velocity dispersion relative to the control, while stars formed after the passage are unaffected. The heating signature is also evident when comparing the age-vertical velocity dispersion relation against a heating relation with a power law of $0.38$, obtained by fitting the isolated host. A single, disc crossing from an early interaction thus suffices to leave lasting, datable fossils in the age-resolved vertical structure of a galactic disc. The fiducial run's dispersion jump of $\sim4$ km s$^{-1}$ matches best with that observed in the outer low-$\alpha$ disc of the Milky Way (Das et al. 2024), corresponding to a perturber mass of $0.7\times10^{11}$ M$_\odot$, with a velocity of $466$ km s$^{-1}$ at a pericentric radius of $16.7$ kpc, though the inversion from jump amplitude to perturber mass is good only to a factor of $\sim1.5$.

</details>

## Exoplanets and planetary science

### [Hints of planet formation in progress around DR Tau from observations with LBT SHARK-NIR and SHARK-VIS](https://arxiv.org/abs/2611.27643)
*D. Mesa, G. Li Causi, R. Gratton et al.* · `astro-ph.EP` · arXiv:2611.27643v1 · relevance 0.14

- **In one sentence**: High-contrast narrow-band imaging of the DR Tau protoplanetary disk with LBT SHARK-VIS and SHARK-NIR searches for accreting embedded companions via H-alpha and Pa-beta emission, finding two compact features that are likely reflected starlight rather than confirmed accretion.
- **In plain words**: Young stars are surrounded by disks of gas and dust where planets may be forming. This paper looks for a hidden baby planet in the disk around the young star DR Tau by searching for the faint glow of gas falling onto it. The team found two small features that persist over seven years and may fit a planet of a few Jupiter masses, but the glow they hoped to see was not detected, so they think the light is probably starlight bouncing off dust.
- **Why it matters**: Directly imaging planets still forming inside their disks is rare, so any candidate matters for understanding how planets form. The result is tentative: the features are consistent with a planet but the accretion signal needed to confirm one was not found, so it is best read as a candidate that needs follow-up.
- **Background needed**: - Protoplanetary disk: a rotating disk of gas and dust around a young star, where planets form.
- Sub-stellar object: a body too small to be a star, such as a planet or brown dwarf.
- Accretion: material falling onto a young object, which can emit specific light (here H-alpha and Pa-beta, hydrogen emission lines in visible and near-infrared light).
- Narrow-band imaging: taking pictures through very narrow color filters to isolate one emission line.
- High-contrast imaging: techniques for seeing a faint object close to a very bright star.
- Signal-to-noise ratio (S/N): how strong a signal is compared with background noise; values of 6 to 13 are modest.
- Keplerian rotation: orbital motion expected from gravity around a central star; the observed motion matches this.
- MJup: Jupiter masses, the unit for planet mass. · level: research-level

<details><summary>Original abstract</summary>

Protoplanetary disks are the primary sites of planet formation. However, the direct imaging of protoplanets still embedded within their parental disks remains a significant challenge, with only a small number of confirmed detections to date and several candidates awaiting verification. We search for embedded planets in the protoplanetary disk of the young star DRTau by targeting accretion signatures from forming sub-stellar objects. Using narrow-band imaging, we observe both visible Halpha and near-infrared Paschen-beta (Pabeta) emission to identify actively accreting companions. To this end, we performed high-contrast observations of DRTau using the SHARK-VIS (0.40-0.95 micron) and SHARK-NIR (0.96-1.70 micron) imagers at the LBT. The study uses a combination of narrow-band filters to isolate accretion signatures and broad-band filters for multi-wavelength characterization in both the visible and near-infrared. Our observations recover the primary disk structures previously identified in the literature, albeit at low signal-to-noise (S/N). We identify two compact features with S/N between 6 and 13 in both narrow- and broad-band filters. The first, an elongated structure, matches previous SPHERE detections, while the second, more compact feature, is now confirmed despite its low S/N in earlier datasets. A comparison over a seven-year baseline confirms the stability of both structures. Their observed orbital motion is consistent with Keplerian rotation, potentially suggesting the presence of an undetected planetary-mass companion (few MJup) at the location of the second feature. However, our analysis does not confirm Halpha or Pabeta emission originating from localized accretion. Instead, we conclude that the observed flux is likely stellar light reflected by dust at these locations and discuss alternative mechanisms that could account for such detections.

</details>

### [2026 QQ8: Earth's temporary flyby of maximum lunation](https://arxiv.org/abs/2611.27770)
*Grigori Fedorets, Marco Micheli, Samantha Hemmelgarn et al.* · `astro-ph.EP` · arXiv:2611.27770v1 · relevance 0.09

- **In one sentence**: Astrometric, photometric and dynamical study of asteroid 2026 QQ8, a natural temporary Earth companion on a long-duration flyby orbit near the theoretical maximum-lunation limit, with solar radiation pressure used to rule out an artificial origin.
- **In plain words**: Sometimes an asteroid drifts close enough to Earth that our planet's gravity briefly holds it, so it orbits Earth for a while before escaping back to the Sun. This paper examines a newly found example, asteroid 2026 QQ8, and checks whether it is a natural rock or a piece of human hardware. The authors measured how sunlight pushes on it, and its colour and brightness, and concluded it is natural.
- **Why it matters**: Only a few such temporary companions are known, and this one is the first long-duration example, with an orbit close to the theoretical upper limit on how long Earth can hold such an object. Its observed orbit is therefore a useful test of models of Earth-Moon capture, though the abstract does not go further into implications.
- **Background needed**: - Temporary capture: a small body is pulled into orbit around Earth for a time, then leaves; it is not a moon in the usual sense.
- Astrometry: precise measurement of an object's position over time, used to work out its orbit.
- Photometry and spectrophotometry: measuring brightness and colour across wavelengths, which hints at what a surface is made of. An S-type asteroid is a stony, silicate-rich class.
- Solar radiation pressure: the small push sunlight exerts on an object; its size depends on shape and mass, so it helps distinguish a natural rock from a manufactured object.
- Lunation: a lunar cycle; the "orbit of maximum lunation" is the orbit that stays bound to Earth for the longest possible time.
- Earth-Moon system: the combined gravitational setting in which capture happens. · level: intermediate

<details><summary>Original abstract</summary>

Aims: On a rare occasion, asteroids are temporarily captured by the Earth to become the planet's interim companions. The discovery of asteroid 2026~QQ$_8$ provided an opportunity to study this class of objects, adding to the sparse discovery catalogue of Earth's temporary companions. Methods: We performed astrometric, photometric, and dynamical studies of 2026~QQ$_8$, and measured its solar radiation pressure signal to discern between a natural and an artificial origin. Results: We find 2026 QQ$_8$ to be of natural origin, with solar radiation pressure signal commensurable with natural objects and spectrophotometry of an S-type object. 2026 QQ$_8$ is Earth's third discovered otemporarily-captured companion on a flyby orbit, and the first long-duration one, owing this to being on the so-called "orbit of maximum lunation". Its unusual orbit lies close to the theoretical upper duration limit of an object captured in the Earth-Moon system, and has now been observed for the first time.

</details>

## High-energy astrophysics

### [Modelling scintillation in Fast Radio Bursts](https://arxiv.org/abs/2611.27527)
*L. Nicotera, T. Sprenger, O. Wucknitz et al.* · `astro-ph.HE` · arXiv:2611.27527v1 · relevance 0.17

- **In one sentence**: Simulation study of how reliably the scintillation bandwidth (ν_s) can be recovered from frequency autocorrelation functions of FRB spectra when only a few scintles fit in the observing band, including averaging ACFs, a finite scintle error prescription (with η = 0.055 proposed for FRBs), and a test on Effelsberg UBB data from FRB 20240114A.
- **In plain words**: Fast radio bursts are very brief, very bright flashes of radio waves from distant galaxies. As these signals travel through clouds of ionised gas, they pick up a pattern of bright and dim patches across radio frequency, a bit like shimmering light through water. This paper uses computer simulations to ask how accurately the typical width of those patches can be measured when the receiver's frequency window only covers a few of them, and tests the approach on a real repeating burst.
- **Why it matters**: The width of these scintillation patches tells us about the scattering material along the line of sight, so measuring it reliably matters for interpreting FRB environments. The text reports that individual measurements become noisy when few patches fit in the band, and that averaging several measurements helps; the broader implications beyond this framework are not established in the text.
- **Background needed**: - FRBs: millisecond radio flashes from outside the Milky Way; some repeat.
- Scintillation: brightness variations caused by turbulence in ionised gas, similar to twinkling stars.
- Scintle: one bright patch in the frequency spectrum of a burst.
- Scintillation bandwidth (ν_s): the typical frequency width of a scintle; it relates to how much the signal is scattered.
- Autocorrelation function (ACF): a measure of how similar a spectrum is to a shifted copy of itself; its width gives ν_s.
- Lorentzian profile: the expected bell-like shape of an ACF peak.
- Finite scintle error (FSE): an empirical formula estimating the uncertainty of ν_s when few scintles are present.
- Bootstrap resampling: a statistical method that estimates uncertainty by repeatedly resampling the data. · level: research-level

<details><summary>Original abstract</summary>

Fast Radio Bursts (FRBs) are bright, ms-duration, extragalactic radio transients. Propagation through inhomogeneities in the ionised medium produces scintillation, observed as frequency-dependent intensity variations in their spectra, with bright patches, called scintles. The characteristic scintillation bandwidth probes scattering material along the line of sight. Measuring this scale can be challenging when the observing bandwidth of the burst spectra contains a few scintles. We study the uncertainties associated with recovering $\nu_s$ from frequency autocorrelation functions (ACFs) under finite-bandwidth conditions. We examine the recovery of $\nu_s$ from individual ACFs and investigate if averaging multiple independent ACFs provides a more robust measurement. Using simulations, we reproduce observational conditions to investigate the modelling of scintillation in ACFs and the associated measurement uncertainties. We use these simulations to test the finite scintle error (FSE) prescription and assess its applicability to real observations. We test the resulting modelling framework on Effelsberg Ultra Broad Band receiver observations of the repeating FRB 20240114A. As the number of scintles decreases, individual ACFs develop fluctuations that deviate from the expected Lorentzian profile. This results in increased scatter in the recovered $\nu_s$ and a less reliable FSE prescription. Averaging multiple independent ACFs mitigates these effects and improves the recovery of $\nu_s$ in the low-scintle regime. Our results provide a framework for ACF modelling and uncertainty estimation in FRBs. For individual bursts, the FSE is effective with sufficient scintles; we find $\eta = 0.055$ more suitable for FRB analysis and update the FSE accordingly. For repeaters, averaging multiple ACFs and bootstrap resampling improve the recovery and uncertainty estimation of $\nu_s$.

</details>

### [From Binary Wind to Radio Burst: Dispersion-Measure Evolution after Accretion-induced Collapse](https://arxiv.org/abs/2611.26696)
*Smadar Naoz, Victoria M. Kaspi* · `astro-ph.HE` · arXiv:2611.26696v1 · relevance 0.13

- **In one sentence**: An angle-dependent toy model of aspherical accretion-induced white-dwarf collapse ejecta expanding through a binary-driven wind bubble, tracking how the dispersion measure of repeating fast radio bursts evolves with time in diffuse versus dense, neutral versus ionized surroundings.
- **In plain words**: Some repeating fast radio bursts (brief, intense flashes of radio waves from distant galaxies) show their "dispersion measure," a measure of how much charged gas the signal passes through, slowly changing over years. This paper models a possible cause: a white dwarf star collapsing into a neutron star, with its debris blasting through gas that a companion star had previously shaped into bubbles and shells. The authors find that, when the surrounding gas starts out neutral, the shock can ionize it and make the dispersion measure rise after roughly 10 to 20 years, while ionized surroundings tend to make it fall or level off.
- **Why it matters**: Measured trends in repeaters' dispersion measure have both signs, and this work offers one physical mechanism that can produce either, suggesting that the sign and size of these trends could help tell source models apart. It is a toy model with idealized assumptions, so its relevance to real sources is not established by the text.
- **Background needed**: - Fast radio bursts (FRBs): millisecond radio flashes from distant galaxies; repeating ones are a subset.
- Dispersion measure (DM): a count of free electrons along the line of sight; lower-frequency radio arrives later, and the delay gives DM.
- Secular DM variation: a slow, multi-year drift in DM, which hints at changing gas near the source.
- White dwarf: the dense remnant of a Sun-like star. Accretion-induced collapse (AIC): a white dwarf that gains mass from a companion and collapses into a neutron star.
- Ejecta, shock, and ionization: material thrown out by the collapse pushes on surrounding gas, creating a shock wave that can strip electrons from atoms, adding charged particles.
- Toy model: a simplified, idealized calculation meant to show qualitative behavior rather than fit specific objects. · level: research-level

<details><summary>Original abstract</summary>

Secular changes in the dispersion measures (DMs) of repeating fast radio bursts probe the source-local plasma. Such DM time variability has been interpreted with spherical, single-density-profile models. Accretion-induced collapse (AIC) of a white dwarf may instead follow binary interaction and occur inside a finite, anisotropic circumstellar structure. Here, we construct an angle-dependent toy model of aspherical AIC ejecta propagating through a pre-AIC free wind, shocked-wind bubble, swept-up external shell, and polar cavity, exploring a diffuse environment (number density of $1~{\rm cm^{-3}}$, located at $10~$pc) and a compact cloud (number density of $500~{\rm cm^{-3}}$, located at $0.3~$pc), bracketing ionized and initially neutral upstream gas. The unshocked ejecta initially yield ${\rm DM}\propto t^{-2}$, while crossings of the finite wind-bubble interfaces produce breaks and curvature in ${\rm DM}(t)$. In initially neutral models, shock ionization can overcome geometric dilution: the total DM reverses from decline to growth after approximately $10$--$20$ yr and later turns over as the finite reservoir is processed. Ionized-upstream models instead generally decline or flatten. Without fitting individual sources, our models span both signs and the approximate magnitudes of the secular DM-variation rates measured among repeaters. In this dynamical framework, DM evolution is set by shock propagation through the circumsource density and ionization structure, rather than the contemporaneous burst rate, distinguishing it from photoionization-driven scenarios. Consequently, in our model, an instantaneous \(d{\rm DM}/dt\) is not a unique indicator of source age. We suggest that the observed distribution of secular DM variation slope amplitudes and signs will be important for distinguishing among different models of DM variations in repeating FRBs.

</details>

## Stars and the Sun

### [Characterisation of B-type stars in four young Galactic open clusters. II. Photometric variability with TESS and identification of pulsating stars](https://arxiv.org/abs/2611.27680)
*Federica Nardini, Dominic M. Bowman, Julia Bodensteiner et al.* · `astro-ph.SR` · arXiv:2611.27680v1 · relevance 0.14

- **In one sentence**: Photometric study with TESS full-frame images of 82 B-type stars in five young Galactic open clusters (h and chi Persei, NGC 457, NGC 581, NGC 1960), classifying pulsators and testing how pulsations and binarity relate.
- **In plain words**: This paper looks at hot, massive young stars grouped together in star clusters about 15 to 30 million years old. The authors used images from NASA's TESS satellite, which records how stars brighten and dim over time, to extract light curves for 63 of 82 stars. Most of these stars show brightness changes caused by internal pulsations, and the team sorts them into pulsator types.</plain>
<parameter name="why">Pulsations inside massive stars affect their structure and evolution, so a clear census of which stars pulsate helps test models of them. The paper also reports that pulsations do not seem to hide most close companion stars from spectroscopic detection, with an exception for Be stars, which may need a higher velocity threshold; the wider significance of this is not established by the text alone.</plain>
<parameter name="background">- Open clusters: groups of stars born together from the same cloud, so they share roughly the same age and composition.
- B-type stars: hot, massive, blue-white stars; a few million to tens of millions of years of life.
- Pulsation: a star's surface swelling and shrinking periodically, seen as regular brightness changes.
- Beta Cephei stars: a class of B-type pulsators with fairly short pulsation periods.
- Be stars: B-type stars that show emission lines from a surrounding gas disc, often rapidly rotating.
- Light curve: a record of a star's brightness over time.
- Binary detection: companions are often found by measuring a star's radial velocity (motion toward or away from us) shifting over time; a threshold of about 20 km/s is the typical cutoff used.
- TESS: a space telescope surveying most of the sky for brightness changes.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Pulsations and binarity are important properties of massive stars and influence their structure and evolution. Young open clusters are ideal laboratories to study massive stars, since they are mostly coeval and chemically homogeneous. We analyse 82 B-type stars in the Galactic open clusters $h$ and $\chi$ Persei, NGC 457, NGC 581, and NGC 1960, which have ages between 15 and 30 Myr. We extract light curves using both simple aperture photometry and a point-spread-function-based method that minimises contamination from crowded fields in full-frame images from the Transiting Exoplanet Survey Satellite (TESS) mission. We successfully extract light curves for 63 stars. The majority have photometric variability caused by pulsations, showing how pulsations are a common property of young B-type stars in clusters. We classify stars into different pulsator types based on their spectral type and frequency spectrum. The most common pulsator class are beta Cephei stars, with 29 stars in total, and we discover pulsation modes in almost all stars with a spectral type of B2 or earlier. All Be stars show pulsations, which supports the consensus of the ubiquity of pulsations in these stars. Finally, we confirm that the majority of early B-type stars are in binary systems, except for two pulsating Be stars and a star with rotational modulation. This indicates that pulsations do not significantly bias the spectroscopic detection of short-period binaries, except for Be stars where the spectroscopic radial velocity variability threshold should be higher than the typical value of 20 km s$^{-1}$.

</details>

### [Accretor Luminosity as Probe of Orbital Evolution and Magnetic Braking in AM CVn Binaries](https://arxiv.org/abs/2611.26973)
*Tin Long Sunny Wong, Peter Scherbak, Jim Fuller* · `astro-ph.SR` · arXiv:2611.26973v1 · relevance 0.05

- **In one sentence**: Models of AM CVn binaries show that the cooling luminosity of the accreting white dwarf, compared with observations, requires extra orbital angular momentum loss from magnetic braking of the donor, and that the Rappaport et al. 1983 and boosted Matt et al. 2015 prescriptions fit the data while the CARB formalism does not.
- **In plain words**: AM CVn binaries are pairs of stars so close together that a white dwarf (a dense, burnt-out star) steals helium-rich material from a companion, and their orbits slowly shrink or widen over time. The authors use how bright the white dwarf appears, since it reflects how hot and young it is, as a clock for that orbital change. They find that the observed brightness is best matched when the donor star loses extra spin by magnetic braking, but only if the standard formulas are scaled up by a large factor.
- **Why it matters**: The white dwarf's brightness gives a way to test how these binaries lose orbital energy, which is hard to measure directly. The paper also suggests that the widely used CARB braking formula is in tension with the data, and it motivates UV spectroscopy and new white dwarf atmosphere models; how well these conclusions hold depends on the modelling assumptions, which the summary text does not detail.
- **Background needed**: - AM CVn binaries: very compact systems (orbits under about 70 minutes) where a white dwarf accretes helium-rich matter from a small companion.
- Orbital period: the time for the two stars to complete one orbit; it changes as angular momentum is lost.
- Gravitational wave emission: the energy loss from orbiting masses that shrinks the orbit; it is the baseline model here.
- Magnetic braking: loss of angular momentum from a magnetised, wind-emitting star, which slows its spin and drags the orbit; several formulas exist (Rappaport 1983, Matt 2015, CARB).
- Accretor luminosity: the brightness of the accreting white dwarf, which depends on how much it has been heated by accretion and how long it has been cooling.
- Formation channels: the paper compares three evolutionary routes (white dwarf donor, helium star donor, evolved cataclysmic variable). · level: research-level

<details><summary>Original abstract</summary>

AM CVn binaries are ultracompact systems with orbital periods $P_{\rm orb} \lesssim 70$ min, where a white dwarf accretes from a He-rich semidegenerate donor. At short orbital periods ($P_{\rm orb} \lesssim 20$ min), rapid accretion reheats the accretor. As the system widens and the mass transfer rate decreases, the accretor follows standard white dwarf cooling at longer orbital periods ($P_{\rm orb} \gtrsim 30$ min). The accretor cooling luminosity then acts as a powerful probe into the orbital evolution of the binary. Recent observations show that the accretor appears brighter (younger) at long orbital periods, compared to models where orbital angular momentum loss is solely set by gravitational wave emission. We show that additional angular momentum loss, which we ascribe to magnetic braking of the donor, can better reproduce observations of accretor luminosity. We test and constrain various proposed magnetic braking formalisms, for the white dwarf, helium star, and evolved cataclysmic variable (CV) channels for AM CVn formation. None of the magnetic braking formalisms in their original form can reproduce the observations, but the widely popular magnetic braking proposed by Rappaport et al. 1983 boosted by a factor $\approx 5$, or the saturated magnetic braking proposed by Matt et al. 2015 boosted by a factor of $\approx 150$, yields satisfactory results. We also find that the CARB formalism, recently applied to the evolved CV channel, is strongly in tension with observations of accretor luminosity. Our models motivate UV spectroscopy observations, and dedicated WD atmosphere models for AM CVn accretors.

</details>

## Chemical physics

### [Molecular structure breaks universality in screening behavior of electrolyte solutions](https://arxiv.org/abs/2611.27955)
*Anna T. Bui, Connie J. Fairchild, Dominic P. W. Thomas et al.* · `cond-mat.stat-mech` · arXiv:2611.27955v1 · relevance 0.13

- **In one sentence**: Using machine-learned classical density functional theory, the authors compute decay lengths for screening in electrolyte models of increasing molecular detail and argue that solvent and ion structure break the apparent universal scaling of screening lengths in concentrated electrolytes.
- **In plain words**: Salt water carries electric charge, and its ions shield each other's electric pull over a certain distance, called the screening length. In dilute salt water this is well described by a single classic theory, but experiments on concentrated salts have suggested that the screening length follows one universal pattern regardless of the salt. This paper tests that idea with detailed computer models of different solvents and ions, and finds that the molecular details change the screening behavior, so no single pattern fits all of them.
- **Why it matters**: The result bears on an active debate about whether concentrated electrolytes are "underscreened" compared with classic theory, which matters for batteries and other charged-fluid technologies. The text does not show how the findings bear on the experiments beyond stating that they challenge equilibrium interpretations of the observed universality.
- **Background needed**: - Electrolyte: a liquid containing dissolved charged particles (ions), such as salt in water.
- Screening length: the distance over which a charge's electric field is weakened by surrounding ions; a shorter length means stronger screening.
- Debye–Hückel theory: the classic, simple theory of screening that works well for dilute solutions.
- Underscreening: the observation that concentrated electrolytes screen charge less effectively than the classic theory predicts.
- Classical density functional theory: a statistical-physics method that computes how particle densities arrange themselves near charges, here accelerated with machine learning.
- Decay mode and re-entrant behavior: ways the screening correlation falls off with distance (monotonically, or non-monotonically with changing concentration).
- Universality/scaling law: the idea that different systems collapse onto one curve when plotted in suitable units. · level: research-level

<details><summary>Original abstract</summary>

Electrostatic screening is one of the most fundamental phenomena in electrolyte solutions. While dilute electrolytes are described by the universal Debye--H\"uckel theory, recent experiments have reported an apparently universal scaling law for screening lengths in concentrated electrolytes, fueling ongoing debate over anomalous underscreening. Yet, liquid state theory has been unable to determine whether molecular details of the solvent, the ions, or both should preserve or break such universality. Using machine-learned classical density functional theory, we compute numerically exact decay lengths across a hierarchy of electrolyte models of increasing molecular complexity. We find that molecular details qualitatively reshape screening: solvent attraction generates a new monotonic decay mode, solvent polarity produces re-entrant behavior, and ionic structure alone can drastically alter screening-length exponents. Consequently, no single scaling law describes screening universally across these molecularly distinct electrolytes. Our results challenge equilibrium interpretations of experimentally observed universality in concentrated electrolytes.

</details>

### [Length and Sequence-Dependent Dipolar and Electronic Properties of $\alpha$-helical Polypeptides](https://arxiv.org/abs/2611.26892)
*Faezeh Shabani, Florian G\"unther, Sibylle Gemming* · `physics.chem-ph` · arXiv:2611.26892v1 · relevance 0.05

- **In one sentence**: Density-functional tight-binding calculations of how chain length, sequence, side-chain and terminal chemistry, and external electric fields shape the dipole moment and frontier orbital energies of three alpha-helical polypeptide families.
- **In plain words**: This paper is a computer simulation study of short protein-like chains that curl into helices, similar to the backbone of many natural proteins. The authors asked how making the chain longer, swapping amino acids, or applying an electric field changes the molecule's electrical polarity and its electronic energy levels. They report that longer helices gain a larger overall dipole, that the backbone carbonyl groups (C=O) drive most of this effect, and that electric fields mainly distort the flexible ends rather than the helix core.
- **Why it matters**: Understanding how helix length and sequence set electronic behavior could inform the design of peptide-based materials for bio-electronic interfaces, biosensors, and artificial electron-transfer systems. The text frames these as possible applications; it does not test any device, so the link to practical use is speculative.
- **Background needed**: - Alpha-helix: a spiral backbone shape common in proteins, held together by hydrogen bonds between nearby residues.
- Polypeptide: a chain of amino acids linked together; here, short model chains of alanine (A), leucine (L), lysine (K), with a cysteine (C) cap.
- Molecular dipole: a separation of positive and negative charge in a molecule, behaving like a tiny built-in arrow; it adds up along aligned bonds.
- Frontier orbitals (HOMO/LUMO): the highest occupied and lowest unoccupied electronic energy levels; their gap governs how a molecule absorbs light and transfers electrons.
- Density-functional tight-binding (DFTB): a fast approximate quantum-chemistry method for modeling molecules, less rigorous than full quantum calculations.
- Stark effect: shifting of energy levels by an electric field.
- Results come only from simulation; no experiments are described in the text. · level: research-level

<details><summary>Original abstract</summary>

Helical polypeptides combine the chemical tunability of synthetic macromolecules with the highly ordered backbone architecture of natural proteins. Here, density-functional tight-binding calculations are used to determine how chain length and sequence chemistry govern the dipolar and electronic properties of three $\alpha$-helical polypeptide families: polyalanine [AAAAA]$_n$, leucine-modified [AAAAL]$_n$, and cysteine-capped, lysine-containing C[AAAAK]$_n$. Increasing chain length produces systematic shifts and splitting of the molecular orbital levels together with an approximately additive increase in the molecular dipole. Analysis of the C[AAAAK]$_3$ helix shows that aligned backbone carbonyl groups provide the dominant contribution to the macro dipole, whose growing electrostatic potential is consistent with an intrinsic Stark-like contribution to the length-dependent orbital-energy evolution. Side-chain and terminal modifications introduce localized perturbations to frontier electronic states while preserving this global backbone-driven trend. Residue-resolved frontier levels additionally form a staircase-like energy landscape along the helical scaffold: individual peptide units retain large local HOMO-LUMO gaps of approximately 5 eV, whereas spatially proximate hydrogen-bonded residues exhibit smaller inter-residue energy separations. Application of external electrostatic fields modifies the frontier-level separation in a direction-dependent manner and induces structural distortions predominantly near the flexible termini, while the helical core remains comparatively robust. By establishing these fundamental sequence-structure-property relationships, this work provides a foundational blueprint for the rational design of peptide-based biomacromolecules tailored for next-generation bio-electronic interfaces, biosensors, and artificial electron-transfer systems.

</details>

## Materials science

### [Designing Perovskites for Chemical Looping Hydrogen Production](https://arxiv.org/abs/2611.27580)
*Ivana Stani\v{c}i\'c, Alfred Juhlin Onbeck, Anders Hellman et al.* · `cond-mat.mtrl-sci` · arXiv:2611.27580v1 · relevance 0.10

- **In one sentence**: An autonomous active-learning loop (Wasserstein autoencoder plus deep-ensemble surrogate) searched perovskite compositions for hydrogen production capacity in chemical looping, raising the mean capacity of acquired candidates from 0.41 to 2.05 mmol H2/g over 50 cycles and then ranking 20 candidates by cost, supply and environmental criteria.
- **In plain words**: This paper is about finding better solid materials for making hydrogen in a cyclic chemical process, where a metal-oxide-type solid is repeatedly reduced and reoxidized to release hydrogen from steam. Because there are a huge number of possible mixtures of elements, the authors used a computer program that repeatedly proposed new mixtures, learned from the results, and proposed better ones. The search raised the average hydrogen yield of the proposed materials substantially and produced 20 candidates that also account for raw-material price, supply and health or environmental concerns.
- **Why it matters**: Hydrogen production is a major industrial and energy topic, and this shows a way to narrow a very large materials search with machine learning while also weighing practical costs. The text reports computational results only, with no experimental validation shown in the excerpt, so the candidates remain predictions; its broader transfer to other processes is stated by the authors but not demonstrated here.
- **Background needed**: - Perovskites: a family of crystal structures with the general formula ABO3, where different metal elements can be swapped into the A and B sites.
- Chemical looping: a cycle in which a solid oxygen carrier is reduced and then reoxidized, used here to produce hydrogen from water.
- Hydrogen production capacity (HPC): the amount of hydrogen produced per gram of material, in mmol/g.
- B-site / A-site: the two positions in the perovskite structure where different metal atoms can sit.
- Active learning: a loop in which a model chooses which experiments or calculations to run next, then updates itself with the results.
- Autoencoder: a neural network that compresses data into a smaller set of numbers and reconstructs it; a Wasserstein autoencoder is a variant with a particular training rule.
- Deep ensemble surrogate: many neural networks trained together to predict results quickly and estimate uncertainty.
- Multi-objective ranking: sorting candidates by several criteria at once, here performance plus cost, supply and environmental impact. · level: research-level

<details><summary>Original abstract</summary>

Perovskites are promising materials for chemical looping hydrogen production (CLHP) due to their compositional flexibility and tunable redox properties. However, cation substitution opens a vast compositional space, making screening for new high-performing materials computationally demanding. Here, an autonomous active-learning framework combining a Wasserstein autoencoder (WAE) with a deep ensemble surrogate model was used to search for perovskites with a high hydrogen production capacity (HPC). In seven independent runs of 50 cycles, the mean HPC of the acquired compositions rose from 0.41 mmol H$_2$ g$^{-1}$ in the starting set to 2.05 mmol H$_2$ g$^{-1}$, and the best compositions reached 2.65-2.99 mmol H$_2$ g$^{-1}$. All runs enriched Sn on the B-site, mostly combined with Ti and with Mg, Ce, K and Y on the A-site. Twenty diverse candidates (2.22-2.84 mmol H$_2$ g$^{-1}$) were then selected by a multi-objective ranking that also accounts for raw-material price, supply resilience and potential environmental and health impacts. The approach links materials discovery with practical deployment constraints, and the methodology is transferable to other chemical looping processes.

</details>

### [Edge-dislocation interactions with sub 3 nm vacancy and interstitial clusters in FeCr alloys: Mechanisms, Obstacle strength and Fate](https://arxiv.org/abs/2611.27583)
*Layatmika Sahoo, Suchandrima Das* · `cond-mat.mtrl-sci` · arXiv:2611.27583v1 · relevance 0.09

- **In one sentence**: Molecular dynamics simulations of an edge dislocation passing through relaxed sub-3 nm vacancy and mixed Fe-Cr interstitial clusters in Fe-3Cr, Fe-5Cr and Fe-10Cr at 300 K, quantifying obstacle strength, survival and Cr segregation, and comparing the results with dispersed-barrier hardening parameters from earlier TEM-based fits.
- **In plain words**: Metals that are exposed to radiation in reactors get harder and more brittle, and this often happens before any defects are visible in an electron microscope. This paper uses computer simulations of atoms to show how a moving line-defect in the crystal (a dislocation) interacts with tiny clusters of missing or extra atoms that are too small to see. It finds that vacancy clusters (missing atoms) are generally strong obstacles that are not destroyed when the dislocation passes, while most interstitial clusters (extra atoms) are weaker and are usually absorbed.
- **Why it matters**: Hardening models for reactor steels are usually fitted to defects that can be seen in microscopes, so the strength parameters they use may be inflated by invisible defects; this work offers a physical, atom-level basis for correcting them. The results come from simulations of idealised clusters, so their direct relevance to real irradiated materials is something the text does not establish.
- **Background needed**: - Dislocation: a line defect in a crystal whose movement lets metals deform plastically.
- Obstacle strength: how much a small feature resists a passing dislocation; often expressed through a dimensionless factor alpha in hardening models.
- Vacancy vs interstitial: a vacancy is a missing atom; an interstitial is an extra atom squeezed between regular atoms. Both can cluster after irradiation.
- Loops and platelets: small clusters that relax into flat disc-like or ring-like shapes with specific crystal orientations.
- Fe-Cr alloys: iron with chromium added, a model system for reactor steels.
- Molecular dynamics: simulating the motion of individual atoms under interatomic forces.
- TEM (transmission electron microscopy): imaging method that can only resolve defects above a certain size. · level: research-level

<details><summary>Original abstract</summary>

Fe-Cr alloys harden at irradiation doses where transmission electron microscopy (TEM) shows no defects, implicating defects too small to be resolved. Their obstacle strength is unknown, so hardening models ignore them and fit measured hardening to visible defects alone. Here, molecular dynamics drives an edge dislocation through relaxed 1-3 nm vacancy and mixed Fe-Cr interstitial clusters in Fe-3Cr, Fe-5Cr and Fe-10Cr at 300 K. Vacancy clusters relax into platelets whose strength rises with size to about 350 MPa at 2.9 nm, following strong-obstacle scaling independently of Cr content, and always survive dislocation passage. Interstitial clusters relax into $\frac{1}{2}\langle 111 \rangle$, mixed or $\langle 100 \rangle$ loops. They are mostly weaker than platelets of the same size, their strength varies up to fivefold with the local Cr arrangement, and most are absorbed. Only $\langle 100 \rangle$ loops in Fe-5Cr and Fe-10Cr often survive. During pinning, Cr collects at the junction between these loops and the dislocation; atom tracking for one loop shows that more than half comes from the loop itself. Surviving loops are not stronger than absorbed ones: strength and survival are thus distinct. Computed dispersed-barrier strengths ($\alpha \approx$ 0.02-0.25) are upper bounds that lie below the $\alpha$ values obtained in earlier studies by fitting hardening to TEM-visible loops. These earlier values are therefore inflated by TEM-invisible defects. Wherever small vacancy clusters form, they are more effective obstacles than interstitial clusters of the same size. These defect-specific strengths and fates provide a physical basis for models of low-dose hardening.

</details>

## Soft matter and polymers

### [Decoupling Entropic and Enthalpic Elasticity in Crosslinked Polymer Nanocomposites](https://arxiv.org/abs/2611.27259)
*Chiranjit Majhi, Sivasurender Chandran, Krishnacharya Khare* · `cond-mat.soft` · arXiv:2611.27259v1 · relevance 0.09

- **In one sentence**: Temperature-dependent thermomechanical measurements separate the entropic and enthalpic parts of elasticity in crosslinked PDMS nanocomposites filled with silica or titania, and find that the effective crosslink density at the particle interfaces drops sharply once particles lie closer than a critical separation.
- **In plain words**: This paper looks at rubber-like materials made of a silicone polymer with tiny particles mixed in. Stretchiness in such materials comes partly from the chains wanting to coil up (entropy) and partly from energy bonds between chains and particles (enthalpy). The authors measured how stiffness changes with temperature to tell these two parts apart, and found that the stiffening from particles is mostly entropy-driven at low particle loading but more energy-driven at high loading.
- **Why it matters**: Understanding how filler particles change the energy and entropy of rubbery networks can guide the design of tougher or more tunable elastomers. The text reports cross-checks with two particle types and with X-ray scattering on one of them, which supports the general claim, though the text does not show application-level results.
- **Background needed**: - Elastomer: a rubber-like polymer network whose chains are joined at crosslinks, letting it stretch and return.
- Crosslink density: how many joints per unit volume link the chains; more joints usually means a stiffer network.
- Entropic elasticity: stiffness that comes from polymer chains losing coiled disorder when stretched; it rises with temperature.
- Enthalpic elasticity: stiffness from energy changes in bonds and chain-particle contacts, which depends less directly on temperature.
- Nanocomposite: a material with nanometre-scale particles dispersed in a host, here silica or titania in PDMS (silicone).
- Interface region: the thin layer of polymer around each particle whose behaviour differs from the bulk.
- Volume fraction: the share of the material's volume taken up by particles.
- Linear superposition: the assumption that the total response is the sum of bulk and interface contributions. · level: research-level

<details><summary>Original abstract</summary>

Nanoparticle-induced local interface regions significantly enhance the bulk mechanical behavior of polymer nanocomposites, yet their energetic contribution in crosslinked elastomer networks remains poorly understood. Here, we decouple the entropic and enthalpic contributions to the elasticity of crosslinked poly(dimethylsiloxane) nanocomposites using temperature-dependent thermomechanical measurements. While the measured bulk elastic modulus exhibits a monotonic increase with nanoparticle volume fraction $\phi_{\rm n}$, we observe that the effective crosslink density initially increases before saturating at larger $\phi_{\rm n}$. These results are independently validated across two nanoparticle systems (silica and titania) and directly confirmed by X-ray scattering experiments on silica-based composites, highlighting the generality of the observation. The trends in effective crosslink density indicate that the elastic response is predominantly entropy-driven at low nanoparticle concentrations, whereas enthalpic contributions become increasingly significant at higher loadings. Assuming a linear superposition of interface and bulk contributions, these results reveal that the effective crosslink density at the particle interface decreases by an order of magnitude below a critical mean interparticle separation, indicating that localized particle proximity and clustering constrain the entropic elasticity at higher loadings.

</details>

### [Lacrymaria-like dynamics: compression and length change in active slender bodies](https://arxiv.org/abs/2611.27577)
*Cl\'ement Moreau, Yukinori Nishigami, Johann H\'erault et al.* · `cond-mat.soft` · arXiv:2611.27577v1 · relevance 0.07

- **In one sentence**: A planar N-link model of active filaments in which both bending angles and segment lengths evolve under resistive-force drag, used to study how axial compression couples with bending in swimming, crawling, and Lacrymaria-like neck extension.
- **In plain words**: Many tiny swimming and crawling organisms, such as the single-celled Lacrymaria olor, change their body length as well as bending it, yet most models treat their filaments as fixed-length. This paper builds a model where the filament can bend and also compress or stretch, with the surrounding fluid's drag acting on each piece. The authors report that simply making the filament stretchy usually slows it down, while prescribed waves of length change can speed up, slow down, or redirect motion depending on their timing and frequency relative to the bending.
- **Why it matters**: It matters for understanding how microorganisms move when their bodies change length, a feature most existing models ignore. The text does not show direct experimental validation or applications beyond the modelled cases, so its relevance to real organisms or to engineered micro-swimmers is a reasonable but untested connection.
- **Background needed**: - Elastohydrodynamics: how elastic bodies (like flexible filaments) deform and move in a viscous fluid where inertia is negligible.
- Resistive force theory: an approximation in which drag on each small piece of a filament depends only on its local velocity, with different drag for motion along and across the filament.
- Inextensible filament: a model assumption that the filament keeps a fixed length; here the authors relax this and allow compression and stretching.
- N-link model: the filament is approximated as a chain of N rigid segments joined by hinges, with segment lengths and joint angles as variables.
- Rest-length waves: a travelling pattern of preferred (unstrained) lengths along the body, which the model drives actively.
- Follower force: a force whose direction rotates with the body, used here to drive oscillation of clamped or free filaments.
- Lacrymaria olor: a single-celled protist with a long, extensible neck used to hunt and explore. · level: research-level

<details><summary>Original abstract</summary>

Length change is central to the behaviour of many active slender bodies, yet most elastohydrodynamic models of microscopic locomotion treat filaments as effectively inextensible. Here we introduce a compressible $N$-link formulation for planar active filaments, in which both bending angles and segment lengths are dynamical variables coupled through local hydrodynamic drag, modelled using resistive force theory. We first use the model to test whether passive extensibility can improve bending-driven swimming and crawling. Across the parameter ranges studied, passive compressibility usually reduces locomotion speed, indicating that axial compliance alone is not a robust mechanism for propulsion enhancement. We then prescribe active rest-length waves and show that compression can either enhance, suppress, or redirect locomotion depending on its phase, wavelength, and frequency relative to bending. Finally, motivated by the extensible neck dynamics of \textit{Lacrymaria olor}, we apply the method to clamped and free filaments driven by oscillatory follower forces. These examples show that elastic compression-bending coupling can reorganise swimming, exploration, and locomotion in strongly deforming active filaments.

</details>

## AI for chemistry and materials

### [Beyond the Ground State: Assessing the Machine-Learned Skala Functional in {\Delta}SCF Calculations of Molecular Excitation Energies](https://arxiv.org/abs/2611.27711)
*Egor Trushin, Thomas D. K\"uhne* · `physics.chem-ph` · arXiv:2611.27711v1 · relevance 0.18

- **In one sentence**: This paper tests whether the machine-learned Skala exchange-correlation functional, trained mainly on ground-state energetics, transfers to molecular excitation energies and singlet-triplet gaps computed with the ΔSCF approach, comparing it with PBE, r²SCAN and PBE0 under UKS and ROKS formalisms.
- **In plain words**: Computer chemists use approximate formulas, called density functionals, to estimate how molecules behave. This paper checks whether a newer formula learned from data, Skala, still works well when asked about excited molecules, meaning molecules that have absorbed light and moved an electron to a higher energy level. It compares Skala with three established formulas on several sets of test molecules.
- **Why it matters**: Skala was designed around ground-state energies, so its accuracy for excited states is a fair question for anyone hoping machine-learned functionals can replace hand-built ones in chemistry and materials design. The results are mixed: Skala does well on some excitation classes and open-shell setups but not others, so the paper supports cautious transferability rather than a general claim of superiority.
- **Background needed**: - Density functional theory (DFT): a computational method that estimates molecular energies from electron density; the exchange-correlation (XC) functional is the approximate part that controls accuracy.
- Skala: a machine-learned XC functional, here assessed beyond the ground state.
- Comparison functionals: PBE and r²SCAN (simpler/semi-local) and PBE0 (hybrid, includes exact exchange).
- ΔSCF: estimating an excited-state energy as the difference between separately converged self-consistent calculations for the excited and ground states.
- Vertical excitation energy: energy needed to lift a molecule to an excited state without changing nuclear positions.
- Singlet-triplet gap: energy difference between states where electron spins are paired versus parallel; an "inverted" gap has the triplet above the singlet, which is unusual.
- UKS vs ROKS: two ways of handling open-shell (unpaired-electron) systems in Kohn-Sham DFT.
- MAE (mean absolute error): average size of the error against reference values; lower is better.
- QUEST sets: benchmark collections of excitation energies; QUEST1 covers small molecules, QUEST6 covers intramolecular charge-transfer excitations. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

We assess the transferability of the machine-learned Skala exchange-correlation (XC) functional beyond ground-state energetics using molecular vertical excitation energies and singlet-triplet gaps calculated with the $\Delta$-self-consistent-field ($\Delta$SCF) approach. We compare Skala with PBE, r$^2$SCAN, and PBE0 on subsets covering small-molecule excitations (QUEST1), inverted singlet-triplet gaps (ST-gap), and intramolecular charge-transfer excitations (QUEST6). Both spin-unrestricted Kohn-Sham (UKS) and restricted open-shell Kohn-Sham (ROKS) formalisms are considered. On QUEST1, Skala achieves the lowest mean absolute errors (MAEs) for singlet and triplet excitation energies with both formalisms, although PBE0 and r$^2$SCAN provide more accurate singlet-triplet gaps through error cancellation. For ST-gap, Skala yields the lowest gap MAEs with both UKS and ROKS. Evaluating the mixed-spin and triplet energy components on the same orbitals optimized for the ROKS open-shell singlet yields negative splittings for seven of eight ST-gap molecules with Skala. Separate triplet optimization increases the gaps, but six remain negative. All three conventional functionals give positive common-orbital splittings and optimized gaps for all eight molecules. For QUEST6, treated with UKS only, Skala yields more accurate singlet excitation energies than PBE and r$^2$SCAN but remains less accurate than PBE0. Across QUEST1 and ST-gap, Skala yields lower MAEs with UKS than ROKS. Overall, these results support Skala's transferability to molecular excited states while highlighting its dependence on the excitation class and open-shell treatment.

</details>

### [Prediction of lattice thermal conductivity of half-Heusler compounds by machine learning and transfer-function calibration](https://arxiv.org/abs/2611.26788)
*Shivam Randive, Ojaswini Randive, Heet Lungaria et al.* · `cond-mat.mtrl-sci` · arXiv:2611.26788v1 · relevance 0.15

- **In one sentence**: The paper quantifies a systematic overestimate of lattice thermal conductivity (heat carried by atomic vibrations) for 18-valence-electron cubic half-Heusler compounds when computed values are compared with measurements on polycrystalline samples, and proposes a temperature-dependent transfer function plus a machine-learning model to correct it.
- **In plain words**: Researchers search for new materials that turn heat into electricity by first computing how well each candidate conducts heat through its crystal lattice. Those computed values describe a perfect single crystal, while lab measurements are made on real, imperfect samples that scatter heat more, so the computed numbers run high. This paper measures how large that gap is across a whole family of compounds and tries to correct for it.
- **Why it matters**: Screening studies that rank candidate materials rely on these calculated values, so a systematic bias would skew which materials look promising. The text reports that the corrected predictions match the agreement between independent labs, but it does not establish how the method performs beyond this compound class.
- **Background needed**: - Thermal conductivity: how readily a material passes heat along; the lattice part comes from atomic vibrations.
- Half-Heusler compounds: a family of cubic crystals studied for thermoelectric (heat-to-electricity) use; this paper covers those with 18 valence electrons.
- First-principles calculation: computing material properties from quantum mechanics alone, with no fitted lab data.
- Single crystal vs. polycrystal: a perfect ordered crystal versus a material made of many grains with boundaries and defects, which scatter heat.
- Transfer function: a simple correction formula mapping calculated values onto expected measured values.
- Machine-learning model: a statistical model trained on existing data to predict a property from crystal structure.
- Withheld chemistries: compounds kept out of all fitting steps to test whether the correction generalizes. · level: research-level
- Matched keywords: crystal structure

<details><summary>Original abstract</summary>

High-throughput searches for half-Heusler thermoelectrics increasingly rely on lattice thermal conductivity ($\kappa_L$) from first-principles calculations, or from machine-learning models trained on them. These calculations describe an ideal single crystal, whereas measurements are made on polycrystalline samples, in which grain boundaries and defects scatter heat as well. The resulting gap between calculated and measured $\kappa_L$ has been noted for individual compounds but not, to our knowledge, quantified across a materials class, so the values used for screening carry an unknown, systematic bias. Here we quantify and correct this bias for cubic half-Heusler compounds with 18 valence electrons. Using a curated literature corpus that keeps calculated and measured values apart, we show that calculations overestimate measured $\kappa_L$ in most bonding families, and that the excess shrinks with temperature. Scattering by defects, added to the intrinsic scattering between lattice vibrations, would give such a trend, but the data do not single out one cause. A simple transfer function with this temperature dependence removes the median offset, and refitting its magnitude within a bonding family lowers the median error further, though not consistently compound by compound. Combined with a machine-learning model that predicts the calculated value from crystal structure, and tested on chemistries withheld from all fitting, the method predicts measured $\kappa_L$ in this class about as closely as independent laboratories agree with one another, and provides testable predictions for compounds not yet measured.

</details>

## Biochemistry

### [RUBRIC: rapid quality assessment tool for RNA 3D structures](https://www.biorxiv.org/content/10.64898/2026.11.20.767675v1)
*Dewan, K. J.; Yesselman, J. D.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.20.767675 v1 · relevance 0.08

- **In one sentence**: RUBRIC is an open-source program that annotates RNA base pairs and checks their geometry, ribose sugar puckers and backbone conformations in 3D structures, including flagging geometrically ambiguous pairs.
- **In plain words**: Scientists use cryo-electron microscopy to build three-dimensional models of RNA molecules, but the checking tools have not kept up, so deposited models can contain distorted parts. This paper presents RUBRIC, a fast free program that checks the pairing, sugar shape and backbone shape of each piece of an RNA model and points out problem spots. The authors report that it analyzes a whole human ribosome in under a second and that the problems it flags tend to shrink in better or re-refined models.
- **Why it matters**: Many RNA structures in the Protein Data Bank, and the datasets used to train structure-prediction methods, may contain errors, so a quick validation tool could help improve them before they are reused. The text does not show how widely RUBRIC will be adopted, so its practical impact remains to be seen.
- **Background needed**: - RNA is a chain-like molecule; its building blocks (bases) pair up to form a folded 3D shape.
- Cryo-electron microscopy (cryo-EM): a method that images frozen molecules to reconstruct their 3D structure.
- Base pair: two RNA bases that hydrogen-bond together; Leontis-Westhof classes describe how the pair is oriented.
- Ribose pucker: the sugar ring in each RNA unit can adopt a few characteristic puckered shapes; wrong puckers signal a bad model.
- Backbone suite: the chain's local twist pattern between neighboring units, which takes known conformations.
- Torsion angles: rotation angles along bonds that define local shape.
- Protein Data Bank (PDB): the public archive where deposited 3D structures are stored.
- Model refinement: adjusting a model to better fit the experimental data and chemical rules. · level: research-level

<details><summary>Original abstract</summary>

Cryo-electron microscopy has transformed RNA structural biology, revealing increasingly large and complex structures at an unprecedented pace. However, validation methods have lagged behind, and deposited models can contain distorted base pairs, incorrect ribose puckers and backbone conformational outliers. Here, we introduce Rapid Unified Base-pair, Ribose and backbone Integrity Check (RUBRIC), an open-source program that combines RNA structural annotation with local validation of base pairs, sugars, and backbones. RUBRIC assigns Leontis-Westhof classes and identifies geometrically ambiguous pairs that cannot be confidently assigned to a single class. It scores unambiguous pairs against reference geometries for each type and class, identifying the parameters responsible for low scores. It also assigns backbone suites to known conformers, suggests target torsions for unassigned suites and flags incorrect ribose puckers. RUBRIC analyzes a complete human ribosome in under a second, with base-pair detection and classification consistent with leading annotation programs. These programs disagreed significantly more often on pairs RUBRIC flagged as ambiguous than on unambiguous pairs. The geometric problems flagged by RUBRIC were reduced in higher-resolution models of the same RNA or after refinement targeting the affected geometry, indicating that these problems are correctable. A PyMOL plug-in and machine-readable output support model building, correction before deposition and assessment of deposited structures before reuse. RUBRIC can therefore help improve RNA structures in the PDB and the datasets used to train and evaluate RNA structure prediction methods.

</details>

### [A cytochrome P450 is essential for cardenolide biosynthesis in Chrysolina beetles](https://www.biorxiv.org/content/10.64898/2026.11.19.767920v1)
*Xu, H.; Stathaki, A.; Florean, M. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.19.767920 v1 · relevance 0.06

- **In one sentence**: A cytochrome P450 enzyme from the leaf beetle Chrysolina coerulans, CcCYP9Z273, converts pregnenolone to caraumbellogenin via C14-hydroxylation, an early step in beetle cardenolide biosynthesis, with one active-site residue controlling C14 versus C15 selectivity.
- **In plain words**: Cardenolides are chemical defense compounds, found in some plants and in certain beetles, and they are also the basis of heart medicines such as digitoxin. Plants make these compounds in a well-studied way, but how insects make them was not known. This paper identifies an enzyme in a leaf beetle that performs an early step of the process, and shows that silencing the gene reduces the beetle's cardenolide production.
- **Why it matters**: It shows that beetles and plants appear to have recruited different enzyme families to build the same shared intermediate, which is a useful piece of evolutionary and biosynthetic understanding. The text does not say whether this could be used to produce medicinal cardenolides, so any such application remains speculative.
- **Background needed**: - Cardenolides: steroid-like natural compounds that act as defense chemicals and include heart drugs such as digitoxin.
- Steroid precursor: pregnenolone is a basic steroid building block that the enzyme modifies.
- Cytochrome P450: a large family of enzymes that add oxygen to molecules, often at specific carbon positions.
- Hydroxylation: adding an –OH group to a carbon atom; here at position C14 (or C15 as a competing outcome).
- Gene silencing: switching off a gene to see what happens to the organism's chemistry.
- Isotope tracing: feeding labelled molecules to track which compounds are true intermediates in a pathway.
- Biosynthetic intermediate: a compound made along the way to the final product. · level: research-level

<details><summary>Original abstract</summary>

Cardenolides are naturally occurring steroidal derivatives that function as chemical defense compounds. These natural products are also widely used in medicine, as exemplified by the use of digitoxin in treating cardiac disease. Although cardenolides are most widely known as plant-derived natural products, these compounds are also produced in certain beetle species. However, while the biosynthesis of cardenolides has been well-studied in plants, it is not known how insects produce these compounds. Here we report the identification of a cardenolide biosynthetic enzyme from the leaf beetle Chrysolina coerulans. This cytochrome P450, CcCYP9Z273, catalyzes an array of steroid oxidations, including the conversion of pregnenolone into caraumbellogenin through C14-hydroxylation. Gene silencing suggests that CcCYP9Z273 is essential for beetle cardenolide formation and isotope tracing experiments support caraumbellogenin as an on-pathway biosynthetic intermediate. Mutagenesis of CcCYP9Z273 identifies an active-site residue that controls the enzyme product selectivity between C14- and C15-hydroxylation. These findings establish an early step in beetle cardenolide biosynthesis and highlight how distinct enzyme families have been recruited in insects and plants to generate a shared intermediate in the biosynthesis of these important metabolites.

</details>

## Pharmacology and drug discovery

### [Evaluation of sources of variability in a TEER (trans-epithelial/endothelial electrical resistance) system](https://www.biorxiv.org/content/10.64898/2026.11.06.764605v1)
*Gutierrez, R.; Lund, S.; Reipa, V. et al.* · `pharmacology and toxicology` · bioRxiv doi:10.64898/2026.11.06.764605 v1 · relevance 0.03

- **In one sentence**: A case study of a chamber-based TEER (electrical resistance across cell layers) system used with a gut co-culture model, partitioning within-run versus run-to-run variability using Bayesian analysis and correlations with control inserts over 23 experiments.
- **In plain words**: Scientists grow cells in a thin layer on a porous insert and measure how electrically resistant that layer is, which shows whether it forms a tight barrier. This paper asks where the noise in those measurements comes from. The authors analyzed 23 experiments and found that differences between separate runs mattered much more than differences within a single run.
- **Why it matters**: Barrier measurements like this are used in drug testing and gut models, so knowing how much of the scatter is run-to-run noise affects how results should be analyzed and compared. The text reports that control inserts (KCl and blank) were only weakly or not correlated with the gut model values, which the authors note was unexpected; the broader lessons are presented as applicable to other TEER methods, though the text does not test that directly.
- **Background needed**: - TEER: electrical resistance measured across a cell layer; higher values generally indicate a tighter barrier.
- Inserts: small porous cups on which cells are grown, with measurements taken across the membrane.
- Co-culture / gut model: a lab model that grows more than one cell type together to imitate the intestinal lining.
- KCl and blank inserts: control measurements (a potassium chloride solution, and an insert with no cells) used to check the instrument.
- Run-to-run vs within-run variability: differences between separate measurement sessions versus differences among plates measured in one session.
- Bayesian analysis: a statistical method that estimates how much each source of variation contributes, with uncertainty.
- Correlational analysis: checks whether control deviations move together with gut model deviations. · level: intermediate

<details><summary>Original abstract</summary>

Trans-epithelial/endothelial electrical resistance (TEER) measurements are a key nondestructive measurement of the barrier integrity of cells grown on inserts. To support the use of TEER measurements in bioassays, we have evaluated the sources of variability in a case study involving a chamber-based TEER system to assess a gut co-culture model. Data from 23 separate experiments, each lasting 22 d, were evaluated. Multiple lines of evidence suggested minimal variability within a run, a period during which several plates were analyzed sequentially. In contrast, run-to-run variability was substantially larger, even when two runs were performed several hours apart on the same day. Bayesian analysis of both KCl and blank insert data revealed that run-to-run variability was among the largest sources of variability, with relative uncertainty values of 3 % to 6 % of the mean value. Correlational analysis investigated whether deviations of KCl or blank insert TEER values within a run compared to long-term median values were correlated with deviations of the biculture gut model values within that same run from their long-term median values. Unexpectedly, the KCl values were not correlated, while the blank insert values had a weak correlation. We also evaluated the information gained from different control measurements. The findings from this study can influence how statistical analyses are performed on TEER results and can inform the design of robust TEER methods. For example, the approaches described here can be used to characterize variability within and among runs in TEER measurements for other methods.

</details>

## Computational and systems biology

### [Integrating CRISPRi perturbation responses and transcription-factor binding priors for regulatory network inference in triple-negative breast cancer](https://www.biorxiv.org/content/10.64898/2026.11.20.768082v1)
*Faroque, O.; Jannaty, M. H.; Abir, S. H. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768082 v1 · relevance 0.13

- **In one sentence**: An interventional gene regulatory network framework that combines single-cell CRISPRi Perturb-seq data with ENCODE transcription-factor binding priors to infer regulators driving triple-negative breast cancer (MDA-MB-231) programs, benchmarked against GENIE3 and co-expression baselines.
- **In plain words**: Cancer cells are controlled by networks of switch-like proteins that turn genes on and off. This paper tries to map which switches control which genes in a hard-to-treat breast cancer type, by deliberately silencing genes one at a time and watching what changes, rather than only looking at which genes move together. The authors report that their method predicted held-out silencing results more accurately than two standard comparison methods and flagged several candidate master regulators.
- **Why it matters**: Triple-negative breast cancer has few drug targets, so better maps of its control circuits could point to candidate targets. The text is a computational study whose predictions still need laboratory validation, and the survival and simulation results are reported only as summary figures in the abstract, so the practical reach is uncertain.
- **Background needed**: - Gene regulatory network: a map of which regulators (transcription factors) switch which genes on or off.
- CRISPRi: a method that uses a modified CRISPR system to reduce activity of a specific gene, used here as a controlled "intervention."
- Perturb-seq: pairing CRISPR interventions with single-cell RNA sequencing to measure each perturbation's effect across many thousands of cells.
- ChIP-seq and ENCODE: lab methods and a public database showing where transcription factors physically bind DNA.
- Enhancer: a DNA region that boosts nearby gene activity.
- Co-expression and GENIE3: baseline approaches that infer networks from correlations in gene activity, without intervention data.
- AUROC / AUPRC / FDR: standard accuracy and false-discovery measures for predicted network edges.
- SHAP: a method for explaining which inputs drive a machine-learning model's predictions.
- Triple-negative breast cancer: a subtype lacking the hormone and HER2 receptors that common targeted drugs act on. · level: research-level

<details><summary>Original abstract</summary>

Triple-Negative Breast Cancer (TNBC) represents an aggressive breast cancer subtype that lacks actionable cell-surface receptors, restricting frontline systemic management to cytotoxic chemotherapy. While recent functional epigenomics shows that TNBC progression is governed by non-coding regulatory remodeling at distal super-enhancers, conventional Gene Regulatory Network (GRN) inference methods rely on observational transcriptomic co-expression, which suffers from technical dropouts and confounding correlations that inflate false discoveries (>30%). Here, we present an interventional network inference framework that integrates large-scale single-cell CRISPR-interference perturbation sequencing (Perturb-seq; GSE224986, 95,678 cells across 11,975 sgRNAs) with ENCODE Factorbook ChIP-seq physical transcription factor binding priors across 819 somatic mutation-associated enhancer loci in human TNBC (MDA-MB-231). Our pipeline reconstructed a tripartite network yielding 5,935 physical TF-enhancer edges, 383,757 functional enhancer-gene edges, and 542,760 unique TF-target gene functional pairs across 372 active enhancers. Topological centrality prioritized master transcriptional drivers governing TNBC oncogenic signaling, including CTCF, POLR2A, EP300, JUND, MYC, and FOS, which regulate Hallmark programs for Epithelial-Mesenchymal Transition (p = 1.2 x 10-9) and cell cycle progression. Explainable machine learning (SHAP TreeExplainer) revealed non-linear, thresholded transactivation dynamics for AP-1 and MYC. Quantitative benchmarking against held-out CRISPRi ground truth demonstrated strong discriminatory accuracy (AUROC = 0.8999, AUPRC = 0.8745, Precision = 90.13%, FDR = 9.87%), substantially outperforming GENIE3 (AUPRC = 0.6323, FDR = 35.73%) and co-expression correlation (AUPRC = 0.6814). In silico-simulated driver feature silencing correlated with experimental responses (R2 = 0.473, p < 10-122), and master driver signatures significantly stratified overall survival in the METABRIC (n = 320) and TCGA-BRCA (n = 160; p [&le;] 0.019) cohorts. Finally, in silico perturbation modeling indicated that multi-target epigenetic combinations achieved 93% topological disruption of oncogenic regulatory connectivity, nominating prioritized candidate circuits for experimental validation.

</details>

### [Predicted templates improve the prediction of antibody-antigen structures by AlphaFold 3 and Boltz-2](https://www.biorxiv.org/content/10.64898/2026.11.20.768078v1)
*Ziaee, O.; Lazou, M.; Joseph-McCarthy, D. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768078 v1 · relevance 0.12

- **In one sentence**: Adding rigid-body docking-generated templates from PIPER to AlphaFold 3 and Boltz-2 raises the success rate for predicting antibody-antigen complex structures on a leakage-free benchmark.
- **In plain words**: Antibodies bind to foreign molecules (antigens), and predicting the 3D shape of that pair is still hard for AI structure-prediction tools. The authors used a cheaper, older physics-style docking program, PIPER, to produce rough guesses of how the two molecules fit together, and fed those guesses to AlphaFold 3 and Boltz-2 as templates. On their benchmark, this raised the share of cases where the top prediction was acceptable or better from 56.2% to 63.4% for AlphaFold 3.
- **Why it matters**: Antibody-antigen structures matter for drug and vaccine design, and the approach is a modest, measured improvement on one benchmark rather than a general solution. It suggests traditional docking can complement machine-learning predictors where training data and evolutionary information are scarce, though the text does not test broader settings.
- **Background needed**: - Protein structure prediction: AI tools estimate a molecule's 3D shape from its sequence.
- Antibody-antigen complex: an antibody physically bound to the target molecule it recognizes.
- Rigid-body docking: computing how two fixed 3D shapes can fit together, ranking many positions by a score.
- Templates: known or approximate structures given to a predictor as a starting hint.
- Success rate here means the share of complexes where the top model is at least "acceptable" quality.
- Random seeds: different starting points for the AI sampling; 1000 seeds means 1000 attempts.
- "Leakage-free" means the benchmark excludes structures the AI may have seen during training. · level: research-level

<details><summary>Original abstract</summary>

Motivation: In spite of the much improved protein structure prediction methods, the success rate remains low for antibody-antigen complexes. While this can be improved by computationally demanding massive sampling, results are still much poorer than for most other types of protein-protein interactions. In principle, improvement can be achieved by using templates that are close enough to the native structure of the complex, but these are generally not available for antibody-antigen complexes. Results: We explore the use of templates, generated by the computationally inexpensive rigid body docking program PIPER. Applied to a leakage-free antibody-antigen benchmark set, standard AlphaFold 3 with 1000 random seeds yields acceptable or better models as the top predictions for 56.2% of complexes. Adding the PIPER generated templates in the unmasked version of AlphaFold 3 either increases the success rate to 63.4%, or reaches the same 56.2% success rate in about 200 runs. The template-based approach similarly improves antibody-antigen prediction by Boltz-2. This result demonstrates that the space explored by the ML based approach can be expanded by adding templates prepared by traditional docking, compensating for the lack of evolutionary relationship and the limited availability of training data. Availability and Implementation: The ClusPro server (https://cluspro.bu.edu/login.php) containing the PIPER program is free for non-commercial applications and the program is available by request (https://www.vajdalab.org/). All other study data are included in the article and/or supporting information.

</details>

## Neuroscience

### [Sex-dependent gating of astrocyte-driven nociceptive plasticity](https://www.biorxiv.org/content/10.64898/2026.11.18.767473v1)
*Klinger, L.; Uhrik, L.; Ravagnan, E. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.18.767473 v1 · relevance 0.08

- **In one sentence**: In rats, chemogenetic activation of distinct spinal astrocyte G-protein-coupled receptor pathways produced sex-dependent synaptic depression or potentiation at nociceptive synapses, with hormones and extracellular matrix organization gating whether plasticity occurs in females.
- **In plain words**: This study looks at how support cells in the spinal cord, called astrocytes, can change the strength of pain-signaling connections. In male rats, switching on specific astrocyte signaling pathways strengthened or weakened these connections, but in female rats the same activation produced no detectable change. Females still developed mechanical hypersensitivity similar to males, so the change in connection strength and the pain behavior did not line up.
- **Why it matters**: Sex differences in pain are well documented but their cellular causes are not well understood, so a sex-dependent control point in spinal circuits is relevant to pain research. The text suggests hormones and the surrounding extracellular matrix may set how susceptible these circuits are, though how this translates to human pain is not shown here.
- **Background needed**: - Astrocytes: star-shaped glial cells that support and modulate neurons, not only the neurons themselves.
- Nociception: the nervous system's detection and signaling of potentially harmful stimuli.
- Synaptic plasticity: lasting strengthening or weakening of connections between nerve cells, thought to underlie learning and some chronic pain.
- Chemogenetics: engineering cells to respond to a designed drug so researchers can switch their activity on or off.
- G-protein-coupled receptors (Gq and related pathways): cell-surface receptors that relay signals inside cells.
- Gonadectomy and ovariectomy: surgical removal of gonads, used to study the role of sex hormones; testosterone treatment tests hormone effects.
- Perineuronal nets: mesh-like extracellular matrix layers around neurons that can limit plasticity.
- Mechanical hypersensitivity: increased pain response to light touch or pressure. · level: research-level

<details><summary>Original abstract</summary>

Sex differences in pain are well established, yet how nociceptive processing is differentially regulated across sexes remains poorly understood. Here, we show that spinal astrocytes provide pathway-specific control of acute nociceptive synaptic plasticity in rats. Chemogenetic activation of distinct astrocytic G-protein-coupled receptor pathways induced synaptic depression or potentiation at spinal nociceptive synapses in males, but failed to evoke detectable plasticity in females. Despite this lack of astrocyte-induced synaptic plasticity, females developed mechanical hypersensitivity comparable to males, revealing a dissociation between synaptic plasticity and pain-related behavior. Gonadectomy prevented astrocyte-induced plasticity in males, whereas testosterone treatment enabled Gq-dependent synaptic depression in ovariectomized females. Females exhibited more prominent perineuronal net labeling, and enzymatic degradation of extracellular matrix (ECM) components enabled Gq-dependent synaptic depression in females. Together, these findings identify hormonal status and ECM organization as important determinants of the susceptibility of spinal nociceptive circuits to astrocyte-driven synaptic plasticity.

</details>

### [Concurrent neuronal activity gates persistent dendritic spine shrinkage during mGluR-induced long-term depression](https://www.biorxiv.org/content/10.64898/2026.11.21.765465v1)
*Rojo-Francas, E.; Sanchez-Rodriguez, N.; Santuy, A. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.21.765465 v1 · relevance 0.07

- **In one sentence**: In rat hippocampal slice cultures, mGluR1/5-induced LTD produces persistent dendritic spine shrinkage only when neuronal activity coincides with mGluR activation, a process the authors call MIND-sLTD that depends on mGluR1/5 and de novo protein synthesis but not NMDARs.
- **In plain words**: Brain cells strengthen or weaken their connections, and the tiny bumps on their branches (spines) grow or shrink along with that change. This paper asks whether weakening caused by a particular chemical signal (mGluR activation) also makes spines shrink, since earlier reports disagreed. The authors found that spines shrink for good only when the brain tissue is also highly active at the same moment, and this also held for single spines stimulated with a laser.
- **Why it matters**: The work offers a possible explanation for conflicting earlier reports on whether this form of weakening changes spine structure, by pointing to timing and activity as a condition. The text does not show how far the finding generalizes beyond these slice cultures and this specific drug-based protocol, so its wider significance is still to be tested.
- **Background needed**: - Dendritic spines: small protrusions on nerve cell branches where most excitatory synapses sit; their size is linked to synaptic strength.
- LTP / LTD: long-lasting strengthening / weakening of synapses, thought to underlie learning and memory.
- mGluR and NMDAR: two types of receptors for the brain's main excitatory signal, glutamate; NMDARs are a separate class from mGluRs.
- DHPG: a drug that activates mGluR1/5 receptors and is used to trigger this form of LTD experimentally.
- Organotypic slice culture: a thin slice of rat hippocampus kept alive in a dish, used as a model of brain tissue.
- Calcium imaging (GCaMP6) and two-photon glutamate uncaging: methods for watching calcium signals in cells and for releasing glutamate at single spines with a laser.
- Protein synthesis: making new proteins, here shown to be needed for the lasting change. · level: research-level

<details><summary>Original abstract</summary>

Synaptic plasticity is a fundamental mechanism underlying learning and memory. Most excitatory synapses reside on dendritic spines, which undergo both functional and structural changes. These two forms of plasticity are typically tightly coupled: spines enlarge during synaptic strengthening (long-term potentiation, LTP) and shrink during synaptic weakening (long-term depression, LTD). While this coupling is well established for NMDA receptor (NMDAR)-dependent LTD, there are conflicting reports concerning whether spine shrinkage is coupled with metabotropic glutamate receptor (mGluR)-dependent LTD. To investigate the source of these conflicting results, we induced mGluR-LTD with the mGluR1/5 agonist DHPG in organotypic rat hippocampal slice cultures and monitored changes in spine morphology and calcium transients in CA1 pyramidal neurons expressing DsRed2 and GCaMP6. We found that mGluR activation is accompanied by long-term spine shrinkage only under conditions of elevated hippocampal neuronal activity. This form of plasticity, mGluR-induced neuronal activity-dependent structural LTD (MIND-sLTD), requires mGluR1/5 activation and de novo protein synthesis, but not NMDAR signaling. Persistent structural changes occur only when neuronal activity coincides temporally with mGluR activation. MIND-sLTD also occurs at individual synapses: mGluR activation induces persistent single-spine shrinkage only when synchronized with two-photon glutamate uncaging, independently of NMDARs. These findings identify a novel form of structural plasticity and suggest a coincidence-detection mechanism that integrates mGluR signaling with synaptic activity to consolidate long-term spine remodeling.

</details>

## Genetics and genomics

### [Population-level learning of non-additive effects enables accurate and efficient prediction of combinatorial perturbation responses](https://www.biorxiv.org/content/10.64898/2026.11.20.768136v1)
*An, s.; Gong, Q.; Cao, K.* · `genomics` · bioRxiv doi:10.64898/2026.11.20.768136 v1 · relevance 0.10

- **In one sentence**: GAIN is a lightweight population-level model that predicts the pseudobulk response to a pair of perturbations as the sum of their single-perturbation responses plus a learned interaction term, benchmarked against additive and cell-level methods on combinatorial genetic and drug screens.
- **In plain words**: Scientists often want to know what happens when two genes are switched off together or when two drugs are combined, but there are too many possible pairs to test them all. This paper proposes GAIN, a simple model that starts from the measured effects of each perturbation on its own, adds them up, and then learns only the correction for how the pair departs from simply adding up. On three single-cell datasets, the authors report that it predicted combination responses more accurately than a plain additive baseline and than cell-level methods, while training much faster.
- **Why it matters**: Predicting combination effects could help choose which gene pairs or drug combinations to test in the lab, which matters when screens are expensive. The text reports that complex deep-learning and foundation models often fail to beat a simple additive baseline, so a lightweight alternative that does better is of interest, though its broader value depends on results beyond the three datasets described.
- **Background needed**: - Combinatorial perturbation: deliberately disrupting two or more genes or treatments together to see their joint effect.
- Additive baseline: the naive prediction that a pair's effect equals the sum of each single effect.
- Non-additive effect (epistasis or synergy): when the combined effect differs from that sum, either stronger (synergy) or weaker (dampening).
- Single-cell data: measurements taken cell by cell; "pseudobulk" means averaging these cells into one profile per condition.
- CRISPR screen: a method that uses gene-editing tools to switch genes off across many cells and see which changes matter.
- Generalization settings: testing whether predictions hold for combinations or conditions not seen during training. · level: research-level

<details><summary>Original abstract</summary>

Combinatorial perturbations are widely used to study genetic interactions and to develop drug combinations, but the number of possible combinations grows quadratically with the number of perturbations, and only a small fraction can be measured in a screen experiment. Despite their growing sophistication, deep-learning and foundation models often fail to outperform a simple additive baseline based on measured single-perturbation responses. This suggests a simpler approach that builds on these measurements and directly learns deviations from additivity at the population level. We therefore developed GAIN, a lightweight model that implements these principles by predicting the pseudobulk response to a combination as the sum of its two single-perturbation responses and a learned interaction term. Across three single-cell datasets of genetic and drug combinations, GAIN corrected deviations from additivity and outperformed the additive model and cell-level methods across generalization settings and metrics, while training 3- to 64-fold faster. Applied to a combinatorial CRISPR screen of leukemia differentiation regulators, GAIN revealed synergy between key regulators of the differentiation block and genes that restrain differentiation but have little effect alone. It also revealed dampening by the histone chaperone FACT, which supports the induction of differentiation genes. These results establish population-level modeling of the deviation from additivity as a simple, accurate and scalable approach to predicting combination responses.

</details>

### [Single-cell study of the FCG rat model and cross-species comparison reveal stronger gene regulation by sex chromosome complement in the medial septum](https://www.biorxiv.org/content/10.64898/2026.11.19.767942v1)
*Turnbill, V.; Zhang, G.; Harris, E. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767942 v1 · relevance 0.09

- **In one sentence**: Single-cell transcriptomic analysis of the medial septum in the four core genotypes (FCG) rat model, compared with the FCG mouse, finds that sex chromosome complement (XX vs. XY) dominates sex-biased gene regulation alongside gonadal effects, though individual sex-biased genes differ between species.
- **In plain words**: Male and female brains differ in many diseases, and it is hard to tell whether this comes from the sex organs (ovaries or testes) or from the chromosomes themselves (XX or XY). This study used a special rat model that separates these two influences and measured gene activity in individual brain cells of the medial septum, a region near the center of the brain involved in mood and memory. The authors report that the chromosomes had a stronger effect on gene activity than the gonads, and that this pattern was broadly similar to what they saw in the mouse version of the model.
- **Why it matters**: The result challenges the common view that sex hormones from the gonads mainly drive sex differences in the brain, which matters for how sex differences in conditions like anxiety, epilepsy, and Alzheimer's disease are studied. The paper also links the affected genes to these diseases and suggests possible drug candidates, but the text does not show whether those candidates have been tested, so their clinical relevance remains unclear.
- **Background needed**: - Sex differences in brain disease can come from sex hormones made by the gonads (ovaries or testes) or from sex chromosomes (XX vs. XY).
- The four core genotypes (FCG) model is a set of animals where chromosome type and gonad type are varied separately, so their effects can be told apart.
- Single-cell gene expression profiling measures which genes are active in each individual cell, grouping cells by type.
- Gene regulatory network and transcription factor analyses try to identify the master switches that control groups of genes.
- Cross-species comparison asks whether a finding in one animal (mouse) also holds in another (rat).
- The medial septum is a small brain region that helps regulate anxiety, memory, and rhythm of brain activity. · level: research-level

<details><summary>Original abstract</summary>

Sex differences are prominent in neuropsychiatric, neurological, and neurodegenerative conditions. While both gonads (ovaries vs. testes) and sex chromosome complement (SCC; XX vs. XY) contribute to sex differences, these effects are hard to differentiate in humans and gonadal contributions have been considered dominant in the brain. The four core genotypes (FCG) mouse model distinguishes between SCC and gonadal effects but whether findings are conserved across species remains unclear. Here, we present the first application of the novel FCG-derived rat model to explore cell-type-specific sex differences in the medial septum (MS), which shows robust structural sex differences, and convergence/divergence between species. Differential gene expression, pathway, transcription factor, and gene regulatory network analyses show dominant SCC effects and concordant gonadal effects on gene and network regulation in rat MS cell types. Comparison between the FCG rat and mouse models find convergence across species on the dominance of the SCC in regulating gene expression in concert with gonadal effects in the MS, despite divergence in individual sex-biased genes. In both species, the sex-biased, cell-type-specific MS genes and networks are associated with diverse diseases relevant to MS functions, such as anxiety, Alzheimers Disease, epilepsy, and schizophrenia, that can be targeted by proposed therapeutic candidates. Our cross-species investigation identifies a conserved dominance of SCC effects in sex-biased gene expression in the MS, thereby challenging the classical gonad-centric view of sexual differentiation in the brain and highlighting the MS as an important region for the study of sex differences driven by the sex chromosome complement.

</details>

## Cell and molecular biology

### [Palmitic acid overload does not promote full-blown dysfunction in SGBS adipocytes which is reflected in their secretome](https://www.biorxiv.org/content/10.64898/2026.11.19.767488v1)
*Angelini, S.; Stifani, G.; La Runa, G. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.19.767488 v1 · relevance 0.11

- **In one sentence**: In cultured SGBS human fat cells, a 96-hour exposure to palmitic acid (a saturated fatty acid) raised lipid droplets, MCP-1 expression and IL-6/IL-8 secretion but did not impair insulin signalling in those cells or in co-cultured muscle cells.
- **In plain words**: Diets high in saturated fats are linked to obesity and poor metabolic health, but it is unclear how much these fats directly harm human fat cells. The authors grew a human fat-cell line (SGBS) in palmitic acid, a common saturated fat, for four days and then checked for inflammation, fat storage, insulin response, and the chemical messages the cells released. The fat cells stored more fat and sent out more inflammatory signals, but they did not become clearly dysfunctional, and their released messages did not block insulin signalling in muscle cells.
- **Why it matters**: It suggests that a saturated fat alone, acting on fat cells without other cell types from the tissue, may not be enough to cause full-blown insulin resistance, which matters for how obesity-related damage is understood. The text does not establish how this applies to whole-body or in-vivo health, and the work uses a single cell line.
- **Background needed**: - Adipocytes: fat-storing cells; they also release hormone-like messenger proteins (adipokines and cytokines).
- SGBS cells: a human pre-fat cell line used as a laboratory model of human fat cells.
- Palmitic acid (PA): the most common saturated fatty acid in the diet and body; BSA (bovine serum albumin) was used as the control carrier.
- Insulin signalling: a chain of protein phosphorylation steps (Akt, AS160) that tells cells to take up glucose; impaired signalling is a marker of insulin resistance.
- NF-kB, MCP-1, IL-6, IL-8, adiponectin: inflammation-related signals and a protective hormone whose levels were measured.
- Stromal vascular fraction: other cell types in fat tissue (such as immune cells) that were absent from this model.
- Myotubes: immature muscle cells grown in culture, used here as a test of insulin response. · level: research-level

<details><summary>Original abstract</summary>

Background: Energy excess, and particularly long-chain saturated fatty acid (SFA) overload, are instrumental in promoting obesity and hampering metabolic health. However, SFA contribution to human adipocyte metabolic and endocrine dysfunction remains elusive. Nonetheless, we have already provided evidence that a 48-hour palmitic acid (PA) exposure is not sufficient to hamper Simpson-Golabi Behmel Syndrome (SGBS) adipocytes insulin signalling. Objective: This study aims at evaluating whether a 96-hour exposure to PA is able to disrupt SGBS adipocyte metabolic health and induce the release of a secretome capable of hampering insulin signalling in skeletal muscle cells. Methods: SGBS adipocytes were treated with either 1000 uM PA or bovine serum albumin (BSA) for 96 hours followed by the assessment of the NFkB signalling and the expression of genes associate with inflammation and adipocyte metabolic stress. Furthermore, adipocytes were labelled with BODIPY and lipid droplet as well as cell size semi-quantified using ImageJ. Insulin-induced phosphorylation of Akt and Akt substrate of 160 kDa (AS160) was assessed by Western Blot. The effect of PA on SGBS secretome was assessed by both ELISA as well as MILLIPLEX. Finally, human immortalised myotubes were co-cultured with BSA or PA-treated SGBS adipocytes for 24 hours followed by the assessment of insulin signalling at the Akt level. Results: PA did not activate the NFkB signalling pathway, but induced the expression of MCP-1 while tending to upregulate IL-6 mRNA levels. Despite 96-hour PA exposure leading to an increase in lipid droplet and cell size, this was not coupled with an impairment in insulin signalling. Nevertheless, this SFA promoted an increase in IL-6 and IL-8 secretion while tending to enhance the release of adiponectin by SGBS adipocytes. Finally, the secretome from PA-treated SGBS adipocyte did not impair insulin-induced phosphorylation of Akt relative to controls in myotubes. Conclusions: Thus, in the absence of the stromal vascular fraction, direct exposure of SGBS adipocytes to PA overload is not sufficient to elicit overt dysfunction. The absence of full-blown adipocyte dysfunction is reflected in the secretome of these cells which failed to disrupt skeletal muscle insulin signalling.

</details>

### [Extra-sheath transplantation of human retinal organoids (hROs): effects on visual recovery and retinal repair following optic nerve injury](https://www.biorxiv.org/content/10.64898/2026.11.18.767615v1)
*Luo, Y.; Chen, X.; Kang, J. et al.* · `developmental biology` · bioRxiv doi:10.64898/2026.11.18.767615 v1 · relevance 0.08

- **In one sentence**: In C57 mice with optic nerve crush, transplanting day-30 human retinal organoids at the injury site was associated with better optic-disc and ganglion cell layer preservation, higher flash VEP P2 amplitudes, and enhanced optomotor responses, though donor-circuit integration was not directly shown.
- **In plain words**: Crushing the optic nerve, the cable that carries vision from the eye to the brain, can cause lasting vision loss. In this mouse study, researchers placed small clusters of lab-grown human retina tissue at the crush site and tracked the eyes and nerve signals over four weeks. Transplanted mice kept more of their nerve-cell layer and showed stronger signals from the visual pathway and better responses to moving stripes, though the authors say they have not yet proven that the human tissue wired itself into the brain's circuits.
- **Why it matters**: Optic nerve injury has few treatments, so a strategy that protects nerve cells and improves visual-pathway activity is of interest. The paper is a preclinical mouse study, so its relevance to human patients is uncertain, and the authors themselves note that tracing and synaptic validation are still needed.
- **Background needed**: - Retinal ganglion cells: the eye's output neurons whose long axons form the optic nerve to the brain.
- Optic nerve crush: a standard lab injury that damages these axons and kills many ganglion cells.
- Retinal organoids: three-dimensional tissue grown from stem cells that mimics parts of the retina.
- Microelectrode array: a plate of tiny electrodes that records electrical activity from cells.
- Electroretinogram (ERG) and visual evoked potential (VEP): recordings of electrical responses from the retina and the visual brain pathway; b-wave reflects mainly outer-retina activity, P2 reflects downstream visual-pathway responses.
- Optomotor response: a mouse's reflexive head or body tracking of moving stripes, used as a measure of vision.
- Light-dark box: a behavior test that is non-specific, since mice move between dark and light for many reasons.
- Immunostaining (RBPMS, TUJ1, IBA1): labeling that marks ganglion cells, their axons, and microglia (immune cells of the brain and retina). · level: research-level

<details><summary>Original abstract</summary>

Traumatic optic nerve injury interrupts retinal ganglion cell output and can produce permanent visual disability, yet a therapeutic strategy that couples retinal protection with recovery of visual-pathway activity remains unavailable. Here, we evaluated human retinal organoid transplantation at the site of optic nerve crush in C57 mice. Human retinal organoids derived from embryonic stem cells were used at day 30 and showed retinal-lineage immunoreactivity together with spontaneous microelectrode-array activity. Across post-surgical days 7, 14, and 28, transplantation was associated with preservation of optic-disc appearance and ganglion cell layer thickness. The structural benefit became statistically distinguishable from the crush group at day 28 and remained incomplete relative to the uninjured or sham group. Serial RBPMS and TUJ1 immunostaining further supported attenuation of retinal ganglion cell body and neurite loss, while IBA1 staining indicated an altered microglial response. Full-field electroretinographic b-wave responses showed no detectable between-group differences, arguing against a major outer-retinal effect. In contrast, flash visual evoked potential P2 amplitude was higher in transplanted than in crush-only mice at all measured time points, consistent with improved visual-pathway responsiveness. Transplant recipients also showed enhanced optomotor responses across tested spatial-frequency and contrast conditions. Light-dark behavior shifted toward greater dark-compartment occupancy and activity, although this assay remains non-specific for visual recovery. Together, these findings support a model in which hROs transplantation at an optic nerve injury site promotes multi-level functional preservation after optic nerve crush. Definitive evidence for donor-derived circuit reconstruction will require graft tracing, synaptic validation, and prespecified electrophysiologic analyses.

</details>

## Immunology and microbiology

### [Local macrophage and cDC1 cooperation in the liver drives T-cell immune surveillance against pioneering metastatic cancer cells.](https://www.biorxiv.org/content/10.64898/2026.11.21.768283v1)
*Pinci, B.; Manzanal, A.; Chiclana-Valcarcel, M. L. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.21.768283 v1 · relevance 0.15

- **In one sentence**: Intravital imaging of early liver metastasis in mice shows that resident Kupffer cells, conventional dendritic cells (cDC1s), and T cells cooperate in local clusters to mount antitumor T-cell responses, and that expanding cDCs with Flt3L-Ig reduces metastatic outcome.
- **In plain words**: Cancer often spreads to the liver through the bloodstream, and this paper asks how the liver's own immune cells respond when the first tumor cells arrive. Using live imaging inside the liver, the authors describe three stages: routine patrolling of the tissue, a rush of neutrophils and uptake of tumor material by resident macrophages, and then T-cell activation in small clusters of immune cells within the liver. They report that this response depends on dendritic cells presenting tumor antigens and on their cooperation with local macrophages.
- **Why it matters**: It describes a local immune program in the liver that may help explain why some arriving tumor cells are controlled and others establish metastases. The text reports that boosting dendritic cells with Flt3L-Ig reduced metastasis development, which could point toward immunotherapy strategies, though the text does not show that such approaches would work in people.
- **Background needed**: - Metastasis: cancer cells leaving a original tumor and seeding new growth elsewhere; the liver is a common site.
- Intravital imaging: filming living cells inside an intact animal organ, here in mice.
- Kupffer cells: macrophages (immune cells that engulf debris) living inside the liver.
- Dendritic cells (cDC1s): immune cells that capture material from invaders or tumors and display pieces of it to T cells; "cross-presentation" means showing material from outside cells on their own surface.
- T cells: immune cells that can kill cells displaying a specific target; their activation is the key step here.
- Flt3L-Ig: a drug-like molecule that increases the number of dendritic cells in mice.
- The text is an abstract only, so details of methods, sample sizes and statistics are not available here. · level: research-level

<details><summary>Original abstract</summary>

The liver is one of the most frequent sites for hematogenous metastasis across different types of cancer, but how the liver mounts effective immune responses against arriving tumor cells is not fully understood. Using intravital imaging, we have visualized the initial steps of liver metastasis and delineated three phases in the immune response at the earliest stages of liver metastasis: first, there is continuous surveillance of the liver parenchyma by discrete immune cell subsets in the premetastatic tissue. Second, upon metastatic cell arrival, there is massive neutrophil recruitment and tumor-cell material uptake mediated by resident macrophages. Third, antitumor-specific T-cell activation takes place in situ within intrahepatic leukocyte clusters. We find that tumor-derived material uptake triggers transcriptional programs in liver myeloid cells that upregulate chemoattraction programs in Kupffer cells and cDCs, leading to T-cell activation. Antigen cross-presentation and a functional partnership between cDC1s and local macrophages to recruit and form T-cell activation clusters are required for the elicitation of these intrahepatic T-cell responses. Consequently, prior expansion of cDCs by Flt3L-Ig treatment significantly enhances immunosurveillance, curtailing successful metastasis development. Collectively, our findings identify coordinated immune responses that are essential for anti-metastatic immunity within the liver, uncovering a program to mount defenses against tumor cells arriving in the liver.

</details>

### [Viral genetic variation programs divergent neuroimmune states during rabies infection](https://www.biorxiv.org/content/10.64898/2026.11.20.768130v1)
*Gassmann, S.; Mullner, R.; Zaeck, L. M. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.20.768130 v1 · relevance 0.13

- **In one sentence**: In mice infected in the brain with genetically distinct rabies viruses, proteomic and spatial imaging analyses show that viral load does not predict the strength or type of the brain's immune response, and that viral genetics (including an engineered interferon-sensitive variant) shape divergent neuroimmune states.
- **In plain words**: Rabies is a virus that attacks the brain, and different strains of it can cause very different reactions from the body's defenses even when they multiply to similar levels. This study infected mice directly in the brain with several rabies viruses, including dangerous field strains, a weakened strain, and a modified strain that is more easily stopped by interferon, an antiviral alarm signal. The researchers tracked proteins over time and mapped immune activity across brain regions.
- **Why it matters**: It suggests that how much virus is present is not a reliable guide to how the brain's immune system responds, which matters for understanding why some infections cause severe disease and for designing safer vaccines. The text is limited to a mouse model, so any link to human rabies or vaccine design is something the authors would need to test rather than something shown here.
- **Background needed**: - Rabies virus (RABV) spreads through nerve tissue and is nearly always fatal once symptoms reach the brain.
- Field strains are wild viruses found in animals; attenuated strains are weakened versions used as models or in vaccines.
- Interferons are signaling proteins that alert cells to viruses and trigger antiviral defenses; some viral proteins (here, the phosphoprotein) block this alarm.
- Complement is a group of blood and tissue proteins that help clear pathogens and inflame tissue.
- Proteomics measures the proteins present in tissue; spatial imaging shows where in the tissue they occur.
- Intracerebral infection means the virus is injected directly into the brain. · level: research-level

<details><summary>Original abstract</summary>

Viral burden does not necessarily predict the extent or composition of the host immune response, reflecting the complexity of virus - host interactions. Rabies virus (RABV) provides a powerful model to investigate this question because genetically distinct RABVs differ in replication, immune evasion, and neuroimmune activation. Here, we performed integrated temporal proteomic and spatial imaging analyses of recombinant RABV, including pathogenic, attenuated, and a newly generated interferon-sensitive variant with disrupted phosphoprotein antagonistic activity. Following intracerebral infection of mice, viruses established distinct neuroimmune states that diverged over time in antiviral signaling, complement activation, and immune response. Notably, the pathogenic field viruses rDogA and rFox both exhibited substantial viral accumulation, but elicited markedly different central nervous system (CNS) responses, with rDogA inducing limited host immune engagement, whereas rFox triggered early and broad antiviral, complement, and immune recruitment programs. Disruption of phosphoprotein-mediated interferon antagonism in rDogA enhanced interferon-stimulated gene expression and antiviral effectors, restricting viral accumulation without inducing broad neuroimmune remodeling. Conversely, the attenuated glycoprotein-modified rSAD GASGAS elicited strong complement activation and T cell recruitment with little detectable viral levels, revealing a highly immunogenic neuroimmune state. Spatial profiling further identified virus-dependent patterns of myeloid, astrocyte-associated, complement, and lymphocyte responses across brain regions. Together, these findings demonstrate how viral genetic background and its modulation of host antiviral responses shape divergent neuroimmune states in which viral accumulation, antiviral immunity, and CNS immune activation are differentially coordinated.

</details>

## Cancer biology

### [Adjuvant myeloperoxidase inhibition promotes B and T cell mediated control of murine melanoma metastasis](https://www.biorxiv.org/content/10.64898/2026.11.20.768197v1)
*Landreth, K. M.; Sharp, A. W.; Basnet, A. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.20.768197 v1 · relevance 0.11

- **In one sentence**: In an immunocompetent spontaneous melanoma mouse model, adjuvant inhibition of myeloperoxidase (MPO) reduced multi-organ metastasis in a B and T cell-dependent manner, linked to reduced NET release, and the effect was also seen in a spontaneous breast cancer model.
- **In plain words**: Melanoma, a dangerous skin cancer, often kills by spreading to distant organs. This study looked at an enzyme called myeloperoxidase, which is made mainly by certain white blood cells, and tested whether blocking it in mice with spontaneous melanoma could limit that spread. In the mice, blocking the enzyme reduced cancer spread to several organs, shifted the immune environment toward more B and T cells, and was linked to lower release of neutrophil extracellular traps (sticky webs of DNA released by immune cells).
- **Why it matters**: Few treatments target the myeloid immune cells that research suggests help cancer spread, so a druggable enzyme in those cells is of interest. The text supports the finding only in mouse models, and whether it applies to people is not shown here.
- **Background needed**: - Metastasis: cancer cells spreading from a primary tumor to distant organs, responsible for most melanoma deaths.
- Myeloid cells: a family of immune cells (such as neutrophils and macrophages) that can either fight or help tumors.
- Myeloperoxidase (MPO): an enzyme found mainly in myeloid cells that produces reactive chemicals; here it is the drug target.
- Neutrophil extracellular traps (NETs): web-like structures of DNA and proteins that immune cells release; the paper proposes them as a downstream mediator.
- B and T cells: adaptive immune cells; CD8+ and CD4+ T cells are subtypes, and the paper shows the anti-metastatic effect depends on them.
- Spontaneous mouse model: tumors arise naturally in an intact immune system rather than from injected cancer cells.
- Adjuvant therapy: treatment given after the primary tumor is removed, aimed at residual spread. · level: research-level

<details><summary>Original abstract</summary>

Metastasis is the spread of cancer cells from primary tumors to distant organs and accounts for the majority of melanoma deaths, with a 5-year survival rate of only 30%. Despite strong evidence that myeloid cells promote metastasis, there are limited clinically effective myeloid-directed therapies. Here, we demonstrate that targeting myeloperoxidase (MPO), a myeloid-lineage restricted enzyme, significantly reduced multi-organ metastatic burden using an immunocompetent mouse model of spontaneous melanoma. Adjuvant MPO inhibition remodeled the metastatic microenvironment by a reduction in Ly6G+Ly6C+ myeloid cells and enrichment of B and T cell populations. Importantly, adjuvant MPO inhibitor-mediated metastatic control was dependent upon B, CD8+ T cells and CD4+ T cells, and rapidly reduced circulating and disseminated tumor cells. MPO inhibition markedly decreased NET release, while NET deficiency and inhibition recapitulated the anti-metastatic effects of targeting MPO, implicating NETs as a potential downstream mediator of MPO-driven metastasis. We further validated these findings in a distinct spontaneous breast cancer model where adjuvant MPO inhibition similarly reduced multi-organ metastatic burden with comparable changes within the metastatic immune microenvironment. Collectively, our studies introduce MPO as a druggable regulator of metastasis where MPO inhibition limits metastatic disease by targeting immunosuppressive myeloid cells.

</details>

### [A KRASG12D-based organoid model for early oncogenic transformation of the mammary epithelium](https://www.biorxiv.org/content/10.64898/2026.11.17.766834v1)
*Jones, D. J.; Rao, L. E.; West, J. J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.17.766834 v1 · relevance 0.07

- **In one sentence**: A mouse mammary epithelial organoid model in which Cre-induced KRASG12D expression drives neoplastic growth without lumen formation, with heterotypic competition between mutant and wild-type cells and suppressed apoptosis.
- **In plain words**: Researchers wanted a lab system for watching the very first steps of breast tumor formation. They grew small 3D clumps of healthy mouse breast cells (organoids) and switched on a cancer-linked mutant gene, KRASG12D, in some of them. The mutant clumps grew abnormally and failed to form the hollow central space they normally develop, and mutant cells gradually took over when mixed with normal cells.
- **Why it matters**: The text suggests a tool for studying early tumor development that could later be used for prevention and drug testing, but it is a single study and the text does not show how far these findings extend to human cancer. The link to human breast cancer rests on gene-expression similarities the summary only describes briefly.
- **Background needed**: - Organoids: small, lab-grown 3D balls of cells that mimic parts of an organ.
- KRAS: a gene that acts as an on/off signal for cell growth; the G12D change is a common cancer-linked mutation that keeps it switched on.
- Cre-mediated expression: a genetic tool that turns a gene on in selected cells at a chosen time.
- Lumen: the hollow central cavity that normal breast ducts and organoids form.
- Heterotypic: a mixture of two cell types (here, mutant and normal cells) in the same tissue.
- Apoptosis: programmed cell death, a normal way for cells to be removed.
- Gene expression analysis: measuring which genes are switched up or down in cells. · level: intermediate

<details><summary>Original abstract</summary>

Modeling cancer initiation, progression, and metastasis has greatly impacted our understanding of fundamental cell and molecular mechanisms driving disease and has led to breakthrough treatments that greatly improve patient outcomes. Understanding the earliest stages of tumor formation is particularly important for uncovering the root causes of oncogenic transformation and tumor evolution. It has been historically difficult to model the cellular dynamics that drive the earliest stages of tumor evolution, largely due to difficulties in culturing and manipulating normal primary cells in 3-dimensional environments, triggering oncogenesis, and observing the resulting effects. Recent advances in 3D organoid culture provide a promising avenue to address these challenges. In this study, we have developed a Kras based organoid model of early tumorigenesis. In our model, oncogenic transformation was triggered by Cre-mediated expression of oncogenic KRASG12D in otherwise healthy murine-derived mammary epithelial organoids. While normal organoids displayed controlled organoid growth and morphogenesis, induction of KRASG12D caused neoplastic organoid growth that occurred with the absence of lumen formation. Gene expression analysis revealed up regulation of several KRAS effectors, and a broad repertoire of genes associated with tumor development and human breast cancer. Induction of oncogenic Kras in our model resulted in heterotypic organoids that possessed KRASG12D + cells growing alongside KRASG12D- cells. In this context, amplification of KRASG12D + cells occurred at the expense of KRASG12D- cells. Finally we observed that neoplastic growth of KRASG12D expressing organoids was associated with a suppression of apoptosis. We believe that our organoid model provides a platform that is suitable to examine the earliest stages of tumor development and can be expanded to study several questions related to cancer biology, prevention studies, therapeutic development, and beyond.

</details>

## Ecology and evolution

### [Biotic interactions buffer the effects of biodiversity loss on ecosystem functioning](https://www.biorxiv.org/content/10.64898/2026.11.20.768031v1)
*Vidiella, B.; Montoya, J. M.* · `ecology` · bioRxiv doi:10.64898/2026.11.20.768031 v1 · relevance 0.17

- **In one sentence**: A theoretical model of species interaction networks predicts that the effect of losing species on ecosystem functions such as primary production and carbon retention depends on how many and how strong the trophic links are.
- **In plain words**: Losing species from an ecosystem often weakens things like plant growth and carbon storage, but it is hard to say when the damage will be large. This paper proposes a theory suggesting that the web of feeding relationships between species decides how much harm each extinction causes. When many or strong feeding links exist, the remaining species can make up for lost ones through other paths, so the damage is smaller; when links are fewer or weaker, the ecosystem is far more sensitive to each loss.
- **Why it matters**: It offers a way to explain why biodiversity loss hits ecosystem functions unevenly across settings, and it names "interaction erosion" as a possible hidden part of the biodiversity crisis. The text gives only the abstract-level claim, so how well the theory fits real ecosystems is not shown here.
- **Background needed**: - Biodiversity: the variety of species in an area.
- Ecosystem functioning: processes such as primary production (plants making biomass from sunlight) and carbon retention (storing carbon rather than releasing it).
- Biotic interactions: relationships between living organisms, such as predation, herbivory or competition.
- Trophic links: feeding connections in a food web, showing who eats whom.
- Species interaction network: a map of all these connections in a community, treated mathematically.
- Extinction sensitivity: how much a function drops when a given species disappears. · level: research-level

<details><summary>Original abstract</summary>

Biodiversity loss generally impairs functions on which nature and societies depend upon. Yet, it is difficult to predict under which conditions losing biodiversity has larger effects on functions such as primary production or carbon retention. We present a theory that demonstrates that biotic interactions mediate the intensity of these effects. In species interaction networks with many or strong trophic links, biodiversity loss has weaker effects on functioning because alternative interaction pathways allow surviving species to compensate for species loss. In contrast, in networks with fewer or weaker links, ecosystem functioning is very sensitive to the extinction of species. Here, we identify interaction erosion as a hidden dimension of the biodiversity crisis that provides a unifying explanation for functional consequences of biodiversity loss across ecological contexts.

</details>

### [Resistance evolution in a single species reorganizes community responses across a resource-antibiotic landscape](https://www.biorxiv.org/content/10.64898/2026.11.20.768032v1)
*Aapalampi, I.-K.; Bischofberger, A. M.; Kiciatovas, D. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.20.768032 v1 · relevance 0.11

- **In one sentence**: Mapping how antibiotic resistance evolving in one bacterial species (Aeromonas caviae) reshapes 3- and 16-species community states, diversity and dominance across a grid of resource and antibiotic levels.
- **In plain words**: This study asks what happens to a whole group of bacterial species when one of them evolves resistance to an antibiotic. The researchers tested 64 combinations of food availability and antibiotic dose, using small communities of three and sixteen species. They found that the same resistance change could raise diversity in some conditions and lower it in others, and that it could reverse which of two dominant species won.
- **Why it matters**: It shows that the community-wide effects of one species evolving can depend strongly on the surrounding environment, which matters for predicting outcomes in medicine and microbial ecology. The text does not show how far these patterns extend beyond these laboratory communities, so broader claims should be treated cautiously.
- **Background needed**: - Community: a set of different species living together and competing for the same resources.
- Rapid evolution: genetic change within a species over a short time, here driven by antibiotic exposure.
- Antibiotic resistance: a heritable ability of bacteria to survive a drug that would normally kill or stop them.
- Inhibitory concentration: the antibiotic dose high enough to stop growth; below it, the drug alters growth more subtly.
- Community-state boundary: a threshold in environmental conditions where the community's composition shifts from one pattern to another.
- Dominance: which species makes up the largest share of the community.
- Diversity: how many species are present and how evenly they are represented. · level: research-level

<details><summary>Original abstract</summary>

Rapid evolution in one species can restructure ecological communities, but how its effects vary across environmental conditions remains poorly understood. Here we mapped the consequences of antibiotic resistance evolution in Aeromonas caviae across 64 combinations of resource availability and antibiotic stress in three- and 16-species bacterial communities. Resistance evolution changed where community-state boundaries were located, with boundaries lost or gained depending on resource availability. The same evolutionary change increased diversity in some environments but decreased it in others. Species success was partly explained by growth traits at zero or low antibiotic concentrations and by intrinsic resistance at inhibitory concentrations. Resistance evolution reversed dominance between the two dominant species and changed which traits mattered. It also altered other species' responses below inhibitory concentrations, mostly between closely related species. Our findings show that the consequences of evolution depend on environmental context but can be partly explained by species traits.

</details>

## Plant biology

### [Circadian clock components CCA1 and LHY shape heat responses across regulatory layers](https://www.biorxiv.org/content/10.64898/2026.11.19.767892v1)
*Strout, R. I.; Grubb, L. E.; Uhrig, R. G. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767892 v1 · relevance 0.11

- **In one sentence**: Time-resolved transcriptome, proteome and metabolome profiling of Arabidopsis clock mutants with altered CCA1/LHY expression after short heat stress, mapping shared and distinct clock-linked heat responses across gene regulation layers.
- **In plain words**: Heat hurts crop yields, and it hurts more when it arrives at night. This study asks how the plant's internal daily clock decides which heat responses happen at which time of day. The researchers used Arabidopsis (a small model plant) with altered levels of two clock genes, CCA1 and LHY, and measured genes, proteins and metabolites over time after a short heat stress.
- **Why it matters**: Understanding how the clock gates heat responses could eventually inform breeding or engineering crops that cope with hot nights, though the text itself only describes candidate connections and does not show direct crop benefits. The paper suggests sulfur assimilation, ROS scavenging and starch degradation as possible contributors to time-of-day thermotolerance, which are leads to test rather than established mechanisms.
- **Background needed**: - The circadian clock is an internal roughly 24-hour timing system that controls when many genes are switched on.
- CCA1 and LHY are closely related clock genes; altering their levels changes the clock's output.
- Transcriptome, proteome and metabolome mean the full sets of gene transcripts (RNA), proteins and small molecules measured in a sample.
- Heat stress here means a short exposure to high temperature, which triggers changes in gene activity.
- ROS (reactive oxygen species) are reactive molecules that rise under stress; plants use scavenging systems to limit damage.
- Starch degradation is the breakdown of stored sugar polymer, which supplies energy at night.
- Post-translational regulation means control of proteins after they are made, such as modification or stability changes. · level: research-level

<details><summary>Original abstract</summary>

High temperatures reprogram gene regulatory responses and are particularly deleterious for crop yield, especially when these events occur at night. This emphasizes that partitioning of heat responses is based on time of day. Coordination between time of day and environmental responses relies on the circadian clock. However, the precise regulatory mechanism of how the clock achieves this partitioning at different levels of gene regulation is poorly understood. Using circadian clock mutants with altered CCA1 and LHY expression, we generated a time-resolved transcriptome, proteome, and metabolome following a short-term heat stress in Arabidopsis. We identified regulatory connections specific to CCA1 and LHY, as well as those shared with other clock components linked to heat stress responses. Additionally, new connections between CCA1 and LHY and non-cycling genes highlight a broader role for the clock in regulating heat responsive gene expression. CCA1 and LHY regulated processes, such as sulfur assimilation and ROS scavenging, may contribute to time-of-day specific thermotolerance. Overall, heat responses were dampened in both the transcriptome and proteome in cca1lhy, suggesting both transcriptional and post-translational circadian-regulated processes are important for heat responses. Lastly, we identified differences in metabolic responses in cca1lhy and suggest a role for circadian regulation of starch degradation in thermotolerance. This study generates and utilizes data across levels of gene regulation to identify heat responses in the transcriptome and proteome regulated by CCA1 and LHY. These findings establish shared and distinct regulatory mechanisms of clock components in response to heat stress and provide new candidates for network integration and a foundation to engineer plants more tolerant to high temperatures depending on time of day.

</details>

### [Auxin regulates the proportions, but not the initiation, of Hibiscus trionum bullseyes](https://www.biorxiv.org/content/10.64898/2026.11.19.767829v1)
*Salvi, E.; Gatti, S.; Yeo, M. T. S. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767829 v1 · relevance 0.10

- **In one sentence**: In the Hibiscus trionum flower, auxin does not initiate the bullseye boundary during pre-patterning, but auxin signalling is needed to maintain distal-region cell behaviour and preserve bullseye proportions set in young petal primordia.
- **In plain words**: Many flowers have coloured patterns, such as a dark central "bullseye," that help attract pollinators. This paper asks whether the plant hormone auxin helps set up where those pattern regions begin in the petal of the Hibiscus trionum flower. The authors found that auxin does not start the boundary, but it is needed to keep the size ratio of the bullseye regions as the petal grows.
- **Why it matters**: The text suggests auxin could act as a "pattern modifier" that changes bullseye size over evolution by altering how fast different petal regions grow, which may help explain how flower patterns vary between species. This is an inference from the abstract alone, and the details of the experiments are not given here, so the strength of the claim is hard to judge.
- **Background needed**: - Auxin: a plant hormone that controls growth and cell behaviour in many tissues.
- Petal bullseye: a ring-like colour pattern with distinct central and outer zones on the petal surface.
- Pre-patterning: the early stage when regions of a developing organ first become different from one another, before visible pattern forms.
- Petal primordium: the very young petal tissue, before it has grown into its final shape.
- Distal region: the part of the petal farthest from the flower's base.
- Transcription factor: a protein that switches genes on or off; the abstract mentions these as known players in pigment and cell-shape control. · level: research-level

<details><summary>Original abstract</summary>

Colourful motifs on the surface of flower petals fulfill important ecological functions, mediating pollination and providing protection against environmental stressors. These patterns form when epidermis cells in different subdomains of the petal acquire contrasting chemical and structural features. While some of the enzymes and transcription factors involved in specifying the production of different pigments, cell shapes and textures have been identified, the signalling events and upstream processes that divide the petal surface in distinct regions are not yet understood. Plant hormones play key roles in orchestrating all aspects of plant development but whether and how they contribute to the establishment of petal patterns remain to be tested. Here, we investigate the roles of auxin during bullseye pattern development in Hibiscus trionum. We found that auxin does not initiate bullseye boundary formation during the pre-patterning phase. Instead, auxin signalling is essential for regulating cell behaviour in the distal region and preserving the bullseye proportions established in young petal primordia. Therefore, auxin could act as a pattern modifier over evolutionary timescales, shifting bullseye dimensions by modulating the relative growth of different petal regions.

</details>

## Bioengineering and synthetic biology

### [Internalizing-peptide engineering converts blocking anti-EGFR antibodies into EGFR lysosomal targeting degraders](https://www.biorxiv.org/content/10.64898/2026.11.20.768013v1)
*Petrov, P. D.; Vinueza-Gavilanes, R.; Vicente, A. P. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.20.768013 v1 · relevance 0.06

- **In one sentence**: Engineering full-length anti-EGFR antibodies (cetuximab and the LEI antibody) with cell-penetrating arginine-rich peptides converts receptor-blocking antibodies into degraders that reduce total EGFR levels in NSCLC models, including 3D spheroids, alone and with EGFR kinase inhibitors.
- **In plain words**: Some cancer drugs that target the EGFR protein only block its signal, while the protein stays on the cell surface. This study attaches short peptides that help cells take in molecules to anti-EGFR antibodies, so the antibody pulls the receptor into the cell where it is broken down. In lung cancer cell lines and 3D cell clusters, the engineered antibody lowered EGFR levels and, combined with kinase inhibitor drugs, slowed growth more than the drugs alone in some tests.</plain>
<parameter name="why">Reducing the amount of a receptor rather than only blocking it is a different strategy from standard EGFR inhibitors, and the text reports gains in combination with osimertinib and gefitinib in lab models. The text is limited to in vitro and 3D cell-culture work, so it does not show whether this helps in animals or patients; it may connect to antibody-based protein degradation approaches more broadly.</plain>
<parameter name="background">- EGFR (epidermal growth factor receptor) is a cell-surface protein that drives growth signals; it is a target in lung cancer.
- Cetuximab and LEI are antibodies that bind EGFR and block its activity.
- Tyrosine kinase inhibitors (TKIs) such as gefitinib and osimertinib block EGFR's internal signaling switch.
- Cell-penetrating peptides (here polyarginine, R12) are short chains that help molecules enter cells.
- Endocytosis and lysosomes: cells engulf surface proteins and break them down in acidic compartments; bafilomycin A1 blocks this acidification, used here as a control.
- Recombinant fusion protein: an antibody and peptide made together as one engineered molecule.
- 3D spheroids: clusters of cancer cells grown in culture that mimic some features of tumors.
- LDH release is a standard marker of cell membrane damage.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Conventional antibodies targeting the epidermal growth factor receptor (EGFR) primarily inhibit receptor activation rather than efficiently eliminating the receptor from tumor cells. Here, we investigated whether engineering full-length anti-EGFR antibodies with internalizing peptides could promote receptor degradation, enhance their biological activity and enable the development of recombinant receptor-depleting antibodies. Chemical conjugation of cetuximab (CTX) to the polyarginine peptide R12 enhanced intracellular uptake, reduced surface-accessible EGFR and decreased total receptor abundance in vitro. CTX-R12 conjugate also enhanced inhibition of wound repopulation in non-small cell lung cancer (NSCLC) cell lines, an effect reproduced using the R12 variant LINC18, and transferred to the independent blocking anti-EGFR antibody LEI. Incorporation of LINC19, a variant of LINC18, into recombinant full-length antibody fusion proteins preserved their activity. The LEI-LINC19 fusion (LEIP), reduced surface-accessible and total EGFR, with bafilomycin A1 reversing receptor loss and supporting an acidification-dependent endolysosomal component of degradation. Functional studies indicated that the antibody-peptide reduced DNA synthesis rate. Furthermore, siRNA-mediated EGFR depletion increased TKI-associated reductions in cellular biomass in PC9 cells and increased gefitinib responsiveness in H1975 cells. Consistently, combining LEIP with either osimertinib or gefitinib produced greater inhibition of H1975 wound repopulation than the corresponding individual treatments. LDH analysis revealed increased membrane-damage-associated LDH release following LEIP-gefitinib treatment but no additional increase with LEIP-osimertinib relative to osimertinib alone. These effects extended to 3D NSCLC models. CTX-R12 inhibited PC9 3D colony development, whereas LEIP restricted expansion of established PC9 colonies and reduced the projected area of H1975 spheroids. In H1975 spheroids initiated with 1,000 or 5,000 cells per well, LEIP-containing combinations with osimertinib or gefitinib produced greater inhibition of the spheroid size than the corresponding TKI-only treatments. Nuclear Green DCS1 staining revealed no detectable baseline core necrosis in untreated H1975 spheroids, whereas LEIP treatment was associated with DNA-positive material within and surrounding the spheroids. Moreover, LEIP-treated H1975 spheroids exhibited markedly reduced EGFR immunofluorescence compared with control and parental LEI-treated spheroids. Together, these findings demonstrate that internalizing-peptide engineering of blocking anti- EGFR antibodies can generate full-length EGFR-depleting fusion proteins with enhanced biological activity. The recombinant LEIP format and its activity in 3D in vitro NSCLC tumor models support further investigation of fusion antibody-mediated EGFR degradation as a complementary strategy to EGFR kinase inhibition.

</details>

### [Dual photoresponsive hydrogel surfaces enabling integrated single-cell analysis of morphology and gene expression](https://www.biorxiv.org/content/10.64898/2026.11.18.767535v1)
*Li, X.; Uehara, R.; Mizuno, K. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.18.767535 v1 · relevance 0.06

- **In one sentence**: A dual photoresponsive hydrogel surface that uses light to trap individual cells in a uniform array, track their shape changes over time, and selectively release chosen cells for single-cell gene expression analysis.
- **In plain words**: Scientists want to watch how individual cells change shape over time and then check which genes those cells are switching on, but it is hard to do both on the same cell. This paper describes a gel-coated surface that holds cells in place using one kind of light, lets researchers film them, and then uses a second kind of light to melt the gel under chosen cells so those cells can be collected. The authors report using this to link cell shape changes to gene activity, including in invasive cancer cells.
- **Why it matters**: Connecting what a cell looks like over time with what genes it is using is a long-standing gap in single-cell research, so a workflow that does both on the same selected cells may be useful for studying cell variability. The text is only an abstract, so the strength of the results, the number of cells, and how well the method compares with existing tools cannot be judged from it.
- **Background needed**: - Single-cell analysis: studying cells one at a time, since cells in the same sample can behave quite differently.
- Gene expression: how actively a cell is turning its genes into products; often measured by sequencing the cell's RNA.
- Hydrogel: a water-swollen, jelly-like polymer network that can be used as a cell-friendly surface or scaffold.
- Photoactivatable / photodegradable: chemical groups that change or break apart when hit with light, letting researchers control the material with a light beam.
- Morphological dynamics: changes in a cell's shape and size over time, usually tracked by microscope imaging.
- Invasive cancer cell behavior: the tendency of cancer cells to move into surrounding tissue, a key feature of metastasis. · level: research-level

<details><summary>Original abstract</summary>

Integrated single-cell analysis linking time-resolved cellular phenotypic dynamics with gene expression is essential for understanding cellular heterogeneity but remains technically challenging. Here, we report a dual photoresponsive hydrogel that combines a photoactivatable cell-trapping material with a photodegradable hydrogel, enabling light-directed single-cell capture, time-resolved imaging, and the on-demand release of selected cells for downstream gene expression analysis. This approach allows cells to be arrayed at a high density with uniform spacing, facilitating high-throughput monitoring of morphological dynamics. Cells exhibiting phenotypes of interest can be precisely retrieved by localized hydrogel degradation induced by secondary light irradiation and subsequently subjected to single-cell gene expression analysis. Using this workflow in combination with high-throughput real-time image processing technology, we directly link dynamic morphological features to gene expression and demonstrated the ability of the workflow to examine transcriptional alterations associated with invasive cancer cell behavior.

</details>

## Mathematical biology (arXiv)

### [One-Step Self-Assembling Lipopolymer Coatings Enable Direct Longitudinal Biosensing in Native Biological Matrices](https://arxiv.org/abs/2611.27422)
*Pascal R\"uedi, Sarina Seiter, Stephan Handschin et al.* · `q-bio.QM` · arXiv:2611.27422v1 · relevance 0.05

- **In one sentence**: A one-step, self-assembling lipid-polymer (lipopolymer) coating for microfluidic channels that resists non-specific sticking and allows label-free digital holographic detection of tetraspanin-positive extracellular vesicles directly in undiluted serum and lung cancer cell cultures.
- **In plain words**: Biosensors that detect specific molecules in blood or other body fluids often get confused by unrelated material that sticks to their surfaces. This paper describes a simple coating, made from fat-like molecules that assemble themselves in minutes inside a tiny channel, which blocks that sticking and attaches detection probes. The authors used it with a microscope-based system to count and track tiny vesicles released by lung cancer cells over time, using 50 microliters of sample and about 10 minutes, without first purifying the sample.
- **Why it matters**: Being able to watch cells release signalling particles continuously, rather than only at one endpoint, could be useful for cancer research and monitoring. The text claims the coating works on both glass and PDMS (a common clear plastic for microfluidic chips), but the evidence reported here is limited to the abstract, so its general usefulness is not yet established.
- **Background needed**: - Biosensor: a device that detects a target molecule and reports its amount.
- Microfluidics: systems that handle tiny volumes of liquid in channels thinner than a human hair.
- Non-specific binding (fouling): unwanted molecules sticking to a surface and creating false signals.
- Lipopolymer / PEGylated lipid: fat-like molecules with a water-friendly polymer chain that helps repel sticky material.
- Extracellular vesicles: tiny bubbles of membrane that cells release, carrying molecular messages; tetraspanins are surface markers used to identify them.
- Digital in-line holography: imaging that reconstructs 3D particle positions from interference patterns, allowing particle counting without labels.
- Label-free: detection that does not require fluorescent or other tags on the target. · level: research-level

<details><summary>Original abstract</summary>

Sample-driven cross-reactivity remains a fundamental bottleneck for sensitive and selective biosensing in complex biological environments, particularly in microfluidic systems where high surface-to-volumes ratios amplify non-specific interactions. Here, we address this challenge with a one-step, biomimetic surface functionalization strategy based on engineered lipid-based nanocarriers that self-assemble within minutes into immunoassay-ready, antifouling interfaces that couple pegylated-lipid passivation with biorthogonal, site-specific probe conjugation. This approach enables rapid, tuneable, and reproducible surface functionalization, which suppresses sample-specific cross-reactivity even in undiluted serum, and supports direct, label-free digital biosensing assays directly in native biological environments. When integrated into an optofluidic platform combining digital in-line holography and microfluidics, this approach allows time-resolved quantification of tetraspanin-positive extracellular vesicle secretion dynamics from two-dimensional and three-dimensional lung cancer cell models using 50 {\mu}L of sample within 10 min, without isolation or purification. Because the presented surface functionalization proceeds via self-assembly rather than covalent surface modification, this one-step modular-approach is intrinsically decoupled from device fabrication and applies to both glass and PDMS, coating the entire microfluidic channel, thereby establishing a general route for integrating biomimetic nanostructures into robust, high-performance immunoassays, advancing biosensing beyond end-point measurements, and towards rapid and continuous real-time monitoring.

</details>

### [Self-organized fractional silencing of pyramidal neurons under global depolarization in a spatial neuron-glial microcircuit model](https://arxiv.org/abs/2611.27847)
*Stanislav V. Lagosha, Andrey Yu. Verisokin, Darya V. Verveyko et al.* · `q-bio.NC` · arXiv:2611.27847v1 · relevance 0.04

- **In one sentence**: A spatial computational model of a neuron-astrocyte-blood vessel unit shows how inhibitory interneurons lose firing first under high extracellular potassium, how stimulation can fragment a network into self-sustaining active clusters, and how a sufficiently large patch of impaired astrocytic potassium clearance can destabilize surrounding tissue.
- **In plain words**: This paper uses a detailed computer simulation of a small patch of brain tissue to study how seizure-like bursts and spreading waves of electrical shutdown can arise. The authors report that inhibitory cells stop firing sooner than the main excitatory cells as potassium builds up outside them, and that strong stimulation can split the network into small clusters that keep firing at high rates. They also report that a small area of faulty support cells (astrocytes) is compensated by neighbors, but a larger faulty area can lead to lasting pathological activity.
- **Why it matters**: Problems of this kind, such as epileptic discharges and spreading depolarization after stroke or brain injury, are important clinically, and the model suggests a specific size threshold for astrocyte damage that could be tested. The text is a modeling study only, so its predictions are not yet checked against experiments or patient data.
- **Background needed**: - Neurons fire electrical spikes; a "depolarization block" is a state where a neuron is kept so electrically charged that it can no longer fire.
- Excitatory pyramidal neurons drive activity; inhibitory interneurons calm it down. Losing inhibition can tip a network into hyperexcitability.
- Astrocytes are support cells that help clear potassium and glutamate from the space around neurons; their failure can let potassium build up.
- Extracellular potassium and neurotransmitter spill over and diffuse through tissue, linking distant cells.
- The Hodgkin-Huxley formalism is a standard set of equations describing how neuron membranes generate spikes.
- Spreading depolarization is a slow wave of neuronal shutdown that travels through brain tissue after injury. · level: research-level

<details><summary>Original abstract</summary>

Pathological transitions in nervous tissue, including epileptiform discharges and cortical spreading depolarization, depend on the interplay between cellular and interstitial mechanisms. We develop a biophysically detailed two-dimensional model of the neurogliovascular unit (NGVU) integrating neuronal populations in the Hodgkin-Huxley formalism, astrocyte-regulated extracellular potassium dynamics, extracellular neurotransmitter spillover, and noradrenergic neuromodulation. Numerical simulations show that inhibitory interneurons enter depolarization block (DB) at significantly lower extracellular potassium concentrations and stimulation intensities than pyramidal neurons. Early loss of inhibition shifts the local excitation-inhibition balance and triggers network hyperexcitability. In the spatially extended network, exceeding a critical stimulation threshold induces a transition from heterogeneous but spatially uniform firing to network fragmentation into stable active microclusters with self-sustained high-frequency firing. Pyramidal neurons with lower excitatory synaptic input receive less recurrent excitation, which protects them from DB. By continuously releasing potassium ions and glutamate into the extracellular space, pyramidal neurons drive strong depolarization in more densely connected neighbors and push them into deep DB. Simulations of localized astrocytic dysfunction predict a spatial limit for potassium clearance defects. Small damaged cores are fully compensated by diffusion and uptake by surrounding healthy astrocyte units. However, above a critical damage size, activity-dependent potassium buildup and firing positive feedback disrupt homeostasis in surrounding units, promoting persistent depolarized centers with self-sustained, spatially segregated pathological activity.

</details>

## Epidemiology

### [Personal HbA1c trajectories and incident diabetes: association, prediction and observability in the English Longitudinal Study of Ageing](https://www.medrxiv.org/content/10.64898/2026.11.20.26368578v1)
*Tapias, D.; Donati, C.; Völter-Mahlknecht, S.* · `epidemiology` · medRxiv doi:10.64898/2026.11.20.26368578 v1 · relevance 0.08

- **In one sentence**: In English older adults (ELSA), personal HbA1c trajectories were weakly associated with later diabetes and did not improve prediction beyond baseline HbA1c, and a drift model suggests sparse measurements may poorly recover individual slopes.
- **In plain words**: This study asks whether tracking a person's blood sugar marker (HbA1c) over several years predicts who will develop diabetes, better than a single test result. Using repeated measurements from the English Longitudinal Study of Ageing, the researchers found that the personal rate of change was linked to later diabetes after adjustment, but adding these patterns did not clearly make predictions more accurate than the latest test alone.
- **Why it matters**: It matters for how clinicians and researchers use repeated lab results, since a single snapshot is the usual standard. The drift model suggests that natural short-term fluctuations can make individual trends hard to recover from sparse measurements, which may limit how useful lab histories are in practice.
- **Background needed**: - HbA1c: a blood test reflecting average blood sugar over roughly the past two to three months; diabetes is diagnosed when it reaches a set threshold.
- ELSA: a long-running study of people aged 50 and over in England, with repeated health measurements.
- Incident diabetes: diabetes newly diagnosed during follow-up.
- Linear mixed model: a statistical method that estimates each person's typical level and rate of change while accounting for repeated measures.
- Odds ratio (OR) per SD: how much the odds of developing diabetes change for each standard-deviation increase in a measure; 1 means no effect.
- AUC: a 0–1 score of how well a test separates people who will and will not develop the condition; differences near zero mean no real gain.
- Transformer: a machine-learning model architecture, here trained to learn patterns from the sequence of measurements.
- Ornstein–Uhlenbeck process: a model of random fluctuations that drift around a level and are correlated over time.
- Cross-fitting: a validation approach where model parameters are estimated on other participants to avoid overfitting. · level: research-level

<details><summary>Original abstract</summary>

Background. Clinical diagnosis often relies on a snapshot: a single measurement interpreted against a population threshold. Repeated (longitudinal) measurements, however, may reveal an individual's typical level and how it changes over time. Extracting this information is challenging when measurements are sparse and biological fluctuations may resemble sustained changes. Using data from the English Longitudinal Study of Ageing (ELSA), we investigated whether individual glycated haemoglobin (HbA1c) trajectories improved the prediction of incident diabetes beyond the most recent measurement, whether they were associated with incident diabetes, and how reliably they could be estimated. Methods. In this secondary analysis of a prospective cohort study, we analysed venous HbA1c measured approximately every four years in ELSA, with a longer final interval of about seven years. A linear mixed model estimated each person's usual HbA1c level and rate of change (personal slope) from their measurements before each diabetes-free health visit, with model parameters estimated in other participants (cross-fitting). We derived four longitudinal features: deviation from the person's usual level, personal slope, change since the last measurement, and the forecast probability that the next HbA1c reaches the diagnostic threshold for diabetes. We evaluated the associations of these features with incident diabetes and their incremental predictive value beyond baseline HbA1c and clinical risk factors in internal, cross-fitted validation, compared predictive performance with a self-supervised Transformer, and modelled within-person variation as serially correlated drift (an Ornstein-Uhlenbeck process) to assess how reliably personal slopes can be recovered under different measurement schedules. Results. The analysis included 5,828 diabetes-free baseline visits from 3,603 participants, of which 234 were followed by incident diabetes. Neither the engineered longitudinal features nor a Transformer that also used additional clinical variables improved discrimination beyond baseline HbA1c and clinical risk factors (difference in the area under the receiver operating characteristic curve, {Delta}AUC, -0.002 to +0.010; all 95% confidence intervals [CIs] including zero). The estimated personal slope was nevertheless associated with incident diabetes after adjustment for baseline HbA1c, age and other clinical factors (odds ratio [OR] per standard deviation [SD] 1.18, 95% CI 1.02--1.36, and 1.39, 1.11--1.74, among visits with at least two earlier HbA1c values), whereas deviation from the person's usual level was not (OR 0.99, 95% CI 0.81--1.21). In the drift model, serially correlated fluctuations accounted for 77--81% of residual within-person variance, although the estimated temporal structure was sensitive to the treatment of the first HbA1c values at or above the diagnostic threshold. Under this model, persistent individual trends were difficult to distinguish from slowly varying fluctuations: with the intercept-slope correlation set to zero, estimated and underlying slopes correlated weakly for four-yearly measurements over up to 12 years (r [&le;] 0.26), and more frequent measurements improved this little. Conclusions. Estimated personal HbA1c slopes carried adjusted prognostic information beyond baseline HbA1c and clinical factors, but longitudinal features, including those learned by a Transformer, did not clearly improve prediction. The drift model suggests that slowly varying within-person fluctuations may limit the reliable estimation of individual slopes from sparse measurements, and that longer observation histories are more informative than more frequent measurement. Whether personal laboratory histories improve prediction depends not only on their association with disease, but also on how reliably individual change can be recovered from the available measurements.

</details>

### [Depressive Symptom Trajectories and Incident Cognitive Impairment by Outcome Ascertainment](https://www.medrxiv.org/content/10.64898/2026.11.18.26368449v1)
*Liu, X. L.; Guo, Z. L.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368449 v1 · relevance 0.07

- **In one sentence**: In four harmonized aging cohorts (CHARLS, HRS, ELSA, SHARE; n = 91,043), associations between depressive symptom trajectories and incident cognitive impairment strengthened stepwise as outcome ascertainment moved from self-report to clinical consensus diagnosis.
- **In plain words**: Researchers asked whether depression really raises the risk of memory and thinking decline in older adults, or whether the answer depends on how that decline was measured. They followed about 91,000 people over age 50 in four countries' long-running studies and grouped them by how their depressive symptoms changed over time. The link looked weak or inconsistent when cognitive problems were judged by self-report, and stronger when a clinical team made the diagnosis.
- **Why it matters**: Depression is often named as a modifiable risk factor for dementia, and cohort estimates of its size vary a lot. The paper suggests that part of that variation may come from how outcomes are measured, which bears on how prevention trials and burden estimates are designed; the authors' claim that self-report may underestimate treatment benefit is a reasoned inference from their data, not something directly tested in a trial.
- **Background needed**: - Cohort study: following a large group of people over time and recording who develops an outcome.
- Depressive symptom trajectories: groups of people whose depression scores follow similar paths (e.g., persistently low, persistently high, getting worse, or improving).
- Incident cognitive impairment: new memory or thinking problems arising during follow-up.
- Ascertainment rigor: how carefully a case is identified, ranging from a simple self-report question to a full clinical expert diagnosis (the Harmonized Cognitive Assessment Protocol is a detailed in-person assessment).
- Hazard ratio (HR) and odds ratio (OR): ways of expressing how much more likely the outcome is in one group versus a reference group; values above 1 mean higher risk.
- Meta-analysis and meta-regression: combining results across cohorts, and testing whether a study-level factor (here, rigor) explains differences between them.
- Competing risk and lagged analyses: checks that account for death before diagnosis and for early reverse causation. · level: research-level

<details><summary>Original abstract</summary>

Importance: Dementia prevention frameworks treat depression as a leading modifiable risk factor, but cohort estimates of the association vary widely; whether this variation reflects how cognitive outcomes are ascertained is unknown. Objective: To examine whether associations between depressive symptom trajectories and incident cognitive impairment vary by outcome ascertainment rigor. Design, Setting, and Participants: This harmonized cohort study included 91,043 adults aged 50 years or older from 4 national longitudinal aging cohorts (CHARLS [China], HRS [US], ELSA [England], and SHARE [16 European countries]); baseline waves spanned 2006 to 2011, with follow-up through 2023. Exposure: Depressive symptom trajectory classes (persistent low, persistent high, incident worsening, remitting) derived using group-based trajectory modeling. Main Outcomes and Measures: Incident cognitive impairment ascertained under a 5-level hierarchy of increasing rigor, from self-report (level 1) to clinical consensus diagnosis (level 5; Harmonized Cognitive Assessment Protocol [HCAP]). Cohort-specific Cox models were pooled by random-effects meta-analysis; meta-regression tested ascertainment rigor as a moderator of heterogeneity. Results: Under nonadjudicated outcomes, the incident-worsening trajectory was associated with incident cognitive impairment in CHARLS (HR, 1.31; 95% CI, 1.06-1.62) and SHARE (HR, 1.99; 95% CI, 1.87-2.13) but not HRS (HR, 1.05; 95% CI, 0.95-1.16) or ELSA (HR, 1.10; 95% CI, 0.95-1.27); the persistent-high trajectory was not significant under any nonadjudicated outcome (HR range, 1.07-1.15). Under clinical consensus diagnosis (n = 3,196), all non-low trajectories were independently associated with mild cognitive impairment or dementia (OR range, 1.66-2.29; dementia-only persistent high: OR, 3.32; 95% CI, 1.85-5.95). Effect sizes increased stepwise with ascertainment rigor (meta-regression slope, 0.314 log HR per level; P < .001; residual I2 = 0%; R2 = 100%; exploratory). Findings were robust to lagged, weighted, and competing-risk analyses; biological aging acceleration did not differ across trajectories. Conclusions and Relevance: The detectability and magnitude of depression-related cognitive risk depend on outcome ascertainment rigor. Prevention trials and burden projections relying on self-reported outcomes may underestimate the benefit of depression treatment.

</details>

## Infectious diseases

Nothing notable this time.

## Public and global health

### [Additional Vascular Imaging in Women With Acute Cerebral Ischemia: Thresholds for Cost-Effectiveness](https://www.medrxiv.org/content/10.64898/2026.11.19.26368544v1)
*Boettger, P.; Klug, J.; Agarwal, A. et al.* · `health economics` · medRxiv doi:10.64898/2026.11.19.26368544 v1 · relevance 0.09

- **In one sentence**: A decision-tree and lifetime state-transition model estimates how often extra intracranial vascular imaging plus timely thrombectomy in women with acute cerebral ischemia would need to yield treatments to be cost-effective in Ontario and under US Medicare.
- **In plain words**: This paper looks at stroke caused by a blocked blood vessel in the brain, where women are less often given detailed scans of those vessels than men. The authors asked how many extra scans would need to lead to a clot-removal procedure, and how much benefit it would need to give, for the added cost to be worth paying. They found that about one extra treatment per 48 scans in Ontario (or one per 57 under Medicare) would meet the usual cost-effectiveness bar, under their assumptions.
- **Why it matters**: It gives health planners a concrete set of conditions to test a possible change in care for women, which matters because outcomes after stroke differ by sex. The results are conditional: they depend on modelled long-term outcomes and on assumed costs, and the text calls for prospective studies to check them.
- **Background needed**: - Acute cerebral ischemia: a stroke caused by a blocked blood supply to part of the brain.
- Intracranial vascular imaging: scans of the blood vessels inside the skull, used to find the blockage.
- M1 occlusion: a blockage in a major artery in the brain (the middle cerebral artery).
- Endovascular thrombectomy (EVT): a catheter procedure that mechanically removes the clot through the blood vessels.
- HERMES: a pooled set of earlier clinical trials of thrombectomy, used here as the source of treatment effect.
- Modified Rankin Scale: a 0–6 scale of disability after stroke; the study tracks how many people end up functionally independent.
- Cost-effectiveness threshold: the maximum price per quality-adjusted life-year (a measure combining length and quality of life) that a health system is willing to pay, here CAD 50,000 or USD 100,000.
- Decision tree and state-transition model: standard modelling tools that simulate patients' paths through treatment and health states over time. · level: research-level

<details><summary>Original abstract</summary>

Background: Women with acute cerebral ischemia receive intracranial vascular imaging less often than men, but the value of expanding imaging is uncertain. We estimated the treatment rates and functional benefits required for additional imaging to be cost-effective. Methods: We developed a decision tree and state-transition model comparing additional imaging followed by timely endovascular thrombectomy (EVT) for M1 occlusion with current care from Ontario public-payer and US Medicare perspectives. Women-specific 90-day modified Rankin Scale distributions from HERMES were projected over a lifetime. We jointly varied the proportion of additional scans leading to additional timely EVT and the treatment effect relative to HERMES. Cost-effectiveness thresholds were CAD 50,000 and USD 100,000 per quality-adjusted life-year. Program costs represented health-care resources in Ontario and additional payments under Medicare. Results: At variable program costs of CAD 1,000 or USD 1,000 per additional scan, assuming the full HERMES effect and no additional fixed costs or pathway-related harm, expected cost-effectiveness required one additional timely EVT per 48 scans in Ontario and 57 under Medicare (2.07% and 1.74%, respectively). Treatment rates of 3.07% and 2.65% were required for a 90% probability of cost-effectiveness under these assumptions. At three additional thrombectomies per 100 scans and the same costs, treatment effects had to reach 76.9% and 67.3% of the HERMES effect. With the full effect, 1,000 additional scans at this treatment rate yielded approximately 5 additional functionally independent survivors at 90 days. Deterministic analyses restricted to 5 years increased the required treatment rates to 4.44% and 4.22%. Conclusions: Additional vascular imaging in women could be cost-effective when a small proportion of scans leads to timely thrombectomy, provided sufficient functional benefit is retained. Prospective evaluations should assess additional treatment opportunities, functional outcomes and program costs against these conditional thresholds, which depend on projected long-term outcomes.

</details>

### [Enhancing Access to and Utilization of Maternal and Child Health Service through Implementation of a District-led Integrated Mobile Health Service Delivery Model in Pastoral Ethiopia: A Multi-Method Implementation Research](https://www.medrxiv.org/content/10.64898/2026.11.18.26368458v1)
*Semahegn, A.; Belete, M.; Tiruneh, G. T. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.18.26368458 v1 · relevance 0.07

- **In one sentence**: A multi-method implementation study with a non-randomized quasi-experimental design (difference-in-differences) evaluates a district-led mobile health service model for maternal, newborn and child care in four pastoralist woredas of Ethiopia, using DHIS2 routine data and 143 interviews.
- **In plain words**: Many nomadic and semi-nomadic communities in Ethiopia live far from clinics, so they often miss routine care for pregnancy, newborns and young children. This study tested a model where mobile teams, planned with local officials and community members, visited remote villages monthly to offer a range of health services. The authors report that over one year the mobile service reached about 79,400 people in 20 hard-to-reach villages, and that antenatal care use and vaccination coverage rose in the study areas.
- **Why it matters**: Access gaps for mobile and remote populations are a persistent problem in sub-Saharan Africa, and this paper gives a concrete, locally planned example of a response. The design is non-randomized, so the comparison groups may differ in ways the study cannot fully control, and the text gives limited detail on the size of the effects, so the findings should be read as suggestive rather than settled.
- **Background needed**: - Pastoralists are communities that move with livestock, so fixed clinics are hard for them to use.
- Woreda is the district-level administrative unit in Ethiopia.
- Antenatal care (ANC) is health checks during pregnancy; penta-3 is the third dose of a five-in-one childhood vaccine.
- DHIS2 is a national routine health information database.
- Difference-in-differences is a method that compares change over time between a program area and a comparison area.
- Quasi-experimental means a study that tests an intervention without random assignment of who receives it.
- Implementation research studies how a program is delivered in practice, not only whether it works in principle. · level: intermediate

<details><summary>Original abstract</summary>

Introduction: Lack of access to essential health services has remained a significant public health challenge in sub-Saharan Africa. The conventional health service delivery models often fail to account for the mobility patterns and socio-cultural values of these communities. These communities are frequently affected by recurrent droughts, conflicts, floods, and disease outbreaks. This study assessed the contribution of a mobile health services (MHS) delivery model designed to improve access to and utilisation of maternal, neonatal, and child health services in pastoralist contexts of Ethiopia. Methods: A multi-method embedded implementation research with a non-randomized controlled quasi-experimental study design was employed in four selected Woredas of Ethiopia. Baseline data from July 2022 to June 2023 and endline data from July 2023 to June 2024 were extracted from DHIS2. The MHS delivery model was co-designed with stakeholders, redefined communitycentred outreach sites, and established a multidisciplinary team, that was implemented monthly. The average distance between the health facility and the centre of the targeted community village was 29.6 kilometres. Data were captured from routine health service records, MHS databases, and program reports, and 143 in-depth interviews among service providers and beneficiaries. Quantitative data were analysed using descriptive statistical methods and difference-indifferences using Stata 18, while qualitative data were coded and analysed using ATLAS.ti. Results: During the twelve months, the MHS reached 79,404 people through 190 sessions held and offered an integrated essential health service in 20 hard-to-reach villages. In the study area, ANC use was 64.0% in Chifra and 75.6% in Dasenech. In addition, penta-3 antigen vaccination improved from 66.0% to 69.7% in Chifra and from 91.2% to 102.1% in Dasenech, respectively. In the difference-indifferences analysis, the MHS significantly enhanced access to ANC follow-up and completion of pentavalent and full vaccination coverage. A Woreda-led approach, community engagement, context-tailored and timely communication, and comprehensive service delivery by a multidisciplinary team enhanced the use and acceptability of the MHS in the pastoral setting. The contribution of MHS to ensuring access and use of MNCH services ranged from 13.0% to 19.1% for continuing family planning and antenatal care, respectively. Conclusions: The study highlights that the MHS delivery model is a suitable platform that has substantially contributed to improving access to and use of maternal, newborn, and child health services in pastoral, agropastoral, and scattered settlements. Being a woreda-led, participatory codesign, community-centred approach, and context-tailored health service delivery approach enhanced the acceptability and effectiveness of the MHS in reaching the underserved community. Integration of MHS with the existing PHC system, with an innovative, sustainable financing mechanism, is recommended to ensure access and use of MNCH in hard-to-reach settings.

</details>

## Psychiatry and neurology

### [Cycle-based neurostimulation for control of circadian brain network dynamics in human epilepsy](https://www.medrxiv.org/content/10.64898/2026.11.19.26368528v1)
*Saboo, K. V.; Fan, J. M.; Tadayon, E. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368528 v1 · relevance 0.14

- **In one sentence**: Longitudinal ECoG study in bitemporal epilepsy reporting that circadian alignment of hippocampal connectivity rhythms predicts responsive neurostimulation seizure reduction, modeled with a nonlinear Kuramoto oscillator and in-silico stimulation timing optimization.
- **In plain words**: This paper looks at whether the body's daily clock affects how well brain stimulation works for epilepsy. The researchers recorded brain activity over months from people with seizures starting in both temporal lobes, and found that when the daily activity rhythms of the left and right hippocampus lined up more closely, patients had more seizure reduction. They also report that the timing of stimulation during the day relates to how these rhythms changed over months, and that a computer model suggested adjusting stimulation timing could improve that alignment.
- **Why it matters**: Most brain stimulation treatments ignore time of day, so showing that daily rhythms carry information about treatment response could matter for personalizing therapy. The text only supports this as a possible direction: the results come from a small clinical recording setting and a computer model, and the authors frame the wider applications (other neurological and psychiatric disorders) as opportunities rather than demonstrated results.
- **Background needed**: - Epilepsy: a condition with recurrent seizures; here it originates in the temporal lobes on both sides.
- Responsive neurostimulation: a device that senses brain activity and delivers electrical pulses when it detects a seizure risk.
- Electrocorticography (ECoG): recording electrical activity from electrodes placed on or in the brain, used clinically.
- Hippocampus: a brain region important for memory and involved in seizure spread; the paper compares left and right sides.
- Circadian rhythm: roughly 24-hour biological cycle, such as sleep-wake timing.
- Connectivity: how strongly different brain regions' activity is coordinated over time.
- Kuramoto oscillator model: a mathematical model of many rhythmic units that drift toward or away from synchrony; used here to describe coupled rhythms.
- Control theory: the field of steering a system's behavior by choosing inputs, here stimulation timing.
- In silico: performed by computer simulation rather than in patients. · level: research-level

<details><summary>Original abstract</summary>

Biological rhythms modulate symptoms of brain disorders, yet brain stimulation therapies largely overlook the temporal organization of pathological brain states. Harnessing these rhythms could improve therapeutic efficacy. Here, we show that circadian coordination of hippocampal network connectivity is a biomarker of therapeutic response to responsive neurostimulation in epilepsy. Using longitudinal electrocorticography from individuals with bitemporal epilepsy, we find that alignment of circadian connectivity rhythms between the left and right hippocampus predicts seizure reduction. The daily distribution of stimulation also predicts how these rhythms evolve over months. We capture these dynamics using a nonlinear Kuramoto oscillator model and demonstrate that optimizing stimulation timing in silico can improve predicted circadian network alignment. Our findings establish a cycle-based, control-theoretic framework for modelling and potentially reshaping brain network rhythms, offering new opportunities for personalized neurostimulation in epilepsy and other neurological and psychiatric disorders.

</details>

### [Carotid Artery Stenosis is Associated with Restless Legs Syndrome in the Absence of Stroke](https://www.medrxiv.org/content/10.64898/2026.11.17.26368361v1)
*Ogulnick, J. V.; Shin, W.; Mathew, J.* · `neurology` · medRxiv doi:10.64898/2026.11.17.26368361 v1 · relevance 0.11

- **In one sentence**: A TriNetX retrospective propensity-matched case-control study (58,382 per arm) finds bilateral internal carotid artery stenosis/occlusion (ICD-10 I65.23) associated with a small increase in restless legs syndrome diagnosis (G25.81) versus atherosclerosis without carotid stenosis (adjusted OR 1.09, 95% CI 1.002-1.186).
- **In plain words**: Restless legs syndrome is a condition that causes an urge to move the legs, often at night. This study asked whether people with severe narrowing or blockage of the large arteries in the neck that supply the brain are more likely to receive that diagnosis, even without having had a stroke. Among about 58,000 matched pairs in a large health-records database, the narrowed-artery group had a slightly higher rate of the diagnosis (1.98% vs 1.82%).
- **Why it matters**: If a reduced blood supply to brain movement circuits contributes to restless legs, this could point to a vascular cause for some cases, but the effect is very small and the study cannot show cause. It is worth attention mainly as a hypothesis to test in prospective studies, including whether treating the arteries changes symptoms.
- **Background needed**: - Restless legs syndrome (RLS): a common neurological condition with an uncomfortable urge to move the legs, often worse at rest or at night.
- Internal carotid artery stenosis (CAS): narrowing of the main arteries in the neck that carry blood to the brain; ICD-10 codes are standard diagnosis labels used in medical records.
- Atherosclerosis: hardening and narrowing of arteries from fatty plaque buildup.
- Retrospective case-control study: looks back at existing records, comparing people with and without a condition.
- Propensity score matching: pairs patients with similar characteristics so groups are more comparable, though unmeasured differences can remain.
- Odds ratio (OR): a measure of how much more likely an outcome is in one group; 1.09 means roughly 9% higher odds, a small effect.
- Confidence interval: the range of values consistent with the data; here the lower bound sits very close to 1.
- Dopaminergic pathways: brain circuits using dopamine, thought to be involved in RLS. · level: research-level

<details><summary>Original abstract</summary>

Background: Restless legs syndrome (RLS) is a common neurological disorder with established links to atherosclerotic disease and secondary causes such as ischemic stroke. Hypothesizing that internal carotid artery stenosis (CAS) could induce secondary RLS through chronic hypoperfusion or microemboli to dopaminergic subcortical structures, even without overt stroke, we investigated the association between bilateral CAS and RLS. Methods: A retrospective propensity score-matched case-control study was conducted using the TriNetX Global Health Research Network. Cases (n=58,382) had bilateral CAS/occlusion (ICD-10-CM I65.23); controls (n=58,382) had atherosclerosis without CAS. Patients were excluded for prior stroke/TIA, iron deficiency, antipsychotic use, and other secondary RLS causes. Cases and controls were 1:1 matched on age, race/ethnicity, chronic kidney disease, peripheral neuropathy, peripheral artery disease, Parkinson's disease, and SSRI use. The outcome was RLS diagnosis (G25.81), assessed via conditional logistic regression. Results: RLS was diagnosed in 1,154 (1.977%) patients with bilateral CAS/occlusion versus 1,060 (1.816%) controls, yielding an absolute risk difference of 0.161% (95% CI 0.005-0.317%; p=0.0437). The adjusted odds ratio was 1.09 (95% CI 1.002-1.186), indicating a modest but significant association. Conclusion: Severe bilateral CAS/occlusion is associated with a small but statistically significant increase in RLS risk, independently of overt cerebrovascular events and known confounders. These findings support a potential vascular contribution to RLS pathogenesis, possibly through subclinical hypoperfusion affecting basal ganglia dopaminergic pathways. Prospective studies are needed to explore causality, dose-dependency, and the impact of carotid revascularization.

</details>

## Oncology

### [Panel-agnostic tumour-only diagnosis of mismatch repair deficiency](https://www.medrxiv.org/content/10.64898/2026.11.19.26368513v1)
*Garcia-Lopez, D.; Hernando, B.; Chaves-Urbano, B. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.19.26368513 v1 · relevance 0.08

- **In one sentence**: A tumour-only classifier (captureMMRd) that infers mismatch repair deficiency from mutational signatures in somatic variant calls that targeted panels already produce, validated against IHC and MSI-PCR across 7,514 samples from 16 cohorts.
- **In plain words**: Some cancers lose a DNA repair system called mismatch repair, and those tumours often respond to immunotherapy, so finding them matters. This paper describes a computer method that spots this loss using only the tumour's own mutation data, the kind of data that routine gene-panel tests already generate, without needing a matched healthy sample. In a pooled set of 7,514 samples, the authors report it agreed with standard lab tests in most cases, with pooled sensitivity of 94.36% and specificity of 99.02%.
- **Why it matters**: Many hospitals test tumours with targeted gene panels that lack the extra information older methods need, so a method that works on existing data could widen access to immunotherapy decisions. The text reports the accuracy figures and a minimum panel size, but the clinical impact has not been tested in the paper itself.
- **Background needed**: - Mismatch repair (MMR) is a cell system that fixes copying errors in DNA; when it fails (MMRd), mutations pile up.
- MMRd tumours can qualify for immunotherapy, so detecting them guides treatment.
- Standard confirmatory tests are immunohistochemistry (IHC, staining for repair proteins) and MSI-PCR (checking unstable short repeated DNA sequences).
- Targeted panels sequence only a selected set of genes; "tumour-only" means no matched normal tissue from the same patient is sequenced.
- Mutational signatures are patterns in the types of mutations a tumour carries, used here as the classifier's input.
- Sensitivity is the share of true cases detected; specificity is the share of non-cases correctly ruled out. · level: research-level

<details><summary>Original abstract</summary>

A diagnosis of mismatch repair deficiency (MMRd) can unlock immunotherapy treatment for a patient. However, existing sequencing-based detection methods require matched normal samples, panel-specific baselines or dedicated microsatellite loci, none of which are available to the tumour-only targeted panels that dominate routine clinical practice. Here we present captureMMRd, an open-source classifier that diagnoses MMRd using mutational signatures computed from the somatic variant calls any panel already produces. Applying a single locked model to 7,514 samples from 16 independent cohorts, spanning whole-exome, whole-genome, targeted panel and plasma cfDNA sequencing, captureMMRd achieved a pooled sensitivity of 94.36% and specificity of 99.02% against orthogonal MMR IHC and MSI-PCR testing, and outperformed microsatellite-based callers on panels with limited microsatellite content. We demonstrate that as few as 3 indels and 44 single-base substitutions are sufficient for reliable diagnosis, defining a minimum panel footprint that most clinically deployed assays already exceed. Our findings extend clinically actionable MMRd detection to the sequencing workflows of routine precision oncology, with the potential to broaden patient access to immunotherapy without new assays, baselines or matched normal samples.

</details>

### [Baseline Prognosis and Treatment Benefit From First-Line Immunotherapy Strategies: Target Trial Emulations Across Advanced Solid Tumors](https://www.medrxiv.org/content/10.64898/2026.11.20.26368610v1)
*Orcutt, X.; Nimgaonkar, V.; Chen, K. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.20.26368610 v1 · relevance 0.07

- **In one sentence**: A target-trial emulation using Flatiron Health electronic records (8,688 patients, 2011–2023) tests whether baseline prognosis, estimated by machine learning 6-month survival models, modifies the benefit of first-line immunotherapy-based strategies across five advanced solid tumor comparisons.
- **In plain words**: Immunotherapy drugs are often chosen for frail cancer patients because they seem gentler, yet some trials have shown more early deaths with them than with chemotherapy-based regimens. This study used routine hospital records from US patients to ask whether the better treatment choice depends on how sick a patient is at the start. It found that for poorer-prognosis patients in head and neck, bladder (urothelial), and possibly lung cancer, adding chemotherapy gave more benefit, while immunotherapy-based treatment helped across risk levels in colorectal cancer and melanoma.
- **Why it matters**: Trials often under-enroll patients with poor prognosis, so this suggests treatment comparisons from trials may not transfer to these patients, and that baseline risk could complement tumor biomarkers such as PD-L1 when choosing therapy. Because it is an observational emulation, the findings are associations that need confirmation, and the lung cancer result was less certain (confidence interval crossing zero).
- **Background needed**: - Immune checkpoint inhibitors (ICIs): drugs that release the immune system's brake so it attacks cancer; pembrolizumab and nivolumab/ipilimumab are examples.
- Target trial emulation: analyzing observational patient records as if they were a randomized trial, to reduce bias.
- Flatiron Health: a US database of electronic health records from oncology clinics.
- PD-L1 (CPS/TPS): lab markers of tumor immune activity used to guide immunotherapy use.
- Restricted mean survival time (RMST): average survival time over a fixed window (here 2 years), expressed in days in this paper.
- Interaction test: checks whether a treatment effect differs across patient groups or risk levels.
- Overlap weighting and pseudo-observations: statistical methods to balance comparison groups and model survival outcomes.
- dMMR/MSI-H: tumors with defects in DNA mismatch repair, often responsive to immunotherapy.
- BRAF/MEK inhibitors: targeted pills for melanoma with a BRAF mutation. · level: research-level

<details><summary>Original abstract</summary>

Background In randomized trials, first-line immune checkpoint inhibitor (ICI)-based therapy has shown excess early mortality versus chemotherapy- or targeted therapy-containing regimens. ICI monotherapy is often chosen for frail patients because it is perceived as less toxic. Whether treatment benefit varies with baseline prognosis is unknown, as poor-prognosis patients are underrepresented in trials. Methods Using the US Flatiron Health electronic health record-derived database, we emulated target trials among 8,688 patients initiating first-line therapy during 2011-2023 across five comparisons: pembrolizumab plus chemotherapy versus pembrolizumab in head and neck squamous cell carcinoma (HNSCC; PD-L1 CPS [&ge;] 1 or unknown) and non-small cell lung cancer (NSCLC; PD-L1 TPS [&ge;] 50%); carboplatin plus gemcitabine versus pembrolizumab in urothelial carcinoma; pembrolizumab versus chemotherapy in dMMR/MSI-H colorectal cancer; and ipilimumab plus nivolumab versus BRAF/MEK inhibition in BRAF-mutant melanoma. Baseline prognosis was estimated with machine learning models predicting 6-month survival. Overlap-weighted pseudo-observation regression evaluated whether differences in 2-year restricted mean survival time (RMST) varied with predicted survival. Results In HNSCC, adding chemotherapy to pembrolizumab did not clearly improve RMST overall (11.5 days; 95% CI, -18.4 to 41.1), but benefit was 102.4 days greater at the 10th versus 90th percentile of predicted survival (95% CI, 40.5 to 164.3; interaction P=.001). Similar gradients favored carboplatin plus gemcitabine over pembrolizumab in urothelial carcinoma (10th-90th percentile difference, 51.4 days; 95% CI, 4.8 to 98.1; P=.03) and, less certainly, adding chemotherapy to pembrolizumab in NSCLC (73.7 days; 95% CI, -3.7 to 151.2; P=.06). Higher-risk patients in these cohorts were more often trial-ineligible. ICI-based therapy improved overall RMST in colorectal cancer (difference, 79.7 days; 95% CI, 49.5 to 107.0) and melanoma (68.3 days; 95% CI, 33.9 to 101.9), without clear variation by predicted survival (interaction P=.32 and P=.91). Conclusions Among patients with poorer prognosis, chemotherapy-containing regimens were associated with greater benefit than ICI monotherapy in HNSCC and urothelial carcinoma, and possibly NSCLC. ICI-based therapy appeared beneficial across prognosis in dMMR/MSI-H colorectal cancer and BRAF-mutant melanoma. Baseline prognosis may complement tumor biomarkers when selecting first-line immunotherapy strategies.

</details>

## Health informatics and medical AI

### [Interpretable competing-risk prediction of hepatocellular carcinoma in cirrhosis from region-wide routine health data](https://www.medrxiv.org/content/10.64898/2026.11.19.26368516v1)
*Gutierrez-Alvarez, I.; Rojas, A.; Calzadilla-Bertot, L. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368516 v1 · relevance 0.12

- **In one sentence**: A three-class, interpretable Explainable Boosting Machine trained on one year of routine electronic health records predicts 12-month hepatocellular carcinoma (liver cancer) in cirrhosis while separating competing deaths and liver transplants, and outperformed aMAP and the Toronto HCC Risk Index in a region-wide Andalusian cohort.
- **In plain words**: Some people with cirrhosis (scarring of the liver) develop liver cancer, but others die or receive a transplant first, which makes predicting cancer harder. The researchers built a transparent computer model using a year of routine health records from a region of Spain, and asked it to sort each patient's next year into liver cancer, death or transplant without cancer, or neither. It predicted liver cancer better than two established risk scores, and it showed whether each abnormal test result pointed toward cancer or toward liver failure.
- **Why it matters**: Earlier risk scores ignore the chance that a patient dies of liver disease before cancer appears, which can mislead decisions about who needs closer surveillance. The text reports better discrimination and fewer competing deaths in the high-risk group, but these are retrospective analyses of one regional database, so whether this improves patient care in practice is untested here.
- **Background needed**: - Cirrhosis: late-stage scarring of the liver, a major risk factor for liver cancer (hepatocellular carcinoma, HCC).
- Competing risk: when another event (such as death from liver failure) can stop the outcome of interest from happening, so it must be modelled separately.
- AUROC / concordance: a 0 to 1 score of how well a model ranks patients who will have an event above those who will not; 0.5 is chance.
- aMAP and Toronto HCC Risk Index: existing clinical scores that estimate liver cancer risk.
- Explainable Boosting Machine: a machine-learning method built from simple per-variable curves, so each input's effect can be read directly.
- Cross-validation: testing a model repeatedly on held-out subsets of the data to estimate how it will generalise.
- Routine health data: records collected during normal care, such as diagnoses and blood tests, not data from a trial. · level: research-level

<details><summary>Original abstract</summary>

Background. Short-term prediction of hepatocellular carcinoma (HCC) in cirrhosis is complicated by the competing risk of death from liver disease. We aimed to develop an interpretable model on region-wide routine data that predicts HCC while separating competing mortality, and to compare it with established risk scores. Methods. From a region-wide cohort of adults with cirrhosis in the Andalusian Population Health Database, we trained the model on 17,177 patients with a prediction date set 12 months before their outcome, between 2020 and 2023. From one year of electronic health records before that date (demographics, liver and chronic disease codes, and eight routine laboratory tests), an Explainable Boosting Machine without interaction terms classified the following 12 months as HCC, death or liver transplantation without HCC, or event-free. We evaluated it in 20 repeats of 5-fold cross-validation against a binary model, a model with pair interactions and a model using the full health record, all on the same folds. We then applied the cross-validated models, without retraining, at the first routine encounter at which aMAP or the Toronto HCC Risk Index could be computed, and compared them with the scores in patients followed forward under competing risks, with and without a 6-month washout and with each province left out of training in turn. Findings. 771 patients (4.5%) developed HCC within 12 months and 3,314 (19.3%) died or underwent liver transplantation without HCC (3,061 deaths, 253 transplants). In cross-validation, the area under the receiver operating characteristic curve (AUROC) for HCC was 0.734 (SD 0.018). A binary formulation, pairwise interactions and the full health record (more than 3,000 features) did not improve it; the full record lowered it by 0.024. At routine encounters the model discriminated 12-month HCC better than aMAP (time-dependent AUC 0.790 vs 0.688; difference +0.102, 95% CI +0.071 to +0.132) and the Toronto HCC Risk Index (0.761 vs 0.703; +0.057, +0.032 to +0.081), and remained better after excluding HCC diagnosed within 6 months (concordance difference +0.055 and +0.040) and when each of the eight provinces was left out of training. At equal group size, its high-risk group held as much HCC as the scores' high-risk categories, with 20-28% fewer competing deaths. Its shape functions separated cancer-specific signal (AFP rising from 2 to 20 g/L, platelets below 150 x10^9/L) from liver failure (bilirubin above 51 mol/L, albumin below 35 g/L); a binary model showed only the first. Interpretation. An interpretable three-class model on routine data outperformed established scores for short-term HCC risk in cirrhosis, while showing whether each abnormal value points to cancer or to competing death.

</details>

### [Unified Machine Learning Model for Early Detection of Mild Cognitive Impairment, Frailty, and Fall Risk Using Multimodal Motor-Function Data](https://www.medrxiv.org/content/10.64898/2026.11.19.26368462v1)
*Akter, S.; Guess, T.; Sarker, S. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368462 v1 · relevance 0.09

- **In one sentence**: A small study (n=79 community-dwelling older adults) trains a single multi-label machine learning model on sensor-based motor tests to predict mild cognitive impairment, frailty, and fall risk together, and compares it with separate single-condition models.
- **In plain words**: Older adults often have memory decline, physical frailty, and a higher risk of falls at the same time, and these conditions are usually screened separately. This study tested whether one computer model could estimate all three from a single set of movement tests (walking, standing up from a chair, balance, stepping, and reaction time) recorded with sensors. The unified model did about as well as three separate models, with the best accuracy for memory impairment and weaker accuracy for frailty and fall risk.
- **Why it matters**: The idea of screening several age-related conditions from one short assessment could make checkups more efficient if it holds up. The authors are measured about this: the sample is small, the model overestimated risk for all three outcomes, and fall-risk prediction was weak, so it needs recalibration and testing in other groups before any practical use.
- **Background needed**: - Mild cognitive impairment (MCI): noticeable memory or thinking decline that is not severe enough to be dementia.
- Frailty: a state of physical weakness and reduced reserve that raises vulnerability to health problems.
- Fall risk: the likelihood that a person will fall, often judged from balance and gait.
- Machine learning classifier: a model that learns from example data to sort people into groups (here, at risk or not).
- Multi-label classification: predicting several yes/no conditions at once for the same person.
- AUC (area under the ROC curve): a 0.5 score is chance and 1.0 is perfect separation of cases from non-cases; here the overall score of 0.645 is modest.
- Cross-validation: testing a model on data held out from training, repeated to estimate reliability.
- SHAP: a method that shows how much each input feature pushes a prediction up or down.
- Dual-task testing: performing a movement while doing a second mental task, which often reveals hidden problems. · level: research-level

<details><summary>Original abstract</summary>

Background: Mild cognitive impairment (MCI), frailty, and fall risk often co-occur in older adults and share motor signs, yet they are screened and modeled separately. A unified model that predicts all 3 conditions from 1 sensor-based assessment could support earlier and more efficient screening, but such a model has rarely been developed or rigorously compared with separate models. Objective: This study aimed to develop a unified machine learning model that predicts MCI, frailty, and fall risk together from sensor-based motor-function data, compare it with separate single-label models, explain its predictions, and test its robustness. Methods: Community-dwelling older adults (n=79) completed a multimodal motor-function assessment with the Mizzou Point-of-Care Assessment System (MPASS), covering gait, sit-to-stand, static balance, step-down, and reaction time, with some tasks repeated under a dual-task condition. With demographic and family-history data, this yielded 59 features. Unified classifier-chain and single-label models were built with 5 algorithms across 6 modeling stages, evaluated with repeated nested cross-validation, and compared using the area under the receiver operating characteristic curve (AUC) and paired bootstrap tests. The final model was explained with Shapley additive explanations (SHAP), and its robustness and the sufficiency of the sample size were tested with chain-input, chain-order sensitivity, domain-ablation, learning-curve, and power analyses. Results: With class weighting, the unified model had a higher mean AUC than the single-label models in 17 of 20 configurations and was never significantly worse, and it performed at least as well under nested model selection (0.615 vs 0.605; P=.58). The final extra trees model achieved a mean AUC of 0.645 (95% CI 0.569-0.722); discrimination was best for MCI (AUC 0.779, 95% CI 0.680-0.872) and lower for frailty (0.606) and fall risk (0.551). The model overestimated risk for all 3 outcomes, most for frailty. Most features (43/59, 73%), led by stride length, were shared across the 3 conditions, with consistent SHAP rankings in training and test participants ({rho}=0.99). Predicted frailty was the most important input for fall risk, and the 45 sensor features alone performed as well as the full model. Learning curves suggested that fall-risk prediction would benefit from more participants. Conclusions: A unified model predicted MCI, frailty, and fall risk together from one sensor-based assessment and performed as well as 3 separate models. It identified motor features shared across the conditions and used the link between frailty and fall risk. It performed best for MCI; with improvement for frailty and fall risk, recalibration, and external validation, such a model could support efficient screening of older adults for several conditions at once. KEYWORDS mild cognitive impairment; frailty; fall risk; machine learning; multi-label classification; classifier chain; gait; dual task; explainable artificial intelligence; Shapley additive explanations.

</details>

## Econometrics and applied economics

### [The Rise of Agents and the Human Labor Market](https://arxiv.org/abs/2611.27210)
*Nicola Borri, Anton Cheremukhin, Yukun Liu et al.* · `econ.GN` · arXiv:2611.27210v1 · relevance 0.08

- **In one sentence**: Using OpenRouter token-consumption data and Lightcast job postings, the paper estimates how firm-level exposure to aggregate agentic AI use, measured via stock-return comovement, predicts subsequent declines in U.S. job-posting growth, with an event study around the Claude Code 2.0 release.
- **In plain words**: The paper asks whether AI "agents," software that carries out multi-step tasks on its own, are reducing how many jobs companies advertise. The authors measure how much each public U.S. company's stock moves with the total amount of agentic AI use over time, and they check whether those companies later post fewer jobs. They find that more exposed firms show slower growth in job postings over the following six to nine months, with the drop concentrated in non-senior roles.
- **Why it matters**: Most earlier evidence on AI and jobs looks at AI in general, so separating out agentic AI is a more specific question with direct relevance to hiring. The paper's measure relies on stock-market reactions and on a single product release, so the findings show association and timing rather than a proven cause; the text does not establish how general the result is beyond U.S. public firms.
- **Background needed**: - Agentic AI: AI systems that plan and carry out sequences of actions (for example, writing and running code) with limited human input, as opposed to answering a single prompt.
- Tokens: the chunks of text an AI model reads or writes; token counts are used here as a measure of how much AI is being used.
- Job postings: online adverts for open roles; growth in postings is a common early signal of hiring demand.
- Stock-return comovement (beta): how strongly a company's share price moves together with some market-wide factor. Here the factor is aggregate agentic AI usage.
- Event study: comparing outcomes before and after a specific dated event, such as a product release, to isolate its effect.
- Senior vs. non-senior roles: job postings are split by seniority level, which helps show who is affected.
- Standard deviation: a unit for describing how spread out a measure is; a one-standard-deviation change is a typical-sized difference between firms. · level: research-level

<details><summary>Original abstract</summary>

We provide the first economy-wide and cross-AI model evidence on the effects of agentic AI on labor demand. We combine proprietary OpenRouter data covering about two quadrillion tokens of realized AI consumption (2 percent of global AI token consumption) across more than 400 AI models, including 1.1 quadrillion agentic tokens, with the full text of 34.8 million U.S. job postings for public firms from Lightcast. We compute our measure of firm-level exposure to aggregate agentic AI consumption (agentic beta) using the comovement of U.S. public firms' stock returns with realized weekly aggregate agentic AI token consumption. We find that a one-standard-deviation increase in a firm's exposure to agentic AI predicts 2.11 percent lower growth in job postings over the next six months and 3.20 percent over nine months. We then conduct an event study based on the release of Claude Code 2.0, which significantly expanded the capabilities of AI agents, and show that a one-standard-deviation higher pre-release exposure to agentic AI predicts 4.73 percent lower posting growth over six months post the release. Furthermore, we show that the decrease in job postings is concentrated among non-senior jobs and is statistically insignificant for senior jobs. In contrast, we find no statistically significant relation between broad AI realized consumption exposure and subsequent job posting growth once agentic exposure is controlled for. Finally, we validate our market-implied agentic exposure measure using independent evidence from firms' mentions of AI deployment in securities filings and earnings calls.

</details>

### [Partially Identified Ambiguity](https://arxiv.org/abs/2602.07634)
*Cheaheon Lim* · `econ.TH` · arXiv:2602.07634v3 · relevance 0.06

- **In one sentence**: The paper asks whether conditional Gamma-minimax decision rules, used in robust Bayesian analysis under partial identification, satisfy Aumann plausibility, and shows this holds exactly when the prior set has "partially identified ambiguity."
- **In plain words**: Economists often cannot pin down a model parameter exactly, only narrow it to a range of values, and they also describe their beliefs with a set of possible prior distributions rather than a single one. This paper asks whether it is sensible to update that set of beliefs on the observed data before making a decision. The authors argue that a particular updating rule should only be used under a specific structure of belief, which they call partially identified ambiguity.
- **Why it matters**: Robust Bayesian methods are increasingly used when data cannot fully determine the answer, so guidance on how to update those beliefs matters for applied work. The text gives a normative argument and a characterization result, but its scope beyond the stated framework is not shown here, so the practical reach is uncertain.
- **Background needed**: - Bayesian analysis: combining a prior belief with data to form an updated (posterior) belief.
- Partial identification: data narrow a parameter to a set of values (the identified set) but do not reveal a single value.
- Robust (Gamma-minimax) Bayesian analysis: instead of one prior, use a set of priors and choose the decision that does best in the worst case.
- Conditioning on the data: updating every prior in the set after seeing the data.
- Aumann plausibility: a set-valued version of the rational expectations idea that beliefs should be consistent with the true data-generating process on average.
- Random set and Aumann expectation: a set-valued analogue of an average, taken over a random collection of distributions. · level: research-level

<details><summary>Original abstract</summary>

This paper addresses the normative question of whether one should condition on the data when performing robust Bayesian analysis under partial identification. We provide an ex ante representation of the conditional Gamma-minimax criterion and show that it can violate Aumann plausibility, a set-valued generalization of the rational expectations property. Our main characterization result establishes that Aumann plausibility holds if and only if the decision maker's prior set exhibits partially identified ambiguity. The latter condition requires the prior set to equal the Aumann expectation of a random set of distributions supported on the parameter's identified sets. We interpret these results as suggesting that conditional Gamma-minimax should only be used under partially identified ambiguity. The implications for various robust Bayesian methods are discussed.

</details>

## Economic theory

### [Exchange rights and vacancy priorities](https://arxiv.org/abs/2611.27684)
*\"Ozg\"un Ekici, M. Bumin Yenmez* · `econ.TH` · arXiv:2611.27684v1 · relevance 0.05

- **In one sentence**: The paper studies strategy-proof, individually rational allocation rules for school-choice-style policies that combine permitted position exchanges with priority-based vacancy allocation, introduces a "propose-and-trade" rule, and characterizes when such rules exist and when conflict cycles block them.
- **In plain words**: The paper looks at how institutions can let people swap assigned spots while also filling newly opened spots in order of priority, such as seats in schools or jobs. It asks which rules can protect people's right to swap and their priority claims without giving them an incentive to misreport their preferences. The authors propose a new rule, propose-and-trade, and show it works under every policy that lacks "conflict cycles," which are loops of competing claims.
- **Why it matters**: The text states that the rule's properties characterize two well-known mechanisms, deferred acceptance and top trading cycles, in their classic settings, which places the work within matching theory. Its connection to real assignment systems is implied by the framing rather than detailed in the text, so the practical reach is not established here.
- **Background needed**: - Matching theory: allocating scarce places (schools, jobs, housing) to people based on their preferences and institutional priorities.
- Strategy-proof: no participant gains by misreporting their true preferences.
- Individually rational: no participant ends up worse off than their starting position.
- Deferred acceptance and top trading cycles: two classic allocation mechanisms, the first based on tentative proposals and the second on trading loops.
- Core allocation: an outcome that no group of participants could improve by trading among themselves.
- Conflict cycle: a loop of priority and exchange claims that can make a clean, manipulation-free rule impossible. · level: research-level

<details><summary>Original abstract</summary>

Many institutions let incumbents exchange positions while allocating announced vacancies by priority, withdrawing positions released by vacancy recipients. A policy specifies permitted exchanges, vacancy eligibility, and priorities. A strategy-proof, individually rational rule protecting exchange rights and vacancy priorities exists precisely for policies without conflict cycles. Restricting protection to first choices does not enlarge this class. We introduce the propose-and-trade rule, which satisfies these properties and selects the applicant-optimal core allocation under every conflict-free policy. We identify when propose-and-trade is the unique strategy-proof, individually rational rule protecting first choices. These axioms characterize deferred acceptance and top trading cycles in their classic settings. Under a policy with a conflict cycle, propose-and-trade is manipulable but protects exchange rights and first-choice claims. Replacing it with any strategy-proof rule makes some applicant worse off at some profile. We show when priority reform alone can eliminate conflict cycles and when eligibility or exchange permissions must change.

</details>

## Game theory and algorithmic economics

### [Stinespring's Dilation, Universal-NOT, and Limitations of Quantum Uncoupled Learning](https://arxiv.org/abs/2611.27251)
*Emmanouil-Vasileios Vlatakis-Gkaragkounis, Pucheng Xiong* · `quant-ph` · arXiv:2611.27251v1 · relevance 0.09

- **In one sentence**: The paper shows that quantum versions of uncoupled learning dynamics, where each player updates a quantum strategy using only its own payoff and a physical copy of the opponent's state, cannot reach Nash equilibrium in certain conjugation games under memoryless or finite-memory constraints, while small classical memory suffices for finite target families.
- **In plain words**: The paper studies a game where players choose quantum states, the basic units of quantum information, rather than simple choices. Each player can only see their own payoff and gets a physical copy of the opponent's state, and must update their own state in a way that quantum physics allows. The authors show that, for a specific family of games, no update rule that has no memory can steer players to the equilibrium, and that finite memory cannot handle every possible target.
- **Why it matters**: It identifies a limit on decentralized learning that comes from physical law rather than from missing information, which may matter for designing learning rules for quantum devices or networks. The text does not say how far these results extend beyond the games studied, so their wider significance is uncertain.
- **Background needed**: - Nash equilibrium: a set of strategies where no player gains by switching alone.
- Uncoupled learning: each player updates using only its own payoffs, not the others' payoffs or strategies.
- Quantum state (qubit): a description of a quantum system; a single qubit is the simplest case.
- Quantum channel: a physically allowed way to transform a quantum state; it must preserve total probability and cannot copy unknown states.
- Conjugation game: a game where the best response for one player is the transpose (a matrix flip) of the other's strategy.
- Memoryless vs. finite memory: whether the update rule can depend on past rounds, and how many classical bits are stored.
- Stinespring's dilation theorem: a standard result stating that any allowed quantum channel can be realized by unitary evolution with an extra environment system.
- Universal-NOT: a quantum operation that tries to flip an unknown state; its best approximate fidelity bound (Buzek, Hillery, Werner) is used here.
- Big-O notation: O(log L) means memory grows only logarithmically with the number of target states. · level: research-level

<details><summary>Original abstract</summary>

Uncoupled learning, in which players know only their own payoff, are a standard model of decentralized learning toward Nash equilibrium. We study their quantum counterpart, where strategies are quantum states and, in each round, a player receives a physical copy of their opponent's current strategy and updates their own state by a quantum channel. This adds to uncoupledness a constraint with no classical analogue: every update must be physically realizable. In fact, this constraint is decisive in conjugation games, in which Bob has a strictly dominant pure strategy and Alice's unique best response is its transpose. In this work, we show some limitations of uncoupled (learning) dynamics in finding the Nash equilibrium for conjugation games. First, we prove that no autonomous, memoryless, uncoupled dynamics converge to Nash equilibrium in a family of four single-qubit conjugation games. Specifically, any memoryless channel that keeps all four equilibria fixed will leave Alice's strategy frozen. This result also extends to $4^n$ games on $n$-qubit registers. Second, we show that this barrier disappears with a small classical memory: for any finite family of $L$ pure targets, a guess-and-test rule with $O(\log L)$ classical bits converges to equilibrium, with an explicit bound on its convergence rate. Finally, we prove that no finite memory, classical or quantum, suffices for the continuum of all pure-qubit targets. Our proof of the impossibility for memoryless channels relies on Stinespring's dilation theorem, while the impossibility for finite-memory channels relies on the optimal universal-NOT (in)fidelity bound by Bu\v{z}ek, Hillery, and Werner.

</details>

### [Learning under Bounded Manipulation for Quadratic Incentive Design](https://arxiv.org/abs/2611.26736)
*Arda G\"u\c{c}l\"u, Subhonmesh Bose, Tamer Ba\c{s}ar* · `cs.GT` · arXiv:2611.26736v1 · relevance 0.07

- **In one sentence**: A repeated quadratic incentive design game in which a leader estimates a follower's private type from noisy actions, while the follower strategically deviates to manipulate those estimates, yielding a minimax regret bound of order max{log T, min{C_T, T}} under a manipulation budget C_T.
- **In plain words**: This paper looks at a setting where one party (the leader) must set rewards for another party (the follower) without knowing the follower's private preferences. The leader learns those preferences by watching the follower's actions, but the follower knows how the leader learns and can act slightly suboptimally on purpose to steer what the leader concludes. The authors measure how much this manipulation can hurt the leader, show a lower bound on the unavoidable loss, and give a simple learning method that matches that bound.
- **Why it matters**: Learning systems that other agents can see and game, such as pricing, contracts, or automated incentive schemes, face this problem, so a precise accounting of what manipulation costs is useful. The text does not discuss specific applications, so the connection to real settings is a reasonable guess rather than something the paper claims.
- **Background needed**: - Incentive design: a leader sets rules (here, an affine reward rule) to shape another agent's behaviour.
- Private type: information only the follower knows, such as his cost or preference parameter.
- Regret: how much worse the leader does compared with an ideal policy that knew the follower's type from the start; minimax means the worst case over possible situations.
- Manipulation budget C_T: a cap on the total squared deviation the follower may make from his myopic (short-sighted) best response over T rounds.
- Lower bound: a proven limit that no method can beat in the worst case; here it is information-theoretic.
- Log T: a slowly growing term typical of learning from noisy data. · level: research-level

<details><summary>Original abstract</summary>

We study a repeated quadratic incentive design game in which a leader learns a follower's private type from noisy observations of the follower's actions and uses her estimates in an affine incentive rule. The follower knows the leader's learning policy, which incorporates past observations to produce estimates of the follower's type, and can deviate from his myopic best response to influence the leader's future estimates. We ask how the follower's ability to manipulate these observations affects the leader's performance. Under a manipulation budget $C_T$ constraining the expected cumulative squared deviation of the follower's actions from his myopic best response, we establish a minimax regret rate of order $\max\{\log T, \min\{C_T,T\}\}$ for approximately rational followers. Our information-theoretic lower bound applies to a general class of causal estimation and manipulation policies for the leader and the follower. We provide a simple learning policy that achieves the lower bound. Finally, we show that under a fixed learning rule, increasing the manipulation budget of the follower can counterintuitively reduce the leader's regret.

</details>

## Mathematical finance

### [A Solvency II-Based Framework for Pricing Structural Longevity Risk under an Affine Mortality Model](https://arxiv.org/abs/2611.26670)
*Madiha Bouhouche (INSEA), Said Khalil (TREE, INSEA) et al.* · `q-fin.PR` · arXiv:2611.26670v1 · relevance 0.05

- **In one sentence**: The paper proposes a Solvency II Cost-of-Capital pricing framework for structural longevity risk, using a Gaussian affine mortality model in calendar time and comparing a trend-based stress with a mortality-level stress and a Value-at-Risk capital measure, illustrated with Belgian mortality data.
- **In plain words**: Insurers and pension funds that pay out annuities risk losing money if people live longer than expected. This paper offers a way to price that long-term risk and to set aside the capital regulators require for it, using a mathematical model of how mortality changes over time. In a Belgian data example, the authors find that stressing the current mortality level produces much larger capital-cost figures than stressing the long-run trend.
- **Why it matters**: Longevity risk is a major concern for annuity and pension providers, and the paper's point that the choice of adverse scenario strongly changes the capital estimate is relevant to how such risks are priced and regulated. The text does not show how widely the framework would be adopted or how well it performs beyond the single numerical example.
- **Background needed**: - Longevity risk: the chance that people live longer than an insurer or pension fund assumed, raising the cost of paying annuities.
- Solvency II: the European insurance regulatory regime that requires insurers to hold capital against risks.
- Best Estimate: the probability-weighted present value of expected future cash flows.
- Solvency Capital Requirement (SCR) and Risk Margin: the capital buffer required, and the extra charge reflecting the cost of holding that capital for others, under the Cost-of-Capital principle.
- Affine mortality model: a model where death probabilities have a closed-form formula driven by a hidden, randomly moving "longevity factor"; this keeps calculations tractable.
- Value-at-Risk (VaR): a loss level not expected to be exceeded at a set confidence level.
- Calendar time: time measured by real dates, so mortality can improve across years for everyone.
- Incomplete market: a market where longevity risk cannot be fully hedged by traded assets. · level: research-level

<details><summary>Original abstract</summary>

This paper develops a Solvency II-based pricing framework for structural longevity risk in incomplete longevity markets. The valuation scheme relies on the Cost-of-Capital principle underlying the Risk Margin and combines it with a continuous-time affine mortality model. Mortality dynamics are specified in calendar time, with age-dependent mortality patterns linked to a latent longevity factor driving long-term mortality improvements. The affine structure preserves closed-form survival probabilities and provides a tractable basis for repeated Best Estimate, Solvency Capital Requirement and Risk Margin calculations. We derive the conditional distribution of one-year discounted Best Estimate variations, obtaining analytical expressions for their asymmetry and Value-at-Risk under the Gaussian affine specification. Within this setting, we introduce a stress-based assessment by applying adverse shocks to the deterministic parameters governing the longevity trend. The trend-based stress is compared with a mortality-level stress and with a Value-at-Risk-based capital assessment. The methodology links stochastic mortality modelling, prudential capital valuation and longevity-linked payoff assessment within a unified actuarial framework. A numerical application based on Belgian mortality data illustrates the implementation and shows that the mortality-level stress produces substantially larger scenario-based capital-cost measures than the trend-based stress. These findings highlight the sensitivity of longevity risk valuation to the specification of adverse mortality scenarios. The approach offers a transparent and operational basis for assessing and pricing structural longevity risk under a Solvency II Cost-of-Capital perspective.

</details>

### [Risk sharing for background risk models with infinite mean](https://arxiv.org/abs/2611.27485)
*Ziting Miao, Yuyu Chen, Han Li* · `q-fin.RM` · arXiv:2611.27485v1 · relevance 0.04

- **In one sentence**: The paper studies when risk sharing (splitting losses among agents) increases risk for positively dependent infinite-mean losses under linear and conditional mean sharing in background risk models, with stochastic-order results for Pareto, Clayton, Fréchet-Gumbel and stable distributions.
- **In plain words**: The paper asks whether pooling and splitting a financial loss among several people always makes things safer, as it usually does. For losses whose average size is infinite, which can happen with very heavy-tailed risks, the authors find that sharing can instead make the overall risk larger. They work this out for several standard multivariate loss models and compare the results across different ways of splitting losses.
- **Why it matters**: It challenges the common intuition that diversification and risk sharing always reduce risk, which matters for insurance and portfolio decisions involving extremely heavy-tailed losses. The text does not say how directly the results apply in practice, so the practical reach is uncertain.
- **Background needed**: - Risk sharing: dividing a random loss among several agents, for example through insurance or a pooled portfolio.
- Background risk: an extra, unrelated-to-the-contract source of uncertainty that the agents also face.
- Infinite mean: a loss whose long-run average is unbounded, so extremely large losses are common enough to dominate.
- Positive dependence: losses tend to be large together.
- Copula: a function describing how dependent random quantities are, separate from their individual distributions.
- Pareto, Clayton, Fréchet-Gumbel, stable distributions: standard heavy-tailed and dependent probability models.
- Stochastic order (usual stochastic order): one risk is uniformly larger than another in distribution.
- Law-invariant monotone risk measure: a rule for scoring risk that depends only on the loss distribution and ranks larger losses as riskier. · level: research-level

<details><summary>Original abstract</summary>

Risk sharing is usually viewed as beneficial for risk-averse agents facing independent risks with finite means, but this situation can be reversed for infinite-mean losses. In this paper, we explore the effects of risk sharing for positively dependent infinite-mean losses using background risk models. Under both linear and conditional mean risk sharing, we show that risk sharing of infinite-mean losses can increase the risk in the sense of usual stochastic order. Our results cover classical multivariate loss distributions, including the Pareto-Clayton and the Fr\'echet-Gumbel models. For linear risk sharing, we further derive stochastic dominance relations between diversified portfolios, including those with Pareto marginals coupled by convex mixtures of commonly used Archimedean copulas. For conditional mean risk sharing, we additionally discuss peakedness and stochastic order relations for stable distributions. Consequently, under the stated conditions, retaining the original risk or a less diversified portfolio is preferred under every law-invariant monotone risk measure that is well defined for infinite-mean models.

</details>

## Financial markets

### [Nonlinear Shrinkage for Higher Moments Estimation in Large Portfolios](https://arxiv.org/abs/2611.27274)
*Paul Ruelloux, Christian Bongiorno, Damien Challet* · `q-fin.PM` · arXiv:2611.27274v1 · relevance 0.07

- **In one sentence**: The paper extends covariance-cleaning methods (cross-validated filtering and the Average Oracle approach) to even-order co-moment tensors, such as cokurtosis, and tests them on large equity portfolios built from Russell 1000 stocks.
- **In plain words**: Investment risk is not just about how much prices wiggle; it also depends on how stocks move together in extreme ways. Estimating these joint patterns from past data is very noisy when a portfolio holds many stocks, so the authors develop filters that clean up those estimates. They report that, on historical Russell 1000 stock returns, the cleaned estimates predict relationships more accurately than the raw sample estimates, and portfolios built with them have lower out-of-sample volatility and kurtosis (a measure of fat-tailed risk).
- **Why it matters**: Portfolio managers who care about tail risk, not only average variance, need reliable estimates of higher-order co-movements, and this paper shows a concrete way to reduce estimation noise for them. The text reports improvements on one dataset (Russell 1000 constituents); how well the gains hold in other markets or periods is not shown in the summary.
- **Background needed**: - Covariance matrix: a table of how every pair of assets moves together; the usual starting point for portfolio risk.
- Co-moments: generalizations beyond covariance. Coskewness and cokurtosis describe how assets jointly behave in asymmetric or extreme moves.
- Tensor: a multi-dimensional array, the natural container for cokurtosis (stocks by stocks by stocks by stocks).
- Kurtosis: a measure of how heavy the tails of returns are, i.e., how often large surprises occur.
- Shrinkage / filtering: deliberately adjusting noisy estimates toward more stable structure to reduce estimation error.
- Out-of-sample: testing on data not used to build the estimate, which is the fair test of forecasting accuracy.
- Frobenius error: a standard size-of-error measure for matrices and tensors; "relative" means scaled against a reference. · level: research-level

<details><summary>Original abstract</summary>

Portfolio risk is not limited to the variance of returns. The moments of portfolio returns depend directly on the covariance matrix and higher-order co-dependences (coskewness, cokurtosis, etc.). In practice, however, these objects are extremely noisy, especially for large portfolios. Here we introduce filtering methods based on tensor decompositions that extend cross-validated covariance cleaning and the Average Oracle methodology to even-order co-moment tensors. Using returns on historical Russell 1000 constituents, we find that the proposed filters improve out-of-sample estimation accuracy relative to sample estimators, both for correlation and cokurtosis tensors, as measured by relative squared Frobenius errors. These improvements translate into lower relative errors on portfolio volatility and kurtosis, and into lower out-of-sample volatility and kurtosis when the portfolio objective penalizes both variance and the fourth moment.

</details>

### [Are Calibrated Decision Models Calibrated on Markets? Geolocated News, Markov Switching and a System One Model for Nasdaq-100 Allocation](https://arxiv.org/abs/2611.26716)
*Jakub Zaj\k{a}c, Micha{\l} Dyrek* · `q-fin.ST` · arXiv:2611.26716v1 · relevance 0.04

- **In one sentence**: A test of whether the Jev probability model, a Markov-switching regime model, and geolocated news features are calibrated against realised Nasdaq-100 four-week declines from 2025 onward, with a half-Kelly allocation comparison.
- **In plain words**: The paper asks how much to trust the probabilities that a forecasting tool gives for whether the Nasdaq-100 stock index will fall over the next four weeks. The authors checked each Friday's forecast against what the market actually did, using 88 weeks from January 2025 on. Their main finding is that the raw probabilities were too high on average, and simply shifting them toward the long-run historical rate of decline made them much more accurate.
- **Why it matters**: Position sizing depends on the probability of loss, so a model that systematically overstates risk can lead to poor allocation decisions. The paper's practical message, that probabilities should be anchored to the base rate of an event before use, may be relevant to anyone using language-model or other probability outputs in finance, though the test covers a single index over a short period.
- **Background needed**: - Calibration: whether a stated probability matches how often the event actually happens (a forecast of 40% should come true about 40% of the time).
- Base rate: the historical frequency of an event, here how often the index fell over four weeks.
- Expected calibration error (ECE): a single number summarising the average gap between forecast probabilities and observed frequencies.
- Markov-switching model: a statistical model that assumes the market moves between a small number of hidden regimes, such as calm and turbulent.
- AUC: a score from 0 to 1 for how well a model ranks likely events above unlikely ones; 0.5 is no better than chance.
- Half-Kelly allocation: a rule for sizing bets based on estimated edge, scaled down by half to reduce risk.
- Platt scaling and isotonic regression: standard methods for recalibrating probabilities using past outcomes.
- Knowledge probe: a check of what events a language model was trained on, here used to show Jev's knowledge ends around late 2024. · level: research-level

<details><summary>Original abstract</summary>

Portfolio allocation is driven by probabilities of losses, not only by forecasts of the direction (up/down) of the market. A decision model such as Jev returns a probability for a yes/no question and has been reported to be well calibrated on a set of benchmarks. However, the model's calibration against realised market outcomes has not been tested. In this study, every Friday we ask whether the Nasdaq-100 will close lower four weeks later and compare a two-regime Markov-switching model estimated on data from 1990 to 2026, Jev reading weekly headlines and geolocated news features computed with spatial queries in PostGIS, and their combination. A knowledge probe shows that Jev knows events up to late 2024, so we evaluate it on 88 weeks from January 2025 onwards. None of the models predicts the direction better than the historical base rate. A key finding is that raw Jev overestimates the probability of a decline: its mean forecast is 0.48 against an observed frequency of 0.38, and its ECE is 0.10. A prior shift to the historical base rate, which uses no outcomes from the test period, lowers the ECE to 0.015. In contrast, Platt scaling, isotonic regression and the combination with the Markov model all make the forecasts worse. In a half-Kelly allocation, the raw Jev strategy returns 3.1% per year, whereas after the prior shift it returns 14.5%; a simple buy-and-hold strategy in QQQ returns 15.3% per year. The Markov model forecasts large declines (more than 10%) well, with an AUC of 0.81, and its strategy has the highest Sharpe ratio over 1999-2026. Asked about such a large decline (base rate 4%), raw Jev forecasts 16-24% on average, and the same prior shift removes this offset. The practical lesson is that decision-model probabilities must be anchored to the base rate of the market event before they are used to size positions.

</details>

## Signal processing

### [DNN-Assisted Deterministic Policy Learning for Adaptive IRS-NOMA-OWC Networks](https://arxiv.org/abs/2611.26742)
*Ahrar N. Hamad, Ahmad A. Qidan, Taisir E. H. El-Gorashi et al.* · `cs.IT` · arXiv:2611.26742v1 · relevance 0.07

- **In one sentence**: The paper proposes a two-stage deep neural network plus deterministic-policy deep reinforcement learning framework that jointly sets power allocation, IRS mirror orientations, and an adaptive NOMA decoding order in an indoor, mobile-user optical wireless network.
- **In plain words**: This paper looks at how to deliver fast wireless internet indoors using light instead of radio, when people are moving around and their light signals can be blocked. The authors use a small set of tiltable mirrors (an intelligent reflecting surface) to bounce light toward users, and a learning system that estimates where users are and decides how to share power among them. The text reports that the approach gets close to theoretical upper bounds and beats several standard learning methods, conventional optimization, and setups without the mirror surface, with faster convergence.
- **Why it matters**: Indoor light-based communication is a possible complement to crowded radio spectrum, and handling moving users is a practical obstacle. The results are simulation-based claims in the text; how they hold up in real hardware or in other settings is not shown here.
- **Background needed**: - Optical wireless communication (OWC): sending data with visible or infrared light instead of radio waves.
- Line-of-sight (LoS) blockage: the direct light path being interrupted, for example by a person or object.
- Intelligent reflecting surface (IRS): a surface whose elements can be adjusted to redirect signals; here, mirrors whose orientation is tuned.
- Non-orthogonal multiple access (NOMA): several users share the same channel at once, with power split between them and decoded in a set order.
- Decoding order: the sequence in which a receiver removes other users' signals; this paper updates it as channels change.
- Sum rate and QoS: total data throughput across users, and minimum service guarantees per user.
- Deep neural network (DNN) and deep reinforcement learning (DRL): learning models that estimate quantities and learn control decisions by trial and feedback; a deterministic policy gradient is one specific DRL training method.
- Non-convex optimization: a hard-to-solve mathematical problem with many local best points. · level: research-level

<details><summary>Original abstract</summary>

Intelligent reflecting surface (IRS) has been considered a promising technology in optical wireless communication (OWC) networks due to its potential to overcome the line-of-sight (LoS) blockage issue and enhance coverage. In this paper, a dynamic IRS-assisted indoor non-orthogonal multiple access (NOMA)-OWC network is modeled, and an optimization problem is formulated to maximize the sum rate subject to the quality-of-service (QoS) requirements of multiple mobile users, by jointly optimizing the power allocation and the IRS mirror orientations, from which the user's decoding order is induced rather than being fixed. Since the problem is non-convex and the channel conditions vary with user mobility, conventional optimization methods may incur considerable computational overhead. Therefore, a two-stage deep neural network-deep reinforcement learning (DNN-DRL) framework is proposed. In the first stage, the DNN estimates the user's positions and orientations in real time, removing the need for perfect knowledge of the user state. In the second stage, a deterministic policy gradient (DPG)-based DRL algorithm uses these estimates to jointly optimize the power allocation and IRS mirror orientations, with the decoding order updated according to the resulting effective channel gains. The results show that the proposed framework approaches the performance upper bounds and outperforms standard DRL algorithms, conventional optimization methods, and deployments without IRS in terms of sum rate and fairness, while achieving faster convergence. Furthermore, online adaptation of the decoding order maintains higher QoS satisfaction than a fixed decoding order, particularly under high user mobility.

</details>

### [From Pilots to Position: Experimental Near-Field Localization for ISAC](https://arxiv.org/abs/2611.27503)
*Yunxin Li, Emiel Vanspranghels, Jialun Kou et al.* · `eess.SP` · arXiv:2611.27503v1 · relevance 0.06

- **In one sentence**: An experimental study of near-field target localization using OFDM pilot signals from a distributed multi-transmitter, multi-receiver communication testbed at 3.4 GHz, comparing coherent backprojection with noncoherent delay-TDOA fusion.
- **In plain words**: The paper asks whether a wireless network built for communication can also work out where an object is, by reusing the reference signals it already sends. The authors built a hardware setup with two transmitters and four receivers and tested it on 16 fixed target positions. Both of their methods located the target to within about 19 cm on average.
- **Why it matters**: It offers real-hardware evidence, rather than only simulation, for how accurate sensing can be when it piggybacks on communication signals. The text does not show how these results compare with other systems, so its wider significance for future wireless networks is unclear.
- **Background needed**: - ISAC (integrated sensing and communication): using the same radio signals to both communicate and sense the environment.
- OFDM: a common wireless modulation that splits data across many closely spaced frequencies.
- Pilot signals: known reference signals sent with the data so receivers can estimate the channel.
- Near field: the close-range zone around an antenna array where wavefronts curve, which changes how location is computed.
- Multistatic sensing: several separate transmitters and receivers observing the same target.
- TDOA (time difference of arrival): locating a source from differences in when signals reach different receivers.
- Coherent vs. noncoherent: coherent methods use the signal's phase as well as its strength; noncoherent methods use only timing or strength.
- Occupied bandwidth: the width of frequency range used; wider bandwidth generally allows finer timing resolution. · level: research-level

<details><summary>Original abstract</summary>

Integrated sensing and communication (ISAC) enables wireless systems to reuse communication signals for environmental sensing, potentially reducing the need for dedicated sensing resources. However, the achievable localization accuracy of communication-centric waveforms under practical hardware constraints remains an important challenge. In this paper, we experimentally investigate near-field target localization using OFDM pilot signals in a distributed communication system. We consider both coherent and noncoherent localization approaches, exploiting multistatic propagation delays and time-difference-of-arrival (TDOA) information extracted from pilot-based channel estimates. A hardware setup comprising two transmitters and four receivers was developed and configured to operate at 3.4 GHz with 198 MHz occupied bandwidth to evaluate localization performance under realistic propagation and synchronization conditions. Experimental results across 16 static target positions demonstrate mean localization errors of 19.8 cm and 18.8 cm for coherent backprojection and noncoherent delay-TDOA fusion, respectively. Furthermore, we investigate the impact of occupied bandwidth on localization accuracy of the two proposed algorithms. These findings provide experimental insights into the capabilities and practical limitations of OFDM pilot-based sensing, supporting resource-efficient localization in future ISAC systems.

</details>

## Audio and speech

### [PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions](https://arxiv.org/abs/2611.27601)
*Sulong Yang, Zhi Zeng, Xiupeng Wu et al.* · `cs.SD` · arXiv:2611.27601v1 · relevance 0.11

- **In one sentence**: PromptTTSD is a open-source spoken dialogue synthesis model, trained on a new large multi-speaker dataset (PromptDialog) extracted from multi-narrator audiobooks with open-ended natural-language style descriptions, that adds fine-grained style control and zero-shot voice cloning to multi-turn conversational speech generation.
- **In plain words**: The paper tackles the problem that today's systems that turn written dialogue scripts into spoken conversation sound fairly flat, and can't easily be told how each line should be delivered. The authors built a large dataset by pulling conversational speech out of audiobooks with several narrators, and used a language model to write style descriptions from the surrounding story text instead of relying on a fixed list of style labels. They then trained a model, PromptTTSD, that takes these style descriptions along with the script, and report that it keeps basic speech quality while giving competitive style control compared with commercial systems.
- **Why it matters**: Natural conversation changes tone from turn to turn, so controllable multi-speaker speech could matter for audiobooks, dubbing, and voice assistants. The main contributions are the dataset and an open model, but the abstract's comparisons are only summarized here, so the size of the gains is not clear from this text alone.
- **Background needed**: - Text-to-speech (TTS): software that generates spoken audio from written text.
- Spoken dialogue synthesis: generating a multi-turn conversation with several voices, where each line should fit the previous ones.
- Prompt-based control: steering how speech sounds (e.g., calm, angry) by giving a natural-language description rather than setting numeric parameters.
- Zero-shot voice cloning: copying a voice from a short sample without extra training for that voice.
- Forced alignment: matching a transcript to the exact timing of words in an audio recording; the paper's two-stage version is used to cut clean dialogue segments from audiobooks.
- Fine-tuning: further training an existing model on a new dataset. · level: research-level

<details><summary>Original abstract</summary>

Spoken dialogue synthesis aims to generate multi-turn conversational speech from dialogue scripts while maintaining speaker consistency and contextual appropriateness. However, existing models largely lack fine-grained controllability, which is critical for capturing the dynamic, context-dependent style shifts in natural conversations. While prompt-based TTS has enabled such control for single-speaker speech, existing datasets heavily rely on predefined tags, which fundamentally limits their capacity to capture open-ended styles. To address this gap, we propose a scalable pipeline for extracting conversational speech from multi-narrator audiobooks, featuring an improved two-stage alignment algorithm to preserve dialogue continuity, paired with LLM-based extraction of style descriptions directly from narrative text. We release PromptDialog, a large-scale multi-speaker conversational speech dataset comprising 8,383 hours of Chinese speech and 120 hours of English speech, with open-ended style descriptions for 79% of utterances. We further introduce PromptTTSD, a spoken dialogue synthesis model built via a prompt-aware fine-tuning strategy that integrates style prompts into text-speech interleaved sequences. PromptTTSD is an open-source spoken dialogue synthesis model that supports both zero-shot voice cloning and natural language style control. Experiments demonstrate that PromptTTSD not only maintains strong fundamental synthesis capabilities but also achieves competitive open-ended style control compared with proprietary models, and substantially improves contextual appropriateness in multi-turn dialogues.

</details>

### [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784)
*Sivashankar Selvarajan, Piyush Verma, Sumit Kumar et al.* · `cs.SD` · arXiv:2611.27784v1 · relevance 0.09

- **In one sentence**: A company report presents ARCAS 290M, a single frozen audio-deepfake detector evaluated across ten public benchmarks and compared against commercial systems on independent leaderboards.
- **In plain words**: Voice cloning can now copy someone's voice from a few seconds of audio, and detection tools often stop working when the fake voice comes from a new generator, phone line, or language. This paper describes ARCAS 290M, a detector from the company Neural Defend, which the authors say works well across many generators, channels, and languages without being retuned for each test. The text reports that it ranks first on the Podonos leaderboard and has the lowest equal error rate among commercial detectors on ASVspoof5, but the full comparison numbers are not given in the summary.
- **Why it matters**: Reliable detection of cloned voices matters for fraud, scam calls, and platform moderation, so a detector that holds up on unseen conditions would be useful if the claims hold. The text is a self-reported company summary with no method details, so the claims should be checked against the full paper and independent evaluations.
- **Background needed**: - Deepfake audio detection: software that decides whether a voice recording was produced by a machine rather than a real speaker.
- Text-to-speech (TTS) and voice conversion: methods that generate or transform speech to sound like a target person.
- Codec language model: a newer kind of speech generator that predicts compressed audio tokens.
- Foundation model: a large model trained once on broad data and then reused across tasks; "frozen" means its weights are not adjusted for each test.
- Zero-shot: tested on data the model was not specifically trained or tuned for.
- Equal error rate (EER): the error level where false alarms and missed fakes are equally common; lower is better.
- ASVspoof5, SpeechFake, ShiftySpeech: public benchmark datasets of real and spoofed speech used to compare detectors.
- Leaderboard: a public ranking of systems on a shared test. · level: intermediate

<details><summary>Original abstract</summary>

Voice cloning now needs only seconds of audio, and detectors tuned to one dataset often fail when the generator, channel, or language changes. We introduce ARCAS 290M, Neural Defend's foundation model for detecting AI-generated audio. A single frozen production model, with no benchmark-specific fine-tuning, generalizes across text-to-speech, voice-conversion, and codec-language-model generators, telephone and Bluetooth channels, recording conditions, and languages. We evaluate it on the complete official test sets of ten public benchmarks, scoring every recording exactly as released, and against commercial systems on independent leaderboards. ARCAS 290M ranks first among all systems on the Podonos leaderboard and has the lowest equal error rate among commercial detectors on ASVspoof5. It separates real from AI-generated speech almost perfectly on ASVspoof5, SpeechFake, and ShiftySpeech, and detects nearly all AI-generated speech in Hindi, Tamil, Bengali, and Telugu. On every benchmark with a published zero-shot comparison, including in-the-wild audio, partial fakes, and the conditions hardest for the field, it surpasses the strongest reported detector by a wide margin. These results establish ARCAS 290M as a general-purpose foundation for AI-generated audio detection in fraud prevention, platform safety, and media verification.

</details>

## Control systems

### [Learned Network Dynamics for Model Predictive Traffic Signal Control under Incidents](https://arxiv.org/abs/2611.27435)
*Dang Viet Anh Nguyen, Carlos Lima Azevedo, Tomer Toledo et al.* · `cs.LG` · arXiv:2611.27435v1 · relevance 0.17

- **In one sentence**: GNN-MPC is a receding-horizon traffic-signal controller that plans with graph-neural-network dynamics learned from action-conditioned data, coordinates phases across intersections via approximate best responses with a cost-based acceptance test, and is evaluated in microscopic simulation under non-recurrent incidents on a homogeneous grid and a heterogeneous 21-intersection network.
- **In plain words**: The paper looks at how to time traffic lights in a city when an incident such as a crash or lane closure disrupts normal traffic flow. The authors use a learned model, built with graph neural networks, to predict how queues will respond to different signal choices, and they plan a short look-ahead of signal timings that is repeatedly updated. In computer simulations, this approach cut travel time and completed more trips than the other controllers tested.
- **Why it matters**: Traffic signals that adapt well to incidents could reduce delays in real cities, and the paper's comparisons suggest that both seeing queues that extend beyond short lane sensors and predicting how queues respond to signal changes matter. The results come only from simulation as described in the text, so how well they transfer to real networks is not established here.
- **Background needed**: - Model predictive control (MPC): at each step, plan a sequence of actions over a short future window using a model, apply only the first action, then re-plan with new measurements.
- Traffic signal phases: the sequence of green-light combinations at an intersection.
- Queue: a line of stopped or slow vehicles; queues can spill back upstream past the sensor area.
- Graph neural network (GNN): a learning model that works on networks of connected nodes (here, intersections and lanes), sharing information among neighbours.
- Store-and-forward model: a simpler traffic model that treats links as holding and passing vehicles with fixed rules, used here as a baseline.
- MaxPressure: a known heuristic signal-control rule that favours phases relieving the most congested movements.
- Best response: in game-theory terms, each intersection's optimal choice given its neighbours' current choices; "approximate" means computed with a simplified method.
- Microscopic simulation: simulating each vehicle individually. · level: research-level

<details><summary>Original abstract</summary>

Model predictive control (MPC) of urban traffic signals relies on a model of how queues respond to signal decisions, which is hard to specify and calibrate in heterogeneous networks, particularly when incidents change capacities and turning shares. Measurements add a second limitation: the controlled lanes at the stop line are often short, so queues extending upstream of them fall outside lane-level measurements. We propose GNN-MPC, a receding-horizon controller that plans with action-conditioned network dynamics learned by graph neural networks. Phase sequences are coordinated across intersections by approximate best responses, with an acceptance test that keeps the predicted cost no higher than that of the initial plan. In microscopic simulation under non-recurrent incidents, GNN-MPC reduces travel time and increases completed trips relative to all tested controllers, on a homogeneous grid and a heterogeneous 21-intersection network. Controlled comparisons on the heterogeneous network distinguish the roles of observation and prediction. With nearly as many vehicles entering the network, GNN-MPC reduces travel time by 13% relative to MaxPressure with the same upstream measurement, and GNN-MPC without the upstream representation does not reproduce its performance. Under the same traffic measurements, planner and objective, replacing the learned dynamics with calibrated store-and-forward predictors increases travel time by 31-34%. Observing hidden demand and predicting its response to control are thus complementary requirements of network-level predictive control.

</details>

### [Nonholonomic Event-Triggered Source Seeking](https://arxiv.org/abs/2611.26802)
*Victor Hugo Pereira Rodrigues, Tiago Roux Oliveira, Miroslav Krstic* · `math.OC` · arXiv:2611.26802v1 · relevance 0.10

- **In one sentence**: An event-triggered source seeking controller for nonholonomic unicycle vehicles that separates continuous probing motion from aperiodic, event-triggered updates of the seeking correction, with practical exponential convergence proved via a time-periodic Lyapunov function and a positive minimum dwell time.
- **In plain words**: This paper looks at how a robot vehicle can find the peak of an unknown signal, such as the strongest source of some field, while only updating its steering correction at certain moments instead of constantly. The vehicle keeps wiggling in a continuous probing motion so it can sense which way the signal is rising, and it only recomputes and sends a new correction when a trigger condition is met. The authors prove that, under their design, the vehicle converges to a neighborhood of the source and that updates never bunch up infinitely fast.
- **Why it matters**: Reducing how often a controller must compute and communicate can save computing and bandwidth on real vehicles, which matters for networked or battery-limited robots. The text claims the analysis also covers source fields with different curvature in different directions, which earlier Lie-bracket analyses did not; the scope of that claim beyond the text is not something I can judge.
- **Background needed**: - Source seeking: steering a vehicle toward the maximum of an unknown field using only measured values, not its shape.
- Nonholonomic unicycle: a wheeled vehicle that cannot move sideways, so its steering is constrained.
- Probing / dithering: small periodic oscillations added to the motion so the sensor signal reveals the direction of the gradient.
- Washout, demodulation, low-pass filtering: standard signal-processing steps that extract a slowly varying gradient estimate from the measured signal.
- Event-triggered control: updating the control only when a measured condition crosses a threshold, rather than on a fixed clock.
- Zeno behavior: an infinite number of triggers in finite time, which the paper rules out via a positive minimum dwell time.
- Lyapunov function: a energy-like function used to prove that a system settles toward a target.
- Averaging / Lie-bracket analysis: mathematical tools for approximating the averaged effect of fast periodic motion. · level: research-level

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
| AI industry news | 34 | 28 | 5 |
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
| Biochemistry | 24 | 21 | 2 |
| Pharmacology and drug discovery | 7 | 6 | 1 |
| Computational and systems biology | 112 | 106 | 2 |
| Neuroscience | 102 | 96 | 2 |
| Genetics and genomics | 43 | 38 | 2 |
| Cell and molecular biology | 70 | 66 | 2 |
| Immunology and microbiology | 75 | 69 | 2 |
| Cancer biology | 38 | 34 | 2 |
| Ecology and evolution | 47 | 43 | 2 |
| Plant biology | 28 | 24 | 2 |
| Bioengineering and synthetic biology | 29 | 25 | 2 |
| Mathematical biology (arXiv) | 15 | 12 | 2 |
| Epidemiology | 22 | 18 | 2 |
| Infectious diseases | 5 | 1 | 0 |
| Public and global health | 16 | 12 | 2 |
| Psychiatry and neurology | 26 | 22 | 2 |
| Oncology | 10 | 6 | 2 |
| Health informatics and medical AI | 24 | 20 | 2 |
| Econometrics and applied economics | 4 | 3 | 2 |
| Economic theory | 3 | 3 | 1 |
| Game theory and algorithmic economics | 9 | 8 | 2 |
| Mathematical finance | 11 | 8 | 2 |
| Financial markets | 6 | 5 | 2 |
| Signal processing | 17 | 15 | 2 |
| Audio and speech | 8 | 6 | 2 |
| Control systems | 32 | 30 | 2 |

<!-- {% endraw %} -->
