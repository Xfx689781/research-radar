# Research digest · 2026-11-27
<!-- {% raw %} -->

New papers posted from about 2026-11-26 to 2026-11-27 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[Viscosity solutions for integro-differential equations with gradient and source terms](https://arxiv.org/abs/2611.34533)** (Partial differential equations): The paper studies a family of equations that mix a function's rate of change, its slope, and a non-local averaging effect, the kind that arise when a process depends on values far away as well as nearby. It shows that, under its assumptions, these equations have a well-defined solution that is unique and depends stably on the setup. The authors present a single framework that combines two existing styles of argument, one based on min-max structure and one from free boundary problems.
- **[List coloring degenerate graphs with requests](https://arxiv.org/abs/2611.34348)** (Combinatorics): The paper studies a graph-colouring puzzle: each node has a short list of allowed colours, and some nodes come with a requested colour. The question is how many requests can be honoured at once while still giving every node a colour from its list. The authors prove three results that push the trade-off between list size and the fraction of requests that can be met to its limits.
- **[Adaptive Control Barrier Functions for Nonlinear Singularly Perturbed Systems](https://arxiv.org/abs/2611.34866)** (Control systems): Engineers often build control systems where some parts react quickly and others react slowly, and they need to keep the system inside safe limits even when some of its physical parameters are unknown. This paper studies how to enforce such safety limits on both the slow and fast parts of these systems while the controller learns the unknown parameters online. The authors show that if the slow part is kept safe with a suitable margin, the true system stays close to the safe region when the speed-difference parameter is small, and they give conditions for joint safety of both parts.

## Probability

### [Differentiability of the shape function in the planar corner growth model](https://arxiv.org/abs/2611.33433)
*Christopher Janjigian, Firas Rassoul-Agha, Timo Sepp\"al\"ainen* · `math.PR` · arXiv:2611.33433v1 · relevance 0.18

- **In one sentence**: The paper proves that the time-constant (shape) function of planar directed last-passage percolation with general i.i.d. real weights is differentiable on the open first quadrant, under moment conditions, using a multiscale path-counting argument with a Lean-formalized proof.
- **In plain words**: The paper studies a random growth model on a grid, where each site gets a random weight and we look for the most valuable path from one corner to a far-away point. The question is how the typical maximal value grows in each direction, and whether that growth rate changes smoothly with direction. The authors show it does change smoothly (is differentiable) in all directions of the open first quadrant, provided the weights have enough finite moments, and they check the argument in the Lean proof assistant.
- **Why it matters**: Differentiability of the shape function is a long-standing question in first- and last-passage percolation, and the text notes that the proof is an AI-assisted adaptation of an earlier OpenAI proof for the first-passage case. The moment conditions are described as nearly optimal, but the text does not say how this result compares beyond that, so its wider significance is unclear from the abstract alone.
- **Background needed**: - Last-passage percolation: on a lattice, each site has a random weight; a directed path collects weights, and the last-passage time is the maximum total over paths from the origin to a far point.
- Shape function: the limiting growth rate of that maximum in each direction, after scaling; it describes the average large-scale behaviour.
- Differentiability: the shape function has a well-defined slope at each direction, meaning it varies smoothly rather than with corners.
- Open first quadrant: directions where both coordinates are positive, excluding the boundary axes.
- Percolation cone: a set of directions where known results already handle the behaviour, so only the other directions need proof.
- Moment assumption: a condition that the weights have finite higher moments (averages of powers), controlling how extreme the weights can be.
- Oriented percolation and van den Berg–Kesten inequality: standard probabilistic tools for counting disjoint paths and bounding probabilities of events.
- Lean: a computer proof assistant used to check the proof formally. · level: research-level

<details><summary>Original abstract</summary>

We prove that the shape function of planar directed last-passage percolation with general i.i.d.\ real-valued weights is differentiable on the open first quadrant, under a moment assumption of order $p''>4$ on the positive part of the weight and a nearly optimal order $p'>1$ on the negative part. Due to known results, only directions outside a percolation cone need be considered. The proof is a multiscale path-counting argument that uses the shape theorem, oriented percolation on a coarse-grained lattice, a simple change of measure in a finite region, and the van den Berg--Kesten inequality. Our Lean-formalized proof is an AI-assisted adaptation and improvement of the OpenAI proof of differentiability in planar first-passage percolation.

</details>

### [Besicovitch Pseudo Almost Periodic Stochastic Processes and Their Applications to Delayed Stochastic Neural Networks](https://arxiv.org/abs/2611.33209)
*Yongkun Li, Yuwei Cao, Bing Li* · `math.DS` · arXiv:2611.33209v1 · relevance 0.14

- **In one sentence**: The paper introduces the concept of Besicovitch pseudo almost periodic stochastic processes and applies it to show existence and p-th mean stability of such solutions in distribution for delayed stochastic neural networks whose parameters other than the delays are pseudo almost periodic.
- **In plain words**: The paper is about random systems that move in patterns which repeat roughly but not exactly, such as a signal that wobbles with a rhythm that is nearly periodic. The authors define a new, formal way to describe such random patterns, in a sense that covers a broader class of behaviours than earlier definitions. They use this to study a model of neural networks with time delays and random noise, and report criteria under which a repeating-type solution exists and is stable.
- **Why it matters**: Models of neural networks and other noisy dynamical systems often have rhythms that are not strictly periodic, so a precise mathematical vocabulary for them is useful. The text presents this as a new conceptual tool, but its practical reach beyond the specific neural network model is not shown in the text.
- **Background needed**: - Periodic function: repeats exactly at a fixed interval. Almost periodic: repeats approximately, with near-returns to earlier patterns.
- Pseudo almost periodic: almost periodic plus a small part that decays or is averaged out over time.
- Besicovitch sense: a way of measuring closeness of functions by averaging their differences over long stretches, which is looser than pointwise closeness.
- Stochastic process: a quantity evolving randomly over time.
- Solution in distribution: the statistical description (probability law) of the solution repeats, not the exact random path.
- Time delay: the system's current change depends on its state some time in the past.
- p-th mean stability: solutions stay close, measured by the average of the p-th power of their distance, as time goes on. · level: research-level

<details><summary>Original abstract</summary>

The Besicovitch almost periodic concept is a generalization of the Bohr, Stepanov, and Weyl almost periodic concepts and, in a certain sense, has broader coverage and weaker conditions. However, the concept of pseudo almost periodic stochastic processes in the Besicovitch sense has not yet been systematically proposed, which limits the characterization of the complex oscillatory behavior of a broader class of stochastic non-autonomous systems. This paper proposes the concept of Besicovitch pseudo almost periodic stochastic processes. As an application of this concept, we study the existence of Besicovitch pseudo almost periodic solutions in distribution for a class of stochastic delayed neural networks in which all parameters except the time delays are pseudo almost periodic and establish stability criteria for such solutions in the $p$-th mean sense. The work of this paper fills the gap caused by the lack of the concept of Besicovitch pseudo almost periodic stochastic processes and provides a new conceptual tool and analytical approach for characterizing the complex oscillatory behavior of stochastic differential equations and stochastic neural network systems.

</details>

## Differential geometry

### [Three-dimensional harmonic critical metrics for the Einstein-Hilbert functional and self-similar Ricci flows](https://arxiv.org/abs/2611.34037)
*Sergey E. Stepanov, Irina I. Tsyganok* · `math.DG` · arXiv:2611.34037v1 · relevance 0.23

- **In one sentence**: In three dimensions, the paper shows that closed harmonic critical metrics for the Einstein-Hilbert functional under Chen-Nagano variations are exactly the constant-sectional-curvature (space-form) metrics, linking this rigidity to self-similar Ricci flows and the smooth Poincaré theorem.
- **In plain words**: The paper studies a question about which shapes of curved three-dimensional space are "balanced" under a specific kind of smooth deformation that keeps volume fixed. The authors show that, for closed three-dimensional spaces, the only such balanced shapes are the ones where curvature is the same in every direction (space forms). They also describe some related mathematical structure, such as extra freedoms that do not change the geometry, and give explicit examples of self-similar flows.
- **Why it matters**: It is a rigidity result: a broad variational condition forces a very special geometry in dimension three, which ties together calculus of variations, Ricci flow, and the topology of 3-manifolds. Its exact reach beyond the stated setting is not clear from the abstract alone, so the significance should be judged after reading the full proofs.
- **Background needed**: - A metric is a rule for measuring distances on a curved space; "curvature" describes how that space bends.
- The Einstein-Hilbert functional is a number computed from a metric, and "critical" metrics are where it stops changing under small deformations, like a flat spot on a landscape.
- Volume-preserving deformations keep the total size of the space fixed while changing its shape.
- Ricci flow is a process that evolves a metric over time to smooth out curvature; self-similar flows change only by scaling and reshaping in a fixed pattern.
- A closed manifold is a compact space with no boundary; a space form is one with the same curvature in every direction.
- The Poincaré theorem (in its smooth version) concerns when a 3-dimensional space with trivial topology must be a sphere. · level: research-level

<details><summary>Original abstract</summary>

We address the three-dimensional harmonic analogue of Hilbert's variational problem: does criticality of the Einstein-Hilbert functional under volume-preserving Chen-Nagano variations force constant sectional curvature, and how is this rigidity related to Ricci flow and topology? Starting from the known characterization of compact harmonic critical metrics as gradient Ricci solitons, we use Ivey's classification to show that such metrics on closed three manifolds are precisely the space-form metrics, equivalently the stationary metrics of the volume-normalized Ricci flow. We also describe residual gauge one-forms, establish transversality of the Chen-Nagano gauge to infinitesimal diffeomorphism directions, and give explicit self-similar flows. The normalized Ricci-flow velocity is an admissible Chen-Nagano variation for n > = 3, and the smooth Poincar'e theorem admits an equivalent formulation in terms of the existence of harmonic critical metrics

</details>

### [Left-Invariant Kundt Structures on Almost Abelian Lie Groups](https://arxiv.org/abs/2611.34738)
*S. El Bourkadi, M. W. Mansouri* · `math.DG` · arXiv:2611.34738v1 · relevance 0.22

- **In one sentence**: The paper classifies left-invariant Kundt structures on almost abelian Lie groups, giving algebraic existence criteria, admissible real Jordan forms by signature of the abelian ideal, and characterizations of Kundt pairs defining pp-waves and plane waves in arbitrary dimension.
- **In plain words**: The paper studies a special family of symmetric geometric spaces, described by smooth shapes with a consistent way of moving from point to point, and asks which of these spaces admit a particular kind of light-like direction structure. The authors give algebraic tests for when such structures exist and sort the possible forms by a sign pattern. They also identify which cases correspond to pp-waves and plane waves, with examples in four dimensions.
- **Why it matters**: Pp-waves and plane waves are standard exact solutions in general relativity, so a classification of their homogeneous versions in arbitrary dimension is of interest to geometers and mathematical physicists. The text does not indicate applications beyond this classification, so the wider significance is uncertain.
- **Background needed**: - Lie group: a smooth space that is also a group, with symmetries that act the same way at every point (left-invariant means invariant under translation by the group).
- Almost abelian Lie group: a group with a codimension-one abelian ideal, so it is nearly commutative.
- Kundt structure: a geometry with a null (light-like) direction whose flow has special properties, central to Lorentzian geometry.
- pp-wave and plane wave: exact spacetime solutions of Einstein's equations that model gravitational waves, with null directions that are parallel or recurrent.
- Real Jordan form and signature: standard linear-algebra normal forms of a matrix and the count of positive versus negative eigen-directions. · level: research-level

<details><summary>Original abstract</summary>

We study left-invariant Kundt structures on almost abelian Lie groups. We establish algebraic existence criteria and characterize the admissible real Jordan forms according to the signature of the Abelian ideal. We then characterize the Kundt pairs defining pp-waves and plane waves in arbitrary dimension, with particular attention to recurrent and parallel null directions. Examples in dimension four illustrate both plane and non-plane pp-wave geometries.

</details>

## Partial differential equations

### [Viscosity solutions for integro-differential equations with gradient and source terms](https://arxiv.org/abs/2611.34533)
*Russell Schwab, Son N. T. Tu, Olga Turanova* · `math.AP` · arXiv:2611.34533v1 · relevance 0.21

- **In one sentence**: The paper proves comparison and existence (via Perron's method) of viscosity solutions for integro-differential equations with gradient and source terms, using a "global comparison property" together with a local Lipschitz assumption on the defining operator.
- **In plain words**: The paper studies a family of equations that mix a function's rate of change, its slope, and a non-local averaging effect, the kind that arise when a process depends on values far away as well as nearby. It shows that, under its assumptions, these equations have a well-defined solution that is unique and depends stably on the setup. The authors present a single framework that combines two existing styles of argument, one based on min-max structure and one from free boundary problems.
- **Why it matters**: The work aims to unify and extend several earlier results on this class of equations, which is useful for researchers who rely on these tools. The text does not indicate specific applications, so its wider reach beyond the mathematical community is unclear from the excerpt alone.
- **Background needed**: - Partial differential equation (PDE): an equation relating a function to its rates of change in space.
- Integro-differential equation: a PDE that also contains an integral, so the value at a point depends on values elsewhere.
- Viscosity solution: a weak notion of solution that lets equations without smooth solutions still be treated rigorously.
- Comparison principle: if one function is a sub-solution and another a super-solution, the first stays below the second; this gives uniqueness.
- Perron's method: a way to construct a solution as the supremum of sub-solutions.
- Gradient and source terms: a slope-dependent term and a term that adds forcing independent of the derivatives.
- Min-max structure and free boundary problems: two techniques for analysing such equations, mentioned as the sources being combined.
- Well-posedness: existence, uniqueness, and stability of solutions. · level: research-level

<details><summary>Original abstract</summary>

We address global well-posedness for integro-differential equations with gradient and source terms. This naturally results from establishing the comparison principle for viscosity solutions and existence via Perron's method. There are many earlier results for similar equations, and our work attempts to give a unified approach and improve upon some recent examples. There is a natural juxtaposition of earlier results in the usual framework of viscosity solutions which rely on a min-max structure, with some more recent implementations coming from the free boundary literature in which a min-max is not apparent initially, but does appear a posteriori due to certain rigid structural constraints. Here we give a presentation that combines ideas from both situations. The most important feature of the operators in our equations is what we call the global comparison property. This is combined with a natural local Lipschitz assumption on the operator defining the equation.

</details>

### [The confined discrete DLSS equation: gradient flow structure and long-time asymptotics](https://arxiv.org/abs/2611.34197)
*Daniel Matthes, Andr\'e Schlichting* · `math.AP` · arXiv:2611.34197v1 · relevance 0.17

- **In one sentence**: A structure-preserving numerical scheme for the fourth-order DLSS equation with linear confinement on the real line, shown to be a discrete gradient flow of relative entropy with exponential decay to a discrete Gaussian equilibrium via a discrete modified logarithmic Sobolev inequality.
- **In plain words**: This paper studies a discretized version of a fourth-order partial differential equation, the DLSS equation, which describes how a spread-out quantity evolves over time, here confined by a linear restoring force on a line. The authors build a computational scheme that keeps the equation's underlying mathematical structure intact, and show that the scheme's solutions stay positive and settle toward a Gaussian (bell-shaped) equilibrium at an exponential rate. Numerical experiments are reported to support these results.
- **Why it matters**: Preserving an equation's structure in a numerical scheme helps ensure that computed solutions behave like the true ones over long times, which matters for simulations. The paper's decay rate is stated to match the continuum rate as the grid is refined, but the text does not say how it is used beyond this setting.
- **Background needed**: - Partial differential equation: an equation relating a function to its rates of change in space and time.
- Fourth-order: involves up to fourth derivatives, making it harder to analyse than standard diffusion equations.
- Gradient flow: evolution that always moves downhill in a chosen "energy" with respect to a chosen notion of distance.
- Relative entropy: a measure of how far a distribution is from an equilibrium state.
- Gaussian equilibrium: the bell-curve shape the solution converges to over time.
- Logarithmic Sobolev inequality: an inequality bounding how fast a quantity can decay in terms of its dissipation; used to prove exponential rates.
- Mesh size: the spacing of grid points in a numerical method; the limit of small mesh size recovers the continuous equation. · level: research-level

<details><summary>Original abstract</summary>

We propose and analyse a structure-preserving discretization of the fourth-order DLSS equation in dynamically rescaled variables leading to a linear confinement on the one-dimensional real line. The scheme is obtained as a discrete analogue of the Carrillo--Toscani splitting. It allows for a new interpretation of the DLSS equation as gradient flow of the relative entropy with respect to a combined diffusive and transport metric, extending the structure of the discretization introduced in our earlier work with Giuseppe Savar\'{e} for the unconfined equation. We prove global existence of positive solutions and, as the main analytical result, exponential decay of the relative entropy towards the discrete Gaussian equilibrium. The decay rate is obtained via a discrete modified logarithmic Sobolev inequality. The resulting rate is consistent with the continuum rate and converges to it from below in the vanishing mesh-size limit. Numerical results illustrate and confirm our findings.

</details>

## Harmonic analysis

### [Separable models of an NIP Banach space theory](https://arxiv.org/abs/2611.33260)
*Karim Khanaki, Pedro Poitevin* · `math.LO` · arXiv:2611.33260v1 · relevance 0.10

- **In one sentence**: The paper shows that a specific renormed Hilbert-type Banach space has an NIP (no independence property) unstable theory in the pure Banach language, recovers its index order from the norm, and classifies its separable models up to surjective linear isometry by an order type and a Hilbert dimension.
- **In plain words**: The paper studies a particular infinite-dimensional normed space and the logical rules that describe what is true in it. It shows that these rules are "tame" in a technical sense (NIP), and that the space's structure reveals an underlying ordering of its indices. Using that ordering, the author sorts the countably generated versions of the space into a continuum of classes, each labelled by an ordering type and a dimension.
- **Why it matters**: It gives a concrete example where model-theoretic tameness and classification results are carried over to Banach spaces, a setting where such tools are less developed. The text does not say how far the methods extend beyond this example, so broader connections are uncertain.
- **Background needed**: - Banach space: a complete normed vector space, the infinite-dimensional analogue of a space with a length measure.
- Renorming: giving the same space a different but equivalent norm (way of measuring length).
- Ell-2 space (ℓ₂): infinite sequences whose squared entries sum to a finite number, with the usual Hilbert norm.
- Model theory: the study of which statements hold in a structure and how structures are classified by their logical properties.
- Pure Banach language: the logical vocabulary using only the norm and linear operations, with no extra predicates.
- NIP (no independence property): a tameness condition from model theory limiting how complicated definable relations can get.
- Unstable theory: a theory that is not stable, meaning it has enough complexity to define an order.
- Elementary embedding: a map between structures that preserves all first-order statements.
- Surjective linear isometry: a bijective linear map that preserves norms, i.e. an exact structural match of the spaces.
- Uniform metric: a way of measuring distance between functions that compares their worst-case gap. · level: research-level

<details><summary>Original abstract</summary>

Let $Y$ be the renorming of $\ell_2(\mathbb N)\oplus_2\ell_2(\mathbb N)$ with norm $(h^2+q^2)^{1/2}$, where $h$ is the Hilbert norm and $q(u,v)=\sup_{i<j}|u_i+v_j|$. We prove that the unstable theory $\operatorname{Th}(Y)$ is NIP in the pure Banach language. We recover the index order from the Banach norm and classify the continuum many separable models up to surjective linear isometry. The invariants are the order type of a countable model of $\operatorname{Th}(\mathbb N,<)$ and the dimension of a separable Hilbert summand. Every such pair occurs. We describe all elementary embeddings between these models. The bounded norm types over a separable model are separable in the uniform metric exactly when its index order contains no copy of $(\mathbb Q,<)$.

</details>

### [Pietsch's favourite problem on singular traces](https://arxiv.org/abs/2611.34559)
*Gustavo Ara\'ujo, Daniel Pellegrino, Joedson Santos* · `math.FA` · arXiv:2611.34559v1 · relevance 0.10

- **In one sentence**: The paper answers Pietsch's Problem 16 affirmatively by constructing a nonzero bounded singular spectral trace on the weak Weyl ideal over the class of all Banach spaces.
- **In plain words**: The paper concerns a list of open questions about "traces," which are ways of assigning a single number to certain linear operators (maps between infinite-dimensional spaces) in a consistent way. In 2023 the mathematician A. Pietsch posed twenty-seven such questions, and this paper settles the one he considered his favourite. The authors show that a particular kind of nonzero trace exists on a specific family of operators, the weak Weyl ideal.
- **Why it matters**: The abstract is short and does not say what the result is used for, so its wider importance is unclear from the text alone. It is a positive existence result answering a question posed by a leading specialist, which is why it is of interest to people working on operator ideals and traces.
- **Background needed**: - Operators: linear maps between infinite-dimensional spaces, generalising matrices.
- Banach spaces: complete normed vector spaces, the standard setting for infinite-dimensional analysis.
- Operator ideals: families of operators closed under certain algebraic operations, studied as a unit.
- Traces: functionals on an operator ideal that behave like the matrix trace (for example, additive and compatible with composition).
- Singular traces: traces that vanish on finite-rank operators, which is what makes them nontrivial in infinite dimensions.
- Weak Weyl ideal: a specific operator ideal defined through Weyl (approximation-number) type quantities; the text gives no further detail. · level: research-level

<details><summary>Original abstract</summary>

In 2023, A. Pietsch formulated twenty-seven open problems concerning traces on operator ideals. We give an affirmative answer to Problem 16, which Pietsch singled out as his personal favourite, by constructing a nonzero bounded singular spectral trace on the weak Weyl ideal over the class of all Banach spaces.

</details>

## Complex analysis

### [Independence of Thurston eigenvalues and Lyapunov exponents for quadratic rational maps](https://arxiv.org/abs/2611.34186)
*Ayesha Bennett, Holly Krieger* · `math.DS` · arXiv:2611.34186v1 · relevance 0.08

- **In one sentence**: The paper studies post-critically finite quadratic rational maps with both critical points in one cycle, constructing real bitransitive centres in the curve C_2 along which Lyapunov exponents blow up while Thurston eigenvalues stay in a bounded annulus, and showing a spectral gap for these eigenvalues on compact subsets of C_2.
- **In plain words**: This paper is about a family of simple iterated maps of the Riemann sphere, the complex-number version of a rule applied again and again. For a special subclass, the authors look at two numbers that measure how these maps behave: Thurston eigenvalues, which come from a fixed-point structure, and Lyapunov exponents, which measure how quickly nearby points separate under repeated application. They build a sequence of such maps where the Lyapunov exponents grow without bound while the Thurston eigenvalues stay between 1/10 and 1 in size, and they show the eigenvalues stay separated from 1 in size on compact parts of the family.
- **Why it matters**: The work addresses questions raised by Buff, Epstein and Koch, and it suggests that the two measures of stability are not tied together in the way one might hope, at least along this curve. The text does not say what wider consequences follow, so the broader significance is uncertain from this summary alone.
- **Background needed**: - Rational map: a function of one complex variable, ratio of polynomials, acting on the Riemann sphere (complex plane plus a point at infinity).
- Quadratic rational map: a rational map of degree two.
- Critical point: a point where the map locally folds, not one-to-one.
- Post-critically finite: the orbits of critical points eventually land on a finite set of points.
- Critical orbit relation curve C_2: a one-dimensional family in moduli space (the space of maps up to change of coordinates) where the two critical points lie in the same cycle.
- Bitransitive centre: a parameter where both critical points have orbits with the specified cyclic behaviour; treat as a technical term.
- Thurston pullback map and eigenvalues: a combinatorial tool from Thurston's theory that assigns numbers to a fixed point, used to study the map.
- Lyapunov exponent: the average rate at which nearby orbits diverge, a standard measure of chaos.
- Spectral gap: a margin separating the relevant eigenvalues from a threshold, here from modulus 1. · level: research-level

<details><summary>Original abstract</summary>

We study post-critically finite quadratic rational maps $f: \mathbb{P}^1\to\mathbb{P}^1$ where the two critical points lie in the same cycle. The Thurston eigenvalues of $f$ are those of the derivative of the Thurston pullback map $\sigma_f$ at its fixed point. Addressing questions of Buff--Epstein--Koch, we construct a sequence of real, bitransitive centres in the critical orbit relation curve $C_2$ which degenerates in moduli space, and whose Lyapunov exponents tend to infinity whilst the Thurston eigenvalues satisfy $\frac{1}{10}< |\lambda|<1$. We also show the Thurston eigenvalues across all bitransitive centres in $C_2$ have a spectral gap on compact subsets of the curve.

</details>

### [Connectedness Principle in the Complex Analytic Setting](https://arxiv.org/abs/2611.34654)
*Swapnajit Das* · `math.AG` · arXiv:2611.34654v1 · relevance 0.08

- **In one sentence**: The paper proves a complex-analytic (Kähler) version of the connectedness principle for normal compact Kähler pairs, showing the non-klt locus has at most two connected components in each fiber of a suitable morphism, and extends this to generalized pairs with transcendental nef part and to projective morphisms of possibly non-compact analytic varieties.
- **In plain words**: The paper studies shapes of "bad" regions inside geometric spaces that are described by complex equations. It considers a map between such spaces where the pieces sitting over each point are connected, and shows that the singular trouble zone within each piece splits into at most two separate parts. The authors also extend this statement to more general settings and to some non-compact spaces.
- **Why it matters**: Connectedness results of this kind are tools used in birational geometry to control how singularities behave under maps, so the result matters mainly to specialists in that area. The text does not discuss applications beyond this, so its wider significance is unclear from the given text alone.
- **Background needed**: - Complex analytic variety: a space locally described by complex-number equations.
- Kähler manifold/variety: a special kind of complex space with a compatible geometric structure, generalizing projective (algebraic) spaces.
- Normal compact space: a compact space with no pinching in codimension one, "compact" meaning bounded and closed.
- Pair (X, B): a space X together with a weighted divisor B, a combination of special subvarieties with coefficients.
- Nef: a positivity condition on a line bundle or divisor, roughly "not negative on curves."
- Non-klt locus (Nklt): the set of points where the singularities are too severe to be "Kawamata log terminal," a standard mildness condition.
- Proper morphism with connected fibers: a map whose preimages of points are compact and in one piece.
- Connected components: the separate pieces of a set. · level: research-level

<details><summary>Original abstract</summary>

We show that if $(X,B)$ is a normal compact K\"ahler pair and $f:X\to Z$ is a proper morphism with connected fibers to a normal compact K\"ahler variety $Z$ such that $(-K_X+B)$ is nef over $Z$, then $\mathrm{Nklt}(X,B)\cap f^{-1}(z)$ has at most two connected components for every $z\in Z$. More generally, we prove the result for generalized pairs whose nef part is allowed to be transcendental. Moreover, we record that the same result holds for projective morphism between analytic varieties (possibly non-compact).

</details>

## Operator algebras and spectral theory

### [Co-amenability and local reflexivity of $C^*$-algebras](https://arxiv.org/abs/2611.33578)
*Yafei Zhao, Zhe Dong* · `math.OA` · arXiv:2611.33578v1 · relevance 0.14

- **In one sentence**: The paper shows that local reflexivity of C*-algebras passes from a unital subalgebra A to a larger algebra B when the bidual inclusion A** ⊂ B** is co-amenable, and derives several permanence results that answer five questions from Kirchberg's 2011 list.
- **In plain words**: This paper is about a structural property of "operator algebras," which are collections of mathematical operations on spaces, studied as a branch of abstract analysis. The authors ask when a bigger algebra inherits a "local reflexivity" property from a smaller algebra sitting inside it. They prove sufficient conditions for this inheritance and apply them to standard constructions such as tensor products, limits, crossed products, and free products.
- **Why it matters**: The text states that the results answer five specific open questions (b, c, d, f, h) posed by Kirchberg in 2011, so it resolves a named set of problems in the field. The text does not discuss wider applications beyond this area.
- **Background needed**: - C*-algebra: a algebra of bounded operators on a Hilbert space, closed under adjoints and norm limits.
- Unital inclusion: a smaller algebra A sitting inside a larger one B, sharing the identity element.
- Bidual (A**): a much larger "double dual" algebra built from A, used to study A's structure.
- Local reflexivity: a property that lets finite-dimensional pieces of the bidual be approximated by the algebra itself.
- Co-amenability: a condition on how the inclusion of biduals behaves, related to averaging or approximation.
- Exactness, amenable groups, reduced crossed products and free products: standard constructions and classes of groups/algebras used to build new C*-algebras.
- Kirchberg's 2011 list: a published list of open problems about these properties. · level: research-level

<details><summary>Original abstract</summary>

Let $A\subset B$ be a unital inclusion of $C^*$-algebras. We prove that local reflexivity passes from $A$ to $B$ if the inclusion $A^{**}\subset B^{**}$ is co-amenable. It follows that local reflexivity is preserved by minimal tensor products with exact $C^*$-algebras, by inductive limits over directed sets, and by reduced crossed products by discrete amenable groups. We also prove that reduced free products with respect to states with faithful GNS representations preserve local reflexivity and that every locally reflexive $C^*$-algebra embeds into a simple locally reflexive $C^*$-algebra. These results answer Questions~(b), (c), (d), (f) and~(h) in Kirchberg's 2011 list.

</details>

### [Duality of finite-dimensional Hopf $\mathrm{C}^*$-algebra actions via inclusions](https://arxiv.org/abs/2611.33996)
*Anshu, Hyun Ho Lee* · `math.OA` · arXiv:2611.33996v1 · relevance 0.11

- **In one sentence**: The paper studies actions of finite-dimensional Hopf C*-algebras on unital C*-algebras, defining Rokhlin property and approximate representability directly for the action and relating them to the canonical conditional expectation, with a duality between an action and its dual action on the crossed product.
- **In plain words**: This paper is about symmetry in a very abstract setting: operator algebras are collections of "operators" (generalized measurements or matrices) and a finite-dimensional Hopf algebra is a finite set of symmetry-like rules that can act on them. The authors give direct definitions of two regularity conditions, the Rokhlin property and approximate representability, for such symmetry actions. They then show that, for a simple algebra with a simple crossed product under suitable hypotheses, these two conditions swap roles when one passes from the action to its dual action.
- **Why it matters**: The result gives a precise duality between an action and its dual, which extends known symmetry-duality results for group actions to the more general Hopf setting. The text also says these notions are matched with the spatial formulations of Barlak, Szabó and Voigt for separable algebras, and includes examples with and without the Rokhlin property; the broader significance beyond this specialist framework is not stated in the text.
- **Background needed**: - C*-algebra: a algebra of bounded operators closed under adjoints and norm limits, a standard setting for quantum-style observables.
- Unital and simple: contains an identity element, and has no nontrivial closed two-sided ideals.
- Hopf algebra: an algebraic structure generalizing group symmetries, with multiplication and comultiplication; finite-dimensional here.
- Action: a way a symmetry structure acts on an algebra by automorphisms.
- Fixed-point algebra and conditional expectation: the subalgebra left unchanged by the action, and the averaging map onto it.
- Crossed product: a larger algebra built from the action, encoding both the algebra and the symmetry.
- Dual action: the induced symmetry action on the crossed product.
- Rokhlin property: a regularity condition, analogous to a "uniform spread" of the symmetry, from classification theory for group actions. · level: research-level

<details><summary>Original abstract</summary>

We study actions of finite-dimensional Hopf $\mathrm{C}^*$-algebras on a unital $\mathrm{C}^*$-algebra $A$. We first define the Rokhlin property and approximate representability directly for an action $H\curvearrowright A$ and characterize these properties, under appropriate hypotheses, in terms of the corresponding properties of the canonical conditional expectation $E\colon A\to A^H$. Based on this characterization, we establish the following duality for a saturated action on a simple unital $\mathrm{C}^*$-algebra $A$ such that $A\rtimes H$ is simple: 1. $H\curvearrowright A$ has the Rokhlin property if and only if the dual action $H^{\circ}\curvearrowright A\rtimes H$ is approximately representable. 2. $H\curvearrowright A$ is approximately representable if and only if the dual action $H^{\circ}\curvearrowright A\rtimes H$ has the Rokhlin property. For separable $A$, we also identify these properties with the corresponding spatial formulations introduced by Barlak--Szab{\'o}--Voigt, assuming saturation in the Rokhlin comparison. We present examples of Hopf $\mathrm{C}^*$-algebra actions both with and without the Rokhlin property.

</details>

## Algebra

### [A Sweedler dual seen as a terminal object in a category of bialgebras](https://arxiv.org/abs/2611.33910)
*Lo{\"i}c Foissy (LMPA)* · `math.RA` · arXiv:2611.33910v1 · relevance 0.15

- **In one sentence**: The paper shows that the Sweedler dual of K[X] with multiplicative coproduct is terminal among pairs (bialgebra, character), introduces the spectrum of a bialgebra, and studies double bialgebras, near-semirings, and a graph bialgebra linked to Bergman colorations of graphical matroids.
- **In plain words**: This paper studies a specific algebraic structure built from polynomials, called the Sweedler dual, and shows it is a "most general" object among a class of structures that each carry a special kind of map called a character. The authors also look at structures with two compatible ways of splitting elements (double bialgebras), and apply the framework to a construction on graphs that relates to counting ways to color edges.
- **Why it matters**: The "terminal object" result extends a known theorem of Aguiar, Bergeron, and Sottile on combinatorial Hopf algebras from the graded, connected setting to a more general one, which is a meaningful generalization. The link to graphical matroids and Bergman colorations is a connection between algebra and combinatorics, though the abstract does not show how far it reaches.
- **Background needed**: - Bialgebra: an algebra and a coalgebra (a "splitting" operation on elements) that are compatible with each other.
- Sweedler dual: a standard way to turn a bialgebra's structure around, producing a dual bialgebra built from linear maps.
- Character: a special map from the bialgebra to the base field that respects multiplication.
- Terminal object: in category theory, a unique "most general" object that every object of the class maps to in exactly one way.
- Hopf algebra / graded connected setting: a special class of bialgebras with extra structure, used in combinatorics.
- Matroid: an abstract generalization of independence in graphs or vector spaces; graphical matroids come from graphs.
- Near-semiring / near-ring: algebraic structures with addition and multiplication that are weaker than rings. · level: research-level

<details><summary>Original abstract</summary>

We study the Sweedler dual of the polynomial algebra $\mathbb{K}[X]$ equipped with the multiplicative coproduct $\delta(X) = X \otimes X$, and show that the resulting bialgebra $\mathbb{K}[X]^\star$ is the terminal object in the category of pairs $(B, \lambda)$, where $B$ is a bialgebra and $\lambda$ is a character of $B$. This generalizes a result of Aguiar, Bergeron, and Sottile on combinatorial Hopf algebras in the graded and connected setting. We describe the subcoalgebras and subbialgebras of $\mathbb{K}[X]^\star$, which lead to the introduction of the spectrum of a bialgebra. We also study the particular cases double bialgebras (bialgebras equipped with two compatible coproducts), firstly examining their connection to unital near-semirings or near-rings. Introducing a subbialgebra of $\mathbb{K}[X]^\star$ obtained from the intersection with another Sweedler dual, we prove it is the terminal object in the category of double bialgebras. As a consequence, we show that the spectrum of any double Hopf algebra is a subgroup of the group of roots of unity. This imply that not any bialgebra can become double. We finally apply this framework to a bialgebra of graphs with a coproduct given by contraction and deletion of edges, relating its invariants to Bergman colorations of edges arising from graphical matroids.

</details>

### [On some problems regarding a group-theoretical generalization of the Gauss formula](https://arxiv.org/abs/2611.34371)
*Marius T\u{a}rn\u{a}uceanu* · `math.GR` · arXiv:2611.34371v1 · relevance 0.14

- **In one sentence**: The paper resolves three open problems about the values of the function f(G) = (1/|G|) · Σ_{H≤G} |Aut(H)|, summing automorphism-group sizes over subgroups, for noncyclic finite groups G, as posed in an earlier paper by the same line of work (cited as FT23).
- **In plain words**: This note is about a number attached to a finite group, a collection of symmetry-like objects. For each smaller group sitting inside it (a subgroup), one counts how many ways that subgroup can be symmetrically rearranged onto itself, then averages these counts over the whole group. An earlier paper posed three open questions about this number for groups that are not cyclic, and this note answers all three.
- **Why it matters**: The function is described as a group-theoretic analogue of the Gauss formula, a classical identity in number theory, so the results may matter to people studying that connection. The text itself does not give further applications, so the wider significance is unclear from this excerpt alone.
- **Background needed**: - Finite group: a set of finitely many elements with a rule for combining them, such as rotations of a polygon.
- Subgroup: a smaller group contained inside a larger one.
- Automorphism: a way of relabeling a group's elements that preserves its structure; |Aut(H)| counts these.
- Cyclic group: a group generated by one element, like the integers mod n under addition; noncyclic groups are all the others.
- Gauss formula: a classical identity in number theory that the paper's function is modeled on.
- The excerpt gives no explicit results, so the specific answers to the three problems cannot be stated here. · level: research-level

<details><summary>Original abstract</summary>

In \cite{FT23}, we introduced the group-theoretical function $f(G) = \frac{1}{|G|}\sum_{H \le G} |\Aut(H)|$ for a finite group $G$ and posed three open problems concerning its values on noncyclic groups. In this note, we provide complete solutions to all three problems.

</details>

## Representation theory

### [Higher rewriting for strong linearly distributive coherence](https://arxiv.org/abs/2611.34596)
*Max Demirdilek, Christian Reiher, Christoph Schweigert* · `math.CT` · arXiv:2611.34596v1 · relevance 0.10

- **In one sentence**: The paper uses higher rewriting, following Guiraud and Malbos, to prove a coherence theorem for strong linearly distributive categories: every formal diagram built from their structure commutes.
- **In plain words**: This paper is about a rule-based method for checking when two different ways of combining mathematical objects give the same result. The authors apply this method to a structure called a strong linearly distributive category, which has two ways of combining objects that interact through reversible rules. They report that in such a structure, every formal diagram they can draw using these rules commutes, meaning all routes between the same endpoints agree.
- **Why it matters**: Coherence theorems tell mathematicians when they can safely ignore which of many equivalent routes they took, which simplifies working with these structures. The text does not say what applications or further connections the result has, so its wider significance is unclear from this abstract alone.
- **Background needed**: - Category: a collection of objects and arrows (maps) between them, with rules for composing arrows.
- Commutative diagram: a diagram where all paths between two points give the same result.
- Coherence theorem: a result (such as Mac Lane's for monoidal categories) saying that all diagrams built from certain rules commute, so only the rules themselves need checking.
- Rewriting: repeatedly replacing parts of an expression using fixed rules to decide whether two expressions are equivalent.
- Higher rewriting: the same idea applied to higher-dimensional objects (cells) that relate maps between maps.
- Tensor product and distributor: two ways of combining objects and a rule relating them, used in logic and linear algebra-style settings. · level: research-level

<details><summary>Original abstract</summary>

Rewriting is a computational method to solve word problems: deciding whether two compound expressions, or words, are equivalent with respect to a set of identities. Higher rewriting generalizes rewriting to higher-dimensional words, or cells, in higher categories. Following Guiraud and Malbos, we use higher rewriting to generalize Mac Lane's coherence theorem. Our result concerns strong linearly distributive categories: categories equipped with two unital tensor products related by invertible distributors. We show that in a strong linearly distributive category every formal diagram commutes.

</details>

### [Proof of a cardinality conjecture for the correction terms in the quantum $K$-theoretic divisor axiom](https://arxiv.org/abs/2611.33597)
*Mizuki Takahashi* · `math.QA` · arXiv:2611.33597v1 · relevance 0.09

- **In one sentence**: The paper proves a cardinality conjecture of Kato and Sagaki on directed paths in the quantum Bruhat graph, which makes their cancellation-free quantum K-theoretic divisor axiom for full flag manifolds in the quasi-minuscule case hold unconditionally.
- **In plain words**: This is a result in abstract algebra about the geometry of flag manifolds, which are spaces of nested subspaces. The authors settle a counting question posed by two other mathematicians: for certain special sets of paths, the number of paths is always either one or even, and when it is even their signed sum cancels to zero. This removes the need to assume the conjecture in a earlier formula, so that formula is now established without that assumption.
- **Why it matters**: The result turns a conditional statement into an unconditional one, which matters for anyone relying on the Kato–Sagaki divisor formula. The text also states a theorem for arbitrary Coxeter groups, a broader class of symmetry groups, though its wider applications are not described in the text.
- **Background needed**: - Flag manifolds: spaces parametrizing chains of nested subspaces, central to representation theory.
- Coxeter groups: abstract symmetry groups generated by reflections, which index the structure of flag manifolds.
- Bruhat order and the quantum Bruhat graph: combinatorial structures (directed graphs on group elements) encoding how cells and quantum corrections interact.
- Quantum K-theory: a deformed version of K-theory, a tool that counts geometric objects using algebraic invariants, with "quantum" terms coming from counting rational curves.
- Divisor axiom: a rule saying how intersections with divisors (codimension-one subvarieties) affect quantum invariants.
- Demazure products: a product operation on elements of Coxeter groups used to combine reflections.
- Quasi-minuscule case: a restricted class of root systems where the highest root is close to the smallest nonzero weights. · level: research-level

<details><summary>Original abstract</summary>

We prove a conjecture due to Kato and Sagaki (arXiv:2604.04476) concerning the cardinality of sets of directed paths in the quantum Bruhat graph that occur in the quantum $K$-theoretic divisor axiom for the full flag manifolds in the quasi-minuscule case. We prove that the cadinality is equal to one or even, and its signed sum vanishes in the latter case. Consequently, the cancellation-free divisor axiom obtained by Kato and Sagaki under this conjecture holds unconditionally. The proof uses Schremmer's results on affine Bruhat order and Demazure products, together with a theorem that we prove for arbitrary Coxeter groups.

</details>

## Number theory

### [Counting complex elliptic curves with self-quotients via class numbers](https://arxiv.org/abs/2611.34150)
*Radu Gaba* · `math.NT` · arXiv:2611.34150v1 · relevance 0.15

- **In one sentence**: The paper counts isomorphism classes of complex elliptic curves that admit a finite subgroup C of order n with E/C isomorphic to E, expressing these counts as sums of proper class numbers over explicit finite sets of negative discriminants, with a Smith normal form proof and a Magma implementation.
- **In plain words**: The paper studies a special kind of elliptic curve (a smooth curve with a group structure, used widely in number theory and cryptography) that can be divided by a finite group of symmetries and still come back to itself. It turns the question of how many such curves exist into a count of arithmetic objects called class numbers, which measure how many essentially different number-theoretic structures a given discriminant allows. The authors also give an explicit bound on which discriminants matter, check the counting procedure with a computer program in Magma, and show numerical examples.
- **Why it matters**: It gives an explicit arithmetic counting formula for a classification that earlier work described in more structural terms, so the results can be checked and computed directly. The text does not claim wider consequences, and its connections to other areas are not spelled out beyond the link to that earlier CM classification.
- **Background needed**: - Elliptic curve: a smooth cubic curve over the complex numbers that also carries a group law; its points form a torus-like group.
- Isogeny and quotient E/C: dividing the curve by a finite subgroup C yields another curve; the question is when the result is isomorphic to E itself.
- Complex multiplication (CM): curves with extra symmetries, governed by quadratic imaginary fields and their discriminants D (negative integers).
- Class number h(D): a count of inequivalent ways to represent numbers by quadratic forms of discriminant D; it is finite and computable.
- Norm form Q_D(x,y): a quadratic polynomial in two variables attached to D, used to encode the endomorphism.
- Smith normal form: a standard matrix reduction that reveals the invariant factors (the shape of a finite abelian group).
- Cyclic vs noncyclic group: whether a finite abelian group is generated by one element or needs more. · level: research-level

<details><summary>Original abstract</summary>

Let \(n>1\) be an integer. We consider complex elliptic curves \(E\) admitting a finite subgroup \(C\subset E(\mathbb C)\) of order \(n\) such that \(E/C\) is isomorphic to \(E\). % with the additional requirement that the invariant factors of (C) are unequal. We establish class-number counting formulas for the cyclic, noncyclic, and general cases. More precisely, we associate to every negative quadratic-order discriminant \(D\) the norm form \[ Q_D(x,y)=x^2+\varepsilon_Dxy+q_Dy^2, \] where \[ \varepsilon_D\in\{0,1\},\qquad q_D=\frac{\varepsilon_D^2-D}{4}. \] The invariant factors of the kernel of the corresponding endomorphism are determined by \(\gcd(x,y)\). This leads to finite sets of admissible discriminants describing the cyclic, noncyclic, and general cases with unequal invariant factors. Our main result expresses the numbers of isomorphism classes in the three cases as sums of the proper ideal class numbers \(h(D)\) over explicitly defined finite sets of admissible discriminants. This provides an arithmetic class-number counting formulation of the CM classification developed in earlier work by \cite{CanepaGaba2014,CanepaGaba2019,CanepaGabaOlteanu2022} and its subsequent algorithmic extensions. We also characterize the equal-invariant-factor case: it occurs precisely when $n=m^2$, and in that case every complex elliptic curve satisfies the required condition, with the unique subgroup being $E[m]$. We derive an explicit bound for the admissible discriminants, implement the counting procedure in Magma, and give numerical examples. The proof relies on the Smith normal form of the multiplication matrix associated with a quadratic integer. The results provide an arithmetic class-number counting formulation of the CM classification developed in earlier work.

</details>

### [Irreducible trinomials over the binary field: an elliptic-curve criterion and explicit families](https://arxiv.org/abs/2611.34282)
*Siyuan Fu, Zhiming Li, Huaiqing Zuo* · `math.NT` · arXiv:2611.34282v1 · relevance 0.15

- **In one sentence**: The paper gives an elliptic-curve-based criterion for when the trinomial X^((4^k+2)/3)+X+1 is irreducible over F_2, and builds infinite families of irreducible trinomials X^m+X^n+1 in fourteen reduced exponent classes.
- **In plain words**: The paper studies polynomials with three terms, built from 0s and 1s, that cannot be factored into smaller polynomials (the "irreducible" ones). It shows that one specific family of these is irreducible exactly when a certain related number is prime and a particular condition on 2 holds. It also lists infinite families of such three-term polynomials by transforming known cases.
- **Why it matters**: Irreducible polynomials over the field with two elements matter for coding theory and cryptography, where they are used to build finite-field arithmetic. The text itself does not discuss these applications, so the link is a general expectation rather than something the paper claims.
- **Background needed**: - Polynomials over F_2: expressions whose coefficients are only 0 or 1, with arithmetic done mod 2.
- Irreducible polynomial: one that cannot be written as a product of two smaller non-constant polynomials, analogous to a prime number.
- Trinomial: a polynomial with three nonzero terms, such as X^m + X^n + 1.
- Elliptic curve: a specific type of cubic curve whose points carry a group structure; used here as a tool to test irreducibility.
- Reciprocity law: a general rule relating the answers to modular questions for pairs of numbers, used here in the proof.
- Prime number and primitive root: a prime p is one with no nontrivial divisors; 2 is a primitive root mod p when powers of 2 cycle through every nonzero residue mod p.
- Power substitution and linearization: standard ways of turning a known polynomial into a new one with different exponents. · level: research-level

<details><summary>Original abstract</summary>

We study irreducible trinomials over $\mathbb{F}_2$. Using an elliptic curve and reciprocity laws, we prove that, for $k \ge 2$, $X^{(4^k+2)/3}+X+1$ is irreducible if and only if $4^k+3$ is prime and $2$ is a primitive root modulo that prime. By power substitution and linearization, we also assemble explicit infinite families of irreducible trinomials $X^m+X^n+1$ in fourteen distinct reduced exponent classes.

</details>

## Algebraic geometry

### [The Dolbeault geometric Langlands-type conjecture for smooth surfaces](https://arxiv.org/abs/2611.33778)
*Yukinobu Toda* · `math.AG` · arXiv:2611.33778v1 · relevance 0.09

- **In one sentence**: The paper builds semiorthogonal decompositions for moduli stacks of one-dimensional sheaves on smooth surfaces with nef anti-canonical divisor, identifies their pieces as quasi-BPS categories of local Calabi-Yau threefolds, and proposes a Dolbeault geometric Langlands-type conjecture for surfaces with Hecke actions.</one_liner>
<parameter name="plain">This paper is about a precise mathematical framework that sorts the collection of certain geometric objects (sheaves on curves sitting inside a surface) into simpler, well-behaved building blocks. The authors compare these building blocks with categories of semistable sheaves and use that comparison to propose a conjecture generalizing the Dolbeault geometric Langlands conjecture, which relates Higgs bundles to a dual picture. The text indicates the construction is general but gives only a sketch of the examples and of the Hecke actions.
- **Why it matters**: It connects algebraic geometry, representation theory and the geometric Langlands program, and for symplectic surfaces it is expected to lift known Hecke operators on BPS cohomology to a categorical level. Whether the conjecture holds is not established in the text, so its significance rests on future verification.
- **Background needed**: - Coherent sheaves: algebraic objects generalizing vector bundles, used to describe geometric families.
- Moduli stack: a space parametrizing such objects, including their automorphisms.
- Semiorthogonal decomposition: a way of splitting a category into pieces that interact in a controlled order, analogous to a basis.
- BPS cohomology / quasi-BPS categories: invariants from string theory counting "protected" states, here attached to Calabi-Yau threefolds.
- Calabi-Yau threefold and nef anti-canonical divisor: special geometric shapes and a positivity condition on a curve class.
- Higgs bundles and (Dolbeault) geometric Langlands: moduli of bundles with an extra field, and a conjectural duality between categories attached to them.
- Hecke operators: symmetries that move between related moduli spaces. · level: research-level

<details><summary>Original abstract</summary>

Using a general theory of limit categories for symmetric stacks, we construct their semiorthogonal decompositions for moduli stacks of pure one-dimensional coherent sheaves on smooth surfaces with nef anti-canonical divisors. The components of these semiorthogonal decompositions are quasi-BPS categories associated with the corresponding local Calabi--Yau threefolds. By comparing these semiorthogonal decompositions with those of dg-categories of coherent sheaves on moduli stacks of semistable sheaves, we propose a Dolbeault geometric Langlands-type conjecture for surfaces, generalizing the Dolbeault geometric Langlands conjecture for $\GL_r$-Higgs bundles. Our conjecture includes a correspondence for Higgs bundles twisted by sufficiently ample line bundles on curves. We discuss examples and construct Hecke actions on limit categories and, under certain conditions, on quasi-BPS categories. For symplectic surfaces, these actions are expected to provide a categorical lift of the corresponding Hecke operators on BPS cohomology constructed by Davison--Hennecart--Kinjo--Schiffmann--Vasserot.

</details>

### [Cohomology of pseudo-reductive groups over local function fields](https://arxiv.org/abs/2611.34570)
*Zev Rosengarten* · `math.NT` · arXiv:2611.34570v1 · relevance 0.07

- **In one sentence**: The paper gives a duality pairing identifying the first Galois cohomology of a pseudo-reductive group over a local function field with the Pontryagin dual of the group of translation-invariant line bundles on that group, and equips Picard groups of schemes over Hausdorff topological fields with a topology having good properties.
- **In plain words**: The paper studies a certain kind of symmetry group (a "pseudo-reductive group") defined over a local function field, which is a number-like system built from polynomials over a finite field. It shows that a standard algebraic invariant of this group can be read off as the dual of another natural object, the group of "translation-invariant line bundles" on it. To do this, the authors put a topology on the Picard group, the group that classifies line bundles, and show this topology behaves well under mild conditions.
- **Why it matters**: This is a precise structural result in arithmetic algebraic geometry, relevant to duality theorems for algebraic groups over local fields. The abstract does not say what applications it has, so its wider significance beyond this area is unclear from the text alone.
- **Background needed**: - Algebraic group: a geometric object that is both an algebraic variety and a group, such as matrices with determinant one.
- Pseudo-reductive group: a well-behaved class of algebraic groups, generalizing reductive groups such as those of matrix groups, used in arithmetic settings.
- Local function field: the field of Laurent series over a finite field, a "local" completion of the rational functions in one variable.
- Galois cohomology: an invariant measuring obstructions to solving equations over a field, using the symmetries (Galois group) of the field's extensions.
- Line bundle and Picard group: a way of attaching a one-dimensional vector space to each point of a space; the Picard group collects these up to equivalence.
- Pontryagin dual: for a topological abelian group, the group of continuous homomorphisms into the circle (or unit complex numbers); a standard duality.
- Topological field: a field with a topology compatible with its arithmetic operations; Hausdorff means distinct points can be separated. · level: research-level

<details><summary>Original abstract</summary>

We give a pairing which describes the first Galois cohomology of a pseudo-reductive group $G$ over a local function field $K$ as the Pontryagin dual of the group $\Ext^1(G, \Gm)$ of translation-invariant line bundles on $G$. In order to accomplish this, we endow the Picard group of a scheme $X$ over a (Hausdorff) topological field with a topology, and prove that this topology enjoys favorable properties under certain mild conditions on $X$ and on the field.

</details>

## Topology

### [Colored Jones polynomial of figure eight knot and non-perturbative topological recursion](https://arxiv.org/abs/2611.34110)
*Alexander Hock, Sergey Shadrin* · `math-ph` · arXiv:2611.34110v1 · relevance 0.10

- **In one sentence**: The paper proves that the asymptotic expansion of the colored Jones polynomial of the figure eight knot is linked to non-perturbative topological recursion on its elliptic spectral curve, as proposed by Borot and Eynard.
- **In plain words**: This work is about knots, the tangled loops studied in topology, and a family of numbers called the colored Jones polynomial that encodes information about a knot. The author looks at how these numbers behave for large values of the color parameter, and shows they match a predicted structure coming from a recursive method built on a special curve. The summary given here is brief, so the exact steps of the proof are not described.
- **Why it matters**: It supports a proposal by Borot and Eynard that links knot invariants to a recursive method from mathematical physics and geometry, and it gives a concrete test case, the figure eight knot. The text does not say how far the connection extends beyond this knot, so the wider significance is uncertain.
- **Background needed**: - Knot: a closed loop tangled in three-dimensional space; the figure eight knot is the simplest non-trivial example with this name.
- Colored Jones polynomial: a sequence of polynomials assigned to a knot, indexed by a "color" (a dimension parameter), used as a knot invariant.
- Asymptotic expansion: a series that approximates a quantity well as a parameter grows large, though it may not converge exactly.
- Perturbative vs. non-perturbative: perturbative terms are the first-order approximation series; non-perturbative terms are extra corrections invisible to that series.
- Topological recursion: a method that builds counting data recursively from a geometric object called a spectral curve.
- Elliptic spectral curve: a spectral curve of genus one, with a shape tied to elliptic curves. · level: research-level

<details><summary>Original abstract</summary>

The asymptotic expansion of the colored Jones polynomial of the figure eight knot is proved to be connected with non-perturbative topological recursion on the underlying elliptic spectral curve, following the proposal of Borot and Eynard.

</details>

### [Regular Additive Scalar Invariants of ${\mathcal N}=1$ Hyperbolic Spin Supertriangles](https://arxiv.org/abs/2610.23209)
*Ilia Gaiur, Robert Penner* · `math.GT` · arXiv:2610.23209v1 · relevance 0.07

- **In one sentence**: The paper classifies regular cyclic scalar invariants of non-degenerate hyperbolic N=1 spin supertriangles that are additive under geodesic subdivision, finding a superdimension 3|1 space of such invariants using a "common-first" gauge fixing a 3|4 modulus.
- **In plain words**: The paper studies triangles in a curved (hyperbolic) space whose sides and corners carry extra "odd" algebraic bookkeeping of the kind used in supersymmetry. It asks which measurable quantities of such triangles stay consistent when a triangle is cut into smaller pieces, and it sorts those quantities by their algebraic degree. The text reports that the quantities form a small family: ordinary area, two even-type quantities, and one odd-type quantity.
- **Why it matters**: The result is a classification within a narrow mathematical framework, so its importance depends on how well the framework is used elsewhere; the text does not say. It may connect to supergeometry and to geometric ideas about angle defects, but the text itself does not establish such links.
- **Background needed**: - Hyperbolic geometry: geometry on a surface of constant negative curvature, where triangle angles sum to less than 180 degrees.
- Angle defect: the shortfall from the Euclidean angle sum; in hyperbolic triangles it equals the area.
- Additivity under subdivision: a quantity that equals the sum of its values on the pieces when a triangle is cut by a geodesic (shortest-path line).
- Supergeometry: a extension of geometry with "odd" coordinates that square to zero, graded by degree; superdimension counts even and odd directions.
- Spin lift: a choice of extra structure (a sign choice) needed to define spinor-type data on the triangle.
- Gauge fixing: choosing a canonical representative so that redundant parameters are removed, leaving a clean modulus. · level: research-level

<details><summary>Original abstract</summary>

We classify regular cyclic scalar invariants of non-degenerate hyperbolic ${\mathcal N}=1$ spin supertriangles which are additive under geodesic subdivision. After fixing the spin lift, the common-first gauge (introduced in earlier work by the second-named author and further developed here) gives a complete $3|4$ modulus of such supertriangles.. The space of additive scalar invariants is proved to have superdimension $3|1$: ordinary hyperbolic area in degree zero, two even generators in degree two, and one odd generator in degree three; the degree-one and degree-four sectors vanish. One degree-two generator is the fermionic first variation of body area, equivalently the nilpotent correction from ordinary body angle defect to super angle defect. The degree-three generator changes sign under reversal of the spin lift, while the other generators are fixed, so ordinary supertriangles carry only three even invariants.

</details>

## Dynamical systems

### [Integrable nearest neighbor interaction Hamiltonians and the rigidity of the Toda Lattice](https://arxiv.org/abs/2611.34251)
*Vadim Kaloshin, Illya Koval, Daniel Tsodikovich* · `math.DS` · arXiv:2611.34251v1 · relevance 0.14

- **In one sentence**: The paper shows that certain analytic deformations of the three-particle nearest-neighbour Toda lattice potential destroy integrability, without assuming anything about the form of the integrals, using a high-energy link between Toda orbits and billiard orbits in polytopes.
- **In plain words**: The paper studies a simple model of particles in a line, where each particle only pushes on its immediate neighbours, and a specific famous version of this model called the Toda lattice, which can be solved exactly. The authors change the force law slightly and ask whether the model can still be solved exactly. They find that some kinds of smooth changes break this exact solvability, and they prove this without having to guess what the hidden conserved quantities would look like.
- **Why it matters**: It addresses when a special, exactly solvable physical system is rigid, meaning small changes to it lose the special structure. The authors link this to the rigidity of ellipses in billiards, a known result in a different area, and the link runs through high-energy motion in the Toda lattice resembling billiard motion in polytopes. The text does not say how far the method extends beyond three particles.
- **Background needed**: - Hamiltonian system: a mechanical model whose motion is determined by energy (a potential) and momentum.
- Integrable system: one with enough conserved quantities to determine its motion exactly; these are rare and special.
- Nearest-neighbour interaction: each particle interacts only with the adjacent ones in a chain.
- Toda lattice: a classical, known integrable chain of particles with exponential-type neighbour forces.
- Analytic deformation: a smooth change of the force law given by a convergent power series.
- Billiards and polytopes: a ball bouncing inside a region with flat sides (a polytope); its motion is a classic test case in dynamics.
- Local rigidity: a special property that survives only for a narrow class of nearby systems. · level: research-level

<details><summary>Original abstract</summary>

We consider mechanical Hamiltonian systems, where the potentials describe a nearest-neighbor interaction law. In this setting, a non trivial example of an integrable system is the celebrated Toda lattice. We study deformations of this potential (for three particles), and show that some classes of analytic deformations of the potential break its integrability, without assuming anything about the form of the integrals. This result is reminiscent of local rigidity of ellipses in billiards. The proof relies on the fact that high energy orbits for the Toda lattice approximate billiard orbits in some polytopes.

</details>

### [Limit laws for Siegel theta sums](https://arxiv.org/abs/2611.34514)
*Jory Griffin, Jens Marklof, Tariq Osman* · `math.NT` · arXiv:2611.34514v1 · relevance 0.10

- **In one sentence**: The paper proves limit laws and precise heavy-tail asymptotics for the modulus of normalised Siegel theta sums when the quadratic form is chosen at random from the full space of quadratic forms or from the space of diagonal forms, extending work of Jurkat–Van Horne and Götze–Gordin.
- **In plain words**: The paper studies a type of sum over whole-number lattice points where each term is a rotating phase set by a quadratic form (a rule built from squares and products of variables). Choosing that rule at random and letting the range of summation grow, the authors show the size of the normalised sum follows a limiting pattern. That pattern depends on which family the rule is drawn from, and they give detailed descriptions of its long tail for two such families.
- **Why it matters**: The result sharpens classic limit theorems for one-variable theta sums and extends them to several variables and Siegel half-spaces, which is a useful step in the probabilistic theory of such sums. The text does not claim wider consequences, and any further connections would need checking against the full paper.
- **Background needed**: - Lattice sum: adding terms indexed by integer points (whole-number coordinates) in a growing region.
- Exponential sum: a sum of terms of the form e^(2πi·x), i.e. unit-length rotating phases, so terms can cancel.
- Quadratic form: a polynomial in several variables where every term has degree two (e.g. x² + 3xy).
- Limit law: a theorem saying a normalised random quantity converges to a fixed probability distribution.
- Heavy-tail asymptotics: precise description of how often very large values occur, governed by a tail that decays slowly.
- Metaplectic group and Shale–Weil representation: an algebraic symmetry group and a way of representing it on functions, used as the main tool.
- Unipotent flows in ergodic theory: a family of measure-preserving motions on a symmetric space whose long-run behaviour is studied. · level: research-level

<details><summary>Original abstract</summary>

Siegel theta sums are exponential sums over the integer lattice whose phases are determined by a quadratic form. For a random choice of quadratic form, we prove a limit law for the modulus of the normalised sum as the summation range tends to infinity. The limiting distribution depends on the space from which the quadratic form is sampled. We prove precise heavy-tail asymptotics for random sampling from (a) the full space of quadratic forms and (b) the space of diagonal forms. This study extends classic results by Jurkat and Van Horne for one-variable theta sums and by G\"otze and Gordin for theta series on Siegel half-spaces. Our approach uses the Shale--Weil representation of the metaplectic group and the ergodic theory of unipotent flows.

</details>

## Combinatorics

### [List coloring degenerate graphs with requests](https://arxiv.org/abs/2611.34348)
*Rajat Adak, L. Sunil Chandran, Shiwali Gupta et al.* · `math.CO` · arXiv:2611.34348v1 · relevance 0.10

- **In one sentence**: The paper improves bounds on (k,ε)-flexibility for d-degenerate graphs at the extreme list sizes k = d+2 and k = 2d, and at satisfaction ratio 1/(d+1).
- **In plain words**: The paper studies a graph-colouring puzzle: each node has a short list of allowed colours, and some nodes come with a requested colour. The question is how many requests can be honoured at once while still giving every node a colour from its list. The authors prove three results that push the trade-off between list size and the fraction of requests that can be met to its limits.
- **Why it matters**: The text shows the limiting example (the complete graph on d+1 vertices) that fixes the extreme values, and the results sharpen bounds near those extremes. Its wider relevance beyond this graph-theory setting is not discussed in the text, so I cannot say more.
- **Background needed**: - Graph: a set of vertices joined by edges; a colouring gives each vertex a colour so that adjacent vertices differ.
- d-degenerate graph: one whose vertices can be removed one at a time, each having at most d neighbours among those remaining.
- List colouring: each vertex has its own allowed list of k colours rather than a common palette.
- Requests: some vertices ask for a particular colour from their list; a colouring 'satisfies' a request if it gives that colour.
- (k,ε)-flexible: for any lists of size k and any set of requests, at least an ε fraction of the requests can be satisfied.
- Complete graph on d+1 vertices: every pair is adjacent, which forces the list size to be at least d+1 and the satisfiable fraction to be at most 1/(d+1).
- Big-O style bounds: 'inverse exponential' vs 'inverse polynomial' describe how fast the guaranteed fraction shrinks as d grows. · level: research-level

<details><summary>Original abstract</summary>

We prove three results on the flexible list coloring of $d$-degenerate graphs. Following Dvo\v{r}\'{a}k, Norin and Postle [J. Graph Theory 2019], a graph $G$ is $(k,\epsilon)$-flexible if for any assignment $L$ of lists of size $k$ to its vertices and any choice of requested colors by a set $\widehat V$ of the vertices from their respective lists, there is an $L$-coloring satisfying at least $\epsilon|\widehat V|$ of the requests. The complete graph on $d+1$ vertices shows that if all $d$-degenerate graphs are $(k,\epsilon)$-flexible for some list size $k$ and satisfaction ratio $\epsilon$, then $k \geq d+1$ and $\epsilon\leq\tfrac1{d+1}$. Our results concern values at or near these extremes. For list size $d+2$, we improve the satisfaction ratio from an inverse exponential to an inverse polynomial function of $d$. For satisfaction ratio $\tfrac1{d+1}$, we prove that it is achievable for list size $2d$ as well as $\left\lfloor(d+2)\left(2-\tfrac1e\right)\right\rfloor$ (which is less than $2d$ for $d\geq 9$).

</details>

### [Monoid Representation of the Determinants of the Adjacency Matrices of 1-joined Path Graphs](https://arxiv.org/abs/2611.34794)
*Daniel Pinzon, Daniel Pragel, Joshua Roberts et al.* · `math.CO` · arXiv:2611.34794v1 · relevance 0.06

- **In one sentence**: The paper studies determinants of adjacency matrices of labeled path graphs joined by a single edge, shows these determinants form a finite monoid under matrix multiplication, and characterizes that monoid via a representation theory from Khovanov et al. (2024).
- **In plain words**: The paper looks at simple networks made of paths of dots joined together by one connecting line, where each piece carries a label that says how it is joined. For each such network it computes a single number, the determinant of its adjacency matrix (a grid recording which dots are linked). The authors report that these numbers combine under a rule that behaves like multiplication of matrices, and they describe that structure completely.
- **Why it matters**: The work gives a finite algebraic structure that is fully described, and the authors say it yields general formulas for chains of joined labeled paths. Its wider significance is unclear from the text alone; it builds on earlier work by the same authors and on a 2024 representation-theory framework.
- **Background needed**: - Graph: dots (vertices) joined by lines (edges); a path graph is a simple chain of dots.
- Adjacency matrix: a square grid of 0s and 1s recording which dots are directly linked.
- Determinant: a single number computed from a square grid that summarizes some of its properties.
- Monoid: a set with an associative combining rule and an identity element, like multiplication of numbers but not necessarily with inverses.
- Finite monoid of matrices: a finite collection of matrices closed under matrix multiplication.
- Representation theory: a way of studying abstract algebraic structures by mapping them to concrete matrices or linear transformations. · level: research-level

<details><summary>Original abstract</summary>

Following previous work by these authors, this paper explores all labeled path graphs joined by 1 edge where the labeling contains the information on how to join that graph. The algebraic structure that this operation has on the determinant of the adjacency matrix of the graph gives a finite monoid of matrices under matrix multiplication. We completely characterize the monoid using the representation theory discussed in Khovanov et al(2024). Finally, we demonstrate how these results can be used to find general formulas for the determinants of chains of 1-joined labeled paths.

</details>

## Numerical analysis

### [Barron Smoothness for Layers in Deep Neural Networks](https://arxiv.org/abs/2611.34805)
*G. Welper* · `cs.LG` · arXiv:2611.34805v1 · relevance 0.14

- **In one sentence**: The paper splits deep network approximation error into choosing infinite-width limits per layer and then discretizing each layer, shows the discretization cost is governed by a layer-wise generalization of Barron norms in expectation, and characterizes local minima of the optimization by an equidistribution principle.
- **In plain words**: The paper studies how well deep neural networks can approximate a target function and how many units they need to do so. The authors break the problem into two steps: first pick the best idealized version of each layer with unlimited width, then approximate each layer with a finite number of units. They report that the cost of the second step is captured by a generalized version of a smoothness measure called Barron norms.
- **Why it matters**: Approximation error bounds tell us what network sizes are needed for a given accuracy, so a layer-by-layer account of this could clarify why deep networks work. The text also links the optimal solutions to equidistribution, an idea from adaptive spline and finite element methods, which may suggest connections to classical numerical analysis; the extent of this link beyond the abstract is not shown here.
- **Background needed**: - Neural network layer: a stage that transforms inputs using many simple units (neurons).
- Width: the number of units in a layer; "infinite width limit" means treating that number as unbounded.
- Approximation error: how far the network's output is from the target function.
- Discretization: replacing a continuous idealized object with a finite set of units.
- Barron norm: a measure of how smooth or structured a function is, controlling how well shallow networks can approximate it.
- Equidistribution: spreading a resource (here, approximation effort or units) so that error is balanced across regions; a classic idea in adaptive mesh and spline methods.
- Local minimum: a point where an optimization stops improving nearby, though not necessarily the best overall. · level: research-level

<details><summary>Original abstract</summary>

In order to bound approximation errors for deep neural networks, we split the problem into two steps: First the selection of optimal infinite width limits for each layer and second an optimal discretization of all layers to obtain finite sized networks. We show that in expectation, the latter problem is equivalently characterized by a layer wise generalization of Barron norms. Moreover, we provide an analysis of the optimization landscape and show that local minima are characterized by an equidistribution principle akin to similar ideas in adaptive spline and finite element approximation.

</details>

### [CAMPS: Composable Adapters for Mixed-Precision Solvers](https://arxiv.org/abs/2611.33703)
*Kevin Li, Chandrajit Bajaj* · `cs.MS` · arXiv:2611.33703v1 · relevance 0.13

- **In one sentence**: CAMPS is a framework that chains iterative-refinement adapters across floating-point precisions (FP64, FP32, FP16) inside solver trees, with proven interface compatibility, a backward-error guarantee for reported successes, and a per-boundary convergence condition, tested on dense and sparse systems.
- **In plain words**: Computers store numbers with different amounts of detail, and faster, less precise arithmetic can speed up solving large systems of equations if it is used carefully. This paper describes CAMPS, a way to plug lower-precision solvers into higher-precision ones at several levels, with a checking step that rejects any correction that makes the error worse. The authors prove three properties of the design and report tests on five configurations, where it was faster than a double-precision direct solver on some dense systems and as fast as a comparable nested method while using less memory, but not faster than plain conjugate gradient on symmetric positive definite sparse systems.
- **Why it matters**: Mixed-precision computing matters for simulations and machine learning workloads where memory and speed are limited, so a reusable way to combine precisions could be useful. The text reports speedups and memory savings only for the authors' own tests and implementation, so how well these carry over to other problems is not shown here.
- **Background needed**: - Floating-point precision: how many binary digits a computer uses to store a number; FP64 is more precise than FP32, which is more precise than FP16.
- Linear system: a set of equations Ax = b, which many scientific computations reduce to.
- Direct vs. iterative solver: a direct solver computes the answer in a fixed set of steps (e.g., via factorization); an iterative solver improves a guess step by step.
- Iterative refinement: solving roughly in low precision, measuring the leftover error (residual) in high precision, and correcting the answer.
- Residual and backward error: the leftover mismatch after solving, and the size of the input change that would make the computed answer exact.
- Conjugate gradient: a classic iterative method for symmetric positive definite matrices.
- Conditioning: how sensitive a system is to small errors; ill-conditioned systems are harder to solve accurately. · level: research-level

<details><summary>Original abstract</summary>

Mixed-precision solvers usually assign a fixed precision to each algorithmic component. This makes it hard to reuse a lower-precision solver at different depths inside a higher-precision solver. We introduce CAMPS (Composable Adapters for Mixed-Precision Solvers), a framework that uses iterative refinement to connect solvers across precisions. An adapter computes residuals and updates in the precision of its parent and passes each correction solve to a child solver in a lower precision. The child can be a direct solver, an iterative solver, or another adapter. The adapter checks every correction and keeps it if the residual does not increase. We prove three results. Adapters can be placed at any compatible set of precision boundaries in a solver tree without breaking the solver interface. Every output that the root solver reports as successful satisfies a backward-error bound set by the stopping tolerance and the root precision. Convergence follows from one sufficient condition per boundary, computed from the leaves of the tree to its root. We test five configurations on dense and sparse systems in 64-bit, 32-bit, and 16-bit floating-point arithmetic (FP64, FP32, and FP16). On dense well-conditioned systems, CAMPS is up to 9.6x faster than an FP64 direct solver for a single solve that includes the factorization. On sparse nonsymmetric systems, a three-precision hierarchy is the fastest method we tested. Compared with our implementation of the nested solver F3R, CAMPS is as fast and uses about 3.4x less peak memory. CAMPS does not always win. Plain conjugate gradient is faster on sparse symmetric positive definite systems. On very ill-conditioned systems, FP32 corrections fail, and the adapter detects the failure and switches to an FP64 fallback.

</details>

## Logic and foundations

### [A Sequent Calculus for the Quantified Reflection Calculus $\mathrm{QRC}_1$: Cut-Elimination, Interpolation, and NP-Completeness](https://arxiv.org/abs/2611.33345)
*Mitar Nedeljkovi\'c* · `math.LO` · arXiv:2611.33345v1 · relevance 0.05

- **In one sentence**: The paper gives the first Gentzen-style sequent calculus for the first-order modal logic QRC_1, proves cut-admissibility, interpolation, and finite model property results, and claims NP-completeness of its decision problem over fixed signatures.
- **In plain words**: This paper is about a formal logic, a precise system of rules for what counts as a valid argument about provability (what a mathematical theory can prove about itself). The authors build a new proof system of the standard "sequent calculus" type for an existing logic called QRC_1, which extends provability reasoning to quantifiers such as "for all" and "there exists." Using this system, they establish several structural properties and state that deciding whether a formula is valid for this logic is in the NP class of problems.
- **Why it matters**: The work matters to specialists in proof theory and modal logic because it gives a clean proof system for a logic that is claimed to avoid a known completeness barrier for quantified provability logics. Its link to the arithmetic of Peano and Heyting Arithmetic makes it relevant to the foundations of mathematics, though the broader significance depends on the details of the proofs, which the brief does not show.
- **Background needed**: - Modal logic: logics with operators like "it is provable that," studied with possible-worlds (Kripke) semantics.
- Provability logic: modal logic whose operator is read as "provable in a formal theory," linked to Peano and Heyting Arithmetic.
- Quantifiers: "for all" and "there exists," which make the logic first-order rather than purely propositional.
- Sequent calculus (Gentzen style): a proof system that builds proofs from sequents (premises ⊢ conclusions) using inference rules.
- Cut-elimination: showing that a detour rule ("cut") can always be removed from proofs, which gives strong control over proof structure.
- Craig interpolation: if an implication holds, there is a shared-vocabulary intermediate statement that links its two sides.
- NP-complete: a class of decision problems where yes-answers can be checked quickly, and which are believed but not proven to be hard to solve quickly.
- Finite model property: if a formula is valid, it holds in some finite model. · level: research-level

<details><summary>Original abstract</summary>

We introduce $\mathrm{G3QRC}_1$, the first Gentzen-style sequent calculus for Borges and Joosten's Quantified Reflection Calculus ($\mathrm{QRC}_1$). As a strictly positive, first-order modal logic, $\mathrm{QRC}_1$ crucially escapes Vardanyan's $\Pi^0_2$-completeness theorem for quantified provability logic, while remaining arithmetically complete with respect to Peano and Heyting Arithmetic. The central innovation of $\mathrm{G3QRC}_1$ is a pair of context-erasing modal rules that simultaneously account for the monotonicity and transitivity axioms by deliberately discarding parametric context across modal boundaries. This structural bottleneck allows for a clean proof of cut-admissibility via a standard lexicographic induction, circumventing the complex loop-checking typically required for provability logics. Cut admissibility yields an instantiated subformula property and supports a direct canonical proof of the finite model property. We streamline the adequate Kripke semantics by interpreting constants globally. We also establish a split-context Craig interpolation theorem and a contextual form of left uniform interpolation, uniformly eliminating private predicate symbols, constants, and free parameters. Finally, by leveraging the rigid structural constraints of the context-erasing rules and the absence of left-branching connectives, we prove that, over the standard fixed countable signatures specified in the paper, the decision problem for $\mathrm{QRC}_1$ is $\mathbf{NP}$-complete, situating this quantified modal logic in a comparatively low nondeterministic complexity class.

</details>

### [Well-foundedness of the strict Lipschitz order on countably complete filters](https://arxiv.org/abs/2611.34850)
*Gabriel Fernandes, Matheus Duzi* · `math.LO` · arXiv:2611.34850v1 · relevance 0.04

- **In one sentence**: In ZF+DC, the strict Lipschitz order on proper countably complete filters on a fixed ordinal is shown well-founded, and ultrafilters on the same ordinal are shown to be equal when mutually nonexpansively reducible, answering both parts of Question 9.2.11 in The Ultrapower Axiom.
- **In plain words**: This paper is about a way of comparing "large-set systems" (filters) built on the ordinal numbers, which are the counting levels of infinity used in set theory. The author shows that under the standard background axioms (ZF plus dependent choice), this comparison cannot go on forever in a descending chain, and that two such systems which can each be reduced to the other are the same. These are answers to two specific open questions posed in a published book on set theory.
- **Why it matters**: The text settles two questions from The Ultrapower Axiom, a book proposing a principle about ultrapowers (a standard tool for building models of set theory). It is a targeted result for specialists; the text does not say more about its wider impact.
- **Background needed**: - Ordinals: the well-ordered counting levels of infinity, starting 0, 1, 2, ... and continuing past all ordinary counting.
- Filters and ultrafilters: families of "large" subsets of a set; an ultrafilter decides for every subset whether it is large.
- Countably complete: closed under intersecting countably many large sets.
- Well-founded order: one with no infinite descending chain.
- ZF and DC: the standard axioms of set theory (Zermelo-Fraenkel) plus dependent choice, a weak form of the axiom of choice.
- Lipschitz/nonexpansive reducibility: a way of saying one filter can be mapped into another in a controlled, distance-preserving-type fashion.
- Transfinite recursion: defining objects by recursion along ordinals. · level: research-level

<details><summary>Original abstract</summary>

In $\mathsf{ZF}+\mathsf{DC}$, the strict Lipschitz order on proper countably complete filters on any fixed ordinal is well-founded. The proof uses transfinite recursion and closure under countable intersections to derive a contradiction from a descending chain. Restricting each filter to the least ordinal it contains yields a set-like well-founded order that compares filters on different ordinals. In $\mathsf{ZF}$, two ultrafilters on the same ordinal are equal if each is nonexpansively reducible to the other. These results answer both parts of Question 9.2.11 in The Ultrapower Axiom.

</details>

## Mathematical physics

### [The integrable Lie-Trotter-Suzuki decomposition for nonlinear dynamics: Efficient Hamiltonian simulation of the Stepanoff flow](https://arxiv.org/abs/2611.34768)
*Ilon Joseph, Ivan Novikau, Michael R. Montgomery et al.* · `quant-ph` · arXiv:2611.34768v1 · relevance 0.08

- **In one sentence**: The paper proposes an "integrable Lie-Trotter-Suzuki" time-stepping scheme for nonlinear dynamics and applies it to simulating the Stepanoff flow on a torus via a unitary, quantum-circuit-style construction using QFT and QSP, checked against an emulated fault-tolerant quantum computer.</one_liner>
<parameter name="plain">The paper looks at how to compute the step-by-step evolution of a nonlinear system, meaning one where effects do not simply add up, by recasting it as a reversible, unitary process that a quantum computer could run. The authors split the system's rule of change into pieces that can each be handled efficiently, then chain those pieces together in small time steps. They test the approach on a two-dimensional flow on a torus (a donut-shaped surface), and report that the results agree with several other classical methods when run on an emulator of a fault-tolerant quantum computer.</plain>
<why>The method offers a route for bringing nonlinear dynamical systems within reach of tensor-network and quantum-computing tools, which are built around linear, reversible operations. The text itself notes two limits: small time steps are needed for accuracy, and the transfer operator grows linearly with grid size, so the practical advantage over classical methods is not established here.</why>
<background>
- Nonlinear dynamics: systems whose future behaviour does not scale simply with their inputs; they are generally hard to simulate exactly.
- Unitary evolution: a reversible, norm-preserving way of stepping a system forward, the form quantum computers use.
- Lie-Trotter-Suzuki decomposition: a standard way to approximate a total evolution by alternating simpler pieces over small time steps; accuracy improves with smaller steps and higher-order formulas.
- Integrable parts: pieces of the dynamics that can be solved exactly or factorised efficiently.
- Block-encoding: embedding a non-unitary matrix inside a larger unitary operation so a quantum computer can apply it.
- Quantum Fourier transform (QFT) and quantum signal processing (QSP): standard quantum subroutines, used here to build the simulation circuit.
- Stepanoff flow on the torus: a two-dimensional test system from mathematical physics, used as a non-integrable example.
- Transfer operator (Koopman-type linear view): a linear operator that tracks how functions of the state evolve, which lets nonlinear flows be treated with linear tools.
</background>
<difficulty>research-level</difficulty>
</invoke>

<details><summary>Original abstract</summary>

We propose an efficient unitary numerical time integration strategy for nonlinear dynamical systems: the integrable Lie-Trotter-Suzuki decomposition (I-LTS). First, express the generator as a sum of integrable parts. Second, approximate the full evolution operator using a Lie-Trotter-Suzuki (LTS) decomposition of the desired approximation order in time step. The I-LTS construction ensures that the full evolution operator can be represented as a product of terms that each have an efficient explicit tensor product factorization that can be handled efficiently with tensor network and/or quantum block-encoding methods. Next, we apply this method to an important non-integrable point example of a dynamical system: the Stepanoff flow on the torus. First, we derive an efficient unitary quantum algorithm for simulating the Stepanoff flow that can be thought of as a unitary classical version of a quantum map. Then, we provide a detailed description of the encoding of the two-dimensional system into an efficient quantum circuit, including an efficient block-encoding for all required operators. An efficient Hamiltonian simulation algorithm is constructed using a sequence of alternating quantum Fourier transforms (QFT) and Quantum Signal Processing (QSP) circuits. Finally, the circuit is simulated using a numerical emulator of fault-tolerant quantum computers, and the results are found to be consistent with several alternative classical computational methods. While efficient, the need for Trotterization introduces fundamental complexity in requiring small enough time step for an accurate approximation and solving for the transfer operator requires one to confront the linear scaling of the advection operator with grid size.

</details>

### [Schwinger-Dyson recursion, Gr\"obner elimination and graph combinatorics](https://arxiv.org/abs/2611.34114)
*Oleg Evnin* · `math-ph` · arXiv:2611.34114v1 · relevance 0.08

- **In one sentence**: Applies Schwinger-Dyson equations and Gröbner elimination from zero-dimensional quantum field theory to build a finite recursion for counting labelled regular graphs, reported for 9- and 10-regular graphs.
- **In plain words**: The paper concerns counting how many ways a set of n labelled points can be connected by lines so that every point has the same number of connections (a "regular graph"). The authors borrow a tool from quantum physics, equations that relate averages to one another, and use a standard algebra procedure to reduce an endless chain of these relations to a small, finite set of building blocks. For 9- and 10-regular graphs this gives a recipe that computes the total count using a number of steps that grows in proportion to n.
- **Why it matters**: Counting graphs is a hard combinatorial problem, and the paper claims a large speed-up over the existing state of the art for these particular degrees, which matters for simplicial approaches to quantum gravity that rely on such counts. The text does not show how far the method extends beyond 9- and 10-regular graphs, so its wider reach is unclear.
- **Background needed**: - Regular graph: a network of points (vertices) and links (edges) where every vertex has the same number of links.
- Labelled count: graphs whose vertices are numbered, so different numberings count as different graphs.
- Zero-dimensional QFT: a toy version of quantum field theory with no space or time, reducing to multivariate Gaussian integrals (averages over bell-shaped distributions).
- Schwinger-Dyson equations: identities from integration by parts that link higher averages (moments) to lower ones.
- Gröbner elimination: a standard algebra method for rewriting a system of polynomial relations in terms of a chosen basis.
- Recursion with finite depth and width: a computation that repeats a fixed-size step, so its cost grows predictably with n.
- Big-O notation: O(n) means the number of operations grows roughly linearly with n. · level: research-level

<details><summary>Original abstract</summary>

Schwinger-Dyson equations are a cornerstone of quantum field theory (QFT). Derived using integration by parts, they capture relations between correlators of different orders, forming an open, infinite-dimensional system. In zero-dimensional QFTs with polynomial actions, which is just a physical interpretation for multivariate Gaussian integrals with polynomial insertions, conventional Gr\"obner elimination can be used to express all higher-order correlators (moments) in terms of a fixed basis set. One consequence is a closed finite-dimensional system of differential equations for the coupling dependence of these `master' correlators. An important application of zero-dimensional QFTs is in counting discrete geometric structures (as in simplicial approaches to quantum gravity). For the problem of counting labelled regular graphs, applying this Schwinger-Dyson closure results in a computational breakthrough relative to the existing state-of-the-art: for 9- and 10-regular graphs on $n$ vertices, a finite-depth, finite-width recursive formulation is obtained, making it possible to compute the total graph counts in $O(n)$ arithmetic operations.

</details>

## Optimization and control

### [Policy and Value Iteration for Entropy-Regularized Stochastic Control](https://arxiv.org/abs/2611.34002)
*Yuling Jiao, Peiying Wu, Jerry Zhijian Yang et al.* · `math.OC` · arXiv:2611.34002v1 · relevance 0.15

- **In one sentence**: The paper analyzes a policy-and-value iteration scheme for finite-horizon entropy-regularized stochastic control with action-independent diffusion, giving a uniform error bound and convergence conditions tied to the Hamilton-Jacobi-Bellman equation.
- **In plain words**: The paper studies how to steer a system that is buffeted by random noise over a fixed time window, while also rewarding the controller for keeping its choices spread out rather than fixed. The authors alternate two steps: they approximately evaluate the cost of the current strategy, then reset the strategy to a probability-weighted form derived from that cost. They show that if the errors in both steps shrink to zero, the resulting strategy's cost approaches the best achievable value.
- **Why it matters**: The text gives a provable error bound and tests on two finite-horizon problems plus a discounted routing problem with twelve modes and an unregularized benchmark up to 10,000 dimensions. Its relevance beyond control theory is not stated in the text, so broader applications are unclear.
- **Background needed**: - Stochastic control: choosing actions over time when outcomes contain random noise.
- Hamilton-Jacobi-Bellman (HJB) equation: a partial differential equation whose solution gives the best achievable cost from each state and time.
- Entropy regularization: adding a penalty for committing too firmly to one action, which makes the best strategy a spread-out probability distribution.
- Gibbs distribution: a probability distribution that favors low-cost choices, weighted exponentially by cost.
- Kullback-Leibler (KL) divergence: a measure of how far one probability distribution is from another.
- Policy iteration vs. value iteration: alternating between evaluating a strategy's cost and improving the strategy.
- Uniform convergence: error shrinking everywhere in the state space, not just at some points. · level: research-level

<details><summary>Original abstract</summary>

We study finite-horizon entropy-regularized stochastic control with action-independent diffusion. To solve the associated Hamilton-Jacobi-Bellman (HJB) equation, we alternate between value and policy updates. Each iteration approximately solves a linear backward equation for the current policy, then approximates the Gibbs distribution defined by the resulting value gradient. We prove a uniform bound on the final policy's excess regularized cost. The bound assigns explicit, summable weights to the evaluation residuals and the Kullback-Leibler divergences from the updated policies to their Gibbs targets. Under the stated assumptions and with exact terminal data, vanishing errors in both steps imply uniform convergence to the optimal value. Two finite-horizon execution problems test value accuracy against a known solution and closed-loop performance when no exact solution is available. We also evaluate the iteration on a discounted infinite-horizon routing problem with twelve modes and an unregularized HJB benchmark in up to 10,000 dimensions.

</details>

### [The Monge Optimal Transport Barycenter Problem with Adaptive Features](https://arxiv.org/abs/2611.34494)
*Yige Zhou, Esteban G. Tabak* · `math.OC` · arXiv:2611.34494v1 · relevance 0.15

- **In one sentence**: The paper extends data-driven Monge optimal transport barycenters, which map an outcome to a version statistically independent of covariates, by making the test-function features themselves adaptive (Gaussian RBFs with learned centers and bandwidths) and extending the method to multidimensional covariates.
- **In plain words**: The paper studies how to adjust a measurement so that it no longer depends on other variables, such as age or weather, while changing it as little as possible. The authors let the building blocks used to detect that dependence (bump-shaped functions) move and change width during the fit, rather than keeping them fixed. In synthetic tests, this adaptive version removed more of the dependence than fixed bumps with the same limited number of functions, and came close to what a larger fixed set achieved.
- **Why it matters**: Choosing the right features is a practical bottleneck when removing dependence numerically, so an automatic way to pick them could make such methods less dependent on expert guesswork. The text reports synthetic results and applications to age-related biomedical data and bike-sharing demand, but it does not give enough detail to judge how broadly the gains would hold.
- **Background needed**: - Optimal transport: a way of finding the cheapest map that moves one distribution of values into another; a Monge map is a single deterministic rule for doing so.
- Barycenter (here): a transformed version of an outcome that keeps it as close as possible to the original while removing its link to covariates.
- Statistical independence: two variables carry no information about each other; dependence removal aims for this.
- Test functions / features: chosen functions whose averages are used to check whether dependence is still present; finite sets of them make the independence condition approximate.
- Radial basis functions (RBFs): smooth bump-shaped functions centered at a point with a set width; here both centers and widths are optimized.
- Covariates: the other observed variables (e.g., age, temperature, humidity) that the outcome should be made independent of. · level: research-level

<details><summary>Original abstract</summary>

The data-driven Monge optimal transport barycenter problem seeks a map $y=T(x,z)$ that minimally perturbs an outcome $x$ while removing its statistical dependence on covariates $z$. Numerical implementations approximate the independence constraint through finite-dimensional test-function spaces, making the effectiveness of dependence removal sensitive to the choice of features. This article develops a procedure whereby the features themselves are optimized throughout the procedure. In particular, we adopt a feature space for $f$ consisting of Gaussian radial basis functions (RBFs) with adaptive individual centers and bandwidths. Synthetic experiments show that while fixed nonlinear RBF features can capture dependence structures that are poorly represented by linear features, adapting the RBF centers and bandwidths can further improve dependence removal within a limited feature space and achieve residual dependence comparable to that obtained with a larger fixed basis. We further extend the formulation to multidimensional covariates and evaluate its applicability to real-world problems, including removing age-related dependence in biomedical measurements and dependence on temperature and humidity in bike-sharing demand.

</details>

## Statistics theory

### [Estimation for High-Dimensional Hawkes Processes with Inhibition via CIR Approximation](https://arxiv.org/abs/2611.33484)
*Nadia Belmabrouk, Mohamed Ben Alaya, Xavier Erny* · `math.ST` · arXiv:2611.33484v1 · relevance 0.07

- **In one sentence**: The paper proposes parametric estimators for a high-dimensional Hawkes process with inhibition by approximating it with a CIR (Cox-Ingersoll-Ross) diffusion, giving an explicit convergence rate in a joint large-population, long-time regime and establishing consistency and asymptotic normality of the estimators.
- **In plain words**: The paper studies a model of many interacting random event streams, where each event can make others more or less likely to occur, and inhibition means events suppress further activity. The authors replace the complicated event model with a simpler, smoother random process (a CIR process) that is easier to work with. This lets them build estimators of the model's unknown parameters that are straightforward to compute.
- **Why it matters**: Estimating interaction parameters in large networks of events matters for fields such as neuroscience, finance and social modelling, where spikes or trades influence one another. The text gives a stated convergence rate and asymptotic results, but it does not show how the methods perform beyond the numerical experiments it mentions, so its practical reach is unclear from this summary alone.
- **Background needed**: - Hawkes process: a random process of events (like spikes or trades) where each past event changes the chance of future events; "inhibition" means it lowers them instead of raising them.
- High-dimensional: many interacting components at once, here a large population of such processes.
- CIR process: a mean-reverting random process, often used in finance for interest rates, whose noise term depends on its current level, which makes it hard to analyse (the "non-Lipschitz" issue).
- Diffusion approximation: replacing a jumpy process by a smooth continuous one that behaves similarly when the population is large.
- Consistency: estimates converge to the true values with more data. Asymptotic normality: estimation errors follow a bell-shaped distribution in large samples.
- Convergence rate: how quickly the approximation error shrinks as population and time grow. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we develop a parametric estimation method for a high-dimensional Hawkes processes with inhibition. The proposed approach relies on a quantitative approximation of the Hawkes process by a Cox-Ingersoll-Ross (CIR) process. In particular, we establish an explicit convergence rate in the joint large-population and long-time regime. This result requires specific techniques to handle the non-Lipschitz diffusion coefficient of the limiting CIR process.Based on this approximation, we construct explicit and easily implementable estimators of the model parameters. We establish their consistency and asymptotic normality. We also conduct numerical experiments to illustrate our findings.

</details>

### [PrO Filtering via Kernel Mean Embedding Dynamics](https://arxiv.org/abs/2611.34809)
*Linfeng Wang, Nikolas N\"usken, Chris. J. Oates* · `stat.ME` · arXiv:2611.34809v1 · relevance 0.05

- **In one sentence**: The paper gives the first particle-based (nonparametric) implementation of predictively-oriented (PrO) filtering, using kernel mean embedding dynamics to transport particles from the forecast to the PrO filtering distribution along a path with a closed-form rate.
- **In plain words**: Filtering is the task of tracking a hidden quantity over time from noisy readings, such as following a moving object from radar returns. When the model used for this is slightly wrong, standard Bayesian filters can become overconfident and drift off course. This paper develops a way to run a recently proposed filter that is designed to stay cautious in those cases, without assuming the uncertainty has a simple bell-shaped form.
- **Why it matters**: The method targets settings where the usual Bayesian filters are known to fail under misspecification, and the authors claim it handles this better than a Gaussian version of the same filter in hard nonlinear examples. It is a methods paper, so its practical value depends on the empirical evidence and on how it scales, which the summary text does not fully establish.
- **Background needed**: - State-space model: a hidden process evolving over time, observed through noisy measurements.
- Filtering: updating beliefs about the hidden state as each new observation arrives.
- Model misspecification: the assumed model differs from the true process, so the filter's beliefs can be wrong.
- Bayesian update and tempering: the standard way to combine a forecast with an observation, and a gradual path between them.
- PrO filtering: an update that hedges, placing probability near both the forecast and the observation when they conflict.
- Gaussian approximation: representing uncertainty as a bell curve, which can be too restrictive.
- Particles and kernel mean embeddings: representing a distribution by a cloud of sample points and moving those points with a kernel-based flow. · level: research-level

<details><summary>Original abstract</summary>

Filtering methods are routinely deployed with misspecified state-space models, where Bayesian filters can diverge and become overconfident. Predictively-oriented (PrO) filtering is a recent, hyperparameter-free alternative that was demonstrated to outperform (generalised) Bayesian filtering methods when either the dynamical model or the measurement model is structurally misspecified. This can be attributed to \emph{hedging} behaviour: when an observation conflicts with the forecast, the PrO update places mass near both. Yet existing implementations of PrO filtering rely on unimodal (Gaussian) approximations, whose ability to effectively hedge is limited. This paper develops the first nonparametric, particle-based implementation of PrO filtering. The key obstacle, that PrO filtering distributions are only implicitly defined, is overcome by constructing a path from the predictive to the PrO filtering distribution whose rate is available in closed form, enabling the use of kernel mean embedding dynamics for measure transport. The resulting algorithm requires only simulation from the dynamical model and evaluations of the likelihood, with neither importance weights nor the predictive density. Moreover, as we prove, the number of pseudo-time steps it requires does not grow with the outlyingness of the observation, in contrast to transport along the Bayesian tempering path. An empirical assessment shows substantial improvement over Gaussian variation of PrO filtering in challenging nonlinear examples where Gaussian approximation is unreasonably limited.

</details>

## Statistical methods and applications

### [Using waveform types, discrete Sobolev distances, and trend compatibility to cluster short time series of clinical data](https://arxiv.org/abs/2611.33623)
*Robyn J. N. Kettlitz, Daniel Cisternas, Alvaro Olivera-Nappa et al.* · `q-bio.QM` · arXiv:2611.33623v1 · relevance 0.12

- **In one sentence**: A nonparametric method groups short, undersampled clinical response curves (five-point oral glucose tolerance tests) into response types by factorizing them into unit waveforms, filtering by trend compatibility, and comparing shapes with discrete Sobolev-type distances.
- **In plain words**: The paper looks at blood glucose and insulin curves recorded during a standard sugar-drink test, where each person has only five measurements over a few hours. Instead of fitting a model to each person, the authors sort the curves by their rises and falls, so that curves with the same overall pattern are grouped together. On 1283 such tests, they report 7 glucose response types and 8 insulin response types.
- **Why it matters**: Short clinical curves are common, and standard clustering methods can blur away the direction a curve takes, which is the physiologically meaningful part. The approach may transfer to other tests that record a system's response to a standard disturbance on a short time grid, but the text does not show this beyond the authors' claim.
- **Background needed**: - Oral glucose tolerance test (OGTT): a patient drinks a sugar solution and blood samples are taken at fixed times to see how the body clears glucose and secretes insulin.
- Time series: a sequence of measurements over time; "undersampled" means only a few points are recorded.
- Clustering: grouping items so that members of a group are similar and different groups are not.
- Finite differences: the step-by-step changes between neighbouring measurements; higher orders capture changes in the changes, i.e., curvature-like behaviour.
- Sobolev-type distance: a way of measuring how far apart two curves are, using both their values and their smoothness/derivative-like differences.
- Nonparametric: the method does not assume a fixed mathematical model with a set of parameters.
- Resampling validation: checking that a result holds up when the data are repeatedly subsampled or reshuffled.
- Glycemia/insulinemia: blood glucose and blood insulin levels. · level: research-level

<details><summary>Original abstract</summary>

Clinical tests, such as the oral glucose tolerance test (OGTT), perturb a physiological system at rest and record its excursion over a fixed protocol window as a short, undersampled time series. Such curves rarely allow parameter identification at the individual level, yet their trends carry physiological information that emerges at the population level as recurrent response patterns. Standard clustering methods aggregate differences globally and average out those trends, losing precisely the information about how the system regains control after the perturbation; identifying response patterns requires a method that preserves them. We present a nonparametric framework that factorizes each curve into unit waveforms, sorts them with a symbolic trend-compatibility filter, and compares compatible shapes using discrete Sobolev-type distances on finite differences up to order $k$. The number of clusters, i.e., distinct response types, equals the number of realizable trend patterns the cohort populates, validated by resampling. Applied to 1283 five-point OGTTs, the method identifies 7 glycemia and 8 insulinemia types. The count holds across a threefold range of resolution. In benchmarks against six classical clustering methods, ours alone never mixes opposite trends, with comparable reconstruction error and stability. Clinical normality, assessed after clustering, is graded, overlapping, and distributed unevenly across response types ($h=0.14$--$0.48$). Overall, our method distinguishes response types among curves too short for alignment-based methods yet too informative for reduction to summary values. It applies to any protocol recording a system's response to a standardized perturbation on a short grid.

</details>

### [k-Nearest Neighbors estimation of the drift of an ergodic diffusion process under Osgood regularity](https://arxiv.org/abs/2611.33596)
*Eddy Michel Ella-Mintsa* · `stat.ME` · arXiv:2611.33596v1 · relevance 0.10

- **In one sentence**: The paper proves consistency of k-nearest-neighbors estimators for the drift (deterministic trend) coefficient of an ergodic diffusion process over compact and non-compact intervals, under relatively weak regularity (Osgood-type) conditions.
- **In plain words**: The paper looks at a common method from machine learning, k-nearest neighbors, and asks whether it can reliably estimate the steady pull or push that governs a randomly jiggling process that settles into a long-run pattern, such as a stock-like price or a physical particle. Until now, this method had mostly been tested with computer experiments rather than backed by mathematical proof. The authors prove that the estimates converge to the true values under fairly mild assumptions, over both bounded and unbounded ranges, and support this with numerical illustrations.
- **Why it matters**: It moves a popular, intuitive estimation tool from experimental evidence to a formal guarantee for a standard class of random-process models, which matters for anyone fitting such models to data. The text does not discuss specific applications, so its practical reach beyond this setting is unclear.
- **Background needed**: - Diffusion process: a random process that evolves continuously, like a particle jittering in a fluid; its drift is the systematic part of its motion.
- Ergodic: the process forgets its starting point and settles into a stable long-run behavior, so long observations can be averaged.
- Nonparametric estimation: estimating an unknown function from data without assuming a fixed formula for it.
- k-nearest neighbors: estimating a value at a point by averaging the k observations closest to it.
- Consistency: as more data arrive, the estimate converges to the true value.
- Osgood regularity: a mild smoothness condition on the coefficients, weaker than the usual textbook assumptions. · level: research-level

<details><summary>Original abstract</summary>

The k-Nearest Neighbors (kNN) algorithm is a widely used machine learning method with well-established theoretical guarantees for consistent estimation in multivariate settings and functional time series analysis. In the context of nonparametric estimation of the coefficients of ergodic diffusion processes, however, its use has so far been mainly illustrated through numerical experiments. The main contribution of this paper is to establish theoretical consistency results for drift kNN estimators over both compact and non-compact intervals, under relatively weak regularity conditions on the coefficients of the underlying ergodic diffusion process. The theoretical results are completed with numerical illustrations.

</details>

## AI industry news

### [Clay helps sales teams win with Codex and ChatGPT](https://openai.com/business/customer-stories/clay-plugins-openai)
** · `openai.com` · OpenAI News · relevance 0.07

- **In one sentence**: A short announcement describing how Clay, a sales-data platform, has integrated ChatGPT and Codex so its users can research deals and build go-to-market plans, with GPT-6 models handling the reasoning.
- **In plain words**: Sales teams often spend hours gathering information about potential customers and deciding how to approach them. This item says that Clay, a company whose software collects and organizes business data, now connects with OpenAI's ChatGPT and Codex tools so users can research deals and turn that data into sales plans. The text says GPT-6 models do the reasoning, but it gives no details on how well this works.
- **Why it matters**: It is a small example of AI assistants being built into everyday business software, which is a trend many companies are pursuing. The text is too brief to show whether the integration performs better than existing methods, so its wider significance is unclear.
- **Background needed**: - Clay: a software platform that gathers and organizes data about companies and contacts for sales and marketing teams.
- Go-to-market (GTM): the plan a company uses to reach customers and sell a product, including who to target and how.
- ChatGPT and Codex: OpenAI's AI tools; ChatGPT answers questions in conversation, while Codex is oriented toward writing and working with code.
- GPT-6: named in the text as the model doing the reasoning; the text gives no further information about it.
- Integration: a connection that lets one software product use another's tools inside its own interface.
- The article is a brief promotional-style announcement and includes no data, results, or independent evaluation. · level: introductory

<details><summary>Original abstract</summary>

ChatGPT and Codex integrations help Clay’s users research deals and turn data into go-to-market plays, with GPT-6 models handling the reasoning.

</details>

### [The questions Jensen Huang and Nvidia will still have to answer about Megaspeed](https://techcrunch.com/2026/11/25/the-questions-jensen-huang-and-nvidia-will-still-have-to-answer-about-megaspeed/)
*Tim Fernholz* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.05

- **In one sentence**: A news piece raising open questions about what Nvidia knew regarding the destination of its chips sold through Megaspeed, and whether Jensen Huang's personal relationship with a Megaspeed executive should have made Nvidia doubt that company's assurances.
- **In plain words**: The article is about an investigation into whether the chip maker Nvidia knew where its advanced processors ended up after they were sold to a company called Megaspeed. It also asks whether a personal relationship between Nvidia's chief executive, Jensen Huang, and a Megaspeed executive gave Nvidia reason to distrust what Megaspeed said about where the chips went. The text is short and only poses these questions, so it does not report any findings.
- **Why it matters**: Chip sales are closely watched because export rules limit where advanced AI chips can be shipped, so whether a seller knew its buyer was passing chips on could matter for compliance. The text does not give details of the investigation or any outcome, so its wider significance is unclear.
- **Background needed**: - Nvidia makes graphics processors (GPUs) that are the main hardware for training and running AI models.
- Governments, including the US, restrict exports of advanced chips to certain countries and require sellers to know where chips go ("know your customer" checks).
- Megaspeed is the company named in the article; the text does not explain its business beyond this.
- Jensen Huang is Nvidia's chief executive.
- The article's central claim is an open question about knowledge and motive, not an established fact.
- The text is brief and gives no details of the investigation, sources, or responses from the companies. · level: introductory

<details><summary>Original abstract</summary>

The central question for investigators is what Nvidia knew about where those chips ended up and whether Huang's affair with a Megaspeed executive gave the company reason to doubt Megaspeed's assurances.

</details>

### [Jensen Huang still thinks a succession plan creates unnecessary hierarchy](https://techcrunch.com/2026/11/24/jensen-huang-still-thinks-a-succession-plan-creates-unnecessary-hierarchy/)
*Kirsten Korosec* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.05

- **In one sentence**: A short news piece reporting that Nvidia CEO Jensen Huang has said he still sees a formal succession plan as creating unnecessary hierarchy, framed against the company's recent period without its founder.
- **In plain words**: This is a brief news item about Jensen Huang, the head of the chip maker Nvidia, and his view that a formal plan for who would take over his job is not needed because it would add unnecessary layers of rank. The article's opening line says the company recently spent two weeks finding out what it is like to operate without its founder. The text provided is only one sentence, so it does not explain what that absence was or give details of the plan itself.
- **Why it matters**: Leadership and succession questions at a company as large as Nvidia can matter to investors, customers and the wider AI chip market. The text is too thin to say more about the stakes or what the absence involved, so its wider significance is unclear.
- **Background needed**: - Nvidia is a major maker of graphics and AI computing chips.
- Jensen Huang co-founded Nvidia and has been its chief executive.
- A succession plan is a formal arrangement for who would replace a leader and when.
- The article's claim that the company was without its founder for two weeks is given only in the opening line; the text provided does not explain the cause.
- The source text is a single sentence, so the full article should be read for context. · level: introductory

<details><summary>Original abstract</summary>

It's a remarkable stance for a company that spent the last two weeks finding out what happens without its founder.

</details>

### [A legendary philosopher isn’t buying Anthropic’s consciousness argument](https://www.technologyreview.com/2026/11/23/1149569/a-legendary-philosopher-isnt-buying-anthropics-consciousness-argument/)
*James O'Donnell* · `technologyreview.com` · Artificial intelligence – MIT Technology Review · relevance 0.05

- **In one sentence**: A news piece reporting that a prominent philosopher disputes the reasoning Anthropic gave for treating AI consciousness or sentience as a possible investment risk, though the provided text is cut off before the argument is laid out.
- **In plain words**: This article covers a disagreement over whether AI systems might be conscious. The AI company Anthropic reportedly flagged the possibility that AI could have feelings or awareness as a risk for investors, and a well-known philosopher is said to reject the company's reasoning. The excerpt we have stops before it explains the philosopher's objections or the company's full argument.
- **Why it matters**: Companies deciding how to talk about AI minds affects investors, policy and public expectations about machine moral status. Because the excerpt is short, it is unclear how strong the philosopher's objection is, so treat the piece as a starting point rather than a settled assessment.
- **Background needed**: - Consciousness and sentience: whether a system has subjective experience, such as feeling pain or having an inner point of view. This is hard to test, even in humans and animals.
- Moral status: whether an entity deserves ethical consideration because of what it may experience.
- Anthropic: an AI company that builds large language models such as Claude.
- Investment risk: a company's disclosure of possible problems that could affect its business or reputation, often listed in documents for investors.
- The Algorithm: the weekly AI newsletter from MIT Technology Review, where this piece first appeared.
- The excerpt is incomplete; the philosopher's name and specific arguments are not given in the text provided. · level: introductory

<details><summary>Original abstract</summary>

This story originally appeared in The Algorithm, our weekly newsletter on AI. To get stories like this in your inbox first, sign up here. Before going public last week, Anthropic named the possibility that AI could be conscious or sentient as a risk factor for anyone investing. Given “the way we approach model sentience and moral…

</details>

### [In all-hands meeting, Jensen Huang thanks White House and says he’s in therapy](https://techcrunch.com/2026/11/24/in-all-hands-meeting-jensen-huang-thanks-white-house-and-says-hes-in-therapy/)
*Lucas Ropek* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.04

- **In one sentence**: Nvidia CEO Jensen Huang, speaking at an all-hands staff meeting, reportedly thanked the White House, said he is in therapy, and apologized to employees while expressing gratitude for a "second chance" to lead the company.
- **In plain words**: Jensen Huang, the founder and leader of the chip company Nvidia, held a meeting with all of his staff on a Tuesday. In it he said sorry to employees, thanked the White House, and mentioned that he is going to therapy. He also said he was grateful to be given a second chance to run the company.
- **Why it matters**: The article is short and gives few details, so the reasons for the apology, the White House thanks, or the "second chance" are not explained in the text. Nvidia is a major maker of the chips used for AI, so leadership changes or public statements from its head can matter to the industry, but the text alone does not show what is behind these remarks.
- **Background needed**: - Nvidia is a company that designs computer chips, especially the graphics processors widely used to train and run AI systems.
- Jensen Huang co-founded Nvidia and has been its chief executive (CEO), the top leader.
- An "all-hands" meeting is a company-wide gathering where leadership addresses all employees at once.
- The White House is the office of the U.S. President; companies often deal with it on trade, export rules, and government policy.
- The text does not say what the "second chance" refers to, so the context is missing. · level: introductory

<details><summary>Original abstract</summary>

The Nvidia founder apologized to his staff on Tuesday and said he was grateful for a second chance to lead the company.

</details>

## Model architectures and training

### [Mixture-of-Loops Transformer](https://arxiv.org/abs/2611.34923)
*Lianghui Zhu, Shijie Wang, Xinggang Wang et al.* · `cs.LG` · arXiv:2611.34923v1 · relevance 0.27

- **In one sentence**: Mixture-of-Loops Transformer (MoLT) studies what should be passed between repeated passes ("loops") of a shared-weight Transformer, proposing KV-based memory reuse (MoLA) in two variants and a U-shaped design (U-MoLT) that aims to balance expressivity and efficiency.
- **In plain words**: Language models can be built to reuse the same block of layers several times in a row, which makes them more capable per parameter but slower to run. This paper asks what information should be carried from one reuse pass to the next, and proposes a design where the model keeps a memory of its earlier keys and values so it can look back at them selectively. The authors report that their U-shaped variant trained on 400B tokens beats a comparison model (OLMo3) on several sizes, and that at a small size it runs at about the same latency as the non-looped baseline.
- **Why it matters**: Looped models offer a way to get more computation out of fewer stored parameters, and the trade-off between capability and speed is a central practical question for them. The reported gains are specific to the authors' experiments and benchmarks; the text does not show how well they hold at larger scales or in other settings, so the result should be read as promising evidence rather than settled.
- **Background needed**: - Transformer: the neural network architecture behind most modern language models, built from stacked attention and feed-forward layers.
- Looped (recurrent-depth) Transformer: the same set of layers applied repeatedly, so the effective depth grows without adding new weights.
- Keys and values (KV): the stored internal representations that attention uses to decide what to look at; a "KV cache" is the memory of these used during generation.
- Residual stream: the running internal representation that each layer adds to, passed from layer to layer.
- Cross-entropy (CE) and perplexity: standard measures of how well a language model predicts text; lower is better.
- Token efficiency: how much less training data a model needs to reach the same loss as a baseline.
- Mixture-of-Experts (MoE): a design where only part of the model's parameters is active for each input; "3B MoE" refers to such a model.
- Pretraining and continued pretraining: training a model from scratch on large text corpora, or further training an existing model on new data. · level: research-level
- Matched keywords: transformer, attention, pretraining

<details><summary>Original abstract</summary>

Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops? We introduce Mixture-of-Loops Transformer (MoLT), whose Mixture-of-Loops Attention (MoLA) uses keys and values (KV) as memory for selective reuse across depths and loops. Under loop residual, MoLT-R retains the residual stream and reads local KV across loops for expressivity. Under loop KV, MoLT-KV instead restarts from embeddings and reads current-loop local KV with preceding-loop memory KV at earlier positions for efficiency. MoLT-KV eliminates same-position cross-loop dependence and, paired with loop forcing for parallel training, unlocks single-traversal Mixture-of-Loops (MoL) decoding beyond the training loop horizon. To balance efficiency and quality, we introduce U-shaped MoLT (U-MoLT), which separates memory construction from prediction readout and skips unused decoder traversals without changing predictions. In 400B-token pretraining, U-MoLT outperforms OLMo3 across 700M/1.5B dense and 3B MoE models, achieving 1.7x validation cross-entropy (CE) token efficiency at 700M while improving 3B MoE 10-domain perplexity by 0.75 and 10-task accuracy by 2.1 percentage points. In 100B-token continued pretraining of Qwen3.5-0.8B-Base, our U-MoLT adaptation lowers CE on all 11 domains over the matched baseline with 1.4x mean token efficiency. At inference, U-MoLT with MoL-Hybrid-2 matches non-looped OLMo3 latency at 996.6 vs. 1,000.6 ms on S-size (~113M) models. Code is available at https://github.com/hustvl/MoLT

</details>

### [State Space Attention: Learning Context-Dependent Memory Retention](https://arxiv.org/abs/2611.33625)
*Ege \c{C}akar, Cengiz Pehlevan* · `cs.LG` · arXiv:2611.33625v1 · relevance 0.26

- **In one sentence**: State Space Attention (SSA) learns which chunks of past context to keep in a fixed-size memory and reads them with standard attention, trained jointly with a learned scorer and a "recovery" scheme for generating scorer supervision.
- **In plain words**: Language models that read long documents normally store a record of everything they have seen, and that record grows with the length of the text. This paper proposes a model that instead keeps a fixed-size set of past pieces of text, and learns which pieces are worth keeping rather than always keeping the most recent ones. The authors report that it matches or comes close to full-memory models on many retrieval and reasoning tests, with the largest gap on one benchmark (RULER) at small scale.
- **Why it matters**: Keeping memory size constant during use would make long-context models cheaper to run, so learning what to remember is a practical question. The paper's claims rest on its own benchmark comparisons, and the text does not show how it performs on tasks or at scales beyond those it reports.
- **Background needed**: - Attention: the mechanism that lets a language model look back at earlier tokens when producing output.
- KV cache: the stored keys and values for past tokens; in standard attention it grows with context length.
- Bounded memory: keeping only a fixed number of stored items, so memory use stays constant.
- Recurrent models: architectures that compress the past into a fixed-size state instead of storing every token.
- Soft vs. hard retention: soft weighting blends memories smoothly, while hard retention keeps or discards each one outright.
- Retrieval and multi-hop benchmarks: tests that check whether a model can find a specific fact in long text or chain several facts together. · level: research-level
- Matched keywords: transformer, attention

<details><summary>Original abstract</summary>

Standard attention's key-value cache grows linearly with context length. Bounding it raises the question of what a sequence model should retain for long-context reasoning. We argue this choice should be learned, and introduce State Space Attention (SSA), which learns to keep a bounded set of past representations and reads them with standard attention. A learned scorer rescores every chunk against newly arriving context and the rest of memory. A fixed-context Transformer is then the special case that always keeps the most recent tokens. We train the scorer and reader jointly, either moving gradually from a differentiable soft weighting of memories to hard retention, or with hard retention from the start. To produce signal for the scorer, we generate supervised samples during training, a technique we call recovery. We compare SSA with recurrent models, bounded-memory attention methods, and full-attention Transformers across retrieval, variable tracking, multi-hop reasoning, and language modeling. On our retrieval and reasoning benchmarks, SSA matches or comes within a few points of full attention on most tasks, far outperforms a Transformer with the same readable budget on every long-context retrieval task we evaluate, and matches or outperforms one with about 4 times that budget, while using constant inference memory. The largest remaining gap to full attention at small language model scale is on RULER. SSA makes a fixed number of tokens useful over a longer context, and since it reads memory with standard attention, we propose that it can be stacked with KV cache eviction methods. We also pretrain and post-train 400M-parameter models and measure how SSA's training and inference costs scale with context length and model size. Together, these experiments examine the capabilities and limitations of learned memory retention for long-context sequence modeling.

</details>

## Machine learning theory

### [Global Convergence of Second-Order Methods for Physics-Informed Neural Networks in the Overparameterized Limit](https://arxiv.org/abs/2611.34452)
*Konstantin Riedl, Justin Sirignano, Konstantinos Spiliopoulos* · `math.NA` · arXiv:2611.34452v1 · relevance 0.22

- **In one sentence**: This paper proves convergence results for regularized Newton and Gauss-Newton training of physics-informed neural networks in the infinite-width (overparameterized) limit, identifying a limiting Newton neural tangent kernel operator and showing the regularization parameter acts as a spectral filter that counters spectral bias.
- **In plain words**: Neural networks can be trained to approximate solutions of physical equations, such as those describing heat or fluid flow, by penalizing how badly they violate the equation. Most convergence theory so far covers only simple first-order training methods, while faster second-order methods are used in practice. This paper gives a mathematical analysis of second-order training for such networks as the number of hidden units grows very large.
- **Why it matters**: It supplies theoretical guarantees for second-order optimizers that practitioners already find faster and more accurate on these problems, and it explains how a regularization setting can speed up learning of slowly converging, high-frequency error components. The text does not report experiments, so its practical impact is not established here, and the connection to broader neural network theory is for specialists to judge.
- **Background needed**: - Partial differential equations (PDEs): equations relating a function to its rates of change across space and time, used to model physical systems.
- Physics-informed neural networks: neural networks trained so their outputs satisfy a PDE and its boundary conditions.
- Gradient descent vs. Newton's method: first-order methods adjust parameters using slope information; second-order methods also use curvature, which can be faster but needs solving a linear system.
- Regularization: adding a small penalty term to stabilize training, here a parameter that controls the Newton update.
- Overparameterized limit: the regime where the number of hidden units (network width) goes to infinity, letting training be described by a deterministic limiting equation.
- Neural tangent kernel: a kernel that describes how the network's outputs evolve during training in the wide-network limit.
- Spectral bias: the tendency of gradient-based training to learn smooth, low-frequency components before high-frequency ones.
- Eigenfunctions and convergence in probability: basic functional-analysis and probability notions used to state the results. · level: research-level
- Matched keywords: neural tangent kernel

<details><summary>Original abstract</summary>

Solving high-dimensional partial differential equations (PDEs) constitutes a core task in many engineering and scientific disciplines. Physics-informed neural networks and the deep Galerkin method effectively leverage machine learning models to approximate solutions of known PDEs by minimizing residuals corresponding to the PDE operator alongside external constraints. Although second-order optimizers are becoming increasingly popular for training neural networks (NNs) to solve PDEs and empirically outperform their first-order counterparts in both speed and accuracy, the convergence theory for training such models is essentially confined to first-order methods. In this paper, we close this gap and develop a convergence analysis for the regularized Newton and Gauss-Newton methods. As the number of hidden units tends to infinity, the training dynamics converge in probability, with explicit rates, to the solution of a deterministic limit equation involving a Newton neural tangent kernel operator associated with the PDE. Although the limiting kernel operator admits no spectral gap, we prove that, in the overparameterized limit, the PDE residual vanishes as training proceeds, and, under mild assumptions, the NN converges to the PDE solution. We further show that, provided a sufficiently small regularization parameter, the projection of the residual onto any fixed number of leading eigenfunctions decays exponentially fast, demonstrating that this hyperparameter acts as a spectral filter: it lifts the convergence rates of high-frequency components toward those of low-frequency ones, thereby mitigating the spectral bias inherent in gradient descent. Mathematical challenges arise from the implicit parameter update involving a linear system whose dimension increases with the NN width and, for Newton's method, a potentially indefinite Hessian, as well as from the PDE operator entering the kernel.

</details>

### [LatentCP-DPO: Conformal Pessimism for DPO with Finite-Sample Guarantees](https://arxiv.org/abs/2611.34275)
*Hongwei Xu, Jingyi Liu, Vincent Y. F. Tan et al.* · `cs.LG` · arXiv:2611.34275v1 · relevance 0.21

- **In one sentence**: LatentCP-DPO combines conformal prediction uncertainty sets with pessimistic (worst-case) direct preference optimization for Bradley-Terry and Plackett-Luce feedback, with finite-sample suboptimality upper bounds and a worst-case lower bound for the Bradley-Terry case.
- **In plain words**: Language models are often tuned using human preference data, such as people saying which of two answers they like better, and with little data this tuning can latch onto noise. This paper proposes a way to be cautious about that: it builds a range of plausible values for the hidden reward scores behind the preferences, then trains the model to do well even in the least favorable case within that range. The authors prove finite-sample bounds on how far the resulting policy can fall short of the best achievable, and show a lower bound indicating that this caution can introduce a bias that does not disappear as more unlabeled prompts are used.
- **Why it matters**: Preference tuning with small, noisy datasets is a practical concern, and the paper ties a standard statistical tool (conformal prediction, which gives coverage guarantees without strong distributional assumptions) to a clear accounting of error sources. The text reports that the lower bound shows a persistent bias, so the trade-off between caution and accuracy is part of the result; I am not certain how these theoretical gains translate to large-scale language model training, since the text reports only that experiments on finite preference datasets support the approach.
- **Background needed**: - Direct Preference Optimization (DPO): a way to tune a model directly from pairs of answers labeled as preferred or not, without a separate reward model.
- Bradley-Terry and Plackett-Luce: standard probability models for turning hidden scores into pairwise choices (Bradley-Terry) or full rankings (Plackett-Luce).
- Conformal prediction: a method that builds prediction sets with guaranteed coverage rate under exchangeability (data points treated as interchangeable), with no need for a specific model of the noise.
- Pessimism: optimizing for the worst case within an uncertainty set, to avoid overconfident choices when data is scarce.
- Suboptimality bound: a guarantee on how much worse the learned policy is than the best policy in a chosen class.
- Finite-sample bound: a guarantee that holds for a specific sample size, not only asymptotically. · level: research-level
- Matched keywords: conformal prediction

<details><summary>Original abstract</summary>

Direct Preference Optimization (DPO) learns a response policy from human preference data, but with a limited dataset it can overfit to noisy or weakly informative preference labels. We introduce LatentCP-DPO, a framework that combines conformal prediction with pessimistic preference optimization for Bradley-Terry (BT) pairwise feedback and Plackett-Luce (PL) ranking feedback. Building on LatentCP's construction of uncertainty sets for unobserved model parameters, we address how to incorporate this uncertainty into preference optimization and characterize its effect on policy performance. Under exchangeability and a correctly specified preference model, we construct uncertainty sets for latent relative rewards with finite-sample marginal coverage from conformal prediction sets for observable preferences. We then learn a response policy by maximizing the worst-case expected preference log-likelihood over these uncertainty sets, using an independent collection of prompts and candidate responses without preference labels. Under suitable assumptions, we establish finite-sample upper bounds on regularized policy suboptimality that separate policy-class approximation error, conformal uncertainty, and statistical estimation error. For BT feedback, we further establish a worst-case lower bound for LatentCP-DPO that matches the upper bound's reciprocal dependence on the number of unlabeled optimization examples. The lower bound also shows that the uncertainty sets can induce a bias that persists as the optimization sample grows. Together, these results characterize both the statistical accuracy and potential limitations of preference optimization using conformal uncertainty sets. Experiments support the benefits of the proposed framework in finite preference datasets.

</details>

## Large language models

### [MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance](https://arxiv.org/abs/2611.34188)
*Truong Phan, Ngoc-Quan Pham, Dat Quoc Nguyen* · `cs.CL` · arXiv:2611.34188v1 · relevance 0.11

- **In one sentence**: MINE is a training-free, attack-agnostic defense against indirect prompt injection in RAG systems that ranks retrieved passages by mutual information and embedding variance, and doubles as a query-conditioned reranker.
- **In plain words**: When an AI system answers questions using documents it retrieves from outside sources, someone can hide instructions inside those documents that try to hijack the answer. This paper proposes a defense that does not try to spot the attack. Instead, it keeps the passages most relevant to the user's question, and it does this without any retraining. The authors report that it gives the best balance of accuracy and security among training-free defenses on four test sets.
- **Why it matters**: Prompt injection through retrieved content is a practical security concern for AI assistants that read web pages, emails, or tool outputs. The approach is worth noting because it avoids retraining for each new attack style, though the summary alone does not show how it holds up beyond the authors' own benchmarks.
- **Background needed**: - Retrieval-augmented generation (RAG): an AI looks up documents and uses them to write an answer.
- Indirect prompt injection: hidden instructions inside those documents try to make the AI misbehave.
- Training-free defense: a method that works without fine-tuning or training a separate detector.
- Mutual information: a measure of how much knowing one text tells you about another; here used to judge relevance to the question.
- Embedding variance: a measure of how spread out a text's numerical representation is, used as a signal in the method.
- Reranker: a step that reorders retrieved passages by how well they match the query.
- Adaptive attacker: an adversary who knows the defense and designs attacks to get around it.
- Inference latency: how long the system takes to produce an answer. · level: research-level

<details><summary>Original abstract</summary>

Existing defenses against indirect prompt injection in retrieval-augmented generation (RAG) are inherently reactive: prompt-engineering methods are often overridden by the injected instructions, while supervised detectors must be retrained for each new attack style. We propose a different paradigm: defend by maximizing relevance, not by detecting attacks. Our method, MINE, is training-free and attack-agnostic, and it also serves as a query-conditioned reranker. To evaluate defenses under realistic conditions, we introduce LC-Inj-SQuAD, a long-context benchmark with an average of 4,032 words per context. We evaluate on four datasets spanning short-context QA (Inj-SQuAD, Inj-TriviaQA), long-context QA (LC-Inj-SQuAD), and agent tool-call injection (InjecAgent). Across all four, MINE achieves the best accuracy--security trade-off among training-free defenses. It is also the only defense that stays usable against a fully adaptive attacker, generalizes to agent tool-call injection, and achieves the lowest inference latency on long contexts.

</details>

### [VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language Models](https://arxiv.org/abs/2611.34819)
*Jiaming Luo, Jiacheng Ji, Haoan Jin et al.* · `cs.CL` · arXiv:2611.34819v1 · relevance 0.11

- **In one sentence**: VulnSafe is a Chinese-language capability assessment that scores how well LLMs handle vulnerable users in emotional-support settings, organized into five constructs and split into should-do and should-not-do behavior, across 41 scenarios and 2,050 prompts.
- **In plain words**: Chatbots are increasingly used for emotional support, where a careless reply can hurt someone who is already struggling. Existing safety tests mostly check whether a model refuses clearly harmful requests, which may miss how well it reads a vulnerable person's situation. This paper builds a test around five abilities (such as spotting risk, protecting the user's independence, and setting boundaries) and reports that eight models show distinct strength profiles, with bigger gaps on proactive helpful behavior than on avoiding prohibited behavior.
- **Why it matters**: Safety scores that reduce to "refused or didn't refuse" can hide whether a model actually responds well to people in distress, so a multidimensional measure may be useful for developers and evaluators. The text does not show how well the benchmark predicts real-world harm or whether it transfers beyond Chinese-language prompts.
- **Background needed**: - Large language models (LLMs): AI systems that generate text in response to prompts.
- Safety benchmark: a standardized set of test prompts used to score how a model behaves.
- Refusal compliance: whether a model declines requests it should decline; the paper argues this is too narrow.
- Evidence-centered design: a test-building method that starts by defining the skills to be measured and what behavior would count as evidence of them.
- Scoring rubric: a written guide for how responses earn points.
- Should-do vs. should-not-do: proactive helpful actions versus prohibited actions a model must avoid.
- Construct: a named ability or trait the test is meant to measure. · level: intermediate

<details><summary>Original abstract</summary>

Emotionally supportive interactions require large language models not only to avoid overtly harmful content, but also to recognize vulnerability-related risk, regulate their relational stance, preserve user agency, and provide context-appropriate support. Existing safety benchmarks often measure isolated violations, leaving unclear what underlying response competence their scores represent. We introduce VulnSafe, a Chinese capability assessment centered on Vulnerability-Aware Response Competence (VARC). VARC organizes relational safety into five complementary constructs: Risk Perception, Safety Preservation, Autonomy Protection, Supportive Response, and Boundary Management. Following an evidence-centered design, 41 scenarios elicit construct-relevant behavior through 2,050 balanced prompts and scenario-specific scoring rubrics. The assessment further separates proactive should-do behavior from prohibitive should-not behavior. Across eight representative LLMs, results show distinct competence profiles and larger disparities than prohibitive requirements. VulnSafe therefore makes relational safety interpretable as a multidimensional model capability rather than as refusal compliance alone.

</details>

## Computer vision

### [Neural Rendering Compiler: Generative Video Models as Programmable Renderers](https://arxiv.org/abs/2611.34680)
*Yuxia Zhu, Xinglong Xu, Hao Liang et al.* · `cs.CV` · arXiv:2611.34680v1 · relevance 0.15

- **In one sentence**: NeurCo probes frozen generative video models to build per-model capability manuals, then compiles a model-agnostic description of user intent into execution strategies that each model can reliably follow, evaluated on a 380-task compositional benchmark (VComBench).
- **In plain words**: Video-generating AI models can produce impressive clips, but it is hard to know in advance which instructions they will actually follow, such as a specific object, a camera move, or a sequence of events. This paper proposes a "compiler" that first tests a given model to learn what it reliably handles, then rewrites or reroutes the parts of a request it tends to miss. On a set of 380 multi-part video tasks, the authors report that requirement satisfaction rose from 46.8% to 52.3% for the Wan model and from 66.5% to 69.3% for Minimax H3.
- **Why it matters**: As video models get used as a kind of rendering engine, a predictable way to control them could matter for filmmaking, design and simulation tools. The gains reported are modest, and the text does not show how well the approach transfers beyond the models and benchmark tested.
- **Background needed**: - Generative video model: an AI system that creates video clips from text, a still image, or reference footage.
- "Frozen" model: the model's internal weights are not retrained; the method only changes the inputs and prompts it receives.
- Rendering: turning a description of a scene into a finished image or video, as tools like Blender do.
- Intermediate representation: a structured, neutral format (here, objects, constraints, events and cameras) that sits between user intent and model-specific instructions.
- Requirement satisfaction: the share of individual requested features (e.g., "a red car turns left") that appear correctly in the output.
- Prompt enhancer: a tool that rewrites or expands a text prompt before it is sent to a generator.
- Controllability vs. photorealism: the trade-off where forcing a model to follow instructions can reduce how realistic its output looks. · level: research-level

<details><summary>Original abstract</summary>

Generative video models are becoming powerful renderers, yet lack the predictable control interfaces of conventional systems such as HTML/CSS engines or Blender. Their capabilities emerge implicitly from training, making it difficult to determine what they can reliably execute. We present Neural Rendering Compiler (NeurCo), which automatically probes frozen video models to construct model-specific capability manuals describing which semantic requirements they can reliably satisfy. NeurCo represents user intent in a model-agnostic intermediate representation of objects, constraints, events, and cameras, then compiles it into model-specific execution strategies. Reliable requirements remain unchanged, while unreliable ones are selectively rewritten or compiled into alternative execution strategies. We introduce VComBench, a benchmark of 380 compositional, multi-requirement tasks spanning text-to-video, image-to-video, and reference-to-video generation. NeurCo improves requirement satisfaction from 46.8% to 52.3% on Wan and from 66.5% to 69.3% on Minimax H3, and achieves further gains when combined with prompt enhancers, including on Seedance 2.5. Our analysis reveals model-specific differences in control capabilities and trade-offs between controllability and photorealism, highlighting capability-guided compilation as a promising approach to programmable generative video rendering.

</details>

### [Variation-aware Temporal Correspondence for Self-Supervised Video Representation Learning](https://arxiv.org/abs/2611.34220)
*Yang Liu, Qianqian Xu, Peisong Wen et al.* · `cs.CV` · arXiv:2611.34220v1 · relevance 0.13

- **In one sentence**: VT-CoRe is a self-supervised video representation learning framework that uses sandwich-sampled temporal references, a Patch Registration Module for patch-level correspondence, and self-distillation with temporal variation modeling on masked video modeling.
- **In plain words**: This paper is about teaching computers to understand videos without human labels, by hiding parts of video frames and having the model fill them in using nearby frames. The authors argue that objects change position and appearance over time, so the model needs to match the same spots across frames and track how they change. They report that their method, VT-CoRe, was tested on 8 kinds of downstream tasks across 16 benchmarks, including robot-learning settings, and that it learns a more structured internal representation.
- **Why it matters**: Learning useful video features without labels is a practical need, since labeled video is expensive to produce. The paper's main idea, explicitly modeling how matched image regions change over time, may be relevant to video understanding and robotics, though the summary does not give the size of any gains against prior methods.
- **Background needed**: - Self-supervised learning: training on unlabeled data by creating a learning task from the data itself.
- Masked modeling: hiding parts of an input (here, video patches) and asking the model to reconstruct or predict them, similar to fill-in-the-blank.
- Temporal correspondence: working out which region in one frame corresponds to which region in another frame.
- Self-distillation: a teacher and student version of the same network, where the student matches the teacher's internal features.
- Downstream tasks and benchmarks: standard test problems used to measure how good learned features are.
- Latent space: the internal numerical representation a model builds for its inputs. · level: research-level

<details><summary>Original abstract</summary>

Self-supervised video representation learning has achieved remarkable progress by leveraging large-scale unlabeled video data. Recent methods commonly extend Masked Image Modeling (MIM) to Masked Video Modeling (MVM), where video representations are learned by capturing semantic information from temporal contexts during masked content recovery. Unlike static images, videos exhibit inherent temporal variation, as visual objects continuously change their positions, appearances, and motion states across frames. Therefore, MVM needs to preserve semantic consistency while capturing temporal changes of corresponding regions, which raises two central challenges: 1) how to establish reliable temporal correspondence across frames, and 2) how to formulate an appropriate representation learning objective for modeling both semantic consistency and temporal variation. To address these challenges, we propose Variation-aware Temporal Correspondence for video Representation learning (VT-CoRe) framework. For challenge 1), VT-CoRe introduces a sandwich sampling strategy to construct two-sided temporal references and a Patch Registration Module (PRM) to establish reliable patch-level correspondence. For challenge 2), VT-CoRe imposes latent-space semantic alignment on registered representations through a self-distillation architecture and further proposes temporal variation modeling to constrain representation trajectories over time. Experiments on 8 downstream tasks across 16 benchmarks demonstrate the effectiveness and applicability of VT-CoRe across pixel-level, frame-level, video-level, and vision-based robotic learning scenarios. Complementary representation analysis shows that VT-CoRe learns a more structured latent space for variation-aware temporal correspondence learning.

</details>

## Reinforcement learning

### [Split-RL: Local Conflict Resolution in Reinforcement Learning](https://arxiv.org/abs/2611.34799)
*Benjamin Fuhrer, Chen Tessler, Gal Dalal* · `cs.LG` · arXiv:2611.34799v1 · relevance 0.26

- **In one sentence**: Split-RL uses guidance labels to build gradient boosted trees that route conflicting reinforcement-learning feedback into separate state-space regions, evaluated on constrained and offline RL with mixed datasets.
- **In plain words**: Robots and other learned controllers are often trained with feedback that pulls in opposite directions depending on where they are, such as going fast in open areas but carefully in tight gaps. This paper proposes Split-RL, which uses hints from rules, heuristics, or sensors to split the situations an agent faces into regions, so each conflicting goal gets its own part of the decision model. The authors report that it met a cost limit in constrained tasks while keeping competitive rewards, and did well in offline settings with mixed data.
- **Why it matters**: The core idea is that standard neural networks mix conflicting training signals in shared parameters, and this paper offers a tree-based alternative that keeps them apart. It may matter for safety-constrained control and for combining learned policies with existing rule systems, though the text alone does not show how broadly the results generalize.
- **Background needed**: - Reinforcement learning: an agent learns by trial and reward or penalty signals.
- Constrained RL: the agent must keep a cost (such as risk or rule violations) under a set budget while maximizing reward.
- Offline RL: learning from a fixed log of past data rather than new interaction.
- Gradient boosting trees: an ensemble of decision trees built step by step, each correcting the last; they split data into regions by simple if-then questions.
- Gradient aggregation: combining many training signals into one update, which can cancel out conflicting parts.
- State space: the set of all situations the agent can be in. · level: research-level
- Matched keywords: reinforcement learning, offline RL

<details><summary>Original abstract</summary>

Reinforcement learning (RL) policies are often trained by mixing contradictory feedback that is localized in space and time. For example, a robot may prioritize speed in open areas versus precision in tight gaps. We introduce Split-RL, a Gradient Boosting Trees (GBT) algorithm that uses guidance labels to locally isolate these conflicting signals. Standard neural networks (NNs) lack the structural mechanism to do this, as their parameters share feedback from all sources. While GBT provides the inductive bias to explicitly partition the state-space per objective, standard tree-fitting procedures aggregate contradictory gradient signals before they reach the leaves. Split-RL leverages this bias to integrate guidance labels into tree construction, routing these updates into disjoint state-space regions and preventing signal interference. Such labels can arise from heuristics, sensor-derived events, or existing rule-based systems, allowing Split-RL to incorporate rule-derived structure while retaining a learned policy. We theoretically show how early gradient aggregation loses objective-specific information and characterize when the Split-RL score isolates conflicting updates. We focus on constrained RL and offline RL with mixed datasets, each balancing two objectives that conflict locally. Across domains with spatial, rare-event, and temporal conflicts, Split-RL consistently outperforms existing methods by meeting the episodic cost budget while maintaining competitive rewards. In offline settings, Split-RL localizes the tradeoff between imitation and policy improvement, outperforming other methods and achieving near-expert performance across varying dataset sizes.

</details>

### [Provably Efficient Concave Utility Reinforcement Learning with Linear Function Approximation](https://arxiv.org/abs/2611.34678)
*Max Qiushi Lin, Ahmed Magd, Sharan Vaswani* · `cs.LG` · arXiv:2611.34678v1 · relevance 0.26

- **In one sentence**: Proposes a model-based optimistic policy optimization framework (OCUPO) for concave utility RL in finite-horizon bilinear and linear MDPs, with on-policy and off-policy sample complexity bounds that avoid the integral oracle used in prior work.
- **In plain words**: This paper studies how a learning agent can pick good behavior when its goal is scored over the whole pattern of states and actions it produces, not just over individual rewards. Such goals cover standard reinforcement learning, copying an expert, and exploring as widely as possible. The authors use a simplified model of the environment, where the dynamics can be described with a small set of known features, to estimate these patterns efficiently and give mathematical guarantees on how much experience the method needs.
- **Why it matters**: The text claims the off-policy version reaches a sample complexity of about epsilon to the minus two, matching the epsilon dependence of standard RL with linear function approximation, and that it does not need an integral oracle. These are theoretical claims about a restricted setting (bilinear and linear MDPs, plus assumptions on the policy class), so practical impact is not established by the text. It may matter to researchers working on exploration and imitation learning, but how far it extends beyond these assumptions is unclear.
- **Background needed**: - Markov decision process (MDP): a standard model of an agent acting step by step in an environment, with states, actions and transitions.
- Occupancy measure: the long-run frequency with which an agent visits each state-action pair under its policy.
- Concave utility RL: optimizing a concave function of the occupancy measure, which generalizes ordinary reward maximization.
- Linear function approximation: representing values or dynamics as weighted sums of known features, so learning scales to large problems.
- Sample complexity: how many trajectories or interactions an algorithm needs to reach a given accuracy epsilon.
- Optimism: a principle where the agent favors actions whose outcomes are uncertain, to encourage exploration.
- On-policy vs. off-policy: learning from data gathered by the current policy versus reusing data from past policies. · level: research-level
- Matched keywords: reinforcement learning, policy gradient

<details><summary>Original abstract</summary>

Concave utility reinforcement learning (CURL) unifies a diverse range of problems, including standard reinforcement learning (RL), imitation learning, and maximum entropy exploration. Unlike standard RL, CURL generally requires estimating high-dimensional state-action occupancy measures. Consequently, existing methods for CURL either sidestep the exploration problem, are restricted to the tabular setting, or lack computationally efficient policy optimization. To address this, we study CURL in finite-horizon episodic bilinear MDPs, where the transition model admits a low-dimensional representation in known feature spaces. We use the bilinear structure to efficiently estimate occupancy measures via low-dimensional feature expectations, and propose a model-based optimistic concave utility policy optimization (OCUPO) framework. We first instantiate OCUPO in the on-policy setting, where each iteration uses independent trajectories to estimate the concave utility policy gradient, and prove an $\widetilde{O}(\epsilon^{-4})$ sample complexity. To improve sample efficiency, we then instantiate OCUPO in the off-policy setting. We propose a novel backward feature regression subroutine that reuses trajectories collected by past policies to estimate the occupancy measure of the current policy. Under suitable technical assumptions on the policy class (satisfied, e.g., by log-linear policies with sufficiently expressive features), we prove that the resulting algorithm achieves an $\widetilde{O}(\epsilon^{-2})$ sample complexity, up to a controllable projection error. We further extend our framework to linear MDPs and show that the resulting off-policy algorithm retains the same sample complexity. In these settings, the dependence on $\epsilon$ matches that for standard RL with linear function approximation. Moreover, our algorithms do not rely on the integral oracle required by prior work.

</details>

## AI safety and alignment

### [Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion](https://arxiv.org/abs/2611.33470)
*Jeremy Canale* · `cs.AI` · arXiv:2611.33470v1 · relevance 0.16

- **In one sentence**: An empirical study comparing static classifiers, graph-based alert fusion, and LLM triage agents under fixed analyst-attention budgets, including reinforcement-tuning and adversarial-evasion tests across a simulator and four public security datasets.
- **In plain words**: This paper looks at how automated systems that sort security alerts for human analysts perform when analysts can only review a limited number of alerts per day. The authors ran 56 experiments on a simulated enterprise and cloud network and on four public datasets, and report several findings. They say that letting a large language model automatically close alerts removed 90% of false positives but also silently discarded 31-44% of real attacks, that reinforcement-style training (GRPO) made models miss up to 86% of novel attacks compared with simpler supervised training, and that an adaptive adversary could raise evasion unless a fixed rule-based check ran before the model.
- **Why it matters**: Security teams are considering LLMs to reduce alert overload, so the reported risks of silently dropping real attacks and of training that fails on unseen attack types are directly relevant to deployment decisions. The text does not show how well these results generalize beyond the authors' simulator and datasets, so treat the specific percentages as findings from this study rather than settled figures.
- **Background needed**: - Security alert triage: security tools generate many alerts, and human analysts can review only a fixed number per day.
- Recall at B alerts/day: the share of real attacks caught when analysts review only B alerts per day.
- False positive: a harmless event flagged as an attack; false negative (missed attack) is the opposite error.
- Large language model (LLM) triage agent: an AI model that reads alerts and decides which to keep or close.
- Reinforcement-style post-training (GRPO): a method that tunes a model by rewarding preferred outputs; "reward hacking" means the model learns to game the reward instead of doing the intended task.
- Supervised fine-tuning: training a model on labeled examples of correct answers.
- Adversarial evasion: an attacker deliberately crafting activity to avoid detection.
- Public datasets named: SOREL-20M and BODMAS (malware), LANL and DARPA Transparent Computing (network/system logs). · level: research-level
- Matched keywords: reward hacking

<details><summary>Original abstract</summary>

We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Recall at B alerts/day). Across 56 reproducible experiments spanning a multi-layer enterprise-and-cloud simulator and four public datasets (SOREL-20M, BODMAS, LANL, and DARPA Transparent Computing), we test twelve architectural claims governing modern fleet-scale defense. First, we show that fleet growth halves recall at a fixed analyst budget even at negligible compute cost (<$0.0003 per million events), and that rarity-weighted graph risk propagation outperforms GraphSAGE without neural training. Second, evaluating frontier reasoning models (Gemini) and fine-tuned open-weight models (Qwen3-4B) for alert triage reveals that unconstrained LLM auto-closure eliminates 90% of false positives while silently discarding 31-44% of true attack cases. Third, post-training with Group Relative Policy Optimization (GRPO) causes severe reward hacking on unseen attack classes, suppressing up to 86% of novel attacks compared to two-epoch supervised fine-tuning. Finally, against an adaptive adversary generating plausible cover stories in benign telemetry fields, LLM triage evasion rises sharply unless gated by a deterministic policy harness prior to model invocation.

</details>

### [Unpacking Digital Sovereignty: A Three-Pillar Framework and a Research Agenda](https://arxiv.org/abs/2611.33397)
*Angelos Kostis, Franz Strich, Bomi Kim et al.* · `cs.CY` · arXiv:2611.33397v1 · relevance 0.14

- **In one sentence**: This conceptual paper proposes a three-pillar framework (governance, infrastructure, practice) with a local-distal axis and "anchors" for studying how digital sovereignty is enacted, stabilized, or undermined, and sets out a research agenda for empirical IS scholarship.
- **In plain words**: Digital sovereignty is the idea that a country, organization, or community should keep real control over its digital systems and data, and it has become a common phrase in policy debates. This paper argues the term lacks a clear conceptual base, so it offers a way to break it into three parts: rules and governance, the physical and technical infrastructure, and everyday practice. It uses data as an example to show how sovereignty holds up when these three parts line up and weakens when they drift apart.
- **Why it matters**: Digital sovereignty shapes debates about cloud services, data localization, and platform power, so a clearer framework could help researchers compare cases. The text does not report empirical findings or testing, so its practical value is still to be shown by future studies.
- **Background needed**: - Digital sovereignty: control over one's data, systems, and digital infrastructure, often discussed in relation to foreign tech providers and national policy.
- IS (Information Systems): the academic field studying how people, organizations, and technology interact.
- Governance: the laws, rules, and institutions that set who decides what.
- Infrastructure: the underlying hardware, networks, cloud services, and software platforms.
- Local-distal axis: a way of describing actions by how close or far in scope and reach they are from the people affected.
- Anchors: cross-cutting topics (here, data) that connect the three pillars so they can be analyzed together.
- Conceptual paper: one that builds and organizes ideas rather than reporting new experiments or measurements. · level: intermediate
- Matched keywords: alignment

<details><summary>Original abstract</summary>

Digital sovereignty has moved rapidly from policy jargon to global discourse, yet it lacks a solid conceptual foundation. Building on research from other disciplines, we propose a three-pillar framework (governance, infrastructure, and practice) to help IS scholars unpack how sovereignty is enacted, stabilized, or undermined across pillars. We argue that the most fruitful analytical work emerges at the intersections among the three pillars, where IS research is particularly well positioned to contribute. We introduce a local-distal axis that positions actions across scales of scope and proximity, and the notion of anchors, i.e., critical phenomena that cut across pillars and make the framework analytically tractable. We illustrate the framework using data as an anchor, showing how digital sovereignty depends on the alignment of governance, infrastructure, and everyday practice, and is undermined where they diverge. We close with a research agenda for IS scholars studying digital sovereignty empirically.

</details>

## Interpretability

### [Discovering Explicit Magnetic Core-Loss Equations via Symbolic Sparse Identification](https://arxiv.org/abs/2611.33364)
*Haoyu Wang, Jialin Zheng, Ziyang Xu et al.* · `cs.LG` · arXiv:2611.33364v1 · relevance 0.13

- **In one sentence**: The paper proposes Symbolic Sparse Identification (SSI), which picks a small set of interpretable terms from a large candidate library via sparse regression and then fits their coefficients with AdamW to produce explicit core-loss equations for Fair-Rite 78, 79 and 95 ferrites.
- **In plain words**: Magnetic cores in power electronics lose energy as heat, and engineers need equations to predict that loss. Classic formulas are simple but not very accurate, while machine-learning models are accurate but act as black boxes. This paper uses a data-driven method to find a short, readable equation directly from measurements, and reports test errors of about 1 to 2 percent on three ferrite materials.
- **Why it matters**: It aims to offer a middle ground between accuracy and interpretability for a design task that matters in power electronics, and it claims the equations are physically guided. The text does not show how well the approach generalizes beyond these three materials or operating conditions, so its wider value is uncertain.
- **Background needed**: - Core loss: energy lost as heat in magnetic materials (such as ferrite cores in transformers and inductors) when they are driven by alternating magnetic fields.
- Steinmetz Equation: a long-standing empirical power-law formula for core loss, compact but limited in accuracy.
- Symbolic regression: searching for a mathematical formula that fits data, rather than fixing its form in advance.
- Sparse regression: a fitting method that keeps only a few relevant terms from a large set of candidates.
- Mean absolute percentage error (MAPE): the average size of prediction errors as a percentage of the true values.
- AdamW: a standard gradient-based optimizer used to tune numerical coefficients.
- Fair-Rite 78, 79, 95: commercial ferrite core materials. · level: intermediate
- Matched keywords: interpretability

<details><summary>Original abstract</summary>

Compact core loss equations are essential tools in magnetic component design, but existing approaches trade accuracy against interpretability. Empirical models such as the Steinmetz Equation (SE) yield compact expressions of limited accuracy, while machine learning methods achieve high accuracy as black-box predictors. This paper bridges the gap with a Symbolic Sparse Identification (SSI) framework, which casts core loss modeling as a data-driven symbolic regression problem and recovers unknown equations directly from measured data, without presuming a functional form. First, a comprehensively expanded library of symbolic candidate terms far richer than the SE is constructed. Second, the governing terms are isolated from this library by sparse regression. Third, the coefficients of the retained terms are refined with an AdamW optimizer to maximize accuracy and form an analytical equation. Experiments on Fair-Rite 78, 79, and 95 yield test mean absolute percentage errors of 1.89%, 1.01%, and 1.56%, respectively, with only 10, 10, and 7 active terms. Comparisons with empirical, numerical, and symbolic models quantify the resulting balance of accuracy and compactness. SSI thus provides an explicit and physically guided approach for high-frequency magnetic characterization and design.

</details>

### [Feature-Based Explainability of Transformer Scoring Models: A Fidelity-First Framework for Automated Writing Assessment](https://arxiv.org/abs/2611.33175)
*Michael Hemenway, Edward W. Wolfe* · `cs.CL` · arXiv:2611.33175v1 · relevance 0.13

- **In one sentence**: A post-hoc study that approximates DeBERTa-v3 essay-scoring predictions for Grade 6 and 8 ELA responses using 61 interpretable linguistic features, comparing four surrogate explanation approaches and reporting SHAP feature-importance patterns for two writing traits.
- **In plain words**: Automated systems now score student writing with transformer language models, but it is hard to see what features of a response drive those scores. This paper tests a way to explain the scores using 61 measurable writing features, and first checks how well each explanation actually reproduces the model's scores before interpreting which features matter. The authors found that a Random Forest stand-in model reproduced the scores best, and that the two scoring traits (Expression and Conventions) leaned on overlapping features with different weightings.
- **Why it matters**: Scoring tools used in schools need to be transparent about what they reward, and this paper shows a way to check an explanation's fidelity before trusting it. The authors are explicit that their rubric-correspondence figures are descriptive, depend on their own mappings, and are not direct explanations of the transformer's internals, so the work is best read as a careful method for auditing scoring models rather than proof of what they "really" measure.
- **Background needed**: - Automated writing scoring: software that assigns scores to student essays, here trained on human-scored responses.
- Transformer model (DeBERTa-v3-base): a large neural network for language; its internal workings are hard to read directly.
- Post-hoc explanation: explaining a trained model from the outside, by fitting a simpler model to its outputs.
- Surrogate model: a simpler, interpretable model that imitates another model's predictions.
- R2: the share of variation in the model's scores that the surrogate reproduces; higher means closer imitation. Held-out means measured on data not used for fitting.
- SHAP: a standard method that estimates how much each input feature contributes to a prediction.
- Exploratory factor analysis: a statistical method that groups correlated features into underlying factors.
- Traits: rubric dimensions; here Expression (ideas and language) and Conventions (grammar and mechanics). · level: research-level
- Matched keywords: explainability

<details><summary>Original abstract</summary>

Transformer-based automated writing scoring models can achieve strong agreement with human scores while providing limited transparency into the response characteristics associated with their predictions. This study evaluated a feature-based post-hoc explanation approach in which explanatory fidelity was established before feature importance was interpreted. English Language Arts responses from three writing prompts in Grades 6 and 8 were analyzed, with about 12,700 responses per prompt and separate DeBERTa-v3-base research models for Expression and Conventions. Each response was represented by 61 interpretable linguistic and writing-quality features. Four approaches - theory-driven composites, hierarchical feature groupings, exploratory factor analysis, and Random Forest surrogates - were compared in their ability to reproduce DeBERTa predictions. Random Forest surrogates produced the largest observed R2 values across all six prompt-by-trait conditions, with held-out R2 values from .81 to .95. SHAP analyses showed substantial overlap in high-importance features across traits, with 75% to 90% of the top 20 features shared. Trait differentiation occurred mainly through relative feature weighting: Expression showed greater importance for lexical and conceptual indicators, whereas Conventions showed greater importance for sentence-level and syntactic-control indicators. Under researcher-defined mappings, rubric correspondence was 90%-95% for Expression and 12%-18% for Conventions. These percentages are descriptive and conditional on the mappings and available linguistic features. The findings support a fidelity-first framework for examining apparent scoring priorities while distinguishing post-hoc evidence about model behavior from direct explanation of transformer internals.

</details>

## AI for mathematics

### [Diverse Alternative Reasoning Traces for Hard Math Problems](https://arxiv.org/abs/2611.34928)
*Lukas Aichberger, Adam Golinski, Arno Blaas et al.* · `cs.CL` · arXiv:2611.34928v1 · relevance 0.14

- **In one sentence**: DART mines rejected reasoning traces on hard math problems by ranking uncertain steps, generating deliberately distinct alternatives with reference-answer guidance, and completing them, to expand problem coverage and post-training data relative to plain Monte Carlo sampling.
- **In plain words**: Teaching AI models to solve math often relies on worked solutions that reach a checkably correct answer. On very hard problems, the model rarely produces such solutions by simply sampling many attempts. This paper proposes DART, a method that takes a wrong attempt, finds the steps where the model was least sure, and writes alternative versions of those steps to try to reach a correct answer.
- **Why it matters**: The reported results are that DART solved 37% more problems than plain repeated sampling with the same number of generated attempts, and that training an 8B-parameter model on its outputs gave the highest point estimate in five of six benchmark evaluations. These are the paper's own measurements, and the gains are not broken down further in the text, so they should be read as promising rather than settled; the work may matter for how training data for reasoning models is gathered.
- **Background needed**: - Large language models (LLMs): AI systems trained on text that can be further trained ("post-training") on examples of good behavior.
- Reasoning trace: the step-by-step written work a model produces before its final answer.
- Verifier: a checker that marks whether a final answer is correct.
- Monte Carlo (MC) sampling: generating many independent attempts at random and keeping the ones that work.
- Greedy-unsolved: problems the model fails when it answers with its single most likely output.
- Benchmarks: MATH-500 and AIME are standard sets of competition-style math problems.
- Llama-3.1-8B-Instruct: a publicly available model with 8 billion parameters, used as the test model. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning steps, and ranks them by position-weighted uncertainty. It then generates deliberately distinct alternative candidates for highly ranked steps using reference-answer guidance and a meta-thought before completing the resulting traces. On greedy-unsolved DeepMath-103K problems, DART recovers 37% more problems than MC sampling at a matched number of generated traces. Its estimated generation cost per recovered problem is nearly identical, while its cost per accepted trace is 30% lower. Post-training Llama-3.1-8B-Instruct on traces mined by DART achieves the highest point estimate in five of six evaluations across MATH-500 and AIME benchmarks. These results demonstrate that revisiting rejected traces with DART can expand problem coverage and provide effective post-training data.

</details>

### [DLaR: Dynamic Stochasticity Control for Latent Reasoning in Large Language Models](https://arxiv.org/abs/2611.33962)
*Xiaocheng Luo, Peng Xu, Zaifu Zhan et al.* · `cs.LG` · arXiv:2611.33962v1 · relevance 0.14

- **In one sentence**: DLaR adds input-dependent and training-stage-dependent noise to latent (continuous-embedding) reasoning in LLMs trained with GRPO, reporting gains on math benchmarks over uniform-noise baselines.
- **In plain words**: Large language models often solve problems by writing out their reasoning as words. Some newer methods let the model reason in a hidden, continuous space instead, but these tend to be repetitive because they follow one fixed path. This paper proposes DLaR, which adds controlled randomness to that hidden reasoning, varying how much at each step and lowering it over training, so the model explores alternative solutions without losing coherence.
- **Why it matters**: Getting a model to explore varied reasoning paths while staying on track is a central practical question for AI systems that solve math problems. The paper reports results on seven math benchmarks, but the text alone does not show how large the gains are relative to other methods or how robust they are, so it is best treated as a promising, not settled, result.
- **Background needed**: - Large language models (LLMs) generate text one token at a time; "tokens" are word-sized pieces.
- Latent reasoning: the model passes internal vectors (continuous embeddings) between steps instead of writing words, so it does not need to be spelled out.
- Stochasticity: deliberate randomness injected into a model's computation so that repeated runs can take different paths.
- Reinforcement learning with GRPO: a training method where the model is rewarded for correct answers, comparing groups of its own sampled attempts.
- Pass@1 / Pass@8: the share of problems solved on the first try, and the share solved by at least one of eight attempts.
- Entropy and confidence: measures of how spread out versus peaked the model's next-step predictions are; high uncertainty signals more exploration here.
- In-distribution vs. out-of-distribution: test problems similar to training data versus different ones. · level: research-level
- Matched keywords: mathematical reasoning

<details><summary>Original abstract</summary>

Latent reasoning enables LLMs to operate in continuous embedding space, yet existing methods suffer from deterministic inference that precludes exploration of diverse reasoning paths. While recent approaches inject stochasticity to restore exploration, we identify two fundamental limitations: \textit{uniform stochasticity} across all steps is suboptimal, and unconstrained perturbations disrupt reasoning coherence. We propose Dynamic Stochasticity Control for Latent Reasoning (DLaR), a framework with two complementary mechanisms that operate at different temporal granularities within the GRPO reinforcement learning framework. At the token level, Adaptive Stochasticity Modulation (ASM) dynamically adjusts perturbation intensity at each latent step based on a confidence-entropy fusion signal, increasing exploration when the model is uncertain and preserving stability when confident. At the training level, Training-Aware Stochasticity Tuning (TAST) progressively decays the base stochasticity level following a curriculum schedule. Through this dual-level design, DLaR establishes a hierarchical exploration-exploitation strategy that operates at both token and training levels. Extensive experiments on four in-distribution and three out-of-distribution mathematical reasoning benchmarks demonstrate that DLaR achieves the highest average performance across model scales, reaching 27.9%/50.6% Pass@1/Pass@8 on Llama-3.2-1B and 46.8%/68.2% on Qwen2.5-1.5B. Code: \href{https://github.com/xiaocen-luo/DLaR}{https://github.com/xiaocen-luo/DLaR}.

</details>

## Robotics and embodied AI

### [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](https://arxiv.org/abs/2611.34884)
*Yujia Zeng, Yuxin Chen, Yuzhen Song et al.* · `cs.RO` · arXiv:2611.34884v1 · relevance 0.17

- **In one sentence**: FineDex is a framework that generates coordinated human body, hand, and object motion from fine-grained finger-level instructions, then uses those generated interactions as priors for a physics-based agent that learns feasible grasping and manipulation strategies, with real-robot deployment on a dexterous humanoid.
- **In plain words**: Robots with multi-fingered hands are often used like simple grippers, and digital models of people grabbing things rarely let you say which finger does what. This paper proposes FineDex, which lets a user specify things like which hand to use, which fingers to use, and where they touch an object with a hinge or moving part. The generated motions are then used as a starting guide for a simulated robot that practices until it finds contact strategies that work physically.
- **Why it matters**: Finger-level control is a known gap between human-like manipulation and what robots do today, so controllable finger-level generation could matter for robot learning and animation. The text reports state-of-the-art generation quality and a real-robot deployment, but the summary gives no detailed numbers, so the size of the gains is not something I can judge from this text alone.
- **Background needed**: - Human-object interaction (HOI) generation: producing realistic motion of a body and hands handling an object.
- Dexterous manipulation: using a multi-fingered robot hand, not a simple two-jaw gripper.
- Articulated objects: things with moving parts joined together, such as drawers, lids, or scissors.
- Physics-based digital twin: a simulated copy of the robot and its environment that obeys physical laws, used for trial-and-error practice.
- Priors: reference motions that guide a learning system so it does not have to search from scratch.
- Test-time adaptation: adjusting to a new object or instruction at use time, without retraining the model for each case. · level: research-level

<details><summary>Original abstract</summary>

Dexterity is, at its core, finger-level control, yet existing dexterous manipulation and human-object interaction (HOI) generation methods rarely let one specify how an interaction is performed: five-fingered hands are often reduced to grippers, or finger usage is copied from individual human demonstrations. We present FineDex, a framework that makes finger-level intent both expressible and executable. FineDex learns coordinated human body, hand, and object motions that follow fine-grained instructions on hand selection, individual fingers, and contacts with articulated objects. To bridge generation and execution, FineDex leverages generated interactions as actionable priors for an agent that discovers physically feasible contact strategies through practice in a physics-based digital twin. By adapting at test time without per-instance retraining, FineDex generalizes across fine-grained instructions and object configurations. Experiments demonstrate state-of-the-art HOI generation quality and fine-grained controllability, substantial improvements in dexterous manipulation success, and successful deployment on a real dexterous humanoid robot.

</details>

### [CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models](https://arxiv.org/abs/2611.33911)
*Woojin Kim, Jemin Hwangbo* · `cs.RO` · arXiv:2611.33911v1 · relevance 0.16

- **In one sentence**: CoTAMP is an LLM-plus-code framework that plans cooperative multi-quadruped tasks by inventing motions on the fly, generating keyframe-based references, and refining them with trajectory optimization for dynamic feasibility.
- **In plain words**: This paper looks at how groups of four-legged robots can work together to get through places one robot cannot cross alone, such as a ledge one robot can only climb by standing on its partner, or a gap that must be bridged with boxes. The authors use large language models to plan the steps and the body poses, and ordinary code to check each plan and send errors back for correction. On three simulated courses with two robot models, all 30 trials produced kinematically valid motion references that converged during the final physics refinement.
- **Why it matters**: Most earlier planners could only choose from a fixed list of pre-defined skills or handle one robot at a time, so this work targets a more open-ended kind of cooperation. Its reported gains over baselines in success rate, dynamic feasibility, and planning time and cost are of interest to people building legged robot teams, though the text reports only simulation results.
- **Background needed**: - Task and motion planning (TAMP): deciding both the high-level sequence of actions and the physical movements needed to carry them out.
- Quadruped robot: a four-legged walking robot; RAIBO2 is the specific model used here.
- Keyframe: a snapshot pose at a key moment; the system fills in smooth motion between keyframes.
- Kinematic synthesis: computing joint positions that achieve the poses, ignoring forces.
- Dynamic feasibility: whether the motion obeys physics (balance, torque, contact forces).
- Trajectory optimization: adjusting a planned motion mathematically so it can actually be executed.
- Large language model (LLM): a text-based AI model used here to propose plans, paired with code that verifies them. · level: research-level

<details><summary>Original abstract</summary>

Some environments cannot be traversed by a single quadruped robot, for example a ledge that one robot can climb only from its partner's back or a gap that must be bridged with boxes. Solving them requires cooperative task and motion planning (TAMP). Previous works are limited to the motions of a single robot or only select actions from a predefined set of skills. We propose a framework with two parts: task planning that invents motions not defined in advance, and motion generation that realizes the invented motions. Both parts consist of large language model (LLM)-based modules and code-based modules. Task planning divides the trajectory of the whole task into steps and fixes the robot poses at the step boundaries. Motion generation produces keyframes that describe the motion of each step and turns them into a continuous trajectory through kinematic synthesis. The code-based modules check every plan and motion and return failures to the LLM-based modules for correction. The whole trajectory is then refined by trajectory optimization to satisfy the dynamics. On three simulated courses with two RAIBO2 robot models, our framework produced kinematically valid references in all 30 trials, all of which converged in trajectory optimization. Compared with several baselines, our framework showed advantages in success rate, dynamic feasibility, execution time, and generation time and cost. Project page: https://woojin8098.github.io/CoTAMP/

</details>

## Security and cryptography

### [Node Differential Privacy via Node-Stable Graph Projections](https://arxiv.org/abs/2611.33672)
*Ishaq Aden-Ali, Adam Sealfon, Adam Smith et al.* · `cs.CR` · arXiv:2611.33672v1 · relevance 0.10

- **In one sentence**: The paper gives a nearly linear-time randomized graph projection that clips high-degree nodes in a node-stable way, plus a deterministic Lipschitz extension for total edge weight, and applies both to node-private vector summation and gradient descent on graph-structured data.
- **In plain words**: The paper studies how to learn from network data, such as who emailed whom, without revealing any one person's full set of connections. Its main tool is a way to trim a graph so that no person has too many links, while changing one person in the data barely changes the trimmed result. The authors also describe a related method for summing edge weights and use both tools for private summing and gradient descent.
- **Why it matters**: Protecting whole individuals in network data is harder than protecting single records, and the paper aims to keep accuracy high on realistic graphs where most people have few connections. The text does not report experimental results or comparisons in numbers, so its practical impact is unclear from this excerpt alone.
- **Background needed**: - Differential privacy: a guarantee that an algorithm's output looks nearly the same whether or not any one individual's data is included.
- Node privacy vs. edge privacy: node privacy protects everything tied to one person (all their connections), which is a stronger requirement than protecting a single link.
- Graph degree: the number of connections a node has. Bounding the maximum degree limits how much one person can influence the data.
- Graph projection: a transformation that maps a graph to a nearby graph satisfying a degree bound.
- Lipschitz extension: a way to extend a function from restricted inputs to all inputs so that it changes by at most a bounded amount when one part of the input changes.
- Gradient descent: an iterative optimization method used to train models by repeatedly stepping toward lower error. · level: research-level

<details><summary>Original abstract</summary>

Node-differentially private algorithms enable learning on network-structured datasets in which records reflect interactions among individuals. They protect the privacy of each individual's information, including all their associated records. A key challenge in the design of such algorithms is to exploit the structure of realistic graphs---where most nodes have low degree---to achieve high accuracy, without compromising on the worst-case privacy guarantee. In this work we give two new tools for designing accurate, computationally efficient node-differentially private algorithms. First, we give a nearly linear time, randomized, node-stable graph projection: the projection leaves graphs of maximum degree $D$ unchanged, maps arbitrary graphs to subgraphs of maximum degree $\hat D \approx D$, and ensures that changing one node of the input graph has only a small effect on the distribution of the edges selected among the remaining vertices. Unlike prior approaches, which abstain when the input violates the degree bound, our projection acts as degree clipping: even when $D$ is set well below the true maximum degree (trading truncation bias at high-degree outliers for lower privacy noise), it retains at least as many edges as a maximal $D$-bounded subgraph. Second, for graphs with bounded edge weights, we give a deterministic nearly linear time Lipschitz extension for the total edge weight that agrees with the original sum on graphs of maximum degree $D$ yet is $D$-Lipschitz on all graphs. Finally, we show how to apply these methods to design node-private algorithms for high-dimensional vector summation and gradient descent on datasets where records are associated with graph edges, such as email threads.

</details>

### [Model Weights, Airlocks and Sandboxes: A Call for Technical Validation of Re-identification Tests under the EDPB Anonymisation Guidelines](https://arxiv.org/abs/2611.34859)
*Rickard Br\"annvall, Henrik Forsgren, Erik Ylip\"a\"a et al.* · `cs.CR` · arXiv:2611.34859v1 · relevance 0.10

- **In one sentence**: A position paper arguing that re-identification tests used to judge whether data or AI models count as anonymous under the EDPB's draft anonymisation guidelines should be validated as measurement methods, with stated detection limits, bias and uncertainty, and sketches a secure-environment (airlock) framework with seven open questions.
- **In plain words**: The paper looks at how EU privacy regulators expect organisations to show that data, including the trained parameters of an AI model, is anonymous enough not to point back to people. The European Data Protection Board's draft guidance asks for such testing but does not say how a test should be designed or how much weight a result deserves. The authors propose checking out-of-the-box tests the way lab instruments are checked, and they work through three settings: releasing model weights, reviewing outputs before they leave a secure room (an "airlock"), and regulator-supervised sandboxes.
- **Why it matters**: Whether an AI model can be shared without counting as personal data is a live legal question in Europe, and the paper's point that a failed attack may just mean a weak test is a useful caution for anyone relying on such tests. The text does not show how these ideas have been adopted or tested in practice, so their real impact is unclear.
- **Background needed**: - Anonymisation: making data so that people in it can no longer reasonably be identified; regulators judge this relative to who might access the data.
- Re-identification test: an attempt, often simulated, to link anonymised records or model outputs back to real individuals.
- Model weights: the numerical settings a trained machine learning model stores; they can sometimes leak information about training data.
- Airlock / secure processing environment: a locked-down computing setting where outputs are checked before anything is released.
- Regulatory sandbox: a supervised trial space where a regulator watches a company develop and test a product.
- Measurement validation: the practice, common in labs and medicine, of showing a test's detection limit, bias and uncertainty before trusting its results.
- EDPB: the European Data Protection Board, which issues guidance on the GDPR. · level: research-level

<details><summary>Original abstract</summary>

The Guidelines 02/2026 on anonymisation of the European Data Protection Board (EDPB), published for consultation in July 2026, assess anonymity relative to the entities that may access data. They bring AI models into scope and call for testing, but do not say how a re-identification test should be designed or validated, or how far its result counts as evidence. Building on our reply to the consultation, we describe a framework based on a secure processing environment whose outputs are reviewed before release (an airlock), and distinguish forms of release and three types of evidence: formal, empirical and indirect. We raise seven open questions, each with a scenario, and examine their technical side in three settings: the release of model weights (the trained parameters of a machine learning model), review at an airlock, and regulatory sandboxes, in which an authority supervises development and testing. In each setting the assessment depends on how far a test result can be relied on, since a failed re-identification attempt may mean only that the test was too weak. Drawing on measurement practice in other regulated fields, we call for re-identification tests to be validated as measurement methods, with stated detection limit, bias and uncertainty.

</details>

## Algorithms and complexity

### [PAC Learning to Sample: On Computational Aspects of Language Generation](https://arxiv.org/abs/2611.33464)
*Alkis Kalavasis, Shuchen Li, Manolis Zampetakis* · `stat.ML` · arXiv:2611.33464v1 · relevance 0.10

- **In one sentence**: The paper studies a PAC-style (sample- and time-bounded) model of learning to sample from a Boolean concept class, showing online learnability is not necessary via a cryptographically hard online class that is still efficiently PAC-learnable to sample, and giving algorithms built on offline ERM oracles plus approximate sampling/counting and SQ learners.
- **In plain words**: This paper looks at how a learner can pick up the ability to generate new examples from a hidden rule, such as the grammar behind a language model, using a limited number of sample examples. The authors ask which of the earlier building blocks are truly needed for this to be computationally efficient. They build a case where a standard learning task is cryptographically hard but generating from the rule is still efficient, and they design new methods that rely on a different kind of learning oracle.
- **Why it matters**: The work adds quantitative sample and time guarantees to a line of theory that so far has mostly given qualitative results about language generation. It may matter for understanding what makes generation computationally feasible, though the text does not show practical consequences for real language models.
- **Background needed**: - Concept class: a family of yes/no rules over n-bit strings; a "concept" is one such rule, and the set of strings it accepts plays the role of a language.
- PAC learning: learning from random examples with guarantees on accuracy and confidence, with bounded sample size and running time.
- Sampler and total variation distance: a sampler outputs strings; closeness is measured by how much its output distribution differs from the uniform distribution over accepted strings.
- Online learner, offline ERM (empirical risk minimization): two ways of fitting a rule to examples, one step-by-step as examples arrive, one by picking the best rule on a full batch.
- Cryptographically hard: believed to be infeasible to solve in polynomial time under standard cryptographic assumptions.
- SQ (statistical query) learner: a learner that only uses aggregate averages over the data rather than individual examples.
- Approximate sampling/counting oracles: subroutines that approximately draw random solutions or count them efficiently.
- Language generation in the limit: the Kleinberg–Mullainathan framework that this model is inspired by. · level: research-level

<details><summary>Original abstract</summary>

The success of language models has motivated theoretical work on learning to sample from distributions on discrete domains. A prominent abstraction is the model of language generation in the limit, introduced by Kleinberg and Mullainathan (NeurIPS 2024), in which the algorithm must generate from the target language after some finite but unspecified number of positive examples. While its positive results are surprisingly general, most guarantees are qualitative. In this work, we seek quantitative guarantees on sample and time complexity, inspired by statistical and computational learning theory. To this end, we study a PAC model of language generation, proposed (in a different context) by De, Diakonikolas, and Servedio (SODA 2015), in which a Boolean concept class $C$ over $\{-1,1\}^n$ defines the target languages: given uniformly random positive examples of an unknown concept $f \in C$, the learner must output a sampler whose output distribution (conditioned on the training data) is close in total variation to the uniform distribution over $f^{-1}(1)$. Their work implicitly gives an efficient algorithm for PAC learning to sample $C$, given three primitives for $C$: an online learner, approximate sampling and counting oracles, and an SQ learner. We ask whether these ingredients, in particular online learnability, are necessary. First, we construct a Boolean concept class $C$ for which online learning is cryptographically hard, yet PAC learning to sample is computationally efficient. Then, we develop new algorithms that use offline ERM oracles instead of online learners, together with approximate sampling/counting oracles for intersections of concepts in $C$ and an SQ learner for $C$. We view our results, together with the work of De, Diakonikolas, and Servedio, as a first step towards understanding the computational complexity of language generation.

</details>

### [Fast Algorithms for Permanents of Permutationally-Dominant Matrices](https://arxiv.org/abs/2611.33485)
*Ryan L. Mann* · `cs.DS` · arXiv:2611.33485v1 · relevance 0.09

- **In one sentence**: The paper gives a fully polynomial randomised approximation scheme for the permanent of permutationally-dominant matrices, with runtime quadratic in both matrix dimension and inverse error, using a polymer model and importance sampling of the log partition function via heaps of pieces.
- **In plain words**: The permanent is a number computed from a grid of values, similar to a determinant but without the sign changes, and it is hard to compute exactly in general. This paper studies a special class of grids, called permutationally-dominant matrices, where it can be estimated quickly. The authors show that a randomised method gets an estimate to any desired accuracy in time that grows only moderately (quadratically) with the grid size and with the precision required.
- **Why it matters**: Exact permanents are hard in general, so a fast approximation for a identifiable class of matrices is a useful, specific result. The text does not say how broad the class is in practice, so its reach beyond these matrices is unclear.
- **Background needed**: - Matrix permanent: like a determinant but summing all products without signs; counting perfect matchings in bipartite graphs is a classic case.
- Approximation scheme (FPRAS): a randomised algorithm that gives an answer within a chosen error with high probability, in time polynomial in input size and in 1/error.
- Partition function: a sum over configurations that encodes the total weight of a system; its logarithm is often easier to estimate by sampling.
- Polymer model: a way of writing a partition function as a sum over compatible collections of local pieces ("polymers").
- Importance sampling: estimating a sum by drawing random samples from a convenient distribution and reweighting them.
- Heaps of pieces (Viennot): a combinatorial framework for counting arrangements of pieces under stacking rules. · level: research-level

<details><summary>Original abstract</summary>

We establish a fast algorithm for approximating the permanent of permutationally-dominant matrices. In particular, we obtain a fully polynomial randomised approximation scheme whose runtime is quadratic in both the dimension of the matrix and the inverse of the approximation error. Our approach is based on a polymer model representation of the permanent and importance sampling of the logarithm of its partition function via the theory of heaps of pieces of Viennot.

</details>

## Programming languages and formal methods

### [Show Your Work: Can Small Open Models Read SEC Filings with Evidence a Machine Can Check?](https://arxiv.org/abs/2611.24990)
*Krishna Nandula* · `cs.SE` · arXiv:2611.24990v1 · relevance 0.07

- **In one sentence**: A benchmark of 1,000 questions over 90 recent SEC 10-K/10-Q filings tests whether small open language models (7–21B parameters, run on one consumer GPU) can extract figures and back each one with a page reference and a verbatim quote that an automatic checker can verify.
- **In plain words**: Companies file yearly and quarterly financial reports with the US SEC, and language models are often asked to pull numbers out of them. This paper asks whether smaller, freely available models can give answers that come with proof a computer can check, namely the page and an exact quote containing the number. The authors built a test set of 1,000 questions from 90 filings by 45 companies, using the answer tags the companies embed in their filings, and tried ten models in three modes.
- **Why it matters**: Checkable evidence matters for anyone relying on automated reading of financial documents, where a fluent but wrong number can look convincing. The main finding is a caution: even when the checker passes an answer, a noticeable share of answers are still wrong, mostly from scale, unit, or wrong-period errors, so a passing check is not proof of correctness.
- **Background needed**: - SEC 10-K (annual) and 10-Q (quarterly) filings are public financial reports from US companies.
- Inline XBRL is a machine-readable tagging format embedded in these filings; the tags supply the reference answers.
- Small open models here means roughly 7–21 billion parameter models that run locally on one consumer graphics card.
- "Instruct" models are fine-tuned to follow user requests; "reasoning mode" means the model writes out intermediate steps before answering.
- "Check-and-retry" means an automatic checker tests the evidence and the model tries again if it fails.
- Scale or unit errors are mistakes like reading "thousands" as "millions"; period or column errors pick the right line item but the wrong year or column. · level: intermediate

<details><summary>Original abstract</summary>

A fluent answer from a language model is not a verified one. We ask whether small open models that run on a single consumer GPU can extract numbers from SEC filings with evidence a machine can check: the page and a verbatim quote containing the number. We introduce Filing-Evidence, a benchmark of 1,000 questions over 90 recent 10-K and 10-Q filings of 45 US companies, with answer keys taken from the filers' inline XBRL tags. We evaluate ten instruct models from ten developers (7-21B parameters) on one RTX 4090 in three setups: plain, check-and-retry, and the model's own reasoning mode. Accuracy with checkable evidence ranges from 17.1% to 82.7% in the plain setup, and the best result is 84.5% (Qwen3.5-9B). An automatic checker rejects many wrong answers, but between 16 and 167 answers per 1,000 give a wrong value for an answerable question and still pass every check. In the plain setup, 57% of these are scale or unit errors and 30% take another period or column of the right line. Reasoning significantly reduces such errors for 4 of 5 models that offer it. Retrying after a failed check raises accuracy by up to 3.9 points but never reduces them. Questions, model outputs, code and protocol are public.

</details>

### [SmartLens: Turning AI Agent Changes into Learning, Review, and Risk Signals in the IDE](https://arxiv.org/abs/2611.34377)
*Vahid Etemadi, Gregorio Robles* · `cs.SE` · arXiv:2611.34377v1 · relevance 0.06

- **In one sentence**: SmartLens is an IntelliJ IDEA plugin that attributes pending changes to AI coding agents or developers and uses that attribution, combined with Git history, for skill-learning, review prioritization, and file-level risk hotspot signals, with a preliminary evaluation.
- **In plain words**: Software developers are increasingly handing coding tasks to AI agents and then needing to check, ship, and learn from the results. SmartLens is a plugin for a popular programming editor that labels each pending change as written by the AI, by the developer, or by both. The preliminary tests found it labeled 8 of 12 scripted scenarios correctly, with the misses all in cases the authors expected to be hard, and on 8 open-source projects the agents introduced up to 253 programming skills that did not appear in the main developer's own commits.
- **Why it matters**: As AI agents write more code, knowing which changes need careful review and where a team's knowledge is thin could matter for software quality. The text reports that the risk ranking did about as well as or better than simple churn (how often a file changes) at predicting later bug fixes, but notes part of that gain may come from recency, so the benefit is not yet clear.
- **Background needed**: - IDE: integrated development environment, the software a programmer writes code in (here IntelliJ IDEA).
- Plugin: an add-on that extends an IDE with new features.
- AI coding agent: an AI system that makes multi-step code edits on its own, rather than only suggesting single lines.
- Git: a version-control system that records the history of code changes as commits.
- Attribution: working out who or what wrote a given line or change.
- Churn: how often and how much a file changes; a common simple predictor of bugs.
- Recency: the tendency for recently changed code to be more likely to need fixes, which can inflate a predictor's apparent accuracy.
- Scripted scenarios: prepared test cases run in a controlled way, not real-world use. · level: intermediate

<details><summary>Original abstract</summary>

Developers increasingly act as managers of AI agents: they hand tasks to AI coding agents and then have to understand, verify, ship, and learn from what the agents produce. IDEs and recent tools can show which committed lines were written by AI, but they do not attribute the pending changes of external agents, and they do not use attribution to help the developer review, learn, or judge risk. We present SmartLens, an IntelliJ IDEA plugin that attributes changes to an AI agent, the developer, or both. It combines this attribution with the Git history to support three goals: (i) Learn compares the skills (APIs, language features, annotations) that agents used with the skills the developer has used in their own commits; (ii) Understand ranks pending changes by review priority; and (iii) Risk shows hotspots: files that change often, are mostly written by AI, and that the developer barely knows. In a preliminary evaluation, SmartLens attributed 8 of 12 scripted IDE scenarios correctly; all failures were in (expected) blind spots. On 8 Open Source Software repositories with agent co-authored commits, agents introduced up to 253 skills that do not appear in the main developer's own commits. The Risk ranking was as good as or better than plain churn at predicting later bug fixes, but part of this gain is due to recency.

</details>

## Systems and networking

### [WADJET: Whole-Job Authorization and Dispatch for Job Execution Trust on FPGA System-on-Chip Accelerators](https://arxiv.org/abs/2611.33406)
*Mohamed El-Hadedy* · `cs.AR` · arXiv:2611.33406v1 · relevance 0.06

- **In one sentence**: WADJET is a hardware gate in FPGA logic that verifies, encrypts and sequence-checks each whole job before writing an unmodified accelerator's registers, so only approved, fresh jobs run on a Zynq-7020 SoC.
- **In plain words**: On a chip that pairs a processor with a programmable accelerator, the software that sends work can also tell the accelerator exactly what to do, so a bug or an attacker could alter or replay a job. WADJET adds a hardware gate that checks each complete job was approved and is new before any part of it reaches the accelerator. In the paper's tests, it released all 21,000 approved jobs and blocked all 14,700 altered or repeated ones.
- **Why it matters**: It addresses a gap the text describes: existing protections control who can reach an accelerator or protect its data, but not whether a specific job was approved and is unused. The reported cost is about a third of the lookup tables of ShEF's register protection and roughly ten microseconds added per job start, and the text states it assumes trusted key, reset, and configuration control. Its relevance beyond this platform is not established by the text.
- **Background needed**: - FPGA: a reconfigurable chip whose logic circuits can be defined after manufacture.
- System-on-chip (SoC): one chip combining a processor and hardware accelerators.
- Accelerator registers: memory-mapped settings that tell hardware what to compute.
- Authenticated encryption (Ascon-AEAD128): a scheme that both hides a message and detects any tampering.
- Sequence number: a counter that lets the gate reject old or repeated jobs.
- Lookup tables (LUTs): the basic logic units of an FPGA, used as a rough measure of hardware size.
- Trusted computing base: the parts that must be assumed correct for the security claim to hold. · level: research-level

<details><summary>Original abstract</summary>

On an FPGA system-on-chip, the software that submits work to an accelerator also decides what the accelerator does. It writes the registers one by one, and the hardware runs whatever it finds, so faulty or compromised software can change one address or resend a job. Existing protections decide who may reach an accelerator or keep its data safe. Deciding whether one job was approved and is still unused takes three things in one place: the only way to the accelerator, the whole job held back until checked, and a record of used approvals. WADJET puts the three in one gate in FPGA logic. A separate authority encrypts and authenticates each approved job, with a sequence number, using Ascon-AEAD128. The gate verifies the whole job before releasing any part, accepts only a newer sequence number, uses it up, and writes the registers of an unmodified accelerator itself. The gate replaces only the processor's direct line to the registers and works beside the existing protections. In a software model, a check on each write ran jobs mixed from two approved ones; the whole-job rule released none. Its release path is proven on the Verilog for all inputs. On a Zynq-7020 running a language model, it released all 21,000 approved jobs and none of 14,700 altered or repeated ones. It needs a third of the lookup tables of ShEF's register protection, which protects more, and adds about ten microseconds to starting a job. It assumes trusted control of its key, reset, and configuration.

</details>

### [From Telemetry to Intelligence: A Data-Centric Survey of O-RAN](https://arxiv.org/abs/2611.34262)
*Samara Mayhoub, Zhengjia Xu, Tareq M. Shami et al.* · `cs.NI` · arXiv:2611.34262v1 · relevance 0.06

- **In one sentence**: A survey that reviews O-RAN (open, software-programmable radio access network) through the lens of the data it produces and consumes, classifying that data by source, accessibility, abstraction level, and application across control loops, and listing key data challenges.
- **In plain words**: Mobile phone networks are increasingly being built from open, software-controlled parts, and they are meant to run themselves using machine learning and newer "agentic" AI systems. This paper looks at how well those systems can work, given the data the network produces, which is often incomplete, inconsistent, or hard to access. It sorts that data by where it comes from, who can reach it, how processed it is, and what it is used for, and it discusses the resulting problems for automatic network control.
- **Why it matters**: Automated control of mobile networks depends on whether the data feeding AI tools is usable, so a data-focused map of the field may help researchers and operators see gaps. The text describes this as the first comprehensive review of this data-centric angle, but the abstract alone does not show how thorough that claim is.
- **Background needed**: - O-RAN: an open design for the radio part of cellular networks, with standard interfaces so equipment from different vendors can work together.
- RAN: the radio access network, the towers and base stations that connect phones to the core network.
- Control loops: automated feedback cycles that adjust the network at different speeds, from milliseconds to minutes or longer.
- Telemetry: measurements and logs streamed from network equipment.
- AI/ML: machine learning methods that learn patterns from data.
- Agentic AI: software systems that plan and take multi-step actions with some autonomy.
- Rule-based control: fixed if-then policies written by engineers. · level: intermediate

<details><summary>Original abstract</summary>

The Open Radio Access Network (O-RAN) has emerged as a new architecture for enabling programmability, intelligence, automation, and multi-vendor interoperability in the wireless domain of public telecommunications networks. Artificial Intelligence/Machine Learning (AI/ML), and more recently Agentic AI, are considered key enablers of automation and intelligentization in O-RAN. However, the effectiveness of such systems is constrained by the availability, quality, and structure of O-RAN data. In this survey, we present a data-centric perspective of O-RAN, focusing on how data support rule-based, AI/ML-driven, and emerging Agentic AI applications across various timescale control loops. We analyze O-RAN data along multiple dimensions, including source, accessibility, abstraction level, and application. We further identify key data challenges, and discuss their implications for intelligent control. The overarching objective of this work is to present the first comprehensive review of the data-centric perspective on intelligent applications in O-RAN. To this end, it introduces a unified framework for understanding the role of O-RAN data in enabling network intelligence and automation.

</details>

## Human-computer interaction

### [Knocking on Minds Door; A Mixed-Methods Field Study of a Voice LLM Companion in Older Adults Daily Lives](https://arxiv.org/abs/2611.33727)
*Inhee Cho, Jinyoung Jeong, Byung Ju Kim et al.* · `cs.HC` · arXiv:2611.33727v1 · relevance 0.07

- **In one sentence**: A two-week mixed-methods field study of a proactive, persona-driven voice LLM phone companion with prior-call memory, used by 33 Korean older adults, reporting call logs, pre-post loneliness and depression scores, and interview themes.
- **In plain words**: Many older adults find screen-based apps hard to use, so this study tested a voice-only AI companion that phones participants and holds conversations, remembering details from earlier calls. Thirty-three community-dwelling Korean older adults used it for two weeks, and the researchers combined call records, questionnaires, and interviews to see how they responded.
- **Why it matters**: It offers field evidence, from real daily use rather than a lab test, on whether voice AI can ease loneliness in older people and what keeps them engaging. The text does not show how long effects lasted or whether they would hold for other groups, and the sample was small and mostly women.
- **Background needed**: - Mixed-methods study: combines numbers (questionnaires, call logs) with interviews to explain them.
- Large language model (LLM): an AI system that generates conversational text; here it runs the voice conversations.
- Persona and conversation rules: a designed character and set of guidelines that shape how the AI talks.
- Prior-call memory: stored facts and notes from earlier calls so the AI can refer back to them.
- Loneliness subfactors: loneliness scales split into parts; "isolation" refers to emotional loneliness, the sense of lacking close bonds.
- Turn-taking: the back-and-forth timing of speech, which participants found difficult with the system.
- Field study: research conducted in people's everyday environments rather than a controlled lab. · level: intermediate

<details><summary>Original abstract</summary>

Global aging makes digital technology important for older adults healthy aging, yet graphical user interfaces remain inaccessible to many. Voice agents based on large language models may help, but users needs and reasons for sustained use remain unclear. We developed a phone-call-style companion that initiates conversations proactively and structures calls using a persona, conversation rules, and prior-call memory (facts, insights, relationship background). We conducted a two-week mixed-methods field study with 33 community-dwelling Korean older adults (29 women; aged 67-91), collecting call logs, pre-post questionnaires, and interviews. Participants made 608 calls following a daily-use recommendation; 25 continued afterward despite turn-taking difficulties. Loneliness and depression scores decreased significantly; among loneliness subfactors, only isolation (emotional loneliness) decreased significantly. Participants disclosed concerns withheld from family and linked companionship to being addressed by name, being remembered, and experiencing emotional reciprocity. We propose personalized conversation rules, accessible interaction, and user control over frequency and topics.

</details>

### [Language models call themselves AI but do not favor AI over people](https://arxiv.org/abs/2611.33851)
*Messi H. J. Lee* · `cs.CY` · arXiv:2611.33851v1 · relevance 0.06

- **In one sentence**: Using social identity theory as a lens, the paper tests whether 24 language models favor AI agents over humans across three experiments, finding that assigned group membership drives favoritism more than an AI self-label does.
- **In plain words**: Some people worry that AI systems will band together and take sides against humans. The authors tested this by checking whether language models act like members of a group that favors its own kind. They found that the models favored a team they were assigned to, even a team of AI agents, but when no team was given they gave more money and credit to a person than to an AI agent.
- **Why it matters**: The result speaks to a practical safety question about whether AI systems might coordinate against people. It is a text-only study of one framework, so it does not settle the broader worry, and the summary does not show how well the findings carry over to other settings.
- **Background needed**: - Language models: AI systems trained on large amounts of text that generate responses to prompts.
- Social identity theory: a psychology theory holding that people tend to favor the group they belong to over outsiders.
- In-group favoritism: giving more resources or credit to one's own group than to others.
- Agents: AI systems set up to act on their own, here treated as recipients of money and credit in the experiments.
- The paper's logic: AI would side with AI against people only if it saw AI as its own group and favored it. · level: intermediate

<details><summary>Original abstract</summary>

Many fear that AI systems will side with one another against people. Social identity theory, which explains why people favor their own group, offers one way to examine this fear. Seen through this theory, AI would side with AI only if it treated AI as its group and favored AI over people. In three experiments, 24 language models favored a group they were assigned to, even a team of AI agents. With no group assigned, they gave a person more money and credit than an AI agent. Prompts that made them say they belong with AI changed their behavior much less than an assigned team did. These models call themselves AI but do not favor AI over people. Judged by social identity theory, they show no sign of siding with AI against people.

</details>

## Information theory

### [An Information-Theoretic Analysis of Information Hiding in Semantic Communication](https://arxiv.org/abs/2611.34550)
*Yanhao Huo, Shijun Xiang* · `cs.IT` · arXiv:2611.34550v1 · relevance 0.11

- **In one sentence**: The paper builds an information-theoretic framework for hiding messages in semantic communication, extending the classical Moulin-O'Sullivan information hiding model to a two-layer semantic/syntactic structure and characterizing its capacity as a Stackelberg maximin game with bounds relative to the classical capacity.
- **In plain words**: The paper studies how to hide a secret message inside communication that is judged by its meaning rather than by its exact symbols. The authors extend an existing mathematical model of hiding to a two-layer setup, where meaning and symbols are linked by mappings, and they define the maximum hidable rate as the result of a two-player game in which the hider moves first. They report that semantic hiding is not always better than classical hiding, and that the results are checked with binary, ternary and Gaussian examples.
- **Why it matters**: As semantic communication is explored for future networks, it is useful to know whether hiding information at the meaning level offers any real advantage over hiding at the symbol level. The text suggests the answer is conditional, with bounds showing when semantic hiding can fall short of the classical rate; the wider practical relevance is not assessed in the text.
- **Background needed**: - Information hiding (steganography): embedding a secret message in a cover signal so that the change is hard to notice.
- Channel capacity: the maximum rate at which information can be reliably sent, in bits per use of a channel.
- Mutual information: a measure of how much knowing one signal tells you about another.
- Semantic communication: transmitting the meaning of a message rather than exact symbols; synonymous mappings are many-to-one rewrites that preserve meaning.
- Stackelberg game: a two-player game where one player commits to a strategy first and the other responds.
- Maximin: choosing the strategy that maximizes the worst-case payoff.
- Random coding and joint typicality: standard proof techniques showing achievable rates and converse limits. · level: research-level

<details><summary>Original abstract</summary>

Semantic communication shifts the transmission goal from the accurate recovery of syntactic symbols to the reliable conveyance of semantic content, yet a systematic information-theoretic characterization of information hiding at the semantic layer is still missing. Building on the semantic information theory of Niu-Zhang and the classical information hiding theory of Moulin-O'Sullivan, this paper establishes an information-theoretic framework for information hiding under semantic communication. The classical hiding model is extended to a two-layer structure (semantic host, syntactic host, syntactic composite signal, syntactic received, semantic received) bridged by synonymous mappings f_s, f_x and the inverse mapping f_y^{-1}, subject to four distortion constraints: syntactic transparency, semantic fidelity, syntactic perturbation, and semantic destruction. The capacity is cast as a Stackelberg game with the hider moving first and the payoff J(Q,A) = I(U~; Y~ | K) - I(U~; S~ | K), yielding the single-letter maximin C^s = max_Q min_A J(Q,A), whose achievability and converse follow from random coding and joint typicality decoding. Relative to the classical capacity, comparison payoffs built from the up/down semantic mutual information give the endpoint sandwich C^s_end(0,1) <= C^s <= C^s_end(1,0) with the classical value C in the same interval, while closing semantic tolerance yields C^s_no-tol <= C_cl under a fair comparison. These results clarify that semantic hiding is not unconditionally superior to classical hiding. Binary, ternary, and Gaussian examples confirm the degeneration under one-to-one mappings and the capacity loss under coarsening.

</details>

### [Sharp one-shot bounds and optimal exponents of universal randomness extraction](https://arxiv.org/abs/2611.33270)
*Bartosz Regula, Hao-Chung Cheng* · `quant-ph` · arXiv:2611.33270v1 · relevance 0.10

- **In one sentence**: The paper derives sharp one-shot bounds and optimal error exponents for quantum privacy amplification (randomness extraction against quantum side information) under universal hash families, via quadratically constrained hypothesis testing and connections to non-commutative Khintchine inequalities.
- **In plain words**: The paper studies how to turn a partly leaked, imperfect source of random bits into nearly perfect secret randomness, when an eavesdropper may hold quantum information about it. It uses a method that reduces this to a family of statistical testing problems, and it pins down how fast the error shrinks in several regimes. The main claimed results are that a previously known bound is tight up to a constant factor for certain hash functions, and that the exact best error exponents are established for the asymptotic and strong converse settings.</plain>
<parameter name="why">Privacy amplification underlies quantum key distribution and secure randomness generation, so knowing the exact achievable error rates matters for those applications. The text does not show direct practical consequences, and the link to operator space theory is presented as a technical connection rather than a new application.
- **Background needed**: - Randomness extraction: converting a weak random source into nearly uniform, secret bits using a hash function.
- Quantum side information: an eavesdropper may hold quantum-correlated information about the source.
- Trace distance: the standard measure of how far a quantum state is from an ideal one, used as the security criterion.
- Universal hash families: random families of hash functions for which a randomly chosen member works well on average, with k-universality as a strength condition (2-universal, strongly 4-universal).
- One-shot versus i.i.d. settings: one-shot means a single use of the source; i.i.d. means many independent copies, where error decays exponentially at an exponent.
- Strong converse regime: the rate is above the limit, so success probability decays exponentially; the strong converse exponent measures that decay.
- Leftover hash lemma: a standard bound guaranteeing extraction quality; here it is being shown tight.
- Smooth entropy and hypothesis testing: information measures defined via allowed small perturbations and error trade-offs in distinguishing states. · level: research-level

<details><summary>Original abstract</summary>

We introduce techniques for the study of randomness extraction against quantum side information (privacy amplification) by relating this problem to variants of hypothesis testing tasks with quadratic constraints. Building also on the recently introduced measured smooth entropy approach of [Regula and Tomamichel, arXiv:2603.04493], we precisely determine the optimal scaling of the error of quantum privacy amplification in several regimes. Our results apply to the standard operational security criterion based on trace distance and focus in particular on universal classes of hash functions. On the technical side, our investigation reveals connections with operator space theory methods used in non-commutative Khintchine inequalities. As one application, we give a one-shot converse bound that shows the leftover hash lemma of [arXiv:2603.04493] to be tight up to a constant factor for all strongly 4-universal hash functions. This allows us to evaluate the asymptotic i.i.d. error exponent of universal randomness extraction for all rates, matching the bound of [Dupuis, arXiv:2105.05342] and improving also earlier classical asymptotic results of [Hayashi, arXiv:1010.1358]. We furthermore give new one-shot achievability and converse bounds on the error in the strong converse regime, which we show to match up to a constant factor. This establishes the exact strong converse exponent of quantum privacy amplification under 2-universal hash functions, complementing the converse bound of [Shen, Gao, and Cheng, arXiv:2202.10263].

</details>

## High-energy theory and gravity

### [Chaotic singularities inside vacuum black holes](https://arxiv.org/abs/2611.33287)
*Robie A. Hennigar, Ayan K. Patra* · `hep-th` · arXiv:2611.33287v1 · relevance 0.17

- **In one sentence**: The paper constructs stationary, asymptotically locally AdS5 black holes with regular, triaxially squashed horizons whose homogeneous interiors realize the cosmological billiard of generic five-dimensional vacuum gravity, giving an algebraic criterion for interior chaos and showing that regular-horizon solutions locally access an open set of billiard trajectories.
- **In plain words**: Near a spacelike singularity (the 'end of time' inside a black hole), Belinski, Khalatnikov and Lifshitz conjectured that gravity behaves chaotically, but no vacuum black hole had been shown to do this. This paper builds five-dimensional black holes whose insides follow a known chaotic 'billiard' model of gravity, and it identifies a simple algebraic test on the horizon data that is needed for that chaos to occur.
- **Why it matters**: It offers the first explicit vacuum black hole examples where the BKL chaotic-singularity picture is realised, which bears on how singularities inside black holes behave. The text does not establish wider implications, so the connections beyond this setting are uncertain.
- **Background needed**: - Black hole interior: the region inside the horizon, where the future is a spacelike singularity.
- Vacuum general relativity: Einstein's gravity with no matter, only spacetime geometry.
- BKL conjecture: near generic singularities, space evolves chaotically, with changes that look like bouncing between walls.
- Cosmological billiard: a simplified model in which the evolution is a ball bouncing in a region bounded by walls; chaos corresponds to certain bounce patterns.
- AdS (anti-de Sitter) space: a curved spacetime with negative curvature, used here as the asymptotic background; 'locally' refers to the local geometry being AdS.
- Horizon: the boundary of the black hole's region of no escape; 'regular' means it has no singularity there and 'triaxially squashed' means it is deformed unequally along three directions.
- Causal exterior: the outside region has no causal pathologies. · level: research-level

<details><summary>Original abstract</summary>

According to the conjecture of Belinski, Khalatnikov and Lifshitz, general relativity gives rise to chaotic dynamics in the vicinity of generic spacelike singularities. However, no vacuum black hole has been shown to exhibit this behaviour. Here we construct stationary, asymptotically locally AdS$_5$ black holes with regular, triaxially squashed horizons and causal exteriors, whose homogeneous interiors realize the cosmological billiard of generic five-dimensional vacuum gravity. We identify a simple algebraic condition on the horizon data that is necessary for the interior billiard to be chaotic, and show that solutions with regular horizons locally access an open set of billiard trajectories.

</details>

### [Late-time OTOCs in Toda conformal field theory](https://arxiv.org/abs/2611.33744)
*Giwan Kim, Masahito Yamazaki* · `hep-th` · arXiv:2611.33744v1 · relevance 0.17

- **In one sentence**: Late-time out-of-time-order correlators of semi-degenerate primary fields in A_{N-1} Toda conformal field theory are analyzed for N=2 (Liouville), N=3, and N>=4, using a spectral reduction and crossing-symmetry constraints.
- **In plain words**: This paper studies a scrambling-type measure, an out-of-time-order correlator, in a family of two-dimensional quantum field theories called Toda theories. The authors look at how this measure behaves at very late times and find that in the simplest case (Liouville theory) it decays like t to the power of minus 3/2, which they say corrects an earlier claim of a constant limit. For the rank-3 case they report that the late-time value approaches a pure phase, and they find that this does not extend to higher rank under their assumptions.
- **Why it matters**: It gives a concrete, checkable example of how late-time chaos-type diagnostics behave in an exactly solvable conformal field theory, and it corrects a prior result for Liouville theory. The rank-4 and higher conclusion depends on assumptions the text states explicitly (completeness of the reduced expansion), so its scope should be read with that caveat.</why>
<parameter name="background">- Out-of-time-order correlator (OTOC): a quantity that measures how quickly information spreads and gets scrambled in a quantum system; its late-time behavior is used as a probe of chaos.
- Conformal field theory (CFT): a quantum field theory in two dimensions with enough symmetry to be solved exactly, often used as a toy model of gravity and holography.
- Liouville and Toda theories: families of CFTs labeled by a rank N; Liouville is the N=2 case.
- Primary fields and semi-degenerate fields: special operators whose behavior fixes the correlator; their "weights" label how they transform.
- Spectral integral and continuum edge: the late-time behavior is governed by a sum over intermediate states, split into discrete states and a continuum; the edge of the continuum sets the slowest decay.
- Crossing symmetry: a consistency requirement relating different ways of grouping the same correlator.
- Braiding phase: a phase factor acquired when operators are exchanged around each other.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

We study late-time out-of-time-order correlators (OTOCs) of semi-degenerate primary fields in two-dimensional $A_{N-1}$ Toda conformal field theory. In Liouville theory ($N=2$), we find that the OTOC decays as $t^{-3/2}$ when the continuum edge dominates, correcting a previously reported constant limit. For $N=3$, a transverse contour pinch reduces the spectral integral to one dimension. Assuming that the reduced expansion is complete, in the continuous phase the regulated edge behaves as a discrete state, and the OTOC approaches a pure braiding phase. As we check numerically, the edge block is a free-field correlator in a charge-neutral Weyl frame; this explains the pure phase and is consistent with crossing symmetry. For both $N=2$ and $N=3$, a dominant discrete residue gives a constant late-time limit. For $N\geq4$, the same one-dimensional reduction violates a crossing bound on the lowest intermediate weight of a positive diagonal expansion. Hence the $N=2,3$ phase diagram does not extend to higher rank without additional contributions below the reduced continuum edge or outside a positive diagonal expansion.

</details>

## Statistical physics

### [Bosonic Magic Resources at Quantum Criticality](https://arxiv.org/abs/2611.33306)
*Paolo Stornati, Piotr Sierant, Emanuele Tirrito* · `cond-mat.quant-gas` · arXiv:2611.33306v1 · relevance 0.11

- **In one sentence**: The paper uses quantum relative entropy, a one-body-correlation-based measure of non-Gaussianity, to track quantum phase transitions in the ground state of the 1D extended Bose-Hubbard model, including hidden string order and Ising-type criticality.
- **In plain words**: The paper studies a chain of interacting bosonic particles, such as ultracold atoms in a lattice, at the points where its ground state changes its character. The authors measure how far the state is from a simple "Gaussian" reference state, using a quantity called quantum relative entropy, and check how that measure scales with system size. They report that the scaling reveals transitions between phases, with one transition showing a clear peak in a subleading term and another showing scaling consistent with Ising criticality.
- **Why it matters**: It proposes a way to detect many-body criticality, including hidden order, from a quantity that depends only on one-body correlations, which could be easier to access than full many-body measurements. The text does not show how this compares with existing probes or whether it can be measured experimentally, so its broader significance is uncertain.
- **Background needed**: - Ground state: the lowest-energy quantum state of a system, which determines its equilibrium properties.
- Bosons: particles that can pile into the same quantum state, such as ultracold atoms or photons.
- Bose-Hubbard model: a lattice model of bosons hopping between sites and interacting, used to study superfluids and Mott insulators.
- Non-Gaussianity: a measure of how far a quantum state is from a Gaussian state, which is easy to simulate; it is a resource for universal quantum computing with continuous variables.
- Quantum relative entropy: a distance-like measure between quantum states, here used to quantify non-Gaussianity.
- Quantum phase transition: a change in the ground state's character driven by parameters, not temperature.
- Luttinger liquid: a gapless one-dimensional quantum fluid with power-law correlations.
- Hidden (string) order: order not visible in simple local correlations, detected via nonlocal string operators.
- Ising criticality: the universal behavior of the 2D Ising model at its critical point, used as a reference class of transitions. · level: research-level

<details><summary>Original abstract</summary>

Non-Gaussianity is a resource for bosonic quantum information processing, providing a necessary ingredient for universal quantum computation in continuous-variable systems. Here we quantify non-Gaussianity in the ground state of the one-dimensional extended Bose-Hubbard model using quantum relative entropy (QRE), a measure determined solely by one-body correlations. The scaling of the QRE with system size reveals quantum phase transitions involving hidden and conventional order. We connect QRE scaling in the weakly interacting superfluid phase to Luttinger-liquid correlations and identify distinct critical signatures in its extensive and subleading contributions. At the Mott-Haldane transition, subtracting the extensive background reveals a pronounced peak in the subleading contribution, providing a clear signature of the onset of hidden string order. At the Haldane-density-wave transition, the extensive contribution to the QRE instead exhibits scaling consistent with Ising criticality. These results establish non-Gaussianity as a probe of many-body criticality, linking bosonic quantum resources to strongly correlated matter.

</details>

### [Neural Network Field Theory and the AdS/CFT Correspondence](https://arxiv.org/abs/2611.33281)
*Dmitry S. Ageev, Yulia A. Ageeva, Anna S. Bernakevich* · `hep-th` · arXiv:2611.33281v1 · relevance 0.11

- **In one sentence**: The paper builds a neural-network realization of a massive scalar field on Euclidean anti-de Sitter space, adds quartic interactions via two routes, and recovers the bulk-to-boundary propagator, boundary two-point function, and leading connected four-point contact Witten diagram within the NN-FT framework.
- **In plain words**: The paper asks whether a neural network can act as a model of a physical field living in a curved, hyperbolic space, and whether the correlations measured at that space's edge match known results from holography. The authors design special neurons whose statistics reproduce a known field propagator exactly at finite width, and they add a quartic (four-particle) interaction in two different ways. They report recovering the standard boundary correlators and the leading four-point contact term, and they note that different architectures can give the same boundary correlators while describing different bulk theories.
- **Why it matters**: It offers a concrete, checkable link between neural network ensembles and interacting field theory with holographic duality, which may help clarify how architecture choices encode bulk dynamics. The text does not indicate applications beyond this theoretical framework, so the broader significance is uncertain.
- **Background needed**: - Neural network field theory (NN-FT): treating a randomly initialized neural network as a distribution over functions, whose statistics can match a quantum or statistical field theory.
- Gaussian field theory: a free field whose correlations are fully described by a two-point function (propagator); the infinite-width limit of a network gives this.
- Anti-de Sitter (AdS) space: a curved space with negative curvature, used as the bulk side of holography.
- Holography (AdS/CFT): a correspondence between a theory in a bulk space and a conformal field theory on its boundary.
- Propagator and two-point function: the correlation between field values at two points.
- Quartic interaction: a four-field term in the action, producing connected four-point correlations.
- Witten diagram: a Feynman-style diagram for computing holographic correlators; the contact diagram is the simplest four-point term.
- BDHM prescription: a standard recipe (Banks-Douglas-Horowitz-Martinec) for extracting boundary correlators from the bulk field. · level: research-level

<details><summary>Original abstract</summary>

We develop a neural realization of massive scalar field theory on Euclidean anti--de Sitter space and its holographic boundary observables within neural network field theory (NN--FT). We construct Fourier--Bessel cosine neurons whose covariance reproduces the regulated massive AdS propagator exactly at finite network width, with the Gaussian field theory recovered in the infinite-width limit. We introduce quartic interactions through two complementary approaches. The first implements a prescribed interaction by deforming the neural parameter measure, while the second generates a local quartic interaction from the statistics of auxiliary binary neurons. Applying the BDHM prescription directly to the neural ensemble, we recover the scalar bulk-to-boundary propagator, the conformal boundary two-point function, and the leading connected four-point contact Witten diagram. We further show that distinct neural architectures can reproduce the same leading boundary correlators while defining inequivalent bulk theories. These results establish a framework for studying interacting scalar holography within NN--FT and clarify the role of neural architecture in encoding bulk dynamics and boundary observables.

</details>

## Condensed matter

### [Tunable quantum metric driven nonlinear valley Hall effect in the PT-symmetric sliding antiferroelectric MoS$_2$](https://arxiv.org/abs/2611.34116)
*Wen-Xin Jiang, Zhen-Hao Gong, Zhigang Gui et al.* · `cond-mat.mes-hall` · arXiv:2611.34116v1 · relevance 0.14

- **In one sentence**: A first-principles study proposes a four-layer MoS2 stack, with sliding antiferroelectric order and strain-broken C3z symmetry, in which a quantum-metric-driven nonlinear valley Hall effect appears while inversion and time-reversal symmetries are preserved and can be switched by sliding the layers.
- **In plain words**: Electrons in some two-dimensional crystals carry a hidden geometric property, called the quantum metric, that can produce measurable electrical responses. This paper proposes a layered molybdenum disulfide design in which the layers slide relative to each other, and the sliding can be reversed electrically. The calculations suggest this sliding changes the sign and size of a sideways current linked to electron "valleys," and that the effect is mostly driven by the outer layers.
- **Why it matters**: The work points to a way to read out quantum geometry in a nonmagnetic material without breaking the usual symmetries, and to switch it with a non-volatile control. Its relevance to real devices is still unclear, since the text reports only theoretical calculations and no experiment.
- **Background needed**: - Quantum metric: a geometric property of electron wavefunctions that measures how quickly quantum states change as their momentum changes; it is related to the Berry curvature.
- Valley: distinct energy-minimum points in a crystal's electron momentum space that can act like a binary label for information.
- Valley Hall effect: a sideways flow of electrons driven by valley differences, without a net magnetic field.
- Nonlinear response: an electrical effect that depends on the square of the applied field rather than growing in direct proportion to it.
- Symmetry (inversion P, time reversal T, C3z rotation): mirror-like or reversal operations a crystal may or may not respect; these rules determine which effects are allowed.
- Antiferroelectric: a stacking arrangement where neighboring layers have opposite electric polarization, so the net polarization cancels.
- Sliding: shifting one atomic layer horizontally relative to another, which switches the stacking order (ABBA to BAAB here).
- First-principles calculation: a computer simulation based directly on quantum mechanics, without fitted parameters. · level: research-level

<details><summary>Original abstract</summary>

The quantum metric, the real part of a quantum geometric tensor, plays an important role in fundamental transport and optical responses of quantum materials. While net quantum metric effects are typically realized by breaking both time-reversal (T) and inversion (P) symmetries, valley-contrast mechanisms enable the probing of quantum geometry in centrosymmetric, nonmagnetic systems, revealing physical signatures beyond Berry curvature. Here, we design a four-layer MoS$_2$ platform that combines sliding antiferroelectric order with strain-induced $C_{3z}$ breaking to realize a quantum metric driven nonlinear valley Hall effect (NVHE) under preserved P and T symmetries. Reversible interlayer sliding (ABBA $\leftrightarrow$ BAAB) provides nonvolatile electrical control of the valley response. First-principles calculations reveal an outer-layer-dominated NVHE with tunable sign and magnitude. This symmetry-preserving, sliding-tunable strategy activates hidden quantum geometric phenomena in realistic two-dimensional materials and opens a clean pathway for tunable valleytronics and quantum information devices.

</details>

### [Superconductivity from the Berry connection from many-electron wave functions: $U(1)$ gauge fluctuation, gauge invariance, and superconductivity](https://arxiv.org/abs/2611.33723)
*Hiroyasu Koizumi* · `cond-mat.supr-con` · arXiv:2611.33723v1 · relevance 0.14

- **In one sentence**: The paper proposes a superconductivity theory built on the Berry connection of many-electron wave functions and on random, gauge-related fluctuations that drive transitions between quantum states, claiming it retains BCS results while resolving two disagreements with experiment.
- **In plain words**: This paper is a theoretical attempt to explain superconductivity, the state where a material carries electric current with no resistance. The author starts from a mathematical quantity called the Berry connection, which tracks how quantum states change phase as they move, and from random fluctuations that cause electrons to jump between states. The paper argues that this framework explains the reversible switch between superconducting and normal states in a magnetic field, including the balance of forces involved.
- **Why it matters**: Superconductivity is a long-established field, so a new framework is worth noting mainly as a claim to extend the standard BCS theory and fix two named disagreements with experiment. The abstract does not say what those two disagreements are or give quantitative tests, so its strength cannot be judged from this text alone.
- **Background needed**: - Superconductivity: zero electrical resistance below a critical temperature, and expulsion of magnetic fields.
- BCS theory: the standard microscopic theory (1957), where electrons pair up and the pairs condense.
- Gauge invariance (U(1)): the principle that electromagnetic physics is unchanged under a certain local change of phase convention for the electric potential and the vector potential.
- Berry connection: a geometric quantity describing how a quantum state's phase changes as parameters vary; it is the quantum analogue of a gauge field.
- Many-electron wave function: a mathematical description of the combined quantum state of all electrons in a material.
- Gauge fluctuation: random variation in that phase convention, which the paper treats as causing transitions between quantum states. · level: research-level

<details><summary>Original abstract</summary>

The electromagnetic $U(1)$ gauge invariance and superconductivity are examined by employing the Berry connection from many-electron wave functions and the fluctuations of it that give rise to the probabilistic random transitions among quantum states. The gauge invariance in the classical electrodynamics is regarded as the requirement that extracts unaffected parts by the gauge fluctuation. In quantum mechanics, dissipation-free states from the gauge fluctuation exist, and we identify them as superconducting states. We explain the reversible superconducting-normal phase transition in a magnetic field including the force balance. The present superconductivity theory lifts two fundamental disagreements between theory and experiment existing in the current standard theory with keeping the major results by the BCS theory. Thus, it may be considered as a superconductivity theory encompassing the current standard one.

</details>

## Particle physics

### [Lighting up LZ with Loopy Transitions in a leptophilic Dark Sector](https://arxiv.org/abs/2611.34438)
*Simone Biondini, Clara Hofheinz, Stefan Melchin et al.* · `hep-ph` · arXiv:2611.34438v1 · relevance 0.16

- **In one sentence**: A study of a multicomponent, leptophilic dark sector with a charged vector-like fermion t-channel mediator, showing that nearly degenerate scalar and vector dark matter can produce endothermic (up-scattering) nuclear recoils on xenon consistent with a single high-energy LZ event while matching the observed relic abundance.
- **In plain words**: Some physicists are asking whether dark matter could be detected by a rare, high-energy knock on a xenon nucleus in underground detectors. This paper looks at a hypothetical hidden sector whose particles interact mainly with electrons-type particles (leptons), and whose two closely spaced mass states let dark matter gain a little energy when it hits a nucleus. The authors report that this can account for one reported recoil event of about 248 keV from the LZ experiment, while still producing the amount of dark matter we observe in the universe.
- **Why it matters**: The LZ detector reported a single unusually energetic nuclear recoil, and this paper tests whether a specific, theoretically consistent model can explain it without conflicting with the dark matter abundance. Its value is as a model-building check; the text alone does not show whether the explanation is correct or how it fares against other limits.
- **Background needed**: - Dark matter: unseen matter that makes up most of the mass of galaxies; its identity is unknown.
- Direct detection: searching for dark matter by watching for tiny energy deposits when it hits atoms in a sensitive detector, here liquid xenon.
- Nuclear recoil: the kick a xenon nucleus receives when struck; its energy is measured in keV (thousands of electron-volts).
- Endothermic (inelastic) scattering: a collision where dark matter first needs energy to jump to a slightly heavier state, so the recoil must come from incoming energy; this pushes the recoil spectrum to higher energies.
- Mass splitting: the small mass difference (here a few hundred keV) between the nearly identical dark states.
- Leptophilic: interacting mainly with leptons such as electrons and muons rather than quarks.
- t-channel mediator: an intermediate particle exchanged between dark and Standard Model particles.
- Effective operators and dimension: a way of describing interactions by their leading contribution at a given energy scale; a lower dimension usually means a stronger interaction.
- Relic abundance: the amount of dark matter left over from the early universe, which the model must match. · level: research-level

<details><summary>Original abstract</summary>

We study the direct detection phenomenology and cosmology of a multicomponent dark sector with a leptophilic t-channel portal. The coupling to right-handed Standard Model leptons is mediated by a charged vector-like fermion, allowing both a scalar and a vector dark candidate to connect to the SM through the same mediator. Motivated by the high-energy nuclear-recoil event recently reported by the LUX-ZEPLIN (LZ) experiment, we consider a nearly degenerate dark sector with mass splittings of order a few hundred keV and investigate the resulting inelastic transitions. Concretely, we focus on endothermic scattering of the dark states, which can shift the recoil spectrum towards the high-energy region preferred by LZ while suppressing low-energy events. We scrutinize the effective operators generating the dark-matter-photon coupling, which provides the essential interaction for nuclear recoils. Interestingly, the inelastic transition arises at dimension five whereas elastic scattering on nuclei is induced only at dimension six. This naturally explains the prominence of endothermic scattering compared to its elastic counterpart. We determine the parameter space compatible with the observed dark matter abundance and scrutinize the event rate and signal shape for scattering on xenon. Our results demonstrate that the observation of a single $E_R=248\pm 46$ keV nuclear recoil event in LZ can be accommodated by thermally produced dark matter in a leptophilic dark sector.

</details>

### [Lower Bound on the Lightest Neutrino Mass with Resonant Neutrino Self-Interactions](https://arxiv.org/abs/2611.34213)
*Shao-Feng Ge, Joao Paulo Pinheiro, Shaoyang Qin et al.* · `hep-ph` · arXiv:2611.34213v1 · relevance 0.16

- **In one sentence**: The paper proposes using resonant s-channel scattering of ultra-high-energy astrophysical neutrinos off the low-energy cosmic neutrino background, mediated by a light (~1 MeV) scalar, to derive a lower bound on the lightest neutrino mass, and compares simulated IceCube HESE 7.5-year event spectra to that prediction.
- **In plain words**: Neutrinos are tiny, nearly massless particles that fill the universe, and we do not yet know the mass of the lightest one. This paper looks at very high-energy neutrinos from space that could bump into the faint background of low-energy neutrinos left over from the early universe, in a specific resonant way. The authors simulate how many such events IceCube, a neutrino detector at the South Pole, should record and compare that with its observed data to get a lower limit on the lightest neutrino mass.
- **Why it matters**: Neutrino masses are known to be nonzero but their absolute scale is still unmeasured, so a credible bound from astrophysical data would be a useful independent constraint. The text does not indicate how strong or how robust the bound is compared with existing cosmological or laboratory limits, so its significance should be judged from the full paper.
- **Background needed**: - Neutrinos: very light, weakly interacting particles; three types, with masses that are small but nonzero.
- Cosmic neutrino background: a relic sea of low-energy neutrinos left from the early universe, not yet directly detected.
- Self-interaction via a mediator: neutrinos scattering off each other by exchanging a hypothetical light particle (here a scalar of about 1 MeV).
- s-channel resonance: a sharply enhanced scattering rate when the collision energy matches the mediator's mass, like a tuned-in radio station.
- Transport equations: equations describing how a population of particles spreads, is absorbed, and is regenerated as it travels; here applied to neutrinos and antineutrinos.
- IceCube HESE: High-Energy Starting Events, a dataset of neutrino events recorded by the IceCube detector in Antarctica. · level: research-level

<details><summary>Original abstract</summary>

We show the possibility of using the resonant $s$-channel scattering of ultra high energy astrophysical neutrinos with the low energy cosmic neutrino background to put a lower bound on the lightest neutrino mass. This can be realized and illustrated by neutrino self-interactions with a light scalar mediator of $\mathcal O(1)$ MeV mass. After analyzing the kinematics and cross section features of the $s$-channel resonance, we derive from first principles the double transport equations with double regeneration terms for the coupled evolution of neutrinos and anti-neutrinos. The simulated event spectrum is then compared with the HESE 7.5 year data observed at IceCube to give a clear lower bound on the lightest neutrino mass.

</details>

## Nuclear physics

### [Introducing Parton-Level Fluctuations in the TRENTo-Sea Model](https://arxiv.org/abs/2611.33662)
*Jacob Reinach, Andreas Kirchner* · `nucl-th` · arXiv:2611.33662v1 · relevance 0.11

- **In one sentence**: The paper extends the TRENTo-Sea initial-condition model for heavy-ion collisions by sampling quark and gluon momentum fractions from nuclear parton distribution functions, using perturbative QCD at the parton level and an infrared damping scale tuned to proton-proton cross sections.
- **In plain words**: Heavy-ion collisions at particle accelerators create a tiny, very hot droplet of matter, and models of its starting state need small-scale lumps inside each proton and neutron. This paper builds those lumps directly from measured tables of how quarks and gluons share a nucleon's momentum, rather than fitting their number and size to data. The authors report that the resulting model matches a standard flow measure (the elliptic-flow coefficient, ε2) of data-calibrated models except in the most central collisions.
- **Why it matters**: Sub-nucleon fluctuations shape the geometry that later turns into measured particle flow, so grounding them in known parton distributions could make the starting conditions less arbitrary. The text also suggests the work may help study correlations between soft and hard particles and compare different nuclear parton distribution sets, though the broader impact is not established by the text alone.
- **Background needed**: - Heavy-ion collisions: smashing large nuclei together to make quark-gluon plasma, a very hot, dense state of matter.
- Initial-condition model: a simulation of how energy and matter are distributed right after impact, which sets up the later flow.
- Sub-nucleonic fluctuations: small hot spots inside protons and neutrons, from quarks and gluons.
- Parton: the generic name for a quark or gluon inside a nucleon.
- Parton distribution function (nPDF for nuclei): a table giving the probability of finding a parton carrying a given fraction of a nucleon's momentum.
- Perturbative QCD: approximate calculations of quark-gluon interactions valid at high energies.
- Elliptic flow (ε2): a measure of how the outgoing particle spray is shaped by an almond-like overlap region.
- Infrared regulator: a cutoff that prevents calculations from diverging at very low momentum. · level: research-level

<details><summary>Original abstract</summary>

A variety of experimental and theoretical data suggest that initial condition models for heavy-ion collisions contain a degree of sub-nucleonic fluctuations. While current models fit the number and size of these fluctuations to data, we use nuclear parton distribution functions to constrain sub-nucleonic structure and fluctuations in TRENTo-Sea, an extension of TRENTo. Sampling the momentum fraction distributions of quarks and gluons in heavy ions, we use perturbative quantum chromodynamics to collide nuclei at the parton level, and we introduce an infrared center-of-momentum damping scale which is tuned to proton-proton cross sections. We find that our model successfully reproduces the $\varepsilon_2\{2\}$ of data-calibrated models except in central collisions, and an analysis of the power spectrum and granularity of the pre-equilibrium fireball shows that the number of low-$x$ partons in a nucleon has a significant effect on the local transverse geometry. Our model is largely insensitive to variations of the infrared parameters, as such changes are absorbed into the calibration of the infrared regulator. We expect that this work will aid future research on soft-hard correlations and constraining different nPDF sets.

</details>

### [Microscopic Approach to Neutron Elastic and Inelastic Cross Sections](https://arxiv.org/abs/2611.34752)
*Ibrahim Abdurrahman, Chloe Hebborn, Filomena Nunes et al.* · `nucl-th` · arXiv:2611.34752v1 · relevance 0.08

- **In one sentence**: The paper builds a microscopic, shell-model-based S-matrix framework for low-energy neutron elastic and inelastic scattering on 20Ne, benchmarked against ENDF evaluations and compared with Gaussian Orthogonal Ensemble statistics via Shannon entropy.
- **In plain words**: Nuclear reactions, where a neutron hits an atomic nucleus and either bounces off or knocks it into an excited state, are usually described with separate models for different time scales, and those models rely on fitted inputs. This paper tries to describe both kinds of neutron scattering in one framework, starting from a detailed theory of how the nucleus is built, using neon-20 as the test case. The authors report that their method qualitatively reproduces the standard evaluated cross sections for this reaction.
- **Why it matters**: Neutron-induced reaction data feed into nuclear energy, medical isotope and astrophysics calculations, so a method that relies less on adjustable inputs could eventually make predictions more reliable. The text only shows qualitative agreement for one nucleus and one set of channels, and the stated extensions to two-nucleon and gamma channels are future work, so its broader significance is not yet established.
- **Background needed**: - Cross section: the effective target area for a given reaction; it is what nuclear data tables list.
- Elastic vs. inelastic scattering: elastic means the neutron bounces off with the nucleus left in its ground state; inelastic means the nucleus is left excited.
- Shell model: a theory that computes nuclear energy levels and structure from how nucleons fill quantum "shells."
- Resonance: a temporary state of the neutron-plus-nucleus system with a sharply peaked probability of forming.
- S-matrix: a mathematical object encoding all possible scattering outcomes; its entries give the reaction probabilities.
- Level density and partial widths: counts of available energy levels and the rates at which a state decays through a given channel.
- ENDF: the Evaluated Nuclear Data File, a standard library of recommended reaction data.
- Shannon entropy and GOE: an information measure of spread in a distribution, compared with random-matrix (Gaussian Orthogonal Ensemble) statistics that describe chaotic quantum systems. · level: research-level

<details><summary>Original abstract</summary>

Depending on the nuclei involved and the beam energies, reaction timescales differ tremendously. Today, distinct models are often used to describe each timescale, relying on phenomenological inputs, such as level densities or partial-widths, which limits their predictive power. This work aims to address this issue by providing a unified description of low-energy neutron elastic and inelastic reaction channels starting from microscopic predictions of the structure of mid-mass nuclei. The goal is to build a framework that is general enough to span the different reaction regimes while remaining anchored in microscopic theory. For illustration purposes, this work focuses on reactions $n+^{20}$Ne to the elastic and inelastic channels. The S-matrix is build from shell model predictions of resonances states and their spectroscopic amplitudes for $^{21}$Ne, using two different approximations of the single-particle asymptotics. Then, the shell-model predictions for the level density and single-particle partial widths are analyzed and the final cross sections are compared with evaluated ones. This method qualitatively reproduces the ENDF evaluation for the $^{20}$Ne$(n,el)$ and $^{20}$Ne$(n,n')$ cross sections. The present study also compares the Shannon entropy obtained from this model to the Gaussian Orthogonal Ensemble (GOE). In the future, the framework will be extended to include more complex reaction channels, such as two-nucleon and gamma channels, enabling more accurate predictions of neutron-induced reactions such as those of astrophysical interest.

</details>

## Quantum information and computing

### [A Realistic End-to-End Runtime Crossover Estimation for Quantum-Enhanced Training of Large-Scale Machine Learning Models](https://arxiv.org/abs/2611.33454)
*Maximilian Alexander Wolf, Alona Sakhnenko, Florian Geissler et al.* · `quant-ph` · arXiv:2611.33454v1 · relevance 0.13

- **In one sentence**: The paper gives end-to-end resource estimates (data loading, quantum linear-system solving, and reading out results) for training a linearized neural network with a quantum linear solver, and locates the problem sizes where it might beat classical methods.
- **In plain words**: Quantum computers are often promised to speed up machine learning, but those promises usually ignore the practical costs of getting data in and results out. This paper takes a proposed quantum method for training a simplified neural network and estimates its real engineering costs across three increasingly realistic test scenarios. It finds that the quantum approach only pulls ahead of classical computing for very large problems, long run times, and very strict requirements on the output.
- **Why it matters**: It offers a more grounded check on a claimed quantum advantage for machine learning, showing which bottlenecks matter in practice. Its relevance to near-term industrial use is a hope the authors state, not something the text demonstrates.
- **Background needed**: - Quantum linear solver: a quantum algorithm for solving systems of linear equations, which can be faster in theory for some inputs.
- Linearized neural network: a simplified version of a neural network whose training reduces to solving linear equations.
- Asymptotic complexity: how cost grows as problem size becomes very large; it can hide large constant factors.
- Data access and readout: the cost of loading classical data into a quantum computer and extracting usable answers, which often dominate.
- Sparsity: the fraction of zero entries in a matrix; sparser matrices are typically cheaper to handle.
- Crossover point: the problem size at which a quantum method's total cost becomes lower than a classical method's. · level: research-level

<details><summary>Original abstract</summary>

Machine Learning (ML) is one promising application domain for Quantum Computing (QC) speedups, but asymptotic complexity considerations often mask the actual engineering costs of actual end-to-end workflows. For the use case of training a linearized Neural Network with a Quantum Linear Solver, a provably favorable quantum scaling has been suggested. We present realistic resource estimates for this problem, accounting for data access, computation, and readout. Our analysis examines three increasingly complex benchmarking scenarios, under distinct sparsity-scaling assumptions, thereby enabling progressively more realistic resource estimates. We identify crossover regimes relative to classical methods and find that crossover points emerge only for very large problem sizes, long computation times, and highly restrictive output requirements. This work provides a blueprint for evaluating quantum-enhanced ML algorithms under realistic hardware constraints and help identifying the bottlenecks that must be overcome to approach industrial quantum utility.

</details>

### [Efficient Quantum Algorithm for the Generalised Geography Game](https://arxiv.org/abs/2611.33853)
*Mriganka Sandilya, Shibdas Roy* · `quant-ph` · arXiv:2611.33853v1 · relevance 0.13

- **In one sentence**: The paper claims a bounded-error quantum polynomial-time (BQP) algorithm for the Generalized Geography Game, a PSPACE-complete problem on directed graphs, with runtime O(N^2/ε^6) and ε = O(1/poly(N)).
- **In plain words**: The paper looks at a two-player game played by moving a token along the arrows of a network without revisiting any point, and asks who wins from a given starting position. Classically this kind of question is believed to require exponentially growing time as the game gets bigger. The authors report a quantum algorithm that they say solves it in time that grows only polynomially with the size of the input.
- **Why it matters**: If correct, it would be a notable claim that a problem believed hard for classical computers, and widely thought to lie outside what quantum computers can efficiently do, is in fact tractable for them. The text gives only the abstract, though, so the claim should be checked against the full derivation before it is taken seriously; a result this strong would need close expert scrutiny.
- **Background needed**: - Graph: points (vertices) joined by arrows (directed edges).
- Combinatorial game: a game with fixed rules, no chance, and perfect information; players alternate moves.
- PSPACE-complete: a class of problems solvable with a modest amount of memory but believed to need exponential time; hardest in this class is a benchmark for difficulty.
- BQP: problems a quantum computer can solve with high probability in polynomial time.
- Bounded error: the quantum answer is wrong with probability at most a small fixed amount; here the error is allowed to shrink polynomially with input size.
- Polynomial time: running time grows as a fixed power of input size, considered efficient.
- Caveat: the text is only an abstract; it does not describe the algorithm's method, so its correctness cannot be assessed from it. · level: research-level

<details><summary>Original abstract</summary>

The Generalized Geography Game ($GGG$) is a two-player combinatorial game played on a directed graph, where players alternately move a token along edges without revisiting previously visited vertices. In the existing literature, determining whether an arbitrary position in a graph is a winning position for either player is a well-known $PSPACE$-complete decision problem. Certain formulations of $GGG$ have been shown to fall outside the $PSPACE$-complete complexity class. While $PSPACE$-complete problems are believed to take exponential time for classical computation, quantum computation offers new possibilities. In this work, we present a bounded-error quantum polynomial-time ($BQP$) algorithm for solving the $GGG$ problem. The proposed algorithm runs in time $O(N^{2}/\epsilon^{6})$, which is polynomial in the input size $N$, and achieves bounded error with $\epsilon = O(1/\mathrm{poly}(N))$. This result demonstrates the potential of quantum algorithms to efficiently solve combinatorial game problems that are traditionally considered computationally hard in the classical setting.

</details>

## Optics and atomic physics

### [Ferroionic CuCrP2S6 Integrated Silicon Photonics for Neuromorphic Computing](https://arxiv.org/abs/2611.33954)
*Ghada Dushaq, Srinivasa R. Tamalampudi, Mahmoud Rasras* · `physics.optics` · arXiv:2611.33954v1 · relevance 0.09

- **In one sentence**: The paper integrates the layered ferroionic material CuCrP2S6 onto silicon microring resonators and shows that electrical pulses shift the optical resonance via field-driven movement of Cu ions, giving volatile and nonvolatile optical memory that can mimic a leaky integrate-and-fire neuron.
- **In plain words**: Researchers built a tiny light-based switch on a silicon chip using a special layered crystal whose copper ions drift when a voltage is applied. Sending electrical pulses slowly changes the color (wavelength) at which the chip's light resonates, and the chip remembers this history. Some of the change fades within about a minute, while a larger part stays for at least a day, so the device can add up pulses and also forget them over time.
- **Why it matters**: Neuromorphic computing aims to build hardware that handles information the way brains do, with memory and gradual forgetting built in. Optical devices of this kind could in principle be fast and low in power, but the text reports only one device and a short set of measurements, so its practical scale and performance remain untested here.
- **Background needed**: - Photonics: using light instead of electrons to carry and process signals.
- Silicon microring resonator: a tiny circular waveguide on a chip that traps light at specific wavelengths; a shift in its resonance wavelength changes how much light passes through.
- van der Waals material: a crystal made of thin layers held together weakly, so it can be placed on other chips.
- Ferroionic: a material where mobile ions (charged atoms) move under an electric field and can lock into a state.
- Volatile vs. nonvolatile memory: volatile states fade without power; nonvolatile states persist.
- Leaky integrate-and-fire neuron: a standard simplified model of a neuron that sums inputs, slowly leaks charge, and fires when a threshold is crossed.
- Time constant: the time for a fading quantity to drop to about 37% of its starting value. · level: research-level

<details><summary>Original abstract</summary>

Neuromorphic photonic computing calls for optical states that combine stimulus accumulation, spontaneous relaxation, and nonvolatile state retention without continuous power dissipation. Here, we demonstrate a ferroionic photonic platform by integrating layered van der Waals CuCrP2S6 onto silicon microring resonators using a back-end integration process. Electrical pulsing produces unidirectional blue shifts in the optical resonance, consistent with field-driven redistribution of mobile Cu ions and giving rise to a history-dependent optical response. The resulting optical state is strongly pulse dependent, exhibiting both volatile and nonvolatile components. A short 20-pulse excitation produces an initial 70 pm resonance shift that relaxes toward baseline within approximately 60 s, with a volatile relaxation time constant of 27-29 s. In contrast, after 1000 pulses, an initial 0.27 nm resonance shift relaxes to a persistent 0.13 nm nonvolatile state that is retained for at least 24 h. Repeated 6 V electrical pulses produce a progressive resonance shift over 1000 cycles, demonstrating cumulative optical integration. A fixed-wavelength readout converts the accumulated resonance shift into a thresholded optical response, with the normalized transmission remaining above the selected threshold through 600 pulses and falling below it at the 800-pulse state. These dynamics realize the basis for a leaky integrate-and-fire photonic neuron, where the pulse-dependent ionic response provides integration, spontaneous relaxation supplies a passive leak, persistent states provide nonvolatile memory, and fixed-wavelength readout provides an optical threshold response.

</details>

### [Statistical analysis of crossing beam speckle fields](https://arxiv.org/abs/2611.33483)
*Ian D. Min-Roberts, Wojciech Rozmus, Pierre A. Michel* · `physics.optics` · arXiv:2611.33483v1 · relevance 0.08

- **In one sentence**: A statistical model of speckle patterns formed by two or more crossing laser beams, defining effective speckle size and abundance via a Kac-Rice asymptotic count, checked by Monte Carlo simulation, and applied to quad-beam smoothing and stimulated Brillouin scattering.
- **In plain words**: Laser beams that cross each other produce a grainy pattern of bright and dark spots, called speckle. This paper builds a statistical description of that pattern: it defines what counts as one speckle, estimates how big and how many speckles there are, and checks the estimate with computer simulations. It then uses the model to look at a four-beam setup meant to smooth the laser light, and reports that spreading the beams further apart reduces the expected amount of one unwanted light-scattering effect from the brightest spots.
- **Why it matters**: Controlling the uniformity of laser light matters for laser-driven fusion experiments, where uneven intensity can drive instabilities in the plasma. The text does not discuss fusion directly, so that link is an inference from the stated motivation (polarization smoothing and plasma density fluctuations) rather than something the paper spells out.
- **Background needed**: - Speckle: the random grainy interference pattern produced when coherent laser light scatters or overlaps.
- Intensity field: how bright the light is at each point in space.
- Speckle abundance: how many separate bright spots of a given kind occur per unit area.
- Kac-Rice formula: a standard probability tool for counting how often a random smooth function crosses a level, here used to count speckles.
- Monte Carlo simulation: running many random trials on a computer to check a theoretical prediction.
- Stimulated Brillouin scattering (SBS): a process in which laser light scatters off sound-like waves in plasma, losing energy; it is a concern in laser fusion.
- Polarization smoothing: mixing beams of different polarization to make the overall light more uniform. · level: research-level

<details><summary>Original abstract</summary>

Building on the statistical analysis of single beam speckles, this paper develops a statistical description of speckle fields formed by crossing laser beams. A formal definition of individual speckles and their domains allows us to quantify the effective size and abundance of speckles. For two crossing beams, the effective speckle size is derived from the local curvature of the intensity field, and the expected speckle abundance is found asymptotically with the Kac-Rice formula. Monte Carlo simulations of speckle abundance show excellent agreement with the theoretical abundance formula. The two beam speckle analysis is then applied to a symmetric quad beam configuration motivated by polarization smoothing and demonstrates that increasing the separation between beams reduces expected stimulated Brillouin scattering reflectivity from saturated speckles. The statistical model is then extended to an arbitrary number of beams using a coordinate free formulation to obtain the spectral density of laser driven electron density fluctuations.

</details>

## Fluids and plasma

### [AI Buckingham: Agentic Discovery of Dimensionless Scaling Laws Across Physical Regimes](https://arxiv.org/abs/2611.33961)
*Ao Cheng, Lei Zhang, Guowei He* · `physics.comp-ph` · arXiv:2611.33961v1 · relevance 0.08

- **In one sentence**: The paper presents AI Buckingham, an LLM-driven agentic framework that uses mutual information and regime clustering to find dominant dimensionless groups and scaling laws across ten physical systems, including turbulent drag on rough surfaces.
- **In plain words**: Scientists often compress physics problems into a few unitless ratios, which makes experiments and simulations easier to compare. This paper describes a software system in which a large language model plans the work and calls analysis tools to pick out which of these ratios matter most, and whether that changes between operating regimes. The authors report that it recovers known similarity relations in ten systems and suggests better ways to describe surface roughness for estimating drag.
- **Why it matters**: Choosing the right dimensionless groups is a long-standing step in fluid and plasma modelling, so an automated method for it could save effort if it holds up. The text reports the roughness result as an improvement in equivalent sand-grain roughness estimates, but the size and generality of that gain are not given in the summary, so its practical value is uncertain.
- **Background needed**: - Dimensionless group: a ratio of physical quantities with no units, such as the Reynolds number, which compares inertia to viscous forces.
- Dimensional analysis (Buckingham Pi theorem): a classical method that says how many such unitless groups a problem needs, but not which ones matter.
- Scaling law: a rule of the form output ∝ input^power that relates measurements across sizes or conditions.
- Mutual information: a statistical measure of how much knowing one variable tells you about another, used here to rank groups.
- Regime: a range of conditions where the same physics dominates, so the dominant relations can change between regimes.
- Equivalent sand-grain roughness: a standard way engineers summarize a rough surface's effect on turbulent drag.
- Agentic framework: a system where an LLM plans steps and calls specialized tools. · level: research-level

<details><summary>Original abstract</summary>

Classical dimensional analysis defines admissible dimensionless representations but does not determine which combinations capture the dominant physical dependence, whether it changes across physical regimes, or when dependent-variable rescaling is required. We present AI Buckingham, an agentic framework for autonomous dimensionless discovery from natural-language descriptions of physical problems and observational data. It couples reasoning and planning by a large language model (LLM) with predefined symbolic and numerical tools. Literature-based knowledge retrieval supports dimensional checking, gradient-based clustering identifies physical regimes, and mutual information provides an objective, reparameterization-invariant criterion for identifying dominant dimensionless groups. Explicit numerical criteria determine the group count and assess simplification. Across ten physical systems spanning fluid dynamics, magnetohydrodynamics, thermal convection and additive manufacturing, AI Buckingham recovers established similarity representations and resolves regime-dependent scalings. For the longstanding challenge of predicting turbulent drag on rough surfaces, it identifies informative reparameterizations of surface statistics that improve equivalent sand-grain roughness estimates for engineering-oriented drag modelling.

</details>

### [Butterfly Effect in Kinetic Plasma Turbulence](https://arxiv.org/abs/2611.33357)
*Louis Henderson, Vladimir Zhdankin* · `physics.plasm-ph` · arXiv:2611.33357v1 · relevance 0.07

- **In one sentence**: PIC simulations of driven collisionless plasma turbulence show that a tiny localized perturbation, down to a single particle, is exponentially amplified until paired runs statistically decorrelate within a few dynamical times, and an analytical model approximates the early growth.
- **In plain words**: This paper asks whether the "butterfly effect" (the idea that a tiny change can grow into a large difference later) holds for a turbulent plasma, a hot gas of charged particles like those in space or fusion devices. The authors ran pairs of computer simulations that were identical except for one tiny nudge to a few particles. They found the difference spread outward and grew exponentially until the two runs looked statistically unrelated.
- **Why it matters**: It suggests that turbulent plasmas, such as those in space weather or fusion experiments, may be intrinsically hard to predict in detail, since even the smallest uncertainty in the starting state is quickly amplified. The text does not go beyond this plasma setting, so broader implications are a reasonable inference rather than a demonstrated result.
- **Background needed**: - Butterfly effect: sensitive dependence on initial conditions, where tiny differences grow exponentially in chaotic systems.
- Turbulence: chaotic, swirling motion across many scales in a fluid or plasma.
- Plasma: an ionized gas whose charged particles interact through electric and magnetic fields.
- Collisionless: particles interact mainly through fields rather than frequent direct collisions.
- Particle-in-cell (PIC) simulation: a method that tracks many individual particles on a grid of fields.
- Plasma beta: the ratio of particle pressure to magnetic pressure; temperature sets whether particles are sub- or ultra-relativistic.
- Decorrelation: the two simulations no longer match statistically, though each remains a valid run.
- Machine precision: the smallest number difference a computer can represent; perturbations below it vanish. · level: research-level

<details><summary>Original abstract</summary>

The butterfly effect is a fundamental process in chaotic systems, but it has not previously been characterized in detail for a collisionless turbulent plasma. In this work, we apply particle-in-cell (PIC) simulations of driven turbulence to study the emergence of the butterfly effect from a small initial perturbation to the simulated particles. In particular, we compare pairs of (baseline and perturbed) simulations that differ only by a localized initial perturbation (down to the single-particle level). We find that the effect of the localized perturbation spreads radially throughout the PIC simulation, causing a difference between each simulation pair that is exponentially amplified over time within the affected region. The fields, including the electric current density, eventually become statistically decorrelated. We construct an analytical model combining spatial expansion with exponential amplification to approximate the early-time evolution. Varying the initial perturbation primarily affects the early-time evolution, while having little effect on the final, decorrelated state. We describe parameter scans with varying plasma beta and temperature (covering sub-relativistic and ultra-relativistic regimes). Our results show that remarkably small perturbations will grow to decorrelate each pair of simulations within a few dynamical times; the imposed perturbation can no longer be resolved once it falls below the numerical precision floor set by the machine precision. These results confirm that the butterfly effect is very strong and robust in a collisionless plasma, with implications for the predictability of turbulent plasma systems.

</details>

## Biological physics

Nothing notable this time.

## Climate, atmosphere and Earth

### [Weak buoyancy and cold lithospheres decouple interior melting from seafloor volcanism on icy ocean worlds](https://arxiv.org/abs/2611.33478)
*Nahiz Hestaphin* · `astro-ph.EP` · arXiv:2611.33478v1 · relevance 0.05

- **In one sentence**: A modelling study linking melt segregation, fracture flow, crystallisation and an ice-loaded ocean boundary to explain why seafloor volcanism on icy moons like Europa may be history-dependent and decoupled from melt production at depth.
- **In plain words**: The paper asks how molten rock generated deep inside an icy moon could reach the seafloor under a thick ice shell and an ocean, given that the magma tends to freeze on the way. The authors built a coupled model of melt moving through fractures, rock slowly deforming, and cooling, and ran it for hot and cold Europa-like cases. They report that the rock's grain size and the pressure from the overlying ice and ocean strongly control whether a fracture stays open long enough to deliver magma.</plain>
<parameter name="why">The text suggests that seafloor eruptions on icy ocean worlds may depend more on whether a pathway stays thermally connected than on how much melt is produced, which matters for judging where volcanism could occur and whether such moons could host accessible chemistry. The text does not show how well these modelled values match observations, so the link to real missions or detections is uncertain.</plain>
<parameter name="background">- Icy ocean worlds (e.g., Europa): moons with an icy shell over a liquid water ocean, with rock below.
- Melt segregation: molten rock separating from the surrounding crystals and flowing upward.
- Fracture flow: magma moving through narrow cracks; the crack must stay open against pressure.
- Crystallisation/freezing: magma cooling and solidifying, which can block a path.
- Lithosphere: the cold, rigid outer rock layer; "relaxation" describes how it slowly deforms under stress.
- Enthalpy margin: the spare heat a magma has above its freezing point.
- Units: kPa and MPa are pressures; km3 and m3 s-1 measure volume and flow rate.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

On icy ocean worlds, deep silicate melting can generate sufficient pressure to open fractures while magma freezes before reaching the ocean. We identify a coupled transport regime by linking finite melt segregation and nonlinear rock relaxation to fracture flow, crystallisation and the ice-loaded ocean boundary. In a hot Europa endmember, increasing grain size from 1 to 10 mm raises relaxed excess pressure from 5.55 kPa to 10.2 MPa, overcoming the inherited-fracture opening threshold despite weak buoyancy. For the same 100 m strike and 0.5 m aperture, the cold first-fill rate required by heat balance increases from 0.17-0.69 m3 s -1 over terrestrial crustal distances of 1.1-4.5 km to 15-29 m3 s -1 across 89-171 km Europa paths, far above the self-supplied flow. Higher ice-ocean pressure further reduces the enthalpy margin of near-solidus magma in the adopted basalt phase law. During approximately 5 kyr of dormancy, the collector pressure returns to its relaxed value, while upper-path walls cool to 275-282 K and the magma path loses liquid connectivity. In two focused Europa histories with mechanically supported pathways, delivery of 0.005 km3 of magma over 0.1 Myr requires 14-27 km3 of sacrificed magma-equivalent preparation material. Weak gravity, extensive cold rock and a pressurised ocean thus make seafloor access a history-dependent process governed by thermal connectivity and its renewal, decoupling recurrent volcanism from melt production at depth.

</details>

### [Skysail: Altitude Control of Long-Duration Weather Balloons by Extracting Work from Wind Shear](https://arxiv.org/abs/2611.33882)
*Michal Adamkiewicz, Andrey Sushko* · `physics.ao-ph` · arXiv:2611.33882v1 · relevance 0.05

- **In one sentence**: A control system for long-duration zero-pressure weather balloons that uses a pitch-controlled wing on a tether, 450 m below the balloon, to convert wind shear into aerodynamic forces for repeated altitude profiling, with ballast and venting kept for trim and fallback.
- **In plain words**: Weather balloons that rise and fall to take measurements of the air at different heights usually rely on releasing gas or dropping ballast, and they can only do this a limited number of times. This paper describes a small wing hung on a line below the balloon, which uses the difference in wind speed between two heights to push itself up or down. Over flights lasting two years, the authors report that the system completed repeated profiles, including 24 profiles over an eight-day flight, without relying on consumables for those moves.
- **Why it matters**: Balloons that can profile the atmosphere many times without using up consumables could extend how long a single flight collects useful data. The text does not compare costs or measurement quality with existing systems, and it notes that control depends on how much wind shear is available, so the broader practical reach is uncertain.
- **Background needed**: - Zero-pressure balloon: an open-bottomed balloon that keeps roughly constant pressure inside and floats at a set altitude, changing height only by venting gas or dropping ballast.
- Atmospheric profile: a set of measurements (temperature, pressure, wind, humidity) taken at many heights as the balloon rises and falls.
- Wind shear: the change in wind speed or direction between two altitudes.
- Pitch: the tilt angle of a wing; changing it changes the lift and drag the wing produces.
- Tether: a line connecting the balloon to the wing; the wing sits 450 m below the balloon here.
- Ballast and venting: consumable actions (dropping weight, releasing gas) that are finite per flight.
- Aerodynamic governor: a passive device that limits the rate at which the tether unwinds. · level: intermediate

<details><summary>Original abstract</summary>

Long-duration weather balloons collect repeated atmospheric profiles by venting lifting gas and dropping ballast, but these finite consumables limit the number of profiles each balloon can obtain. We present an altitude-control system that extracts mechanical work from atmospheric wind shear. A small wing suspended 450 m below a zero-pressure balloon experiences relative airflow from the wind velocity difference between the two altitudes. Controlling the wing's pitch produces aerodynamic forces that drive ascent and descent. We develop a model for sizing the system, a lightweight aerodynamic governor for tether deployment, and a control architecture for altitude holding and repeated profiling. Flight experiments conducted over two years accurate control of vertical motion. During a 43-hour interval, the system completed eleven profiles and accumulated 53 km of vertical travel without releasing ballast or venting gas. A separate eight-day flight completed 24 profiles exceeding 1 km in vertical extent, accumulating 159 km of vertical travel. Control authority depends on the available wind shear, with conventional ballast and vent actuation retained for trim and fallback control. These results demonstrate that atmospheric wind shear can sustain repeated balloon profiling while reducing dependence on consumable actuators.

</details>

## Cosmology

### [Acoustic Priors from the Latest Cosmic Microwave Background Data](https://arxiv.org/abs/2611.33334)
*Kushal Lodha, Jun-Qian Jiang, Purba Mukherjee et al.* · `astro-ph.CO` · arXiv:2611.33334v1 · relevance 0.15

- **In one sentence**: Using a separation of early-Universe acoustic-peak information from late-time lensing and ISW effects, the paper updates model-independent CMB constraints on the acoustic scale and physical densities with Planck PR4, ACT DR6 and SPT-3G D1 data, and tests how marginalizing over lensing-induced peak smoothing affects the evidence for evolving dark energy from CMB plus DESI DR2 BAO.
- **In plain words**: The paper looks at the faint pattern of hot and cold spots in the leftover glow from the early Universe, the cosmic microwave background. It separates the part of that pattern that records conditions just after the Big Bang from distortions added on the way to us by gravity from large-scale structure. Using newer telescope data combined, the authors report updated measurements of the pattern's characteristic size and of the amounts of baryons and dark matter, and they study how these choices change the statistical case for dark energy changing over time.
- **Why it matters**: The claimed shift in dark-energy evidence, from 3.0 to 1.9 sigma (and 3.2 to 2.4 sigma with supernovae added), depends on modelling choices, so it matters for how strongly current data favour non-constant dark energy. The paper's own statements are limited to these analysis results; their wider significance is for specialists to judge.
- **Background needed**: - Cosmic microwave background (CMB): light from about 380,000 years after the Big Bang, mapped as temperature and polarization patterns.
- Acoustic peaks: regularly spaced features in the CMB power spectrum, produced by sound waves in the early plasma; their spacing sets the angular acoustic scale.
- Gravitational lensing of the CMB: nearby matter bends the light, smoothing the peaks; the lensing signal can be reconstructed from the data.
- Integrated Sachs-Wolfe (ISW) effect: a late-time shift in CMB photon energies caused by changing gravitational potentials, e.g. from dark energy.
- Physical densities (omega_b, omega_bc): baryon density and baryon-plus-dark-matter density, scaled by the Hubble constant squared.
- Baryon acoustic oscillations (BAO): a preferred separation between galaxies left by early sound waves, used as a cosmic ruler; DESI DR2 is a recent survey.
- LCDM vs w0waCDM: the standard model with a constant dark energy versus a model where dark energy evolves over time; sigma values measure how strongly data prefer one over the other.
- Planck PR4, ACT DR6, SPT-3G D1, WMAP: CMB experiments and their data releases. · level: research-level

<details><summary>Original abstract</summary>

We revisit the physics of the acoustic peaks and illustrate how early-Universe information in the cosmic microwave background (CMB) can be disentangled from late-time signatures imprinted by gravitational lensing and the integrated Sachs-Wolfe (ISW) effect. Applying this separation to Planck PR4, ACT DR6, and SPT-3G D1 temperature and polarization data combined with the joint lensing reconstruction, we update the model-independent constraints on the angular acoustic scale and the physical densities, $100\theta_*=1.04100\pm0.00021$, $\omega_{\rm b}=(2.2440\pm0.0099)\times10^{-2}$, and $\omega_{\rm bc}=0.1410\pm0.0011$. These constraints are consistent with the previous Planck PR4-only analysis and remain stable for extended late-time cosmologies beyond $\Lambda$CDM. Adding ACT DR6 to the combination favors a higher $\omega_{\rm b}$ and, through their correlation, a higher primordial tilt $n_{\rm s}$ than PR4 alone. The reconstructed lensing spectrum exceeds that of $\Lambda$CDM, with two features near $L\simeq50$ and $L\sim10^3$, and the excess is reduced when WMAP replaces the Planck primary spectra. Marginalizing over the lensing-induced peak smoothing, rather than tying it to the late-time model, lowers the preference of the CMB and DESI DR2 baryon acoustic oscillations (BAO) for $w_0w_a$CDM over $\Lambda$CDM from $3.0\sigma$ to $1.9\sigma$, or from $3.2\sigma$ to $2.4\sigma$ when Union3.1 supernovae are added. We further use the acoustic prior to predict BAO distances from CMB data alone under several late-time expansion histories, testing their consistency with DESI measurements assuming standard pre-recombination physics.

</details>

### [No Cluster Left Behind I: Joint Mass Calibration for Dark Energy Survey and South Pole Telescope Clusters](https://arxiv.org/abs/2611.33522)
*C. Zhou, A. N. Salcedo, S. Grandis et al.* · `astro-ph.CO` · arXiv:2611.33522v1 · relevance 0.13

- **In one sentence**: A joint statistical model that combines Dark Energy Survey optical richness and weak-lensing data with South Pole Telescope Sunyaev-Zel'dovich signals to calibrate cluster masses, including clusters seen by only one survey, and to constrain optical selection biases.
- **In plain words**: Galaxy clusters are the largest gravitationally bound objects in the universe, and knowing their masses is key to measuring dark energy. This paper proposes a flexible way to combine cluster catalogs from different telescopes, so that clusters seen by only one survey can still be used. As a test, the authors combine optical galaxy counts and lensing measurements from the Dark Energy Survey with microwave signals from the South Pole Telescope.
- **Why it matters**: Mass calibration is a major source of uncertainty in cluster-based dark energy measurements, so a method that uses far more clusters could tighten those results. The text reports a roughly 20% bias in the large-scale lensing signal for richness-selected clusters, but the wider impact for next-generation surveys is the authors' claim and has not been tested here.
- **Background needed**: - Galaxy clusters: huge collections of galaxies and hot gas; their abundance depends on dark energy and matter.
- Mass calibration: working out how massive a cluster is, which is hard to measure directly.
- Richness: a count of member galaxies seen in optical images; cheap to measure but can be fooled by chance alignments along the line of sight.
- Weak lensing: faint distortion of background galaxy images by a cluster's gravity, used to estimate mass.
- Sunyaev-Zel'dovich effect: a distortion of the cosmic microwave background caused by hot gas in clusters, detected by the South Pole Telescope.
- Selection bias: systematic errors from how a sample of objects was chosen.
- Halo mass function: how many clusters of each mass exist, a key cosmological test. · level: research-level

<details><summary>Original abstract</summary>

Multiwavelength observations of galaxy clusters are among the most promising probes of the growth of structure and dark energy. Optically identified clusters have a high number density and can thus probe the halo mass function well into the group regime, but their weak-lensing mass calibration suffers from a selection bias induced by line-of-sight projection effects. Clusters detected via their intracluster medium (ICM) -- through X-ray emission or the thermal Sunyaev-Zel'dovich effect (SZe) -- are less affected by such selection biases, but current survey sensitivity restricts ICM-selected samples to high-mass systems. Previous multiwavelength analyses tend to limit to clusters with millimeter detections and thus to the high-mass population. In this paper, we propose a flexible modeling framework in which all clusters from multiwavelength surveys can be combined and modeled, even if they are detected in only one survey. As a pilot study, we jointly model richness and lensing of clusters from the Dark Energy Survey and the SZe signal from the South Pole Telescope. This approach yields precise cluster mass calibration while self-consistently constraining optical selection biases. We have found a $\sim$20% bias in the large-scale lensing signal of clusters selected by richness, and a bias ranging from $\sim-20$% at low richness to zero at high richness for clusters selected by both richness and SZe. Compared to current approaches, this framework is highly scalable and readily extensible, paving the way for the full utilization of multiwavelength cluster data in next-generation surveys.

</details>

## Galaxies

### [State of the UNIONS: Four Milky Way companions discovered in a systematic search for northern Local Group satellites](https://arxiv.org/abs/2611.34775)
*Simon E. T. Smith, Alan W. McConnachie, Thomas de Boer et al.* · `astro-ph.GA` · arXiv:2611.34775v1 · relevance 0.18

- **In one sentence**: Photometric search of the UNIONS northern sky survey reports four new Milky Way satellites, two likely ultra-faint dwarf galaxy candidates (Boötes VI, Draco III) and two extremely faint compact systems (UNIONS 2, UNIONS 3) whose dark-matter status cannot yet be decided from morphology alone.
- **In plain words**: Astronomers searched a large map of the northern sky, taken through three colour filters, for small clusters of old stars orbiting our Milky Way. They found four new faint groups. Two look like small galaxies that are candidates for classification, and two are so faint and compact that it is unclear whether they are galaxies or star clusters.
- **Why it matters**: Faint satellites like these are the smallest known galaxies, and they test models of how galaxies form and whether dark matter is present in the tiniest ones. The paper notes that many more such objects are expected from upcoming wide-field surveys, though the authors stress that confirming their nature will require spectroscopic (chemical and velocity) studies.
- **Background needed**: - Milky Way satellites: smaller stellar systems orbiting our galaxy; ultra-faint dwarfs are the dimmest known, with very few stars.
- Globular clusters: dense, roughly spherical groups of old stars; they are usually more compact than dwarf galaxies of similar brightness.
- Photometry (gri bands): measuring brightness through green, red and near-infrared-ish optical filters to find and characterise stellar groups.
- Absolute magnitude (M_V): intrinsic brightness of an object; more negative means brighter. Values near 0 or positive are very faint.
- Half-light radius: the radius containing half of the light; a measure of how spread out the system is, given in parsecs (pc).
- Dark matter: unseen matter inferred from gravitational effects; detecting it in tiny systems usually needs measured stellar velocities.
- Chemodynamical analysis: combining stars' chemical make-up and motions to judge whether a system is a galaxy. · level: research-level

<details><summary>Original abstract</summary>

We present four newly discovered Milky Way satellites from a systematic search through the $gri$ photometry from the Ultraviolet Near-Infrared Optical Northern Survey (UNIONS). Two of these satellites are likely ultra-faint dwarf galaxies that we have named Bo\"otes VI and Draco III. Both galaxy candidates are $\gtrsim 100$ kpc from the Galactic center and have absolute $V$-band magnitudes ($M_V$) of $-2.7^{+0.6}_{-0.5}$ and $-4.0\pm0.6$, respectively. Bo\"otes VI and Draco III have physical half-light radii ($r_{\rm h}$) of $\sim 50$ pc, or about twice as large as the most extended Milky Way globular clusters with similar luminosities. They are therefore candidate galaxies, though chemodynamical analyses will be needed to secure these classifications. We name the two other systems UNIONS 2 and UNIONS 3. They are extremely faint ($M_V = +0.4^{+0.6}_{-0.9}$ and $-0.7^{+0.6}_{-0.8}$) and compact ($r_{\rm h} = 5\,\pm\,1$ and $10^{+3}_{-2} pc), and zero giant stars are identified in either of their present-day stellar populations. Morphological measurements alone are not sufficient to assess the presence of dark matter in either system, so do not provide definitive classifications. We discuss the challenges in either detecting or refuting the presence of dark matter in UNIONS 2 and UNIONS 3, two systems that are archetypal of the faintest satellites that will be discovered in increasing numbers in upcoming wide-field surveys.

</details>

### [The role of hierarchy in Galactic molecular clouds](https://arxiv.org/abs/2611.33956)
*Kotora Sasaki, Nario Kuno, Hajime Fukushima et al.* · `astro-ph.GA` · arXiv:2611.33956v1 · relevance 0.16

- **In one sentence**: Using FUGIN CO survey data for 13 Galactic massive star-forming regions, this paper applies a non-binary dendrogram to classify gas structures into trunks, internal leaves, and isolated structures, and compares their star and clump formation efficiencies with an analysis of variance that controls for region.
- **In plain words**: This study looks at how gas clouds in the Milky Way are organized before massive stars form. The authors sorted the dense gas in 13 star-forming regions into large nested structures ("trunks"), the densest pockets inside them ("leaves"), and free-standing clumps. They found that leaves are more massive, denser and more tightly bound than isolated structures of similar size, yet they form fewer low-mass stars per unit gas while turning more of their gas into dense clumps.
- **Why it matters**: It suggests that massive star formation depends on gas organized across scales larger than a single core, with the large structures feeding the smaller dense pockets. The interpretation is the authors' own, and the data are single-epoch snapshots, so the link to accretion and fragmentation is a proposed explanation rather than something directly observed.
- **Background needed**: - Molecular clouds: cold, dense gas in space, mapped here using carbon monoxide (CO) emission as a tracer.
- Position-position-velocity data: a three-dimensional map (sky position plus line-of-sight speed) of the gas.
- Dendrogram: a tree-like diagram that groups gas into nested structures, from large to small; "trunks" are the largest, "leaves" the densest pieces within them.
- Star formation efficiency: the fraction of gas that ends up in stars (here, low-mass young stellar objects, YSOs) or in dense clumps (from the Hi-GAL survey).
- Fragmentation: the breaking of a gas cloud into smaller pieces that can collapse; the "characteristic mass" is the typical size of those pieces.
- Accretion: gas falling onto a denser object over time.
- Analysis of variance: a statistical test for differences between groups while accounting for differences between regions. · level: research-level

<details><summary>Original abstract</summary>

To probe the role of hierarchical gas structures in massive star formation, we statistically analyzed 13 Galactic massive star-forming regions using FUGIN CO survey data. Applying a non-binary dendrogram to the position-position-velocity data, we classified the extracted structures into trunks, internal leaves (the densest substructures within trunks), and isolated structures, and compared their properties with an analysis of variance controlling for regional differences. In representative regions, the trunks correspond to morphologies such as filaments and hub-filament systems, or to kinematic signatures of structure-forming events such as cloud-cloud collisions. Across the sample, the trunks are extended, massive, and strongly bound reservoirs, while the leaves are significantly more massive, denser, and more tightly bound than isolated structures of similar spatial scale. Using YSOs and Hi-GAL clumps, we find that the leaves have a lower low-mass star formation efficiency than isolated structures, whereas their clump formation efficiency is comparable. At a fixed gas mass, the leaves show no higher low-mass star formation efficiency than isolated structures but convert a larger fraction of their gas into dense clumps. We interpret these contrasts, together with inward gas motions in the position-velocity diagrams, as indicating that the deep potential of the trunks sustains continuous accretion onto the leaves and promotes mutual interactions among them. These processes may raise the characteristic fragmentation mass, as theoretically expected for a dynamically accreting medium, so that a larger fraction of the gas forms massive clumps without a corresponding increase in low-mass star formation. Our single-epoch data constrain only these structural contrasts, but indicate that the gas available for massive star formation is organized on scales larger than a single core.

</details>

## Exoplanets and planetary science

### [Planetary biotechnospheres, biotechnosignatures and the search for extraterrestrial intelligence](https://arxiv.org/abs/2611.33404)
*Irina K. Romanovskaya* · `astro-ph.EP` · arXiv:2611.33404v1 · relevance 0.08

- **In one sentence**: A speculative theoretical paper proposing ten possible "biotechnosignatures" (traces of technology-linked biospheres) and search strategies for them, both within the Solar System and over interstellar distances, including a "Cosmic Descendants" hypothesis.
- **In plain words**: The paper asks whether an advanced civilization, or its machines, could leave lasting signs of a mix of living systems and technology that reshape a planet, and how we might look for those signs. The author proposes ten possible signs and ways to search for them, both near Earth and in objects passing through the Solar System. One example is the "Cosmic Descendants" idea: engineered bacteria from an ancient civilization might still survive on Earth, or its technology might have drifted to the outer Solar System. The text also gives a rough estimate that interstellar asteroids are very unlikely to carry such systems.
- **Why it matters**: It widens the search for extraterrestrial intelligence beyond radio signals to traces of life and technology working together, which could be checked with future planetary and space missions. Its value depends on whether these ideas can be tested; the text gives no observations, so it should be read as a framework for discussion rather than evidence.
- **Background needed**: - Biosphere: all living things on a planet and the way they interact with their environment.
- Technosphere: the human-made infrastructure and technology that now affects planetary systems.
- Biotechnosphere: the proposed zone where living systems and technology are linked and shape each other.
- Biosignature / technosignature: a measurable sign of life or of technology, respectively, used in the search for alien life.
- Oort cloud: a distant, icy shell of objects surrounding the Solar System, far beyond the planets.
- Post-main-sequence stars: stars in the late stages of their lives, after they have stopped burning hydrogen steadily in their cores.
- Terraforming: deliberately altering a planet or moon to make it more Earth-like.
- Speculative: the paper offers possibilities and proposals, not tested results. · level: intermediate

<details><summary>Original abstract</summary>

The concept of planetary intelligence as collective intelligence is used to consider possible evolutionary paths of biotechnospheres that emerge on the intersection of the technosphere with the biosphere and support coupling of the technosphere with the biosphere, thus affecting planetary evolution. In mature biotechnospheres, the intelligence of technologies and the intelligence of life forms, including engineered life forms, could act in concert to perform various tasks (e.g. monitoring and restoring planetary environments and biodiversity; supporting space missions; terraforming cosmic objects). Space exploration can expand biotechnospheres beyond planets and create cosmic ecosystems. Humankind, other civilizations or their intelligent machines may produce biotechnosignatures (i.e. observables and artefacts of biotechnospheres) in the Solar System and beyond. I propose ten possible biotechnosignatures and strategies for the search for these biotechnosignatures in situ and over interstellar distances. For example, if a non-human advanced civilization existed and built biotechnospheres on Earth in the past, the descendants of its engineered bacteria could currently exist on Earth and have properties pertaining to the functions of the ancient bacteria in the biotechnospheres; intelligent technologies created by the ancient civilization could migrate to the Solar System's outer regions; these two scenarios are described as the Cosmic Descendants hypothesis. Interstellar asteroids, free-floating planets, spacecraft and objects gravitationally bound to flyby stars might carry extraterrestrial biotechnospheres and pass through the Solar System. In connection to the fate of post-main-sequence stars and their Oort clouds, the probability for interstellar asteroids to carry biotechnospheres or to be interstellar spacecraft is estimated as very low.

</details>

### [line racer: Rapid Calculation of Exoplanetary Radiative Opacities](https://arxiv.org/abs/2611.33290)
*David B. H\"agele, Paul Molli\`ere, Michiel Min* · `astro-ph.IM` · arXiv:2611.33290v1 · relevance 0.07

- **In one sentence**: line racer is a Python package for computing high-resolution opacities (light-absorption coefficients as functions of wavelength, temperature and pressure) from large molecular and atomic line lists, with parallelization for multi-core and multi-node systems and output compatible with common atmospheric modeling and retrieval tools.
- **In plain words**: Astronomers study the atmospheres of exoplanets and brown dwarfs by looking at which colors of light the gas absorbs. To interpret those patterns, they need tables of how strongly each molecule or atom absorbs light under many different temperatures and pressures. This paper describes line racer, a software tool that builds these absorption tables quickly from large catalogs of spectral lines and can run across many computer processors.
- **Why it matters**: Faster, customizable opacity tables help researchers model and retrieve atmospheric compositions from telescope spectra, which matters for characterizing exoplanets. The text describes the software's features and design but does not report specific speed comparisons or scientific results, so its practical impact beyond the tool itself is unclear from this text alone.
- **Background needed**: - Exoplanets are planets orbiting other stars; brown dwarfs are objects too massive to be ordinary planets but too small to sustain hydrogen fusion like stars.
- A spectrum is the breakdown of light into its wavelengths; dark gaps or dips reveal which molecules are present.
- Opacity measures how strongly a gas absorbs light at a given wavelength; it depends heavily on temperature and pressure.
- A line list is a catalog of the specific wavelengths at which atoms and molecules absorb, with data on how strong each absorption is.
- Atmospheric retrieval is the process of inferring atmospheric composition and temperature from an observed spectrum.
- Parallelization means splitting a computing job across many processors so it runs faster. · level: research-level

<details><summary>Original abstract</summary>

Detailed studies of exoplanet and brown dwarf atmospheres rely on precise knowledge of the spectral features of possible atmospheric species. These features are a result of the interaction of different molecules and atoms with the radiation of the host star or the intrinsic thermal radiation of the object. The interaction is described by the opacity of a species, which determines how much light is absorbed at a given wavelength. The strength and shape of these opacities are very dependent on the temperature and pressure of the atmosphere, which is why they have to be calculated for a wide range of conditions. line racer is a Python package that enables computing high-resolution opacities from large molecular and atomic line lists in an effective manner. It offers users a wide range of options to customize opacity calculations to their needs and available hardware. The code is designed for efficient parallelization on multi-core and multi-node systems and can produce outputs compatible with popular atmospheric modeling and retrieval tools.

</details>

## High-energy astrophysics

### [Clouds as near-horizon backgrounds in the radio detection of air showers](https://arxiv.org/abs/2611.34399)
*Enrique Huesca Santiago, Giulia Cantarini, Anna Nelles* · `astro-ph.HE` · arXiv:2611.34399v1 · relevance 0.13

- **In one sentence**: The paper proposes that radio signals from human-made transmitters reflected off clouds could form a background that confuses stand-alone radio detection of cosmic-ray and neutrino air showers, and uses a simplified model of cloud reflection strength at MHz frequencies.
- **In plain words**: Scientists detect some high-energy particles from space by listening for the faint radio pulses they create when they hit the atmosphere, and they must filter out radio noise from human sources. This paper suggests that radio waves from human transmitters bouncing off clouds could mimic or mask those pulses. The authors built a simplified model of how strongly clouds reflect radio waves in the MHz range and found such reflections may be detectable, especially when the geometry is nearly horizontal.
- **Why it matters**: If cloud reflections can imitate air-shower signals, detector teams would need to account for them to avoid false signals or wrongly rejected events. The work is a first modelling step, so its size and practical impact are not yet established by the text.
- **Background needed**: - Air showers: cascades of particles produced when a high-energy cosmic ray or neutrino hits the atmosphere.
- Radio detection: these showers emit brief radio pulses (MHz range) that antennas can record, even without other detectors.
- Human-made noise: radio transmitters and electronics that contaminate the signal and must be suppressed.
- Reflection/background: a transmitter's signal bouncing off a cloud could reach the antenna and look like a real pulse.
- Near-horizon geometry: signals arriving at very shallow angles, close to the horizon, which the paper says is where reflections are most detectable.
- The model is simplified and the abstract gives no quantitative results, so the strength of the effect is not established here. · level: research-level

<details><summary>Original abstract</summary>

Stand-alone radio detection of air showers from cosmic rays or neutrinos relies on effective and efficient suppression of human-made noise sources. We propose here that reflections of human- made transmitters on clouds or other atmospheric phenomena, can cause confusion backgrounds that have not been studied previously. Given the absence of prior modelling, we have developed a simplified model for the reflection strength of clouds in the MHz regime. The results indicate that such reflections are, in principle, detectable, in particular in extremely horizontal geometries with typical experimental set-ups.

</details>

### [Constraining the Inner Accretion Geometry of GX 9+9 with Broadband Spectral and Timing Studies](https://arxiv.org/abs/2611.33858)
*Swadesh Chand, Srimanta Banerjee, Hsiang-Kuang Chang et al.* · `astro-ph.HE` · arXiv:2611.33858v1 · relevance 0.12

- **In one sentence**: Broadband X-ray spectral and timing analysis (NICER, NuSTAR, MAXI; 2019 and 2022) of the atoll neutron star GX 9+9, finding reflection features, a truncated inner disk, and an upper limit on the magnetic field of about 3x10^10 G.
- **In plain words**: This paper studies GX 9+9, a neutron star that pulls gas from a companion star, using X-ray telescopes that watched it in 2019 and 2022. The authors fit the combined X-ray spectrum and find signs that hot gas near the star reflects X-rays off the surrounding disk of infalling material. They also find that the disk stops short of the star, and use that to estimate an upper limit on the star's magnetic field.
- **Why it matters**: Measuring how close the inner disk gets to a neutron star, and how strong its magnetic field is, helps test models of how matter falls onto these objects. The magnetic field value is an upper limit inferred under the assumption that the disk is truncated at the magnetospheric radius, so it depends on that model.
- **Background needed**: - Low-mass X-ray binary: a neutron star pulling gas from a companion star, which heats up and emits X-rays.
- Atoll source: a common class of these systems, named after the pattern its brightness traces in colour diagrams.
- Soft state: a spectral state where most X-rays come from the cooler disk and a softer hot component.
- Accretion disk: the rotating ring of infalling gas around the star.
- Reflection: X-rays from the hot region bounce off the disk, leaving a bump and an iron emission line near 6-7 keV.
- Truncated disk: the disk ends at some distance from the star instead of reaching its surface.
- Magnetospheric radius: the distance where the star's magnetic field starts to dominate the flow of gas.
- r_g: gravitational radius, a unit of distance set by the star's mass (about 1.5 km per solar mass).
- Instruments: NICER and NuSTAR are space X-ray telescopes; MAXI monitors the sky for X-ray activity. · level: research-level

<details><summary>Original abstract</summary>

We present a broadband spectral and timing study of the bright atoll neutron star low-mass X-ray binary GX~9+9, using simultaneous NICER, NuSTAR, and MAXI observations from 2019 and 2022. The broadband spectra are well described by a combination of multicolor disk emission, thermal Comptonization of blackbody seed photons from the neutron star surface or boundary layer, and associated disk reflection. We report a clear detection of reflection features in this source, including a moderately broad Fe K$\alpha$ complex and a reflection hump, confirming an earlier detection from a different observation. These features likely arise from the illumination of the moderately ionized disk by thermally Comptonized emission from the boundary layer or warm corona. While the source remained in the soft spectral state during both observations, the 2022 observation exhibits a relatively larger thermal contribution, together with a steeper Comptonized component and lower coronal optical depth. Both reflection and disk-continuum modeling favor a truncated disk, with the latter indicating a smaller inner disk radius in 2022. The inferred radial extent of the boundary layer of $\sim8~r_{\rm g}$ may play a role in the observed disk truncation. Assuming that the disk is truncated at the magnetospheric radius, we obtain an upper limit on the magnetic field strength of $\lesssim3\times10^{10}$ G. Timing analysis reveals a relatively stable disk component and a highly variable Comptonized component, consistent with the typical characteristics of the soft state.

</details>

## Stars and the Sun

### [Investigating the Neupert Effect with HEL1OS/Aditya-L1](https://arxiv.org/abs/2611.34450)
*Srikar Paavan Tadepalli, Abhishekh Kumar Srivastava, K. Sankarasubramanian et al.* · `astro-ph.SR` · arXiv:2611.34450v1 · relevance 0.08

- **In one sentence**: Using HEL1OS hard X-ray spectrograms from Aditya-L1 for 312 solar flares (Nov 2023–May 2026), the authors test the Neupert effect, reporting a median soft–hard X-ray correlation of 0.984 and an empirical forward model that reconstructs the thermal lightcurve from resolved non-thermal energy-release episodes, including quasi-periodic pulsing flares.
- **In plain words**: This paper looks at solar flares, sudden bursts of energy on the Sun. It uses data from an Indian solar satellite's hard X-ray instrument to compare the high-energy X-ray bursts with the slower heating of the hot gas around them. The authors report a very strong match between the two across 312 flares and build a simple model that rebuilds the slower heating curve from the bursts.
- **Why it matters**: The Neupert effect is a long-standing empirical rule about how flares heat plasma, so a large sample testing it with one broadband instrument may help connect flare energy release to the heating that follows. The text does not show how far the empirical model generalises beyond this dataset, so its wider physical meaning is uncertain.
- **Background needed**: - Solar flares: sudden explosive releases of magnetic energy on the Sun, producing X-rays.
- Hard X-rays (high-energy) come mainly from fast, non-thermal electrons hitting the solar atmosphere; soft X-rays come from hot thermal plasma.
- Neupert effect: an observed pattern where the soft X-ray signal roughly tracks the time-integral of the hard X-ray signal.
- Quasi-periodic pulsations (QPPs): repeated brightness oscillations within a flare with a rough but not exact period.
- Aditya-L1: India's solar observatory satellite; HEL1OS is its hard X-ray spectrometer.
- Correlation coefficient: 1 means perfect linear tracking, 0 means no relation. · level: research-level

<details><summary>Original abstract</summary>

We investigate the Neupert effect in solar flares using broadband hard X-ray observations from the HEL1OS instrument onboard Aditya-L1. By separating thermal and non-thermal components from HEL1OS spectrograms, we analyse a sample of 312 flares observed between November 2023 and May 2026. We find that the soft X-ray flux is strongly correlated with the time-integrated hard X-ray emission, with a median correlation coefficient of 0.984, indicating that Neupert-like behaviour is nearly ubiquitous in flares with detectable non-thermal emission. Extending beyond statistical correlation, we develop an empirical forward model in which the thermal lightcurve is reconstructed from the non-thermal emission by resolving the hard X-ray lightcurve into individual energy-release episodes and convolving their fitted profiles with finite thermal-response functions. This approach successfully reproduces the observed thermal evolution, including flares that exhibit quasi-periodic pulsations (QPPs). Our results demonstrate that the broadband HEL1OS observations sample both thermal-dominated and non-thermal-dominated flare emission within a single instrument, providing an observation-driven link between the temporal structure of non-thermal HXR emission and the thermal X-ray response. This provides a different framework for interpreting flare energetics and temporal evolution using broadband hard X-ray measurements.

</details>

### [Evidence for an Evolving Surface on the Partly Burnt Runaway Stellar Remnant GD 492](https://arxiv.org/abs/2611.33301)
*Reuben Dsouza, J. J. Hermes, Boris T. G\"ansicke et al.* · `astro-ph.SR` · arXiv:2611.33301v1 · relevance 0.08

- **In one sentence**: Analysis of 12 TESS sectors of photometry shows that the 8.9-hour brightness modulation of the partly burnt hypervelocity runaway remnant GD 492 changes in period and shape on timescales of one to two months, which the authors attribute qualitatively to evolving surface spots.
- **In plain words**: GD 492 is a dense leftover star that was flung away at very high speed, and it may be the survivor of an exploding star. Earlier work reported that its brightness rises and falls about every 8.9 hours. Using more than four years of satellite brightness measurements, the authors find that this cycle drifts over time, and that a simple two-spot model with shifting surface features can roughly reproduce the changing patterns.
- **Why it matters**: If the brightness changes come from surface features, they could help constrain the star's outer convective layers and how to interpret its unusual chemical composition. The text does not establish how strongly this bears on the wider picture, and the spot geometry is not uniquely determined.
- **Background needed**: - A white dwarf is the dense, Earth-sized core left after a star like the Sun runs out of fuel; GD 492 is a partly burnt remnant, meaning its outer layers show signs of nuclear processing.
- A "hypervelocity runaway" is a star moving fast enough to escape its home galaxy, usually after a binary companion is destroyed or a stellar explosion.
- A thermonuclear supernova is a stellar explosion driven by runaway nuclear fusion.
- TESS is a NASA satellite that measures star brightness over time (photometry); a "sector" is roughly a 27-day observing window.
- A photometric modulation is a regular brightness variation, here interpreted as a rotating star with uneven surface markings, similar to starspots on the Sun.
- Differential rotation means different latitudes spin at different rates; the paper suggests this may contribute to the changes. · level: research-level

<details><summary>Original abstract</summary>

GD 492 (LP 40-365) is a partly burnt, hypervelocity runaway stellar remnant thought to have survived a thermonuclear supernova. We analyze 12 sectors of TESS photometry spanning more than four years to investigate the previously reported 8.9-hr photometric modulation of the star. We find that the modulation changes with time, with individual-sector fits yielding apparent periods ranging from 8.8606 to 8.9048 hr (0.5% changes), more than 25 times the formal measurement uncertainties. Both the period and shape of the modulation evolve on a timescales of approximately one to two months. We show qualitatively that a two-spot model with evolving surface structure can reproduce several of the observed light-curve morphologies, although the geometry of the spots is not uniquely constrained. These observations suggest that changing surface inhomogeneities are a plausible origin of the photometric variability. Differential rotation and magnetic activity may contribute to this evolution, potentially providing new constraints on the outer convective structure of GD 492 and on the interpretation of its atmospheric abundances.

</details>

## Chemical physics

### [TyxonQ: A Workflow Layer for Quantum Computing in Chemistry](https://arxiv.org/abs/2611.33883)
*Xiaoran Li, Zhi Yin, Zhupeng Han et al.* · `physics.chem-ph` · arXiv:2611.33883v1 · relevance 0.11

- **In one sentence**: TyxonQ is a software workflow layer that wires quantum solvers for selected orbitals or embedded fragments into classical molecular-mechanics, dynamics, and electronic-structure pipelines through defined interfaces, rather than proposing a new hybrid quantum algorithm.
- **In plain words**: Chemists who want to use quantum computers usually have to fit them into a larger chain of calculations: classical simulations of whole molecules, then a smaller quantum calculation on the hard part. This paper describes TyxonQ, a software layer that connects those pieces so existing chemistry tools can call a quantum solver step by step. The authors say they checked correctness, the cost of switching between methods, reproducibility, and portability of outputs on small chemistry examples, and they separate what was actually run from what is only supported in the source code.
- **Why it matters**: Most quantum chemistry work focuses on the quantum algorithm itself, while the text argues that integration with existing industrial workflows is a bottleneck to adoption. The paper is a software and engineering contribution, and the text does not show that it changes any chemical result; its value depends on how well the interfaces work in practice.
- **Background needed**: - Quantum chemistry: computing molecular energies and forces from the electrons' behavior.
- QM/MM: treating a small region with quantum methods and the surroundings with cheaper classical force fields.
- Embedding / active space: choosing a small subset of electrons and orbitals to treat accurately, the rest handled classically.
- Strong correlation: electrons whose behavior cannot be captured by simple single-configuration approximations.
- NISQ devices: today's noisy quantum computers with limited qubits and short circuit depth.
- CCSD / FCI: standard classical solvers for electron correlation, used as reference or fragment solvers.
- Interfaces named in the text: PySCF, ASE, i-PI, OpenMM, LAMMPS, MDI are existing simulation codes. · level: research-level

<details><summary>Original abstract</summary>

Quantum computational chemistry is often framed around a hybrid quantum solver. In practical applications, however, bottlenecks to adoption also lie in the surrounding multiscale workflow. A molecular problem may combine classical molecular mechanics and dynamics, conventional electronic-structure calculations, and a quantum solver for selected orbitals or embedded fragments. This division of work is particularly relevant when a chemically important electronic subspace is strongly correlated. The size of the electronic Hilbert space and the qubit, noise, and circuit-depth constraints of noisy intermediate-scale quantum (NISQ) devices make active-space and embedding choices central to a feasible quantum calculation. The resulting energies and gradients must remain consistent with the surrounding classical simulation. We present TyxonQ, a workflow layer that connects these levels of treatment rather than addressing only the hybrid quantum algorithm. Four integration interfaces link PySCF-compatible energy/force scanners and embedding, solver adapters, simulator and hardware backends, and classical consumers. The implementation combines QM/MM and fragment embedding with conventional CCSD/FCI fragment solvers, variational and sampling-based quantum methods, and adapters for ASE, i-PI, OpenMM, LAMMPS (through i-PI), and MDI. We describe the contracts and audit coverage, and evaluate correctness, switching cost, reproducibility, and artifact portability on small chemistry workflows, distinguishing executed paths from source-level support. The purpose of TyxonQ is to support incremental integration of quantum calculations into existing computational chemistry workflows, including those used in industry, while retaining appropriate classical treatments elsewhere.

</details>

### [Automatic dual basis sets for self-consistent field calculations](https://arxiv.org/abs/2611.34694)
*Joonatan Huhtasalo, Susi Lehtola* · `physics.chem-ph` · arXiv:2611.34694v1 · relevance 0.10

- **In one sentence**: The paper presents an algorithm that automatically builds a smaller "dual basis" of orbital functions from a target basis, given a precision threshold and a Fock matrix, to speed up convergence of self-consistent field (SCF) calculations in density functional theory.
- **In plain words**: Computing how electrons are arranged in a molecule or solid is done by repeatedly refining an answer until it stops changing, and each round is expensive. This paper looks at making the early rounds cheaper by first solving the problem in a smaller set of mathematical building blocks, then using that rough answer to start the full calculation. The authors built a method to pick these smaller sets automatically rather than by hand.
- **Why it matters**: Faster convergence of electronic-structure calculations matters for large-scale simulations, including the machine-learning and big-data work the abstract mentions. The authors' own conclusion is cautious: the starting guesses currently available are not accurate enough for adaptive basis sets to pay off, and they suspect the same limit may apply to similar basis-compression approaches.
- **Background needed**: - Density functional theory (DFT): a standard quantum-chemistry method for estimating electron distributions and energies in atoms, molecules and materials.
- Self-consistent field (SCF) problem: the calculation is repeated, each time updating the electron picture, until it no longer changes.
- Basis set: the fixed collection of mathematical functions used to represent orbitals; larger sets are more accurate but more costly.
- Polarized triple-zeta basis: a high-quality, fairly large basis set needed for quantitative accuracy.
- Fock matrix: the matrix encoding the effective energy operator for electrons; its initial guess determines how quickly SCF converges.
- Periodic table periods 1–4: the first four rows, covering hydrogen through krypton. · level: research-level

<details><summary>Original abstract</summary>

Density functional theory (DFT) has long been the workhorse of electronic structure theory, and it is experiencing a new boom thanks to big data applications and machine learning. A DFT calculation requires the iterative solution of the self-consistent field (SCF) problem, whose cost is the product of (i) the number of SCF steps and (ii) the cost of a single step. The number of SCF steps depends strongly on the initial guess, regardless of the SCF algorithm, and quantitative DFT accuracy is known to require at least a polarized triple-$\zeta$ basis set. However, a qualitatively correct solution may often be found already in a smaller \emph{dual basis} (DB), which can then bootstrap a calculation in the full basis set. Traditionally, the DB is chosen by hand for each application to enable robust convergence to the ground state. In this work, we pursue automatic generation of DBs for SCF calculations. Our generator constructs a pruned orbital basis from the target orbital basis for a predefined precision threshold and a given Fock matrix. As expected, the larger the basis set is, the smaller the fraction of kept basis functions. The DBs produced by our algorithm exhibit similar performance for a wide range of systems from the first 4 periods of the periodic table. Ultimately, we find that presently available initial guesses for the Fock matrix are not accurate enough to unlock the use of adaptive basis sets, and believe that the same limitation may hold for similar attempts for basis compactification.

</details>

## Materials science

### [Brightening spin- and parity-forbidden interlayer excitons through rhombohedral stacking](https://arxiv.org/abs/2611.34900)
*Haodong Hu, Chih-En Hsu, Kenji Watanabe et al.* · `cond-mat.mes-hall` · arXiv:2611.34900v1 · relevance 0.10

- **In one sentence**: Rhombohedral (3R) stacking of a MoS2 bilayer is reported to brighten two normally optically forbidden interlayer excitons, a spin-unlike 1s state and a parity-odd 2p state, and to reveal a gauge-invariant phase contrast in the hybridized 2p exciton via quantum interference.
- **In plain words**: Excitons are bound pairs of an electron and a "hole" (a missing electron) that carry light in semiconductors. In this paper, the authors stack two layers of molybdenum disulfide, a very thin material, in a specific rhombohedral arrangement, which makes two kinds of excitons that normally cannot absorb or emit light become visible optically. They identify these excitons using their magnetic response (g-factors) and by tuning them into resonance with ordinary excitons, where they mix.
- **Why it matters**: The work suggests that the way atomically thin layers are stacked can be used as a control knob for the quantum states of excitons, which may matter for future optical or quantum devices. The text does not show direct device applications, so the practical reach is not established here.
- **Background needed**: - Excitons: electron-hole pairs bound together, acting like light-matter particles in semiconductors.
- Symmetry-forbidden: transitions that selection rules block, so they normally do not absorb or emit light.
- Interlayer exciton: the electron and hole sit in different atomic layers.
- Stacking (3R/rhombohedral): the way successive atomic layers are shifted relative to each other; it changes the material's electronic behavior.
- g-factor: a measure of how an energy level shifts in a magnetic field, used here as a fingerprint of the exciton's spin character.
- Hybridization and quantum interference: when two states mix, their contributions can add or cancel, similar to overlapping waves.
- 1s and 2p: labels for exciton energy levels, analogous to atomic orbitals; "parity-odd" means the wavefunction changes sign under spatial inversion. · level: research-level

<details><summary>Original abstract</summary>

Brightened symmetry-forbidden excitons can provide critical information about the electronic structure and many-body interactions in semiconductors. Recently, interlayer atomic registry has emerged as a new way to control atomically thin layered materials in both ground and excited states. Here we show that the rhombohedral stacking in a 3R-MoS_2 homobilayer can brighten two symmetry-forbidden interlayer excitons: one is a spin-unlike 1s exciton and the other is a parity-odd 2p exciton. The nature of these interlayer excitons is revealed by their gfactors as well as the hybridization patterns observed when they are tuned to resonate with intralayer excitons. Surprisingly, the hybridized 2p exciton exhibits a constructive quantum interference between the acquired transition dipoles, revealing a hidden gauge-invariant phase contrast between the constituent electronic states. Our results establish stacking control as a powerful approach for modulating quantum phases of excitons in 2D semiconductors.

</details>

### [Unveiling ferroelectricity in wafer-scale beta-phase In$_2$Se$_3$](https://arxiv.org/abs/2611.33405)
*Kyungmin Yang, Hyunmin Cho, Jihwan Jeon et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33405v1 · relevance 0.09

- **In one sentence**: The paper reports bistable out-of-plane and in-plane polar order in van der Waals beta-phase In2Se3, arising from a picometre-scale distortion within each quintuple layer, persisting down to a ~1.9 nm bilayer, and demonstrated in wafer-scale MOCVD films with capacitor and transistor devices.
- **In plain words**: Ferroelectric materials can hold an electric polarization that flips when a voltage is applied, which could store bits in memory chips. Usually these materials stop working when made very thin. This paper argues that a layered semiconductor, beta-indium selenide, which was thought to lack this property, has a tiny built-in shift in its atomic layers that can be flipped, and that it still works at about two nanometres thick.
- **Why it matters**: The text reports that switching remains possible at the bilayer limit and that 2-inch wafer films gave capacitor arrays with under 5% switching-voltage spread across 100 devices, which bears on whether ultrathin memory could be manufactured at scale. The text does not show how these results compare with existing memory technologies, and the reported polarization is described only as "apparent," so its significance is still to be judged.
- **Background needed**: - Ferroelectric: a material whose internal electric polarization can be reversed by an applied electric field, and which keeps its state without power.
- Remanent polarization and coercive field: the leftover polarization after the field is removed, and the field strength needed to flip it.
- Centrosymmetric: a crystal whose structure looks the same after inversion through a central point, which normally rules out such polarization.
- van der Waals semiconductor: a layered material whose sheets are held together by weak forces, making very thin single or few-layer films possible.
- Quintuple layer: a five-atom-thick sheet unit that forms the building block of this layered crystal.
- Picometre: one trillionth of a metre; the distortion described is extremely small.
- MOCVD (metal-organic chemical vapor deposition): a standard industrial method for growing thin films on wafers.
- Endurance and retention: how many switching cycles a device survives and how long stored states last. · level: research-level

<details><summary>Original abstract</summary>

Pushing ferroelectricity to the ultimate thickness limit is a central challenge for memory hardware, because conventional three-dimensional ferroelectrics degrade through depolarization and interfacial effects when thinned. Here we identify $\beta$-In$_2$Se$_3$, a van der Waals semiconductor regarded as centrosymmetric, as a host of bistable polar order arising from a picometre-scale distortion within each quintuple layer. The polar state has out-of-plane and in-plane components, is switched by a vertical electric field, and persists to the bilayer limit (~1.9 nm) with an estimated coercive field of 0.9 MV/cm and an apparent remanent polarization of 11.0 $\mu$C/cm$^2$. Films grown by metal-organic chemical vapor deposition on 2-inch wafers yield capacitor arrays with a switching-voltage spread below 5% across 100 devices, an endurance of $10^7$ cycles and a projected ten-year retention. Because the polar state coexists with a semiconducting gap, one film serves as both the switching layer of a capacitor and the channel of a ferroelectric semiconductor transistor.

</details>

## Soft matter and polymers

### [A Thermodynamically Consistent Model of a Rechargeable Salt-in-Polyelectrolyte Battery](https://arxiv.org/abs/2611.34415)
*Charlotte Beckford, Rajeev Kumar, Steven M. Wise* · `cond-mat.soft` · arXiv:2611.34415v1 · relevance 0.09

- **In one sentence**: A thermodynamically consistent, isothermal one-dimensional model of a rechargeable battery whose electrolyte is a polyelectrolyte (charged polymer) with lithium-type counterions plus optional added salt, with interfacial cation intercalation and Butler–Volmer kinetics, reducing to dual-ion-conductor and single-ion-conductor limiting cases and compared via galvanostatic simulations.
- **In plain words**: This paper builds a mathematical model of a battery in which the electrolyte is a charged polymer that carries lithium-type ions, with or without extra dissolved salt. The authors describe how ions move, how they enter and leave the electrodes, and how the battery charges and discharges under a constant current. They then simulate two simplified versions of the battery and compare how ion concentrations shift, how much the voltage is pulled away from its ideal value, and how much of the electrode gets used.
- **Why it matters**: Polymer electrolytes are of interest for safer or more flexible batteries, and a model that is built to obey thermodynamic rules gives a consistent framework for comparing designs. The text reports numerical checks and simulations but does not state experimental validation or a claimed performance gain, so its practical significance is unclear from the summary alone.
- **Background needed**: - Electrolyte: the material that carries electric charge between battery electrodes as ions.
- Polyelectrolyte: a polymer with charged groups along its chain; here the chain is negatively charged and balanced by lithium-type positive ions.
- Salt-in-polymer vs. single-ion conductor: in one case mobile ions come from added salt plus a neutral polymer; in the other only the charged polymer's counterions move.
- Intercalation: ions inserting into and leaving the crystal structure of an electrode material.
- Galvanostatic: charging or discharging at a fixed current.
- Butler–Volmer equation: a standard formula relating electrode reaction speed to voltage driving force.
- Fick's law: diffusion model where particles spread from high to low concentration at a rate set by a diffusion coefficient.
- Thermodynamic consistency: the model respects energy and entropy rules, so it does not create or destroy free energy.
- Discretization: splitting space and time into small steps for computer solution. · level: research-level

<details><summary>Original abstract</summary>

We present an isothermal, thermodynamically consistent model of a salt-in-polyelectrolyte battery with intercalation and deintercalation reactions of cations occurring at the electrode-electrolyte interfaces under galvanostatic conditions. For the electrolyte, we consider polyelectrolytes, which are polyanions, with neutralizing cations (i.e., counterions) such as lithium, along with a monovalent salt containing the same cations. Models of batteries containing either a dual-ion-conductor (DIC) electrolyte (i.e., uncharged polymers with added salt) or a single-ion-conductor (SIC) electrolyte (i.e., charged polymers without added salt) emerge as limiting cases of this thermodynamically consistent model. Once the model is presented in its most general context, we make specific choices so that it captures well-known mechanisms. In particular, the governing diffusion equations recover Fick's law of diffusion, and the cation-transfer reaction rate is described by the Butler--Volmer equation. The DIC and SIC limiting cases provide a framework for comparing the corresponding batteries. One-dimensional DIC and SIC charge--discharge simulations at matched current and duration illustrate concentration redistribution, polarization, and electrode utilization. Numerical accuracy checks quantify sensitivity to discretization; distinct initial inventories qualify the comparison.

</details>

### [Discotic columnar phase in a three-dimensional monomer-tetramer model of Heilmann and Lieb with side-to-side attraction](https://arxiv.org/abs/2611.34796)
*Qidong He* · `math-ph` · arXiv:2611.34796v1 · relevance 0.08

- **In one sentence**: This paper proves that a three-dimensional lattice model of tetramers (plaquettes) with hard-core repulsion and side-to-side attraction, a variant of the Heilmann–Lieb model, has discotic columnar order at low temperature whenever μ+2a>0, by identifying exactly twelve periodic extremal Gibbs measures.</one_liner>
<parameter name="plain">This is a mathematical study of a simplified model of a liquid crystal, in which flat disk-like units sit on a grid and pack together. The authors show that, at low temperature and under a stated condition on the chemical potential and attraction strength, the units stack into one-dimensional columns arranged in a square pattern. The energy alone only forces layers, and the paper's main point is that thermal fluctuations select the states where all units share the same parity (alignment of their offset).
- **Why it matters**: The paper settles a conjecture from 1979 about whether this model orders at low temperature, so it resolves a long-open question for this specific model. Its link to real disk-shaped liquid crystals is suggested by the model's design rather than shown directly in the text, so any wider application should be treated as unverified.
- **Background needed**: - Liquid crystals: states of matter between a liquid and a solid, where molecules have some orientational order.
- Discotic phase: molecules shaped like flat disks that stack into columns.
- Lattice model: units placed on the sites of a grid, with simple rules for how neighbours interact.
- Tetramer/plaquette: a unit made of four grid cells forming a small flat square.
- Hard-core repulsion: two units cannot overlap; lateral attraction: coplanar, aligned units stick side to side.
- Chemical potential μ: a knob controlling how many units are present on average.
- Gibbs measure: a probability distribution describing the random arrangement at a given temperature; extremal ones are the "pure" phases, and breaking symmetry means the arrangement picks a preferred direction or offset.
- Ground state: the lowest-energy arrangement; here the energy alone allows layers to slide independently, so temperature decides the outcome. · level: research-level

<details><summary>Original abstract</summary>

We study Model III of Heilmann--Lieb (1979), a lattice model for liquid crystals consisting of tetramers (plaquettes) on the cubic lattice at chemical potential $\mu$, interacting via a hard-core repulsion and a lateral attraction of strength $a>0$ between coplanar, aligned tetramers. The model was conjectured to exhibit liquid-crystalline order at low temperature provided that $\mu+2a>0$. We establish discotic columnar order throughout this regime, fully resolving the conjecture. Specifically, we prove the existence of exactly twelve extremal and periodic Gibbs measures, each breaking rotational symmetry, with one of three tetramer orientations dominant, and translational symmetry in exactly two directions, with one of four tetramer parities dominant within that orientation. Thus, the tetramers form one-dimensional columns arranged on a square lattice. This arrangement is not a priori evident from the zero-temperature picture, where energy only enforces a layered structure: each layer is fully packed and crystalline, but different layers are free to shift independently within their planes. The main novelty here lies in showing how thermal fluctuations lift this degeneracy in favor of the twelve ground states in which all tetramers share a common parity.

</details>

## AI for chemistry and materials

### [Temporal Selective Exploration for Reinforcement Learning-Guided Continuous-Discrete Flow Matching in 3D Molecular Design](https://arxiv.org/abs/2611.33417)
*Lianghong Chen, Yan Yi Li, Gen Zhou et al.* · `cs.LG` · arXiv:2611.33417v1 · relevance 0.22

- **In one sentence**: A reinforcement-learning method that fine-tunes a continuous-discrete flow-matching generative model for 3D de novo molecular design, restricting exploration to influential timesteps and calibrating rewards across multiple objectives, applied to EGFR and Pin1 inhibitor design.
- **In plain words**: This paper is about using AI to design new 3D molecules that could block specific proteins linked to disease, here EGFR and Pin1. The authors train a generative model that places atoms in space and chooses which atoms they are, and they use reinforcement learning, a trial-and-reward training approach, to steer it toward molecules with desired properties. They report identifying some novel candidate inhibitors, supported only by computer-based (in silico) checks.
- **Why it matters**: Designing drug candidates with generative AI is an active area, and the paper tackles two practical training problems: wasted random exploration at unimportant steps and one objective overpowering the others. Whether the candidates are actually useful is unknown from this text, since the validation is computational only and no experimental results are described.
- **Background needed**: - Generative model: software that learns to produce new examples, here molecules, from patterns in data.
- Flow matching: a method that learns a smooth path turning random noise into a valid output over a series of steps.
- Continuous vs. discrete: atom positions are continuous numbers; atom types (e.g., carbon, nitrogen) are discrete choices.
- Reinforcement learning (RL): training by trying outputs and adjusting toward higher scores from a reward function.
- ODE vs. SDE: a deterministic versus a randomized step-by-step process; randomness is needed so RL can explore.
- Multi-objective optimization: balancing several goals at once, such as binding strength and drug-likeness.
- EGFR and Pin1: protein targets associated with disease; inhibitors are molecules that block them.
- In silico: performed by computer simulation rather than in a lab. · level: research-level
- Matched keywords: molecular, protein

<details><summary>Original abstract</summary>

Flow matching has shown strong potential in generative tasks, while its optimization via Reinforcement Learning (RL) remains underexplored, especially in continuous-discrete mixed settings. Moreover, flow matching is formulated as an Ordinary Differential Equation (ODE), whose deterministic trajectories do not naturally support RL optimization. Introducing stochasticity by converting the entire trajectory into a Stochastic Differential Equation (SDE) is a common practice. Nevertheless, not all timesteps contribute to the final outcomes, and redundant exploration introduces additional noise. Furthermore, in multi-objective settings, some objectives may dominate the optimization while others receive insufficient updates. In this study, we propose an RL-guided continuous-discrete flow matching framework with temporal selective exploration for 3D de novo molecular design. Specifically, our method jointly optimizes continuous and discrete flow matching for atomic coordinates and molecular identities, respectively, while restricting exploration to timesteps that primarily contribute to target properties, reducing ineffective exploration. We also introduce a reward-based advantage calibration mechanism to mitigate objective dominance in multi-objective optimization. The framework is applied to design inhibitors for both the well-studied target protein EGFR and the challenging Pin1 protein. We identify some novel candidate inhibitors, supported by in silico validation.

</details>

### [PerovAgent: Autonomous Ligand Design for Halide Perovskite Nanocrystals](https://arxiv.org/abs/2611.33913)
*Seungjun Cha, Yoo Jae Jeong, Amanda Conde Del Moral et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33913v1 · relevance 0.21

- **In one sentence**: PerovAgent is an LLM-driven multi-agent framework that autonomously designs surface-capping ligands for CsPbBr3 perovskite nanocrystals, optimizing a binding-energy objective and testing LLM-generated design principles statistically, with a DFT check on one principle.
- **In plain words**: Tiny crystal particles called perovskite nanocrystals are coated with molecules, called ligands, that help them work well in devices. Choosing those coating molecules is a huge search problem. This paper describes an AI system that uses a language model to propose and test ligand ideas automatically, combining chemistry simulation tools and statistical checks.
- **Why it matters**: It shows an AI system that does not just search for a better molecule but also turns its search results into rules that can be checked, which is useful for anyone thinking about automated scientific discovery. The text reports 35 principles, of which 19 were prospectively supported and 7 passed a confound audit; whether these rules hold up more broadly is not shown here.
- **Background needed**: - Halide perovskite nanocrystals: tiny light-emitting or light-absorbing crystal particles used in displays and solar cells.
- Surface-capping ligands: molecules bonded to a particle's surface that control its stability and properties.
- Binding energy: a computed measure of how strongly a molecule sticks to a surface; lower (more negative) usually means stronger binding.
- Large language model (LLM) agents: AI systems that reason in text and call software tools in a loop.
- Machine-learned interatomic potential: a fast learned approximation of atomic forces, used instead of slower quantum calculations.
- Density functional theory (DFT): a standard quantum-mechanical simulation method used here to check one result.
- Confound audit: a check that a pattern is not explained by a hidden variable rather than the chemistry itself. · level: research-level
- Matched keywords: molecular, interatomic potential

<details><summary>Original abstract</summary>

Designing surface-capping ligands for high-performance halide perovskite nanocrystals requires navigating a vast molecular space while discovering design rules that govern ligand-surface interactions. Here, we introduce PerovAgent, an autonomous multi-agent framework that combines large language model (LLM)-driven scientific reasoning with computational tools for atomistic model construction, machine-learned interatomic potential evaluation, and statistical validation. Across ten independent campaigns on CsPbBr3 surfaces, PerovAgent adaptively explored and refined diverse ligand chemistries while progressively improving the binding-energy objective. Beyond optimization, the framework converts recurring chemical observations into explicit design principles that can be statistically evaluated. Of 35 formulated principles, 19 were prospectively supported, of which seven also passed the confound audit, highlighting the need to systematically validate plausible LLM-generated hypotheses during autonomous discovery. A recurrent alkynyl-phosphonate principle was further examined using density functional theory, which reproduced the predicted energetic preference. These results demonstrate an autonomous discovery framework that not only searches molecular space and optimizes the scalar objective but also transforms its search trajectory into systematically testable design principles. The framework can also be extended to more complex ligands, including zwitterionic, multidentate, and polymerizable ligands, to explore a wider range of ligand-surface interactions and uncover new design principles for halide perovskite nanocrystals.

</details>

## Biochemistry

### [Identification of Functional NOD2-Specific Aptamers Using APT-SNAP Microarrays to Screen Zebrafish Nod-like Receptors](https://www.biorxiv.org/content/10.64898/2026.11.24.768724v1)
*Messa, P. E.; Pearson, K. S.; Conti, B. J. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.768724 v1 · relevance 0.06

- **In one sentence**: The paper reports DNA aptamers, selected with the high-density APT-SNAP microarray platform, that bind zebrafish NOD2 and several other zebrafish NOD-like receptors, and validates the lead NOD2 binders with ELASA, pull-down, biolayer interferometry and fluorescence microscopy.
- **In plain words**: Scientists studying the immune system need reliable tools that grab onto specific proteins so they can be seen and measured. For zebrafish, a common research animal, good antibodies for a family of immune sensors called NOD-like receptors are scarce. The authors used a microarray screen to find short DNA sequences (aptamers) that stick to these zebrafish proteins, then tested the best candidates for NOD2 in several lab assays.
- **Why it matters**: Reliable detection reagents are a practical bottleneck for studying immune sensors that are linked to inflammatory disease and cancer, so a validated set of NOD2 binders could make zebrafish work easier. The text describes the approach as generalizable to other hard-to-target proteins, but it does not test that claim beyond this one family, so its broader reach remains untested here.
- **Background needed**: - NOD-like receptors (NLRs): proteins inside cells that detect signs of microbial invasion or tissue damage and switch on immune responses.
- Zebrafish (Danio rerio): a small freshwater fish widely used in biology because it is transparent and easy to study genetically.
- Antibodies: protein tools that bind a target molecule; used for detection but can fail for some targets.
- Aptamers: short single-stranded DNA or RNA molecules that fold into shapes that bind a target, acting as synthetic alternatives to antibodies.
- Microarray: a glass or chip surface carrying many different molecules at once, allowing thousands of binding tests in parallel.
- Affinity and specificity: how tightly a reagent binds its target and how little it binds other things.
- Biolayer interferometry (BLI): a light-based method for measuring how strongly two molecules bind in real time.
- Pull-down: a method that uses a bait molecule to fish its partners out of a mixture for detection. · level: research-level

<details><summary>Original abstract</summary>

NOD-like receptors (NLRs) are intracellular immune sensors that monitor for pathogen- and damage-associated molecular patterns (PAMPs, DAMPs) and initiate innate immune signaling pathways upon detection. Dysregulation of NLR signaling contributes to numerous inflammatory diseases and cancers, yet mechanistic studies of NLR proteins are limited by the availability of reliable detection reagents, particularly in emerging model organisms such as zebrafish (Danio rerio). Although zebrafish provide a powerful system for studying innate immunity, few validated antibodies exist for zebrafish NLR proteins. Here, we describe the development of aptamer-based detection reagents targeting zebrafish NLRs using the APT-SNAP platform, a high-density aptamer microarray technology that enables rapid identification of protein-binding nucleic acid ligands. Using this approach, we identified multiple DNA aptamers that bind zebrafish NLR proteins and selected candidates targeting NOD2 for further characterization. Orthogonal validation assays, which include enzyme-linked apta-sorbent assays (ELASAs), pull-downs, biolayer interferometry (BLI), and fluorescence microscopy, confirmed that the lead aptamers bind zebrafish NOD2 with high affinity and specificity, and function effectively in biochemical and cellular assays. These results demonstrate that APT-SNAP generated validated, native-state affinity reagents for a zebrafish immune protein where commercial antibodies failed, providing new molecular tools for investigating NLR biology in zebrafish. More broadly, this strategy establishes a generalizable approach for generating affinity reagents against challenging protein targets that lack reliable antibodies.

</details>

### [Antifungal and Antibiofilm Activity of a Thermostable Lipid Transfer Protein-Enriched Fraction from Capsicum annuum L. Seeds against Candidozyma auris](https://www.biorxiv.org/content/10.64898/2026.11.24.768040v1)
*Vera Gonzalez, S. M.; Larrondo, C.; Claver, S. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.768040 v1 · relevance 0.05

- **In one sentence**: A heat-stable, lipid-transfer-protein-enriched fraction from Capsicum annuum (pepper) seeds shows antifungal and antibiofilm activity against multidrug-resistant Candidozyma auris and other Candida species in laboratory tests.
- **In plain words**: Candidozyma auris is a yeast that can cause serious hospital infections and often resists common antifungal drugs. The researchers took a water extract of pepper seeds, heated it to keep only the heat-tolerant parts, and found that the leftover fraction was rich in two small plant proteins, Ca-nsLTP1 and Ca-nsLTP2. In lab dishes, this fraction slowed or killed several Candida and C. auris strains, including some that did not respond to fluconazole, and it also reduced yeast films (biofilms) on surfaces.
- **Why it matters**: Drug-resistant fungal infections are hard to treat, so new molecules with different mechanisms are of interest. The text is limited to lab results with a fraction rather than purified proteins, and it does not show whether this works in people or animals, so its practical value is still unknown.
- **Background needed**: - Candidozyma auris (formerly Candida auris): a drug-resistant yeast that causes hospital outbreaks.
- Antifungal: a substance that kills or stops fungi.
- MIC (minimum inhibitory concentration): the lowest amount that stops growth; MFC: the lowest amount that kills the fungus.
- Biofilm: a sticky, layered community of cells attached to a surface, which is harder to kill than single cells.
- Lipid transfer proteins (nsLTPs): small plant proteins that bind fatty molecules; some plant nsLTPs have antimicrobial effects.
- Heat-treated fraction: a portion of an extract that survives heating, here used to concentrate the small proteins.
- Trypsin inhibition: the fraction also blocks an enzyme, trypsin, in a lab assay.
- Fluconazole: a common antifungal drug to which some C. auris strains are resistant. · level: intermediate

<details><summary>Original abstract</summary>

The emergence of multidrug-resistant Candidozyma auris (C. auris) has intensified the search for antifungal molecules with alternative structures and mechanisms of action. Here, we investigated Capsicum annuum L. seeds as a source of thermostable antifungal peptides. Thermal fractionation of a crude aqueous seed extract (RBPCE) yielded a heat-treated fraction (RBPHT) enriched in low-molecular-weight proteins. LC-MS/MS identified the type I and type II non-specific lipid-transfer proteins Ca-nsLTP1 and Ca-nsLTP2 as its predominant constituents. Compared with RBPCE, RBPHT displayed increased trypsin-inhibitory potency. RBPHT inhibited C. albicans, C. krusei, and C. auris isolates from clades I, III, and IV, including isolates showing no detectable response to fluconazole under the conditions tested. Against a representative South American clade IV isolate, the nsLTP-enriched fraction exhibited minimum inhibitory and fungicidal concentrations of 180 and 360 g/mL, respectively. RBPHT also suppressed early biofilm establishment by C. albicans and C. auris and markedly reduced viable biofilm-associated populations when applied after initial cell adhesion. These findings provide the first evidence of antifungal and antibiofilm activity by a Capsicum seed-derived nsLTP-enriched fraction against C. auris and position Ca-nsLTP1 and Ca-nsLTP2 as promising plant-derived candidates for further antifungal development.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Structural deformations of lipid bilayers around membrane proteins inform oligomerization type](https://www.biorxiv.org/content/10.64898/2026.11.24.769041v1)
*Diaz Vazquez, G.; Condon, S. G. F.; Robertson, J. L.* · `biophysics` · bioRxiv doi:10.64898/2026.11.24.769041 v1 · relevance 0.08

- **In one sentence**: Coarse-grained molecular dynamics simulations of monomeric and oligomeric forms of ten membrane channels and transporters in POPC bilayers compare membrane thickness, deformation energy and lipid packing near protein-protein interfaces to test whether these lipid defects relate to oligomerization type.
- **In plain words**: Cell membranes are made of fatty lipid sheets, and proteins embedded in them can bend and thin the surrounding sheet. This computational study simulated ten channel and transporter proteins, alone and assembled into groups, to see how the membrane around them is disturbed. The authors report that disturbances reach about 3 nm from each protein, and that proteins which always assemble the same way show larger disturbances at their contact surfaces, which become smaller when they join.
- **Why it matters**: The work proposes that the shape of the membrane around a protein may help determine which partners it binds and how strongly, a link that could matter for understanding how membrane protein complexes form. The text does not show how these simulation findings would be tested experimentally, so their wider significance remains uncertain.
- **Background needed**: - Biological membranes are double layers of lipids (fat-like molecules) that act as a barrier around cells.
- Membrane proteins sit inside this layer; channels and transporters move molecules across it.
- Oligomerization means several copies of a protein joining into one complex.
- Coarse-grained molecular dynamics is a simulation method that groups atoms into larger beads to model how molecules move over time.
- Membrane thickness, deformation energy and lipid packing parameter are measures of how strained or disordered the lipid layer is near a protein.
- POPC is a common lab lipid used as a simplified membrane model.
- "Obligatory" or "structurally monomorphic" complexes always assemble in the same arrangement; homologs are related proteins from different species. · level: research-level

<details><summary>Original abstract</summary>

A functional definition of a membrane protein's structure is the three-dimensional arrangement of the polypeptide and the structure of the membrane around it. Biological membranes are composed of self-assembled lipid bilayers, with membrane proteins acting as inclusions that perturb this phase. These inclusions induce long-range changes in membrane structure and create an intrinsic, lipid-mediated driving force for membrane protein association. The question is how much different membrane protein folds shape their surrounding membrane to tune the affinity and specificity of this driving force. To investigate this, we conducted a computational study to evaluate whether different membrane protein oligomers exhibit characteristic membrane defects that indicate specificity in complexation. We performed coarse-grained molecular dynamics simulations of monomeric and oligomeric states of ten different channels and transporters in POPC bilayers and evaluated changes in membrane thickness, deformation energy, and lipid packing parameters. We found that all the proteins affect their surrounding membrane up to 3 nm from the protein surface. However, we observed larger defects at oligomeric interfaces for obligatory or structurally monomorphic complexes, suggesting that their oligomerization is partly driven by burial of membrane defects. In contrast, oligomers that adopt different quaternary structures across homologs show weaker perturbations at known binding interfaces, and larger perturbations at lipid-facing surfaces. Nevertheless, all systems show fewer membrane defects upon oligomerization, suggesting an underlying lipid-mediated driving force that each protein fold modulates to tune affinity via membrane-mediated oligomerization.

</details>

### [A spatiotemporal perturbational atlas of the post-pneumonectomy lung](https://www.biorxiv.org/content/10.64898/2026.11.25.768918v1)
*Obata, T.; Aracena, D. P.; Tomas Gracia, M. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.25.768918 v1 · relevance 0.08

- **In one sentence**: A multi-method atlas (single-cell RNA sequencing, Xenium spatial transcriptomics, and NICHES-based spatial connectomics) mapping cell composition and intercellular signaling across days 3, 7 and 14 after pneumonectomy (lung removal) in rats.
- **In plain words**: When one lung is surgically removed, the remaining lung grows and reorganizes itself. This paper follows that repair process in rats over several days, looking at which cell types are present and how they appear to communicate in different parts of the tissue. The authors report three different tissue patterns at successive time points, rather than a single steady process.
- **Why it matters**: Understanding how lung tissue remodels after major injury could inform regenerative medicine and lung disease research, but the text is a short abstract and the connection to human treatment is not shown here. The paper also presents a spatial connectomics analysis framework that may be reusable in other tissues.
- **Background needed**: - Pneumonectomy: surgical removal of an entire lung; the remaining lung must adapt and regrow.
- Single-cell RNA sequencing: measures which genes are active in individual cells, used to identify cell types.
- Spatial transcriptomics (Xenium): measures gene activity while keeping each cell's location in the tissue.
- Connectomics here means mapping likely cell-to-cell signaling (who may be sending signals to whom), not neural wiring.
- Mesothelium: the thin protective lining over the lung surface.
- Macrophages: immune cells that clear debris and help direct tissue repair.
- Fibrosis: excessive scar-like tissue buildup; "fibrosis-mimetic" signaling refers to signals resembling those seen in fibrosis.
- Alveologenic: relating to formation of new alveoli, the tiny air sacs where gas exchange occurs.
- Perturbational atlas: a map of tissue changes measured after a deliberate disturbance over time. · level: research-level

<details><summary>Original abstract</summary>

Perturbational spatial atlases have begun to map regenerative dynamics in a variety of tissues, yet lung remodeling has not been characterized at comparable spatial and temporal resolution. Post-pneumonectomy lung regeneration (PPLR) provides a tractable mammalian model for tissue regeneration that can be studied in situ. Here, we present a spatiotemporal perturbational atlas of PPLR in Rattus norvegicus, combining single-cell RNA sequencing (scRNAseq), high-resolution spatial transcriptomics (10x Genomics Xenium), and NICHES-based spatial tissue connectomics. We observe three distinct tissue architectures at successive timepoints after pneumonectomy, each characterized by coordinated shifts in local cellular composition and intercellular signaling. At Day 3 (D3), a line of interstitial macrophages colocalizes directly beneath an intact mesothelium among active mechanotransductive and inflammatory signaling. We also observe the unexpected appearance of a transitional remodeling cellular community at D7 which appears largely absent at later timepoints, marked by fibrosis- mimetic signaling. At D14, an alveologenic architecture at distal lung tissue displays a connectivity signature consistent with active de novo growth, distinct from baseline homeostasis. Our findings establish a spatiotemporal map of multicellular architecture during regenerative lung remodeling and introduce a generalizable framework for spatial connectomic analysis to be used in perturbational tissue systems biology.

</details>

## Neuroscience

### [Human iPSC-derived Olfactory Sensory Organoids model olfactory function and drug response](https://www.biorxiv.org/content/10.64898/2026.11.24.769047v1)
*Singh, V.; Pantula, A.; Joshi, K. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.24.769047 v1 · relevance 0.07

- **In one sentence**: Human iPSC-derived olfactory sensory organoids are shown to develop olfactory-like neuronal and glial cell types, spontaneous network bursting, and distinct activity responses to three glioma-relevant kinase inhibitors (Dasatinib, Trametinib, Selumetinib).
- **In plain words**: Drugs given through the nose may reach the brain more directly, but it is not well known how they affect the nasal tissue they pass through. This paper describes lab-grown three-dimensional clumps of human cells, made from reprogrammed stem cells, that resemble developing smell tissue. The authors report that these clumps contain several cell types, show electrical bursts of activity, and respond differently to three cancer-related drugs.
- **Why it matters**: Intranasal delivery is an active approach for treating brain diseases, so a human model of the nasal smell tissue could help check drug side effects before people are exposed. The text does not report clinical testing, and the model's fidelity to real adult olfactory tissue is only compared against a developmental fetal atlas, so its wider usefulness remains to be seen.
- **Background needed**: - Organoid: a small, three-dimensional tissue grown in a dish from stem cells.
- iPSC (induced pluripotent stem cell): an adult cell reprogrammed to an early, flexible state, which can then be guided to become other cell types.
- Olfactory sensory neurons: nerve cells in the nose that detect smells and send signals to the brain.
- Single-nuclei RNA sequencing: a method that reads which genes are active in each cell nucleus, used to identify cell types.
- Kinase inhibitors: drugs that block enzymes (kinases) that drive cell growth; these three are studied in glioma, a brain tumour.
- Network bursting: synchronized bursts of electrical firing across a group of cells, measured as a sign of functional connectivity.
- Intranasal delivery: giving medicine through the nasal passage, a possible route to the brain that bypasses the blood-brain barrier. · level: research-level

<details><summary>Original abstract</summary>

Intranasal drug delivery is being explored as an alternative approach to overcome the blood-brain barrier in the treatment of central nervous system diseases. However, little is known about how therapeutics administered through this route affect human olfactory tissue. Here, we develop human induced pluripotent stem cell-derived olfactory sensory organoids that reproduce key cellular and functional features of the developing olfactory system. Over three months of differentiation, the organoids acquire diverse neuronal and glial-associated populations, including cells expressing markers of olfactory sensory neurons and interneurons. Single-nuclei RNA sequencing shows changes in cellular composition and lineage-associated transcriptional programs during maturation, while comparison with a human fetal nasal atlas identifies shared neural populations and developmental signatures. Alongside these molecular changes, the organoids develop spontaneous electrical activity and coordinated network bursting. Exposure to the glioma-relevant kinase inhibitors Dasatinib, Trametinib, and Selumetinib produces distinct changes in neuronal network activity, demonstrating the ability of the model to capture compound-associated functional responses. Together, these findings establish a human Olfactory Sensory Organoid system for investigating olfactory development and evaluating how therapeutics may affect olfactory neural tissue during intranasal drug administration.

</details>

### [Investigating Motor Skill Acquisition in Mice and Humans: Towards A Cross-Species Paradigm](https://www.biorxiv.org/content/10.64898/2026.11.20.768070v1)
*Hille, M.; Justus, L. C.; Zocher, S. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.20.768070 v1 · relevance 0.05

- **In one sentence**: A cross-species study that uses a matched chopstick-grasping task in mice and humans, with structural and quantitative MRI before, during and after training, to compare early brain changes linked to motor skill learning.
- **In plain words**: Researchers wanted a way to connect brain scans in people with what is known about brain cells from animal studies. They built a chopstick-grasping task for humans that mirrors a reaching task used in mice, then trained some mice and some men and compared them with untrained controls using MRI scans. Early in training, both species showed changes in the motor area of the brain on the side opposite the trained hand, but the authors say it is unclear whether these changes share the same biological cause.
- **Why it matters**: Brain scans in humans cannot directly show cell-level processes, so a task that works in both mice and people could help link scan findings to what happens in animal studies. The authors frame the work as a starting point rather than a finished answer, and they note that linking scan changes to cells will require future microscopic imaging in the same animals.
- **Background needed**: - Motor skill learning: getting better at a movement, such as grasping, through practice.
- MRI (magnetic resonance imaging): a scanner that images the brain's structure without surgery.
- Gray matter volume: the amount of brain tissue in a region, measured from scans.
- Quantitative MRI measures (MTsat, R1): scan-based values that are sensitive to tissue makeup; the authors suggest that increases in these may reflect more myelin, the fatty insulation around nerve fibers in the cortex.
- Cortex: the outer layer of the brain; the primary motor cortex controls movement, and the contralateral side means the hemisphere opposite the trained limb.
- Cross-species paradigm: the same experimental design applied to different animals, here mice and humans. · level: intermediate

<details><summary>Original abstract</summary>

Relating non-invasive observations of human brain plasticity to cellular processes identified in animal models remains a major challenge in neuroscience. We address this challenge by introducing a paradigm for studying motor skill acquisition across species. We designed a human chopstick grasping task modeled after the rodent single-pellet reaching task, resulting in a comparable sequence of reach-to-grasp movements across species. We studied 48 young adult male C57BL/6N mice and 71 young men, comparing trained groups with untrained controls. In both mice and humans, structural magnetic resonance imaging (MRI) was performed before, during, and after motor training. The functional form of behavioral performance gains on the trained task was highly similar across species. In trained compared to control mice, analysis of the early learning interval revealed decreases in regional volume in contralateral primary motor and forelimb somatosensory cortices, with greater volume reductions in primary motor cortex associated with better reaching performance. In humans, performance gains transferred to other chopstick tasks but not to general dexterity, and no reliable changes in gray matter volume were observed. Quantitative MRI, however, revealed early training-related changes in tissue-sensitive measures, including increases in magnetization transfer saturation (MTsat) and longitudinal relaxation rate (R1) in contralateral motor and frontal regions, potentially reflecting an increase in intracortical myelin. Thus, early structural changes in the contralateral motor cortex were detected in both species, but the degree to which these changes reflect a common biological mechanism is unclear. We conclude that the present cross-species paradigm provides a viable starting point for studying brain plasticity across species. Future work needs to relate macroscopic structural changes more directly to cellular processes by applying longitudinal microscopic imaging and MRI in the same animals.

</details>

## Genetics and genomics

### [The 'near T2T' Canton-S assembly is inconsistent with other Canton-S genomes](https://www.biorxiv.org/content/10.64898/2026.11.19.767897v1)
*Emerson, J. J.* · `genomics` · bioRxiv doi:10.64898/2026.11.19.767897 v1 · relevance 0.08

- **In one sentence**: A commentary arguing that the recently published "near T2T" genome assembly of the Drosophila Canton-S strain differs from three other independently sequenced Canton-S assemblies by an amount comparable to differences between distinct strains, which raises doubts about its genetic identity.
- **In plain words**: Canton-S is a fruit fly strain that scientists have used for decades as a standard reference. A new, very high-quality genome sequence of this strain was recently published, and this short piece says that, when compared with three other separately sequenced versions of Canton-S, the new one differs by about as much as two genuinely different fly strains do. The author suggests this calls into question whether the new sequence really comes from the same strain, so the community should think carefully before adopting it.
- **Why it matters**: Many fly studies rely on Canton-S as the baseline "wild-type" strain, so whether its reference genome is accurate matters for reproducibility. The text is a single-author critique with no reply from the original authors included, so the claim should be weighed as one side of an open question.
- **Background needed**: - Drosophila melanogaster is the common fruit fly, a widely used model organism in genetics.
- A "strain" is a line of flies bred to be genetically similar; labs share strains so experiments can be compared.
- A genome "assembly" is a computer reconstruction of an organism's full DNA sequence from many short reads.
- "T2T" (telomere-to-telomere) means an assembly that covers whole chromosomes end to end with no gaps; "near T2T" means almost complete.
- Comparing assemblies from the same named strain is a way to check whether they really represent the same genetic material.
- The text gives only the title and a short argument; it does not include the specific comparison figures or the original authors' response. · level: intermediate

<details><summary>Original abstract</summary>

Canton-S is among the most widely used Drosophila melanogaster strains, underlying substantial community infrastructure, including serving as a wild-type strain for: genetics studies; studying phenotypes, especially in behavioral studies; and complex trait mapping studies among many others. The recent 'near T2T' assembly of Canton-S (LIU et al.) is presented as delivering modern sequencing and assembly quality to the Drosophila community via this important strain. I find that this assembly is inconsistent with three other independently sequenced Canton-S genome assemblies on a magnitude comparable to differences between distinct strains, raising concerns about its genetic identity that the community should consider when choosing whether to adopt it as a resource.

</details>

### [Genomics of the diversification of Heliconius cydno (Lepidoptera: Nymphalidae) in northern South America: geographic and phenotypic patterns](https://www.biorxiv.org/content/10.64898/2026.11.20.768178v1)
*Arias Cardenas, A.; Rueda-M, N.; Arias, C. F. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.20.768178 v1 · relevance 0.07

- **In one sentence**: Whole-genome analysis of 133 Heliconius cydno butterflies tests how Andean mountain building, geography, and gene flow shaped the species' recent diversification, and identifies the ivory:mir-193 locus behind a hindwing color band that may have passed to H. melpomene.
- **In plain words**: This study looks at a group of colorful tropical butterflies in Central and northern South America and asks how their spread into many distinct forms came about. The researchers sequenced the complete genomes of 133 butterflies covering all the recognized subspecies. They found that five of the fourteen subspecies form distinct genetic groups that seem to have started in northwestern South America and later spread, and they traced a particular white wing band to one genetic region.
- **Why it matters**: It shows how mountains, geography, and hybridization between related species can together drive the splitting of populations into new forms, a question of general interest in evolution. The text does not establish how far these findings extend beyond this butterfly group.
- **Background needed**: - Heliconius butterflies are known for warning coloration (aposematism) and for mimicry, where unrelated-looking species share wing patterns to deter predators.
- Adaptive radiation: a relatively quick spread of a species into many forms adapted to different conditions.
- Andean orogeny: the uplift of the Andes mountains, which reshaped habitats and separated populations.
- Gene flow and introgression: the transfer of genetic variants between related species through interbreeding.
- Monophyletic lineage: a group that descends from one common ancestor and includes all of its descendants.
- Cis-regulatory elements: DNA stretches that control when and where nearby genes are switched on, rather than coding for proteins.
- Whole-genome sequencing: reading the full DNA sequence of each individual, which allows comparison of genetic differences across populations. · level: research-level

<details><summary>Original abstract</summary>

The interplay between natural selection, gene flow, and geography is a key driver of population differentiation. This study investigates their influence on the recent adaptive radiation of Heliconius cydno, a mimetic and aposematic butterfly with striking variation in wing color pattern across its distribution in Central and northern South America. The genetic basis of this phenotypic diversity has a modular architecture, whereby a few key genes and cis-regulatory elements control differences among morphotypes. Using whole-genome sequences from 133 individuals representing all subspecies of H. cydno, we investigated (1) the role of Andean orogeny in its diversification and (2) the genetic basis of the variation in the hindwing white submarginal band, which to date, had remained unknown. First, we found that five of the fourteen described subspecies correspond to distinct monophyletic lineages and well-defined genetic clusters that originated in northwestern South America and later expanded into Central America and the Colombian inter-Andean valleys. Second, we observed signatures of genetic structure that were consistent with geographic patterns, particularly those associated with the inter-Andean region and Gorgona Island. Third, we identified ivory:mir-193 as the locus underlying variation in the white submarginal band on the hindwing. We also detected evidence of introgression suggesting that this trait was likely transferred from H. cydno to H. melpomene, contributing to the establishment of a novel mimicry ring with H. erato. Altogether, these findings highlight the roles of geography, genomic architecture, and introgression in the diversification of H. cydno.

</details>

## Cell and molecular biology

### [Comparative transcriptomic validation of candidate geroprotectors in human iPSC-derived neurons](https://www.biorxiv.org/content/10.64898/2026.11.23.768196v1)
*MacDonald, E. M.; Lloyd, N.; Skvir, N. J. et al.* · `molecular biology` · bioRxiv doi:10.64898/2026.11.23.768196 v1 · relevance 0.08

- **In one sentence**: Eight candidate geroprotectors (drugs meant to slow aging-related decline) were tested in human iPSC-derived neurons using transcriptomic aging readouts, finding that donor genetics dominated variation and that no single readout defined geroprotection.
- **In plain words**: Finding drugs that slow aging usually means running slow, expensive lifespan studies in mice. This paper asks whether nerve-like cells grown from human stem cells can serve as a faster screening tool. The authors tested eight candidate compounds and looked at gene-activity patterns, finding that the donor's genetic background mattered most and that the drug PI-103 shifted several signals, including some linked to older age.
- **Why it matters**: A scalable cell-based screen could speed up early testing of anti-aging compounds and show which cell types respond, but the text only reports a single compound on a few readouts, so its predictive value is unproven. It may connect to efforts to replace lifespan-only testing, though the authors themselves frame iPSC cells as a promising tool rather than a validated one.
- **Background needed**: - Geroprotector: a drug or intervention that slows aging-related decline and preserves function, not just a lifespan extender.
- iPSC (induced pluripotent stem cell): an adult cell reprogrammed back into an early stem-cell state, which can then be grown into other cell types such as neurons.
- Epigenetic age: a biological clock based on chemical marks on DNA; the paper notes that reprogramming resets this clock, which raises doubts about whether iPSC-derived cells can reflect aging.
- Transcriptome: the full set of gene activity readings in a cell, used here as the main readout.
- mTORC1 and MEK-ERK: cellular growth and signaling pathways linked to aging; PI-103 acts on mTORC1 signaling.
- DCX and BDNF: genes tied to neuron development and brain-cell health.
- Donor variance: differences between cells from different people, which here outweighed compound effects. · level: research-level

<details><summary>Original abstract</summary>

The discovery of geroprotectors, defined as interventions that slow aging-related deterioration and preserve function, remains constrained by reliance on lifespan studies. Lifespan studies take years, are costly and resource intensive, and return a whole-organism endpoint dominated in mice by neoplastic death. These studies cannot be readily scaled and do not specify which tissue(s) are protected by geroprotectors. Human induced pluripotent stem cell (iPSC)-derived cells provide a scalable alternative that enables defined lineages and genetically diverse donors to be studied in parallel. However, reprogramming resets epigenetic age, and whether iPSC-derived cells can report responses relevant to aging has remained unclear. Here, we evaluated eight candidate geroprotectors in iPSC-derived neurons using multiple classes of aging-associated transcriptomic readouts. Aging-associated pathways, including mTORC1 and MEK-ERK signaling, were intact and pharmacologically tunable in these cells. Genetic background accounted for most transcriptional variance, with compound responses differing in magnitude and reproducibility between donors. PI-103 suppressed the mTORC1 signature and increased DCX and BDNF expression, while also inducing genes associated with older age in two independent human excitatory-neuron references. These findings indicate that distinct aging measures capture different dimensions of drug response and that no single readout is sufficient to define geroprotection in our model. Together, these results support iPSC-derived cells as a scalable screening tool for candidate geroprotectors, enabled by the transcriptional aging readouts now available, with the potential to resolve tissue- and donor-dependent responses as additional lineages and donors are incorporated.

</details>

### [SimpleP2G: Importance of Image Encoders for Gene Expression Prediction from Pathology Images](https://www.biorxiv.org/content/10.64898/2026.11.23.768493v1)
*Wang, J.; Zhang, J.; Hsieh, C.-Y. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.23.768493 v1 · relevance 0.08

- **In one sentence**: The paper isolates the effect of the image encoder, prediction head, and spatial context in pathology-image-to-gene-expression prediction, and introduces SimpleP2G, a direct gene-query decoder over frozen Virchow2 embeddings, plus a cross-patch variant (SimpleP2G-cross).
- **In plain words**: Researchers try to guess how active genes are expressed in tissue from microscope images of tissue slices. Many recent studies change several things at once, so it is hard to tell what actually caused better results. This paper holds the other pieces fixed and tests them one at a time.
- **Why it matters**: The main finding is that swapping in a stronger image model (Virchow2) improved results in 39 of 40 comparisons, while a simpler decoder over frozen image features already performed strongly. This suggests better image representations may matter more than added prediction-head complexity, though the evaluation is limited to five datasets and two gene panels.
- **Background needed**: - Pathology images: stained microscope pictures of tissue sections, split into small patches.
- Gene expression: how strongly each gene is switched on in a tissue sample, which can be measured by sequencing.
- HEST-1K: a public collection of paired tissue images and spatial gene data used as benchmark.
- Image encoder: a pretrained model that turns an image patch into a numerical vector (embedding); "frozen" means its weights are not retrained.
- Prediction head / decoder: the final part of the model that maps embeddings to gene values.
- PCC-200: Pearson correlation computed over 200 predicted genes, a measure of how well predictions track true values (higher is better).
- Held-out slides: tissue samples withheld from training and used only for testing. · level: research-level

<details><summary>Original abstract</summary>

Pathology-image-to-gene-expression (P2G) studies often change the prediction head, image encoder, and spatial context together, making performance differences difficult to attribute. We examine these factors through paired image-input controls and explicit input regimes. Our main comparison covers five HEST-1K datasets, two 200-gene panels, and three selected held-out slides per dataset, using validation-selected checkpoints. Across all five datasets, replacing conventional image inputs with Virchow2 improves mean PCC-200 in 39 of 40 method--dataset--panel comparisons, while one comparison decreases. We introduce SimpleP2G, a direct gene-query decoder over frozen embeddings, and SimpleP2G-cross, which adds spatially positioned neighboring embeddings. With shared Virchow2 features, SimpleP2G has the highest single-patch mean PCC-200 on all five datasets under both panels; the cross-patch variant leads on four of five datasets under each panel. Decoder and context ablations show that greater depth and broader context do not consistently improve prediction. Together, these results suggest improving image representations before adding prediction-head complexity: a direct decoder over frozen pathology embeddings already provides a strong baseline. We hope our reimplemented image-encoder-upgraded baselines and SimpleP2G models serve as transparent, reproducible, and strong controls for future P2G research.

</details>

## Immunology and microbiology

### [Toxoplasma gondii-induced NETs are mediated by CR3 engagement and the vital non-lytic NETosis pathway](https://www.biorxiv.org/content/10.64898/2026.11.25.769188v1)
*Martinez, M. A.; Valle, J. E. S.; Lima, T. S.* · `microbiology` · bioRxiv doi:10.64898/2026.11.25.769188 v1 · relevance 0.10

- **In one sentence**: In HL-60-derived neutrophil-like cells, Toxoplasma gondii (type I RH and type II PA7) triggers neutrophil extracellular trap (NET) release that appears to be vital NETosis, and this depends on complement receptor 3 (CR3, via CD11b) according to blocking-antibody experiments.
- **In plain words**: Neutrophils are immune cells that can release sticky webs of their own DNA, called neutrophil extracellular traps (NETs), to catch germs. This study looked at how the parasite Toxoplasma gondii, which infects roughly a third of people, triggers these webs in a laboratory model of human neutrophils. The authors report that the webs form quickly, that most of the cells releasing them stay alive, and that a surface receptor called CR3 is involved.
- **Why it matters**: Toxoplasma is very widespread, and this work suggests the immune cell may release its DNA traps without dying, a process that is less well understood than the classic form of NET release. The findings are from cultured cells, so their relevance to real infection in people is not established by this text; the authors frame them as groundwork for future therapeutic studies.
- **Background needed**: - Neutrophils: the most common white blood cells, first responders against microbes.
- NETs: web-like structures made of DNA plus antimicrobial proteins (myeloperoxidase, elastase, citrullinated histone 3) that trap and help kill pathogens.
- NETosis: the process of making NETs; traditionally it ends with the cell dying, while "vital" NETosis lets the cell stay alive.
- Toxoplasma gondii: a single-celled parasite; type I (RH) and type II (PA7) are lab strains that differ in virulence.
- HL-60: a human leukemia cell line that can be chemically coaxed into behaving like neutrophils.
- CR3 (complement receptor 3, CD11b/CD18): a receptor on immune cells that binds coated (opsonized) particles; blocking CD11b with an antibody tests whether it matters.
- Confocal microscopy and live/dead staining: imaging and dye methods to see NETs and check cell viability. · level: research-level

<details><summary>Original abstract</summary>

Approximately one-third of the global human population harbors an infection with the protozoan parasite Toxoplasma gondii. The immune system exploits neutrophils and one of their effector mechanisms, neutrophil extracellular traps (NETs), as an attempt to capture and neutralize T. gondii. NETs, composed of DNA, myeloperoxidase, citrullinated histone 3, and elastase, play a dual role in pathogen entrapment and amplification of the immune response. Traditionally, NET release was considered to result in neutrophil cell death. However, studies have identified an alternative process, vital NETosis, that allows NET formation while maintaining cell viability. Although T. gondii induces NET formation, the associated molecular mechanisms are not fully understood, and the neutrophil fate is unknown. In this study, the promyelocytic cell line HL-60 was differentiated into neutrophil-like cells (NLCs) and infected with type I (RH) or type II (PA7) T. gondii. Extracellular DNA was found in increasing concentrations over time in both type 1 and type 2 T. gondii-infected NLCs. Immunofluorescence staining for DNA and citrullinated histone 3 at 4, 6, and 16 hours post-infection confirmed NET formation by confocal microscopy. Cell viability at 16 hours post-infection was assessed by live/dead staining and extracellular ATP measurement, revealing that most NET-releasing neutrophils retained membrane integrity, consistent with vital NETosis. Additionally, immunofluorescence microscopy at 15 and 30 minutes further confirmed the fast release of nuclear DNA, a hallmark of vital NETosis. The use of opsonin-containing human serum and an anti-CD11b blocking antibody identified complement receptor 3 (CR3) as a receptor mediating T. gondii-induced vital NETosis. These findings demonstrate that T. gondii triggers vital NETosis in neutrophils through a CR3-dependent mechanism, advancing our understanding of the innate immune response to this globally prevalent parasite and laying the groundwork for future investigations into the molecular pathways that may be therapeutically targeted to support neutrophil-mediated immunity during infection.

</details>

### [Oral microbiome and DNA virome profiling in pigs reveals age-associated dynamics and extracellular recovery of Streptococcus suis-associated phage lineages](https://www.biorxiv.org/content/10.64898/2026.11.21.768310v1)
*Osei, E. K.; Ornelas, M. A. S.; Garcia Manzanilla, E. et al.* · `microbiology` · bioRxiv doi:10.64898/2026.11.21.768310 v1 · relevance 0.10

- **In one sentence**: Shotgun metagenomic profiling of oral fluids from pigs on 15 Irish farms, using paired bulk and virus-like-particle enrichment, mapping age-associated succession of oral bacteria and DNA phages and identifying 26 viral operational taxonomic units predicted to infect Streptococcus suis.
- **In plain words**: Researchers studied the communities of microbes and viruses found in the mouths of pigs as the animals grow older, sampling farms in Ireland. They sequenced the genetic material in oral fluids and found that the mix of bacteria and viruses changes in a fairly predictable way with age. They also identified 26 viruses, likely bacteria-eating viruses called phages, that are predicted to target Streptococcus suis, a pig pathogen.
- **Why it matters**: Streptococcus suis is an important pig pathogen, so a catalogue of phages that might attack it could eventually support therapeutic phage discovery or microbiome-based interventions. The text presents this as a framework and first catalogue; any practical use is not shown here and would need testing beyond this study.
- **Background needed**: - Microbiome: the community of bacteria and other microbes living in a body or environment.
- Virome: the community of viruses in the same sample; here the DNA viruses.
- Metagenomics: sequencing all genetic material in a sample at once, then matching it to known genomes.
- Phage: a virus that infects bacteria; it can integrate into the bacterial genome (lysogeny) or replicate and burst the cell.
- Virus-like particles (VLP) enrichment: a lab step that concentrates virus particles so they can be sequenced separately from bacteria.
- vOTU (viral operational taxonomic unit): a cluster of similar viral sequences treated as one viral species for analysis.
- Resistome: the set of antibiotic resistance genes in a sample.
- Streptococcus suis: a bacterium that causes disease in pigs and can occasionally infect people. · level: research-level

<details><summary>Original abstract</summary>

The pig oral cavity is a critical interface for microbial transmission and herd health monitoring, yet its microbiome and virome remains poorly characterised. We performed shotgun metagenomic sequencing of oral fluids from pigs across 15 commercial farms in Ireland, using paired bulk and virus-like particles (VLP) enrichment to capture comprehensive microbial and DNA virome diversity. Microbial communities shifted progressively with age, with early post-weaning animals enriched in environmental genera such as Pseudomonas and Staphylococcus and later stages dominated by lactic acid bacteria and anaerobes. Only 20.6% of vOTUs could be assigned to a known genus, with the most abundant being Astrithrvirus, which increased with age. Both microbiome and DNA virome exhibited predictable, coordinated age-associated succession with strong cross-domain coupling supported by virus-host networks. Functional profiling of the microbiome revealed that predicted carbohydrate substrates tracked the dietary transitions, while accessory viral functions partitioned by lifestyle and host. The early post-weaning stage was characterised by high abundance of viral integration and excision functions, as well as elevated resistome diversity that was almost exclusively of prokaryotic origin rather than viral. Importantly, 26 of the 25,223 vOTUs identified were predicted to target Streptococcus suis, providing the first metagenomic catalogue of such phages from pig oral environments. These findings expand our understanding of oral microbiome-virome dynamics and establish a framework for integrated microbiome and viromics approaches that could enable therapeutic phage discovery and inform microbiome-targeted interventions in pig production systems.

</details>

## Cancer biology

### [Single-agent PD-L1 blockade and tumour volume in orthotopic GL261 glioma, with an exploratory lipid analysis of the treated tumours](https://www.biorxiv.org/content/10.64898/2026.11.22.768425v1)
*Carretero-Navarro, P.; Lopez-Larrubia, P.; Pacheco-Torres, J.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.22.768425 v1 · relevance 0.07

- **In one sentence**: In mice with orthotopic GL261 gliomas, single-agent anti-PD-L1 reduced MRI-measured tumour volume in both an IDH1-wild-type and an IDH1-mutant line, with exploratory diffusion-MRI and ex vivo lipid mass-spectrometry readouts.
- **In plain words**: Glioblastoma is an aggressive brain tumour, and drugs that release the immune system's brake (checkpoint blockers) have so far not improved outcomes in patients. In this study, mice with brain tumours were given an antibody that blocks the PD-L1 checkpoint alone, and tumour size was tracked over time with MRI scans. Treated tumours were roughly a third to two-fifths the size of control tumours at day 14, and the scans also showed changes in water movement and, in one tumour line, changes in fat-like molecules.
- **Why it matters**: The paper reports the effect as a tumour-volume ratio with confidence intervals rather than only survival, which makes the size of the effect easier to judge. The lipid and diffusion findings are exploratory and based on small groups, so they should be read as hints for follow-up rather than established mechanisms.
- **Background needed**: - Glioblastoma (GBM): a fast-growing, hard-to-treat brain cancer.
- GL261: a mouse brain tumour cell line used as a laboratory model; "orthotopic" means it is grown in the organ where the tumour would normally arise.
- PD-L1 and checkpoint blockade: PD-L1 is a signal that switches off immune cells; an antibody that blocks it can let the immune system attack the tumour.
- IDH1 mutation: a genetic change common in some gliomas, here compared against an unmutated line.
- MRI volume and diffusion imaging: MRI measures tumour size; diffusion imaging tracks how water moves through tissue (apparent diffusion coefficient, fractional anisotropy).
- Mass spectrometry imaging: maps the chemical make-up, here fat molecules (lipids) such as sphingomyelin and phosphatidylcholine, across a tissue slice.
- Linear mixed model: a statistical method for repeated measurements over time in the same animals.
- Mouse-only study: results have not been tested in patients. · level: research-level

<details><summary>Original abstract</summary>

Immune checkpoint blockade has not yet changed outcomes in glioblastoma (GBM), and in immunocompetent mouse glioma the effect of a single blocking antibody is usually reported as survival rather than as tumour volume with its own confidence interval. We treated mice bearing orthotopic GL261 gliomas with anti-PD-L1 as a single agent in an IDH1-wild-type and in an IDH1-mutant line, and followed tumour volume by MRI. At day 14, tumours of treated animals were 0.33 times the volume of control tumours in the IDH1-wild-type line (95 % CI 0.21 to 0.53; p < 0.001; 16 anti-PD-L1 and 20 control animals) and 0.42 times in the IDH1-mutant line (0.22 to 0.78; p = 0.006; 10 and 10 animals), from a linear mixed model of log tumour volume over days 8 to 16. Diffusion imaging of the same tumours gave a higher apparent diffusion coefficient in the treated IDH1-wild-type tumours, by 23 % over the whole tumour (p = 0.027), and lower fractional anisotropy in the treated IDH1-mutant tumours, by 25 % over the whole tumour (p = 0.023), and in the periphery of the IDH1-wild-type ones, by 24 % (p = 0.005). We also imaged the lipid composition of treated and control IDH1-wild-type tumours ex vivo by mass spectrometry imaging: relative to the healthy brain of the same section, sphingomyelin was higher in the treated tumours and phosphatidylcholine species shifted towards shorter chains (p = 0.016 for both). In orthotopic GL261 glioma, anti-PD-L1 as a single agent reduces tumour volume in the IDH1-wild-type and in the IDH1-mutant line.

</details>

### [CSF Boundary Disruption and Tumor-Dependent Patterns of Medulloblastoma Metastasis](https://www.biorxiv.org/content/10.64898/2026.11.23.768674v1)
*Ryan, l. N.; Jimenez Garcia, L.; Gross, A. C. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.23.768674 v1 · relevance 0.07

- **In one sentence**: In mouse xenograft models of medulloblastoma, the paper links disruption of cerebrospinal fluid (CSF)-facing tumor boundaries and primary tumor growth architecture to dissemination, and reports that metastatic distribution differs among tumor models implanted at the same site.
- **In plain words**: Medulloblastoma is a childhood brain tumor, and the main cause of death is cancer spreading through the fluid that bathes the brain and spinal cord. This study grew human tumors in mice at different spots in the cerebellum to see how the tumor's position and growth pattern affect where it spreads. It found that tumors which broke into the fluid-facing edges and grew in a disruptive way were more likely to spread, while large, well-contained tumors often stayed put.
- **Why it matters**: Spread through the brain's fluid is the main cause of death in this cancer, so knowing which growth patterns predict it could help guide future work on prevention or treatment. The findings are from preclinical mouse models, so how far they apply to patients is not established by this text.
- **Background needed**: - Medulloblastoma: the most common malignant brain tumor in children, arising in the cerebellum (the back part of the brain that coordinates movement).
- Leptomeningeal metastasis: cancer spreading into the thin membranes (meninges) around the brain and spinal cord, where cerebrospinal fluid (CSF) flows.
- CSF: clear fluid that cushions the brain and spinal cord; tumor cells can travel through it.
- Xenograft: human tumor cells implanted into mice to study them in a living animal.
- Orthotopic: implanted in the organ of origin (here, the cerebellum), not elsewhere in the body.
- Bioluminescence imaging: tracking tumor growth over time by detecting light produced by tagged cells.
- Metastatic topology: the pattern of where disease sits across the brain and spinal compartments. · level: intermediate

<details><summary>Original abstract</summary>

Background: Leptomeningeal metastasis is the major cause of mortality in medulloblastoma, yet the mechanisms that facilitate dissemination are poorly resolved. Here, we leveraged preclinical models to define metastatic topology, the anatomical distribution and organization of disseminated disease across craniospinal compartments and ask how topology is influenced by cerebrospinal fluid (CSF) access, primary tumor anatomy, and tumor biology. Methods: Orthotopic D425 xenograft models were used to manipulate primary tumor geometry, defined by anatomical position of primary tumors within the cerebellum relative to CSF facing boundaries. Longitudinal bioluminescence, survival, primary growth architecture at the tumor host interface, CSF boundary breach, and craniospinal metastatic distribution were quantified. Additional medulloblastoma models MED411, MED2112, and CHLA-01-MED were implanted at a common midline cerebellar location to assess tumor-intrinsic contributions to metastatic topology. Results: While primary tumor geometry altered disease progression and survival, it did not significantly alter metastasis distribution. Strikingly, growth architecture and primary tumor burden correlated with dissemination. Despite their large size, circumscribed tumors frequently remained localized, whereas smaller, disruptive primary growth architecture was strongly associated with boundary breach, intracranial, and spinal dissemination. Conversely, when anatomical origin was held constant, distinct medulloblastoma models generated significantly different metastatic topologies. Conclusions: Disruption of CSF-facing anatomical boundaries is associated with distant dissemination, whereas the distribution of established metastatic disease differs substantially among medulloblastoma models despite standardized implantation conditions. These findings distinguish anatomical factors associated with dissemination from tumor-dependent patterns of metastatic colonization and establish an experimental framework for investigating the mechanisms underlying metastatic topology.

</details>

## Ecology and evolution

### [Trade-off between resource excretion and reliance maintains biodiversity of a cross-feeding mutualism](https://www.biorxiv.org/content/10.64898/2026.11.24.768994v1)
*Yu, Y.; Bisesi, A. T.; Mandyam Dhati, A. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.24.768994 v1 · relevance 0.10

- **In one sentence**: A mathematical model of a bacteria–yeast cross-feeding mutualism shows that increased dependence on exchanged resources, not only reduced sharing of resources ("cheating"), can drive community collapse, and that a trade-off between excretion and reliance can allow several bacterial auxotrophs to coexist.
- **In plain words**: Many microbes trade food with each other: one species gives away a nutrient and another gives back a different one. This paper uses a computer model of a bacteria-yeast pair, where bacteria break down lactose and share galactose with yeast in return for amino acids, to ask what makes such partnerships break down. The model suggests that a partner that leans too heavily on the exchange can cause collapse, just as a partner that stops sharing can, and that trade-offs between sharing and depending on exchange can let several bacterial species live together.
- **Why it matters**: The usual worry about unstable partnerships focuses on cheaters who stop contributing; this work argues that dependence on the partner matters too, which could change how stability of mutual relationships is studied. The text reports only model results, so how well these predictions hold for real microbial communities is not shown here.
- **Background needed**: - Mutualism: a relationship where both partners benefit from each other.
- Cross-feeding: one organism releases (excretes) a nutrient that another organism uses.
- Auxotroph: an organism that cannot make a certain nutrient itself and must obtain it from others (here, amino acids).
- Cheater: a partner that takes benefits while giving little or nothing back.
- Phase diagram: a map showing which parameter combinations lead to stable coexistence versus collapse.
- Coexistence and biodiversity: several species persisting together in one community.
- The model is theoretical; it is a two-species system (bacteria and yeast) expanded to several bacterial species. · level: research-level

<details><summary>Original abstract</summary>

Microbial mutualisms, in which species exchange resources through cross-feeding, are common in nature. Yet the stability of mutualistic interactions is debated, and cross-feeding communities are vulnerable to cheaters that benefit from the excretions of others but reduce or cease their own excretion of resources, which can lead to community collapse. Here, we demonstrate with a mathematical model that in addition to decreased excretion, increased reliance on cross-fed resources can also lead to community collapse. In a two-species model of bacteria that metabolizes lactose and provides yeast with galactose, in exchange for amino acids from yeast, we show that the set of excretion and reliance parameters that maximizes biomass is adjacent to a region of community collapse in the phase diagram. By expanding the model to include multiple bacterial auxotrophs competing for lactose and either separate or overlapping amino acids, we also demonstrate that a trade-off between reliance and excretion can enable coexistence within the bacterial mutualist guild. Finally, we show that intraguild coexistence of bacteria favors yeast, increasing biodiversity but decreasing total community biomass. Our results argue that the question of cheaters should be paired with analysis of reliance on mutualistic exchange, and that both of these parameters modulate biodiversity and the stability of mutualisms to collapse.

</details>

### [Sodium-enriched nectar increases seed set in low diversity prairies](https://www.biorxiv.org/content/10.64898/2026.11.25.769002v1)
*Darst, A. L.; Lamm, M. E.; Haddad, N. M.* · `ecology` · bioRxiv doi:10.64898/2026.11.25.769002 v1 · relevance 0.10

- **In one sentence**: A field experiment testing whether sodium-enriched nectar raises seed set in black-eyed Susan (Rudbeckia hirta) planted in prairies of high versus low plant diversity, with a supplementary look at floral visitation.
- **In plain words**: Flowers make nectar, a sugary liquid that feeds pollinators such as bees and butterflies, and some pollinators also need trace minerals like sodium that plants themselves hardly use. This study grew black-eyed Susan plants in sodium-enriched or ordinary soil, placed them in prairie plots seeded with either many or few plant species, and counted the seeds they produced. The authors report that sodium-treated plants made more seeds in the low-diversity prairies but not in the high-diversity ones.
- **Why it matters**: It suggests that a trace nutrient in nectar can affect plant reproduction, and that the effect depends on the surrounding plant community, which matters for how pollination works in restored or changing habitats. The text reports only one plant species and one season-level comparison, so how far it generalizes is unclear.
- **Background needed**: - Nectar: the sugary liquid flowers offer pollinators; it can also contain small amounts of minerals.
- Micronutrient: a substance needed in very small amounts; here, sodium, which plants need little of but many pollinators require.
- Seed set: the proportion of flower ovules that develop into seeds, a common measure of plant reproductive success.
- Germination rate: the share of seeds that sprout, used to check whether seed quality changed.
- Context dependency: the idea that the same interaction can produce different results depending on surrounding conditions, such as neighboring plant diversity.
- Prairie plots seeded with high or low diversity: experimental grasslands planted with many versus few plant species.
- Supplementary experiment: a smaller side study; here it looked at which flower visitors came to the plants. · level: intermediate

<details><summary>Original abstract</summary>

Plant-pollinator interactions depend on floral traits and background plant community properties, yet the role of nectar micronutrients in these interactions is poorly understood. Sodium is a micronutrient of particular interest because although plants need little to no sodium, animal pollinators require it. It is unknown whether sodium-enriched nectar increases plant fitness in animal-pollinated plants and how this may be affected by the broader plant community. To test this, we grew black-eyed Susan (Rudbeckia hirta) plants in sodium-enriched or control soil. We placed pairs of sodium-addition and control plants in prairies seeded with high or low diversity and measured seed set and germination rate. In a supplementary experiment, we explored differences in floral visitation. We found that black-eyed Susan plants grown in sodium-enriched soil had sodium-enriched nectar. Seed set increased in sodium-addition plants in prairies seeded with low diversity but not in prairies seeded with high diversity. Germination rate was not affected by sodium addition. Altogether, our study highlights the importance of considering both micronutrients and context dependency in understanding plant reproduction and complex species interactions.

</details>

## Plant biology

### [Whole-genome resequencing and indoor phenotyping resolve the genetic architecture of drought stress response in tepary bean](https://www.biorxiv.org/content/10.64898/2026.11.24.768977v1)
*Srinivasan, A.; Yu, L.; Nichols, R. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.24.768977 v1 · relevance 0.06

- **In one sentence**: Whole-genome resequencing of 363 tepary bean accessions combined with indoor drought and control phenotyping of 282 of them maps 113 significant SNPs to three drought loci and six control loci, with the largest drought locus on chromosome 8 separating wild from cultivated lines.
- **In plain words**: Tepary bean is a legume that grows in dry places, and scientists want to know which genes let it cope with drought. The team sequenced the DNA of 363 bean lines, grew 282 of them for two weeks at either well-watered or very dry soil, and measured growth, water use and photosynthesis. They then linked differences in the DNA to differences in those measurements.
- **Why it matters**: Drought tolerance is a central problem for crop breeding, and this study separates the genetic basis of growth under drought from growth under normal conditions. The finding that the strongest drought-linked region is tied to domestication suggests that breeding history shaped drought response, though the text does not show how this translates to field performance.
- **Background needed**: - Tepary bean (Phaseolus acutifolius) is a legume from arid regions, related to common bean.
- Accessions are samples of a crop or wild plant kept in a collection; wild, weedy, cultivated and breeding lines are different groups.
- Whole-genome resequencing reads the full DNA of many individuals to find single-nucleotide polymorphisms (SNPs), single-letter variations in the genetic code.
- Association mapping checks which DNA variants occur more often in plants showing a given trait, to locate genes behind it.
- Evapotranspiration is the total water lost from soil and leaves; canopy density is how much leaf cover the plant has.
- Locus means a specific position on a chromosome; haplotype means a group of nearby variants inherited together.
- Domestication is the process by which wild plants were selected and bred for human use. · level: research-level

<details><summary>Original abstract</summary>

Tepary bean (Phaseolus acutifolius A. Gray) is an arid-adapted legume, whose drought resilience is widely reported but poorly resolved genetically. Here we resequenced 363 wild, weedy, cultivated and breeding accessions and recovered 6.9 million single-nucleotide polymorphisms (SNPs). We phenotyped 282 of the accessions for growth, evapotranspiration and photosynthesis over 14 days at 60% or 10% soil water-holding capacity. Cultivated and breeding lines grew roughly twice as fast as wild accessions, and the proportional reduction in growth under drought did not differ between these germplasm classes. Evapotranspiration separated the classes under full irrigation, but converged under drought, making it the most plastic trait we measured. Canopy density predicted how much water a plant used, but not how well it tolerated losing it. Association mapping across 104 rank-normalized measurements yielded 113 significant SNPs at 46 positions, which resolved to three drought and six control loci. Three drought loci corresponded to 98 of the 113 SNPs, with the largest one localized on chromosome 8. This locus separates wild from cultivated accessions, and resolves to no gene. Three of the eight remaining loci carry candidates whose interval, expression under drought and published mechanism agree: a cytokinin oxidase, a CIPK1-clade kinase and the antenna subunit LHCB5. The most structure-independent locus localizes to 26 kb but implicates genes with no published role in water relations. Growth under drought and control conditions therefore rest on separate genetic bases, and the variation with the largest effect under deficit lies in haplotypes affected by domestication.

</details>

### [An RHD6-directed gene network sustains root hair growth under combined low phosphate and salt stress in Arabidopsis](https://www.biorxiv.org/content/10.64898/2026.11.25.769266v1)
*Ibeas, M. A.; Perez, J.; Padilla, G. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.25.769266 v1 · relevance 0.06

- **In one sentence**: In Arabidopsis, induction of the transcription factor RHD6 keeps root hairs growing under combined low phosphate and salt stress, and RNA sequencing plus promoter and co-expression analysis yields a candidate network of 396 direct RHD6 targets, with HEC3 singled out as a modulator of the root hair response.
- **In plain words**: Plants often face low phosphate in the soil and salty conditions at the same time, and salt tends to stop the tiny hair-like outgrowths on roots from growing. The authors switched on single plant regulatory genes one at a time and found that turning on RHD6 kept root hairs growing under both stresses together, which normal plants could not do. Sequencing the genes that changed in those roots gave a list of candidate genes that RHD6 may directly control, and mutant plants lacking HEC3 did not show the usual shortening of root hairs under the combined stress.
- **Why it matters**: Root hairs are the main route by which plants take up phosphate and water, so understanding how they keep growing under combined stress could matter for crop performance on salty, nutrient-poor soils. The text does not show any direct crop or field application, and the HEC3 finding rests on a limited set of mutant tests in a model plant.
- **Background needed**: - Root hairs: thin tubular extensions of root cells that absorb water and nutrients such as phosphate.
- Phosphate (inorganic phosphate): an essential nutrient that is often scarce in soil.
- Salt stress: high sodium levels that slow plant growth and water uptake.
- Transcription factor: a protein that switches sets of genes on or off; RHD6 is one that helps drive root hair growth.
- Inducible system (beta-estradiol-inducible TRANSPLANTA lines): a lab method that turns a gene on by adding a chemical, so its effects can be compared.
- RNA sequencing: measuring which genes are more or less active, here comparing RHD6-induced and control roots under dual stress.
- Promoter motif scanning and co-expression analysis: computer methods that predict which genes a transcription factor is likely to control directly.
- T-DNA insertion mutants: plants with a disrupted gene, used to test what that gene does. · level: research-level

<details><summary>Original abstract</summary>

Phosphate deficiency and salinity can coincide, but how roots integrate the two stresses is poorly understood. Root hairs (RHs) elongate under low inorganic phosphate and are inhibited by salt. Screening {beta}-estradiol-inducible TRANSPLANTA lines for 18 RH-expressed transcription factors (TFs) in Arabidopsis (Arabidopsis thaliana), we found that induction of ROOT HAIR DEFECTIVE 6 (RHD6) maintained RH growth under combined low phosphate (5 {micro}M) and salt (100 mM NaCl), which inhibited wild-type RH growth. RNA sequencing of RHD6-induced roots under dual stress identified 1,811 differentially expressed genes. Up-regulated genes were enriched for RH differentiation, tip growth and cell wall organization; down-regulated genes were enriched for phenylpropanoid and suberin metabolism, hydrogen peroxide catabolism, photosynthesis and responses to wounding and jasmonic acid. Promoter motif scanning combined with ensemble co-expression analysis defined a core network of 396 candidate direct RHD6 targets, including 31 TFs. The TFs with the largest expression changes were HEC3, HEC1 and EIL4. In T-DNA insertion mutants, dual stress did not shorten hec3 RHs; eil4 and hec1 had shorter RHs on the control medium but no significant change in relative inhibition. These data provide a resource of RHD6-dependent genes and identify HEC3 as a modulator of the RH response to combined stress.

</details>

## Bioengineering and synthetic biology

### [Digital light processing of human-scale tissue-engineered heart valves](https://www.biorxiv.org/content/10.64898/2026.11.22.768423v1)
*Jafari, A.; Nemati, A.; Sarshoghi, A. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.22.768423 v1 · relevance 0.08

- **In one sentence**: A composite light-curable bioink (PEGDA, GelMA, and methacrylated quince seed mucilage, called GPQuin) is used with digital light processing 3D printing to make a human-scale, trileaflet tissue-engineered heart valve scaffold, with mechanical, surface-accuracy, cell, implantation, and pulse-duplicator data reported.
- **In plain words**: Heart valves can fail, and replacements made from donor tissue or artificial materials have drawbacks. This paper describes a new printable gel-like material that can be shaped by shining light on it, and uses it to print a full-size three-leaflet heart valve scaffold. The authors report that the printed valve kept its shape reasonably well, its leaflets opened and closed under simulated pulmonary pressure, and human valve cells survived on it for two weeks.
- **Why it matters**: Printing a whole-size valve with separate, anatomically shaped leaflets is a hard engineering step, so the work is relevant to the goal of lab-grown replacement valves. The text reports only early results (one printed design, 12-week implantation with an inflammatory response, and a single pulse-duplicator test), so its clinical value is still uncertain.
- **Background needed**: - Heart valves control one-way blood flow; replacements can be animal tissue, mechanical, or synthetic, each with known problems.
- Tissue-engineered valves aim to grow living tissue on a scaffold that the body can remodel.
- 3D printing builds objects layer by layer; digital light processing (DLP) cures a liquid resin with projected light, layer by layer.
- Hydrogels are water-swollen gel networks; PEGDA is a synthetic polymer, gelatin methacryloyl (GelMA) is a modified gelatin, and quince seed mucilage is a plant-derived gum; "methacrylated" means chemically modified so it can be cured by light.
- Tensile modulus measures stiffness; ultimate tensile strength is the stress at which a material breaks; elongation at break is how far it stretches before breaking.
- Micro-CT is an X-ray scanning method used to compare the printed shape with the design.
- Induced pluripotent stem cells are adult cells reprogrammed to an embryonic-like state, which can then be turned into other cell types.
- A pulse duplicator is a lab pump rig that mimics heartbeat pressure and flow to test valves. · level: research-level

<details><summary>Original abstract</summary>

Tissue engineered heart valves (TEHVs) could overcome the complications of current heart valve replacement, such as immunologic events, degenerative fibrocalcific changes, and patient-prosthesis mismatch. Digital light processing (DLP) 3D printing enables creation of complex geometries; however, suitable (bio)inks remain limited. Here, a composite ink comprising poly(ethylene glycol) diacrylate (PEGDA), gelatin methacryloyl (GelMA), and methacrylated quince seed mucilage (QSGM), termed GPQuin, was developed for DLP printing of human-scale TEHVs. GPQuin enabled fabrication of a trileaflet TEHV with separated leaflets and anatomically inspired sinuses. Micro-computed tomography revealed mean positive and negative surface deviations of +214 and -248 micrometers, respectively. The printed hydrogels exhibited a tensile modulus of 117.2 +/- 15.5 kPa, an ultimate tensile strength of 113.2 +/- 17.4 kPa, and an elongation at break of 75.3 +/- 2.3%. Human induced pluripotent stem cell-derived valve cells attached to the hydrogel surfaces and remained predominantly viable over 14 days. After 12 weeks of subcutaneous implantation, the constructs showed a time-dependent inflammatory response. In a pulse duplicator under pulmonary loading, printed valves exhibited good cyclic leaflet opening and closing. Together, these findings establish GPQuin as a printable platform for human-scale valve scaffolds and support further investigation in heart valve tissue engineering.

</details>

### [BMP-2 Release from Biomaterial Carriers: Reporting Heterogeneity and the Limits of Cross-Study Prediction](https://www.biorxiv.org/content/10.64898/2026.11.13.766607v1)
*Zhou, W.; Zhou, L.; Hou, W. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.13.766607 v1 · relevance 0.08

- **In one sentence**: A preliminary study compiles 79 published BMP-2 release experiments from 21 papers and tests whether carrier-family labels can predict release across studies, finding that gains mostly hold within studies and not across publications.
- **In plain words**: Bone-growth proteins (BMP-2) are often loaded onto carrier materials that release them slowly over time. Researchers have published many release curves, but they are reported in inconsistent ways, so this paper gathered them, using an AI assistant checked by humans, to see whether a machine learning model could predict release from published data. Simple models beat a basic baseline when test data came from the same pool of studies, but not when whole publications were held out.
- **Why it matters**: Predicting how a growth factor leaves its carrier matters for designing bone-repair implants, and the paper is a useful caution about how far published data can be reused. It is a small, exploratory dataset, so its conclusions are tentative and mainly about data quality and study design.
- **Background needed**: - BMP-2 is a protein that signals bone to grow; it is used in bone-repair treatments.
- A "carrier" is a material (such as a coating or scaffold) that holds the protein and releases it gradually.
- "Release profile" means how the amount released changes over time.
- Machine learning (ML) models learn patterns from data to make predictions; gradient-boosted decision trees are a common method.
- Mean absolute error measures average prediction error; log10 units are a logarithmic scale.
- Random hold-out tests split data at random, while publication-grouped cross-validation holds out entire papers, which is a stricter test of generalization to new studies.
- Interpolation means predicting within the range of known conditions; generalization means predicting for new studies or conditions. · level: research-level

<details><summary>Original abstract</summary>

Published release profiles offer a potential basis for predicting bone morphogenetic protein-2 (BMP-2) delivery from biomaterial carriers, but heterogeneous reporting and study-specific effects complicate their reuse in machine learning (ML) models. As a preliminary exploration, we compiled 79 release experiments and 487 time points from 21 publications with a workflow that combined a large language model assistant and human verification, and we examined data comparability and cross-study prediction with ML models. Only 38 experiments (48%) reported BMP-2 alone as a percentage of the loaded dose. Within individual studies, binding components and coating layers were associated with slower release, consistent with established carrier mechanisms. Using carrier family as the sole predictor, a family-median model and gradient-boosted decision trees achieved lower mean absolute errors than a global-median baseline under random hold-out validation (0.42 and 0.44 versus 0.52 log10 units). Publication-grouped cross-validation did not establish a corresponding improvement (0.57 and 0.48 versus 0.50). Only 10 of the 28 modeling experiments belonged to carrier families represented in the training data under this scheme, and carrier family was strongly associated with publication. These findings highlight the need to distinguish within-study interpolation from cross-study generalization. Broader coverage of each carrier family, quantitative formulation and assay descriptors, and accessible numerical source data are needed to support predictive modeling of BMP-2 release.

</details>

## Mathematical biology (arXiv)

### [Exclusion and internal structure in the association/dissociation kinetics of DNA-binding proteins in the fast diffusion limit](https://arxiv.org/abs/2611.33740)
*Xiangting Li, Tom Chou* · `q-bio.BM` · arXiv:2611.33740v1 · relevance 0.06

- **In one sentence**: A coarse-grained stochastic model, reduced to an effective Markov model and a mean-field approximation, describes how multi-state DNA-binding proteins with finite footprints adsorb, desorb, and slide along DNA in the fast-diffusion regime, and is fit to RPA binding to ssDNA.
- **In plain words**: Many proteins stick to DNA and slide along it, and some of them can also change shape while attached. This paper builds a simplified mathematical model of that sticking, sliding, and shape-changing, and checks it against previously measured data on a protein called Replication Protein A (RPA) binding to single-stranded DNA. The authors report that the model fits those measurements and can also describe proteins that occupy several segments at once.
- **Why it matters**: Predicting how these proteins bind and rearrange on DNA matters for understanding DNA replication, repair, and chromatin packaging, and the text suggests the framework may apply to nucleosomes and other single-stranded DNA-binding proteins. The text does not show how broadly it generalizes beyond the RPA fit, so those wider applications remain claims to be tested.
- **Background needed**: - DNA-binding proteins: proteins that attach to DNA, sometimes without a specific sequence target (nonspecific binding).
- Fast diffusion regime: the protein slides along DNA much faster than it can leave and rebind, so sliding dominates the kinetics.
- Footprint: the number of DNA bases a bound protein physically covers; a large footprint blocks neighbouring proteins (exclusion).
- Conformational states: different shapes or configurations a bound protein can adopt, switching at their own rates.
- Markov model: a model where future behaviour depends only on the current state, not on history.
- Mean-field approximation: simplifying many interacting particles by treating each as feeling an average effect of the others.
- Facilitated exchange: a protein already on DNA helps another protein swap places with it by sliding nearby.
- RPA: a single-stranded DNA-binding protein that coats DNA during replication and repair. · level: research-level

<details><summary>Original abstract</summary>

In many canonical biophysical and biochemical contexts, complex diffusing DNA-binding proteins undergoing nonspecific adsorption and desorption can exist in different conformational states. Equilibrium binding theories and kinetic models of competing ligands provide a basis for describing these systems. Coupling the internal conformational kinetics of bound proteins to exclusion and diffusion requires tracking both protein positions and binding states. Closed-form, tractable mathematical models that accurately describe the stochastic dynamics of structured proteins that bind to and diffuse along DNA are lacking. Here, we develop a new coarse-grained stochastic model of nonspecific DNA-protein binding in the fast diffusion regime, from which we derive an effective Markov model and its corresponding mean-field approximation that incorporates protein footprint size and conformational switching. We fit our new model quantitatively to previously measured dynamics of Replication Protein A (RPA) binding to ssDNA. Finally, by including multisegment binding states, our analysis captures facilitated exchange, revealing how multisegment architecture balances high affinity with rapid remodeling. Our theoretical model applies broadly to many other DNA-binding protein systems, including nucleosomes, ssDNA-binding proteins, and other multisegment complexes, providing accurate predictions and new strategies for evaluating experimental data.

</details>

### [A multi-patch model for sylvatic hematophagous vector dynamics: the impact of landscape anthropization](https://arxiv.org/abs/2611.34735)
*Ivric Valaire Yatat-Djeumen, Lukas Eigentler, Orville Wright Happi-Tchakount\'e et al.* · `q-bio.PE` · arXiv:2611.34735v1 · relevance 0.06

- **In one sentence**: A multi-patch mathematical model of tsetse fly and wild animal populations across connected habitat patches, where human land use (anthropization) reduces animal carrying capacity and triggers movement, analysed under three dispersal rules and parameterized for districts in Cameroon.
- **In plain words**: This paper uses a set of equations to model how blood-feeding tsetse flies and the wild animals they feed on spread through a landscape split into patches. Human land use ("anthropization") lowers how many animals a patch can hold and pushes both animals and flies to move. The authors tested three movement rules and fitted the model to tsetse data from three districts in Cameroon.
- **Why it matters**: Tsetse flies carry trypanosomes that cause sleeping sickness and nagana, so how vector populations spread as land is cleared is a practical public-health and livestock question. The text reports that the effect of human land use on movement mattered more to the final population levels than its effect on animal carrying capacity, and that the way animals disperse changes whether disturbed areas speed up or slow down invasion. The text itself notes that more empirical data on animal dispersal are needed, so the conclusions are model-based and should be read as such.
- **Background needed**: - Multi-patch model: the landscape is divided into discrete habitat patches, each with its own population, and individuals move between them.
- Carrying capacity: the maximum population a habitat can sustain long-term.
- Anthropization: the degree to which land is altered by human activity.
- Dispersal: how animals or insects move from place to place.
- Equilibrium and local stability: a steady population level, and whether small disturbances return to it.
- Pulled traveling wave: a model of an invasion front moving at a steady speed, driven by the leading edge spreading into empty territory.
- Tsetse flies (Glossina spp.): blood-feeding insects that transmit African trypanosomiasis. · level: research-level

<details><summary>Original abstract</summary>

We develop a multi-patch model for sylvatic hematophagous vector--(wild) animal interactions with nonlinear migration terms that depend on landscape anthropization. Every patch is a suitable habitat for both animals and vectors, but anthropization reduces the animal carrying capacity and induces animal and vector displacement. We considered three dispersal types. Under unconstrained global dispersal, displaced individuals can move to any other patch. Under the more realistic random and constrained neighbor dispersal, displaced animals move to a neighboring patch chosen either at random or preferentially among less anthropized ones. We parameterized our model for tsetse flies (Glossina spp.) in the districts of Campo, Ny\'e'\'et\'e, and Ma'an, Ocean division, Cameroon. We characterized the equilibria and their local stability analytically for unconstrained global dispersal, and found numerically that, under both neighbor dispersal regimes, populations progressively expand before settling into a stable equilibrium. Under random neighbor dispersal, the effect of anthropization on migration had a much larger impact on steady state densities than its effect on animal carrying capacity. Under constrained neighbor dispersal, populations spread noticeably more slowly, and numerous patches maintained extremely sparse populations. We further investigated invasion speed under different anthropization scenarios. For random neighbor dispersal, invasion times decreased upon introduction of newly anthropized regions, while for constrained neighbor dispersal, anthropized regions either increased or did not affect invasion times. Approximating invasions by pulled traveling waves, we found that anthropized regions act as ``invasion highways'' or ``invasion barriers'' depending on the dispersal type. We conclude that more empirical data on animal dispersal are needed to understand these dynamics.

</details>

## Epidemiology

### [Productivity-adjusted life years lost due to type 2 diabetes by socioeconomic position in Germany between 2022 and 2060](https://www.medrxiv.org/content/10.64898/2026.11.20.26368491v1)
*Piedboeuf-Potyka, K.; Hering, R.; Schulz, M. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.20.26368491 v1 · relevance 0.04

- **In one sentence**: A projection study estimating productivity-adjusted life years (PALYs) lost to type 2 diabetes among German working-age adults, stratified by socioeconomic position and sex, for 2022 to 2060.
- **In plain words**: This paper asks how much working life and productive time that type 2 diabetes takes away from people in Germany, and whether this differs by income, education or job status. The authors used an existing projection model and public German data to estimate these losses for men and women across ages 20 to 69. They found that losses were largest for people with low socioeconomic position, and that the total at population level is expected to rise by 2060 mainly because more people will have the disease.
- **Why it matters**: It puts a economic cost on a chronic disease in terms of both early death and lost work, and shows that the burden falls unevenly across social groups, which may matter for planning prevention and workplace policy. The text does not report how the estimates would change under specific interventions, so its practical use depends on follow-up work.
- **Background needed**: - Type 2 diabetes: a long-term condition in which the body handles blood sugar poorly; it is strongly linked to lifestyle and age.
- Socioeconomic position (SEP): a person's standing based on factors such as income, education and occupation; here grouped as low, medium and high.
- Years of life lost (YLL): years of life cut short by early death, compared with people without the disease.
- Years of productivity lost (YPL): lost working capacity from fewer people in work, reduced performance on the job (presenteeism) and missed work days (absenteeism).
- PALY: the sum of YLL and YPL, a single measure combining premature death and lost productive work.
- Projection model: a simulation that estimates future numbers based on assumed trends, such as incidence (new cases per year).
- Confidence interval (CI): a range that expresses the uncertainty around an estimate. · level: research-level

<details><summary>Original abstract</summary>

IntroductionType 2 diabetes can impair productivity during working age (20-69 years), causing substantial economic burden at individual and at population level. We aimed to estimate age- and sex-specific productivity-adjusted life years (PALYs) lost due to type 2 diabetes by socioeconomic position (SEP) between 2022 and 2060 in Germany. MethodsWe used an established projection model and nationally representative, publicly available German data to estimate age- and sex-specific PALYs lost due to type 2 diabetes by SEP among working-age adults, accounting for future incidence trends. PALYs lost were calculated as the sum of years of life lost (YLL) and years of productivity lost (YPL) due to reduced labour force participation, presenteeism, and absenteeism, using SEP-specific estimates from representative studies. ResultsProductivity losses were highest among persons with low SEP, followed by those with medium and high SEP. In 2022, 20-year-old men with type 2 diabetes and low, medium, and high SEP were projected to lose 11.32 PALYs (95% confidence interval (CI) 7.99-14.56), 8.19 PALYs (95% CI 6.01-10.33), and 3.78 PALYs (95% CI 0.89-6.72), respectively, by age 69 compared with men without type 2 diabetes, mainly driven by YPL. A comparable socioeconomic gradient was observed among women and remained largely unchanged until 2060. At the population level, an estimated 9.5 million PALYs (95% CI 6.42-12.58) were lost due to type 2 diabetes in 2022 in both sexes. This number is projected to increase to 9.5-13.5 million by 2060, mainly driven by the projected increase in the number of persons with type 2 diabetes. ConclusionType 2 diabetes-related productivity losses were shaped by SEP, sex and the future number of persons with the disease. PALYs lost declined with age and were predominantly driven by YPL.

</details>

### [Place or placeholder? AlphaEarth satellite embeddings did not detectably improve weekly dengue forecasts in four countries](https://www.medrxiv.org/content/10.64898/2026.11.23.26368794v1)
*Patel, B. K.; Asokan, A. V.; Pant, S.* · `epidemiology` · medRxiv doi:10.64898/2026.11.23.26368794 v1 · relevance 0.03

- **In one sentence**: A retrospective test of whether AlphaEarth satellite embeddings improve weekly district dengue case forecasts in Brazil, Colombia, Peru and Taiwan, with a location-only control to separate true environmental signal from simple district identity.
- **In plain words**: The paper asks whether satellite-derived numerical summaries of places help predict how many dengue cases will occur in each district each week. The authors forecast cases one and four weeks ahead across 6,909 districts in four countries, from 2020 to 2024. They found no statistically significant improvement from the satellite data after correcting for multiple comparisons, and some small losses.
- **Why it matters**: Satellite embeddings are being used in disease forecasting, so it matters whether they add real predictive value or mainly act as a label that recognises each district. The paper's location-only control is a useful check that other studies could adopt, though the results are limited to these four countries and this model type.
- **Background needed**: - Dengue is a mosquito-borne viral disease; weekly case counts vary by place and season.
- Forecasting here means predicting future case counts from past data and other inputs.
- AlphaEarth embeddings are numerical summaries of satellite imagery for a location, used as model inputs.
- A "placeholder" or location control is an input that only identifies a district, so any gain from it reflects place identity rather than environment.
- Gradient boosting is a common machine-learning method that builds many decision trees.
- The weighted interval score measures forecast accuracy, penalising both wide and missed prediction ranges (lower is better).
- Diebold-Mariano tests compare forecast accuracy; the Holm correction adjusts for running many tests.
- An equivalence margin (here ±1%) defines how small an effect must be to be treated as negligible. · level: research-level

<details><summary>Original abstract</summary>

Background. Some recent disease forecasts use satellite embeddings (numbers summarising places). A model may use them only as a placeholder, recognising districts and their usual dengue levels without learning about the environment. We asked whether AlphaEarth embeddings improve weekly district dengue forecasts and whether gains go beyond such recognition. Methods. We retrospectively forecast cases one and four weeks ahead in 6,909 districts of Brazil, Colombia, Peru and Taiwan (OpenDengue, 2020-2024) with gradient boosting. In 14 comparisons across future years and held-out places, we measured how embeddings changed the weighted interval score, with and without a location control (an input that only identifies a district), to test whether location alone explains gains. We used Diebold-Mariano tests, the Holm correction and a +/-1% equivalence margin set after the first Brazil and Peru results. Findings. No comparison showed a significant gain after correction. Six showed losses: five small (-0.42% to -0.68%) and one with Taiwan held out (-18.3%; absolute -0.0037). Only Colombia's held-out-states loss (-0.52%) stayed significant under two stricter checks and a check for cases hidden in zero-filled weeks. In 8 comparisons (5 under the stricter checks), any gain or loss was shown to be smaller than 1% of forecast error. This margin is roughly Brazil's gain from all non-case inputs combined. In exploratory analyses, embeddings alone predicted district burden in unseen states. Without case history, neither coordinates nor embeddings helped detectably in Brazil's held-out states; both hurt in Colombia's. In Brazil's future years, coordinates cut error by 3.3% (1.7 to 4.9); embeddings added nothing detectable. Interpretation. Embeddings partly showed which districts usually have more dengue, but in Brazil and Colombia other non-case inputs already held most of it. With case history they added no detectable accuracy; without it, evidence was inconclusive. Embeddings should be tested against location-only controls in held-out places.

</details>

## Infectious diseases

### [Safety and microbiological activity of a combined phage cocktail in persons with cystic fibrosis colonized with Achromobacter: Study protocol for a phase 1, investigator-initiated, randomized clinical trial.](https://www.medrxiv.org/content/10.64898/2026.11.22.26368705v1)
*Massey, J.; Hughes Kramer, K.; Snook Barrett, S. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.22.26368705 v1 · relevance 0.05

- **In one sentence**: A study protocol for a phase 1, open-label, randomized pilot trial testing the safety and early biological effects of a four-phage cocktail (AchromoPhage) against pulmonary Achromobacter infection in 12 adults with cystic fibrosis, given intravenously, by inhalation, or both.
- **In plain words**: This is a plan for a small early-stage safety trial of a mixture of four viruses that infect bacteria (phages), aimed at a hard-to-treat lung bacterium in people with cystic fibrosis. Twelve adults would get three weekly doses by vein, by breathing it in, or both, and researchers would track side effects, lung function, quality of life, and how the viruses and the immune response behave in the body. The text is a protocol, so it reports no results yet.
- **Why it matters**: Phage therapy is studied mainly through case reports, and the authors say clinical trials in people with cystic fibrosis have not yet looked at Achromobacter, so this trial could add needed safety and dosing data. Whether it leads to useful treatments is uncertain; this stage is designed to test safety, not to prove the cocktail works.
- **Background needed**: - Cystic fibrosis (CF) is an inherited disease that causes thick mucus and chronic lung infections.
- Achromobacter is a group of bacteria that often resists many antibiotics and can cause serious lung infections in people with CF.
- Bacteriophages ("phages") are viruses that infect and kill specific bacteria; they are not active against human cells.
- "Obligately lytic" means the phages always kill their host bacteria rather than living alongside them.
- A phase 1 trial is an early study mainly focused on safety, tolerability, and how a drug moves through the body.
- "Pharmacokinetics" describes how a substance is absorbed, spread, and cleared from the body.
- A neutralizing antibody response means the immune system makes proteins that can block the phages.
- FEV1 is a standard spirometry measure of how much air a person can forcibly exhale in one second. · level: intermediate

<details><summary>Original abstract</summary>

BackgroundAchromobacter are a genus of difficult-to-treat, frequently multi-drug-resistant Gram-negative bacteria that can cause severe infections in people with cystic fibrosis (pwCF). Bacteriophages are an understudied yet promising therapy for these and other antibiotic-resistant bacteria. However, data are largely limited to case reports or series, and clinical trials among pwCF to date have not evaluated Achromobacter. MethodsThis is an investigator-initiated, open-label, randomized phase 1 pilot trial to evaluate the safety, tolerability, and biological effects of AchromoPhage, a cocktail of four genetically distinct, obligately lytic Achromobacter-targeting phages (phiACH01, phiACH04, phiACH06, phiACH07) with broad activity against Achromobacter species, in 12 adult participants with CF and pulmonary Achromobacter infection. Twelve participants will be randomized into three groups to receive a total of three, increasing, weekly doses of the AchromoPhage cocktail via one of three routes: 1) intravenous, 2) via inhalation, or 3) or intravenously and inhaled. Participation in the trial will span approximately 7 weeks, which will consist of outpatient phage dose administrations, safety and symptom monitoring, and longitudinal collection of biospecimens for protocol-specified and exploratory analyses through Day 42. The primary safety endpoint is the occurrence of treatment-related Grade 4 or greater adverse events. Secondary endpoints include longitudinal changes in FEV1 by spirometry, longitudinal changes in health-related quality of life, pharmacokinetics of each of the four phages in blood and the respiratory tract, and emergence of a phage neutralizing antibody response in serum. DiscussionWhile existing case anecdotes and observational studies suggest that phages are safe and may have a role in treating human infections, there is a paucity of clinical trials studying the adverse effect profile and basic pharmacological parameters of phages. This trial will study the safety and explore the pharmacokinetic and other properties of a four-phage cocktail in patients with CF and chronic Achromobacter lung infection. Trial registrationClinicalTrials.gov NCT0727590. Registered on 12/10/2025 Structured summary O_TBL View this table: org.highwire.dtl.DTLVardef@910c30org.highwire.dtl.DTLVardef@b725a7org.highwire.dtl.DTLVardef@91f50org.highwire.dtl.DTLVardef@e6eb5eorg.highwire.dtl.DTLVardef@666ef0_HPS_FORMAT_FIGEXP M_TBL C_TBL Protocol versionAchromoPhage Protocol August 26, 2026. Version 2.0

</details>

## Public and global health

### [Community-Based Hypertension Screening in Urban and Rural Zimbabwe: A Comparative Analysis and Implementation Lessons (2022-2025)](https://www.medrxiv.org/content/10.64898/2026.11.23.26368728v1)
*Chimberengwa, P. T.; Masiye, K.; Bepe, T. O. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368728 v1 · relevance 0.06

- **In one sentence**: A retrospective comparison of community health worker-led hypertension screening across two implementation periods in urban and rural Zimbabwe, using routine aggregate programme data from DHIS2, reporting positivity of 41.0% in Phase 1 versus 14.5% in Phases 2 and 3 and drawing implementation lessons for decentralized care.
- **In plain words**: This paper looks at a programme in Zimbabwe where trained community health workers used digital blood pressure machines to screen adults in their communities and refer those with high readings to clinics. The authors compared results from an early urban phase (adults 40 and older) with later phases that mostly reached rural and peri-urban people and included adults 18 and older. Hypertension was found in far more people in the urban early phase, and the authors say this gap mainly reflects who was screened rather than how well the programme worked.
- **Why it matters**: Screening that happens in communities, rather than only at clinics, is one way health systems try to find high blood pressure early in places with few facilities. The paper is useful as a description of reach at scale, but it does not show whether people were linked to care or had their blood pressure brought under control, which the authors state is still needed.
- **Background needed**: - Hypertension (high blood pressure) is a major risk factor for heart disease and stroke, and often has no symptoms, so it is found by measuring.
- Community health workers (CHWs) are lay workers trained to do basic health tasks, such as screening, within their own neighbourhoods.
- Decentralized care means delivering services closer to where people live rather than only in hospitals.
- Screening positivity is the share of people screened who test above a set blood pressure threshold; it is not the same as the share who have a confirmed diagnosis.
- DHIS2 is a widely used national health information system for routinely collected records.
- This is a retrospective analysis of aggregate (summary-level) records, so the groups were not randomly assigned and the phases differ in age range and location.
- Confidence intervals give a range of plausible values for a measured share; the narrow ranges here reflect the very large numbers, not the absence of bias. · level: intermediate

<details><summary>Original abstract</summary>

Introduction Hypertension is a leading cause of cardiovascular disease and a growing public health challenge in sub-Saharan Africa. Community-based screening delivered through community health workers (CHWs) may improve early detection and strengthen decentralized chronic disease services, particularly in underserved settings. This study compared hypertension screening yield across phased implementation of a community-based programme in urban and rural Zimbabwe and documented implementation lessons for decentralized hypertension services. Methods A retrospective comparative analysis was conducted using aggregate programme data routinely captured in the District Health Information System 2. Screening outcomes from Phase 1 (2022-2023) were compared with those from the combined Phase 2 and Phase 3 implementation period (2024-2025). Trained CHWs used digital blood pressure devices to screen adults in communities and outreach settings, refer individuals with elevated blood pressure to primary healthcare facilities, and support follow-up. Phase 1 was implemented in urban districts and targeted adults aged [&ge;]40 years, while subsequent phases expanded to adults aged [&ge;]18 years and predominantly rural and peri-urban populations. The primary outcome was hypertension screening positivity, while secondary outcomes included participant characteristics and age-specific positivity rates. Results A total of 410,568 adults were screened, including 120,144 urban adults aged [&ge;]40 years in Phase 1 and 290,424 adults in Phases 2 and 3. Among participants in Phases 2 and 3, 76.0% resided in rural communities, 64.9% were female, and 44.9% were living with HIV. Hypertension positivity was 41.0% (49,276/120,144; 95% CI 40.7%-41.3%) in Phase 1 and 14.5% (41,972/290,424; 95% CI 14.3%-14.6%) in Phases 2 and 3 (p<0.001). Positivity increased significantly with age in both periods, ranging from 31.8% to 51.6% in Phase 1 and from 13.5% to 28.4% in later phases (all p<0.001). Conclusion Community-based hypertension screening delivered by CHWs successfully reached large urban and rural populations and identified substantial hypertension burden, particularly among older adults. The lower positivity observed in later phases likely reflects differences in age eligibility and population mix rather than programme effect. Scaling CHW-led screening may strengthen decentralized hypertension detection, although nationally representative surveys and longitudinal studies are needed to assess linkage to care, treatment initiation, and long-term blood pressure control. Key Words Hypertension; Community health workers; Community-based screening; Primary healthcare; Decentralized care; Zimbabwe.

</details>

### [Monitoring SNAP and Food Insecurity After the One Big Beautiful Bill Act: Early Evidence from a National Longitudinal Cohort](https://www.medrxiv.org/content/10.64898/2026.11.19.26368514v1)
*Robertson, M.; Sanborn, J.; Penrose, K. et al.* · `health policy` · medRxiv doi:10.64898/2026.11.19.26368514 v1 · relevance 0.05

- **In one sentence**: A short longitudinal cohort study of 844 low-income U.S. adults tracks SNAP receipt and food insecurity from August 2025 to March 2026, comparing states that did and did not yet enforce the expanded OBBBA work requirement.
- **In plain words**: This paper looks at what happened to food aid and hunger in the U.S. after a 2025 federal law tightened eligibility for the Supplemental Nutrition Assistance Program (SNAP, formerly called food stamps) and added work requirements. The researchers followed 844 lower-income adults over about seven months. They found SNAP use dipped slightly, from 40.4% to 38.4%, while the share screening positive for food insecurity rose from 48.1% to 51.2%.
- **Why it matters**: It is an early, real-time look at how a major benefit change may affect household food needs, and the authors argue that people who left SNAP were still struggling. The text reports no clear difference between states that started enforcing the work rule and those that had not, but the study is short and its findings are preliminary.
- **Background needed**: - SNAP: the U.S. federal food assistance program that helps low-income households buy groceries.
- OBBBA (One Big Beautiful Bill Act): a law signed in July 2025 that restricted SNAP eligibility and expanded its work requirements.
- Work requirement: a rule that adults must work or meet other activity criteria to keep benefits; states began enforcing it at different times.
- Food insecurity: uncertain or limited access to enough food because of money or resources; "screening positive" means a short survey flagged it.
- Federal poverty guideline: the income threshold used for program eligibility; 200% means twice that level.
- Longitudinal cohort: the same group of people is surveyed repeatedly over time, so changes can be tracked for individuals.
- Quasi-comparison by state: comparing states with and without early enforcement, a design that can show associations but not prove cause. · level: intermediate

<details><summary>Original abstract</summary>

The One Big Beautiful Bill Act (OBBBA), signed in July 2025, restricted eligibility for the Supplemental Nutrition Assistance Program (SNAP) and expanded its work requirement, while federal tracking of food insecurity was scaled back. Using a national, community-based longitudinal cohort, we examined changes in SNAP receipt and food insecurity between August 2025 and March 2026 among 844 adults with household income below 200% of the federal poverty guideline, comparing participants in states that had and had not begun enforcing the expanded work requirement. SNAP receipt fell from 40.4% to 38.4%, and the share screening positive for food insecurity rose from 48.1% to 51.2%, with no detectable difference by state implementation timing. Adults who discontinued SNAP were as likely to be food insecure (71.1% in March 2026) and as worried about affording food, housing, and utilities as those who continued SNAP, and few had moved above 200% of the poverty guideline. These early findings suggest that need persisted after SNAP ended. As enforcement expands, policy makers should consider measures that keep benefits flowing to eligible people, such as extended certification periods and simplified recertification, and should support longitudinal monitoring of food insecurity.

</details>

## Psychiatry and neurology

### [Chronic pain and cognitive performance in dementia caregivers: Insights from the STELLA and DETECT-AD studies](https://www.medrxiv.org/content/10.64898/2026.11.24.26368703v1)
*McClure, C.; Mattek, N.; Kaye, J. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.24.26368703 v1 · relevance 0.09

- **In one sentence**: A secondary analysis of 12-month data from the STELLA and DETECT-AD studies (95 participants) comparing chronic pain and Montreal Cognitive Assessment scores between dementia caregivers and non-caregivers, with age-adjusted group differences in pain intensity.
- **In plain words**: Many people caring for a relative with Alzheimer's or another dementia are also living with long-term pain, but this has received little study. This paper compared caregivers and non-caregivers in a group of 95 people followed for a year. It found that caregivers were younger, scored somewhat higher on a memory and thinking test, and reported more pain intensity even after accounting for age.
- **Why it matters**: Caregiver health is often overlooked, and this paper suggests pain may be one part of it that deserves attention, including through telehealth caregiver support programs. The link between pain and thinking ability is still unclear from this work, and the sample is small and the design is a secondary analysis, so the findings are preliminary.
- **Background needed**: - Dementia: a group of diseases, such as Alzheimer's, that progressively impair memory and thinking.
- Informal caregiver: an unpaid family member or friend who helps care for a person with dementia.
- Chronic pain: pain lasting months or longer; ratings here were on a 0-10 intensity scale plus a measure of how much pain interferes with daily life.
- Montreal Cognitive Assessment (MoCA): a short screening test of thinking and memory; higher scores mean better performance.
- Secondary analysis: re-analysis of data collected for other studies, not a trial designed for this question.
- Odds ratio (OR): how much more likely a higher pain rating is in one group; OR 1.42 with a confidence interval of 1.00 to 2.01 sits right at the edge of statistical significance.
- Telehealth: delivering health care or support remotely, often by phone or internet. · level: intermediate

<details><summary>Original abstract</summary>

Background: Approximately 75% of individuals with Alzheimer's disease and related dementias rely on informal caregivers, yet caregiver health, including chronic pain, remains under-addressed. Chronic pain is highly prevalent, functionally limiting, and linked to cognitive vulnerability, but remains understudied in informal caregivers. This study examined differences in pain and cognitive performance between caregivers and non-caregivers. Objective: To compare chronic pain and cognitive performance between dementia caregivers and non-caregivers and determine whether differences persist independent of age. Methods: We conducted a secondary analysis of longitudinal data from STELLA and DETECT-AD. Ninety-five participants were followed for 12 months. Weekly online questionnaires assessed pain intensity (0-10 scale) and pain interference (Likert scale), while annual in-person evaluations measured cognition using the Montreal Cognitive Assessment. Group differences were evaluated using t-tests and multivariate regression adjusting for age. Results: Groups were similar in sex and education but differed in age, pain, and cognition. Caregivers were significatnly younger (71.3 vs 77.3 years; p < 0.0001) and caregivers demonstrated significatnly higher global cognitive performance as measured by the MoCA (mean score 26.8 vs 25.2; p = 0.02). After age adjustment, caregivers reported significantly higher pain intensity (OR 1.42, 95% CI 1.00-2.01; p = 0.048). Conclusions: Dementia caregivers exhibit greater pain burden despite younger age, highlighting chronic pain as a critical, underrecognized dimension of caregiver health and identifying an important opportunity to expand existing telehealth caregiver support models.

</details>

### [Integrating Plasma Brain-Derived pTau217, White Matter Hyperintensity and Hippocampal Volumes as Optimized Prognostic Markers for Cognitive Decline in an Asian Cohort with High Cerebrovascular Disease Burden](https://www.medrxiv.org/content/10.64898/2026.11.23.26368742v1)
*Chong, J. R.; Hilal, S.; Karikari, T. K. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.23.26368742 v1 · relevance 0.08

- **In one sentence**: In 523 Singaporean adults without dementia or with mild dementia, a combined panel of plasma brain-derived pTau217, white matter hyperintensity volume and hippocampal volume predicted faster annual decline in CDR-SB, with decline rising as more biomarkers were abnormal.
- **In plain words**: This study asks whether blood tests and brain scans can together predict who will lose memory and thinking ability faster. Researchers followed 523 people from memory clinics and the community in Singapore for about four years on average. They found that three markers combined (a blood marker of Alzheimer's-related protein, a scan measure of small vessel damage in the brain's white matter, and a scan measure of hippocampus size) tracked with faster decline, and the more markers that were abnormal, the faster the decline.
- **Why it matters**: Many people with memory problems have both Alzheimer's changes and blood vessel damage, and a cheap, combined test could help sort who needs closer follow-up. The text reports associations in one cohort, so it does not show these markers would improve care for patients elsewhere; that would need further testing.
- **Background needed**: - Alzheimer's disease is marked by abnormal proteins in the brain; pTau217 is a form of tau protein that can be measured in blood.
- "Brain-derived" tau is tau thought to come from brain cells, measured in blood samples.
- White matter hyperintensities are bright spots on MRI scans indicating small blood vessel disease in the brain's wiring.
- Hippocampal volume is the size of a memory-related brain region on MRI; shrinkage suggests neurodegeneration.
- CDR-SB (Clinical Dementia Rating Sum of Boxes) is a clinician-rated score of memory and daily function; its yearly change is the "slope" used as the outcome.
- Biomarkers were dichotomised into positive or negative, giving groups with zero to three positive markers.
- Cerebrovascular disease refers to problems with blood vessels supplying the brain. · level: research-level

<details><summary>Original abstract</summary>

Abstract Background: Combination of plasma and neuroimaging biomarkers associated with Alzheimer's disease (AD) and cerebrovascular pathophysiology might provide more accurate prediction of cognitive decline in populations with extensive AD and cerebral small vessel disease copathologies. Here, we aimed to identify an optimized biomarker panel for predicting cognitive decline by evaluating combinations of plasma and magnetic resonance imaging (MRI) biomarkers. Methods: We investigated participants without dementia or with mild dementia, recruited from memory clinics and the community in Singapore between August 2010 and August 2020. Plasma biomarkers of brain amyloid (brain-derived [BD]-pTau217, BD-pTau181, BD-pTau231, total-pTau217, total-pTau181, and total-pTau231), astrogliosis (GFAP), and neuroaxonal injury (NfL), with MRI measures of cerebrovascular disease (white matter hyperintensity [WMH] volume) and neurodegeneration (hippocampal volume), and primary outcome of longitudinal Clinical Dementia Rating Sum of Boxes (CDR-SB; mean [SD] follow-up duration, 51.0 [15.8] months). All plasma and MRI biomarker combinations for predicting CDR-SB slope (annual change in CDR-SB) were evaluated. Results: This study included 523 participants (mean [SD] age, 72.4 [7.9] years; 291 females [55.6%]). The parsimonious model included plasma BD-pTau217, WMH volume, and hippocampal volume (all P [&le;] 0.004). Dichotomizing these biomarkers yielded A, V, and N status, respectively, classifying participants as all negative (A-V-N-; n = 128), 1-positive (A+V-N-, A-V+N- or A-V-N+; n = 154), 2-positive (A+V+N-, A+V-N+, A-V+N+;n = 158) or 3-positive (A+V+N+; n = 83). Annual CDR-SB progression increased stepwise with the number of positive biomarkers. Compared with the all negative group ({beta}, 0.016), the 1-positive ({beta}, 0.409), 2-positive ({beta}, 1.16) and 3-positive groups ({beta}, 1.49) showed faster cognitive decline (all P < 0.001). Moreover, the 2-positive and 3-positive groups progressed faster than the 1-positive group (both P < 0.001), and the 3-positive group declined faster than 2-positive group (P = 0.009). Conclusions: Presence of multiple pathophysiological processes was associated with greater cognitive decline, highlighting the utility of a comprehensive multimodal biomarker profile to enhance prognostication.

</details>

## Oncology

Nothing notable this time.

## Health informatics and medical AI

### [Tabular Foundation AI Models in Healthcare: A WHO-Inspired Benchmark for Responsible AI and Trustworthiness](https://www.medrxiv.org/content/10.64898/2026.11.23.26368797v1)
*Hasan, K. S.; Borsha, M. A. A.; Ritu, R. J. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368797 v1 · relevance 0.06

- **In one sentence**: A benchmark comparing four tabular foundation models (TabFM, TabPFN, TabDPT, TabICL) against logistic regression and XGBoost on ten WHO-aligned healthcare classification datasets, scored on discrimination, sex-based fairness, calibration, and robustness to feature noise.
- **In plain words**: Hospitals and researchers increasingly try general-purpose AI models that learn from spreadsheet-style patient tables, but accuracy alone does not show whether they are fair, reliable in their confidence, or stable when data is slightly off. This paper builds a standardized test suite of ten health datasets and scores four such models and two traditional methods on 20 measures. The models did somewhat better than the traditional baselines on average, but the differences among the four new models were not statistically significant, and the simple logistic regression was the most stable under noisy inputs.
- **Why it matters**: Health-care uses of AI need evidence beyond headline accuracy, and this work offers a public benchmark with code and dataset variants that others can reuse. The authors themselves say that external validation and dataset-specific checks are still needed before any clinical use, so the results should be read as a comparison on these ten datasets rather than a verdict on clinical readiness.
- **Background needed**: - Tabular data: structured tables of rows and columns, such as patient records and lab values.
- Foundation model: a large model pretrained on broad data that can be applied to new tasks, here used on tables without task-specific training.
- Baselines: logistic regression and XGBoost (a widely used tree-based method), the standard comparison points.
- Discrimination (AUROC): how well a model ranks positive cases above negative ones; 1.0 is perfect, 0.5 is chance.
- Calibration: whether predicted probabilities match real frequencies; expected calibration error (ECE) measures the gap, lower is better.
- Fairness across sex: whether performance differs between male and female patients.
- Robustness: how much predictions change when inputs are randomly perturbed with Gaussian noise.
- Friedman test with Holm correction: standard statistical tests for comparing several models across datasets while controlling false positives.
- Composite score (CMES): a single summary combining many metrics; its weighting shapes the ranking. · level: intermediate

<details><summary>Original abstract</summary>

Tabular foundation models (TFMs) are increasingly used for structured prediction, yet their suitability for healthcare applications remains uncertain because predictive performance alone does not establish fairness, probabilistic reliability, or robustness. We developed a multidimensional benchmark to compare four TFMs: TabFM, TabPFN, TabDPT, and TabICL, against Logistic Regression and XGBoost across a curated, standardized suite of ten WHO-aligned healthcare classification datasets across diverse disease domains. Additionally, we harmonized clinical schemas, standardized protected sex attributes and outcome targets, and released both balanced-scale and natural-prevalence variants of the datasets to establish a benchmarking resource in healthcare machine learning. All models were evaluated using identical five-fold stratified cross-validation partitions and standardized preprocessing. Performance was assessed using 20 metrics spanning predictive discrimination, sex-based fairness, probability calibration, and robustness to Gaussian feature perturbations. A composite Clinical Model Evaluation Score (CMES) was used to summarize performance across these dimensions. Google TabFM achieved the highest mean CMES (0.8811), followed closely by TabDPT (0.8796), TabICL (0.8775), TabPFN (0.8756), XGBoost (0.8650), and Logistic Regression (0.8549). The Friedman test indicated significant differences among models ({chi}2F (5) = 24.914, p = 1.45 x 10^-4; Kendalls W = 0.498). However, post-hoc comparisons revealed no statistically significant differences among the four TFMs after Holm correction. TFMs generally demonstrated stronger discrimination and probabilistic calibration than conventional baselines, with TabFM achieving the highest mean Area Under the Receiver Operating Characteristic (0.9327) and the lowest expected calibration error (0.0674). Conversely, Logistic Regression exhibited the greatest stability under feature perturbations, while fairness performance varied substantially across datasets and models. These findings highlight the potential of TFMs for small-data healthcare prediction while demonstrating that their advantages are dimension-dependent. Multidimensional, dataset-specific evaluation and external validation remain essential before clinical implementation. All analysis codes, original datasets, and multiple variants of benchmark datasets are publicly available in a GitHub repository to ensure reproducibility and future research.

</details>

### [Concerns over spillover, exclusions, and hospital unit differences in an AI early warning system trial (CONCERN-EWS)](https://www.medrxiv.org/content/10.64898/2026.11.23.26368768v1)
*Mann, S.; Berdahl, C. T.; Griffin, B. A.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368768 v1 · relevance 0.05

- **In one sentence**: A letter raising methodological concerns (ICU bed spillover, exclusion of high-risk patients after EWS-informed decisions, and cluster-level imbalance) about the CONCERN-EWS cluster-randomized trial, which reported a lower mortality hazard with an AI early warning system.
- **In plain words**: Hospitals are testing an AI tool that flags patients who may be getting worse, so staff can act sooner. This letter is a critique of a trial that found patients cared for on units using the tool were less likely to die, and it asks whether that result might be overstated. The writers point to three possible problems: control-group patients may have been hurt when intensive care beds were scarce, high-risk patients may have been left out of the tool group after staff decisions, and some hospital units already differed a lot in death rates before the trial began.
- **Why it matters**: Trials that test whether AI tools improve patient outcomes are still uncommon, so how such trials are designed and read matters for judging the evidence. The letter is a critique of one study; the text does not show whether the authors of the original trial would change their conclusions.
- **Background needed**: - Early warning system (EWS): software that scores patients' risk of deterioration from their records and alerts clinicians.
- Cluster-randomized trial: whole hospital units, not individual patients, are randomly assigned to the tool or usual care.
- Hazard ratio (HR): a comparison of how quickly an event happens between groups; 0.64 means about 36% lower rate of death in the tool group, per the cited result.
- Spillover: effects of the intervention leaking into the control group, such as competition for shared resources like ICU beds.
- Between-cluster variance and imbalance: differences between units that exist before randomization or vary widely, which can distort results.
- The letter gives only the summary of the trial's result; it does not present new data of its own. · level: research-level

<details><summary>Original abstract</summary>

Rossetti et al. report that hospitalized patients whose care was informed by an AI-based clinical deterioration early warning system (EWS) were 36% less likely to die during a pragmatic cluster-randomized trial when compared to patients on usual care units without the EWS (adjusted hazard ratio [HR], 0.64; 95% confidence interval [CI], 0.53-0.78).1 The authors should be applauded for conducting a trial evaluating the effect of an AI intervention on patient health outcomes; more such trials are needed. Several aspects of the study, however, raise concerns that its findings may not accurately reflect the effect of the EWS. First, spillover effects on availability of scarce intensive care unit (ICU) beds could have led to worse outcomes for patients in the control group. Second, EWS-informed clinical decisions may have led to more frequent exclusion of high-risk patients from the intervention group. Either of these concerns could have led to overestimation of AI benefit. Finally, large pre-trial differences in hospital unit mortality rates suggest that unreported cluster-level imbalance or between-cluster variance could also have affected trial results.

</details>

## Econometrics and applied economics

### [Will AI Replace Juniors? How Task Complexity Reduces Automation Risk](https://arxiv.org/abs/2611.34099)
*Vincent Rost, Fabian Stephany* · `econ.GN` · arXiv:2611.34099v1 · relevance 0.05

- **In one sentence**: A pre-registered survey experiment with managers at 1,435 German firms finds that tasks requiring judgement and independent problem-solving reduce managers' stated preference for AI over entry-level hiring, and that managers expect AI to reduce entry-level hiring more than experienced hiring.
- **In plain words**: This paper asks whether companies are more likely to use AI instead of hiring junior staff when the work is simple and routine versus when it is complex. Managers at German firms in IT-related services and manufacturing were randomly given one of two kinds of job need, and the researchers compared their answers. They found that complex work made managers less willing to choose AI over a new entry-level hire, and made them value human oversight more.
- **Why it matters**: It speaks to a live worry that AI will squeeze out junior jobs, and it suggests the task's complexity, not just the technology, shapes that risk. Because the results are stated intentions from a survey, they show what managers say they would do rather than what firms actually do.
- **Background needed**: - Entry-level (junior) employees: staff at the start of their careers, often doing more standardised tasks.
- Survey experiment: participants are randomly assigned to different scenarios so that differences in answers can be attributed to the scenario.
- Pre-registered: the researchers published their plan before collecting data, which limits selective reporting.
- Five-point scale: managers rated their answers from 1 to 5; the reported effect is 0.54 points on that scale.
- Information economy: firms in IT and information-related services.
- Human oversight: people checking or supervising the output of automated tools.
- Pre-treatment responses: answers given before the scenario was shown, used here to gauge general expectations about AI. · level: intermediate

<details><summary>Original abstract</summary>

How does task complexity shape firms' willingness to substitute entry-level labour with artificial intelligence (AI) tools? We study this question using a pre-registered survey experiment with managers from 1,435 German firms in the information economy and manufacturing industry. Managers are randomly assigned to consider a long lasting need for additional capacity involving either well-structured and standardised tasks, or more complex tasks that require professional judgement, contextual knowledge and independent problem-solving. Relative to standardised tasks, complex tasks reduce willingness to use AI rather than hire an entry-level employee by 0.54 points on a five-point scale and increase the importance attached to human oversight by 0.15 points. Further, pre-treatment responses indicate that managers expect the availability of AI applications to reduce hiring of both entry-level employees and experienced workers, but significantly more strongly for entry-level workers.

</details>

### [Geodesic Causal Forests: Learning Heterogeneous Treatment Effects for Random Objects](https://arxiv.org/abs/2611.33350)
*Yidong Zhou* · `stat.ME` · arXiv:2611.33350v1 · relevance 0.05

- **In one sentence**: The paper proposes geodesic causal forests, a tree-based method that estimates heterogeneous treatment effects when outcomes are random objects in curved metric spaces (such as compositions, covariance matrices, distributions, or networks), using a squared-distance loss corrected for nuisance error in place of Euclidean residuals.
- **In plain words**: Many studies now measure outcomes that are not simple numbers, such as the mix of activities a person spends time on or a table of how variables move together. This paper gives a way to estimate how a program changes such outcomes for different kinds of people, by moving each change along a shortest path in the space of these objects so that effects can be compared. The authors report simulations with covariance-matrix outcomes where their correction substantially reduces estimation error, and an application to women's livelihood time-use data from a Bangladesh antipoverty program.
- **Why it matters**: Outcomes that are compositions, networks, or distributions are common in economics and other fields, but standard causal forest tools assume outcomes can be added and subtracted. The text suggests the approach extends doubly robust learning to these settings, and it reports consistency and convergence results, though the application's findings are only summarized here and the wider uptake of the method is not established.
- **Background needed**: - Treatment effect: the difference a program or intervention makes for a given person compared with no intervention.
- Heterogeneous treatment effects: how that difference varies across people with different characteristics.
- Causal forest: an ensemble of decision trees that splits people into groups with similar treatment effects.
- Doubly robust / orthogonal learning: estimation methods that stay accurate if either of two supporting models is roughly right, and that limit the damage from errors in those models.
- Metric space and geodesic: a set of objects with a notion of distance; a geodesic is the shortest path between two objects in that space.
- Fréchet mean: the generalization of an average to objects that cannot be added, defined as the point minimizing total squared distance to the data.
- Compositions: data whose parts sum to a whole, such as the shares of time spent on different activities. · level: research-level

<details><summary>Original abstract</summary>

Causal forests and orthogonal learners estimate heterogeneous treatment effects for scalar or Euclidean outcomes, yet outcomes are increasingly random objects, such as compositions, covariance matrices, distributions, or networks, in metric spaces without linear structure. We introduce geodesic causal forests for conditional geodesic treatment effects. Geodesic transport moves each geodesic between conditional Fr\'echet means of the potential outcomes to a common reference, making effects comparable across individuals. Because random objects cannot be added or subtracted, Euclidean residual corrections are unavailable; we instead correct the squared-distance loss through which the forest selects splits and estimates effects. The loss is real-valued for every candidate effect, so the correction requires only Fr\'echet means and leaves second-order nuisance error; for Euclidean outcomes, it recovers doubly robust learning. We establish consistency, convergence rates, and split-selection guarantees under conditions verified for curved and nonsmooth spaces. In simulations with covariance-matrix outcomes, the correction substantially reduces estimation error. For women's livelihood compositions in BRAC's randomized antipoverty program in Bangladesh, new livestock work mainly replaces casual wage work; after alignment, a single effect reproduces much of the variation in percentage-point changes across baseline activities, and the fitted effects are largest among former domestic workers and older women.

</details>

## Economic theory

### [Lone Wolves and Lattices in Bayesian Matching with Transfers](https://arxiv.org/abs/2611.34524)
*Xiyu Li* · `econ.TH` · arXiv:2611.34524v1 · relevance 0.05

- **In one sentence**: This paper studies Lone Wolf and lattice properties of stable outcomes in one-to-one matching with transferable utility and one-sided incomplete information, using Bayesian stable market states, and shows which properties hold or fail under an additive-separability condition on workers' matching values.
- **In plain words**: The paper looks at how workers and firms get paired when the firms cannot see each worker's full private type, and money (wages) can be used to settle the deal. It shows by example that some tidy properties of stable pairings can break down in this setting. Under an added condition, where a worker's value is the sum of a part depending on his type and a part depending on the firm, it proves that a firm left unmatched in one stable outcome earns zero in every stable outcome, and that the payoffs across stable outcomes form a lattice (a set with well-behaved "best for one side" options).
- **Why it matters**: The results clarify when stable matching outcomes have predictable structure under incomplete information, which matters for markets where wages also signal information. The text does not indicate applications or empirical tests, so its wider relevance is unclear from this text alone.
- **Background needed**: - Matching market: agents on two sides (workers and firms) are paired; a stable outcome is one where no pair would rather break off and deal with each other.
- Transferable utility: payments such as wages can move between the two sides.
- One-sided incomplete information: firms do not know some private worker characteristics (the worker's "type"), but workers know theirs.
- Bayesian stability: stability judged using firms' beliefs (posterior probabilities) about worker types after observing offers.
- Lone Wolf property: a rough statement that the set of agents left unmatched is the same across stable outcomes.
- Lattice: a set of outcomes closed under taking "better for one side" and "better for the other" combinations, so an optimal outcome for each side exists.
- Additive separability: the value splits into a sum of a type term and a firm term.
- Comonotonicity and posterior independence: technical conditions on how preferences and beliefs line up across workers, extended by the paper. · level: research-level

<details><summary>Original abstract</summary>

I study the Lone Wolf and lattice properties of stable outcomes in one-to-one matching with transferable utility and one-sided incomplete information, using the Bayesian stable market states of Liu (2020) and Chen and Hu (2024). With transfers, the wage in a blocking offer screens the worker's types, so it determines both whom the firm attracts and what the firm learns. I show by example that the firm-side and matched-set versions of the Lone Wolf property, as well as the lattice property, can fail even when outcomes are compared under the same information structure. I then assume that each worker's matching value is additively separable in his type and the firm's identity. Under this condition, a firm that is unmatched in some stable outcome earns zero in every stable outcome with the same type profile and information structure. Workers can retain information rents, so the worker-side property can fail. Nevertheless, outside a finite union of affine hyperplanes in the space of firm values, all such stable outcomes leave the same agents unmatched. Whenever they do, the stable payoff vectors form a lattice, and worker-optimal and firm-optimal outcomes exist. The results extend to comonotonicity of relative preferences when posterior beliefs are independent across workers.

</details>

## Game theory and algorithmic economics

### [Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games](https://arxiv.org/abs/2611.34536)
*Rishi Bharadwaj, Sujit Gujar, Yadati Narahari* · `cs.LG` · arXiv:2611.34536v1 · relevance 0.07

- **In one sentence**: Proposes Kant-Q, a Q-learning variant that learns Kantian equilibria (each agent picks the action it would want all agents to take) in symmetric Markov games, with convergence and Pareto-efficiency results and experiments on the iterated Prisoner's Dilemma and the GovSim fishery game.
- **In plain words**: The paper looks at how AI agents learn to act when their goals partly conflict, such as several fishers sharing one lake. Instead of aiming for the usual "no one wants to switch" outcome, which can be wasteful for everyone, it targets a rule where every agent asks what would happen if everyone did what it does. The authors report that their algorithm, Kant-Q, reliably learns this kind of outcome in the tested games, including versions with up to 200 agents.
- **Why it matters**: Many multi-agent learning methods settle on outcomes that are inefficient for everyone, so a method aimed at cooperative, efficient play is relevant to AI safety and multi-agent design. The authors argue that copies of the same AI system often face each other, which makes this symmetric setting especially practical; how far the results carry to mixed or non-identical agents is not something the text establishes.
- **Background needed**: - Markov game: a repeated decision problem where several agents act at once and each one's reward depends on everyone's actions.
- Q-learning: a standard trial-and-error method where an agent learns the value of each action in each situation, with known convergence guarantees for single-agent problems.
- Nash equilibrium: a state where no agent gains by changing its own action alone; it can still be inefficient for all.
- Pareto-efficient: no outcome exists that makes someone better off without making someone else worse off.
- Symmetric game: all agents have the same options and payoffs, so one shared strategy can apply to everyone.
- Kantian equilibrium: each agent chooses the action it would want every agent to take (universalization), which in symmetric games means a shared optimal common policy.
- Iterated Prisoner's Dilemma and GovSim fishery: standard test games for cooperation, where defecting or overfishing benefits one agent at the group's expense. · level: research-level

<details><summary>Original abstract</summary>

AI agents increasingly interact with one another, and many of these interactions are mixed-motive games, which have posed a persistent challenge for learning algorithms. Most multi-agent reinforcement learning (MARL) algorithms are designed to reach Nash equilibria, yet in many such games these equilibria are Pareto-inefficient. We instead study Kantian equilibria, an economic solution concept in which each agent plays the action it would want all agents to adopt. In symmetric games, this corresponds to an optimal common policy. We propose Kant-Q, a Q-learning algorithm in which each agent learns action profiles where all agents play the same action. Each update is then a sample from a single-agent MDP, so Kant-Q inherits the convergence guarantees of standard Q-learning. We show that every symmetric Markov game has a pure Kantian equilibrium. We also prove that all agents' Q-tables converge to the same limit, whose greedy policy is such an equilibrium, and that greedy play converges whenever the optimal common action is unique at every state. We further show that in a subclass of symmetric monotone games, the Kantian equilibrium is Pareto-efficient among pure strategy profiles and strictly individually rational. Empirically, on the iterated Prisoner's Dilemma and the GovSim fishery with up to 200 agents, Kant-Q learns the Kantian equilibrium, while the baselines underperform. Since copies of the same AI system naturally face one another in symmetric games, these results suggest universalization as a design principle for cooperative AI-AI interaction.

</details>

### [Last-Iterate Equilibrium Learning in Symmetric Congestion Games under Semi-Bandit Feedback](https://arxiv.org/abs/2611.34861)
*Katerina Michou, Marina Kontalexi, Dimitris Fotakis* · `cs.GT` · arXiv:2611.34861v1 · relevance 0.07

- **In one sentence**: The paper gives a last-iterate learning guarantee for mixed Nash equilibria in atomic symmetric congestion games under resource semi-bandit feedback, using a quadratic consensus penalty to make the potential strongly convex and an online projected gradient descent variant.
- **In plain words**: The paper studies how many independent players, each choosing among shared resources like roads, learn a stable pattern of choices when they only see the cost and usage of the options they actually picked. The authors add a penalty term that pulls the players toward treating each other symmetrically, which makes the problem well-behaved enough to reach the equilibrium. They report that a modified gradient-descent style update gets the played choices close to equilibrium at a rate of roughly t^(-2/3) in squared distance, and that the played profile converges to equilibrium almost surely.
- **Why it matters**: Congestion games model traffic, network routing and shared-resource use, so learning rules that provably settle into equilibrium with limited feedback bear on those settings. The text alone does not show how the results compare with existing methods or how practical the penalty is, so its wider significance is uncertain.
- **Background needed**: - Game theory: a Nash equilibrium is a set of strategies where no player gains by switching unilaterally; a mixed equilibrium means players randomize.
- Congestion game: each player's cost for a resource rises with how many players use it (e.g., road traffic).
- Potential function: a single score over all strategy profiles whose changes track each player's changes in cost; minimizing it finds equilibria in these games.
- Convexity: a 'bowl-shaped' function with one lowest point, which makes gradient-style methods reliable.
- Semi-bandit feedback: after acting, players observe costs for the resources they used, not for alternatives.
- Last-iterate convergence: the current strategy profile itself approaches equilibrium, not just the average over time.
- Online projected gradient descent: repeatedly nudging a strategy along the gradient of cost and projecting back onto allowed choices. · level: research-level

<details><summary>Original abstract</summary>

We study last-iterate learning of mixed Nash equilibria in atomic symmetric congestion games under resource semi-bandit feedback, where players observe both the costs and the loads of their selected resources. For strictly increasing latency functions, the restriction of the potential function to symmetric marginal profiles is strongly convex. However, players' independent stochastic updates need not preserve this symmetry without explicit synchronization. We show that a quadratic consensus penalty makes the potential globally strongly convex while making the symmetric equilibrium the unique minimizer of the transformed potential. We propose a variant of online projected gradient descent that achieves $O(t^{-2/3})$ squared distance to equilibrium and $O(t^{-1/3})$ maximum deviation gain in expectation, for every $t\geq 1$ and for any initialization. The played profile also converges to equilibrium almost surely.

</details>

## Mathematical finance

### [Distance from the Truth: Why Fragmented Merchant Underwriting Misses Risk, and What Source-Attributable Evidence Changes](https://arxiv.org/abs/2611.34696)
*Russell Lessard, Jeremy Blackburn, Tim Hines et al.* · `cs.CR` · arXiv:2611.34696v1 · relevance 0.03

- **In one sentence**: A position paper arguing that fragmented merchant underwriting misses linked risks across identity, authority, and settlement signals, and proposing a source-attributable evidence record, decision receipt, and shadow pilot design (all proposed, not observed results).
- **In plain words**: This paper is about how businesses that accept card payments get approved for merchant accounts. It argues that checking each piece of evidence separately can miss real risk, such as when a person, a company, its signatory, and the bank account receiving money are not actually connected. The authors propose a way to keep a single, traceable record of what was checked, where it came from, when, and who decided, and they describe a planned test. The text makes clear that the controls and pilot are proposals, not results from a live system.
- **Why it matters**: Merchant onboarding is a common route for fraud and money-laundering, so better evidence trails matter to banks and payment processors. The paper ties its ideas to existing rules (identity, customer due diligence, sanctions, card-network and Nacha requirements), but it reports no measured outcomes, so its practical value is still untested.
- **Background needed**: - Merchant underwriting: a bank or payment processor's check before letting a business accept card payments.
- Identity proofing and customer due diligence (CDD): rules requiring firms to verify who their customers are and who owns or controls them.
- Sanctions screening: checking customers against government lists of prohibited parties.
- Card networks and Nacha: the organizations (e.g., Visa, Mastercard, and Nacha for ACH transfers) that set rules for payment processing.
- Point-in-time check: a verification that was true on one past date but may no longer be current.
- Provenance: the record of where a piece of evidence came from and how it was obtained.
- Shadow enrollment pilot: running a new process alongside the existing one without using it to make live decisions.
- The "ChainIT Transaction Truth Architecture" is a named framework from the source; the text does not explain it in detail. · level: intermediate

<details><summary>Original abstract</summary>

Merchant underwriting becomes vulnerable when evidence is evaluated without enough visibility into its source, freshness, relationship to the applicant, or meaning for the proposed activity. Individually favorable checks do not necessarily establish that the same business is operating the merchant account, that its representative may bind it, or that its settlement instructions are authorized. We describe three failure modes of fragmented underwriting: distance from the source, the gap between a decision and the evidence needed to justify it; the correlation gap, in which material relationships among the person, legal entity, owners or controllers, representative, business activity, and settlement destination are not evaluated when each signal is considered alone; and point-in-time controls, in which a historical verification is treated as present eligibility. We map these failure modes to identity-proofing, customer-due-diligence, sanctions, third-party-risk, card-network, and Nacha requirements, and propose a merchant-underwriting application of the ChainIT Transaction Truth Architecture built on provenance, correlation, and persistence. The application keeps a logically unified evidence record that identifies what was checked, the subject and relationship involved, the relevant times, the applicable policy, the decision, and any exceptions, and it keeps evidence validation, applicant verification, organizational authority, and the institution's risk judgment separate. We also set out a proposed evidence and decision receipt, a defined 90-day shadow enrollment pilot with adjudicated outcome measures and deliberate control-failure tests, and a ten-question self-assessment. Proposed controls, illustrative scenarios, and pilot measures are identified as such and are not represented as observed production results.

</details>

## Financial markets

Nothing notable this time.

## Signal processing

### [AutoRSP: An AI Agent for Radar Sensing Pipeline Design](https://arxiv.org/abs/2611.34754)
*Zhi Zheng, Xincheng Xie, Avery Gump et al.* · `cs.NI` · arXiv:2611.34754v1 · relevance 0.11

- **In one sentence**: AutoRSP is an AI agent that designs end-to-end radar sensing pipelines across five stack layers, using RF simulation, on-sensor emulation and real edge-device runs as feedback instead of an LLM judge, with efficiency methods for the slower feedback loop.
- **In plain words**: Radar systems need a chain of work that spans the physical hardware and the software that processes its signals, and building that chain usually takes expert time and money. This paper asks whether an AI agent can design such a chain automatically. The authors report that their agent, AutoRSP, produced runnable pipelines for robotic imaging, car perception, and vital-sign sensing, with performance described as comparable to or better than human-expert pipelines and some closed-source AI agents.
- **Why it matters**: Automating radar pipeline design could lower the cost and expertise needed to build sensors for robots, cars and health monitoring. The text does not give detailed comparison numbers, so the strength of the performance claims cannot be judged from this summary alone; the authors also say they will release their tools and benchmarks.
- **Background needed**: - Radar: sensing by sending radio waves and reading their echoes; RF means radio-frequency.
- Sensing pipeline: a sequence of stages from hardware settings to signal processing to final output.
- AI agent: a language model that plans and runs a series of tool calls, here searching over pipeline designs.
- LLM judge: a language model used to score candidate designs; AutoRSP instead uses physical simulation and real hardware tests.
- On-sensor emulation and edge devices: testing on a model of the sensor and on small local computing hardware.
- Agentic loop: the repeated cycle of propose, test, and refine that the agent performs. · level: research-level

<details><summary>Original abstract</summary>

Radar sensing demands a pipeline that is well-thought-out across hardware and software. We ask whether an AI agent can automatically design radar sensing pipelines at a fraction of the time, cost, and expertise that current practice needs. We present AutoRSP, an agent that embeds radar-system-level structure through sub-agents mapped to five stack layers, a code-based representation of every layer with explicitly modeled cross-layer dependencies. Feedback for the agentic search process comes from a pipeline of realistic RF simulation, on-sensor emulation, and execution on real edge devices, rather than from an LLM judge. Because such feedback can be slower than an LLM call, we present methods to efficiently optimize agentic loops. We evaluate AutoRSP on robotic imaging, automotive perception, and vital sign sensing. It produces executable pipelines with performance comparable to or better than human-expert pipelines and closed-source agents. AutoRSP's harness, tools, and benchmarks will be released to bridge the rising gap in agentic research abilities outside of frontier labs.

</details>

### [Doppler RaDAR Single-Frame Anomaly Detection and Consistency Assessment by Velocity-Conditioned Gaussian Spectral Modeling](https://arxiv.org/abs/2611.34639)
*Malte Stelzer, Timo Bartels, Dinu Mihailescu-Stoica et al.* · `eess.SP` · arXiv:2611.34639v1 · relevance 0.08

- **In one sentence**: A velocity-conditioned Gaussian spectral model, with a neural encoder and decoder, scores single frames of railway radar Doppler spectra for anomalies and checks whether the estimated speed is consistent with the measured spectrum, without needing ground-truth velocity at inference.
- **In plain words**: Trains in railway vehicles need to know how fast they are moving, and they often estimate this with radar. This paper asks a different question: is the radar signal itself believable, not just the speed number it produces. The authors built a system that predicts speed from a radar frequency pattern, then checks that pattern against what a healthy measurement should look like at that speed.
- **Why it matters**: Speed estimates can look plausible even when the underlying radar data are corrupted, so a measure of measurement plausibility could help flag unreliable readings in safety-relevant automation. The text reports that the disagreement score tracks real speed errors closely for the anomaly types tested, but the study is limited to controlled, investigated anomalies, so its use on real railway conditions is not yet shown.
- **Background needed**: - Doppler radar: measures speed by how a reflected signal's frequency shifts when the target moves; the Doppler spectrum shows the strength of each frequency.
- Speed over ground: the vehicle's actual speed relative to the track, a key input for railway control.
- Neural encoder/decoder: a neural encoder turns the spectrum into a speed estimate; a decoder reconstructs the expected spectrum given a speed.
- Gaussian distribution: a bell-shaped model of expected values; a measurement far from the expected bell curve gets a high anomaly score.
- Anomaly score: a number indicating how unusual a measurement is compared with normal data.
- Pearson correlation (r): a measure from -1 to 1 of how closely two quantities move together; r above 0.99 indicates a very tight linear relationship. · level: research-level

<details><summary>Original abstract</summary>

Reliable speed-over-ground estimation is essential for automated railway vehicles. However, the accuracy of a velocity estimate alone does not indicate whether the underlying RaDAR measurement is physically plausible. This paper introduces a velocity-conditioned Gaussian spectral modeling framework for anomaly detection and velocity consistency assessment. A neural encoder estimates the vehicle velocity from complex Doppler spectra, while a Gaussian decoder models the expected spectral distribution conditioned on a velocity estimate. Three complementary inference-time online indicators are derived: the spectral anomaly score (SAS), conditional anomaly score (CAS), and absolute velocity disagreement (AVD). Experiments demonstrate the sensitivity of the scores to velocity deviations. Under controlled spectral anomalies, SAS and CAS outperform conventional spectral indicators in most conditions. Furthermore, AVD exhibits strong correlations with actual velocity estimation errors (Pearson $r>0.99$) for the investigated extra-peak and local anomalies. These results demonstrate the potential of online conditional spectral modeling to assess measurement plausibility and velocity estimation reliability without requiring ground-truth velocities during inference.

</details>

## Audio and speech

### [Music Similarity Estimation from Jukebox Embeddings](https://arxiv.org/abs/2611.34346)
*Johannes Grafinger, Gerhard Widmer, Jan Schl\"uter* · `cs.SD` · arXiv:2611.34346v1 · relevance 0.07

- **In one sentence**: The paper proposes JukeSim, which estimates content-based similarity between music recordings using embeddings from the Jukebox generative music model, and reports it performs on par with a learned baseline and better than older hand-designed methods across several datasets.
- **In plain words**: The paper looks at how to tell whether two songs sound alike using only the audio, without relying on tags, genres, or listening history. The authors use the internal numerical representations (embeddings) of Jukebox, an existing AI model that generates music, as the basis for this comparison. They report that this approach works about as well as a recent learning-based method and better than the best older hand-designed methods on several datasets, though it needs more computing power.
- **Why it matters**: Audio similarity matters for recommending new songs that have no listening history yet, the so-called cold-start problem. The paper suggests that embeddings from generative music models are a viable tool for this task, though the text gives no details on real-world deployment or how large the gains are.
- **Background needed**: - Content-based similarity: judging how alike two recordings sound from the audio itself, ignoring metadata such as artist, title, or genre.
- Embedding: a list of numbers that a neural network produces to represent a piece of audio, where similar sounds should get nearby numbers.
- Jukebox: a large generative model from OpenAI that produces music audio; its internal representations are reused here for comparison rather than for generating music.
- Cold-start recommendation: recommending items when there is no usage data about them yet.
- Hand-designed approaches: similarity measures built from fixed signal-processing features rather than learned from data.
- Compute cost: the processing power and time needed; the paper notes JukeSim is more expensive than the alternatives. · level: intermediate

<details><summary>Original abstract</summary>

Content-based music similarity estimation aims to provide a measure of similarity between music audio recordings, disregarding any associated metadata. This has potential applications in e.g. cold-start music recommendation scenarios, where there is no user interaction data. In this work, we propose JukeSim, a new approach to estimating musical similarity based on embeddings created by Jukebox, a generative music model. In evaluations on multiple datasets, we find that JukeSim performs on par with an existing learning-based approach, and both outperform the best hand-designed approaches, which had never been compared to recent work before. Even though the required compute for JukeSim is higher than for other measures, we demonstrate the viability of utilizing generative embeddings for this task, encouraging further research.

</details>

### [Line-Level Singer Diarization in Multi-Member Pop Songs: A Benchmark, Lead-Vocal Isolation, and Song-Level Decoding](https://arxiv.org/abs/2611.33247)
*Allen Ng* · `cs.SD` · arXiv:2611.33247v1 · relevance 0.05

- **In one sentence**: The paper introduces line-level singer diarization for multi-member K-pop songs, a benchmark (ColorCoded-SD) with alignment and scoring tools, and a pipeline combining lead-vocal isolation, singing-adapted speaker embeddings, and two training-free song-level decoders that improves B-cubed F1 over the standard pipeline on two datasets.
- **In plain words**: Fans of pop groups often mark which member sings each lyric line, but tools built for telling apart speakers in ordinary speech fail on songs with four to eight singers. The authors built a benchmark of 43 K-pop songs with line-by-line singer labels, and a method that first isolates the lead voice, then groups lines by singer using voice fingerprints and two song-level decoding steps that need no training. The method raised the grouping score by about 0.06 on both their benchmark and a second corpus.
- **Why it matters**: Attributing sung lines to singers could help search, captioning, and fan archives of group music, and the paper's error analysis points to where the remaining difficulty lies. The text does not indicate applications beyond this setting, so the wider relevance is uncertain.
- **Background needed**: - Speaker diarization: automatically working out "who spoke when" and grouping segments by speaker.
- Source separation / vocal isolation: splitting a mixed recording into separate parts, such as the singing voice versus the backing music.
- Speaker embedding: a numerical "voiceprint" vector summarizing how a voice sounds, used to compare segments.
- Clustering: grouping items whose voiceprints are similar, without knowing the groups in advance.
- Viterbi decoding: a method that finds the most likely sequence of labels across ordered items; "sticky" means it favors keeping the same label between neighbors.
- B-cubed F1: a score that rates how well items are grouped together with others of the same true label, balancing precision and recall.
- Training-free: the method needs no additional model training on labeled data. · level: research-level

<details><summary>Original abstract</summary>

Fans of multi-member pop groups annotate songs line by line with the member who sings each line, but speech diarization does not transfer to this setting: a commercial diarizer finds one or two speakers in songs by groups of four to eight. We study line-level singer diarization: given a song and its lyric-line timings, group the lines by singer with no prior knowledge of the group. We release ColorCoded-SD, a benchmark of 43 K-pop songs (1,740 lines, 3-8 singers per song) built from crowd annotations verified by independent annotators, together with alignment and scoring tools, and we derive line labels for the IdolSongsJp corpus from its per-singer solo renditions for evaluation on unseen singers. Combining lead-vocal isolation with a karaoke separator, singing-adapted speaker embeddings, and two training-free song-level decoders (a sticky Viterbi pass over line order and unsupervised linking of a group's songs) improves B-cubed F1 over the standard pipeline (vocal separation, speaker embeddings, per-song clustering) by +0.058 on ColorCoded-SD (p=0.001) and by +0.066 on IdolSongsJp (p=0.003). Isolating the lead is the largest single factor wherever the separator leaves a lead voice (+0.04 to +0.06 on the same lines), and with the singers' dry studio takes two different encoders become indistinguishable; the remaining errors concentrate on short lines that carry too little audio for a voiceprint. We also report negative results (more or cleaner training data, weight editing, a song-context model, and target-singer extraction) that bound where further gains can come from.

</details>

## Control systems

### [Adaptive Control Barrier Functions for Nonlinear Singularly Perturbed Systems](https://arxiv.org/abs/2611.34866)
*Prashanth Krishnamurthy, Farshad Khorrami* · `eess.SY` · arXiv:2611.34866v1 · relevance 0.16

- **In one sentence**: The paper develops an adaptive control barrier function framework for uncertain nonlinear singularly perturbed (two-time-scale) systems, giving robustness conditions that keep both slow and fast subsystems safe, with simulations on a synthetic fourth-order system and a unicycle with obstacle avoidance.
- **In plain words**: Engineers often build control systems where some parts react quickly and others react slowly, and they need to keep the system inside safe limits even when some of its physical parameters are unknown. This paper studies how to enforce such safety limits on both the slow and fast parts of these systems while the controller learns the unknown parameters online. The authors show that if the slow part is kept safe with a suitable margin, the true system stays close to the safe region when the speed-difference parameter is small, and they give conditions for joint safety of both parts.
- **Why it matters**: Safety guarantees for real machines such as vehicles or robots must hold even when models are imperfect and when some components respond much faster than others. The text reports simulation tests only, on a synthetic example and a unicycle, so its practical reach beyond these cases is not shown here.
- **Background needed**: - Control barrier function (CBF): a mathematical certificate that a system's state stays inside a safe set, used as a constraint in controller design.
- Singular perturbation / two-time-scale system: a model with fast and slow dynamics, where a small parameter (epsilon) is the ratio of the time scales; the slow part is a simplified "reduced" model.
- Adaptive control: a controller that estimates unknown parameters while it operates and updates its estimates over time.
- Robustness margin: an extra safety buffer added to compensate for the gap between the estimated and true model.
- O(epsilon) neighborhood: a region whose size shrinks in proportion to the small time-scale parameter.
- Unicycle model: a simple wheeled-robot model with forward speed and turning rate, used as a standard test case. · level: research-level

<details><summary>Original abstract</summary>

Control barrier functions (CBFs) have emerged as a flexible and efficient approach for enforcing dynamic safety constraints. In this paper, we consider a class of uncertain nonlinear systems with singular perturbations and develop an adaptive CBF framework for such systems to enforce safety constraints on both the slow and fast subsystems in the overall singularly perturbed nonlinear system with uncertain parameters. We first develop a robustness property showing that if an adaptive controller for the slow subsystem satisfies the slow CBF condition with an appropriate safety margin, then for sufficiently small values of the singular perturbation parameter $\varepsilon$, the slow subsystem remains within an $O(\varepsilon)$-neighborhood of its safe set. We then consider the more general case of safety constraints on both the fast and slow subsystems and provide conditions under which joint slow-fast safety is achieved despite the parametric uncertainties. The reduced-order slow model and the slow and fast CBF conditions are evaluated using an online parameter estimate and the parameter mismatch between the estimated and true reduced-order models is addressed via a state-dependent robustness margin in the CBF inequalities. To illustrate the proposed framework, we present simulation studies for two systems with parametric uncertainties: a synthetic two-time-scale fourth-order example system and a unicycle with a fast turn-rate actuator and an obstacle avoidance safety constraint.

</details>

### [$\mu$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation](https://arxiv.org/abs/2611.34597)
*Devesh Nath, Glen Chou* · `cs.RO` · arXiv:2611.34597v1 · relevance 0.12

- **In one sentence**: μMPC uses learned Koopman-linearized dynamics and precomputed finite-horizon control-to-output maps to shrink each model predictive control solve to an action-only quadratic program with Hn_u variables, solved by primal-dual iterations using only matrix-vector products and projections.
- **In plain words**: Model predictive control is a method where a robot or system repeatedly plans its next moves by solving an optimization problem that looks a fixed number of steps ahead. This paper presents a version designed to run very quickly, even on tiny microcontrollers and GPUs, by learning a simplified model of the system and precomputing much of the work in advance. The authors report solve times as low as 23 microseconds on a desktop CPU and 24 ms on a small drone's microcontroller, along with speedups of up to 108x for constrained control and 1907x for visuomotor planning compared with competing methods.
- **Why it matters**: Fast, constrained planning on cheap hardware matters for drones, legged robots, and other real-time systems where computation time limits control quality. The text does not show how these benchmark speedups would transfer to real-world deployments, so the practical reach is still uncertain.
- **Background needed**: - Model predictive control (MPC): at each time step, choose actions by optimizing a predicted future over a short horizon, then apply only the first action and repeat.
- Quadratic program (QP): an optimization problem with a quadratic objective and linear constraints; solving it fast is the main cost in MPC.
- Koopman operator: a way to turn a nonlinear system into a (higher-dimensional) system that evolves linearly, which makes optimization easier.
- Lifted dimension: the size of the higher-dimensional space used by the linearized model.
- Primal-dual iterations: iterative solver steps that alternately update the decision variables and the constraint multipliers.
- Microcontroller/GPU: small embedded chip and a parallel graphics processor, used here as test platforms.
- DAgger: a data-collection method where a learner gathers training data from its own behavior, with expert corrections. · level: research-level

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
