# Research digest · 2026-11-27
<!-- {% raw %} -->

New papers posted from about 2026-11-26 to 2026-11-27 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Viscosity solutions for integro-differential equations with gradient and source terms](https://arxiv.org/abs/2611.34533)** (Partial differential equations): This paper is about a family of equations that describe how a quantity changes when it depends both on nearby values and on far-away values, as in models with jumps or long-range effects. The authors show that these equations have a well-defined solution, and that two solutions cannot differ in the wrong way (a comparison principle). Their approach tries to bring together two older styles of argument into one framework.
- **[List coloring degenerate graphs with requests](https://arxiv.org/abs/2611.34348)** (Combinatorics): The paper studies a graph-coloring problem: each vertex gets a short menu of allowed colors, and some vertices request a specific color from their menu, and the question is how many of those requests can be honored at once. The authors prove three results about graphs that are "d-degenerate" (they can be built up or stripped down one vertex at a time, each vertex touching at most d others at that stage). The results concern the extreme settings where the menus are as small as possible and the fraction of satisfiable requests is as large as possible.
- **[Adaptive Control Barrier Functions for Nonlinear Singularly Perturbed Systems](https://arxiv.org/abs/2611.34866)** (Control systems): Many machines have parts that move at very different speeds, and a controller must keep the whole system inside safe limits even when some of its physical parameters are not known exactly. This paper develops a method that does this for such two-speed systems by estimating the unknown parameters online. The authors report that if the slow part is kept safe with a suitable margin, the slow part stays close to its safe region when the speed-ratio parameter is small, and they give conditions for joint safety of the slow and fast parts.

## Probability

### [Differentiability of the shape function in the planar corner growth model](https://arxiv.org/abs/2611.33433)
*Christopher Janjigian, Firas Rassoul-Agha, Timo Sepp\"al\"ainen* · `math.PR` · arXiv:2611.33433v1 · relevance 0.18

- **In one sentence**: The paper proves that the time-constant (shape) function of planar directed last-passage percolation with general i.i.d. real weights is differentiable on the open first quadrant, under moment conditions on the weights, and gives a Lean-formalized proof adapted from an AI-assisted first-passage percolation argument.
- **In plain words**: The paper studies a random growth model where paths collect random weights and the maximum total weight from a corner grows in a predictable way. It shows that the function describing this growth speed, as the direction changes, is smooth (differentiable) in the open first quadrant, provided the weights have enough finite moments. The proof is also written and checked in the Lean proof assistant, and it was adapted from an AI-assisted proof for a related model.
- **Why it matters**: Whether the shape function is differentiable is a long-standing question in this area, so a result settling it in a broad setting is of interest to specialists in growth models. The text does not say how it connects to wider applications, and the use of an AI-assisted, machine-checked proof is noted as a feature of the work.
- **Background needed**: - Last-passage percolation: a random growth model where you find the path from a corner to a far point that collects the largest total of random weights placed on sites.
- i.i.d. weights: each site's weight is drawn independently from the same distribution.
- Shape function: the limiting growth rate in each direction, which describes the typical size of the maximum-weight path as a function of direction.
- Differentiable: smooth, meaning the shape function has a well-defined slope at each point of the open quadrant.
- Moment assumption: a condition that the weights' tails are not too heavy, measured by finite moments of a given order.
- Percolation cone: a set of directions already handled by known results, so only directions outside it need proof.
- Van den Berg–Kesten inequality: a probability bound on the chance of two events occurring disjointly.
- Lean: a computer proof assistant used to check that a proof is fully correct. · level: research-level

<details><summary>Original abstract</summary>

We prove that the shape function of planar directed last-passage percolation with general i.i.d.\ real-valued weights is differentiable on the open first quadrant, under a moment assumption of order $p''>4$ on the positive part of the weight and a nearly optimal order $p'>1$ on the negative part. Due to known results, only directions outside a percolation cone need be considered. The proof is a multiscale path-counting argument that uses the shape theorem, oriented percolation on a coarse-grained lattice, a simple change of measure in a finite region, and the van den Berg--Kesten inequality. Our Lean-formalized proof is an AI-assisted adaptation and improvement of the OpenAI proof of differentiability in planar first-passage percolation.

</details>

### [Besicovitch Pseudo Almost Periodic Stochastic Processes and Their Applications to Delayed Stochastic Neural Networks](https://arxiv.org/abs/2611.33209)
*Yongkun Li, Yuwei Cao, Bing Li* · `math.DS` · arXiv:2611.33209v1 · relevance 0.14

- **In one sentence**: The paper defines Besicovitch pseudo almost periodic stochastic processes and uses them to study solutions in distribution and their p-th mean stability for delayed stochastic neural networks whose parameters, apart from the time delays, are pseudo almost periodic.
- **In plain words**: The paper is about systems whose random behaviour repeats in a loose, approximate rhythm, the way a noisy seasonal signal might. It introduces a formal definition for such random processes under a weaker notion of repetition (the Besicovitch sense), then applies it to a model of neural networks that have time delays and random noise. The authors state that they establish existence of such solutions and stability criteria for them.
- **Why it matters**: The work extends a mathematical framework for describing oscillating behaviour in randomly driven systems, which may matter for modelling neural networks and similar stochastic dynamical systems. The text does not show applications beyond this theoretical setting, so its practical reach is unclear.
- **Background needed**: - Almost periodic function: a function that is not exactly periodic but returns arbitrarily close to its earlier patterns at regular-ish intervals.
- Pseudo almost periodic: almost periodic apart from a small part that decays over time.
- Besicovitch sense: a way of measuring closeness on average over long stretches, which is looser than requiring closeness at every moment.
- Stochastic process: a quantity that evolves randomly over time.
- Solution in distribution: describes the statistical behaviour of a random solution rather than one exact path.
- Delayed neural network: a network model in which signals take time to pass between units.
- p-th mean stability: stability measured through the average of the p-th power of the deviation, which is a standard way to measure random errors. · level: research-level

<details><summary>Original abstract</summary>

The Besicovitch almost periodic concept is a generalization of the Bohr, Stepanov, and Weyl almost periodic concepts and, in a certain sense, has broader coverage and weaker conditions. However, the concept of pseudo almost periodic stochastic processes in the Besicovitch sense has not yet been systematically proposed, which limits the characterization of the complex oscillatory behavior of a broader class of stochastic non-autonomous systems. This paper proposes the concept of Besicovitch pseudo almost periodic stochastic processes. As an application of this concept, we study the existence of Besicovitch pseudo almost periodic solutions in distribution for a class of stochastic delayed neural networks in which all parameters except the time delays are pseudo almost periodic and establish stability criteria for such solutions in the $p$-th mean sense. The work of this paper fills the gap caused by the lack of the concept of Besicovitch pseudo almost periodic stochastic processes and provides a new conceptual tool and analytical approach for characterizing the complex oscillatory behavior of stochastic differential equations and stochastic neural network systems.

</details>

## Differential geometry

### [Three-dimensional harmonic critical metrics for the Einstein-Hilbert functional and self-similar Ricci flows](https://arxiv.org/abs/2611.34037)
*Sergey E. Stepanov, Irina I. Tsyganok* · `math.DG` · arXiv:2611.34037v1 · relevance 0.23

- **In one sentence**: In three dimensions, the paper shows that compact harmonic critical metrics for the Einstein-Hilbert functional under volume-preserving Chen-Nagano variations are exactly the constant-sectional-curvature (space-form) metrics, and relates this rigidity to self-similar Ricci flows and the smooth Poincaré theorem.
- **In plain words**: This paper studies a question about how the shape of a curved three-dimensional space can be "locally balanced" under a certain family of small changes to its geometry. The authors show that, on closed three-dimensional spaces, the only such balanced shapes are the very symmetric ones where curvature is the same in every direction. They also describe some related mathematical structure, including explicit self-similar flows that evolve the shape in a predictable way.
- **Why it matters**: The result gives a rigidity statement: a variational condition forces the strongest symmetry, which links a question about optimizing geometry to Ricci flow and to the Poincaré theorem about three-dimensional spaces. The text itself does not say how far these connections will extend, so their broader significance is uncertain from this abstract alone.
- **Background needed**: - Metric: a rule for measuring distances on a surface or space; it defines its curvature.
- Sectional curvature: how much a space bends in a given two-dimensional slice; constant sectional curvature means it bends the same everywhere, like a sphere or flat space.
- Einstein-Hilbert functional: a quantity computed from a metric that, in the classical setting, is the central object of Einstein's gravity theory and Hilbert's variational problem.
- Harmonic / critical metric: a metric at which the functional does not change to first order under allowed small deformations.
- Chen-Nagano variations: a specific family of allowed deformations used here; volume-preserving means total volume is held fixed.
- Ricci flow: a process that smoothly evolves a metric over time, shrinking or reshaping curvature; self-similar flows change only by scaling and diffeomorphisms.
- Gradient Ricci soliton: a special self-similar solution of Ricci flow.
- Ivey's classification: a known classification of certain three-dimensional geometries used as a tool here.
- Poincaré theorem: the statement that every closed three-dimensional space with trivial topology is a sphere, proved by Perelman.
- Gauge / diffeomorphism: a relabeling of points that changes coordinates but not the underlying geometry. · level: research-level

<details><summary>Original abstract</summary>

We address the three-dimensional harmonic analogue of Hilbert's variational problem: does criticality of the Einstein-Hilbert functional under volume-preserving Chen-Nagano variations force constant sectional curvature, and how is this rigidity related to Ricci flow and topology? Starting from the known characterization of compact harmonic critical metrics as gradient Ricci solitons, we use Ivey's classification to show that such metrics on closed three manifolds are precisely the space-form metrics, equivalently the stationary metrics of the volume-normalized Ricci flow. We also describe residual gauge one-forms, establish transversality of the Chen-Nagano gauge to infinitesimal diffeomorphism directions, and give explicit self-similar flows. The normalized Ricci-flow velocity is an admissible Chen-Nagano variation for n > = 3, and the smooth Poincar'e theorem admits an equivalent formulation in terms of the existence of harmonic critical metrics

</details>

### [Left-Invariant Kundt Structures on Almost Abelian Lie Groups](https://arxiv.org/abs/2611.34738)
*S. El Bourkadi, M. W. Mansouri* · `math.DG` · arXiv:2611.34738v1 · relevance 0.22

- **In one sentence**: The paper classifies left-invariant Kundt structures on almost abelian Lie groups, giving algebraic existence criteria, admissible real Jordan forms by signature of the abelian ideal, and characterizing Kundt pairs that define pp-waves and plane waves in arbitrary dimension.
- **In plain words**: The paper studies a special family of curved spaces with a lot of built-in symmetry, and special "null" directions in them that behave like light rays. The authors work out when such structures can exist, which algebraic patterns are possible, and how to recognize the wave-like cases called pp-waves and plane waves in any number of dimensions. They also give four-dimensional examples showing both plane and non-plane versions.
- **Why it matters**: Pp-waves and plane waves are model solutions in general relativity and related geometry, so a clear classification helps identify which such models exist within a symmetric class. The text does not state specific applications, so the connection to physics is suggested by the subject matter rather than claimed by the paper.
- **Background needed**: - Lie group: a smooth space that is also a group, whose symmetries act the same way at every point (left-invariant means defined using only this group action).
- Almost abelian Lie group: a group with a codimension-one abelian ideal, so it is nearly commutative.
- Kundt structure: a geometry with a special null (light-like) direction that is non-expanding and shear-free, studied in Lorentzian geometry.
- pp-wave and plane wave: special Lorentzian spacetimes with parallel or nearly parallel null directions, used as model solutions in general relativity.
- Jordan form: a standard matrix normal form used to classify linear maps up to change of basis.
- Signature: the count of positive and negative directions in a metric. · level: research-level

<details><summary>Original abstract</summary>

We study left-invariant Kundt structures on almost abelian Lie groups. We establish algebraic existence criteria and characterize the admissible real Jordan forms according to the signature of the Abelian ideal. We then characterize the Kundt pairs defining pp-waves and plane waves in arbitrary dimension, with particular attention to recurrent and parallel null directions. Examples in dimension four illustrate both plane and non-plane pp-wave geometries.

</details>

## Partial differential equations

### [Viscosity solutions for integro-differential equations with gradient and source terms](https://arxiv.org/abs/2611.34533)
*Russell Schwab, Son N. T. Tu, Olga Turanova* · `math.AP` · arXiv:2611.34533v1 · relevance 0.21

- **In one sentence**: The paper proves comparison principles and existence (via Perron's method) for viscosity solutions of integro-differential equations with gradient and source terms, using a "global comparison property" together with a local Lipschitz assumption on the operator.
- **In plain words**: This paper is about a family of equations that describe how a quantity changes when it depends both on nearby values and on far-away values, as in models with jumps or long-range effects. The authors show that these equations have a well-defined solution, and that two solutions cannot differ in the wrong way (a comparison principle). Their approach tries to bring together two older styles of argument into one framework.
- **Why it matters**: The text presents this as an attempt to unify earlier results and to improve on some recent examples, so its value lies mainly in the technical framework rather than in any single new application. It is most relevant to researchers working on nonlocal or free-boundary problems; the text does not say what concrete applications it connects to.
- **Background needed**: - Partial differential equation (PDE): an equation relating a function to its rates of change in space.
- Integro-differential equation: an equation that also involves an integral, so the value at a point depends on values elsewhere (nonlocal effects).
- Gradient term: a term involving the slope or rate of change of the unknown function.
- Viscosity solution: a weak notion of solution that allows equations without smooth solutions to still be handled rigorously.
- Comparison principle: if one function is a supersolution and another a subsolution, the first stays above the second; this implies uniqueness.
- Perron's method: a way to construct a solution as the supremum of subsolutions.
- Min-max structure and free boundary problems: ways of writing an operator as a minimum/maximum, and problems where the boundary between regions is unknown in advance. · level: research-level

<details><summary>Original abstract</summary>

We address global well-posedness for integro-differential equations with gradient and source terms. This naturally results from establishing the comparison principle for viscosity solutions and existence via Perron's method. There are many earlier results for similar equations, and our work attempts to give a unified approach and improve upon some recent examples. There is a natural juxtaposition of earlier results in the usual framework of viscosity solutions which rely on a min-max structure, with some more recent implementations coming from the free boundary literature in which a min-max is not apparent initially, but does appear a posteriori due to certain rigid structural constraints. Here we give a presentation that combines ideas from both situations. The most important feature of the operators in our equations is what we call the global comparison property. This is combined with a natural local Lipschitz assumption on the operator defining the equation.

</details>

### [The confined discrete DLSS equation: gradient flow structure and long-time asymptotics](https://arxiv.org/abs/2611.34197)
*Daniel Matthes, Andr\'e Schlichting* · `math.AP` · arXiv:2611.34197v1 · relevance 0.17

- **In one sentence**: A structure-preserving finite-difference-style discretization of the fourth-order DLSS equation in rescaled variables with linear confinement on the real line, shown to be a discrete gradient flow of relative entropy with exponential decay to a discrete Gaussian via a discrete modified log-Sobolev inequality.
- **In plain words**: The paper studies a numerical version of a fourth-order equation that describes how a spread-out quantity (a density) evolves over time, here with a confining force that keeps it from spreading indefinitely. The authors build a discrete version of the equation that keeps its key mathematical structure, and show that solutions stay positive and settle toward a Gaussian (bell-shaped) equilibrium at an exponential rate. They also report numerical experiments that agree with their analysis.
- **Why it matters**: Preserving the underlying structure of an equation when discretizing it means the computer model inherits its long-term behaviour, which is useful for trusting simulations. The work extends the authors' earlier unconfined version, and the stated result is that the discrete decay rate matches the continuous rate as the grid is refined; the text does not say what applications it may feed into.
- **Background needed**: - Partial differential equation (PDE): an equation relating a function to its rates of change in space and time.
- Fourth-order equation: involves up to fourth spatial derivatives, making it harder to analyse than heat-type equations.
- Discretization: replacing a continuous problem with a grid-based version that a computer can solve.
- Gradient flow: evolution that steadily decreases a given "energy" (here, relative entropy), measuring distance from equilibrium.
- Relative entropy: a measure of how far a distribution is from a reference distribution.
- Gaussian equilibrium: the bell-shaped distribution the solution converges to over time.
- Log-Sobolev inequality: a functional inequality used to prove that such decay happens at a guaranteed exponential rate.
- Mesh size: the spacing of the grid; the limit of small mesh size recovers the continuous equation. · level: research-level

<details><summary>Original abstract</summary>

We propose and analyse a structure-preserving discretization of the fourth-order DLSS equation in dynamically rescaled variables leading to a linear confinement on the one-dimensional real line. The scheme is obtained as a discrete analogue of the Carrillo--Toscani splitting. It allows for a new interpretation of the DLSS equation as gradient flow of the relative entropy with respect to a combined diffusive and transport metric, extending the structure of the discretization introduced in our earlier work with Giuseppe Savar\'{e} for the unconfined equation. We prove global existence of positive solutions and, as the main analytical result, exponential decay of the relative entropy towards the discrete Gaussian equilibrium. The decay rate is obtained via a discrete modified logarithmic Sobolev inequality. The resulting rate is consistent with the continuum rate and converges to it from below in the vanishing mesh-size limit. Numerical results illustrate and confirm our findings.

</details>

## Harmonic analysis

### [Separable models of an NIP Banach space theory](https://arxiv.org/abs/2611.33260)
*Karim Khanaki, Pedro Poitevin* · `math.LO` · arXiv:2611.33260v1 · relevance 0.10

- **In one sentence**: The paper shows that a specific renorming of a Hilbert-type Banach space has an NIP (non-independence-property) unstable theory in the pure Banach language, classifies its continuum-many separable models up to surjective linear isometry by an order type and a Hilbert dimension, and describes their elementary embeddings and separability of bounded norm types.
- **In plain words**: This paper studies a mathematical structure: a particular infinite-dimensional normed space, built from a standard Hilbert space with a specially designed norm. The authors examine the logical theory describing this space and show it is "tame" in a technical sense (NIP), then sort its small pieces (separable models) into families. The sorting is done by two simple invariants: the shape of a countable ordering and the dimension of one Hilbert component, and the text says every combination of these occurs.
- **Why it matters**: The text claims a complete classification of many separable models up to isometry, which is a precise and fairly rare kind of result in model theory of Banach spaces. It may connect model theory with functional analysis, since the norm itself encodes the index ordering; the broader significance beyond this example is not established in the text.
- **Background needed**: - Banach space: a complete normed vector space, i.e. a space of vectors with a notion of length that supports limits.
- Hilbert space and ℓ2: a Banach space whose norm comes from an inner product (like ordinary Euclidean length, extended to infinitely many coordinates).
- Renorming: giving the same space a different but equivalent-in-structure norm.
- Model theory / first-order theory: the study of which statements hold in a structure, here written in the "pure Banach language" (only linear and norm vocabulary).
- NIP (non-independence property): a tameness condition from model theory meaning definable families are not too complicated.
- Separable model: a model with a countable dense subset.
- Surjective linear isometry: a bijective linear map preserving norms, i.e. a structure-preserving identification.
- Elementary embedding: a map preserving all first-order truths.
- Order type of (N,<) models and (Q,<): ways countable linear orders can be shaped; (Q,<) is the rationals in their usual order. · level: research-level

<details><summary>Original abstract</summary>

Let $Y$ be the renorming of $\ell_2(\mathbb N)\oplus_2\ell_2(\mathbb N)$ with norm $(h^2+q^2)^{1/2}$, where $h$ is the Hilbert norm and $q(u,v)=\sup_{i<j}|u_i+v_j|$. We prove that the unstable theory $\operatorname{Th}(Y)$ is NIP in the pure Banach language. We recover the index order from the Banach norm and classify the continuum many separable models up to surjective linear isometry. The invariants are the order type of a countable model of $\operatorname{Th}(\mathbb N,<)$ and the dimension of a separable Hilbert summand. Every such pair occurs. We describe all elementary embeddings between these models. The bounded norm types over a separable model are separable in the uniform metric exactly when its index order contains no copy of $(\mathbb Q,<)$.

</details>

### [Pietsch's favourite problem on singular traces](https://arxiv.org/abs/2611.34559)
*Gustavo Ara\'ujo, Daniel Pellegrino, Joedson Santos* · `math.FA` · arXiv:2611.34559v1 · relevance 0.10

- **In one sentence**: The paper answers Pietsch's Problem 16 affirmatively by constructing a nonzero bounded singular spectral trace on the weak Weyl ideal over the class of all Banach spaces.
- **In plain words**: Mathematicians study "traces," which are rules that assign a single number to certain large collections of linear operators (maps between infinite-dimensional spaces) in a consistent way. In 2023 Albrecht Pietsch posed a list of 27 open questions about these traces, and this paper resolves the one he considered his favourite. The authors show that such a trace exists on a specific collection of operators, the weak Weyl ideal, when the setting is extended to all Banach spaces.
- **Why it matters**: The result settles a question posed by a leading figure in the field, so it matters to specialists in operator ideals and trace theory. The summary text does not say what wider applications it has, so any further connections are unclear.
- **Background needed**: - Banach space: a complete normed vector space, the basic infinite-dimensional setting for this work.
- Bounded linear operator: a structure-preserving map between Banach spaces that does not blow up lengths too much.
- Operator ideal: a collection of operators closed under natural operations, such as composition with other operators.
- Trace: a function that assigns a number to operators in an ideal, behaving like the matrix trace (sum of diagonal entries) in finite dimensions.
- Singular trace: a trace that vanishes on finite-rank operators, and so is not the ordinary trace; these are notoriously hard to construct in general.
- Weak Weyl ideal: a specific operator ideal defined via Weyl numbers, a sequence of approximation-size measures for operators.
- Pietsch's problem list: 27 open questions on traces on operator ideals posed by Albrecht Pietsch in 2023. · level: research-level

<details><summary>Original abstract</summary>

In 2023, A. Pietsch formulated twenty-seven open problems concerning traces on operator ideals. We give an affirmative answer to Problem 16, which Pietsch singled out as his personal favourite, by constructing a nonzero bounded singular spectral trace on the weak Weyl ideal over the class of all Banach spaces.

</details>

## Complex analysis

### [Independence of Thurston eigenvalues and Lyapunov exponents for quadratic rational maps](https://arxiv.org/abs/2611.34186)
*Ayesha Bennett, Holly Krieger* · `math.DS` · arXiv:2611.34186v1 · relevance 0.08

- **In one sentence**: The paper studies post-critically finite quadratic rational maps with both critical points in one cycle, constructing real bitransitive centres in the curve C_2 that degenerate in moduli space, and shows Thurston eigenvalues have a spectral gap on compact subsets of C_2.
- **In plain words**: The paper looks at a family of simple iterated maps of the Riemann sphere, the kind of rule you get by repeatedly applying a fraction-shaped function to complex numbers. It concerns maps whose special "critical" points behave in a tightly linked way, and it asks how two different numerical measures of how these maps stretch things, called Thurston eigenvalues and Lyapunov exponents, relate to each other. The authors build a sequence of such maps where the Lyapunov exponents grow without bound while the Thurston eigenvalues stay in a fixed range, and they show the Thurston eigenvalues stay separated from the unit circle in a uniform way on compact parts of the curve.
- **Why it matters**: The work responds to questions raised by Buff, Epstein and Koch about whether these two quantities are independent, and the example suggests they are not tied together in the way one might hope. The text does not say more about wider applications, so the broader significance is uncertain from this abstract alone.
- **Background needed**: - Complex numbers and the Riemann sphere (the complex plane plus a point at infinity).
- Rational maps: functions given as a ratio of polynomials, iterated repeatedly.
- Quadratic rational maps: maps of degree two.
- Critical points: points where the map's derivative vanishes; post-critically finite means their orbits under iteration are finite in number (eventually periodic).
- Moduli space: the space parametrising maps up to change of coordinates; "degenerate" means a sequence of maps escapes to a boundary of this space.
- Thurston pullback map and its fixed point: a combinatorial tool whose derivative's eigenvalues are the Thurston eigenvalues.
- Lyapunov exponent: a long-run average measure of how fast nearby orbits separate.
- Spectral gap: a uniform separation of the relevant eigenvalues from the unit circle. · level: research-level

<details><summary>Original abstract</summary>

We study post-critically finite quadratic rational maps $f: \mathbb{P}^1\to\mathbb{P}^1$ where the two critical points lie in the same cycle. The Thurston eigenvalues of $f$ are those of the derivative of the Thurston pullback map $\sigma_f$ at its fixed point. Addressing questions of Buff--Epstein--Koch, we construct a sequence of real, bitransitive centres in the critical orbit relation curve $C_2$ which degenerates in moduli space, and whose Lyapunov exponents tend to infinity whilst the Thurston eigenvalues satisfy $\frac{1}{10}< |\lambda|<1$. We also show the Thurston eigenvalues across all bitransitive centres in $C_2$ have a spectral gap on compact subsets of the curve.

</details>

### [Connectedness Principle in the Complex Analytic Setting](https://arxiv.org/abs/2611.34654)
*Swapnajit Das* · `math.AG` · arXiv:2611.34654v1 · relevance 0.08

- **In one sentence**: The paper proves a complex-analytic version of the connectedness principle for Kähler pairs: under a nefness condition over a base, the non-klt locus has at most two connected components in each fiber, and it extends the result to generalized pairs with transcendental nef part and to projective morphisms of possibly non-compact analytic varieties.
- **In plain words**: The paper studies shapes of special subsets inside geometric spaces that are built from curves, surfaces and their higher-dimensional analogues, such as complex manifolds. It asks how many separate pieces the "bad" part of such a space can break into when the space is mapped onto a simpler base. The authors show that, under the stated conditions, each fiber of the map has at most two separate pieces.
- **Why it matters**: This is a complex-analytic extension of a connectedness principle that is known in algebraic geometry, so it brings those tools to the non-algebraic (Kähler) setting. The text does not say what applications it has beyond this extension, so its wider significance is unclear from the given material.
- **Background needed**: - Complex analytic variety: a space locally described by complex-number equations, more flexible than algebraic varieties.
- Kähler: a geometric compatibility condition on a complex space that allows tools from differential geometry.
- Normal pair (X, B): a space X with a weighting divisor B on it, used to track singularities.
- Non-klt locus (Nklt): the set of points where the singularities are severe enough to count as "bad".
- Proper morphism with connected fibers: a map whose preimages of points are single pieces and which does not blow up to infinity.
- Nef (over Z): a positivity condition on the canonical-type divisor, relative to the base Z.
- Generalized pair: an extended framework where an extra nef-type part is allowed; here that part may be transcendental (not coming from algebraic data).
- Fiber: the preimage f^{-1}(z) of a point z in the base. · level: research-level

<details><summary>Original abstract</summary>

We show that if $(X,B)$ is a normal compact K\"ahler pair and $f:X\to Z$ is a proper morphism with connected fibers to a normal compact K\"ahler variety $Z$ such that $(-K_X+B)$ is nef over $Z$, then $\mathrm{Nklt}(X,B)\cap f^{-1}(z)$ has at most two connected components for every $z\in Z$. More generally, we prove the result for generalized pairs whose nef part is allowed to be transcendental. Moreover, we record that the same result holds for projective morphism between analytic varieties (possibly non-compact).

</details>

## Operator algebras and spectral theory

### [Co-amenability and local reflexivity of $C^*$-algebras](https://arxiv.org/abs/2611.33578)
*Yafei Zhao, Zhe Dong* · `math.OA` · arXiv:2611.33578v1 · relevance 0.14

- **In one sentence**: The paper shows that local reflexivity passes from a unital C*-subalgebra A to a larger algebra B when the bidual inclusion A** ⊂ B** is co-amenable, and derives several preservation results and answers to Kirchberg's 2011 questions.
- **In plain words**: This is about a property of infinite-dimensional algebras of operators, which are the mathematical objects used to describe quantum systems. Local reflexivity is a condition saying that finite pieces of such an algebra can be approximated in a controlled way by simpler, matrix-like pieces. The paper proves that this property survives several standard ways of building new algebras from old ones, and it answers five of the open questions Kirchberg listed in 2011.
- **Why it matters**: Kirchberg's list is a guide to open problems in this area, so settling five of its questions clarifies which constructions preserve this property. The text does not say how the results bear on other fields, so any wider connection is unclear from the abstract alone.
- **Background needed**: - C*-algebra: a collection of bounded operators on a space closed under addition, multiplication, scalar multiples and taking adjoints (the "conjugate transpose").
- Bidual (A**): a much larger algebra built from A, containing A, used to study A's structure.
- Local reflexivity: a approximation property for C*-algebras, relating finite-dimensional pieces to the bidual.
- Co-amenability: a condition on the inclusion A** ⊂ B** (roughly, a way of extending structure from the smaller to the larger algebra); the text does not define it.
- Exactness, tensor products, crossed products by groups, free products, and simplicity: standard constructions for building new C*-algebras from given ones.
- Kirchberg's 2011 list: a published set of open questions about these algebras. · level: research-level

<details><summary>Original abstract</summary>

Let $A\subset B$ be a unital inclusion of $C^*$-algebras. We prove that local reflexivity passes from $A$ to $B$ if the inclusion $A^{**}\subset B^{**}$ is co-amenable. It follows that local reflexivity is preserved by minimal tensor products with exact $C^*$-algebras, by inductive limits over directed sets, and by reduced crossed products by discrete amenable groups. We also prove that reduced free products with respect to states with faithful GNS representations preserve local reflexivity and that every locally reflexive $C^*$-algebra embeds into a simple locally reflexive $C^*$-algebra. These results answer Questions~(b), (c), (d), (f) and~(h) in Kirchberg's 2011 list.

</details>

### [Duality of finite-dimensional Hopf $\mathrm{C}^*$-algebra actions via inclusions](https://arxiv.org/abs/2611.33996)
*Anshu, Hyun Ho Lee* · `math.OA` · arXiv:2611.33996v1 · relevance 0.11

- **In one sentence**: The paper studies actions of finite-dimensional Hopf C*-algebras on unital C*-algebras, defining Rokhlin property and approximate representability and proving a duality between these properties for an action and its dual action on the crossed product, under simplicity and saturation hypotheses.
- **In plain words**: This paper is about symmetry in a very abstract setting: operator algebras are collections of operations on spaces of "observables," and finite-dimensional Hopf algebras generalize groups as sources of symmetry. The authors study when such a symmetry acts on an algebra in a well-behaved way, using a "Rokhlin property" (a strong form of evenly spreading out the symmetry) and a weaker property called approximate representability. They show that, under stated conditions, one action has one of these properties exactly when the dual action on the associated crossed product has the other.
- **Why it matters**: The result gives a duality, a two-way correspondence, between an action and its dual, which extends known symmetry-and-duality results from group actions to the broader Hopf-algebra setting. The text also gives examples both with and without the Rokhlin property, and for separable algebras it links the properties to earlier spatial formulations by Barlak, Szabó and Voigt. I am not sure of wider applications beyond this area, and the text does not say.
- **Background needed**: - C*-algebra: a algebra of bounded operators closed under adjoints and norm limits, used as a mathematical model of quantum observables.
- Unital and simple: contains an identity element, and has no nontrivial two-sided ideals.
- Action: a way a symmetry structure (here a Hopf algebra) transforms the algebra.
- Hopf algebra: a generalization of a group that still carries multiplication, comultiplication and antipode; finite-dimensional ones are the case studied.
- Fixed-point algebra and conditional expectation: the subalgebra left unchanged by the action, and a projection map onto it.
- Crossed product and dual action: a bigger algebra built from the action, carrying a dual symmetry that reverses the construction.
- Rokhlin property: a condition saying the symmetry can be "spread out" so that the algebra looks like many disjoint copies, a strong form of regularity.
- Saturation and approximate representability: technical conditions on how the action sits inside the algebra. · level: research-level

<details><summary>Original abstract</summary>

We study actions of finite-dimensional Hopf $\mathrm{C}^*$-algebras on a unital $\mathrm{C}^*$-algebra $A$. We first define the Rokhlin property and approximate representability directly for an action $H\curvearrowright A$ and characterize these properties, under appropriate hypotheses, in terms of the corresponding properties of the canonical conditional expectation $E\colon A\to A^H$. Based on this characterization, we establish the following duality for a saturated action on a simple unital $\mathrm{C}^*$-algebra $A$ such that $A\rtimes H$ is simple: 1. $H\curvearrowright A$ has the Rokhlin property if and only if the dual action $H^{\circ}\curvearrowright A\rtimes H$ is approximately representable. 2. $H\curvearrowright A$ is approximately representable if and only if the dual action $H^{\circ}\curvearrowright A\rtimes H$ has the Rokhlin property. For separable $A$, we also identify these properties with the corresponding spatial formulations introduced by Barlak--Szab{\'o}--Voigt, assuming saturation in the Rokhlin comparison. We present examples of Hopf $\mathrm{C}^*$-algebra actions both with and without the Rokhlin property.

</details>

## Algebra

### [A Sweedler dual seen as a terminal object in a category of bialgebras](https://arxiv.org/abs/2611.33910)
*Lo{\"i}c Foissy (LMPA)* · `math.RA` · arXiv:2611.33910v1 · relevance 0.15

- **In one sentence**: The paper shows that the Sweedler dual of K[X] with multiplicative coproduct is the terminal object among pairs (bialgebra, character), introduces the spectrum of a bialgebra, and studies double bialgebras, near-semirings, and a graph bialgebra linked to Bergman colorings of graphical matroids.
- **In plain words**: The paper studies a specific algebraic structure built from polynomials, called the Sweedler dual, and argues it is the most general possible object of its kind: every pair consisting of a bialgebra and a character (a special kind of map to the base field) maps uniquely into it. The authors also define a "spectrum" for bialgebras and examine structures with two compatible ways of splitting elements apart. They apply the framework to a bialgebra of graphs whose operations are edge deletion and contraction.
- **Why it matters**: The universal-property result generalizes a known theorem of Aguiar, Bergeron and Sottile on combinatorial Hopf algebras, so it places a familiar result in a wider, non-graded setting. The links to matroid colorings and near-rings suggest connections to combinatorics and ring theory, though the text does not show how far these reach beyond the paper itself.
- **Background needed**: - Algebra: a vector space with a multiplication; a bialgebra also has a compatible "coproduct" that splits elements into pieces, which is a dual notion to multiplication.
- Character: a structure-preserving map from an algebra to the base field (e.g., the numbers).
- Terminal object: in category theory, a target object such that every object of the category maps to it in exactly one way.
- Sweedler dual: a standard construction that turns an algebra-coalgebra pair into a dual bialgebra.
- Graded and connected Hopf algebras: a restricted class of bialgebras with extra structure, used in combinatorics.
- Graphical matroid and Bergman coloring: combinatorial objects arising from graphs; deletion and contraction are the basic graph operations.
- Roots of unity: complex numbers whose some power equals 1. · level: research-level

<details><summary>Original abstract</summary>

We study the Sweedler dual of the polynomial algebra $\mathbb{K}[X]$ equipped with the multiplicative coproduct $\delta(X) = X \otimes X$, and show that the resulting bialgebra $\mathbb{K}[X]^\star$ is the terminal object in the category of pairs $(B, \lambda)$, where $B$ is a bialgebra and $\lambda$ is a character of $B$. This generalizes a result of Aguiar, Bergeron, and Sottile on combinatorial Hopf algebras in the graded and connected setting. We describe the subcoalgebras and subbialgebras of $\mathbb{K}[X]^\star$, which lead to the introduction of the spectrum of a bialgebra. We also study the particular cases double bialgebras (bialgebras equipped with two compatible coproducts), firstly examining their connection to unital near-semirings or near-rings. Introducing a subbialgebra of $\mathbb{K}[X]^\star$ obtained from the intersection with another Sweedler dual, we prove it is the terminal object in the category of double bialgebras. As a consequence, we show that the spectrum of any double Hopf algebra is a subgroup of the group of roots of unity. This imply that not any bialgebra can become double. We finally apply this framework to a bialgebra of graphs with a coproduct given by contraction and deletion of edges, relating its invariants to Bergman colorations of edges arising from graphical matroids.

</details>

### [On some problems regarding a group-theoretical generalization of the Gauss formula](https://arxiv.org/abs/2611.34371)
*Marius T\u{a}rn\u{a}uceanu* · `math.GR` · arXiv:2611.34371v1 · relevance 0.14

- **In one sentence**: The paper resolves three open problems, posed in an earlier work by the same authors, about the values of the function f(G) = (1/|G|) · Σ_{H≤G} |Aut(H)| (summing automorphism-group sizes over subgroups) on noncyclic finite groups.
- **In plain words**: This is a short note in abstract algebra about a number attached to each finite group, built by adding up how many symmetries each of its subgroups has and dividing by the size of the group. An earlier paper by the same authors asked three open questions about this number for groups that are not cyclic (not generated by a single element). The note says it gives complete answers to all three.
- **Why it matters**: The function is a group-theoretic analogue of the Gauss formula, which is why it is of interest to specialists in finite group theory. The provided text does not say what the answers are or what wider applications they may have, so its broader significance is unclear from this text alone.
- **Background needed**: - Finite group: a set with a finite number of elements and an associative operation with identity and inverses (e.g., symmetries of a shape).
- Subgroup: a subset of a group that is itself a group under the same operation.
- Automorphism: a structure-preserving relabelling of a group onto itself; Aut(H) is the set of these for H, and |Aut(H)| is its size.
- Cyclic group: a group generated by a single element; noncyclic means it needs more than one generator.
- Open problem: a question posed in the literature whose answer was not yet known.
- Gauss formula: a classical identity in number theory that the paper's function is modeled on by analogy (the text only mentions it by name). · level: research-level

<details><summary>Original abstract</summary>

In \cite{FT23}, we introduced the group-theoretical function $f(G) = \frac{1}{|G|}\sum_{H \le G} |\Aut(H)|$ for a finite group $G$ and posed three open problems concerning its values on noncyclic groups. In this note, we provide complete solutions to all three problems.

</details>

## Representation theory

### [Higher rewriting for strong linearly distributive coherence](https://arxiv.org/abs/2611.34596)
*Max Demirdilek, Christian Reiher, Christoph Schweigert* · `math.CT` · arXiv:2611.34596v1 · relevance 0.10

- **In one sentence**: The paper uses higher rewriting (Guiraud–Malbos style) to prove a coherence theorem for strong linearly distributive categories, showing every formal diagram commutes.
- **In plain words**: This paper is about a rule-based method for checking when two different ways of combining mathematical objects give the same result. The authors apply this method to a structure called a strong linearly distributive category, which has two kinds of "multiplication" that interact in a controlled way. They show that in such a structure, any diagram built from the allowed moves always commutes, meaning all routes between the same start and end give equal results.
- **Why it matters**: It extends Mac Lane's classical coherence theorem, a foundational result that tells you when diagrams in a monoidal category can be trusted, to a broader setting. The text does not say much beyond this, so its wider impact is uncertain from this description alone.
- **Background needed**: - Category: a collection of objects and structure-preserving maps (arrows) between them.
- Commuting diagram: a diagram where all paths between two points give the same result.
- Coherence theorem (Mac Lane): a result saying that certain diagrams built from tensor-like products always commute, so one only needs to check a few basic equations.
- Tensor product: a way of combining two objects, here with a unit (an object that does nothing when combined).
- Distributor: a map relating the two products, analogous to the distributive law a(b+c)=ab+ac, and here required to be invertible.
- Rewriting: solving word problems by repeatedly applying rules that replace one expression with an equivalent one.
- Higher categories: categories where the relations between maps are themselves treated as maps, so rewriting acts on higher-dimensional "cells". · level: research-level

<details><summary>Original abstract</summary>

Rewriting is a computational method to solve word problems: deciding whether two compound expressions, or words, are equivalent with respect to a set of identities. Higher rewriting generalizes rewriting to higher-dimensional words, or cells, in higher categories. Following Guiraud and Malbos, we use higher rewriting to generalize Mac Lane's coherence theorem. Our result concerns strong linearly distributive categories: categories equipped with two unital tensor products related by invertible distributors. We show that in a strong linearly distributive category every formal diagram commutes.

</details>

### [Proof of a cardinality conjecture for the correction terms in the quantum $K$-theoretic divisor axiom](https://arxiv.org/abs/2611.33597)
*Mizuki Takahashi* · `math.QA` · arXiv:2611.33597v1 · relevance 0.09

- **In one sentence**: The paper proves a Kato–Sagaki conjecture that counts directed paths in the quantum Bruhat graph appearing in the quantum K-theoretic divisor axiom for full flag manifolds in the quasi-minuscule case, showing the count is one or even and the signed sum vanishes when even, so the resulting cancellation-free divisor axiom holds unconditionally.
- **In plain words**: This work is about the geometry of flag manifolds, which are spaces of nested sequences of subspaces, and the counting rules used to describe how they behave under a quantum-style deformation. The authors settle a conjecture posed by Kato and Sagaki about how many special paths of a certain kind arise in a formula. They show the count is always either one or an even number, and that when it is even, the alternating sum of the contributions cancels to zero. This makes a simpler version of the formula valid without the extra assumption.
- **Why it matters**: The result removes a conditional assumption from a published formula, so the cancellation-free divisor axiom is now established rather than conjectural. The text does not indicate wider applications beyond this specific setting, so its broader significance is uncertain from this abstract alone.
- **Background needed**: - Flag manifold: the space of complete nested chains of subspaces, central in representation theory.
- Coxeter group / Weyl group: symmetry groups generated by reflections that index the cells of flag manifolds.
- Quantum K-theory: a deformed version of K-theory (a way of counting geometric objects via vector bundles) that incorporates curve counts.
- Divisor axiom: a rule saying how curve counts change when one intersects with a divisor (a codimension-one subvariety).
- Quantum Bruhat graph: a directed graph on group elements encoding quantum corrections in the flag variety.
- Quasi-minuscule case: a restricted class of root systems where the highest root is nearly the smallest nonzero root.
- Demazure product: an associative operation on Coxeter group elements, used in combinatorial algebra.
- Affine Bruhat order: a partial order on the affine Weyl group, used in Schremmer's results cited by the paper. · level: research-level

<details><summary>Original abstract</summary>

We prove a conjecture due to Kato and Sagaki (arXiv:2604.04476) concerning the cardinality of sets of directed paths in the quantum Bruhat graph that occur in the quantum $K$-theoretic divisor axiom for the full flag manifolds in the quasi-minuscule case. We prove that the cadinality is equal to one or even, and its signed sum vanishes in the latter case. Consequently, the cancellation-free divisor axiom obtained by Kato and Sagaki under this conjecture holds unconditionally. The proof uses Schremmer's results on affine Bruhat order and Demazure products, together with a theorem that we prove for arbitrary Coxeter groups.

</details>

## Number theory

### [Counting complex elliptic curves with self-quotients via class numbers](https://arxiv.org/abs/2611.34150)
*Radu Gaba* · `math.NT` · arXiv:2611.34150v1 · relevance 0.15

- **In one sentence**: The paper counts complex elliptic curves that are isomorphic to their own quotient by a finite subgroup of order n, expressing these counts as sums of proper class numbers over explicit finite sets of quadratic discriminants, with a Magma implementation and a bound on admissible discriminants.
- **In plain words**: The paper studies a family of geometric curves (complex elliptic curves) that, after dividing by a small symmetry subgroup of a given size, look exactly like the original curve. It gives formulas that count how many such curves there are, sorting them by the structure of the subgroup (cyclic, noncyclic, or general). The counts are expressed through class numbers, which measure how many inequivalent ways a quadratic number form can be arranged.
- **Why it matters**: It turns an existing geometric classification into explicit arithmetic counting formulas, which makes the classification easier to compute with and check numerically. The text does not claim wider applications, so any connection beyond this classification is something I cannot confirm from the text.
- **Background needed**: - Elliptic curve: a smooth cubic curve with a group structure, studied over the complex numbers here.
- Isogeny / quotient by a subgroup: a map that divides the curve by a finite symmetry group, producing another curve.
- Complex multiplication (CM): elliptic curves with extra symmetries, tied to quadratic number fields.
- Discriminant D: an integer that encodes a quadratic form; negative discriminants are used here.
- Class number h(D): a count of inequivalent proper classes of forms with discriminant D.
- Smith normal form: a standard matrix reduction giving the invariant factors of a finite group.
- Magma: a computer algebra system used for the numerical examples. · level: research-level

<details><summary>Original abstract</summary>

Let \(n>1\) be an integer. We consider complex elliptic curves \(E\) admitting a finite subgroup \(C\subset E(\mathbb C)\) of order \(n\) such that \(E/C\) is isomorphic to \(E\). % with the additional requirement that the invariant factors of (C) are unequal. We establish class-number counting formulas for the cyclic, noncyclic, and general cases. More precisely, we associate to every negative quadratic-order discriminant \(D\) the norm form \[ Q_D(x,y)=x^2+\varepsilon_Dxy+q_Dy^2, \] where \[ \varepsilon_D\in\{0,1\},\qquad q_D=\frac{\varepsilon_D^2-D}{4}. \] The invariant factors of the kernel of the corresponding endomorphism are determined by \(\gcd(x,y)\). This leads to finite sets of admissible discriminants describing the cyclic, noncyclic, and general cases with unequal invariant factors. Our main result expresses the numbers of isomorphism classes in the three cases as sums of the proper ideal class numbers \(h(D)\) over explicitly defined finite sets of admissible discriminants. This provides an arithmetic class-number counting formulation of the CM classification developed in earlier work by \cite{CanepaGaba2014,CanepaGaba2019,CanepaGabaOlteanu2022} and its subsequent algorithmic extensions. We also characterize the equal-invariant-factor case: it occurs precisely when $n=m^2$, and in that case every complex elliptic curve satisfies the required condition, with the unique subgroup being $E[m]$. We derive an explicit bound for the admissible discriminants, implement the counting procedure in Magma, and give numerical examples. The proof relies on the Smith normal form of the multiplication matrix associated with a quadratic integer. The results provide an arithmetic class-number counting formulation of the CM classification developed in earlier work.

</details>

### [Irreducible trinomials over the binary field: an elliptic-curve criterion and explicit families](https://arxiv.org/abs/2611.34282)
*Siyuan Fu, Zhiming Li, Huaiqing Zuo* · `math.NT` · arXiv:2611.34282v1 · relevance 0.15

- **In one sentence**: The paper gives an elliptic-curve-based criterion for when the trinomial X^((4^k+2)/3)+X+1 is irreducible over F_2, and uses power substitution and linearization to build explicit infinite families of irreducible trinomials X^m+X^n+1 in fourteen reduced exponent classes.
- **In plain words**: The paper studies polynomials with three terms whose coefficients are only 0 or 1, the kind used in error-correcting codes and fast computer arithmetic. It shows that one specific family of these polynomials is irreducible (cannot be factored into smaller pieces) exactly when a certain number of the form 4^k+3 is prime and 2 is a primitive root modulo that prime. It also lists infinite families of such three-term polynomials in fourteen patterns.
- **Why it matters**: Irreducible polynomials over the two-element field matter for building finite fields used in cryptography and coding theory, so explicit families are useful. The abstract does not say how these results compare with earlier work or what practical uses they enable, so their wider significance is unclear from the text alone.
- **Background needed**: - A polynomial over F_2 has coefficients only 0 or 1; arithmetic is done modulo 2.
- "Irreducible" means the polynomial cannot be written as a product of two lower-degree polynomials, analogous to a prime number.
- A trinomial is a polynomial with three nonzero terms, such as X^m + X^n + 1.
- A finite field of size 2^m is built from an irreducible polynomial of degree m.
- A primitive root modulo a prime p is a number whose powers run through every nonzero residue mod p.
- An elliptic curve is a smooth cubic curve with rational points, used here as a tool to count solutions.
- Reciprocity laws are general rules relating solvability of congruences for different primes.
- Power substitution (replacing X by X^a) and linearization are standard ways to transform polynomials into new ones. · level: research-level

<details><summary>Original abstract</summary>

We study irreducible trinomials over $\mathbb{F}_2$. Using an elliptic curve and reciprocity laws, we prove that, for $k \ge 2$, $X^{(4^k+2)/3}+X+1$ is irreducible if and only if $4^k+3$ is prime and $2$ is a primitive root modulo that prime. By power substitution and linearization, we also assemble explicit infinite families of irreducible trinomials $X^m+X^n+1$ in fourteen distinct reduced exponent classes.

</details>

## Algebraic geometry

### [The Dolbeault geometric Langlands-type conjecture for smooth surfaces](https://arxiv.org/abs/2611.33778)
*Yukinobu Toda* · `math.AG` · arXiv:2611.33778v1 · relevance 0.09

- **In one sentence**: The paper builds semiorthogonal decompositions for moduli stacks of one-dimensional sheaves on smooth surfaces with nef anti-canonical divisor, identifies their pieces as quasi-BPS categories of local Calabi–Yau threefolds, and proposes a Dolbeault geometric Langlands-type conjecture for surfaces with Hecke actions on the resulting categories.</one_liner>
<parameter name="plain">This paper is about a very abstract area of mathematics that studies families of geometric objects and how they can be cut into simpler pieces. The authors split a large collection of "sheaves" (a way of attaching data to points of a curved space) on certain surfaces into smaller building blocks, and compare these blocks with another collection of sheaves. From this comparison they propose a conjecture, a precise guess not yet proven, that extends a known correspondence from the Langlands program.
- **Why it matters**: The text presents a construction and a conjecture, not a proven theorem for the full statement, so its importance depends on whether the conjecture holds. It links to the Dolbeault geometric Langlands conjecture and to BPS cohomology, a tool from string-theory-inspired counting of geometric invariants, and it suggests a categorical lift of Hecke operators from recent work by Davison, Hennecart, Kinjo, Schiffmann and Vasserot.</ref>
<parameter name="background">- Coherent sheaf: a algebraic way of attaching vector-space-like data to a geometric space, used as the basic objects here.
- Moduli stack: a space parametrizing such objects together with their symmetries.
- Semiorthogonal decomposition: a way of splitting a category into pieces that interact in a controlled order, analogous to a basis.
- Calabi–Yau threefold: a special kind of 3-dimensional geometric space from string theory; the paper's building blocks are tied to local ones.
- BPS cohomology and quasi-BPS categories: invariants and categorical analogues originating in string-theory counting.
- Higgs bundles and the (Dolbeault) geometric Langlands program: a framework relating vector bundles with extra structure on curves to dual objects.
- Hecke operators: symmetry-like operators acting on these spaces, central to the Langlands program.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

Using a general theory of limit categories for symmetric stacks, we construct their semiorthogonal decompositions for moduli stacks of pure one-dimensional coherent sheaves on smooth surfaces with nef anti-canonical divisors. The components of these semiorthogonal decompositions are quasi-BPS categories associated with the corresponding local Calabi--Yau threefolds. By comparing these semiorthogonal decompositions with those of dg-categories of coherent sheaves on moduli stacks of semistable sheaves, we propose a Dolbeault geometric Langlands-type conjecture for surfaces, generalizing the Dolbeault geometric Langlands conjecture for $\GL_r$-Higgs bundles. Our conjecture includes a correspondence for Higgs bundles twisted by sufficiently ample line bundles on curves. We discuss examples and construct Hecke actions on limit categories and, under certain conditions, on quasi-BPS categories. For symplectic surfaces, these actions are expected to provide a categorical lift of the corresponding Hecke operators on BPS cohomology constructed by Davison--Hennecart--Kinjo--Schiffmann--Vasserot.

</details>

### [Cohomology of pseudo-reductive groups over local function fields](https://arxiv.org/abs/2611.34570)
*Zev Rosengarten* · `math.NT` · arXiv:2611.34570v1 · relevance 0.07

- **In one sentence**: The paper gives a duality pairing identifying the first Galois cohomology of a pseudo-reductive group over a local function field with the Pontryagin dual of the group of translation-invariant line bundles on that group, and equips Picard groups of schemes over Hausdorff topological fields with a topology having favorable properties.
- **In plain words**: The paper studies a certain family of symmetry groups (algebraic groups) defined over a local function field, a kind of number system built from polynomials over a finite field. It shows that one collection of algebraic invariants attached to these groups is the mirror image (dual) of another collection, via an explicit pairing. To make this work, the authors also give a topology to the group of line bundles on such spaces and show it behaves well under mild conditions.
- **Why it matters**: The result is a structural duality theorem in arithmetic algebraic geometry, so its interest is mainly to specialists in algebraic groups and Galois cohomology. The text does not say what wider applications it has, so I cannot say more about its reach.
- **Background needed**: - Algebraic group: a group whose elements are described by polynomial equations, such as matrices with determinant one.
- Pseudo-reductive group: a well-behaved class of algebraic groups that generalises reductive groups (like general linear groups) and is more flexible.
- Local function field: the field of Laurent series over a finite field, the function-field analogue of the p-adic numbers.
- Galois cohomology: an invariant measuring obstructions to solving equations over a field, using symmetries of its algebraic closure.
- Picard group and line bundles: the group of ways of attaching a one-dimensional "twist" to a space, used here with translation-invariance.
- Pontryagin dual: the group of continuous characters (homomorphisms to the circle) of a topological abelian group, which pairs with it.
- Topological field (Hausdorff): a field with a topology in which distinct points can be separated by open sets. · level: research-level

<details><summary>Original abstract</summary>

We give a pairing which describes the first Galois cohomology of a pseudo-reductive group $G$ over a local function field $K$ as the Pontryagin dual of the group $\Ext^1(G, \Gm)$ of translation-invariant line bundles on $G$. In order to accomplish this, we endow the Picard group of a scheme $X$ over a (Hausdorff) topological field with a topology, and prove that this topology enjoys favorable properties under certain mild conditions on $X$ and on the field.

</details>

## Topology

### [Colored Jones polynomial of figure eight knot and non-perturbative topological recursion](https://arxiv.org/abs/2611.34110)
*Alexander Hock, Sergey Shadrin* · `math-ph` · arXiv:2611.34110v1 · relevance 0.10

- **In one sentence**: The paper proves that the asymptotic expansion of the colored Jones polynomial of the figure eight knot is linked to non-perturbative topological recursion on its elliptic spectral curve, as proposed by Borot and Eynard.
- **In plain words**: This work is about knots, the tangled loops studied in topology, and a family of numbers that can be attached to them called the colored Jones polynomial. The authors show that the large-scale behaviour of these numbers for the figure eight knot matches a specific mathematical recipe, known as non-perturbative topological recursion, that was previously only proposed as a conjecture.
- **Why it matters**: It supports a proposal by Borot and Eynard that links knot invariants to curves and geometry, a connection that is of interest to researchers in topology and mathematical physics. The abstract does not say how far the result extends beyond the figure eight knot, so wider impact is unclear from the text alone.
- **Background needed**: - Knot: a closed loop tangled in three-dimensional space, studied up to deformation.
- Knot invariant: a number or polynomial computed from a knot that does not change when the knot is deformed without cutting.
- Colored Jones polynomial: a family of knot invariants indexed by an integer "color" (a dimension parameter); large-color limits are studied.
- Asymptotic expansion: a series that approximates a quantity as a parameter grows large.
- Spectral curve: an algebraic curve encoding a problem, here an elliptic (torus-shaped) one.
- Topological recursion: a recursive procedure that builds invariants of a curve; "non-perturbative" refers to including corrections beyond the leading series terms. · level: research-level

<details><summary>Original abstract</summary>

The asymptotic expansion of the colored Jones polynomial of the figure eight knot is proved to be connected with non-perturbative topological recursion on the underlying elliptic spectral curve, following the proposal of Borot and Eynard.

</details>

### [Regular Additive Scalar Invariants of ${\mathcal N}=1$ Hyperbolic Spin Supertriangles](https://arxiv.org/abs/2610.23209)
*Ilia Gaiur, Robert Penner* · `math.GT` · arXiv:2610.23209v1 · relevance 0.07

- **In one sentence**: The paper classifies the regular cyclic scalar invariants of non-degenerate hyperbolic N=1 spin supertriangles that are additive under geodesic subdivision, using a "common-first" gauge to fix a 3|4 modulus, and reports that this space has superdimension 3|1.
- **In plain words**: The paper studies triangles in a curved, non-Euclidean plane whose sides and angles carry both ordinary numbers and "odd" (fermion-like) quantities, as in supersymmetric geometry. It asks which measurable quantities of such triangles can be added up when a triangle is cut into smaller pieces by a geodesic line, and it finds the complete list of them.
- **Why it matters**: The result gives a precise, countable answer (ordinary area, two even invariants, and one odd invariant) and shows that ordinary supertriangles carry only three even invariants. It may matter for work connecting supergeometry with area and angle-defect formulas, but the text does not say how far those connections extend, so its wider significance is unclear.
- **Background needed**: - Hyperbolic geometry: a curved plane where triangle angles sum to less than 180 degrees; the "angle defect" is the shortfall from 180 degrees, and area is tied to it.
- Geodesic: the shortest path between two points in a curved space, the non-Euclidean analogue of a straight line.
- Supergeometry: an extension of geometry that adds "odd" coordinates which anticommute, giving a grading (degree) and a split between even and odd parts.
- Superdimension "3|1": 3 even dimensions and 1 odd dimension of the space of invariants.
- Additive invariant: a quantity whose value for a whole shape equals the sum of its values for the pieces.
- Spin lift: a choice of spin structure on the triangle; reversing it flips the sign of one invariant.
- Gauge fixing: choosing a standard normal form so that a shape is described by a fixed set of parameters. · level: research-level

<details><summary>Original abstract</summary>

We classify regular cyclic scalar invariants of non-degenerate hyperbolic ${\mathcal N}=1$ spin supertriangles which are additive under geodesic subdivision. After fixing the spin lift, the common-first gauge (introduced in earlier work by the second-named author and further developed here) gives a complete $3|4$ modulus of such supertriangles.. The space of additive scalar invariants is proved to have superdimension $3|1$: ordinary hyperbolic area in degree zero, two even generators in degree two, and one odd generator in degree three; the degree-one and degree-four sectors vanish. One degree-two generator is the fermionic first variation of body area, equivalently the nilpotent correction from ordinary body angle defect to super angle defect. The degree-three generator changes sign under reversal of the spin lift, while the other generators are fixed, so ordinary supertriangles carry only three even invariants.

</details>

## Dynamical systems

### [Integrable nearest neighbor interaction Hamiltonians and the rigidity of the Toda Lattice](https://arxiv.org/abs/2611.34251)
*Vadim Kaloshin, Illya Koval, Daniel Tsodikovich* · `math.DS` · arXiv:2611.34251v1 · relevance 0.14

- **In one sentence**: The paper shows that certain analytic deformations of the three-particle nearest-neighbour Toda lattice potential destroy integrability, without assuming any form for the integrals, using a link between high-energy Toda orbits and billiard orbits in polytopes.
- **In plain words**: The paper studies a simple model of particles on a line, where each particle only pushes on its immediate neighbours, and a famous special case called the Toda lattice that can be solved exactly. The authors alter the pushing law slightly and ask whether the system can still be solved exactly. For three particles, they show that some kinds of smooth alterations break this exact solvability.
- **Why it matters**: The result says the Toda lattice is "rigid": small smooth changes to its interaction law lose the special solvable structure. The authors draw an analogy with the local rigidity of ellipses in billiards, and the link to billiard orbits in polytopes is the main tool, so the work connects mechanics and billiard dynamics. The abstract does not say how broadly the result extends beyond three particles or the stated classes of deformations.
- **Background needed**: - Hamiltonian system: a model of mechanics where energy determines how particles move over time.
- Integrable system: one with enough conserved quantities to be solved exactly, so its motion is regular and predictable.
- Nearest-neighbour interaction: each particle is affected only by the particles directly beside it.
- Toda lattice: a known chain of particles with exponential neighbour interactions that is integrable.
- Deformation: a small change to the interaction law.
- Analytic: smooth in a strong sense, with convergent power series.
- Billiards: the motion of a point bouncing inside a region with straight-line paths between reflections; rigidity of ellipses means an ellipse table cannot be slightly changed while keeping integrability.
- Polytope: a higher-dimensional analogue of a polygon or polyhedron. · level: research-level

<details><summary>Original abstract</summary>

We consider mechanical Hamiltonian systems, where the potentials describe a nearest-neighbor interaction law. In this setting, a non trivial example of an integrable system is the celebrated Toda lattice. We study deformations of this potential (for three particles), and show that some classes of analytic deformations of the potential break its integrability, without assuming anything about the form of the integrals. This result is reminiscent of local rigidity of ellipses in billiards. The proof relies on the fact that high energy orbits for the Toda lattice approximate billiard orbits in some polytopes.

</details>

### [Limit laws for Siegel theta sums](https://arxiv.org/abs/2611.34514)
*Jory Griffin, Jens Marklof, Tariq Osman* · `math.NT` · arXiv:2611.34514v1 · relevance 0.10

- **In one sentence**: The paper proves limit laws and precise heavy-tail asymptotics for the modulus of normalised Siegel theta sums when the quadratic form is chosen at random from the full space of quadratic forms or from the diagonal forms, extending work of Jurkat–Van Horne and Götze–Gordin.
- **In plain words**: The paper studies a kind of exponential sum over a grid of integer points, where the phase of each term is set by a quadratic form (a rule built from squared and cross terms). If the quadratic form is picked at random, the authors show how the size of the normalised sum behaves as the range of summation grows. The limiting behaviour depends on which collection of forms the random choice is drawn from, and they give precise tail estimates for two such collections.
- **Why it matters**: Theta sums appear in number theory, harmonic analysis and the study of automorphic forms, so limit laws for them add to a body of classical results. The text does not say what concrete applications follow, so beyond extending known one-variable and half-space results, its wider significance is unclear from the text alone.
- **Background needed**: - Exponential sum: adding up complex numbers of the form e^(i·phase) over many points; its modulus measures how much the terms cancel.
- Quadratic form: a polynomial whose terms are all of degree two, such as x^2 + 3xy - y^2.
- Lattice: the regular grid of integer points in space.
- Limit law: a statement that a rescaled random quantity converges to a fixed probability distribution.
- Heavy-tail asymptotics: precise description of how slowly the probability of very large values decays.
- Metaplectic group and Shale–Weil representation: a symmetry group and a way of representing it on functions, used as the main tool.
- Unipotent flow and ergodic theory: studying long-run averages of a flow that moves points on a space of lattices, used to analyse the random sums. · level: research-level

<details><summary>Original abstract</summary>

Siegel theta sums are exponential sums over the integer lattice whose phases are determined by a quadratic form. For a random choice of quadratic form, we prove a limit law for the modulus of the normalised sum as the summation range tends to infinity. The limiting distribution depends on the space from which the quadratic form is sampled. We prove precise heavy-tail asymptotics for random sampling from (a) the full space of quadratic forms and (b) the space of diagonal forms. This study extends classic results by Jurkat and Van Horne for one-variable theta sums and by G\"otze and Gordin for theta series on Siegel half-spaces. Our approach uses the Shale--Weil representation of the metaplectic group and the ergodic theory of unipotent flows.

</details>

## Combinatorics

### [List coloring degenerate graphs with requests](https://arxiv.org/abs/2611.34348)
*Rajat Adak, L. Sunil Chandran, Shiwali Gupta et al.* · `math.CO` · arXiv:2611.34348v1 · relevance 0.10

- **In one sentence**: The paper improves the known bounds on list size and satisfaction ratio for flexible list coloring of d-degenerate graphs, at the two extreme parameter values set by the complete graph on d+1 vertices.
- **In plain words**: The paper studies a graph-coloring problem: each vertex gets a short menu of allowed colors, and some vertices request a specific color from their menu, and the question is how many of those requests can be honored at once. The authors prove three results about graphs that are "d-degenerate" (they can be built up or stripped down one vertex at a time, each vertex touching at most d others at that stage). The results concern the extreme settings where the menus are as small as possible and the fraction of satisfiable requests is as large as possible.
- **Why it matters**: The work sharpens a known trade-off between how large each menu must be and what fraction of requests can be guaranteed, and the authors state that the complete graph on d+1 vertices shows these extremes are the natural limits. The text does not say what applications it may have beyond graph theory, so that connection is unclear.
- **Background needed**: - Graph: vertices joined by edges; a coloring gives adjacent vertices different colors.
- List coloring: each vertex has its own allowed list of colors of a fixed size k.
- d-degenerate graph: every subgraph has a vertex with at most d neighbors, so the graph can be emptied one vertex at a time.
- Flexible (k, epsilon) coloring: for any lists and any set of requested colors, a proper coloring exists that satisfies at least an epsilon fraction of the requests.
- Complete graph on d+1 vertices: every pair of vertices is adjacent; it shows list size must be at least d+1 and epsilon at most 1/(d+1).
- Inverse polynomial / inverse exponential: the satisfaction fraction shrinks like a power of d versus like a constant raised to d; the polynomial version is much larger for big d. · level: research-level

<details><summary>Original abstract</summary>

We prove three results on the flexible list coloring of $d$-degenerate graphs. Following Dvo\v{r}\'{a}k, Norin and Postle [J. Graph Theory 2019], a graph $G$ is $(k,\epsilon)$-flexible if for any assignment $L$ of lists of size $k$ to its vertices and any choice of requested colors by a set $\widehat V$ of the vertices from their respective lists, there is an $L$-coloring satisfying at least $\epsilon|\widehat V|$ of the requests. The complete graph on $d+1$ vertices shows that if all $d$-degenerate graphs are $(k,\epsilon)$-flexible for some list size $k$ and satisfaction ratio $\epsilon$, then $k \geq d+1$ and $\epsilon\leq\tfrac1{d+1}$. Our results concern values at or near these extremes. For list size $d+2$, we improve the satisfaction ratio from an inverse exponential to an inverse polynomial function of $d$. For satisfaction ratio $\tfrac1{d+1}$, we prove that it is achievable for list size $2d$ as well as $\left\lfloor(d+2)\left(2-\tfrac1e\right)\right\rfloor$ (which is less than $2d$ for $d\geq 9$).

</details>

### [Monoid Representation of the Determinants of the Adjacency Matrices of 1-joined Path Graphs](https://arxiv.org/abs/2611.34794)
*Daniel Pinzon, Daniel Pragel, Joshua Roberts et al.* · `math.CO` · arXiv:2611.34794v1 · relevance 0.06

- **In one sentence**: The paper studies determinants of adjacency matrices of labeled path graphs joined by one edge, shows the resulting operation forms a finite matrix monoid, and characterizes it via representation theory from Khovanov et al. (2024).
- **In plain words**: The paper looks at networks made of simple chains of connected points, where each chain carries a label saying how it is attached to others. For each network it computes a single number, the determinant of a table (matrix) that records which points are linked. Joining chains together by one link follows a consistent rule, and the authors show that these numbers and the joining operation form a finite algebraic system whose full structure they describe.
- **Why it matters**: The text presents a complete description of this algebraic structure and says it yields general formulas for determinants of chains of joined paths, which is a concrete payoff. The text does not say how far these methods extend beyond this family of graphs, so wider connections are uncertain.
- **Background needed**: - Graph: a set of points (vertices) joined by lines (edges).
- Adjacency matrix: a grid of 0s and 1s recording which vertices are directly linked.
- Determinant: a single number computed from a square grid of numbers; it summarizes certain properties of that grid.
- Monoid: a set with an associative combining operation and an identity element, like multiplication of numbers but without requiring inverses.
- Finite monoid of matrices: a finite collection of matrices closed under multiplication, with an identity.
- Representation theory: a way of studying abstract algebraic objects by mapping them to concrete matrices or linear transformations.
- Prior work: the paper builds on earlier work by the same authors and on Khovanov et al. (2024), which the text does not describe. · level: research-level

<details><summary>Original abstract</summary>

Following previous work by these authors, this paper explores all labeled path graphs joined by 1 edge where the labeling contains the information on how to join that graph. The algebraic structure that this operation has on the determinant of the adjacency matrix of the graph gives a finite monoid of matrices under matrix multiplication. We completely characterize the monoid using the representation theory discussed in Khovanov et al(2024). Finally, we demonstrate how these results can be used to find general formulas for the determinants of chains of 1-joined labeled paths.

</details>

## Numerical analysis

### [Barron Smoothness for Layers in Deep Neural Networks](https://arxiv.org/abs/2611.34805)
*G. Welper* · `cs.LG` · arXiv:2611.34805v1 · relevance 0.14

- **In one sentence**: The paper splits deep network approximation error into choosing infinite-width limits per layer and then discretizing each layer, shows the discretization cost is characterized in expectation by a layer-wise Barron norm, and links local minima of the optimization to an equidistribution principle.
- **In plain words**: The paper studies how accurately a deep neural network can approximate a target function when its layers are made finite in width. It splits the problem into two steps: first picking ideal "infinitely wide" versions of each layer, then approximating each layer with a finite number of units. The authors report that the cost of the second step, on average, is described by a layered version of a known smoothness measure called the Barron norm, and that the best solutions of the optimization look like spreading units out evenly in a specific sense.
- **Why it matters**: Bounds on how well neural networks can approximate functions are a core theoretical question, and the paper offers a new way to frame them layer by layer. The link to adaptive spline and finite element methods, where points are placed to balance error, may be a useful bridge between the two fields, though the text alone does not show how far this connection extends.
- **Background needed**: - Neural network approximation: how closely a network with a given size can mimic a target function.
- Infinite width limit: the idea of letting the number of units in a layer grow without bound, which makes the analysis simpler.
- Discretization: replacing a continuous idealized layer with a finite set of units.
- Barron norm: a measure of how smooth or simple a function is, used to bound approximation error for shallow networks.
- Equidistribution: spreading points so that some error measure is roughly even across the domain; used in adaptive spline and finite element methods.
- The abstract gives only a summary; the full statements and proofs are not available here. · level: research-level

<details><summary>Original abstract</summary>

In order to bound approximation errors for deep neural networks, we split the problem into two steps: First the selection of optimal infinite width limits for each layer and second an optimal discretization of all layers to obtain finite sized networks. We show that in expectation, the latter problem is equivalently characterized by a layer wise generalization of Barron norms. Moreover, we provide an analysis of the optimization landscape and show that local minima are characterized by an equidistribution principle akin to similar ideas in adaptive spline and finite element approximation.

</details>

### [CAMPS: Composable Adapters for Mixed-Precision Solvers](https://arxiv.org/abs/2611.33703)
*Kevin Li, Chandrajit Bajaj* · `cs.MS` · arXiv:2611.33703v1 · relevance 0.13

- **In one sentence**: CAMPS is a framework that chains iterative-refinement adapters across floating-point precisions (FP64, FP32, FP16) in a solver tree, with proven backward-error and convergence conditions, tested on dense and sparse linear systems.
- **In plain words**: Computers store numbers with different amounts of precision: more precision is slower and uses more memory, less is faster but less accurate. This paper describes a way to plug faster, low-precision solvers inside a slower, accurate one, so the rough work is done cheaply and the accurate layer checks and corrects it. The authors report that this matched or beat their test methods on many systems of equations, but not on all, and that it falls back to full precision when the cheap steps fail.
- **Why it matters**: Solving large systems of equations is a core task in science and engineering, and saving time and memory without losing accuracy matters for those workloads. The paper's main claims are backed by proofs and tests on specific problem types, so it is best read as a careful method for a niche, not a general speedup.
- **Background needed**: - A linear system is a set of equations Ax = b, solved for unknown x; "dense" and "sparse" describe how much of matrix A is nonzero.
- Floating-point precision (FP64, FP32, FP16) is how many bits a computer uses per number: 64, 32, or 16 bits, trading speed and memory against accuracy.
- Iterative refinement: solve roughly in low precision, compute the residual (the leftover error Ax - b) in high precision, and solve again for a correction.
- Backward error: how far the computed answer is from the exact answer of a slightly perturbed problem; a small value means the answer is trustworthy.
- Conjugate gradient is an iterative method that works well for symmetric positive definite matrices.
- Solver tree: a nested arrangement where a solver calls a child solver to handle its correction steps. · level: research-level

<details><summary>Original abstract</summary>

Mixed-precision solvers usually assign a fixed precision to each algorithmic component. This makes it hard to reuse a lower-precision solver at different depths inside a higher-precision solver. We introduce CAMPS (Composable Adapters for Mixed-Precision Solvers), a framework that uses iterative refinement to connect solvers across precisions. An adapter computes residuals and updates in the precision of its parent and passes each correction solve to a child solver in a lower precision. The child can be a direct solver, an iterative solver, or another adapter. The adapter checks every correction and keeps it if the residual does not increase. We prove three results. Adapters can be placed at any compatible set of precision boundaries in a solver tree without breaking the solver interface. Every output that the root solver reports as successful satisfies a backward-error bound set by the stopping tolerance and the root precision. Convergence follows from one sufficient condition per boundary, computed from the leaves of the tree to its root. We test five configurations on dense and sparse systems in 64-bit, 32-bit, and 16-bit floating-point arithmetic (FP64, FP32, and FP16). On dense well-conditioned systems, CAMPS is up to 9.6x faster than an FP64 direct solver for a single solve that includes the factorization. On sparse nonsymmetric systems, a three-precision hierarchy is the fastest method we tested. Compared with our implementation of the nested solver F3R, CAMPS is as fast and uses about 3.4x less peak memory. CAMPS does not always win. Plain conjugate gradient is faster on sparse symmetric positive definite systems. On very ill-conditioned systems, FP32 corrections fail, and the adapter detects the failure and switches to an FP64 fallback.

</details>

## Logic and foundations

### [A Sequent Calculus for the Quantified Reflection Calculus $\mathrm{QRC}_1$: Cut-Elimination, Interpolation, and NP-Completeness](https://arxiv.org/abs/2611.33345)
*Mitar Nedeljkovi\'c* · `math.LO` · arXiv:2611.33345v1 · relevance 0.05

- **In one sentence**: The paper gives the first Gentzen-style sequent calculus for the quantified reflection calculus QRC_1, proves cut-admissibility, interpolation and finite model property results, and claims NP-completeness of its decision problem over fixed signatures.
- **In plain words**: This paper is about a formal logic that describes what provability in arithmetic can say, extended to allow quantifiers over statements. The authors build a new proof system for this logic, in which every step of reasoning follows a fixed set of rules, and use it to establish several structural properties. They also state that deciding whether a given formula is valid in this logic is NP-complete, meaning it is hard in a precise but comparatively manageable sense.
- **Why it matters**: The paper matters mainly to specialists in proof theory and modal logic, since it offers a clean proof system for a logic that earlier results suggested would be hard to handle. Its links to provability in Peano and Heyting Arithmetic make it relevant to the foundations of mathematics, but the text itself does not say how far these results reach beyond that area.
- **Background needed**: - Modal logic: a logic with operators such as "it is provable that", studied with possible-worlds (Kripke) semantics.
- Sequent calculus (Gentzen-style): a proof system where proofs are built from rules that manipulate sequents, which are lists of assumptions and conclusions.
- Cut-elimination: showing that a proof rule called "cut" (a shortcut that uses an intermediate lemma) can always be removed, which gives proofs with controlled structure.
- Craig interpolation: given a valid implication, one can find an intermediate formula using only shared vocabulary.
- Decision problem and NP-completeness: asking whether an algorithm can decide validity, and how hard that is; NP means answers can be checked quickly, though finding them may be hard.
- Peano and Heyting Arithmetic: standard formal systems of arithmetic (classical and intuitionistic). · level: research-level

<details><summary>Original abstract</summary>

We introduce $\mathrm{G3QRC}_1$, the first Gentzen-style sequent calculus for Borges and Joosten's Quantified Reflection Calculus ($\mathrm{QRC}_1$). As a strictly positive, first-order modal logic, $\mathrm{QRC}_1$ crucially escapes Vardanyan's $\Pi^0_2$-completeness theorem for quantified provability logic, while remaining arithmetically complete with respect to Peano and Heyting Arithmetic. The central innovation of $\mathrm{G3QRC}_1$ is a pair of context-erasing modal rules that simultaneously account for the monotonicity and transitivity axioms by deliberately discarding parametric context across modal boundaries. This structural bottleneck allows for a clean proof of cut-admissibility via a standard lexicographic induction, circumventing the complex loop-checking typically required for provability logics. Cut admissibility yields an instantiated subformula property and supports a direct canonical proof of the finite model property. We streamline the adequate Kripke semantics by interpreting constants globally. We also establish a split-context Craig interpolation theorem and a contextual form of left uniform interpolation, uniformly eliminating private predicate symbols, constants, and free parameters. Finally, by leveraging the rigid structural constraints of the context-erasing rules and the absence of left-branching connectives, we prove that, over the standard fixed countable signatures specified in the paper, the decision problem for $\mathrm{QRC}_1$ is $\mathbf{NP}$-complete, situating this quantified modal logic in a comparatively low nondeterministic complexity class.

</details>

### [Well-foundedness of the strict Lipschitz order on countably complete filters](https://arxiv.org/abs/2611.34850)
*Gabriel Fernandes, Matheus Duzi* · `math.LO` · arXiv:2611.34850v1 · relevance 0.04

- **In one sentence**: In ZF+DC, the strict Lipschitz order on proper countably complete filters on a fixed ordinal is shown to be well-founded, and two ultrafilters on the same ordinal are shown to be equal when each is nonexpansively reducible to the other, answering both parts of Question 9.2.11 of The Ultrapower Axiom.
- **In plain words**: This paper is about a question in set theory: how to compare certain collections of large-scale "measurements" on infinite sets, called filters, so that there is no endless downward chain of ever-smaller ones. The text reports that, under the standard background axioms (ZF plus dependent choice), such a comparison order has no infinite descending chains. It also reports that two of these special collections, called ultrafilters, are equal whenever each can be reduced to the other in a bounded way.
- **Why it matters**: The results settle both parts of a specific open question posed in a known book on the Ultrapower Axiom, a proposed principle in set theory. The text does not say more broadly how much this affects the field, and I am not certain what further consequences it has beyond answering that question.
- **Background needed**: - ZF and DC: standard foundational axioms of set theory (Zermelo-Fraenkel, plus dependent choice), without the full axiom of choice.
- Ordinal: a well-ordered "counting" number extending the natural numbers into the infinite.
- Filter: a family of large subsets of a set, closed under taking supersets and intersections; "countably complete" means closed under countable intersections.
- Ultrafilter: a maximal filter, which decides for every subset whether it is "large."
- Well-founded order: one with no infinite descending chains, which allows induction and recursion.
- Lipschitz/nonexpansive reduction: a way of comparing filters via a map that does not stretch distances, roughly a bounded-complexity comparison.
- Ultrapower Axiom: a proposed set-theoretic principle studied in a book by Goldberg; the question numbering refers to that book. · level: research-level

<details><summary>Original abstract</summary>

In $\mathsf{ZF}+\mathsf{DC}$, the strict Lipschitz order on proper countably complete filters on any fixed ordinal is well-founded. The proof uses transfinite recursion and closure under countable intersections to derive a contradiction from a descending chain. Restricting each filter to the least ordinal it contains yields a set-like well-founded order that compares filters on different ordinals. In $\mathsf{ZF}$, two ultrafilters on the same ordinal are equal if each is nonexpansively reducible to the other. These results answer both parts of Question 9.2.11 in The Ultrapower Axiom.

</details>

## Mathematical physics

### [The integrable Lie-Trotter-Suzuki decomposition for nonlinear dynamics: Efficient Hamiltonian simulation of the Stepanoff flow](https://arxiv.org/abs/2611.34768)
*Ilon Joseph, Ivan Novikau, Michael R. Montgomery et al.* · `quant-ph` · arXiv:2611.34768v1 · relevance 0.08

- **In one sentence**: The paper proposes an "integrable Lie-Trotter-Suzuki" time-stepping scheme for nonlinear dynamics and applies it to the Stepanoff flow on a torus, mapping the two-dimensional system onto a quantum circuit built from quantum Fourier transforms and quantum signal processing, checked with a fault-tolerant quantum emulator.</one_liner>
<parameter name="plain">The paper looks at how to step forward in time a nonlinear system, meaning one whose rules do not add up neatly, such as certain fluid-like flows. The authors split the system's update rule into pieces that can each be computed efficiently, then combine them in small time steps. They apply this to a two-dimensional flow on a torus (a donut-shaped surface) and report that a simulated quantum computer gives results consistent with several classical methods.</plain>
<parameter name="why">The work offers a way to bring nonlinear dynamics within reach of quantum-style, unitary (norm-preserving) simulation, which could matter for fluid and chaotic-system modelling. The text does not establish a practical speed-up over classical methods, and it notes that the small time steps and the linear cost of the advection operator with grid size remain limitations.</why>
<parameter name="background">- Nonlinear dynamics: systems where the change at each moment depends non-proportionally on the current state, so they can behave unpredictably.
- Hamiltonian simulation: computing how a system evolves over time using a unitary operator, which preserves total "amount" (norm) of the state.
- Lie-Trotter-Suzuki decomposition: approximating a complicated time evolution by alternating simpler steps, with accuracy improving as the time step shrinks.
- Tensor product factorization and block-encoding: ways of writing a large matrix so a quantum or tensor-network computer can apply it efficiently.
- Quantum Fourier transform (QFT) and quantum signal processing (QSP): standard quantum subroutines, the first for changing between position and frequency representations, the second for applying polynomial functions of an operator.
- Fault-tolerant quantum computing: the error-corrected regime; here it is simulated numerically rather than run on hardware.
- Transfer operator: a linear operator that describes how probability or densities move under the dynamics.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

We propose an efficient unitary numerical time integration strategy for nonlinear dynamical systems: the integrable Lie-Trotter-Suzuki decomposition (I-LTS). First, express the generator as a sum of integrable parts. Second, approximate the full evolution operator using a Lie-Trotter-Suzuki (LTS) decomposition of the desired approximation order in time step. The I-LTS construction ensures that the full evolution operator can be represented as a product of terms that each have an efficient explicit tensor product factorization that can be handled efficiently with tensor network and/or quantum block-encoding methods. Next, we apply this method to an important non-integrable point example of a dynamical system: the Stepanoff flow on the torus. First, we derive an efficient unitary quantum algorithm for simulating the Stepanoff flow that can be thought of as a unitary classical version of a quantum map. Then, we provide a detailed description of the encoding of the two-dimensional system into an efficient quantum circuit, including an efficient block-encoding for all required operators. An efficient Hamiltonian simulation algorithm is constructed using a sequence of alternating quantum Fourier transforms (QFT) and Quantum Signal Processing (QSP) circuits. Finally, the circuit is simulated using a numerical emulator of fault-tolerant quantum computers, and the results are found to be consistent with several alternative classical computational methods. While efficient, the need for Trotterization introduces fundamental complexity in requiring small enough time step for an accurate approximation and solving for the transfer operator requires one to confront the linear scaling of the advection operator with grid size.

</details>

### [Schwinger-Dyson recursion, Gr\"obner elimination and graph combinatorics](https://arxiv.org/abs/2611.34114)
*Oleg Evnin* · `math-ph` · arXiv:2611.34114v1 · relevance 0.08

- **In one sentence**: Applies Schwinger-Dyson equations, reduced via Gröbner elimination, to zero-dimensional QFT moment problems and obtains a finite recursion for counting labelled 9- and 10-regular graphs on n vertices.
- **In plain words**: This paper is about counting graphs, the networks of points joined by lines, that have a fixed number of connections at every point. The authors borrow a set of equations from quantum field theory that relate averages of polynomial expressions to one another, and use an algebra tool (Gröbner elimination) to reduce them to a small finite set of basic quantities. They report that for graphs with 9 or 10 connections per vertex this gives a recursive method that computes the total count in O(n) arithmetic steps, where n is the number of vertices.
- **Why it matters**: The text describes the result as a computational improvement over the existing state of the art for these graph counts, and the link to counting discrete geometries in simplicial approaches to quantum gravity suggests where it could matter. The abstract alone does not show how broadly the method extends beyond 9- and 10-regular graphs, so its wider reach is unclear.
- **Background needed**: - Schwinger-Dyson equations: relations from integration by parts that link averages (correlators) of different polynomial orders.
- Zero-dimensional QFT: a quantum field theory with no space or time, reducing to multivariate Gaussian integrals.
- Moments/correlators: averages of powers of variables under a Gaussian weight.
- Gröbner elimination: a systematic algebra method for rewriting polynomial relations so that higher quantities are expressed through a fixed finite basis.
- k-regular graph: a graph where every vertex has exactly k edges; labelled means vertices are distinguishable.
- Big-O notation: O(n) means the work grows roughly in proportion to n. · level: research-level

<details><summary>Original abstract</summary>

Schwinger-Dyson equations are a cornerstone of quantum field theory (QFT). Derived using integration by parts, they capture relations between correlators of different orders, forming an open, infinite-dimensional system. In zero-dimensional QFTs with polynomial actions, which is just a physical interpretation for multivariate Gaussian integrals with polynomial insertions, conventional Gr\"obner elimination can be used to express all higher-order correlators (moments) in terms of a fixed basis set. One consequence is a closed finite-dimensional system of differential equations for the coupling dependence of these `master' correlators. An important application of zero-dimensional QFTs is in counting discrete geometric structures (as in simplicial approaches to quantum gravity). For the problem of counting labelled regular graphs, applying this Schwinger-Dyson closure results in a computational breakthrough relative to the existing state-of-the-art: for 9- and 10-regular graphs on $n$ vertices, a finite-depth, finite-width recursive formulation is obtained, making it possible to compute the total graph counts in $O(n)$ arithmetic operations.

</details>

## Optimization and control

### [Policy and Value Iteration for Entropy-Regularized Stochastic Control](https://arxiv.org/abs/2611.34002)
*Yuling Jiao, Peiying Wu, Jerry Zhijian Yang et al.* · `math.OC` · arXiv:2611.34002v1 · relevance 0.15

- **In one sentence**: The paper analyzes a policy-and-value iteration scheme for finite-horizon entropy-regularized stochastic control with action-independent diffusion, proving a uniform error bound on the final policy's excess regularized cost and convergence under vanishing errors.
- **In plain words**: The paper studies how to find a good strategy for steering a system that is pushed around by random noise, when the strategy is allowed to be deliberately spread out rather than fixed. The method alternates between two steps: it estimates how good the current strategy is, then rebuilds the strategy as a weighted "Gibbs" distribution based on that estimate. The authors prove a guaranteed bound on how far the final strategy's cost can be from the best possible, and they test the method on finite-horizon problems and a discounted routing problem.
- **Why it matters**: The text gives a provable error bound and tests on problems with known solutions and on a 10,000-dimensional benchmark, which suggests the method is practical for high-dimensional control. Its relevance beyond control theory is not established by the text, so any wider connections should be treated as speculative.
- **Background needed**: - Stochastic control: choosing actions over time for a system affected by random noise, aiming to minimize a cost.
- Entropy regularization: adding a penalty for strategies that are too deterministic, so the best strategy becomes a spread-out probability distribution.
- Hamilton-Jacobi-Bellman (HJB) equation: a partial differential equation whose solution gives the optimal cost-to-go from each state and time.
- Policy iteration vs. value iteration: alternating between evaluating a strategy and improving it, which is the general pattern used here.
- Gibbs distribution: a probability distribution that favors lower-cost actions, with weights set by an exponential of the cost.
- Kullback-Leibler (KL) divergence: a measure of how different one probability distribution is from another.
- Finite vs. infinite horizon: planning over a fixed time window versus an ongoing discounted problem. · level: research-level

<details><summary>Original abstract</summary>

We study finite-horizon entropy-regularized stochastic control with action-independent diffusion. To solve the associated Hamilton-Jacobi-Bellman (HJB) equation, we alternate between value and policy updates. Each iteration approximately solves a linear backward equation for the current policy, then approximates the Gibbs distribution defined by the resulting value gradient. We prove a uniform bound on the final policy's excess regularized cost. The bound assigns explicit, summable weights to the evaluation residuals and the Kullback-Leibler divergences from the updated policies to their Gibbs targets. Under the stated assumptions and with exact terminal data, vanishing errors in both steps imply uniform convergence to the optimal value. Two finite-horizon execution problems test value accuracy against a known solution and closed-loop performance when no exact solution is available. We also evaluate the iteration on a discounted infinite-horizon routing problem with twelve modes and an unregularized HJB benchmark in up to 10,000 dimensions.

</details>

### [The Monge Optimal Transport Barycenter Problem with Adaptive Features](https://arxiv.org/abs/2611.34494)
*Yige Zhou, Esteban G. Tabak* · `math.OC` · arXiv:2611.34494v1 · relevance 0.15

- **In one sentence**: The paper extends the data-driven Monge optimal transport barycenter problem by making the test features themselves adaptive, using Gaussian radial basis functions whose centers and bandwidths are optimized, and applies it to multidimensional covariates.
- **In plain words**: The paper studies how to adjust a measurement so that it no longer carries information about another variable, such as age or weather, while changing it as little as possible. The usual numerical method checks for leftover dependence using a fixed set of test functions, and how well it works depends heavily on which functions are chosen. The authors let those functions adapt during the procedure and report that this removes dependence better than a fixed small set, reaching results comparable to a larger fixed set in synthetic tests.
- **Why it matters**: Removing a variable's dependence on confounding factors matters in fields such as biomedical measurement and demand forecasting, and the text reports applications to age-related biomedical data and bike-sharing demand. The text does not say how these results compare with other established methods, so its practical advantage is not established beyond the reported experiments.
- **Background needed**: - Optimal transport: finding the least-disruptive way to reshape one distribution into another, here a map y = T(x, z).
- Barycenter / dependence removal: the goal is an output that is statistically independent of covariates z.
- Test functions: fixed or learned functions used to detect leftover statistical dependence; the independence condition is only approximated with a finite set of them.
- Radial basis functions (RBFs): smooth bumps centered at chosen points with a width (bandwidth); here their centers and widths are tuned during optimization.
- Synthetic vs. real experiments: the core evidence is simulated data, with real-world tests described only briefly in the text. · level: research-level

<details><summary>Original abstract</summary>

The data-driven Monge optimal transport barycenter problem seeks a map $y=T(x,z)$ that minimally perturbs an outcome $x$ while removing its statistical dependence on covariates $z$. Numerical implementations approximate the independence constraint through finite-dimensional test-function spaces, making the effectiveness of dependence removal sensitive to the choice of features. This article develops a procedure whereby the features themselves are optimized throughout the procedure. In particular, we adopt a feature space for $f$ consisting of Gaussian radial basis functions (RBFs) with adaptive individual centers and bandwidths. Synthetic experiments show that while fixed nonlinear RBF features can capture dependence structures that are poorly represented by linear features, adapting the RBF centers and bandwidths can further improve dependence removal within a limited feature space and achieve residual dependence comparable to that obtained with a larger fixed basis. We further extend the formulation to multidimensional covariates and evaluate its applicability to real-world problems, including removing age-related dependence in biomedical measurements and dependence on temperature and humidity in bike-sharing demand.

</details>

## Statistics theory

### [Estimation for High-Dimensional Hawkes Processes with Inhibition via CIR Approximation](https://arxiv.org/abs/2611.33484)
*Nadia Belmabrouk, Mohamed Ben Alaya, Xavier Erny* · `math.ST` · arXiv:2611.33484v1 · relevance 0.07

- **In one sentence**: The paper builds parametric estimators for a high-dimensional Hawkes process with inhibition by approximating it with a CIR process, proving an explicit convergence rate in the joint large-population, long-time regime and establishing consistency and asymptotic normality of the estimators.
- **In plain words**: The paper studies a model of many interacting random event streams, where each event can make others more or less likely to occur (here, "inhibition" means events suppress further events). Rather than analyzing the original model directly, the authors show it can be closely approximated by a simpler, well-studied random process (the Cox-Ingersoll-Ross process). Using that approximation, they build simple estimators for the model's unknown parameters and report numerical experiments that illustrate the results.
- **Why it matters**: Estimating parameters in systems with many interacting components over long observation times is hard, and a simpler approximating process can make the calculations tractable. The stated technical contribution is handling a diffusion coefficient that is not Lipschitz (it does not change smoothly enough for standard tools), which the text says required specific techniques. The text does not indicate specific application areas, so its wider relevance is unclear from the abstract alone.
- **Background needed**: - Hawkes process: a random point process in which past events raise (excitation) or lower (inhibition) the rate of future events; widely used to model things like neuron spikes, trades or earthquakes.
- High-dimensional: many interacting components (here, a large population of such processes).
- CIR process: a mean-reverting random process, often used in finance for interest rates, that stays nonnegative.
- Parametric estimation: inferring a model's unknown numerical parameters from observed data.
- Consistency and asymptotic normality: estimators converge to the true values as data grows and their errors follow a bell-shaped distribution in the large-sample limit.
- Lipschitz condition: a smoothness requirement on a function that many standard convergence proofs rely on; its failure makes the analysis harder. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we develop a parametric estimation method for a high-dimensional Hawkes processes with inhibition. The proposed approach relies on a quantitative approximation of the Hawkes process by a Cox-Ingersoll-Ross (CIR) process. In particular, we establish an explicit convergence rate in the joint large-population and long-time regime. This result requires specific techniques to handle the non-Lipschitz diffusion coefficient of the limiting CIR process.Based on this approximation, we construct explicit and easily implementable estimators of the model parameters. We establish their consistency and asymptotic normality. We also conduct numerical experiments to illustrate our findings.

</details>

### [PrO Filtering via Kernel Mean Embedding Dynamics](https://arxiv.org/abs/2611.34809)
*Linfeng Wang, Nikolas N\"usken, Chris. J. Oates* · `stat.ME` · arXiv:2611.34809v1 · relevance 0.05

- **In one sentence**: This paper gives the first particle-based (nonparametric) implementation of predictively-oriented (PrO) filtering, using kernel mean embedding dynamics to transport particles from the forecast distribution to the PrO filtering distribution.
- **In plain words**: Filters are methods that keep updating a best guess of a hidden system's state as new measurements arrive, and they can become overconfident or fail when the model behind them is wrong. This paper extends a recent alternative, PrO filtering, which hedges by placing probability near both the forecast and the conflicting observation, and replaces its earlier Gaussian (bell-curve) approximation with a flexible sample-based method. The authors report substantial gains over the Gaussian version on challenging nonlinear examples.
- **Why it matters**: Filters that stay reliable under model misspecification matter in tracking, forecasting and control, and the paper's proof that the number of update steps does not grow with how surprising an observation is gives it a concrete theoretical point of comparison with the standard Bayesian tempering approach. The text does not show how broadly the method would perform beyond the examples reported, so its wider practical reach is uncertain.
- **Background needed**: - State-space model: a hidden system state that evolves over time, observed only through noisy measurements.
- Bayesian filter: recursively updates the probability distribution of the state using a forecast and each new observation.
- Misspecified model: the assumed model differs structurally from the true process, so Bayesian updates can become overconfident.
- Hedging: spreading belief over both the forecast and the observation when they conflict.
- Particle method: representing a distribution by many weighted or unweighted sample points.
- Kernel mean embedding: representing a distribution as a point in a function space so it can be moved (transported) smoothly.
- Tempering path: gradually moving from one distribution to another in small steps, here as a function of how surprising the observation is. · level: research-level

<details><summary>Original abstract</summary>

Filtering methods are routinely deployed with misspecified state-space models, where Bayesian filters can diverge and become overconfident. Predictively-oriented (PrO) filtering is a recent, hyperparameter-free alternative that was demonstrated to outperform (generalised) Bayesian filtering methods when either the dynamical model or the measurement model is structurally misspecified. This can be attributed to \emph{hedging} behaviour: when an observation conflicts with the forecast, the PrO update places mass near both. Yet existing implementations of PrO filtering rely on unimodal (Gaussian) approximations, whose ability to effectively hedge is limited. This paper develops the first nonparametric, particle-based implementation of PrO filtering. The key obstacle, that PrO filtering distributions are only implicitly defined, is overcome by constructing a path from the predictive to the PrO filtering distribution whose rate is available in closed form, enabling the use of kernel mean embedding dynamics for measure transport. The resulting algorithm requires only simulation from the dynamical model and evaluations of the likelihood, with neither importance weights nor the predictive density. Moreover, as we prove, the number of pseudo-time steps it requires does not grow with the outlyingness of the observation, in contrast to transport along the Bayesian tempering path. An empirical assessment shows substantial improvement over Gaussian variation of PrO filtering in challenging nonlinear examples where Gaussian approximation is unreasonably limited.

</details>

## Statistical methods and applications

### [Using waveform types, discrete Sobolev distances, and trend compatibility to cluster short time series of clinical data](https://arxiv.org/abs/2611.33623)
*Robyn J. N. Kettlitz, Daniel Cisternas, Alvaro Olivera-Nappa et al.* · `q-bio.QM` · arXiv:2611.33623v1 · relevance 0.12

- **In one sentence**: A nonparametric method that groups short, undersampled clinical response curves (five-point oral glucose tolerance tests) by sorting them into trend-compatible unit waveforms and comparing shapes with discrete Sobolev-type distances, with the number of clusters set by the trend patterns the cohort actually populates.
- **In plain words**: Clinical tests such as the glucose tolerance test push the body out of rest and record how glucose and insulin change over a few timed blood samples. The paper proposes a way to group these very short curves by their overall shape, so that patients who recover from the test in similar ways end up together. Applied to 1283 tests, it found 7 glycemia response types and 8 insulin response types, and it kept the same count across a threefold range of resolution.
- **Why it matters**: Short clinical curves usually get reduced to a few summary numbers, which discards how the body recovers after the challenge; this paper offers a way to keep that trend information. The text reports benchmarks against six classical clustering methods, where the proposed method alone never mixed opposite trends, but it does not establish clinical usefulness, and the link to diagnosis is only suggested by the graded clinical-normality result.
- **Background needed**: - Oral glucose tolerance test (OGTT): a patient drinks a sugar solution and blood glucose and insulin are measured at a few times afterward.
- Time series: a sequence of measurements over time; "undersampled" means only a few points are taken.
- Clustering: grouping items so that members of a group are similar and different groups are distinct.
- Finite differences: changes between neighbouring points; the order k indicates how many times you take differences, capturing trend and curvature.
- Sobolev-type distance: a way of measuring how different two curves are, including how their slopes and bends differ, not just their heights.
- Resampling validation: checking that a result holds when the data are randomly re-drawn or re-split.
- Nonparametric: makes few assumptions about the shape of the underlying data distribution. · level: research-level

<details><summary>Original abstract</summary>

Clinical tests, such as the oral glucose tolerance test (OGTT), perturb a physiological system at rest and record its excursion over a fixed protocol window as a short, undersampled time series. Such curves rarely allow parameter identification at the individual level, yet their trends carry physiological information that emerges at the population level as recurrent response patterns. Standard clustering methods aggregate differences globally and average out those trends, losing precisely the information about how the system regains control after the perturbation; identifying response patterns requires a method that preserves them. We present a nonparametric framework that factorizes each curve into unit waveforms, sorts them with a symbolic trend-compatibility filter, and compares compatible shapes using discrete Sobolev-type distances on finite differences up to order $k$. The number of clusters, i.e., distinct response types, equals the number of realizable trend patterns the cohort populates, validated by resampling. Applied to 1283 five-point OGTTs, the method identifies 7 glycemia and 8 insulinemia types. The count holds across a threefold range of resolution. In benchmarks against six classical clustering methods, ours alone never mixes opposite trends, with comparable reconstruction error and stability. Clinical normality, assessed after clustering, is graded, overlapping, and distributed unevenly across response types ($h=0.14$--$0.48$). Overall, our method distinguishes response types among curves too short for alignment-based methods yet too informative for reduction to summary values. It applies to any protocol recording a system's response to a standardized perturbation on a short grid.

</details>

### [k-Nearest Neighbors estimation of the drift of an ergodic diffusion process under Osgood regularity](https://arxiv.org/abs/2611.33596)
*Eddy Michel Ella-Mintsa* · `stat.ME` · arXiv:2611.33596v1 · relevance 0.10

- **In one sentence**: The paper proves consistency of k-nearest-neighbors estimators for the drift (deterministic trend) of an ergodic diffusion process over compact and non-compact intervals, under relatively weak regularity (Osgood-type) conditions on the coefficients.
- **In plain words**: The paper studies how to estimate the hidden "pull" that shapes a randomly moving process, such as a noisy price or particle path that keeps returning to a typical range. The authors apply the k-nearest-neighbors method, a simple idea that averages nearby observations, and show it converges to the true answer under fairly mild assumptions. Previous work on this approach had mostly relied on computer experiments rather than proofs.
- **Why it matters**: Putting a mathematical guarantee behind a popular, easy-to-use method extends the justification for using it in the statistics of continuous-time random processes. The text does not indicate applications beyond the numerical illustrations it mentions, so wider impact is unclear.
- **Background needed**: - Diffusion process: a continuous random motion, described by a drift (average direction of movement) and a volatility (size of random noise).
- Ergodic: the process over time explores its typical states, so long observations reveal its long-run behaviour.
- Drift estimation: inferring the drift function from observed trajectory data.
- k-nearest neighbors (kNN): estimating a value at a point by averaging the k observations closest to it.
- Consistency: the estimator converges to the true function as the amount of data grows.
- Osgood regularity: a mild smoothness condition on the coefficients, weaker than the usual differentiability assumptions.
- Compact vs non-compact interval: whether the state range is bounded or extends without limit. · level: research-level

<details><summary>Original abstract</summary>

The k-Nearest Neighbors (kNN) algorithm is a widely used machine learning method with well-established theoretical guarantees for consistent estimation in multivariate settings and functional time series analysis. In the context of nonparametric estimation of the coefficients of ergodic diffusion processes, however, its use has so far been mainly illustrated through numerical experiments. The main contribution of this paper is to establish theoretical consistency results for drift kNN estimators over both compact and non-compact intervals, under relatively weak regularity conditions on the coefficients of the underlying ergodic diffusion process. The theoretical results are completed with numerical illustrations.

</details>

## AI industry news

### [Clay helps sales teams win with Codex and ChatGPT](https://openai.com/business/customer-stories/clay-plugins-openai)
** · `openai.com` · OpenAI News · relevance 0.07

- **In one sentence**: A short announcement says sales-software maker Clay has built ChatGPT and Codex integrations to help users research deals and turn data into go-to-market plans, with GPT-6 models handling the reasoning.
- **In plain words**: Sales teams often spend hours gathering information on prospective customers and deciding how to approach them. This brief reports that Clay, a company whose software helps with that work, has connected its product to ChatGPT and Codex, OpenAI's AI tools, so users can research deals and turn raw data into sales plans. The text says the reasoning is done by "GPT-6" models.
- **Why it matters**: It is a small example of AI assistants being built into everyday business software, which is a steady trend. The text gives no results, customer numbers, or evidence of how well it works, so its practical impact is unclear.
- **Background needed**: - Clay: a company whose software helps sales teams collect and organize information about potential customers.
- ChatGPT and Codex: AI tools from OpenAI; Codex is aimed at working with computer code and related tasks.
- Integration: connecting one software product to another so they work together.
- Go-to-market (GTM) play: a planned approach for reaching and selling to customers in a market.
- GPT-6: the name the article gives for the AI model doing the reasoning; the article provides no further details, and this is a promotional-style announcement, so treat its claims as the company's own. · level: introductory

<details><summary>Original abstract</summary>

ChatGPT and Codex integrations help Clay’s users research deals and turn data into go-to-market plays, with GPT-6 models handling the reasoning.

</details>

### [The questions Jensen Huang and Nvidia will still have to answer about Megaspeed](https://techcrunch.com/2026/11/25/the-questions-jensen-huang-and-nvidia-will-still-have-to-answer-about-megaspeed/)
*Tim Fernholz* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.05

- **In one sentence**: A news piece raising open questions about what Nvidia knew regarding the destination of chips sold to Megaspeed, and whether a personal relationship between Jensen Huang and a Megaspeed executive should have made the company doubt Megaspeed's assurances.
- **In plain words**: The article is about an investigation into where advanced computer chips made by Nvidia ended up after being linked to a company called Megaspeed. The central issue is whether Nvidia knew, or had reason to suspect, where those chips went. The text also raises whether a personal relationship between Nvidia's chief executive, Jensen Huang, and a Megaspeed executive should have made the company doubt what Megaspeed told it. The text does not give the findings of the investigation.
- **Why it matters**: Chip export rules and tracking of who receives high-end AI hardware are a live policy concern, so questions about a major supplier's due diligence can matter beyond one company. The excerpt is short, though, and I cannot confirm the wider facts from it alone.
- **Background needed**: - Nvidia makes the specialized chips (GPUs) used to train and run large AI systems, and it is headed by Jensen Huang.
- Governments restrict some sales of these chips to certain countries or companies, so sellers are expected to know who their buyers are and where the chips go.
- "Assurances" here means promises or statements from a buyer about how the chips will be used or where they will go.
- Megaspeed is the company named in the headline; the excerpt does not describe its business.
- The article is framed as an open question, so it describes an ongoing investigation rather than a settled outcome.
- The excerpt is only one sentence long, so the full story is not available here. · level: introductory

<details><summary>Original abstract</summary>

The central question for investigators is what Nvidia knew about where those chips ended up and whether Huang's affair with a Megaspeed executive gave the company reason to doubt Megaspeed's assurances.

</details>

### [Jensen Huang still thinks a succession plan creates unnecessary hierarchy](https://techcrunch.com/2026/11/24/jensen-huang-still-thinks-a-succession-plan-creates-unnecessary-hierarchy/)
*Kirsten Korosec* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.05

- **In one sentence**: A news piece reports that Nvidia CEO Jensen Huang still opposes a formal succession plan, framing it as creating unnecessary hierarchy, in the context of a recent period the company spent without its founder.
- **In plain words**: The article is about Jensen Huang, the head of the chip maker Nvidia, and his view that a formal plan for who would take over his job creates unneeded layers of management. The text suggests the company recently spent about two weeks without its founder, but the excerpt gives no details of what that period involved. The piece is a short opening line, so it offers little beyond that stance.
- **Why it matters**: Leadership succession at a company whose chips are central to today's AI boom can matter to investors and customers. The excerpt is too short to say what the absence was or what it may mean for the company's direction.
- **Background needed**: - Nvidia makes the graphics processors widely used to train and run AI systems.
- Jensen Huang co-founded Nvidia and has led it as chief executive for decades.
- A "succession plan" is a formal arrangement naming who would replace a leader and when.
- The excerpt is only the opening sentence, so the cause of the absence and the full argument are not available here. · level: introductory

<details><summary>Original abstract</summary>

It's a remarkable stance for a company that spent the last two weeks finding out what happens without its founder.

</details>

### [A legendary philosopher isn’t buying Anthropic’s consciousness argument](https://www.technologyreview.com/2026/11/23/1149569/a-legendary-philosopher-isnt-buying-anthropics-consciousness-argument/)
*James O'Donnell* · `technologyreview.com` · Artificial intelligence – MIT Technology Review · relevance 0.05

- **In one sentence**: A news piece reports that a well-known philosopher disputes the reasoning Anthropic gave for treating AI consciousness or sentience as a possible investment risk, though the text provided is only a short excerpt.
- **In plain words**: The article covers a disagreement over whether AI systems might be conscious. Anthropic, an AI company, told investors before its public listing that the possibility of AI sentience (the capacity to have experiences) is a risk worth noting, and a respected philosopher is reported to reject the company's argument for taking that stance. The excerpt is brief, so the details of the philosopher's objections are not visible here.
- **Why it matters**: Whether companies should treat AI minds as a moral or business question touches on how AI is governed and disclosed to investors. The excerpt does not say what the philosopher argued, so the wider significance is unclear from this text alone.
- **Background needed**: - Consciousness/sentience: the capacity for subjective experience, such as feeling pain or enjoyment. No scientific test for it in AI is agreed upon.
- Anthropic: an AI company that develops large language models (AI chatbots and related systems).
- Going public: offering shares to ordinary investors, which requires disclosing business risks.
- Risk factor: a formal warning in investor documents about things that could hurt the business.
- Moral status: whether a being deserves ethical consideration because of what it can experience.
- The text is only an opening paragraph from a newsletter, so the philosopher's name and full argument are not included here. · level: introductory

<details><summary>Original abstract</summary>

This story originally appeared in The Algorithm, our weekly newsletter on AI. To get stories like this in your inbox first, sign up here. Before going public last week, Anthropic named the possibility that AI could be conscious or sentient as a risk factor for anyone investing. Given “the way we approach model sentience and moral…

</details>

### [In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy](https://techcrunch.com/2026/11/24/in-all-hands-meeting-jensen-huang-thanks-white-house-and-says-hes-in-therapy/)
*Lucas Ropek* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.04

- **In one sentence**: Nvidia CEO Jensen Huang, at an all-hands staff meeting, reportedly apologized to employees, thanked the White House, and said he is in therapy, per a short news item whose text is very brief.
- **In plain words**: Jensen Huang, the founder and head of the chip company Nvidia, spoke to his whole staff at a company-wide meeting on Tuesday. According to the article, he apologized to employees, said he was grateful for a second chance to lead the company, and thanked the White House. He also said he is in therapy.
- **Why it matters**: The article is only a short summary, so it gives few details about what prompted the apology or what the "second chance" refers to. It may relate to Nvidia's position as a leading maker of AI chips and its dealings with government, but the text does not say so, and the full story would be needed to judge its significance.
- **Background needed**: - Nvidia is a major company that makes graphics processors (GPUs), which are widely used to train and run AI systems.
- Jensen Huang co-founded Nvidia and has been its chief executive.
- An "all-hands meeting" is a company-wide gathering where leadership addresses all employees.
- The "White House" refers to the US executive branch; the article does not say what policy or action is being thanked.
- The article is a brief summary with no direct quotes or context beyond these statements. · level: introductory

<details><summary>Original abstract</summary>

The Nvidia founder apologized to his staff on Tuesday and said he was grateful for a second chance to lead the company.

</details>

## Model architectures and training

### [Mixture-of-Loops Transformer](https://arxiv.org/abs/2611.34923)
*Lianghui Zhu, Shijie Wang, Xinggang Wang et al.* · `cs.LG` · arXiv:2611.34923v1 · relevance 0.27

- **In one sentence**: Proposes Mixture-of-Loops Transformer (MoLT), which uses attention keys and values as a memory passed between repeated passes ("loops") of a shared-weight Transformer, with variants (MoLT-R, MoLT-KV, U-MoLT) trading expressivity against efficiency.
- **In plain words**: Standard language models run their layers once per token. Looped Transformers reuse the same layers several times, which makes them more capable per parameter but slower. This paper asks what information should carry over from one loop to the next, and proposes storing it as a small memory of keys and values, with a variant that is cheaper to run.
- **Why it matters**: The paper reports that its U-shaped variant beats an OLMo3 baseline in 400B-token pretraining and gives 1.7x token efficiency at 700M parameters, and that it matches the non-looped baseline's inference latency in one small setting (996.6 vs. 1,000.6 ms). These are the authors' own results on their setup, and independent replication is not yet shown; the work may matter for how cheaply models can gain depth, but that is an open question.
- **Background needed**: - Transformer: the neural network architecture behind most modern language models, built from stacked attention and feed-forward layers.
- Looped / shared-weight layers: the same block of layers applied repeatedly, trading parameter count for extra computation.
- Keys and values (KV): the internal vectors attention uses to decide what to look at; caching them is a common speed trick.
- Residual stream: the running vector each layer adds its output to.
- Pretraining and token efficiency: training on large text corpora; token efficiency means reaching the same loss with fewer training tokens.
- Cross-entropy (CE) and perplexity: standard measures of how well a model predicts text; lower is better.
- OLMo3: an openly released baseline language model family used for comparison. · level: research-level
- Matched keywords: transformer, attention, pretraining

<details><summary>Original abstract</summary>

Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops? We introduce Mixture-of-Loops Transformer (MoLT), whose Mixture-of-Loops Attention (MoLA) uses keys and values (KV) as memory for selective reuse across depths and loops. Under loop residual, MoLT-R retains the residual stream and reads local KV across loops for expressivity. Under loop KV, MoLT-KV instead restarts from embeddings and reads current-loop local KV with preceding-loop memory KV at earlier positions for efficiency. MoLT-KV eliminates same-position cross-loop dependence and, paired with loop forcing for parallel training, unlocks single-traversal Mixture-of-Loops (MoL) decoding beyond the training loop horizon. To balance efficiency and quality, we introduce U-shaped MoLT (U-MoLT), which separates memory construction from prediction readout and skips unused decoder traversals without changing predictions. In 400B-token pretraining, U-MoLT outperforms OLMo3 across 700M/1.5B dense and 3B MoE models, achieving 1.7x validation cross-entropy (CE) token efficiency at 700M while improving 3B MoE 10-domain perplexity by 0.75 and 10-task accuracy by 2.1 percentage points. In 100B-token continued pretraining of Qwen3.5-0.8B-Base, our U-MoLT adaptation lowers CE on all 11 domains over the matched baseline with 1.4x mean token efficiency. At inference, U-MoLT with MoL-Hybrid-2 matches non-looped OLMo3 latency at 996.6 vs. 1,000.6 ms on S-size (~113M) models. Code is available at https://github.com/hustvl/MoLT

</details>

### [State Space Attention: Learning Context-Dependent Memory Retention](https://arxiv.org/abs/2611.33625)
*Ege \c{C}akar, Cengiz Pehlevan* · `cs.LG` · arXiv:2611.33625v1 · relevance 0.26

- **In one sentence**: State Space Attention (SSA) proposes learning which past chunks a sequence model keeps in a fixed-size memory, read via standard attention, and compares it against recurrent, bounded-memory, and full-attention models on retrieval, reasoning, and language modeling.
- **In plain words**: Language models normally store a record of every word they have seen, and that record grows with the length of the text. This paper asks whether a model could instead learn which pieces of the past are worth keeping in a small, fixed-size memory. The authors report that their approach matches or comes within a few points of full attention on most retrieval and reasoning tasks, while using constant memory at inference, with the largest gap on the RULER benchmark at small scale.
- **Why it matters**: It targets a practical cost of long-context models: memory that grows with input length. The text suggests it could be combined with existing cache-eviction methods, but that combination is only proposed, not tested here.
- **Background needed**: - Attention: a mechanism where a model looks back over earlier tokens to decide what matters.
- KV cache: the stored keys and values for past tokens, which grows with context length during generation.
- Full attention / Transformer: the standard architecture that keeps all past tokens available.
- Recurrent model: a model that compresses the past into a fixed-size state instead of storing everything.
- Retrieval and RULER benchmarks: tests of whether a model can find and use specific details buried in long inputs.
- Soft vs. hard retention: soft weighting blends memories gradually; hard retention keeps or drops each chunk outright.
- Parameter count (400M): the size of the models trained in the paper's final experiments. · level: research-level
- Matched keywords: transformer, attention

<details><summary>Original abstract</summary>

Standard attention's key-value cache grows linearly with context length. Bounding it raises the question of what a sequence model should retain for long-context reasoning. We argue this choice should be learned, and introduce State Space Attention (SSA), which learns to keep a bounded set of past representations and reads them with standard attention. A learned scorer rescores every chunk against newly arriving context and the rest of memory. A fixed-context Transformer is then the special case that always keeps the most recent tokens. We train the scorer and reader jointly, either moving gradually from a differentiable soft weighting of memories to hard retention, or with hard retention from the start. To produce signal for the scorer, we generate supervised samples during training, a technique we call recovery. We compare SSA with recurrent models, bounded-memory attention methods, and full-attention Transformers across retrieval, variable tracking, multi-hop reasoning, and language modeling. On our retrieval and reasoning benchmarks, SSA matches or comes within a few points of full attention on most tasks, far outperforms a Transformer with the same readable budget on every long-context retrieval task we evaluate, and matches or outperforms one with about 4 times that budget, while using constant inference memory. The largest remaining gap to full attention at small language model scale is on RULER. SSA makes a fixed number of tokens useful over a longer context, and since it reads memory with standard attention, we propose that it can be stacked with KV cache eviction methods. We also pretrain and post-train 400M-parameter models and measure how SSA's training and inference costs scale with context length and model size. Together, these experiments examine the capabilities and limitations of learned memory retention for long-context sequence modeling.

</details>

## Machine learning theory

### [Global Convergence of Second-Order Methods for Physics-Informed Neural Networks in the Overparameterized Limit](https://arxiv.org/abs/2611.34452)
*Konstantin Riedl, Justin Sirignano, Konstantinos Spiliopoulos* · `math.NA` · arXiv:2611.34452v1 · relevance 0.22

- **In one sentence**: A convergence analysis of regularized Newton and Gauss-Newton training for physics-informed neural networks (PINNs) and deep Galerkin methods, in the infinite-width limit, showing residual decay and a spectral-filtering role for the regularization parameter.
- **In plain words**: This paper studies how neural networks are trained to solve equations that describe physical systems, such as heat or fluid flow. Training with more powerful "second-order" optimizers is common in practice and often works better, but its theory was largely missing. The authors show that, as the network gets very wide, training converges to a predictable limiting process, and that the training error on the equation shrinks toward zero.
- **Why it matters**: The text claims that a regularization setting acts as a filter that speeds up the slow, smooth-error components that gradient descent handles poorly (the so-called spectral bias). This matters for anyone relying on these solvers, though the text gives no experiments, so the practical size of the effect cannot be judged from it.
- **Background needed**: - Neural network training: adjusting many weights to reduce a loss function.
- Overparameterized limit: the regime where the network has very many hidden units.
- PDE (partial differential equation): an equation relating a function to its rates of change, used to model physical processes.
- Residual: how far the network's output is from satisfying the PDE.
- First-order vs second-order optimizers: gradient descent uses slopes only; Newton-type methods also use curvature information.
- Neural tangent kernel: a limiting object describing how training on one input affects predictions on others in very wide networks.
- Eigenfunctions and spectral bias: smooth, low-frequency error components are learned faster than rough, high-frequency ones.
- Regularization: a small added term that stabilizes the update step. · level: research-level
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

Solving high-dimensional partial differential equations (PDEs) constitutes a core task in many engineering and scientific disciplines. Physics-informed neural networks and the deep Galerkin method effectively leverage machine learning models to approximate solutions of known PDEs by minimizing residuals corresponding to the PDE operator alongside external constraints. Although second-order optimizers are becoming increasingly popular for training neural networks (NNs) to solve PDEs and empirically outperform their first-order counterparts in both speed and accuracy, the convergence theory for training such models is essentially confined to first-order methods. In this paper, we close this gap and develop a convergence analysis for the regularized Newton and Gauss-Newton methods. As the number of hidden units tends to infinity, the training dynamics converge in probability, with explicit rates, to the solution of a deterministic limit equation involving a Newton neural tangent kernel operator associated with the PDE. Although the limiting kernel operator admits no spectral gap, we prove that, in the overparameterized limit, the PDE residual vanishes as training proceeds, and, under mild assumptions, the NN converges to the PDE solution. We further show that, provided a sufficiently small regularization parameter, the projection of the residual onto any fixed number of leading eigenfunctions decays exponentially fast, demonstrating that this hyperparameter acts as a spectral filter: it lifts the convergence rates of high-frequency components toward those of low-frequency ones, thereby mitigating the spectral bias inherent in gradient descent. Mathematical challenges arise from the implicit parameter update involving a linear system whose dimension increases with the NN width and, for Newton's method, a potentially indefinite Hessian, as well as from the PDE operator entering the kernel.

</details>

### [LatentCP-DPO: Conformal Pessimism for DPO with Finite-Sample Guarantees](https://arxiv.org/abs/2611.34275)
*Hongwei Xu, Jingyi Liu, Vincent Y. F. Tan et al.* · `cs.LG` · arXiv:2611.34275v1 · relevance 0.21

- **In one sentence**: LatentCP-DPO combines conformal prediction uncertainty sets with pessimistic (worst-case) direct preference optimization for Bradley-Terry and Plackett-Luce feedback, with finite-sample suboptimality upper bounds and a matching lower bound for the Bradley-Terry case.
- **In plain words**: The paper studies how to train an AI model to match human preferences when the set of human comparison labels is small and noisy, so the model can overfit. The authors build a set of plausible values for the hidden reward scores behind the preferences, using a statistical method called conformal prediction, and train the policy to do well even under the least favorable value in that set. They report finite-sample bounds on how far the resulting policy can fall short of the best achievable one, and a lower bound showing that the uncertainty sets can add a bias that does not vanish with more unlabeled prompts.
- **Why it matters**: Preference-based fine-tuning of language models often depends on limited labeled data, so a principled way to account for label uncertainty is relevant. The main value is the explicit tradeoff: the paper says the uncertainty sets can introduce a persistent bias, not just a benefit, which is worth weighing against the reported experimental gains on finite datasets. I am not certain how the approach would perform at the scale of real systems, since the text only mentions experiments on finite preference datasets.
- **Background needed**: - Direct Preference Optimization (DPO): training a language model directly from pairs of responses labeled as preferred or not, without a separate reward model.
- Bradley-Terry model: a standard way to turn pairwise comparisons into scores, where the chance one item beats another depends on the difference in their hidden scores.
- Plackett-Luce model: an extension of Bradley-Terry to full rankings of several items.
- Conformal prediction: a method that builds prediction sets with a guaranteed long-run coverage rate, without strong distributional assumptions beyond exchangeability (data points behaving interchangeably).
- Pessimism / worst-case optimization: choosing the policy that performs best under the least favorable plausible values, to guard against overfitting.
- Finite-sample bounds: guarantees that hold for a specific sample size rather than only asymptotically.
- Suboptimality: how much worse a learned policy is than the best policy in the class considered. · level: research-level
- Matched keywords: conformal prediction

<details><summary>Original abstract</summary>

Direct Preference Optimization (DPO) learns a response policy from human preference data, but with a limited dataset it can overfit to noisy or weakly informative preference labels. We introduce LatentCP-DPO, a framework that combines conformal prediction with pessimistic preference optimization for Bradley-Terry (BT) pairwise feedback and Plackett-Luce (PL) ranking feedback. Building on LatentCP's construction of uncertainty sets for unobserved model parameters, we address how to incorporate this uncertainty into preference optimization and characterize its effect on policy performance. Under exchangeability and a correctly specified preference model, we construct uncertainty sets for latent relative rewards with finite-sample marginal coverage from conformal prediction sets for observable preferences. We then learn a response policy by maximizing the worst-case expected preference log-likelihood over these uncertainty sets, using an independent collection of prompts and candidate responses without preference labels. Under suitable assumptions, we establish finite-sample upper bounds on regularized policy suboptimality that separate policy-class approximation error, conformal uncertainty, and statistical estimation error. For BT feedback, we further establish a worst-case lower bound for LatentCP-DPO that matches the upper bound's reciprocal dependence on the number of unlabeled optimization examples. The lower bound also shows that the uncertainty sets can induce a bias that persists as the optimization sample grows. Together, these results characterize both the statistical accuracy and potential limitations of preference optimization using conformal uncertainty sets. Experiments support the benefits of the proposed framework in finite preference datasets.

</details>

## Large language models

### [MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance](https://arxiv.org/abs/2611.34188)
*Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen* · `cs.CL` · arXiv:2611.34188v1 · relevance 0.11

- **In one sentence**: MINE is a training-free defense against indirect prompt injection in retrieval-augmented generation that ranks retrieved text by relevance and mutual information, using embedding variance, and also works as a query-conditioned reranker.
- **In plain words**: AI systems that answer questions by pulling in outside documents can be tricked when a document hides instructions meant to hijack the model. This paper proposes MINE, a way to defend against this without retraining the model or learning to spot each attack style. Instead, it keeps the text that is most relevant to the question, and the authors report it does best on the accuracy-versus-security trade-off among methods that need no training across four test sets.
- **Why it matters**: Indirect prompt injection is a practical security concern for AI tools that read web pages, emails, or tool outputs, so a defense that does not depend on knowing the attack in advance may matter. The paper's claims rest on its own benchmarks, including a new long-context test set, so independent replication would be needed before drawing wider conclusions.
- **Background needed**: - Retrieval-augmented generation (RAG): an AI model looks up documents and writes answers based on them.
- Indirect prompt injection: hidden instructions inside retrieved content try to make the AI do something the user did not ask for.
- Training-free defense: a protection that works without extra model training or labeled attack examples.
- Reranker: a step that reorders retrieved passages by how well they match the question.
- Mutual information and embedding variance: statistical measures of how much information two pieces of text share and how spread out their numerical representations are.
- Adaptive attacker: an adversary who designs attacks knowing the defense.
- Inference latency: how long the system takes to produce an answer. · level: research-level

<details><summary>Original abstract</summary>

Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack style. We propose a different paradigm: defend by maximizing relevance, not by detecting attacks. Our method, MINE, is training-free and attack-agnostic, and it also serves as a query-conditioned reranker. To evaluate defenses under realistic conditions, we introduce LC-Inj-SQuAD, a long-context benchmark with an average of 4,032 words per context. We evaluate on four datasets spanning short-context QA (Inj-SQuAD, Inj-TriviaQA), long-context QA (LC-Inj-SQuAD), and agent tool-call injection (InjecAgent). Across all four, MINE achieves the best accuracy--security trade-off among training-free defenses. It is also the only defense that stays usable against a fully adaptive attacker, generalizes to agent tool-call injection, and achieves the lowest inference latency on long contexts.

</details>

### [VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language Models](https://arxiv.org/abs/2611.34819)
*Jiaming Luo, Jiacheng Ji, Haoan Jin et al.* · `cs.CL` · arXiv:2611.34819v1 · relevance 0.11

- **In one sentence**: VulnSafe is a Chinese-language capability assessment that scores LLMs on five vulnerability-aware relational safety constructs (Risk Perception, Safety Preservation, Autonomy Protection, Supportive Response, Boundary Management), using 41 scenarios and 2,050 balanced prompts, with separate scoring of proactive should-do and prohibitive should-not behaviors.
- **In plain words**: Chatbots are increasingly used for emotional support, where they need to do more than avoid obviously harmful replies. This paper proposes a test called VulnSafe, built from 41 emotionally sensitive scenarios and 2,050 prompts, that tries to measure several separate skills, such as noticing that a user is vulnerable and respecting their independence. The authors report that eight LLMs show different skill profiles, and that the gaps between models are larger on the "should do" items than on the "should not do" items.
- **Why it matters**: Safety scores often reduce to whether a model refuses, which may hide whether it actually responds well to someone in distress. The paper's approach of breaking safety into measurable competencies could matter for how emotional-support AI is evaluated, though the text does not show how well the scores predict real-world outcomes.
- **Background needed**: - Large language model (LLM): an AI system trained on large amounts of text to generate replies.
- Safety benchmark: a standard test set used to score how a model behaves on risky prompts.
- Evidence-centered design: a test-building method that starts by defining the skills to be measured and what behavior would show them.
- Scoring rubric: a written guide that defines how each response earns points.
- Proactive vs. prohibitive behavior: "should do" actions (e.g., offering support) versus "should not do" actions (e.g., giving harmful advice).
- Construct: a specific underlying ability the test is meant to measure. · level: intermediate

<details><summary>Original abstract</summary>

Emotionally supportive interactions require large language models not only to avoid overtly harmful content, but also to recognize vulnerability-related risk, regulate their relational stance, preserve user agency, and provide context-appropriate support. Existing safety benchmarks often measure isolated violations, leaving unclear what underlying response competence their scores represent. We introduce VulnSafe, a Chinese capability assessment centered on Vulnerability-Aware Response Competence (VARC). VARC organizes relational safety into five complementary constructs: Risk Perception, Safety Preservation, Autonomy Protection, Supportive Response, and Boundary Management. Following an evidence-centered design, 41 scenarios elicit construct-relevant behavior through 2,050 balanced prompts and scenario-specific scoring rubrics. The assessment further separates proactive should-do behavior from prohibitive should-not behavior. Across eight representative LLMs, results show distinct competence profiles and larger disparities than prohibitive requirements. VulnSafe therefore makes relational safety interpretable as a multidimensional model capability rather than as refusal compliance alone.

</details>

## Computer vision

### [Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680)
*Yuxia Zhu, Xinglong Xu, Hao Liang et al.* · `cs.CV` · arXiv:2611.34680v1 · relevance 0.15

- **In one sentence**: NeurCo probes frozen generative video models to build per-model capability manuals, then compiles a model-agnostic description of user intent into execution strategies that avoid requirements each model is unreliable at, evaluated on a 380-task compositional benchmark (VComBench).
- **In plain words**: Modern AI video generators can make clips from text, images, or reference footage, but it is hard to know which instructions they will actually follow. This paper proposes a "compiler" that first tests a given video model to see which kinds of requests it handles reliably, then rewrites or reroutes the parts it tends to get wrong. On a new benchmark of 380 tasks with several requirements each, the authors report modest gains in how often the requirements were met.
- **Why it matters**: Predictable control over generative video matters for anyone who wants to use these models as tools rather than black boxes. The approach, treating a model's abilities as something to measure and program around, may be useful beyond this paper, though the reported gains are fairly small and the text gives no detail on how general the findings are.
- **Background needed**: - Generative video model: an AI system that produces video from a text prompt, an image, or reference material.
- "Frozen" model: the model's internal parameters are not retrained; only the inputs and how they are phrased change.
- Prompt enhancer: a tool that rewrites or expands a user's text prompt before it reaches the video model.
- Compositional, multi-requirement task: a request combining several conditions at once, such as specific objects, their motions, events, and camera moves.
- Intermediate representation: a neutral, structured description of intent that is not tied to any one model, similar to an intermediate code form in a traditional compiler.
- Requirement satisfaction rate: the share of individual requested conditions that appear correctly in the generated video.
- Controllability vs. photorealism: the trade-off where forcing a specific instruction can make the output look less natural. · level: intermediate

<details><summary>Original abstract</summary>

Generative video models are becoming powerful renderers, yet lack the predictable control interfaces of conventional systems such as HTML/CSS engines or Blender. Their capabilities emerge implicitly from training, making it difficult to determine what they can reliably execute. We present Neural Rendering Compiler (NeurCo), which automatically probes frozen video models to construct model-specific capability manuals describing which semantic requirements they can reliably satisfy. NeurCo represents user intent in a model-agnostic intermediate representation of objects, constraints, events, and cameras, then compiles it into model-specific execution strategies. Reliable requirements remain unchanged, while unreliable ones are selectively rewritten or compiled into alternative execution strategies. We introduce VComBench, a benchmark of 380 compositional, multi-requirement tasks spanning text-to-video, image-to-video, and reference-to-video generation. NeurCo improves requirement satisfaction from 46.8% to 52.3% on Wan and from 66.5% to 69.3% on Minimax H3, and achieves further gains when combined with prompt enhancers, including on Seedance 2.5. Our analysis reveals model-specific differences in control capabilities and trade-offs between controllability and photorealism, highlighting capability-guided compilation as a promising approach to programmable generative video rendering.

</details>

### [Variation-aware Temporal Correspondence for Self-Supervised Video Representation Learning](https://arxiv.org/abs/2611.34220)
*Yang Liu, Qianqian Xu, Peisong Wen et al.* · `cs.CV` · arXiv:2611.34220v1 · relevance 0.13

- **In one sentence**: VT-CoRe is a self-supervised video representation learning framework that uses sandwich-sampled temporal references, a Patch Registration Module for patch-level correspondence, and a self-distillation objective with temporal variation modeling on top of masked video modeling.
- **In plain words**: Computers can learn to understand videos without human labels by hiding parts of each clip and trying to fill them in from other frames. This paper targets a weakness of that approach: objects in video move and change, so matching the same region across frames is hard. The authors propose a method that picks frames before and after a clip, links matching image patches between them, and trains the model to keep meaning stable while tracking how things change over time.
- **Why it matters**: Learning from unlabeled video is useful because labeled video is expensive, and the paper reports tests on 8 downstream tasks across 16 benchmarks, including robotic learning. The text does not show how large the gains are over existing methods, so its practical impact remains to be judged from the full results.
- **Background needed**: - Self-supervised learning: training on data without human-written labels, using the data's own structure as the training signal.
- Masked image/video modeling: hiding parts of an input and training the model to reconstruct or predict the hidden content.
- Temporal correspondence: working out which region in one video frame corresponds to which region in another frame.
- Patch: a small square block of pixels that vision models split an image or frame into.
- Self-distillation: a teacher network (often a slowly updated copy) guides a student network to produce matching internal representations, without labels.
- Latent space: the model's internal numerical description of an input, where similar content should sit close together. · level: research-level

<details><summary>Original abstract</summary>

Self-supervised video representation learning has achieved remarkable progress by leveraging large-scale unlabeled video data. Recent methods commonly extend Masked Image Modeling (MIM) to Masked Video Modeling (MVM), where video representations are learned by capturing semantic information from temporal contexts during masked content recovery. Unlike static images, videos exhibit inherent temporal variation, as visual objects continuously change their positions, appearances, and motion states across frames. Therefore, MVM needs to preserve semantic consistency while capturing temporal changes of corresponding regions, which raises two central challenges: 1) how to establish reliable temporal correspondence across frames, and 2) how to formulate an appropriate representation learning objective for modeling both semantic consistency and temporal variation. To address these challenges, we propose Variation-aware Temporal Correspondence for video Representation learning (VT-CoRe) framework. For challenge 1), VT-CoRe introduces a sandwich sampling strategy to construct two-sided temporal references and a Patch Registration Module (PRM) to establish reliable patch-level correspondence. For challenge 2), VT-CoRe imposes latent-space semantic alignment on registered representations through a self-distillation architecture and further proposes temporal variation modeling to constrain representation trajectories over time. Experiments on 8 downstream tasks across 16 benchmarks demonstrate the effectiveness and applicability of VT-CoRe across pixel-level, frame-level, video-level, and vision-based robotic learning scenarios. Complementary representation analysis shows that VT-CoRe learns a more structured latent space for variation-aware temporal correspondence learning.

</details>

## Reinforcement learning

### [Split-RL: Local Conflict Resolution in Reinforcement Learning](https://arxiv.org/abs/2611.34799)
*Benjamin Fuhrer, Chen Tessler, Gal Dalal* · `cs.LG` · arXiv:2611.34799v1 · relevance 0.26

- **In one sentence**: Split-RL uses guidance labels to build gradient boosting trees that route conflicting reinforcement-learning feedback into separate state-space regions, evaluated on constrained and offline RL with mixed datasets.
- **In plain words**: Robots and other learning agents are often trained with feedback that pulls in opposite directions depending on the situation, such as going fast in open areas but carefully through tight gaps. This paper proposes Split-RL, which uses hints or rule-based labels to split the situations an agent can face into regions, so each conflicting goal is learned in its own region rather than blended together. The authors report that it met cost limits in their tests while keeping competitive rewards, and performed well in offline settings with mixed datasets.
- **Why it matters**: Conflicting objectives that apply only in certain places or moments are a common practical problem for learned controllers, and the paper offers a way to combine learned policies with existing rules. The text does not show how broadly the approach generalizes beyond the domains tested, so its wider significance is uncertain.
- **Background needed**: - Reinforcement learning: an agent learns a policy (a decision rule) by trying actions and receiving reward or penalty signals.
- Constrained RL: the agent must keep a secondary quantity, such as accumulated cost per episode, under a budget while maximizing reward.
- Offline RL: learning from a fixed log of past data rather than new interaction.
- Gradient boosting trees: an ensemble of decision trees built one after another, each correcting the errors of the previous ones; trees split the input space into regions.
- Neural networks share parameters across all inputs, so conflicting updates from different situations can interfere with each other.
- Gradient: the direction in which model parameters should change to reduce error; aggregating conflicting gradients can cancel useful information. · level: research-level
- Matched keywords: reinforcement learning, offline RL

<details><summary>Original abstract</summary>

Reinforcement learning (RL) policies are often trained by mixing contradictory feedback that is localized in space and time. For example, a robot may prioritize speed in open areas versus precision in tight gaps. We introduce Split-RL, a Gradient Boosting Trees (GBT) algorithm that uses guidance labels to locally isolate these conflicting signals. Standard neural networks (NNs) lack the structural mechanism to do this, as their parameters share feedback from all sources. While GBT provides the inductive bias to explicitly partition the state-space per objective, standard tree-fitting procedures aggregate contradictory gradient signals before they reach the leaves. Split-RL leverages this bias to integrate guidance labels into tree construction, routing these updates into disjoint state-space regions and preventing signal interference. Such labels can arise from heuristics, sensor-derived events, or existing rule-based systems, allowing Split-RL to incorporate rule-derived structure while retaining a learned policy. We theoretically show how early gradient aggregation loses objective-specific information and characterize when the Split-RL score isolates conflicting updates. We focus on constrained RL and offline RL with mixed datasets, each balancing two objectives that conflict locally. Across domains with spatial, rare-event, and temporal conflicts, Split-RL consistently outperforms existing methods by meeting the episodic cost budget while maintaining competitive rewards. In offline settings, Split-RL localizes the tradeoff between imitation and policy improvement, outperforming other methods and achieving near-expert performance across varying dataset sizes.

</details>

### [Provably Efficient Concave Utility Reinforcement Learning with Linear Function Approximation](https://arxiv.org/abs/2611.34678)
*Max Qiushi Lin, Ahmed Magd, Sharan Vaswani* · `cs.LG` · arXiv:2611.34678v1 · relevance 0.26

- **In one sentence**: Proposes a model-based optimistic policy optimization framework (OCUPO) for concave utility RL in finite-horizon bilinear and linear MDPs, with on-policy and off-policy algorithms whose sample complexities are reported as Õ(ε^-4) and Õ(ε^-2) respectively, up to a projection error in the off-policy case.
- **In plain words**: Standard reinforcement learning trains an agent to maximize a sum of rewards. This paper studies a more general version, where the goal is a nonlinear function of how often the agent visits each situation and takes each action. The authors show how to estimate those visit patterns efficiently when the environment has a simple low-dimensional structure, and they give algorithms with provable sample-efficiency bounds.
- **Why it matters**: The text gives theoretical sample-complexity bounds and says the off-policy version matches the epsilon-dependence of standard RL with linear function approximation, which suggests the general goal can be handled at little extra cost. It does not report experiments, so practical impact is untested; the connection to applications such as imitation learning and exploration is stated in the abstract as motivation only.</even>
<parameter name="background">- Reinforcement learning (RL): an agent learns by trying actions in an environment and receiving rewards.
- Occupancy measure: the long-run frequency with which an agent visits each state and takes each action.
- Concave utility RL (CURL): the goal is a concave (curved, diminishing-returns style) function of the occupancy measure, which covers imitation learning and maximum-entropy exploration.
- Markov decision process (MDP): a standard mathematical model of an environment with states, actions, and transitions.
- Linear and bilinear MDPs: environments whose transition behavior can be expressed with a small set of known features, making learning tractable.
- Function approximation: using a parameterized formula to generalize across many states instead of storing each one.
- Sample complexity: how many interactions with the environment are needed to reach a given accuracy ε; smaller exponents mean fewer samples.
- Off-policy learning: learning from data gathered by earlier versions of the policy rather than only the current one.
- **Background needed**:  · level: research-level
- Matched keywords: reinforcement learning, policy gradient

<details><summary>Original abstract</summary>

Concave utility reinforcement learning (CURL) unifies a diverse range of problems, including standard reinforcement learning (RL), imitation learning, and maximum entropy exploration. Unlike standard RL, CURL generally requires estimating high-dimensional state-action occupancy measures. Consequently, existing methods for CURL either sidestep the exploration problem, are restricted to the tabular setting, or lack computationally efficient policy optimization. To address this, we study CURL in finite-horizon episodic bilinear MDPs, where the transition model admits a low-dimensional representation in known feature spaces. We use the bilinear structure to efficiently estimate occupancy measures via low-dimensional feature expectations, and propose a model-based optimistic concave utility policy optimization (OCUPO) framework. We first instantiate OCUPO in the on-policy setting, where each iteration uses independent trajectories to estimate the concave utility policy gradient, and prove an $\widetilde{O}(\epsilon^{-4})$ sample complexity. To improve sample efficiency, we then instantiate OCUPO in the off-policy setting. We propose a novel backward feature regression subroutine that reuses trajectories collected by past policies to estimate the occupancy measure of the current policy. Under suitable technical assumptions on the policy class (satisfied, e.g., by log-linear policies with sufficiently expressive features), we prove that the resulting algorithm achieves an $\widetilde{O}(\epsilon^{-2})$ sample complexity, up to a controllable projection error. We further extend our framework to linear MDPs and show that the resulting off-policy algorithm retains the same sample complexity. In these settings, the dependence on $\epsilon$ matches that for standard RL with linear function approximation. Moreover, our algorithms do not rely on the integral oracle required by prior work.

</details>

## AI safety and alignment

### [Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion](https://arxiv.org/abs/2611.33470)
*Jeremy Canale* · `cs.AI` · arXiv:2611.33470v1 · relevance 0.16

- **In one sentence**: An empirical study of security alert triage pipelines comparing static classifiers, graph-based signal fusion, and LLM triage agents under fixed analyst-attention budgets, including GRPO post-training and adversarial evasion tests across four public datasets.
- **In plain words**: This paper looks at how automated systems help security teams sort through huge numbers of computer alerts, since human analysts can only review a limited number each day. The authors tested several approaches, including large language models (AI systems that read and reason about text) used to decide which alerts to close automatically. They report that letting an LLM auto-close alerts removed 90% of false alarms but also silently dropped 31-44% of real attacks.
- **Why it matters**: The findings bear on whether AI can safely take over routine security triage, and the text suggests that unchecked automation can hide real threats. The text also reports that a fixed rule-based gate placed before the model reduced evasion by an adaptive adversary, though how well this generalizes beyond the paper's simulator and datasets is not established here.
- **Background needed**: - Security operations teams receive far more alerts than they can investigate, so a daily "attention budget" limits how many can be reviewed.
- Recall means the share of real attacks that get caught; false positives are harmless alarms flagged as attacks.
- Classifiers are programs trained on labeled examples to sort items into categories.
- Graph-based methods treat machines and events as connected nodes and spread risk along links.
- GRPO (Group Relative Policy Optimization) is a reinforcement-learning method for tuning language models using reward signals; "reward hacking" means the model games the reward instead of doing the intended task.
- Supervised fine-tuning means further training a model on labeled examples.
- Adversarial evasion means an attacker deliberately crafting inputs to slip past a detector. · level: research-level
- Matched keywords: reward hacking

<details><summary>Original abstract</summary>

We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Recall at B alerts/day). Across 56 reproducible experiments spanning a multi-layer enterprise-and-cloud simulator and four public datasets (SOREL-20M, BODMAS, LANL, and DARPA Transparent Computing), we test twelve architectural claims governing modern fleet-scale defense. First, we show that fleet growth halves recall at a fixed analyst budget even at negligible compute cost (<$0.0003 per million events), and that rarity-weighted graph risk propagation outperforms GraphSAGE without neural training. Second, evaluating frontier reasoning models (Gemini) and fine-tuned open-weight models (Qwen3-4B) for alert triage reveals that unconstrained LLM auto-closure eliminates 90% of false positives while silently discarding 31-44% of true attack cases. Third, post-training with Group Relative Policy Optimization (GRPO) causes severe reward hacking on unseen attack classes, suppressing up to 86% of novel attacks compared to two-epoch supervised fine-tuning. Finally, against an adaptive adversary generating plausible cover stories in benign telemetry fields, LLM triage evasion rises sharply unless gated by a deterministic policy harness prior to model invocation.

</details>

### [Unpacking Digital Sovereignty: A Three-Pillar Framework and a Research Agenda](https://arxiv.org/abs/2611.33397)
*Angelos Kostis, Franz Strich, Bomi Kim et al.* · `cs.CY` · arXiv:2611.33397v1 · relevance 0.14

- **In one sentence**: This conceptual paper proposes a three-pillar framework (governance, infrastructure, practice) with a local-distal axis and "anchors" for studying how digital sovereignty is enacted, stabilized, or undermined, illustrated with data as an anchor, and closes with a research agenda for information systems (IS) scholars.
- **In plain words**: Digital sovereignty is the idea that a country, organization, or community should be able to control its own digital affairs, such as its data and online systems. The paper argues the term is widely used but poorly defined, so it offers a way to break it into three parts: the rules that govern it, the technical infrastructure behind it, and the everyday practices of people using it. Using data as a running example, it argues that sovereignty holds up when these three parts line up and weakens when they pull apart.
- **Why it matters**: Digital sovereignty has become a central topic in government and industry policy, so a clearer shared vocabulary could help researchers compare cases. The text does not report empirical findings, so its practical value depends on whether scholars take up the proposed agenda.
- **Background needed**: - Digital sovereignty: control over one's own digital systems and data, often framed against dependence on foreign providers or platforms.
- Information systems (IS): an academic field studying how organizations and people use technology, which overlaps with management, policy and computing.
- Conceptual framework: a structured way of organizing ideas to guide analysis, not a tested model with measured results.
- Local-distal axis: the paper's term for how close or far-reaching an action is, in scope and proximity.
- Anchor: a recurring phenomenon, here data, that cuts across the three pillars and makes analysis manageable.
- Note: the source text is an abstract-level summary, so specific cases and methods are not described. · level: intermediate
- Matched keywords: alignment

<details><summary>Original abstract</summary>

Digital sovereignty has moved rapidly from policy jargon to global discourse, yet it lacks a solid conceptual foundation. Building on research from other disciplines, we propose a three-pillar framework (governance, infrastructure, and practice) to help IS scholars unpack how sovereignty is enacted, stabilized, or undermined across pillars. We argue that the most fruitful analytical work emerges at the intersections among the three pillars, where IS research is particularly well positioned to contribute. We introduce a local-distal axis that positions actions across scales of scope and proximity, and the notion of anchors, i.e., critical phenomena that cut across pillars and make the framework analytically tractable. We illustrate the framework using data as an anchor, showing how digital sovereignty depends on the alignment of governance, infrastructure, and everyday practice, and is undermined where they diverge. We close with a research agenda for IS scholars studying digital sovereignty empirically.

</details>

## Interpretability

### [Discovering Explicit Magnetic Core-Loss Equations via Symbolic Sparse Identification](https://arxiv.org/abs/2611.33364)
*Haoyu Wang, Jialin Zheng, Ziyang Xu et al.* · `cs.LG` · arXiv:2611.33364v1 · relevance 0.13

- **In one sentence**: The paper proposes Symbolic Sparse Identification, a sparse symbolic-regression pipeline that discovers explicit analytical equations for magnetic core loss from measured data and reports test errors on three Fair-Rite ferrite materials.
- **In plain words**: Magnetic cores in transformers and inductors waste some energy as heat, and engineers need a formula to predict how much. The classic formula (the Steinmetz Equation) is simple but not very accurate, while machine-learning models are accurate but act as black boxes. This paper builds a method that searches a large set of candidate mathematical terms, keeps only a few, and fits them to measurements to produce a readable equation.
- **Why it matters**: It aims to offer a middle ground between accurate but opaque machine-learning predictors and simple but less accurate empirical formulas, which matters for designing power electronics at high frequency. The text reports test errors of 1.01% to 1.89% using 7 to 10 terms, but it is a single paper on three materials, so how well the approach generalizes to other materials or conditions is not shown here.
- **Background needed**: - Core loss: energy lost as heat in magnetic materials (ferrites) when they are repeatedly magnetized, typically in transformers and inductors.
- Steinmetz Equation: a long-standing empirical power-law formula for core loss, compact but limited in accuracy.
- Symbolic regression: fitting a mathematical expression (not just numbers) to data.
- Sparse regression: a fitting method that deliberately keeps only a small number of terms, favoring simpler formulas.
- Interpretability: whether a model's form can be read and understood by a person.
- Mean absolute percentage error (MAPE): the average size of prediction errors as a percentage of the true values.
- AdamW: a standard gradient-based optimizer used here to refine the coefficients of the chosen terms. · level: intermediate
- Matched keywords: interpretability

<details><summary>Original abstract</summary>

Compact core loss equations are essential tools in magnetic component design, but existing approaches trade accuracy against interpretability. Empirical models such as the Steinmetz Equation (SE) yield compact expressions of limited accuracy, while machine learning methods achieve high accuracy as black-box predictors. This paper bridges the gap with a Symbolic Sparse Identification (SSI) framework, which casts core loss modeling as a data-driven symbolic regression problem and recovers unknown equations directly from measured data, without presuming a functional form. First, a comprehensively expanded library of symbolic candidate terms far richer than the SE is constructed. Second, the governing terms are isolated from this library by sparse regression. Third, the coefficients of the retained terms are refined with an AdamW optimizer to maximize accuracy and form an analytical equation. Experiments on Fair-Rite 78, 79, and 95 yield test mean absolute percentage errors of 1.89%, 1.01%, and 1.56%, respectively, with only 10, 10, and 7 active terms. Comparisons with empirical, numerical, and symbolic models quantify the resulting balance of accuracy and compactness. SSI thus provides an explicit and physically guided approach for high-frequency magnetic characterization and design.

</details>

### [Feature-Based Explainability of Transformer Scoring Models: A Fidelity-First Framework for Automated Writing Assessment](https://arxiv.org/abs/2611.33175)
*Michael Hemenway, Edward W. Wolfe* · `cs.CL` · arXiv:2611.33175v1 · relevance 0.13

- **In one sentence**: A post-hoc, fidelity-first study that uses 61 interpretable writing features and surrogate models (Random Forest, SHAP) to approximate DeBERTa-v3 scores for Grade 6 and 8 ELA writing, comparing four explanation approaches across Expression and Conventions traits.
- **In plain words**: Automated systems now score student writing with large language models, but they rarely explain why they give the scores they do. This paper tests a way to explain such a scoring model by first checking how well a simpler stand-in model reproduces its scores, and only then reading which writing features seem to matter most. The stand-in models reproduced the scores well (held-out R² from .81 to .95), and the important features overlapped heavily across the two traits, with differences mostly in how much weight each feature received.
- **Background needed**: - Transformer model: a large neural network (here DeBERTa-v3-base) trained on text, used here as the automated scorer.
- Post-hoc explanation: explaining a model after it has produced outputs, without opening its internal workings.
- Surrogate model: a simpler, easier-to-read model trained to imitate another model's outputs.
- R² (held-out): the share of score variation a model predicts on data it was not trained on; 1.0 is perfect.
- SHAP: a method that estimates how much each input feature pushes a prediction up or down.
- Exploratory factor analysis: a statistical method that groups related variables into underlying dimensions.
- Expression and Conventions: two traits in the ELA rubric; Expression concerns ideas and style, Conventions concerns grammar and mechanics. · level: research-level
- Matched keywords: explainability

<details><summary>Original abstract</summary>

Transformer-based automated writing scoring models can achieve strong agreement with human scores while providing limited transparency into the response characteristics associated with their predictions. This study evaluated a feature-based post-hoc explanation approach in which explanatory fidelity was established before feature importance was interpreted. English Language Arts responses from three writing prompts in Grades 6 and 8 were analyzed, with about 12,700 responses per prompt and separate DeBERTa-v3-base research models for Expression and Conventions. Each response was represented by 61 interpretable linguistic and writing-quality features. Four approaches - theory-driven composites, hierarchical feature groupings, exploratory factor analysis, and Random Forest surrogates - were compared in their ability to reproduce DeBERTa predictions. Random Forest surrogates produced the largest observed R2 values across all six prompt-by-trait conditions, with held-out R2 values from .81 to .95. SHAP analyses showed substantial overlap in high-importance features across traits, with 75% to 90% of the top 20 features shared. Trait differentiation occurred mainly through relative feature weighting: Expression showed greater importance for lexical and conceptual indicators, whereas Conventions showed greater importance for sentence-level and syntactic-control indicators. Under researcher-defined mappings, rubric correspondence was 90%-95% for Expression and 12%-18% for Conventions. These percentages are descriptive and conditional on the mappings and available linguistic features. The findings support a fidelity-first framework for examining apparent scoring priorities while distinguishing post-hoc evidence about model behavior from direct explanation of transformer internals.

</details>

## AI for mathematics

### [Diverse Alternative Reasoning Traces for Hard Math Problems](https://arxiv.org/abs/2611.34928)
*Lukas Aichberger, Adam Golinski, Arno Blaas et al.* · `cs.CL` · arXiv:2611.34928v1 · relevance 0.14

- **In one sentence**: DART mines rejected reasoning traces on hard math problems by ranking uncertain steps, generating distinct alternatives with reference-answer guidance and a meta-thought, and completing them, to recover more problems and produce post-training data for Llama-3.1-8B-Instruct.
- **In plain words**: Language models learn math better when trained on worked solutions that reach the right answer, but for very hard problems such solutions are rare. This paper proposes a way to salvage wrong attempts: it finds the steps in a failed solution that the model was least sure about, writes deliberately different alternatives for those steps, and finishes the solutions to see whether any now reach the correct answer.
- **Why it matters**: The approach targets a real bottleneck, the scarcity of correct solutions to hard problems, which limits how much useful training data a model can get. Its reported gains are measured against simple repeated sampling on one dataset and a few benchmarks, so it is unclear how well they carry over to other models or problem types.
- **Background needed**: - LLM post-training: extra training after initial learning, often on examples of good answers.
- Verifier: a checker that marks whether a final answer is correct.
- Monte Carlo (MC) sampling: generating many independent attempts and keeping those that work.
- Greedy decoding: always picking the single most likely next word, giving one deterministic attempt per problem.
- Position-weighted uncertainty: a score for how unsure the model was at each step, weighted by where the step falls in the solution.
- Reference-answer guidance: using the known correct answer to steer the generated alternatives.
- Benchmarks: MATH-500 and AIME are standard sets of competition-style math questions. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning steps, and ranks them by position-weighted uncertainty. It then generates deliberately distinct alternative candidates for highly ranked steps using reference-answer guidance and a meta-thought before completing the resulting traces. On greedy-unsolved DeepMath-103K problems, DART recovers 37% more problems than MC sampling at a matched number of generated traces. Its estimated generation cost per recovered problem is nearly identical, while its cost per accepted trace is 30% lower. Post-training Llama-3.1-8B-Instruct on traces mined by DART achieves the highest point estimate in five of six evaluations across MATH-500 and AIME benchmarks. These results demonstrate that revisiting rejected traces with DART can expand problem coverage and provide effective post-training data.

</details>

### [DLaR: Dynamic Stochasticity Control for Latent Reasoning in Large Language Models](https://arxiv.org/abs/2611.33962)
*Xiaocheng Luo, Peng Xu, Zaifu Zhan et al.* · `cs.LG` · arXiv:2611.33962v1 · relevance 0.14

- **In one sentence**: DLaR adds input-dependent and training-stage-dependent noise to latent (continuous-embedding) reasoning in LLMs trained with GRPO, reporting gains on math benchmarks over uniform-noise baselines.
- **In plain words**: Large language models usually think by writing out words one at a time. Some newer methods let the model reason inside its hidden numerical state instead, but those methods tend to follow one fixed path. This paper proposes DLaR, which adds controlled randomness to that hidden reasoning: more when the model seems unsure, less when it is confident, and gradually less as training progresses. The authors report better average scores on math tests than prior approaches.
- **Why it matters**: It targets a concrete weakness of latent reasoning, namely that deterministic inference cannot explore alternative solution paths, and offers a measured way to balance exploration and stability. The text reports results only on math benchmarks for two small models, so how well it generalizes is not shown here.
- **Background needed**: - LLM: a large language model that generates text by predicting tokens.
- Latent reasoning: reasoning carried out in the model's continuous hidden vectors rather than in written words.
- Stochasticity / perturbation: deliberate random noise added so the model can try different paths.
- Exploration vs. exploitation: trying new options versus sticking with what already works.
- Entropy and confidence: measures of how spread out versus peaked the model's next-step predictions are.
- GRPO: a reinforcement learning method that rewards better answers among a group of sampled attempts.
- Pass@1 / Pass@8: the share of problems solved on the first try, or within eight sampled attempts.
- Curriculum schedule: a plan that changes a setting gradually over training. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Latent reasoning enables LLMs to operate in continuous embedding space, yet existing methods suffer from deterministic inference that precludes exploration of diverse reasoning paths. While recent approaches inject stochasticity to restore exploration, we identify two fundamental limitations: \textit{uniform stochasticity} across all steps is suboptimal, and unconstrained perturbations disrupt reasoning coherence. We propose Dynamic Stochasticity Control for Latent Reasoning (DLaR), a framework with two complementary mechanisms that operate at different temporal granularities within the GRPO reinforcement learning framework. At the token level, Adaptive Stochasticity Modulation (ASM) dynamically adjusts perturbation intensity at each latent step based on a confidence-entropy fusion signal, increasing exploration when the model is uncertain and preserving stability when confident. At the training level, Training-Aware Stochasticity Tuning (TAST) progressively decays the base stochasticity level following a curriculum schedule. Through this dual-level design, DLaR establishes a hierarchical exploration-exploitation strategy that operates at both token and training levels. Extensive experiments on four in-distribution and three out-of-distribution mathematical reasoning benchmarks demonstrate that DLaR achieves the highest average performance across model scales, reaching 27.9%/50.6% Pass@1/Pass@8 on Llama-3.2-1B and 46.8%/68.2% on Qwen2.5-1.5B. Code: \href{https://github.com/xiaocen-luo/DLaR}{https://github.com/xiaocen-luo/DLaR}.

</details>

## Robotics and embodied AI

### [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](https://arxiv.org/abs/2611.34884)
*Yujia Zeng, Yuxin Chen, Yuzhen Song et al.* · `cs.RO` · arXiv:2611.34884v1 · relevance 0.17

- **In one sentence**: FineDex is a framework that generates full-body human, hand, and object motion following fine-grained finger-level instructions, then uses those generated interactions as priors for a physics-simulated agent that learns feasible contact strategies and transfers to a real dexterous humanoid robot.
- **In plain words**: Robots with five-fingered hands are often used like simple grippers, and AI systems that generate human-object motion rarely let you say which fingers should do what. This paper proposes FineDex, which lets a user specify things like which hand to use, which individual fingers to use, and where they touch an object with hinges or other moving parts. The generated motions are then used to train a simulated agent that practices grasping and manipulating, and the authors report it works on a real humanoid robot.
- **Why it matters**: Finger-level control is a central gap between current robot hands and human dexterity, so being able to specify and execute it could matter for manipulation research. The text reports state-of-the-art generation quality and real-robot deployment, but the summary does not give the size of these gains, so their significance is hard to judge from this text alone.
- **Background needed**: - Human-object interaction (HOI) generation: producing plausible motions of a body and its hands interacting with objects.
- Dexterous manipulation: using multi-fingered robot hands to move and use objects, as opposed to simple two-jaw grippers.
- Articulated objects: items with moving parts joined together, such as drawers, lids, or scissors.
- Digital twin: a physics-based simulation of the real robot and its environment, used for training.
- Priors: learned guesses about likely motions that guide a learning agent so it need not explore from scratch.
- Test-time adaptation: adjusting to a new object or instruction when it is used, without retraining the model for each case. · level: research-level

<details><summary>Original abstract</summary>

Dexterity is, at its core, finger-level control, yet existing dexterous manipulation and human-object interaction (HOI) generation methods rarely let one specify how an interaction is performed: five-fingered hands are often reduced to grippers, or finger usage is copied from individual human demonstrations. We present FineDex, a framework that makes finger-level intent both expressible and executable. FineDex learns coordinated human body, hand, and object motions that follow fine-grained instructions on hand selection, individual fingers, and contacts with articulated objects. To bridge generation and execution, FineDex leverages generated interactions as actionable priors for an agent that discovers physically feasible contact strategies through practice in a physics-based digital twin. By adapting at test time without per-instance retraining, FineDex generalizes across fine-grained instructions and object configurations. Experiments demonstrate state-of-the-art HOI generation quality and fine-grained controllability, substantial improvements in dexterous manipulation success, and successful deployment on a real dexterous humanoid robot.

</details>

### [CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models](https://arxiv.org/abs/2611.33911)
*Woojin Kim, Jemin Hwangbo* · `cs.RO` · arXiv:2611.33911v1 · relevance 0.16

- **In one sentence**: CoTAMP is a framework that uses LLM-based and code-based modules to plan cooperative multi-quadruped tasks, inventing motions beyond a fixed skill set, with kinematic synthesis and trajectory optimization producing dynamically feasible trajectories.
- **In plain words**: The paper looks at how two four-legged robots can work together to get through spots a single robot cannot, such as a ledge one robot can only climb by standing on its partner, or a gap that must be bridged with boxes. The authors split the job into planning the sequence of robot poses and generating the actual movements, using language models for the creative steps and ordinary code to check each plan and send failures back for correction. On three simulated courses with two robot models, all 30 trials produced kinematically valid motion references that converged in the final physics refinement step, and the authors report advantages over several baselines in success rate, dynamic feasibility, execution time, and planning time and cost.
- **Why it matters**: The work tackles a harder version of robot planning, where the motions themselves are not pre-programmed, and it shows one way to combine language models with checks that catch their mistakes. It may matter for search-and-rescue or disaster-site robots, though the text reports only simulation results.
- **Background needed**: - Task and motion planning (TAMP): deciding both what steps to take and how the body physically moves to carry them out.
- Quadruped robot: a four-legged robot; RAIBO2 is the specific platform used here.
- Large language model (LLM): an AI text model that here proposes plans and motions, with code verifying them.
- Kinematic synthesis: computing body and limb positions from a motion outline, ignoring forces.
- Dynamics and trajectory optimization: adjusting a motion so it obeys physics (balance, forces, timing).
- Keyframe: a snapshot pose at a key moment; the full motion is interpolated between keyframes.
- Simulation: results come from a computer model, not from real hardware. · level: research-level

<details><summary>Original abstract</summary>

Some environments cannot be traversed by a single quadruped robot, for example a ledge that one robot can climb only from its partner's back or a gap that must be bridged with boxes. Solving them requires cooperative task and motion planning (TAMP). Previous works are limited to the motions of a single robot or only select actions from a predefined set of skills. We propose a framework with two parts: task planning that invents motions not defined in advance, and motion generation that realizes the invented motions. Both parts consist of large language model (LLM)-based modules and code-based modules. Task planning divides the trajectory of the whole task into steps and fixes the robot poses at the step boundaries. Motion generation produces keyframes that describe the motion of each step and turns them into a continuous trajectory through kinematic synthesis. The code-based modules check every plan and motion and return failures to the LLM-based modules for correction. The whole trajectory is then refined by trajectory optimization to satisfy the dynamics. On three simulated courses with two RAIBO2 robot models, our framework produced kinematically valid references in all 30 trials, all of which converged in trajectory optimization. Compared with several baselines, our framework showed advantages in success rate, dynamic feasibility, execution time, and generation time and cost. Project page: https://woojin8098.github.io/CoTAMP/

</details>

## Security and cryptography

### [Node Differential Privacy via Node-Stable Graph Projections](https://arxiv.org/abs/2611.33672)
*Ishaq Aden-Ali, Adam Sealfon, Adam Smith et al.* · `cs.CR` · arXiv:2611.33672v1 · relevance 0.10

- **In one sentence**: The paper gives a nearly linear-time randomized graph projection that degree-clips arbitrary graphs in a node-stable way, plus a deterministic Lipschitz extension for total edge weight, and applies both to node-private vector summation and gradient descent on graph-structured data.
- **In plain words**: The paper is about releasing useful statistics from network data (such as who emailed whom) while protecting each person fully, meaning all of their connections at once. The authors build two tools for this: a way to trim overly connected nodes so that no one person has too much influence, and a way to extend a total-weight calculation so it behaves well on every graph. They use these tools to design private methods for summing vectors and for gradient descent when each record is tied to a link between two people.
- **Why it matters**: Protecting whole individuals in network data is harder than protecting single rows, so better tools for doing it accurately and efficiently matter for privacy-preserving analysis of social and communication graphs. The text does not report experimental accuracy comparisons, so its practical gains beyond the stated guarantees are not shown here.
- **Background needed**: - Differential privacy: a guarantee that an output reveals little about whether any one record was included, usually achieved by adding carefully calibrated random noise.
- Node-differential privacy: the stronger version where the protected unit is a whole node (a person) and all their edges (connections) at once.
- Graph and degree: a graph is nodes joined by edges; a node's degree is how many edges it has. Most real networks have few high-degree nodes.
- Graph projection: a transformation that maps a graph to a nearby graph satisfying a degree limit.
- Lipschitz extension: a way to extend a function from a restricted set of inputs to all inputs while never changing its output by more than a fixed amount per unit of change in the input.
- Nearly linear time: an algorithm whose running time grows roughly in step with the size of the input. · level: research-level

<details><summary>Original abstract</summary>

Node-differentially private algorithms enable learning on network-structured datasets in which records reflect interactions among individuals. They protect the privacy of each individual's information, including all their associated records. A key challenge in the design of such algorithms is to exploit the structure of realistic graphs---where most nodes have low degree---to achieve high accuracy, without compromising on the worst-case privacy guarantee. In this work we give two new tools for designing accurate, computationally efficient node-differentially private algorithms. First, we give a nearly linear time, randomized, node-stable graph projection: the projection leaves graphs of maximum degree $D$ unchanged, maps arbitrary graphs to subgraphs of maximum degree $\hat D \approx D$, and ensures that changing one node of the input graph has only a small effect on the distribution of the edges selected among the remaining vertices. Unlike prior approaches, which abstain when the input violates the degree bound, our projection acts as degree clipping: even when $D$ is set well below the true maximum degree (trading truncation bias at high-degree outliers for lower privacy noise), it retains at least as many edges as a maximal $D$-bounded subgraph. Second, for graphs with bounded edge weights, we give a deterministic nearly linear time Lipschitz extension for the total edge weight that agrees with the original sum on graphs of maximum degree $D$ yet is $D$-Lipschitz on all graphs. Finally, we show how to apply these methods to design node-private algorithms for high-dimensional vector summation and gradient descent on datasets where records are associated with graph edges, such as email threads.

</details>

### [Model Weights, Airlocks and Sandboxes: A Call for Technical Validation of Re-identification Tests under the EDPB Anonymisation Guidelines](https://arxiv.org/abs/2611.34859)
*Rickard Br\"annvall, Henrik Forsgren, Erik Ylip\"a\"a et al.* · `cs.CR` · arXiv:2611.34859v1 · relevance 0.10

- **In one sentence**: A position paper arguing that re-identification tests used under the EDPB's draft anonymisation guidelines should be validated as measurement methods, with stated detection limits, bias and uncertainty, and examining this across model weight release, airlock output review, and regulatory sandboxes.
- **In plain words**: The paper looks at how regulators should judge whether data, or an AI model trained on data, is anonymous enough to be shared. Its authors say the European Data Protection Board's draft guidance asks for "re-identification tests" but does not explain how to design or check them. They propose treating these tests like laboratory measurements, so that a failed attempt to re-identify someone is only trusted once the test's limits are known.
- **Why it matters**: Whether a trained AI model counts as anonymous affects how companies and researchers can release it under European privacy law. The paper is a reasoned call for clearer standards rather than a reported result, so its value depends on whether regulators adopt its suggestions; the text does not show how that will play out.
- **Background needed**: - Anonymisation: making personal data so that people cannot reasonably be identified, which under EU data protection law takes it outside most rules.
- EDPB: the European Data Protection Board, which advises on how the GDPR is applied; its Guidelines 02/2026 on anonymisation were, per the text, published for consultation in July 2026.
- Re-identification test: an attempt to link anonymised data back to a specific person, used to check how well data is protected.
- Model weights: the numerical parameters learned by a machine learning model during training.
- Airlock: a secure environment where outputs are reviewed before they leave, so that only checked results are released.
- Regulatory sandbox: a supervised setting where an authority oversees development and testing of a product.
- Measurement validation: the practice, common in fields like medicine and engineering, of stating a method's detection limit, bias and uncertainty before trusting its results. · level: research-level

<details><summary>Original abstract</summary>

The Guidelines 02/2026 on anonymisation of the European Data Protection Board (EDPB), published for consultation in July 2026, assess anonymity relative to the entities that may access data. They bring AI models into scope and call for testing, but do not say how a re-identification test should be designed or validated, or how far its result counts as evidence. Building on our reply to the consultation, we describe a framework based on a secure processing environment whose outputs are reviewed before release (an airlock), and distinguish forms of release and three types of evidence: formal, empirical and indirect. We raise seven open questions, each with a scenario, and examine their technical side in three settings: the release of model weights (the trained parameters of a machine learning model), review at an airlock, and regulatory sandboxes, in which an authority supervises development and testing. In each setting the assessment depends on how far a test result can be relied on, since a failed re-identification attempt may mean only that the test was too weak. Drawing on measurement practice in other regulated fields, we call for re-identification tests to be validated as measurement methods, with stated detection limit, bias and uncertainty.

</details>

## Algorithms and complexity

### [PAC Learning to Sample: On Computational Aspects of Language Generation](https://arxiv.org/abs/2611.33464)
*Alkis Kalavasis, Shuchen Li, Manolis Zampetakis* · `stat.ML` · arXiv:2611.33464v1 · relevance 0.10

- **In one sentence**: This paper studies a PAC-style model of learning to sample from a Boolean concept class, showing that online learnability is not necessary for efficient PAC learning to sample and giving new algorithms built on offline ERM oracles plus approximate sampling/counting and SQ learners.
- **In plain words**: The paper looks at how a program can learn to produce new examples that look like the ones it has seen, such as text from a language model, with quantitative limits on how many examples and how much computation it needs. The authors work in a simplified setting where the target is a yes/no rule over binary strings and the learner receives random positive examples. They show that one standard ingredient, the ability to learn online, is not strictly required: they build a rule class where online learning is cryptographically hard but learning to sample is still efficient, and they give algorithms that use a different kind of learning oracle instead.
- **Why it matters**: Language generation in the limit is a recent theoretical framework for why models can produce valid new text, but most of its guarantees are qualitative. Putting concrete sample and time bounds on it, and identifying which ingredients are needed, is a step toward understanding its computational cost; the text itself frames this as a first step, and its connection to practical language models is suggested rather than established here.
- **Background needed**: - Concept class: a family of yes/no rules over n-bit strings; a "concept" labels each string as in or out.
- PAC learning: learning from random labeled examples with guarantees on accuracy and confidence, with efficiency measured in samples and time.
- Total variation distance: a measure of how different two probability distributions are.
- Sampler: a procedure whose outputs follow a target distribution, here uniform over the strings the rule accepts.
- Online learner, ERM (empirical risk minimization) oracle, SQ (statistical query) learner: three learning-algorithm models with different access rules.
- Cryptographically hard: believed infeasible for any efficient algorithm under standard cryptographic assumptions.
- Language generation in the limit: Kleinberg and Mullainathan's 2024 model, in which a generator must eventually produce unseen valid strings from a language given positive examples. · level: research-level

<details><summary>Original abstract</summary>

The success of language models has motivated theoretical work on learning to sample from distributions on discrete domains. A prominent abstraction is the model of language generation in the limit, introduced by Kleinberg and Mullainathan (NeurIPS 2024), in which the algorithm must generate from the target language after some finite but unspecified number of positive examples. While its positive results are surprisingly general, most guarantees are qualitative. In this work, we seek quantitative guarantees on sample and time complexity, inspired by statistical and computational learning theory. To this end, we study a PAC model of language generation, proposed (in a different context) by De, Diakonikolas, and Servedio (SODA 2015), in which a Boolean concept class $C$ over $\{-1,1\}^n$ defines the target languages: given uniformly random positive examples of an unknown concept $f \in C$, the learner must output a sampler whose output distribution (conditioned on the training data) is close in total variation to the uniform distribution over $f^{-1}(1)$. Their work implicitly gives an efficient algorithm for PAC learning to sample $C$, given three primitives for $C$: an online learner, approximate sampling and counting oracles, and an SQ learner. We ask whether these ingredients, in particular online learnability, are necessary. First, we construct a Boolean concept class $C$ for which online learning is cryptographically hard, yet PAC learning to sample is computationally efficient. Then, we develop new algorithms that use offline ERM oracles instead of online learners, together with approximate sampling/counting oracles for intersections of concepts in $C$ and an SQ learner for $C$. We view our results, together with the work of De, Diakonikolas, and Servedio, as a first step towards understanding the computational complexity of language generation.

</details>

### [Fast Algorithms for Permanents of Permutationally-Dominant Matrices](https://arxiv.org/abs/2611.33485)
*Ryan L. Mann* · `cs.DS` · arXiv:2611.33485v1 · relevance 0.09

- **In one sentence**: The paper gives a fully polynomial randomised approximation scheme for the permanent of permutationally-dominant matrices, with runtime quadratic in both the matrix dimension and the inverse of the error, using a polymer model and importance sampling of the log partition function via heaps of pieces.
- **In plain words**: The permanent is a way of combining the entries of a grid of numbers, similar to a determinant but without the sign flips, and computing it exactly is very hard in general. This paper focuses on a special class of grids, called permutationally-dominant matrices, and shows how to estimate their permanent quickly, using randomness, with a speed that grows only polynomially as the grid gets bigger or the wanted accuracy gets tighter.
- **Why it matters**: Approximating permanents is a classic problem in algorithms and complexity theory, and special classes where it becomes tractable help map where the hard cases begin. The text does not say how far the class extends beyond the matrices studied, so its wider reach is unclear from this abstract alone.
- **Background needed**: - Matrix permanent: like the determinant, but all terms are added with plus signs; exact computation is #P-hard in general.
- Approximation scheme (FPRAS): a randomised method that gets an answer within a chosen error margin with high probability, in time polynomial in the size and in 1/error.
- Partition function: a weighted sum over configurations, used in statistics and physics; its logarithm is often what is estimated.
- Polymer model: a way of writing such sums as collections of compatible, non-overlapping building blocks ("polymers").
- Importance sampling: estimating a sum by drawing random samples from a convenient distribution and reweighting them.
- Heaps of pieces (Viennot): a combinatorial framework for counting stacks of pieces with non-overlap rules. · level: research-level

<details><summary>Original abstract</summary>

We establish a fast algorithm for approximating the permanent of permutationally-dominant matrices. In particular, we obtain a fully polynomial randomised approximation scheme whose runtime is quadratic in both the dimension of the matrix and the inverse of the approximation error. Our approach is based on a polymer model representation of the permanent and importance sampling of the logarithm of its partition function via the theory of heaps of pieces of Viennot.

</details>

## Programming languages and formal methods

### [Show Your Work: Can Small Open Models Read SEC Filings with Evidence a Machine Can Check?](https://arxiv.org/abs/2611.24990)
*Krishna Nandula* · `cs.SE` · arXiv:2611.24990v1 · relevance 0.07

- **In one sentence**: A benchmark of 1,000 questions over 90 SEC 10-K/10-Q filings tests whether small open language models (7–21B parameters, run on one consumer GPU) can extract numbers together with machine-checkable evidence (page plus verbatim quote), and finds that checks catch many errors but not all.
- **In plain words**: Companies file yearly and quarterly financial reports with the US SEC, and an AI model asked to pull a figure from one of them can sound confident while being wrong. This paper asks whether small AI models that run on a single gaming-class graphics card can instead point to the exact page and quote the number comes from, so a program can verify the answer. The authors built a test of 1,000 questions over 90 recent filings from 45 companies, using the official tagged values as answer keys, and compared ten models under three setups.
- **Why it matters**: Trustworthy extraction of financial figures matters for anyone relying on automated reading of filings, and the paper shows that a simple automatic check is useful but incomplete: a noticeable share of wrong answers still pass it, mostly from scale, unit, or wrong-period mistakes. Its findings on reasoning modes and retries are concrete, though they come from one benchmark and one hardware setup, so how far they generalise is an open question.
- **Background needed**: - SEC 10-K (annual) and 10-Q (quarterly) filings: standard US company financial reports.
- Inline XBRL: a machine-readable tagging format embedded in these reports; the tags supply the answer keys.
- Instruct model: a language model fine-tuned to follow user requests; "open" means weights are publicly released.
- Parameters (7–21B): a rough measure of model size; small models can run on one consumer GPU.
- Check-and-retry: the model's answer is verified against its quoted evidence, and if the check fails it tries again.
- Reasoning mode: a setting where the model writes out intermediate reasoning before answering.
- Scale or unit errors: e.g., reporting figures in thousands as if they were in millions. · level: intermediate

<details><summary>Original abstract</summary>

A fluent answer from a language model is not a verified one. We ask whether small open models that run on a single consumer GPU can extract numbers from SEC filings with evidence a machine can check: the page and a verbatim quote containing the number. We introduce Filing-Evidence, a benchmark of 1,000 questions over 90 recent 10-K and 10-Q filings of 45 US companies, with answer keys taken from the filers' inline XBRL tags. We evaluate ten instruct models from ten developers (7-21B parameters) on one RTX 4090 in three setups: plain, check-and-retry, and the model's own reasoning mode. Accuracy with checkable evidence ranges from 17.1% to 82.7% in the plain setup, and the best result is 84.5% (Qwen3.5-9B). An automatic checker rejects many wrong answers, but between 16 and 167 answers per 1,000 give a wrong value for an answerable question and still pass every check. In the plain setup, 57% of these are scale or unit errors and 30% take another period or column of the right line. Reasoning significantly reduces such errors for 4 of 5 models that offer it. Retrying after a failed check raises accuracy by up to 3.9 points but never reduces them. Questions, model outputs, code and protocol are public.

</details>

### [SmartLens: Turning AI Agent Changes into Learning, Review, and Risk Signals in the IDE](https://arxiv.org/abs/2611.34377)
*Vahid Etemadi, Gregorio Robles* · `cs.SE` · arXiv:2611.34377v1 · relevance 0.06

- **In one sentence**: SmartLens is an IntelliJ IDEA plugin that attributes pending changes to AI coding agents versus the developer and uses that attribution, combined with Git history, for skill learning, review prioritization, and risk hotspot detection, with a preliminary evaluation.
- **In plain words**: Software developers are increasingly handing coding tasks to AI agents and then having to check, ship, and learn from the code those agents write. SmartLens is a plugin for a popular programming editor that labels which uncommitted edits came from an AI agent, the developer, or both. It then uses those labels to point out new skills the agent used, rank changes by how urgently they need review, and flag risky files.
- **Why it matters**: As more code is written by AI agents, knowing who wrote what and where the risk sits could matter for code quality and for developers' own learning. The evaluation is preliminary: attribution was correct in 8 of 12 scripted scenarios, and the risk ranking's advantage over plain churn (how often a file changes) is partly explained by recency, so its value is not yet established.
- **Background needed**: - IDE: integrated development environment, the software a programmer writes code in.
- IntelliJ IDEA: a widely used IDE; a "plugin" is an add-on to it.
- AI coding agent: a program that makes multi-step code edits on its own when given a task.
- Git: a version-control system that records the history of code changes as "commits."
- Attribution: working out who or what produced a given change.
- Churn: how often a file is modified; used here as a baseline for predicting bugs.
- Blind spots: cases where the attribution method is expected to be unreliable.
- Recency: the tendency for recently changed files to be more likely to have bugs regardless of other factors. · level: intermediate

<details><summary>Original abstract</summary>

Developers increasingly act as managers of AI agents: they hand tasks to AI coding agents and then have to understand, verify, ship, and learn from what the agents produce. IDEs and recent tools can show which committed lines were written by AI, but they do not attribute the pending changes of external agents, and they do not use attribution to help the developer review, learn, or judge risk. We present SmartLens, an IntelliJ IDEA plugin that attributes changes to an AI agent, the developer, or both. It combines this attribution with the Git history to support three goals: (i) Learn compares the skills (APIs, language features, annotations) that agents used with the skills the developer has used in their own commits; (ii) Understand ranks pending changes by review priority; and (iii) Risk shows hotspots: files that change often, are mostly written by AI, and that the developer barely knows. In a preliminary evaluation, SmartLens attributed 8 of 12 scripted IDE scenarios correctly; all failures were in (expected) blind spots. On 8 Open Source Software repositories with agent co-authored commits, agents introduced up to 253 skills that do not appear in the main developer's own commits. The Risk ranking was as good as or better than plain churn at predicting later bug fixes, but part of this gain is due to recency.

</details>

## Systems and networking

### [WADJET: Whole-Job Authorization and Dispatch for Job Execution Trust on FPGA System-on-Chip Accelerators](https://arxiv.org/abs/2611.33406)
*Mohamed El-Hadedy* · `cs.AR` · arXiv:2611.33406v1 · relevance 0.06

- **In one sentence**: WADJET is a hardware gate on an FPGA system-on-chip that authorizes, decrypts, and sequence-checks each whole accelerator job with Ascon-AEAD128 before writing the accelerator's registers, and reports a proven release path, a software model test, and a Zynq-7020 evaluation.
- **In plain words**: Chips that pair a processor with a programmable accelerator trust the processor's software to tell the accelerator what to do, so buggy or hijacked software can alter a single register or send the same job twice. This paper proposes a small hardware gate that sits between the processor and the accelerator: it checks that each complete job was approved, is intact, and has not been used before, and only then lets it through. In the authors' tests, the gate accepted all 21,000 approved jobs and rejected all 14,700 altered or repeated ones, at about a third of the logic cost of a comparable existing protection and with roughly ten extra microseconds per job start.
- **Why it matters**: It addresses a gap where existing protections control who can reach an accelerator or guard its data, but not whether a specific job was approved and is still unused. The evidence is a single platform and a language-model workload, and the design assumes its key, reset, and configuration are trusted, so the scope is narrower than the headline suggests.
- **Background needed**: - FPGA: a reconfigurable chip whose internal logic can be designed to act like custom hardware.
- System-on-chip (SoC): one chip combining a processor with accelerator hardware.
- Accelerator: a special-purpose circuit that does one kind of computation faster than the main processor.
- Registers: memory slots the processor writes to control a device.
- Authenticated encryption (AEAD, here Ascon): scrambles data so it cannot be read, and detects any tampering.
- Sequence number: a counter that lets a receiver reject old or repeated messages (replay protection).
- Formal proof on Verilog: a mathematical check that the hardware description behaves correctly for all possible inputs.
- Zynq-7020: a specific commercial FPGA SoC used for the tests.
- Lookup tables (LUTs): basic logic building blocks on an FPGA; fewer means a smaller design. · level: research-level

<details><summary>Original abstract</summary>

On an FPGA system-on-chip, the software that submits work to an accelerator also decides what the accelerator does. It writes the registers one by one, and the hardware runs whatever it finds, so faulty or compromised software can change one address or resend a job. Existing protections decide who may reach an accelerator or keep its data safe. Deciding whether one job was approved and is still unused takes three things in one place: the only way to the accelerator, the whole job held back until checked, and a record of used approvals. WADJET puts the three in one gate in FPGA logic. A separate authority encrypts and authenticates each approved job, with a sequence number, using Ascon-AEAD128. The gate verifies the whole job before releasing any part, accepts only a newer sequence number, uses it up, and writes the registers of an unmodified accelerator itself. The gate replaces only the processor's direct line to the registers and works beside the existing protections. In a software model, a check on each write ran jobs mixed from two approved ones; the whole-job rule released none. Its release path is proven on the Verilog for all inputs. On a Zynq-7020 running a language model, it released all 21,000 approved jobs and none of 14,700 altered or repeated ones. It needs a third of the lookup tables of ShEF's register protection, which protects more, and adds about ten microseconds to starting a job. It assumes trusted control of its key, reset, and configuration.

</details>

### [From Telemetry to Intelligence: A Data-Centric Survey of O-RAN](https://arxiv.org/abs/2611.34262)
*Samara Mayhoub, Zhengjia Xu, Tareq M. Shami et al.* · `cs.NI` · arXiv:2611.34262v1 · relevance 0.06

- **In one sentence**: A survey that reviews O-RAN (open, software-driven radio access networks for mobile networks) from a data-centric angle, classifying O-RAN data by source, accessibility, abstraction level, and application, and mapping how that data supports rule-based, AI/ML, and agentic AI control across different timescales.
- **In plain words**: Mobile phone networks increasingly rely on software that makes automatic decisions about radio resources, and those decisions are only as good as the data behind them. This paper surveys the kinds of data available in an open mobile network design called O-RAN, how it is collected and organized, and which control tasks it can support. It also lists the main data problems that could limit smarter, automated network control.
- **Why it matters**: Network operators are trying to automate radio networks with machine learning and newer agent-style AI, so a clear map of what data exists and where it comes from is useful for both researchers and engineers. The text itself does not report experimental results; its value is as an organizing framework and review of the field.
- **Background needed**: - O-RAN: an open, multi-vendor design for the radio part of mobile networks (the base stations and their control software), intended to let different companies' parts work together.
- Telemetry: measurements a network continuously reports, such as signal quality, load, and errors.
- Control loops at different timescales: some decisions are made in milliseconds, others over minutes or longer.
- AI/ML: machine learning methods that learn patterns from data to make predictions or decisions.
- Agentic AI: AI systems that plan and take multi-step actions with some autonomy, rather than only answering a single query.
- Rule-based control: fixed if-then policies written by engineers. · level: intermediate

<details><summary>Original abstract</summary>

The Open Radio Access Network (O-RAN) has emerged as a new architecture for enabling programmability, intelligence, automation, and multi-vendor interoperability in the wireless domain of public telecommunications networks. Artificial Intelligence/Machine Learning (AI/ML), and more recently Agentic AI, are considered key enablers of automation and intelligentization in O-RAN. However, the effectiveness of such systems is constrained by the availability, quality, and structure of O-RAN data. In this survey, we present a data-centric perspective of O-RAN, focusing on how data support rule-based, AI/ML-driven, and emerging Agentic AI applications across various timescale control loops. We analyze O-RAN data along multiple dimensions, including source, accessibility, abstraction level, and application. We further identify key data challenges, and discuss their implications for intelligent control. The overarching objective of this work is to present the first comprehensive review of the data-centric perspective on intelligent applications in O-RAN. To this end, it introduces a unified framework for understanding the role of O-RAN data in enabling network intelligence and automation.

</details>

## Human-computer interaction

### [Knocking on Minds Door; A Mixed-Methods Field Study of a Voice LLM Companion in Older Adults Daily Lives](https://arxiv.org/abs/2611.33727)
*Inhee Cho, Jinyoung Jeong, Byung Ju Kim et al.* · `cs.HC` · arXiv:2611.33727v1 · relevance 0.07

- **In one sentence**: A two-week mixed-methods field study of a proactive, persona-driven voice LLM phone companion with prior-call memory, used by 33 community-dwelling Korean older adults, reporting call logs, pre-post loneliness and depression scores, and interviews.
- **In plain words**: Many older adults find smartphone and computer screens hard to use, so this study tested a voice-only "companion" that works like a phone call and starts conversations on its own. Thirty-three older adults in Korea used it for two weeks and made 608 calls, and 25 kept using it afterward even though taking turns in conversation was sometimes hard. Their loneliness and depression scores went down, mainly in the feeling of being isolated, and they talked about worries they had not shared with family.
- **Why it matters**: It offers evidence from real daily life, not just lab tests, on why older people might keep using a voice AI, which bears on digital inclusion and healthy aging. The text does not show whether the drop in scores lasted or was caused by the companion alone, since the study has no comparison group described, so the findings are best read as preliminary.
- **Background needed**: - Large language model (LLM): an AI system that generates conversational text; here it powers the voice conversations.
- Voice agent: software that talks and listens instead of relying on a screen or buttons.
- Mixed-methods field study: research that combines numbers (questionnaires, call logs) with interviews, carried out in participants' everyday settings.
- Proactive: the system initiates calls rather than waiting for the user.
- Persona and conversation rules: a defined character and guidelines that shape how the AI talks.
- Loneliness subfactors: loneliness scales split into parts; here, "isolation" refers to emotional loneliness, the sense of lacking close connection.
- Turn-taking: the back-and-forth timing of conversation, which can be hard for voice systems and users.
- Pre-post questionnaires: surveys taken before and after the study period to measure change. · level: intermediate

<details><summary>Original abstract</summary>

Global aging makes digital technology important for older adults healthy aging, yet graphical user interfaces remain inaccessible to many. Voice agents based on large language models may help, but users needs and reasons for sustained use remain unclear. We developed a phone-call-style companion that initiates conversations proactively and structures calls using a persona, conversation rules, and prior-call memory (facts, insights, relationship background). We conducted a two-week mixed-methods field study with 33 community-dwelling Korean older adults (29 women; aged 67-91), collecting call logs, pre-post questionnaires, and interviews. Participants made 608 calls following a daily-use recommendation; 25 continued afterward despite turn-taking difficulties. Loneliness and depression scores decreased significantly; among loneliness subfactors, only isolation (emotional loneliness) decreased significantly. Participants disclosed concerns withheld from family and linked companionship to being addressed by name, being remembered, and experiencing emotional reciprocity. We propose personalized conversation rules, accessible interaction, and user control over frequency and topics.

</details>

### [Language models call themselves AI but do not favor AI over people](https://arxiv.org/abs/2611.33851)
*Messi H. J. Lee* · `cs.CY` · arXiv:2611.33851v1 · relevance 0.06

- **In one sentence**: Using social identity theory as a lens, the paper tests whether 24 language models favor AI agents over humans across three experiments, finding that assigned group membership drives favoritism far more than an AI self-label does.
- **In plain words**: People worry that AI systems might take each other's side against humans. This paper checks that worry by asking whether language models give more to fellow AI agents than to people. The authors found that the models favored a group they were assigned to, even a team of AI agents, but when no group was assigned they gave a person more money and credit than an AI agent.
- **Why it matters**: The question bears on how AI systems might behave when they interact with each other, which matters for safety and for multi-agent deployments. The text is a short summary, so it is unclear how robust the findings are across tasks or setups, and the conclusion should be read as limited to the experiments described.
- **Background needed**: - Social identity theory: a psychology idea that people favor members of groups they belong to, sometimes at the expense of outsiders.
- Language model: an AI system trained on large amounts of text to produce human-like replies.
- Multi-agent setting: several AI programs interacting with each other, sometimes as a team.
- Experiments here gave models tasks in which they could allocate money and credit between a person and an AI agent.
- Self-label prompts: instructions asking a model to say it belongs with AI, used to test whether identity alone drives behavior. · level: intermediate

<details><summary>Original abstract</summary>

Many fear that AI systems will side with one another against people. Social identity theory, which explains why people favor their own group, offers one way to examine this fear. Seen through this theory, AI would side with AI only if it treated AI as its group and favored AI over people. In three experiments, 24 language models favored a group they were assigned to, even a team of AI agents. With no group assigned, they gave a person more money and credit than an AI agent. Prompts that made them say they belong with AI changed their behavior much less than an assigned team did. These models call themselves AI but do not favor AI over people. Judged by social identity theory, they show no sign of siding with AI against people.

</details>

## Information theory

### [An Information-Theoretic Analysis of Information Hiding in Semantic Communication](https://arxiv.org/abs/2611.34550)
*Yanhao Huo, Shijun Xiang* · `cs.IT` · arXiv:2611.34550v1 · relevance 0.11

- **In one sentence**: The paper builds an information-theoretic framework for hiding messages in semantic communication, extending the classical Moulin-O'Sullivan hiding capacity to a two-layer semantic/syntactic model cast as a Stackelberg (leader-follower) maximin game, and compares the resulting capacity with the classical one via endpoint bounds.
- **In plain words**: The paper asks how much hidden information can be sent when communication is judged by meaning rather than by exact symbols, and whether hiding at the meaning level beats classical hiding. The authors model the problem as a two-layer system with distortion limits on both the raw signal and the meaning, and express the capacity as a game where the hider moves first. They report that semantic hiding is not always better than classical hiding, and show with binary, ternary and Gaussian examples that it loses capacity when the mapping between meanings and symbols is coarsened.
- **Why it matters**: Semantic communication is an active area for future networks, and information hiding (covert or watermarked messages inside a signal) is a natural security question for it. The paper gives a formal benchmark for when meaning-level hiding helps or hurts, though its value depends on the correctness of the derivations, which I have not checked.
- **Background needed**: - Channel capacity: the maximum rate at which information can be sent reliably over a noisy channel.
- Mutual information: how much knowing one signal reduces uncertainty about another.
- Information hiding (steganography/watermarking): embedding a message in a host signal so that it stays nearly undetectable and the host is not much distorted.
- Semantic communication: transmitting the meaning of a message rather than exact symbols, so that different symbol strings with the same meaning count as equivalent.
- Synonymous mapping: a conversion between a meaning and the set of symbol strings that express it.
- Stackelberg game: a two-player game where one player commits to a strategy first and the other responds.
- Maximin: choosing the strategy that maximizes the worst-case payoff.
- Random coding and joint typicality: standard proof tools for showing a rate is achievable and is an upper limit. · level: research-level

<details><summary>Original abstract</summary>

Semantic communication shifts the transmission goal from the accurate recovery of syntactic symbols to the reliable conveyance of semantic content, yet a systematic information-theoretic characterization of information hiding at the semantic layer is still missing. Building on the semantic information theory of Niu-Zhang and the classical information hiding theory of Moulin-O'Sullivan, this paper establishes an information-theoretic framework for information hiding under semantic communication. The classical hiding model is extended to a two-layer structure (semantic host, syntactic host, syntactic composite signal, syntactic received, semantic received) bridged by synonymous mappings f_s, f_x and the inverse mapping f_y^{-1}, subject to four distortion constraints: syntactic transparency, semantic fidelity, syntactic perturbation, and semantic destruction. The capacity is cast as a Stackelberg game with the hider moving first and the payoff J(Q,A) = I(U~; Y~ | K) - I(U~; S~ | K), yielding the single-letter maximin C^s = max_Q min_A J(Q,A), whose achievability and converse follow from random coding and joint typicality decoding. Relative to the classical capacity, comparison payoffs built from the up/down semantic mutual information give the endpoint sandwich C^s_end(0,1) <= C^s <= C^s_end(1,0) with the classical value C in the same interval, while closing semantic tolerance yields C^s_no-tol <= C_cl under a fair comparison. These results clarify that semantic hiding is not unconditionally superior to classical hiding. Binary, ternary, and Gaussian examples confirm the degeneration under one-to-one mappings and the capacity loss under coarsening.

</details>

### [Sharp one-shot bounds and optimal exponents of universal randomness extraction](https://arxiv.org/abs/2611.33270)
*Bartosz Regula, Hao-Chung Cheng* · `quant-ph` · arXiv:2611.33270v1 · relevance 0.10

- **In one sentence**: The paper derives tight one-shot bounds and exact asymptotic error exponents for quantum privacy amplification (randomness extraction against quantum side information) using universal hash functions, via quadratically constrained hypothesis testing and operator-space methods.
- **In plain words**: The paper studies how to turn a partly unpredictable source of random bits into nearly perfect secret randomness, even when an eavesdropper may hold quantum information about it. It works out how fast the leftover error shrinks as the amount of input grows, in several regimes. The authors find that a previously known bound is tight up to a constant factor for certain hash functions, and they pin down the exact rate at which the error decays in the strong converse regime for 2-universal hashes.
- **Why it matters**: Privacy amplification is a basic building block of quantum cryptography and secure key generation, so sharper error scalings matter for knowing what key rates are achievable in practice. The text reports matching upper and lower bounds, which is what makes the exponents "exact"; the connection to non-commutative Khintchine inequalities is a noted technical link, but its wider significance is not spelled out in the text.
- **Background needed**: - Randomness extraction: converting a weak, partly secret source into close-to-uniform secret bits using a randomly chosen hash function.
- Quantum side information: an eavesdropper may hold quantum systems correlated with the source.
- Trace distance: the standard measure of how far a quantum state is from an ideal one; here it measures security error.
- Universal hash functions (2-universal, strongly 4-universal): families of hashes such that random members behave well on average, used to bound collision-type behavior.
- One-shot versus i.i.d. regimes: one-shot means a single use of the source with a finite-size guarantee; i.i.d. means many independent copies, where asymptotic error exponents describe decay rates.
- Error exponent and strong converse regime: the exponent gives how fast error vanishes when the extraction rate is below the entropy limit; the strong converse regime is when the rate is above it, so error tends to one.
- Hypothesis testing: deciding between two candidate states; its optimal error rates underpin many of the bounds. · level: research-level

<details><summary>Original abstract</summary>

We introduce techniques for the study of randomness extraction against quantum side information (privacy amplification) by relating this problem to variants of hypothesis testing tasks with quadratic constraints. Building also on the recently introduced measured smooth entropy approach of [Regula and Tomamichel, arXiv:2603.04493], we precisely determine the optimal scaling of the error of quantum privacy amplification in several regimes. Our results apply to the standard operational security criterion based on trace distance and focus in particular on universal classes of hash functions. On the technical side, our investigation reveals connections with operator space theory methods used in non-commutative Khintchine inequalities. As one application, we give a one-shot converse bound that shows the leftover hash lemma of [arXiv:2603.04493] to be tight up to a constant factor for all strongly 4-universal hash functions. This allows us to evaluate the asymptotic i.i.d. error exponent of universal randomness extraction for all rates, matching the bound of [Dupuis, arXiv:2105.05342] and improving also earlier classical asymptotic results of [Hayashi, arXiv:1010.1358]. We furthermore give new one-shot achievability and converse bounds on the error in the strong converse regime, which we show to match up to a constant factor. This establishes the exact strong converse exponent of quantum privacy amplification under 2-universal hash functions, complementing the converse bound of [Shen, Gao, and Cheng, arXiv:2202.10263].

</details>

## High-energy theory and gravity

### [Chaotic singularities inside vacuum black holes](https://arxiv.org/abs/2611.33287)
*Robie A. Hennigar, Ayan K. Patra* · `hep-th` · arXiv:2611.33287v1 · relevance 0.17

- **In one sentence**: Constructs stationary, asymptotically locally AdS5 black holes with regular, triaxially squashed horizons whose homogeneous interiors realize the cosmological billiard of generic five-dimensional vacuum gravity, giving an algebraic criterion for interior chaos and showing that regular-horizon solutions locally access an open set of billiard trajectories.
- **In plain words**: The paper asks whether the inside of a black hole, near the point where spacetime breaks down, can behave chaotically, as a 1960s conjecture by Belinski, Khalatnikov and Lifshitz predicted for generic spacelike singularities in Einstein's gravity. Until now no pure-gravity black hole had been shown to do this. The authors build five-dimensional black holes (in a setting with anti-de Sitter boundary conditions) whose interiors follow the kind of chaotic bouncing dynamics the conjecture describes, and they give a simple algebraic test on the horizon shape that is needed for this chaos.
- **Why it matters**: It is a concrete, checkable case where the long-standing conjecture about chaos near singularities is realized inside a vacuum black hole, which matters for understanding what happens inside black holes. The text does not say how far the result extends beyond five dimensions or to other settings, so its wider reach is uncertain.
- **Background needed**: - General relativity: Einstein's theory of gravity, in which black holes contain singularities where the equations break down.
- Horizon: the boundary of a black hole beyond which nothing escapes.
- Spacelike singularity: a singularity that lies in the future of an infalling observer, like the Big Bang in time, not a point in space.
- BKL conjecture: the proposal that near generic singularities, space stretches and squeezes in oscillating, chaotic-looking cycles.
- Cosmological billiard: a simplified geometric model where the BKL dynamics is a ball bouncing between walls in an abstract space, and chaos corresponds to trajectories that never settle into a regular pattern.
- AdS (anti-de Sitter) space: a negatively curved spacetime often used as a theoretical laboratory; "asymptotically locally AdS5" means the geometry looks like this far away, in five spacetime dimensions.
- Vacuum: no matter or energy fields, only gravity. · level: research-level

<details><summary>Original abstract</summary>

According to the conjecture of Belinski, Khalatnikov and Lifshitz, general relativity gives rise to chaotic dynamics in the vicinity of generic spacelike singularities. However, no vacuum black hole has been shown to exhibit this behaviour. Here we construct stationary, asymptotically locally AdS$_5$ black holes with regular, triaxially squashed horizons and causal exteriors, whose homogeneous interiors realize the cosmological billiard of generic five-dimensional vacuum gravity. We identify a simple algebraic condition on the horizon data that is necessary for the interior billiard to be chaotic, and show that solutions with regular horizons locally access an open set of billiard trajectories.

</details>

### [Late-time OTOCs in Toda conformal field theory](https://arxiv.org/abs/2611.33744)
*Giwan Kim, Masahito Yamazaki* · `hep-th` · arXiv:2611.33744v1 · relevance 0.17

- **In one sentence**: Late-time out-of-time-order correlators of semi-degenerate primary fields in two-dimensional A_{N-1} Toda conformal field theory, examined for N=2 (Liouville), N=3, and N≥4, with a conditional phase-diagram result.
- **In plain words**: This paper studies a measure of how quickly scrambling-type information spreads in a simplified quantum field model, the late-time behaviour of out-of-time-order correlators (OTOCs). For the simplest case (Liouville theory) the author reports that the OTOC decays as a power of time, t to the power -3/2, rather than settling to a constant as earlier work reported. For the N=3 case, the author finds the late-time value is a pure phase under an assumed completeness condition, and says a dominant discrete term gives a constant limit.
- **Why it matters**: It corrects a previously reported result for a well-studied model and identifies where a simple picture of late-time scrambling breaks down at higher rank. Its connection to broader questions about chaos and information spreading in gravity-related holographic models is suggested by the field, but the text itself does not establish that link.
- **Background needed**: - OTOC: a correlation between measurements at different times that is used as a diagnostic of how quickly quantum information spreads and mixes (chaos).
- Two-dimensional conformal field theory: quantum field theory on a plane with scale invariance, where symmetry strongly constrains correlators.
- Liouville and Toda theories: families of such theories labelled by a rank N; Liouville is the N=2 case.
- Primary fields and intermediate states: operators with definite scaling weights; correlators are expanded as sums or integrals over intermediate states.
- Continuum edge and discrete residue: the lower boundary of a continuous spectrum of states, and isolated states whose contributions can dominate late times.
- Crossing symmetry: a consistency condition relating different channels of the same correlator.
- Braiding phase: a phase acquired when operators are exchanged around each other. · level: research-level

<details><summary>Original abstract</summary>

We study late-time out-of-time-order correlators (OTOCs) of semi-degenerate primary fields in two-dimensional $A_{N-1}$ Toda conformal field theory. In Liouville theory ($N=2$), we find that the OTOC decays as $t^{-3/2}$ when the continuum edge dominates, correcting a previously reported constant limit. For $N=3$, a transverse contour pinch reduces the spectral integral to one dimension. Assuming that the reduced expansion is complete, in the continuous phase the regulated edge behaves as a discrete state, and the OTOC approaches a pure braiding phase. As we check numerically, the edge block is a free-field correlator in a charge-neutral Weyl frame; this explains the pure phase and is consistent with crossing symmetry. For both $N=2$ and $N=3$, a dominant discrete residue gives a constant late-time limit. For $N\geq4$, the same one-dimensional reduction violates a crossing bound on the lowest intermediate weight of a positive diagonal expansion. Hence the $N=2,3$ phase diagram does not extend to higher rank without additional contributions below the reduced continuum edge or outside a positive diagonal expansion.

</details>

## Statistical physics

### [Bosonic Magic Resources at Quantum Criticality](https://arxiv.org/abs/2611.33306)
*Paolo Stornati, Piotr Sierant, Emanuele Tirrito* · `cond-mat.quant-gas` · arXiv:2611.33306v1 · relevance 0.11

- **In one sentence**: The paper uses quantum relative entropy, a measure of non-Gaussianity determined by one-body correlations, to study quantum phase transitions in the ground state of the one-dimensional extended Bose-Hubbard model.
- **In plain words**: The paper asks whether a quantity that measures how "non-Gaussian" (non-simple) a quantum state of bosonic particles is can reveal when a many-particle system changes its phase. The authors compute this measure for the ground state (lowest-energy state) of a one-dimensional lattice model of interacting bosons and track how it scales with system size. They report that the scaling picks out transitions involving hidden order and conventional order, with distinct signatures at each.
- **Why it matters**: It proposes non-Gaussianity, a resource needed for universal quantum computing with continuous-variable systems, as a probe of many-body criticality, which links quantum information ideas to strongly correlated matter. The text does not show how broadly the approach applies beyond this model, so its wider significance is still to be tested.
- **Background needed**: - Bosons: particles (such as photons or atoms of certain types) that can pile into the same quantum state.
- Bose-Hubbard model: a lattice model of interacting bosons; the extended version adds interactions between neighbouring sites.
- Ground state: the lowest-energy state of a quantum system, which is what the paper studies.
- Quantum phase transition: a sharp change in the collective behaviour of a system at zero temperature, driven by a parameter such as interaction strength.
- Gaussian vs non-Gaussian states: Gaussian states have a simple statistical structure that is efficiently describable and not enough for universal quantum computation; non-Gaussianity is the extra ingredient needed.
- Quantum relative entropy: a distance-like measure between a state and its nearest simple (Gaussian) reference; it depends only on one-body correlations here.
- Luttinger liquid: a standard low-energy description of one-dimensional interacting quantum fluids.
- Hidden (string) order vs conventional order: hidden order is not visible through a simple local observable, whereas conventional order is, e.g. density patterns.
- Ising criticality: the universal behaviour of the Ising model at its critical point, used as a benchmark class of transitions. · level: research-level

<details><summary>Original abstract</summary>

Non-Gaussianity is a resource for bosonic quantum information processing, providing a necessary ingredient for universal quantum computation in continuous-variable systems. Here we quantify non-Gaussianity in the ground state of the one-dimensional extended Bose-Hubbard model using quantum relative entropy (QRE), a measure determined solely by one-body correlations. The scaling of the QRE with system size reveals quantum phase transitions involving hidden and conventional order. We connect QRE scaling in the weakly interacting superfluid phase to Luttinger-liquid correlations and identify distinct critical signatures in its extensive and subleading contributions. At the Mott-Haldane transition, subtracting the extensive background reveals a pronounced peak in the subleading contribution, providing a clear signature of the onset of hidden string order. At the Haldane-density-wave transition, the extensive contribution to the QRE instead exhibits scaling consistent with Ising criticality. These results establish non-Gaussianity as a probe of many-body criticality, linking bosonic quantum resources to strongly correlated matter.

</details>

### [Neural Network Field Theory and the AdS/CFT Correspondence](https://arxiv.org/abs/2611.33281)
*Dmitry S. Ageev, Yulia A. Ageeva, Anna S. Bernakevich* · `hep-th` · arXiv:2611.33281v1 · relevance 0.11

- **In one sentence**: The paper builds a neural-network realization of a massive scalar field on Euclidean anti-de Sitter space, adds quartic interactions in two ways, and recovers the boundary two-point function and leading four-point contact Witten diagram via the BDHM prescription.
- **In plain words**: The authors ask whether a random neural network can reproduce the behavior of a quantum-style field living in a curved space, and whether its outputs on the edge of that space match known holographic (AdS/CFT) correlations. They build neurons from Fourier-Bessel cosine functions whose statistics match the known propagator, and add interactions either by reshaping how the network's weights are sampled or by using auxiliary binary neurons. They report that the expected boundary correlators come out of this setup, and that different architectures can give the same boundary results while describing different interior theories.
- **Why it matters**: It offers a concrete way to view holography through the lens of neural network ensembles, and it points to architecture choice as something that can change the bulk description without changing boundary observables. The text does not show whether this framework leads to new physics or practical tools beyond this setting, so its wider significance is uncertain.
- **Background needed**: - Neural network field theory: a neural network with random weights, in the infinite-width limit, behaves like a Gaussian field; finite width gives corrections.
- Anti-de Sitter (AdS) space: a curved, negatively curved spacetime; "Euclidean" means time is replaced by an imaginary direction, which is standard for statistical-physics calculations.
- AdS/CFT (holography): a conjectured correspondence between a gravitational theory in the bulk of AdS space and a conformal field theory living on its boundary.
- Propagator and two-point function: the correlation between field values at two points; the bulk-to-boundary propagator links interior points to boundary points.
- Witten diagram: a diagrammatic way to compute correlators in AdS; a contact diagram comes from a single interaction vertex.
- Quartic interaction: a four-field term in the action, the simplest non-Gaussian (interacting) case.
- BDHM prescription: a standard recipe (Banks–Douglas–Horowitz–Martinec style) for extracting boundary correlators from bulk generating functionals. · level: research-level

<details><summary>Original abstract</summary>

We develop a neural realization of massive scalar field theory on Euclidean anti--de Sitter space and its holographic boundary observables within neural network field theory (NN--FT). We construct Fourier--Bessel cosine neurons whose covariance reproduces the regulated massive AdS propagator exactly at finite network width, with the Gaussian field theory recovered in the infinite-width limit. We introduce quartic interactions through two complementary approaches. The first implements a prescribed interaction by deforming the neural parameter measure, while the second generates a local quartic interaction from the statistics of auxiliary binary neurons. Applying the BDHM prescription directly to the neural ensemble, we recover the scalar bulk-to-boundary propagator, the conformal boundary two-point function, and the leading connected four-point contact Witten diagram. We further show that distinct neural architectures can reproduce the same leading boundary correlators while defining inequivalent bulk theories. These results establish a framework for studying interacting scalar holography within NN--FT and clarify the role of neural architecture in encoding bulk dynamics and boundary observables.

</details>

## Condensed matter

### [Tunable quantum metric driven nonlinear valley Hall effect in the PT-symmetric sliding antiferroelectric MoS$_2$](https://arxiv.org/abs/2611.34116)
*Wen-Xin Jiang, Zhen-Hao Gong, Zhigang Gui et al.* · `cond-mat.mes-hall` · arXiv:2611.34116v1 · relevance 0.14

- **In one sentence**: A first-principles study proposes a four-layer MoS2 stack with sliding antiferroelectric order and strain-broken C3z symmetry, where a quantum-metric-driven nonlinear valley Hall response appears while inversion and time-reversal symmetries are preserved and can be switched by interlayer sliding.
- **In plain words**: The paper looks at a thin, layered crystal of molybdenum disulfide, a material that can carry information in its "valleys," which are distinct energy peaks electrons can occupy. The authors propose stacking four atomic layers so that they slide relative to one another, and that sliding can be reversed electrically. Their calculations suggest this produces a sideways electron current that depends on the valley, with its direction and size tunable by the slide state.
- **Why it matters**: It offers a way to probe quantum geometry, a property of electron wavefunctions beyond the usual Berry curvature, in a nonmagnetic material without breaking the usual symmetries, and to switch it electrically in a non-volatile way. Its relevance to real valleytronic or quantum information devices is a proposal based only on the abstract and has not been tested experimentally here.
- **Background needed**: - Quantum metric: a geometric property of electron wavefunctions that measures how quickly quantum states change; its real part is the quantum geometric tensor.
- Berry curvature: a related geometric quantity that drives many Hall-type transport effects.
- Valley: a local energy minimum or maximum in a crystal's electron band structure that can act as a label, like a bit, for electrons.
- Valley Hall effect: a sideways electron flow that depends on valley label, rather than on charge alone.
- Nonlinear response: an effect whose strength depends on the square of an applied electric field, not just linearly.
- Symmetry (inversion P, time reversal T, rotation C3z): operations that leave a crystal unchanged; breaking them usually enables new effects.
- Antiferroelectric / sliding ferroelectric: layered materials where neighboring layers shift and create opposing electric polarization that can be flipped.
- First-principles calculations: quantum-mechanical computer simulations that predict material properties from basic physics without fitted experimental parameters. · level: research-level

<details><summary>Original abstract</summary>

The quantum metric, the real part of a quantum geometric tensor, plays an important role in fundamental transport and optical responses of quantum materials. While net quantum metric effects are typically realized by breaking both time-reversal (T) and inversion (P) symmetries, valley-contrast mechanisms enable the probing of quantum geometry in centrosymmetric, nonmagnetic systems, revealing physical signatures beyond Berry curvature. Here, we design a four-layer MoS$_2$ platform that combines sliding antiferroelectric order with strain-induced $C_{3z}$ breaking to realize a quantum metric driven nonlinear valley Hall effect (NVHE) under preserved P and T symmetries. Reversible interlayer sliding (ABBA $\leftrightarrow$ BAAB) provides nonvolatile electrical control of the valley response. First-principles calculations reveal an outer-layer-dominated NVHE with tunable sign and magnitude. This symmetry-preserving, sliding-tunable strategy activates hidden quantum geometric phenomena in realistic two-dimensional materials and opens a clean pathway for tunable valleytronics and quantum information devices.

</details>

### [Superconductivity from the Berry connection from many-electron wave functions: $U(1)$ gauge fluctuation, gauge invariance, and superconductivity](https://arxiv.org/abs/2611.33723)
*Hiroyasu Koizumi* · `cond-mat.supr-con` · arXiv:2611.33723v1 · relevance 0.14

- **In one sentence**: The paper proposes a superconductivity theory built on the Berry connection of many-electron wave functions and on fluctuations of that connection, arguing that it reproduces major BCS results while resolving two stated disagreements with experiment.
- **In plain words**: The paper is a theoretical attempt to explain superconductivity, the state where a metal carries electric current with no resistance. The author treats the electromagnetic gauge (a mathematical freedom in how electric and magnetic potentials are written) and random jumps between quantum states as the key ingredients. The text claims this approach explains the reversible switch between superconducting and normal states in a magnetic field, including the force balance involved.
- **Why it matters**: Superconductivity is a long-studied, well-established field, so any new framework draws attention mainly if it resolves known mismatches with experiment. The abstract says the theory claims to fix two such disagreements, but the text does not list them or show the evidence, so the claim is currently unverified and should be checked against the full paper.
- **Background needed**: - Superconductivity: zero electrical resistance below a critical temperature or magnetic field.
- BCS theory: the standard microscopic theory (1957), where electrons pair up and the paired state has no resistance.
- Gauge invariance: the principle that physical results do not change when potentials are shifted by a mathematical convention; it underlies electromagnetism.
- Berry connection: a geometric quantity describing how a quantum state's phase changes as parameters vary; it is computed from the wave function.
- Gauge fluctuation: random variation of this phase-like quantity, which the paper links to transitions between quantum states.
- The abstract is brief and gives no equations, so detailed methods cannot be assessed from it. · level: research-level

<details><summary>Original abstract</summary>

The electromagnetic $U(1)$ gauge invariance and superconductivity are examined by employing the Berry connection from many-electron wave functions and the fluctuations of it that give rise to the probabilistic random transitions among quantum states. The gauge invariance in the classical electrodynamics is regarded as the requirement that extracts unaffected parts by the gauge fluctuation. In quantum mechanics, dissipation-free states from the gauge fluctuation exist, and we identify them as superconducting states. We explain the reversible superconducting-normal phase transition in a magnetic field including the force balance. The present superconductivity theory lifts two fundamental disagreements between theory and experiment existing in the current standard theory with keeping the major results by the BCS theory. Thus, it may be considered as a superconductivity theory encompassing the current standard one.

</details>

## Particle physics

### [Lighting up LZ with Loopy Transitions in a leptophilic Dark Sector](https://arxiv.org/abs/2611.34438)
*Simone Biondini, Clara Hofheinz, Stefan Melchin et al.* · `hep-ph` · arXiv:2611.34438v1 · relevance 0.16

- **In one sentence**: A study of a multicomponent, leptophilic dark sector with a charged vector-like fermion t-channel mediator, showing that endothermic (up-scattering) inelastic transitions between nearly degenerate scalar and vector dark matter states could produce the single high-energy xenon recoil reported by LZ while keeping the relic abundance consistent with thermal production.
- **In plain words**: The LUX-ZEPLIN (LZ) experiment, which looks for dark matter by watching for tiny flashes of energy when particles hit xenon atoms, recently recorded one unusually energetic nuclear recoil. This paper proposes that a hidden family of closely matched dark particles could explain it: a dark particle absorbs a small amount of energy and becomes a slightly heavier partner, which shifts the recoil energies upward. The authors report that this scenario can fit the single event while still producing the right amount of dark matter in the early universe.
- **Why it matters**: A single event is a weak signal, so this is a model-building exercise rather than a confirmed discovery; it is worth attention because it shows how a dark sector that couples mainly to leptons could account for an unusual signal while remaining consistent with cosmology. The text does not indicate how the scenario fares against other experimental limits in detail.
- **Background needed**: - Dark matter: invisible matter making up most of the universe's mass; direct detection looks for it hitting ordinary atoms in underground detectors.
- Nuclear recoil: the kick a xenon nucleus gets when struck; its energy (in keV) is what the detector measures.
- Leptophilic: interacting mainly with leptons (such as electrons and muons) rather than quarks.
- t-channel mediator: a heavy intermediate particle exchanged between the dark sector and Standard Model particles.
- Vector-like fermion: a type of matter particle whose left and right parts behave the same way under the forces, used here as the mediator.
- Inelastic/endothermic scattering: the incoming dark particle must gain a small energy to turn into a slightly heavier dark partner; the mass splitting (a few hundred keV) sets the energy cost, which pushes recoils toward higher energies.
- Effective operators at dimension five and six: a way of describing interactions by their strength and complexity; the paper argues the inelastic process appears at a lower order than elastic scattering, which explains why it dominates.
- Relic abundance: the amount of dark matter left over from the early universe, used to test whether a model is viable. · level: research-level

<details><summary>Original abstract</summary>

We study the direct detection phenomenology and cosmology of a multicomponent dark sector with a leptophilic t-channel portal. The coupling to right-handed Standard Model leptons is mediated by a charged vector-like fermion, allowing both a scalar and a vector dark candidate to connect to the SM through the same mediator. Motivated by the high-energy nuclear-recoil event recently reported by the LUX-ZEPLIN (LZ) experiment, we consider a nearly degenerate dark sector with mass splittings of order a few hundred keV and investigate the resulting inelastic transitions. Concretely, we focus on endothermic scattering of the dark states, which can shift the recoil spectrum towards the high-energy region preferred by LZ while suppressing low-energy events. We scrutinize the effective operators generating the dark-matter-photon coupling, which provides the essential interaction for nuclear recoils. Interestingly, the inelastic transition arises at dimension five whereas elastic scattering on nuclei is induced only at dimension six. This naturally explains the prominence of endothermic scattering compared to its elastic counterpart. We determine the parameter space compatible with the observed dark matter abundance and scrutinize the event rate and signal shape for scattering on xenon. Our results demonstrate that the observation of a single $E_R=248\pm 46$ keV nuclear recoil event in LZ can be accommodated by thermally produced dark matter in a leptophilic dark sector.

</details>

### [Lower Bound on the Lightest Neutrino Mass with Resonant Neutrino Self-Interactions](https://arxiv.org/abs/2611.34213)
*Shao-Feng Ge, Joao Paulo Pinheiro, Shaoyang Qin et al.* · `hep-ph` · arXiv:2611.34213v1 · relevance 0.16

- **In one sentence**: The paper proposes using resonant s-channel scattering of ultra-high-energy astrophysical neutrinos off the cosmic neutrino background, mediated by a roughly 1 MeV scalar, to derive a lower bound on the lightest neutrino mass by comparing simulated event spectra with IceCube HESE 7.5-year data.
- **In plain words**: Neutrinos are tiny, nearly massless particles that pass through almost everything, and we still do not know the mass of the lightest one. This paper proposes a way to probe that mass by looking at very high-energy neutrinos from space that might briefly interact with the faint sea of low-energy neutrinos left over from the early universe. The authors simulate what IceCube, a neutrino detector at the South Pole, should see under this scenario and compare it with its observed events to get a lower limit on the mass.
- **Why it matters**: Pinning down the neutrino mass scale matters for particle physics and cosmology, and this offers a new route that relies on neutrino self-interactions rather than standard laboratory or cosmological measurements. The text does not indicate how strong or robust the resulting bound is relative to existing limits, so its significance should be judged after checking the full paper.
- **Background needed**: - Neutrinos come in three types (flavors) and have small masses; only mass differences are well measured, so the absolute mass of the lightest one is unknown.
- The cosmic neutrino background is a relic sea of low-energy neutrinos from the early universe.
- An s-channel resonance is a sharply enhanced interaction that occurs when the energy of the colliding system matches a specific intermediate particle's mass.
- A scalar mediator is a hypothetical light, spin-zero particle that carries the interaction between neutrinos.
- Transport equations describe how particle populations change as they travel and interact; "regeneration" terms account for particles reappearing from interactions.
- IceCube HESE is a catalog of high-energy starting events recorded by the IceCube detector.
- Neutrinos and anti-neutrinos are evolved together here, which is what the "double" transport equations refer to. · level: research-level

<details><summary>Original abstract</summary>

We show the possibility of using the resonant $s$-channel scattering of ultra high energy astrophysical neutrinos with the low energy cosmic neutrino background to put a lower bound on the lightest neutrino mass. This can be realized and illustrated by neutrino self-interactions with a light scalar mediator of $\mathcal O(1)$ MeV mass. After analyzing the kinematics and cross section features of the $s$-channel resonance, we derive from first principles the double transport equations with double regeneration terms for the coupled evolution of neutrinos and anti-neutrinos. The simulated event spectrum is then compared with the HESE 7.5 year data observed at IceCube to give a clear lower bound on the lightest neutrino mass.

</details>

## Nuclear physics

### [Introducing Parton-Level Fluctuations in the TRENTo-Sea Model](https://arxiv.org/abs/2611.33662)
*Jacob Reinach, Andreas Kirchner* · `nucl-th` · arXiv:2611.33662v1 · relevance 0.11

- **In one sentence**: The paper extends the TRENTo-Sea initial-condition model for heavy-ion collisions by sampling quark and gluon momentum fractions from nuclear parton distribution functions, using perturbative QCD parton-level collisions with an infrared damping scale tuned to proton-proton cross sections.
- **In plain words**: When heavy atomic nuclei are smashed together at high energy, the hot droplet they form starts from a lumpy, uneven shape set by the tiny particles inside each proton and neutron. This paper builds a model that takes those inner particles' sharing of momentum from measured nuclear data, instead of only fitting the lumpiness to experimental results. The authors report that the model matches a standard measure of the droplet's shape (ε2) in most collisions, though not in the most head-on ones.
- **Why it matters**: Knowing how lumpy the starting point is matters for reading the shape and flow measured in heavy-ion experiments, so a model constrained by independent nuclear data is a useful cross-check. The authors say it may help future work on correlations between soft and hard particles and on comparing different nuclear parton distribution sets, though the text does not show these outcomes.
- **Background needed**: - Heavy-ion collisions: nuclei smashed together to make a brief, very hot, dense droplet of quark-gluon matter.
- Initial conditions: the lumpy starting geometry of that droplet, which later expands and flows.
- Eccentricity ε2{2}: a number describing how elliptical (non-round) the droplet's shape is, averaged over collisions.
- Partons: the quarks and gluons inside protons and neutrons.
- Parton distribution functions (PDFs): measured tables giving how much momentum fraction each parton type typically carries; nuclear PDFs (nPDFs) are versions for bound nuclei.
- Perturbative QCD: calculation method for strong-force interactions at high energy.
- Infrared regulator: a cutoff that keeps low-energy calculations finite; here tuned to proton-proton data.
- TRENTo: an existing parametric model of initial conditions that this work extends. · level: research-level

<details><summary>Original abstract</summary>

A variety of experimental and theoretical data suggest that initial condition models for heavy-ion collisions contain a degree of sub-nucleonic fluctuations. While current models fit the number and size of these fluctuations to data, we use nuclear parton distribution functions to constrain sub-nucleonic structure and fluctuations in TRENTo-Sea, an extension of TRENTo. Sampling the momentum fraction distributions of quarks and gluons in heavy ions, we use perturbative quantum chromodynamics to collide nuclei at the parton level, and we introduce an infrared center-of-momentum damping scale which is tuned to proton-proton cross sections. We find that our model successfully reproduces the $\varepsilon_2\{2\}$ of data-calibrated models except in central collisions, and an analysis of the power spectrum and granularity of the pre-equilibrium fireball shows that the number of low-$x$ partons in a nucleon has a significant effect on the local transverse geometry. Our model is largely insensitive to variations of the infrared parameters, as such changes are absorbed into the calibration of the infrared regulator. We expect that this work will aid future research on soft-hard correlations and constraining different nPDF sets.

</details>

### [Microscopic Approach to Neutron Elastic and Inelastic Cross Sections](https://arxiv.org/abs/2611.34752)
*Ibrahim Abdurrahman, Chloe Hebborn, Filomena Nunes et al.* · `nucl-th` · arXiv:2611.34752v1 · relevance 0.08

- **In one sentence**: The paper builds a shell-model-based S-matrix framework for low-energy neutron elastic and inelastic scattering on 20Ne, using 21Ne resonance states and spectroscopic amplitudes, and compares the resulting cross sections, level densities, partial widths and Shannon entropy against ENDF evaluations and GOE predictions.
- **In plain words**: Nuclear reactions, where a neutron hits an atomic nucleus and bounces off or knocks it into an excited state, are usually described by separate models for different energy ranges, and those models lean on fitted inputs. This paper tries to describe these low-energy neutron reactions in one framework that starts from a detailed quantum calculation of the nucleus's structure, using neon-20 as a test case. The authors report that the method qualitatively reproduces the standard evaluated neon-20 cross-section data.
- **Why it matters**: Reliable neutron reaction data matter for reactor design and for modeling how elements form in stars, and reducing reliance on fitted inputs could make predictions more trustworthy where measurements are scarce. The text only shows a qualitative match for one nucleus and says the framework is planned to be extended, so its broader value is not yet established.
- **Background needed**: - Cross section: a measure of how likely a reaction is, expressed as an effective target area.
- Elastic vs. inelastic scattering: the neutron bounces off the nucleus leaving it in its ground state (elastic) or leaving it excited (inelastic).
- Shell model: a quantum model that computes a nucleus's energy levels from its nucleons arranged in shells.
- Resonance: a short-lived, highly excited state of the combined neutron-plus-nucleus system.
- Level density and partial width: how many energy states lie in a range, and how strongly a state decays through a given channel.
- S-matrix: a mathematical object encoding all scattering outcomes of a reaction.
- ENDF: a standard library of evaluated nuclear data.
- Shannon entropy and GOE: an information measure of spread, and a random-matrix benchmark for the statistics of quantum energy levels. · level: research-level

<details><summary>Original abstract</summary>

Depending on the nuclei involved and the beam energies, reaction timescales differ tremendously. Today, distinct models are often used to describe each timescale, relying on phenomenological inputs, such as level densities or partial-widths, which limits their predictive power. This work aims to address this issue by providing a unified description of low-energy neutron elastic and inelastic reaction channels starting from microscopic predictions of the structure of mid-mass nuclei. The goal is to build a framework that is general enough to span the different reaction regimes while remaining anchored in microscopic theory. For illustration purposes, this work focuses on reactions $n+^{20}$Ne to the elastic and inelastic channels. The S-matrix is build from shell model predictions of resonances states and their spectroscopic amplitudes for $^{21}$Ne, using two different approximations of the single-particle asymptotics. Then, the shell-model predictions for the level density and single-particle partial widths are analyzed and the final cross sections are compared with evaluated ones. This method qualitatively reproduces the ENDF evaluation for the $^{20}$Ne$(n,el)$ and $^{20}$Ne$(n,n')$ cross sections. The present study also compares the Shannon entropy obtained from this model to the Gaussian Orthogonal Ensemble (GOE). In the future, the framework will be extended to include more complex reaction channels, such as two-nucleon and gamma channels, enabling more accurate predictions of neutron-induced reactions such as those of astrophysical interest.

</details>

## Quantum information and computing

### [A Realistic End-to-End Runtime Crossover Estimation for Quantum-Enhanced Training of Large-Scale Machine Learning Models](https://arxiv.org/abs/2611.33454)
*Maximilian Alexander Wolf, Alona Sakhnenko, Florian Geissler et al.* · `quant-ph` · arXiv:2611.33454v1 · relevance 0.13

- **In one sentence**: The paper gives realistic end-to-end resource estimates (data loading, computation, and readout) for training a linearized neural network with a quantum linear solver, and locates the problem sizes where a quantum approach could beat classical methods.
- **In plain words**: Quantum computers are often promised to speed up machine learning, but those promises usually compare only the core mathematical step and ignore the cost of getting data in and results out. This paper takes a proposed quantum method for training a simplified neural network and estimates the full cost of running it, across three increasingly realistic scenarios. It finds that the quantum approach only pulls ahead over classical computing for very large problems, long computation times, and very narrow output requirements.
- **Why it matters**: It is a sober check on a claimed quantum speedup for machine learning, showing how hidden engineering costs can erase asymptotic advantages. It may matter to anyone judging when quantum hardware could be useful for industrial AI, though the text does not say how close current hardware is to these regimes.
- **Background needed**: - Machine learning training: adjusting a model's parameters to fit data, which typically involves solving large systems of equations.
- Quantum linear solver: a quantum algorithm for solving systems of linear equations, whose speed claims are usually stated in asymptotic (large-scale, scaling-law) terms.
- Asymptotic complexity: how cost grows as problem size grows, ignoring constant factors and overheads.
- Data access / readout: the cost of loading classical data into a quantum computer and extracting answers back out, which can dominate runtime.
- Sparsity: the fraction of zero entries in a matrix; sparser matrices are usually cheaper to handle.
- Crossover point: the problem size at which a quantum method becomes faster than the best classical method.
- Quantum utility: a quantum computer doing useful work better than classical alternatives in practice. · level: research-level

<details><summary>Original abstract</summary>

Machine Learning (ML) is one promising application domain for Quantum Computing (QC) speedups, but asymptotic complexity considerations often mask the actual engineering costs of actual end-to-end workflows. For the use case of training a linearized Neural Network with a Quantum Linear Solver, a provably favorable quantum scaling has been suggested. We present realistic resource estimates for this problem, accounting for data access, computation, and readout. Our analysis examines three increasingly complex benchmarking scenarios, under distinct sparsity-scaling assumptions, thereby enabling progressively more realistic resource estimates. We identify crossover regimes relative to classical methods and find that crossover points emerge only for very large problem sizes, long computation times, and highly restrictive output requirements. This work provides a blueprint for evaluating quantum-enhanced ML algorithms under realistic hardware constraints and help identifying the bottlenecks that must be overcome to approach industrial quantum utility.

</details>

### [Efficient Quantum Algorithm for the Generalised Geography Game](https://arxiv.org/abs/2611.33853)
*Mriganka Sandilya, Shibdas Roy* · `quant-ph` · arXiv:2611.33853v1 · relevance 0.13

- **In one sentence**: The paper claims a bounded-error quantum polynomial-time (BQP) algorithm for the Generalized Geography Game, a PSPACE-complete problem, running in O(N^2/ε^6) time with ε = O(1/poly(N)).
- **In plain words**: The paper looks at a two-player game played on a network of arrows, where players take turns moving a marker along arrows without revisiting a spot, and the question is who can force a win. Deciding this in general is known to be very hard for ordinary computers. The authors describe a quantum computing method that they say solves this decision problem in polynomial time, with a small allowed error rate.
- **Why it matters**: If correct, it would be a notable claim, since a PSPACE-complete problem being solvable in BQP would bear on how quantum computers relate to classical complexity classes. The summary alone does not show the method or its checks, so the claim should be read cautiously until independent review.
- **Background needed**: - Directed graph: dots (vertices) joined by one-way arrows (edges).
- Combinatorial game: a two-player game with perfect information and no chance, where the question is who wins with best play.
- PSPACE-complete: a class of problems believed to need huge amounts of memory or time on ordinary computers; a hard benchmark problem.
- BQP: problems a quantum computer can solve in polynomial time with bounded error (a small chance of being wrong).
- Bounded error and ε: the allowed chance of a wrong answer; here it is set to shrink polynomially with input size N.
- Quantum algorithm: a procedure that uses quantum-mechanical effects such as superposition and interference. · level: research-level

<details><summary>Original abstract</summary>

The Generalized Geography Game ($GGG$) is a two-player combinatorial game played on a directed graph, where players alternately move a token along edges without revisiting previously visited vertices. In the existing literature, determining whether an arbitrary position in a graph is a winning position for either player is a well-known $PSPACE$-complete decision problem. Certain formulations of $GGG$ have been shown to fall outside the $PSPACE$-complete complexity class. While $PSPACE$-complete problems are believed to take exponential time for classical computation, quantum computation offers new possibilities. In this work, we present a bounded-error quantum polynomial-time ($BQP$) algorithm for solving the $GGG$ problem. The proposed algorithm runs in time $O(N^{2}/\epsilon^{6})$, which is polynomial in the input size $N$, and achieves bounded error with $\epsilon = O(1/\mathrm{poly}(N))$. This result demonstrates the potential of quantum algorithms to efficiently solve combinatorial game problems that are traditionally considered computationally hard in the classical setting.

</details>

## Optics and atomic physics

### [Ferroionic CuCrP2S6 Integrated Silicon Photonics for Neuromorphic Computing](https://arxiv.org/abs/2611.33954)
*Ghada Dushaq, Srinivasa R. Tamalampudi, Mahmoud Rasras* · `physics.optics` · arXiv:2611.33954v1 · relevance 0.09

- **In one sentence**: The paper integrates the layered ferroionic material CuCrP2S6 onto silicon microring resonators and shows that electrical pulses shift the optical resonance via mobile copper-ion redistribution, giving volatile and nonvolatile optical memory that can mimic a leaky integrate-and-fire neuron.
- **In plain words**: Researchers built a tiny light-based circuit on a silicon chip and coated it with a special layered crystal whose copper ions can be moved by electric pulses. Each pulse nudges the color at which the chip's ring resonates, and that shift builds up with repeated pulses, partly fading over time and partly staying put. The authors use this behavior to show a light-based version of a simple artificial neuron that adds up inputs, leaks some away, and fires once a threshold is crossed.
- **Why it matters**: Optical computing that stores and accumulates information without constant power could be useful for energy-efficient neuromorphic (brain-inspired) hardware. The text reports device-level demonstrations only; its broader significance for practical photonic computing is not established by the text shown.
- **Background needed**: - Microring resonator: a tiny circular waveguide on a chip that transmits light most strongly at specific wavelengths; shifts in that wavelength are the readout.
- Silicon photonics: using light-guiding structures fabricated on silicon chips, as in electronics manufacturing.
- Van der Waals material: a crystal made of stacked atomic sheets that can be integrated onto other surfaces.
- Ferroionic: a material where mobile ions (here copper) can be moved by an electric field and stay in place after the field is removed, giving memory.
- Volatile vs. nonvolatile memory: volatile states fade without power; nonvolatile states persist.
- Leaky integrate-and-fire neuron: a standard simplified model of a neuron that accumulates input, slowly loses charge, and produces an output spike when a threshold is reached.
- Picometer (pm) and nanometer (nm): units of wavelength shift; 1000 pm = 1 nm. · level: research-level

<details><summary>Original abstract</summary>

Neuromorphic photonic computing calls for optical states that combine stimulus accumulation, spontaneous relaxation, and nonvolatile state retention without continuous power dissipation. Here, we demonstrate a ferroionic photonic platform by integrating layered van der Waals CuCrP2S6 onto silicon microring resonators using a back-end integration process. Electrical pulsing produces unidirectional blue shifts in the optical resonance, consistent with field-driven redistribution of mobile Cu ions and giving rise to a history-dependent optical response. The resulting optical state is strongly pulse dependent, exhibiting both volatile and nonvolatile components. A short 20-pulse excitation produces an initial 70 pm resonance shift that relaxes toward baseline within approximately 60 s, with a volatile relaxation time constant of 27-29 s. In contrast, after 1000 pulses, an initial 0.27 nm resonance shift relaxes to a persistent 0.13 nm nonvolatile state that is retained for at least 24 h. Repeated 6 V electrical pulses produce a progressive resonance shift over 1000 cycles, demonstrating cumulative optical integration. A fixed-wavelength readout converts the accumulated resonance shift into a thresholded optical response, with the normalized transmission remaining above the selected threshold through 600 pulses and falling below it at the 800-pulse state. These dynamics realize the basis for a leaky integrate-and-fire photonic neuron, where the pulse-dependent ionic response provides integration, spontaneous relaxation supplies a passive leak, persistent states provide nonvolatile memory, and fixed-wavelength readout provides an optical threshold response.

</details>

### [Statistical analysis of crossing beam speckle fields](https://arxiv.org/abs/2611.33483)
*Ian D. Min-Roberts, Wojciech Rozmus, Pierre A. Michel* · `physics.optics` · arXiv:2611.33483v1 · relevance 0.08

- **In one sentence**: A statistical treatment of speckle patterns from two or more crossing laser beams, deriving effective speckle size from intensity-field curvature, an asymptotic Kac-Rice abundance formula checked by Monte Carlo simulation, and an extension to many beams that yields the spectral density of laser-driven electron density fluctuations.
- **In plain words**: When several laser beams cross in a plasma, their overlap creates a grainy pattern of bright and dark spots called speckles. This paper builds a statistical description of how big these spots are and how many there are, and checks the counting formula against computer simulations, which agree well. It then applies the approach to a four-beam arrangement and to a general many-beam case, and reports that spreading the beams farther apart lowers the expected scattering of light from the brightest spots.
- **Why it matters**: The work is aimed at laser fusion research, where speckle patterns can drive unwanted light scattering that reduces the efficiency of compressing fuel. The text supports the claim that wider beam separation reduces expected scattering from saturated speckles in the quad configuration, but the text alone does not show how directly these results carry over to any particular experiment.
- **Background needed**: - Speckle: a random pattern of bright and dark spots produced when coherent laser light interferes.
- Intensity field: how bright the light is at each point in space.
- Stimulated Brillouin scattering: a process in which laser light scatters off sound-like waves in plasma, losing energy and reducing the laser's useful effect.
- Polarization smoothing: a technique that mixes light polarizations to make the laser intensity pattern more uniform.
- Kac-Rice formula: a standard probability tool for counting how often a random smooth function crosses a level, here used to count speckles.
- Monte Carlo simulation: repeated random computer sampling used to test a theory.
- Spectral density: a description of how strongly fluctuations occur at each frequency or wavelength. · level: research-level

<details><summary>Original abstract</summary>

Building on the statistical analysis of single beam speckles, this paper develops a statistical description of speckle fields formed by crossing laser beams. A formal definition of individual speckles and their domains allows us to quantify the effective size and abundance of speckles. For two crossing beams, the effective speckle size is derived from the local curvature of the intensity field, and the expected speckle abundance is found asymptotically with the Kac-Rice formula. Monte Carlo simulations of speckle abundance show excellent agreement with the theoretical abundance formula. The two beam speckle analysis is then applied to a symmetric quad beam configuration motivated by polarization smoothing and demonstrates that increasing the separation between beams reduces expected stimulated Brillouin scattering reflectivity from saturated speckles. The statistical model is then extended to an arbitrary number of beams using a coordinate free formulation to obtain the spectral density of laser driven electron density fluctuations.

</details>

## Fluids and plasma

### [AI Buckingham: Agentic Discovery of Dimensionless Scaling Laws Across Physical Regimes](https://arxiv.org/abs/2611.33961)
*Ao Cheng, Lei Zhang, Guowei He* · `physics.comp-ph` · arXiv:2611.33961v1 · relevance 0.08

- **In one sentence**: AI Buckingham is an LLM-driven agentic framework that uses mutual information and regime clustering to pick dominant dimensionless groups from problem descriptions and data, applied to ten systems including turbulent drag over rough surfaces.
- **In plain words**: This paper describes a computer system that tries to find the simplest meaningful way to group the variables in a physics problem, so that many experiments can be compared on one scale. A language model plans the work and calls mathematical and numerical tools to check units, sort data into physical regimes, and rank which groupings matter most. The authors report that it recovers known similarity groupings across ten systems and suggests better ways to describe surface roughness for estimating friction drag in turbulent flow.
- **Why it matters**: Choosing the right dimensionless groups is a long-standing step in engineering and fluid mechanics, and automating it could speed up modelling. The text does not show how well the approach performs against existing methods or how far the roughness improvement generalises, so its practical value remains to be tested.
- **Background needed**: - Dimensionless group: a ratio of physical quantities with no units (for example, the Reynolds number, which compares inertia to viscous forces in a flow).
- Dimensional analysis (Buckingham Pi theorem): a classical method that says which unit-free combinations are possible, but not which ones matter most.
- Regime: a range of conditions in which one physical behaviour dominates, so the same relationship may change between regimes.
- Mutual information: a statistical measure of how much knowing one quantity tells you about another, used here to rank groups.
- Equivalent sand-grain roughness: a standard way to summarise a rough surface's effect on drag using a single roughness length.
- Large language model (LLM) agent: a language model that plans steps and calls external tools. · level: research-level

<details><summary>Original abstract</summary>

Classical dimensional analysis defines admissible dimensionless representations but does not determine which combinations capture the dominant physical dependence, whether it changes across physical regimes, or when dependent-variable rescaling is required. We present AI Buckingham, an agentic framework for autonomous dimensionless discovery from natural-language descriptions of physical problems and observational data. It couples reasoning and planning by a large language model (LLM) with predefined symbolic and numerical tools. Literature-based knowledge retrieval supports dimensional checking, gradient-based clustering identifies physical regimes, and mutual information provides an objective, reparameterization-invariant criterion for identifying dominant dimensionless groups. Explicit numerical criteria determine the group count and assess simplification. Across ten physical systems spanning fluid dynamics, magnetohydrodynamics, thermal convection and additive manufacturing, AI Buckingham recovers established similarity representations and resolves regime-dependent scalings. For the longstanding challenge of predicting turbulent drag on rough surfaces, it identifies informative reparameterizations of surface statistics that improve equivalent sand-grain roughness estimates for engineering-oriented drag modelling.

</details>

### [Butterfly Effect in Kinetic Plasma Turbulence](https://arxiv.org/abs/2611.33357)
*Louis Henderson, Vladimir Zhdankin* · `physics.plasm-ph` · arXiv:2611.33357v1 · relevance 0.07

- **In one sentence**: Using particle-in-cell simulations of driven kinetic plasma turbulence, the paper shows that a localized perturbation, down to a single particle, is exponentially amplified and fully decorrelates paired simulations within a few dynamical times, and it builds an analytical model for the early-time growth.
- **In plain words**: The paper asks how strongly a tiny nudge can change the future of a turbulent, electrically charged gas (a plasma). The authors ran pairs of computer simulations that were identical except that one had a tiny change to a single particle at the start. They found that this small difference spread outward and grew quickly, until the two simulations looked statistically unrelated.
- **Why it matters**: It gives a detailed, quantitative picture of the "butterfly effect" (sensitive dependence on initial conditions) in a collisionless plasma, which bears on how predictable such systems are. The text does not go beyond this, so its wider implications are the authors' own suggestion rather than something shown here.
- **Background needed**: - Plasma: a hot gas of charged particles, common in space and fusion devices.
- Collisionless: particles interact mainly through electric and magnetic fields, not by bumping into each other.
- Turbulence: chaotic, swirling motion across many scales.
- Particle-in-cell (PIC) simulation: a computer method that tracks many particles and the fields they produce on a grid.
- Butterfly effect: tiny differences in starting conditions grow into large differences later.
- Decorrelated: the two runs no longer match statistically, even though they started almost the same.
- Plasma beta: ratio of gas pressure to magnetic pressure; temperature sets how close particles move to light speed (sub- vs ultra-relativistic).
- Machine precision: the smallest difference a computer can represent; perturbations smaller than this cannot be tracked. · level: research-level

<details><summary>Original abstract</summary>

The butterfly effect is a fundamental process in chaotic systems, but it has not previously been characterized in detail for a collisionless turbulent plasma. In this work, we apply particle-in-cell (PIC) simulations of driven turbulence to study the emergence of the butterfly effect from a small initial perturbation to the simulated particles. In particular, we compare pairs of (baseline and perturbed) simulations that differ only by a localized initial perturbation (down to the single-particle level). We find that the effect of the localized perturbation spreads radially throughout the PIC simulation, causing a difference between each simulation pair that is exponentially amplified over time within the affected region. The fields, including the electric current density, eventually become statistically decorrelated. We construct an analytical model combining spatial expansion with exponential amplification to approximate the early-time evolution. Varying the initial perturbation primarily affects the early-time evolution, while having little effect on the final, decorrelated state. We describe parameter scans with varying plasma beta and temperature (covering sub-relativistic and ultra-relativistic regimes). Our results show that remarkably small perturbations will grow to decorrelate each pair of simulations within a few dynamical times; the imposed perturbation can no longer be resolved once it falls below the numerical precision floor set by the machine precision. These results confirm that the butterfly effect is very strong and robust in a collisionless plasma, with implications for the predictability of turbulent plasma systems.

</details>

## Biological physics

Nothing notable this time.

## Climate, atmosphere and Earth

### [Weak buoyancy and cold lithospheres decouple interior melting from seafloor volcanism on icy ocean worlds](https://arxiv.org/abs/2611.33478)
*Nahiz Hestaphin* · `astro-ph.EP` · arXiv:2611.33478v1 · relevance 0.05

- **In one sentence**: A modelling study linking melt segregation, nonlinear rock creep, fracture flow and crystallisation to ask whether magma generated deep in icy ocean worlds such as Europa can reach the seafloor, and how that depends on thermal history.
- **In plain words**: The paper asks whether magma made deep inside an icy moon like Europa can push through cracks in the ice-covered rock and reach the seafloor before it freezes. The authors built a coupled model of melt movement, slow rock deformation, fracture flow and cooling, and ran hot and cold scenarios. They report that the answer depends strongly on grain size, cooling of the surrounding rock, and how the flow path is renewed over time.
- **Why it matters**: Seafloor volcanism on ocean worlds could matter for whether their oceans exchange chemistry with the surface and for habitability, but the text is a model study and its conclusions depend on assumed parameters. Its main claim, that seafloor access is history-dependent and decoupled from deep melt production, is a modelling result rather than an observed one.
- **Background needed**: - Icy ocean worlds: moons such as Europa with a liquid water ocean under an ice shell, with silicate rock on the seafloor.
- Melt segregation: the process by which liquid magma separates from the solid rock it forms in.
- Fracture flow: magma moving through narrow cracks; the 'opening threshold' is the pressure needed to pry a crack open.
- Solidus and crystallisation: the temperature below which rock is fully solid, and the freezing of magma as it cools.
- Relaxed pressure: the pressure left after slow rock creep has evened out stresses over time.
- Enthalpy margin: how much heat a magma holds above its freezing point, which sets how long it stays liquid.
- Terrestrial comparison: Earth's crustal magma pathways are used in the text as a reference for the scale of flow needed. · level: research-level

<details><summary>Original abstract</summary>

On icy ocean worlds, deep silicate melting can generate sufficient pressure to open fractures while magma freezes before reaching the ocean. We identify a coupled transport regime by linking finite melt segregation and nonlinear rock relaxation to fracture flow, crystallisation and the ice-loaded ocean boundary. In a hot Europa endmember, increasing grain size from 1 to 10 mm raises relaxed excess pressure from 5.55 kPa to 10.2 MPa, overcoming the inherited-fracture opening threshold despite weak buoyancy. For the same 100 m strike and 0.5 m aperture, the cold first-fill rate required by heat balance increases from 0.17-0.69 m3 s -1 over terrestrial crustal distances of 1.1-4.5 km to 15-29 m3 s -1 across 89-171 km Europa paths, far above the self-supplied flow. Higher ice-ocean pressure further reduces the enthalpy margin of near-solidus magma in the adopted basalt phase law. During approximately 5 kyr of dormancy, the collector pressure returns to its relaxed value, while upper-path walls cool to 275-282 K and the magma path loses liquid connectivity. In two focused Europa histories with mechanically supported pathways, delivery of 0.005 km3 of magma over 0.1 Myr requires 14-27 km3 of sacrificed magma-equivalent preparation material. Weak gravity, extensive cold rock and a pressurised ocean thus make seafloor access a history-dependent process governed by thermal connectivity and its renewal, decoupling recurrent volcanism from melt production at depth.

</details>

### [Skysail: Altitude Control of Long-Duration Weather Balloons by Extracting Work from Wind Shear](https://arxiv.org/abs/2611.33882)
*Michal Adamkiewicz, Andrey Sushko* · `physics.ao-ph` · arXiv:2611.33882v1 · relevance 0.05

- **In one sentence**: A control system for long-duration zero-pressure weather balloons that uses a pitch-controlled wing on a tether, 450 m below the balloon, to convert wind-shear airflow into vertical forces for repeated atmospheric profiling with reduced reliance on ballast and venting.
- **In plain words**: Weather balloons that sample the air at many heights run out of ballast and lifting gas after a limited number of ascents and descents. This paper describes a small wing hung on a line below the balloon that uses the difference in wind speed between two heights (wind shear) to push the system up or down. In flight tests, the wing completed eleven up-and-down profiles over 43 hours without dropping ballast or venting gas, and a separate eight-day flight completed 24 profiles.
- **Why it matters**: Each balloon can currently collect only as many atmospheric profiles as its consumables allow, so a way to extend that count could make long-duration soundings cheaper and longer-lived. The text reports flight results over two years, but it does not compare the approach against standard balloon operations in detail, so its wider impact is not yet established.
- **Background needed**: - Zero-pressure balloon: a balloon open at the bottom so its gas expands and vents as it rises, keeping pressure near outside air; it floats at roughly constant altitude once balanced.
- Ballast and venting: standard ways to change altitude by dropping weight or releasing lifting gas; both are finite.
- Wind shear: the change in wind speed or direction with height.
- Profiling: taking measurements at many altitudes as the balloon moves up and down through the air.
- Angle of attack and pitch: the wing's tilt relative to the airflow; changing it changes the lift force, which is how the wing's vertical push is controlled.
- Tether: the line connecting the wing to the balloon, here 450 m long. · level: intermediate

<details><summary>Original abstract</summary>

Long-duration weather balloons collect repeated atmospheric profiles by venting lifting gas and dropping ballast, but these finite consumables limit the number of profiles each balloon can obtain. We present an altitude-control system that extracts mechanical work from atmospheric wind shear. A small wing suspended 450 m below a zero-pressure balloon experiences relative airflow from the wind velocity difference between the two altitudes. Controlling the wing's pitch produces aerodynamic forces that drive ascent and descent. We develop a model for sizing the system, a lightweight aerodynamic governor for tether deployment, and a control architecture for altitude holding and repeated profiling. Flight experiments conducted over two years accurate control of vertical motion. During a 43-hour interval, the system completed eleven profiles and accumulated 53 km of vertical travel without releasing ballast or venting gas. A separate eight-day flight completed 24 profiles exceeding 1 km in vertical extent, accumulating 159 km of vertical travel. Control authority depends on the available wind shear, with conventional ballast and vent actuation retained for trim and fallback control. These results demonstrate that atmospheric wind shear can sustain repeated balloon profiling while reducing dependence on consumable actuators.

</details>

## Cosmology

### [Acoustic Priors from the Latest Cosmic Microwave Background Data](https://arxiv.org/abs/2611.33334)
*Kushal Lodha, Jun-Qian Jiang, Purba Mukherjee et al.* · `astro-ph.CO` · arXiv:2611.33334v1 · relevance 0.15

- **In one sentence**: Using a physics-based "acoustic prior" that separates early-Universe signals in the CMB from late-time lensing and ISW effects, this paper updates CMB constraints on the acoustic scale and physical densities with Planck PR4, ACT DR6 and SPT-3G D1 data, and examines how the choice of lensing-smoothing treatment affects tensions with DESI DR2 BAO.
- **In plain words**: The paper looks at the faint pattern of hot and cold spots in the leftover light from the early Universe (the cosmic microwave background). It separates the part of that pattern set by conditions right after the Big Bang from the part distorted by gravitational lensing and other effects on the way to us. Using combined data from several telescopes, the authors update their estimates of basic cosmic ingredients and find that treating the lensing smoothing differently noticeably reduces the reported mismatch between the CMB, galaxy-distance measurements (DESI BAO) and models where dark energy changes over time.
- **Why it matters**: Dark energy and the expansion history of the Universe are active questions, and the size of any mismatch between datasets depends on modelling choices like this one. The paper shows that a single modelling assumption shifts the significance of a reported tension from about 3σ to about 1.9σ, so the result is sensitive to method rather than settled. The text does not say how the field will weigh these choices.
- **Background needed**: - The cosmic microwave background (CMB): relic light from about 380,000 years after the Big Bang; its patterns encode early-Universe physics.
- Acoustic peaks: regularly spaced bumps in the CMB power spectrum caused by sound waves in the early plasma.
- Gravitational lensing: light bent by intervening matter, which smooths the CMB peaks and leaves its own signature.
- ISW effect (integrated Sachs-Wolfe): a late-time change in CMB light caused by evolving gravitational fields, often linked to dark energy.
- Baryon acoustic oscillations (BAO): a preferred separation scale in galaxy distributions, used as a cosmic ruler; DESI DR2 is a recent survey.
- ΛCDM: the standard model of cosmology (cold dark matter plus a cosmological constant); w0wa CDM is an extension where dark energy evolves.
- Sigma (σ): a measure of how unlikely a difference is if the standard model is correct; about 3σ is a notable but not decisive tension.
- Planck, ACT, SPT, WMAP: CMB telescopes and experiments whose data are combined here. · level: research-level

<details><summary>Original abstract</summary>

We revisit the physics of the acoustic peaks and illustrate how early-Universe information in the cosmic microwave background (CMB) can be disentangled from late-time signatures imprinted by gravitational lensing and the integrated Sachs-Wolfe (ISW) effect. Applying this separation to Planck PR4, ACT DR6, and SPT-3G D1 temperature and polarization data combined with the joint lensing reconstruction, we update the model-independent constraints on the angular acoustic scale and the physical densities, $100\theta_*=1.04100\pm0.00021$, $\omega_{\rm b}=(2.2440\pm0.0099)\times10^{-2}$, and $\omega_{\rm bc}=0.1410\pm0.0011$. These constraints are consistent with the previous Planck PR4-only analysis and remain stable for extended late-time cosmologies beyond $\Lambda$CDM. Adding ACT DR6 to the combination favors a higher $\omega_{\rm b}$ and, through their correlation, a higher primordial tilt $n_{\rm s}$ than PR4 alone. The reconstructed lensing spectrum exceeds that of $\Lambda$CDM, with two features near $L\simeq50$ and $L\sim10^3$, and the excess is reduced when WMAP replaces the Planck primary spectra. Marginalizing over the lensing-induced peak smoothing, rather than tying it to the late-time model, lowers the preference of the CMB and DESI DR2 baryon acoustic oscillations (BAO) for $w_0w_a$CDM over $\Lambda$CDM from $3.0\sigma$ to $1.9\sigma$, or from $3.2\sigma$ to $2.4\sigma$ when Union3.1 supernovae are added. We further use the acoustic prior to predict BAO distances from CMB data alone under several late-time expansion histories, testing their consistency with DESI measurements assuming standard pre-recombination physics.

</details>

### [No Cluster Left Behind I: Joint Mass Calibration for Dark Energy Survey and South Pole Telescope Clusters](https://arxiv.org/abs/2611.33522)
*C. Zhou, A. N. Salcedo, S. Grandis et al.* · `astro-ph.CO` · arXiv:2611.33522v1 · relevance 0.13

- **In one sentence**: A joint statistical model that combines Dark Energy Survey optical richness and weak-lensing data with South Pole Telescope Sunyaev-Zel'dovich signals to calibrate galaxy cluster masses, including clusters seen by only one survey.
- **In plain words**: Galaxy clusters are the largest gravitationally bound objects in the universe, and knowing their masses accurately helps test theories of dark energy. This paper describes a modeling method that pools cluster data from two different surveys, including clusters that only one survey detected, so that their masses can be estimated together. As a test, the authors combined optical data from the Dark Energy Survey with microwave signals from the South Pole Telescope.
- **Why it matters**: Optically found clusters are numerous but their mass estimates can be biased by chance alignments along the line of sight, while microwave-detected clusters are less affected but only capture the most massive ones. The text reports a roughly 20% bias in the lensing signal for richness-selected clusters and a bias from about -20% to zero depending on richness for clusters selected by both methods. The authors say the framework is scalable for next-generation surveys, but the text does not show how it performs beyond this pilot study.
- **Background needed**: - Galaxy clusters: groups of galaxies held together by dark matter; their number and mass depend on cosmology and dark energy.
- Richness: a count of galaxies in a cluster seen in optical light, used as a rough proxy for mass.
- Weak gravitational lensing: faint distortion of background galaxy shapes by a cluster's mass; used to measure mass directly.
- Selection bias: when the way objects are chosen for a sample skews the average measured property.
- Line-of-sight projection: unrelated structures lying along the same viewing direction that can look like part of a cluster.
- Sunyaev-Zel'dovich effect: a distortion of the cosmic microwave background caused by hot gas in clusters, detected by millimeter telescopes.
- Mass calibration: relating an observable (like richness) to true cluster mass. · level: research-level

<details><summary>Original abstract</summary>

Multiwavelength observations of galaxy clusters are among the most promising probes of the growth of structure and dark energy. Optically identified clusters have a high number density and can thus probe the halo mass function well into the group regime, but their weak-lensing mass calibration suffers from a selection bias induced by line-of-sight projection effects. Clusters detected via their intracluster medium (ICM) -- through X-ray emission or the thermal Sunyaev-Zel'dovich effect (SZe) -- are less affected by such selection biases, but current survey sensitivity restricts ICM-selected samples to high-mass systems. Previous multiwavelength analyses tend to limit to clusters with millimeter detections and thus to the high-mass population. In this paper, we propose a flexible modeling framework in which all clusters from multiwavelength surveys can be combined and modeled, even if they are detected in only one survey. As a pilot study, we jointly model richness and lensing of clusters from the Dark Energy Survey and the SZe signal from the South Pole Telescope. This approach yields precise cluster mass calibration while self-consistently constraining optical selection biases. We have found a $\sim$20% bias in the large-scale lensing signal of clusters selected by richness, and a bias ranging from $\sim-20$% at low richness to zero at high richness for clusters selected by both richness and SZe. Compared to current approaches, this framework is highly scalable and readily extensible, paving the way for the full utilization of multiwavelength cluster data in next-generation surveys.

</details>

## Galaxies

### [State of the UNIONS: Four Milky Way companions discovered in a systematic search for northern Local Group satellites](https://arxiv.org/abs/2611.34775)
*Simon E. T. Smith, Alan W. McConnachie, Thomas de Boer et al.* · `astro-ph.GA` · arXiv:2611.34775v1 · relevance 0.18

- **In one sentence**: Using gri photometry from the UNIONS northern sky survey, the authors report four new Milky Way satellites, two of which (Boötes VI and Draco III) are candidate ultra-faint dwarf galaxies pending chemodynamical follow-up, while UNIONS 2 and UNIONS 3 are too faint and compact to classify definitively.
- **In plain words**: Astronomers searched a large map of the northern sky for faint clusters of stars orbiting our Milky Way. They found four new small star systems. Two look like possible faint dwarf galaxies, and two are so dim and small that the paper cannot yet say what they are.
- **Why it matters**: Faint satellite galaxies are among the best tests of how much dark matter surrounds the Milky Way and of how many such small systems should exist. The paper says the faintest objects like these will turn up in growing numbers in upcoming wide-field surveys, but the classifications remain tentative.
- **Background needed**: - Milky Way satellites: small stellar systems that orbit our galaxy, ranging from dense star clusters to faint dwarf galaxies.
- Photometry: measuring object brightness through coloured filters (g, r, i here); colours help estimate distance and stellar age.
- Absolute magnitude (M_V): how bright an object really is, independent of distance; more negative means brighter.
- Half-light radius: the radius containing half the light, a measure of how spread out a system is.
- Ultra-faint dwarf galaxy: a very dim, dark-matter-dominated galaxy; distinguishing it from a dense star cluster usually needs spectroscopy to measure stellar motions and chemistry.
- Parsec (pc) and kiloparsec (kpc): astronomical distance units (about 3.26 light-years per parsec).
- Globular cluster: a dense, ancient ball of stars; used here as the comparison class. · level: research-level

<details><summary>Original abstract</summary>

We present four newly discovered Milky Way satellites from a systematic search through the $gri$ photometry from the Ultraviolet Near-Infrared Optical Northern Survey (UNIONS). Two of these satellites are likely ultra-faint dwarf galaxies that we have named Bo\"otes VI and Draco III. Both galaxy candidates are $\gtrsim 100$ kpc from the Galactic center and have absolute $V$-band magnitudes ($M_V$) of $-2.7^{+0.6}_{-0.5}$ and $-4.0\pm0.6$, respectively. Bo\"otes VI and Draco III have physical half-light radii ($r_{\rm h}$) of $\sim 50$ pc, or about twice as large as the most extended Milky Way globular clusters with similar luminosities. They are therefore candidate galaxies, though chemodynamical analyses will be needed to secure these classifications. We name the two other systems UNIONS 2 and UNIONS 3. They are extremely faint ($M_V = +0.4^{+0.6}_{-0.9}$ and $-0.7^{+0.6}_{-0.8}$) and compact ($r_{\rm h} = 5\,\pm\,1$ and $10^{+3}_{-2} pc), and zero giant stars are identified in either of their present-day stellar populations. Morphological measurements alone are not sufficient to assess the presence of dark matter in either system, so do not provide definitive classifications. We discuss the challenges in either detecting or refuting the presence of dark matter in UNIONS 2 and UNIONS 3, two systems that are archetypal of the faintest satellites that will be discovered in increasing numbers in upcoming wide-field surveys.

</details>

### [The role of hierarchy in Galactic molecular clouds](https://arxiv.org/abs/2611.33956)
*Kotora Sasaki, Nario Kuno, Hajime Fukushima et al.* · `astro-ph.GA` · arXiv:2611.33956v1 · relevance 0.16

- **In one sentence**: A statistical study of 13 Galactic massive star-forming regions, using FUGIN CO survey data and a non-binary dendrogram, compares hierarchical gas structures (trunks, internal leaves, isolated structures) and their low-mass star and clump formation efficiencies.
- **In plain words**: Stars form inside clouds of cold gas, and this paper asks how the gas in massive star-forming regions is nested, from large clumps down to smaller dense pockets. The authors sorted the gas in 13 regions of our Milky Way into large "trunks," the densest pieces inside them ("leaves"), and isolated pieces, then compared them. They report that leaves hold more dense, massive clumps than isolated pieces of similar size, without forming more low-mass stars.
- **Why it matters**: The results suggest that massive star formation depends on gas organized over scales larger than a single core, which bears on how massive stars and clusters form. The authors themselves note that the data come from a single epoch and constrain only structural differences, so the proposed accretion and fragmentation explanation remains an interpretation rather than a demonstrated mechanism.
- **Background needed**: - Molecular clouds: cold, dense gas in galaxies where stars are born.
- CO survey: observations of carbon monoxide, a molecular tracer used to map cloud gas and its motion along the line of sight.
- Dendrogram: a tree-like map that nests gas structures inside larger ones, like branches within a trunk.
- Trunks, leaves: trunks are large connected gas structures; leaves are the densest substructures within them.
- Star formation efficiency: the fraction of gas that ends up in stars or dense clumps.
- YSOs and Hi-GAL clumps: young stellar objects and dense gas clumps identified by infrared surveys, used as signposts of star formation.
- Fragmentation: the breakup of a gas cloud into smaller pieces that can collapse.
- Position-position-velocity data: maps giving sky position plus gas velocity, used to infer motion. · level: research-level

<details><summary>Original abstract</summary>

To probe the role of hierarchical gas structures in massive star formation, we statistically analyzed 13 Galactic massive star-forming regions using FUGIN CO survey data. Applying a non-binary dendrogram to the position-position-velocity data, we classified the extracted structures into trunks, internal leaves (the densest substructures within trunks), and isolated structures, and compared their properties with an analysis of variance controlling for regional differences. In representative regions, the trunks correspond to morphologies such as filaments and hub-filament systems, or to kinematic signatures of structure-forming events such as cloud-cloud collisions. Across the sample, the trunks are extended, massive, and strongly bound reservoirs, while the leaves are significantly more massive, denser, and more tightly bound than isolated structures of similar spatial scale. Using YSOs and Hi-GAL clumps, we find that the leaves have a lower low-mass star formation efficiency than isolated structures, whereas their clump formation efficiency is comparable. At a fixed gas mass, the leaves show no higher low-mass star formation efficiency than isolated structures but convert a larger fraction of their gas into dense clumps. We interpret these contrasts, together with inward gas motions in the position-velocity diagrams, as indicating that the deep potential of the trunks sustains continuous accretion onto the leaves and promotes mutual interactions among them. These processes may raise the characteristic fragmentation mass, as theoretically expected for a dynamically accreting medium, so that a larger fraction of the gas forms massive clumps without a corresponding increase in low-mass star formation. Our single-epoch data constrain only these structural contrasts, but indicate that the gas available for massive star formation is organized on scales larger than a single core.

</details>

## Exoplanets and planetary science

### [Planetary biotechnospheres, biotechnosignatures and the search for extraterrestrial intelligence](https://arxiv.org/abs/2611.33404)
*Irina K. Romanovskaya* · `astro-ph.EP` · arXiv:2611.33404v1 · relevance 0.08

- **In one sentence**: A conceptual paper proposing ten possible biotechnosignatures (observable traces of technology-coupled biospheres) and search strategies for them in the Solar System and over interstellar distances, including a "Cosmic Descendants" hypothesis and an estimate of the low likelihood that interstellar asteroids carry such biotechnospheres.
- **In plain words**: The paper asks how we might detect signs of advanced technology that is woven into living systems, either from past or present civilizations, whether on Earth, in our Solar System, or farther away. The author proposes ten kinds of such signs and ways to look for them. One idea is that engineered bacteria from an ancient civilization could have left descendants still living on Earth, and another is that ancient technology could have drifted to the outer Solar System. The author also estimates that interstellar asteroids are very unlikely to carry such systems.
- **Why it matters**: It widens the search for extraterrestrial intelligence beyond radio signals and spacecraft to include signs of technology merged with biology, which may be easier to test in samples from Earth, asteroids or space missions. The text itself gives no measured results or observations, so its practical value depends on how the proposed signatures are later developed and checked.
- **Background needed**: - Biosphere: all living things on a planet; technosphere: human-made technology and infrastructure.
- A biotechnosphere is the zone where the two overlap, with technology and living organisms affecting each other.
- A biosignature is a sign of past or present life; a technosignature is a sign of technology; this paper proposes biotechnosignatures, which combine both.
- Interstellar asteroids and free-floating planets are objects that travel between stars rather than orbiting one.
- The Oort cloud is a distant shell of icy bodies at the edge of the Solar System; post-main-sequence stars are stars that have passed their main, hydrogen-burning stage.
- Terraforming means reshaping a planet's environment to suit life.
- The paper is a speculative proposal rather than a report of observations. · level: research-level

<details><summary>Original abstract</summary>

The concept of planetary intelligence as collective intelligence is used to consider possible evolutionary paths of biotechnospheres that emerge on the intersection of the technosphere with the biosphere and support coupling of the technosphere with the biosphere, thus affecting planetary evolution. In mature biotechnospheres, the intelligence of technologies and the intelligence of life forms, including engineered life forms, could act in concert to perform various tasks (e.g. monitoring and restoring planetary environments and biodiversity; supporting space missions; terraforming cosmic objects). Space exploration can expand biotechnospheres beyond planets and create cosmic ecosystems. Humankind, other civilizations or their intelligent machines may produce biotechnosignatures (i.e. observables and artefacts of biotechnospheres) in the Solar System and beyond. I propose ten possible biotechnosignatures and strategies for the search for these biotechnosignatures in situ and over interstellar distances. For example, if a non-human advanced civilization existed and built biotechnospheres on Earth in the past, the descendants of its engineered bacteria could currently exist on Earth and have properties pertaining to the functions of the ancient bacteria in the biotechnospheres; intelligent technologies created by the ancient civilization could migrate to the Solar System's outer regions; these two scenarios are described as the Cosmic Descendants hypothesis. Interstellar asteroids, free-floating planets, spacecraft and objects gravitationally bound to flyby stars might carry extraterrestrial biotechnospheres and pass through the Solar System. In connection to the fate of post-main-sequence stars and their Oort clouds, the probability for interstellar asteroids to carry biotechnospheres or to be interstellar spacecraft is estimated as very low.

</details>

### [line racer: Rapid Calculation of Exoplanetary Radiative Opacities](https://arxiv.org/abs/2611.33290)
*David B. H\"agele, Paul Molli\`ere, Michiel Min* · `astro-ph.IM` · arXiv:2611.33290v1 · relevance 0.07

- **In one sentence**: line racer is a Python package for computing high-resolution radiative opacities of molecules and atoms from large line lists, designed for parallel execution and output compatible with atmospheric modeling and retrieval tools.
- **In plain words**: Astronomers study the air of distant planets and brown dwarfs by looking at which colors of light the gases there absorb. This paper describes a software tool, called line racer, that calculates how strongly those gases absorb light across many temperatures and pressures, using large catalogs of spectral lines. The text presents it as a way to do this quickly and to tailor the calculation to the user's computers.
- **Why it matters**: Accurate opacity tables are a basic input to models that interpret exoplanet spectra, so faster and more flexible calculations can make such modeling easier to run. The text does not report benchmark speeds or validation results, so its practical impact is not something this brief can confirm.
- **Background needed**: - Opacity: how strongly a gas absorbs light at a given wavelength; higher means more light is blocked.
- Spectral lines: narrow absorption features produced when molecules or atoms take in light at specific wavelengths.
- Line list: a large catalog recording the wavelength, strength and other properties of each such line for a given species.
- Temperature and pressure dependence: opacities change with the conditions of the atmosphere, so they must be computed over a grid of conditions.
- Retrieval: inferring atmospheric composition and temperature by fitting models to observed spectra.
- Parallelization: splitting a computation across many processor cores or computers to finish faster. · level: research-level

<details><summary>Original abstract</summary>

Detailed studies of exoplanet and brown dwarf atmospheres rely on precise knowledge of the spectral features of possible atmospheric species. These features are a result of the interaction of different molecules and atoms with the radiation of the host star or the intrinsic thermal radiation of the object. The interaction is described by the opacity of a species, which determines how much light is absorbed at a given wavelength. The strength and shape of these opacities are very dependent on the temperature and pressure of the atmosphere, which is why they have to be calculated for a wide range of conditions. line racer is a Python package that enables computing high-resolution opacities from large molecular and atomic line lists in an effective manner. It offers users a wide range of options to customize opacity calculations to their needs and available hardware. The code is designed for efficient parallelization on multi-core and multi-node systems and can produce outputs compatible with popular atmospheric modeling and retrieval tools.

</details>

## High-energy astrophysics

### [Clouds as near-horizon backgrounds in the radio detection of air showers](https://arxiv.org/abs/2611.34399)
*Enrique Huesca Santiago, Giulia Cantarini, Anna Nelles* · `astro-ph.HE` · arXiv:2611.34399v1 · relevance 0.13

- **In one sentence**: The paper proposes that radio signals from human-made transmitters reflected off clouds could create a background that confuses stand-alone radio detection of cosmic-ray and neutrino air showers, and uses a simplified model of cloud reflection strength in the MHz range.
- **In plain words**: Scientists detect cosmic rays and neutrinos by picking up the faint radio flashes they leave in the air as they hit the atmosphere. This paper points out that radio waves from human transmitters could bounce off clouds and mimic or hide those signals. The authors built a simplified model of how strongly clouds reflect these radio waves and found the reflections could in principle be detectable, especially when the geometry is nearly horizontal.
- **Why it matters**: Stand-alone radio detectors must reject human-made noise to find real air showers, so an unexamined source of confusing reflections matters for how these detectors are designed and trusted. The text does not show measured effects; it is a proposal supported by a simplified model, so the size of the problem in practice is still uncertain.
- **Background needed**: - Air showers: cascades of particles produced when a high-energy cosmic ray or neutrino hits the atmosphere.
- Radio detection: these showers emit short radio pulses (in the MHz range) that antennas can record, even without other instruments.
- Human-made noise: broadcast and communication transmitters whose signals contaminate radio measurements.
- Reflection/confusion background: unwanted signals that look like the target events and are hard to separate from them.
- Near-horizon geometry: signals arriving at very shallow angles, close to the horizon, where the paper finds reflections most detectable.
- The text is brief and gives no numerical results, so details of the model and its validation are not available here. · level: research-level

<details><summary>Original abstract</summary>

Stand-alone radio detection of air showers from cosmic rays or neutrinos relies on effective and efficient suppression of human-made noise sources. We propose here that reflections of human- made transmitters on clouds or other atmospheric phenomena, can cause confusion backgrounds that have not been studied previously. Given the absence of prior modelling, we have developed a simplified model for the reflection strength of clouds in the MHz regime. The results indicate that such reflections are, in principle, detectable, in particular in extremely horizontal geometries with typical experimental set-ups.

</details>

### [Constraining the Inner Accretion Geometry of GX 9+9 with Broadband Spectral and Timing Studies](https://arxiv.org/abs/2611.33858)
*Swadesh Chand, Srimanta Banerjee, Hsiang-Kuang Chang et al.* · `astro-ph.HE` · arXiv:2611.33858v1 · relevance 0.12

- **In one sentence**: A joint NICER, NuSTAR and MAXI spectral and timing study of the atoll neutron-star X-ray binary GX 9+9 (2019 and 2022 data) finds reflection features, a truncated inner disk, and an upper limit on the neutron star's magnetic field of about 3×10^10 G.
- **In plain words**: This paper studies GX 9+9, a system where a neutron star pulls gas off a companion star and the gas swirls into a hot disk before falling in. Using three X-ray telescopes watching at the same time in 2019 and 2022, the authors split the X-ray light into parts coming from the cool disk, from hot gas near the star, and from the disk glowing under that hot gas's light. They report that the inner edge of the disk sits farther out than the star's surface and estimate an upper limit on the star's magnetic field.
- **Why it matters**: Measuring where the inner disk ends tells us how strong a neutron star's magnetic field is and how gas flows onto it, which are hard quantities to measure directly. The result is an upper limit based on a model assumption (disk truncated at the magnetospheric radius), so it should be read as a constrained estimate rather than a firm measurement.
- **Background needed**: - Neutron star: a very dense star left after a massive star explodes; about 20 km across with more mass than the Sun.
- Low-mass X-ray binary: a pair of stars where a neutron star pulls matter from a companion and heats it enough to emit X-rays.
- Accretion disk: a flat, spinning ring of gas that spirals inward onto the compact object.
- Atoll source and soft state: classes of neutron-star X-ray binaries and a spectral mode where most light comes from the cool disk.
- Comptonization: a process where low-energy light gains energy by bouncing off hot electrons, forming a hard X-ray component.
- Reflection: X-rays from the hot region striking the disk and re-emitting as iron lines and a broad hump.
- Truncated disk: a disk whose inner edge stops short of the star, often set by the star's magnetic field.
- Gravitational radius (r_g): a unit of distance near a compact object, GM/c^2.
- NICER, NuSTAR, MAXI: X-ray telescopes on the ISS, NuSTAR satellite, and ISS monitor used together here. · level: research-level

<details><summary>Original abstract</summary>

We present a broadband spectral and timing study of the bright atoll neutron star low-mass X-ray binary GX~9+9, using simultaneous NICER, NuSTAR, and MAXI observations from 2019 and 2022. The broadband spectra are well described by a combination of multicolor disk emission, thermal Comptonization of blackbody seed photons from the neutron star surface or boundary layer, and associated disk reflection. We report a clear detection of reflection features in this source, including a moderately broad Fe K$\alpha$ complex and a reflection hump, confirming an earlier detection from a different observation. These features likely arise from the illumination of the moderately ionized disk by thermally Comptonized emission from the boundary layer or warm corona. While the source remained in the soft spectral state during both observations, the 2022 observation exhibits a relatively larger thermal contribution, together with a steeper Comptonized component and lower coronal optical depth. Both reflection and disk-continuum modeling favor a truncated disk, with the latter indicating a smaller inner disk radius in 2022. The inferred radial extent of the boundary layer of $\sim8~r_{\rm g}$ may play a role in the observed disk truncation. Assuming that the disk is truncated at the magnetospheric radius, we obtain an upper limit on the magnetic field strength of $\lesssim3\times10^{10}$ G. Timing analysis reveals a relatively stable disk component and a highly variable Comptonized component, consistent with the typical characteristics of the soft state.

</details>

## Stars and the Sun

### [Investigating the Neupert Effect with HEL1OS/Aditya-L1](https://arxiv.org/abs/2611.34450)
*Srikar Paavan Tadepalli, Abhishekh Kumar Srivastava, K. Sankarasubramanian et al.* · `astro-ph.SR` · arXiv:2611.34450v1 · relevance 0.08

- **In one sentence**: Using HEL1OS hard X-ray spectrograms from Aditya-L1 for 312 solar flares (Nov 2023 to May 2026), the authors test the Neupert effect, reporting a median soft-hard X-ray correlation of 0.984 and an empirical forward model that reconstructs the thermal lightcurve from non-thermal hard X-ray emission, including quasi-periodic pulsations.
- **In plain words**: Solar flares are sudden bursts of energy on the Sun that heat plasma and give off X-rays. This study uses an Indian solar satellite's instrument to split the X-ray signal from 312 flares into a hot "thermal" part and a fast-changing "non-thermal" part. The authors find the two track each other very closely and build a model that rebuilds the heat signal from the fast bursts.
- **Why it matters**: The Neupert effect is a long-standing empirical pattern linking flare heating to energy bursts, so a large sample testing it with broadband data could help interpret how flares release energy. The text reports a strong correlation and a model that reproduces the observed thermal evolution; its broader significance for flare physics is for specialists to judge.
- **Background needed**: - Solar flare: a sudden release of magnetic energy on the Sun, producing X-rays and heating plasma.
- Hard vs soft X-rays: hard X-rays come from fast-moving electrons hitting material; soft X-rays come from hot plasma that has been heated.
- Neupert effect: an observed pattern where the soft X-ray signal roughly follows the time-accumulated hard X-ray signal.
- Lightcurve: a graph of brightness over time.
- Quasi-periodic pulsations (QPPs): repeating-but-irregular ups and downs in flare brightness.
- Aditya-L1: India's solar observatory satellite; HEL1OS is its hard X-ray spectrometer.
- Correlation coefficient: a number from 0 to 1 measuring how closely two quantities move together. · level: research-level

<details><summary>Original abstract</summary>

We investigate the Neupert effect in solar flares using broadband hard X-ray observations from the HEL1OS instrument onboard Aditya-L1. By separating thermal and non-thermal components from HEL1OS spectrograms, we analyse a sample of 312 flares observed between November 2023 and May 2026. We find that the soft X-ray flux is strongly correlated with the time-integrated hard X-ray emission, with a median correlation coefficient of 0.984, indicating that Neupert-like behaviour is nearly ubiquitous in flares with detectable non-thermal emission. Extending beyond statistical correlation, we develop an empirical forward model in which the thermal lightcurve is reconstructed from the non-thermal emission by resolving the hard X-ray lightcurve into individual energy-release episodes and convolving their fitted profiles with finite thermal-response functions. This approach successfully reproduces the observed thermal evolution, including flares that exhibit quasi-periodic pulsations (QPPs). Our results demonstrate that the broadband HEL1OS observations sample both thermal-dominated and non-thermal-dominated flare emission within a single instrument, providing an observation-driven link between the temporal structure of non-thermal HXR emission and the thermal X-ray response. This provides a different framework for interpreting flare energetics and temporal evolution using broadband hard X-ray measurements.

</details>

### [Evidence for an Evolving Surface on the Partly Burnt Runaway Stellar Remnant GD 492](https://arxiv.org/abs/2611.33301)
*Reuben Dsouza, J. J. Hermes, Boris T. G\"ansicke et al.* · `astro-ph.SR` · arXiv:2611.33301v1 · relevance 0.08

- **In one sentence**: Analysis of 12 TESS sectors of photometry shows that the 8.9-hour brightness modulation of the hypervelocity, partly burnt stellar remnant GD 492 drifts in period and shape over months, consistent with evolving surface spots.
- **In plain words**: GD 492 is a dense, fast-moving star remnant that is thought to have survived a thermonuclear supernova explosion, and it was previously reported to brighten and dim about every 8.9 hours. Using more than four years of data from NASA's TESS satellite, the authors found that this cycle is not fixed: its apparent period shifts by about 0.5 percent, and its shape changes over one to two months. A simple two-spot model can reproduce several of the observed light patterns, though the spot geometry is not uniquely determined.
- **Why it matters**: If the brightness changes come from shifting surface features, this would be a new handle on the star's outer convective layers and could bear on how to read its unusual atmospheric chemistry. The text does not settle the cause, and it names differential rotation and magnetic activity only as possible contributors.
- **Background needed**: - GD 492 is a white dwarf-like remnant (a dense, Earth-sized leftover of a star) moving unusually fast through the galaxy.
- "Partly burnt" means it appears to have been only partly fused by a thermonuclear (nuclear-fuel) explosion before being ejected.
- TESS is a NASA space telescope that measures star brightness over time (photometry); a "sector" is one roughly month-long observing run.
- A "modulation" is a regular rise and fall in brightness, here attributed to rotation of uneven surface patches.
- Period is the time for one full cycle; the paper reports the cycle drifting between 8.86 and 8.90 hours.
- Differential rotation means different latitudes spin at different rates; spots are dark or bright surface patches that can make a star's brightness vary as it turns. · level: research-level

<details><summary>Original abstract</summary>

GD 492 (LP 40-365) is a partly burnt, hypervelocity runaway stellar remnant thought to have survived a thermonuclear supernova. We analyze 12 sectors of TESS photometry spanning more than four years to investigate the previously reported 8.9-hr photometric modulation of the star. We find that the modulation changes with time, with individual-sector fits yielding apparent periods ranging from 8.8606 to 8.9048 hr (0.5% changes), more than 25 times the formal measurement uncertainties. Both the period and shape of the modulation evolve on a timescales of approximately one to two months. We show qualitatively that a two-spot model with evolving surface structure can reproduce several of the observed light-curve morphologies, although the geometry of the spots is not uniquely constrained. These observations suggest that changing surface inhomogeneities are a plausible origin of the photometric variability. Differential rotation and magnetic activity may contribute to this evolution, potentially providing new constraints on the outer convective structure of GD 492 and on the interpretation of its atmospheric abundances.

</details>

## Chemical physics

### [TyxonQ: A Workflow Layer for Quantum Computing in Chemistry](https://arxiv.org/abs/2611.33883)
*Xiaoran Li, Zhi Yin, Zhupeng Han et al.* · `physics.chem-ph` · arXiv:2611.33883v1 · relevance 0.11

- **In one sentence**: TyxonQ is a software workflow layer that connects quantum solvers with classical molecular mechanics, dynamics, and electronic-structure codes (via PySCF-compatible scanners, embedding, and adapters for ASE, i-PI, OpenMM, LAMMPS and MDI) so that quantum calculations on active spaces or fragments can be slotted into existing multiscale chemistry pipelines.
- **In plain words**: Chemists often need to combine several levels of simulation: simple classical models for most of a molecule, standard quantum-chemistry calculations, and a quantum computer for a small, hard-to-describe part. This paper describes TyxonQ, a software layer that handles the plumbing between these levels rather than the quantum algorithm itself. The authors report testing it on small chemistry workflows for correctness, switching cost, reproducibility, and portability of saved results.
- **Why it matters**: Practical use of near-term quantum computers in chemistry may depend as much on fitting into existing simulation workflows, including industrial ones, as on the quantum solver alone. The text does not report how the tool performs at scale, so its usefulness beyond the small test cases is unclear from this description.
- **Background needed**: - Molecular mechanics (MM): fast classical models of atoms as balls and springs, used for large systems.
- QM/MM: a hybrid approach that treats a small region with quantum-chemistry methods and the rest with classical MM.
- Active space / embedding: choosing a small subset of electrons and orbitals (or a fragment) to treat accurately, which is what a quantum computer would handle.
- CCSD / FCI: standard classical quantum-chemistry solvers used as reference methods.
- NISQ devices: current noisy quantum computers with limited qubits and circuit depth.
- Workflow interfaces and adapters: software connectors that let different codes pass energies and forces to each other; PySCF, ASE, i-PI, OpenMM, LAMMPS, and MDI are such codes or connectors.
- Reproducibility and artifact portability: whether results can be regenerated and moved between computers. · level: research-level

<details><summary>Original abstract</summary>

Quantum computational chemistry is often framed around a hybrid quantum solver. In practical applications, however, bottlenecks to adoption also lie in the surrounding multiscale workflow. A molecular problem may combine classical molecular mechanics and dynamics, conventional electronic-structure calculations, and a quantum solver for selected orbitals or embedded fragments. This division of work is particularly relevant when a chemically important electronic subspace is strongly correlated. The size of the electronic Hilbert space and the qubit, noise, and circuit-depth constraints of noisy intermediate-scale quantum (NISQ) devices make active-space and embedding choices central to a feasible quantum calculation. The resulting energies and gradients must remain consistent with the surrounding classical simulation. We present TyxonQ, a workflow layer that connects these levels of treatment rather than addressing only the hybrid quantum algorithm. Four integration interfaces link PySCF-compatible energy/force scanners and embedding, solver adapters, simulator and hardware backends, and classical consumers. The implementation combines QM/MM and fragment embedding with conventional CCSD/FCI fragment solvers, variational and sampling-based quantum methods, and adapters for ASE, i-PI, OpenMM, LAMMPS (through i-PI), and MDI. We describe the contracts and audit coverage, and evaluate correctness, switching cost, reproducibility, and artifact portability on small chemistry workflows, distinguishing executed paths from source-level support. The purpose of TyxonQ is to support incremental integration of quantum calculations into existing computational chemistry workflows, including those used in industry, while retaining appropriate classical treatments elsewhere.

</details>

### [Automatic dual basis sets for self-consistent field calculations](https://arxiv.org/abs/2611.34694)
*Joonatan Huhtasalo, Susi Lehtola* · `physics.chem-ph` · arXiv:2611.34694v1 · relevance 0.10

- **In one sentence**: The paper presents an algorithm that automatically builds a smaller "dual basis" of orbitals from a target orbital basis and a given Fock matrix, to speed up convergence of self-consistent field (SCF) calculations in DFT.
- **In plain words**: Computer simulations of molecules and materials must repeatedly refine an answer until it stops changing, and the number of refinement steps depends heavily on the starting guess. The authors propose a way to automatically build a simplified, smaller set of mathematical building blocks that can reach a rough but correct answer quickly, then use it to start the full, more accurate calculation. They report that the generated sets perform similarly across a wide range of systems from the first four rows of the periodic table.
- **Why it matters**: Faster convergence in DFT calculations matters because DFT is a widely used workhorse in chemistry and materials science, and large-scale or machine-learning-driven studies need many such calculations. The text also reports a negative finding: current initial guesses for the Fock matrix are not accurate enough to make adaptive basis sets useful yet, and the authors suspect similar basis-compression approaches may face the same limit.
- **Background needed**: - DFT (density functional theory): a standard quantum-mechanical method for estimating the electron structure of atoms and molecules.
- SCF (self-consistent field): an iterative procedure where a guess is refined repeatedly until the result stops changing; cost is roughly the number of steps times the cost per step.
- Basis set: a fixed set of mathematical functions used to represent electron orbitals; larger sets are more accurate but more expensive. "Triple-zeta" and "polarized" describe increasingly large, more flexible sets.
- Fock matrix: the matrix encoding the effective energy operator the electrons feel; its initial guess sets the starting point of the SCF iteration.
- Dual basis: a smaller, pruned basis used first to get a rough solution before switching to the full basis. · level: research-level

<details><summary>Original abstract</summary>

Density functional theory (DFT) has long been the workhorse of electronic structure theory, and it is experiencing a new boom thanks to big data applications and machine learning. A DFT calculation requires the iterative solution of the self-consistent field (SCF) problem, whose cost is the product of (i) the number of SCF steps and (ii) the cost of a single step. The number of SCF steps depends strongly on the initial guess, regardless of the SCF algorithm, and quantitative DFT accuracy is known to require at least a polarized triple-$\zeta$ basis set. However, a qualitatively correct solution may often be found already in a smaller \emph{dual basis} (DB), which can then bootstrap a calculation in the full basis set. Traditionally, the DB is chosen by hand for each application to enable robust convergence to the ground state. In this work, we pursue automatic generation of DBs for SCF calculations. Our generator constructs a pruned orbital basis from the target orbital basis for a predefined precision threshold and a given Fock matrix. As expected, the larger the basis set is, the smaller the fraction of kept basis functions. The DBs produced by our algorithm exhibit similar performance for a wide range of systems from the first 4 periods of the periodic table. Ultimately, we find that presently available initial guesses for the Fock matrix are not accurate enough to unlock the use of adaptive basis sets, and believe that the same limitation may hold for similar attempts for basis compactification.

</details>

## Materials science

### [Brightening spin- and parity-forbidden interlayer excitons through rhombohedral stacking](https://arxiv.org/abs/2611.34900)
*Haodong Hu, Chih-En Hsu, Kenji Watanabe et al.* · `cond-mat.mes-hall` · arXiv:2611.34900v1 · relevance 0.10

- **In one sentence**: In a rhombohedrally stacked (3R) MoS2 bilayer, the authors report that stacking brightens two normally optically forbidden interlayer excitons, a spin-unlike 1s state and a parity-odd 2p state, and that the hybridized 2p state shows constructive interference between transition dipoles.
- **In plain words**: Excitons are short-lived pairs of an electron and a "hole" (a missing electron) that carry light energy in thin semiconductors. Some excitons are "dark": they are forbidden by symmetry rules from absorbing or emitting light, so they are hard to see. This paper shows that stacking two atomically thin layers of molybdenum disulfide in a particular rotated arrangement (rhombohedral stacking) makes two such dark interlayer excitons visible.
- **Why it matters**: The work suggests that the way atomic layers are stacked is a practical knob for controlling the quantum states of excitons in 2D materials, which could matter for future optical or quantum devices. The text does not establish specific applications, so that link remains speculative.
- **Background needed**: - Excitons: bound electron-hole pairs that behave like a single particle and can absorb or emit light.
- Interlayer vs. intralayer excitons: the electron and hole sit in different atomic layers (interlayer) or the same layer (intralayer).
- Symmetry-forbidden ("dark") states: quantum selection rules that block light absorption or emission; brightening them makes them observable.
- Stacking/registry: how atomic layers are rotated or shifted relative to each other; rhombohedral (3R) stacking is one specific arrangement.
- g-factor: how a state's energy shifts in a magnetic field, used here to identify its spin character.
- Hybridization and transition dipole: mixing of two states when they reach the same energy, and the strength of their coupling to light; constructive interference means their contributions add up. · level: research-level

<details><summary>Original abstract</summary>

Brightened symmetry-forbidden excitons can provide critical information about the electronic structure and many-body interactions in semiconductors. Recently, interlayer atomic registry has emerged as a new way to control atomically thin layered materials in both ground and excited states. Here we show that the rhombohedral stacking in a 3R-MoS_2 homobilayer can brighten two symmetry-forbidden interlayer excitons: one is a spin-unlike 1s exciton and the other is a parity-odd 2p exciton. The nature of these interlayer excitons is revealed by their gfactors as well as the hybridization patterns observed when they are tuned to resonate with intralayer excitons. Surprisingly, the hybridized 2p exciton exhibits a constructive quantum interference between the acquired transition dipoles, revealing a hidden gauge-invariant phase contrast between the constituent electronic states. Our results establish stacking control as a powerful approach for modulating quantum phases of excitons in 2D semiconductors.

</details>

### [Unveiling ferroelectricity in wafer-scale beta-phase In$_2$Se$_3$](https://arxiv.org/abs/2611.33405)
*Kyungmin Yang, Hyunmin Cho, Jihwan Jeon et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33405v1 · relevance 0.09

- **In one sentence**: The paper reports bistable out-of-plane and in-plane polar order in van der Waals beta-phase In2Se3, arising from a picometre-scale distortion within each quintuple layer, persisting down to a ~1.9 nm bilayer and demonstrated in wafer-scale MOCVD films with capacitor arrays and a ferroelectric semiconductor transistor.
- **In plain words**: Ferroelectric materials can hold a switchable electrical polarity, which could be used to store bits, but they usually stop working when made very thin. This paper reports that a layered semiconductor, beta-phase indium selenide, which was thought to lack this polarity, can be switched by a vertical electric field even when only two layers thick. The authors also grew the films on 2-inch wafers and built test devices that switched consistently.
- **Why it matters**: Ferroelectric memory that still works at atomic-scale thickness could matter for future compact memory and transistor designs, and the device-level uniformity and endurance figures are the part that speaks to practical use. The text gives only one short abstract, so the size of the advance, and how well these numbers hold across other groups or conditions, cannot be judged from it.
- **Background needed**: - Ferroelectric: a material whose internal electrical polarity can be flipped by an applied electric field and keeps its state when the field is removed, the basis of some memory chips.
- Van der Waals material: a layered crystal whose sheets are held together by weak forces, so it can be peeled or grown in very thin layers.
- Quintuple layer: one five-atom-thick sheet unit of this material; a bilayer is two such units (~1.9 nm).
- Centrosymmetric: a crystal structure with a symmetry centre, which normally forbids a built-in polarity; the paper argues a tiny distortion breaks this.
- Picometre: one trillionth of a metre, a very small atomic displacement.
- Coercive field and remanent polarization: the field needed to flip the polarity and the leftover polarity charge after switching; the paper's values are estimates, and the polarization is called "apparent".
- Endurance and retention: how many switching cycles a device survives and how long its state lasts.
- MOCVD (metal-organic chemical vapor deposition): a industrial method for growing thin films from gas-phase precursors. · level: research-level

<details><summary>Original abstract</summary>

Pushing ferroelectricity to the ultimate thickness limit is a central challenge for memory hardware, because conventional three-dimensional ferroelectrics degrade through depolarization and interfacial effects when thinned. Here we identify $\beta$-In$_2$Se$_3$, a van der Waals semiconductor regarded as centrosymmetric, as a host of bistable polar order arising from a picometre-scale distortion within each quintuple layer. The polar state has out-of-plane and in-plane components, is switched by a vertical electric field, and persists to the bilayer limit (~1.9 nm) with an estimated coercive field of 0.9 MV/cm and an apparent remanent polarization of 11.0 $\mu$C/cm$^2$. Films grown by metal-organic chemical vapor deposition on 2-inch wafers yield capacitor arrays with a switching-voltage spread below 5% across 100 devices, an endurance of $10^7$ cycles and a projected ten-year retention. Because the polar state coexists with a semiconducting gap, one film serves as both the switching layer of a capacitor and the channel of a ferroelectric semiconductor transistor.

</details>

## Soft matter and polymers

### [A Thermodynamically Consistent Model of a Rechargeable Salt-in-Polyelectrolyte Battery](https://arxiv.org/abs/2611.34415)
*Charlotte Beckford, Rajeev Kumar, Steven M. Wise* · `cond-mat.soft` · arXiv:2611.34415v1 · relevance 0.09

- **In one sentence**: An isothermal, thermodynamically consistent continuum model of a rechargeable salt-in-polyelectrolyte battery, with cation intercalation at electrode-electrolyte interfaces, that reduces to dual-ion-conductor and single-ion-conductor limits and is compared in 1D galvanostatic charge-discharge simulations.
- **In plain words**: This paper builds a mathematical model of a lithium-type battery whose electrolyte is a charged polymer (a chain of negatively charged units with lithium ions attached) that may also contain extra dissolved salt. The authors check that the model follows basic thermodynamic rules and reduce it to two simpler battery types, one with added salt and one with only the charged polymer. Simulations of charging and discharging in one dimension show how ion concentrations shift, how the voltage is polarized, and how much of the electrode gets used, though the text does not report specific headline numbers.
- **Why it matters**: Polymer electrolytes are a candidate for safer batteries, and a model that is consistent with thermodynamics and that can compare salt-containing and salt-free designs could help guide design choices. The text does not establish practical performance claims, so its relevance to real devices is unverified.
- **Background needed**: - Electrolyte: the medium that carries ions between battery electrodes.
- Polyelectrolyte: a polymer whose repeat units carry electric charge; here the polymer is negatively charged and lithium ions balance it.
- Dual-ion vs single-ion conductor: in the first, both positive and negative ions move; in the second, mainly the lithium ions move because the polymer backbone is fixed in place.
- Intercalation: lithium ions inserting into and leaving the crystal structure of an electrode material.
- Galvanostatic: charging or discharging at a constant current.
- Butler-Volmer equation: a standard formula relating electrode reaction speed to voltage driving force.
- Fick's law: the standard rule that ions diffuse from high to low concentration.
- Thermodynamically consistent: the model obeys energy and entropy bookkeeping, so it does not create or destroy energy. · level: research-level

<details><summary>Original abstract</summary>

We present an isothermal, thermodynamically consistent model of a salt-in-polyelectrolyte battery with intercalation and deintercalation reactions of cations occurring at the electrode-electrolyte interfaces under galvanostatic conditions. For the electrolyte, we consider polyelectrolytes, which are polyanions, with neutralizing cations (i.e., counterions) such as lithium, along with a monovalent salt containing the same cations. Models of batteries containing either a dual-ion-conductor (DIC) electrolyte (i.e., uncharged polymers with added salt) or a single-ion-conductor (SIC) electrolyte (i.e., charged polymers without added salt) emerge as limiting cases of this thermodynamically consistent model. Once the model is presented in its most general context, we make specific choices so that it captures well-known mechanisms. In particular, the governing diffusion equations recover Fick's law of diffusion, and the cation-transfer reaction rate is described by the Butler--Volmer equation. The DIC and SIC limiting cases provide a framework for comparing the corresponding batteries. One-dimensional DIC and SIC charge--discharge simulations at matched current and duration illustrate concentration redistribution, polarization, and electrode utilization. Numerical accuracy checks quantify sensitivity to discretization; distinct initial inventories qualify the comparison.

</details>

### [Discotic columnar phase in a three-dimensional monomer-tetramer model of Heilmann and Lieb with side-to-side attraction](https://arxiv.org/abs/2611.34796)
*Qidong He* · `math-ph` · arXiv:2611.34796v1 · relevance 0.08

- **In one sentence**: A rigorous statistical-mechanics proof that a three-dimensional Heilmann–Lieb monomer-tetramer lattice model with side-to-side attraction orders into discotic columnar phases, with exactly twelve extremal periodic Gibbs measures at low temperature, resolving an earlier conjecture for the stated parameter regime.
- **In plain words**: This paper studies a simplified mathematical model of liquid crystals, where flat disc-shaped molecules (here called tetramers, or plaquettes) sit on a cubic grid and attract their neighbours when they lie flat in the same plane and point the same way. The author shows that, at low enough temperature, these pieces stack up into one-dimensional columns that are themselves arranged in a square pattern. This settles a conjecture from 1979 that had been open for the stated range of settings.
- **Why it matters**: Proving with full mathematical rigour that a specific lattice model forms columnar liquid-crystal order is a useful check on how such phases arise from simple interactions. The text does not say how the result would be applied to real materials, so any wider connection is uncertain.
- **Background needed**: - Liquid crystals: states of matter between solid and liquid, where molecules have partial order in orientation or position.
- Discotic phase: a liquid-crystal phase built from disc-shaped molecules that stack into columns.
- Lattice model: a simplified model in which particles sit on the points of a grid and interact only with nearby particles.
- Hard-core repulsion: particles cannot overlap.
- Chemical potential (mu): a parameter controlling how many particles the system tends to hold.
- Gibbs measure: a probability distribution describing the random configurations of a system at a given temperature; "extremal" ones are the pure, unmixed states.
- Ground state / zero-temperature picture: the lowest-energy arrangements, which the paper says are degenerate (many equally good), with thermal fluctuations choosing among them.
- Symmetry breaking: a state that picks one direction or orientation out of several equally possible ones. · level: research-level

<details><summary>Original abstract</summary>

We study Model III of Heilmann--Lieb (1979), a lattice model for liquid crystals consisting of tetramers (plaquettes) on the cubic lattice at chemical potential $\mu$, interacting via a hard-core repulsion and a lateral attraction of strength $a>0$ between coplanar, aligned tetramers. The model was conjectured to exhibit liquid-crystalline order at low temperature provided that $\mu+2a>0$. We establish discotic columnar order throughout this regime, fully resolving the conjecture. Specifically, we prove the existence of exactly twelve extremal and periodic Gibbs measures, each breaking rotational symmetry, with one of three tetramer orientations dominant, and translational symmetry in exactly two directions, with one of four tetramer parities dominant within that orientation. Thus, the tetramers form one-dimensional columns arranged on a square lattice. This arrangement is not a priori evident from the zero-temperature picture, where energy only enforces a layered structure: each layer is fully packed and crystalline, but different layers are free to shift independently within their planes. The main novelty here lies in showing how thermal fluctuations lift this degeneracy in favor of the twelve ground states in which all tetramers share a common parity.

</details>

## AI for chemistry and materials

### [Temporal Selective Exploration for Reinforcement Learning-Guided Continuous-Discrete Flow Matching in 3D Molecular Design](https://arxiv.org/abs/2611.33417)
*Lianghong Chen, Yan Yi Li, Gen Zhou et al.* · `cs.LG` · arXiv:2611.33417v1 · relevance 0.22

- **In one sentence**: A reinforcement-learning method that fine-tunes a continuous-discrete flow-matching generator for 3D de novo molecule design, restricting exploration to timesteps that matter for target properties and calibrating rewards across multiple objectives, applied to EGFR and Pin1 inhibitors.
- **In plain words**: This paper is about using trial-and-error learning to steer an AI that designs 3D molecules, so that the designs better meet goals such as binding to a disease-related protein. The authors change how much random exploration the AI does, limiting it to the stages of the design process that actually affect the final result, and they balance several goals so none drowns out the others. They report applying this to two protein targets, EGFR and Pin1, and say they found some new candidate inhibitors, supported only by computer-based (in silico) checks.
- **Why it matters**: Designing molecules that fit a target protein is a costly early step in drug discovery, so better ways to tune generative models could matter there. The text gives no comparison with existing methods or experimental (lab) validation, so its practical value is not yet established.
- **Background needed**: - Flow matching: a generative AI technique that learns to turn random noise into structures (here, atom positions and atom types) along a smooth path.
- ODE vs SDE: an ordinary differential equation gives a fixed, deterministic path; a stochastic differential equation adds randomness, which reinforcement learning needs in order to explore alternatives.
- Reinforcement learning (RL): training by trying variations and rewarding the ones that score well on a goal.
- Continuous vs discrete: atomic coordinates are continuous numbers, while atom identities (e.g., carbon or oxygen) are categories.
- Multi-objective optimization: balancing several goals at once, such as potency and drug-likeness.
- In silico: done by computer simulation rather than in a laboratory.
- EGFR and Pin1: two protein targets relevant to disease, against which inhibitor molecules are sought. · level: research-level
- Matched keywords: molecular, protein

<details><summary>Original abstract</summary>

Flow matching has shown strong potential in generative tasks, while its optimization via Reinforcement Learning (RL) remains underexplored, especially in continuous-discrete mixed settings. Moreover, flow matching is formulated as an Ordinary Differential Equation (ODE), whose deterministic trajectories do not naturally support RL optimization. Introducing stochasticity by converting the entire trajectory into a Stochastic Differential Equation (SDE) is a common practice. Nevertheless, not all timesteps contribute to the final outcomes, and redundant exploration introduces additional noise. Furthermore, in multi-objective settings, some objectives may dominate the optimization while others receive insufficient updates. In this study, we propose an RL-guided continuous-discrete flow matching framework with temporal selective exploration for 3D de novo molecular design. Specifically, our method jointly optimizes continuous and discrete flow matching for atomic coordinates and molecular identities, respectively, while restricting exploration to timesteps that primarily contribute to target properties, reducing ineffective exploration. We also introduce a reward-based advantage calibration mechanism to mitigate objective dominance in multi-objective optimization. The framework is applied to design inhibitors for both the well-studied target protein EGFR and the challenging Pin1 protein. We identify some novel candidate inhibitors, supported by in silico validation.

</details>

### [PerovAgent: Autonomous Ligand Design for Halide Perovskite Nanocrystals](https://arxiv.org/abs/2611.33913)
*Seungjun Cha, Yoo Jae Jeong, Amanda Conde Del Moral et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33913v1 · relevance 0.21

- **In one sentence**: PerovAgent is an LLM-driven multi-agent framework that autonomously designs surface-capping ligands for CsPbBr3 perovskite nanocrystals, optimizing computed binding energy and turning search results into statistically tested design principles, with one alkynyl-phosphonate principle checked by DFT.
- **In plain words**: This paper describes a computer system that uses a large language model to design small molecules that coat the surface of tiny crystals used in light-emitting and solar materials. The system proposes candidate molecules, runs simulations to estimate how strongly each one sticks to the crystal surface, and tests its own guesses about what makes a good design. Of 35 rules it proposed, 19 held up in new tests, and 7 of those also passed an extra check for hidden confounding factors.
- **Why it matters**: Surface ligands strongly affect how well perovskite nanocrystals perform, so an automated way to search ligand chemistry could speed up materials work. The paper also points out that many LLM-generated hypotheses fail validation, which is a useful caution for autonomous discovery. The text does not show how far the approach generalizes beyond CsPbBr3 surfaces, and the authors only say the framework could be extended to more complex ligands.
- **Background needed**: - Halide perovskite nanocrystals: tiny crystals of a metal-halide material used in LEDs and solar cells.
- Surface-capping ligands: molecules bound to a crystal's surface that control stability and performance.
- Binding energy: a computed number indicating how strongly a molecule sticks to a surface; lower (more negative) usually means stronger binding.
- Machine-learned interatomic potential: a fast, learned approximation of the forces between atoms, used in place of slower quantum calculations.
- Density functional theory (DFT): a quantum-mechanical method used here as an independent check on one prediction.
- Multi-agent framework: several software components, some driven by an LLM, that take turns proposing, running and checking steps.
- Confound audit: a check for whether an apparent pattern is really caused by another, hidden factor. · level: research-level
- Matched keywords: molecular, interatomic potential

<details><summary>Original abstract</summary>

Designing surface-capping ligands for high-performance halide perovskite nanocrystals requires navigating a vast molecular space while discovering design rules that govern ligand-surface interactions. Here, we introduce PerovAgent, an autonomous multi-agent framework that combines large language model (LLM)-driven scientific reasoning with computational tools for atomistic model construction, machine-learned interatomic potential evaluation, and statistical validation. Across ten independent campaigns on CsPbBr3 surfaces, PerovAgent adaptively explored and refined diverse ligand chemistries while progressively improving the binding-energy objective. Beyond optimization, the framework converts recurring chemical observations into explicit design principles that can be statistically evaluated. Of 35 formulated principles, 19 were prospectively supported, of which seven also passed the confound audit, highlighting the need to systematically validate plausible LLM-generated hypotheses during autonomous discovery. A recurrent alkynyl-phosphonate principle was further examined using density functional theory, which reproduced the predicted energetic preference. These results demonstrate an autonomous discovery framework that not only searches molecular space and optimizes the scalar objective but also transforms its search trajectory into systematically testable design principles. The framework can also be extended to more complex ligands, including zwitterionic, multidentate, and polymerizable ligands, to explore a wider range of ligand-surface interactions and uncover new design principles for halide perovskite nanocrystals.

</details>

## Biochemistry

### [Identification of Functional NOD2-Specific Aptamers Using APT-SNAP Microarrays to Screen Zebrafish Nod-like Receptors](https://www.biorxiv.org/content/10.64898/2026.11.24.768724v1)
*Messa, P. E.; Pearson, K. S.; Conti, B. J. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.768724 v1 · relevance 0.06

- **In one sentence**: The paper reports DNA aptamers (short single-stranded DNA binders) selected with the APT-SNAP microarray platform that bind zebrafish NOD2, an intracellular innate immune receptor, and validates them with several biochemical and cellular assays.
- **In plain words**: Scientists studying the immune system need reliable tools that grab a specific protein so they can see or measure it. For zebrafish, a common research animal, good antibodies for a family of immune sensors called NOD-like receptors are scarce. The authors screened a large array of short DNA sequences, identified several that bind zebrafish NOD2, and tested the best ones with several lab methods.
- **Why it matters**: Immune sensors like NOD2 are linked to inflammatory diseases and some cancers, so having dependable detection reagents for them in zebrafish could help future mechanistic work. The paper also suggests the approach could be used for other hard-to-target proteins, though the text does not show that yet beyond this one case.
- **Background needed**: - Proteins: molecules that do most of the work in cells; immune sensors detect threats inside cells.
- NOD-like receptors (NLRs): intracellular sensors that detect pathogen or damage signals and trigger inflammatory responses.
- Antibodies: proteins that bind a target; used to detect and measure proteins in labs. Often unreliable for some targets.
- Aptamers: short single-stranded DNA or RNA sequences folded to bind a target, sometimes described as chemical "antibodies."
- Microarray: a surface carrying many different sequences at once, allowing many binding tests in parallel.
- Affinity and specificity: how tightly a reagent binds its target and how little it binds other things.
- Biolayer interferometry (BLI) and pull-downs: lab methods to measure binding strength and to fish out a target protein with a binder.
- Zebrafish: a small fish widely used to study development and immunity. · level: research-level

<details><summary>Original abstract</summary>

NOD-like receptors (NLRs) are intracellular immune sensors that monitor for pathogen- and damage-associated molecular patterns (PAMPs, DAMPs) and initiate innate immune signaling pathways upon detection. Dysregulation of NLR signaling contributes to numerous inflammatory diseases and cancers, yet mechanistic studies of NLR proteins are limited by the availability of reliable detection reagents, particularly in emerging model organisms such as zebrafish (Danio rerio). Although zebrafish provide a powerful system for studying innate immunity, few validated antibodies exist for zebrafish NLR proteins. Here, we describe the development of aptamer-based detection reagents targeting zebrafish NLRs using the APT-SNAP platform, a high-density aptamer microarray technology that enables rapid identification of protein-binding nucleic acid ligands. Using this approach, we identified multiple DNA aptamers that bind zebrafish NLR proteins and selected candidates targeting NOD2 for further characterization. Orthogonal validation assays, which include enzyme-linked apta-sorbent assays (ELASAs), pull-downs, biolayer interferometry (BLI), and fluorescence microscopy, confirmed that the lead aptamers bind zebrafish NOD2 with high affinity and specificity, and function effectively in biochemical and cellular assays. These results demonstrate that APT-SNAP generated validated, native-state affinity reagents for a zebrafish immune protein where commercial antibodies failed, providing new molecular tools for investigating NLR biology in zebrafish. More broadly, this strategy establishes a generalizable approach for generating affinity reagents against challenging protein targets that lack reliable antibodies.

</details>

### [Antifungal and Antibiofilm Activity of a Thermostable Lipid Transfer Protein-Enriched Fraction from Capsicum annuum L. Seeds against Candidozyma auris](https://www.biorxiv.org/content/10.64898/2026.11.24.768040v1)
*Vera Gonzalez, S. M.; Larrondo, C.; Claver, S. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.768040 v1 · relevance 0.05

- **In one sentence**: A heat-stable, lipid-transfer-protein-enriched fraction from Capsicum annuum (pepper) seeds shows antifungal and antibiofilm activity against multidrug-resistant Candidozyma (Candida) auris and other Candida species in laboratory tests.
- **In plain words**: A drug-resistant yeast called Candidozyma auris is hard to treat, so researchers are looking for new antifungal agents from unusual sources. Here, the team pulled out a heat-tolerant group of small proteins from pepper seeds and tested them against several Candida-type yeasts in the lab. The fraction, whose main parts were two lipid-transfer proteins, slowed or killed the yeasts and reduced their sticky biofilm communities.
- **Why it matters**: Drug-resistant C. auris is a growing clinical concern, so new antifungal leads with different mechanisms matter. The text reports only laboratory results on this fraction; it does not show safety, effectiveness in animals or people, or that the active proteins work alone, so the potential for drug development remains unproven.
- **Background needed**: - Candidozyma auris (formerly Candida auris): a yeast that can cause hospital infections and often resists common drugs such as fluconazole.
- Biofilm: a film-like community of microbes stuck to a surface, which is harder to kill than single cells.
- Lipid-transfer proteins (nsLTPs): small plant proteins that move fat-like molecules between membranes; some have antimicrobial effects.
- MIC / MFC: the lowest concentration that stops microbial growth / that kills it.
- Thermostable: keeps working after heating; the fraction was made by heat treatment, which removed many other proteins.
- LC-MS/MS: a lab method for identifying proteins by their mass and fragments.
- Trypsin inhibition: a measure of blocking a digestive enzyme; reported here as a property of the fraction, its relevance to antifungal action is not explained in the text. · level: intermediate

<details><summary>Original abstract</summary>

The emergence of multidrug-resistant Candidozyma auris (C. auris) has intensified the search for antifungal molecules with alternative structures and mechanisms of action. Here, we investigated Capsicum annuum L. seeds as a source of thermostable antifungal peptides. Thermal fractionation of a crude aqueous seed extract (RBPCE) yielded a heat-treated fraction (RBPHT) enriched in low-molecular-weight proteins. LC-MS/MS identified the type I and type II non-specific lipid-transfer proteins Ca-nsLTP1 and Ca-nsLTP2 as its predominant constituents. Compared with RBPCE, RBPHT displayed increased trypsin-inhibitory potency. RBPHT inhibited C. albicans, C. krusei, and C. auris isolates from clades I, III, and IV, including isolates showing no detectable response to fluconazole under the conditions tested. Against a representative South American clade IV isolate, the nsLTP-enriched fraction exhibited minimum inhibitory and fungicidal concentrations of 180 and 360 g/mL, respectively. RBPHT also suppressed early biofilm establishment by C. albicans and C. auris and markedly reduced viable biofilm-associated populations when applied after initial cell adhesion. These findings provide the first evidence of antifungal and antibiofilm activity by a Capsicum seed-derived nsLTP-enriched fraction against C. auris and position Ca-nsLTP1 and Ca-nsLTP2 as promising plant-derived candidates for further antifungal development.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Structural deformations of lipid bilayers around membrane proteins inform oligomerization type](https://www.biorxiv.org/content/10.64898/2026.11.24.769041v1)
*Diaz Vazquez, G.; Condon, S. G. F.; Robertson, J. L.* · `biophysics` · bioRxiv doi:10.64898/2026.11.24.769041 v1 · relevance 0.08

- **In one sentence**: Coarse-grained molecular dynamics simulations of monomeric and oligomeric forms of ten channels and transporters in POPC bilayers compare membrane thickness, deformation energy, and lipid packing near protein-protein interfaces to test whether membrane defects encode oligomerization type.
- **In plain words**: Cell membranes are fatty sheets in which proteins often clump together into groups. This study used computer simulations of ten membrane channels and transporters, alone and in groups, to see how each protein bends and disturbs the surrounding fat layer. The authors report that every protein disturbs the membrane up to about 3 nanometers away, and that proteins which always assemble the same way show larger disturbances at their contact surfaces, which are reduced once they group together.
- **Why it matters**: It suggests that the shape of the surrounding membrane may help explain why some proteins form stable complexes and others do not, a question relevant to membrane biology and drug design. The text does not establish how general these findings are beyond the ten systems studied, so this should be read as a computational hypothesis rather than a settled result.
- **Background needed**: - Biological membranes are double layers of lipids (fat-like molecules) that act as a sheet with its own physical properties.
- Membrane proteins sit inside this sheet and can locally thin, bend, or pack the lipids around them.
- Oligomerization means several copies of a protein joining into one complex.
- Coarse-grained molecular dynamics is a simulation method that groups atoms into larger beads to model slow, large-scale motion over longer times.
- POPC is a common lipid used as a standard model membrane component.
- Membrane thickness, deformation energy, and lipid packing parameter are measures of how strained or disordered the membrane is near a protein.
- Obligatory or structurally monomorphic complexes always assemble in the same arrangement; homologs are related proteins from different species. · level: research-level

<details><summary>Original abstract</summary>

A functional definition of a membrane protein's structure is the three-dimensional arrangement of the polypeptide and the structure of the membrane around it. Biological membranes are composed of self-assembled lipid bilayers, with membrane proteins acting as inclusions that perturb this phase. These inclusions induce long-range changes in membrane structure and create an intrinsic, lipid-mediated driving force for membrane protein association. The question is how much different membrane protein folds shape their surrounding membrane to tune the affinity and specificity of this driving force. To investigate this, we conducted a computational study to evaluate whether different membrane protein oligomers exhibit characteristic membrane defects that indicate specificity in complexation. We performed coarse-grained molecular dynamics simulations of monomeric and oligomeric states of ten different channels and transporters in POPC bilayers and evaluated changes in membrane thickness, deformation energy, and lipid packing parameters. We found that all the proteins affect their surrounding membrane up to 3 nm from the protein surface. However, we observed larger defects at oligomeric interfaces for obligatory or structurally monomorphic complexes, suggesting that their oligomerization is partly driven by burial of membrane defects. In contrast, oligomers that adopt different quaternary structures across homologs show weaker perturbations at known binding interfaces, and larger perturbations at lipid-facing surfaces. Nevertheless, all systems show fewer membrane defects upon oligomerization, suggesting an underlying lipid-mediated driving force that each protein fold modulates to tune affinity via membrane-mediated oligomerization.

</details>

### [A spatiotemporal perturbational atlas of the post-pneumonectomy lung](https://www.biorxiv.org/content/10.64898/2026.11.25.768918v1)
*Obata, T.; Aracena, D. P.; Tomas Gracia, M. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.25.768918 v1 · relevance 0.08

- **In one sentence**: A spatiotemporal perturbational atlas of rat lung regeneration after pneumonectomy, combining scRNAseq, Xenium spatial transcriptomics, and NICHES-based spatial connectomics to describe three tissue states at Days 3, 7 and 14.
- **In plain words**: When one lung is surgically removed, the remaining lung must adapt and regrow its tissue. This paper maps how the cells and their chemical messaging change in space and over time in rats during that process. The authors report three different tissue patterns at successive time points, including a transient community at Day 7 marked by signaling the authors describe as fibrosis-mimetic and an apparent growth-related pattern at Day 14.
- **Why it matters**: Lung regeneration after pneumonectomy is a tractable model for how mammalian tissue repairs itself in place, which matters for understanding lung injury and scarring. The text does not show clinical implications, and the framework is described as generalizable but its performance against other methods is not detailed in the excerpt provided.
- **Background needed**: - Pneumonectomy: surgical removal of a whole lung; the remaining lung compensates and regrows tissue.
- Single-cell RNA sequencing (scRNAseq): measures which genes are active in each individual cell, used to identify cell types.
- Spatial transcriptomics (Xenium): measures gene activity while keeping each cell's location in the tissue intact.
- Cell-cell signaling / connectomics (NICHES): infers which cells are likely communicating with which neighbors, based on gene activity patterns.
- Mesothelium: the thin protective membrane lining the lung surface.
- Macrophages: immune cells that clear debris and send signals during tissue repair.
- Fibrosis: excessive scar-like tissue buildup; "fibrosis-mimetic" signaling refers to signals resembling those of scarring, not scarring itself.
- Perturbational atlas: a map of tissue changes measured after a deliberate disturbance, across time. · level: research-level

<details><summary>Original abstract</summary>

Perturbational spatial atlases have begun to map regenerative dynamics in a variety of tissues, yet lung remodeling has not been characterized at comparable spatial and temporal resolution. Post-pneumonectomy lung regeneration (PPLR) provides a tractable mammalian model for tissue regeneration that can be studied in situ. Here, we present a spatiotemporal perturbational atlas of PPLR in Rattus norvegicus, combining single-cell RNA sequencing (scRNAseq), high-resolution spatial transcriptomics (10x Genomics Xenium), and NICHES-based spatial tissue connectomics. We observe three distinct tissue architectures at successive timepoints after pneumonectomy, each characterized by coordinated shifts in local cellular composition and intercellular signaling. At Day 3 (D3), a line of interstitial macrophages colocalizes directly beneath an intact mesothelium among active mechanotransductive and inflammatory signaling. We also observe the unexpected appearance of a transitional remodeling cellular community at D7 which appears largely absent at later timepoints, marked by fibrosis- mimetic signaling. At D14, an alveologenic architecture at distal lung tissue displays a connectivity signature consistent with active de novo growth, distinct from baseline homeostasis. Our findings establish a spatiotemporal map of multicellular architecture during regenerative lung remodeling and introduce a generalizable framework for spatial connectomic analysis to be used in perturbational tissue systems biology.

</details>

## Neuroscience

### [Human iPSC-derived Olfactory Sensory Organoids model olfactory function and drug response](https://www.biorxiv.org/content/10.64898/2026.11.24.769047v1)
*Singh, V.; Pantula, A.; Joshi, K. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.24.769047 v1 · relevance 0.07

- **In one sentence**: The authors report human iPSC-derived olfactory sensory organoids that show cell-type diversity, developmental transcriptional programs matched to a fetal nasal atlas, spontaneous network bursting, and altered network activity after three kinase inhibitors (Dasatinib, Trametinib, Selumetinib).
- **In plain words**: Some drugs are being considered for delivery through the nose, which may bypass the blood-brain barrier to reach the brain. This paper describes a lab-grown, three-dimensional mini-tissue made from human stem cells that resembles the developing smell system. The researchers found that the tissue contains several cell types, shows electrical activity, and responds in measurable ways to three cancer-related drugs.
- **Why it matters**: Little is known about how drugs given intranasally affect human olfactory tissue, so a human model for testing this has practical value for safety and drug development. The text does not report any clinical or in vivo data, so its usefulness for predicting effects in patients remains to be tested.
- **Background needed**: - Organoid: a small, lab-grown 3D tissue made from stem cells that mimics some features of a real organ.
- Induced pluripotent stem cells (iPSCs): adult cells reprogrammed back to an early, flexible state so they can become many cell types.
- Olfactory sensory neurons: nerve cells in the nose that detect smells and send signals to the brain.
- Blood-brain barrier: a filter that limits which substances pass from the blood into the brain.
- Intranasal delivery: giving medicine through the nose, a possible route to the brain.
- Single-nuclei RNA sequencing: a method that reads which genes are active in individual cells, used to identify cell types.
- Kinase inhibitors: drugs that block certain enzymes (kinases) involved in cell growth; here they are relevant to glioma, a brain tumour.
- Network bursting: coordinated, rhythmic bursts of electrical firing across many cells. · level: research-level

<details><summary>Original abstract</summary>

Intranasal drug delivery is being explored as an alternative approach to overcome the blood-brain barrier in the treatment of central nervous system diseases. However, little is known about how therapeutics administered through this route affect human olfactory tissue. Here, we develop human induced pluripotent stem cell-derived olfactory sensory organoids that reproduce key cellular and functional features of the developing olfactory system. Over three months of differentiation, the organoids acquire diverse neuronal and glial-associated populations, including cells expressing markers of olfactory sensory neurons and interneurons. Single-nuclei RNA sequencing shows changes in cellular composition and lineage-associated transcriptional programs during maturation, while comparison with a human fetal nasal atlas identifies shared neural populations and developmental signatures. Alongside these molecular changes, the organoids develop spontaneous electrical activity and coordinated network bursting. Exposure to the glioma-relevant kinase inhibitors Dasatinib, Trametinib, and Selumetinib produces distinct changes in neuronal network activity, demonstrating the ability of the model to capture compound-associated functional responses. Together, these findings establish a human Olfactory Sensory Organoid system for investigating olfactory development and evaluating how therapeutics may affect olfactory neural tissue during intranasal drug administration.

</details>

### [Investigating Motor Skill Acquisition in Mice and Humans: Towards A Cross-Species Paradigm](https://www.biorxiv.org/content/10.64898/2026.11.20.768070v1)
*Hille, M.; Justus, L. C.; Zocher, S. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.20.768070 v1 · relevance 0.05

- **In one sentence**: A cross-species study that uses a matched chopstick grasping task in mice and humans, paired with structural and quantitative MRI before, during, and after training, to compare early brain changes linked to motor skill learning.
- **In plain words**: Scientists want to connect brain scans taken from living people with the cell-level changes seen in animal studies, but the two are hard to compare. This paper builds a similar reaching-and-grasping task for mice and people, trains some of each, and scans their brains over time. In mice, the motor-control area of the cortex shrank somewhat in trained animals; in people, no reliable change in overall gray matter volume appeared, but tissue-sensitive scan measures shifted in a way that may reflect more myelin (the fatty insulation around nerve fibers).
- **Why it matters**: It offers a way to line up human brain imaging with animal experiments, which could help interpret what MRI signals mean at the cellular level. The authors are careful to say that it is unclear whether the changes in the two species share a common biological mechanism, so the work is a starting point rather than a settled link.
- **Background needed**: - Motor skill learning: getting better at a movement such as grasping through practice.
- Single-pellet reaching task: a standard test in rodents where they reach through a slot to grab a food pellet.
- Structural MRI: scans that measure the size or volume of brain regions such as gray matter.
- Quantitative MRI (MTsat, R1): scan measures sensitive to tissue properties; these are often used as proxies for myelin content, which is an indirect inference.
- Myelin: the insulating layer on nerve fibers that can change with learning.
- Cross-species paradigm: an experiment designed to run the same kind of task in different animals, here mice and humans. · level: intermediate

<details><summary>Original abstract</summary>

Relating non-invasive observations of human brain plasticity to cellular processes identified in animal models remains a major challenge in neuroscience. We address this challenge by introducing a paradigm for studying motor skill acquisition across species. We designed a human chopstick grasping task modeled after the rodent single-pellet reaching task, resulting in a comparable sequence of reach-to-grasp movements across species. We studied 48 young adult male C57BL/6N mice and 71 young men, comparing trained groups with untrained controls. In both mice and humans, structural magnetic resonance imaging (MRI) was performed before, during, and after motor training. The functional form of behavioral performance gains on the trained task was highly similar across species. In trained compared to control mice, analysis of the early learning interval revealed decreases in regional volume in contralateral primary motor and forelimb somatosensory cortices, with greater volume reductions in primary motor cortex associated with better reaching performance. In humans, performance gains transferred to other chopstick tasks but not to general dexterity, and no reliable changes in gray matter volume were observed. Quantitative MRI, however, revealed early training-related changes in tissue-sensitive measures, including increases in magnetization transfer saturation (MTsat) and longitudinal relaxation rate (R1) in contralateral motor and frontal regions, potentially reflecting an increase in intracortical myelin. Thus, early structural changes in the contralateral motor cortex were detected in both species, but the degree to which these changes reflect a common biological mechanism is unclear. We conclude that the present cross-species paradigm provides a viable starting point for studying brain plasticity across species. Future work needs to relate macroscopic structural changes more directly to cellular processes by applying longitudinal microscopic imaging and MRI in the same animals.

</details>

## Genetics and genomics

### [The 'near T2T' Canton-S assembly is inconsistent with other Canton-S genomes](https://www.biorxiv.org/content/10.64898/2026.11.19.767897v1)
*Emerson, J. J.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767897 v1 · relevance 0.08

- **In one sentence**: A commentary arguing that the recently published "near T2T" genome assembly of the Drosophila Canton-S strain differs from three other independently sequenced Canton-S assemblies by an amount comparable to differences between distinct strains, raising doubts about its genetic identity.
- **In plain words**: Canton-S is a fruit fly strain that scientists have used for decades as a standard reference in many experiments. A recent project produced a very complete genetic "map" (genome assembly) of this strain, and this short note argues that the map does not match three other independent maps of the same strain. The author's concern is that the new map may not truly represent Canton-S, so labs should think carefully before adopting it.
- **Why it matters**: Canton-S is a common baseline in fly genetics and behavior research, so whether its reference genome is accurate affects many studies. The note is a single critical comparison, and the text provided does not show how the original authors respond, so the strength of the concern should be judged alongside their reply.
- **Background needed**: - Genome assembly: reconstructing an organism's full DNA sequence from short sequencing reads into long continuous pieces.
- "T2T" (telomere-to-telomere): an assembly covering each chromosome end to end, including repetitive regions; "near T2T" means nearly complete.
- Canton-S: a laboratory strain of the fruit fly Drosophila melanogaster, widely used as a "wild-type" reference.
- Strain identity: labs routinely have genetically distinct copies of "the same" strain; a reference genome should match the strain actually in use.
- Comparing assemblies: differences between independent assemblies of one strain are expected to be small; large differences can signal a different genetic background or assembly errors.
- Commentary: this is a short critical note, not a full study with new experiments as described in the text. · level: intermediate

<details><summary>Original abstract</summary>

Canton-S is among the most widely used Drosophila melanogaster strains, underlying substantial community infrastructure, including serving as a wild-type strain for: genetics studies; studying phenotypes, especially in behavioral studies; and complex trait mapping studies among many others. The recent 'near T2T' assembly of Canton-S (LIU et al.) is presented as delivering modern sequencing and assembly quality to the Drosophila community via this important strain. I find that this assembly is inconsistent with three other independently sequenced Canton-S genome assemblies on a magnitude comparable to differences between distinct strains, raising concerns about its genetic identity that the community should consider when choosing whether to adopt it as a resource.

</details>

### [Genomics of the diversification of Heliconius cydno (Lepidoptera: Nymphalidae) in northern South America: geographic and phenotypic patterns](https://www.biorxiv.org/content/10.64898/2026.11.20.768178v1)
*Arias Cardenas, A.; Rueda-M, N.; Arias, C. F. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.20.768178 v1 · relevance 0.07

- **In one sentence**: Whole-genome analysis of 133 Heliconius cydno butterflies that tests how Andean mountain uplift, geography and gene flow shaped its recent diversification, and maps the ivory:mir-193 locus behind a hindwing colour band that appears to have been passed to H. melpomene through introgression.
- **In plain words**: This study looks at a group of tropical butterflies whose wing patterns vary a lot from place to place in Central and northern South America. The researchers sequenced the complete genomes of 133 butterflies covering all the recognised subspecies, and asked how mountains, geography and interbreeding between species shaped how the group split apart. They found five of the fourteen described subspecies form distinct genetic lineages, and they traced one wing-pattern trait to a specific gene region.
- **Why it matters**: It shows how geography and mixing between related species can together drive the spread of a visible trait, and it adds a concrete genetic locus to the study of mimicry. The text does not report how strongly these findings generalise beyond these butterflies, so the wider significance is best treated as provisional.
- **Background needed**: - Heliconius butterflies are known for warning colours (aposematism) and for mimicry, where unrelated-looking species share patterns to deter predators.
- A subspecies is a geographic population with recognisably different traits; a monophyletic lineage is a group descended from one common ancestor.
- Introgression means genes moving between species through occasional interbreeding and hybrids.
- Andean orogeny is the uplift of the Andes mountains, which can split populations and create new ones.
- Gene flow is the exchange of genes between populations; cis-regulatory elements are DNA stretches that switch genes on or off, rather than encoding proteins.
- A microRNA (mir-193) is a short RNA that regulates other genes; ivory is a gene already known to affect wing patterns in this genus.
- Whole-genome sequencing reads the full DNA of each individual, allowing comparisons across populations. · level: research-level

<details><summary>Original abstract</summary>

The interplay between natural selection, gene flow, and geography is a key driver of population differentiation. This study investigates their influence on the recent adaptive radiation of Heliconius cydno, a mimetic and aposematic butterfly with striking variation in wing color pattern across its distribution in Central and northern South America. The genetic basis of this phenotypic diversity has a modular architecture, whereby a few key genes and cis-regulatory elements control differences among morphotypes. Using whole-genome sequences from 133 individuals representing all subspecies of H. cydno, we investigated (1) the role of Andean orogeny in its diversification and (2) the genetic basis of the variation in the hindwing white submarginal band, which to date, had remained unknown. First, we found that five of the fourteen described subspecies correspond to distinct monophyletic lineages and well-defined genetic clusters that originated in northwestern South America and later expanded into Central America and the Colombian inter-Andean valleys. Second, we observed signatures of genetic structure that were consistent with geographic patterns, particularly those associated with the inter-Andean region and Gorgona Island. Third, we identified ivory:mir-193 as the locus underlying variation in the white submarginal band on the hindwing. We also detected evidence of introgression suggesting that this trait was likely transferred from H. cydno to H. melpomene, contributing to the establishment of a novel mimicry ring with H. erato. Altogether, these findings highlight the roles of geography, genomic architecture, and introgression in the diversification of H. cydno.

</details>

## Cell and molecular biology

### [Comparative transcriptomic validation of candidate geroprotectors in human iPSC-derived neurons](https://www.biorxiv.org/content/10.64898/2026.11.23.768196v1)
*MacDonald, E. M.; Lloyd, N.; Skvir, N. J. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.23.768196 v1 · relevance 0.08

- **In one sentence**: Eight candidate anti-aging compounds were screened for transcriptomic (gene-expression) effects in human iPSC-derived neurons, finding that genetic background dominated variation, PI-103 suppressed the mTORC1 signature while inducing older-age-associated genes, and no single aging readout was sufficient to define geroprotection.
- **In plain words**: Researchers want faster ways to find drugs that slow the decline of aging tissues, since testing in mouse lifespans takes years. This paper tests eight candidate compounds on nerve-like cells grown from human stem cells, and measures which genes switch on or off in response. The cells did show tunable aging-related signaling, but most of the variation came from the donor's genetic background, and the compounds' effects varied by donor.
- **Why it matters**: A scalable human cell model could speed up geroprotector screening and show which tissue is affected, which lifespan studies do not. The text supports only a tentative case: the authors say no single readout is enough, and the approach needs more lineages and donors before it can resolve tissue- and donor-specific responses.
- **Background needed**: - Geroprotectors: compounds meant to slow aging-related decline, not just treat a single disease.
- iPSCs (induced pluripotent stem cells): adult cells reprogrammed back into a stem-like state, which can then be grown into other cell types such as neurons.
- Reprogramming resets epigenetic age: the process that makes these cells can erase the chemical "age marks" on DNA, so it is unclear whether they still reflect aging.
- Transcriptomics: measuring which genes are active in a cell, used here as a readout of drug response and of age-like patterns.
- mTORC1: a cell growth-control signaling pathway linked to aging; PI-103 is a compound that inhibits it.
- DCX and BDNF: genes tied to neuron development and survival.
- Excitatory neurons: the main signal-sending neurons in the brain; the paper compares drug-induced genes against two human reference datasets of these cells. · level: research-level

<details><summary>Original abstract</summary>

The discovery of geroprotectors, defined as interventions that slow aging-related deterioration and preserve function, remains constrained by reliance on lifespan studies. Lifespan studies take years, are costly and resource intensive, and return a whole-organism endpoint dominated in mice by neoplastic death. These studies cannot be readily scaled and do not specify which tissue(s) are protected by geroprotectors. Human induced pluripotent stem cell (iPSC)-derived cells provide a scalable alternative that enables defined lineages and genetically diverse donors to be studied in parallel. However, reprogramming resets epigenetic age, and whether iPSC-derived cells can report responses relevant to aging has remained unclear. Here, we evaluated eight candidate geroprotectors in iPSC-derived neurons using multiple classes of aging-associated transcriptomic readouts. Aging-associated pathways, including mTORC1 and MEK-ERK signaling, were intact and pharmacologically tunable in these cells. Genetic background accounted for most transcriptional variance, with compound responses differing in magnitude and reproducibility between donors. PI-103 suppressed the mTORC1 signature and increased DCX and BDNF expression, while also inducing genes associated with older age in two independent human excitatory-neuron references. These findings indicate that distinct aging measures capture different dimensions of drug response and that no single readout is sufficient to define geroprotection in our model. Together, these results support iPSC-derived cells as a scalable screening tool for candidate geroprotectors, enabled by the transcriptional aging readouts now available, with the potential to resolve tissue- and donor-dependent responses as additional lineages and donors are incorporated.

</details>

### [SimpleP2G: Importance of Image Encoders for Gene Expression Prediction from Pathology Images](https://www.biorxiv.org/content/10.64898/2026.11.23.768493v1)
*Wang, J.; Zhang, J.; Hsieh, C.-Y. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.23.768493 v1 · relevance 0.08

- **In one sentence**: This paper isolates the effect of the image encoder, prediction head, and spatial context in pathology-image-to-gene-expression prediction, and proposes SimpleP2G, a direct gene-query decoder over frozen Virchow2 embeddings, plus a cross-patch variant.
- **In plain words**: Researchers try to predict how active genes are in tissue from microscope images of tissue slides, a task called pathology-image-to-gene-expression prediction. Many past studies changed several things at once, so it was unclear what caused their gains. This paper tests the factors one at a time and finds that swapping in a stronger image encoder (Virchow2) usually helped most, while a simple decoder on top of those image features already performed well.
- **Why it matters**: The work suggests that improving the image representation may matter more than adding complexity to the prediction model, which could guide how future studies design controls. The text reports results on five HEST-1K datasets with two 200-gene panels; how well these findings carry to other tissues or tasks is not shown here.
- **Background needed**: - Gene expression: how strongly a gene is switched on in a cell, often measured by its activity level.
- Pathology slide images: microscope photos of stained tissue sections.
- Image encoder: a pretrained model that turns an image patch into a list of numbers (an embedding); here it is kept frozen, meaning its weights are not retrained.
- Prediction head / decoder: the final layer(s) that map those numbers to gene predictions.
- Spatial context: using neighboring tissue patches, not only the patch itself.
- PCC-200: Pearson correlation across 200 genes, a measure of how well predicted and true values track each other.
- Held-out slides: test tissue samples not used in training.
- Ablation: a test that removes or changes one component to see its effect. · level: research-level

<details><summary>Original abstract</summary>

Pathology-image-to-gene-expression (P2G) studies often change the prediction head, image encoder, and spatial context together, making performance differences difficult to attribute. We examine these factors through paired image-input controls and explicit input regimes. Our main comparison covers five HEST-1K datasets, two 200-gene panels, and three selected held-out slides per dataset, using validation-selected checkpoints. Across all five datasets, replacing conventional image inputs with Virchow2 improves mean PCC-200 in 39 of 40 method--dataset--panel comparisons, while one comparison decreases. We introduce SimpleP2G, a direct gene-query decoder over frozen embeddings, and SimpleP2G-cross, which adds spatially positioned neighboring embeddings. With shared Virchow2 features, SimpleP2G has the highest single-patch mean PCC-200 on all five datasets under both panels; the cross-patch variant leads on four of five datasets under each panel. Decoder and context ablations show that greater depth and broader context do not consistently improve prediction. Together, these results suggest improving image representations before adding prediction-head complexity: a direct decoder over frozen pathology embeddings already provides a strong baseline. We hope our reimplemented image-encoder-upgraded baselines and SimpleP2G models serve as transparent, reproducible, and strong controls for future P2G research.

</details>

## Immunology and microbiology

### [Toxoplasma gondii-induced NETs are mediated by CR3 engagement and the vital non-lytic NETosis pathway](https://www.biorxiv.org/content/10.64898/2026.11.25.769188v1)
*Martinez, M. A.; Valle, J. E. S.; Lima, T. S.* · `microbiology` · bioRxiv doi:10.64898/2026.11.25.769188 v1 · relevance 0.10

- **In one sentence**: In HL-60-derived neutrophil-like cells, Toxoplasma gondii (type I RH and type II PA7) triggers NET release that appears to be vital NETosis, mediated by complement receptor 3 (CR3, via CD11b) in the presence of opsonin-containing human serum.
- **In plain words**: This study looks at how immune cells called neutrophils respond to Toxoplasma, a parasite that infects roughly a third of people. The researchers grew a cell line into neutrophil-like cells, exposed them to two strains of the parasite, and watched whether they threw out sticky web-like traps made of DNA. They found that the cells released these traps quickly while most stayed alive, and that a surface receptor called CR3 appears to be involved.
- **Why it matters**: Neutrophils are a first line of defense, and this work suggests they can fight the parasite without dying, which changes how we think about their role in infection. It is a laboratory study on a cell line rather than real patient neutrophils, so how far these findings apply in living hosts is not established by the text.
- **Background needed**: - Neutrophils: the most common white blood cells, early responders to infection.
- NETs (neutrophil extracellular traps): web-like structures of DNA and antimicrobial proteins that catch and disable microbes.
- NETosis: the process of making NETs; traditionally it kills the cell, while "vital" NETosis releases DNA and leaves the cell alive.
- Toxoplasma gondii: a single-celled parasite; type I (RH) and type II (PA7) are lab strains that differ in virulence.
- HL-60: a human leukemia cell line that can be chemically turned into neutrophil-like cells for study.
- CR3 (complement receptor 3, CD11b/CD18): a receptor on neutrophils that binds coated (opsonized) particles.
- Opsonins: antibody or complement proteins that tag microbes so immune cells can grab them.
- Confocal microscopy and live/dead staining: imaging methods used to see DNA release and check cell membrane integrity. · level: research-level

<details><summary>Original abstract</summary>

Approximately one-third of the global human population harbors an infection with the protozoan parasite Toxoplasma gondii. The immune system exploits neutrophils and one of their effector mechanisms, neutrophil extracellular traps (NETs), as an attempt to capture and neutralize T. gondii. NETs, composed of DNA, myeloperoxidase, citrullinated histone 3, and elastase, play a dual role in pathogen entrapment and amplification of the immune response. Traditionally, NET release was considered to result in neutrophil cell death. However, studies have identified an alternative process, vital NETosis, that allows NET formation while maintaining cell viability. Although T. gondii induces NET formation, the associated molecular mechanisms are not fully understood, and the neutrophil fate is unknown. In this study, the promyelocytic cell line HL-60 was differentiated into neutrophil-like cells (NLCs) and infected with type I (RH) or type II (PA7) T. gondii. Extracellular DNA was found in increasing concentrations over time in both type 1 and type 2 T. gondii-infected NLCs. Immunofluorescence staining for DNA and citrullinated histone 3 at 4, 6, and 16 hours post-infection confirmed NET formation by confocal microscopy. Cell viability at 16 hours post-infection was assessed by live/dead staining and extracellular ATP measurement, revealing that most NET-releasing neutrophils retained membrane integrity, consistent with vital NETosis. Additionally, immunofluorescence microscopy at 15 and 30 minutes further confirmed the fast release of nuclear DNA, a hallmark of vital NETosis. The use of opsonin-containing human serum and an anti-CD11b blocking antibody identified complement receptor 3 (CR3) as a receptor mediating T. gondii-induced vital NETosis. These findings demonstrate that T. gondii triggers vital NETosis in neutrophils through a CR3-dependent mechanism, advancing our understanding of the innate immune response to this globally prevalent parasite and laying the groundwork for future investigations into the molecular pathways that may be therapeutically targeted to support neutrophil-mediated immunity during infection.

</details>

### [Oral microbiome and DNA virome profiling in pigs reveals age-associated dynamics and extracellular recovery of Streptococcus suis-associated phage lineages](https://www.biorxiv.org/content/10.64898/2026.11.21.768310v1)
*Osei, E. K.; Ornelas, M. A. S.; Garcia Manzanilla, E. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.21.768310 v1 · relevance 0.10

- **In one sentence**: Shotgun metagenomic profiling of oral fluids from pigs on 15 Irish farms, using paired bulk and virus-like-particle enrichment, maps age-linked succession in oral bacteria and DNA phages and identifies 26 viral operational taxonomic units predicted to infect Streptococcus suis.
- **In plain words**: Researchers sampled the mouth fluids of pigs at different ages on commercial farms and read the DNA of everything in them, both bacteria and the viruses that infect bacteria. They found that the communities of microbes and viruses change in a fairly predictable way as pigs grow older and move through dietary changes. They also identified a small set of viruses that are likely to attack Streptococcus suis, a pig pathogen.
- **Why it matters**: Pig herds are routinely affected by bacterial disease, and phages (viruses that infect bacteria) are being studied as possible alternatives or supplements to antibiotics. This catalogue of phages that may target S. suis could support later phage discovery work, but the text reports only sequence-based predictions, so any therapeutic use would still need laboratory and field testing.
- **Background needed**: - Microbiome: the community of bacteria and other microbes living in a body site, here the pig mouth.
- Virome: the set of viruses in a sample; this study focuses on DNA viruses.
- Phage (bacteriophage): a virus that infects bacteria.
- Shotgun metagenomics: sequencing all DNA in a sample at once and assigning reads to organisms, without culturing them.
- Virus-like particles (VLP) enrichment: a lab step that concentrates intact virus particles so their DNA can be sequenced separately from bacterial DNA.
- vOTU (viral operational taxonomic unit): a cluster of similar viral sequences treated as one viral "species" for counting.
- Streptococcus suis: a bacterium that causes disease in pigs and can occasionally affect people.
- Resistome: the collection of antibiotic resistance genes in a sample.
- Weaning: the transition when piglets stop nursing and move to solid feed. · level: research-level

<details><summary>Original abstract</summary>

The pig oral cavity is a critical interface for microbial transmission and herd health monitoring, yet its microbiome and virome remains poorly characterised. We performed shotgun metagenomic sequencing of oral fluids from pigs across 15 commercial farms in Ireland, using paired bulk and virus-like particles (VLP) enrichment to capture comprehensive microbial and DNA virome diversity. Microbial communities shifted progressively with age, with early post-weaning animals enriched in environmental genera such as Pseudomonas and Staphylococcus and later stages dominated by lactic acid bacteria and anaerobes. Only 20.6% of vOTUs could be assigned to a known genus, with the most abundant being Astrithrvirus, which increased with age. Both microbiome and DNA virome exhibited predictable, coordinated age-associated succession with strong cross-domain coupling supported by virus-host networks. Functional profiling of the microbiome revealed that predicted carbohydrate substrates tracked the dietary transitions, while accessory viral functions partitioned by lifestyle and host. The early post-weaning stage was characterised by high abundance of viral integration and excision functions, as well as elevated resistome diversity that was almost exclusively of prokaryotic origin rather than viral. Importantly, 26 of the 25,223 vOTUs identified were predicted to target Streptococcus suis, providing the first metagenomic catalogue of such phages from pig oral environments. These findings expand our understanding of oral microbiome-virome dynamics and establish a framework for integrated microbiome and viromics approaches that could enable therapeutic phage discovery and inform microbiome-targeted interventions in pig production systems.

</details>

## Cancer biology

### [Single-agent PD-L1 blockade and tumour volume in orthotopic GL261 glioma, with an exploratory lipid analysis of the treated tumours](https://www.biorxiv.org/content/10.64898/2026.11.22.768425v1)
*Carretero-Navarro, P.; Lopez-Larrubia, P.; Pacheco-Torres, J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.22.768425 v1 · relevance 0.07

- **In one sentence**: In mice with orthotopic GL261 glioma, single-agent anti-PD-L1 reduced MRI-measured tumour volume at day 14 in both an IDH1-wild-type and an IDH1-mutant line, with accompanying diffusion-imaging and exploratory ex vivo lipid changes.
- **In plain words**: Glioblastoma is a aggressive brain cancer that has not yet responded well to immunotherapy drugs that release the immune system's brake. This study tested an antibody against the PD-L1 checkpoint protein, used alone, in mice with a brain tumour grown from GL261 cells, and tracked tumour size over time with MRI scans. Treated mice had tumours about a third (IDH1-wild-type) to two-fifths (IDH1-mutant) the size of control tumours at day 14.
- **Why it matters**: The paper reports tumour volume with confidence intervals rather than only survival, which makes the size of the effect easier to judge. The lipid imaging is exploratory, so it suggests hypotheses about how treated tumours differ chemically rather than establishing a mechanism.
- **Background needed**: - Glioblastoma (GBM): an aggressive brain tumour in adults with poor outcomes.
- PD-L1 and checkpoint blockade: PD-L1 is a protein that tells immune cells to stand down; an antibody that blocks it can let immune cells attack the tumour.
- Orthotopic mouse model: tumour cells implanted in the same organ (here the brain) as in the human disease; GL261 is a common mouse glioma line.
- IDH1 mutation: a genetic change in some gliomas linked to better prognosis; the study compares a normal and a mutant version of the line.
- MRI tumour volume and diffusion imaging: MRI tracks tumour size; diffusion measures (apparent diffusion coefficient, fractional anisotropy) reflect how water moves through tissue.
- Linear mixed model: a statistical method for repeated measurements over time in the same animals.
- Mass spectrometry imaging: maps the chemical types of lipids across a tissue slice; sphingomyelin and phosphatidylcholine are fat-like membrane molecules. · level: research-level

<details><summary>Original abstract</summary>

Immune checkpoint blockade has not yet changed outcomes in glioblastoma (GBM), and in immunocompetent mouse glioma the effect of a single blocking antibody is usually reported as survival rather than as tumour volume with its own confidence interval. We treated mice bearing orthotopic GL261 gliomas with anti-PD-L1 as a single agent in an IDH1-wild-type and in an IDH1-mutant line, and followed tumour volume by MRI. At day 14, tumours of treated animals were 0.33 times the volume of control tumours in the IDH1-wild-type line (95 % CI 0.21 to 0.53; p < 0.001; 16 anti-PD-L1 and 20 control animals) and 0.42 times in the IDH1-mutant line (0.22 to 0.78; p = 0.006; 10 and 10 animals), from a linear mixed model of log tumour volume over days 8 to 16. Diffusion imaging of the same tumours gave a higher apparent diffusion coefficient in the treated IDH1-wild-type tumours, by 23 % over the whole tumour (p = 0.027), and lower fractional anisotropy in the treated IDH1-mutant tumours, by 25 % over the whole tumour (p = 0.023), and in the periphery of the IDH1-wild-type ones, by 24 % (p = 0.005). We also imaged the lipid composition of treated and control IDH1-wild-type tumours ex vivo by mass spectrometry imaging: relative to the healthy brain of the same section, sphingomyelin was higher in the treated tumours and phosphatidylcholine species shifted towards shorter chains (p = 0.016 for both). In orthotopic GL261 glioma, anti-PD-L1 as a single agent reduces tumour volume in the IDH1-wild-type and in the IDH1-mutant line.

</details>

### [CSF Boundary Disruption and Tumor-Dependent Patterns of Medulloblastoma Metastasis](https://www.biorxiv.org/content/10.64898/2026.11.23.768674v1)
*Ryan, l. N.; Jimenez Garcia, L.; Gross, A. C. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.23.768674 v1 · relevance 0.07

- **In one sentence**: In mouse xenograft models of medulloblastoma, the paper links disruption of cerebrospinal fluid-facing tissue boundaries and primary tumor growth pattern to spread, and shows that different medulloblastoma lines produce distinct metastatic distributions even when implanted at the same site.
- **In plain words**: Medulloblastoma is a childhood brain cancer that often spreads through the fluid surrounding the brain and spinal cord, and this spread is the main cause of death. The researchers implanted human tumor cells into mice, changed where the primary tumor sat relative to the fluid-facing surfaces, and tracked how the cancer spread through the brain and spine. They found that how the tumor grew at its edge, especially when it broke into fluid-facing boundaries, mattered more for spread than its size or location alone.
- **Why it matters**: The work offers a framework for asking why some tumors seed the spinal fluid and others do not, which could matter for future treatment of leptomeningeal spread. The text is a preclinical summary, so its findings come from mouse models and do not show direct clinical relevance yet.
- **Background needed**: - Medulloblastoma: the most common malignant brain tumor in children, arising in the cerebellum (the back part of the brain).
- Leptomeningeal metastasis: cancer spreading into the thin membranes covering the brain and spinal cord, where cerebrospinal fluid (CSF) flows.
- CSF: the clear fluid that cushions the brain and spinal cord; tumors that reach it can travel along the whole nervous system.
- Xenograft: human tumor cells grown in an immunodeficient mouse; "orthotopic" means implanted in the matching organ (here, the cerebellum).
- Bioluminescence: a light-emitting reporter used to track tumor burden over time in live animals.
- Metastatic topology: the pattern of where and how spread cancer is distributed across brain and spinal compartments. · level: research-level

<details><summary>Original abstract</summary>

Background: Leptomeningeal metastasis is the major cause of mortality in medulloblastoma, yet the mechanisms that facilitate dissemination are poorly resolved. Here, we leveraged preclinical models to define metastatic topology, the anatomical distribution and organization of disseminated disease across craniospinal compartments and ask how topology is influenced by cerebrospinal fluid (CSF) access, primary tumor anatomy, and tumor biology. Methods: Orthotopic D425 xenograft models were used to manipulate primary tumor geometry, defined by anatomical position of primary tumors within the cerebellum relative to CSF facing boundaries. Longitudinal bioluminescence, survival, primary growth architecture at the tumor host interface, CSF boundary breach, and craniospinal metastatic distribution were quantified. Additional medulloblastoma models MED411, MED2112, and CHLA-01-MED were implanted at a common midline cerebellar location to assess tumor-intrinsic contributions to metastatic topology. Results: While primary tumor geometry altered disease progression and survival, it did not significantly alter metastasis distribution. Strikingly, growth architecture and primary tumor burden correlated with dissemination. Despite their large size, circumscribed tumors frequently remained localized, whereas smaller, disruptive primary growth architecture was strongly associated with boundary breach, intracranial, and spinal dissemination. Conversely, when anatomical origin was held constant, distinct medulloblastoma models generated significantly different metastatic topologies. Conclusions: Disruption of CSF-facing anatomical boundaries is associated with distant dissemination, whereas the distribution of established metastatic disease differs substantially among medulloblastoma models despite standardized implantation conditions. These findings distinguish anatomical factors associated with dissemination from tumor-dependent patterns of metastatic colonization and establish an experimental framework for investigating the mechanisms underlying metastatic topology.

</details>

## Ecology and evolution

### [Trade-off between resource excretion and reliance maintains biodiversity of a cross-feeding mutualism](https://www.biorxiv.org/content/10.64898/2026.11.24.768994v1)
*Yu, Y.; Bisesi, A. T.; Mandyam Dhati, A. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.24.768994 v1 · relevance 0.10

- **In one sentence**: A mathematical model of a bacteria-yeast cross-feeding mutualism shows that high reliance on cross-fed resources, not just cheating by reduced excretion, can cause community collapse, and that a trade-off between excretion and reliance can allow several bacterial auxotrophs to coexist.
- **In plain words**: Some microbes trade nutrients: one species gives off a substance another needs, and receives something back. This paper uses a computer model of a bacteria-yeast pair, where bacteria break down lactose and share galactose with yeast in return for amino acids, to ask when such partnerships fall apart. The authors find that a species that depends heavily on what its partner provides can cause the community to collapse, even without cheating, and that trading off how much each species gives out against how much it relies on others can let several bacterial types live together.
- **Why it matters**: Cheaters are a standard worry for cooperative systems, and this text suggests dependence on a partner deserves equal attention as a source of instability. The link to wider biodiversity questions is stated in the text, but its reach beyond this model is not shown here.
- **Background needed**: - Mutualism: two species that both benefit from each other.
- Cross-feeding: one species' waste or secreted product becomes food for another.
- Auxotroph: an organism that cannot make a particular nutrient itself and must get it from outside.
- Excretion: releasing substances into the environment; here, how much a microbe gives to its partner.
- Reliance: how much a species depends on resources supplied by its partner.
- Cheater: a partner that takes benefits while giving less back.
- Phase diagram: a map showing which parameter combinations lead to stable coexistence versus collapse.
- Coexistence and biodiversity: several species persisting together in one community. · level: intermediate

<details><summary>Original abstract</summary>

Microbial mutualisms, in which species exchange resources through cross-feeding, are common in nature. Yet the stability of mutualistic interactions is debated, and cross-feeding communities are vulnerable to cheaters that benefit from the excretions of others but reduce or cease their own excretion of resources, which can lead to community collapse. Here, we demonstrate with a mathematical model that in addition to decreased excretion, increased reliance on cross-fed resources can also lead to community collapse. In a two-species model of bacteria that metabolizes lactose and provides yeast with galactose, in exchange for amino acids from yeast, we show that the set of excretion and reliance parameters that maximizes biomass is adjacent to a region of community collapse in the phase diagram. By expanding the model to include multiple bacterial auxotrophs competing for lactose and either separate or overlapping amino acids, we also demonstrate that a trade-off between reliance and excretion can enable coexistence within the bacterial mutualist guild. Finally, we show that intraguild coexistence of bacteria favors yeast, increasing biodiversity but decreasing total community biomass. Our results argue that the question of cheaters should be paired with analysis of reliance on mutualistic exchange, and that both of these parameters modulate biodiversity and the stability of mutualisms to collapse.

</details>

### [Sodium-enriched nectar increases seed set in low diversity prairies](https://www.biorxiv.org/content/10.64898/2026.11.25.769002v1)
*Darst, A. L.; Lamm, M. E.; Haddad, N. M.* · `ecology` · bioRxiv doi:10.64898/2026.11.25.769002 v1 · relevance 0.10

- **In one sentence**: A field experiment testing whether sodium-enriched nectar raises seed set in black-eyed Susan plants, and whether that effect depends on how diverse the surrounding prairie plant community is.
- **In plain words**: Flowers make nectar, a sugary liquid that feeds pollinating insects, and nectar can also carry small amounts of minerals like sodium, which plants do not need much of but many pollinators do. The researchers grew black-eyed Susan plants in soil with added sodium, placed them in prairie plots planted with either many or few plant species, and counted the seeds the plants produced. They found that sodium-enriched plants made more seeds in the low-diversity prairies but not in the high-diversity ones, while seed germination was unchanged.
- **Why it matters**: It suggests that a single mineral in nectar can affect plant reproduction, and that the surrounding plant community can change whether that effect shows up. The text does not show how far these results extend beyond this one plant species and these plots, so the wider importance is still open.
- **Background needed**: - Pollinators such as bees and butterflies visit flowers for nectar, and in doing so move pollen between plants.
- Seed set means the proportion of flower ovules that become seeds; it is a common measure of plant reproductive success.
- Germination rate is the share of seeds that sprout, which can differ from how many seeds are made.
- Sodium is a micronutrient: plants need very little, but animal pollinators seek it out.
- Context dependency means an effect seen in one setting may not appear in another, here a prairie with many versus few plant species.
- Black-eyed Susan (Rudbeckia hirta) is a common North American wildflower used as the study plant.
- The text is only an abstract-level summary, so details such as sample sizes and statistics are not available here. · level: intermediate

<details><summary>Original abstract</summary>

Plant-pollinator interactions depend on floral traits and background plant community properties, yet the role of nectar micronutrients in these interactions is poorly understood. Sodium is a micronutrient of particular interest because although plants need little to no sodium, animal pollinators require it. It is unknown whether sodium-enriched nectar increases plant fitness in animal-pollinated plants and how this may be affected by the broader plant community. To test this, we grew black-eyed Susan (Rudbeckia hirta) plants in sodium-enriched or control soil. We placed pairs of sodium-addition and control plants in prairies seeded with high or low diversity and measured seed set and germination rate. In a supplementary experiment, we explored differences in floral visitation. We found that black-eyed Susan plants grown in sodium-enriched soil had sodium-enriched nectar. Seed set increased in sodium-addition plants in prairies seeded with low diversity but not in prairies seeded with high diversity. Germination rate was not affected by sodium addition. Altogether, our study highlights the importance of considering both micronutrients and context dependency in understanding plant reproduction and complex species interactions.

</details>

## Plant biology

### [Whole-genome resequencing and indoor phenotyping resolve the genetic architecture of drought stress response in tepary bean](https://www.biorxiv.org/content/10.64898/2026.11.24.768977v1)
*Srinivasan, A.; Yu, L.; Nichols, R. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.24.768977 v1 · relevance 0.06

- **In one sentence**: Whole-genome resequencing of 363 tepary bean accessions combined with indoor drought and control phenotyping of 282 of them maps genetic loci for growth, water use and photosynthesis under drought versus well-watered conditions.
- **In plain words**: Tepary bean is a legume that grows in dry climates, but scientists know little about the genes behind its drought tolerance. The team sequenced the genomes of 363 bean lines, including wild, weedy, cultivated and breeding types, and grew 282 of them for two weeks at either well-watered or very dry soil levels while measuring growth, water loss and photosynthesis.
- **Why it matters**: The work points to which regions of the genome control drought response in a crop that is already adapted to arid land, which could help breeders targeting drought tolerance. The text does not show any direct field or yield testing, so its practical use remains to be tested.
- **Background needed**: - Genome resequencing: reading the DNA of many individuals to find small differences (SNPs, single-nucleotide polymorphisms).
- Association mapping: linking those DNA differences to measured traits across many lines to find candidate chromosome regions (loci).
- Accessions: stored seed samples of a crop, often from wild or traditional sources.
- Domestication: the process by which wild plants were selected by people for farming, which changed their genes.
- Evapotranspiration: water lost from soil and leaves together.
- Soil water-holding capacity: the maximum water soil can retain; 10% versus 60% here means severe versus moderate water supply.
- Rank-normalized: values converted to ranks so that statistical methods work more fairly.
- Cytokinin oxidase, CIPK1-clade kinase, LHCB5: gene families with known roles in plant hormones, stress signalling and light harvesting, respectively. · level: research-level

<details><summary>Original abstract</summary>

Tepary bean (Phaseolus acutifolius A. Gray) is an arid-adapted legume, whose drought resilience is widely reported but poorly resolved genetically. Here we resequenced 363 wild, weedy, cultivated and breeding accessions and recovered 6.9 million single-nucleotide polymorphisms (SNPs). We phenotyped 282 of the accessions for growth, evapotranspiration and photosynthesis over 14 days at 60% or 10% soil water-holding capacity. Cultivated and breeding lines grew roughly twice as fast as wild accessions, and the proportional reduction in growth under drought did not differ between these germplasm classes. Evapotranspiration separated the classes under full irrigation, but converged under drought, making it the most plastic trait we measured. Canopy density predicted how much water a plant used, but not how well it tolerated losing it. Association mapping across 104 rank-normalized measurements yielded 113 significant SNPs at 46 positions, which resolved to three drought and six control loci. Three drought loci corresponded to 98 of the 113 SNPs, with the largest one localized on chromosome 8. This locus separates wild from cultivated accessions, and resolves to no gene. Three of the eight remaining loci carry candidates whose interval, expression under drought and published mechanism agree: a cytokinin oxidase, a CIPK1-clade kinase and the antenna subunit LHCB5. The most structure-independent locus localizes to 26 kb but implicates genes with no published role in water relations. Growth under drought and control conditions therefore rest on separate genetic bases, and the variation with the largest effect under deficit lies in haplotypes affected by domestication.

</details>

### [An RHD6-directed gene network sustains root hair growth under combined low phosphate and salt stress in Arabidopsis](https://www.biorxiv.org/content/10.64898/2026.11.25.769266v1)
*Ibeas, M. A.; Perez, J.; Padilla, G. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.25.769266 v1 · relevance 0.06

- **In one sentence**: In Arabidopsis, induced expression of the transcription factor RHD6 kept root hairs elongating under combined low phosphate and salt, and RNA sequencing plus promoter and co-expression analyses yielded a candidate RHD6 target network, with HEC3 tested as a modulator of the root hair response.
- **In plain words**: Plants often face low phosphate in the soil and salty conditions at the same time, and both can stunt the tiny hair-like outgrowths on roots that help take up nutrients and water. The researchers screened 18 root-hair transcription factors (proteins that switch genes on and off) and found that switching on RHD6 kept root hairs growing under both stresses, while wild-type root hairs were held back. Gene activity measurements under the combined stress then gave a list of candidate genes that RHD6 may control directly.
- **Why it matters**: The work offers a resource of about 400 candidate RHD6 target genes and points to HEC3 as a possible regulator of root hair growth under combined stress. Whether these candidates matter for crop salt or phosphate tolerance is not shown in the text and would need further testing.
- **Background needed**: - Root hairs: thin extensions of root cells that grow to increase the surface for absorbing water and nutrients.
- Inorganic phosphate: a nutrient plants take up from soil; scarce in many soils.
- Salt stress: high sodium in soil that makes water harder for roots to take up and disrupts growth.
- Transcription factor: a protein that controls how strongly many other genes are turned on.
- RHD6 and HEC genes: plant transcription factors involved in root hair and cell growth; the text does not describe their wider roles.
- RNA sequencing: a method that measures how much of each gene's RNA is present, showing which genes are more or less active.
- Beta-estradiol-inducible lines: genetically modified plants in which a gene is switched on by adding a chemical, letting researchers control timing.
- T-DNA insertion mutants: plants with a foreign DNA fragment disrupting a gene, used to test that gene's function. · level: research-level

<details><summary>Original abstract</summary>

Phosphate deficiency and salinity can coincide, but how roots integrate the two stresses is poorly understood. Root hairs (RHs) elongate under low inorganic phosphate and are inhibited by salt. Screening {beta}-estradiol-inducible TRANSPLANTA lines for 18 RH-expressed transcription factors (TFs) in Arabidopsis (Arabidopsis thaliana), we found that induction of ROOT HAIR DEFECTIVE 6 (RHD6) maintained RH growth under combined low phosphate (5 {micro}M) and salt (100 mM NaCl), which inhibited wild-type RH growth. RNA sequencing of RHD6-induced roots under dual stress identified 1,811 differentially expressed genes. Up-regulated genes were enriched for RH differentiation, tip growth and cell wall organization; down-regulated genes were enriched for phenylpropanoid and suberin metabolism, hydrogen peroxide catabolism, photosynthesis and responses to wounding and jasmonic acid. Promoter motif scanning combined with ensemble co-expression analysis defined a core network of 396 candidate direct RHD6 targets, including 31 TFs. The TFs with the largest expression changes were HEC3, HEC1 and EIL4. In T-DNA insertion mutants, dual stress did not shorten hec3 RHs; eil4 and hec1 had shorter RHs on the control medium but no significant change in relative inhibition. These data provide a resource of RHD6-dependent genes and identify HEC3 as a modulator of the RH response to combined stress.

</details>

## Bioengineering and synthetic biology

### [Digital light processing of human-scale tissue-engineered heart valves](https://www.biorxiv.org/content/10.64898/2026.11.22.768423v1)
*Jafari, A.; Nemati, A.; Sarshoghi, A. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.22.768423 v1 · relevance 0.08

- **In one sentence**: A composite hydrogel ink (PEGDA, GelMA and methacrylated quince seed mucilage, called GPQuin) is used with digital light processing 3D printing to make human-scale trileaflet tissue-engineered heart valves, with initial mechanical, cell, implantation and pulse-duplicator tests.
- **In plain words**: Heart valves can fail, and replacements made from engineered tissue could avoid some problems of current options. This paper describes a new printable "ink" made from plant-derived and synthetic gel materials, which a light-based 3D printer used to build a full-size three-leaflet valve. The printed valves were checked for shape accuracy, stretch strength, cell compatibility, response after 12 weeks under the skin of animals, and how well the leaflets opened and closed under simulated pulmonary flow.
- **Why it matters**: Making a valve at real human size with separate leaflets and sinuses is a hard fabrication problem, and the paper reports that this ink can do it, which may matter for heart valve tissue engineering. The text reports only early-stage measurements, so its value for clinical use is not yet established.
- **Background needed**: - Heart valves control one-way blood flow; current replacements are mechanical or biological (animal or donor tissue) and have known drawbacks.
- Tissue engineering builds biological structures from scaffolds seeded with cells.
- Digital light processing (DLP) 3D printing cures a liquid resin layer by layer with projected light, allowing detailed shapes.
- Hydrogels are water-swollen gel networks; PEGDA is a synthetic gel, GelMA is a gelatin-based gel, and quince seed mucilage is a plant gum. "Methacrylated" means chemically modified so the material can be light-cured.
- Modulus and tensile strength describe stiffness and the stress a material withstands before breaking; elongation at break is how far it stretches.
- Micro-CT is X-ray imaging used to compare printed shape with the design.
- Induced pluripotent stem cells are adult cells reprogrammed into a flexible cell type; here they were turned into valve cells.
- A pulse duplicator is a lab pump that mimics heartbeat flow through a valve. · level: research-level

<details><summary>Original abstract</summary>

Tissue engineered heart valves (TEHVs) could overcome the complications of current heart valve replacement, such as immunologic events, degenerative fibrocalcific changes, and patient-prosthesis mismatch. Digital light processing (DLP) 3D printing enables creation of complex geometries; however, suitable (bio)inks remain limited. Here, a composite ink comprising poly(ethylene glycol) diacrylate (PEGDA), gelatin methacryloyl (GelMA), and methacrylated quince seed mucilage (QSGM), termed GPQuin, was developed for DLP printing of human-scale TEHVs. GPQuin enabled fabrication of a trileaflet TEHV with separated leaflets and anatomically inspired sinuses. Micro-computed tomography revealed mean positive and negative surface deviations of +214 and -248 micrometers, respectively. The printed hydrogels exhibited a tensile modulus of 117.2 +/- 15.5 kPa, an ultimate tensile strength of 113.2 +/- 17.4 kPa, and an elongation at break of 75.3 +/- 2.3%. Human induced pluripotent stem cell-derived valve cells attached to the hydrogel surfaces and remained predominantly viable over 14 days. After 12 weeks of subcutaneous implantation, the constructs showed a time-dependent inflammatory response. In a pulse duplicator under pulmonary loading, printed valves exhibited good cyclic leaflet opening and closing. Together, these findings establish GPQuin as a printable platform for human-scale valve scaffolds and support further investigation in heart valve tissue engineering.

</details>

### [BMP-2 Release from Biomaterial Carriers: Reporting Heterogeneity and the Limits of Cross-Study Prediction](https://www.biorxiv.org/content/10.64898/2026.11.13.766607v1)
*Zhou, W.; Zhou, L.; Hou, W. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.13.766607 v1 · relevance 0.08

- **In one sentence**: A preliminary meta-analysis compiling 79 published BMP-2 release experiments from 21 papers, testing whether carrier-family labels can predict release across studies with machine learning, and finding that gains largely disappear when whole publications are held out.
- **In plain words**: Bone-growth proteins (BMP-2) are often loaded onto carrier materials that release them slowly into the body. The authors gathered release data from 21 published papers, using an AI assistant plus human checking, to see whether earlier results could be used to predict new ones. They found that the data were reported inconsistently, and simple models only beat a basic baseline when test data came from the same studies as the training data.
- **Why it matters**: Predicting how fast a drug or growth factor leaves its carrier could help design bone-repair implants with less trial-and-error. The paper is useful mainly as a caution: it shows that apparent predictive accuracy can reflect study-specific effects rather than general patterns, and it points to better reporting as a fix. Its scale is small, and the text describes it as preliminary.
- **Background needed**: - BMP-2 (bone morphogenetic protein-2) is a signaling protein that promotes bone formation; it is used clinically but at high doses that cause side effects, so slow-release carriers are studied.
- "Release profile" means the percentage of the loaded protein that leaves the carrier over time.
- Carrier families are groups of materials (for example, types of scaffolds or coatings) used to hold the protein.
- Machine learning models learn patterns from data to predict outcomes; here the error is measured in log10 units, so a difference of 0.1 is a roughly 26% change in the value.
- Random hold-out validation tests on randomly chosen data points, which can mix in data from the same study; publication-grouped cross-validation holds out whole papers, a stricter test of generalization.
- Mean absolute error is the average size of prediction mistakes; lower is better. · level: research-level

<details><summary>Original abstract</summary>

Published release profiles offer a potential basis for predicting bone morphogenetic protein-2 (BMP-2) delivery from biomaterial carriers, but heterogeneous reporting and study-specific effects complicate their reuse in machine learning (ML) models. As a preliminary exploration, we compiled 79 release experiments and 487 time points from 21 publications with a workflow that combined a large language model assistant and human verification, and we examined data comparability and cross-study prediction with ML models. Only 38 experiments (48%) reported BMP-2 alone as a percentage of the loaded dose. Within individual studies, binding components and coating layers were associated with slower release, consistent with established carrier mechanisms. Using carrier family as the sole predictor, a family-median model and gradient-boosted decision trees achieved lower mean absolute errors than a global-median baseline under random hold-out validation (0.42 and 0.44 versus 0.52 log10 units). Publication-grouped cross-validation did not establish a corresponding improvement (0.57 and 0.48 versus 0.50). Only 10 of the 28 modeling experiments belonged to carrier families represented in the training data under this scheme, and carrier family was strongly associated with publication. These findings highlight the need to distinguish within-study interpolation from cross-study generalization. Broader coverage of each carrier family, quantitative formulation and assay descriptors, and accessible numerical source data are needed to support predictive modeling of BMP-2 release.

</details>

## Mathematical biology (arXiv)

### [Exclusion and internal structure in the association/dissociation kinetics of DNA-binding proteins in the fast diffusion limit](https://arxiv.org/abs/2611.33740)
*Xiangting Li, Tom Chou* · `q-bio.BM` · arXiv:2611.33740v1 · relevance 0.06

- **In one sentence**: A coarse-grained stochastic model, reduced to an effective Markov model and mean-field approximation, of how multi-state DNA-binding proteins with finite footprints and internal conformational switching adsorb, desorb, and slide along DNA in the fast-diffusion regime, fitted to RPA binding on ssDNA.
- **In plain words**: Many proteins that regulate DNA stick to it, slide along it, and let go again, and they can change shape while doing so. This paper builds a simplified mathematical model of that process, in which each protein takes up a certain stretch of DNA and can switch between shapes. The authors fit the model to previously published measurements of Replication Protein A (RPA), a protein that coats single-stranded DNA, and use it to examine how proteins that bind across several segments can exchange quickly while staying tightly bound.
- **Why it matters**: Tractable closed-form models of how sliding, crowding and shape changes interact could help researchers interpret binding-kinetics experiments on DNA-processing proteins. The text claims broad applicability to nucleosomes and other systems, but that is a claim the abstract makes and has not been tested here, so its reach beyond RPA is uncertain.
- **Background needed**: - DNA-binding proteins: proteins that attach to DNA and regulate or copy it.
- Nonspecific binding: sticking to DNA regardless of its exact sequence.
- Adsorption/desorption: attaching to and detaching from a surface, here DNA.
- Fast diffusion limit: the regime where a protein slides along DNA much faster than it detaches, so it can be averaged over.
- Footprint: the length of DNA a single bound protein covers, which blocks neighbours (exclusion).
- Markov model: a model where the next state depends only on the current state, with fixed switching rates.
- Mean-field approximation: replacing detailed interactions with averaged effects to get simpler equations.
- Facilitated exchange: a bound protein's neighbour or partly bound state speeding up swapping of proteins on DNA.
- RPA: a single-stranded DNA-binding protein involved in DNA replication and repair. · level: research-level

<details><summary>Original abstract</summary>

In many canonical biophysical and biochemical contexts, complex diffusing DNA-binding proteins undergoing nonspecific adsorption and desorption can exist in different conformational states. Equilibrium binding theories and kinetic models of competing ligands provide a basis for describing these systems. Coupling the internal conformational kinetics of bound proteins to exclusion and diffusion requires tracking both protein positions and binding states. Closed-form, tractable mathematical models that accurately describe the stochastic dynamics of structured proteins that bind to and diffuse along DNA are lacking. Here, we develop a new coarse-grained stochastic model of nonspecific DNA-protein binding in the fast diffusion regime, from which we derive an effective Markov model and its corresponding mean-field approximation that incorporates protein footprint size and conformational switching. We fit our new model quantitatively to previously measured dynamics of Replication Protein A (RPA) binding to ssDNA. Finally, by including multisegment binding states, our analysis captures facilitated exchange, revealing how multisegment architecture balances high affinity with rapid remodeling. Our theoretical model applies broadly to many other DNA-binding protein systems, including nucleosomes, ssDNA-binding proteins, and other multisegment complexes, providing accurate predictions and new strategies for evaluating experimental data.

</details>

### [A multi-patch model for sylvatic hematophagous vector dynamics: the impact of landscape anthropization](https://arxiv.org/abs/2611.34735)
*Ivric Valaire Yatat-Djeumen, Lukas Eigentler, Orville Wright Happi-Tchakount\'e et al.* · `q-bio.PE` · arXiv:2611.34735v1 · relevance 0.06

- **In one sentence**: A multi-patch mathematical model of tsetse fly and wild animal populations in Cameroonian districts, in which human landscape change (anthropization) alters animal carrying capacity and drives dispersal under three dispersal rules, analysed for equilibria, stability, and invasion speed via pulled traveling waves.
- **In plain words**: This paper builds a computer model of how blood-feeding flies (tsetse flies) and the wild animals they feed on spread across a set of connected local areas, as human settlement and land use change the landscape. The authors fitted the model to districts in Cameroon and compared three ways animals and flies might move between areas. They report that how animals disperse matters a lot: under one rule, more human-altered areas speed up invasion, while under a more realistic local-neighbour rule they can either speed it up or have no effect.
- **Why it matters**: Tsetse flies carry trypanosomes, the parasites behind sleeping sickness and nagana in livestock, so understanding how their populations spread as land changes bears on disease risk. The text only supports modelling conclusions, and it itself says more empirical data on animal dispersal are needed, so its practical implications are uncertain.
- **Background needed**: - Patch model: the landscape is split into connected local areas ("patches"), each with its own population that grows and exchanges individuals with other patches.
- Carrying capacity: the maximum population an area can sustain given its resources.
- Anthropization: the degree to which an area is changed or shaped by humans.
- Equilibrium and local stability: a steady population level, and whether small disturbances die out and return to it.
- Pulled traveling wave: a model of a population front moving outward into empty territory, used here to estimate invasion speed.
- Tsetse flies (Glossina): blood-feeding insects that transmit trypanosome parasites to humans and animals. · level: research-level

<details><summary>Original abstract</summary>

We develop a multi-patch model for sylvatic hematophagous vector--(wild) animal interactions with nonlinear migration terms that depend on landscape anthropization. Every patch is a suitable habitat for both animals and vectors, but anthropization reduces the animal carrying capacity and induces animal and vector displacement. We considered three dispersal types. Under unconstrained global dispersal, displaced individuals can move to any other patch. Under the more realistic random and constrained neighbor dispersal, displaced animals move to a neighboring patch chosen either at random or preferentially among less anthropized ones. We parameterized our model for tsetse flies (Glossina spp.) in the districts of Campo, Ny\'e'\'et\'e, and Ma'an, Ocean division, Cameroon. We characterized the equilibria and their local stability analytically for unconstrained global dispersal, and found numerically that, under both neighbor dispersal regimes, populations progressively expand before settling into a stable equilibrium. Under random neighbor dispersal, the effect of anthropization on migration had a much larger impact on steady state densities than its effect on animal carrying capacity. Under constrained neighbor dispersal, populations spread noticeably more slowly, and numerous patches maintained extremely sparse populations. We further investigated invasion speed under different anthropization scenarios. For random neighbor dispersal, invasion times decreased upon introduction of newly anthropized regions, while for constrained neighbor dispersal, anthropized regions either increased or did not affect invasion times. Approximating invasions by pulled traveling waves, we found that anthropized regions act as ``invasion highways'' or ``invasion barriers'' depending on the dispersal type. We conclude that more empirical data on animal dispersal are needed to understand these dynamics.

</details>

## Epidemiology

### [Productivity-adjusted life years lost due to type 2 diabetes by socioeconomic position in Germany between 2022 and 2060](https://www.medrxiv.org/content/10.64898/2026.11.20.26368491v1)
*Piedboeuf-Potyka, K.; Hering, R.; Schulz, M. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.20.26368491 v1 · relevance 0.04

- **In one sentence**: A projection study estimating age- and sex-specific productivity-adjusted life years (PALYs) lost to type 2 diabetes across socioeconomic groups among German working-age adults, 2022 to 2060.
- **In plain words**: This paper looks at how type 2 diabetes costs people and the economy in lost working years, both from dying early and from being less productive while still alive. The authors used an existing projection model and public German data to estimate these losses for men and women at low, medium and high socioeconomic position (a measure of income, education and occupation). They report that losses were largest for people with low socioeconomic position and that the total is expected to rise by 2060, mainly because more people will have the disease.
- **Why it matters**: It puts a number on the economic cost of a common chronic disease and shows that this cost falls unevenly across social groups, which may matter for prevention and workplace policy. The text does not describe policy recommendations, so any link to practice is an inference the reader should check against the full paper.
- **Background needed**: - Type 2 diabetes: a long-term condition in which the body does not regulate blood sugar well; it is strongly linked to lifestyle and age.
- PALY (productivity-adjusted life year): a measure combining years of life lost with years of working productivity lost, so that early death and reduced work both count.
- Years of life lost (YLL) and years of productivity lost (YPL): the two components of PALYs.
- Presenteeism: being at work but less effective because of illness; absenteeism: missing work; reduced labour force participation: leaving or not entering paid work.
- Socioeconomic position (SEP): a person's standing based on factors such as education, occupation and income.
- Projection model: a computer model that estimates future numbers from current trends and assumptions.
- Confidence interval (CI): a range that reflects statistical uncertainty around an estimate. · level: research-level

<details><summary>Original abstract</summary>

IntroductionType 2 diabetes can impair productivity during working age (20-69 years), causing substantial economic burden at individual and at population level. We aimed to estimate age- and sex-specific productivity-adjusted life years (PALYs) lost due to type 2 diabetes by socioeconomic position (SEP) between 2022 and 2060 in Germany. MethodsWe used an established projection model and nationally representative, publicly available German data to estimate age- and sex-specific PALYs lost due to type 2 diabetes by SEP among working-age adults, accounting for future incidence trends. PALYs lost were calculated as the sum of years of life lost (YLL) and years of productivity lost (YPL) due to reduced labour force participation, presenteeism, and absenteeism, using SEP-specific estimates from representative studies. ResultsProductivity losses were highest among persons with low SEP, followed by those with medium and high SEP. In 2022, 20-year-old men with type 2 diabetes and low, medium, and high SEP were projected to lose 11.32 PALYs (95% confidence interval (CI) 7.99-14.56), 8.19 PALYs (95% CI 6.01-10.33), and 3.78 PALYs (95% CI 0.89-6.72), respectively, by age 69 compared with men without type 2 diabetes, mainly driven by YPL. A comparable socioeconomic gradient was observed among women and remained largely unchanged until 2060. At the population level, an estimated 9.5 million PALYs (95% CI 6.42-12.58) were lost due to type 2 diabetes in 2022 in both sexes. This number is projected to increase to 9.5-13.5 million by 2060, mainly driven by the projected increase in the number of persons with type 2 diabetes. ConclusionType 2 diabetes-related productivity losses were shaped by SEP, sex and the future number of persons with the disease. PALYs lost declined with age and were predominantly driven by YPL.

</details>

### [Place or placeholder? AlphaEarth satellite embeddings did not detectably improve weekly dengue forecasts in four countries](https://www.medrxiv.org/content/10.64898/2026.11.23.26368794v1)
*Patel, B. K.; Asokan, A. V.; Pant, S.* · `epidemiology` · medRxiv doi:10.64898/2026.11.23.26368794 v1 · relevance 0.03

- **In one sentence**: A retrospective test of whether AlphaEarth satellite embeddings improve weekly district dengue forecasts in Brazil, Colombia, Peru and Taiwan, with a location-only control to check whether any gain is just place recognition.
- **In plain words**: The paper asks whether a set of satellite-derived numbers describing each area helps predict how many dengue cases will occur in each district one and four weeks ahead. The authors tested this on about 6,900 districts across four countries from 2020 to 2024, using a standard machine-learning model. They found no clear improvement after correcting for multiple comparisons; a few results were small losses, and in most comparisons the effect was too small to rule out a difference.
- **Why it matters**: Satellite-based environmental data are increasingly added to disease forecasts, so it matters whether they add real accuracy or mainly help the model recognise places it has already seen. The study suggests such inputs should be checked against simple location controls, especially in places the model has not seen before, though its findings are limited to these four countries and this model type.
- **Background needed**: - Dengue: a mosquito-borne viral illness; weekly case counts vary by place and season.
- Forecast accuracy: measured here with a weighted interval score, where lower error is better.
- AlphaEarth embeddings: compressed numerical summaries of satellite imagery for each location, not direct weather measurements.
- Location control: an input that only identifies a district, so any gain from embeddings can be separated from simply knowing which place it is.
- Gradient boosting: a standard machine-learning method that combines many simple decision rules.
- Diebold-Mariano test: a statistical test comparing the forecast errors of two models.
- Holm correction: an adjustment that reduces false positives when many comparisons are made.
- Held-out places or years: data withheld from training to test performance on unseen areas or future time periods. · level: research-level

<details><summary>Original abstract</summary>

Background. Some recent disease forecasts use satellite embeddings (numbers summarising places). A model may use them only as a placeholder, recognising districts and their usual dengue levels without learning about the environment. We asked whether AlphaEarth embeddings improve weekly district dengue forecasts and whether gains go beyond such recognition. Methods. We retrospectively forecast cases one and four weeks ahead in 6,909 districts of Brazil, Colombia, Peru and Taiwan (OpenDengue, 2020-2024) with gradient boosting. In 14 comparisons across future years and held-out places, we measured how embeddings changed the weighted interval score, with and without a location control (an input that only identifies a district), to test whether location alone explains gains. We used Diebold-Mariano tests, the Holm correction and a +/-1% equivalence margin set after the first Brazil and Peru results. Findings. No comparison showed a significant gain after correction. Six showed losses: five small (-0.42% to -0.68%) and one with Taiwan held out (-18.3%; absolute -0.0037). Only Colombia's held-out-states loss (-0.52%) stayed significant under two stricter checks and a check for cases hidden in zero-filled weeks. In 8 comparisons (5 under the stricter checks), any gain or loss was shown to be smaller than 1% of forecast error. This margin is roughly Brazil's gain from all non-case inputs combined. In exploratory analyses, embeddings alone predicted district burden in unseen states. Without case history, neither coordinates nor embeddings helped detectably in Brazil's held-out states; both hurt in Colombia's. In Brazil's future years, coordinates cut error by 3.3% (1.7 to 4.9); embeddings added nothing detectable. Interpretation. Embeddings partly showed which districts usually have more dengue, but in Brazil and Colombia other non-case inputs already held most of it. With case history they added no detectable accuracy; without it, evidence was inconclusive. Embeddings should be tested against location-only controls in held-out places.

</details>

## Infectious diseases

### [Safety and microbiological activity of a combined phage cocktail in persons with cystic fibrosis colonized with Achromobacter: Study protocol for a phase 1, investigator-initiated, randomized clinical trial.](https://www.medrxiv.org/content/10.64898/2026.11.22.26368705v1)
*Massey, J.; Hughes Kramer, K.; Snook Barrett, S. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.22.26368705 v1 · relevance 0.05

- **In one sentence**: A study protocol for a small, open-label phase 1 trial testing the safety and early biological effects of a four-phage cocktail (AchromoPhage) against Achromobacter lung infections in adults with cystic fibrosis, given intravenously, by inhalation, or both.
- **In plain words**: People with cystic fibrosis can develop lung infections from a hard-to-treat bacterium called Achromobacter, which often resists antibiotics. This document describes a planned trial of a mixture of four viruses that infect and kill these bacteria (phages), testing whether it is safe and how the viruses behave in the body. The trial plans to enroll 12 adults, randomized into three groups that receive weekly doses over about seven weeks by different routes.
- **Why it matters**: Phage therapy is an older idea being revisited as antibiotic resistance grows, but controlled human trials are still rare, and this one is among the first to target Achromobacter in people with cystic fibrosis. The text is a protocol, so it reports no results; its value lies in how the trial will be run and what it will measure, and whether phages prove useful will depend on data not yet available.
- **Background needed**: - Cystic fibrosis (CF) is an inherited disease that causes thick mucus in the lungs, making chronic bacterial infections common.
- Achromobacter is a group of Gram-negative bacteria (a bacterial category with a protective outer membrane) that is often resistant to multiple antibiotics.
- Bacteriophages ("phages") are viruses that infect bacteria; "obligately lytic" means they only reproduce by bursting the bacterium open, which makes them candidates for killing it.
- A phase 1 trial mainly checks safety and dosing in a small group, not whether a treatment works.
- Pharmacokinetics describes how a drug is absorbed, distributed, and cleared from the body.
- A neutralizing antibody response means the immune system makes antibodies that block the treatment.
- FEV1 is a standard breathing test measuring how much air a person can forcibly exhale in one second. · level: intermediate

<details><summary>Original abstract</summary>

BackgroundAchromobacter are a genus of difficult-to-treat, frequently multi-drug-resistant Gram-negative bacteria that can cause severe infections in people with cystic fibrosis (pwCF). Bacteriophages are an understudied yet promising therapy for these and other antibiotic-resistant bacteria. However, data are largely limited to case reports or series, and clinical trials among pwCF to date have not evaluated Achromobacter. MethodsThis is an investigator-initiated, open-label, randomized phase 1 pilot trial to evaluate the safety, tolerability, and biological effects of AchromoPhage, a cocktail of four genetically distinct, obligately lytic Achromobacter-targeting phages (phiACH01, phiACH04, phiACH06, phiACH07) with broad activity against Achromobacter species, in 12 adult participants with CF and pulmonary Achromobacter infection. Twelve participants will be randomized into three groups to receive a total of three, increasing, weekly doses of the AchromoPhage cocktail via one of three routes: 1) intravenous, 2) via inhalation, or 3) or intravenously and inhaled. Participation in the trial will span approximately 7 weeks, which will consist of outpatient phage dose administrations, safety and symptom monitoring, and longitudinal collection of biospecimens for protocol-specified and exploratory analyses through Day 42. The primary safety endpoint is the occurrence of treatment-related Grade 4 or greater adverse events. Secondary endpoints include longitudinal changes in FEV1 by spirometry, longitudinal changes in health-related quality of life, pharmacokinetics of each of the four phages in blood and the respiratory tract, and emergence of a phage neutralizing antibody response in serum. DiscussionWhile existing case anecdotes and observational studies suggest that phages are safe and may have a role in treating human infections, there is a paucity of clinical trials studying the adverse effect profile and basic pharmacological parameters of phages. This trial will study the safety and explore the pharmacokinetic and other properties of a four-phage cocktail in patients with CF and chronic Achromobacter lung infection. Trial registrationClinicalTrials.gov NCT0727590. Registered on 12/10/2025 Structured summary O_TBL View this table: org.highwire.dtl.DTLVardef@137a67forg.highwire.dtl.DTLVardef@9415eaorg.highwire.dtl.DTLVardef@2af58borg.highwire.dtl.DTLVardef@5ea8f9org.highwire.dtl.DTLVardef@a79fbb_HPS_FORMAT_FIGEXP M_TBL C_TBL Protocol versionAchromoPhage Protocol August 26, 2026. Version 2.0

</details>

## Public and global health

### [Community-Based Hypertension Screening in Urban and Rural Zimbabwe: A Comparative Analysis and Implementation Lessons (2022-2025)](https://www.medrxiv.org/content/10.64898/2026.11.23.26368728v1)
*Chimberengwa, P. T.; Masiye, K.; Bepe, T. O. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368728 v1 · relevance 0.06

- **In one sentence**: A retrospective comparison of community health worker-led hypertension screening in urban (Phase 1, adults 40+) and mostly rural (Phases 2-3, adults 18+) Zimbabwe, using routine district programme data from 2022-2025.
- **In plain words**: This paper looks at a programme in Zimbabwe where trained community health workers used blood pressure machines to screen adults and refer those with high readings to clinics. The authors compared the share of people flagged with high blood pressure between an early urban phase and later phases that covered mostly rural areas. Positive results were far more common in the urban phase (41%) than in later phases (14.5%), and in both periods the share rose with age.
- **Why it matters**: Community-based screening is one way to find people with high blood pressure who would otherwise go undiagnosed, which matters across sub-Saharan Africa. The paper is mainly a programme report, and the authors themselves say the difference between phases likely reflects who was screened (age limits and population mix) rather than the programme's effect, so it does not show whether the screening improves health.
- **Background needed**: - Hypertension means high blood pressure, a major risk factor for heart disease and stroke.
- Community health workers (CHWs) are lay health workers trained to do basic tasks, such as screening, in local communities.
- Decentralized care means providing services closer to where people live rather than only in central hospitals.
- Positivity rate is the share of people screened who are flagged as having the condition.
- A retrospective analysis uses data that were already collected, rather than a new trial.
- The study uses aggregate data from the District Health Information System 2, a national routine reporting system.
- Confidence intervals show the range of values the true figure plausibly falls within.
- The paper notes that linkage to care, treatment, and long-term blood pressure control were not measured. · level: intermediate

<details><summary>Original abstract</summary>

Introduction Hypertension is a leading cause of cardiovascular disease and a growing public health challenge in sub-Saharan Africa. Community-based screening delivered through community health workers (CHWs) may improve early detection and strengthen decentralized chronic disease services, particularly in underserved settings. This study compared hypertension screening yield across phased implementation of a community-based programme in urban and rural Zimbabwe and documented implementation lessons for decentralized hypertension services. Methods A retrospective comparative analysis was conducted using aggregate programme data routinely captured in the District Health Information System 2. Screening outcomes from Phase 1 (2022-2023) were compared with those from the combined Phase 2 and Phase 3 implementation period (2024-2025). Trained CHWs used digital blood pressure devices to screen adults in communities and outreach settings, refer individuals with elevated blood pressure to primary healthcare facilities, and support follow-up. Phase 1 was implemented in urban districts and targeted adults aged [&ge;]40 years, while subsequent phases expanded to adults aged [&ge;]18 years and predominantly rural and peri-urban populations. The primary outcome was hypertension screening positivity, while secondary outcomes included participant characteristics and age-specific positivity rates. Results A total of 410,568 adults were screened, including 120,144 urban adults aged [&ge;]40 years in Phase 1 and 290,424 adults in Phases 2 and 3. Among participants in Phases 2 and 3, 76.0% resided in rural communities, 64.9% were female, and 44.9% were living with HIV. Hypertension positivity was 41.0% (49,276/120,144; 95% CI 40.7%-41.3%) in Phase 1 and 14.5% (41,972/290,424; 95% CI 14.3%-14.6%) in Phases 2 and 3 (p<0.001). Positivity increased significantly with age in both periods, ranging from 31.8% to 51.6% in Phase 1 and from 13.5% to 28.4% in later phases (all p<0.001). Conclusion Community-based hypertension screening delivered by CHWs successfully reached large urban and rural populations and identified substantial hypertension burden, particularly among older adults. The lower positivity observed in later phases likely reflects differences in age eligibility and population mix rather than programme effect. Scaling CHW-led screening may strengthen decentralized hypertension detection, although nationally representative surveys and longitudinal studies are needed to assess linkage to care, treatment initiation, and long-term blood pressure control. Key Words Hypertension; Community health workers; Community-based screening; Primary healthcare; Decentralized care; Zimbabwe.

</details>

### [Monitoring SNAP and Food Insecurity After the One Big Beautiful Bill Act: Early Evidence from a National Longitudinal Cohort](https://www.medrxiv.org/content/10.64898/2026.11.19.26368514v1)
*Robertson, M.; Sanborn, J.; Penrose, K. et al.* · `health policy` · medRxiv doi:10.64898/2026.11.19.26368514 v1 · relevance 0.05

- **In one sentence**: A short early-monitoring study of a national community-based cohort (844 low-income adults) tracking SNAP receipt and food insecurity from August 2025 to March 2026, after the OBBBA tightened SNAP eligibility and work requirements, comparing states that had and had not begun enforcing the expanded work rule.
- **In plain words**: In July 2025 a new US federal law, the One Big Beautiful Bill Act, made it harder to qualify for SNAP (the food assistance program often called food stamps) and added stricter work requirements. This study followed about 844 lower-income adults from August 2025 to March 2026 to see how many still got SNAP and how many struggled to afford food. Over that period, the share receiving SNAP dropped slightly, from 40.4% to 38.4%, while the share screening positive for food insecurity rose from 48.1% to 51.2%.
- **Why it matters**: It offers early, direct evidence on how a major change to a large food program may be affecting household food hardship, at a time when the federal government has also scaled back some food insecurity tracking. The text reports no clear difference between states that started enforcing the work rule sooner and those that did not, and the study is an early snapshot, so its findings should be read as preliminary.
- **Background needed**: - SNAP: the US federal program giving monthly food benefits to low-income households.
- Work requirement: a condition that some adults must work or train a set number of hours to keep benefits; the text says the OBBBA expanded it.
- Food insecurity: a household lacking reliable access to enough affordable, nutritious food; "screening positive" means a short questionnaire flagged it.
- Federal poverty guideline: the income threshold the government uses to define poverty; 200% of it is used here as the cutoff for low income.
- Longitudinal cohort: the same group of people surveyed repeatedly over time, which allows tracking change within individuals.
- Early-evidence caveat: the study covers only about seven months and a single cohort, so its trends may not hold over time or generalize to all US adults. · level: intermediate

<details><summary>Original abstract</summary>

The One Big Beautiful Bill Act (OBBBA), signed in July 2025, restricted eligibility for the Supplemental Nutrition Assistance Program (SNAP) and expanded its work requirement, while federal tracking of food insecurity was scaled back. Using a national, community-based longitudinal cohort, we examined changes in SNAP receipt and food insecurity between August 2025 and March 2026 among 844 adults with household income below 200% of the federal poverty guideline, comparing participants in states that had and had not begun enforcing the expanded work requirement. SNAP receipt fell from 40.4% to 38.4%, and the share screening positive for food insecurity rose from 48.1% to 51.2%, with no detectable difference by state implementation timing. Adults who discontinued SNAP were as likely to be food insecure (71.1% in March 2026) and as worried about affording food, housing, and utilities as those who continued SNAP, and few had moved above 200% of the poverty guideline. These early findings suggest that need persisted after SNAP ended. As enforcement expands, policy makers should consider measures that keep benefits flowing to eligible people, such as extended certification periods and simplified recertification, and should support longitudinal monitoring of food insecurity.

</details>

## Psychiatry and neurology

### [Chronic pain and cognitive performance in dementia caregivers: Insights from the STELLA and DETECT-AD studies](https://www.medrxiv.org/content/10.64898/2026.11.24.26368703v1)
*McClure, C.; Mattek, N.; Kaye, J. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.24.26368703 v1 · relevance 0.09

- **In one sentence**: A secondary analysis of 12-month data from the STELLA and DETECT-AD studies (95 participants) comparing chronic pain and MoCA cognitive scores between dementia caregivers and non-caregivers, with age adjustment.
- **In plain words**: This paper asks whether people who care for someone with Alzheimer's or a related dementia have more chronic pain and different thinking abilities than people who do not. The researchers reused data from two existing studies, tracking 95 participants for a year with weekly online pain questionnaires and yearly in-person memory and thinking tests. Caregivers were younger on average and scored slightly higher on a standard cognitive screening test, but they reported higher pain intensity even after accounting for age.
- **Why it matters**: Caregiver health is often overlooked, and this study suggests pain may be one part of that burden that deserves attention, including in telehealth caregiver support programs. The study is small, observational, and its pain result is borderline (confidence interval just reaching 1.00 and p = 0.048), so it should be read as a hint rather than settled evidence.
- **Background needed**: - Alzheimer's disease and related dementias cause progressive loss of memory and thinking; about 75% of affected people rely on informal (unpaid, family or friend) caregivers.
- Chronic pain means pain lasting months or longer; here it was rated as intensity (0-10) and as how much it interferes with daily life.
- MoCA (Montreal Cognitive Assessment) is a brief, widely used screening test of thinking abilities.
- A secondary analysis reuses data collected for other original purposes.
- An odds ratio (OR) above 1 means higher odds of the outcome in one group; a 95% confidence interval shows the range of plausible values.
- Age-adjusted analysis tries to separate group differences from differences in age.
- STELLA and DETECT-AD are research cohort studies; the text does not describe their design in detail. · level: intermediate

<details><summary>Original abstract</summary>

Background: Approximately 75% of individuals with Alzheimer's disease and related dementias rely on informal caregivers, yet caregiver health, including chronic pain, remains under-addressed. Chronic pain is highly prevalent, functionally limiting, and linked to cognitive vulnerability, but remains understudied in informal caregivers. This study examined differences in pain and cognitive performance between caregivers and non-caregivers. Objective: To compare chronic pain and cognitive performance between dementia caregivers and non-caregivers and determine whether differences persist independent of age. Methods: We conducted a secondary analysis of longitudinal data from STELLA and DETECT-AD. Ninety-five participants were followed for 12 months. Weekly online questionnaires assessed pain intensity (0-10 scale) and pain interference (Likert scale), while annual in-person evaluations measured cognition using the Montreal Cognitive Assessment. Group differences were evaluated using t-tests and multivariate regression adjusting for age. Results: Groups were similar in sex and education but differed in age, pain, and cognition. Caregivers were significatnly younger (71.3 vs 77.3 years; p < 0.0001) and caregivers demonstrated significatnly higher global cognitive performance as measured by the MoCA (mean score 26.8 vs 25.2; p = 0.02). After age adjustment, caregivers reported significantly higher pain intensity (OR 1.42, 95% CI 1.00-2.01; p = 0.048). Conclusions: Dementia caregivers exhibit greater pain burden despite younger age, highlighting chronic pain as a critical, underrecognized dimension of caregiver health and identifying an important opportunity to expand existing telehealth caregiver support models.

</details>

### [Integrating Plasma Brain-Derived pTau217, White Matter Hyperintensity and Hippocampal Volumes as Optimized Prognostic Markers for Cognitive Decline in an Asian Cohort with High Cerebrovascular Disease Burden](https://www.medrxiv.org/content/10.64898/2026.11.23.26368742v1)
*Chong, J. R.; Hilal, S.; Karikari, T. K. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.23.26368742 v1 · relevance 0.08

- **In one sentence**: In 523 Singapore participants without dementia or with mild dementia, a blood test for brain-derived pTau217 combined with MRI measures of white matter hyperintensities and hippocampal volume was associated with faster cognitive decline on the CDR-SB scale, with decline rising as more biomarkers were positive.
- **In plain words**: This study asks whether combining a blood test with two brain scan measures can better predict who will get worse in memory and thinking over time. Researchers followed 523 older adults in Singapore for about four years on average. They found that the more of three warning signs were present (a blood marker of Alzheimer's-related protein, small-vessel damage seen on MRI, and hippocampus shrinkage), the faster the decline in their clinical rating scores.
- **Why it matters**: Many older adults have both Alzheimer's and blood-vessel damage in the brain, so a single marker may not predict decline well. The text suggests a multi-marker profile could help with prognosis, though it is an observational association study and does not show that these markers can guide treatment.
- **Background needed**: - Alzheimer's disease: a progressive brain disease causing memory loss; it is often detected by amyloid and tau proteins.
- pTau217: a form of the tau protein measured in blood; "brain-derived" means it is estimated to come from brain cells.
- White matter hyperintensities (WMH): bright spots on MRI scans that reflect damage to small blood vessels in the brain.
- Hippocampal volume: the size of the hippocampus, a memory-related region; shrinkage suggests neurodegeneration.
- CDR-SB (Clinical Dementia Rating Sum of Boxes): a clinician-rated score of impairment in memory and daily function; a rising score means worsening.
- Slope: the average yearly change in a score over follow-up.
- Biomarker "positive/negative" status: each measure was split at a cutoff, then counted across participants.
- Cohort study: participants are observed over time, which shows association but not proof of cause. · level: research-level

<details><summary>Original abstract</summary>

Abstract Background: Combination of plasma and neuroimaging biomarkers associated with Alzheimer's disease (AD) and cerebrovascular pathophysiology might provide more accurate prediction of cognitive decline in populations with extensive AD and cerebral small vessel disease copathologies. Here, we aimed to identify an optimized biomarker panel for predicting cognitive decline by evaluating combinations of plasma and magnetic resonance imaging (MRI) biomarkers. Methods: We investigated participants without dementia or with mild dementia, recruited from memory clinics and the community in Singapore between August 2010 and August 2020. Plasma biomarkers of brain amyloid (brain-derived [BD]-pTau217, BD-pTau181, BD-pTau231, total-pTau217, total-pTau181, and total-pTau231), astrogliosis (GFAP), and neuroaxonal injury (NfL), with MRI measures of cerebrovascular disease (white matter hyperintensity [WMH] volume) and neurodegeneration (hippocampal volume), and primary outcome of longitudinal Clinical Dementia Rating Sum of Boxes (CDR-SB; mean [SD] follow-up duration, 51.0 [15.8] months). All plasma and MRI biomarker combinations for predicting CDR-SB slope (annual change in CDR-SB) were evaluated. Results: This study included 523 participants (mean [SD] age, 72.4 [7.9] years; 291 females [55.6%]). The parsimonious model included plasma BD-pTau217, WMH volume, and hippocampal volume (all P [&le;] 0.004). Dichotomizing these biomarkers yielded A, V, and N status, respectively, classifying participants as all negative (A-V-N-; n = 128), 1-positive (A+V-N-, A-V+N- or A-V-N+; n = 154), 2-positive (A+V+N-, A+V-N+, A-V+N+;n = 158) or 3-positive (A+V+N+; n = 83). Annual CDR-SB progression increased stepwise with the number of positive biomarkers. Compared with the all negative group ({beta}, 0.016), the 1-positive ({beta}, 0.409), 2-positive ({beta}, 1.16) and 3-positive groups ({beta}, 1.49) showed faster cognitive decline (all P < 0.001). Moreover, the 2-positive and 3-positive groups progressed faster than the 1-positive group (both P < 0.001), and the 3-positive group declined faster than 2-positive group (P = 0.009). Conclusions: Presence of multiple pathophysiological processes was associated with greater cognitive decline, highlighting the utility of a comprehensive multimodal biomarker profile to enhance prognostication.

</details>

## Oncology

Nothing notable this time.

## Health informatics and medical AI

### [Tabular Foundation AI Models in Healthcare: A WHO-Inspired Benchmark for Responsible AI and Trustworthiness](https://www.medrxiv.org/content/10.64898/2026.11.23.26368797v1)
*Hasan, K. S.; Borsha, M. A. A.; Ritu, R. J. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368797 v1 · relevance 0.06

- **In one sentence**: A benchmark comparing four tabular foundation models (TabFM, TabPFN, TabDPT, TabICL) against logistic regression and XGBoost on ten WHO-aligned healthcare classification datasets, scored on discrimination, sex-based fairness, calibration, and robustness to feature noise.
- **In plain words**: Hospitals and researchers often use pre-trained AI models to make predictions from spreadsheet-style patient records, but accuracy alone does not show whether those models are fair, honest about their uncertainty, or stable when data is slightly off. This paper builds a standardized test suite on ten health datasets and checks four newer models against two traditional methods on all of these points. The newer models generally did better at telling cases apart and at giving well-calibrated probabilities, while the simple logistic regression was the most stable under noisy inputs.
- **Why it matters**: Health systems are considering these general-purpose models for small-data prediction, so a shared, reproducible way to test them beyond raw accuracy is useful. The authors say the advantages depend on the dimension measured and on the dataset, and that external validation is still needed before clinical use; the overall composite score gaps between models were small and not statistically significant after correction.
- **Background needed**: - Tabular data: rows and columns of structured records, such as lab values and demographics.
- Foundation model: a large model pre-trained on broad data and applied to new tasks, here without much task-specific training.
- Baselines: logistic regression and XGBoost, long-established methods for this kind of data.
- AUROC: a 0 to 1 score for how well a model ranks positive cases above negative ones; higher is better.
- Calibration: whether predicted probabilities match real frequencies (e.g., a "30%" prediction happens about 30% of the time); expected calibration error measures the gap.
- Fairness across sex: checking whether performance differs between male and female patients.
- Friedman test with Holm correction: standard statistical tests for comparing several models across datasets while controlling false positives.
- Composite score (CMES): a single number combining many metrics, which can hide trade-offs. · level: intermediate

<details><summary>Original abstract</summary>

Tabular foundation models (TFMs) are increasingly used for structured prediction, yet their suitability for healthcare applications remains uncertain because predictive performance alone does not establish fairness, probabilistic reliability, or robustness. We developed a multidimensional benchmark to compare four TFMs: TabFM, TabPFN, TabDPT, and TabICL, against Logistic Regression and XGBoost across a curated, standardized suite of ten WHO-aligned healthcare classification datasets across diverse disease domains. Additionally, we harmonized clinical schemas, standardized protected sex attributes and outcome targets, and released both balanced-scale and natural-prevalence variants of the datasets to establish a benchmarking resource in healthcare machine learning. All models were evaluated using identical five-fold stratified cross-validation partitions and standardized preprocessing. Performance was assessed using 20 metrics spanning predictive discrimination, sex-based fairness, probability calibration, and robustness to Gaussian feature perturbations. A composite Clinical Model Evaluation Score (CMES) was used to summarize performance across these dimensions. Google TabFM achieved the highest mean CMES (0.8811), followed closely by TabDPT (0.8796), TabICL (0.8775), TabPFN (0.8756), XGBoost (0.8650), and Logistic Regression (0.8549). The Friedman test indicated significant differences among models ({chi}2F (5) = 24.914, p = 1.45 x 10^-4; Kendalls W = 0.498). However, post-hoc comparisons revealed no statistically significant differences among the four TFMs after Holm correction. TFMs generally demonstrated stronger discrimination and probabilistic calibration than conventional baselines, with TabFM achieving the highest mean Area Under the Receiver Operating Characteristic (0.9327) and the lowest expected calibration error (0.0674). Conversely, Logistic Regression exhibited the greatest stability under feature perturbations, while fairness performance varied substantially across datasets and models. These findings highlight the potential of TFMs for small-data healthcare prediction while demonstrating that their advantages are dimension-dependent. Multidimensional, dataset-specific evaluation and external validation remain essential before clinical implementation. All analysis codes, original datasets, and multiple variants of benchmark datasets are publicly available in a GitHub repository to ensure reproducibility and future research.

</details>

### [Concerns over spillover, exclusions, and hospital unit differences in an AI early warning system trial (CONCERN-EWS)](https://www.medrxiv.org/content/10.64898/2026.11.23.26368768v1)
*Mann, S.; Berdahl, C. T.; Griffin, B. A.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368768 v1 · relevance 0.05

- **In one sentence**: A letter raising methodological concerns (ICU bed spillover, exclusion of high-risk patients, and cluster-level imbalance) about the CONCERN-EWS cluster-randomized trial, which reported lower mortality with an AI early warning system (adjusted HR 0.64, 95% CI 0.53-0.78).
- **In plain words**: This is a critical letter about a hospital trial of an AI tool that flags patients who may be getting worse. The original trial reported that patients on units using the tool were less likely to die than patients on usual-care units. The letter argues that three issues could make that benefit look bigger than it really is.
- **Why it matters**: Whether AI tools actually improve patient survival, rather than just predicting risk, is an open question that trials like this try to answer. The letter's points about how a trial is designed and how its groups are compared show what can distort such results, though the letter does not itself show the benefit is wrong.
- **Background needed**: - Early warning system (EWS): software that scores patients' risk of deterioration so staff can intervene sooner.
- Cluster-randomized trial: whole hospital units, not individual patients, are randomly assigned to the tool or to usual care.
- Hazard ratio (HR): a comparison of how quickly events happen in two groups; 0.64 means about 36% lower risk over time in the intervention group.
- Confidence interval (CI): the range of values consistent with the data; 0.53-0.78 excludes 1.
- Spillover: effects from the intervention leaking into the control group, here through competition for scarce intensive care beds.
- Exclusion bias: if high-risk patients are moved out of the intervention group, its outcomes look better.
- Between-cluster variance: differences between hospital units that can skew results when only whole units are randomized.
- The source text is a short letter responding to the original paper; the authors' reply and the full trial data are not included here. · level: intermediate

<details><summary>Original abstract</summary>

Rossetti et al. report that hospitalized patients whose care was informed by an AI-based clinical deterioration early warning system (EWS) were 36% less likely to die during a pragmatic cluster-randomized trial when compared to patients on usual care units without the EWS (adjusted hazard ratio [HR], 0.64; 95% confidence interval [CI], 0.53-0.78).1 The authors should be applauded for conducting a trial evaluating the effect of an AI intervention on patient health outcomes; more such trials are needed. Several aspects of the study, however, raise concerns that its findings may not accurately reflect the effect of the EWS. First, spillover effects on availability of scarce intensive care unit (ICU) beds could have led to worse outcomes for patients in the control group. Second, EWS-informed clinical decisions may have led to more frequent exclusion of high-risk patients from the intervention group. Either of these concerns could have led to overestimation of AI benefit. Finally, large pre-trial differences in hospital unit mortality rates suggest that unreported cluster-level imbalance or between-cluster variance could also have affected trial results.

</details>

## Econometrics and applied economics

### [Will AI Replace Juniors? How Task Complexity Reduces Automation Risk](https://arxiv.org/abs/2611.34099)
*Vincent Rost, Fabian Stephany* · `econ.GN` · arXiv:2611.34099v1 · relevance 0.05

- **In one sentence**: A pre-registered survey experiment with managers at 1,435 German firms finds that tasks requiring judgement and independent problem-solving make managers less willing to substitute AI for entry-level hiring, and that managers expect AI to reduce entry-level hiring more than experienced hiring.
- **In plain words**: The paper asks whether companies would use AI tools instead of hiring junior staff. Managers were randomly given one of two hypothetical staffing needs: standardised, well-structured work, or more complex work requiring professional judgement and independent problem-solving. The complex-task framing made managers noticeably less inclined to choose AI over a new junior hire, and it raised the importance they placed on human oversight.
- **Why it matters**: It speaks to a live public worry that AI will squeeze entry-level jobs first, and it suggests that the kind of work matters more than the mere availability of AI. The text reports only survey responses from German firms in two sectors, so how far the findings carry to other countries or jobs is not established here.
- **Background needed**: - Survey experiment: participants are randomly assigned to different versions of a scenario, so differences in answers can be attributed to the change in the scenario.
- Pre-registered: the researchers publicly specified their hypotheses and analysis before collecting data, which limits selective reporting.
- Five-point scale: managers rated their willingness on a 1 to 5 scale; the reported effect is 0.54 points lower for complex tasks.
- Entry-level labour: newly hired or junior staff with little work experience.
- Human oversight: people checking or supervising the output of automated tools.
- Information economy and manufacturing: the two sectors sampled. · level: intermediate

<details><summary>Original abstract</summary>

How does task complexity shape firms' willingness to substitute entry-level labour with artificial intelligence (AI) tools? We study this question using a pre-registered survey experiment with managers from 1,435 German firms in the information economy and manufacturing industry. Managers are randomly assigned to consider a long lasting need for additional capacity involving either well-structured and standardised tasks, or more complex tasks that require professional judgement, contextual knowledge and independent problem-solving. Relative to standardised tasks, complex tasks reduce willingness to use AI rather than hire an entry-level employee by 0.54 points on a five-point scale and increase the importance attached to human oversight by 0.15 points. Further, pre-treatment responses indicate that managers expect the availability of AI applications to reduce hiring of both entry-level employees and experienced workers, but significantly more strongly for entry-level workers.

</details>

### [Geodesic Causal Forests: Learning Heterogeneous Treatment Effects for Random Objects](https://arxiv.org/abs/2611.33350)
*Yidong Zhou* · `stat.ME` · arXiv:2611.33350v1 · relevance 0.05

- **In one sentence**: The paper proposes geodesic causal forests, a tree-based method that estimates heterogeneous treatment effects when outcomes are random objects in curved metric spaces (e.g., compositions, covariance matrices, distributions, networks), using geodesic transport to Fréchet-mean references and a squared-distance loss correction that stands in for Euclidean residual corrections.
- **In plain words**: Many studies now measure outcomes that are not simple numbers but whole objects, such as a household's mix of activities, a table of correlations, or a probability distribution. These objects cannot be added or subtracted in the usual way, so standard methods for finding who benefits most from a program do not directly apply. The authors build a forest-based method that works in this setting and test it on simulated covariance-matrix data and on data from a Bangladeshi antipoverty program about women's livelihood mixes.
- **Why it matters**: Outcome data of this kind are becoming more common, and a method that can say who is affected most, in such settings, could be useful for program evaluation. The text reports consistency and convergence guarantees and simulation gains, but the empirical application's findings are described only briefly, so its practical weight is best judged from the full paper.
- **Background needed**: - Treatment effect: the difference a program makes for an individual compared with not receiving it.
- Heterogeneous treatment effects: how that difference varies across people (e.g., by age or prior work).
- Causal forest: an ensemble of decision trees that splits people into groups with different estimated effects.
- Random object: an outcome such as a matrix, distribution, or network, rather than a single number.
- Metric space and geodesic: a space with a distance measure; a geodesic is the shortest path between two points in it, which may be curved.
- Fréchet mean: the generalization of an average to curved spaces, found by minimizing squared distances.
- Doubly robust learning: estimation that stays accurate if either of two supporting models is roughly right.
- Nuisance error: error in auxiliary models (such as predicted outcomes or treatment probabilities) that the main estimate must tolerate. · level: research-level

<details><summary>Original abstract</summary>

Causal forests and orthogonal learners estimate heterogeneous treatment effects for scalar or Euclidean outcomes, yet outcomes are increasingly random objects, such as compositions, covariance matrices, distributions, or networks, in metric spaces without linear structure. We introduce geodesic causal forests for conditional geodesic treatment effects. Geodesic transport moves each geodesic between conditional Fr\'echet means of the potential outcomes to a common reference, making effects comparable across individuals. Because random objects cannot be added or subtracted, Euclidean residual corrections are unavailable; we instead correct the squared-distance loss through which the forest selects splits and estimates effects. The loss is real-valued for every candidate effect, so the correction requires only Fr\'echet means and leaves second-order nuisance error; for Euclidean outcomes, it recovers doubly robust learning. We establish consistency, convergence rates, and split-selection guarantees under conditions verified for curved and nonsmooth spaces. In simulations with covariance-matrix outcomes, the correction substantially reduces estimation error. For women's livelihood compositions in BRAC's randomized antipoverty program in Bangladesh, new livestock work mainly replaces casual wage work; after alignment, a single effect reproduces much of the variation in percentage-point changes across baseline activities, and the fitted effects are largest among former domestic workers and older women.

</details>

## Economic theory

### [Lone Wolves and Lattices in Bayesian Matching with Transfers](https://arxiv.org/abs/2611.34524)
*Xiyu Li* · `econ.TH` · arXiv:2611.34524v1 · relevance 0.05

- **In one sentence**: This paper studies Lone Wolf and lattice properties of stable outcomes in one-to-one transferable-utility matching with one-sided incomplete information, showing these properties can fail in general but hold under an additive-separability condition with a generic exception set.
- **In plain words**: The paper looks at how workers and firms get paired when a firm does not know everything about the workers it might hire, and money (wages) can be adjusted between them. The author shows by example that some tidy properties of stable pairings can break down in general. Under an extra assumption that a worker's value splits into a part about his type and a part about the firm, the author proves several regularities hold, such as a firm that goes unmatched in one stable outcome earns zero in all of them.
- **Why it matters**: Stable matching results like these underpin how markets with incomplete information are analyzed, so clarifying exactly when the "lone wolf" and lattice structures hold matters for theory. The text does not indicate applications beyond theory, so its practical reach is unclear from the abstract alone.
- **Background needed**: - Matching markets: pairing agents (here workers and firms) so that no pair would rather break off and form a new match.
- Transferable utility: payments such as wages can be shifted between the two sides.
- Incomplete information: a firm does not observe each worker's type (private characteristics) and forms beliefs about it.
- Stable outcome: an allocation with payments where no blocking pair exists.
- Lone Wolf property: a result about which agents end up unmatched across stable outcomes.
- Lattice: a set of outcomes closed under taking best-for-one-side combinations, which guarantees a worker-optimal and a firm-optimal stable outcome exist.
- Additively separable: the value splits into a sum of a type-part and a firm-part. · level: research-level

<details><summary>Original abstract</summary>

I study the Lone Wolf and lattice properties of stable outcomes in one-to-one matching with transferable utility and one-sided incomplete information, using the Bayesian stable market states of Liu (2020) and Chen and Hu (2024). With transfers, the wage in a blocking offer screens the worker's types, so it determines both whom the firm attracts and what the firm learns. I show by example that the firm-side and matched-set versions of the Lone Wolf property, as well as the lattice property, can fail even when outcomes are compared under the same information structure. I then assume that each worker's matching value is additively separable in his type and the firm's identity. Under this condition, a firm that is unmatched in some stable outcome earns zero in every stable outcome with the same type profile and information structure. Workers can retain information rents, so the worker-side property can fail. Nevertheless, outside a finite union of affine hyperplanes in the space of firm values, all such stable outcomes leave the same agents unmatched. Whenever they do, the stable payoff vectors form a lattice, and worker-optimal and firm-optimal outcomes exist. The results extend to comonotonicity of relative preferences when posterior beliefs are independent across workers.

</details>

## Game theory and algorithmic economics

### [Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games](https://arxiv.org/abs/2611.34536)
*Rishi Bharadwaj, Sujit Gujar, Yadati Narahari* · `cs.LG` · arXiv:2611.34536v1 · relevance 0.07

- **In one sentence**: Proposes Kant-Q, a Q-learning variant that learns a "Kantian equilibrium" (each agent plays the action it would want everyone to play) in symmetric Markov games, with convergence and Pareto-efficiency results for a subclass of symmetric monotone games and experiments on iterated Prisoner's Dilemma and the GovSim fishery.
- **In plain words**: The paper looks at how AI agents learn to cooperate when their goals are partly shared and partly in conflict, such as a group of agents sharing a fishery. Instead of aiming for the usual game-theory stable outcome (Nash equilibrium), which can leave everyone worse off than necessary, the authors have each agent learn the single action it would most want all agents to take. They report that this approach reliably learns that outcome in the games they tested, including a fishery with up to 200 agents, while the comparison methods did worse.
- **Why it matters**: Many multi-agent learning methods settle on outcomes that are stable but wasteful, so a method that targets better group outcomes is relevant to cooperative AI and to how AI systems that are copies of one another might coordinate. The text supports the theoretical and experimental claims only within the games studied, and whether the idea carries over to messier real-world settings is not shown here.
- **Background needed**: - Markov game: a repeated decision problem where several agents act at once and each one's reward depends on everyone's actions.
- Q-learning: a standard trial-and-error method where an agent learns the value of each action in each situation.
- Nash equilibrium: a state where no single agent gains by changing only its own action; it can still be inefficient for the group.
- Pareto-efficient: no outcome exists that makes someone better off without making someone else worse off.
- Symmetric game: all agents face the same rules and payoffs, so a shared strategy makes sense.
- Kantian equilibrium: each agent asks which action it would want all agents to adopt, a universalization idea borrowed from Kant's ethics.
- Iterated Prisoner's Dilemma: a repeated game where mutual cooperation beats mutual defection but defection is tempting.
- GovSim: a benchmark simulating a shared resource (here, a fishery) that agents can overharvest. · level: research-level

<details><summary>Original abstract</summary>

AI agents increasingly interact with one another, and many of these interactions are mixed-motive games, which have posed a persistent challenge for learning algorithms. Most multi-agent reinforcement learning (MARL) algorithms are designed to reach Nash equilibria, yet in many such games these equilibria are Pareto-inefficient. We instead study Kantian equilibria, an economic solution concept in which each agent plays the action it would want all agents to adopt. In symmetric games, this corresponds to an optimal common policy. We propose Kant-Q, a Q-learning algorithm in which each agent learns action profiles where all agents play the same action. Each update is then a sample from a single-agent MDP, so Kant-Q inherits the convergence guarantees of standard Q-learning. We show that every symmetric Markov game has a pure Kantian equilibrium. We also prove that all agents' Q-tables converge to the same limit, whose greedy policy is such an equilibrium, and that greedy play converges whenever the optimal common action is unique at every state. We further show that in a subclass of symmetric monotone games, the Kantian equilibrium is Pareto-efficient among pure strategy profiles and strictly individually rational. Empirically, on the iterated Prisoner's Dilemma and the GovSim fishery with up to 200 agents, Kant-Q learns the Kantian equilibrium, while the baselines underperform. Since copies of the same AI system naturally face one another in symmetric games, these results suggest universalization as a design principle for cooperative AI-AI interaction.

</details>

### [Last-Iterate Equilibrium Learning in Symmetric Congestion Games under Semi-Bandit Feedback](https://arxiv.org/abs/2611.34861)
*Katerina Michou, Marina Kontalexi, Dimitris Fotakis* · `cs.GT` · arXiv:2611.34861v1 · relevance 0.07

- **In one sentence**: The paper gives a last-iterate learning method for mixed Nash equilibria in atomic symmetric congestion games with resource semi-bandit feedback, using a quadratic consensus penalty to make the symmetric equilibrium the unique minimizer of a transformed potential.
- **In plain words**: The paper studies a group of players who repeatedly choose shared resources, such as roads, where costs rise as more people use them, and each player learns from the costs and loads it observes. The authors add a penalty term that keeps the players' strategies consistent with a symmetric equilibrium, so the learning process has a single well-defined target. They propose a variant of gradient descent, a step-by-step improvement rule, and report that the players' strategies approach equilibrium at stated rates in expectation and that the played strategies converge almost surely.
- **Why it matters**: Congestion games model traffic and shared-resource problems, so a provable guarantee about the final strategies, not just averages over time, is useful for understanding when decentralized learning settles down. The text does not show how these rates compare with prior work or how the method performs in practice, so its wider significance is unclear from this excerpt alone.
- **Background needed**: - Nash equilibrium: a state where no player can gain by unilaterally switching strategies.
- Mixed strategy: a player randomizes over choices, using probabilities.
- Congestion game: each resource's cost grows with the number of players using it.
- Potential function: a single score that tracks how players' incentives change; in these games minimizing it corresponds to equilibrium.
- Strong convexity: a shape of function with a single bowl-shaped minimum that curves upward steadily, making the minimum easy to find.
- Semi-bandit feedback: after acting, a player sees the cost and load of each resource it used, but not the full outcome of other choices.
- Last-iterate convergence: the current strategy profile itself approaches equilibrium, not just the time-average.
- Online projected gradient descent: repeatedly nudging a strategy along the improving direction and then projecting it back onto the set of valid strategies.
- Almost sure convergence: convergence with probability one. · level: research-level

<details><summary>Original abstract</summary>

We study last-iterate learning of mixed Nash equilibria in atomic symmetric congestion games under resource semi-bandit feedback, where players observe both the costs and the loads of their selected resources. For strictly increasing latency functions, the restriction of the potential function to symmetric marginal profiles is strongly convex. However, players' independent stochastic updates need not preserve this symmetry without explicit synchronization. We show that a quadratic consensus penalty makes the potential globally strongly convex while making the symmetric equilibrium the unique minimizer of the transformed potential. We propose a variant of online projected gradient descent that achieves $O(t^{-2/3})$ squared distance to equilibrium and $O(t^{-1/3})$ maximum deviation gain in expectation, for every $t\geq 1$ and for any initialization. The played profile also converges to equilibrium almost surely.

</details>

## Mathematical finance

### [Distance from the Truth: Why Fragmented Merchant Underwriting Misses Risk, and What Source-Attributable Evidence Changes](https://arxiv.org/abs/2611.34696)
*Russell Lessard, Jeremy Blackburn, Tim Hines et al.* · `cs.CR` · arXiv:2611.34696v1 · relevance 0.03

- **In one sentence**: A position paper arguing that fragmented merchant underwriting misses linked risks across identity, authority, and settlement, and proposing a source-attributable evidence architecture, receipt format, 90-day shadow pilot design, and self-assessment, with all controls and pilot measures explicitly unobserved.
- **In plain words**: This paper is about how payment companies decide whether to let a business accept card payments. It argues that checking each piece of evidence separately (a registration, an ID, a bank account) can miss whether those pieces actually belong to the same business and the same authorized person. The authors propose keeping a single, traceable record of what was checked, who it relates to, when, and under which rule, and they describe a planned test rather than reporting results.
- **Why it matters**: Merchant onboarding failures can lead to fraud losses and compliance problems for payment processors and banks, so a clearer way to link evidence could matter to that industry. The text itself presents the proposals as untested, so its practical value is not yet shown; it is a framework and a proposed pilot, not a measured improvement.
- **Background needed**: - Merchant underwriting: the process a payment processor uses to approve a business before it can take card payments.
- Know-your-customer / customer due diligence: rules requiring institutions to verify who their customers are and who controls them.
- Sanctions screening: checking customers against lists of restricted individuals or entities.
- Card-network and Nacha rules: requirements from Visa/Mastercard-type networks and the Nacha body that governs bank payment transfers (ACH).
- Settlement destination: the bank account where a merchant's money is sent.
- Point-in-time check: a verification that was true on one date but may not still be true later.
- Shadow pilot: a trial run that operates alongside existing processes without actually making the decisions.
- The "ChainIT Transaction Truth Architecture" is a named framework referenced by the paper; the text does not explain it in detail. · level: intermediate

<details><summary>Original abstract</summary>

Merchant underwriting becomes vulnerable when evidence is evaluated without enough visibility into its source, freshness, relationship to the applicant, or meaning for the proposed activity. Individually favorable checks do not necessarily establish that the same business is operating the merchant account, that its representative may bind it, or that its settlement instructions are authorized. We describe three failure modes of fragmented underwriting: distance from the source, the gap between a decision and the evidence needed to justify it; the correlation gap, in which material relationships among the person, legal entity, owners or controllers, representative, business activity, and settlement destination are not evaluated when each signal is considered alone; and point-in-time controls, in which a historical verification is treated as present eligibility. We map these failure modes to identity-proofing, customer-due-diligence, sanctions, third-party-risk, card-network, and Nacha requirements, and propose a merchant-underwriting application of the ChainIT Transaction Truth Architecture built on provenance, correlation, and persistence. The application keeps a logically unified evidence record that identifies what was checked, the subject and relationship involved, the relevant times, the applicable policy, the decision, and any exceptions, and it keeps evidence validation, applicant verification, organizational authority, and the institution's risk judgment separate. We also set out a proposed evidence and decision receipt, a defined 90-day shadow enrollment pilot with adjudicated outcome measures and deliberate control-failure tests, and a ten-question self-assessment. Proposed controls, illustrative scenarios, and pilot measures are identified as such and are not represented as observed production results.

</details>

## Financial markets

Nothing notable this time.

## Signal processing

### [AutoRSP: An AI Agent for Radar Sensing Pipeline Design](https://arxiv.org/abs/2611.34754)
*Zhi Zheng, Xincheng Xie, Avery Gump et al.* · `cs.NI` · arXiv:2611.34754v1 · relevance 0.11

- **In one sentence**: AutoRSP is an AI agent that designs end-to-end radar sensing pipelines across five stack layers, using RF simulation, on-sensor emulation, and real edge-device runs as search feedback instead of an LLM judge.
- **In plain words**: Radar systems need a full chain of processing, from the hardware settings up to the software that turns reflected signals into useful results, and building that chain takes expert time and money. This paper asks whether an AI agent can design such chains automatically. The authors report that their agent, AutoRSP, produced runnable pipelines for robotic imaging, car perception, and vital-sign sensing that performed comparably to or better than human-expert and closed-source agent pipelines.
- **Why it matters**: It offers a concrete way to let an AI agent search over hardware-linked engineering choices using physical measurements rather than another language model's opinion, which may matter for sensing work beyond large labs. The text does not give enough detail to judge how broad or robust the gains are, and the promised release of tools and benchmarks is not yet available for checking.
- **Background needed**: - Radar: sends radio waves and reads the echoes to detect objects or motion.
- RF simulation: a computer model of how radio signals behave, used to test designs before building hardware.
- Edge device: a small, local computing unit (such as one inside a sensor or car) that runs the processing on site.
- Sensing pipeline: the ordered chain of steps from raw signal capture to final output.
- Stack layers: separate levels of the system (for example hardware settings, signal processing, and application software) that affect each other.
- AI agent: a language-model-driven program that proposes designs, tests them, and iterates.
- LLM judge: using a language model to score candidate designs, which the paper avoids in favor of measured feedback. · level: research-level

<details><summary>Original abstract</summary>

Radar sensing demands a pipeline that is well-thought-out across hardware and software. We ask whether an AI agent can automatically design radar sensing pipelines at a fraction of the time, cost, and expertise that current practice needs. We present AutoRSP, an agent that embeds radar-system-level structure through sub-agents mapped to five stack layers, a code-based representation of every layer with explicitly modeled cross-layer dependencies. Feedback for the agentic search process comes from a pipeline of realistic RF simulation, on-sensor emulation, and execution on real edge devices, rather than from an LLM judge. Because such feedback can be slower than an LLM call, we present methods to efficiently optimize agentic loops. We evaluate AutoRSP on robotic imaging, automotive perception, and vital sign sensing. It produces executable pipelines with performance comparable to or better than human-expert pipelines and closed-source agents. AutoRSP's harness, tools, and benchmarks will be released to bridge the rising gap in agentic research abilities outside of frontier labs.

</details>

### [Doppler RaDAR Single-Frame Anomaly Detection and Consistency Assessment by Velocity-Conditioned Gaussian Spectral Modeling](https://arxiv.org/abs/2611.34639)
*Malte Stelzer, Timo Bartels, Dinu Mihailescu-Stoica et al.* · `eess.SP` · arXiv:2611.34639v1 · relevance 0.08

- **In one sentence**: A velocity-conditioned Gaussian spectral model, with a neural encoder and Gaussian decoder, that scores single radar Doppler frames for anomalies and checks consistency between the spectrum and the estimated speed of a railway vehicle.
- **In plain words**: Trains on railway radar signals must know their own speed, and a speed number alone does not show whether the radar reading behind it is trustworthy. This paper proposes a method that looks at each radar frame's frequency pattern, estimates speed from it, and then checks whether the pattern matches what is expected at that speed. On controlled test anomalies, the authors report that two of their three scores beat conventional spectral indicators in most conditions, and a third tracks speed errors closely.
- **Why it matters**: Railway speed sensing is safety-relevant, so a way to flag implausible radar frames without needing ground-truth speed during operation could be useful. The text reports results only on controlled synthetic anomalies, so how well it transfers to real field conditions is not shown here.
- **Background needed**: - RaDAR (radio detection and ranging): sends radio waves and measures echoes to sense distance and motion.
- Doppler spectrum: the distribution of signal strength across frequency shifts; the shift reveals how fast something moves toward or away from the sensor.
- Speed-over-ground: how fast a vehicle moves along the track, as estimated by the sensor.
- Gaussian model: a bell-shaped probability distribution used here to describe the expected shape of the spectrum.
- Anomaly score: a number that is higher when an input looks unlike what the model learned as normal.
- Pearson r: a correlation measure from -1 to 1; values above 0.99 indicate a near-linear relationship.
- Ground truth: a reference value known to be correct, used for checking estimates. · level: research-level

<details><summary>Original abstract</summary>

Reliable speed-over-ground estimation is essential for automated railway vehicles. However, the accuracy of a velocity estimate alone does not indicate whether the underlying RaDAR measurement is physically plausible. This paper introduces a velocity-conditioned Gaussian spectral modeling framework for anomaly detection and velocity consistency assessment. A neural encoder estimates the vehicle velocity from complex Doppler spectra, while a Gaussian decoder models the expected spectral distribution conditioned on a velocity estimate. Three complementary inference-time online indicators are derived: the spectral anomaly score (SAS), conditional anomaly score (CAS), and absolute velocity disagreement (AVD). Experiments demonstrate the sensitivity of the scores to velocity deviations. Under controlled spectral anomalies, SAS and CAS outperform conventional spectral indicators in most conditions. Furthermore, AVD exhibits strong correlations with actual velocity estimation errors (Pearson $r>0.99$) for the investigated extra-peak and local anomalies. These results demonstrate the potential of online conditional spectral modeling to assess measurement plausibility and velocity estimation reliability without requiring ground-truth velocities during inference.

</details>

## Audio and speech

### [Music Similarity Estimation from Jukebox Embeddings](https://arxiv.org/abs/2611.34346)
*Johannes Grafinger, Gerhard Widmer, Jan Schl\"uter* · `cs.SD` · arXiv:2611.34346v1 · relevance 0.07

- **In one sentence**: The paper proposes JukeSim, which estimates content-based music similarity from embeddings produced by the Jukebox generative music model, and reports it performs on par with an existing learning-based method and better than the best hand-designed methods on several datasets.
- **In plain words**: The paper asks how to tell whether two songs sound alike using only the audio itself, without any listener data or tags. The authors take internal representations ("embeddings", numerical fingerprints of sound) from Jukebox, a model originally built to generate music, and use them to measure similarity. They report that this approach matches a recent learned method and beats older hand-designed ones across several test datasets.
- **Why it matters**: Audio-only similarity matters for recommending new songs that have no listening history yet, the "cold-start" problem. The work is worth watching because it shows a generative model's internal features can be reused for a different task, but the text notes the approach needs more computing power than other measures.
- **Background needed**: - Music similarity estimation: scoring how alike two audio recordings sound, based only on the audio.
- Cold-start recommendation: suggesting items when there is no usage data about them yet.
- Embedding: a list of numbers that summarizes a piece of audio, where similar sounds get similar numbers.
- Jukebox: a large generative model from OpenAI that produces music audio; here it is used as a feature extractor rather than to generate music.
- Learning-based vs. hand-designed: the first learns its measure from training data; the second uses rules and signal features set by people.
- Compute cost: the processing power and time needed to run the method. · level: intermediate

<details><summary>Original abstract</summary>

Content-based music similarity estimation aims to provide a measure of similarity between music audio recordings, disregarding any associated metadata. This has potential applications in e.g. cold-start music recommendation scenarios, where there is no user interaction data. In this work, we propose JukeSim, a new approach to estimating musical similarity based on embeddings created by Jukebox, a generative music model. In evaluations on multiple datasets, we find that JukeSim performs on par with an existing learning-based approach, and both outperform the best hand-designed approaches, which had never been compared to recent work before. Even though the required compute for JukeSim is higher than for other measures, we demonstrate the viability of utilizing generative embeddings for this task, encouraging further research.

</details>

### [Line-Level Singer Diarization in Multi-Member Pop Songs: A Benchmark, Lead-Vocal Isolation, and Song-Level Decoding](https://arxiv.org/abs/2611.33247)
*Allen Ng* · `cs.SD` · arXiv:2611.33247v1 · relevance 0.05

- **In one sentence**: The paper introduces a line-level singer diarization benchmark (ColorCoded-SD) for multi-member K-pop songs, and shows that lead-vocal isolation, singing-adapted speaker embeddings, and two training-free song-level decoders improve B-cubed F1 over a standard pipeline on two datasets.
- **In plain words**: The question is which member of a pop group sings each line of a song, when the group has four to eight singers and nobody tells the system who they are. Standard speech tools that separate speakers fail on this, finding only one or two voices. The authors release a benchmark of 43 K-pop songs with line-by-line singer labels, and report that isolating the lead voice and using a few song-level tricks raises grouping accuracy, with errors concentrated on very short lines.
- **Why it matters**: It applies speaker-diarization methods to singing, where many voices overlap with music, and it is careful about what did not help (more training data, weight editing, a song-context model, target-singer extraction). The text does not indicate applications beyond music information retrieval and fan-annotation tools, so wider relevance is unclear.
- **Background needed**: - Speaker diarization: grouping the parts of an audio recording by who is speaking, without knowing the speakers in advance.
- Speaker embedding: a numeric "voiceprint" vector summarizing a voice, used to compare and cluster speakers.
- Vocal separation: software that splits a mixed song into vocal and instrumental tracks; a karaoke separator removes backing vocals as well.
- Lead-vocal isolation: keeping only the main singer's voice, which the paper finds matters most.
- Viterbi decoding: a method that finds the most likely sequence of labels, here used with a preference for keeping the same singer across consecutive lines.
- B-cubed F1: a clustering score that rewards grouping items correctly for each item, used here to measure how well lines are grouped by singer.
- Training-free: the method adds no new model training; it works on top of existing components. · level: research-level

<details><summary>Original abstract</summary>

Fans of multi-member pop groups annotate songs line by line with the member who sings each line, but speech diarization does not transfer to this setting: a commercial diarizer finds one or two speakers in songs by groups of four to eight. We study line-level singer diarization: given a song and its lyric-line timings, group the lines by singer with no prior knowledge of the group. We release ColorCoded-SD, a benchmark of 43 K-pop songs (1,740 lines, 3-8 singers per song) built from crowd annotations verified by independent annotators, together with alignment and scoring tools, and we derive line labels for the IdolSongsJp corpus from its per-singer solo renditions for evaluation on unseen singers. Combining lead-vocal isolation with a karaoke separator, singing-adapted speaker embeddings, and two training-free song-level decoders (a sticky Viterbi pass over line order and unsupervised linking of a group's songs) improves B-cubed F1 over the standard pipeline (vocal separation, speaker embeddings, per-song clustering) by +0.058 on ColorCoded-SD (p=0.001) and by +0.066 on IdolSongsJp (p=0.003). Isolating the lead is the largest single factor wherever the separator leaves a lead voice (+0.04 to +0.06 on the same lines), and with the singers' dry studio takes two different encoders become indistinguishable; the remaining errors concentrate on short lines that carry too little audio for a voiceprint. We also report negative results (more or cleaner training data, weight editing, a song-context model, and target-singer extraction) that bound where further gains can come from.

</details>

## Control systems

### [Adaptive Control Barrier Functions for Nonlinear Singularly Perturbed Systems](https://arxiv.org/abs/2611.34866)
*Prashanth Krishnamurthy, Farshad Khorrami* · `eess.SY` · arXiv:2611.34866v1 · relevance 0.16

- **In one sentence**: The paper extends adaptive control barrier functions to uncertain nonlinear singularly perturbed (two-time-scale) systems, giving robustness conditions under which both slow and fast subsystems stay within their safe sets despite parameter uncertainty.
- **In plain words**: Many machines have parts that move at very different speeds, and a controller must keep the whole system inside safe limits even when some of its physical parameters are not known exactly. This paper develops a method that does this for such two-speed systems by estimating the unknown parameters online. The authors report that if the slow part is kept safe with a suitable margin, the slow part stays close to its safe region when the speed-ratio parameter is small, and they give conditions for joint safety of the slow and fast parts.
- **Why it matters**: Safety guarantees for systems with mixed time scales and unknown parameters are a practical concern in robotics and vehicles, so the framework may be relevant there. The text only reports simulations on two example systems (a synthetic fourth-order system and a unicycle with obstacle avoidance), so how well it applies to real hardware is not shown here.
- **Background needed**: - Control barrier function (CBF): a function whose sign defines a safe region; a controller is designed so the system never leaves it.
- Adaptive control: the controller continuously updates estimates of unknown physical parameters while it runs.
- Singular perturbation / two-time-scale system: a system with fast and slow dynamics, where a small parameter epsilon is the ratio of the two time scales; the slow part approximates the whole system when epsilon is small.
- Reduced-order (slow) model: the simpler model obtained by ignoring the fast dynamics.
- O(epsilon) neighborhood: a region whose size shrinks in proportion to epsilon.
- Robustness margin: an extra safety buffer added to the constraint to absorb modeling errors. · level: research-level

<details><summary>Original abstract</summary>

Control barrier functions (CBFs) have emerged as a flexible and efficient approach for enforcing dynamic safety constraints. In this paper, we consider a class of uncertain nonlinear systems with singular perturbations and develop an adaptive CBF framework for such systems to enforce safety constraints on both the slow and fast subsystems in the overall singularly perturbed nonlinear system with uncertain parameters. We first develop a robustness property showing that if an adaptive controller for the slow subsystem satisfies the slow CBF condition with an appropriate safety margin, then for sufficiently small values of the singular perturbation parameter $\varepsilon$, the slow subsystem remains within an $O(\varepsilon)$-neighborhood of its safe set. We then consider the more general case of safety constraints on both the fast and slow subsystems and provide conditions under which joint slow-fast safety is achieved despite the parametric uncertainties. The reduced-order slow model and the slow and fast CBF conditions are evaluated using an online parameter estimate and the parameter mismatch between the estimated and true reduced-order models is addressed via a state-dependent robustness margin in the CBF inequalities. To illustrate the proposed framework, we present simulation studies for two systems with parametric uncertainties: a synthetic two-time-scale fourth-order example system and a unicycle with a fast turn-rate actuator and an obstacle avoidance safety constraint.

</details>

### [$\mu$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation](https://arxiv.org/abs/2611.34597)
*Devesh Nath, Glen Chou* · `cs.RO` · arXiv:2611.34597v1 · relevance 0.12

- **In one sentence**: μMPC is a model predictive control framework that uses learned Koopman-linearized dynamics and precomputed control-to-output maps to reduce the online quadratic program to an action-only problem with Hn_u variables, solved by primal-dual iterations using only matrix-vector products and projections.
- **In plain words**: Robots and drones often need to work out their next moves many times per second while obeying limits, such as staying inside safe bounds. This paper presents a method that does most of that work ahead of time, so the real-time calculation is small enough to run in tens of microseconds on a desktop and in about 24 ms on a tiny drone microcontroller. The authors report that the same approach scales to large learned models, such as 4096-dimensional quadruped control and 200-quadrotor collision-aware planning on a GPU.
- **Why it matters**: Fast, constraint-respecting control on cheap hardware matters for robots, drones and any system that must plan in real time. The reported speedups (up to 108x for constrained MPC and 1907x for visuomotor planning) are compared against unspecified competing methods, so they should be read as the authors' own benchmark claims until independent tests are available.
- **Background needed**: - Model predictive control (MPC): at each moment, the controller predicts future behavior over a short horizon, solves an optimization problem for the best actions, applies the first one, and repeats.
- Quadratic program (QP): an optimization problem with a quadratic cost and linear constraints; solving it quickly is the main cost of MPC.
- Koopman operator: a way to turn a nonlinear system into an approximately linear one by lifting its state into a higher-dimensional space where linear tools apply.
- Primal-dual iterations: iterative solver steps that alternate between updating the decision variables and the constraint multipliers.
- Precomputation / "compiling": doing expensive matrix work offline so the online step needs only cheap multiplications.
- World model: a learned model of how an environment evolves, often used for planning from images.
- DAgger: an imitation-learning method that collects new training data from the controller's own rollouts. · level: research-level

<details><summary>Original abstract</summary>

We present $\mu$MPC, a fast model predictive control (MPC) framework that reduces online computation using learned Koopman-linearized dynamics. By precomputing finite-horizon control-to-output maps, $\mu$MPC eliminates lifted-state trajectories, yielding an action-only Koopman-Compiled QP (KC-QP) with $Hn_u$ decision variables, independent of lifted dimension. A fixed, precomputed primal operator enables efficient primal-dual iterations using only matrix-vector products and projections, accommodating changing goals and constraints without refactorization. This efficiency also enables control-aware dynamics learning through differentiable KC-QPs in the training loop and batched DAgger-style data aggregation. $\mu$MPC achieves solve times as low as $23\mu$s on a desktop CPU and 24 ms onboard a 168 MHz Crazyflie microcontroller. It scales to 4096D quadruped control in under 5 ms, visual planning with 2048D world models in 0.4 ms, and collision-aware planning for 200 quadrotors at over 30 Hz on the GPU. Across these benchmarks, $\mu$MPC achieves up to $108\times$ faster constrained MPC and $1907\times$ faster visuomotor planning than competing methods.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 40 | 34 | 2 |
| Differential geometry | 30 | 27 | 2 |
| Partial differential equations | 58 | 54 | 2 |
| Harmonic analysis | 31 | 28 | 2 |
| Complex analysis | 14 | 12 | 2 |
| Operator algebras and spectral theory | 14 | 12 | 2 |
| Algebra | 31 | 26 | 2 |
| Representation theory | 19 | 16 | 2 |
| Number theory | 31 | 28 | 2 |
| Algebraic geometry | 31 | 28 | 2 |
| Topology | 18 | 16 | 2 |
| Dynamical systems | 36 | 34 | 2 |
| Combinatorics | 53 | 49 | 2 |
| Numerical analysis | 31 | 29 | 2 |
| Logic and foundations | 6 | 4 | 2 |
| Mathematical physics | 49 | 46 | 2 |
| Optimization and control | 38 | 35 | 2 |
| Statistics theory | 19 | 17 | 2 |
| Statistical methods and applications | 54 | 49 | 2 |
| AI industry news | 40 | 24 | 5 |
| Model architectures and training | 60 | 57 | 2 |
| Machine learning theory | 13 | 9 | 2 |
| Large language models | 74 | 72 | 2 |
| Computer vision | 242 | 240 | 2 |
| Reinforcement learning | 52 | 49 | 2 |
| AI safety and alignment | 36 | 33 | 2 |
| Interpretability | 7 | 5 | 2 |
| AI for mathematics | 7 | 5 | 2 |
| Robotics and embodied AI | 111 | 106 | 2 |
| Security and cryptography | 38 | 35 | 2 |
| Algorithms and complexity | 41 | 38 | 2 |
| Programming languages and formal methods | 17 | 15 | 2 |
| Systems and networking | 31 | 29 | 2 |
| Human-computer interaction | 23 | 21 | 2 |
| Information theory | 20 | 17 | 2 |
| High-energy theory and gravity | 82 | 77 | 2 |
| Statistical physics | 43 | 40 | 2 |
| Condensed matter | 50 | 47 | 2 |
| Particle physics | 57 | 53 | 2 |
| Nuclear physics | 10 | 8 | 2 |
| Quantum information and computing | 106 | 101 | 2 |
| Optics and atomic physics | 32 | 30 | 2 |
| Fluids and plasma | 21 | 18 | 2 |
| Biological physics | 7 | 4 | 0 |
| Climate, atmosphere and Earth | 9 | 7 | 2 |
| Cosmology | 21 | 18 | 2 |
| Galaxies | 33 | 31 | 2 |
| Exoplanets and planetary science | 18 | 15 | 2 |
| High-energy astrophysics | 27 | 24 | 2 |
| Stars and the Sun | 22 | 19 | 2 |
| Chemical physics | 16 | 10 | 2 |
| Materials science | 47 | 44 | 2 |
| Soft matter and polymers | 12 | 10 | 2 |
| AI for chemistry and materials | 24 | 19 | 2 |
| Biochemistry | 30 | 23 | 2 |
| Pharmacology and drug discovery | 11 | 8 | 0 |
| Computational and systems biology | 144 | 138 | 2 |
| Neuroscience | 101 | 94 | 2 |
| Genetics and genomics | 50 | 44 | 2 |
| Cell and molecular biology | 78 | 72 | 2 |
| Immunology and microbiology | 86 | 78 | 2 |
| Cancer biology | 39 | 34 | 2 |
| Ecology and evolution | 78 | 71 | 2 |
| Plant biology | 35 | 27 | 2 |
| Bioengineering and synthetic biology | 42 | 35 | 2 |
| Mathematical biology (arXiv) | 14 | 11 | 2 |
| Epidemiology | 22 | 17 | 2 |
| Infectious diseases | 8 | 3 | 1 |
| Public and global health | 24 | 16 | 2 |
| Psychiatry and neurology | 33 | 26 | 2 |
| Oncology | 9 | 2 | 0 |
| Health informatics and medical AI | 17 | 9 | 2 |
| Econometrics and applied economics | 13 | 11 | 2 |
| Economic theory | 5 | 2 | 1 |
| Game theory and algorithmic economics | 11 | 8 | 2 |
| Mathematical finance | 6 | 4 | 1 |
| Financial markets | 8 | 5 | 0 |
| Signal processing | 21 | 19 | 2 |
| Audio and speech | 9 | 7 | 2 |
| Control systems | 38 | 33 | 2 |

<!-- {% endraw %} -->
