# Research digest · 2026-11-25
<!-- {% raw %} -->

New papers posted from about 2026-11-24 to 2026-11-25 (UTC).

> Papers are picked by how closely their wording matches each topic's description (the "relevance" score), not by quality. Summaries are written by AI from the abstract only; open the paper before relying on them.

## Highlights

- **[The majority game chromatic number for dense random graphs](https://arxiv.org/abs/2611.32746)** (Combinatorics): The paper studies a two-player game on random networks: players take turns colouring the vertices of a graph so that no two neighbours share a colour, and the question is how many colours are needed. For random graphs that are fairly dense (each pair of vertices is joined with a fixed probability above two-thirds), the authors show that three colours are enough with high probability, meaning the chance of this failing goes to zero as the graph grows.
- **[Tuning evolutionary information in MSAs shapes protein generation and folding](https://www.biorxiv.org/content/10.64898/2026.11.23.768656v1)** (Computational and systems biology): Researchers who use computer models to design or predict protein shapes feed them a collection of related protein sequences from many species. This study asks whether deliberately choosing which sequences go into that collection, rather than treating the collection as fixed, changes what the models generate and how confidently they predict structures. The authors report that the coherence of the chosen sequences tracked both structure-prediction confidence and how novel the generated sequences were, with the strongest effects near a particular information level.
- **[Implementation of Machine Translation for the Uzbek Language Based on Transformer Models](https://arxiv.org/abs/2611.32359)** (Large language models): This paper is about building an automatic translator between Uzbek, a language with relatively little digital text, and English. The authors gathered and cleaned up sentence pairs in both languages, expanded the collection, and then adjusted two existing AI language models to do the translation. They report that the result beats older translation approaches, measured by a standard scoring method.

## Probability

### [Sharp estimates for incremental moments of inverse subordinators and approximation errors for time-changed stochastic differential equations](https://arxiv.org/abs/2611.33075)
*Ivan Bio\v{c}i\'c, Sixian Jin, Kei Kobayashi* · `math.PR` · arXiv:2611.33075v1 · relevance 0.23

- **In one sentence**: The paper proves sharp upper and lower bounds on the incremental moments of inverse subordinators and uses them to derive an error bound, shown to be optimal in general, for numerically approximating stochastic differential equations time-changed by an inverse subordinator.
- **In plain words**: The paper studies a random "clock" that runs slow and jumpy, used to model processes that move more slowly than usual, such as diffusion through a crowded medium. It establishes precise limits on how much this random clock can change over a short stretch of time. These limits are then used to bound the error when computers approximate such time-changed random processes on a fixed grid of time steps.
- **Why it matters**: Numerical methods for these time-changed models need reliable error guarantees, and the paper gives one and shows the resulting convergence rate cannot be improved in general. The text does not say which specific applications it targets beyond subdiffusion modelling, so the broader impact is unclear from this abstract alone.
- **Background needed**: - Stochastic differential equation: a equation describing a quantity that evolves with random noise, such as a jittery price or particle path.
- Subordinator: a random process that only moves forward in time, built from random jumps; it can act as a random clock.
- Inverse subordinator: the "inverse" of such a clock, which counts how far real time has advanced relative to the random clock; it has flat stretches and is used to model subdiffusion, i.e. slowed-down random motion.
- Time change: substituting a random clock for ordinary time in a process.
- Incremental moments: averages of powers of how much a random quantity changes over a time interval, used to measure size of fluctuations.
- Order of convergence: how quickly the approximation error shrinks as the time step gets smaller.
- Deterministic time grid: approximation computed at fixed, evenly or predefined time points. · level: research-level

<details><summary>Original abstract</summary>

This paper establishes precise upper and lower bounds for the incremental moments of general inverse subordinators. Such processes are used as random time changes to model subdiffusive phenomena. The upper and lower bounds provide the foundation for a general framework for analyzing numerical approximation of time-changed stochastic differential equations on deterministic time grids. We derive an upper bound for the approximation error and further prove that the resulting order of convergence cannot be improved in general.

</details>

### [Temporal Inhomogeneous Random Graphs](https://arxiv.org/abs/2611.32717)
*Sofiya Burova, Francisco Calvillo* · `math.PR` · arXiv:2611.32717v1 · relevance 0.21

- **In one sentence**: Extends results on temporal stochastic block models to graphon-based random graphs with a continuous, strictly positive kernel, studying increasing-path reachability and path-length asymptotics in the sparse regime of connection probabilities of order log n / n with uniformly random edge timestamps.
- **In plain words**: This paper studies random networks where each pair of nodes is linked with a chance that depends on their positions in a population, and every link gets a random time stamp. It asks how far one can travel from a starting point if each step must use links with strictly later time stamps. The authors find the first-order (leading-order, large-network) size of the set of nodes reachable this way from a fixed node, and the leading-order lengths of the longest and shortest such time-respecting routes.</plain>
<parameter name="why">Time-respecting routes matter for modeling how things spread through contact networks, where order of contacts changes what can reach whom. The text only motivates this via time-dependent propagation in inhomogeneous populations; it does not show specific applications, so the practical reach is unclear from the abstract alone.</why>
<parameter name="background">- Random graph: a network whose links are created by chance; here n is the number of nodes.
- Graphon: a continuous function describing how likely two "types" of nodes are to connect; it generalizes block models where nodes fall into groups.
- Stochastic block model: a random network with a few groups, with link chances depending on group membership.
- Increasing path: a route through the network whose link time stamps strictly increase at each step.
- Log n / n scaling: connection chances sparse enough that each node has on the order of log n links, a regime near where the network becomes connected.
- First-order asymptotics: the leading term describing how a quantity grows as n becomes large.</background>
<parameter name="difficulty">research-level

<details><summary>Original abstract</summary>

Motivated by the study of time-dependent propagation processes in inhomogeneous populations, we extend Burova, Lugosi and Perarnau's results on the temporal stochastic block model to graphon-based random graphs with a continuous and strictly positive kernel. We consider such a graph in the regime where connection probabilities are of the order of $\log n/n$, and equip its edges with a uniformly random ordering, interpreted as timestamps. We study the size of reachable sets via increasing paths (that is, paths whose edge timestamps are strictly increasing). We establish tight first-order asymptotics for the size of the reachable set from a fixed vertex, and also determine the first-order asymptotics of the lengths of the longest and shortest increasing paths with one or two fixed endpoints.

</details>

## Differential geometry

### [Rotationally symmetric fractional minimal surfaces](https://arxiv.org/abs/2611.32252)
*Chiara Gambicchia, Matteo Novaga, Matteo Talluri* · `math.DG` · arXiv:2611.32252v1 · relevance 0.20

- **In one sentence**: The paper constructs a rotationally symmetric s-minimal surface, built from alternating radial sets bounded by concentric spheres, in which the fractional mean curvature H_s vanishes at every free interface, and shows that a rescaled limit gives a properly embedded locally finite hypersurface with H_s = 0 on its boundary.
- **In plain words**: The paper studies a generalized version of a soap-film-like surface, where the usual curvature rule is replaced by a "fractional" rule that depends on the whole shape rather than only on nearby points. The authors build an example of such a surface that has rotational symmetry, made of alternating shells bounded by concentric spheres. They then rescale these shapes and take a limit, obtaining a rotationally symmetric surface that satisfies the fractional rule at every point of its boundary.
- **Why it matters**: Explicit non-trivial examples are rare for fractional minimal surfaces, so a concrete rotationally symmetric case gives the theory something to test against. The text does not say what wider applications it may have, so its broader significance is uncertain.
- **Background needed**: - Minimal surface: a surface whose mean curvature is zero, like a soap film spanning a wire frame.
- Mean curvature: a local measure of how a surface bends on average.
- Fractional (s-) version: replaces the local curvature with a nonlocal quantity, weighted by a parameter s between 0 and 1, so distant parts of the surface influence each point.
- Radial set / concentric spheres: regions whose boundaries are nested spheres centered at one point, which makes the problem reduce to one radial variable.
- Rotational symmetry: the shape looks the same when turned around an axis or center.
- Locally finite hypersurface: a surface that, in every bounded region, is made of finitely many pieces.
- Rescaling and limit: shrinking or enlarging a configuration so its innermost radius becomes fixed, then studying what shape the sequence approaches. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we provide a non-trivial example of an $s$-minimal surface that is invariant under rotations. More precisely, we study alternating radial sets whose boundaries are finite or locally finite unions of concentric spheres and prove that, fixing the outer radius to $r=1$, there exists a radial configuration for which the fractional mean curvature $H_s$ vanishes at every free interface. We then show that rescaling radial maximizers by their innermost radius and passing to the limit yields a properly embedded, rotationally symmetric, locally finite hypersurface satisfying $H_s=0$ at every point of the boundary.

</details>

### [An intrinsic criterion for Pansu differentials to be homomorphisms of nilpotent Lie groups](https://arxiv.org/abs/2611.32893)
*Cristian Sopio, Francesca Tripaldi* · `math.DG` · arXiv:2611.32893v1 · relevance 0.19

- **In one sentence**: The paper gives an intrinsic criterion, for a suitable grading, for when the Pansu differential of a Lipschitz map from a nilpotent Lie group with bracket-generating distribution is a group homomorphism, and shows the threshold on target step is sharp.
- **In plain words**: The paper studies how "smooth-like" maps behave between curved, non-Euclidean spaces built from groups of motions. For a class of such spaces, the best local linear approximation of a map may fail to respect the group structure. The authors identify a condition, phrased using only the space itself, that decides when it does, and show with an example that a size threshold in that condition cannot be loosened.
- **Why it matters**: Pansu differentiation is a central tool for understanding maps between sub-Riemannian and metric spaces, so a clean test for when the approximation is a true homomorphism is useful to specialists. The text does not claim wider applications, and I am not certain how far the criterion extends beyond the setting described.
- **Background needed**: - Lie group: a continuous group of transformations, such as rotations and translations, with smooth structure.
- Nilpotent group: a group whose repeated commutators eventually vanish, making it "almost abelian" in layers.
- Carnot group: a nilpotent group with a graded structure, the model spaces for Pansu's theorem.
- Bracket-generating distribution: a family of allowed directions of motion whose commutators span the whole tangent space, so any two points can be connected by paths along those directions.
- Pansu differential: a limiting linear-like approximation of a Lipschitz map (a map with bounded stretching) at almost every point, which is a group homomorphism when the target is Carnot.
- Grading and step: a decomposition of the Lie algebra into layers; the step is the number of layers needed.
- Homomorphism: a map that preserves the group operation. · level: research-level

<details><summary>Original abstract</summary>

By Pansu's theorem, Lipschitz maps between Carnot groups are differentiable almost everywhere, and their differentials are group homomorphisms. When the domain is instead a nilpotent Lie group with a bracket-generating left-invariant distribution, the Pansu differential is a homomorphism of an osculating Carnot group, which depends on an auxiliary choice of grading, and it need not be a homomorphism of the original group. We give an intrinsic criterion for when it is one, for a suitable choice of grading: the differential must vanish on an ideal that depends only on the group and its distribution, and comes from a universal quotient onto a Carnot group. The criterion holds automatically when the step of the target is small enough, and an explicit example shows that this threshold is sharp. Along the way, we determine exactly how the obstruction depends on the choice of grading.

</details>

## Partial differential equations

### [Weighted pointwise estimates for the damped wave equation and global solutions to Nakao's problem in three dimensions](https://arxiv.org/abs/2611.31881)
*Vladimir Georgiev, Kosuke Kita* · `math.AP` · arXiv:2611.31881v1 · relevance 0.22

- **In one sentence**: The paper proves weighted pointwise estimates for the Duhamel term of the three-dimensional damped wave equation, and uses them to show small-data global existence and uniqueness of mild solutions for Nakao's coupled damped-wave/wave system in weighted L-infinity spaces.
- **In plain words**: This is a mathematical study of two coupled equations that describe how waves and damped (energy-losing) waves spread through space over time in three dimensions. The authors develop new size bounds on a term that captures how the damped system responds to an external push, combining a parabolic-type decay weight with a wave-type decay weight. Using these bounds, they show that if the starting disturbance is small, solutions exist for all time and are unique, under stated conditions on the powers in the nonlinear terms.
- **Why it matters**: The text supports only a technical contribution: sharper pointwise bounds for a damped wave Duhamel term, applied to a specific coupled system. It is a targeted result in the well-studied area of nonlinear wave and damped-wave equations, and the text does not claim wider consequences.
- **Background needed**: - Partial differential equation (PDE): an equation relating a function to its rates of change in space and time; it describes physical processes such as waves and heat flow.
- Wave equation: describes disturbances that travel at a fixed speed, like sound or ripples; in 3D they weaken as they spread out.
- Damped wave equation: a wave equation with a friction-like term that drains energy, so over long times it behaves partly like heat diffusion (parabolic decay).
- Duhamel term: the part of a solution produced by an outside forcing term, accumulated over time.
- Pointwise estimate: a bound on the size of the solution at each location and time, not just on average.
- Weighted L-infinity space: a set of functions whose maximum size, multiplied by a decay weight depending on position and time, is bounded.
- Small-data global existence: if the initial data are small enough, the solution is guaranteed to persist for all time.
- Contraction argument: a fixed-point method that builds the solution by repeatedly applying a map that shrinks distances. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we establish weighted pointwise estimates for the Duhamel term of the three-dimensional damped wave equation. The estimates combine the parabolic weight $\langle t+|x|^2\rangle$ with the wave-cone weight $\langle t-|x|\rangle$, and thereby account for both the diffusive part of the damped wave flow and source terms with wave-like decay. As an application, we study Nakao's problem, a weakly coupled system consisting of one semilinear damped wave equation and one semilinear wave equation. Under explicit conditions on the exponents of nonlinear terms, we prove small-data global existence and uniqueness of mild solutions in weighted $L^\infty$ spaces. The result covers both the full parabolic decay and slower pointwise decay for the damped-wave component, and allows either the standard wave decay or slower pointwise decay for the wave component. The proof combines the new Duhamel estimate with weighted estimates for the free wave equation and a contraction argument.

</details>

### [Large-time existence for the gravity water waves equations](https://arxiv.org/abs/2611.32994)
*Th\'eo Fradin, Benjamin Melinand* · `math.AP` · arXiv:2611.32994v1 · relevance 0.13

- **In one sentence**: The paper proves local-in-time well-posedness for the gravity water-waves equations without surface tension, over a long timescale growing like the inverse of the nonlinearity parameter, uniformly in the shallow-water parameter and allowing a large but non-emerging bathymetry.
- **In plain words**: This paper is about the mathematics of waves on the surface of water, such as waves moving over a seabed. It shows that, for a finite but fairly smooth starting state, the equations that describe these waves have a solution that persists for a fairly long time. The authors say the time span grows as the wave-size parameter gets smaller, and that the result holds even when the seabed is deep in a varying way, though not so deep that it breaks through the surface.
- **Why it matters**: Knowing how long water-wave models stay valid is central to coastal and ocean modelling, so a guaranteed time span is a useful mathematical result. The text does not discuss applications or numerical comparisons, so its practical reach beyond the mathematics is unclear.
- **Background needed**: - Water-waves equations: the standard model of a free water surface over a fluid that is incompressible (volume-preserving) and irrotational (no swirling).
- Gravity versus surface tension: here only gravity acts to restore the surface; surface tension is dropped.
- Well-posedness: a solution exists, is unique, and depends continuously on its starting data.
- Sobolev regularity: a measure of how smooth the solution is; "high but finite" means many derivatives are controlled but not infinitely many.
- Non-linearity parameter: a size measure of wave amplitude relative to depth; small values mean gentle waves.
- Shallow-water parameter: the ratio of depth to wavelength; the result holds uniformly across it.
- Bathymetry: the shape of the seabed.
- Existence on a timescale: the solution is guaranteed only up to a certain time, here one that grows as the nonlinearity shrinks. · level: research-level

<details><summary>Original abstract</summary>

We provide a new well-posedness result on the gravity water-waves equations, i.e. the free-surface, incompressible and irrotational Euler equations, in the absence of surface tension. Our main contribution is to provide the existence of solutions, in high enough but finite Sobolev regularity, on a timescale that grows like the inverse of the non-linearity parameter. Our result is also uniform in the shallow-water parameter. The main difficulty is that we allow for the presence of a large (though not emerging) bathymetry.

</details>

## Harmonic analysis

### [Normal and Unitary Operators on Smooth Banach Spaces via the Duality Mapping](https://arxiv.org/abs/2611.31874)
*Mohammed Shameem, Deepesh K. P* · `math.FA` · arXiv:2611.31874v1 · relevance 0.21

- **In one sentence**: The paper extends the notions of normal and unitary operators, and the spectral properties of normal operators, from Hilbert spaces to smooth Banach spaces by using the duality mapping.
- **In plain words**: Mathematicians have long studied a special class of operators (maps that transform vectors in a space) that behave nicely on Hilbert spaces, which are spaces where lengths and angles work as in ordinary geometry. This paper asks how much of that theory survives in a wider family of spaces called smooth Banach spaces, where a geometric tool called the duality mapping replaces the inner product. The text reports that the authors define normal and unitary operators in this setting, prove several characterisations of them, and find that many classical properties carry over.
- **Why it matters**: The work is a generalisation of a well-known part of functional analysis, so its value lies in showing which classical results depend on the inner product and which do not. The provided text does not say which specific applications, if any, it connects to, so the wider significance is uncertain.
- **Background needed**: - Operator: a rule that maps vectors in a space to vectors in the same or another space.
- Hilbert space: a space with an inner product (a way of measuring angles and lengths), the setting of classical quantum-style operator theory.
- Banach space: a complete space where lengths are measured by a norm but angles need not be defined.
- Smooth Banach space: a Banach space in which the norm has no sharp corners, so each vector has a unique supporting direction.
- Duality mapping: a rule that assigns to each vector a set of matching functionals (linear measuring tools) of the same size, replacing the inner product.
- Normal and unitary operators: classes of operators that commute with their own adjoint and preserve length, respectively, in Hilbert spaces.
- Spectrum: the set of scalars for which an operator minus that scalar fails to be invertible. · level: research-level

<details><summary>Original abstract</summary>

This article extends the classical notions of normal and unitary operators from Hilbert spaces to smooth Banach spaces through the duality mapping. The class of normal operators introduced in this setting contains, as a special case, the self-adjoint operators on smooth Banach spaces defined via the duality mapping. We establish several characterisations of these operators and investigate their fundamental properties. In particular, we examine various spectral properties of normal operators on smooth Banach spaces. These results demonstrate that many fundamental aspects of the classical theory of normal and unitary operators on Hilbert spaces persist in the smooth Banach space setting.

</details>

### [Kernel Estimates and Calder\'{o}n-Zygmund Theory in the $(k,a)$-generalized Laguerre setting](https://arxiv.org/abs/2611.31933)
*Mingwei Shi, Yongsheng Han, Yu Liu* · `math.FA` · arXiv:2611.31933v1 · relevance 0.13

- **In one sentence**: The paper proves heat and Poisson kernel estimates for the operator ||x||^{2-a} Δ_k in the (k,a)-generalized Laguerre setting (Dunkl Laplacian over a finite reflection group), and builds a Calderón–Zygmund singular integral theory on it, including a T1 characterization of L^2 boundedness.
- **In plain words**: This is a piece of pure mathematics about how heat and diffusion spread under a specific, somewhat unusual rule of motion, one that mixes ordinary spatial change with symmetries given by mirror-like reflections. The authors pin down the size and smoothness of the "spreading" kernel that describes this process. From those estimates they develop a general toolkit for a family of averaging operators on this setting and give a test for when such operators behave well on signals.
- **Why it matters**: The text presents this as a systematic extension of classical harmonic analysis tools (Calderón–Zygmund theory and the T1 theorem) to a new, symmetry-twisted setting. The text does not state specific applications, so its wider significance is uncertain from the abstract alone.
- **Background needed**: - Heat kernel: the function describing how heat (or a quantity) spreads from a point over time.
- Poisson kernel: a related smoothing function, here obtained by "subordination" (averaging heat-type behavior over time).
- Dunkl Laplacian: a generalized second-derivative operator that incorporates reflection symmetries of a finite group.
- Laguerre setting: a framework built around Laguerre-type operators, here with an extra power weight parameter a.
- Calderón–Zygmund operators: singular integral operators whose kernels obey size and smoothness conditions, which yield L^p bounds from L^2 bounds.
- L^p spaces, weak type (1,1), BMO (functions of bounded mean oscillation): standard measures of size and of boundedness.
- T1 theorem: a criterion that reduces L^2 boundedness of an operator to checking its action on the constant function 1 (and its adjoint), plus a weak boundedness condition. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we establish heat and Poisson kernel estimates for $\mathfrak L=\|x\|^{2-a}\Delta_k$ in the $(k,a)$-generalized Laguerre setting, where $\Delta_k$ is the Dunkl Laplacian associated with a finite reflection group. The heat kernel is nonnegative, symmetric, and conservative, and satisfies a Gaussian bound in the orbit distance together with polynomial decay in the distance between the transformed coordinates. The Poisson kernel, obtained by subordination, satisfies corresponding size and time-derivative estimates, while $-t\partial_t p_t$ has integral zero in each variable. Motivated by these estimates, we introduce a class of $(k,a)$-Calder\'{o}n-Zygmund singular integral operators and show that $L^2_{k,a}$-boundedness implies $L^p_{k,a}$-boundedness for $1<p<\infty$, together with weak type $(1,1)$ and $L^\infty$-to-$\BMO$ estimates. Finally, we establish a $T1$ theorem characterizing the $L^2$-boundedness of such operators by the conditions $T1\in BMO$, $T^*1\in BMO$, and the weak boundedness property.

</details>

## Complex analysis

### [H\"older continuity of Green functions for Markov sets](https://arxiv.org/abs/2611.33131)
*Leokadia Bialas-Ciez, Rafa{\l} Pierzcha{\l}a* · `math.CV` · arXiv:2611.33131v1 · relevance 0.13

- **In one sentence**: For a compact set K in C^N, the paper shows that the Green function (and so the Siciak extremal function) is Hölder continuous exactly when polynomial derivatives satisfy Markov's inequality on K, settling a long-open implication, with a Hölder exponent of 1/m in one variable from a Markov bound of degree m.
- **In plain words**: The paper studies a measure of how "spread out" a compact set of points is in the complex plane or higher-dimensional complex space, using a function built from polynomials that vanish on the set. It asks when this function varies smoothly in a controlled way (Hölder continuity, a precise limit on how steeply it can change). The authors show this smoothness is equivalent to a bound on how fast polynomial derivatives can grow, and they settle a long-standing open question in one direction.
- **Why it matters**: The result connects two areas, approximation theory and pluripotential theory, by linking a regularity property of an extremal function to a classical inequality about polynomials. Its value to wider work depends on the specialist applications, which the text does not discuss.
- **Background needed**: - Compact set: a closed, bounded collection of points, such as a disk or a curve.
- Polynomial and its derivative: a sum of powers of the variable and the rate at which it changes.
- Markov's inequality: a bound saying a polynomial of degree n cannot have derivatives larger than about A·n^m times its maximum size on the set.
- Green function / Siciak extremal function: a function, built from polynomials bounded on K, that measures how far a point is from K.
- Hölder continuity: a smoothness condition with an exponent; larger exponent means smoother, exponent 1 is Lipschitz.
- Several complex variables: working with several complex numbers at once; Hörmander's theorem concerns extending holomorphic functions from a point. · level: research-level

<details><summary>Original abstract</summary>

Let $K$ be a nonempty compact subset of $\mathbb C^N$. We prove that its Green function (and consequently, the Siciak extremal function) is H\"older continuous if and only if the first derivatives of polynomials satisfy Markov's inequality on $K$. The implication from Markov's inequality to H\"older continuity of the associated Green function settles a longstanding open problem at the intersection of approximation theory and pluripotential theory. A Markov bound $An^m$ in degree $n$ gives every H\"older exponent below $1/m$. In one complex variable it gives the exponent $1/m$ itself. The proof compares the extremal functions of two neighborhoods of $K$. For $N>1$ we use H\"ormander's theorem on holomorphic extension from a point. For $N=1$ the comparison follows from the maximum principle.

</details>

### [Smale's Mean Values And Geometric Mean Values](https://arxiv.org/abs/2611.31546)
*Yunping Jiang, Zhe Wang* · `math.NT` · arXiv:2611.31546v1 · relevance 0.13

- **In one sentence**: The paper shows that the geometric mean value of Smale's mean values can be arbitrarily large for polynomials of each degree above 2, derives upper bounds for it under extra assumptions to support Smale's mean value conjecture on several polynomial subclasses, and links Smale's mean values to Fekete points.
- **In plain words**: The paper studies a quantity that measures how polynomials (formulas like x^3 - 2x + 1) behave near their roots, which is tied to a long-standing conjecture by mathematician Steve Smale. The authors show that one natural version of this quantity, the geometric mean value, can be made larger than any chosen number for polynomials of each degree above 2. That means this quantity alone cannot give the best possible bound on the smaller Smale mean values. They also prove bounds under extra conditions and relate the problem to Fekete points, special arrangements of points that are used in approximation theory.
- **Why it matters**: Smale's mean value conjecture is a well-known open question in complex analysis, so the paper's result that one tool cannot settle it is informative about which approaches are dead ends. The link to Fekete points suggests a new research direction, though the text does not show how far that connection will carry.
- **Background needed**: - Polynomial: a sum of powers of a variable, such as x^3 - 2x + 1; its degree is the highest power.
- Complex numbers and complex analysis: polynomials are studied with complex inputs, where roots and derivatives behave in structured ways.
- Smale's mean value conjecture: a conjecture about how the derivative of a polynomial at a root relates to the polynomial's other roots, bounding the smallest such "mean value" by a constant.
- Geometric mean value: a version of the mean built by multiplying terms and taking a root, as opposed to an ordinary average.
- Fekete points: a set of points chosen to be as spread out as possible in a region, used in approximation and interpolation.
- Upper bound: a number that a quantity is guaranteed not to exceed. · level: research-level

<details><summary>Original abstract</summary>

We prove that, for every integer $d>2$ and every $L>0$, there exists a polynomial of degree $d$ whose geometric mean value exceeds $L$. This result demonstrates that the geometric mean value alone is insufficient to establish the smallest upper bound for the minimum of Smale's mean values. Under certain additional assumptions, we derive upper bounds for the geometric mean value, thereby verifying Smale's mean value conjecture for several subclasses of polynomials. Furthermore, we connect Smale's mean values to Fekete points. Motivated by this connection, we formulate a new problem concerning Fekete points in the spirit of Smale's mean values.

</details>

## Operator algebras and spectral theory

### [The Universal Frame Characterization of C*-algebras](https://arxiv.org/abs/2611.32953)
*Mohammad B. Asadi, Zahra Hassanpour-Yakhdani* · `math.OA` · arXiv:2611.32953v1 · relevance 0.18

- **In one sentence**: The paper proves that a C*-algebra is exactly one of compact operators if and only if every Hilbert A-module admits a frame, settling a question of Amini, Asadi, Elliott and Khosravi (2017) that goes back to Frank and Larson (2002).
- **In plain words**: This paper is about a precise yes-or-no question in the mathematics of operators, which are rules that act on spaces of functions or vectors. The authors ask which algebras of such operators have a particular kind of "frame," a way of spreading a space's contents out so every element can be rebuilt from its pieces. They show that this property holds exactly for the algebras made of compact operators, which answers a question posed in 2017.
- **Why it matters**: The result gives a clean characterization: one structural property of an algebra is equivalent to another, which closes an open question raised by earlier researchers. Its connections to wider areas are not described in the text, so any broader significance is unclear from this abstract alone.
- **Background needed**: - C*-algebra: a collection of bounded linear operators on a Hilbert space that is closed under addition, multiplication, scalar multiples, and taking adjoints (a kind of conjugate transpose), with a norm compatible with these operations.
- Compact operators: operators that behave like finite-dimensional matrices in the limit; they form a basic, well-understood special case of C*-algebras.
- Hilbert module: a generalization of a Hilbert space in which the "scalars" are replaced by elements of a C*-algebra.
- Frame: a spanning family of vectors that allows any element to be reconstructed from its inner products with the family, though the vectors need not be independent.
- The question originates in work by Frank and Larson (2002) and was posed further by Amini, Asadi, Elliott and Khosravi (2017). · level: research-level

<details><summary>Original abstract</summary>

We prove that a C*-algebra A is a C*-algebra of compact operators if and only if every Hilbert A-module admits a frame. This answers affirmatively the question of Amini, Asadi, Elliott and Khosravi (2017), arising from the problem of Frank and Larson (2002)

</details>

### [Algebraic derivations and the first \(L^2\)-cohomology of free group factors](https://arxiv.org/abs/2611.32121)
*J. Huang, K. Kudaybergenov, F. Sukochev et al.* · `math.OA` · arXiv:2611.32121v1 · relevance 0.16

- **In one sentence**: The paper shows that the first L²-Betti number of the free group factor L(F_n) (in the Connes–Shlyakhtenko sense) is infinite, using algebraic derivations built from assignments on the semicircular generators and a rank identity for Jacobians of polynomial relations.
- **In plain words**: This paper studies a measure of "how much room" a certain algebraic structure has, called the first L²-Betti number, for the von Neumann algebra built from a free group with a finite number of generators. The authors show this number is infinite. They do this by showing that values assigned to the basic generators can always be extended to a full algebraic derivation (a rule for how things change under products), and they also show that an outer derivation of this kind forces the number to be infinite in any II₁ factor with separable predual.
- **Why it matters**: Infinite L²-Betti number is a strong structural statement about these algebras, and the paper links derivations to a rank identity for Jacobians, which may connect operator algebra theory to tools from algebraic geometry. The text alone does not show how far the methods reach beyond free group factors, so the wider significance is uncertain.
- **Background needed**: - Von Neumann algebra: a self-adjoint algebra of bounded operators on Hilbert space, the non-commutative analogue of a space of measurable functions.
- Free group factor L(F_n): the von Neumann algebra generated by the free group on n generators; a II₁ factor.
- L²-Betti number (Connes–Shlyakhtenko): a dimension-like invariant measuring the size of the first L²-cohomology of a bimodule-valued derivation problem; infinite means maximally large in this sense.
- Derivation: a linear map satisfying the Leibniz (product) rule; algebraic means defined by polynomial expressions rather than analytic limits; outer means not of the trivial inner form.
- Semicircular elements: the non-commutative analogue of Gaussian random variables, the standard generators of free group factors.
- Jacobian / rank identity: in this setting, the matrix of partial derivatives of polynomial relations and its rank, used to build derivations.
- II₁ factor with separable predual: a type of infinite-dimensional operator algebra with a faithful trace and a countable dense subset of its predual. · level: research-level

<details><summary>Original abstract</summary>

Let \(M\) be the von Neumann algebra of a nonabelian free group of finite rank. We prove that its first \(L^2\)-Betti number in the sense of Connes and Shlyakhtenko is infinite. We show that every assignment of values in \(\Aff(M\bar\otimes M^{\op})\) to the standard semicircular generators extends to an algebraic derivation on all of \(M\). The extension follows from a rank identity for the Jacobians of finite systems of polynomial relations. We also prove that, for any \(\mathrm{II}_1\) factor with separable predual, the existence of an outer derivation with these coefficients forces the first \(L^2\)-Betti number to be infinite.

</details>

## Algebra

### [Gorenstein symmetry can fail for noetherian rings](https://arxiv.org/abs/2611.32871)
*Liran Shaul* · `math.RA` · arXiv:2611.32871v1 · relevance 0.15

- **In one sentence**: The paper constructs a two-sided noetherian ring whose injective dimension is 1 on the left and infinite on the right, showing that Gorenstein symmetry can fail for such rings, and it also studies dualizing complexes and injective generation over a field of characteristic not 2.
- **In plain words**: This is a pure-mathematics paper about algebraic structures called rings, which are sets of numbers or objects that can be added and multiplied. The question is whether a certain measure of how "well-behaved" a ring is comes out the same whether you look at the ring from the left or from the right. The authors build an example where the two sides give very different answers, so the expected symmetry does not hold.
- **Why it matters**: Gorenstein symmetry is a long-standing expected property in ring theory, and the paper shows that it can fail even for rings that are noetherian, a fairly tame and well-studied class. The text does not say what wider applications it has, so its importance beyond this area is unclear.
- **Background needed**: - Ring: a set with addition and multiplication, where multiplication need not commute.
- Left and right modules: ways the ring's elements act on other objects from the left or the right; a ring can behave differently on each side.
- Noetherian ring: a ring in which every chain of ideals eventually stops growing, a common finiteness condition.
- Injective dimension: a number measuring how far a module is from being "injective" (a strong extension property); small is nicer, infinite means it never settles.
- Gorenstein symmetry: the expectation that the left and right injective dimensions of a ring agree when both are finite.
- Dualizing complex and Rickard-Keller injective generation: more technical structures in the derived category used to study these modules. · level: research-level

<details><summary>Original abstract</summary>

We construct a two-sided noetherian ring $A$ which has injective dimension $1$ as a left module over itself and infinite injective dimension as a right module over itself. This shows that Gorenstein symmetry can fail for two-sided noetherian rings. It is further shown that there is such an example over any field of characteristic different than $2$, that it has a dualizing complex, and that its derived category of right modules does not satisfy injective-generation in the sense of Rickard-Keller.

</details>

### [The optimal exponent in the Babai-Goodman-Pyber theorem](https://arxiv.org/abs/2611.32149)
*Shaowu Zheng* · `math.GR` · arXiv:2611.32149v1 · relevance 0.14

- **In one sentence**: The paper determines the optimal exponent c in the Babai-Goodman-Pyber bound [X:Rad(X)] ≤ [X:H]^c for finite groups, showing the least possible c is 1+log_9(168·24^{1/3}) ≈ 3.8141, with a sharper coefficient 24^{-1/3} for nonsoluble groups, and reduces the question to soluble subgroups of automorphism groups of finite simple groups.
- **In plain words**: This is about finite groups, which are collections of symmetries that can be combined, and how large their non-solvable core is compared with a solvable subgroup (a subgroup whose structure is built up in simple layered steps). The paper gives the smallest exponent for which a known size-comparison inequality holds, and it shows the answer is about 3.81. For groups that are not solvable, it also gives a tighter version of the inequality with a specific constant, and it uses examples based on the group PSL_2(8) to show these values cannot be improved.
- **Why it matters**: It settles the exact best constant in a known theorem of Babai, Goodman and Pyber, so the question of how sharp that theorem is now has a definite answer. The text does not say what wider applications it has, so any connection beyond group theory is unclear from the text alone.
- **Background needed**: - Finite group: a set of symmetries (or permutations) with finitely many elements, combined by composition.
- Subgroup: a smaller group sitting inside a larger one; [X:H] is the index, roughly how many copies of H fill X.
- Soluble (solvable) group: one that can be built from abelian (commutative) pieces in successive layers; it is the "simple-ish" end of group structure.
- Normal subgroup: one that is preserved under conjugation (relabeling by group elements); the radical Rad(X) is the largest soluble normal subgroup.
- Finite simple group: a finite group with no nontrivial normal subgroups; these are the building blocks of all finite groups.
- Automorphism group: the group of structure-preserving relabelings of a group.
- Exponent and coefficient: c is the power to which the index is raised; 24^{-1/3} is a multiplicative constant.
- PSL_2(8): a specific finite simple group used as the extremal example. · level: research-level

<details><summary>Original abstract</summary>

Babai, Goodman and Pyber proved that there exists an absolute constant $c$ such that $[X:\operatorname{Rad}(X)]\le [X:H]^c$ for every finite group $X$ and every soluble subgroup $H\le X$, where $\operatorname{Rad}(X)$ denotes the largest soluble normal subgroup of $X$. We prove that the least possible value of $c$ is $b_0=1+\log_9(168\cdot 24^{1/3})\approx3.8141$. For nonsoluble $X$, we obtain the stronger inequality $[X:\operatorname{Rad}(X)]\le 24^{-1/3}[X:H]^{b_0}$, and the coefficient $24^{-1/3}$ is optimal for this exponent. We reduce the problem to bounds on soluble subgroups of automorphism groups of finite simple groups. Examples based on $\operatorname{PSL}_2(8)$ establish sharpness.

</details>

## Representation theory

### [Abelian envelopes and quantum groups in Knop's interpolation categories](https://arxiv.org/abs/2611.33152)
*Johannes Flake, Peter Mader* · `math.CT` · arXiv:2611.33152v1 · relevance 0.25

- **In one sentence**: The paper proves that large classes of subcategories of Knop's tensor envelopes (interpolation categories) admit abelian envelopes, which correspond to quantum groups inside Deligne's interpolation category of symmetric groups, including interpolation categories of group-theoretical easy quantum groups, wreath products, finite general linear groups, and finite affine groups.
- **In plain words**: Mathematicians study symmetry through categories, which are collections of objects and maps between them that behave like sets of symmetries. This paper asks when such a category can be "completed" into a more structured setting where its symmetries behave like groups, and it shows this is possible for many important families. The authors build the needed pieces explicitly, using a calculus of diagrams (relations) that underlies these categories.
- **Why it matters**: The work extends a program that links symmetry groups of many kinds to a single unifying framework, which is of interest to specialists in quantum groups and representation theory. The text itself does not say how far the results reach beyond the listed cases, so the wider impact is uncertain.
- **Background needed**: - Groups and their representations: a group is a set of symmetries with a combining rule; a representation lets it act on vector spaces.
- Tensor categories: collections of objects that can be combined (tensored), with maps between them, used to encode symmetry.
- Interpolation categories: categories in which the number of objects (like the size n of a symmetric group) is treated as a continuous-style parameter, in the sense of Deligne and Knop.
- Abelian envelope: a larger abelian category (one where kernels and cokernels behave like ordinary linear algebra) that contains the original category.
- Quantum groups and Hopf algebras: algebraic generalizations of groups, with coordinate algebras describing their functions.
- Easy quantum groups: a classification of quantum symmetry groups via diagrams of pairings. · level: research-level

<details><summary>Original abstract</summary>

We show the existence of abelian envelopes for large classes of subcategories of Knop's tensor envelopes. It follows that these abelian envelopes correspond to groups or more generally Hopf algebras (``quantum groups'') in their parent interpolation categories. As a special case, we obtain that the interpolation categories in the sense of Flake--Maassen (2022) of all so-called group-theoretical easy quantum groups have abelian envelopes given by quantum groups in Deligne's interpolation category of the symmetric groups. Similarly, we apply our theory to interpolation categories of wreath products, finite general linear groups, and finite affine groups. Our main technique is an explicit construction of objects corresponding to coordinate algebras using the calculus of relations that Knop's categories are based on.

</details>

### [Non-formality of prefactorization algebras](https://arxiv.org/abs/2611.33125)
*Coline Emprin, Alex Takeda* · `math.AT` · arXiv:2611.33125v1 · relevance 0.14

- **In one sentence**: The paper builds a Poisson bracket on the cohomology of locally constant prefactorization algebras on R^m (for m ≥ 2) that obstructs formality, generalizing a two-dimensional bracket of Bruinsma, Schenkel and Vicedo and extending their non-formality result to higher dimensions.
- **In plain words**: This paper is about a mathematical structure that assigns algebra-like data to regions of space, and whether that data can be simplified to a standard form. The authors define a new kind of bracket (a way of multiplying cohomology classes that gives a Poisson structure) that detects when this simplification is impossible, in every dimension at least two. They use it to show that several families of algebras, including factorization envelopes of Lie algebras and certain physical gauge theories, are not formal.
- **Why it matters**: The text presents a general obstruction to formality that works in all dimensions, extending an earlier two-dimensional result. Its wider significance beyond this specialist setting is not discussed in the text, so I cannot say more about its impact.
- **Background needed**: - Prefactorization algebra: a structure assigning algebraic data to open subsets of a space, compatible with placing regions side by side.
- Locally constant: the data depends only on the topology of the regions, not on fine geometry.
- Cohomology: an invariant extracted from a chain complex, measuring the "holes" in the structure.
- Formality: whether an algebraic structure is equivalent to its simplest version (its cohomology with trivial higher operations).
- Non-formality: a structure that cannot be simplified this way; an obstruction is a computable invariant that proves this.
- Poisson bracket: a bilinear operation with derivation and Jacobi-type properties, central to classical and quantum mechanics.
- Lie algebra, L-infinity algebra, BF theory, Chern-Simons theory: standard algebraic and physical structures; only the basic idea is needed.
- Linking spheres: spheres around a point used to define the construction; a geometric tool. · level: research-level

<details><summary>Original abstract</summary>

We construct a Poisson bracket on the cohomology of locally constant prefactorization algebras on $\mathbb{R}^m$ that provides an obstruction to formality in every dimension $m\geqslant 2$. Our construction combines colored obstruction sequences to formality with linking spheres and generalizes the two-dimensional bracket of Bruinsma, Schenkel, and Vicedo. We use it to extend their non-formality theorem for Lie algebra factorization envelopes to all higher dimensions. We also establish new non-formality results for factorization envelopes of Lie algebras, their compactifications and generalizations to $L_\infty$-algebras, free BF-type theories, higher abelian Chern-Simons theories and their compactifications.

</details>

## Number theory

### [An elliptic Lehmer bound of exponent one at a supersingular prime](https://arxiv.org/abs/2611.32749)
*Jorge Mello* · `math.NT` · arXiv:2611.32749v1 · relevance 0.27

- **In one sentence**: Proves a lower bound of the form D^{-1-o(1)} on the Néron–Tate height of non-torsion points on elliptic curves with good supersingular reduction at a prime, which by Elkies covers all elliptic curves over Q, improving earlier exponents due to Masser and to Hindry–Silverman.
- **In plain words**: The paper studies how small a "height" (a measure of how complicated a point on a curve is) can be for points that are not of finite order. It shows that for elliptic curves with a certain good behaviour modulo a prime, such heights cannot drop below a bound that shrinks only slightly faster than one over the degree of the field generated by the point's coordinate. Via a result of Elkies, this applies to every elliptic curve over the rational numbers.</plain>
<parameter name="why">Lower bounds on heights of points are a central theme in Diophantine geometry, and this paper sharpens the known exponent from earlier work of Masser and of Hindry and Silverman. The text does not say what further consequences this has, so I cannot say more about its wider reach.
- **Background needed**: - Elliptic curve: a smooth cubic curve with a group law on its points, studied over number fields (finite extensions of the rational numbers).
- Néron–Tate height: a canonical way of assigning a non-negative size to a point; it is zero exactly on torsion points (points of finite order).
- Degree D = [K(x(P)):K]: how many steps of field extension are needed to write down the x-coordinate of the point P; a measure of the point's arithmetic complexity.
- Lehmer-type bound: a lower bound saying nonzero heights cannot be arbitrarily small, here in terms of D.
- Good supersingular reduction at a prime: a condition on how the curve behaves when reduced modulo a prime, which is special and makes the curve's reduction unusually rigid.
- Elkies' result: a statement that every elliptic curve over Q has supersingular reduction at some prime, which is what lets the theorem apply to all curves over Q.
- Notation o(1): a quantity that tends to zero as D grows, so the bound is D to the power minus one, up to small corrections. · level: research-level

<details><summary>Original abstract</summary>

Let $E$ be an elliptic curve over a number field $K$ with good supersingular reduction at a prime $\p$. We prove that the N\'eron--Tate height of every non-torsion $P\in E(\Kbar)$ satisfies $\hh_E(P)\ge c\,D^{-1}(\log3D)^{-1}\exp(-c'\sqrt{\log3D})$, where $D=[K(x(P)):K]$ and $c,c'>0$ depend only on $E$, $K$ and $\p$; so $\hh_E(P)\ge D^{-1-o(1)}$. By a result of Elkies this applies to every elliptic curve over $\QQ$, and it improves the exponents of Masser and of Hindry and Silverman.

</details>

### [Counting elliptic curves by discriminant](https://arxiv.org/abs/2611.31390)
*Stephanie Chan, Peter Koymans* · `math.NT` · arXiv:2611.31390v1 · relevance 0.27

- **In one sentence**: The paper proves an asymptotic count with a power saving for rational elliptic curves ordered by minimal discriminant, conditionally on the abc conjecture, and gives an unconditional version for curves with an extra bound on c_4, using new bounds on integral points (c_4, c_6) near the cusp c_4^3 = c_6^2.
- **In plain words**: The paper asks how many elliptic curves over the rational numbers exist when they are sorted by a size measure called the minimal discriminant. It gives a precise formula for that count, with an error term that shrinks by a power of X, but the full result assumes the abc conjecture, an unproven statement about whole numbers. Without that assumption, the authors get the same formula only for a restricted subfamily of curves.
- **Why it matters**: Counting elliptic curves is a central question in arithmetic geometry, and an error term with a power saving is a much sharper statement than a bare asymptotic. The text does not say how these results compare with earlier work or what further applications they have, so the wider significance is unclear from this abstract alone.
- **Background needed**: - Elliptic curve: a smooth cubic curve with a rational point, the basic object of study in arithmetic geometry; over the rationals it is classified up to isomorphism by invariants c_4 and c_6.
- Discriminant: a whole number built from the curve's coefficients that measures how "degenerate" it is; the minimal discriminant uses the best integer model of the curve.
- Asymptotic formula: an expression saying how a count grows as a size bound X grows, here with an error term that is a power of X smaller than the main term ("power saving").
- abc conjecture: an unproven statement that bounds how often small integers can share large prime factors; it implies strong constraints on rational points and is assumed here.
- Cusp c_4^3 = c_6^2: the singular locus of the parameter space of curves, where the curves degenerate; counting integral points near it is the technical bottleneck.
- Q-isomorphism: two curves are counted as the same if they are related by a change of variables defined over the rationals. · level: research-level

<details><summary>Original abstract</summary>

We prove an asymptotic formula with a power saving for the number of $\mathbb{Q}$-isomorphism classes of elliptic curves $E/\mathbb{Q}$ ordered by minimal discriminant, assuming the $abc$ conjecture. Unconditionally, we obtain the same asymptotic for the curves with $|\Delta_{\min}(E)| \le X$ and $c_4(E) \le X^{8/3 - \delta}$ for any fixed $\delta > 0$, by obtaining new bounds for the number of integral points $(c_4, c_6)$ near the cusp $c_4^3 = c_6^2$.

</details>

## Algebraic geometry

### [Flexible algebraic curves and fake vanishing cycles](https://arxiv.org/abs/2611.31551)
*Joshua Lehman, Tudur Lewis* · `math.GT` · arXiv:2611.31551v1 · relevance 0.15

- **In one sentence**: The paper proves that complex curves in sufficiently ample linear systems on simply connected projective surfaces (including smooth plane curves) are topologically (spin) flexible, which yields fake vanishing cycles and examples of pushed-in Seifert surfaces that need one stabilization to become spin-flexible.
- **In plain words**: The paper studies smooth curves drawn on surfaces in complex geometry, and how their shapes can be moved around inside the four-dimensional space they sit in. The authors show that for curves of this kind, any allowed rearrangement of the curve's underlying real surface can be extended to a rearrangement of the whole four-dimensional space. They use this to find simple loops on the curve that look like they could be shrunk away inside the space, but do not actually behave that way.
- **Why it matters**: The results sharpen what topology can and cannot see about algebraic curves, and they make precise the difference between loops that can be cancelled by a disk and loops that genuinely cannot. The text does not say how far the results reach beyond the cases stated, so the wider significance is unclear from this excerpt alone.
- **Background needed**: - Algebraic curves: solution sets of polynomial equations over the complex numbers; a complex curve is also a real surface.
- Linear systems and ampleness: families of curves on a surface; "sufficiently ample" means the family is large enough to have good geometric properties.
- Simply connected surface: a surface in which every loop can be shrunk to a point.
- Mapping class: a way of moving a surface onto itself, considered up to continuous deformation.
- Topological flexibility: the property that every such symmetry of the curve extends to a symmetry of the surrounding four-dimensional space.
- Vanishing cycle: a loop on a surface that can be collapsed by a disk inside the surrounding space; a "fake" one bounds a disk in the complement but is not a true vanishing cycle.
- Framing and spin structure: extra bookkeeping data attached to surfaces and disks, which the disk-bounding condition refers to.
- Seifert surface, pushed-in surface, stabilization: standard objects and operations in knot theory in four dimensions.
- Equivariant intersection form: an algebraic invariant that records how loops intersect, tracked in a setting with a symmetry action. · level: research-level

<details><summary>Original abstract</summary>

We prove that complex curves in sufficiently ample linear systems on simply connected projective surfaces are topologically (spin) flexible: any (spin) mapping class of the underlying real surface extends to a topological mapping class of the ambient 4-manifold. As a corollary, we prove that smooth curves in the complex projective plane are topologically (spin) flexible. A consequence of topological flexibility is the existence of fake vanishing cycles, that is, simple closed curves on the underlying real surface that are not vanishing cycles, yet still bound a topologically embedded $(\pm1)$-framed disk in the surface exterior. We also give examples of pushed in Seifert surfaces in $D^4$ that are not topologically spin-flexible, but become spin-flexible after a single internal stabilization. Our methods utilize the equivariant intersection form on the surface exterior.

</details>

### [Line bundles on regular semisimple Hessenberg varieties](https://arxiv.org/abs/2611.32752)
*Arkadev Ghosh, Pinakinath Saha* · `math.AG` · arXiv:2611.32752v1 · relevance 0.08

- **In one sentence**: For a connected simply-connected simple complex group G with Borel subgroup B, the paper gives a necessary and sufficient condition for the restriction map Pic(G/B) → Pic(Y) to be an isomorphism, where Y is an irreducible regular semisimple Hessenberg variety inside G/B.
- **In plain words**: The paper studies a family of geometric shapes, called Hessenberg varieties, that sit inside a standard flag space built from a symmetry group. For one especially regular kind of these shapes, it asks when every way of assigning a "line bundle" (a smooth twisting structure over the shape) on the big space carries over exactly to the smaller shape. The text states that the author gives a complete yes-or-no test for when this carries over exactly.
- **Why it matters**: The result pins down exactly when the big space's line bundles fully determine those on a subvariety, which is a precise structural question about how these shapes sit inside flag spaces. The text does not say what applications it has, so I cannot say more about its wider importance.
- **Background needed**: - Algebraic group: a group of symmetries described by polynomial equations over the complex numbers.
- Borel subgroup and flag variety G/B: the space of complete nested flags that the group acts on.
- Hessenberg variety: a subvariety of G/B cut out by a condition involving a linear operator and a "Hessenberg" shape constraint.
- Regular semisimple: a generic, well-behaved case where the operator has distinct eigenvalues.
- Picard group Pic: the group of line bundles (one-dimensional twisting structures) on a variety, up to isomorphism.
- Restriction map: taking a line bundle on the big space and viewing it on the subvariety. · level: research-level

<details><summary>Original abstract</summary>

Let $G$ be a connected simply-connected simple algebraic group over $\mathbb{C}$ and $B$ be a Borel subgroup of $G$. Let $Y$ be an irreducible regular semisimple Hessenberg variety in $G/B$. In this article, we give a necessary and sufficient condition for the natural restriction map $\mathrm{res}: \mathrm{Pic}(G/B)\longrightarrow \mathrm{Pic}(Y)$ of Picard groups induced by the inclusion $Y\subseteq G/B$ to be an isomorphism.

</details>

## Topology

### [One monoid to realize them all: a master monoid for homotopy types](https://arxiv.org/abs/2611.32655)
*Isaac Carcac\'ia-Campos* · `math.AT` · arXiv:2611.32655v1 · relevance 0.17

- **In one sentence**: The paper shows that every homotopy type (CW complex up to homotopy) can be realized as the classifying space of the translation category of an action of a single monoid on a set, obtained by collapsing the objects of the semisimplicial category while keeping its face maps, and it situates this within weak test category theory.
- **In plain words**: The paper asks whether the shapes studied in homotopy theory, which are usually described using topological spaces or structured collections of sets, can instead be captured by the action of one algebraic object, a monoid (a set with an associative operation and an identity). The authors build such a monoid by merging all the objects of a standard combinatorial category while keeping its face maps, and they show every CW homotopy type arises this way. The text presents this as a general algebraic framework rather than a new computation.
- **Why it matters**: It offers an unusual algebraic route into homotopy theory, connecting it to the theory of test categories and to monoid actions. The abstract's claims about finite presentation and which dimensions are realized are stated in the text, but the wider significance for the field is for specialists to judge.
- **Background needed**: - Homotopy type: a shape considered up to continuous deformation; CW complexes are a standard class of spaces built from cells.
- Classifying space of a category: a topological space built from a category's objects and arrows, used to encode its homotopy information.
- Semisimplicial category: a combinatorial category whose objects are ordered sets and whose maps include face operators (deleting an element).
- Monoid and monoid action: a monoid is a set with an associative operation and identity; an action assigns to each element a map on a set.
- Test category: a small category whose presheaves model homotopy types, in Grothendieck's sense.
- Translation category (action groupoid analogue): the category with objects the set elements and arrows given by the monoid action.
- Coreflective subcategory: a subcategory where each object has a best map into it from the larger category. · level: research-level

<details><summary>Original abstract</summary>

Homotopy theory has traditionally been approached either through topological spaces or through categories of presheaves on suitable combinatorial categories, a perspective subsumed by Grothendieck's theory of test categories. In this paper, we develop a more algebraic viewpoint: homotopy types can be represented by actions of a single monoid on sets. This monoid is obtained by identifying all the objects of the semisimplicial category while retaining its face operators. Every CW homotopy type is the classifying space of the translation category of one of its actions, and its truncation at dimension n is finitely presented and realizes exactly the homotopy types of dimension at most n. The construction rests on a general result: every set-valued functor on a small category freely generates an action of its universal monoid, and its category of elements is a full coreflective subcategory of the resulting translation category. Hence every weak test category gives rise to a monoid whose actions realize all homotopy types; when the category has more than one object, however, this monoid is not itself a weak test category, so that a single monoid may realize all homotopy types without modelling homotopy theory as a localization. The obstruction lies in identifying objects, not in having a single one: there are strict test categories with a single object, such as the monoid of all self-maps of an infinite set and a countable monoid of primitive recursive functions.

</details>

### [An Introduction to O-minimal Geometry](https://arxiv.org/abs/2611.32426)
*Michel Coste* · `math.AG` · arXiv:2611.32426v1 · relevance 0.12

- **In one sentence**: Lecture notes covering the foundations of o-minimal geometry, a tame setting for studying real geometric sets, through cell decomposition, dimension, triangulation, generic fibers, and smoothness.
- **In plain words**: These are lecture notes, not a report of new findings. They teach a branch of mathematics that studies shapes defined by simple rules in a way that keeps them well behaved, and they go through its main tools in six chapters. The text given is only the chapter list, so it does not show the details of any argument.
- **Why it matters**: The text gives no results or claims of novelty, so its importance cannot be judged from it. Such notes are usually used as a textbook entry point, and o-minimal geometry is known to connect to real algebraic geometry and model theory, though the text itself does not say this.
- **Background needed**: - Sets: a collection of points, such as a curve or a surface in space.
- Dimension: the number of independent directions a shape has, such as 1 for a curve and 2 for a surface.
- Triangulation: cutting a shape into small triangle-like pieces.
- Smoothness: whether a shape has no sharp corners or cusps.
- Model theory: the study of which properties can be stated in a formal logical language. · level: research-level

<details><summary>Original abstract</summary>

These lecture notes on o-minimal geometry comprise six chapters: 1 - O minimal Structures. 2 - Cell Decomposition. 3 - Connected Components and Dimension. 4 - Definable Triangulation. 5 - Generic Fibers for Definable Families. 6 - Smoothness.

</details>

## Dynamical systems

### [Doubly Intermittent Singular Skew Products](https://arxiv.org/abs/2611.31490)
*Stefano Luzzatto, Rizwan Rizwanullah* · `math.DS` · arXiv:2611.31490v1 · relevance 0.10

- **In one sentence**: The paper studies a class of skew product systems (an expanding circle map coupled with a full-branch interval map having two indifferent fixed points and unbounded derivatives), constructs an induced full-branch map, and proves an invariant probability measure equivalent to Lebesgue plus decay of correlations.
- **In plain words**: The paper looks at a mathematical model of a system that evolves step by step, where one part's motion drives another part's motion. Parts of the system move very slowly near a few special "sticky" points, which makes its long-term behaviour harder to analyse. The authors generalise earlier examples of such systems and show, by building a simpler related map, that the system has a stable long-run pattern and that its memory of the starting point fades over time.
- **Why it matters**: The text reports a generalisation of earlier skew-product results, namely the Gouëzel skew products, to a broader class of fibre maps with two sticky points and unbounded derivatives. It is a technical contribution to ergodic theory; the text does not say what applications it may have beyond that field.
- **Background needed**: - Dynamical system: a rule that repeatedly moves points in a space, such as a map of a circle or interval.
- Skew product: a coupled system where one component drives the evolution of another; equivalently, a random dynamical system.
- Uniformly expanding map: a map that stretches distances by a fixed factor everywhere, so nearby points separate quickly.
- Indifferent (neutral) fixed point: a point the map leaves nearly in place, so orbits linger near it. Intermittency maps are the standard example.
- Invariant probability measure equivalent to Lebesgue: a long-run distribution of points that has the same null sets as ordinary length, so it is not concentrated on a small set.
- Decay of correlations: how quickly the influence of the starting point on later observations fades.
- Induced map: a simpler map obtained by recording the system only at return times to a chosen region. · level: research-level

<details><summary>Original abstract</summary>

We study a large class of skew product systems, which can also be thought of as random dynamical systems, coupling a uniformly expanding circle map with a full branch interval map with two indifferent fixed points and unbounded derivatives. This significantly generalizes the setting of several skew products considered in the literature, in particular the Gou\"ezel skew products [Gou\"ezel, Statistical properties of a skew product with a curve of neutral points, Erg. Th. & Dyn. Sys. (2007)], in which the fibre maps are intermittency maps with a single indifferent fixed point and bounded derivatives. Through the construction of an induced full branch map, we prove various statistical properties of the skew products, including existence of an invariant probability measure equivalent to Lebesgue and decay of correlations.

</details>

### [Saddle-focus to saddle transition of 4D heteroclinic orbits resembling oscillatory and regularized shock waves of some dissipative Boussinesq systems](https://arxiv.org/abs/2611.31934)
*Rezwana Razzaque Angana, Brendan Harding, Dimitrios Mitsotakis* · `math.DS` · arXiv:2611.31934v1 · relevance 0.09

- **In one sentence**: The paper computes traveling-wave solutions of dissipative Bona–Smith Boussinesq systems, modeled as heteroclinic orbits in a four-dimensional phase space, and tracks how an equilibrium changes from saddle-focus to saddle as dissipation increases, so the wave shifts from oscillatory to regularized shock-like profiles; it also introduces a finite-difference numerical method for these orbits.
- **In plain words**: The paper studies wave patterns that look like the step-like fronts (bores) seen when a tidal or river surge moves through shallow water. Such waves are shaped by a balance between dispersion (spreading), nonlinearity, and dissipation (energy loss). The authors find these waves as connecting paths in a four-variable mathematical system and show that a key feature changes smoothly as energy loss increases, going from a wavy front to a smooth one.
- **Why it matters**: It links a fine-grained change in the mathematical structure of a system (a saddle-focus turning into a saddle) to a visible change in the shape of a physical wave, which is useful for understanding undular bores. The text does not indicate its wider impact beyond this model class, so the broader significance is uncertain.
- **Background needed**: - Traveling wave: a wave that keeps its shape while moving at constant speed.
- Shock wave / bore: a sharp front where water depth or height changes abruptly; an undular bore has a train of smaller waves behind it.
- Boussinesq-type model: an approximate equation for water waves in shallow water that includes dispersion.
- Dissipation: loss of energy, such as through friction, which damps waves.
- Dynamical system and phase space: a way of describing evolution by a set of variables; here the traveling-wave equations become a system with four variables.
- Equilibrium point, saddle, focus: fixed points of the system; a saddle attracts along some directions and repels along others, a focus spirals.
- Heteroclinic orbit: a trajectory that leaves one equilibrium and arrives at another, corresponding to a wave profile connecting two states.
- Finite-difference method: a numerical technique that approximates derivatives on a grid of points. · level: research-level

<details><summary>Original abstract</summary>

Oscillatory and regularized shock waves have long been studied to understand the formation and dynamics of undular bores in shallow waters, phenomena that typically arise from the interplay between dispersion, nonlinearity, and dissipation. In this work, we investigate and describe the nature and shape of traveling wave solutions that resemble oscillatory and regularized shock waves of some Boussinesq-type water wave models known as Bona--Smith systems in the presence of dissipation. The associated traveling wave equations are solutions of four-dimensional dynamical systems, leading to both computational challenges and rich structural behavior. In particular, to describe the properties of these traveling waves, we analyze heteroclinic orbits that connect two distinct equilibria, one of which undergoes a transition in the four-dimensional phase space from a saddle-focus to a saddle point as the dissipation parameter increases. This transition governs the nature of the wave profile, which evolves smoothly from an oscillatory shock wave to a regularized (non-oscillatory) shock wave. To compute such solutions, we introduce a finite-difference-based numerical method tailored for this class of problems.

</details>

## Combinatorics

### [The majority game chromatic number for dense random graphs](https://arxiv.org/abs/2611.32746)
*Stijn Cambie, Annika Heckel, Brahadeesh Sankarnarayanan et al.* · `math.CO` · arXiv:2611.32746v1 · relevance 0.33

- **In one sentence**: For fixed edge probability 2/3 < p < 1, the majority game chromatic number of the Erdős–Rényi random graph G(n,p) equals 3 with high probability.
- **In plain words**: The paper studies a two-player game on random networks: players take turns colouring the vertices of a graph so that no two neighbours share a colour, and the question is how many colours are needed. For random graphs that are fairly dense (each pair of vertices is joined with a fixed probability above two-thirds), the authors show that three colours are enough with high probability, meaning the chance of this failing goes to zero as the graph grows.
- **Why it matters**: It gives a sharp answer for a specific range of densities in a game-version of graph colouring, a classical topic. The text does not say how the result compares with other ranges of p or with related games, so its wider significance is uncertain.
- **Background needed**: - Graph: vertices joined by edges; a proper colouring gives adjacent vertices different colours.
- Chromatic number: the fewest colours needed for a proper colouring.
- Erdős–Rényi random graph G(n,p): n vertices, each pair joined independently with probability p.
- "With high probability": the probability of the stated outcome tends to 1 as n grows.
- Game chromatic number: a variant where two players alternately colour vertices; the "majority" version has a specific set of rules not described in the given text. · level: research-level

<details><summary>Original abstract</summary>

We show that for every fixed $2/3<p<1$ the majority game chromatic number of the Erd\H{o}s--R\'enyi random graph $G_{n,p}$ is $3$ with high probability.

</details>

### [On some off-diagonal hypergraph Ramsey problems](https://arxiv.org/abs/2611.32594)
*Eion Mulrenin, Cosmin Pohoata* · `math.CO` · arXiv:2611.32594v1 · relevance 0.11

- **In one sentence**: A short new proof that the 3-uniform off-diagonal Ramsey number r_3(K_4^-, K_n) is at least 2^{Ω(n log n)}, using a construction linked to a directed graph from Bradač's work on off-diagonal graph Ramsey numbers, with sharp bounds claimed for higher-uniformity extensions.
- **In plain words**: This paper is about a question in combinatorics: how large a set must be before any way of coloring its groups of items is forced to contain a particular pattern. The authors give a shorter proof of an earlier result by Fox and He about one such case, and the proof uses a construction tied to a directed graph studied by Bradač. They also say the same idea extends to several related problems with more items per group, which answers questions posed by Mubayi and Suk.
- **Why it matters**: The work simplifies an existing lower-bound argument and, according to the abstract, yields sharp bounds for several generalizations that other researchers had asked about. It is a specialist result, and the text does not say how broadly it will matter beyond this area of Ramsey theory.
- **Background needed**: - Ramsey number: the smallest size of a structure guaranteed to contain a given pattern when its elements are colored or split in every possible way.
- Graph vs. hypergraph: a graph links pairs of vertices; a 3-uniform hypergraph links triples of vertices.
- K_4^- and K_n: K_n is a complete graph on n vertices (every pair linked); K_4^- is four vertices with five of the six links, a small pattern to look for.
- Off-diagonal: the two patterns searched for are different, so the problem is asymmetric.
- Lower bound 2^{Ω(n log n)}: a rough growth rate saying the number grows roughly exponentially in n log n; it shows how large the number must be at least.
- Sharp bound: a bound that matches the known answer up to constant factors. · level: research-level

<details><summary>Original abstract</summary>

We give a new short proof of a theorem of Fox and He that the $3$-uniform Ramsey number $r_3(K_4^-, K_n)$ is at least $2^{\Omega(n \log n)}$. The construction exploits a new connection with a directed graph recently introduced by Brada\v{c} in his work on off-diagonal graph Ramsey numbers. Moreover, it generalizes naturally to give sharp bounds for several extensions of this problem in higher uniformity, answering questions raised by Mubayi and Suk.

</details>

## Numerical analysis

### [An adaptive finite element method for the interior problem of Helmholtz equations with generalized transmission boundary conditions](https://arxiv.org/abs/2611.32479)
*Zhe Zhu, Lei Lin, Wei Yang et al.* · `math.NA` · arXiv:2611.32479v1 · relevance 0.26

- **In one sentence**: The paper develops and analyzes an adaptive finite element method, with a-priori and a-posteriori error estimates, for the interior transmission problem of Helmholtz equations with generalized transmission boundary conditions involving a surface Laplace-Beltrami operator, using T-coercivity and a lifting operator to establish well-posedness in nonstandard Sobolev spaces.
- **In plain words**: This paper is about a method for computing wave behavior at the boundary between two materials, where waves can pass through the interface and the interface itself has its own surface behavior. The authors build a computer method that refines its mesh where errors are largest, prove it is mathematically sound, and test it on numerical examples. They also apply the method to find special resonant frequencies (interior transmission eigenvalues) of the problem.
- **Why it matters**: Computing accurate wave solutions with complicated interface conditions matters for modeling scattering and inverse problems in acoustics and electromagnetics. The text reports numerical examples showing accuracy and convergence, but it does not say how the method compares with existing approaches beyond stating that it is efficient.
- **Background needed**: - Helmholtz equation: a standard equation describing steady wave behavior (sound, light, water waves) at a fixed frequency.
- Interior transmission problem: a setup where waves are coupled across the boundary of a region, with conditions on both sides of that boundary.
- Generalized transmission boundary conditions: rules that specify how the wave and its normal derivative must match across an interface, here including a surface term.
- Laplace-Beltrami operator: a differential operator describing how a quantity varies along a curved surface, analogous to a Laplacian restricted to the surface.
- Finite element method: a numerical technique that splits a domain into small pieces (a mesh) and solves for an approximate solution on them.
- Adaptive / a posteriori error estimates: methods that compute the error from the approximate solution itself and refine the mesh where the error is largest.
- T-coercivity and lifting operators: advanced functional-analysis tools used to prove that the variational problem has a unique, stable solution.
- Interior transmission eigenvalues: special frequencies at which the interior transmission problem has nontrivial solutions. · level: research-level

<details><summary>Original abstract</summary>

This paper proposes a new adaptive finite element method for solving the interior transmission problem with generalized transmission boundary conditions (GTBCs) involving a surface Laplace-Beltrami operator. A $\mathbb{T}$-coercivity technique relying on a lifting operator is established to show the well-posedness of the variational problem in appropriate nonstandard Sobolev spaces. Then both the a priori error estimates and a posteriori error estimates including the upper bound and local lower bound of the finite element discretization are constructed. Numerical examples are presented to illustrate the accuracy and convergence of the adaptive finite element method. Extension and high efficiency of the proposed method for the computation of the interior transmission eigenvalues for the problem with GTBCs are also discussed numerically.

</details>

### [Upwind finite element approximation of the gradient blow-up time for a viscous Hamilton--Jacobi equation](https://arxiv.org/abs/2611.31859)
*Yohei Fujishima, Takahiro Yamada* · `math.NA` · arXiv:2611.31859v1 · relevance 0.18

- **In one sentence**: The paper proves maximum-norm convergence of an upwind piecewise-linear finite element scheme, and convergence of computed gradient-blow-up times, for a viscous Hamilton–Jacobi equation with superquadratic gradient source on polytopal approximations of smooth domains in 1–3 dimensions, verified on the disk.
- **In plain words**: The paper studies a equation describing a quantity whose slope becomes infinitely steep in finite time, a "gradient blow-up." The authors use a computer method that splits the domain into small triangles or segments and uses a directional ("upwind") rule to handle the steep gradients. They prove that the computed solution approaches the true one before the steepening happens, and that the computed time of steepening approaches the true time, under stated conditions, with a worked example on a disk and numerical experiments.
- **Why it matters**: Getting the timing of a singularity right is hard for numerical methods, since small errors in a steep slope can shift the predicted event. The work gives rigorous error guarantees for this kind of problem rather than only plots, though the text does not say how it compares with other schemes or applications.
- **Background needed**: - Hamilton–Jacobi equation: a partial differential equation describing how a function evolves, often used for optimal control and front motion.
- Viscous term: a diffusion (smoothing) term that keeps solutions from becoming discontinuous too early.
- Gradient blow-up: the slope of the solution grows without bound in finite time, even though the solution itself stays bounded.
- Superquadratic source: a nonlinear growth term in the slope that grows faster than the square of the slope.
- Dirichlet boundary condition: the solution is fixed (here zero) on the edge of the domain.
- Finite element method: approximating a function by simple pieces (e.g., piecewise linear) on a mesh of small cells.
- Upwind scheme: a discretization that takes information from the direction the flow comes from, for stability.
- Maximum-norm convergence: the worst-case pointwise error goes to zero as the mesh is refined.
- Polytopal domain: a domain with straight-edged (polygonal/polyhedral) boundary approximating a smooth one. · level: research-level

<details><summary>Original abstract</summary>

We analyze an upwind finite element method with piecewise linear elements for a viscous Hamilton--Jacobi equation with a superquadratic gradient source term, subject to homogeneous Dirichlet boundary conditions. On polytopal inner approximations of smooth bounded domains in dimensions $N=1,2,3$, we prove maximum-norm convergence of the numerical solution to the exact solution before gradient blow-up and convergence of gradient-threshold times to the blow-up time under explicit mesh and regularity assumptions. We also verify the regularity assumption and finite-time gradient blow-up for an example on the disk, to which the main theorem therefore applies. Numerical experiments illustrate this gradient blow-up.

</details>

## Logic and foundations

### [Cardinal Transfer Events for Infinitary Logic with Infinitary Quantification](https://arxiv.org/abs/2611.31725)
*Edgar Valenzuela* · `math.LO` · arXiv:2611.31725v1 · relevance 0.08

- **In one sentence**: Under the assumption of a certain theory Φ, the paper claims to solve the Gap-n problem for more than one predicate in infinitary logic with infinitary quantification, via cardinal transfer events.
- **In plain words**: This paper is about a question in the foundations of mathematics: when a logical language can talk about very large infinite sizes (cardinals), and whether certain "transfer" properties of those sizes hold. The text is only a short abstract. It says the authors solve a version of the "Gap-n problem" for more than one predicate, but only under an extra assumption they call the theory Φ.
- **Why it matters**: The abstract is too brief to show how strong the result is or which open questions it settles, so its importance is hard to judge from this text alone. It likely matters to specialists in infinitary logic and set theory, but the connection to wider mathematics is not stated.
- **Background needed**: - Infinitary logic: logical languages that allow infinitely long conjunctions or disjunctions, unlike ordinary finite formulas.
- Infinitary quantification: quantifiers ("for all", "there exists") ranging over infinitely many objects at once, not just finitely many.
- Cardinals: measures of infinite size, such as how many elements an infinite set has.
- Predicates: properties or relations that a logical formula can express about objects.
- Transfer event (cardinal transfer): a statement that a structure with one pair of infinite sizes has a substructure with another pair, a standard tool in model theory.
- Gap-n problem: a question about whether certain cardinal transfer properties hold at a given level of complexity; the abstract does not define it further.
- Assumed theory Φ: an extra hypothesis, not identified in the text, on which the results depend. · level: research-level

<details><summary>Original abstract</summary>

Assuming the existence of a certain theory $\Phi$, we solve the Gap-$n$ problem for more than one predicate. This will be done for infinitary logic with infinitary quantification.

</details>

### [Alpha-Beta Pruning via Monadic Continuations](https://arxiv.org/abs/2611.32320)
*Mart\'in Escard\'o, Paulo Oliva* · `cs.AI` · arXiv:2611.32320v1 · relevance 0.06

- **In one sentence**: The paper gives a monadic (continuation- and reader-monad based) formulation of alpha-beta pruning for minimax game search, records bounds inside outcomes rather than move types, extends the ordinary continuation monad to return optimal plays, and proves the pruned search agrees with exhaustive minimax.
- **In plain words**: The paper looks at a classic method that lets a game-playing program skip parts of its search tree when those parts cannot change the best move. The authors rewrite this method using a programming pattern called monads, which packages computations in a structured way. They show it finds the same best outcomes and best sequences of moves as checking every option, and they test it on Tic-Tac-Toe, where it evaluated 39 times fewer plays than exhaustive search.
- **Why it matters**: It offers a compositional, formally verified way to express a foundational AI search algorithm inside functional programming, which may matter for building and checking game-playing software. The text reports only a single Tic-Tac-Toe test, so how well the approach scales to larger games is not shown here.
- **Background needed**: - Minimax: a search method where one player maximises and the opponent minimises the final score, looking ahead through possible moves.
- Alpha-beta pruning: an optimisation of minimax that skips branches which cannot affect the final decision.
- Monad: a programming abstraction for chaining computations with extra context (here, the continuation and reader monads manage control flow and passed-in bounds).
- Continuation: a way of representing "what happens next" as a function, letting a search decide when to stop early.
- Formal correctness proof: a mathematical argument that the optimised method always gives the same answer as the simple one. · level: research-level

<details><summary>Original abstract</summary>

Alpha-beta pruning is a fundamental technique in game-playing AI, enabling efficient minimax search by avoiding the exploration of branches that cannot affect the optimal decision. We present a monadic formulation of alpha-beta pruning based on the combination of the continuation monad and the reader monad. Unlike previous approaches that encode alpha-beta bounds into the types of available moves, our construction records these bounds within monadic outcomes, leaving the move types unchanged. We further show that the ordinary continuation monad suffices to compute not only optimal outcomes but also optimal plays, by extending the outcome type to include the corresponding sequences of moves. This provides an alternative to generalisations of the continuation monad proposed to address the inefficiencies associated with the selection monad in alpha-beta search. We illustrate our approach with an implementation of Tic-Tac-Toe, observing a 39-fold reduction in the number of plays evaluated, compared with exhaustive search, in computing an optimal play. Finally, we formally establish the correctness of our construction by proving that the monadic alpha-beta search computes the same optimal outcomes and plays as exhaustive minimax search. Our results demonstrate how a foundational algorithm in AI can be expressed and verified using standard monadic abstractions, providing a basis for further development of compositional approaches to adversarial search.

</details>

## Mathematical physics

### [Dynamical phase transition in Brownian motion via sharp large deviations](https://arxiv.org/abs/2611.31453)
*Benjamin Budway, Makiko Sasada, Mykhaylo Shkolnikov* · `math.PR` · arXiv:2611.31453v1 · relevance 0.15

- **In one sentence**: The paper proves a dynamical phase transition for Brownian motion with drift conditioned on upper large deviations of its occupation measure on [-1,1], using a new sharp large deviation estimate for that occupation measure.
- **In plain words**: The paper studies a random path (Brownian motion, the jittery motion of a particle buffeted at random) that is forced, over a long stretch of time, to spend unusually much time inside a fixed window around zero. It shows that the way the path changes under this forcing depends on how unusual the event is: for a far-out event the path follows one specific modified random motion, while for a milder event it follows a different modified motion only for part of the time and then behaves normally. The authors establish this switch mathematically rather than by experiment.
- **Why it matters**: The behaviour was predicted in the physics literature, and this text presents a rigorous proof of it, which is the main contribution. The authors also state that the sharp large deviation result they needed is of independent interest and that the approach extends to other Markov processes and additive functionals; the text does not go further than that on applications.
- **Background needed**: - Brownian motion: a continuous random path whose increments are independent Gaussian noise; the standard model of diffusing particles.
- Drift: a steady push added to the random motion.
- Occupation measure: the fraction of a time interval a path spends in each region; here, how much time it spends in [-1,1].
- Large deviation: an event that is rare but whose probability decays at a known exponential rate; "sharp" means the rate is pinned down with precise constants.
- Upper tail / near vs far: how far above the typical value the rare event sits; the paper distinguishes a near and a far regime.
- Donsker-Varadhan variational formula: a standard recipe that gives the exponential rate for occupation-type averages and identifies the optimal modified process.
- Langevin diffusion: a random process with a steady pull plus noise, here the modified process that the conditioned path converges to.
- Gibbs conditioning principle: the idea that conditioning a random system on a rare macroscopic event makes it look like the most likely configuration consistent with that event.
- Phase transition: an abrupt qualitative change in behaviour as a control parameter (here, the severity of the event) crosses a threshold. · level: research-level

<details><summary>Original abstract</summary>

We prove a dynamical phase transition in Brownian motion with drift, a phenomenon recently predicted in the physics literature. Specifically, when a Brownian motion with drift on a long time interval is conditioned on an upper large deviation event for the (normalized) occupation measure of the interval [-1,1], in the spirit of the Gibbs conditioning principle, a phase transition occurs. If one conditions on a large deviation event in the far upper tail, the conditioned process follows the Langevin diffusion suggested by the Donsker-Varadhan variational formula for additive functionals. In contrast, if one conditions on a large deviation event in the near upper tail, the conditioned process follows a different Langevin diffusion on a fraction of the time interval and subsequently behaves like the unconditioned process. We establish this phase transition via a new sharp large deviation result for the occupation measure, which is of independent interest. We also provide further corollaries of this result and discuss generalizations to other Markov processes and additive functionals.

</details>

### [The role of composition rules in an axiomatic derivation of quantum mechanics](https://arxiv.org/abs/2611.32237)
*Erkka Haapasalo, Pekka Lahti, Juha-Pekka Pellonp\"a\"a* · `quant-ph` · arXiv:2611.32237v1 · relevance 0.13

- **In one sentence**: The paper revisits how local effects and states of subsystems are embedded into compound-system effect and state spaces within an information-theoretic axiomatization of quantum mechanics, building on earlier work by Matolcsi and by Aerts and Daubechies, and reformulates the local-discrimination and purification axioms of D'Ariano et al.
- **In plain words**: This paper looks at the mathematical rules that describe how a quantum system made of several parts is built from its individual parts. Quantum theory usually assumes this via a standard construction called the tensor product, and the authors ask how that construction should follow from more basic rules. They restate two of the principles used in a well-known set of axioms for quantum theory in a weaker form, and they propose rules for when different joint states can be told apart by measuring each part separately.
- **Why it matters**: Deriving the standard mathematics of quantum theory from a few plain, physically motivated principles is an active foundational question, and this work tightens the step that handles composite systems. The text does not show whether the weaker axioms lead to new results; the authors only say they believe the reformulation could be useful for future axiomatizations.
- **Background needed**: - Quantum theory axiomatization: deriving the mathematical framework of quantum mechanics from a small set of stated principles, rather than taking it as given.
- States and effects: a state describes what a system is like; an effect describes a measurement outcome (a yes/no test). Both live in mathematical spaces.
- Compound system: a system made of several parts, such as two particles, whose joint state must be built from the parts.
- Tensor product: the standard mathematical way to combine two spaces into one for a joint system; the paper refines this by specifying which versions (projective, injective) are needed for states and effects.
- Local discriminability: the idea that different joint states can be distinguished by measuring each part separately.
- Purification: the principle that a mixed (partly random) state of a system can be seen as part of a pure state of a larger system. · level: research-level

<details><summary>Original abstract</summary>

Local discriminability and purification are two key axioms in an information-theoretic axiomatization of quantum mechanics as proposed by G. M. D'Ariano et al. (Quantum Theory from First Principles, 2017). Both of them refer to compound systems, the theory of which is rather directly assumed to be given by the tensor product structure. This structure, though well understood, should, however, be based on a more careful study of formal composition rules describing how local effects can be embedded into the compound effect space and how to reduce joint states onto subsystems. In that we follow the earlier work of T. Matolcsi, (Acta Sci. Math., 1975), and D. Aerts and I. Daubechies, (Helvetica Physica Acta, 1978), as summarized, e.g., in The Logic of Quantum Mechanics, 1981, by E. Beltrametti and G. Cassinelli. We also establish axioms of local discrimination stating that compound states can be told apart by local measurements the notion of which we also formally define. The purification axioms first introduced as axioms of quantum mechanics by D'Ariano et al. are also rewritten in a weaker form which we believe could be fruitful for future axiomatizations. These reformulations bring us closer to proper tensor product structures for joint state and effect spaces, so that the embedding map for states factors through the projective tensor product of the local state spaces and the embedding map for effects factors through the injective tensor product of the local effect spaces. We also discuss the case of multipartite composition axioms and associativity properties required in these settings.

</details>

## Optimization and control

### [Mirror flow for semimartingale optimal transport](https://arxiv.org/abs/2611.32785)
*Francois Buet-Golfouse, Ana\"is Despr\'es, Anna Kazeykina et al.* · `math.OC` · arXiv:2611.32785v1 · relevance 0.20

- **In one sentence**: The paper proposes a mirror flow (a preconditioned mirror-descent scheme) for the dual problem of semimartingale optimal transport, proves geometric convergence of the continuous-time sequence, and gives a discrete first-order linearized scheme with a uniform-in-time error bound on accumulated linearization error under a smallness condition on initial error.
- **In plain words**: The paper looks at a family of "best way to move one random process into another" problems, which arise in mathematical finance and in some AI image-generation models. Standard gradient-descent solvers for these problems are slow because the function being minimized is badly scaled. The authors use a mirror-descent approach that reshapes the problem so it is easier to optimize, and they build a practical step-by-step version of it.
- **Why it matters**: Slow solvers are a practical bottleneck for these problems, so a better-conditioned method could matter for finance and generative modelling. The text reports a substantial efficiency gain only for one specific problem (SEMOT), so its wider reach is not established here.
- **Background needed**: - Optimal transport: finding the cheapest way to reshape one probability distribution into another.
- Semimartingale: a broad class of random processes (including Brownian-motion-driven ones) used to model prices and paths.
- Dual problem: an equivalent reformulation in terms of a "potential" function; here the potential is what gets optimized.
- Gradient descent: iteratively nudging a solution downhill; slow when the landscape is badly scaled (poorly conditioned).
- Mirror descent: a variant that updates in a transformed space, which can fix poor scaling.
- Geometric convergence: error shrinks by a fixed factor each step, i.e., exponentially fast.
- Linearization: replacing a nonlinear update with its first-order approximation to make it computable. · level: research-level

<details><summary>Original abstract</summary>

Semimartingale optimal transport arises in a wide range of applications, including mathematical finance and flow-based generative models. A recurring computational challenge is that the dual energy functional is often poorly conditioned with respect to the dual potential, leading to slow convergence of gradient descent algorithms. To address this issue, we investigate a mirror flow approach that effectively preconditions the dual energy functional. We establish the geometric convergence of the mirror descent sequence. To obtain a practical numerical algorithm, we introduce a feasible discrete-time scheme based on first-order linearization. We prove that the scheme is well-defined and establish a uniform-in-time error bound for the accumulated linearization error, under a suitable smallness condition on the initial error. Finally, we apply the proposed mirror flow scheme to the specific-entropic martingale optimal transport (SEMOT) problem \cite{BuetGolfouseEtAl2026SEMOT} and observe a substantial improvement in computational efficiency.

</details>

### [Beyond Classical Minimax Rates: Quantum Sampling in Gradient-Based Simulation Optimization](https://arxiv.org/abs/2611.32004)
*Hao Cao, Jian-Qiang Hu, Mingjie Hu et al.* · `quant-ph` · arXiv:2611.32004v1 · relevance 0.17

- **In one sentence**: For convex simulation optimization with noisy gradient estimates, the paper shows quantum mean estimation applied to paired finite differences improves the query-complexity exponent from classical N^{-2/3} to N^{-4/3}, with coupling-dependent variants and claimed matching minimax lower bounds for fixed dimension.
- **In plain words**: The paper looks at how to find the best setting of a system when you can only learn about it through noisy simulations, and each simulation run is expensive. The authors estimate slopes (gradients) by comparing nearby simulation runs, and they use a quantum computing technique for averaging noisy results to get more accurate slopes from the same number of runs. They report that this speeds up how quickly the error shrinks as the budget of runs grows, and that the resulting rates cannot be beaten under the stated assumptions.
- **Why it matters**: It claims a concrete change in how query budget translates into accuracy, backed by lower bounds, which matters for anyone designing costly simulation-based optimization. Its practical relevance depends on whether quantum sampling hardware can actually supply the required queries; the text does not address that.
- **Background needed**: - Simulation optimization: tuning inputs to a model that returns noisy outputs rather than exact values.
- Gradient: the slope of the objective, telling you which direction to adjust inputs.
- Finite differences: estimating a slope by running the system at two slightly different inputs and comparing.
- Convex problem: one with a single bowl-shaped optimum, so local search can find it.
- Convergence rate / query complexity: how fast the error shrinks as the number of simulation runs N grows; a larger exponent means faster improvement.
- Minimax optimal: the best achievable worst-case rate, and no method can do better for that class of problems.
- Quantum mean estimation: a quantum-computing method that estimates an average with fewer samples than classical averaging, under the assumption that quantum queries are available. · level: research-level

<details><summary>Original abstract</summary>

We study gradient-based search for a class of convex simulation optimization problems with gradients estimated from noisy outputs. With independent outputs, the optimal classical convergence rate for the expected objective gap is of order $O(N^{-2/3})$, where $N$ is the query budget. We apply quantum mean estimation to paired finite differences and progressively increase their estimation accuracy as the perturbations shrink, improving the convergence rate to $O(N^{-4/3})$. Furthermore, we show that coupling nearby evaluations improves the classical and quantum convergence rates to $O(N^{-2/(3-\kappa)})$ and $O(N^{-4/(3-\kappa)})$, respectively, where $\kappa\in[0,1]$ describes the variance reduction in paired outputs. Thus, quantum estimation halves the accuracy exponent in query complexity across coupling orders. Moreover, we establish matching lower bounds and show that these accuracy exponents are minimax optimal for fixed decision dimension, even when query locations and batch sizes are adaptive. Reconstruction from feasible differences retains the exponents when every simulation query must be feasible and accommodates boundary optima.

</details>

## Statistics theory

### [Sharp Hellinger Risk of the Multivariate Gaussian NPMLE](https://arxiv.org/abs/2611.31728)
*Xingzhou Wang, Zheng Li* · `math.ST` · arXiv:2611.31728v1 · relevance 0.11

- **In one sentence**: The paper shows that the unconstrained nonparametric maximum likelihood estimator for multivariate Gaussian location mixtures with sub-Gaussian tails attains the minimax rate (log n)^d/n under squared Hellinger loss, improving an earlier (log n)^{d+1}/n bound by a log factor, via a sharp bracketing bound for multivariate polynomials.
- **In plain words**: Statisticians often estimate an unknown probability distribution from random samples, and a standard tool for this is the "maximum likelihood" estimate, which picks the distribution that makes the observed data most probable. This paper studies that estimate for a particular family of bell-curve-shaped mixtures in several dimensions. It proves that the estimate is as accurate as theoretically possible, up to the best achievable constant-free rate, and removes an extra logarithmic factor that earlier analyses had left in the error bound.
- **Why it matters**: The result closes a gap between an upper bound and a matching lower bound for a well-studied estimator, which tells us the estimator is optimal rather than merely good. The main technical tool, a sharp count of how many small pieces are needed to cover polynomial functions, may be useful in other problems about function classes; the text does not show how far it extends beyond this setting.
- **Background needed**: - Gaussian (bell-curve) location mixture: a distribution formed by averaging normal distributions with different centers drawn from an unknown mixing distribution.
- Nonparametric maximum likelihood estimator (NPMLE): the mixing distribution that maximizes the likelihood of the observed data, with no fixed parametric shape assumed.
- Hellinger distance: a way to measure how far apart two probability densities are; squared Hellinger loss is the error measure used.
- Minimax rate: the best worst-case error any estimator can achieve; a matching lower bound shows no method can do better.
- Sub-Gaussian tails: the mixing distribution's probability of far-away values decays at least as fast as a normal distribution's.
- Bracketing number: the number of small "brackets" needed to cover a function class at a given precision; its logarithm measures the class's complexity.
- Total degree of a polynomial: the highest sum of exponents across its variables. · level: research-level

<details><summary>Original abstract</summary>

For multivariate Gaussian location mixtures whose mixing distributions have coordinatewise sub-Gaussian tails, we prove that the unconstrained nonparametric maximum likelihood estimator attains the minimax rate $(\log n)^d/n$ under squared Hellinger loss. This holds for every fixed dimension $d\geq2$ and every fixed tail parameter $\sigma>0$. The upper bound applies to every measurable choice of a global likelihood maximizer and improves the earlier bound of order $(\log n)^{d+1}/n$ by a factor of $\log n$. A key step is a sharp bracketing bound for multivariate polynomials. For the $L^2(\rho)$ unit ball of real polynomials in $d$ variables with total degree at most $m$, the log bracketing number at width $\varepsilon$ is at most $\binom{m+d}{d}\log(C_d/\varepsilon)$ for $0<\varepsilon\leq1$. The constant $C_d$ depends only on $d$. The bound holds for every positive Borel measure $\rho$ under which each nonzero polynomial in the space has a finite, positive $L^2(\rho)$ norm. We prove the bound using volume estimates for a complex Veronese cone and Gaussian small-ball probabilities, then apply it to bound the local Hellinger bracketing entropy of Gaussian mixture densities. We obtain the matching minimax lower bound by adapting the Hermite perturbation construction of Kim and Guntuboyina.

</details>

### [Aalen-Johansen as an augmented IPCW estimator](https://arxiv.org/abs/2611.32026)
*Lu Mao* · `stat.ME` · arXiv:2611.32026v1 · relevance 0.06

- **In one sentence**: The paper shows that the Aalen-Johansen estimator of state occupation probabilities is an augmented inverse-probability-of-censoring-weighted estimator, decomposes its influence function against the semiparametric efficient one, and proposes a model-free least-squares augmentation that narrows the gap under non-Markov processes without increasing asymptotic variance.
- **In plain words**: The paper looks at a standard method for estimating how likely a person is to be in each of several health or event states over time, when some people are lost to follow-up (censored). The authors show that this standard method can be rewritten as a weighted correction that also uses a simple prediction based only on each person's current state. They then propose a small adjustment that uses more of each person's past history, and report that it reduces the gap under non-Markov (history-dependent) processes in theory and in simulations.
- **Why it matters**: The Aalen-Johansen estimator is widely used in medical and survival studies, so a clearer account of why it holds up when its modelling assumption is wrong is of practical interest. The text does not indicate applications beyond simulations, so its real-world impact is unclear from the abstract alone.
- **Background needed**: - State occupation probability: the chance a subject is in a given state (e.g., healthy, ill, dead) at a given time.
- Censoring: when a subject's follow-up ends early, so their outcome is unknown.
- Inverse probability of censoring weighting (IPCW): reweights observed subjects to account for those censored, by dividing by their estimated chance of remaining under observation.
- Aalen-Johansen estimator: the standard nonparametric estimator for multi-state survival data, which implicitly assumes a Markov process (future depends only on the current state).
- Non-Markov process: one where past history beyond the current state affects future transitions.
- Influence function and semiparametric efficiency: a way of describing how an estimator responds to individual data points, and the lowest achievable variance among a broad class of estimators.
- Augmentation: adding a correction term with mean zero that can reduce variance or bias without changing the target. · level: research-level

<details><summary>Original abstract</summary>

We show that, in every sample, the widely used Aalen-Johansen estimator of a state occupation probability is an inverse probability of censoring weighted estimator augmented by a working Markov prediction from each subject's current state. This identity explains the robustness of the Aalen-Johansen against departures from the Markov assumption. It also reveals that its influence function differs from the semiparametric efficient one by two orthogonal components: the information in earlier history beyond the current state, and the error of the Markov prediction. Based on this decomposition, we propose a practical, model-free least-squares augmentation of the Aalen-Johansen that regresses the outcome on a history score, narrowing the gap under non-Markov processes without increasing the asymptotic variance. Its advantages are validated both theoretically and in simulations.

</details>

## Statistical methods and applications

### [Admissibility of Linear Time Series Models under Cone Constraints](https://arxiv.org/abs/2611.32414)
*Won-Ki Seo* · `math.ST` · arXiv:2611.32414v1 · relevance 0.16

- **In one sentence**: The paper gives a necessary and sufficient support condition for stationary Hilbert-space linear processes to stay almost surely inside a closed convex cone, and studies what this implies for additive linear models of quantiles, densities and covariance operators.
- **In plain words**: Many data objects, such as probability densities, quantile curves and covariance matrices, must obey built-in rules (for example, being non-negative or increasing). The paper asks when the usual additive way of modelling a series over time, where each value is a weighted sum of past random shocks, can respect those rules. It finds that with certain shock distributions, including Gaussian ones, the randomness is forced into a restricted subspace, and it constructs working models that avoid this for quantiles, densities and covariance matrices.
- **Why it matters**: Standard linear time series models are widely used, so knowing exactly when they remain valid for constrained objects matters for applied modelling of distributions and covariances. The text is a theoretical abstract, so its practical reach beyond these model classes is not shown here.
- **Background needed**: - Stationary time series: a process whose statistical behaviour does not change over time.
- Linear process: each value is a weighted sum of current and past random shocks (innovations).
- Hilbert space: an infinite-dimensional vector space, used here so that functions such as densities or quantile curves can be treated as data points.
- Closed convex cone: a set closed under addition and non-negative scaling, such as non-negative functions or positive semidefinite matrices; the "largest linear subspace" inside it is the part where the cone's constraints act like ordinary equalities.
- Almost surely: holding with probability one.
- Fractional filter: a weighting scheme with slowly decaying coefficients, giving long-memory behaviour.
- Quantile function: the inverse of a cumulative distribution function, describing the spread of a distribution.
- Mean square boundedness: the average squared size of a quantity stays finite over time. · level: research-level

<details><summary>Original abstract</summary>

Time series analysis extends beyond vector-valued observations to evolving probability densities, quantile functions, and covariance operators. These objects carry intrinsic constraints, raising questions about the admissibility of additive linear models, which have long served as a foundation for time series modelling and theory. We give a necessary and sufficient support condition for a stationary Hilbert-space linear process to remain in a closed convex cone almost surely. Innovations with unbounded lower tails, including Gaussian innovations, confine randomness to the cone's largest linear subspace. For fractional filters with convergent normalized cumulative coefficients, the leading stochastic directions obey the same restriction, even with bounded innovations. For real-line quantiles, variation under unbounded lower tails and leading fractional accumulation can occur only through location shifts. For cone-valued processes, partial sums of centred stationary increments remain bounded in mean square when evaluated by any linear functional that is nonnegative on the cone, in contrast to the growing variance of a random walk. We derive an exact slope criterion for locally absolutely continuous quantiles and construct nondegenerate additive models with bounded innovations for quantiles, densities, and covariance matrices. These findings clarify the scope of ordinary additive modelling under structural constraints.

</details>

### [Exact local queries for pseudo-marginal Markov chains](https://arxiv.org/abs/2611.32955)
*Zihan Xu* · `stat.CO` · arXiv:2611.32955v1 · relevance 0.14

- **In one sentence**: The paper proposes "decision certificates" built from finite historical parameter ranges that let a pseudo-marginal Markov chain on Gaussian graph priors answer prespecified local queries exactly, without resolving all neighbouring updates first, and reports work bounds and experiments on path/grid graphs and two applications.
- **In plain words**: Markov chain samplers are computer procedures that wander through possible parameter settings to approximate a probability distribution, and often each step depends on earlier steps. This paper looks at how to read off the value of one part of such a chain on demand, without recomputing everything that came before. The authors report that, under their stated assumptions, this selective method recovers the same results as the full computation while doing less work for sparse requests, though full requests were faster with the alternative method.
- **Why it matters**: It targets a practical cost problem in Bayesian computation, namely how much work is needed to query one piece of a long sampling chain, and it tests the idea on tomography and classification examples. The text does not show how broadly the approach would transfer beyond the stated graph families and models.
- **Background needed**: - Markov chain: a sequence of random states where each new state depends on the previous one.
- Pseudo-marginal sampling: a Monte Carlo method where an estimate of a likelihood (how well data fit a setting) replaces its exact value, while still targeting the correct distribution.
- Gaussian graph prior: a probability model over parameters attached to nodes of a network (graph), where neighbouring nodes are linked.
- Auxiliary variables: extra randomly introduced variables that make sampling easier.
- Picard iteration: a method that repeatedly refines a guess until it stops changing, used here as a comparison.
- Gaussian process classification: a method that learns a flexible function to sort data into classes.
- Positron emission tomography (PET): an imaging method that reconstructs a spatial map from detected emissions.
- Monte Carlo uncertainty: the error that comes from using finite random samples. · level: research-level

<details><summary>Original abstract</summary>

Local queries of a Markov chain can depend on past updates outside the queried components. For pseudo-marginal chains with Gaussian graph priors, we construct decision certificates from finite historical parameter ranges to settle updates before all neighbouring records are resolved. Under shared random inputs and exact arithmetic, the executor recovers the reference parameters, auxiliary variables and likelihood estimates for any prespecified finite query sequence. We bound conditional expected work, including likelihood evaluation, historical range construction and execution management. On specified path and grid families, we fix per-node history lengths and all other parameters in the work bounds. As graph size grows, expected incremental work stays bounded for certificate execution and grows linearly for the specified cached pointwise evaluator answering the same query. In controlled experiments, certificate execution is faster than pointwise and parallel Picard execution for sparse queries, whereas Picard is faster than certificate execution for full queries. We apply the method to positron emission tomography and Gaussian process classification of Landmine data. For a fixed numerical tomography posterior, certificate execution completes all queries of regional mean distribution volume within budget, while full execution completes none from the same initial cache. In Landmine, posterior summaries of the difference in log length scales between two sites agree across pseudo-marginal and ancillary augmentation samplers within estimated Monte Carlo uncertainty. Certificate execution resolves almost every scheduled update over the full query sequence.

</details>

## AI industry news

### [Where scientists draw the line on AI agents](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents)
** · `huggingface.co` · Hugging Face - Blog · relevance 0.13

- **In one sentence**: A news article titled "Where scientists draw the line on AI agents" that, as provided, has no body text, so its content on how researchers define or limit AI agents cannot be verified.
- **In plain words**: This is a news piece about where researchers set boundaries for AI agents, which are AI systems that can take actions on their own, such as browsing the web or running tasks. The text provided is empty, so I cannot tell what specific view, study, or event it covers.
- **Why it matters**: The topic of limits on autonomous AI systems is an active area of public and research debate, so the subject is relevant. Beyond the title, however, I cannot say what the article claims or how strong its evidence is.
- **Background needed**: - An "AI agent" is an AI system that does multi-step tasks with little human input, such as booking, searching, or editing files.
- "Drawing the line" here likely means deciding what such systems should and should not be allowed to do, or how they should be defined.
- Debates in this area often involve safety, reliability, and who is responsible when an automated system makes a mistake.
- The article's body text was not available, so the specifics must be checked against the original source. · level: introductory

<details><summary>Original abstract</summary>



</details>

### [Anthropic’s Dario Amodei calls accusations of surrendering human control to AI ‘absurd’](https://techcrunch.com/2026/11/25/anthropics-dario-amodei-calls-accusations-of-surrendering-human-control-to-ai-absurd/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.11

- **In one sentence**: Anthropic CEO Dario Amodei publicly rejects rivals' claims that he favors handing human decision-making over to AI, as leading labs increasingly automate parts of their own research and model development.
- **In plain words**: The article reports on a public dispute between Anthropic's chief executive, Dario Amodei, and critics who say he wants to give up human control to AI systems. Amodei calls that charge "absurd." The piece also notes that top AI companies are increasingly using AI to help build their own AI models and do research.
- **Why it matters**: The debate touches on a live question: if AI companies hand more of their own development work to AI, how much human oversight remains. The text is short and gives only Amodei's rejection of the accusation, so it does not show who the critics are or what specific plans are at issue.
- **Background needed**: - Anthropic is an AI company that develops the Claude family of AI models.
- "Automating research" means using AI systems to carry out parts of the work of designing and testing new AI, rather than only humans doing it.
- "Human agency" or "human control" refers to people keeping the final say over important decisions, including those made by AI.
- The article gives no details of the rivals' specific statements, so the exact nature of the accusation is only summarized. · level: intermediate

<details><summary>Original abstract</summary>

Anthropic CEO Dario Amodei pushes back against rivals’ accusations that he favors surrendering human agency to AI, even as leading AI companies increasingly automate their own research and model development.

</details>

### [An Indic Voice Agent with CUGA](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga)
** · `huggingface.co` · Hugging Face - Blog · relevance 0.10

- **In one sentence**: A news item titled "An Indic Voice Agent with CUGA" that appears to concern a voice-based AI agent for Indian languages built with a system called CUGA, but the body text is unavailable, so details cannot be confirmed.
- **In plain words**: The item seems to be about a spoken-word AI assistant designed for languages used in India. The text provided is empty, so I cannot say what was built, how well it works, or what was tested. Only the title is available.
- **Why it matters**: Voice assistants that handle many Indian languages could matter for reaching users who do not read or speak English well. Beyond the title, I cannot tell whether this is a significant advance or a small project, so the reader should check the original source.
- **Background needed**: - A "voice agent" is an AI system that listens to speech, works out what is wanted, and replies or takes action by voice.
- "Indic" refers to the languages of the Indian subcontinent, such as Hindi, Tamil, Bengali and others.
- "CUGA" is named only in the title; I do not know what it is from this text.
- Speech systems for less widely studied languages often need more data and testing than English systems do. · level: intermediate

<details><summary>Original abstract</summary>



</details>

### [Want to buy your kid an AI toy this Christmas? Not in New York](https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/)
*Rebecca Bellan* · `techcrunch.com` · AI News & Artificial Intelligence | TechCrunch · relevance 0.10

- **In one sentence**: New York has reportedly banned AI chatbot toys for five years, citing safety failures found in new Common Sense Media research, including exposure to inappropriate content and risks to emotional development.
- **In plain words**: New York has put a five-year ban on AI chatbot toys, meaning toys that hold conversations using artificial intelligence. The article says this follows new research from Common Sense Media, a children's media advocacy group, which found safety problems. The research reportedly points to children being exposed to inappropriate content and to possible harm to their emotional development.
- **Why it matters**: Parents buying gifts and regulators deciding what children can use both depend on evidence like this. The short text does not say how the research was done or how many toys were tested, so the scale of the findings is unclear.
- **Background needed**: - AI chatbot: a program that holds back-and-forth conversations in natural language, here built into a toy.
- Common Sense Media: a US nonprofit that rates and reviews media and technology for families and children.
- Emotional development: how children learn to understand and manage feelings and relationships.
- The article is brief and reports the ban and the findings without the full details of either. · level: introductory

<details><summary>Original abstract</summary>

New York has banned AI chatbot toys for five years as new research from Common Sense Media reveals troubling safety failures, including exposure to inappropriate content and risks to emotional development.

</details>

### [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood)
** · `openai.com` · OpenAI News · relevance 0.09

- **In one sentence**: A news piece titled "How iFood scales coding agents across 15,000 repositories," though the body text is missing, so only the headline's subject (scaling AI coding agents across a very large set of code repositories at the food-delivery company iFood) can be identified.
- **In plain words**: This item is about how the Brazilian food-delivery company iFood uses AI "coding agents," programs that can write or change software on their own, across about 15,000 code repositories (storage spaces where a project's source code is kept). The text itself is not available, so I cannot say what approach was used or what results were reported.
- **Why it matters**: Companies running AI tools across thousands of software projects at once is a practical question for engineering teams, but the article's content is unknown here, so its significance cannot be judged from what is provided. It may connect to wider efforts to bring AI assistants into large software organizations.
- **Background needed**: - Coding agent: an AI system that can read code, make changes, and run tasks with limited human direction.
- Repository (repo): a stored collection of a software project's code and its change history, often managed with tools like Git.
- Scaling across many repos: applying the same tool or process to thousands of separate projects, which raises questions about reliability, review, and cost.
- iFood: a large food-delivery platform based in Brazil.
- Note: the article text was empty, so no details, figures, or claims from the piece are confirmed here. · level: intermediate

<details><summary>Original abstract</summary>



</details>

## Model architectures and training

### [Eliciting the Recall Capacity of Linear Attention](https://arxiv.org/abs/2611.32969)
*Johan Lindqvist, Antonio Orvieto* · `cs.LG` · arXiv:2611.32969v1 · relevance 0.32

- **In one sentence**: The paper studies why linear-attention language models recall information from context far worse than softmax attention, and shows that targeted training changes (in-context sentence repetition and context-sensitive loss reweighting) narrow that gap without changing the architecture.
- **In plain words**: Language models often need to look back at earlier text and pull out a specific detail, such as a name paired with a fact. Linear-attention models, which are cheaper to run than the standard kind, are noticeably worse at this. The paper tests this gap with synthetic tasks and natural text, and finds that the models can learn this skill when training is adjusted to reward it.
- **Why it matters**: Linear attention is an attempt to make language models cheaper on long inputs, so a recall deficit is a real cost of that efficiency. The result suggests the gap may be partly a training problem rather than a fixed limit of the design, though the text does not show how well this carries over to larger or different production models.
- **Background needed**: - Attention: the mechanism in language models that lets each word look back at earlier words in the input.
- Softmax attention: the standard form of attention, which is accurate at recall but its cost grows quickly with input length.
- Linear attention: a cheaper approximation whose cost grows in a straight line with input length, but which keeps a fixed-size memory of past text.
- Associative recall: a test where the model must output the value linked to a given key, such as a name and its number, seen earlier in the text.
- State size: how much information the fixed memory can hold; the paper links it to how many items can be recalled.
- Loss reweighting: changing how much each training prediction counts, so that recall-relevant predictions get more emphasis. · level: research-level
- Matched keywords: attention, linear attention, architecture

<details><summary>Original abstract</summary>

Linear attention models exhibit a disproportionate deficit relative to softmax attention in associative recall (AR) in language modeling. We investigate this gap through natural language evaluations, synthetic recall tasks, and targeted training interventions. Using a synthetic setting, we quantify the role of state-size in how many items can be recalled from memory and find a similar empirical scaling across the tested linear-attention architectures. Testing this relationship reveals that even a single layer at scale can learn to retrieve thousands of associations across long distances. Yet, standard language model training does not reliably teach a linear model to copy from context, whereas a comparable softmax model learns to do so. Considering this, we strengthen recall supervision during training through in-context sentence repetition and context-sensitive loss reweighting. Both methods improve recall-intensive benchmark performance and narrow the long-distance AR gap to the softmax baseline without changing the architecture, token budget, or number of optimization steps, at a slight cost to general language modeling. These targeted changes to training can thus elicit substantial but underutilized retrieval capacity in linear-attention models. These findings suggest that, although linear-attention architectures have substantial capacity for recall, their inductive biases and the demands of language model training make it difficult to develop this capability without dedicated incentives.

</details>

### [Structure-Aware Transformers for Hierarchical Authorization in Personal AI Agents](https://arxiv.org/abs/2611.32018)
*Dongyu Cui, Jie Ding, Xuan Bi* · `cs.LG` · arXiv:2611.32018v1 · relevance 0.31

- **In one sentence**: PATH is a transformer-based neural network that predicts users' permission decisions for hierarchically organized authorization requests from personal AI agents, using hierarchy-aware attention masks, a parent-gated probability formulation, and hierarchy-level embeddings, with reported finite-sample risk bounds and zero hierarchy violations in experiments.
- **In plain words**: Personal AI assistants that act for you often ask for many permissions, and approving each one by hand is tedious while approving everything is risky. This paper proposes a model that learns from a user's past yes-or-no decisions to predict how they would answer new permission requests, so they only need to step in where it matters. The authors report that the model predicts well on simulated data, AI-generated profiles, and real user data, and that its predictions never break the parent-child structure of the permission categories.
- **Background needed**: - Personal AI agent: software that performs multi-step tasks for a user, such as booking, messaging, or file access, and must ask permission for sensitive actions.
- Authorization: a user's decision to allow or deny a given permission request.
- Hierarchical requests: permissions organized in parent-child categories, where a child permission only makes sense if its parent is considered.
- Transformer: a neural network architecture that uses attention to weigh relationships among items in a sequence; attention masks restrict which items can relate to each other.
- Parent-gated probability: a prediction for a child category that is conditioned on its parent's prediction, so the two stay consistent.
- Sparse observations: few recorded user decisions relative to the number of possible permissions.
- Finite-sample risk bounds and convergence: theoretical guarantees on how prediction error shrinks with more data and whether the training procedure settles on a solution. · level: research-level
- Matched keywords: transformer, attention, architecture

<details><summary>Original abstract</summary>

Personal AI agents can carry out complex, multi-step tasks on users' behalf, but doing so often involves numerous permission requests. Manually reviewing each request is time-consuming, while indiscriminate approval poses privacy and security risks. Predicting users' authorization preferences offers a way to reduce this burden while preserving user control. However, authorization prediction is challenging because permission requests are often hierarchical and observed user decisions are sparse and potentially correlated. To address these challenges, We propose the Parent-gated Authorization Transformer for Hierarchies (PATH) to predict users' authorization preferences for personal AI agents. PATH is a novel neural network architecture that combines hierarchy-aware attention masks with a parent-gated probability formulation to ensure hierarchy-consistent predictions. Hierarchy-level embeddings further support learning from sparse observations and patterns shared within each authorization level. We establish finite-sample risk bounds and provide sufficient conditions for consistent authorization probability estimation and algorithmic convergence. Experiments on simulated data, AI-generated user profiles, and real user authorization data demonstrate strong predictive performance with zero hierarchy violations.

</details>

## Machine learning theory

### [Instance-Dependent Bandit Convex Optimization in One Dimension](https://arxiv.org/abs/2611.31608)
*Felix Breuer, Alireza Bakhtiari, Kevin Jamieson* · `stat.ML` · arXiv:2611.31608v1 · relevance 0.32

- **In one sentence**: The paper studies instance-dependent sample complexity for one-dimensional stochastic bandit convex optimization in the fixed-confidence setting, showing a matching-rate result for minimizer localization but no comparable instance-dependent gain for simple regret.
- **In plain words**: The paper looks at how many noisy measurements are needed to find the lowest point of an unknown curve when each measurement is a costly test at a chosen spot. It asks whether the answer depends on how the specific curve is shaped, not just on worst-case bounds. The authors find that locating the minimizer can be done faster on easier curves, while merely finding a point that is nearly as good as the best one cannot be sped up in the same way.
- **Why it matters**: The result separates two goals that are often treated as one, which may matter for designing adaptive experiments and sequential testing. The text does not show broader impact beyond this one-dimensional theory, so its reach beyond that setting is unclear.
- **Background needed**: - Multi-armed bandit: choosing where to sample next and learning from noisy rewards.
- Fixed-confidence setting: the learner must stop with a guaranteed error level, and the goal is to minimize the number of samples used.
- Convex function: a bowl-shaped curve with a single lowest point, the minimizer.
- Sublevel set: the set of points where the curve lies below a given height.
- Instance-dependent vs. minimax: instance-dependent bounds depend on the specific problem; minimax bounds are worst-case over all problems in a class.
- Simple regret: how far the chosen point is from the best value.
- Sample complexity: the number of measurements needed. · level: research-level
- Matched keywords: sample complexity, minimax

<details><summary>Original abstract</summary>

We study the instance-dependent sample complexity of one-dimensional stochastic bandit convex optimization in the fixed-confidence setting. First, we consider minimizer localization, where the learner seeks to identify a point within distance $\varepsilon$ of the unique minimizer. We introduce a new instance-dependent quantity $\Delta_\varepsilon(f)$, corresponding to the threshold for which the sublevel set of $f-\min f$ has length $2\varepsilon$. We prove a lower bound of order $\Delta_\varepsilon(f)^{-2}$ and give a bisection-style algorithm that matches this rate up to logarithmic factors. We then revisit the simple-regret setting, where the goal is to identify an $\varepsilon$-optimal point. Surprisingly, no comparable instance-dependent improvement is possible: every correct algorithm has sample complexity of order $\varepsilon^{-2}$ on every instance, matching the minimax rate up to constants. Together, these results separate the statistical complexity of minimizer localization from that of simple-regret optimization in one-dimensional convex bandits.

</details>

### [PAC-style Bounds on the Conditional Validity of Conformal Predictors](https://arxiv.org/abs/2611.33023)
*Nicolo Colombo* · `cs.LG` · arXiv:2611.33023v1 · relevance 0.25

- **In one sentence**: The paper derives PAC-style probabilistic lower bounds on input-conditional coverage of conformal predictors, using Markov and Cantelli inequalities, and proposes conditional-coverage variance as an estimable measure of conditional validity.
- **In plain words**: Conformal prediction is a way to output a set of likely answers, rather than a single answer, with a promised long-run success rate. That promise holds on average across all inputs, but it can be off for particular kinds of inputs. This paper gives probability-based guarantees on how well the coverage holds for a given input, using only a finite amount of calibration data.
- **Why it matters**: Guarantees that hold for specific subgroups or individual inputs matter in settings such as medical or safety decisions, where average success can hide failures. The text suggests the variance of conditional coverage could serve as a practical check of this, but the abstract alone does not show how well this works in practice.
- **Background needed**: - Prediction sets: instead of one predicted value, a model returns a range or set of plausible outcomes.
- Coverage: the fraction of cases where the true outcome falls inside the set; the target here is 1 minus alpha (for example 90%).
- Marginal vs. conditional validity: marginal means the rate holds averaged over all inputs; conditional means it holds for each kind of input.
- Calibration data: a held-out sample used to set the size of the prediction sets.
- PAC-style bound: a guarantee of the form "with high probability, the true quantity is at least this large."
- Markov and Cantelli inequalities: standard probability tools that bound how far a random quantity can stray from its average, using only its mean (and variance for Cantelli).
- Hoeffding argument: a classic tool giving finite-sample confidence limits on an average. · level: research-level
- Matched keywords: conformal prediction

<details><summary>Original abstract</summary>

Conformal prediction sets are guaranteed to be marginally valid over the attribute space, but local coverage can diverge from the user-defined target $1-\alpha$. Constructing conditionally valid prediction sets with finite calibration data is impossible for a general data-generating distribution. We derive PAC-type probabilistic lower bounds on the input-conditional coverage of any conformal predictor, without assumptions on the data distribution. They are based on the Markov and Cantelli inequalities and adapt to both calibration-marginal and calibration-conditional setups. A tighter, model-dependent Cantelli bound depends on the variance of the conditional coverage and is estimable from data using a fully non-asymptotic Hoeffding argument. The results suggest conditional-coverage variance as a scalable and theoretically motivated empirical measure of conditional validity.

</details>

## Large language models

### [Implementation of Machine Translation for the Uzbek Language Based on Transformer Models](https://arxiv.org/abs/2611.32359)
*Mukhammadjon Musaev, Mannon Ochilov* · `cs.CL` · arXiv:2611.32359v1 · relevance 0.23

- **In one sentence**: The paper fine-tunes transformer models (T5 and mT5) on a roughly 3-million-pair Uzbek-English parallel corpus and evaluates translation quality with BLEU, claiming improvement over older methods.
- **In plain words**: This paper is about building an automatic translator between Uzbek, a language with relatively little digital text, and English. The authors gathered and cleaned up sentence pairs in both languages, expanded the collection, and then adjusted two existing AI language models to do the translation. They report that the result beats older translation approaches, measured by a standard scoring method.
- **Why it matters**: Low-resource languages are often poorly served by translation tools, so work that makes them better supported matters for the people who speak them. The text gives only a general claim of improvement and does not show detailed results, so how large the gain is and how well it holds up cannot be judged from this summary alone.
- **Background needed**: - Machine translation: software that converts text from one language to another automatically.
- Transformer models: the neural network design behind most modern AI language tools; T5 and mT5 are published transformer models, with mT5 trained on many languages at once.
- Fine-tuning: further training a pretrained model on a specific task or dataset to improve it there.
- Parallel corpus: a collection of sentences paired with their translations in another language, used as training material.
- Data augmentation: artificially expanding a dataset, for example by creating new variants of existing sentences.
- BLEU score: a common automatic metric that compares machine translations to human reference translations; higher is better, but it is an imperfect proxy for quality.
- Low-resource language: a language with little available digital text for training AI systems. · level: intermediate

<details><summary>Original abstract</summary>

This research focuses on building a machine translation system for the Uzbek language using transformer models such as T5 and mT5. Because of the limited data and the complexity of the Uzbek language, we collect, preprocess and augment data to create a strong Uzbek-English parallel corpus of about 3 million sentence pairs. The models are fine-tuned for optimal translation performance, and we use the BLEU score to evaluate the results. This study shows that our approach significantly improves upon older methods and helps promote the Uzbek language in the digital world.

</details>

### [Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models](https://arxiv.org/abs/2611.31821)
*Keyu He, Michael Li, Jiarui Liu et al.* · `cs.CL` · arXiv:2611.31821v1 · relevance 0.11

- **In one sentence**: The paper tests whether training small Qwen3 language models with supervised fine-tuning and reinforcement learning on objective game outcomes from three multi-player social games improves their social play, with some held-out-game transfer.
- **In plain words**: Researchers want AI models that can communicate and cooperate socially, but grading that behavior usually needs expensive AI judges that can be gamed. They used multi-player social games, where the rules themselves decide who wins, as a training ground. Small Qwen3 models trained this way won far more often against a much larger Gemma-3-27B model, and the gains partly carried over to games they had not been trained on.
- **Why it matters**: The approach offers a way to train social skills without relying on judge models that can be fooled, which matters for building agents that work with people or other agents. Whether these gains reflect general social intelligence, rather than skill at these specific games, is not settled by the text, and the held-out gain is smaller (39% to 54%) than the in-game gain.
- **Background needed**: - Large language model (LLM): a text-predicting AI system such as Qwen3 or Gemma-3.
- Supervised fine-tuning (SFT): further training a model on example responses that show the desired behavior.
- Reinforcement learning with verifiable rewards (RLVR): training where the model is rewarded by an objective, checkable result (here, the game's outcome) rather than a judge's opinion.
- Reward hacking: when a model finds a way to score well on the reward signal without actually doing the intended task.
- Win rate: the share of games won against an opponent; "pp" means percentage points.
- Held-out games: games not used during training, used to test whether skills transfer.
- Multi-player social games: games like hidden-role party games that require talking, coordinating and inferring others' hidden roles. · level: intermediate

<details><summary>Original abstract</summary>

The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acquire through supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). Results show that against a much stronger Gemma-3-27B model, SFT and RLVR raise the win rate of Qwen3-4B from 33% to 81% on the three trained games, and from 39% to 54% on three additional held-out games. In contrast, in-context strategies such as prompting improve the win rate of Qwen3-4B by only about 6 pp across the same games we train and evaluate on. Furthermore, we show that the gains from SFT and RLVR hold across the model sizes 1.7B, 4B, and 32B. Qualitative analyses of agent behavior show signs of stronger social intelligence; for example, trained agents tend to share information more openly, check each other's claims against public evidence, and coordinate their votes. More broadly, our results demonstrate that training LLMs on verifiable outcomes in social games can cultivate generalizable social behaviors, which offers a scalable path for building socially intelligent agents.

</details>

## Computer vision

### [Visual-State Graph Memory for Streaming Video Understanding](https://arxiv.org/abs/2611.32369)
*Ailar Mahdizadeh, Pritam Sarkar, Xiangteng He et al.* · `cs.CV` · arXiv:2611.32369v1 · relevance 0.14

- **In one sentence**: Proposes Visual-State Graph (VSG), a training-free memory for streaming video that stores objects, their relations, and an event log as a persistent, dynamically updated scene graph, and retrieves from it alongside recent frames under a fixed input budget.
- **In plain words**: Video models often need to answer questions about something that happened earlier in a long live video, but the important moment may have scrolled out of their short window of recent frames. This paper proposes a memory that keeps a running summary of the scene instead of every frame: each object gets one lasting entry with a dated history of how it changed, plus a log of events. When a question arrives, the system pulls out the relevant objects and events together with the latest frames.
- **Why it matters**: Streaming video applications such as monitoring or assistive devices need to recall the past without storing unlimited footage, so a compact memory of scene state is a practical design question. The text reports that, across four benchmarks and seven open-source vision-language models (7B to 32B parameters), VSG improved reasoning about the past under matched input budgets while keeping real-time operation; the size and consistency of these gains beyond the abstract are not described here.
- **Background needed**: - Vision-language model (VLM): an AI system that answers questions about images or video given as input.
- Streaming video: video that arrives continuously, so the model sees it frame by frame and cannot look ahead.
- Scene graph: a structured description of a scene as nodes (objects) connected by edges (relations such as "holding" or "next to").
- Training-free: the method is added on top of existing models without retraining them.
- Input budget: a fixed limit on how much information (e.g., number of frames or tokens) the model can take in at once.
- Retrieval: selecting only the stored items relevant to the current question. · level: intermediate

<details><summary>Original abstract</summary>

In streaming video understanding, the evidence needed to answer a question may have already left the recent-frame window. Keeping all frames does not scale with video length, while dropping older frames limits the model's ability to reason about the past. We propose Visual-State Graph (VSG), a training-free memory that stores the state of a stream rather than the raw sequence of frames. VSG represents the stream as a graph of objects and their relations, together with a log of events; similar to a dynamically evolving scene graph. An object observed repeatedly is represented by one persistent node, with a timestamped history of how its state changes. To determine whether a newly mentioned object already exists in the graph, we compare the relations it takes part in with those of stored objects. We build this memory as the video arrives, before the questions are known. When a question arrives, we retrieve relevant objects and events alongside recent frames under a fixed input budget. Our evaluation spans four streaming-video benchmarks and seven open-source vision-language models ranging from 7B to 32B parameters. Under matched input budgets, VSG improves reasoning about the past while preserving real-time understanding.

</details>

### [DOPER: Deep Object Pose Estimation Revisited](https://arxiv.org/abs/2611.32846)
*Hugo Hadfield, Alperen Degirmenci, Jonathan Tremblay* · `cs.CV` · arXiv:2611.32846v1 · relevance 0.14

- **In one sentence**: DOPER is an RGB-only framework that shares one visual backbone across detection, segmentation, and keypoint prediction to estimate 6D object poses via Perspective-n-Point, trained from synthetic data and adapted to real images with partial supervision and multi-view geometric constraints.
- **In plain words**: This paper is about working out where a known object is and how it is turned in 3D, using only ordinary color camera images. The method first learns from computer-generated images, then adapts to real photos, and it locates points on the object to compute its position and orientation. The authors report state-of-the-art detection scores on four benchmark datasets and real-time speed (about 35 times per second per object).
- **Why it matters**: Estimating object pose from a plain camera matters for robotics and spacecraft or warehouse tasks where depth sensors are not available. The text claims state-of-the-art detection accuracy and real-time speed, but the summary alone does not show how these compare to other methods in detail.
- **Background needed**: - Pose estimation: finding an object's 3D position and rotation (6D pose) relative to the camera.
- Keypoints and heatmaps: a few marked points on the object, and a map of how likely each point is to be at each pixel.
- Perspective-n-Point (PnP): a standard calculation that turns matched 2D image points and known 3D model points into a pose.
- Synthetic training: learning from computer-rendered images rather than real photos, then adapting to real ones.
- CAD model: a digital 3D design of the object.
- Multi-view and calibration: using several cameras whose positions are precisely known.
- Average precision (AP): a standard score for how well detections match the true objects. · level: research-level

<details><summary>Original abstract</summary>

We present DOPER, an RGB pose estimation framework that shares a visual backbone across object detection, segmentation, and keypoint prediction to recover the 6D pose of known objects through Perspective-n-Point. Starting from synthetic training, DOPER adapts to real observations using partial supervision while retaining synthetic keypoint labels. Calibrated multi-view observations provide geometric constraints for keypoint supervision. During inference, optional heatmap refinement fits a rigid pose directly to the predicted keypoint distributions, resolving ambiguous correspondences without depth input or a learned pose refiner. Starting from underspecified CAD models, DOPER progressively refines the object representation and pose estimator. Results on SPEED+ and SHIRT further demonstrate effective adaptation to illumination changes and accurate temporal pose estimation. Across the evaluated single-view and multi-view configurations, DOPER achieves state-of-the-art detection AP results on HANDAL, HOPEv2, HOT3D, and T-LESS while using only RGB and running in real time (35 Hz per object model on one GB300). These results demonstrate the effectiveness of jointly learning detection and pose keypoints, with real observations and geometric constraints.

</details>

## Reinforcement learning

### [To Critic Or Not To Critic](https://arxiv.org/abs/2611.32013)
*Jason Wei, George Pu, Jingxuan Fan et al.* · `cs.LG` · arXiv:2611.32013v1 · relevance 0.26

- **In one sentence**: An empirical study of when a learned critic (PPO) beats critic-free group-based advantage estimation (GRPO) in RL, framed as a bias-variance tradeoff in gradient direction across batch sizes, horizons, and domains including LLM tasks.
- **In plain words**: Training AI systems with trial-and-error rewards often uses one of two methods: one trains a helper "critic" that estimates how good each step is, and the other skips the helper and compares a group of attempts instead. This paper asks when the helper is worth its cost. Across more than 1,200 training runs, the authors find that the helper-based method tends to win when batches of training data are small, while the simpler group method catches up as batches grow, and needs bigger batches on longer, harder tasks.
- **Why it matters**: Many recent language-model training results compare these two methods without a clear rule for which to use, so a set of conditions for the choice is useful to practitioners. The text reports the trends but does not show how far they generalize beyond the tasks tested.
- **Background needed**: - Reinforcement learning (RL): training by rewards from trial and error.
- Policy gradient: the direction in which to nudge a model so it earns more reward.
- Critic / value function: a learned estimate of expected future reward, used to judge actions.
- Advantage: how much better an action was than expected.
- Bias vs. variance: a noisy estimate (high variance) versus one that is systematically off (bias). Critics reduce noise but can introduce bias when they are wrong.
- Bootstrapping: updating estimates using other estimates, which can propagate errors.
- Batch size: how many examples are used per update; larger batches give less noisy gradients.
- PPO and GRPO: two popular RL algorithms; GRPO scores each attempt relative to its group, with no critic. · level: research-level
- Matched keywords: reinforcement learning, policy gradient

<details><summary>Original abstract</summary>

As large language models tackle longer and more complex tasks, understanding when a critic improves the efficiency of reinforcement learning (RL) becomes increasingly important. Proximal Policy Optimization (PPO) trains a critic to reduce variance and provide fine-grained credit assignment, while Group Relative Policy Optimization (GRPO) drops the critic and avoids the bias of bootstrapping from the critic's value estimates. Although recent critic-based methods have reported strong performance relative to GRPO, it remains unclear when each approach is preferable. We argue that there is no universal answer; instead, the choice depends on several interacting factors, including batch size, critic reliance, and task complexity. We study the bias-variance tradeoff in terms of gradient direction, measuring how closely each method's gradient estimates align with the true policy gradient as batch size grows. Under a shared actor objective, we compare GRPO with PPO in control tasks, short-horizon math, and long-horizon terminal agents. Across more than 1,200 training runs, including 96 with LLMs, we find that PPO generally leads at small batch sizes, while GRPO often overtakes heavily bootstrapped PPO and reaches parity with lightly bootstrapped PPO at larger batches. At longer horizons and in more complex domains, GRPO needs larger batches to catch up to PPO's performance. Accounting for training compute, critics pay off at small budgets, but their returns diminish at larger budgets.

</details>

### [Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884)
*Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang et al.* · `cs.AI` · arXiv:2611.32884v1 · relevance 0.21

- **In one sentence**: The paper proposes RLVB, a reinforcement learning reward that uses the simulator's exact posterior over the answer to teach vision-language agents when to stop gathering evidence and commit, and introduces the Pro Worlds visual-puzzle benchmark.
- **In plain words**: AI agents solving multi-step tasks often give an answer too early, before they have seen enough evidence. The authors train agents with a reward that checks, during training only, whether the evidence so far already settles the answer, and rewards the agent for exploring when it does not and for answering when it does. They report gains over the base model on nine test settings, with some of the tests using tasks not seen in training.
- **Why it matters**: Premature guessing is a practical failure for agents that work through long tasks, and the paper's point that a final-answer-only reward cannot teach timing is a clear, testable claim. The approach's reliance on a simulator that can compute the exact answer probability during training limits where it applies, so its wider relevance is uncertain.
- **Background needed**: - Reinforcement learning: training by rewarding actions that lead to good outcomes.
- Reward signal: the score the agent gets; an end-of-episode reward only scores the final answer.
- Posterior: the probability distribution over possible answers given the evidence seen so far.
- Vision-language model: an AI model that takes both images and text as input.
- GRPO and PPO: two common reinforcement learning training algorithms; the paper compares against them.
- Process reward from an LLM judge: a score on intermediate steps given by another language model.
- GPU-hours: a measure of computing cost.
- Laziness here means committing to an answer before the evidence supports it. · level: research-level
- Matched keywords: reinforcement learning, reward model

<details><summary>Original abstract</summary>

AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scores only the final answer, so it cannot teach the agent when to commit, because a lucky guess receives the same reward as an answer backed by evidence. During training, however, the simulator can compute the exact posterior over the answer at every step and tell whether the evidence is already enough. We propose Reinforcement Learning with Verifiable Beliefs (RLVB), which rewards the agent for taking further steps while this posterior still allows several answers and for committing once the evidence is sufficient. The reward needs no judge, critic or reward model, and it never reads the belief line the agent writes before each action. We also introduce Pro Worlds, a benchmark of visual puzzles where the agent views a large world through a small window. We evaluate three vision-language models on three benchmarks, two of which are never seen in training. RLVB improves the base model in all nine settings, by 17.1% on average. Under the outcome reward, GRPO and PPO fall below the base model on average. RLVB also outperforms PPO with a process reward from an LLM judge by 9.3% on average while using 1.6 times fewer GPU-hours. The trained agent answers with sufficient evidence in 51%, 12% and 74% of the episodes on the three benchmarks, against 8%, 0.4% and 36% for the base model. Its accuracy gain therefore comes from answering more often at high levels of evidence. The belief line shows how the agent reaches this evidence: it acts on its own belief. It commits at only 0.1 to 2.2% of the turns at which the evidence is insufficient and its line still names several answers, against 3 to 68% for the base model.

</details>

## AI safety and alignment

### [SALSA: Sampling Adversarial Suffixes from Learned Distributions for LLM Safety Assessment](https://arxiv.org/abs/2611.33030)
*Shivank Rajput, Himanshu Singh, A. V. Subramanyam* · `cs.CL` · arXiv:2611.33030v1 · relevance 0.22

- **In one sentence**: SALSA trains a generative model on optimization-derived jailbreak suffixes so that new adversarial suffixes can be sampled quickly, and reports attack success comparable to GCG-style baselines on open models and higher transfer to GPT-3.5-Turbo and GPT-4o.
- **In plain words**: Chatbots are trained to refuse harmful requests, but attackers can add a string of odd words to a prompt that tricks them into complying. Finding such strings with current methods is slow, and strings that work on one model often fail on others. This paper describes SALSA, which learns the pattern of these strings from examples and then samples new ones quickly.
- **Why it matters**: It matters for AI safety because cheap, transferable attack generation is a way to test whether models are robust before release. The text reports speed gains and black-box success rates, but these are the authors' own results and have not been independently checked; the broader significance for safety evaluation is a reasonable reading rather than something the text establishes.
- **Background needed**: - Jailbreak attack: a prompt crafted to make an AI model ignore its safety training.
- Adversarial suffix: a string of text appended to a prompt to push the model toward a harmful reply.
- GCG-style attack: an optimization method that searches for effective suffixes, usually slow per prompt.
- Attack success rate (ASR): the share of attempts that get the model to comply with a harmful request.
- Transfer / black-box: attacks built on open models that are then tried on closed commercial models without access to their internals.
- Generative model / sampling: a model that learns a distribution over outputs and draws new samples from it. · level: research-level
- Matched keywords: alignment, jailbreak

<details><summary>Original abstract</summary>

Large language models (LLMs) remain vulnerable to jailbreak attacks, where adversaries append optimized suffixes to otherwise benign looking prompts to bypass safety alignment. Existing optimization-based GCG-style attacks can be effective, but they are expensive at inference time, and suffer from poor transfer. We present, SALSA, a generative framework that learns a distribution over jailbreak suffixes from optimization-derived attack corpora. Once trained, the model supports efficient sampling-based attacks. On open-source targets, it achieves attack success rates comparable to state-of-the-art optimization baselines, while reducing generation time from 3.46s to 0.04s per prompt. In black-box transfer, it remains highly effective against proprietary systems, including 99% ASR on GPT-3.5-Turbo, and reaches 45% ASR on the substantially harder GPT-4o, more than doubling the strongest baseline at an equal sampling budget. We further offer an intuition for why generative sampling can preserve high attack success, when the learned suffix distribution is close to the distribution of optimization outputs. Overall, our results show that learning adversarial suffix distributions yields a scalable, and practically efficient foundation for continuous LLM vulnerability discovery.

</details>

### [Monitorable-by-design architectures for a post-Astra world: a compartmentalization-based approach](https://arxiv.org/abs/2611.31610)
*Jake Watts, Joel Sokol* · `cs.AI` · arXiv:2611.31610v1 · relevance 0.21

- **In one sentence**: A proposal for language model architectures that compartmentalize dangerous capabilities so their use can be monitored more cheaply than reading chain-of-thought, building on methods such as GRAM, SGTM, DEMix and BTS.
- **In plain words**: The paper addresses a worry that AI systems may increasingly reason in ways humans cannot read, so watching their written reasoning ("chain of thought") may stop working. Its authors propose changing how models are built, so that risky abilities sit in separate, identifiable parts of the network that can be checked more cheaply. They describe several versions of this design meant to trade off different costs, and mention extra benefits such as the possibility of removing a capability. The text does not report experimental results.
- **Why it matters**: If reading an AI's reasoning stops being a reliable safety check, designs that make dangerous abilities easier to watch could matter for oversight. The text is a proposal without shown results, so its practical value is unconfirmed, and it is unclear how well these methods would work at scale.
- **Background needed**: - Chain of thought: the step-by-step reasoning a language model writes out, which overseers can read to spot problems.
- Monitorability: how easily humans or automated tools can check what an AI is doing and why.
- Compartmentalization: keeping certain capabilities in separate parts of a model, so they can be isolated and inspected.
- Asynchronous monitoring: checking a system's activity after the fact or in batches, rather than in real time, to save cost.
- The named methods (GRAM, SGTM, DEMix, BTS) are prior techniques for training models with separable parts; this paper builds on them, and the text does not explain them in detail.
- "GPT-6 Astra" is a model name used in the text; the text gives no further details about it. · level: research-level
- Matched keywords: dangerous capabilities

<details><summary>Original abstract</summary>

Frontier models like GPT-6 Astra are increasingly able to do substantial reasoning without a monitorable chain of thought, chains of thought are becoming less legible, and are often monitored asynchronously to reduce cost. With the future of chain of thought monitoring unclear, it may be necessary to design LLMs with monitorability in mind. We propose a modification to existing LLM architectures based on GRAM, SGTM, DEMix, BTS, and similar methods to compartmentalize dangerous capabilities so that their use, especially in combination with dangerous reasoning types that may indicate strategic adversarial use, can be monitored more cheaply than chain of thought in a way that might outlast monitorable chain of thought. We propose several variants of this architecture designed to balance tradeoffs and discuss other benefits, such as capability removal.

</details>

## Interpretability

### [Social Bias Neurons in Multilingual Language Models: A Mechanistic Interpretability Analysis](https://arxiv.org/abs/2611.32685)
*Lance Calvin Lim Gamboa, Yue Feng, Mark Lee* · `cs.CL` · arXiv:2611.32685v1 · relevance 0.27

- **In one sentence**: This paper applies mechanistic interpretability methods to locate "social bias neurons" in three instruction-tuned multilingual language models across four languages and seven bias dimensions, comparing two identification methods.
- **In plain words**: AI language models can reflect social stereotypes, and this paper looks for the specific internal units inside these models that carry that bias. The authors tested two ways of finding such units across several languages and kinds of stereotypes. They report that one method, integrated gap gradients, found units whose suppression reduced bias more sharply, and that these units sit mostly in the model's deepest layers.
- **Why it matters**: Being able to point to the parts of a model that carry bias could support targeted fixes instead of retraining everything. The paper also reports that bias patterns differ between high- and low-resource languages and overlap most for gender, nationality, and social class, though the text gives no evidence on how far these findings generalize beyond the models tested.
- **Background needed**: - Language models are AI systems trained on large amounts of text to predict and generate language.
- "Neurons" here means individual numerical units inside the network whose activation levels can be measured.
- Mechanistic interpretability is the effort to understand which internal parts of a model do which jobs.
- Instruction-tuned models are models further trained to follow user instructions.
- Multilingual means the model handles many languages; high-resource languages have far more training text than low-resource ones.
- Activation probability entropy and integrated gap gradients are two scoring methods for ranking how strongly a neuron relates to bias; the text does not describe their details.
- Suppressing a neuron means switching off or dampening its output to test whether bias drops. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Multilingual models exhibit social bias when processing inputs pertaining to societal stereotypes. We adapt emerging mechanistic interpretability methods to pinpoint and characterize model components that encode this bias. We conduct our analysis across three instruction-tuned models, four languages, and seven bias dimensions. Specifically, we leverage multilingual bias benchmarks in implementing two methods for identifying social bias neurons: activation probability entropy and integrated gap gradients. We find the latter method to be more effective, as the neurons it isolates (which are largely concentrated at the model's deepest layers) lead to sharper decreases in model bias when suppressed. Further analysis reveals neuron distribution patterns differ between high- and low-resourced languages, suggesting that a language's representation in pretraining data influences how its biases are represented within model internals. Our results also indicate that neurons linked to gender, nationality, and social class biases overlap the most with neurons related to other bias dimensions, pointing to the pivotal role these three dimensions play in how models learn and handle bias.

</details>

### [Capability and Interpretability of Transformers on Multi-task Recurrence](https://arxiv.org/abs/2611.31260)
*Xiamin Chen, Linyu Liu, Jiachen Hu et al.* · `cs.CL` · arXiv:2611.31260v1 · relevance 0.24

- **In one sentence**: A controlled study of how Transformers learn, identify, and switch between linear recurrence rules over finite cyclic groups, probed with linear probes and input patching.
- **In plain words**: This paper asks how Transformer neural networks, the kind behind many language AI systems, handle rules that repeat in a sequence. The authors built a set of simple, controlled puzzles where each output depends on earlier items through a fixed arithmetic rule. They then tested which rule-handling tasks the models could learn and what internal representations they used.
- **Why it matters**: Language often follows recurring structures, so understanding how a model represents and switches between rules may help explain its behavior, though the text does not show how far these toy results carry over to real language. The work uses standard interpretability tools, which makes its findings checkable in principle.
- **Background needed**: - Transformer: the neural network architecture used in most modern language models.
- Linear recurrence: a sequence where each new value is a fixed combination of earlier values, like a rule applied step by step.
- Finite cyclic group: a set of numbers that wraps around (like clock arithmetic), used here as a clean testbed.
- Latent rule: a rule that is not stated explicitly and must be inferred from context.
- Input masking: hiding some of the input during training or testing.
- Mechanistic interpretability: reverse-engineering what a network computes internally.
- Linear probing: training a simple classifier on internal activations to test what information they contain.
- Input patching: swapping internal activations between runs to see which parts causally affect the output.
- Curriculum training: teaching the model easier examples or tasks first, then harder ones. · level: research-level
- Matched keywords: interpretability, mechanistic interpretability

<details><summary>Original abstract</summary>

Transformers are widely used in various language tasks, with limited understanding of their internal mechanisms. Motivated by the recurrent structure of many linguistic rules, we study the capability and interpretability of Transformers through a controlled family of linear recurrence tasks over finite cyclic groups. These tasks range from executing a single fixed rule to identifying a latent rule from context and switching between explicitly specified rules, with and without input masking. Through extensive experiments across different configurations, we find that switching specified rules is simpler than identifying latent rules for Transformers in general. We also identify how several key factors affect the generalization capability of Transformers, including the depth, width, and the algebraic structure of the linear recurrence. Curriculum training is extremely useful when the number of rules is large. With standard tools in mechanistic interpretability like linear probing and input patching, our study reveals how Transformers represent, identify, and execute multiple rules.

</details>

## AI for mathematics

### [Safe Autoformalization: Sufficiency and Necessity with Entailment Graphs](https://arxiv.org/abs/2611.31571)
*Umut A. Acar, Eli Goldweber* · `cs.AI` · arXiv:2611.31571v1 · relevance 0.26

- **In one sentence**: The paper proposes a graph-based method for autoformalization (turning natural-language statements into logic formulas) that uses LLM-generated candidate formulas, solver-checked entailment orderings, and LLM entailment oracles to certify one-sided logical adequacy, with soundness and completeness results and a Lean machine-checked proof.
- **In plain words**: The paper is about turning ordinary English statements, such as security requirements, into precise logical formulas that a computer can check. Language models produce such formulas, but with no guarantee they match what the statement means. The authors arrange candidate formulas in a graph ordered by how strong they are, and use checks to find formulas that safely bound the intended meaning from above and below.
- **Why it matters**: Formal checking is only as trustworthy as the translation it starts from, so a method that certifies when a translation is safe to rely on matters for AI-assisted verification. The text reports a small expert-adjudicated study on AWS security properties, where the graph method was safe in all 20 cases while two baselines were unsafe in 25% and 10%; the scale of that study is small, so the broader applicability is not established by the text.
- **Background needed**: - Autoformalization: translating natural-language statements into formal logic.
- Entailment: statement A entails B if whenever A holds, B must also hold.
- Sufficient vs. necessary formula: a sufficient formula implies the intended meaning (safe to enforce); a necessary formula is implied by it (safe to rely on).
- Entailment graph: nodes are candidate formulas, edges record logical strength; a solver (automated logic checker) decides the ordering.
- Residual and co-residual: the two adjoint operations of an ordering, used here to define the local checks.
- Sound vs. complete oracle: sound accepts only true entailments; complete accepts all true entailments.
- Lean: a proof assistant used to machine-check the mathematical proofs.
- AWS: Amazon Web Services; the security properties tested come from its setting. · level: research-level
- Matched keywords: Lean, autoformalization

<details><summary>Original abstract</summary>

Autoformalization translates a natural-language statement into a formula that captures its intent, which depends on the statement's context: the background that disambiguates it. LLMs make autoformalization practical, but their probabilistic output carries no formal guarantees. We propose techniques for safe autoformalization that certify one-sided logical adequacy: a formula sufficient for the intent is safe to enforce, and a formula necessary for it is safe to rely on. We use LLMs to generate candidate formulas and order them by logical strength in an Entailment Graph (EG), an ordering a solver decides. Each edge carries a residual and a co-residual, the two adjoints of the entailment order, all fixed by the candidate pool alone. In a context, two searches return the sufficient frontier, the weakest candidates that entail the statement, and the necessary frontier, the strongest candidates the statement entails; each step is one local check against an edge's residual or co-residual. The frontiers bracket the statement and yield the ambiguity residue, which holds exactly of the situations the candidates certify neither as satisfying nor as violating it; the statement is ambiguous precisely when the residue is satisfiable. For natural-language statements and contexts, an LLM entailment oracle decides the checks; it is sound if it accepts only checks that hold, and complete if it accepts every check that holds. We prove that a sound oracle makes the search safe regardless of pool quality, and that a complete one makes the frontiers tight. On security-critical AWS properties, EGs are safe in all 20 cases of an expert-adjudicated study, where majority vote over equivalence clusters and Universal Self-Consistency are unsafe in 25% and 10%. An ablation with the same oracle but no graph is unsafe in 25% and rejects every candidate in another 30%. We machine-checked our proofs in Lean.

</details>

### [How Far Apart Are Two Proofs? Measuring Proof Dissimilarity in a Proof Kernel and in Lean/Mathlib](https://arxiv.org/abs/2611.31811)
*Nikolaos Nikolaou* · `cs.LO` · arXiv:2611.31811v1 · relevance 0.25

- **In one sentence**: The paper defines 19 measures of how different two formal proofs of the same theorem are, groups them into six families, and tests them on machine-checked proofs in a Curry-Howard kernel and in Lean 4/Mathlib.
- **In plain words**: As AI systems produce more mathematical proofs than people can read, the authors ask how to tell whether a proof is genuinely new or just a rewrite of an existing one. They define a set of ways to measure how far apart two proofs are, and test them on several computer-checked proofs that there are infinitely many primes. Their findings include that measures based on which earlier results a proof relies on tend to match intuition, while measures based on meaning can rank proofs in surprising ways.
- **Why it matters**: Checking whether AI-generated proofs are duplicates or truly new ideas is a practical problem as machine-generated mathematics grows, and the paper ties this to Hilbert's 24th problem on the theory of proofs. The text reports small test sets (5 proofs in one kernel, 3 theorems and 19 proofs in Lean), so the measures are better seen as a starting framework than as settled tools.
- **Background needed**: - A proof is a step-by-step argument that a statement is true; in formal systems such as Lean, each step is checked by a computer.
- Curry-Howard correspondence: a view in which proofs are treated as programs, which lets proof-checking systems be studied as type-theory kernels.
- Lean 4 and Mathlib: a proof assistant and its large community library of formalised mathematics.
- "Proof irrelevance": the idea that all proofs of the same statement count as equal in some logical systems.
- Dissimilarity measure: a number saying how far apart two objects are; here, how different two proofs are, measured at several levels (text, structure, dependencies, meaning, information content).
- The infinitude of primes: a classical result, proved by Euclid, with later proofs such as Goldbach's and Furstenberg's topological one. · level: research-level
- Matched keywords: Lean, mathlib

<details><summary>Original abstract</summary>

We now live in the age of machine-generated mathematics: AI systems produce research-level proofs faster than the human mathematical community can read them. Verification is only part of the challenge. We also need to know whether a "new proof" is indeed new, whether a thousand generated proofs contain one idea or many, and where each sits relative to human mathematics. All of these require measuring distances between proofs. Following Hilbert's 24th problem and the identity-of-proofs problem, we ask how far apart two proofs of one theorem are, and what shape the proof space they inhabit has. We define 19 dissimilarity measures in 6 families (syntactic, structural, dependency & resource, semantic, information-theoretic, higher-categorical) and 10 desirable properties, which we argue are the conditions for safely optimising a measure. In a Curry-Howard kernel, 5 machine-checked proofs that the primes are infinite show that raw syntax cannot tell a rewrite from a new argument, that dependency-based and structural measures reproduce the intuitive ordering (Euclid rewritten < Goldbach < Furstenberg), and that semantic measures invert it: Furstenberg's topological proof produces exactly Euclid's witness. A replication in Lean 4/Mathlib (3 theorems, 19 proofs, 18 measures) confirms that dependency-closure measures track intuition best, and shows that equality of normal forms never holds between differently written versions of the same argument, that proofs by citation look unlike the arguments they cite, and that proof irrelevance cannot distinguish any two proofs. We argue for reporting dissimilarity as a multi-level profile, extend the measures to proofs of different theorems, and discuss uses, from detecting duplicated AI proofs and orchestrating prover agents to interpreting AI proofs via their nearest human-understandable counterparts. Code, Lean sources and data are released.

</details>

## Robotics and embodied AI

### [PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents](https://arxiv.org/abs/2611.33144)
*Feixiang Ruan, Guodong Lv, Kewei Zhang et al.* · `cs.RO` · arXiv:2611.33144v1 · relevance 0.20

- **In one sentence**: PyRUA-Dex uses coding agents to write programmatic robot policies for bimanual dexterous manipulation without human demonstrations, evaluated on Bench2Dex and DexJoCo benchmarks and on a real two-hand robot.
- **In plain words**: Teaching robot hands to do fine tasks usually needs many examples from humans, and those examples are hard to collect well. This paper has AI coding agents write the robot's control program instead: several agents try out skills in parallel, a summarizing agent keeps the successful ones as a reusable library and one program, and that program is then refined on randomized setups. The authors report strong scores in simulation and real-world demos on a robot with two 22-joint hands, including playing piano and writing calligraphy.
- **Why it matters**: It offers an alternative to collecting human demonstrations, which the authors say is the main bottleneck for dexterous robots. Whether this approach generalizes beyond the tasks shown is not established by the text, so its wider significance is still uncertain.
- **Background needed**: - Dexterous manipulation: using multi-fingered robot hands for fine, precise object handling.
- Bimanual: using two hands or arms together.
- Degrees of freedom (DoF): independent joints or movement directions; 22-DoF hands are highly articulated.
- Demonstrations and retargeting: learning from recorded human examples, including mapping human hand motion onto a robot hand.
- Programmatic policy: a robot controller written as readable code rather than a neural network.
- Coding agents: AI systems that write and run software to solve a task.
- Simulation benchmarks: standardized virtual test suites (Bench2Dex, DexJoCo) used to compare methods; scores are as reported by the authors.
- Domain randomization: varying object positions and conditions during training so the controller is robust. · level: research-level

<details><summary>Original abstract</summary>

Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explore in parallel for task skills and ways to compose them, and a distilling agent condenses the successful attempts into a task library and one program. During refinement, this program is improved through randomized layouts for enhanced robustness and execution efficiency. In simulated environments, PyRUA-Dex achieves SOTA on Bench2Dex with a score of 72.9 and reaches 81.0% success on DexJoCo under full randomization, ahead of every trained policy on both benchmarks. In real world experiments on a bimanual platform with two 22-DoF hands, PyRUA-Dex learns to play piano, write calligraphy, and other tasks efficiently: learning a new piece from sheet music takes as little as 30 minutes. These results suggest that PyRUA-Dex is an effective framework for developing dexterous manipulation policies with coding agents in the absence of high quality dexterous manipulation demonstrations.

</details>

### [Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations](https://arxiv.org/abs/2611.32101)
*Ange Bao, Haishan Zhang, Lingzi Xie et al.* · `cs.RO` · arXiv:2611.32101v1 · relevance 0.17

- **In one sentence**: Ego2Real transfers bimanual dexterous manipulation from egocentric human videos paired with tactile gloves to anthropomorphic robot hands, using tactile signals both to refine hand-object reconstructions and to define contact rewards for reinforcement learning.
- **In plain words**: Teaching robot hands to handle objects by watching people is cheaper than programming them by hand, but video alone misses how hard a person is pressing and where contact happens. This paper adds touch sensors worn as gloves on the demonstrator, and uses that touch data in two places: to correct the estimated hand poses from video, and to reward a robot's training when its contacts match the human's. The paper reports that adding touch data to both steps yields higher task success rates.
- **Why it matters**: Robots that learn from human demonstration need better data about physical contact, which is the hard part of dexterous work. The approach may matter for scaling robot skill learning, but the text gives no details on the size of the gains, the tasks, or how it compares with other methods, so its wider significance is uncertain.
- **Background needed**: - Egocentric demonstration: video recorded from the person's own head or chest camera, showing their hands doing a task.
- Bimanual dexterous manipulation: using two multi-fingered hands together to handle objects.
- Tactile sensing: measuring touch and pressure, here through sensor gloves.
- Hand-object reconstruction: estimating the 3D positions of a hand and an object from images.
- Reinforcement learning: a robot learns by trial and error, guided by a reward signal.
- Contact reward: a bonus given when the robot's fingertips touch an object as the human's did.
- Anthropomorphic hand: a robot hand shaped roughly like a human hand, with a different body and motors than a person's. · level: research-level

<details><summary>Original abstract</summary>

Learning dexterous manipulation from egocentric human demonstrations offers a scalable path toward robot skill acquisition. Vision alone, however, provides limited information about physical contacts and the demonstrator's force intent, leading to ambiguities in interpreting hand-object interactions. Capturing human touch via tactile sensing is therefore crucial for reliable human-to-robot dexterous skill transfer. We present Ego2Real, a framework that leverages egocentric demonstrations and tactile gloves to transfer bimanual dexterous manipulation skills to robotic hands. Ego2Real incorporates tactile supervision at two complementary stages: (1) tactile-guided hand-object interaction reconstruction, which uses measured tactile signals to refine hand poses and contact geometry; and (2) contact-informed reinforcement learning, which translates human contact patterns into robotic contact rewards. By combining refined motion references with physical contact rewards during training, Ego2Real guides anthropomorphic robotic hands to emulate demonstrated contact behaviors while adapting to their own morphology and actuation. Experiments show that incorporating tactile supervision into both reconstruction and policy learning yields higher manipulation success rates, underscoring the importance of enriching egocentric demonstrations with tactile observations to improve their quality and transferability.

</details>

## Security and cryptography

### [Trustworthy Edge AI: Security, Privacy, and Resilience for Distributed Intelligence](https://arxiv.org/abs/2611.31331)
*Jaydip Sen, Subhasis Dasgupta* · `cs.CR` · arXiv:2611.31331v1 · relevance 0.11

- **In one sentence**: A book chapter surveying security, privacy, and resilience mechanisms for Edge AI systems, with a call for cross-layer design, drawing on case studies from smart cities, autonomous vehicles, healthcare, and industrial IoT.
- **In plain words**: This is an overview chapter about keeping AI running on local devices (such as sensors, cars, and hospital equipment) rather than in distant data centers. It explains the ways such systems can be attacked or fail, and reviews protective methods like trusted hardware, checking device identity, and training AI on shared data without pooling the raw data in one place. The text is a survey and argument rather than a report of new experimental results.
- **Why it matters**: Edge AI is spreading into cities, vehicles, and healthcare, so how these systems protect data and keep working under attack matters to many fields. The text itself gives no measured findings, so it is best read as a guide to open questions and trade-offs rather than evidence for any specific method.
- **Background needed**: - Edge AI: running AI models on or near the device that collects the data, instead of only in the cloud.
- Attack surface: the number of points where an attacker could get in; more varied devices means more of these points.
- Zero-trust: a model where no device or connection is trusted by default and each must be verified.
- Attestation: a device proving to others that its software is genuine and unaltered.
- Federated learning: several devices improve a shared model by sending back model updates instead of their raw data.
- Differential privacy: adding controlled noise so that results reveal little about any single person's data.
- Adversarial robustness: how well a model resists inputs deliberately crafted to fool it. · level: intermediate

<details><summary>Original abstract</summary>

This chapter examines the principles and emerging research directions for building secure, privacy-preserving, and resilient Edge Artificial Intelligence (Edge AI) systems. As intelligence shifts from centralized clouds to distributed edge environments, challenges arise in ensuring data integrity, privacy, and reliable operation under adversarial and uncertain conditions. The chapter analyzes Edge AI architectures, emphasizing the expanded attack surface due to heterogeneous devices, resource constraints, and dynamic networks. It reviews core security mechanisms, including hardware-rooted trust, zero-trust models, secure communication, and attestation. Privacy-preserving approaches, such as federated learning, secure aggregation, and differential privacy, enable collaborative intelligence without centralized data sharing. Resilience strategies, including fault tolerance, adversarial robustness, and adaptive orchestration, are also explored. Case studies from smart cities, autonomous vehicles, healthcare, and industrial IoT illustrate practical trade-offs. The chapter advocates a holistic, cross-layer design integrating security, privacy, and resilience for trustworthy edge intelligence.

</details>

### [Your bids are showing: re-identifying power plants in anonymized market data, and a differentially private alternative](https://arxiv.org/abs/2611.31681)
*Nikhil Ravi* · `eess.SY` · arXiv:2611.31681v1 · relevance 0.07

- **In one sentence**: The paper shows that PJM-style masking of power-plant offer curves in anonymized electricity market data can be undone by matching against public plant data, and proposes a differentially private monthly aggregate release with stated accuracy trade-offs.
- **In plain words**: Electricity markets publish how much each power plant is willing to sell at each price, so analysts can study prices and spot possible manipulation. Some grid operators hide plant names with codes, assuming this keeps the offers private. Using Texas (ERCOT) data where the names are public as a test, the authors found that public fuel and emissions records could still match many coded units back to their plants.
- **Why it matters**: It matters for how grid regulators and market monitors decide what data to publish and how much privacy they can actually promise. The paper also offers a noisy aggregate release that keeps the main market measures usable, though its results come from one market and its own simulations, and the claim that PJM's feed would fail the same way is an expectation rather than a tested result.
- **Background needed**: - Offer curve: a plant's stated willingness to sell power at each price level, by hour.
- Merit order: ranking plants from cheapest to most expensive offer to build the market supply curve.
- Clearing price: the price where supply meets demand in the market.
- Masking/anonymization: replacing names with codes; the paper tests whether this hides identity.
- Re-identification: linking anonymous records back to real plants using other public data.
- Differential privacy: a guarantee that the published output barely changes whether any one unit's data is included; adds calibrated random noise. Zero-concentrated differential privacy (zCDP) is one formal way to measure this, and epsilon (ε) sets the strength (smaller is stronger).
- Fuel group: a category such as gas, coal, wind or hydro.
- Combined-cycle: a type of gas plant. · level: research-level

<details><summary>Original abstract</summary>

ERCOT publishes every generator's hourly offer curve 60 days after the operating day. Market monitors, researchers and traders use these records to study the merit order and check for withholding. PJM publishes the same kind of data with unit names replaced by codes, on the view that masking keeps offers confidential. We test that view on ERCOT data from 2024 to 2026, where names are public and so provide ground truth, by masking the records under PJM's published rules. Public EIA and EPA data match 25% of the masked units we can score (32% of their capacity) to their plant, and 45% fall within the top five guesses. PJM's feed carries the same fields, so we expect masking to fail there too. Publishing exact fuel-group totals instead does not help. An attacker who knows the other units in a group recovers one unit's high-price offers exactly, and an outsider who knows only the target's outage dates reaches a correlation of 0.77, most of it from a few renewable and hydro units that offer at very high prices (0.32 over fossil units). We propose a differentially private release: monthly totals by fuel group and price bin, with Gaussian noise calibrated under zero-concentrated differential privacy so that each unit's whole year of offers is protected. It publishes an unbiased noisy layer and derives a monotone supply curve and shares from it at no extra privacy cost. At $\varepsilon=10$ per unit-year the market supply curve stays within 11% of the truth, the implied clearing price within \$3.0/MWh, and the attacker's correlation falls to 0.23. Whether an analysis still works depends on one ratio, how much the true quantity varies month to month against the noise, which predicts the accuracy of totals to within 0.05. The clearing price, supply slope and combined-cycle capacity remain usable, but no monthly release, private or exact, can answer questions about single hours or single units.

</details>

## Algorithms and complexity

### [Improved Lower Bounds for Online Parallel Machine Scheduling](https://arxiv.org/abs/2611.32565)
*Junwen Xiao, Zhiyi Tan* · `cs.DS` · arXiv:2611.32565v1 · relevance 0.24

- **In one sentence**: The paper proves improved lower bounds on the competitive ratio of online algorithms for makespan minimization on parallel identical machines, using a bin-packing-based estimate of the optimum and a direct construction for five machines.
- **In plain words**: This paper studies a scheduling problem: jobs arrive one at a time and must be assigned to one of several identical machines without knowing what jobs come later, with the goal of finishing all work as early as possible. The authors show that no method for doing this can do better than a certain worst-case factor, 1.887111 times the best possible finish time in general. For the special case of five machines, they give a separate, smaller bound of 1.74916.
- **Why it matters**: Lower bounds say how well any online method could ever perform, so raising them narrows the gap between what is known to be achievable and what is known to be impossible. The text says the new bounds beat results that are about two decades old, but it does not compare them to the best upper bounds, so the size of the remaining gap is not stated here.
- **Background needed**: - Makespan: the finish time of the last job; the goal is to minimize it.
- Parallel identical machines: several machines that run jobs at the same speed.
- Online algorithm: it must decide on each job immediately, without seeing future jobs.
- Competitive ratio: the worst-case ratio between an online method's makespan and the best offline (all-knowing) makespan.
- Lower bound: a proof that no algorithm can achieve a ratio below a given value.
- Bin packing: packing items into fixed-size bins with as few bins as possible; used here to estimate the optimal makespan. · level: research-level

<details><summary>Original abstract</summary>

This paper establishes new lower bounds for online parallel machine scheduling aimed at minimizing the makespan. By leveraging bin packing algorithms to estimate the optimal makespan, we prove that the competitive ratio of any online algorithm is at least 1.887111. Additionally, via a direct construction, we demonstrate a lower bound of 1.74916 for the case of five machines. Our results improve upon the best known lower bounds established two decades ago.

</details>

### [Better-than-3 Approximation for 2ECSS Using the Primal-Dual Method](https://arxiv.org/abs/2611.32924)
*Ana Cezara Danciu, Sharat Ibrahimpur* · `cs.DS` · arXiv:2611.32924v1 · relevance 0.14

- **In one sentence**: This paper gives a single-phase primal-dual algorithm for the 2-edge-connected spanning subgraph problem with approximation ratio sqrt(3)+1 (about 2.74), improving on the previous best primal-dual ratio of 3, measured against the natural linear relaxation.
- **In plain words**: The paper studies how to build the cheapest network in which every link can fail without cutting off any city from the rest, where links have costs. The authors give a method that finds such a network whose cost is guaranteed to be within about 2.74 times the best possible, improving the previous guarantee of 3 for this style of method. The method works by gradually raising "prices" on groups of nodes and buying links once their prices become fully paid, then discarding unneeded links.
- **Why it matters**: Approximation ratios for a classic network design problem are a measure of how close a fast algorithm can get to the true optimum, and this paper narrows the gap for one specific technique. The text does not say how it compares to the other known 2-approximation methods, so its wider practical or theoretical reach is unclear.
- **Background needed**: - Graph: nodes joined by edges (links); a multigraph allows parallel edges.
- 2-edge-connected: removing any single edge leaves the graph connected.
- Approximation ratio: worst-case factor by which an algorithm's cost can exceed the optimal cost.
- Linear relaxation: a continuous version of the problem, used as a lower bound on the optimum.
- Primal-dual method: an algorithm design approach that grows dual "prices" on sets of nodes and buys edges when their dual constraints become tight.
- Cut: a split of the nodes into two sides; every cut must be crossed by enough chosen edges.
- Contraction: merging a group of nodes into one node to simplify the graph. · level: research-level

<details><summary>Original abstract</summary>

In the $2$-edge-connected spanning subgraph problem (2ECSS), we are given an undirected multigraph whose edges have nonnegative costs, and the goal is to find a $2$-edge-connected spanning subgraph with minimum total cost. Two distinct approaches yield $2$-approximation algorithms: a reduction to the minimum-cost rooted $2$-arborescence problem and iterative rounding. Despite significant efforts, the best known approximation ratio using the primal-dual method has remained at $3$. Our main result in this work is a primal-dual algorithm for 2ECSS that achieves an approximation ratio of $\sqrt{3}+1 (\leq 2.74)$. The algorithm runs in a single phase and the approximation guarantee is relative to the natural linear relaxation, which requires the sum of the edge variables across every cut to be at least $2$. The algorithm follows the standard template of growing dual variables corresponding to minimal violated sets, albeit at non-uniform rates, until the dual constraint for an edge becomes tight, at which point the edge is temporarily purchased. Once feasibility is attained, redundant edges are dropped in the reverse order in which they were purchased. Our choice of dual growth rates is inspired by the single-phase $3$-approximation algorithm of Beyer, Chimani, and Spoerhase (COCOON 2020). As in their work, our algorithm maintains a forest of purchased edges by repeatedly contracting $2$-edge-connected subgraphs, and dual variables corresponding to leaves and isolated vertices of this forest are grown at a rate of $1$. Our main modification is to additionally grow dual variables corresponding to nontrivial connected components at rate $(\sqrt{3}-1)/2 \approx 0.37$, when the forest is disconnected.

</details>

## Programming languages and formal methods

### [Verifying Type Soundness for Nontransitive Information Flow Security](https://arxiv.org/abs/2611.32123)
*Chenyi Zhang* · `cs.PL` · arXiv:2611.32123v1 · relevance 0.15

- **In one sentence**: A machine-checked (Dafny) soundness proof for a type system enforcing nontransitive noninterference, an information flow security property, extended to an imperative language.
- **In plain words**: This paper is about checking that a set of rules for keeping secret information from leaking through a program is itself correct. The authors used a proof assistant-style tool, Dafny, to mechanically verify that the rule system guarantees its security property, rather than relying on paper arguments alone. The text presents this as the first such machine-checked proof for this kind of type-enforced security property.
- **Why it matters**: Software that claims to keep data private is only as trustworthy as the rules checking it, so formally verifying those rules gives stronger assurance. The text's main claim is the absence of prior machine-checked proofs for this property, and it does not report wider applications or measured effects beyond that.
- **Background needed**: - Information flow security: tracking whether secret data can influence publicly visible outputs.
- Noninterference: the property that high-security inputs have no observable effect on low-security outputs.
- Nontransitive policies: security rules where information may flow from A to B and from B to C without permitting a flow from A to C.
- Type system: a set of static rules that classify program parts and reject insecure ones before the program runs.
- Imperative language: a programming style built on sequences of statements that change memory.
- Machine-checked proof: a proof whose every step is verified by software, reducing reliance on human error.
- Dafny: a programming language and verifier used to write and automatically check formal proofs. · level: research-level

<details><summary>Original abstract</summary>

We present a machine-checked soundness proof of a type system for the nontransitive noninterference (NTNI) information flow security property in an imperative programming language using Dafny. The original formulation of NTNI was developed for a functional programming language augmented with memory access operators, where security policies are expressed as coarse-grained information flow constraints over component-based software systems. Although subsequent research has extended NTNI type systems in various directions, to the best of our knowledge, no prior work has established a machine-checked soundness proof for type-enforced NTNI. As a result, the correctness of existing NTNI enforcement mechanisms has not been formally verified with a high degree of assurance.

</details>

### [Denotational Results in Compiler Correctness and Comparisons with Operational Approaches](https://arxiv.org/abs/2611.31724)
*Jeremy G. Siek, Matthew Heimerdinger, Tianyu Chen et al.* · `cs.PL` · arXiv:2611.31724v1 · relevance 0.13

- **In one sentence**: The paper gives the first denotational (meaning-based) proofs that closure conversion for a Turing-complete functional language is semantically reflected, using a graph model and a Scott-domain model, and compares mechanized compiler-correctness proofs across five semantic styles, two denotational and three operational.
- **In plain words**: This paper is about proving that a compiler, the program that translates code from one language into another, does not change what the code means. The authors ask whether "denotational" semantics, which describe a program by the mathematical value it stands for, can be used for such proofs as well as the "operational" styles, which describe a program by the steps it takes when run. They test this on a compiler from a small functional language to a low-level language, and report which style gave shorter proofs for which step.
- **Why it matters**: Correctness proofs for compilers are costly, and the choice of semantic style affects how hard they are. The text reports that no single style was best for every pass, and that proof size depends on how different the source and target runs are (operational) or whether a pass needs a logical relation (denotational). This is a measured comparison of tradeoffs rather than a claim that one approach wins.
- **Background needed**: - Compiler: a program that translates source code into another language, such as machine-level code.
- Semantics: a precise mathematical description of what programs mean.
- Operational semantics: describes meaning by the step-by-step execution of a program (for example, abstract machines or interpreters).
- Denotational semantics: describes meaning by a mathematical object the program stands for, such as a function in a model.
- Compiler correctness: the target program must behave as the source does; "preserved" means meaning carries over, "reflected" means meaning of the output implies meaning of the input.
- Closure conversion: a translation that turns nested functions, which capture variables from their surroundings, into flat first-order code.
- Turing-complete: powerful enough to express any computation, including ones that never halt.
- Logical relation: a proof technique that relates source and target values across types, often used for functions.
- Mechanized proof: a proof checked by a computer proof assistant. · level: research-level

<details><summary>Original abstract</summary>

Anyone setting out to prove a compiler correct must choose a style of semantics. The CakeML and CompCert projects, among others, show that operational semantics such as abstract machines and interpreters are viable choices. In this paper we explore whether denotational semantics can also be used in proofs of compiler correctness and evaluate the tradeoffs. We focus on a compiler from FPC, a language with lexically scoped functions and recursive types, to a first-order low-level intermediate language. This compiler includes closure conversion, but no prior proof of correctness with respect to denotational semantics covers closure conversion for a Turing-complete language. Compiler correctness requires that the denotation of a program be both preserved and reflected by the compiler. For closure conversion, reflection is the hard direction. We present the first denotational proofs of semantic reflection for closure conversion applied to a Turing-complete language, one proof with respect to a graph model and one with respect to Scott domains. For the graph-model proof we develop a new logical relation, the approximant logical relation, and for the Scott-domain proof we adapt a logical relation of Reynolds. As a first step in evaluating the tradeoffs, we compare mechanized correctness proofs of an eight-pass compiler, from FPC down to a typed low-level intermediate language, in five semantic styles. Two of the styles are denotational and three are operational. We find that no one semantics yields the shortest proofs for every compiler pass. We identify two factors that influence proof size. For operational semantics, proof size tends to grow with how much the runs of the source and target differ. For denotational semantics, the proofs are succinct when the correctness of a pass is an equation between meanings, and lengthy when a pass needs a logical relation.

</details>

## Systems and networking

### [Real-Time AI Acceleration on a 2D Spatial Dataflow Architecture](https://arxiv.org/abs/2611.31556)
*Shriram Raja, Anton Njavro, Richard West* · `cs.DC` · arXiv:2611.31556v1 · relevance 0.11

- **In one sentence**: The paper profiles the Tenstorrent Blackhole spatial dataflow accelerator and builds a worst-case execution time task model, expressed as a Homogeneous Synchronous Dataflow Graph, extended with a pessimistic NoC contention analysis for multi-core workloads.
- **In plain words**: Machine learning is being built into systems that must respond on strict schedules, so engineers need to be able to guarantee how long each computation can take. This paper studies an open-design AI chip, the Tenstorrent Blackhole, as an alternative to GPUs, whose internal timing is poorly documented. The authors measured the chip, built a model that estimates the longest time a task can take, and tested it across 12,567 task configurations.
- **Why it matters**: Predictable timing is a precondition for using AI accelerators in safety-critical real-time systems such as robotics or vehicles, and the open software stack makes this platform easier to study than closed GPUs. The text reports that the model's estimates always sat above the observed worst case, but the overheads are sizeable (up to 200% for single-core and 500% for multi-core), and the authors describe the work as laying foundations rather than a finished solution.
- **Background needed**: - Worst-case execution time (WCET): an upper bound on how long a task can take, used to check that deadlines are met.
- Real-time system: one that must finish work by fixed deadlines.
- Spatial dataflow accelerator: a chip with a grid of small processing cores that pass data to each other, with the programmer controlling where data goes.
- Network-on-Chip (NoC): the on-chip communication network that links the cores; contention means cores compete for it and slow each other down.
- Synchronous dataflow graph: a way of describing a program as tasks that consume and produce fixed amounts of data, which makes timing easier to bound.
- GPU scheduling: GPUs group threads in ways that are not fully documented, which makes their timing hard to analyze. · level: research-level

<details><summary>Original abstract</summary>

Machine Learning (ML) is increasingly being integrated into real-time systems, which makes the timing analysis of ML accelerators necessary. However, the most popular commercial accelerator, the Graphics Processing Unit (GPU), remains difficult to analyze as several aspects of its behavior, including scheduling of threads involved in single-instruction multiple-thread computations and memory access latency, are not fully documented. Spatial dataflow accelerators present an interesting alternative to GPUs, as they inherently support compute and memory partitioning. Data movement and computation locality are explicitly controlled by the programmer. In this work, we consider the Tenstorrent Blackhole, which is based on a commodity RISC-V architecture. It consists of a 2D grid of cores connected by Networks-on-Chip (NoCs), supporting a fully open software runtime. We profile the Blackhole platform and develop a worst-case execution time task model as a Homogeneous Synchronous Dataflow Graph. We extend this model to a preliminary analysis of multi-core workloads by considering NoC-related delays. Finally, we evaluate our model across 12,567 task configurations and workloads. Results show that the estimate derived from our model lies above the observed worst case in every configuration. For single-core workloads, the overhead is less than 100% in most cases, with a maximum of less than 200%, and for multi-core workloads, it is less than 500% using a pessimistic NoC contention analysis. This paper lays the foundations for real-time computing on a promising open accelerator design.

</details>

### [The Recycler: In-Transit Machine Learning on High-Fidelity Data from Simulation Campaigns as an Optimized Approach for Building Frontier Models](https://arxiv.org/abs/2611.31434)
*Nikhil Rao, Mark Berrill, Ankush Checkervarty et al.* · `cs.DC` · arXiv:2611.31434v1 · relevance 0.10

- **In one sentence**: The paper describes an in-transit machine learning workflow that streams data from several parallel simulations in a simulation campaign directly into training of a large model on an exascale supercomputer, instead of writing it to files first.
- **In plain words**: Scientists often run many large computer simulations at once, such as variations of a particle accelerator or climate model, and they produce far more detailed data than disks can store. This paper reports a setup that sends that data straight from the running simulations into the training of an AI model, skipping most of the saving to files. The text presents this as a first demonstration on a very large supercomputer and says it can use much more of the detailed data than file storage allows.
- **Why it matters**: Storage limits often force researchers to throw away most simulation output, so training AI on live data could make better use of expensive computing time. The text suggests this could help steer simulation campaigns with AI feedback, though it gives no performance figures here, so the practical size of the benefit is not yet clear from this text alone.
- **Background needed**: - Simulation campaign: many related simulations run in parallel with different settings.
- Exascale supercomputer: a machine capable of about a billion billion calculations per second.
- In-transit machine learning: training an AI model on data while it is still moving from simulation to storage, rather than after it is saved.
- File I/O: reading and writing data to disk, which is slow and capacity-limited at this scale.
- Frontier model: a very large, state-of-the-art AI model.
- High-fidelity data: detailed, accurate simulation output with fine resolution. · level: research-level

<details><summary>Original abstract</summary>

We report on the first realization of in-transit machine learning using data streamed from multiple simulations running in parallel to the training on the same exascale high performance computing system. This workflow can be commonly applied to a broad variety of scenarios in which simulation campaigns play an important role. Unlike single simulations, campaigns run several simulations in parallel. This is interesting for finding an optimum operation point of a machine like a particle accelerator or a fusion reactor, quantifying the variation in model predictions e.g. in climate research, or discovering new capabilities e.g. in materials or drug design. Such campaigns produce huge amounts of high-fidelity data at high rates. File system bandwidth and capacity prohibit retaining all of that data, usually requiring orders of magnitude in reduction before it can be stored. We demonstrate a workflow that streams the data from multiple simulations to train a frontier model in parallel, thereby maximizing data throughput. We demonstrate that this can use a much larger amount of high-fidelity data as training data for the model compared to storage in files, essentially replacing file IO by in-transit training of large-scale frontier models. This will allow to create AI-informed feedback loops to steer simulation campaigns while reducing the overall computation time needed and provide high-fidelity frontier models for reuse by the scientific community.

</details>

## Human-computer interaction

### [Emerging International Best Practices for AI Model Specs](https://arxiv.org/abs/2611.32768)
*Edward Kembery, Nathan Lambert, Robert McCarthy et al.* · `cs.CY` · arXiv:2611.32768v1 · relevance 0.06

- **In one sentence**: This paper offers a five-part guide to writing "model specs" (public documents stating how frontier AI models should behave), covering benefits, a taxonomy, practical writing and implementation guidance, eight open problems, and recommendations for companies, governments and civil society.
- **In plain words**: AI companies are starting to publish documents that describe how their AI systems are meant to behave, and there has been little independent advice on how to write them. This paper tries to fill that gap by explaining why such documents help, sorting them into a rough classification, suggesting how to write and apply them, and listing unresolved questions. The text provided is a summary of the paper's structure; it does not show the specific content of the guidance or the taxonomy.
- **Why it matters**: As AI systems become more influential, publicly stated behaviour rules are becoming part of how these systems are developed and governed, so practical guidance on them may matter to developers, regulators and the public. The text does not show how widely the proposals have been adopted or tested, so their real impact is unclear.
- **Background needed**: - A "model spec" is a written document from an AI developer describing the intended behaviour of its AI model, including what it should and should not do.
- "Frontier AI developers" means the organisations building the most capable, cutting-edge AI models.
- A "taxonomy" is a structured classification of types or categories, here of model specs.
- "Governance" refers to the rules, oversight and institutions that guide how a technology is developed and used.
- Model specs are a fairly new kind of document, so there is no settled standard for them yet. · level: intermediate

<details><summary>Original abstract</summary>

Frontier AI developers from around the world have begun to publish documents that describe how their AI models are intended to behave. Although these 'model specifications'-or 'model specs', for short-are increasingly important in AI development and governance, little independent guidance exists for writing them. This paper addresses this gap in five main sections. First, we outline the advantages of writing a model spec for AI developers and society at large. Second, we introduce a taxonomy for model specs that developers can take inspiration from. Third, we propose guidance for writing and implementing a spec in practice. Fourth, we note eight open problems related to writing model specs for safe and desirable behaviour. We conclude with recommendations for frontier AI companies, governments, and research and civil society organisations.

</details>

### [Calm Agent: Reframing Agent Interaction around Intermittent Human Attention](https://arxiv.org/abs/2611.32009)
*Dian Jin, Zixun Fu, Guan Wang et al.* · `cs.HC` · arXiv:2611.32009v1 · relevance 0.05

- **In one sentence**: This position paper proposes "Calm Agent," a design framework for AI agents running ongoing background tasks that organizes three on-demand interaction modes (Delegate, Adjust, Check) around a persistent task representation, and illustrates it with a desktop prototype called Orvlet.
- **In plain words**: The paper argues that AI helpers doing side tasks should be designed for people who only check in now and then, because their attention is elsewhere. The authors describe a way to structure this: users hand off a task, tune it, or glance at its status, with the task's state kept in one continuing record. They show the ideas through a desktop prototype, Orvlet, but the text does not report user testing or measured results.
- **Why it matters**: As AI agents start running tasks for long stretches in the background, how people keep track of and steer them without being pulled away from their main work is an open design question. The paper's framing may be relevant to interface design and attention research, though its evidence is a position and prototype description rather than a study.
- **Background needed**: - AI agent: software that carries out multi-step tasks on a user's behalf with some autonomy.
- Intermittent attention: a person who looks at a task only occasionally while doing other work.
- Persistent task representation: a continuing internal record of what a task is, its status, and its settings, so users can pick it up again.
- Generative interaction: interfaces an AI creates on the fly to fit an open-ended goal, versus fixed, pre-built controls.
- Human-computer interaction (HCI): the field studying how people use and design computer systems.
- Position paper: a text that argues for a viewpoint and proposes a framework, typically without a full empirical evaluation. · level: intermediate

<details><summary>Original abstract</summary>

AI agents can carry out auxiliary tasks while users focus on other work. Yet users still need to understand task state, make changes, and respond when help is required. We argue that agents for ongoing auxiliary tasks should be designed around intermittent human attention: tasks should continue between interactions, and users should be able to return with little effort to understand and control them. We develop this position as Calm Agent. It connects three on-demand interaction modes: Delegate, Adjust, and Check, through a persistent task representation. Generative interaction provides controls and feedback suited to open-ended goals, while existing controls support routine actions. We illustrate these principles with Orvlet, a desktop prototype for background execution and compact task interfaces. We identify challenges in adapting interfaces while preserving continuity, coordinating attention across tasks, providing responsive interaction, and learning user habits over time. The aim is to support continuing task control while protecting attention for primary work.

</details>

## Information theory

### [Multi-User Linear Precoder Optimization for Obfuscation-Aided Mixed Regular and Wiretap Coding](https://arxiv.org/abs/2611.31840)
*Bastian Loss, Ahmad Nimr, Gerhard Fettweis* · `cs.IT` · arXiv:2611.31840v1 · relevance 0.19

- **In one sentence**: The paper proposes a generalized obfuscation-aided mixed wiretap/regular coding system built on multi-user linear precoding, formulates the precoder optimization with a minimum secrecy rate constraint, and studies it with simulations on a geometric two-user line-of-sight channel.
- **In plain words**: Wireless signals can be overheard by an eavesdropper, and a common defense is "wiretap coding," which hides data by exploiting the fact that the intended receiver has a better channel than the eavesdropper. When that advantage is small, this defense sharply cuts how much data can be sent. This paper studies a mixed scheme: a short secret is protected with wiretap coding, and that secret is used to scramble the main data, which is then sent with ordinary error-correcting code. The authors design how the transmitter aims its signals for two users and report simulation results on how the scheme behaves.
- **Why it matters**: It addresses a practical limit of physical-layer security, where secrecy is provided by the channel itself rather than by encryption, and it may matter for future wireless systems. The text reports simulation results only, so its practical significance beyond the modeled geometric channel is not established.
- **Background needed**: - Wiretap coding: a way to send data so an eavesdropper learns almost nothing, relying on the receiver having a better channel.
- Regular (ordinary) channel coding: standard error-correction that maximizes data rate without secrecy.
- Secrecy rate: the amount of data per use of the channel that stays hidden from the eavesdropper.
- Obfuscation: scrambling the data with a secret key so it is unreadable without that key.
- Linear precoding: the transmitter weights signals across multiple antennas to aim beams at chosen users.
- Beampattern: a map of how signal strength varies with direction, used to see where a transmitter sends energy.
- Line-of-sight (LoS) channel: a channel dominated by a direct path between transmitter and receiver, modeled from geometry. · level: research-level

<details><summary>Original abstract</summary>

Physical-layer security has attracted considerable research interest with the development of quantum computing. One prominent approach is wiretap coding, which exploits the channel advantage of a legitimate receiver over an eavesdropper to achieve secure communication. However, under unfavorable channel conditions, wiretap coding can significantly reduce the achievable rate compared to regular channel coding. Mixed coding alleviates this limitation by using wiretap coding to protect a short secret required for obfuscation, while the obfuscated payload is encoded using regular channel coding. In this work, we propose a generalized obfuscation-aided mixed-coding system based on the multi-user (MU)-linear precoding (LP) architecture that unifies existing approaches employing different obfuscation functions. We then formulate the corresponding precoder optimization problem, abstracting the obfuscation function through a minimum secrecy rate constraint. Numerical simulations using a geometric two-user line-of-sight (LoS) channel demonstrated how the minimum secrecy rate requirement determines the operating point of mixed coding between regular and wiretap coding. Subsequent beampattern analysis revealed a key synergy between mixed coding and precoding: Mixed coding enables individual beam shaping for the two coding layers. Finally, spatial analysis showed that mixed coding offers the largest sum-rate gains when users are positioned at similar angles.

</details>

### [Self-Orthogonal Minimal Codes from n-to-1 Mappings](https://arxiv.org/abs/2611.32192)
*Qin Du, Ziling Heng, Jun Zhang* · `cs.IT` · arXiv:2611.32192v1 · relevance 0.15

- **In one sentence**: Using right greatest common divisors of skew polynomials to find kernel dimensions of linearized polynomials, the paper derives exact weight distributions and proves minimality and self-orthogonality for linear codes from three families of n-to-1 mappings over finite fields.
- **In plain words**: This paper is about error-correcting codes, the mathematical recipes used to protect data from corruption. It studies codes built from certain functions that map many inputs to one output, and it is hard to count how often their codewords have each weight for complicated functions. The authors use an algebraic tool called skew polynomial rings to work out those counts for two new function families and one known family, and they show the resulting codes have two useful properties.
- **Why it matters**: The codes are claimed to be both self-orthogonal, which is the property used in building quantum error-correcting codes, and minimal, which is the property used in secret-sharing schemes, so one family could serve both purposes. The text does not say how these codes would perform in practice, so the practical significance is unclear from this text alone.
- **Background needed**: - Linear code: a set of vectors over a finite field (a number system with finitely many elements) closed under addition and scaling; its weight is the count of nonzero entries in a codeword.
- Weight distribution: how many codewords have each possible weight; it reveals a code's error-correcting behaviour.
- Self-orthogonal code: a code whose codewords are orthogonal to one another, a property needed for quantum error-correcting codes.
- Minimal code: a code where no codeword's support is contained in another's; this lets its supports define access rules for secret sharing.
- n-to-1 mapping: a function where exactly n inputs share each output value; Walsh spectrum and linearized polynomials are standard tools for analysing such functions.
- Skew polynomial ring: a generalisation of ordinary polynomials in which variables do not commute, with a "right greatest common divisor" used as the key computational tool. · level: research-level

<details><summary>Original abstract</summary>

Self-orthogonal codes are central to the construction of quantum error-correcting codes, and minimal codes yield secret-sharing schemes whose access structures are read off from the supports of their codewords. A code that is both self-orthogonal and minimal therefore serves both purposes at once, so that a single family of codes can produce a quantum code and a secret-sharing scheme simultaneously. Linear codes arising from n-to-1 mappings over finite fields are a natural source of such codes and have attracted considerable attention recently, yet their parameters and weight distributions remain difficult to determine: for most high-degree functions the Walsh spectra cannot be computed directly, and it is precisely these weights on which the analysis of minimality and self-orthogonality rests. We address this difficulty through the algebraic theory of skew polynomial rings. Using the right greatest common divisor of skew polynomials, we determine the dimensions of the kernel spaces of the linearized polynomials associated with the n-to-1 mappings, which in turn yield the weight distributions of the corresponding codes. With this method we treat two newly constructed families of n-to-1 functions together with one known family, and obtain the exact weight distributions of the resulting codes; we further prove that all of these codes are minimal and self-orthogonal. Each family therefore simultaneously yields a quantum error-correcting code and a secret-sharing scheme, with explicitly determined parameters and access structures. This work offers a new perspective for determining the parameters of linear codes derived from n-to-1 mappings.

</details>

## High-energy theory and gravity

### [Free hyperboloidal evolution in 3D: gauge waves and constraint-violating gravitational waves](https://arxiv.org/abs/2611.31379)
*Alex Va\~n\'o-Vi\~nuales* · `gr-qc` · arXiv:2611.31379v1 · relevance 0.22

- **In one sentence**: This paper extends hyperboloidal (conformally compactified) evolution with the BSSN/Z4 formulation of general relativity from spherical symmetry to full 3D, demonstrating free evolution of gauge waves and constraint-violating gravitational waves on Minkowski spacetime with signal extraction at future null infinity.
- **In plain words**: Scientists who simulate gravity on computers usually have to cut off their simulated universe at a finite distance, which can distort the gravitational waves they want to study. This paper describes a way to carry the simulation all the way out to "future null infinity," the far-away boundary where outgoing waves can be read off cleanly, and it does so for full three-dimensional simulations. The authors test it on simple disturbances in empty flat space and report that the code runs reliably and the signals can be extracted at that far boundary.
- **Why it matters**: Clean access to waves at infinity matters for predicting the gravitational-wave signals that detectors such as LIGO and Virgo are meant to catch, so a working 3D tool is a useful building block. The text only covers tests in flat spacetime with simple perturbations, so it does not yet show how the method performs for realistic sources such as merging black holes.
- **Background needed**: - General relativity describes gravity as the curvature of spacetime; numerical relativity solves its equations on computers.
- Gravitational waves are ripples in spacetime produced by accelerating massive objects.
- "Minkowski spacetime" is empty, flat spacetime, the simplest test background.
- "Future null infinity" is the idealized far-away region where outgoing light and gravitational waves end up; hyperboloidal slices are time slices that reach it.
- Conformal compactification maps infinite distance onto a finite boundary so the whole region can be simulated.
- BSSN and Z4 are standard formulations of Einstein's equations used in simulations; "free evolution" means the constraint equations are not enforced exactly during the run, so small constraint violations can appear.
- Gauge waves are coordinate-choice disturbances that do not carry physical energy. · level: research-level

<details><summary>Original abstract</summary>

Hyperboloidal evolution allows to reach future null infinity within numerical relativity simulations. This work extends the conformal compactification approach with BSSN/Z4 from spherical symmetry to full 3D simulations. This is the first free numerical hyperboloidal evolution in 3D with a common formulation of general relativity. In this first step, gauge waves and constraint-violating gravitational waves perturbing Minkowski spacetime are evolved nonlinearly and show that the implementation is reliable and signals can be successfully extracted at future null infinity.

</details>

### [NS5-branes and the black hole/string transition](https://arxiv.org/abs/2611.31945)
*Asad Fayiz, Emil J. Martinec* · `hep-th` · arXiv:2611.31945v1 · relevance 0.21

- **In one sentence**: The paper extends a family of 6d BPS supergravity solutions (fundamental strings plus NS5-branes near the BTZ black hole threshold) to include gauge excitations of the fivebranes, and studies the energetics of D-string solitons relative to the deconfinement transition of little strings.
- **In plain words**: This paper is about a theoretical question in string theory: when does a tangle of strings turn into a black hole, and what happens at the tipping point between the two. The authors build more detailed model geometries that describe a set of strings and five-dimensional membranes (fivebranes) sitting very close to that tipping point. They then examine how much energy certain small objects called D-string solitons carry, and how that relates to the point where the little strings stop being confined.
- **Why it matters**: The black hole/string transition is a long-standing topic linking gravity and string theory, so the work matters to specialists studying that connection. The provided text only gives the aims and setup, not the specific results, so its broader significance is unclear from this summary alone.
- **Background needed**: - BTZ black hole: a simple black hole solution in three-dimensional spacetime, used as a toy model in gravity research.
- Supergravity solution: a classical geometry of gravity that solves the equations of a supersymmetric theory, often used to model string theory objects.
- BPS state: a special, highly symmetric configuration whose energy is fixed by its charges, making it easier to analyse.
- Fundamental string and NS5-brane: basic extended objects in string theory; branes are higher-dimensional generalisations of points or strings.
- Little strings: non-gravitational strings that live on NS5-branes and behave as the basic non-abelian degrees of freedom in the relevant theory.
- Deconfinement transition: a phase change, analogous to melting, in which the constituents of a bound state become free.
- D-string soliton: a stable, particle-like lump of energy built from D-strings, a class of branes that carry charge for open strings. · level: research-level

<details><summary>Original abstract</summary>

Near to the onset of BTZ black hole formation in string theory is a large ensemble of 6d BPS supergravity solutions sourced by slightly separated fundamental strings and Neveu-Schwarz fivebranes. We extend the construction of these geometries to include gauge excitations of the fivebranes, and then study the energetics of D-string solitons in relation to the deconfinement transition of little strings, which are the natural non-abelian degrees of freedom that deconfine in the transition to the black hole phase.

</details>

## Statistical physics

### [Parametric neural-network wavefunctions across a bosonic phase transition](https://arxiv.org/abs/2611.33150)
*Daniil S. Antonenko, Liang Fu, Leonid I. Glazman* · `cond-mat.quant-gas` · arXiv:2611.33150v1 · relevance 0.26

- **In one sentence**: The paper introduces Boseformer, an attention-based neural-network ansatz that is trained over a Hamiltonian parameter to represent bosonic wavefunctions across a superfluid-to-crystal quantum phase transition in 2D bosons with 1/r^3 repulsion.
- **In plain words**: The paper looks at how a gas of particles that follow bosonic quantum rules behaves as it shifts between a flowing superfluid state and an ordered crystal state. The authors build a single neural network that describes the quantum wavefunction (the mathematical object encoding the system's state) for many strength settings of the interaction at once. Once trained, it can be used across the transition without retraining for each setting.
- **Why it matters**: Describing phase transitions in quantum matter is computationally hard, and a model that works across a range of parameters without retraining could reduce that cost. The text is a short abstract, so it does not show how accurate the results are or how the method compares with existing approaches, and its wider significance is not yet established.
- **Background needed**: - Bosons: particles (such as some atoms) that can share the same quantum state, unlike electrons.
- Wavefunction: the mathematical function that gives the full quantum description of a system.
- Phase transition: an abrupt change in a material's state, such as melting or freezing, here between flowing (superfluid) and ordered (crystal) forms.
- Hamiltonian parameter: a tunable setting in the system's energy rules, here the strength of interactions.
- Variational Monte Carlo: a method that tunes an approximate wavefunction using random sampling to lower its energy.
- Neural-network wavefunction: using a neural network as a flexible, trainable guess for the wavefunction.
- Attention: a neural-network mechanism that lets each part of the input weigh other parts, widely used in modern AI models. · level: research-level

<details><summary>Original abstract</summary>

We propose Boseformer, a universal attention-based neural-network architecture for representing the wavefunctions of particles with bosonic quantum statistics, including superfluid and crystal phases. The model is trained to generate the wavefunction as a function of a Hamiltonian parameter across the quantum phase transition between these phases. Once trained with variational Monte Carlo optimization, it can serve as a foundation model describing the phase transition without the need to retrain it for individual parameter values. We demonstrate our method on a system of two-dimensional bosons with $1/r^3$ repulsive interaction.

</details>

### [Polar Streams through Active Condensation in Flocks](https://arxiv.org/abs/2611.33007)
*Lauritz Hahn, Xinyu Dou, Ziqi Zhou et al.* · `cond-mat.soft` · arXiv:2611.33007v1 · relevance 0.18

- **In one sentence**: Experiments on self-propelled Janus colloid dimers, backed by simulations and coarse-grained hydrodynamic theory, show that flocks can phase-separate into elongated polar streams via an "active nematic condensation" mechanism in which denser regions gain stronger polar and nematic order that draws in more particle flux.
- **In plain words**: Researchers studied tiny self-propelled particles that move together as a group, called a flock. They found that the flock can split into dense, elongated streams that move along their long axis, instead of the sideways bands usually seen near the point where flocking begins. The text attributes this to a feedback loop: denser parts of the flock align more strongly, which pulls in even more particles.
- **Why it matters**: The paper proposes that flocking and clustering can work together rather than only compete, and that nematic order (alignment without a preferred direction, like rods lying side by side) can shape flocks, which the standard Toner-Tu flocking equations do not include. Its wider relevance to natural or engineered swarms is suggested by the authors as a generic mechanism, but the text itself does not test that beyond this system.
- **Background needed**: - Active matter: systems whose units consume energy to move on their own, such as colloids, cells or animals.
- Janus colloid dimers: pairs of micron-scale particles with two faces of different chemistry, which self-propel when driven (here, the experimental model).
- Flocking: particles aligning their directions so the group moves coherently; the Toner-Tu equations are the standard continuum description.
- Motility-induced phase separation: self-propelled particles bunch together into dense clusters even without attraction between them.
- Polar vs. nematic order: polar order means all particles point the same way; nematic order means they share an axis but may point either way.
- Coarse-graining: replacing individual particles with smooth density and orientation fields to derive a hydrodynamic theory. · level: research-level

<details><summary>Original abstract</summary>

Two of the most paradigmatic phenomena in active matter are flocking, where particles align to move collectively, and motility-induced phase separation, where self-propulsion causes particles to condense even without attractive interactions. Here, using experiments on self-propelled Janus colloid dimers, we show that flocks can phase separate to form polar streams. These structures are elongated dense clusters of particles that flock along the stream's long axis, in contrast to the well-known transverse bands that form close to the flocking transition. We use particle-based simulations and hydrodynamic theory obtained through coarse-graining to identify the underlying mechanism, which we call active nematic condensation: Denser regions of the flock develop stronger polar and hence nematic order, which leads to further particle fluxes into the dense region. These results reveal a generic mechanism whereby flocks can condense into streams. Our findings uncover that flocks can be shaped by nematic order, which is usually not accounted for in the standard Toner-Tu equations. More broadly, our work shows that collective motion and phase separation can not only coexist but also cooperate in active matter.

</details>

## Condensed matter

### [Detecting Topological Phases Through Dynamics of Chiral Density in Momentum-space Lattices](https://arxiv.org/abs/2611.31878)
*Rui Tian, Xiayao He, Tianhao Wu et al.* · `cond-mat.quant-gas` · arXiv:2611.31878v1 · relevance 0.21

- **In one sentence**: A theoretical proposal to detect topological edge modes and bulk-boundary correspondence in a momentum-space Su-Schrieffer-Heeger chain by Fourier-transforming the time evolution of the chiral density, which is linked to the local density of states.
- **In plain words**: This paper is about a way to tell whether a simulated quantum system has special "topological" features, namely states stuck at its edges with zero energy. The authors use a lattice whose sites are arranged in momentum rather than in real space, and they watch how a particular quantity (the chiral density) changes over time. Applying a Fourier transform to that signal recovers the energy-resolved picture of the system, which shows the edge states.
- **Why it matters**: Momentum-space lattices are a practical platform for quantum simulation, so a dynamical readout that can identify topological edge states could be a useful diagnostic for such experiments. The text presents this as a proposal; it does not report an experiment, so how well it works in practice is not shown here.
- **Background needed**: - Topological phase: a property of a material's overall structure that stays fixed under small changes, and that often shows up as special states at the edges.
- Edge modes with zero energy: states localized at the boundary of a system that sit at zero energy, a hallmark of topology.
- Su-Schrieffer-Heeger (SSH) chain: a simple one-dimensional chain of sites with alternating coupling strengths, a standard toy model for topological edge states.
- Bulk-boundary correspondence: the principle that topological edge states appear at the boundary whenever the interior of the system is topological.
- Density of states and local density of states: measures of how many energy levels exist overall, and how they are distributed in space; they are usually probed by spectroscopy.
- Chiral operator: a symmetry-related operator whose expectation value the paper tracks over time.
- Quantum simulation: using a controllable quantum system to mimic another system that is hard to study directly.
- Fourier transform: a mathematical step that converts a signal in time into a spectrum of frequencies (here, energies). · level: research-level

<details><summary>Original abstract</summary>

Momentum-space lattices offer a versatile platform for quantum simulation in particular emulating topological states of matter.In this work, we propose a spectroscopic protocol via utilizing the dynamics of the chiral operator to detect the topological properties of a momentum-space Su-Schrieffer-Heeger chain. We show that the time evolution of the chiral density is directly linked to the local density of state (LDOS). By performing a Fourier transformation of that, we reconstruct both the LDOS and density of states of the system, enabling the unambiguous signature of zero-energy edge modes and the bulk-boundary correspondence. This dynamical approach provides a diagnostic tool for exploring topological phases in synthetic quantum matter.

</details>

### [Intrinsic longitudinal Hall effect in ferroaxial metals with high-order rotation axes](https://arxiv.org/abs/2611.32709)
*Eleni Chatzikyriakou, Stepan Tsirkin, Fernando Pe\~naranda et al.* · `cond-mat.mes-hall` · arXiv:2611.32709v1 · relevance 0.20

- **In one sentence**: The paper shows that the intrinsic (quantum) longitudinal Hall effect in ferroaxial metals should be isolated in the eight ferroaxial groups that have a 3-, 4- or 6-fold rotation axis, where the classical Lorentz-force term vanishes, and proposes Ni3P as a candidate for measurement.
- **In plain words**: When a metal carries electric current and sits in a magnetic field, it produces a sideways voltage called the Hall effect. Part of this comes from a quantum property of the electrons' motion, but the ordinary push of the magnetic field on moving charges usually hides it. The authors find that in certain crystal families with high-order rotational symmetry, the ordinary part cancels for a specific sideways-measured setup, which would leave the quantum part visible; they calculated this for several materials and suggest Ni3P as the best one to test.
- **Why it matters**: Being able to measure the quantum contribution without the much larger classical background would give a cleaner test of how electron band structure produces transport signals. The text presents this as a theoretical proposal supported by first-principles calculations; it does not report an experiment, so the practical payoff is still to be shown.
- **Background needed**: - Hall effect: a voltage generated perpendicular to both current and magnetic field in a conductor.
- Lorentz force: the classical push a magnetic field exerts on moving charges; it is the usual, larger source of the Hall signal.
- Berry curvature: a geometric property of electron wavefunctions in a crystal that acts like an internal magnetic field in momentum space; it can produce a quantum Hall-type contribution.
- Fermi surface: the surface in momentum space separating occupied from unoccupied electron states, which controls most metallic transport.
- Ferroaxial crystals: crystals lacking certain mirror and inversion symmetries in a way that allows a rotation-like ("axial") order parameter; the paper classifies them by their rotation axes.
- Rotation axis order (3-, 4-, 6-fold): how many times a crystal looks unchanged under a full turn divided by the number of such turns; higher order means more symmetry.
- First-principles calculation: computing material properties directly from quantum mechanics and known atomic structure, without fitted parameters.
- Units: S/m/T means siemens per metre per tesla, a measure of Hall conductivity per unit magnetic field. · level: research-level

<details><summary>Original abstract</summary>

The low-field Hall resistivity of non-magnetic metals has an intrinsic quantum contribution that derives from the field-corrected Berry curvature and intrinsic magnetic moment of the Bloch states near the Fermi surface. However, its effect is usually overshadowed by the classical Lorentz-force contribution. Here we show that for the longitudinal Hall effect, which occurs in ferroaxial crystals when the applied magnetic field lies in the Hall plane, the Lorentz force contribution vanishes for the eight ferroaxial groups with a 3,4 or 6-fold rotation axis. This provides an opportunity to measure the quantum correction in isolation, but so far all measured instances of the effect fall in the remaining five ferroaxial groups of lower symmetry, where the Lorentz force dominates the signal. We compile a list of candidate ferroaxial metals with such high-order rotation axis and compute the Hall effect from first principles for representative candidates, identifying Ni$_3$P with $\sigma^{\rm H}_{xzx} = 28.4$ S/m/T as a promising material to unambiguously measure the intrinsic longitudinal Hall effect.

</details>

## Particle physics

### [Dark vector meson effects on composite dark matter](https://arxiv.org/abs/2611.31368)
*Tomohiro Abe, Ryosuke Sato, Ozan Semin et al.* · `hep-ph` · arXiv:2611.31368v1 · relevance 0.20

- **In one sentence**: Extends studies of G-parity-odd dark pion dark matter in a QCD-like dark sector by adding dark rho vector mesons, examining their effects on relic abundance, their mixing with Standard Model gauge bosons, and collider reach at ATLAS/CMS recasts and future FCC-hh and muon colliders.
- **In plain words**: This paper looks at a hypothetical hidden sector, a dark version of the strong force with its own quarks, whose lightest particles could make up dark matter. It adds a heavier "dark rho" particle to earlier models and finds that it can change how much dark matter would be left over from the early universe, and that it can mix with ordinary force carriers so it decays in new ways. The authors also estimate how far future colliders could search for these particles, reporting that the FCC-hh could probe rho masses up to about 40 TeV.
- **Why it matters**: If dark matter is a composite particle from a hidden strong force, heavier partner particles can alter the cosmological calculation and the collider signals, so this sets concrete targets for future experiments. The connection to real dark matter remains a hypothesis; the text does not show that such a sector exists.
- **Background needed**: - Dark matter: unseen matter whose gravity shapes galaxies; its "relic abundance" is the amount left over after the early universe cooled.
- QCD-like gauge theory: a model of a strong force like the one binding quarks in protons, here assumed to exist in a hidden sector.
- Pions and rho mesons: bound states of dark quarks; pions are the lightest, rho mesons are heavier vector (spin-1) partners.
- G-parity: a symmetry-like label that determines which decays and interactions are allowed.
- Resonant enhancement: a sharp increase in interaction rate when a particle's mass matches the energy of colliding particles.
- Mixing with Standard Model gauge bosons: the dark rho can partly turn into ordinary W, Z or photon-like particles, opening decay routes.
- Collider terms: ATLAS and CMS are LHC experiments; FCC-hh is a proposed future proton collider; muon colliders are a proposed lepton machine; "recast" means reinterpreting existing searches for a new model. · level: research-level

<details><summary>Original abstract</summary>

We extend previous studies of $\mathcal{G}$-parity-odd dark pion dark matter in a QCD-like $\mathrm{SU}(N_c)$ gauge theory with electroweakly interacting dark quarks to include the effects of $\rho$ mesons. We show that vector mesons can substantially affect relic abundance calculations through resonant enhancement, significantly affecting the conditions required to reproduce the observed relic abundance. Electroweak interactions further induce mixing between the dark $\rho$ mesons and Standard Model gauge bosons, opening new decay channels for the dark $\rho$ and modifying the effective interactions of the dark pions. We recast existing ATLAS and CMS searches to constrain the model, and perform a collider phenomenology study targeting the future FCC-hh and muon colliders, focusing on the resonant enhancement of cross sections in the $e^+e^-$, $\mu^+\mu^-$, and $W^+W^-$ final states for the latter. We show that the FCC-hh could probe $\rho$ mesons whose mass is up to 40 TeV.

</details>

### [Dark Matter Assisted Axion-Magnetic Resonance](https://arxiv.org/abs/2611.32906)
*Chen Sun, Si-Yu Wu, Seokhoon Yun* · `hep-ph` · arXiv:2611.32906v1 · relevance 0.18

- **In one sentence**: A proposed resonance in which an oscillating axion dark matter background boosts the conversion of stellar axions into X-ray photons in magnetic fields, tested against NuSTAR observations of the starburst galaxy M82.
- **In plain words**: The paper looks at a hypothetical particle called the axion, which might make up dark matter and might also be produced inside stars. The authors propose that the invisible dark matter background can help a stellar axion turn into a detectable X-ray photon when it passes through a magnetic field. They apply this idea to the starburst galaxy M82 and use existing X-ray data from the NuSTAR telescope to set limits.
- **Why it matters**: If the mechanism is right, it could raise the expected X-ray signal by a factor of roughly 100 in some axion mass ranges where ordinary conversion is weak, tightening limits on how strongly axions couple to photons. The text reports only a moderate preference over the background-only model that is still consistent with statistical fluctuations, so the result is suggestive rather than a detection.
- **Background needed**: - Axions: hypothetical, very light particles proposed to solve a puzzle in particle physics and considered a dark matter candidate.
- Dark matter: unseen matter that makes up most of the mass in galaxies; here it is modeled as an oscillating axion field.
- Photon-axion conversion: the process by which an axion turns into a photon in a magnetic field, and the reverse.
- Resonance: a condition where two effects match up so a signal is strongly amplified, similar to a swing pushed at the right rhythm.
- Dispersion relation mismatch: photons and axions travel with different energy-momentum relations, so they normally convert poorly; the dark matter background is said to compensate for this difference.
- Stellar axions: axions expected to be produced in the hot cores of stars, here those of M82.
- NuSTAR: a NASA X-ray space telescope whose existing data are reanalyzed.
- Coupling limits: upper bounds on how strongly axions interact with photons, given as constraints over a range of masses. · level: research-level

<details><summary>Original abstract</summary>

An oscillating axion dark matter (DM) background can enhance the conversion of another relativistic axion into photons when traversing a magnetic field. The DM background rotates photon polarization relative the magnetic orientation, which compensates the photon's and the propagating axion's dispersion relation mismatch. We relate this mechanism to Axion Magnetic Resonance (AMR) and apply it to stellar axions in the starburst galaxy M82. We analyze its enhancement to the resulting X-ray signals while accounting for the finite magnetic domain size, dark matter coherence length, DM density morphology, plasma profiles, and the detector response. We derive strong constraints using existing X-ray data from NuSTAR. We show that this resonant conversion can lead to $\mathcal O(10^2)$ enhancement in the photon-axion conversion probability, improving the upper limits on axion's photon coupling over part of the mass range where ordinary conversion is suppressed. We also show that this type of resonance predicts distinctive features in the hard X-ray spectrum, which is moderately favored by the data over the background only model, yet it is currently still consistent with statistical fluctuations.

</details>

## Nuclear physics

### [Elastic polar oscillations and nuclear parameters](https://arxiv.org/abs/2611.31819)
*Hajime Sotani* · `astro-ph.HE` · arXiv:2611.31819v1 · relevance 0.12

- **In one sentence**: A review of how crustal elasticity shapes neutron-star polar oscillation modes (s- and i-modes), and how their frequencies, if observed in short gamma-ray burst precursors, could constrain nuclear saturation parameters K0 and L via fitting formulas that depend on stellar compactness.
- **In plain words**: Neutron stars are extremely dense stellar remnants, and they can ring like a bell with several vibration patterns. This paper summarizes earlier work on the vibrations that depend on the star's solid crust, and suggests that if such vibrations were detected (possibly in the bursts of gamma rays that come just before a merger of two neutron stars), their frequencies could reveal properties of the dense matter. The authors report that, for a given set of nuclear properties, certain scaled frequencies follow a formula depending mainly on how compact the star is.
- **Why it matters**: Reading a neutron star's vibrations is one of the few proposed ways to learn about nuclear matter under conditions that cannot be recreated in laboratories, so it links astrophysics and nuclear physics. The text is a summary of previous studies and says observations are still challenging, so the practical payoff is uncertain and depends on future detections.
- **Background needed**: - Neutron star: a collapsed star roughly 1.4 times the Sun's mass packed into about 20 km across, with a solid crust over a fluid core.
- Oscillation modes: patterns in which the star vibrates, like the notes of a struck bell. Named families include fundamental, pressure, gravity, shear, and interface modes; s- and i-modes involve the crust's elasticity.
- Short gamma-ray burst: a brief, intense flash of gamma rays, here thought possibly to be preceded by signals from a binary neutron star merger.
- Asteroseismology: inferring a star's interior structure from its oscillation frequencies, as seismologists do with earthquakes.
- Equation of state (EOS): the relation between pressure and density of dense matter.
- Nuclear saturation parameters: properties of ordinary nuclear matter, here the incompressibility K0 (resistance to squeezing) and the slope L of nuclear symmetry energy.
- Compactness: the ratio of a star's mass to its radius (a dimensionless measure of how strongly gravity compresses it). · level: research-level

<details><summary>Original abstract</summary>

Owing to the elasticity of a neutron star, the shear and interface modes are excited, in addition to the fundamental, pressure, and gravity modes. While direct observations of the oscillation spectrum remain challenging, potential resonance signatures from these modes could be manifested in the precursors of short gamma-ray bursts from binary neutron star mergers. If the oscillation spectrum is observed, this is a good opportunity to extract the physical properties through the technique of asteroseismology. In particular, we focus on the crustal elasticity and examine the $s$- and $i$-mode frequencies. We find that, for a given EOS specified by the nuclear saturation parameters, the radius-scaled $s$-mode frequencies and the mass-scaled $i$-mode frequencies can be expressed as a function of the stellar compactness, independently of the stiffness of the core EOS, at least when the EOS in a higher-density region can be characterized only by the specific constant sound velocity. Then, we could derive the fitting formula for the $s_i$-mode for $i=1-4$ and $i_1$-mode frequencies as a function of the stellar compactness and the combination of the incompressibility of symmetric nuclear matter, $K_0$, and the slope parameter for the nuclear symmetry energy, $L$. If the $s$- and/or $i$-mode oscillation frequencies were observed, one may get the relation between these properties by identifying the observed frequencies with specific modes, using our fitting formula, which offers useful insights into the nuclear saturation parameters and stellar properties. By combining the other observational data, it may be possible to narrow the parameter space of EOS parameters and stellar properties. We emphasize that this article summarizes the results presented in our previous studies and discusses their implications for neutron star seismology.

</details>

### [Softer charged-hadron spectra in Ne+Ne than in O+O collisions at the same multiplicity at $\sqrt{s_{\rm NN}} = 5.36$ TeV](https://arxiv.org/abs/2611.32516)
*Kishora Nayak* · `nucl-ex` · arXiv:2611.32516v1 · relevance 0.07

- **In one sentence**: Compares ATLAS charged-hadron transverse-momentum spectra in O+O and Ne+Ne collisions at equal charged-particle multiplicity (rather than equal centrality), finding Ne+Ne spectra softer, and tests the same procedure on Xe+Xe and Pb+Pb.
- **In plain words**: Heavy-ion collisions at the Large Hadron Collider smash nuclei together and spray out many particles. This paper asks whether the energy spread of those particles depends on how big the colliding nuclei are, once you compare collisions that produce the same number of particles. The authors find that neon-on-neon collisions give slightly gentler (softer) particle energy distributions than oxygen-on-oxygen collisions at the same particle count, and that this difference is modest and statistically significant under the stated uncertainties.
- **Why it matters**: If the collision region is larger at the same particle count, the particles should spread out less in momentum, which connects the observed shape to the geometry of the collision. This is a careful reanalysis of published ATLAS data; the text does not establish the cause beyond the proposed area explanation, and the significance depends on how systematic uncertainties are treated.
- **Background needed**: - Heavy-ion collisions: nuclei collided at very high energy (5.36 TeV per nucleon pair here) to create a hot, dense state of matter.
- Centrality: how head-on a collision is; 3-4% centrality means very central (near head-on) events.
- Charged-particle multiplicity: the number of electrically charged particles produced in one collision, used as a proxy for collision size.
- Transverse momentum (pT): the sideways momentum of a particle relative to the beam; its spectrum is the distribution of pT values.
- Mean pT and "stretch factor": a summary average, and a single scaling of the pT axis that makes one spectrum match another.
- Pseudorapidity: a measure of angle from the beam direction; "forward" means closer to the beam.
- Standard deviations (sigma): how many uncertainty widths a difference lies from zero. · level: research-level

<details><summary>Original abstract</summary>

Charged-hadron spectra measured by the ATLAS Collaboration in O+O and Ne+Ne collisions at $\sqrt{s_{\rm NN}} = 5.36$ TeV are compared at the same charged-particle multiplicity instead of at the same centrality, to test whether the shape of the transverse-momentum spectrum at a given multiplicity depends on the size of the colliding system. At equal multiplicity, Ne+Ne collisions have a lower mean transverse momentum $\langle p_{\rm T}\rangle$ than O+O collisions. Without any spectral fit, the published $\langle p_{\rm T}\rangle$ values give a Ne+Ne/O+O ratio of 0.9822 at 3-4% centrality, 6.6 standard deviations below unity even if the O+O systematic uncertainties are taken as uncorrelated between centrality classes. At $0.4 < p_{\rm T} < 2$ GeV the Ne+Ne spectrum is described by the O+O spectrum with the transverse-momentum axis compressed by a single stretch factor, $\lambda_{\rm Ne/O} = 0.969$ in the 3-4% class. It lies 9.5 or 3.3 standard deviations below unity, depending on whether the common part of the O+O systematic uncertainties cancels between centrality classes. This ordering is expected if Ne+Ne collisions have a larger transverse area at the same multiplicity and a larger area gives a softer spectrum. The softening decreases towards peripheral collisions and is the same at forward pseudorapidity. In central collisions the spectral shape follows the centrality class more closely than the multiplicity. The same procedure is tested in Xe+Xe and Pb+Pb collisions.

</details>

## Quantum information and computing

### [On the concentration of the ambiguity function on centered balls](https://arxiv.org/abs/2611.31326)
*Fabio Nicola* · `math.FA` · arXiv:2611.31326v1 · relevance 0.20

- **In one sentence**: The paper proves that Gaussian functions maximize the L^2 concentration of the ambiguity function on every centered ball, up to time-frequency shifts and unimodular phase factors, using tools from quantum information theory.
- **In plain words**: The paper studies a mathematical tool that describes a signal's time and frequency content at once. It asks how much of that tool's energy can be squeezed into a small region centered at the origin, and it shows that the bell-shaped Gaussian signal does this best. The argument borrows ideas from quantum information theory.
- **Why it matters**: The result sharpens a known kind of limit on how tightly a signal can be localized in time and frequency together, which matters for signal processing and harmonic analysis. The text does not say what further applications it has, so its wider importance is uncertain from this summary alone.
- **Background needed**: - The ambiguity function: a two-variable function of time shift and frequency shift that encodes a signal's time-frequency structure.
- L^2 concentration: the fraction of a function's total energy (squared size) that lies inside a given region.
- Centered ball: a disk-like region around the origin in the time-frequency plane.
- Gaussian: the bell-shaped function, which is the usual extremal example in uncertainty-type inequalities.
- Time-frequency shifts and unimodular constants: moving a signal in time or frequency, and multiplying by a complex phase of size one; these do not change the concentration, so they are ignored in the statement.
- Quantum information theory: the field that studies information in quantum systems; the paper says its ideas were used in the proof. · level: research-level

<details><summary>Original abstract</summary>

We show that the Gaussian uniquely maximizes the $L^2$ concentration of the ambiguity function on every centered ball, up to time-frequency shifts and multiplication by a unimodular constant. The proof relies on ideas from quantum information theory.

</details>

### [Benchmarking Quantum Machine Learning for Power-System Attack Detection: Evaluation Choices Can Decide the Outcome](https://arxiv.org/abs/2608.15617)
*Md Rezwanul Islam, ASM Shihavuddin* · `cs.LG` · arXiv:2608.15617v2 · relevance 0.18

- **In one sentence**: A benchmark comparing two quantum and six classical machine-learning detectors for power-grid cyberattacks finds that evaluation choices such as row-level versus whole-file splits, and per-model attack design, can change the reported outcome.
- **In plain words**: The paper looks at whether quantum computing methods can spot cyberattacks on electric grids and gas pipelines better than ordinary computer methods. The authors ran two quantum and six classical detectors on public attack data under the same tuning effort. They found that how the test is set up, for example splitting data by individual rows instead of by whole files, can make a method look much better than it is, and that neither quantum detector was more accurate or consistently more robust on the grid and pipeline data.
- **Why it matters**: Quantum machine learning is being proposed for infrastructure security, so claims of advantage need careful testing. The paper's main point is methodological: small changes in evaluation design shifted results, which may matter for any benchmark claim in this area; the text does not show how widely these findings generalize beyond the datasets used.
- **Background needed**: - Machine learning detector: a program trained on labeled examples to flag attacks.
- Quantum machine learning: methods that run parts of a model on quantum hardware or simulated quantum circuits.
- Macro-averaged F1: a score balancing precision and recall across classes; chance is 0.50 for the binary task described.
- White-box attack: an attacker who knows the model's internals and can craft inputs against it; black-box and transfer attacks use a substitute model instead.
- Row-level vs file-level split: whether test rows can come from the same recordings as training rows (which inflates scores) or whether whole files are held out.
- Random label flips: deliberately corrupting some training labels to test robustness.
- Gradient-based attack: an attack that uses the model's gradients; tree models do not admit this, so their attacked scores are only upper bounds. · level: research-level

<details><summary>Original abstract</summary>

Quantum machine learning is proposed to detect grid cyberattacks, but no study we could read tests quantum and classical detectors under white-box, transfer, and black-box attacks and random label flips in one protocol. We compare two quantum and six classical detectors on public grid-attack data under equal tuning budgets. Our main finding: evaluation choices can decide the outcome. On these data, seven choices each changed a reported result with model families fixed. Row-level splits inflate our best score by 0.31 macro-averaged F1 over held-out files, where matched-dimensionality classical and quantum models barely clear chance. Under its own white-box attack the quantum kernel's score falls from 0.56 to 0.01 (chance 0.50), while a transferred attack in the same run leaves 0.52. Trees admit no gradient-based white-box attack, so their attacked scores are upper bounds. These attack results use eight-dimension detectors under row-level splits. On gas-pipeline and simulated-grid data, neither quantum detector is more accurate or consistently more robust; three of the seven choices reproduce fully on gas data with one pressure feature log-scaled (two within noise), and none of the four checked on the grids does. Benchmarks should hold out whole files and give every model its own attack where possible. We release code and checklist.

</details>

## Optics and atomic physics

### [Integrated lasing and dual-band gain in neodymium-implanted silicon nitride](https://arxiv.org/abs/2611.32935)
*Jan de Haan, Arturo Fern\'andez Gamez, Nina Zdravkovi\'c et al.* · `physics.optics` · arXiv:2611.32935v1 · relevance 0.15

- **In one sentence**: Demonstrates neodymium-ion-implanted LPCVD silicon nitride waveguide amplifiers with gain in two bands near 920 nm and 1100 nm, and a ring laser built on the same platform, fabricated on 200 mm commercial wafers.
- **In plain words**: This paper is about building tiny laser circuits on a chip for light near 1 micrometer, a wavelength used in quantum technology, precise measurement, and sensing. The authors took standard silicon nitride chip waveguides made on a commercial wafer, implanted neodymium ions (a rare-earth element) into individual chips to add light-amplifying material, and tested them. They report that the amplifiers boost light in two wavelength bands, and that a ring-shaped resonator on the chip lases.
- **Why it matters**: Making lasers on standard chip-manufacturing lines could make them smaller and easier to produce at scale, which matters for quantum and sensing devices. The text does not report output power, efficiency, or how stable the lasers are, so the practical significance is still open.
- **Background needed**: - Photonic integrated circuit: a chip that guides light through tiny channels (waveguides), similar to electrical wiring for light.
- Silicon nitride (LPCVD): a common chip material deposited from gas at low pressure; a standard, mass-producible platform.
- Rare-earth gain: rare-earth ions such as neodymium emit light at specific wavelengths when pumped with energy, which can amplify light passing through them.
- Ion implantation: firing ions into a material at high energy to add them to its surface layer.
- Waveguide amplifier: a guided-light channel that increases the signal passing through it.
- Ring resonator: a looped waveguide that selects specific wavelengths; a laser cavity can be built from it.
- Lasing: the point where amplification overcomes losses and the device emits coherent light. · level: intermediate

<details><summary>Original abstract</summary>

Lasers at wavelengths near 1 micrometer are used in quantum technologies, precision metrology, and sensing. Rare-earth gain at these wavelengths in photonic integrated circuits can reduce the size and enable the scalable fabrication of these lasers. We fabricate neodymium-based integrated waveguide amplifiers and a ring laser using neodymium-implanted LPCVD silicon nitride. The photonic integrated circuits were fabricated on a 200 mm commercial wafer platform, and individual dies were implanted with neodymium ions. We show that the amplifiers provide gain in two bands around wavelengths of 920 nm and 1100 nm, and we show lasing in a ring resonator. This demonstrates that neodymium-implanted LPCVD silicon nitride is a suitable gain material for integrated lasers.

</details>

### [Temporal Soliton Waves in Modern Fiber Laser Systems](https://arxiv.org/abs/2611.31799)
*Shilong Liu, Boris Malomed* · `physics.optics` · arXiv:2611.31799v1 · relevance 0.10

- **In one sentence**: A survey chapter reviewing theory, experiments, generation and control methods for temporal soliton families (dissipative solitons, soliton molecules, dispersion-managed solitons) in mode-locked fiber lasers.
- **In plain words**: This is an overview chapter about tiny, self-sustaining pulses of light that keep their shape as they travel through optical fiber inside a laser. The chapter gathers the underlying theory, experimental results, and ways to create, measure, and steer these pulses. It also covers newer work that uses machine learning to help control them.
- **Why it matters**: Stable ultrashort light pulses are used in precision measurement, communications and materials processing, so a consolidated review of how they form and how they can be controlled is useful for people entering the field. The text does not indicate any single new result, and its claims about recent progress are only described at a general level.
- **Background needed**: - Mode-locked laser: a laser that emits a train of very short light pulses instead of a steady beam.
- Optical fiber: a thin glass strand that guides light; the laser cavity is typically a loop of it.
- Soliton: a pulse that holds its shape because the fiber's nonlinear response balances its tendency to spread out.
- Dispersion: the effect where different colors of light travel at slightly different speeds, stretching pulses.
- Gain and loss: light is amplified in the fiber and lost elsewhere; "dissipative" solitons depend on this balance.
- Soliton molecules: several pulses locked together at fixed spacing, like a bound pair.
- Breathing state: a pulse that periodically changes its width or energy while traveling.
- Machine learning control: using trained algorithms to adjust laser settings to reach desired pulse behavior. · level: research-level

<details><summary>Original abstract</summary>

This chapter provides a comprehensive survey of temporal soliton-wave in modern fiber systems. Temporal soliton waves constitute a broad class of nonlinear localized structures in modern fiber laser systems, arising from different balances among dispersion, nonlinearity, gain, loss, spectral filtering, and various forms of cavity coupling. We review the underlying theory, basic experimental findings, and practical methods for the generation, real-time characterization, and active control of soliton families, with a particular focus on recent progress reported for mode-locked fiber-laser platforms. The families covered in the chapter include dissipative solitons, soliton molecules (bound states), and dispersion-managed solitons. For each species, we focus on the pulse energy, duration, stationary and breathing states, and emerging intelligent (machine-learning-assisted) control strategies.

</details>

## Fluids and plasma

### [Toward divertor plasma detachment in pure D-T plasma in fusion reactor with H-mode-like plasma confinement](https://arxiv.org/abs/2611.31616)
*S. I. Krasheninnikov, R. D. Smirnov, M. V. Umansky* · `physics.plasm-ph` · arXiv:2611.31616v1 · relevance 0.09

- **In one sentence**: Analytical estimates of the separatrix density and scrape-off-layer heat flux conditions needed for ultimate divertor plasma detachment under H-mode confinement in pure deuterium, tritium, or D-T plasmas, checked against present tokamaks and AUG data.
- **In plain words**: The paper looks at how to cool down the hot exhaust plasma in a fusion reactor before it damages the walls. The divertor is the part of the reactor that catches this exhaust, and "detachment" means the plasma there cools enough to pull away from the target plates. The authors estimate the conditions under which this can happen while the core still runs in a high-performance mode, and find it is reachable on some current machines but would need denser plasma than the empirical density limit in future reactors such as ITER, ARC and EU-DEMO.
- **Why it matters**: Divertor heat load is a central obstacle to designing a practical fusion power plant, so a clear statement of the density and heat-flux conditions for detachment helps frame reactor design. The text suggests possible routes (operating above the density limit, turbulence-broadened heat flux width, reduced parallel heat flux in long-leg divertors), but these are proposals described in the abstract, and the text does not show how well they would work in practice.
- **Background needed**: - Tokamak: a doughnut-shaped magnetic fusion device that confines hot plasma.
- Divertor: the exhaust region where charged particles and heat are directed onto target plates.
- Scrape-off layer and separatrix: the thin edge layer of plasma outside the confined core, and the boundary between core and edge.
- Detachment: a state where the plasma in front of the target cools and loses its power to the target, reducing damage.
- H-mode: a high-confinement operating regime with better energy containment.
- Empirical density limit: an observed upper limit on plasma density beyond which confinement typically degrades.
- D-T: the deuterium-tritium fuel mix used in fusion reactors.
- AUG: ASDEX Upgrade, a German tokamak where detachment was achieved in pure deuterium. · level: research-level

<details><summary>Original abstract</summary>

The conditions between the separatrix plasma density and the heat flux into the scrape-off layer region allowing reaching an ultimate divertor plasma detachment with H-mode confinement in pure hydrogen (deuterium or the mixture of deuterium and tritium) plasma are obtained. Estimates for a number of present-day tokamaks show that this regime is accessible at separatrix plasma densities below or around the empirical density limit. Moreover, they are in reasonable agreement with the data from the AUG tokamak, where detachment was reached in pure deuterium plasma. However, in future reactors, such as ITER, ARC, and EU-DEMO, it would require densities exceeding this empirical density limit. Therefore, additional measures are needed for future reactors, such as operation above the density limit, which, according to recent experimental data, may not be a hard operational boundary, turbulence induced broadening of the heat flux width and reduction of the parallel heat flux in the long legs of advanced divertor configurations. Their successful implementation would open the possibility for a more efficient reactor design.

</details>

### [The effects of closure parameter on the properties of kinetic range plasma turbulence](https://arxiv.org/abs/2611.31769)
*Jago V. H. Edyvean, Andrea F. Irwin, Tulasi N. Parashar* · `physics.plasm-ph` · arXiv:2611.31769v1 · relevance 0.09

- **In one sentence**: A numerical study of how the free "closure parameter" in a 10-moment fluid model of plasma turbulence changes heating of ions versus electrons, across artificial ion-electron mass ratios.
- **In plain words**: Plasmas such as the solar wind are too costly to simulate with the most detailed kinetic methods, so researchers use simpler fluid approximations that still track some particle behaviour. This paper examines how one tunable setting in such an approximation, the "closure parameter," changes the way turbulent energy is shared between the two charged species, ions and electrons. The authors report that the choice of this setting affects the heating of each species, and that the effect is strongest when the ion-to-electron mass ratio is artificially low and shrinks as it approaches the real value.
- **Why it matters**: Knowing how much energy goes into ions versus electrons matters for explaining the temperatures observed in the solar wind, but the text suggests that results from this fluid model may depend on a modelling choice rather than on physics alone. The text does not say how well the model matches spacecraft observations, so its relevance to real plasmas is not established here.
- **Background needed**: - Plasma: a gas of charged particles (ions and electrons), common in space and fusion devices.
- Kinetic vs fluid description: kinetic methods track the full distribution of particle velocities; fluid methods track averaged quantities such as density, flow and pressure, which is cheaper.
- Moments: successive averages of the particle velocity distribution (density, velocity, pressure, heat flux). A "10-moment" model keeps moments up to second order.
- Closure: an approximation for the higher moments (here the heat flux) so the set of equations can be solved.
- Closure parameter: a free number in that approximation, chosen by the modeller.
- Mass ratio: ion mass divided by electron mass; simulations often use smaller values than reality for computational reasons.
- Compressive vs incompressive turbulence: fluctuations that change plasma density/pressure versus those that mainly swirl without compressing it. · level: research-level

<details><summary>Original abstract</summary>

Simulations of plasmas such as the solar wind require an accurate representation of kinetic physics given the lack of frequent collisions. Fully kinetic treatments are computationally expensive and necessarily confine simulations to small domain sizes. A good compromise is to utilise higher-order fluid-moment models such as the 10-moment model. This model retains all physics up to the second moment, with the moment hierarchy closed by approximating the heat flux. One choice is to use a model for the divergence of the heat flux, $\partial_m q_{ijm} \approx v_t |k_0|(\mathbf{P}_{ij}-p\delta_{ij})$, with a free parameter $k_0$, called the ``closure parameter''. We study the effects of this closure parameter on the properties of turbulence, combined with artificial ion-electron mass ratios. We show that the heating of the two plasma species is affected by the choice of the closure parameter. For all combinations of closure parameters, the relative compressive and incompressive heating rates are affected even for realistic mass ratios. The effects are more prominent for lower mass ratios and diminish when approaching realistic mass ratios.

</details>

## Biological physics

### [Geometry and topology of DNA defects](https://arxiv.org/abs/2611.32850)
*A. Fassino, E. Carlon, D. Marenduzzo* · `cond-mat.soft` · arXiv:2611.32850v1 · relevance 0.09

- **In one sentence**: The paper defines a geometric order parameter (a backbone-to-base polar vector plus a base-orientation quaternion) to classify DNA defects as flips, stacking defects, or composites, and examines their occurrence in real structures and in biased molecular dynamics simulations.
- **In plain words**: DNA is normally a tidy double helix, but its strands can be locally disturbed by damage, by proteins sitting on it, or by enzymes such as RNA polymerase. This paper gives a precise geometric way to describe these local disturbances and how they change over time. The authors combine this description with computer simulations and with analysis of experimentally determined DNA structures.
- **Why it matters**: A quantitative, shared description of defects could help connect the shape of DNA to its chemical function, and the authors suggest it could be extended to RNA and nucleosome arrays. The text does not show how far these applications would go, so their practical value remains to be tested.
- **Background needed**: - DNA is a double helix of two strands; each strand has a sugar-phosphate backbone and attached bases (A, T, G, C).
- Normally the bases stack neatly on top of each other and point in a consistent direction relative to the backbone.
- A "defect" here means a local departure from that regular arrangement, such as a base flipping out or bases stacking imperfectly.
- A "polar vector" is an arrow with a direction, here running from backbone to base; a "quaternion" is a compact mathematical way to encode 3D orientation.
- Atomistic simulations model every atom and its motion; biased molecular dynamics pushes the system toward a chosen deformation to study it. · level: research-level

<details><summary>Original abstract</summary>

DNA defects arise frequently, either as a result of damage, protein binding or the action of molecular enzymes such as an RNA polymerase. Here we combine geometry, atomistic simulations and an analysis of real DNA structures to provide a quantitative characterisation of DNA defects and their dynamics. The composite order parameter describing defects geometrically is a backbone-to-base polar vector, together with a quaternion capturing 3D base orientation in a single strand. There are three types of defects: flips of the polar vector, stacking defects of bases, and composite defects encompassing both. All types of defects feature in realistic structures for DNA and have functional relevance. Additionally, biased molecular dynamics simulations of DNA with an imposed elastic deformation form flip or stacking defects whose abundance and dynamics strongly depend on sequence and type of deformation. Our results provide a link between geometry and biochemistry, and could also be applied, for instance, to identify defects in RNA molecules and nucleosome arrays.

</details>

### [Lattice models of chiral random motion: A short review](https://arxiv.org/abs/2611.32743)
*E. Kalz, J. Wojcik, N. Sherf et al.* · `cond-mat.stat-mech` · arXiv:2611.32743v1 · relevance 0.06

- **In one sentence**: A short review that frames lattice random walks with a rotational (chiral) bias around a memory-carrying internal state, using the recently introduced chiral random walk as a template and linking persistent, chiral, run-and-tumble and cyclic walks, odd diffusion in environments, and spiral self-avoiding walks.
- **In plain words**: This review looks at random movement on a grid where the walker has a built-in tendency to turn one way, as with bacteria that swim in circles near surfaces or charged particles bent by a magnetic field. The authors argue that on a lattice this sideways bias only works if the walker remembers something about its recent direction, and they organise many scattered earlier models around that idea. The text describes the framework and where the memory shows up: in the walker, the surrounding environment, and the path traced out.
- **Why it matters**: Chiral random motion appears in biology, active matter and magnetic transport, and lattice models are simple enough to solve exactly, so a common framework could help researchers in several fields see related work. The text does not report new experimental results, and its practical reach beyond these communities is not stated.
- **Background needed**: - A random walk is a path built from repeated random steps; diffusion is its large-scale spreading.
- A lattice is a regular grid of points that a walker hops between.
- Mean-squared displacement measures how far, on average, a walker has spread from its start.
- Chirality means a systematic left or right rotational bias.
- The diffusion tensor describes how spreading depends on direction; an antisymmetric part produces sideways (odd) transport that does not change the spreading distance.
- Persistent walks keep their heading for a while; run-and-tumble motion alternates straight runs with random reorientations, as in E. coli.
- Self-avoiding walks are paths that never revisit a site. · level: intermediate

<details><summary>Original abstract</summary>

Chirality, a systematic rotational bias, is ubiquitous in many random motion patterns, from bacteria cells, that swim in circles near surfaces and spinning colloids, to charged particles diffusing under the influence of magnetic fields. In two dimensions, chirality renders random transport \textit{odd}: the diffusion tensor acquires an antisymmetric part that leaves the mean-squared displacement invariant but modifies fluxes and boundary currents. Lattice models for random motion are a natural setting to study chirality, since they are exactly solvable, connect directly to heterogeneous media, cellular automata, and programmable robots, and in discrete time admit fully chiral limits with a localised bulk and edge transport. Lattice walks with a rotational bias have been introduced in different communities several times since 1960, yet without a common language or conceptual connection between them. Here we review these models from the perspective that on the lattice, chirality requires memory. Taking the recently introduced chiral random walk model as a template, we describe the walker with an internal degree of freedom. With a chiral biased updating rule, the full diffusion tensor of this chiral walker turns odd. Within this picture, we can unite persistent and chiral walks, run-and-tumble motion, and cyclic random motions in one framework. We discuss how the memory is followed into the environment; in Lorentz lattice gases, kinetic and rotor walks, and random odd environments; and into the path; in spiral self-avoiding walks.

</details>

## Climate, atmosphere and Earth

### [Evaluation of Machine-Learning Weather Models in Reproducing Mesoscale Tornado-Favorable Convective Environments](https://arxiv.org/abs/2611.31564)
*Yiding Luo (University of Washington), Rui Yuan (University of Washington), Shetian Xia (University of Washington) et al.* · `physics.ao-ph` · arXiv:2611.31564v1 · relevance 0.14

- **In one sentence**: This paper benchmarks three machine-learning weather models (Pangu-Weather, FengWu v1/v2, FuXi Weather) against reanalysis data on eight tornado-relevant parameters across ten Oklahoma tornado events and lead times of 24 to 168 hours.
- **In plain words**: Tornadoes form when specific atmospheric conditions line up, such as wind shear and warm, moist air near the ground. This study asks whether newer AI-based weather forecasting models can reproduce those conditions for ten past severe-tornado events in Oklahoma. It finds that performance varies by model, variable, and event: one model does better on a rotation-related measure, another on temperature and moisture measures, though it tends to exaggerate their strength, and forecasts lose accuracy for extremes and fine spatial detail as lead time grows.
- **Why it matters**: Machine-learning forecasts are being used operationally and are much cheaper to run than traditional models, but most were trained on coarse global data that may miss the small-scale conditions behind tornadoes. The paper suggests that headline forecast scores alone can hide model-specific biases and errors in extreme values, which matters for anyone relying on these tools for severe-weather guidance.</why>
<parameter name="background">- Numerical weather prediction (NWP): forecasting by solving physics equations on a grid of the atmosphere.
- Machine-learning (ML) weather models: systems trained on past data to predict the next atmospheric state; much faster to run than NWP.
- Reanalysis: a gridded reconstruction of past weather combining observations with a model, used here as both input and "truth."
- Grid spacing (0.25 degrees): roughly 25 km between grid points, too coarse to resolve many small storm features.
- Lead time: how far ahead the forecast goes (here 24 to 168 hours, i.e., 1 to 7 days).
- Storm-relative helicity: a measure of how much the wind rotates with height, linked to storm rotation.
- Cold pool: a pocket of cool air spreading out from a thunderstorm, often at the surface.
- Overprediction/extreme-value fidelity: whether a model gets the strength of the largest values right, not just the average pattern.</background>
<parameter name="difficulty">intermediate

<details><summary>Original abstract</summary>

Machine-learning (ML)-based weather prediction models have developed rapidly in recent years and are already being used in operational weather forecasting. These ML-based models' performance has exceeded that of traditional numerical weather prediction (NWP) methods in certain implementations, with substantially lower computational cost. However, most ML-based models were trained on global data at a horizontal grid spacing of 0.25 degrees, which may be too coarse to capture tornado-favorable parameters. The ability of these ML-based models to predict the parameters relevant for tornado-favorable convection remains unclear. Here, we compare the performance of three ML-based models, Pangu-Weather, FengWu (versions 1 and 2), and FuXi Weather, in forecasting ten distinct convective events associated with strong tornadoes that occurred in Oklahoma, USA. The proposed methodology incorporates five lead times, ranging from 24 to 168 h, for each event and uses reanalysis data as both model input and ground truth. We evaluate the models by forecasting eight tornado-relevant parameters and by conducting spatial and value-consistency checks between model outputs and ground truth. Performance varies across parameters, models, and events. Pangu-Weather performs well for positive storm-relative helicity, while FuXi Weather performs well for several thermodynamic parameters, albeit with some overprediction of magnitude. Increasing lead time is associated with loss of extreme-value and spatial-structure fidelity. In the Global Forecast System (GFS) case study, ML-based models retain convective signals at longer lead times but poorly represent fine-scale structures such as cold pool-like features. These findings indicate that model-specific biases and spatial extremes should be assessed alongside domain-wide forecast scores.

</details>

### [Critical ocean physics on the edge of AMOC instability](https://arxiv.org/abs/2611.31448)
*Reyk B\"orner, Anna S. von der Heydt, Robbin Bastiaansen et al.* · `physics.ao-ph` · arXiv:2611.31448v1 · relevance 0.08

- **In one sentence**: In a 1-degree global ocean model, the authors compute an unstable saddle equilibrium (an "AMOC edge state") that sits on the boundary between AMOC recovery and collapse, and analyze North Atlantic freshwater and heat balances near it.
- **In plain words**: The Atlantic overturning circulation is a large system of ocean currents that carries warm water north and cold, dense water south, and climate models suggest it may weaken as the planet warms. This paper asks whether that weakening would be temporary or would tip into a collapse that does not reverse. The authors used a global ocean model to find a special, unstable state that marks the dividing line between the circulation recovering and collapsing. They report that near this state, warming and saltiness effects on surface water density roughly cancel out, and that surface density loss lines up with recovery while density gain lines up with collapse.
- **Why it matters**: Whether the Atlantic circulation can recover or will tip into collapse matters for regional climate and sea level, so a physical marker of the tipping boundary is useful. The authors suggest the regional net surface buoyancy flux (a measure of how much the surface water is made lighter or denser) could serve as an early indicator, though the text does not test this as a forecasting tool.
- **Background needed**: - AMOC: the Atlantic Meridional Overturning Circulation, a conveyor-like system of ocean currents that moves heat northward in the Atlantic.
- Deep water formation: surface water in cold regions (here the Nordic Seas) becomes dense enough to sink, driving the circulation.
- Buoyancy flux: the rate at which surface water is made lighter or denser by heat exchange (thermal) and by salt or freshwater exchange (haline).
- Tipping transition vs. transient response: a tipping transition is a shift to a different state that does not reverse when conditions return; a transient response reverses once forcing eases.
- Saddle equilibrium: a steady state that is unstable; small nudges push the system toward either recovery or collapse, so it marks the boundary between them.
- Edge state: the unstable state lying on the boundary between the two basins of attraction.
- Global ocean model at 1-degree resolution: a simulation whose grid cells are about 1 degree across. · level: research-level

<details><summary>Original abstract</summary>

The Atlantic Meridional Overturning Circulation (AMOC) is expected to weaken under global warming, but whether this signifies a transient response or a tipping transition remains unclear. Distinguishing between these cases requires a physical understanding of the boundary separating ocean states leading to AMOC recovery from those leading to collapse. In a global ocean model with 1{\deg} resolution, we compute an AMOC edge state -- an unstable saddle equilibrium that anchors this instability boundary. The edge state maintains weak overturning sourced by marginal deep water formation in the Nordic Seas. Analyzing the North Atlantic freshwater and heat balances that govern the edge state dynamics, we show that near the edge state, thermal and haline components of the surface buoyancy flux approximately compensate. Surface buoyancy loss (gain) coincides with AMOC recovery (collapse). Our findings support using the regional net surface buoyancy flux as an indicator for the onset of AMOC tipping.

</details>

## Cosmology

### [Learning to find cosmic filaments with graph neural networks](https://arxiv.org/abs/2611.31494)
*Alexis Tastet, Daniela Gal\'arraga-Espinosa, Leander Thiele* · `astro-ph.CO` · arXiv:2611.31494v1 · relevance 0.17

- **In one sentence**: A generative model built from flow matching and graph neural networks learns to produce probabilistic samples of cosmic filament networks from sparse galaxy tracer positions.
- **In plain words**: Astronomers want to map the large-scale threads of matter, called cosmic filaments, that link galaxy clusters together. Galaxy catalogs give only scattered points, so the exact shape of these threads cannot be read off directly. This paper trains a machine-learning model to generate many plausible filament layouts consistent with the galaxies, and reports that the outputs match key statistics of the target filaments while varying across samples.
- **Why it matters**: Filaments are a major part of the cosmic web, and a method that reports uncertainty about them could matter for future galaxy surveys. The text describes this as a first step, so its practical value for real survey data is not yet shown.
- **Background needed**: - Cosmic web: the large-scale pattern of galaxies, filaments, walls and voids in the Universe.
- Galaxy survey: a catalog of galaxy positions, which is incomplete and sparse.
- Filament finding: algorithms that trace these threads through galaxy positions.
- Generative model: a model that learns a distribution and can produce new samples from it, here giving many possible filament networks.
- Flow matching: a training method that learns to transform random noise into samples resembling the target data.
- Graph neural network: a neural network operating on nodes and connections, suited to networks of points.
- Conditional model: one whose outputs depend on given inputs, here the observed tracers. · level: research-level

<details><summary>Original abstract</summary>

Inferring the large-scale structure of the Universe from galaxy surveys is a fundamental challenge in cosmology. In particular, cosmic filaments form an extended and geometrically complex network whose underlying structure cannot be reconstructed from discrete galaxy catalogs without uncertainty. We investigate a generative approach to filament finding based on flow matching and graph neural networks. The learned model reproduces key statistical properties of the target filament distribution while generating a distribution over possible filament configurations, demonstrating its ability to model uncertainty. Our work provides a first step towards probabilistic inference of the cosmic web directly from galaxy surveys. More broadly, these results demonstrate the potential of conditional generative models for reconstructing filament-like structures from sparse observational tracers.

</details>

### [Resolving the Hubble Tension at $0.1\sigma$ with Early Dark Energy: Key Role of the Highest-redshift Galaxies from JWST Observations](https://arxiv.org/abs/2611.32552)
*Guo-Hong Du, Tian-Nuo Li, Jing-Fei Zhang et al.* · `astro-ph.CO` · arXiv:2611.32552v1 · relevance 0.15

- **In one sentence**: A cosmology paper arguing that early dark energy (axion EDE) combined with CMB, DESI BAO, and JWST high-redshift galaxy UV luminosity functions can bring the inferred Hubble constant to within 0.1σ of SH0ES, with a running of the spectral index (α_s) pushing H0 higher still.
- **In plain words**: The universe is expanding at a rate that different measurement methods disagree on: measurements from the early universe give a lower value than direct measurements from nearby stars and galaxies (SH0ES). This paper tests whether a modified model with an extra, short-lived "early dark energy" component, combined with new JWST counts of very distant galaxies, can close that gap. The authors report that it can, with the result depending strongly on how the most distant galaxies are counted and on how the model's power spectrum is allowed to vary with scale.
- **Why it matters**: The Hubble tension is one of the most discussed open problems in cosmology, and the paper ties it to new JWST observations of early galaxies and to the settings of the primordial matter spectrum. It is worth watching because the result depends on modelling choices, so it is an interesting proposal rather than a settled resolution; whether it holds up will depend on independent data and reanalyses.
- **Background needed**: - Hubble constant (H0): the present expansion rate of the universe, in km/s per megaparsec.
- Hubble tension: early-universe measurements (CMB) and local measurements (SH0ES, using nearby Cepheid stars and supernovae) give different H0 values.
- Early dark energy (EDE): a hypothetical extra component active briefly before recombination, which changes the expansion history; the axion version is one specific model.
- CMB: the cosmic microwave background, the afterglow of the early universe.
- DESI baryon acoustic oscillations (BAO): a standard-ruler measurement of galaxy clustering from the DESI survey.
- JWST UV luminosity function: counts of galaxies by ultraviolet brightness at high redshift (very distant, early galaxies); converting these counts to physical quantities requires assuming a reference cosmology.
- Spectral index n_s and running α_s: describe how the primordial density fluctuations vary with physical scale; α_s measures the scale dependence of that tilt.
- σ (sigma): the standard unit of statistical significance; 0.1σ means the two values agree very closely. · level: research-level

<details><summary>Original abstract</summary>

We show that the Hubble tension can be resolved at the $0.1\sigma$ level within the early dark energy (EDE) framework, with the highest-redshift galaxies from the JWST observations playing a key role. By accounting for the reference cosmologies of the JWST ultraviolet luminosity function measurements and combining them with cosmic microwave background (CMB) and DESI baryon acoustic oscillation data, we obtain $H_0=72.76\pm1.00~\mathrm{km\,s^{-1}\,Mpc^{-1}}$ in the axion EDE model, in excellent agreement with SH0ES at the $0.1\sigma$ level. We find that the enhanced galaxy abundances at $z=11$ and $12.5$ play a key role in driving this result. These observations favor stronger small-scale matter power, which can be accommodated by increasing the primordial scalar spectral index $n_{\rm s}$. Under the CMB constraints, the positive correlations among $n_{\rm s}$, $f_{\rm EDE}$, and $H_0$ lead to a higher inferred $H_0$. Allowing additional scale dependence in the primordial power spectrum through $\alpha_{\rm s}$ yields a positive running at more than $4\sigma$, further increasing $H_0$ to $73.75\pm1.04~\mathrm{km\,s^{-1}\,Mpc^{-1}}$, with its value even exceeding the SH0ES measurement. These results reveal how high-redshift small-scale structure observations influence the inferred $H_0$ through the interplay between the primordial power spectrum and EDE parameter degeneracies.

</details>

## Galaxies

### [Euclid: Discovery of a quasar at z = 8.13 hosting a 360-million-solar-mass black hole](https://arxiv.org/abs/2611.31385)
*J. Wolf, S. Belladitta, D. Yang et al.* · `astro-ph.GA` · arXiv:2611.31385v1 · relevance 0.19

- **In one sentence**: Discovery and spectroscopic confirmation of quasar J1504+6252 at z = 8.13, the first quasar confirmed beyond z = 8, with a black hole estimated at log10(M/Msun) of roughly 8.3–8.9 from H-beta and Mg II line widths.
- **In plain words**: This paper reports a very distant quasar, a bright object powered by a supermassive black hole, seen as it was about 630 million years after the Big Bang. The object was first picked out in images from the Euclid space telescope and then confirmed with several large telescopes, including JWST. The authors estimate its central black hole holds several hundred million times the Sun's mass, which is surprisingly large for such an early time.
- **Why it matters**: It moves the record for the most distant confirmed quasar by about 39 million years, and it raises the question of how black holes grew so massive so early. The text suggests that either very heavy starting seeds or unusually efficient early growth would be needed, and that similar objects may still be undiscovered; how general that conclusion is remains to be seen.
- **Background needed**: - Quasar: an extremely bright galactic core where a supermassive black hole is actively pulling in gas.
- Redshift (z): how much light from a distant object has been stretched by cosmic expansion; larger z means further away and earlier in time. z = 8.13 is roughly 630 million years after the Big Bang.
- Broad emission lines: light emitted by fast-moving gas near the black hole; their width is used to estimate the black hole's mass.
- Single-epoch calibration: an empirical formula that converts one spectrum's line width and brightness into a mass estimate, which carries large uncertainty (here about ±0.4 in log10).
- Eddington ratio: how fast a black hole is feeding compared with the theoretical maximum; 'sub-Eddington' means feeding slower than that limit.
- Reionisation era: the period when the first luminous objects ionised the hydrogen filling the universe.
- Seed: the initial black hole from which a supermassive one grows. · level: research-level

<details><summary>Original abstract</summary>

Quasars powered by rapid accretion onto supermassive black holes (SMBHs) have been uncovered deep into the first gigayear of cosmic history. We present the discovery of EUCL J150452.291+625224.39 (J1504+6252), selected from Euclid Wide Survey imaging and spectroscopically confirmed as the first quasar at z > 8 through observations with Keck, HST, LBT, and JWST. J1504+6252 exhibits the defining spectral signatures of archetypal quasars at lower redshift, including a luminous blue power-law continuum and broad permitted emission lines, indicating a classical broad-line region. JWST/NIRSpec G395M spectroscopy yields a systemic redshift of z = 8.129 +/- 0.005, corresponding to 630 Myr after the Big Bang and shifting the quasar redshift frontier by about 39 Myr (6% of the age of the Universe at that epoch). From H-beta and Mg II, we measured intrinsic broad-line-region FWHM of 3160 +/- 270 and 3740 (+160/-170) km/s, respectively. A widely used single-epoch H-beta calibration gives a reference black hole mass of log10(MBH/Msun) = 8.56 +/- 0.43. Applying a range of calibrations to both Mg II and H-beta yields log10(MBH/Msun) = 8.33-8.89 and Eddington ratios of 0.12-0.44. Assembling a black hole of several hundred million solar masses within the first few hundred million years, despite its currently sub-Eddington accretion rate, requires either a massive seed or sustained, highly efficient early growth. The discovery of a mature, sub-Eddington quasar at z > 8 suggests that substantially more luminous quasars hosting similarly massive black holes may remain to be discovered. Conversely, previously known reionisation-era quasars may represent the rapidly accreting end of a broader population of already massive black holes spanning a wider range of accretion states.

</details>

### [Tidally Induced Coda: Double Transients from Black Hole-Star Binary Encounters with Massive Black Holes](https://arxiv.org/abs/2611.31361)
*Konstantinos Kritos, Rosalba Perna* · `astro-ph.HE` · arXiv:2611.31361v1 · relevance 0.12

- **In one sentence**: Few-body scattering simulations (SpaceHub) of stellar-mass black hole–star binaries passing near a massive black hole, quantifying outcomes including a micro-tidal disruption event that yields a double flare, with fitted cross-section and time-delay formulae and event-rate estimates.
- **In plain words**: This paper studies what happens when a pair of objects, a black hole and a star orbiting each other, flies close to a much larger black hole at the centre of a galaxy. The huge black hole's pull can stretch the pair's orbit so much that the star is torn apart by its black hole partner. The debris then falls onto the large black hole, producing two bursts of light separated in time.
- **Why it matters**: The authors suggest the two-flare pattern, with a delay of months for a black hole of about a million solar masses, could be a distinctive signature for identifying these small disruption events. They estimate rates of a few to about 100 per year within 40 gigaparsecs, but the text does not show how well these rates would hold up against observations.
- **Background needed**: - Massive black hole (MBH): a black hole with a mass of roughly a million or more Suns, typically at galaxy centres.
- Stellar-mass black hole: a black hole formed from a dead massive star, a few to tens of Suns in mass.
- Binary: two objects orbiting each other.
- Tidal disruption event (TDE): a star torn apart by a black hole's gravity, whose debris lights up as a flare when it falls in. A micro-TDE (μTDE) is the same process where the tearing force comes from a companion black hole rather than the large one.
- Eccentricity: how stretched out an orbit is; extreme values mean a very elongated orbit.
- Few-body scattering experiment: a direct numerical simulation of a small number of gravitating bodies interacting over a close encounter.
- Cross section: an effective target area describing how likely an event is for a given encounter.
- Luminosity distance: the distance inferred from how bright a source appears. · level: research-level

<details><summary>Original abstract</summary>

Dense stellar environments surrounding massive black holes (MBHs) provide a natural setting for dynamical interactions that can produce transient electromagnetic and gravitational-wave sources. In particular, the tidal field of an MBH can strongly perturb binaries undergoing close encounters with it, driving their internal orbits to extreme eccentricities. Here, we investigate the outcomes of such interactions for binaries composed of a stellar-mass black hole (BH) and a star. Using direct few-body scattering experiments with the code SpaceHub, we explore hyperbolic encounters between BH-star binaries and MBHs. We systematically quantify the probabilities of different dynamical outcomes as functions of the binary orbital parameters and MBH mass, with particular emphasis on a channel in which the tidally induced eccentricity triggers a micro-tidal disruption event ($\mu$TDE), as the star is disrupted by its BH companion, followed by accretion of the stellar debris onto the MBH. We derive fitting formulae for the $\mu$TDE cross section and for the time delay between the two resulting flares, finding that the latter can be a few months for an MBH of $10^6\,M_\odot$. These double transients offer a distinctive observational signature of $\mu$TDEs. We estimate event rates ranging from a few to $\sim 100\,{\rm yr}^{-1}$ within a luminosity distance of $40\,{\rm Gpc}$.

</details>

## Exoplanets and planetary science

### [From residuals to warps: Probing disk geometry with gas kinematics](https://arxiv.org/abs/2611.31408)
*C. N. Kimmig, G. P. Rosotti, A. J. Winter et al.* · `astro-ph.EP` · arXiv:2611.31408v1 · relevance 0.17

- **In one sentence**: Using CO line kinematics from synthetic radiative-transfer maps, this paper tests when residuals from a Keplerian disk model can recover the three-dimensional warp shape of protoplanetary disks, and where the method fails.
- **In plain words**: Young stars are often surrounded by spinning disks of gas and dust that may be bent out of flat, like a warped record. Measuring that bend from light is hard because a warp can look much like other features, such as shadows. The authors simulated disks with known bends, produced fake telescope maps of carbon monoxide gas, and checked how well a simple method could recover the bend from how the gas moves.
- **Why it matters**: Warps may shape how disks evolve and where planets form, and shadows cast by warped disks have been seen in observations, so a reliable way to measure warps matters. The text reports the method works for nearly face-on disks with small warps but breaks down at high inclinations, high emission heights, and sharp transitions, so its use on real disks is still limited.
- **Background needed**: - Protoplanetary disks: gas and dust disks around young stars, where planets may form.
- Keplerian disk: a disk whose gas orbits in the simple pattern set by gravity; deviations from this pattern carry information about the disk's shape.
- Inclination and position angle: how tilted the disk is to our line of sight and its orientation on the sky.
- Warp: a change in tilt or orientation with distance from the star, so the disk is not flat.
- Shadows: dark bands in scattered light caused by parts of a warped disk blocking starlight.
- CO rotational line emission observed with ALMA: radio light from carbon monoxide molecules, used to trace gas motion via Doppler shifts.
- Radiative transfer simulation: computing how light travels through and is emitted by a modeled object.
- Spectral resolution: how finely velocities are resolved in the data. · level: research-level

<details><summary>Original abstract</summary>

Evidence of shadowing among protoplanetary disks suggests that warped protoplanetary disks are widespread, making it crucial to constrain their three-dimensional shape in order to understand their dynamical evolution and origin. Yet, inferring this warp shape from observations is challenging, as the typical signatures of a warp, especially shadows, are often degenerate with the warp shape. Kinematics of disks may provide a method to recover the shape by interpreting the residuals from a Keplerian disk model as local changes in inclination and position angle. In this work, we test its applicability and limitations. We perform radiative transfer simulations of disks with a parametrized warp shape to create synthetic maps of $^{12}\mathrm{CO}$ rotational line emission at ALMA wavelengths and compare the fitted warp with the true warp shape. We find that the warp shape can be recovered for nearly face-on disks with small warp misalignments of a few degrees, even without knowledge about disk properties such as emission height. The overall warp shape remains traceable even at moderate spectral resolutions up to $0.8\,\mathrm{km/s}$. However, we identify regimes where the method breaks down, including disks with an inclination higher than $40^\circ$, a high emission height of the tracer, and sharp warp transitions. In addition, radial and vertical motions can introduce apparent warps and twists, motivating extensions of the method to account for these effects.

</details>

### [Kepler-404: A near-resonant pair of sub-Neptunes. Reinterpreting a false-positive signal with the novel detection method RIVERS.radon](https://arxiv.org/abs/2611.32298)
*Yannick Eyholzer, Marylyn Rosenqvist, Adrien Leleu et al.* · `astro-ph.EP` · arXiv:2611.32298v1 · relevance 0.09

- **In one sentence**: The paper shows that transit-timing variations can hide low-signal planets from standard transit searches, and uses a new 2D cross-correlation detector (RIVERS.radon) to recover Kepler-404b from a false-positive flag, finding it in a near 5:4 resonance with Kepler-404c and fitting both planets' radii and masses.
- **In plain words**: Planets that pass in front of their star cause tiny regular dips in its brightness, and a planet's own gravitational tugs on its neighbour can shift those dips in time, which makes standard searches miss faint signals. The authors built a new search method that does not assume the dips arrive on a strict schedule, and applied it to the star Kepler-404. They found that a signal previously labelled a false positive is a real planet, and that it and a companion planet orbit in a near-resonant pattern with similar size and mass.</plain>
<parameter name="why">Near-resonant planet pairs are expected to be common by planet-formation theory, yet few are observed, and this work suggests detection bias from timing shifts may partly explain the gap. The link to that broader population question is the paper's own argument; the text alone does not show how general the bias is.
- **Background needed**: - Transit method: a planet crossing its star dims the starlight slightly; the dips reveal the planet.
- Transit timing variations (TTVs): when planets gravitationally perturb each other, their transits arrive earlier or later than a fixed schedule.
- Resonance: two planets whose orbital periods form a simple whole-number ratio (here near 5:4), so they regularly tug on each other.
- Signal-to-noise ratio: how strong a signal is relative to random noise; low values make detection hard.
- Photodynamical fit: a model that simulates the gravitational dynamics and the light curve together to estimate planet masses and radii.
- False positive: a signal flagged as a planet candidate that later turns out to come from something else.
- Kepler mission: NASA telescope whose light curves are the data source here. · level: research-level

<details><summary>Original abstract</summary>

According to the current understanding of planet formation and evolution, (near)-resonant systems should be a common occurrence in nature. However, pairs of planets with period ratios close to commensurability are rarely observed. In this paper, we discuss how observational bias caused by transit timing variations (TTVs) can affect the detection of low signal-to-noise ratio (S/N) planets in transit surveys, playing a role in the lack of representation of these systems. We present an alternative detection method, RIVERS.radon, which overcomes the effect of TTVs on planet detectability by not relying on an exact periodic solution for the transit signal. It leverages 2D representations of the light curve and approximates the transits with a set of local periodic solutions with the use of 2D cross-correlation. We present an application of RIVERS.radon to the near-resonant system Kepler-404, showing that the signal of the false-positive candidate KOI-2768.03 belongs to the planet Kepler-404b and that it is in a near 5:4 resonance with its companion Kepler-404c, causing TTVs of amplitudes 117.64 and 110.09 minutes, respectively. With a photodynamical fit, we retrieve a pair of similar planets, respectively of radii $1.68^{+0.09}_{-0.09}$ and $1.69^{+0.10}_{-0.10}\,R_\oplus$ and of masses $1.91^{+0.41}_{-0.33}$ and $2.34^{+0.47}_{-0.40}\,M_\oplus$. We find that these planets exhibit typical (near)-resonant features: their densities are lower than the bulk population of exoplanets, and their orbits are nearly coplanar. Interestingly, the planets are found outside the resonance but at a significant distance from the equilibrium point of the $(X_{\rm res}, \delta)$ plane of the Hamiltonian, which is consistent with post-disk instability but somewhat at odds with the observed coplanarity.

</details>

## High-energy astrophysics

### [Cosmic ray protons from 40 GeV to 10 EeV due to star formation?](https://arxiv.org/abs/2611.32671)
*Timur Dzhatdoev, Ilya Kudryashov, Anatoly Semenov* · `astro-ph.HE` · arXiv:2611.32671v1 · relevance 0.18

- **In one sentence**: The paper proposes that cosmic-ray protons from about 40 GeV to 10 EeV could be described as a sum of three components from three distinct populations of supernova remnants, tested under a supergalactic diffusion scenario (halo size 1-20 Mpc) and a cosmological scenario (source redshift up to 6).
- **In plain words**: Cosmic rays are very fast charged particles that arrive at Earth from space, and their energy spectrum (how many arrive at each energy) has a shape that still needs explaining. This paper asks whether the particles at energies from about 40 billion electron-volts up to 10 billion billion electron-volts could come from exploding stars, and it tests two broad pictures of where they travel from. The text reports that a sum of three contributions, one for each of three groups of exploding-star remnants, reasonably matches the observed spectrum.
- **Why it matters**: Knowing where the highest-energy cosmic rays come from is an open question in astrophysics, and linking them to star formation would connect them to the life cycle of galaxies. The text gives only the framing and a summary claim of a reasonable fit; I cannot judge from it how strong or unique that fit is, so its significance remains uncertain.
- **Background needed**: - Cosmic rays: high-energy atomic nuclei (here protons) that travel through space and hit Earth's atmosphere.
- Energy units: GeV is a billion electron-volts, EeV is a billion billion electron-volts.
- Supernova remnant: the expanding debris and shock wave left after a massive star explodes; shocks can accelerate particles.
- Hypernova: an especially energetic supernova, which the paper suggests can push particle energies to about 1 EeV.
- Energy spectrum: the count of particles at each energy; its shape (breaks, slopes) is what models try to reproduce.
- Diffusion in a magnetic field: particles wander randomly through magnetic structures before escaping; the paper's halo size H (1-20 Mpc) sets how far they wander.
- Redshift: a measure of cosmic distance and age; z = 6 corresponds to sources existing very early in the universe. · level: research-level

<details><summary>Original abstract</summary>

The formation of massive stars eventually results in supernovae explosions. Typical supernova remnants (SNRs) accelerate cosmic ray (CR) protons up to $E_{max-p} \sim 10$ TeV; the value of $E_{max-p}$ may reach $\sim 1$ EeV for the case of the hypernovae and/or for a sub-relativistic velocity of the SNR's shock wave. We show that the observable CR proton spectrum in the energy range between 40 GeV and 10 EeV is reasonably well described with a sum of three components that correspond to three distinct SNR populations. We consider two basic scenarios of CR origin: I) the supergalactic scenario assuming diffusion of the protons inside a magnetic field structure with the characteristic radius $H = 1-20$ Mpc and II. the cosmological scenario with the maximum redshift of the sources $z_{max} = 6$.

</details>

### [Super-Eddington Neutron Star Accretion Columns: Comparing GRRMHD Simulations with Spectral Models](https://arxiv.org/abs/2611.32865)
*Fatemeh Kayanikhoo, Marios Kouzis* · `astro-ph.HE` · arXiv:2611.32865v1 · relevance 0.17

- **In one sentence**: Four axisymmetric general relativistic radiation magnetohydrodynamic simulations of super-Eddington accretion onto magnetized neutron stars (surface fields 3×10^10 to 1×10^11 G) measure accretion column width and estimated radiation shock height, and compare the resulting column radii with spectral fits from Be/X-ray binary outbursts using the bwcycl model.
- **In plain words**: A neutron star is a very dense, collapsed star, and when it pulls in gas faster than radiation pressure can comfortably balance, the gas lands on its magnetic poles in a narrow column that glows in X-rays. This paper uses computer simulations of that gas flow for four strengths of the star's magnetic field. It reports how wide the column is, how tall the braking region above the surface is, and how these compare with values inferred from X-ray observations of outbursts in Be/X-ray binaries.
- **Why it matters**: Understanding the shape of these columns matters for interpreting the X-ray light from bright outbursts, since the observed spectra are fit with models that assume a geometry. The paper finds that three of its four column radii fall in the upper part of the range the spectral fits suggest, which offers a rough cross-check between simulation and observation. The text does not show how strongly this agreement constrains the models, so it should be read as a consistency check rather than a settled answer.
- **Background needed**: - Accretion: matter falling onto a compact object such as a neutron star, releasing energy as it falls.
- Eddington limit: the rough brightness ceiling where outward radiation pressure balances gravity; "super-Eddington" means the inflow exceeds it.
- Neutron star: an extremely dense stellar remnant with a very strong magnetic field that can channel infalling gas to its poles.
- Accretion column: the narrow, funnel-shaped stream of gas hitting the magnetic pole.
- Be/X-ray binary: a system pairing a rapidly spinning, gas-emitting Be star with a neutron star; outbursts occur when the neutron star pulls in extra gas.
- General relativistic radiation magnetohydrodynamics (GRRMHD): simulations combining Einstein's gravity, magnetic fields, fluid flow and radiation transport.
- Axisymmetric: simulated as symmetric around one axis, which simplifies the calculation.
- Radiation shock: a boundary where fast infalling gas is abruptly slowed by radiation pressure.
- Spectral modeling: fitting a model to the measured X-ray energy distribution to infer physical parameters. · level: research-level

<details><summary>Original abstract</summary>

The geometry and structure of neutron star accretion columns affect the X-ray emission in super-Eddington accreting systems. We perform four axisymmetric general relativistic radiation magnetohydrodynamic simulations of super-Eddington accretion onto magnetized neutron stars with the maximum surface magnetic fields ranging from $3\times10^{10}$ to $1\times10^{11}\,\mathrm{G}$. We measure the column width and estimate the characteristic radiation shock heights from the flow velocity and velocity gradient. Across the four models, the angular width decreases from approximately $0.14$ to $0.07\,\mathrm{rad}$, while the estimated shock height increases from $1.95$ to $3.89\,\mathrm{km}$. We then compare our solutions to the best-fit values derived from spectral modeling of super-Eddington Be/X-ray binary outbursts. We calculate area-equivalent column radii that vary between 5.2 and 3.2 km, three of which fall within the upper part of the range inferred from spectral results using the \texttt{bwcycl} model.

</details>

## Stars and the Sun

### [Constraining the Binary Fraction and Mass-Ratio Distribution of FGK Dwarfs with Gaia XP Spectra: Metallicity, $\alpha$-Element, and Age Dependencies](https://arxiv.org/abs/2611.32656)
*Yinuo Zhang, Zexi Niu, Haibo Yuan et al.* · `astro-ph.SR` · arXiv:2611.32656v1 · relevance 0.06

- **In one sentence**: Using the Stellar Locus Outlier method on synthetic Gaia XP photometry plus LAMOST DR9 stellar parameters, this paper estimates the binary fraction and high-mass-ratio power-law slope for about 200,000 FGK dwarfs within 1 kpc and examines their dependence on metallicity, alpha-element abundances, and age.
- **In plain words**: The paper asks how often Sun-like stars have a companion star, and what kinds of companions they tend to have. The authors used colour measurements from the Gaia satellite's low-resolution spectra, for nearly 200,000 nearby stars, and looked for the tell-tale colour offset that a hidden companion adds to a star's light. They then compared the results with each star's chemical makeup and estimated age.
- **Why it matters**: Knowing how many stars come in pairs, and how their masses are matched, constrains how stars form and evolve. The text links the chemistry trends to possible dynamical or formation processes, but it does not establish a causal mechanism, so that link remains a suggestion.
- **Background needed**: - Binary fraction: the share of stars that have a companion star.
- Mass ratio (q): the companion's mass divided by the primary's mass; the distribution describes how common different pairings are.
- FGK dwarfs: main-sequence stars somewhat cooler or similar to the Sun, which are the most common stars nearby.
- Gaia XP spectra: low-resolution light spectra from the Gaia space telescope, used here as synthetic colour photometry.
- LAMOST DR9: a spectroscopic survey data release that supplies stellar parameters such as metallicity and element abundances.
- Metallicity: how much of a star's mass is made of elements heavier than helium.
- Alpha elements (Mg, Si, Ca): elements formed mainly in massive-star deaths; their ratios help trace stellar populations.
- Thin and thick disk: two stellar populations of the Milky Way, with the thick disk generally older and more metal-poor.
- Stellar locus: the main curve on a colour-colour plot where single stars lie; binaries appear as outliers displaced from it. · level: research-level

<details><summary>Original abstract</summary>

We present a study of the binary fraction and mass-ratio distribution for near 200,000 FGK dwarf stars within 1 kpc, utilizing the Stellar Locus Outlier (SLOT) method applied to synthetic Gaia XP photometry and stellar parameters from LAMOST DR9. By modeling the asymmetric color residuals relative to a metallicity-dependent single-star locus, we measure the binary fraction $f_b$ and constrain the power-law slope $\gamma_{\rm large\,q}$ of the mass-ratio distribution at high mass ratio $q$. Higher metallicity is associated with a steeper (more negative) $\gamma_{{\rm large}q}$, indicating a larger proportion of low-mass-ratio systems. For $\alpha$-elements, [Mg/H] and [Si/H] are anticorrelated with $f_b$ in thin-disk-dominated subsamples; conversely, [Ca/H] shows a positive correlation with $f_b$ in thin-disk-dominated subsamples. No correlation is found between $f_b$ and $\alpha$-element abundances in thick-disk-dominated subsamples. The binary fraction increases modestly toward older ages in the thin-disk population, a trend that likely reflects underlying correlations with chemistry. Our results shed light on how chemical composition and dynamical processes shape the binary properties of solar-type stars.

</details>

### [A Study of Three Intrinsically Luminous Long Period Interacting Eclipsing Binaries in the Galaxy and the Small Magellanic Cloud](https://arxiv.org/abs/2611.33002)
*T. J. Davidge* · `astro-ph.SR` · arXiv:2611.33002v1 · relevance 0.05

- **In one sentence**: A study of three long-period (hundreds of days), interacting eclipsing binary stars with highly evolved giant components, two in the Small Magellanic Cloud and one (PW Pup) in the Galaxy, using archival visible and mid-infrared photometry and spectroscopy to constrain masses, mass ratios and mass transfer history.
- **In plain words**: This paper looks at three pairs of stars that orbit each other and periodically pass in front of one another, making their combined brightness dip. Two of the pairs are in the Small Magellanic Cloud, a neighbouring galaxy, and one is in our own Galaxy. Using old observations already in archives, the authors estimate how heavy the hidden companion stars must be and suggest that these systems have already passed material between them.
- **Why it matters**: Systems like these are useful test cases for how stars evolve when they exchange mass, and the text says some of the companions may be hard to detect directly, so the findings point to where future infrared observations could help. The text itself does not claim wider consequences beyond these three systems.
- **Background needed**: - Eclipsing binary: two stars orbiting each other whose alignment with us makes them dim periodically; the dips reveal their sizes, temperatures and orbits.
- Orbital period of hundreds of days: the stars circle each other slowly, so they are far apart compared with close binaries.
- Giant (K and M type): cool, large, evolved stars that have swollen after using up core fuel.
- Mass transfer: one star feeding material onto its partner, which changes both stars' evolution.
- Mass function and minimum mass: an estimate, from orbital motion alone, of the least mass a hidden companion can have.
- Mass ratio: the ratio of the two stars' masses, which light-curve models must assume or fit.
- Mid-infrared (MIR): longer-wavelength light that is invisible to the eye and can reveal cooler dust or disks.
- Main sequence and B spectral type: B-type stars are hot, massive stars burning hydrogen; the paper says the stars began as B-type stars.
- Small Magellanic Cloud: a satellite galaxy of the Milky Way, with stars at a different chemical makeup than ours. · level: research-level

<details><summary>Original abstract</summary>

The properties of the eclipsing binaries SMC004701.39-732645.8, SMC005609.41-722809.2 and PW Pup are examined using archival photometric and spectroscopic observations. These systems have orbital periods of hundreds of days, and contain highly evolved components with temperature differences of at least 1000 - 2000K. The SMC systems are among the brightest eclipsing binaries in that galaxy at visible wavelengths, and show excess thermal emission that appears to be typical for luminous K and M giants in that galaxy. A preliminary mass function for SMC004701 suggests a minimum mass for the secondary of 3.8 +/- 0.8 Msolar, whereas the PW Pup mass function indicates a minimum mass for the secondary of 3.2 +/- 0.3 Msolar. Light curve elements are examined for a range of mass ratios using observations at visible and mid-infrared (MIR) wavelengths. The results suggest that SMC004701 may prove to be a double line spectroscopic binary at visible wavelengths. However, with the possible exception of emission from a circumstellar disk, infrared observations will likely be required to detect light from the secondary in the other two systems. All three systems have likely experienced mass transfer, and had components with initial masses that correspond to B spectral types on the main sequence. The light associated with the secondary likely originates from a shell or disk that obscures a hotter central star.

</details>

## Chemical physics

### [Current-Dependent Meta-GGA and Local Hybrid Functionals for Relativistic NMR Shifts](https://arxiv.org/abs/2611.31432)
*Yannick J. Franzke, Christof Holzer* · `physics.chem-ph` · arXiv:2611.31432v1 · relevance 0.22

- **In one sentence**: The paper derives and implements a two-component relativistic version of the current-dependent kinetic-energy density for meta-GGA and local hybrid density functionals in NMR shielding and shift calculations, using a Kramers-restricted Kohn-Sham reference and SAP-X2C relativistic treatment.
- **In plain words**: Chemists use computer models to predict NMR spectra, the fingerprint signals that show how atoms sit in a molecule. For compounds with heavy atoms, relativistic effects matter, and the standard software support for the more accurate modern calculation methods is limited. This paper presents a way to include a more gauge-consistent form of one such method in relativistic NMR calculations.</plain>
<parameter name="why">Predicting NMR shifts for heavy-element compounds is useful for checking and interpreting experiments, so a more reliable calculation method could help. The text presents the formulation and its gauge invariance, but it does not report benchmark accuracy numbers in the excerpt, so its practical gain is not established here.</plain>
<parameter name="background">- NMR chemical shift: the frequency at which a nucleus resonates, sensitive to its local electronic environment.
- Density functional theory (DFT): a computational method that gets molecular energies and properties from electron density instead of full wavefunctions.
- Meta-GGA and local hybrid functionals: refined DFT approximations that use extra density information (such as kinetic-energy density) to improve accuracy.
- Gauge invariance: results do not depend on the arbitrary choice of reference origin for the magnetic vector potential; this is needed for reliable magnetic properties.
- Relativistic effects and spin-orbit coupling: important for heavy atoms; they make electron currents and spin mix, so the calculation must treat current densities in the ground state.
- Two-component (X2C) theory: a simplified relativistic framework that approximates the full four-component Dirac treatment.
- Kramers-restricted Kohn-Sham: a reference-state formalism for systems with time-reversal symmetry in relativistic calculations.
- **Background needed**:  · level: research-level

<details><summary>Original abstract</summary>

NMR chemical shifts are key for the characterization of novel compounds. Especially for molecules with heavy elements, the experimental data is often corroborated with computational studies in density functional theory (DFT). However, modern meta-generalized gradient approximations (meta-GGAs) and local hybrid functionals are not widely supported in relativistic calculations with quantum chemistry program suites. So far, their current-dependent generalization in the spirit of Dobson, Becke, and Tao was not presented at all. This generalization ensures gauge invariance and does not introduce artifacts--unlike the more popular field-dependent generalization of the kinetic-energy density. In non-relativistic and scalar-relativistic calculations, the first was shown to be superior but the current density only arises due to the magnetic field perturbation. In contrast, spin--orbit coupling also induces current densities in the preceding ground-state calculation and the DFT framework needs to be generalized to a current density functional theory (CDFT) for consistency with the current-dependent response equations. Herein, we present the two-component relativistic generalization of the current-dependent kinetic-energy density of a Kramers-restricted Kohn--Sham reference for meta-GGAs and local hybrid functionals in NMR calculations. The extension is invariant under a position-dependent phase and a position-dependent spin rotation of the spinors, or a local U(1)$\times$SU(2) transformation. Relativistic effects are considered with exact two-component theory using a superposition of atomic potentials to include the two-electron picture-change correction (SAP-X2C).

</details>

### [Spin-adapted state preparation for quantum chemistry](https://arxiv.org/abs/2611.30014)
*Matthew L. Sims-Goh, Fredrik Hasselgren, Hamza Jnane* · `quant-ph` · arXiv:2611.30014v1 · relevance 0.14

- **In one sentence**: The paper shows that spin-adapted DMRG matrix product states, indexed by unitary group approach steps, form an abelian-symmetric MPS that block-sparse protocols can load at a cost set by the spin-multiplet count, followed by a per-site Clebsch-Gordan rotation, and gives Toffoli and ancilla resource estimates for singlet ground states of iron-sulphur active space models.
- **In plain words**: Quantum computers could in principle estimate the energy of molecules that are hard to model on ordinary computers, but they first need a good starting state, and building that state is expensive. This paper proposes a way to prepare a starting state that respects the total spin of the molecule, which lets the circuit store fewer amplitudes. The authors estimate the cost of their circuits for model iron-sulphur clusters and report lower Toffoli-gate counts and fewer ancilla qubits than the comparison methods they name.
- **Why it matters**: Preparing the initial state is a major fault-tolerant cost for phase estimation on strongly correlated molecules, so cheaper preparation bears directly on whether such calculations become practical. The results are resource estimates from the paper's own circuit designs, not hardware demonstrations, so the size of the practical gain remains to be tested.
- **Background needed**: - Quantum phase estimation: a quantum algorithm for finding the energy of a molecule, which needs a good approximate starting state.
- Fault-tolerant cost: the count of expensive error-corrected operations (such as Toffoli gates) and the number of ancilla (helper) qubits a circuit needs.
- Matrix product state (MPS): a chain-like way of compactly writing a quantum state of many particles, built with the density matrix renormalisation group (DMRG) method.
- Spin and symmetry: a molecule's total spin is conserved, and exploiting that conservation reduces the number of amplitudes to store; "block-sparse" means storing only the nonzero blocks that respect a symmetry.
- Unitary group approach: a standard way of labelling electron configurations and spin states in quantum chemistry.
- Clebsch-Gordan coefficient: a number from angular momentum theory that tells how spin states combine.
- Active space model: a reduced set of orbitals and electrons chosen to capture the strongly correlated part of a molecule. · level: research-level

<details><summary>Original abstract</summary>

Quantum phase estimation for strongly-correlated molecules requires an initial state of high overlap with the true ground state, and preparing one is a significant fault-tolerant cost. Matrix product states (MPS) produced by the density matrix renormalisation group (DMRG) are a leading choice, yet existing circuits treat their tensors as dense or do not use the full symmetries present in molecular electronic Hamiltonians. In quantum chemistry, DMRG also exploits total spin, a non-abelian symmetry, storing one amplitude per spin multiplet instead of one per state. We show that the reduced tensors of such a spin-adapted MPS, labelled by the steps of the unitary group approach, form an abelian-symmetric MPS, which existing block-sparse preparation protocols can load at a cost set by the multiplet count. One state-independent rotation per site, determined by a Clebsch-Gordan coefficient, then returns the state to the occupation basis. We provide resource estimates for our circuits on singlet ground states of active space models of iron-sulphur clusters, finding improvements in Toffoli count up to $135\times$ compared to dense methods and $4.9\times$ compared to block-sparse methods applied to the same states, with up to $3.7\times$ fewer ancilla qubits required.

</details>

## Materials science

### [Magic-layer scenario for predicting non-van der Waals two-dimensional materials: The case of double-layer honeycomb structures](https://arxiv.org/abs/2611.31748)
*Shota Ono* · `cond-mat.mtrl-sci` · arXiv:2611.31748v1 · relevance 0.15

- **In one sentence**: Using first-principles calculations, the authors propose a "magic-layer" stability criterion, based on excess energies of thin films at different thicknesses, to predict which non-van der Waals compounds (III-V, II-VI, I-VII and Mn-based) can form stable double-layer honeycomb 2D structures.
- **In plain words**: Some flat, one-atom-or-few-atom-thick sheets can be peeled off a bulk crystal easily because their layers are held together weakly. Many other materials are not like this, and making their thin sheets is hard. This paper borrows an idea from cluster physics, where certain "magic" sizes are unusually stable, and checks which thicknesses of several compound crystals are energetically favoured.
- **Why it matters**: The text reports that the stability measure separates compounds that have been experimentally synthesized from those that have not, which suggests it could be a screening tool for finding new 2D materials. The text does not show how well this generalises beyond the studied families, so its predictive reach remains to be tested.
- **Background needed**: - Van der Waals (vdW) bonding: weak attraction between layers, which lets sheets be peeled off (exfoliated), as with graphene.
- Non-vdW 2D material: a sheet-like material whose layers are held by stronger chemical bonds, so it is hard to separate from its bulk crystal.
- First-principles calculations: computer simulations of material energies starting from basic quantum mechanics, with no fitted experimental inputs.
- Excess energy: how much higher in energy a thin film is than the bulk crystal; lower values indicate a more stable film.
- Magic number: a size of a cluster that is unusually stable compared with neighbouring sizes.
- Honeycomb structure: a hexagonal lattice pattern of atoms, like graphene's.
- III-V, II-VI, I-VII: groups of compounds built from elements in those columns of the periodic table (e.g., GaAs, ZnS, NaCl-type salts). · level: research-level

<details><summary>Original abstract</summary>

A magic number is a specific size of a van der Waals (vdW) cluster that shows pronounced stability compared to adjacent sizes, and therefore magic clusters are preferentially formed in experiments. We apply the ``magic-layer'' concept to identify non-vdW two-dimensional (2D) materials that are difficult to exfoliate from their parent 3D crystals. As a case, we study the stability of thin films in III-V, II-VI, I-VII, and Mn-based compounds using first-principles calculations. By calculating excess energies for various thicknesses, we find significant stabilization reflecting the formation of double-layer honeycomb structures at specific thicknesses. The stability measure based on the magic-layer concept can distinguish the experimentally synthesized systems from the experimentally unrealized systems, which serves as a key descriptor for predicting the realization of non-vdW 2D materials.

</details>

### [Compositionally Tunable Synthesis of High-Entropy Transition Metal Dichalcogenides Exhibiting Above-Room-Temperature Magnetism](https://arxiv.org/abs/2611.33115)
*Chen Zhang, Xiahua Zhong, Dejia Kong et al.* · `cond-mat.mtrl-sci` · arXiv:2611.33115v1 · relevance 0.15

- **In one sentence**: The paper reports a two-step, solution-based route to ultrathin high-entropy transition metal dichalcogenides, using a mixed-metal layered hydroxide precursor that is then chalcogenized, with a representative (VCrFeCoNi)S2-x composition showing magnetism above room temperature.
- **In plain words**: Researchers want very thin, flat magnetic materials that keep working at ordinary room temperature, since such materials could support future electronics and data-storage technologies. This paper describes a way to make thin layered sheets that mix five or more different metals at the atomic level. The team first builds a mixed-metal layered hydroxide precursor by chemical precipitation in a sealed heated vessel, then converts it into a sulfur-based layered compound, and reports that one example stays magnetic above room temperature.
- **Why it matters**: Magnetic two-dimensional materials are a active research area for spintronics and low-power information technology, and a method that can tune their composition is potentially useful. The text does not show device performance or how widely the approach extends beyond the representative composition, so its practical impact remains to be tested.
- **Background needed**: - Two-dimensional (2D) materials: crystals only a few atoms thick, arranged in sheets.
- Transition metals: elements such as iron, cobalt, nickel, chromium and vanadium, whose electrons often give rise to magnetism.
- Dichalcogenides: compounds of a metal with a chalcogen (sulfur, selenium or tellurium).
- High-entropy materials: materials that mix five or more elements in roughly comparable amounts, often in one uniform structure.
- Layered double hydroxides: layered mineral-like solids that can host mixed metal ions between their sheets; used here as a precursor.
- Hydrothermal coprecipitation: making a solid by mixing dissolved salts in water in a heated, sealed container so the solid forms.
- Chalcogenization: reacting a material with a chalcogen to convert it into the sulfide or similar compound.
- Magnetism above room temperature: magnetic order that persists at roughly 20–25 °C, which matters for practical devices. · level: research-level

<details><summary>Original abstract</summary>

As silicon-based electronics approach their physical limits, low-dimensional magnetic materials have attracted increasing attention for next-generation electronic and information technologies. Realizing these opportunities requires two-dimensional (2D) materials with robust and tunable room-temperature magnetism. Here, we report a two-step synthesis strategy for fabricating 2D high-entropy transition metal dichalcogenides (HE-TMDs) incorporating magnetic elements beyond conventional groups 4-6. High-entropy layered double hydroxides (HE-LDHs) are first synthesized via hydrothermal coprecipitation, enabling atomic-level mixing of diverse transition metals across groups 4-12. Subsequent chalcogenization yields 2D HE-TMDs while preserving homogeneous elemental distribution. This approach circumvents the constraints of solid-state reaction, chemical vapor transport methods, enabling the synthesis of compositionally complex and structurally controlled 2D magnets. Representative (VCrFeCoNi)S2-x exhibits robust magnetism above room temperature, demonstrating the potential of this high-entropy design strategy for expanding the compositional and functional diversity of 2D magnetic materials.

</details>

## Soft matter and polymers

### [Long-Range Hydrodynamic Communication in Active Matter](https://arxiv.org/abs/2611.32867)
*Abhishek Thakur, Bibaswan Ghosh* · `cond-mat.soft` · arXiv:2611.32867v1 · relevance 0.17

- **In one sentence**: A symmetric passive rotor inside a circular domain is driven into steady one-way rotation by the collective hydrodynamic flow of a boundary-confined flock of Marangoni swimmers, with no physical contact, and the authors attribute the stabilization to suppression of reverse-torque events and a minimal flow-superposition model.
- **In plain words**: Tiny self-propelled swimmers that move along a liquid surface by a chemical-driven surface-tension effect (the Marangoni effect) can set a free-floating, symmetric wheel spinning in one direction without touching it. The authors report that single swimmers give occasional backward kicks, but larger groups create a steady circulating flow that keeps the wheel turning consistently. Velocimetry measurements of the fluid flow show that this push carries over long distances.
- **Why it matters**: It shows that directed mechanical motion can arise from collective fluid flow alone, without the built-in shapes (ratchets or gears) normally used to rectify random motion, which may matter for remote actuation in active matter. The text is a brief abstract only, so the strength of the evidence, the experimental details, and how general the effect is cannot be judged from it.
- **Background needed**: - Active matter: systems whose units consume energy to move on their own, such as swimmers or self-propelled particles.
- Marangoni effect: fluid flow driven by gradients of surface tension, often produced by a chemical released at a liquid surface.
- Passive rotor: an object that does not propel itself but can be turned by fluid around it.
- Ratchet: a asymmetric structure that turns random jiggling into net one-way motion; this paper claims to avoid needing one.
- Hydrodynamic coupling: the way one moving body pushes the surrounding fluid, which then moves other bodies.
- Particle image velocimetry (PIV): an imaging method that tracks tracer particles to map fluid velocity.
- Torque: a twisting force; reverse torque means a momentary push in the opposite rotational direction. · level: intermediate

<details><summary>Original abstract</summary>

Directed transport in active matter is typically achieved by introducing geometric asymmetry, such as ratchets or gears, that rectify the stochastic motion of active particles. Here we demonstrate a fundamentally different route in which persistent mechanical motion emerges without any geometric bias. A symmetric passive rotor placed at the center of a circular domain undergoes spontaneous unidirectional rotation driven solely by the hydrodynamic flow generated by a boundary-confined flocks of Marangoni swimmers, despite the absence of direct physical contact. While individual swimmers produce intermittent torque reversals arising from transient hydrodynamic backflow, increasing the size of the flock establishes coherent circulation that stabilizes the rotor dynamics. Particle image velocimetry (PIV) reveals that the collectively generated flow transmits momentum over macroscopic distances, converting local active forcing into robust mechanical transport. Together with a minimal flow superposition model, our results identify the suppression of reverse-torque events as a collective signature of hydrodynamic coupling between active swimmers and a passive body, providing a contact-free mechanism for remote mechanical actuation in active matter.

</details>

### [Periodic and quasiperiodic structures produced by microphase separation in one-component simple liquids with competing interactions](https://arxiv.org/abs/2611.32273)
*Lorenzo Agosta, Alfredo Metere, Mikhail Dzugutov* · `cond-mat.mes-hall` · arXiv:2611.32273v1 · relevance 0.12

- **In one sentence**: A Perspective reviewing molecular-dynamics simulations of microphase separation in single-component simple liquids whose pair potentials combine short-range attraction with long-range repulsion (SALR), and the periodic and quasiperiodic structures these produce.
- **In plain words**: When two opposing forces act on the same particles, a liquid can avoid splitting into two large regions and instead form a repeating pattern of small-scale domains. This review looks at computer simulations of simple particles that do this using only one type of particle, with a short-range attraction and a long-range repulsion. The authors report that these simple models can reproduce patterns seen in block copolymers and liquid crystals, and they suggest such patterns could serve as templates for metamaterials.
- **Why it matters**: It suggests that the complex molecular structure of real materials is not required to form these ordered patterns, which matters for understanding how such patterns arise. The suggested link to topology-governed metamaterials is a proposal in the text, and its practical value is not demonstrated here.
- **Background needed**: - Phase separation: a mixture or liquid splitting into distinct regions, such as oil and water.
- Microphase separation: because competing forces stop large-scale splitting, the separation happens on a small, repeating length scale instead.
- Short-range attraction plus long-range repulsion (SALR): particles stick to close neighbours but push back against more distant ones.
- Block copolymers: long molecules made of chemically different segments that cannot separate fully, so they form nanoscale patterns.
- Mesophases: intermediate ordered states between liquid and crystal, such as those in liquid crystals.
- Molecular dynamics: computer simulation that tracks how each particle moves over time.
- Metamaterials: engineered materials whose behaviour comes from their structure rather than their chemistry. · level: research-level

<details><summary>Original abstract</summary>

Competing interactions can generate frustration which suppresses macroscopic-scale phase separation, superseding it with separation patterns on the microscopic scale. This phenomenon, referred to as microphase separation, produces thermodynamically stable mesoscopic-scale periodic patterns in systems of different physical nature. The studies of this effect follow two paradigms. First, in block copolymers, the macroscopic-scale separation of chemically distinct components is prevented by the covalent bonds between them. In the other, the microscopic-scale separation is produced in simple single-component liquids by the competition between a short-range attraction and a long-range repulsion (SALR) in the pair potential, the separation occurring between a dense phase and a gas. The interest in the simple liquid models with SALR interaction was inspired by the apparent universality of the modulated structures generated by competing interactions in different systems. Simple particle models are tractable by theory and thereby make it possible to discern the microscopic mechanisms of pattern formation; particle-based simulations give access to systems beyond the reach of experiments. In this Perspective we review the recent advances in the molecular-dynamics simulation of microphase separation in single-component simple liquids using SALR potentials. We show that these simulations reproduce the mesophases typical of block copolymers and liquid crystals, which demonstrates that the complexity of the constituent particles of real liquids is not a necessary condition for their formation, and that they produce novel periodic morphologies of both conceptual interest and technological relevance; we discuss how simulated mesophases can serve as templates for metamaterials whose properties are governed by topology.

</details>

## AI for chemistry and materials

### [Evolutionary constraints on protein fold diversity](https://arxiv.org/abs/2611.33104)
*Harutyun Sahakyan, Eugene V. Koonin* · `q-bio.BM` · arXiv:2611.33104v1 · relevance 0.32

- **In one sentence**: A review-style abstract arguing that natural proteins use only a small fraction of the folds that their secondary-structure arrangements could in principle form, and asking whether biophysics or evolutionary history sets that limit.
- **In plain words**: Proteins are chains that fold into 3D shapes, and in principle many more shapes are possible than nature actually uses. This short piece asks whether that gap comes from physical limits on what can fold or from the accidents of evolutionary history. The text says recent structure-prediction tools, protein comparison methods, and cryo-electron microscopy have helped map this space, and that natural proteins occupy only a small fraction of it.
- **Why it matters**: Knowing which shapes are reachable matters for designing new proteins and enzymes, and it bears on how evolution explores possibilities. The text is only an abstract, so it does not show the specific evidence or how strongly the constraints are established; the full paper would be needed to judge that.
- **Background needed**: - Proteins are chains of amino acids that fold into 3D shapes; the shape largely determines function.
- Secondary structures are local building blocks such as alpha helices and beta strands; their arrangement defines a fold's topology.
- A "fold" is a broad category of 3D architecture shared by proteins with a similar overall layout.
- Structure prediction and cryo-electron microscopy (a method that images molecules frozen in thin ice) let researchers see many more protein shapes than before.
- The open question is whether physics or evolutionary contingency (the role of chance and history) limits which folds exist. · level: intermediate
- Matched keywords: molecular, protein

<details><summary>Original abstract</summary>

Arrangements of secondary structures in proteins yield a wide variety of possible topologies, yet the protein folds observed in nature are limited in their diversity. Is the number of protein folds limited by biophysical constraints or by evolutionary contingency? In recent years, the development of new methods for protein structure prediction and comparison, molecular design, and the rapid progress of cryo-electron microscopy revealed new insights into the protein fold space. Here, we present recent findings demonstrating that natural proteins adopt only a small fraction of all possible folds and discuss how evolutionary processes limit the diversity of evolving protein folds.

</details>

### [OMNI-P3x universal neural network potential for large-scale computational photochemistry workflows](https://arxiv.org/abs/2611.32133)
*Miko{\l}aj Martyka, Joanna Jankowska, Pavlo O. Dral* · `physics.chem-ph` · arXiv:2611.32133v1 · relevance 0.24

- **In one sentence**: The paper presents OMNI-P3x, a universal machine-learned interatomic potential trained on ground- and singlet excited-state geometries of neutral and charged organic molecules, and applies it to screen flavylium and xanthene dye libraries for photochemical properties.
- **In plain words**: Designing light-responsive molecules, such as dyes that glow at particular colours, usually requires slow quantum calculations for every candidate, which makes testing huge lists of molecules impractical. The authors built a trained computer model that stands in for those calculations: it estimates molecular shapes and how strongly a molecule absorbs light without running new quantum calculations for each one. They used it to screen about 234,000 flavylium derivatives and, after fine-tuning, about 163,000 xanthene-based dyes, which they report as identifying new candidates for red, near-infrared and short-wavelength infrared emission.
- **Why it matters**: Faster screening could narrow down which molecules are worth synthesising and testing for applications such as imaging or light-harvesting materials. The text claims accuracy "approaching" TD-DFT (a standard but costly quantum method), but the abstract alone does not give the size of that error, so the practical reliability should be checked in the full paper.
- **Background needed**: - Photochemistry: how molecules change when they absorb light and enter an excited electronic state.
- Ground vs. excited state: the molecule's resting arrangement versus its arrangement after light absorption.
- Quantum-mechanical (QM) calculations: accurate but computationally expensive simulations of electrons and atoms.
- TD-DFT: time-dependent density functional theory, a widely used, moderately expensive method for excited states; here it serves as the accuracy benchmark.
- Machine-learned interatomic potential (MLIP): a neural network trained on quantum results that predicts atomic forces and energies far faster.
- Fine-tuning: adjusting a pretrained model on a narrower dataset to improve performance on a specific class of molecules.
- Flavylium and xanthene dyes: families of coloured organic molecules used as dyes and fluorescent markers.
- Near-infrared / short-wavelength infrared: light wavelengths just beyond visible red, useful for imaging through tissue. · level: research-level
- Matched keywords: molecular, interatomic potential

<details><summary>Original abstract</summary>

Computational photochemistry supports the design and understanding of new materials. However, the high cost of excited-state quantum-mechanical (QM) calculations makes screening large molecular libraries prohibitively expensive. To address this limitation, we introduce OMNI-P3x, a universal machine-learned interatomic potential (MLIP) for singlet ground- and excited-state simulations of neutral and charged organic molecules. Trained on both ground- and excited-state conformations, it performs complete computational photochemistry workflows with accuracy approaching TD-DFT. We demonstrate its practical applicability by screening a combinatorial library of 234,375 flavylium derivatives, where the pretrained model performs ground-state geometry optimization and predicts absorption properties without additional QM calculations. Following fine-tuning, we further screen 162,960 xanthene-based dyes, identifying new candidates for red, near-infrared and short-wavelength infrared emission. Furthermore, state-dependent neural charges, learned without reference atomic charges, provide an interpretable picture of intramolecular charge redistribution upon excitation.

</details>

## Biochemistry

### [Resolving Hepatic Metabolic Flux During Ex Vivo Liver Perfusion Reveals Compartment-Specific Constraints](https://www.biorxiv.org/content/10.64898/2026.11.24.769061v1)
*Amin, A. M.; Mcleod, M.; Browder, N. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.24.769061 v1 · relevance 0.10

- **In one sentence**: Using 13C-labelled tracers in staged ex vivo perfused mouse livers and serial lobectomies, the authors test whether a simple glucose-fragment flux model holds and find that a two-compartment model (glycolytic plus gluconeogenic) fits intracellular isotopomer data better than a one-compartment model, with partial agreement between the two flux estimates.
- **In plain words**: Surgeons keep donor livers alive outside the body on a perfusion machine and currently judge them with broad measures. This study asks whether tracking how labelled sugars and fuels move inside liver cells can give a more detailed picture of how the liver is working. In mouse livers, a simple one-region model failed to fit most data, especially for TCA cycle intermediates such as malate, while a model split into two cell regions fit 41 of 45 datasets.
- **Why it matters**: Better intracellular measures could eventually help judge whether a donor liver is healthy enough to transplant, though the text is limited to mouse work and does not show any clinical use. The finding that liver compartmentation limits whole-liver flux estimates matters for how such tracer studies are interpreted, and the authors say simplified models still support quantitative assessment.
- **Background needed**: - Normothermic machine perfusion: keeping an organ warm and circulating fluid through it outside the body.
- Metabolic flux: the rate at which molecules are converted through biochemical pathways.
- 13C tracers: fuels (lactate, pyruvate, glucose) with heavy carbon atoms, so their path through cells can be followed.
- Isotopomers: versions of a molecule that differ in where or how many heavy atoms they carry.
- TCA cycle: the central energy-producing cycle in mitochondria; malate is one of its intermediates.
- Gluconeogenesis: the liver making new glucose from non-sugar precursors.
- Compartmentation: dividing a tissue into functional regions with different metabolic behaviour.
- Lobectomy: surgical removal of a lobe of the liver. · level: research-level

<details><summary>Original abstract</summary>

Normothermic machine perfusion (NMP) is used to preserve and assess donor livers, but current viability criteria rely on global measures that do not resolve intracellular metabolism, which would provide a more mechanistic measure of donor liver function. We combined staged ex vivo perfusion of mouse livers, serial lobectomy and 13C tracers ([U-13C3]lactate, [U-13C3]pyruvate and [U-13C6]glucose) to test whether glucose fragment-based flux models used in vivo describe intact hepatic metabolism. With intracellular metabolite isotopomers as constraints, a homogeneous one-compartment model failed to fit most datasets, and the lack of fit centered on TCA cycle intermediates such as malate. A two-compartment model, in which a glycolytic compartment takes up glucose from the sinusoidal pool, including glucose released by a gluconeogenic compartment, fitted 41 of 45 datasets. Flux partitioning between compartments depended on nutritional state, which influenced hepatic metabolism more than perfusate glucose. Nevertheless, glucose fragment and two-compartment flux estimates correlated (R2 = 0.68-0.89). Intracellular isotope tracing thus shows that hepatic compartmentation constrains whole-liver flux estimation, while supporting simplified models for quantitative assessment during perfusion.

</details>

### [Albumin alleviates pressure overload-induced heart failure by improving mitochondrial homeostasis via PKA-LKB1-AMPK axis](https://www.biorxiv.org/content/10.64898/2026.11.21.768247v1)
*AN, Q.; Ma, B.; Fu, Y. et al.* · `biochemistry` · bioRxiv doi:10.64898/2026.11.21.768247 v1 · relevance 0.06

- **In one sentence**: In a mouse model of pressure-overload heart failure, recombinant mouse serum albumin improved cardiac function and mitochondrial energy metabolism, with the authors proposing a PKA-LKB1-AMPK signaling axis as the mechanism.
- **In plain words**: Heart failure is a condition where the heart cannot pump blood well, and patients with it often have low levels of albumin, the most common protein in blood. This study used mice whose hearts were put under extra pressure by constricting the aorta, and found that giving them recombinant (lab-made) mouse albumin improved heart function, reduced thickening and scarring of the heart muscle, and eased inflammation. Mice lacking albumin did worse, and the albumin treatment helped them too.
- **Why it matters**: Low albumin is already linked to worse outcomes in heart failure, so this work tests whether albumin is a cause rather than just a marker, and suggests a possible treatment direction. The evidence comes from mice and cultured heart cells only, so it does not show that albumin would work in patients; the abstract also gives no detail on dosing or clinical testing.
- **Background needed**: - Heart failure: the heart pumps too weakly to meet the body's needs; it is common, deadly and costly.
- Serum albumin: the main protein in blood plasma, which carries molecules around the body and helps maintain fluid balance; low levels are a known warning sign in heart disease.
- Transverse aortic constriction (TAC): a surgical method that narrows the main artery from the heart to create pressure overload, a standard way to model heart failure in mice.
- Cardiac hypertrophy and fibrosis: enlargement of heart muscle cells and build-up of scar-like tissue, both signs of heart damage.
- Mitochondria: the cell's energy-producing structures; "mitochondrial homeostasis" means keeping them healthy and balanced.
- Fatty acid oxidation and oxidative phosphorylation: the processes by which cells burn fats and sugars to make energy.
- AMPK and LKB1, PKA: cellular signaling proteins that sense energy status and coordinate responses; the paper proposes they form a chain activated by albumin.
- Knockout mice (AKO): mice genetically engineered to lack the albumin gene, used to test whether the protein is needed. · level: research-level

<details><summary>Original abstract</summary>

Aims Heart failure (HF) is a global health challenge due to its high incidence, mortality, and socioeconomic burden. Despite medical advancements, HF prognosis remains poor, highlighting the need for enhanced understanding and treatment strategies. Serum albumin, a key circulatory protein, has gained attention as a biomarker in cardiovascular diseases. Low serum albumin levels are linked to HF incidence, progression, and prognosis, suggesting its regulatory role, though mechanisms remain unclear. This study aimed to elucidate the role of serum albumin in HF pathogenesis and investigate its potential therapeutic effects. Methods and results A mouse model of pressure overload-induced HF was established via transverse aortic constriction (TAC). Serum albumin levels were significantly decreased in HF mice. Administration of recombinant mouse serum albumin (rMSA) effectively restored serum albumin concentrations, improved cardiac systolic function, alleviated cardiac hypertrophy and fibrosis, and reduced inflammatory responses, collectively attenuating disease progression. In contrast, albumin-knockout (Alb-/-, AKO) HF mice displayed aggravated pathological manifestations compared with wild-type (WT) controls, whereas rMSA supplementation markedly ameliorated these impairments. In vitro experiments demonstrated that rMSA protected against phenylephrine (PE)-induced hypertrophy in cardiomyocytes. To elucidate the underlying mechanism, transcriptomic analyses of cardiac tissues revealed that albumin played a critical role in improving mitochondrial homeostasis. Experimental validation further demonstrated that albumin activated the PKA-LKB1-AMPK signaling axis, leading to improved mitochondrial respiratory function and oxidative phosphorylation, as well as enhanced mitochondrial quality control. These changes promoted fatty acid oxidation and optimized energy metabolism, thereby reversing the energy imbalance underlying cardiac dysfunction. Conclusion Our study suggests that serum albumin exerts a protective effect in HF by improving mitochondrial dysfunction and energy metabolism disorders, thus reversing energy imbalance and mitigating disease progression. These results support recombinant serum albumin as a promising therapeutic for HF, with its mechanism involving the critical improvement of mitochondrial homeostasis.

</details>

## Pharmacology and drug discovery

Nothing notable this time.

## Computational and systems biology

### [Tuning evolutionary information in MSAs shapes protein generation and folding](https://www.biorxiv.org/content/10.64898/2026.11.23.768656v1)
*Richardson, G.; Colliandre, L.* · `bioinformatics` · bioRxiv doi:10.64898/2026.11.23.768656 v1 · relevance 0.15

- **In one sentence**: The paper tests whether changing which homologous sequences are included in a protein multiple sequence alignment (MSA), and thereby its per-site information content, steers generative protein design and structure prediction outcomes.
- **In plain words**: Researchers who use computer models to design or predict protein shapes feed them a collection of related protein sequences from many species. This study asks whether deliberately choosing which sequences go into that collection, rather than treating the collection as fixed, changes what the models generate and how confidently they predict structures. The authors report that the coherence of the chosen sequences tracked both structure-prediction confidence and how novel the generated sequences were, with the strongest effects near a particular information level.
- **Why it matters**: It suggests that the input alignment, often treated as a fixed preprocessing step, is a lever that can change model behaviour, which matters for anyone relying on these tools for design. The text does not show how broadly the effects generalise beyond the 45-protein cohort and the benchmark named, so the scale of the practical impact is unclear.
- **Background needed**: - Multiple sequence alignment (MSA): a table lining up many related protein sequences so that matching positions sit in the same column.
- Homologues: sequences related by shared evolutionary ancestry.
- Information content (bits per site): a measure of how strongly a column is conserved; low values mean the position varies a lot across sequences.
- Structure prediction confidence: the model's own score of how sure it is about a predicted 3D shape.
- Generative protein models: systems that propose new amino acid sequences; "decoder uncertainty" refers to how unsure the generator is when choosing residues.
- Matched-depth control: a comparison set with the same number of sequences but chosen at random, to separate the effect of selection from the effect of size.
- The text is an abstract-level summary; methods and effect sizes are not given, so the findings should be read as preliminary. · level: research-level

<details><summary>Original abstract</summary>

Protein multiple sequence alignments are widely regarded as fixed artifacts of homologue retrieval. An alignment's row composition shapes the evolutionary context that is supplied to a protein model. In this study, we tested whether tuning row composition would steer protein generation and structure prediction outcomes. We tuned lower-tail alignment information by controlling row selection within a reference protein-projected coordinate frame. We paired each information-targeted alignment with a matched-depth random-row control alignment. Across a cohort of 45 diverse proteins, row coherence among the retained homologues is predictive of structural confidence readouts and generated sequence novelty. The strongest row-coherence states occur near an empirical lower-tail information reference point of 1 bit/site. Below this reference point, generated de novo sequences demonstrate more eager exploration, higher decoder uncertainty, and reduced structural confidence at mutated positions. Across an independent structure-prediction benchmark, controlling the fraction of low-information positions demonstrated that intermediate fractions of low-information positions were associated with improved structure prediction within a confidence-gated subset. These findings evince that evolutionary information in protein alignments can be tuned to shape protein generation and structure prediction results.

</details>

### [Microbiome complexity shapes host transcriptional networks across the ileum-liver axis](https://www.biorxiv.org/content/10.64898/2026.11.16.767119v1)
*Halkhoree, A. C.; Grannell, A.; Pearson, C. et al.* · `systems biology` · bioRxiv doi:10.64898/2026.11.16.767119 v1 · relevance 0.09

- **In one sentence**: Transcriptomic survey of mouse terminal ileum across germ-free, defined 12-strain microbiota (MM12), and specific-pathogen-free conditions, examining how microbiome complexity shapes co-expression networks linked to the ileum-liver axis.
- **In plain words**: This paper asks how much the community of microbes living in the gut changes the genes that are switched on in the lower small intestine (the terminal ileum) of mice, and whether that reaches the liver. The researchers compared mice with no microbes (germ-free), mice with a simple set of 12 known bacterial strains, and mice with a normal, diverse microbiome, with 15 animals in each group. The text provided ends at the study design, so the actual findings are not described here.
- **Why it matters**: Gut microbes are known to influence the immune system, bile acid handling and liver function, so tracing how their complexity tunes gene activity in the gut could help explain gut-liver links. The available text does not report results, so its significance beyond the stated aim cannot yet be judged.
- **Background needed**: - Microbiome: the community of bacteria and other microbes living in the gut.
- Germ-free mouse: raised with no microbes at all, used as a baseline.
- Oligo-Mouse-Microbiota-12 (MM12): a defined, simplified community of 12 bacterial strains.
- Specific pathogen free (SPF): mice with a normal, diverse microbiome but free of known pathogens.
- Terminal ileum: the last section of the small intestine, where nutrients and bile acids are absorbed.
- Transcriptome: the full set of gene activity readings in a tissue sample.
- Co-expression network: a map of genes whose activity rises and falls together, suggesting shared regulation.
- Gut-liver axis: the two-way communication between the intestine and the liver, partly via bile acids and immune cells. · level: research-level

<details><summary>Original abstract</summary>

The microbiome plays an increasingly recognised role in development, metabolism and immunity across all segments of the small and large intestine, as well as more distant organs such as the liver. In the terminal ileum - a key site of nutrient absorption - the presence of microbes dictates the development of secondary lymphoid structures (Peyers patches), mediates bile acid metabolism, and impacts absorption. In part, coordinated regulatory networks in the gut impact liver function and immunity through gut-liver connectivity and the movement of immune cells and bioactive small molecules that includes bile acids and other bacterial metabolites. We aimed to examine the extent of microbiome involvement in ileal transcription, where subtle changes in co-expression networks can be tuned by microbiome diversity, composition and function. We surveyed ileal transcriptomes across mouse models which vary in microbiome complexity ranging from germ-free (GF, n = 15), the Oligo-Mouse-Microbiota-12 (MM12, n = 15), and specific pathogen free (SPF, n = 15).

</details>

## Neuroscience

### [Benchmarking machine learning across development reveals stage-specific neuroanatomical sex signatures.](https://www.biorxiv.org/content/10.64898/2026.11.24.768941v1)
*Poon, E.; Honari, H.; Ansarifar, J. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.24.768941 v1 · relevance 0.10

- **In one sentence**: A benchmark of linear and nonlinear machine-learning classifiers for sex prediction from structural brain MRI in children and adolescents (ages 8–21), examining how age affects accuracy, feature stability, and SHAP/LIME-based attributions of sex-discriminative regions.
- **In plain words**: Researchers trained computer models to guess a person's sex from brain scans taken across childhood and adolescence. They compared several model types and checked how well the models worked at different ages and whether the brain regions the models relied on stayed consistent. The text reports that simple and complex models performed about the same, but that the patterns the models used changed with developmental stage.
- **Why it matters**: Sex differences in brain structure are a common but contested topic, and models that look accurate can still rely on unreliable features. The paper's emphasis on checking whether explanations are stable across development is a useful caution for anyone interpreting brain-imaging AI; the text does not establish what the regions mean biologically.
- **Background needed**: - Machine learning (ML): computer methods that learn patterns from example data to make predictions.
- Classification: predicting a category, here sex, from measurements.
- Structural neuroimaging: MRI scans that measure brain size and shape (e.g., cortical thickness, subcortical volumes), not activity.
- Linear vs. nonlinear models: simple weighted-sum models versus more flexible models that capture complex interactions.
- Cross-age generalization: testing whether a model trained on one age group works on another.
- SHAP and LIME: explainability tools that estimate how much each input feature pushed a prediction one way or another.
- Feature stability: whether the same features are chosen or weighted similarly across training runs or age groups.
- Cortical/subcortical: outer brain layer versus deeper brain structures. · level: intermediate

<details><summary>Original abstract</summary>

Machine learning (ML) offers powerful approaches for identifying multivariate patterns in neuroimaging data, yet the biological validity and interpretability of the discriminative patterns learned by such models remain incompletely understood. Here, we benchmarked multiple ML approaches for sex classification across development (8-21 years) on structural neuroimaging data and investigated the effects of age on model performance and feature stability. Linear and nonlinear models demonstrated comparable classification performance, indicating that high predictive accuracy can be achieved without relying on highly complex architectures; however, age-stratified analyses and cross-age generalization tests demonstrated that developmental stage influences classification performance, and consistency of learned neuroanatomical features. To assess biological interpretability, we applied SHAP and LIME explainability methods and developed a comprehensive framework for translating feature attributions into biologically interpretable patterns. Sex-discriminative regions were distributed across multiple cortical and subcortical structures and exhibited marked developmental variation. Together, these findings demonstrate the utility of interpretable ML for developmental neuroimaging and highlight the importance of evaluating predictive performance while simultaneously taking biological validity, developmental specificity, and attribution stability into consideration.

</details>

### [Jump: Making Large-Scale Connectomics Accessible](https://www.biorxiv.org/content/10.64898/2026.11.12.765999v1)
*Morris, G. P.; Mohamed, H. F.; Selim, R. S. et al.* · `neuroscience` · bioRxiv doi:10.64898/2026.11.12.765999 v1 · relevance 0.09

- **In one sentence**: The paper presents Jump, a set of web-based tools (demonstrated through uJump on the MICrONS mouse visual cortex EM dataset) for exploring, community-reviewing, and quantitatively analysing large volume electron microscopy connectomics data, with a case study reclassifying pericytes and endothelial cells in cortical vasculature.
- **In plain words**: Scientists who map the brain with electron microscope images now have huge libraries of cell shapes and connections, but computers label many of the cells automatically and those labels are hard to check. This paper describes Jump, a set of web tools that let people search these libraries, inspect individual cells, measure their shapes and locations, and have experts review and correct labels so the corrections can be shared. The authors show the approach on blood-vessel cells as an example.
- **Why it matters**: As connectomic datasets grow to hundreds of thousands of cells, checking automated labels becomes a bottleneck, so tools that lower that barrier could matter for many labs. The text does not report measured gains in accuracy or speed, so the practical impact is still to be shown by use over time.
- **Background needed**: - Connectomics: mapping the wiring of neurons and other cells, usually from very thin slices imaged with electron microscopy (EM).
- Volumetric EM: 3D electron microscope imaging of tissue, producing datasets of hundreds of thousands of cells.
- Automated segmentation and classification: software that outlines cells and assigns them types, which then needs human checking.
- MICrONS: a large public mouse visual cortex dataset used here as the example.
- Pericytes and endothelial cells: cell types that line and support blood vessels in the brain.
- Web platform: a tool used through a browser, without needing to install specialised software.
- The paper says the platforms were generated using Claude, an AI model, which is relevant to how the software was built. · level: intermediate

<details><summary>Original abstract</summary>

Large-scale connectomic resources generated from volumetric electron microscopy (EM) have transformed neuroscience by enabling detailed 3D reconstructions of cellular and subcellular morphology and connectivity across hundreds of thousands of cells in diverse tissues and organisms. Recent advances in machine learning-based cell classification and automated segmentation have enabled large-scale annotation of these datasets, yet barriers remain in validating automated classifications and extracting biological insights. To address these challenges, we developed Jump, a suite of user-friendly web-based platforms generated using Claude. These platforms support interactive exploration, expert-guided community review, and quantitative analysis of multiple publicly available EM datasets, while building a growing repository of community-generated annotations. Using uJump, which hosts data from the MICrONS mouse visual cortex dataset, as an example, we demonstrate rapid retrieval of specific cell populations, region-of-interest filtering, biological inspection of cells, and extraction of quantitative morphological and spatial metrics. We showcase analytical features including cell abundance and spatial organisation, connectivity, local cellular neighbourhoods, and volumetric measurements. Using pericytes and endothelial cells as a case study on the cortical vasculature, we further demonstrate how manual review and reclassification can generate accurately identified cell populations for downstream analyses. Consistent with the open-science principles underpinning many large-scale EM resources, Jump is designed to enable broad community participation. By lowering technical barriers to the use of EM datasets, Jump increases analytical efficiency and promotes collaborative efforts to accurately classify cells and structures. Expert-reviewed annotations can be shared across the community, allowing users to build on existing work rather than repeatedly validating the same automated classifications. Collectively, Jump will help researchers to accelerate biological discovery from connectomic datasets.

</details>

## Genetics and genomics

### [Functional interrogation of osteoarthritis-associated regulatory variants and effector genes.](https://www.biorxiv.org/content/10.64898/2026.11.23.768666v1)
*Piedade, A. P.; Stuppy, S. R.; Shine, J. et al.* · `genomics` · bioRxiv doi:10.64898/2026.11.23.768666 v1 · relevance 0.11

- **In one sentence**: Functional genomics in primary human chondrocytes (MPRA, CRISPR activation/interference, chromatin and conformation data) that links osteoarthritis GWAS loci to regulatory variants and target genes, centred on rs1895062 and PAPPA at 9q33.
- **In plain words**: Genetic studies have linked hundreds of spots in the human genome to osteoarthritis, a common joint disease, but in most cases it is unclear which DNA letter matters or which gene it affects. The authors tested candidate regions in cartilage cells grown in the lab, using methods that measure how strongly each DNA version switches genes on and off. They report that one variant, rs1895062, appears to raise activity of a nearby gene called PAPPA, with the risk version showing higher activity.
- **Why it matters**: It moves beyond association by combining several lines of evidence to suggest a likely causal variant and gene for one osteoarthritis risk locus, which could help prioritise follow-up work. The text does not show whether PAPPA is a viable drug target or how it affects joint health in people, so those links remain open.
- **Background needed**: - GWAS (genome-wide association study): scans of many people's genomes to find DNA regions statistically linked to a disease; such regions rarely point to the exact causal change.
- Regulatory variant: a DNA change that alters how much a gene is switched on, rather than changing the protein itself.
- Chondrocyte: the cell type that makes and maintains cartilage.
- MPRA (massively parallel reporter assay): a test that puts many DNA sequences into cells at once to measure which ones drive gene activity.
- CRISPR activation/interference: tools that turn a target gene's regulatory region up or down, to see the effect on gene expression.
- Chromatin accessibility, H3K27ac and chromatin conformation: markers of open, active DNA regions and of physical loops that bring distant DNA into contact with gene promoters.
- PAPPA: a protease involved in growth-factor signalling and extracellular matrix remodelling. · level: research-level

<details><summary>Original abstract</summary>

Background: Genome-wide association studies (GWAS) have identified hundreds of loci associated with osteoarthritis (OA); however, the regulatory variants and effector genes underlying most associations remain unresolved. Results: We used complementary functional genomic approaches in chondrocytes to resolve prioritized OA risk loci. Massively parallel reporter assays (MPRAs) in primary human chondrocytes identified allele-specific regulatory activity at variants across multiple loci, two of which were independently validated using low-throughput reporter assays. In parallel, integration of OA GWAS signals with chromatin accessibility, H3K27ac CUT&Tag, and chromatin conformation data prioritised candidate regulatory elements for CRISPR based perturbation. CRISPR activation and interference supported functional regulatory relationships between OA risk regions and Pappalysin 1 (PAPPA) and Sprouty RTK signaling antagonist 4 (SPRY4) as target genes. At the 9q33 locus, multiple independent lines of evidence converged on rs1895062, which resides in an accessible region that loops to the PAPPA promoter. The OA risk G allele at rs1895062 results in higher regulatory activity by MPRA and low throughput reporter assay. Activation of this region by CRISPR increases PAPPA gene expression and induces widespread transcriptional changes involving extracellular matrix remodelling and other OA-relevant pathways. Conclusion: Integrating genetic association, genomic and epigenomic data, and functional perturbation in disease-relevant cells can resolve the regulatory mechanisms underlying OA risk loci. Using this multi-faceted approach, we provide convergent functional evidence for rs1895062 as a likely causal variant that controls PAPPA gene expression and OA risk.

</details>

### [isoGS: A genomic method to navigate the breeder's dilemma of diversity versus eliteness](https://www.biorxiv.org/content/10.64898/2026.11.23.768689v1)
*Monyak, T.; Fall, S. T.; Opare-Obuobi, K. et al.* · `genetics` · bioRxiv doi:10.64898/2026.11.23.768689 v1 · relevance 0.09

- **In one sentence**: A simulation study proposing an isoeliteness score (an effect-size-weighted Hamming distance over QTL markers) between founder lines, and an isoeliteness-guided genomic selection (isoGS) method, to manage the diversity-versus-eliteness trade-off in admixed crop germplasm.
- **In plain words**: Public crop breeding programs swap seed lines with one another to add genetic variety, but mixing lines can break up gene combinations that already make a crop good. This paper uses computer simulations of a self-pollinating annual crop to test when such mixing hurts the gains that genomic selection (choosing plants by their DNA markers) can deliver. The authors score how genetically different founder lines are in the traits that matter most, and find that less compatible pairs gain less early on; a modified selection method, isoGS, recovers some of that loss.
- **Why it matters**: Breeders must balance adding new genetic diversity against keeping the traits that make elite varieties valuable, and this work offers a way to measure and manage that trade-off trait by trait. Because the results come only from simulations, how far they carry over to real breeding programs is not established by this text.
- **Background needed**: - Crop breeding: developing new plant varieties by crossing and selecting lines with desired traits.
- Elite germplasm: the best-performing breeding lines and seeds already in use.
- Genomic selection (GS): predicting a plant's value from its DNA markers so that breeders can pick plants without growing every one to maturity.
- Genetic gain: the improvement in a trait over successive breeding cycles.
- QTL (quantitative trait loci): stretches of DNA linked to a trait that is controlled by many genes.
- Epistasis and haplotypes: genes interacting with one another, and blocks of DNA inherited together; breaking up favorable combinations can reduce performance.
- Transgressive segregation: offspring that show traits more extreme than either parent, which can be useful or undesirable.
- Hamming distance: a count of positions where two DNA sequences differ, here weighted by how strongly each position affects the trait. · level: research-level

<details><summary>Original abstract</summary>

Global networks of public crop breeding programs exchange germplasm to share traits and increase diversity for genetic gain. There is a fundamental dilemma in crop breeding between the need to expand the genetic variation in elite gene pools while avoiding disruptions to essential traits required for eliteness. One particular challenge in admixed germplasm is the release of undesired transgressive segregation due to the disruption of favorable epistatic haplotypes of essential traits, which may stymie deployment of genomic selection (GS) In this study, we used breeding simulations to model recurrent population improvement for an annual crop species that can be selfed and crossed to examine the effectiveness of GS in admixed germplasm. We quantified the genetic heterogeneity between founder lines with an isoeliteness score, an effect size-weighted Hamming distance using quantitative trait loci markers. Populations with low founder isoeliteness (i.e. low genetic compatibility) had lower genetic gain with GS in early cycles than those with high founder isoeliteness (63% and 27% lower after 2 and 4 cycles). To mitigate this, we developed an isoeliteness-guided GS (isoGS) method to recover favorable epistatic haplotypes in a segregating population, which enabled 31% and 15% more genetic gain after 4 and 20 cycles. Our results suggest that founder isoeliteness scores and isoGS are valuable tools for overcoming the diversity vs. eliteness dilemma by managing the introduction of genetic diversity in a trait-specific manner.

</details>

## Cell and molecular biology

### [Allele-specific open chromatin analysis revealed allelic bias of alcohol-induced gene expression in human microglia](https://www.biorxiv.org/content/10.64898/2026.11.23.768544v1)
*Li, X.; Green, N.; Messenger, J. S. et al.* · `cell biology` · bioRxiv doi:10.64898/2026.11.23.768544 v1 · relevance 0.10

- **In one sentence**: Integrating microglia-specific allele-specific open chromatin mapping with GWAS, eQTL, and expression data, the authors prioritize the AUD-associated non-coding variant rs7307261 and report that its minor allele is linked to higher ethanol-induced CD163 expression and altered phagocytosis in microglia-like cells.
- **In plain words**: Alcohol use disorder is influenced by many genetic variants, most of which sit in stretches of DNA that do not code for proteins, so it is unclear which ones actually matter. This study combined several datasets from human brain immune cells (microglia) and lab-grown microglia-like cells to narrow down candidates, then tested one variant, rs7307261, in experiments. The authors report that this variant's minor allele was tied to higher CD163 expression after alcohol exposure, and that changing the variant altered both that response and the cells' ability to engulf material.
- **Why it matters**: It offers a concrete example of moving from a genetic association found in population studies to a specific regulatory variant, target gene, and cell behavior, which is a hard step in psychiatric genetics. The text does not establish how these cellular changes relate to drinking behavior or disease in people, so its clinical relevance remains unclear.
- **Background needed**: - GWAS (genome-wide association study): a scan of many people's genomes to find variants statistically linked to a trait or disease.
- Non-coding variant: a DNA change outside protein-coding genes that can still affect how much a gene is switched on.
- Allele: one of the alternative forms of a DNA letter at a given position; a person carries two copies, and the minor allele is the less common form.
- Open chromatin / ATAC-seq: regions where DNA is loosely packed and accessible to regulatory proteins, often marking active control elements.
- eQTL: a genetic variant associated with the level of expression of a nearby gene.
- Transcription factor motif: a short DNA sequence that a regulatory protein binds; ETS-family factors such as FLI1 and ELF2 are examples.
- Microglia: immune cells of the brain that clear debris and respond to injury; CD163 is a marker associated with some of their states.
- iPSC-derived cells: cells made by reprogramming adult cells into stem-like cells and then coaxing them into a target cell type.
- Phagocytosis: a cell engulfing and digesting particles or debris. · level: research-level

<details><summary>Original abstract</summary>

Alcohol use disorder (AUD) is a polygenic disorder. Most AUD-associated variants identified by genome-wide association studies (GWAS) are located in non-coding regions, making it challenging to determine which variants are functional and how they contribute to disease-relevant cellular phenotypes. Here, we integrated microglia-specific allele-specific open chromatin (ASoC) mapping, GWAS, eQTLs, differentially expressed genes identified from postmortem human microglia and iPSC-derived microglial-like cells, and chromatin accessibility (ATAC-seq) data from postmortem microglia to prioritize regulatory variants, followed by functional validation using multiple assays. We identified a panel of AUD-associated non-coding variants, particularly rs7307261, as a candidate functional variant that showed regulatory potential. The minor allele (A) of rs7307261 showed higher predicted similarity to binding motifs for E26 transformation-specific (ETS)-family transcription factors, including FLI1 and ELF2, than the G allele. The A allele was also associated with increased CD163 expression in AUD postmortem microglia and in iPSC-derived microglial-like cells after ethanol exposure. Notably, the ethanol-induced CD163 expression was abolished by knocking out rs7307261 or converting rs7307261 A/A to G/G, accompanied by changes in ethanol-induced microglial phagocytic function. Together, our study provides a framework for translating AUD genetic associations into context-specific functional mechanisms by linking non-coding risk variants to target genes and ethanol-induced cellular phenotypes.

</details>

### [Spatiotemporal Dynamics of Vascular Wall Cells during Ductus Arteriosus Development and Closure](https://www.biorxiv.org/content/10.64898/2026.11.23.768583v1)
*Sanderson, C.; Dahal, I.; Sinha, A. et al.* · `developmental biology` · bioRxiv doi:10.64898/2026.11.23.768583 v1 · relevance 0.09

- **In one sentence**: Spatial transcriptomic profiling of mouse ductus arteriosus (DA) and aorta from E14.5 to P2.5, with a human DA comparison, mapping temporal changes in mural, endothelial and fibroblast gene programs during DA closure.
- **In plain words**: Before birth, a short blood vessel called the ductus arteriosus lets blood bypass the lungs; after birth it must close so that blood flows to the lungs. This study followed the mouse version of this vessel, and the nearby aorta, at five stages from late pregnancy to two days after birth, measuring which genes were active in different cell types within tissue slices. The authors also looked at a human postnatal ductus and an external mouse single-cell dataset to check selected findings.
- **Why it matters**: Failure of this vessel to close is a known cause of heart defects in newborns, so a map of how its wall cells change over time may be useful background for that problem. The text does not show clinical applications, so any link to treatment is speculative.
- **Background needed**: - Ductus arteriosus: a fetal blood vessel connecting the main artery from the heart (aorta) and the lung artery; it normally closes after birth.
- Vascular wall cells: smooth muscle-like "mural" cells, endothelial cells lining the inside, and fibroblasts in the outer layer.
- Contractile vs. synthetic cell states: contractile cells squeeze the vessel; synthetic cells make structural material and remodel tissue.
- Extracellular matrix and elastic lamellae: the scaffolding and elastic sheets that give vessel walls strength and stretch.
- Spatial transcriptomics: measuring which genes are active at specific locations in a tissue slice, so each result can be tied to a position.
- Single-cell RNA sequencing: measuring gene activity in individual cells, used here as a comparison dataset. · level: research-level

<details><summary>Original abstract</summary>

Background: The transition from fetal to postnatal circulation requires closure of the ductus arteriosus (DA), involving smooth muscle cell contraction followed by anatomical remodeling. However, the spatial organization and developmental transcriptional dynamics of vascular wall cells during this transition remain poorly understood. Methods: We analyzed vascular morphology and spatial transcript profiles of the mouse DA and aorta at five stages from embryonic day 14.5 (E14.5) to postnatal day 2.5 (P2.5), enabling paired comparisons within tissue sections. Selected findings were compared with an independent mouse single-cell RNA-sequencing dataset. Histological and spatial transcript analyses were also performed on human DA tissue and the adjacent pulmonary artery. Results: The DA exhibited transiently higher cell-cycle-associated transcription across multiple vascular wall populations at E16.5, preceding medial thickening at E18.5 and postnatal luminal closure. Prenatally, DA mural cells exhibited greater contractile-associated gene expression than aortic mural cells. This difference diminished after birth, accompanied by a marked shift toward synthetic-like transcriptional programs associated with extracellular matrix remodeling and proteolysis. Ductal endothelial cells exhibited postnatal divergence from aortic endothelial cells in matrix- and adhesion-associated gene expression. Adventitial fibroblasts displayed distinct extracellular matrix- and insulin-like growth factor-associated expression profiles. In a human postnatal DA specimen, synthetic-like mural cells were enriched in regions of disrupted elastic lamellae and prominent collagen staining and shared selected remodeling-associated markers with postnatal mouse DA mural cells. Conclusions: DA development and closure involve temporally organized transcriptional changes across vascular wall populations, characterized by prenatal cell-cycle-associated activity and rapid postnatal reorganization of mural transcriptional programs. These findings provide a spatial framework for understanding vascular cell plasticity and multicellular remodeling during DA closure.

</details>

## Immunology and microbiology

### [mRNA-1273.262 and mRNA-1283.262 Vaccines Expressing XFG Antigens Neutralize Relevant Circulating Variants](https://www.biorxiv.org/content/10.64898/2026.11.18.767652v1)
*Nasir, A.; Ogega, C.; Lee, D. W. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.18.767652 v1 · relevance 0.15

- **In one sentence**: Preclinical report on mRNA vaccine candidates encoding XFG-variant SARS-CoV-2 spike antigens (full-length and linked subdomain formats), showing neutralizing responses against JN.1-family variants in primary and booster animal models, to support XFG as the 2026-2027 season vaccine strain.
- **In plain words**: Every year, COVID-19 vaccines have to be updated to match the version of the virus that is spreading. This paper reports animal experiments on new mRNA vaccines built around a virus variant called XFG, which the authors propose for the 2026-2027 season. In the animals, the vaccines produced antibodies that neutralized (blocked) related variants from the JN.1 family.
- **Why it matters**: Choosing which viral version a vaccine targets each year affects how well people are protected, so this shows the preclinical basis for one such choice. The text is a short summary, so it does not give the sample sizes, comparison groups, or how the choice was validated against other candidates; the broader value depends on the full study.
- **Background needed**: - SARS-CoV-2 is the virus that causes COVID-19; it is now endemic, meaning it keeps circulating.
- The spike protein is the viral surface protein that vaccines teach the immune system to recognize.
- mRNA vaccines deliver a genetic message that cells use to make the antigen (the target protein) temporarily.
- Neutralizing antibodies are immune proteins that block the virus from infecting cells.
- JN.1 and XFG are named lineages (variants) of the Omicron family of SARS-CoV-2.
- "Preclinical" means tested in cells and animals, not yet in human trials.
- "Primary series" is the initial vaccination; "booster" is a later extra dose. · level: research-level

<details><summary>Original abstract</summary>

SARS-CoV-2 continues to circulate and causes substantial disease burden as an endemic respiratory pathogen. Vaccination is a key public health measure to ameliorate the effects of COVID-19 disease but requires annual update to match strains that are circulating. Monitoring of circulating virus and characterization of matched candidate vaccines helps to inform which antigens will provide the greatest benefit to public well-being. The 2026-2027 season will leverage XFG as the variant of interest for vaccine production and in vitro and in vivo data was generated preclinically to support this selection. XFG variant vaccines express well in mRNA format as both full-length spike and linked subdomain antigen formats. Animals immunized with these vaccines elicit robust neutralizing responses to relevant JN.1-family virus variants in both primary series and booster models. In future seasons, robust epidemiologically monitoring including viral genome sequencing will improve early detection of relevant variants and subsequent preparation of vaccine antigens.

</details>

### [Longitudinal multiomics analysis in blood from individuals before and after HIV acquisition](https://www.biorxiv.org/content/10.64898/2026.11.23.767218v1)
*Moron-Lopez, S.; Garrido-Sanz, L.; Soriaga, L. et al.* · `immunology` · bioRxiv doi:10.64898/2026.11.23.767218 v1 · relevance 0.13

- **In one sentence**: A longitudinal single-nucleus multiome and multiomics study of PBMCs and plasma from five people sampled before HIV acquisition, during early infection, and after at least six months of ART, reporting cell-type-specific chromatin and transcriptional changes, rare HIV-positive cells, and transient versus persistent inflammatory and metabolic signals.
- **In plain words**: This study follows five people through the period before they became infected with HIV, the early weeks of infection, and then after months of antiretroviral drugs that suppress the virus. The researchers measured immune cells at the level of individual cell nuclei, looking at which genes are switched on and how the DNA is packaged, along with chemicals in the blood. They found that some immune changes faded after treatment began, while others, including certain metabolic shifts, lasted.
- **Why it matters**: Samples taken before HIV infection are rare, so a paired before-and-after view of the same people is unusual and can show which changes come from the infection itself. The small number of participants (five) limits how far the findings can be generalized, and the text does not say how these changes relate to HIV cure strategies beyond framing them as relevant to that field.
- **Background needed**: - PBMCs: peripheral blood mononuclear cells, the white blood cells found in circulating blood.
- Single-nucleus multiome: a method that reads, in the same cell nucleus, which DNA regions are open for gene activity (chromatin accessibility) and which genes are being expressed (transcription).
- Multiomics: combining several layers of biological measurement (genes, proteins, metabolites, lipids) in one study.
- ART: antiretroviral therapy, daily drugs that keep HIV at undetectable levels but do not remove it from the body.
- HIV cure research: work aiming to eliminate or permanently control the virus after treatment stops.
- Interferon and NF-kB programs: standard immune alarm and inflammation gene sets.
- IP-10, IFI44L, ATAD3A: a blood signaling protein and two genes named in the study.
- Nominal decrease: a drop that reached a threshold of statistical significance on its own, without correction for testing many measures, so it should be read cautiously. · level: research-level

<details><summary>Original abstract</summary>

A comprehensive understanding of cellular immunity is essential for controlling viral infections, yet individual and coordinated immune responses continue to pose significant challenges in HIV cure research. Recent advances in single-cell and multiomics technologies provide powerful tools to dissect intricate multicellular behaviors and identify novel therapeutic targets. Direct characterization of HIV-induced immune alterations is challenging because matched samples obtained before HIV acquisition are rare. To better understand individual and coordinated cellular immune responses relevant to HIV cure research, we integrated single-nucleus chromatin-accessibility and transcriptomic profiling of 150,060 PBMCs with plasma metabolome, lipidome and soluble immune-profiling from five individuals before HIV acquisition, during early infection and after at least six months of suppressive antiretroviral therapy (ART). HIV acquisition expanded activated CD8 T and proliferating NK/CD8 T cells and induced cell-type-specific chromatin and transcriptional changes enriched for interferon, inflammatory and TNF-NF-{kappa}B programs, many persisting during ART. Multiome sequencing detected 32 HIV-positive cells which were associated with increased expression of IFI44L during early infection and ATAD3A after ART. Plasma IP-10 increased transiently, whereas eight energy- or amino-acid-related metabolites showed nominal decreases persisting after ART. These paired observations distinguish transient inflammatory responses from persistent molecular and metabolic perturbations after HIV acquisition.

</details>

## Cancer biology

### [Fishing for new immunotherapy compounds to boost innate tumor rejection](https://www.biorxiv.org/content/10.64898/2026.11.15.766748v1)
*Machado, A. B.; Labao-Almeida, C.; Oliveira, I. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.15.766748 v1 · relevance 0.10

- **In one sentence**: In vivo phenotypic screen of over 500 FDA-approved drugs in zebrafish xenografts of human colorectal and breast tumors identifies tiotropium (a muscarinic antagonist) as a myeloid-reprogramming compound that synergizes with anti-PD-1 in a syngeneic CT26 mouse model.
- **In plain words**: Some tumors are cleared by the immune system when transplanted into zebrafish, while others take hold, and the researchers used this difference to test existing approved drugs for ones that help the body clear tumors. They screened over 500 drugs and found 23 hits, with drugs acting on the nerves that control involuntary body functions (especially cholinergic ones) overrepresented. The lead, tiotropium, appeared to shift tumor-associated macrophages (immune cells) toward an inflammatory, anti-tumor state, and in mice it worked better together with an anti-PD-1 checkpoint drug than either alone.
- **Why it matters**: It proposes a new route for drug discovery, using whole-animal screening to find innate immune targets, and points to the nerve-immune connection as a possible lever against immunotherapy resistance. The evidence so far comes from zebrafish and one mouse model, and the text does not establish that the effect carries over to patients.
- **Background needed**: - Innate immunity: the body's first-line immune defense, which does not need prior training; macrophages are a key cell type in it.
- Xenograft: transplanting human tumor cells into another animal (here, zebrafish embryos or larvae).
- Phenotypic screen: testing many compounds and looking for a visible outcome (here, tumor clearance) without knowing the target in advance.
- Muscarinic/cholinergic: relating to receptors that respond to acetylcholine, a nerve signaling chemical; antagonists block these receptors.
- Anti-PD-1: an immunotherapy antibody that releases a brake on T cells.
- Syngeneic model: mice with a tumor from the same genetic background, so the immune system is intact; NSG mice lack much of their immune system and were used as a control.
- Phagocytosis: immune cells engulfing debris or cancer cells. · level: research-level

<details><summary>Original abstract</summary>

Despite significant advances in cancer immunotherapy, tackling immunosuppression remains critical to achieve more effective responses. While developing the zebrafish xenograft model, we found that some human tumors engraft very efficiently ("progressors"), while others are cleared by the host ("regressors"). We showed that this was dependent on innate immunity, which recognizes and eliminates some cancer cells, while others are able to evade and suppress it. This opened an opportunity to perform an in vivo phenotypic drug screen to find compounds that induce clearance by boosting innate-tumor rejection. Zebrafish xenografts of human colorectal (CRC) and breast cancer (BC) that show a high engraftment/low clearance phenotype were used to screen over 500 FDA-approved small-molecule compounds, with tumor clearance serving as the phenotypic readout. The screen identified 23 hit compounds, of which six were effective across both cancer models. Mechanism-of-action enrichment analysis revealed a significant overrepresentation of autonomic nervous system-targeting drugs among the hits, particularly cholinergic ones. Immune profiling in myeloid reporter lines showed that the lead hit, Tiotropium bromide, a muscarinic receptor antagonist, reprograms tumor-associated macrophages toward a pro-inflammatory, anti-tumoral state. Tiotropium significantly increased macrophage phagocytosis, and macrophage depletion completely abolished its pro-clearance activity, establishing these myeloid cells as essential effectors. In a syngeneic CT26 colorectal mouse model, Tiotropium synergized with anti-PD-1 to control tumor growth and improve survival, outperforming all monotherapy arms. This effect was immune-dependent, as it was lost in immunodeficient NSG mice. Together, these findings demonstrate that in vivo phenotypic screening of FDA-approved compounds in zebrafish xenografts is a productive strategy for innate immune drug discovery in cancer. The identification of Tiotropium as a myeloid-reprogramming innate immune primer, together with the unbiased recovery of the neuro-immune axis as a druggable target, opens new avenues for overcoming immunotherapy resistance.

</details>

### [Beyond IgG: Oral Secretory IgA as a new efficient modality for cancer immunotherapy](https://www.biorxiv.org/content/10.64898/2026.11.23.768496v1)
*Brousse, M.; Pintat, A.; Favre-Bulle, O. et al.* · `cancer biology` · bioRxiv doi:10.64898/2026.11.23.768496 v1 · relevance 0.09

- **In one sentence**: Preclinical study testing an orally delivered anti-CEACAM5 secretory IgA antibody (ABC-101) in human colorectal and gastric cancer mouse models, alone and with chemotherapy, compared with an IgG1 version and cetuximab.
- **In plain words**: Most cancer antibody drugs are given by injection into the bloodstream. This paper tests whether an antibody swallowed as a pill-like oral dose could reach and act on colorectal tumors in mice. The authors report that the oral antibody built up in CEACAM5-positive tumors and metastases while staying at low levels in the rest of the body, and that it slowed tumor growth and spread more than the comparison antibodies.
- **Why it matters**: Oral antibodies would be a new route for cancer drugs, and the paper suggests the gut's mucosal immune system could be used to treat distant tumors. The results come only from animal models described in this summary, so it is not yet clear whether they will hold in people; the text does not report any human testing.
- **Background needed**: - Antibodies (IgG) are Y-shaped immune proteins; many cancer drugs are built from them and given intravenously.
- Secretory IgA (SIgA) is the main antibody type found in mucus and gut secretions, and it is normally resistant to digestion.
- CEACAM5 is a protein found at high levels on many colorectal and gastric cancer cells; it is the drug's target.
- Cetuximab is an approved antibody drug used against colorectal cancer; it serves here as a comparator.
- Irinotecan and FOLFIRI are standard chemotherapy regimens for colorectal cancer.
- CD89 (FcαRI) is a receptor on innate immune cells such as neutrophils and macrophages, which the antibody appears to recruit into tumors.
- Orthotopic models place human tumor cells in the matching organ of a mouse, which better mimics real disease than tumors under the skin. · level: research-level

<details><summary>Original abstract</summary>

Monoclonal antibody therapies have revolutionized cancer treatment but are almost exclusively based on intravenously administered IgG antibodies. Here, we developed and evaluated the first orally delivered anti-CEACAM5 secretory IgA (SIgA) for colorectal cancer. The pharmacokinetics, biodistribution, antitumor efficacy and immune effects of oral anti-CEACAM5 SIgA (ABC-101) were evaluated in an orthotopic metastatic human colorectal cancer model. Its therapeutic activity was compared with cetuximab, as monotherapy and in combination with irinotecan- or FOLFIRI-based chemotherapy along with that of an anti-CEACAM5 IgG1 sharing the same antigen-binding domain. Tumor-associated FcRI (CD89)-expressing myeloid populations were characterized at primary and metastatic sites. ABC-101 activity was evaluated on a second human cancer cell line, in vivo in an orthotopic human gastric cancer model. Oral anti-CEACAM5 SIgA (ABC-101) exhibited a unique pharmacokinetic profile, selectively accumulating in CEACAM5-positive primary tumors and metastases while maintaining minimal systemic exposure. Compared with the anti-CEACAM5 IgG1 and cetuximab, oral SIgA achieved superior inhibition of primary tumor growth and metastatic dissemination. It also enhanced the efficacy of irinotecan- and FOLFIRI-based chemotherapy, outperforming the FOLFIRI/cetuximab standard-of-care comparator. Mechanistically, ABC-101 remodeled the tumor immune microenvironment by promoting the recruitment of FcRI (CD89)-expressing neutrophils, monocytes, macrophages, and dendritic cells at both primary and metastatic sites, consistent with enhanced innate antitumor activity. Oral ABC-101 shows targeted activity against CEAhigh MKN-45 cells, reducing markers of cell proliferation and migration. These findings establish therapeutic SIgA as a first-in-class oral antibody immunotherapy combining selective tumor targeting, innate immune activation, and enhanced chemotherapy efficacy. More broadly, this work establishes mucosal immunity as a promising therapeutic frontier, demonstrating that orally delivered antibodies can enable systemic control of metastatic digestive cancers.

</details>

## Ecology and evolution

### [Social information use promotes breeding synchrony but constrains adaptation to rapid environmental changes](https://www.biorxiv.org/content/10.64898/2026.11.20.767538v1)
*Zheng, J.; Kuijper, B.; Aplin, L. M. et al.* · `animal behavior and cognition` · bioRxiv doi:10.64898/2026.11.20.767538 v1 · relevance 0.09

- **In one sentence**: An evolutionary individual-based model shows that breeders using neighbours' timing cues synchronise their breeding, which speeds adaptation in stable or fluctuating conditions but lags behind under directional climate change.
- **In plain words**: The paper asks how animals that nest in territories decide when to breed, and whether watching their neighbours helps or hurts when the climate is shifting. Using a computer simulation of populations that evolve over time, the authors compare individuals that use only their own sensing with individuals that also copy cues from nearby neighbours. Copying neighbours makes breeding times line up across the population, which helps under stable conditions but makes the population slow to follow a steadily warming climate.
- **Why it matters**: Timing of breeding is shifting with climate in many species, and this work suggests that social learning, often assumed to be beneficial, can become a liability when conditions change quickly. It is a modelling study, so its conclusions depend on the assumptions built into the simulation and would need testing against field data.
- **Background needed**: - Phenology: the timing of seasonal events such as breeding or flowering.
- Social information: cues gained by observing others, such as neighbours starting to breed.
- Private information: cues an individual gathers itself, such as local temperature or food.
- Individual-based model: a simulation where each animal is tracked separately and the population evolves through selection on traits.
- Synchrony: many individuals acting at the same time, which can build through positive feedback when each copies the others.
- Adaptive lag: the population's timing trails behind a moving environmental optimum.
- Peaked resources: food availability that is highest at one point in the season and falls off either side. · level: intermediate

<details><summary>Original abstract</summary>

Animals use social information to make decisions, yet how such processes influence predictions in reproductive timing and population adaptation under environmental change remains unclear. While social information can improve decision accuracy through information pooling, spatiotemporal heterogeneity in conditions and patterns of environmental changes creates noise that potentially limits the value of social information use among breeding individuals. Here, we established an evolutionary individual-based model to examine how social and private sensing interact to shape breeding phenology in species distributed across territories with peaked resources and facing annual fluctuations and rapid climate change. We show that when individuals incorporate social information from neighbours, behavioural responses become increasingly synchronised through positive feedback in decision-making. This emergent synchrony helps populations to adapt faster and can increase reproductive output under stable environmental conditions relative to relying only on private information. However, under directional climate change, the same mechanism reduces population responsiveness by constraining variation in individual responses, leading to systematic lag in tracking shifting environmental optima and reduced population reproductive output. Our results demonstrate that social information use can produce a general trade-off at the population level between synchronisation and adaptive flexibility across environmental contexts. Social interaction enhances population performance when environments are either consistent or changing drastically across both spatial and temporal scales. Rather than uniformly improving performance, social interaction may create conditions under which collective behaviour becomes maladaptive when environments change rapidly.

</details>

### [Stomatal conductance and net photosynthesis depend on nitrogen supply in drought-limited boreal forest](https://www.biorxiv.org/content/10.64898/2026.11.23.768591v1)
*Dulamsuren, C.; Amarjargal, D.; Bazar, D. et al.* · `ecology` · bioRxiv doi:10.64898/2026.11.23.768591 v1 · relevance 0.09

- **In one sentence**: In drought-limited Larix sibirica stands in Mongolia, branch gas-exchange measurements show stomatal conductance rises with nitrogen supply, while net photosynthesis peaks at a moderate fertilization rate and falls at the highest.
- **In plain words**: Boreal forests, the cold northern woodlands, are becoming drier as the climate warms, and this study asks whether soil nutrients change how trees cope with that dryness. Researchers fertilized larch trees in a dry Mongolian forest at three nitrogen levels and measured how the branches exchanged carbon dioxide and water vapor. They found that the pores on leaves opened wider with more nitrogen, but carbon gain was lowest at the lowest dose, highest at the middle dose, and dropped at the highest dose.
- **Why it matters**: The authors argue that climate studies of boreal drought tolerance should include nitrogen availability, which they say may be falling in remote forests because of rising atmospheric CO2 and can be shifted locally by land use. The text does not show how far these branch-level results apply to whole forests or over longer periods.
- **Background needed**: - Boreal forest: cold-climate forest dominated by conifers such as larch; historically limited by cold, now increasingly by drought.
- Nitrogen fertilization experiment: plots given measured doses of nitrogen, a nutrient plants need, to see how growth and physiology respond.
- Stomata: tiny pores on leaves that let in CO2 and let out water vapor; stomatal conductance measures how open they are.
- Net photosynthesis: the net rate at which a plant takes up CO2 to make sugars, after subtracting CO2 released by respiration.
- Vapor pressure deficit: how strongly dry the air is, which pulls water out of leaves.
- Gas exchange measurements: sensors clamped on branches that record CO2 and water vapor flows. · level: intermediate

<details><summary>Original abstract</summary>

Transition from cold limitation to drought limitation due to climate change is widespread in boreal forests. We explored in the scope of the Dry Boreal Forest Long-Term Nitrogen Fertilization Experiment (DryBoreal-LTNE) in southern boreal forests of Mongolia how N supply interacts with tree water and C relations in forests of Larix sibirica, which are naturally drought-limited. Using branches of mature L. sibirica subjected to N fertilization of 6.25-25 kg N ha-1 a-1, we conducted CO2/H2O gas exchange measurements to examine how N availability interferes with the climatic control of stomatal conductance (gs) in L. sibirica. We tested the hypotheses that gs increases with increasing N availability and that this increase can be translated into increased net photosynthesis (A) in L. sibirica even under the dry continental climate of Mongolia. We could confirm the first hypothesis and found that A decreased at low fertilization (6.25 kg N ha-1 a-1) probably caused by increases in respiration due to metabolic costs of intensified N uptake. A attained the highest values at 12.5 kg N ha-1 a-1, but declined at the highest fertilization level of 25 kg N ha-1 a-1. Our results demonstrate that research on the drought tolerance of boreal forests under climate change should not only focus on changes in temperature, vapor pressure deficit, and precipitation, but should take N availability into account, especially as N availability is thought to decrease in remote boreal forests due to elevated atmospheric CO2 concentrations and can be locally influenced by land use.

</details>

## Plant biology

### [Restoring beneficial ancestral genomic sites enhances broad disease resistance in rice](https://www.biorxiv.org/content/10.64898/2026.11.22.768253v1)
*Wang, J.; Liu, S.; Duan, Y. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.22.768253 v1 · relevance 0.16

- **In one sentence**: The paper proposes "Beneficial Ancestral Genomic Sites," restoring ancestral acidic residues at phosphorylatable sites in plant proteins, and reports that doing so in the rice NADPH oxidases OsRbohB and OsRbohI raised broad-spectrum disease resistance, with field tests of growth-defense tradeoff models.
- **In plain words**: Crop breeders usually work only with the genetic variation already present in farmed plants and their wild relatives. This paper proposes going back further in evolutionary history: restoring an older, ancestral version of specific chemical sites in plant proteins. The authors tested this in rice by changing two immune-related enzymes so they resemble their ancestral form, and report that this raised resistance to several diseases.
- **Background needed**: - Proteins are chains of amino acids; some amino acids can have a phosphate group attached (phosphorylation), which can switch a protein's activity on or off.
- Acidic residues carry a negative charge and can sometimes mimic a phosphate group at these sites.
- NADPH oxidases (Rboh enzymes) produce reactive oxygen molecules that plants use as part of their immune response.
- Growth-defense tradeoff: resources spent on defense can reduce growth or yield, and the paper tests competing models of this tradeoff in the field.
- Ancestral sequence reconstruction: inferring what a gene looked like in ancient ancestors, which is the source of the "ancestral" sites here. · level: research-level

<details><summary>Original abstract</summary>

Crop improvement has long been constrained to genetic variations within cultivated germplasms and their wild relatives, which capture only a small fraction of historical protein diversity accumulated over evolutionary processes. Here, we propose the Beneficial Ancestral Genomic Sites concept, hypothesizing that restoring conserved ancestral acidic residues at phosphorylatable sites in plant proteins could substantially improve plant performance. We experimentally validate this concept with key immune-associated NADPH oxidases OsRbohB and OsRbohI to elevate broad-spectrum disease resistance in rice. Field-level testing of two competing models for growth-defense tradeoffs in plants strongly supports mitigating tradeoffs in modern agricultural settings. Our work unlocks a hidden, untapped reservoir of elite molecular variations inaccessible from conventional breeding resources, establishing a potentially transformative strategy for next-generation crop improvement under modern agriculture contexts.

</details>

### [GnotoBag: A versatile peat-based gnotobiotic system for plant microbiome research beyond model species](https://www.biorxiv.org/content/10.64898/2026.11.22.768464v1)
*Wu, N.; Cheng, Y. T.; Paasch, B. C. et al.* · `plant biology` · bioRxiv doi:10.64898/2026.11.22.768464 v1 · relevance 0.06

- **In one sentence**: The paper presents GnotoBag, a bag-based, peat-substrate gnotobiotic (germ-controlled) growth system that extends a prior platform to allow longer, sterile-condition cultivation of Arabidopsis and larger crops such as rice and tomato.
- **In plain words**: Scientists who study how microbes living around plant roots affect plant growth need plants that can be grown without unwanted microbes for long periods. This paper describes a modified growing setup, made from bags filled with peat, that improves airflow and adds a built-in way to supply water and nutrients. The authors report that it keeps small model plants growing through flowering and gives bigger plants like rice and tomato room to grow for at least four weeks.
- **Why it matters**: Controlled, microbe-free growth makes it easier to tell which effects come from specific microbes rather than from background noise, which matters for future work on crop productivity. The text does not report any measured benefit to crop yield, so the link to agriculture is a stated goal rather than a shown result.
- **Background needed**: - Gnotobiotic means growing organisms in a setting where the microbial community is fully known, usually by starting from sterile conditions and adding back chosen microbes.
- Axenic means free of all other organisms; keeping it that way is hard over weeks or months.
- The plant microbiome is the community of bacteria, fungi and other microbes living on and inside plants, especially in the roots.
- Arabidopsis thaliana is a small flowering plant widely used as a laboratory model.
- The previous platform had a 6.5-week workflow; GnotoBag aims to go beyond that.
- Peat is an organic growing medium; the "headspace" is the air space above the growing material. · level: intermediate

<details><summary>Original abstract</summary>

Plants and their microbial communities form a symbiotic system, where microbial communities play a key role in plant growth, development and stress resilience. However, the molecular mechanisms underlying plant-microbiota interactions remain poorly understood. A practical challenge is maintaining axenic conditions during prolonged plant growth while providing adequate space, ventilation, water, and nutrients. To advance research on plant-microbiome interactions, we developed the "GnotoBag" system, a bag-based extension of a previously established peat-based gnotobiotic plant growth platform. Key improvements of this GnotoBag system include enhanced ventilation and an integrated nutrient and water delivery system that sustains plant growth. These modifications support prolonged cultivation beyond the previously described 6.5-week workflow, enabling studies of microbiome effects on Arabidopsis thaliana growth and development under controlled microbial conditions, including the transition from vegetative to reproductive growth. Additionally, the expanded headspace of the GnotoBag provides sufficient space for cultivating larger plants, including rice and tomato, for at least four weeks. The increased headspace and the ability to add nutrients and water support research on larger crop plants, laying a foundation for future studies of microbiome functions in agricultural production.

</details>

## Bioengineering and synthetic biology

### [Extracellular matrix-enriched human induced chondrocyte organoids as living building blocks for scalable cartilage tissue engineering](https://www.biorxiv.org/content/10.64898/2026.11.23.768121v1)
*Menssen, D. M. A.; Mazzini, G.; Abinzano, F. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.23.768121 v1 · relevance 0.13

- **In one sentence**: Human induced chondrocytes (hiCHOs), matured in spinner flasks and then reaggregated with a tissue-derived matrix supplement, self-assemble into matrix-rich cartilage organoids that can fuse into larger constructs.
- **In plain words**: Cartilage damage in joints often leads to painful arthritis, and current repair methods need many of a patient's own cells and scale poorly. This paper describes growing cartilage-like clusters, called organoids, from stem-cell-derived cartilage cells in a spinning culture flask, with a natural matrix supplement added to help them form. The authors report that one million cells gave over 27,000 organoids in two weeks, and that these organoids could join together into larger pieces of cartilage.
- **Why it matters**: The main claim is about scalability: making many cartilage building blocks from an off-the-shelf cell source could matter for future joint repair. The text does not show clinical testing, so its relevance to patients is still a possibility to be tested rather than a demonstrated result.
- **Background needed**: - Articular cartilage: the smooth tissue covering joint ends; it heals poorly, and damage can progress to osteoarthritis.
- Tissue engineering: growing tissue in the lab to repair or replace damaged body parts.
- Induced pluripotent or progenitor cells: adult cells reprogrammed into a stem-like state, then guided to become a target cell type (here, chondrocytes, the cartilage-making cells).
- Organoid: a small 3D cell cluster that self-organizes and mimics aspects of a tissue.
- Spinner flask: a stirred culture vessel that keeps cells suspended and moving, allowing larger batches.
- Extracellular matrix: the protein-and-sugar scaffolding cells secrete; here, a tissue-derived supplement is added to support it.
- Autologous: taken from the patient themselves; off-the-shelf means a ready-made, donor-independent supply. · level: research-level

<details><summary>Original abstract</summary>

Articular cartilage defects are common and often develop into painful and debilitating osteoarthritis due to the low innate healing capacity of cartilage. However, current regenerative treatments are limited as they depend on large autologous cell numbers and poor scalability. Here, a novel approach for rapid and plentiful cartilage organoid production is introduced for modular and scalable cartilage tissue engineering, by combining an off-the-shelf cell source with a natural matrix supplement in spinner flask cultures. First, human induced chondroprogenitor cell (hiCPC) colonies are matured towards human induced chondrocytes (hiCHO) aggregates in spinner flasks. Although maturation is achieved, resulting hiCHO aggregates show some phenotypic heterogeneity between clones. Nevertheless, subsequent dissociation and culture with a tissue-derived matrix supplement results in rapid and homogeneous organoid self-assembly, generating large numbers of hiCHO-derived cartilage organoids. This matrix-supplemented culture generates consistent pericellular and extracellular matrix-rich organoids without detected off-target cells, limiting the need of labor-intensive selections steps and enhancing scalability. Impressively, 1 million hiCHOs produce over 27,000 organoids within two weeks, with an approximately 30-fold increase in cell number. Finally, hiCHO-derived organoids fuse together to assemble large cartilage constructs, demonstrating their potential as scalable, off-the-shelf building blocks and addressing an unmet need in regenerative cartilage tissue engineering.

</details>

### [Plasma-Polymerized Polyurethane/Reduced Graphene Oxide Electrospun Patch for Cardiac Tissue Engineering](https://www.biorxiv.org/content/10.64898/2026.11.22.768432v1)
*Jugie, C.; Mousavi, A.; Nemati, A. et al.* · `bioengineering` · bioRxiv doi:10.64898/2026.11.22.768432 v1 · relevance 0.12

- **In one sentence**: Electrospun polyurethane fiber patches containing reduced graphene oxide, surface-coated with a nitrogen-rich plasma polymer, are characterized for structure, strength, conductivity, and cytotoxicity toward primary cardiac fibroblasts as a candidate cardiac tissue engineering scaffold.
- **In plain words**: Heart disease is a leading cause of death, and heart transplants are limited by few donors and lifelong immune-suppressing drugs. This paper describes a thin, flexible mesh-like patch meant to support heart tissue and conduct electrical signals, made from a plastic-like polymer mixed with a conductive carbon material. The authors report physical, electrical, and mechanical measurements and show the patch was not toxic to heart fibroblast cells in lab tests.
- **Why it matters**: Cardiac patches that are both strong and electrically conductive could matter for repairing damaged heart muscle, which must contract in coordinated electrical waves. The text reports only material characterization and a single cytotoxicity assay, so it does not show whether the patch helps heart tissue repair or works in living animals.
- **Background needed**: - Cardiac patch: a sheet placed on damaged heart tissue to provide support and help regrowth.
- Electrospinning: a method that uses an electric field to draw polymer solutions into very fine fibers, forming a mesh.
- Polyurethane (PU): a flexible, durable plastic often used in medical devices.
- Graphene oxide and reduced graphene oxide (rGO): sheets of carbon atoms; the reduced form conducts electricity better.
- Low-pressure plasma polymerization: treating a surface with ionized gas to deposit a thin coating; here nitrogen-rich, meant to help cells stick.
- Cytotoxicity assay: a lab test checking whether a material harms cells.
- Primary cardiac fibroblasts: connective-tissue cells taken directly from heart tissue.
- X-ray photoelectron spectroscopy and tensile testing: surface chemistry analysis and stretch-to-break strength testing. · level: intermediate

<details><summary>Original abstract</summary>

Cardiovascular diseases remain the leading cause of mortality worldwide. Traditional treatments, including heart transplantation, are limited by the scarcity of donor organs and the need for lifelong immunosuppression, highlighting the urgent need for alternative therapies. Cardiac patches represent a promising approach to restoring heart function by providing structural support and promoting cardiac tissue regeneration. Here, we developed biocompatible and conductive electrospun cardiac patches, aiming to mimic the structural, mechanical, and electrical properties of the native myocardium. polyurethane (PU) was selected as the base material due to its favorable mechanical properties and biocompatibility. Reduced graphene oxide (rGO) was incorporated into the electrospun PU fibers to enhance electrical conductivity, and a low-pressure plasma-polymerized nitrogen-rich (LPPE:N) coating was applied to improve cell adhesion. The fabricated patches were characterized through various techniques, including scanning electron microscopy, X-ray photoelectron spectroscopy, tensile testing, and conductivity measurements. Also, in vitro cytotoxicity assay using primary cardiac fibroblasts confirmed the biocompatibility of the patches. These physicochemical, electromechanical, and biological characterizations suggest that the rGO/LPPE:N-functionalized PU patches demonstrate promising potential for cardiac tissue engineering applications.

</details>

## Mathematical biology (arXiv)

### [Turbulent Epidemics: Scale-dependent Fluctuations as a Probe of Population Heterogeneity](https://arxiv.org/abs/2611.31334)
*Bernhard Mueller, Michael Lorke, M. Gabriela M. Gomes et al.* · `q-bio.PE` · arXiv:2611.31334v1 · relevance 0.13

- **In one sentence**: The paper adapts turbulence-style scale-dependent fluctuation analysis to disaggregated COVID-19 case data from Germany's 2020/21 winter wave and uses a new network simulator (Epimetheus) to test which heterogeneity mechanisms, such as clustering and variable susceptibility, could reproduce the observed patterns.
- **In plain words**: Infections rarely spread evenly: some people and groups pass on far more virus than others. This paper borrows a tool from fluid physics, which breaks turbulent motion into fluctuations at different sizes, and applies it to case data from Germany's COVID-19 winter wave of 2020/21. The authors then run computer simulations of an idealized structured population to see which combinations of clustering and variation in susceptibility can reproduce the observed patterns.
- **Why it matters**: The approach offers a way to use the spatial and group-level structure in case data to constrain models of heterogeneous spread, which matters for prediction and for judging the effects of interventions. The text reports only a qualitative comparison between simulation and data, so the conclusions, such as the estimated 0.2 to 0.35 population limit on the outbreak, are tentative and depend on the chosen model.
- **Background needed**: - Heterogeneity in epidemics: individuals and groups differ in how many people they infect (for example, superspreading events).
- Secondary attack rate: the fraction of close contacts of an infected person who become infected.
- Overdispersion: a measure of how much more variable case counts are than a simple random model would predict.
- Fluctuation spectrum: a breakdown of how much variation occurs at each size scale, borrowed from turbulence studies in fluid dynamics.
- Network-based simulation: modeling a population as nodes (people or groups) connected by contacts, and simulating transmission across those links.
- Self-limiting effects: mechanisms such as depletion of susceptible people that slow an outbreak without deliberate intervention. · level: research-level

<details><summary>Original abstract</summary>

Heterogeneous dynamics, including phenomena such as superspreading and clustering, is a hallmark of many infectious diseases. A key challenge lies in identifying observables that constrain heterogeneous dynamics. We here adapt the technique of turbulence decomposition from fluid dynamics to extract scale-dependent fluctuation spectra and correlation functions from disaggregated epidemiological data as a probe of population heterogeneity. To investigate possible explanations for the observed heterogeneities during the COVID-19 winter wave in Germany in 2020/21, we calculate synthetic observables using the new network-based simulation code \textsc{Epimetheus} for an idealized structured population. The code can flexibly incorporate clustering, heterogeneous connectivity and susceptibility, superspreading as well as temporal modulations of transmission risk and factors like waning of immunity and vaccination. A qualitative comparison of simulated and observed fluctuation spectra and correlation functions as well as the secondary attack rate and the overdispersion indicates that both clustering and variations of susceptibility across population substructures of all scales are required to produce the observed dynamics. Combined with heterogeneous connectivity, it is likely that self-limiting effects would have limited the winter outbreak to $0.2\texttt{-}0.35$ of the population without further behavioral changes after the autumn of 2020. A uniform population-wide reduction of transmission risk alone does not adequately explain the observed heterogeneities. Further analysis of the relative contributions and interplay of interventions and self-limiting effects on COVID-19 disease dynamics is required. We outline avenues towards a better integration of heterogeneity in models for predicting infectious disease dynamics and diagnosing effects of interventions.

</details>

### [Normative and neural network models of multisensory integration](https://arxiv.org/abs/2611.32829)
*Marcus Ghosh, John S. Butler* · `q-bio.NC` · arXiv:2611.32829v1 · relevance 0.06

- **In one sentence**: A review that organizes models of multisensory integration into normative (hypothesis-driven, statistically optimal) and neural network (circuit-emulating) classes, with accompanying equations and Python code.
- **In plain words**: This review looks at how brains combine signals from different senses, such as smell, sight and sound, into one picture. It sorts the many existing mathematical and computer models of this process into two groups: those that start from what the brain ideally should do, and those that try to mimic how real networks of neurons could do it. The authors also provide a step-by-step guide with simple equations and Python code, and compare what each approach explains.
- **Why it matters**: Combining senses is a common problem for animals and for artificial systems, so a clear comparison of the two modelling styles may help researchers in neuroscience and AI relate their work. The text does not show specific new results, so its value lies mainly in organizing and teaching existing ideas.
- **Background needed**: - Multisensory integration: merging information from several senses about the same event.
- Statistically optimal integration: weighting each cue by its reliability, so the combined estimate is as precise as possible.
- Normative model: a model built from a hypothesis about what the brain should compute, rather than from its wiring.
- Neural network model: a simulated set of connected units, loosely inspired by neurons, that learns or processes inputs; artificial networks can have billions of parameters.
- Neuron response profile: how a cell's firing rate changes with the stimulus it receives.
- Python code: a programming language; the review includes examples to run. · level: intermediate

<details><summary>Original abstract</summary>

Animals continuously detect scents, sights and sounds, which their brains combine into diverse multisensory streams. Multisensory integration accelerates learning, increases reaction speeds and helps to resolve sensory ambiguities. In studying this process, the field has developed a continuum of models; from concise mathematical equations, with a handful of variables, to artificial neural networks, with billions of parameters. In this review, we divide this spectrum into two classes: normative models start from a hypothesis about how multisensory signals should be integrated, while neural network models aim to emulate how circuits could integrate them. Together, these models demonstrate that observers can integrate cues in a statistically optimal fashion, and help to explain experimental findings, including the diversity of multisensory neuron response profiles and network architectures. In this review, we provide a didactic overview of multisensory models, complete with accessible equations and Python code, and compare their assumptions and explanatory power. We detail what has been learned from these models. Finally, we discuss how the ideas and insights from classical theoretical models can be reconciled with those from artificial neural networks, and how this convergence should shape future research.

</details>

## Epidemiology

### [Improving Prediction of Patient-Reported Health Outcomes Among Older Adults With Diabetes Across Diverse Populations Through Transfer Learning](https://www.medrxiv.org/content/10.64898/2026.11.24.26368865v1)
*Wang, X.; Chen, Y.; Shao, W. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.24.26368865 v1 · relevance 0.08

- **In one sentence**: A regression-based transfer learning approach was tested for predicting patient-reported health outcomes in older adults with diabetes, borrowing information from international aging cohorts (Gateway) and race/ethnicity groups in the RAND HRS, with gains evaluated by AUC and Brier score.
- **In plain words**: Prediction models built on one group of people often work less well on another group that differs in background or health setting. This paper tests whether a method called transfer learning, which borrows useful information from other related datasets, can make predictions for older adults with diabetes more accurate. The authors compared it with models built only on the target group and with models pooling all the data, across eight international cohorts and four race/ethnicity groups in a US study.
- **Why it matters**: Many prediction tools are developed on one population and may not transfer to others, which matters for fairness and for public health planning. The reported gains are small (about 0.1% to 3.1% in AUC), and the text itself describes them as modest, so the practical value is still an open question rather than a settled result.
- **Background needed**: - Diabetes: a long-term condition in which blood sugar regulation is impaired; common in older adults.
- Prediction model: a statistical formula that estimates the chance of an outcome from risk factors such as age or clinical measures.
- Transfer learning: reusing information from related datasets to improve a model built on a smaller target dataset.
- Transportability: whether a model that works in one population still works in another.
- AUC: a 0 to 1 score for how well a model separates people who will have an outcome from those who will not; higher is better.
- Brier score: a measure of how close predicted probabilities are to what actually happened; lower is better.
- Bootstrap resampling: repeatedly resampling the data to estimate how uncertain a result is.
- Patient-reported outcomes: health measures reported by participants themselves rather than by clinicians. · level: research-level

<details><summary>Original abstract</summary>

Population heterogeneity challenges the transportability of prediction models. Transfer learning may improve prediction through information borrowing, but its utility across population settings remains unclear. We evaluated a regression-based transfer learning framework across international aging cohorts (Gateway) and race/ethnicity groups within the RAND Health and Retirement Study (RAND HRS). Gateway included 19,879 adults with diabetes from eight cohorts, while RAND HRS included 3,926 participants across four race/ethnicity groups. Prediction models for patient-reported health outcomes were developed using demographic and clinical risk factors. Transfer learning was compared with target-only and pooled models using AUC and Brier score, with bootstrap resampling to assess uncertainty. Transfer learning improved prediction in 75% (6/8) of Gateway cohorts, with AUC gains of 0.1%-0.6%, and in all four RAND HRS race/ethnicity groups, with gains of 0.8%-3.1%. Improvements were greater and more consistent across within-cohort groups. These findings demonstrate the potential of regression-based transfer learning to improve prediction across heterogeneous populations. Information borrowing from sufficiently transferable external data may enhance prediction performance and provide meaningful public health benefits, even when improvements are modest, particularly in large population-based cohorts.

</details>

### [Disease-anchored organ aging clocks enable multi-organ risk profiling from routine labs](https://www.medrxiv.org/content/10.64898/2026.11.22.26368688v1)
*Shi, C.; Sun, Y.; Ruan, X. et al.* · `epidemiology` · medRxiv doi:10.64898/2026.11.22.26368688 v1 · relevance 0.05

- **In one sentence**: The paper trains organ-specific "aging clocks" on first onset of each organ's disease using routine blood lab tests from UK Biobank, freezes the coefficients, and tests whether they track own-organ disease risk in NHANES (US) and JMDC (Japan) cohorts.
- **In plain words**: Doctors can estimate how old a person's organs are behaving, not just their calendar age, by looking at blood markers. Existing methods of doing this need expensive protein measurements and are trained on age rather than disease. This paper builds organ "clocks" trained directly on when each organ's disease first appears, using ordinary lab tests, and then checks whether they flag the right organ's disease.
- **Why it matters**: The approach aims to make organ-level risk estimates possible from routine blood tests rather than specialised proteomics, which could matter for screening. The text reports that the frozen clocks kept organ correspondence in a second country's cohort, predicted own-organ disease in a third, and added information beyond current organ clocks to clinical risk scores; whether this improves care is not shown in the text.
- **Background needed**: - Biological age: an estimate of how well body systems are functioning, which can differ from chronological age.
- Organ clocks: models that estimate the biological age of a specific organ (e.g., heart, kidney) from blood measurements.
- Proteomics: measuring large numbers of proteins in blood; costly and not routine.
- Routine laboratory tests: common blood tests (e.g., cholesterol, glucose, liver enzymes) done in standard clinical care.
- Frozen coefficients: the model's fitted weights are fixed after training and then applied unchanged to new cohorts.
- Negative control: random protein panels of matching size are used to check that results are not just due to panel size.
- Cohorts: UK Biobank (training), NHANES (US) and JMDC (Japan) (external tests).
- Clinical risk scores: standard tools that combine factors such as age and sex to estimate disease risk. · level: research-level

<details><summary>Original abstract</summary>

Organ clocks estimate the biological age of organs from blood, but current clocks assign tissue-enriched proteins to organs and train on chronological age, which requires proteomics and does not yield organ-specific disease risk. In the UK Biobank, we trained organ clocks on first onset of disease of each organ using routine laboratory tests and froze the coefficients. Under an age label, organ-clock readouts arose equally in size-matched random protein panels; with a disease label, clocks selected their own organ's proteins and predicted their own organ's diseases. Defining extreme aging by multiples of disease risk concentrated flags on own-organ disease. Frozen clocks kept organ correspondence in the US NHANES cohort, predicted first onset of own-organ disease in the Japanese JMDC cohort and added more information to clinical risk scores than current organ clocks. Trained once where disease follow-up exists, organ clocks can be used wherever routine laboratory tests are measured.

</details>

## Infectious diseases

### [Efficacy, Immunogenicity, and Safety of an Inactivated Bivalent EV-A71-CVA16 Vaccine in Children: A Randomized Phase 3 Trial](https://www.medrxiv.org/content/10.64898/2026.11.23.26368796v1)
*Tong, Y.; Liang, H.; Tang, J. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.23.26368796 v1 · relevance 0.09

- **In one sentence**: A randomized, double-blind phase 3 trial in 8,000 children aged 6-71 months reports that a bivalent inactivated EV-A71/CVA16 vaccine met its prespecified efficacy endpoint against CVA16-associated hand, foot and mouth disease and its noninferiority endpoint for EV-A71 immunogenicity versus a licensed EV-A71 vaccine.
- **In plain words**: Hand, foot and mouth disease is a common illness in young children, caused mainly by two viruses, EV-A71 and CVA16. This trial gave a new vaccine that targets both viruses at once to thousands of children, and compared it with a vaccine already licensed against EV-A71 alone. The reported results suggest the two-dose vaccine protected against CVA16 illness and produced antibody responses against EV-A71 that were at least as good as the licensed vaccine.
- **Why it matters**: Currently licensed vaccines cover only EV-A71, so CVA16 has been a gap in protection; a single product covering both viruses could address that. The text reports only the trial's own results, and the efficacy estimate rests on a small number of cases (4 versus 44), so the findings should be seen as preliminary until independent confirmation and longer follow-up are available.
- **Background needed**: - Hand, foot and mouth disease (HFMD): a viral infection causing fever, blisters on hands, feet and mouth, mostly in young children.
- Enterovirus A71 (EV-A71) and coxsackievirus A16 (CVA16): two viruses that are major causes of HFMD.
- Inactivated vaccine: a vaccine made from virus particles killed so they cannot replicate, but still able to trigger immunity.
- Bivalent vaccine: a single vaccine containing two strains or types of target.
- Randomized, double-blind trial: participants are assigned to groups by chance and neither they nor the researchers know which vaccine is given.
- Vaccine efficacy: the percentage reduction in cases among vaccinated versus control participants.
- Seroconversion and geometric mean titer (GMT): measures of antibody response; seroconversion is the share of people who develop detectable antibodies, and GMT is the average antibody level on a log scale.
- Noninferiority: showing a new vaccine is not meaningfully worse than an existing one.
- RT-PCR: a lab test that detects viral genetic material. · level: intermediate

<details><summary>Original abstract</summary>

Background Enterovirus A71 (EVA71) and coxsackievirus A16 (CVA16) cause hand, foot, and mouth disease (HFMD). We evaluated the efficacy, immunogenicity, and safety of a bivalent EVA71-CVA16 vaccine. Methods In this multicenter, double-blind, phase 3 trial, 8,000 healthy children aged 6-71 months were randomly assigned (1:1) to two doses of the bivalent or a licensed EVA71 vaccine, 1 month apart. The primary efficacy endpoint was RT-PCR-confirmed CVA16-associated HFMD with onset at least 14 days after dose 2. EVA71 immunogenicity noninferiority was assessed among baseline-seronegative participants without previous EVA71 vaccination. Results Of 7,975 participants receiving at least one dose, 7,419 underwent the primary efficacy analysis. CVA16-associated HFMD occurred in 4 bivalent-group versus 44 EVA71-group participants (vaccine efficacy, 90.91%; 95% CI, 75.03-97.63). At 30 days after dose 2, the EVA71 geometric mean titer (GMT) ratio was 2.04 (95% CI, 1.71-2.44) among baseline-seronegative participants without previous EVA71 vaccination. In the humoral immunogenicity population at this time point, CVA16 seroconversion rates were 96.94% versus 8.68%, and GMTs were 918.96 versus 3.88 U/mL. Adverse reactions within 30 days after either dose occurred in 46.73% versus 36.07% of reactogenicity-subgroup participants. In the overall safety population, serious adverse events occurred in 6.22% versus 7.55% from dose 1 through 6 months after dose 2; one bivalent-group event was considered possibly vaccine-related. No deaths occurred. Conclusions The bivalent EVA71-CVA16 vaccine met the prespecified efficacy criterion against CVA16-associated HFMD and the EVA71 immunogenicity noninferiority criterion in children aged 6-71 months (ClinicalTrials.gov: NCT06734832).

</details>

### [Deep Learning-based Phylodynamic Inference of Oropouche Virus Transmission Dynamics in Brazil Between 2023 and 2025](https://www.medrxiv.org/content/10.64898/2026.11.24.26368826v1)
*Arantes, I.; Bello, G.; Naveca, F. et al.* · `infectious diseases` · medRxiv doi:10.64898/2026.11.24.26368826 v1 · relevance 0.09

- **In one sentence**: A deep-learning phylodynamic model (BDEIVH) that explicitly represents alternating human-vector transmission and incubation is applied to Oropouche virus genomic clusters in Brazil (2023–2025), estimating vector and human infection durations and reproduction numbers.
- **In plain words**: Oropouche virus, spread by biting midges and mosquitoes, caused a large outbreak across the Americas from 2023 to 2025. The authors built a computer model that tracks how the virus passes back and forth between people and insects, and used it to read the family trees of viral genomes collected in Brazil. They report that the model estimates the virus spread more accurately than standard models in simulated tests, and that each infected person typically passed it on to about 1.15 to 1.81 others across the three main Brazilian clusters.
- **Why it matters**: Understanding how fast a vector-borne virus spreads in both endemic and non-endemic areas can inform surveillance and control planning. The text does not describe any public-health intervention or validation against field case counts, so its practical impact is not established from this text alone.
- **Background needed**: - Phylodynamics: inferring how an epidemic spreads by analysing the family tree (phylogeny) of viral genome sequences.
- Birth-death model: a standard statistical model of how lineages branch and die out over time, used here as a baseline.
- Reproduction number (R): the average number of new infections caused by one infected individual; here R_HH is the human-to-human value over one full human-vector-human cycle.
- Vector: an organism, such as a midge or mosquito, that carries the pathogen between hosts.
- Incubation period (exposed stage): the time between being infected and becoming able to transmit.
- Reassortant lineage: a virus strain formed when segments of its genome mix with another strain.
- Endemic vs non-endemic: whether a disease is regularly present in a region versus newly appearing there.
- Deep learning: machine-learning methods using layered neural networks, here used to make the inference. · level: research-level

<details><summary>Original abstract</summary>

Oropouche virus caused an unprecedented epidemic across the Americas during 2023-2025, associated with the expansion of the reassortant M1L2S2 lineage. To investigate its dissemination, we develop the Birth-Death Exposed-Infectious Vector-Human (BDEIVH) model within a deep-learning framework that explicitly represents alternating human-vector transmission and incubation periods. The model defines two directional reproduction numbers, RVH and RHV, whose product, RHH, quantifies the expected number of secondary human infections generated by a single infectious human through one complete transmission cycle. In simulations, BDEIVH provides more accurate RHH estimates than conventional birth-death models, with predictive accuracy improving with phylogeny size and remaining robust under reduced phylogenetic resolution. Across three major Brazilian OROV genomic clusters, estimated durations of infection range from 15.4 to 18.5 days in vectors and from 9.42 to 12.3 days in humans, whereas whole-cluster RHH estimates range from 1.15 to 1.81. RHH estimates reached a peak of 4.4 in the endemic Amazon region and 3.0 in the non-endemic Atlantic Forest region. These findings show that explicitly modelling vector-mediated transmission improves phylodynamic inference and reveals substantial OROV transmission in both endemic and non-endemic regions.

</details>

## Public and global health

### [Procedure composition, age and race/color in gender-affirming surgical authorizations of the Brazilian public health system, 2014-2025](https://www.medrxiv.org/content/10.64898/2026.11.23.26368723v1)
*dos Santos, J.; Amorim Costa, C. M.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368723 v1 · relevance 0.09

- **In one sentence**: A nationwide descriptive study of 1,375 Brazilian Unified Health System (SUS) hospital admission authorizations for gender-affirming surgery from 2014 to 2025, classifying procedures by a versioned code list and reporting procedure mix, age, race/color, and hospital counts.
- **In plain words**: This paper looks at records of surgeries that Brazil's public health system paid for to help people align their bodies with their gender, from 2014 to 2025. The records are billing forms, so they show which procedures were paid for, not who the patients are or why they had them. The authors found that the share of feminizing surgeries fell over time, and that the two groups of surgeries were made up of very different procedures.
- **Why it matters**: Public health records like these are increasingly used to describe gender-affirming care, so the paper's point that billing codes cannot show identity, need, or access is a useful caution for monitoring. The authors say that questions of access and equity would need person-level or patient-reported data, which this design does not have.
- **Background needed**: - SUS (Sistema Único de Saúde): Brazil's publicly funded national health system.
- Hospital admission authorization (AIH): a billing record for a hospital stay or procedure, filed through the Hospital Information System (SIH).
- Procedure codes: standard billing codes for surgeries; the paper uses a version-tracked list to decide whether each code is feminizing or masculinizing.
- Descriptive study: it counts and summarizes what happened, without testing causes.
- Median: the middle value of a set of numbers.
- "Parda": a Brazilian census category for mixed-race people, used in self-reported race/color.
- Composition vs. rate: the shares reported describe the mix of records in each period, not the rate of surgery in the population. · level: intermediate

<details><summary>Original abstract</summary>

Hospital admission authorizations from publicly financed health systems are increasingly used to describe gender-affirming surgery, although they record billed procedures whose feminizing or masculinizing direction can be inferred from the code, without identifying people, self-reported gender identity or clinical need. This nationwide descriptive study examined the authorizations for gender-affirming surgery processed by the Brazilian Unified Health System from 2014 to 2025, which were selected from 3,888 public monthly state files of the Hospital Information System with a historically versioned classification of procedure codes. Of the 1,375 selected authorizations, 711 corresponded to directly feminizing procedures, 428 to directly masculinizing procedures and 236 to a complementary procedure that was analyzed separately. The feminizing share of the directly classified authorizations decreased from 81.7% (196/240) in 2014-2018 to 72.2% (213/295) in 2019-2023 and to 50.0% (302/604) in 2024-2025, proportions that describe composition within periods of unequal length and cannot be read as population rates. In 2024-2025, bilateral mastectomy accounted for 264 of the 302 masculinizing authorizations (87.4%), whereas bilateral breast reconstruction with silicone implants accounted for 118 of the 302 feminizing authorizations (39.1%). The median recorded age was 35 years in feminizing and 30 years in masculinizing authorizations over the whole period, and 34 and 29 years when the comparison was restricted to 2024-2025. The brown (parda) race/color category was recorded in 42.6% (303/711) of feminizing and 61.0% (261/428) of masculinizing authorizations, in a comparison pooled over the whole period and not adjusted for period or procedure. The number of hospitals habilitated for these surgeries remained at five from 2014 to 2022 and doubled in 2023. All aggregate results were reproduced by an independent pipeline that re-read every original public file. It was observed that the equal numbers of feminizing and masculinizing authorizations in the most recent period resulted from markedly different procedure portfolios, which suggests that the monitoring of publicly funded gender-affirming surgery may benefit from procedure-specific indicators and versioned code definitions, while questions of access and equity would require person-level and patient-reported data.

</details>

### [Developing a Stakeholder-Driven One Health Collaboration Framework for Bovine Tuberculosis Control at the Human-Animal Interface in Lundazi and Monze Districts, Zambia](https://www.medrxiv.org/content/10.64898/2026.11.23.26368721v1)
*Phiri, A.; Zulu, M.; Phiri, M. et al.* · `public and global health` · medRxiv doi:10.64898/2026.11.23.26368721 v1 · relevance 0.07

- **In one sentence**: A qualitative study in two Zambian districts (Lundazi and Monze) that used focus groups and key informant interviews to identify barriers to veterinary-medical collaboration on bovine tuberculosis and proposes a five-pillar One Health collaboration framework.
- **In plain words**: Bovine tuberculosis is a cattle disease that can spread to people through raw milk, undercooked meat, and handling infected carcasses. Researchers held group discussions with 104 people, including farmers, abattoir workers, vets, doctors and officials, in two rural Zambian districts in 2022. They found that human and animal health workers mostly work separately, with little formal coordination, and they proposed a framework for better teamwork.
- **Why it matters**: The paper addresses a neglected disease that spreads between animals and people, and it shows how gaps between national policy and district-level practice can leave frontline workers isolated. The authors suggest the framework could also apply to other zoonoses such as brucellosis, anthrax and rabies, but the text does not test this, so that claim remains untested.
- **Background needed**: - Zoonosis: a disease that passes between animals and people.
- Mycobacterium bovis: the bacterium that causes bovine tuberculosis in cattle; it is related to the human tuberculosis bacterium, which the paper notes district hospitals often cannot tell apart from it.
- One Health: an approach that brings human, animal and environmental health workers together to tackle shared diseases.
- Qualitative study: research based on group discussions and interviews rather than numerical measurement.
- Focus group discussion (FGD) and key informant interview (KII): structured conversations with groups or with selected experts.
- Thematic analysis: a method for finding recurring themes in transcribed conversations.
- Abattoir: a slaughterhouse; carcass condemnation means meat is rejected as unfit. · level: intermediate

<details><summary>Original abstract</summary>

Background: Bovine tuberculosis, caused by Mycobacterium bovis, is a neglected zoonosis at the human-animal interface in Zambia, particularly affecting cattle-dependent rural communities in Eastern and Southern Provinces, where cattle are central to livelihoods, nutrition, and cultural identity. While Zambia has a One Health Strategic Plan 2022-2026 and a One Health Secretariat under Zambia National Public Health Institute, operational collaboration between veterinary and medical sectors at district level remains fragmented, contributing to diagnostic gaps, under-reporting, and continued transmission through consumption of raw milk, undercooked meat, and occupational exposure during slaughter and handling of infected carcasses. The disconnect between national policy and district implementation has created a vacuum where frontline workers operate in isolation despite sharing the same disease burden. Methods: This qualitative exploratory study was conducted in Lundazi District (Eastern Province) and Monze District (Southern Province), Zambia, from February to June 2022. Ten Focus Group Discussions were conducted with 104 participants, including cattle farmers, cattle businessmen, abattoir workers, veterinary and para-veterinary professionals, and medical doctors, and ten Key Informant Interviews were conducted with District Veterinary Officers, District Medical Officers, Ministry of Health officials, and Ministry of Fisheries and Livestock officials. Participants were purposively selected based on their role, experience, and knowledge of bovine tuberculosis and One Health collaboration. Discussions were held in local languages (Tumbuka, Tonga, Chewa), audio-recorded with consent, transcribed verbatim, translated into English, and imported into NVivo 12 (QSR International, Melbourne, Australia) for thematic analysis following Braun and Clarke's six-step approach, with framework matrices for triangulation and trustworthiness. This methodological rigor ensured that diverse voices from community to policy level were systematically captured and compared. Results: Five themes emerged: (1) awareness of bovine tuberculosis, (2) socio-economic impacts, (3) public health impacts, (4) cultural practices and transmission, and (5) collaboration gaps and proposed framework. Medical and veterinary professionals demonstrated excellent awareness, while cattle farmers and abattoir workers showed poor awareness. Socio-economic impacts included reduced milk yield and carcass condemnation. Key barriers to collaboration included lack of diagnostic capacity at district hospitals to differentiate Mycobacterium bovis from Mycobacterium tuberculosis, siloed training curricula, absence of formal round-table coordination mechanisms, and limited funding. An existing enabler was informal collaboration in meat inspection between veterinary assistants and environmental health officers. Based on these findings, a five-pillar One Health Collaboration Framework is proposed. This framework was co-constructed from participant recommendations, making it contextually grounded and acceptable to end-users. Conclusion: Effective control of bovine tuberculosis in Zambia requires institutionalized One Health collaboration, moving from informal ad hoc interactions to formal governance structures. The proposed framework provides a practical, low-cost and contextually grounded roadmap for district-level implementation and is applicable to other zoonoses such as brucellosis, anthrax and rabies. Its implementation can help break the cycle of under-reporting and under-funding that currently sustains zoonotic transmission in rural Zambia

</details>

## Psychiatry and neurology

### [Plasma proteomic markers of cognitive and brain aging in a multi-ethnic cohort](https://www.medrxiv.org/content/10.64898/2026.11.22.26368682v1)
*Wood, B.; Wood Alexander, M.; Clappison, A. et al.* · `neurology` · medRxiv doi:10.64898/2026.11.22.26368682 v1 · relevance 0.09

- **In one sentence**: A plasma proteomics study measuring 220 blood proteins in 250 older adults of Chinese, South Asian, and non-Hispanic White background, with replication in 1,381 ADNI participants, linking protein levels to cognition, brain MRI markers, and cognitive decline.
- **In plain words**: Researchers measured about 220 proteins in blood samples from 250 older adults from three ethnic groups, and checked how those levels related to thinking skills and brain scans. Several proteins tied to brain disease, nerve connections, oxidative stress, and inflammation were linked to poorer cognition, and a tau-related protein was linked to a thinner area of the brain involved in memory. The main findings were then checked in a much larger US cohort of 1,381 people, where some of the same proteins were associated with cognitive decline and progression toward clinical disease.
- **Why it matters**: Blood tests that reflect brain aging could be easier and cheaper to use than brain scans or spinal fluid tests, and the study includes ethnic groups that are usually underrepresented in Alzheimer's research. Whether these proteins will prove useful as clinical markers is not established by this text; it reports associations, not diagnostic performance.
- **Background needed**: - Plasma proteomics: measuring many proteins at once in a blood sample; "ultrasensitive" means very low concentrations can be detected.
- Tau (pTau): a protein that forms tangles in Alzheimer's disease; phosphorylated forms are chemically modified versions used as disease markers.
- Entorhinal cortex: a brain region near the hippocampus important for memory, often one of the first affected in Alzheimer's.
- Cerebral small vessel disease: damage to the tiny blood vessels of the brain, often seen as white matter changes on MRI.
- Cohort study: following a defined group of people over time; ADNI is a large US Alzheimer's research cohort.
- Associations are correlational; they do not by themselves show that a protein causes brain changes. · level: research-level

<details><summary>Original abstract</summary>

Advances in ultrasensitive proteomics offer opportunities to characterize molecular pathways underlying brain aging. We measured 220 plasma proteins using NULISAseq Neuro220 in 250 Chinese, South Asian, and non-Hispanic White older adults (mean age=68.2 years, 70.4% female). Proteins implicated in neurodegenerative diseases (including brain-derived phosphorylated Tau, BDpTau), synaptic function, oxidative stress, and inflammation were associated with poorer cognition. Phosphorylated Tau205 was associated with reduced entorhinal thickness, whereas inflammatory proteins were associated with imaging markers of cerebral small vessel disease. Several findings were replicated in 1,381 participants in the Alzheimer's Disease Neuroimaging Initiative, including associations of BDpTau species, NPTX2, BACE1, TREM1, CCL17, PRDX6, and IGF1R with cognitive decline and clinical progression. Cardiometabolic risk factors were associated with widespread proteomic alterations, many of which were also linked to poorer brain health. These results identify promising molecular markers of brain aging and extend proteomic research to ethnically diverse populations historically underrepresented in Alzheimer's disease research.

</details>

### [Nigral volume as a marker for Lewy body copathology in Alzheimer's disease](https://www.medrxiv.org/content/10.64898/2026.11.23.26368759v1)
*langley, j.; Hwang, K. S.; Hu, X. P.* · `neurology` · medRxiv doi:10.64898/2026.11.23.26368759 v1 · relevance 0.09

- **In one sentence**: In 73 ADNI participants with clinical AD or MCI, lower antemortem neuromelanin-MRI substantia nigra volume was associated with autopsy-confirmed Lewy body copathology and with greater nigral hypopigmentation at autopsy, though the study is single-cohort and modest in size.
- **In plain words**: Many people diagnosed with Alzheimer's disease also have Lewy body deposits, clumps of a protein called alpha-synuclein in the brain, and these are linked to earlier symptoms and faster memory and thinking decline. This study asked whether a special brain scan measuring the size of a midbrain region called the substantia nigra, taken while people were alive, could help flag those cases. Among 73 people whose brains were examined after death, those with Lewy body deposits tended to have a smaller nigral region on the scan and paler (less pigmented) tissue at autopsy.
- **Why it matters**: A scan-based marker that hints at hidden Lewy body pathology in Alzheimer's patients could help clinicians and researchers sort patients during life, which matters for prognosis and trial selection. The result is preliminary: it comes from one small cohort, the scans were taken years before autopsy, and the predictive value shown (area under the curve about 0.77) is moderate and was not tested in separate data.
- **Background needed**: - Alzheimer's disease (AD): the most common cause of dementia, defined by amyloid and tau brain changes.
- Mild cognitive impairment (MCI): noticeable memory or thinking problems that do not yet meet the full dementia threshold.
- Lewy bodies: abnormal clumps of alpha-synuclein protein; they define Parkinson's disease and dementia with Lewy bodies, and often co-occur with AD.
- Substantia nigra: a midbrain area that makes dopamine; its pigmented cells are lost in Parkinson's disease.
- Neuromelanin-sensitive MRI: a scan that picks up the dark pigment in the substantia nigra, used as a proxy for its health.
- Autopsy confirmation: the diagnosis of Lewy body pathology was made on tissue after death, which is the reference standard here.
- ADNI: the Alzheimer's Disease Neuroimaging Initiative, a large shared research database. · level: research-level

<details><summary>Original abstract</summary>

Background: Lewy body (LB) copathology in Alzheimer's disease (AD) is associated with earlier symptom onset and faster cognitive decline. Depigmentation of substantia nigra pars compacta (SNc) volume is seen in both Parkinson's disease and dementia with Lewy bodies. We examined whether lower antemortem SNc volume was associated with autopsy confirmed LB pathology in patients with AD or mild cognitive impairment (MCI). Methods: Seventy-three participants with a clinical diagnosis of AD or MCI, neuromelanin-sensitive MRI, and subsequent neuropathologic assessment from the Alzheimer's Disease Neuroimaging Initiative were studied. At autopsy, 33 participants had LB pathology (LB+) and 40 had no LB pathology (LB-). We compared SNc volume between groups using analysis of covariance adjusted for age and sex. Within the LB+ group, we assessed the association between SNc volume and nigral hypopigmentation using Spearman correlation. In a secondary analysis, we tested whether adding SNc volume to a logistic regression mode containing age, sex, and executive function improved model fit for autopsy-defined LB status. Results: LB+ participants had greater nigral hypopigmentation at autopsy and lower antemortem SNc volume than LB- participants. The adjusted mean difference in SNc volume (LB+ minus LB-) was -66 mm3 (95% confidence interval -115.9 to -16.2, P=0.010). Within the LB+ group, lower SNc volume was associated with greater hypopigmentation (Spearman rho;=-0.373, P=0.032). Among 71 participants with complete model data, adding SNc volume improved model fit (likelihood ratio=8.67, P=0.003). The combined model had an in sample area under the receiver operating characteristic curve of 0.770 (95% confidence interval: 0.661-0.879). Conclusion: The correspondence between lower antemortem SNc volume and greater hypopigmentation at autopsy supports the use of neuromelanin-sensitive MRI to characterize nigral involvement in AD or MCI with LB copathology. These findings are based on a single cohort, and the interval of several years between imaging and autopsy limits how closely the pigmentation ratings reflect nigral integrity at imaging.

</details>

## Oncology

### [The cellular neighbourhoods of adult gliomas and their clinical associations](https://www.medrxiv.org/content/10.64898/2026.11.24.26368523v1)
*Mathioudaki, A.; Rutz, S.; Seferbekova, Z. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.24.26368523 v1 · relevance 0.06

- **In one sentence**: A single-cell spatial transcriptomic atlas of 275 adult glioma patients (2.6 million cells) reports recurrent cellular neighbourhoods across glioma types, with some neighbourhood abundances linked to survival in astrocytoma.
- **In plain words**: This study looks at the most common malignant brain tumours in adults, gliomas, and asks whether the different types of cells inside them are arranged in repeating local groups. The researchers mapped the position and activity of about 2.6 million cells from 275 patients, using a technique that measures which genes are switched on in each cell while keeping its location in the tissue. They found recurring cell "neighbourhoods" with particular immune and support-cell mixes, some shared across tumour types and some linked to clinical features.
- **Why it matters**: It suggests that the spatial layout of tumour cells, not only their molecular type, may carry information about prognosis, and the authors report that in astrocytoma neighbourhood abundance was associated with survival independently of WHO grade. Whether this could guide treatment or diagnosis is not shown in the text and would need further study.
- **Background needed**: - Gliomas are tumours arising from glial cells, the support cells of the brain; glioblastoma is the most aggressive common type.
- IDH mutations and 1p/19q codeletion are genetic markers used to classify these tumours.
- WHO grade is a standard pathology scale of how aggressive a tumour looks under the microscope.
- Single-cell spatial transcriptomics measures gene activity in individual cells while retaining their positions in a tissue slice.
- A "neighbourhood" here means a recurring group of nearby cells with a characteristic mix of cell types.
- AC-like (astrocyte-like) refers to a cell state resembling normal astrocytes, a type of glial cell.
- H&E is the routine stain used to view tissue sections under a microscope.
- Multiplexed protein imaging labels many proteins at once in the same tissue section. · level: research-level

<details><summary>Original abstract</summary>

Glial tumours are the most common primary malignant brain tumours in adults and comprise molecularly and histologically distinct entities with diverse outcomes. Despite this diversity, they arise within a shared anatomical environment, suggesting that common organisational principles may shape tumour heterogeneity. However, how cellular states are organised across gliomas and whether this organisation relates to clinical outcomes remains unclear. To that end, we generated a single-cell resolution spatial transcriptomic atlas of 2.6 million cells from 275 patients spanning IDH-wildtype glioblastoma, IDH-mutant and chromosome 1p/19q codeleted oligodendroglioma, IDH-mutant astrocytoma and ependymoma. Across diagnoses, we show how heterogeneous tumour cell states are spatially organised into recurrent neighbourhoods with distinct immune and glial composition, which in turn assemble into a higher-order architecture. Among these cellular neighbourhoods, some, such as the astrocyte-like (AC-like), are conserved across entities, whereas others segregate by clinicopathological parameters. AI-powered histopathology further reveals selective association of neighbourhoods within histological clusters, providing a link between molecular spatial organisation to routine H&E morphology. In astrocytoma, neighbourhood abundance is associated with patient survival independently of WHO grade, with AC-like enrichment linked to favourable outcomes. Same-cell high-plex spatial transcriptomics and multiplexed protein imaging in an independent astrocytoma cohort validated these neighbourhoods and further confirmed enrichment of oligodendrocytes within the TBI neighbourhood. Collectively, our findings reveal that glial tumours are spatially encoded through recurrent multicellular neighbourhoods across different molecular entities, showing clinical relevance beyond conventional histology and providing a foundation for analogous investigation across cancer types.

</details>

### [Integrated real-world and translational studies nominate CREB binding protein/EP3001 inhibition to overcome androgen receptor pathway modulator resistance in men with prostate cancer](https://www.medrxiv.org/content/10.64898/2026.11.24.26368506v1)
*Somarelli, J. A.; Dougherty, B. V.; Beckmann, A. G. et al.* · `oncology` · medRxiv doi:10.64898/2026.11.24.26368506 v1 · relevance 0.06

- **In one sentence**: Regulatory network models built from multi-omic data of over 10,000 prostate cancer patients point to EP300/CBP as a target in androgen pathway modulator-resistant disease, supported by preclinical work with the inhibitor pocenbrodib and one clinical case.
- **In plain words**: Prostate cancer drugs that block male hormone signalling often stop working over time, and doctors need new targets for these resistant tumours. The authors used computer models of gene regulation, built from large sets of patient molecular data, to find a protein called EP300 (and its close relative CBP) linked to resistance. They then tested a new inhibitor of these proteins, pocenbrodib, in lab and animal studies, and report benefit in one patient.
- **Why it matters**: Resistance to hormone-blocking drugs is nearly universal in advanced prostate cancer, so a new candidate target is of interest. The evidence is limited: the human benefit rests on a single patient, so the finding is a lead for further testing rather than an established treatment.
- **Background needed**: - Androgen pathway modulators (APMs): drugs that block male hormones such as testosterone from driving prostate cancer growth through the androgen receptor.
- Therapy resistance: when tumours keep growing despite treatment.
- Multi-omic data: measurements across several layers of biology (genes, proteins, and so on) from the same patients.
- Regulatory network model: a computer map of which genes and proteins control others.
- EP300 / CBP: related proteins that switch genes on by adding chemical tags (acetylation) to histones and other proteins.
- Acetylomics: measuring these acetyl tags across the proteome.
- Oxidative phosphorylation and fatty acid metabolism: cell processes that produce energy; the paper links the drug to suppressing them.
- In vitro / in vivo: lab-dish and living-animal experiments; a single-patient clinical report is far weaker evidence than a trial. · level: research-level

<details><summary>Original abstract</summary>

Androgen pathway modulators (APMs) have significantly improved outcomes for men with metastatic prostate cancer, but the evolution of therapy resistance is nearly universal, and there remains a major clinical need to identify actionable vulnerabilities for therapy-resistant disease. To address this need, we employed regulatory network models that leverage multi-omic data from over 10,000 prostate cancer patients with longitudinal clinical data. Analysis of the architecture of the network models identified EP300 as the top actionable target associated with androgen receptor-mediated therapy resistance. These observations were validated using a novel inhibitor of CBP/EP300, pocenbrodib, which showed preclinical activity in vitro and in vivo. Acetylomics analysis and functional studies pinpointed inhibition of oxidative phosphorylation and fatty acid metabolism as key mechanisms of action for pocenbrodib. Clinical benefit for this agent was demonstrated in a patient with metastatic APM-resistant prostate cancer (NCT04575766), highlighting CBP/EP300 as a key target for further translation.

</details>

## Health informatics and medical AI

### [Effect of a feedback loop on clinical prediction model performance](https://www.medrxiv.org/content/10.64898/2026.11.23.26368745v1)
*Pacynko, S.; Sperrin, M.; Jenkins, D.* · `health informatics` · medRxiv doi:10.64898/2026.11.23.26368745 v1 · relevance 0.17

- **In one sentence**: A simulation study of how updating a clinical prediction model with data generated by its own treatment recommendations (a feedback loop) degrades calibration and discrimination, and whether including treatment as a predictor or unmeasured confounding changes this.
- **In plain words**: Medical risk calculators can change the care patients receive, and that care then changes the outcomes the calculator learns from. This paper uses computer simulations, with settings based on cardiovascular disease, to see how much a model's accuracy drops when it is retrained on data from patients it helped treat. It also checks whether adding the treatment itself as an input to the model helps.
- **Why it matters**: Prediction tools that guide treatment may quietly lose accuracy after they are updated, which could affect patient outcomes without anyone noticing. The authors say the findings agree with earlier work and point to the need for monitoring methods after a model is deployed; the text does not report how widespread the problem is in real clinical use.
- **Background needed**: - Clinical prediction model: a formula that estimates a patient's chance of a future event (here, a bad cardiovascular outcome) from measured details such as age or blood pressure.
- Feedback loop: the model's own recommendations change who gets treated, so the data later used to update the model no longer reflect the original situation.
- Calibration: whether predicted risks match observed event rates (calibration-in-the-large is the overall level; calibration slope is whether the spread of risks is right).
- C-statistic: how well the model ranks patients who will have the event above those who will not.
- Unmeasured confounding: a hidden factor that affects both treatment and outcome, which the model cannot see.
- Simulation study: the researchers generate artificial patient data with known rules, so they can test the model under controlled conditions.
- Causal inference: statistical methods for estimating the effect of a treatment rather than just associations. · level: intermediate

<details><summary>Original abstract</summary>

Clinical prediction models (CPMs) that guide treatment-initiation, and therefore affect patient outcomes, may create feedback loops when updated using data from patients whose care they influenced. Treatment can alter predictor-outcome relationships and outcome prevalence, potentially reducing model performance. This simulation study aims to quantify this effect using setting parameters based on cardiovascular disease prediction and intervention and assess if including a treatment variable in the model mitigates any performance degradation. In the simulation, models were developed to predict the probability of a binary adverse outcome, guide treatment allocation, and then updated using data containing patients in whom the model was applied. Scenarios varied treatment inclusion as a predictor in the model and the presence of unmeasured confounding. Performance was assessed with calibration-in-the-large, calibration slope, c-statistic, and correct risk assignment relative to treatment threshold. Without unmeasured confounding, excluding treatment as a predictor resulted in miscalibration, but including treatment solves this problem completely. With unmeasured confounding, performance deteriorated even when treatment was included. These results agree with previous findings and illustrate the likelihood that models that guide interventions may experience performance deterioration due to the difficulty of recording treatment and avoiding unmeasured confounders. Causal inference methods combined with risk prediction may help address this problem. Further research is needed on monitoring techniques to allow detection of this issue post-model implementation.

</details>

### [STREAM: Sequential Transformer for Risk Estimation from Asynchronous Medical Events for Dynamic Postoperative AKI Prediction](https://www.medrxiv.org/content/10.64898/2026.11.21.26368665v1)
*Lu, S.; Ruan, X.; Wang, L. et al.* · `health informatics` · medRxiv doi:10.64898/2026.11.21.26368665 v1 · relevance 0.11

- **In one sentence**: STREAM is a Transformer model that treats irregular electronic health record data as a time-ordered stream of clinical events to predict postoperative acute kidney injury (PO-AKI) at surgery completion and after each new event, reporting AUROC/AUPRC and calibration against Time-series Transformer and GRU-D baselines in a 167,078-episode retrospective noncardiac surgery cohort.
- **In plain words**: Doctors need to know how likely a patient is to develop kidney injury after surgery, and that estimate should change as new test results and notes arrive. This paper describes a model, STREAM, that reads a patient's records as a chronological list of events rather than fixed time blocks, and updates its risk estimate as each new event comes in. In a retrospective set of about 167,000 non-heart surgeries, it scored somewhat higher than two comparison models, and the authors say its risk estimates were more consistent across the postoperative period.
- **Why it matters**: Risk estimates that update as information accumulates could matter for timing clinical checks after surgery, and the text suggests the event-level explanations may help clinicians see what drove a change. The gains over the comparators are modest in the reported numbers, and the study is retrospective, so its clinical value is not yet shown; the link to "perioperative digital twins" is described by the authors as a potential component, not a demonstrated one.
- **Background needed**: - Acute kidney injury (AKI): a sudden drop in kidney function, here studied after surgery.
- Electronic health record (EHR): the digital hospital chart, including labs, medications, and notes, often recorded at irregular times.
- Transformer: a neural network architecture that weighs relationships among items in a sequence; widely used in language models.
- GRU-D: a recurrent neural network designed for data with gaps and irregular timing.
- AUROC / AUPRC: measures of how well a model ranks patients who will and will not develop the outcome; AUPRC is more informative when the outcome is rare.
- Calibration: whether predicted probabilities match observed frequencies.
- Retrospective cohort: a study using past records rather than a prospective trial.
- Digital twin: a computer model of a patient updated with their data over time. · level: research-level

<details><summary>Original abstract</summary>

Postoperative acute kidney injury (PO-AKI) risk estimates evolve as clinical information accumulates, yet many electronic health record (EHR) models use static or fixed-window representations. We developed STREAM, a perioperative event-stream Transformer that represents irregular EHR data as chronological clinical events and supports surgery-index prediction at surgery completion and event-by-event postoperative AKI prediction. In a retrospective cohort of 167,078 noncardiac surgical episodes, STREAM achieved surgery-index AUROC/AUPRC of 0.942/0.771, the Time-series Transformer 0.933/0.729, and GRU-D 0.926/0.695. Postoperative macro-AUPRC across 6-hour evaluation intervals was 0.589, 0.525, and 0.547, respectively. STREAM showed more consistent calibration across postoperative time points than the comparators. Event-arrival attribution and within-window permutation analysis enabled event-level interpretation of how newly arrived information and fine-grained event ordering shaped evolving risk estimates. These findings support event-stream modeling as an interpretable framework for dynamic, temporally resolved prediction from longitudinal EHR data as well as a potential risk-estimation component for future perioperative digital twins.

</details>

## Econometrics and applied economics

### [Training decision models for simulating human respondents](https://arxiv.org/abs/2611.31613)
*Davood Wadi, Yu Ma* · `cs.CL` · arXiv:2611.31613v1 · relevance 0.05

- **In one sentence**: The paper tests whether fine-tuning language-model "decision models" on historical respondent-level choice data, before any target-study data is seen, reduces the bias that off-the-shelf LLMs introduce when used as synthetic survey respondents for econometric inference.
- **In plain words**: Researchers are increasingly using AI language models in place of real people in surveys and experiments, but these stand-ins choose differently from humans and distort the conclusions drawn from them. This paper trains such models on past records of how real people made choices, so they start out closer to human behavior. Across four new held-out studies on topics like vaccines and nutrition labels, the trained models cut the error in estimated treatment effects by 22% to 89%.
- **Why it matters**: Synthetic respondents are cheap and fast, so whether they can be made to give unbiased estimates matters for market research and experimental economics. The paper also reports a caveat: training on a single study can lower prediction loss while worsening treatment-effect error, so the approach is not a simple fix, and the text does not show how well it generalizes beyond the studies tested.
- **Background needed**: - Synthetic respondents: AI models asked to answer survey or experiment questions as if they were people ("silicon sampling").
- Discrete choice experiment: a study where participants pick one option from a set, used to measure preferences; conjoint analysis is a common version.
- Treatment effect: the difference in outcomes caused by an intervention, such as a changed label or message.
- Conditional maximum likelihood: a standard statistical method for fitting model weights so that observed choices become as probable as possible.
- Cross-entropy: a measure of how well a model predicts observed outcomes; lower is better, but not the same as unbiased estimates.
- Post-inference calibration: correcting estimates after the model has produced them.
- Held-out studies: studies withheld from training and used only for testing. · level: research-level

<details><summary>Original abstract</summary>

Researchers increasingly use large language models (LLMs) as synthetic respondents in market research, conjoint analysis, and randomized experiments. However, synthetic choice data from off-the-shelf generative LLMs bias downstream econometric inference. Neither proprietary models nor higher reasoning effort reliably reduces this bias. We investigate decision models (System One architectures) for silicon sampling. Using choice training, we update KEV model weights on historical respondent-level choice microdata by conditional maximum likelihood, before inference and without target-study data. Across three model scales, training on two discrete choice experiments lowers treatment-effect error by 22% to 89% on four held-out studies from new domains (vaccines, nutrition labels, consumer rights, and AI) and new response formats. A small choice-trained model outperforms a much larger off-the-shelf model on three of the four studies. Although training on single studies lowers cross-entropy, it can exacerbate treatment-effect error. Choice training thus complements post-inference calibration by providing a stronger starting point for estimating human preferences.

</details>

### [Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement](https://arxiv.org/abs/2611.33050)
*Zihan Chen, Di Zhu, Lei Nico Zheng* · `cs.CL` · arXiv:2611.33050v1 · relevance 0.03

- **In one sentence**: Using a French government chatbot arena, WildChat logs, and congestion-driven latency variation, the paper finds that streaming a fresh answer as it is written wins more blind votes than replaying the same stored text at once, while waiting reduces users' follow-up questions.
- **In plain words**: AI chatbots now reply at very different speeds, from a long pause while the model "thinks" to an instant reply from a stored copy. This paper asks whether the speed or the way an answer appears changes how people judge it, which matters because public rankings of chatbots come from people voting blind on answers. The authors found that the same stored text won more votes when it was typed out live (57% of decisive votes) than when it was shown instantly (29%), and that slow replies made users less likely to ask a follow-up question.
- **Why it matters**: It suggests that preference leaderboards may partly reward how an answer is delivered rather than what it says, and that latency has a real cost in user engagement. The text reports observational and arena data only, so the scope of these effects across other services and tasks is unclear.
- **Background needed**: - Large language models (LLMs): AI systems that generate text in response to prompts.
- Reasoning models: models that take extra time to work through a problem before answering.
- Response cache: a stored earlier answer that can be sent back instantly instead of generating a new one.
- Blind preference vote: a user compares two anonymous answers and picks the better one; these votes are used to rank models.
- Decisive vote: a vote where one answer is clearly preferred (not a tie or both-bad judgment).
- Labor illusion: the idea that people value outputs more when they can see effort going into them.
- Streaming: showing text word by word as it is generated, rather than all at once.
- Randomized comparison: assigning conditions by chance so differences can be attributed to the condition. · level: intermediate

<details><summary>Original abstract</summary>

Answers from generative AI chatbots built on large language models (LLMs) now arrive at very different speeds: reasoning models deliberate before replying, while response caches can return a stored answer at once. Blind preference votes, which rank these models, are read as judgments of their text, and if delivery matters, faster answers are expected to gain. Research on the labor illusion and on how text appears on screen suggests instead that an answer which unfolds as it is written is credited over the same answer shown at once. We test these accounts with three sources of variation in natural use. First, compar:IA, a French government chatbot arena, answered repeated prompts, by a random draw, either with a fresh answer streamed as it was written or with a stored earlier answer from the same model, shown at once. Within the same prompt, a replay lowered an answer's chance of winning a decisive blind vote by 25.8 percentage points. The same stored text won 57% of its decisive votes when streamed and 29% when replayed, and voters called it less complete, more superficial and more often incorrect when replayed. Second, provider congestion slowed streamed answers. In 324,029 conversations, slower answers earned no detectable net credit in the vote, but a slower first exchange made visitors less likely to ask a follow-up question. Third, in 4,378,514 WildChat replies from everyday ChatGPT use, replies slowed by congestion made users less likely to continue. Delivery moved blind votes, in the direction opposite to the one the arena's designers expected, while waiting cost follow-up questions that a comparison between two answers cannot register when both are slow. The results bear on how AI services cache and stream answers, how they budget latency, and how preference leaderboards evaluate models.

</details>

## Economic theory

### [Contests versus Contracts in Innovation Procurement](https://arxiv.org/abs/2611.31829)
*Xiaoyun Qiu, Christopher Snyder* · `econ.TH` · arXiv:2611.31829v1 · relevance 0.08

- **In one sentence**: A mechanism-design study of how a funder should structure competition among firms pursuing uncertain technological approaches, comparing independent contracts, contests, and interdependent contracts under different contractability, heterogeneity, and payment-flexibility assumptions.
- **In plain words**: The paper asks how much competition a government or other buyer should create when it pays several teams to develop innovations whose feasibility is only learned by trying. It compares three kinds of arrangement: separate contracts for each team, prize contests, and a middle option where each team's reward also depends on how rivals are doing and whether experimentation continues. The authors report that the best arrangement depends on whether failures can be written into contracts, whether the approaches differ in difficulty, and whether payments can change over time.
- **Why it matters**: Innovation procurement is a real policy question for public agencies funding research, and the paper gives formal results on when a contest is cheaper than contracts. It is a theory paper, so its claims hold under its modeling assumptions and have not been tested against real procurement data in the text provided.
- **Background needed**: - Mechanism design: designing payment rules so that self-interested firms reveal information or act as the buyer wants.
- Contest: a setup where a prize goes to the best performer (for example, the first to succeed or the top-ranked finisher).
- Contract: a payment agreement tied to specified outcomes, here breakthroughs (successes) and possibly breakdowns (confirmed failures).
- Contractable: outcomes that can be verified and enforced in a contract.
- Experimentation under uncertainty: firms learn whether an approach is feasible only by trying it, so stopping and continuing decisions matter.
- Success cutoff and deadline: rules for stopping the whole process after a set number of successes or at a fixed time.
- Rents: extra profit a firm earns above its costs, which a buyer tries to limit. · level: research-level

<details><summary>Original abstract</summary>

How much competition should a designer introduce when procuring innovation? We study a designer funding multiple technological approaches whose feasibility is learned through experimentation. Between independent contracts and contests, we introduce interdependent contracts, which combine approach-specific rewards with continuation decisions that depend on rivals' outcomes. When both breakthroughs and breakdowns are contractable, these contracts implement the optimum by extracting firms' rents and coordinating experimentation across approaches. When only breakthroughs are contractable, we compare simple mechanisms with constant contractual payments. Under technological symmetry, optimal interdependent contracts terminate experimentation at a success cutoff or deadline. Fixed-prize contests can implement the same innovation outcomes, but their relative expenditure depends on the experimentation horizon: for interior success cutoffs, contests are more expensive when the horizon is short and less expensive when it is sufficiently long. Rank-contingent contests can weakly outperform constant-payment interdependent contracts, but technological heterogeneity can reverse this ranking because individualized contracts better tailor incentives to different approaches. We further characterize optimal interdependent contracts with time-varying payments, extending the comparison beyond simple mechanisms. Our results show how outcome contractability, technological heterogeneity, and payment flexibility shape the desirable form of competition in innovation procurement.

</details>

### [What it is to Obey](https://arxiv.org/abs/2611.32741)
*Mark Whitmeyer* · `econ.TH` · arXiv:2611.32741v1 · relevance 0.06

- **In one sentence**: In simultaneous-move games, a designer who commits to a signaling device and evaluates the resulting equilibria with a Hausdorff-continuous function; the paper shows that restricting to direct obedient devices is without loss of optimality under incomplete information exactly when the designer assumes her preferred equilibrium is played, and characterizes monotone evaluations under complete information.
- **In plain words**: This paper studies a setting where a planner sends private hints to players who are about to act at the same time, such as a recommendation to each firm or driver about what to do. The question is when the planner can limit herself to a simple kind of hint, one that players want to follow, without losing anything in the best outcome she can reach. The text says this holds under incomplete information exactly when the planner assumes her preferred equilibrium (a stable pattern of play that no one wants to leave) will actually be played.
- **Why it matters**: Signaling devices that recommend actions are a central idea in the study of how outside coordination can shape strategic behavior, so the result clarifies when simple recommendations are enough. The text is brief and I cannot judge how the results relate to the wider literature beyond what is stated.
- **Background needed**: - Simultaneous-move game: players choose actions at the same time without seeing each other's choice.
- Equilibrium: a set of actions where no player gains by switching alone.
- Signaling device: a mechanism that sends each player a private message, often a suggested action.
- Obedient device: one where following the recommendation is each player's best response, so players want to obey.
- Incomplete vs. complete information: whether players lack or share knowledge of each other's payoffs.
- Hausdorff continuity: a way of saying that small changes in the set of equilibria cause only small changes in the designer's evaluation.
- Monotone evaluation: an evaluation that rises when the set of equilibria gets better in a consistent ordering sense; the maximally optimistic and pessimistic evaluations are special cases. · level: research-level

<details><summary>Original abstract</summary>

Prior to agents taking part in a simultaneous-move game, a designer commits a device that sends signals to each of the agents, evaluating the resulting set of equilibria according to a (Hausdorff-)continuous function. In games of incomplete information I show that it must be without loss of optimality for the designer to restrict attention to direct obedient devices if and only if she assumes her preferred equilibrium will be played. In games of complete information, I characterize the monotone evaluations, which include both the maximally optimistic one and the maximally pessimistic one.

</details>

## Game theory and algorithmic economics

### [Optimal Signaling Mechanisms for One-round Matching Markets](https://arxiv.org/abs/2611.31517)
*Varsha Dani, David G. Harris, Thomas P. Hayes et al.* · `cs.GT` · arXiv:2611.31517v1 · relevance 0.19

- **In one sentence**: The paper derives optimal deterministic and randomized signaling mechanisms for a one-round matching market with n applicants and n firms, where each applicant signals k firms, and characterizes their limiting efficiency as k grows.
- **In plain words**: The paper studies how job seekers can use signals, like a limited number of special "I'm interested" tokens, to show employers which firms they really want, so that matches are more likely to happen. The authors work out the best possible signaling rules for a simple market with equal numbers of applicants and firms. They report that, as the number of signals per applicant grows large, the best deterministic rule gets about 75.45% of applicants a job offer, and the best randomized rule gets about 78.20%.
- **Why it matters**: Signaling is used in real job and dating markets, and this work gives exact limits on how well such schemes can do in a stylized model, including a comparison between fixed and randomized rules. It is a theory result, so its relevance to real markets depends on how closely the simple model matches them.
- **Background needed**: - Matching markets: two sides (applicants and firms) are paired, such as jobs and workers or dating partners.
- Signaling: a costly or limited way for one side to show real interest, so the other side can prioritize it.
- Deterministic vs. randomized mechanisms: a fixed rule for assigning signals versus one that uses chance.
- Limit as k goes to infinity: the result when each applicant may signal very many firms, used to state the best achievable rate.
- Incentive compatibility: whether firms gain by following the prescribed mechanism rather than deviating.
- The paper's key figures are stated as approximate percentages in the abstract; the full proofs are not in the given text. · level: research-level

<details><summary>Original abstract</summary>

Signaling mechanisms are used in various types of matching markets so that applicants may credibly signal interest in firms. They have been observed to improve outcomes in job markets and dating markets, and proven to improve outcomes in several stylized theoretical models. In this paper we develop optimal signaling mechanisms for a simple one-round matching market consisting of $n$ applicants and $n$ firms. We consider a much richer space of signals than have been used previously, in theory or practice, and also consider randomized signaling mechanisms, which have not been systematically studied. For each $k \geq 1$, we determine the optimal deterministic and randomized signaling mechanisms in which applicants signal $k$ firms. In the limit as $k\to \infty$, our deterministic mechanism guarantees that in expectation, $\approx 75.4504\%$ of the applicants receive job offers, and this is optimal. Likewise, for $k \to \infty$, our randomized mechanism guarantees that $\approx 78.197\%$ of the applicants receive offers, which is also optimal. The optimal $k$-signal randomized mechanism is non-constructive, and has a rather complex description. We describe some simple randomized signaling mechanisms whose efficiency surpasses that of the limiting optimal deterministic mechanism. Finally, we also discuss incentive-compatibility for the firms to follow the mechanism.

</details>

### [Heterogeneous Risk-Sensitive Evolutionary Learning in Coordination Games: Polarization, Welfare Loss, and Intervention for Efficiency](https://arxiv.org/abs/2611.31568)
*Solaleh Mohammadi, Yiman Fong, Kaiqing Zhang* · `eess.SY` · arXiv:2611.31568v1 · relevance 0.09

- **In one sentence**: In a finite population playing coordination games under risk-sensitive best response with mutations, the paper characterizes when a polarized state with heterogeneous risk attitudes (entropic risk measure) is uniquely stochastically stable, shows its welfare can fall below the risk-dominant equilibrium, and analyzes intervention shares and intensities that restore the payoff-dominant equilibrium.
- **In plain words**: The paper studies how a group of people who repeatedly learn from experience can end up split, with one subgroup choosing one option and the other subgroup choosing a different one, even when both would do better by coordinating on a single option. Each person's attitude toward risk is built into how they judge outcomes, and the two subgroups differ in that attitude. The authors identify when this split state is the one the learning process settles into in the long run, show it can leave everyone worse off, and test policies that nudge some agents' risk attitudes to steer the group back to the best coordinated outcome.
- **Why it matters**: The result suggests that differences in risk attitude alone, with no difference in payoffs, can lock a population into an inefficient outcome, which is relevant to questions of polarization and coordination failure. The text is limited to the abstract and does not show empirical tests or applications, so its relevance to real-world settings is an open question.
- **Background needed**: - Coordination game: each player gains most when they pick the same action as others, but there are several such matching outcomes with different payoffs.
- Payoff-dominant vs. risk-dominant equilibrium: the first gives the highest payoff to everyone; the second is the safer choice when people are unsure what others will do.
- Evolutionary learning with mutations: players repeatedly switch to best responses, with occasional random experimentation; the stochastically stable state is the one the process spends most time in over the long run.
- Entropic risk measure: a way of valuing uncertain payoffs that penalizes or favors risk depending on a risk parameter; higher parameter means more risk-sensitive.
- Pareto dominance: one outcome is Pareto dominated by another if every agent is at least as well off and some are strictly better off in the other.
- Intervention share and intensity: the fraction of agents whose risk parameter is changed, and by how much. · level: research-level

<details><summary>Original abstract</summary>

We study evolutionary learning in coordination games in a finite population of agents with heterogeneous risk attitudes, modeled using the entropic risk measure (ERM). The population consists of two subpopulations, each with a fixed risk attitude. Under risk-sensitive best response with mutations (BRM), we characterize the long-run outcomes of the learning process. In particular, we characterize when a polarized state, in which the two subpopulations choose different actions, is uniquely stochastically stable in terms of agents' risk attitudes and the subpopulation sizes. Notably, this polarized state is strictly Pareto dominated by the payoff-dominant equilibrium under both expected payoffs and agents' own ERM-adjusted payoffs. Moreover, its welfare, measured by average expected payoff, is always lower than that of the payoff-dominant equilibrium and can also be lower than that of the risk-dominant equilibrium. Thus, heterogeneity of risk attitudes in learning alone can lead to an inefficient long-run outcome. To mitigate such inefficiency, we propose intervention mechanisms to modify agents' risk attitudes in learning. We show that a sufficiently large intervention share (the fraction of agents modified) and sufficiently high intervention intensity (the increase in their risk parameter) ensure that the payoff-dominant equilibrium is uniquely stochastically stable. However, greater intervention intensity cannot compensate for an insufficient intervention share, and a larger intervention share cannot compensate for insufficient intervention intensity.

</details>

## Mathematical finance

### [Rough log-normal stochastic volatility with quadratic drift: second-moment stability and the martingale property under positive correlation](https://arxiv.org/abs/2611.32791)
*Artur Sepp, Parviz Rakhmonov* · `q-fin.MF` · arXiv:2611.32791v1 · relevance 0.14

- **In one sentence**: The paper extends a log-normal stochastic volatility model with quadratic drift to a rough (fractional Volterra) setting, derives second-moment stability thresholds and a martingale condition under the share measure, and reports calibration to Bitcoin and Ether option smiles under positive correlation.
- **In plain words**: The paper studies a mathematical model of how the price swings of an asset (here, the size of its fluctuations over time) evolve randomly. The authors show the model has a well-behaved, non-negative solution over any finite period, and they work out when its average squared size stays bounded and when a price built on it is a fair "martingale" (no expected drift). They also test the model against option prices for Bitcoin and Ether and link it to a simple model of trades pushing prices.
- **Why it matters**: Volatility models of this kind are used to price options and volatility indices such as the VIX, so exact conditions for stability and fairness matter for pricing and simulation. The text does not show how the results compare with existing rough-volatility models in practice, and the claim that the martingale condition is necessary is proved only for one class of kernels, with the singular-kernel case left open.
- **Background needed**: - Stochastic volatility: a model in which the size of price fluctuations is itself random and evolves over time.
- Log-normal model: volatility is modelled as the exponential of a random process, so it stays positive.
- Rough volatility and fractional kernels: a memory term with a fractional (Volterra) kernel, which makes volatility paths rougher than standard diffusions; the Hurst exponent sets the roughness.
- Moments: the expected value of a power of a random quantity, e.g. the second moment is the expected squared value; boundedness of moments indicates stability.
- Martingale: a process whose expected future value equals its current value, i.e. no predictable drift; a "fair" game.
- Share measure: a change of probability viewpoint (numéraire) used in pricing, under which the asset price is a martingale.
- VIX: a market index of expected short-term volatility derived from option prices.
- Implied volatility smile: the pattern of option implied volatilities across strikes. · level: research-level

<details><summary>Original abstract</summary>

We extend the log-normal stochastic volatility model with quadratic drift to a fractional Volterra equation. The volatility has a unique global non-negative solution with finite moments on every finite horizon. With linear drift we derive the conditional first and second moments, expected integrated variance and conditional squared VIX. We give the exact threshold for a uniformly bounded second moment and the exponential growth rate above it. With positive quadratic damping the second moment is uniformly bounded for every admissible Hurst exponent and volatility of volatility. A separate bound on long-run expected integrated variance per unit time depends only on the drift parameters. Under the share measure the volatility beta offsets the quadratic damping. The price is a true martingale when damping covers beta. For a positive finite exponential mixture this condition is also necessary. The converse for a singular fractional kernel remains open. We illustrate calibration under positive correlation on observed Bitcoin and Ether option smiles and benchmark the simulation against exact moments. A marked order-flow construction relates multiplicative volatility noise to signed trade impacts arriving at a rate proportional to variance. A small state-dependent bias generates the quadratic drift. We establish a stopped diffusion limit for the constant kernel.

</details>

### [Delta-Vega Hedging with Deep Reinforcement Learning: From Simulation to Reality](https://arxiv.org/abs/2611.32790)
*Michele Colombi, Marco Di Francesco, Pietro Rossi* · `q-fin.CP` · arXiv:2611.32790v1 · relevance 0.10

- **In one sentence**: The paper trains a PPO deep reinforcement learning agent to delta-vega hedge option portfolios under discrete trading and transaction costs, using the underlying asset and a longer-dated option, with simulation tests and an out-of-sample check on S&P 500 index option data.
- **In plain words**: Traders who sell options need to offset the risk that prices move, and also the risk that market volatility (how much prices swing) changes. This paper asks whether a learning-based trading agent can do that using the underlying asset plus a second, longer-dated option, while keeping trading costs in mind. The authors train the agent on simulated data, restrict it to inputs a trader could see in the market, and then test it on historical S&P 500 option data.
- **Why it matters**: Hedging volatility risk is costly and is a practical concern for option desks, so an approach that holds up on real market data under transaction costs is relevant to derivatives practice. The paper reports that its advantage appears mainly in high-volatility periods and at higher costs; how far these results generalise beyond the tested data is not established by the text.
- **Background needed**: - Option: a contract giving the right to buy or sell an asset at a set price later; its value depends on the asset price and its volatility.
- Hedging: taking offsetting positions so that a portfolio's losses from market moves are reduced.
- Delta hedge: offsetting price risk by holding the underlying asset in proportion to the option's price sensitivity (delta).
- Vega: an option's sensitivity to volatility; a delta-vega hedge also trades a second option to offset volatility risk.
- Stochastic volatility model: a price model in which volatility itself changes randomly over time.
- Transaction costs and discrete-time trading: trades cost money and happen at fixed intervals rather than continuously.
- Reinforcement learning: an agent learns a trading rule by trial and error against a reward signal; PPO is a common training algorithm.
- Profit-and-loss (P&L) dispersion: the spread of outcomes, used here as a measure of hedging risk. · level: research-level

<details><summary>Original abstract</summary>

Hedging an option portfolio with the underlying asset alone leaves the position exposed to changes in volatility, which can be managed by trading another derivative, at higher transaction costs. We propose a deep reinforcement learning approach to hedge both price and volatility risk under discrete-time trading and transaction costs, by trading the underlying asset and a second, longer-dated option. We train the agent with Proximal Policy Optimization (PPO) on synthetic data from a stochastic volatility model, and restrict its state to quantities observable in the market, so that the policy learned in simulation applies directly to market data. In simulation, we validate the policy against semi-analytical Delta and Delta-Vega hedging benchmarks. PPO matches Delta-Vega's objective at baseline transaction costs and increasingly outperforms it as costs rise, with both two-instrument strategies consistently outperforming the single-instrument Delta hedge. On historical S&P 500 index option data, we benchmark our approach against practitioner Black-Scholes Delta and Delta-Vega hedging strategies. The two-instrument strategies roughly halve the profit-and-loss dispersion of the Delta hedge, and PPO attains a lower profit-and-loss volatility than Delta-Vega at comparable transaction costs. PPO holds more of the hedging option than Delta-Vega, in line with the stochastic-volatility model hedge, and its advantage is concentrated in high-volatility episodes.

</details>

## Financial markets

### [Semivariance and Semivolatility in Portfolio Selection: A Unified Framework for Downside-Risk Portfolio Models](https://arxiv.org/abs/2611.32638)
*Francesco Cesarone, Massimiliano Corradini, Nicol\`o Giunta* · `q-fin.PM` · arXiv:2611.32638v1 · relevance 0.07

- **In one sentence**: The paper classifies downside-risk portfolio models (semivariance and semivolatility) by the positive homogeneity degree of the risk measure, states a non-degeneracy condition under which risk-parity, most-diversified and Sortino-ratio problems are well posed, and runs a rolling-window out-of-sample comparison of seventeen long-only strategies on Dow Jones and Nasdaq-100 total returns.
- **In plain words**: This paper is about how investors measure risk when they care mainly about losses rather than all ups and downs. It looks at a risk measure called semivariance, which counts only returns that fall below a chosen threshold, and its square root, semivolatility. The authors argue these measures should be chosen according to the type of portfolio problem being solved, and they test many investment strategies on past stock index data.
- **Why it matters**: Many downside-risk models are presented as simple extensions of standard variance-based models, and this paper argues that the extension needs care for certain portfolio goals. The empirical comparison on two index datasets gives a practical check, though its results are limited to the periods and indexes studied and say little beyond them.
- **Background needed**: - Portfolio: a mix of investments with weights that add up to one.
- Variance and volatility: standard ways to measure how much returns spread out; volatility is the square root of variance.
- Downside risk: risk measured only through losses or returns below a threshold (here the mean, zero, or a market index return).
- Semivariance / semivolatility: downside versions of variance and volatility.
- Positive homogeneity of degree one: if all weights are doubled, risk doubles; this is what makes risk contributions add up to total risk.
- Risk parity and risk budgeting: spreading risk evenly, or in prescribed shares, across holdings.
- Most-diversified portfolio: maximizes diversification as a ratio of weighted volatilities to portfolio volatility.
- Sortino ratio: a reward-to-risk measure using downside risk instead of total volatility.
- Convex program: an optimization problem that can be solved reliably.
- Rolling-window backtest and block bootstrap: testing a strategy on repeated past windows of data and using resampling to judge whether differences are statistically meaningful. · level: research-level

<details><summary>Original abstract</summary>

In this paper, we study downside risk in portfolio selection beyond minimum-risk models, where semivariance and its square root, semivolatility, yield the same portfolio. Downside-risk models are often presented as direct extensions of their variance-based counterparts, although different classes of portfolio problems require different properties of the risk measure. We classify these models by the degree of positive homogeneity of the risk measure in the weights: degree one makes risk contributions add up to the portfolio risk and keeps diversification and reward-to-risk ratios scale invariant. For three thresholds, the portfolio mean, zero and a market-index return, we state a non-degeneracy condition on long-only downside risk under which the risk-parity, most-diversified and Sortino-ratio problems are well posed. Under this condition, the two ratio problems reduce to convex programs, and the differentiability of semivolatility ensures that the risk-budgeting formulation attains the prescribed budgets. We also characterize when below-mean semivolatility is additive. Finally, we provide an out-of-sample analysis on two real-world datasets of total returns, the current constituents of the Dow Jones and Nasdaq-100 indexes. We compare seventeen long-only strategies, covering the minimum-risk, reward-to-risk, risk-parity and most-diversified families, in a rolling-window backtest, and test the differences within each family by block-bootstrap inference.

</details>

### [Large-Scale Streaming Portfolio Optimization with Pauli Correlation Encoding](https://arxiv.org/abs/2611.32769)
*Vicente P. Soloviev, Josh Kirsopp* · `quant-ph` · arXiv:2611.32769v1 · relevance 0.06

- **In one sentence**: This paper extends Pauli Correlation Encoding (PCE), a qubit-efficient quantum-style clustering approach to portfolio selection, into a rolling-window streaming setting and compares PCE and a joint multi-cut variant (dPCE) against a Buy & Hold baseline on portfolios of up to several thousand assets.
- **In plain words**: Choosing which stocks to hold from a very large pool is a hard selection puzzle, and this paper tests a quantum-inspired method for it under conditions closer to real trading, where the data and the portfolio are updated repeatedly over time rather than set once. The authors report that both versions beat a simple buy-and-hold strategy, and that the main method, PCE, lost noticeably less than the baseline during a market downturn. They also say the joint variant, dPCE, becomes harder to run as the portfolio grows.
- **Why it matters**: Portfolio selection over thousands of assets is a practical problem for asset managers, and the paper checks a promising method against repeated rebalancing rather than a single snapshot. Its relevance to real quantum hardware is not established by the text, which describes the method as using far fewer qubits than assets but does not show results on actual quantum devices.
- **Background needed**: - Portfolio optimization: choosing asset weights to balance expected return against risk (risk aversion) and trading costs.
- Buy & Hold: a passive baseline that buys assets and keeps them without active rebalancing.
- Rolling window / streaming: re-estimating correlations and the portfolio repeatedly as new price data arrives.
- Clustering as selection: grouping correlated assets so that one representative per group can be chosen, shrinking the problem.
- Qubit: the basic unit of quantum computing; PCE encodes many assets into fewer qubits than one per asset.
- Measurement shots: the number of repeated quantum measurements used to estimate results; a shot budget is the cap on these repeats.
- Rebalancing cadence: how often the portfolio is adjusted. · level: research-level

<details><summary>Original abstract</summary>

Classical portfolio construction over large asset universes is a combinatorial selection problem that existing heuristics do not solve well at scale. Pauli Correlation Encoding (PCE) addresses this by representing the underlying clustering problem with far fewer qubits than one per asset, and a prior study showed it is competitive with classical methods on a single historical snapshot. This paper moves beyond that static test to a streaming deployment, in which the correlation structure and the portfolio are both re-estimated on a rolling basis, as a live rebalancing system would actually operate. We introduce two streaming variants -- PCE itself and a joint multi-cut variant, dPCE -- and evaluate both against a Buy & Hold baseline across window lengths, portfolio sizes up to several thousand assets, risk-aversion and transaction-cost settings, and measurement-shot budgets. Streaming PCE and dPCE consistently outperform the passive baseline, including during a market downturn where both lose money but PCE loses markedly less -- evidence that the method's value is not confined to rising markets. PCE also proves the more practical choice at scale, since dPCE's resource requirements and its sensitivity to rebalancing frequency both grow faster with portfolio size. We further report which operational choices -- rebalancing cadence, shot budget, and transaction-cost awareness -- matter most for a real deployment, and which matter less than commonly assumed.

</details>

## Signal processing

### [Score-Based Diffusion for Hypergraph Signals in the t-Spectral Domain](https://arxiv.org/abs/2611.33026)
*Zhiyuan Dong, Carlos Mundo-Levano, Daniel L. Lau et al.* · `cs.LG` · arXiv:2611.33026v1 · relevance 0.09

- **In one sentence**: A score-based diffusion generative model for signals living on a fixed hypergraph, built in the spectral domain of t-product hypergraph signal processing, with a per-mode frequency shift to keep the forward diffusion well-posed and a posterior-sampling method for recovering missing nodes.
- **In plain words**: The paper studies how to generate new realistic data values on a network where connections can join more than two nodes at once (a hypergraph). The authors convert the problem into a frequency-like representation, add a small shift so the noising process behaves properly, and train a small neural denoiser on that representation. They report that their method beats a simpler clique-expansion baseline on hypergraphs of up to 500 nodes and can fill in missing nodes with lower error than classical baselines.
- **Why it matters**: Many real systems, such as group interactions or multi-way relations, are better described by hypergraphs than by ordinary graphs, so generative tools for signals on them could matter for tasks like imputing missing data. The text reports numbers on its own benchmarks but does not show how it performs on real-world datasets or against stronger modern hypergraph methods, so its broader significance is unclear.
- **Background needed**: - Signal on a graph or hypergraph: a value attached to each node, such as a sensor reading or user attribute.
- Hypergraph: a network where an edge can link any number of nodes, not just two.
- Clique expansion: a common workaround that turns each hyperedge into ordinary pairwise edges, losing some structure.
- Spectral domain: describing a signal by its components along the network's natural vibration modes, analogous to frequencies.
- Diffusion model: a generative method that learns to reverse a gradual noising process; the "score" is the gradient of the log-probability that guides denoising.
- Ornstein-Uhlenbeck process: a mean-reverting random process whose noising has closed-form statistics.
- Posterior sampling / guidance: generating data consistent with partial observations, here used to fill in missing nodes.
- NMSE (normalized mean squared error): a scaled measure of reconstruction error where lower is better. · level: research-level

<details><summary>Original abstract</summary>

We introduce the first score-based generative model for signals on a fixed hypergraph, formulated in the spectral domain of t-product hypergraph signal processing (t-HGSP). The naive tensor heat semigroup is ill-posed, since after palindromic symmetrization the spectral slices of the Laplacian tensor are no longer positive semidefinite. A per-mode frequency shift repairs it, yielding a forward Ornstein-Uhlenbeck diffusion that decouples per (eigenmode, slice) pair with closed-form marginals, exact score targets, and an exactly isotropic stationary law. A lightweight slice-conditioned denoiser is trained on the resulting real spectral grid. Sampling combines its score on data-active modes with the closed-form score elsewhere, which proves essential for stability at scale. A closed cosine-form observation operator turns missing-node recovery into linear-Gaussian guidance with stabilized posterior sampling. On hypergraphs of up to 500 nodes, our model beats a clique-expansion baseline by margins growing from $2\times$ to $27\times$ in covariance error, matches the graph-spectral statistics of the data better than the graph-basis model itself, and reaches the finite-sample estimation floor on data rotated off the t-spectral axes. Posterior sampling reduces missing-node NMSE to 0.28-0.64 (classical baselines 0.87-1.1) at conservative coverage, and cuts the framework's own denoising baseline by up to $3.6\times$.

</details>

### [Multiple-Input Multiple-Output Forward Scatter Radar](https://arxiv.org/abs/2611.32546)
*Abdollah Ajorloo, Stefano Amato Ciciretti, Fabiola Colone* · `eess.SP` · arXiv:2611.32546v1 · relevance 0.09

- **In one sentence**: The paper proposes a multiple-input multiple-output forward scatter radar that jointly estimates target departure and arrival angles from amplitude-only measurements, using FDM and TDM multiplexing with analytical resolution and ambiguity results and outdoor software-defined-radio proof-of-concept tests.
- **In plain words**: Forward scatter radar detects objects that pass directly between a transmitter and a receiver, where they reflect strongly. This paper extends that idea to use arrays of antennas at both ends, so the system can estimate a target's position as two angles without needing the transmitter and receiver to be phase-synchronized. The authors describe the principle, two ways of separating the signals, simulations, and outdoor experiments with software-defined radios.
- **Why it matters**: Avoiding phase synchronization between distributed antennas could make radar-style sensing cheaper and easier to deploy, which may matter for integrated sensing and communications. The text reports simulations and outdoor proof-of-concept tests, but it is a limited demonstration, so the practical reach of the approach is not yet established.
- **Background needed**: - Radar: sends radio waves and infers objects from the echoes or signals they affect.
- Forward scatter radar: transmitter and receiver sit on opposite sides of an area; a target crossing the line between them scatters strongly, making it easier to detect.
- Radar cross section: how strongly an object reflects radio waves.
- SISO / SIMO / MIMO: single or multiple antennas at transmitter (input) and receiver (output).
- Direction of departure (DoD) and direction of arrival (DoA): the angles at which signals leave the transmitter array and reach the receiver array.
- Amplitude-only, non-coherent measurements: only signal strength is used, not its phase, so no precise timing or phase link between devices is needed.
- FDM / TDM: frequency-division or time-division multiplexing, ways of letting several transmit channels share the medium without interfering.
- Integrated sensing and communications: systems that use one set of radio hardware for both sensing and data transfer. · level: research-level

<details><summary>Original abstract</summary>

Forward Scatter Radar (FSR) enhances the detection of low-observable targets by exploiting the increased radar cross section that occurs when a target crosses the transmitter-receiver baseline. Conventional FSR typically uses single-input single-output (SISO) architectures with limited localization capability, while recent single-input multiple-output (SIMO) systems enable non-coherent angular estimation. This paper introduces a multiple-input multiple-output FSR (MIMO-FSR) framework for joint estimation of target direction of departure (DoD) and direction of arrival (DoA) from non-coherent, amplitude-only measurements. By exploiting antenna arrays at both the transmitter (TX) and receiver (RX), the proposed approach enables two-dimensional angular localization without phase synchronization among TX/RX array elements. We establish the underlying operating principle under ideal signal separability and then develop practical frequency-division multiplexing (FDM) and time-division multiplexing (TDM) implementations. For each scheme, dedicated signal models and processing methods compensate for distortions caused by frequency offsets and target motion, respectively. We also derive analytical expressions for angular resolution, ambiguity conditions, and output-map distortions. Extensive numerical simulations for short- and long-baseline scenarios reveal operational limits and trade-offs between the two multiplexing schemes. Finally, proof-of-concept outdoor experiments using software-defined radio platforms validate the proposed framework. The results demonstrate joint DoD-DoA estimation and support the feasibility of MIMO-FSR for future active, passive, and integrated sensing and communications applications.

</details>

## Audio and speech

### [Cif-query bridging for audio-native asr transfer to visual speech recognition](https://arxiv.org/abs/2611.32697)
*Chang Sun, Dongliang Xie, Wanpeng Xie et al.* · `cs.SD` · arXiv:2611.32697v1 · relevance 0.16

- **In one sentence**: A lightweight cross-attention bridge, driven by adaptive queries from a continuous integrate-and-fire predictor, connects a Paraformer visual speech recognition encoder to the pretrained Qwen3-ASR language decoder, reporting 7.97% CER on CMLR versus 11.78% for native Paraformer.
- **In plain words**: This paper is about reading speech from lip movements (video only, no sound) by reusing a model that was built for listening to audio. The lip-reading model produces many video frames, which do not fit neatly into the compact input the audio model expects, so the authors add a small connector that condenses the video into a shorter set of query points and refines them against the full frame sequence. On the CMLR test set, the reported character error rate drops from 11.78% for the original Paraformer system to 7.97% for the combined system.
- **Why it matters**: Transferring the strong language knowledge of audio speech models to silent lip reading is a practical route to better visual speech recognition, which matters for accessibility and noisy settings. The text reports ablations on bridge depth, projector initialization, adapter size and CTC supervision, but the evidence comes from one dataset (CMLR), so how far the gain generalizes is not established here.
- **Background needed**: - Visual speech recognition (VSR): transcribing speech from video of lips, without audio.
- Automatic speech recognition (ASR): converting speech to text; Qwen3-ASR is a pretrained audio model with a large language-model decoder.
- Paraformer: a non-autoregressive speech recognition architecture; its CIF (continuous integrate-and-fire) predictor estimates how many text tokens each stretch of input corresponds to.
- Cross-attention: a mechanism that lets one set of vectors look up and weigh information from another set.
- Character error rate (CER): share of characters transcribed wrongly; lower is better.
- CTC: a training loss that aligns input frames to output characters without explicit alignment labels. · level: research-level

<details><summary>Original abstract</summary>

Audio-native automatic speech recognition (ASR) models provide strong speech-language priors, but their compact acoustic interfaces are mismatched with long, frame-level visual features. We propose CIF-Query Bridge, a lightweight connection from a Paraformer visual speech recognition (VSR) encoder to Qwen3-ASR. The existing visual continuous integrate-and-fire (CIF) predictor produces an input-dependent number of token-rate queries; a two-layer cross-attention bridge refines them against the complete frame sequence, and a linear adapter feeds the pretrained ASR projector and decoder. This design preserves access to uncompressed visual context while avoiding direct autoregressive processing of hundreds of video frames. On CMLR, the complete visual-only transfer system achieves 7.97% character error rate, compared with 11.78% for native Paraformer under the same test split and scoring protocol---a 3.81-point absolute and 32.3% relative reduction. Controlled ablations characterize bridge depth, projector initialization, adapter capacity, and CTC supervision. The results show that CIF-derived adaptive queries provide a compact interface for transferring audio-native ASR capability to VSR.

</details>

### [SoundWeaver: Compositional Warm-Starting for Text-to-Audio Diffusion Serving](https://arxiv.org/abs/2603.07865)
*Ayush Barik, Sofia Stoica, Nikhil Sarda et al.* · `cs.SD` · arXiv:2603.07865v2 · relevance 0.07

- **In one sentence**: SoundWeaver is a training-free method that speeds up text-to-audio diffusion by warm-starting generation from a prompt-conditioned acoustic prior assembled from segments of cached audio clips, with an adaptive bandit choosing the skip depth per request.
- **In plain words**: Generating sound from a text description with modern diffusion models takes many slow refinement steps, which adds latency. This paper proposes reusing pieces of audio that were already generated earlier: it stitches segments from a small cache of about 1,000 clips into a starting point that matches the prompt, then begins the denoising process partway through instead of from pure static. The authors report speedups of 1.48 to 3.74 times across several backbone models, with quality said to improve.
- **Why it matters**: Cutting the number of model evaluations needed per clip matters for making generative audio practical in real-time or large-scale serving. The idea of reusing acoustic structure across requests, rather than treating each generation independently, may be of interest to people working on efficient inference and caching for generative models, though the text alone does not show how well it holds up outside the reported benchmarks.
- **Background needed**: - Diffusion models generate output by starting from random noise and removing it step by step; each step is a "neural function evaluation" (NFE), and fewer steps means faster generation.
- "Warm-starting" means beginning the process from a partly denoised state instead of pure noise, so fewer steps remain.
- Neural codecs are learned compressors that turn audio into compact numerical representations.
- A contextual bandit is an adaptive method that picks among options (here, how deep to skip) based on feedback from past choices.
- Training-free means the method works on existing pretrained models without any new training. · level: research-level

<details><summary>Original abstract</summary>

Text-to-audio (T2A) diffusion models generate high-quality audio but require tens of neural function evaluations (NFEs), resulting in substantial inference latency. Existing acceleration methods primarily optimize each generation trajectory independently, even when reusable acoustic structure exists in prior examples. We introduce SoundWeaver, the first training-free framework for compositional cross example acoustic reuse. Rather than generating from pure noise, SoundWeaver constructs a prompt-conditioned acoustic prior from segments distributed across cached audios and warm-starts diffusion from an intermediate noise level. We introduce an Acoustic Composition Graph (ACG), which uses neural codec representations and segment-level identification to identify candidate cross-cache transitions and structured path search to jointly optimize prompt relevance and acoustic continuity. We further establish a warm-start error bound showing how prior quality and diffusion SNR jointly govern the admissible skip depth, motivating an adaptive contextual-bandit Skip Gater that selects the warm-start level for each request. Across T2A diffusion backbones, SoundWeaver achieves 1.48-3.74x generation speedup with only a 1K-clip cache while improving generation quality.

</details>

## Control systems

### [Automated Design and Evaluation Pipeline for Optimal Control Transcriptions in Model Predictive Control](https://arxiv.org/abs/2611.32558)
*Fabio Schneider, Peter K\"otting, Renato Loureiro* · `eess.SY` · arXiv:2611.32558v1 · relevance 0.18

- **In one sentence**: An automated pipeline that uses Bayesian optimization to search over pseudospectral Legendre-Gauss-Radau transcription settings, including mesh configurations, to minimize user-defined computation-time or closed-loop performance metrics for Model Predictive Control, demonstrated on spacecraft on-orbit servicing scenarios.
- **In plain words**: Model Predictive Control is a method where a computer repeatedly plans the best next moves for a machine, but the planning can be too slow for real-time use. This paper describes a semi-automatic way to choose how that planning problem is set up so it runs faster or performs better, instead of relying on expert trial and error. The authors test it on spacecraft that move and control themselves while servicing other satellites in orbit.
- **Why it matters**: Slow onboard computation is a practical limit on using advanced control in fast or resource-limited systems, such as spacecraft. The text reports improvements in MPC performance in the spacecraft scenarios, but it does not give the size of those gains in the provided excerpt, so the scale of the benefit is unclear from this text alone.
- **Background needed**: - Model Predictive Control (MPC): at each time step, solve an optimization problem to pick control inputs over a short future horizon, then apply only the first step and repeat.
- Transcription: converting a continuous control problem into a finite set of equations a solver can handle.
- Pseudospectral / collocation methods: approximating a trajectory with polynomials evaluated at chosen points (the "mesh"); Legendre-Gauss-Radau is one such point pattern.
- Forward Euler and implicit collocation: simple versus higher-accuracy ways of stepping a system forward in time.
- Bayesian optimization: a strategy for tuning settings with expensive evaluations by building a model of how settings affect the outcome.
- Closed-loop performance: how well the controller actually performs when it is running on the system.
- On-orbit servicing: spacecraft performing tasks like inspecting, refueling, or repairing other spacecraft. · level: research-level

<details><summary>Original abstract</summary>

The computational burden of Model Predictive Control represents a bottleneck limiting its widespread deployment in real-time applications. The selection of the optimal control transcription strategy for a given MPC formulation is a key driver of computational efficiency. Identifying performant MPC transcriptions requires significant effort and domain knowledge. We propose an automated pipeline for the design and evaluation of performant optimal control transcriptions for a given MPC formulation. Custom multi-objective design metrics, such as computation time or closed-loop performance, can be specified and are minimized by the pipeline. As a transcription method, a pseudospectral Legendre-Gauss-Radau method is employed. We show that it incorporates forward Euler integration and implicit collocation methods of low and high order in one formulation, leveraging the pipeline to evaluate both numerical approaches. Furthermore, different mesh configurations can be parameterized. To identify the optimal configuration of the transcription, a Bayesian Optimization framework is applied. The pipelines improvements in MPC performance are demonstrated through On-Orbit Servicing scenarios involving spacecraft motion planning and closed-loop control.

</details>

### [From Safety-Driven Redundancy to Value-Driven Architecture: An ODD-Based Rationalization Framework for Level 4 Autonomous Vehicles](https://arxiv.org/abs/2611.32960)
*Tiago Sim\~ao Ferreira (Federal Institute of Minas Gerais - IFMG), Farzad Fallahi (University of Luxembourg)* · `eess.SY` · arXiv:2611.32960v1 · relevance 0.13

- **In one sentence**: An ODD-based, safety-constrained systems-engineering framework that screens and ranks architecture transformations (removal, relocation, reassignment, consolidation) for a generic synthetic Level 4 autonomous vehicle, using lifecycle-cost sensitivity and robust multiobjective Pareto analysis.
- **In plain words**: Self-driving cars need backup systems so they keep working safely when sensors, computers, power, or steering/braking parts fail, but those backups add cost and complexity. This paper proposes a method for trimming or rearranging a car's system design while first checking that every change still meets safety limits for the conditions the car is meant to operate in. The authors tested it on a made-up, generic car design, not a real product, and found that simply removing parts gave little room for savings, while moving and combining functions produced more safe options, with the best option cutting modeled lifecycle cost by 5.55%.
- **Why it matters**: Cost and validation effort are becoming central concerns as self-driving vehicles move toward mass production, so a structured way to tie design choices to operating conditions could be useful to engineers. The results depend on an illustrative cost model and synthetic parameters, so they show what the method can do rather than what a real vehicle would save.
- **Background needed**: - Level 4 autonomous vehicle: a car that drives itself without a human backup within a defined area or set of conditions.
- Operational Design Domain (ODD): the specific roads, weather, speeds and situations a self-driving system is designed to handle.
- Fault-tolerant architecture: a system layout that keeps essential functions running when some components fail.
- Redundancy: duplicate components kept as backups.
- Safety-feasibility gate: a check that rejects any design change that would break safety requirements; safety is treated as a hard pass/fail limit, not something to trade off against cost.
- Lifecycle cost: total cost over the product's life, including design, validation, integration and maintenance.
- Pareto analysis: finding designs where no option is better on one goal (e.g., cost) without being worse on another (e.g., performance); these are the "non-dominated" solutions.
- Ablation: testing a design by removing one component at a time to see its effect. · level: research-level

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
| Neuroscience | 88 | 83 | 2 |
| Genetics and genomics | 50 | 47 | 2 |
| Cell and molecular biology | 63 | 61 | 2 |
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
