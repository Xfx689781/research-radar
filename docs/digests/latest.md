# Research digest · 2026-11-23
<!-- {% raw %} -->

New papers posted from about 2026-11-22 to 2026-11-23 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Overview and recent progress on the classical Bernoulli free boundary problem](https://arxiv.org/abs/2611.26636)** (Partial differential equations): This is an overview article about a mathematical problem where a function is defined in a region, but the edge of that region is not known in advance and must be found as part of the solution. The text is a short abstract that says the survey covers the Bernoulli or one-phase version of this problem and highlights recent progress. The abstract does not list specific results, so details of what was found cannot be taken from it.
- **[Autonomous quantum machine learning via Riemannian gradient-based optimization](https://arxiv.org/abs/2611.27815)** (Quantum information and computing): Most quantum machine learning today trains by repeatedly measuring a quantum device and sending the results to a classical computer to adjust settings. This paper proposes a way to let the quantum system update its own settings during training, so the classical feedback loop is removed. The authors state that under certain conditions this can be done autonomously, that training converges exponentially in the number of iterations for small steps, and that in their numerical tests the model could find a hidden symmetry in the data at low circuit depth using only a few training examples.
- **[Hidden Semi-Markov Models for Fully Functional Time Series](https://arxiv.org/abs/2611.26838)** (Statistical methods and applications): Many signals, such as brain recordings, switch between hidden modes over time, and a common model for this is the hidden Markov model. That model forces each mode to last for a random time that drops off quickly, which often does not fit real data. This paper replaces it with a version where each hidden mode can last for a more flexible, data-driven length, and applies the approach to overnight sleep-study EEG recordings from children.

## Probability

### [Stochastic Differential Equations on the Simplex](https://arxiv.org/abs/2611.27309)
*Paolo Guasoni, Eberhard Mayerhofer* · `math.PR` · arXiv:2611.27309v1 · relevance 0.29

- **In one sentence**: The paper builds a class of simplex-valued diffusion processes as solutions to stochastic differential equations driven by antisymmetric Brownian motion, covering multivariate Jacobi processes and general simplex polynomial diffusions, and proves weak existence plus global strong existence and pathwise uniqueness from strictly positive starting states under a boundary non-attainment condition.
- **In plain words**: This paper studies random processes that move around inside a simplex, meaning a set of numbers that are all non-negative and add up to one, like a split of a whole into shares. The authors describe such moving shares as solutions to a type of random-motion equation, using a specific kind of random noise that keeps the total fixed. They show that these processes exist and are uniquely determined when they start with every share strictly positive, under a stated condition that they never reach the edge of the simplex.
- **Why it matters**: Shares that evolve randomly over time, such as portfolio weights or population proportions, are a natural setting for these models, so a general, well-posed framework matters for that kind of modelling. The text does not discuss applications, so any link to specific fields is my inference rather than something the paper states.
- **Background needed**: - Simplex: the set of non-negative numbers that sum to one (e.g., proportions of a whole).
- Brownian motion: the mathematical model of continuous random jiggling, as in pollen particles in water.
- Stochastic differential equation (SDE): an equation describing how a quantity changes over time with both a steady push (drift) and random noise.
- Diffusion process: a random process whose solution is described by such an SDE.
- Weak vs. strong solution: a weak solution exists in some probabilistic sense; a strong solution is defined pathwise on a given noise source.
- Pathwise uniqueness: for a given noise path, there is only one solution.
- Jacobi process: a known diffusion living on an interval, here generalised to the simplex. · level: research-level

<details><summary>Original abstract</summary>

We propose a framework for simplex-valued diffusion processes, formulated as solutions to stochastic differential equations driven by antisymmetric Brownian motion. Our edge-wise representation includes the multivariate Jacobi processes and the general class of continuous simplex-valued polynomial diffusions. Also, it allows bounded, locally Lipschitz state-dependent drift rates and edge weights. We establish weak solutions, as well as global strong existence and pathwise uniqueness for strictly positive initial states under a sufficient boundary non-attainment condition.

</details>

### [Isolation in Random Graphs](https://arxiv.org/abs/2611.26781)
*Laurentiu Ploscaru* · `math.CO` · arXiv:2611.26781v1 · relevance 0.21

- **In one sentence**: Studies the isolation number, domination number and F-isolation of the binomial random graph G(n,p) for p = o(1) and np → ∞, giving two-point concentration results, a transition in the gap between domination and isolation, and asymptotic sharpness of the minimum-degree bound for regular hosts.
- **In plain words**: This paper looks at random networks where each possible link between n points appears independently with some small probability p. It asks how few "chosen" vertices are needed so that every other vertex is either chosen or next to a chosen one, and how that changes when the goal is weakened to leaving behind only vertices that do not contain a given shape (such as a tree-like pattern). The authors give fairly precise answers on how these numbers behave as the network grows, and show how the gap between two related counts depends on how sparse the network is.
- **Why it matters**: These are questions about how precisely typical large random networks can be covered or dominated, and the text reports sharp thresholds where the behaviour of this gap changes. The text does not say what applications it may have, so its wider relevance is unclear from the abstract alone.
- **Background needed**: - A random graph G(n,p): n vertices, each pair joined by an edge independently with probability p.
- "Asymptotic" / "with high probability": statements about what happens as n grows large, holding with probability tending to 1.
- Domination number γ(G): the fewest vertices that together touch or include every vertex (each vertex is chosen or adjacent to a chosen one).
- Isolation number ι(G): the fewest vertices whose removal leaves a graph with no edges; the paper's F-isolation generalises this to leaving a graph with no copy of F, where F is a fixed forest (F = an edge gives ordinary isolation).
- Two-point concentration: the value is, with high probability, one of two adjacent integers.
- Minimum degree bound: a classical lower bound on domination in terms of the smallest number of neighbours any vertex has.
- Probability asymptotics, including log and little-o notation. · level: research-level

<details><summary>Original abstract</summary>

We study isolation in the binomial random graph $G(n,p)$. When $p=o(1)$ and $np\to\infty$, allowing an $F$-free graph on the undominated vertices gives the same first-order asymptotics for every fixed forest $F$ as the domination number $\gamma(G)$ in $G(n,p)$. For the ordinary isolation number $\iota(G)$ ($F$ is an edge) we prove two-point concentration when $p$ is bounded away from $1$ and $np^2/(\log n)^3\to\infty$. We also identify a transition in the gap $\gamma(G)-\iota(G)$ when $\log(1/p)=o(\log n)$. This gap tends to infinity in probability when $p$ is well below $(\log\log n/\log n)^2$ and is at most one with high probability when $p$ is well above this scale. Finally, for every fixed graph $F$, we show that the classical minimum degree bound for domination is asymptotically sharp for $F$-isolation, even for regular host graphs.

</details>

## Differential geometry

### [Projectively Flat Spherically Symmetric Sprays of Constant Curvature](https://arxiv.org/abs/2611.27723)
*Yajing Gui, Benling Li* · `math.DG` · arXiv:2611.27723v1 · relevance 0.11

- **In one sentence**: The paper classifies projectively flat, spherically symmetric sprays of constant curvature by solving the equations that constant curvature imposes on the projective factor p(r,s), obtaining four explicit families that include the spray cases for constant flag curvature K = 0, -1, and 1.
- **In plain words**: This is a pure mathematics paper about "sprays," which are rules describing how straight-line-like paths behave on a curved space, the kind used in Finsler geometry (a generalization of Riemannian geometry where distances can depend on direction). The authors write down the conditions that make such a spray have constant curvature, solve them, and sort every possible solution into four explicit families. They also check that the known constant-curvature examples with curvature 0, -1, and 1 fall inside these families.
- **Why it matters**: The result gives a complete list rather than a set of examples, which matters for anyone studying which curved geometries of this type exist. The text does not describe applications outside geometry, so its wider relevance is uncertain.
- **Background needed**: - Manifold: a space that looks locally like ordinary Euclidean space, on which calculus can be done.
- Finsler metric: a way of measuring length in which the length of a vector can depend on its direction, generalizing Riemannian metrics.
- Spray: a geometric object on the space of directions that determines the "natural paths" (geodesics) of a Finsler metric.
- Projective flatness: the spray's paths match straight lines up to reparametrization, the Finsler analogue of a flat-looking geometry.
- Spherical symmetry: the spray looks the same in all directions around a point, so it depends only on the radius r and a direction variable s.
- Flag curvature: a measure of how curved the space is along a given 2-dimensional direction; constant means the same everywhere and in all directions.
- Projective factor p(r,s): the function that encodes the spray's projective structure and is solved for in the paper. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study projectively flat spherically symmetric sprays of constant curvature. We derive a system of equations that is equivalent to the constant-curvature condition for such sprays and solve it to obtain a complete classification of the projective factor \(p(r,s)\) into four explicit families. We further show that the sprays induced by projectively flat spherically symmetric Finsler metrics of constant flag curvature \(K=0\), \(K=-1\), and \(K=1\) are all special cases of our classification, thereby confirming that the sprays induced by these constant-flag-curvature Finsler metrics are fully contained in our framework.

</details>

### [A local symmetry forces positivity for projectively induced Kahler-Einstein metrics](https://arxiv.org/abs/2611.27345)
*Filippo Salis* · `math.DG` · arXiv:2611.27345v1 · relevance 0.10

- **In one sentence**: The paper shows that a projectively induced Kähler–Einstein metric must have positive Einstein constant whenever it has at least one nonzero local real-holomorphic Killing field, with no completeness or global group-action assumption, and extends this to a non-Einstein obstruction and compact equivariant continuations.
- **In plain words**: The paper studies curved geometric shapes that sit inside a flat-style projective space and carry a specific kind of balanced, evenly curved structure. The authors show that if such a shape has even a local symmetry (a smooth flow that preserves the geometry in a neighbourhood), then its curvature must be strictly positive, so negative and zero curvature are ruled out. The argument uses a global extension of the local symmetry, which the text describes as coming from a known rigidity result of Calabi.
- **Why it matters**: The general question of whether such embedded Kähler–Einstein submanifolds of projective space must have positive curvature is open, and this gives a partial answer under a local symmetry hypothesis. The text does not say how far the method extends beyond this setting, so its wider reach is uncertain.
- **Background needed**: - Kähler manifold: a complex geometric space with a compatible notion of distance and angle.
- Kähler–Einstein metric: a Kähler metric whose Ricci curvature is a constant multiple of the metric; the sign of that constant (positive, zero, negative) is the key quantity.
- Projective space and submanifold: the complex analogue of the sphere-like space of lines through the origin; a submanifold is a smaller shape embedded inside it.
- Killing field: a smooth vector field whose flow preserves the metric, i.e. a continuous symmetry.
- Real-holomorphic vector field: a flow that respects the complex structure.
- Calabi rigidity: a result saying that local symmetries of such embeddings extend in a controlled way.
- Omori–Yau maximum principle and Yau's Liouville theorem: standard tools for showing that certain bounded functions on non-compact spaces must be constant.
- Hulin's continuation: a known construction extending the embedded metric; the text uses it as an input. · level: research-level

<details><summary>Original abstract</summary>

We prove that a projectively induced Kahler-Einstein metric has positive Einstein constant as soon as it admits one nonzero local real-holomorphic Killing field. Neither completeness nor a prescribed global group action is assumed. This gives a partial answer, under a local symmetry hypothesis, to the general positivity problem for Kahler-Einstein submanifolds of (finite-dimensional) projective space. The key observation is that, by Calabi rigidity, a local real-holomorphic Killing field is induced by a projective unitary vector field whose tangency propagates along any connected global Kahler immersion, without a simple-connectivity assumption. Applied to Hulin's complete continuation, this produces a global Killing field with a bounded Hamiltonian potential given by the ambient projective moment map. The resulting Laplace equation, the Omori--Yau maximum principle and Yau's Liouville theorem exclude both negative and zero Einstein curvature. We also prove a non-Einstein obstruction under uniformly negative Ricci curvature and obtain compact equivariant continuations.

</details>

## Partial differential equations

### [Overview and recent progress on the classical Bernoulli free boundary problem](https://arxiv.org/abs/2611.26636)
*Xavier Fern\'andez-Real* · `math.AP` · arXiv:2611.26636v1 · relevance 0.42

- **In one sentence**: A survey of the classical Bernoulli (one-phase) free boundary problem in PDE theory, emphasizing recent progress.
- **In plain words**: This is an overview article about a mathematical problem where a function is defined in a region, but the edge of that region is not known in advance and must be found as part of the solution. The text is a short abstract that says the survey covers the Bernoulli or one-phase version of this problem and highlights recent progress. The abstract does not list specific results, so details of what was found cannot be taken from it.
- **Why it matters**: Free boundary problems model settings such as fluid flow, heat spread and phase changes, where the shape of a boundary is part of the answer. The abstract gives no specific results or links to applications, so its wider relevance cannot be judged from the text alone.
- **Background needed**: - A partial differential equation (PDE) describes how a quantity, such as temperature or pressure, varies across space.
- A free boundary is an edge of a region whose position is unknown and must be solved for along with the function.
- The Bernoulli (one-phase) problem is a classic example in which the function is zero on one side of the boundary and the rate of change across the boundary is tied to the boundary's shape.
- A survey is a review that collects and organizes existing work rather than presenting new results. · level: research-level

<details><summary>Original abstract</summary>

This survey gives an overview of the Bernoulli or one-phase free boundary problem, with emphasis on recent progress.

</details>

### [On the fully nonlinear degenerate parabolic quenching problem](https://arxiv.org/abs/2611.27774)
*Seunghyun Kim, Jos\'{e} Miguel Urbano* · `math.AP` · arXiv:2611.27774v1 · relevance 0.19

- **In one sentence**: The paper studies a fully nonlinear, degenerate parabolic quenching (free boundary) problem with a gradient-dependent operator, proving existence of nonnegative viscosity solutions with prescribed boundary data, an optimal upper growth rate along the free boundary, and matching non-degeneracy estimates.
- **In plain words**: The paper looks at a time-dependent equation in which a quantity u must stay nonnegative, and the region where u is positive has a moving edge called the free boundary. The authors show that a suitable solution exists for given nonnegative boundary values, and they pin down how fast u can grow as one approaches that edge. They also prove that u cannot be too flat near the edge, with estimates matched to the natural time-and-space scaling of the problem.
- **Why it matters**: Free boundary problems of this type model situations where a process turns off or saturates once a quantity reaches zero, so the sharp growth and non-degeneracy bounds describe how the solution behaves at that switching edge. The text does not describe specific applications, so any wider connection is uncertain; the work is mainly a technical contribution to the theory of fully nonlinear equations.
- **Background needed**: - Parabolic equation: an equation describing evolution in time, like heat spreading, with u_t the rate of change in time.
- Free boundary: the edge between the region where the solution is positive and where it is zero; its location is part of the answer.
- Fully nonlinear, degenerate operator: the equation depends non-linearly on the second derivatives (and here on the size of the gradient |Du|), and can lose ellipticity in some directions; convex or concave uniformly elliptic F means F is bounded in a controlled way.
- Viscosity solution: a weak notion of solution that works when classical derivatives may not exist.
- Growth rate and non-degeneracy: how fast the solution rises away from the edge and a lower bound ensuring it does not flatten out.
- Scaling: parabolic cylinders are regions adapted to the equation's time-space scaling, so estimates hold at every size.
- Barrier arguments and compactness: standard tools for building comparison functions and extracting convergent subsequences of solutions. · level: research-level

<details><summary>Original abstract</summary>

We study the fully nonlinear degenerate parabolic free boundary problem $$|Du|^\kappa F(D^2u)-u_t=u^{\gamma-1} \qquad \textrm{in} \quad \{u>0\},$$ where $\kappa>0$, $0<\gamma<1$, and $F$ is a convex or concave uniformly elliptic operator with $F(0)=0$. We establish the existence of a nonnegative viscosity solution with prescribed continuous nonnegative boundary data and prove its optimal upper growth along the free boundary, together with matching non-degeneracy estimates in parabolic cylinders adapted to the scaling. Our approach combines a weak Bernstein estimate with barrier arguments to obtain local compactness and boundary attainment. To obtain the optimal growth rate, we further use persistence of positivity for limits with vanishing absorption coefficients to identify the homogeneous equation across the zero set, and then combine the optimal spatial regularity estimate of \cite{LLYZ25} with an iteration argument.

</details>

## Harmonic analysis

### [Freedom is all you need](https://arxiv.org/abs/2611.27943)
*Julian Bushelli, James Eldred Pascoe* · `math.FA` · arXiv:2611.27943v1 · relevance 0.14

- **In one sentence**: The paper begins a representation theory that relates a generic free functional calculus (for matrices and operators, over categories) to the classical noncommutative functional calculus of Taylor and Voiculescu, and notes consequences for domains that are closed under direct sums and similarity changes of coordinates.
- **In plain words**: The paper is about a way of applying functions to grids of numbers (matrices) and to more abstract operators, where the inputs can be non-commuting. It starts a general framework that links a newer "free" version of this calculus to the older classical version. The abstract only states that this framework is initiated and gives some properties of the resulting function classes; it does not give the detailed results.
- **Why it matters**: The abstract connects the framework to complex analysis and to large parallel networks, and it suggests a possible but explicitly "hypothetical" explanation for why overfitting can sometimes be harmless in such networks. That link is speculative as stated, and the text alone does not show how far it goes.
- **Background needed**: - Functional calculus: a way of plugging a matrix or operator into a function (like a polynomial or power series) and getting a matrix or operator back.
- Matrices do not generally commute (AB may differ from BA), so "noncommutative" versions of these ideas are harder than the usual scalar case.
- Similarity (change of coordinates): rewriting a matrix in a different basis; a domain is "similarity invariant" if the property is preserved under such rewriting.
- Direct sum: stacking matrices block-diagonally.
- Category: an abstract framework of objects and maps between them, used here as the setting for the free calculus.
- Analyticity: a function that is locally given by a convergent power series; "monodromy" refers to how analytic continuation around loops can change a function.
- Overfitting: a machine learning model fitting training data very closely, including noise. · level: research-level

<details><summary>Original abstract</summary>

The functional calculus allows for the rigorous analysis of functions of matrices or even operators. The free functional calculus gives the natural class of functions over any category. We initiate the representation theory for taking a generic free functional calculus to the classical nc functional calculus going back to Taylor, Voiculescu and many others, with an eye towards learning of categories. The functional calculus on direct sum closed and locally similarity (i.e. change of coordinates) invariant domains inherits the niceties of complex analysis and large-scale parallel networks, such as automatic analyticity, free universal monodromy, which gives a hypothetical explanation for beneficial overfitting.

</details>

### [The Ritt problem is decidable](https://arxiv.org/abs/2611.27008)
*Jason Fang, James Freitag, Matthew Harrison-Trainor* · `math.AC` · arXiv:2611.27008v1 · relevance 0.14

- **In one sentence**: The paper claims a positive answer to the Ritt problem, which asks whether a certain algorithmic decision question about functional decompositions of polynomials and related functions is solvable.
- **In plain words**: This paper settles a long-standing question about how complicated formulas can be broken into simpler pieces. The Ritt problem asks whether there is a reliable procedure that can decide if two such breakdowns of a formula are equivalent. The text says the authors give a positive answer, meaning such a procedure exists, but the short summary does not spell out the method.
- **Why it matters**: The text is only a one-sentence abstract, so its importance cannot be judged from it alone. Results of this kind matter to researchers in algebra, dynamics and computer algebra, since they settle whether a class of questions can be answered by computation at all.
- **Background needed**: - Polynomials: sums of powers of a variable, such as x^2 + 3x.
- Functional decomposition: writing a function as a composition of simpler functions, e.g. f(g(x)).
- Ritt's theory: classical results by Joseph Ritt (1920s–1930s) on when and how such decompositions can be rearranged.
- Decidability: whether a yes/no question can be answered by a fixed, always-terminating algorithm.
- Harmonic analysis is the listed field, but the abstract itself concerns algebraic decomposition problems; the link is not explained in the text. · level: research-level

<details><summary>Original abstract</summary>

We give an affirmative solution to the Ritt problem.

</details>

## Complex analysis

### [An affine surface with 3-step nilpotent fundamental group](https://arxiv.org/abs/2611.27475)
*Sergey Polevoy, Vasily Rogov* · `math.AG` · arXiv:2611.27475v1 · relevance 0.09

- **In one sentence**: The paper constructs a smooth complex affine surface whose fundamental group is virtually 3-step nilpotent but not virtually 2-step nilpotent, giving a negative answer to the quasi-projective version of Campana's nilpotency problem.
- **In plain words**: The paper is about the shapes that complex algebraic surfaces can have, as seen through their "loops" (the fundamental group, a way of recording which closed paths can be deformed into one another). The author builds a specific smooth surface of this kind whose loop structure is nested three levels deep but not two, which settles a question in the negative.
- **Why it matters**: The result answers a specific open question (a version of Campana's nilpotency problem) by showing the answer is no in the quasi-projective setting. Beyond that, the text does not say more about wider implications, so its significance beyond this question is unclear from the summary alone.
- **Background needed**: - Complex affine surface: a smooth solution set of polynomial equations in two complex variables, with the points at infinity removed.
- Fundamental group: a group recording which loops on a space can be continuously deformed into one another.
- Nilpotent group: a group that becomes trivial after repeatedly taking commutators; "k-step nilpotent" measures how many such levels are needed.
- Virtually nilpotent: the group has a finite-index subgroup that is nilpotent.
- Campana's nilpotency problem: a conjectural link between the loop structure of a space and its nilpotency, asked in the projective and quasi-projective settings.
- Quasi-projective: a space that is an open subset of a projective (compact-type) algebraic variety. · level: research-level

<details><summary>Original abstract</summary>

We construct a smooth complex affine surface $Y$ such that $\pi_1(Y)$ is virtually $3$-step nilpotent, but not virtually $2$-step nilpotent. This gives a negative answer to the quasi-projective version of Campana's nilpotency problem.

</details>

### [Local connectivity of Julia sets of Newton maps of trigonometric and hyperbolic functions](https://arxiv.org/abs/2611.26654)
*Molla Basir Ahamed, Sayantan Chakraborty* · `math.DS` · arXiv:2611.26654v1 · relevance 0.07

- **In one sentence**: The paper proves local connectivity of Julia sets (the boundaries between stable and chaotic behaviour) for Newton maps of sin, cos, sinh and cosh, by verifying repelling petals at infinity for the cosine map and showing the hyperbolic family is affinely conjugate to the sine case.
- **In plain words**: The paper studies a method for finding roots of equations, called Newton's method, applied to four standard trigonometric and hyperbolic functions, and asks how the boundary between starting points that converge and those that do not is shaped. The authors show that for the cosine version, certain half-plane regions far from the origin behave in a way that lets an existing mathematical criterion apply, giving a clean boundary shape. They also show that a whole family of hyperbolic functions is, after a change of coordinates, the same as the sine version, so a previously published result covers them too.
- **Why it matters**: It settles a structural question about the boundaries of these dynamical systems for a whole family of maps by reducing them to one known case. Its wider relevance is mainly to specialists in complex dynamics; the text does not claim applications beyond that field.
- **Background needed**: - Newton's method: an iterative rule for approximating roots of an equation; each starting point is mapped step by step.
- Julia set: the boundary between starting points whose iterates behave tamely and those that behave chaotically.
- Basin of attraction: the set of starting points that converge to a given attracting point; "immediate" means the component touching that point directly.
- Transcendental meromorphic function: a complex function that is not a polynomial or rational function, with poles allowed, such as sin or cos.
- Local connectivity: a topological property saying the boundary is not pinched in a way that makes it hard to approach locally; here it is stated for the boundary of each basin.
- Repelling petal: a region near infinity where iteration pushes points away, used as a technical tool.
- Affine conjugacy: two maps are the same up to a linear change of coordinates. · level: research-level

<details><summary>Original abstract</summary>

We study the Newton maps of $\sin z$, $\cos z$, $\sinh z$, and $\cosh z$, each of which is transcendental meromorphic and has infinitely many unbounded immediate attracting basins. We first verify directly that, for the cosine Newton map $N_{\cos}(z) = z + \cot z$, the half-planes $\{\pm \operatorname{Im} z > M\}$ are repelling petals at infinity for every $M \ge 2$. These explicit petals allow us to apply the tame-basin criterion of Bara\'nski, Fagella, Jarque, and Karpi\'nska and obtain local connectivity of the spherical boundary of each immediate basin of $N_{\cos}$. We also show that the Newton map of $Ae^{\lambda z} + Be^{-\lambda z}$, where $AB\lambda \neq 0$, is affinely conjugate to the sine Newton map $N_{\sin}(z) = z - \tan z$. The published local-connectivity theorem for $J(N_{\sin})$ therefore applies to this entire family, including the cosine and the two hyperbolic Newton maps. We describe the invariant lines and basin geometry of the four maps and illustrate the corresponding dynamical planes numerically.

</details>

## Operator algebras and spectral theory

### [On the AF embedding problem](https://arxiv.org/abs/2611.27471)
*Christopher Schafhauser* · `math.OA` · arXiv:2611.27471v1 · relevance 0.17

- **In one sentence**: A survey of the AF-embedding problem for C*-algebras, centred on the author's result that separable, exact, UCT C*-algebras with a faithful quasidiagonal trace embed into a unital simple AF algebra.
- **In plain words**: This paper is a survey about when a mathematical object called a C*-algebra can be placed inside a simpler kind of algebra, one built up step by step from finite-dimensional pieces. The main content, based on the author's earlier paper, is a sufficient condition for this kind of embedding to exist. The text also mentions some other results but gives only a brief outline of them.
- **Why it matters**: Embedding a complicated algebra into a simpler, well-understood one is a standard way to learn about the original, so results of this type help organise the field. The text does not say how far these results reach beyond operator algebras, so any wider connection is uncertain.
- **Background needed**: - A C*-algebra is a collection of bounded linear operators on a Hilbert space (a space of possible states or waves), closed under addition, multiplication, and taking adjoints.
- An AF (approximately finite dimensional) algebra is a limit of a growing chain of finite-dimensional matrix-type algebras.
- "Embedding" means placing one algebra inside another as a copy of a subalgebra.
- Terms like exact, UCT, quasidiagonal, faithful trace, and simple are technical properties of these algebras; each is a condition restricting which algebras qualify.
- Familiarity with linear algebra and basic functional analysis is needed. · level: research-level

<details><summary>Original abstract</summary>

This article gives a survey of the AF-embedding problem for $C^*$-algebras. The problem asks when a given $C^*$-algebra $A$ embeds into an \emph{approximately finite dimensional} (AF) $C^*$-algebra (a direct limit of finite dimensional $C^*$-algebras). This is largely based on my paper ``Subalgebras of simple AF algebras,'' which shows that separable, exact $C^*$-algebras satisfying the UCT and admitting a faithful, quasidiagonal trace embed into a unital, simple AF algebra. Some other results are also discussed.

</details>

### [Rigidity in the Lichnerowicz inequality for word-length semigroups](https://arxiv.org/abs/2611.27204)
*Melchior Wirth* · `math.OA` · arXiv:2611.27204v1 · relevance 0.15

- **In one sentence**: The paper shows that, for word-length semigroups on group von Neumann algebras, equality in two noncommutative Lichnerowicz-type spectral gap inequalities (the complete Γ2 constant of Junge–Zeng and the geometric Ricci constant of Junge–LaRacuente–Li) holds exactly when the group's Cayley graph is a partial cube.
- **In plain words**: The paper studies a rate at which a random-walk-like process on a group settles down to equilibrium, and how that rate compares with a geometric bound. The authors ask when the bound is exactly tight, and they find that tightness happens precisely when the group's Cayley graph (the picture of the group's elements linked by generator steps) can be drawn isometrically inside a hypercube, a class called partial cubes. The text given is only the abstract, so the details of the proofs are not visible here.
- **Why it matters**: It gives a precise graph-theoretic characterization of when a noncommutative geometric inequality is sharp, linking operator algebras to discrete geometry. The abstract alone does not show how broadly the result extends beyond word-length semigroups.
- **Background needed**: - Group von Neumann algebra: an operator-algebra version of a discrete group, used to model quantum systems built from a group.
- Quantum Markov semigroup: a family of maps describing how a quantum system evolves randomly over time, analogous to a random walk.
- Spectral gap: the smallest nonzero eigenvalue of a generator; it controls how fast the process mixes toward equilibrium.
- Lichnerowicz inequality: a classical bound relating spectral gap to curvature-like geometric quantities; here its noncommutative versions are studied.
- Cayley graph: a graph whose vertices are group elements, with edges given by multiplying by generators.
- Partial cube: a graph that embeds isometrically (distances preserved) into a hypercube.
- Word-length semigroup: a semigroup of operators generated by the length of group elements measured in generators. · level: research-level

<details><summary>Original abstract</summary>

We give an operator-algebraic characterization of Cayley graphs that are partial cubes, that is, embed isometrically into a hypercube. More precisely, noncommutative versions of the Lichnerowicz inequality control the spectral gap of the generator of a quantum Markov semigroup by the constant in the complete $\Gamma_2$-criterion of Junge and Zeng or the constant in the geometric Ricci criterion of Junge, LaRacuente and Li. We show that for word-length semigroups on group von Neumann algebras, equality in either of these inequalities occurs exactly when the Cayley graph is a partial cube.

</details>

## Algebra

### [On coherence of enveloping algebras of infinite-dimensional Lie algebras](https://arxiv.org/abs/2611.27824)
*Susan J. Sierra, James Timmins* · `math.RA` · arXiv:2611.27824v1 · relevance 0.22

- **In one sentence**: The paper determines when universal enveloping algebras of infinite-dimensional Lie algebras (notably loop algebras and the Witt algebra) are coherent, and studies coherence of related graded and filtered rings.
- **In plain words**: The paper studies a property called "coherence" for a family of algebraic structures built from infinite-dimensional symmetry-like objects (Lie algebras). Coherence is a tidy-behaviour condition: roughly, certain systems of equations have solutions that are finitely described. The authors show that for loop algebras the property holds exactly when the underlying finite-dimensional algebra is nilpotent, and they find that several specific examples fail it.
- **Why it matters**: It sharpens what is known about which infinite-dimensional algebras behave well under standard finiteness conditions, and it extends earlier work on non-Noetherianity of the Witt-algebra enveloping algebra. The text does not indicate further applications beyond this algebraic classification.
- **Background needed**: - Lie algebra: a vector space with a bracket operation, used to describe continuous symmetries.
- Universal enveloping algebra U(g): a ring built from a Lie algebra g that encodes its representations.
- Loop algebra: functions from a circle (or Laurent polynomials) with values in a finite-dimensional Lie algebra.
- Witt algebra: the derivations of Laurent polynomials, an infinite-dimensional example.
- Coherent ring: a ring where finitely generated one-sided ideals are finitely presented; a finiteness property.
- Noetherian ring: every ideal is finitely generated; coherence is a weaker related condition.
- Nilpotent: a Lie algebra whose repeated brackets eventually vanish.
- Graded and filtered rings: rings split into pieces indexed by integers or ordered by a size-like filtration; the Rees ring links the two. · level: research-level

<details><summary>Original abstract</summary>

We investigate when the universal enveloping algebra $U(\mathfrak{g})$ of an infinite-dimensional Lie algebra $\mathfrak{g}$ is coherent. We show that if $\mathfrak{g}$ is the loop algebra of a finite-dimensional Lie algebra $\mathfrak{h}$ then $U(\mathfrak{g})$ is coherent exactly when $\mathfrak{h}$ is nilpotent. As a consequence, we show that $U(\mathfrak{g})$ is not coherent if $\mathfrak{g}$ is complex, simple, $\mathbb{Z}$-graded, of polynomially bounded growth, and not isomorphic to the Witt algebra $W = \mathrm{Der} \mathbb{C}[t,t^{-1}]$ or its one-sided version. We also demonstrate that the homomorphic image of $U(W)$ used to prove non-Noetherianity of $U(W)$ in previous work of the first author and Walton is not coherent. On the other hand, we establish that two closely related connected graded rings are graded coherent. Finally, we prove that any exhaustively filtered ring is coherent if its Rees ring is graded coherent.

</details>

### [Large orbits of $p$-groups on conjugacy classes of arbitrary finite groups](https://arxiv.org/abs/2611.27916)
*Thomas Michael Keller* · `math.GR` · arXiv:2611.27916v1 · relevance 0.19

- **In one sentence**: The paper extends a known result on large orbits of coprime p-group actions from solvable to arbitrary finite groups, showing via the classification of finite simple groups that some conjugacy class (or irreducible character) has stabilizer of order at most |P|^{1/2}, with a new nonsolvable family attaining the bound.
- **In plain words**: This paper is about symmetries of finite groups: a small group P of symmetries (of prime-power size) acts on a finite group H, and the question is how many elements of H P can leave mostly in place. The author-level result is that, for every such action, some conjugacy class of H has a stabilizer in P of size at most the square root of |P|. A previous paper had proved this only when H is solvable, and this paper removes that restriction, using the classification of finite simple groups.
- **Why it matters**: The bound is sharp: the text says it is attained, and the paper gives a new family of nonsolvable examples where it is reached. The result also gives, as a consequence, an irreducible character of H whose inertia group in P is small, which links the question to representation theory; the text does not say more about wider applications.
- **Background needed**: - Finite group: a group with finitely many elements, such as the symmetries of a finite object.
- p-group: a group whose size is a power of a prime p.
- Acting coprimely and faithfully: P applies symmetries to H in a way that is nontrivial and does not share prime factors with H's order in a problematic way.
- Conjugacy class: a set of elements of H that are equivalent under relabeling by H itself.
- Stabilizer / orbit: the stabilizer is the set of symmetries in P fixing a given class; the orbit is the set of classes it moves it to. Large orbit means small stabilizer.
- Solvable group: a group built up by stacking simple pieces that are abelian; nonsolvable groups contain more complex simple pieces.
- Classification of finite simple groups: a large completed classification of the basic building blocks of finite groups, used as a tool here.
- Irreducible character and inertia group: basic objects of representation theory; the inertia group is the set of symmetries that preserve a given character. · level: research-level

<details><summary>Original abstract</summary>

Let $P$ be a $p$-group that acts faithfully and coprimely on a finite group $H$. In a previous paper it was shown that if $H$ is solvable, then there exists a conjugacy class $c$ of $H$ whose stabilizer in $P$ has order at most $|P|^{1/2}$, and that this bound is best possible. In this paper we remove the hypothesis that $H$ is solvable. As a consequence, there always exists an irreducible character of $H$ whose inertia group in $P$ has order at most $|P|^{1/2}$. The proof depends on the classification of finite simple groups. Its main new ingredient is a result on quasiprimitive linear actions of $p$-nilpotent groups which shows that the elements acting as field automorphisms can be ignored when one looks for vectors with small stabilizers. We also present a new family of examples, with nonsolvable $H$, in which the bound is attained.

</details>

## Representation theory

### [The $n!$ theorem via quaternionic rotation of Cherednik algebras](https://arxiv.org/abs/2611.27113)
*Stephen Griffeth* · `math.RT` · arXiv:2611.27113v1 · relevance 0.13

- **In one sentence**: The paper gives a new proof of the n! theorem (a result about the dimension of certain representations of Cherednik algebras, which are algebras attached to symmetric groups and related reflection groups), using an analogue of rotating complex structures coming from a quaternion action.
- **In plain words**: This is a mathematics paper about a known result called the "n! theorem," which concerns a family of algebraic objects built from symmetric groups (the groups of ways to rearrange n items). The authors give a new proof of it. Their method uses a trick borrowed from geometry: rotating the structure that makes a space "complex," using an action of the quaternions, a number system extending the complex numbers.
- **Why it matters**: The text is short, so it does not say what new consequences the new proof gives or how it compares to earlier proofs. Its value is mainly as an alternative route to a known theorem, which may connect representation theory with geometry, though the text does not spell out these links.
- **Background needed**: - Representation theory: studying abstract groups or algebras by how they act on vector spaces.
- Symmetric group: the group of all rearrangements of n objects; it has n! elements.
- Cherednik algebras: a family of algebras depending on parameters, built from reflection groups, used to study such representations.
- The n! theorem: a known result in this area, which the paper re-proves; the text does not state its exact form.
- Quaternions: an extension of the complex numbers with three imaginary units; "rotating complex structures" means changing which linear map plays the role of multiplication by i.
- Background in abstract algebra at the graduate level is assumed. · level: research-level

<details><summary>Original abstract</summary>

We give a proof of the $n!$ theorem based on the representation theory of Cherednik algebras and an analog of the rotation of complex structures arising from an action of the quaternions.

</details>

### [The weighted fundamental lemma for non-split groups](https://arxiv.org/abs/2611.26750)
*Cass Halleck-Dub\'e* · `math.RT` · arXiv:2611.26750v1 · relevance 0.12

- **In one sentence**: The paper proves the Weighted Fundamental Lemma for Lie algebras over unramified quasi-split groups by adapting the Chaudouard–Laumon geometric method (via ξ-stable Higgs bundles and a Frobenius point count), and derives Waldspurger's nonstandard version and a twisted version in good characteristic.
- **In plain words**: This is a paper in pure mathematics about symmetry groups and the counting identities that link them, which underpin the study of automorphic forms (highly symmetric functions on number-theoretic spaces). The authors extend a known result, the Weighted Fundamental Lemma, from split groups to a wider class called quasi-split groups. They do this by adapting an existing geometric proof, building a suitable family of algebraic objects over a curve and counting points on them.
- **Why it matters**: The text says the result is a step needed to complete Moeglin–Waldspurger's stabilization of the twisted trace formula, and that it makes the endoscopic classification for classical groups unconditional. Its wider significance rests on those downstream consequences, which I have not checked and which the text only asserts.
- **Background needed**: - Reductive group: a continuous symmetry group of algebraic type, such as matrix groups.
- Quasi-split and unramified: a special, relatively tame class of such groups over local number fields.
- Orbital integral: an averaged quantity over conjugacy classes, used to compare different trace formulas.
- Fundamental lemma: a identity comparing orbital integrals on a group and on an associated endoscopic group; the "weighted" and "Lie algebra" versions are refinements.
- Higgs bundle and Hitchin base: geometric objects on a curve and their parameter space, used as a tool for counting.
- Trace formula and endoscopy: frameworks in automorphic representation theory for classifying automorphic forms by comparing groups.
- Frobenius point count: counting solutions over finite fields as a route to an identity. · level: research-level

<details><summary>Original abstract</summary>

In this work, we prove the Weighted Fundamental Lemma for Lie algebras for general (quasi-split) unramified $G$. The strategy is to adapt the proof of Chaudouard--Laumon from the split case. In particular, we define the notion of a $\xi$-stable Higgs bundle for a quasi-split reductive group scheme $G$ on a curve, and prove that the stack of such form a proper, finite-type Deligne--Mumford stack over the Hitchin base when $G$ has anisotropic center. We then adapt the global cohomological theorem of Chaudouard--Laumon to the quasi-split setting, and perform the required Frobenius-point count to obtain an identity of adelic orbital integrals. A local-to-global argument deduces the WFL for Lie algebras. In the last chapter, we perform a parallel reduction to deduce Waldspurger's nonstandard WFL from a global version which follows from the same geometric theory. Our work implies the Twisted Weighted Fundamental Lemma in good characteristic, which completes Moeglin--Waldspurger's stabilization of the twisted Arthur--Selberg trace formula. We therefore render unconditional the endoscopic classification for classical groups and an array of downstream consequences in automorphic theory.

</details>

## Number theory

### [Splitting types of Richelot isogenies over finite fields and a newform of weight four](https://arxiv.org/abs/2611.27775)
*Hung Dang* · `math.NT` · arXiv:2611.27775v1 · relevance 0.17

- **In one sentence**: Counts factorizations of square-free sextics over finite fields into three quadratics, with splitting conditions, via Richelot isogenies of genus-2 curves, with the answer expressed through the trace of a weight-4 newform of level 8 and a twisted second moment of the Legendre family.
- **In plain words**: This paper studies a counting problem: how many ways a polynomial of degree six, over a finite field with q elements, can be split into three quadratic pieces, when we also track which of those pieces factor further over the field. The authors give an exact formula for each of the 64 possible splitting patterns. The formulas involve a known number-theoretic quantity tied to a specific modular form, and the proof reduces the counting, by elementary means, to a known hypergeometric value.
- **Why it matters**: The result links a concrete counting question about polynomials and genus-2 curves to a specific modular form, which is a meaningful connection between two areas of number theory. The text does not say much about wider applications, so its broader significance is best judged by specialists.
- **Background needed**: - A finite field F_q is a set with q elements, where q is a prime power; arithmetic is done modulo the field's structure.
- A square-free sextic is a degree-six polynomial with no repeated roots; splitting it into three monic quadratics is a factorization.
- A genus-2 curve is a curve of "genus" (number of holes) two; its Jacobian splits or relates to elliptic curves.
- A (2,2)-isogeny is a structure-preserving map between abelian varieties with a kernel of order four; the Richelot construction produces the dual quadratics.
- Splitting behaviour refers to whether a quadratic has roots in F_q or not.
- A newform is a special modular form; its trace of Frobenius is an integer tied to counting points mod p.
- The Legendre family is a standard family of elliptic curves; a twisted second moment is an averaged sum over that family.
- The paper says the value was evaluated for primes by Ahlgren and Ono. · level: research-level

<details><summary>Original abstract</summary>

A factorization $f=uvw$ of a square-free sextic over a finite field $\mathbb{F}_q$ of odd characteristic into three monic quadratics defines a genus-2 curve with a rational $(2,2)$-isogeny kernel, and the Richelot construction attaches to it three dual quadratics $U,V,W$. We determine, for every odd prime power $q$, the number of such factorizations with prescribed splitting behaviour over $\mathbb{F}_q$ of all six quadratics. Each of the $64$ counts is $q(q-1)(q+1-n_f)/64$ times $C(q)\pm t_q$, where $n_f$ is the number of roots of $f$ in $\mathbb{F}_q$, $C$ is an explicit monic cubic, and $t_q$ is the trace of Frobenius attached to the newform $\eta(2z)^{4}\eta(4z)^{4}$ of weight $4$ and level $8$. The proof reduces the counts by elementary means to a twisted second moment of the Legendre family of elliptic curves, which is a value of a hypergeometric function over $\mathbb{F}_q$ evaluated by Ahlgren and Ono for primes. As consequences, the number of factorizations whose three pairwise resultants lie in one square class is a polynomial in $q$, with proportion $1/4+3/(4q^{2})+O(q^{-4})$. When the quotient is a product of two elliptic curves conjugate over $\mathbb{F}_{q^2}$, we prove that the splitting of the factors $u,v,w$ over $\mathbb{F}_q$ decides which points of order two of the elliptic factor are divisible by two.

</details>

### [An explicit Cassels--Tate pairing in characteristic $2$ and the parity of $2$-Selmer ranks](https://arxiv.org/abs/2611.27040)
*Abhishek Shukla* · `math.NT` · arXiv:2611.27040v1 · relevance 0.17

- **In one sentence**: For ordinary elliptic curves over global fields of characteristic 2 with a rational 2-torsion point, the paper gives an explicit local-symbol formula for the Cassels–Tate pairing on the 2-torsion of Sha, relates it to Kramer's descent pairing and Milne's flat duality, and uses it to express the parity of rk A(K) + dim Sha(A/K)[2] via local terms and root numbers.
- **In plain words**: This paper studies elliptic curves, smooth curves defined by cubic equations, over number-like fields where arithmetic works in characteristic 2 (a setting where numbers behave like binary digits). It concerns a hidden group called Sha that measures how far certain rational solutions fail to exist globally despite existing locally. The authors give an explicit formula for a pairing that organises this hidden group and show it matches other known descriptions, which lets them determine the parity (even or odd) of a key count in terms of local data.
- **Why it matters**: Parity questions about ranks of rational points are central to arithmetic geometry, and the paper ties an algebraic pairing to local root numbers, a link that is of interest to specialists. The text does not indicate wider consequences beyond this setting, and the extension to prime order rational points, including the new case where the prime equals the characteristic, is presented as a technical advance.
- **Background needed**: - Elliptic curve: a cubic curve with a group law on its rational points.
- Global field of characteristic 2: a function field or number field-like object where arithmetic is done modulo 2.
- Rank of A(K): the number of independent rational points of infinite order.
- Sha (Tate–Shafarevich group): obstructions to local solutions being global; its size is largely conjectural.
- 2-Selmer group and Cassels–Tate pairing: tools that detect elements of Sha and whose structure constrains ranks.
- Isogeny (Verschiebung) and 2-torsion: maps between curves and points of order 2.
- Artin–Schreier symbols: local pairing values used in characteristic 2.
- Local root numbers: local signs from the functional equation of L-functions, linked to parity of rank. · level: research-level

<details><summary>Original abstract</summary>

Let $K$ be a global field of characteristic $2$ and $\varphi\colon E\to E'$ the Verschiebung of an ordinary elliptic curve $E/K$ with a rational point of order $2$. We prove an explicit formula for the homogeneous-space Cassels--Tate pairing on $\Sha(E/K)[\varphi]$ as a sum of local Artin--Schreier symbols, show that it coincides with Kramer's descent pairing and, on $\Sha(E/K)[\varphi]$, with the pairing induced by Milne's flat duality, and deduce that it is non-degenerate on $\Sha(E/K)[\varphi]/\hat\varphi(\Sha(E'/K)[2])$. For every ordinary elliptic curve $A/K$ we express the parity of $\mathrm{rk}\,A(K)+\dim\Sha(A/K)[2]$ by local terms (after Kramer), and identify these with local root numbers at places of semistable or potentially multiplicative reduction, and in further cases using curves with finite $\Sha$. We determine $\Sha$ in examples, and extend the formula to rational points of any prime order $\ell$, the new case being $\ell=\operatorname{char}K$.

</details>

## Algebraic geometry

### [Combinatorial relative orientability for toric and tropical geometry](https://arxiv.org/abs/2611.27238)
*Nathan Tiggemann* · `math.AG` · arXiv:2611.27238v1 · relevance 0.25

- **In one sentence**: The paper gives a combinatorial criterion for relative orientability of vector bundles on smooth proper toric varieties, shows it is preserved under tropicalization, and applies this to a quadratically enriched Bernstein-Khovanskii-Kushnirenko theorem and to k-phase structures on tropical hypersurfaces.
- **In plain words**: Many counting problems in geometry ask how many solutions a system of equations has, and modern methods answer these by computing a single numerical invariant. This paper works on making that invariant well-defined over any field, and it translates the question into a simpler combinatorial setting called tropical geometry, where the problem reduces to counting on piecewise-linear shapes. The authors give a checkable combinatorial test for when the needed geometric data is consistent, and they show that the test carries over to the tropical setting.
- **Why it matters**: It offers a route for using tropical geometry, which turns hard algebra into combinatorics, to answer enumerative questions over arbitrary fields, not only over the complex numbers. The text itself only indicates this as a goal and a demonstration, so the broader impact is something to judge from the full paper.
- **Background needed**: - Enumerative geometry: counting solutions to geometric problems, such as how many curves satisfy given conditions.
- Vector bundle: a family of vector spaces attached smoothly to each point of a space; "relatively oriented" means a consistent choice of orientation is possible, which is needed for the count to be well-defined.
- Chern class and Euler class: invariants of vector bundles whose degree gives a count of solutions; the Euler class lives in Chow-Witt groups, a refined version that works over any field.
- A^1-homotopy theory: a framework from modern algebraic topology that lets topological tools be applied to algebraic varieties over arbitrary fields.
- Toric variety: an algebraic variety built from combinatorial data (a fan of cones), so its geometry can be read off from polytopes and lattices.
- Tropical geometry: a piecewise-linear shadow of algebraic geometry, where polynomial problems become problems about polyhedral complexes.
- Bernstein-Khovanskii-Kushnirenko theorem: a classical result counting solutions of polynomial systems via the volumes of their Newton polytopes.
- Quadratic enrichment: refining an integer count into a count valued in quadratic forms, which keeps track of extra arithmetic information.
- Phase structure: extra data on a tropical hypersurface that records signs; the real case is the classical version that the paper generalizes to k phases. · level: research-level

<details><summary>Original abstract</summary>

Many problems in enumerative geometry are solved by computing the degree of the top Chern class of a suitable vector bundle. Results from $\mathbb{A}^1$-homotopy theory allow to answer enumerative questions over arbitrary fields, replacing the top Chern class by the Euler class in Chow-Witt groups. For its degree to be well-defined, one needs the vector bundle to be relatively oriented. Another way to solve enumerative problems is to translate them to tropical geometry, where they become combinatorial problems. In this paper, we give a combinatorial description of relative orientability for vector bundles over smooth proper toric varieties. We show that it behaves well under tropicalization, establishing a tropical version of relative orientability, which will allow to the use of tropical geometry to answer enumerative questions over arbitrary fields. As a demonstration, we prove a quadratically enriched version of the Bernstein-Khovanskii-Kushnirenko theorem via tropical geometry. Lastly, we define the notion of $k$-phase structures on tropical hypersurfaces, generalizing the real case.

</details>

### [Classification of strongly $F$-regular and $F$-pure surface singularities with imperfect residue fields](https://arxiv.org/abs/2611.27597)
*Tatsuro Kawakami, Kenta Sato* · `math.AG` · arXiv:2611.27597v1 · relevance 0.12

- **In one sentence**: The paper classifies strongly F-regular and F-pure normal surface singularities over possibly imperfect residue fields, via weighted dual graphs and geometric reducedness of exceptional components of the minimal resolution, extending Hara's algebraically closed case.
- **In plain words**: The paper studies a family of "mild" singular points on surfaces, the kind of points where a shape folds in on itself, and asks when these points behave well under a specific arithmetic operation (the Frobenius map, which raises coefficients to a power p) in characteristic p. It works in a more general setting where the underlying number field need not be perfect, which the earlier classical results did not cover. The authors give a description of these singularities using the pattern of a graph built from the resolved surface, and they also list which graphs can occur for the weaker F-pure version.
- **Why it matters**: The work extends a known classification by Hara from algebraically closed fields to imperfect residue fields, so it covers a broader class of cases. The text also states a specific consequence: for F-pure surface singularities, the exceptional components are geometrically reduced unless the singularity is a rational double point. How far this reaches beyond surfaces is not stated in the text.
- **Background needed**: - Singularity: a point where a surface fails to be smooth, e.g. a cone tip.
- Minimal resolution: a way of replacing the singular point by a smooth surface with a chain or tree of curves, the exceptional components.
- Dual graph: a diagram with one node per exceptional curve and edges for intersections, weighted by numerical data.
- Characteristic p and Frobenius: working with arithmetic where adding p copies of 1 gives 0; Frobenius raises functions to the p-th power.
- F-regular / F-pure: technical "good behaviour under Frobenius" conditions indicating mild singularities.
- Residue field: the field of values at the singular point; "imperfect" means Frobenius is not surjective on it.
- Geometric reducedness: a curve stays reduced (no repeated components) after passing to an algebraic closure.
- Rational double point: a simple, well-classified type of surface singularity. · level: research-level

<details><summary>Original abstract</summary>

We study strongly $F$-regular and $F$-pure normal surface singularities whose residue fields are not necessarily perfect. We characterize strong $F$-regularity in terms of the weighted dual graph and geometric reducedness of the exceptional components of the minimal resolution, extending Hara's classification over algebraically closed residue fields. We also determine the possible dual graphs of $F$-pure surface singularities and give converse criteria. Notably, the exceptional components of an $F$-pure surface singularity are geometrically reduced unless the singularity is a rational double point.

</details>

## Topology

### [Persistent Mayer Path Homology and Mayer Path Laplacian](https://arxiv.org/abs/2611.26982)
*Dilan Karaguler, Guowei Wei* · `math.AT` · arXiv:2611.26982v1 · relevance 0.16

- **In one sentence**: The paper introduces persistent Mayer path homology and Mayer path Laplacians for filtered directed graphs, extending path homology built on a nilpotent boundary map with N-th roots of unity, with stability results and an application to cucurbit[7]uril molecular contacts.
- **In plain words**: The paper studies shape-like invariants of networks where connections have a direction, such as one-way links between points. It builds a new version of these invariants, called Mayer path homology, that tracks how structures appear and disappear as a distance threshold grows. The authors report that it can detect feed-forward loops, which the older standard method misses, and in a molecule example it changes at more filtration values than the older method.
- **Why it matters**: Tracking directed structures across scales could help analyze networks where direction matters, such as chemical contact graphs or signalling networks. The text shows the method is applied to one molecule, so its wider usefulness is not established here.
- **Background needed**: - Directed graph: a network whose edges have a one-way direction.
- Homology: a counting method from topology that records loops and holes in a space; Betti numbers are the counts.
- Boundary operator: a rule that maps a structure to its outline; in ordinary homology applying it twice gives zero, and Mayer homology relaxes this to applying it N times gives zero.
- Persistent homology: tracking these counts as a distance threshold (filtration) grows, producing barcodes that show when features are born and die.
- Laplacian (combinatorial): a matrix whose kernel and eigenvalues encode the same homology information in spectral form.
- Feed-forward loop: a three-node directed motif where one node points to a second, which points to a third, and the first also points to the third.
- Filtration by van der Waals radii: distances between atoms scaled by their typical contact size, used to decide when atoms count as connected. · level: research-level

<details><summary>Original abstract</summary>

In topological data analysis, path homology accounts for directed graph while combinatorial Laplacian extends homology groups to spectral theory. However, these approaches are built on a boundary operator with condition $\partial^2=0$. Mayer homology replaces this condition with $N$-nilpotent boundary map $\partial^N=0$. By using the primitive $N$-th root of unity in the boundary operator, it relates each degree $n$ to the degrees $n-q$ and $n+N-q$. This work introduces persistent Mayer path homology. We show that Mayer path homology is functorial for strict digraph maps, which gives persistent Mayer path homology for filtered digraphs, and prove that its barcodes are stable under perturbations. For $N=3$ we derive formulas that reduce $\beta_0^{3,1}$ and $\beta_2^{3,2}$ to the classes of vertices identified by squares and the rank of a small matrix indexed by triangles. We also introduce the Mayer path Laplacian and its persistence theory, prove that their kernels recover (persistent) Mayer path homology, show that they distinguish digraphs with the same Mayer path Betti numbers, and prove a stability bound for the eigenvalues of the persistent up-Laplacian. We demonstrate that persistent Mayer path homology detects the formation of feed-forward loops, whose formation is not detected by ordinary path homology. In an application to cucurbit[7]uril, filtered by an interatomic distance normalized by van der Waals radii, Mayer path homology separates contacts that only close cycles from contacts that close feed-forward triangles, and changes at almost four times as many filtration values as path homology after the bonded framework is formed.

</details>

### [A simple approach to ends of manifolds and the Freudenthal compactification](https://arxiv.org/abs/2611.26989)
*Rodrigo Hern\'andez-Guti\'errez, Carlos Rios-Mendoza* · `math.GN` · arXiv:2611.26989v1 · relevance 0.12

- **In one sentence**: The paper gives a new, more streamlined definition of the Freudenthal end-compactification of non-compact manifolds, via filters of open sets with compact boundary that have a base of connected subsets, and shows it agrees with the older constructions.
- **In plain words**: The paper is about how a non-compact shape (a manifold, such as an infinitely long surface) can be closed up by adding points that describe the different ways it "goes off to infinity." The author proposes a simpler way to define these added points, using collections of open regions with compact boundaries, and checks that this gives the same result as the standard construction. The text also gives an example of a non-metrizable manifold, and uses the new definitions to prove a known metrization theorem and to give an alternative proof of a known characterization.
- **Why it matters**: The Freudenthal compactification is a standard tool in topology, so a cleaner definition that is proven equivalent to the usual ones can make it easier to teach and apply. The text does not indicate further connections beyond the metrization and characterization results it mentions.
- **Background needed**: - Manifold: a space that locally looks like ordinary Euclidean space, such as a surface.
- Compact set: a set that is closed and bounded in a strong sense; in everyday terms, it does not leak off to infinity.
- Compactification: adding points to a space so that it becomes compact, in a controlled way.
- Ends of a space: the different ways of escaping to infinity; the Freudenthal compactification adds one point per end.
- Filter: a family of sets that is closed under taking supersets and finite intersections, used here to pick out "directions toward infinity."
- Metrizable: a space whose topology can be described by a distance function. · level: research-level

<details><summary>Original abstract</summary>

In this note we give an alternative definition of the Freudenthal end-compactification of a non-compact manifold by defining ends to be the filters of open subsets with compact boundaries that have a base of connected subsets. We start by defining these notions and proving that the resulting compactification is equivalent to the Freudenthal compactification. In particular, we explicitly discuss the equivalence between our definitions and those from two different approaches: maximal binding families and inverse limits. After that, we give an example of a non-metrizable manifold, showing how these new definitions make it easier to identify ends and understand the topology of the end-compactification. We also prove a well-known metrization theorem, showing an application of our definition. Finally, we also give an alternative proof of the topological characterization of the Freudenthal compactification.

</details>

## Dynamical systems

### [Recurrent sets and Lyapunov functions: from topological dynamics to weak KAM theory](https://arxiv.org/abs/2611.27887)
*Olga Bernardi, Mattia Sensi, Jim Wiseman* · `math.DS` · arXiv:2611.27887v1 · relevance 0.18

- **In one sentence**: A survey linking Lyapunov functions and Conley's chain recurrent sets in topological dynamics, including recent weak KAM results for homeomorphisms, connections to the stationary Hamilton-Jacobi equation, and examples from epidemiology and predator-prey dynamics.
- **In plain words**: This survey looks at how to describe where a system that changes over time can keep returning near its starting points, and how "energy-like" measuring functions (Lyapunov functions) can reveal that structure. It reviews existing results, including newer ones from a field called weak KAM theory, and links them to a classical equation from physics and mathematics. To show how these sets change with a parameter, it works through a disease compartment model and a predator-prey model with an Allee effect (where small populations struggle to grow).
- **Why it matters**: The text presents this as a review of the current state of the field rather than a single new finding, so its value lies mainly in organizing known results. It may matter to researchers connecting stability analysis of dynamical systems with Hamilton-Jacobi equations, though the text does not spell out specific applications beyond the two examples.
- **Background needed**: - Dynamical system: a rule that describes how a state evolves over time.
- Recurrent set: a region a system keeps coming back to, at least approximately, after leaving it.
- Chain recurrence (Conley): a way to track returns using short jumps that allow small errors.
- Lyapunov function: a measuring function that decreases along trajectories, like an energy that settles, used to prove stability.
- Homeomorphism: a continuous, reversible change of a space, used as the discrete-time analogue of a flow.
- Hamilton-Jacobi equation: a partial differential equation from mechanics and optimal control; its stationary form is time-independent.
- Weak KAM theory: a generalized framework from Hamiltonian mechanics relating dynamics to solutions of this equation.
- Compartmental model: an epidemiology model that splits a population into groups such as susceptible and infected.
- Allee effect: a condition where populations grow poorly when they are very small. · level: research-level

<details><summary>Original abstract</summary>

The aim of this survey is to clarify the intimate relations between Lyapunov functions and chain recurrent sets. The study of this subject comes from a seminal paper by Conley and has had recent advances by the so-called Weak KAM Theory for homeomorphisms. We provide a survey of the state of the art, presenting recent improvements and connections with the stationary Hamilton-Jacobi equation. Finally, in order to illustrate the distinctions between recurrent sets in a non-trivial case as well as their dependence on a parameter, we discuss a compartmental model from mathematical epidemiology and a fast-slow version of a prey-predator model with Allee effect.

</details>

### [Non-local ergodic measures in symplectic dynamics](https://arxiv.org/abs/2611.27429)
*Jaime Paradela* · `math.DS` · arXiv:2611.27429v1 · relevance 0.15

- **In one sentence**: For a product of two symplectomorphisms (one with a basic set, the other with a non-degenerate elliptic equilibrium on a compact surface), the paper shows that under a local domination condition a typical real-analytic perturbation yields a large normally hyperbolic lamination on which the natural invariant measure is ergodic.
- **In plain words**: This paper studies a mathematical model of a system that moves in a way that preserves a kind of "volume" from classical mechanics. The authors build a combined system from two simpler pieces and show that, after a small generic nudge to the rules, the system has a large structured set on which its typical behavior mixes thoroughly, so a long-run average over the set matches the average over the whole set. The text does not give the full statements, so details of the mixing claim are limited to the abstract.
- **Why it matters**: Ergodicity, the property that a system's time averages match its space averages, is a central question in dynamics, and this work addresses it for systems that are not uniformly hyperbolic, where such results are harder. The abstract says the technique, which combines KAM theory with geometric measure theory and introduces a new geometric source of "semi-local" ergodicity, may apply to more general settings, but how far it extends is not stated here.
- **Background needed**: - Symplectomorphism: a transformation that preserves the area/volume structure of phase space, the basic symmetry of Hamiltonian mechanics.
- Ergodic measure: a natural invariant measure under which almost every trajectory explores the set evenly over time.
- Basic set: a compact invariant set with chaotic, hyperbolic dynamics, a building block in the theory of dynamical systems.
- Elliptic equilibrium: a fixed point around which nearby orbits circle rather than run away or collapse.
- Normally hyperbolic lamination: a layered family of invariant sets where motion transverse to the layers grows or shrinks at a controlled rate.
- KAM theory: the body of results showing that many quasi-periodic motions survive small perturbations of a Hamiltonian system.
- Real-analytic perturbation: a small change to the system's rules that is smooth in a strong, power-series sense. · level: research-level

<details><summary>Original abstract</summary>

We consider the direct product of two symplectomorphisms, one of which exhibits a basic set and the other one acts on a compact surface and has a non-degenerate elliptic equilibrium. Under a local domination condition we show that a typical real-analytic perturbation of this system displays a large normally hyperbolic lamination on which the natural invariant measure is ergodic. The proof, which introduces a novel geometric source of semi-local ergodicity, combines tools ranging from KAM theory to geometric measure theory and is robust enough to be of interest in more general configurations.

</details>

## Combinatorics

### [Small spherical 7-designs in prime dimensions](https://arxiv.org/abs/2611.26879)
*Andriy Bondarenko, Dmytro Mitin* · `math.CO` · arXiv:2611.26879v1 · relevance 0.14

- **In one sentence**: The paper constructs antipodal spherical 7-designs on the unit sphere S^{p-1} for every prime p ≥ 29, using at most 42(p-1)(p+2)^2 points, via eigenlines of finite Weil operators.
- **In plain words**: The paper is about placing a finite set of points evenly over the surface of a high-dimensional sphere so that they average out the way a truly uniform spread would, at least for polynomial functions up to degree 7. The author builds such point sets for every prime dimension p at least 29, with a stated point count of 42(p-1)(p+2)^2. The construction draws on a mathematical tool called Weil operators, which are used to find special directions (eigenlines) that supply the points.
- **Why it matters**: Small, explicit designs of this kind matter for numerical integration, coding and quantum state sampling, where fewer well-spread points save work. The text does not state which applications, if any, this result affects, so its wider relevance is uncertain from the abstract alone.
- **Background needed**: - Sphere S^{p-1}: the surface of a ball in p-dimensional space.
- Spherical t-design: a finite point set whose average of any polynomial of degree at most t equals the average over the whole sphere; here t = 7.
- Antipodal: the point set is symmetric, so for every point x its opposite -x is also included.
- Prime dimension p: the construction works only when the dimension is prime and at least 29.
- Weil operator / eigenline: a finite-field object from number theory whose special eigen-directions give the point set; the abstract does not explain the details.
- Point count: the bound 42(p-1)(p+2)^2 is an upper bound on how many points are used. · level: research-level

<details><summary>Original abstract</summary>

For every prime $p\ge 29$, we construct an antipodal spherical $7$-design on $S^{p-1}$ with $42(p-1)(p+2)^2$ points. The construction uses eigenlines of finite Weil operators.

</details>

### [Extremal problems for graphs with bounded $k$-th binding number](https://arxiv.org/abs/2611.27699)
*Ao Fan, Ruifang Liu* · `math.CO` · arXiv:2611.27699v1 · relevance 0.12

- **In one sentence**: The paper determines the maximum number of edges and the maximum spectral radius over n-vertex graphs with k-th binding number below r, and characterizes the extremal graphs, generalizing known k=1 results.
- **In plain words**: This paper is about graphs, which are networks of points joined by lines, and a score called the k-th binding number that measures how well every group of vertices is connected to the rest. The authors ask: if a graph's score is kept below a fixed value r, how many connections can it have at most, and what does the densest such graph look like? They answer this for both the number of edges and a matrix-based measure called the spectral radius, and identify the graphs that reach the maximum.
- **Why it matters**: Extremal questions like this show how a structural condition limits how dense a network can be, which is the core of Turán-type graph theory. The authors say the proof method, which links neighborhood inequalities to the complement of the graph, may carry over to other Turán-type problems, but the text does not show how far that reaches.
- **Background needed**: - Graph: vertices (points) joined by edges (lines); order n means number of vertices, size means number of edges.
- Perfect matching / k-factor: a way to pair up all vertices (or cover them by k-regular spanning subgraphs) using edges.
- Binding number: a graph parameter (Woodall, 1973) measuring how much the neighborhoods of vertex sets expand; Anderson (1971) showed binding number at least 4/3 forces a perfect matching.
- k-th binding number: a higher-order version introduced by Chen et al.; the text notes that score at least 1 guarantees a k-factor when kn is even.
- Extremal problem (Turán-type): find the largest graph (by edges or spectral radius) that avoids a given property.
- Spectral radius: the largest eigenvalue of the graph's adjacency matrix, a single number summarizing its structure.
- Complement graph: the graph on the same vertices with exactly the missing edges. · level: research-level

<details><summary>Original abstract</summary>

The binding number of a graph, introduced by Woodall [J. Combin. Theory, Ser. B, 1973], is a central topic in structural and extremal graph theory. Recently, Chen et al. introduced the $k$-th binding number $\beta^k(G)$. Anderson [J. Combin. Theory, Ser. B, 1971] proved that every graph $G$ of even order with $\beta^1(G)\ge\frac43$ contains a perfect matching, and that the bound $\frac43$ is best possible. For $k\ge2$, Chen et al. proved that $\beta^k(G)\ge1$ guarantees a $k$-factor whenever $kn$ is even, and that the bound $1$ is best possible. The above facts reveal a fundamental distinction between the higher-order binding number and the classical binding number. This distinction makes extremal problems for graphs with bounded $k$-th binding number particularly intriguing. For positive integers $n,$ $k$ and $r$, we in this paper determine the maximum size and spectral radius among all graphs $G$ of order $n$ satisfying $\beta^k(G)<r$, and characterize the corresponding extremal graphs, respectively. In particular, when $k=1$, our results imply the corresponding extremal results of Fan and Lin [Electron. J. Combin., 2024] and Liu, Chen and Fan [Electron. J. Combin., 2026]. Our proofs develop a structural framework that relates higher-order neighborhood inequalities to the structure of the complements of graphs. This framework may provide an approach to Tur\'{a}n-type problem involving the $k$-th binding number, and the approach may be of independent interest.

</details>

## Numerical analysis

### [Convergence of a finite element Chorin projection method for the stochastic Navier--Stokes equations](https://arxiv.org/abs/2611.27969)
*Franziska Weber* · `math.NA` · arXiv:2611.27969v1 · relevance 0.16

- **In one sentence**: Proves that a fully discrete finite element Chorin projection scheme for the stochastic incompressible Navier--Stokes equations with multiplicative noise and Dirichlet boundary conditions converges (along a subsequence) to a martingale solution in two and three dimensions, under a coupling of space and time step sizes.
- **In plain words**: This paper studies a computer method for simulating fluid flow (like water or air) that is randomly disturbed by noise, where the fluid is kept incompressible and sits inside a container with fixed walls. The authors show that their step-by-step numerical scheme stays well-behaved and, as the grid gets finer, its results settle toward a valid random-solution of the underlying equations. They also test the method numerically in two dimensions on smooth and vortex-sheet starting conditions.
- **Why it matters**: Random fluid models are used when uncertainty or noise matters, so a convergence proof gives some confidence that the computed results mean something. The text does not say how the method compares with other schemes or what applications it targets, so its wider impact is uncertain.
- **Background needed**: - Navier--Stokes equations: the standard equations describing how viscous fluids move.
- Incompressible: the fluid's density stays constant, so its velocity must be divergence free (no net sources or sinks).
- Stochastic / multiplicative noise: random forcing whose strength depends on the current state of the flow.
- Finite element method: splitting a domain into small pieces and approximating the solution with simple functions on them.
- Chorin projection method: a two-step time-stepping trick that first moves the flow forward, then corrects it to restore incompressibility.
- Martingale solution: a weak notion of a random solution, defined on a possibly different probability space, which need not be unique.
- Moment estimates and tightness: bounds on average sizes of the random quantities and a way to guarantee that a sequence of random paths has convergent subsequences.
- Aldous' criterion: a standard test for tightness of random processes.
- Vortex sheet: an idealized flow with a concentrated jump in velocity across a curve, a hard test case. · level: research-level

<details><summary>Original abstract</summary>

We analyze a fully discrete finite element projection method for the stochastic incompressible Navier--Stokes equations with homogeneous Dirichlet boundary conditions and multiplicative noise. We show solvability and uniform moment estimates for the intermediate and the corrected velocity approximations under the assumption that the initial data is square-integrable and divergence free, and that the deterministic forcing term is bounded in $L^{q}(0,T;H^{-1}(D))$ for a sufficiently large $q$. Under standard stability and approximation assumptions on the finite element spaces and a coupling condition on the spatial and temporal discretization parameters, we prove convergence of a subsequence to a martingale solution of the stochastic Navier--Stokes equations. The analysis combines the complementary spatial and temporal estimates of the predicted and the corrected velocity approximations and uses the numerical dissipation to identify their common limit. We establish tightness of the piecewise constant temporal interpolations of the velocity field approximations using Aldous' criterion combined with the uniform discrete moment estimates. The convergence result holds in two and three space dimensions as it does not rely on any additional regularity of the limiting martingale solution beyond the one naturally available from the energy inequality. Finally, we demonstrate the performance of the scheme in numerical experiments in two space dimensions for smooth and vortex sheet initial data.

</details>

### [A Validation-Driven Bilevel Optimization Method for Mesh-Free PDE Solvers and Its Error Analysis](https://arxiv.org/abs/2611.27347)
*Yongcun Song, Shangzhi Zeng, Jin Zhang et al.* · `math.OC` · arXiv:2611.27347v1 · relevance 0.14

- **In one sentence**: The paper proposes a validation-driven bilevel optimization framework for tuning design parameters of mesh-free PDE solvers (Kansa, random feature/extreme learning machine, and physics-informed neural network methods), using an efficient implicit hypergradient with warm-started damped Gauss-Newton and preconditioned minimum-residual adjoint solves, and derives local error bounds linking validation residuals to solution accuracy.
- **In plain words**: Mesh-free methods solve equations like heat or fluid flow by checking the equation at scattered sample points instead of on a grid. These methods have settings, such as network shape or regularization strength, that strongly affect accuracy and are hard to choose. The authors choose these settings by fitting the solution on training points and scoring it on separate held-out validation points, and they make the search for good settings computationally cheaper for nonlinear equations.
- **Why it matters**: Choosing solver settings is a practical bottleneck for these methods, and a single selection framework that works across several solver families could be useful. The text reports numerical experiments, including a high-dimensional nonlinear problem, but I cannot judge from the abstract alone how large the practical gains are.
- **Background needed**: - PDE (partial differential equation): an equation relating a function to its rates of change, used to model physical processes such as heat or waves.
- Mesh-free solver: a numerical method that works from scattered points rather than a fixed grid of cells.
- Residual: how far a candidate solution misses satisfying the equation at chosen points.
- Bilevel optimization: an outer problem (choose settings) wrapped around an inner problem (fit the solution to the settings).
- Validation set: held-out points used to score choices without fitting to them.
- Hypergradient: the gradient of the outer score with respect to the settings, which lets the outer choice be improved by gradient steps.
- Gauss-Newton method: an iterative method for nonlinear least-squares fitting; "damped" means step sizes are tempered for stability.
- Adjoint system: an auxiliary linear system used to compute hypergradients efficiently.
- Preconditioning: transforming a linear system so an iterative solver converges faster.
- Physics-informed neural network (PINN): a neural network trained to satisfy a PDE and its boundary conditions. · level: research-level

<details><summary>Original abstract</summary>

Mesh-free partial differential equation (PDE) solvers construct discrete systems from residuals at sampled points. These solvers fit coefficients in a parameterized trial representation and select solver-design parameters governing the representation, training-residual weighting, and regularization. These parameters strongly affect solution accuracy, yet existing selection strategies are largely tailored to particular solver classes. To address this limitation, we formulate a unified validation-driven bilevel optimization framework applicable across different solver classes, in which the lower level fits coefficients using training collocation residuals, while the upper level selects solver-design parameters using held-out validation residuals. For nonlinear PDEs, however, solving the nonlinear lower-level problem to high accuracy is costly, while the adjoint system is typically ill-conditioned and indefinite. To address this issue, we propose an efficient implicit hypergradient method that approximates the lower-level response using finite, warm-started damped Gauss-Newton (GN) updates. For the adjoint solve, we use the damped GN matrix to compute an initial adjoint and to precondition a finite number of minimum residual iterations. To quantify the errors introduced by these approximations, we derive local hypergradient error bounds that separate the contributions of the finite lower-level solve, adjoint damping, and the final adjoint residual. Combining this analysis with validation sampling bounds and residual stability, we relate validation residuals to PDE solution accuracy and establish error bounds for the computed PDE solution. Numerical experiments on several nonlinear PDEs, including a high-dimensional problem, demonstrate the accuracy and efficiency of the proposed method across Kansa, random feature and extreme learning machine, and physics-informed neural network solvers.

</details>

## Logic and foundations

### [Bridging Badiou's Gaps: Topos Theory and the Bodies of Mathematical Expression](https://arxiv.org/abs/2611.27280)
*Antti Veilahti* · `math.CT` · arXiv:2611.27280v1 · relevance 0.11

- **In one sentence**: A philosophical reconstruction of Alain Badiou's use of topos theory (forcing, Kripke-Joyal semantics, and his typology of change) recast in a categorical framework, arguing that a topos can be read as a "body of mathematical expression."
- **In plain words**: The paper revisits how the philosopher Alain Badiou used a branch of advanced mathematics, topos theory, in his books Being and Event and Logics of Worlds. The author argues that Badiou shrank this mathematics down to a narrow, set-based version, and asks what is lost when it is restored to its fuller categorical form. The author says the aim is conceptual clarification rather than new mathematical results.
- **Why it matters**: It connects philosophy of mathematics, the foundations of logic, and the reception of category theory in continental philosophy, and it is a second part of an argument begun in 2013. The text itself does not show how much influence the argument has, so its wider significance is uncertain.
- **Background needed**: - Badiou: a French philosopher whose works Being and Event and Logics of Worlds use set theory and topos theory to describe truth, events and change.
- Topos (plural topoi): a mathematical structure from category theory that generalises set theory and can serve as a setting for logic.
- Category theory: a framework that studies mathematical objects through the relationships (maps) between them rather than their internal contents.
- Forcing: Paul Cohen's technique for building new models of set theory, used to show certain statements cannot be proved or disproved from the standard axioms.
- Kripke-Joyal semantics: a way of giving meaning to logical statements inside a topos.
- Localic: a more restricted, point-based form of topos, which the author argues Badiou relied on.
- Grothendieck topos: a general notion of topos introduced in algebraic geometry.
- Johnstone's "universe of discourse": a description of a topos as a setting in which mathematical reasoning takes place. · level: research-level

<details><summary>Original abstract</summary>

This article develops a second stage of an argument begun in 2013, revisiting Alain Badiou's use of topos theory in Being and Event and Logics of Worlds. The previous article diagnosed Badiou's reduction of topos theory to its atomistic, localic form as the scientific scapegoat in his attack on 'democratic materialism'. Now I ask what follows when this logicist illusion is dispelled and the categorical alternative is taken seriously, particularly with respect to forcing, semantic expression, and mathematical subjectification that constitute the key elements of Badiou's earlier work. I thus reconstruct Badiou's own arguments in a corrected form, while transferring them to a categorical framework. The aim is not to introduce new mathematical results, but to identify what is conceptually lost through their reduction to set-theoretic formalism. In particular, I describe Cohen's forcing argument in the context of Grothendieck topoi and Kripke-Joyal semantics, thereby explicating the geometric structures implicit in Badiou's thinking. This reconstruction further brings into view a different way of understanding Badiou's concepts of subject, body, and change. Rather than treating a topos as merely a formal container for mathematical objects, I propose reading it as a body of mathematical expression, aligning with Johnstone's characterization of a topos as a 'universe of discourse'. At the same time, the geometrization of logic allows Badiou's own four-fold typology of change - when applied to topos theory itself as a mathematical 'event' - to be anchored to various historical definitions of a topos. In this way, the article bridges Badiou's two major works while clarifying how his own limited expression of mathematical formalism embodies his 'dialectical', ultimately singular concept of the event, and the way it clouds his philosophical understanding of locality and temporality.

</details>

### [The Power Of Enumerations](https://arxiv.org/abs/2611.27239)
*Karthik Ravishankar* · `math.LO` · arXiv:2611.27239v1 · relevance 0.08

- **In one sentence**: The paper studies the computational strength of enumeration reducibility for generic and random sets, showing limits on what enumerations of 3-generics and weak 2-randoms can compute and mapping which Turing degrees can lie above quasiminimal enumeration degrees.
- **In plain words**: The paper is about how much information can be extracted from "typical" infinite sets of binary digits, using a way of computing called enumeration, which asks whether a set can be listed out from another set rather than decided item by item. The authors show that some such listing-based constructions cannot recover typical sets at higher levels of typicality. They also answer an open question of Slaman and Sorbi by showing that some quasiminimal degrees have no minimal Turing degrees above them.</plain>
<parameter name="why">It sharpens the picture of how randomness and genericity behave under computability reductions, a central topic in the study of what can be computed from what. The text itself does not say how these results bear on wider applications, so their broader significance is unclear from this text alone.
- **Background needed**: - Computability theory asks which infinite sets of numbers can be computed from which others.
- Turing degree: a class of sets that are equally hard to compute from one another, under ordinary Turing computation.
- Enumeration degree: a coarser-to-finer notion where a set is computed by listing its members (positive information only), not by deciding membership.
- Generic and random sets: "typical" infinite sets that avoid all definable special properties (genericity) or are incompressible/unpredictable (randomness). Levels (2-generic, 3-generic, 1-random, weak 2-random) measure how strongly typical.
- Quasiminimal: an enumeration degree with no non-computable (total) degrees strictly below it, apart from trivial ones.
- PA degrees: degrees that compute a solution to a certain combinatorial principle (Peano arithmetic-related), and dimension 1 sets are a measure of how much of the set's information is free. · level: research-level

<details><summary>Original abstract</summary>

We study the computational strength of enumerations of generic and random sets, particularly its interplay with computing these `typical' sets. We show that, while enumerations of $2$-generics can compute $2$-generics, this fails at higher levels---every $3$-generic has an enumeration which computes no weak $3$-generic. The analogous statement holds for randoms---every weak $2$-random has an enumeration which computes no $1$-random. We then analyze the total degrees above a quasiminimal enumeration degree, showing certain restrictions as well as certain positive results on the possible Turing degrees in such a cone. This answers a question of Slaman and Sorbi, by showing that there are quasiminimals with no minimal Turing degrees above them. We also show that while every total degree above some quasiminimals compute dimension $1$ sets, the total degrees above any quasiminimal fail to be a subset of the PA degrees.

</details>

## Mathematical physics

### [Brane Tilings and Polygons with Two Interior Points](https://arxiv.org/abs/2611.27861)
*Rak-Kyeong Seong* · `hep-th` · arXiv:2611.27861v1 · relevance 0.11

- **In one sentence**: A complete classification of brane tilings and their associated 4d N=1 quiver gauge theories for toric Calabi-Yau 3-folds whose toric diagrams are convex lattice polygons with exactly two interior lattice points (45 polygons, 323 toric phases), including Hilbert series and mesonic moduli space data.
- **In plain words**: This paper is a catalogue in theoretical physics and geometry. It looks at a family of shapes that encode certain higher-dimensional geometric spaces, and at the physics theories (built from particles and their interactions) linked to each one. The authors list every such shape with two interior points, find all 323 physical versions of them, and record the matching diagrams and mathematical data for each.
- **Why it matters**: The text presents this as a complete classification, which makes it a useful reference for anyone studying the link between string-theory gauge theories and the geometry of Calabi-Yau spaces. The text does not say what broader consequences follow, so its wider importance is unclear from this text alone.
- **Background needed**: - Toric diagram: a small lattice polygon (points on a grid) that encodes a toric Calabi-Yau 3-fold, a special higher-dimensional geometric space used in string theory.
- Interior lattice point: a grid point strictly inside the polygon; here, polygons with exactly two.
- Brane tiling (dimer model): a tiling of a torus by polygons that encodes a gauge theory's particles and interactions.
- Quiver gauge theory: a diagram of nodes (gauge groups) and arrows (matter fields) describing a 4d supersymmetric theory.
- Superpotential: a polynomial describing the interactions among the fields.
- Toric phase: one of the distinct gauge theories that share the same underlying geometry.
- Moduli space, Hilbert series, plethystic logarithm: tools for counting the gauge-invariant quantities and their relations in a theory.
- U(1)R charge: a symmetry charge used to fix the theory's superconformal behaviour. · level: research-level

<details><summary>Original abstract</summary>

We fully classify the brane tilings and the 4d N=1 supersymmetric quiver gauge theories corresponding to toric Calabi-Yau 3-folds whose toric diagrams are convex lattice polygons with two interior lattice points. There are 45 such polygons up to GL(2,Z) transformations and lattice translations: 5 triangles, 19 quadrilaterals, 16 pentagons and 5 hexagons. We identify all 323 toric phases corresponding to these toric Calabi-Yau 3-folds. For every toric phase, we present the brane tiling with its quiver and superpotential, the perfect matching matrix and the F- and D-term charge matrices. For each brane tiling, we study the mesonic moduli space of the corresponding abelian 4d N=1 theory through its Hilbert series and plethystic logarithm, and identify its generators and their leading relations. We also identify the mesonic global symmetry for each brane tiling and determine the superconformal U(1)R charges.

</details>

### [The moments and asymptotic spectral distribution of the Grassmannian ensemble](https://arxiv.org/abs/2611.27914)
*Aryan Gadhave, Asghar Ghorbanpour, Liam Hickey et al.* · `quant-ph` · arXiv:2611.27914v1 · relevance 0.07

- **In one sentence**: The paper computes all tracial moments and mixed reduced-state moments of random density matrices obtained by partial traces of projections onto random subspaces drawn from the Grassmannian, using Weingarten calculus, and derives almost-sure convergence of the spectrum to a rescaled Marchenko-Pastur law, an asymptotic freeness decomposition, and the asymptotic average entanglement entropy.
- **In plain words**: The paper studies a model of a "typical" quantum state: pick a random subspace of a two-part quantum system, then look at the state of just one part by averaging out the other. The authors work out the statistical averages of the eigenvalue pattern of these random density matrices exactly, using a counting technique called Weingarten calculus. From these results they show that the pattern of eigenvalues settles into a known shape (a rescaled Marchenko-Pastur law) as the system grows, and they estimate the average entanglement entropy.
- **Why it matters**: Random density matrices like these are used as benchmarks for what generic quantum states look like, which matters for quantum information and statistical physics. The text offers two routes to the same spectral result, one of which goes through asymptotic freeness, a link to random matrix theory; the broader impact beyond this setting is not addressed in the text.
- **Background needed**: - Density matrix: a matrix describing a quantum state; its eigenvalues are nonnegative and sum to one.
- Partial trace: averaging out one subsystem to get the state of the other.
- Grassmannian: the space of all subspaces of a fixed dimension, here sampled uniformly via the unitary group.
- Tracial moments: averages of powers of the matrix's trace, which encode the eigenvalue distribution.
- Weingarten calculus: a systematic method for integrating polynomial functions of random unitary matrices.
- Marchenko-Pastur law: the limiting eigenvalue distribution of certain large random matrices.
- Asymptotic freeness: a notion from free probability describing when large random matrices behave independently in a specific algebraic sense.
- Entanglement entropy: a measure of how correlated the two subsystems are, computed from the reduced density matrix. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study random density matrices constructed by taking partial traces of projections onto random subspaces of a bipartite Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_{B}$ distributed according to the pushforward measure of the action of the unitary group on the Grassmannian $\text{Gr}_{n}(\mathcal{H}_A \otimes \mathcal{H}_{B})$. This ensemble models a `typical' quantum subspace. All tracial moments of the density operator, as well as mixed tracial moments of reduced density operators, are computed explicitly using Weingarten calculus. There are several consequences of these results. In particular, we prove that the empirical spectral distribution of the density operator converges almost surely to a rescaled Marchenko-Pastur law. We also prove that this ensemble can be written as a sum of asymptotically free random density operators, leading to an alternative proof of the convergence of the spectral distribution. Finally, we compute the asymptotic expansion of the average entanglement entropy.

</details>

## Optimization and control

### [Small noise limit for Entropic Variational Mean-Field Games](https://arxiv.org/abs/2611.27695)
*Alessandro Cosenza, Luca Nenna* · `math.AP` · arXiv:2611.27695v1 · relevance 0.25

- **In one sentence**: The paper proves that, as the random noise in second-order variational mean-field games shrinks to zero, the entropy-minimizing Lagrangian formulation Γ-converges to its deterministic first-order counterpart, and it derives a first-order energy expansion for the original Eulerian problem that selects among deterministic minimizers.
- **In plain words**: The paper studies large systems of many interacting agents that move under random noise and each try to optimize their own cost. It asks what happens when the noise is made very small, so the system approaches a deterministic model. The authors show that the noisy problem converges, in a precise variational sense, to the deterministic one, and that the noisy version also recovers a known result linking random transport (the Schrödinger problem) to optimal transport.
- **Why it matters**: The text indicates the work connects a noisy game-theoretic model with its noiseless limit and gives a new dynamical route to the Schrödinger-to-optimal-transport convergence. It also says a small-noise expansion selects particular minimizers of the deterministic problem; the broader significance beyond these claims is not stated in the text.
- **Background needed**: - Mean-field game: a model of a very large population of agents, each optimizing a cost that depends on the population's overall distribution.
- Second-order vs first-order: second-order models include random noise (diffusion); first-order models are deterministic.
- Entropy: a measure of spread or randomness; entropy minimization here penalizes deviation from a reference random motion.
- Schrödinger problem: a noisy, entropy-regularized version of optimal transport (finding the cheapest way to move one distribution of mass to another).
- Optimal transport: the least-cost way to rearrange one distribution into another.
- Γ-convergence: a notion of convergence for minimization problems, ensuring minimizers of approximating problems approach minimizers of the limit problem.
- Eulerian vs Lagrangian: Eulerian tracks a density and velocity field at fixed points in space; Lagrangian tracks individual particle paths. · level: research-level

<details><summary>Original abstract</summary>

We study second order variational mean-field games with quadratic Hamiltonian. In analogy with entropic optimal transport, Benamou, Carlier, Di Marino and the second author recently proposed an entropy-minimization formulation of the problem, which could be interpreted as the Lagrangian counterpart of the classical Eulerian approach. We investigate the small-noise $\Gamma$-limit for the Lagrangian entropy-minimization formulation and establish $\Gamma$-convergence of second order mean-field games towards their deterministic first order counterpart. This also translates into another (dynamical) proof of the convergence of the Schr\"odinger problem to optimal transport. Moreover, we study the original Eulerian problem and prove a first order energy expansion, which establishes a selection principle for minimizers of the deterministic problem.

</details>

### [Approximating technique for the solution to the ${H}^{\infty}$ -optimal control problem](https://arxiv.org/abs/2611.27520)
*Gabriela Marinoschi* · `math.AP` · arXiv:2611.27520v1 · relevance 0.23

- **In one sentence**: The paper proposes an approximation scheme that builds a sequence of infinite-dimensional systems to compute solutions of the H-infinity optimal control problem and its associated Riccati equation, and proves convergence of the approximate solutions to the original one.
- **In plain words**: The paper is about designing a feedback controller that keeps a system stable even when it is affected by unknown disturbances or modelling errors. Since the exact solution is hard to compute directly, the author builds a series of simpler approximating problems and shows that their solutions approach the true one. A worked example at the end shows how the method computes the controller and the related Riccati equation.
- **Why it matters**: Robust control of this kind is used in engineering settings where guarantees against disturbances matter, and a provable approximation method makes such designs more practical to compute. The text does not indicate specific applications or how the method performs beyond the single example, so its practical reach is uncertain. It continues earlier work by the same author cited in the text.
- **Background needed**: - Optimal control: choosing inputs over time to make a system behave well at minimal cost.
- Robust stabilization: designing a controller that keeps a system stable despite uncertainty or disturbances.
- H-infinity norm: a measure of how strongly disturbances can affect a system's output in the worst case.
- Riccati equation: a nonlinear matrix equation whose solution gives the optimal feedback gain in many control problems.
- Infinite-dimensional systems: models where the state is a function (e.g., of space), not a finite list of numbers, so they are approximated by finite or simpler systems.
- Convergence: the approximate solutions get closer to the true solution as the approximation is refined. · level: research-level

<details><summary>Original abstract</summary>

This paper continues the results published in [G. Marinoschi, Appl. Math. Optimiz. 94:44, 1-29, 2026], by presenting an approximating method of calculating the solution to the $H^{\infty }$-optimal control problem, which solves the robust stabilization of a system by a feedback controller, and to the associated Riccati equation. This method generates a sequence of infinite dimensional systems approximating the original system and the solution to the approximating $H^{\infty }$-optimal control problem is proved to converge to the solution of the original $H^{\infty }$-optimal control problem. An example for calculating the solution to the Riccati equation and the feedback controller is provided at the end.

</details>

## Statistics theory

### [Pathwise Factorization and Uncertainty Quantification for Impedance Obstacles with Random Boundaries](https://arxiv.org/abs/2611.26761)
*George Pelekanos, Koung Hee Leem* · `math.NA` · arXiv:2611.26761v1 · relevance 0.09

- **In one sentence**: A factorization method for locating two-dimensional impedance obstacles with random boundaries from finitely many noisy multistatic measurements, with finite-sample confidence guarantees, simultaneous confidence bands, and a combined-field integral equation computed numerically.
- **In plain words**: The paper looks at how to find an object that sound waves bounce off when the object's edge is not fixed but varies randomly from one trial to the next. Using a limited set of noisy measurements, the authors build an imaging method and attach statistical error bounds to it, so the picture of where the object is comes with stated uncertainty. They check the resulting coverage of those error bounds against a high-accuracy Monte Carlo reference.
- **Why it matters**: Imaging hidden objects from scattered waves is used in radar, sonar, and medical or geophysical imaging, and attaching confidence statements to the image is the kind of step those fields need. The text does not discuss applications, so any connection beyond this specialist setting is my inference rather than something the paper states.
- **Background needed**: - Acoustic scattering: waves sent at an object and the echoes or far-field patterns recorded.
- Impedance obstacle: an object whose surface partly absorbs or reflects waves, described by a boundary condition.
- Factorization method: an inverse-scattering technique that tests sampling points to decide whether they lie inside the object.
- Multistatic data: measurements taken from several sending and receiving positions.
- Monte Carlo reference: a brute-force simulation used as a benchmark for accuracy.
- Confidence band and coverage: a range that should contain the true value with a stated probability, and the check of how often that holds.
- Integral equation: a reformulation of the wave problem that can be solved numerically. · level: research-level

<details><summary>Original abstract</summary>

We develop a factorization method with finite-sample statistical guarantees for two-dimensional acoustic scattering by impedance obstacles whose boundary is random and whose data are finitely many noisy multistatic measurements. In the two-dimensional far-field normalization, the symmetrization must act on a phase-rotated far-field operator; we prove the optical and range identities for every realization of a compact family of uniformly bi-Lipschitz domains, with jointly measurable regularized indicators. A quadrature-weighted finite-sample analysis separates angular approximation, measurement noise, test-vector error, and regularization, and yields a consistency theorem for empirical means and variances, joint in all data parameters. Bounded indicators admit simultaneous confidence bands, a diagonal threshold recovers the probability that a sampling point lies in the random obstacle, and a nested design yields unbiased variance components. Computations use a combined-field integral equation proved invertible at all frequencies, and the finite-grid guarantees are examined in a coverage study against a high-accuracy Monte Carlo reference.

</details>

### [An Asymptotic One-Sample Surrogate for Non-Gaussian ERM with General Convex Regularization](https://arxiv.org/abs/2611.27754)
*Tianjian Zhang, Cosme Louart, Malik Tiomoko et al.* · `math.ST` · arXiv:2611.27754v1 · relevance 0.07

- **In one sentence**: The paper builds a one-Gaussian-vector surrogate for convex empirical risk minimization with non-Gaussian features and nonsmooth penalties, calibrates it to the true joint law, and proves agreement of minimizers, prediction variances, and risks under a Poincaré inequality and regularity assumptions.
- **In plain words**: The paper studies a common way of fitting statistical models: pick settings that make the model's error small on training data while penalizing complexity. Real data are rarely Gaussian (bell-curve shaped), which makes exact analysis hard. The authors replace the messy data with a simpler surrogate built from one Gaussian random vector, and they show that, under stated conditions, the fitted solution and its predictions behave similarly to those of the surrogate.
- **Why it matters**: It offers a way to predict test error and classification risk for penalized models on non-Gaussian data without relying on the data being Gaussian, which matters for anyone relying on such formulas. The text does not show how widely the conditions apply in practice, so its reach beyond the stated settings is uncertain.
- **Background needed**: - Empirical risk minimization (ERM): choosing model parameters to minimize average loss on a training sample.
- Convex penalty: an added cost term (such as the Lasso's sum of absolute values) that keeps the problem well behaved and encourages simple solutions.
- Gaussian approximation: replacing a complicated random quantity with a normal (bell-curve) one that has matching mean and variance.
- Poincaré inequality: a condition limiting how much a random function can fluctuate, used to control the non-Gaussian data.
- Anti-concentration: the requirement that random projections are not too likely to fall in a tiny interval.
- Hamilton-Jacobi / cavity method: a technique from statistical physics that compares a system with and without one data point. · level: research-level

<details><summary>Original abstract</summary>

We study convex empirical risk minimization (ERM) with non-Gaussian features and nonsmooth penalties through a surrogate driven by a single Gaussian vector. The surrogate preserves the penalty and calibrates its coefficients using the actual joint law of the feature-label model. We prove that this population calibration exists and is unique. We prove a Gaussian approximation for fresh prediction scores when the data satisfy a Poincar\'e inequality. Together with regularity conditions on the losses, this approximation yields agreement between the ERM minimizer and its surrogate in normalized means and prediction variances, as well as formulas for prediction and classification risks. The result covers general uniformly strongly convex penalties and pure Lasso under projection anti-concentration. The core proof relies on a cavity Hamilton-Jacobi argument that compares the main statistics of the two minimizers without differentiating the penalty.

</details>

## Statistical methods and applications

### [Hidden Semi-Markov Models for Fully Functional Time Series](https://arxiv.org/abs/2611.26838)
*Jake Hoover, Adam B Kashlak, Giseon Heo* · `stat.ME` · arXiv:2611.26838v1 · relevance 0.23

- **In one sentence**: The paper extends hidden semi-Markov models, with data-driven state durations, to fully functional time series, embedding the hidden chain in a larger Markov chain so Baum-Welch and Viterbi fitting can be used, and applies this to pediatric EEG signals in the Gaussian-measure setting of locally convex spaces.
- **In plain words**: Many signals, such as brain recordings, switch between hidden modes over time, and a common model for this is the hidden Markov model. That model forces each mode to last for a random time that drops off quickly, which often does not fit real data. This paper replaces it with a version where each hidden mode can last for a more flexible, data-driven length, and applies the approach to overnight sleep-study EEG recordings from children.
- **Why it matters**: Modeling how long a hidden state lasts is central to interpreting physiological signals such as sleep stages, so a more realistic duration model may matter for that kind of analysis. The provided text does not report comparative results against standard models, so its practical gain is not established here.
- **Background needed**: - Hidden Markov model: a model where an unseen state changes over time, and each state produces the observed data.
- Markov property: the next state depends only on the current one, which makes durations decay geometrically.
- Semi-Markov / sojourn time: a model that lets the time spent in a state follow its own distribution, such as a negative binomial.
- Baum-Welch and Viterbi: standard algorithms for fitting such models and finding the most likely hidden state sequence.
- Functional time series: data where each observation is a whole curve or function, not a single number.
- Gaussian measures on locally convex spaces: a generalization of normal distributions to infinite-dimensional settings, used here to handle curves.
- EEG and polysomnography: recordings of brain electrical activity and other signals during sleep. · level: research-level

<details><summary>Original abstract</summary>

Functional time series have a wide range of practical applications to modeling complex datasets such as Electroencephalogram (EEG) and other biological signals. Often latent states are hidden within the data dictating how a system is behaving and changing over time. The Hidden Markov Model (HMM) is one common and highly applicable latent state space model where the hidden state sequence evolves as a Markov chain. While the HMM has had much success modeling discrete, multivariate, and fully functional time series, it is also restricted by the Markov property which causes hidden states to persist only at geometrically decaying rates. This work investigates the implementation of hidden semi-Markov models for modeling fully functional time series data. This allows for the hidden state sequence to persist in a given state for a data-driven sojourn time, which can be parametrized by a discrete distribution (e.g. negative binomial) or left non-parametric. For efficient fitting of such a model, the hidden semi-Markov chain is embedded into a larger state space Markov chain and classic methods like the Baum-Welch and Viterbi algorithms are applied. We furthermore consider functional time series in the general setting of Gaussian measures in locally convex topological vector spaces. This is applied to a time series of pediatric EEG signals collected via overnight polysomnography.

</details>

### [A generalized Bayesian method for identifying local and global changepoints in dynamic network data](https://arxiv.org/abs/2611.26955)
*Yuhui Wang, Michael Jauch, Joshua Daniel Loyal* · `stat.ME` · arXiv:2611.26955v1 · relevance 0.10

- **In one sentence**: A generalized Bayesian changepoint method for dynamic networks uses a multinomial log loss, a low-rank sparse prior, and a Pólya-Gamma Gibbs sampler to locate local and global structural shifts in time-indexed adjacency matrices.
- **In plain words**: The paper addresses how to find the moments when a network that changes over time (such as who emails whom, or which countries are in conflict) suddenly shifts its pattern. The authors build a statistical method that looks at both the full set of connections and simple summary measures of the network, and it estimates where the change points are along with how uncertain those estimates are. They report that in simulations it was often more accurate than competing methods, and they illustrate it on an email network and an international conflict network.
- **Why it matters**: Detecting when relationships in a network change matters for fields that track communication, social ties, or political conflict over time. The text does not say how broadly the method will transfer beyond the benchmark simulations and the two applications shown.
- **Background needed**: - A dynamic network is a sequence of snapshots over time, each recorded as an adjacency matrix (a grid where an entry marks whether two nodes are linked).
- A changepoint is a time at which the underlying process generating the data shifts.
- Bayesian inference combines a prior belief with observed data to get a posterior distribution, which expresses uncertainty about unknown quantities.
- A generalized posterior replaces the usual likelihood with a loss function, so the method does not depend on knowing the exact data-generating process.
- Low-rank structure and sparsity are simplifying assumptions that keep the model parameters compact and mostly zero.
- Gibbs sampling and Pólya-Gamma data augmentation are computational techniques for drawing samples from the posterior. · level: research-level

<details><summary>Original abstract</summary>

We introduce a generalized Bayesian approach to multiple changepoint analysis in dynamic network data based on a multinomial log loss function and a prior distribution that imposes low-rank structure and sparsity on the model parameters. The method can detect local and global changes in network structure by incorporating information from both the full adjacency matrices and network summary statistics. Moreover, the proposed method is agnostic to the true data-generating process. From the generalized posterior distribution, we can make simultaneous inferences with meaningful uncertainty quantification about the locations of changepoints as well as deduce the network attributes and summary statistics that characterize them. For posterior simulation, we develop an efficient Gibbs sampler based on P\'olya-Gamma data augmentation with a computational cost that grows linearly with the number of observed edges in the dynamic network. Simulations across several benchmark network models show that the proposed method is often more accurate and flexible than competitors. We demonstrate the practical value of the method through applications to an email communication network and an international conflict network.

</details>

## AI industry news

### [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence)
** · `openai.com` · OpenAI News · relevance 0.12

- **In one sentence**: A news piece that discusses perplexity, a standard language-model metric, as a possible common yardstick for judging progress and emerging capabilities in AI models.
- **In plain words**: This article looks at a score called "perplexity," which measures how well an AI language model predicts the next word in a piece of text. It argues that this score could give developers a shared way to compare models and track new abilities as they appear. The text provided is only a one-sentence summary, so it does not show the specific results or examples behind the argument.
- **Why it matters**: Agreeing on how to measure AI progress matters for comparing systems and judging what they can do. The provided text is too thin to say how strong the argument is, so its practical impact is unclear.
- **Background needed**: - Language model: an AI system trained to predict and generate text one word at a time.
- Perplexity: a score where lower usually means the model finds the text less surprising, i.e. predicts it better.
- Evaluation/benchmark: a standard test used to compare systems on the same terms.
- Emerging capabilities: abilities that appear as models grow larger, which are hard to forecast. · level: intermediate

<details><summary>Original abstract</summary>

How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

</details>

### [Finding faster quantum algorithms with agents and formal verification](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)
** · `deepmind.google` · Google DeepMind News · relevance 0.09

- **In one sentence**: A news piece describing the use of AI agent teams and formal verification to improve quantum algorithms aimed at fusion energy and chemistry simulations.
- **In plain words**: The article covers work on making quantum computer programs faster for two hard scientific problems: modeling fusion energy and simulating chemistry. It says AI "agent teams" and formal verification (a method of using logic to mathematically prove that a program does what it should) were used to improve these algorithms. The text is only a short summary, so it does not give details of the specific improvements or how large they were.
- **Why it matters**: Faster quantum algorithms could matter for hard simulations in energy and materials research, but the summary gives no measured results, so the practical impact is unclear. It is also a sign of interest in using AI systems to help design and check scientific software.
- **Background needed**: - Quantum algorithm: a set of steps meant to run on a quantum computer, which uses quantum physics rather than ordinary bits.
- Fusion energy: generating power by fusing atomic nuclei, the process that powers the sun, which requires detailed simulations.
- Quantum chemistry simulation: using computers to model how molecules behave, a task that is very hard for classical machines.
- AI agents: software systems that carry out multistep tasks with some autonomy, here working as a team.
- Formal verification: mathematically proving that a program meets its specification, rather than only testing it. · level: research-level

<details><summary>Original abstract</summary>

Using agent teams and formal verification to improve quantum algorithms for fusion and chemistry.

</details>

### [Amazon snaps up Decart’s AI optimization tech for $7.5B as it prepares to sell Trainium chips](https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.09

- **In one sentence**: Amazon is reported to be acquiring the AI optimization technology and research team of Decart for about $7.5 billion, as it prepares to sell its Trainium AI chips.
- **In plain words**: Amazon is reportedly buying a startup called Decart, including its technology for making AI systems run more efficiently and the researchers who built it. The reported price is about $7.5 billion. The article is short and gives few details beyond the deal itself and the mention of Amazon's Trainium chips.
- **Why it matters**: Large acquisitions of AI efficiency teams can signal where big cloud companies are investing to cut the cost of running AI. The link to Amazon's Trainium chips suggests a possible connection to its chip business, but the text does not explain how the two are related.
- **Background needed**: - Decart: the company being acquired, per the headline and text; the article gives no further description of its work.
- AI optimization: techniques that make AI models faster or cheaper to run, for example by using less computing power.
- Trainium: Amazon's custom chips designed for training and running AI models, as an alternative to chips from other suppliers.
- "Reported" deal: the $7.5 billion figure comes from reports, not necessarily from an official announcement in this text.
- Acqui-hire: buying a company partly to bring its staff on board, which the phrase "research team" hints at. · level: introductory

<details><summary>Original abstract</summary>

Amazon is acquiring Decart’s AI optimization technology and research team in a reported $7.5 billion deal.

</details>

### [Megaspeed, the company at the center of the Jensen Huang scandal, appears headed for a US blacklist](https://techcrunch.com/2026/11/23/megaspeed-the-company-at-the-center-of-the-jensen-huang-scandal-appears-headed-for-a-u-s-blacklist/)
*Lucas Ropek* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.08

- **In one sentence**: A news report says Megaspeed, a company previously led by Alice Huang, appears headed for a U.S. blacklist that would bar American companies from doing business with it unless they obtain a special federal license.
- **In plain words**: The article reports that a company called Megaspeed seems likely to be placed on a U.S. government blacklist. If that happens, American businesses would generally not be allowed to work with it unless they first get a special permit from the federal government. The text is a short summary, so it does not explain the reasons for the listing or the wider dispute its headline refers to.
- **Why it matters**: Blacklists like this are a common tool for controlling which firms can buy US technology, and the headline links the company to a "Jensen Huang scandal," which may connect it to the AI chip supply business. The text is too thin to say what the scandal involves or how serious the listing will be, so treat the connection as unconfirmed.
- **Background needed**: - Blacklist (in this context): a government list of companies that U.S. firms may not trade with without special approval.
- Special license: a formal permission from a government agency that allows a restricted transaction.
- Jensen Huang: chief executive of Nvidia, a major maker of AI chips; the headline ties him to a scandal, but the article text does not describe it.
- Alice Huang: former leader of Megaspeed, per the article; the text does not say whether she is related to Jensen Huang.
- The article appears to be based on reporting of a planned or likely action, not a finalized one. · level: introductory

<details><summary>Original abstract</summary>

Megaspeed, which was previously led by Alice Huang, would be barred from doing business with U.S. companies unless those companies attained a special license from the federal government.

</details>

### [Richpanel helps companies automate 50% of support in 30 days](https://openai.com/business/customer-stories/richpanel-ai-customer-support)
** · `openai.com` · OpenAI News · relevance 0.07

- **In one sentence**: A short vendor-style news item says Richpanel uses several OpenAI-named models (GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna) to run AI customer-support agents that it claims can automate 50% of support within 30 days.
- **In plain words**: This item is about Richpanel, a company that sells customer-support software. It says its AI support agents are built on several language models: one set equips the agents with tools and step-by-step procedures, and another handles the actual back-and-forth conversations with customers. The headline claims companies can automate half of their support work within 30 days.
- **Why it matters**: It is a small example of how businesses are packaging AI models into customer-service products, which matters to support teams and to anyone judging such claims. The text gives only the headline figure and the model names, so it does not show how the 50% was measured or how well the agents perform; treat it as a company claim rather than a verified result.
- **Background needed**: - Language models are AI systems that generate and understand text; companies usually license them from a model provider and build products on top.
- "Automating support" means an AI handles customer requests that would otherwise need a human agent, often measured as a share of tickets.
- The model names given (GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna) are the labels used in the article; the text does not explain how they differ beyond their assigned roles.
- "Tools and procedures" refers to actions the AI can take (such as looking up an order) and fixed workflows it must follow.
- The article is brief and promotional in tone, and it gives no independent data, methods, or customer results. · level: introductory

<details><summary>Original abstract</summary>

Richpanel uses GPT-6 Astra and GPT-6.1 Sol to equip its AI support agents with tools and procedures, and GPT-6 Luna for their conversations.

</details>

## Model architectures and training

### [Turnout: Adaptive Attention Switching for Efficient Reasoning](https://arxiv.org/abs/2611.27500)
*Anna Kuzina, Mart van Baalen, Paul N. Whatmough et al.* · `cs.LG` · arXiv:2611.27500v1 · relevance 0.33

- **In one sentence**: Turnout converts a pretrained full-attention transformer into a hybrid that can switch each layer between full and linear attention at generation time, with the switching policy learned by reinforcement learning under a reward that trades off answer correctness against memory use.
- **In plain words**: Large language models remember what they have already written using a growing memory store, which gets expensive when they produce long chains of reasoning. This paper takes an existing model and swaps part of that memory for a fixed-size one, which saves memory but usually makes answers less accurate. The authors add a learned controller that decides, layer by layer and during writing, when to use the full memory and when to use the cheaper one, and report that this gives a better balance of accuracy and efficiency than fixed rules on reasoning tasks.
- **Why it matters**: Memory cost of long reasoning outputs is a practical limit on how these models are deployed, so a method that keeps accuracy while cutting memory could matter. The text reports only that the learned policy beats fixed-switching and static hybrid baselines on a Pareto frontier; it gives no specific numbers here, so the size of the gain is unclear from this summary alone.
- **Background needed**: - Transformer: the neural network architecture behind most modern language models.
- Attention: the mechanism that lets the model look back at earlier tokens when producing the next one.
- Key-value (KV) cache: stored memory of past tokens that grows as the output gets longer; it is the main memory cost during generation.
- Linear attention: an approximation with a fixed-size memory that does not grow with length, but is typically less accurate.
- Linearization / distillation: converting a trained model to use the cheaper mechanism by training the new path to mimic the original.
- Hybrid model: a model that uses both full and linear attention in different layers.
- Reinforcement learning: training a policy by rewarding good outcomes; here the reward combines correctness and memory use.
- Pareto frontier: the set of trade-offs where you cannot improve accuracy without spending more memory, or vice versa. · level: research-level
- Matched keywords: transformer, attention, linear attention, distillation

<details><summary>Original abstract</summary>

Post-hoc transformer linearization replaces the key-value cache of full attention, which grows linearly with generation length, with a fixed size state. This change reduces memory consumption but often hurts accuracy. In reasoning tasks, which require long generations, this effect is especially pronounced. In this work we introduce Turnout, a method that mitigates accuracy loss as a result of linearization, while maintaining its memory-reduction benefits. We apply post-hoc linearization to a pretrained full-attention model, training a linear path through distillation while leaving the original full-attention path unchanged. During response generation, the resulting hybrid model retains both paths and uses a learned policy to control when each layer switches from full to linear attention. We train the policy with reinforcement learning using a reward that balances answer correctness and memory use. Empirical evaluation of our method shows that the learned adaptive policy achieves a better accuracy-efficiency Pareto frontier on reasoning tasks compared to fixed switching and static hybrid baselines.

</details>

### [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973)
*Chang Nie, Chaoyou Fu, Songlin Liu et al.* · `cs.CL` · arXiv:2611.27973v1 · relevance 0.30

- **In one sentence**: MemOnce proposes a language model memory architecture that caches a small set of final-layer hidden states, decodes them into attention KV caches on demand, and uses sparse retrieval whose indices are computed once and shared across layers, with reported gains in memory footprint, latency, and throughput at 1M-token contexts.
- **In plain words**: Chatbots and other language models normally keep a growing scratchpad of everything they have read, and this scratchpad takes up more and more computer memory as conversations get longer. This paper proposes a different way to store that history: it keeps only a compact summary of each part and rebuilds the detailed working memory from those summaries when needed. The authors report that, when they adapt a 4-billion-parameter Qwen3.5 model with this method, the stored memory shrinks about 1,313 times and the time to process a 1-million-token input drops about 6.9 times, though these results come from the authors' own experiments.
- **Why it matters**: Memory cost is a practical limit on running language models over long, continuing interactions, so a method that keeps detail while cutting storage could matter for that use. The text does not show how the approach compares under independent testing, so its significance is still open.
- **Background needed**: - Transformer language models store a "KV cache": per-token internal values reused for attention, which grows with context length.
- Attention cost grows quadratically with context length in standard Transformers; linear-time models compress history into a fixed-size state instead.
- Hidden states are the internal numerical representations a network produces at each layer.
- Sparse attention means attending to only a selected subset of past items rather than all of them.
- Pretraining trains a model from scratch on broad data; post-training adaptation tunes an existing model further.
- Zero-shot generalization means applying a trained model to new tasks without task-specific training. · level: research-level
- Matched keywords: attention, pretraining, architecture

<details><summary>Original abstract</summary>

Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures compress history into fixed-size states, but struggle to retain fine-grained details. We introduce MemOnce, a foundation architecture that learns scalable memory states for language models. MemOnce is based on two core designs: (a) Memory encoder-decoder: it caches only a small subset of final-layer hidden states as compact memory representations and dynamically decodes them back into KV caches for attention layers; (b) Memory sparse attention: for each continual input, MemOnce adaptively retrieves relevant memory representations, with the sparse indices computed only once across layers. Coupling these two designs enables efficient on-the-fly memory loading and KV cache decoding, drastically reducing the GPU memory footprint and achieving linear-time complexity. We conduct extensive experiments to show that MemOnce outperforms Transformers and other architectures across varying model sizes, context lengths, and training paradigms (pretraining and post-training adaptation). In particular, adapting Qwen3.5-4B with MemOnce reduces memory state cache by 1313$\times$ and prefill latency by 6.9$\times$ at 1M context, and improves throughput by 3.5$\times$ and overall memory performance by +5.77%. Finally, MemOnce generalizes zero-shot to downstream representation tasks, achieving competitive results against specialized models.

</details>

## Machine learning theory

### [Renormalized Entropy from Symmetries: Simplicity Bias and Neural Heat Death](https://arxiv.org/abs/2611.27889)
*Vasco Portilheiro, Samuel Liebana, Andrew Saxe et al.* · `cs.LG` · arXiv:2611.27889v1 · relevance 0.30

- **In one sentence**: The paper derives the equilibrium distribution over functions learned by neural networks under Langevin dynamics with weak Gaussian regularization, showing how parameter symmetries induce a renormalized entropy that favors singular, low-rank functions in linear networks and inactive neurons in homogeneous-activation networks.
- **In plain words**: Neural networks can be reparameterized in many ways that leave the function they compute unchanged, and this paper asks whether those redundancies quietly steer which functions training tends to settle on. The authors study a noisy training process in the limit of vanishing regularization and find that, at nonzero noise, a renormalized "entropy" favors certain functions. In their examples, this pushes linear networks toward low-rank functions and pushes networks with homogeneous activations toward switched-off neurons, which can drive the output toward zero.
- **Why it matters**: It offers an explicit account of how symmetry alone can bias what a network learns, a question relevant to understanding generalization and implicit regularization. The text does not show how far these results extend beyond the linear and homogeneous-activation cases it treats, so broader impact is uncertain.
- **Background needed**: - Parameter symmetry: a change to a network's weights that leaves the computed function identical (for example, rescaling connected layers in a ReLU network).
- Langevin dynamics: a noisy gradient-descent process whose long-run behavior settles into an equilibrium distribution over parameters.
- Gaussian regularization: a penalty that pulls weights toward zero, here with a strength that is taken to zero.
- Low-temperature limit: the regime where the noise is small, so the process concentrates near minima of the loss.
- Entropy (in this context): a measure of how much parameter space corresponds to a given function; more volume means more probability.
- Neural tangent kernel: a linearized approximation describing how a function changes as parameters change; the paper uses it to interpret the "simplicity bias".
- Homogeneous activation: an activation such as ReLU where scaling the input scales the output by the same factor. · level: research-level
- Matched keywords: neural tangent kernel, implicit bias

<details><summary>Original abstract</summary>

Neural networks have parameter symmetries: parameter transformations that do not affect the represented function. How do these symmetries affect the functions that neural networks ultimately learn? We study the implicit bias arising from these symmetries by calculating the equilibrium distribution over represented functions under Langevin dynamics with Gaussian regularization. To isolate the effect of symmetries on this distribution, we study the limit in which the strength of the regularization is taken to zero. In certain cases, we show that the zero-regularization and infinite-time limits commute. In the low temperature limit, we recover known effective regularizations. At positive temperature, a renormalization procedure allows us to derive a novel entropy which predicts symmetry-induced preference for certain functions. For linear networks, we obtain explicit entropy terms that favor singular and low-rank functions. For networks with homogeneous activations, we find entropy terms that favor inactive neurons, which can lead to neural "heat death" in which equilibrium mass concentrates on networks with vanishing output. We interpret these results through the neural tangent kernel, as a simplicity bias selecting for functions that vary slowly under variations in the parameters.

</details>

### [Verifying and Strengthening Neural Tangent Kernel Theory](https://arxiv.org/abs/2611.27487)
*Hao Zhu* · `cs.LG` · arXiv:2611.27487v1 · relevance 0.26

- **In one sentence**: A Lean 4 machine-checked formalisation of the two-layer neural tangent kernel (NTK) convergence theorem for tanh networks, which also tightens the standard concentration-width bounds and flags a Hessian-norm obstacle to the usual linearisation argument.
- **In plain words**: Very wide neural networks trained by gradient descent are often claimed to behave in a simple, predictable way, and a known theory (neural tangent kernel theory) explains why. This paper rebuilds the main argument for a small two-layer network inside a computer proof assistant, so every step is checked by machine rather than by reading. The authors report that the checked proof holds with explicit width conditions and that the error shrinks exponentially over training time.
- **Why it matters**: Checking a standard theory line by line can catch hidden gaps, and the paper reports that its alternative variance bound gives concentration-width certificates 36 to 121 times smaller than the conventional one in the stated settings. The required widths remain far beyond practical sizes, and the text itself says this limits applicability, so the work is best read as a verification and sharpening exercise rather than a practical advance.
- **Background needed**: - Neural network: a function built from layers of weighted sums and simple nonlinear functions, whose weights are tuned by training.
- Gradient descent / gradient flow: repeatedly nudging weights downhill on an error measure; gradient flow is the continuous-time version.
- Neural tangent kernel (NTK): a fixed similarity measure between inputs that describes how a very wide network changes during training.
- Lazy training: a regime where weights move only slightly from their starting values, so the network acts almost like a fixed linear model.
- Concentration inequalities: bounds stating that random quantities stay close to their average with high probability; the matrix-Bernstein bound is one such tool.
- Operator norm and Hessian: a measure of the largest stretching a matrix or curvature matrix applies; the Hessian describes local curvature of the loss.
- Lean 4: a proof assistant in which mathematical statements and proofs are checked by computer.
- Width: the number of units in a hidden layer. · level: research-level
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

Writing Neural tangent kernel (NTK) theory explains why very wide neural networks trained by gradient methods converge in the lazy-training regime. Its standard proof combines matrix concentration, random Gram matrices, continuous-time dynamics, spectral perturbation, and a bootstrap argument, but has lacked machine-checked verification. We present a Lean\~4 formalisation for two-layer networks, proving an end-to-end theorem: for a smooth bounded activation (instantiated with $\sigma=\tanh$), frozen biases, paired $\pm 1$ initialisation, and explicit width conditions, gradient flow exists uniquely with probability at least $1-\delta$, and $$ \|r(t)\|^2 \leq \|y\|^2 e^{-\lambda_0 t/2}. $$ The sole data assumption is population NTK non-degeneracy, $\lambda_0>0$. Initial coercivity, kernel drift, the movement bootstrap, the residual ODE, and flow existence and uniqueness are formally proved. The formalisation also sharpens the standard analysis in two ways. First, replacing the conventional matrix-Bernstein variance proxy with the classical row-covariance proxy yields estimated concentration-width certificates for $\tanh$ that are $36$--$53\times$ smaller at $(m,d)=(16,8)$ and $94$--$121\times$ smaller at $(32,16)$. Lean certifies the inequality; the ratios are numerical. Second, the network Hessian has operator norm $\Theta(\sqrt{p})$ on the sup-norm parameter ball (a paper calculation), preventing the expected $O(1/\sqrt{p})$ linearisation bound via sup-norm Taylor estimates. An $L^2$ parameter geometry resolves this issue. Required widths remain polynomial but far beyond practical scales, limiting applicability.

</details>

## Large language models

### [Partially canonical axes in large language model representations](https://arxiv.org/abs/2611.26920)
*Andrea Gregor de Varda, Ferdinando D'Elia, Greta Tuckute et al.* · `cs.CL` · arXiv:2611.26920v1 · relevance 0.14

- **In one sentence**: Across 12 LLMs from six families, the native coordinate axes of hidden representations align better with other models, human brain responses, and interpretable linguistic features than randomly rotated axes with the same geometry, yet fall short of the best achievable alignment, so the axes are "partially canonical."
- **In plain words**: A common assumption is that the individual numbered slots inside a language model's internal state are arbitrary, and only whole directions carry meaning. This paper tests that by comparing the model's actual slots against versions of the same data rotated to a random orientation. The authors find the real slots match other models, human brain activity during language, and simple linguistic features somewhat better than the rotated versions, but not as well as the best possible alignment.
- **Why it matters**: If individual units in language models carry consistent meaning, that matters for interpreting how these systems work and for comparing them with brains. The paper's claim is a middle position rather than a full answer, and the text does not show how large or robust the effects are beyond the summary given.
- **Background needed**: - Hidden representation: the list of numbers a neural network produces internally for a piece of text.
- Coordinate axis: one of those numbered positions; rotating the whole space changes the axes but not the overall geometry of the points.
- Random rotation baseline: a control in which the same data is spun to a random orientation, to test whether the original axes are special.
- Representational alignment: a measure of how similar two systems' internal geometry is, used here to compare models with each other and with brain recordings.
- Interpretable linguistic features: properties such as part of speech or syntactic role that humans can name.
- Canonical vs. arbitrary axes: canonical means the axes pick out meaningful units; arbitrary means any rotation would work equally well. · level: research-level

<details><summary>Original abstract</summary>

Large language models (LLMs) develop rich internal representations of language, but whether their individual coordinate axes carry meaning, or whether meaning is encoded only in directions in representation space, is still an open question. A common assumption is that individual axes in LLMs are arbitrary. We here challenge this view: across 12 LLMs from six model families, the native axes are reliably more aligned with other models' representations, with human brain responses to language, and with interpretable linguistic features than randomly rotated axes that preserve the same geometry. The native axes nonetheless fall well short of the best achievable alignment, so LLM coordinates are not fully arbitrary but also not fully canonical: they are partially canonical. A theory of how LLMs represent language must explain both the population geometry they learn and why individual units acquire patterns of response profiles that recur across systems.

</details>

### [Explicit Style Extraction for Personalized Long-Form Text Generation](https://arxiv.org/abs/2611.27211)
*Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam et al.* · `cs.CL` · arXiv:2611.27211v1 · relevance 0.13

- **In one sentence**: SP-Refine makes style extraction an explicit inference-time step for personalized long-form generation, using a 28-aspect taxonomy (StylePrism) to build a user style profile that guides draft revision on LongLaMP tasks.
- **In plain words**: Language models that write in a particular person's voice usually get a few of that person's past texts pasted into the prompt and must work out the style on their own. This paper proposes a method where the model first writes down an explicit profile of the user's writing habits, with quoted examples, then drafts and revises against that profile. Across three long-form writing tasks and three models, the method beat the standard retrieval-based baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average.
- **Why it matters**: Personalizing text generation is a practical goal for writing assistants, and the paper's ablations suggest the explicit profile works mainly as revision guidance rather than a replacement for the user's samples. Whether the gains carry over to real users and to other metrics is not shown in the text; the authors also note that larger gains depend on information unavailable at inference time.
- **Background needed**: - Retrieval-augmented generation (RAG): putting relevant examples from a user's past into the model's prompt before it writes.
- Personalized long-form generation: producing multi-paragraph text that matches a specific person's style.
- ROUGE and METEOR: automatic scores that measure word overlap between generated text and a reference text; they are imperfect proxies for quality or style match.
- Inference-time method: a technique applied when the model is run, without retraining it.
- Ablation: a test that removes one component to see how much it contributes.
- Oracle variant: a version that peeks at the answer, used to estimate an upper bound. · level: intermediate

<details><summary>Original abstract</summary>

Personalized long-form generation asks a language model to write new text the way a specific user would. The standard recipe, retrieval-augmented generation, places a few of the user's past texts in the prompt but leaves the model to decide what to take from them. We introduce StylePrism, a taxonomy of 28 stylistic aspects in seven categories, and SP-Refine, an inference-time method that makes style extraction an explicit step: the model first fills StylePrism with the user's patterns, quoted evidence, and habits to avoid, then drafts from the user's samples and revises the draft twice against this profile, guided by its own style scores. On the three long-form tasks of LongLaMP with three LLMs, SP-Refine outperforms LongLaMP's retrieval-augmented baseline in 25 of 27 ROUGE and METEOR comparisons, by 10.2% on average and by up to 35.8%. Annotating users' own texts with the extracted profiles shows that StylePrism captures concrete, checkable habits, from the order of rhetorical moves to a reviewer's sign-off. Ablations show that the profile helps as revision guidance, not as a replacement for the samples: writing from the profile alone is worse in all 27 comparisons, while a single implicit-inference call is a cheaper alternative that comes close. Oracle variants that let the reviser see the reference, together with reference-free controls, show that larger refinement gains require information unavailable at inference time.

</details>

## Computer vision

### [PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation](https://arxiv.org/abs/2611.27266)
*Junyi He, Xu Peng, Chengming Xu et al.* · `cs.CV` · arXiv:2611.27266v1 · relevance 0.18

- **In one sentence**: PP-CFG is a few-step diffusion distillation method that keeps positive and negative text conditions separate, combines their attention responses with opposite signs, and uses a scale-and-timestep mixer to keep adjustable classifier-free guidance and negative prompting for image and video generation.
- **In plain words**: Modern AI image and video generators often need many small refinement steps to produce output, and speeding them up by distilling them into fewer steps tends to remove the ability to fine-tune how strongly a prompt is followed or to tell the model what to avoid. This paper proposes a way to keep those controls in a four-step student model. The authors report results on video (Wan2.1) and image (Qwen-Image) generators, including a VBench score of 81.46 in four steps and higher target-removal rates on their own 1,000-case negative-prompt benchmark than the teacher models.
- **Why it matters**: Making generation both fast and controllable is a practical bottleneck for image and video tools, so a method that preserves guidance and negative prompts in few-step models is worth watching. The text supports claims across two backbones and two distillation methods, but the evaluation is described only at a high level and the benchmark is the authors' own, so the strength of the generality claim is not yet established.
- **Background needed**: - Diffusion models generate images or videos by starting from noise and removing it over many denoising steps.
- Distillation trains a faster "student" model with few steps to imitate a slower "teacher" model.
- Classifier-free guidance (CFG) is a dial that controls how strongly the output follows a text prompt.
- Negative prompts tell the model what to leave out of the output.
- Attention is the mechanism through which parts of the model weigh and combine information from the text and image.
- VBench is a standard benchmark suite for scoring video generation quality.
- Distribution matching distillation (DMD) and latent consistency models (LCM) are two specific distillation techniques named in the paper. · level: research-level

<details><summary>Original abstract</summary>

Few-step diffusion distillation reduces sampling cost but often weakens adjustable classifier-free guidance (CFG) and runtime negative prompting. We introduce PP-CFG, an architecture that keeps positive and negative text conditions separate and combines their attention responses with opposite signs within a shared visual backbone. Its Scale-Time Polarity Mixer refines each condition using the guidance scale and denoising timestep, allowing prompt influence to vary throughout generation. The student retains a continuous scale input and selectable negative prompts with one visual backbone pass per step. We evaluate PP-CFG on Wan2.1 for video generation with distribution matching distillation (DMD), and on Qwen-Image with both latent consistency model (LCM) distillation and DMD. PP-CFG achieves 81.46 VBench in four steps and lower video teacher-student distances across guidance scales than step-distilled DMD. On NegElement-1K, our benchmark of 1,000 matched image and video prompt cases, it achieves higher target-removal rates than the corresponding teachers. These experiments support the method's generality across attention architectures, generation modalities, and distillation objectives while retaining competitive generation quality.

</details>

### [Learning 3D MRI Representations with Generative Adversarial Networks](https://arxiv.org/abs/2611.27057)
*Sujeet Lahane, Sapna Mishra, Akash Suryavanshi et al.* · `cs.CV` · arXiv:2611.27057v1 · relevance 0.15

- **In one sentence**: The paper proposes R2RG, a 3D CNN-based representation learning method that uses an auto-encoding GAN and a composite loss to learn reconstruction-based features from 3D MRI scans with limited data, reporting gains over contrastive methods on Parkinson's and Alzheimer's classification.
- **In plain words**: Medical scans like MRI are 3D, but many AI methods handle only flat 2D slices, which throws away depth information, and they often need more data than medical datasets provide. This paper presents a method that learns compact summaries of whole 3D brain MRI volumes by training a network to rebuild the scans, with a generative adversarial network (a pair of AI models that compete to make realistic images) helping sharpen the rebuilt results. The authors report that these learned summaries work across several datasets, including small ones, and perform better than certain competing approaches on Parkinson's and Alzheimer's disease classification.
- **Why it matters**: Many medical AI tasks have little labelled data, so methods that learn useful features without labels could matter in clinical research. The text reports results on a few datasets, but it does not show how well the approach would hold up in routine clinical use, so its wider significance is still to be tested.
- **Background needed**: - Representation learning: training a model to turn raw data into compact numerical features that other tasks can use.
- Reconstruction-based learning: learning by trying to rebuild the original input from its compressed form, with no human labels needed.
- Contrastive learning: learning by pulling similar examples together and pushing different ones apart in feature space; a common alternative.
- CNN (convolutional neural network): a common type of image model that detects local patterns; a 3D version works on volumes rather than flat images.
- GAN (generative adversarial network): two networks trained against each other, one generating images and one judging them, often used to make outputs look realistic.
- MRI: magnetic resonance imaging, which produces 3D scans of soft tissue such as the brain.
- Parkinson's and Alzheimer's classification: deciding from scans whether a patient has these diseases, used here as a test of the learned features. · level: research-level

<details><summary>Original abstract</summary>

Learning representations of visual images is a challenging task. It requires extracting abstract patterns from high-dimensional data without explicit supervision. This becomes pronounced with 3D MR imaging due to sparse features, higher dimensional inputs, and smaller datasets. Many state-of-the-art representation learning algorithms successfully rely on transformers and diffusion-based architectures. However, these methods struggle with smaller datasets. In effect, solution methods relax the problem by slicing 3D volumes and solving the problem for 2D medical imaging, resulting in a loss of spatial 3D information. We present R2RG, a representation learning method based on Convolutional Neural Networks (CNNs), with Generative Adversarial Networks (GANs) honing the reconstruction task. Our key insights lie in exploiting architectural biases in 3D CNNs, combined with data-efficient auto-encoding GANs and a composite loss function to enhance reconstruction fidelity and stabilize training. Our experiments on three standard datasets and a locally collected dataset show that R2RG not only achieves superior performance but also generalizes to heterogeneous and smaller datasets. Furthermore, representations learned with R2RG outperform those learned with contrastive-based representation learning methods on Parkinson's and Alzheimer's disease classification. Our work demonstrates that reconstruction-based representation learning is a promising direction for 3D medical imaging under limited data availability.

</details>

## Reinforcement learning

### [Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27368)
*Dennis Gross, J{\o}rn Eirik Betten, Helge Spieker* · `cs.MA` · arXiv:2611.27368v1 · relevance 0.23

- **In one sentence**: The paper proposes DisQ, a test-case selection method that uses a "Q-value gap" (disagreement between agents' value estimates in a state) to find failure-revealing states when testing value-based cooperative multi-agent reinforcement learning policies.
- **In plain words**: Teams of AI agents that learn to work together can behave unsafely in ways their reward signal does not capture, and those failures are hard to explain. This paper proposes a way to pick which situations to test by flagging states where the agents' estimates of future reward diverge beyond a set threshold. The authors report that, in most of four benchmark environments tested, this selection finds more failures than random testing or genetic-algorithm search methods borrowed from single-agent testing.
- **Why it matters**: Testing multi-agent systems for safety has received less attention than testing single agents, and the authors offer an explainable signal computable from one state without running the system. Its practical value beyond the four benchmarks evaluated is not established in the text.
- **Background needed**: - Reinforcement learning: an AI learns by trying actions and receiving rewards.
- Multi-agent reinforcement learning: several agents learn at the same time, here aiming at one shared goal.
- Q-value: a learned estimate of the total future reward from taking an action in a given state.
- Coordination failure: agents' individual choices work against each other, so the team does badly.
- Test case selection: choosing which situations to run a system in, to find failures efficiently.
- Random testing and genetic-algorithm search: standard baseline methods for finding failures. · level: research-level
- Matched keywords: reinforcement learning, Q-learning

<details><summary>Original abstract</summary>

Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the reward, and these behaviors are hard to explain. However, testing CMARL policies for safety has received less attention than the safety testing of single-agent RL policies. In this paper, we propose DisQ, a test case selection method that identifies failure-revealing states in value-based CMARL by exploiting a signal specific to trained Q-learning agents. The signal is the Q-value gap, an explainable metric that flags a state when the agents' estimates of the achievable return diverge by more than a calibrated threshold. DisQ selects such states for execution and skips those without a gap. Our experiments in four CMARL benchmark environments show that, in most of the evaluated configurations, DisQ improves failure detection over single-agent RL testing methods applied to CMARL, namely random testing and search-based testing with genetic algorithms. Our main contributions are the Q-value gap, an indicator of potential miscoordination computable from a single state without executing the system, and DisQ, a test case selection method that adapts existing single-agent testing methods to CMARL.

</details>

### [Decision Models Are General-Purpose Process Reward Models](https://arxiv.org/abs/2611.27068)
*Jiajun Fan, Qinglong Zheng, Ziwen Wang et al.* · `cs.AI` · arXiv:2611.27068v1 · relevance 0.20

- **In one sentence**: DM-PRM turns a general-purpose yes/no decision model into a zero-shot, step-level process reward that is added to the advantage in policy-gradient RL for language agents, evaluated on ALFWorld and WebShop.
- **In plain words**: Training AI agents with reinforcement learning usually gives one score at the end of a whole attempt, so the agent cannot tell which individual steps helped. This paper proposes asking a general yes/no question about each step, using a model's probability answer as a step-by-step score, without extra labels or training. The authors report that this improves the GRPO training method on two household and web-shopping task benchmarks, and that it helps other methods too.
- **Why it matters**: It offers a way to get per-step credit without hand-made step labels or a separately trained critic, which are costly to build. Whether this holds beyond the two benchmarks and one small model (Qwen2.5-1.5B) is not shown in the text, so its broader value remains to be tested.
- **Background needed**: - Reinforcement learning (RL): training by trial and reward; here an AI language agent learns from task success or failure.
- Policy gradient: a family of RL update rules that make good actions more likely.
- Reward and credit assignment: deciding which steps in a long attempt deserve the credit or blame for the result.
- Process reward model (PRM): a scorer that rates intermediate steps, not just the final outcome.
- Advantage: how much better an action turned out than expected; used to scale the learning update.
- GRPO, PPO, GiGPO, HGPO, GraphGPO: named RL training methods for language agents; PPO uses a learned critic.
- ALFWorld and WebShop: simulated benchmarks for household tasks and online shopping.
- Zero-shot: used without task-specific training. · level: research-level
- Matched keywords: reinforcement learning, reward model

<details><summary>Original abstract</summary>

Reinforcement learning (RL) from verifiable outcomes gives a language agent one reward per episode: every step is credited alike, and nothing about the task is learned when all rollouts fail. The last mile, step-level credit, usually requires step labels, a learned critic, costly LLM judges or hand-written rules. We introduce DM-PRM, which turns a general-purpose decision model -- one answering yes/no questions with probabilities -- into a general-purpose process reward model (PRM), zero-shot: no step labels, no fine-tuning, no critic. DM-PRM asks one question per step and adds the standardised answers to the advantage. It plugs into any policy-gradient method; one model, with one question text per environment, serves household tasks, web shopping and multiple RL methods. With Qwen2.5-1.5B it lifts GRPO by over twenty points on ALFWorld and over ten on WebShop, overtakes GiGPO on ALFWorld and learns in far fewer iterations; it also improves GiGPO and GraphGPO on both benchmarks and reaches the highest success of our comparison, ahead of critic-based PPO and of state-of-the-art GiGPO, HGPO and GraphGPO. Its scores locate useful steps in failed rollouts, and trained agents drop idle actions and explore instead of circling. DM-PRM shows that step credit need not be learned: it can be asked for.

</details>

## AI safety and alignment

### [Preserving Pretrained CFG Structure in RL for Diffusion Models with Conditional Contrast Regularization](https://arxiv.org/abs/2611.27288)
*Yunfei Zheng, Xiaolong Wang, Dandan Zheng et al.* · `cs.LG` · arXiv:2611.27288v1 · relevance 0.29

- **In one sentence**: The paper proposes Conditional Contrast Regularization (CCR), which uses the frozen pretrained model's classifier-free guidance direction as a structural prior to keep diffusion-model generation quality from degrading during reinforcement-learning fine-tuning for a target reward.
- **In plain words**: Image-generating AI models are often fine-tuned with reinforcement learning to score higher on a chosen reward, but this can make the images worse overall even as the score rises. The authors treat this as a kind of reward hacking and look at a built-in guidance technique (classifier-free guidance) that already makes images clearer and better aligned with prompts. They use it as a reference point to keep the fine-tuning from drifting away from good-quality behavior.
- **Why it matters**: Reward-driven fine-tuning that quietly lowers overall quality is a practical concern for deployed generative models, and this work offers a concrete, cheap regularizer tied to an existing component. Its broader significance beyond the reported experiments is not established by the text, which describes results only across unspecified reward settings and backbones.
- **Background needed**: - Diffusion models: image generators that start from noise and refine it step by step.
- Reinforcement learning (RL) post-training: adjusting a trained model to maximize a score (reward) on its outputs.
- Reward hacking: the model improves the score in ways that do not reflect the real goal.
- Classifier-free guidance (CFG): a standard sampling technique that pushes outputs toward the prompt, improving clarity and alignment.
- Correction vectors: the difference between a model's prediction and a baseline, used here to compare CFG and RL updates geometrically.
- Frozen reference model: a copy of the original model whose weights are not updated, used as an anchor.
- Regularization: an extra penalty that keeps training close to a desired behavior. · level: research-level
- Matched keywords: alignment, reward hacking

<details><summary>Original abstract</summary>

Reinforcement Learning (RL) has become an important component in the post-training of diffusion models. In practice, however, standard RL often improves the target reward without reliably preserving holistic generation quality, leading to unstable reward-quality trade-offs that we view as a form of reward hacking. Since Classifier-Free Guidance (CFG) is known to improve visual clarity, prompt alignment, and perceptual quality in generation, we investigate whether its underlying structure can serve as a useful prior during RL. We present a unified geometric view that interprets both CFG and RL as correction vectors in a common prediction space, and identify the projection of the RL-induced correction onto the pretrained CFG correction as a useful diagnostic of quality-related structural preservation. Geometric analysis and rotation intervention further show that the pretrained CFG direction carries information useful for generation quality that reward-driven RL updates do not necessarily preserve. Based on this insight, we propose Conditional Contrast Regularization (CCR), which uses the frozen reference model's conditional contrast as a local structural prior during RL. Experiments across multiple reward settings and backbones show that CCR more consistently preserves generation quality while maintaining competitive reward, yielding a better reward-quality trade-off than standard RL and generic regularization methods.

</details>

### [The Assistant Persona Differs Across Languages in Activation Space](https://arxiv.org/abs/2611.27504)
*Daniel Yoo, Naama Rozen, Evan Harris* · `cs.CL` · arXiv:2611.27504v1 · relevance 0.24

- **In one sentence**: The paper extracts an "assistant persona" direction in activation space for 31 languages in Qwen3-32B and finds that these directions differ across languages, correlate with resource level, and affect how steering changes jailbreak susceptibility.
- **In plain words**: Language models are known to be less safe in languages with less training data. This paper looks inside a model to ask whether its internal "helpful assistant" setting is the same across languages. The authors found that the internal direction for this persona differs noticeably from language to language, and that the differences track how much data each language has.
- **Why it matters**: It offers a mechanistic, inside-the-model account of a safety gap that has so far mostly been measured from outside through behavior. The text suggests that multilingual alignment may need to target the assistant persona directly, though the findings come from a single model and the text does not show whether this carries over to other models.
- **Background needed**: - Activation space: the set of internal numerical states a neural network passes through when processing text.
- Direction: a particular axis in that space; a "persona direction" is one linked to a role or personality the model adopts.
- Cosine similarity: a score from -1 to 1 for how closely two directions point the same way; 1 means identical.
- Steering: nudging the model's internal activations along a direction to change its behavior.
- Jailbreak: a prompt crafted to get a model to ignore its safety rules.
- Resource level: how much text data exists for a language; "lower-resource" languages have less.
- Qwen3-32B: a specific open large language model with 32 billion parameters. · level: research-level
- Matched keywords: alignment, jailbreak

<details><summary>Original abstract</summary>

Large language models behave differently across languages, and are noticeably less safe in lower-resource languages. This gap is well established behaviorally, but not mechanistically. Directions in activation space, including the assistant persona direction, are almost always extracted from English and assumed to generalize across languages. We extract the assistant persona direction in 31 languages in Qwen3-32B, and find that the resulting axes differ substantially: their cosine similarity to the English axis ranges from 0.378 to 0.911. Moreover, each language's assistant persona direction and its magnitude are correlated with the language's resource level. We also find that the model's default assistant state is farther from the helpful assistant pole in lower-resource languages. Finally, steering against a language's own axis amplifies persona-based jailbreak more than steering against the English axis. These results indicate that the model does not carry a single assistant representation across languages. More broadly, the assistant persona may need to be an explicit target of multilingual alignment.

</details>

## Interpretability

### [Parasite Features: Causal Abstraction Through Spurious Pathways](https://arxiv.org/abs/2611.26711)
*Denis Sutter, Qing Yao, Sasha Boguraev et al.* · `cs.LG` · arXiv:2611.26711v1 · relevance 0.29

- **In one sentence**: The paper shows that Distributed Alignment Search, a causal-abstraction interpretability method, can be fooled into crediting a neural network with a feature it does not actually use, via "parasite features" formed by two directions in representation space that together pass equivalence tests.
- **In plain words**: Researchers study how to check whether a neural network does a task in the same way a human-written algorithm would. They argue that a common checking method can be fooled: two separate directions inside the network, one that sorts inputs by some feature and one that pushes the output toward an answer, can together mimic the intended behavior. The method then appears to show the network uses that feature when it may not. They test this on grammar agreement and two-digit addition.
- **Why it matters**: Causal abstraction is a leading tool for explaining what neural networks compute, so a case where it gives false positives matters for how its results should be read. The text does not say how widespread this failure is in practice, and it only reports experiments on two tasks.
- **Background needed**: - Neural network "representation space": the internal numerical state of a model, where concepts can be encoded as directions.
- Mechanistic interpretability: reverse-engineering what internal parts of a model do.
- Causal abstraction: testing whether a network's internal computation matches a simpler algorithm by intervening on internal states and checking that outputs match.
- Distributed Alignment Search (DAS): a method that learns a linear map to find directions in the network that correspond to an algorithm's variables.
- Spurious feature: something that looks like the real mechanism in a test but is not actually what the model relies on. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Causal Abstraction defines a notion of \emph{equivalence} between a neural network and an algorithm, thus serving as a powerful framework for mechanistic interpretability. In this paper, however, we show the existence of a class of \emph{spurious features} which straightforwardly pass such equivalence tests. Suppose there are two directions in a model's representation space where: (i) one discriminates the input based on some feature, and (ii) the other steers the model towards a certain output. Interpretability methods based on Causal Abstraction (e.g., Distributed Alignment Search) can \emph{spuriously} simulate these directions' combined behavior by leveraging pathways passing through them, giving the impression that the model implements this feature. In such cases, we say the method discovered a \defn{parasite feature}. Experimentally, we show that Distributed Alignment Search finds parasite features using linear alignment maps in two tasks: syntactic agreement and two-digit addition. Our paper highlights an important consideration for Causal Abstraction and contributes to the ongoing debate about best practices for mechanistic interpretability.

</details>

### [WaXup: Weight Averaging of Experts as Data Augmentation for Robust Introspection](https://arxiv.org/abs/2611.27353)
*Marc Bo\"elle, Lucas Dixon, Alexandre Ram\'e* · `cs.CL` · arXiv:2611.27353v1 · relevance 0.25

- **In one sentence**: WaXup augments the training data for trainable introspection (models trained to describe their own finetuned behaviors) by linearly interpolating weights of finetuned experts, motivated by linear mode connectivity, and evaluates it on hidden-behavior models, a real-world NLP meta-dataset, and AuditBench.
- **In plain words**: Researchers are trying to get AI language models to explain, in plain words, what they were taught during extra training, rather than relying on hard-to-read technical inspection of their internals. This paper proposes WaXup, which creates extra training examples by blending the settings of several specialized versions of a model. The authors report that this improves how accurately the model describes its behaviors and how well it holds up when the test situations change.
- **Why it matters**: Being able to ask a model what it has learned, and trust the answer, could help people audit models for hidden or concealed behaviors, which matters for safety. The text reports gains in accuracy and robustness but gives limited detail on size or scale of those gains, so its practical impact is not yet clear.
- **Background needed**: - Mechanistic interpretability: studying a model's internal parts (weights and activations) to understand what it computes.
- Finetuning: extra training of a general model on a narrow task or behavior, producing a specialized "expert" version.
- Introspection (here): training a model to describe, in natural language, the behavior it acquired during finetuning.
- Weight space and weight averaging: each model is a long list of numbers (weights); blending two such lists gives a model whose behavior is often between the originals.
- Linear mode connectivity: the observation that some finetuned models can be averaged without losing performance, suggesting they lie in a smooth region together.
- Data augmentation: creating extra training examples from existing ones to make learning more robust. MiXup, the framework built on, is a related augmentation method.
- Alignment auditing and AuditBench: checking whether a model has hidden or concealed behaviors; AuditBench is a suite of models adversarially trained to hide theirs. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

As the capabilities of large language models keep improving, traditional mechanistic interpretability methods struggle to keep pace. In contrast, trainable introspection methods emerge as a promising alternative; they repurpose the model itself as a self-diagnostic tool, trained to verbalize what it has learned during finetuning in natural language. While training on datasets of finetuned experts achieves encouraging results, it currently lacks robustness and generalization. Building on the data augmentation framework of MiXup, we introduce WaXup, a method that augments the introspection training set through linear interpolation in the weight space. This is motivated by the linear mode connectivity property: weight averaged experts interpolate the behaviors of the initial experts. We evaluate WaXup on three benchmarks: hidden-behavior models, a meta-dataset of real-world NLP tasks and AuditBench, a challenging alignment auditing suite of models adversarially trained to conceal their behaviors. WaXup improves the accuracy of generated descriptions as well as robustness to various distribution shifts. We hope to improve the reliability of trainable introspection methods towards better and safer models.

</details>

## AI for mathematics

### [Budget-Aware Predict-and-Verify Theorem Proving with Heterogeneous LLM Solvers](https://arxiv.org/abs/2611.26906)
*Wei Jiang, Ziran Liu, Wei Wang* · `cs.AI` · arXiv:2611.26906v1 · relevance 0.23

- **In one sentence**: BudgetPV is an agentic predict-and-verify system that uses a cross-solver predictor, trained with two different loss objectives for early and late allocation stages, to route Lean subgoals across heterogeneous LLM provers under a compute budget.
- **In plain words**: Automatic theorem provers use AI language models to break math proofs into smaller pieces, but some models are costly and others are cheap. This paper describes a way to decide which model should try each piece, and how to spend more effort on pieces that are still unsolved. The authors report that their method used less model computation than giving every piece the same effort, while solving the same number of pieces on four math benchmarks.
- **Why it matters**: Running large models on every step of a formal proof is expensive, so a better way to split effort across models could make automated proving cheaper. The text does not say how large the savings are in absolute terms or how the approach compares with other budget-allocation methods, so its wider significance is uncertain.
- **Background needed**: - Theorem proving: a formal proof is checked by a computer; here the proof assistant is Lean.
- Subgoal: a smaller statement that must be proved on the way to the full theorem.
- LLM solver: a language model that tries to write a proof; solvers differ in skill and cost.
- Predict-and-verify: a predictor guesses which solver is likely to succeed, and the proof checker confirms the result.
- Cross-entropy: a standard training loss for classification; class weighting makes rare classes count more.
- Calibrated probabilities: predicted probabilities that match how often the outcomes actually occur.
- Benchmarks named: Lean Workbook, miniF2F, ProofNet, PutnamBench. · level: research-level
- Matched keywords: Lean, theorem proving

<details><summary>Original abstract</summary>

Large language model (LLM) theorem solvers differ in both proving capability and inference cost. Applying an expensive solver to every subgoal wastes computation when cheaper models are sufficient, while always starting from the cheapest solver wastes attempts on subgoals that require stronger models. We present BudgetPV, an agentic budget-aware predict-and-verify system that allocates computation across unresolved subgoals and heterogeneous LLM solvers. BudgetPV uses a cross-solver predictor to guide solver selection for each subgoal and revises the allocation as verification feedback becomes available. The allocation problem changes as proving progresses. Early decisions mainly determine which solver should handle an untried subgoal, while later decisions determine which previously attempted subgoals should receive additional computation. We train the predictor with two objectives for these two stages. Class-weighted cross-entropy improves assignment to less frequent stronger solvers during the initial stage, while plain cross-entropy provides better calibrated probabilities for later allocation among previously attempted subgoals. We evaluate BudgetPV on Lean Workbook, miniF2F, ProofNet, and PutnamBench using three progressively expanded solver settings: a strong but expensive solver alone, adding a medium-cost solver with intermediate solving capability, and further adding a cheap solver with lower solving capability. BudgetPV requires less LLM generation computation than uniform allocation to solve the same number of subgoals across the evaluated settings. The experiments further show the computation savings obtained as medium- and lower-cost solvers are added.

</details>

### [Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning Using Executable Symbolic Representations](https://arxiv.org/abs/2611.27203)
*Yu-Bin Liu, Shi-Ju Ran* · `cs.LG` · arXiv:2611.27203v1 · relevance 0.15

- **In one sentence**: The paper introduces GSM-AB, a benchmark that separately varies operand digit length and operation count, and reports that executable symbolic representations (Lean, with a Python program-of-thought control) slow accuracy decline in LLM arithmetic reasoning compared with natural-language reasoning.
- **In plain words**: Large language models often score well on math tests, but that does not show whether they stay accurate when problems get harder. The authors built a controlled test where they could separately make numbers longer and make problems involve more steps. They report that having models write answers as runnable formal or code-based programs (Lean and Python) kept accuracy higher and made it fall more slowly than plain-language reasoning.
- **Why it matters**: Reliability on harder, multi-step calculations is a practical concern for using AI in math and science, so a method that makes accuracy degrade more gently is relevant. The text does not report how large the effects are or how broadly they hold beyond the tested models, so its significance should be treated as provisional.
- **Background needed**: - LLM: a large language model, an AI system trained on text that generates answers from patterns learned in data.
- Natural-language reasoning: the model writes out its steps in ordinary sentences.
- Executable symbolic representation: the model writes its reasoning as formal code or proof that a computer can run and check.
- Lean: a proof assistant language used to write machine-checkable mathematics.
- Program-of-thought (PoT): a method where the model writes a short program to compute the answer rather than doing the arithmetic in its head.
- Operand digit length: how many digits the numbers in a problem have.
- Operation count: how many calculation steps a problem requires.
- Accuracy scaling: how accuracy changes as problems get harder. · level: intermediate
- Matched keywords: Lean

<details><summary>Original abstract</summary>

High accuracy on mathematical benchmarks does not establish whether reasoning remains reliable as problem complexity increases. We examine how executable symbolic representations change accuracy scaling in large language models compared with natural-language reasoning. To address this limitation, we introduce the GSM Arithmetic Benchmark (GSM-AB), a controlled benchmark that independently varies operand digit length and operation count to probe numerical scale and compositional complexity. We find that executable representations can improve accuracy and slow its decline as complexity increases. Lean reduces average sensitivity to operand digit length at every tested model size. By contrast, slower degradation with increasing operation count emerges at the larger model sizes. A Python program-of-thought (Python-PoT) control shows a similar operation-axis pattern, suggesting that this finding is not specific to Lean. These findings show that reasoning representation shapes arithmetic accuracy scaling and support executable symbolic representations for more reliable reasoning on complex arithmetic tasks.

</details>

## Robotics and embodied AI

### [Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter](https://arxiv.org/abs/2611.27845)
*Songyang Liu, Yu Hou, Yuqing Hu et al.* · `cs.RO` · arXiv:2611.27845v1 · relevance 0.20

- **In one sentence**: A runtime safety filter that screens each operator command during VR teleoperation of a humanoid robot, using a head-camera scene model and a target-conditioned control barrier function quadratic program to keep the tool clear of a non-target electrical switch.
- **In plain words**: The paper looks at using humanoid robots to flip electrical switches so workers stay out of harm's way. The main risk is that a slightly imprecise remote command could make the robot's tool touch a neighbouring switch that should not be touched. The authors add a software filter that checks each command before it reaches the robot and adjusts only the unsafe ones, and they report it worked in ten real-robot trials on a Unitree G1 and in a simulation study.
- **Why it matters**: Electrical switching is a real safety hazard for people, so a way to let robots do it with fewer errors is worth watching. The text reports small-scale tests only, so it shows feasibility rather than readiness for field use.
- **Background needed**: - Humanoid robot: a human-shaped robot with arms, legs and a head camera.
- Teleoperation: a person controls the robot remotely, here through virtual reality.
- Scene model: a computer's estimate of where objects are, built from camera images.
- Control barrier function (CBF): a mathematical boundary that keeps a system inside a safe region.
- Quadratic program (QP): an optimisation step that finds the closest safe version of a command.
- Safety filter: a layer that passes safe commands unchanged and corrects unsafe ones.
- Simulation vs. real-world test: simulation is a computer model; real-world tests use the physical robot. · level: intermediate

<details><summary>Original abstract</summary>

Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch. This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of a humanoid robot. The filter integrates a scene model estimated from the robot head camera and a target-conditioned control barrier function quadratic program that keeps the tool away from the non-target switch while passing safe commands unchanged. In real-world experiments on a Unitree G1 humanoid robot, with six rounds at each of two standing positions, target operations succeed in all ten rounds with an unchanged target and no non-target actuation. A simulation study achieves 9/9 safe completions, compared with 5/9 for raw teleoperation, demonstrating the feasibility of the method for humanoid switching operations.

</details>

### [HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots](https://arxiv.org/abs/2611.27181)
*Jinlin Gan, Mingzhe Li, Junsheng Zhang et al.* · `cs.RO` · arXiv:2611.27181v1 · relevance 0.18

- **In one sentence**: HumanoidPose introduces the Humanoids benchmark and a monocular framework for recovering the 3D whole-body pose of humanoid robots from single camera images, using robot articulation modeling and explicit kinematic grounding.
- **In plain words**: Humanoid robots are becoming more common, and it is useful to know their full body posture from an ordinary camera image. Existing tools were built either for factory-style robot arms or for human bodies, so they fit humanoid robots poorly. This paper provides a benchmark with synthetic and hand-labeled training data, plus a method called HumanoidPose that is designed for humanoid bodies.
- **Why it matters**: Estimating a robot's posture from a camera, without extra sensors, could support monitoring, motion analysis, and robot learning. The text reports strong results on its own benchmark and on the DHRP-H1 benchmark, including zero-shot transfer to real-world data, but the abstract gives no comparison numbers, so its practical impact is not yet clear.
- **Background needed**: - Pose estimation: finding the positions and angles of a body's joints from an image.
- 2D vs 3D pose: 2D is joint locations in the picture; 3D adds depth and the true spatial arrangement of the joints.
- Monocular: using a single camera, with no depth sensor or stereo pair.
- Kinematics: the rules describing how connected links and joints move, such as limb lengths and joint angle limits.
- Synthetic data: computer-generated training images with known ground-truth poses.
- Zero-shot transfer: applying a model to new data it was not trained on, without extra tuning.
- Benchmark: a shared dataset and test protocol for fair comparison between methods. · level: intermediate

<details><summary>Original abstract</summary>

As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation (HPE), while not being fully addressed by either paradigm: RPE primarily focuses on non-humanoid robots, particularly fixed-base manipulators, whereas HPE is built upon human-specific skeletal topologies, body models, and motion priors. Despite recent progress in humanoid 2D keypoint detection and HPE adaptation, humanoid-native 3D pose recovery remains insufficiently studied, and a dedicated benchmark with suitable training data and evaluation protocols is still lacking. To address this gap, we introduce Humanoids, a benchmark for monocular 3D humanoid robot pose estimation, and propose HumanoidPose, a framework for this task. Humanoids provides synthetic 3D supervision across diverse humanoid embodiments, manually annotated real-world 2D data, and real-world RGB sequences paired with robot states for 3D evaluation on a physical Roban humanoid. HumanoidPose combines human-inspired visual perception with robot articulation modeling and explicit kinematic grounding. Experiments on Humanoids and the DHRP-H1 benchmark demonstrate strong performance in articulation recovery and 3D pose estimation, including zero-shot transfer to real-world 2D and 3D evaluation. Ablation studies further show the contribution of robot-native articulation modeling and explicit kinematic grounding. The dataset and code will be publicly released to support future research in the community.

</details>

## Security and cryptography

### [Post-Quantum Migration in Brownfield 5G Core Networks: Verified Hybrid Key Establishment, Performance, and Rollback](https://arxiv.org/abs/2611.27735)
*Shubham Verma* · `cs.CR` · arXiv:2611.27735v1 · relevance 0.11

- **In one sentence**: A deployment-controlled method for adding hybrid post-quantum/classical key establishment to an unmodified Open5GS AMF-NRF 5G Service-Based Interface via external boundary cryptographic entities, with packet-level verification, latency measurements, and rollback tests.
- **In plain words**: Phone networks use encryption to protect messages between their internal software components, and future quantum computers could eventually break some of the math that current encryption relies on. This paper looks at how an existing (brownfield) 5G core network can be upgraded to newer, quantum-resistant key exchange without changing the software of the network functions themselves, by routing traffic through external mediating units. In a lab test on one representative link, the authors found the new handshake worked and the network kept functioning, with a median registration delay rising from about 23 ms to about 26 ms, and they could switch back to the old setup.
- **Why it matters**: Operators running large networks cannot rebuild everything at once, so a way to add quantum-resistant encryption to deployed software without code changes is a practical question for the telecom security field. The results come from a single controlled testbed and one interface, so they say little yet about production networks or about the cost of the key exchange alone.
- **Background needed**: - 5G Core: the software that runs the central part of a mobile network, split into network functions (such as AMF and NRF) that talk over a Service-Based Interface (SBI).
- Open5GS: an open-source implementation of the 5G Core used for the experiments.
- TLS: the standard protocol that encrypts connections; it begins with a key-establishment handshake.
- Post-quantum cryptography (PQC): encryption designed to resist attacks from future quantum computers.
- Hybrid key establishment: combining a classical method (X25519) with a post-quantum one (ML-KEM-768, named X25519MLKEM768), so security holds if either one is unbroken.
- Brownfield: an existing, already-deployed system that must be changed gradually.
- Rollback: returning a system to its earlier working configuration.
- Median and confidence interval: the middle value of measurements, and a range that expresses the uncertainty in the estimated difference. · level: intermediate

<details><summary>Original abstract</summary>

Migrating brownfield 5G Core networks to post-quantum cryptography (PQC) is difficult because deployed network functions, base images, and TLS libraries evolve under different upgrade constraints. This paper evaluates a deployment-controlled migration strategy that enables hybrid post-quantum/traditional key establishment through externally deployed Boundary Cryptographic Execution Entities (BCEEs), without modifying participating network function source code. The approach is evaluated using the Open5GS AMF-NRF Service-Based Interface as a representative 5G Core scenario. Classical and hybrid configurations are compared under an unchanged mediation topology. Packet-level analysis confirms successful negotiation of X25519MLKEM768, and functional validation demonstrates that representative SBI procedures remain operational through the mediated path. In 120 NF-registration transactions, the median AMF-facing registration latency increased from 22.968 ms under the classical state to 26.351 ms under the hybrid state, reflecting a 3.383 ms (14.73 percent) increase, with a whole-block 95 percent confidence interval of [1.193, 7.872] ms. At the mediated TLS boundary, the hybrid configuration shows a 4.599 ms higher median segment-local TLS-establishment time than the classical configuration. These two reported differences reflect system-level runtime effects and do not isolate key-encapsulation cost. Packet evidence verifies rollback from hybrid-mediated operation to classical mediated operation and, separately, restoration of the native direct path. NF-facing compatibility legs remained plaintext and outside the hybrid post-quantum scope. The results demonstrate a packet-verifiable and manually reversible brownfield mechanism for introducing hybrid post-quantum key establishment on a controlled 5G SBI segment.

</details>

### [Enhancing Metaverse Security using Explainable AI-based Intrusion Detection Framework](https://arxiv.org/abs/2611.27199)
*Esha Kuppanda, Shalaka Mahadik, Pranav M. Pawar et al.* · `cs.CR` · arXiv:2611.27199v1 · relevance 0.08

- **In one sentence**: The paper compares machine learning models for intrusion detection in Internet-of-Things-linked metaverse environments across three benchmark datasets (ToN-IoT, CIC-IoT-2023, BoT-IoT), and uses SHAP and LIME explainability methods to identify influential features and justify the chosen model.
- **In plain words**: The paper looks at how to spot unauthorized access in the "Metaverse of Things," a setting where virtual worlds are linked to connected physical devices. The authors tested several machine learning models on three public security datasets and chose the best performers, reporting accuracy of 99.83% on ToN-IoT and 96.45% on CIC-IoT-2023 with XGBoost, and 99.99% on BoT-IoT with Random Forest and Extra Trees. They also used explanation tools to show which data features drove those decisions.
- **Why it matters**: Intrusion detection systems that are hard to interpret are harder for operators to trust and check, so pairing high accuracy with explanations speaks to a practical concern for connected devices and virtual platforms. The text does not show how these results hold up in real deployments, and the datasets are benchmarks, so real-world performance remains unclear.
- **Background needed**: - Intrusion detection system (IDS): software that watches network traffic and flags suspicious or malicious activity.
- Internet of Things (IoT): everyday devices (sensors, cameras, appliances) connected to the internet.
- Metaverse of Things: a concept linking virtual environments with IoT devices.
- Machine learning (ML): algorithms that learn patterns from example data to make predictions, here classifying traffic as normal or attack.
- Classifiers named in the text: XGBoost, Random Forest, and Extra Trees are common types of ML models.
- Explainable AI (XAI): methods that show why a model made a particular decision.
- SHAP and LIME: two popular XAI techniques that estimate how much each input feature contributed to a prediction.
- Accuracy and benchmark datasets: accuracy is the share of correct classifications; benchmark datasets are shared test collections used to compare methods. · level: intermediate

<details><summary>Original abstract</summary>

The MoT virtual environment, called the Metaverse of Things (MoT), combines machine learning (ML) and Internet of Things (IoT) to offer significant business opportunities in various sectors such as entertainment, healthcare, and education. In addition to its benefits, the MoT poses risks to privacy and security through unauthorized access, which threatens trustworthiness. While traditional intrusion detection systems (IDS) exist to handle this challenge, they struggle with high-dimensional data and poor interpretability. To address this challenge, the research conducted a thorough analysis of different ML models and proposed the optimal model to secure the MoT environment. The research employed explainable artificial intelligence (XAI) to identify the most effective features that contributed to optimal model selection. The research presented an optimal framework combining ML and XAI to safeguard MoT networks from the most recent cyberthreats. The research used three advanced benchmark security datasets: ToN-IoT, CIC-IoT-2023, and BoT-IoT, to examine the XAI-based intrusion detection framework. The XAI-based intrusion detection framework achieved 99.83% accuracy on ToN-IoT and 96.45% on CIC-IoT-2023 using the XGBoost model. On the BoT-IoT dataset, the Random Forest (RF) and Extra Trees (ET) classifiers reached 99.99% accuracy. The Shapley Additive Explanations (SHAP) and Local Interpretable Model-Agnostic Explanations (LIME) techniques used for XAI further enhanced feature relevance and user confidence in the optimal model.

</details>

## Algorithms and complexity

### [No Polynomial-Time Algorithm For Tarski Fixed Points Unless Cryptographic Assumptions Fail](https://arxiv.org/abs/2611.27977)
*Eleni Batziou, John Fearnley, Alexandros Hollender et al.* · `cs.CC` · arXiv:2611.27977v1 · relevance 0.24

- **In one sentence**: The paper gives a subexponential-time reduction from UEOPL to Tarski fixed-point finding, yielding conditional quasi-polynomial running-time lower bounds that match known query lower bounds.
- **In plain words**: The paper studies how fast a computer can find a "Tarski fixed point," a point that stays put when a rule that only ever pushes things in one consistent direction is applied to a grid of options. The authors show that solving this problem could be used to solve a different, known-hard search problem (UEOPL) with only a modest overhead. Their result is that, if certain cryptographic assumptions hold, no algorithm can solve Tarski fixed points in polynomial time.
- **Why it matters**: It moves the known query lower bounds for this problem to conditional running-time lower bounds, which is a stronger kind of hardness statement. The connection to cryptographic assumptions means the conclusion holds only if those assumptions are true, so it is a conditional result rather than an unconditional proof.
- **Background needed**: - Fixed point: an input that the rule maps back to itself.
- Tarski fixed point: the guaranteed fixed point of a monotone map on a lattice (an ordered grid), which exists by Tarski's theorem but may be hard to locate.
- Polynomial time vs. quasi-polynomial time: efficient algorithms grow polynomially with input size; quasi-polynomial time grows slightly faster but still far slower than exponential.
- Reduction: a way of showing one problem is at least as hard as another by converting instances of one into instances of the other.
- UEOPL (Unique End of Potential Line): a search problem in a class believed to be hard, used here as the source of hardness.
- Cryptographic lower bounds: results that rest on widely believed assumptions about the difficulty of breaking cryptographic primitives.
- Query lower bound: a limit on how many times an algorithm must query the input, as opposed to total running time. · level: research-level

<details><summary>Original abstract</summary>

We study the time complexity of finding a Tarski fixed point. We provide a subexponential-time reduction from the Unique End of Potential Line (UEOPL) problem to the problem of finding a Tarski fixed point. Using a range of known cryptographic lower bounds for UEOPL, our reduction implies a range of conditional lower bounds on the running time of any algorithm that finds a Tarski fixed point. The strongest of these give quasi-polynomial-time lower bounds for the problem. We also obtain a similar quasi-polynomial-time lower bound for Tarski based instead on a weak exponential-time type hypothesis for UEOPL. These running time lower bounds match the recently discovered quasi-polynomial query lower bounds for the problem.

</details>

### [Compiling Existential-Positive Queries to Bounded-Variable Fragments](https://arxiv.org/abs/2611.26869)
*Christoph Berkholz, Hubie Chen* · `cs.LO` · arXiv:2611.26869v1 · relevance 0.16

- **In one sentence**: The paper studies the formula-size cost of rewriting existential-positive first-order queries into the bounded-variable fragment of positive first-order logic, giving exponential upper bounds, polynomial bounds in some signature and variable regimes, and an unconditional exponential lower bound proved via circuit complexity.
- **In plain words**: Database-style queries can often be rewritten using fewer variable names, which makes them faster to evaluate. This paper asks what that rewriting costs: the rewritten query may become much longer. The authors show the growth in length is at most exponential, identify cases where it is only polynomial, and prove that in the remaining cases an exponential increase is unavoidable.
- **Why it matters**: The result gives a provable limit on a common preprocessing trade-off: fewer variables help evaluation, but the formula can grow sharply. The lower bound is described as the first unconditional one for this kind of compilation, and the circuit-complexity link is said to be of possible future interest; the text does not show further practical consequences.
- **Background needed**: - First-order logic: a formal language for statements about objects, using quantifiers such as "for all" and "there exists".
- Existential-positive queries: queries built only from "there exists", "and", "or" and atomic conditions, with no negation or "for all".
- Variable count: the number of distinct variable names a formula uses; bounded-variable fragments restrict this number.
- Polynomial vs. exponential: polynomial growth is manageable; exponential growth means length can blow up very quickly with input size.
- Formula size: the length or number of symbols in a formula, which the paper treats as the cost of rewriting.
- Circuit complexity: the study of how large Boolean circuits (networks of logic gates) must be to compute functions; used here to prove the lower bound.
- Unconditional lower bound: a proof that does not rely on an unproven assumption such as P not equal to NP. · level: research-level

<details><summary>Original abstract</summary>

A crucial property of bounded-variable fragments of first-order logic is that they can be evaluated in polynomial time. It is therefore a useful preprocessing step to rewrite, if possible, a first-order query to a logically equivalent one with a minimum number of variables. However, it may occur that reducing the number of variables causes an increase in formula size. We investigate this trade-off for the existential-positive fragment of first-order queries, where variable minimisation is decidable in general. In particular, we study the blow-up in the formula size when compiling existential-positive queries to the bounded variable fragment of positive first-order logic. While the increase of the formula size is always at most exponential, we identify situations (based on the signature and the number of variables) where only a polynomial blow-up is needed. In all other cases, we show that an exponential lower bound on the formula size of the compiled formula that matches the general upper bound. This exponential lower bound is unconditional, and is the first unconditional lower bound for formula size with respect to the studied compilation; it is proved via establishing a novel interface with circuit complexity which may be of future interest.

</details>

## Programming languages and formal methods

### [Perceived Differences in Activity and Experience Between Developing Software With and Without AI](https://arxiv.org/abs/2611.27947)
*Rubash Mali, Juho Leinonen, John Edwards* · `cs.SE` · arXiv:2611.27947v1 · relevance 0.20

- **In one sentence**: A study of how software engineers perceive their activities and experience differ when developing with generative AI tools versus traditional methods, and how those differences vary with years of programming experience.
- **In plain words**: This paper looks at how programmers feel their daily work has changed now that they use AI tools to write software. Based on what engineers report, they talk less with peers about technical problems, break work down less, search documentation less, and use debuggers less, while switching between tasks more and feeling less deep focus and less control over code and design. Core coding tasks like writing, refactoring, and fixing code show only small differences, and the changes are larger for engineers who started programming before generative AI existed.
- **Why it matters**: It matters for how the next generation of engineers is trained and whether experienced engineers will stay in the field and adapt. The text reports perceptions rather than measured performance, so it shows how people feel their work has changed, not whether the changes improve or harm software quality.
- **Background needed**: - Generative AI: software that produces text or code in response to prompts, such as coding assistants.
- Software engineering "craft" activities: decomposing problems (breaking them into smaller parts), searching documentation, debugging, and refactoring (reorganizing code without changing what it does).
- Self-reported survey data: the findings are based on what engineers say about their own work, not on direct observation.
- Experience gradient: a pattern where the size of an effect grows with years of experience. · level: introductory

<details><summary>Original abstract</summary>

The fundamental changes in software engineering driven by generative AI will have profound effects not only on the number of available software engineering jobs but also on what software engineering itself looks like. As the career evolves, questions arise about what the skillset and interests of the next generation of software engineers will be and whether long-time engineers will continue to be attracted to the career. In this paper, we contribute to answering these questions by studying how software development with AI tools is perceived to differ from traditional development and how the differences are modulated by years of programming experience. We find that, in terms of programming activities, engineers report less talking with peers about technical problems, less decomposition, less searching of documentation, and less using a debugger, while they report more task switching. We also find experiential differences, including less deep focus and less sense of control over code and design. We call these the different craft results, in contrast to core code-production activities such as writing, refactoring, and fixing code, which show only small mean differences. We also find that these differences are amplified by years of programming experience (an experience gradient), with software engineers who started programming before the age of generative AI perceiving greater changes in both activity and developer experience. We discuss our findings and their implications on training of the next generation of engineers and on engineers who may have difficulty transitioning to the AI-infused world of software engineering.

</details>

### [Compositional Temporal Specifications for Interaction Trees](https://arxiv.org/abs/2611.27553)
*Linyu Yang, Jianwei Yin, Mingshuai Chen* · `cs.PL` · arXiv:2611.27553v1 · relevance 0.07

- **In one sentence**: The paper introduces iBuchi, a shallowly embedded temporal specification language over Choice Trees for reasoning about the ordering of observable interactions in Interaction Trees, with trace- and tree-level satisfaction relations, compositional principles, and integration into the Dijkstra Monads Forever framework, all mechanized in Rocq.
- **In plain words**: Programs often interact with their surroundings over time, such as reading input, writing output, or making requests, and the order of those interactions matters as much as the final answer. This paper gives a way to write down rules about the timing and order of such interactions and to check that a program follows them. The authors built the framework in the Rocq proof assistant and tested it on several non-trivial examples.
- **Why it matters**: Being able to state and verify how a program behaves over time, in modular pieces, matters for software that runs continuously or reacts to its environment. The text does not claim wider impact, so its practical reach beyond the Interaction Trees and Rocq setting is unclear from this summary alone.
- **Background needed**: - Formal verification: proving mathematically that a program meets a specification.
- Interaction Trees: a data structure that represents a program's effects as a tree of possible interactions with its environment, possibly infinite.
- Temporal properties: statements about how behaviour unfolds over time, such as "a response always eventually follows a request."
- Linear Temporal Logic (LTL): a notation for such time-based statements, with operators like "always" and "eventually."
- Hoare-style specifications: pre- and post-condition statements about what a program does.
- Rocq (formerly Coq): a proof assistant used to write and machine-check proofs.
- Shallow embedding: encoding a specification language directly within the host language rather than as a separate syntax tree. · level: research-level

<details><summary>Original abstract</summary>

The correctness of modern effectful programs depends not only on their final results but also on the temporal evolution of observable interactions with their environments. Interaction Trees (ITrees) provide a reusable denotational semantics for such programs by representing effectful computations as potentially infinite trees of observable interactions. However, reusable temporal reasoning over ITrees remains largely unexplored. This paper presents a compositional temporal specification framework for ITrees. We introduce iBuchi, a shallowly embedded temporal specification language based on Choice Trees, which represents finite and infinite interaction traces and supports expressive temporal operators, including sequencing, branching, conjunction, repetition, and Linear Temporal Logic modalities. We define trace- and tree-level satisfaction relations between iBuchi specifications and ITrees, together with compositional reasoning principles for modular verification of effectful programs. We integrate iBuchi into the Dijkstra Monads Forever framework, thereby enabling temporal specifications to compose with conventional Hoare-style specifications and supporting a generator-based encoding of future conditions. We have formally developed and verified our framework in Rocq and demonstrated its expressiveness and compositionality through several non-trivial case studies.

</details>

## Systems and networking

### [Bring Cloud-Native Networking to FreeBSD Jails: Porting Calico from Linux](https://arxiv.org/abs/2611.27320)
*Soma Sakaguchi, Shintaro Suzuki, Yuki Nakata et al.* · `cs.OS` · arXiv:2611.27320v1 · relevance 0.13

- **In one sentence**: The paper describes porting Calico, a widely used Kubernetes-style container networking plugin, to FreeBSD Jails by swapping Linux networking components for FreeBSD equivalents (ipfw for iptables, routing sockets for netlink, vnet for network namespaces).
- **In plain words**: Software that runs many isolated programs on one computer, called containers, needs a way to connect them to networks and set rules about who can talk to whom. On Linux, a popular tool called Calico does this, but FreeBSD (an operating system with its own style of containers called Jails) lacked an equivalent, so users set things up by hand. This paper describes adapting Calico to run on FreeBSD by replacing Linux-only pieces with FreeBSD's own built-in tools.
- **Why it matters**: It aims to let FreeBSD work with the same container orchestration systems that Linux users rely on, which could matter for anyone running FreeBSD servers at scale. The text is a short abstract only, so it does not report measured results, and how complete or well-tested the port is cannot be judged from it.
- **Background needed**: - Container: a way to run an isolated program with its own view of files and network, sharing the host's operating system.
- FreeBSD Jails: FreeBSD's built-in container-like isolation.
- CNI (Container Network Interface) plugin: a standard add-on that handles networking for containers in orchestration systems such as Kubernetes.
- Calico: a widely used networking plugin that also enforces rules about which containers may communicate.
- iptables / ipfw: packet-filtering rule systems on Linux and FreeBSD respectively.
- Netlink / routing sockets: the interfaces programs use to query and change network settings in the kernel.
- Network namespace / vnet: a way to give each container its own separate network stack. · level: intermediate

<details><summary>Original abstract</summary>

While Linux containers benefit from a rich ecosystem of Container Network Interface (CNI) plugins such as Calico and Cilium, FreeBSD Jails lacked native, standardized solutions for advanced networking. As a result, users have relied on manual, error-prone configurations, limiting scalability and integration with modern orchestration platforms. This paper introduces porting Calico, a widely adopted CNI plugin, to the FreeBSD operating system. Our approach replaced Linux-specific components with FreeBSD-native equivalents: iptables with ipfw, netlink sockets with routing sockets, and Linux network namespaces with FreeBSD's vnet. This work aims to bridge the gap between Linux and BSD container networking. By providing scalable, policy-driven capabilities that are compatible with existing Linux-centric infrastructure, FreeBSD can participate more fully in the broader container networking ecosystem.

</details>

### [Contention-Aware Flexible Execution for Machine Learning Workloads](https://arxiv.org/abs/2611.26840)
*Marco Kurzynski, Shaizeen Aga, Di Wu* · `cs.DC` · arXiv:2611.26840v1 · relevance 0.12

- **In one sentence**: A characterization of how concurrently running GPU kernels slow each other down on AMD MI300X hardware, followed by CAFEML, a contention-aware scheduler that tunes operator overlap and resource allocation for ML training and inference, reporting up to 13% end-to-end speedup without kernel rewrites.
- **In plain words**: Modern AI software runs many small computing tasks (called kernels) at the same time on a graphics processor, and they compete for shared parts of the chip such as memory and cache, so each can run slower. This paper measures how much that slowdown happens on a current datacenter AI chip, and sorts the results by whether a task is limited by memory or by computation, and whether it is large or small. It then proposes simple scheduling rules for when to start overlapping tasks and how to split chip resources between them.
- **Why it matters**: Keeping expensive AI accelerators busy is a practical concern for anyone running large models, and the paper suggests that the default "start whatever is ready first" policy used by frameworks leaves performance on the table. The gain reported (up to 13% end-to-end) comes from scheduling changes alone, which is a modest but practically relevant result; the text does not show how well it generalizes beyond the scenarios tested.
- **Background needed**: - GPU (graphics processing unit): a chip with many parallel cores, widely used to train and run AI models.
- Kernel: a single compute job launched on a GPU, such as one matrix multiplication.
- Concurrent execution: running several kernels at once so the chip is used more fully.
- Contention: competition for shared resources like cache and memory bandwidth, which slows each job.
- Memory-bound vs. compute-bound: whether a job is limited by how fast data moves or by how fast arithmetic can be done.
- Training vs. inference (prefill and decode): training updates a model; inference uses it to generate output, with prefill and decode being its two phases.
- End-to-end speedup: the improvement in total run time for a whole workload, not just one piece. · level: research-level

<details><summary>Original abstract</summary>

Concurrent kernel execution is a ubiquitous paradigm in artificial intelligence (AI) and machine learning (ML) across both training and inference. That said, concurrency causes potential slowdown as concurrent kernels contend for limited GPU resources (cores, caches, memory bandwidth), which are shared between these kernels rather than exclusively available to one, as in isolated execution. This raises an important research question: to what extent does concurrency slow down kernel execution and how can it be mitigated. To answer this question, our work presents two studies. First, we characterize concurrent kernel execution extensively for the first time, to our knowledge. We conduct not just performance analysis of concurrent kernels but also memory behavior under concurrency on state-of-the-art AMD Instinct MI300X GPUs designed for datacenter AI, using the AMD-internal millisecond sampler. Based on the observations, we share insights on the slowdown along two dimensions (memory vs. compute bound, large vs. small kernels) to inform future optimizations. Second, we put the derived insights to use, aiming to deliver higher performance via targeted, flexible overlap of ML operators. Frameworks today make the simple decision of early-first for concurrent kernels, which is suboptimal. Noticing the opportunity that ML dataflow has inherent flexibility in which operators can be overlapped and how hardware resources can be allocated, we deduce simple heuristics to tune both overlap anchors and resource allocation for concurrent kernels to improve performance. We evaluate our proposed contention-aware flexible execution (termed CAFEML) across a variety of ML scenarios (inference decode, inference prefill, training) and demonstrate a speedup of up to 13% end-to-end with simple scheduling changes and no kernel rewrites.

</details>

## Human-computer interaction

### [AROMA: Understanding AI Support For Mental Well-being through Role Theory](https://arxiv.org/abs/2611.26843)
*Issac Ting, Ethan Pan, Koustuv Saha et al.* · `cs.HC` · arXiv:2611.26843v1 · relevance 0.05

- **In one sentence**: The paper proposes AROMA, a role-oriented framework that annotates over 7,515 conversations from 13 datasets to derive eight observed "Role States" for AI mental well-being supporters, and uses them to analyze support contexts, structural and temporal differences from humans, and a prompting strategy for better role alignment.
- **In plain words**: AI chatbots that offer emotional support sometimes act outside the role they were meant to play, and this can hurt the relationship with the user. Standard tests only check whether such bots work in narrow tasks, so they miss why these mismatches happen. The authors labeled thousands of real conversations from 13 datasets by the roles the speakers actually took, and identified eight recurring role patterns.
- **Why it matters**: The work offers a shared vocabulary for describing when and how AI supporters drift from their intended role, which may help explain failures that task-based evaluations overlook. The text does not report how much the proposed prompting strategy improves outcomes, so its practical impact is unclear from the abstract alone.
- **Background needed**: - Role theory: a social-science idea that people behave according to expected parts in a relationship, such as counselor or friend.
- Relational harm: damage to trust or the relationship when one party behaves in unexpected ways.
- Annotation: human labeling of data (here, conversation turns) to create a coded dataset.
- Role States: the paper's term for eight behavior categories inferred from what speakers actually did, not from what they were told to do.
- Prompting strategy: instructions written to steer a language model's behavior.
- Structural and temporal characteristics: how conversation turns are organized and how roles shift over the course of a conversation. · level: intermediate

<details><summary>Original abstract</summary>

AI supporters for mental well-being are becoming more prevalent. When these AI supporters start acting in ways beyond their expected function it leads to relational harm. Standard approaches to evaluating such AI supporters are limited to inspecting their efficacy in narrow task-specific settings, which do not explain these discrepancies in expected and actual behavior. To address this gap, we propose the AROMA (A Role-Oriented Model of Analysis) framework to provide a common role taxonomy for different support contexts. We developed AROMA using a theory-informed annotation of over 7,515 conversations from 13 datasets and propose eight "Role States" based on observed-not prescribed-behavior. We show these Role States vary according to the context of support; depict unique structural and temporal characteristics of AI supporters vis-a-vis Humans; and inform novel AI support prompting strategy for better role alignment. This framework provides a new lens to understand AI support failures.

</details>

### [A Frugal AI Framework for India: Responsible and Right-sized AI](https://arxiv.org/abs/2611.27189)
*Balaraman Ravindran, K. S. Venkataraghavan, Gokul S Krishnan et al.* · `cs.CY` · arXiv:2611.27189v1 · relevance 0.04

- **In one sentence**: A CeRAI (IIT Madras) white paper proposing "Responsible Frugal AI" as a right-sized, resource-conscious policy and engineering framework for deploying AI at population scale in India, with seven levers, a seven-point checklist and eleven policy statements.
- **In plain words**: This white paper argues that India should not try to copy the huge, expensive AI models built in the US or China, nor simply use foreign AI with local tweaks. Instead it proposes a third approach: use the smallest AI system that does the job well enough, with careful checks, human oversight for serious decisions, and limits on total resource use. The authors frame this as a policy and design guide rather than a set of experimental results.
- **Why it matters**: India must serve a very large and varied population under tight budgets and uneven infrastructure, so a cost-aware approach to AI is a practical question for public services. The text is a position paper with a framework and checklist; it does not report measured outcomes, so its practical effect is untested from this text alone.
- **Background needed**: - Foundation model: a very large AI model trained on huge datasets, costly in computing power and money.
- Compute: the processing power (and electricity) needed to train or run AI.
- Responsible AI: designing AI to be fair, safe, transparent and accountable.
- Digital public infrastructure: shared government-built digital systems (such as identity or payment platforms) that others can build on.
- Sovereignty: a country's ability to control, inspect and adapt the technology it relies on.
- Vernacular-first: designing for local languages before English.
- Right-sized model: the smallest model that meets a defined requirement with a safety margin. · level: introductory

<details><summary>Original abstract</summary>

India's AI debate often swings between two insufficient options: replicating the compute-intensive, capital-heavy foundation-model programmes of the United States or China, or remaining a downstream adopter of foreign AI with localised interfaces and safeguards. Neither serves a country that must deliver AI to a very large, diverse population across uneven infrastructure and within constrained budgets. This white paper from the Centre for Responsible AI (CeRAI), IIT Madras, proposes a third path: Responsible Frugal AI, which applies principle-based frugal engineering alongside Responsible AI. Responsible Frugal AI is right-sized AI: it fixes the functional requirement first, asks whether AI is needed at all, and then chooses the smallest sufficient model, meeting the requirement with minimal resources while keeping a verified margin, robustness and responsible governance. The framework applies frugality across four dimensions (data, compute, model and operations) through seven levers spanning the AI lifecycle, each with practices and measures. It calls for public AI rails, vernacular-first design, measured resource use, human oversight for high-stakes decisions, and a cap on total resource consumption so that efficiency gains are not cancelled out by rising usage. We argue that India is resource-imbalanced rather than resource-poor, and that frugal principles offer the most viable route to population-scale deployment, fit naturally with India's digital public infrastructure, and make sovereignty operational by preserving India's capacity to specify, deploy, govern, inspect and adapt its AI systems. A seven-point adoption checklist and eleven policy statements translate the framework into practice, positioning AI in India as a responsible, frugal public-value system that maximises social value per rupee and per joule.

</details>

## Information theory

### [Coding Length and Optimal Power Allocation in Correlated Block Fading](https://arxiv.org/abs/2611.27694)
*Haoran Xu, Huazhong Zhao* · `cs.IT` · arXiv:2611.27694v1 · relevance 0.06

- **In one sentence**: For a Gaussian block-fading channel with correlated fades, the paper studies when outage probability predicts the achievable rate under an exponential error-exponent requirement with many receive antennas, and it characterizes the optimal power allocation across blocks.
- **In plain words**: The paper looks at how to send a message reliably over a wireless link where signal strength varies in blocks of time that are correlated with each other. The transmitter knows only the statistical pattern of the fading, not the actual values, and the receiver has many antennas. The authors find when the simple "outage" measure (the chance the link is too weak to support a rate) correctly predicts the best rate, and when it overestimates it.
- **Why it matters**: It sharpens when a standard engineering shortcut for wireless links, outage, is accurate, and it gives explicit examples where power should be left off a block and then used again as reliability demands tighten. The text does not indicate links to specific applications beyond wireless communication.
- **Background needed**: - Block fading: the channel gain stays fixed within a block and changes between blocks.
- Outage: the event that the channel is too weak to support a chosen rate; outage probability is its chance.
- Error exponent: how fast the chance of decoding error shrinks as a parameter (here, the number of receive antennas) grows.
- Dispersion: a measure of how much the achievable rate fluctuates around the capacity for finite-length codes.
- Power allocation: how a fixed total energy is split across the blocks of a codeword.
- Autoregressive (AR(1)) fading: a model where each block's gain is correlated with the previous one. · level: research-level

<details><summary>Original abstract</summary>

A codeword spans a fixed number of correlated Gaussian fading blocks. The receiver knows the gains and the transmitter knows only their law. At fixed average signal-to-noise ratio, we require the decoding error probability to decay exponentially with the number of receive antennas. When does outage predict the achievable rate? If block length grows faster than the number of antennas, outage gives the limiting optimal rate. If both grow to infinity at a fixed positive ratio of block length to array size, outage strictly overestimates the limiting rate. We determine the critical ratio above which positive rates are possible. For sufficiently large finite ratios, we find the exact limiting rate over all codes satisfying a total energy constraint on each codeword. The leading rate loss is inversely proportional to the ratio. Its coefficient depends on Gaussian channel dispersion at the most likely fade causing outage and on how quickly the outage rate decreases as the required error exponent increases. In the long-block limit, equal power loses rate on every window of three or more blocks under stationary first-order autoregressive fading with positive lag-one correlation. In a different three-block channel with identical marginal gains, tightening the reliability requirement first makes it optimal to leave the middle block unused and later to use it again.

</details>

### [$L^1$ stability of the entropy power inequality in $\mathbb{R}^d$ without moment assumptions](https://arxiv.org/abs/2611.27790)
*Norman El Fartass, Lampros Gavalakis, Ioannis Kontoyiannis* · `cs.IT` · arXiv:2611.27790v1 · relevance 0.04

- **In one sentence**: The paper proves qualitative stability of Shannon's entropy power inequality in R^d in L^1 and Ruzsa distance without any moment assumptions, using an optimal transport argument, majorization of density rearrangements, and Christ's stability result for sharp Young's inequality.
- **In plain words**: The paper studies a basic inequality from information theory that bounds how the uncertainty (entropy) of a sum of independent random quantities relates to that of the parts. It asks what happens when that inequality is nearly tight, and shows the near-equality stays close in a precise sense, without requiring the random quantities to have finite moments (a technical condition on how spread out they can be). The authors also extend several earlier one-dimensional results to random vectors of any dimension.</plain>
<parameter name="why">Stability results say that near-optimal cases must look close to the extremal ones, which matters for proofs and for understanding when the bound is sharp. The text does not describe applications beyond this mathematical setting, so any wider connections are unclear from the abstract alone.
- **Background needed**: - Differential entropy: a measure of spread or uncertainty for a continuous random vector, with a density function.
- Entropy power inequality: a bound saying the entropy power of a sum of independent random vectors is at least the sum of their entropy powers; equality holds for Gaussians.
- Stability: if the inequality is almost an equality, the distributions are close to Gaussian-type extremizers in some measured distance.
- L^1 distance: the total amount by which two probability densities differ, integrated over space.
- Ruzsa distance: a distance between random variables that is used in additive combinatorics and probability.
- Optimal transport: a way of moving one probability distribution into another at minimal cost, used here as a proof tool.
- Young's inequality: a sharp inequality on convolutions of functions; its sharp form has known extremizers (Gaussians).
- Moment assumptions: conditions that random variables have finite averages of powers of their size; the paper removes these. · level: research-level

<details><summary>Original abstract</summary>

We establish qualitative stability in $L^1$ and Ruzsa distance for Shannon's entropy power inequality in $\mathbb{R}^d$, without any moment assumptions. The proof uses the optimal transport argument by Rioul (2017), majorization bounds of density rearrangements, and the stability of the sharp form of Young's inequality due to Christ (2019). Along the way we also extend recent one-dimensional results on de Bruijn's identity, the continuity of differential entropy, and the equality case of the entropy power inequality to random vectors of any dimension.

</details>

## High-energy theory and gravity

### [Type-II quasinormal modes of dilaton--Euler--Heisenberg AdS black holes](https://arxiv.org/abs/2611.27195)
*Chao-Ming Zhang, Fu-Wen Shu, Yun Soo Myung et al.* · `gr-qc` · arXiv:2611.27195v1 · relevance 0.20

- **In one sentence**: Computes Type-II quasinormal modes (coupled gravitational, dilaton and electromagnetic perturbations for ℓ=0,1,2) of a magnetically charged dilaton–Euler–Heisenberg black hole in AdS, using direct integration and Chebyshev pseudospectral methods, and links the ℓ=0 dilaton modes to the black hole's thermodynamic phase transition.</one_liner>
<parameter name="plain">The paper studies how a charged black hole in a curved, AdS-type universe "rings" after being disturbed, the way a struck bell rings at certain tones that fade over time. It looks at several coupled kinds of disturbance (gravity, a scalar "dilaton" field, and electromagnetism) and computes the tones and fading rates numerically. It reports that the black hole appears stable, since all modes it computes decay, and that the fading rate shows a change near the black hole's thermodynamic phase transition.
- **Why it matters**: Quasinormal modes are the characteristic signals a black hole emits when perturbed, so they are a theoretical handle on black-hole stability and on how such objects might be probed. The link drawn between these modes and a thermodynamic phase transition is the most unusual part; the text does not say how directly this could be tested, so the broader significance is uncertain.
- **Background needed**: - A black hole's quasinormal modes are damped oscillations with a real frequency (pitch) and an imaginary part (how fast they fade); negative imaginary part means stability.
- AdS (anti-de Sitter) is a universe with negative curvature that acts like a box confining signals.
- The dilaton is a hypothetical scalar field coupled to electromagnetism, appearing in some string-inspired gravity theories.
- Euler–Heisenberg corrections are nonlinear modifications to electromagnetism at strong fields, from quantum vacuum effects.
- ℓ is the angular-momentum label of a mode: ℓ=0 monopole, ℓ=1 dipole, ℓ=2 quadrupole.
- Chebyshev pseudospectral methods are numerical techniques for solving the governing equations accurately.
- A thermodynamic phase transition is a qualitative change in a system's state (like water boiling); here it is studied in the black hole's isobaric (constant-pressure) process. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we investigate Type-II quasinormal modes (QNMs) of a magnetically charged dilaton--Euler--Heisenberg black hole in anti-de Sitter (AdS) spacetime. The Type-II includes coupled gravitational, dilaton and electromagnetic perturbations. Its coupled equations are derived for $\ell=0,1,2$ modes and the QNM frequencies are calculated by employing direct integration and Chebyshev pseudospectral methods, giving consistent results. For nondegenerate dipole ($\ell=1$) mode at fixed curvature, the nonlinear correction starts at order $Q^2$ for electromagnetic-led branch and at order $Q^4$ for scalar-led branch. In this case, stronger AdS curvature enhances reduction of the electromagnetic-led real frequency for positive coupling, while gravitational-led quadrupole real frequency changes weakly with charge. As the curvature weakens, the dipole frequencies approach the AdS normal-mode scale and their damping decreases. We find that all modes computed have negative imaginary parts for nonextremal black holes, implying this black hole is stable against Type-II perturbations. Furthermore, we explore the connection between thermodynamic phase transition and QNMs for $\ell=0$ dilaton. For a subcritical isobaric process, the QNM real frequency of $\ell=0$ dilaton decreases with increasing temperature of small black holes, while it increases with increasing temperature of large black holes. At coexistence, the damping rate for large black holes is about 4.28 times that for small black holes.

</details>

### [Onset of quantum chaos in a family of two-dimensional conformal field theories](https://arxiv.org/abs/2611.26694)
*Felix M. Haehl, Moshe Rozali* · `hep-th` · arXiv:2611.26694v1 · relevance 0.16

- **In one sentence**: In a family of two-dimensional K3 sigma models near the Kummer orbifold point, the first-order splitting of degenerate non-BPS spin-zero operator dimensions along generic blow-up deformation directions follows GOE random-matrix statistics once exact symmetries are resolved, unlike the singlet deformation.
- **In plain words**: This paper studies a quantum field theory on a two-dimensional surface, a sort of idealized model of string theory on a special shape called K3. At a special point the energy levels of certain particle-like states sit exactly on top of one another. The authors nudge the model in small directions and measure how these tied levels split apart, and find that the pattern of splittings looks statistically like the random-matrix patterns seen in complicated physical systems.
- **Why it matters**: Random-matrix statistics are a sign of quantum chaos, and finding them in a solvable conformal field theory is a question of interest for how chaos arises in quantum gravity-related models. The text supports the comparison with the singlet deformation, but whether this connects to broader holographic or gravitational questions is not established by the abstract alone.
- **Background needed**: - Conformal field theory (CFT): a quantum theory on a 2D surface that is scale-invariant; its states have "scaling dimensions," which act like energy levels.
- Sigma model with K3 target space: a 2D theory whose fields live on the K3 surface, a special four-dimensional shape from geometry.
- Supersymmetry (N=(4,4)): an extra symmetry relating bosons and fermions.
- Orbifold: a space made by quotienting a simpler space (here a torus) by a symmetry; the Kummer point is one such special point.
- BPS operators: protected states whose energies do not change under deformation; non-BPS ones can shift.
- Marginal deformation: a small change to the theory that does not change its scale-invariance at leading order.
- Degenerate levels and first-order splitting: several states with equal energy that separate under a small perturbation; the size of the separation at leading order is what is measured.
- Random matrix theory and GOE: statistics of eigenvalues of random symmetric matrices, used as the benchmark for chaotic quantum systems; diagnostics include gap ratios and rigidity. · level: research-level

<details><summary>Original abstract</summary>

We exhibit random matrix statistics in the scaling dimensions of non-BPS primary operators in a family of two-dimensional conformal field theories. Specifically, we consider the sigma model with K3 target space and $\mathcal N=(4,4)$ supersymmetry in a neighborhood of the Kummer orbifold point $\mathbb T^4/\mathbb Z_2$. At the free-fermion radius, the spin-zero spectrum of the $\mathbb Z_2^4$-invariant sector is exactly degenerate at integer energies. The exactly marginal blow-up deformations that preserve this symmetry form a four-dimensional space, whose directions we parametrize by unit quaternions. Along each deformation direction, we compute the first-order splitting of the degenerate levels, i.e., the leading anomalous dimensions as the coupling goes to zero. In sectors where all exact symmetries are resolved, including a hidden $\mathbb Z_2$ at the even levels, the non-zero first-order shifts along a generic direction follow the Gaussian orthogonal ensemble (GOE), as we verify by computing several spectral diagnostics. We compare quantitatively with the well-known singlet deformation, which has enhanced symmetry: even after all its known symmetries are resolved, its first-order spectrum has exact degeneracies, its gap ratio approaches the GOE value only slowly as the energy increases, and its unfolded spectrum lacks the long-range rigidity of the GOE.

</details>

## Statistical physics

### [Large deviations, effective dynamics, and dynamical phase transitions in random maps](https://arxiv.org/abs/2611.26704)
*\'Angela Tajuelo-Valbuena, Jorge Hidalgo, Ricardo Guti\'errez et al.* · `cond-mat.stat-mech` · arXiv:2611.26704v1 · relevance 0.20

- **In one sentence**: The paper extends the Doob transform and spectral large-deviation methods from deterministic chaotic maps to random maps, to build effective dynamics for rare trajectories and to characterize dynamical phase transitions.
- **In plain words**: The paper studies unusual, rare patterns of behavior over long stretches of time in simple systems that evolve in discrete steps with added randomness. Such patterns are exponentially hard to observe by just running the system normally. The authors show how to build a modified version of the dynamics in which these rare behaviors become typical, so they can be reproduced directly, and they use spectral methods to see when the system switches between different behavioral regimes.
- **Why it matters**: Rare fluctuations and sudden switches between behavioral regimes are central questions in statistical physics, and the framework could help study them in a wider class of systems. The text itself does not indicate specific applications beyond random chaotic maps, so the broader reach is unclear from this abstract alone.
- **Background needed**: - Random maps: systems that update in discrete time steps, with each step including some randomness.
- Large deviation theory: the mathematics of how improbable averages over time behave, typically with probabilities decaying exponentially.
- Time-averaged observable: a quantity averaged over a long trajectory, such as how often a state is visited.
- Doob transform: a reweighting of a random process that changes its probabilities so that a chosen rare event becomes the likely outcome.
- Tilted operator: a modified transfer operator whose leading eigenvalue and eigenfunctions encode the rate of rare events.
- Dynamical phase transition: an abrupt change in the typical behavior of a trajectory as a control parameter (here, the size of the deviation being studied) varies. · level: research-level

<details><summary>Original abstract</summary>

Large deviation theory provides a natural framework to characterize rare fluctuations of time-averaged observables in deterministic and stochastic systems. Building on previous results for deterministic chaotic maps, here we extend the Doob transform to random maps, constructing an effective dynamics in which rare events become typical. This makes it possible to directly reproduce the dynamics of rare trajectories that are exponentially difficult to sample under the original dynamics. We further apply spectral large-deviation methods to characterize dynamical phase transitions in random maps. The spectral structure of the tilted operator provides insight into the mechanisms underlying these transitions and, in particular, allows us to identify the appropriate initial states that select one dynamical phase or another. Our results extend the connection between large deviation theory, spectral methods, and effective dynamics to random chaotic maps, providing a general framework to study rare events and dynamical phase transitions in these systems.

</details>

### [Cup and Cap Topological Neural Network](https://arxiv.org/abs/2610.03169)
*Marta Niedostatek, Ferran Hernandez Caralt, Runyue Wang et al.* · `cond-mat.dis-nn` · arXiv:2610.03169v2 · relevance 0.15

- **In one sentence**: The paper proposes the Cup and Cap Topological Neural Network (CCNN), which uses cup and cap products from algebraic topology to move signals between simplices of different dimensions in one layer and learns node-level features via many-body (e.g. triangle) interactions, validated on TopoBench datasets against other simplicial complex networks.
- **In plain words**: Many machine-learning models built on shapes or networks of connected parts can only pass information between neighbouring levels of structure, such as points to lines or lines to triangles, one level at a time. This paper proposes a new model that uses mathematical operations called "cup" and "cap" products, which let information jump across more than one level in a single step. The authors test it on standard benchmark datasets and report that it performs competitively with other existing models of this kind.
- **Why it matters**: The work targets a stated limitation of current topological deep learning, namely that signals can only be raised or lowered one dimension per layer, so it may matter for modelling group interactions in data. The text reports only competitive benchmark performance, not superiority, so the practical gain is unclear from this abstract alone.
- **Background needed**: - Simplices: building blocks of a shape or network: points (dimension 0), edges (1), triangles (2), and higher.
- Simplicial complex: a collection of such blocks glued together; it can represent group interactions, not just pairwise links.
- Cochain: an assignment of numbers (features) to the blocks of a given dimension; node-based variables are 0-cochains.
- Boundary operators and Hodge Laplacians: standard tools that move information between neighbouring dimensions of a complex.
- Cup and cap products: operations from algebraic topology that combine features across dimensions, allowing jumps of more than one dimension.
- TopoBench: a benchmark suite for topological neural networks. · level: research-level

<details><summary>Original abstract</summary>

Topological Deep Learning (TDL) is designed to learn features associated not only with nodes but also with edges, triangles and higher dimensional simplices. However, most TDL approaches, being based on boundary operators and Hodge Laplacians, have the limitation that features and signals cannot be lifted or lowered across more than one dimension per layer. To overcome this limitation, in this work, we propose the adoption of the cup and cap products. Specifically, we formulate the Cup and Cap Topological Neural Network (CCNN), a topological deep learning architecture designed to learn node-based variables (or 0-cochains) by taking into account their many-body interactions (e.g. triangles) present in the data. We validate CCNN by assessing its performance on the TopoBench datasets, demonstrating its competitive performance with respect to other simplicial complex neural networks.

</details>

## Condensed matter

### [Topological phases protected by half-chiral symmetry](https://arxiv.org/abs/2611.26693)
*Chen-Shen Lee, Itamar Kimchi* · `cond-mat.mes-hall` · arXiv:2611.26693v1 · relevance 0.21

- **In one sentence**: The paper proposes topological phases protected by "half-chiral" symmetry, where the sublattice (chiral) symmetry holds on only one sublattice, and builds a real-space invariant framework with a 2D Kekulé honeycomb model showing higher-order corner modes.
- **In plain words**: Some materials have atoms arranged on two interlocking sublattices, and a special symmetry normally pins down their edge behavior. This paper looks at the case where that symmetry holds on only one of the two sublattices, which can happen when the sublattices are unequal or when orbitals are localized. The authors describe a new way to classify such systems and show, in a two-dimensional model, that a single zero-energy state can be stuck to one corner.
- **Why it matters**: It extends the well-known idea of topology protected by sublattice symmetry to a weaker, algebraic constraint that group-theory methods do not cover, which may matter for materials like graphene on hexagonal boron nitride. The text does not report experiments or quantify practical impact, so its wider significance is uncertain.
- **Background needed**: - Topological phase: a property of a material's electronic structure that stays the same under smooth changes, often producing protected edge or corner states.
- Sublattice (chiral) symmetry: in a lattice split into two interleaved sets of sites, hopping only between the sets; this makes zero-energy edge states robust.
- Su-Schrieffer-Heeger (SSH) chain: a simple one-dimensional model of such a chain, a standard example.
- Hamiltonian: the matrix describing a system's energies and how particles hop between sites.
- Projection P: a mathematical operator that selects the states on one sublattice; the constraint PHP=0 means no direct hopping within that sublattice.
- Higher-order topology: edge states that appear at corners or hinges rather than along full edges.
- Graphene and hexagonal boron nitride (hBN): atomically thin honeycomb-lattice materials; Kekulé distortion is a pattern that changes hopping strengths on the honeycomb. · level: research-level

<details><summary>Original abstract</summary>

Chiral (or sublattice) symmetry describes bipartite systems such as the Su-Schrieffer-Heeger (SSH) chain where same-sublattice A-A and B-B hoppings are forbidden, enabling the protection of topological phases. Here we identify new topological phases protected by half-chiral symmetry wherein chiral symmetry is preserved on only one sublattice, as may occur with sublattice imbalance (e.g. graphene-hBN) or localized orbitals (e.g. zincblende). Unlike conventional symmetry operators described by group theory, half-chiral symmetry is an algebraic constraint on the sublattice-projected Hamiltonian such as $PHP=0$, requiring a new framework for topological protection. We develop such a framework, identifying real-space bulk topological invariants and corresponding topological boundary modes that stick to zero energy. In two dimensions we construct a half-chiral Kekule honeycomb model and show that its unusual higher-order topology protects a single zero-energy mode at a single corner.

</details>

### [Comparing weakly interacting and free quantum dynamics locally](https://arxiv.org/abs/2611.27707)
*Jorge Acu\~na Flores, Joscha Henheik, Marius Lemm et al.* · `math-ph` · arXiv:2611.27707v1 · relevance 0.15

- **In one sentence**: Using Lieb-Robinson bounds to show that weakly interacting many-body quantum dynamics can be locally approximated by free (non-interacting) one-body dynamics on large perturbative time scales, yielding quantum diffusion results for weakly interacting Fermi systems and free-correlation approximations for Fermi-Hubbard models with low spin-down density.
- **In plain words**: This paper studies how quantum particles spread out and interact in a crowd. It shows that, for weak interactions and for a limited time, the complicated many-particle behavior can be locally replaced by a simpler version where the particles do not interact. Using this replacement, the authors prove that spreading behaves diffusively in certain systems and that some correlation patterns match their non-interacting counterparts.
- **Why it matters**: It gives a rigorous way to transfer known results for simple non-interacting systems to interacting ones over finite times, which matters for understanding how quantum information spreads. The text does not indicate direct experimental or applied consequences, and its link to the numerical work by Bippus et al. is described only as a counterpart, not as a confirmation.
- **Background needed**: - Quantum many-body system: many interacting particles whose joint state is described by quantum mechanics.
- Lieb-Robinson bound: a mathematical limit showing that effects spread through a lattice system at a finite speed, roughly like a light cone.
- Non-interacting (one-body) dynamics: each particle evolves on its own, which is much easier to analyze.
- Quantum diffusion: spreading that grows with time in the way heat or ink spreads, here measured by an operator spreading diagnostic.
- Out-of-time-ordered correlator (OTOC): a correlation function used to measure how quickly quantum information scrambles.
- Fermi-Hubbard model: a standard lattice model of interacting electrons.
- Perturbative regime: results valid when interactions or disorder are weak and times are not too long. · level: research-level

<details><summary>Original abstract</summary>

Lieb-Robinson bounds (LRBs) have become a standard tool for perturbative results in quantum many-body physics, including gap stability and many-body adiabatic theory. Here, we use LRBs to locally approximate weakly interacting many-body dynamics with one-body dynamics on large, perturbative time scales. This allows us to use one-body transport results to establish the expected many-body transport behavior on finite time scales in the following two illustrative settings: (i) We prove quantum diffusion, as quantified by a certain operator spreading diagnostic, in weakly interacting and weakly disordered Fermi systems in dimensions $D\geq2$ on large finite time scales based on the non-interacting diffusion result of Black, Drogin, and Hern\'andez [arXiv:2506.06468]. (ii) We show for Fermi-Hubbard models with initially low spin-down density, that all local multi-time spin-up correlation functions are approximated by their free counterparts. In particular, we obtain an OTOC (out-of-time-ordered correlator) counterpart to the patterns of short-time entanglement related to lattice path counts observed numerically by Bippus et al. [Phys. Rev. B 113, 035152 (2026)].

</details>

## Particle physics

### [Probing Compressed Dark Sectors at a Muon Collider through Dilepton Signatures and Machine Learning](https://arxiv.org/abs/2611.27518)
*Mohamed Belfkir, Ayoub Hmissou, Larbi Rahili* · `hep-ph` · arXiv:2611.27518v1 · relevance 0.19

- **In one sentence**: A study proposing that machine-learning classifiers (BDT and XGBoost) applied to dilepton final states at a future muon collider could help find inert-doublet scalar dark matter in compressed mass spectra via the process μ+μ− → AH, A → HZ*, Z* → ℓ+ℓ−.
- **In plain words**: The paper asks whether a possible dark matter particle, a hidden heavier cousin of the Higgs in a simple extension of the Standard Model, could be spotted at a future muon collider. The idea is that two heavy partner particles are made in muon collisions, one decays into the other plus a virtual Z boson, and that Z decays to a pair of leptons. Machine-learning tools are used to pick this signal out from ordinary background events.
- **Why it matters**: Dark matter that is only slightly heavier-or-lighter than its partner ("compressed" spectra) is hard to see at existing colliders, so a cleaner collider with machine-learning analysis is one proposed route to search for it. The text does not report sensitivity numbers or specific results, so how strong the claimed discovery potential is cannot be judged from this summary alone.
- **Background needed**: - Standard Model: the current theory of known particles and forces.
- Inert doublet model: a simple extension adding a second Higgs-like field; its lightest neutral new particle can be dark matter.
- Dark matter relic abundance: the amount of dark matter left over from the early universe; the model struggles to match the observed amount in some mass ranges.
- Compressed spectrum: new particles with very similar masses, so their decay products are soft and hard to detect.
- Muon collider: a proposed future machine colliding muons and antimuons, offering cleaner collisions than proton machines.
- Dilepton signature: a pair of leptons (electron or muon pairs) used as the detectable trace of the event.
- BDT / XGBoost: machine-learning methods that combine many decision rules to separate signal from background.
- Off-shell Z* : a virtual Z boson, not on its mass shell, produced in the decay chain. · level: research-level

<details><summary>Original abstract</summary>

The inert doublet model (IDM), a minimal extension of the Standard Model (SM), provides a scalar dark matter (DM) candidate that belongs to the additional Higgs doublet. The model faces challenges in achieving the correct relic abundance for compressed spectra and DM masses in the high-mass range. In this work we investigate the prospects of detecting dark matter candidates at future high-energy muon colliders. Focusing on the process $\mu^+ \mu^- \to AH$ with subsequent decay $A \to H Z^*$ and $Z^* \to \ell^+\ell^-$, we explore the sensitivity of machine learning techniques, specifically Boosted Decision Trees (BDT) and XGBoost, to distinguish the signal from Standard Model backgrounds. We demonstrate that the combination of advanced multivariate analysis with high-luminosity muon collisions enhances the discovery potential for inert scalars in compressed mass spectra scenarios.

</details>

### [From Resonance Properties to High-Energy Behavior: The $R$ Ratio from Lattice QCD](https://arxiv.org/abs/2611.27586)
*Nan Wang, Long-cheng Gui, Jun Hua et al.* · `hep-lat` · arXiv:2611.27586v1 · relevance 0.17

- **In one sentence**: A lattice QCD study that uses Bayesian spectral reconstruction of Euclidean correlators near the physical pion mass to extract the R-ratio, the rho-peak decay constant f_rho, and a Gaussian-smeared R-ratio compared against experiment, with finite-volume effects examined across ensembles.
- **In plain words**: This paper uses supercomputer simulations of the strong force that binds quarks into protons and pions to predict how often electrons and positrons colliding at high energy turn into hadrons, a quantity called the R-ratio. The authors reconstruct the particle-production spectrum from simulated data and compare it with experimental measurements. They report that the reconstruction matches the smooth high-energy trend seen in experiment, and that the rho resonance's decay constant comes out close to the experimental value.
- **Why it matters**: Computing this kind of inclusive quantity directly from the underlying theory is hard, so a method that reproduces both the resonance peak and the broad high-energy behavior is of interest to lattice QCD and hadron physics. The text does not establish how this compares with other lattice approaches, and its claimed applications to other channels and decay rates are stated as potential only.
- **Background needed**: - QCD (quantum chromodynamics) is the theory of the strong force binding quarks and gluons.
- Lattice QCD simulates that theory on a discrete grid of space and time on computers.
- The R-ratio is the ratio of hadron production to muon-pair production in electron-positron collisions; it probes the strong force across energies.
- A resonance (here the rho meson) is a short-lived particle seen as a peak in the energy spectrum; f_rho is its decay constant, a measure of how strongly it couples to its decay channel.
- Euclidean correlators are simulation outputs in imaginary time that must be mathematically converted (via Bayesian reconstruction) back to real-energy spectra.
- Finite-volume effects are distortions caused by simulating in a box of finite size.
- A Gaussian smearing with width sigma is a broadening applied to compare lattice and experimental spectra on equal footing. · level: research-level

<details><summary>Original abstract</summary>

We investigate resonance properties and inclusive spectral behavior through Bayesian reconstruction of the $R$-ratio from Euclidean lattice correlators near the physical pion mass. Without additional Gaussian smearing, the reconstructed spectrum already captures the smooth high-energy behavior observed in experiment. Direct integration of the $\rho$ peak determines $f_\rho$ with approximately $1\%$ statistical precision and close agreement with the experimental reference, providing access to resonance properties without resolving individual finite-volume levels. With a common Gaussian width of $\sigma=0.6$~GeV, the lattice and experimental $R$-ratios show good overall agreement over $0.25$--$2.50$~GeV. Comparisons among ensembles with spatial extents up to approximately $10$~fm demonstrate that finite-volume effects can be controlled across these complementary observables. These results demonstrate a unified framework for studying resonance and inclusive physics from lattice QCD, with potential applications to other hadronic channels, inclusive decay rates, and hadronic tensors.

</details>

## Nuclear physics

### [Nuclear Shell Model on the Light Front](https://arxiv.org/abs/2611.26895)
*Zhenkai Fu, Adam Freese, Gerald A. Miller* · `nucl-th` · arXiv:2611.26895v1 · relevance 0.17

- **In one sentence**: The paper builds an analytically solvable light-front harmonic-oscillator model of nuclear shell structure and electromagnetic form factors, finding shell splitting tied to a longitudinal confinement interaction and form factors that differ from non-relativistic results, illustrated for 48Ca and 208Pb.
- **In plain words**: This paper looks at how the protons and neutrons inside an atomic nucleus are arranged in energy levels, using a version of quantum theory that treats space and time more relativistically than the usual textbook approach. The authors solve a simple model exactly, and find that one kind of energy level splits apart in a way the standard non-relativistic picture does not predict. They then apply the model to calcium-48 and lead-208 and report that its predicted scattering patterns (form factors) differ noticeably from the non-relativistic ones.
- **Why it matters**: Nuclear shell models underpin much of how physicists interpret nuclear experiments, so a tractable way to include relativistic effects could matter for future calculations. The text does not show how large these effects are in experiments or whether they change existing predictions in practice, so that remains uncertain.
- **Background needed**: - Nuclear shell model: nucleons fill discrete energy levels in the nucleus, much like electrons in an atom.
- Non-relativistic treatment: the standard approach that ignores the effects of Einstein's special relativity on fast-moving particles.
- Light-front quantization: a relativistic formulation that uses "light-front" time to make certain calculations simpler.
- Harmonic oscillator: an idealised model where particles are held by a spring-like force, which is exactly solvable.
- Form factor: a function describing how a nucleus scatters probes such as electrons, reflecting its internal charge and structure.
- Hellmann-Feynman theorem: a standard result that relates how an energy changes to the expectation value of a parameter's operator, used here to trace the splitting to a specific interaction. · level: research-level

<details><summary>Original abstract</summary>

Light-front descriptions of nuclear structure provide a relativistic framework that can potentially deepen our understanding of nuclear structure by revealing effects that are absent from traditional non-relativistic treatments. To utilize this framework, we start from the light-front harmonic oscillator to analytically calculate the shell structure and electromagnetic form factors. The relativistic shell model shows that the light-front result recovers the nonrelativistic oscillator limit while introducing shell splitting that depends on the longitudinal excitation quantum number. We derive the resulting effects on the shell model and use the Hellmann-Feynman theorem to identify the longitudinal confinement interaction as the origin of this splitting. We illustrate these results through applications to $^{48}\mathrm{Ca}$ and $^{208}\mathrm{Pb}$. In addition, we demonstrate a substantial difference between form factors calculated using non-relativistic and light-front treatments, a difference that further underscores the importance of including relativistic effects in the description of nuclear structure. Our findings demonstrate a tractable approach to relativistic nuclear calculations and show how extending nuclear models beyond the non-relativistic approximation can yield meaningful physical insight.

</details>

### [Nuclear Precision and Multimessenger Constraints on Neutron-Star Structure](https://arxiv.org/abs/2611.27669)
*Hisham Anwer, A. Adel, E. Omar* · `nucl-th` · arXiv:2611.27669v1 · relevance 0.10

- **In one sentence**: The paper proposes an observable-dependent variance ceiling on neutron-star core structure and a "radius–Love compensation" mechanism, and reports that a 0.3 km pulsar radius plus a 10% binary tidal measurement would remove 44–68% of current logarithmic Love-number variance across four data-conditioned equation-of-state families.
- **In plain words**: This paper asks how much we can pin down the inside of a neutron star, the extremely dense leftover core of a collapsed star, using nuclear laboratory data together with astronomical measurements. The authors estimate how much uncertainty remains in one property, the tidal Love number, which describes how easily a star deforms under another body's gravity. They report that combining a precise radius measurement from a pulsar with a tidal measurement from a binary star system would remove roughly 44 to 68 percent of the present uncertainty.
- **Why it matters**: Neutron-star tides and radii are measurable from gravitational-wave and X-ray observations, so linking them to laboratory nuclear constraints is a concrete way to test models of ultra-dense matter. The text does not show how robust these estimates are beyond the four equation-of-state families it uses, so the size of the effect should be treated as provisional.
- **Background needed**: - Neutron star: the collapsed core of a massive star, roughly city-sized but denser than an atomic nucleus.
- Equation of state (EOS): a rule linking pressure to density, which determines how a star is built; "families" are groups of such models.
- Tidal Love number: a dimensionless number describing how much a star deforms when another body pulls on it.
- Logarithmic variance: a measure of spread in the logarithm of a quantity, i.e. how uncertain the value is.
- Pulsar radius: the size of a rapidly spinning neutron star, inferred from its emission.
- Binary tide: the deformation of a star caused by a companion in a two-star orbit, measured from orbital or gravitational-wave signals.
- Nuclear constraints: limits from experiments on atomic nuclei that restrict the possible EOS. · level: research-level

<details><summary>Original abstract</summary>

Neutron-star cores retain structural freedom beyond the constraints supplied by nuclear measurements. We quantify this freedom through an observable-dependent variance ceiling and identify radius--Love compensation as a mechanism suppressing nuclear constraints on tides. Across four data-conditioned equation-of-state families, a pulsar radius measured to 0.3 km paired with a binary tide measured to 10\% removes 44--68\% of the current logarithmic Love-number variance. The framework connects laboratory precision and complementary stellar measurements to core structure.

</details>

## Quantum information and computing

### [Autonomous quantum machine learning via Riemannian gradient-based optimization](https://arxiv.org/abs/2611.27815)
*Kasidit Srimahajariyapong, Thiparat Chotibut, Suwannachad Suwannajitt et al.* · `quant-ph` · arXiv:2611.27815v1 · relevance 0.25

- **In one sentence**: The paper proposes autonomous quantum machine learning, where Riemannian gradient-based training runs entirely inside a quantum circuit without quantum measurements or a classical optimization loop, with an exponential convergence guarantee for small step sizes and numerical tests on phase classification and hidden-symmetry unitary learning.
- **In plain words**: Most quantum machine learning today trains by repeatedly measuring a quantum device and sending the results to a classical computer to adjust settings. This paper proposes a way to let the quantum system update its own settings during training, so the classical feedback loop is removed. The authors state that under certain conditions this can be done autonomously, that training converges exponentially in the number of iterations for small steps, and that in their numerical tests the model could find a hidden symmetry in the data at low circuit depth using only a few training examples.
- **Why it matters**: Measurement and classical feedback are often named as a key bottleneck for scaling quantum machine learning, so a training method that avoids them addresses a real practical concern. The results are numerical and limited to the paper's chosen examples, so how far the approach extends to larger or noisy hardware is not established by the text.
- **Background needed**: - Quantum machine learning: training a parameterized quantum circuit to perform a learning task.
- Measurement: reading out a quantum state yields classical numbers but disturbs the state and must be repeated many times.
- Gradient-based optimization: adjusting parameters step by step in the direction that reduces a cost function.
- Riemannian gradient: gradient descent constrained to a curved space of allowed quantum operations (e.g., unitary matrices), so updates stay valid.
- Circuit depth: the number of sequential layers of quantum gates; a proxy for run time and noise exposure.
- Unitary learning and phase classification: learning a quantum transformation, or sorting quantum states by their phase of matter.
- Hidden symmetry: an invariance in the data (such as a transformation that leaves outcomes unchanged) not specified in advance. · level: research-level

<details><summary>Original abstract</summary>

Quantum machine learning models typically rely on repeated quantum measurements and classical optimization during training, making the quantum-to-classical information-extraction process a fundamental bottleneck for scalability. We propose a framework for autonomous self-training quantum machine learning, based on Riemannian gradient optimization, in which the optimization proceeds entirely within the quantum domain without requiring quantum measurements or classical feedback. We derive the Riemannian gradient update rules for a broad class of learning tasks and identify sufficient conditions under which the resulting training dynamics can be realized fully autonomously. Within this regime, we establish an exponential convergence guarantee, in the training iterations, for sufficiently small step sizes, and further analyze the training cost in terms of the growth of the circuit depth. Importantly, we further show that the trained model can automatically discover symmetries hidden in the training data without $\textit{a priori}$ specification. For the canonical examples of quantum phase classification and unitary learning with a hidden symmetry, our numerical study indicates that learning can be achieved at low circuit depths with only a few distinct training examples. Our results thus establish autonomous quantum machine learning as a promising paradigm that removes the classical optimization loop while retaining strong theoretical guarantees and practical performances.

</details>

### [Practical insights into controlling exponential concentration in quantum machine learning](https://arxiv.org/abs/2611.27486)
*Fernando Mondragon-Sampedro, Diego Alvarez-Estevez* · `quant-ph` · arXiv:2611.27486v1 · relevance 0.19

- **In one sentence**: A comparative empirical study of exponential concentration (observables becoming insensitive to input changes as system size grows) across fidelity quantum kernels, projected quantum kernels, and quantum extreme learning, using an expectation-value variance framework and bandwidth scaling as a control knob.
- **In plain words**: Quantum machine learning models can fail when their measured outputs barely change as the input changes, and this gets worse as the quantum system grows. This paper compares three quantum model designs to see how strongly this happens and what factors influence it. It finds that some approaches suffer more than others, and that scaling the encoding "bandwidth" (how strongly inputs are stretched into the quantum circuit) can help in moderate cases but loses its benefit when the circuit is highly expressive.
- **Why it matters**: Exponential concentration is a known obstacle to scaling quantum machine learning, so practical guidance on which designs and settings reduce it is useful to researchers building these models. The text does not establish how far the findings extend beyond the systems studied, so their broader significance is uncertain.
- **Background needed**: - Quantum machine learning: using quantum circuits as models that learn from data.
- Quantum kernel: a similarity measure between data points computed from quantum states; fidelity kernels compare overlaps of states.
- Exponential concentration: as the number of qubits (quantum bits) grows, outputs cluster around one value, so differences between inputs become tiny and hard to measure.
- Observable and expectation value: a measurable quantity and its average result from repeated quantum measurements; variance measures how spread out those results are.
- Measurement locality: whether a measurement involves a few qubits (local) or the whole system (global).
- Entanglement and expressivity: entanglement is quantum correlation between qubits; expressivity is how broadly a circuit can explore possible quantum states.
- Bandwidth scaling: a factor that controls how strongly input data is mapped into rotation angles in the circuit. · level: research-level

<details><summary>Original abstract</summary>

Quantum Machine Learning (QML) models are often limited by exponential concentration, where quantum observables become insensitive to input variations as system size increases. In this work, we provide a comparative empirical study of this phenomenon across Fidelity Quantum Kernels (FQK), Projected Quantum Kernels (PQK), and Quantum Extreme Learning (QEL), within a unified observable-based framework based on expectation-value variance. We investigate how measurement locality, entanglement, and circuit expressivity shape concentration across different architectures. Global fidelity-based kernels exhibit strong concentration driven by Hilbert space dimensionality, whereas local-observable approaches reduce but do not eliminate this effect. In PQK and QEL, concentration is primarily governed by entanglement and quantum dynamical expressivity, with reservoir depth emerging as a key factor in QEL architectures. We further study bandwidth scaling as a general mechanism for controlling encoding expressivity across all models. Our results indicate that bandwidth scaling effectively reduces concentration in moderate regimes by restricting the effective expressivity of the encoding, though this protective effect diminishes in highly expressive structural settings.

</details>

## Optics and atomic physics

### [Coherence Lengths of Laser Pointers](https://arxiv.org/abs/2611.26878)
*Vaishnavi Rao Namakkal Ranga Rao, Marissa R. Godoy, Mark D. Sotnikov et al.* · `physics.optics` · arXiv:2611.26878v1 · relevance 0.15

- **In one sentence**: The paper measures the coherence lengths of several low-cost green laser pointers, using a noncollinear-beam interferometer read out by a CMOS detector array, and finds values that can exceed 10 cm while varying from device to device.
- **In plain words**: Coherence length is how far a light beam can travel and still interfere with a copy of itself, a rough measure of how "pure" or single-colored the light is. The authors tested cheap green laser pointers, including three diode-type lasers and one frequency-doubled solid-state laser, to see how far their light stayed coherent. They found the answer varies between devices, but often reaches more than 10 cm.
- **Why it matters**: The work is modest in scope: it characterizes everyday consumer lasers and suggests the setup could serve as a teaching experiment for advanced undergraduates. The abstract also says it may inspire laser-pointer designs that rely on interference, but that is speculative and not demonstrated in the text.
- **Background needed**: - Coherence length: the distance over which a light wave stays in step with itself; longer means more spectrally pure light.
- Interferometer: an instrument that splits a beam, recombines it, and reads the bright and dark fringes formed by the overlap.
- Noncollinear beam geometry: the two beams cross at an angle rather than travelling along the same line.
- Multimodal behavior: a laser emitting several slightly different wavelengths (modes) at once, which shortens coherence length.
- Diode laser and diode-pumped solid-state (DPSS) laser: two common designs; the green pointer uses a solid-state crystal that doubles an infrared neodymium laser's frequency to green.
- CMOS detector array: the same kind of sensor chip found in cameras, used here to record the fringe pattern. · level: intermediate

<details><summary>Original abstract</summary>

We report on the coherence lengths of low-cost green laser pointers in the midst of multimodal behavior using an optical interferometer based on noncollinear beam geometries and a CMOS detector array. Examined devices include three diode lasers and a frequency-doubled neodymium-emission diode-pumped solid state (DPSS) laser. Coherence length measurements are variable among devices, but values can nevertheless regularly exceed 10 cm. The work serves as a template for an advanced undergraduate physics laboratory experiment and may inspire new kinds of laser pointer devices utilizing interference effects as operative principles.

</details>

### [Test of gravitational redshift by optical clocks at different latitudes](https://arxiv.org/abs/2611.27588)
*Ingo Nosske, Chetan Vishwakarma, Tim L\"ucke et al.* · `physics.atom-ph` · arXiv:2611.27588v1 · relevance 0.13

- **In one sentence**: Two Earth-fixed optical atomic clocks at different latitudes are compared against the gravitational redshift predicted by general relativity, using independent geodetic height data, reaching a 4.6×10^-5 uncertainty and arguing that Earth's rotation can enhance sensitivity to a violation.
- **In plain words**: The paper checks a prediction of Einstein's general relativity: clocks sitting higher in a gravitational field tick slightly faster. The authors compared the ticking of two optical atomic clocks placed at different heights and latitudes on Earth, and found the measured difference matches the predicted shift. Their main new idea is that separating the clocks north-south, not just up-down, can make the test more sensitive because Earth's rotation partly offsets the height difference.
- **Why it matters**: The result tightens ground-based tests of a basic relativity prediction by about a factor of two, according to the text, and the latitude approach is presented as a new way to get closer to space-based test sensitivity. Its wider significance beyond precision testing of relativity is not stated in the text.
- **Background needed**: - General relativity: Einstein's theory of gravity, which says gravity affects the passage of time.
- Gravitational redshift: clocks lower in a gravitational field run slower compared with clocks higher up; the shift is seen as a change in frequency.
- Optical atomic clocks: very precise clocks that count the oscillations of light absorbed by atoms, far more stable than ordinary clocks.
- Geodetic measurements: precise surveys of the heights and positions of the clock sites relative to Earth's shape.
- Centrifugal potential: the effective pull from Earth's spin, which depends on latitude and partly cancels gravity's height effect.
- Uncertainty level: the size of the largest plausible error; smaller means a stricter test. · level: research-level

<details><summary>Original abstract</summary>

General relativity predicts that frequency comparisons between clocks are affected by both gravitational and kinematic time dilation. While the kinematic contribution has been tested with high accuracy, experimental tests of the gravitational redshift remain comparatively less stringent. Here, we measure the frequency shift between two Earth-fixed optical atomic clocks at different potentials and compare it to the redshift predicted by general relativity using independent geodetic measurements. The observed shift agrees with the prediction, testing the gravitational redshift at the $4.6 \times 10^{-5}$ uncertainty level, improving ground-based tests by a factor two. Previous ground-based tests separated the clocks mainly vertically. For clocks at different latitudes, their height difference is governed not only by the gravitational potentials at their locations but also by the centrifugal potentials caused by Earth's rotation. As both contributions can partially cancel, the gravitational contribution can be considerably larger than their height difference suggests. In this work, a separation of the clocks by $4^\circ$ in latitude enhances their sensitivity to a gravitational redshift violation threefold, to the equivalent of an approximately 1200 m difference in height for small latitudinal separation. Our results establish Earth's rotation as a so far unexploited resource for advancing ground-based tests of the gravitational redshift towards the sensitivity of previous space-based experiments.

</details>

## Fluids and plasma

### [Hot-Layer Ignition in High-Gain Inertial Confinement Fusion](https://arxiv.org/abs/2611.27760)
*M. Lourmande, B. Canaud* · `physics.plasm-ph` · arXiv:2611.27760v1 · relevance 0.13

- **In one sentence**: The paper proposes an analytical ignition criterion for a shocked deuterium-tritium shell (a "hot layer") that can ignite independently of the hot spot in very high-gain inertial confinement fusion targets, and checks it with a three-zone model and 1D simulations.
- **In plain words**: Inertial confinement fusion squeezes a small fuel capsule with lasers or X-rays until it fuses. This paper looks at a case where a thin, heated outer layer of the fuel starts burning on its own, and the energy from that burn helps squeeze the hot core again. The authors describe this in a simple three-zone model and in 1D computer simulations, and report that it adds roughly 50% to the energy the target releases.
- **Why it matters**: Energy gain is the central measure of whether fusion targets can produce more energy than they take in, so a mechanism that boosts output by about 50% in simulation is worth attention. The text does not say how well this holds up in full 3D experiments, so the result should be read as a modelling claim for now.
- **Background needed**: - Inertial confinement fusion (ICF): a tiny fuel pellet is compressed and heated so fusion reactions happen before it flies apart.
- Deuterium and tritium: heavy forms of hydrogen, the usual fusion fuel.
- Hot spot: the central, very hot, low-density region where ignition is normally thought to start.
- Shocked shell: the denser outer fuel layer heated by the compression shock wave.
- Alpha particles: helium nuclei released by fusion; they deposit their energy locally and heat nearby fuel.
- Ignition: the point where self-heating from fusion outpaces energy losses and burning becomes self-sustaining.
- Gain: ratio of fusion energy released to the laser or driver energy put in.
- 1D simulation: a computer model that varies in only one spatial direction, simpler than full 3D models. · level: research-level

<details><summary>Original abstract</summary>

Ignition of the shocked deuterium tritium shell is identified during the thermonuclear combustion of very high-gain targets in inertial confinement fusion (ICF). This mechanism is due to the local energy deposition of the fusion alphas created in this shocked shell, independently of hot-spot ignition, and generates sufficient energy to fully recompress the hot spot. A new analytical criterion for the ignition of the hot layer is presented. A simple three zone model, based on the thick layer hot-spot model, reproduces this mechanism, which breaks down into successive stages: ignition of the hot spot, compression of the shocked shell, ignition of the shocked shell, and subsequent recompression of the hot spot. 1D numerical simulations highlight the onset of this hot layer ignition thereby satisfying the analytical ignition criterion. It is shown that this mechanism amplifies the energy released by the combustion of the target by approximately 50 %.

</details>

### [A 3D PINN-Based Framework for Patient-Specific Pulmonary Hemodynamics Using Windkessel Models](https://arxiv.org/abs/2611.27351)
*Celia Taboada, Luis Nu\~nez, Ang\'elica Casero et al.* · `math.NA` · arXiv:2611.27351v1 · relevance 0.12

- **In one sentence**: A physics-informed neural network (PINN) framework that solves pulsatile blood flow in a patient-specific pulmonary artery, coupled to a three-parameter Windkessel outlet model, with validation on 2D channels and an inverse identification of the outlet parameters from synthetic data.
- **In plain words**: Doctors often simulate blood flow in arteries using detailed computer meshes, which are slow and hard to set up for each patient. This paper tries a different route: a neural network trained to obey the fluid equations directly, without a mesh. The authors test it on simple channels, then on a patient's right pulmonary artery, and also use it to work backward and estimate the outlet resistance and compliance settings from synthetic data.
- **Why it matters**: Faster, mesh-free simulations could make patient-specific blood-flow modeling more practical in clinics and support "digital twin" models of a patient. The reported results are on 2D test cases and one geometry with synthetic data, and the authors themselves note open issues such as residual bias in local pressure and untested robustness to noisy clinical data, so the practical value is not yet established.
- **Background needed**: - Computational Fluid Dynamics (CFD): computer simulation of fluid flow, usually by dividing space into a mesh of small cells.
- Physics-Informed Neural Network (PINN): a neural network trained so its output satisfies the governing equations of physics (here, fluid flow), instead of needing a mesh.
- Windkessel model: a simple lumped electrical-style analogy (resistors and capacitors) that represents how the smaller vessels downstream resist and store pressure, used as a boundary condition at an outlet.
- RCR model: a Windkessel variant with two resistances and one capacitance; its three parameters are what the inverse problem estimates.
- Pulsatile flow: flow that rises and falls with each heartbeat.
- Inverse problem: inferring unknown model parameters from observed data, rather than predicting data from known parameters.
- Digital twin: a computer model tuned to mirror a specific patient's system. · level: research-level

<details><summary>Original abstract</summary>

Cardiovascular fluid dynamics modeling relies heavily on mesh-based numerical methods such as Computational Fluid Dynamics (CFD). While accurate, these methods entail significant computational costs and complex meshing workflows that limit their translation to clinical practice. Physics-Informed Neural Networks (PINNs) are a promising meshless alternative that embeds the governing equations directly into neural network training. In this work, we propose a PINN framework for pulsatile blood flow in patient-specific geometries with dynamic lumped-parameter Windkessel (RCR) outlet conditions representing distal vascular impedance. Coupling the Windkessel ODE to a 3D network raises two difficulties: the ODE alone does not fix the pressure level, and the local pressure variations that drive the flow are orders of magnitude smaller than the basal pressure imposed by the outlet. We address them by decomposing pressure into a time-dependent basal part and a spatially varying part, an initial condition and gauge for the Windkessel equation, a global mass-balance constraint, and a periodic Fourier embedding of time. Validated on 2D canonical channels (steady and pulsatile, with and without RCR outlet), the framework is then applied to a patient-specific right pulmonary artery, reproducing outlet flow, mean pressure, and the velocity and dynamic pressure fields with errors on the order of the data resolution. Finally, we solve the inverse problem of identifying the three Windkessel parameters of the outlet from synthetic data, recovering them with errors of about 0.3% from deliberately wrong initial values. Residual biases in the local pressure field and the need to test robustness to noisy clinical data remain open, but the results support PINNs as complementary tools for meshless hemodynamics and patient-specific digital twins.

</details>

## Biological physics

### [Receptor Abundance Alone Underpredicts Red Blood Cell Adhesion in Gaucher Disease](https://arxiv.org/abs/2611.27960)
*Zhaojie Chai, Pierre A. Buffet, Melanie Franco et al.* · `physics.bio-ph` · arXiv:2611.27960v1 · relevance 0.05

- **In one sentence**: A simulation study asks whether the rise in Lu/BCAM laminin receptors on red blood cells in Gaucher disease explains their excess adhesion, and finds that total receptor abundance alone underpredicts it, pointing instead toward receptor activity state.
- **In plain words**: Gaucher disease is an inherited condition in which red blood cells stick abnormally to blood vessel walls. The authors built a computer model of cells that form stochastic molecular bonds with a protein called laminin, calibrated it on healthy donors, and asked whether the extra receptors on diseased cells could account for the stickiness. They found that the modest rise in receptor count predicts much less adhesion than measured, and that matching the data needs several-fold more receptors that can actually bind, which fits a rise in chemically modified (phosphorylated) receptors.
- **Why it matters**: The result suggests that counting how many receptors a cell has may miss what matters for sticking, and that receptor activity may be the better measure. The text also reports that the same approach, using active-receptor counts, tracks changes in sickle cell disease under hydroxyurea treatment, and that stiffening the membrane may keep cells trapped at the spleen's narrow slits; how far these links hold beyond the reported model is not established here.
- **Background needed**: - Red blood cells carry surface receptors; adhesion depends on how many bonds form with a partner surface.
- Lu/BCAM is a receptor on red cells that binds laminin, a protein in the walls of blood vessels.
- Gaucher disease is an inherited disorder of fat-breakdown enzymes that alters red cell behaviour.
- Phosphorylation is the addition of a phosphate group that can switch a protein's activity on or off.
- Shear stress is the force of flowing blood sliding along a surface.
- Stochastic simulation models events, such as bond formation, as random processes over many trials.
- Sickle cell disease and hydroxyurea (a treatment that alters red cell properties) are mentioned as a comparison case. · level: research-level

<details><summary>Original abstract</summary>

Red blood cells (RBCs) in Gaucher disease (GD) adhere abnormally to vessel walls and carry more Lutheran/basal cell adhesion molecule (Lu/BCAM), a laminin receptor. Whether receptor abundance sets this adhesion is untested. We simulated RBCs carrying stochastic Lu/BCAM-laminin bonds, calibrated a population on control donors, and predicted GD adhesion from the 1.3-fold receptor rise. On laminin and endothelium the data exceed the prediction 1.6- to 1.7-fold. Matching them requires 2.4- and 4.6-fold more binding-competent receptors, compatible with the estimated 5.7-fold rise in phosphorylated receptors. Neither a stiffer membrane nor higher bond affinity removes the shortfall at high shear stress. In sickle cell disease, given active-receptor counts, the model predicts the fall in adhesion under hydroxyurea within 1.4-fold, while total receptors rise. Adhesion likely follows receptor state more than abundance. Stiffening instead retains cells at a splenic slit.

</details>

## Climate, atmosphere and Earth

### [Carbon dioxide responses shape estimates of Amazon forest vulnerability under solar geoengineering](https://arxiv.org/abs/2611.26908)
*Anupama K Xavier, Chris Jones* · `physics.ao-ph` · arXiv:2611.26908v1 · relevance 0.07

- **In one sentence**: Uses a CO2-dependent forest-sustainability threshold in a shared climate phase space to test whether stratospheric aerosol injection (SAI) reduces Amazon forest vulnerability under high-emission and mitigation scenarios.
- **In plain words**: The Amazon rainforest may be pushed toward dieback by heat and changes in rainfall. This paper asks whether spraying reflective particles into the upper atmosphere, a form of solar geoengineering, could ease that risk. The authors find it cuts projected warming a lot but leaves substantial drying and longer dry seasons, and the answer on forest risk depends heavily on how much extra CO2 is assumed to help plants.</plain>
<parameter name="why">Solar geoengineering is being discussed as a way to limit climate harm, so whether it protects a major forest matters for policy. The paper's main point is that its conclusion about forest protection swings sharply depending on whether elevated CO2 is assumed to make plants more resilient; the text does not establish how strong that effect is in reality.</plain>
<parameter name="background">- Stratospheric aerosol injection (SAI): releasing fine particles high in the atmosphere to reflect some sunlight and cool the planet.
- Solar geoengineering: deliberate efforts to reduce warming by changing how much sunlight reaches or is absorbed by Earth.
- Hydroclimate: the water side of climate, such as rainfall, dryness and dry-season length.
- Climate phase space: a way of plotting different climate scenarios on shared axes (for example warming versus rainfall change) so they can be compared.
- Sustainability threshold: a set of climate conditions beyond which forest is expected to be at risk of loss.
- CO2 fertilisation: plants may grow more or use water more efficiently when CO2 is higher, which is the resilience benefit the paper treats as uncertain.
- Grid cells: the map squares used in climate models; the paper reports the share of these exceeding the threshold.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

The Amazon rainforest is vulnerable to warming and changes in rainfall, yet whether solar geoengineering can reduce conditions associated with forest loss remains uncertain. Stratospheric aerosol injection (SAI) can offset greenhouse-gas-driven warming without fully restoring regional hydroclimate. Here we assess Amazon forest vulnerability under mitigation, high-emission and SAI scenarios using a Carbon dioxide-dependent forest-sustainability threshold in a common climate phase space. By late century, SAI reduces projected Amazon warming from 5.49 degree Celsius under high emissions to 2.45 degree Celsius, but substantial drying and longer dry seasons persist. Under SAI, 44.7 percentage of analysed grid cells exceed the present-day threshold, compared with 8.7 percentage when the future Carbon dioxide-dependent threshold is considered. This contrast reveals that apparent forest protection depends strongly on the assumed resilience benefits of elevated Carbon dioxide. Our findings highlight the importance of hydroclimatic changes and Carbon dioxide-dependent vegetation responses in assessing the potential of solar geoengineering to reduce Amazon forest vulnerability.

</details>

### [Spatiotemporal Landslide Runout Reconstruction from Sparse Observations with LAPIS-SHRED](https://arxiv.org/abs/2611.27132)
*Xingyue Zhang, Yuxuan Bao, Jeffrey Keck et al.* · `cs.CE` · arXiv:2611.27132v1 · relevance 0.06

- **In one sentence**: The paper applies LAPIS-SHRED, a latent-space neural-network reconstruction method trained on physics-based simulation ensembles, to reconstruct the spatiotemporal runout of landslides near Mount St. Helens from sparse sensor data.
- **In plain words**: Landslides move fast and are rarely watched as they happen, so scientists usually only see the mud and debris left behind afterward. This paper describes a method that rebuilds the full path and timing of a landslide's runout from a small number of sensor readings, using computer simulations to learn from. The authors report that 32 sensor readings from one moment were enough to recover full trajectories with error below 5.8%.
- **Why it matters**: Better reconstruction of how far and how fast landslides travel could help hazard assessment where monitoring is thin. The text reports a spatial correlation of 0.843 against observed deposits, compared with 0.853 for the calibrated simulator, so it is close to but not better than the simulator; its practical value in real field settings is not shown in the text.
- **Background needed**: - Landslide runout: how far and how fast a slide or debris flow travels after it starts.
- Physics-based simulation ensemble: many computer runs of a flow model with varied settings, used as training data.
- Sparse observations: only a few sensor readings or deposit samples rather than full coverage.
- Latent space: a compressed, simplified internal representation a neural network learns from data.
- Recurrent decoder: a neural network that generates sequences over time from a compressed input.
- NRMSE (normalized root-mean-square error): an error measure scaled to the data range; lower is better.
- Spatial correlation (r): how closely two maps match in pattern, from 0 (none) to 1 (perfect). · level: research-level

<details><summary>Original abstract</summary>

Reconstructing the spatiotemporal evolution of landslide runout from limited observations is a central challenge in geohazard assessment: transient flow dynamics are rarely observed directly, and available data are often confined to post-event deposits or brief monitoring windows. We apply LAPIS-SHRED (LAtent Phase Inference from Short time sequence using SHallow REcurrent Decoders) to reconstruct runout events near Mount St. Helens, USA. Trained on physics-based simulation ensembles, the framework supports both backward reconstruction from single frame and forward prediction from short initial window across different runout regimes. Using 32 sensor observations from a single timepoint, LAPIS-SHRED recovers complete runout trajectories with NRMSE below 5.8%, robust across varying observational and training conditions. Validation against observed deposits yields spatial correlation of r = 0.843 against the calibrated simulator's r = 0.853. These results suggest that latent-space temporal inference offers a viable pathway for spatiotemporal landslide reconstruction under extreme observational constraints typical of field settings.

</details>

## Cosmology

### [Beyond the Peak: Constraining early dark energy with the damping tail](https://arxiv.org/abs/2611.27069)
*Hao Wang, Gen Ye, Yun-Song Piao* · `astro-ph.CO` · arXiv:2611.27069v1 · relevance 0.16

- **In one sentence**: The paper argues that the post-peak "tail" of an early dark energy scalar field, not just its peak amplitude and location, carries observable information about a multiscale potential (axion-like plus alpha-attractor regimes) and can improve fits to high-ℓ CMB data and the inferred H0.
- **In plain words**: Cosmologists have proposed an "early dark energy" component that briefly existed before the universe's recombination era, which might ease a disagreement between two ways of measuring how fast the universe expands. This paper focuses on the part of that energy's behavior after its main burst, which the authors call the "tail," and builds a simple model in which different parts of a field's energy landscape control its motion. Fitting the model to cosmic microwave background, galaxy-clustering (baryon acoustic oscillation), and supernova data, they report a better match to the high-resolution microwave data and a higher best-fit expansion rate.
- **Why it matters**: The Hubble tension is a well-known discrepancy in cosmology, and the paper suggests that a previously overlooked feature of early dark energy models could help distinguish between them and partly address it. The text does not establish how decisive the improvement is, and the claims would need independent checks against other datasets.
- **Background needed**: - The Hubble tension: measurements of the universe's current expansion rate (H0) from the early universe (CMB) and from nearby stars and supernovae disagree.
- Early dark energy (EDE): a hypothetical scalar field that briefly contributes energy shortly before recombination, changing the sound-wave scale in the early universe; proposed as one way to ease the tension.
- Scalar field and potential: a field whose energy depends on its value, like a ball rolling in a landscape; the "potential" is that landscape's shape.
- Axion-like and alpha-attractor potentials: two classes of field-landscape shapes used in model building.
- Observational datasets: CMB (light from about 380,000 years after the Big Bang), baryon acoustic oscillations (large-scale galaxy patterns), and supernovae (distance markers).
- High-ℓ CMB: the small-angle, fine-scale part of the microwave sky map. · level: research-level

<details><summary>Original abstract</summary>

Early dark energy is commonly characterized by the amplitude and location of its primary energy-injection peak. We show that its post-peak evolution, which we call the \emph{EDE tail}, provides an additional observable probe of the underlying scalar dynamics and can materially affect its ability to alleviate the Hubble tension. We construct a simple phenomenological framework in which distinct regions of a multiscale scalar potential govern the dynamics at different field scales. As a representative realization, we consider a potential that combines axion-like and $\alpha$-attractor-like regimes, thereby allowing the EDE tail to be reshaped through reflection and asymmetric oscillations. Confronting this framework with cosmic microwave background, baryon acoustic oscillation, and supernova observations, we find an improved fit to the high-$\ell$ CMB data together with a higher inferred bestfit $H_0$. Our results show that the EDE tail retains observable information about the underlying scalar potential that is not captured by the conventional peak parameters alone. This provides a complementary route for constructing and observationally distinguishing EDE scenarios, and potentially for further alleviating the Hubble tension.

</details>

### [Dark Energy Based on Modified Gravity: Where the Future Lies?](https://arxiv.org/abs/2611.27228)
*Shin'ichi Nojiri, Sergei D. Odintsov, V. K. Oikonomou et al.* · `gr-qc` · arXiv:2611.27228v1 · relevance 0.16

- **In one sentence**: The paper argues that realistic F(R) gravity models fitted to DESI-era dark energy data can drift into anti-gravity or ghost-graviton regimes in the future, and proposes a scalar-field potential barrier at small curvature to prevent this without fine-tuning initial conditions.
- **In plain words**: Recent measurements hint that dark energy, the mysterious cause of the universe's accelerating expansion, may have behaved in an unusual "phantom" way in the recent past and then switched to a more ordinary form. Some modified-gravity theories fit these data, but this paper finds that some of them may eventually lead to unphysical behavior, such as repulsive "anti-gravity." The authors propose adding a barrier to a scalar field that keeps the universe out of that future, and suggest ways to test this with galaxy motion and the kinetic Sunyaev-Zel'dovich effect.
- **Why it matters**: It bears on whether the dark-energy models that currently fit DESI survey data are physically sound over the long term, a question that matters for the future of cosmology. The text does not show how strongly the proposed barrier would be supported by data, so its practical weight is still open.
- **Background needed**: - Dark energy: the unknown component driving the universe's accelerated expansion.
- Phantom vs. quintessence: phantom dark energy has an equation-of-state value below -1, quintessence stays above it; the text says the behavior may have shifted between them.
- DESI: a large galaxy survey whose data constrain dark energy.
- F(R) gravity: a modification of Einstein's general relativity in which the gravitational Lagrangian depends on the Ricci scalar curvature R.
- Scalar field: an extra field whose value can vary across space and time; here it carries the potential barrier.
- Ghost graviton: a mode with negative kinetic energy, which signals instability.
- Peculiar velocities and the kSZ (kinetic Sunyaev-Zel'dovich) effect: observable signatures used to test gravity and dark energy on large scales.
- Fine-tuning: choosing special starting values for parameters to get a desired outcome. · level: research-level

<details><summary>Original abstract</summary>

Based on current observational data, there is a strong possibility that dark energy was in a phantom regime in the near past, and a transition from a phantom to a quintessential regime may have occurred. Since then, many scenarios compatible with the DESI data have been proposed. In particular, there exist several realistic models in the framework of $F(R)$ gravity. In this paper, we show that such realistic models of $F(R)$ gravity may produce an anti-gravity or ghost graviton in the future. The problem could be avoided by further changing the parameters and fine-tuning the initial conditions, but we propose to introduce a potential barrier of the scalar field for the small scalar curvature region, which prevents the Universe from evolving into the anti-gravity or having a ghost graviton region, without the fine-tuning of the initial conditions. We also discuss how this regime can be tested using peculiar velocity and kSZ effect probes.

</details>

## Galaxies

### [The role of gas on the collisional runaway path to supermassive black hole seeds](https://arxiv.org/abs/2611.26885)
*Boris Cuevas, Basti\'an Reinoso, Andr\'es Escala et al.* · `astro-ph.GA` · arXiv:2611.26885v1 · relevance 0.18

- **In one sentence**: Coupled N-body and SPH simulations (AMUSE, BRIDGE) of dense, gas-embedded star clusters test how gas fraction (0–20%) changes runaway stellar collisions and the mass of the resulting black hole seed.
- **In plain words**: The paper looks at how the very large black holes seen in the early universe might have started, specifically from tightly packed clusters of stars that merge together. The authors ran 48 computer simulations of such clusters, some containing gas, and tracked how stars collide. They report that more gas tended to produce a more massive central black hole, with the gain growing from about 8% at low gas fractions to about 44% at 20% gas.
- **Why it matters**: Supermassive black holes are observed at a time when the universe was young, and it is unclear how they grew so fast, so a possible seed-formation route is of interest. The result is limited to the simulated setups, and the authors say their simulations do not fully resolve the dynamical friction effect they mention, so the findings should be read as a model-based indication rather than a settled answer.
- **Background needed**: - Supermassive black holes: black holes with millions to billions of times the Sun's mass, found at the centres of galaxies.
- Black hole "seeds": the smaller black holes that the largest ones are thought to grow from.
- Star cluster core collapse: the process in which stars in a dense cluster's centre sink and crowd together, speeding up collisions.
- Runaway collisions: stars merging repeatedly to form one very massive object that can collapse into a black hole.
- N-body simulation: a computer method that tracks the gravitational pull between many individual bodies (here, stars).
- SPH (smoothed particle hydrodynamics): a method that models gas as many small particles.
- Gas fraction: the share of the cluster's mass that is gas rather than stars.
- Dynamical friction: the drag that heavy objects feel as they move through a surrounding sea of lighter matter, which pulls them toward the centre. · level: research-level

<details><summary>Original abstract</summary>

The origin of supermassive black holes (SMBHs) remains unclear, despite observational evidence for their rapid formation in the early Universe, as evidenced by active galactic nuclei (AGN) at high redshift. In this paper, we investigate stellar dynamics in dense, gas-embedded clusters. We explore how gas influences the runaway collision process and the subsequent formation of SMBH seeds in a global instability scenario. We perform a series of coupled N-body and SPH simulations using the AMUSE framework, with the stellar and gaseous components interacting gravitationally via the BRIDGE method. We use 12 initial condition models with equal-mass stars following Plummer distributions, with total masses ranging from $10^3$ to $5 \times 10^5~M_{\odot}$, virial radii from $0.005$ to $0.1$ pc, and stellar masses of $1$, $10$ and $50$ $M_{\odot}$. For each model, we perform four simulations with gas fractions ranging from 0\% to 20\%, resulting in a total of 48 simulations. The gas is sampled with the same spatial distribution as the stars, with a mass ratio per particle of $m_{\rm SPH}/m = 0.01$, where $m$ is the stellar mass. We find that in most of our simulations, higher gas fractions lead to the formation of more massive black hole, as the core collapses earlier, triggering collisions through gas--star interactions. Our results show increases in BH mass of $\sim 8\%$ for low gas fractions, to $\sim 44\%$ at 20\% gas fraction. The core collapse time is also shortened, with the strongest reduction at $20\%$ gas fraction ($\sim 27\%$). The transonic regime of our initial conditions is where dynamical friction is most efficient in principle. Although our simulations do not fully resolve this effect, gas--star interactions are the principal mechanism driving the enhancement in BH formation efficiency, in the absence of other dissipation mechanisms.

</details>

### [An early interaction between the Sagittarius dwarf and the Milky Way I: Fossil signatures in the phase-space structure of the disc](https://arxiv.org/abs/2611.27898)
*Payel Das, Jason A. S. Hunt* · `astro-ph.GA` · arXiv:2611.27898v1 · relevance 0.14

- **In one sentence**: Using four controlled N-body plus hydrodynamic simulations of a Milky-Way-like galaxy hit by a Sagittarius-like dwarf on a polar orbit, this paper shows that a single early disc crossing thickens and heats the age-resolved thin disc in a datable way, and that the fiducial run's dispersion jump roughly matches the outer low-alpha disc observed by Das et al. (2024).
- **In plain words**: Our galaxy, the Milky Way, may have been brushed by the Sagittarius dwarf galaxy, a smaller neighbour, about 5 to 7 billion years ago. The authors ran computer simulations of that encounter and checked how the stars in the galaxy's flat disc were shaken up. They found that stars already present during the pass were puffed up and sped up in their up-and-down motion, while stars born later were not affected.
- **Why it matters**: If the disc keeps a lasting, age-dated record of one passing satellite, stellar ages and motions could be used to date past encounters and estimate the mass of the visitor. The authors say the mass-from-jump inversion is only good to about a factor of 1.5, so the link to the real satellite is approximate.
- **Background needed**: - Milky Way disc: the flat, rotating plane of stars containing the Sun.
- Sagittarius dwarf: a small galaxy being absorbed by the Milky Way; its orbit is thought to have passed through the disc in the past.
- N-body plus hydro simulation: a computer model tracking many gravitating particles (stars, dark matter) and gas over time.
- Phase-space structure: the joint map of where stars are and how fast they move.
- Vertical velocity dispersion: the spread of stars' up-and-down speeds; a higher value means the stars are being heated.
- Age-velocity dispersion relation: how the up-and-down spread grows with stellar age, a clock for disc heating.
- Thickening: stars spreading further above and below the disc plane.
- Low-alpha disc: a chemically defined, younger-looking population of Milky Way stars, identified by abundance ratios.
- Pericentre: the closest approach of an orbiting object to the centre of the host. · level: research-level

<details><summary>Original abstract</summary>

Several independent lines of evidence point to an early encounter between the Milky Way and the Sagittarius dwarf galaxy $5$-$7$ Gyr ago. We present four controlled $N$-body+hydro simulations, one of an isolated host galaxy and three of a single interaction between a Milky-Way-like host and a Sagittarius-like satellite on an unbound polar orbit. Relative to the fiducial satellite (with total mass $0.7\times10^{11}$ M$_\odot$), one run increases the satellite's mass by a factor of $1.5$ and another its crossing speed by a factor of $1.4$, giving pericentric speeds of $466$-$634$ km s$^{-1}$ at pericentric radii of $R\simeq15$-$18$ kpc. Comparing the present-day, phase-space structure in radial bins by age of newly-formed thin-disc stars across the runs, we find that stars that existed at the time of the passage are thickened by up to $\sim37$ per cent in mass-enclosed height and heated by up to $\sim5$ km s$^{-1}$ in vertical velocity dispersion relative to the control, while stars formed after the passage are unaffected. The heating signature is also evident when comparing the age-vertical velocity dispersion relation against a heating relation with a power law of $0.38$, obtained by fitting the isolated host. A single, disc crossing from an early interaction thus suffices to leave lasting, datable fossils in the age-resolved vertical structure of a galactic disc. The fiducial run's dispersion jump of $\sim4$ km s$^{-1}$ matches best with that observed in the outer low-$\alpha$ disc of the Milky Way (Das et al. 2024), corresponding to a perturber mass of $0.7\times10^{11}$ M$_\odot$, with a velocity of $466$ km s$^{-1}$ at a pericentric radius of $16.7$ kpc, though the inversion from jump amplitude to perturber mass is good only to a factor of $\sim1.5$.

</details>

## Exoplanets and planetary science

### [Hints of planet formation in progress around DR Tau from observations with LBT SHARK-NIR and SHARK-VIS](https://arxiv.org/abs/2611.27643)
*D. Mesa, G. Li Causi, R. Gratton et al.* · `astro-ph.EP` · arXiv:2611.27643v1 · relevance 0.14

- **In one sentence**: High-contrast narrow-band and broad-band imaging of the DR Tau protoplanetary disk with LBT SHARK-VIS and SHARK-NIR finds two compact features, consistent with reflected starlight rather than confirmed Halpha or Pabeta accretion from an embedded planet.
- **In plain words**: Young stars are surrounded by disks of gas and dust where planets form, and astronomers want to directly see newborn planets still inside them. This paper looks at one such disk, around the star DR Tau, using two cameras on a large telescope in Arizona. The team found two faint compact spots that have persisted over seven years and may move like objects orbiting the star, but the light they emit appears to be starlight bounced off dust rather than the glow of a forming planet.
- **Why it matters**: Direct detections of forming planets are rare, so candidate sources in disks matter for testing how planets form. This paper is a useful but tentative step: its main result is that the spots are most likely reflected dust light, so the planet interpretation remains unconfirmed.
- **Background needed**: - Protoplanetary disk: a rotating disk of gas and dust around a young star, where planets form.
- Embedded planet: a planet still growing inside its disk, usually much harder to see than a finished planet.
- Accretion: material falling onto a young object; hot falling gas emits specific colors of light, here hydrogen Halpha (visible red) and Paschen-beta (near-infrared).
- Narrow-band vs broad-band filters: narrow filters isolate one emission line; broad filters capture a wider color range.
- Signal-to-noise (S/N): how strong a signal is relative to background noise; S/N of 6 to 13 is a modest detection.
- Keplerian rotation: orbital motion expected for objects around a star, with inner parts moving faster than outer parts.
- MJup: Jupiter masses, a unit of planet mass.
- SPHERE: a previous high-contrast imager on the European VLT telescope that first detected the disk features. · level: research-level

<details><summary>Original abstract</summary>

Protoplanetary disks are the primary sites of planet formation. However, the direct imaging of protoplanets still embedded within their parental disks remains a significant challenge, with only a small number of confirmed detections to date and several candidates awaiting verification. We search for embedded planets in the protoplanetary disk of the young star DRTau by targeting accretion signatures from forming sub-stellar objects. Using narrow-band imaging, we observe both visible Halpha and near-infrared Paschen-beta (Pabeta) emission to identify actively accreting companions. To this end, we performed high-contrast observations of DRTau using the SHARK-VIS (0.40-0.95 micron) and SHARK-NIR (0.96-1.70 micron) imagers at the LBT. The study uses a combination of narrow-band filters to isolate accretion signatures and broad-band filters for multi-wavelength characterization in both the visible and near-infrared. Our observations recover the primary disk structures previously identified in the literature, albeit at low signal-to-noise (S/N). We identify two compact features with S/N between 6 and 13 in both narrow- and broad-band filters. The first, an elongated structure, matches previous SPHERE detections, while the second, more compact feature, is now confirmed despite its low S/N in earlier datasets. A comparison over a seven-year baseline confirms the stability of both structures. Their observed orbital motion is consistent with Keplerian rotation, potentially suggesting the presence of an undetected planetary-mass companion (few MJup) at the location of the second feature. However, our analysis does not confirm Halpha or Pabeta emission originating from localized accretion. Instead, we conclude that the observed flux is likely stellar light reflected by dust at these locations and discuss alternative mechanisms that could account for such detections.

</details>

### [2026 QQ8: Earth's temporary flyby of maximum lunation](https://arxiv.org/abs/2611.27770)
*Grigori Fedorets, Marco Micheli, Samantha Hemmelgarn et al.* · `astro-ph.EP` · arXiv:2611.27770v1 · relevance 0.09

- **In one sentence**: Astrometric, photometric and dynamical study of asteroid 2026 QQ8, a natural temporary Earth companion on a long flyby orbit near the theoretical maximum-duration "orbit of maximum lunation," with solar radiation pressure used to rule out an artificial origin.
- **In plain words**: Sometimes a small asteroid is briefly pulled into orbit around the Earth and then drifts away again. This paper examines one such object, 2026 QQ8, which was recently discovered. The authors tracked its position and brightness, modelled its path, and checked how sunlight pushes on it, concluding it is a natural rock rather than man-made debris.
- **Why it matters**: It is only the third known temporary Earth companion on a flyby orbit and the first of long duration, and its orbit sits near the predicted upper limit for how long such a capture can last in the Earth-Moon system. This makes it a useful test case for models of how Earth captures and releases small bodies; the text does not go beyond this.
- **Background needed**: - Temporary captures: a small asteroid can orbit Earth for a limited time before escaping, unlike the Moon, which is permanently bound.
- Astrometry: measuring precise sky positions over time to work out an orbit.
- Photometry and spectrophotometry: measuring brightness and colour across wavelengths; an "S-type" asteroid is a stony class, as opposed to darker carbon-rich types.
- Solar radiation pressure: the small push sunlight exerts on an object, which depends on its shape and density; here it helps separate natural from artificial objects.
- Orbit of maximum lunation: an orbit geometry, tied to the Moon's influence, where capture lasts longest.
- Discovery is recent, so the text gives no long-term follow-up. · level: research-level

<details><summary>Original abstract</summary>

Aims: On a rare occasion, asteroids are temporarily captured by the Earth to become the planet's interim companions. The discovery of asteroid 2026~QQ$_8$ provided an opportunity to study this class of objects, adding to the sparse discovery catalogue of Earth's temporary companions. Methods: We performed astrometric, photometric, and dynamical studies of 2026~QQ$_8$, and measured its solar radiation pressure signal to discern between a natural and an artificial origin. Results: We find 2026 QQ$_8$ to be of natural origin, with solar radiation pressure signal commensurable with natural objects and spectrophotometry of an S-type object. 2026 QQ$_8$ is Earth's third discovered otemporarily-captured companion on a flyby orbit, and the first long-duration one, owing this to being on the so-called "orbit of maximum lunation". Its unusual orbit lies close to the theoretical upper duration limit of an object captured in the Earth-Moon system, and has now been observed for the first time.

</details>

## High-energy astrophysics

### [Modelling scintillation in Fast Radio Bursts](https://arxiv.org/abs/2611.27527)
*L. Nicotera, T. Sprenger, O. Wucknitz et al.* · `astro-ph.HE` · arXiv:2611.27527v1 · relevance 0.17

- **In one sentence**: Simulation-based study of how reliably the scintillation bandwidth (nu_s) of fast radio bursts can be recovered from frequency autocorrelation functions under finite observing bandwidth, including tests of the finite scintle error prescription and an application to Effelsberg UBB data of FRB 20240114A.
- **In plain words**: Fast radio bursts are millisecond flashes of radio waves from distant galaxies. As they travel through clumpy gas, their radio spectra get a pattern of bright and dim patches, like ripples of light through water. This paper asks how accurately the typical size of those patches can be measured when only a few of them fit inside the receiver's frequency window, and it tests the methods using simulations and one repeating burst.
- **Why it matters**: The patch size tells us about the scattering material along the line of sight, so getting it right matters for interpreting the environment of these sources. The text reports that averaging several correlation measurements and bootstrap resampling help when there are few patches, but the broader implications are not claimed beyond the repeater analysis.
- **Background needed**: - Fast radio burst (FRB): a very brief, very bright radio flash from outside our galaxy; repeaters emit more than once.
- Scintillation: intensity changes caused by turbulence in the ionised gas between us and the source, similar to twinkling stars.
- Scintle: one bright patch in the scintillation pattern across frequency.
- Scintillation bandwidth (nu_s): the typical frequency width of one patch; it is linked to how strongly the gas scatters the signal.
- Autocorrelation function (ACF): a curve showing how similar a spectrum is to a shifted copy of itself; its width gives nu_s.
- Lorentzian profile: the expected bell-like shape of an ACF from ideal scintillation.
- Bootstrap resampling: estimating uncertainty by repeatedly resampling the data.
- Finite scintle error (FSE): an empirical uncertainty prescription for cases with limited numbers of scintles. · level: research-level

<details><summary>Original abstract</summary>

Fast Radio Bursts (FRBs) are bright, ms-duration, extragalactic radio transients. Propagation through inhomogeneities in the ionised medium produces scintillation, observed as frequency-dependent intensity variations in their spectra, with bright patches, called scintles. The characteristic scintillation bandwidth probes scattering material along the line of sight. Measuring this scale can be challenging when the observing bandwidth of the burst spectra contains a few scintles. We study the uncertainties associated with recovering $\nu_s$ from frequency autocorrelation functions (ACFs) under finite-bandwidth conditions. We examine the recovery of $\nu_s$ from individual ACFs and investigate if averaging multiple independent ACFs provides a more robust measurement. Using simulations, we reproduce observational conditions to investigate the modelling of scintillation in ACFs and the associated measurement uncertainties. We use these simulations to test the finite scintle error (FSE) prescription and assess its applicability to real observations. We test the resulting modelling framework on Effelsberg Ultra Broad Band receiver observations of the repeating FRB 20240114A. As the number of scintles decreases, individual ACFs develop fluctuations that deviate from the expected Lorentzian profile. This results in increased scatter in the recovered $\nu_s$ and a less reliable FSE prescription. Averaging multiple independent ACFs mitigates these effects and improves the recovery of $\nu_s$ in the low-scintle regime. Our results provide a framework for ACF modelling and uncertainty estimation in FRBs. For individual bursts, the FSE is effective with sufficient scintles; we find $\eta = 0.055$ more suitable for FRB analysis and update the FSE accordingly. For repeaters, averaging multiple ACFs and bootstrap resampling improve the recovery and uncertainty estimation of $\nu_s$.

</details>

### [From Binary Wind to Radio Burst: Dispersion-Measure Evolution after Accretion-induced Collapse](https://arxiv.org/abs/2611.26696)
*Smadar Naoz, Victoria M. Kaspi* · `astro-ph.HE` · arXiv:2611.26696v1 · relevance 0.13

- **In one sentence**: An angle-dependent toy model of aspherical accretion-induced white-dwarf collapse ejecta expanding through a binary wind bubble and surrounding gas, tracking how the dispersion measure of repeating fast radio bursts evolves with time for diffuse and compact environments.
- **In plain words**: Some repeating fast radio bursts (brief, bright flashes of radio waves from distant galaxies) show their dispersion measure, a number that tracks how much charged plasma the signal passes through, slowly changing over years. This paper asks whether a white dwarf that collapses into a neutron star, after pulling matter from a companion star, could produce such changes. The authors modeled the expanding debris moving through a lopsided, shell-like cloud of gas and found that in initially neutral gas the shock-heated plasma can make the dispersion measure rise after roughly 10 to 20 years, while in ionized gas it generally falls or levels off.
- **Why it matters**: Secular changes in dispersion measure are one of the few observable clues about the immediate surroundings of repeating fast radio bursts, so a model that predicts both signs of change could help test competing explanations. The text is a toy model with chosen parameters and does not fit any real source, so its relevance to actual observations remains to be shown.
- **Background needed**: - Fast radio bursts (FRBs): millisecond radio flashes from extragalactic sources; some repeat.
- Dispersion measure (DM): the integrated amount of free electrons along the line of sight; it shifts the arrival time of lower-frequency radio waves, and changes in it signal changing plasma near the source.
- White dwarf: a dense, Earth-sized remnant of a Sun-like star. Accretion-induced collapse (AIC): a white dwarf gaining mass from a companion until it collapses, likely into a neutron star.
- Ejecta and wind bubble: material thrown out by the collapse, and the cavity carved by the star's earlier wind; shock fronts where fast material hits slower gas heat and ionize it.
- Ionized vs. neutral gas: whether the surrounding gas already has free electrons; shocks can create new ones in neutral gas.
- Toy model: a simplified, idealized calculation meant to show qualitative behavior rather than match specific data. · level: research-level

<details><summary>Original abstract</summary>

Secular changes in the dispersion measures (DMs) of repeating fast radio bursts probe the source-local plasma. Such DM time variability has been interpreted with spherical, single-density-profile models. Accretion-induced collapse (AIC) of a white dwarf may instead follow binary interaction and occur inside a finite, anisotropic circumstellar structure. Here, we construct an angle-dependent toy model of aspherical AIC ejecta propagating through a pre-AIC free wind, shocked-wind bubble, swept-up external shell, and polar cavity, exploring a diffuse environment (number density of $1~{\rm cm^{-3}}$, located at $10~$pc) and a compact cloud (number density of $500~{\rm cm^{-3}}$, located at $0.3~$pc), bracketing ionized and initially neutral upstream gas. The unshocked ejecta initially yield ${\rm DM}\propto t^{-2}$, while crossings of the finite wind-bubble interfaces produce breaks and curvature in ${\rm DM}(t)$. In initially neutral models, shock ionization can overcome geometric dilution: the total DM reverses from decline to growth after approximately $10$--$20$ yr and later turns over as the finite reservoir is processed. Ionized-upstream models instead generally decline or flatten. Without fitting individual sources, our models span both signs and the approximate magnitudes of the secular DM-variation rates measured among repeaters. In this dynamical framework, DM evolution is set by shock propagation through the circumsource density and ionization structure, rather than the contemporaneous burst rate, distinguishing it from photoionization-driven scenarios. Consequently, in our model, an instantaneous \(d{\rm DM}/dt\) is not a unique indicator of source age. We suggest that the observed distribution of secular DM variation slope amplitudes and signs will be important for distinguishing among different models of DM variations in repeating FRBs.

</details>

## Stars and the Sun

### [Characterisation of B-type stars in four young Galactic open clusters. II. Photometric variability with TESS and identification of pulsating stars](https://arxiv.org/abs/2611.27680)
*Federica Nardini, Dominic M. Bowman, Julia Bodensteiner et al.* · `astro-ph.SR` · arXiv:2611.27680v1 · relevance 0.14

- **In one sentence**: Photometric study with TESS full-frame images of 82 early B-type stars in five young Galactic open clusters (ages 15-30 Myr), classifying pulsators (notably beta Cephei stars, 29 in total), Be stars, and binarity.
- **In plain words**: This paper looks at 82 hot, massive young stars in five loose star groups in our Milky Way galaxy. Using brightness measurements from NASA's TESS space telescope, the authors tracked how each star's light rises and falls over time. Most of the stars with usable data turned out to pulsate, meaning their surfaces swell and shrink rhythmically, and many were also checked for hidden partner stars.
- **Why it matters**: The work suggests that pulsation is common among young massive stars, and that it does not much hide the presence of close companion stars when they are detected by their wobbling motion, except in Be stars. Its importance rests on how well these clusters' ages and compositions are known, so it is a measured contribution to understanding massive-star evolution rather than a sweeping result.
- **Background needed**: - B-type stars: hot, luminous, massive stars, a few to tens of times the Sun's mass.
- Open cluster: a group of stars born together from the same cloud, so they share an age and roughly the same composition.
- TESS: a NASA space telescope that records brightness over time across large sky areas.
- Light curve: a record of how a star's brightness changes over time.
- Pulsation: rhythmic expansion and contraction of a star's outer layers, seen as regular brightness changes.
- Beta Cephei star: a class of massive pulsating stars.
- Be star: a B-type star with a surrounding disc of gas, often rapidly spinning.
- Spectroscopic binary: two stars orbiting each other, detected by the back-and-forth shifts in the light's spectrum; the 20 km/s figure is the speed-change threshold used to flag them.
- This is Part II of a series; Part I is not described in the text provided. · level: research-level

<details><summary>Original abstract</summary>

Pulsations and binarity are important properties of massive stars and influence their structure and evolution. Young open clusters are ideal laboratories to study massive stars, since they are mostly coeval and chemically homogeneous. We analyse 82 B-type stars in the Galactic open clusters $h$ and $\chi$ Persei, NGC 457, NGC 581, and NGC 1960, which have ages between 15 and 30 Myr. We extract light curves using both simple aperture photometry and a point-spread-function-based method that minimises contamination from crowded fields in full-frame images from the Transiting Exoplanet Survey Satellite (TESS) mission. We successfully extract light curves for 63 stars. The majority have photometric variability caused by pulsations, showing how pulsations are a common property of young B-type stars in clusters. We classify stars into different pulsator types based on their spectral type and frequency spectrum. The most common pulsator class are beta Cephei stars, with 29 stars in total, and we discover pulsation modes in almost all stars with a spectral type of B2 or earlier. All Be stars show pulsations, which supports the consensus of the ubiquity of pulsations in these stars. Finally, we confirm that the majority of early B-type stars are in binary systems, except for two pulsating Be stars and a star with rotational modulation. This indicates that pulsations do not significantly bias the spectroscopic detection of short-period binaries, except for Be stars where the spectroscopic radial velocity variability threshold should be higher than the typical value of 20 km s$^{-1}$.

</details>

### [Accretor Luminosity as Probe of Orbital Evolution and Magnetic Braking in AM CVn Binaries](https://arxiv.org/abs/2611.26973)
*Tin Long Sunny Wong, Peter Scherbak, Jim Fuller* · `astro-ph.SR` · arXiv:2611.26973v1 · relevance 0.05

- **In one sentence**: Uses the cooling luminosity of the white dwarf accretor in AM CVn binaries as a probe of orbital evolution, testing whether magnetic braking of the donor (in several formalisms, including CARB for the evolved CV channel) can explain observed accretor brightness at long orbital periods.
- **In plain words**: AM CVn systems are pairs of stars orbiting very closely, where a dense dead star (a white dwarf) pulls helium-rich gas off a companion. The authors look at how bright the white dwarf is at different orbital periods, since that brightness reveals how fast the pair is spiralling together. Observed white dwarfs look younger (brighter) than predicted when only gravitational-wave energy loss is assumed, so they test whether an extra drag from magnetic braking of the donor star fits better.
- **Why it matters**: It offers a new way to use the faint glow of a white dwarf to test how binaries lose orbital energy, a question that affects predictions for gravitational-wave sources. The text says the results show which magnetic braking models fit and which do not, and it suggests UV spectroscopy and better white dwarf atmosphere models as next steps; how far these conclusions generalise beyond AM CVn systems is not addressed in the text.
- **Background needed**: - White dwarf: the dense, cooling remnant of a Sun-like star; its brightness falls as it cools with age.
- AM CVn binary: an ultracompact pair with orbital period under about 70 minutes, where a white dwarf accretes helium-rich material from a semidegenerate donor.
- Orbital period and mass transfer: as the pair loses orbital energy it shrinks and speeds up; as it widens, mass transfer slows and the accretor cools.
- Gravitational-wave emission: the energy loss from orbiting masses that shrinks the orbit; it is the baseline model here.
- Magnetic braking: a magnetised, wind-carrying star loses angular momentum, adding extra orbital shrinkage. Several formalisms (Rappaport 1983, Matt 2015, CARB) are compared.
- Evolved cataclysmic variable (CV) channel: one of the proposed formation routes for AM CVn systems, alongside the white dwarf and helium star channels. · level: research-level

<details><summary>Original abstract</summary>

AM CVn binaries are ultracompact systems with orbital periods $P_{\rm orb} \lesssim 70$ min, where a white dwarf accretes from a He-rich semidegenerate donor. At short orbital periods ($P_{\rm orb} \lesssim 20$ min), rapid accretion reheats the accretor. As the system widens and the mass transfer rate decreases, the accretor follows standard white dwarf cooling at longer orbital periods ($P_{\rm orb} \gtrsim 30$ min). The accretor cooling luminosity then acts as a powerful probe into the orbital evolution of the binary. Recent observations show that the accretor appears brighter (younger) at long orbital periods, compared to models where orbital angular momentum loss is solely set by gravitational wave emission. We show that additional angular momentum loss, which we ascribe to magnetic braking of the donor, can better reproduce observations of accretor luminosity. We test and constrain various proposed magnetic braking formalisms, for the white dwarf, helium star, and evolved cataclysmic variable (CV) channels for AM CVn formation. None of the magnetic braking formalisms in their original form can reproduce the observations, but the widely popular magnetic braking proposed by Rappaport et al. 1983 boosted by a factor $\approx 5$, or the saturated magnetic braking proposed by Matt et al. 2015 boosted by a factor of $\approx 150$, yields satisfactory results. We also find that the CARB formalism, recently applied to the evolved CV channel, is strongly in tension with observations of accretor luminosity. Our models motivate UV spectroscopy observations, and dedicated WD atmosphere models for AM CVn accretors.

</details>

## Chemical physics

### [Molecular structure breaks universality in screening behavior of electrolyte solutions](https://arxiv.org/abs/2611.27955)
*Anna T. Bui, Connie J. Fairchild, Dominic P. W. Thomas et al.* · `cond-mat.stat-mech` · arXiv:2611.27955v1 · relevance 0.13

- **In one sentence**: Using machine-learned classical density functional theory, the authors compute decay lengths of electrolyte screening across several solvent and ion models and find that molecular detail breaks the apparent universal scaling seen in concentrated electrolytes.
- **In plain words**: Salt water shields electric charges so that their pull fades over a certain distance, called the screening length. Experiments on concentrated salt solutions have suggested that this length follows one common pattern regardless of the salt, and this paper asks whether that pattern holds once the shapes and interactions of the solvent and ions are modelled in detail. The authors report that it does not: the molecular details change how the screening fades, so no single rule covers all the models they tested.
- **Why it matters**: The result bears on a debate about whether concentrated electrolytes show "anomalous underscreening," which matters for batteries, colloids and biological fluids. The text does not show how far the findings extend beyond the model systems studied, so the connection to real experiments remains a question the paper itself raises rather than settles.
- **Background needed**: - Electrolyte: a liquid containing dissolved ions (charged atoms or molecules), such as salt in water.
- Screening length: the distance over which an electric charge's effect is cancelled out by nearby ions; a shorter length means stronger shielding.
- Debye–Hückel theory: the classic, simple theory of screening that works for dilute solutions.
- Universality: the idea that very different systems follow the same scaling law once measured in the right way.
- Underscreening: when a salt solution shields charge less well than the classic theory predicts.
- Classical density functional theory: a statistical method for computing how particle densities arrange themselves near charges; "machine-learned" means part of it was learned from data.
- Decay mode: the way correlations fade with distance, for example monotonically (steadily) or with oscillations. · level: research-level

<details><summary>Original abstract</summary>

Electrostatic screening is one of the most fundamental phenomena in electrolyte solutions. While dilute electrolytes are described by the universal Debye--H\"uckel theory, recent experiments have reported an apparently universal scaling law for screening lengths in concentrated electrolytes, fueling ongoing debate over anomalous underscreening. Yet, liquid state theory has been unable to determine whether molecular details of the solvent, the ions, or both should preserve or break such universality. Using machine-learned classical density functional theory, we compute numerically exact decay lengths across a hierarchy of electrolyte models of increasing molecular complexity. We find that molecular details qualitatively reshape screening: solvent attraction generates a new monotonic decay mode, solvent polarity produces re-entrant behavior, and ionic structure alone can drastically alter screening-length exponents. Consequently, no single scaling law describes screening universally across these molecularly distinct electrolytes. Our results challenge equilibrium interpretations of experimentally observed universality in concentrated electrolytes.

</details>

### [Length and Sequence-Dependent Dipolar and Electronic Properties of $\alpha$-helical Polypeptides](https://arxiv.org/abs/2611.26892)
*Faezeh Shabani, Florian G\"unther, Sibylle Gemming* · `physics.chem-ph` · arXiv:2611.26892v1 · relevance 0.05

- **In one sentence**: A density-functional tight-binding study of how chain length and residue chemistry set the dipole moment and frontier orbital energies of polyalanine, leucine-modified and cysteine-capped lysine-containing alpha-helical polypeptides, including responses to external electric fields.
- **In plain words**: This paper uses computer simulations to ask how the length of a helical peptide chain and the kinds of amino acids along it change its electrical behaviour. The authors studied three families of short helices and found that longer chains gain a larger overall dipole, meaning a stronger built-in separation of positive and negative charge, with the aligned backbone carbonyl groups doing most of the work. Side-chain changes mainly alter electronic states locally, and applying external electric fields shifts the energy gap and mainly distorts the flexible ends rather than the helix core.
- **Why it matters**: Understanding how sequence and length tune a helix's electronic energy levels is relevant to designing peptide-based materials for bio-electronic interfaces, biosensors and electron-transfer systems. The text itself frames these as possible applications; it does not show any device built or tested, so the practical link remains speculative.
- **Background needed**: - Alpha-helix: a common coiled backbone shape of proteins, held together by hydrogen bonds between nearby residues.
- Polypeptide: a chain of amino acids linked end to end; here short synthetic model chains.
- Dipole moment: a measure of how unevenly charge is distributed in a molecule, like a tiny built-in magnet for electric charge.
- HOMO-LUMO gap: the energy difference between the highest occupied and lowest empty electronic levels; it roughly sets how easily a molecule's electrons are excited.
- Density-functional tight-binding: a fast, approximate quantum-mechanical simulation method suited to large molecules.
- Stark effect: shifting of energy levels by an electric field.
- Results come from computational modelling only; the abstract gives no experimental validation. · level: research-level

<details><summary>Original abstract</summary>

Helical polypeptides combine the chemical tunability of synthetic macromolecules with the highly ordered backbone architecture of natural proteins. Here, density-functional tight-binding calculations are used to determine how chain length and sequence chemistry govern the dipolar and electronic properties of three $\alpha$-helical polypeptide families: polyalanine [AAAAA]$_n$, leucine-modified [AAAAL]$_n$, and cysteine-capped, lysine-containing C[AAAAK]$_n$. Increasing chain length produces systematic shifts and splitting of the molecular orbital levels together with an approximately additive increase in the molecular dipole. Analysis of the C[AAAAK]$_3$ helix shows that aligned backbone carbonyl groups provide the dominant contribution to the macro dipole, whose growing electrostatic potential is consistent with an intrinsic Stark-like contribution to the length-dependent orbital-energy evolution. Side-chain and terminal modifications introduce localized perturbations to frontier electronic states while preserving this global backbone-driven trend. Residue-resolved frontier levels additionally form a staircase-like energy landscape along the helical scaffold: individual peptide units retain large local HOMO-LUMO gaps of approximately 5 eV, whereas spatially proximate hydrogen-bonded residues exhibit smaller inter-residue energy separations. Application of external electrostatic fields modifies the frontier-level separation in a direction-dependent manner and induces structural distortions predominantly near the flexible termini, while the helical core remains comparatively robust. By establishing these fundamental sequence-structure-property relationships, this work provides a foundational blueprint for the rational design of peptide-based biomacromolecules tailored for next-generation bio-electronic interfaces, biosensors, and artificial electron-transfer systems.

</details>

## Materials science

### [Designing Perovskites for Chemical Looping Hydrogen Production](https://arxiv.org/abs/2611.27580)
*Ivana Stani\v{c}i\'c, Alfred Juhlin Onbeck, Anders Hellman et al.* · `cond-mat.mtrl-sci` · arXiv:2611.27580v1 · relevance 0.10

- **In one sentence**: An autonomous active-learning loop (Wasserstein autoencoder plus deep-ensemble surrogate) searched perovskite compositions for hydrogen production capacity in chemical looping, and then ranked 20 candidates by cost, supply resilience and environmental/health impact.
- **In plain words**: Researchers wanted to find better solid materials for making hydrogen in a cyclic chemical process, where a metal-oxide-like material repeatedly gives up and takes back oxygen. There are too many possible mixtures of elements to test one by one, so they used a computer program that proposes new mixtures, learns from the results, and repeats. Over 50 cycles, the average hydrogen yield of the proposed materials rose from 0.41 to 2.05 mmol per gram, and the best reached about 2.65 to 2.99.
- **Why it matters**: It shows a way to speed up materials searches while also weighing price, supply and safety, which matters for practical deployment of cleaner hydrogen. The text does not report experimental validation or how far these computed values would hold up in a real reactor, so its practical impact is still uncertain.
- **Background needed**: - Perovskites: a family of crystal materials with a flexible structure whose elements can be swapped (A and B sites) to tune properties.
- Chemical looping: a cycle in which a solid material is reduced and then re-oxidized, here used to produce hydrogen from steam.
- Hydrogen production capacity (HPC): the amount of hydrogen produced per gram of material, in mmol per gram.
- Active learning: a loop where a model picks the next most informative experiments or calculations, then updates itself.
- Autoencoder: a neural network that compresses data into a smaller set of numbers and reconstructs it; the Wasserstein variant is a specific training method.
- Deep ensemble: many neural networks trained together whose spread gives a sense of uncertainty.
- Multi-objective ranking: choosing candidates by balancing several criteria at once, such as performance, cost and environmental impact. · level: research-level

<details><summary>Original abstract</summary>

Perovskites are promising materials for chemical looping hydrogen production (CLHP) due to their compositional flexibility and tunable redox properties. However, cation substitution opens a vast compositional space, making screening for new high-performing materials computationally demanding. Here, an autonomous active-learning framework combining a Wasserstein autoencoder (WAE) with a deep ensemble surrogate model was used to search for perovskites with a high hydrogen production capacity (HPC). In seven independent runs of 50 cycles, the mean HPC of the acquired compositions rose from 0.41 mmol H$_2$ g$^{-1}$ in the starting set to 2.05 mmol H$_2$ g$^{-1}$, and the best compositions reached 2.65-2.99 mmol H$_2$ g$^{-1}$. All runs enriched Sn on the B-site, mostly combined with Ti and with Mg, Ce, K and Y on the A-site. Twenty diverse candidates (2.22-2.84 mmol H$_2$ g$^{-1}$) were then selected by a multi-objective ranking that also accounts for raw-material price, supply resilience and potential environmental and health impacts. The approach links materials discovery with practical deployment constraints, and the methodology is transferable to other chemical looping processes.

</details>

### [Edge-dislocation interactions with sub 3 nm vacancy and interstitial clusters in FeCr alloys: Mechanisms, Obstacle strength and Fate](https://arxiv.org/abs/2611.27583)
*Layatmika Sahoo, Suchandrima Das* · `cond-mat.mtrl-sci` · arXiv:2611.27583v1 · relevance 0.09

- **In one sentence**: Molecular dynamics simulations of an edge dislocation passing through sub-3 nm vacancy and mixed Fe-Cr interstitial clusters in Fe-3Cr, Fe-5Cr and Fe-10Cr at 300 K, quantifying obstacle strength, survival, and the dispersed-barrier alpha values implied for low-dose hardening.
- **In plain words**: Metal alloys used in nuclear reactors get harder and more brittle under radiation, even at doses where microscopes show no visible damage. This paper uses computer simulations of atoms to study tiny clusters of missing or extra atoms, too small to see under a microscope, and how strongly they block the movement of dislocations (line-like defects whose motion makes metals soft). The authors find that vacancy clusters (missing atoms) are strong blockers that always survive, while most interstitial clusters (extra atoms) are weaker and usually get absorbed.
- **Why it matters**: Models of radiation hardening are usually fitted to defects visible in electron microscopes, so they may overstate how strong those visible defects are if invisible clusters contribute. The paper argues that earlier fitted strength values are inflated for this reason, which could matter for predicting the lifetime of reactor steels; the link to real materials is inferred from simulations and has not been tested here.
- **Background needed**: - Edge dislocation: a line defect in a crystal; its glide through the lattice is what makes metals deform.
- Obstacle strength: how hard a defect resists a passing dislocation; here reported in MPa and as a dimensionless alpha in hardening models.
- Vacancy / interstitial cluster: small groups of missing atoms or extra atoms in a crystal lattice, typically a few nanometres across.
- Dispersed-barrier hardening: a standard model where hardening scales with the square root of defect density times defect strength.
- Molecular dynamics (MD): simulating how atoms move according to interatomic forces, limited to very short timescales and small sample sizes.
- Fe-Cr alloys: iron with 3-10% chromium, a model for reactor structural steels.
- TEM (transmission electron microscopy): imaging technique that resolves defects only above a certain size. · level: research-level

<details><summary>Original abstract</summary>

Fe-Cr alloys harden at irradiation doses where transmission electron microscopy (TEM) shows no defects, implicating defects too small to be resolved. Their obstacle strength is unknown, so hardening models ignore them and fit measured hardening to visible defects alone. Here, molecular dynamics drives an edge dislocation through relaxed 1-3 nm vacancy and mixed Fe-Cr interstitial clusters in Fe-3Cr, Fe-5Cr and Fe-10Cr at 300 K. Vacancy clusters relax into platelets whose strength rises with size to about 350 MPa at 2.9 nm, following strong-obstacle scaling independently of Cr content, and always survive dislocation passage. Interstitial clusters relax into $\frac{1}{2}\langle 111 \rangle$, mixed or $\langle 100 \rangle$ loops. They are mostly weaker than platelets of the same size, their strength varies up to fivefold with the local Cr arrangement, and most are absorbed. Only $\langle 100 \rangle$ loops in Fe-5Cr and Fe-10Cr often survive. During pinning, Cr collects at the junction between these loops and the dislocation; atom tracking for one loop shows that more than half comes from the loop itself. Surviving loops are not stronger than absorbed ones: strength and survival are thus distinct. Computed dispersed-barrier strengths ($\alpha \approx$ 0.02-0.25) are upper bounds that lie below the $\alpha$ values obtained in earlier studies by fitting hardening to TEM-visible loops. These earlier values are therefore inflated by TEM-invisible defects. Wherever small vacancy clusters form, they are more effective obstacles than interstitial clusters of the same size. These defect-specific strengths and fates provide a physical basis for models of low-dose hardening.

</details>

## Soft matter and polymers

### [Decoupling Entropic and Enthalpic Elasticity in Crosslinked Polymer Nanocomposites](https://arxiv.org/abs/2611.27259)
*Chiranjit Majhi, Sivasurender Chandran, Krishnacharya Khare* · `cond-mat.soft` · arXiv:2611.27259v1 · relevance 0.09

- **In one sentence**: Temperature-dependent thermomechanical measurements separate the entropic and enthalpic parts of elasticity in crosslinked PDMS nanocomposites, finding that effective crosslink density rises with silica or titania loading and then saturates, with interfacial crosslink density dropping sharply below a critical interparticle spacing.
- **In plain words**: Rubbery materials stiffen when tiny particles are mixed into them, but it is unclear how much of that stiffening comes from energy stored in bonds versus the tendency of polymer chains to stretch into disordered shapes. This paper uses temperature-dependent tests on silicone rubber filled with silica or titania particles to split these two contributions apart. The authors report that at low particle loadings elasticity is mostly entropy-driven, while at higher loadings the energetic part matters more, and that particles packed close together limit the chains' stretching.
- **Why it matters**: Particle-filled elastomers are widely used, and the text suggests that the near-particle interface region, not just the bulk filler fraction, controls stiffness. The finding that particle clustering reduces entropic elasticity may help guide how nanocomposites are designed, though the text alone does not show how far the result transfers to other systems.
- **Background needed**: - Elastomer: a rubbery polymer network whose chains are joined at crosslinks, letting it stretch and snap back.
- Crosslink density: how many chemical joins link the chains; more joins usually means a stiffer network.
- Entropic elasticity: stiffness from chains resisting being stretched out of their disordered coiled state.
- Enthalpic elasticity: stiffness from energy changes in bonds and chain interactions, which can be measured by how stress shifts with temperature.
- Nanocomposite: a material with nanometre-scale filler particles (here silica and titania) dispersed in a polymer (here PDMS silicone).
- Volume fraction: the share of the material's volume taken up by the particles.
- Interparticle separation: the typical gap between neighbouring particles. · level: research-level

<details><summary>Original abstract</summary>

Nanoparticle-induced local interface regions significantly enhance the bulk mechanical behavior of polymer nanocomposites, yet their energetic contribution in crosslinked elastomer networks remains poorly understood. Here, we decouple the entropic and enthalpic contributions to the elasticity of crosslinked poly(dimethylsiloxane) nanocomposites using temperature-dependent thermomechanical measurements. While the measured bulk elastic modulus exhibits a monotonic increase with nanoparticle volume fraction $\phi_{\rm n}$, we observe that the effective crosslink density initially increases before saturating at larger $\phi_{\rm n}$. These results are independently validated across two nanoparticle systems (silica and titania) and directly confirmed by X-ray scattering experiments on silica-based composites, highlighting the generality of the observation. The trends in effective crosslink density indicate that the elastic response is predominantly entropy-driven at low nanoparticle concentrations, whereas enthalpic contributions become increasingly significant at higher loadings. Assuming a linear superposition of interface and bulk contributions, these results reveal that the effective crosslink density at the particle interface decreases by an order of magnitude below a critical mean interparticle separation, indicating that localized particle proximity and clustering constrain the entropic elasticity at higher loadings.

</details>

### [Lacrymaria-like dynamics: compression and length change in active slender bodies](https://arxiv.org/abs/2611.27577)
*Cl\'ement Moreau, Yukinori Nishigami, Johann H\'erault et al.* · `cond-mat.soft` · arXiv:2611.27577v1 · relevance 0.07

- **In one sentence**: A planar N-link model in which both bending angles and segment lengths are dynamical, coupled through resistive-force hydrodynamic drag, used to study how axial compression and extension alter the swimming and crawling of active slender filaments, including a Lacrymaria-inspired extensible neck.
- **In plain words**: This paper looks at tiny swimming or crawling threads, such as the neck of a single-celled organism called Lacrymaria olor, that can stretch and shorten as well as bend. The authors built a computer model where each piece of the thread can change length as well as angle, with water drag acting on it. They found that simply making the thread stretchy usually slowed it down, but when the length changes were driven in a timed rhythm, they could help, hinder, or change the direction of movement depending on timing and frequency.
- **Why it matters**: Most models of microscopic swimming treat filaments as unable to stretch, so this work tests whether length change matters, which the text suggests it can. Its link to Lacrymaria is a motivating example; the text does not show that the model explains that organism's behaviour in detail.
- **Background needed**: - Active filament: a flexible thread that generates its own bending or length-changing motion, like cilia or flagella.
- Elastohydrodynamics: the study of how elastic bodies deform and move through a viscous fluid such as water, where inertia is negligible.
- Resistive force theory: an approximation that treats the water drag on each small segment as a simple function of its velocity.
- N-link model: a thread represented as a chain of N rigid segments joined by hinges, here with adjustable lengths.
- Compressibility: the ability of a body to shorten or lengthen under force.
- Lacrymaria olor: a single-celled protist with a long, extensible neck used for hunting and exploring.
- Follower force: a force that keeps turning with the body's orientation, used to drive the filament's oscillation. · level: research-level

<details><summary>Original abstract</summary>

Length change is central to the behaviour of many active slender bodies, yet most elastohydrodynamic models of microscopic locomotion treat filaments as effectively inextensible. Here we introduce a compressible $N$-link formulation for planar active filaments, in which both bending angles and segment lengths are dynamical variables coupled through local hydrodynamic drag, modelled using resistive force theory. We first use the model to test whether passive extensibility can improve bending-driven swimming and crawling. Across the parameter ranges studied, passive compressibility usually reduces locomotion speed, indicating that axial compliance alone is not a robust mechanism for propulsion enhancement. We then prescribe active rest-length waves and show that compression can either enhance, suppress, or redirect locomotion depending on its phase, wavelength, and frequency relative to bending. Finally, motivated by the extensible neck dynamics of \textit{Lacrymaria olor}, we apply the method to clamped and free filaments driven by oscillatory follower forces. These examples show that elastic compression-bending coupling can reorganise swimming, exploration, and locomotion in strongly deforming active filaments.

</details>

## AI for chemistry and materials

### [Beyond the Ground State: Assessing the Machine-Learned Skala Functional in {\Delta}SCF Calculations of Molecular Excitation Energies](https://arxiv.org/abs/2611.27711)
*Egor Trushin, Thomas D. K\"uhne* · `physics.chem-ph` · arXiv:2611.27711v1 · relevance 0.18

- **In one sentence**: This paper tests whether the machine-learned Skala exchange-correlation functional, trained mainly on ground-state energetics, transfers to molecular excitation energies and singlet-triplet gaps computed with the ΔSCF approach, compared against PBE, r²SCAN and PBE0.
- **In plain words**: Computer models of molecules often need an energy term that is hard to write down exactly, called the exchange-correlation functional. This paper checks whether a newer version learned from data, called Skala, still works well when asked about excited states, meaning molecules that have absorbed light and moved an electron to a higher energy level. The authors compare it with three established methods on several sets of molecules.
- **Why it matters**: Skala was built for ground-state energies, so asking whether it carries over to excited states is a fair test of how far machine-learned chemistry models generalize. The results are mixed: Skala does best on some tasks but not others, and it gives negative singlet-triplet splittings for several molecules under one setup, so it is a cautious result rather than a clear win.
- **Background needed**: - Ground state: the lowest-energy arrangement of a molecule's electrons; excited states are higher-energy arrangements, often reached by absorbing light.
- Exchange-correlation functional: the approximate term in density functional theory (DFT) that accounts for how electrons interact; its choice largely sets the accuracy of the calculation.
- Machine-learned functional: a functional whose form was fitted to data rather than derived by hand. Skala is one such functional.
- ΔSCF (delta self-consistent field): a method that estimates an excitation energy as the difference between the total energies of two separately optimized electron configurations.
- Singlet and triplet states: spin states of a molecule; the singlet-triplet gap is the energy difference between them.
- UKS / ROKS: two ways of handling electron spin in open-shell calculations (unrestricted vs. restricted open-shell Kohn-Sham).
- MAE (mean absolute error): the average size of the error against reference values; lower is better.
- PBE, r²SCAN, PBE0: established functionals of increasing complexity used here as baselines. · level: research-level
- Matched keywords: molecule, molecular

<details><summary>Original abstract</summary>

We assess the transferability of the machine-learned Skala exchange-correlation (XC) functional beyond ground-state energetics using molecular vertical excitation energies and singlet-triplet gaps calculated with the $\Delta$-self-consistent-field ($\Delta$SCF) approach. We compare Skala with PBE, r$^2$SCAN, and PBE0 on subsets covering small-molecule excitations (QUEST1), inverted singlet-triplet gaps (ST-gap), and intramolecular charge-transfer excitations (QUEST6). Both spin-unrestricted Kohn-Sham (UKS) and restricted open-shell Kohn-Sham (ROKS) formalisms are considered. On QUEST1, Skala achieves the lowest mean absolute errors (MAEs) for singlet and triplet excitation energies with both formalisms, although PBE0 and r$^2$SCAN provide more accurate singlet-triplet gaps through error cancellation. For ST-gap, Skala yields the lowest gap MAEs with both UKS and ROKS. Evaluating the mixed-spin and triplet energy components on the same orbitals optimized for the ROKS open-shell singlet yields negative splittings for seven of eight ST-gap molecules with Skala. Separate triplet optimization increases the gaps, but six remain negative. All three conventional functionals give positive common-orbital splittings and optimized gaps for all eight molecules. For QUEST6, treated with UKS only, Skala yields more accurate singlet excitation energies than PBE and r$^2$SCAN but remains less accurate than PBE0. Across QUEST1 and ST-gap, Skala yields lower MAEs with UKS than ROKS. Overall, these results support Skala's transferability to molecular excited states while highlighting its dependence on the excitation class and open-shell treatment.

</details>

### [Prediction of lattice thermal conductivity of half-Heusler compounds by machine learning and transfer-function calibration](https://arxiv.org/abs/2611.26788)
*Shivam Randive, Ojaswini Randive, Heet Lungaria et al.* · `cond-mat.mtrl-sci` · arXiv:2611.26788v1 · relevance 0.15

- **In one sentence**: The paper quantifies a systematic overestimate of calculated versus measured lattice thermal conductivity across 18-valence-electron cubic half-Heusler compounds and corrects it with a temperature-dependent transfer function combined with a machine-learning model.
- **In plain words**: Researchers screening materials for heat-to-electricity conversion often estimate how well a material conducts heat through its crystal lattice using computer calculations. Those calculations describe a perfect single crystal, while lab measurements use real polycrystalline samples where grain boundaries and defects block heat, so the calculated values tend to be too high. This paper measures that gap across a whole family of compounds and proposes a correction that brings predictions closer to measured values.
- **Why it matters**: Screening studies that rank candidate thermoelectric materials depend on these heat-conduction estimates, so a known, systematic bias matters for which compounds get picked. The method is validated on withheld chemistries, but the text does not establish how well it transfers beyond this compound class.
- **Background needed**: - Thermoelectric materials convert heat differences into electricity; good ones conduct electricity well but conduct heat poorly.
- Lattice thermal conductivity is the part of heat conduction carried by atomic vibrations (phonons) in the solid's crystal framework.
- Half-Heusler compounds are a class of crystalline materials with three elements in a fixed ratio; "18 valence electrons" refers to the count of outer-shell electrons per formula unit, which groups them by bonding type.
- First-principles calculations solve quantum-mechanical equations for an idealized perfect crystal, with no defects.
- Polycrystalline samples are made of many small grains; grain boundaries and point defects scatter heat-carrying vibrations.
- A transfer function here is a simple empirical correction mapping calculated values onto measured ones, fitted to data.
- Machine-learning models are trained on existing data to predict a property from crystal structure. · level: research-level
- Matched keywords: crystal structure

<details><summary>Original abstract</summary>

High-throughput searches for half-Heusler thermoelectrics increasingly rely on lattice thermal conductivity ($\kappa_L$) from first-principles calculations, or from machine-learning models trained on them. These calculations describe an ideal single crystal, whereas measurements are made on polycrystalline samples, in which grain boundaries and defects scatter heat as well. The resulting gap between calculated and measured $\kappa_L$ has been noted for individual compounds but not, to our knowledge, quantified across a materials class, so the values used for screening carry an unknown, systematic bias. Here we quantify and correct this bias for cubic half-Heusler compounds with 18 valence electrons. Using a curated literature corpus that keeps calculated and measured values apart, we show that calculations overestimate measured $\kappa_L$ in most bonding families, and that the excess shrinks with temperature. Scattering by defects, added to the intrinsic scattering between lattice vibrations, would give such a trend, but the data do not single out one cause. A simple transfer function with this temperature dependence removes the median offset, and refitting its magnitude within a bonding family lowers the median error further, though not consistently compound by compound. Combined with a machine-learning model that predicts the calculated value from crystal structure, and tested on chemistries withheld from all fitting, the method predicts measured $\kappa_L$ in this class about as closely as independent laboratories agree with one another, and provides testable predictions for compounds not yet measured.

</details>

## Biochemistry

### [RUBRIC: rapid quality assessment tool for RNA 3D structures](https://www.biorxiv.org/content/10.64898/2026.11.20.767675v1)
*Dewan, K. J.; Yesselman, J. D.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.20.767675 v1 · relevance 0.08

- **In one sentence**: RUBRIC is an open-source tool that annotates RNA base pairs and checks their geometry, ribose sugar puckers and backbone conformations in 3D RNA structural models, flagging ambiguous or distorted features.
- **In plain words**: Cryo-electron microscopy now produces very large RNA molecule models quickly, but the checks used to catch errors in those models have not kept up. This paper presents RUBRIC, a free program that examines each RNA base pair, sugar ring and backbone segment, and flags shapes that are distorted or cannot be clearly classified. The authors report that it processes a complete human ribosome in under a second and that its base-pair labels mostly agree with established annotation programs.
- **Why it matters**: Errors in deposited RNA structures can propagate into the databases used to train and test structure prediction methods, so better validation could matter for both structural biology and computational modelling. The text reports that flagged problems were reduced in higher-resolution models or after targeted refinement, but its wider impact on the PDB is not yet shown.
- **Background needed**: - RNA is a chain of nucleotides; each has a sugar (ribose), a phosphate backbone and a base.
- Base pairs are hydrogen-bonded partner bases; Leontis-Westhof classes describe how the two bases pair geometrically.
- Ribose "pucker" is the puckered shape of the sugar ring; backbone "suites" describe conformations of the chain between sugars.
- Cryo-EM is an imaging method that yields 3D molecular models at near-atomic detail; "resolution" indicates how fine the detail is (lower numbers are better).
- The PDB (Protein Data Bank) is the public archive of deposited 3D structures.
- Validation means automated checks that find implausible geometry before a model is published or reused. · level: research-level

<details><summary>Original abstract</summary>

Cryo-electron microscopy has transformed RNA structural biology, revealing increasingly large and complex structures at an unprecedented pace. However, validation methods have lagged behind, and deposited models can contain distorted base pairs, incorrect ribose puckers and backbone conformational outliers. Here, we introduce Rapid Unified Base-pair, Ribose and backbone Integrity Check (RUBRIC), an open-source program that combines RNA structural annotation with local validation of base pairs, sugars, and backbones. RUBRIC assigns Leontis-Westhof classes and identifies geometrically ambiguous pairs that cannot be confidently assigned to a single class. It scores unambiguous pairs against reference geometries for each type and class, identifying the parameters responsible for low scores. It also assigns backbone suites to known conformers, suggests target torsions for unassigned suites and flags incorrect ribose puckers. RUBRIC analyzes a complete human ribosome in under a second, with base-pair detection and classification consistent with leading annotation programs. These programs disagreed significantly more often on pairs RUBRIC flagged as ambiguous than on unambiguous pairs. The geometric problems flagged by RUBRIC were reduced in higher-resolution models of the same RNA or after refinement targeting the affected geometry, indicating that these problems are correctable. A PyMOL plug-in and machine-readable output support model building, correction before deposition and assessment of deposited structures before reuse. RUBRIC can therefore help improve RNA structures in the PDB and the datasets used to train and evaluate RNA structure prediction methods.

</details>

### [A cytochrome P450 is essential for cardenolide biosynthesis in Chrysolina beetles](https://www.biorxiv.org/content/10.64898/2026.11.19.767920v1)
*Xu, H.; Stathaki, A.; Florean, M. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.19.767920 v1 · relevance 0.06

- **In one sentence**: A cytochrome P450 enzyme from the leaf beetle Chrysolina coerulans, CcCYP9Z273, converts pregnenolone to caraumbellogenin via C14-hydroxylation, an early step in beetle cardenolide biosynthesis, and one active-site residue controls whether C14 or C15 hydroxylation occurs.
- **In plain words**: Some beetles make cardenolides, chemicals related to the heart drug digitoxin, to defend themselves. This paper identifies an enzyme in one leaf beetle species that performs an early chemical step in making these compounds. Silencing the gene for the enzyme reduced the beetle's cardenolide production, and tracing labeled molecules suggested the product it makes, caraumbellogenin, is a real intermediate on the route.
- **Why it matters**: Cardenolides have been studied in plants for a long time, but how insects make them was not known, so this identifies a missing step. The finding that insects and plants use different enzyme families to reach a shared intermediate is of interest to researchers in natural product chemistry and drug-related biosynthesis, though the text does not show direct medical applications.
- **Background needed**: - Cardenolides: steroid-based defensive chemicals, also the class of compounds that includes digitoxin, a heart medicine.
- Steroid backbone: the four-ring carbon skeleton shared by cholesterol and related molecules; pregnenolone is an early member of this family.
- Cytochrome P450: a large family of enzymes that add oxygen to molecules, often at specific carbon positions.
- Hydroxylation: adding an –OH group to a carbon atom; C14 and C15 refer to specific carbon positions on the steroid ring.
- Biosynthetic intermediate: a molecule formed along the way to a final product.
- Gene silencing: switching off a gene to see what happens to the organism's chemistry.
- Isotope tracing: feeding labeled atoms to an organism to track which molecules are made from which.
- Active-site residue: an amino acid lining the enzyme's reaction pocket that shapes which reaction it favors. · level: research-level

<details><summary>Original abstract</summary>

Cardenolides are naturally occurring steroidal derivatives that function as chemical defense compounds. These natural products are also widely used in medicine, as exemplified by the use of digitoxin in treating cardiac disease. Although cardenolides are most widely known as plant-derived natural products, these compounds are also produced in certain beetle species. However, while the biosynthesis of cardenolides has been well-studied in plants, it is not known how insects produce these compounds. Here we report the identification of a cardenolide biosynthetic enzyme from the leaf beetle Chrysolina coerulans. This cytochrome P450, CcCYP9Z273, catalyzes an array of steroid oxidations, including the conversion of pregnenolone into caraumbellogenin through C14-hydroxylation. Gene silencing suggests that CcCYP9Z273 is essential for beetle cardenolide formation and isotope tracing experiments support caraumbellogenin as an on-pathway biosynthetic intermediate. Mutagenesis of CcCYP9Z273 identifies an active-site residue that controls the enzyme product selectivity between C14- and C15-hydroxylation. These findings establish an early step in beetle cardenolide biosynthesis and highlight how distinct enzyme families have been recruited in insects and plants to generate a shared intermediate in the biosynthesis of these important metabolites.

</details>

## Pharmacology and drug discovery

### [Evaluation of sources of variability in a TEER (trans-epithelial/endothelial electrical resistance) system](https://www.biorxiv.org/content/10.64898/2026.11.06.764605v1)
*Gutierrez, R.; Lund, S.; Reipa, V. et al.* · `pharmacology and toxicology` · bioRxiv doi:10.64898/2026.11.06.764605 v1 · relevance 0.03

- **In one sentence**: A case study of a chamber-based TEER system used with a gut co-culture model, analyzing 23 twenty-two-day experiments to separate within-run from run-to-run variability using Bayesian analysis and correlation of control measurements.
- **In plain words**: Scientists grow layers of cells on small porous inserts and measure how electrically resistant the layer is, as a way to check that it forms a tight barrier. This paper asks how much of the variation in those readings comes from within a single test session versus from one session to the next. The authors found that variation within a session was small, but differences between sessions, even ones run hours apart on the same day, were larger.
- **Why it matters**: Barrier measurements like this are used in drug testing and bioassays, so knowing where the noise comes from helps decide how results should be compared and analyzed. The text suggests the methods could be applied to other TEER measurements, though its scope is a single case study.
- **Background needed**: - TEER (trans-epithelial/endothelial electrical resistance): an electrical resistance reading across a cell layer; higher values generally indicate a tighter barrier.
- Cell inserts: small cup-like membranes on which cells are grown, letting researchers measure across the layer.
- Gut co-culture model: a lab model in which two cell types are grown together to mimic the intestinal lining.
- KCl and blank inserts: control measurements. KCl is a salt solution used as a reference reading; blank inserts have no cells and show the baseline.
- Run: a batch of plates measured in one session.
- Bayesian analysis: a statistical method that estimates how much each source of variation contributes, with uncertainty.
- Correlation: a measure of whether two sets of deviations move together; here, whether control deviations track model deviations within a run. · level: intermediate

<details><summary>Original abstract</summary>

Trans-epithelial/endothelial electrical resistance (TEER) measurements are a key nondestructive measurement of the barrier integrity of cells grown on inserts. To support the use of TEER measurements in bioassays, we have evaluated the sources of variability in a case study involving a chamber-based TEER system to assess a gut co-culture model. Data from 23 separate experiments, each lasting 22 d, were evaluated. Multiple lines of evidence suggested minimal variability within a run, a period during which several plates were analyzed sequentially. In contrast, run-to-run variability was substantially larger, even when two runs were performed several hours apart on the same day. Bayesian analysis of both KCl and blank insert data revealed that run-to-run variability was among the largest sources of variability, with relative uncertainty values of 3 % to 6 % of the mean value. Correlational analysis investigated whether deviations of KCl or blank insert TEER values within a run compared to long-term median values were correlated with deviations of the biculture gut model values within that same run from their long-term median values. Unexpectedly, the KCl values were not correlated, while the blank insert values had a weak correlation. We also evaluated the information gained from different control measurements. The findings from this study can influence how statistical analyses are performed on TEER results and can inform the design of robust TEER methods. For example, the approaches described here can be used to characterize variability within and among runs in TEER measurements for other methods.

</details>

## Computational and systems biology

### [Integrating CRISPRi perturbation responses and transcription-factor binding priors for regulatory network inference in triple-negative breast cancer](https://www.biorxiv.org/content/10.64898/2026.11.20.768082v1)
*Faroque, O.; Jannaty, M. H.; Abir, S. H. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768082 v1 · relevance 0.13

- **In one sentence**: An interventional gene regulatory network framework combining single-cell CRISPRi Perturb-seq data with ChIP-seq transcription factor binding priors, applied to enhancer loci in MDA-MB-231 triple-negative breast cancer cells, with benchmarking against GENIE3 and co-expression baselines and survival analysis in METABRIC and TCGA-BRCA cohorts.
- **In plain words**: Cancer cells run on networks of genes switched on and off by regulatory proteins that bind to switch-like DNA regions called enhancers. This paper tries to map those networks by actually switching genes off in cells (using CRISPR interference) and watching what changes, rather than only looking at which genes move up and down together. The authors report that their method predicted which gene-control links were real more accurately than two common comparison methods, and that some proteins, such as MYC and AP-1 family members, appear central to the network.
- **Why it matters**: Triple-negative breast cancer has few targeted drug options, so better maps of the control circuits driving it could help point toward candidate targets. The work is computational and the text reports predictions and retrospective associations only; the claimed candidate circuits still require experimental validation, which the authors themselves note is pending.
- **Background needed**: - Gene regulatory network: a map of which regulatory proteins (transcription factors) control which genes.
- Enhancer: a DNA region that boosts nearby gene activity; many are non-coding.
- CRISPRi (CRISPR interference): a way to switch off specific genes or regions, here paired with single-cell sequencing (Perturb-seq) to read out the effects in each cell.
- ChIP-seq binding priors: lab data showing where a protein physically sits on DNA, used to constrain which links are plausible.
- Co-expression correlation: genes that rise and fall together; often confounded, so it can produce false links.
- AUROC / AUPRC / FDR: standard measures of how well predicted links match held-out truth and how many false positives appear.
- SHAP: a method for explaining which inputs drove a machine-learning model's predictions.
- Survival cohorts (METABRIC, TCGA-BRCA): patient databases used to test whether a gene signature relates to outcome. · level: research-level

<details><summary>Original abstract</summary>

Triple-Negative Breast Cancer (TNBC) represents an aggressive breast cancer subtype that lacks actionable cell-surface receptors, restricting frontline systemic management to cytotoxic chemotherapy. While recent functional epigenomics shows that TNBC progression is governed by non-coding regulatory remodeling at distal super-enhancers, conventional Gene Regulatory Network (GRN) inference methods rely on observational transcriptomic co-expression, which suffers from technical dropouts and confounding correlations that inflate false discoveries (>30%). Here, we present an interventional network inference framework that integrates large-scale single-cell CRISPR-interference perturbation sequencing (Perturb-seq; GSE224986, 95,678 cells across 11,975 sgRNAs) with ENCODE Factorbook ChIP-seq physical transcription factor binding priors across 819 somatic mutation-associated enhancer loci in human TNBC (MDA-MB-231). Our pipeline reconstructed a tripartite network yielding 5,935 physical TF-enhancer edges, 383,757 functional enhancer-gene edges, and 542,760 unique TF-target gene functional pairs across 372 active enhancers. Topological centrality prioritized master transcriptional drivers governing TNBC oncogenic signaling, including CTCF, POLR2A, EP300, JUND, MYC, and FOS, which regulate Hallmark programs for Epithelial-Mesenchymal Transition (p = 1.2 x 10-9) and cell cycle progression. Explainable machine learning (SHAP TreeExplainer) revealed non-linear, thresholded transactivation dynamics for AP-1 and MYC. Quantitative benchmarking against held-out CRISPRi ground truth demonstrated strong discriminatory accuracy (AUROC = 0.8999, AUPRC = 0.8745, Precision = 90.13%, FDR = 9.87%), substantially outperforming GENIE3 (AUPRC = 0.6323, FDR = 35.73%) and co-expression correlation (AUPRC = 0.6814). In silico-simulated driver feature silencing correlated with experimental responses (R2 = 0.473, p < 10-122), and master driver signatures significantly stratified overall survival in the METABRIC (n = 320) and TCGA-BRCA (n = 160; p [&le;] 0.019) cohorts. Finally, in silico perturbation modeling indicated that multi-target epigenetic combinations achieved 93% topological disruption of oncogenic regulatory connectivity, nominating prioritized candidate circuits for experimental validation.

</details>

### [Predicted templates improve the prediction of antibody-antigen structures by AlphaFold 3 and Boltz-2](https://www.biorxiv.org/content/10.64898/2026.11.20.768078v1)
*Ziaee, O.; Lazou, M.; Joseph-McCarthy, D. et al.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.20.768078 v1 · relevance 0.12

- **In one sentence**: Adding rigid-body docking-generated templates from PIPER to AlphaFold 3 and Boltz-2 raises the rate of acceptable antibody-antigen complex predictions on a leakage-free benchmark.
- **In plain words**: Antibodies are immune proteins that bind to foreign targets (antigens), and computer tools still often fail to predict how the two fit together. This paper tests whether giving AI structure predictors a rough starting "template" of the pair, made by a cheaper traditional docking program called PIPER, helps them find the right shape. The authors report that this raised the share of cases with acceptable top predictions from 56.2% to 63.4% for AlphaFold 3, and that a similar gain appeared with Boltz-2.
- **Why it matters**: Antibody-antigen structures matter for drug and vaccine design, and the paper offers a fairly cheap way to improve predictions without massive sampling. The text reports benchmark gains only, so how far these results carry to real-world antibody design is not something it establishes.
- **Background needed**: - Antibody: an immune protein that binds a specific target; its binding site varies a lot between antibodies.
- Antigen: the molecule an antibody binds to.
- Protein structure prediction: using AI or computation to estimate a protein's 3D shape from its sequence.
- AlphaFold 3 and Boltz-2: AI models that predict structures of protein complexes.
- Rigid-body docking (PIPER): a traditional method that places two molecular shapes against each other without bending them; it is fast but less accurate.
- Template: a known or approximate structure given to a predictor as a starting guide.
- "Acceptable or better" models: a standard quality grade for predicted protein-protein complexes.
- Random seeds: different starting points for the AI's sampling; running many seeds is expensive.
- Leakage-free benchmark: a test set with no overlap with the data the AI was trained on, so results are not inflated. · level: research-level

<details><summary>Original abstract</summary>

Motivation: In spite of the much improved protein structure prediction methods, the success rate remains low for antibody-antigen complexes. While this can be improved by computationally demanding massive sampling, results are still much poorer than for most other types of protein-protein interactions. In principle, improvement can be achieved by using templates that are close enough to the native structure of the complex, but these are generally not available for antibody-antigen complexes. Results: We explore the use of templates, generated by the computationally inexpensive rigid body docking program PIPER. Applied to a leakage-free antibody-antigen benchmark set, standard AlphaFold 3 with 1000 random seeds yields acceptable or better models as the top predictions for 56.2% of complexes. Adding the PIPER generated templates in the unmasked version of AlphaFold 3 either increases the success rate to 63.4%, or reaches the same 56.2% success rate in about 200 runs. The template-based approach similarly improves antibody-antigen prediction by Boltz-2. This result demonstrates that the space explored by the ML based approach can be expanded by adding templates prepared by traditional docking, compensating for the lack of evolutionary relationship and the limited availability of training data. Availability and Implementation: The ClusPro server (https://cluspro.bu.edu/login.php) containing the PIPER program is free for non-commercial applications and the program is available by request (https://www.vajdalab.org/). All other study data are included in the article and/or supporting information.

</details>

## Neuroscience

### [Sex-dependent gating of astrocyte-driven nociceptive plasticity](https://www.biorxiv.org/content/10.64898/2026.11.18.767473v1)
*Klinger, L.; Uhrik, L.; Ravagnan, E. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.18.767473 v1 · relevance 0.08

- **In one sentence**: In rats, chemogenetic activation of distinct spinal astrocyte GPCR pathways produced synaptic depression or potentiation at nociceptive synapses in males but not females, and the female-specific gating was linked to hormonal status and extracellular matrix organization.
- **In plain words**: This study looks at how support cells in the spinal cord, called astrocytes, can change how strongly pain signals pass between nerve cells, and whether that effect differs between male and female rats. The researchers activated astrocytes with engineered receptors and found that this changed pain-signal connections in males but not in females. Still, females developed mechanical hypersensitivity (heightened sensitivity to touch) about as much as males, so the change in connections and the change in pain behavior did not track each other.
- **Why it matters**: Sex differences in pain are well documented but their cellular basis is poorly understood, and this paper points to hormones and the brain's extracellular matrix as possible switches controlling whether astrocytes can reshape pain circuits. The finding that synaptic plasticity and pain behavior can dissociate is worth noting, though the text alone does not show how this relates to chronic pain in people.
- **Background needed**: - Synaptic plasticity: lasting strengthening or weakening of connections between nerve cells; it is one proposed basis for learning and for pain that persists.
- Nociception: the nervous system's detection and signaling of potentially harmful stimuli.
- Astrocytes: star-shaped support cells in the nervous system that also influence nearby synapses.
- G-protein-coupled receptors (GPCRs): cell-surface receptors that trigger internal signaling; chemogenetics uses engineered versions to switch specific cells on or off with a drug.
- Gonadectomy / ovariectomy and testosterone treatment: surgical removal of sex glands and hormone replacement, used to test hormone effects.
- Perineuronal nets: mesh-like extracellular matrix structures around neurons that can limit how easily connections change.
- Mechanical hypersensitivity: increased pain response to light touch or pressure, typically measured in animals with filaments. · level: research-level

<details><summary>Original abstract</summary>

Sex differences in pain are well established, yet how nociceptive processing is differentially regulated across sexes remains poorly understood. Here, we show that spinal astrocytes provide pathway-specific control of acute nociceptive synaptic plasticity in rats. Chemogenetic activation of distinct astrocytic G-protein-coupled receptor pathways induced synaptic depression or potentiation at spinal nociceptive synapses in males, but failed to evoke detectable plasticity in females. Despite this lack of astrocyte-induced synaptic plasticity, females developed mechanical hypersensitivity comparable to males, revealing a dissociation between synaptic plasticity and pain-related behavior. Gonadectomy prevented astrocyte-induced plasticity in males, whereas testosterone treatment enabled Gq-dependent synaptic depression in ovariectomized females. Females exhibited more prominent perineuronal net labeling, and enzymatic degradation of extracellular matrix (ECM) components enabled Gq-dependent synaptic depression in females. Together, these findings identify hormonal status and ECM organization as important determinants of the susceptibility of spinal nociceptive circuits to astrocyte-driven synaptic plasticity.

</details>

### [Concurrent neuronal activity gates persistent dendritic spine shrinkage during mGluR-induced long-term depression](https://www.biorxiv.org/content/10.64898/2026.11.21.765465v1)
*Rojo-Francas, E.; Sanchez-Rodriguez, N.; Santuy, A. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.21.765465 v1 · relevance 0.07

- **In one sentence**: In organotypic rat hippocampal slices, mGluR1/5-induced LTD produced persistent dendritic spine shrinkage only when neuronal activity coincided with mGluR activation, a process the authors call MIND-sLTD that depends on mGluR1/5 and protein synthesis but not NMDARs.
- **In plain words**: Brain cells connect at small bumps called dendritic spines, and when a connection weakens, its spine tends to shrink. This paper asks whether shrinkage also happens when the weakening is triggered by a different receptor type (metabotropic glutamate receptors), where earlier reports disagreed. The authors chemically activated these receptors in slices of rat brain tissue and watched individual spines and calcium signals under a microscope. They found lasting shrinkage only when the cells were also firing actively at the same time.
- **Why it matters**: The work offers a possible explanation for conflicting earlier reports by suggesting that timing with neural activity matters for whether spines stay smaller. It may matter for understanding how memories are structurally consolidated, but the text alone does not establish how general or behaviorally relevant the effect is.
- **Background needed**: - Synapses: junctions where one neuron passes signals to another; most excitatory ones sit on dendritic spines.
- LTP / LTD: long-lasting strengthening / weakening of a synapse, thought to underlie learning and memory.
- Structural vs functional plasticity: changes in spine size and shape versus changes in signal strength.
- mGluR and NMDAR: two types of glutamate receptors (the brain's main excitatory chemical messenger); DHPG is a chemical that activates mGluR1/5.
- Organotypic slice culture: a thin slice of brain tissue kept alive in a dish.
- GCaMP6 and DsRed2: fluorescent markers used to track calcium activity and spine structure.
- Two-photon glutamate uncaging: a laser-based way to release glutamate onto a single spine.
- Coincidence detection: a process that responds only when two inputs arrive together. · level: research-level

<details><summary>Original abstract</summary>

Synaptic plasticity is a fundamental mechanism underlying learning and memory. Most excitatory synapses reside on dendritic spines, which undergo both functional and structural changes. These two forms of plasticity are typically tightly coupled: spines enlarge during synaptic strengthening (long-term potentiation, LTP) and shrink during synaptic weakening (long-term depression, LTD). While this coupling is well established for NMDA receptor (NMDAR)-dependent LTD, there are conflicting reports concerning whether spine shrinkage is coupled with metabotropic glutamate receptor (mGluR)-dependent LTD. To investigate the source of these conflicting results, we induced mGluR-LTD with the mGluR1/5 agonist DHPG in organotypic rat hippocampal slice cultures and monitored changes in spine morphology and calcium transients in CA1 pyramidal neurons expressing DsRed2 and GCaMP6. We found that mGluR activation is accompanied by long-term spine shrinkage only under conditions of elevated hippocampal neuronal activity. This form of plasticity, mGluR-induced neuronal activity-dependent structural LTD (MIND-sLTD), requires mGluR1/5 activation and de novo protein synthesis, but not NMDAR signaling. Persistent structural changes occur only when neuronal activity coincides temporally with mGluR activation. MIND-sLTD also occurs at individual synapses: mGluR activation induces persistent single-spine shrinkage only when synchronized with two-photon glutamate uncaging, independently of NMDARs. These findings identify a novel form of structural plasticity and suggest a coincidence-detection mechanism that integrates mGluR signaling with synaptic activity to consolidate long-term spine remodeling.

</details>

## Genetics and genomics

### [Population-level learning of non-additive effects enables accurate and efficient prediction of combinatorial perturbation responses](https://www.biorxiv.org/content/10.64898/2026.11.20.768136v1)
*An, s.; Gong, Q.; Cao, K.* · `genomics` · bioRxiv doi:10.64898/2026.11.20.768136 v1 · relevance 0.10

- **In one sentence**: GAIN is a lightweight model that predicts the population-level (pseudobulk) response to a two-perturbation combination as the sum of the two single-perturbation responses plus a learned interaction term, and is evaluated on single-cell genetic and drug combination datasets.
- **In plain words**: Scientists often want to know what happens when two genetic changes or two drugs are applied together, but testing every pair is impossible because the number of pairs grows fast. This paper proposes a simple model that starts from how each treatment acts on its own and learns only the extra effect that appears when they are combined. The authors report that this approach predicted combination responses more accurately than a plain additive baseline and than more complex cell-level methods, while training much faster.
- **Why it matters**: Predicting combination effects could help choose which genetic or drug pairs to test in costly lab screens, and the text suggests that a simple model can match or beat more complex deep-learning tools on these tasks. The text does not establish how well the approach transfers beyond the three datasets and one leukemia screen it reports, so its broader usefulness remains to be seen.
- **Background needed**: - Perturbation experiment: deliberately switching off a gene (often with CRISPR) or adding a drug, then measuring what changes in cells.
- Combinatorial perturbation: applying two or more perturbations together; the number of possible pairs grows quickly with the number of targets.
- Additive baseline: predicting the combined effect as the sum of the two single effects, which is the default expectation when treatments do not interact.
- Non-additive effect (interaction or synergy): when the combined result differs from the sum, for example stronger or weaker than expected.
- Single-cell data vs. pseudobulk: single-cell data measure each cell separately; pseudobulk averages cells within a group into one profile per condition.
- Foundation model: a large, general-purpose machine-learning model trained on very large datasets and adapted to specific tasks.
- Histone chaperone FACT: a protein complex that helps package DNA around histones and regulates gene activity. · level: intermediate

<details><summary>Original abstract</summary>

Combinatorial perturbations are widely used to study genetic interactions and to develop drug combinations, but the number of possible combinations grows quadratically with the number of perturbations, and only a small fraction can be measured in a screen experiment. Despite their growing sophistication, deep-learning and foundation models often fail to outperform a simple additive baseline based on measured single-perturbation responses. This suggests a simpler approach that builds on these measurements and directly learns deviations from additivity at the population level. We therefore developed GAIN, a lightweight model that implements these principles by predicting the pseudobulk response to a combination as the sum of its two single-perturbation responses and a learned interaction term. Across three single-cell datasets of genetic and drug combinations, GAIN corrected deviations from additivity and outperformed the additive model and cell-level methods across generalization settings and metrics, while training 3- to 64-fold faster. Applied to a combinatorial CRISPR screen of leukemia differentiation regulators, GAIN revealed synergy between key regulators of the differentiation block and genes that restrain differentiation but have little effect alone. It also revealed dampening by the histone chaperone FACT, which supports the induction of differentiation genes. These results establish population-level modeling of the deviation from additivity as a simple, accurate and scalable approach to predicting combination responses.

</details>

### [Single-cell study of the FCG rat model and cross-species comparison reveal stronger gene regulation by sex chromosome complement in the medial septum](https://www.biorxiv.org/content/10.64898/2026.11.19.767942v1)
*Turnbill, V.; Zhang, G.; Harris, E. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767942 v1 · relevance 0.09

- **In one sentence**: Single-cell transcriptomics of the medial septum in a novel four-core-genotype (FCG) rat model, compared with the FCG mouse, tests whether sex chromosome complement (XX vs. XY) or gonads drive sex-biased gene regulation across species.
- **In plain words**: Men and women differ in many brain-related conditions, but it is hard to tell whether the cause is the sex chromosomes or the sex hormones made by the gonads. The authors used a special rat model that separates these two effects and measured gene activity in individual brain cells from a small brain region called the medial septum. They report that differences in the sex chromosomes had a stronger effect on gene activity than gonads, and that this pattern was similar in mice and rats even though many individual genes differed.
- **Why it matters**: The finding argues against the common view that hormones from the gonads are the main source of sex differences in the brain, which matters for how sex differences in brain disease are studied. The authors also link the sex-biased genes to conditions such as anxiety, Alzheimer's disease, epilepsy and schizophrenia, but the text gives only the association, not evidence that these genes cause those conditions.
- **Background needed**: - Sex chromosome complement (SCC): whether an animal has XX or XY chromosomes, separate from whether it has ovaries or testes.
- Gonads: the ovaries or testes, which produce sex hormones.
- Four core genotypes (FCG) model: a mouse (and here rat) system that crosses these two factors, so chromosome and gonad effects can be compared directly.
- Medial septum: a small brain region involved in mood, memory and rhythm of brain activity; it shows structural sex differences.
- Single-cell gene expression: measuring which genes are active in each individual cell, then grouping cells by type.
- Gene regulatory network and transcription factor analysis: computational methods that infer which regulatory proteins control groups of genes.
- Cross-species comparison: checking whether a pattern found in one animal also holds in another, here rats and mice. · level: research-level

<details><summary>Original abstract</summary>

Sex differences are prominent in neuropsychiatric, neurological, and neurodegenerative conditions. While both gonads (ovaries vs. testes) and sex chromosome complement (SCC; XX vs. XY) contribute to sex differences, these effects are hard to differentiate in humans and gonadal contributions have been considered dominant in the brain. The four core genotypes (FCG) mouse model distinguishes between SCC and gonadal effects but whether findings are conserved across species remains unclear. Here, we present the first application of the novel FCG-derived rat model to explore cell-type-specific sex differences in the medial septum (MS), which shows robust structural sex differences, and convergence/divergence between species. Differential gene expression, pathway, transcription factor, and gene regulatory network analyses show dominant SCC effects and concordant gonadal effects on gene and network regulation in rat MS cell types. Comparison between the FCG rat and mouse models find convergence across species on the dominance of the SCC in regulating gene expression in concert with gonadal effects in the MS, despite divergence in individual sex-biased genes. In both species, the sex-biased, cell-type-specific MS genes and networks are associated with diverse diseases relevant to MS functions, such as anxiety, Alzheimers Disease, epilepsy, and schizophrenia, that can be targeted by proposed therapeutic candidates. Our cross-species investigation identifies a conserved dominance of SCC effects in sex-biased gene expression in the MS, thereby challenging the classical gonad-centric view of sexual differentiation in the brain and highlighting the MS as an important region for the study of sex differences driven by the sex chromosome complement.

</details>

## Cell and molecular biology

### [Palmitic acid overload does not promote full-blown dysfunction in SGBS adipocytes which is reflected in their secretome](https://www.biorxiv.org/content/10.64898/2026.11.19.767488v1)
*Angelini, S.; Stifani, G.; La Runa, G. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.19.767488 v1 · relevance 0.11

- **In one sentence**: In cultured SGBS human adipocytes, a 96-hour palmitic acid (PA) exposure raised lipid droplet and cell size and shifted cytokine and adiponectin secretion, but did not impair insulin signalling in adipocytes or in co-cultured myotubes.
- **In plain words**: Eating too much saturated fat is thought to help drive obesity and poor metabolic health, but it is unclear how much it damages human fat cells directly. This study grew fat cells from a human cell line (SGBS) in palmitic acid, a common saturated fat, for four days and checked their fat storage, inflammation signals, and the chemicals they released. The fat cells stored more fat and released more of some inflammatory signals, yet they did not become clearly dysfunctional, and their released chemicals did not block insulin action in muscle cells.</plain>
<parameter name="why">It suggests that a saturated fat alone, acting directly on fat cells without other immune or support cells present, may not be enough to produce the full set of problems linked to obesity. This is relevant to how fat tissue contributes to insulin resistance, though the result comes from a single cell model and says little about whole bodies.
- **Background needed**: - Adipocytes are fat-storing cells; SGBS is a human pre-adipocyte line that matures into fat cells in the lab.
- Palmitic acid (PA) is a long-chain saturated fatty acid common in the diet; BSA (bovine serum albumin) is the carrier protein used for the control condition.
- Insulin signalling works through proteins such as Akt and AS160; if it is impaired, cells take up less sugar, a feature of insulin resistance.
- NF-kB is an inflammation-related signalling pathway; MCP-1, IL-6 and IL-8 are inflammatory messenger molecules; adiponectin is a hormone usually considered protective.
- The secretome is the set of molecules a cell releases into its surroundings; it was tested by transferring it onto muscle cells (myotubes).
- The stromal vascular fraction (immune and support cells found in fat tissue) was absent here, which the authors note limits how far the results apply to real tissue. · level: research-level

<details><summary>Original abstract</summary>

Background: Energy excess, and particularly long-chain saturated fatty acid (SFA) overload, are instrumental in promoting obesity and hampering metabolic health. However, SFA contribution to human adipocyte metabolic and endocrine dysfunction remains elusive. Nonetheless, we have already provided evidence that a 48-hour palmitic acid (PA) exposure is not sufficient to hamper Simpson-Golabi Behmel Syndrome (SGBS) adipocytes insulin signalling. Objective: This study aims at evaluating whether a 96-hour exposure to PA is able to disrupt SGBS adipocyte metabolic health and induce the release of a secretome capable of hampering insulin signalling in skeletal muscle cells. Methods: SGBS adipocytes were treated with either 1000 uM PA or bovine serum albumin (BSA) for 96 hours followed by the assessment of the NFkB signalling and the expression of genes associate with inflammation and adipocyte metabolic stress. Furthermore, adipocytes were labelled with BODIPY and lipid droplet as well as cell size semi-quantified using ImageJ. Insulin-induced phosphorylation of Akt and Akt substrate of 160 kDa (AS160) was assessed by Western Blot. The effect of PA on SGBS secretome was assessed by both ELISA as well as MILLIPLEX. Finally, human immortalised myotubes were co-cultured with BSA or PA-treated SGBS adipocytes for 24 hours followed by the assessment of insulin signalling at the Akt level. Results: PA did not activate the NFkB signalling pathway, but induced the expression of MCP-1 while tending to upregulate IL-6 mRNA levels. Despite 96-hour PA exposure leading to an increase in lipid droplet and cell size, this was not coupled with an impairment in insulin signalling. Nevertheless, this SFA promoted an increase in IL-6 and IL-8 secretion while tending to enhance the release of adiponectin by SGBS adipocytes. Finally, the secretome from PA-treated SGBS adipocyte did not impair insulin-induced phosphorylation of Akt relative to controls in myotubes. Conclusions: Thus, in the absence of the stromal vascular fraction, direct exposure of SGBS adipocytes to PA overload is not sufficient to elicit overt dysfunction. The absence of full-blown adipocyte dysfunction is reflected in the secretome of these cells which failed to disrupt skeletal muscle insulin signalling.

</details>

### [Extra-sheath transplantation of human retinal organoids (hROs): effects on visual recovery and retinal repair following optic nerve injury](https://www.biorxiv.org/content/10.64898/2026.11.18.767615v1)
*Luo, Y.; Chen, X.; Kang, J. et al.* · `developmental biology` · bioRxiv doi:10.64898/2026.11.18.767615 v1 · relevance 0.08

- **In one sentence**: In C57 mice with optic nerve crush, transplanting day-30 human retinal organoids at the injury site was associated with preserved optic-disc appearance, ganglion cell layer thickness, and flash VEP P2 amplitude, with a b-wave showing no between-group difference, though donor-derived circuit integration was not demonstrated.
- **In plain words**: Damage to the optic nerve, the cable that carries vision signals from the eye to the brain, can cause lasting vision loss. In this study, researchers placed small lab-grown human "mini-retinas" (retinal organoids) at the site of a crushed optic nerve in mice and tracked the eyes and visual responses for up to 28 days. Transplanted mice kept more of their nerve-cell layer and showed stronger visual-brain signals and better responses to moving stripes than mice with the crush alone, though the authors say the results do not yet prove the graft wired into the visual circuit.
- **Why it matters**: Optic nerve injury has few treatments that protect the nerve cells and restore signalling at the same time, so a graft-based approach is of interest. The text is measured about its limits: the benefits were incomplete compared with uninjured mice, and the behavioural light-dark test is non-specific, so the work is an early preclinical signal rather than evidence of a therapy.
- **Background needed**: - Retinal ganglion cells: the eye's output neurons whose long axons form the optic nerve to the brain.
- Optic nerve crush: a standard lab injury model that mechanically damages this nerve.
- Retinal organoids: three-dimensional tissue grown from stem cells that mimics parts of the retina.
- Microelectrode array (MEA): a plate that records electrical activity from cells.
- Electroretinography (ERG) and visual evoked potentials (VEP): recordings of electrical responses from the retina (ERG b-wave) and the visual cortex (VEP P2 peak) to light flashes.
- Optomotor response: a mouse's reflex to turn its head with rotating stripes, used to gauge vision.
- Immunostaining (RBPMS, TUJ1, IBA1): labelling that marks ganglion cells, their axons, and microglia (immune cells of the nervous system).
- Mouse strain C57: a common inbred laboratory mouse line. · level: research-level

<details><summary>Original abstract</summary>

Traumatic optic nerve injury interrupts retinal ganglion cell output and can produce permanent visual disability, yet a therapeutic strategy that couples retinal protection with recovery of visual-pathway activity remains unavailable. Here, we evaluated human retinal organoid transplantation at the site of optic nerve crush in C57 mice. Human retinal organoids derived from embryonic stem cells were used at day 30 and showed retinal-lineage immunoreactivity together with spontaneous microelectrode-array activity. Across post-surgical days 7, 14, and 28, transplantation was associated with preservation of optic-disc appearance and ganglion cell layer thickness. The structural benefit became statistically distinguishable from the crush group at day 28 and remained incomplete relative to the uninjured or sham group. Serial RBPMS and TUJ1 immunostaining further supported attenuation of retinal ganglion cell body and neurite loss, while IBA1 staining indicated an altered microglial response. Full-field electroretinographic b-wave responses showed no detectable between-group differences, arguing against a major outer-retinal effect. In contrast, flash visual evoked potential P2 amplitude was higher in transplanted than in crush-only mice at all measured time points, consistent with improved visual-pathway responsiveness. Transplant recipients also showed enhanced optomotor responses across tested spatial-frequency and contrast conditions. Light-dark behavior shifted toward greater dark-compartment occupancy and activity, although this assay remains non-specific for visual recovery. Together, these findings support a model in which hROs transplantation at an optic nerve injury site promotes multi-level functional preservation after optic nerve crush. Definitive evidence for donor-derived circuit reconstruction will require graft tracing, synaptic validation, and prespecified electrophysiologic analyses.

</details>

## Immunology and microbiology

### [Local macrophage and cDC1 cooperation in the liver drives T-cell immune surveillance against pioneering metastatic cancer cells.](https://www.biorxiv.org/content/10.64898/2026.11.21.768283v1)
*Pinci, B.; Manzanal, A.; Chiclana-Valcarcel, M. L. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.21.768283 v1 · relevance 0.15

- **In one sentence**: Intravital imaging of early liver metastasis in mice shows that resident Kupffer cells, macrophages and cDC1 dendritic cells cooperate via antigen cross-presentation to recruit T cells into activation clusters that help control arriving tumor cells.
- **In plain words**: Cancer often spreads to the liver through the bloodstream, and this study asks how the liver's own immune cells respond when the first tumor cells arrive. Using live imaging inside the organ, the authors describe three stages: routine immune patrolling, a rush of neutrophils and macrophage uptake of tumor material, and T-cell activation in small clusters within the liver. Boosting dendritic cell numbers with Flt3L-Ig reduced successful metastasis in their experiments.
- **Why it matters**: It maps the earliest immune steps against metastasis in a major target organ, which may matter for designing therapies that prime local immunity. The text does not show whether these mouse findings translate to human patients, so that link remains open.
- **Background needed**: - Metastasis: cancer cells leaving a tumor and seeding new growth elsewhere, here in the liver.
- Intravital imaging: filming living cells inside an intact animal organ with microscopes.
- Kupffer cells: macrophages (immune cells that engulf material) resident in the liver.
- Dendritic cells (cDC1): immune cells that capture antigens (molecular pieces of a pathogen or tumor) and present them to T cells; cross-presentation means displaying material from outside the cell.
- T cells: immune cells that can kill targeted cells once activated.
- Flt3L-Ig: a drug used in mice to expand dendritic cell populations. · level: research-level

<details><summary>Original abstract</summary>

The liver is one of the most frequent sites for hematogenous metastasis across different types of cancer, but how the liver mounts effective immune responses against arriving tumor cells is not fully understood. Using intravital imaging, we have visualized the initial steps of liver metastasis and delineated three phases in the immune response at the earliest stages of liver metastasis: first, there is continuous surveillance of the liver parenchyma by discrete immune cell subsets in the premetastatic tissue. Second, upon metastatic cell arrival, there is massive neutrophil recruitment and tumor-cell material uptake mediated by resident macrophages. Third, antitumor-specific T-cell activation takes place in situ within intrahepatic leukocyte clusters. We find that tumor-derived material uptake triggers transcriptional programs in liver myeloid cells that upregulate chemoattraction programs in Kupffer cells and cDCs, leading to T-cell activation. Antigen cross-presentation and a functional partnership between cDC1s and local macrophages to recruit and form T-cell activation clusters are required for the elicitation of these intrahepatic T-cell responses. Consequently, prior expansion of cDCs by Flt3L-Ig treatment significantly enhances immunosurveillance, curtailing successful metastasis development. Collectively, our findings identify coordinated immune responses that are essential for anti-metastatic immunity within the liver, uncovering a program to mount defenses against tumor cells arriving in the liver.

</details>

### [Viral genetic variation programs divergent neuroimmune states during rabies infection](https://www.biorxiv.org/content/10.64898/2026.11.20.768130v1)
*Gassmann, S.; Mullner, R.; Zaeck, L. M. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.20.768130 v1 · relevance 0.13

- **In one sentence**: In mice infected intracerebrally with genetically distinct rabies viruses, temporal proteomics and spatial imaging show that viral genetics, through interferon antagonism, shape divergent brain immune states that are not simply proportional to viral load.
- **In plain words**: Rabies is a virus that attacks the brain, and different strains can cause very different immune reactions even when they reach similar levels in the tissue. The researchers infected mice directly into the brain with several engineered rabies viruses, including disease-causing field strains, a weakened strain, and a new variant that is more sensitive to interferon, an antiviral alarm signal. They then tracked protein changes over time and mapped where immune cells appeared in different brain regions.
- **Why it matters**: The text suggests that how much virus is present does not fully predict the strength or type of the host's immune response, which matters for understanding why some infections trigger brain inflammation and others do not. The work is limited to mice and a direct brain-injection model, so any link to human rabies or to vaccine design is an open question the text does not settle.
- **Background needed**: - Rabies virus (RABV) spreads through the nervous system and is nearly always fatal once symptoms appear.
- Field strains are viruses taken from wild or domestic animals; attenuated strains are weakened versions, often used as a basis for vaccines.
- Interferons are signalling proteins that alarm cells and trigger antiviral defences; some viruses carry proteins (here, the phosphoprotein) that block this alarm.
- Complement is a group of blood and tissue proteins that help clear pathogens and can also drive inflammation.
- Proteomics measures the proteins present in tissue; spatial imaging shows where in the tissue they are found.
- Recombinant viruses are built in the lab with specific genetic changes to test what each change does. · level: research-level

<details><summary>Original abstract</summary>

Viral burden does not necessarily predict the extent or composition of the host immune response, reflecting the complexity of virus - host interactions. Rabies virus (RABV) provides a powerful model to investigate this question because genetically distinct RABVs differ in replication, immune evasion, and neuroimmune activation. Here, we performed integrated temporal proteomic and spatial imaging analyses of recombinant RABV, including pathogenic, attenuated, and a newly generated interferon-sensitive variant with disrupted phosphoprotein antagonistic activity. Following intracerebral infection of mice, viruses established distinct neuroimmune states that diverged over time in antiviral signaling, complement activation, and immune response. Notably, the pathogenic field viruses rDogA and rFox both exhibited substantial viral accumulation, but elicited markedly different central nervous system (CNS) responses, with rDogA inducing limited host immune engagement, whereas rFox triggered early and broad antiviral, complement, and immune recruitment programs. Disruption of phosphoprotein-mediated interferon antagonism in rDogA enhanced interferon-stimulated gene expression and antiviral effectors, restricting viral accumulation without inducing broad neuroimmune remodeling. Conversely, the attenuated glycoprotein-modified rSAD GASGAS elicited strong complement activation and T cell recruitment with little detectable viral levels, revealing a highly immunogenic neuroimmune state. Spatial profiling further identified virus-dependent patterns of myeloid, astrocyte-associated, complement, and lymphocyte responses across brain regions. Together, these findings demonstrate how viral genetic background and its modulation of host antiviral responses shape divergent neuroimmune states in which viral accumulation, antiviral immunity, and CNS immune activation are differentially coordinated.

</details>

## Cancer biology

### [Adjuvant myeloperoxidase inhibition promotes B and T cell mediated control of murine melanoma metastasis](https://www.biorxiv.org/content/10.64898/2026.11.20.768197v1)
*Landreth, K. M.; Sharp, A. W.; Basnet, A. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.20.768197 v1 · relevance 0.11

- **In one sentence**: In an immunocompetent mouse model of spontaneous melanoma, adjuvant myeloperoxidase (MPO) inhibition reduced multi-organ metastasis in a manner dependent on B, CD8+ and CD4+ T cells and linked to reduced neutrophil extracellular trap (NET) release, with similar effects reported in a spontaneous breast cancer model.
- **In plain words**: Melanoma is a skin cancer that spreads to distant organs, and that spread causes most deaths from it. This study tested whether blocking an enzyme called myeloperoxidase, which is made by a type of immune cell, could slow that spread in mice with a natural form of melanoma. The authors report fewer spread tumors across several organs, more B and T immune cells in the affected tissue, and fewer tumor cells circulating in the blood.
- **Why it matters**: Most current immune-directed cancer treatments do not target the myeloid cells that the authors say help metastasis, so an enzyme that can be blocked by a drug is a potentially new angle. The text does not establish that this approach works in patients, and the mouse results would need clinical testing before any conclusions about treatment.
- **Background needed**: - Metastasis: cancer cells leaving a primary tumor and forming new tumors in distant organs.
- Myeloid cells: a family of white blood cells, including neutrophils, that the paper says can suppress immune attacks on tumors.
- Myeloperoxidase (MPO): an enzyme found in myeloid cells; the paper treats it as a drug target.
- Neutrophil extracellular traps (NETs): web-like strands of DNA and proteins released by neutrophils; the paper proposes them as a downstream mediator of MPO's effect.
- B and T cells: adaptive immune cells that can attack tumors; the study shows the MPO inhibitor's effect depends on them.
- Adjuvant therapy: treatment given after the main tumor is removed or controlled, aimed at preventing recurrence or spread.
- Spontaneous model: mice that develop tumors on their own rather than from injected cancer cells. · level: research-level

<details><summary>Original abstract</summary>

Metastasis is the spread of cancer cells from primary tumors to distant organs and accounts for the majority of melanoma deaths, with a 5-year survival rate of only 30%. Despite strong evidence that myeloid cells promote metastasis, there are limited clinically effective myeloid-directed therapies. Here, we demonstrate that targeting myeloperoxidase (MPO), a myeloid-lineage restricted enzyme, significantly reduced multi-organ metastatic burden using an immunocompetent mouse model of spontaneous melanoma. Adjuvant MPO inhibition remodeled the metastatic microenvironment by a reduction in Ly6G+Ly6C+ myeloid cells and enrichment of B and T cell populations. Importantly, adjuvant MPO inhibitor-mediated metastatic control was dependent upon B, CD8+ T cells and CD4+ T cells, and rapidly reduced circulating and disseminated tumor cells. MPO inhibition markedly decreased NET release, while NET deficiency and inhibition recapitulated the anti-metastatic effects of targeting MPO, implicating NETs as a potential downstream mediator of MPO-driven metastasis. We further validated these findings in a distinct spontaneous breast cancer model where adjuvant MPO inhibition similarly reduced multi-organ metastatic burden with comparable changes within the metastatic immune microenvironment. Collectively, our studies introduce MPO as a druggable regulator of metastasis where MPO inhibition limits metastatic disease by targeting immunosuppressive myeloid cells.

</details>

### [A KRASG12D-based organoid model for early oncogenic transformation of the mammary epithelium](https://www.biorxiv.org/content/10.64898/2026.11.17.766834v1)
*Jones, D. J.; Rao, L. E.; West, J. J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.17.766834 v1 · relevance 0.07

- **In one sentence**: A mouse mammary (breast) epithelial organoid model in which Cre-induced KRASG12D expression produces neoplastic growth without lumen formation, with heterotypic competition between mutant and wild-type cells and suppressed apoptosis.
- **In plain words**: Researchers wanted a lab system for watching the very first steps of cancer forming in breast tissue. They grew small 3D clusters of healthy mouse mammary cells (organoids) and switched on a cancer-linked mutation, KRASG12D, in some of them. The mutated clusters grew abnormally and failed to form the hollow central space that normal ones develop, and mutant cells gained ground over normal neighbors.
- **Background needed**: - Organoids: small 3D clusters of cells grown in a dish that mimic some features of a real organ.
- KRAS: a gene that normally helps control cell growth; the G12D change is a common cancer-linked mutation that keeps it switched on.
- Cre-mediated expression: a genetic switch that turns a gene on in selected cells.
- Lumen: the hollow central cavity that normal mammary ducts and organoids form.
- Heterotypic organoid: an organoid containing a mix of two cell types, here mutant and normal cells.
- Apoptosis: programmed cell death, a normal way cells are removed.
- The study is a model-building paper in mice-derived cells; it does not test treatments in patients. · level: research-level

<details><summary>Original abstract</summary>

Modeling cancer initiation, progression, and metastasis has greatly impacted our understanding of fundamental cell and molecular mechanisms driving disease and has led to breakthrough treatments that greatly improve patient outcomes. Understanding the earliest stages of tumor formation is particularly important for uncovering the root causes of oncogenic transformation and tumor evolution. It has been historically difficult to model the cellular dynamics that drive the earliest stages of tumor evolution, largely due to difficulties in culturing and manipulating normal primary cells in 3-dimensional environments, triggering oncogenesis, and observing the resulting effects. Recent advances in 3D organoid culture provide a promising avenue to address these challenges. In this study, we have developed a Kras based organoid model of early tumorigenesis. In our model, oncogenic transformation was triggered by Cre-mediated expression of oncogenic KRASG12D in otherwise healthy murine-derived mammary epithelial organoids. While normal organoids displayed controlled organoid growth and morphogenesis, induction of KRASG12D caused neoplastic organoid growth that occurred with the absence of lumen formation. Gene expression analysis revealed up regulation of several KRAS effectors, and a broad repertoire of genes associated with tumor development and human breast cancer. Induction of oncogenic Kras in our model resulted in heterotypic organoids that possessed KRASG12D + cells growing alongside KRASG12D- cells. In this context, amplification of KRASG12D + cells occurred at the expense of KRASG12D- cells. Finally we observed that neoplastic growth of KRASG12D expressing organoids was associated with a suppression of apoptosis. We believe that our organoid model provides a platform that is suitable to examine the earliest stages of tumor development and can be expanded to study several questions related to cancer biology, prevention studies, therapeutic development, and beyond.

</details>

## Ecology and evolution

### [Biotic interactions buffer the effects of biodiversity loss on ecosystem functioning](https://www.biorxiv.org/content/10.64898/2026.11.20.768031v1)
*Vidiella, B.; Montoya, J. M.* · `ecology` · bioRxiv doi:10.64898/2026.11.20.768031 v1 · relevance 0.17

- **In one sentence**: A theoretical model of species interaction networks suggests that the number and strength of trophic links determine how strongly losing species reduces ecosystem functions such as primary production and carbon retention.
- **In plain words**: Losing species from an ecosystem often weakens things like plant growth and carbon storage, but it is hard to say when the damage will be large. This paper builds a theoretical model showing that the web of who eats or affects whom shapes the answer. In networks with many or strong feeding links, surviving species can make up for lost ones through alternative pathways, so the loss hurts less; in networks with fewer or weaker links, the ecosystem is much more sensitive to extinctions.
- **Why it matters**: It offers a single framework for why biodiversity loss matters more in some systems than others, and it proposes that losing interactions, not just species, is a hidden part of the biodiversity crisis. The text is only an abstract, so the strength of the evidence and how well the model fits real ecosystems cannot be judged from it.
- **Background needed**: - Ecosystem functioning: the processes an ecosystem performs, such as producing plant biomass (primary production) and storing carbon.
- Trophic link: a feeding relationship, such as a predator eating prey or a herbivore eating a plant.
- Species interaction network: a map of which species interact with which, drawn as nodes (species) joined by links (interactions).
- Interaction strength: how much one species affects another's numbers or activity.
- Compensation: when surviving species take over the role of lost ones, cushioning the effect on the whole system.
- Theory vs. data: this is a model-based argument; the abstract does not report empirical tests. · level: research-level

<details><summary>Original abstract</summary>

Biodiversity loss generally impairs functions on which nature and societies depend upon. Yet, it is difficult to predict under which conditions losing biodiversity has larger effects on functions such as primary production or carbon retention. We present a theory that demonstrates that biotic interactions mediate the intensity of these effects. In species interaction networks with many or strong trophic links, biodiversity loss has weaker effects on functioning because alternative interaction pathways allow surviving species to compensate for species loss. In contrast, in networks with fewer or weaker links, ecosystem functioning is very sensitive to the extinction of species. Here, we identify interaction erosion as a hidden dimension of the biodiversity crisis that provides a unifying explanation for functional consequences of biodiversity loss across ecological contexts.

</details>

### [Resistance evolution in a single species reorganizes community responses across a resource-antibiotic landscape](https://www.biorxiv.org/content/10.64898/2026.11.20.768032v1)
*Aapalampi, I.-K.; Bischofberger, A. M.; Kiciatovas, D. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.20.768032 v1 · relevance 0.11

- **In one sentence**: Mapping how antibiotic resistance evolution in one Aeromonas caviae lineage reshapes three- and 16-species bacterial community states, diversity and dominance across a grid of resource and antibiotic conditions.
- **In plain words**: Evolution can happen fast enough to change a whole community of organisms, not just the species that evolves. This study asked how one bacterial species becoming antibiotic-resistant changed the wider community, and whether those changes depended on food supply and antibiotic level. The authors tested 64 combinations of resources and antibiotic and found that the same resistance change had different effects in different settings.
- **Why it matters**: It suggests that the ecological effects of evolution cannot be judged from one environment alone, which matters for predicting how resistance spreads through microbial communities. The text does not indicate applications beyond this experimental system, so the wider significance is uncertain.
- **Background needed**: - Antibiotic resistance: a heritable ability of bacteria to survive a drug that would normally kill or stop them.
- Community: a set of coexisting species interacting in the same place.
- Community-state boundary: the tipping line between environmental conditions where different sets of species dominate or persist.
- Inhibitory concentration: the drug level high enough to stop a species growing; below it, the drug may still affect growth.
- Intrinsic resistance: a species' inherent tolerance to a drug, as opposed to one acquired by evolution.
- Dominance and diversity: which species take over a community, and how evenly many species coexist. · level: research-level

<details><summary>Original abstract</summary>

Rapid evolution in one species can restructure ecological communities, but how its effects vary across environmental conditions remains poorly understood. Here we mapped the consequences of antibiotic resistance evolution in Aeromonas caviae across 64 combinations of resource availability and antibiotic stress in three- and 16-species bacterial communities. Resistance evolution changed where community-state boundaries were located, with boundaries lost or gained depending on resource availability. The same evolutionary change increased diversity in some environments but decreased it in others. Species success was partly explained by growth traits at zero or low antibiotic concentrations and by intrinsic resistance at inhibitory concentrations. Resistance evolution reversed dominance between the two dominant species and changed which traits mattered. It also altered other species' responses below inhibitory concentrations, mostly between closely related species. Our findings show that the consequences of evolution depend on environmental context but can be partly explained by species traits.

</details>

## Plant biology

### [Circadian clock components CCA1 and LHY shape heat responses across regulatory layers](https://www.biorxiv.org/content/10.64898/2026.11.19.767892v1)
*Strout, R. I.; Grubb, L. E.; Uhrig, R. G. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767892 v1 · relevance 0.11

- **In one sentence**: A time-resolved transcriptome, proteome and metabolome study of Arabidopsis clock mutants (altered CCA1 and LHY) after short heat stress, mapping shared and distinct clock-linked heat-response regulation across gene expression layers.
- **In plain words**: Heat is especially harmful to crops when it hits at night, so plants may need to respond differently depending on the time of day. This paper looks at how the plant's internal daily clock, specifically two clock genes called CCA1 and LHY, shapes the plant's response to a short burst of heat. The authors measured genes, proteins and metabolites over time in normal plants and in mutants lacking these clock genes.
- **Why it matters**: Crop losses from heat are a practical concern, and the text suggests timing-dependent heat tolerance could guide breeding or engineering. The work is mainly a data resource and set of candidate connections; the text does not show that these findings would translate to crops.
- **Background needed**: - Circadian clock: an internal roughly 24-hour timekeeper that controls when many genes are switched on in a plant.
- CCA1 and LHY: two closely related clock genes; the mutant plants have altered levels of them.
- Transcriptome, proteome, metabolome: the full sets of RNA messages, proteins and small molecules in a sample, measured to see how a stress ripples through the cell.
- Heat stress: a short period of high temperature that changes gene activity.
- Thermotolerance: a plant's ability to survive and function under high heat.
- Post-translational regulation: control of protein activity or levels after a protein is made.
- Arabidopsis: a small model plant widely used in laboratory research. · level: research-level

<details><summary>Original abstract</summary>

High temperatures reprogram gene regulatory responses and are particularly deleterious for crop yield, especially when these events occur at night. This emphasizes that partitioning of heat responses is based on time of day. Coordination between time of day and environmental responses relies on the circadian clock. However, the precise regulatory mechanism of how the clock achieves this partitioning at different levels of gene regulation is poorly understood. Using circadian clock mutants with altered CCA1 and LHY expression, we generated a time-resolved transcriptome, proteome, and metabolome following a short-term heat stress in Arabidopsis. We identified regulatory connections specific to CCA1 and LHY, as well as those shared with other clock components linked to heat stress responses. Additionally, new connections between CCA1 and LHY and non-cycling genes highlight a broader role for the clock in regulating heat responsive gene expression. CCA1 and LHY regulated processes, such as sulfur assimilation and ROS scavenging, may contribute to time-of-day specific thermotolerance. Overall, heat responses were dampened in both the transcriptome and proteome in cca1lhy, suggesting both transcriptional and post-translational circadian-regulated processes are important for heat responses. Lastly, we identified differences in metabolic responses in cca1lhy and suggest a role for circadian regulation of starch degradation in thermotolerance. This study generates and utilizes data across levels of gene regulation to identify heat responses in the transcriptome and proteome regulated by CCA1 and LHY. These findings establish shared and distinct regulatory mechanisms of clock components in response to heat stress and provide new candidates for network integration and a foundation to engineer plants more tolerant to high temperatures depending on time of day.

</details>

### [Auxin regulates the proportions, but not the initiation, of Hibiscus trionum bullseyes](https://www.biorxiv.org/content/10.64898/2026.11.19.767829v1)
*Salvi, E.; Gatti, S.; Yeo, M. T. S. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.19.767829 v1 · relevance 0.10

- **In one sentence**: In the petals of Hibiscus trionum, auxin signalling is not needed to set up the initial bullseye boundary during pre-patterning, but it is needed in the distal petal region to maintain the bullseye's proportions established in young primordia.
- **In plain words**: Many flowers have coloured patterns on their petals, such as the dark centre of a bullseye, that guide pollinators. This paper asks whether a plant growth hormone called auxin helps draw the boundaries of these patterns in the hibiscus Hibiscus trionum. The authors report that auxin does not start the boundary, but it is needed to keep the pattern's proportions steady as the petal grows.
- **Why it matters**: The study suggests that a general growth hormone could change how big different parts of a pattern are, which may help explain how flower patterns vary between species over evolutionary time. The summary provided is limited to the abstract, so the strength of the evidence and the specific experiments cannot be judged from it.
- **Background needed**: - Petal patterns such as bullseyes are made of epidermis cells (the outer skin layer of the petal) that differ in pigment and surface texture across regions.
- Auxin is a plant hormone that controls cell growth and direction of development across many plant organs.
- A petal primordium is the very young, not-yet-open petal tissue, where early pattern layout is set.
- "Pre-patterning" means the early stage when regions of the petal are first marked out before colours appear.
- "Distal region" means the part of the petal farthest from where it attaches to the flower.
- "Proportions" here means the relative sizes of the bullseye's inner and outer zones. · level: research-level

<details><summary>Original abstract</summary>

Colourful motifs on the surface of flower petals fulfill important ecological functions, mediating pollination and providing protection against environmental stressors. These patterns form when epidermis cells in different subdomains of the petal acquire contrasting chemical and structural features. While some of the enzymes and transcription factors involved in specifying the production of different pigments, cell shapes and textures have been identified, the signalling events and upstream processes that divide the petal surface in distinct regions are not yet understood. Plant hormones play key roles in orchestrating all aspects of plant development but whether and how they contribute to the establishment of petal patterns remain to be tested. Here, we investigate the roles of auxin during bullseye pattern development in Hibiscus trionum. We found that auxin does not initiate bullseye boundary formation during the pre-patterning phase. Instead, auxin signalling is essential for regulating cell behaviour in the distal region and preserving the bullseye proportions established in young petal primordia. Therefore, auxin could act as a pattern modifier over evolutionary timescales, shifting bullseye dimensions by modulating the relative growth of different petal regions.

</details>

## Bioengineering and synthetic biology

### [Internalizing-peptide engineering converts blocking anti-EGFR antibodies into EGFR lysosomal targeting degraders](https://www.biorxiv.org/content/10.64898/2026.11.20.768013v1)
*Petrov, P. D.; Vinueza-Gavilanes, R.; Vicente, A. P. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.20.768013 v1 · relevance 0.06

- **In one sentence**: Engineering full-length anti-EGFR antibodies (cetuximab and the blocking antibody LEI) with cell-penetrating arginine-rich peptides yields recombinant fusion proteins that promote EGFR lysosomal degradation and enhance growth inhibition of NSCLC cells in 2D and 3D models, alone and with EGFR tyrosine kinase inhibitors.
- **In plain words**: Many cancer drugs that target the EGFR protein only block its signaling, leaving the protein sitting on the cell surface. This study attaches short peptides that help cells take in material to antibodies against EGFR, so the antibody pulls the receptor inside the cell where it is broken down. In lung cancer cell cultures and 3D clumps of cells, the engineered fusion proteins reduced EGFR levels and slowed growth more than the unmodified antibodies, especially when combined with EGFR kinase inhibitors.
- **Why it matters**: It offers a possible complementary approach to kinase inhibitors: removing the target protein rather than only blocking it, which may matter for drug resistance in lung cancer. The text reports laboratory and 3D culture results only, so whether this works in animals or patients is unknown.
- **Background needed**: - EGFR (epidermal growth factor receptor) is a cell-surface protein that drives growth signals; it is overactive in some lung cancers.
- Antibodies such as cetuximab usually block EGFR activity without removing the protein from the cell.
- Tyrosine kinase inhibitors (TKIs such as gefitinib and osimertinib) block EGFR's internal signaling switch.
- Cell-penetrating peptides (here polyarginine peptides like R12) help molecules enter cells.
- Endocytosis and lysosomes: cells take in surface proteins in bubbles, which fuse with acidic lysosomes that break them down; bafilomycin A1 blocks this acidification.
- Fusion protein: a single engineered protein combining an antibody with a peptide.
- 2D cell wound-healing assays and 3D spheroids are lab models that mimic tumors more closely than flat cell layers.
- siRNA: a tool that silences a gene to reduce a protein's production. · level: research-level

<details><summary>Original abstract</summary>

Conventional antibodies targeting the epidermal growth factor receptor (EGFR) primarily inhibit receptor activation rather than efficiently eliminating the receptor from tumor cells. Here, we investigated whether engineering full-length anti-EGFR antibodies with internalizing peptides could promote receptor degradation, enhance their biological activity and enable the development of recombinant receptor-depleting antibodies. Chemical conjugation of cetuximab (CTX) to the polyarginine peptide R12 enhanced intracellular uptake, reduced surface-accessible EGFR and decreased total receptor abundance in vitro. CTX-R12 conjugate also enhanced inhibition of wound repopulation in non-small cell lung cancer (NSCLC) cell lines, an effect reproduced using the R12 variant LINC18, and transferred to the independent blocking anti-EGFR antibody LEI. Incorporation of LINC19, a variant of LINC18, into recombinant full-length antibody fusion proteins preserved their activity. The LEI-LINC19 fusion (LEIP), reduced surface-accessible and total EGFR, with bafilomycin A1 reversing receptor loss and supporting an acidification-dependent endolysosomal component of degradation. Functional studies indicated that the antibody-peptide reduced DNA synthesis rate. Furthermore, siRNA-mediated EGFR depletion increased TKI-associated reductions in cellular biomass in PC9 cells and increased gefitinib responsiveness in H1975 cells. Consistently, combining LEIP with either osimertinib or gefitinib produced greater inhibition of H1975 wound repopulation than the corresponding individual treatments. LDH analysis revealed increased membrane-damage-associated LDH release following LEIP-gefitinib treatment but no additional increase with LEIP-osimertinib relative to osimertinib alone. These effects extended to 3D NSCLC models. CTX-R12 inhibited PC9 3D colony development, whereas LEIP restricted expansion of established PC9 colonies and reduced the projected area of H1975 spheroids. In H1975 spheroids initiated with 1,000 or 5,000 cells per well, LEIP-containing combinations with osimertinib or gefitinib produced greater inhibition of the spheroid size than the corresponding TKI-only treatments. Nuclear Green DCS1 staining revealed no detectable baseline core necrosis in untreated H1975 spheroids, whereas LEIP treatment was associated with DNA-positive material within and surrounding the spheroids. Moreover, LEIP-treated H1975 spheroids exhibited markedly reduced EGFR immunofluorescence compared with control and parental LEI-treated spheroids. Together, these findings demonstrate that internalizing-peptide engineering of blocking anti- EGFR antibodies can generate full-length EGFR-depleting fusion proteins with enhanced biological activity. The recombinant LEIP format and its activity in 3D in vitro NSCLC tumor models support further investigation of fusion antibody-mediated EGFR degradation as a complementary strategy to EGFR kinase inhibition.

</details>

### [Dual photoresponsive hydrogel surfaces enabling integrated single-cell analysis of morphology and gene expression](https://www.biorxiv.org/content/10.64898/2026.11.18.767535v1)
*Li, X.; Uehara, R.; Mizuno, K. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.18.767535 v1 · relevance 0.06

- **In one sentence**: A dual photoresponsive hydrogel surface that uses light to trap single cells in a uniform array, track their shape changes over time, and then photodegrade the gel locally to release chosen cells for single-cell gene expression analysis.
- **In plain words**: Scientists want to watch individual cells change shape over time and then check which genes those cells are switching on. This paper describes a gel-coated surface that uses two kinds of light: one beam holds cells in place in an evenly spaced grid, and a second beam melts the gel under chosen cells so they can be collected. The authors report using this to link cell shape changes to gene activity, including in invasive cancer cells.
- **Why it matters**: Separating what a cell looks like from what it is doing inside is a central problem in studying cell variation, and this workflow tries to connect the two in the same cells. The text does not report how broadly the approach has been tested, so its wider usefulness remains to be seen.
- **Background needed**: - Hydrogel: a water-swollen, soft gel-like material that cells can sit on or be held in.
- Photoactivatable / photodegradable: materials that change behavior or break down when hit with specific light.
- Single-cell gene expression analysis: measuring which genes a single cell is actively using, usually by reading its RNA.
- Morphological dynamics: how a cell's shape and structure change over time, often followed by microscope imaging.
- Heterogeneity: the fact that cells of the same type can behave differently from one another.
- Invasive cancer cells: cancer cells that move into surrounding tissue, a key step in spread. · level: research-level

<details><summary>Original abstract</summary>

Integrated single-cell analysis linking time-resolved cellular phenotypic dynamics with gene expression is essential for understanding cellular heterogeneity but remains technically challenging. Here, we report a dual photoresponsive hydrogel that combines a photoactivatable cell-trapping material with a photodegradable hydrogel, enabling light-directed single-cell capture, time-resolved imaging, and the on-demand release of selected cells for downstream gene expression analysis. This approach allows cells to be arrayed at a high density with uniform spacing, facilitating high-throughput monitoring of morphological dynamics. Cells exhibiting phenotypes of interest can be precisely retrieved by localized hydrogel degradation induced by secondary light irradiation and subsequently subjected to single-cell gene expression analysis. Using this workflow in combination with high-throughput real-time image processing technology, we directly link dynamic morphological features to gene expression and demonstrated the ability of the workflow to examine transcriptional alterations associated with invasive cancer cell behavior.

</details>

## Mathematical biology (arXiv)

### [One-Step Self-Assembling Lipopolymer Coatings Enable Direct Longitudinal Biosensing in Native Biological Matrices](https://arxiv.org/abs/2611.27422)
*Pascal R\"uedi, Sarina Seiter, Stephan Handschin et al.* · `q-bio.QM` · arXiv:2611.27422v1 · relevance 0.05

- **In one sentence**: A one-step, self-assembling lipid-polymer coating for microfluidic channels that suppresses non-specific binding in undiluted serum and enables label-free digital holographic counting of tetraspanin-positive extracellular vesicles from lung cancer cell models.
- **In plain words**: Medical sensing devices often give false signals because proteins and other molecules in blood or serum stick to their surfaces. This paper describes a simple coating, built from fat-like molecules that assemble themselves within minutes, that makes the inside of tiny fluid channels resist this sticking and still lets test molecules attach where intended. The authors used it with a microscope-based imaging setup to track tiny cell-released particles (extracellular vesicles) over time from lung cancer cells, using 50 microlitres of sample without first purifying it.
- **Why it matters**: Real-time, continuous monitoring of biological samples would be more useful than one-off end-point tests, and this coating is presented as simple and compatible with both glass and PDMS plastic devices. The text does not give comparison benchmarks or independent validation, so its practical reach beyond these experiments is uncertain.
- **Background needed**: - Biosensor: a device that detects a specific molecule or particle, often by using a capture probe on a surface.
- Non-specific binding (fouling): unwanted sticking of proteins or other molecules to a surface, which creates false signals.
- Lipid-based self-assembly: fat-like molecules that spontaneously organize into a layer on a surface without chemical reactions.
- PEGylated lipids: fat molecules carrying a polyethylene glycol chain that repels proteins and helps surfaces resist sticking.
- Microfluidics: handling tiny volumes of fluid in channels a fraction of a millimetre wide.
- Digital in-line holography: a lens-free imaging method that records interference patterns to count and size particles.
- Extracellular vesicles: small membrane bubbles that cells release, often studied as messengers or disease markers; tetraspanins are surface proteins used to identify them. · level: research-level

<details><summary>Original abstract</summary>

Sample-driven cross-reactivity remains a fundamental bottleneck for sensitive and selective biosensing in complex biological environments, particularly in microfluidic systems where high surface-to-volumes ratios amplify non-specific interactions. Here, we address this challenge with a one-step, biomimetic surface functionalization strategy based on engineered lipid-based nanocarriers that self-assemble within minutes into immunoassay-ready, antifouling interfaces that couple pegylated-lipid passivation with biorthogonal, site-specific probe conjugation. This approach enables rapid, tuneable, and reproducible surface functionalization, which suppresses sample-specific cross-reactivity even in undiluted serum, and supports direct, label-free digital biosensing assays directly in native biological environments. When integrated into an optofluidic platform combining digital in-line holography and microfluidics, this approach allows time-resolved quantification of tetraspanin-positive extracellular vesicle secretion dynamics from two-dimensional and three-dimensional lung cancer cell models using 50 {\mu}L of sample within 10 min, without isolation or purification. Because the presented surface functionalization proceeds via self-assembly rather than covalent surface modification, this one-step modular-approach is intrinsically decoupled from device fabrication and applies to both glass and PDMS, coating the entire microfluidic channel, thereby establishing a general route for integrating biomimetic nanostructures into robust, high-performance immunoassays, advancing biosensing beyond end-point measurements, and towards rapid and continuous real-time monitoring.

</details>

### [Self-organized fractional silencing of pyramidal neurons under global depolarization in a spatial neuron-glial microcircuit model](https://arxiv.org/abs/2611.27847)
*Stanislav V. Lagosha, Andrey Yu. Verisokin, Darya V. Verveyko et al.* · `q-bio.NC` · arXiv:2611.27847v1 · relevance 0.04

- **In one sentence**: A spatial computational model of a neuron–astrocyte–vascular unit shows how inhibitory interneurons lose firing first under high extracellular potassium, how stimulation can fragment a network into self-sustaining active microclusters, and how a damaged astrocyte region can destabilize surrounding healthy tissue once it exceeds a critical size.
- **In plain words**: This paper studies how brain tissue can slip into harmful patterns such as seizure-like bursts and spreading waves of depolarization, where cells become electrically stuck. Using a detailed computer simulation of a two-dimensional patch of neurons, support cells called astrocytes, and blood-vessel-linked units, the authors found that inhibitory cells switch off before excitatory pyramidal cells, and that strong stimulation breaks the network into small clusters of persistently overactive cells. They also report that a small area of faulty astrocyte potassium clearance is compensated by healthy neighbors, but a larger damaged area can tip surrounding tissue into lasting pathological activity.
- **Why it matters**: Epileptiform discharges and spreading depolarization are serious events in conditions such as seizures and stroke, and the model offers a testable account of how local astrocyte damage could spread into wider dysfunction. As a purely simulation study, its predictions depend on the chosen model parameters and would need experimental checking before any clinical relevance can be claimed.
- **Background needed**: - Neurons communicate through electrical spikes; "firing" means producing spikes.
- Hodgkin-Huxley model: a standard mathematical description of how neurons generate spikes from ion currents.
- Depolarization block: a state where a neuron is pushed so far from its resting voltage that it can no longer fire.
- Extracellular potassium: excess potassium outside cells raises neuronal excitability; astrocytes normally clear it.
- Excitation vs. inhibition: pyramidal neurons excite the network, interneurons calm it; their balance governs stability.
- Glutamate spillover: neurotransmitter leaking beyond synapses to affect neighboring cells.
- Neuromodulation (noradrenergic): chemical signals from norepinephrine that tune neuron activity.
- Microclusters: small, spatially separated groups of cells firing persistently. · level: research-level

<details><summary>Original abstract</summary>

Pathological transitions in nervous tissue, including epileptiform discharges and cortical spreading depolarization, depend on the interplay between cellular and interstitial mechanisms. We develop a biophysically detailed two-dimensional model of the neurogliovascular unit (NGVU) integrating neuronal populations in the Hodgkin-Huxley formalism, astrocyte-regulated extracellular potassium dynamics, extracellular neurotransmitter spillover, and noradrenergic neuromodulation. Numerical simulations show that inhibitory interneurons enter depolarization block (DB) at significantly lower extracellular potassium concentrations and stimulation intensities than pyramidal neurons. Early loss of inhibition shifts the local excitation-inhibition balance and triggers network hyperexcitability. In the spatially extended network, exceeding a critical stimulation threshold induces a transition from heterogeneous but spatially uniform firing to network fragmentation into stable active microclusters with self-sustained high-frequency firing. Pyramidal neurons with lower excitatory synaptic input receive less recurrent excitation, which protects them from DB. By continuously releasing potassium ions and glutamate into the extracellular space, pyramidal neurons drive strong depolarization in more densely connected neighbors and push them into deep DB. Simulations of localized astrocytic dysfunction predict a spatial limit for potassium clearance defects. Small damaged cores are fully compensated by diffusion and uptake by surrounding healthy astrocyte units. However, above a critical damage size, activity-dependent potassium buildup and firing positive feedback disrupt homeostasis in surrounding units, promoting persistent depolarized centers with self-sustained, spatially segregated pathological activity.

</details>

## Epidemiology

### [Personal HbA1c trajectories and incident diabetes: association, prediction and observability in the English Longitudinal Study of Ageing](https://www.medrxiv.org/content/10.64898/2026.11.20.26368578v1)
*Tapias, D.; Donati, C.; Völter-Mahlknecht, S.* · `epidemiology` · medRxiv doi:10.64898/2026.11.20.26368578 v1 · relevance 0.08

- **In one sentence**: In English older adults (ELSA), individual HbA1c trajectories gave modest adjusted association with incident diabetes but did not improve prediction beyond baseline HbA1c, and a drift model suggests personal slopes are hard to recover from sparse measurements.
- **In plain words**: This study asks whether tracking a person's blood sugar marker (HbA1c) over several years predicts who will develop diabetes, better than a single test result. Using repeated measurements from the English Longitudinal Study of Ageing, the researchers found that a person's personal upward or downward trend was linked to later diabetes after adjustment, but adding these trend features did not clearly improve prediction overall. They also found that slow natural fluctuations make individual trends hard to pin down when tests are spaced years apart.
- **Why it matters**: It bears on how doctors might use repeated routine lab results rather than a single snapshot, and on the limits of such data for personal risk estimates. The text is an observational secondary analysis of one cohort, so its findings are measured and not a basis for changing clinical practice.
- **Background needed**: - HbA1c: a blood test reflecting average blood sugar over roughly the previous two to three months; a diagnostic threshold marks diabetes.
- Incident diabetes: diabetes that develops during follow-up, not present at the start.
- Prospective cohort: a group of people followed over time, with measurements taken repeatedly.
- Linear mixed model: a statistical model that estimates each person's typical level and rate of change while borrowing information across people.
- Cross-fitting: fitting model parameters on other participants to avoid overfitting to the person being predicted.
- AUC (area under the ROC curve): a 0 to 1 score of how well a method ranks people who will and will not develop the condition; 0.5 is chance.
- Transformer: a neural network architecture, here trained on the lab sequences, used as a comparison method.
- Ornstein-Uhlenbeck process: a model of random fluctuations that drift back toward an average and are correlated over time, used to mimic biological noise.
- Odds ratio per SD: how much the odds of diabetes change for each standard-deviation increase in a measure. · level: research-level

<details><summary>Original abstract</summary>

Background. Clinical diagnosis often relies on a snapshot: a single measurement interpreted against a population threshold. Repeated (longitudinal) measurements, however, may reveal an individual's typical level and how it changes over time. Extracting this information is challenging when measurements are sparse and biological fluctuations may resemble sustained changes. Using data from the English Longitudinal Study of Ageing (ELSA), we investigated whether individual glycated haemoglobin (HbA1c) trajectories improved the prediction of incident diabetes beyond the most recent measurement, whether they were associated with incident diabetes, and how reliably they could be estimated. Methods. In this secondary analysis of a prospective cohort study, we analysed venous HbA1c measured approximately every four years in ELSA, with a longer final interval of about seven years. A linear mixed model estimated each person's usual HbA1c level and rate of change (personal slope) from their measurements before each diabetes-free health visit, with model parameters estimated in other participants (cross-fitting). We derived four longitudinal features: deviation from the person's usual level, personal slope, change since the last measurement, and the forecast probability that the next HbA1c reaches the diagnostic threshold for diabetes. We evaluated the associations of these features with incident diabetes and their incremental predictive value beyond baseline HbA1c and clinical risk factors in internal, cross-fitted validation, compared predictive performance with a self-supervised Transformer, and modelled within-person variation as serially correlated drift (an Ornstein-Uhlenbeck process) to assess how reliably personal slopes can be recovered under different measurement schedules. Results. The analysis included 5,828 diabetes-free baseline visits from 3,603 participants, of which 234 were followed by incident diabetes. Neither the engineered longitudinal features nor a Transformer that also used additional clinical variables improved discrimination beyond baseline HbA1c and clinical risk factors (difference in the area under the receiver operating characteristic curve, {Delta}AUC, -0.002 to +0.010; all 95% confidence intervals [CIs] including zero). The estimated personal slope was nevertheless associated with incident diabetes after adjustment for baseline HbA1c, age and other clinical factors (odds ratio [OR] per standard deviation [SD] 1.18, 95% CI 1.02--1.36, and 1.39, 1.11--1.74, among visits with at least two earlier HbA1c values), whereas deviation from the person's usual level was not (OR 0.99, 95% CI 0.81--1.21). In the drift model, serially correlated fluctuations accounted for 77--81% of residual within-person variance, although the estimated temporal structure was sensitive to the treatment of the first HbA1c values at or above the diagnostic threshold. Under this model, persistent individual trends were difficult to distinguish from slowly varying fluctuations: with the intercept-slope correlation set to zero, estimated and underlying slopes correlated weakly for four-yearly measurements over up to 12 years (r [&le;] 0.26), and more frequent measurements improved this little. Conclusions. Estimated personal HbA1c slopes carried adjusted prognostic information beyond baseline HbA1c and clinical factors, but longitudinal features, including those learned by a Transformer, did not clearly improve prediction. The drift model suggests that slowly varying within-person fluctuations may limit the reliable estimation of individual slopes from sparse measurements, and that longer observation histories are more informative than more frequent measurement. Whether personal laboratory histories improve prediction depends not only on their association with disease, but also on how reliably individual change can be recovered from the available measurements.

</details>

### [Depressive Symptom Trajectories and Incident Cognitive Impairment by Outcome Ascertainment](https://www.medrxiv.org/content/10.64898/2026.11.18.26368449v1)
*Liu, X. L.; Guo, Z. L.* · `epidemiology` · medRxiv doi:10.64898/2026.11.18.26368449 v1 · relevance 0.07

- **In one sentence**: In four harmonized national aging cohorts (91,043 adults aged 50+), depressive symptom trajectories were associated with incident cognitive impairment more strongly when outcomes were ascertained with more rigorous, clinically adjudicated methods, with a meta-regression exploring ascertainment rigor as a moderator of heterogeneity.
- **In plain words**: Researchers asked whether the link between long-term depression symptoms and later memory or thinking decline in older adults depends on how that decline is measured. They pooled data from aging studies in China, the US, England and Europe and found that when cognitive problems were judged by self-report, the link was weak or inconsistent across countries. When judged by a full clinical diagnosis, depression-related risk appeared for every non-low symptom pattern, and the effect grew with each step up in measurement rigor.
- **Why it matters**: It suggests that differences in past estimates of depression as a dementia risk factor may partly reflect how outcomes were measured, which matters for prevention trials and burden forecasts. The authors note the meta-regression is exploratory and based on only five levels, so the pattern should be checked in other data before being relied on.
- **Background needed**: - Cohort study: following a group of people over time and recording who develops an outcome.
- Depressive symptom trajectories: groups of people with similar patterns of depression scores over time (e.g., persistently low, persistently high, worsening, remitting), identified statistically.
- Incident cognitive impairment: new memory or thinking problems that appear during follow-up.
- Ascertainment rigor: how carefully a condition is identified, from self-report up to a clinical expert consensus diagnosis (HCAP is a standardized cognitive assessment protocol).
- Hazard ratio (HR) and odds ratio (OR): measures of how much more likely an outcome is in one group than another; values above 1 mean higher risk.
- Meta-analysis and meta-regression: combining results across studies, and testing whether study features explain differences between them.
- Mild cognitive impairment (MCI): a stage between normal ageing and dementia. · level: research-level

<details><summary>Original abstract</summary>

Importance: Dementia prevention frameworks treat depression as a leading modifiable risk factor, but cohort estimates of the association vary widely; whether this variation reflects how cognitive outcomes are ascertained is unknown. Objective: To examine whether associations between depressive symptom trajectories and incident cognitive impairment vary by outcome ascertainment rigor. Design, Setting, and Participants: This harmonized cohort study included 91,043 adults aged 50 years or older from 4 national longitudinal aging cohorts (CHARLS [China], HRS [US], ELSA [England], and SHARE [16 European countries]); baseline waves spanned 2006 to 2011, with follow-up through 2023. Exposure: Depressive symptom trajectory classes (persistent low, persistent high, incident worsening, remitting) derived using group-based trajectory modeling. Main Outcomes and Measures: Incident cognitive impairment ascertained under a 5-level hierarchy of increasing rigor, from self-report (level 1) to clinical consensus diagnosis (level 5; Harmonized Cognitive Assessment Protocol [HCAP]). Cohort-specific Cox models were pooled by random-effects meta-analysis; meta-regression tested ascertainment rigor as a moderator of heterogeneity. Results: Under nonadjudicated outcomes, the incident-worsening trajectory was associated with incident cognitive impairment in CHARLS (HR, 1.31; 95% CI, 1.06-1.62) and SHARE (HR, 1.99; 95% CI, 1.87-2.13) but not HRS (HR, 1.05; 95% CI, 0.95-1.16) or ELSA (HR, 1.10; 95% CI, 0.95-1.27); the persistent-high trajectory was not significant under any nonadjudicated outcome (HR range, 1.07-1.15). Under clinical consensus diagnosis (n = 3,196), all non-low trajectories were independently associated with mild cognitive impairment or dementia (OR range, 1.66-2.29; dementia-only persistent high: OR, 3.32; 95% CI, 1.85-5.95). Effect sizes increased stepwise with ascertainment rigor (meta-regression slope, 0.314 log HR per level; P < .001; residual I2 = 0%; R2 = 100%; exploratory). Findings were robust to lagged, weighted, and competing-risk analyses; biological aging acceleration did not differ across trajectories. Conclusions and Relevance: The detectability and magnitude of depression-related cognitive risk depend on outcome ascertainment rigor. Prevention trials and burden projections relying on self-reported outcomes may underestimate the benefit of depression treatment.

</details>

## Infectious diseases

Nothing notable this time.

## Public and global health

### [Additional Vascular Imaging in Women With Acute Cerebral Ischemia: Thresholds for Cost-Effectiveness](https://www.medrxiv.org/content/10.64898/2026.11.19.26368544v1)
*Boettger, P.; Klug, J.; Agarwal, A. et al.* · `health economics` · medRxiv doi:10.64898/2026.11.19.26368544 v1 · relevance 0.09

- **In one sentence**: A decision-tree and lifetime state-transition model estimating how many additional intracranial vascular scans in women with acute cerebral ischemia would need to lead to timely endovascular thrombectomy to be cost-effective under Ontario and US Medicare assumptions.
- **In plain words**: Women with a sudden stroke caused by a blocked blood vessel in the brain are less likely than men to get a scan that looks at those brain vessels. This paper asks how much extra scanning would need to lead to a clot-removal procedure, and how well that procedure would need to work, before the extra care is worth its cost. The authors used computer models of costs and health over a lifetime, with results reported for Canada (Ontario) and the US Medicare program.
- **Why it matters**: The question matters for fairness in stroke care, since a sex gap in access to imaging and treatment is a concrete, actionable problem. The findings are conditional thresholds from modelling rather than measured outcomes, so they indicate what a future prospective program would have to achieve rather than showing that it would pay off.
- **Background needed**: - Acute cerebral ischemia: a stroke where blood flow to part of the brain is cut off, usually by a clot.
- Intracranial vascular imaging: scans (such as CT or MR angiography) that show the blood vessels inside the skull and whether one is blocked.
- M1 occlusion: a blockage in a major artery in the brain (the proximal middle cerebral artery).
- Endovascular thrombectomy (EVT): a catheter procedure that threads into the brain's arteries to physically pull out the clot.
- HERMES: a pooled analysis of randomized trials that measured the benefit of thrombectomy.
- Modified Rankin Scale (mRS): a 0 to 6 scale of how dependent a person is after stroke; scores 0 to 2 are usually treated as functionally independent.
- Decision tree and state-transition model: standard health economic tools that follow patients through possible outcomes and health states over time.
- Cost-effectiveness threshold: the price per quality-adjusted life-year (QALY) a payer is willing to accept; here CAD 50,000 and USD 100,000.
- Sensitivity analysis: rerunning the model with different assumptions to see how robust results are. · level: research-level

<details><summary>Original abstract</summary>

Background: Women with acute cerebral ischemia receive intracranial vascular imaging less often than men, but the value of expanding imaging is uncertain. We estimated the treatment rates and functional benefits required for additional imaging to be cost-effective. Methods: We developed a decision tree and state-transition model comparing additional imaging followed by timely endovascular thrombectomy (EVT) for M1 occlusion with current care from Ontario public-payer and US Medicare perspectives. Women-specific 90-day modified Rankin Scale distributions from HERMES were projected over a lifetime. We jointly varied the proportion of additional scans leading to additional timely EVT and the treatment effect relative to HERMES. Cost-effectiveness thresholds were CAD 50,000 and USD 100,000 per quality-adjusted life-year. Program costs represented health-care resources in Ontario and additional payments under Medicare. Results: At variable program costs of CAD 1,000 or USD 1,000 per additional scan, assuming the full HERMES effect and no additional fixed costs or pathway-related harm, expected cost-effectiveness required one additional timely EVT per 48 scans in Ontario and 57 under Medicare (2.07% and 1.74%, respectively). Treatment rates of 3.07% and 2.65% were required for a 90% probability of cost-effectiveness under these assumptions. At three additional thrombectomies per 100 scans and the same costs, treatment effects had to reach 76.9% and 67.3% of the HERMES effect. With the full effect, 1,000 additional scans at this treatment rate yielded approximately 5 additional functionally independent survivors at 90 days. Deterministic analyses restricted to 5 years increased the required treatment rates to 4.44% and 4.22%. Conclusions: Additional vascular imaging in women could be cost-effective when a small proportion of scans leads to timely thrombectomy, provided sufficient functional benefit is retained. Prospective evaluations should assess additional treatment opportunities, functional outcomes and program costs against these conditional thresholds, which depend on projected long-term outcomes.

</details>

### [Enhancing Access to and Utilization of Maternal and Child Health Service through Implementation of a District-led Integrated Mobile Health Service Delivery Model in Pastoral Ethiopia: A Multi-Method Implementation Research](https://www.medrxiv.org/content/10.64898/2026.11.18.26368458v1)
*Semahegn, A.; Belete, M.; Tiruneh, G. T. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.18.26368458 v1 · relevance 0.07

- **In one sentence**: A multi-method implementation study with a non-randomized quasi-experimental (difference-in-differences) design evaluates a district-led, monthly mobile health service model for maternal, newborn and child health in four pastoralist woredas of Ethiopia, using DHIS2 routine data and 143 interviews.
- **In plain words**: Many people in remote, mobile pastoralist communities in Ethiopia are far from clinics, so they often miss care during pregnancy and for young children. This study tested a monthly mobile health service, run through the local district, that brought antenatal care, vaccines and other services to 20 hard-to-reach villages. The authors report that over one year the service reached about 79,000 people across 190 sessions, and that it was linked to better antenatal and vaccination coverage compared with comparison areas.
- **Why it matters**: It addresses a real gap in reaching mobile and remote populations, where standard clinic-based models struggle, and it gives practical lessons on district leadership and community co-design. The design is non-randomized and the outcomes are from routine records, so the effect estimates are best read as suggestive rather than definitive; the text does not show long-term sustainability or costs.
- **Background needed**: - Pastoralists move herds seasonally, so fixed clinics are often far away; the average facility-to-village distance here was 29.6 km.
- MNCH means maternal, newborn and child health; ANC is antenatal care (check-ups during pregnancy).
- Penta-3 is the third dose of a five-in-one childhood vaccine, used as a common coverage marker.
- DHIS2 is a national routine health information database used for facility records.
- Difference-in-differences is a comparison method: it compares the change over time in the intervention areas with the change in comparison areas, to estimate the program's added effect.
- Quasi-experimental means there was an intervention and comparison group but people or areas were not randomly assigned.
- Implementation research studies how a program is delivered in practice, not only whether it works in principle.
- PHC means primary health care. · level: intermediate

<details><summary>Original abstract</summary>

Introduction: Lack of access to essential health services has remained a significant public health challenge in sub-Saharan Africa. The conventional health service delivery models often fail to account for the mobility patterns and socio-cultural values of these communities. These communities are frequently affected by recurrent droughts, conflicts, floods, and disease outbreaks. This study assessed the contribution of a mobile health services (MHS) delivery model designed to improve access to and utilisation of maternal, neonatal, and child health services in pastoralist contexts of Ethiopia. Methods: A multi-method embedded implementation research with a non-randomized controlled quasi-experimental study design was employed in four selected Woredas of Ethiopia. Baseline data from July 2022 to June 2023 and endline data from July 2023 to June 2024 were extracted from DHIS2. The MHS delivery model was co-designed with stakeholders, redefined communitycentred outreach sites, and established a multidisciplinary team, that was implemented monthly. The average distance between the health facility and the centre of the targeted community village was 29.6 kilometres. Data were captured from routine health service records, MHS databases, and program reports, and 143 in-depth interviews among service providers and beneficiaries. Quantitative data were analysed using descriptive statistical methods and difference-indifferences using Stata 18, while qualitative data were coded and analysed using ATLAS.ti. Results: During the twelve months, the MHS reached 79,404 people through 190 sessions held and offered an integrated essential health service in 20 hard-to-reach villages. In the study area, ANC use was 64.0% in Chifra and 75.6% in Dasenech. In addition, penta-3 antigen vaccination improved from 66.0% to 69.7% in Chifra and from 91.2% to 102.1% in Dasenech, respectively. In the difference-indifferences analysis, the MHS significantly enhanced access to ANC follow-up and completion of pentavalent and full vaccination coverage. A Woreda-led approach, community engagement, context-tailored and timely communication, and comprehensive service delivery by a multidisciplinary team enhanced the use and acceptability of the MHS in the pastoral setting. The contribution of MHS to ensuring access and use of MNCH services ranged from 13.0% to 19.1% for continuing family planning and antenatal care, respectively. Conclusions: The study highlights that the MHS delivery model is a suitable platform that has substantially contributed to improving access to and use of maternal, newborn, and child health services in pastoral, agropastoral, and scattered settlements. Being a woreda-led, participatory codesign, community-centred approach, and context-tailored health service delivery approach enhanced the acceptability and effectiveness of the MHS in reaching the underserved community. Integration of MHS with the existing PHC system, with an innovative, sustainable financing mechanism, is recommended to ensure access and use of MNCH in hard-to-reach settings.

</details>

## Psychiatry and neurology

### [Cycle-based neurostimulation for control of circadian brain network dynamics in human epilepsy](https://www.medrxiv.org/content/10.64898/2026.11.19.26368528v1)
*Saboo, K. V.; Fan, J. M.; Tadayon, E. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.19.26368528 v1 · relevance 0.14

- **In one sentence**: Longitudinal ECoG study in bitemporal epilepsy reporting that daily alignment of hippocampal connectivity rhythms predicts seizure reduction under responsive neurostimulation, modeled with a nonlinear Kuramoto oscillator and in-silico stimulation-timing optimization.
- **In plain words**: This paper looks at whether the body's daily (roughly 24-hour) cycles affect how well brain stimulation works for epilepsy. The researchers followed people with seizures starting in both temporal lobes over months, recording brain activity from electrodes on the brain surface. They found that when the rhythms in the left and right hippocampus (a memory-related brain region) lined up in time, patients had more seizure reduction, and the timing of when stimulation was delivered during the day was linked to how these rhythms changed.
- **Why it matters**: It suggests that the timing of stimulation within the day, not just its amount, may matter for treatment, which could inform personalized neurostimulation for epilepsy and possibly other brain disorders. The text itself does not show that timing-based stimulation improves outcomes in patients; the timing optimization was only tested in simulation.
- **Background needed**: - Epilepsy: a condition with recurring seizures; here the focus is on seizures arising in both temporal lobes (bitemporal).
- Responsive neurostimulation: a device that detects abnormal brain activity and delivers electrical pulses in response.
- Electrocorticography (ECoG): recording brain electrical activity with electrodes placed on the brain surface.
- Circadian rhythm: a roughly 24-hour biological cycle, such as sleep-wake timing.
- Hippocampus: a brain region involved in memory; the study compares its left and right sides.
- Kuramoto oscillator model: a mathematical model of many rhythmic units that synchronize with one another, used here to describe how the two hippocampi's rhythms align.
- In silico: carried out in computer simulation rather than in patients. · level: research-level

<details><summary>Original abstract</summary>

Biological rhythms modulate symptoms of brain disorders, yet brain stimulation therapies largely overlook the temporal organization of pathological brain states. Harnessing these rhythms could improve therapeutic efficacy. Here, we show that circadian coordination of hippocampal network connectivity is a biomarker of therapeutic response to responsive neurostimulation in epilepsy. Using longitudinal electrocorticography from individuals with bitemporal epilepsy, we find that alignment of circadian connectivity rhythms between the left and right hippocampus predicts seizure reduction. The daily distribution of stimulation also predicts how these rhythms evolve over months. We capture these dynamics using a nonlinear Kuramoto oscillator model and demonstrate that optimizing stimulation timing in silico can improve predicted circadian network alignment. Our findings establish a cycle-based, control-theoretic framework for modelling and potentially reshaping brain network rhythms, offering new opportunities for personalized neurostimulation in epilepsy and other neurological and psychiatric disorders.

</details>

### [Carotid Artery Stenosis is Associated with Restless Legs Syndrome in the Absence of Stroke](https://www.medrxiv.org/content/10.64898/2026.11.17.26368361v1)
*Ogulnick, J. V.; Shin, W.; Mathew, J.* · `neurology` · medRxiv doi:10.64898/2026.11.17.26368361 v1 · relevance 0.11

- **In one sentence**: A TriNetX propensity-matched case-control study (58,382 per group) reports a small association between bilateral internal carotid artery stenosis/occlusion (ICD-10 I65.23) and later restless legs syndrome diagnosis (G25.81), with an adjusted OR of 1.09 (95% CI 1.002-1.186).
- **In plain words**: Restless legs syndrome is a common condition that causes an urge to move the legs, often at night. This study asked whether narrowing or blockage of the large arteries in the neck that supply the brain is linked to getting that condition, even when the person has not had a stroke. Using a large database of electronic health records, the researchers compared patients with severe bilateral neck-artery narrowing to similar patients with hardening of the arteries but no narrowing, and found a small increase in restless legs diagnoses.
- **Why it matters**: If a blood-flow problem in the brain contributes to restless legs, that would add a possible vascular cause to a condition usually treated as neurological or iron-related. The effect is small, though, and the study is observational, so it only suggests a link and cannot show that narrowed arteries cause the condition. The authors themselves call for prospective studies.
- **Background needed**: - Restless legs syndrome (RLS): a common disorder causing uncomfortable leg sensations and a strong urge to move, usually worse at rest or at night.
- Internal carotid artery stenosis (CAS): narrowing of the main arteries on each side of the neck that carry blood to the brain.
- Chronic hypoperfusion: long-term reduced blood flow to brain tissue.
- Dopaminergic pathways: brain circuits using dopamine, a chemical messenger; these are thought to be involved in RLS.
- Retrospective case-control study: looks back at existing records, comparing people with and without an exposure.
- Propensity score matching: pairing patients on many background traits so the groups are comparable.
- Odds ratio (OR): a measure of how much more likely an outcome is in one group; 1.09 means about 9% higher odds, a small effect.
- Confidence interval (CI): the range of values consistent with the data; this one is narrow and just above 1.
- Absolute risk difference: 1.977% vs 1.816%, about 0.16 percentage points. · level: research-level

<details><summary>Original abstract</summary>

Background: Restless legs syndrome (RLS) is a common neurological disorder with established links to atherosclerotic disease and secondary causes such as ischemic stroke. Hypothesizing that internal carotid artery stenosis (CAS) could induce secondary RLS through chronic hypoperfusion or microemboli to dopaminergic subcortical structures, even without overt stroke, we investigated the association between bilateral CAS and RLS. Methods: A retrospective propensity score-matched case-control study was conducted using the TriNetX Global Health Research Network. Cases (n=58,382) had bilateral CAS/occlusion (ICD-10-CM I65.23); controls (n=58,382) had atherosclerosis without CAS. Patients were excluded for prior stroke/TIA, iron deficiency, antipsychotic use, and other secondary RLS causes. Cases and controls were 1:1 matched on age, race/ethnicity, chronic kidney disease, peripheral neuropathy, peripheral artery disease, Parkinson's disease, and SSRI use. The outcome was RLS diagnosis (G25.81), assessed via conditional logistic regression. Results: RLS was diagnosed in 1,154 (1.977%) patients with bilateral CAS/occlusion versus 1,060 (1.816%) controls, yielding an absolute risk difference of 0.161% (95% CI 0.005-0.317%; p=0.0437). The adjusted odds ratio was 1.09 (95% CI 1.002-1.186), indicating a modest but significant association. Conclusion: Severe bilateral CAS/occlusion is associated with a small but statistically significant increase in RLS risk, independently of overt cerebrovascular events and known confounders. These findings support a potential vascular contribution to RLS pathogenesis, possibly through subclinical hypoperfusion affecting basal ganglia dopaminergic pathways. Prospective studies are needed to explore causality, dose-dependency, and the impact of carotid revascularization.

</details>

## Oncology

### [Panel-agnostic tumour-only diagnosis of mismatch repair deficiency](https://www.medrxiv.org/content/10.64898/2026.11.19.26368513v1)
*Garcia-Lopez, D.; Hernando, B.; Chaves-Urbano, B. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.19.26368513 v1 · relevance 0.08

- **In one sentence**: A tumour-only classifier (captureMMRd) that infers mismatch repair deficiency from mutational signatures in somatic variant calls already produced by targeted panels, validated across 7,514 samples from 16 cohorts against IHC and MSI-PCR reference tests.
- **In plain words**: Some cancers lose a DNA repair system called mismatch repair, and patients whose tumours have this loss may respond to immunotherapy. Current tests for it often need a matched normal sample or special genetic markers that many routine gene panels lack. This paper describes an open-source tool that spots the loss using patterns in the mutations already found in a tumour's sequencing data.
- **Why it matters**: If it holds up, it could let hospitals that already run tumour-only gene panels screen for a treatment-relevant condition without adding a new test. The text reports strong agreement with standard lab tests, but these are retrospective results across many cohorts, and real-world performance on individual panels still needs checking.
- **Background needed**: - Mismatch repair (MMR) is a cell system that fixes copying errors in DNA; when it fails (MMRd), mutations pile up.
- MMRd tumours can respond to immune checkpoint immunotherapy, so detecting them matters clinically.
- Standard confirmatory tests are immunohistochemistry (IHC, staining for repair proteins) and MSI-PCR (checking microsatellite instability, i.e. length changes in repeated DNA stretches).
- Targeted panels sequence only selected genes; tumour-only means no matched healthy-tissue sample is sequenced for comparison.
- Mutational signatures are characteristic patterns of mutation types that reveal the processes that caused them.
- Sensitivity is the share of true cases detected; specificity is the share of true non-cases correctly cleared. · level: research-level

<details><summary>Original abstract</summary>

A diagnosis of mismatch repair deficiency (MMRd) can unlock immunotherapy treatment for a patient. However, existing sequencing-based detection methods require matched normal samples, panel-specific baselines or dedicated microsatellite loci, none of which are available to the tumour-only targeted panels that dominate routine clinical practice. Here we present captureMMRd, an open-source classifier that diagnoses MMRd using mutational signatures computed from the somatic variant calls any panel already produces. Applying a single locked model to 7,514 samples from 16 independent cohorts, spanning whole-exome, whole-genome, targeted panel and plasma cfDNA sequencing, captureMMRd achieved a pooled sensitivity of 94.36% and specificity of 99.02% against orthogonal MMR IHC and MSI-PCR testing, and outperformed microsatellite-based callers on panels with limited microsatellite content. We demonstrate that as few as 3 indels and 44 single-base substitutions are sufficient for reliable diagnosis, defining a minimum panel footprint that most clinically deployed assays already exceed. Our findings extend clinically actionable MMRd detection to the sequencing workflows of routine precision oncology, with the potential to broaden patient access to immunotherapy without new assays, baselines or matched normal samples.

</details>

### [Baseline Prognosis and Treatment Benefit From First-Line Immunotherapy Strategies: Target Trial Emulations Across Advanced Solid Tumors](https://www.medrxiv.org/content/10.64898/2026.11.20.26368610v1)
*Orcutt, X.; Nimgaonkar, V.; Chen, K. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.20.26368610 v1 · relevance 0.07

- **In one sentence**: A target trial emulation using US electronic health records (8,688 patients, first-line therapy 2011–2023) tests whether benefit from immunotherapy-based regimens varies with machine-learning-predicted 6-month baseline survival across five advanced solid tumor comparisons.
- **In plain words**: Doctors must choose first-line treatment for patients with advanced cancer, and some immunotherapy drugs cause early deaths in trials, especially in frail patients who are often given immunotherapy alone because it seems gentler. This study used real-world hospital records from the US to copy the design of trials and asked whether patients with a worse outlook gain more from adding chemotherapy than from immunotherapy alone. In head and neck, urothelial (bladder-lining), and possibly lung cancers, the answer was that patients with poorer predicted survival appeared to benefit more from chemotherapy-containing regimens, while in colorectal cancer and melanoma immunotherapy helped across the range of predicted prognosis.
- **Why it matters**: Trials rarely enroll the sickest patients, so this suggests baseline prognosis could guide treatment choice alongside tumor biomarkers. It is observational data, so the gradients are associations that may be affected by unmeasured differences between patients; the lung cancer result was not clearly significant.
- **Background needed**: - Immune checkpoint inhibitors (ICIs) are drugs that release the brakes on the immune system; pembrolizumab and nivolumab are examples.
- Chemotherapy and targeted therapy (e.g., BRAF/MEK inhibitors) are the main alternatives compared here.
- Target trial emulation: analyzing observational records as if they were a randomized trial, to reduce bias.
- Flatiron Health: a US electronic health record database of oncology patients.
- PD-L1 CPS/TPS, dMMR/MSI-H: tumor biomarkers used to predict who responds to immunotherapy.
- Restricted mean survival time (RMST): the average survival time over a fixed window (here 2 years), a way to compare groups.
- Overlap weighting and pseudo-observation regression: statistical methods for balancing groups and modeling survival.
- Interaction P value: tests whether the treatment effect differs across levels of a factor such as predicted prognosis. · level: research-level

<details><summary>Original abstract</summary>

Background In randomized trials, first-line immune checkpoint inhibitor (ICI)-based therapy has shown excess early mortality versus chemotherapy- or targeted therapy-containing regimens. ICI monotherapy is often chosen for frail patients because it is perceived as less toxic. Whether treatment benefit varies with baseline prognosis is unknown, as poor-prognosis patients are underrepresented in trials. Methods Using the US Flatiron Health electronic health record-derived database, we emulated target trials among 8,688 patients initiating first-line therapy during 2011-2023 across five comparisons: pembrolizumab plus chemotherapy versus pembrolizumab in head and neck squamous cell carcinoma (HNSCC; PD-L1 CPS [&ge;] 1 or unknown) and non-small cell lung cancer (NSCLC; PD-L1 TPS [&ge;] 50%); carboplatin plus gemcitabine versus pembrolizumab in urothelial carcinoma; pembrolizumab versus chemotherapy in dMMR/MSI-H colorectal cancer; and ipilimumab plus nivolumab versus BRAF/MEK inhibition in BRAF-mutant melanoma. Baseline prognosis was estimated with machine learning models predicting 6-month survival. Overlap-weighted pseudo-observation regression evaluated whether differences in 2-year restricted mean survival time (RMST) varied with predicted survival. Results In HNSCC, adding chemotherapy to pembrolizumab did not clearly improve RMST overall (11.5 days; 95% CI, -18.4 to 41.1), but benefit was 102.4 days greater at the 10th versus 90th percentile of predicted survival (95% CI, 40.5 to 164.3; interaction P=.001). Similar gradients favored carboplatin plus gemcitabine over pembrolizumab in urothelial carcinoma (10th-90th percentile difference, 51.4 days; 95% CI, 4.8 to 98.1; P=.03) and, less certainly, adding chemotherapy to pembrolizumab in NSCLC (73.7 days; 95% CI, -3.7 to 151.2; P=.06). Higher-risk patients in these cohorts were more often trial-ineligible. ICI-based therapy improved overall RMST in colorectal cancer (difference, 79.7 days; 95% CI, 49.5 to 107.0) and melanoma (68.3 days; 95% CI, 33.9 to 101.9), without clear variation by predicted survival (interaction P=.32 and P=.91). Conclusions Among patients with poorer prognosis, chemotherapy-containing regimens were associated with greater benefit than ICI monotherapy in HNSCC and urothelial carcinoma, and possibly NSCLC. ICI-based therapy appeared beneficial across prognosis in dMMR/MSI-H colorectal cancer and BRAF-mutant melanoma. Baseline prognosis may complement tumor biomarkers when selecting first-line immunotherapy strategies.

</details>

## Health informatics and medical AI

### [Interpretable competing-risk prediction of hepatocellular carcinoma in cirrhosis from region-wide routine health data](https://www.medrxiv.org/content/10.64898/2026.11.19.26368516v1)
*Gutierrez-Alvarez, I.; Rojas, A.; Calzadilla-Bertot, L. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368516 v1 · relevance 0.12

- **In one sentence**: A three-class, interpretable Explainable Boosting Machine trained on one year of routine electronic health records predicts 12-month hepatocellular carcinoma (liver cancer) in cirrhosis while treating death or liver transplant as a competing outcome, and outperformed aMAP and the Toronto HCC Risk Index in a region-wide Andalusian cohort.
- **In plain words**: The study looks at who with advanced liver scarring (cirrhosis) is likely to develop liver cancer within the next year. Because many of these patients die of liver failure before any cancer appears, the model was built to score cancer risk and death risk separately. Using routine records from a large regional health database, it discriminated cancer risk better than two established scoring tools, and it shows which abnormal lab values point toward cancer and which point toward liver failure.
- **Why it matters**: Liver cancer is often found late in people with cirrhosis, so better short-term risk estimates could help decide who gets closer surveillance. The approach of using routine data and showing how each value contributes may be useful for clinical decision support, but the text is a retrospective study with cross-validation and a single region's data, so external validation and effects on patient outcomes remain unknown.
- **Background needed**: - Cirrhosis: late-stage scarring of the liver, a major risk factor for liver cancer (hepatocellular carcinoma, HCC).
- Competing risk: when another event (here death from liver disease or liver transplant) prevents the outcome of interest from happening, so it must be modelled alongside it.
- aMAP and Toronto HCC Risk Index: existing clinical scores that estimate liver cancer risk from routine measurements.
- Explainable Boosting Machine: a machine-learning method built from simple per-variable curves, so each input's effect can be inspected.
- AUROC / time-dependent AUC: measures of how well a model ranks patients who will and will not develop the outcome (0.5 is chance, 1.0 is perfect).
- Cross-validation: repeatedly splitting data into training and test parts to estimate performance on unseen patients.
- AFP (alpha-fetoprotein) is a blood marker often raised in liver cancer; bilirubin and albumin reflect liver function. · level: research-level

<details><summary>Original abstract</summary>

Background. Short-term prediction of hepatocellular carcinoma (HCC) in cirrhosis is complicated by the competing risk of death from liver disease. We aimed to develop an interpretable model on region-wide routine data that predicts HCC while separating competing mortality, and to compare it with established risk scores. Methods. From a region-wide cohort of adults with cirrhosis in the Andalusian Population Health Database, we trained the model on 17,177 patients with a prediction date set 12 months before their outcome, between 2020 and 2023. From one year of electronic health records before that date (demographics, liver and chronic disease codes, and eight routine laboratory tests), an Explainable Boosting Machine without interaction terms classified the following 12 months as HCC, death or liver transplantation without HCC, or event-free. We evaluated it in 20 repeats of 5-fold cross-validation against a binary model, a model with pair interactions and a model using the full health record, all on the same folds. We then applied the cross-validated models, without retraining, at the first routine encounter at which aMAP or the Toronto HCC Risk Index could be computed, and compared them with the scores in patients followed forward under competing risks, with and without a 6-month washout and with each province left out of training in turn. Findings. 771 patients (4.5%) developed HCC within 12 months and 3,314 (19.3%) died or underwent liver transplantation without HCC (3,061 deaths, 253 transplants). In cross-validation, the area under the receiver operating characteristic curve (AUROC) for HCC was 0.734 (SD 0.018). A binary formulation, pairwise interactions and the full health record (more than 3,000 features) did not improve it; the full record lowered it by 0.024. At routine encounters the model discriminated 12-month HCC better than aMAP (time-dependent AUC 0.790 vs 0.688; difference +0.102, 95% CI +0.071 to +0.132) and the Toronto HCC Risk Index (0.761 vs 0.703; +0.057, +0.032 to +0.081), and remained better after excluding HCC diagnosed within 6 months (concordance difference +0.055 and +0.040) and when each of the eight provinces was left out of training. At equal group size, its high-risk group held as much HCC as the scores' high-risk categories, with 20-28% fewer competing deaths. Its shape functions separated cancer-specific signal (AFP rising from 2 to 20 g/L, platelets below 150 x10^9/L) from liver failure (bilirubin above 51 mol/L, albumin below 35 g/L); a binary model showed only the first. Interpretation. An interpretable three-class model on routine data outperformed established scores for short-term HCC risk in cirrhosis, while showing whether each abnormal value points to cancer or to competing death.

</details>

### [Unified Machine Learning Model for Early Detection of Mild Cognitive Impairment, Frailty, and Fall Risk Using Multimodal Motor-Function Data](https://www.medrxiv.org/content/10.64898/2026.11.19.26368462v1)
*Akter, S.; Guess, T.; Sarker, S. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.19.26368462 v1 · relevance 0.09

- **In one sentence**: A small study (n=79 community-dwelling older adults) tests a single multi-label machine learning model that predicts mild cognitive impairment, frailty and fall risk together from sensor-based motor tests, comparing it with separate single-label models and probing its explanations and robustness.
- **In plain words**: Older adults often have memory decline, physical frailty and a higher risk of falls at the same time, and these are usually screened separately. This paper asks whether one model, built from a single sensor-based movement assessment (walking, standing up from a chair, balance, stepping, and reaction time, some done while doing a second task), can flag all three. The authors report that the combined model performed about as well as three separate models, with its best accuracy for memory impairment and weaker results for frailty and fall risk.
- **Why it matters**: Screening several age-related conditions in one short test could make checkups quicker and cheaper if the approach holds up. The text reports only modest accuracy (overall mean AUC 0.645) and a small sample, and the authors themselves say recalibration and external validation are needed before any clinical use.
- **Background needed**: - Mild cognitive impairment (MCI): early memory or thinking decline that is not yet dementia.
- Frailty: a state of low physical reserve and weakness that raises vulnerability to health problems.
- Fall risk: the likelihood that a person will fall, which is often assessed through movement tests.
- Machine learning classifier: a program that learns patterns from labeled examples to predict a category.
- Multi-label classification: predicting several yes/no conditions for the same person at once, instead of one.
- AUC (area under the ROC curve): a 0.5 score means chance-level discrimination and 1.0 means perfect separation.
- Cross-validation: a way of testing a model on data it was not trained on, to estimate real-world performance.
- SHAP: a method that shows how much each input feature pushed a prediction up or down.
- Dual-task condition: a movement test done while also performing a mental task, which can reveal hidden problems. · level: research-level

<details><summary>Original abstract</summary>

Background: Mild cognitive impairment (MCI), frailty, and fall risk often co-occur in older adults and share motor signs, yet they are screened and modeled separately. A unified model that predicts all 3 conditions from 1 sensor-based assessment could support earlier and more efficient screening, but such a model has rarely been developed or rigorously compared with separate models. Objective: This study aimed to develop a unified machine learning model that predicts MCI, frailty, and fall risk together from sensor-based motor-function data, compare it with separate single-label models, explain its predictions, and test its robustness. Methods: Community-dwelling older adults (n=79) completed a multimodal motor-function assessment with the Mizzou Point-of-Care Assessment System (MPASS), covering gait, sit-to-stand, static balance, step-down, and reaction time, with some tasks repeated under a dual-task condition. With demographic and family-history data, this yielded 59 features. Unified classifier-chain and single-label models were built with 5 algorithms across 6 modeling stages, evaluated with repeated nested cross-validation, and compared using the area under the receiver operating characteristic curve (AUC) and paired bootstrap tests. The final model was explained with Shapley additive explanations (SHAP), and its robustness and the sufficiency of the sample size were tested with chain-input, chain-order sensitivity, domain-ablation, learning-curve, and power analyses. Results: With class weighting, the unified model had a higher mean AUC than the single-label models in 17 of 20 configurations and was never significantly worse, and it performed at least as well under nested model selection (0.615 vs 0.605; P=.58). The final extra trees model achieved a mean AUC of 0.645 (95% CI 0.569-0.722); discrimination was best for MCI (AUC 0.779, 95% CI 0.680-0.872) and lower for frailty (0.606) and fall risk (0.551). The model overestimated risk for all 3 outcomes, most for frailty. Most features (43/59, 73%), led by stride length, were shared across the 3 conditions, with consistent SHAP rankings in training and test participants ({rho}=0.99). Predicted frailty was the most important input for fall risk, and the 45 sensor features alone performed as well as the full model. Learning curves suggested that fall-risk prediction would benefit from more participants. Conclusions: A unified model predicted MCI, frailty, and fall risk together from one sensor-based assessment and performed as well as 3 separate models. It identified motor features shared across the conditions and used the link between frailty and fall risk. It performed best for MCI; with improvement for frailty and fall risk, recalibration, and external validation, such a model could support efficient screening of older adults for several conditions at once. KEYWORDS mild cognitive impairment; frailty; fall risk; machine learning; multi-label classification; classifier chain; gait; dual task; explainable artificial intelligence; Shapley additive explanations.

</details>

## Econometrics and applied economics

### [The Rise of Agents and the Human Labor Market](https://arxiv.org/abs/2611.27210)
*Nicola Borri, Anton Cheremukhin, Yukun Liu et al.* · `econ.GN` · arXiv:2611.27210v1 · relevance 0.08

- **In one sentence**: Using OpenRouter token-consumption data and Lightcast job postings, the paper estimates how firm-level exposure to agentic AI (measured via stock-return comovement with aggregate agentic token use) predicts subsequent declines in U.S. public-firm job postings, including an event study around the Claude Code 2.0 release.
- **In plain words**: The paper asks whether AI agents, software that carries out multi-step tasks on its own, are reducing the number of job openings at companies. The authors track how much AI is actually being used across many models, and how each public company's stock moves with that usage, to rank firms by how exposed they are. They find that more exposed firms post fewer new jobs in the following months, and that the drop is concentrated in non-senior roles.
- **Why it matters**: Most earlier work on AI and jobs uses occupation exposure scores or survey data, so a firm-level, usage-based measure tied to agents is a new angle. It bears on the wider debate about whether AI is substituting for entry-level or routine white-collar work, though the text alone does not establish causation beyond the event-study design.
- **Background needed**: - Job postings: openings firms advertise; their growth is used as an early signal of hiring demand.
- AI agents: AI systems that plan and take multi-step actions (e.g., writing and running code), as opposed to answering a single prompt.
- Tokens: the chunks of text an AI model reads and writes; total token counts are a proxy for how much AI is being used.
- Stock-return comovement ("beta"): how strongly a firm's share price moves with a market-wide factor; here, with aggregate agentic AI usage.
- Event study: comparing outcomes before and after a specific event (here, the Claude Code 2.0 release) to isolate its effect.
- Standard deviation: a unit of spread; the results are reported per one-standard-deviation difference in exposure.
- Senior vs. non-senior jobs: a split by seniority level used to see which roles are affected. · level: research-level

<details><summary>Original abstract</summary>

We provide the first economy-wide and cross-AI model evidence on the effects of agentic AI on labor demand. We combine proprietary OpenRouter data covering about two quadrillion tokens of realized AI consumption (2 percent of global AI token consumption) across more than 400 AI models, including 1.1 quadrillion agentic tokens, with the full text of 34.8 million U.S. job postings for public firms from Lightcast. We compute our measure of firm-level exposure to aggregate agentic AI consumption (agentic beta) using the comovement of U.S. public firms' stock returns with realized weekly aggregate agentic AI token consumption. We find that a one-standard-deviation increase in a firm's exposure to agentic AI predicts 2.11 percent lower growth in job postings over the next six months and 3.20 percent over nine months. We then conduct an event study based on the release of Claude Code 2.0, which significantly expanded the capabilities of AI agents, and show that a one-standard-deviation higher pre-release exposure to agentic AI predicts 4.73 percent lower posting growth over six months post the release. Furthermore, we show that the decrease in job postings is concentrated among non-senior jobs and is statistically insignificant for senior jobs. In contrast, we find no statistically significant relation between broad AI realized consumption exposure and subsequent job posting growth once agentic exposure is controlled for. Finally, we validate our market-implied agentic exposure measure using independent evidence from firms' mentions of AI deployment in securities filings and earnings calls.

</details>

### [Partially Identified Ambiguity](https://arxiv.org/abs/2602.07634)
*Cheaheon Lim* · `econ.TH` · arXiv:2602.07634v3 · relevance 0.06

- **In one sentence**: The paper asks whether conditional Gamma-minimax (a robust Bayesian rule that conditions on observed data) satisfies Aumann plausibility under partial identification, and characterizes when it does via "partially identified ambiguity" in the prior set.
- **In plain words**: When data cannot pin down an unknown quantity exactly, analysts use a set of possible prior beliefs rather than a single one. This paper asks whether it is sensible to update that set of beliefs using the observed data, and finds that a common updating rule can break a natural consistency requirement. The authors say the requirement holds only when the set of priors has a specific structure they call partially identified ambiguity.
- **Why it matters**: Robust Bayesian methods are widely used when models are only partly identified, so the question of whether to condition on data affects how such results are reported. The text does not show how widely these methods are adopted or what practical errors follow, so the practical stakes are unclear from this abstract alone.
- **Background needed**: - Partial identification: data only narrow an unknown parameter to a set of values (an "identified set"), not a single value.
- Prior: a probability distribution expressing beliefs before seeing data; a "prior set" is a collection of such distributions.
- Robust Bayesian analysis: reasoning with a set of priors instead of one, to guard against dependence on a single belief.
- Gamma-minimax: a decision rule that picks the action with the best worst-case expected outcome across the prior set.
- Conditioning on the data: updating each prior in the set using Bayes' rule after observing data.
- Aumann expectation: the set-valued analogue of an average, taken over a random set of distributions.
- Aumann plausibility: a set-valued version of the rational expectations idea that beliefs should be consistent with the true data-generating process. · level: research-level

<details><summary>Original abstract</summary>

This paper addresses the normative question of whether one should condition on the data when performing robust Bayesian analysis under partial identification. We provide an ex ante representation of the conditional Gamma-minimax criterion and show that it can violate Aumann plausibility, a set-valued generalization of the rational expectations property. Our main characterization result establishes that Aumann plausibility holds if and only if the decision maker's prior set exhibits partially identified ambiguity. The latter condition requires the prior set to equal the Aumann expectation of a random set of distributions supported on the parameter's identified sets. We interpret these results as suggesting that conditional Gamma-minimax should only be used under partially identified ambiguity. The implications for various robust Bayesian methods are discussed.

</details>

## Economic theory

### [Exchange rights and vacancy priorities](https://arxiv.org/abs/2611.27684)
*\"Ozg\"un Ekici, M. Bumin Yenmez* · `econ.TH` · arXiv:2611.27684v1 · relevance 0.05

- **In one sentence**: The paper studies strategy-proof, individually rational allocation rules for policies that combine permitted position exchanges with priority-based allocation of announced vacancies, showing when such rules exist, introducing the propose-and-trade rule, and characterizing it against classic deferred acceptance and top trading cycles.
- **In plain words**: The paper looks at institutions, such as school or job placement systems, where people already holding positions can swap them, and where open spots go to whoever has priority. It asks when a fair assignment rule can protect both the right to swap and the priority for open spots, so that nobody gains by misreporting their preferences. The authors find that such a rule exists exactly when the policy has no "conflict cycles," and they propose a rule called propose-and-trade that works in those cases.
- **Why it matters**: Allocation systems that mix reassignment with vacancy filling are common, and the paper clarifies exactly which policy designs allow a manipulation-resistant rule. The text does not show practical adoption or empirical impact, so its significance beyond theory is unclear from the summary alone.
- **Background needed**: - Strategy-proof rule: a matching procedure where reporting true preferences is always best, so no one gains by lying.
- Individually rational: nobody is assigned something worse than what they already hold.
- Priorities: rankings that decide who gets a vacant position first when several people want it.
- Deferred acceptance and top trading cycles: two classic matching procedures in economic theory, used here as benchmarks.
- Core allocation: an assignment that no group of participants could improve by trading among themselves.
- Conflict cycle: a circular pattern of exchanges and vacancy claims that blocks a consistent rule. · level: research-level

<details><summary>Original abstract</summary>

Many institutions let incumbents exchange positions while allocating announced vacancies by priority, withdrawing positions released by vacancy recipients. A policy specifies permitted exchanges, vacancy eligibility, and priorities. A strategy-proof, individually rational rule protecting exchange rights and vacancy priorities exists precisely for policies without conflict cycles. Restricting protection to first choices does not enlarge this class. We introduce the propose-and-trade rule, which satisfies these properties and selects the applicant-optimal core allocation under every conflict-free policy. We identify when propose-and-trade is the unique strategy-proof, individually rational rule protecting first choices. These axioms characterize deferred acceptance and top trading cycles in their classic settings. Under a policy with a conflict cycle, propose-and-trade is manipulable but protects exchange rights and first-choice claims. Replacing it with any strategy-proof rule makes some applicant worse off at some profile. We show when priority reform alone can eliminate conflict cycles and when eligibility or exchange permissions must change.

</details>

## Game theory and algorithmic economics

### [Stinespring's Dilation, Universal-NOT, and Limitations of Quantum Uncoupled Learning](https://arxiv.org/abs/2611.27251)
*Emmanouil-Vasileios Vlatakis-Gkaragkounis, Pucheng Xiong* · `quant-ph` · arXiv:2611.27251v1 · relevance 0.09

- **In one sentence**: The paper shows that quantum versions of uncoupled learning dynamics, where each player updates a quantum strategy using only their own payoff and a physical copy of the opponent's state, cannot reach Nash equilibrium in certain conjugation games under memoryless or finite-memory rules, while small classical memory can help for finite target families.
- **In plain words**: The paper studies how two players, each choosing a quantum state, might learn their way to a stable outcome when each only sees their own payoff and gets a physical copy of the other's current state. The authors show that for a specific family of simple two-player games, no memoryless rule that follows the laws of quantum physics can reach the equilibrium. They also show that a small amount of classical memory fixes this for a finite set of target strategies, but not for all possible pure qubit targets.
- **Why it matters**: It sharpens the question of what decentralized learning can achieve when updates must be physically realizable, a constraint with no classical counterpart. The connections it draws to quantum information theory (Stinespring's dilation theorem and the universal-NOT fidelity bound) suggest a useful bridge between game-theoretic learning and quantum physics, though the broader implications are not spelled out in the text.</why>
<parameter name="background">- Nash equilibrium: a set of strategies where no player gains by switching alone.
- Uncoupled learning: each player adjusts using only their own payoff, not others' payoffs or strategies.
- Qubit: the quantum analogue of a bit; a strategy here is a quantum state of one qubit.
- Quantum channel: a physically allowed way to transform a quantum state (it must be realizable by a physical process).
- Conjugation game: a game where one player's best reply is the transpose (a mathematical flip) of the other's pure strategy.
- Stinespring's dilation theorem: a standard result stating every physical quantum operation can be implemented by adding an auxiliary system and acting unitarily.
- Universal-NOT: a quantum operation that tries to flip an unknown state; its best achievable fidelity is a known limit (Buzek, Hillery, Werner).
- Memoryless vs. finite-memory: whether the update rule can use past information beyond the current state.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Uncoupled learning, in which players know only their own payoff, are a standard model of decentralized learning toward Nash equilibrium. We study their quantum counterpart, where strategies are quantum states and, in each round, a player receives a physical copy of their opponent's current strategy and updates their own state by a quantum channel. This adds to uncoupledness a constraint with no classical analogue: every update must be physically realizable. In fact, this constraint is decisive in conjugation games, in which Bob has a strictly dominant pure strategy and Alice's unique best response is its transpose. In this work, we show some limitations of uncoupled (learning) dynamics in finding the Nash equilibrium for conjugation games. First, we prove that no autonomous, memoryless, uncoupled dynamics converge to Nash equilibrium in a family of four single-qubit conjugation games. Specifically, any memoryless channel that keeps all four equilibria fixed will leave Alice's strategy frozen. This result also extends to $4^n$ games on $n$-qubit registers. Second, we show that this barrier disappears with a small classical memory: for any finite family of $L$ pure targets, a guess-and-test rule with $O(\log L)$ classical bits converges to equilibrium, with an explicit bound on its convergence rate. Finally, we prove that no finite memory, classical or quantum, suffices for the continuum of all pure-qubit targets. Our proof of the impossibility for memoryless channels relies on Stinespring's dilation theorem, while the impossibility for finite-memory channels relies on the optimal universal-NOT (in)fidelity bound by Bu\v{z}ek, Hillery, and Werner.

</details>

### [Learning under Bounded Manipulation for Quadratic Incentive Design](https://arxiv.org/abs/2611.26736)
*Arda G\"u\c{c}l\"u, Subhonmesh Bose, Tamer Ba\c{s}ar* · `cs.GT` · arXiv:2611.26736v1 · relevance 0.07

- **In one sentence**: A repeated quadratic incentive design game in which a leader learns a follower's private type from noisy actions while the follower may strategically deviate from myopic best responses, giving a minimax regret rate of max{log T, min{C_T, T}} under a manipulation budget C_T, with a matching lower bound and policy.
- **In plain words**: A leader wants to set incentives for a follower but does not know the follower's private type, so she estimates it from the follower's noisy actions. The follower knows how she learns and may act slightly differently from his best short-term choice to steer her future estimates. The paper measures how much this manipulation, capped by a budget, costs the leader in regret, and finds a matching best-possible rate along with a simple learning method that achieves it.
- **Why it matters**: It gives a precise accounting of how strategic behavior that distorts the data a learner sees limits learning performance, which matters for pricing, mechanism design and any setting where the people being learned about can game the learner. The text does not show applications beyond this formal model, so broader relevance is uncertain.
- **Background needed**: - Incentive design: a leader offers rewards or rules (here an affine rule) to shape a follower's actions.
- Private type: a hidden parameter of the follower that the leader must estimate.
- Regret: the total loss of the leader compared with an optimal player who knew the type from the start; minimax means the best worst-case guarantee over all followers.
- Manipulation budget C_T: a cap on the expected total squared deviation the follower may make from his myopic best response over T rounds.
- Approximately rational follower: one who responds nearly optimally, not perfectly.
- Lower bound: a proof that no policy can do better than a given rate, here information-theoretic, meaning it holds regardless of computing power.
- Log T: a slowly growing term typical of learning problems where the number of rounds is T. · level: research-level

<details><summary>Original abstract</summary>

We study a repeated quadratic incentive design game in which a leader learns a follower's private type from noisy observations of the follower's actions and uses her estimates in an affine incentive rule. The follower knows the leader's learning policy, which incorporates past observations to produce estimates of the follower's type, and can deviate from his myopic best response to influence the leader's future estimates. We ask how the follower's ability to manipulate these observations affects the leader's performance. Under a manipulation budget $C_T$ constraining the expected cumulative squared deviation of the follower's actions from his myopic best response, we establish a minimax regret rate of order $\max\{\log T, \min\{C_T,T\}\}$ for approximately rational followers. Our information-theoretic lower bound applies to a general class of causal estimation and manipulation policies for the leader and the follower. We provide a simple learning policy that achieves the lower bound. Finally, we show that under a fixed learning rule, increasing the manipulation budget of the follower can counterintuitively reduce the leader's regret.

</details>

## Mathematical finance

### [A Solvency II-Based Framework for Pricing Structural Longevity Risk under an Affine Mortality Model](https://arxiv.org/abs/2611.26670)
*Madiha Bouhouche (INSEA), Said Khalil (TREE, INSEA) et al.* · `q-fin.PR` · arXiv:2611.26670v1 · relevance 0.05

- **In one sentence**: The paper proposes a Solvency II Cost-of-Capital pricing framework for structural longevity risk, using a continuous-time affine mortality model with a latent longevity factor, and compares a trend-based stress with a mortality-level stress on Belgian data.
- **In plain words**: The paper looks at how an insurer should price the risk that people live longer than expected, a risk that matters for pension and annuity books. It builds a pricing method that follows the European insurance rules (Solvency II) for holding capital against that risk, using a mathematical model of how mortality changes over time. On Belgian mortality data, the authors find that stressing the mortality level produces much larger capital-cost figures than stressing the long-run trend.
- **Why it matters**: Longevity risk is a major concern for insurers and pension funds, and the paper ties together mortality modelling and prudential capital rules. The text shows that the choice of adverse scenario changes the result a lot, which is a useful point for regulators and practitioners; its wider practical impact is not established from the abstract alone.
- **Background needed**: - Longevity risk: the danger that people live longer than an insurer or pension fund has assumed, so payouts last longer than planned.
- Solvency II: the European Union regulatory regime for insurers, which sets how much capital they must hold.
- Best Estimate: the probability-weighted present value of future cash flows, without a safety margin.
- Solvency Capital Requirement (SCR) and Risk Margin: the capital buffer for severe losses, and the extra charge reflecting the cost of holding that capital for others to pay for.
- Cost-of-Capital principle: the Risk Margin is the annual cost of the capital held, discounted over time.
- Affine mortality model: a model where mortality rates depend on a hidden (latent) factor in a way that keeps calculations, such as survival probabilities, in simple closed form.
- Value-at-Risk (VaR): a loss level not expected to be exceeded at a given confidence level.
- Incomplete market: a market where some risks cannot be fully hedged or traded away. · level: research-level

<details><summary>Original abstract</summary>

This paper develops a Solvency II-based pricing framework for structural longevity risk in incomplete longevity markets. The valuation scheme relies on the Cost-of-Capital principle underlying the Risk Margin and combines it with a continuous-time affine mortality model. Mortality dynamics are specified in calendar time, with age-dependent mortality patterns linked to a latent longevity factor driving long-term mortality improvements. The affine structure preserves closed-form survival probabilities and provides a tractable basis for repeated Best Estimate, Solvency Capital Requirement and Risk Margin calculations. We derive the conditional distribution of one-year discounted Best Estimate variations, obtaining analytical expressions for their asymmetry and Value-at-Risk under the Gaussian affine specification. Within this setting, we introduce a stress-based assessment by applying adverse shocks to the deterministic parameters governing the longevity trend. The trend-based stress is compared with a mortality-level stress and with a Value-at-Risk-based capital assessment. The methodology links stochastic mortality modelling, prudential capital valuation and longevity-linked payoff assessment within a unified actuarial framework. A numerical application based on Belgian mortality data illustrates the implementation and shows that the mortality-level stress produces substantially larger scenario-based capital-cost measures than the trend-based stress. These findings highlight the sensitivity of longevity risk valuation to the specification of adverse mortality scenarios. The approach offers a transparent and operational basis for assessing and pricing structural longevity risk under a Solvency II Cost-of-Capital perspective.

</details>

### [Risk sharing for background risk models with infinite mean](https://arxiv.org/abs/2611.27485)
*Ziting Miao, Yuyu Chen, Han Li* · `q-fin.RM` · arXiv:2611.27485v1 · relevance 0.04

- **In one sentence**: The paper studies when risk sharing among agents with positively dependent infinite-mean losses, modeled with background risk, can increase total risk in the usual stochastic order, under linear and conditional mean sharing rules.
- **In plain words**: The paper asks whether pooling and splitting a risk among several people, which normally makes things safer, can backfire when the possible losses are so heavy-tailed that their average size is effectively infinite. The authors show that under the stated conditions, sharing such losses can make the overall risk larger, and they check this for common heavy-tailed multivariate models. In that setting, keeping the original risk or a less diversified split is preferred under any law-invariant monotone risk measure that works for infinite-mean models.
- **Why it matters**: Risk sharing is a basic idea in insurance and finance, and the usual argument that diversification helps assumes finite averages. This work points to a specific setting where that assumption fails, which matters for pricing and regulating heavy-tailed risks; the text itself does not go beyond the stated results, so wider practical impact is unclear.
- **Background needed**: - Risk sharing: splitting a total loss among several agents, e.g., through linear or conditional-mean allocation rules.
- Background risk: an extra independent source of uncertainty that affects every agent's wealth.
- Infinite-mean (heavy-tailed) losses: distributions such as Pareto where the average loss is unbounded, so usual averages and variances do not exist.
- Positive dependence and copulas: a copula is a function describing how variables move together, separate from their individual distributions; Archimedean copulas (e.g., Clayton, Gumbel-type) are common examples.
- Stochastic order: one risk is "larger" than another if it takes bigger values with higher probability across all thresholds.
- Law-invariant monotone risk measure: a rule for scoring risk that depends only on the distribution and gives higher scores to larger losses.
- Stable distributions and peakedness: stable laws generalize the normal and allow heavy tails; peakedness compares how concentrated a distribution is around its center. · level: research-level

<details><summary>Original abstract</summary>

Risk sharing is usually viewed as beneficial for risk-averse agents facing independent risks with finite means, but this situation can be reversed for infinite-mean losses. In this paper, we explore the effects of risk sharing for positively dependent infinite-mean losses using background risk models. Under both linear and conditional mean risk sharing, we show that risk sharing of infinite-mean losses can increase the risk in the sense of usual stochastic order. Our results cover classical multivariate loss distributions, including the Pareto-Clayton and the Fr\'echet-Gumbel models. For linear risk sharing, we further derive stochastic dominance relations between diversified portfolios, including those with Pareto marginals coupled by convex mixtures of commonly used Archimedean copulas. For conditional mean risk sharing, we additionally discuss peakedness and stochastic order relations for stable distributions. Consequently, under the stated conditions, retaining the original risk or a less diversified portfolio is preferred under every law-invariant monotone risk measure that is well defined for infinite-mean models.

</details>

## Financial markets

### [Nonlinear Shrinkage for Higher Moments Estimation in Large Portfolios](https://arxiv.org/abs/2611.27274)
*Paul Ruelloux, Christian Bongiorno, Damien Challet* · `q-fin.PM` · arXiv:2611.27274v1 · relevance 0.07

- **In one sentence**: The paper extends covariance cleaning methods (cross-validated filtering and the Average Oracle approach) to even-order co-moment tensors, such as cokurtosis, and tests them on large portfolios of Russell 1000 stocks.
- **In plain words**: Investors care about more than how much a portfolio's returns vary; they also care about how often extreme gains and losses occur. Estimating these higher-order measures from historical data is very noisy when a portfolio holds many assets. The authors develop filtering methods that reduce this noise and test them on historical returns of Russell 1000 stocks.
- **Why it matters**: The text reports that the filtered estimates were more accurate out of sample than plain sample estimates, and that this carried over to portfolio volatility and kurtosis, including when the portfolio objective penalized the fourth moment. Its relevance beyond this dataset and setup is not shown in the text.
- **Background needed**: - Portfolio returns have a variance (volatility), which is the second moment, and a kurtosis, which is the fourth moment and reflects how heavy the tails are.
- A covariance matrix records how pairs of assets move together; coskewness and cokurtosis extend this to three- and four-way co-movements, stored in tensors (multi-dimensional arrays).
- "Noisy" estimates come from limited historical data; with many assets, sample estimates can be unreliable.
- Shrinkage or filtering means adjusting raw estimates toward more stable values to reduce estimation error.
- Out-of-sample testing evaluates a method on data not used to build it.
- The Frobenius error is a standard way of measuring the overall size of the gap between an estimated matrix or tensor and the true one. · level: research-level

<details><summary>Original abstract</summary>

Portfolio risk is not limited to the variance of returns. The moments of portfolio returns depend directly on the covariance matrix and higher-order co-dependences (coskewness, cokurtosis, etc.). In practice, however, these objects are extremely noisy, especially for large portfolios. Here we introduce filtering methods based on tensor decompositions that extend cross-validated covariance cleaning and the Average Oracle methodology to even-order co-moment tensors. Using returns on historical Russell 1000 constituents, we find that the proposed filters improve out-of-sample estimation accuracy relative to sample estimators, both for correlation and cokurtosis tensors, as measured by relative squared Frobenius errors. These improvements translate into lower relative errors on portfolio volatility and kurtosis, and into lower out-of-sample volatility and kurtosis when the portfolio objective penalizes both variance and the fourth moment.

</details>

### [Are Calibrated Decision Models Calibrated on Markets? Geolocated News, Markov Switching and a System One Model for Nasdaq-100 Allocation](https://arxiv.org/abs/2611.26716)
*Jakub Zaj\k{a}c, Micha{\l} Dyrek* · `q-fin.ST` · arXiv:2611.26716v1 · relevance 0.04

- **In one sentence**: A test of whether the Jev probability model, a Markov-switching regime model, and geolocated news features are calibrated against realised Nasdaq-100 outcomes over 88 out-of-sample weeks in 2025 onward, with half-Kelly position sizing.
- **In plain words**: The paper asks whether a tool that gives probabilities for yes/no market questions is accurate about how often the Nasdaq-100 index falls over the next four weeks. Each Friday, the authors compare several forecasting approaches with what the market actually did, and then see what each would have returned if used to size positions. The main finding is that the raw Jev model overstates the chance of a decline, and simply anchoring its forecasts to the long-run historical base rate makes them much better calibrated.
- **Why it matters**: It shows a specific, checkable failure mode: a probability model can look well calibrated on benchmarks yet be miscalibrated on real market outcomes, and that matters when probabilities are used to size positions. The authors' lesson, to anchor probabilities to base rates, is a narrow finding from one index and one test period of 88 weeks, so its wider applicability is uncertain.
- **Background needed**: - Calibration: whether a stated probability matches how often the event actually happens (a forecast of 40% should come true about 40% of the time).
- Expected calibration error (ECE): a single number summarising the average gap between stated probabilities and observed frequencies; lower is better.
- Base rate: the long-run historical frequency of an event, here how often the index falls over four weeks.
- Markov-switching model: a statistical model that assumes markets move between a small number of hidden regimes, such as calm and turbulent.
- AUC: a score from 0 to 1 for how well a model ranks likely events above unlikely ones; 0.5 is no better than chance.
- Platt scaling and isotonic regression: standard methods that adjust raw probabilities to better match outcomes, here reported as not helping.
- Half-Kelly allocation: a position-sizing rule based on expected edge, scaled down by half to reduce risk.
- Sharpe ratio: return earned per unit of volatility taken.
- PostGIS: a geographic database extension used to tag news by location.
- Knowledge probe: a check of what events a language model was trained on, so that test weeks are after its training cutoff. · level: research-level

<details><summary>Original abstract</summary>

Portfolio allocation is driven by probabilities of losses, not only by forecasts of the direction (up/down) of the market. A decision model such as Jev returns a probability for a yes/no question and has been reported to be well calibrated on a set of benchmarks. However, the model's calibration against realised market outcomes has not been tested. In this study, every Friday we ask whether the Nasdaq-100 will close lower four weeks later and compare a two-regime Markov-switching model estimated on data from 1990 to 2026, Jev reading weekly headlines and geolocated news features computed with spatial queries in PostGIS, and their combination. A knowledge probe shows that Jev knows events up to late 2024, so we evaluate it on 88 weeks from January 2025 onwards. None of the models predicts the direction better than the historical base rate. A key finding is that raw Jev overestimates the probability of a decline: its mean forecast is 0.48 against an observed frequency of 0.38, and its ECE is 0.10. A prior shift to the historical base rate, which uses no outcomes from the test period, lowers the ECE to 0.015. In contrast, Platt scaling, isotonic regression and the combination with the Markov model all make the forecasts worse. In a half-Kelly allocation, the raw Jev strategy returns 3.1% per year, whereas after the prior shift it returns 14.5%; a simple buy-and-hold strategy in QQQ returns 15.3% per year. The Markov model forecasts large declines (more than 10%) well, with an AUC of 0.81, and its strategy has the highest Sharpe ratio over 1999-2026. Asked about such a large decline (base rate 4%), raw Jev forecasts 16-24% on average, and the same prior shift removes this offset. The practical lesson is that decision-model probabilities must be anchored to the base rate of the market event before they are used to size positions.

</details>

## Signal processing

### [DNN-Assisted Deterministic Policy Learning for Adaptive IRS-NOMA-OWC Networks](https://arxiv.org/abs/2611.26742)
*Ahrar N. Hamad, Ahmad A. Qidan, Taisir E. H. El-Gorashi et al.* · `cs.IT` · arXiv:2611.26742v1 · relevance 0.07

- **In one sentence**: The paper proposes a two-stage deep neural network plus deterministic-policy deep reinforcement learning framework that jointly sets power allocation and reflector (IRS mirror) orientations in an indoor IRS-assisted NOMA optical wireless network, with the decoding order adapted to channel gains.
- **In plain words**: The paper looks at how to keep indoor wireless-by-light connections fast and fair when people are moving and the light path can be blocked. A small set of mirrors, called an intelligent reflecting surface, bounces light toward users, and the system must decide how much power to give each user and where to aim the mirrors. The authors use a neural network to estimate where users are and how they are oriented, then a learning method to pick the power and mirror settings.
- **Why it matters**: Light-based indoor networks are a possible complement to radio, and the main difficulty is blocked line-of-sight paths for moving users. The reported comparisons (against standard learning methods, conventional optimization, and no-mirror setups) suggest the approach could help, but the text is only an abstract, so the size and realism of the gains cannot be judged from it.
- **Background needed**: - Optoptical wireless communication (OWC): sending data with light, such as LEDs, instead of radio waves.
- Line-of-sight (LoS) blockage: when a person or object cuts the direct light path between transmitter and receiver.
- Intelligent reflecting surface (IRS): a flat array of adjustable reflectors that steers signals toward users.
- Non-orthogonal multiple access (NOMA): several users share the same channel at once, with different power levels; the receiver decodes signals in a set order.
- Sum rate and QoS: total data throughput across users, and minimum service guarantees per user.
- Deep neural network (DNN) and deep reinforcement learning (DRL): machine-learning models; DRL learns decisions by trial and reward, and a deterministic policy gradient method is one specific DRL technique.
- Non-convex optimization: a hard class of design problems where standard solvers can get stuck or be slow. · level: research-level

<details><summary>Original abstract</summary>

Intelligent reflecting surface (IRS) has been considered a promising technology in optical wireless communication (OWC) networks due to its potential to overcome the line-of-sight (LoS) blockage issue and enhance coverage. In this paper, a dynamic IRS-assisted indoor non-orthogonal multiple access (NOMA)-OWC network is modeled, and an optimization problem is formulated to maximize the sum rate subject to the quality-of-service (QoS) requirements of multiple mobile users, by jointly optimizing the power allocation and the IRS mirror orientations, from which the user's decoding order is induced rather than being fixed. Since the problem is non-convex and the channel conditions vary with user mobility, conventional optimization methods may incur considerable computational overhead. Therefore, a two-stage deep neural network-deep reinforcement learning (DNN-DRL) framework is proposed. In the first stage, the DNN estimates the user's positions and orientations in real time, removing the need for perfect knowledge of the user state. In the second stage, a deterministic policy gradient (DPG)-based DRL algorithm uses these estimates to jointly optimize the power allocation and IRS mirror orientations, with the decoding order updated according to the resulting effective channel gains. The results show that the proposed framework approaches the performance upper bounds and outperforms standard DRL algorithms, conventional optimization methods, and deployments without IRS in terms of sum rate and fairness, while achieving faster convergence. Furthermore, online adaptation of the decoding order maintains higher QoS satisfaction than a fixed decoding order, particularly under high user mobility.

</details>

### [From Pilots to Position: Experimental Near-Field Localization for ISAC](https://arxiv.org/abs/2611.27503)
*Yunxin Li, Emiel Vanspranghels, Jialun Kou et al.* · `eess.SP` · arXiv:2611.27503v1 · relevance 0.06

- **In one sentence**: An experimental study of near-field target localization using OFDM pilot signals from a distributed multi-transmitter, multi-receiver ISAC testbed, comparing coherent backprojection with noncoherent delay-TDOA fusion at 3.4 GHz.
- **In plain words**: The paper asks whether wireless signals meant for communication can also be used to find where an object is, with good accuracy. The authors built a hardware setup with two transmitters and four receivers and tested it on 16 fixed target positions. Two localization methods gave average errors of about 19.8 cm and 18.8 cm, and the effect of signal bandwidth on accuracy was also examined.
- **Why it matters**: Reusing communication signals for sensing could reduce the need for dedicated radar hardware in future wireless networks, so real measurements of achievable accuracy are useful. The text reports only static targets and one hardware setup, so how well these results carry over to moving targets or other environments is not shown here.
- **Background needed**: - ISAC (integrated sensing and communication): using one wireless system to both transmit data and sense the surroundings.
- OFDM: a common modulation scheme that splits a signal across many narrow frequency slots; pilot signals are known reference tones used to estimate the channel.
- Near-field: the close-range zone around an antenna where wavefronts are curved, which changes how position is computed.
- Multistatic / TDOA: using several separate transmitters and receivers and the small differences in signal arrival times to pin down a location.
- Coherent vs. noncoherent: coherent methods use the full phase of the signal; noncoherent methods use only timing or power information, which is more robust to synchronization errors.
- Backprojection: a method that maps measured signal echoes back onto a grid of candidate positions and picks the best match.
- Occupied bandwidth: the width of the frequency band the signal uses; wider bandwidth generally allows finer timing resolution. · level: research-level

<details><summary>Original abstract</summary>

Integrated sensing and communication (ISAC) enables wireless systems to reuse communication signals for environmental sensing, potentially reducing the need for dedicated sensing resources. However, the achievable localization accuracy of communication-centric waveforms under practical hardware constraints remains an important challenge. In this paper, we experimentally investigate near-field target localization using OFDM pilot signals in a distributed communication system. We consider both coherent and noncoherent localization approaches, exploiting multistatic propagation delays and time-difference-of-arrival (TDOA) information extracted from pilot-based channel estimates. A hardware setup comprising two transmitters and four receivers was developed and configured to operate at 3.4 GHz with 198 MHz occupied bandwidth to evaluate localization performance under realistic propagation and synchronization conditions. Experimental results across 16 static target positions demonstrate mean localization errors of 19.8 cm and 18.8 cm for coherent backprojection and noncoherent delay-TDOA fusion, respectively. Furthermore, we investigate the impact of occupied bandwidth on localization accuracy of the two proposed algorithms. These findings provide experimental insights into the capabilities and practical limitations of OFDM pilot-based sensing, supporting resource-efficient localization in future ISAC systems.

</details>

## Audio and speech

### [PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions](https://arxiv.org/abs/2611.27601)
*Sulong Yang, Zhi Zeng, Xiupeng Wu et al.* · `cs.SD` · arXiv:2611.27601v1 · relevance 0.11

- **In one sentence**: PromptTTSD is an open-source model for generating multi-speaker conversational speech from dialogue scripts with open-ended natural-language style control, trained on a new dataset (PromptDialog) extracted from multi-narrator audiobooks.
- **In plain words**: Current systems that turn written dialogue into spoken conversation struggle to make each line sound right for its moment, such as shifting tone as a conversation changes. This paper builds a large set of conversational speech from audiobooks, with style descriptions written in ordinary language and pulled from the story text by a language model. The authors then train a model, PromptTTSD, that accepts both the script and a plain-language style description.
- **Why it matters**: The work targets a real gap: most prior datasets only label style with fixed tags, which limits how expressive the output can be. The text reports that the model keeps strong basic speech quality, competes with proprietary systems on style control, and improves how well lines fit the surrounding conversation; the evaluation details are not given in the summary, so the size of these gains is unclear.
- **Background needed**: - Text-to-speech (TTS): software that turns written text into spoken audio.
- Spoken dialogue synthesis: generating a multi-turn conversation with several voices, not just one reading.
- Zero-shot voice cloning: copying a voice from a short sample without extra training for that voice.
- Prompt-based control: steering the speaking style by giving a text description (e.g., "calm, slightly sad") instead of choosing from preset labels.
- Audiobook alignment: matching audio recordings to their text so that individual spoken lines can be cut out and labeled.
- Large language model (LLM): an AI text model used here to write style descriptions from story passages.
- Proprietary vs. open-source: the comparison models are closed commercial systems; this model's code and weights are publicly released. · level: research-level

<details><summary>Original abstract</summary>

Spoken dialogue synthesis aims to generate multi-turn conversational speech from dialogue scripts while maintaining speaker consistency and contextual appropriateness. However, existing models largely lack fine-grained controllability, which is critical for capturing the dynamic, context-dependent style shifts in natural conversations. While prompt-based TTS has enabled such control for single-speaker speech, existing datasets heavily rely on predefined tags, which fundamentally limits their capacity to capture open-ended styles. To address this gap, we propose a scalable pipeline for extracting conversational speech from multi-narrator audiobooks, featuring an improved two-stage alignment algorithm to preserve dialogue continuity, paired with LLM-based extraction of style descriptions directly from narrative text. We release PromptDialog, a large-scale multi-speaker conversational speech dataset comprising 8,383 hours of Chinese speech and 120 hours of English speech, with open-ended style descriptions for 79% of utterances. We further introduce PromptTTSD, a spoken dialogue synthesis model built via a prompt-aware fine-tuning strategy that integrates style prompts into text-speech interleaved sequences. PromptTTSD is an open-source spoken dialogue synthesis model that supports both zero-shot voice cloning and natural language style control. Experiments demonstrate that PromptTTSD not only maintains strong fundamental synthesis capabilities but also achieves competitive open-ended style control compared with proprietary models, and substantially improves contextual appropriateness in multi-turn dialogues.

</details>

### [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784)
*Sivashankar Selvarajan, Piyush Verma, Sumit Kumar et al.* · `cs.SD` · arXiv:2611.27784v1 · relevance 0.09

- **In one sentence**: A company report presents ARCAS 290M, a frozen foundation model for detecting AI-generated speech that is claimed to generalize across generators, channels, and languages without benchmark-specific fine-tuning, evaluated on ten public benchmarks and commercial leaderboards.
- **In plain words**: Cheap voice-cloning tools can now copy someone's voice from a few seconds of audio, which makes scam calls and fake recordings harder to spot. This work describes a single detector model, ARCAS 290M, built by a company called Neural Defend, that is meant to tell real speech from AI-generated speech across many kinds of fakes, phone lines, and languages. The authors report strong results on several public test sets and leaderboards, though these are self-reported claims in a summary.
- **Why it matters**: Reliable detection of synthetic voices matters for fraud prevention, platform safety, and verifying media. The text, however, is a promotional-style summary without the detailed methods, error rates, or independent verification needed to judge how strong the claims are.
- **Background needed**: - Voice cloning / text-to-speech (TTS): software that generates speech in a chosen voice from text.
- Voice conversion: changing one speaker's voice to sound like another.
- Deepfake audio detection: classifiers that label a recording as real or AI-generated.
- Foundation model: a large general-purpose model trained once and reused for many tasks.
- Zero-shot / fine-tuning: testing on data the model was not specifically tuned for, versus adapting it to a benchmark.
- Equal error rate (EER): a standard score where lower means the detector confuses real and fake less often.
- Benchmarks and leaderboards (e.g., ASVspoof5, SpeechFake): shared test datasets and public rankings used to compare systems.
- Codec language model: a speech generator that works on compressed audio tokens.
- Channel effects: distortion from telephone or Bluetooth transmission that can confuse detectors. · level: research-level

<details><summary>Original abstract</summary>

Voice cloning now needs only seconds of audio, and detectors tuned to one dataset often fail when the generator, channel, or language changes. We introduce ARCAS 290M, Neural Defend's foundation model for detecting AI-generated audio. A single frozen production model, with no benchmark-specific fine-tuning, generalizes across text-to-speech, voice-conversion, and codec-language-model generators, telephone and Bluetooth channels, recording conditions, and languages. We evaluate it on the complete official test sets of ten public benchmarks, scoring every recording exactly as released, and against commercial systems on independent leaderboards. ARCAS 290M ranks first among all systems on the Podonos leaderboard and has the lowest equal error rate among commercial detectors on ASVspoof5. It separates real from AI-generated speech almost perfectly on ASVspoof5, SpeechFake, and ShiftySpeech, and detects nearly all AI-generated speech in Hindi, Tamil, Bengali, and Telugu. On every benchmark with a published zero-shot comparison, including in-the-wild audio, partial fakes, and the conditions hardest for the field, it surpasses the strongest reported detector by a wide margin. These results establish ARCAS 290M as a general-purpose foundation for AI-generated audio detection in fraud prevention, platform safety, and media verification.

</details>

## Control systems

### [Learned Network Dynamics for Model Predictive Traffic Signal Control under Incidents](https://arxiv.org/abs/2611.27435)
*Dang Viet Anh Nguyen, Carlos Lima Azevedo, Tomer Toledo et al.* · `cs.LG` · arXiv:2611.27435v1 · relevance 0.17

- **In one sentence**: GNN-MPC is a receding-horizon traffic-signal controller that plans with action-conditioned graph-neural-network dynamics, coordinates phases across intersections via approximate best responses with an acceptance test, and is evaluated in microscopic simulation under non-recurrent incidents on a homogeneous grid and a heterogeneous 21-intersection network.
- **In plain words**: Cities use traffic lights to manage queues, and a crash or lane closure can make those queues behave in ways that are hard to predict. This paper proposes a controller that uses a learned model of how the whole road network responds to each light decision, rather than a hand-calibrated model. In computer traffic simulations with incidents, it reduced travel time and completed more trips than the controllers it was compared with.
- **Why it matters**: Traffic signals that adapt to incidents could reduce delays, and the paper's comparison suggests that both seeing queues that extend beyond short lanes and predicting how queues respond to control matter. The results come from simulation only, so it is unclear how they would transfer to real streets; the text does not address deployment.
- **Background needed**: - Model predictive control (MPC): at each time step, the controller simulates several future steps under a model, picks the best action sequence, applies only the first action, then repeats.
- Graph neural network (GNN): a neural network that operates on a graph of nodes (here, intersections and lanes) and passes information between connected nodes.
- Action-conditioned dynamics: a model that predicts how the system will evolve given the control action being considered.
- Store-and-forward model: a simple queueing model where vehicles are held at a link and released downstream, used here as a baseline predictor.
- MaxPressure: a known traffic-signal heuristic that favors phases that relieve the most congested movements.
- Non-recurrent incident: an unexpected, temporary disruption such as a crash or closure.
- Microscopic simulation: software that models each vehicle individually. · level: research-level

<details><summary>Original abstract</summary>

Model predictive control (MPC) of urban traffic signals relies on a model of how queues respond to signal decisions, which is hard to specify and calibrate in heterogeneous networks, particularly when incidents change capacities and turning shares. Measurements add a second limitation: the controlled lanes at the stop line are often short, so queues extending upstream of them fall outside lane-level measurements. We propose GNN-MPC, a receding-horizon controller that plans with action-conditioned network dynamics learned by graph neural networks. Phase sequences are coordinated across intersections by approximate best responses, with an acceptance test that keeps the predicted cost no higher than that of the initial plan. In microscopic simulation under non-recurrent incidents, GNN-MPC reduces travel time and increases completed trips relative to all tested controllers, on a homogeneous grid and a heterogeneous 21-intersection network. Controlled comparisons on the heterogeneous network distinguish the roles of observation and prediction. With nearly as many vehicles entering the network, GNN-MPC reduces travel time by 13% relative to MaxPressure with the same upstream measurement, and GNN-MPC without the upstream representation does not reproduce its performance. Under the same traffic measurements, planner and objective, replacing the learned dynamics with calibrated store-and-forward predictors increases travel time by 31-34%. Observing hidden demand and predicting its response to control are thus complementary requirements of network-level predictive control.

</details>

### [Nonholonomic Event-Triggered Source Seeking](https://arxiv.org/abs/2611.26802)
*Victor Hugo Pereira Rodrigues, Tiago Roux Oliveira, Miroslav Krstic* · `math.OC` · arXiv:2611.26802v1 · relevance 0.10

- **In one sentence**: An event-triggered source-seeking controller for nonholonomic unicycle vehicles that separates continuous probing motion from aperiodically updated correction, with practical exponential convergence proved via a time-periodic Lyapunov function and a positive minimum dwell time.
- **In plain words**: This paper looks at how a robot vehicle can find the strongest point of a signal, such as the peak of a field, without constantly recalculating its steering. The vehicle keeps wiggling in a steady probing pattern to sense which way the signal rises, but it only updates its course correction when a trigger condition is met. The authors show, using mathematical proof, that the vehicle still gets close to the source and that updates never happen so rapidly that they pile up.
- **Why it matters**: Reducing how often a vehicle must compute and send control updates can save computing and communication resources, which matters for battery-powered or networked machines. The text does not report experiments or hardware results, so its practical payoff is not yet shown.
- **Background needed**: - Source seeking: steering a vehicle toward a hidden maximum (or minimum) of an unknown signal, using only measurements.
- Nonholonomic unicycle: a wheeled vehicle that cannot move sideways directly and must steer by turning and moving forward.
- Event-triggered control: updating the control only when a measured error crosses a threshold, instead of at fixed time steps.
- Dither/probing signals: small periodic wiggles that let the vehicle estimate the local slope of the signal.
- Washout, demodulation and low-pass filtering: standard signal-processing steps that extract the slope estimate from the wiggles.
- Lyapunov function: a energy-like certificate used to prove a system settles toward a target.
- Zeno behavior: an unphysical case where triggered updates pile up infinitely fast; the paper proves a positive minimum gap between updates to rule this out.
- Lie-bracket / averaging analysis: mathematical tools that approximate the fast wiggling motion by its average effect. · level: research-level

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
| AI industry news | 34 | 29 | 5 |
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
| Psychiatry and neurology | 25 | 21 | 2 |
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
