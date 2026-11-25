# Research digest · 2026-11-25
<!-- {% raw %} -->

New papers posted from about 2026-11-24 to 2026-11-25 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[The majority game chromatic number for dense random graphs](https://arxiv.org/abs/2611.32746)** (Combinatorics): The paper studies a two-player game on random networks: players take turns colouring the vertices of a graph so that no two neighbours share a colour, and the question is how few colours are needed. For random graphs where most pairs of vertices are connected (edge probability between 2/3 and 1), the authors show that three colours are enough with high probability, meaning the chance of this holding tends to 1 as the graph grows.
- **[Tuning evolutionary information in MSAs shapes protein generation and folding](https://www.biorxiv.org/content/10.64898/2026.11.23.768656v1)** (Computational and systems biology): Protein models often learn from a collection of related sequences (an alignment) that is treated as fixed input. This study deliberately changed which rows went into those collections and measured how the designed sequences and predicted structures changed. The authors report that alignments with certain levels of evolutionary information tended to produce more novel generated sequences and lower structural confidence, and that a moderate share of low-information positions was linked to better predictions in a subset of cases.
- **[Implementation of Machine Translation for the Uzbek Language Based on Transformer Models](https://arxiv.org/abs/2611.32359)** (Large language models): This paper is about building a computer program that translates between Uzbek, a language with relatively little digital text, and English. The authors gathered and cleaned a large collection of matching Uzbek and English sentences, roughly 3 million pairs, and used it to adapt two existing AI language models. They report that their approach beats older translation methods, measured with a standard similarity score.

## Probability

### [Sharp estimates for incremental moments of inverse subordinators and approximation errors for time-changed stochastic differential equations](https://arxiv.org/abs/2611.33075)
*Ivan Bio\v{c}i\'c, Sixian Jin, Kei Kobayashi* · `math.PR` · arXiv:2611.33075v1 · relevance 0.23

- **In one sentence**: The paper proves sharp upper and lower bounds on incremental moments of general inverse subordinators and uses them to derive an error bound, shown to be optimal in general, for numerically approximating time-changed stochastic differential equations on deterministic time grids.
- **In plain words**: The paper studies a random "clock" that runs slow and in jumps, used to model processes that move more sluggishly than ordinary random motion, such as diffusion through a sticky medium. It gives precise limits on how much this clock can change over short time spans. Those limits are then used to bound the error when a computer simulates such a process on a fixed grid of time steps, and the authors show this error bound cannot be improved in general.
- **Why it matters**: Simulating subdiffusive models is common in physics, finance and biology, so a guaranteed error rate for the numerical schemes matters for trusting those simulations. The text does not say how the results compare with prior work or which applications would benefit most, so that connection is my inference rather than something the abstract states.
- **Background needed**: - Stochastic differential equation: a equation describing a quantity evolving under random noise, like a particle jostled by molecules.
- Subordinator: a random process that only moves forward in time, in jumps; it can serve as a random clock.
- Inverse subordinator: the "inverse" of that clock, which measures how much real time has passed in terms of the clock's own count; it is the source of the slowed-down, subdiffusive behaviour.
- Time change: replacing ordinary time in an equation with a random clock.
- Incremental moments: averages of powers of how much the random clock changes over a short interval.
- Numerical approximation and order of convergence: computing an approximate solution on a grid of time steps, and how fast the error shrinks as steps get finer. · level: research-level

<details><summary>Original abstract</summary>

This paper establishes precise upper and lower bounds for the incremental moments of general inverse subordinators. Such processes are used as random time changes to model subdiffusive phenomena. The upper and lower bounds provide the foundation for a general framework for analyzing numerical approximation of time-changed stochastic differential equations on deterministic time grids. We derive an upper bound for the approximation error and further prove that the resulting order of convergence cannot be improved in general.

</details>

### [Temporal Inhomogeneous Random Graphs](https://arxiv.org/abs/2611.32717)
*Sofiya Burova, Francisco Calvillo* · `math.PR` · arXiv:2611.32717v1 · relevance 0.21

- **In one sentence**: This paper extends results on temporal stochastic block models to graphon-based random graphs with a continuous, strictly positive kernel, studying increasing-path reachability in the sparse log n/n regime with uniformly random edge timestamps.
- **In plain words**: The paper studies random networks where each connection has a timestamp and a path counts only if its timestamps keep increasing, like a message passed along links that always move forward in time. It asks how many people a starting point can reach this way, and how long the shortest and longest such paths are. The text reports first-order (leading-order) asymptotic results for these quantities, meaning the main growth rates for large networks.
- **Why it matters**: Time-respecting paths matter for modelling how things spread through populations where contacts happen at specific times, such as information or disease transmission. The abstract does not say how the results apply to any specific real-world system, so that link is a plausible motivation rather than a demonstrated one.
- **Background needed**: - Random graph: a network whose edges are placed at random according to probabilities.
- Stochastic block model: a random network with groups of vertices whose connection probabilities depend on group membership.
- Graphon: a continuous limiting description of very large random networks, given by a kernel that sets connection likelihood between positions in [0,1].
- Sparse regime (connection probability of order log n / n): each vertex has only about log n connections, so the network is just barely connected.
- Increasing path: a route through the network whose edge timestamps strictly increase along the way.
- First-order asymptotics: the leading-order behaviour of a quantity as the network grows large. · level: research-level

<details><summary>Original abstract</summary>

Motivated by the study of time-dependent propagation processes in inhomogeneous populations, we extend Burova, Lugosi and Perarnau's results on the temporal stochastic block model to graphon-based random graphs with a continuous and strictly positive kernel. We consider such a graph in the regime where connection probabilities are of the order of $\log n/n$, and equip its edges with a uniformly random ordering, interpreted as timestamps. We study the size of reachable sets via increasing paths (that is, paths whose edge timestamps are strictly increasing). We establish tight first-order asymptotics for the size of the reachable set from a fixed vertex, and also determine the first-order asymptotics of the lengths of the longest and shortest increasing paths with one or two fixed endpoints.

</details>

## Differential geometry

### [Rotationally symmetric fractional minimal surfaces](https://arxiv.org/abs/2611.32252)
*Chiara Gambicchia, Matteo Novaga, Matteo Talluri* · `math.DG` · arXiv:2611.32252v1 · relevance 0.20

- **In one sentence**: The paper constructs a nontrivial rotationally symmetric s-minimal surface by studying alternating radial sets bounded by concentric spheres, where the fractional mean curvature H_s vanishes on every free interface, and shows the limit of rescaled radial maximizers gives a properly embedded, rotationally symmetric, locally finite hypersurface with H_s = 0 on its boundary.
- **In plain words**: The paper studies a generalized version of soap-film-like surfaces, where the usual notion of curvature is replaced by a "fractional" one that depends on the whole surface rather than just its immediate neighbourhood. The authors look at shapes built from nested rings of spheres, with the outer radius fixed at 1, and show that some arrangement of these shapes has zero fractional curvature along every free boundary. They then rescale these shapes and take a limit, obtaining a rotationally symmetric surface with the same zero-curvature property.
- **Why it matters**: Minimal surfaces are a central object in geometry, and the fractional version is an active area; a concrete nontrivial rotationally symmetric example is useful as a test case for general theory. The text does not indicate applications beyond this, so its wider significance is uncertain from the abstract alone.
- **Background needed**: - Minimal surface: a surface whose mean curvature is zero, like a soap film spanning a wire frame.
- Mean curvature: a local measure of how a surface bends on average at a point.
- Fractional (s-) mean curvature: a nonlocal generalization in which the value at a point depends on the surface globally, with a parameter s controlling the range of this influence.
- Rotational symmetry: the shape looks the same when rotated about an axis; here built from concentric spheres (nested shells of different radii).
- Locally finite hypersurface: a surface that may be unbounded but has only finitely many pieces within any bounded region.
- Limit and rescaling: shrinking or enlarging a shape by a factor and taking a limiting shape as the factor changes. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we provide a non-trivial example of an $s$-minimal surface that is invariant under rotations. More precisely, we study alternating radial sets whose boundaries are finite or locally finite unions of concentric spheres and prove that, fixing the outer radius to $r=1$, there exists a radial configuration for which the fractional mean curvature $H_s$ vanishes at every free interface. We then show that rescaling radial maximizers by their innermost radius and passing to the limit yields a properly embedded, rotationally symmetric, locally finite hypersurface satisfying $H_s=0$ at every point of the boundary.

</details>

### [An intrinsic criterion for Pansu differentials to be homomorphisms of nilpotent Lie groups](https://arxiv.org/abs/2611.32893)
*Cristian Sopio, Francesca Tripaldi* · `math.DG` · arXiv:2611.32893v1 · relevance 0.19

- **In one sentence**: The paper gives an intrinsic criterion, for a suitable grading, for when the Pansu differential of a Lipschitz map from a nilpotent Lie group with a bracket-generating distribution is a group homomorphism, and shows the criterion holds automatically when the target's step is small and that the threshold is sharp.
- **In plain words**: The paper studies smooth-like "derivatives" of distance-preserving-type maps (Lipschitz maps) between curved spaces with a built-in sideways-moving structure, known as nilpotent Lie groups. Such a map has a local best-approximating version, the Pansu differential, which is a homomorphism (a structure-preserving map) of a simpler model group rather than of the original group. The authors find a checkable condition that tells when this approximation is also structure-preserving on the original group, and they show a concrete example where the condition's threshold cannot be pushed further.
- **Why it matters**: Pansu's theorem is a standard tool for understanding maps between sub-Riemannian and metric spaces, so a precise test for when its derivative respects the group structure of the original space clarifies where that tool applies cleanly. The text does not say what further applications this may have, so the wider significance is unclear from the abstract alone.
- **Background needed**: - Lipschitz map: a map that stretches distances by at most a fixed factor.
- Lie group: a continuous group of transformations that is also a smooth manifold; nilpotent means its commutator brackets eventually vanish.
- Distribution (sideways directions): a choice of allowed directions at each point; bracket-generating means repeated commutators of these directions span all directions.
- Carnot group: a nilpotent group with a graded structure, the simplest model of such spaces.
- Pansu differential: the limiting "derivative" of a Lipschitz map at a point, which is a homomorphism between Carnot groups.
- Grading: a splitting of the Lie algebra into layers; the osculating Carnot group depends on this choice.
- Homomorphism: a map that preserves the group operation; ideal: a normal subgroup-like substructure used to form quotients.
- Step: how many layers of nested brackets are needed before the structure stops growing. · level: research-level

<details><summary>Original abstract</summary>

By Pansu's theorem, Lipschitz maps between Carnot groups are differentiable almost everywhere, and their differentials are group homomorphisms. When the domain is instead a nilpotent Lie group with a bracket-generating left-invariant distribution, the Pansu differential is a homomorphism of an osculating Carnot group, which depends on an auxiliary choice of grading, and it need not be a homomorphism of the original group. We give an intrinsic criterion for when it is one, for a suitable choice of grading: the differential must vanish on an ideal that depends only on the group and its distribution, and comes from a universal quotient onto a Carnot group. The criterion holds automatically when the step of the target is small enough, and an explicit example shows that this threshold is sharp. Along the way, we determine exactly how the obstruction depends on the choice of grading.

</details>

## Partial differential equations

### [Weighted pointwise estimates for the damped wave equation and global solutions to Nakao's problem in three dimensions](https://arxiv.org/abs/2611.31881)
*Vladimir Georgiev, Kosuke Kita* · `math.AP` · arXiv:2611.31881v1 · relevance 0.22

- **In one sentence**: The paper derives weighted pointwise estimates for the Duhamel term of the three-dimensional damped wave equation, combining a parabolic weight with a wave-cone weight, and applies them to prove small-data global existence and uniqueness for Nakao's coupled damped-wave/wave system in weighted L^infinity spaces.
- **In plain words**: The paper studies a pair of coupled equations that describe how waves and damped (energy-losing) waves spread through space over time, in three dimensions. The authors prove sharper size bounds on one piece of the solution, the part driven by a source, and use them to show that, when the starting disturbance is small and the nonlinear terms meet stated conditions, solutions exist for all time and are unique. The result covers both fast and slower decay rates for each component.
- **Why it matters**: Global existence results for coupled nonlinear wave systems show when small disturbances stay bounded forever rather than blowing up, which is a basic question in the theory of such equations. The text does not indicate applications beyond this mathematical setting, so its wider significance is unclear from the abstract alone.
- **Background needed**: - A wave equation describes vibrations or signals travelling through a medium at finite speed.
- A damped wave equation adds friction, so the energy fades and the solution spreads out and decays over time, somewhat like heat diffusion.
- Nakao's problem is a named open-style question about a specific pair of such equations coupled together.
- Duhamel term: the part of a solution produced by a forcing or source term acting over time.
- Pointwise estimate: a bound on the size of the solution at each individual point, rather than on average.
- Weighted L^infinity space: a function space that bounds the solution's maximum size while weighting it by a factor that controls decay in space and time.
- Small-data global existence: if the starting data are small enough, the solution is guaranteed to exist for all times.
- Contraction argument: a standard method that builds the solution as a fixed point of a map that shrinks distances. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we establish weighted pointwise estimates for the Duhamel term of the three-dimensional damped wave equation. The estimates combine the parabolic weight $\langle t+|x|^2\rangle$ with the wave-cone weight $\langle t-|x|\rangle$, and thereby account for both the diffusive part of the damped wave flow and source terms with wave-like decay. As an application, we study Nakao's problem, a weakly coupled system consisting of one semilinear damped wave equation and one semilinear wave equation. Under explicit conditions on the exponents of nonlinear terms, we prove small-data global existence and uniqueness of mild solutions in weighted $L^\infty$ spaces. The result covers both the full parabolic decay and slower pointwise decay for the damped-wave component, and allows either the standard wave decay or slower pointwise decay for the wave component. The proof combines the new Duhamel estimate with weighted estimates for the free wave equation and a contraction argument.

</details>

### [Large-time existence for the gravity water waves equations](https://arxiv.org/abs/2611.32994)
*Th\'eo Fradin, Benjamin Melinand* · `math.AP` · arXiv:2611.32994v1 · relevance 0.13

- **In one sentence**: The paper proves local-in-time, long-timescale (lifespan growing like the inverse of the nonlinearity parameter) existence of solutions to the gravity water-waves equations without surface tension, uniformly in the shallow-water parameter and allowing a large but not emerging bathymetry.
- **In plain words**: The paper studies how waves move on the surface of water over an uneven floor, using the standard mathematical model of an incompressible, irrotational fluid with a free surface and gravity acting, but no surface tension. It shows that, for sufficiently smooth starting conditions, a solution exists for a long stretch of time, and that this stretch gets longer as the waves get smaller. The result holds even when the seabed varies by a sizable amount, though not so much that the bottom breaks through the surface.
- **Why it matters**: Knowing how long a model of water waves stays well-behaved is a basic question for both theory and for the approximate models used in coastal and ocean studies. The text does not claim wider applications, so its reach beyond this mathematical setting is uncertain.
- **Background needed**: - Water-waves equations: the standard model of a free water surface under gravity, with the water assumed incompressible (constant density) and irrotational (no swirling).
- Well-posedness: the question of whether a solution exists, is unique, and depends continuously on the starting data.
- Sobolev regularity: a measure of how smooth the initial data must be; "high but finite" means the data must be quite smooth but not infinitely so.
- Nonlinearity parameter: a small number measuring wave amplitude relative to depth; the result's time span scales with its inverse.
- Shallow-water parameter: a measure of depth relative to wavelength; the result holds uniformly across it.
- Bathymetry: the shape of the seabed; "large but not emerging" means the bottom varies substantially but stays below the surface.
- Lifespan: how long the solution is guaranteed to exist. · level: research-level

<details><summary>Original abstract</summary>

We provide a new well-posedness result on the gravity water-waves equations, i.e. the free-surface, incompressible and irrotational Euler equations, in the absence of surface tension. Our main contribution is to provide the existence of solutions, in high enough but finite Sobolev regularity, on a timescale that grows like the inverse of the non-linearity parameter. Our result is also uniform in the shallow-water parameter. The main difficulty is that we allow for the presence of a large (though not emerging) bathymetry.

</details>

## Harmonic analysis

### [Normal and Unitary Operators on Smooth Banach Spaces via the Duality Mapping](https://arxiv.org/abs/2611.31874)
*Mohammed Shameem, Deepesh K. P* · `math.FA` · arXiv:2611.31874v1 · relevance 0.21

- **In one sentence**: The paper generalises normal and unitary operators, and the self-adjoint subclass, from Hilbert spaces to smooth Banach spaces by using the duality mapping, and studies their characterisations and spectral properties.
- **In plain words**: Mathematicians have a well-understood family of "nice" transformations on spaces where lengths and angles behave like ordinary geometry (Hilbert spaces). This paper asks how far those ideas stretch to a wider class of spaces, called smooth Banach spaces, where angles are not available but a substitute tool, the duality mapping, is. The authors define normal and unitary operators in this setting, show that self-adjoint operators fit inside the new normal class, and report several equivalent descriptions and spectral properties.
- **Why it matters**: It tests which familiar results from quantum-style linear algebra survive when the inner product is removed, so it matters mainly to specialists in functional analysis. The text does not indicate applications beyond this theoretical extension, so its wider significance is uncertain.
- **Background needed**: - Banach space: a complete space with a notion of length (norm) but no required angles.
- Hilbert space: a Banach space with an inner product, giving angles; the classical setting for normal and unitary operators.
- Operator: a linear map from a space to itself.
- Self-adjoint / normal / unitary: classes of operators with special symmetry; normal means commuting with its adjoint, unitary means preserving length and inner products.
- Duality mapping: a substitute for the inner product that sends each vector to a set of "dual" functionals of matching size; it is set-valued in general.
- Smoothness: a geometric condition ensuring the duality mapping is single-valued.
- Spectrum: the set of scalars where an operator fails to be invertible; spectral properties concern its shape and structure. · level: research-level

<details><summary>Original abstract</summary>

This article extends the classical notions of normal and unitary operators from Hilbert spaces to smooth Banach spaces through the duality mapping. The class of normal operators introduced in this setting contains, as a special case, the self-adjoint operators on smooth Banach spaces defined via the duality mapping. We establish several characterisations of these operators and investigate their fundamental properties. In particular, we examine various spectral properties of normal operators on smooth Banach spaces. These results demonstrate that many fundamental aspects of the classical theory of normal and unitary operators on Hilbert spaces persist in the smooth Banach space setting.

</details>

### [Kernel Estimates and Calder\'{o}n-Zygmund Theory in the $(k,a)$-generalized Laguerre setting](https://arxiv.org/abs/2611.31933)
*Mingwei Shi, Yongsheng Han, Yu Liu* · `math.FA` · arXiv:2611.31933v1 · relevance 0.13

- **In one sentence**: The paper proves heat and Poisson kernel estimates for the operator ||x||^{2-a}Δ_k in the (k,a)-generalized Laguerre setting (Dunkl Laplacian from a finite reflection group), then develops a (k,a)-Calderón-Zygmund theory with L^p boundedness, weak type (1,1), BMO endpoint estimates, and a T1 characterization of L^2 boundedness.
- **In plain words**: The paper studies a family of mathematical operators that describe how heat or influence spreads over a space with built-in symmetries. The authors first pin down the detailed size and decay behaviour of the associated heat and Poisson kernels, which are the basic 'spreading patterns' of those operators. Using these estimates, they show that a certain class of singular integral operators that are bounded in one basic sense (L^2) are automatically bounded in a whole range of other standard measures of size.
- **Why it matters**: Calderón-Zygmund theory is a central toolkit in harmonic analysis, and extending it to this symmetric, generalized setting broadens where its results apply. The T1 criterion gives a practical test for boundedness; the text does not say what applications beyond this setting it may have.
- **Background needed**: - Heat kernel: a function describing how heat (or a quantity diffusing over time) spreads from a point; it is the fundamental solution of the heat equation.
- Poisson kernel: a related spreading function, obtained here by "subordination" (a time-change trick that links it to the heat kernel).
- Laplacian: the operator summing second derivatives; it measures how a function differs from its local average.
- Dunkl operators: generalized derivatives that respect the symmetries (reflections) of a finite group, used to extend classical analysis to symmetric settings.
- Singular integral operator: an averaging operator with a kernel that is not integrable near the diagonal; a standard object in harmonic analysis.
- L^p spaces and weak type (1,1): ways of measuring functions by p-th power integrability; weak type (1,1) is a borderline size bound.
- BMO (bounded mean oscillation): a space of functions with controlled average fluctuation, the usual endpoint replacement for L^infinity in this theory.
- T1 theorem: a criterion saying an operator is L^2-bounded if its action on the constant function 1 (and its adjoint's action) is BMO and a weak boundedness condition holds. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we establish heat and Poisson kernel estimates for $\mathfrak L=\|x\|^{2-a}\Delta_k$ in the $(k,a)$-generalized Laguerre setting, where $\Delta_k$ is the Dunkl Laplacian associated with a finite reflection group. The heat kernel is nonnegative, symmetric, and conservative, and satisfies a Gaussian bound in the orbit distance together with polynomial decay in the distance between the transformed coordinates. The Poisson kernel, obtained by subordination, satisfies corresponding size and time-derivative estimates, while $-t\partial_t p_t$ has integral zero in each variable. Motivated by these estimates, we introduce a class of $(k,a)$-Calder\'{o}n-Zygmund singular integral operators and show that $L^2_{k,a}$-boundedness implies $L^p_{k,a}$-boundedness for $1<p<\infty$, together with weak type $(1,1)$ and $L^\infty$-to-$\BMO$ estimates. Finally, we establish a $T1$ theorem characterizing the $L^2$-boundedness of such operators by the conditions $T1\in BMO$, $T^*1\in BMO$, and the weak boundedness property.

</details>

## Complex analysis

### [H\"older continuity of Green functions for Markov sets](https://arxiv.org/abs/2611.33131)
*Leokadia Bialas-Ciez, Rafa{\l} Pierzcha{\l}a* · `math.CV` · arXiv:2611.33131v1 · relevance 0.13

- **In one sentence**: For a compact set K in C^N, the paper shows the Green function (and the Siciak extremal function) is Hölder continuous exactly when polynomial first derivatives obey Markov's inequality on K, settling the Markov-to-Hölder direction and giving the sharp exponent 1/m in one variable.
- **In plain words**: The paper studies a measure of how "spread out" a region in the complex plane (or complex space) is, built from polynomials that stay small on that region. It shows that a certain smoothness property of this measure holds exactly when a standard polynomial bound, Markov's inequality, holds for the derivatives of polynomials on the region. The proof compares the measure on the region with its measure on a slightly larger neighborhood.
- **Why it matters**: The text describes the Markov-to-Hölder implication as settling a longstanding open problem between approximation theory and pluripotential theory, so it is of interest to specialists in those areas. The text does not say what further applications it may have, so beyond that connection I cannot say more.
- **Background needed**: - Compact set: a closed, bounded region, such as a disk or a segment in the complex plane.
- Polynomial inequality (Markov's inequality): a bound on how fast a polynomial of degree n can grow on the set; here the bound is of the form A n^m.
- Green function / Siciak extremal function: a way of measuring how far a point is from the set, using polynomials that stay bounded on it.
- Hölder continuity: a quantitative smoothness condition; a function is Hölder with exponent α if its change over a small distance d is at most a constant times d^α.
- Maximum principle and Hörmander's extension theorem: standard tools from complex analysis used in the proof.
- Several complex variables: the case N>1, where the set lives in C^N. · level: research-level

<details><summary>Original abstract</summary>

Let $K$ be a nonempty compact subset of $\mathbb C^N$. We prove that its Green function (and consequently, the Siciak extremal function) is H\"older continuous if and only if the first derivatives of polynomials satisfy Markov's inequality on $K$. The implication from Markov's inequality to H\"older continuity of the associated Green function settles a longstanding open problem at the intersection of approximation theory and pluripotential theory. A Markov bound $An^m$ in degree $n$ gives every H\"older exponent below $1/m$. In one complex variable it gives the exponent $1/m$ itself. The proof compares the extremal functions of two neighborhoods of $K$. For $N>1$ we use H\"ormander's theorem on holomorphic extension from a point. For $N=1$ the comparison follows from the maximum principle.

</details>

### [Smale's Mean Values And Geometric Mean Values](https://arxiv.org/abs/2611.31546)
*Yunping Jiang, Zhe Wang* · `math.NT` · arXiv:2611.31546v1 · relevance 0.13

- **In one sentence**: The paper studies Smale's mean values of complex polynomials, showing the geometric mean value alone cannot give the sharpest bound on the minimum of Smale's mean values, verifying Smale's mean value conjecture for some subclasses, and linking the problem to Fekete points.
- **In plain words**: This paper is about a question concerning polynomials with complex coefficients: how large must a "typical" point's local behavior be in terms of the polynomial's roots and derivative values. The authors show that for every degree above 2 and every positive number L, some polynomial of that degree has a geometric mean value larger than L. They also prove upper bounds for special families of polynomials, which supports Smale's conjecture in those cases.
- **Why it matters**: The text shows that one natural quantity (the geometric mean value) is not enough by itself to pin down the sharpest bound for Smale's mean values, which narrows how the conjecture can be attacked. The authors also tie the problem to Fekete points, a classical object from potential theory, and propose a new problem about Fekete points; the broader significance of these links is not spelled out in the text.
- **Background needed**: - A complex polynomial is a sum of powers of a complex variable with complex coefficients; its roots are the points where it equals zero.
- Smale's mean value conjecture concerns how the values of a polynomial's derivative at its roots relate to the rest of the polynomial, measured by averaged quantities called Smale's mean values.
- The geometric mean value is one such average, taken as a product rather than a sum, so it is sensitive to very small or very large terms.
- A "bound" here is a guaranteed upper limit; showing a quantity can exceed every L means no finite bound of that kind holds for it alone.
- Fekete points are special sets of points, chosen to be maximally spread out, from potential theory and approximation theory.
- Degree d means the highest power of the variable in the polynomial. · level: research-level

<details><summary>Original abstract</summary>

We prove that, for every integer $d>2$ and every $L>0$, there exists a polynomial of degree $d$ whose geometric mean value exceeds $L$. This result demonstrates that the geometric mean value alone is insufficient to establish the smallest upper bound for the minimum of Smale's mean values. Under certain additional assumptions, we derive upper bounds for the geometric mean value, thereby verifying Smale's mean value conjecture for several subclasses of polynomials. Furthermore, we connect Smale's mean values to Fekete points. Motivated by this connection, we formulate a new problem concerning Fekete points in the spirit of Smale's mean values.

</details>

## Operator algebras and spectral theory

### [The Universal Frame Characterization of C*-algebras](https://arxiv.org/abs/2611.32953)
*Mohammad B. Asadi, Zahra Hassanpour-Yakhdani* · `math.OA` · arXiv:2611.32953v1 · relevance 0.18

- **In one sentence**: The paper proves that a C*-algebra is exactly one of compact operators if and only if every Hilbert A-module admits a frame, settling a question of Amini, Asadi, Elliott and Khosravi (2017).
- **In plain words**: This paper is about a precise yes-or-no question in the abstract mathematics of operators, which are rules that act on spaces of functions or vectors. The author shows that a certain class of algebras, the C*-algebras of compact operators, is characterized by a property: every "Hilbert module" over the algebra has a frame, a kind of spanning family of vectors. The result answers a question that earlier researchers had raised.
- **Why it matters**: It gives a clean converse: a structural property of the algebra is equivalent to a frame-existence property for all its modules, which resolves an open question from the literature. The text does not say what wider applications it may have, so the broader significance is unclear from this text alone.
- **Background needed**: - C*-algebra: a collection of bounded operators closed under addition, multiplication, scaling and taking adjoints (a kind of conjugate transpose), with a norm compatibility condition.
- Compact operators: operators that behave like limits of finite-rank matrices; they are the "smallest" nontrivial operator algebras of this type.
- Hilbert module: a generalization of a Hilbert space in which inner products take values in an algebra rather than in complex numbers.
- Frame: a family of vectors that spans a space in a stable, possibly redundant way, so every element can be reconstructed from its inner products with the family.
- Background result: Frank and Larson (2002) raised the underlying problem about frames in Hilbert modules; Amini, Asadi, Elliott and Khosravi (2017) posed the specific question answered here. · level: research-level

<details><summary>Original abstract</summary>

We prove that a C*-algebra A is a C*-algebra of compact operators if and only if every Hilbert A-module admits a frame. This answers affirmatively the question of Amini, Asadi, Elliott and Khosravi (2017), arising from the problem of Frank and Larson (2002)

</details>

### [Algebraic derivations and the first \(L^2\)-cohomology of free group factors](https://arxiv.org/abs/2611.32121)
*J. Huang, K. Kudaybergenov, F. Sukochev et al.* · `math.OA` · arXiv:2611.32121v1 · relevance 0.16

- **In one sentence**: The paper proves that the first L^2-Betti number of the free group factor of a finite-rank free group is infinite, using algebraic derivations into affiliated operators of the tensor square and a rank identity for Jacobians of polynomial relations.
- **In plain words**: The paper studies a measure of "how many independent ways a structure can be stretched" for a certain infinite-dimensional algebra built from a free group. The authors show this measure is infinite for the free group algebra, which is a result about the size of a certain cohomology space. They do this by extending values assigned to basic generators to full derivations, using a counting identity for polynomial relations.
- **Why it matters**: Whether the first L^2-Betti number of free group factors is finite was a known open question in this area, so settling it in the infinite direction matters for the structure theory of these algebras. The text does not show connections to other fields beyond this area, so broader significance is unclear from the summary alone.
- **Background needed**: - Free group: a group whose elements are words built from generators with no relations other than trivial cancellation.
- von Neumann algebra / II_1 factor: an infinite-dimensional algebra of bounded operators on Hilbert space, the analogue of a ring of functions for quantum or noncommutative settings.
- L^2-Betti number: a dimension-like invariant from L^2-cohomology, measuring the size of a space of derivations modulo inner ones.
- Derivation: a map that obeys the product rule, like differentiation.
- Semicircular elements: the noncommutative analogue of a Gaussian random variable, used as generators here.
- Jacobian rank identity: a linear-algebra count of how many independent constraints a system of polynomial equations imposes. · level: research-level

<details><summary>Original abstract</summary>

Let \(M\) be the von Neumann algebra of a nonabelian free group of finite rank. We prove that its first \(L^2\)-Betti number in the sense of Connes and Shlyakhtenko is infinite. We show that every assignment of values in \(\Aff(M\bar\otimes M^{\op})\) to the standard semicircular generators extends to an algebraic derivation on all of \(M\). The extension follows from a rank identity for the Jacobians of finite systems of polynomial relations. We also prove that, for any \(\mathrm{II}_1\) factor with separable predual, the existence of an outer derivation with these coefficients forces the first \(L^2\)-Betti number to be infinite.

</details>

## Algebra

### [Gorenstein symmetry can fail for noetherian rings](https://arxiv.org/abs/2611.32871)
*Liran Shaul* · `math.RA` · arXiv:2611.32871v1 · relevance 0.15

- **In one sentence**: The paper constructs a two-sided noetherian ring whose injective dimension is 1 on the left but infinite on the right, showing Gorenstein symmetry can fail for such rings, and examines related properties (dualizing complex, injective generation) over fields of characteristic not 2.
- **In plain words**: This is a question about algebraic structures called rings, which mathematicians use to describe collections of numbers and transformations. A common expectation is that a ring looks the same whether you view it from the left or the right in terms of a certain "size" measure called injective dimension. The paper builds a counterexample where the two sides differ sharply: finite from the left, infinite from the right.
- **Why it matters**: It settles a question of whether a symmetry expected for a broad class of rings (Gorenstein symmetry) actually holds, answering it negatively. The text does not say how it bears on wider applications, so its reach beyond this area of algebra is unclear.
- **Background needed**: - Ring: a set with addition and multiplication, where multiplication need not commute.
- Left and right modules: ways a ring acts on other algebraic objects from the left or the right.
- Noetherian ring: one where every chain of ideals eventually stops growing; a finiteness condition.
- Injective dimension: a measure of how far a module is from being "injective" (roughly, how well it can be extended); finite means it stops after finitely many steps.
- Gorenstein symmetry: the expectation that left and right injective dimensions agree for noetherian rings.
- Dualizing complex and Rickard-Keller injective generation: technical structures from homological algebra that relate duality properties of the derived category of modules. · level: research-level

<details><summary>Original abstract</summary>

We construct a two-sided noetherian ring $A$ which has injective dimension $1$ as a left module over itself and infinite injective dimension as a right module over itself. This shows that Gorenstein symmetry can fail for two-sided noetherian rings. It is further shown that there is such an example over any field of characteristic different than $2$, that it has a dualizing complex, and that its derived category of right modules does not satisfy injective-generation in the sense of Rickard-Keller.

</details>

### [The optimal exponent in the Babai-Goodman-Pyber theorem](https://arxiv.org/abs/2611.32149)
*Shaowu Zheng* · `math.GR` · arXiv:2611.32149v1 · relevance 0.14

- **In one sentence**: The paper determines the optimal exponent c = b_0 = 1 + log_9(168·24^{1/3}) ≈ 3.8141 in the Babai–Goodman–Pyber bound relating the index of the soluble radical of a finite group to the index of any soluble subgroup, with a sharper coefficient 24^{-1/3} for nonsoluble groups and sharpness examples from PSL_2(8).
- **In plain words**: This is about finite groups, which are collections of symmetries that can be combined, and how "large" a group is compared with its simpler pieces. A known result says the part of a group left after removing its largest simple-to-handle (soluble) normal piece cannot be much bigger than any simple-to-handle subgroup raised to some fixed power. The paper finds the smallest possible value of that power, about 3.81, and shows it cannot be lowered, using an example built from the group PSL_2(8).
- **Why it matters**: It settles the exact best constant in a known bound, so the question of how sharp the original theorem is now has a precise answer. The text does not say what wider applications it has, and I am not sure of any beyond the specialist area of finite group theory.
- **Background needed**: - Finite group: a group with finitely many elements, such as the symmetries of a finite object.
- Subgroup and index: a subgroup is a smaller group inside a larger one; the index is roughly how many copies of the subgroup fit into the whole group.
- Soluble group: a group that can be built step by step from abelian (commutative) pieces; informally, "simple to handle".
- Normal subgroup: a subgroup that is preserved under conjugation (a change of viewpoint), so the quotient makes sense.
- Radical Rad(X): the largest soluble normal subgroup of X.
- Simple group and automorphism group: simple groups are the indivisible building blocks of finite groups; automorphism groups are the symmetries of a group itself.
- Exponent and constant: the bound says the index of the radical is at most a power of the index of H; the question is the smallest allowed power. · level: research-level

<details><summary>Original abstract</summary>

Babai, Goodman and Pyber proved that there exists an absolute constant $c$ such that $[X:\operatorname{Rad}(X)]\le [X:H]^c$ for every finite group $X$ and every soluble subgroup $H\le X$, where $\operatorname{Rad}(X)$ denotes the largest soluble normal subgroup of $X$. We prove that the least possible value of $c$ is $b_0=1+\log_9(168\cdot 24^{1/3})\approx3.8141$. For nonsoluble $X$, we obtain the stronger inequality $[X:\operatorname{Rad}(X)]\le 24^{-1/3}[X:H]^{b_0}$, and the coefficient $24^{-1/3}$ is optimal for this exponent. We reduce the problem to bounds on soluble subgroups of automorphism groups of finite simple groups. Examples based on $\operatorname{PSL}_2(8)$ establish sharpness.

</details>

## Representation theory

### [Abelian envelopes and quantum groups in Knop's interpolation categories](https://arxiv.org/abs/2611.33152)
*Johannes Flake, Peter Mader* · `math.CT` · arXiv:2611.33152v1 · relevance 0.25

- **In one sentence**: The paper shows that large classes of subcategories of Knop's tensor envelopes admit abelian envelopes, which correspond to quantum groups (Hopf algebras) inside Deligne-type interpolation categories, including those of group-theoretical easy quantum groups.
- **In plain words**: This paper is about a way of taking a family of symmetry structures, described by counting diagrams, and turning it into a more familiar setting where it behaves like a collection of symmetries acting on spaces. The authors prove that for many such families an "abelian envelope" exists, meaning a well-behaved completion in which the structure can be read as a quantum group. They also apply the method to several concrete families, such as wreath products and finite general linear and affine groups.
- **Why it matters**: It connects two research programs: the interpolation categories that let symmetric groups be treated as if their size were a continuous parameter, and the theory of quantum groups. Its specific scope is the existence result and the correspondence with quantum groups; the text does not say how far beyond these cases the results extend.
- **Background needed**: - Representation theory: studying groups through the linear actions they have on vector spaces.
- Tensor category: a collection of objects (such as representations) that can be combined by a tensor product, with morphisms between them.
- Interpolation category: a category built so that a parameter (such as the size n of a symmetric group) can take arbitrary values, via counting diagrams.
- Abelian envelope: an enlargement of a category into an abelian one (one where kernels and cokernels behave as in linear algebra), which lets it be studied with standard tools.
- Hopf algebra / quantum group: a generalization of a group of symmetries, with an algebraic structure that allows multiplication and comultiplication; quantum groups are its noncommutative, deformed versions.
- Easy quantum group: a quantum symmetry group defined through a category of diagrams (partitions) of a specific kind. · level: research-level

<details><summary>Original abstract</summary>

We show the existence of abelian envelopes for large classes of subcategories of Knop's tensor envelopes. It follows that these abelian envelopes correspond to groups or more generally Hopf algebras (``quantum groups'') in their parent interpolation categories. As a special case, we obtain that the interpolation categories in the sense of Flake--Maassen (2022) of all so-called group-theoretical easy quantum groups have abelian envelopes given by quantum groups in Deligne's interpolation category of the symmetric groups. Similarly, we apply our theory to interpolation categories of wreath products, finite general linear groups, and finite affine groups. Our main technique is an explicit construction of objects corresponding to coordinate algebras using the calculus of relations that Knop's categories are based on.

</details>

### [Non-formality of prefactorization algebras](https://arxiv.org/abs/2611.33125)
*Coline Emprin, Alex Takeda* · `math.AT` · arXiv:2611.33125v1 · relevance 0.14

- **In one sentence**: The paper builds a Poisson bracket on the cohomology of locally constant prefactorization algebras on R^m (for m ≥ 2) that obstructs formality, generalizing the two-dimensional bracket of Bruinsma, Schenkel and Vicedo and extending their non-formality theorem for Lie algebra factorization envelopes to all dimensions.
- **In plain words**: The paper studies a mathematical structure that assigns algebraic data to regions of space, and asks whether that data can be simplified to a standard form without losing information. The authors build an invariant, a kind of bracket operation on the simplified data, whose non-zero value shows that such simplification is impossible in every dimension two or higher. They use this to show that several families of algebraic objects, including factorization envelopes of Lie algebras and certain physics-inspired field theories, are not formal.
- **Why it matters**: A non-zero bracket gives a checkable test that a structure cannot be reduced to its simplest form, which matters for classifying these objects. The link to field theories such as Chern-Simons and BF theories suggests relevance to mathematical physics, but the text does not say more about those applications.
- **Background needed**: - Prefactorization algebra: an assignment of algebraic data to open regions of a space, compatible with placing regions side by side (a local-to-global structure from factorization homology).
- Locally constant: the data depends only on topology, not on fine geometry, so it behaves like a topological invariant.
- Cohomology: an algebraic invariant that counts independent 'holes' or obstructions in a structure; here it is the object that carries the bracket.
- Poisson bracket: an antisymmetric product on functions or classes that satisfies a Leibniz-type rule; it is the 'signal' used to detect non-formality.
- Formality: the property that a structure is equivalent to its cohomology with trivial higher operations; non-formality means this simplification fails.
- L-infinity algebra: a generalization of a Lie algebra with a family of higher operations.
- Lie algebra, BF theory and Chern-Simons theory: standard algebraic and physical structures; only needed at a high level. · level: research-level

<details><summary>Original abstract</summary>

We construct a Poisson bracket on the cohomology of locally constant prefactorization algebras on $\mathbb{R}^m$ that provides an obstruction to formality in every dimension $m\geqslant 2$. Our construction combines colored obstruction sequences to formality with linking spheres and generalizes the two-dimensional bracket of Bruinsma, Schenkel, and Vicedo. We use it to extend their non-formality theorem for Lie algebra factorization envelopes to all higher dimensions. We also establish new non-formality results for factorization envelopes of Lie algebras, their compactifications and generalizations to $L_\infty$-algebras, free BF-type theories, higher abelian Chern-Simons theories and their compactifications.

</details>

## Number theory

### [An elliptic Lehmer bound of exponent one at a supersingular prime](https://arxiv.org/abs/2611.32749)
*Jorge Mello* · `math.NT` · arXiv:2611.32749v1 · relevance 0.27

- **In one sentence**: Proves a lower bound on Néron–Tate heights of non-torsion points on elliptic curves with good supersingular reduction at a prime, with exponent one in the degree, which by Elkies' result covers all elliptic curves over Q.
- **In plain words**: The paper is about how "small" a nonzero point on an elliptic curve (a special kind of curve defined by a cubic equation) can be, measured by a height function that grows with how complicated the point's coordinates are. It shows that such a point cannot have height smaller than a quantity that shrinks only slightly faster than the reciprocal of its degree, which is the number of ways its coordinates are tied to the base number field. The bound is stated for curves with a particular behaviour modulo a prime, and the text says this covers every elliptic curve over the rational numbers.
- **Why it matters**: This is a sharpened version of a Lehmer-type lower bound, a family of questions asking how small a height can get before it is forced to be zero. The text reports that the exponent improves on earlier results by Masser and by Hindry and Silverman, but the text does not say how much these bounds matter for other problems.
- **Background needed**: - Elliptic curve: the set of solutions of a cubic equation in two variables, with a natural group structure on its points.
- Number field: a finite extension of the rational numbers, such as the field generated by a square root.
- Néron–Tate height: a measure of the arithmetic complexity of a point on an elliptic curve; it is zero exactly for torsion points (points of finite order).
- Lehmer-type bound: a lower bound saying that nonzero heights cannot be arbitrarily close to zero, given the degree of the field involved.
- Good supersingular reduction: a condition on how the curve behaves when reduced modulo a prime; supersingular is a special, rare case of this.
- Degree D: the size of the field generated by the x-coordinate of the point over the base field.
- Notation o(1): a quantity that tends to zero as D grows. · level: research-level

<details><summary>Original abstract</summary>

Let $E$ be an elliptic curve over a number field $K$ with good supersingular reduction at a prime $\p$. We prove that the N\'eron--Tate height of every non-torsion $P\in E(\Kbar)$ satisfies $\hh_E(P)\ge c\,D^{-1}(\log3D)^{-1}\exp(-c'\sqrt{\log3D})$, where $D=[K(x(P)):K]$ and $c,c'>0$ depend only on $E$, $K$ and $\p$; so $\hh_E(P)\ge D^{-1-o(1)}$. By a result of Elkies this applies to every elliptic curve over $\QQ$, and it improves the exponents of Masser and of Hindry and Silverman.

</details>

### [Counting elliptic curves by discriminant](https://arxiv.org/abs/2611.31390)
*Stephanie Chan, Peter Koymans* · `math.NT` · arXiv:2611.31390v1 · relevance 0.27

- **In one sentence**: The paper proves an asymptotic count with a power saving for rational elliptic curves ordered by minimal discriminant, conditionally on the abc conjecture, and unconditionally for curves with a restricted c4 size, via new bounds on integral points (c4, c6) near the cusp c4^3 = c6^2.
- **In plain words**: The paper studies how many elliptic curves (a standard family of smooth curves defined by cubic equations, used heavily in number theory) have a given size of "discriminant," a number that measures how degenerate the curve is. The authors give a precise formula for how this count grows as the size bound increases. Part of the result assumes the abc conjecture, an unproven statement about how addition and multiplication of whole numbers interact, and part is proved without it under an extra restriction.
- **Why it matters**: Counting elliptic curves is a central question in arithmetic geometry, and a formula with a power saving (an error term that shrinks polynomially) is a sharper result than an asymptotic alone. The text does not say how it compares with earlier counts, so its wider significance is unclear from the abstract alone.
- **Background needed**: - Elliptic curve: a smooth cubic curve over the rational numbers, with its rational points forming a group.
- Q-isomorphism class: curves counted up to a change of coordinates over the rationals, so equivalent curves are counted once.
- Minimal discriminant: a whole number built from the curve's coefficients that measures degeneracy; smaller means the curve is "nicer."
- Asymptotic formula: a formula saying how a count grows as the bound X goes to infinity.
- Power saving: the error in the formula shrinks like a power of X.
- c4, c6: standard integer invariants of a curve; the cusp c4^3 = c6^2 is where the curve becomes singular.
- abc conjecture: an unproven conjecture on the sizes of prime factors of integers a+b=c; it is used here as a hypothesis. · level: research-level

<details><summary>Original abstract</summary>

We prove an asymptotic formula with a power saving for the number of $\mathbb{Q}$-isomorphism classes of elliptic curves $E/\mathbb{Q}$ ordered by minimal discriminant, assuming the $abc$ conjecture. Unconditionally, we obtain the same asymptotic for the curves with $|\Delta_{\min}(E)| \le X$ and $c_4(E) \le X^{8/3 - \delta}$ for any fixed $\delta > 0$, by obtaining new bounds for the number of integral points $(c_4, c_6)$ near the cusp $c_4^3 = c_6^2$.

</details>

## Algebraic geometry

### [Flexible algebraic curves and fake vanishing cycles](https://arxiv.org/abs/2611.31551)
*Joshua Lehman, Tudur Lewis* · `math.GT` · arXiv:2611.31551v1 · relevance 0.15

- **In one sentence**: The paper proves that complex curves in sufficiently ample linear systems on simply connected projective surfaces (including smooth plane curves) are topologically (spin) flexible, and uses this to produce fake vanishing cycles, with equivariant intersection forms on the surface exterior as the main tool.
- **In plain words**: The paper studies smooth curves drawn on surfaces (such as the ordinary plane) viewed as shapes in four-dimensional space. It shows that for these curves, any way of re-mapping the curve's underlying real surface can be extended to a re-mapping of the surrounding four-dimensional space. This leads to simple closed loops on the curve that look like they could be the kind that can be shrunk away, yet are not.
- **Why it matters**: The result gives a clear, checkable answer to whether these curves are topologically flexible, and it produces "fake vanishing cycles," a notion that helps separate topological from algebraic behavior of curves. The text does not state wider consequences, so its connections beyond this area are unclear.
- **Background needed**: - Complex curve: a one-dimensional complex-algebraic object; its real points form a real surface.
- Linear system / ample: a family of curves cut out by polynomials of high enough degree on a surface.
- Simply connected surface: a surface with no non-trivial loops that cannot be shrunk.
- Mapping class: a way of moving a surface onto itself, considered up to smooth deformation.
- Topological flexibility: a curve whose surface re-mappings all extend to the ambient 4-dimensional space.
- Vanishing cycle: a loop that can be collapsed to a point inside a deformation of the curve; a fake one bounds a disk in the complement but is not a true vanishing cycle.
- Intersection form: a bookkeeping tool counting how surfaces and loops cross each other. · level: research-level

<details><summary>Original abstract</summary>

We prove that complex curves in sufficiently ample linear systems on simply connected projective surfaces are topologically (spin) flexible: any (spin) mapping class of the underlying real surface extends to a topological mapping class of the ambient 4-manifold. As a corollary, we prove that smooth curves in the complex projective plane are topologically (spin) flexible. A consequence of topological flexibility is the existence of fake vanishing cycles, that is, simple closed curves on the underlying real surface that are not vanishing cycles, yet still bound a topologically embedded $(\pm1)$-framed disk in the surface exterior. We also give examples of pushed in Seifert surfaces in $D^4$ that are not topologically spin-flexible, but become spin-flexible after a single internal stabilization. Our methods utilize the equivariant intersection form on the surface exterior.

</details>

### [Line bundles on regular semisimple Hessenberg varieties](https://arxiv.org/abs/2611.32752)
*Arkadev Ghosh, Pinakinath Saha* · `math.AG` · arXiv:2611.32752v1 · relevance 0.08

- **In one sentence**: For a connected simply-connected simple complex group G with Borel subgroup B, the paper gives a necessary and sufficient condition for the restriction map Pic(G/B) → Pic(Y) to be an isomorphism, where Y is an irreducible regular semisimple Hessenberg variety inside G/B.
- **In plain words**: This paper studies a family of geometric shapes, called Hessenberg varieties, sitting inside a standard space built from a symmetry group (the flag variety G/B). It asks when the "line bundles" on the big space (ways of attaching a one-dimensional twisted structure to each point, grouped into a group called the Picard group) carry over exactly to the smaller shape. The main result is a precise test that tells when this carrying-over is a perfect match.
- **Why it matters**: The text gives only the setup and the main statement, not the proof or examples, so its wider significance is hard to judge from here. It sits in algebraic geometry and relates to the study of Hessenberg varieties, which link to combinatorics and representation theory; that connection is my general understanding rather than something the text spells out.
- **Background needed**: - Algebraic group: a group of matrices or transformations defined by polynomial equations over the complex numbers.
- Borel subgroup and flag variety G/B: the space of nested chains of subspaces that the group acts on.
- Hessenberg variety: a subvariety of G/B defined by a linear-algebra condition involving a fixed matrix and a "Hessenberg" shape constraint.
- Regular semisimple: a condition on the defining matrix that makes the variety well-behaved (smooth, with nice symmetry).
- Picard group Pic(X): the group of isomorphism classes of line bundles on X, a way to measure the twisting of the space.
- Restriction map: taking a line bundle on the big space and restricting it to the smaller subvariety. · level: research-level

<details><summary>Original abstract</summary>

Let $G$ be a connected simply-connected simple algebraic group over $\mathbb{C}$ and $B$ be a Borel subgroup of $G$. Let $Y$ be an irreducible regular semisimple Hessenberg variety in $G/B$. In this article, we give a necessary and sufficient condition for the natural restriction map $\mathrm{res}: \mathrm{Pic}(G/B)\longrightarrow \mathrm{Pic}(Y)$ of Picard groups induced by the inclusion $Y\subseteq G/B$ to be an isomorphism.

</details>

## Topology

### [One monoid to realize them all: a master monoid for homotopy types](https://arxiv.org/abs/2611.32655)
*Isaac Carcac\'ia-Campos* · `math.AT` · arXiv:2611.32655v1 · relevance 0.17

- **In one sentence**: The paper shows that every homotopy type (CW complex up to homotopy) can be realized as the classifying space of the translation category of an action of a single monoid on a set, obtained by collapsing all objects of the semisimplicial category while keeping its face maps, and it analyzes when such a monoid can serve as a weak test category.
- **In plain words**: Homotopy theory studies shapes up to continuous deformation, and it is usually described using spaces or using collections of combinatorial building blocks. This paper asks whether all such shapes can instead be encoded by actions of one algebraic object, a monoid (a set with an associative operation and an identity), acting on sets. The authors find that this is possible for every CW complex, and that truncating the construction at dimension n gives a finitely presented object that captures exactly the shapes of dimension at most n.
- **Why it matters**: It offers a purely algebraic route into homotopy theory, which may matter for researchers interested in combinatorial or computational models of shape. The text also draws a distinction: one object can realize all homotopy types, yet that monoid need not model homotopy theory as a localization, and the obstruction is identifying objects rather than having only one. How far this connects to other frameworks is not established in the text.
- **Background needed**: - Homotopy type: a shape considered up to continuous deformation (for example, a sphere or a torus).
- CW complex: a standard way of building spaces by gluing cells of increasing dimension.
- Classifying space of a category: a space built from a category's objects and arrows, used to link combinatorics to topology.
- Monoid: a set with an associative binary operation and an identity element; an "action" of it on a set is a way of letting its elements transform that set.
- Semisimplicial category: a combinatorial category whose objects are ordered sets and whose maps are face operators, used to model spaces.
- Test category: a small category whose presheaves model homotopy theory; a "weak" test category is a relaxed version of this notion.
- Coreflective subcategory: a subcategory with a right adjoint-type inclusion, roughly a sub-collection closed under a canonical "best approximation". · level: research-level

<details><summary>Original abstract</summary>

Homotopy theory has traditionally been approached either through topological spaces or through categories of presheaves on suitable combinatorial categories, a perspective subsumed by Grothendieck's theory of test categories. In this paper, we develop a more algebraic viewpoint: homotopy types can be represented by actions of a single monoid on sets. This monoid is obtained by identifying all the objects of the semisimplicial category while retaining its face operators. Every CW homotopy type is the classifying space of the translation category of one of its actions, and its truncation at dimension n is finitely presented and realizes exactly the homotopy types of dimension at most n. The construction rests on a general result: every set-valued functor on a small category freely generates an action of its universal monoid, and its category of elements is a full coreflective subcategory of the resulting translation category. Hence every weak test category gives rise to a monoid whose actions realize all homotopy types; when the category has more than one object, however, this monoid is not itself a weak test category, so that a single monoid may realize all homotopy types without modelling homotopy theory as a localization. The obstruction lies in identifying objects, not in having a single one: there are strict test categories with a single object, such as the monoid of all self-maps of an infinite set and a countable monoid of primitive recursive functions.

</details>

### [An Introduction to O-minimal Geometry](https://arxiv.org/abs/2611.32426)
*Michel Coste* · `math.AG` · arXiv:2611.32426v1 · relevance 0.12

- **In one sentence**: Lecture notes covering the core theory of o-minimal structures, including cell decomposition, dimension, definable triangulation, generic fibers, and smoothness.
- **In plain words**: These are teaching notes on a branch of mathematics that studies "tame" collections of shapes and sets defined by simple rules. The text only lists the six chapters (the basic definitions, splitting shapes into simple pieces, counting dimension, cutting shapes into triangles, studying families of sets, and smoothness), so it does not report any new findings. It is an overview of how the subject is organized.
- **Why it matters**: The notes are a structured entry point into a field of mathematics concerned with well-behaved geometry, which has links to model theory and real algebraic geometry. The provided text is only a chapter list, so I cannot say more about its specific content or its influence.
- **Background needed**: - Sets in the plane or space and what "dimension" means for them
- Basic topology: open and closed sets, continuity, connected pieces
- Familiarity with real numbers, polynomials, and graphs of functions
- Some logic vocabulary helps: a "structure" is a collection of sets and functions on the real numbers, and "definable" means describable by a formula in that structure
- Triangulation means cutting a shape into simplices (triangles, tetrahedra, and their higher analogues) · level: research-level

<details><summary>Original abstract</summary>

These lecture notes on o-minimal geometry comprise six chapters: 1 - O minimal Structures. 2 - Cell Decomposition. 3 - Connected Components and Dimension. 4 - Definable Triangulation. 5 - Generic Fibers for Definable Families. 6 - Smoothness.

</details>

## Dynamical systems

### [Doubly Intermittent Singular Skew Products](https://arxiv.org/abs/2611.31490)
*Stefano Luzzatto, Rizwan Rizwanullah* · `math.DS` · arXiv:2611.31490v1 · relevance 0.10

- **In one sentence**: The paper studies a class of skew product systems (a uniformly expanding circle map coupled with a full branch interval map having two indifferent fixed points and unbounded derivatives), constructs an induced full branch map, and proves an invariant probability measure equivalent to Lebesgue plus decay of correlations.
- **In plain words**: This paper studies a mathematical model of a system that evolves step by step, where each step has a random-like driving component. The authors look at a broad family of such systems, which generalizes earlier examples from the literature. They show that these systems settle into a stable long-run pattern that matches ordinary uniform (Lebesgue) spread of points, and that their memory of starting conditions fades over time.
- **Why it matters**: The work extends a known family of examples (Gouëzel's skew products) to a much wider setting, which helps clarify which features drive the statistical behaviour. The text does not discuss applications, so any connection to physical or other modelling is unclear from this abstract alone.
- **Background needed**: - Dynamical system: a rule that repeatedly updates a point's position over time.
- Skew product: a system where one component's evolution depends on a second component, often read as a random dynamical system.
- Uniformly expanding map: a map that stretches distances by a fixed factor everywhere.
- Indifferent (neutral) fixed point: a point that the map leaves in place, where nearby points move very slowly; this makes orbits "intermittent," spending long stretches near such points.
- Invariant measure equivalent to Lebesgue: a long-run distribution of points that has the same null sets as ordinary length, so it is a natural "typical" distribution.
- Decay of correlations: how quickly the influence of the starting state fades; faster decay means more predictable long-run averages.
- Induced map: a simpler map obtained by looking only at the times the system returns to a chosen region. · level: research-level

<details><summary>Original abstract</summary>

We study a large class of skew product systems, which can also be thought of as random dynamical systems, coupling a uniformly expanding circle map with a full branch interval map with two indifferent fixed points and unbounded derivatives. This significantly generalizes the setting of several skew products considered in the literature, in particular the Gou\"ezel skew products [Gou\"ezel, Statistical properties of a skew product with a curve of neutral points, Erg. Th. & Dyn. Sys. (2007)], in which the fibre maps are intermittency maps with a single indifferent fixed point and bounded derivatives. Through the construction of an induced full branch map, we prove various statistical properties of the skew products, including existence of an invariant probability measure equivalent to Lebesgue and decay of correlations.

</details>

### [Saddle-focus to saddle transition of 4D heteroclinic orbits resembling oscillatory and regularized shock waves of some dissipative Boussinesq systems](https://arxiv.org/abs/2611.31934)
*Rezwana Razzaque Angana, Brendan Harding, Dimitrios Mitsotakis* · `math.DS` · arXiv:2611.31934v1 · relevance 0.09

- **In one sentence**: The paper computes traveling-wave solutions of dissipative Bona–Smith Boussinesq systems that resemble oscillatory and regularized shock waves, using heteroclinic orbits in a four-dimensional phase space whose equilibrium changes from a saddle-focus to a saddle as dissipation increases, and introduces a finite-difference numerical method to compute them.
- **In plain words**: The paper studies the shape of waves that move at a steady speed in shallow water models, such as the bores (wave fronts) that form when a tidal or river surge advances. The authors describe two kinds of wave front, one with ripples and one smooth, and show how the first can turn smoothly into the second as friction-like damping (dissipation) increases. They also present a numerical method for computing these waves.
- **Why it matters**: The work links a change in the local structure of a mathematical system (a saddle-focus turning into a saddle) to a visible change in wave shape, which is a clear example of how structure governs behavior. The text does not show practical applications beyond undular bore modeling, so its wider impact is uncertain.
- **Background needed**: - Shallow-water waves: a bore is a sudden rise of water front; "undular" means it has a train of ripples behind it, while "regularized" means it is smooth.
- Boussinesq-type models: equations approximating water waves that include dispersion (waves of different wavelengths travel at different speeds).
- Dissipation: energy loss, such as friction, that damps the wave.
- Traveling wave: a wave that keeps its shape while moving at constant speed, reducing the PDE to an ODE system.
- Phase space and equilibria: a state space where each point is a possible system state; equilibria are fixed points.
- Saddle vs. saddle-focus: types of equilibria, classified by how nearby trajectories approach or leave them (saddle-focus includes spiraling).
- Heteroclinic orbit: a trajectory leaving one equilibrium and arriving at another. · level: research-level

<details><summary>Original abstract</summary>

Oscillatory and regularized shock waves have long been studied to understand the formation and dynamics of undular bores in shallow waters, phenomena that typically arise from the interplay between dispersion, nonlinearity, and dissipation. In this work, we investigate and describe the nature and shape of traveling wave solutions that resemble oscillatory and regularized shock waves of some Boussinesq-type water wave models known as Bona--Smith systems in the presence of dissipation. The associated traveling wave equations are solutions of four-dimensional dynamical systems, leading to both computational challenges and rich structural behavior. In particular, to describe the properties of these traveling waves, we analyze heteroclinic orbits that connect two distinct equilibria, one of which undergoes a transition in the four-dimensional phase space from a saddle-focus to a saddle point as the dissipation parameter increases. This transition governs the nature of the wave profile, which evolves smoothly from an oscillatory shock wave to a regularized (non-oscillatory) shock wave. To compute such solutions, we introduce a finite-difference-based numerical method tailored for this class of problems.

</details>

## Combinatorics

### [The majority game chromatic number for dense random graphs](https://arxiv.org/abs/2611.32746)
*Stijn Cambie, Annika Heckel, Brahadeesh Sankarnarayanan et al.* · `math.CO` · arXiv:2611.32746v1 · relevance 0.33

- **In one sentence**: For fixed edge probability 2/3 < p < 1, the majority game chromatic number of the random graph G(n,p) equals 3 with high probability.
- **In plain words**: The paper studies a two-player game on random networks: players take turns colouring the vertices of a graph so that no two neighbours share a colour, and the question is how few colours are needed. For random graphs where most pairs of vertices are connected (edge probability between 2/3 and 1), the authors show that three colours are enough with high probability, meaning the chance of this holding tends to 1 as the graph grows.
- **Why it matters**: It gives a precise answer for a specific, fairly dense range of random graphs, which sharpens what is known about how such games behave. The abstract alone does not say how it connects to wider applications, so any broader significance is uncertain.
- **Background needed**: - Graph: a set of vertices joined by edges, like people connected by friendships.
- Proper colouring: giving each vertex a colour so that no two adjacent vertices share one.
- Chromatic number: the fewest colours needed for a proper colouring.
- Random graph G(n,p): n vertices, each pair joined independently with probability p.
- Maker-Breaker / game version: two players alternately colour vertices; the "majority" rule is a specific variant of how the game is scored or played (the text does not spell out the rules).
- "With high probability": the claim holds with probability approaching 1 as n grows. · level: research-level

<details><summary>Original abstract</summary>

We show that for every fixed $2/3<p<1$ the majority game chromatic number of the Erd\H{o}s--R\'enyi random graph $G_{n,p}$ is $3$ with high probability.

</details>

### [On some off-diagonal hypergraph Ramsey problems](https://arxiv.org/abs/2611.32594)
*Eion Mulrenin, Cosmin Pohoata* · `math.CO` · arXiv:2611.32594v1 · relevance 0.11

- **In one sentence**: A short new proof of a lower bound on the off-diagonal 3-uniform Ramsey number r_3(K_4^-, K_n), via a construction linked to Bradač's directed graph, with claimed sharp bounds for higher-uniformity variants that answer questions of Mubayi and Suk.
- **In plain words**: This paper is about how large a set of items must be before a certain pattern is forced to appear when every group of items is coloured in one of two ways. The authors give a shorter proof of an earlier result by Fox and He, which says the required size grows at least roughly like 2 raised to the power n log n. They build the key example using a directed graph (a network of arrows between points) that Bradač introduced earlier.
- **Why it matters**: The abstract says the construction also extends naturally to several related problems in higher uniformity and gives sharp bounds there, answering open questions from Mubayi and Suk. The text provided does not say more about the wider significance, so the scope beyond these specific questions is unclear.
- **Background needed**: - Ramsey number: the smallest size of a structure guaranteeing a given pattern appears whenever its elements are two-coloured.
- Graph vs. hypergraph: a graph links pairs of points; a 3-uniform hypergraph links triples of points.
- K_n is the complete graph on n points (every pair linked); K_4^- is four points with all triples-in-pairs links except one.
- Off-diagonal: the two colour classes are asked to forbid different patterns, here K_4^- and K_n.
- Lower bound 2^{Ω(n log n)}: a construction showing the number is at least exponentially large in n log n, up to constant factors.
- Sharp bound: a bound that matches the true value up to constant factors, so cannot be improved in order of magnitude.
- Directed graph: a graph whose edges have a direction, like one-way arrows. · level: research-level

<details><summary>Original abstract</summary>

We give a new short proof of a theorem of Fox and He that the $3$-uniform Ramsey number $r_3(K_4^-, K_n)$ is at least $2^{\Omega(n \log n)}$. The construction exploits a new connection with a directed graph recently introduced by Brada\v{c} in his work on off-diagonal graph Ramsey numbers. Moreover, it generalizes naturally to give sharp bounds for several extensions of this problem in higher uniformity, answering questions raised by Mubayi and Suk.

</details>

## Numerical analysis

### [An adaptive finite element method for the interior problem of Helmholtz equations with generalized transmission boundary conditions](https://arxiv.org/abs/2611.32479)
*Zhe Zhu, Lei Lin, Wei Yang et al.* · `math.NA` · arXiv:2611.32479v1 · relevance 0.26

- **In one sentence**: The paper develops an adaptive finite element method, with a T-coercivity argument via a lifting operator, for the interior transmission problem for Helmholtz equations with generalized transmission boundary conditions involving a surface Laplace-Beltrami operator, including a priori and a posteriori error estimates and interior transmission eigenvalue computations.
- **In plain words**: This paper is about a numerical method for solving a wave-type equation (the Helmholtz equation) inside a region when the boundary carries a special coupling condition. The authors build a computational scheme that refines its mesh adaptively, where the error is largest, and they prove the scheme's well-posedness and error bounds. They also report numerical tests showing accuracy and convergence, and they extend the method to compute certain special eigenvalues of this interior transmission problem.
- **Why it matters**: Problems of this type arise in wave scattering and inverse scattering, where interior transmission eigenvalues are studied. The text supports the claims of accuracy and efficiency only through numerical examples, and it does not indicate applications beyond this setting, so the wider significance is uncertain.
- **Background needed**: - Helmholtz equation: a standard model for time-harmonic waves (sound, light, electromagnetic fields).
- Interior transmission problem: a coupled system of two wave equations inside a region, with matching conditions on its boundary.
- Generalized transmission boundary conditions: boundary coupling rules that include a surface Laplace-Beltrami operator, a generalization of the Laplacian that acts along a curved surface.
- Finite element method: approximating a solution by piecewise simple functions on a mesh of small cells.
- Adaptive refinement with a posteriori error estimates: computable error indicators guide where the mesh is refined; upper and lower bounds show the indicator tracks the true error.
- A priori vs. a posteriori error estimates: bounds derived before computing (depending on the unknown solution's smoothness) versus bounds computed from the approximate solution itself.
- T-coercivity and lifting operator: a technique for proving well-posedness in nonstandard function spaces where the usual coercivity argument does not directly apply.
- Interior transmission eigenvalues: special frequencies at which the interior transmission problem has nontrivial solutions; they matter in inverse scattering. · level: research-level

<details><summary>Original abstract</summary>

This paper proposes a new adaptive finite element method for solving the interior transmission problem with generalized transmission boundary conditions (GTBCs) involving a surface Laplace-Beltrami operator. A $\mathbb{T}$-coercivity technique relying on a lifting operator is established to show the well-posedness of the variational problem in appropriate nonstandard Sobolev spaces. Then both the a priori error estimates and a posteriori error estimates including the upper bound and local lower bound of the finite element discretization are constructed. Numerical examples are presented to illustrate the accuracy and convergence of the adaptive finite element method. Extension and high efficiency of the proposed method for the computation of the interior transmission eigenvalues for the problem with GTBCs are also discussed numerically.

</details>

### [Upwind finite element approximation of the gradient blow-up time for a viscous Hamilton--Jacobi equation](https://arxiv.org/abs/2611.31859)
*Yohei Fujishima, Takahiro Yamada* · `math.NA` · arXiv:2611.31859v1 · relevance 0.18

- **In one sentence**: The paper proves maximum-norm convergence of an upwind piecewise-linear finite element scheme for a viscous Hamilton--Jacobi equation with superquadratic gradient source, and shows that discrete gradient-threshold blow-up times converge to the exact blow-up time under stated mesh and regularity assumptions in dimensions one to three.
- **In plain words**: The paper studies a equation that describes how a quantity's slope can grow without limit in finite time, so the computed solution "blows up." The authors analyze a computer method for approximating this solution on a mesh and prove that the approximation stays close to the true solution until the slope blows up, and that the computed time of blow-up approaches the true time. They also check that the assumptions hold for one example on a disk and show numerical experiments of the blow-up.
- **Why it matters**: Predicting when a solution breaks down numerically is hard, because simulations can go wrong near the blow-up. The paper gives mathematical guarantees for a specific scheme, which is useful for anyone trusting numerical simulations of such equations; the text does not say how far the results extend beyond this setting.
- **Background needed**: - Hamilton--Jacobi equation: a partial differential equation describing how a function changes over time, here with a gradient (slope) term.
- Viscous term: a diffusion/smoothing term that keeps solutions well-behaved for a while.
- Gradient blow-up: the slope of the solution becomes infinite at a finite time.
- Superquadratic source: the nonlinear growth term in the slope grows faster than the square of the slope.
- Finite element method: a numerical technique that approximates a solution by piecewise simple functions on a mesh of small cells.
- Upwind scheme: a discretization that biases calculations toward the direction the information flows, for stability.
- Maximum-norm convergence: the error is measured by the largest pointwise difference.
- Dirichlet boundary condition: the solution is fixed (here zero) on the boundary of the domain.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

We analyze an upwind finite element method with piecewise linear elements for a viscous Hamilton--Jacobi equation with a superquadratic gradient source term, subject to homogeneous Dirichlet boundary conditions. On polytopal inner approximations of smooth bounded domains in dimensions $N=1,2,3$, we prove maximum-norm convergence of the numerical solution to the exact solution before gradient blow-up and convergence of gradient-threshold times to the blow-up time under explicit mesh and regularity assumptions. We also verify the regularity assumption and finite-time gradient blow-up for an example on the disk, to which the main theorem therefore applies. Numerical experiments illustrate this gradient blow-up.

</details>

## Logic and foundations

### [Cardinal Transfer Events for Infinitary Logic with Infinitary Quantification](https://arxiv.org/abs/2611.31725)
*Edgar Valenzuela* · `math.LO` · arXiv:2611.31725v1 · relevance 0.08

- **In one sentence**: Under an assumed theory Φ, the paper solves the Gap-n problem for more than one predicate in infinitary logic with infinitary quantification, as a cardinal transfer result.
- **In plain words**: This paper is about a kind of logic that allows statements built from infinitely many pieces, where one can also quantify over infinitely many objects at once. It studies "transfer" results, which ask when a property that holds in a large infinite universe also holds in a smaller one. The abstract says that, assuming a certain theory called Φ exists, the authors settle a version of the Gap-n problem for several predicates at once.
- **Why it matters**: The abstract is very short, so its significance is hard to judge from it alone. It likely matters to specialists in set theory and model theory, who study how infinite cardinal sizes constrain what logical statements can say.
- **Background needed**: - Logic: a formal language for stating and checking claims, here extended to infinitely long formulas.
- Predicate: a property or relation that a statement can talk about, such as "is red" or "is less than".
- Cardinal numbers: measures of infinite size, such as the size of the natural numbers.
- Transfer result: a claim that a structure of one infinite size with a property implies another structure of a smaller infinite size has it too.
- Gap-n problem: a specific open question in this area about how such transfers behave, which the text does not define.
- Assumed theory Φ: the result is conditional on an extra mathematical hypothesis whose details are not given in the text. · level: research-level

<details><summary>Original abstract</summary>

Assuming the existence of a certain theory $\Phi$, we solve the Gap-$n$ problem for more than one predicate. This will be done for infinitary logic with infinitary quantification.

</details>

### [Alpha-Beta Pruning via Monadic Continuations](https://arxiv.org/abs/2611.32320)
*Mart\'in Escard\'o, Paulo Oliva* · `cs.AI` · arXiv:2611.32320v1 · relevance 0.06

- **In one sentence**: The paper gives a monadic (continuation- and reader-monad based) formulation of alpha-beta pruning for minimax game search, records pruning bounds inside monadic outcomes rather than in move types, extends outcomes to return optimal plays, and proves the result matches exhaustive minimax.
- **In plain words**: The paper looks at a standard method that lets a game-playing program find the best move while skipping many possible lines of play that cannot change the answer. The authors rewrite this method using abstract programming structures called monads, which keep track of intermediate results in a tidy way. They test it on Tic-Tac-Toe, where it evaluated 39 times fewer plays than checking every possibility, and they formally prove it gives the same answers as the full exhaustive search.
- **Why it matters**: Alpha-beta pruning is a foundational technique in game AI, so a cleaner, provably correct way to express it within standard functional-programming abstractions may be useful for building and verifying search code. The text reports only a Tic-Tac-Toe example, so its impact on larger games or practical systems is not shown here.
- **Background needed**: - Minimax: a search where one player maximises and the opponent minimises the final score, over all possible game continuations.
- Alpha-beta pruning: a speed-up that stops exploring a branch once it is clear it cannot change the decision.
- Monad: a programming abstraction for chaining computations that carry extra context; used here to organise search results.
- Continuation monad: a way of passing "what happens next" as a function, letting a search decide how to proceed.
- Reader monad: a way of passing shared settings (here, the pruning bounds) implicitly through a computation.
- Selection monad: a related abstraction for choosing moves in games, which the text says is inefficient for alpha-beta search.
- Formal correctness proof: a mathematical argument, typically checked by a proof assistant, that the program meets its specification. · level: research-level

<details><summary>Original abstract</summary>

Alpha-beta pruning is a fundamental technique in game-playing AI, enabling efficient minimax search by avoiding the exploration of branches that cannot affect the optimal decision. We present a monadic formulation of alpha-beta pruning based on the combination of the continuation monad and the reader monad. Unlike previous approaches that encode alpha-beta bounds into the types of available moves, our construction records these bounds within monadic outcomes, leaving the move types unchanged. We further show that the ordinary continuation monad suffices to compute not only optimal outcomes but also optimal plays, by extending the outcome type to include the corresponding sequences of moves. This provides an alternative to generalisations of the continuation monad proposed to address the inefficiencies associated with the selection monad in alpha-beta search. We illustrate our approach with an implementation of Tic-Tac-Toe, observing a 39-fold reduction in the number of plays evaluated, compared with exhaustive search, in computing an optimal play. Finally, we formally establish the correctness of our construction by proving that the monadic alpha-beta search computes the same optimal outcomes and plays as exhaustive minimax search. Our results demonstrate how a foundational algorithm in AI can be expressed and verified using standard monadic abstractions, providing a basis for further development of compositional approaches to adversarial search.

</details>

## Mathematical physics

### [Dynamical phase transition in Brownian motion via sharp large deviations](https://arxiv.org/abs/2611.31453)
*Benjamin Budway, Makiko Sasada, Mykhaylo Shkolnikov* · `math.PR` · arXiv:2611.31453v1 · relevance 0.15

- **In one sentence**: The paper proves a dynamical phase transition for Brownian motion with drift conditioned on upper large deviations of its occupation measure on [-1,1], using a new sharp large deviation estimate for that occupation measure.
- **In plain words**: The paper studies a random path (Brownian motion with a steady push, or drift) observed over a long stretch of time, and asks what it looks like when we force it to spend unusually much time in a fixed interval. The authors show that the answer changes sharply depending on how unusual the forced event is: for very extreme cases the path behaves one way, and for milder cases it behaves in a different way for part of the time and then acts like an ordinary random path. They prove this using a new, more precise version of a large deviation estimate, which is a bound on how rare such unusual events are.
- **Why it matters**: The result turns a dynamical phase transition, previously predicted in the physics literature, into a rigorous mathematical theorem, which gives confidence in those predictions. The sharp large deviation estimate is stated to be of independent interest, and the authors note possible extensions to other Markov processes and additive functionals, though the text does not detail those applications.
- **Background needed**: - Brownian motion: the mathematical model of a random, jittery path, such as a pollen grain's motion in water.
- Drift: a constant tendency to move in one direction added to the random motion.
- Occupation measure: the fraction of total time the path spends in a given region (here, the interval [-1,1]).
- Large deviation: an event that is far less likely than typical behavior, and the study of how fast its probability shrinks.
- Conditioning (Gibbs-style): looking at how the path behaves given that a rare event has occurred.
- Phase transition: a sudden qualitative change in behavior as a parameter crosses a threshold, like water freezing.
- Donsker-Varadhan variational formula: a standard tool for computing the rate of such rare events for time-averaged quantities.
- Langevin diffusion: a standard random process with a pull toward a preferred state; the conditioned path follows one of these. · level: research-level

<details><summary>Original abstract</summary>

We prove a dynamical phase transition in Brownian motion with drift, a phenomenon recently predicted in the physics literature. Specifically, when a Brownian motion with drift on a long time interval is conditioned on an upper large deviation event for the (normalized) occupation measure of the interval [-1,1], in the spirit of the Gibbs conditioning principle, a phase transition occurs. If one conditions on a large deviation event in the far upper tail, the conditioned process follows the Langevin diffusion suggested by the Donsker-Varadhan variational formula for additive functionals. In contrast, if one conditions on a large deviation event in the near upper tail, the conditioned process follows a different Langevin diffusion on a fraction of the time interval and subsequently behaves like the unconditioned process. We establish this phase transition via a new sharp large deviation result for the occupation measure, which is of independent interest. We also provide further corollaries of this result and discuss generalizations to other Markov processes and additive functionals.

</details>

### [The role of composition rules in an axiomatic derivation of quantum mechanics](https://arxiv.org/abs/2611.32237)
*Erkka Haapasalo, Pekka Lahti, Juha-Pekka Pellonp\"a\"a* · `quant-ph` · arXiv:2611.32237v1 · relevance 0.13

- **In one sentence**: The paper revisits how local effects and states of subsystems are embedded into compound-system spaces within D'Ariano et al.'s information-theoretic axiomatization of quantum mechanics, using composition rules from Matolcsi and from Aerts and Daubechies, and proposes weaker purification and local discrimination axioms with tensor-product structure.
- **In plain words**: This paper looks at one of the rule sets used to rebuild quantum mechanics from basic principles about information and measurement. It asks how the behavior of parts of a combined system should be formally described, instead of simply assuming the standard mathematical "tensor product" construction. The authors add axioms saying that joint states can be told apart by measurements on each part, and they restate a key axiom ("purification") in a weaker form.
- **Why it matters**: Deriving quantum theory from a few physical principles is a long-running question in foundations of physics, and the composition of subsystems is one of the places where the standard mathematics is usually taken for granted. The text does not show what practical or experimental consequences follow, so its significance is best seen as foundational and technical.
- **Background needed**: - Quantum mechanics describes systems through "states" (what is known about a system) and "effects" (possible measurement outcomes).
- An axiomatic derivation starts from a short list of principles and aims to show that quantum theory is the only theory satisfying them.
- A "compound system" is a combination of parts, such as two particles considered together.
- The "tensor product" is the standard mathematical way to combine the spaces of two parts into the space of the whole.
- "Purification" roughly means every mixed (partly random) state can be seen as part of a pure state of a larger system.
- "Local discriminability" means that different joint states can be distinguished using measurements on each part separately.
- Projective and injective tensor products are two specific mathematical ways of combining spaces, with different properties. · level: research-level

<details><summary>Original abstract</summary>

Local discriminability and purification are two key axioms in an information-theoretic axiomatization of quantum mechanics as proposed by G. M. D'Ariano et al. (Quantum Theory from First Principles, 2017). Both of them refer to compound systems, the theory of which is rather directly assumed to be given by the tensor product structure. This structure, though well understood, should, however, be based on a more careful study of formal composition rules describing how local effects can be embedded into the compound effect space and how to reduce joint states onto subsystems. In that we follow the earlier work of T. Matolcsi, (Acta Sci. Math., 1975), and D. Aerts and I. Daubechies, (Helvetica Physica Acta, 1978), as summarized, e.g., in The Logic of Quantum Mechanics, 1981, by E. Beltrametti and G. Cassinelli. We also establish axioms of local discrimination stating that compound states can be told apart by local measurements the notion of which we also formally define. The purification axioms first introduced as axioms of quantum mechanics by D'Ariano et al. are also rewritten in a weaker form which we believe could be fruitful for future axiomatizations. These reformulations bring us closer to proper tensor product structures for joint state and effect spaces, so that the embedding map for states factors through the projective tensor product of the local state spaces and the embedding map for effects factors through the injective tensor product of the local effect spaces. We also discuss the case of multipartite composition axioms and associativity properties required in these settings.

</details>

## Optimization and control

### [Mirror flow for semimartingale optimal transport](https://arxiv.org/abs/2611.32785)
*Francois Buet-Golfouse, Ana\"is Despr\'es, Anna Kazeykina et al.* · `math.OC` · arXiv:2611.32785v1 · relevance 0.20

- **In one sentence**: The paper proposes a mirror flow (a preconditioned mirror-descent scheme) for the dual problem of semimartingale optimal transport, proves geometric convergence of the mirror descent sequence, and gives a first-order linearized discrete-time scheme with a uniform-in-time error bound.
- **In plain words**: The paper looks at a mathematical problem about finding the cheapest way to move random processes from one description to another, a setting that comes up in finance and in some generative AI models. Gradient-style search for the solution is often slow because the problem is badly scaled. The authors replace it with a "mirror" version that reshapes the geometry of the search so it behaves better, and they build a practical step-by-step version of it.
- **Why it matters**: Slow convergence is a practical bottleneck for these problems, so a better-conditioned search method could matter for computation in finance and flow-based generative modelling. The text reports a substantial efficiency gain on one specific test problem (SEMOT); how far this carries to other problems is not shown in the text.
- **Background needed**: - Optimal transport: finding the least-cost way to rearrange one distribution into another.
- Semimartingale: a broad class of random processes (generalising Brownian motion) used in stochastic calculus.
- Martingale: a process whose best forecast of its future value is its current value; a fair-game condition.
- Dual energy functional: an equivalent reformulation of the problem in terms of a auxiliary "potential" function whose optimum gives the answer.
- Gradient descent: iteratively improving a guess by stepping downhill; slow when the landscape is stretched unevenly (poorly conditioned).
- Mirror descent / mirror flow: a variant of gradient descent that measures steps in a transformed geometry to fix such unevenness.
- Linearization and discretization: approximating a continuous-time flow by small computable steps, with error from the approximation. · level: research-level

<details><summary>Original abstract</summary>

Semimartingale optimal transport arises in a wide range of applications, including mathematical finance and flow-based generative models. A recurring computational challenge is that the dual energy functional is often poorly conditioned with respect to the dual potential, leading to slow convergence of gradient descent algorithms. To address this issue, we investigate a mirror flow approach that effectively preconditions the dual energy functional. We establish the geometric convergence of the mirror descent sequence. To obtain a practical numerical algorithm, we introduce a feasible discrete-time scheme based on first-order linearization. We prove that the scheme is well-defined and establish a uniform-in-time error bound for the accumulated linearization error, under a suitable smallness condition on the initial error. Finally, we apply the proposed mirror flow scheme to the specific-entropic martingale optimal transport (SEMOT) problem \cite{BuetGolfouseEtAl2026SEMOT} and observe a substantial improvement in computational efficiency.

</details>

### [Beyond Classical Minimax Rates: Quantum Sampling in Gradient-Based Simulation Optimization](https://arxiv.org/abs/2611.32004)
*Hao Cao, Jian-Qiang Hu, Mingjie Hu et al.* · `quant-ph` · arXiv:2611.32004v1 · relevance 0.17

- **In one sentence**: For gradient-based optimization of convex simulation problems with noisy gradient estimates, the paper shows quantum mean estimation applied to paired finite differences improves the query-complexity accuracy exponent from -2/3 to -4/3 (classical minimax rate in the independent case), with coupling-dependent generalizations and matching lower bounds for fixed dimension.
- **In plain words**: The paper studies how to find the best setting of a quantity when each check is done by a noisy computer simulation and the slope (gradient) must be estimated from those noisy results. It asks how accurately one can optimize for a given number of simulation runs. The authors report that using a quantum method to average the estimates, along with carefully coupling nearby simulation runs, reduces the error faster than classical methods can under the same budget.
- **Why it matters**: The result is a theoretical claim about how fast error can shrink, and it comes with matching lower bounds that suggest the exponents cannot be beaten for fixed dimension under the stated assumptions. It may matter for anyone who pays for expensive simulations, though the text is purely theoretical and says nothing about practical quantum hardware or real-world runtimes.
- **Background needed**: - Simulation optimization: finding the input that minimizes an output of a noisy simulator, where each run costs time or money.
- Gradient: the slope of the objective with respect to inputs; here it is estimated by finite differences (small perturbations of the input and comparing outputs).
- Convergence rate / query complexity: how the error shrinks as the number of simulation queries N grows; an exponent like -2/3 means error scales roughly as N to the power -2/3.
- Minimax optimal: no method can do better in the worst case, and a matching lower bound proves this.
- Variance reduction and coupling: running paired simulations with shared randomness so their difference is less noisy; the parameter kappa measures this.
- Quantum mean estimation: a quantum-computing technique for estimating an average with fewer samples than classical averaging, here assumed to be available as a subroutine. · level: research-level

<details><summary>Original abstract</summary>

We study gradient-based search for a class of convex simulation optimization problems with gradients estimated from noisy outputs. With independent outputs, the optimal classical convergence rate for the expected objective gap is of order $O(N^{-2/3})$, where $N$ is the query budget. We apply quantum mean estimation to paired finite differences and progressively increase their estimation accuracy as the perturbations shrink, improving the convergence rate to $O(N^{-4/3})$. Furthermore, we show that coupling nearby evaluations improves the classical and quantum convergence rates to $O(N^{-2/(3-\kappa)})$ and $O(N^{-4/(3-\kappa)})$, respectively, where $\kappa\in[0,1]$ describes the variance reduction in paired outputs. Thus, quantum estimation halves the accuracy exponent in query complexity across coupling orders. Moreover, we establish matching lower bounds and show that these accuracy exponents are minimax optimal for fixed decision dimension, even when query locations and batch sizes are adaptive. Reconstruction from feasible differences retains the exponents when every simulation query must be feasible and accommodates boundary optima.

</details>

## Statistics theory

### [Sharp Hellinger Risk of the Multivariate Gaussian NPMLE](https://arxiv.org/abs/2611.31728)
*Xingzhou Wang, Zheng Li* · `math.ST` · arXiv:2611.31728v1 · relevance 0.11

- **In one sentence**: The paper shows that the unconstrained nonparametric maximum likelihood estimator for multivariate Gaussian location mixtures with sub-Gaussian tails attains the minimax rate (log n)^d/n under squared Hellinger loss, improving an earlier (log n)^{d+1}/n upper bound by a log factor.
- **In plain words**: The paper studies a standard method for estimating an unknown probability distribution from data, when the data are noisy Gaussian bell-curve draws around hidden centers. It proves that this estimator is as accurate as theoretically possible, up to the stated rate, in any fixed number of dimensions, improving a previous estimate by a logarithmic factor. The main tool is a sharp count of how many small pieces are needed to approximate multivariate polynomials, and the lower bound comes from adapting an existing construction.
- **Why it matters**: It closes a gap between the known upper and lower bounds for this estimator in the multivariate setting, which matters for understanding how well mixture-density estimation can work in practice. The polynomial bracketing bound may also be useful in other empirical-process arguments, though the text does not establish such uses.
- **Background needed**: - Gaussian location mixture: data generated by picking a hidden center from some distribution, then adding Gaussian (bell-curve) noise.
- Nonparametric maximum likelihood estimator (NPMLE): choosing the mixing distribution that makes the observed data most likely, with no fixed shape assumed.
- Hellinger distance: a way to measure how different two probability densities are, commonly used for squared-error-type loss in density estimation.
- Minimax rate: the best worst-case error any estimator can guarantee; a matching upper and lower bound means the rate is sharp.
- Bracketing number: the number of simple upper and lower envelope functions needed to cover a function class at a given precision; a standard measure of complexity.
- Sub-Gaussian tail: the hidden centers are unlikely to be far from zero, decaying at least as fast as a Gaussian.
- Log factor: a slowly growing term (log n) that separates the earlier and current rates. · level: research-level

<details><summary>Original abstract</summary>

For multivariate Gaussian location mixtures whose mixing distributions have coordinatewise sub-Gaussian tails, we prove that the unconstrained nonparametric maximum likelihood estimator attains the minimax rate $(\log n)^d/n$ under squared Hellinger loss. This holds for every fixed dimension $d\geq2$ and every fixed tail parameter $\sigma>0$. The upper bound applies to every measurable choice of a global likelihood maximizer and improves the earlier bound of order $(\log n)^{d+1}/n$ by a factor of $\log n$. A key step is a sharp bracketing bound for multivariate polynomials. For the $L^2(\rho)$ unit ball of real polynomials in $d$ variables with total degree at most $m$, the log bracketing number at width $\varepsilon$ is at most $\binom{m+d}{d}\log(C_d/\varepsilon)$ for $0<\varepsilon\leq1$. The constant $C_d$ depends only on $d$. The bound holds for every positive Borel measure $\rho$ under which each nonzero polynomial in the space has a finite, positive $L^2(\rho)$ norm. We prove the bound using volume estimates for a complex Veronese cone and Gaussian small-ball probabilities, then apply it to bound the local Hellinger bracketing entropy of Gaussian mixture densities. We obtain the matching minimax lower bound by adapting the Hermite perturbation construction of Kim and Guntuboyina.

</details>

### [Aalen-Johansen as an augmented IPCW estimator](https://arxiv.org/abs/2611.32026)
*Lu Mao* · `stat.ME` · arXiv:2611.32026v1 · relevance 0.06

- **In one sentence**: The paper shows the Aalen-Johansen estimator of state occupation probabilities is an augmented inverse-probability-of-censoring-weighted estimator, decomposes its influence function against the semiparametric efficient one, and proposes a model-free least-squares augmentation that narrows the gap under non-Markov processes without raising asymptotic variance.
- **In plain words**: The paper concerns a standard tool for following people through a sequence of health states (for example healthy, ill, dead) when some people drop out of observation partway through. The authors show that this tool, the Aalen-Johansen estimator, can be rewritten as a weighted correction for dropouts plus a built-in guess about each person's next state based on the state they are in now. They then propose a simple add-on that uses a little of each person's earlier history to improve the estimate, and report that it helps in theory and in simulations.
- **Why it matters**: Multi-state survival estimates are used widely in medical and actuarial work, so a clearer account of why the standard method is robust, and where it loses efficiency, is useful. The text does not indicate applications beyond simulation studies, so the practical impact is unclear from this summary alone.
- **Background needed**: - Multi-state model: people move among a set of states over time, and we want the probability of being in each state at a given time.
- Censoring: some people are lost to follow-up, so their outcome is only partly observed.
- Inverse probability of censoring weighting (IPCW): re-weights observed people to stand in for those lost to follow-up.
- Markov assumption: the future depends only on the current state, not on earlier history.
- Aalen-Johansen estimator: the standard nonparametric estimator for state occupation probabilities.
- Influence function and asymptotic variance: describe how an estimate responds to individual data and how precise it is in large samples.
- Semiparametric efficiency: the lowest achievable variance among estimators that do not rely on a fully specified model. · level: research-level

<details><summary>Original abstract</summary>

We show that, in every sample, the widely used Aalen-Johansen estimator of a state occupation probability is an inverse probability of censoring weighted estimator augmented by a working Markov prediction from each subject's current state. This identity explains the robustness of the Aalen-Johansen against departures from the Markov assumption. It also reveals that its influence function differs from the semiparametric efficient one by two orthogonal components: the information in earlier history beyond the current state, and the error of the Markov prediction. Based on this decomposition, we propose a practical, model-free least-squares augmentation of the Aalen-Johansen that regresses the outcome on a history score, narrowing the gap under non-Markov processes without increasing the asymptotic variance. Its advantages are validated both theoretically and in simulations.

</details>

## Statistical methods and applications

### [Admissibility of Linear Time Series Models under Cone Constraints](https://arxiv.org/abs/2611.32414)
*Won-Ki Seo* · `math.ST` · arXiv:2611.32414v1 · relevance 0.16

- **In one sentence**: The paper gives necessary and sufficient support conditions for stationary Hilbert-space linear processes to stay almost surely inside a closed convex cone, and studies the consequences for quantiles, densities and covariance matrices.
- **In plain words**: Many data objects, such as probability densities, quantile curves and covariance matrices, must obey fixed rules (for example, being nonnegative or increasing). The paper asks when a standard additive time-series model, which adds shocks step by step, can respect such rules over time. It finds that with certain shock types, such as Gaussian ones with unbounded lower tails, the randomness is squeezed into a restricted set of directions, and it builds examples that still work with bounded shocks.
- **Why it matters**: Ordinary linear time-series models are widely used, so knowing when they can be applied to constrained objects without breaking the constraints clarifies their scope. The text does not indicate specific applications or wider connections beyond this theoretical scope.
- **Background needed**: - Time series: data recorded in sequence over time, where each value depends on earlier ones.
- Linear process: a model where the current value is a weighted sum of past random shocks (innovations).
- Stationary: the statistical behaviour does not change over time.
- Hilbert space: an infinite-dimensional generalisation of ordinary geometry, used for curves or functions as data.
- Closed convex cone: a set closed under nonnegative scaling and addition, such as nonnegative functions or positive semidefinite matrices; "almost surely" means with probability one.
- Quantile function: the inverse of a cumulative distribution, describing where a distribution's values fall.
- Fractional filter: a weighting scheme with slowly decaying coefficients, giving long memory.
- Random walk: a process that accumulates shocks, so its variance grows over time. · level: research-level

<details><summary>Original abstract</summary>

Time series analysis extends beyond vector-valued observations to evolving probability densities, quantile functions, and covariance operators. These objects carry intrinsic constraints, raising questions about the admissibility of additive linear models, which have long served as a foundation for time series modelling and theory. We give a necessary and sufficient support condition for a stationary Hilbert-space linear process to remain in a closed convex cone almost surely. Innovations with unbounded lower tails, including Gaussian innovations, confine randomness to the cone's largest linear subspace. For fractional filters with convergent normalized cumulative coefficients, the leading stochastic directions obey the same restriction, even with bounded innovations. For real-line quantiles, variation under unbounded lower tails and leading fractional accumulation can occur only through location shifts. For cone-valued processes, partial sums of centred stationary increments remain bounded in mean square when evaluated by any linear functional that is nonnegative on the cone, in contrast to the growing variance of a random walk. We derive an exact slope criterion for locally absolutely continuous quantiles and construct nondegenerate additive models with bounded innovations for quantiles, densities, and covariance matrices. These findings clarify the scope of ordinary additive modelling under structural constraints.

</details>

### [Exact local queries for pseudo-marginal Markov chains](https://arxiv.org/abs/2611.32955)
*Zihan Xu* · `stat.CO` · arXiv:2611.32955v1 · relevance 0.14

- **In one sentence**: The paper introduces "decision certificates" built from finite historical parameter ranges that let a pseudo-marginal Markov chain with Gaussian graph priors answer prespecified local queries exactly, with work bounds and experiments on path and grid graphs.
- **In plain words**: Some statistical sampling methods update a model one piece at a time, but each update can depend on distant earlier updates, which makes it costly to get one local answer. This paper proposes a way to settle each update early, using stored records of past parameter ranges, so that only the needed parts of the chain are computed. The authors report that, under shared random inputs and exact arithmetic, the method recovers the same reference results as the full computation, and that it is faster than the alternatives for sparse queries (few requested answers) but slower than a parallel method when all answers are requested.
- **Why it matters**: The work targets a practical cost problem in Bayesian computation for large models, with applications to tomography imaging and Gaussian process classification. The text reports speed comparisons and two applications, but the evidence is from controlled experiments and specific examples, so its wider usefulness is not established from this text alone.
- **Background needed**: - Markov chain: a sequence of random states where each new state depends only on the previous one; used to sample from complicated probability distributions.
- Pseudo-marginal method: a sampling approach that replaces an exact likelihood (how well a model fits data) with a random estimate of it, while still targeting the right distribution.
- Gaussian graph prior: a probability model over parameters attached to the nodes of a network or grid, where neighbouring nodes are linked.
- Auxiliary variables: extra hidden random quantities added to make sampling easier.
- Local query: asking for the value at one node or a small set of nodes without computing the whole chain.
- Positron emission tomography (PET): an imaging technique that reconstructs internal tissue activity from detected radiation.
- Gaussian process classification: a method that predicts categories using a smooth random function as a prior; the Landmine dataset is a standard example.
- Picard iteration: a repeated-update scheme for solving equations, used here as a comparison method. · level: research-level

<details><summary>Original abstract</summary>

Local queries of a Markov chain can depend on past updates outside the queried components. For pseudo-marginal chains with Gaussian graph priors, we construct decision certificates from finite historical parameter ranges to settle updates before all neighbouring records are resolved. Under shared random inputs and exact arithmetic, the executor recovers the reference parameters, auxiliary variables and likelihood estimates for any prespecified finite query sequence. We bound conditional expected work, including likelihood evaluation, historical range construction and execution management. On specified path and grid families, we fix per-node history lengths and all other parameters in the work bounds. As graph size grows, expected incremental work stays bounded for certificate execution and grows linearly for the specified cached pointwise evaluator answering the same query. In controlled experiments, certificate execution is faster than pointwise and parallel Picard execution for sparse queries, whereas Picard is faster than certificate execution for full queries. We apply the method to positron emission tomography and Gaussian process classification of Landmine data. For a fixed numerical tomography posterior, certificate execution completes all queries of regional mean distribution volume within budget, while full execution completes none from the same initial cache. In Landmine, posterior summaries of the difference in log length scales between two sites agree across pseudo-marginal and ancillary augmentation samplers within estimated Monte Carlo uncertainty. Certificate execution resolves almost every scheduled update over the full query sequence.

</details>

## AI industry news

### [Where scientists draw the line on AI agents](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents)
** · `huggingface.co` · Hugging Face - Blog · relevance 0.13

- **In one sentence**: A news article titled "Where scientists draw the line on AI agents," but the body text is missing, so its actual content and claims cannot be confirmed.
- **In plain words**: The article appears to be about how researchers decide what counts as an AI agent, meaning software that takes actions on its own rather than only answering questions. The text provided is empty, so I cannot say what specific views, findings, or events it reports.
- **Why it matters**: Debates over where AI agents begin and end matter for safety rules, product claims, and accountability, but I cannot tell from the title alone what this article argues. Treat this as unverified until the full text is available.
- **Background needed**: - AI agent: an AI system that can plan and carry out multi-step tasks, such as browsing websites or running code, with limited human input.
- Definitions matter: "agent" is used loosely in industry, so researchers often debate which systems qualify and what level of autonomy counts.
- Title only: this brief is based solely on the headline because no article text was supplied. · level: introductory

<details><summary>Original abstract</summary>



</details>

### [Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.11

- **In one sentence**: Anthropic CEO Dario Amodei rejects rivals' claims that he favors giving up human agency to AI, as leading AI firms increasingly automate their own research and model development.
- **In plain words**: The article reports on a public dispute in the AI industry. Anthropic's chief executive, Dario Amodei, has called accusations that he wants to hand control to machines "absurd." The text is a short news summary and gives only his response and the broader context, not the full arguments on either side.
- **Why it matters**: The debate concerns how much people should keep control over AI systems that are increasingly used to build other AI systems. The text is too brief to say how serious the criticism is or what specific actions are involved, so its wider significance is unclear.
- **Background needed**: - Anthropic is an AI company that develops large language models, the systems behind chatbots like Claude.
- "Human agency" or "human control" here means people's ability to make and override key decisions about AI.
- "Automating research and model development" means AI systems are being used to help design, test, and improve other AI models, with less direct human work.
- The article names rivals' accusations but does not identify who made them or give their exact claims.
- Public statements by company leaders are not independent evidence of how AI is actually governed. · level: introductory

<details><summary>Original abstract</summary>

Anthropic CEO Dario Amodei pushes back against rivals’ accusations that he favors surrendering human agency to AI, even as leading AI companies increasingly automate their own research and model development.

</details>

### [An Indic Voice Agent with CUGA](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga)
** · `huggingface.co` · Hugging Face - Blog · relevance 0.10

- **In one sentence**: A news item titled "An Indic Voice Agent with CUGA" that, as provided, has no body text, so its content, results, and claims cannot be verified.
- **In plain words**: The item appears to be about a voice-based AI assistant built for Indian languages, using a system called CUGA. The text itself is missing, so I cannot say what was built, how well it works, or what was found. Only the title is available.
- **Why it matters**: Voice assistants that work in many Indian languages could matter for people who do not use English online, but the text provided does not show whether this work does that. Treat this as unverified until the full article is read.
- **Background needed**: - "Voice agent": an AI program that listens to speech, works out what is wanted, and replies by voice or takes actions.
- "Indic": refers to languages of the Indian subcontinent, such as Hindi, Bengali, Tamil and others.
- "CUGA": the name given in the title; the text does not explain what it is. Assume it is a specific software system unless the full article says otherwise.
- Speech assistants usually combine speech recognition, language understanding, and speech output. · level: intermediate

<details><summary>Original abstract</summary>



</details>

### [Want to buy your kid an AI toy this Christmas? Not in New York](https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.09

- **In one sentence**: A news report says New York has banned AI chatbot toys for five years, citing new Common Sense Media research that describes safety failures such as exposure to inappropriate content and risks to emotional development.
- **In plain words**: New York has put a five-year ban on toys that use AI chatbots, meaning toys that hold conversations like a chatbot. The article says new research from Common Sense Media, a US children's media watchdog group, found serious safety problems with these toys, including children being exposed to inappropriate content and possible harm to emotional development.
- **Why it matters**: Parents buying holiday gifts and regulators deciding what children's products are allowed may both care about this. The text is short and does not give the study's methods, sample size, or specific findings, so it is hard to judge how strong the evidence is.
- **Background needed**: - AI chatbot: a program that generates conversational replies to typed or spoken words.
- Common Sense Media: a US nonprofit that reviews media and technology for children and families.
- Emotional development: how children learn to understand and manage feelings and relationships.
- The article is brief; it gives no details of the ban's legal basis, the study's design, or the companies involved. · level: introductory

<details><summary>Original abstract</summary>

New York has banned AI chatbot toys for five years as new research from Common Sense Media reveals troubling safety failures, including exposure to inappropriate content and risks to emotional development.

</details>

### [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)
** · `openai.com` · OpenAI News · relevance 0.09

- **In one sentence**: A news piece, titled "How iFood scales coding agents across 15,000 repositories," that appears to describe how the Brazilian food-delivery company iFood runs AI coding agents across a very large set of code repositories, but the article text itself is unavailable.
- **In plain words**: This item is about how a large food-delivery company, iFood, uses AI software that writes or changes computer code, spread across about 15,000 code projects. The text of the article was not provided, so I cannot say what problems were encountered or what results were reported. The title alone suggests a description of how the approach was expanded to that scale.
- **Why it matters**: Companies running AI coding tools across thousands of projects is a practical question for software teams, since it touches on quality control, cost, and how much human review is needed. Beyond the title, I cannot confirm any specific outcomes, so treat this as a pointer to a topic rather than evidence of results.
- **Background needed**: - Coding agent: an AI program that can read, edit, and test software code with some autonomy, rather than only suggesting single lines.
- Repository (repo): a stored project of source code, usually tracked with version-control software such as Git.
- Scaling: making a tool work reliably across many teams or projects, not just one trial.
- iFood: a large online food-delivery platform based in Brazil.
- Note: the article body was empty, so this brief relies only on the title. · level: introductory

<details><summary>Original abstract</summary>



</details>

## Model architectures and training

### [Eliciting the Recall Capacity of Linear Attention](https://arxiv.org/abs/2611.32969)
*Johan Lindqvist, Antonio Orvieto* · `cs.LG` · arXiv:2611.32969v1 · relevance 0.32

- **In one sentence**: The paper shows that linear-attention language models have substantial but underused associative-recall capacity, and that adding recall-focused training signals (in-context sentence repetition and context-sensitive loss reweighting) narrows their gap to softmax attention without changing architecture or token budget.
- **In plain words**: Language models often read text by holding it in a memory, and the usual transformer design (softmax attention) is good at looking things up in that memory. Faster "linear" versions of these models are known to be worse at recalling specific facts from earlier in a text. This paper finds that the weakness is partly about training: the linear models can in principle store thousands of associations, but standard training does not teach them to copy from context, and two training changes help them do so.
- **Why it matters**: It suggests the recall gap between fast linear models and standard transformers may be narrowed by how they are trained rather than only by redesigning the architecture. The text does not show how far these gains carry over to larger real-world models, so that remains open.
- **Background needed**: - Associative recall: given a key seen earlier (like a name), retrieving the value attached to it (like a phone number).
- Softmax attention: the standard transformer mechanism that lets a model look back at every earlier token; accurate but costly for long texts.
- Linear attention: a cheaper variant that compresses past text into a fixed-size memory ("state"), so its recall is limited by how big that state is.
- State size: how much information the compressed memory can hold; the paper relates it to how many items can be recalled.
- Synthetic recall tasks: controlled test puzzles that measure recall without the noise of natural language.
- Loss reweighting: changing how strongly each training prediction counts, here to emphasize recall-relevant tokens.
- Token budget: the total amount of training text, held fixed in the comparisons. · level: research-level
- Matched keywords: attention, linear attention, architecture

<details><summary>Original abstract</summary>

Linear attention models exhibit a disproportionate deficit relative to softmax attention in associative recall (AR) in language modeling. We investigate this gap through natural language evaluations, synthetic recall tasks, and targeted training interventions. Using a synthetic setting, we quantify the role of state-size in how many items can be recalled from memory and find a similar empirical scaling across the tested linear-attention architectures. Testing this relationship reveals that even a single layer at scale can learn to retrieve thousands of associations across long distances. Yet, standard language model training does not reliably teach a linear model to copy from context, whereas a comparable softmax model learns to do so. Considering this, we strengthen recall supervision during training through in-context sentence repetition and context-sensitive loss reweighting. Both methods improve recall-intensive benchmark performance and narrow the long-distance AR gap to the softmax baseline without changing the architecture, token budget, or number of optimization steps, at a slight cost to general language modeling. These targeted changes to training can thus elicit substantial but underutilized retrieval capacity in linear-attention models. These findings suggest that, although linear-attention architectures have substantial capacity for recall, their inductive biases and the demands of language model training make it difficult to develop this capability without dedicated incentives.

</details>

### [Structure-Aware Transformers for Hierarchical Authorization in Personal AI Agents](https://arxiv.org/abs/2611.32018)
*Dongyu Cui, Jie Ding, Xuan Bi* · `cs.LG` · arXiv:2611.32018v1 · relevance 0.31

- **In one sentence**: PATH is a transformer-based architecture that predicts a user's allow/deny decisions on hierarchically organized permission requests from personal AI agents, using hierarchy-aware attention masks, a parent-gated probability formulation, and hierarchy-level embeddings, with finite-sample risk bounds and convergence conditions.
- **In plain words**: Personal AI agents that act for a user often ask for many permissions, and reviewing each one by hand is tedious while approving them all is risky. This paper proposes a model that learns a user's likely yes-or-no answers to these requests, so that routine ones can be handled with less manual review. The authors report strong prediction performance on simulated data, AI-generated user profiles, and real user authorization data, and say the model never produced predictions that contradict the permission hierarchy.
- **Background needed**: - Personal AI agent: software that carries out multi-step tasks for a user, such as accessing accounts or files.
- Permission request: the agent asking for access to a specific resource or action.
- Hierarchical permissions: requests organized in parent-child groups, where a general category contains more specific ones.
- Transformer: a neural network design that uses attention to weigh relationships among input items.
- Attention mask: a rule that restricts which items can attend to which, here enforcing the hierarchy.
- Parent-gated probability: a formulation where a child permission's probability depends on its parent's, so predictions stay consistent with the hierarchy.
- Finite-sample risk bounds: guarantees on expected prediction error for a given amount of data.
- Sparse observations: few recorded user decisions relative to the number of possible requests. · level: research-level
- Matched keywords: transformer, attention, architecture

<details><summary>Original abstract</summary>

Personal AI agents can carry out complex, multi-step tasks on users' behalf, but doing so often involves numerous permission requests. Manually reviewing each request is time-consuming, while indiscriminate approval poses privacy and security risks. Predicting users' authorization preferences offers a way to reduce this burden while preserving user control. However, authorization prediction is challenging because permission requests are often hierarchical and observed user decisions are sparse and potentially correlated. To address these challenges, We propose the Parent-gated Authorization Transformer for Hierarchies (PATH) to predict users' authorization preferences for personal AI agents. PATH is a novel neural network architecture that combines hierarchy-aware attention masks with a parent-gated probability formulation to ensure hierarchy-consistent predictions. Hierarchy-level embeddings further support learning from sparse observations and patterns shared within each authorization level. We establish finite-sample risk bounds and provide sufficient conditions for consistent authorization probability estimation and algorithmic convergence. Experiments on simulated data, AI-generated user profiles, and real user authorization data demonstrate strong predictive performance with zero hierarchy violations.

</details>

## Machine learning theory

### [Instance-Dependent Bandit Convex Optimization in One Dimension](https://arxiv.org/abs/2611.31608)
*Felix Breuer, Alireza Bakhtiari, Kevin Jamieson* · `stat.ML` · arXiv:2611.31608v1 · relevance 0.32

- **In one sentence**: The paper studies instance-dependent sample complexity for one-dimensional stochastic bandit convex optimization in the fixed-confidence setting, proving a matching-up-to-logs instance-dependent rate for minimizer localization but showing no comparable improvement for simple regret.
- **In plain words**: The paper looks at a learning problem where an algorithm tries to find the lowest point of a smooth, bowl-shaped function on a line, but can only learn about it by taking noisy measurements at chosen points. It asks how many measurements are needed, and how that depends on how the particular function looks. The authors find that locating the lowest point can be done faster on easier functions, while merely finding a point whose value is close to the lowest value cannot be sped up in the same way.
- **Why it matters**: The result separates two goals that might seem similar, locating the minimizer versus finding a near-optimal value, and shows they have different statistical costs. The text does not say how far the findings extend beyond one dimension, so their wider relevance is uncertain.
- **Background needed**: - Stochastic bandit: a learner picks actions and receives noisy rewards or losses, learning only from the outcomes it observes.
- Convex function: a bowl-shaped function with a single lowest point (the minimizer).
- Fixed-confidence setting: the algorithm must output an answer that is correct with high probability, and the aim is to minimize the number of samples used.
- Sample complexity: the number of measurements needed to reach the goal.
- Instance-dependent versus minimax: instance-dependent bounds depend on the specific function, while minimax bounds are the worst case over all functions in a class.
- Sublevel set: the set of points where the function is below a given threshold.
- Simple regret: the gap between the value at the chosen point and the best possible value. · level: research-level
- Matched keywords: sample complexity, minimax

<details><summary>Original abstract</summary>

We study the instance-dependent sample complexity of one-dimensional stochastic bandit convex optimization in the fixed-confidence setting. First, we consider minimizer localization, where the learner seeks to identify a point within distance $\varepsilon$ of the unique minimizer. We introduce a new instance-dependent quantity $\Delta_\varepsilon(f)$, corresponding to the threshold for which the sublevel set of $f-\min f$ has length $2\varepsilon$. We prove a lower bound of order $\Delta_\varepsilon(f)^{-2}$ and give a bisection-style algorithm that matches this rate up to logarithmic factors. We then revisit the simple-regret setting, where the goal is to identify an $\varepsilon$-optimal point. Surprisingly, no comparable instance-dependent improvement is possible: every correct algorithm has sample complexity of order $\varepsilon^{-2}$ on every instance, matching the minimax rate up to constants. Together, these results separate the statistical complexity of minimizer localization from that of simple-regret optimization in one-dimensional convex bandits.

</details>

### [PAC-style Bounds on the Conditional Validity of Conformal Predictors](https://arxiv.org/abs/2611.33023)
*Nicolo Colombo* · `cs.LG` · arXiv:2611.33023v1 · relevance 0.25

- **In one sentence**: The paper derives PAC-style probabilistic lower bounds on the input-conditional coverage of conformal predictors, using Markov and Cantelli inequalities, and proposes a data-estimable Cantelli bound based on the variance of conditional coverage.
- **In plain words**: Conformal prediction methods output a set of possible answers rather than a single guess, and they are designed so that the set contains the true answer about as often as promised. That promise holds on average across all inputs, but it can be off for particular kinds of inputs. This paper gives guaranteed lower limits on how often the set is right for a given input, using only a finite amount of calibration data and no assumptions about how the data are distributed.
- **Why it matters**: Users often need reliability for specific cases, not just on average, so a checkable measure of local reliability matters for safety-sensitive uses. The authors suggest the variance of conditional coverage as a practical signal of how trustworthy a predictor is for different inputs; the text does not show how well this works in practice.
- **Background needed**: - Prediction set: a range or list of candidate outputs instead of one value.
- Coverage: the fraction of cases where the true answer falls inside the set; the target here is 1 minus alpha (for example, 90%).
- Marginal vs. conditional validity: marginal means correct on average over all inputs; conditional means correct for each specific input or group.
- Calibration data: a held-out sample used to set the size of the prediction sets.
- PAC-style bound: a guarantee that holds with high probability over the random calibration sample, not just in expectation.
- Markov and Cantelli inequalities: classic probability tools that bound how far a random quantity can stray from its average, using only its mean (and variance for Cantelli).
- Hoeffding argument: a standard concentration result that lets a quantity be estimated from samples with a known confidence level. · level: research-level
- Matched keywords: conformal prediction

<details><summary>Original abstract</summary>

Conformal prediction sets are guaranteed to be marginally valid over the attribute space, but local coverage can diverge from the user-defined target $1-\alpha$. Constructing conditionally valid prediction sets with finite calibration data is impossible for a general data-generating distribution. We derive PAC-type probabilistic lower bounds on the input-conditional coverage of any conformal predictor, without assumptions on the data distribution. They are based on the Markov and Cantelli inequalities and adapt to both calibration-marginal and calibration-conditional setups. A tighter, model-dependent Cantelli bound depends on the variance of the conditional coverage and is estimable from data using a fully non-asymptotic Hoeffding argument. The results suggest conditional-coverage variance as a scalable and theoretically motivated empirical measure of conditional validity.

</details>

## Large language models

### [Implementation of Machine Translation for the Uzbek Language Based on Transformer Models](https://arxiv.org/abs/2611.32359)
*Mukhammadjon Musaev, Mannon Ochilov* · `cs.CL` · arXiv:2611.32359v1 · relevance 0.23

- **In one sentence**: The paper fine-tunes transformer models T5 and mT5 for Uzbek-English machine translation, using a parallel corpus of about 3 million sentence pairs built through data collection, preprocessing and augmentation, and evaluates with BLEU.
- **In plain words**: This paper is about building a computer program that translates between Uzbek, a language with relatively little digital text, and English. The authors gathered and cleaned a large collection of matching Uzbek and English sentences, roughly 3 million pairs, and used it to adapt two existing AI language models. They report that their approach beats older translation methods, measured with a standard similarity score.
- **Why it matters**: Low-resource languages like Uzbek are often poorly served by translation tools, so work that makes them usable online has practical value. The summary gives no detailed comparison numbers, so the size of the improvement cannot be judged from this text alone.
- **Background needed**: - Machine translation: software that converts text from one language to another.
- Transformer models: a widely used neural network design behind modern language AI; T5 and mT5 are published examples that can be trained on many languages.
- Fine-tuning: further training a pre-built model on a specific task or dataset.
- Parallel corpus: a collection of texts paired with their translations, used as training examples.
- BLEU score: an automatic metric that compares machine translations with human reference translations; higher is better, but it is an imperfect proxy for quality.
- Low-resource language: a language with little available digital text for training AI systems. · level: intermediate

<details><summary>Original abstract</summary>

This research focuses on building a machine translation system for the Uzbek language using transformer models such as T5 and mT5. Because of the limited data and the complexity of the Uzbek language, we collect, preprocess and augment data to create a strong Uzbek-English parallel corpus of about 3 million sentence pairs. The models are fine-tuned for optimal translation performance, and we use the BLEU score to evaluate the results. This study shows that our approach significantly improves upon older methods and helps promote the Uzbek language in the digital world.

</details>

### [Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models](https://arxiv.org/abs/2611.31821)
*Keyu He, Michael Li, Jiarui Liu et al.* · `cs.CL` · arXiv:2611.31821v1 · relevance 0.11

- **In one sentence**: The paper tests whether training small Qwen3 language models with supervised fine-tuning and reinforcement learning on objective game outcomes from three multi-player social games improves their social play, with some held-out-game transfer.
- **In plain words**: Researchers want AI chatbots that can work with others through conversation, but grading that behavior usually requires other AI models acting as judges, which is costly and easy to game. This paper uses multi-player social games instead, where the game's rules decide who wins, so the win itself serves as the training signal. The reported results: a small model's win rate against a much stronger opponent rose from 33% to 81% on the three games used for training, and from 39% to 54% on three games it was not trained on.
- **Why it matters**: It offers a way to train social skills without relying on AI judges, which the text describes as expensive, noisy, and open to reward hacking. Whether the gains generalize beyond these games and to real-world social tasks is not shown in the text, so the broader claim should be treated as preliminary.
- **Background needed**: - Large language model (LLM): an AI system trained on large amounts of text to generate and understand language.
- Supervised fine-tuning (SFT): further training a model on examples of good behavior.
- Reinforcement learning with verifiable rewards (RLVR): training by trial and error, where the reward comes from a checkable rule-based result, such as winning a game, rather than a judgment.
- Reward hacking: when a model finds shortcuts that score well on the reward without doing the intended thing.
- Win rate: the share of games won against an opponent.
- Held-out games: games deliberately withheld from training to test whether skills transfer.
- Qwen3 and Gemma-3-27B: specific open-weight language models; the numbers refer to parameter counts (for example, 4B means about 4 billion parameters).
- "pp" means percentage points. · level: intermediate

<details><summary>Original abstract</summary>

The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acquire through supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). Results show that against a much stronger Gemma-3-27B model, SFT and RLVR raise the win rate of Qwen3-4B from 33% to 81% on the three trained games, and from 39% to 54% on three additional held-out games. In contrast, in-context strategies such as prompting improve the win rate of Qwen3-4B by only about 6 pp across the same games we train and evaluate on. Furthermore, we show that the gains from SFT and RLVR hold across the model sizes 1.7B, 4B, and 32B. Qualitative analyses of agent behavior show signs of stronger social intelligence; for example, trained agents tend to share information more openly, check each other's claims against public evidence, and coordinate their votes. More broadly, our results demonstrate that training LLMs on verifiable outcomes in social games can cultivate generalizable social behaviors, which offers a scalable path for building socially intelligent agents.

</details>

## Computer vision

### [Visual-State Graph Memory for Streaming Video Understanding](https://arxiv.org/abs/2611.32369)
*Ailar Mahdizadeh, Pritam Sarkar, Xiangteng He et al.* · `cs.CV` · arXiv:2611.32369v1 · relevance 0.14

- **In one sentence**: Proposes Visual-State Graph (VSG), a training-free memory for streaming video that stores objects, their relations, and a timestamped event log, retrieved alongside recent frames under a fixed input budget.
- **In plain words**: Video models often need to answer questions about something that happened long before the current moment, but only a short window of recent frames is kept. This paper builds a compact running memory of what is in the video: each object is kept as one entry with a dated history of how it changed, plus a log of events. When a question comes in, the relevant parts of this memory are pulled out and given to the model together with recent frames.
- **Why it matters**: Reasoning about the past is a practical limit for systems that watch live video, such as monitoring or assistive tools, where storing every frame is not feasible. The text reports gains on four benchmarks with seven open-source vision-language models (7B to 32B parameters) under matched input budgets, but the summary gives no further detail on size of gains, so its broader significance is unclear.
- **Background needed**: - Streaming video: video that arrives continuously, so the system sees each frame once and cannot look ahead.
- Vision-language model: an AI model that takes images or video plus text and answers questions about them.
- Scene graph: a structured description of objects in a scene and how they relate (for example, "cup on table").
- Training-free: the method is added on top of existing models without retraining them.
- Input budget: a fixed limit on how much information (frames, text) the model can receive at once. · level: research-level

<details><summary>Original abstract</summary>

In streaming video understanding, the evidence needed to answer a question may have already left the recent-frame window. Keeping all frames does not scale with video length, while dropping older frames limits the model's ability to reason about the past. We propose Visual-State Graph (VSG), a training-free memory that stores the state of a stream rather than the raw sequence of frames. VSG represents the stream as a graph of objects and their relations, together with a log of events; similar to a dynamically evolving scene graph. An object observed repeatedly is represented by one persistent node, with a timestamped history of how its state changes. To determine whether a newly mentioned object already exists in the graph, we compare the relations it takes part in with those of stored objects. We build this memory as the video arrives, before the questions are known. When a question arrives, we retrieve relevant objects and events alongside recent frames under a fixed input budget. Our evaluation spans four streaming-video benchmarks and seven open-source vision-language models ranging from 7B to 32B parameters. Under matched input budgets, VSG improves reasoning about the past while preserving real-time understanding.

</details>

### [DOPER: Deep Object Pose Estimation Revisited](https://arxiv.org/abs/2611.32846)
*Hugo Hadfield, Alperen Degirmenci, Jonathan Tremblay* · `cs.CV` · arXiv:2611.32846v1 · relevance 0.14

- **In one sentence**: DOPER is an RGB-only framework that shares one visual backbone across detection, segmentation, and keypoint prediction to estimate the 6D pose of known objects via Perspective-n-Point, trained from synthetic data and adapted to real images with partial supervision and multi-view geometric constraints.
- **In plain words**: This paper is about working out where a known object is and how it is turned in a camera image, using only ordinary color pictures and no depth sensor. The method first learns from computer-generated images, then adapts to real photos, and it refines a rough 3D model of the object as it goes. The authors report that it reaches top detection scores on several public benchmark datasets and runs at about 35 times per second per object.
- **Why it matters**: Reliable pose estimation from ordinary cameras matters for robots that pick up objects and for spacecraft or similar systems that need to know an object's orientation. The text reports benchmark results and speed, but it does not show how the system performs in deployed robots or spacecraft, so its practical reach is unclear.
- **Background needed**: - Pose estimation: finding an object's position and rotation (6D: three for location, three for orientation) relative to the camera.
- Keypoints: specific points on an object, such as corners, whose image locations are predicted and then matched to the 3D model.
- Perspective-n-Point (PnP): a standard geometric calculation that gives the object's pose from matched 2D image points and known 3D points.
- Synthetic training: learning from computer-rendered images instead of real photos, which then need adapting to real conditions.
- CAD model: a digital 3D drawing of an object; "underspecified" means it lacks some detail.
- Multi-view and calibrated cameras: several cameras with known positions, which constrain 3D geometry.
- Average precision (AP): a standard score for how well detections match the true objects.
- Benchmarks named: SPEED+ (spacecraft images), SHIRT, HANDAL, HOPEv2, HOT3D, and T-LESS (object datasets). · level: research-level

<details><summary>Original abstract</summary>

We present DOPER, an RGB pose estimation framework that shares a visual backbone across object detection, segmentation, and keypoint prediction to recover the 6D pose of known objects through Perspective-n-Point. Starting from synthetic training, DOPER adapts to real observations using partial supervision while retaining synthetic keypoint labels. Calibrated multi-view observations provide geometric constraints for keypoint supervision. During inference, optional heatmap refinement fits a rigid pose directly to the predicted keypoint distributions, resolving ambiguous correspondences without depth input or a learned pose refiner. Starting from underspecified CAD models, DOPER progressively refines the object representation and pose estimator. Results on SPEED+ and SHIRT further demonstrate effective adaptation to illumination changes and accurate temporal pose estimation. Across the evaluated single-view and multi-view configurations, DOPER achieves state-of-the-art detection AP results on HANDAL, HOPEv2, HOT3D, and T-LESS while using only RGB and running in real time (35 Hz per object model on one GB300). These results demonstrate the effectiveness of jointly learning detection and pose keypoints, with real observations and geometric constraints.

</details>

## Reinforcement learning

### [To Critic Or Not To Critic](https://arxiv.org/abs/2611.32013)
*Jason Wei, George Pu, Jingxuan Fan et al.* · `cs.LG` · arXiv:2611.32013v1 · relevance 0.26

- **In one sentence**: An empirical study of when a learned critic (PPO) beats critic-free group-based advantage estimation (GRPO) in RL, framed as a bias-variance tradeoff in gradient direction across batch sizes, tasks, and horizons.
- **In plain words**: Training AI systems with reinforcement learning often requires a "critic," a separate model that estimates how good each situation is. This paper asks whether that extra model is worth its cost, comparing a critic-based method (PPO) with a method that skips the critic (GRPO). The authors report that the answer depends on factors such as batch size, task length, and complexity, rather than one method always winning.
- **Why it matters**: Choosing between these methods affects how expensive it is to train large language models on long, multi-step tasks. The text reports results across more than 1,200 training runs, including 96 with LLMs, but I have not checked the details behind those numbers.
- **Background needed**: - Reinforcement learning (RL): training by trial and error, using rewards as feedback.
- Policy gradient: adjusting a model's behavior in the direction that earns more reward.
- Critic / value function: a model that predicts expected future reward, used to judge how good an action was.
- Variance vs. bias: noisy estimates (high variance) versus systematically off estimates (bias). A critic can reduce noise but can add bias if its predictions are wrong.
- Bootstrapping: updating estimates using other estimates, which can propagate errors.
- PPO (Proximal Policy Optimization): a common RL method that uses a critic.
- GRPO (Group Relative Policy Optimization): a method that drops the critic and compares several sampled answers to each other instead.
- Batch size: how many samples are used per update; larger batches give less noisy gradients. · level: research-level
- Matched keywords: reinforcement learning, policy gradient

<details><summary>Original abstract</summary>

As large language models tackle longer and more complex tasks, understanding when a critic improves the efficiency of reinforcement learning (RL) becomes increasingly important. Proximal Policy Optimization (PPO) trains a critic to reduce variance and provide fine-grained credit assignment, while Group Relative Policy Optimization (GRPO) drops the critic and avoids the bias of bootstrapping from the critic's value estimates. Although recent critic-based methods have reported strong performance relative to GRPO, it remains unclear when each approach is preferable. We argue that there is no universal answer; instead, the choice depends on several interacting factors, including batch size, critic reliance, and task complexity. We study the bias-variance tradeoff in terms of gradient direction, measuring how closely each method's gradient estimates align with the true policy gradient as batch size grows. Under a shared actor objective, we compare GRPO with PPO in control tasks, short-horizon math, and long-horizon terminal agents. Across more than 1,200 training runs, including 96 with LLMs, we find that PPO generally leads at small batch sizes, while GRPO often overtakes heavily bootstrapped PPO and reaches parity with lightly bootstrapped PPO at larger batches. At longer horizons and in more complex domains, GRPO needs larger batches to catch up to PPO's performance. Accounting for training compute, critics pay off at small budgets, but their returns diminish at larger budgets.

</details>

### [Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884)
*Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang et al.* · `cs.AI` · arXiv:2611.32884v1 · relevance 0.21

- **In one sentence**: The paper proposes RLVB, a reinforcement learning reward that uses the simulator's exact posterior over answers to teach vision-language agents when to stop gathering evidence and commit, and introduces the Pro Worlds visual-puzzle benchmark.
- **In plain words**: AI agents solving long tasks often give an answer too early, before they have gathered enough evidence. The authors train agents with a reward that checks, during training only, how much evidence the agent actually has, so it can reward continuing to look when several answers remain possible and reward committing once the evidence is enough. Across three vision-language models and three benchmarks, the trained agents answered with sufficient evidence far more often than the base model.
- **Why it matters**: Premature guessing is a practical failure in agents that act over many steps, and the paper shows that a reward based on exact evidence, rather than only the final answer, can change when the agent commits. The text reports gains against standard outcome-reward training and an LLM-judge baseline, but the results come from the authors' own benchmarks and setup, so how far they carry to other tasks is unclear.
- **Background needed**: - Reinforcement learning: training by trial and reward, where an agent learns which actions lead to higher scores.
- Outcome reward: a score given only at the end of an episode, based on whether the final answer is correct.
- Process reward: a score given along the way, here from an LLM judge that grades intermediate steps.
- Posterior: the probability of each possible answer given the evidence so far; the simulator can compute it exactly during training.
- Vision-language model: an AI model that takes both images and text as input.
- GRPO and PPO: two common reinforcement learning algorithms used to fine-tune language models.
- Episode: one complete attempt at a task, from start to final answer.
- Out-of-distribution benchmark: a test set not seen during training, used to check generalization. · level: research-level
- Matched keywords: reinforcement learning, reward model

<details><summary>Original abstract</summary>

AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scores only the final answer, so it cannot teach the agent when to commit, because a lucky guess receives the same reward as an answer backed by evidence. During training, however, the simulator can compute the exact posterior over the answer at every step and tell whether the evidence is already enough. We propose Reinforcement Learning with Verifiable Beliefs (RLVB), which rewards the agent for taking further steps while this posterior still allows several answers and for committing once the evidence is sufficient. The reward needs no judge, critic or reward model, and it never reads the belief line the agent writes before each action. We also introduce Pro Worlds, a benchmark of visual puzzles where the agent views a large world through a small window. We evaluate three vision-language models on three benchmarks, two of which are never seen in training. RLVB improves the base model in all nine settings, by 17.1% on average. Under the outcome reward, GRPO and PPO fall below the base model on average. RLVB also outperforms PPO with a process reward from an LLM judge by 9.3% on average while using 1.6 times fewer GPU-hours. The trained agent answers with sufficient evidence in 51%, 12% and 74% of the episodes on the three benchmarks, against 8%, 0.4% and 36% for the base model. Its accuracy gain therefore comes from answering more often at high levels of evidence. The belief line shows how the agent reaches this evidence: it acts on its own belief. It commits at only 0.1 to 2.2% of the turns at which the evidence is insufficient and its line still names several answers, against 3 to 68% for the base model.

</details>

## AI safety and alignment

### [SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](https://arxiv.org/abs/2611.33030)
*Shivank Rajput, Himanshu Singh, A. V. Subramanyam* · `cs.CL` · arXiv:2611.33030v1 · relevance 0.22

- **In one sentence**: SALSA trains a generative model on optimization-derived jailbreak suffixes so that new adversarial suffixes can be sampled quickly, reporting comparable attack success on open-source models and higher transfer success on GPT-3.5-Turbo and GPT-4o than the strongest baseline at equal budget.
- **In plain words**: Chatbots are trained to refuse harmful requests, but attackers can add a string of odd words to a prompt that gets the model to ignore that training. This paper proposes SALSA, which learns the pattern of those attack strings from examples and then generates new ones on demand instead of searching for each one from scratch. The authors report that this is much faster and still works often, including against some commercial chatbots.
- **Why it matters**: Making attack generation cheap matters for safety testing, since it lets red-teamers probe models at scale, and it also raises the stakes for defenses. The text reports results only from the authors, and the comparisons depend on their chosen baselines and budgets, so the findings should be treated as preliminary until independently checked.
- **Background needed**: - LLM (large language model): an AI system that generates text, such as a chatbot.
- Safety alignment: training that makes a model refuse harmful requests.
- Jailbreak: a prompt crafted to make a model bypass its safety training.
- Adversarial suffix: a string of text appended to a prompt to trigger the bypass.
- GCG-style attack: an attack that searches for a suffix by repeated automated optimization, which is slow at test time.
- Attack success rate (ASR): the share of attack attempts that get a harmful response.
- Transfer / black-box: a suffix found on one model is tried on a different model whose internals the attacker cannot see.
- Sampling budget: the number of candidate suffixes an attacker is allowed to try. · level: intermediate
- Matched keywords: alignment, jailbreak

<details><summary>Original abstract</summary>

Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are expensive at inference time, and suffer from poor transfer. We present, SALSA, a generative framework that learns a distribution over jailbreak suffixes from optimization-derived attack corpora. Once trained, the model supports efficient sampling-based attacks. On open-source targets, it achieves attack success rates comparable to state-of-the-art optimization baselines, while reducing generation time from 3.46s to 0.04s per prompt. In black-box transfer, it remains highly effective against proprietary systems, including 99% ASR on GPT-3.5-Turbo, and reaches 45% ASR on the substantially harder GPT-4o, more than doubling the strongest baseline at an equal sampling budget. We further offer an intuition for why generative sampling can preserve high attack success, when the learned suffix distribution is close to the distribution of optimization outputs. Overall, our results show that learning adversarial suffix distributions yields a scalable, and practically efficient foundation for continuous LLM vulnerability discovery.

</details>

### [Monitorable-by-design architectures for a post-Astra world: a compartmentalization-based approach](https://arxiv.org/abs/2611.31610)
*Jake Watts, Joel Sokol* · `cs.AI` · arXiv:2611.31610v1 · relevance 0.21

- **In one sentence**: The paper proposes modifying LLM architectures, building on methods such as GRAM, SGTM, DEMix and BTS, to compartmentalize dangerous capabilities so their use can be monitored more cheaply than reading chain-of-thought reasoning.
- **In plain words**: Today, safety teams often check how AI models reason by reading their written step-by-step notes, called chain of thought, but those notes are becoming harder to read and are often checked only occasionally to save money. This paper proposes building AI models so that risky abilities sit in separate, identifiable parts of the model, which would be easier and cheaper to watch. The text describes several versions of this design and says it could also help remove certain abilities from a model, but it does not report experimental results.
- **Why it matters**: It addresses a concern that monitoring AI reasoning through its written text may stop working as models get more capable, so it is worth attention as a possible alternative. Whether it works in practice is not shown in the text, which only describes a proposal and its variants.
- **Background needed**: - Chain of thought: the step-by-step text a language model writes while reasoning, which overseers can read to spot problems.
- Monitorability: how easily humans or automated tools can check what an AI is doing and why.
- Compartmentalization: splitting a model's internal parts so specific abilities are confined to identifiable sections.
- Named methods (GRAM, SGTM, DEMix, BTS) are prior techniques the paper builds on; the text does not explain them, so their details are unknown here.
- "GPT-6 Astra" is named in the text as an example of a frontier model; no further claims about it are given.
- Capability removal: deliberately reducing a model's ability to do certain tasks. · level: research-level
- Matched keywords: dangerous capabilities

<details><summary>Original abstract</summary>

Frontier models like GPT-6 Astra are increasingly able to do substantial reasoning without a monitorable chain of thought, chains of thought are becoming less legible, and are often monitored asynchronously to reduce cost. With the future of chain of thought monitoring unclear, it may be necessary to design LLMs with monitorability in mind. We propose a modification to existing LLM architectures based on GRAM, SGTM, DEMix, BTS, and similar methods to compartmentalize dangerous capabilities so that their use, especially in combination with dangerous reasoning types that may indicate strategic adversarial use, can be monitored more cheaply than chain of thought in a way that might outlast monitorable chain of thought. We propose several variants of this architecture designed to balance tradeoffs and discuss other benefits, such as capability removal.

</details>

## Interpretability

### [Social Bias Neurons in Multilingual Language Models: A Mechanistic Interpretability Analysis](https://arxiv.org/abs/2611.32685)
*Lance Calvin Lim Gamboa, Yue Feng, Mark Lee* · `cs.CL` · arXiv:2611.32685v1 · relevance 0.27

- **In one sentence**: This paper applies two mechanistic interpretability methods (activation probability entropy and integrated gap gradients) to locate "social bias neurons" in three instruction-tuned multilingual language models across four languages and seven bias dimensions.
- **In plain words**: Language models trained on many languages can reproduce social stereotypes, and this paper asks where inside the model that bias is stored. The authors search for individual internal units (neurons) that respond to biased content, then switch them off to see whether the bias drops. They report that one of the two search methods works better and that the bias-linked units sit mostly in the deepest layers.
- **Why it matters**: Finding specific internal components tied to bias could make it possible to reduce bias more directly than retraining the whole model. The text does not show how well these results carry over to other models, languages, or real-world uses, so the practical impact is uncertain.
- **Background needed**: - Language model: a program trained on large amounts of text to predict and generate language.
- Neuron: a single numerical unit inside the model whose activity rises or falls with the input.
- Mechanistic interpretability: the study of which internal parts of a model do which jobs, rather than only judging its outputs.
- Activation probability entropy and integrated gap gradients: two scoring methods for ranking neurons by how strongly they relate to biased inputs (the text does not give their formulas).
- Instruction-tuned: a model further trained to follow user instructions.
- Deepest layers: the final processing stages of the network, closest to the output.
- High- vs low-resource languages: languages with much vs little text available for training. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Multilingual models exhibit social bias when processing inputs pertaining to societal stereotypes. We adapt emerging mechanistic interpretability methods to pinpoint and characterize model components that encode this bias. We conduct our analysis across three instruction-tuned models, four languages, and seven bias dimensions. Specifically, we leverage multilingual bias benchmarks in implementing two methods for identifying social bias neurons: activation probability entropy and integrated gap gradients. We find the latter method to be more effective, as the neurons it isolates (which are largely concentrated at the model's deepest layers) lead to sharper decreases in model bias when suppressed. Further analysis reveals neuron distribution patterns differ between high- and low-resourced languages, suggesting that a language's representation in pretraining data influences how its biases are represented within model internals. Our results also indicate that neurons linked to gender, nationality, and social class biases overlap the most with neurons related to other bias dimensions, pointing to the pivotal role these three dimensions play in how models learn and handle bias.

</details>

### [Capability and Interpretability of Transformers on Multi-task Recurrence](https://arxiv.org/abs/2611.31260)
*Xiamin Chen, Linyu Liu, Jiachen Hu et al.* · `cs.CL` · arXiv:2611.31260v1 · relevance 0.24

- **In one sentence**: A controlled study of how Transformers learn and execute linear recurrence rules over finite cyclic groups, covering single fixed rules, latent rule identification, and explicit rule switching with and without input masking, probed with linear probing and input patching.
- **In plain words**: This paper asks how Transformer neural networks, the kind behind many language AI systems, handle sequences that follow a repeating rule. The authors build a set of simple, fully controlled puzzles based on repeating arithmetic patterns, from following one fixed rule to working out a hidden rule from context and switching between rules. They report that switching between rules that are stated explicitly is easier for the models than inferring a hidden rule, and they examine how depth, width, and the arithmetic structure of the rule affect generalization.
- **Why it matters**: The controlled setup makes it possible to inspect what the model stores internally, which is hard to do with real language data. The text does not say how these toy findings transfer to large language models, so any link to natural language is a hypothesis rather than a result shown here.
- **Background needed**: - Transformer: the neural network architecture used in most modern language AI.
- Recurrence: a rule where each item in a sequence is computed from earlier items.
- Cyclic group: a set of numbers that wraps around, like hours on a clock, used here for arithmetic.
- Generalization: how well a model handles cases it was not trained on.
- Linear probing: training a simple readout to check whether information is stored inside the network.
- Input patching: swapping parts of the input or internal activations to see which parts affect the output.
- Curriculum training: teaching the model easier tasks first and gradually harder ones. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Transformers are widely used in various language tasks, with limited understanding of their internal mechanisms. Motivated by the recurrent structure of many linguistic rules, we study the capability and interpretability of Transformers through a controlled family of linear recurrence tasks over finite cyclic groups. These tasks range from executing a single fixed rule to identifying a latent rule from context and switching between explicitly specified rules, with and without input masking. Through extensive experiments across different configurations, we find that switching specified rules is simpler than identifying latent rules for Transformers in general. We also identify how several key factors affect the generalization capability of Transformers, including the depth, width, and the algebraic structure of the linear recurrence. Curriculum training is extremely useful when the number of rules is large. With standard tools in mechanistic interpretability like linear probing and input patching, our study reveals how Transformers represent, identify, and execute multiple rules.

</details>

## AI for mathematics

### [Safe Autoformalization: Sufficiency and Necessity with Entailment Graphs](https://arxiv.org/abs/2611.31571)
*Umut A. Acar, Eli Goldweber* · `cs.AI` · arXiv:2611.31571v1 · relevance 0.26

- **In one sentence**: The paper proposes a graph-based method for autoformalization (turning natural-language statements into logic formulas) that uses LLM-generated candidate formulas, a solver-checked entailment order, and frontier searches to certify one-sided logical adequacy, with soundness and completeness results for the LLM oracle and Lean-checked proofs.
- **In plain words**: Turning a plain-English requirement into a precise logical formula is useful but error-prone, and language models give answers with no guarantees. This paper describes a way to organize several candidate formulas by how strong they are, so that some of them can be certified as safe to enforce (they imply the intended meaning) or safe to rely on (the intended meaning implies them). On security-related AWS properties, the authors report that their approach was safe in all 20 cases of an expert-reviewed study, while two simpler baselines were unsafe in 25% and 10% of cases.
- **Why it matters**: Formal checks of AI-written specifications matter most where a wrong translation could leave a security gap, so a method that can flag when it is unsure is of interest. The evidence is a small expert-adjudicated study and the text does not say how large or varied it was, so its broader reach is unclear.
- **Background needed**: - Autoformalization: converting a natural-language statement into a precise logical formula.
- Logical entailment: formula A entails B if whenever A holds, B must hold; a solver can check this.
- Sufficient vs. necessary: a formula sufficient for an intent implies it; a necessary one is implied by it.
- Soundness and completeness of an oracle: sound means it only approves checks that truly hold; complete means it approves all checks that truly hold.
- Lean: a proof assistant used here to machine-check the proofs.
- Baselines named: majority vote over equivalence clusters and Universal Self-Consistency (ways of picking an answer from many LLM samples). · level: research-level
- Matched keywords: Lean, autoformalization

<details><summary>Original abstract</summary>

Autoformalization translates a natural-language statement into a formula that captures its intent, which depends on the statement's context: the background that disambiguates it. LLMs make autoformalization practical, but their probabilistic output carries no formal guarantees. We propose techniques for safe autoformalization that certify one-sided logical adequacy: a formula sufficient for the intent is safe to enforce, and a formula necessary for it is safe to rely on. We use LLMs to generate candidate formulas and order them by logical strength in an Entailment Graph (EG), an ordering a solver decides. Each edge carries a residual and a co-residual, the two adjoints of the entailment order, all fixed by the candidate pool alone. In a context, two searches return the sufficient frontier, the weakest candidates that entail the statement, and the necessary frontier, the strongest candidates the statement entails; each step is one local check against an edge's residual or co-residual. The frontiers bracket the statement and yield the ambiguity residue, which holds exactly of the situations the candidates certify neither as satisfying nor as violating it; the statement is ambiguous precisely when the residue is satisfiable. For natural-language statements and contexts, an LLM entailment oracle decides the checks; it is sound if it accepts only checks that hold, and complete if it accepts every check that holds. We prove that a sound oracle makes the search safe regardless of pool quality, and that a complete one makes the frontiers tight. On security-critical AWS properties, EGs are safe in all 20 cases of an expert-adjudicated study, where majority vote over equivalence clusters and Universal Self-Consistency are unsafe in 25% and 10%. An ablation with the same oracle but no graph is unsafe in 25% and rejects every candidate in another 30%. We machine-checked our proofs in Lean.

</details>

### [How Far Apart Are Two Proofs? Measuring Proof Dissimilarity in a Proof Kernel and in Lean/Mathlib](https://arxiv.org/abs/2611.31811)
*Nikolaos Nikolaou* · `cs.LO` · arXiv:2611.31811v1 · relevance 0.25

- **In one sentence**: The paper defines 19 measures of how different two formal proofs of the same theorem are, groups them into six families, and tests them on proofs that the primes are infinite in a Curry-Howard kernel and in Lean 4/Mathlib.
- **In plain words**: As AI systems produce more mathematical proofs than people can read, it becomes useful to know whether a proof is really new or just a rewording of an old one. The authors propose many ways to measure how far apart two proofs are and check how well each matches human intuition, using proofs that infinitely many primes exist. They report that measures based on which earlier results a proof depends on track intuition best, while measures based on meaning can give surprising answers.
- **Why it matters**: Checking whether AI-generated proofs are duplicates or genuinely new, and relating them to human arguments, depends on having a sound way to measure proof distance. The text presents this as a foundation for such uses but does not show any of these applications in practice.
- **Background needed**: - A proof is a formal argument that a machine can check step by step; Lean/Mathlib is a widely used library of such checked mathematics.
- Curry-Howard correspondence: proofs and programs are treated as the same kind of object, which lets proofs be compared like code.
- Hilbert's 24th problem asks for a general theory of what makes proofs simple or similar; the identity-of-proofs problem asks when two proofs should count as the same.
- "Proof irrelevance" means that any two proofs of the same statement are treated as equal in some formal systems.
- Euclid's proof, Furstenberg's topological proof and Goldbach-style arguments are different routes to the same fact that there are infinitely many primes. · level: research-level
- Matched keywords: Lean, mathlib

<details><summary>Original abstract</summary>

We now live in the age of machine-generated mathematics: AI systems produce research-level proofs faster than the human mathematical community can read them. Verification is only part of the challenge. We also need to know whether a "new proof" is indeed new, whether a thousand generated proofs contain one idea or many, and where each sits relative to human mathematics. All of these require measuring distances between proofs. Following Hilbert's 24th problem and the identity-of-proofs problem, we ask how far apart two proofs of one theorem are, and what shape the proof space they inhabit has. We define 19 dissimilarity measures in 6 families (syntactic, structural, dependency & resource, semantic, information-theoretic, higher-categorical) and 10 desirable properties, which we argue are the conditions for safely optimising a measure. In a Curry-Howard kernel, 5 machine-checked proofs that the primes are infinite show that raw syntax cannot tell a rewrite from a new argument, that dependency-based and structural measures reproduce the intuitive ordering (Euclid rewritten < Goldbach < Furstenberg), and that semantic measures invert it: Furstenberg's topological proof produces exactly Euclid's witness. A replication in Lean 4/Mathlib (3 theorems, 19 proofs, 18 measures) confirms that dependency-closure measures track intuition best, and shows that equality of normal forms never holds between differently written versions of the same argument, that proofs by citation look unlike the arguments they cite, and that proof irrelevance cannot distinguish any two proofs. We argue for reporting dissimilarity as a multi-level profile, extend the measures to proofs of different theorems, and discuss uses, from detecting duplicated AI proofs and orchestrating prover agents to interpreting AI proofs via their nearest human-understandable counterparts. Code, Lean sources and data are released.

</details>

## Robotics and embodied AI

### [PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents](https://arxiv.org/abs/2611.33144)
*Feixiang Ruan, Guodong Lv, Kewei Zhang et al.* · `cs.RO` · arXiv:2611.33144v1 · relevance 0.20

- **In one sentence**: PyRUA-Dex uses multiple coding agents to write programmatic (code-based) control policies for dexterous bimanual robot manipulation without human demonstrations, evaluated on Bench2Dex and DexJoCo in simulation and on a two-hand real robot.
- **In plain words**: Teaching robot hands to do fine tasks like playing piano usually requires many examples from people, and those examples are hard to collect well. This paper describes a method where AI coding agents explore possible actions in parallel, keep the attempts that work, and condense them into a reusable code program that is then refined under randomized conditions. The authors report strong simulated scores and real-robot results on piano and calligraphy, including learning a new piece from sheet music in as little as 30 minutes.
- **Why it matters**: It offers an alternative to demonstration-heavy robot learning, which may matter for scaling dexterous manipulation. The text reports benchmark and hardware results but does not establish how well the approach generalizes beyond the tasks shown, so its broader significance is unclear.
- **Background needed**: - Dexterous manipulation: robot hands with many joints doing fine motor tasks.
- Bimanual: using two hands or arms at once.
- Programmatic policy: a robot controller written as code rather than as a neural network's learned weights.
- Demonstrations: recorded examples of a human doing the task, used to train robots; the paper's point is avoiding them.
- Teleoperation and retargeting: ways of controlling or mapping human motion onto a robot hand to collect examples.
- Randomized layouts: varying object positions and conditions during training so the policy is robust.
- Benchmarks (Bench2Dex, DexJoCo): standard simulated test suites for dexterous tasks; scores are as reported by the authors.
- SOTA: state of the art, the best published result on a benchmark. · level: research-level

<details><summary>Original abstract</summary>

Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explore in parallel for task skills and ways to compose them, and a distilling agent condenses the successful attempts into a task library and one program. During refinement, this program is improved through randomized layouts for enhanced robustness and execution efficiency. In simulated environments, PyRUA-Dex achieves SOTA on Bench2Dex with a score of 72.9 and reaches 81.0% success on DexJoCo under full randomization, ahead of every trained policy on both benchmarks. In real world experiments on a bimanual platform with two 22-DoF hands, PyRUA-Dex learns to play piano, write calligraphy, and other tasks efficiently: learning a new piece from sheet music takes as little as 30 minutes. These results suggest that PyRUA-Dex is an effective framework for developing dexterous manipulation policies with coding agents in the absence of high quality dexterous manipulation demonstrations.

</details>

### [Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations](https://arxiv.org/abs/2611.32101)
*Ange Bao, Haishan Zhang, Lingzi Xie et al.* · `cs.RO` · arXiv:2611.32101v1 · relevance 0.17

- **In one sentence**: Ego2Real uses egocentric human demonstrations recorded with tactile gloves to refine hand-object reconstructions and to add contact-based rewards for reinforcement learning, so anthropomorphic bimanual robot hands can learn dexterous manipulation.
- **In plain words**: Robots can learn skills by watching people, but cameras alone miss how hard a person is touching an object and where contact happens. This paper adds touch sensing through gloves worn by the demonstrator, and uses that touch data in two places: to correct the estimated hand poses and contact shapes, and to reward a robot's learning when its fingers make similar contacts. The authors report that adding touch information to both steps gives higher success rates on manipulation tasks.
- **Why it matters**: It targets a known gap in learning from human video: vision cannot reliably show force or contact, and this work tests whether touch data can make human demonstrations more useful for robot hands. The text does not give enough detail to judge how broadly the gains would carry over to other tasks or robots.
- **Background needed**: - Egocentric demonstration: video recorded from a head- or chest-mounted camera showing a person's own hands doing a task.
- Bimanual dexterous manipulation: using both hands with many finger joints to handle objects.
- Tactile sensing: measuring touch and contact pressure, here through instrumented gloves.
- Hand-object reconstruction: estimating the 3D shape and pose of a hand and the object it holds from images.
- Reinforcement learning: a robot learns by trial and error, guided by a reward signal; here, contact patterns from the human define part of that reward.
- Anthropomorphic robotic hand: a robot hand shaped roughly like a human hand, with a different body and motors than a person's.
- Sim-to-real style transfer: the learned policy must adapt to the robot's own morphology and actuation rather than copy human motion exactly. · level: research-level

<details><summary>Original abstract</summary>

Learning dexterous manipulation from egocentric human demonstrations offers a scalable path toward robot skill acquisition. Vision alone, however, provides limited information about physical contacts and the demonstrator's force intent, leading to ambiguities in interpreting hand-object interactions. Capturing human touch via tactile sensing is therefore crucial for reliable human-to-robot dexterous skill transfer. We present Ego2Real, a framework that leverages egocentric demonstrations and tactile gloves to transfer bimanual dexterous manipulation skills to robotic hands. Ego2Real incorporates tactile supervision at two complementary stages: (1) tactile-guided hand-object interaction reconstruction, which uses measured tactile signals to refine hand poses and contact geometry; and (2) contact-informed reinforcement learning, which translates human contact patterns into robotic contact rewards. By combining refined motion references with physical contact rewards during training, Ego2Real guides anthropomorphic robotic hands to emulate demonstrated contact behaviors while adapting to their own morphology and actuation. Experiments show that incorporating tactile supervision into both reconstruction and policy learning yields higher manipulation success rates, underscoring the importance of enriching egocentric demonstrations with tactile observations to improve their quality and transferability.

</details>

## Security and cryptography

### [Trustworthy Edge AI: Security, Privacy, and Resilience for Distributed Intelligence](https://arxiv.org/abs/2611.31331)
*Jaydip Sen, Subhasis Dasgupta* · `cs.CR` · arXiv:2611.31331v1 · relevance 0.11

- **In one sentence**: A book chapter surveying security, privacy, and resilience mechanisms for Edge AI systems, with a call for cross-layer design that treats these properties together.
- **In plain words**: This chapter is an overview of how to keep AI running on devices near the user, such as sensors, vehicles, and factory equipment, rather than only in distant data centers. It covers how to protect data and devices from attack, how to let devices learn together without sharing raw data, and how to keep systems working when parts fail or conditions are uncertain. It illustrates these trade-offs with examples from smart cities, self-driving cars, healthcare, and industrial monitoring.
- **Why it matters**: Moving AI onto many small, varied devices widens the ways a system can be attacked or fail, so a survey that ties security, privacy, and reliability together may help readers plan such systems. The text itself is a broad review and does not report new experimental results, so its value lies in organizing the field rather than in any specific finding.
- **Background needed**: - Edge AI: running AI models on local devices instead of in a central cloud.
- Federated learning: training a shared model where each device keeps its own data and only sends model updates.
- Secure aggregation: a method that lets a server combine device updates without seeing any single device's update.
- Differential privacy: adding controlled noise to data or results so individuals cannot be identified.
- Zero-trust: a security approach that checks every device and connection instead of trusting anything inside a network by default.
- Attestation: a device proving to others that its software is genuine and unmodified.
- Adversarial robustness: how well a model resists inputs deliberately crafted to fool it.
- Cross-layer design: building protections across hardware, software, and network layers together. · level: intermediate

<details><summary>Original abstract</summary>

This chapter examines the principles and emerging research directions for building secure, privacy-preserving, and resilient Edge Artificial Intelligence (Edge AI) systems. As intelligence shifts from centralized clouds to distributed edge environments, challenges arise in ensuring data integrity, privacy, and reliable operation under adversarial and uncertain conditions. The chapter analyzes Edge AI architectures, emphasizing the expanded attack surface due to heterogeneous devices, resource constraints, and dynamic networks. It reviews core security mechanisms, including hardware-rooted trust, zero-trust models, secure communication, and attestation. Privacy-preserving approaches, such as federated learning, secure aggregation, and differential privacy, enable collaborative intelligence without centralized data sharing. Resilience strategies, including fault tolerance, adversarial robustness, and adaptive orchestration, are also explored. Case studies from smart cities, autonomous vehicles, healthcare, and industrial IoT illustrate practical trade-offs. The chapter advocates a holistic, cross-layer design integrating security, privacy, and resilience for trustworthy edge intelligence.

</details>

### [Your bids are showing: re-identifying power plants in anonymized market data, and a differentially private alternative](https://arxiv.org/abs/2611.31681)
*Nikhil Ravi* · `eess.SY` · arXiv:2611.31681v1 · relevance 0.07

- **In one sentence**: The paper shows that PJM-style masking of power plant offer curves in ERCOT data can be undone by matching public plant data, and proposes a differentially private monthly release of aggregated offers calibrated with zero-concentrated differential privacy.
- **In plain words**: Electricity grid operators publish how much each power generator offers to sell at each price, but some hide the generator names, assuming that keeps the bids confidential. The authors tested this on Texas data where the names are public, and found that public fuel and emissions records could match about a quarter of the masked units to their actual plants. They then propose publishing only monthly totals with carefully sized random noise, which keeps the overall market picture usable while making it much harder to learn about any single unit.
- **Why it matters**: Offer data is used by market monitors to look for withholding of power, so how it is released matters for market oversight and for fairness among sellers. The text reports that the masked feed of PJM, another US grid operator, has the same fields, so the authors expect the same weakness there, but they did not test PJM's data directly.
- **Background needed**: - Electricity markets: generators submit offers (price and quantity) for each hour; the cheapest offers are dispatched first, and the price is set by the last unit needed (the clearing price).
- Merit order: the ranking of generators from cheapest to most expensive; the supply curve is the cumulative offered quantity by price.
- Re-identification: linking "anonymous" records to real identities using other public data such as outage dates and emissions reports.
- Differential privacy: a method that adds calibrated random noise so that the presence or data of any one person (here, one unit's year of offers) cannot be confidently inferred. Zero-concentrated differential privacy (zCDP) is a specific accounting method for measuring this privacy loss; epsilon is the privacy budget, where smaller means more privacy.
- Correlation: a measure from -1 to 1 of how closely two series move together. · level: research-level

<details><summary>Original abstract</summary>

ERCOT publishes every generator's hourly offer curve 60 days after the operating day. Market monitors, researchers and traders use these records to study the merit order and check for withholding. PJM publishes the same kind of data with unit names replaced by codes, on the view that masking keeps offers confidential. We test that view on ERCOT data from 2024 to 2026, where names are public and so provide ground truth, by masking the records under PJM's published rules. Public EIA and EPA data match 25% of the masked units we can score (32% of their capacity) to their plant, and 45% fall within the top five guesses. PJM's feed carries the same fields, so we expect masking to fail there too. Publishing exact fuel-group totals instead does not help. An attacker who knows the other units in a group recovers one unit's high-price offers exactly, and an outsider who knows only the target's outage dates reaches a correlation of 0.77, most of it from a few renewable and hydro units that offer at very high prices (0.32 over fossil units). We propose a differentially private release: monthly totals by fuel group and price bin, with Gaussian noise calibrated under zero-concentrated differential privacy so that each unit's whole year of offers is protected. It publishes an unbiased noisy layer and derives a monotone supply curve and shares from it at no extra privacy cost. At $\varepsilon=10$ per unit-year the market supply curve stays within 11% of the truth, the implied clearing price within \$3.0/MWh, and the attacker's correlation falls to 0.23. Whether an analysis still works depends on one ratio, how much the true quantity varies month to month against the noise, which predicts the accuracy of totals to within 0.05. The clearing price, supply slope and combined-cycle capacity remain usable, but no monthly release, private or exact, can answer questions about single hours or single units.

</details>

## Algorithms and complexity

### [Improved Lower Bounds for Online Parallel Machine Scheduling](https://arxiv.org/abs/2611.32565)
*Junwen Xiao, Zhiyi Tan* · `cs.DS` · arXiv:2611.32565v1 · relevance 0.24

- **In one sentence**: The paper proves improved lower bounds on the competitive ratio of online algorithms for makespan minimization on parallel identical machines, using a bin-packing-based estimate of the optimal makespan and a direct construction for five machines.
- **In plain words**: The paper studies how well a scheduler can assign jobs to several identical machines when jobs arrive one at a time and the scheduler cannot see future jobs, with the goal of finishing all work as early as possible. The authors show that no online method can do better than a ratio of about 1.887 compared with the best possible schedule. For the special case of five machines, they give a separate, direct argument that the ratio is at least 1.749.
- **Why it matters**: The text reports that these bounds improve on the best known lower bounds from about twenty years ago, so it updates how close current online methods can be to optimal. The text does not say whether the bounds are tight, and it does not discuss practical applications.
- **Background needed**: - Online algorithm: makes decisions as inputs arrive, without knowing what comes later.
- Makespan: the finish time of the last job, i.e. the total length of the schedule.
- Competitive ratio: the worst-case factor by which an online method's makespan exceeds the best offline schedule's makespan.
- Lower bound: a proof that no method can beat a given ratio; a larger lower bound means a harder problem.
- Parallel identical machines: several interchangeable processors that can each run one job at a time.
- Bin packing: the related problem of fitting items into the fewest containers; the paper uses it to estimate the optimal schedule length. · level: research-level

<details><summary>Original abstract</summary>

This paper establishes new lower bounds for online parallel machine scheduling aimed at minimizing the makespan. By leveraging bin packing algorithms to estimate the optimal makespan, we prove that the competitive ratio of any online algorithm is at least 1.887111. Additionally, via a direct construction, we demonstrate a lower bound of 1.74916 for the case of five machines. Our results improve upon the best known lower bounds established two decades ago.

</details>

### [Better-than-3 Approximation for 2ECSS Using the Primal-Dual Method](https://arxiv.org/abs/2611.32924)
*Ana Cezara Danciu, Sharat Ibrahimpur* · `cs.DS` · arXiv:2611.32924v1 · relevance 0.14

- **In one sentence**: This paper gives a single-phase primal-dual algorithm for the 2-edge-connected spanning subgraph problem with approximation ratio sqrt(3)+1 (about 2.74), improving on the previously best primal-dual ratio of 3, measured against the natural linear relaxation.
- **In plain words**: The paper studies how to cheaply build a network in which every link can fail without disconnecting any pair of points, given a menu of links with prices. The authors give a method that finds such a network whose cost is guaranteed to be at most about 2.74 times the best possible, down from the previous guarantee of 3 for this style of method. The approach works by gradually raising "prices" on groups of points and buying links once their prices become fully paid.
- **Why it matters**: Approximation ratios for this classic network-design problem have stayed at 2 or 3 for years, so a measured improvement for the primal-dual approach is a notable technical step. The text does not claim it beats the best 2-approximations, and its practical or wider impact is not discussed.
- **Background needed**: - Graph: points (vertices) joined by links (edges), each with a cost.
- 2-edge-connected: removing any single link leaves the graph connected.
- Spanning subgraph: a subset of links that still reaches every point.
- Approximation ratio: the worst-case factor by which an algorithm's cost can exceed the optimum.
- Linear relaxation: a looser, solvable version of the problem (here, each cut must be crossed by total weight at least 2) that gives a lower bound on the optimum.
- Primal-dual method: an algorithm that grows dual "prices" on sets of vertices and buys an edge when its dual constraint becomes tight, then prunes redundant edges.
- Contraction: merging a group of vertices into one node to simplify the problem. · level: research-level

<details><summary>Original abstract</summary>

In the $2$-edge-connected spanning subgraph problem (2ECSS), we are given an undirected multigraph whose edges have nonnegative costs, and the goal is to find a $2$-edge-connected spanning subgraph with minimum total cost. Two distinct approaches yield $2$-approximation algorithms: a reduction to the minimum-cost rooted $2$-arborescence problem and iterative rounding. Despite significant efforts, the best known approximation ratio using the primal-dual method has remained at $3$. Our main result in this work is a primal-dual algorithm for 2ECSS that achieves an approximation ratio of $\sqrt{3}+1 (\leq 2.74)$. The algorithm runs in a single phase and the approximation guarantee is relative to the natural linear relaxation, which requires the sum of the edge variables across every cut to be at least $2$. The algorithm follows the standard template of growing dual variables corresponding to minimal violated sets, albeit at non-uniform rates, until the dual constraint for an edge becomes tight, at which point the edge is temporarily purchased. Once feasibility is attained, redundant edges are dropped in the reverse order in which they were purchased. Our choice of dual growth rates is inspired by the single-phase $3$-approximation algorithm of Beyer, Chimani, and Spoerhase (COCOON 2020). As in their work, our algorithm maintains a forest of purchased edges by repeatedly contracting $2$-edge-connected subgraphs, and dual variables corresponding to leaves and isolated vertices of this forest are grown at a rate of $1$. Our main modification is to additionally grow dual variables corresponding to nontrivial connected components at rate $(\sqrt{3}-1)/2 \approx 0.37$, when the forest is disconnected.

</details>

## Programming languages and formal methods

### [Verifying Type Soundness for Nontransitive Information Flow Security](https://arxiv.org/abs/2611.32123)
*Chenyi Zhang* · `cs.PL` · arXiv:2611.32123v1 · relevance 0.15

- **In one sentence**: A machine-checked (Dafny) soundness proof for a type system enforcing nontransitive noninterference, an information-flow security property, extended to an imperative language.
- **In plain words**: This paper is about checking, with a computer proof assistant, that a set of rules for keeping secret information from leaking through a program is actually correct. The property studied is called nontransitive noninterference, which controls how information may flow between parts of a software system. The authors report a machine-checked proof that the type system, which checks programs against these rules, is sound for an imperative (step-by-step, state-changing) language.
- **Why it matters**: Security rules enforced by type checkers are only as trustworthy as their underlying proofs, and the text notes that existing enforcement mechanisms have not been formally verified to a high level of assurance. The work may matter to people building secure component-based software, though the text does not discuss practical deployment or performance.
- **Background needed**: - Noninterference: a security property saying secret inputs cannot affect publicly visible outputs.
- Information flow: tracking how data moves through a program so that secrets do not leak.
- Nontransitive policy: information may flow from A to B and from B to C without necessarily flowing from A to C, unlike simple "chain" rules.
- Type system: a set of checking rules, applied before a program runs, that rejects programs that could break a security policy.
- Soundness proof: a mathematical argument that the checking rules guarantee the property for every accepted program.
- Machine-checked proof: a proof written in a formal language and verified by software (here Dafny), so that human error in the argument is less likely.
- Imperative language: a programming style built on sequences of commands that change stored values. · level: research-level

<details><summary>Original abstract</summary>

We present a machine-checked soundness proof of a type system for the nontransitive noninterference (NTNI) information flow security property in an imperative programming language using Dafny. The original formulation of NTNI was developed for a functional programming language augmented with memory access operators, where security policies are expressed as coarse-grained information flow constraints over component-based software systems. Although subsequent research has extended NTNI type systems in various directions, to the best of our knowledge, no prior work has established a machine-checked soundness proof for type-enforced NTNI. As a result, the correctness of existing NTNI enforcement mechanisms has not been formally verified with a high degree of assurance.

</details>

### [Denotational Results in Compiler Correctness and Comparisons with Operational Approaches](https://arxiv.org/abs/2611.31724)
*Jeremy G. Siek, Matthew Heimerdinger, Tianyu Chen et al.* · `cs.PL` · arXiv:2611.31724v1 · relevance 0.13

- **In one sentence**: The paper gives the first denotational (meaning-based) proofs that closure conversion, a compiler pass for a Turing-complete functional language, is semantically reflecting, using a graph model and a Scott-domain model, and compares mechanized compiler-correctness proofs across five semantic styles.
- **In plain words**: This paper is about how to prove that a compiler, the program that translates code from one language to another, keeps the meaning of the code intact. The authors ask whether "denotational" semantics, which describe a program by the mathematical value it stands for, can be used for such proofs, as an alternative to "operational" semantics, which describe step-by-step execution. They work with a compiler from a functional language down to a simpler low-level form, and they compare the size of the proofs written in five different styles.
- **Why it matters**: Compiler correctness is a central goal in programming language research, and the text reports that closure conversion (a specific translation step) had no earlier denotational correctness proof for a Turing-complete language. The comparison of proof sizes is a first step toward guidance on choosing a semantic style, and the text presents it as only a first step.
- **Background needed**: - A compiler translates source code into a lower-level target language; correctness means the translated program behaves as the original should.
- Semantics is a precise description of what programs mean. Operational semantics describes step-by-step execution; denotational semantics maps programs to mathematical objects.
- Closure conversion turns nested functions that capture variables from their surroundings into flat, first-order code with explicit captured data.
- Preservation and reflection: a correct compiler must keep meanings (preservation) and must not create new meanings for programs that had none (reflection). The text says reflection is the harder direction here.
- Turing-complete means the language can express any computation, including ones that may not terminate.
- Logical relations are a proof technique relating values across two languages or models; graph models and Scott domains are two mathematical frameworks for denotational meaning. · level: research-level

<details><summary>Original abstract</summary>

Anyone setting out to prove a compiler correct must choose a style of semantics. The CakeML and CompCert projects, among others, show that operational semantics such as abstract machines and interpreters are viable choices. In this paper we explore whether denotational semantics can also be used in proofs of compiler correctness and evaluate the tradeoffs. We focus on a compiler from FPC, a language with lexically scoped functions and recursive types, to a first-order low-level intermediate language. This compiler includes closure conversion, but no prior proof of correctness with respect to denotational semantics covers closure conversion for a Turing-complete language. Compiler correctness requires that the denotation of a program be both preserved and reflected by the compiler. For closure conversion, reflection is the hard direction. We present the first denotational proofs of semantic reflection for closure conversion applied to a Turing-complete language, one proof with respect to a graph model and one with respect to Scott domains. For the graph-model proof we develop a new logical relation, the approximant logical relation, and for the Scott-domain proof we adapt a logical relation of Reynolds. As a first step in evaluating the tradeoffs, we compare mechanized correctness proofs of an eight-pass compiler, from FPC down to a typed low-level intermediate language, in five semantic styles. Two of the styles are denotational and three are operational. We find that no one semantics yields the shortest proofs for every compiler pass. We identify two factors that influence proof size. For operational semantics, proof size tends to grow with how much the runs of the source and target differ. For denotational semantics, the proofs are succinct when the correctness of a pass is an equation between meanings, and lengthy when a pass needs a logical relation.

</details>

## Systems and networking

### [Real-Time AI Acceleration on a 2D Spatial Dataflow Architecture](https://arxiv.org/abs/2611.31556)
*Shriram Raja, Anton Njavro, Richard West* · `cs.DC` · arXiv:2611.31556v1 · relevance 0.11

- **In one sentence**: The paper profiles the Tenstorrent Blackhole spatial dataflow accelerator and builds a worst-case execution time model, expressed as a Homogeneous Synchronous Dataflow Graph, extended with NoC contention delays for multi-core workloads.
- **In plain words**: Machine learning is being put into systems that must respond on strict deadlines, such as vehicles or industrial controllers, so engineers need to predict the longest time a computation could take. This paper studies an open-design AI chip, the Tenstorrent Blackhole, made of a grid of small processor cores linked by on-chip communication networks, and proposes a way to estimate that worst-case time. The authors tested the estimate across 12,567 task configurations and report that it was always above the slowest observed run.
- **Why it matters**: Commercial GPUs are hard to analyze for timing because some of their scheduling and memory behavior is undocumented, so an open, analyzable accelerator could matter for real-time AI. The reported overestimates (under 100% in most single-core cases, under 500% for multi-core with pessimistic contention analysis) are sizable, so the work is best read as a foundation rather than a finished guarantee.
- **Background needed**: - Worst-case execution time (WCET): the longest a task can take; real-time systems need a safe upper bound.
- ML accelerator: specialized chip (beyond a CPU) for running neural networks.
- GPU scheduling: GPUs run many threads in lockstep groups; how they are scheduled is not fully documented, complicating timing analysis.
- Spatial dataflow: a design where many cores each do fixed work and pass data to neighbors through a grid, with the programmer controlling data movement.
- Network-on-Chip (NoC): the on-chip communication network linking cores; sharing it causes delays (contention).
- Synchronous dataflow graph: a model of tasks and data flows with fixed rates, used to reason about timing.
- Overestimate percentage: how far the predicted bound exceeds the observed worst case. · level: research-level

<details><summary>Original abstract</summary>

Machine Learning (ML) is increasingly being integrated into real-time systems, which makes the timing analysis of ML accelerators necessary. However, the most popular commercial accelerator, the Graphics Processing Unit (GPU), remains difficult to analyze as several aspects of its behavior, including scheduling of threads involved in single-instruction multiple-thread computations and memory access latency, are not fully documented. Spatial dataflow accelerators present an interesting alternative to GPUs, as they inherently support compute and memory partitioning. Data movement and computation locality are explicitly controlled by the programmer. In this work, we consider the Tenstorrent Blackhole, which is based on a commodity RISC-V architecture. It consists of a 2D grid of cores connected by Networks-on-Chip (NoCs), supporting a fully open software runtime. We profile the Blackhole platform and develop a worst-case execution time task model as a Homogeneous Synchronous Dataflow Graph. We extend this model to a preliminary analysis of multi-core workloads by considering NoC-related delays. Finally, we evaluate our model across 12,567 task configurations and workloads. Results show that the estimate derived from our model lies above the observed worst case in every configuration. For single-core workloads, the overhead is less than 100% in most cases, with a maximum of less than 200%, and for multi-core workloads, it is less than 500% using a pessimistic NoC contention analysis. This paper lays the foundations for real-time computing on a promising open accelerator design.

</details>

### [The Recycler: In-Transit Machine Learning on High-Fidelity Data from Simulation Campaigns as an Optimized Approach for Building Frontier Models](https://arxiv.org/abs/2611.31434)
*Nikhil Rao, Mark Berrill, Ankush Checkervarty et al.* · `cs.DC` · arXiv:2611.31434v1 · relevance 0.10

- **In one sentence**: The paper reports a first demonstration of in-transit machine learning, where a large model trains on data streamed live from several parallel simulations in a campaign on an exascale supercomputer, instead of reading data saved to files.
- **In plain words**: Scientists often run many computer simulations at once to explore a system, such as a particle accelerator or a fusion reactor, but these runs produce far more data than storage systems can keep. This paper describes a workflow that sends the data straight from the running simulations into an AI model as it is being trained, skipping most of the saving to disk. The text presents this as a demonstration on a large supercomputer, and it reports the approach can use much more high-fidelity data for training than file storage allows.
- **Why it matters**: Storage limits force scientists to throw away most simulation output, so a way to learn from the full data stream could matter for fields that rely on large simulation campaigns. The text claims this could enable AI-guided feedback that steers simulations and cuts total computing time, but it gives no detailed measured results in the excerpt, so those benefits remain claims to be checked against the full paper.
- **Background needed**: - Simulation campaign: many simulation runs executed in parallel with different settings, rather than one run.
- Exascale high-performance computing: supercomputers capable of more than a quintillion (10^18) calculations per second.
- In-transit machine learning: training an AI model on data while it is moving between the simulation and storage, rather than after it is saved to files.
- File I/O: reading and writing data to disk, which is slow and capacity-limited at this scale.
- High-fidelity data: detailed, accurate simulation output, which is usually compressed heavily before saving.
- Frontier model: a very large, state-of-the-art AI model.
- Surrogate/feedback loop: using a trained model to guide which simulations to run next. · level: research-level

<details><summary>Original abstract</summary>

We report on the first realization of in-transit machine learning using data streamed from multiple simulations running in parallel to the training on the same exascale high performance computing system. This workflow can be commonly applied to a broad variety of scenarios in which simulation campaigns play an important role. Unlike single simulations, campaigns run several simulations in parallel. This is interesting for finding an optimum operation point of a machine like a particle accelerator or a fusion reactor, quantifying the variation in model predictions e.g. in climate research, or discovering new capabilities e.g. in materials or drug design. Such campaigns produce huge amounts of high-fidelity data at high rates. File system bandwidth and capacity prohibit retaining all of that data, usually requiring orders of magnitude in reduction before it can be stored. We demonstrate a workflow that streams the data from multiple simulations to train a frontier model in parallel, thereby maximizing data throughput. We demonstrate that this can use a much larger amount of high-fidelity data as training data for the model compared to storage in files, essentially replacing file IO by in-transit training of large-scale frontier models. This will allow to create AI-informed feedback loops to steer simulation campaigns while reducing the overall computation time needed and provide high-fidelity frontier models for reuse by the scientific community.

</details>

## Human-computer interaction

### [Emerging International Best Practices for AI Model Specs](https://arxiv.org/abs/2611.32768)
*Edward Kembery, Nathan Lambert, Robert McCarthy et al.* · `cs.CY` · arXiv:2611.32768v1 · relevance 0.06

- **In one sentence**: A position-style paper that offers a taxonomy, practical writing guidance, and a list of open problems for "model specs," the public documents in which frontier AI developers describe intended model behaviour.
- **In plain words**: AI companies are beginning to publish documents that explain how their chatbots and AI models are meant to behave. This paper argues that little independent advice exists on how to write such documents, so it sets out the benefits of writing them, a way of classifying them, practical steps for writing and applying them, and eight unresolved questions. It ends with recommendations for AI companies, governments, and researchers and civil society groups.
- **Why it matters**: As AI systems take on more roles, publicly stated behaviour rules may shape how developers are held accountable and how governments approach oversight. The text itself does not show how widely these documents are adopted or how well they work in practice, so their real-world impact remains uncertain.
- **Background needed**: - A "model spec" is a written document from an AI developer stating how its model should respond and what it should prioritise.
- "Frontier AI developers" means the companies building the most capable AI systems.
- A "taxonomy" is a structured classification of types of documents, here used to group different spec designs.
- "Open problems" are questions the field has not yet settled.
- Governance refers to the rules, norms and oversight that guide how AI is built and used.
- The paper is a guidance and position piece, not an experiment; the summary is based only on its abstract-level description. · level: introductory

<details><summary>Original abstract</summary>

Frontier AI developers from around the world have begun to publish documents that describe how their AI models are intended to behave. Although these 'model specifications'-or 'model specs', for short-are increasingly important in AI development and governance, little independent guidance exists for writing them. This paper addresses this gap in five main sections. First, we outline the advantages of writing a model spec for AI developers and society at large. Second, we introduce a taxonomy for model specs that developers can take inspiration from. Third, we propose guidance for writing and implementing a spec in practice. Fourth, we note eight open problems related to writing model specs for safe and desirable behaviour. We conclude with recommendations for frontier AI companies, governments, and research and civil society organisations.

</details>

### [Calm Agent: Reframing Agent Interaction around Intermittent Human Attention](https://arxiv.org/abs/2611.32009)
*Dian Jin, Zixun Fu, Guan Wang et al.* · `cs.HC` · arXiv:2611.32009v1 · relevance 0.05

- **In one sentence**: This position paper proposes "Calm Agent," a design framework for AI agents running ongoing background tasks around intermittent human attention, linking Delegate, Adjust, and Check interaction modes through a persistent task representation, and illustrates it with a desktop prototype called Orvlet.
- **In plain words**: AI helpers can now keep working on side jobs while a person focuses on something else. This paper argues that such helpers should be built around the fact that people only glance back at them now and then, so the work keeps going between visits and the person can quickly see what is happening and change it. The authors describe a three-part approach (hand off a task, adjust it, check on it) and show it through a desktop prototype, Orvlet, but the text does not report user studies or measured results.
- **Why it matters**: As AI agents take on longer background work, how people re-enter and supervise that work while protecting focus on primary tasks is an open interface question. The paper mainly sets out a design position and lists challenges, so its value depends on how far the prototype and later work develop these ideas.
- **Background needed**: - AI agent: software that carries out multi-step tasks on a user's behalf, rather than answering a single question.
- Intermittent attention: a person's focus comes and goes, so they check in briefly instead of watching continuously.
- Persistent task representation: a stored, always-updated record of what the agent is doing, its status, and its options, so the user can pick up where they left off.
- Generative interface: an interface the AI builds on the fly to fit an open-ended goal, as opposed to fixed buttons and menus.
- Background execution: a task that keeps running without occupying the user's screen or focus.
- Human-computer interaction (HCI): the field studying how people use and design computer systems. · level: intermediate

<details><summary>Original abstract</summary>

AI agents can carry out auxiliary tasks while users focus on other work. Yet users still need to understand task state, make changes, and respond when help is required. We argue that agents for ongoing auxiliary tasks should be designed around intermittent human attention: tasks should continue between interactions, and users should be able to return with little effort to understand and control them. We develop this position as Calm Agent. It connects three on-demand interaction modes: Delegate, Adjust, and Check, through a persistent task representation. Generative interaction provides controls and feedback suited to open-ended goals, while existing controls support routine actions. We illustrate these principles with Orvlet, a desktop prototype for background execution and compact task interfaces. We identify challenges in adapting interfaces while preserving continuity, coordinating attention across tasks, providing responsive interaction, and learning user habits over time. The aim is to support continuing task control while protecting attention for primary work.

</details>

## Information theory

### [Multi-User Linear Precoder Optimization for Obfuscation-Aided Mixed Regular and Wiretap Coding](https://arxiv.org/abs/2611.31840)
*Bastian Loss, Ahmad Nimr, Gerhard Fettweis* · `cs.IT` · arXiv:2611.31840v1 · relevance 0.19

- **In one sentence**: The paper proposes a generalized obfuscation-aided mixed wiretap/regular coding system built on multi-user linear precoding, formulates a precoder optimization under a minimum secrecy rate constraint, and reports simulation results for a geometric two-user line-of-sight channel.
- **In plain words**: The paper looks at how to send information securely over a wireless link so that an eavesdropper cannot easily read it. Standard secure ("wiretap") coding can be slow when the eavesdropper's channel is nearly as good as the intended receiver's, so the authors use a mixed scheme: a short secret is protected with secure coding, and that secret scrambles (obfuscates) a larger payload sent with ordinary coding. Using simulations of a two-user line-of-sight channel, they study how the secrecy requirement sets the balance between the two coding modes and how antenna beam shaping can be tuned for each layer.
- **Why it matters**: Mixed coding aims to recover data rate that pure secure coding loses on poor channels, which matters for physical-layer security as an complement to classical encryption. The text is limited to simulations of one geometric channel model, so its general applicability is not established from this description alone.
- **Background needed**: - Wiretap coding: a method that exploits the gap between the legitimate receiver's channel and the eavesdropper's channel to keep messages secret without a shared key.
- Regular channel coding: standard error-correcting coding that maximizes reliable data rate, with no secrecy guarantee.
- Obfuscation: scrambling a payload with a secret so it is useless without that secret.
- Secrecy rate: the rate at which information is delivered to the intended receiver while the eavesdropper learns essentially nothing.
- Linear precoding: multiplying signals by a matrix before transmission across multiple antennas, to steer beams toward users.
- Multi-user line-of-sight (LoS) channel: a wireless link with a direct path, where user positions set the channel geometry.
- Beampattern: a map of how much transmit power goes in each direction. · level: research-level

<details><summary>Original abstract</summary>

Physical-layer security has attracted considerable research interest with the development of quantum computing. One prominent approach is wiretap coding, which exploits the channel advantage of a legitimate receiver over an eavesdropper to achieve secure communication. However, under unfavorable channel conditions, wiretap coding can significantly reduce the achievable rate compared to regular channel coding. Mixed coding alleviates this limitation by using wiretap coding to protect a short secret required for obfuscation, while the obfuscated payload is encoded using regular channel coding. In this work, we propose a generalized obfuscation-aided mixed-coding system based on the multi-user (MU)-linear precoding (LP) architecture that unifies existing approaches employing different obfuscation functions. We then formulate the corresponding precoder optimization problem, abstracting the obfuscation function through a minimum secrecy rate constraint. Numerical simulations using a geometric two-user line-of-sight (LoS) channel demonstrated how the minimum secrecy rate requirement determines the operating point of mixed coding between regular and wiretap coding. Subsequent beampattern analysis revealed a key synergy between mixed coding and precoding: Mixed coding enables individual beam shaping for the two coding layers. Finally, spatial analysis showed that mixed coding offers the largest sum-rate gains when users are positioned at similar angles.

</details>

### [Self-Orthogonal Minimal Codes from n-to-1 Mappings](https://arxiv.org/abs/2611.32192)
*Qin Du, Ziling Heng, Jun Zhang* · `cs.IT` · arXiv:2611.32192v1 · relevance 0.15

- **In one sentence**: Using right greatest common divisors of skew polynomials to compute kernel dimensions of linearized polynomials, the paper derives exact weight distributions for linear codes from three families of n-to-1 mappings and shows the codes are minimal and self-orthogonal.
- **In plain words**: This paper is about error-correcting codes, the mathematical recipes used to protect data from corruption. The authors study codes built from certain functions over finite fields, which are small number systems, and find a way to count how their codewords are distributed without checking each one. They then show that three families of these codes have two useful properties that let one code serve both quantum error correction and secret sharing.
- **Why it matters**: Codes that are both self-orthogonal and minimal can feed two applications at once: building quantum error-correcting codes and defining secret-sharing schemes. The text presents a new algebraic method for getting exact weight counts where direct computation is hard, which may help future work on such codes, though its wider impact is not shown in the text.
- **Background needed**: - Linear code: a set of vectors closed under addition, used to add redundancy so errors can be detected or fixed.
- Finite field: a number system with finitely many elements, the arithmetic base for these codes.
- n-to-1 mapping: a function where exactly n inputs share each output; its structure determines the code.
- Weight distribution: how many codewords have each number of nonzero entries; it governs code performance.
- Walsh spectrum: a transform of a function that encodes the same weight information.
- Self-orthogonal code: a code whose vectors are orthogonal to each other, a requirement for many quantum code constructions.
- Minimal code: no codeword's support is contained in another's; this makes it usable for secret sharing.
- Secret-sharing scheme: a way to split a secret among participants so only approved groups can recover it.
- Skew polynomial ring: a polynomial algebra where variables do not commute, used here as the main tool.
- Right greatest common divisor: the largest common right factor of two skew polynomials, used to find kernel dimensions. · level: research-level

<details><summary>Original abstract</summary>

Self-orthogonal codes are central to the construction of quantum error-correcting codes, and minimal codes yield secret-sharing schemes whose access structures are read off from the supports of their codewords. A code that is both self-orthogonal and minimal therefore serves both purposes at once, so that a single family of codes can produce a quantum code and a secret-sharing scheme simultaneously. Linear codes arising from n-to-1 mappings over finite fields are a natural source of such codes and have attracted considerable attention recently, yet their parameters and weight distributions remain difficult to determine: for most high-degree functions the Walsh spectra cannot be computed directly, and it is precisely these weights on which the analysis of minimality and self-orthogonality rests. We address this difficulty through the algebraic theory of skew polynomial rings. Using the right greatest common divisor of skew polynomials, we determine the dimensions of the kernel spaces of the linearized polynomials associated with the n-to-1 mappings, which in turn yield the weight distributions of the corresponding codes. With this method we treat two newly constructed families of n-to-1 functions together with one known family, and obtain the exact weight distributions of the resulting codes; we further prove that all of these codes are minimal and self-orthogonal. Each family therefore simultaneously yields a quantum error-correcting code and a secret-sharing scheme, with explicitly determined parameters and access structures. This work offers a new perspective for determining the parameters of linear codes derived from n-to-1 mappings.

</details>

## High-energy theory and gravity

### [Free hyperboloidal evolution in 3D: gauge waves and constraint-violating gravitational waves](https://arxiv.org/abs/2611.31379)
*Alex Va\~n\'o-Vi\~nuales* · `gr-qc` · arXiv:2611.31379v1 · relevance 0.22

- **In one sentence**: This paper extends the conformal compactification approach with BSSN/Z4 formulations of general relativity from spherical symmetry to full 3D, demonstrating free hyperboloidal evolution that reaches future null infinity, tested on gauge waves and constraint-violating gravitational waves in Minkowski spacetime.
- **In plain words**: Physicists who simulate gravity on computers usually stop their simulated space short of the far future edge, where gravitational waves finally escape to infinity. This paper describes a way to use slanted, hyperboloid-shaped time slices that reach that far edge, and extends the method from simple spherical setups to fully three-dimensional simulations. The authors tested it on simple waves moving through empty flat space and report that the code behaves reliably and that signals can be read off at the far edge.
- **Why it matters**: Reading gravitational-wave signals directly at future null infinity avoids errors from cutting the simulation off at an artificial boundary, which matters for predicting signals that detectors such as LIGO could see. The text only covers tests in flat spacetime with a first step, so its wider usefulness for realistic black hole or merger simulations is not shown here.
- **Background needed**: - General relativity describes gravity as curved spacetime; numerical relativity solves its equations on computers.
- Gravitational waves are ripples in spacetime that carry energy outward.
- Future null infinity is the idealized boundary where outgoing light and gravitational waves end up as time goes to infinity.
- Hyperboloidal slices are time slices that reach that boundary, unlike ordinary constant-time slices that stop short of it.
- Conformal compactification rescales space so that infinity becomes a finite, reachable location.
- BSSN and Z4 are standard formulations of Einstein's equations used in simulations; constraints are equations that must stay satisfied, and "constraint-violating" waves are test perturbations that break them on purpose.
- Gauge waves are coordinate-only ripples that test how the simulation handles choices of time and space labels.
- Minkowski spacetime is flat, empty space with no gravity, used as a simple test background. · level: research-level

<details><summary>Original abstract</summary>

Hyperboloidal evolution allows to reach future null infinity within numerical relativity simulations. This work extends the conformal compactification approach with BSSN/Z4 from spherical symmetry to full 3D simulations. This is the first free numerical hyperboloidal evolution in 3D with a common formulation of general relativity. In this first step, gauge waves and constraint-violating gravitational waves perturbing Minkowski spacetime are evolved nonlinearly and show that the implementation is reliable and signals can be successfully extracted at future null infinity.

</details>

### [NS5-branes and the black hole/string transition](https://arxiv.org/abs/2611.31945)
*Asad Fayiz, Emil J. Martinec* · `hep-th` · arXiv:2611.31945v1 · relevance 0.21

- **In one sentence**: The paper extends a family of 6d BPS supergravity solutions (built from slightly separated fundamental strings and NS5-branes near the BTZ black hole threshold) to include gauge excitations of the fivebranes, and studies D-string soliton energetics relative to the deconfinement transition of little strings.
- **In plain words**: The paper looks at a hypothetical setting in string theory where a black hole-like object begins to form from a bundle of strings and five-dimensional membranes called branes. The authors extend a set of known mathematical descriptions of this setting so they include extra internal "gauge" excitations on the branes. They then compare the energy cost of certain brane-bound solitons (localized lumps of energy) with the point at which the tangled strings switch from a confined to a free, black-hole-like state.
- **Why it matters**: The transition between a string-like state and a black hole is a long-standing question about how gravity and strings fit together, so the question is of interest to specialists. The text does not report a definitive result, and its wider significance beyond this framework is not stated in the abstract.
- **Background needed**: - String theory: a framework where fundamental particles are tiny vibrating strings, requiring extra dimensions.
- Black hole/string transition: the idea that highly excited strings and black holes may be two sides of one phase change.
- BTZ black hole: a simple black hole solution in three-dimensional gravity, used as a toy model.
- NS5-branes: five-dimensional extended objects in string theory; "little strings" are the strings living on them.
- Supergravity and BPS solutions: low-energy gravity theories and special, highly symmetric solutions that are stable because of supersymmetry.
- Deconfinement: a phase change where bound constituents become free, similar to melting or boiling in ordinary matter.
- Gauge excitations and solitons: internal field configurations and stable localized lumps of energy. · level: research-level

<details><summary>Original abstract</summary>

Near to the onset of BTZ black hole formation in string theory is a large ensemble of 6d BPS supergravity solutions sourced by slightly separated fundamental strings and Neveu-Schwarz fivebranes. We extend the construction of these geometries to include gauge excitations of the fivebranes, and then study the energetics of D-string solitons in relation to the deconfinement transition of little strings, which are the natural non-abelian degrees of freedom that deconfine in the transition to the black hole phase.

</details>

## Statistical physics

### [Parametric neural-network wavefunctions across a bosonic phase transition](https://arxiv.org/abs/2611.33150)
*Daniil S. Antonenko, Liang Fu, Leonid I. Glazman* · `cond-mat.quant-gas` · arXiv:2611.33150v1 · relevance 0.26

- **In one sentence**: The paper introduces Boseformer, an attention-based neural-network ansatz that represents bosonic many-body wavefunctions as a function of a Hamiltonian parameter, trained via variational Monte Carlo across a superfluid-to-crystal quantum phase transition in 2D bosons with 1/r^3 repulsion.
- **In plain words**: The paper looks at a group of identical quantum particles (bosons) that can either flow without friction as a superfluid or lock into a regular crystal, depending on how strongly they repel each other. The authors built a neural network, called Boseformer, that encodes the particles' quantum state, and trained it so that one network covers a whole range of interaction strengths rather than being retrained for each value. They report this on a simulated two-dimensional system with a particular long-range repulsion.
- **Why it matters**: Describing the transition with one trained model instead of many separate calculations could make it cheaper to map out phase diagrams of quantum materials and cold-atom systems. The text is short and gives no quantitative comparisons, so how well the approach works relative to existing methods cannot be judged from it.
- **Background needed**: - Wavefunction: the mathematical description of a quantum system's state; its square gives probabilities of finding particles in various arrangements.
- Bosons: particles (such as atoms of certain types) that can share the same quantum state and obey Bose statistics.
- Superfluid vs. crystal: a superfluid flows with zero viscosity; a crystal has particles fixed in a repeating lattice. Moving between them is a quantum phase transition, driven by a parameter in the energy function rather than temperature.
- Hamiltonian: the energy rule of the system; here one of its parameters is varied.
- Variational Monte Carlo: a method that tunes a trial wavefunction by random sampling to lower its energy, used when exact solutions are impossible.
- Neural-network wavefunction: using a machine-learning model as the trial wavefunction; attention is the mechanism in modern networks that weighs relationships between inputs.
- 1/r^3 interaction: a repulsion that falls off with distance r as the inverse cube, longer-ranged than ordinary contact forces. · level: research-level

<details><summary>Original abstract</summary>

We propose Boseformer, a universal attention-based neural-network architecture for representing the wavefunctions of particles with bosonic quantum statistics, including superfluid and crystal phases. The model is trained to generate the wavefunction as a function of a Hamiltonian parameter across the quantum phase transition between these phases. Once trained with variational Monte Carlo optimization, it can serve as a foundation model describing the phase transition without the need to retrain it for individual parameter values. We demonstrate our method on a system of two-dimensional bosons with $1/r^3$ repulsive interaction.

</details>

### [Polar Streams through Active Condensation in Flocks](https://arxiv.org/abs/2611.33007)
*Lauritz Hahn, Xinyu Dou, Ziqi Zhou et al.* · `cond-mat.soft` · arXiv:2611.33007v1 · relevance 0.18

- **In one sentence**: Experiments on self-propelled Janus colloid dimers, backed by particle simulations and coarse-grained hydrodynamic theory, show that a flock can phase-separate into elongated dense polar streams via an "active nematic condensation" mechanism that goes beyond the standard Toner-Tu description.
- **In plain words**: Researchers studied tiny self-propelled particles that move together as a flock. They found that the flock can split into dense, elongated streams that all move along their own length, unlike the sideways bands seen near the flocking transition. The authors attribute this to denser regions becoming more strongly aligned, which pulls in more particles and feeds the condensation.
- **Why it matters**: The paper suggests that collective motion and clustering can reinforce each other rather than compete, and that nematic (rod-like, head-to-tail-free) alignment can shape flocks, which the usual Toner-Tu equations do not include. Its wider relevance to biological or synthetic swarms is plausible but not established by the text.
- **Background needed**: - Active matter: systems of self-propelled units that consume energy to move, such as colloids, cells, or animals.
- Flocking: particles align their movement direction so the group moves coherently.
- Motility-induced phase separation: self-propulsion alone can make particles bunch into dense clusters, without any attraction between them.
- Janus colloids: microparticles with two faces of different chemistry, which can be propelled by a chemical or field gradient; dimers are pairs of linked particles.
- Polar order: all particles point the same way. Nematic order: particles share an axis but not a direction.
- Toner-Tu equations: a standard continuum theory of flocks that describes the average direction and density of motion.
- Coarse-graining: deriving large-scale equations from microscopic particle rules. · level: research-level

<details><summary>Original abstract</summary>

Two of the most paradigmatic phenomena in active matter are flocking, where particles align to move collectively, and motility-induced phase separation, where self-propulsion causes particles to condense even without attractive interactions. Here, using experiments on self-propelled Janus colloid dimers, we show that flocks can phase separate to form polar streams. These structures are elongated dense clusters of particles that flock along the stream's long axis, in contrast to the well-known transverse bands that form close to the flocking transition. We use particle-based simulations and hydrodynamic theory obtained through coarse-graining to identify the underlying mechanism, which we call active nematic condensation: Denser regions of the flock develop stronger polar and hence nematic order, which leads to further particle fluxes into the dense region. These results reveal a generic mechanism whereby flocks can condense into streams. Our findings uncover that flocks can be shaped by nematic order, which is usually not accounted for in the standard Toner-Tu equations. More broadly, our work shows that collective motion and phase separation can not only coexist but also cooperate in active matter.

</details>

## Condensed matter

### [Detecting Topological Phases Through Dynamics of Chiral Density in Momentum-space Lattices](https://arxiv.org/abs/2611.31878)
*Rui Tian, Xiayao He, Tianhao Wu et al.* · `cond-mat.quant-gas` · arXiv:2611.31878v1 · relevance 0.21

- **In one sentence**: The paper proposes a spectroscopic protocol that uses the time evolution of a chiral-operator density in a momentum-space Su-Schrieffer-Heeger chain to reconstruct the local and total density of states and detect zero-energy edge modes and bulk-boundary correspondence.
- **In plain words**: Researchers study how to tell whether a simulated quantum material is in a special "topological" state, which can carry protected signals at its edges. They propose watching how a particular measured quantity changes over time after the system is disturbed, then applying a Fourier transform (a standard way of turning a time signal into an energy spectrum). According to the abstract, this recovers the energy-resolved information needed to spot edge modes.
- **Why it matters**: The approach is a proposed diagnostic for quantum simulators built from momentum-space lattices, which are a flexible experimental platform. Its practical value depends on whether it can be realized and works beyond the simple model studied here; the text alone does not show that.
- **Background needed**: - Topological phase: a state of matter whose key properties are robust to small changes, often shown by special states at the edges.
- Su-Schrieffer-Heeger (SSH) chain: a simple one-dimensional model of particles hopping along a chain, used as a standard testbed for topology.
- Momentum-space lattice: a lattice in which the sites correspond to momentum values rather than physical positions, allowing quantum simulation with cold atoms or photons.
- Density of states and local density of states: how many energy levels exist overall, and how many are concentrated at a given location.
- Zero-energy edge modes: states pinned at zero energy at the ends of a topological chain.
- Fourier transform: converting a signal recorded over time into its frequency or energy content. · level: research-level

<details><summary>Original abstract</summary>

Momentum-space lattices offer a versatile platform for quantum simulation in particular emulating topological states of matter.In this work, we propose a spectroscopic protocol via utilizing the dynamics of the chiral operator to detect the topological properties of a momentum-space Su-Schrieffer-Heeger chain. We show that the time evolution of the chiral density is directly linked to the local density of state (LDOS). By performing a Fourier transformation of that, we reconstruct both the LDOS and density of states of the system, enabling the unambiguous signature of zero-energy edge modes and the bulk-boundary correspondence. This dynamical approach provides a diagnostic tool for exploring topological phases in synthetic quantum matter.

</details>

### [Intrinsic longitudinal Hall effect in ferroaxial metals with high-order rotation axes](https://arxiv.org/abs/2611.32709)
*Eleni Chatzikyriakou, Stepan Tsirkin, Fernando Pe\~naranda et al.* · `cond-mat.mes-hall` · arXiv:2611.32709v1 · relevance 0.20

- **In one sentence**: The paper argues that the intrinsic (quantum, Berry-curvature-based) longitudinal Hall effect in ferroaxial metals can be isolated in the eight ferroaxial groups that have a 3-, 4- or 6-fold rotation axis, where the classical Lorentz-force term vanishes, and identifies Ni3P via first-principles calculation as a candidate.
- **In plain words**: When an electric current flows through a metal in a magnetic field, the sideways voltage (the Hall effect) usually comes mostly from a classical force on moving electrons, which hides a smaller quantum contribution. This paper looks at crystals with a special kind of hidden twist symmetry, called ferroaxial, where the voltage measured along the current direction can be set up so the classical part cancels. The authors list candidate metals with high-order rotation symmetry and calculate the effect for Ni3P, which they suggest is a promising material for measuring the quantum part on its own.
- **Why it matters**: Separating a quantum contribution from a classical one is what makes such a measurement informative about the electronic structure of a metal. The text does not show experimental confirmation, so the practical value depends on whether Ni3P or similar materials can be measured as predicted.
- **Background needed**: - Hall effect: a voltage produced perpendicular to an electric current when a magnetic field is applied.
- Longitudinal Hall effect here: the voltage response lies along the current direction, which is unusual and occurs only in certain crystal symmetries.
- Lorentz force: the classical push on moving charges from a magnetic field; it is normally the dominant Hall signal.
- Berry curvature: a geometric property of electron wavefunctions in a crystal that acts like an internal magnetic field in momentum space.
- Fermi surface: the boundary in momentum space separating occupied and unoccupied electron states in a metal; the effect is set by states near it.
- Ferroaxial crystals: crystals lacking certain mirror and inversion symmetries, with a rotational "axial" order that is not magnetic.
- Rotation axis of order 3, 4 or 6: a symmetry where rotating the crystal by 120, 90 or 60 degrees leaves it unchanged.
- First-principles calculation: computing material properties directly from quantum mechanics without fitted parameters. · level: research-level

<details><summary>Original abstract</summary>

The low-field Hall resistivity of non-magnetic metals has an intrinsic quantum contribution that derives from the field-corrected Berry curvature and intrinsic magnetic moment of the Bloch states near the Fermi surface. However, its effect is usually overshadowed by the classical Lorentz-force contribution. Here we show that for the longitudinal Hall effect, which occurs in ferroaxial crystals when the applied magnetic field lies in the Hall plane, the Lorentz force contribution vanishes for the eight ferroaxial groups with a 3,4 or 6-fold rotation axis. This provides an opportunity to measure the quantum correction in isolation, but so far all measured instances of the effect fall in the remaining five ferroaxial groups of lower symmetry, where the Lorentz force dominates the signal. We compile a list of candidate ferroaxial metals with such high-order rotation axis and compute the Hall effect from first principles for representative candidates, identifying Ni$_3$P with $\sigma^{\rm H}_{xzx} = 28.4$ S/m/T as a promising material to unambiguously measure the intrinsic longitudinal Hall effect.

</details>

## Particle physics

### [Dark vector meson effects on composite dark matter](https://arxiv.org/abs/2611.31368)
*Tomohiro Abe, Ryosuke Sato, Ozan Semin et al.* · `hep-ph` · arXiv:2611.31368v1 · relevance 0.20

- **In one sentence**: Extends prior work on G-parity-odd dark pion dark matter in a QCD-like SU(N_c) dark sector by adding dark rho vector mesons, which enable resonant enhancement in relic abundance and mix with Standard Model gauge bosons, and recasts LHC searches and projects FCC-hh and muon collider reach.
- **In plain words**: This paper studies a hypothetical hidden sector, a dark version of the strong force with its own quarks, whose lightest particles could make up dark matter. Earlier work looked only at the dark "pions" as the dark matter; this study adds the heavier dark "rho" particles. The authors find that these heavier particles can noticeably change how much dark matter is left over from the early universe, and they outline how existing collider searches and future machines could detect them.
- **Why it matters**: It offers a concrete, testable route for a dark matter candidate that could show up at colliders, not only in cosmic or underground detectors. The text gives only the headline claims (resonant enhancement, mixing with Standard Model bosons, FCC-hh reach up to 40 TeV), so the strength of these results should be checked against the full calculations.
- **Background needed**: - Dark matter: unseen matter that makes up most of the mass of galaxies; its amount is set by how it was produced and thinned out in the early universe (the "relic abundance").
- Relic abundance and resonant enhancement: when a particle's mass is near a particle-pair energy, interactions are boosted, changing how much survives.
- Hidden or dark sector: particles that interact with ordinary matter only weakly, here via a QCD-like strong force with dark quarks.
- Dark pions and rho mesons: bound states of dark quarks, analogous to ordinary pions and rho mesons; the rho is a heavier "vector" partner.
- G-parity: a symmetry property that determines which decays and couplings are allowed.
- Mixing with Standard Model gauge bosons: the dark rho can blend with W, Z or photon-like particles, giving it new ways to decay.
- Colliders: LHC (ATLAS, CMS) searches are reinterpreted; FCC-hh (a proposed 100 TeV proton collider) and muon colliders are future machines. · level: research-level

<details><summary>Original abstract</summary>

We extend previous studies of $\mathcal{G}$-parity-odd dark pion dark matter in a QCD-like $\mathrm{SU}(N_c)$ gauge theory with electroweakly interacting dark quarks to include the effects of $\rho$ mesons. We show that vector mesons can substantially affect relic abundance calculations through resonant enhancement, significantly affecting the conditions required to reproduce the observed relic abundance. Electroweak interactions further induce mixing between the dark $\rho$ mesons and Standard Model gauge bosons, opening new decay channels for the dark $\rho$ and modifying the effective interactions of the dark pions. We recast existing ATLAS and CMS searches to constrain the model, and perform a collider phenomenology study targeting the future FCC-hh and muon colliders, focusing on the resonant enhancement of cross sections in the $e^+e^-$, $\mu^+\mu^-$, and $W^+W^-$ final states for the latter. We show that the FCC-hh could probe $\rho$ mesons whose mass is up to 40 TeV.

</details>

### [Dark Matter Assisted Axion-Magnetic Resonance](https://arxiv.org/abs/2611.32906)
*Chen Sun, Si-Yu Wu, Seokhoon Yun* · `hep-ph` · arXiv:2611.32906v1 · relevance 0.18

- **In one sentence**: A proposed resonance in which an oscillating axion dark matter background boosts the conversion of stellar axions into X-rays in a magnetic field, tested against NuSTAR data from the starburst galaxy M82.
- **In plain words**: The paper looks for a hypothetical light particle called the axion, which could make up dark matter and could also be made in stars. In a magnetic field, such axions can turn into X-ray photons, and the authors show that the dark matter background can make this conversion much stronger at certain particle masses. They apply this idea to X-ray observations of the galaxy M82 from the NuSTAR telescope.
- **Why it matters**: If correct, the effect would tighten limits on how strongly axions couple to light over part of the mass range where ordinary conversion is suppressed, which matters for dark matter searches. The authors report only a moderate preference for their features in the data, which is still consistent with statistical noise, so the result needs confirmation.
- **Background needed**: - Axion: a hypothetical, very light particle proposed to solve a problem in particle physics and a candidate for dark matter.
- Dark matter: unseen matter that makes up most of the mass of galaxies, detected only through gravity.
- Photon-axion conversion: an axion turning into a photon (particle of light) when passing through a magnetic field.
- Resonance: a condition where two effects match up so a process is strongly amplified, like pushing a swing at its natural rhythm.
- Dispersion relation: how a particle's energy depends on its momentum and mass; mismatch between photons and axions normally suppresses conversion.
- Stellar axions: axions expected to be produced in the hot cores of stars.
- M82: a starburst galaxy with intense star formation, used as a bright source.
- NuSTAR: an X-ray space telescope whose existing data is reanalysed here.
- Upper limit / constraint: a bound saying a coupling must be smaller than some value given no signal was seen. · level: research-level

<details><summary>Original abstract</summary>

An oscillating axion dark matter (DM) background can enhance the conversion of another relativistic axion into photons when traversing a magnetic field. The DM background rotates photon polarization relative the magnetic orientation, which compensates the photon's and the propagating axion's dispersion relation mismatch. We relate this mechanism to Axion Magnetic Resonance (AMR) and apply it to stellar axions in the starburst galaxy M82. We analyze its enhancement to the resulting X-ray signals while accounting for the finite magnetic domain size, dark matter coherence length, DM density morphology, plasma profiles, and the detector response. We derive strong constraints using existing X-ray data from NuSTAR. We show that this resonant conversion can lead to $\mathcal O(10^2)$ enhancement in the photon-axion conversion probability, improving the upper limits on axion's photon coupling over part of the mass range where ordinary conversion is suppressed. We also show that this type of resonance predicts distinctive features in the hard X-ray spectrum, which is moderately favored by the data over the background only model, yet it is currently still consistent with statistical fluctuations.

</details>

## Nuclear physics

### [Elastic polar oscillations and nuclear parameters](https://arxiv.org/abs/2611.31819)
*Hajime Sotani* · `astro-ph.HE` · arXiv:2611.31819v1 · relevance 0.12

- **In one sentence**: A review-style summary of how crustal elastic oscillation modes (s- and i-modes) of neutron stars, potentially seen in short gamma-ray burst precursors, could be used to constrain nuclear saturation parameters K0 and L via compactness-based fitting formulas.
- **In plain words**: Neutron stars are extremely dense stellar remnants, and when two of them merge they may make the crust ring like a bell before a short gamma-ray burst. This paper summarizes earlier work on the ringing frequencies tied to the crust's elasticity, which could in principle reveal how the star's matter behaves. The authors report that, for a given set of nuclear properties, certain scaled frequencies depend mainly on the star's compactness, and they give fitting formulas linking those frequencies to two nuclear parameters, K0 and L.
- **Why it matters**: If such oscillations were observed, matching them to these formulas could help narrow the possible values of nuclear properties that are hard to measure in the laboratory, which is why the approach is of interest to neutron-star seismology. The text does not report any observation of these modes, so the practical payoff remains conditional on future detections.
- **Background needed**: - Neutron star: a collapsed star roughly 1.4 times the Sun's mass packed into about 20 km across.
- Oscillation modes: ways a star can vibrate; the fundamental, pressure, and gravity modes are the usual ones, while shear and interface modes arise from the crust's elasticity.
- s-mode and i-mode: crust-related vibration modes named in the paper; the text does not define them in detail.
- Asteroseismology: inferring a star's interior properties from its vibration frequencies, similar to how seismologists use earthquake waves.
- Compactness: the ratio of a star's mass to its radius, a measure of how strongly gravity compresses it.
- Equation of state (EOS): the relation between pressure and density that describes the matter inside the star.
- Nuclear saturation parameters: K0 (incompressibility of symmetric nuclear matter, how stiff it is to squeezing) and L (slope of the nuclear symmetry energy, how the energy cost of neutron-proton imbalance changes with density).
- Short gamma-ray burst precursors: brief high-energy flashes that may come just before a merger. · level: research-level

<details><summary>Original abstract</summary>

Owing to the elasticity of a neutron star, the shear and interface modes are excited, in addition to the fundamental, pressure, and gravity modes. While direct observations of the oscillation spectrum remain challenging, potential resonance signatures from these modes could be manifested in the precursors of short gamma-ray bursts from binary neutron star mergers. If the oscillation spectrum is observed, this is a good opportunity to extract the physical properties through the technique of asteroseismology. In particular, we focus on the crustal elasticity and examine the $s$- and $i$-mode frequencies. We find that, for a given EOS specified by the nuclear saturation parameters, the radius-scaled $s$-mode frequencies and the mass-scaled $i$-mode frequencies can be expressed as a function of the stellar compactness, independently of the stiffness of the core EOS, at least when the EOS in a higher-density region can be characterized only by the specific constant sound velocity. Then, we could derive the fitting formula for the $s_i$-mode for $i=1-4$ and $i_1$-mode frequencies as a function of the stellar compactness and the combination of the incompressibility of symmetric nuclear matter, $K_0$, and the slope parameter for the nuclear symmetry energy, $L$. If the $s$- and/or $i$-mode oscillation frequencies were observed, one may get the relation between these properties by identifying the observed frequencies with specific modes, using our fitting formula, which offers useful insights into the nuclear saturation parameters and stellar properties. By combining the other observational data, it may be possible to narrow the parameter space of EOS parameters and stellar properties. We emphasize that this article summarizes the results presented in our previous studies and discusses their implications for neutron star seismology.

</details>

### [Softer charged-hadron spectra in Ne+Ne than in O+O collisions at the same multiplicity at $\sqrt{s_{\rm NN}} = 5.36$ TeV](https://arxiv.org/abs/2611.32516)
*Kishora Nayak* · `nucl-ex` · arXiv:2611.32516v1 · relevance 0.07

- **In one sentence**: Compares ATLAS charged-hadron transverse-momentum spectra in O+O and Ne+Ne collisions at equal charged-particle multiplicity (rather than equal centrality), finding Ne+Ne spectra softer, and tests the same procedure on Xe+Xe and Pb+Pb.
- **In plain words**: Heavy-ion collisions at the Large Hadron Collider smash nuclei together and spray out many particles. This paper takes published measurements of oxygen-on-oxygen and neon-on-neon collisions and compares them when both have the same number of produced particles, instead of the same overlap "centrality" class. At equal particle counts, the neon-on-neon sprays are found to have a somewhat gentler energy distribution, with a lower average transverse momentum.
- **Why it matters**: It bears on whether the spread of particle energies in these tiny collisions is set by how many particles are made or by how large the fireball is, a question relevant to how the quark-gluon plasma forms in small systems. The text reports the effect with explicit statistical significance, but the interpretation (larger transverse area gives softer spectra) is only described as the expected ordering, so it should be read as a measured tendency rather than a settled explanation.
- **Background needed**: - Heavy-ion collisions: nuclei smashed together at high energy to create a hot, dense state of matter.
- Centrality: how head-on a collision is; more central collisions produce more particles.
- Multiplicity: the number of charged particles produced in one collision.
- Transverse momentum (pT): the sideways momentum of a particle relative to the beam; a spectrum shows how many particles occur at each pT.
- Mean pT: the average sideways momentum; a lower value means a "softer" spectrum.
- Stretch factor: a single scaling of the pT axis used to match one spectrum to another.
- Standard deviations (sigma): how many measurement uncertainties a difference is from no difference.
- Pseudorapidity: a measure of angle from the beam direction; "forward" means closer to the beam. · level: research-level

<details><summary>Original abstract</summary>

Charged-hadron spectra measured by the ATLAS Collaboration in O+O and Ne+Ne collisions at $\sqrt{s_{\rm NN}} = 5.36$ TeV are compared at the same charged-particle multiplicity instead of at the same centrality, to test whether the shape of the transverse-momentum spectrum at a given multiplicity depends on the size of the colliding system. At equal multiplicity, Ne+Ne collisions have a lower mean transverse momentum $\langle p_{\rm T}\rangle$ than O+O collisions. Without any spectral fit, the published $\langle p_{\rm T}\rangle$ values give a Ne+Ne/O+O ratio of 0.9822 at 3-4% centrality, 6.6 standard deviations below unity even if the O+O systematic uncertainties are taken as uncorrelated between centrality classes. At $0.4 < p_{\rm T} < 2$ GeV the Ne+Ne spectrum is described by the O+O spectrum with the transverse-momentum axis compressed by a single stretch factor, $\lambda_{\rm Ne/O} = 0.969$ in the 3-4% class. It lies 9.5 or 3.3 standard deviations below unity, depending on whether the common part of the O+O systematic uncertainties cancels between centrality classes. This ordering is expected if Ne+Ne collisions have a larger transverse area at the same multiplicity and a larger area gives a softer spectrum. The softening decreases towards peripheral collisions and is the same at forward pseudorapidity. In central collisions the spectral shape follows the centrality class more closely than the multiplicity. The same procedure is tested in Xe+Xe and Pb+Pb collisions.

</details>

## Quantum information and computing

### [On the concentration of the ambiguity function on centered balls](https://arxiv.org/abs/2611.31326)
*Fabio Nicola* · `math.FA` · arXiv:2611.31326v1 · relevance 0.20

- **In one sentence**: The paper proves that Gaussian functions maximize the L^2 concentration of the ambiguity function on every centered ball, up to time-frequency shifts and unimodular constants, using ideas from quantum information theory.
- **In plain words**: The paper studies a mathematical "fingerprint" of a signal, called the ambiguity function, which shows how a signal's time and frequency content overlap. It asks how tightly that fingerprint can be packed into a disk around the origin, and it shows that the bell-shaped Gaussian signal does this best, apart from trivial shifts and changes of phase.
- **Why it matters**: Results of this kind sharpen uncertainty principles, which limit how precisely a signal can be localized in time and frequency at once. The abstract says the proof draws on quantum information theory, which may be the more interesting link for readers in that area; the text provided is only the abstract, so the wider significance is not clear from it.
- **Background needed**: - Signal: a function of time (or of position), such as a sound wave or a radio pulse.
- Ambiguity function: a two-variable function built from a signal that measures how it correlates with shifted and frequency-modulated copies of itself; widely used in radar and signal analysis.
- Concentration on a ball: the fraction of the function's squared size (its L^2 energy) that lies inside a disk of a given radius centered at the origin.
- Gaussian: the bell-shaped function, which is the standard extremal example in uncertainty principles.
- Time-frequency shift: moving a signal in time or changing its frequency; these do not change how concentrated it is.
- Unimodular constant: a complex number of size one, i.e. a pure change of phase.
- Quantum information theory: the field studying information in quantum systems; the paper says its techniques were used in the proof. · level: research-level

<details><summary>Original abstract</summary>

We show that the Gaussian uniquely maximizes the $L^2$ concentration of the ambiguity function on every centered ball, up to time-frequency shifts and multiplication by a unimodular constant. The proof relies on ideas from quantum information theory.

</details>

### [Benchmarking Quantum Machine Learning for Power-System Attack Detection: Evaluation Choices Can Decide the Outcome](https://arxiv.org/abs/2608.15617)
*Md Rezwanul Islam, ASM Shihavuddin* · `cs.LG` · arXiv:2608.15617v2 · relevance 0.18

- **In one sentence**: A benchmark comparing two quantum and six classical detectors for power-grid cyberattacks finds that evaluation choices such as row-level versus file-level splits, and how attacks are generated, can change reported results more than the choice of model.
- **In plain words**: The paper looks at whether quantum machine learning can spot cyberattacks on electricity grids better than ordinary computer methods. The authors tested two quantum detectors and six classical ones on public attack datasets, giving each the same tuning effort. Their main point is that small decisions in how the test is set up, such as how data is split and how attacks are simulated, can flip the apparent winner, and on their data neither quantum detector was more accurate or more consistently robust than the classical ones.</plain>
<parameter name="why">Quantum machine learning is being proposed for critical infrastructure security, so claims about it need careful testing. The paper's warning that evaluation design can outweigh model choice applies to security benchmarking more broadly, though the results come from specific public datasets and a limited set of models.
- **Background needed**: - Machine learning detector: a program trained on labelled examples to flag attacks.
- Quantum kernel: a quantum-computed similarity measure used as part of a classifier.
- Macro-averaged F1: a score combining precision and recall, averaged equally over classes; 0.50 is chance for the two-class task described.
- White-box attack: an attacker who knows the model's internals and crafts inputs to fool it; transfer attack uses a substitute model's attacks; black-box attack has no internal access.
- Row-level versus file-level split: whether test rows come from the same recordings seen in training (which can inflate scores) or from entirely held-out files.
- Random label flips: deliberately corrupting some training labels to test robustness.
- Upper bound: because tree models have no gradient for gradient-based attacks, their attacked scores can only be stated as upper limits. · level: intermediate

<details><summary>Original abstract</summary>

Quantum machine learning is proposed to detect grid cyberattacks, but no study we could read tests quantum and classical detectors under white-box, transfer, and black-box attacks and random label flips in one protocol. We compare two quantum and six classical detectors on public grid-attack data under equal tuning budgets. Our main finding: evaluation choices can decide the outcome. On these data, seven choices each changed a reported result with model families fixed. Row-level splits inflate our best score by 0.31 macro-averaged F1 over held-out files, where matched-dimensionality classical and quantum models barely clear chance. Under its own white-box attack the quantum kernel's score falls from 0.56 to 0.01 (chance 0.50), while a transferred attack in the same run leaves 0.52. Trees admit no gradient-based white-box attack, so their attacked scores are upper bounds. These attack results use eight-dimension detectors under row-level splits. On gas-pipeline and simulated-grid data, neither quantum detector is more accurate or consistently more robust; three of the seven choices reproduce fully on gas data with one pressure feature log-scaled (two within noise), and none of the four checked on the grids does. Benchmarks should hold out whole files and give every model its own attack where possible. We release code and checklist.

</details>

## Optics and atomic physics

### [Integrated lasing and dual-band gain in neodymium-implanted silicon nitride](https://arxiv.org/abs/2611.32935)
*Jan de Haan, Arturo Fern\'andez Gamez, Nina Zdravkovi\'c et al.* · `physics.optics` · arXiv:2611.32935v1 · relevance 0.15

- **In one sentence**: Demonstrates neodymium-implanted LPCVD silicon nitride waveguide amplifiers with gain near 920 nm and 1100 nm, and a ring laser built on a 200 mm commercial wafer platform.
- **In plain words**: The paper concerns making small, chip-scale lasers that emit light near 1 micrometer, the infrared range used in quantum experiments, precision measurement, and sensing. The authors took standard silicon nitride optical circuits made on a commercial wafer line, implanted neodymium ions into selected chips, and built waveguide amplifiers and a ring-shaped laser from them. They report that the amplifiers boost light in two wavelength bands, around 920 nm and 1100 nm, and that the ring laser does lase.
- **Why it matters**: Getting light amplification and lasing on a chip with a rare-earth dopant that is compatible with a standard foundry-style process is a step toward cheaper, scalable on-chip light sources. The text does not report output power, efficiency, or linewidth, so its practical reach is not yet clear.
- **Background needed**: - Integrated photonics: light is guided in tiny waveguides etched on a chip, similar in spirit to electrical wiring on a microchip.
- Silicon nitride (LPCVD): a common, low-loss material for these waveguides, deposited in a furnace-style process.
- Rare-earth gain: certain elements (here neodymium) emit light when pumped with energy; adding them to a material lets it amplify light.
- Ion implantation: firing dopant ions into a material to place them at controlled depths and concentrations.
- Ring resonator: a looped waveguide that selects specific wavelengths; a laser built on one is a compact cavity.
- Amplifier vs. laser: an amplifier boosts an input signal; a laser adds feedback so it generates light on its own. · level: research-level

<details><summary>Original abstract</summary>

Lasers at wavelengths near 1 micrometer are used in quantum technologies, precision metrology, and sensing. Rare-earth gain at these wavelengths in photonic integrated circuits can reduce the size and enable the scalable fabrication of these lasers. We fabricate neodymium-based integrated waveguide amplifiers and a ring laser using neodymium-implanted LPCVD silicon nitride. The photonic integrated circuits were fabricated on a 200 mm commercial wafer platform, and individual dies were implanted with neodymium ions. We show that the amplifiers provide gain in two bands around wavelengths of 920 nm and 1100 nm, and we show lasing in a ring resonator. This demonstrates that neodymium-implanted LPCVD silicon nitride is a suitable gain material for integrated lasers.

</details>

### [Temporal Soliton Waves in Modern Fiber Laser Systems](https://arxiv.org/abs/2611.31799)
*Shilong Liu, Boris Malomed* · `physics.optics` · arXiv:2611.31799v1 · relevance 0.10

- **In one sentence**: A survey chapter reviewing theory, experiments, generation, characterization, and control of temporal soliton families (dissipative solitons, soliton molecules, and dispersion-managed solitons) in mode-locked fiber lasers.
- **In plain words**: This is an overview chapter about tiny, stable pulses of light that keep their shape while travelling through special glass-fiber laser setups. It collects the underlying theory, lab results, and methods for making, measuring, and steering these pulses, including newer approaches that use machine learning. The text describes the topics covered but does not present new experimental results of its own.
- **Why it matters**: Fiber lasers that produce such pulses are used in fields such as precision measurement and optical communications, so a consolidated review may help newcomers orient themselves. The text does not say how directly these results feed into any specific application.
- **Background needed**: - A laser "mode-locked" state emits light as a train of very short pulses, often lasting picoseconds or femtoseconds (trillionths or quadrillionths of a second).
- A "soliton" is a pulse that holds its shape because two effects, such as dispersion (colors spreading apart) and nonlinearity (light changing the glass), cancel out.
- "Dissipative solitons" depend on a balance of gain (light amplification) and loss, not only on the fiber's physics.
- "Soliton molecules" are several pulses locked together at fixed spacing, like a bound pair.
- "Dispersion-managed solitons" are pulses whose shape stretches and squeezes periodically along a cavity with alternating fiber types.
- Machine learning here means algorithms used to adjust or predict laser behaviour automatically. · level: research-level

<details><summary>Original abstract</summary>

This chapter provides a comprehensive survey of temporal soliton-wave in modern fiber systems. Temporal soliton waves constitute a broad class of nonlinear localized structures in modern fiber laser systems, arising from different balances among dispersion, nonlinearity, gain, loss, spectral filtering, and various forms of cavity coupling. We review the underlying theory, basic experimental findings, and practical methods for the generation, real-time characterization, and active control of soliton families, with a particular focus on recent progress reported for mode-locked fiber-laser platforms. The families covered in the chapter include dissipative solitons, soliton molecules (bound states), and dispersion-managed solitons. For each species, we focus on the pulse energy, duration, stationary and breathing states, and emerging intelligent (machine-learning-assisted) control strategies.

</details>

## Fluids and plasma

### [Toward divertor plasma detachment in pure D-T plasma in fusion reactor with H-mode-like plasma confinement](https://arxiv.org/abs/2611.31616)
*S. I. Krasheninnikov, R. D. Smirnov, M. V. Umansky* · `physics.plasm-ph` · arXiv:2611.31616v1 · relevance 0.09

- **In one sentence**: A theoretical estimate of the plasma density and heat-flux conditions under which a tokamak divertor can reach ultimate detachment in pure hydrogen-isotope plasma while keeping H-mode confinement, checked against present-day machines and AUG data.
- **In plain words**: Fusion reactors must get rid of intense heat at the edge of the hot plasma without damaging the walls. One way is "detachment," where the plasma cools down in front of the exhaust plate (the divertor). This paper works out the conditions for reaching this cooled state in pure deuterium-tritium plasma while keeping the good-confinement mode (H-mode). The estimates fit some current tokamaks and the AUG data, but for ITER, ARC and EU-DEMO they suggest the required density would be above the empirical density limit.
- **Why it matters**: Divertor heat handling is a central obstacle for future fusion power plants, so the gap it identifies between present machines and reactors matters. The text names possible remedies (operating above the density limit, turbulence-broadened heat flux, reduced parallel heat flux in long-leg divertors) but only outlines them, so their feasibility is not established here.
- **Background needed**: - Tokamak: a doughnut-shaped magnetic-confinement device for fusion.
- H-mode: a high-confinement operating regime with better energy containment.
- Divertor: the region where exhaust heat and particles are directed onto plates.
- Scrape-off layer and separatrix: the thin edge layer outside the confined plasma, and the boundary between the two.
- Detachment: the plasma cools and detaches from the divertor plates, reducing heat load.
- Empirical density limit: an observed density above which plasma performance degrades.
- D-T plasma: a mix of deuterium and tritium, the fuel for fusion reactors.
- ITER, ARC, EU-DEMO: planned or proposed fusion devices. · level: research-level

<details><summary>Original abstract</summary>

The conditions between the separatrix plasma density and the heat flux into the scrape-off layer region allowing reaching an ultimate divertor plasma detachment with H-mode confinement in pure hydrogen (deuterium or the mixture of deuterium and tritium) plasma are obtained. Estimates for a number of present-day tokamaks show that this regime is accessible at separatrix plasma densities below or around the empirical density limit. Moreover, they are in reasonable agreement with the data from the AUG tokamak, where detachment was reached in pure deuterium plasma. However, in future reactors, such as ITER, ARC, and EU-DEMO, it would require densities exceeding this empirical density limit. Therefore, additional measures are needed for future reactors, such as operation above the density limit, which, according to recent experimental data, may not be a hard operational boundary, turbulence induced broadening of the heat flux width and reduction of the parallel heat flux in the long legs of advanced divertor configurations. Their successful implementation would open the possibility for a more efficient reactor design.

</details>

### [The effects of closure parameter on the properties of kinetic range plasma turbulence](https://arxiv.org/abs/2611.31769)
*Jago V. H. Edyvean, Andrea F. Irwin, Tulasi N. Parashar* · `physics.plasm-ph` · arXiv:2611.31769v1 · relevance 0.09

- **In one sentence**: A study of how the free "closure parameter" in a 10-moment fluid model of plasma (the solar-wind-like medium) changes heating between ion and electron species and the compressive versus incompressive parts of kinetic-range turbulence, across artificial ion-electron mass ratios.
- **In plain words**: Space plasmas such as the solar wind are too collisionless to model perfectly with simple fluid equations, and full particle-by-particle simulations are too expensive for large regions. This paper uses a middle-ground fluid model, the 10-moment model, which needs an approximation for heat flow; that approximation contains an adjustable number called the closure parameter. The authors vary this number and the ion-to-electron mass ratio to see how it changes how energy is shared between ions and electrons in turbulence.
- **Why it matters**: The sharing of turbulent heating between ions and electrons is a central question for understanding how the solar wind heats up, so the finding that the modelling choice alone shifts these heating rates matters for trusting such simulations. The text reports that the effect persists at realistic mass ratios, though it weakens as the ratio approaches realistic values; the broader implications beyond this model are not stated in the text.
- **Background needed**: - Plasma: a gas of charged particles (ions and electrons) that carries magnetic fields.
- Turbulence: chaotic, swirling fluctuations that cascade energy from large to small scales.
- Kinetic range: small scales where particle motion, not just fluid flow, matters; collisions are too rare for simple fluid behaviour.
- Fluid moments: averaged quantities (density, velocity, pressure, heat flux) used to describe a plasma; the 10-moment model keeps moments up to the pressure tensor and must approximate higher ones (the heat flux) to close the equations.
- Closure parameter: the adjustable constant in that approximation.
- Compressive vs incompressive heating: energy going into density/pressure changes versus into swirling, divergence-free motions.
- Mass ratio: ion mass divided by electron mass; realistic is about 1836 for hydrogen, and simulations often use smaller artificial values. · level: research-level

<details><summary>Original abstract</summary>

Simulations of plasmas such as the solar wind require an accurate representation of kinetic physics given the lack of frequent collisions. Fully kinetic treatments are computationally expensive and necessarily confine simulations to small domain sizes. A good compromise is to utilise higher-order fluid-moment models such as the 10-moment model. This model retains all physics up to the second moment, with the moment hierarchy closed by approximating the heat flux. One choice is to use a model for the divergence of the heat flux, $\partial_m q_{ijm} \approx v_t |k_0|(\mathbf{P}_{ij}-p\delta_{ij})$, with a free parameter $k_0$, called the ``closure parameter''. We study the effects of this closure parameter on the properties of turbulence, combined with artificial ion-electron mass ratios. We show that the heating of the two plasma species is affected by the choice of the closure parameter. For all combinations of closure parameters, the relative compressive and incompressive heating rates are affected even for realistic mass ratios. The effects are more prominent for lower mass ratios and diminish when approaching realistic mass ratios.

</details>

## Biological physics

### [Geometry and topology of DNA defects](https://arxiv.org/abs/2611.32850)
*A. Fassino, E. Carlon, D. Marenduzzo* · `cond-mat.soft` · arXiv:2611.32850v1 · relevance 0.09

- **In one sentence**: The paper defines a geometric order parameter (a backbone-to-base polar vector plus a base-orientation quaternion) to classify DNA defects into flip, stacking, and composite types, and tests it on real DNA structures and biased atomistic simulations.
- **In plain words**: DNA is normally a tidy double helix, but damage, proteins binding to it, or enzymes such as RNA polymerase can locally disturb how its building blocks sit. This paper offers a precise way to describe these local disturbances using geometry, and checks it against real DNA structures and computer simulations. It reports three kinds of defect: a flip of the direction of a strand's backbone-to-base arrow, a stacking defect where bases shift out of their neat layering, and a combination of both.
- **Why it matters**: The text says all three defect types appear in realistic DNA structures and have functional relevance, and that the approach might extend to RNA and nucleosome arrays. Whether this becomes a standard tool depends on follow-up work the text does not show.
- **Background needed**: - DNA is a double helix; each strand has a sugar-phosphate backbone with a base attached.
- Bases stack on top of each other inside the helix, and this stacking helps hold the structure together.
- A "defect" here means a local departure from the normal regular geometry.
- A quaternion is a compact mathematical way to describe 3D orientation (rotation), used here for how a base is oriented.
- Atomistic molecular dynamics simulates every atom's motion over time; "biased" simulations push the molecule in a chosen direction to force deformations.
- Nucleosomes are DNA wrapped around protein spools, which package the genome. · level: research-level

<details><summary>Original abstract</summary>

DNA defects arise frequently, either as a result of damage, protein binding or the action of molecular enzymes such as an RNA polymerase. Here we combine geometry, atomistic simulations and an analysis of real DNA structures to provide a quantitative characterisation of DNA defects and their dynamics. The composite order parameter describing defects geometrically is a backbone-to-base polar vector, together with a quaternion capturing 3D base orientation in a single strand. There are three types of defects: flips of the polar vector, stacking defects of bases, and composite defects encompassing both. All types of defects feature in realistic structures for DNA and have functional relevance. Additionally, biased molecular dynamics simulations of DNA with an imposed elastic deformation form flip or stacking defects whose abundance and dynamics strongly depend on sequence and type of deformation. Our results provide a link between geometry and biochemistry, and could also be applied, for instance, to identify defects in RNA molecules and nucleosome arrays.

</details>

### [Lattice models of chiral random motion: A short review](https://arxiv.org/abs/2611.32743)
*E. Kalz, J. Wojcik, N. Sherf et al.* · `cond-mat.stat-mech` · arXiv:2611.32743v1 · relevance 0.06

- **In one sentence**: A short review that recasts several lattice random-walk models with a rotational bias (chiral walks) as one framework, using an internal state for the walker as the carrier of memory, and surveys their effects on diffusion, edge transport, and self-avoiding paths.
- **In plain words**: This paper reviews computer models of random movement on a grid, where the walker has a built-in tendency to turn one way, as seen in swimming bacteria, spinning particles, and charges moving in magnetic fields. The authors argue that on a grid this sideways bias only works if the walker remembers its recent direction, and they use a recently proposed chiral walk model as a template to bring several earlier, separately developed models together. The text describes where this memory shows up: in the surrounding environment, in the path the walker traces, and in the transport along edges.
- **Why it matters**: The review ties together lattice models that have been introduced in different fields since 1960 without a shared language, which may help researchers working on active matter, odd transport, and programmable robots see common structure. The text is a review and does not itself report new experimental results, so its practical impact is best judged by the cited literature.
- **Background needed**: - Random walk: a path built from repeated random steps; its spread grows with the number of steps.
- Diffusion tensor: a table of numbers describing how spreading differs by direction; an "antisymmetric" part means a sideways, swirling component.
- Chirality: a handedness, a systematic tendency to turn one way (like a left or right hand).
- Odd transport: transport that gains a sideways (Hall-like) component, with currents that flow across rather than only along gradients.
- Lattice model: movement restricted to grid points, which makes it exactly solvable on paper and easy to simulate.
- Memory: the walker's dependence on its previous step or internal state, which the review argues chirality requires on a lattice.
- Run-and-tumble: motion alternating between straight runs and random reorientations, as in E. coli.
- Self-avoiding walk: a path that never revisits a site. · level: research-level

<details><summary>Original abstract</summary>

Chirality, a systematic rotational bias, is ubiquitous in many random motion patterns, from bacteria cells, that swim in circles near surfaces and spinning colloids, to charged particles diffusing under the influence of magnetic fields. In two dimensions, chirality renders random transport \textit{odd}: the diffusion tensor acquires an antisymmetric part that leaves the mean-squared displacement invariant but modifies fluxes and boundary currents. Lattice models for random motion are a natural setting to study chirality, since they are exactly solvable, connect directly to heterogeneous media, cellular automata, and programmable robots, and in discrete time admit fully chiral limits with a localised bulk and edge transport. Lattice walks with a rotational bias have been introduced in different communities several times since 1960, yet without a common language or conceptual connection between them. Here we review these models from the perspective that on the lattice, chirality requires memory. Taking the recently introduced chiral random walk model as a template, we describe the walker with an internal degree of freedom. With a chiral biased updating rule, the full diffusion tensor of this chiral walker turns odd. Within this picture, we can unite persistent and chiral walks, run-and-tumble motion, and cyclic random motions in one framework. We discuss how the memory is followed into the environment; in Lorentz lattice gases, kinetic and rotor walks, and random odd environments; and into the path; in spiral self-avoiding walks.

</details>

## Climate, atmosphere and Earth

### [Evaluation of Machine-Learning Weather Models in Reproducing Mesoscale Tornado-Favorable Convective Environments](https://arxiv.org/abs/2611.31564)
*Yiding Luo (University of Washington), Rui Yuan (University of Washington), Shetian Xia (University of Washington) et al.* · `physics.ao-ph` · arXiv:2611.31564v1 · relevance 0.14

- **In one sentence**: This paper benchmarks three machine-learning weather models (Pangu-Weather, FengWu v1/v2, FuXi Weather) on tornado-favorable convective parameters for ten strong-tornado events in Oklahoma, using reanalysis data as input and ground truth across lead times of 24 to 168 hours.
- **In plain words**: Some tornadoes form when the air near the ground is warm and humid and the winds change speed and direction with height. This study asks whether newer AI-based weather forecasting models can reproduce those conditions for ten past tornado outbreaks in Oklahoma. The authors found that performance depended on the weather variable, the model, and the event, and that forecasts lost accuracy for extreme values and fine spatial detail as the lead time grew.
- **Why it matters**: AI weather models are already used operationally and are cheap to run, so checking whether they capture the specific ingredients of tornado-prone weather matters for severe-weather forecasting. The text does not show direct effects on warnings or public safety, so the practical impact remains uncertain.
- **Background needed**: - Numerical weather prediction (NWP): forecasts made by solving physics equations on a computer grid, the traditional approach.
- Machine-learning (ML) weather models: neural networks trained on past atmospheric data to forecast the weather; much cheaper to run than NWP.
- Grid spacing (0.25 degrees): the distance between points in the model's map, roughly 25 km; coarse grids can miss small features.
- Reanalysis data: a gridded historical record that blends observations with a model, used here as the "truth" to compare against.
- Lead time: how far ahead the forecast goes (here 1 to 7 days).
- Convective parameters: measurable quantities such as storm-relative helicity (a measure of rotation potential in the wind) and thermodynamic variables (temperature and moisture) that indicate whether storms can form and rotate.
- Cold pool: a pocket of cool air spreading out from a storm, a fine-scale feature. · level: research-level

<details><summary>Original abstract</summary>

Machine-learning (ML)-based weather prediction models have developed rapidly in recent years and are already being used in operational weather forecasting. These ML-based models' performance has exceeded that of traditional numerical weather prediction (NWP) methods in certain implementations, with substantially lower computational cost. However, most ML-based models were trained on global data at a horizontal grid spacing of 0.25 degrees, which may be too coarse to capture tornado-favorable parameters. The ability of these ML-based models to predict the parameters relevant for tornado-favorable convection remains unclear. Here, we compare the performance of three ML-based models, Pangu-Weather, FengWu (versions 1 and 2), and FuXi Weather, in forecasting ten distinct convective events associated with strong tornadoes that occurred in Oklahoma, USA. The proposed methodology incorporates five lead times, ranging from 24 to 168 h, for each event and uses reanalysis data as both model input and ground truth. We evaluate the models by forecasting eight tornado-relevant parameters and by conducting spatial and value-consistency checks between model outputs and ground truth. Performance varies across parameters, models, and events. Pangu-Weather performs well for positive storm-relative helicity, while FuXi Weather performs well for several thermodynamic parameters, albeit with some overprediction of magnitude. Increasing lead time is associated with loss of extreme-value and spatial-structure fidelity. In the Global Forecast System (GFS) case study, ML-based models retain convective signals at longer lead times but poorly represent fine-scale structures such as cold pool-like features. These findings indicate that model-specific biases and spatial extremes should be assessed alongside domain-wide forecast scores.

</details>

### [Critical ocean physics on the edge of AMOC instability](https://arxiv.org/abs/2611.31448)
*Reyk B\"orner, Anna S. von der Heydt, Robbin Bastiaansen et al.* · `physics.ao-ph` · arXiv:2611.31448v1 · relevance 0.08

- **In one sentence**: In a 1-degree global ocean model, the authors compute an unstable saddle equilibrium (an "AMOC edge state") that marks the boundary between AMOC recovery and collapse, and find that the regional net surface buoyancy flux tracks the onset of tipping.
- **In plain words**: The Atlantic overturning circulation, a large system of ocean currents that carries warm water north and cold water south, is expected to weaken as the planet warms. This paper asks whether that weakening will recover on its own or tip into a collapse that does not reverse. The authors locate the dividing line between those two outcomes in a global ocean model and study the balanced state that sits on that line.
- **Why it matters**: Whether the overturning circulation can recover or will tip into collapse matters for projections of climate in the Atlantic region. The paper suggests a possible early-warning signal, the regional net surface buoyancy flux (a measure of how much the surface water is becoming denser or lighter), but the text reports this from one model, so how well it transfers to other models or to the real ocean is not established here.
- **Background needed**: - The AMOC is a large-scale overturning current in the Atlantic; it moves heat northward and is driven by water getting denser and sinking, mainly in the far North Atlantic.
- A "tipping transition" is a shift that, once triggered, continues on its own rather than reversing when the cause eases.
- A "saddle equilibrium" is a balanced state that is unstable: a small push sends the system toward either recovery or collapse, so it sits on the boundary between them.
- Surface buoyancy flux is the net effect of heating/cooling (thermal) and evaporation/rain/ice melt (haline, related to salt) on how dense surface water is.
- Freshwater and heat balances are accounting of how much fresh water and heat enter or leave a region.
- A global ocean model at 1-degree resolution is a computer simulation dividing the ocean into grid cells about 100 km across. · level: research-level

<details><summary>Original abstract</summary>

The Atlantic Meridional Overturning Circulation (AMOC) is expected to weaken under global warming, but whether this signifies a transient response or a tipping transition remains unclear. Distinguishing between these cases requires a physical understanding of the boundary separating ocean states leading to AMOC recovery from those leading to collapse. In a global ocean model with 1{\deg} resolution, we compute an AMOC edge state -- an unstable saddle equilibrium that anchors this instability boundary. The edge state maintains weak overturning sourced by marginal deep water formation in the Nordic Seas. Analyzing the North Atlantic freshwater and heat balances that govern the edge state dynamics, we show that near the edge state, thermal and haline components of the surface buoyancy flux approximately compensate. Surface buoyancy loss (gain) coincides with AMOC recovery (collapse). Our findings support using the regional net surface buoyancy flux as an indicator for the onset of AMOC tipping.

</details>

## Cosmology

### [Learning to find cosmic filaments with graph neural networks](https://arxiv.org/abs/2611.31494)
*Alexis Tastet, Daniela Gal\'arraga-Espinosa, Leander Thiele* · `astro-ph.CO` · arXiv:2611.31494v1 · relevance 0.17

- **In one sentence**: A generative model built from flow matching and graph neural networks learns to produce probabilistic maps of cosmic filaments conditioned on sparse galaxy tracers, reproducing key statistics of the target filament distribution.
- **In plain words**: Galaxies are spread through space in a web-like pattern, with long thread-like filaments linking dense clusters. The paper asks how to estimate where these filaments are from a sparse set of galaxy positions, where the answer is always uncertain. The authors train a machine-learning model that generates many possible filament layouts, rather than a single best guess, and report that these layouts match key statistical properties of the target filaments.
- **Why it matters**: Mapping the cosmic web from galaxy surveys matters for understanding how matter is distributed on the largest scales. The text presents this as a first step toward probabilistic inference directly from survey data, and the approach may also apply to other sparse-tracer reconstruction problems, though the text does not test those.
- **Background needed**: - Cosmic web: the large-scale network of galaxies, filaments, walls and voids in the Universe.
- Galaxy survey: a catalog of galaxy positions in 3D space, which is discrete and incomplete.
- Filament: a thread-like structure of matter linking galaxy clusters.
- Generative model: a model that learns a data distribution and produces new samples from it.
- Flow matching: a training method that learns to transform random noise into realistic samples.
- Graph neural network: a neural network that operates on nodes and connections, suited to networks of points.
- Probabilistic inference: estimating a range of plausible answers with their likelihoods, not one fixed answer. · level: research-level

<details><summary>Original abstract</summary>

Inferring the large-scale structure of the Universe from galaxy surveys is a fundamental challenge in cosmology. In particular, cosmic filaments form an extended and geometrically complex network whose underlying structure cannot be reconstructed from discrete galaxy catalogs without uncertainty. We investigate a generative approach to filament finding based on flow matching and graph neural networks. The learned model reproduces key statistical properties of the target filament distribution while generating a distribution over possible filament configurations, demonstrating its ability to model uncertainty. Our work provides a first step towards probabilistic inference of the cosmic web directly from galaxy surveys. More broadly, these results demonstrate the potential of conditional generative models for reconstructing filament-like structures from sparse observational tracers.

</details>

### [Resolving the Hubble Tension at $0.1\sigma$ with Early Dark Energy: Key Role of the Highest-redshift Galaxies from JWST Observations](https://arxiv.org/abs/2611.32552)
*Guo-Hong Du, Tian-Nuo Li, Jing-Fei Zhang et al.* · `astro-ph.CO` · arXiv:2611.32552v1 · relevance 0.15

- **In one sentence**: This paper reports that an axion-type early dark energy model, fit to CMB and DESI BAO data plus JWST high-redshift galaxy UV luminosity functions, yields H0 = 72.76 ± 1.00 km/s/Mpc consistent with SH0ES at 0.1σ, and that allowing running of the spectral index raises H0 further to 73.75 ± 1.04 km/s/Mpc.
- **In plain words**: The universe seems to expand at two different rates depending on how it is measured: nearby stars and galaxies give a faster rate than the early-universe afterglow (the cosmic microwave background). This paper tests a proposed extra ingredient, "early dark energy," that briefly changes the early universe, and finds that galaxy counts from the James Webb Space Telescope (JWST) in the very distant, early universe help bring the two rates into agreement. The authors also report that adding a small extra tilt to how structure size varies pushes the inferred rate slightly above the nearby measurement.
- **Why it matters**: The Hubble tension is one of the most discussed open problems in cosmology, and this paper suggests early-universe galaxy observations could be relevant to it. However, the result depends on modelling choices (reference cosmologies used by JWST analyses, and a model extension with running of the spectral index), so it should be treated as one proposed resolution under test rather than a settled answer.
- **Background needed**: - Hubble constant (H0): the present expansion rate of the universe, in km/s per megaparsec.
- Hubble tension: local measurements (e.g. SH0ES, about 73) disagree with values inferred from the early universe via the cosmic microwave background (about 67-68).
- Early dark energy (EDE): an extra component that acts briefly just before recombination, shifting the inferred expansion rate; the "axion" version is one specific model.
- CMB (cosmic microwave background): the faint light left from about 380,000 years after the Big Bang.
- BAO (baryon acoustic oscillations): a preferred clustering scale in galaxy maps used as a cosmic ruler; DESI is a survey that measures it.
- JWST UV luminosity function: counts of galaxies at different brightnesses in ultraviolet light, used here to probe galaxies at redshift z of about 11-12.5, roughly 400 million years after the Big Bang.
- Spectral index n_s and running alpha_s: describe how the strength of primordial density fluctuations varies with physical scale; running is the scale-dependence of that variation.
- sigma (σ): a measure of statistical tension; 0.1σ means the values agree very closely. · level: research-level

<details><summary>Original abstract</summary>

We show that the Hubble tension can be resolved at the $0.1\sigma$ level within the early dark energy (EDE) framework, with the highest-redshift galaxies from the JWST observations playing a key role. By accounting for the reference cosmologies of the JWST ultraviolet luminosity function measurements and combining them with cosmic microwave background (CMB) and DESI baryon acoustic oscillation data, we obtain $H_0=72.76\pm1.00~\mathrm{km\,s^{-1}\,Mpc^{-1}}$ in the axion EDE model, in excellent agreement with SH0ES at the $0.1\sigma$ level. We find that the enhanced galaxy abundances at $z=11$ and $12.5$ play a key role in driving this result. These observations favor stronger small-scale matter power, which can be accommodated by increasing the primordial scalar spectral index $n_{\rm s}$. Under the CMB constraints, the positive correlations among $n_{\rm s}$, $f_{\rm EDE}$, and $H_0$ lead to a higher inferred $H_0$. Allowing additional scale dependence in the primordial power spectrum through $\alpha_{\rm s}$ yields a positive running at more than $4\sigma$, further increasing $H_0$ to $73.75\pm1.04~\mathrm{km\,s^{-1}\,Mpc^{-1}}$, with its value even exceeding the SH0ES measurement. These results reveal how high-redshift small-scale structure observations influence the inferred $H_0$ through the interplay between the primordial power spectrum and EDE parameter degeneracies.

</details>

## Galaxies

### [Euclid: Discovery of a quasar at z = 8.13 hosting a 360-million-solar-mass black hole](https://arxiv.org/abs/2611.31385)
*J. Wolf, S. Belladitta, D. Yang et al.* · `astro-ph.GA` · arXiv:2611.31385v1 · relevance 0.19

- **In one sentence**: Discovery and spectroscopic confirmation of the quasar EUCL J150452.291+625224.39 (J1504+6252) at z = 8.129, the first quasar confirmed at z > 8, with black hole mass and Eddington-ratio estimates from H-beta and Mg II broad lines.
- **In plain words**: This paper reports a very distant quasar, a bright object powered by a supermassive black hole, seen as it was about 630 million years after the Big Bang. The object was spotted in Euclid survey images and then confirmed with several telescopes, including JWST. The authors estimate the black hole weighs a few hundred million times the Sun's mass, while it is currently feeding on gas at a rate below its maximum.
- **Why it matters**: It pushes the known redshift record for quasars back by about 39 million years and suggests that more massive black holes from this early era may exist unseen. Whether it changes how black holes form is not settled by the text; it says the object needs either a heavy starting seed or unusually efficient early growth.
- **Background needed**: - Redshift (z): how much light from a distant object is stretched to longer wavelengths by cosmic expansion; larger z means further away and earlier in time. z = 8.13 is roughly 630 million years after the Big Bang.
- Quasar: a very luminous core of a galaxy powered by a supermassive black hole swallowing surrounding gas.
- Broad emission lines: bright spectral lines from fast-moving gas near the black hole; their width (FWHM) is used to estimate black hole mass.
- Mass estimates: these rely on empirical calibrations between line width, brightness and mass, so they carry large uncertainties (here about 0.4 dex, a factor of roughly 2.5).
- Eddington ratio: the current accretion rate relative to the maximum rate a black hole can sustain; "sub-Eddington" means feeding below that limit.
- Reionisation era: the period when the first luminous objects ionised the hydrogen fog filling the early universe.
- Euclid, JWST, Keck, HST, LBT: telescopes and surveys used for the discovery and follow-up. · level: research-level

<details><summary>Original abstract</summary>

Quasars powered by rapid accretion onto supermassive black holes (SMBHs) have been uncovered deep into the first gigayear of cosmic history. We present the discovery of EUCL J150452.291+625224.39 (J1504+6252), selected from Euclid Wide Survey imaging and spectroscopically confirmed as the first quasar at z > 8 through observations with Keck, HST, LBT, and JWST. J1504+6252 exhibits the defining spectral signatures of archetypal quasars at lower redshift, including a luminous blue power-law continuum and broad permitted emission lines, indicating a classical broad-line region. JWST/NIRSpec G395M spectroscopy yields a systemic redshift of z = 8.129 +/- 0.005, corresponding to 630 Myr after the Big Bang and shifting the quasar redshift frontier by about 39 Myr (6% of the age of the Universe at that epoch). From H-beta and Mg II, we measured intrinsic broad-line-region FWHM of 3160 +/- 270 and 3740 (+160/-170) km/s, respectively. A widely used single-epoch H-beta calibration gives a reference black hole mass of log10(MBH/Msun) = 8.56 +/- 0.43. Applying a range of calibrations to both Mg II and H-beta yields log10(MBH/Msun) = 8.33-8.89 and Eddington ratios of 0.12-0.44. Assembling a black hole of several hundred million solar masses within the first few hundred million years, despite its currently sub-Eddington accretion rate, requires either a massive seed or sustained, highly efficient early growth. The discovery of a mature, sub-Eddington quasar at z > 8 suggests that substantially more luminous quasars hosting similarly massive black holes may remain to be discovered. Conversely, previously known reionisation-era quasars may represent the rapidly accreting end of a broader population of already massive black holes spanning a wider range of accretion states.

</details>

### [Tidally Induced Coda: Double Transients from Black Hole-Star Binary Encounters with Massive Black Holes](https://arxiv.org/abs/2611.31361)
*Konstantinos Kritos, Rosalba Perna* · `astro-ph.HE` · arXiv:2611.31361v1 · relevance 0.12

- **In one sentence**: Few-body scattering simulations (SpaceHub) of stellar-mass black hole–star binaries passing near a massive black hole, quantifying outcomes including a tidally triggered micro-tidal disruption event and fitting formulae for its cross section and the delay between two flares.
- **In plain words**: This paper looks at what happens when a pair of objects, a stellar-mass black hole orbiting a normal star, flies close to a much heavier black hole at the centre of a galaxy. The gravity of the heavy black hole can stretch the pair's orbit into a very elongated shape, which may cause the star to be torn apart by its black hole partner. The authors ran many computer simulations to estimate how often each outcome happens and how long apart two resulting flashes of light would appear.
- **Why it matters**: The paper proposes that such events would show up as two flares separated by months, which could serve as a distinctive signature to look for in surveys. The abstract's estimated event rates (a few to about 100 per year within 40 Gpc) are model predictions that depend on the simulation assumptions, so they should be read as estimates rather than confirmed numbers.
- **Background needed**: - Massive black hole (MBH): a black hole with millions to billions of times the Sun's mass, typically at a galaxy's centre.
- Stellar-mass black hole: a black hole formed from a collapsed massive star, a few times to tens of times the Sun's mass.
- Binary: two objects orbiting each other under mutual gravity.
- Eccentricity: how stretched an orbit is; 0 is a circle, near 1 is a very long thin ellipse.
- Tidal disruption event (TDE): a star torn apart by the gravity of a black hole, producing a flash of light. The "micro" version here involves a stellar-mass black hole doing the tearing.
- Few-body scattering experiment: a numerical simulation of a small number of gravitating bodies interacting at close range.
- Cross section: an effective target area describing how likely an interaction is. · level: research-level

<details><summary>Original abstract</summary>

Dense stellar environments surrounding massive black holes (MBHs) provide a natural setting for dynamical interactions that can produce transient electromagnetic and gravitational-wave sources. In particular, the tidal field of an MBH can strongly perturb binaries undergoing close encounters with it, driving their internal orbits to extreme eccentricities. Here, we investigate the outcomes of such interactions for binaries composed of a stellar-mass black hole (BH) and a star. Using direct few-body scattering experiments with the code SpaceHub, we explore hyperbolic encounters between BH-star binaries and MBHs. We systematically quantify the probabilities of different dynamical outcomes as functions of the binary orbital parameters and MBH mass, with particular emphasis on a channel in which the tidally induced eccentricity triggers a micro-tidal disruption event ($\mu$TDE), as the star is disrupted by its BH companion, followed by accretion of the stellar debris onto the MBH. We derive fitting formulae for the $\mu$TDE cross section and for the time delay between the two resulting flares, finding that the latter can be a few months for an MBH of $10^6\,M_\odot$. These double transients offer a distinctive observational signature of $\mu$TDEs. We estimate event rates ranging from a few to $\sim 100\,{\rm yr}^{-1}$ within a luminosity distance of $40\,{\rm Gpc}$.

</details>

## Exoplanets and planetary science

### [From residuals to warps: Probing disk geometry with gas kinematics](https://arxiv.org/abs/2611.31408)
*C. N. Kimmig, G. P. Rosotti, A. J. Winter et al.* · `astro-ph.EP` · arXiv:2611.31408v1 · relevance 0.17

- **In one sentence**: Using CO gas velocity residuals from a Keplerian disk model, the authors test when radiative-transfer mock observations can recover the three-dimensional warp shape of protoplanetary disks, and where the method fails.
- **In plain words**: This paper asks how to measure the tilt and twist of young, planet-forming disks of gas and dust around newborn stars. The authors simulated disks with a built-in warp, made synthetic ALMA maps of carbon monoxide gas emission, and checked whether a fitting method could recover the true warp from how the gas moves. They found the warp can be recovered for nearly face-on disks with slight misalignments of a few degrees, but the method breaks down for steeper disks (inclination above 40 degrees), high emission layers, and sharp warp transitions.
- **Why it matters**: Warps are suggested by shadows seen in many disks, and their shape bears on how disks evolve and why they bend. The work sets out the conditions under which a kinematic method can be trusted, which matters for interpreting future observations, though the text does not show that the method has been applied to real data.
- **Background needed**: - Protoplanetary disks: rotating disks of gas and dust around young stars, where planets may form.
- Warp: a bend or tilt in a disk, so its orientation changes with distance from the star.
- Keplerian disk model: the standard model in which gas orbits the star with speed set by gravity; deviations from it reveal extra motion or tilt.
- Inclination and position angle: how tilted the disk is toward our line of sight, and the direction of its tilt on the sky.
- Shadowing: dark regions cast on the outer disk by an inner warped part, used as evidence for warps.
- CO rotational line emission: radio light from carbon monoxide molecules, observed with ALMA, that traces gas motion.
- Radiative transfer simulation: a computer calculation of how light travels through and is emitted by a model object.
- Spectral resolution: how finely velocity is sampled in the data (here, down to 0.8 km/s). · level: research-level

<details><summary>Original abstract</summary>

Evidence of shadowing among protoplanetary disks suggests that warped protoplanetary disks are widespread, making it crucial to constrain their three-dimensional shape in order to understand their dynamical evolution and origin. Yet, inferring this warp shape from observations is challenging, as the typical signatures of a warp, especially shadows, are often degenerate with the warp shape. Kinematics of disks may provide a method to recover the shape by interpreting the residuals from a Keplerian disk model as local changes in inclination and position angle. In this work, we test its applicability and limitations. We perform radiative transfer simulations of disks with a parametrized warp shape to create synthetic maps of $^{12}\mathrm{CO}$ rotational line emission at ALMA wavelengths and compare the fitted warp with the true warp shape. We find that the warp shape can be recovered for nearly face-on disks with small warp misalignments of a few degrees, even without knowledge about disk properties such as emission height. The overall warp shape remains traceable even at moderate spectral resolutions up to $0.8\,\mathrm{km/s}$. However, we identify regimes where the method breaks down, including disks with an inclination higher than $40^\circ$, a high emission height of the tracer, and sharp warp transitions. In addition, radial and vertical motions can introduce apparent warps and twists, motivating extensions of the method to account for these effects.

</details>

### [Kepler-404: A near-resonant pair of sub-Neptunes. Reinterpreting a false-positive signal with the novel detection method RIVERS.radon](https://arxiv.org/abs/2611.32298)
*Yannick Eyholzer, Marylyn Rosenqvist, Adrien Leleu et al.* · `astro-ph.EP` · arXiv:2611.32298v1 · relevance 0.09

- **In one sentence**: The paper shows that transit timing variations can hide low signal-to-noise planets from standard searches, introduces the RIVERS.radon 2D cross-correlation method, and uses it to re-identify a false-positive Kepler signal as a planet in a near-5:4 resonance with a companion, with a photodynamical fit giving radii, masses and orbit-plane constraints.
- **In plain words**: Planets are often found by watching for small, regular dips in a star's brightness when a planet passes in front of it. Gravitational tugs from neighbouring planets can shift these dips around, so a standard search may miss weak signals. This paper presents a new search method that does not assume the dips are perfectly regular, and uses it to show that a signal previously labelled a false alarm around the star Kepler-404 is in fact a real planet.
- **Why it matters**: Pairs of planets locked in near-resonant orbits are expected to be common, yet few have been observed, and this work suggests detection bias may be part of the reason. The reported result, a pair of similar small planets with lower-than-typical densities, is a single-system case study, so its wider significance rests on whether the method finds other hidden planets.
- **Background needed**: - Transit method: a planet is detected when its orbit carries it in front of its star, causing a small periodic dimming in the light curve.
- Signal-to-noise ratio (S/N): how strong a signal is compared with random background fluctuation; weak signals are easily missed.
- Transit timing variations (TTVs): shifts in when transits occur, caused by gravitational interactions between planets.
- Resonance (e.g. 5:4): two planets whose orbital periods form a ratio of small whole numbers, so they tug on each other regularly.
- Sub-Neptunes: planets with radii between Earth's and Neptune's.
- False positive: a signal that looks like a planet but is caused by something else, such as an eclipsing binary star.
- Photodynamical fit: a model fitting the light curve together with the gravitational dynamics of the planets to estimate their masses and radii.
- Density: mass divided by volume; lower density suggests a larger share of light gases or a different composition. · level: research-level

<details><summary>Original abstract</summary>

According to the current understanding of planet formation and evolution, (near)-resonant systems should be a common occurrence in nature. However, pairs of planets with period ratios close to commensurability are rarely observed. In this paper, we discuss how observational bias caused by transit timing variations (TTVs) can affect the detection of low signal-to-noise ratio (S/N) planets in transit surveys, playing a role in the lack of representation of these systems. We present an alternative detection method, RIVERS.radon, which overcomes the effect of TTVs on planet detectability by not relying on an exact periodic solution for the transit signal. It leverages 2D representations of the light curve and approximates the transits with a set of local periodic solutions with the use of 2D cross-correlation. We present an application of RIVERS.radon to the near-resonant system Kepler-404, showing that the signal of the false-positive candidate KOI-2768.03 belongs to the planet Kepler-404b and that it is in a near 5:4 resonance with its companion Kepler-404c, causing TTVs of amplitudes 117.64 and 110.09 minutes, respectively. With a photodynamical fit, we retrieve a pair of similar planets, respectively of radii $1.68^{+0.09}_{-0.09}$ and $1.69^{+0.10}_{-0.10}\,R_\oplus$ and of masses $1.91^{+0.41}_{-0.33}$ and $2.34^{+0.47}_{-0.40}\,M_\oplus$. We find that these planets exhibit typical (near)-resonant features: their densities are lower than the bulk population of exoplanets, and their orbits are nearly coplanar. Interestingly, the planets are found outside the resonance but at a significant distance from the equilibrium point of the $(X_{\rm res}, \delta)$ plane of the Hamiltonian, which is consistent with post-disk instability but somewhat at odds with the observed coplanarity.

</details>

## High-energy astrophysics

### [Cosmic ray protons from 40 GeV to 10 EeV due to star formation?](https://arxiv.org/abs/2611.32671)
*Timur Dzhatdoev, Ilya Kudryashov, Anatoly Semenov* · `astro-ph.HE` · arXiv:2611.32671v1 · relevance 0.18

- **In one sentence**: The paper proposes that cosmic ray protons from about 40 GeV to 10 EeV can be modeled as the sum of three supernova-remnant populations, tested under a supergalactic diffusion scenario (halo radius 1–20 Mpc) and a cosmological scenario (source redshift up to 6).
- **In plain words**: Cosmic rays are very fast charged particles that rain onto Earth from space. This paper asks whether the observed spectrum of these protons, across an enormous range of energies, can be explained by debris from exploding stars formed during star formation. The authors report that a sum of three components, each tied to a different population of supernova remnants, reasonably describes the observed spectrum, under two possible scenarios for where the particles come from.
- **Why it matters**: The highest-energy end of the cosmic ray spectrum has unresolved questions about its origin, so linking it to the known population of stellar explosions is of interest. The text does not show how well the fit compares with alternative explanations, so its significance remains uncertain.
- **Background needed**: - Cosmic rays: high-energy atomic nuclei (here protons) arriving from space; energies are often quoted in electron volts (GeV = billion, TeV = trillion, EeV = quintillion eV).
- Supernova remnants: expanding gas shells left after stars explode; their shock waves are thought to accelerate cosmic rays up to roughly 10 TeV, and possibly about 1 EeV for hypernovae (more energetic explosions) or slower shocks.
- Spectrum: how the number of particles varies with energy; fitting it constrains where particles come from.
- Diffusion and magnetic halo: particles wander through magnetic fields, so the size of the field region (here 1–20 megaparsecs) affects what reaches us.
- Redshift: a measure of distance and look-back time in the expanding universe; z = 6 corresponds to sources very early in cosmic history.
- Supergalactic vs cosmological scenario: whether the particles come from nearby structure or from sources spread across the universe. · level: research-level

<details><summary>Original abstract</summary>

The formation of massive stars eventually results in supernovae explosions. Typical supernova remnants (SNRs) accelerate cosmic ray (CR) protons up to $E_{max-p} \sim 10$ TeV; the value of $E_{max-p}$ may reach $\sim 1$ EeV for the case of the hypernovae and/or for a sub-relativistic velocity of the SNR's shock wave. We show that the observable CR proton spectrum in the energy range between 40 GeV and 10 EeV is reasonably well described with a sum of three components that correspond to three distinct SNR populations. We consider two basic scenarios of CR origin: I) the supergalactic scenario assuming diffusion of the protons inside a magnetic field structure with the characteristic radius $H = 1-20$ Mpc and II. the cosmological scenario with the maximum redshift of the sources $z_{max} = 6$.

</details>

### [Super-Eddington Neutron Star Accretion Columns: Comparing GRRMHD Simulations with Spectral Models](https://arxiv.org/abs/2611.32865)
*Fatemeh Kayanikhoo, Marios Kouzis* · `astro-ph.HE` · arXiv:2611.32865v1 · relevance 0.17

- **In one sentence**: Four axisymmetric general relativistic radiation magnetohydrodynamic simulations of super-Eddington accretion onto magnetized neutron stars (surface fields 3×10^10 to 1×10^11 G) measure accretion column width and estimated radiation shock height, and compare these to column radii inferred from spectral modeling of Be/X-ray binary outbursts using the bwcycl model.
- **In plain words**: Some neutron stars pull in gas faster than the usual brightness limit allows, and the gas funnels onto small spots at the magnetic poles, where it glows in X-rays. This paper uses detailed computer simulations of that funnel flow for four different magnetic field strengths. It then checks whether the funnel sizes they produce match the sizes that X-ray spectra from real outbursts suggest.
- **Why it matters**: Matching simulated funnel geometry against X-ray spectral fits is a way to test whether the models used to read outburst data are physically sound. The text reports that three of the four simulated column radii fall in the upper part of the range inferred from spectra, but it does not say how well the match holds overall, so the agreement should be read cautiously.
- **Background needed**: - Neutron star: a very dense collapsed star, about the mass of the Sun packed into a city-sized ball, with a strong magnetic field.
- Accretion: gas falling onto a compact object from a companion star or disk.
- Eddington limit: a rough brightness ceiling where outward radiation pressure balances gravity; super-Eddington means accretion exceeds it.
- Accretion column: the funnel-shaped region where gas follows magnetic field lines onto the star's magnetic poles.
- Radiation shock: a sharp boundary where infalling gas abruptly slows down because of radiation pressure, near the stellar surface.
- Be/X-ray binary: a system with a rapidly spinning Be star and a neutron star companion, which can have bright outbursts.
- General relativistic radiation magnetohydrodynamics: computer simulations of magnetized, radiating gas under Einstein's gravity; axisymmetric means the model assumes rotational symmetry around an axis.
- Spectral modeling: fitting a theoretical model to the measured spread of X-ray energies to infer physical properties. · level: research-level

<details><summary>Original abstract</summary>

The geometry and structure of neutron star accretion columns affect the X-ray emission in super-Eddington accreting systems. We perform four axisymmetric general relativistic radiation magnetohydrodynamic simulations of super-Eddington accretion onto magnetized neutron stars with the maximum surface magnetic fields ranging from $3\times10^{10}$ to $1\times10^{11}\,\mathrm{G}$. We measure the column width and estimate the characteristic radiation shock heights from the flow velocity and velocity gradient. Across the four models, the angular width decreases from approximately $0.14$ to $0.07\,\mathrm{rad}$, while the estimated shock height increases from $1.95$ to $3.89\,\mathrm{km}$. We then compare our solutions to the best-fit values derived from spectral modeling of super-Eddington Be/X-ray binary outbursts. We calculate area-equivalent column radii that vary between 5.2 and 3.2 km, three of which fall within the upper part of the range inferred from spectral results using the \texttt{bwcycl} model.

</details>

## Stars and the Sun

### [Constraining the Binary Fraction and Mass-Ratio Distribution of FGK Dwarfs with Gaia XP Spectra: Metallicity, $\alpha$-Element, and Age Dependencies](https://arxiv.org/abs/2611.32656)
*Yinuo Zhang, Zexi Niu, Haibo Yuan et al.* · `astro-ph.SR` · arXiv:2611.32656v1 · relevance 0.06

- **In one sentence**: Using the Stellar Locus Outlier method on synthetic Gaia XP photometry and LAMOST DR9 stellar parameters, this paper estimates the binary fraction and high-mass-ratio power-law slope for about 200,000 FGK dwarfs within 1 kpc and examines how these depend on metallicity, alpha-element abundances, and age.
- **In plain words**: Many Sun-like stars are actually pairs of stars orbiting each other. This study looks at roughly 200,000 nearby stars of that type and uses their precise colors, measured from a satellite's spectra, to estimate how many are binaries and how their partner masses are distributed. It then checks how these numbers change with the stars' chemical makeup and estimated age.
- **Why it matters**: Knowing how often Sun-like stars have companions, and what those companions tend to be, feeds into theories of how stars form and how their chemistry and dynamics evolve. The text reports correlations with chemistry and age, but it describes the age trend as likely reflecting underlying chemical correlations, so the causal link is not established here.
- **Background needed**: - Binary star: two stars orbiting a common center of mass; a "binary fraction" is the share of stars that have a companion.
- Mass ratio: the companion's mass divided by the primary's; a distribution of mass ratios describes how likely different partner masses are.
- FGK dwarfs: main-sequence stars somewhat cooler or similar to the Sun (spectral types F, G, K).
- Gaia XP spectra: low-resolution color-like spectra from the Gaia space telescope, used here as synthetic photometry.
- Stellar locus: the tight color-versus-brightness band that single stars follow; unresolved binaries sit off this band, which is what the method exploits.
- Metallicity and alpha-elements: the share of elements heavier than helium, and the subset (such as magnesium, silicon, calcium) produced in certain stellar processes; these trace a star's chemical history.
- Thin vs. thick disk: two populations of stars in the Milky Way's disk, differing in age and chemistry.
- LAMOST DR9: a spectroscopic survey data release providing the stellar parameters used. · level: research-level

<details><summary>Original abstract</summary>

We present a study of the binary fraction and mass-ratio distribution for near 200,000 FGK dwarf stars within 1 kpc, utilizing the Stellar Locus Outlier (SLOT) method applied to synthetic Gaia XP photometry and stellar parameters from LAMOST DR9. By modeling the asymmetric color residuals relative to a metallicity-dependent single-star locus, we measure the binary fraction $f_b$ and constrain the power-law slope $\gamma_{\rm large\,q}$ of the mass-ratio distribution at high mass ratio $q$. Higher metallicity is associated with a steeper (more negative) $\gamma_{{\rm large}q}$, indicating a larger proportion of low-mass-ratio systems. For $\alpha$-elements, [Mg/H] and [Si/H] are anticorrelated with $f_b$ in thin-disk-dominated subsamples; conversely, [Ca/H] shows a positive correlation with $f_b$ in thin-disk-dominated subsamples. No correlation is found between $f_b$ and $\alpha$-element abundances in thick-disk-dominated subsamples. The binary fraction increases modestly toward older ages in the thin-disk population, a trend that likely reflects underlying correlations with chemistry. Our results shed light on how chemical composition and dynamical processes shape the binary properties of solar-type stars.

</details>

### [A Study of Three Intrinsically Luminous Long Period Interacting Eclipsing Binaries in the Galaxy and the Small Magellanic Cloud](https://arxiv.org/abs/2611.33002)
*T. J. Davidge* · `astro-ph.SR` · arXiv:2611.33002v1 · relevance 0.05

- **In one sentence**: A study of three long-period (hundreds of days) interacting eclipsing binaries, two in the Small Magellanic Cloud and one in the Galaxy (PW Pup), using archival visible and mid-infrared photometry and spectroscopy to constrain masses, mass transfer history, and the light from the hidden secondary.
- **In plain words**: This paper looks at three pairs of stars that orbit each other in periods of hundreds of days and pass in front of each other, causing regular dimming. The authors reanalyzed old telescope measurements of brightness and starlight spectra for these systems. They estimate the minimum masses of the companion stars and suggest that all three have transferred material between stars in the past.
- **Why it matters**: Long-period binaries of evolved giant stars are useful tests of how stars change when they share mass, and the Small Magellanic Cloud offers a distant, well-measured sample. The text does not establish wider implications beyond these three systems, and the findings are described as preliminary in places.
- **Background needed**: - Eclipsing binary: two stars orbiting each other, whose regular dimming when one passes in front of the other reveals their sizes, temperatures and orbits.
- Orbital period of hundreds of days: the stars take many months to complete one orbit, much longer than most known binaries.
- Giant stars (K and M type): cool, large, evolved stars that have burned through core hydrogen and swelled up.
- Mass function: a value from the orbit and radial-velocity (Doppler shift) data that sets a minimum mass for the unseen companion.
- Mass transfer: one star feeding material to its partner, which changes both stars' masses and evolution.
- Mid-infrared (MIR) light: longer-wavelength light that can reveal cool dust or disks that are faint in visible light.
- Main sequence and B spectral type: a hot, bright, young-star stage; the text says the components started as B-type stars.
- Small Magellanic Cloud (SMC): a small satellite galaxy of the Milky Way. · level: research-level

<details><summary>Original abstract</summary>

The properties of the eclipsing binaries SMC004701.39-732645.8, SMC005609.41-722809.2 and PW Pup are examined using archival photometric and spectroscopic observations. These systems have orbital periods of hundreds of days, and contain highly evolved components with temperature differences of at least 1000 - 2000K. The SMC systems are among the brightest eclipsing binaries in that galaxy at visible wavelengths, and show excess thermal emission that appears to be typical for luminous K and M giants in that galaxy. A preliminary mass function for SMC004701 suggests a minimum mass for the secondary of 3.8 +/- 0.8 Msolar, whereas the PW Pup mass function indicates a minimum mass for the secondary of 3.2 +/- 0.3 Msolar. Light curve elements are examined for a range of mass ratios using observations at visible and mid-infrared (MIR) wavelengths. The results suggest that SMC004701 may prove to be a double line spectroscopic binary at visible wavelengths. However, with the possible exception of emission from a circumstellar disk, infrared observations will likely be required to detect light from the secondary in the other two systems. All three systems have likely experienced mass transfer, and had components with initial masses that correspond to B spectral types on the main sequence. The light associated with the secondary likely originates from a shell or disk that obscures a hotter central star.

</details>

## Chemical physics

### [Current-Dependent Meta-GGA and Local Hybrid Functionals for Relativistic NMR Shifts](https://arxiv.org/abs/2611.31432)
*Yannick J. Franzke, Christof Holzer* · `physics.chem-ph` · arXiv:2611.31432v1 · relevance 0.22

- **In one sentence**: The paper derives and implements a two-component relativistic version of the current-dependent kinetic-energy density for meta-GGA and local hybrid density functionals in NMR shielding calculations, using SAP-X2C to treat relativistic effects.
- **In plain words**: Chemists use computer simulations to predict NMR spectra, which help identify new molecules, especially those containing heavy atoms where relativistic effects matter. This paper addresses a gap: the more advanced families of density functionals (the approximations used in these simulations) were not well supported in relativistic calculations, and a particular gauge-invariant form of them had not been presented. The authors build that form for relativistic two-component calculations and state that it respects the required symmetries of the spinor wavefunctions.
- **Why it matters**: Heavy-element compounds are hard to characterize, and NMR predictions are often used alongside experiment, so a more reliable functional form could matter for that work. The text describes a formal derivation and implementation; it does not report benchmark accuracy numbers, so its practical benefit is not shown in this excerpt.
- **Background needed**: - NMR chemical shift: the frequency at which a nucleus responds in a magnetic field; it reflects the local electronic environment.
- Density functional theory (DFT): a computational method that approximates a molecule's energy from its electron density.
- Meta-GGA and local hybrid functionals: more elaborate DFT approximations that also use kinetic-energy density or local exact-exchange terms.
- Current density: the flow of electrons induced by a magnetic field; spin-orbit coupling can also induce it.
- Gauge invariance: the requirement that physical results do not depend on the arbitrary choice of reference origin for the magnetic vector potential.
- Relativistic two-component theory (X2C, SAP-X2C): a way to include relativistic effects of heavy atoms in a compact form, with spinors instead of four-component wavefunctions.
- Kramers-restricted Kohn–Sham: a reference-state formulation that respects time-reversal symmetry for electrons. · level: research-level

<details><summary>Original abstract</summary>

NMR chemical shifts are key for the characterization of novel compounds. Especially for molecules with heavy elements, the experimental data is often corroborated with computational studies in density functional theory (DFT). However, modern meta-generalized gradient approximations (meta-GGAs) and local hybrid functionals are not widely supported in relativistic calculations with quantum chemistry program suites. So far, their current-dependent generalization in the spirit of Dobson, Becke, and Tao was not presented at all. This generalization ensures gauge invariance and does not introduce artifacts--unlike the more popular field-dependent generalization of the kinetic-energy density. In non-relativistic and scalar-relativistic calculations, the first was shown to be superior but the current density only arises due to the magnetic field perturbation. In contrast, spin--orbit coupling also induces current densities in the preceding ground-state calculation and the DFT framework needs to be generalized to a current density functional theory (CDFT) for consistency with the current-dependent response equations. Herein, we present the two-component relativistic generalization of the current-dependent kinetic-energy density of a Kramers-restricted Kohn--Sham reference for meta-GGAs and local hybrid functionals in NMR calculations. The extension is invariant under a position-dependent phase and a position-dependent spin rotation of the spinors, or a local U(1)$\times$SU(2) transformation. Relativistic effects are considered with exact two-component theory using a superposition of atomic potentials to include the two-electron picture-change correction (SAP-X2C).

</details>

### [Spin-adapted state preparation for quantum chemistry](https://arxiv.org/abs/2611.30014)
*Matthew L. Sims-Goh, Fredrik Hasselgren, Hamza Jnane* · `quant-ph` · arXiv:2611.30014v1 · relevance 0.14

- **In one sentence**: The paper shows that spin-adapted DMRG matrix product states, indexed by unitary group approach steps, form an abelian-symmetric MPS that block-sparse protocols can prepare on a quantum computer at a cost set by the number of spin multiplets, followed by one Clebsch-Gordan-determined rotation per site to recover the occupation basis, with resource estimates for iron-sulphur active space models.
- **In plain words**: Quantum computers could one day estimate the energy of molecules whose electrons are strongly interacting, but they first need a good starting guess of the molecule's ground state, and building that guess is expensive. This paper proposes a way to build the starting guess that takes advantage of the molecule's total electron spin, so the circuit stores one value per spin group rather than one per individual arrangement. The authors give cost estimates for circuits applied to iron-sulphur cluster models, reporting fewer Toffoli gates (a costly building block in fault-tolerant quantum circuits) and fewer helper qubits than the comparison methods.
- **Why it matters**: Preparing a good initial state is a stated bottleneck for quantum phase estimation on strongly correlated molecules, so reducing its cost bears on whether such calculations become practical on fault-tolerant hardware. The reported gains are resource estimates from the authors' own calculations on specific model systems, not measured hardware runs, so their practical size remains to be tested.
- **Background needed**: - Ground state: the lowest-energy quantum state of a molecule, which determines its chemical properties.
- Quantum phase estimation: a quantum algorithm for finding energies, which needs an initial state with high overlap (similarity) to the true ground state.
- Fault-tolerant cost: counting expensive operations (such as Toffoli gates) and helper qubits (ancillas) needed for error-corrected quantum computers.
- Matrix product state (MPS) and DMRG: a compact, chain-like way to represent many-electron states, and the classical algorithm used to find them.
- Spin and symmetry: electrons have total spin; states related by spin symmetry can be grouped into multiplets, so fewer numbers are needed to describe them.
- Block-sparse protocols: circuit methods that exploit conserved quantities (symmetries) so that only allowed blocks of the state are stored and prepared.
- Unitary group approach (UGA) and Clebsch-Gordan coefficients: standard tools from quantum angular momentum theory used to label and rotate spin states. · level: research-level

<details><summary>Original abstract</summary>

Quantum phase estimation for strongly-correlated molecules requires an initial state of high overlap with the true ground state, and preparing one is a significant fault-tolerant cost. Matrix product states (MPS) produced by the density matrix renormalisation group (DMRG) are a leading choice, yet existing circuits treat their tensors as dense or do not use the full symmetries present in molecular electronic Hamiltonians. In quantum chemistry, DMRG also exploits total spin, a non-abelian symmetry, storing one amplitude per spin multiplet instead of one per state. We show that the reduced tensors of such a spin-adapted MPS, labelled by the steps of the unitary group approach, form an abelian-symmetric MPS, which existing block-sparse preparation protocols can load at a cost set by the multiplet count. One state-independent rotation per site, determined by a Clebsch-Gordan coefficient, then returns the state to the occupation basis. We provide resource estimates for our circuits on singlet ground states of active space models of iron-sulphur clusters, finding improvements in Toffoli count up to $135\times$ compared to dense methods and $4.9\times$ compared to block-sparse methods applied to the same states, with up to $3.7\times$ fewer ancilla qubits required.

</details>

## Materials science

### [Magic-layer scenario for predicting non-van der Waals two-dimensional materials: The case of double-layer honeycomb structures](https://arxiv.org/abs/2611.31748)
*Shota Ono* · `cond-mat.mtrl-sci` · arXiv:2611.31748v1 · relevance 0.15

- **In one sentence**: Using first-principles calculations, the authors propose a "magic-layer" stability criterion, based on excess energies of thin films at different thicknesses, to predict which non-van der Waals compounds (III-V, II-VI, I-VII and Mn-based) can form stable double-layer honeycomb 2D films.
- **In plain words**: Some flat, sheet-like materials can be peeled off a bulk crystal, but many compounds cannot be separated that way. This paper borrows the idea of "magic" cluster sizes, which are unusually stable sizes, and asks whether certain thin-film thicknesses are unusually stable for several families of compounds. The authors calculated the energy of films of different thicknesses and found extra stability at specific thicknesses that correspond to a double-layer honeycomb structure.
- **Why it matters**: The text says the stability measure separates experimentally synthesized systems from unrealized ones, which suggests it could serve as a screening tool for finding new 2D materials before they are attempted in the lab. This is a proposed descriptor tested on a set of cases in the paper; its broader reliability beyond those cases is not shown in the text provided.
- **Background needed**: - Van der Waals (vdW) bonding: weak attractions between layers that let some crystals be peeled into single sheets (for example graphene).
- Non-vdW 2D material: a sheet-like material whose layers are held by stronger bonds, so it is hard to exfoliate from its 3D parent crystal.
- Magic number: a size of a cluster that is unusually stable compared with neighboring sizes.
- Honeycomb structure: a hexagonal lattice of atoms, like graphene's pattern.
- III-V, II-VI, I-VII: families of compounds built from elements in those groups of the periodic table (e.g., GaAs, ZnO, NaCl-type salts).
- First-principles calculation: computing material properties from quantum mechanics without fitted experimental parameters.
- Excess energy: energy of a structure relative to a reference; lower values mean more stable. · level: research-level

<details><summary>Original abstract</summary>

A magic number is a specific size of a van der Waals (vdW) cluster that shows pronounced stability compared to adjacent sizes, and therefore magic clusters are preferentially formed in experiments. We apply the ``magic-layer'' concept to identify non-vdW two-dimensional (2D) materials that are difficult to exfoliate from their parent 3D crystals. As a case, we study the stability of thin films in III-V, II-VI, I-VII, and Mn-based compounds using first-principles calculations. By calculating excess energies for various thicknesses, we find significant stabilization reflecting the formation of double-layer honeycomb structures at specific thicknesses. The stability measure based on the magic-layer concept can distinguish the experimentally synthesized systems from the experimentally unrealized systems, which serves as a key descriptor for predicting the realization of non-vdW 2D materials.

</details>

### [Compositionally Tunable Synthesis of High-Entropy Transition Metal Dichalcogenides Exhibiting Above-Room-Temperature Magnetism](https://arxiv.org/abs/2611.33115)
*Chen Zhang, Xiahua Zhong, Dejia Kong et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33115v1 · relevance 0.15

- **In one sentence**: The paper reports a two-step, solution-based route to ultrathin high-entropy transition metal dichalcogenides containing many magnetic metals, with the (VCrFeCoNi)S2-x composition showing magnetism above room temperature.
- **In plain words**: Computer chips are nearing the limits of how small silicon-based circuits can get, so researchers are looking at ultrathin magnetic materials for future electronics. This paper describes a way to make such flat, sheet-like materials by first building a layered precursor that mixes many metal types evenly at the atomic scale, then converting it into a sulfur-containing compound. The example material, made from five metals and sulfur, is reported to stay magnetic above room temperature.
- **Why it matters**: Magnetism that survives at room temperature is a practical requirement for many magnetic device ideas, so a tunable way to make such 2D magnets could widen the set of usable materials. The text does not give magnetic strength data or device tests, so its practical impact is still uncertain.
- **Background needed**: - Two-dimensional (2D) materials: crystals only a few atomic layers thick, with very different properties from bulk material.
- Transition metals: the metal elements in the middle of the periodic table (e.g., V, Cr, Fe, Co, Ni), often magnetic.
- Dichalcogenides: compounds of a metal with a chalcogen such as sulfur, selenium or tellurium.
- High-entropy materials: materials that mix five or more elements in roughly comparable amounts, with the mixing itself stabilizing the structure.
- Layered double hydroxides: layered mineral-like precursors that can be made in water and used as a template for the target material.
- Hydrothermal coprecipitation: making solids by mixing dissolved salts in water in a sealed heated vessel, so they precipitate together.
- Chalcogenization: reacting a precursor with a chalcogen (here, sulfur) to convert it into the target compound.
- Curie-type magnetism above room temperature: magnetic ordering that persists at roughly 20–25 °C or higher. · level: research-level

<details><summary>Original abstract</summary>

As silicon-based electronics approach their physical limits, low-dimensional magnetic materials have attracted increasing attention for next-generation electronic and information technologies. Realizing these opportunities requires two-dimensional (2D) materials with robust and tunable room-temperature magnetism. Here, we report a two-step synthesis strategy for fabricating 2D high-entropy transition metal dichalcogenides (HE-TMDs) incorporating magnetic elements beyond conventional groups 4-6. High-entropy layered double hydroxides (HE-LDHs) are first synthesized via hydrothermal coprecipitation, enabling atomic-level mixing of diverse transition metals across groups 4-12. Subsequent chalcogenization yields 2D HE-TMDs while preserving homogeneous elemental distribution. This approach circumvents the constraints of solid-state reaction, chemical vapor transport methods, enabling the synthesis of compositionally complex and structurally controlled 2D magnets. Representative (VCrFeCoNi)S2-x exhibits robust magnetism above room temperature, demonstrating the potential of this high-entropy design strategy for expanding the compositional and functional diversity of 2D magnetic materials.

</details>

## Soft matter and polymers

### [Long-Range Hydrodynamic Communication in Active Matter](https://arxiv.org/abs/2611.32867)
*Abhishek Thakur, Bibaswan Ghosh* · `cond-mat.soft` · arXiv:2611.32867v1 · relevance 0.17

- **In one sentence**: A symmetric passive rotor inside a circular domain is set into persistent unidirectional rotation by the hydrodynamic flow from a boundary-confined flock of Marangoni swimmers, with no contact between them, and larger flocks suppress reverse-torque events.
- **In plain words**: Tiny self-propelled swimmers, driven by surface-tension (Marangoni) forces, are placed around the edge of a circular pool, and a freely turning rotor sits in the middle. The swimmers never touch the rotor, yet their combined fluid flow makes it spin in one direction. Single swimmers sometimes push the rotor backward, but a larger group produces a steady circulating flow that keeps the spinning consistent.
- **Why it matters**: Most schemes for directed motion in active matter rely on built-in asymmetry such as ratchets or gears; this text reports a route without that bias, transmitted through fluid flow alone. Its relevance to practical contact-free actuation is suggested by the authors but not tested beyond the systems described.
- **Background needed**: - Active matter: systems of self-propelled units (here, swimmers) that consume energy to move on their own.
- Marangoni swimmers: objects that move by releasing surface-active material, which changes surface tension and drives flow along the liquid surface.
- Hydrodynamic coupling: one moving object alters the surrounding fluid, which pushes or turns other objects without direct contact.
- Rotor and torque: a freely turning body; torque is the twisting push that spins it, and reverse torque means spinning backward.
- Ratchet: a structure with built-in asymmetry that rectifies random motion into a preferred direction.
- Particle image velocimetry (PIV): an imaging method that tracks tracer particles in a fluid to map its flow field. · level: intermediate

<details><summary>Original abstract</summary>

Directed transport in active matter is typically achieved by introducing geometric asymmetry, such as ratchets or gears, that rectify the stochastic motion of active particles. Here we demonstrate a fundamentally different route in which persistent mechanical motion emerges without any geometric bias. A symmetric passive rotor placed at the center of a circular domain undergoes spontaneous unidirectional rotation driven solely by the hydrodynamic flow generated by a boundary-confined flocks of Marangoni swimmers, despite the absence of direct physical contact. While individual swimmers produce intermittent torque reversals arising from transient hydrodynamic backflow, increasing the size of the flock establishes coherent circulation that stabilizes the rotor dynamics. Particle image velocimetry (PIV) reveals that the collectively generated flow transmits momentum over macroscopic distances, converting local active forcing into robust mechanical transport. Together with a minimal flow superposition model, our results identify the suppression of reverse-torque events as a collective signature of hydrodynamic coupling between active swimmers and a passive body, providing a contact-free mechanism for remote mechanical actuation in active matter.

</details>

### [Periodic and quasiperiodic structures produced by microphase separation in one-component simple liquids with competing interactions](https://arxiv.org/abs/2611.32273)
*Lorenzo Agosta, Alfredo Metere, Mikhail Dzugutov* · `cond-mat.mes-hall` · arXiv:2611.32273v1 · relevance 0.12

- **In one sentence**: A Perspective reviewing molecular-dynamics simulations of microphase separation in single-component simple liquids whose pair potentials combine short-range attraction with long-range repulsion (SALR), and the periodic and quasiperiodic structures these produce.
- **In plain words**: When a liquid's particles attract at short range but repel at long range, they cannot simply clump into one big droplet; instead they settle into repeating patterns on a scale much larger than the particles themselves. This Perspective reviews recent computer simulations showing that simple, single-component particle models can reproduce the kinds of patterns seen in block copolymers and liquid crystals. The authors also describe new periodic structures that these simulations produce.
- **Why it matters**: The text suggests the simulations show that chemically complex molecules are not required to form these mesoscale patterns, which is a conceptual point about how such structures arise. The authors also suggest the simulated patterns could serve as templates for topology-governed metamaterials, but the text gives no details of such devices, so that application remains speculative.
- **Background needed**: - Phase separation: a mixture splitting into distinct regions, like oil and water.
- Microphase separation: competing forces stop this splitting at large scale, so regions form only at a fixed, small scale, giving repeating patterns.
- SALR potential: a rule for how particles push and pull, with short-range attraction and long-range repulsion.
- Block copolymers: long molecules made of chemically different segments joined together, which self-assemble into periodic patterns.
- Mesophases: intermediate ordered states between liquid and crystal, such as those in liquid crystals.
- Molecular dynamics: computer simulation that tracks how each particle moves over time.
- Metamaterials: engineered materials whose behaviour comes from their structure rather than their chemistry. · level: research-level

<details><summary>Original abstract</summary>

Competing interactions can generate frustration which suppresses macroscopic-scale phase separation, superseding it with separation patterns on the microscopic scale. This phenomenon, referred to as microphase separation, produces thermodynamically stable mesoscopic-scale periodic patterns in systems of different physical nature. The studies of this effect follow two paradigms. First, in block copolymers, the macroscopic-scale separation of chemically distinct components is prevented by the covalent bonds between them. In the other, the microscopic-scale separation is produced in simple single-component liquids by the competition between a short-range attraction and a long-range repulsion (SALR) in the pair potential, the separation occurring between a dense phase and a gas. The interest in the simple liquid models with SALR interaction was inspired by the apparent universality of the modulated structures generated by competing interactions in different systems. Simple particle models are tractable by theory and thereby make it possible to discern the microscopic mechanisms of pattern formation; particle-based simulations give access to systems beyond the reach of experiments. In this Perspective we review the recent advances in the molecular-dynamics simulation of microphase separation in single-component simple liquids using SALR potentials. We show that these simulations reproduce the mesophases typical of block copolymers and liquid crystals, which demonstrates that the complexity of the constituent particles of real liquids is not a necessary condition for their formation, and that they produce novel periodic morphologies of both conceptual interest and technological relevance; we discuss how simulated mesophases can serve as templates for metamaterials whose properties are governed by topology.

</details>

## AI for chemistry and materials

### [Evolutionary constraints on protein fold diversity](https://arxiv.org/abs/2611.33104)
*Harutyun Sahakyan, Eugene V. Koonin* · `q-bio.BM` · arXiv:2611.33104v1 · relevance 0.32

- **In one sentence**: A review-style abstract arguing that natural proteins use only a small fraction of the folds that secondary-structure arrangements could theoretically produce, and asking whether biophysics or evolutionary history limits fold diversity.
- **In plain words**: Proteins are chains that fold into 3D shapes, and in principle their building blocks could be arranged into a huge number of shapes. This paper asks why nature uses only a limited set of these shapes, whether physics or the messy history of evolution is the cause. The text reports that natural proteins take up only a small fraction of possible folds and discusses how evolution restricts which new folds can arise.
- **Why it matters**: Knowing which fold shapes are reachable matters for designing new proteins and for predicting structures from sequence. The text is only an abstract, so it does not show the specific evidence, and the link to AI-driven design is mentioned only in passing.
- **Background needed**: - Protein fold: the overall 3D shape a protein chain settles into.
- Secondary structures: local building blocks such as alpha helices and beta strands, which pack together to form a fold.
- Topology: how those blocks are connected and arranged in space.
- Structure prediction and cryo-electron microscopy: computational and imaging methods used to determine protein shapes.
- Evolutionary contingency: the idea that past historical accidents, not just physical rules, shape which forms exist. · level: intermediate
- Matched keywords: molecular, protein

<details><summary>Original abstract</summary>

Arrangements of secondary structures in proteins yield a wide variety of possible topologies, yet the protein folds observed in nature are limited in their diversity. Is the number of protein folds limited by biophysical constraints or by evolutionary contingency? In recent years, the development of new methods for protein structure prediction and comparison, molecular design, and the rapid progress of cryo-electron microscopy revealed new insights into the protein fold space. Here, we present recent findings demonstrating that natural proteins adopt only a small fraction of all possible folds and discuss how evolutionary processes limit the diversity of evolving protein folds.

</details>

### [OMNI-P3x universal neural network potential for large-scale computational photochemistry workflows](https://arxiv.org/abs/2611.32133)
*Miko{\l}aj Martyka, Joanna Jankowska, Pavlo O. Dral* · `physics.chem-ph` · arXiv:2611.32133v1 · relevance 0.24

- **In one sentence**: The paper introduces OMNI-P3x, a universal machine-learned interatomic potential trained on ground- and singlet excited-state geometries of neutral and charged organic molecules, and applies it to high-throughput photochemical screening of flavylium and xanthene dyes.
- **In plain words**: Designing light-responsive molecules, such as dyes that glow at particular colours, normally requires slow quantum calculations for each candidate, which makes checking large libraries too costly. The authors built a machine-learning model that imitates those calculations for both the resting and light-excited states of organic molecules. They used it to screen about 234,000 flavylium dyes without new quantum calculations, then fine-tuned it and screened about 163,000 xanthene dyes, flagging candidates that may emit red, near-infrared and short-wavelength infrared light.
- **Why it matters**: It shows a machine-learned shortcut can handle full photochemistry workflows, not just ground-state chemistry, at very large scale, which could speed up searching for new dyes and emitters. Whether the predicted candidates work in practice is not established by the text, and its accuracy is described only as "approaching" TD-DFT, a standard but approximate excited-state method.
- **Background needed**: - Interatomic potential: a model that predicts the energy and forces on atoms from their positions, so molecular shapes can be simulated without solving quantum equations each time.
- Machine-learned potential (MLIP): such a potential learned from reference quantum calculations; "universal" means it is meant to cover many kinds of molecules.
- Excited state: the state a molecule enters after absorbing light; photochemistry studies how molecules behave in it.
- TD-DFT (time-dependent density functional theory): a common, moderately expensive quantum method for computing excited-state energies and absorption colours.
- Flavylium and xanthene dyes: families of coloured organic molecules used as dyes and fluorescent markers.
- Partial (atomic) charges: how electron density is shared among atoms; here the charges are learned without reference charge data and used to show charge shifts on excitation. · level: research-level
- Matched keywords: molecular, interatomic potential

<details><summary>Original abstract</summary>

Computational photochemistry supports the design and understanding of new materials. However, the high cost of excited-state quantum-mechanical (QM) calculations makes screening large molecular libraries prohibitively expensive. To address this limitation, we introduce OMNI-P3x, a universal machine-learned interatomic potential (MLIP) for singlet ground- and excited-state simulations of neutral and charged organic molecules. Trained on both ground- and excited-state conformations, it performs complete computational photochemistry workflows with accuracy approaching TD-DFT. We demonstrate its practical applicability by screening a combinatorial library of 234,375 flavylium derivatives, where the pretrained model performs ground-state geometry optimization and predicts absorption properties without additional QM calculations. Following fine-tuning, we further screen 162,960 xanthene-based dyes, identifying new candidates for red, near-infrared and short-wavelength infrared emission. Furthermore, state-dependent neural charges, learned without reference atomic charges, provide an interpretable picture of intramolecular charge redistribution upon excitation.

</details>

## Biochemistry

### [Resolving Hepatic Metabolic Flux During Ex Vivo Liver Perfusion Reveals Compartment-Specific Constraints](https://www.biorxiv.org/content/10.64898/2026.11.24.769061v1)
*Amin, A. M.; Mcleod, M.; Browder, N. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.769061 v1 · relevance 0.10

- **In one sentence**: Using staged ex vivo perfusion of mouse livers with 13C-labelled tracers, the authors test whether simplified glucose-fragment flux models hold for intact liver and find that a two-compartment model fits substantially better than a one-compartment model.
- **In plain words**: Surgeons keep donor livers alive outside the body on a machine before transplant, and they currently judge liver health with broad measures. This study asks whether tracking how labelled sugar and related fuels move through individual liver cells could give a more detailed picture of liver metabolism. The authors found that treating the liver as one uniform unit did not explain most of their measurements, but splitting it into a sugar-making part and a sugar-using part did fit most of the data.
- **Why it matters**: Donor liver viability assessment is a practical clinical problem, so a more mechanistic readout could matter if it proves usable. The link to transplant decisions is only implied by the text; the paper itself is a mouse study and does not report clinical outcomes.
- **Background needed**: - Normothermic machine perfusion: keeping an organ warm and circulating fluid through it outside the body.
- Metabolic flux: the rate at which molecules are converted through biochemical pathways.
- 13C tracers: fuels (lactate, pyruvate, glucose) made with heavy carbon atoms so their path through metabolism can be tracked by measuring labelled molecules.
- Isotopomers: versions of a molecule that differ in which carbon atoms carry the heavy label.
- TCA cycle: the central energy-producing cycle in mitochondria; malate is one of its intermediates.
- Gluconeogenesis: making new glucose from non-sugar sources.
- Compartmentation: separating a tissue's metabolism into distinct functional zones or cell groups, modelled as separate units.
- Lobectomy: surgical removal of a lobe of the liver, used here in a serial design. · level: research-level

<details><summary>Original abstract</summary>

Normothermic machine perfusion (NMP) is used to preserve and assess donor livers, but current viability criteria rely on global measures that do not resolve intracellular metabolism, which would provide a more mechanistic measure of donor liver function. We combined staged ex vivo perfusion of mouse livers, serial lobectomy and 13C tracers ([U-13C3]lactate, [U-13C3]pyruvate and [U-13C6]glucose) to test whether glucose fragment-based flux models used in vivo describe intact hepatic metabolism. With intracellular metabolite isotopomers as constraints, a homogeneous one-compartment model failed to fit most datasets, and the lack of fit centered on TCA cycle intermediates such as malate. A two-compartment model, in which a glycolytic compartment takes up glucose from the sinusoidal pool, including glucose released by a gluconeogenic compartment, fitted 41 of 45 datasets. Flux partitioning between compartments depended on nutritional state, which influenced hepatic metabolism more than perfusate glucose. Nevertheless, glucose fragment and two-compartment flux estimates correlated (R2 = 0.68-0.89). Intracellular isotope tracing thus shows that hepatic compartmentation constrains whole-liver flux estimation, while supporting simplified models for quantitative assessment during perfusion.

</details>

### [Albumin alleviates pressure overload-induced heart failure by improving mitochondrial homeostasis via PKA-LKB1-AMPK axis](https://www.biorxiv.org/content/10.64898/2026.11.21.768247v1)
*AN, Q.; Ma, B.; Fu, Y. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.21.768247 v1 · relevance 0.06

- **In one sentence**: In a mouse model of pressure-overload heart failure, recombinant serum albumin improved cardiac function and mitochondrial energy metabolism, reportedly via a PKA-LKB1-AMPK signaling axis.
- **In plain words**: Heart failure is a condition where the heart gradually loses its ability to pump blood well, and it carries a high rate of death and cost. This study asked whether albumin, the most abundant protein in blood, plays a protective role, since people with heart failure often have low albumin. In mice whose aortas were narrowed to overload the heart, giving them extra mouse albumin improved heart pumping, reduced thickening and scarring, and eased inflammation.
- **Why it matters**: Low albumin is already known to track with worse heart failure outcomes, but the cause-and-effect link has been unclear, so this work tries to test it directly. It may point toward albumin, or the pathway it reportedly activates, as a treatment target, though the evidence here is from mice and the text alone does not show whether this would work in people.
- **Background needed**: - Heart failure: the heart cannot pump enough blood to meet the body's needs; pressure overload (for example from high blood pressure or a narrowed aortic valve) is one cause.
- Transverse aortic constriction (TAC): a surgical method that narrows the main artery leaving the heart in mice to mimic pressure overload.
- Serum albumin: the most common protein in blood, which carries molecules and helps maintain fluid balance; here it was given as a recombinant (lab-made) mouse version.
- Knockout (AKO) mice: animals genetically engineered to lack the albumin gene, used to test whether albumin is needed.
- Mitochondria: the cell's energy-producing structures; "mitochondrial homeostasis" means keeping them healthy and functioning.
- Fatty acid oxidation and oxidative phosphorylation: ways cells burn fats and produce energy (ATP).
- PKA, LKB1, AMPK: cellular signaling proteins that relay energy-status and hormone signals; AMPK acts as a cell's energy sensor.
- Hypertrophy: enlargement of heart muscle cells; phenylephrine (PE) is a drug used in cell experiments to trigger this. · level: research-level

<details><summary>Original abstract</summary>

Aims Heart failure (HF) is a global health challenge due to its high incidence, mortality, and socioeconomic burden. Despite medical advancements, HF prognosis remains poor, highlighting the need for enhanced understanding and treatment strategies. Serum albumin, a key circulatory protein, has gained attention as a biomarker in cardiovascular diseases. Low serum albumin levels are linked to HF incidence, progression, and prognosis, suggesting its regulatory role, though mechanisms remain unclear. This study aimed to elucidate the role of serum albumin in HF pathogenesis and investigate its potential therapeutic effects. Methods and results A mouse model of pressure overload-induced HF was established via transverse aortic constriction (TAC). Serum albumin levels were significantly decreased in HF mice. Administration of recombinant mouse serum albumin (rMSA) effectively restored serum albumin concentrations, improved cardiac systolic function, alleviated cardiac hypertrophy and fibrosis, and reduced inflammatory responses, collectively attenuating disease progression. In contrast, albumin-knockout (Alb-/-, AKO) HF mice displayed aggravated pathological manifestations compared with wild-type (WT) controls, whereas rMSA supplementation markedly ameliorated these impairments. In vitro experiments demonstrated that rMSA protected against phenylephrine (PE)-induced hypertrophy in cardiomyocytes. To elucidate the underlying mechanism, transcriptomic analyses of cardiac tissues revealed that albumin played a critical role in improving mitochondrial homeostasis. Experimental validation further demonstrated that albumin activated the PKA-LKB1-AMPK signaling axis, leading to improved mitochondrial respiratory function and oxidative phosphorylation, as well as enhanced mitochondrial quality control. These changes promoted fatty acid oxidation and optimized energy metabolism, thereby reversing the energy imbalance underlying cardiac dysfunction. Conclusion Our study suggests that serum albumin exerts a protective effect in HF by improving mitochondrial dysfunction and energy metabolism disorders, thus reversing energy imbalance and mitigating disease progression. These results support recombinant serum albumin as a promising therapeutic for HF, with its mechanism involving the critical improvement of mitochondrial homeostasis.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Tuning evolutionary information in MSAs shapes protein generation and folding](https://www.biorxiv.org/content/10.64898/2026.11.23.768656v1)
*Richardson, G.; Colliandre, L.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.23.768656 v1 · relevance 0.15

- **In one sentence**: The paper tests whether changing which homologous sequences are included in a protein multiple sequence alignment (MSA), and thereby its per-site information content, steers generative protein design and structure prediction outcomes, using matched random-row controls across 45 proteins and a separate structure-prediction benchmark.
- **In plain words**: Protein models often learn from a collection of related sequences (an alignment) that is treated as fixed input. This study deliberately changed which rows went into those collections and measured how the designed sequences and predicted structures changed. The authors report that alignments with certain levels of evolutionary information tended to produce more novel generated sequences and lower structural confidence, and that a moderate share of low-information positions was linked to better predictions in a subset of cases.
- **Why it matters**: If the composition of the input alignment measurably shapes what protein generators and structure predictors output, alignment choice becomes a design variable rather than a background detail. The text does not establish how general these effects are beyond the cohorts studied, so the practical reach remains unclear.
- **Background needed**: - Multiple sequence alignment (MSA): a table lining up many evolutionarily related protein sequences so that matching positions appear in the same column.
- Rows: individual sequences in the alignment; "row selection" means choosing which homologues to keep.
- Information (bits per site): a measure of how strongly a column's amino acids are constrained; low-information columns look close to random.
- Lower-tail information: the least-constrained part of the distribution of column information.
- Structure-prediction confidence: the model's self-reported certainty about a predicted 3D fold.
- Decoder uncertainty: how unsure a generative model is when choosing each next residue.
- Matched-depth random-row control: a comparison alignment with the same number of sequences but chosen at random, to separate the effect of information from the effect of size.
- Confidence-gated subset: the subset of cases kept based on a confidence threshold before evaluation. · level: research-level

<details><summary>Original abstract</summary>

Protein multiple sequence alignments are widely regarded as fixed artifacts of homologue retrieval. An alignment's row composition shapes the evolutionary context that is supplied to a protein model. In this study, we tested whether tuning row composition would steer protein generation and structure prediction outcomes. We tuned lower-tail alignment information by controlling row selection within a reference protein-projected coordinate frame. We paired each information-targeted alignment with a matched-depth random-row control alignment. Across a cohort of 45 diverse proteins, row coherence among the retained homologues is predictive of structural confidence readouts and generated sequence novelty. The strongest row-coherence states occur near an empirical lower-tail information reference point of 1 bit/site. Below this reference point, generated de novo sequences demonstrate more eager exploration, higher decoder uncertainty, and reduced structural confidence at mutated positions. Across an independent structure-prediction benchmark, controlling the fraction of low-information positions demonstrated that intermediate fractions of low-information positions were associated with improved structure prediction within a confidence-gated subset. These findings evince that evolutionary information in protein alignments can be tuned to shape protein generation and structure prediction results.

</details>

### [Microbiome complexity shapes host transcriptional networks across the ileum-liver axis](https://www.biorxiv.org/content/10.64898/2026.11.16.767119v1)
*Halkhoree, A. C.; Grannell, A.; Pearson, C. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.16.767119 v1 · relevance 0.09

- **In one sentence**: Transcriptomic survey of mouse terminal ileum across germ-free, defined 12-strain microbiota (MM12), and specific-pathogen-free conditions, examining how microbiome complexity shapes host gene co-expression networks along the ileum-liver axis.
- **In plain words**: This study asks how the community of microbes living in the gut changes the way genes switch on and off in the last part of the small intestine, called the ileum, and possibly in the liver. The researchers compared mice with no microbes at all, mice carrying a simple set of 12 known bacterial strains, and mice with a full, diverse normal microbiome, with 15 animals in each group. The provided text describes the design and aims only; it does not report the results.
- **Why it matters**: Gut microbes are known to affect digestion, immunity and liver function, so mapping how their diversity tunes host gene activity could help explain gut-liver links. The text does not show findings, so the size or direction of any effect is unknown from this excerpt.
- **Background needed**: - Microbiome: the community of bacteria and other microbes living in the gut.
- Germ-free (GF) mice: raised without any microbes, used as a baseline.
- MM12 (Oligo-Mouse-Microbiota-12): a defined community of 12 bacterial strains, a simpler stand-in for a microbiome.
- SPF (specific pathogen free): standard lab mice with a normal, diverse microbiome but no listed pathogens.
- Transcriptome: the full set of gene activity readouts (RNA) in a tissue.
- Co-expression network: a map of genes whose activity rises and falls together, suggesting shared regulation.
- Ileum and liver: the small intestine's final segment (nutrient absorption, immune tissue) and the liver, linked through blood and bile.
- Bile acids: digestive molecules modified by gut bacteria and involved in gut-liver signaling. · level: research-level

<details><summary>Original abstract</summary>

The microbiome plays an increasingly recognised role in development, metabolism and immunity across all segments of the small and large intestine, as well as more distant organs such as the liver. In the terminal ileum - a key site of nutrient absorption - the presence of microbes dictates the development of secondary lymphoid structures (Peyers patches), mediates bile acid metabolism, and impacts absorption. In part, coordinated regulatory networks in the gut impact liver function and immunity through gut-liver connectivity and the movement of immune cells and bioactive small molecules that includes bile acids and other bacterial metabolites. We aimed to examine the extent of microbiome involvement in ileal transcription, where subtle changes in co-expression networks can be tuned by microbiome diversity, composition and function. We surveyed ileal transcriptomes across mouse models which vary in microbiome complexity ranging from germ-free (GF, n = 15), the Oligo-Mouse-Microbiota-12 (MM12, n = 15), and specific pathogen free (SPF, n = 15).

</details>

## Neuroscience

### [Benchmarking machine learning across development reveals stage-specific neuroanatomical sex signatures.](https://www.biorxiv.org/content/10.64898/2026.11.24.768941v1)
*Poon, E.; Honari, H.; Ansarifar, J. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.24.768941 v1 · relevance 0.10

- **In one sentence**: A benchmark of linear and nonlinear machine learning models for classifying sex from structural brain MRI in children and adolescents (ages 8–21), testing how age affects accuracy, feature stability, and SHAP/LIME-based attributions of which regions drive predictions.
- **In plain words**: Researchers trained computer models to guess a person's sex from brain scans of children and young adults aged 8 to 21. They compared several model types and checked how well the models worked at different ages and which brain regions they relied on. The simpler and more complex models performed about the same, but the brain features the models used shifted with developmental stage.
- **Why it matters**: The paper argues that high accuracy alone does not show a model is biologically meaningful, and that results can change across development. This matters for anyone using AI to interpret brain imaging, though the text does not establish what the specific regional findings mean biologically.
- **Background needed**: - Machine learning: software that learns patterns from labeled examples, here brain scans labeled by sex.
- Structural neuroimaging (MRI): scans of brain size, shape and tissue, not activity.
- Linear vs nonlinear models: simple weighted-sum rules versus more flexible models that can capture complex interactions.
- Cross-age generalization: training a model on one age group and testing it on another, to see whether patterns carry over.
- SHAP and LIME: explanation tools that estimate how much each input feature pushed a prediction up or down.
- Feature stability: whether the same brain regions are consistently identified as important across runs or groups.
- Sex classification is a research tool here; it is not a measure of a person's sex identity. · level: research-level

<details><summary>Original abstract</summary>

Machine learning (ML) offers powerful approaches for identifying multivariate patterns in neuroimaging data, yet the biological validity and interpretability of the discriminative patterns learned by such models remain incompletely understood. Here, we benchmarked multiple ML approaches for sex classification across development (8-21 years) on structural neuroimaging data and investigated the effects of age on model performance and feature stability. Linear and nonlinear models demonstrated comparable classification performance, indicating that high predictive accuracy can be achieved without relying on highly complex architectures; however, age-stratified analyses and cross-age generalization tests demonstrated that developmental stage influences classification performance, and consistency of learned neuroanatomical features. To assess biological interpretability, we applied SHAP and LIME explainability methods and developed a comprehensive framework for translating feature attributions into biologically interpretable patterns. Sex-discriminative regions were distributed across multiple cortical and subcortical structures and exhibited marked developmental variation. Together, these findings demonstrate the utility of interpretable ML for developmental neuroimaging and highlight the importance of evaluating predictive performance while simultaneously taking biological validity, developmental specificity, and attribution stability into consideration.

</details>

### [Jump: Making Large-Scale Connectomics Accessible](https://www.biorxiv.org/content/10.64898/2026.11.12.765999v1)
*Morris, G. P.; Mohamed, H. F.; Selim, R. S. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.12.765999 v1 · relevance 0.09

- **In one sentence**: The paper presents Jump, a set of web-based tools (with uJump for the MICrONS mouse visual cortex EM dataset as the worked example) for exploring, reviewing, and quantifying cell classifications in large volumetric electron microscopy connectomics datasets, with a pericyte and endothelial cell case study on cortical vasculature.
- **In plain words**: Scientists have mapped the wiring of brain tissue using very detailed microscope images, producing huge databases of cells, but computer-generated labels for those cells are hard to check and hard to analyse. This paper describes Jump, a set of user-friendly websites that let researchers browse these datasets, have experts review and correct cell labels, and measure things like cell counts, shapes, and spacing. The authors show how this works on one mouse brain dataset and use blood-vessel cells as a test case.
- **Why it matters**: Large brain-mapping datasets are only useful if their automated labels can be trusted, and this work aims to make that checking and sharing easier for more people. The text does not report independent measures of how much faster or more accurate the approach is, so its practical impact is still to be seen.
- **Background needed**: - Electron microscopy (EM): imaging at very high resolution, used here to photograph thin slices of brain tissue and stack them into 3D.
- Connectomics: mapping the connections between nerve cells in a tissue.
- Segmentation: automatically outlining each cell or structure in the images.
- Cell classification: using software to label what type each cell is (for example, a pericyte or endothelial cell).
- Pericytes and endothelial cells: support and lining cells of small blood vessels.
- MICrONS: a large public dataset of mouse visual cortex mapped with EM.
- Web-based platform: a tool run in a browser, so no special local software is needed. · level: intermediate

<details><summary>Original abstract</summary>

Large-scale connectomic resources generated from volumetric electron microscopy (EM) have transformed neuroscience by enabling detailed 3D reconstructions of cellular and subcellular morphology and connectivity across hundreds of thousands of cells in diverse tissues and organisms. Recent advances in machine learning-based cell classification and automated segmentation have enabled large-scale annotation of these datasets, yet barriers remain in validating automated classifications and extracting biological insights. To address these challenges, we developed Jump, a suite of user-friendly web-based platforms generated using Claude. These platforms support interactive exploration, expert-guided community review, and quantitative analysis of multiple publicly available EM datasets, while building a growing repository of community-generated annotations. Using uJump, which hosts data from the MICrONS mouse visual cortex dataset, as an example, we demonstrate rapid retrieval of specific cell populations, region-of-interest filtering, biological inspection of cells, and extraction of quantitative morphological and spatial metrics. We showcase analytical features including cell abundance and spatial organisation, connectivity, local cellular neighbourhoods, and volumetric measurements. Using pericytes and endothelial cells as a case study on the cortical vasculature, we further demonstrate how manual review and reclassification can generate accurately identified cell populations for downstream analyses. Consistent with the open-science principles underpinning many large-scale EM resources, Jump is designed to enable broad community participation. By lowering technical barriers to the use of EM datasets, Jump increases analytical efficiency and promotes collaborative efforts to accurately classify cells and structures. Expert-reviewed annotations can be shared across the community, allowing users to build on existing work rather than repeatedly validating the same automated classifications. Collectively, Jump will help researchers to accelerate biological discovery from connectomic datasets.

</details>

## Genetics and genomics

### [Functional interrogation of osteoarthritis-associated regulatory variants and effector genes.](https://www.biorxiv.org/content/10.64898/2026.11.23.768666v1)
*Piedade, A. P.; Stuppy, S. R.; Shine, J. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.23.768666 v1 · relevance 0.11

- **In one sentence**: Functional genomics in primary human chondrocytes (MPRA, CRISPR activation/interference, chromatin and conformation data) that nominates rs1895062 at the 9q33 locus as a likely causal variant regulating PAPPA expression in osteoarthritis risk.
- **In plain words**: Genetic studies have linked hundreds of spots in the genome to osteoarthritis, a common joint disease, but for most of them it is unclear which DNA change matters and which nearby gene it affects. This paper tested candidate DNA regions in cartilage-forming cells, using lab assays that measure how strongly each version of a sequence switches genes on. For one variant, rs1895062, the researchers found that the version linked to higher risk drives more activity, and that switching on its region raises the expression of the PAPPA gene.
- **Why it matters**: It moves beyond association to suggest a specific variant and gene that could be studied as a mechanism in joint disease. The text presents this as convergent evidence rather than proof, and the link to actual osteoarthritis in patients is not directly tested here.
- **Background needed**: - Osteoarthritis: wear-and-tear joint disease of cartilage.
- GWAS (genome-wide association study): scans that find genetic variants statistically linked to a disease; they rarely identify the causal variant or gene.
- Variant / allele: a single-letter DNA difference at one position; the "G allele" is one version of it.
- Regulatory element: a stretch of DNA that controls how much a gene is turned on, often far from the gene itself.
- Chondrocyte: cartilage cell.
- MPRA (massively parallel reporter assay): tests thousands of DNA sequences at once for how strongly they drive gene activity.
- CRISPR activation/interference: tools that switch a gene up or down at a chosen DNA location.
- Chromatin accessibility, H3K27ac, chromatin looping: lab signals showing DNA that is open and active, and which distant DNA segments physically contact a gene's promoter.
- PAPPA: a protein-cleaving enzyme involved in growth-factor signalling; SPRY4 is a signalling regulator also studied as a target. · level: research-level

<details><summary>Original abstract</summary>

Background: Genome-wide association studies (GWAS) have identified hundreds of loci associated with osteoarthritis (OA); however, the regulatory variants and effector genes underlying most associations remain unresolved. Results: We used complementary functional genomic approaches in chondrocytes to resolve prioritized OA risk loci. Massively parallel reporter assays (MPRAs) in primary human chondrocytes identified allele-specific regulatory activity at variants across multiple loci, two of which were independently validated using low-throughput reporter assays. In parallel, integration of OA GWAS signals with chromatin accessibility, H3K27ac CUT&Tag, and chromatin conformation data prioritised candidate regulatory elements for CRISPR based perturbation. CRISPR activation and interference supported functional regulatory relationships between OA risk regions and Pappalysin 1 (PAPPA) and Sprouty RTK signaling antagonist 4 (SPRY4) as target genes. At the 9q33 locus, multiple independent lines of evidence converged on rs1895062, which resides in an accessible region that loops to the PAPPA promoter. The OA risk G allele at rs1895062 results in higher regulatory activity by MPRA and low throughput reporter assay. Activation of this region by CRISPR increases PAPPA gene expression and induces widespread transcriptional changes involving extracellular matrix remodelling and other OA-relevant pathways. Conclusion: Integrating genetic association, genomic and epigenomic data, and functional perturbation in disease-relevant cells can resolve the regulatory mechanisms underlying OA risk loci. Using this multi-faceted approach, we provide convergent functional evidence for rs1895062 as a likely causal variant that controls PAPPA gene expression and OA risk.

</details>

### [isoGS: A genomic method to navigate the breeder's dilemma of diversity versus eliteness](https://www.biorxiv.org/content/10.64898/2026.11.23.768689v1)
*Monyak, T.; Fall, S. T.; Opare-Obuobi, K. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.23.768689 v1 · relevance 0.09

- **In one sentence**: A simulation study proposes an isoeliteness score for founder lines and an isoeliteness-guided genomic selection (isoGS) method to manage the trade-off between adding genetic diversity and preserving favorable epistatic haplotypes in recurrent crop breeding.
- **In plain words**: Plant breeders often share seed lines across public programs to bring in new genetic variety, but mixing lines can break up gene combinations that already work well together, making the resulting populations harder to improve with computer-predicted selection. This paper uses breeding simulations of a self- and cross-pollinating annual crop to measure how genetically compatible founder lines are and to test a modified selection method. The authors report that low-compatibility founders gained less under standard genomic selection in early cycles, and that their adjusted method gave more gain after 4 and 20 cycles.
- **Why it matters**: Crop breeding networks need to balance new diversity against keeping elite traits intact, and this work offers a way to score that trade-off trait by trait before lines are combined. Because the results come from simulations rather than field trials, how well they carry over to real breeding programs is not established by the text.
- **Background needed**: - Genomic selection (GS): predicting which plants will perform well from their DNA markers, then using those predictions to choose parents.
- Founder lines: the starting parent lines that a breeding program crosses to create new populations.
- Elite gene pool: the set of high-performing lines a breeder keeps improving.
- Epistasis: when genes interact, so a combination of gene variants works well together but not separately.
- Haplotype: a block of linked gene variants inherited together from one parent.
- Transgressive segregation: offspring that show traits beyond either parent, which can be good or undesired.
- Hamming distance: a count of positions where two sequences differ; here weighted by how strongly each marker affects the trait.
- Quantitative trait loci (QTL): chromosome regions linked to measurable traits such as yield.
- Genetic gain: the improvement in average trait value over successive breeding cycles. · level: research-level

<details><summary>Original abstract</summary>

Global networks of public crop breeding programs exchange germplasm to share traits and increase diversity for genetic gain. There is a fundamental dilemma in crop breeding between the need to expand the genetic variation in elite gene pools while avoiding disruptions to essential traits required for eliteness. One particular challenge in admixed germplasm is the release of undesired transgressive segregation due to the disruption of favorable epistatic haplotypes of essential traits, which may stymie deployment of genomic selection (GS) In this study, we used breeding simulations to model recurrent population improvement for an annual crop species that can be selfed and crossed to examine the effectiveness of GS in admixed germplasm. We quantified the genetic heterogeneity between founder lines with an isoeliteness score, an effect size-weighted Hamming distance using quantitative trait loci markers. Populations with low founder isoeliteness (i.e. low genetic compatibility) had lower genetic gain with GS in early cycles than those with high founder isoeliteness (63% and 27% lower after 2 and 4 cycles). To mitigate this, we developed an isoeliteness-guided GS (isoGS) method to recover favorable epistatic haplotypes in a segregating population, which enabled 31% and 15% more genetic gain after 4 and 20 cycles. Our results suggest that founder isoeliteness scores and isoGS are valuable tools for overcoming the diversity vs. eliteness dilemma by managing the introduction of genetic diversity in a trait-specific manner.

</details>

## Cell and molecular biology

### [Allele-specific open chromatin analysis revealed allelic bias of alcohol-induced gene expression in human microglia](https://www.biorxiv.org/content/10.64898/2026.11.23.768544v1)
*Li, X.; Green, N.; Messenger, J. S. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.23.768544 v1 · relevance 0.10

- **In one sentence**: Integrates microglia-specific allele-specific open chromatin mapping with GWAS, eQTL, expression and ATAC-seq data to prioritize a non-coding AUD risk variant (rs7307261) and tests its effect on ethanol-induced CD163 expression and phagocytosis in iPSC-derived microglial-like cells.
- **In plain words**: Genetic studies have linked alcohol use disorder to many DNA variants, but most sit in stretches of DNA that do not code for proteins, so it is unclear which ones actually matter. This paper combines several existing datasets from human brain immune cells (microglia) and lab-grown look-alike cells to narrow the list, then tests one candidate variant, rs7307261, in the lab. The authors report that its minor allele is linked to higher CD163 expression after ethanol exposure, and that editing the variant changes both that response and how the cells engulf material.
- **Why it matters**: It offers one concrete example of tracing a common genetic association for alcohol use disorder to a specific regulatory variant, target gene and cell behavior, which is the step that GWAS alone rarely provides. The work is still early: it rests on one candidate variant and cell-culture assays, so its relevance to alcohol use disorder in people is not yet established.
- **Background needed**: - GWAS (genome-wide association study): a scan of many people's DNA to find variants that occur more often in people with a trait or disease.
- Non-coding DNA: regions that do not make proteins directly but help control when and how much genes are switched on.
- Allele: one of the alternative versions of a DNA letter at a given position; a variant such as rs7307261 has two alleles (A and G here).
- Open chromatin / ATAC-seq: DNA regions packed loosely enough for regulatory proteins to bind; ATAC-seq is a test that maps them.
- Allele-specific open chromatin (ASoC): checking which allele of a variant sits in an open region, to see if the variant affects regulation.
- eQTL: a variant associated with the expression level of a nearby gene.
- Microglia: immune cells of the brain; iPSC-derived microglial-like cells are similar cells grown from reprogrammed skin or blood cells.
- Transcription factors (e.g., ETS family, FLI1, ELF2): proteins that bind DNA motifs to switch genes on or off.
- CD163: a gene/protein involved in immune cell function; phagocytosis means cells engulfing debris or particles. · level: research-level

<details><summary>Original abstract</summary>

Alcohol use disorder (AUD) is a polygenic disorder. Most AUD-associated variants identified by genome-wide association studies (GWAS) are located in non-coding regions, making it challenging to determine which variants are functional and how they contribute to disease-relevant cellular phenotypes. Here, we integrated microglia-specific allele-specific open chromatin (ASoC) mapping, GWAS, eQTLs, differentially expressed genes identified from postmortem human microglia and iPSC-derived microglial-like cells, and chromatin accessibility (ATAC-seq) data from postmortem microglia to prioritize regulatory variants, followed by functional validation using multiple assays. We identified a panel of AUD-associated non-coding variants, particularly rs7307261, as a candidate functional variant that showed regulatory potential. The minor allele (A) of rs7307261 showed higher predicted similarity to binding motifs for E26 transformation-specific (ETS)-family transcription factors, including FLI1 and ELF2, than the G allele. The A allele was also associated with increased CD163 expression in AUD postmortem microglia and in iPSC-derived microglial-like cells after ethanol exposure. Notably, the ethanol-induced CD163 expression was abolished by knocking out rs7307261 or converting rs7307261 A/A to G/G, accompanied by changes in ethanol-induced microglial phagocytic function. Together, our study provides a framework for translating AUD genetic associations into context-specific functional mechanisms by linking non-coding risk variants to target genes and ethanol-induced cellular phenotypes.

</details>

### [Spatiotemporal Dynamics of Vascular Wall Cells during Ductus Arteriosus Development and Closure](https://www.biorxiv.org/content/10.64898/2026.11.23.768583v1)
*Sanderson, C.; Dahal, I.; Sinha, A. et al.* · `developmental biology` · bioRxiv doi:10.64898/2026.11.23.768583 v1 · relevance 0.09

- **In one sentence**: Spatial transcriptomic profiling of mouse ductus arteriosus (DA) and aorta from E14.5 to P2.5, with a human postnatal DA comparison, mapping temporal changes in mural, endothelial and fibroblast transcriptional programs during DA closure.
- **In plain words**: Shortly after birth, a temporary blood vessel near the heart called the ductus arteriosus must close so that blood flows to the lungs. This study tracked the cells in that vessel wall in mice across late pregnancy and the first days after birth, and compared them with the nearby aorta and a few human samples. The authors report that cells in the duct were more active in dividing and more contractile before birth, then shifted after birth toward a remodeling state that builds and breaks down the wall's structural material.
- **Why it matters**: Closure of this vessel is a normal part of the newborn's circulation change, and problems with it are clinically important in premature infants. The paper offers a spatial, stage-by-stage map of the cell types involved, which may help frame future work on vascular remodeling, though the text does not establish a direct clinical application.
- **Background needed**: - Ductus arteriosus: a fetal blood vessel linking the pulmonary artery and aorta, which normally closes after birth.
- Mural cells: smooth muscle-like cells that wrap the vessel wall; "contractile" means they tighten, while "synthetic" means they make structural material such as extracellular matrix.
- Extracellular matrix: the scaffold of proteins (such as collagen and elastic fibers) that gives vessel walls strength and flexibility.
- Transcriptome: the set of gene activity readouts in cells; spatial transcriptomics keeps this information tied to tissue location.
- Single-cell RNA sequencing: a method that measures gene activity in individual cells, used here as an independent comparison dataset.
- Embryonic day (E) and postnatal day (P): time markers counted from conception and from birth, respectively. · level: research-level

<details><summary>Original abstract</summary>

Background: The transition from fetal to postnatal circulation requires closure of the ductus arteriosus (DA), involving smooth muscle cell contraction followed by anatomical remodeling. However, the spatial organization and developmental transcriptional dynamics of vascular wall cells during this transition remain poorly understood. Methods: We analyzed vascular morphology and spatial transcript profiles of the mouse DA and aorta at five stages from embryonic day 14.5 (E14.5) to postnatal day 2.5 (P2.5), enabling paired comparisons within tissue sections. Selected findings were compared with an independent mouse single-cell RNA-sequencing dataset. Histological and spatial transcript analyses were also performed on human DA tissue and the adjacent pulmonary artery. Results: The DA exhibited transiently higher cell-cycle-associated transcription across multiple vascular wall populations at E16.5, preceding medial thickening at E18.5 and postnatal luminal closure. Prenatally, DA mural cells exhibited greater contractile-associated gene expression than aortic mural cells. This difference diminished after birth, accompanied by a marked shift toward synthetic-like transcriptional programs associated with extracellular matrix remodeling and proteolysis. Ductal endothelial cells exhibited postnatal divergence from aortic endothelial cells in matrix- and adhesion-associated gene expression. Adventitial fibroblasts displayed distinct extracellular matrix- and insulin-like growth factor-associated expression profiles. In a human postnatal DA specimen, synthetic-like mural cells were enriched in regions of disrupted elastic lamellae and prominent collagen staining and shared selected remodeling-associated markers with postnatal mouse DA mural cells. Conclusions: DA development and closure involve temporally organized transcriptional changes across vascular wall populations, characterized by prenatal cell-cycle-associated activity and rapid postnatal reorganization of mural transcriptional programs. These findings provide a spatial framework for understanding vascular cell plasticity and multicellular remodeling during DA closure.

</details>

## Immunology and microbiology

### [mRNA-1273.262 and mRNA-1283.262 Vaccines Expressing XFG Antigens Neutralize Relevant Circulating Variants](https://www.biorxiv.org/content/10.64898/2026.11.18.767652v1)
*Nasir, A.; Ogega, C.; Lee, D. W. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.18.767652 v1 · relevance 0.15

- **In one sentence**: Preclinical mRNA vaccine candidates encoding XFG-variant SARS-CoV-2 spike antigens (full-length and linked subdomain formats) are reported to elicit neutralizing responses against relevant JN.1-family variants in animal primary and booster models.
- **In plain words**: COVID-19 vaccines have to be updated each year to match the version of the virus that is spreading. This paper describes preclinical tests of new mRNA vaccines built around the XFG variant, which is proposed for the 2026-2027 season. In animals, the authors report that these vaccines produced strong antibody responses that neutralized related virus variants from the JN.1 family.
- **Why it matters**: Annual strain selection decides what millions of people are vaccinated against, so evidence supporting a specific choice matters for public health planning. The text is a brief summary, so the size of the effects, the comparison groups and the animal details are not available here, and it should be read as early evidence rather than a settled result.
- **Background needed**: - SARS-CoV-2 is the virus that causes COVID-19; it is now endemic, meaning it keeps circulating.
- The spike protein on the virus surface is the main target of mRNA vaccines, which give cells instructions to make this protein so the immune system learns to recognize it.
- Variants evolve over time; JN.1 is a widely circulating lineage, and XFG is a descendant variant of the JN.1 family.
- Neutralizing responses are antibodies that block the virus from infecting cells.
- "Primary series" means the initial vaccine doses; "booster" means later doses given to people already vaccinated.
- "Subdomain" antigens are smaller pieces of the spike protein used instead of the whole thing.
- Preclinical means tested in the lab or in animals, before human trials. · level: intermediate

<details><summary>Original abstract</summary>

SARS-CoV-2 continues to circulate and causes substantial disease burden as an endemic respiratory pathogen. Vaccination is a key public health measure to ameliorate the effects of COVID-19 disease but requires annual update to match strains that are circulating. Monitoring of circulating virus and characterization of matched candidate vaccines helps to inform which antigens will provide the greatest benefit to public well-being. The 2026-2027 season will leverage XFG as the variant of interest for vaccine production and in vitro and in vivo data was generated preclinically to support this selection. XFG variant vaccines express well in mRNA format as both full-length spike and linked subdomain antigen formats. Animals immunized with these vaccines elicit robust neutralizing responses to relevant JN.1-family virus variants in both primary series and booster models. In future seasons, robust epidemiologically monitoring including viral genome sequencing will improve early detection of relevant variants and subsequent preparation of vaccine antigens.

</details>

### [Longitudinal multiomics analysis in blood from individuals before and after HIV acquisition](https://www.biorxiv.org/content/10.64898/2026.11.23.767218v1)
*Moron-Lopez, S.; Garrido-Sanz, L.; Soriaga, L. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.23.767218 v1 · relevance 0.13

- **In one sentence**: A small longitudinal study combining single-nucleus chromatin and transcriptome profiling of blood cells with plasma metabolomic, lipidomic and cytokine measurements in five people sampled before HIV acquisition, during early infection, and after at least six months of antiretroviral therapy.
- **In plain words**: The paper follows five people's blood before they became infected with HIV, during the early weeks of infection, and after at least six months of suppressive drug treatment. Researchers measured gene activity in about 150,000 individual immune cells, along with small molecules in the blood such as metabolites, fats and inflammatory signals. They found that infection temporarily boosted some immune cell groups and inflammatory signals, while some changes in gene activity and in certain energy- and amino-acid-related molecules lasted even after treatment.
- **Why it matters**: Samples taken before HIV infection are rare, so a paired before-and-after view like this is unusual and can separate short-lived inflammation from lasting changes. Because the group is only five people, the findings are best read as a detailed case-level description that may generate hypotheses for HIV cure research rather than as firm general conclusions.
- **Background needed**: - HIV infects immune cells, mainly CD4 T cells, and antiretroviral therapy (ART) suppresses the virus but does not remove it from the body; a "cure" means eliminating or controlling the remaining virus.
- PBMCs are peripheral blood mononuclear cells, the white blood cells drawn from a blood sample (T cells, NK cells, monocytes and others).
- Single-nucleus multiome sequencing measures, in each cell, which DNA regions are open (chromatin accessibility) and which genes are active (transcription).
- Interferon and TNF-NF-κB are inflammatory signalling pathways the immune system uses to respond to threats.
- IP-10 is an inflammatory signalling protein (a chemokine) that rises during viral infection.
- Metabolome and lipidome are the full sets of small molecules and fats measured in plasma.
- "Nominal" decreases means changes that looked notable before correcting for multiple comparisons, so they need confirmation. · level: research-level

<details><summary>Original abstract</summary>

A comprehensive understanding of cellular immunity is essential for controlling viral infections, yet individual and coordinated immune responses continue to pose significant challenges in HIV cure research. Recent advances in single-cell and multiomics technologies provide powerful tools to dissect intricate multicellular behaviors and identify novel therapeutic targets. Direct characterization of HIV-induced immune alterations is challenging because matched samples obtained before HIV acquisition are rare. To better understand individual and coordinated cellular immune responses relevant to HIV cure research, we integrated single-nucleus chromatin-accessibility and transcriptomic profiling of 150,060 PBMCs with plasma metabolome, lipidome and soluble immune-profiling from five individuals before HIV acquisition, during early infection and after at least six months of suppressive antiretroviral therapy (ART). HIV acquisition expanded activated CD8 T and proliferating NK/CD8 T cells and induced cell-type-specific chromatin and transcriptional changes enriched for interferon, inflammatory and TNF-NF-{kappa}B programs, many persisting during ART. Multiome sequencing detected 32 HIV-positive cells which were associated with increased expression of IFI44L during early infection and ATAD3A after ART. Plasma IP-10 increased transiently, whereas eight energy- or amino-acid-related metabolites showed nominal decreases persisting after ART. These paired observations distinguish transient inflammatory responses from persistent molecular and metabolic perturbations after HIV acquisition.

</details>

## Cancer biology

### [Fishing for new immunotherapy compounds to boost innate tumor rejection](https://www.biorxiv.org/content/10.64898/2026.11.15.766748v1)
*Machado, A. B.; Labao-Almeida, C.; Oliveira, I. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.15.766748 v1 · relevance 0.10

- **In one sentence**: A zebrafish xenograft phenotypic screen of over 500 FDA-approved drugs identified tiotropium bromide, a muscarinic antagonist, which reprograms tumor-associated macrophages and synergizes with anti-PD-1 in a syngeneic CT26 mouse model.
- **In plain words**: Some tumors are cleared by the immune system when transplanted into zebrafish, while others take hold. The authors screened hundreds of approved drugs for ones that help the fish's innate immune system clear human colorectal and breast cancer cells. They report that tiotropium, an inhaled asthma and COPD drug, stood out, and that it works through immune cells called macrophages.
- **Why it matters**: It suggests a route to drug repurposing for immunotherapy resistance and points to the nervous system's influence on immunity as a possible target. The text reports mouse results with anti-PD-1 but does not show clinical use, so the translational value is still unproven.
- **Background needed**: - Innate immunity is the body's first-line, non-specific defense, including macrophages that engulf (phagocytose) cells.
- Zebrafish xenografts: human tumor cells transplanted into young zebrafish, which are transparent and allow fast in vivo imaging.
- Phenotypic screen: testing many compounds by their observable effect (here, tumor clearance) without knowing the target beforehand.
- Muscarinic receptors are nerve-signal receptors that respond to acetylcholine; antagonists block them.
- Anti-PD-1 is an immune checkpoint antibody that releases the brakes on T cells.
- CT26 is a mouse colon tumor line; NSG mice lack functional immune cells, so the drug's effect disappearing there implies immune involvement.
- Results so far come from preclinical models (fish and mice), not human patients. · level: research-level

<details><summary>Original abstract</summary>

Despite significant advances in cancer immunotherapy, tackling immunosuppression remains critical to achieve more effective responses. While developing the zebrafish xenograft model, we found that some human tumors engraft very efficiently ("progressors"), while others are cleared by the host ("regressors"). We showed that this was dependent on innate immunity, which recognizes and eliminates some cancer cells, while others are able to evade and suppress it. This opened an opportunity to perform an in vivo phenotypic drug screen to find compounds that induce clearance by boosting innate-tumor rejection. Zebrafish xenografts of human colorectal (CRC) and breast cancer (BC) that show a high engraftment/low clearance phenotype were used to screen over 500 FDA-approved small-molecule compounds, with tumor clearance serving as the phenotypic readout. The screen identified 23 hit compounds, of which six were effective across both cancer models. Mechanism-of-action enrichment analysis revealed a significant overrepresentation of autonomic nervous system-targeting drugs among the hits, particularly cholinergic ones. Immune profiling in myeloid reporter lines showed that the lead hit, Tiotropium bromide, a muscarinic receptor antagonist, reprograms tumor-associated macrophages toward a pro-inflammatory, anti-tumoral state. Tiotropium significantly increased macrophage phagocytosis, and macrophage depletion completely abolished its pro-clearance activity, establishing these myeloid cells as essential effectors. In a syngeneic CT26 colorectal mouse model, Tiotropium synergized with anti-PD-1 to control tumor growth and improve survival, outperforming all monotherapy arms. This effect was immune-dependent, as it was lost in immunodeficient NSG mice. Together, these findings demonstrate that in vivo phenotypic screening of FDA-approved compounds in zebrafish xenografts is a productive strategy for innate immune drug discovery in cancer. The identification of Tiotropium as a myeloid-reprogramming innate immune primer, together with the unbiased recovery of the neuro-immune axis as a druggable target, opens new avenues for overcoming immunotherapy resistance.

</details>

### [Beyond IgG: Oral Secretory IgA as a new efficient modality for cancer immunotherapy](https://www.biorxiv.org/content/10.64898/2026.11.23.768496v1)
*Brousse, M.; Pintat, A.; Favre-Bulle, O. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.23.768496 v1 · relevance 0.09

- **In one sentence**: A preclinical study in mice testing an orally delivered, mucosal-type secretory IgA antibody against CEACAM5 in colorectal and gastric cancer models, compared with an IgG1 version and cetuximab, alone and with chemotherapy.
- **In plain words**: Most cancer antibody drugs are given by injection into the bloodstream. This paper tests whether an antibody taken by mouth, in a form normally found in the gut lining (secretory IgA), can reach colorectal tumors and their spread to other sites and slow them down. In mouse models, the oral antibody (called ABC-101) concentrated in CEACAM5-positive tumors while staying at low levels in the rest of the body, and it did better than the comparison antibodies in slowing tumor growth and spread.
- **Why it matters**: If an oral antibody can work safely and selectively, it could offer a non-injected option for cancer treatment and a new way to use the immune system's mucosal defenses. The text reports only mouse experiments, so whether any of this carries over to people is unknown.
- **Background needed**: - Antibodies: immune proteins that bind a specific target; most cancer antibody drugs are IgG and given intravenously.
- Secretory IgA (SIgA): the antibody type the body uses on mucosal surfaces such as the gut; it is more resistant to digestion than IgG.
- CEACAM5: a protein often found at high levels on colorectal and gastric cancer cells, used here as the target.
- Cetuximab: an approved antibody drug used as a comparison.
- FOLFIRI and irinotecan: standard chemotherapy regimens for colorectal cancer.
- FcRI (CD89): a receptor on certain immune cells (neutrophils, monocytes, macrophages, dendritic cells) that the authors say the antibody helps recruit.
- Orthotopic model: human cancer cells implanted in the organ where the cancer naturally arises, in mice.
- Preclinical: tested in cells and animals, not yet in people. · level: research-level

<details><summary>Original abstract</summary>

Monoclonal antibody therapies have revolutionized cancer treatment but are almost exclusively based on intravenously administered IgG antibodies. Here, we developed and evaluated the first orally delivered anti-CEACAM5 secretory IgA (SIgA) for colorectal cancer. The pharmacokinetics, biodistribution, antitumor efficacy and immune effects of oral anti-CEACAM5 SIgA (ABC-101) were evaluated in an orthotopic metastatic human colorectal cancer model. Its therapeutic activity was compared with cetuximab, as monotherapy and in combination with irinotecan- or FOLFIRI-based chemotherapy along with that of an anti-CEACAM5 IgG1 sharing the same antigen-binding domain. Tumor-associated FcRI (CD89)-expressing myeloid populations were characterized at primary and metastatic sites. ABC-101 activity was evaluated on a second human cancer cell line, in vivo in an orthotopic human gastric cancer model. Oral anti-CEACAM5 SIgA (ABC-101) exhibited a unique pharmacokinetic profile, selectively accumulating in CEACAM5-positive primary tumors and metastases while maintaining minimal systemic exposure. Compared with the anti-CEACAM5 IgG1 and cetuximab, oral SIgA achieved superior inhibition of primary tumor growth and metastatic dissemination. It also enhanced the efficacy of irinotecan- and FOLFIRI-based chemotherapy, outperforming the FOLFIRI/cetuximab standard-of-care comparator. Mechanistically, ABC-101 remodeled the tumor immune microenvironment by promoting the recruitment of FcRI (CD89)-expressing neutrophils, monocytes, macrophages, and dendritic cells at both primary and metastatic sites, consistent with enhanced innate antitumor activity. Oral ABC-101 shows targeted activity against CEAhigh MKN-45 cells, reducing markers of cell proliferation and migration. These findings establish therapeutic SIgA as a first-in-class oral antibody immunotherapy combining selective tumor targeting, innate immune activation, and enhanced chemotherapy efficacy. More broadly, this work establishes mucosal immunity as a promising therapeutic frontier, demonstrating that orally delivered antibodies can enable systemic control of metastatic digestive cancers.

</details>

## Ecology and evolution

### [Social information use promotes breeding synchrony but constrains adaptation to rapid environmental changes](https://www.biorxiv.org/content/10.64898/2026.11.20.767538v1)
*Zheng, J.; Kuijper, B.; Aplin, L. M. et al.* · `animal behavior and cognition` · bioRxiv doi:10.64898/2026.11.20.767538 v1 · relevance 0.09

- **In one sentence**: An evolutionary individual-based model shows that breeding birds (or similar animals) copying neighbours' timing of breeding produces population-level synchrony that speeds adaptation in stable or abrupt-change settings but lags behind directional climate change.
- **In plain words**: Many animals decide when to breed partly by watching their neighbours, and this paper asks what that habit does to whether a population can keep up with a changing climate. Using a computer simulation of animals living in territories with resources that peak at certain times, the authors compared individuals that use neighbours' information with those that rely only on their own sensing. Copying neighbours made breeding times line up across the population, which helped under stable conditions but made the population slow to shift when the climate changed steadily.
- **Why it matters**: Timing of breeding is central to how wild populations respond to warming, so a mechanism that trades synchrony against flexibility could matter for predicting which species fall behind. The text only reports simulation results, so how far it applies to real species is not established here.
- **Background needed**: - Breeding phenology: the timing of reproduction within the year, often matched to when food peaks.
- Private information: cues an individual gathers itself (e.g., temperature, food).
- Social information: cues gained by observing others, such as neighbours starting to breed.
- Individual-based model: a simulation where each animal is tracked separately and can evolve over generations.
- Synchrony and lag: when many individuals act at the same time, and when a population trails a moving target (the environmental optimum).
- Information pooling: averaging many noisy signals to get a more accurate estimate. · level: research-level

<details><summary>Original abstract</summary>

Animals use social information to make decisions, yet how such processes influence predictions in reproductive timing and population adaptation under environmental change remains unclear. While social information can improve decision accuracy through information pooling, spatiotemporal heterogeneity in conditions and patterns of environmental changes creates noise that potentially limits the value of social information use among breeding individuals. Here, we established an evolutionary individual-based model to examine how social and private sensing interact to shape breeding phenology in species distributed across territories with peaked resources and facing annual fluctuations and rapid climate change. We show that when individuals incorporate social information from neighbours, behavioural responses become increasingly synchronised through positive feedback in decision-making. This emergent synchrony helps populations to adapt faster and can increase reproductive output under stable environmental conditions relative to relying only on private information. However, under directional climate change, the same mechanism reduces population responsiveness by constraining variation in individual responses, leading to systematic lag in tracking shifting environmental optima and reduced population reproductive output. Our results demonstrate that social information use can produce a general trade-off at the population level between synchronisation and adaptive flexibility across environmental contexts. Social interaction enhances population performance when environments are either consistent or changing drastically across both spatial and temporal scales. Rather than uniformly improving performance, social interaction may create conditions under which collective behaviour becomes maladaptive when environments change rapidly.

</details>

### [Stomatal conductance and net photosynthesis depend on nitrogen supply in drought-limited boreal forest](https://www.biorxiv.org/content/10.64898/2026.11.23.768591v1)
*Dulamsuren, C.; Amarjargal, D.; Bazar, D. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.23.768591 v1 · relevance 0.09

- **In one sentence**: In drought-limited Larix sibirica stands in Mongolia, nitrogen fertilization raised stomatal conductance as hypothesized, but net photosynthesis followed a non-linear pattern, peaking at a mid-level N dose and declining at the highest dose.
- **In plain words**: Boreal forests are shifting from being limited by cold to being limited by drought as the climate warms. This study fertilized Siberian larch trees in a dry Mongolian forest with different amounts of nitrogen and measured how their leaves exchanged carbon dioxide and water vapour. Stomatal conductance (how widely the tiny leaf pores open) rose with nitrogen, but photosynthesis did not simply rise with it: it fell at the lowest dose, peaked at the middle dose, and fell again at the highest dose.
- **Why it matters**: The results suggest that nutrient availability, not only temperature and rainfall, may shape how boreal trees cope with drought, which matters for forecasts of forest carbon uptake. The text does not show how far these branch-level measurements extend to whole forests or other years, so the broader significance is still to be tested.
- **Background needed**: Boreal forest: cold northern coniferous forest, here dominated by larch. Stomata: microscopic pores on leaves that let in carbon dioxide and let out water vapour. Stomatal conductance: how easily gas passes through those pores. Net photosynthesis: carbon gained by the leaf after subtracting carbon lost to respiration. Respiration: the energy-using process that releases carbon, which here rises with the cost of taking up nitrogen. Vapour pressure deficit: how dry the air is, which pulls water out of leaves. Nitrogen fertilization: adding nitrogen to soil as a plant nutrient, used here as an experimental treatment. Long-term experiment: a plot study run over years to compare treatments. · level: intermediate

<details><summary>Original abstract</summary>

Transition from cold limitation to drought limitation due to climate change is widespread in boreal forests. We explored in the scope of the Dry Boreal Forest Long-Term Nitrogen Fertilization Experiment (DryBoreal-LTNE) in southern boreal forests of Mongolia how N supply interacts with tree water and C relations in forests of Larix sibirica, which are naturally drought-limited. Using branches of mature L. sibirica subjected to N fertilization of 6.25-25 kg N ha-1 a-1, we conducted CO2/H2O gas exchange measurements to examine how N availability interferes with the climatic control of stomatal conductance (gs) in L. sibirica. We tested the hypotheses that gs increases with increasing N availability and that this increase can be translated into increased net photosynthesis (A) in L. sibirica even under the dry continental climate of Mongolia. We could confirm the first hypothesis and found that A decreased at low fertilization (6.25 kg N ha-1 a-1) probably caused by increases in respiration due to metabolic costs of intensified N uptake. A attained the highest values at 12.5 kg N ha-1 a-1, but declined at the highest fertilization level of 25 kg N ha-1 a-1. Our results demonstrate that research on the drought tolerance of boreal forests under climate change should not only focus on changes in temperature, vapor pressure deficit, and precipitation, but should take N availability into account, especially as N availability is thought to decrease in remote boreal forests due to elevated atmospheric CO2 concentrations and can be locally influenced by land use.

</details>

## Plant biology

### [Restoring beneficial ancestral genomic sites enhances broad disease resistance in rice](https://www.biorxiv.org/content/10.64898/2026.11.22.768253v1)
*Wang, J.; Liu, S.; Duan, Y. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.22.768253 v1 · relevance 0.16

- **In one sentence**: The paper proposes restoring conserved ancestral acidic residues at phosphorylatable sites in plant proteins, and reports that doing so in the NADPH oxidases OsRbohB and OsRbohI raises broad-spectrum disease resistance in rice.
- **In plain words**: Crops have been bred mostly from the genetic variants found in cultivated plants and their wild relatives, which cover only part of the diversity that evolution has produced over time. This work looks back at older versions of plant proteins and tries to bring back one specific feature, a negatively charged amino acid at sites where a protein can be chemically tagged to switch it on or off. The authors report that restoring this feature in two immune-related rice proteins increased resistance to several diseases.
- **Why it matters**: If the approach holds up, it suggests a way to improve crops using variation from deep evolutionary history rather than only from existing breeding material, which could matter for disease control. The text also says field tests were used to examine whether growth and defense trade off against each other, but the summary alone does not show the size or consistency of these effects, so the strength of the claims is not yet clear.
- **Background needed**: - Proteins are chains of amino acids; some amino acids are negatively charged ("acidic").
- Phosphorylation is the addition of a phosphate tag to a protein, often acting as an on/off switch for its activity.
- NADPH oxidases (Rboh enzymes) produce reactive oxygen molecules that plants use as part of their immune response.
- Growth-defense tradeoff: plants that invest heavily in defense may grow less, and the reverse.
- Ancestral sequence reconstruction: inferring what a gene's protein looked like in past species.
- The text is an abstract-level summary only; methods, sample sizes and detailed results are not included, so the claims cannot be checked from it. · level: research-level

<details><summary>Original abstract</summary>

Crop improvement has long been constrained to genetic variations within cultivated germplasms and their wild relatives, which capture only a small fraction of historical protein diversity accumulated over evolutionary processes. Here, we propose the Beneficial Ancestral Genomic Sites concept, hypothesizing that restoring conserved ancestral acidic residues at phosphorylatable sites in plant proteins could substantially improve plant performance. We experimentally validate this concept with key immune-associated NADPH oxidases OsRbohB and OsRbohI to elevate broad-spectrum disease resistance in rice. Field-level testing of two competing models for growth-defense tradeoffs in plants strongly supports mitigating tradeoffs in modern agricultural settings. Our work unlocks a hidden, untapped reservoir of elite molecular variations inaccessible from conventional breeding resources, establishing a potentially transformative strategy for next-generation crop improvement under modern agriculture contexts.

</details>

### [GnotoBag: A versatile peat-based gnotobiotic system for plant microbiome research beyond model species](https://www.biorxiv.org/content/10.64898/2026.11.22.768464v1)
*Wu, N.; Cheng, Y. T.; Paasch, B. C. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.22.768464 v1 · relevance 0.06

- **In one sentence**: The paper describes GnotoBag, a bag-based, peat-substrate gnotobiotic growth system that extends a previously published method to keep plants sterile or microbially defined for longer periods, with added ventilation and built-in water and nutrient delivery.
- **In plain words**: Scientists studying how plants interact with the microbes living around and in them need plants grown under tightly controlled conditions, free of unwanted microbes. This paper presents a improved growing setup, a sealed bag filled with peat, that keeps plants in this controlled state for longer, with better airflow and a way to feed them water and nutrients. The authors report that it supports the model plant Arabidopsis through flowering and can also hold larger plants such as rice and tomato for at least four weeks.
- **Why it matters**: Much of what is known about plant-microbe partnerships comes from small, simple model plants, and a reliable way to grow bigger crops under controlled microbes could let researchers test those findings on plants that matter for farming. The text does not report yield, crop-performance or field results, so its practical impact remains to be shown.
- **Background needed**: - Gnotobiotic: grown with a known, controlled set of microbes, or none at all (axenic), so effects of specific microbes can be isolated.
- Microbiome: the community of bacteria, fungi and other microbes living with a plant, including in its roots.
- Arabidopsis thaliana: a small flowering weed widely used as a laboratory model plant.
- Peat: a soil-like organic material used here as the growing medium.
- Vegetative vs. reproductive growth: the leafy growth phase compared with the flowering and seed-producing phase.
- The text gives no numbers beyond the timelines mentioned, and it does not show the detailed methods, so the description here is limited to the abstract. · level: intermediate

<details><summary>Original abstract</summary>

Plants and their microbial communities form a symbiotic system, where microbial communities play a key role in plant growth, development and stress resilience. However, the molecular mechanisms underlying plant-microbiota interactions remain poorly understood. A practical challenge is maintaining axenic conditions during prolonged plant growth while providing adequate space, ventilation, water, and nutrients. To advance research on plant-microbiome interactions, we developed the "GnotoBag" system, a bag-based extension of a previously established peat-based gnotobiotic plant growth platform. Key improvements of this GnotoBag system include enhanced ventilation and an integrated nutrient and water delivery system that sustains plant growth. These modifications support prolonged cultivation beyond the previously described 6.5-week workflow, enabling studies of microbiome effects on Arabidopsis thaliana growth and development under controlled microbial conditions, including the transition from vegetative to reproductive growth. Additionally, the expanded headspace of the GnotoBag provides sufficient space for cultivating larger plants, including rice and tomato, for at least four weeks. The increased headspace and the ability to add nutrients and water support research on larger crop plants, laying a foundation for future studies of microbiome functions in agricultural production.

</details>

## Bioengineering and synthetic biology

### [Extracellular matrix-enriched human induced chondrocyte organoids as living building blocks for scalable cartilage tissue engineering](https://www.biorxiv.org/content/10.64898/2026.11.23.768121v1)
*Menssen, D. M. A.; Mazzini, G.; Abinzano, F. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.23.768121 v1 · relevance 0.13

- **In one sentence**: Stem-cell-derived chondrocytes (hiCHOs) are matured in spinner flasks, then dissociated and recultured with a tissue-derived matrix supplement to form matrix-rich cartilage organoids that fuse into larger constructs.
- **In plain words**: Cartilage damage often leads to painful arthritis, and cartilage heals poorly, so repair treatments need large numbers of cells. This paper describes a way to grow cartilage-like clusters, called organoids, from an off-the-shelf stem-cell-derived cell source in stirred flasks. Adding a natural matrix supplement made the clusters form quickly and uniformly, and the authors report that 1 million cells yielded over 27,000 organoids in two weeks, which could then join into larger pieces of cartilage.
- **Why it matters**: Cell numbers are a practical bottleneck for cartilage repair, so a method that multiplies cells and produces uniform building blocks addresses a real unmet need. The text reports only lab-scale results, so whether this approach works in patients or for clinical repair is not shown here.
- **Background needed**: - Articular cartilage is the smooth tissue covering joint ends; it has very limited ability to heal itself.
- Organoids are small, self-organizing 3D clusters of cells that mimic aspects of a tissue.
- Induced pluripotent or progenitor cells are adult cells reprogrammed to a stem-like state, which can then be guided into a specific cell type such as chondrocytes (cartilage cells).
- Spinner flasks are stirred culture vessels that keep cells suspended and allow growth in larger volumes.
- Extracellular matrix is the network of proteins and sugars cells secrete around themselves; it provides structure and signals.
- Scalability means producing the same material reliably in much larger quantities. · level: intermediate

<details><summary>Original abstract</summary>

Articular cartilage defects are common and often develop into painful and debilitating osteoarthritis due to the low innate healing capacity of cartilage. However, current regenerative treatments are limited as they depend on large autologous cell numbers and poor scalability. Here, a novel approach for rapid and plentiful cartilage organoid production is introduced for modular and scalable cartilage tissue engineering, by combining an off-the-shelf cell source with a natural matrix supplement in spinner flask cultures. First, human induced chondroprogenitor cell (hiCPC) colonies are matured towards human induced chondrocytes (hiCHO) aggregates in spinner flasks. Although maturation is achieved, resulting hiCHO aggregates show some phenotypic heterogeneity between clones. Nevertheless, subsequent dissociation and culture with a tissue-derived matrix supplement results in rapid and homogeneous organoid self-assembly, generating large numbers of hiCHO-derived cartilage organoids. This matrix-supplemented culture generates consistent pericellular and extracellular matrix-rich organoids without detected off-target cells, limiting the need of labor-intensive selections steps and enhancing scalability. Impressively, 1 million hiCHOs produce over 27,000 organoids within two weeks, with an approximately 30-fold increase in cell number. Finally, hiCHO-derived organoids fuse together to assemble large cartilage constructs, demonstrating their potential as scalable, off-the-shelf building blocks and addressing an unmet need in regenerative cartilage tissue engineering.

</details>

### [Plasma-Polymerized Polyurethane/Reduced Graphene Oxide Electrospun Patch for Cardiac Tissue Engineering](https://www.biorxiv.org/content/10.64898/2026.11.22.768432v1)
*Jugie, C.; Mousavi, A.; Nemati, A. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.22.768432 v1 · relevance 0.12

- **In one sentence**: Electrospun polyurethane fiber patches containing reduced graphene oxide, surface-coated with a nitrogen-rich plasma polymer, are characterized for structure, strength, conductivity, and cytotoxicity toward primary cardiac fibroblasts as a cardiac tissue engineering scaffold.
- **In plain words**: Heart disease is a leading cause of death, and donor hearts are scarce, so researchers are trying to build patches that could support damaged heart muscle. This paper describes a flexible mesh-like patch made from a plastic-like polymer (polyurethane) mixed with a conductive carbon material (reduced graphene oxide), with a thin chemical coating to help cells stick. The authors report that the patch was tested for structure, stretch strength, electrical conductivity, and whether it was safe for heart-derived cells in the lab.
- **Why it matters**: Heart tissue conducts electrical signals, so a patch that is both stretchy enough and electrically conductive could be useful for repairing it. The text supports only early laboratory characterization and a basic cell-safety test; it does not show that the patch repairs heart tissue in animals or people.
- **Background needed**: - Cardiac patch: a thin scaffold placed on the heart to provide support and a surface for new tissue to grow.
- Electrospinning: a method that uses an electric field to draw polymer solutions into very fine fibers that form a mesh.
- Polyurethane: a flexible, durable plastic often used in medical devices.
- Graphene oxide / reduced graphene oxide: carbon sheets, one atom thick; the reduced form conducts electricity better.
- Plasma polymerization: exposing a surface to ionized gas to deposit a thin polymer coating.
- Cytotoxicity assay: a lab test checking whether a material harms living cells.
- Fibroblasts: common connective-tissue cells; primary cells are taken directly from tissue.
- Tensile testing: pulling a sample to measure how strong and stretchy it is. · level: intermediate

<details><summary>Original abstract</summary>

Cardiovascular diseases remain the leading cause of mortality worldwide. Traditional treatments, including heart transplantation, are limited by the scarcity of donor organs and the need for lifelong immunosuppression, highlighting the urgent need for alternative therapies. Cardiac patches represent a promising approach to restoring heart function by providing structural support and promoting cardiac tissue regeneration. Here, we developed biocompatible and conductive electrospun cardiac patches, aiming to mimic the structural, mechanical, and electrical properties of the native myocardium. polyurethane (PU) was selected as the base material due to its favorable mechanical properties and biocompatibility. Reduced graphene oxide (rGO) was incorporated into the electrospun PU fibers to enhance electrical conductivity, and a low-pressure plasma-polymerized nitrogen-rich (LPPE:N) coating was applied to improve cell adhesion. The fabricated patches were characterized through various techniques, including scanning electron microscopy, X-ray photoelectron spectroscopy, tensile testing, and conductivity measurements. Also, in vitro cytotoxicity assay using primary cardiac fibroblasts confirmed the biocompatibility of the patches. These physicochemical, electromechanical, and biological characterizations suggest that the rGO/LPPE:N-functionalized PU patches demonstrate promising potential for cardiac tissue engineering applications.

</details>

## Mathematical biology (arXiv)

### [Turbulent Epidemics: Scale-dependent Fluctuations as a Probe of Population Heterogeneity](https://arxiv.org/abs/2611.31334)
*Bernhard Mueller, Michael Lorke, M. Gabriela M. Gomes et al.* · `q-bio.PE` · arXiv:2611.31334v1 · relevance 0.13

- **In one sentence**: The paper adapts turbulence-style scale decomposition of fluctuation spectra to disaggregated COVID-19 data from Germany's 2020/21 winter wave and compares them with a network-based simulation (Epimetheus) of structured populations with clustering, heterogeneous susceptibility and superspreading.
- **In plain words**: Infections often spread unevenly, with some groups or places driving most cases. This paper borrows a mathematical tool from fluid dynamics that splits fluctuations into different size scales, and applies it to detailed case data from Germany's COVID-19 winter wave. The authors then run computer simulations of an idealized structured population to see which mixtures of clustering and uneven susceptibility could produce the same patterns.
- **Why it matters**: It offers a way to use the scale-by-scale pattern of case counts as a test of models that assume uniform mixing, which matters for predicting outbreaks and judging interventions. The text reports qualitative agreement only, and its claim that uniform transmission reduction alone does not explain the data is a model-based inference, so the findings should be read as suggestive rather than settled.
- **Background needed**: - Heterogeneity: infection risk differs between people, places or groups, rather than being the same for everyone.
- Superspreading: a small share of infected people cause a large share of new infections.
- Secondary attack rate: the fraction of close contacts of an infected person who become infected.
- Overdispersion: case counts vary more widely than a simple random model would predict.
- Fluctuation spectrum: a breakdown of how much variation occurs at each size scale, borrowed from turbulence analysis in fluid dynamics.
- Network-based simulation: a model in which individuals are nodes linked by contacts, and infection spreads along those links.
- Self-limiting effects: the epidemic slows on its own as people become immune or the susceptible pool shrinks. · level: research-level

<details><summary>Original abstract</summary>

Heterogeneous dynamics, including phenomena such as superspreading and clustering, is a hallmark of many infectious diseases. A key challenge lies in identifying observables that constrain heterogeneous dynamics. We here adapt the technique of turbulence decomposition from fluid dynamics to extract scale-dependent fluctuation spectra and correlation functions from disaggregated epidemiological data as a probe of population heterogeneity. To investigate possible explanations for the observed heterogeneities during the COVID-19 winter wave in Germany in 2020/21, we calculate synthetic observables using the new network-based simulation code \textsc{Epimetheus} for an idealized structured population. The code can flexibly incorporate clustering, heterogeneous connectivity and susceptibility, superspreading as well as temporal modulations of transmission risk and factors like waning of immunity and vaccination. A qualitative comparison of simulated and observed fluctuation spectra and correlation functions as well as the secondary attack rate and the overdispersion indicates that both clustering and variations of susceptibility across population substructures of all scales are required to produce the observed dynamics. Combined with heterogeneous connectivity, it is likely that self-limiting effects would have limited the winter outbreak to $0.2\texttt{-}0.35$ of the population without further behavioral changes after the autumn of 2020. A uniform population-wide reduction of transmission risk alone does not adequately explain the observed heterogeneities. Further analysis of the relative contributions and interplay of interventions and self-limiting effects on COVID-19 disease dynamics is required. We outline avenues towards a better integration of heterogeneity in models for predicting infectious disease dynamics and diagnosing effects of interventions.

</details>

### [Normative and neural network models of multisensory integration](https://arxiv.org/abs/2611.32829)
*Marcus Ghosh, John S. Butler* · `q-bio.NC` · arXiv:2611.32829v1 · relevance 0.06

- **In one sentence**: A review that organizes models of multisensory integration into normative (hypothesis-driven, statistically optimal) and neural network (circuit-emulating) classes, with accompanying equations and Python code.
- **In plain words**: This review looks at how brains combine signals from different senses, such as smell, sight and sound, into one picture. It sorts the many mathematical and computer models built to explain this into two groups: those that start from what the brain should ideally do, and those that try to mimic how real networks of neurons might do it. It also gives a beginner-friendly walkthrough of these models, with simple equations and code.
- **Why it matters**: Combining senses is a basic problem for both animals and artificial systems, so a clear comparison of the two modeling traditions may help researchers in neuroscience and machine learning see how their approaches connect. The text itself does not give specific new results, so its value lies mainly in synthesis and teaching.
- **Background needed**: - Multisensory integration: the brain merging information from several senses about the same event.
- Statistically optimal combination: weighting each cue by its reliability, as in Bayesian inference, so that the combined estimate is as precise as possible.
- Normative model: a model derived from a stated goal of how a system should behave, rather than from its physical wiring.
- Neural network model: a simulated network of simple units whose connections are tuned, here used to ask how circuits could do the same task.
- Basic familiarity with probability and simple equations is helpful; the review includes Python code. · level: intermediate

<details><summary>Original abstract</summary>

Animals continuously detect scents, sights and sounds, which their brains combine into diverse multisensory streams. Multisensory integration accelerates learning, increases reaction speeds and helps to resolve sensory ambiguities. In studying this process, the field has developed a continuum of models; from concise mathematical equations, with a handful of variables, to artificial neural networks, with billions of parameters. In this review, we divide this spectrum into two classes: normative models start from a hypothesis about how multisensory signals should be integrated, while neural network models aim to emulate how circuits could integrate them. Together, these models demonstrate that observers can integrate cues in a statistically optimal fashion, and help to explain experimental findings, including the diversity of multisensory neuron response profiles and network architectures. In this review, we provide a didactic overview of multisensory models, complete with accessible equations and Python code, and compare their assumptions and explanatory power. We detail what has been learned from these models. Finally, we discuss how the ideas and insights from classical theoretical models can be reconciled with those from artificial neural networks, and how this convergence should shape future research.

</details>

## Epidemiology

### [Improving Prediction of Patient-Reported Health Outcomes Among Older Adults With Diabetes Across Diverse Populations Through Transfer Learning](https://www.medrxiv.org/content/10.64898/2026.11.24.26368865v1)
*Wang, X.; Chen, Y.; Shao, W. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.24.26368865 v1 · relevance 0.08

- **In one sentence**: A regression-based transfer learning framework was tested for predicting patient-reported health outcomes in older adults with diabetes, borrowing information from international aging cohorts (Gateway) and across race/ethnicity groups in RAND HRS, with gains evaluated by AUC and Brier score.
- **In plain words**: Prediction models often work less well when moved to a new group of people. This paper asks whether borrowing information from other, related groups can help predict how older adults with diabetes rate their own health. The authors report that the borrowing helped in 6 of 8 international cohorts and in all four US race/ethnicity groups, though the gains were small (about 0.1% to 3.1% in AUC, a measure of how well a model separates cases from non-cases).
- **Why it matters**: Many prediction tools are built on one population and then applied to others, so a way to transfer information safely is relevant to public health. The gains reported are modest, and the text does not show how much they would matter in practice, so the value of the approach remains to be tested.
- **Background needed**: - Prediction model: a statistical rule that estimates a future outcome (here, a self-reported health outcome) from risk factors such as age, sex, and clinical measures.
- Transfer learning: reusing information from related datasets to improve a model in a target dataset, rather than building it from scratch.
- Target-only vs. pooled models: a model fit only on the group of interest versus one fit on all groups combined; the paper compares transfer learning against both.
- AUC: area under the ROC curve; ranges from 0.5 (no better than chance) to 1 (perfect separation). Gains are reported in percentage points.
- Brier score: a measure of prediction error, where lower values mean predictions closer to what happened.
- Bootstrap resampling: repeatedly resampling the data to estimate uncertainty in results.
- Gateway and RAND HRS: international aging cohort consortium and a US longitudinal survey of older adults, respectively. · level: intermediate

<details><summary>Original abstract</summary>

Population heterogeneity challenges the transportability of prediction models. Transfer learning may improve prediction through information borrowing, but its utility across population settings remains unclear. We evaluated a regression-based transfer learning framework across international aging cohorts (Gateway) and race/ethnicity groups within the RAND Health and Retirement Study (RAND HRS). Gateway included 19,879 adults with diabetes from eight cohorts, while RAND HRS included 3,926 participants across four race/ethnicity groups. Prediction models for patient-reported health outcomes were developed using demographic and clinical risk factors. Transfer learning was compared with target-only and pooled models using AUC and Brier score, with bootstrap resampling to assess uncertainty. Transfer learning improved prediction in 75% (6/8) of Gateway cohorts, with AUC gains of 0.1%-0.6%, and in all four RAND HRS race/ethnicity groups, with gains of 0.8%-3.1%. Improvements were greater and more consistent across within-cohort groups. These findings demonstrate the potential of regression-based transfer learning to improve prediction across heterogeneous populations. Information borrowing from sufficiently transferable external data may enhance prediction performance and provide meaningful public health benefits, even when improvements are modest, particularly in large population-based cohorts.

</details>

### [Disease-anchored organ aging clocks enable multi-organ risk profiling from routine labs](https://www.medrxiv.org/content/10.64898/2026.11.22.26368688v1)
*Shi, C.; Sun, Y.; Ruan, X. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.22.26368688 v1 · relevance 0.05

- **In one sentence**: The paper trains organ-specific aging clocks on first onset of disease in each organ using routine blood lab tests, then tests whether the frozen clocks select their own organ's proteins, predict own-organ disease, and add information to clinical risk scores across UK Biobank, NHANES and JMDC cohorts.
- **In plain words**: Doctors can estimate how old a person's organs are biologically by looking at blood markers, but existing methods mostly rely on chronological age and specialised protein tests. This paper builds "organ clocks" that are trained directly on which people later developed disease in a given organ, using ordinary lab tests. The authors report that the clocks pick out proteins from their own organ, predict disease in that organ across three cohorts, and add some information beyond standard clinical risk scores.
- **Why it matters**: Organ-specific risk from cheap, routine blood tests could help flag which organ is at risk, if the approach holds up outside the original study. The text does not show how large the gain over existing risk scores is, so the practical value remains to be judged.
- **Background needed**: - Biological age: how old tissues function, which can differ from calendar age.
- Organ clock: a model that estimates an organ's biological age from blood measurements.
- Proteomics: measuring thousands of proteins in blood; more costly than routine tests.
- Random protein panels: size-matched sets of random proteins used as a control to check that results are not just a generic effect.
- UK Biobank, NHANES (US), JMDC (Japan): large population cohorts with health records and follow-up.
- "Frozen" coefficients: the model is trained once and then applied without refitting to new cohorts.
- Clinical risk scores: standard tools that estimate disease risk from common factors; the test is whether organ clocks add to them. · level: research-level

<details><summary>Original abstract</summary>

Organ clocks estimate the biological age of organs from blood, but current clocks assign tissue-enriched proteins to organs and train on chronological age, which requires proteomics and does not yield organ-specific disease risk. In the UK Biobank, we trained organ clocks on first onset of disease of each organ using routine laboratory tests and froze the coefficients. Under an age label, organ-clock readouts arose equally in size-matched random protein panels; with a disease label, clocks selected their own organ's proteins and predicted their own organ's diseases. Defining extreme aging by multiples of disease risk concentrated flags on own-organ disease. Frozen clocks kept organ correspondence in the US NHANES cohort, predicted first onset of own-organ disease in the Japanese JMDC cohort and added more information to clinical risk scores than current organ clocks. Trained once where disease follow-up exists, organ clocks can be used wherever routine laboratory tests are measured.

</details>

## Infectious diseases

### [Efficacy, Immunogenicity, and Safety of an Inactivated Bivalent EV-A71-CVA16 Vaccine in Children: A Randomized Phase 3 Trial](https://www.medrxiv.org/content/10.64898/2026.11.23.26368796v1)
*Tong, Y.; Liang, H.; Tang, J. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.23.26368796 v1 · relevance 0.09

- **In one sentence**: A randomized phase 3 trial in about 8,000 children aged 6-71 months reports that a single inactivated vaccine targeting both enterovirus A71 and coxsackievirus A16 met its prespecified efficacy and EV-A71 immunogenicity noninferiority criteria against hand, foot, and mouth disease (HFMD).
- **In plain words**: Hand, foot, and mouth disease is a common childhood illness caused by several viruses, two of the main ones being enterovirus A71 and coxsackievirus A16. This trial tested a combined vaccine against both viruses, comparing it with an existing licensed EV-A71-only vaccine in young children. The combined vaccine prevented most of the coxsackievirus A16 cases seen in the comparison group, and its immune response to EV-A71 was not worse than the licensed vaccine's.
- **Why it matters**: Hand, foot, and mouth disease spreads widely among young children, and a vaccine covering both main causes could be useful for public health. The text reports efficacy and immune-response results, but it does not show long-term protection, and the trial's full data would be needed to judge how it compares with other approaches.
- **Background needed**: - Hand, foot, and mouth disease (HFMD): a usually mild childhood infection with fever, blisters on hands, feet, and mouth; rarely it becomes severe.
- Enteroviruses: a family of viruses that spread easily among young children; EV-A71 and CVA16 are two key causes of HFMD.
- Inactivated vaccine: a vaccine made from viruses killed so they cannot replicate, but still able to trigger an immune response.
- Bivalent vaccine: a vaccine containing two targets (here, two viruses) in one product.
- Randomized, double-blind trial: participants are assigned to groups by chance, and neither they nor the researchers know which vaccine is given, reducing bias.
- Vaccine efficacy: the percentage reduction in cases among vaccinated versus comparison children (here about 91%, with a 95% confidence interval of 75-98%).
- Seroconversion and geometric mean titer (GMT): measures of antibody response; seroconversion is the share of people who develop a detectable antibody rise, and GMT is the average antibody level on a log scale.
- Noninferiority: a test showing a new product is not meaningfully worse than an existing one.
- Phase 3: the large late-stage trial type used before regulatory review. · level: intermediate

<details><summary>Original abstract</summary>

Background Enterovirus A71 (EVA71) and coxsackievirus A16 (CVA16) cause hand, foot, and mouth disease (HFMD). We evaluated the efficacy, immunogenicity, and safety of a bivalent EVA71-CVA16 vaccine. Methods In this multicenter, double-blind, phase 3 trial, 8,000 healthy children aged 6-71 months were randomly assigned (1:1) to two doses of the bivalent or a licensed EVA71 vaccine, 1 month apart. The primary efficacy endpoint was RT-PCR-confirmed CVA16-associated HFMD with onset at least 14 days after dose 2. EVA71 immunogenicity noninferiority was assessed among baseline-seronegative participants without previous EVA71 vaccination. Results Of 7,975 participants receiving at least one dose, 7,419 underwent the primary efficacy analysis. CVA16-associated HFMD occurred in 4 bivalent-group versus 44 EVA71-group participants (vaccine efficacy, 90.91%; 95% CI, 75.03-97.63). At 30 days after dose 2, the EVA71 geometric mean titer (GMT) ratio was 2.04 (95% CI, 1.71-2.44) among baseline-seronegative participants without previous EVA71 vaccination. In the humoral immunogenicity population at this time point, CVA16 seroconversion rates were 96.94% versus 8.68%, and GMTs were 918.96 versus 3.88 U/mL. Adverse reactions within 30 days after either dose occurred in 46.73% versus 36.07% of reactogenicity-subgroup participants. In the overall safety population, serious adverse events occurred in 6.22% versus 7.55% from dose 1 through 6 months after dose 2; one bivalent-group event was considered possibly vaccine-related. No deaths occurred. Conclusions The bivalent EVA71-CVA16 vaccine met the prespecified efficacy criterion against CVA16-associated HFMD and the EVA71 immunogenicity noninferiority criterion in children aged 6-71 months (ClinicalTrials.gov: NCT06734832).

</details>

### [Deep Learning-based Phylodynamic Inference of Oropouche Virus Transmission Dynamics in Brazil Between 2023 and 2025](https://www.medrxiv.org/content/10.64898/2026.11.24.26368826v1)
*Arantes, I.; Bello, G.; Naveca, F. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.24.26368826 v1 · relevance 0.09

- **In one sentence**: A deep-learning birth-death model with explicit exposed stages for vectors and humans is used to estimate Oropouche virus transmission reproduction numbers (RHH) and infection durations across three Brazilian genomic clusters from 2023-2025.
- **In plain words**: Oropouche is a mosquito-borne virus that caused a large outbreak across the Americas in 2023 to 2025. The authors built a computer model that follows the virus as it passes back and forth between mosquitoes and people, and used it to reconstruct how the virus spread in Brazil from viral genome sequences. They report that the model gives more accurate estimates than a standard approach in simulations, and that the estimated spread was substantial in both an area where the virus is already common (Amazon) and one where it is not (Atlantic Forest).
- **Why it matters**: Oropouche has spread to new areas, so estimates of how easily it passes between people and mosquitoes matter for public health planning. The method is a modelling advance that may help other vector-borne viruses, but the text is only an abstract, so the results have not been checked here in full detail.
- **Background needed**: - Phylodynamics: inferring how an outbreak spread over time from the genetic differences between viral genome sequences.
- Birth-death model: a standard statistical model in which lineages "branch" (transmission) and "end" (recovery or sampling) over time.
- Reproduction number (R): the average number of new infections caused by one infected case. Here RVH and RHV are the steps from human to mosquito and back, and RHH is their product, the expected new human infections per infected person per full cycle.
- Exposed (E) stage: the incubation period after infection, before a host becomes infectious.
- Reassortant lineage M1L2S2: a virus variant formed when segments of two viral strains are swapped.
- Deep learning: machine-learning methods using layered neural networks, here used to make the inference. · level: research-level

<details><summary>Original abstract</summary>

Oropouche virus caused an unprecedented epidemic across the Americas during 2023-2025, associated with the expansion of the reassortant M1L2S2 lineage. To investigate its dissemination, we develop the Birth-Death Exposed-Infectious Vector-Human (BDEIVH) model within a deep-learning framework that explicitly represents alternating human-vector transmission and incubation periods. The model defines two directional reproduction numbers, RVH and RHV, whose product, RHH, quantifies the expected number of secondary human infections generated by a single infectious human through one complete transmission cycle. In simulations, BDEIVH provides more accurate RHH estimates than conventional birth-death models, with predictive accuracy improving with phylogeny size and remaining robust under reduced phylogenetic resolution. Across three major Brazilian OROV genomic clusters, estimated durations of infection range from 15.4 to 18.5 days in vectors and from 9.42 to 12.3 days in humans, whereas whole-cluster RHH estimates range from 1.15 to 1.81. RHH estimates reached a peak of 4.4 in the endemic Amazon region and 3.0 in the non-endemic Atlantic Forest region. These findings show that explicitly modelling vector-mediated transmission improves phylodynamic inference and reveals substantial OROV transmission in both endemic and non-endemic regions.

</details>

## Public and global health

### [Procedure composition, age and race/color in gender-affirming surgical authorizations of the Brazilian public health system, 2014-2025](https://www.medrxiv.org/content/10.64898/2026.11.23.26368723v1)
*dos Santos, J.; Amorim Costa, C. M.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368723 v1 · relevance 0.09

- **In one sentence**: A nationwide descriptive study of 1,375 Brazilian Unified Health System (SUS) hospital admission authorizations for gender-affirming surgery from 2014 to 2025, classified by procedure code direction, reporting shifts in feminizing versus masculinizing procedure mix, recorded age and race/color, and hospital habilitation counts.
- **In plain words**: This paper looks at records of surgeries that Brazil's public health system paid for to help people align their body with their gender, covering 2014 to 2025. The authors sorted billed procedure codes by whether they feminize or masculinize the body, then counted them over time. They found the share of feminizing procedures fell from about 82% in 2014–2018 to 50% in 2024–2025, and that the two groups relied on very different types of surgery.
- **Why it matters**: Public health-system billing records are increasingly used to describe gender-affirming care, so the paper's point that these codes show procedure type but not identity, clinical need or access is useful for anyone reading such counts. The authors suggest monitoring should use procedure-specific indicators and versioned code definitions, but the records cannot answer equity questions by themselves.
- **Background needed**: - SUS (Sistema Único de Saúde): Brazil's publicly funded national health system.
- AIH (hospital admission authorization): a billing record for a hospital admission paid by the public system; it does not identify the person or record their gender identity.
- Hospital Information System (SIH): the national database holding these monthly billing files.
- Procedure codes: standardized billing codes whose meaning can change over time, so the study used a versioned classification.
- Feminizing vs. masculinizing procedures: the direction a surgery is inferred to move the body; this is read from the code, not from the patient.
- Descriptive study: it reports counts and proportions; it does not test causes or estimate population rates.
- Habilitation: official accreditation of a hospital to provide a specific service.
- Parda: an official Brazilian census category for mixed race/color, recorded here in pooled, unadjusted comparisons. · level: intermediate

<details><summary>Original abstract</summary>

Hospital admission authorizations from publicly financed health systems are increasingly used to describe gender-affirming surgery, although they record billed procedures whose feminizing or masculinizing direction can be inferred from the code, without identifying people, self-reported gender identity or clinical need. This nationwide descriptive study examined the authorizations for gender-affirming surgery processed by the Brazilian Unified Health System from 2014 to 2025, which were selected from 3,888 public monthly state files of the Hospital Information System with a historically versioned classification of procedure codes. Of the 1,375 selected authorizations, 711 corresponded to directly feminizing procedures, 428 to directly masculinizing procedures and 236 to a complementary procedure that was analyzed separately. The feminizing share of the directly classified authorizations decreased from 81.7% (196/240) in 2014-2018 to 72.2% (213/295) in 2019-2023 and to 50.0% (302/604) in 2024-2025, proportions that describe composition within periods of unequal length and cannot be read as population rates. In 2024-2025, bilateral mastectomy accounted for 264 of the 302 masculinizing authorizations (87.4%), whereas bilateral breast reconstruction with silicone implants accounted for 118 of the 302 feminizing authorizations (39.1%). The median recorded age was 35 years in feminizing and 30 years in masculinizing authorizations over the whole period, and 34 and 29 years when the comparison was restricted to 2024-2025. The brown (parda) race/color category was recorded in 42.6% (303/711) of feminizing and 61.0% (261/428) of masculinizing authorizations, in a comparison pooled over the whole period and not adjusted for period or procedure. The number of hospitals habilitated for these surgeries remained at five from 2014 to 2022 and doubled in 2023. All aggregate results were reproduced by an independent pipeline that re-read every original public file. It was observed that the equal numbers of feminizing and masculinizing authorizations in the most recent period resulted from markedly different procedure portfolios, which suggests that the monitoring of publicly funded gender-affirming surgery may benefit from procedure-specific indicators and versioned code definitions, while questions of access and equity would require person-level and patient-reported data.

</details>

### [Developing a Stakeholder-Driven One Health Collaboration Framework for Bovine Tuberculosis Control at the Human-Animal Interface in Lundazi and Monze Districts, Zambia](https://www.medrxiv.org/content/10.64898/2026.11.23.26368721v1)
*Phiri, A.; Zulu, M.; Phiri, M. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368721 v1 · relevance 0.07

- **In one sentence**: A qualitative study of 104 focus-group participants and 10 key informants in two Zambian districts that identifies barriers to veterinary-medical collaboration on bovine tuberculosis and proposes a five-pillar One Health framework for district-level action.
- **In plain words**: This paper looks at bovine tuberculosis, a cattle disease that can pass to people through raw milk, undercooked meat, and handling infected animals. Researchers in two rural Zambian districts held group discussions and interviews with farmers, abattoir workers, vets, doctors, and government officials. They found that the animal and human health sectors work largely separately, and they drafted a framework for closer teamwork built from the participants' own suggestions.
- **Why it matters**: Zoonotic diseases that spread between animals and people are often under-reported in rural areas, and the paper ties this to a gap between national policy and what happens in districts. The authors say the framework may also suit other zoonoses such as brucellosis, anthrax and rabies, but the study itself covers only tuberculosis in two districts, so that wider applicability is untested.
- **Background needed**: - One Health: the idea that human, animal and environmental health are linked and should be tackled together.
- Zoonosis: an infection that moves between animals and people.
- Mycobacterium bovis: the bacterium that causes bovine tuberculosis in cattle; it is related to the human tuberculosis bacterium but is a different organism.
- Qualitative study: research based on interviews and group discussions rather than numerical measurements.
- Focus group discussion: a guided conversation with a small group of people about a topic.
- Thematic analysis: sorting interview content into recurring themes.
- Abattoir and carcass condemnation: slaughterhouse processing, and removal of meat from sale when it is found to be unfit. · level: intermediate

<details><summary>Original abstract</summary>

Background: Bovine tuberculosis, caused by Mycobacterium bovis, is a neglected zoonosis at the human-animal interface in Zambia, particularly affecting cattle-dependent rural communities in Eastern and Southern Provinces, where cattle are central to livelihoods, nutrition, and cultural identity. While Zambia has a One Health Strategic Plan 2022-2026 and a One Health Secretariat under Zambia National Public Health Institute, operational collaboration between veterinary and medical sectors at district level remains fragmented, contributing to diagnostic gaps, under-reporting, and continued transmission through consumption of raw milk, undercooked meat, and occupational exposure during slaughter and handling of infected carcasses. The disconnect between national policy and district implementation has created a vacuum where frontline workers operate in isolation despite sharing the same disease burden. Methods: This qualitative exploratory study was conducted in Lundazi District (Eastern Province) and Monze District (Southern Province), Zambia, from February to June 2022. Ten Focus Group Discussions were conducted with 104 participants, including cattle farmers, cattle businessmen, abattoir workers, veterinary and para-veterinary professionals, and medical doctors, and ten Key Informant Interviews were conducted with District Veterinary Officers, District Medical Officers, Ministry of Health officials, and Ministry of Fisheries and Livestock officials. Participants were purposively selected based on their role, experience, and knowledge of bovine tuberculosis and One Health collaboration. Discussions were held in local languages (Tumbuka, Tonga, Chewa), audio-recorded with consent, transcribed verbatim, translated into English, and imported into NVivo 12 (QSR International, Melbourne, Australia) for thematic analysis following Braun and Clarke's six-step approach, with framework matrices for triangulation and trustworthiness. This methodological rigor ensured that diverse voices from community to policy level were systematically captured and compared. Results: Five themes emerged: (1) awareness of bovine tuberculosis, (2) socio-economic impacts, (3) public health impacts, (4) cultural practices and transmission, and (5) collaboration gaps and proposed framework. Medical and veterinary professionals demonstrated excellent awareness, while cattle farmers and abattoir workers showed poor awareness. Socio-economic impacts included reduced milk yield and carcass condemnation. Key barriers to collaboration included lack of diagnostic capacity at district hospitals to differentiate Mycobacterium bovis from Mycobacterium tuberculosis, siloed training curricula, absence of formal round-table coordination mechanisms, and limited funding. An existing enabler was informal collaboration in meat inspection between veterinary assistants and environmental health officers. Based on these findings, a five-pillar One Health Collaboration Framework is proposed. This framework was co-constructed from participant recommendations, making it contextually grounded and acceptable to end-users. Conclusion: Effective control of bovine tuberculosis in Zambia requires institutionalized One Health collaboration, moving from informal ad hoc interactions to formal governance structures. The proposed framework provides a practical, low-cost and contextually grounded roadmap for district-level implementation and is applicable to other zoonoses such as brucellosis, anthrax and rabies. Its implementation can help break the cycle of under-reporting and under-funding that currently sustains zoonotic transmission in rural Zambia

</details>

## Psychiatry and neurology

### [Plasma proteomic markers of cognitive and brain aging in a multi-ethnic cohort](https://www.medrxiv.org/content/10.64898/2026.11.22.26368682v1)
*Wood, B.; Wood Alexander, M.; Clappison, A. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.22.26368682 v1 · relevance 0.09

- **In one sentence**: A plasma proteomics study of 250 older adults from three ethnic groups links blood levels of 220 neurology-related proteins to cognition, brain MRI markers, and cognitive decline, with selected findings replicated in 1,381 ADNI participants.
- **In plain words**: Researchers measured 220 proteins in blood samples from 250 older adults of Chinese, South Asian, and non-Hispanic White backgrounds. They looked for links between these proteins and thinking ability, brain scan measures, and heart and metabolic health. Several proteins tied to Alzheimer's-type tau, brain synapses, oxidative stress, and inflammation were linked to poorer cognition, and some findings were checked in a separate larger US cohort.
- **Why it matters**: Blood tests that reflect brain aging could be cheaper and easier than brain scans or spinal fluid tests, and including ethnically diverse participants addresses a gap in Alzheimer's research. The text does not show whether these markers would be useful for diagnosis or treatment, so that remains open.
- **Background needed**: - Plasma proteomics: measuring many proteins at once in a blood sample.
- Tau (pTau, BDpTau): a protein that forms tangles in Alzheimer's disease; phosphorylated forms are studied as blood markers.
- Entorhinal thickness: thickness of a brain region involved in memory, measured on MRI.
- Cerebral small vessel disease: damage to tiny blood vessels in the brain, visible on imaging.
- Cross-sectional vs. longitudinal: the main sample is a single snapshot; the ADNI replication tracks people over time.
- ADNI (Alzheimer's Disease Neuroimaging Initiative): a large, mostly US research cohort.
- Associations shown here do not establish that a protein causes brain aging. · level: research-level

<details><summary>Original abstract</summary>

Advances in ultrasensitive proteomics offer opportunities to characterize molecular pathways underlying brain aging. We measured 220 plasma proteins using NULISAseq Neuro220 in 250 Chinese, South Asian, and non-Hispanic White older adults (mean age=68.2 years, 70.4% female). Proteins implicated in neurodegenerative diseases (including brain-derived phosphorylated Tau, BDpTau), synaptic function, oxidative stress, and inflammation were associated with poorer cognition. Phosphorylated Tau205 was associated with reduced entorhinal thickness, whereas inflammatory proteins were associated with imaging markers of cerebral small vessel disease. Several findings were replicated in 1,381 participants in the Alzheimer's Disease Neuroimaging Initiative, including associations of BDpTau species, NPTX2, BACE1, TREM1, CCL17, PRDX6, and IGF1R with cognitive decline and clinical progression. Cardiometabolic risk factors were associated with widespread proteomic alterations, many of which were also linked to poorer brain health. These results identify promising molecular markers of brain aging and extend proteomic research to ethnically diverse populations historically underrepresented in Alzheimer's disease research.

</details>

### [Nigral volume as a marker for Lewy body copathology in Alzheimer's disease](https://www.medrxiv.org/content/10.64898/2026.11.23.26368759v1)
*langley, j.; Hwang, K. S.; Hu, X. P.* · `neurology` · medRxiv doi:10.64898/2026.11.23.26368759 v1 · relevance 0.09

- **In one sentence**: In 73 ADNI participants with clinical AD or MCI, lower antemortem neuromelanin-MRI substantia nigra volume was associated with autopsy-confirmed Lewy body copathology and with greater nigral hypopigmentation at autopsy, in a single-cohort analysis.
- **In plain words**: Some people diagnosed with Alzheimer's disease or mild cognitive impairment also have Lewy body deposits in the brain, a second protein problem that tends to bring earlier symptoms and faster memory and thinking decline. This study checked whether a brain scan of a midbrain region called the substantia nigra, read with a special MRI that picks up its dark pigment, could flag those people while they were still alive. Scans taken before death were compared with brain examinations after death, and smaller nigral volume was linked to Lewy body presence.
- **Why it matters**: If confirmed, a non-invasive scan could help identify Alzheimer's patients who also carry Lewy body pathology, which may matter for diagnosis and for how their decline is expected to go. The study is small, comes from one cohort, and the gap of several years between scan and autopsy limits how closely the findings reflect the brain at the time of scanning, so it is best read as an early signal.
- **Background needed**: - Alzheimer's disease (AD): the most common dementia, marked by amyloid and tau protein deposits in the brain.
- Mild cognitive impairment (MCI): noticeable memory or thinking problems that are not yet severe enough to count as dementia.
- Lewy bodies: clumps of the alpha-synuclein protein; they are the hallmark of Parkinson's disease and dementia with Lewy bodies, and can co-occur with AD.
- Substantia nigra: a midbrain area that makes dopamine and contains dark pigment (neuromelanin); losing it is a known feature of Parkinson's disease.
- Neuromelanin-sensitive MRI: a scan technique that highlights this pigment so the region's size and darkness can be measured in living people.
- Autopsy confirmation: the brain is examined after death, which is the reference standard for whether Lewy bodies were present.
- ADNI: the Alzheimer's Disease Neuroimaging Initiative, a research database of scans and clinical data. · level: research-level

<details><summary>Original abstract</summary>

Background: Lewy body (LB) copathology in Alzheimer's disease (AD) is associated with earlier symptom onset and faster cognitive decline. Depigmentation of substantia nigra pars compacta (SNc) volume is seen in both Parkinson's disease and dementia with Lewy bodies. We examined whether lower antemortem SNc volume was associated with autopsy confirmed LB pathology in patients with AD or mild cognitive impairment (MCI). Methods: Seventy-three participants with a clinical diagnosis of AD or MCI, neuromelanin-sensitive MRI, and subsequent neuropathologic assessment from the Alzheimer's Disease Neuroimaging Initiative were studied. At autopsy, 33 participants had LB pathology (LB+) and 40 had no LB pathology (LB-). We compared SNc volume between groups using analysis of covariance adjusted for age and sex. Within the LB+ group, we assessed the association between SNc volume and nigral hypopigmentation using Spearman correlation. In a secondary analysis, we tested whether adding SNc volume to a logistic regression mode containing age, sex, and executive function improved model fit for autopsy-defined LB status. Results: LB+ participants had greater nigral hypopigmentation at autopsy and lower antemortem SNc volume than LB- participants. The adjusted mean difference in SNc volume (LB+ minus LB-) was -66 mm3 (95% confidence interval -115.9 to -16.2, P=0.010). Within the LB+ group, lower SNc volume was associated with greater hypopigmentation (Spearman rho;=-0.373, P=0.032). Among 71 participants with complete model data, adding SNc volume improved model fit (likelihood ratio=8.67, P=0.003). The combined model had an in sample area under the receiver operating characteristic curve of 0.770 (95% confidence interval: 0.661-0.879). Conclusion: The correspondence between lower antemortem SNc volume and greater hypopigmentation at autopsy supports the use of neuromelanin-sensitive MRI to characterize nigral involvement in AD or MCI with LB copathology. These findings are based on a single cohort, and the interval of several years between imaging and autopsy limits how closely the pigmentation ratings reflect nigral integrity at imaging.

</details>

## Oncology

### [The cellular neighbourhoods of adult gliomas and their clinical associations](https://www.medrxiv.org/content/10.64898/2026.11.24.26368523v1)
*Mathioudaki, A.; Rutz, S.; Seferbekova, Z. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.24.26368523 v1 · relevance 0.06

- **In one sentence**: A single-cell spatial transcriptomic atlas of 275 adult glioma patients (about 2.6 million cells) reports recurrent multicellular neighbourhoods across glioma types, with some neighbourhood abundances linked to survival in astrocytoma.
- **In plain words**: Adult brain tumours called gliomas come in several types that behave differently, yet they grow in the same part of the body. This study mapped where different cell types sit inside 275 tumours, using a method that measures which genes are active in each cell and where it is located. The authors found that tumour cells group into repeating local "neighbourhoods" with characteristic mixes of immune and support cells, and that some of these neighbourhoods relate to patient survival.
- **Why it matters**: It suggests a spatial layout of tumour cells that goes beyond the standard microscope-based grading, which could in principle inform prognosis. The text does not show that these neighbourhoods would change treatment, and the survival link is reported for astrocytoma only, so clinical use remains unproven.
- **Background needed**: - Gliomas: the most common primary malignant brain tumours in adults, with several molecular types (glioblastoma, oligodendroglioma, astrocytoma, ependymoma).
- IDH mutation and 1p/19q codeletion: molecular markers that define tumour subtypes and affect outcome.
- WHO grade: a standard score from tissue examination that indicates how aggressive a tumour looks.
- Spatial transcriptomics: a method that measures gene activity in cells while keeping their physical positions in a tissue slice.
- Cellular neighbourhood: a group of nearby cells with a recurring mix of cell types.
- AC-like: astrocyte-like tumour cell state, a type of support-cell-like state.
- H&E: routine hematoxylin and eosin stain used to view tissue under a microscope. · level: research-level

<details><summary>Original abstract</summary>

Glial tumours are the most common primary malignant brain tumours in adults and comprise molecularly and histologically distinct entities with diverse outcomes. Despite this diversity, they arise within a shared anatomical environment, suggesting that common organisational principles may shape tumour heterogeneity. However, how cellular states are organised across gliomas and whether this organisation relates to clinical outcomes remains unclear. To that end, we generated a single-cell resolution spatial transcriptomic atlas of 2.6 million cells from 275 patients spanning IDH-wildtype glioblastoma, IDH-mutant and chromosome 1p/19q codeleted oligodendroglioma, IDH-mutant astrocytoma and ependymoma. Across diagnoses, we show how heterogeneous tumour cell states are spatially organised into recurrent neighbourhoods with distinct immune and glial composition, which in turn assemble into a higher-order architecture. Among these cellular neighbourhoods, some, such as the astrocyte-like (AC-like), are conserved across entities, whereas others segregate by clinicopathological parameters. AI-powered histopathology further reveals selective association of neighbourhoods within histological clusters, providing a link between molecular spatial organisation to routine H&E morphology. In astrocytoma, neighbourhood abundance is associated with patient survival independently of WHO grade, with AC-like enrichment linked to favourable outcomes. Same-cell high-plex spatial transcriptomics and multiplexed protein imaging in an independent astrocytoma cohort validated these neighbourhoods and further confirmed enrichment of oligodendrocytes within the TBI neighbourhood. Collectively, our findings reveal that glial tumours are spatially encoded through recurrent multicellular neighbourhoods across different molecular entities, showing clinical relevance beyond conventional histology and providing a foundation for analogous investigation across cancer types.

</details>

### [Integrated real-world and translational studies nominate CREB binding protein/EP3001 inhibition to overcome androgen receptor pathway modulator resistance in men with prostate cancer](https://www.medrxiv.org/content/10.64898/2026.11.24.26368506v1)
*Somarelli, J. A.; Dougherty, B. V.; Beckmann, A. G. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.24.26368506 v1 · relevance 0.06

- **In one sentence**: Regulatory network models built from multi-omic data of over 10,000 prostate cancer patients point to EP300/CBP as a target in androgen pathway modulator-resistant disease, supported by preclinical work with the inhibitor pocenbrodib and one clinical case.
- **In plain words**: Hormone-blocking drugs for advanced prostate cancer usually stop working over time, and doctors need new targets for cancers that have become resistant. The authors used computer models of gene regulation, fed with genetic and molecular data from many patients, to find a protein called EP300 (and its close partner CBP) that seemed linked to resistance. They then tested a new drug that blocks these proteins, pocenbrodib, in lab and animal studies, and report one patient who benefited.
- **Why it matters**: Resistance to hormone-pathway drugs is nearly universal in metastatic prostate cancer, so a new candidate target is of interest. The evidence is still early: it rests on lab and animal experiments and a single patient, so whether it helps patients in general is not yet shown.
- **Background needed**: - Androgen pathway modulators (APMs): drugs that block male hormone (androgen) signalling, which fuels prostate cancer growth.
- Androgen receptor: the protein that androgens bind to; it switches on genes that drive tumour growth.
- Therapy resistance: when a cancer stops responding to a drug that once worked.
- EP300 / CBP: two related proteins that add chemical tags (acetyl groups) to other proteins and help control gene activity.
- Multi-omic data: measurements across several layers of biology (genes, RNA, proteins, etc.) from the same samples.
- Regulatory network model: a computer map of which genes and proteins influence one another.
- Oxidative phosphorylation and fatty acid metabolism: the cell's energy-producing processes that the inhibitor was found to suppress.
- Preclinical: tested in cells and animals, not yet proven in people. · level: research-level

<details><summary>Original abstract</summary>

Androgen pathway modulators (APMs) have significantly improved outcomes for men with metastatic prostate cancer, but the evolution of therapy resistance is nearly universal, and there remains a major clinical need to identify actionable vulnerabilities for therapy-resistant disease. To address this need, we employed regulatory network models that leverage multi-omic data from over 10,000 prostate cancer patients with longitudinal clinical data. Analysis of the architecture of the network models identified EP300 as the top actionable target associated with androgen receptor-mediated therapy resistance. These observations were validated using a novel inhibitor of CBP/EP300, pocenbrodib, which showed preclinical activity in vitro and in vivo. Acetylomics analysis and functional studies pinpointed inhibition of oxidative phosphorylation and fatty acid metabolism as key mechanisms of action for pocenbrodib. Clinical benefit for this agent was demonstrated in a patient with metastatic APM-resistant prostate cancer (NCT04575766), highlighting CBP/EP300 as a key target for further translation.

</details>

## Health informatics and medical AI

### [Effect of a feedback loop on clinical prediction model performance](https://www.medrxiv.org/content/10.64898/2026.11.23.26368745v1)
*Pacynko, S.; Sperrin, M.; Jenkins, D.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368745 v1 · relevance 0.17

- **In one sentence**: A simulation study of how clinical prediction models that guide treatment decisions degrade when refitted on data generated by their own use, with and without treatment included as a predictor and with unmeasured confounding.
- **In plain words**: Medical risk calculators can change the care patients receive, and that care can then change the outcomes the calculator was built to predict. This paper uses computer simulations, based on cardiovascular disease prediction and treatment, to test what happens when such a model is updated with data from patients it helped treat. Without hidden factors affecting both treatment and outcome, leaving treatment out of the model made it miscalibrated, while including treatment fixed this fully. When hidden confounders were present, performance got worse even with treatment included.
- **Why it matters**: Prediction tools that are retrained on their own outcomes can quietly lose accuracy after deployment, which matters for patient safety. The authors suggest causal inference methods and post-deployment monitoring as possible responses, though the text does not test these.
- **Background needed**: - Clinical prediction model: a formula that estimates a patient's chance of an outcome (e.g., a heart attack) from measured factors.
- Calibration: whether predicted risks match observed event rates; calibration-in-the-large checks overall average level, calibration slope checks whether predictions spread too widely or narrowly.
- C-statistic: a measure of how well a model ranks patients from higher to lower risk.
- Treatment threshold: the risk level above which treatment is recommended.
- Feedback loop: when a model's decisions change the data it is later updated on.
- Unmeasured confounding: a hidden factor that influences both who gets treated and the outcome, biasing results.
- Simulation study: generating artificial data with known rules to test a method under controlled conditions. · level: research-level

<details><summary>Original abstract</summary>

Clinical prediction models (CPMs) that guide treatment-initiation, and therefore affect patient outcomes, may create feedback loops when updated using data from patients whose care they influenced. Treatment can alter predictor-outcome relationships and outcome prevalence, potentially reducing model performance. This simulation study aims to quantify this effect using setting parameters based on cardiovascular disease prediction and intervention and assess if including a treatment variable in the model mitigates any performance degradation. In the simulation, models were developed to predict the probability of a binary adverse outcome, guide treatment allocation, and then updated using data containing patients in whom the model was applied. Scenarios varied treatment inclusion as a predictor in the model and the presence of unmeasured confounding. Performance was assessed with calibration-in-the-large, calibration slope, c-statistic, and correct risk assignment relative to treatment threshold. Without unmeasured confounding, excluding treatment as a predictor resulted in miscalibration, but including treatment solves this problem completely. With unmeasured confounding, performance deteriorated even when treatment was included. These results agree with previous findings and illustrate the likelihood that models that guide interventions may experience performance deterioration due to the difficulty of recording treatment and avoiding unmeasured confounders. Causal inference methods combined with risk prediction may help address this problem. Further research is needed on monitoring techniques to allow detection of this issue post-model implementation.

</details>

### [STREAM: Sequential Transformer for Risk Estimation from Asynchronous Medical Events for Dynamic Postoperative AKI Prediction](https://www.medrxiv.org/content/10.64898/2026.11.21.26368665v1)
*Lu, S.; Ruan, X.; Wang, L. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.21.26368665 v1 · relevance 0.11

- **In one sentence**: STREAM is a Transformer model that treats irregular electronic health record data as a chronological stream of clinical events to predict postoperative acute kidney injury (PO-AKI) at surgery completion and after each new event, reporting AUROC/AUPRC and macro-AUPRC comparisons against a Time-series Transformer and GRU-D in a retrospective cohort of 167,078 noncardiac surgical episodes.
- **In plain words**: Doctors want to know how likely a patient is to develop kidney injury after surgery, and that estimate should change as new test results and notes arrive. This paper describes a model, STREAM, that reads a patient's health records as a time-ordered list of events and updates its risk estimate each time a new event appears. In a retrospective set of about 167,000 non-heart surgeries, it scored somewhat higher than two comparison models on the measures reported.
- **Why it matters**: Risk estimates that update as information arrives could matter for timing kidney-protecting care after surgery, and the paper suggests the model could be one part of a future perioperative "digital twin" (a computer model of a patient). The reported gains over the comparators are modest, the study is retrospective, and the text does not show that it improves patient outcomes, so its clinical value remains unproven.
- **Background needed**: - Acute kidney injury (AKI): a sudden drop in kidney function, a common complication after surgery.
- Electronic health record (EHR): the hospital's digital chart, with labs, medications, vitals and notes recorded at irregular times.
- Transformer: a neural network architecture that weighs relationships among items in a sequence; widely used in language models.
- GRU-D: a recurrent neural network designed for data with gaps and irregular timing; used here as a comparison.
- AUROC / AUPRC: scores from 0 to 1 for how well a model separates patients who will and will not have the outcome; AUPRC is especially informative when the outcome is rare.
- Calibration: whether predicted probabilities match observed event rates.
- Retrospective cohort: a study using past records rather than a new prospective trial.
- Permutation analysis: shuffling the order of inputs to test whether the order affects the prediction.
- Digital twin: a continuously updated computer model of an individual patient. · level: research-level

<details><summary>Original abstract</summary>

Postoperative acute kidney injury (PO-AKI) risk estimates evolve as clinical information accumulates, yet many electronic health record (EHR) models use static or fixed-window representations. We developed STREAM, a perioperative event-stream Transformer that represents irregular EHR data as chronological clinical events and supports surgery-index prediction at surgery completion and event-by-event postoperative AKI prediction. In a retrospective cohort of 167,078 noncardiac surgical episodes, STREAM achieved surgery-index AUROC/AUPRC of 0.942/0.771, the Time-series Transformer 0.933/0.729, and GRU-D 0.926/0.695. Postoperative macro-AUPRC across 6-hour evaluation intervals was 0.589, 0.525, and 0.547, respectively. STREAM showed more consistent calibration across postoperative time points than the comparators. Event-arrival attribution and within-window permutation analysis enabled event-level interpretation of how newly arrived information and fine-grained event ordering shaped evolving risk estimates. These findings support event-stream modeling as an interpretable framework for dynamic, temporally resolved prediction from longitudinal EHR data as well as a potential risk-estimation component for future perioperative digital twins.

</details>

## Econometrics and applied economics

### [Training decision models for simulating human respondents](https://arxiv.org/abs/2611.31613)
*Davood Wadi, Yu Ma* · `cs.CL` · arXiv:2611.31613v1 · relevance 0.05

- **In one sentence**: The paper tests whether fine-tuning language-model "decision models" on historical respondent-level choice data, before any target-study data is seen, reduces bias when LLMs are used as synthetic survey respondents in econometric analysis.
- **In plain words**: Researchers are starting to use AI language models in place of real people in surveys and experiments, but answers from ready-made models tend to distort the conclusions drawn from them. This paper trains a model on past records of how real people chose between options, then tests it on four new studies covering topics like vaccines and nutrition labels. The training reduced the error in estimated treatment effects by 22% to 89%, and a small trained model beat a much larger untrained one on three of the four studies.
- **Why it matters**: Using simulated respondents could make research cheaper and faster, but only if the simulated answers lead to correct conclusions. The paper's finding that training on a single study can lower prediction error while making treatment-effect estimates worse is a useful caution, and the authors present choice training as complementary to calibration rather than a full fix.
- **Background needed**: - Synthetic respondent (silicon sampling): using an AI model to generate survey or experiment answers in place of human participants.
- Discrete choice experiment: a study where people pick one option from a set, used to learn how much they value features such as price or labels.
- Treatment effect: the measured difference an intervention makes, such as how much a label changes choices.
- Conditional maximum likelihood: a statistical method that adjusts model settings so the observed choices become as probable as possible.
- Cross-entropy: a measure of how well a model's predicted probabilities match actual outcomes; lower is better.
- Post-inference calibration: correcting estimates after the model has produced them.
- Held-out studies: datasets kept back from training and used only for testing. · level: research-level

<details><summary>Original abstract</summary>

Researchers increasingly use large language models (LLMs) as synthetic respondents in market research, conjoint analysis, and randomized experiments. However, synthetic choice data from off-the-shelf generative LLMs bias downstream econometric inference. Neither proprietary models nor higher reasoning effort reliably reduces this bias. We investigate decision models (System One architectures) for silicon sampling. Using choice training, we update KEV model weights on historical respondent-level choice microdata by conditional maximum likelihood, before inference and without target-study data. Across three model scales, training on two discrete choice experiments lowers treatment-effect error by 22% to 89% on four held-out studies from new domains (vaccines, nutrition labels, consumer rights, and AI) and new response formats. A small choice-trained model outperforms a much larger off-the-shelf model on three of the four studies. Although training on single studies lowers cross-entropy, it can exacerbate treatment-effect error. Choice training thus complements post-inference calibration by providing a stronger starting point for estimating human preferences.

</details>

### [Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement](https://arxiv.org/abs/2611.33050)
*Zihan Chen, Di Zhu, Lei Nico Zheng* · `cs.CL` · arXiv:2611.33050v1 · relevance 0.03

- **In one sentence**: Using a French government chatbot arena, WildChat logs, and random assignment of streamed versus cached replies, this paper tests how response speed and streaming affect blind preference votes on LLM answers and whether users keep chatting.
- **In plain words**: AI chatbots now reply at very different speeds: some think for a long time, while others return a saved answer instantly. This paper asks whether that delivery speed changes how people rate the answers, and whether waiting changes whether they keep chatting. The authors found that, in a French government chatbot arena, the same stored text won more votes when it was streamed word by word than when it was replayed at once, and that slow replies made users less likely to ask follow-up questions.
- **Why it matters**: Preference leaderboards that rank chatbots are usually read as judgments of text alone, so a delivery effect would matter for how models are compared and how services budget speed and caching. The link to the broader literature on the "labor illusion" (people value effort they can see) is suggested by the authors, but how far the findings generalise beyond these settings is not established by the text provided.
- **Background needed**: - Large language model (LLM): the AI system that generates text for chatbots.
- Blind preference vote: a user compares two anonymous answers and picks the better one; these votes build model rankings.
- Streaming: showing text as it is generated, rather than all at once.
- Caching: storing and reusing an earlier answer instead of generating a new one.
- Labor illusion: the tendency to value outputs more when the effort behind them is visible.
- Percentage points: the difference between two percentages (e.g., 57% vs 29% is 28 points).
- Congestion: slowdowns caused by heavy server load.
- WildChat: a public dataset of real conversations with ChatGPT. · level: intermediate

<details><summary>Original abstract</summary>

Answers from generative AI chatbots built on large language models (LLMs) now arrive at very different speeds: reasoning models deliberate before replying, while response caches can return a stored answer at once. Blind preference votes, which rank these models, are read as judgments of their text, and if delivery matters, faster answers are expected to gain. Research on the labor illusion and on how text appears on screen suggests instead that an answer which unfolds as it is written is credited over the same answer shown at once. We test these accounts with three sources of variation in natural use. First, compar:IA, a French government chatbot arena, answered repeated prompts, by a random draw, either with a fresh answer streamed as it was written or with a stored earlier answer from the same model, shown at once. Within the same prompt, a replay lowered an answer's chance of winning a decisive blind vote by 25.8 percentage points. The same stored text won 57% of its decisive votes when streamed and 29% when replayed, and voters called it less complete, more superficial and more often incorrect when replayed. Second, provider congestion slowed streamed answers. In 324,029 conversations, slower answers earned no detectable net credit in the vote, but a slower first exchange made visitors less likely to ask a follow-up question. Third, in 4,378,514 WildChat replies from everyday ChatGPT use, replies slowed by congestion made users less likely to continue. Delivery moved blind votes, in the direction opposite to the one the arena's designers expected, while waiting cost follow-up questions that a comparison between two answers cannot register when both are slow. The results bear on how AI services cache and stream answers, how they budget latency, and how preference leaderboards evaluate models.

</details>

## Economic theory

### [Contests versus Contracts in Innovation Procurement](https://arxiv.org/abs/2611.31829)
*Xiaoyun Qiu, Christopher Snyder* · `econ.TH` · arXiv:2611.31829v1 · relevance 0.08

- **In one sentence**: A mechanism-design study comparing independent contracts, contests, and "interdependent" contracts for a funder who pays several competing approaches to an uncertain innovation, where feasibility is learned through experimentation.
- **In plain words**: This paper looks at how a government or other buyer should pay several teams that are all trying to develop the same new technology, when it is not known in advance which approaches will work. The authors compare three designs: paying each team separately, running a prize contest, and a newer hybrid where each team's payment and whether it keeps experimenting depend on what its rivals achieve. They find that the best hybrid designs can match the optimum, and that the cheaper option between contests and contracts depends on how long the experimentation period lasts.
- **Why it matters**: Public funders such as defence and science agencies often split money across competing projects, so the question of how much rivalry to build into the payment scheme has practical weight. The text is a theory paper with no empirical data, so its results apply to modelled conditions rather than to any specific programme.
- **Background needed**: - Innovation procurement: a buyer pays firms to develop a new technology rather than buying an existing product.
- Contract vs. contest: a contract pays each firm under its own terms; a contest pays only the winner(s) of a race to a goal, such as a fixed prize.
- Mechanism design: the study of how to set up rules and payments so that self-interested participants behave in the way the designer wants.
- Breakthrough vs. breakdown: a breakthrough is a success; a breakdown is a clear failure that signals an approach is infeasible. "Contractable" means the buyer can write payments conditional on it being observed and verified.
- Experimentation: firms try approaches over time, learning whether each one works; the buyer can stop experiments at a cutoff or deadline.
- Rent extraction: the buyer reduces the extra profit firms would otherwise keep above their costs. · level: research-level

<details><summary>Original abstract</summary>

How much competition should a designer introduce when procuring innovation? We study a designer funding multiple technological approaches whose feasibility is learned through experimentation. Between independent contracts and contests, we introduce interdependent contracts, which combine approach-specific rewards with continuation decisions that depend on rivals' outcomes. When both breakthroughs and breakdowns are contractable, these contracts implement the optimum by extracting firms' rents and coordinating experimentation across approaches. When only breakthroughs are contractable, we compare simple mechanisms with constant contractual payments. Under technological symmetry, optimal interdependent contracts terminate experimentation at a success cutoff or deadline. Fixed-prize contests can implement the same innovation outcomes, but their relative expenditure depends on the experimentation horizon: for interior success cutoffs, contests are more expensive when the horizon is short and less expensive when it is sufficiently long. Rank-contingent contests can weakly outperform constant-payment interdependent contracts, but technological heterogeneity can reverse this ranking because individualized contracts better tailor incentives to different approaches. We further characterize optimal interdependent contracts with time-varying payments, extending the comparison beyond simple mechanisms. Our results show how outcome contractability, technological heterogeneity, and payment flexibility shape the desirable form of competition in innovation procurement.

</details>

### [What it is to Obey](https://arxiv.org/abs/2611.32741)
*Mark Whitmeyer* · `econ.TH` · arXiv:2611.32741v1 · relevance 0.06

- **In one sentence**: In simultaneous-move games, a designer who commits in advance to a signaling device and evaluates the resulting equilibria with a Hausdorff-continuous function is shown to be without loss in restricting to direct obedient devices under incomplete information exactly when she assumes her preferred equilibrium will be played, and the monotone evaluations are characterized under complete information.
- **In plain words**: The paper studies a setting where a planner sets up a private messaging scheme before players make simultaneous choices, sending each player a signal that may recommend what to do. The planner judges the set of resulting equilibrium outcomes with a continuous scoring rule. The text reports conditions under which it is safe to limit attention to "obedient" schemes, where players are told what to do and find it in their interest to follow, and it classifies which scoring rules behave in a consistent (monotone) way in games where everyone knows the payoffs.
- **Why it matters**: This is a theory result about how much a designer can gain from recommendations, and whether simple obedient recommendations lose nothing. It connects to the literature on Bayesian persuasion and correlated equilibrium, and its relevance beyond those models is not established by the text.
- **Background needed**: - Simultaneous-move game: players choose at the same time, without seeing each other's choices.
- Equilibrium: a set of strategies where no player gains by switching alone.
- Signaling device / recommendation: a private message to each player suggesting an action; "obedient" means following it is optimal for the player.
- Designer's evaluation: a scoring function over the set of equilibria; "Hausdorff-continuous" means small changes in the equilibrium set cause small changes in the score.
- Incomplete vs. complete information: whether players know each other's payoffs.
- Monotone evaluation: a scoring rule that does not fall when the set of equilibria grows, roughly; the optimistic and pessimistic extremes are the best and worst case over equilibria. · level: research-level

<details><summary>Original abstract</summary>

Prior to agents taking part in a simultaneous-move game, a designer commits a device that sends signals to each of the agents, evaluating the resulting set of equilibria according to a (Hausdorff-)continuous function. In games of incomplete information I show that it must be without loss of optimality for the designer to restrict attention to direct obedient devices if and only if she assumes her preferred equilibrium will be played. In games of complete information, I characterize the monotone evaluations, which include both the maximally optimistic one and the maximally pessimistic one.

</details>

## Game theory and algorithmic economics

### [Optimal Signaling Mechanisms for One-round Matching Markets](https://arxiv.org/abs/2611.31517)
*Varsha Dani, David G. Harris, Thomas P. Hayes et al.* · `cs.GT` · arXiv:2611.31517v1 · relevance 0.19

- **In one sentence**: The paper derives optimal deterministic and randomized signaling mechanisms for a one-round matching market with n applicants and n firms, where each applicant signals k firms, and gives limiting efficiency values as k grows.
- **In plain words**: The paper studies how job seekers can send signals of interest to employers so that matches happen more often, a setting like job or dating markets where many people compete for limited slots. The authors work out the best possible signaling rules for a simple model with equal numbers of applicants and firms, including rules that use randomness. They report that as the number of signals per applicant grows large, about 75.45% of applicants get offers under the best deterministic rule and about 78.2% under the best randomized rule.
- **Why it matters**: It gives precise limits on how much signaling can improve matching in a stylized model, and it shows that randomization can beat the best deterministic rule. The text does not say how these results transfer to real job or dating markets, so the practical reach is unclear.
- **Background needed**: - Matching market: a setting where applicants and firms pair up, such as jobs or dating.
- Signaling: a costly or limited way for applicants to show real interest in a firm, so firms can prioritize.
- Deterministic vs randomized mechanism: a fixed rule versus a rule that uses chance to decide which signals or outcomes occur.
- Limit as k goes to infinity: the result when each applicant may send an ever-larger number of signals.
- Incentive compatibility: whether firms gain by following the prescribed rule rather than deviating.
- Optimal here means best achievable within the model's assumptions, not best in practice. · level: research-level

<details><summary>Original abstract</summary>

Signaling mechanisms are used in various types of matching markets so that applicants may credibly signal interest in firms. They have been observed to improve outcomes in job markets and dating markets, and proven to improve outcomes in several stylized theoretical models. In this paper we develop optimal signaling mechanisms for a simple one-round matching market consisting of $n$ applicants and $n$ firms. We consider a much richer space of signals than have been used previously, in theory or practice, and also consider randomized signaling mechanisms, which have not been systematically studied. For each $k \geq 1$, we determine the optimal deterministic and randomized signaling mechanisms in which applicants signal $k$ firms. In the limit as $k\to \infty$, our deterministic mechanism guarantees that in expectation, $\approx 75.4504\%$ of the applicants receive job offers, and this is optimal. Likewise, for $k \to \infty$, our randomized mechanism guarantees that $\approx 78.197\%$ of the applicants receive offers, which is also optimal. The optimal $k$-signal randomized mechanism is non-constructive, and has a rather complex description. We describe some simple randomized signaling mechanisms whose efficiency surpasses that of the limiting optimal deterministic mechanism. Finally, we also discuss incentive-compatibility for the firms to follow the mechanism.

</details>

### [Heterogeneous Risk-Sensitive Evolutionary Learning in Coordination Games: Polarization, Welfare Loss, and Intervention for Efficiency](https://arxiv.org/abs/2611.31568)
*Solaleh Mohammadi, Yiman Fong, Kaiqing Zhang* · `eess.SY` · arXiv:2611.31568v1 · relevance 0.09

- **In one sentence**: In a finite population playing coordination games under risk-sensitive best-response learning with mutations, two subpopulations with different fixed entropic-risk attitudes can settle into a polarized, Pareto-dominated state, and interventions that shift risk parameters for a share of agents can restore the payoff-dominant equilibrium only when both intervention share and intensity are large enough.
- **In plain words**: The paper studies how a group of players who learn by trial and adjustment ends up when they play a game where everyone does best by matching choices, and when the players differ in how cautious they are about risk. The authors find that a split outcome, where the two groups pick different actions, can be the long-run result and that it leads to lower average payoffs than the best available agreement. They also test ways to nudge some players toward less cautious attitudes, and find that both how many players are nudged and how strongly must be large enough to bring the best outcome back.
- **Why it matters**: It offers a formal account of how differences in risk attitudes alone, without any change in the game, can make a group's learning settle on a worse outcome, which may bear on coordination problems in markets, social norms, or policy. The text does not show how well the model matches real populations, so its practical reach is unclear from this summary alone.
- **Background needed**: - Coordination game: each player gains when they pick the same action as others; several agreements can exist.
- Payoff-dominant equilibrium: the agreement where everyone gets the highest payoff.
- Risk-dominant equilibrium: the agreement that is safest to aim for when unsure what others will do.
- Pareto dominance: one outcome is better for everyone than another.
- Entropic risk measure: a way to score gambles that penalizes bad outcomes more heavily, with a parameter setting how cautious a player is.
- Stochastic stability: the state a learning process tends to spend most of its time in when rare random mutations occur.
- Best response with mutations: players usually pick the best reply to recent play, but sometimes experiment at random.
- Polarized state: a stable split in which the two subpopulations choose different actions. · level: research-level

<details><summary>Original abstract</summary>

We study evolutionary learning in coordination games in a finite population of agents with heterogeneous risk attitudes, modeled using the entropic risk measure (ERM). The population consists of two subpopulations, each with a fixed risk attitude. Under risk-sensitive best response with mutations (BRM), we characterize the long-run outcomes of the learning process. In particular, we characterize when a polarized state, in which the two subpopulations choose different actions, is uniquely stochastically stable in terms of agents' risk attitudes and the subpopulation sizes. Notably, this polarized state is strictly Pareto dominated by the payoff-dominant equilibrium under both expected payoffs and agents' own ERM-adjusted payoffs. Moreover, its welfare, measured by average expected payoff, is always lower than that of the payoff-dominant equilibrium and can also be lower than that of the risk-dominant equilibrium. Thus, heterogeneity of risk attitudes in learning alone can lead to an inefficient long-run outcome. To mitigate such inefficiency, we propose intervention mechanisms to modify agents' risk attitudes in learning. We show that a sufficiently large intervention share (the fraction of agents modified) and sufficiently high intervention intensity (the increase in their risk parameter) ensure that the payoff-dominant equilibrium is uniquely stochastically stable. However, greater intervention intensity cannot compensate for an insufficient intervention share, and a larger intervention share cannot compensate for insufficient intervention intensity.

</details>

## Mathematical finance

### [Rough log-normal stochastic volatility with quadratic drift: second-moment stability and the martingale property under positive correlation](https://arxiv.org/abs/2611.32791)
*Artur Sepp, Parviz Rakhmonov* · `q-fin.MF` · arXiv:2611.32791v1 · relevance 0.14

- **In one sentence**: The paper extends a log-normal stochastic volatility model with quadratic drift to a rough (fractional Volterra) setting and studies second-moment stability, expected integrated variance, and when the discounted price is a true martingale under positive correlation.
- **In plain words**: The paper studies a mathematical model of how the randomly changing "volatility" (the size of price swings) of an asset such as Bitcoin or Ether evolves over time. It shows the model has a unique non-negative solution with finite moments on any finite time horizon, and gives exact conditions under which its second moment stays bounded. It also checks the model against option prices for those assets and against exact moment formulas in simulations.
- **Why it matters**: Rough volatility models are an active area in quantitative finance, and results on when a model's moments stay bounded and when prices are true martingales matter for pricing and risk checks. The abstract reports these results for the paper's own model; its practical use beyond that setting is not established in the text.
- **Background needed**: - Volatility: how strongly an asset's price moves; here modeled as a random process that must stay non-negative.
- Stochastic volatility model: a model where volatility itself follows a random process rather than being fixed.
- Log-normal: volatility is modeled as the exponential of a Gaussian-type process, which keeps it positive.
- Rough / fractional Volterra equation: a model where volatility is driven by a noise with memory, with roughness set by the Hurst exponent.
- Moments: averages of powers of a random quantity; "second moment" relates to average squared size.
- Martingale: a process whose expected future value equals its current value, i.e. no predictable drift in a fair game.
- Share measure: a change of pricing viewpoint (numeraire) used in finance.
- VIX: a published index of expected market volatility derived from option prices.
- Implied volatility smile: how option-implied volatility varies with strike price. · level: research-level

<details><summary>Original abstract</summary>

We extend the log-normal stochastic volatility model with quadratic drift to a fractional Volterra equation. The volatility has a unique global non-negative solution with finite moments on every finite horizon. With linear drift we derive the conditional first and second moments, expected integrated variance and conditional squared VIX. We give the exact threshold for a uniformly bounded second moment and the exponential growth rate above it. With positive quadratic damping the second moment is uniformly bounded for every admissible Hurst exponent and volatility of volatility. A separate bound on long-run expected integrated variance per unit time depends only on the drift parameters. Under the share measure the volatility beta offsets the quadratic damping. The price is a true martingale when damping covers beta. For a positive finite exponential mixture this condition is also necessary. The converse for a singular fractional kernel remains open. We illustrate calibration under positive correlation on observed Bitcoin and Ether option smiles and benchmark the simulation against exact moments. A marked order-flow construction relates multiplicative volatility noise to signed trade impacts arriving at a rate proportional to variance. A small state-dependent bias generates the quadratic drift. We establish a stopped diffusion limit for the constant kernel.

</details>

### [Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality](https://arxiv.org/abs/2611.32790)
*Michele Colombi, Marco Di Francesco, Pietro Rossi* · `q-fin.CP` · arXiv:2611.32790v1 · relevance 0.10

- **In one sentence**: The paper trains a PPO deep reinforcement learning agent to delta-vega hedge option portfolios under discrete trading and transaction costs, using the underlying asset and a longer-dated option, with validation in a stochastic volatility simulator and on historical S&P 500 index option data.
- **In plain words**: Options sellers need to protect their books from price moves and from swings in how volatile the market is expected to be. This paper asks whether a learning algorithm can decide how much of the underlying asset and a second, longer-dated option to trade to do that job, while keeping trading costs in mind. The authors train it on simulated markets, then test it on real S&P 500 option data and compare it with standard textbook hedging rules.
- **Why it matters**: Hedging volatility risk is costly, and the paper reports that the learned policy beats a standard delta-vega rule as trading costs rise and cuts profit-and-loss spread roughly in half versus a simple delta hedge on historical data. It may matter for derivatives desks and for work applying reinforcement learning to finance, though the text gives no evidence about live trading performance beyond the backtest-style comparison.
- **Background needed**: - Option: a contract giving the right to buy or sell an asset at a set price later; its value depends on price and volatility.
- Hedging: taking offsetting positions so that losses in one holding are cancelled by gains in another.
- Delta: sensitivity of an option's value to the underlying price; delta hedging means holding the matching amount of the asset.
- Vega: sensitivity of an option's value to volatility; delta-vega hedging also uses a second option to offset volatility risk.
- Stochastic volatility model: a model in which volatility itself moves randomly over time.
- Reinforcement learning: training an agent to choose actions by trial and reward; PPO (Proximal Policy Optimization) is a common algorithm for this.
- Transaction costs: fees and price impact paid on each trade, which discourage frequent rebalancing.
- Profit-and-loss (P&L) dispersion: how widely the hedged portfolio's gains and losses vary; lower is steadier. · level: research-level

<details><summary>Original abstract</summary>

Hedging an option portfolio with the underlying asset alone leaves the position exposed to changes in volatility, which can be managed by trading another derivative, at higher transaction costs. We propose a deep reinforcement learning approach to hedge both price and volatility risk under discrete-time trading and transaction costs, by trading the underlying asset and a second, longer-dated option. We train the agent with Proximal Policy Optimization (PPO) on synthetic data from a stochastic volatility model, and restrict its state to quantities observable in the market, so that the policy learned in simulation applies directly to market data. In simulation, we validate the policy against semi-analytical Delta and Delta-Vega hedging benchmarks. PPO matches Delta-Vega's objective at baseline transaction costs and increasingly outperforms it as costs rise, with both two-instrument strategies consistently outperforming the single-instrument Delta hedge. On historical S&P 500 index option data, we benchmark our approach against practitioner Black-Scholes Delta and Delta-Vega hedging strategies. The two-instrument strategies roughly halve the profit-and-loss dispersion of the Delta hedge, and PPO attains a lower profit-and-loss volatility than Delta-Vega at comparable transaction costs. PPO holds more of the hedging option than Delta-Vega, in line with the stochastic-volatility model hedge, and its advantage is concentrated in high-volatility episodes.

</details>

## Financial markets

### [Semivariance and Semivolatility in Portfolio Selection: A Unified Framework for Downside-Risk Portfolio Models](https://arxiv.org/abs/2611.32638)
*Francesco Cesarone, Massimiliano Corradini, Nicol\`o Giunta* · `q-fin.PM` · arXiv:2611.32638v1 · relevance 0.07

- **In one sentence**: The paper classifies downside-risk portfolio models (semivariance and semivolatility) by the positive homogeneity degree of the risk measure, states a non-degeneracy condition under which risk-parity, most-diversified and Sortino-ratio problems are well posed, and tests seventeen long-only strategies out of sample on Dow Jones and Nasdaq-100 constituents.</one_liner>
<parameter name="plain">This paper looks at how to build investment portfolios that focus on the bad side of returns, meaning losses below a chosen threshold, rather than all ups and downs. The authors argue that these downside-risk measures should not simply copy the standard variance-based versions, because different portfolio problems need different mathematical properties. They then compare seventeen portfolio strategies on real stock index data, rebuilding them over time and checking whether differences in performance are statistically meaningful.
- **Why it matters**: Many investors and fund managers judge risk by losses rather than by overall variability, so a clearer framework for when downside measures behave well matters for how portfolios are built. The text does not show how widely these methods are used in practice, and its empirical results are only described in general terms here.
- **Background needed**: - Portfolio selection: choosing the share of money put into each asset (the "weights").
- Variance and volatility: standard measures of how much returns spread out; volatility is the square root of variance.
- Downside risk: only counts returns falling below a threshold, such as the mean return, zero, or a market index return.
- Semivariance and semivolatility: downside versions of variance and volatility.
- Positive homogeneity: if all weights are doubled, the risk doubles (degree one), which keeps risk contributions adding up to total risk.
- Risk parity, most-diversified and risk budgeting: strategies that spread risk across holdings in set proportions.
- Sortino ratio: a reward-to-risk measure using downside risk instead of total volatility.
- Convex program: an optimization problem with a single best solution that standard solvers can find reliably.
- Out-of-sample backtest and block bootstrap: testing a strategy on data not used to design it, and using resampled blocks of time series to judge statistical significance. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study downside risk in portfolio selection beyond minimum-risk models, where semivariance and its square root, semivolatility, yield the same portfolio. Downside-risk models are often presented as direct extensions of their variance-based counterparts, although different classes of portfolio problems require different properties of the risk measure. We classify these models by the degree of positive homogeneity of the risk measure in the weights: degree one makes risk contributions add up to the portfolio risk and keeps diversification and reward-to-risk ratios scale invariant. For three thresholds, the portfolio mean, zero and a market-index return, we state a non-degeneracy condition on long-only downside risk under which the risk-parity, most-diversified and Sortino-ratio problems are well posed. Under this condition, the two ratio problems reduce to convex programs, and the differentiability of semivolatility ensures that the risk-budgeting formulation attains the prescribed budgets. We also characterize when below-mean semivolatility is additive. Finally, we provide an out-of-sample analysis on two real-world datasets of total returns, the current constituents of the Dow Jones and Nasdaq-100 indexes. We compare seventeen long-only strategies, covering the minimum-risk, reward-to-risk, risk-parity and most-diversified families, in a rolling-window backtest, and test the differences within each family by block-bootstrap inference.

</details>

### [Large-Scale Streaming Portfolio Optimization with Pauli Correlation Encoding](https://arxiv.org/abs/2611.32769)
*Vicente P. Soloviev, Josh Kirsopp* · `quant-ph` · arXiv:2611.32769v1 · relevance 0.06

- **In one sentence**: This paper tests Pauli Correlation Encoding (PCE), a qubit-efficient quantum-style heuristic for clustering-based portfolio selection, in a rolling streaming setup against a Buy & Hold baseline, and compares a joint multi-cut variant (dPCE) on portfolios of up to several thousand assets.
- **In plain words**: Choosing which stocks to hold from a very large list is a hard combinatorial puzzle, and existing shortcut methods handle it poorly at scale. This paper takes an earlier static test of a quantum-inspired method (PCE) and runs it as a live system that keeps re-estimating correlations and rebalancing over time. The authors report that both PCE and a joint variant beat a simple buy-and-hold strategy, and that PCE lost noticeably less during a market downturn, while the joint variant becomes more costly as portfolios grow.
- **Why it matters**: It matters for anyone asking whether specialized quantum-style optimization can be used in realistic, repeated trading decisions rather than one-off tests. The text does not show how results hold outside the study's own data and settings, so its practical value should be treated as provisional.
- **Background needed**: - Portfolio optimization: choosing which assets to hold and in what amounts to balance return against risk.
- Combinatorial selection: picking a best subset from a huge number of possibilities, which becomes very hard as the list grows.
- Correlation structure: how assets move together; clustering groups similar assets to shrink the problem.
- Qubit: the basic unit of a quantum computer; PCE uses far fewer qubits than one per asset.
- Rolling re-estimation / rebalancing: periodically recomputing correlations and adjusting holdings using recent data.
- Buy & Hold: a passive baseline that buys assets and keeps them without trading.
- Shots: repeated measurements of a quantum circuit; the shot budget is how many are used.
- Transaction costs and risk aversion: trading fees and how strongly the strategy penalizes volatility. · level: research-level

<details><summary>Original abstract</summary>

Classical portfolio construction over large asset universes is a combinatorial selection problem that existing heuristics do not solve well at scale. Pauli Correlation Encoding (PCE) addresses this by representing the underlying clustering problem with far fewer qubits than one per asset, and a prior study showed it is competitive with classical methods on a single historical snapshot. This paper moves beyond that static test to a streaming deployment, in which the correlation structure and the portfolio are both re-estimated on a rolling basis, as a live rebalancing system would actually operate. We introduce two streaming variants -- PCE itself and a joint multi-cut variant, dPCE -- and evaluate both against a Buy & Hold baseline across window lengths, portfolio sizes up to several thousand assets, risk-aversion and transaction-cost settings, and measurement-shot budgets. Streaming PCE and dPCE consistently outperform the passive baseline, including during a market downturn where both lose money but PCE loses markedly less -- evidence that the method's value is not confined to rising markets. PCE also proves the more practical choice at scale, since dPCE's resource requirements and its sensitivity to rebalancing frequency both grow faster with portfolio size. We further report which operational choices -- rebalancing cadence, shot budget, and transaction-cost awareness -- matter most for a real deployment, and which matter less than commonly assumed.

</details>

## Signal processing

### [Score-Based Diffusion for Hypergraph Signals in the t-Spectral Domain](https://arxiv.org/abs/2611.33026)
*Zhiyuan Dong, Carlos Mundo-Levano, Daniel L. Lau et al.* · `cs.LG` · arXiv:2611.33026v1 · relevance 0.09

- **In one sentence**: A score-based diffusion generative model for signals living on a fixed hypergraph, built in the spectral domain of t-product hypergraph signal processing, using a per-mode frequency shift to make the forward diffusion well-posed and a closed-form score for inactive modes.
- **In plain words**: The paper studies how to generate new data values that live on the nodes of a hypergraph, a network where one connection can link more than two items at once. The authors build a diffusion-style generator that adds noise in a frequency-like representation of the network, learns how to reverse that noise, and then uses the same machinery to fill in missing nodes. They report that it beats a clique-expansion baseline (a method that turns the hypergraph into an ordinary graph) on networks of up to 500 nodes.
- **Why it matters**: Many real systems, such as group interactions or multi-way relations, are better described by hypergraphs than by ordinary graphs, so generative tools for signals on them could matter for data imputation and simulation. The text reports specific gains on its own benchmarks, but it does not show how the approach performs on real-world datasets or against stronger recent methods, so its wider significance is unclear.
- **Background needed**: - Signal on a graph: a value attached to each node, such as a sensor reading or user attribute.
- Hypergraph: a generalization of a graph in which an edge can join any number of nodes.
- Graph/hypergraph Laplacian: a matrix describing how connected nodes differ; its eigenvectors act like frequencies for the network.
- Tensor product (t-product): a way of multiplying multi-dimensional arrays that the paper uses to define its spectral domain.
- Diffusion model: a generator that learns to reverse a gradual noising process; the "score" is the gradient of the log probability that guides this reversal.
- Ornstein-Uhlenbeck process: a noising process that drifts back toward a fixed average while adding random noise, with a known stationary distribution.
- Posterior sampling / guidance: generating samples consistent with partial observations, here used to recover missing nodes.
- NMSE (normalized mean squared error): a scale-free measure of reconstruction error, where lower is better. · level: research-level

<details><summary>Original abstract</summary>

We introduce the first score-based generative model for signals on a fixed hypergraph, formulated in the spectral domain of t-product hypergraph signal processing (t-HGSP). The naive tensor heat semigroup is ill-posed, since after palindromic symmetrization the spectral slices of the Laplacian tensor are no longer positive semidefinite. A per-mode frequency shift repairs it, yielding a forward Ornstein-Uhlenbeck diffusion that decouples per (eigenmode, slice) pair with closed-form marginals, exact score targets, and an exactly isotropic stationary law. A lightweight slice-conditioned denoiser is trained on the resulting real spectral grid. Sampling combines its score on data-active modes with the closed-form score elsewhere, which proves essential for stability at scale. A closed cosine-form observation operator turns missing-node recovery into linear-Gaussian guidance with stabilized posterior sampling. On hypergraphs of up to 500 nodes, our model beats a clique-expansion baseline by margins growing from $2\times$ to $27\times$ in covariance error, matches the graph-spectral statistics of the data better than the graph-basis model itself, and reaches the finite-sample estimation floor on data rotated off the t-spectral axes. Posterior sampling reduces missing-node NMSE to 0.28-0.64 (classical baselines 0.87-1.1) at conservative coverage, and cuts the framework's own denoising baseline by up to $3.6\times$.

</details>

### [Multiple-Input Multiple-Output Forward Scatter Radar](https://arxiv.org/abs/2611.32546)
*Abdollah Ajorloo, Stefano Amato Ciciretti, Fabiola Colone* · `eess.SP` · arXiv:2611.32546v1 · relevance 0.09

- **In one sentence**: This paper proposes a multiple-input multiple-output forward scatter radar that estimates a target's departure and arrival angles from amplitude-only, non-coherent measurements, using frequency- or time-division multiplexing, and validates it with simulations and outdoor software-defined radio experiments.
- **In plain words**: Forward scatter radar detects objects that are hard to see by catching the strong signal they reflect when they pass directly between a transmitter and a receiver. This paper extends that idea by using arrays of antennas at both ends, so the system can estimate the target's position in two angular directions without needing the signals to be phase-synchronized. The authors describe two ways to separate the signals, simulate their performance, and report outdoor proof-of-concept tests.
- **Why it matters**: It offers a way to locate targets with simpler, unsynchronized hardware, which may matter for low-cost or integrated sensing and communications systems. The text reports simulations and outdoor tests, but these are described only at a proof-of-concept level, so its practical reach is not yet established.
- **Background needed**: - Radar: sends radio waves and measures echoes to detect and locate objects.
- Radar cross section: how strongly an object reflects radio waves.
- Forward scatter: detection when a target sits on the straight line between transmitter and receiver, where reflection is unusually strong.
- Transmitter-receiver baseline: the line between the two units.
- Direction of departure (DoD) and direction of arrival (DoA): the angles at which the signal leaves the transmitter and reaches the receiver.
- Coherent vs. non-coherent: coherent systems use the signal's phase; non-coherent systems use only its strength (amplitude).
- Antenna array and MIMO: several antennas at each end, transmitting and receiving multiple signals.
- Multiplexing (FDM/TDM): sharing the channel by assigning different frequencies or time slots to each signal.
- Software-defined radio: radio hardware whose behaviour is set by software. · level: research-level

<details><summary>Original abstract</summary>

Forward Scatter Radar (FSR) enhances the detection of low-observable targets by exploiting the increased radar cross section that occurs when a target crosses the transmitter-receiver baseline. Conventional FSR typically uses single-input single-output (SISO) architectures with limited localization capability, while recent single-input multiple-output (SIMO) systems enable non-coherent angular estimation. This paper introduces a multiple-input multiple-output FSR (MIMO-FSR) framework for joint estimation of target direction of departure (DoD) and direction of arrival (DoA) from non-coherent, amplitude-only measurements. By exploiting antenna arrays at both the transmitter (TX) and receiver (RX), the proposed approach enables two-dimensional angular localization without phase synchronization among TX/RX array elements. We establish the underlying operating principle under ideal signal separability and then develop practical frequency-division multiplexing (FDM) and time-division multiplexing (TDM) implementations. For each scheme, dedicated signal models and processing methods compensate for distortions caused by frequency offsets and target motion, respectively. We also derive analytical expressions for angular resolution, ambiguity conditions, and output-map distortions. Extensive numerical simulations for short- and long-baseline scenarios reveal operational limits and trade-offs between the two multiplexing schemes. Finally, proof-of-concept outdoor experiments using software-defined radio platforms validate the proposed framework. The results demonstrate joint DoD-DoA estimation and support the feasibility of MIMO-FSR for future active, passive, and integrated sensing and communications applications.

</details>

## Audio and speech

### [Cif-query bridging for audio-native asr transfer to visual speech recognition](https://arxiv.org/abs/2611.32697)
*Chang Sun, Dongliang Xie, Wanpeng Xie et al.* · `cs.SD` · arXiv:2611.32697v1 · relevance 0.16

- **In one sentence**: A lightweight cross-attention bridge, seeded by a CIF predictor's adaptive token-rate queries, connects a Paraformer visual speech recognition encoder to the Qwen3-ASR audio-native decoder, reporting 7.97% CER versus 11.78% for native Paraformer on CMLR.
- **In plain words**: Lip-reading systems turn video of a talking face into text. This paper takes a speech recognizer built for sound and reuses its language knowledge to read lips, by adding a small connecting module between a visual front end and the pretrained sound-based model. On the CMLR test set, the authors report that this setup makes fewer character errors than the original visual system (7.97% versus 11.78%).
- **Why it matters**: Reusing a large pretrained speech model for silent video could help lip-reading where visual data is scarce, and the bridge is designed to keep detail from many video frames without making the model read them all directly. The text reports only one dataset and a comparison against one baseline, so the size of the gain in other settings is unknown.
- **Background needed**: - Visual speech recognition (VSR): transcribing speech from silent video of lips and face.
- ASR (automatic speech recognition): software that turns audio into text.
- Character error rate (CER): share of characters wrongly transcribed; lower is better.
- Continuous integrate-and-fire (CIF): a method that groups frame-level features into a variable number of token-sized chunks.
- Cross-attention: a mechanism that lets one sequence of vectors look up relevant information in another.
- Adapter/projector: small trainable layers that map one model's output format into another's input format.
- CTC: a training objective for aligning sequences of frames with text without explicit alignment.
- CMLR: a Chinese lip-reading dataset used as the benchmark here. · level: research-level

<details><summary>Original abstract</summary>

Audio-native automatic speech recognition (ASR) models provide strong speech-language priors, but their compact acoustic interfaces are mismatched with long, frame-level visual features. We propose CIF-Query Bridge, a lightweight connection from a Paraformer visual speech recognition (VSR) encoder to Qwen3-ASR. The existing visual continuous integrate-and-fire (CIF) predictor produces an input-dependent number of token-rate queries; a two-layer cross-attention bridge refines them against the complete frame sequence, and a linear adapter feeds the pretrained ASR projector and decoder. This design preserves access to uncompressed visual context while avoiding direct autoregressive processing of hundreds of video frames. On CMLR, the complete visual-only transfer system achieves 7.97% character error rate, compared with 11.78% for native Paraformer under the same test split and scoring protocol---a 3.81-point absolute and 32.3% relative reduction. Controlled ablations characterize bridge depth, projector initialization, adapter capacity, and CTC supervision. The results show that CIF-derived adaptive queries provide a compact interface for transferring audio-native ASR capability to VSR.

</details>

### [SoundWeaver: Compositional Warm-Starting for Text-to-Audio Diffusion Serving](https://arxiv.org/abs/2603.07865)
*Ayush Barik, Sofia Stoica, Nikhil Sarda et al.* · `cs.SD` · arXiv:2603.07865v2 · relevance 0.07

- **In one sentence**: SoundWeaver is a training-free method that speeds up text-to-audio diffusion by warm-starting generation from acoustic segments reused across a cache of previously generated clips, with an adaptive bandit choosing the skip depth per request.
- **In plain words**: Generating sound from a text description with modern diffusion models is slow, because the model must refine noise step by step through many passes. This paper proposes SoundWeaver, which reuses pieces of sound from a small library of already-generated clips, stitches them into a rough starting point that fits the prompt, and then begins the refinement partway through instead of from pure static. The authors report speedups of 1.48 to 3.74 times on several text-to-audio backbones, using a cache of only 1,000 clips, and say generation quality also improved.
- **Why it matters**: Faster audio generation without retraining matters for anyone deploying these models at scale, where latency and compute cost add up. The idea of reusing structure across past outputs, rather than treating each request in isolation, may also be relevant to caching and serving systems more broadly, though the text does not address that connection.
- **Background needed**: - Diffusion models generate output by starting from random noise and removing it over many steps (neural function evaluations, or NFEs, are these model passes).
- Warm-starting means beginning the process from a partly formed guess instead of pure noise, so fewer steps are needed.
- Neural audio codecs compress audio into compact numerical representations that can be compared.
- A contextual bandit is an online decision method that picks among options (here, how many steps to skip) and learns from feedback.
- Signal-to-noise ratio (SNR) describes how much signal remains relative to noise at a given step.
- The paper's error bound is a theoretical guarantee on how far the warm start can be skipped before quality suffers. · level: research-level

<details><summary>Original abstract</summary>

Text-to-audio (T2A) diffusion models generate high-quality audio but require tens of neural function evaluations (NFEs), resulting in substantial inference latency. Existing acceleration methods primarily optimize each generation trajectory independently, even when reusable acoustic structure exists in prior examples. We introduce SoundWeaver, the first training-free framework for compositional cross example acoustic reuse. Rather than generating from pure noise, SoundWeaver constructs a prompt-conditioned acoustic prior from segments distributed across cached audios and warm-starts diffusion from an intermediate noise level. We introduce an Acoustic Composition Graph (ACG), which uses neural codec representations and segment-level identification to identify candidate cross-cache transitions and structured path search to jointly optimize prompt relevance and acoustic continuity. We further establish a warm-start error bound showing how prior quality and diffusion SNR jointly govern the admissible skip depth, motivating an adaptive contextual-bandit Skip Gater that selects the warm-start level for each request. Across T2A diffusion backbones, SoundWeaver achieves 1.48-3.74x generation speedup with only a 1K-clip cache while improving generation quality.

</details>

## Control systems

### [Automated Design and Evaluation Pipeline for Optimal Control Transcriptions in Model Predictive Control](https://arxiv.org/abs/2611.32558)
*Fabio Schneider, Peter K\"otting, Renato Loureiro* · `eess.SY` · arXiv:2611.32558v1 · relevance 0.18

- **In one sentence**: An automated pipeline uses Bayesian Optimization to pick the best pseudospectral Legendre-Gauss-Radau transcription and mesh configuration for a given Model Predictive Control formulation, minimizing user-defined metrics such as computation time or closed-loop performance, and is demonstrated on spacecraft on-orbit servicing scenarios.
- **In plain words**: Model Predictive Control is a method where a computer repeatedly plans the best sequence of actions over a short future window and applies the first step, but the planning can be too slow for real-time use. This paper describes an automated tool that searches for the most efficient way to set up that planning problem, judged by criteria the user chooses such as speed or control quality. The authors test it on spacecraft tasks, such as moving satellites for servicing in orbit, and report that it improves MPC performance in those scenarios.
- **Why it matters**: Computational cost is a stated bottleneck for deploying MPC in real-time systems, so a tool that automates the search for faster problem setups could help engineers in robotics, aerospace and process control. The text does not give quantitative results, so the size of the improvement and how well it generalizes beyond the presented scenarios are not clear from this summary.
- **Background needed**: - Model Predictive Control (MPC): repeatedly solving a short-horizon optimal planning problem and acting on the first step.
- Optimal control transcription: converting a continuous-time planning problem into a finite set of equations a solver can handle.
- Pseudospectral / Legendre-Gauss-Radau method: a transcription that places sample points at special positions in time to represent the trajectory accurately with few points.
- Forward Euler and implicit collocation: simple and more accurate ways of approximating how a system changes over time; the paper says its one formulation covers both.
- Mesh configuration: how the time interval is divided into segments and points.
- Bayesian Optimization: a method for tuning settings by testing promising options and learning from past results, useful when each test is expensive.
- On-orbit servicing: robotic or autonomous maintenance of spacecraft in orbit, such as repair, refueling or repositioning. · level: research-level

<details><summary>Original abstract</summary>

The computational burden of Model Predictive Control represents a bottleneck limiting its widespread deployment in real-time applications. The selection of the optimal control transcription strategy for a given MPC formulation is a key driver of computational efficiency. Identifying performant MPC transcriptions requires significant effort and domain knowledge. We propose an automated pipeline for the design and evaluation of performant optimal control transcriptions for a given MPC formulation. Custom multi-objective design metrics, such as computation time or closed-loop performance, can be specified and are minimized by the pipeline. As a transcription method, a pseudospectral Legendre-Gauss-Radau method is employed. We show that it incorporates forward Euler integration and implicit collocation methods of low and high order in one formulation, leveraging the pipeline to evaluate both numerical approaches. Furthermore, different mesh configurations can be parameterized. To identify the optimal configuration of the transcription, a Bayesian Optimization framework is applied. The pipelines improvements in MPC performance are demonstrated through On-Orbit Servicing scenarios involving spacecraft motion planning and closed-loop control.

</details>

### [From Safety-Driven Redundancy to Value-Driven Architecture: An ODD-Based Rationalization Framework for Level 4 Autonomous Vehicles](https://arxiv.org/abs/2611.32960)
*Tiago Sim\~ao Ferreira (Federal Institute of Minas Gerais - IFMG), Farzad Fallahi (University of Luxembourg)* · `eess.SY` · arXiv:2611.32960v1 · relevance 0.13

- **In one sentence**: A safety-constrained, ODD-based systems-engineering framework that screens and ranks architecture transformations (removal, relocation, reassignment, consolidation) for a generic synthetic Level 4 autonomous vehicle, using lifecycle-cost sensitivity and robust multiobjective Pareto analysis.
- **In plain words**: Self-driving cars need backup systems so they can keep driving safely when sensors, computers, power, or steering parts fail, but those backups add cost and complexity. This paper proposes a method for trimming or rearranging that hardware only where the car would still be safe in its intended driving conditions. The authors tested it on a made-up, generic vehicle design rather than a real one, and found that simply removing parts had little room to help, while moving and combining functions produced more safe options, with the best option cutting normalized lifecycle cost by 5.55%.
- **Why it matters**: Cost and validation effort are real obstacles to scaling up autonomous vehicles, so a principled way to check whether redundancy can be reduced without losing safety may be useful to engineers. The results rest on illustrative, synthetic assumptions and are explicitly described as design candidates, not validated production architectures, so their practical weight is limited until tested on real systems.
- **Background needed**: - Level 4 autonomous vehicle: a car that drives itself fully within defined conditions, without a human backup.
- Operational Design Domain (ODD): the set of road, weather, and traffic conditions a system is designed to handle.
- Fault-tolerant architecture: a system design that keeps working when some parts fail, usually through redundancy.
- Non-compensatory constraint: a safety requirement that cannot be traded off against cost savings; a design failing it is rejected regardless of other benefits.
- Pareto analysis: a way of finding options that cannot be improved in one goal (e.g., cost) without worsening another (e.g., risk); "non-dominated" means on that frontier.
- Ablation: testing a design by removing components one at a time to see the effect. · level: research-level

<details><summary>Original abstract</summary>

Level 4 autonomous vehicles require fault-tolerant architectures that preserve critical driving functions under sensing, computing, communication, power, and actuation failures. As these systems progress toward industrial scalability, architectural complexity, validation burden, integration effort, and lifecycle cost become increasingly relevant. This study proposes an Operational Design Domain (ODD)-based, safety-constrained systems-engineering framework for architecture rationalization. ODD-specific capabilities, physical fault assumptions, post-fault operational policies, and spatial sensing requirements are propagated through an integrated safety-feasibility gate. Architecture transformations, including removal, relocation, functional reassignment, and consolidation, are evaluated only within the resulting safety-feasible design space, followed by lifecycle-cost sensitivity and robust multiobjective Pareto analysis. A generic, synthetically parameterized Level 4 architecture is used as a demonstrative computational case study. Within this modeled design space, direct ablation showed limited rationalization potential, whereas directional redistribution and functional consolidation generated a broader set of safety-feasible candidates. Under the illustrative lifecycle-cost model, the best nominal candidate achieved a 5.55% normalized cost reduction and remained cost-reducing across all 5,000 sampled points in the prescribed uncertainty domain. The analysis identified 15 non-dominated architecture-policy solutions representing seven physical transformations. The results support capability-based, policy-conditioned, and lifecycle-aware architecture rationalization under the stated assumptions, with safety retained as a non-compensatory feasibility constraint. The reported transformations are design candidates rather than validated production architectures.

</details>

## Fetch statistics

| Topic | Fetched | New | Selected |
|---|---|---|---|
| Probability | 49 | 49 | 2 |
| Differential geometry | 24 | 24 | 2 |
| Partial differential equations | 59 | 59 | 2 |
| Harmonic analysis | 43 | 43 | 2 |
| Complex analysis | 13 | 13 | 2 |
| Operator algebras and spectral theory | 18 | 18 | 2 |
| Algebra | 33 | 33 | 2 |
| Representation theory | 24 | 24 | 2 |
| Number theory | 48 | 48 | 2 |
| Algebraic geometry | 31 | 31 | 2 |
| Topology | 24 | 24 | 2 |
| Dynamical systems | 14 | 14 | 2 |
| Combinatorics | 70 | 70 | 2 |
| Numerical analysis | 34 | 34 | 2 |
| Logic and foundations | 10 | 10 | 2 |
| Mathematical physics | 49 | 49 | 2 |
| Optimization and control | 49 | 49 | 2 |
| Statistics theory | 14 | 14 | 2 |
| Statistical methods and applications | 48 | 48 | 2 |
| AI industry news | 40 | 32 | 5 |
| Model architectures and training | 88 | 88 | 2 |
| Machine learning theory | 10 | 10 | 2 |
| Large language models | 74 | 74 | 2 |
| Computer vision | 264 | 264 | 2 |
| Reinforcement learning | 47 | 47 | 2 |
| AI safety and alignment | 38 | 38 | 2 |
| Interpretability | 10 | 10 | 2 |
| AI for mathematics | 13 | 13 | 2 |
| Robotics and embodied AI | 111 | 111 | 2 |
| Security and cryptography | 64 | 64 | 2 |
| Algorithms and complexity | 33 | 33 | 2 |
| Programming languages and formal methods | 33 | 33 | 2 |
| Systems and networking | 52 | 52 | 2 |
| Human-computer interaction | 20 | 20 | 2 |
| Information theory | 26 | 26 | 2 |
| High-energy theory and gravity | 92 | 92 | 2 |
| Statistical physics | 36 | 36 | 2 |
| Condensed matter | 60 | 60 | 2 |
| Particle physics | 61 | 61 | 2 |
| Nuclear physics | 16 | 16 | 2 |
| Quantum information and computing | 100 | 100 | 2 |
| Optics and atomic physics | 36 | 36 | 2 |
| Fluids and plasma | 31 | 31 | 2 |
| Biological physics | 9 | 9 | 2 |
| Climate, atmosphere and Earth | 5 | 5 | 2 |
| Cosmology | 24 | 24 | 2 |
| Galaxies | 25 | 25 | 2 |
| Exoplanets and planetary science | 21 | 21 | 2 |
| High-energy astrophysics | 19 | 19 | 2 |
| Stars and the Sun | 24 | 24 | 2 |
| Chemical physics | 14 | 14 | 2 |
| Materials science | 47 | 47 | 2 |
| Soft matter and polymers | 19 | 19 | 2 |
| AI for chemistry and materials | 15 | 15 | 2 |
| Biochemistry | 21 | 18 | 2 |
| Pharmacology and drug discovery | 8 | 7 | 0 |
| Computational and systems biology | 132 | 127 | 2 |
| Neuroscience | 87 | 82 | 2 |
| Genetics and genomics | 49 | 46 | 2 |
| Cell and molecular biology | 60 | 58 | 2 |
| Immunology and microbiology | 76 | 70 | 2 |
| Cancer biology | 32 | 28 | 2 |
| Ecology and evolution | 61 | 58 | 2 |
| Plant biology | 27 | 23 | 2 |
| Bioengineering and synthetic biology | 28 | 25 | 2 |
| Mathematical biology (arXiv) | 12 | 12 | 2 |
| Epidemiology | 22 | 21 | 2 |
| Infectious diseases | 8 | 7 | 2 |
| Public and global health | 24 | 20 | 2 |
| Psychiatry and neurology | 33 | 30 | 2 |
| Oncology | 9 | 6 | 2 |
| Health informatics and medical AI | 18 | 14 | 2 |
| Econometrics and applied economics | 8 | 8 | 2 |
| Economic theory | 4 | 4 | 2 |
| Game theory and algorithmic economics | 13 | 13 | 2 |
| Mathematical finance | 5 | 5 | 2 |
| Financial markets | 9 | 9 | 2 |
| Signal processing | 31 | 31 | 2 |
| Audio and speech | 12 | 12 | 2 |
| Control systems | 31 | 31 | 2 |

<!-- {% endraw %} -->
